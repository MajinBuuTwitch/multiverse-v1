"""t5.py -- rotation-curve tests T5-A, T5-B, T5c and gate G9-d (own code from PREREG §5.6 / EQUATIONS (f3))."""
import os, sys, json, math, time
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
from scipy.special import erf
from scipy.interpolate import PchipInterpolator
from scipy.optimize import minimize_scalar
from scipy.integrate import quad

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "sparc")
RES = os.path.join(ROOT, "results_rebuild")
G_KPC = 4.30091727e-6        # kpc (km/s)^2 / Msun
SEED = 20261030
SQ2PI = math.sqrt(2.0 * math.pi)


# ------------------------------------------------------------------ registered kernel (closed form)
def F_kernel(r, rp, sigma):
    """Fraction of a unit point/shell mass at radius rp, smeared by an isotropic 3D Gaussian of width sigma,
    enclosed within radius r.  Broadcasts over r, rp."""
    r = np.asarray(r, float); rp = np.asarray(rp, float)
    r, rp = np.broadcast_arrays(r, rp)
    s = sigma
    out = np.empty(r.shape)
    big = rp / s >= 1e-4
    rb, pb = r[big], rp[big]
    out[big] = 0.5 * (erf((rb + pb) / (math.sqrt(2) * s)) + erf((rb - pb) / (math.sqrt(2) * s))) \
        - (1.0 / SQ2PI) * (s / pb) * (np.exp(-(rb - pb) ** 2 / (2 * s * s)) - np.exp(-(rb + pb) ** 2 / (2 * s * s)))
    rs = r[~big]
    out[~big] = erf(rs / (math.sqrt(2) * s)) - math.sqrt(2.0 / math.pi) * (rs / s) * np.exp(-rs ** 2 / (2 * s * s))
    return out


def gate_G9d():
    """Registered 5x7 grid vs scipy.stats.ncx2.cdf, abs tol < 1e-10; plus independent Monte Carlo check."""
    import numpy, scipy
    from scipy.stats import ncx2, chi2
    rr = [0.2, 0.5, 1.0, 2.0, 4.0]
    pp = [0.0, 1e-5, 0.2, 0.5, 1.0, 2.0, 4.0]
    rows, maxdiff, fallback = [], 0.0, []
    for x in rr:
        for y in pp:
            mine = float(F_kernel(x, y, 1.0))
            try:
                ref = float(ncx2.cdf(x ** 2, df=3, nc=y ** 2))
                if not np.isfinite(ref):
                    raise ValueError
            except Exception:
                ref = float(chi2.cdf(x ** 2, 3)); fallback.append((x, y))
            dd = abs(mine - ref)
            maxdiff = max(maxdiff, dd)
            rows.append(dict(r_over_sigma=x, rp_over_sigma=y, F=mine, ncx2=ref, absdiff=dd))
    # direct 3D Monte Carlo (independent validation route, REBUILD_RULES)
    rng = np.random.default_rng(SEED)
    N = 2_000_000
    mc = []
    for (r, rp, s) in [(1.0, 1.0, 1.0), (2.0, 1.0, 1.5), (0.5, 2.0, 1.0), (3.0, 0.5, 2.0), (1.0, 0.0, 1.0), (4.0, 4.0, 1.0)]:
        pts = rng.standard_normal((N, 3)) * s
        pts[:, 2] += rp
        inside = (np.einsum("ij,ij->i", pts, pts) <= r * r)
        m, se = inside.mean(), inside.std(ddof=1) / math.sqrt(N)
        f = float(F_kernel(r, rp, s))
        mc.append(dict(r=r, rp=rp, sigma=s, F=f, mc=float(m), mc_se=float(se), z=float((m - f) / se)))
    res = dict(numpy=numpy.__version__, scipy=scipy.__version__, grid=rows, max_abs_diff=maxdiff,
               tolerance=1e-10, nc0_fallback=fallback,
               PASS=bool(maxdiff < 1e-10 and numpy.__version__ == "2.5.4" and scipy.__version__ == "1.18.1"),
               monte_carlo=mc, mc_max_abs_z=max(abs(m["z"]) for m in mc))
    return res


# ------------------------------------------------------------------ SPARC data
def load_sparc():
    """Parse MassModels_Lelli2016c.mrt (fixed-width, byte-by-byte description in the header) and
    SPARC_Lelli2016c.mrt (galaxy table with Rdisk, Q, Inc)."""
    mm = {}
    lines = open(os.path.join(DATA, "MassModels_Lelli2016c.mrt")).read().splitlines()
    # data lines start after the last line of dashes
    dash = [i for i, l in enumerate(lines) if l.startswith("-----")]
    for l in lines[dash[-1] + 1:]:
        if not l.strip():
            continue
        p = l.split()
        gid = l[0:11].strip()
        vals = [float(v) for v in p[1:]]
        D, R, Vobs, eV, Vgas, Vdisk, Vbul, SBdisk, SBbul = vals[:9]
        mm.setdefault(gid, []).append((R, Vobs, eV, Vgas, Vdisk, Vbul, SBdisk, SBbul, D))
    gal = {}
    lines = open(os.path.join(DATA, "SPARC_Lelli2016c.mrt")).read().splitlines()
    dash = [i for i, l in enumerate(lines) if l.startswith("-----")]
    for l in lines[dash[-1] + 1:]:
        if not l.strip():
            continue
        gid = l[0:11].strip()
        # whitespace-separated (galaxy names contain no blanks; the byte columns in the header are offset by
        # one in this file): Galaxy T D e_D f_D Inc e_Inc L e_L Reff SBeff Rdisk SBdisk MHI RHI Vflat e_Vflat Q Ref
        p = l.split()
        assert p[0] == gid
        gal[gid] = dict(T=int(p[1]), D=float(p[2]), Inc=float(p[5]), Rdisk=float(p[11]), Q=int(p[17]))
    out = {}
    for gid, rows in mm.items():
        a = np.array(rows)
        out[gid] = dict(R=a[:, 0], Vobs=a[:, 1], eV=a[:, 2], Vgas=a[:, 3], Vdisk=a[:, 4], Vbul=a[:, 5],
                        SBdisk=a[:, 6], SBbul=a[:, 7], **gal[gid])
    return out


def split_sparc(gals):
    ids = sorted(g.strip() for g in gals)         # Python byte-wise ASCII sort on stripped ids
    train = ids[0::2]                              # odd positions 1,3,5,... (1-indexed)
    test = ids[1::2]
    return ids, train, test


class Galaxy:
    """Precomputes everything that does not depend on sigma."""

    def __init__(self, g):
        self.R = g["R"]; self.Vobs = g["Vobs"]; self.eV = g["eV"]; self.Rd = g["Rdisk"]
        v2 = g["Vgas"] * np.abs(g["Vgas"]) + 0.5 * g["Vdisk"] ** 2 + 0.7 * g["Vbul"] ** 2
        Mraw = self.R * v2 / G_KPC
        self.Mmono = np.maximum.accumulate(np.maximum(0.0, Mraw))
        r1, rmax = self.R[0], self.R[-1]
        lin = np.linspace(0.0, r1, 201)[:-1]                 # 200 linear nodes on [0, r1)
        lg = np.geomspace(r1, rmax, 200)                     # 200 log nodes on [r1, rmax]
        nodes = np.concatenate([lin, lg])                    # 400 distinct nodes, 0 ... rmax
        assert len(np.unique(nodes)) == 400
        M = np.empty_like(nodes)
        core = nodes < r1
        M[core] = self.Mmono[0] * (nodes[core] / r1) ** 3
        if len(self.R) >= 2:
            M[~core] = PchipInterpolator(self.R, self.Mmono)(nodes[~core])
        else:
            M[~core] = self.Mmono[0]
        self.dM_int = np.diff(M)
        self.rmid_int = 0.5 * (nodes[:-1] + nodes[1:])
        self.rmax = rmax
        self.Sig_tail = 1e6 * (0.5 * g["SBdisk"][-1] + 0.7 * g["SBbul"][-1])     # Msun / kpc^2
        self.N = len(self.R)
        self.Rq = None

    def vmodel(self, sigma, Rfac):
        """Rfac = 6 (1 - f_leak)."""
        dr = 5.0 * sigma / 100.0
        edges = self.rmax + dr * np.arange(101)
        rmid_t = 0.5 * (edges[:-1] + edges[1:])
        if self.Rd > 0:
            dM_t = 2 * math.pi * rmid_t * self.Sig_tail * np.exp(-(rmid_t - self.rmax) / self.Rd) * dr
        else:
            dM_t = np.zeros_like(rmid_t)
        rp = np.concatenate([self.rmid_int, rmid_t])
        dM = np.concatenate([self.dM_int, dM_t])
        Fm = F_kernel(self.R[:, None], rp[None, :], sigma)
        Msh = Rfac * (Fm @ dM)
        return np.sqrt(G_KPC * (self.Mmono + Msh) / self.R), Msh

    def chi2(self, sigma, Rfac):
        v, _ = self.vmodel(sigma, Rfac)
        return float(np.sum(((self.Vobs - v) / self.eV) ** 2))


def train_scan(gals, Rfac, mode, objective="sum_red", grid=None):
    """mode 'A': sigma in kpc; 'B': sigma_g = k * Rd_g.  Returns grid, objective values, refined optimum."""
    lo, hi = (0.1, 100.0) if mode == "A" else (0.05, 50.0)
    grid = np.geomspace(lo, hi, 200)

    def obj(par):
        vals = []
        for g in gals:
            s = par if mode == "A" else par * g.Rd
            c = g.chi2(s, Rfac)
            vals.append(c / g.N if objective in ("sum_red", "median_red") else c)
        vals = np.array(vals)
        if objective == "median_red":
            return float(np.median(vals))
        return float(vals.sum())

    L = np.array([obj(x) for x in grid])
    i = int(np.argmin(L))
    a, b = grid[max(i - 1, 0)], grid[min(i + 1, len(grid) - 1)]
    r = minimize_scalar(obj, bounds=(a, b), method="bounded", options={"xatol": 1e-5})
    best = float(r.x) if r.fun <= L[i] else float(grid[i])
    return dict(grid=grid.tolist(), L=L.tolist(), grid_argmin=float(grid[i]), bracket=[float(a), float(b)],
                best=best, L_best=float(min(r.fun, L[i])))


def evaluate(gals, ids, par, Rfac, mode):
    out = {}
    for gid, g in zip(ids, gals):
        s = par if mode == "A" else par * g.Rd
        out[gid] = g.chi2(s, Rfac) / g.N
    v = np.array(list(out.values()))
    M = float(np.median(v)); F2 = float(np.mean(v < 2.0))
    if M <= 1.5 and F2 >= 0.70:
        verdict = "PASS"
    elif M > 3.0 or F2 < 0.40:
        verdict = "FAIL"
    else:
        verdict = "INCONCLUSIVE"
    return dict(chi2_red=out, median=M, frac_lt2=F2, n=len(v), verdict=verdict)


def t5c(sigma, Rfac):
    Mstar, Re = 2.0e8, 2.2
    d3 = math.sqrt(1.5) * 80.0
    def Mb(r):
        return Mstar * r ** 3 / (r * r + Re * Re) ** 1.5
    def dMb(rp):
        return Mstar * 3 * Re * Re * rp * rp / (rp * rp + Re * Re) ** 2.5
    res = {}
    for r in (2.7, 3.1, 7.6):
        Msh = Rfac * quad(lambda rp: float(F_kernel(r, rp, sigma)) * dMb(rp), 0, np.inf, limit=400,
                          epsabs=0, epsrel=1e-10)[0]
        Mgrp = Rfac * 1.0e11 * float(F_kernel(r, d3, sigma))
        res[str(r)] = dict(Mb=Mb(r), Msh_DF2=Msh, Msh_group=Mgrp, Mpred=Mb(r) + Msh + Mgrp)
    m27, m31 = res["2.7"]["Mpred"], res["3.1"]["Mpred"]
    if m27 > 3.7e8:
        verdict = "FAIL"
    elif m27 <= 2.9e8 and m31 < 3.2e8:
        verdict = "PASS"
    else:
        verdict = "INCONCLUSIVE"
    return dict(sigma_ref=sigma, Rfac=Rfac, masses=res, verdict=verdict)
