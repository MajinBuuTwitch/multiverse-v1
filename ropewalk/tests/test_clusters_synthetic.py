import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from clusters_t4 import (
    compute_sigma_diff,
    classify_subcluster,
    fit_tau_lag_hard_step,
    evaluate_t4b_test_half,
    truncated_normal_prob_young,
)


def test_sigma_diff_and_classification():
    # sigma_I = 30, sigma_S = 20, sigma_G = 20 -> sigma_diff = sqrt(900 + 400 + 400) = sqrt(1700)
    s_diff = compute_sigma_diff(30.0, 20.0, 20.0)
    assert abs(s_diff - 1700.0**0.5) < 1e-9

    # 2 * sigma_diff = 82.462
    assert classify_subcluster(10.0, 100.0, s_diff) == "with_galaxies"
    assert classify_subcluster(100.0, 10.0, s_diff) == "with_gas"
    assert classify_subcluster(50.0, 100.0, s_diff) == "unclassified"


def test_synthetic_two_regime_pass_and_null_fail():
    # Synthetic training half: 4 young with_galaxies (t_p = 0.2, 0.3, 0.4, 0.5 Gyr)
    # and 4 old with_gas (t_p = 0.7, 0.8, 0.9, 1.0 Gyr)
    train_synth = [
        {"cluster_id": i + 1, "cluster_name": f"Train_{i+1}", "split": "train", "t_p_gyr": tp, "primary_class": cls}
        for i, (tp, cls) in enumerate([
            (0.20, "with_galaxies"),
            (0.30, "with_galaxies"),
            (0.40, "with_galaxies"),
            (0.50, "with_galaxies"),
            (0.70, "with_gas"),
            (0.80, "with_gas"),
            (0.90, "with_gas"),
            (1.00, "with_gas"),
        ])
    ]
    fit = fit_tau_lag_hard_step(train_synth, tau_min_myr=235, tau_max_myr=1500, step_myr=5)
    # Smallest tau_lag on 5 Myr grid [235, 1500] with t_p = 0.50 < tau_lag <= 0.70 is 505 Myr
    assert fit["tau_lag_myr"] == 505
    assert abs(fit["train_acc"] - 1.0) < 1e-12

    # Synthetic test half that PASSES (8/8 correct: 4 young with_galaxies, 4 old with_gas)
    test_pass = [
        {"cluster_id": i + 9, "cluster_name": f"Test_{i+1}", "split": "test", "t_p_gyr": tp, "primary_class": cls}
        for i, (tp, cls) in enumerate([
            (0.25, "with_galaxies"),
            (0.35, "with_galaxies"),
            (0.40, "with_galaxies"),
            (0.45, "with_galaxies"),
            (0.65, "with_gas"),
            (0.85, "with_gas"),
            (1.10, "with_gas"),
            (1.30, "with_gas"),
        ])
    ]
    eval_pass = evaluate_t4b_test_half(train_synth + test_pass, fit)
    assert eval_pass["verdict"] == "PASS"
    assert eval_pass["k_test_correct"] == 8
    assert abs(eval_pass["p_T4b_raw"] - (0.5**8)) < 1e-12

    # Synthetic test half where all clusters stay with_galaxies (single-regime null -> FAIL)
    test_fail = [
        {"cluster_id": i + 9, "cluster_name": f"Test_{i+1}", "split": "test", "t_p_gyr": tp, "primary_class": "with_galaxies"}
        for i, tp in enumerate([0.25, 0.35, 0.40, 0.45, 0.65, 0.85, 1.10, 1.30])
    ]
    eval_fail = evaluate_t4b_test_half(train_synth + test_fail, fit)
    assert eval_fail["verdict"] == "FAIL"
    assert eval_fail["n_gas_old_branch_test"] == 0


def test_truncated_normal_prob():
    p = truncated_normal_prob_young(0.5, 0.1, 0.5)
    assert abs(p - 0.5) < 1e-5


if __name__ == "__main__":
    test_sigma_diff_and_classification()
    test_synthetic_two_regime_pass_and_null_fail()
    test_truncated_normal_prob()
    print("ALL SYNTHETIC CLUSTER TESTS PASSED.")
