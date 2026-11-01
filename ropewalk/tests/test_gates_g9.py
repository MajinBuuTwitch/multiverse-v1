import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import sys
import json
import numpy as np
from scipy import optimize, special, stats

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT_DIR, "scripts"))

import cosmology as cosmo


def F_sigma_kernel(r, rp, sigma):
    """Piecewise 3D Gaussian enclosed-mass kernel F_sigma(r, r') from PREREG.md §5.6 & MULTIVERSE_STAGE1_EQUATIONS.md (f3)."""
    r = np.asarray(r, dtype=float)
    rp = np.asarray(rp, dtype=float)
    r_b, rp_b = np.broadcast_arrays(r, rp)
    out = np.empty_like(r_b, dtype=float)
    mask_small = (rp_b / sigma) < 1e-4
    if np.any(mask_small):
        rs = r_b[mask_small]
        x = rs / (np.sqrt(2.0) * sigma)
        out[mask_small] = special.erf(x) - np.sqrt(2.0 / np.pi) * (rs / sigma) * np.exp(-0.5 * (rs / sigma) ** 2)
    if np.any(~mask_small):
        rn = r_b[~mask_small]
        rpn = rp_b[~mask_small]
        xp = (rn + rpn) / (np.sqrt(2.0) * sigma)
        xm = (rn - rpn) / (np.sqrt(2.0) * sigma)
        term1 = 0.5 * (special.erf(xp) + special.erf(xm))
        term2 = (1.0 / np.sqrt(2.0 * np.pi)) * (sigma / rpn) * (
            np.exp(-0.5 * ((rn - rpn) / sigma) ** 2) - np.exp(-0.5 * ((rn + rpn) / sigma) ** 2)
        )
        out[~mask_small] = term1 - term2
    return out


def run_gate_g9a(data_dir):
    """Gate G9-a: DESI DR2 BAO-only flat LCDM validation on unmodified desi_bao_dr2.
    Target: Omega_m = 0.2975 +- 0.0086 within 0.3 sigma (|Omega_m - 0.2975| <= 0.00258).
    """
    bao = cosmo.DESIBAOLikelihood(data_dir, lya_mode="unmodified")

    # In BAO-only flat LCDM, the observables depend on Omega_m and hr_d = h * r_d (in Mpc).
    # Fix h=0.6736 and optimize (Omega_m, r_d_override)
    def obj(params):
        om, rd = params
        if not (0.1 < om < 0.6 and 100.0 < rd < 200.0):
            return 1e12
        return bao.chi2_cpl(om, 0.6736, 0.02237, w0=-1.0, wa=0.0, rd_override=rd)

    res = optimize.minimize(obj, [0.2975, 147.09], method="Nelder-Mead", options={"xatol": 1e-8, "fatol": 1e-10})
    om_best, rd_best = float(res.x[0]), float(res.x[1])
    chi2_min = float(res.fun)

    # Profile 1-sigma uncertainty on Omega_m
    eps = 1e-4
    # Hessian of 2D chi2
    p0 = np.array([om_best, rd_best])
    H = np.zeros((2, 2))
    steps = [1e-4, 1e-2]
    for i in range(2):
        for j in range(2):
            e_i = np.zeros(2)
            e_j = np.zeros(2)
            e_i[i] = steps[i]
            e_j[j] = steps[j]
            H[i, j] = (
                obj(p0 + e_i + e_j) - obj(p0 + e_i - e_j) - obj(p0 - e_i + e_j) + obj(p0 - e_i - e_j)
            ) / (4.0 * steps[i] * steps[j])
    cov = np.linalg.inv(0.5 * H)
    sig_om = float(np.sqrt(cov[0, 0]))
    diff_sigma = abs(om_best - 0.2975) / 0.0086
    passed = bool(diff_sigma <= 0.3)
    return {
        "gate": "G9-a",
        "target_Omega_m": 0.2975,
        "target_sigma": 0.0086,
        "obtained_Omega_m": om_best,
        "obtained_sigma": sig_om,
        "obtained_hrd_Mpc": 0.6736 * rd_best,
        "chi2_min": chi2_min,
        "diff_in_target_sigma": diff_sigma,
        "tolerance_sigma": 0.3,
        "passed": passed,
    }


def run_gate_g9b():
    """Gate G9-b: Compressed CMB prior & r_s(z_*) validation on Chen, Huang & Wang (2019, Table 1 & Table 2) LCDM.
    Chen et al. (2019) Table 2 flat LCDM from distance priors:
      Omega_m = 0.3153 +- 0.0073 (or 0.3166 +- 0.0084 TT,TE,EE+lowE), h = 0.6727 +- 0.0060, 100*omega_b = 2.236 +- 0.015.
    """
    cmb = cosmo.CMBLikelihood(table="lcdm", mode="full_3x3")

    def obj(params):
        om, h, wb100 = params
        if not (0.15 < om < 0.50 and 0.55 < h < 0.85 and 1.9 < wb100 < 2.5):
            return 1e12
        vec = cosmo.cmb_priors_observable_cpl(om, h, wb100 / 100.0, w0=-1.0, wa=0.0)
        return cmb.chi2(vec)

    res = optimize.minimize(obj, [0.3153, 0.6736, 2.236], method="Nelder-Mead", options={"xatol": 1e-8, "fatol": 1e-10})
    om_best, h_best, wb100_best = [float(x) for x in res.x]

    # Compute numerical Jacobian of (R, l_A, 100*omega_b) wrt (om, h, wb100) for Fisher covariance
    p0 = np.array([om_best, h_best, wb100_best])
    steps = np.array([1e-4, 1e-4, 1e-4])
    J = np.zeros((3, 3))
    for j in range(3):
        dp = np.zeros(3)
        dp[j] = steps[j]
        v_plus = cosmo.cmb_priors_observable_cpl(*(p0 + dp)[:2], (p0[2] + dp[2]) / 100.0)
        v_minus = cosmo.cmb_priors_observable_cpl(*(p0 - dp)[:2], (p0[2] - dp[2]) / 100.0)
        J[:, j] = (v_plus - v_minus) / (2.0 * steps[j])
    cov_params = np.linalg.inv(J.T @ cmb.inv_cov3 @ J)
    sig_om, sig_h, sig_wb100 = [float(np.sqrt(cov_params[i, i])) for i in range(3)]

    # Compare against Planck 2018 / Chen+19 Table 2 flat LCDM (Omega_m = 0.3153 +- 0.0073, h = 0.6736 +- 0.0054, 100*omega_b = 2.236 +- 0.015)
    diff_om_sig = abs(om_best - 0.3153) / 0.0073
    diff_h_sig = abs(h_best - 0.6736) / 0.0054
    diff_wb_sig = abs(wb100_best - 2.236) / 0.015
    max_diff_sig = max(diff_om_sig, diff_h_sig, diff_wb_sig)
    passed = bool(max_diff_sig <= 0.3)
    return {
        "gate": "G9-b",
        "obtained_Omega_m": om_best,
        "obtained_sigma_Omega_m": sig_om,
        "obtained_h": h_best,
        "obtained_sigma_h": sig_h,
        "obtained_100_omega_b": wb100_best,
        "obtained_sigma_100_omega_b": sig_wb100,
        "diff_Omega_m_sigma": diff_om_sig,
        "diff_h_sigma": diff_h_sig,
        "diff_wb_sigma": diff_wb_sig,
        "max_diff_sigma": max_diff_sig,
        "tolerance_sigma": 0.3,
        "passed": passed,
    }


def run_gate_g9c(data_dir):
    """Gate G9-c: Full DESI (unmodified BAO) + CMB (LCDM Table 1) + DES-Dovekie w0waCDM validation.
    Target: Popovic et al. (2025, Table 11) w0 = -0.803 +- 0.054, wa = -0.72 +- 0.21 within 1.0 sigma.
    """
    bao = cosmo.DESIBAOLikelihood(data_dir, lya_mode="unmodified")
    cmb = cosmo.CMBLikelihood(table="lcdm", mode="full_3x3")
    sn = cosmo.DESDovekieLikelihood(data_dir)

    def obj(params):
        om, h, wb100, w0, wa = params
        if not (0.15 < om < 0.50 and 0.55 < h < 0.85 and 1.9 < wb100 < 2.5 and -2.5 < w0 < 0.5 and -3.0 < wa < 1.5):
            return 1e12
        if w0 + wa >= 0.0:
            return 1e12
        wb = wb100 / 100.0
        c_bao = bao.chi2_cpl(om, h, wb, w0=w0, wa=wa)
        vec_cmb = cosmo.cmb_priors_observable_cpl(om, h, wb, w0=w0, wa=wa)
        c_cmb = cmb.chi2(vec_cmb)
        c_sn = sn.chi2_cpl(om, h, w0=w0, wa=wa)
        return c_bao + c_cmb + c_sn

    x0 = [0.313, 0.675, 2.236, -0.803, -0.72]
    res1 = optimize.minimize(obj, x0, method="Nelder-Mead", options={"xatol": 1e-5, "fatol": 1e-5, "maxiter": 5000})
    res = optimize.minimize(
        obj,
        res1.x,
        method="L-BFGS-B",
        bounds=[(0.15, 0.50), (0.55, 0.85), (1.9, 2.5), (-2.5, 0.5), (-3.0, 1.5)],
        options={"ftol": 1e-12},
    )
    om_b, h_b, wb100_b, w0_b, wa_b = [float(v) for v in res.x]
    chi2_min = float(res.fun)

    diff_w0_sig = abs(w0_b - (-0.803)) / 0.054
    diff_wa_sig = abs(wa_b - (-0.72)) / 0.21
    passed = bool(diff_w0_sig <= 1.0 and diff_wa_sig <= 1.0)
    return {
        "gate": "G9-c",
        "target_w0": -0.803,
        "target_sigma_w0": 0.054,
        "target_wa": -0.72,
        "target_sigma_wa": 0.21,
        "obtained_Omega_m": om_b,
        "obtained_h": h_b,
        "obtained_100_omega_b": wb100_b,
        "obtained_w0": w0_b,
        "obtained_wa": wa_b,
        "chi2_min": chi2_min,
        "diff_w0_sigma": diff_w0_sig,
        "diff_wa_sigma": diff_wa_sig,
        "tolerance_sigma": 1.0,
        "passed": passed,
    }


def run_gate_g9d():
    """Gate G9-d: Rotation-curve kernel unit test across 5x7 grid including r'=0 and r'=1e-5*sigma
    against scipy.stats.ncx2.cdf((r/sigma)**2, df=3, nc=(rp/sigma)**2) to < 1e-10.
    """
    r_vals = np.array([0.2, 0.5, 1.0, 2.0, 4.0])
    rp_vals = np.array([0.0, 1e-5, 0.2, 0.5, 1.0, 2.0, 4.0])
    sigma = 1.0
    max_abs_err = 0.0
    for r in r_vals:
        for rp in rp_vals:
            val_k = float(F_sigma_kernel(r, rp, sigma))
            if rp == 0.0:
                val_ref = float(stats.chi2.cdf((r / sigma) ** 2, df=3))
            else:
                val_ref = float(stats.ncx2.cdf((r / sigma) ** 2, df=3, nc=(rp / sigma) ** 2))
            err = abs(val_k - val_ref)
            if err > max_abs_err:
                max_abs_err = err
    passed = bool(max_abs_err < 1e-10)
    return {
        "gate": "G9-d",
        "numpy_version": np.__version__,
        "scipy_version": sys.modules["scipy"].__version__,
        "max_abs_error": max_abs_err,
        "tolerance": 1e-10,
        "passed": passed,
    }


def main():
    data_dir = os.path.join(ROOT_DIR, "data")
    g9a = run_gate_g9a(data_dir)
    print("G9-a:", json.dumps(g9a, indent=2))
    g9b = run_gate_g9b()
    print("G9-b:", json.dumps(g9b, indent=2))
    g9c = run_gate_g9c(data_dir)
    print("G9-c:", json.dumps(g9c, indent=2))
    g9d = run_gate_g9d()
    print("G9-d:", json.dumps(g9d, indent=2))

    out = {
        "G9-a": g9a,
        "G9-b": g9b,
        "G9-c": g9c,
        "G9-d": g9d,
        "all_passed": bool(g9a["passed"] and g9b["passed"] and g9c["passed"] and g9d["passed"]),
    }
    out_path = os.path.join(ROOT_DIR, "results", "validation_gates_g9.json")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, indent=2)
    print("Saved validation gate results to", out_path)
    assert out["all_passed"], f"One or more validation gates failed: {out}"


if __name__ == "__main__":
    main()
