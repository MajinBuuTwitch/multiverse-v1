"""generate_mocks.py -- Phase 3 injection mocks (PHASE3_INJECTION_SPEC_SEALED.txt), blind-rebuild workspace.

Forward models are the rebuild's registered ones, imported unchanged from ../../rebuild:
  cosmo.py        expansion history (photons, 2 massless + 1 x 0.06 eV nu, flat), Law 1 RK4, CPL, distances,
                  sound horizon (a5) at z* (HS96) and r_d = F * r_s(z_d^EH98) (DEVIATIONS D3), (R, l_A, 100 w_b)
  likelihoods.py  file readers (used for the parse self-check) and the BAO / CMB / SN chi^2
  t5.py           SPARC reader, registered M_b^mono, 400+100 shell grid, shadow kernel F_sigma, Upsilon 0.5/0.7
  t6.py           Galactic HEALPix Nside=1 RING pixels + registered sparse-pixel merge, GLS M_B fix, T6 fit
Each universe folder mirrors the original data/ layout (desi_bao_dr2/, pantheonplus/, des_dovekie/, sparc/), so
the original readers work with nothing but a path change.

usage:  python generate_mocks.py generate      # writes MOCKS_FOR_ARGON/ + SEALED/ANSWER_KEY.json
        python generate_mocks.py selfcheck     # spec section 6 checks -> appended to GENERATION_LOG.md
"""
import os, sys, json, math, re, shutil, hashlib, secrets, string, datetime, tempfile, glob
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np

SEALED = os.path.dirname(os.path.abspath(__file__))
PH3 = os.path.dirname(SEALED)
ROOT = os.path.dirname(PH3)
OUT = os.path.join(PH3, "MOCKS_FOR_ARGON")
ORIG = os.path.join(ROOT, "data")
KEY = os.path.join(SEALED, "ANSWER_KEY.json")
LOG = os.path.join(SEALED, "GENERATION_LOG.md")
sys.path.insert(0, os.path.join(ROOT, "rebuild"))
import cosmo, likelihoods as L, t5, t6          # noqa: E402

cosmo.load_rd_calibration(os.path.join(ROOT, "results_rebuild", "validation", "rd_calibration.json"))
np.seterr(all="ignore")

M_ABS = -19.253                 # spec G5
GDAG_MS2 = 1.20e-10             # spec G3 (RAR)
MS2_TO_KMS2_PER_KPC = 3.0856775814913673e19 / 1e6
LYA = dict(DH=0.066, DM=0.33, r=-0.431)        # registered joint Lya BAO+AP block (PREREG 5.1)
DES_NOISE_CAP = 1.0            # mag; see Originals (DES-Dovekie de-weighted contaminant directions)
SENTINELS = ("-9", "-99", "-999", "-9.0", "-999.0")
REF_SIG = dict(R=0.065, Omega_b=0.00086, wb100=0.015, H0=0.54, BBN_wb100=0.055)   # spec G7


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def log(msg):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"- {now()} — {msg}\n")


# ================================================================== truths (spec section 3)
def onu(h):
    return cosmo.M_NU / (cosmo.NU93 * h * h)


def truths():
    T = {}
    h, wb, wc = 0.6736, 0.02237, 0.1200
    obc = (wb + wc) / h ** 2
    T["C1"] = dict(family="COSMO", label="LCDM (Planck 2018)", model="lcdm", h=h, ombh2=wb, omch2=wc, Obc=obc,
                   Om_tot=obc + onu(h))
    h2 = 0.6600
    wb2 = h2 ** 2 / 19.0
    T["C2"] = dict(family="COSMO", label="MODEL-TRUE Law 1 (gamma_u = 0.10, Omega_b = 1/19, f_leak = 1/6)",
                   model="law1", gam=0.10, h=h2, ombh2=wb2, omch2=5.0 * wb2, Obc=6.0 / 19.0,
                   Om_tot=6.0 / 19.0 + onu(h2))
    T["C3"] = dict(family="COSMO", label="off-curve CPL (w0 = -0.75, wa = -1.0), matter as C1", model="cpl",
                   w0=-0.75, wa=-1.0, h=h, ombh2=wb, omch2=wc, Obc=obc, Om_tot=obc + onu(h))
    for k in ("C1", "C2", "C3"):
        t = T[k]
        t["H0"] = 100 * t["h"]; t["wb100"] = 100 * t["ombh2"]; t["Omega_b"] = t["ombh2"] / t["h"] ** 2
        t["R_wc_over_wb"] = t["omch2"] / t["ombh2"]
        if t["model"] == "law1":
            t["w0_fit"] = -1 + t["gam"]
            t["wa_tangent"] = -1.5 * t["gam"] * (t["Om_tot"] + t["gam"] * (1 - t["Om_tot"]))
    T["G1"] = dict(family="GALAXY", label="MODEL-TRUE wide shadow kernel", kind="kernel", sigma_ref_kpc=9.0,
                   R_shadow=5.0, f_leak=1.0 / 6.0)
    T["G2"] = dict(family="GALAXY", label="MODEL-TRUE narrow shadow kernel", kind="kernel", sigma_ref_kpc=3.0,
                   R_shadow=5.0, f_leak=1.0 / 6.0)
    T["G3"] = dict(family="GALAXY", label="RAR-TRUE", kind="rar", gdagger_ms2=GDAG_MS2)
    # regional: LCDM background with the C1 matter density and h = 0.73
    for k, A in (("H1", 0.0), ("H2", 2.0), ("H3", 5.0)):
        T[k] = dict(family="REGIONAL", label={"H1": "NULL (uniform H0 = 73.0)", "H2": "SMALL VARIATION +-2",
                                              "H3": "LARGE VARIATION +-5"}[k], amplitude=A, H0_mean=73.0,
                    Om_tot=T["C1"]["Om_tot"], ombh2=wb)
    return T


def params_of(t, h=None):
    h = t["h"] if h is None else h
    if t.get("model") == "law1":
        return cosmo.Params(t["Om_tot"], h, t["ombh2"], model="law1", gam=t["gam"])
    if t.get("model") == "cpl":
        return cosmo.Params(t["Om_tot"], h, t["ombh2"], model="cpl", w0=t["w0"], wa=t["wa"])
    return cosmo.Params(t["Om_tot"], h, t["ombh2"])


# ================================================================== format-preserving token writers
def ndec(tok):
    if "e" in tok.lower():
        m = tok.lower().split("e")[0]
    else:
        m = tok
    return len(m.split(".")[1]) if "." in m else 0


def fmt_like(tok, val, dec=None):
    d = ndec(tok) if dec is None else dec
    if "e" in tok.lower():
        return f"{val:.{d}e}"
    return f"{val:.{d}f}"


def replace_fixed(line, tok_index, newtok):
    """replace the tok_index-th whitespace token, right-aligned at the same end column (fixed-width files)."""
    spans = [m.span() for m in re.finditer(r"\S+", line)]
    s, e = spans[tok_index]
    prev_end = spans[tok_index - 1][1] if tok_index > 0 else 0
    room = e - prev_end - 1
    if len(newtok) > room:
        raise ValueError(f"token {newtok!r} does not fit ({room} chars)")
    return line[:e - len(newtok)].rjust(0)[:e - len(newtok)] if False else \
        line[:prev_end + 1] + newtok.rjust(e - prev_end - 1) + line[e:]


# ================================================================== originals (read once)
class Originals:
    def __init__(self):
        # DESI
        self.desi_lines = open(os.path.join(ORIG, "desi_bao_dr2", "desi_gaussian_bao_ALL_GCcomb_mean.txt")).read().splitlines(True)
        self.bao = L.load_bao("std")
        self.bao_chol = np.linalg.cholesky(self.bao["cov"])
        # Pantheon+
        txt = open(os.path.join(ORIG, "pantheonplus", "Pantheon+SH0ES.dat")).read().splitlines(True)
        self.pp_header = txt[0]
        self.pp_cols = txt[0].split()
        self.pp_rows = [l.rstrip("\n").split(" ") for l in txt[1:]]
        assert all(len(r) == len(self.pp_cols) for r in self.pp_rows)
        df, cov = L._read_pplus()
        self.pp_df = df
        self.pp_chol = np.linalg.cholesky(cov)
        self.pp_cols_dec = {c: max(ndec(r[i]) for r in self.pp_rows) for i, c in enumerate(self.pp_cols)}
        # DES-Dovekie
        self.dv_lines = open(os.path.join(ORIG, "des_dovekie", "DES-Dovekie_HD.csv")).read().splitlines(True)
        self.dv = L.load_dovekie()                       # W = inverse covariance
        # noise from C = W^-1 via the eigenbasis of W.  The published DES-Dovekie covariance gives the
        # PROBIA_BEAMS ~ 0 contaminant SNe errors of ~100-300 mag (zero weight); along the eigen-directions whose
        # variance exceeds DES_NOISE_CAP^2 the noise sigma is capped at DES_NOISE_CAP (exact everywhere else).
        lam, V = np.linalg.eigh(self.dv.W)
        sd = 1.0 / np.sqrt(lam)
        self.dv_ncapped = int(np.sum(sd > DES_NOISE_CAP))
        self.dv_noise_map = V * np.minimum(sd, DES_NOISE_CAP)[None, :]
        # SPARC
        self.mm_lines = open(os.path.join(ORIG, "sparc", "MassModels_Lelli2016c.mrt"), newline="").read().splitlines(True)
        gals = t5.load_sparc()
        self.gals = gals
        self.G = {k: t5.Galaxy(gals[k]) for k in gals}
        # T6 pixel -> final region map (registered merge on the registered HF sample)
        self.pp_pix = pp_pixels(df)
        self.region_of_pixel, self.region_counts = t6_region_map(df, self.pp_pix)
        # DES MU zero-point convention: constant, so MU levels resemble the original file (M is marginalised)
        c1 = truths()["C1"]
        p = params_of(c1); d = cosmo.Distances(p)
        mu = 5 * np.log10((1 + self.dv.zhel) * d.DM(self.dv.zcmb)) + 25
        r = self.dv.mobs - mu
        self.des_offset = float(self.dv.W1 @ r / self.dv.S)


def pp_pixels(df):
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    g = SkyCoord(ra=df["RA"].values * u.deg, dec=df["DEC"].values * u.deg, frame="icrs").galactic
    return t6.ang2pix_ring_nside1(g.l.deg, g.b.deg)


def t6_region_map(df, pix):
    z = df["zHD"].values
    sel = (z >= 0.023) & (z <= 0.15) & (df["IS_CALIBRATOR"].values == 0)
    cur = np.bincount(pix[sel], minlength=12)
    target = {i: i for i in range(12)}
    for i in range(12):                                    # identical single pass to t6.run_T6
        if 0 < cur[i] < 10:
            t = t6.MERGE_TARGET[i]
            for k in range(12):
                if target[k] == i:
                    target[k] = t
            cur[t] += cur[i]; cur[i] = 0
    keep = [i for i in range(12) if cur[i] >= 10]
    reg = {k: (target[k] if target[k] in keep else None) for k in range(12)}
    return reg, {i: int(cur[i]) for i in keep}


# ================================================================== writers
def write_desi(O, out, th, noise_vec):
    os.makedirs(os.path.join(out, "desi_bao_dr2"), exist_ok=True)
    vals = th + noise_vec
    lines, k = [], 0
    for l in O.desi_lines:
        if l.startswith("#") or not l.strip():
            lines.append(l); continue
        z, v, q = l.split()
        lines.append(f"{z} {fmt_like(v, vals[k])} {q}\n" if l.endswith("\n") else f"{z} {fmt_like(v, vals[k])} {q}")
        k += 1
    assert k == len(vals)
    open(os.path.join(out, "desi_bao_dr2", "desi_gaussian_bao_ALL_GCcomb_mean.txt"), "w", newline="").write("".join(lines))
    shutil.copyfile(os.path.join(ORIG, "desi_bao_dr2", "desi_gaussian_bao_ALL_GCcomb_cov.txt"),
                    os.path.join(out, "desi_bao_dr2", "desi_gaussian_bao_ALL_GCcomb_cov.txt"))


def bao_theory(p, d, bao):
    rd = cosmo.r_drag(p)
    z = bao["z"]; DM = d.DM(z); DH = d.DH(z)
    th = np.empty_like(z)
    for i, k in enumerate(bao["kind"]):
        th[i] = DM[i] / rd if k == "DM_over_rs" else DH[i] / rd if k == "DH_over_rs" else \
            (z[i] * DM[i] ** 2 * DH[i]) ** (1 / 3) / rd
    return th, rd


def write_pantheon(O, out, mu_true, noise):
    os.makedirs(os.path.join(out, "pantheonplus"), exist_ok=True)
    df = O.pp_df
    cols = O.pp_cols
    ix = {c: i for i, c in enumerate(cols)}
    m_new = mu_true + M_ABS + noise
    cal = df["IS_CALIBRATOR"].values == 1
    rows = []
    for j, r in enumerate(O.pp_rows):
        r = list(r)
        m_old = float(r[ix["m_b_corr"]])
        delta = m_new[j] - m_old
        fac = 10 ** (-0.4 * delta)
        dec = O.pp_cols_dec
        r[ix["m_b_corr"]] = fmt_like(r[ix["m_b_corr"]], m_new[j], dec["m_b_corr"])
        r[ix["MU_SH0ES"]] = fmt_like(r[ix["MU_SH0ES"]], m_new[j] - M_ABS, dec["MU_SH0ES"])
        if cal[j]:
            r[ix["CEPH_DIST"]] = fmt_like(r[ix["CEPH_DIST"]], mu_true[j], dec["CEPH_DIST"])
        # raw SALT2 quantities kept consistent with the new corrected magnitude
        if r[ix["mB"]] not in SENTINELS:
            r[ix["mB"]] = fmt_like(r[ix["mB"]], float(r[ix["mB"]]) + delta, dec["mB"])
        for c in ("x0", "x0ERR", "COV_x1_x0", "COV_c_x0"):
            tok = r[ix[c]]
            r[ix[c]] = fmt_like(tok, float(tok) * fac, max(ndec(tok), 3) if "e" not in tok.lower() else None) \
                if "e" not in tok.lower() else fmt_like(tok, float(tok) * fac)
        rows.append(" ".join(r) + "\n")
    open(os.path.join(out, "pantheonplus", "Pantheon+SH0ES.dat"), "w", newline="").write(O.pp_header + "".join(rows))
    shutil.copyfile(os.path.join(ORIG, "pantheonplus", "Pantheon+SH0ES_STAT+SYS.cov"),
                    os.path.join(out, "pantheonplus", "Pantheon+SH0ES_STAT+SYS.cov"))


def write_dovekie(O, out, mu_obs):
    os.makedirs(os.path.join(out, "des_dovekie"), exist_ok=True)
    cols = None; k = 0; lines = []
    for l in O.dv_lines:
        if l.startswith("VARNAMES:"):
            cols = l.split()[1:]; lines.append(l); continue
        if l.startswith("SN:"):
            imu = cols.index("MU") + 1                   # +1 for the 'SN:' token
            tok = l.split()[imu]
            lines.append(replace_fixed(l, imu, fmt_like(tok, mu_obs[k], 5)))
            k += 1
        else:
            lines.append(l)
    assert k == len(mu_obs)
    open(os.path.join(out, "des_dovekie", "DES-Dovekie_HD.csv"), "w", newline="").write("".join(lines))
    shutil.copyfile(os.path.join(ORIG, "des_dovekie", "STAT+SYS.npz"), os.path.join(out, "des_dovekie", "STAT+SYS.npz"))


def write_sparc(O, out, vobs):
    os.makedirs(os.path.join(out, "sparc"), exist_ok=True)
    dash = [i for i, l in enumerate(O.mm_lines) if l.startswith("-----")][-1]
    lines = list(O.mm_lines[:dash + 1])
    cnt = {}
    for l in O.mm_lines[dash + 1:]:
        if not l.strip():
            lines.append(l); continue
        gid = l[0:11].strip()
        j = cnt.get(gid, 0); cnt[gid] = j + 1
        lines.append(replace_fixed(l, 3, f"{vobs[gid][j]:.2f}"))
    assert all(cnt[g] == len(vobs[g]) for g in vobs)
    open(os.path.join(out, "sparc", "MassModels_Lelli2016c.mrt"), "w", newline="").write("".join(lines))
    shutil.copyfile(os.path.join(ORIG, "sparc", "SPARC_Lelli2016c.mrt"), os.path.join(out, "sparc", "SPARC_Lelli2016c.mrt"))


# ================================================================== one universe
def make_universe(O, t, rng, out, noise=True):
    """returns the realization-specific truth record for the answer key."""
    rec = {}
    nz = (lambda n: rng.standard_normal(n)) if noise else (lambda n: np.zeros(n))
    if t["family"] == "COSMO":
        p = params_of(t); d = cosmo.Distances(p)
        th, rd = bao_theory(p, d, O.bao)
        write_desi(O, out, th, O.bao_chol @ nz(len(th)))
        # registered joint Lya BAO+AP replacement vector (PREREG 5.1), drawn from its own 2x2 covariance
        zl = np.array([2.33])
        DH, DM = float(d.DH(zl)[0] / rd), float(d.DM(zl)[0] / rd)
        C2 = np.array([[LYA["DH"] ** 2, LYA["r"] * LYA["DH"] * LYA["DM"]],
                       [LYA["r"] * LYA["DH"] * LYA["DM"], LYA["DM"] ** 2]])
        e = np.linalg.cholesky(C2) @ nz(2)
        json.dump({"description": "joint Lyman-alpha BAO+AP distance ratios at z_eff = 2.33 (same quantities as "
                                  "arXiv:2607.27410 used by PREREG 5.1); replaces the z = 2.33 rows of "
                                  "desi_gaussian_bao_ALL_GCcomb_mean.txt in the model fits",
                   "z_eff": 2.33, "DH_over_rd": round(DH + e[0], 4), "DM_over_rd": round(DM + e[1], 4),
                   "sigma_DH_over_rd": LYA["DH"], "sigma_DM_over_rd": LYA["DM"], "corr_DH_DM": LYA["r"]},
                  open(os.path.join(out, "desi_bao_dr2", "lya_bao_ap_joint.json"), "w"), indent=1)
        # compressed CMB (registered 3x3 Chen+19 covariance)
        R, lA, wb100, zs, rs = cosmo.cmb_observables(p, d)
        cmb = L.cmb_prior("lcdm3")
        ec = np.linalg.cholesky(cmb["C"]) @ nz(3)
        os.makedirs(os.path.join(out, "cmb_distance_prior"), exist_ok=True)
        json.dump({"description": "compressed CMB distance prior, same structure as Chen, Huang & Wang (2019) "
                                  "JCAP 02 028 Table 1 (column used by PREREG); only the mean vector differs",
                   "parameters": ["R", "l_A", "100omega_b"],
                   "mean": [round(R + ec[0], 5), round(lA + ec[1], 4), round(wb100 + ec[2], 4)],
                   "sigma": cmb_sig(), "correlation": cmb_corr()},
                  open(os.path.join(out, "cmb_distance_prior", "distance_prior.json"), "w"), indent=1)
        # supernovae
        df = O.pp_df
        mu = 5 * np.log10((1 + df["zHEL"].values) * d.DM(df["zHD"].values)) + 25
        write_pantheon(O, out, mu, O.pp_chol @ nz(len(mu)))
        mud = 5 * np.log10((1 + O.dv.zhel) * d.DM(O.dv.zcmb)) + 25
        ed = O.dv_noise_map @ nz(len(mud))                               # cov = W^-1 (capped, see Originals)
        write_dovekie(O, out, mud + O.des_offset + ed)
        # external reference measurements (spec G7)
        r = nz(5)
        ref = {"description": "external reference measurements for this universe (Gaussian, registered sigma)",
               "R_omegac_over_omegab": {"value": round(t["R_wc_over_wb"] + REF_SIG["R"] * r[0], 4), "sigma": REF_SIG["R"]},
               "Omega_b": {"value": round(t["Omega_b"] + REF_SIG["Omega_b"] * r[1], 6), "sigma": REF_SIG["Omega_b"]},
               "100omega_b": {"value": round(t["wb100"] + REF_SIG["wb100"] * r[2], 4), "sigma": REF_SIG["wb100"]},
               "H0": {"value": round(t["H0"] + REF_SIG["H0"] * r[3], 3), "sigma": REF_SIG["H0"]},
               "BBN_100omega_b_prior": {"value": round(t["wb100"] + REF_SIG["BBN_wb100"] * r[4], 4),
                                        "sigma": REF_SIG["BBN_wb100"]}}
        json.dump(ref, open(os.path.join(out, "REFERENCES.json"), "w"), indent=1)
        rec.update(noiseless=dict(R=R, l_A=lA, wb100=wb100, z_star=zs, r_s_zstar=rs, r_d=rd, lya_DH=DH, lya_DM=DM),
                   references=ref, des_mu_offset=O.des_offset)
    elif t["family"] == "GALAXY":
        vobs, gal_rec = {}, {}
        for gid, gal in O.gals.items():
            G = O.G[gid]
            if t["kind"] == "kernel":
                v, _ = G.vmodel(t["sigma_ref_kpc"], t["R_shadow"])
            else:
                gbar = t5.G_KPC * G.Mmono / G.R ** 2                      # (km/s)^2 / kpc
                gd = t["gdagger_ms2"] * MS2_TO_KMS2_PER_KPC
                x = np.sqrt(np.maximum(gbar, 0) / gd)
                gobs = np.where(x > 1e-8, gbar / -np.expm1(-x), np.sqrt(np.maximum(gbar, 0) * gd))
                v = np.sqrt(gobs * G.R)
            vobs[gid] = v + gal["eV"] * nz(len(v))
        write_sparc(O, out, vobs)
    else:   # REGIONAL
        reg_ids = sorted(O.region_counts)
        A = t["amplitude"]
        signs = rng.choice([-1.0, 1.0], size=len(reg_ids)) if A > 0 else np.zeros(len(reg_ids))
        H = 73.0 + A * signs
        n = np.array([O.region_counts[i] for i in reg_ids], float)
        H = H - (n @ H / n.sum() - 73.0)
        Hreg = dict(zip(reg_ids, H))
        tt = dict(t, model="lcdm", h=0.73)
        p = params_of(tt); d = cosmo.Distances(p)
        df = O.pp_df
        mu = 5 * np.log10((1 + df["zHEL"].values) * d.DM(df["zHD"].values)) + 25
        cal = df["IS_CALIBRATOR"].values == 1
        dmu = np.zeros(len(mu))
        for j in range(len(mu)):
            rg = O.region_of_pixel[int(O.pp_pix[j])]
            if (not cal[j]) and rg is not None:
                dmu[j] = 5 * math.log10(73.0 / Hreg[rg])
        write_pantheon(O, out, mu + dmu, O.pp_chol @ nz(len(mu)))
        rec.update(H0_regions={str(k): float(v) for k, v in Hreg.items()}, signs=[float(s) for s in signs],
                   region_counts_HF={str(k): v for k, v in O.region_counts.items()},
                   region_of_pixel={str(k): v for k, v in O.region_of_pixel.items()}, background_h=0.73)
    return rec


def cmb_sig():
    return [float(x) for x in L.CMB_LCDM["sig"]]


def cmb_corr():
    return L.CMB_LCDM["corr"].tolist()


# ================================================================== generate
def generate():
    if os.path.exists(KEY):
        raise SystemExit("ANSWER_KEY.json exists: refusing to regenerate over a sealed set")
    if os.listdir(OUT):
        raise SystemExit("MOCKS_FOR_ARGON is not empty")
    master = secrets.randbits(62)
    ss = np.random.SeedSequence(master)
    rng = np.random.default_rng(ss.spawn(1)[0])
    T = truths()
    names = list(T)
    alphabet = string.ascii_uppercase + string.digits
    ids = set()
    while len(ids) < 45:
        ids.add("U-" + "".join(rng.choice(list(alphabet), 4)))
    ids = list(ids)
    rng.shuffle(ids)
    plan = []
    for rnd in range(1, 6):
        order = list(rng.permutation(names))
        for k in order:
            plan.append(dict(universe_id=ids.pop(), truth=k, round=rnd))
    useeds = [int(x) for x in np.random.SeedSequence(master).generate_state(45, dtype=np.uint64) >> np.uint64(1)]
    log(f"generate: 45 universes planned (5 rounds x 9 truths, shuffled within each round); master seed and "
        f"realization seeds recorded in ANSWER_KEY.json only")
    O = Originals()
    log(f"DES-Dovekie noise: exact draw from the published covariance except {O.dv_ncapped} eigen-directions with "
        f"variance > {DES_NOISE_CAP}^2 mag^2 (the PROBIA_BEAMS~0 contaminants de-weighted by ~100-300 mag errors), whose "
        f"sigma is capped at {DES_NOISE_CAP} mag; these directions carry ~1e-5 of the likelihood weight")
    log(f"forward-model inputs loaded: DESI {len(O.bao['z'])} rows, Pantheon+ {len(O.pp_rows)} rows, "
        f"DES-Dovekie {O.dv.N} SNe, SPARC {len(O.gals)} galaxies; T6 final regions {sorted(O.region_counts)} "
        f"(HF counts {O.region_counts})")
    key = dict(spec_sha256=sha(os.path.join(SEALED, "PHASE3_INJECTION_SPEC_SEALED.txt"))
               if os.path.exists(os.path.join(SEALED, "PHASE3_INJECTION_SPEC_SEALED.txt")) else None,
               generated=now(), master_seed=master, M_abs=M_ABS, truths=T,
               rd_calibration_factor=cosmo.RD_CALIB, des_mu_offset=O.des_offset, universes=[])
    for u, s in zip(plan, useeds):
        t = T[u["truth"]]
        out = os.path.join(OUT, u["universe_id"])
        os.makedirs(out)
        rec = make_universe(O, t, np.random.default_rng(s), out, noise=True)
        key["universes"].append(dict(universe_id=u["universe_id"], round=u["round"], family=t["family"],
                                     truth=u["truth"], realization_seed=s, **rec))
        print(u["universe_id"], u["round"], u["truth"], flush=True)
    with open(os.path.join(OUT, "MOCK_MANIFEST.csv"), "w", newline="") as f:
        f.write("universe_id,family,round\n")
        for u in sorted(key["universes"], key=lambda x: (x["round"], x["universe_id"])):
            f.write(f"{u['universe_id']},{u['family']},{u['round']}\n")
    json.dump(key, open(KEY, "w"), indent=1, default=float)
    log(f"generate: wrote {len(key['universes'])} universe folders + MOCK_MANIFEST.csv to MOCKS_FOR_ARGON/ and "
        f"ANSWER_KEY.json to SEALED/")


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


# ================================================================== self-check (spec section 6)
def with_data(path):
    """point the rebuild readers at a universe folder (nothing but a path change)."""
    L.DATA = path
    t5.DATA = os.path.join(path, "sparc")


def selfcheck():
    key = json.load(open(KEY))
    T = key["truths"]
    O = Originals()
    res = {"parse": {}, "noiseless": {}, "grep": {}}
    orig_hash = {rel: sha(os.path.join(ORIG, rel)) for rel in
                 ("desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt", "pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
                  "des_dovekie/STAT+SYS.npz", "sparc/SPARC_Lelli2016c.mrt")}
    pp_meas = {"m_b_corr", "MU_SH0ES", "CEPH_DIST", "mB", "x0", "x0ERR", "COV_x1_x0", "COV_c_x0"}
    bad = []
    # ---------------- 1. parse with the same readers, identical structure
    for u in key["universes"]:
        uid = u["universe_id"]; d = os.path.join(OUT, uid); fam = u["family"]
        with_data(d)
        try:
            if fam == "COSMO":
                b = L.load_bao("std")
                assert np.array_equal(b["z"], O.bao["z"]) and b["kind"] == O.bao["kind"] and np.array_equal(b["cov"], O.bao["cov"])
                ml = open(os.path.join(d, "desi_bao_dr2", "desi_gaussian_bao_ALL_GCcomb_mean.txt")).read().splitlines(True)
                assert len(ml) == len(O.desi_lines)
                assert all((a.split()[0], a.split()[2]) == (o.split()[0], o.split()[2]) for a, o in zip(ml, O.desi_lines)
                           if not a.startswith("#")) and ml[0] == O.desi_lines[0]
                sdv = L.load_dovekie()
                assert sdv.N == O.dv.N and np.array_equal(sdv.zcmb, O.dv.zcmb) and np.array_equal(sdv.W, O.dv.W)
                dl = open(os.path.join(d, "des_dovekie", "DES-Dovekie_HD.csv")).read().splitlines(True)
                assert len(dl) == len(O.dv_lines)
                cols = None
                for a, o in zip(dl, O.dv_lines):
                    if o.startswith("VARNAMES:"):
                        cols = o.split()
                    if not o.startswith("SN:"):
                        assert a == o
                    else:
                        ta, to = a.split(), o.split()
                        im = cols.index("MU")
                        assert len(a) == len(o) and ta[:im] + ta[im + 1:] == to[:im] + to[im + 1:]
                json.load(open(os.path.join(d, "REFERENCES.json")))
                json.load(open(os.path.join(d, "cmb_distance_prior", "distance_prior.json")))
                json.load(open(os.path.join(d, "desi_bao_dr2", "lya_bao_ap_joint.json")))
                for rel in ("desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt", "des_dovekie/STAT+SYS.npz"):
                    assert sha(os.path.join(d, rel)) == orig_hash[rel]
            if fam in ("COSMO", "REGIONAL"):
                sp = L.load_pantheonplus()
                df, cov = L._read_pplus()
                assert len(df) == len(O.pp_df) and list(df.columns) == list(O.pp_df.columns) and sp.N == 1580
                pl = open(os.path.join(d, "pantheonplus", "Pantheon+SH0ES.dat")).read().splitlines(True)
                assert pl[0] == O.pp_header and len(pl) == len(O.pp_rows) + 1
                for a, o in zip(pl[1:], O.pp_rows):
                    ta = a.rstrip("\n").split(" ")
                    assert len(ta) == len(o)
                    for c, x, y in zip(O.pp_cols, ta, o):
                        if c not in pp_meas:
                            assert x == y, (c, x, y)
                        if c == "CEPH_DIST" and y == "-9":
                            assert x == "-9"
                assert sha(os.path.join(d, "pantheonplus/Pantheon+SH0ES_STAT+SYS.cov")) == orig_hash["pantheonplus/Pantheon+SH0ES_STAT+SYS.cov"]
            if fam == "GALAXY":
                g = t5.load_sparc()
                assert set(g) == set(O.gals)
                for k in g:
                    for col in ("R", "eV", "Vgas", "Vdisk", "Vbul", "SBdisk", "SBbul", "Rdisk", "Q", "Inc"):
                        assert np.array_equal(np.asarray(g[k][col]), np.asarray(O.gals[k][col])), (k, col)
                ml = open(os.path.join(d, "sparc", "MassModels_Lelli2016c.mrt"), newline="").read().splitlines(True)
                assert len(ml) == len(O.mm_lines)
                for a, o in zip(ml, O.mm_lines):
                    assert len(a) == len(o) and a[:26] == o[:26] and a[32:] == o[32:]
                assert sha(os.path.join(d, "sparc/SPARC_Lelli2016c.mrt")) == orig_hash["sparc/SPARC_Lelli2016c.mrt"]
            res["parse"][uid] = "OK"
        except AssertionError as e:
            res["parse"][uid] = f"FAIL {e}"; bad.append(uid)
    log(f"self-check 1 (parse with the rebuild's own readers after a path change; identical structure; unchanged "
        f"covariance/aux files byte-identical): {sum(v == 'OK' for v in res['parse'].values())}/45 OK"
        + (f"; FAILED: {bad}" if bad else ""))
    # ---------------- 2. noiseless prediction fits the truth with chi2 ~ 0 (one realization per truth)
    tmp = tempfile.mkdtemp(prefix="ph3_noiseless_")
    for k, t in T.items():
        u = [x for x in key["universes"] if x["truth"] == k and x["round"] == 1][0]
        d = os.path.join(tmp, k)
        os.makedirs(d)
        make_universe(O, t, np.random.default_rng(u["realization_seed"]), d, noise=False)
        with_data(d)
        r = {}
        if t["family"] == "COSMO":
            p = params_of(t); dd = cosmo.Distances(p)
            r["BAO_desi_dr2_chi2"] = L.chi2_bao(p, dd, cosmo.r_drag(p), L.load_bao("std"))
            cm = L.cmb_prior("lcdm3")
            cm["mu"] = np.array(json.load(open(os.path.join(d, "cmb_distance_prior", "distance_prior.json")))["mean"])
            r["CMB_chi2"] = L.chi2_cmb(p, dd, cm)
            ly = json.load(open(os.path.join(d, "desi_bao_dr2", "lya_bao_ap_joint.json")))
            rd = cosmo.r_drag(p)
            dv = np.array([dd.DH(np.array([2.33]))[0] / rd - ly["DH_over_rd"], dd.DM(np.array([2.33]))[0] / rd - ly["DM_over_rd"]])
            C2 = np.array([[LYA["DH"] ** 2, LYA["r"] * LYA["DH"] * LYA["DM"]], [LYA["r"] * LYA["DH"] * LYA["DM"], LYA["DM"] ** 2]])
            r["Lya_BAO_AP_chi2"] = float(dv @ np.linalg.solve(C2, dv))
            r["PantheonPlus_chi2_Mmarg_1580"] = L.load_pantheonplus().chi2(dd)
            r["DESDovekie_chi2_Mmarg_1820"] = L.load_dovekie().chi2(dd)
            ref = json.load(open(os.path.join(d, "REFERENCES.json")))
            r["references_max_abs_dev"] = max(abs(ref["R_omegac_over_omegab"]["value"] - t["R_wc_over_wb"]),
                                              abs(ref["H0"]["value"] - t["H0"]), abs(ref["100omega_b"]["value"] - t["wb100"]))
        elif t["family"] == "GALAXY":
            g = t5.load_sparc()
            chis = []
            for gid in g:
                G = t5.Galaxy(g[gid])
                if t["kind"] == "kernel":
                    chis.append(G.chi2(t["sigma_ref_kpc"], t["R_shadow"]) / G.N)
                else:
                    gbar = t5.G_KPC * G.Mmono / G.R ** 2
                    gd = t["gdagger_ms2"] * MS2_TO_KMS2_PER_KPC
                    x = np.sqrt(np.maximum(gbar, 0) / gd)
                    gobs = np.where(x > 1e-8, gbar / -np.expm1(-x), np.sqrt(np.maximum(gbar, 0) * gd))
                    chis.append(float(np.sum(((G.Vobs - np.sqrt(gobs * G.R)) / G.eV) ** 2)) / G.N)
            r["max_chi2_red_over_175_galaxies"] = float(np.max(chis))
            r["median_chi2_red"] = float(np.median(chis))
        else:
            df, cov = L._read_pplus()
            fx = t6.fix_MB(df, cov)
            m = t6.run_T6(df, cov, fx["MB"], fx["sigma_MB"])
            hk = u["H0_regions"]
            r["M_B_fixed"] = fx["MB"]
            r["max_abs_dH0_region_vs_truth"] = float(max(abs(h - hk[str(rg)]) for rg, h in zip(m["regions"], m["H0_regions"])))
            r["chi2_het_noiseless"] = m["chi2_het"]
            r["note"] = "regional H0 from the registered cosmographic (q0=-0.55, j0=1) T6 estimator vs LCDM truth"
        res["noiseless"][k] = r
    log(f"self-check 2 noiseless files kept (never deleted) at {tmp}")
    log("self-check 2 (noiseless prediction re-read with the rebuild readers and evaluated at the truth with the "
        "rebuild likelihoods; round-1 realization of each truth): " + json.dumps(res["noiseless"], default=float))
    # ---------------- 3. no truth value, seed or truth label in MOCKS_FOR_ARGON
    res["grep"] = grep_check(key, O)
    log("self-check 3 (truth values / seeds / truth labels in MOCKS_FOR_ARGON): " + json.dumps(res["grep"]))
    json.dump(res, open(os.path.join(tempfile.gettempdir(), "ph3_selfcheck_last.json"), "w"), indent=1, default=float)
    print(json.dumps(res["grep"], indent=1)); print(json.dumps(res["noiseless"], indent=1, default=float))
    print("parse:", sum(v == "OK" for v in res["parse"].values()), "/ 45")


NUM_PATTERNS = ["0.6736", "0.02237", "0.1200", "0.31377", "0.10", "0.90", "0.6600", "0.022926", "0.315789", "5.000",
                "0.75", "1.0", "0.18", "9.0", "3.0", "1.20", "73.0", "19.253", "0.06"]
NAME_PATTERNS = [r"LCDM", "ΛCDM", r"Law ?1", r"law1", r"CPL", r"\bRAR\b", r"MODEL", r"NULL", r"unwind", r"weaken",
                 r"\b[CGH][123]\b", r"truth", r"f_leak", r"gamma", r"sigma_ref", r"MOND", r"shadow", r"inject",
                 r"mock", r"seed"]


def grep_check(key, O):
    """Every text file in MOCKS_FOR_ARGON is scanned. A hit counts as INHERITED if it lies in a token that is
    byte-identical to the original public file at the same row/column (real data, not a truth); every other hit
    is reported. Exact-value matches of a truth number in changed content are listed separately."""
    seeds = [str(key["master_seed"])] + [str(u["realization_seed"]) for u in key["universes"]]
    out = dict(files_scanned=0, seed_hits=0, name_hits_new_content=[], number_substring_hits_new_content={},
               number_exact_token_hits_new_content=[], inherited_hits={})
    origmap = {"desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt": O.desi_lines,
               "pantheonplus/Pantheon+SH0ES.dat": [O.pp_header] + [" ".join(r) + "\n" for r in O.pp_rows],
               "des_dovekie/DES-Dovekie_HD.csv": O.dv_lines,
               "sparc/MassModels_Lelli2016c.mrt": O.mm_lines}
    tv = {p: float(p) for p in NUM_PATTERNS}
    for path in sorted(glob.glob(os.path.join(OUT, "**", "*"), recursive=True)):
        if os.path.isdir(path):
            continue
        rel = os.path.relpath(path, OUT).replace("\\", "/")
        sub = rel.split("/", 1)[1] if "/" in rel else rel
        raw = open(path, "rb").read()
        out["files_scanned"] += 1
        for s in seeds:
            if s.encode() in raw:
                out["seed_hits"] += 1
        if path.endswith(".npz"):
            continue
        txt = raw.decode("utf-8", "replace")
        lines = txt.splitlines(True)
        olines = origmap.get(sub)
        identical_file = sub in ("pantheonplus/Pantheon+SH0ES_STAT+SYS.cov", "desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
                                 "sparc/SPARC_Lelli2016c.mrt")
        if identical_file:
            out["inherited_hits"][sub] = "byte-identical copy of the original public file"
            continue
        for i, line in enumerate(lines):
            otoks = olines[i].split() if olines is not None and i < len(olines) else None
            for m in re.finditer(r"\S+", line):
                tok = m.group(0)
                j = len(re.findall(r"\S+", line[:m.start()]))
                inherited = otoks is not None and j < len(otoks) and otoks[j] == tok
                for pat in NAME_PATTERNS:
                    if re.search(pat, tok, flags=re.I if pat in ("mock", "seed", "inject", "truth", "shadow") else 0):
                        if inherited:
                            out["inherited_hits"].setdefault(sub, 0); out["inherited_hits"][sub] = \
                                out["inherited_hits"][sub] + 1 if isinstance(out["inherited_hits"][sub], int) else 1
                        else:
                            out["name_hits_new_content"].append(f"{rel}:{i + 1}:{tok}")
                for pat in NUM_PATTERNS:
                    if pat in tok:
                        if inherited:
                            continue
                        out["number_substring_hits_new_content"][pat] = out["number_substring_hits_new_content"].get(pat, 0) + 1
                        try:
                            v = float(tok.strip('",:[]{}'))
                            if abs(v - tv[pat]) < 0.5 * 10 ** (-ndec(pat)) or abs(abs(v) - tv[pat]) < 0.5 * 10 ** (-ndec(pat)):
                                out["number_exact_token_hits_new_content"].append(f"{rel}:{i + 1}:{tok}")
                        except ValueError:
                            pass
    return out


if __name__ == "__main__":
    {"generate": generate, "selfcheck": selfcheck}[sys.argv[1]]()
