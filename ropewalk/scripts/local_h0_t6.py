import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import json
import math
from pathlib import Path
import numpy as np
from scipy.stats import chi2

C_LIGHT_KMS = 299792.458

# Pre-registered mechanical sparse-pixel merge map for HEALPix N_side=1 RING (PREREG.md Sec 5.7 line 300)
SPARSE_MERGE_MAP = {
    0: 1, 1: 0, 2: 1, 3: 0,
    4: 0, 5: 0, 6: 1, 7: 2,
    8: 4, 9: 5, 10: 6, 11: 4,
}


def icrs_to_galactic_rad(ra_deg: np.ndarray, dec_deg: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    [Established Astronomy]
    Convert ICRS / J2000 (RA, Dec) in degrees to Galactic (l, b) in radians
    using the standard Hipparcos/IAU J2000 rotation matrix.
    """
    ra = np.deg2rad(ra_deg)
    dec = np.deg2rad(dec_deg)
    x = np.cos(dec) * np.cos(ra)
    y = np.cos(dec) * np.sin(ra)
    z = np.sin(dec)

    # Exact J2000 ICRS -> Galactic rotation matrix (ESA Hipparcos / Astropy convention)
    r_mat = np.array([
        [-0.0548755604162154, -0.8734370902348850, -0.4838350155487132],
        [+0.4941094278755837, -0.4448296299600112, +0.7469822444972189],
        [-0.8676661490190047, -0.1980763734312015, +0.4559837761750669],
    ], dtype=float)

    xyz_gal = r_mat @ np.vstack([x, y, z])
    b = np.arcsin(np.clip(xyz_gal[2], -1.0, 1.0))
    l = np.mod(np.arctan2(xyz_gal[1], xyz_gal[0]), 2.0 * math.pi)
    return l, b


def healpix_nside1_ring(theta_rad: np.ndarray, phi_rad: np.ndarray) -> np.ndarray:
    """
    [Established Math - Gorski et al. 2005, ApJ 622, 759]
    Exact HEALPix N_side = 1 RING pixel index in {0, 1, ..., 11} for colatitude
    theta in [0, pi] and longitude phi in [0, 2*pi).
    """
    nside = 1
    z_arr = np.cos(theta_rad)
    phi_arr = np.mod(phi_rad, 2.0 * math.pi)
    tt_arr = (2.0 / math.pi) * phi_arr  # in [0, 4)

    pix_out = np.zeros(len(z_arr), dtype=int)
    for idx in range(len(z_arr)):
        z = float(z_arr[idx])
        za = abs(z)
        tt = float(tt_arr[idx])
        if za <= (2.0 / 3.0):
            temp1 = nside * (0.5 + tt)
            temp2 = nside * z * 0.75
            jp = int(math.floor(temp1 - temp2))
            jm = int(math.floor(temp1 + temp2))
            ir = nside + 1 + jp - jm
            kshift = 1 - (ir & 1)
            ip = (jp + jm - nside + kshift + 1) // 2
            ip = ip % (4 * nside)
            pix_out[idx] = (ir - 1) * 4 * nside + ip
        else:
            ip = int(math.floor(tt)) % 4
            if z > 0.0:
                pix_out[idx] = ip
            else:
                pix_out[idx] = 8 + ip
    return pix_out


def load_pantheon_plus_full(pantheon_dir: str | Path) -> dict:
    """
    Load Pantheon+SH0ES.dat and Pantheon+SH0ES_STAT+SYS.cov.
    """
    pantheon_dir = Path(pantheon_dir)
    dat_path = pantheon_dir / "Pantheon+SH0ES.dat"
    cov_path = pantheon_dir / "Pantheon+SH0ES_STAT+SYS.cov"

    with open(dat_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    header = lines[0].split()
    col_idx = {name: i for i, name in enumerate(header)}

    rows = []
    for line in lines[1:]:
        if not line.strip():
            continue
        p = line.split()
        rows.append({
            "CID": p[col_idx["CID"]],
            "zHD": float(p[col_idx["zHD"]]),
            "zCMB": float(p[col_idx["zCMB"]]),
            "zHEL": float(p[col_idx["zHEL"]]),
            "m_b_corr": float(p[col_idx["m_b_corr"]]),
            "CEPH_DIST": float(p[col_idx["CEPH_DIST"]]),
            "IS_CALIBRATOR": int(p[col_idx["IS_CALIBRATOR"]]),
            "RA": float(p[col_idx["RA"]]),
            "DEC": float(p[col_idx["DEC"]]),
        })

    with open(cov_path, "r", encoding="utf-8") as f:
        n_cov = int(f.readline().strip())
        cov_flat = np.fromfile(f, dtype=float, sep="\n")
    cov_mat = cov_flat.reshape((n_cov, n_cov))

    return {"rows": rows, "cov": cov_mat}


def fit_t6_calibrators(pantheon_data: dict) -> dict:
    """
    [Registered FIX Step for Test T6 - PREREG.md Sec 5.7 line 297]
    Fit and freeze the GLS weighted-mean Type Ia absolute magnitude M_B^fixed and its
    variance sigma_{M_B^fixed}^2 on the SH0ES Cepheid calibrator sample (IS_CALIBRATOR == 1).
    """
    rows = pantheon_data["rows"]
    cov = pantheon_data["cov"]

    cal_indices = [i for i, r in enumerate(rows) if r["IS_CALIBRATOR"] == 1]
    m_b_vec = np.array([rows[i]["m_b_corr"] - rows[i]["CEPH_DIST"] for i in cal_indices], dtype=float)
    cov_cal = cov[np.ix_(cal_indices, cal_indices)]

    inv_cov_cal = np.linalg.inv(cov_cal)
    ones = np.ones(len(cal_indices), dtype=float)
    denom = float(ones @ inv_cov_cal @ ones)
    m_b_fixed = float((ones @ inv_cov_cal @ m_b_vec) / denom)
    var_m_b_fixed = float(1.0 / denom)
    sigma_m_b_fixed = math.sqrt(var_m_b_fixed)

    return {
        "n_calibrators": len(cal_indices),
        "M_B_fixed": round(m_b_fixed, 8),
        "sigma_M_B_fixed": round(sigma_m_b_fixed, 8),
        "var_M_B_fixed": float(var_m_b_fixed),
    }


def dimensionless_dl_sh0es(z_hd: np.ndarray, z_hel: np.ndarray, q0: float = -0.55, j0: float = 1.0) -> np.ndarray:
    """
    [Established Cosmography - Riess et al. 2022 Eq. 4]
    Dimensionless luminosity distance d_L(z) * (H_0 / c) at low redshift (0.023 <= z <= 0.15):
      d_tilde_L(z) = ((1 + z_hel) / (1 + z_hd)) * z_hd * [1 + 0.5*(1 - q0)*z_hd - (1/6)*(1 - q0 - 3*q0^2 + j0)*z_hd^2]
    """
    term1 = 0.5 * (1.0 - q0) * z_hd
    term2 = -(1.0 / 6.0) * (1.0 - q0 - 3.0 * (q0 ** 2) + j0) * (z_hd ** 2)
    return ((1.0 + z_hel) / (1.0 + z_hd)) * z_hd * (1.0 + term1 + term2)


def assign_and_merge_pixels(raw_pixels: np.ndarray, apply_merge: bool = True) -> tuple[np.ndarray, list[int], dict]:
    """
    [Registered Mechanical Rule - PREREG.md Sec 5.7 line 300, Review V3 B4]
    In increasing order of RING index i in {0, ..., 11}, any pixel with 0 < N_{SN,i} < 10
    is merged into SPARSE_MERGE_MAP[i] in a single pass; any empty pixel or any region
    still having N_SN < 10 after this single pass is dropped.
    """
    pix = raw_pixels.copy()
    initial_counts = {i: int(np.sum(pix == i)) for i in range(12)}
    merge_actions = []

    if apply_merge:
        for i in range(12):
            cnt = int(np.sum(pix == i))
            if 0 < cnt < 10:
                target = SPARSE_MERGE_MAP[i]
                pix[pix == i] = target
                merge_actions.append({"from_pixel": i, "to_pixel": target, "count_moved": cnt})

    post_counts = {i: int(np.sum(pix == i)) for i in range(12)}
    retained_pixels = [i for i in range(12) if post_counts[i] >= 10]
    dropped_pixels = [i for i in range(12) if 0 < post_counts[i] < 10]

    return pix, retained_pixels, {
        "initial_counts": initial_counts,
        "merge_actions": merge_actions,
        "post_merge_counts": post_counts,
        "retained_pixels": retained_pixels,
        "dropped_sparse_pixels": dropped_pixels,
    }


def evaluate_t6_hubble_flow(
    pantheon_data: dict,
    m_b_fixed: float,
    sigma_m_b_fixed: float,
    coord_frame: str = "galactic",
    z_col: str = "zHD",
    apply_merge: bool = True,
) -> dict:
    """
    [Registered TEST Step for Test T6 - PREREG.md Sec 5.7 lines 298-308]
    Evaluate regional H_0 heterogeneity across retained HEALPix N_side=1 RING sky regions
    for Pantheon+ Hubble-flow supernovae (0.023 <= z <= 0.15, IS_CALIBRATOR == 0).
    """
    rows = pantheon_data["rows"]
    cov = pantheon_data["cov"]

    hf_indices = [
        i for i, r in enumerate(rows)
        if r["IS_CALIBRATOR"] == 0 and (0.023 <= r[z_col] <= 0.15)
    ]
    z_vec = np.array([rows[i][z_col] for i in hf_indices], dtype=float)
    z_hel = np.array([rows[i]["zHEL"] for i in hf_indices], dtype=float)
    mb_vec = np.array([rows[i]["m_b_corr"] for i in hf_indices], dtype=float)
    ra_deg = np.array([rows[i]["RA"] for i in hf_indices], dtype=float)
    dec_deg = np.array([rows[i]["DEC"] for i in hf_indices], dtype=float)

    if coord_frame == "galactic":
        lon_rad, lat_rad = icrs_to_galactic_rad(ra_deg, dec_deg)
    elif coord_frame == "equatorial":
        lon_rad = np.deg2rad(np.mod(ra_deg, 360.0))
        lat_rad = np.deg2rad(dec_deg)
    else:
        raise ValueError(f"Unknown coord_frame: {coord_frame}")

    theta_rad = (0.5 * math.pi) - lat_rad
    raw_pix = healpix_nside1_ring(theta_rad, lon_rad)
    merged_pix, retained_pixels, pix_info = assign_and_merge_pixels(raw_pix, apply_merge=apply_merge)

    # Filter to supernovae belonging to retained regions (N_SN >= 10)
    keep_mask = np.isin(merged_pix, retained_pixels)
    kept_hf_indices = [hf_indices[j] for j in range(len(hf_indices)) if keep_mask[j]]
    kept_pix = merged_pix[keep_mask]
    z_kept = z_vec[keep_mask]
    z_hel_kept = z_hel[keep_mask]
    mb_kept = mb_vec[keep_mask]

    n_pix = len(retained_pixels)
    n_sn_kept = len(kept_hf_indices)
    cov_hf = cov[np.ix_(kept_hf_indices, kept_hf_indices)]
    inv_cov_hf = np.linalg.inv(cov_hf)

    # Construct y_k = 5*log10(c * d_tilde_L(z_k)) + 25 - (m_{b,corr,k} - M_B^fixed)
    d_tilde = dimensionless_dl_sh0es(z_kept, z_hel_kept)
    y_vec = 5.0 * np.log10(C_LIGHT_KMS * d_tilde) + 25.0 - (mb_kept - m_b_fixed)

    # Design matrix P (n_sn_kept x n_pix)
    P = np.zeros((n_sn_kept, n_pix), dtype=float)
    for j, p_id in enumerate(retained_pixels):
        P[kept_pix == p_id, j] = 1.0

    # GLS estimate of eta_i = 5 * log10(H_{0,i})
    pt_cinv = P.T @ inv_cov_hf
    c_eta = np.linalg.inv(pt_cinv @ P)
    eta_hat = c_eta @ (pt_cinv @ y_vec)

    # Convert to H_{0,i} = 10^(eta_i / 5) and propagate covariance C_{H_0} = J C_eta J^T
    h0_hat = 10.0 ** (eta_hat / 5.0)
    jac = np.diag((math.log(10.0) / 5.0) * h0_hat)
    c_h0 = jac @ c_eta @ jac.T
    inv_c_h0 = np.linalg.inv(c_h0)

    ones = np.ones(n_pix, dtype=float)
    denom_h0 = float(ones @ inv_c_h0 @ ones)
    h0_bar = float((ones @ inv_c_h0 @ h0_hat) / denom_h0)

    # Total variance on h0_bar including calibrator zero-point variance (PREREG.md line 301)
    var_h0_bar_hf = float(1.0 / denom_h0)
    var_h0_bar_cal = ((math.log(10.0) / 5.0) * h0_bar * sigma_m_b_fixed) ** 2
    sigma_h0_bar_total = math.sqrt(var_h0_bar_hf + var_h0_bar_cal)

    # Heterogeneity chi-squared and p-value (dof = N_pix - 1)
    diff_h0 = h0_hat - h0_bar
    chi2_het = float(diff_h0 @ inv_c_h0 @ diff_h0)
    dof = max(n_pix - 1, 1)
    p_het = float(chi2.sf(chi2_het, df=dof)) if n_pix >= 2 else 1.0
    p_holm = p_het if n_pix >= 2 else 1.0

    # All-sky tension against Planck 2018 LambdaCDM (67.36 +/- 0.54 km/s/Mpc)
    z_all_sky = (h0_bar - 67.36) / math.sqrt(sigma_h0_bar_total ** 2 + 0.54 ** 2)

    # Exhaustive deciding thresholds (PREREG.md lines 304-307):
    # 1. FAIL: N_pix >= 2 and p_het > 0.3173 (< 1-sigma heterogeneity)
    # 2. PASS: N_pix >= 2, p_het <= 0.00270 (>= 3-sigma), Z_all_sky >= 3.0 (subject to Holm control)
    # 3. INCONCLUSIVE: Every other outcome
    fail_reasons = []
    inconclusive_reasons = []
    if n_pix >= 2 and p_het > 0.3173:
        verdict = "FAIL"
        fail_reasons.append(f"p_het = {p_het:.6f} > 0.3173 (< 1-sigma regional H_0 heterogeneity).")
    elif n_pix >= 2 and p_het <= 0.00270 and z_all_sky >= 3.0:
        verdict = "PASS"
    else:
        verdict = "INCONCLUSIVE"
        if n_pix < 2:
            inconclusive_reasons.append(f"N_pix = {n_pix} < 2.")
        else:
            inconclusive_reasons.append(
                f"Intermediate heterogeneity: 0.00270 < p_het = {p_het:.6f} <= 0.3173 (or Z_all_sky = {z_all_sky:.2f} < 3.0)."
            )

    regional_table = []
    sigma_h0_diag = np.sqrt(np.diag(c_h0))
    for j, p_id in enumerate(retained_pixels):
        regional_table.append({
            "pixel_ring_id": int(p_id),
            "n_sn": int(np.sum(kept_pix == p_id)),
            "H0_kms_Mpc": round(float(h0_hat[j]), 4),
            "sigma_H0_hf_only": round(float(sigma_h0_diag[j]), 4),
        })

    return {
        "coord_frame": coord_frame,
        "z_column": z_col,
        "apply_merge": apply_merge,
        "n_hf_total_in_z_range": len(hf_indices),
        "n_hf_retained": n_sn_kept,
        "N_pix": n_pix,
        "dof": dof,
        "H0_bar_kms_Mpc": round(h0_bar, 4),
        "sigma_H0_bar_hf_only": round(math.sqrt(var_h0_bar_hf), 4),
        "sigma_H0_bar_total": round(sigma_h0_bar_total, 4),
        "Z_all_sky_vs_Planck": round(z_all_sky, 4),
        "chi2_het": round(chi2_het, 4),
        "p_het": round(p_het, 8),
        "p_T6_holm": round(p_holm, 8),
        "h0_min_region": round(float(np.min(h0_hat)), 4),
        "h0_max_region": round(float(np.max(h0_hat)), 4),
        "h0_range_max_minus_min": round(float(np.max(h0_hat) - np.min(h0_hat)), 4),
        " h0_rms_scatter": round(float(np.std(h0_hat, ddof=1)), 4),
        "verdict": verdict,
        "fail_reasons": fail_reasons,
        "inconclusive_reasons": inconclusive_reasons,
        "pixel_merging_summary": pix_info,
        "regional_H0": regional_table,
    }


def compute_coincidence_window(f_leak_frozen: float) -> dict:
    """
    [Pre-Registered Coincidence Window Diagnostic - PREREG.md Sec 6 lines 311-316 & EQUATIONS Sec 8.2]
    With Planck 2018 base LambdaCDM parameters (omega_b = 0.02237, omega_c = 0.1200, H_0 = 67.36,
    Omega_bc = 0.3138, Omega_{m,tot} = 0.3153, Omega_Lambda = 0.6847), compute the cosmic time span
    Delta t_coinc during which Omega_b(a), Omega_dm(a), Omega_de(a) remain simultaneously within:
      - Criterion H-Abs: max_i |Omega_i(a) - s_i^target| <= 0.05
      - Criterion H-Rel: max_i |Omega_i(a) - s_i^target| / s_i^target <= 0.10
    evaluated for both f_leak = 1/6 and the T2-A-Pantheon+-frozen f_leak.
    """
    h = 0.6736
    omega_b0 = 0.02237 / (h ** 2)   # 0.0493017
    omega_dm0 = 0.1200 / (h ** 2)   # 0.2644702
    omega_m_tot = 0.3153
    omega_de0 = 0.6847

    # 1 / H_0 in Gyr: 977.79222 / 67.36 = 14.515918 Gyr
    t_hubble_gyr = 977.79222 / 67.36

    # Fine scale-factor grid a in [1e-4, 5.0]
    a_grid = np.linspace(1e-4, 5.0, 200_000)
    e2_grid = omega_m_tot * (a_grid ** -3) + omega_de0
    e_grid = np.sqrt(e2_grid)
    dt_da_gyr = t_hubble_gyr / (a_grid * e_grid)

    omega_b_a = (omega_b0 * (a_grid ** -3)) / e2_grid
    omega_dm_a = (omega_dm0 * (a_grid ** -3)) / e2_grid
    omega_de_a = omega_de0 / e2_grid

    # Current age of the universe t_0 (a <= 1.0)
    mask_today = a_grid <= 1.0
    t0_gyr = float(np.trapezoid(dt_da_gyr[mask_today], x=a_grid[mask_today]))

    def eval_for_fleak(f_val: float, label: str) -> dict:
        s_b = 1.0 / 19.0
        s_dm = 6.0 * (1.0 - f_val) / 19.0
        s_de = (12.0 + 6.0 * f_val) / 19.0

        err_abs = np.maximum.reduce([
            np.abs(omega_b_a - s_b),
            np.abs(omega_dm_a - s_dm),
            np.abs(omega_de_a - s_de),
        ])
        err_rel = np.maximum.reduce([
            np.abs(omega_b_a - s_b) / s_b,
            np.abs(omega_dm_a - s_dm) / max(abs(s_dm), 1e-12),
            np.abs(omega_de_a - s_de) / s_de,
        ])

        mask_abs = err_abs <= 0.05
        mask_rel = err_rel <= 0.10

        def span_stats(mask: np.ndarray) -> dict:
            if not np.any(mask):
                return {"delta_t_gyr": 0.0, "frac_of_t0": 0.0, "a_min": None, "a_max": None, "z_min": None, "z_max": None}
            a_sub = a_grid[mask]
            dt_sub = dt_da_gyr[mask]
            dt_gyr = float(np.sum(dt_sub) * (a_grid[1] - a_grid[0]))
            a_min = float(a_sub[0])
            a_max = float(a_sub[-1])
            return {
                "delta_t_gyr": round(dt_gyr, 4),
                "frac_of_t0": round(dt_gyr / t0_gyr, 4),
                "a_min": round(a_min, 4),
                "a_max": round(a_max, 4),
                "z_at_a_min": round((1.0 / a_min) - 1.0, 4),
                "z_at_a_max": round((1.0 / a_max) - 1.0, 4),
                "contains_present_a1": bool((a_min <= 1.0) and (1.0 <= a_max)),
            }

        # Present-day deviations at a = 1
        idx_1 = int(np.argmin(np.abs(a_grid - 1.0)))
        return {
            "label": label,
            "f_leak": round(f_val, 6),
            "target_shares": {
                "s_b": round(s_b, 6),
                "s_dm": round(s_dm, 6),
                "s_de": round(s_de, 6),
            },
            "present_day_a1_deviations": {
                "max_abs_err": round(float(err_abs[idx_1]), 5),
                "max_rel_err": round(float(err_rel[idx_1]), 5),
            },
            "Criterion_H_Abs_5pct": span_stats(mask_abs),
            "Criterion_H_Rel_10pct": span_stats(mask_rel),
        }

    return {
        "t0_cosmic_age_gyr": round(t0_gyr, 4),
        "planck_present_shares": {
            "Omega_b0": round(omega_b0, 6),
            "Omega_dm0": round(omega_dm0, 6),
            "Omega_de0": round(omega_de0, 6),
        },
        "f_leak_1_over_6": eval_for_fleak(1.0 / 6.0, "Geometric f_leak = 1/6 (1:5:13)"),
        "f_leak_T2A_PantheonPlus": eval_for_fleak(f_leak_frozen, "Frozen T2-A-Pantheon+ f_leak"),
    }
