import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import json
import sys
import time
import numpy as np
import psutil
import dynesty

try:
    psutil.Process(os.getpid()).nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

H2H_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(H2H_DIR, ".."))
if H2H_DIR not in sys.path:
    sys.path.insert(0, H2H_DIR)
if os.path.join(ROOT_DIR, "scripts") not in sys.path:
    sys.path.insert(0, os.path.join(ROOT_DIR, "scripts"))

import cosmology as cosmo
import h2h_cosmology as h2h


def validate_rs_quadratures() -> dict:
    """
    Validate Reading A r_s(z_*) across Planck 2018 fiducial and prior-box test points
    using two independent quadratures: 128-node Gauss-Legendre (GL128) vs scipy.integrate.quad (QUAD).
    Requires relative difference < 1e-6.
    """
    test_points = [
        {"label": "Planck_2018_fiducial", "Omega_bc": 0.3138, "h": 0.6736, "wb100": 2.237},
        {"label": "Chen_2019_Table1_mean", "Omega_bc": 0.31388, "h": 0.6727, "wb100": 2.236},
        {"label": "Prior_low_corner", "Omega_bc": 0.15, "h": 0.55, "wb100": 1.85},
        {"label": "Prior_high_corner", "Omega_bc": 0.45, "h": 0.85, "wb100": 2.55},
        {"label": "M2_structural_fiducial", "Omega_bc": 0.310, "h": 0.652, "wb100": 100.0 * (0.652 ** 2) / 19.0},
    ]
    rows = []
    max_rel_diff = 0.0
    for pt in test_points:
        omega_b = pt["wb100"] / 100.0
        h = pt["h"]
        omega_bc = pt["Omega_bc"] * (h ** 2)
        omega_m = omega_bc + cosmo.OMEGA_NU_MASS_H2
        z_star = float(cosmo.z_star_hu_sugiyama(omega_b, omega_m))
        rs_gl128 = h2h.sound_horizon_rs_a5_gl128(z_star, omega_b, omega_bc, h=h)
        rs_quad, quad_err = h2h.sound_horizon_rs_a5_quad(z_star, omega_b, omega_bc, h=h)
        rs_chen = float(cosmo.sound_horizon_rs_chen(z_star, omega_b, omega_m))
        abs_diff = abs(rs_gl128 - rs_quad)
        rel_diff = abs_diff / rs_quad
        max_rel_diff = max(max_rel_diff, rel_diff)
        rows.append(
            {
                **pt,
                "z_star": z_star,
                "rs_reading_a_gl128_Mpc": rs_gl128,
                "rs_reading_a_quad_Mpc": rs_quad,
                "quad_est_abs_err_Mpc": quad_err,
                "abs_diff_gl128_vs_quad_Mpc": abs_diff,
                "rel_diff_gl128_vs_quad": rel_diff,
                "rs_reading_b_chen_Mpc": rs_chen,
                "rel_diff_chen_vs_a5": (rs_chen - rs_gl128) / rs_gl128,
            }
        )
    passed = bool(max_rel_diff < 1e-6)
    return {
        "passed": passed,
        "tolerance_rel": 1e-6,
        "max_rel_diff_gl128_vs_quad": max_rel_diff,
        "drag_calib_factor_reading_a": float(h2h._DRAG_CALIB_FACTOR_A5),
        "drag_calib_factor_reading_b": float(cosmo._DRAG_CALIB_FACTOR),
        "points": rows,
    }


def run_lcdm_sanity_check(data_dir: str) -> dict:
    """
    Sanity check before main runs: for LCDM (Reading B, matching Stage 2), the best-fit chi2
    from the nested-sampling run (nlive=1000, dlogz=0.01, bound='multi', sample='rwalk', seed=20261030)
    must match the Stage 2 LCDM chi2_min to within 0.1.
    Also records Reading A LCDM nested-sampling vs direct-optimizer chi2_min agreement.
    """
    with open(os.path.join(ROOT_DIR, "results", "part9_cosmology_results.json"), "r", encoding="utf-8") as f:
        part9 = json.load(f)

    stage2_chi2_pantheon = float(part9["T1"]["T1_L1_deciding"]["PantheonPlus"]["chi2_min_LCDM"])
    stage2_chi2_dovekie = float(part9["T1"]["T1_L1_deciding"]["DES_Dovekie"]["chi2_min_LCDM"])

    bao_like = cosmo.DESIBAOLikelihood(data_dir, lya_mode="joint_ap_deciding")
    cmb_like = cosmo.CMBLikelihood(table="lcdm", mode="full_3x3")
    sn_map = {
        "Pantheon+": (cosmo.PantheonPlusLikelihood(data_dir), stage2_chi2_pantheon),
        "DES-Dovekie": (cosmo.DESDovekieLikelihood(data_dir), stage2_chi2_dovekie),
    }

    def prior_transform_lcdm(u):
        # Omega_bc in [0.10, 0.50], h in [0.50, 0.90], 100*omega_b in [1.80, 2.60]
        return np.array(
            [
                0.10 + 0.40 * u[0],
                0.50 + 0.40 * u[1],
                1.80 + 0.80 * u[2],
            ],
            dtype=float,
        )

    sanity_results = {}
    all_passed = True

    for sn_name, (sn_like, stage2_target) in sn_map.items():
        def loglike(theta):
            chi2 = h2h.joint_chi2_cpl_reading(
                float(theta[0]), float(theta[1]), float(theta[2]), -1.0, 0.0, "B", bao_like, cmb_like, sn_like
            )
            if not np.isfinite(chi2):
                return -1e30
            return -0.5 * chi2

        t0 = time.perf_counter()
        rng = np.random.default_rng(20261030)
        sampler = dynesty.NestedSampler(
            loglike,
            prior_transform_lcdm,
            ndim=3,
            nlive=1000,
            bound="multi",
            sample="rwalk",
            rstate=rng,
        )
        sampler.run_nested(dlogz=0.01, print_progress=False)
        elapsed_s = time.perf_counter() - t0
        res = sampler.results

        best_idx = int(np.argmax(res.logl))
        chi2_min_ns = float(-2.0 * res.logl[best_idx])
        best_theta_ns = [float(x) for x in res.samples[best_idx]]
        abs_diff = abs(chi2_min_ns - stage2_target)
        passed = bool(abs_diff <= 0.1)
        all_passed = all_passed and passed

        sanity_results[sn_name] = {
            "sn_compilation": sn_name,
            "reading": "B",
            "seed": 20261030,
            "nlive": 1000,
            "dlogz": 0.01,
            "stage2_chi2_min_LCDM": stage2_target,
            "nested_sampling_chi2_min": chi2_min_ns,
            "abs_diff_chi2": abs_diff,
            "tolerance_chi2": 0.1,
            "passed": passed,
            "best_fit_theta_ns_Omega_bc_h_100wb": best_theta_ns,
            "lnZ": float(res.logz[-1]),
            "lnZ_err_dynesty": float(res.logzerr[-1]),
            "ncall": int(np.sum(res.ncall)),
            "niter": int(res.niter),
            "elapsed_sec": elapsed_s,
        }

    return {
        "all_passed": all_passed,
        "runs": sanity_results,
    }


def main():
    data_dir = os.path.join(ROOT_DIR, "data")
    print("1. Validating Reading A r_s(z_*) two independent quadratures (GL128 vs QUAD)...")
    quad_val = validate_rs_quadratures()
    print(f"   Max relative difference: {quad_val['max_rel_diff_gl128_vs_quad']:.3e} (passed={quad_val['passed']})")

    print("2. Recomputing Gate G9-b under Reading A (literal registered a5 integral)...")
    g9b_a = h2h.run_gate_g9b_reading_a()
    print(
        f"   G9-b Reading A: h = {g9b_a['obtained_h']:.6f} +- {g9b_a['obtained_sigma_h']:.6f}, "
        f"diff_h = {g9b_a['diff_h_sigma_vs_0p6736_0p0054']:.4f} sigma (vs 0.6736+-0.0054), "
        f"{g9b_a['diff_h_sigma_vs_0p6727_0p0060']:.4f} sigma (vs 0.6727+-0.0060), "
        f"verdict = {g9b_a['verdict']}"
    )

    with open(os.path.join(ROOT_DIR, "results", "validation_gates_g9_final.json"), "r", encoding="utf-8") as f:
        g9_stage2 = json.load(f)

    print("3. Running LCDM nested-sampling chi2_min sanity check (Reading B, seed=20261030)...")
    sanity = run_lcdm_sanity_check(data_dir)
    for k, v in sanity["runs"].items():
        print(
            f"   {k}: NS chi2_min = {v['nested_sampling_chi2_min']:.6f} vs Stage 2 = {v['stage2_chi2_min_LCDM']:.6f} "
            f"(|diff| = {v['abs_diff_chi2']:.6f} <= 0.1 -> passed={v['passed']}), "
            f"lnZ = {v['lnZ']:.4f} +- {v['lnZ_err_dynesty']:.4f} ({v['elapsed_sec']:.1f}s)"
        )

    out = {
        "label": "supplementary analysis, not pre-registered",
        "completed_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "rs_two_quadrature_validation": quad_val,
        "gate_G9b_reading_A": g9b_a,
        "gate_G9b_reading_B_stage2": g9_stage2["G9-b"],
        "lcdm_nested_sampling_sanity_check": sanity,
    }
    out_path = os.path.join(H2H_DIR, "validation_h2h.json")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, indent=2)
    print(f"Saved validation results to {out_path}")

    assert quad_val["passed"], "Two-quadrature r_s(z_*) validation failed!"
    assert sanity["all_passed"], "LCDM nested-sampling chi2_min sanity check failed!"


if __name__ == "__main__":
    main()
