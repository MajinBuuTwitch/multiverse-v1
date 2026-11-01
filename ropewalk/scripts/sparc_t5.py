import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import json
import math
from pathlib import Path
import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import minimize_scalar
from scipy.special import erf

# Gravitational constant in kpc * (km/s)^2 / M_sun [Established]
G_KPC_KMS2_MSUN = 4.30091e-6

# Fixed SPARC stellar mass-to-light ratios at 3.6 um (PREREG.md Sec 5.6) [Established]
UPSILON_DISK = 0.50
UPSILON_BUL = 0.70


def kernel_f_sigma(r: np.ndarray, r_prime: np.ndarray, sigma_ref: float) -> np.ndarray:
    """
    [Established Math / Model Ansatz - Corrected per Review B1 & Gate G9-d]
    Exact piecewise 1D radial enclosed-mass kernel F_sigma(r, r') (PREREG.md Sec 5.6 lines 254-257):
      - For r' / sigma_ref >= 1e-4:
          0.5 * [erf((r + r')/(sqrt(2)*sigma)) + erf((r - r')/(sqrt(2)*sigma))]
          - (1 / sqrt(2*pi)) * (sigma / r') * [exp(-(r - r')^2/(2*sigma^2)) - exp(-(r + r')^2/(2*sigma^2))]
      - For r' / sigma_ref < 1e-4 (analytical point-mass limit):
          erf(r / (sqrt(2)*sigma)) - sqrt(2/pi) * (r / sigma) * exp(-r^2 / (2*sigma^2))
    Supports 2D broadcasting with r shape (N_r, 1) and r_prime shape (1, N_shells).
    """
    r_arr = np.asarray(r, dtype=float)
    rp_arr = np.asarray(r_prime, dtype=float)
    if sigma_ref <= 0.0:
        return (r_arr >= rp_arr).astype(float)

    sqrt2_s = math.sqrt(2.0) * sigma_ref
    two_s2 = 2.0 * sigma_ref * sigma_ref

    # Broadcast shapes
    r_b, rp_b = np.broadcast_arrays(r_arr, rp_arr)
    out = np.empty_like(r_b, dtype=float)

    small_mask = (rp_b / sigma_ref) < 1.0e-4
    if np.any(small_mask):
        rs = r_b[small_mask]
        out[small_mask] = (
            erf(rs / sqrt2_s)
            - math.sqrt(2.0 / math.pi) * (rs / sigma_ref) * np.exp(-np.clip((rs * rs) / two_s2, 0.0, 700.0))
        )

    reg_mask = ~small_mask
    if np.any(reg_mask):
        rr = r_b[reg_mask]
        rpr = rp_b[reg_mask]
        t1 = 0.5 * (erf((rr + rpr) / sqrt2_s) + erf((rr - rpr) / sqrt2_s))
        e_minus = np.exp(-np.clip(((rr - rpr) ** 2) / two_s2, 0.0, 700.0))
        e_plus = np.exp(-np.clip(((rr + rpr) ** 2) / two_s2, 0.0, 700.0))
        t2 = (1.0 / math.sqrt(2.0 * math.pi)) * (sigma_ref / rpr) * (e_minus - e_plus)
        out[reg_mask] = t1 - t2

    return np.clip(out, 0.0, 1.0)


def parse_sparc_catalog(sparc_dir: str | Path) -> list[dict]:
    """
    Parse SPARC_Lelli2016c.mrt and MassModels_Lelli2016c.mrt into a byte-wise ASCII sorted
    list of 175 galaxies, and precompute M_b^mono(< r_j), the 400-point interior grid shells,
    and the stellar tail surface density Sigma_b^tail(r_max) per PREREG.md Section 5.6 (lines 258-275).
    """
    sparc_dir = Path(sparc_dir)
    table1_path = sparc_dir / "SPARC_Lelli2016c.mrt"
    mass_path = sparc_dir / "MassModels_Lelli2016c.mrt"

    meta = {}
    with open(table1_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    start_idx = 0
    for idx, line in enumerate(lines):
        if line.startswith("------"):
            start_idx = idx + 1

    for line in lines[start_idx:]:
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) < 18:
            continue
        gal_name = parts[0].strip()
        hubble_t = int(parts[1])
        dist_mpc = float(parts[2])
        inc_deg = float(parts[5])
        lum_36_1e9 = float(parts[7])
        r_eff_kpc = float(parts[9])
        r_disk_kpc = float(parts[11])
        m_hi_1e9 = float(parts[13])
        v_flat = float(parts[15])
        e_v_flat = float(parts[16])
        q_flag = int(parts[17])

        m_baryon_msun = max((UPSILON_DISK * lum_36_1e9 + 1.33 * m_hi_1e9) * 1e9, 1.0e6)
        meta[gal_name] = {
            "galaxy": gal_name,
            "hubble_t": hubble_t,
            "dist_mpc": dist_mpc,
            "inc_deg": inc_deg,
            "lum_36_1e9": lum_36_1e9,
            "r_eff_kpc": r_eff_kpc,
            "r_disk_kpc": max(r_disk_kpc, 1e-4),
            "m_hi_1e9": m_hi_1e9,
            "m_baryon_msun": m_baryon_msun,
            "v_flat_kms": v_flat,
            "e_v_flat_kms": e_v_flat,
            "q_flag": q_flag,
            "pts": [],
        }

    with open(mass_path, "r", encoding="utf-8") as f:
        mlines = f.readlines()

    m_start = 0
    for idx, line in enumerate(mlines):
        if line.startswith("------"):
            m_start = idx + 1

    for line in mlines[m_start:]:
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) < 9:
            continue
        gal_id = parts[0].strip()
        if gal_id not in meta:
            continue
        r_kpc = float(parts[2])
        v_obs = float(parts[3])
        e_v_obs = float(parts[4])
        v_gas = float(parts[5])
        v_disk = float(parts[6])
        v_bul = float(parts[7])
        sb_disk = float(parts[8])
        sb_bul = float(parts[9]) if len(parts) >= 10 else 0.0

        meta[gal_id]["pts"].append(
            (r_kpc, v_obs, e_v_obs, v_gas, v_disk, v_bul, sb_disk, sb_bul)
        )

    # Byte-wise ASCII sorted() on gal_id.strip() (PREREG.md line 274)
    sorted_names = sorted(meta.keys())
    galaxies = []
    for idx, name in enumerate(sorted_names):
        g = meta[name]
        pts = g.pop("pts")
        arr = np.array(pts, dtype=float)
        R = arr[:, 0]
        v_obs = arr[:, 1]
        e_v_obs = arr[:, 2]
        v_gas = arr[:, 3]
        v_disk = arr[:, 4]
        v_bul = arr[:, 5]
        sb_disk = arr[:, 6]
        sb_bul = arr[:, 7]

        # PREREG.md line 259: v_{bar,raw}^2(r_j) = v_gas|v_gas| + 0.5*v_disk^2 + 0.7*v_bul^2
        v_bar_raw2 = (
            v_gas * np.abs(v_gas)
            + UPSILON_DISK * (v_disk ** 2)
            + UPSILON_BUL * (v_bul ** 2)
        )
        m_b_raw = (R * v_bar_raw2) / G_KPC_KMS2_MSUN
        # Enforce strict radial monotonicity: M_b^mono(< r_j) = max_{1<=m<=j}(0, M_b^raw(< r_m))
        m_b_mono = np.maximum.accumulate(np.maximum(0.0, m_b_raw))
        v_bar_mono2 = (G_KPC_KMS2_MSUN * m_b_mono) / np.maximum(R, 1e-12)

        # Construct 400-point interior grid on [0, r_max] (PREREG.md line 263):
        # 200 linear nodes on [0, r_1] joined to 200 log nodes on [r_1, r_max] (dropping duplicate r_1)
        r_1 = float(R[0])
        r_max = float(R[-1])
        nodes_core = np.linspace(0.0, r_1, 200)
        m_core = m_b_mono[0] * ((nodes_core / max(r_1, 1e-12)) ** 3)

        if len(R) >= 2 and r_max > r_1:
            nodes_outer = np.geomspace(r_1, r_max, 201)[1:]
            # Handle any duplicate R values defensively before PCHIP
            r_unique, u_idx = np.unique(R, return_index=True)
            m_unique = m_b_mono[u_idx]
            pchip = PchipInterpolator(r_unique, m_unique)
            m_outer = np.maximum.accumulate(np.maximum(m_b_mono[0], pchip(nodes_outer)))
            nodes_int = np.concatenate([nodes_core, nodes_outer])
            m_int = np.concatenate([m_core, m_outer])
        else:
            nodes_int = nodes_core
            m_int = m_core

        r_mid_int = 0.5 * (nodes_int[:-1] + nodes_int[1:])
        dm_int = np.maximum(0.0, m_int[1:] - m_int[:-1])

        # Stellar-only exponential tail surface density at r_max (PREREG.md line 265)
        sigma_b_tail_rmax = 1.0e6 * (UPSILON_DISK * sb_disk[-1] + UPSILON_BUL * sb_bul[-1])

        # Odd 1-based positions (idx % 2 == 0) -> train (88); Even (idx % 2 == 1) -> test (87)
        g["split"] = "train" if (idx % 2 == 0) else "test"
        g["alphabetical_index_1based"] = idx + 1
        g["n_pts"] = len(R)
        g["R"] = R
        g["R_min"] = r_1
        g["R_max"] = r_max
        g["v_obs"] = v_obs
        g["e_v_obs"] = e_v_obs
        g["v_bar_raw2"] = v_bar_raw2
        g["m_b_mono"] = m_b_mono
        g["v_bar_mono2"] = v_bar_mono2
        g["r_mid_int"] = r_mid_int
        g["dm_int"] = dm_int
        g["sigma_b_tail_rmax"] = float(sigma_b_tail_rmax)
        galaxies.append(g)

    return galaxies


def predict_galaxy_rotation_curve(
    gal: dict,
    sigma_ref_kpc: float,
    f_leak: float,
) -> np.ndarray:
    """
    [Model Ansatz / Registered Protocol]
    Compute v_model(r_j) for SPARC galaxy g using the 400-point interior grid + 100-point
    stellar-only exponential tail on [r_max, r_max + 5*sigma_ref] (PREREG.md Sec 5.6 lines 259-266).
    """
    sigma = max(float(sigma_ref_kpc), 1e-6)
    r_max = gal["R_max"]
    r_d = gal["r_disk_kpc"]
    s_tail_0 = gal["sigma_b_tail_rmax"]

    # 100 uniformly spaced linear intervals on [r_max, r_max + 5*sigma]
    tail_edges = np.linspace(r_max, r_max + 5.0 * sigma, 101)
    r_mid_tail = 0.5 * (tail_edges[:-1] + tail_edges[1:])
    dr_tail = tail_edges[1:] - tail_edges[:-1]
    sigma_tail = s_tail_0 * np.exp(-(r_mid_tail - r_max) / r_d)
    dm_tail = (2.0 * math.pi) * r_mid_tail * sigma_tail * dr_tail

    r_all_mid = np.concatenate([gal["r_mid_int"], r_mid_tail])
    dm_all = np.concatenate([gal["dm_int"], dm_tail])

    R_col = gal["R"][:, None]
    Rp_row = r_all_mid[None, :]
    F_mat = kernel_f_sigma(R_col, Rp_row, sigma)

    r_factor = 6.0 * (1.0 - f_leak)
    m_sh = r_factor * np.dot(F_mat, dm_all)
    v_model2 = G_KPC_KMS2_MSUN * (gal["m_b_mono"] + m_sh) / np.maximum(gal["R"], 1e-12)
    return np.sqrt(np.maximum(v_model2, 0.0))


def evaluate_sparc_sample(
    galaxies: list[dict],
    model_type: str,
    param_val: float,
    f_leak: float,
) -> dict:
    """
    Evaluate T5-A (model_type='T5A', universal constant sigma_ref = param_val in kpc)
    or T5-B (model_type='T5B', scaled width sigma_ref,g = param_val * R_d,g)
    across a sample of SPARC galaxies (PREREG.md Sec 5.6 lines 251-280).
    """
    chi2_red_list = []
    total_chi2 = 0.0
    total_pts = 0
    sigma_i_list = []
    per_galaxy = []

    for gal in galaxies:
        if model_type == "T5A":
            sigma_g = float(param_val)
            v_pred = predict_galaxy_rotation_curve(gal, sigma_g, f_leak)
        elif model_type == "T5B":
            sigma_g = float(param_val) * gal["r_disk_kpc"]
            v_pred = predict_galaxy_rotation_curve(gal, sigma_g, f_leak)
        elif model_type == "BARYON_ONLY":
            sigma_g = 0.0
            v_pred = np.sqrt(np.maximum(gal["v_bar_mono2"], 0.0))
        else:
            raise ValueError(f"Unknown model_type: {model_type}")

        residuals = (gal["v_obs"] - v_pred) / gal["e_v_obs"]
        chi2_gal = float(np.sum(residuals ** 2))
        n_pts = gal["n_pts"]
        chi2_red = chi2_gal / n_pts

        chi2_red_list.append(chi2_red)
        total_chi2 += chi2_gal
        total_pts += n_pts
        sigma_i_list.append(sigma_g)
        per_galaxy.append({
            "galaxy": gal["galaxy"],
            "n_pts": n_pts,
            "sigma_kpc": round(sigma_g, 5),
            "chi2_red": round(chi2_red, 4),
        })

    arr_red = np.array(chi2_red_list, dtype=float)
    return {
        "n_galaxies": len(galaxies),
        "total_pts": int(total_pts),
        "sum_chi2_red": float(np.sum(arr_red)),
        "mean_chi2_red": float(np.mean(arr_red)),
        "median_chi2_red": float(np.median(arr_red)),
        "total_chi2": float(total_chi2),
        "pooled_chi2_red": float(total_chi2 / max(total_pts, 1)),
        "frac_chi2_red_lt_2": float(np.mean(arr_red < 2.0)),
        "median_sigma_kpc": float(np.median(sigma_i_list)),
        "per_galaxy": per_galaxy,
    }


def fit_sparc_parameter(
    train_galaxies: list[dict],
    model_type: str,
    f_leak: float,
    loss_metric: str = "sum_chi2_red",
) -> dict:
    """
    [Model Ansatz / Registered Protocol]
    Fit sigma_ref (T5-A, [0.1, 100.0] kpc) or k (T5-B, [0.05, 50.0]) on the 88 training galaxies
    by scanning a 200-point log grid to bracket the global minimum of L_train, followed by
    scipy.optimize.minimize_scalar(..., method='bounded', options={'xatol': 1e-5}) (PREREG.md line 271).
    Deciding loss_metric is 'sum_chi2_red'; 'total_chi2' and 'median_chi2_red' are sensitivity checks.
    """
    bounds = (0.1, 100.0) if model_type == "T5A" else (0.05, 50.0)
    grid = np.geomspace(bounds[0], bounds[1], 200)
    vals = np.array([
        evaluate_sparc_sample(train_galaxies, model_type, float(x), f_leak)[loss_metric]
        for x in grid
    ])
    best_idx = int(np.argmin(vals))
    low = float(grid[max(0, best_idx - 1)])
    high = float(grid[min(len(grid) - 1, best_idx + 1)])

    opt = minimize_scalar(
        lambda x: evaluate_sparc_sample(train_galaxies, model_type, float(x), f_leak)[loss_metric],
        bounds=(low, high),
        method="bounded",
        options={"xatol": 1e-5},
    )
    fitted_param = float(opt.x)
    # Check if grid endpoint was better than interior bracket
    if vals[best_idx] < float(opt.fun):
        fitted_param = float(grid[best_idx])

    train_eval = evaluate_sparc_sample(train_galaxies, model_type, fitted_param, f_leak)
    train_eval.pop("per_galaxy", None)
    return {
        "model_type": model_type,
        "loss_metric": loss_metric,
        "f_leak": f_leak,
        "fitted_param": round(fitted_param, 6),
        "train_summary": train_eval,
    }


def score_t5_subtest(test_summary: dict) -> tuple[str, list[str]]:
    """
    [Registered Protocol - PREREG.md Sec 5.6 lines 277-280]
    Exhaustive 3-way partition on the 87 held-out SPARC galaxies:
      - PASS: M_chi2 <= 1.5 AND F_<2 >= 0.70
      - FAIL: M_chi2 > 3.0  OR  F_<2 < 0.40
      - INCONCLUSIVE: Every other outcome.
    """
    m_chi2 = test_summary["median_chi2_red"]
    f_lt2 = test_summary["frac_chi2_red_lt_2"]
    reasons = []

    if m_chi2 <= 1.5 and f_lt2 >= 0.70:
        return "PASS", []
    if m_chi2 > 3.0:
        reasons.append(f"M_chi2 = {m_chi2:.4f} > 3.0")
    if f_lt2 < 0.40:
        reasons.append(f"F_<2 = {f_lt2:.4f} < 0.40")
    if len(reasons) > 0:
        return "FAIL", reasons
    return "INCONCLUSIVE", [
        f"Intermediate outcome: M_chi2 = {m_chi2:.4f} in (1.5, 3.0] or F_<2 = {f_lt2:.4f} in [0.40, 0.70)."
    ]


def evaluate_t5c_df2(
    sigma_ref_kpc: float,
    f_leak: float,
) -> dict:
    """
    [Secondary Test T5c - PREREG.md Sec 5.6 lines 284-291]
    NGC 1052-DF2 stress check using a 3D Plummer sphere (M_* = 2.0e8 M_sun, R_e = 2.2 kpc)
    plus the NGC 1052 group baryon contribution (M_b = 1.0e11 M_sun at d_3D = sqrt(3/2)*80 = 98.0 kpc),
    evaluated with the T5-A frozen sigma_ref_kpc and T2-A-Pantheon+ frozen f_leak.
    """
    m_star_df2 = 2.0e8  # M_sun
    r_e = 2.2           # kpc
    m_group = 1.0e11    # M_sun
    d_3d_group = math.sqrt(1.5) * 80.0  # 97.97959 kpc
    r_factor = 6.0 * (1.0 - f_leak)

    # Discretize 3D Plummer sphere M_b(< r') = M_* * r'^3 / (r'^2 + R_e^2)^(3/2)
    r_edges = np.concatenate([
        np.linspace(0.0, r_e, 400),
        np.geomspace(r_e, 200.0 * r_e, 601)[1:],
    ])
    m_edges = m_star_df2 * (r_edges ** 3) / ((r_edges ** 2 + r_e ** 2) ** 1.5)
    r_mid = 0.5 * (r_edges[:-1] + r_edges[1:])
    dm_shells = m_edges[1:] - m_edges[:-1]

    def eval_at_radius(r_eval: float) -> dict:
        m_b_enc = m_star_df2 * (r_eval ** 3) / ((r_eval ** 2 + r_e ** 2) ** 1.5)
        f_df2 = kernel_f_sigma(np.array([[r_eval]]), r_mid[None, :], sigma_ref_kpc)[0]
        m_sh_df2 = float(r_factor * np.dot(f_df2, dm_shells))
        f_grp = float(kernel_f_sigma(np.array([[r_eval]]), np.array([[d_3d_group]]), sigma_ref_kpc)[0, 0])
        m_sh_group = float(r_factor * m_group * f_grp)
        m_pred = m_b_enc + m_sh_df2 + m_sh_group
        return {
            "r_eval_kpc": r_eval,
            "M_b_enc_1e8_Msun": round(m_b_enc / 1e8, 4),
            "M_sh_DF2_1e8_Msun": round(m_sh_df2 / 1e8, 4),
            "M_sh_group_1e8_Msun": round(m_sh_group / 1e8, 4),
            "M_pred_1e8_Msun": round(m_pred / 1e8, 4),
            "M_pred_Msun": float(m_pred),
        }

    res_27 = eval_at_radius(2.7)
    res_31 = eval_at_radius(3.1)
    res_76 = eval_at_radius(7.6)

    m_27_1e8 = res_27["M_pred_Msun"] / 1e8
    m_31_1e8 = res_31["M_pred_Msun"] / 1e8

    # PREREG.md lines 289-291:
    # PASS: M_pred(<2.7 kpc) <= 2.9e8 AND M_pred(<3.1 kpc) < 3.2e8
    # FAIL: M_pred(<2.7 kpc) > 3.7e8
    # INCONCLUSIVE: Every other outcome
    reasons = []
    if m_27_1e8 <= 2.9 and m_31_1e8 < 3.2:
        verdict = "PASS"
    elif m_27_1e8 > 3.7:
        verdict = "FAIL"
        reasons.append(f"M_pred(<2.7 kpc) = {m_27_1e8:.4f}e8 M_sun > 3.7e8 M_sun.")
    else:
        verdict = "INCONCLUSIVE"
        reasons.append(
            f"Intermediate DF2 mass: M_pred(<2.7 kpc)={m_27_1e8:.4f}e8 M_sun, M_pred(<3.1 kpc)={m_31_1e8:.4f}e8 M_sun."
        )

    return {
        "sigma_ref_kpc_used": round(sigma_ref_kpc, 6),
        "f_leak_used": round(f_leak, 6),
        "r_2p7_kpc_danieli19": res_27,
        "r_3p1_kpc_vd18": res_31,
        "r_7p6_kpc_vd18": res_76,
        "verdict": verdict,
        "reasons": reasons,
    }


def evaluate_rar_benchmark(
    train_galaxies: list[dict],
    test_galaxies: list[dict],
) -> dict:
    """
    [Benchmark Analysis - MULTIVERSE_STAGE1_EQUATIONS.md Sec 7 (f2)]
    Evaluate empirical RAR (g_dagger = 1.20e-10 m/s^2 = 3702.7 (km/s)^2 / kpc, and fitted g_dagger)
    on the same 88 training and 87 held-out SPARC galaxies.
    """
    def eval_rar(sample: list[dict], g_dag: float) -> dict:
        chi2_reds = []
        tot_chi2 = 0.0
        tot_pts = 0
        for gal in sample:
            g_bar = np.maximum(gal["v_bar_mono2"], 1e-8) / np.maximum(gal["R"], 1e-6)
            denom = 1.0 - np.exp(-np.sqrt(g_bar / g_dag))
            g_obs = g_bar / np.maximum(denom, 1e-12)
            v_rar = np.sqrt(np.maximum(gal["R"] * g_obs, 0.0))
            res = (gal["v_obs"] - v_rar) / gal["e_v_obs"]
            c2 = float(np.sum(res ** 2))
            chi2_reds.append(c2 / gal["n_pts"])
            tot_chi2 += c2
            tot_pts += gal["n_pts"]
        arr = np.array(chi2_reds, dtype=float)
        return {
            "sum_chi2_red": float(np.sum(arr)),
            "median_chi2_red": float(np.median(arr)),
            "mean_chi2_red": float(np.mean(arr)),
            "pooled_chi2_red": float(tot_chi2 / max(tot_pts, 1)),
            "frac_chi2_red_lt_2": float(np.mean(arr < 2.0)),
        }

    g_dag_fixed = 1.20e-10 / 3.24077929e-14  # 3702.81 (km/s)^2 / kpc
    opt = minimize_scalar(
        lambda g: eval_rar(train_galaxies, float(g))["sum_chi2_red"],
        bounds=(500.0, 15000.0),
        method="bounded",
        options={"xatol": 1e-3},
    )
    g_dag_fit = float(opt.x)
    return {
        "fixed_McGaugh16_g_dagger_1p2e-10": {
            "g_dagger_m_s2": 1.20e-10,
            "train_summary": eval_rar(train_galaxies, g_dag_fixed),
            "test_summary": eval_rar(test_galaxies, g_dag_fixed),
        },
        "fitted_g_dagger": {
            "g_dagger_m_s2": float(f"{g_dag_fit * 3.24077929e-14:.4e}"),
            "train_summary": eval_rar(train_galaxies, g_dag_fit),
            "test_summary": eval_rar(test_galaxies, g_dag_fit),
        },
    }


def compute_saturation_and_vc_tau_diagnostics(
    galaxies: list[dict],
    sigma_ref_kpc: float,
    f_leak: float,
    tau_lag_gyr: float,
) -> dict:
    """
    [Mechanistic Diagnostics f3 & f4 - MULTIVERSE_STAGE1_EQUATIONS.md Sec 7]
    1. Fraction of SPARC radial points where observed g_obs / g_bar exceeds the
       Gaussian-diffusion saturation cap 1 + 6(1 - f_leak).
    2. Comparison of fitted sigma_ref against v_flat * tau_lag across SPARC galaxies.
    """
    cap_ratio = 1.0 + 6.0 * (1.0 - f_leak)
    total_pts = 0
    exceed_cap_pts = 0
    galaxies_with_exceed = 0

    for gal in galaxies:
        ratio = (gal["v_obs"] ** 2) / np.maximum(gal["v_bar_mono2"], 1e-6)
        n_exc = int(np.sum(ratio > cap_ratio))
        total_pts += gal["n_pts"]
        exceed_cap_pts += n_exc
        if n_exc > 0:
            galaxies_with_exceed += 1

    kms_gyr_to_kpc = 1.022712
    vc_tau_list = [
        gal["v_flat_kms"] * tau_lag_gyr * kms_gyr_to_kpc
        for gal in galaxies
        if gal["v_flat_kms"] > 0.0
    ]

    return {
        "saturation_cap_ratio_1_plus_R": round(cap_ratio, 4),
        "total_radial_pts": total_pts,
        "pts_exceeding_cap": exceed_cap_pts,
        "frac_pts_exceeding_cap": round(exceed_cap_pts / max(total_pts, 1), 4),
        "galaxies_with_pts_exceeding_cap": galaxies_with_exceed,
        "frac_galaxies_exceeding_cap": round(galaxies_with_exceed / max(len(galaxies), 1), 4),
        "vc_tau_lag_check": {
            "tau_lag_gyr_used": tau_lag_gyr,
            "sigma_ref_kpc_used": round(sigma_ref_kpc, 4),
            "n_galaxies_with_vflat": len(vc_tau_list),
            "median_vc_tau_lag_kpc": round(float(np.median(vc_tau_list)), 3),
            "iqr_vc_tau_lag_kpc": [
                round(float(np.percentile(vc_tau_list, 25)), 3),
                round(float(np.percentile(vc_tau_list, 75)), 3),
            ],
        },
    }
