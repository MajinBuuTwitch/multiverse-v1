import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from sparc_t5 import (
    kernel_f_sigma,
    parse_sparc_catalog,
    predict_galaxy_rotation_curve,
    evaluate_t5c_df2,
)
from local_h0_t6 import (
    healpix_nside1_ring,
    assign_and_merge_pixels,
    compute_coincidence_window,
)


def test_kernel_f_sigma_against_3d_monte_carlo():
    # Direct 3D Monte Carlo check of a thin shell of radius r_prime = 4.0 kpc
    # smeared by 3D isotropic Gaussian of width sigma_ref = 2.5 kpc, evaluated at r = 5.0 kpc
    rng = np.random.default_rng(20261030)
    r_prime = 4.0
    sigma = 2.5
    r_eval = 5.0
    n_mc = 500_000

    dx = rng.normal(0.0, sigma, size=n_mc)
    dy = rng.normal(0.0, sigma, size=n_mc)
    dz = rng.normal(r_prime, sigma, size=n_mc)
    r_mc = np.sqrt(dx * dx + dy * dy + dz * dz)
    mc_frac = float(np.mean(r_mc <= r_eval))

    analytic_frac = float(kernel_f_sigma(np.array([[r_eval]]), np.array([[r_prime]]), sigma)[0, 0])
    assert abs(mc_frac - analytic_frac) < 2.0e-3, f"MC={mc_frac}, analytic={analytic_frac}"

    # Also test point-mass branch (r' = 0)
    dx0 = rng.normal(0.0, sigma, size=n_mc)
    dy0 = rng.normal(0.0, sigma, size=n_mc)
    dz0 = rng.normal(0.0, sigma, size=n_mc)
    r0_mc = np.sqrt(dx0 * dx0 + dy0 * dy0 + dz0 * dz0)
    mc0_frac = float(np.mean(r0_mc <= r_eval))
    analytic0_frac = float(kernel_f_sigma(np.array([[r_eval]]), np.array([[0.0]]), sigma)[0, 0])
    assert abs(mc0_frac - analytic0_frac) < 2.0e-3, f"MC0={mc0_frac}, analytic0={analytic0_frac}"


def test_sparc_catalog_parse_and_split():
    sparc_dir = ROOT / "data" / "sparc"
    galaxies = parse_sparc_catalog(sparc_dir)
    assert len(galaxies) == 175, f"Expected 175 SPARC galaxies, got {len(galaxies)}"
    train = [g for g in galaxies if g["split"] == "train"]
    test = [g for g in galaxies if g["split"] == "test"]
    assert len(train) == 88, f"Expected 88 training galaxies, got {len(train)}"
    assert len(test) == 87, f"Expected 87 test galaxies, got {len(test)}"

    v_pred = predict_galaxy_rotation_curve(train[0], 5.0, 1.0 / 6.0)
    assert len(v_pred) == train[0]["n_pts"]
    assert np.all(np.isfinite(v_pred))
    assert np.all(v_pred >= 0.0)

    # Check T5c DF2 threshold boundaries from PREREG.md lines 289-290
    df2_wide = evaluate_t5c_df2(sigma_ref_kpc=5.0, f_leak=1.0 / 6.0)
    assert df2_wide["verdict"] == "PASS"
    df2_narrow = evaluate_t5c_df2(sigma_ref_kpc=1.0, f_leak=1.0 / 6.0)
    assert df2_narrow["verdict"] == "FAIL"


def test_healpix_and_coincidence_window():
    # Test HEALPix N_side=1 RING pixel centers:
    # North cap (z = 5/6 -> theta = arccos(5/6)), phi = pi/4, 3pi/4, 5pi/4, 7pi/4 -> pixels 0, 1, 2, 3
    theta_n = np.full(4, np.arccos(5.0 / 6.0))
    phi_n = np.array([0.25, 0.75, 1.25, 1.75]) * np.pi
    assert list(healpix_nside1_ring(theta_n, phi_n)) == [0, 1, 2, 3]

    # Equatorial belt (z = 0 -> theta = pi/2), phi = 0, pi/2, pi, 3pi/2 -> pixels 4, 5, 6, 7
    theta_eq = np.full(4, 0.5 * np.pi)
    phi_eq = np.array([0.0, 0.5, 1.0, 1.5]) * np.pi
    assert list(healpix_nside1_ring(theta_eq, phi_eq)) == [4, 5, 6, 7]

    # South cap (z = -5/6 -> theta = arccos(-5/6)), phi = pi/4, 3pi/4, 5pi/4, 7pi/4 -> pixels 8, 9, 10, 11
    theta_s = np.full(4, np.arccos(-5.0 / 6.0))
    assert list(healpix_nside1_ring(theta_s, phi_n)) == [8, 9, 10, 11]

    # Test sparse pixel merge rule: pixel 4 with 5 SNe merges into pixel 0 (which has 12 SNe -> 17 SNe)
    raw = np.array([0] * 12 + [4] * 5 + [1] * 15)
    merged, retained, info = assign_and_merge_pixels(raw, apply_merge=True)
    assert retained == [0, 1]
    assert info["post_merge_counts"][0] == 17

    # Test coincidence window computation
    cw = compute_coincidence_window(1.0 / 6.0)
    assert cw["t0_cosmic_age_gyr"] > 13.0
    assert cw["f_leak_1_over_6"]["Criterion_H_Abs_5pct"]["delta_t_gyr"] > 0.0


if __name__ == "__main__":
    test_kernel_f_sigma_against_3d_monte_carlo()
    test_sparc_catalog_parse_and_split()
    test_healpix_and_coincidence_window()
    print("ALL SYNTHETIC SPARC AND T6 TESTS PASSED.")
