"""likelihoods.py -- data loading and chi^2 terms (own code)."""
import os, math
import numpy as np
import cosmo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

# ---------------------------------------------------------------- DESI DR2 BAO
def load_bao(variant="mod"):
    """variant: 'std' = unmodified desi_bao_dr2; 'mod' = Lya z=2.33 row replaced by arXiv:2607.27410
    BAO+AP (DH=8.600+-0.066, DM=39.32+-0.33, r=-0.431)  [registered deciding];
    'mod_r0' = same but r=0 (sensitivity)."""
    rows = []
    for line in open(os.path.join(DATA, "desi_bao_dr2", "desi_gaussian_bao_ALL_GCcomb_mean.txt")):
        if line.startswith("#") or not line.strip():
            continue
        z, v, q = line.split()
        rows.append((float(z), float(v), q))
    cov = np.loadtxt(os.path.join(DATA, "desi_bao_dr2", "desi_gaussian_bao_ALL_GCcomb_cov.txt"))
    z = np.array([r[0] for r in rows]); val = np.array([r[1] for r in rows]); kind = [r[2] for r in rows]
    if variant in ("mod", "mod_r0"):
        iDH = [i for i in range(len(z)) if abs(z[i] - 2.33) < 1e-6 and kind[i] == "DH_over_rs"][0]
        iDM = [i for i in range(len(z)) if abs(z[i] - 2.33) < 1e-6 and kind[i] == "DM_over_rs"][0]
        # Lya block must be uncorrelated with the other tracers in the official file
        others = [i for i in range(len(z)) if i not in (iDH, iDM)]
        assert np.all(cov[np.ix_([iDH, iDM], others)] == 0)
        r = -0.431 if variant == "mod" else 0.0
        val[iDH], val[iDM] = 8.600, 39.32
        cov[iDH, iDH] = 0.066 ** 2
        cov[iDM, iDM] = 0.33 ** 2
        cov[iDH, iDM] = cov[iDM, iDH] = r * 0.066 * 0.33
    elif variant != "std":
        raise ValueError(variant)
    return dict(z=z, val=val, kind=kind, cov=cov, icov=np.linalg.inv(cov), variant=variant)


def chi2_bao(p, dist, rd, bao):
    z = bao["z"]
    DM = dist.DM(z); DH = dist.DH(z)
    th = np.empty_like(z)
    for i, k in enumerate(bao["kind"]):
        if k == "DM_over_rs":
            th[i] = DM[i] / rd
        elif k == "DH_over_rs":
            th[i] = DH[i] / rd
        elif k == "DV_over_rs":
            th[i] = (z[i] * DM[i] ** 2 * DH[i]) ** (1.0 / 3.0) / rd
        else:
            raise ValueError(k)
    d = th - bao["val"]
    return float(d @ bao["icov"] @ d)


# ---------------------------------------------------------------- Chen, Huang & Wang (2019) Table 1 priors
CMB_LCDM = dict(mu=np.array([1.7502, 301.471, 2.236]), sig=np.array([0.0046, 0.090, 0.015]),
                corr=np.array([[1.00, 0.46, -0.66], [0.46, 1.00, -0.33], [-0.66, -0.33, 1.00]]))
# wCDM column (sensitivity only): symmetrised errors from Table 1: R +0.0046/-0.0047, lA +0.089/-0.090
CMB_WCDM = dict(mu=np.array([1.7493, 301.462, 2.239]), sig=np.array([0.00465, 0.0895, 0.015]),
                corr=np.array([[1.00, 0.47, -0.66], [0.47, 1.00, -0.34], [-0.66, -0.34, 1.00]]))


def cmb_prior(kind="lcdm3"):
    """kind: 'lcdm3' full 3x3 LCDM prior; 'wcdm3' wCDM column 3x3; 'cond' conditional (R,lA|omega_b);
    'marg' marginal 2x2 (R,lA) block."""
    base = CMB_WCDM if kind == "wcdm3" else CMB_LCDM
    C = base["corr"] * np.outer(base["sig"], base["sig"])
    out = dict(kind=kind, mu=base["mu"].copy(), C=C)
    if kind in ("lcdm3", "wcdm3"):
        out["icov"] = np.linalg.inv(C)
    elif kind == "cond":
        C11 = C[:2, :2]; C12 = C[:2, 2]; C22 = C[2, 2]
        out["slope"] = C12 / C22
        out["Ccond"] = C11 - np.outer(C12, C12) / C22
        out["icov"] = np.linalg.inv(out["Ccond"])
    elif kind == "marg":
        out["icov"] = np.linalg.inv(C[:2, :2])
    return out


def chi2_cmb(p, dist, cmb):
    R, lA, wb100, zs, rs = cosmo.cmb_observables(p, dist)
    if cmb["kind"] in ("lcdm3", "wcdm3"):
        d = np.array([R, lA, wb100]) - cmb["mu"]
    elif cmb["kind"] == "cond":
        mu = cmb["mu"][:2] + cmb["slope"] * (wb100 - cmb["mu"][2])
        d = np.array([R, lA]) - mu
    else:
        d = np.array([R, lA]) - cmb["mu"][:2]
    return float(d @ cmb["icov"] @ d)


# ---------------------------------------------------------------- supernovae
class SN:
    """Generic SN likelihood with analytic marginalisation over the magnitude offset M."""

    def __init__(self, name, zcmb, zhel, mobs, icov):
        self.name, self.zcmb, self.zhel, self.mobs = name, zcmb, zhel, mobs
        self.W = icov
        self.W1 = icov.sum(axis=1)
        self.S = float(self.W1.sum())
        self.N = len(zcmb)
        # performance only (logged 2026-10-30, before any SN fit): W = L L^T, d^T W d = |L^T d|^2 via BLAS
        # dtrmv, which reads half the matrix; identical to d @ W @ d to ~1e-9 in chi^2.
        from scipy.linalg import cholesky
        self.Lc = np.asfortranarray(cholesky(icov, lower=True))

    def chi2(self, dist):
        from scipy.linalg import blas
        mu = 5.0 * np.log10((1.0 + self.zhel) * dist.DM(self.zcmb)) + 25.0
        d = self.mobs - mu
        y = blas.dtrmv(self.Lc, d, lower=1, trans=1)
        B = float(self.W1 @ d)
        return float(y @ y) - B * B / self.S


def _read_pplus():
    import pandas as pd
    df = pd.read_csv(os.path.join(DATA, "pantheonplus", "Pantheon+SH0ES.dat"), sep=r"\s+")
    f = open(os.path.join(DATA, "pantheonplus", "Pantheon+SH0ES_STAT+SYS.cov"))
    n = int(f.readline())
    cov = np.array(f.read().split(), dtype=float).reshape(n, n)
    assert n == len(df)
    return df, cov


def load_pantheonplus():
    df, cov = _read_pplus()
    m = (df["zHD"].values > 0.01) & (df["IS_CALIBRATOR"].values == 0)
    C = cov[np.ix_(m, m)]
    icov = np.linalg.inv(C)
    icov = 0.5 * (icov + icov.T)
    return SN("Pantheon+", df["zHD"].values[m], df["zHEL"].values[m], df["m_b_corr"].values[m], icov)


def load_dovekie():
    import pandas as pd
    cols, recs = None, []
    for line in open(os.path.join(DATA, "des_dovekie", "DES-Dovekie_HD.csv")):
        if line.startswith("VARNAMES:"):
            cols = line.split()[1:]
        elif line.startswith("SN:"):
            recs.append(line.split()[1:])
    df = pd.DataFrame(recs, columns=cols)
    for c in cols[1:]:
        df[c] = df[c].astype(float)
    d = np.load(os.path.join(DATA, "des_dovekie", "STAT+SYS.npz"))
    n = int(d["nsn"][0])
    icov = np.zeros((n, n))
    icov[np.triu_indices(n)] = d["cov"].astype(float)
    il = np.tril_indices(n, -1)
    icov[il] = icov.T[il]
    assert n == len(df), (n, len(df))
    m = df["zHD"].values > 0.0
    assert m.all()
    return SN("DES-Dovekie", df["zHD"].values, df["zHEL"].values, df["MU"].values, icov)


# ---------------------------------------------------------------- BBN priors
BBN = {"desi": (2.218, 0.055), "cooke": (2.166, 0.019)}
