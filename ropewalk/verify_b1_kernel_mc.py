import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import math
import numpy as np
from scipy.special import erf
from scipy.stats import ncx2

SEED = 20261030


def F_sigma_corrected(r: float, rp: float, sig: float) -> float:
    """Exact 1D radial enclosed-mass kernel with corrected 1/sqrt(2*pi) prefactor."""
    if rp / sig < 1e-4:
        u = r / (math.sqrt(2.0) * sig)
        return math.erf(u) - math.sqrt(2.0 / math.pi) * (r / sig) * math.exp(-u * u)
    a = (r + rp) / (math.sqrt(2.0) * sig)
    b = (r - rp) / (math.sqrt(2.0) * sig)
    term1 = 0.5 * (erf(a) + erf(b))
    term2 = (1.0 / math.sqrt(2.0 * math.pi)) * (sig / rp) * (
        math.exp(-b * b) - math.exp(-a * a)
    )
    return float(term1 - term2)


def F_sigma_old_buggy(r: float, rp: float, sig: float) -> float:
    """Old v1 formula with buggy sqrt(2/pi) prefactor."""
    a = (r + rp) / (math.sqrt(2.0) * sig)
    b = (r - rp) / (math.sqrt(2.0) * sig)
    term1 = 0.5 * (erf(a) + erf(b))
    term2 = math.sqrt(2.0 / math.pi) * (sig / rp) * (
        math.exp(-b * b) - math.exp(-a * a)
    )
    return float(term1 - term2)


def main() -> None:
    rng = np.random.default_rng(SEED)
    n_samples = 500_000
    test_points = [
        (1.0, 1.0, 1.0),
        (2.0, 1.0, 1.5),
        (0.5, 2.0, 1.0),
        (3.0, 0.5, 2.0),
    ]
    print("=== B1 Kernel Monte Carlo & ncx2.cdf Verification ===")
    for r, rp, sig in test_points:
        z = rng.standard_normal((n_samples, 3)) * sig
        z[:, 2] += rp
        dist = np.linalg.norm(z, axis=1)
        inside = (dist <= r).astype(float)
        mc_mean = float(np.mean(inside))
        mc_se = float(np.std(inside, ddof=1) / math.sqrt(n_samples))
        exact = F_sigma_corrected(r, rp, sig)
        ncx2_val = float(ncx2.cdf((r / sig) ** 2, df=3, nc=(rp / sig) ** 2))
        old_val = F_sigma_old_buggy(r, rp, sig)
        z_diff = (mc_mean - exact) / mc_se
        print(
            f"(r={r:.1f}, rp={rp:.1f}, sig={sig:.1f}): "
            f"exact={exact:.6f}, ncx2={ncx2_val:.6f} (|diff|={abs(exact-ncx2_val):.2e}), "
            f"MC={mc_mean:.6f} +/- {mc_se:.6f} ({z_diff:+.2f} SE), "
            f"old_buggy={old_val:+.6f}"
        )

    # Gate G9-d 5x5 grid check
    grid = [0.2, 0.5, 1.0, 2.0, 4.0]
    max_err = 0.0
    for u in grid:
        for v in grid:
            val1 = F_sigma_corrected(u, v, 1.0)
            val2 = float(ncx2.cdf(u * u, df=3, nc=v * v))
            max_err = max(max_err, abs(val1 - val2))
    print(f"G9-d 5x5 grid max |F_sigma - ncx2.cdf| = {max_err:.3e}")


if __name__ == "__main__":
    main()
