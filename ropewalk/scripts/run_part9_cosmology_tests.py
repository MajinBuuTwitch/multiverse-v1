import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import datetime
import json
import math
import multiprocessing as mp
from pathlib import Path
import numpy as np
import psutil
import emcee
from scipy.optimize import minimize
from scipy.stats import chi2

from cosmology import (
    OMEGA_NU_MASS_H2,
    CMBLikelihood,
    DESIBAOLikelihood,
    PantheonPlusLikelihood,
    DESDovekieLikelihood,
    joint_chi2_cpl,
    joint_chi2_law1,
)
from run_part8_fixes import set_below_normal_priority, compute_split_rhat_and_ess
from local_h0_t6 import load_pantheon_plus_full, evaluate_t6_hubble_flow, compute_coincidence_window

N_CORES = 12
SEED = 20261030


def polish_chi2_min(neg2logp_fn, top_samples: list[np.ndarray], bounds: list[tuple[float, float]]) -> tuple[float, np.ndarray]:
    """
    [Registered Optimizer Protocol - PREREG.md Sec 4 line 99]
    Compute chi2_min by running Nelder-Mead (xatol=1e-6, fatol=1e-6, maxiter=10000)
    initialized from the 5 highest-likelihood MCMC samples, followed by bounded L-BFGS-B (ftol=1e-12).
    """
    best_val = float("inf")
    best_x = top_samples[0].copy()

    for x_init in top_samples:
        res_nm = minimize(
            neg2logp_fn,
            x_init,
            method="Nelder-Mead",
            options={"xatol": 1e-6, "fatol": 1e-6, "maxiter": 10000},
        )
        if float(res_nm.fun) < best_val:
            best_val = float(res_nm.fun)
            best_x = res_nm.x.copy()

        res_lb = minimize(
            neg2logp_fn,
            res_nm.x,
            method="L-BFGS-B",
            bounds=bounds,
            options={"ftol": 1e-12, "maxiter": 5000},
        )
        if float(res_lb.fun) < best_val:
            best_val = float(res_lb.fun)
            best_x = res_lb.x.copy()

    return best_val, best_x


def run_t1_or_t2b_mcmc_worker(task: dict) -> dict:
    """
    Worker function running one complete MCMC + polished chi2_min fit for:
      - 'LCDM': 3 params (Omega_m, h, 100*omega_b)
      - 'LAW1': 4 params (Omega_m, h, 100*omega_b, gamma_u)
      - 'CPL':  5 params (Omega_m, h, 100*omega_b, w0, wa) with w0 + wa < 0
      - 'T2B':  4 params (Omega_m, h, w0, wa) with 100*omega_b = 100*h^2/19 constrained inside likelihood
    """
    set_below_normal_priority()
    data_dir = task["data_dir"]
    run_id = task["run_id"]
    model_kind = task["model_kind"]
    sn_name = task["sn_name"]
    cmb_table = task.get("cmb_table", "lcdm")
    cmb_mode = task.get("cmb_mode", "full_3x3")
    lya_mode = task.get("lya_mode", "joint_ap_deciding")
    bbn_prior = task.get("bbn_prior", None)
    seed_offset = int(task["seed_offset"])

    bao_like = DESIBAOLikelihood(data_dir, lya_mode=lya_mode)
    cmb_like = CMBLikelihood(table=cmb_table, mode=cmb_mode)
    sn_like = PantheonPlusLikelihood(data_dir) if sn_name == "Pantheon+" else DESDovekieLikelihood(data_dir)

    if model_kind == "LCDM":
        n_dim = 3
        bounds = [(0.1, 0.6), (0.5, 0.9), (1.8, 2.6)]
        x0 = np.array([0.302, 0.683, 2.240], dtype=float)
        scales = np.array([0.002, 0.002, 0.008], dtype=float)

        def neg2logp(theta):
            om, h, wb100 = theta
            if not (0.1 <= om <= 0.6 and 0.5 <= h <= 0.9 and 1.8 <= wb100 <= 2.6):
                return 1e30
            c2 = joint_chi2_cpl(om, h, wb100, -1.0, 0.0, bao_like, cmb_like, sn_like, bbn_prior=bbn_prior)
            return c2 if np.isfinite(c2) else 1e30

    elif model_kind == "LAW1":
        n_dim = 4
        bounds = [(0.1, 0.6), (0.5, 0.9), (1.8, 2.6), (0.0, 2.0)]
        x0 = np.array([0.305, 0.678, 2.238, 0.06], dtype=float)
        scales = np.array([0.002, 0.002, 0.008, 0.015], dtype=float)

        def neg2logp(theta):
            om, h, wb100, gamma_u = theta
            if not (0.1 <= om <= 0.6 and 0.5 <= h <= 0.9 and 1.8 <= wb100 <= 2.6 and 0.0 <= gamma_u <= 2.0):
                return 1e30
            c2 = joint_chi2_law1(om, h, wb100, gamma_u, bao_like, cmb_like, sn_like, bbn_prior=bbn_prior)
            return c2 if np.isfinite(c2) else 1e30

    elif model_kind == "CPL":
        n_dim = 5
        bounds = [(0.1, 0.6), (0.5, 0.9), (1.8, 2.6), (-3.0, 1.0), (-3.0, 2.0)]
        x0 = np.array([0.311, 0.676, 2.236, -0.83, -0.65], dtype=float)
        scales = np.array([0.003, 0.003, 0.008, 0.02, 0.08], dtype=float)

        def neg2logp(theta):
            om, h, wb100, w0, wa = theta
            if not (0.1 <= om <= 0.6 and 0.5 <= h <= 0.9 and 1.8 <= wb100 <= 2.6):
                return 1e30
            if not (-3.0 <= w0 <= 1.0 and -3.0 <= wa <= 2.0 and (w0 + wa) < 0.0):
                return 1e30
            c2 = joint_chi2_cpl(om, h, wb100, w0, wa, bao_like, cmb_like, sn_like, bbn_prior=bbn_prior)
            return c2 if np.isfinite(c2) else 1e30

    elif model_kind == "T2B":
        # Constrained fit with omega_b = h^2 / 19 -> 100*omega_b = 100 * h^2 / 19 (PREREG.md Sec 5.2 line 180)
        n_dim = 4
        bounds = [(0.1, 0.6), (0.5, 0.9), (-3.0, 1.0), (-3.0, 2.0)]
        x0 = np.array([0.315, 0.652, -0.82, -0.70], dtype=float)
        scales = np.array([0.003, 0.002, 0.02, 0.08], dtype=float)

        def neg2logp(theta):
            om, h, w0, wa = theta
            if not (0.1 <= om <= 0.6 and 0.5 <= h <= 0.9):
                return 1e30
            if not (-3.0 <= w0 <= 1.0 and -3.0 <= wa <= 2.0 and (w0 + wa) < 0.0):
                return 1e30
            wb100 = 100.0 * (h * h) / 19.0
            if not (1.8 <= wb100 <= 2.6):
                return 1e30
            c2 = joint_chi2_cpl(om, h, wb100, w0, wa, bao_like, cmb_like, sn_like, bbn_prior=bbn_prior)
            return c2 if np.isfinite(c2) else 1e30
    else:
        raise ValueError(f"Unknown model_kind: {model_kind}")

    def log_prob(theta):
        val = neg2logp(theta)
        if val >= 1e29:
            return -np.inf
        return -0.5 * val

    # Preliminary Nelder-Mead to center walkers
    res_init = minimize(neg2logp, x0, method="Nelder-Mead", options={"xatol": 1e-5, "fatol": 1e-5, "maxiter": 4000})
    center = res_init.x.copy()

    rng = np.random.default_rng(SEED + seed_offset)
    n_walkers = 32
    pos = center[None, :] + rng.normal(0.0, 1.0, size=(n_walkers, n_dim)) * scales[None, :]
    for i in range(n_walkers):
        for d in range(n_dim):
            low, high = bounds[d]
            pos[i, d] = np.clip(pos[i, d], low + 1e-4, high - 1e-4)
        if model_kind == "CPL" and (pos[i, 3] + pos[i, 4] >= -0.01):
            pos[i, 4] = -0.05 - pos[i, 3]
        if model_kind == "T2B" and (pos[i, 2] + pos[i, 3] >= -0.01):
            pos[i, 3] = -0.05 - pos[i, 2]

    sampler = emcee.EnsembleSampler(n_walkers, n_dim, log_prob)
    n_burn = 1000
    n_prod = 4000
    state = sampler.run_mcmc(pos, n_burn, progress=False)
    sampler.reset()
    state = sampler.run_mcmc(state, n_prod, progress=False)

    chain = sampler.get_chain()
    diag = compute_split_rhat_and_ess(chain)

    ext_count = 0
    while (diag["max_rhat_minus_1"] >= 0.01 or diag["min_ess"] <= 1000.0) and ext_count < 2:
        state = sampler.run_mcmc(state, 2000, progress=False)
        chain = sampler.get_chain()
        diag = compute_split_rhat_and_ess(chain)
        ext_count += 1

    flat = chain.reshape((-1, n_dim))
    logp_flat = sampler.get_log_prob().reshape(-1)
    top5_idx = np.argsort(logp_flat)[-5:][::-1]
    top5_samples = [flat[idx] for idx in top5_idx]

    chi2_min, best_x = polish_chi2_min(neg2logp, top5_samples, bounds)

    def summarize(arr: np.ndarray) -> dict:
        q16, q50, q84 = np.percentile(arr, [16.0, 50.0, 84.0])
        return {
            "median": round(float(q50), 6),
            "mean": round(float(np.mean(arr)), 6),
            "std": round(float(np.std(arr, ddof=1)), 6),
            "sigma_68": round(float(0.5 * (q84 - q16)), 6),
        }

    out = {
        "run_id": run_id,
        "model_kind": model_kind,
        "sn_dataset": sn_name,
        "cmb_table": cmb_table,
        "cmb_mode": cmb_mode,
        "lya_mode": lya_mode,
        "n_walkers": n_walkers,
        "n_burn": n_burn,
        "n_prod": int(chain.shape[0]),
        "n_samples_total": int(flat.shape[0]),
        "chi2_min": round(float(chi2_min), 6),
        "best_fit_vector": [round(float(v), 6) for v in best_x],
        "convergence": diag,
        "converged": bool(diag["max_rhat_minus_1"] < 0.01 and diag["min_ess"] > 1000.0),
    }

    if model_kind == "LCDM":
        out["parameters"] = {
            "Omega_m_tot": summarize(flat[:, 0]),
            "h": summarize(flat[:, 1]),
            "100_omega_b": summarize(flat[:, 2]),
        }
    elif model_kind == "LAW1":
        om_s, h_s, wb_s, gu_s = flat[:, 0], flat[:, 1], flat[:, 2], flat[:, 3]
        w0_fit_s = -1.0 + gu_s
        wa_fit_s = -1.5 * gu_s * (om_s + gu_s * (1.0 - om_s))
        out["parameters"] = {
            "Omega_m_tot": summarize(om_s),
            "h": summarize(h_s),
            "100_omega_b": summarize(wb_s),
            "gamma_u": summarize(gu_s),
            "w0_implied": summarize(w0_fit_s),
            "wa_implied": summarize(wa_fit_s),
        }
    elif model_kind == "CPL":
        om_s, h_s, wb_s, w0_s, wa_s = flat[:, 0], flat[:, 1], flat[:, 2], flat[:, 3], flat[:, 4]
        prob_w0_gt_m1 = float(np.mean(w0_s > -1.0))
        prob_w0_lt_m1 = float(np.mean(w0_s < -1.0))
        w0_sum = summarize(w0_s)
        z_w0_gt_m1 = (w0_sum["mean"] - (-1.0)) / max(w0_sum["std"], 1e-12)
        out["parameters"] = {
            "Omega_m_tot": summarize(om_s),
            "h": summarize(h_s),
            "100_omega_b": summarize(wb_s),
            "w0": w0_sum,
            "wa": summarize(wa_s),
        }
        out["T1_Sign_metrics"] = {
            "P_w0_gt_minus1_mcmc": round(prob_w0_gt_m1, 6),
            "P_w0_lt_minus1_mcmc": round(prob_w0_lt_m1, 6),
            "z_gaussian_w0_gt_minus1": round(float(z_w0_gt_m1), 4),
        }
    elif model_kind == "T2B":
        om_s, h_s, w0_s, wa_s = flat[:, 0], flat[:, 1], flat[:, 2], flat[:, 3]
        wb_s = 100.0 * (h_s ** 2) / 19.0
        omega_bc_s = om_s - (OMEGA_NU_MASS_H2 / (h_s ** 2))
        q16, q50, q84 = np.percentile(omega_bc_s, [16.0, 50.0, 84.0])
        om_bc_med = float(q50)
        sig_om_bc = float(0.5 * (q84 - q16))
        f_leak = 1.0 - (19.0 * om_bc_med - 1.0) / 6.0
        r_pred = 19.0 * om_bc_med - 1.0
        sig_r_pred = 19.0 * sig_om_bc
        sig_comb = math.sqrt(sig_r_pred ** 2 + 0.065 ** 2)
        z_r = abs(r_pred - 5.36) / sig_comb
        out["parameters"] = {
            "Omega_m_tot": summarize(om_s),
            "Omega_bc": summarize(omega_bc_s),
            "h": summarize(h_s),
            "100_omega_b_implied": summarize(wb_s),
            "w0": summarize(w0_s),
            "wa": summarize(wa_s),
        }
        out["T2B_metrics"] = {
            "Omega_bc_median": round(om_bc_med, 6),
            "sigma_Omega_bc": round(sig_om_bc, 6),
            "f_leak": round(f_leak, 6),
            "R_pred": round(r_pred, 6),
            "sigma_R_pred": round(sig_r_pred, 6),
            "sigma_comb": round(sig_comb, 6),
            "tension_sigma_vs_Planck": round(z_r, 4),
        }

    return out


def score_t1_l1_per_run(a_r: float, b_r: float) -> tuple[str, list[str]]:
    """
    [Registered Protocol - PREREG.md Sec 5.1 lines 125-128]
    1. Per-Run FAIL (takes precedence): B_r > +9.0 or A_r > -1.0
    2. Per-Run PASS: Not FAIL, and A_r <= -4.0 and B_r <= +4.0
    3. Per-Run INCONCLUSIVE: Every other converged outcome
    """
    reasons = []
    if b_r > 9.0:
        reasons.append(f"B_r = Delta_chi2(Law1 - w0waCDM) = {b_r:+.4f} > +9.0")
    if a_r > -1.0:
        reasons.append(f"A_r = Delta_chi2(Law1 - LCDM) = {a_r:+.4f} > -1.0")
    if len(reasons) > 0:
        return "FAIL", reasons
    if a_r <= -4.0 and b_r <= 4.0:
        return "PASS", []
    return "INCONCLUSIVE", [
        f"Intermediate Delta_chi2: A_r = {a_r:+.4f}, B_r = {b_r:+.4f} (neither FAIL nor PASS)."
    ]


def fast_sensitivity_t1_check(data_dir: str, sn_name: str, cmb_table: str, lya_mode: str) -> dict:
    """
    Fast Nelder-Mead + L-BFGS-B Delta_chi2 sensitivity check for T1-L1 and T1-Sign
    under alternate CMB table ('wcdm') or Ly-alpha correlation/BAO modes ('joint_ap_r0', 'unmodified').
    """
    bao_like = DESIBAOLikelihood(data_dir, lya_mode=lya_mode)
    cmb_like = CMBLikelihood(table=cmb_table, mode="full_3x3")
    sn_like = PantheonPlusLikelihood(data_dir) if sn_name == "Pantheon+" else DESDovekieLikelihood(data_dir)

    res_lcdm = minimize(
        lambda x: joint_chi2_cpl(x[0], x[1], x[2], -1.0, 0.0, bao_like, cmb_like, sn_like),
        np.array([0.302, 0.683, 2.240]),
        method="Nelder-Mead",
        options={"xatol": 1e-6, "fatol": 1e-6, "maxiter": 5000},
    )
    res_law1 = minimize(
        lambda x: joint_chi2_law1(x[0], x[1], max(x[2], 1.8), max(x[3], 0.0), bao_like, cmb_like, sn_like),
        np.array([0.305, 0.678, 2.238, 0.06]),
        method="Nelder-Mead",
        options={"xatol": 1e-6, "fatol": 1e-6, "maxiter": 5000},
    )
    res_cpl = minimize(
        lambda x: joint_chi2_cpl(x[0], x[1], x[2], x[3], x[4], bao_like, cmb_like, sn_like) if (x[3] + x[4] < 0) else 1e30,
        np.array([0.311, 0.676, 2.236, -0.83, -0.65]),
        method="Nelder-Mead",
        options={"xatol": 1e-6, "fatol": 1e-6, "maxiter": 6000},
    )

    c2_lcdm = float(res_lcdm.fun)
    c2_law1 = float(res_law1.fun)
    c2_cpl = float(res_cpl.fun)
    a_r = c2_law1 - c2_lcdm
    b_r = c2_law1 - c2_cpl
    verdict, reasons = score_t1_l1_per_run(a_r, b_r)

    return {
        "sn_dataset": sn_name,
        "cmb_table": cmb_table,
        "lya_mode": lya_mode,
        "chi2_min_LCDM": round(c2_lcdm, 4),
        "chi2_min_Law1": round(c2_law1, 4),
        "chi2_min_w0waCDM": round(c2_cpl, 4),
        "A_r_Law1_minus_LCDM": round(a_r, 4),
        "B_r_Law1_minus_w0waCDM": round(b_r, 4),
        "Law1_gamma_u_best": round(float(max(res_law1.x[3], 0.0)), 5),
        "CPL_w0_best": round(float(res_cpl.x[3]), 4),
        "CPL_wa_best": round(float(res_cpl.x[4]), 4),
        "per_run_verdict": verdict,
        "reasons": reasons,
    }


def evaluate_t2_tests(freeze_t2: dict, t2b_pantheon: dict, t2b_dovekie: dict, cpl_pantheon_chi2: float, cpl_dovekie_chi2: float) -> dict:
    """
    Evaluate T2-A (loading frozen values from FREEZE_T2.json per Rule G3),
    T2-N1, T2-N2, and sensitivity test T2-B.
    """
    r_planck = 5.36
    sig_planck = 0.065

    def eval_t2a_run(run_dict: dict) -> dict:
        fq = run_dict["frozen_quantities"]
        r_pred = fq["R_pred"]
        sig_r = fq["sigma_R_pred"]
        sig_comb = math.sqrt(sig_r ** 2 + sig_planck ** 2)
        diff = r_pred - r_planck
        z_tension = abs(diff) / sig_comb
        verdict = "PASS" if z_tension <= 2.0 else "FAIL"
        return {
            "sn_dataset": run_dict["sn_dataset"],
            "Omega_bc_median": fq["Omega_bc_median"],
            "sigma_Omega_bc": fq["sigma_Omega_bc"],
            "f_leak": fq["f_leak"],
            "sigma_f_leak": fq["sigma_f_leak"],
            "R_pred": r_pred,
            "sigma_R_pred": sig_r,
            "R_Planck": r_planck,
            "sigma_Planck": sig_planck,
            "sigma_comb": round(sig_comb, 6),
            "diff_R_pred_minus_Planck": round(diff, 6),
            "tension_sigma": round(z_tension, 4),
            "per_run_verdict": verdict,
        }

    p_eval = eval_t2a_run(freeze_t2["deciding_PantheonPlus"])
    d_eval = eval_t2a_run(freeze_t2["deciding_DES_Dovekie"])

    # PREREG.md lines 167-169: FAIL if either run > 2*sigma_comb; PASS if both <= 2*sigma_comb
    if p_eval["per_run_verdict"] == "FAIL" or d_eval["per_run_verdict"] == "FAIL":
        t2a_joint = "FAIL"
        t2a_reasons = []
        if p_eval["per_run_verdict"] == "FAIL":
            t2a_reasons.append(f"Pantheon+ |R_pred - R_Planck|/sigma_comb = {p_eval['tension_sigma']:.2f}sigma > 2.0sigma.")
        if d_eval["per_run_verdict"] == "FAIL":
            t2a_reasons.append(f"DES-Dovekie |R_pred - R_Planck|/sigma_comb = {d_eval['tension_sigma']:.2f}sigma > 2.0sigma.")
    else:
        t2a_joint = "PASS"
        t2a_reasons = []

    # Sensitivity runs from FREEZE_T2.json
    sens_evals = {
        k: eval_t2a_run(v) for k, v in freeze_t2["sensitivity_runs"].items()
    }

    # T2-N1: Direct Baryon Share Check (PREREG.md line 173)
    omega_b_model = 1.0 / 19.0
    omega_b_planck = 0.04930
    sig_ob_planck = 0.00086
    z_n1 = (omega_b_model - omega_b_planck) / sig_ob_planck
    t2_n1 = {
        "Omega_b_model": round(omega_b_model, 6),
        "Omega_b_Planck": omega_b_planck,
        "sigma_Omega_b_Planck": sig_ob_planck,
        "diff": round(omega_b_model - omega_b_planck, 6),
        "tension_sigma": round(z_n1, 4),
        "verdict": "PASS" if abs(z_n1) <= 2.0 else "FAIL",
    }

    # T2-N2: Implied Hubble Constant Check (PREREG.md line 175)
    # H_0^pred = 100 * sqrt(19 * omega_b) with Planck omega_b = 0.02237 +/- 0.00015
    wb_planck = 0.02237
    sig_wb_planck = 0.00015
    h0_pred = 100.0 * math.sqrt(19.0 * wb_planck)
    sig_h0_pred = 0.5 * h0_pred * (sig_wb_planck / wb_planck)
    h0_planck = 67.36
    sig_h0_planck = 0.54
    sig_comb_h0 = math.sqrt(sig_h0_pred ** 2 + sig_h0_planck ** 2)
    z_n2 = (h0_pred - h0_planck) / sig_comb_h0

    # Sensitivity comparisons for T2-N2 (PREREG.md line 177)
    h0_pred_desi_bbn = 100.0 * math.sqrt(19.0 * 0.02218)
    sig_h0_desi_bbn = 0.5 * h0_pred_desi_bbn * (0.00055 / 0.02218)
    z_n2_desi_bbn = (h0_pred_desi_bbn - h0_planck) / math.sqrt(sig_h0_desi_bbn ** 2 + sig_h0_planck ** 2)

    h0_pred_cooke = 100.0 * math.sqrt(19.0 * 0.02166)
    sig_h0_cooke = 0.5 * h0_pred_cooke * (0.00019 / 0.02166)
    z_n2_cooke_vs_planck = (h0_pred_cooke - h0_planck) / math.sqrt(sig_h0_cooke ** 2 + sig_h0_planck ** 2)
    z_n2_cooke_vs_desibbn = (h0_pred_cooke - 68.52) / math.sqrt(sig_h0_cooke ** 2 + 0.62 ** 2)

    t2_n2 = {
        "H0_pred_kms_Mpc": round(h0_pred, 4),
        "sigma_H0_pred": round(sig_h0_pred, 4),
        "H0_Planck_kms_Mpc": h0_planck,
        "sigma_H0_Planck": sig_h0_planck,
        "sigma_comb_H0": round(sig_comb_h0, 4),
        "diff_H0": round(h0_pred - h0_planck, 4),
        "tension_sigma": round(z_n2, 4),
        "verdict": "PASS" if abs(z_n2) <= 2.0 else "FAIL",
        "sensitivity": {
            "DESI_LUNA_BBN_vs_Planck": {
                "H0_pred": round(h0_pred_desi_bbn, 4),
                "sigma_H0_pred": round(sig_h0_desi_bbn, 4),
                "tension_sigma": round(z_n2_desi_bbn, 4),
            },
            "Cooke18_BBN_vs_Planck": {
                "H0_pred": round(h0_pred_cooke, 4),
                "sigma_H0_pred": round(sig_h0_cooke, 4),
                "tension_sigma_vs_Planck": round(z_n2_cooke_vs_planck, 4),
                "tension_sigma_vs_DESI_BBN_68p52": round(z_n2_cooke_vs_desibbn, 4),
            },
        },
    }

    # Sensitivity Test T2-B (PREREG.md line 180)
    dc2_t2b_p = t2b_pantheon["chi2_min"] - cpl_pantheon_chi2
    dc2_t2b_d = t2b_dovekie["chi2_min"] - cpl_dovekie_chi2
    t2b_p_pass = (t2b_pantheon["T2B_metrics"]["tension_sigma_vs_Planck"] <= 2.0) and (dc2_t2b_p <= 9.0)
    t2b_d_pass = (t2b_dovekie["T2B_metrics"]["tension_sigma_vs_Planck"] <= 2.0) and (dc2_t2b_d <= 9.0)
    t2b_joint = "PASS" if (t2b_p_pass and t2b_d_pass) else "FAIL"

    return {
        "T2_A_deciding": {
            "joint_verdict": t2a_joint,
            "fail_reasons": t2a_reasons,
            "PantheonPlus": p_eval,
            "DES_Dovekie": d_eval,
        },
        "T2_N1_secondary": t2_n1,
        "T2_N2_secondary": t2_n2,
        "T2_sensitivity": {
            "T2_B_constrained": {
                "joint_verdict": t2b_joint,
                "PantheonPlus": {
                    **t2b_pantheon["T2B_metrics"],
                    "chi2_min": t2b_pantheon["chi2_min"],
                    "Delta_chi2_vs_w0waCDM": round(dc2_t2b_p, 4),
                    "per_run_verdict": "PASS" if t2b_p_pass else "FAIL",
                },
                "DES_Dovekie": {
                    **t2b_dovekie["T2B_metrics"],
                    "chi2_min": t2b_dovekie["chi2_min"],
                    "Delta_chi2_vs_w0waCDM": round(dc2_t2b_d, 4),
                    "per_run_verdict": "PASS" if t2b_d_pass else "FAIL",
                },
            },
            "T2_A_alternate_priors": sens_evals,
        },
    }


def main():
    set_below_normal_priority()
    root = Path(__file__).resolve().parent.parent
    data_dir = str(root / "data")
    results_dir = root / "results"

    # Load frozen values per Rule G3
    freeze_t1 = json.loads((results_dir / "FREEZE_T1.json").read_text(encoding="utf-8"))
    freeze_t2 = json.loads((results_dir / "FREEZE_T2.json").read_text(encoding="utf-8"))
    freeze_t6 = json.loads((results_dir / "FREEZE_T6.json").read_text(encoding="utf-8"))

    print("1. Launching 8 parallel MCMC + polished chi2_min runs for T1-L1, T1-Sign, and T2-B...")
    mcmc_tasks = [
        # Pantheon+ deciding trio (LCDM, LAW1, CPL) with full 3x3 CMB prior
        {"run_id": "T1_LCDM_Pantheon+", "model_kind": "LCDM", "sn_name": "Pantheon+", "data_dir": data_dir, "seed_offset": 201},
        {"run_id": "T1_LAW1_Pantheon+", "model_kind": "LAW1", "sn_name": "Pantheon+", "data_dir": data_dir, "seed_offset": 202},
        {"run_id": "T1_CPL_Pantheon+", "model_kind": "CPL", "sn_name": "Pantheon+", "data_dir": data_dir, "seed_offset": 203},
        # DES-Dovekie deciding trio (LCDM, LAW1, CPL) with full 3x3 CMB prior
        {"run_id": "T1_LCDM_DES-Dovekie", "model_kind": "LCDM", "sn_name": "DES-Dovekie", "data_dir": data_dir, "seed_offset": 204},
        {"run_id": "T1_LAW1_DES-Dovekie", "model_kind": "LAW1", "sn_name": "DES-Dovekie", "data_dir": data_dir, "seed_offset": 205},
        {"run_id": "T1_CPL_DES-Dovekie", "model_kind": "CPL", "sn_name": "DES-Dovekie", "data_dir": data_dir, "seed_offset": 206},
        # T2-B sensitivity constrained fits (with conditional 2x2 CMB + DESI/LUNA BBN prior)
        {
            "run_id": "T2B_Pantheon+",
            "model_kind": "T2B",
            "sn_name": "Pantheon+",
            "cmb_mode": "conditional_2x2",
            "bbn_prior": (2.218, 0.055),
            "data_dir": data_dir,
            "seed_offset": 207,
        },
        {
            "run_id": "T2B_DES-Dovekie",
            "model_kind": "T2B",
            "sn_name": "DES-Dovekie",
            "cmb_mode": "conditional_2x2",
            "bbn_prior": (2.218, 0.055),
            "data_dir": data_dir,
            "seed_offset": 208,
        },
    ]

    with mp.Pool(processes=min(len(mcmc_tasks), N_CORES), initializer=set_below_normal_priority) as pool:
        mcmc_list = pool.map(run_t1_or_t2b_mcmc_worker, mcmc_tasks)

    by_id = {r["run_id"]: r for r in mcmc_list}

    # Evaluate T1-L1 deciding per-run and joint results
    a_pantheon = by_id["T1_LAW1_Pantheon+"]["chi2_min"] - by_id["T1_LCDM_Pantheon+"]["chi2_min"]
    b_pantheon = by_id["T1_LAW1_Pantheon+"]["chi2_min"] - by_id["T1_CPL_Pantheon+"]["chi2_min"]
    v_p, r_p = score_t1_l1_per_run(a_pantheon, b_pantheon)

    a_dovekie = by_id["T1_LAW1_DES-Dovekie"]["chi2_min"] - by_id["T1_LCDM_DES-Dovekie"]["chi2_min"]
    b_dovekie = by_id["T1_LAW1_DES-Dovekie"]["chi2_min"] - by_id["T1_CPL_DES-Dovekie"]["chi2_min"]
    v_d, r_d = score_t1_l1_per_run(a_dovekie, b_dovekie)

    # Discovery p-value p_{T1-L1} (PREREG.md Sec 3.2 line 77)
    p_disc_pantheon = float(chi2.sf(max(0.0, -a_pantheon), df=1)) if a_pantheon < 0.0 else 1.0
    p_disc_dovekie = float(chi2.sf(max(0.0, -a_dovekie), df=1)) if a_dovekie < 0.0 else 1.0
    p_t1_l1_holm = max(p_disc_pantheon, p_disc_dovekie)

    # Joint T1-L1 verdict (PREREG.md lines 130-132: FAIL if either fails; PASS if both pass)
    t1_fail_reasons = []
    t1_inc_reasons = []
    if v_p == "FAIL" or v_d == "FAIL":
        t1_l1_joint = "FAIL"
        if v_p == "FAIL":
            t1_fail_reasons.extend([f"Pantheon+: {msg}" for msg in r_p])
        if v_d == "FAIL":
            t1_fail_reasons.extend([f"DES-Dovekie: {msg}" for msg in r_d])
    elif v_p == "PASS" and v_d == "PASS":
        t1_l1_joint = "PASS"
    else:
        t1_l1_joint = "INCONCLUSIVE"
        if v_p == "INCONCLUSIVE":
            t1_inc_reasons.extend([f"Pantheon+: {msg}" for msg in r_p])
        if v_d == "INCONCLUSIVE":
            t1_inc_reasons.extend([f"DES-Dovekie: {msg}" for msg in r_d])

    # Evaluate T1-Sign secondary test (PREREG.md lines 136-141)
    p_w0_gt_p = by_id["T1_CPL_Pantheon+"]["T1_Sign_metrics"]["P_w0_gt_minus1_mcmc"]
    p_w0_lt_p = by_id["T1_CPL_Pantheon+"]["T1_Sign_metrics"]["P_w0_lt_minus1_mcmc"]
    p_w0_gt_d = by_id["T1_CPL_DES-Dovekie"]["T1_Sign_metrics"]["P_w0_gt_minus1_mcmc"]
    p_w0_lt_d = by_id["T1_CPL_DES-Dovekie"]["T1_Sign_metrics"]["P_w0_lt_minus1_mcmc"]

    if p_w0_lt_p >= 0.95 or p_w0_lt_d >= 0.95:
        t1_sign_joint = "FAIL"
    elif p_w0_gt_p >= 0.95 and p_w0_gt_d >= 0.95:
        t1_sign_joint = "PASS"
    else:
        t1_sign_joint = "INCONCLUSIVE"

    print("2. Running T1 sensitivity checks (wCDM CMB table, r_Lya=0, unmodified BAO)...")
    t1_sens = {
        "Pantheon+_wCDM_CMB": fast_sensitivity_t1_check(data_dir, "Pantheon+", "wcdm", "joint_ap_deciding"),
        "DES-Dovekie_wCDM_CMB": fast_sensitivity_t1_check(data_dir, "DES-Dovekie", "wcdm", "joint_ap_deciding"),
        "Pantheon+_Lya_r0": fast_sensitivity_t1_check(data_dir, "Pantheon+", "lcdm", "joint_ap_r0"),
        "DES-Dovekie_Lya_r0": fast_sensitivity_t1_check(data_dir, "DES-Dovekie", "lcdm", "joint_ap_r0"),
        "Pantheon+_unmodified_BAO": fast_sensitivity_t1_check(data_dir, "Pantheon+", "lcdm", "unmodified"),
        "DES-Dovekie_unmodified_BAO": fast_sensitivity_t1_check(data_dir, "DES-Dovekie", "lcdm", "unmodified"),
    }

    t1_results = {
        "T1_L1_deciding": {
            "joint_verdict_raw": t1_l1_joint,
            "p_T1_L1_holm": round(p_t1_l1_holm, 8),
            "fail_reasons": t1_fail_reasons,
            "inconclusive_reasons": t1_inc_reasons,
            "PantheonPlus": {
                "chi2_min_LCDM": by_id["T1_LCDM_Pantheon+"]["chi2_min"],
                "chi2_min_Law1": by_id["T1_LAW1_Pantheon+"]["chi2_min"],
                "chi2_min_w0waCDM": by_id["T1_CPL_Pantheon+"]["chi2_min"],
                "A_r_Law1_minus_LCDM": round(a_pantheon, 4),
                "B_r_Law1_minus_w0waCDM": round(b_pantheon, 4),
                "p_discovery_vs_LCDM": round(p_disc_pantheon, 8),
                "per_run_verdict": v_p,
                "reasons": r_p,
                "Law1_chain": by_id["T1_LAW1_Pantheon+"],
                "LCDM_chain": by_id["T1_LCDM_Pantheon+"],
            },
            "DES_Dovekie": {
                "chi2_min_LCDM": by_id["T1_LCDM_DES-Dovekie"]["chi2_min"],
                "chi2_min_Law1": by_id["T1_LAW1_DES-Dovekie"]["chi2_min"],
                "chi2_min_w0waCDM": by_id["T1_CPL_DES-Dovekie"]["chi2_min"],
                "A_r_Law1_minus_LCDM": round(a_dovekie, 4),
                "B_r_Law1_minus_w0waCDM": round(b_dovekie, 4),
                "p_discovery_vs_LCDM": round(p_disc_dovekie, 8),
                "per_run_verdict": v_d,
                "reasons": r_d,
                "Law1_chain": by_id["T1_LAW1_DES-Dovekie"],
                "LCDM_chain": by_id["T1_LCDM_DES-Dovekie"],
            },
        },
        "T1_Sign_secondary": {
            "joint_verdict": t1_sign_joint,
            "PantheonPlus": {
                "CPL_chain": by_id["T1_CPL_Pantheon+"],
                "Delta_chi2_w0wa_minus_LCDM": round(
                    by_id["T1_CPL_Pantheon+"]["chi2_min"] - by_id["T1_LCDM_Pantheon+"]["chi2_min"], 4
                ),
            },
            "DES_Dovekie": {
                "CPL_chain": by_id["T1_CPL_DES-Dovekie"],
                "Delta_chi2_w0wa_minus_LCDM": round(
                    by_id["T1_CPL_DES-Dovekie"]["chi2_min"] - by_id["T1_LCDM_DES-Dovekie"]["chi2_min"], 4
                ),
            },
        },
        "T1_sensitivity": t1_sens,
    }

    print("3. Evaluating T2-A, T2-N1, T2-N2, and T2-B...")
    t2_results = evaluate_t2_tests(
        freeze_t2,
        by_id["T2B_Pantheon+"],
        by_id["T2B_DES-Dovekie"],
        freeze_t2["deciding_PantheonPlus"]["chi2_min"],
        freeze_t2["deciding_DES_Dovekie"]["chi2_min"],
    )

    print("4. Evaluating T6 on Pantheon+ Hubble-flow supernovae and Coincidence Window...")
    pantheon_full = load_pantheon_plus_full(root / "data" / "pantheon_plus")
    mb_fixed = freeze_t6["calibrator_fit"]["M_B_fixed"]
    sig_mb_fixed = freeze_t6["calibrator_fit"]["sigma_M_B_fixed"]

    t6_deciding = evaluate_t6_hubble_flow(
        pantheon_full, mb_fixed, sig_mb_fixed, coord_frame="galactic", z_col="zHD", apply_merge=True
    )
    t6_sens_eq = evaluate_t6_hubble_flow(
        pantheon_full, mb_fixed, sig_mb_fixed, coord_frame="equatorial", z_col="zHD", apply_merge=True
    )
    t6_sens_zcmb = evaluate_t6_hubble_flow(
        pantheon_full, mb_fixed, sig_mb_fixed, coord_frame="galactic", z_col="zCMB", apply_merge=True
    )
    t6_sens_nomerge = evaluate_t6_hubble_flow(
        pantheon_full, mb_fixed, sig_mb_fixed, coord_frame="galactic", z_col="zHD", apply_merge=False
    )

    t6_results = {
        "calibrator_freeze_used": freeze_t6["calibrator_fit"],
        "T6_deciding": t6_deciding,
        "T6_sensitivity": {
            "equatorial_RING": t6_sens_eq,
            "galactic_zCMB": t6_sens_zcmb,
            "galactic_drop_sparse_no_merge": t6_sens_nomerge,
        },
    }

    f_leak_frozen = freeze_t2["single_frozen_f_leak_for_T5"]["f_leak"]
    coincidence_window = compute_coincidence_window(f_leak_frozen)

    part9_out = {
        "completed_at": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "T1": t1_results,
        "T2": t2_results,
        "T6": t6_results,
        "coincidence_window_sec6": coincidence_window,
    }
    out_path = results_dir / "part9_cosmology_results.json"
    out_path.write_text(json.dumps(part9_out, indent=2), encoding="utf-8")
    print("PART 9 COSMOLOGY TESTS COMPLETED.")
    print(f"  T1-L1 verdict: {t1_l1_joint} (A_P+={a_pantheon:+.2f}, B_P+={b_pantheon:+.2f}; A_Dov={a_dovekie:+.2f}, B_Dov={b_dovekie:+.2f})")
    print(f"  T1-Sign verdict: {t1_sign_joint}")
    print(f"  T2-A verdict: {t2_results['T2_A_deciding']['joint_verdict']}")
    print(f"  T2-N1 verdict: {t2_results['T2_N1_secondary']['verdict']} ({t2_results['T2_N1_secondary']['tension_sigma']:+.2f}sigma)")
    print(f"  T2-N2 verdict: {t2_results['T2_N2_secondary']['verdict']} ({t2_results['T2_N2_secondary']['tension_sigma']:+.2f}sigma)")
    print(f"  T6 verdict: {t6_deciding['verdict']} (p_het={t6_deciding['p_het']:.4f}, N_pix={t6_deciding['N_pix']})")


if __name__ == "__main__":
    main()
