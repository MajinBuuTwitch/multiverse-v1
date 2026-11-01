"""t4b.py -- T4b age-cutoff test (PREREG §5.5), own code."""
import os, json, math
import numpy as np
from scipy.stats import binom
from scipy.integrate import quad

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = 20261030


def DA_flat_lcdm(z, H0=67.36, Om=0.315):
    c = 299792.458
    chi = quad(lambda x: 1.0 / math.sqrt(Om * (1 + x) ** 3 + 1 - Om), 0, z, epsrel=1e-10)[0]
    return c / H0 * chi / (1 + z)          # Mpc


def sigma_1d(err_axes):
    a, b = err_axes
    return math.sqrt(0.5 * (a * a + b * b))


def classify(c):
    """returns (class, details) using the registered rule; positions in arcmin (consistent units)."""
    if c.get("status") != "complete":
        return "unclassified", dict(reason=c["status"])
    I, G, S = (np.array(c[k]["xy"], float) for k in "IGS")
    sI, sG, sS = (sigma_1d(c[k]["err_axes"]) for k in "IGS")
    kpc_per_arcmin = DA_flat_lcdm(c["z_cl"]) * 1e3 * math.radians(1.0 / 60.0)
    dIG = float(np.linalg.norm(I - G)) * kpc_per_arcmin
    dIS = float(np.linalg.norm(I - S)) * kpc_per_arcmin
    sd = math.sqrt(sI ** 2 + sG ** 2 + sS ** 2) * kpc_per_arcmin
    if dIS - dIG > 2 * sd:
        cl = "dark mass with gas"
    elif dIG - dIS > 2 * sd:
        cl = "dark mass with galaxies"
    else:
        cl = "unclassified"
    return cl, dict(d_IG_kpc=dIG, d_IS_kpc=dIS, sigma_I_kpc=sI * kpc_per_arcmin, sigma_G_kpc=sG * kpc_per_arcmin,
                    sigma_S_kpc=sS * kpc_per_arcmin, sigma_diff_kpc=sd, kpc_per_arcmin=kpc_per_arcmin,
                    margin_over_2sigma=(abs(dIG - dIS) / (2 * sd)))


def predicted(tp_gyr, tau_myr):
    return "dark mass with galaxies" if tp_gyr * 1000.0 < tau_myr else "dark mass with gas"


def accuracy(items, tau):
    if not items:
        return 0.0
    return float(np.mean([predicted(c["tp"], tau) == c["class"] for c in items]))


def run(table, label="deciding"):
    cls = []
    for c in table["clusters"]:
        k, det = classify(c)
        cls.append(dict(row=c["row"], designation=c["designation"], tp=c["tp"], sig_tp=c["sig_tp"],
                        half=("train" if c["row"] % 2 == 1 else "test"), **{"class": k}, details=det,
                        paper=c["paper"], pointer=c["pointer"]))
    # registered byte-wise ASCII sort check: odd positions = training
    names = [c["designation"] for c in table["clusters"]]
    srt = sorted(names)
    assert srt == names, "table order must equal byte-wise sorted designations"
    train = [c for c in cls if c["half"] == "train" and c["class"] != "unclassified"]
    test = [c for c in cls if c["half"] == "test" and c["class"] != "unclassified"]
    grid = np.arange(235, 1500 + 1e-9, 5.0)
    if len(train) == 0:
        acc_tr = np.zeros_like(grid)
    else:
        acc_tr = np.array([accuracy(train, t) for t in grid])
    imax = int(np.argmax(acc_tr))           # first index = smallest tau among ties
    tau_hat = float(grid[imax]); acc_train_max = float(acc_tr[imax])
    n_tr, n_te = len(train), len(test)
    acc_test = accuracy(test, tau_hat) if n_te > 0 else float("nan")
    k_obs = int(round(acc_test * n_te)) if n_te > 0 else 0
    p_t4b = float(binom.sf(k_obs - 1, n_te, 0.5)) if n_te > 0 else 1.0
    fail_a = (n_tr == 0) or (acc_train_max < 0.80)
    fail_b = (n_te >= 6) and (acc_test < 0.60)
    old = [c for c in test if c["tp"] >= 1.0]
    fail_c = (n_te >= 6) and all(c["class"] == "dark mass with galaxies" for c in test) and len(old) > 0
    if fail_a or fail_b or fail_c:
        raw = "FAIL"
    elif n_te >= 6 and acc_test >= 0.80:
        raw = "PASS (raw, before Holm)"
    else:
        raw = "INCONCLUSIVE"
    p_for_holm = p_t4b if (n_te >= 6) else 1.0           # edge-case rule: n_test < 6 -> p = 1
    # NON-DECIDING: Monte Carlo age-posterior-weighted accuracy (Gaussian t_p, truncated at 0)
    rng = np.random.default_rng(SEED)
    mc = {}
    for nm, items in (("train", train), ("test", test)):
        if not items:
            mc[nm] = None
            continue
        draws = []
        for _ in range(20000):
            ok = []
            for c in items:
                t = -1
                while t < 0:
                    t = rng.normal(c["tp"], c["sig_tp"])
                ok.append(predicted(t, tau_hat) == c["class"])
            draws.append(np.mean(ok))
        mc[nm] = dict(mean=float(np.mean(draws)), q16=float(np.percentile(draws, 16)),
                      q84=float(np.percentile(draws, 84)))
    return dict(label=label, clusters=cls, n_train=n_tr, n_test=n_te, tau_hat_myr=tau_hat,
                acc_train_max=acc_train_max, acc_test=acc_test, k_obs=k_obs, p_T4b_binomial=p_t4b,
                p_T4b_for_holm=p_for_holm, fail_clauses=dict(a=bool(fail_a), b=bool(fail_b), c=bool(fail_c)),
                raw_verdict=raw, mc_age_weighted_accuracy=mc,
                acc_train_curve=dict(tau=grid.tolist(), acc=acc_tr.tolist()))
