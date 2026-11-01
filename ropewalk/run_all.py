import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import subprocess
import sys
from pathlib import Path
import psutil


def set_below_normal_priority():
    try:
        p = psutil.Process(os.getpid())
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass


def run_step(description: str, script_rel_path: str, root: Path):
    print(f"\n{'=' * 72}\n[RUN_ALL] {description} ({script_rel_path})\n{'=' * 72}")
    cmd = [sys.executable, str(root / script_rel_path)]
    res = subprocess.run(cmd, cwd=str(root), check=True)
    return res.returncode


def main():
    set_below_normal_priority()
    root = Path(__file__).resolve().parent

    steps = [
        ("Step 1: Verify Pre-Test Validation Gates (G9-a to G9-d)", "tests/test_gates_g9.py"),
        ("Step 2: Run Synthetic Cluster Pipeline Unit Tests", "tests/test_clusters_synthetic.py"),
        ("Step 3: Run Synthetic SPARC & HEALPix Unit Tests", "tests/test_sparc_synthetic.py"),
        ("Step 4: Execute All FIX Runs and Freeze Parameters (Part 8)", "scripts/run_part8_fixes.py"),
        ("Step 5: Execute Cosmological TEST Runs T1, T2, T6 & Coincidence Window (Part 9)", "scripts/run_part9_cosmology_tests.py"),
        ("Step 6: Execute Astrophysical TEST Runs T4, T5, Holm Control & Figures (Part 10)", "scripts/run_part10_astrophysics_and_verdict.py"),
    ]

    for desc, rel_path in steps:
        run_step(desc, rel_path, root)

    print("\n" + "=" * 72)
    print("[RUN_ALL] ALL VALIDATION GATES, FIXES, TESTS, AND FIGURES COMPLETED.")
    print("Master JSON output: results/results.json")
    print("=" * 72)


if __name__ == "__main__":
    main()
