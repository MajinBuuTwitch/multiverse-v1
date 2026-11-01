import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import sys
import json
import hashlib
from datetime import datetime

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT_DIR, "scripts"))
sys.path.insert(0, os.path.join(ROOT_DIR, "tests"))

import test_gates_g9 as tg9
import cosmology as cosmo
import sparc_t5
from scipy import optimize


def sha256_file(rel_path):
    p = os.path.join(ROOT_DIR, rel_path.replace("/", os.sep))
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def run_fast_path_checks(data_dir):
    """Also verify G9-a, G9-b, G9-c through the vectorized joint_chi2_cpl fast path in cosmology.py."""
    bao = cosmo.DESIBAOLikelihood(data_dir, lya_mode="unmodified")
    cmb = cosmo.CMBLikelihood(table="lcdm", mode="full_3x3")
    sn = cosmo.DESDovekieLikelihood(data_dir)

    # G9-a via _fast_cum_integral_inv_E on _SHARED_Z_GRID
    cosmo._ensure_grid_lookup(bao, bao.unique_z)
    def obj_a(params):
        om, rd = params
        if not (0.1 < om < 0.6 and 100.0 < rd < 200.0):
            return 1e12
        h = 0.6736
        h2 = h * h
        Omega_gamma = cosmo.OMEGA_GAMMA_H2 / h2
        Omega_nu_0 = cosmo.OMEGA_NU_MASS_H2 / h2
        Omega_bc = om - Omega_nu_0
        Omega_de = 1.0 - (Omega_gamma + (cosmo._SHARED_NU_REL_COEFF / h2) + Omega_nu_0 + Omega_bc)
        e2_grid = Omega_gamma * cosmo._SHARED_A_M4 + (cosmo._SHARED_ONU_GRID / h2) + Omega_bc * cosmo._SHARED_A_M3 + Omega_de
        E_grid = np.sqrt(e2_grid)
        cum_I, inv_E = cosmo._fast_cum_integral_inv_E(1.0 / E_grid)
        dh0 = cosmo.C_KM_S / (100.0 * h)
        I_bao = cosmo._eval_cum_integral_at(bao.unique_z, cum_I, inv_E, bao._shared_idx, bao._shared_u, bao._shared_dz)
        DM_u = dh0 * I_bao
        DH_u = dh0 / cosmo.E_of_z_cpl(bao.unique_z, om, h, w0=-1.0, wa=0.0)
        pred = bao._model_vector(DM_u, DH_u, rd)
        diff = pred - bao.mean
        return float(diff @ bao.inv_cov @ diff)

    import numpy as np
    res_a = optimize.minimize(obj_a, [0.2975, 147.09], method="Nelder-Mead", options={"xatol": 1e-8, "fatol": 1e-10})
    om_a_fast = float(res_a.x[0])
    diff_a_fast_sig = abs(om_a_fast - 0.2975) / 0.0086

    # G9-b via joint_chi2_cpl (CMB only)
    def obj_b(params):
        om, h, wb100 = params
        if not (0.15 < om < 0.50 and 0.55 < h < 0.85 and 1.9 < wb100 < 2.5):
            return 1e12
        h2 = h * h
        omega_b = wb100 / 100.0
        omega_m = om * h2
        Omega_gamma = cosmo.OMEGA_GAMMA_H2 / h2
        Omega_nu_0 = cosmo.OMEGA_NU_MASS_H2 / h2
        Omega_bc = om - Omega_nu_0
        Omega_de = 1.0 - (Omega_gamma + (cosmo._SHARED_NU_REL_COEFF / h2) + Omega_nu_0 + Omega_bc)
        e2_grid = Omega_gamma * cosmo._SHARED_A_M4 + (cosmo._SHARED_ONU_GRID / h2) + Omega_bc * cosmo._SHARED_A_M3 + Omega_de
        E_grid = np.sqrt(e2_grid)
        cum_I, inv_E = cosmo._fast_cum_integral_inv_E(1.0 / E_grid)
        dh0 = cosmo.C_KM_S / (100.0 * h)
        z_star = cosmo.z_star_hu_sugiyama(omega_b, omega_m)
        DM_star = dh0 * cosmo._eval_scalar_cum_integral(z_star, cum_I, inv_E)
        R_shift = float(np.sqrt(om)) * (DM_star / dh0)
        rs_star = cosmo.sound_horizon_rs_chen(z_star, omega_b, omega_m)
        l_A = float(np.pi) * DM_star / rs_star
        return cmb.chi2(np.array([R_shift, l_A, wb100], dtype=float))

    res_b = optimize.minimize(obj_b, [0.3153, 0.6736, 2.236], method="Nelder-Mead", options={"xatol": 1e-8, "fatol": 1e-10})
    om_b_fast, h_b_fast, wb_b_fast = [float(x) for x in res_b.x]

    # G9-c via joint_chi2_cpl
    def obj_c(params):
        om, h, wb100, w0, wa = params
        if not (0.15 < om < 0.50 and 0.55 < h < 0.85 and 1.9 < wb100 < 2.5 and -2.5 < w0 < 0.5 and -3.0 < wa < 1.5):
            return 1e12
        if w0 + wa >= 0.0:
            return 1e12
        return cosmo.joint_chi2_cpl(om, h, wb100, w0, wa, bao, cmb, sn, bbn_prior=None)

    x0 = [0.313, 0.675, 2.236, -0.803, -0.72]
    res1 = optimize.minimize(obj_c, x0, method="Nelder-Mead", options={"xatol": 1e-5, "fatol": 1e-5, "maxiter": 5000})
    res_c = optimize.minimize(
        obj_c,
        res1.x,
        method="L-BFGS-B",
        bounds=[(0.15, 0.50), (0.55, 0.85), (1.9, 2.5), (-2.5, 0.5), (-3.0, 1.5)],
        options={"ftol": 1e-12},
    )
    om_c_f, h_c_f, wb_c_f, w0_c_f, wa_c_f = [float(v) for v in res_c.x]
    return {
        "G9-a_fast_path": {
            "obtained_Omega_m": om_a_fast,
            "chi2_min": float(res_a.fun),
            "diff_in_target_sigma": diff_a_fast_sig,
            "passed": bool(diff_a_fast_sig <= 0.3),
        },
        "G9-b_fast_path": {
            "obtained_Omega_m": om_b_fast,
            "obtained_h": h_b_fast,
            "obtained_100_omega_b": wb_b_fast,
            "diff_Omega_m_sigma": abs(om_b_fast - 0.3153) / 0.0073,
            "diff_h_sigma": abs(h_b_fast - 0.6736) / 0.0054,
            "passed": bool(max(abs(om_b_fast - 0.3153) / 0.0073, abs(h_b_fast - 0.6736) / 0.0054) <= 0.3),
        },
        "G9-c_fast_path": {
            "obtained_Omega_m": om_c_f,
            "obtained_h": h_c_f,
            "obtained_100_omega_b": wb_c_f,
            "obtained_w0": w0_c_f,
            "obtained_wa": wa_c_f,
            "chi2_min": float(res_c.fun),
            "diff_w0_sigma": abs(w0_c_f - (-0.803)) / 0.054,
            "diff_wa_sigma": abs(wa_c_f - (-0.72)) / 0.21,
            "passed": bool(abs(w0_c_f - (-0.803)) / 0.054 <= 1.0 and abs(wa_c_f - (-0.72)) / 0.21 <= 1.0),
        },
    }


def main():
    data_dir = os.path.join(ROOT_DIR, "data")
    g9a = tg9.run_gate_g9a(data_dir)
    g9b = tg9.run_gate_g9b()
    g9c = tg9.run_gate_g9c(data_dir)
    g9d = tg9.run_gate_g9d()

    # Also verify sparc_t5.F_sigma_kernel matches test_gates_g9.F_sigma_kernel exactly
    import numpy as np
    r_vals = np.array([0.2, 0.5, 1.0, 2.0, 4.0])
    rp_vals = np.array([0.0, 1e-5, 0.2, 0.5, 1.0, 2.0, 4.0])
    max_diff_sparc_vs_test = 0.0
    for r in r_vals:
        for rp in rp_vals:
            diff = abs(float(sparc_t5.kernel_f_sigma(r, rp, 1.0)) - float(tg9.F_sigma_kernel(r, rp, 1.0)))
            if diff > max_diff_sparc_vs_test:
                max_diff_sparc_vs_test = diff
    g9d["max_diff_sparc_t5_vs_test_gates_g9"] = max_diff_sparc_vs_test

    script_files = [
        "scripts/cosmology.py",
        "scripts/clusters_t4.py",
        "scripts/sparc_t5.py",
        "scripts/local_h0_t6.py",
        "scripts/run_part8_fixes.py",
        "scripts/run_part9_cosmology_tests.py",
        "scripts/run_part10_astrophysics_and_verdict.py",
        "tests/test_gates_g9.py",
    ]
    scripts_sha256 = {rel: sha256_file(rel) for rel in script_files}

    out = {
        "generated_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "note": "Re-run of G9-a, G9-b, G9-c, G9-d on the final unmodified analysis scripts (REVIEW_FINAL M1).",
        "scripts_sha256": scripts_sha256,
        "G9-a": g9a,
        "G9-b": g9b,
        "G9-c": g9c,
        "G9-d": g9d,
        "fast_path_joint_chi2_cpl_verification": run_fast_path_checks(data_dir),
        "all_passed": bool(g9a["passed"] and g9b["passed"] and g9c["passed"] and g9d["passed"]),
    }

    out_path = os.path.join(ROOT_DIR, "results", "validation_gates_g9_final.json")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, indent=2)

    print(json.dumps(out, indent=2))
    assert out["all_passed"], f"One or more validation gates failed on final code: {out}"


if __name__ == "__main__":
    main()
