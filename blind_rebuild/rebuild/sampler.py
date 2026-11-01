"""sampler.py -- own MCMC sampler + convergence diagnostics + chi2_min optimiser.

Sampler (rebuild's own choice, logged in REBUILD_RESULTS.md): multi-chain random-walk Metropolis with a
Gaussian proposal whose covariance is learned during an adaptive phase (Haario et al. 2001 style) and then
FROZEN, so the production chains are exactly Markov / reversible.  8 independent chains started from
dispersed points; genuine between-chain Gelman-Rubin diagnostics are therefore available.
Convergence (registered): Gelman-Rubin R-1 < 0.01 (both classic split-R and rank-normalised split-R, Vehtari
et al. 2021) and bulk ESS > 1000 per parameter; burn-in >= max(1000, 5 tau) steps per chain; production
>= 128,000 samples in total (registered production minimum).  Maximum extension: 80,000 production steps/chain.
"""
import math
import numpy as np
from scipy.stats import norm, rankdata
from scipy.optimize import minimize


# ------------------------------------------------------------------ diagnostics
def _split(chains):
    m, n = chains.shape
    h = n // 2
    return np.vstack([chains[:, :h], chains[:, h:2 * h]])


def rhat_classic(chains):
    c = _split(chains)
    m, n = c.shape
    W = c.var(axis=1, ddof=1).mean()
    B = n * c.mean(axis=1).var(ddof=1)
    var = (n - 1) / n * W + B / n
    return math.sqrt(var / W)


def rhat_rank(chains):
    """rank-normalised split-R (bulk) and folded (tail) version; returns max."""
    c = _split(chains)
    def z(x):
        r = rankdata(x.ravel()).reshape(x.shape)
        return norm.ppf((r - 0.375) / (x.size + 0.25))
    zb = z(c)
    zf = z(np.abs(c - np.median(c)))
    return max(rhat_classic_unsplit(zb), rhat_classic_unsplit(zf))


def rhat_classic_unsplit(c):
    m, n = c.shape
    W = c.var(axis=1, ddof=1).mean()
    B = n * c.mean(axis=1).var(ddof=1)
    var = (n - 1) / n * W + B / n
    return math.sqrt(var / W)


def _autocov(x):
    n = len(x)
    f = np.fft.rfft(x - x.mean(), n=2 * n)
    ac = np.fft.irfft(f * np.conj(f))[:n]
    return ac / n


def ess_bulk(chains):
    """multi-chain ESS (Geyer initial monotone sequence, Stan convention) on rank-normalised split chains."""
    c = _split(chains)
    r = rankdata(c.ravel()).reshape(c.shape)
    c = norm.ppf((r - 0.375) / (c.size + 0.25))
    m, n = c.shape
    acov = np.array([_autocov(ci) for ci in c])
    chain_var = acov[:, 0] * n / (n - 1)
    W = chain_var.mean()
    B = n * c.mean(axis=1).var(ddof=1)
    var_plus = (n - 1) / n * W + B / n
    rho = 1.0 - (W - acov.mean(axis=0)) / var_plus
    rho[0] = 1.0
    # Geyer: sum pairs while positive, enforce monotone
    t = 0
    P = []
    while 2 * t + 1 < n:
        s = rho[2 * t] + rho[2 * t + 1]
        if s < 0:
            break
        P.append(s)
        t += 1
    P = np.minimum.accumulate(np.array(P))
    tau = -1.0 + 2.0 * P.sum()
    tau = max(tau, 1.0 / math.log10(m * n))
    return m * n / tau


def tau_int(x):
    """integrated autocorrelation time of a single 1-D chain (Sokal window, c=5)."""
    ac = _autocov(x)
    rho = ac / ac[0]
    taus = 2.0 * np.cumsum(rho) - 1.0
    for M in range(1, len(taus)):
        if M >= 5 * taus[M]:
            return taus[M]
    return taus[-1]


# ------------------------------------------------------------------ sampler
class AMSampler:
    def __init__(self, logpost, ndim, rng, nchains=8):
        self.lp, self.d, self.rng, self.m = logpost, ndim, rng, nchains

    def _run_fixed(self, x, lpx, L, nsteps, store=True):
        d = self.d
        out = np.empty((nsteps, d)) if store else None
        outlp = np.empty(nsteps) if store else None
        acc = 0
        for t in range(nsteps):
            y = x + L @ self.rng.standard_normal(d)
            lpy = self.lp(y)
            if math.log(self.rng.random()) < lpy - lpx:
                x, lpx = y, lpy
                acc += 1
            if store:
                out[t] = x; outlp[t] = lpx
        return x, lpx, out, outlp, acc / nsteps

    def run(self, starts, init_cov, n_adapt=4000, n_burn=3000, block=4000, min_prod_total=128000,
            max_prod=80000, log=print):
        d, m = self.d, self.m
        sd = 2.38 ** 2 / d
        xs = [np.array(s, float) for s in starts]
        lps = [self.lp(x) for x in xs]
        # ---- adaptive phase (per-chain Haario AM, covariance updated every 200 steps)
        hist = [[] for _ in range(m)]
        covs = [np.array(init_cov, float) for _ in range(m)]
        for c in range(m):
            L = np.linalg.cholesky(covs[c] * sd)
            for t0 in range(0, n_adapt, 200):
                xs[c], lps[c], ch, _, _ = self._run_fixed(xs[c], lps[c], L, 200)
                hist[c].append(ch)
                H = np.vstack(hist[c])
                if len(H) >= 600:
                    Cn = np.cov(H[len(H) // 2:].T) + 1e-12 * np.eye(d)
                    try:
                        L = np.linalg.cholesky(Cn * sd)
                    except np.linalg.LinAlgError:
                        pass
        pooled = np.vstack([np.vstack(h)[n_adapt // 2:] for h in hist])
        Cfix = np.cov(pooled.T) + 1e-14 * np.eye(d)
        # step-size tuning (fixed afterwards): target acceptance 0.2-0.35 using short trial runs
        scale = sd
        for _ in range(6):
            L = np.linalg.cholesky(Cfix * scale)
            accs = []
            for c in range(m):
                xs[c], lps[c], _, _, a = self._run_fixed(xs[c], lps[c], L, 300, store=False)
                accs.append(a)
            a = float(np.mean(accs))
            if 0.2 <= a <= 0.35:
                break
            scale *= math.exp(2.0 * (a - 0.27))
        L = np.linalg.cholesky(Cfix * scale)
        log(f"  adapt done: acceptance {a:.3f}, scale {scale:.3f}")
        # ---- burn-in with frozen proposal
        for c in range(m):
            xs[c], lps[c], _, _, _ = self._run_fixed(xs[c], lps[c], L, n_burn, store=False)
        # ---- production in blocks
        prod = [[] for _ in range(m)]
        prodlp = [[] for _ in range(m)]
        accs = np.zeros(m)
        nprod = 0
        diag = None
        while True:
            for c in range(m):
                xs[c], lps[c], ch, chlp, a = self._run_fixed(xs[c], lps[c], L, block)
                prod[c].append(ch); prodlp[c].append(chlp); accs[c] = a
            nprod += block
            chains = np.array([np.vstack(p) for p in prod])          # (m, n, d)
            # extra burn-in so that total burn-in >= max(1000, 5 tau)
            taus0 = [np.mean([tau_int(chains[c, :, k]) for c in range(m)]) for k in range(d)]
            extra = int(max(0, math.ceil(5 * max(taus0)) - n_burn))
            trimmed = chains[:, extra:, :]
            diag = self.diagnostics(trimmed, n_burn + extra)
            log(f"  prod {nprod}/chain (extra burn {extra}): Rmax-1={diag['rhat_max'] - 1:.4f} "
                f"ESSmin={diag['ess_min']:.0f} tau_max={diag['tau_max']:.1f} acc={accs.mean():.3f}")
            if (diag["converged"] and (nprod - extra) * m >= min_prod_total) or nprod >= max_prod:
                break
        lpall = np.array([np.concatenate(p) for p in prodlp])[:, extra:]
        chains = trimmed
        diag["acceptance"] = float(accs.mean())
        diag["n_prod_per_chain"] = nprod - extra
        diag["n_adapt"] = n_adapt
        diag["proposal_scale"] = scale
        diag["production_min_met"] = bool((nprod - extra) * m >= min_prod_total)
        diag["converged_final"] = bool(diag["converged"] and diag["production_min_met"])
        return chains, lpall, diag

    @staticmethod
    def diagnostics(chains, n_burn):
        m, n, d = chains.shape
        rc = [rhat_classic(chains[:, :, k]) for k in range(d)]
        rr = [rhat_rank(chains[:, :, k]) for k in range(d)]
        es = [ess_bulk(chains[:, :, k]) for k in range(d)]
        taus = [np.mean([tau_int(chains[c, :, k]) for c in range(m)]) for k in range(d)]
        rmax = max(max(rc), max(rr))
        burn_ok = n_burn >= max(1000, 5 * max(taus))
        return dict(rhat_classic=rc, rhat_rank=rr, ess_bulk=es, tau=taus, rhat_max=rmax,
                    ess_min=min(es), tau_max=max(taus), burn_ok=bool(burn_ok), n_burn=n_burn,
                    converged=bool(rmax - 1 < 0.01 and min(es) > 1000 and burn_ok))


# ------------------------------------------------------------------ chi2_min (registered procedure)
def chi2_min(chi2fun, samples, chi2_samples, bounds, n_starts=5):
    """Nelder-Mead (xatol=fatol=1e-6, maxiter=10000) from the 5 highest-likelihood MCMC samples,
    then bounded L-BFGS-B polish (ftol=1e-12).  Returns best (chi2, x) and all trials."""
    order = np.argsort(chi2_samples)
    starts, seen = [], set()
    for i in order:
        key = tuple(np.round(samples[i], 12))
        if key in seen:
            continue
        seen.add(key); starts.append(samples[i])
        if len(starts) == n_starts:
            break
    trials = []
    best = (np.inf, None)
    for s in starts:
        r1 = minimize(chi2fun, s, method="Nelder-Mead",
                      options={"xatol": 1e-6, "fatol": 1e-6, "maxiter": 10000})
        x1 = r1.x
        r2 = minimize(chi2fun, x1, method="L-BFGS-B", bounds=bounds, options={"ftol": 1e-12})
        cand = [(r1.fun, x1), (r2.fun, r2.x)]
        f, x = min(cand, key=lambda t: t[0])
        trials.append(dict(start=list(map(float, s)), nm_chi2=float(r1.fun), lbfgsb_chi2=float(r2.fun),
                           x=list(map(float, x))))
        if f < best[0]:
            best = (float(f), np.array(x))
    return best[0], best[1], trials
