"""cosmo_runs.py -- definitions and execution of every expansion-history fit (gates, T1, T2, sensitivities)."""
import os, sys, json, math, time, traceback
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cosmo, likelihoods as L
from sampler import AMSampler, chi2_min

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, "results_rebuild")
CHAINS = os.path.join(RES, "chains")
SEED = 20261030

PARNAMES = {"lcdm": ["Om", "h", "wb100"], "cpl": ["Om", "h", "wb100", "w0", "wa"],
            "law1": ["Om", "h", "wb100", "gam"], "t2b": ["Om", "h", "w0", "wa"]}
BOUNDS = {"Om": (0.1, 0.6), "h": (0.5, 0.9), "wb100": (1.8, 2.6), "w0": (-3.0, 1.0), "wa": (-3.0, 2.0),
          "gam": (0.0, 2.0)}
WIDTH = {"Om": 0.008, "h": 0.008, "wb100": 0.015, "w0": 0.06, "wa": 0.2, "gam": 0.03}
FID = {"Om": 0.31, "h": 0.68, "wb100": 2.24, "w0": -0.9, "wa": -0.3, "gam": 0.08}

# ------------------------------------------------------------------ run table
RUNS = {}
def _add(name, model, bao, cmb, sn, bbn=None, role=""):
    RUNS[name] = dict(model=model, bao=bao, cmb=cmb, sn=sn, bbn=bbn, role=role)

# validation gates
_add("G9a_lcdm_BAOstd", "lcdm", "std", None, None, role="gate G9-a")
_add("G9b_lcdm_CMB", "lcdm", None, "lcdm3", None, role="gate G9-b")
_add("G9c_cpl_BAOstd_CMB_D", "cpl", "std", "lcdm3", "D", role="gate G9-c")
# deciding T1 runs (T1-L1 and T1-Sign)
for sn in ("P", "D"):
    for mdl in ("lcdm", "law1", "cpl"):
        _add(f"T1_{mdl}_{sn}", mdl, "mod", "lcdm3", sn, role="T1 deciding")
    _add(f"T2A_{sn}", "cpl", "mod", "cond", sn, bbn="desi", role="T2-A deciding")
# sensitivity runs (NON-DECIDING)
for sn in ("P", "D"):
    _add(f"S_T2B_{sn}", "t2b", "mod", "cond", sn, bbn="desi", role="T2-B sensitivity")
    _add(f"S_T2A_cooke_{sn}", "cpl", "mod", "cond", sn, bbn="cooke", role="T2-A Cooke BBN sensitivity")
    _add(f"S_T2A_marg_{sn}", "cpl", "mod", "marg", sn, bbn="desi", role="T2-A marginal (R,lA) block sensitivity")
    _add(f"S_T2A_r0_{sn}", "cpl", "mod_r0", "cond", sn, bbn="desi", role="T2-A Lya r=0 sensitivity")
    _add(f"S_T2A_LyaStd_{sn}", "cpl", "std", "cond", sn, bbn="desi", role="T2-A unmodified Lya row sensitivity")
    for mdl in ("lcdm", "law1", "cpl"):
        _add(f"S_T1wcdm_{mdl}_{sn}", mdl, "mod", "wcdm3", sn, role="T1 wCDM CMB prior sensitivity")
        _add(f"S_T1r0_{mdl}_{sn}", mdl, "mod_r0", "lcdm3", sn, role="T1 Lya r=0 sensitivity")
        _add(f"S_T1LyaStd_{mdl}_{sn}", mdl, "std", "lcdm3", sn, role="T1 unmodified Lya row sensitivity")

_DATA_CACHE = {}


def _get(kind, key):
    k = (kind, key)
    if k not in _DATA_CACHE:
        if kind == "bao":
            _DATA_CACHE[k] = L.load_bao(key)
        elif kind == "cmb":
            _DATA_CACHE[k] = L.cmb_prior(key)
        elif kind == "sn":
            _DATA_CACHE[k] = L.load_pantheonplus() if key == "P" else L.load_dovekie()
    return _DATA_CACHE[k]


class Chi2:
    def __init__(self, cfg):
        self.cfg = cfg
        self.names = PARNAMES[cfg["model"]]
        self.bounds = [BOUNDS[n] for n in self.names]
        self.bao = _get("bao", cfg["bao"]) if cfg["bao"] else None
        self.cmb = _get("cmb", cfg["cmb"]) if cfg["cmb"] else None
        self.sn = _get("sn", cfg["sn"]) if cfg["sn"] else None
        self.bbn = L.BBN[cfg["bbn"]] if cfg["bbn"] else None

    def params(self, x):
        v = dict(zip(self.names, x))
        mdl = self.cfg["model"]
        if mdl == "t2b":
            v["wb100"] = 100.0 * v["h"] ** 2 / 19.0
        return v

    def in_prior(self, x):
        for xi, (lo, hi) in zip(x, self.bounds):
            if not (lo <= xi <= hi):
                return False
        v = self.params(x)
        if "w0" in v and not (v["w0"] + v["wa"] < 0.0):
            return False
        if not (BOUNDS["wb100"][0] <= v["wb100"] <= BOUNDS["wb100"][1]):
            return False
        return True

    def make_cosmo(self, x):
        v = self.params(x)
        mdl = self.cfg["model"]
        if mdl == "lcdm":
            return cosmo.Params(v["Om"], v["h"], v["wb100"] / 100.0)
        if mdl in ("cpl", "t2b"):
            return cosmo.Params(v["Om"], v["h"], v["wb100"] / 100.0, model="cpl", w0=v["w0"], wa=v["wa"])
        if mdl == "law1":
            return cosmo.Params(v["Om"], v["h"], v["wb100"] / 100.0, model="law1", gam=v["gam"])

    def parts(self, x):
        p = self.make_cosmo(x)
        if not np.isfinite(p.Ode) or p.Obc <= 0:
            return None
        d = cosmo.Distances(p)
        out = {}
        if self.bao is not None:
            out["bao"] = L.chi2_bao(p, d, cosmo.r_drag(p), self.bao)
        if self.cmb is not None:
            out["cmb"] = L.chi2_cmb(p, d, self.cmb)
        if self.sn is not None:
            out["sn"] = self.sn.chi2(d)
        if self.bbn is not None:
            out["bbn"] = ((p.ombh2 * 100.0 - self.bbn[0]) / self.bbn[1]) ** 2
        return out

    def __call__(self, x):
        x = np.asarray(x, float)
        if not self.in_prior(x):
            return 1e30
        try:
            pr = self.parts(x)
        except (FloatingPointError, ValueError, ZeroDivisionError):
            return 1e30
        if pr is None:
            return 1e30
        tot = sum(pr.values())
        return tot if np.isfinite(tot) else 1e30

    def logpost(self, x):
        c = self(x)
        return -0.5 * c if c < 1e29 else -np.inf


def summarize(names, flat):
    s = {}
    for k, n in enumerate(names):
        v = flat[:, k]
        q = np.percentile(v, [2.5, 16, 50, 84, 97.5])
        s[n] = dict(mean=float(v.mean()), sd=float(v.std(ddof=1)), q025=float(q[0]), q16=float(q[1]),
                    median=float(q[2]), q84=float(q[3]), q975=float(q[4]))
    return s


def run_one(name):
    import psutil
    try:
        psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    np.seterr(all="ignore")
    cosmo.load_rd_calibration(os.path.join(RES, "validation", "rd_calibration.json"))
    cfg = RUNS[name]
    idx = sorted(RUNS).index(name)
    seed = SEED + 1000 * idx
    rng = np.random.default_rng(seed)
    logf = open(os.path.join(CHAINS, f"{name}.log"), "w")
    def log(s):
        logf.write(s + "\n"); logf.flush()
    t0 = time.time()
    log(f"run {name} cfg={cfg} seed={seed} start={time.strftime('%Y-%m-%dT%H:%M:%S')}")
    f = Chi2(cfg)
    names = f.names
    d = len(names)
    # crude mode search for starting points (Nelder-Mead from the fiducial point)
    from scipy.optimize import minimize
    x0 = np.array([FID[n] for n in names])
    best = minimize(f, x0, method="Nelder-Mead", options={"xatol": 1e-4, "fatol": 1e-3, "maxiter": 4000})
    xm = best.x
    log(f"  start mode {xm} chi2={best.fun:.3f}")
    widths = np.array([WIDTH[n] for n in names])
    starts = []
    while len(starts) < 8:
        s = xm + 2.0 * widths * rng.standard_normal(d)
        if np.isfinite(f.logpost(s)):
            starts.append(s)
    sam = AMSampler(f.logpost, d, rng, nchains=8)
    chains, lp, diag = sam.run(starts, np.diag(widths ** 2), log=log)
    flat = chains.reshape(-1, d)
    chi2flat = -2.0 * lp.reshape(-1)
    # derived quantities
    der = {}
    v = {n: flat[:, k] for k, n in enumerate(names)}
    if cfg["model"] == "t2b":
        v["wb100"] = 100 * v["h"] ** 2 / 19
    Onu = cosmo.M_NU / (cosmo.NU93 * v["h"] ** 2)
    der["Obc"] = v["Om"] - Onu
    if cfg["model"] == "law1":
        der["w0_fit"] = -1 + v["gam"]
        der["wa_fit_tangent"] = -1.5 * v["gam"] * (v["Om"] + v["gam"] * (1 - v["Om"]))
    if cfg["model"] == "t2b":
        der["wb100"] = v["wb100"]
    dnames = list(der)
    dflat = np.column_stack([der[k] for k in dnames]) if dnames else np.zeros((len(flat), 0))
    summ = summarize(names, flat)
    summ.update(summarize(dnames, dflat))
    if "w0" in names:
        k = names.index("w0")
        summ["P_w0_gt_m1"] = float(np.mean(flat[:, k] > -1.0))
    # chi2_min (registered optimiser procedure)
    cmin, xbest, trials = chi2_min(f, flat, chi2flat, f.bounds)
    parts = f.parts(xbest)
    res = dict(name=name, cfg=cfg, seed=seed, params=names, derived=dnames, summary=summ, diagnostics=diag,
               chi2_min=cmin, x_best=list(map(float, xbest)), chi2_parts_best={k: float(v_) for k, v_ in parts.items()},
               optimizer_trials=trials, runtime_s=time.time() - t0,
               n_data=dict(sn=(f.sn.N if f.sn else 0), bao=(len(f.bao["z"]) if f.bao else 0)))
    np.savez_compressed(os.path.join(CHAINS, f"{name}.npz"), chains=chains.astype(np.float64), lp=lp,
                        names=np.array(names))
    json.dump(res, open(os.path.join(CHAINS, f"{name}.json"), "w"), indent=1, default=float)
    log(f"done chi2_min={cmin:.4f} at {xbest} runtime {time.time() - t0:.0f}s converged={diag['converged_final']}")
    logf.close()
    return name


def run_many(names, ncores):
    import multiprocessing as mp
    os.makedirs(CHAINS, exist_ok=True)
    todo = [n for n in names if not os.path.exists(os.path.join(CHAINS, f"{n}.json"))]
    # longest (law1) first
    todo.sort(key=lambda n: (RUNS[n]["model"] != "law1", n))
    print(f"{len(todo)} runs to do on {ncores} cores")
    with mp.get_context("spawn").Pool(min(ncores, max(1, len(todo)))) as pool:
        for r in pool.imap_unordered(_safe_run, todo):
            print(time.strftime("%H:%M:%S"), "finished", r, flush=True)


def _safe_run(name):
    try:
        return run_one(name)
    except Exception:
        return name + " FAILED: " + traceback.format_exc()


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    ncores = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    if which == "all":
        sel = list(RUNS)
    elif which == "deciding":
        sel = [n for n in RUNS if not n.startswith("S_")]
    elif which == "sens":
        sel = [n for n in RUNS if n.startswith("S_")]
    else:
        sel = which.split(",")
    run_many(sel, ncores)
