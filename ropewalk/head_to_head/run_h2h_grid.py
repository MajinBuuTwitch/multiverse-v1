import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import json
import math
import multiprocessing as mp
import sys
import time
import numpy as np
import psutil
from scipy import optimize
import dynesty
from dynesty import utils as dyfunc

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

N_CORES = 12
NLIVE = 1000
DLOGZ = 0.01
SEEDS = [20261030, 20261031, 20261032]

_WORKER_DATA = {}


def _init_worker(data_dir: str):
    os.environ["OMP_NUM_THREADS"] = "1"
    os.environ["MKL_NUM_THREADS"] = "1"
    os.environ["OPENBLAS_NUM_THREADS"] = "1"
    os.environ["NUMEXPR_NUM_THREADS"] = "1"
    try:
        psutil.Process(os.getpid()).nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    _WORKER_DATA["bao"] = cosmo.DESIBAOLikelihood(data_dir, lya_mode="joint_ap_deciding")
    _WORKER_DATA["cmb"] = cosmo.CMBLikelihood(table="lcdm", mode="full_3x3")
    _WORKER_DATA["Pantheon+"] = cosmo.PantheonPlusLikelihood(data_dir)
    _WORKER_DATA["DES-Dovekie"] = cosmo.DESDovekieLikelihood(data_dir)


def _cpl_w0_wa_from_unit(u3: float, u4: float) -> tuple[float, float]:
    """
    Exact constant-Jacobian mapping from [0, 1]^2 onto the polygon
    P = {(w0, wa) in [-3, 1] x [-3, 2] : w0 + wa < 0} of area 15.5 [Established].
    """
    area = 15.5 * float(u3)
    if area <= 5.0:
        w0 = -3.0 + area / 5.0
    else:
        w0 = 3.0 - math.sqrt(max(0.0, 35.0 - 2.0 * area))
    wa_max = min(2.0, -w0)
    wa = -3.0 + float(u4) * (wa_max + 3.0)
    return w0, wa


def _run_single_seed_task(task: dict) -> dict:
    """Execute one (run_id, seed) nested-sampling run and save chain + log to disk."""
    try:
        psutil.Process(os.getpid()).nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass

    run_id = task["run_id"]
    task_id = task["task_id"]
    model = task["model"]
    sn_name = task["sn_name"]
    reading = task["reading"]
    gamma_u_max = task.get("gamma_u_max", 2.0)
    seed = int(task["seed"])

    chains_dir = os.path.join(H2H_DIR, "chains")
    logs_dir = os.path.join(H2H_DIR, "logs")
    os.makedirs(chains_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)
    log_path = os.path.join(logs_dir, f"{task_id}.json")
    chain_path = os.path.join(chains_dir, f"{task_id}.npz")

    if os.path.exists(log_path) and os.path.exists(chain_path):
        with open(log_path, "r", encoding="utf-8") as f:
            return json.load(f)

    bao_like = _WORKER_DATA["bao"]
    cmb_like = _WORKER_DATA["cmb"]
    sn_like = _WORKER_DATA[sn_name]

    if model == "LCDM":
        ndim = 3
        param_names = ["Omega_bc", "h", "100_omega_b"]
        bounds = [(0.10, 0.50), (0.50, 0.90), (1.80, 2.60)]

        def prior_transform(u):
            return np.array(
                [
                    0.10 + 0.40 * u[0],
                    0.50 + 0.40 * u[1],
                    1.80 + 0.80 * u[2],
                ],
                dtype=float,
            )

        def chi2_fn(theta):
            return h2h.joint_chi2_cpl_reading(
                float(theta[0]), float(theta[1]), float(theta[2]), -1.0, 0.0, reading, bao_like, cmb_like, sn_like
            )

    elif model == "CPL":
        ndim = 5
        param_names = ["Omega_bc", "h", "100_omega_b", "w0", "wa"]
        bounds = [(0.10, 0.50), (0.50, 0.90), (1.80, 2.60), (-3.0, 1.0), (-3.0, 2.0)]

        def prior_transform(u):
            w0, wa = _cpl_w0_wa_from_unit(u[3], u[4])
            return np.array(
                [
                    0.10 + 0.40 * u[0],
                    0.50 + 0.40 * u[1],
                    1.80 + 0.80 * u[2],
                    w0,
                    wa,
                ],
                dtype=float,
            )

        def chi2_fn(theta):
            if theta[3] + theta[4] >= 0.0:
                return np.inf
            return h2h.joint_chi2_cpl_reading(
                float(theta[0]),
                float(theta[1]),
                float(theta[2]),
                float(theta[3]),
                float(theta[4]),
                reading,
                bao_like,
                cmb_like,
                sn_like,
            )

    elif model == "M1":
        ndim = 4
        param_names = ["Omega_bc", "h", "100_omega_b", "gamma_u"]
        bounds = [(0.10, 0.50), (0.50, 0.90), (1.80, 2.60), (0.0, gamma_u_max)]

        def prior_transform(u):
            return np.array(
                [
                    0.10 + 0.40 * u[0],
                    0.50 + 0.40 * u[1],
                    1.80 + 0.80 * u[2],
                    gamma_u_max * u[3],
                ],
                dtype=float,
            )

        def chi2_fn(theta):
            return h2h.joint_chi2_law1_reading(
                float(theta[0]),
                float(theta[1]),
                float(theta[2]),
                float(theta[3]),
                reading,
                bao_like,
                cmb_like,
                sn_like,
            )

    elif model == "M2":
        ndim = 3
        param_names = ["Omega_bc", "h", "gamma_u"]
        bounds = [(0.10, 0.50), (0.50, 0.90), (0.0, gamma_u_max)]

        def prior_transform(u):
            return np.array(
                [
                    0.10 + 0.40 * u[0],
                    0.50 + 0.40 * u[1],
                    gamma_u_max * u[2],
                ],
                dtype=float,
            )

        def chi2_fn(theta):
            h_val = float(theta[1])
            wb100_val = 100.0 * (h_val * h_val) / 19.0
            return h2h.joint_chi2_law1_reading(
                float(theta[0]),
                h_val,
                wb100_val,
                float(theta[2]),
                reading,
                bao_like,
                cmb_like,
                sn_like,
            )

    else:
        raise ValueError(f"Unknown model: {model}")

    def loglike(theta):
        c2 = chi2_fn(theta)
        if not np.isfinite(c2):
            return -1e30
        return -0.5 * c2

    t0 = time.perf_counter()
    started_at = time.strftime("%Y-%m-%dT%H:%M:%S")
    rng = np.random.default_rng(seed)
    sampler = dynesty.NestedSampler(
        loglike,
        prior_transform,
        ndim=ndim,
        nlive=NLIVE,
        bound="multi",
        sample="rwalk",
        rstate=rng,
    )
    sampler.run_nested(dlogz=DLOGZ, print_progress=False)
    elapsed_s = time.perf_counter() - t0
    completed_at = time.strftime("%Y-%m-%dT%H:%M:%S")

    res = sampler.results
    weights = np.exp(res.logwt - res.logz[-1])
    weights /= np.sum(weights)

    best_idx = int(np.argmax(res.logl))
    chi2_min_ns = float(-2.0 * res.logl[best_idx])
    best_theta_ns = np.array(res.samples[best_idx], dtype=float)

    # Polish best-fit chi2 starting from best nested-sampling sample
    def obj_opt(x):
        for val, (lo, hi) in zip(x, bounds):
            if val < lo or val > hi:
                return 1e12
        c2 = chi2_fn(x)
        return c2 if np.isfinite(c2) else 1e12

    opt1 = optimize.minimize(
        obj_opt, best_theta_ns, method="Nelder-Mead", options={"xatol": 1e-6, "fatol": 1e-7, "maxiter": 3000}
    )
    opt2 = optimize.minimize(obj_opt, opt1.x, method="L-BFGS-B", bounds=bounds, options={"ftol": 1e-12})
    if float(opt2.fun) <= float(opt1.fun):
        chi2_min_opt = float(opt2.fun)
        best_theta_opt = [float(v) for v in opt2.x]
    else:
        chi2_min_opt = float(opt1.fun)
        best_theta_opt = [float(v) for v in opt1.x]
    if chi2_min_ns < chi2_min_opt:
        chi2_min_opt = chi2_min_ns
        best_theta_opt = [float(v) for v in best_theta_ns]

    mean_vec, cov_mat = dyfunc.mean_and_cov(res.samples, weights)
    std_vec = np.sqrt(np.diag(cov_mat))
    param_stats = {}
    for idx_p, pname in enumerate(param_names):
        param_stats[pname] = {
            "mean": float(mean_vec[idx_p]),
            "std": float(std_vec[idx_p]),
            "best_ns": float(best_theta_ns[idx_p]),
            "best_opt": float(best_theta_opt[idx_p]),
        }

    # Derived parameters for M2 (omega_b = h^2 / 19 and 100*omega_b = 100*h^2 / 19)
    if model == "M2":
        h_samps = res.samples[:, 1]
        omega_b_samps = (h_samps ** 2) / 19.0
        wb100_samps = 100.0 * omega_b_samps
        ob_mean = float(np.sum(weights * omega_b_samps))
        ob_std = float(np.sqrt(np.sum(weights * ((omega_b_samps - ob_mean) ** 2))))
        param_stats["omega_b_derived"] = {
            "mean": ob_mean,
            "std": ob_std,
            "best_ns": float((best_theta_ns[1] ** 2) / 19.0),
            "best_opt": float((best_theta_opt[1] ** 2) / 19.0),
        }
        param_stats["100_omega_b_derived"] = {
            "mean": 100.0 * ob_mean,
            "std": 100.0 * ob_std,
            "best_ns": float(100.0 * (best_theta_ns[1] ** 2) / 19.0),
            "best_opt": float(100.0 * (best_theta_opt[1] ** 2) / 19.0),
        }

    # Save chain archive
    np.savez_compressed(
        chain_path,
        samples=res.samples,
        logwt=res.logwt,
        logl=res.logl,
        logz=res.logz,
        logzerr=res.logzerr,
        weights=weights,
        ncall=res.ncall,
        param_names=np.array(param_names),
    )

    out_summary = {
        "task_id": task_id,
        "run_id": run_id,
        "group": task["group"],
        "model": model,
        "sn_name": sn_name,
        "reading": reading,
        "gamma_u_prior": [0.0, gamma_u_max] if model in ("M1", "M2") else None,
        "seed": seed,
        "nlive": NLIVE,
        "dlogz": DLOGZ,
        "ndim": ndim,
        "started_at": started_at,
        "completed_at": completed_at,
        "elapsed_sec": elapsed_s,
        "niter": int(res.niter),
        "ncall": int(np.sum(res.ncall)),
        "lnZ": float(res.logz[-1]),
        "lnZ_err_dynesty": float(res.logzerr[-1]),
        "chi2_min_ns": chi2_min_ns,
        "chi2_min_opt": chi2_min_opt,
        "best_theta_ns": [float(v) for v in best_theta_ns],
        "best_theta_opt": best_theta_opt,
        "parameters": param_stats,
        "chain_file": f"head_to_head/chains/{task_id}.npz",
    }

    with open(log_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out_summary, f, indent=2)

    return out_summary


def _aggregate_seed_group(run_meta: dict, seed_results: list[dict]) -> dict:
    """Combine the 3 seed runs for a given configuration and compute pooled posterior statistics."""
    seed_results = sorted(seed_results, key=lambda x: x["seed"])
    lnz_arr = np.array([r["lnZ"] for r in seed_results], dtype=float)
    lnz_err_arr = np.array([r["lnZ_err_dynesty"] for r in seed_results], dtype=float)

    lnz_mean = float(np.mean(lnz_arr))
    sigma_dyn_rms = float(np.sqrt(np.mean(lnz_err_arr ** 2)))
    sigma_dyn_mean = float(np.mean(lnz_err_arr))
    sigma_scatter_sd = float(np.std(lnz_arr, ddof=1))
    sigma_scatter_rms = float(np.std(lnz_arr, ddof=0))
    lnz_span = float(np.max(lnz_arr) - np.min(lnz_arr))
    sigma_adopted = float(max(sigma_dyn_rms, sigma_scatter_sd))

    chi2_ns_list = [r["chi2_min_ns"] for r in seed_results]
    chi2_opt_list = [r["chi2_min_opt"] for r in seed_results]
    best_ns_idx = int(np.argmin(chi2_ns_list))
    best_opt_idx = int(np.argmin(chi2_opt_list))

    # Pool posterior means and variances across the 3 seeds with equal weight (1/3 each)
    pnames = list(seed_results[0]["parameters"].keys())
    pooled_params = {}
    for pn in pnames:
        means = np.array([r["parameters"][pn]["mean"] for r in seed_results], dtype=float)
        stds = np.array([r["parameters"][pn]["std"] for r in seed_results], dtype=float)
        pooled_mean = float(np.mean(means))
        # Law of total variance across equally weighted seed posteriors
        pooled_var = float(np.mean(stds ** 2 + (means - pooled_mean) ** 2))
        pooled_std = float(np.sqrt(pooled_var))
        pooled_params[pn] = {
            "mean": pooled_mean,
            "std": pooled_std,
            "seed_means": [float(v) for v in means],
            "seed_stds": [float(v) for v in stds],
            "best_ns": float(seed_results[best_ns_idx]["parameters"][pn]["best_ns"]),
            "best_opt": float(seed_results[best_opt_idx]["parameters"][pn]["best_opt"]),
        }

    return {
        **run_meta,
        "lnZ_mean": lnz_mean,
        "lnZ_err_dynesty_rms": sigma_dyn_rms,
        "lnZ_err_dynesty_mean": sigma_dyn_mean,
        "lnZ_scatter_std_ddof1": sigma_scatter_sd,
        "lnZ_scatter_rms_ddof0": sigma_scatter_rms,
        "lnZ_seed_span": lnz_span,
        "lnZ_err_adopted": sigma_adopted,
        "lnZ_per_seed": [float(v) for v in lnz_arr],
        "lnZ_err_dynesty_per_seed": [float(v) for v in lnz_err_arr],
        "chi2_min_ns": float(chi2_ns_list[best_ns_idx]),
        "chi2_min_ns_per_seed": [float(v) for v in chi2_ns_list],
        "chi2_min_opt": float(chi2_opt_list[best_opt_idx]),
        "chi2_min_opt_per_seed": [float(v) for v in chi2_opt_list],
        "total_ncall": int(sum(r["ncall"] for r in seed_results)),
        "total_elapsed_sec": float(sum(r["elapsed_sec"] for r in seed_results)),
        "parameters": pooled_params,
        "seed_runs": seed_results,
    }


def _jeffreys_label(ln_b: float) -> tuple[str, str]:
    """Return (strength_label, favoured_model_direction) on the Jeffreys / Kass-Raftery scale."""
    abs_b = abs(ln_b)
    if abs_b < 1.0:
        strength = "inconclusive"
    elif abs_b < 2.5:
        strength = "weak"
    elif abs_b <= 5.0:
        strength = "moderate"
    else:
        strength = "strong"
    return strength, ("model favoured over LCDM" if ln_b > 0 else "LCDM favoured over model")


def build_run_definitions() -> list[dict]:
    run_defs = []
    # 16 main runs: 4 models x 2 SN compilations x 2 r_s readings
    for sn_name in ["Pantheon+", "DES-Dovekie"]:
        sn_tag = "PantheonPlus" if sn_name == "Pantheon+" else "DES_Dovekie"
        for reading in ["A", "B"]:
            for model in ["LCDM", "CPL", "M1", "M2"]:
                run_id = f"main__{sn_tag}__reading_{reading}__{model}"
                run_defs.append(
                    {
                        "run_id": run_id,
                        "group": "main",
                        "model": model,
                        "model_label": model,
                        "sn_name": sn_name,
                        "sn_tag": sn_tag,
                        "reading": reading,
                        "gamma_u_max": 2.0 if model in ("M1", "M2") else None,
                    }
                )
    # 8 prior-sensitivity runs: 2 models (M1, M2 with gamma_u in [0, 0.5]) x 2 SN compilations x 2 r_s readings
    for sn_name in ["Pantheon+", "DES-Dovekie"]:
        sn_tag = "PantheonPlus" if sn_name == "Pantheon+" else "DES_Dovekie"
        for reading in ["A", "B"]:
            for model in ["M1", "M2"]:
                run_id = f"sens__{sn_tag}__reading_{reading}__{model}_gamma0p5"
                run_defs.append(
                    {
                        "run_id": run_id,
                        "group": "prior_sensitivity",
                        "model": model,
                        "model_label": f"{model}_narrow",
                        "sn_name": sn_name,
                        "sn_tag": sn_tag,
                        "reading": reading,
                        "gamma_u_max": 0.5,
                    }
                )
    return run_defs


def main():
    data_dir = os.path.join(ROOT_DIR, "data")
    run_defs = build_run_definitions()
    tasks = []
    for rd in run_defs:
        for seed in SEEDS:
            tasks.append(
                {
                    **rd,
                    "seed": seed,
                    "task_id": f"{rd['run_id']}__seed_{seed}",
                }
            )

    model_priority = {"CPL": 0, "M1": 1, "M2": 2, "LCDM": 3}
    sn_priority = {"DES-Dovekie": 0, "Pantheon+": 1}
    tasks.sort(key=lambda t: (model_priority.get(t["model"], 9), sn_priority.get(t["sn_name"], 9), t["reading"], t["seed"]))

    print(f"Launching {len(tasks)} nested-sampling tasks ({len(run_defs)} runs x {len(SEEDS)} seeds) across {N_CORES} workers...")
    t_start = time.perf_counter()

    completed_tasks = []
    with mp.Pool(processes=N_CORES, initializer=_init_worker, initargs=(data_dir,)) as pool:
        for idx, res_summary in enumerate(pool.imap_unordered(_run_single_seed_task, tasks), 1):
            completed_tasks.append(res_summary)
            print(
                f"[{idx:02d}/{len(tasks):02d}] {res_summary['task_id']}: "
                f"lnZ = {res_summary['lnZ']:.4f} +- {res_summary['lnZ_err_dynesty']:.4f}, "
                f"chi2_ns = {res_summary['chi2_min_ns']:.4f}, chi2_opt = {res_summary['chi2_min_opt']:.4f} "
                f"({res_summary['elapsed_sec']:.1f}s)"
            )
            sys.stdout.flush()

    total_wall_s = time.perf_counter() - t_start
    print(f"Completed all {len(tasks)} nested-sampling tasks in {total_wall_s:.1f}s wall-clock time.")

    # Group by run_id
    by_run_id = {}
    for t_res in completed_tasks:
        by_run_id.setdefault(t_res["run_id"], []).append(t_res)

    aggregated_runs = {}
    for rd in run_defs:
        rid = rd["run_id"]
        aggregated_runs[rid] = _aggregate_seed_group(rd, by_run_id[rid])

    # Compute Bayes factors and Delta_chi2 relative to LCDM within each (sn_tag, reading) cell
    comparisons = {}
    for sn_name in ["Pantheon+", "DES-Dovekie"]:
        sn_tag = "PantheonPlus" if sn_name == "Pantheon+" else "DES_Dovekie"
        comparisons[sn_tag] = {}
        for reading in ["A", "B"]:
            lcdm_id = f"main__{sn_tag}__reading_{reading}__LCDM"
            lcdm_agg = aggregated_runs[lcdm_id]
            lnz_lcdm = lcdm_agg["lnZ_mean"]
            err_lcdm = lcdm_agg["lnZ_err_adopted"]
            chi2_ns_lcdm = lcdm_agg["chi2_min_ns"]
            chi2_opt_lcdm = lcdm_agg["chi2_min_opt"]

            cell_models = {}
            for model in ["LCDM", "CPL", "M1", "M2"]:
                mid = f"main__{sn_tag}__reading_{reading}__{model}"
                m_agg = aggregated_runs[mid]
                if model == "LCDM":
                    ln_b = 0.0
                    ln_b_err = 0.0
                    strength = "baseline"
                    direction = "baseline (LCDM)"
                else:
                    ln_b = float(m_agg["lnZ_mean"] - lnz_lcdm)
                    ln_b_err = float(math.sqrt(m_agg["lnZ_err_adopted"] ** 2 + err_lcdm ** 2))
                    strength, direction = _jeffreys_label(ln_b)

                m_agg["lnB_vs_LCDM"] = ln_b
                m_agg["lnB_err_vs_LCDM"] = ln_b_err
                m_agg["delta_chi2_ns_vs_LCDM"] = float(m_agg["chi2_min_ns"] - chi2_ns_lcdm)
                m_agg["delta_chi2_opt_vs_LCDM"] = float(m_agg["chi2_min_opt"] - chi2_opt_lcdm)
                m_agg["jeffreys_strength"] = strength
                m_agg["jeffreys_direction"] = direction
                cell_models[model] = m_agg

            sens_models = {}
            for model in ["M1", "M2"]:
                sid = f"sens__{sn_tag}__reading_{reading}__{model}_gamma0p5"
                s_agg = aggregated_runs[sid]
                ln_b = float(s_agg["lnZ_mean"] - lnz_lcdm)
                ln_b_err = float(math.sqrt(s_agg["lnZ_err_adopted"] ** 2 + err_lcdm ** 2))
                strength, direction = _jeffreys_label(ln_b)
                s_agg["lnB_vs_LCDM"] = ln_b
                s_agg["lnB_err_vs_LCDM"] = ln_b_err
                s_agg["delta_chi2_ns_vs_LCDM"] = float(s_agg["chi2_min_ns"] - chi2_ns_lcdm)
                s_agg["delta_chi2_opt_vs_LCDM"] = float(s_agg["chi2_min_opt"] - chi2_opt_lcdm)
                s_agg["jeffreys_strength"] = strength
                s_agg["jeffreys_direction"] = direction
                sens_models[f"{model}_gamma0p5"] = s_agg

            comparisons[sn_tag][f"Reading_{reading}"] = {
                "sn_compilation": sn_name,
                "reading": reading,
                "main_models": cell_models,
                "prior_sensitivity_models": sens_models,
            }

    val_path = os.path.join(H2H_DIR, "validation_h2h.json")
    validation_data = None
    if os.path.exists(val_path):
        with open(val_path, "r", encoding="utf-8") as f:
            validation_data = json.load(f)

    master_out = {
        "label": "supplementary analysis, not pre-registered",
        "scope": "Background expansion only (DESI DR2 BAO with joint Lya + Chen, Huang & Wang 2019 compressed CMB + Pantheon+ or DES-Dovekie SNe). Does not change any registered Stage 2 verdict; the T5-A rotation-curve failure and MODEL FALSIFIED (FAIL) verdict stand.",
        "completed_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "wall_clock_sec": total_wall_s,
        "environment": {
            "python": sys.version,
            "numpy": np.__version__,
            "scipy": sys.modules["scipy"].__version__,
            "dynesty": dynesty.__version__,
            "psutil": psutil.__version__,
            "n_cores": N_CORES,
            "nlive": NLIVE,
            "dlogz": DLOGZ,
            "bound": "multi",
            "sample": "rwalk",
            "seeds": SEEDS,
            "cpl_prior_polygon_area": 15.5,
            "cpl_unrenormalized_box_shift_ln_15p5_over_20": float(math.log(15.5 / 20.0)),
        },
        "validation": validation_data,
        "comparisons": comparisons,
        "runs": aggregated_runs,
    }

    results_path = os.path.join(H2H_DIR, "results.json")
    with open(results_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(master_out, f, indent=2)
    print(f"Saved complete head-to-head results to {results_path}")


if __name__ == "__main__":
    main()
