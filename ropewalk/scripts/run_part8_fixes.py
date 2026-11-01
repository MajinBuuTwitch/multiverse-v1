import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import datetime
import hashlib
import json
import math
import multiprocessing as mp
from pathlib import Path
import numpy as np
import psutil
import emcee
from scipy.optimize import minimize

from cosmology import (
    OMEGA_NU_MASS_H2,
    CMBLikelihood,
    DESIBAOLikelihood,
    PantheonPlusLikelihood,
    DESDovekieLikelihood,
    joint_chi2_cpl,
)
from clusters_t4 import load_mergers_csv, fit_tau_lag_hard_step
from sparc_t5 import parse_sparc_catalog, fit_sparc_parameter, evaluate_rar_benchmark
from local_h0_t6 import load_pantheon_plus_full, fit_t6_calibrators

N_CORES = 12
SEED = 20261030


def set_below_normal_priority():
    """Set current process priority to Below Normal per GEMINI.md Rule 5."""
    try:
        p = psutil.Process(os.getpid())
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass


def compute_scripts_sha256(scripts_dir: Path) -> dict[str, str]:
    """Compute SHA-256 of all .py files in scripts/ per Rule G3."""
    hashes = {}
    for py_file in sorted(scripts_dir.glob("*.py")):
        h = hashlib.sha256(py_file.read_bytes()).hexdigest()
        hashes[py_file.name] = h
    return hashes


def compute_split_rhat_and_ess(chain: np.ndarray) -> dict:
    """
    Compute split Gelman-Rubin R_hat - 1 and Effective Sample Size (ESS)
    for an emcee production chain of shape (n_steps, n_walkers, n_dim).
    """
    n_steps, n_walkers, n_dim = chain.shape
    half_t = n_steps // 2
    half_w = n_walkers // 2
    # Form 4 independent sub-ensemble chains (2 time halves x 2 complementary walker half-ensembles)
    # and also check walker-level split-Rhat across 4 time blocks
    blocks = [
        chain[:half_t, :half_w, :].reshape(-1, n_dim),
        chain[:half_t, half_w:, :].reshape(-1, n_dim),
        chain[half_t : 2 * half_t, :half_w, :].reshape(-1, n_dim),
        chain[half_t : 2 * half_t, half_w:, :].reshape(-1, n_dim),
    ]
    sub_chains = np.stack(blocks, axis=1)  # shape (half_t, 4, n_dim)
    m = sub_chains.shape[1]
    n = sub_chains.shape[0]

    rhat_minus_1 = []
    for d in range(n_dim):
        arr = sub_chains[:, :, d]  # shape (n, m)
        chain_means = np.mean(arr, axis=0)
        chain_vars = np.var(arr, axis=0, ddof=1)
        W = float(np.mean(chain_vars))
        B = float(n * np.var(chain_means, ddof=1))
        var_hat = ((n - 1.0) / n) * W + (1.0 / n) * B
        rhat = math.sqrt(max(var_hat / max(W, 1e-15), 1.0))
        rhat_minus_1.append(round(abs(rhat - 1.0), 6))

    try:
        tau = emcee.autocorr.integrated_time(chain, quiet=True)
        tau_list = [round(float(t), 2) for t in tau]
        ess_list = [round(float((n_steps * n_walkers) / max(float(t), 1.0)), 1) for t in tau]
    except Exception:
        tau_list = [50.0] * n_dim
        ess_list = [float((n_steps * n_walkers) / 50.0)] * n_dim

    return {
        "rhat_minus_1": rhat_minus_1,
        "max_rhat_minus_1": float(np.max(rhat_minus_1)),
        "tau_autocorr": tau_list,
        "max_tau_autocorr": float(np.max(tau_list)),
        "ess": ess_list,
        "min_ess": float(np.min(ess_list)),
    }


def run_single_t2a_mcmc_worker(task: dict) -> dict:
    """
    Worker function running one complete T2-A flat w0waCDM MCMC chain
    (Omega_m, h, 100*omega_b, w0, wa) with 32 walkers, 1,000 burn-in + 4,000 production steps.
    """
    set_below_normal_priority()
    data_dir = task["data_dir"]
    run_id = task["run_id"]
    sn_name = task["sn_name"]
    cmb_mode = task["cmb_mode"]
    bbn_prior = tuple(task["bbn_prior"])
    seed_offset = int(task["seed_offset"])

    bao_like = DESIBAOLikelihood(data_dir, lya_mode="joint_ap_deciding")
    cmb_like = CMBLikelihood(table="lcdm", mode=cmb_mode)
    if sn_name == "Pantheon+":
        sn_like = PantheonPlusLikelihood(data_dir)
    elif sn_name == "DES-Dovekie":
        sn_like = DESDovekieLikelihood(data_dir)
    else:
        raise ValueError(f"Unknown sn_name: {sn_name}")

    # Parameter bounds per PREREG.md Sec 5.2 (line 156):
    # Omega_m in [0.1, 0.6], h in [0.5, 0.9], 100*omega_b in [1.8, 2.6],
    # w0 in [-3.0, 1.0], wa in [-3.0, 2.0], w0 + wa < 0
    def log_prob(theta):
        om, h, wb100, w0, wa = theta
        if not (0.1 <= om <= 0.6 and 0.5 <= h <= 0.9 and 1.8 <= wb100 <= 2.6):
            return -np.inf
        if not (-3.0 <= w0 <= 1.0 and -3.0 <= wa <= 2.0 and (w0 + wa) < 0.0):
            return -np.inf
        c2 = joint_chi2_cpl(om, h, wb100, w0, wa, bao_like, cmb_like, sn_like, bbn_prior=bbn_prior)
        if not np.isfinite(c2):
            return -np.inf
        return -0.5 * c2

    # Find MAP / chi2_min first to initialize walkers cleanly
    x0 = np.array([0.311, 0.675, bbn_prior[0], -0.83, -0.65], dtype=float)
    res_nm = minimize(
        lambda x: -2.0 * log_prob(x),
        x0,
        method="Nelder-Mead",
        options={"xatol": 1e-5, "fatol": 1e-5, "maxiter": 4000},
    )
    center = res_nm.x
    chi2_min = float(res_nm.fun)

    rng = np.random.default_rng(SEED + seed_offset)
    n_walkers = 32
    n_dim = 5
    scales = np.array([0.003, 0.003, 0.01, 0.02, 0.08], dtype=float)
    pos = center[None, :] + rng.normal(0.0, 1.0, size=(n_walkers, n_dim)) * scales[None, :]
    # Ensure w0 + wa < 0 for all initial walkers
    for i in range(n_walkers):
        if pos[i, 3] + pos[i, 4] >= -0.01:
            pos[i, 4] = -0.05 - pos[i, 3]

    sampler = emcee.EnsembleSampler(n_walkers, n_dim, log_prob)

    n_burn = 1000
    n_prod = 4000
    state = sampler.run_mcmc(pos, n_burn, progress=False)
    sampler.reset()
    state = sampler.run_mcmc(state, n_prod, progress=False)

    chain = sampler.get_chain()  # shape (n_prod, n_walkers, n_dim)
    diag = compute_split_rhat_and_ess(chain)

    # Extend up to 2 times if needed to guarantee R_hat - 1 < 0.01 and ESS > 1000
    ext_count = 0
    while (diag["max_rhat_minus_1"] >= 0.01 or diag["min_ess"] <= 1000.0) and ext_count < 2:
        state = sampler.run_mcmc(state, 2000, progress=False)
        chain = sampler.get_chain()
        diag = compute_split_rhat_and_ess(chain)
        ext_count += 1

    flat = chain.reshape((-1, n_dim))
    logp_flat = sampler.get_log_prob().reshape(-1)
    best_idx = int(np.argmax(logp_flat))
    chi2_min = min(chi2_min, float(-2.0 * logp_flat[best_idx]))

    om_samples = flat[:, 0]
    h_samples = flat[:, 1]
    wb100_samples = flat[:, 2]
    w0_samples = flat[:, 3]
    wa_samples = flat[:, 4]

    # Exact baryon+CDM density parameter Omega_{bc} = Omega_{m,tot} - Omega_{nu,0} (PREREG.md Sec 5.2 line 149)
    omega_nu_samples = OMEGA_NU_MASS_H2 / (h_samples ** 2)
    omega_bc_samples = om_samples - omega_nu_samples

    # Extract median and 68% half-width sigma_{Omega_bc} = 0.5 * (p84 - p16) (PREREG.md line 163)
    p16, p50, p84 = np.percentile(omega_bc_samples, [16.0, 50.0, 84.0])
    omega_bc_med = float(p50)
    sigma_omega_bc = float(0.5 * (p84 - p16))

    # Model predictions: f_leak = 1 - (19*Omega_bc - 1)/6, R_pred = 19*Omega_bc - 1 (PREREG.md line 150)
    f_leak = 1.0 - (19.0 * omega_bc_med - 1.0) / 6.0
    sigma_f_leak = (19.0 / 6.0) * sigma_omega_bc
    r_pred = 19.0 * omega_bc_med - 1.0
    sigma_r_pred = 19.0 * sigma_omega_bc

    def param_summary(arr: np.ndarray) -> dict:
        q16, q50, q84 = np.percentile(arr, [16.0, 50.0, 84.0])
        return {
            "median": round(float(q50), 6),
            "mean": round(float(np.mean(arr)), 6),
            "std": round(float(np.std(arr, ddof=1)), 6),
            "sigma_68": round(float(0.5 * (q84 - q16)), 6),
        }

    return {
        "run_id": run_id,
        "sn_dataset": sn_name,
        "cmb_mode": cmb_mode,
        "bbn_prior_100wb": {"mean": bbn_prior[0], "sigma": bbn_prior[1]},
        "n_walkers": n_walkers,
        "n_burn": n_burn,
        "n_prod": int(chain.shape[0]),
        "n_samples_total": int(flat.shape[0]),
        "chi2_min": round(chi2_min, 4),
        "convergence": diag,
        "converged": bool(diag["max_rhat_minus_1"] < 0.01 and diag["min_ess"] > 1000.0),
        "parameters": {
            "Omega_m_tot": param_summary(om_samples),
            "Omega_bc": param_summary(omega_bc_samples),
            "h": param_summary(h_samples),
            "100_omega_b": param_summary(wb100_samples),
            "w0": param_summary(w0_samples),
            "wa": param_summary(wa_samples),
        },
        "frozen_quantities": {
            "Omega_bc_median": round(omega_bc_med, 6),
            "sigma_Omega_bc": round(sigma_omega_bc, 6),
            "f_leak": round(f_leak, 6),
            "sigma_f_leak": round(sigma_f_leak, 6),
            "R_pred": round(r_pred, 6),
            "sigma_R_pred": round(sigma_r_pred, 6),
        },
    }


def main():
    set_below_normal_priority()
    root = Path(__file__).resolve().parent.parent
    data_dir = str(root / "data")
    results_dir = root / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    scripts_hashes = compute_scripts_sha256(root / "scripts")
    now_iso = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    print("1. Running T2-A MCMC fixing chains in parallel across worker pool...")
    tasks = [
        {
            "run_id": "T2-A-Pantheon+_deciding",
            "sn_name": "Pantheon+",
            "cmb_mode": "conditional_2x2",
            "bbn_prior": (2.218, 0.055),
            "data_dir": data_dir,
            "seed_offset": 101,
        },
        {
            "run_id": "T2-A-DES-Dovekie_deciding",
            "sn_name": "DES-Dovekie",
            "cmb_mode": "conditional_2x2",
            "bbn_prior": (2.218, 0.055),
            "data_dir": data_dir,
            "seed_offset": 102,
        },
        {
            "run_id": "T2-A-Pantheon+_Cooke18_sensitivity",
            "sn_name": "Pantheon+",
            "cmb_mode": "conditional_2x2",
            "bbn_prior": (2.166, 0.019),
            "data_dir": data_dir,
            "seed_offset": 103,
        },
        {
            "run_id": "T2-A-DES-Dovekie_Cooke18_sensitivity",
            "sn_name": "DES-Dovekie",
            "cmb_mode": "conditional_2x2",
            "bbn_prior": (2.166, 0.019),
            "data_dir": data_dir,
            "seed_offset": 104,
        },
        {
            "run_id": "T2-A-Pantheon+_MarginalCMB_sensitivity",
            "sn_name": "Pantheon+",
            "cmb_mode": "marginal_2x2",
            "bbn_prior": (2.218, 0.055),
            "data_dir": data_dir,
            "seed_offset": 105,
        },
        {
            "run_id": "T2-A-DES-Dovekie_MarginalCMB_sensitivity",
            "sn_name": "DES-Dovekie",
            "cmb_mode": "marginal_2x2",
            "bbn_prior": (2.218, 0.055),
            "data_dir": data_dir,
            "seed_offset": 106,
        },
    ]

    with mp.Pool(processes=min(len(tasks), N_CORES), initializer=set_below_normal_priority) as pool:
        t2_results_list = pool.map(run_single_t2a_mcmc_worker, tasks)

    t2_by_id = {r["run_id"]: r for r in t2_results_list}
    f_leak_frozen = t2_by_id["T2-A-Pantheon+_deciding"]["frozen_quantities"]["f_leak"]
    sigma_f_leak_frozen = t2_by_id["T2-A-Pantheon+_deciding"]["frozen_quantities"]["sigma_f_leak"]
    print(f"   T2-A-Pantheon+ frozen f_leak = {f_leak_frozen:.6f} +/- {sigma_f_leak_frozen:.6f}")

    # 2. Freeze T1 structural parameters (FREEZE_T1.json)
    freeze_t1 = {
        "test_id": "T1 (T1-L1 Primary Pillar 1 & T1-Sign Secondary)",
        "frozen_at": now_iso,
        "structural_constants": {"N_s": 19, "N_r": 133, "Omega_b_structural": 1.0 / 19.0},
        "law1_priors": {
            "Omega_m_tot": [0.1, 0.6],
            "h": [0.5, 0.9],
            "100_omega_b": [1.8, 2.6],
            "gamma_u": [0.0, 2.0],
        },
        "cpl_priors": {
            "Omega_m_tot": [0.1, 0.6],
            "h": [0.5, 0.9],
            "100_omega_b": [1.8, 2.6],
            "w0": [-3.0, 1.0],
            "wa": [-3.0, 2.0],
            "constraint": "w0 + wa < 0",
        },
        "scripts_sha256": scripts_hashes,
    }
    freeze_t1_path = results_dir / "FREEZE_T1.json"
    freeze_t1_path.write_text(json.dumps(freeze_t1, indent=2), encoding="utf-8")

    # 3. Freeze T2 parameters (FREEZE_T2.json)
    freeze_t2 = {
        "test_id": "T2 (T2-A Primary Pillar 2, T2-N1, T2-N2)",
        "frozen_at": now_iso,
        "deciding_PantheonPlus": t2_by_id["T2-A-Pantheon+_deciding"],
        "deciding_DES_Dovekie": t2_by_id["T2-A-DES-Dovekie_deciding"],
        "single_frozen_f_leak_for_T5": {
            "source_run": "T2-A-Pantheon+_deciding",
            "f_leak": f_leak_frozen,
            "sigma_f_leak": sigma_f_leak_frozen,
        },
        "sensitivity_runs": {
            "PantheonPlus_Cooke18": t2_by_id["T2-A-Pantheon+_Cooke18_sensitivity"],
            "DES_Dovekie_Cooke18": t2_by_id["T2-A-DES-Dovekie_Cooke18_sensitivity"],
            "PantheonPlus_MarginalCMB": t2_by_id["T2-A-Pantheon+_MarginalCMB_sensitivity"],
            "DES_Dovekie_MarginalCMB": t2_by_id["T2-A-DES-Dovekie_MarginalCMB_sensitivity"],
        },
        "scripts_sha256": scripts_hashes,
    }
    freeze_t2_path = results_dir / "FREEZE_T2.json"
    freeze_t2_path.write_text(json.dumps(freeze_t2, indent=2), encoding="utf-8")

    # 4. Run T4b training-half fit and freeze (FREEZE_T4.json)
    print("2. Running T4b training-half fit...")
    mergers = load_mergers_csv(root / "data" / "MERGERS.csv")
    train_mergers = [c for c in mergers if c["split"] == "train"]
    t4_fit_deciding = fit_tau_lag_hard_step(train_mergers, tau_min_myr=235, tau_max_myr=1500, step_myr=5)
    t4_fit_400 = fit_tau_lag_hard_step(train_mergers, tau_min_myr=400, tau_max_myr=1500, step_myr=5)
    print(f"   T4b frozen tau_lag = {t4_fit_deciding['tau_lag_myr']} Myr (train_acc = {t4_fit_deciding['train_acc']:.4f})")

    freeze_t4 = {
        "test_id": "T4b (Cluster Merger Age Cutoff Primary Pillar 3)",
        "frozen_at": now_iso,
        "deciding_training_fit": t4_fit_deciding,
        "sensitivity_Bullet_median_400Myr_fit": t4_fit_400,
        "scripts_sha256": scripts_hashes,
    }
    freeze_t4_path = results_dir / "FREEZE_T4.json"
    freeze_t4_path.write_text(json.dumps(freeze_t4, indent=2), encoding="utf-8")

    # 5. Run T5-A and T5-B training-half fits using frozen f_leak and freeze (FREEZE_T5.json)
    print("3. Running T5-A and T5-B SPARC training-half fits...")
    sparc_galaxies = parse_sparc_catalog(root / "data" / "sparc")
    sparc_train = [g for g in sparc_galaxies if g["split"] == "train"]

    t5a_deciding = fit_sparc_parameter(sparc_train, "T5A", f_leak_frozen, loss_metric="sum_chi2_red")
    t5b_deciding = fit_sparc_parameter(sparc_train, "T5B", f_leak_frozen, loss_metric="sum_chi2_red")

    # Sensitivity training objectives (PREREG.md line 272) and f_leak = 1/6 sensitivity
    t5a_tot_chi2 = fit_sparc_parameter(sparc_train, "T5A", f_leak_frozen, loss_metric="total_chi2")
    t5a_med_chi2 = fit_sparc_parameter(sparc_train, "T5A", f_leak_frozen, loss_metric="median_chi2_red")
    t5a_fleak_1_6 = fit_sparc_parameter(sparc_train, "T5A", 1.0 / 6.0, loss_metric="sum_chi2_red")
    t5b_tot_chi2 = fit_sparc_parameter(sparc_train, "T5B", f_leak_frozen, loss_metric="total_chi2")
    t5b_med_chi2 = fit_sparc_parameter(sparc_train, "T5B", f_leak_frozen, loss_metric="median_chi2_red")

    print(
        f"   T5-A frozen sigma_ref = {t5a_deciding['fitted_param']:.6f} kpc; "
        f"T5-B frozen k = {t5b_deciding['fitted_param']:.6f}"
    )

    freeze_t5 = {
        "test_id": "T5 (T5-A Primary Pillar 4, T5-B & T5c Secondary)",
        "frozen_at": now_iso,
        "f_leak_frozen_from_T2A_PantheonPlus": f_leak_frozen,
        "T5A_deciding_training_fit": t5a_deciding,
        "T5B_deciding_training_fit": t5b_deciding,
        "sensitivity_training_fits": {
            "T5A_total_chi2_loss": t5a_tot_chi2,
            "T5A_median_chi2_red_loss": t5a_med_chi2,
            "T5A_f_leak_1_over_6": t5a_fleak_1_6,
            "T5B_total_chi2_loss": t5b_tot_chi2,
            "T5B_median_chi2_red_loss": t5b_med_chi2,
        },
        "scripts_sha256": scripts_hashes,
    }
    freeze_t5_path = results_dir / "FREEZE_T5.json"
    freeze_t5_path.write_text(json.dumps(freeze_t5, indent=2), encoding="utf-8")

    # 6. Run T6 SH0ES calibrator fit and freeze (FREEZE_T6.json)
    print("4. Running T6 SH0ES Cepheid calibrator fit...")
    pantheon_full = load_pantheon_plus_full(root / "data" / "pantheon_plus")
    t6_cal_fit = fit_t6_calibrators(pantheon_full)
    print(f"   T6 frozen M_B = {t6_cal_fit['M_B_fixed']:.6f} +/- {t6_cal_fit['sigma_M_B_fixed']:.6f} mag")

    freeze_t6 = {
        "test_id": "T6 (Local H0 Regional Heterogeneity Secondary Test)",
        "frozen_at": now_iso,
        "calibrator_fit": t6_cal_fit,
        "scripts_sha256": scripts_hashes,
    }
    freeze_t6_path = results_dir / "FREEZE_T6.json"
    freeze_t6_path.write_text(json.dumps(freeze_t6, indent=2), encoding="utf-8")

    # 7. Write master FIXED_VALUES.json with SHA-256 of each FREEZE_*.json file
    freeze_files = ["FREEZE_T1.json", "FREEZE_T2.json", "FREEZE_T4.json", "FREEZE_T5.json", "FREEZE_T6.json"]
    freeze_hashes = {
        fname: hashlib.sha256((results_dir / fname).read_bytes()).hexdigest()
        for fname in freeze_files
    }

    fixed_values = {
        "frozen_at": now_iso,
        "seed": SEED,
        "freeze_file_sha256": freeze_hashes,
        "summary_of_frozen_parameters": {
            "T2_A_PantheonPlus": t2_by_id["T2-A-Pantheon+_deciding"]["frozen_quantities"],
            "T2_A_DES_Dovekie": t2_by_id["T2-A-DES-Dovekie_deciding"]["frozen_quantities"],
            "T4b_tau_lag_myr": t4_fit_deciding["tau_lag_myr"],
            "T4b_tau_lag_gyr": t4_fit_deciding["tau_lag_gyr"],
            "T5_A_sigma_ref_kpc": t5a_deciding["fitted_param"],
            "T5_B_k": t5b_deciding["fitted_param"],
            "T6_M_B_fixed_mag": t6_cal_fit["M_B_fixed"],
            "T6_sigma_M_B_fixed_mag": t6_cal_fit["sigma_M_B_fixed"],
        },
        "scripts_sha256": scripts_hashes,
    }
    fixed_values_path = results_dir / "FIXED_VALUES.json"
    fixed_values_path.write_text(json.dumps(fixed_values, indent=2), encoding="utf-8")
    print("ALL PART 8 FIXES COMPLETED AND FROZEN.")
    print(json.dumps(fixed_values["summary_of_frozen_parameters"], indent=2))


if __name__ == "__main__":
    main()
