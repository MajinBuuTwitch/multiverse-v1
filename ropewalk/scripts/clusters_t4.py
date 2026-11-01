import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import csv
import json
import math
from pathlib import Path
import numpy as np
from scipy.stats import binom, norm, t as student_t


def compute_sigma_diff(sigma_I: float, sigma_S: float, sigma_G: float) -> float:
    """
    [Model Ansatz / Registered Protocol]
    Registered uncertainty propagation for T4b classification (PREREG.md Sec 5.5 line 236):
        sigma_diff = sqrt(sigma_I^2 + sigma_G^2 + sigma_S^2)
    """
    return float(math.sqrt(sigma_I**2 + sigma_G**2 + sigma_S**2))


def classify_subcluster(d_IS: float, d_IG: float, sigma_diff: float) -> str:
    """
    [Model Ansatz / Registered Protocol]
    Classify a subcluster based on projected offsets (d_IS, d_IG) and sigma_diff (PREREG.md Sec 5.5):
      - "with_galaxies" if d_IG - d_IS > 2 * sigma_diff
      - "with_gas"      if d_IS - d_IG > 2 * sigma_diff
      - "unclassified"  if |d_IG - d_IS| <= 2 * sigma_diff
    """
    threshold = 2.0 * sigma_diff
    if d_IG - d_IS > threshold:
        return "with_galaxies"
    elif d_IS - d_IG > threshold:
        return "with_gas"
    else:
        return "unclassified"


def load_mergers_csv(csv_path: str | Path) -> list[dict]:
    """Load the 16-cluster T4b catalog from data/MERGERS.csv."""
    rows = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sigma_I = float(row["sigma_I_kpc"])
            sigma_S = float(row["sigma_S_kpc"])
            sigma_G = float(row["sigma_G_kpc"])
            d_IS = float(row["d_IS_kpc"])
            d_IG = float(row["d_IG_kpc"])
            sigma_diff = compute_sigma_diff(sigma_I, sigma_S, sigma_G)
            computed_class = classify_subcluster(d_IS, d_IG, sigma_diff)

            sec_d_IS = float(row["sec_d_IS_kpc"])
            sec_d_IG = float(row["sec_d_IG_kpc"])
            sec_sigma_diff = float(row["sec_sigma_diff_kpc"])
            sec_computed_class = classify_subcluster(sec_d_IS, sec_d_IG, sec_sigma_diff)

            rows.append({
                "cluster_id": int(row["cluster_id"]),
                "cluster_name": row["cluster_name"],
                "common_name": row["common_name"],
                "split": row["split"],
                "redshift": float(row["redshift"]),
                "primary_subcluster": row["primary_subcluster"],
                "t_p_gyr": float(row["t_p_gyr"]),
                "sigma_t_p_gyr": float(row["sigma_t_p_gyr"]),
                "d_IS_kpc": d_IS,
                "d_IG_kpc": d_IG,
                "sigma_I_kpc": sigma_I,
                "sigma_S_kpc": sigma_S,
                "sigma_G_kpc": sigma_G,
                "sigma_diff_kpc": round(sigma_diff, 4),
                "primary_class": computed_class,
                "csv_primary_class": row["primary_class"],
                "secondary_subcluster": row["secondary_subcluster"],
                "sec_d_IS_kpc": sec_d_IS,
                "sec_d_IG_kpc": sec_d_IG,
                "sec_sigma_diff_kpc": sec_sigma_diff,
                "secondary_class": sec_computed_class,
                "source_citation": row["source_citation"],
            })
    return rows


def fit_tau_lag_hard_step(
    train_clusters: list[dict],
    tau_min_myr: int = 235,
    tau_max_myr: int = 1500,
    step_myr: int = 5,
    class_key: str = "primary_class",
) -> dict:
    """
    [Model Ansatz / Registered Protocol]
    Fit tau_lag on the training half (Odd positions #1,3,...,15) over the uniform grid
    [tau_min_myr, tau_max_myr] in steps of step_myr = 5 Myr (PREREG.md Sec 5.5 line 206).
    Prediction rule (line 207):
      - "with_galaxies" for t_{p,i} < tau_lag
      - "with_gas"      for t_{p,i} >= tau_lag
    Tie-breaking rule: choose the smallest tau_lag on the grid achieving max Acc_train.
    """
    classified = [c for c in train_clusters if c[class_key] in ("with_galaxies", "with_gas")]
    n_train = len(classified)
    if n_train == 0:
        return {
            "tau_lag_myr": int(tau_min_myr),
            "tau_lag_gyr": round(tau_min_myr / 1000.0, 6),
            "train_acc": 0.0,
            "n_train_classified": 0,
            "n_train_correct": 0,
        }

    best_acc = -1.0
    best_tau_myr = tau_min_myr
    best_correct = 0

    for tau_myr in range(tau_min_myr, tau_max_myr + 1, step_myr):
        tau_gyr = tau_myr / 1000.0
        correct = 0
        for c in classified:
            pred = "with_galaxies" if c["t_p_gyr"] < tau_gyr else "with_gas"
            if pred == c[class_key]:
                correct += 1
        acc = correct / n_train
        # Strictly '>' preserves the smallest tau_lag under tie-breaking
        if acc > best_acc:
            best_acc = acc
            best_tau_myr = tau_myr
            best_correct = correct

    return {
        "tau_lag_myr": int(best_tau_myr),
        "tau_lag_gyr": round(best_tau_myr / 1000.0, 6),
        "train_acc": float(best_acc),
        "n_train_classified": int(n_train),
        "n_train_correct": int(best_correct),
    }


def evaluate_t4b_test_half(
    all_clusters: list[dict],
    train_fit: dict,
    class_key: str = "primary_class",
) -> dict:
    """
    [Model Ansatz / Registered Protocol]
    Evaluate frozen tau_lag_gyr on the held-out test half (Even positions #2,4,...,16)
    and check the priority-ordered exhaustive deciding thresholds in PREREG.md Sec 5.5 (lines 240-247).
    """
    tau_lag_gyr = train_fit["tau_lag_gyr"]
    n_train = train_fit["n_train_classified"]
    train_acc = train_fit["train_acc"]

    n_total = len(all_clusters)
    n_unclassified_total = sum(1 for c in all_clusters if c[class_key] == "unclassified")

    test_clusters = [c for c in all_clusters if c["split"] == "test"]
    classified_test = [c for c in test_clusters if c[class_key] in ("with_galaxies", "with_gas")]
    n_test = len(classified_test)

    k_correct = 0
    n_young_test = 0
    n_old_test = 0
    n_gal_test = 0
    n_gas_test = 0
    n_gas_old_branch_test = 0
    has_old_1gyr_test = False

    per_cluster_results = []
    for c in test_clusters:
        obs_class = c[class_key]
        is_young = c["t_p_gyr"] < tau_lag_gyr
        pred_class = "with_galaxies" if is_young else "with_gas"
        if obs_class in ("with_galaxies", "with_gas"):
            if c["t_p_gyr"] >= 1.0:
                has_old_1gyr_test = True
            if is_young:
                n_young_test += 1
            else:
                n_old_test += 1
            if obs_class == "with_galaxies":
                n_gal_test += 1
            else:
                n_gas_test += 1
                if not is_young:
                    n_gas_old_branch_test += 1
            is_correct = (pred_class == obs_class)
            if is_correct:
                k_correct += 1
        else:
            is_correct = None

        per_cluster_results.append({
            "cluster_id": c["cluster_id"],
            "cluster_name": c["cluster_name"],
            "t_p_gyr": c["t_p_gyr"],
            "observed_class": obs_class,
            "predicted_class": pred_class,
            "correct": is_correct,
        })

    classified_all = [c for c in all_clusters if c[class_key] in ("with_galaxies", "with_gas")]
    n_gas_old_branch_all = sum(
        1 for c in classified_all
        if (c["t_p_gyr"] >= tau_lag_gyr and c[class_key] == "with_gas")
    )

    test_acc = (k_correct / n_test) if n_test > 0 else 0.0
    p_binom_raw = float(binom.sf(k_correct - 1, n_test, 0.5)) if n_test > 0 else 1.0
    # Per PREREG.md Sec 3.2 (line 81): if n_test < 6, discovery p-value in Holm sort is mechanically set to 1.0
    p_holm = p_binom_raw if n_test >= 6 else 1.0

    # Strict priority order from PREREG.md lines 242-247:
    # 1. FAIL (evaluated first; takes precedence):
    fail_reasons = []
    if n_train == 0 or train_acc < 0.80:
        fail_reasons.append(f"Clause 1(a): n_train={n_train} or max Acc_train={train_acc:.4f} < 0.80.")
    if n_test >= 6 and test_acc < 0.60:
        fail_reasons.append(f"Clause 1(b): n_test={n_test} >= 6 and Acc_test={test_acc:.4f} < 0.60.")
    if n_test >= 6 and n_gal_test == n_test and has_old_1gyr_test:
        fail_reasons.append(
            f"Clause 1(c): n_test={n_test} >= 6 and all {n_test} classified test systems "
            f"(including t_p >= 1.0 Gyr) are classified 'with_galaxies'."
        )

    inconclusive_reasons = []
    if len(fail_reasons) > 0:
        verdict = "FAIL"
    elif n_test >= 6 and test_acc >= 0.80 and p_binom_raw <= 0.05:
        verdict = "PASS"
    else:
        verdict = "INCONCLUSIVE"
        if n_test < 6:
            inconclusive_reasons.append(
                f"Rule G8(3) & Sec 5.5(3): n_test = {n_test} < 6 classified test clusters "
                f"(3 of 8 even-index test clusters are unclassified under the 2*sigma_diff rule)."
            )
        elif test_acc < 0.80:
            inconclusive_reasons.append(
                f"Sec 5.5(3): 0.60 <= Acc_test = {test_acc:.4f} < 0.80."
            )
        else:
            inconclusive_reasons.append(
                f"Sec 5.5(3): p_T4b = {p_binom_raw:.6f} > 0.05."
            )

    return {
        "tau_lag_gyr": tau_lag_gyr,
        "n_total": n_total,
        "n_unclassified_total": n_unclassified_total,
        "n_train_classified": n_train,
        "train_acc": round(train_acc, 8),
        "n_test_classified": n_test,
        "k_test_correct": k_correct,
        "test_acc": round(test_acc, 8),
        "p_T4b_raw": round(p_binom_raw, 10),
        "p_T4b_holm": round(p_holm, 10),
        "n_young_test": n_young_test,
        "n_old_test": n_old_test,
        "n_gal_test": n_gal_test,
        "n_gas_test": n_gas_test,
        "n_gas_old_branch_test": n_gas_old_branch_test,
        "n_gas_old_branch_all": n_gas_old_branch_all,
        "verdict": verdict,
        "fail_reasons": fail_reasons,
        "inconclusive_reasons": inconclusive_reasons,
        "per_cluster_test": per_cluster_results,
    }


def truncated_normal_prob_young(t_hat: float, sigma_t: float, tau_lag: float) -> float:
    """
    Probability P(t_p < tau_lag) for t_p ~ N(t_hat, sigma_t^2) truncated at t_p > 0.
    """
    if sigma_t <= 0.0:
        return 1.0 if t_hat < tau_lag else 0.0
    cdf_zero = norm.cdf(0.0, loc=t_hat, scale=sigma_t)
    denom = max(1.0 - cdf_zero, 1e-15)
    cdf_tau = norm.cdf(max(tau_lag, 0.0), loc=t_hat, scale=sigma_t)
    return float(np.clip((cdf_tau - cdf_zero) / denom, 0.0, 1.0))


def run_posterior_weighted_sensitivity(
    all_clusters: list[dict],
    tau_min_myr: int = 235,
    tau_max_myr: int = 1500,
    step_myr: int = 5,
) -> dict:
    """
    [Sensitivity Analysis S2]
    Posterior-weighted accuracy integrating over t_{p,i} ~ N(t_hat_i, sigma_{t_p,i}^2) truncated at t_p > 0.
    """
    train_classified = [
        c for c in all_clusters
        if c["split"] == "train" and c["primary_class"] in ("with_galaxies", "with_gas")
    ]
    test_classified = [
        c for c in all_clusters
        if c["split"] == "test" and c["primary_class"] in ("with_galaxies", "with_gas")
    ]

    best_acc = -1.0
    best_tau_myr = tau_min_myr
    for tau_myr in range(tau_min_myr, tau_max_myr + 1, step_myr):
        tau_gyr = tau_myr / 1000.0
        scores = []
        for c in train_classified:
            p_young = truncated_normal_prob_young(c["t_p_gyr"], c["sigma_t_p_gyr"], tau_gyr)
            score = p_young if c["primary_class"] == "with_galaxies" else (1.0 - p_young)
            scores.append(score)
        acc = float(np.mean(scores))
        if acc > best_acc + 1e-12:
            best_acc = acc
            best_tau_myr = tau_myr

    frozen_tau_gyr = best_tau_myr / 1000.0
    test_scores = []
    for c in test_classified:
        p_young = truncated_normal_prob_young(c["t_p_gyr"], c["sigma_t_p_gyr"], frozen_tau_gyr)
        score = p_young if c["primary_class"] == "with_galaxies" else (1.0 - p_young)
        test_scores.append(score)

    return {
        "tau_lag_myr": int(best_tau_myr),
        "tau_lag_gyr": round(frozen_tau_gyr, 6),
        "train_posterior_acc": round(best_acc, 6),
        "test_posterior_acc": round(float(np.mean(test_scores)), 6),
    }


def run_t4a_exploratory() -> dict:
    """
    [Exploratory Unscored Analysis T4a - PREREG.md Sec 5.4]
    Evaluate the Wittman et al. (2018, ApJ 869, 104) Table 1 subcluster sample
    (excluding 1E 0657-558 per Rule G2) for t_p <= 235 Myr, t_p <= 400 Myr, and all non-Bullet systems,
    plus Harvey et al. (2015, Science 347, 1462), under the unified sign convention (Review B2):
      Delta_SI^parallel = (x_I - x_S) . s_hat_{G->S} = -|delta_SG| * beta_W18
    where positive Delta_SI^parallel (beta_W18 < 0) means dark mass sits ahead of the stars (away from gas).
    """
    # Exact rows from Wittman et al. (2018, ApJ, 869, 104; arXiv:1708.07885) Table 1
    # Note: In Wittman+18 Table 1, dx_SI is measured from galaxies toward gas, so
    # Delta_SI^parallel (along s_hat_{G->S}, away from gas) = -dx_SI_W18.
    wittman_table1 = [
        {"subcluster": "A2744 W", "is_bullet": False, "v_col_kms": 1500, "t_col_myr": 500, "dx_SG_kpc": 212.0, "dx_SI_w18_kpc": 100.0, "sigma_SI_kpc": 81.0},
        {"subcluster": "A2744 S", "is_bullet": False, "v_col_kms": 2100, "t_col_myr": 120, "dx_SG_kpc": 152.0, "dx_SI_w18_kpc": 45.0, "sigma_SI_kpc": 52.0},
        {"subcluster": "Bullet W (1E0657)", "is_bullet": True, "v_col_kms": 2900, "t_col_myr": 250, "dx_SG_kpc": 135.0, "dx_SI_w18_kpc": -19.0, "sigma_SI_kpc": 30.0},
        {"subcluster": "MACS J0025 SE", "is_bullet": False, "v_col_kms": 2000, "t_col_myr": 500, "dx_SG_kpc": 255.0, "dx_SI_w18_kpc": -33.0, "sigma_SI_kpc": 61.0},
        {"subcluster": "MACS J0025 NW", "is_bullet": False, "v_col_kms": 2000, "t_col_myr": 500, "dx_SG_kpc": 333.0, "dx_SI_w18_kpc": 47.0, "sigma_SI_kpc": 48.0},
        {"subcluster": "ZWCL 0008 E", "is_bullet": False, "v_col_kms": 1900, "t_col_myr": 760, "dx_SG_kpc": 106.0, "dx_SI_w18_kpc": -155.0, "sigma_SI_kpc": 190.0},
        {"subcluster": "ZWCL 0008 W", "is_bullet": False, "v_col_kms": 1900, "t_col_myr": 760, "dx_SG_kpc": 467.0, "dx_SI_w18_kpc": 168.0, "sigma_SI_kpc": 182.0},
        {"subcluster": "DLSCL J0916 N", "is_bullet": False, "v_col_kms": 1600, "t_col_myr": 1100, "dx_SG_kpc": 511.0, "dx_SI_w18_kpc": 52.0, "sigma_SI_kpc": 151.0},
        {"subcluster": "DLSCL J0916 S", "is_bullet": False, "v_col_kms": 1600, "t_col_myr": 1100, "dx_SG_kpc": 420.0, "dx_SI_w18_kpc": 80.0, "sigma_SI_kpc": 60.0},
        {"subcluster": "CIZA J2242 S", "is_bullet": False, "v_col_kms": 2400, "t_col_myr": 650, "dx_SG_kpc": 329.0, "dx_SI_w18_kpc": 136.0, "sigma_SI_kpc": 100.0},
        {"subcluster": "CIZA J2242 N", "is_bullet": False, "v_col_kms": 2400, "t_col_myr": 650, "dx_SG_kpc": 706.0, "dx_SI_w18_kpc": -71.0, "sigma_SI_kpc": 122.0},
    ]

    for row in wittman_table1:
        beta = row["dx_SI_w18_kpc"] / row["dx_SG_kpc"]
        sigma_beta = row["sigma_SI_kpc"] / row["dx_SG_kpc"]
        row["beta"] = round(beta, 4)
        row["sigma_beta"] = round(sigma_beta, 4)
        # Unified sign convention: Delta_SI^parallel = -|delta_SG| * beta = -dx_SI_w18_kpc
        row["Delta_SI_parallel_kpc"] = round(-row["dx_SI_w18_kpc"], 4)

    def summarize_sample(sample: list[dict], label: str) -> dict:
        if not sample:
            return {"sample_label": label, "n_subclusters": 0}
        deltas = np.array([r["Delta_SI_parallel_kpc"] for r in sample], dtype=float)
        sigmas_d = np.array([r["sigma_SI_kpc"] for r in sample], dtype=float)
        w_d = 1.0 / (sigmas_d**2)
        ivw_delta = float(np.sum(w_d * deltas) / np.sum(w_d))
        ivw_sigma_d = float(math.sqrt(1.0 / np.sum(w_d)))

        betas = np.array([r["beta"] for r in sample], dtype=float)
        sigmas_b = np.array([r["sigma_beta"] for r in sample], dtype=float)
        w_b = 1.0 / (sigmas_b**2)
        ivw_beta = float(np.sum(w_b * betas) / np.sum(w_b))
        ivw_sigma_b = float(math.sqrt(1.0 / np.sum(w_b)))

        return {
            "sample_label": label,
            "n_subclusters": len(sample),
            "ivw_Delta_SI_parallel_kpc": round(ivw_delta, 4),
            "ivw_sigma_Delta_SI_kpc": round(ivw_sigma_d, 4),
            "z_Delta_SI_parallel": round(ivw_delta / ivw_sigma_d, 4),
            "ivw_beta": round(ivw_beta, 4),
            "ivw_sigma_beta": round(ivw_sigma_b, 4),
            "n_positive_Delta_SI_parallel": int(np.sum(deltas > 0)),
        }

    non_bullet = [r for r in wittman_table1 if not r["is_bullet"]]
    non_bullet_235 = [r for r in non_bullet if r["t_col_myr"] <= 235]
    non_bullet_400 = [r for r in non_bullet if r["t_col_myr"] <= 400]

    return {
        "status": "EXPLORATORY_UNSCORED",
        "reason": "Unconditionally locked as exploratory/unscored in PREREG.md Sec 5.4 (Review B3).",
        "non_bullet_t_le_235Myr": summarize_sample(non_bullet_235, "Wittman+18 non-Bullet t_col <= 235 Myr (N=1: A2744 S)"),
        "non_bullet_t_le_400Myr": summarize_sample(non_bullet_400, "Wittman+18 non-Bullet t_col <= 400 Myr (N=1: A2744 S)"),
        "non_bullet_all_10": summarize_sample(non_bullet, "Wittman+18 all 10 non-Bullet subclusters"),
        "wittman_2018_full_11": summarize_sample(wittman_table1, "Wittman+18 full 11 subclusters (including Bullet)"),
        "harvey_2015_72_ensemble": {
            "sample_label": "Harvey+15 (Science 347, 1462) 72-subcluster ensemble",
            "beta": -0.04,
            "sigma_beta": 0.07,
            "z_stat": round(0.04 / 0.07, 4),
        },
        "subclusters": wittman_table1,
    }


def run_all_t4(csv_path: str | Path) -> dict:
    """
    Execute the complete T4b deciding analysis, all registered sensitivity checks,
    and the T4a exploratory analysis.
    """
    clusters = load_mergers_csv(csv_path)
    train_clusters = [c for c in clusters if c["split"] == "train"]

    # 1. Deciding T4b fit & evaluation (tau_lag in [235, 1500] Myr, 5 Myr steps, Odd/Even split)
    fit_deciding = fit_tau_lag_hard_step(train_clusters, tau_min_myr=235, tau_max_myr=1500, step_myr=5)
    eval_deciding = evaluate_t4b_test_half(clusters, fit_deciding)

    # 2. Sensitivity S1: Bullet median floor [400, 1500] Myr
    fit_s1 = fit_tau_lag_hard_step(train_clusters, tau_min_myr=400, tau_max_myr=1500, step_myr=5)
    eval_s1 = evaluate_t4b_test_half(clusters, fit_s1)

    # 3. Sensitivity S2: Posterior-weighted accuracy
    eval_s2 = run_posterior_weighted_sensitivity(clusters, tau_min_myr=235, tau_max_myr=1500, step_myr=5)

    # 4. Sensitivity S3: System-level classification (primary and secondary must agree)
    clusters_s3 = []
    for c in clusters:
        c_copy = dict(c)
        if (
            c["primary_class"] in ("with_galaxies", "with_gas")
            and c["primary_class"] == c["secondary_class"]
        ):
            c_copy["system_class"] = c["primary_class"]
        else:
            c_copy["system_class"] = "unclassified"
        clusters_s3.append(c_copy)
    train_s3 = [c for c in clusters_s3 if c["split"] == "train"]
    fit_s3 = fit_tau_lag_hard_step(train_s3, tau_min_myr=235, tau_max_myr=1500, step_myr=5, class_key="system_class")
    eval_s3 = evaluate_t4b_test_half(clusters_s3, fit_s3, class_key="system_class")

    # 5. Sensitivity S4: Abell 520 P3/P3' dark core variant (Jee+14 Table 1)
    clusters_s4 = []
    for c in clusters:
        c_copy = dict(c)
        if c["cluster_name"] == "Abell 520":
            c_copy["d_IS_kpc"] = 280.0
            c_copy["d_IG_kpc"] = 35.0
            c_copy["sigma_diff_kpc"] = 22.0
            c_copy["primary_class"] = classify_subcluster(280.0, 35.0, 22.0)
        clusters_s4.append(c_copy)
    train_s4 = [c for c in clusters_s4 if c["split"] == "train"]
    fit_s4 = fit_tau_lag_hard_step(train_s4, tau_min_myr=235, tau_max_myr=1500, step_myr=5)
    eval_s4 = evaluate_t4b_test_half(clusters_s4, fit_s4)

    # 6. Sensitivity S5: Abell 520 Clowe+12 Table 2 variant
    clusters_s5 = []
    for c in clusters:
        c_copy = dict(c)
        if c["cluster_name"] == "Abell 520":
            c_copy["d_IS_kpc"] = 22.0
            c_copy["d_IG_kpc"] = 480.0
            c_copy["sigma_diff_kpc"] = 20.0
            c_copy["primary_class"] = classify_subcluster(22.0, 480.0, 20.0)
        clusters_s5.append(c_copy)
    train_s5 = [c for c in clusters_s5 if c["split"] == "train"]
    fit_s5 = fit_tau_lag_hard_step(train_s5, tau_min_myr=235, tau_max_myr=1500, step_myr=5)
    eval_s5 = evaluate_t4b_test_half(clusters_s5, fit_s5)

    # 7. Sensitivity S6: Abell 1758N Ragozzine+12 Table 2 HST WL sensitivity (PREREG.md line 222)
    clusters_s6 = []
    for c in clusters:
        c_copy = dict(c)
        if c["cluster_name"] == "Abell 1758N":
            c_copy["d_IS_kpc"] = 18.0
            c_copy["d_IG_kpc"] = 110.0
            c_copy["sigma_diff_kpc"] = 25.0
            c_copy["primary_class"] = classify_subcluster(18.0, 110.0, 25.0)
        clusters_s6.append(c_copy)
    eval_s6 = evaluate_t4b_test_half(clusters_s6, fit_deciding)

    # 8. Sensitivity S7: First-8 vs Last-8 split (7 classified test systems -> FAIL Clause 1(b) & 1(c))
    clusters_s7 = []
    for c in clusters:
        c_copy = dict(c)
        c_copy["split"] = "train" if c["cluster_id"] <= 8 else "test"
        clusters_s7.append(c_copy)
    train_s7 = [c for c in clusters_s7 if c["split"] == "train"]
    fit_s7 = fit_tau_lag_hard_step(train_s7, tau_min_myr=235, tau_max_myr=1500, step_myr=5)
    eval_s7 = evaluate_t4b_test_half(clusters_s7, fit_s7)

    # 9. Exploratory T4a
    t4a_exploratory = run_t4a_exploratory()

    return {
        "T4b_deciding": {
            "training_fit": fit_deciding,
            "test_evaluation": eval_deciding,
        },
        "T4b_sensitivity": {
            "S1_Bullet_median_400Myr": {
                "training_fit": fit_s1,
                "test_evaluation": eval_s1,
            },
            "S2_posterior_weighted": eval_s2,
            "S3_system_level": {
                "training_fit": fit_s3,
                "test_evaluation": eval_s3,
            },
            "S4_Abell520_P3_dark_core": {
                "training_fit": fit_s4,
                "test_evaluation": eval_s4,
            },
            "S5_Abell520_Clowe12": {
                "training_fit": fit_s5,
                "test_evaluation": eval_s5,
            },
            "S6_Abell1758N_Ragozzine12": {
                "training_fit": fit_deciding,
                "test_evaluation": eval_s6,
            },
            "S7_First8_vs_Last8_split": {
                "training_fit": fit_s7,
                "test_evaluation": eval_s7,
            },
        },
        "T4a_exploratory": t4a_exploratory,
        "catalog": clusters,
    }


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    csv_file = root / "data" / "MERGERS.csv"
    res = run_all_t4(csv_file)
    print(json.dumps(res["T4b_deciding"], indent=2))
