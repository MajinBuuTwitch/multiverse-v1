import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import json
import math
import sys
import time
from pathlib import Path
import numpy as np
import psutil
import emcee
from scipy import linalg, optimize
from scipy.stats import chi2

PHASE3_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(PHASE3_DIR, ".."))
if os.path.join(ROOT_DIR, "scripts") not in sys.path:
    sys.path.insert(0, os.path.join(ROOT_DIR, "scripts"))
if os.path.join(ROOT_DIR, "head_to_head") not in sys.path:
    sys.path.insert(0, os.path.join(ROOT_DIR, "head_to_head"))

# Read-only imports of frozen Stage 2 and Head-to-Head modules
import cosmology as cosmo
from run_part8_fixes import set_below_normal_priority, compute_split_rhat_and_ess
from run_part9_cosmology_tests import polish_chi2_min, score_t1_l1_per_run
import sparc_t5
import local_h0_t6
import h2h_cosmology as h2h

BASE_SEED = 20261030


class MockDESIBAOLikelihood(cosmo.DESIBAOLikelihood):
    """
    Thin wrapper around frozen cosmo.DESIBAOLikelihood that reads the universe's own
    joint Lya BAO+AP measurement from <u_dir>/desi_bao_dr2/lya_bao_ap_joint.json
    in place of the real-universe hard-coded arXiv:2607.27410 values [Established].
    """

    def __init__(self, u_dir: str | Path, lya_mode: str = "joint_ap_deciding"):
        u_dir_str = str(u_dir)
        super().__init__(u_dir_str, lya_mode="unmodified")
        self.lya_mode = lya_mode

        if lya_mode in ("joint_ap_deciding", "joint_ap_r0"):
            lya_path = os.path.join(u_dir_str, "desi_bao_dr2", "lya_bao_ap_joint.json")
            with open(lya_path, "r", encoding="utf-8") as f:
                lya_data = json.load(f)

            z_target = float(lya_data.get("z_eff", 2.33))
            idx_dm = [i for i, (zv, q) in enumerate(zip(self.z, self.qty)) if abs(zv - z_target) < 0.05 and "DM" in q]
            idx_dh = [i for i, (zv, q) in enumerate(zip(self.z, self.qty)) if abs(zv - z_target) < 0.05 and "DH" in q]
            assert len(idx_dm) == 1 and len(idx_dh) == 1, "Could not locate unique z=2.33 Lya DM and DH rows"
            idm, idh = idx_dm[0], idx_dh[0]

            self.mean[idm] = float(lya_data["DM_over_rd"])
            self.mean[idh] = float(lya_data["DH_over_rd"])
            sig_dm = float(lya_data["sigma_DM_over_rd"])
            sig_dh = float(lya_data["sigma_DH_over_rd"])
            r_corr = float(lya_data["corr_DH_DM"]) if lya_mode == "joint_ap_deciding" else 0.0

            self.cov[idm, :] = 0.0
            self.cov[:, idm] = 0.0
            self.cov[idh, :] = 0.0
            self.cov[:, idh] = 0.0
            self.cov[idm, idm] = sig_dm ** 2
            self.cov[idh, idh] = sig_dh ** 2
            self.cov[idm, idh] = r_corr * sig_dm * sig_dh
            self.cov[idh, idm] = r_corr * sig_dm * sig_dh
            self.inv_cov = linalg.inv(self.cov)


class MockCMBLikelihood(cosmo.CMBLikelihood):
    """
    Thin wrapper around frozen cosmo.CMBLikelihood that reads the universe's own
    compressed CMB distance prior from <u_dir>/cmb_distance_prior/distance_prior.json
    in place of the real-universe hard-coded Chen, Huang & Wang (2019) Table 1 vector [Established].
    """

    def __init__(self, u_dir: str | Path, mode: str = "full_3x3"):
        cmb_path = os.path.join(str(u_dir), "cmb_distance_prior", "distance_prior.json")
        with open(cmb_path, "r", encoding="utf-8") as f:
            d = json.load(f)

        self.mu = np.array(d["mean"], dtype=float)
        self.sig = np.array(d["sigma"], dtype=float)
        self.corr = np.array(d["correlation"], dtype=float)
        self.cov3 = np.outer(self.sig, self.sig) * self.corr
        self.inv_cov3 = linalg.inv(self.cov3)
        self.mode = mode

        self.c11 = self.cov3[:2, :2]
        self.c12 = self.cov3[:2, 2]
        self.c22 = self.cov3[2, 2]
        self.cond_cov2 = self.c11 - np.outer(self.c12, self.c12) / self.c22
        self.inv_cond_cov2 = linalg.inv(self.cond_cov2)
        self.inv_marg_cov2 = linalg.inv(self.c11)


class MockPantheonPlusLikelihood(cosmo.PantheonPlusLikelihood):
    """
    Thin wrapper around frozen cosmo.PantheonPlusLikelihood that reads from
    <u_dir>/pantheonplus/ (without underscore) instead of <u_dir>/pantheon_plus/ [Established].
    """

    def __init__(self, u_dir: str | Path):
        u_dir_str = str(u_dir)
        dat_path = os.path.join(u_dir_str, "pantheonplus", "Pantheon+SH0ES.dat")
        cov_path = os.path.join(u_dir_str, "pantheonplus", "Pantheon+SH0ES_STAT+SYS.cov")

        with open(dat_path, "r", encoding="utf-8") as f:
            header = f.readline().strip().split()
            rows = [line.strip().split() for line in f if line.strip()]

        col_zhd = header.index("zHD")
        col_zhel = header.index("zHEL")
        col_mb = header.index("m_b_corr")
        col_calib = header.index("IS_CALIBRATOR")

        zhd_all = np.array([float(r[col_zhd]) for r in rows], dtype=float)
        zhel_all = np.array([float(r[col_zhel]) for r in rows], dtype=float)
        mb_all = np.array([float(r[col_mb]) for r in rows], dtype=float)
        calib_all = np.array([int(r[col_calib]) for r in rows], dtype=int)

        mask = (zhd_all > 0.01) & (calib_all == 0)
        self.mask = mask
        self.z_hd = zhd_all[mask]
        self.z_hel = zhel_all[mask]
        self.m_obs = mb_all[mask]
        self.n_sn = int(np.sum(mask))

        raw = np.loadtxt(cov_path, dtype=float)
        n_tot = int(round(raw[0]))
        cov_full = raw[1:].reshape((n_tot, n_tot))
        cov_sub = cov_full[np.ix_(mask, mask)]

        self.inv_cov = linalg.inv(cov_sub, check_finite=False)
        ones = np.ones(self.n_sn, dtype=float)
        self.cinv_ones = self.inv_cov @ ones
        self.ones_cinv_ones = float(np.dot(ones, self.cinv_ones))
        self.z_max = float(np.max(self.z_hd))
        self.z_grid = np.linspace(0.0, self.z_max * 1.01, 351)


def joint_chi2_cpl_dispatch(
    Omega_m_tot: float,
    h: float,
    wb100: float,
    w0: float,
    wa: float,
    reading: str,
    bao_like: MockDESIBAOLikelihood,
    cmb_like: MockCMBLikelihood,
    sn_like: MockPantheonPlusLikelihood | cosmo.DESDovekieLikelihood,
    bbn_prior: tuple[float, float] | None = None,
) -> float:
    """
    Dispatch CPL / LCDM joint chi2 to Reading B (frozen cosmo.joint_chi2_cpl)
    or Reading A (frozen h2h.joint_chi2_cpl_reading + optional BBN prior) [Established].
    """
    if reading == "B":
        return cosmo.joint_chi2_cpl(Omega_m_tot, h, wb100, w0, wa, bao_like, cmb_like, sn_like, bbn_prior=bbn_prior)
    elif reading == "A":
        h2 = h * h
        Omega_bc = Omega_m_tot - (cosmo.OMEGA_NU_MASS_H2 / h2)
        c2 = h2h.joint_chi2_cpl_reading(Omega_bc, h, wb100, w0, wa, "A", bao_like, cmb_like, sn_like)
        if bbn_prior is not None and np.isfinite(c2):
            mu_bbn, sig_bbn = bbn_prior
            c2 += ((wb100 - mu_bbn) / sig_bbn) ** 2
        return float(c2)
    else:
        raise ValueError(f"Unknown reading: {reading}")


def joint_chi2_law1_dispatch(
    Omega_m_tot: float,
    h: float,
    wb100: float,
    gamma_u: float,
    reading: str,
    bao_like: MockDESIBAOLikelihood,
    cmb_like: MockCMBLikelihood,
    sn_like: MockPantheonPlusLikelihood | cosmo.DESDovekieLikelihood,
    bbn_prior: tuple[float, float] | None = None,
) -> float:
    """
    Dispatch Law 1 joint chi2 to Reading B (frozen cosmo.joint_chi2_law1)
    or Reading A (frozen h2h.joint_chi2_law1_reading + optional BBN prior) [Model Ansatz].
    """
    if reading == "B":
        return cosmo.joint_chi2_law1(Omega_m_tot, h, wb100, gamma_u, bao_like, cmb_like, sn_like, bbn_prior=bbn_prior)
    elif reading == "A":
        h2 = h * h
        Omega_bc = Omega_m_tot - (cosmo.OMEGA_NU_MASS_H2 / h2)
        c2 = h2h.joint_chi2_law1_reading(Omega_bc, h, wb100, gamma_u, "A", bao_like, cmb_like, sn_like)
        if bbn_prior is not None and np.isfinite(c2):
            mu_bbn, sig_bbn = bbn_prior
            c2 += ((wb100 - mu_bbn) / sig_bbn) ** 2
        return float(c2)
    else:
        raise ValueError(f"Unknown reading: {reading}")


def summarize_samples(arr: np.ndarray) -> dict:
    """Compute mean +- 1sigma (std ddof=1), median +- sigma_68, and 95% interval [p2.5, p97.5]."""
    p2p5, p16, p50, p84, p97p5 = np.percentile(arr, [2.5, 16.0, 50.0, 84.0, 97.5])
    return {
        "mean": round(float(np.mean(arr)), 6),
        "std": round(float(np.std(arr, ddof=1)), 6),
        "median": round(float(p50), 6),
        "sigma_68": round(float(0.5 * (p84 - p16)), 6),
        "ci95": [round(float(p2p5), 6), round(float(p97p5), 6)],
    }


def run_single_cosmo_mcmc_task(task: dict) -> dict:
    """
    Worker function running one registered Stage 2 MCMC + polished chi2_min chain
    for a COSMO mock universe under Reading B or Reading A.
    """
    set_below_normal_priority()
    t0 = time.perf_counter()

    u_dir = task["u_dir"]
    universe_id = task["universe_id"]
    run_id = task["run_id"]
    model_kind = task["model_kind"]  # 'LAW1', 'LCDM', 'CPL', or 'T2A_CPL'
    sn_name = task["sn_name"]        # 'Pantheon+' or 'DES-Dovekie'
    reading = task["reading"]        # 'B' or 'A'
    cmb_mode = task["cmb_mode"]      # 'full_3x3' or 'conditional_2x2'
    bbn_prior = tuple(task["bbn_prior"]) if task.get("bbn_prior") is not None else None
    seed = int(task["seed"])

    bao_like = MockDESIBAOLikelihood(u_dir, lya_mode="joint_ap_deciding")
    cmb_like = MockCMBLikelihood(u_dir, mode=cmb_mode)
    sn_like = MockPantheonPlusLikelihood(u_dir) if sn_name == "Pantheon+" else cosmo.DESDovekieLikelihood(u_dir)

    wb_init = bbn_prior[0] if bbn_prior is not None else float(cmb_like.mu[2])
    wb_init = float(np.clip(wb_init, 1.85, 2.55))

    if model_kind == "LCDM":
        n_dim = 3
        bounds = [(0.1, 0.6), (0.5, 0.9), (1.8, 2.6)]
        x0 = np.array([0.302, 0.683, wb_init], dtype=float)
        scales = np.array([0.002, 0.002, 0.008], dtype=float)

        def neg2logp(theta):
            om, h, wb100 = theta
            if not (0.1 <= om <= 0.6 and 0.5 <= h <= 0.9 and 1.8 <= wb100 <= 2.6):
                return 1e30
            c2 = joint_chi2_cpl_dispatch(om, h, wb100, -1.0, 0.0, reading, bao_like, cmb_like, sn_like, bbn_prior=bbn_prior)
            return c2 if np.isfinite(c2) else 1e30

    elif model_kind == "LAW1":
        n_dim = 4
        bounds = [(0.1, 0.6), (0.5, 0.9), (1.8, 2.6), (0.0, 2.0)]
        x0 = np.array([0.305, 0.678, wb_init, 0.06], dtype=float)
        scales = np.array([0.002, 0.002, 0.008, 0.015], dtype=float)

        def neg2logp(theta):
            om, h, wb100, gamma_u = theta
            if not (0.1 <= om <= 0.6 and 0.5 <= h <= 0.9 and 1.8 <= wb100 <= 2.6 and 0.0 <= gamma_u <= 2.0):
                return 1e30
            c2 = joint_chi2_law1_dispatch(om, h, wb100, gamma_u, reading, bao_like, cmb_like, sn_like, bbn_prior=bbn_prior)
            return c2 if np.isfinite(c2) else 1e30

    elif model_kind in ("CPL", "T2A_CPL"):
        n_dim = 5
        bounds = [(0.1, 0.6), (0.5, 0.9), (1.8, 2.6), (-3.0, 1.0), (-3.0, 2.0)]
        x0 = np.array([0.311, 0.675, wb_init, -0.83, -0.65], dtype=float)
        scales = np.array([0.003, 0.003, 0.01 if model_kind == "T2A_CPL" else 0.008, 0.02, 0.08], dtype=float)

        def neg2logp(theta):
            om, h, wb100, w0, wa = theta
            if not (0.1 <= om <= 0.6 and 0.5 <= h <= 0.9 and 1.8 <= wb100 <= 2.6):
                return 1e30
            if not (-3.0 <= w0 <= 1.0 and -3.0 <= wa <= 2.0 and (w0 + wa) < 0.0):
                return 1e30
            c2 = joint_chi2_cpl_dispatch(om, h, wb100, w0, wa, reading, bao_like, cmb_like, sn_like, bbn_prior=bbn_prior)
            return c2 if np.isfinite(c2) else 1e30
    else:
        raise ValueError(f"Unknown model_kind: {model_kind}")

    def log_prob(theta):
        val = neg2logp(theta)
        if val >= 1e29:
            return -np.inf
        return -0.5 * val

    res_init = optimize.minimize(
        neg2logp,
        x0,
        method="Nelder-Mead",
        options={"xatol": 1e-5, "fatol": 1e-5, "maxiter": 4000},
    )
    center = res_init.x.copy()
    chi2_init = float(res_init.fun)

    rng = np.random.default_rng(seed)
    n_walkers = 32
    pos = center[None, :] + rng.normal(0.0, 1.0, size=(n_walkers, n_dim)) * scales[None, :]
    for i in range(n_walkers):
        for d in range(n_dim):
            low, high = bounds[d]
            pos[i, d] = np.clip(pos[i, d], low + 1e-4, high - 1e-4)
        if model_kind in ("CPL", "T2A_CPL") and (pos[i, 3] + pos[i, 4] >= -0.01):
            pos[i, 4] = -0.05 - pos[i, 3]

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

    if model_kind == "T2A_CPL":
        best_idx = int(np.argmax(logp_flat))
        chi2_min = min(chi2_init, float(-2.0 * logp_flat[best_idx]))
        best_x = flat[best_idx].copy()
    else:
        top5_idx = np.argsort(logp_flat)[-5:][::-1]
        top5_samples = [flat[idx] for idx in top5_idx]
        chi2_min, best_x = polish_chi2_min(neg2logp, top5_samples, bounds)

    om_s = flat[:, 0]
    h_s = flat[:, 1]
    wb_s = flat[:, 2]
    omega_bc_s = om_s - (cosmo.OMEGA_NU_MASS_H2 / (h_s ** 2))

    params_out = {
        "Omega_bc": summarize_samples(omega_bc_s),
        "Omega_m_tot": summarize_samples(om_s),
        "h": summarize_samples(h_s),
        "100_omega_b": summarize_samples(wb_s),
    }

    extra_out = {}
    if model_kind == "LAW1":
        gu_s = flat[:, 3]
        w0_imp = -1.0 + gu_s
        wa_imp = -1.5 * gu_s * (om_s + gu_s * (1.0 - om_s))
        params_out["gamma_u"] = summarize_samples(gu_s)
        params_out["w0_implied"] = summarize_samples(w0_imp)
        params_out["wa_implied"] = summarize_samples(wa_imp)

        # Law 1 implied T1-Sign and T2-A statistics
        gu_mean = float(np.mean(gu_s))
        gu_std = float(np.std(gu_s, ddof=1))
        z_gu_gt_0 = gu_mean / max(gu_std, 1e-12)
        p16, p50, p84 = np.percentile(omega_bc_s, [16.0, 50.0, 84.0])
        om_bc_med = float(p50)
        sig_om_bc = float(0.5 * (p84 - p16))
        r_pred_med = 19.0 * om_bc_med - 1.0
        sig_r_pred_68 = 19.0 * sig_om_bc
        f_leak_med = 1.0 - r_pred_med / 6.0
        om_bc_mean = float(np.mean(omega_bc_s))
        om_bc_std = float(np.std(omega_bc_s, ddof=1))
        r_pred_mean = 19.0 * om_bc_mean - 1.0
        sig_r_pred_std = 19.0 * om_bc_std
        extra_out["Law1_derived_metrics"] = {
            "Omega_bc_median": round(om_bc_med, 6),
            "sigma_Omega_bc_68": round(sig_om_bc, 6),
            "f_leak_median": round(f_leak_med, 6),
            "R_pred_median": round(r_pred_med, 6),
            "sigma_R_pred_68": round(sig_r_pred_68, 6),
            "R_pred_mean": round(r_pred_mean, 6),
            "sigma_R_pred_std": round(sig_r_pred_std, 6),
            "z_gaussian_gamma_u_gt_0": round(z_gu_gt_0, 4),
            "P_gamma_u_gt_0_mcmc": round(float(np.mean(gu_s > 0.0)), 6),
        }

    elif model_kind in ("CPL", "T2A_CPL"):
        w0_s = flat[:, 3]
        wa_s = flat[:, 4]
        params_out["w0"] = summarize_samples(w0_s)
        params_out["wa"] = summarize_samples(wa_s)

        prob_w0_gt_m1 = float(np.mean(w0_s > -1.0))
        prob_w0_lt_m1 = float(np.mean(w0_s < -1.0))
        w0_mean = float(np.mean(w0_s))
        w0_std = float(np.std(w0_s, ddof=1))
        z_w0_gt_m1 = (w0_mean - (-1.0)) / max(w0_std, 1e-12)
        extra_out["T1_Sign_metrics"] = {
            "P_w0_gt_minus1_mcmc": round(prob_w0_gt_m1, 6),
            "P_w0_lt_minus1_mcmc": round(prob_w0_lt_m1, 6),
            "z_gaussian_w0_gt_minus1": round(z_w0_gt_m1, 4),
        }

        p16, p50, p84 = np.percentile(omega_bc_s, [16.0, 50.0, 84.0])
        om_bc_med = float(p50)
        sig_om_bc = float(0.5 * (p84 - p16))
        f_leak = 1.0 - (19.0 * om_bc_med - 1.0) / 6.0
        sig_f_leak = (19.0 / 6.0) * sig_om_bc
        r_pred = 19.0 * om_bc_med - 1.0
        sig_r_pred = 19.0 * sig_om_bc
        extra_out["frozen_quantities"] = {
            "Omega_bc_median": round(om_bc_med, 6),
            "sigma_Omega_bc": round(sig_om_bc, 6),
            "f_leak": round(f_leak, 6),
            "sigma_f_leak": round(sig_f_leak, 6),
            "R_pred": round(r_pred, 6),
            "sigma_R_pred": round(sig_r_pred, 6),
        }

    elapsed_s = time.perf_counter() - t0
    return {
        "universe_id": universe_id,
        "run_id": run_id,
        "model_kind": model_kind,
        "sn_dataset": sn_name,
        "reading": reading,
        "cmb_mode": cmb_mode,
        "bbn_prior_100wb": {"mean": bbn_prior[0], "sigma": bbn_prior[1]} if bbn_prior is not None else None,
        "seed": seed,
        "n_walkers": n_walkers,
        "n_burn": n_burn,
        "n_prod": int(chain.shape[0]),
        "n_samples_total": int(flat.shape[0]),
        "chi2_min": round(float(chi2_min), 6),
        "best_fit_vector": [round(float(v), 6) for v in best_x],
        "convergence": diag,
        "converged": bool(diag["max_rhat_minus_1"] < 0.01 and diag["min_ess"] > 1000.0),
        "elapsed_sec": round(elapsed_s, 3),
        "parameters": params_out,
        **extra_out,
    }


def assemble_cosmo_universe_result(
    universe_id: str,
    round_num: int,
    u_dir: str | Path,
    chain_results: list[dict],
    wall_elapsed_sec: float,
) -> dict:
    """
    Assemble all Reading B and Reading A model fits, statistics, and registered verdicts
    for a single COSMO universe using its REFERENCES.json.
    """
    ref_path = os.path.join(str(u_dir), "REFERENCES.json")
    with open(ref_path, "r", encoding="utf-8") as f:
        refs = json.load(f)

    r_ref = float(refs["R_omegac_over_omegab"]["value"])
    sig_r_ref = float(refs["R_omegac_over_omegab"]["sigma"])
    ob_ref = float(refs["Omega_b"]["value"])
    sig_ob_ref = float(refs["Omega_b"]["sigma"])
    wb100_ref = float(refs["100omega_b"]["value"])
    sig_wb100_ref = float(refs["100omega_b"]["sigma"])
    h0_ref = float(refs["H0"]["value"])
    sig_h0_ref = float(refs["H0"]["sigma"])
    bbn_mu = float(refs["BBN_100omega_b_prior"]["value"])
    bbn_sig = float(refs["BBN_100omega_b_prior"]["sigma"])

    by_id = {c["run_id"]: c for c in chain_results}

    def build_reading_summary(reading: str) -> dict:
        # 1. T1-L1 per SN compilation and joint
        law1_p = by_id[f"{universe_id}__R{reading}__LAW1__Pantheon+"]
        lcdm_p = by_id[f"{universe_id}__R{reading}__LCDM__Pantheon+"]
        cpl_p = by_id[f"{universe_id}__R{reading}__CPL__Pantheon+"]

        law1_d = by_id[f"{universe_id}__R{reading}__LAW1__DES-Dovekie"]
        lcdm_d = by_id[f"{universe_id}__R{reading}__LCDM__DES-Dovekie"]
        cpl_d = by_id[f"{universe_id}__R{reading}__CPL__DES-Dovekie"]

        t2a_p = by_id[f"{universe_id}__R{reading}__T2A_CPL__Pantheon+"]
        t2a_d = by_id[f"{universe_id}__R{reading}__T2A_CPL__DES-Dovekie"]

        a_p = law1_p["chi2_min"] - lcdm_p["chi2_min"]
        b_p = law1_p["chi2_min"] - cpl_p["chi2_min"]
        vp_t1, rp_t1 = score_t1_l1_per_run(a_p, b_p)
        p_disc_p = float(chi2.sf(max(0.0, -a_p), df=1)) if a_p < 0.0 else 1.0

        a_d = law1_d["chi2_min"] - lcdm_d["chi2_min"]
        b_d = law1_d["chi2_min"] - cpl_d["chi2_min"]
        vd_t1, rd_t1 = score_t1_l1_per_run(a_d, b_d)
        p_disc_d = float(chi2.sf(max(0.0, -a_d), df=1)) if a_d < 0.0 else 1.0
        p_t1_holm = max(p_disc_p, p_disc_d)

        if vp_t1 == "FAIL" or vd_t1 == "FAIL":
            t1_l1_joint = "FAIL"
        elif vp_t1 == "PASS" and vd_t1 == "PASS":
            t1_l1_joint = "PASS"
        else:
            t1_l1_joint = "INCONCLUSIVE"

        # 2. T1-Sign per SN compilation and joint (from CPL chain, plus Law 1 metrics)
        pw0_gt_p = cpl_p["T1_Sign_metrics"]["P_w0_gt_minus1_mcmc"]
        pw0_lt_p = cpl_p["T1_Sign_metrics"]["P_w0_lt_minus1_mcmc"]
        vp_sign = "FAIL" if pw0_lt_p >= 0.95 else ("PASS" if pw0_gt_p >= 0.95 else "INCONCLUSIVE")

        pw0_gt_d = cpl_d["T1_Sign_metrics"]["P_w0_gt_minus1_mcmc"]
        pw0_lt_d = cpl_d["T1_Sign_metrics"]["P_w0_lt_minus1_mcmc"]
        vd_sign = "FAIL" if pw0_lt_d >= 0.95 else ("PASS" if pw0_gt_d >= 0.95 else "INCONCLUSIVE")

        if pw0_lt_p >= 0.95 or pw0_lt_d >= 0.95:
            t1_sign_joint = "FAIL"
        elif pw0_gt_p >= 0.95 and pw0_gt_d >= 0.95:
            t1_sign_joint = "PASS"
        else:
            t1_sign_joint = "INCONCLUSIVE"

        # 3. T2-A per SN compilation and joint (registered T2A_CPL chain + Law 1 chain comparison)
        def eval_t2a(t2a_chain: dict, law1_chain: dict) -> dict:
            fq = t2a_chain["frozen_quantities"]
            r_pred = fq["R_pred"]
            sig_r = fq["sigma_R_pred"]
            sig_comb = math.sqrt(sig_r ** 2 + sig_r_ref ** 2)
            diff = r_pred - r_ref
            z_signed = diff / sig_comb
            z_abs = abs(z_signed)
            verdict = "PASS" if z_abs <= 2.0 else "FAIL"

            # Law 1 chain Omega_bc derived R_pred
            l1m = law1_chain["Law1_derived_metrics"]
            r_l1 = l1m["R_pred_median"]
            sig_r_l1 = l1m["sigma_R_pred_68"]
            sig_comb_l1 = math.sqrt(sig_r_l1 ** 2 + sig_r_ref ** 2)
            diff_l1 = r_l1 - r_ref
            z_signed_l1 = diff_l1 / sig_comb_l1
            z_abs_l1 = abs(z_signed_l1)
            verdict_l1 = "PASS" if z_abs_l1 <= 2.0 else "FAIL"

            return {
                "sn_dataset": t2a_chain["sn_dataset"],
                "Omega_bc_median": fq["Omega_bc_median"],
                "sigma_Omega_bc": fq["sigma_Omega_bc"],
                "Omega_bc_summary": t2a_chain["parameters"]["Omega_bc"],
                "f_leak": fq["f_leak"],
                "sigma_f_leak": fq["sigma_f_leak"],
                "R_pred": r_pred,
                "sigma_R_pred": sig_r,
                "R_ref": r_ref,
                "sigma_R_ref": sig_r_ref,
                "sigma_comb": round(sig_comb, 6),
                "diff_R_pred_minus_ref": round(diff, 6),
                "signed_tension_sigma": round(z_signed, 4),
                "tension_sigma": round(z_abs, 4),
                "per_run_verdict": verdict,
                "from_Law1_chain": {
                    "Omega_bc_median": l1m["Omega_bc_median"],
                    "sigma_Omega_bc": l1m["sigma_Omega_bc_68"],
                    "f_leak": l1m["f_leak_median"],
                    "R_pred": r_l1,
                    "sigma_R_pred": sig_r_l1,
                    "sigma_comb": round(sig_comb_l1, 6),
                    "diff_R_pred_minus_ref": round(diff_l1, 6),
                    "signed_tension_sigma": round(z_signed_l1, 4),
                    "tension_sigma": round(z_abs_l1, 4),
                    "per_run_verdict": verdict_l1,
                },
            }

        t2a_eval_p = eval_t2a(t2a_p, law1_p)
        t2a_eval_d = eval_t2a(t2a_d, law1_d)
        t2a_joint = (
            "FAIL"
            if (t2a_eval_p["per_run_verdict"] == "FAIL" or t2a_eval_d["per_run_verdict"] == "FAIL")
            else "PASS"
        )
        t2a_joint_law1 = (
            "FAIL"
            if (
                t2a_eval_p["from_Law1_chain"]["per_run_verdict"] == "FAIL"
                or t2a_eval_d["from_Law1_chain"]["per_run_verdict"] == "FAIL"
            )
            else "PASS"
        )

        return {
            "reading": reading,
            "PantheonPlus": {
                "Law1": law1_p,
                "LCDM": lcdm_p,
                "CPL": cpl_p,
                "T2A_CPL": t2a_p,
                "chi2_min": {
                    "Law1": law1_p["chi2_min"],
                    "LCDM": lcdm_p["chi2_min"],
                    "CPL": cpl_p["chi2_min"],
                    "T2A_CPL": t2a_p["chi2_min"],
                },
                "verdicts_and_stats": {
                    "T1_L1": {
                        "A_r_Law1_minus_LCDM": round(a_p, 4),
                        "B_r_Law1_minus_CPL": round(b_p, 4),
                        "p_discovery_vs_LCDM": round(p_disc_p, 8),
                        "verdict": vp_t1,
                        "reasons": rp_t1,
                    },
                    "T1_Sign": {
                        **cpl_p["T1_Sign_metrics"],
                        "Delta_chi2_CPL_minus_LCDM": round(cpl_p["chi2_min"] - lcdm_p["chi2_min"], 4),
                        "Law1_z_gamma_u_gt_0": law1_p["Law1_derived_metrics"]["z_gaussian_gamma_u_gt_0"],
                        "verdict": vp_sign,
                    },
                    "T2_A": t2a_eval_p,
                },
            },
            "DES_Dovekie": {
                "Law1": law1_d,
                "LCDM": lcdm_d,
                "CPL": cpl_d,
                "T2A_CPL": t2a_d,
                "chi2_min": {
                    "Law1": law1_d["chi2_min"],
                    "LCDM": lcdm_d["chi2_min"],
                    "CPL": cpl_d["chi2_min"],
                    "T2A_CPL": t2a_d["chi2_min"],
                },
                "verdicts_and_stats": {
                    "T1_L1": {
                        "A_r_Law1_minus_LCDM": round(a_d, 4),
                        "B_r_Law1_minus_CPL": round(b_d, 4),
                        "p_discovery_vs_LCDM": round(p_disc_d, 8),
                        "verdict": vd_t1,
                        "reasons": rd_t1,
                    },
                    "T1_Sign": {
                        **cpl_d["T1_Sign_metrics"],
                        "Delta_chi2_CPL_minus_LCDM": round(cpl_d["chi2_min"] - lcdm_d["chi2_min"], 4),
                        "Law1_z_gamma_u_gt_0": law1_d["Law1_derived_metrics"]["z_gaussian_gamma_u_gt_0"],
                        "verdict": vd_sign,
                    },
                    "T2_A": t2a_eval_d,
                },
            },
            "joint_verdicts": {
                "T1_L1": {
                    "verdict": t1_l1_joint,
                    "p_T1_L1_holm": round(p_t1_holm, 8),
                    "PantheonPlus_A_r": round(a_p, 4),
                    "PantheonPlus_B_r": round(b_p, 4),
                    "DES_Dovekie_A_r": round(a_d, 4),
                    "DES_Dovekie_B_r": round(b_d, 4),
                },
                "T1_Sign": {
                    "verdict": t1_sign_joint,
                    "PantheonPlus_P_w0_gt_m1": pw0_gt_p,
                    "DES_Dovekie_P_w0_gt_m1": pw0_gt_d,
                },
                "T2_A": {
                    "verdict": t2a_joint,
                    "verdict_from_Law1_chain": t2a_joint_law1,
                    "PantheonPlus_signed_sigma": t2a_eval_p["signed_tension_sigma"],
                    "PantheonPlus_abs_sigma": t2a_eval_p["tension_sigma"],
                    "DES_Dovekie_signed_sigma": t2a_eval_d["signed_tension_sigma"],
                    "DES_Dovekie_abs_sigma": t2a_eval_d["tension_sigma"],
                },
            },
        }

    reading_b = build_reading_summary("B")
    reading_a = build_reading_summary("A")

    # T2-N1 and T2-N2 using REFERENCES.json
    omega_b_model = 1.0 / 19.0
    diff_n1 = omega_b_model - ob_ref
    z_n1_signed = diff_n1 / sig_ob_ref
    z_n1_abs = abs(z_n1_signed)
    t2_n1 = {
        "Omega_b_model": round(omega_b_model, 6),
        "Omega_b_ref": ob_ref,
        "sigma_Omega_b_ref": sig_ob_ref,
        "diff": round(diff_n1, 6),
        "signed_tension_sigma": round(z_n1_signed, 4),
        "tension_sigma": round(z_n1_abs, 4),
        "verdict": "PASS" if z_n1_abs <= 2.0 else "FAIL",
    }

    wb_ref = wb100_ref / 100.0
    sig_wb_ref = sig_wb100_ref / 100.0
    h0_pred = 100.0 * math.sqrt(19.0 * wb_ref)
    sig_h0_pred = 0.5 * h0_pred * (sig_wb_ref / wb_ref)
    sig_comb_h0 = math.sqrt(sig_h0_pred ** 2 + sig_h0_ref ** 2)
    diff_h0 = h0_pred - h0_ref
    z_n2_signed = diff_h0 / sig_comb_h0
    z_n2_abs = abs(z_n2_signed)

    # BBN-prior sensitivity for T2-N2
    wb_bbn = bbn_mu / 100.0
    sig_wb_bbn = bbn_sig / 100.0
    h0_pred_bbn = 100.0 * math.sqrt(19.0 * wb_bbn)
    sig_h0_bbn = 0.5 * h0_pred_bbn * (sig_wb_bbn / wb_bbn)
    z_n2_bbn_signed = (h0_pred_bbn - h0_ref) / math.sqrt(sig_h0_bbn ** 2 + sig_h0_ref ** 2)

    t2_n2 = {
        "H0_pred_kms_Mpc": round(h0_pred, 4),
        "sigma_H0_pred": round(sig_h0_pred, 4),
        "H0_ref_kms_Mpc": h0_ref,
        "sigma_H0_ref": sig_h0_ref,
        "sigma_comb_H0": round(sig_comb_h0, 4),
        "diff_H0": round(diff_h0, 4),
        "signed_tension_sigma": round(z_n2_signed, 4),
        "tension_sigma": round(z_n2_abs, 4),
        "verdict": "PASS" if z_n2_abs <= 2.0 else "FAIL",
        "BBN_prior_sensitivity": {
            "H0_pred": round(h0_pred_bbn, 4),
            "sigma_H0_pred": round(sig_h0_bbn, 4),
            "signed_tension_sigma": round(z_n2_bbn_signed, 4),
            "tension_sigma": round(abs(z_n2_bbn_signed), 4),
        },
    }

    reading_b["joint_verdicts"]["T2_N1"] = {
        "verdict": t2_n1["verdict"],
        "signed_sigma": t2_n1["signed_tension_sigma"],
        "abs_sigma": t2_n1["tension_sigma"],
    }
    reading_b["joint_verdicts"]["T2_N2"] = {
        "verdict": t2_n2["verdict"],
        "signed_sigma": t2_n2["signed_tension_sigma"],
        "abs_sigma": t2_n2["tension_sigma"],
    }

    return {
        "universe_id": universe_id,
        "family": "COSMO",
        "round": round_num,
        "elapsed_sec": round(wall_elapsed_sec, 3),
        "references_used": refs,
        "Reading_B": reading_b,
        "Reading_A": reading_a,
        "T2_N1": t2_n1,
        "T2_N2": t2_n2,
    }


def _compute_sparc_param_uncertainty(
    train_galaxies: list[dict],
    model_type: str,
    f_leak: float,
    fitted_param: float,
    seed: int,
) -> dict:
    """
    Compute mean +- 1sigma and 95% interval [p2.5, p97.5] for fitted sigma_ref (T5-A) or k (T5-B)
    on the 88 training galaxies via:
      1. 1,000-replicate training-galaxy bootstrap ('bootstrap'),
      2. Profile posterior under sum_chi2_red ('posterior_sum_chi2_red'),
      3. Profile posterior under total_chi2 ('posterior_total_chi2').
    """
    bounds = (0.1, 100.0) if model_type == "T5A" else (0.05, 50.0)
    # Build composite grid: 600 log-spaced nodes across full range + 400 linear nodes around fitted_param
    lo_local = max(bounds[0], fitted_param * 0.65)
    hi_local = min(bounds[1], fitted_param * 1.45)
    grid = np.unique(
        np.concatenate([
            np.geomspace(bounds[0], bounds[1], 600),
            np.linspace(lo_local, hi_local, 400),
            np.array([fitted_param]),
        ])
    )
    n_grid = len(grid)
    n_train = len(train_galaxies)

    # Matrix of per-galaxy chi2_red (n_train x n_grid) and n_pts vector (n_train,)
    chi2_red_mat = np.empty((n_train, n_grid), dtype=float)
    n_pts_vec = np.array([g["n_pts"] for g in train_galaxies], dtype=float)

    for j, x_val in enumerate(grid):
        val_f = float(x_val)
        for i, gal in enumerate(train_galaxies):
            sig_g = val_f if model_type == "T5A" else val_f * gal["r_disk_kpc"]
            v_pred = sparc_t5.predict_galaxy_rotation_curve(gal, sig_g, f_leak)
            res = (gal["v_obs"] - v_pred) / gal["e_v_obs"]
            c2_gal = float(np.sum(res * res))
            chi2_red_mat[i, j] = c2_gal / gal["n_pts"]

    sum_chi2_red_grid = np.sum(chi2_red_mat, axis=0)
    tot_chi2_grid = np.dot(n_pts_vec, chi2_red_mat)

    def posterior_from_loss(loss_arr: np.ndarray) -> dict:
        dloss = loss_arr - np.min(loss_arr)
        w = np.exp(-0.5 * np.clip(dloss, 0.0, 700.0))
        # Trapezoidal integration weights on grid
        trap_w = np.zeros_like(grid)
        trap_w[0] = 0.5 * (grid[1] - grid[0])
        trap_w[-1] = 0.5 * (grid[-1] - grid[-2])
        trap_w[1:-1] = 0.5 * (grid[2:] - grid[:-2])
        pw = w * trap_w
        pw_sum = float(np.sum(pw))
        if pw_sum <= 0.0:
            return {
                "mean": round(fitted_param, 6),
                "std": 0.0,
                "ci95": [round(fitted_param, 6), round(fitted_param, 6)],
            }
        pw /= pw_sum
        mean_val = float(np.sum(pw * grid))
        std_val = float(np.sqrt(max(0.0, float(np.sum(pw * ((grid - mean_val) ** 2))))))
        cdf = np.cumsum(pw)
        p2p5 = float(np.interp(0.025, cdf, grid))
        p16 = float(np.interp(0.16, cdf, grid))
        p50 = float(np.interp(0.50, cdf, grid))
        p84 = float(np.interp(0.84, cdf, grid))
        p97p5 = float(np.interp(0.975, cdf, grid))
        return {
            "mean": round(mean_val, 6),
            "std": round(std_val, 6),
            "median": round(p50, 6),
            "sigma_68": round(0.5 * (p84 - p16), 6),
            "ci95": [round(p2p5, 6), round(p97p5, 6)],
        }

    # 1,000-replicate training-galaxy bootstrap
    rng = np.random.default_rng(seed)
    n_boot = 1000
    boot_idx = rng.integers(0, n_train, size=(n_boot, n_train))
    counts = np.zeros((n_boot, n_train), dtype=float)
    for b in range(n_boot):
        np.add.at(counts[b], boot_idx[b], 1.0)
    boot_losses = counts @ chi2_red_mat  # shape (n_boot, n_grid)
    best_grid_indices = np.argmin(boot_losses, axis=1)
    boot_opt = np.empty(n_boot, dtype=float)
    for b in range(n_boot):
        idx = int(best_grid_indices[b])
        if 0 < idx < (n_grid - 1):
            x1, x2, x3 = grid[idx - 1], grid[idx], grid[idx + 1]
            y1, y2, y3 = boot_losses[b, idx - 1], boot_losses[b, idx], boot_losses[b, idx + 1]
            # 3-point parabolic vertex refinement
            denom = (x1 - x2) * (x1 - x3) * (x2 - x3)
            if abs(denom) > 1e-18:
                A = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / denom
                B = (x3 * x3 * (y1 - y2) + x2 * x2 * (y3 - y1) + x1 * x1 * (y2 - y3)) / denom
                if A > 0.0:
                    xv = -B / (2.0 * A)
                    boot_opt[b] = float(np.clip(xv, x1, x3))
                else:
                    boot_opt[b] = float(x2)
            else:
                boot_opt[b] = float(x2)
        else:
            boot_opt[b] = float(grid[idx])

    return {
        "point_estimate": round(fitted_param, 6),
        "bootstrap_train_galaxies": summarize_samples(boot_opt),
        "posterior_sum_chi2_red": posterior_from_loss(sum_chi2_red_grid),
        "posterior_total_chi2": posterior_from_loss(tot_chi2_grid),
    }


def run_single_galaxy_universe(task: dict) -> dict:
    """
    Worker function running registered T5-A and T5-B procedures on a GALAXY mock universe
    with fixed f_leak = 1/6.
    """
    set_below_normal_priority()
    t0 = time.perf_counter()

    universe_id = task["universe_id"]
    round_num = int(task["round"])
    u_dir = Path(task["u_dir"])
    seed = int(task["seed"])
    f_leak = 1.0 / 6.0

    sparc_galaxies = sparc_t5.parse_sparc_catalog(u_dir / "sparc")
    sparc_train = [g for g in sparc_galaxies if g["split"] == "train"]
    sparc_test = [g for g in sparc_galaxies if g["split"] == "test"]

    # Registered T5-A fit on training half and score on test half
    t5a_fit = sparc_t5.fit_sparc_parameter(sparc_train, "T5A", f_leak, loss_metric="sum_chi2_red")
    sigma_ref_hat = float(t5a_fit["fitted_param"])
    t5a_test_eval = sparc_t5.evaluate_sparc_sample(sparc_test, "T5A", sigma_ref_hat, f_leak)
    t5a_verdict, t5a_reasons = sparc_t5.score_t5_subtest(t5a_test_eval)
    t5a_test_clean = dict(t5a_test_eval)
    t5a_test_clean.pop("per_galaxy", None)

    # Registered T5-B fit on training half and score on test half
    t5b_fit = sparc_t5.fit_sparc_parameter(sparc_train, "T5B", f_leak, loss_metric="sum_chi2_red")
    k_hat = float(t5b_fit["fitted_param"])
    t5b_test_eval = sparc_t5.evaluate_sparc_sample(sparc_test, "T5B", k_hat, f_leak)
    t5b_verdict, t5b_reasons = sparc_t5.score_t5_subtest(t5b_test_eval)
    t5b_test_clean = dict(t5b_test_eval)
    t5b_test_clean.pop("per_galaxy", None)

    # Uncertainty summaries (mean +- 1sigma, 95% interval) on fitted sigma_ref and k
    sigma_ref_unc = _compute_sparc_param_uncertainty(sparc_train, "T5A", f_leak, sigma_ref_hat, seed)
    k_unc = _compute_sparc_param_uncertainty(sparc_train, "T5B", f_leak, k_hat, seed + 1)

    elapsed_s = time.perf_counter() - t0
    return {
        "universe_id": universe_id,
        "family": "GALAXY",
        "round": round_num,
        "elapsed_sec": round(elapsed_s, 3),
        "f_leak_used": f_leak,
        "T5_A": {
            "fitted_sigma_ref_kpc": round(sigma_ref_hat, 6),
            "sigma_ref_uncertainty": sigma_ref_unc,
            "training_fit": t5a_fit,
            "test_evaluation": t5a_test_clean,
            "test_median_chi2_red": round(float(t5a_test_eval["median_chi2_red"]), 6),
            "test_frac_chi2_red_lt_2": round(float(t5a_test_eval["frac_chi2_red_lt_2"]), 6),
            "n_test_lt_2": int(round(float(t5a_test_eval["frac_chi2_red_lt_2"]) * t5a_test_eval["n_galaxies"])),
            "n_test_galaxies": int(t5a_test_eval["n_galaxies"]),
            "verdict": t5a_verdict,
            "reasons": t5a_reasons,
        },
        "T5_B": {
            "fitted_k": round(k_hat, 6),
            "k_uncertainty": k_unc,
            "training_fit": t5b_fit,
            "test_evaluation": t5b_test_clean,
            "test_median_chi2_red": round(float(t5b_test_eval["median_chi2_red"]), 6),
            "test_frac_chi2_red_lt_2": round(float(t5b_test_eval["frac_chi2_red_lt_2"]), 6),
            "n_test_lt_2": int(round(float(t5b_test_eval["frac_chi2_red_lt_2"]) * t5b_test_eval["n_galaxies"])),
            "n_test_galaxies": int(t5b_test_eval["n_galaxies"]),
            "verdict": t5b_verdict,
            "reasons": t5b_reasons,
        },
    }


def run_single_regional_universe(task: dict) -> dict:
    """
    Worker function running registered T6 procedure on a REGIONAL mock universe.
    """
    set_below_normal_priority()
    t0 = time.perf_counter()

    universe_id = task["universe_id"]
    round_num = int(task["round"])
    u_dir = Path(task["u_dir"])

    pantheon_full = local_h0_t6.load_pantheon_plus_full(u_dir / "pantheonplus")
    cal_fit = local_h0_t6.fit_t6_calibrators(pantheon_full)
    mb_fixed = float(cal_fit["M_B_fixed"])
    sig_mb_fixed = float(cal_fit["sigma_M_B_fixed"])

    t6_deciding = local_h0_t6.evaluate_t6_hubble_flow(
        pantheon_full, mb_fixed, sig_mb_fixed, coord_frame="galactic", z_col="zHD", apply_merge=True
    )

    # Also attach total uncertainty (including calibrator zero-point) per region alongside HF-only error
    for reg_row in t6_deciding["regional_H0"]:
        h0_i = float(reg_row["H0_kms_Mpc"])
        sig_hf = float(reg_row["sigma_H0_hf_only"])
        sig_cal_i = (math.log(10.0) / 5.0) * h0_i * sig_mb_fixed
        reg_row["sigma_H0_total_incl_cal"] = round(math.sqrt(sig_hf ** 2 + sig_cal_i ** 2), 4)

    elapsed_s = time.perf_counter() - t0
    return {
        "universe_id": universe_id,
        "family": "REGIONAL",
        "round": round_num,
        "elapsed_sec": round(elapsed_s, 3),
        "calibrator_fit": cal_fit,
        "T6": t6_deciding,
    }
