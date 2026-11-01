"""t6.py -- regional H0 heterogeneity test T6 (own code from PREREG §5.7, EQUATIONS (g4), PART2 (g4))."""
import os, sys, math, json
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
C_KMS = 299792.458
Q0, J0 = -0.55, 1.0
MERGE_TARGET = {0: 1, 1: 0, 2: 1, 3: 0, 4: 0, 5: 0, 6: 1, 7: 2, 8: 4, 9: 5, 10: 6, 11: 4}   # registered


def ang2pix_ring_nside1(lon_deg, lat_deg):
    """Own HEALPix RING ang2pix for Nside = 1 (Gorski et al. 2005 algorithm)."""
    nside = 1
    lon = np.radians(np.mod(lon_deg, 360.0)); z = np.sin(np.radians(lat_deg))
    tt = lon / (0.5 * math.pi)                         # in [0, 4)
    za = np.abs(z)
    pix = np.empty(len(z), dtype=int)
    eq = za <= 2.0 / 3.0
    # equatorial belt
    t1 = nside * (0.5 + tt[eq]); t2 = nside * z[eq] * 0.75
    jp = np.floor(t1 - t2).astype(int); jm = np.floor(t1 + t2).astype(int)
    ir = nside + 1 + jp - jm
    kshift = 1 - (ir & 1)
    ip = (jp + jm - nside + kshift + 1) // 2
    ip = np.mod(ip, 4 * nside)
    ncap = 2 * nside * (nside - 1)
    pix[eq] = ncap + (ir - 1) * 4 * nside + ip
    # polar caps
    pc = ~eq
    tp = tt[pc] - np.floor(tt[pc])
    tmp = nside * np.sqrt(3.0 * (1.0 - za[pc]))
    jp = np.floor(tp * tmp).astype(int); jm = np.floor((1.0 - tp) * tmp).astype(int)
    ir = jp + jm + 1
    ip = np.floor(tt[pc] * ir).astype(int)
    ip = np.mod(ip, 4 * ir)
    npix = 12 * nside * nside
    north = z[pc] > 0
    pix_pc = np.where(north, 2 * ir * (ir - 1) + ip, npix - 2 * ir * (ir + 1) + ip)
    pix[pc] = pix_pc
    return pix


def load():
    import pandas as pd
    df = pd.read_csv(os.path.join(ROOT, "data", "pantheonplus", "Pantheon+SH0ES.dat"), sep=r"\s+")
    f = open(os.path.join(ROOT, "data", "pantheonplus", "Pantheon+SH0ES_STAT+SYS.cov"))
    n = int(f.readline())
    cov = np.array(f.read().split(), dtype=float).reshape(n, n)
    return df, cov


def fix_MB(df, cov):
    cal = df["IS_CALIBRATOR"].values == 1
    y = df["m_b_corr"].values[cal] - df["CEPH_DIST"].values[cal]
    C = cov[np.ix_(cal, cal)]
    Ci = np.linalg.inv(C)
    one = np.ones(len(y))
    var = 1.0 / (one @ Ci @ one)
    MB = var * (one @ Ci @ y)
    return dict(MB=float(MB), sigma_MB=float(math.sqrt(var)), n_cal=int(cal.sum()))


def run_T6(df, cov, MB, sMB, coords="galactic", zcol="zHD", merge=True):
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    z = df[zcol].values
    sel = (z >= 0.023) & (z <= 0.15) & (df["IS_CALIBRATOR"].values == 0)
    d = df[sel]
    zz = d[zcol].values; zh = d["zHEL"].values
    ra, dec = d["RA"].values, d["DEC"].values
    if coords == "galactic":
        g = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame="icrs").galactic
        lon, lat = g.l.deg, g.b.deg
    else:
        lon, lat = ra, dec
    pix = ang2pix_ring_nside1(lon, lat)
    # cross-check with astropy-healpix
    from astropy_healpix import HEALPix
    hp = HEALPix(nside=1, order="ring")
    pix_ref = hp.lonlat_to_healpix(lon * u.deg, lat * u.deg)
    assert np.array_equal(pix, np.asarray(pix_ref)), "own HEALPix disagrees with astropy-healpix"
    counts0 = np.bincount(pix, minlength=12)
    region = pix.copy()
    merges = []
    if merge:
        cur = counts0.copy()
        for i in range(12):                      # single pass, increasing RING index
            if 0 < cur[i] < 10:
                t = MERGE_TARGET[i]
                region[region == i] = t
                cur[t] += cur[i]; cur[i] = 0
                merges.append((i, t))
    counts = np.bincount(region, minlength=12)
    keep_regions = [i for i in range(12) if counts[i] >= 10]
    m = np.isin(region, keep_regions)
    Npix = len(keep_regions)
    out = dict(coords=coords, zcol=zcol, merge=merge, n_sel=int(sel.sum()), counts_initial=counts0.tolist(),
               merges=merges, counts_final=counts.tolist(), regions=keep_regions, Npix=Npix,
               n_used=int(m.sum()))
    if Npix < 2:
        out.update(verdict="INCONCLUSIVE", p_het=1.0)
        return out
    zz, zh = zz[m], zh[m]
    idx_sel = np.where(sel)[0][m]
    C = cov[np.ix_(idx_sel, idx_sel)]
    f = zz * (1 + 0.5 * (1 - Q0) * zz - (1 - Q0 - 3 * Q0 ** 2 + J0) / 6.0 * zz ** 2)
    mu0 = MB + 25 + 5 * np.log10(C_KMS * (1 + zh) / (1 + zz) * f)
    y = mu0 - d["m_b_corr"].values[m]
    P = np.zeros((len(y), Npix))
    for k, rg in enumerate(keep_regions):
        P[region[m] == rg, k] = 1.0
    Ci = np.linalg.inv(C)
    A = P.T @ Ci @ P
    Ceta = np.linalg.inv(A)
    eta = Ceta @ (P.T @ Ci @ y)
    H = 10 ** (eta / 5)
    CH = (math.log(10) / 5) ** 2 * np.outer(H, H) * Ceta
    CHi = np.linalg.inv(CH)
    one = np.ones(Npix)
    Hbar = float(one @ CHi @ H / (one @ CHi @ one))
    var_stat = float(1.0 / (one @ CHi @ one))
    sHbar = math.sqrt(var_stat + (math.log(10) / 5 * Hbar) ** 2 * sMB ** 2)
    r = H - Hbar
    chi2 = float(r @ CHi @ r)
    from scipy.stats import chi2 as chi2d, norm
    p = float(chi2d.sf(chi2, Npix - 1))
    Z = (Hbar - 67.36) / math.sqrt(sHbar ** 2 + 0.54 ** 2)
    if p > 0.3173:
        v = "FAIL"
    elif p <= 0.00270 and Z >= 3.0:
        v = "PASS (raw, before Holm)"
    else:
        v = "INCONCLUSIVE"
    out.update(H0_regions=H.tolist(), H0_region_sigma=np.sqrt(np.diag(CH)).tolist(), Hbar=Hbar,
               sigma_Hbar=sHbar, sigma_Hbar_stat=math.sqrt(var_stat), chi2_het=chi2, dof=Npix - 1, p_het=p,
               Z_het=float(norm.isf(p / 2)), Z_allsky=float(Z), verdict=v)
    return out
