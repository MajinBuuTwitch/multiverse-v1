import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import hashlib
import sys
import ctypes
import ssl
from datetime import datetime

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(ROOT_DIR)


def stamp_with_ots(filepath):
    orig_load = ctypes.cdll.LoadLibrary

    def patched_load(name):
        if name is None:
            return ctypes.CDLL(r"C:\Python314\DLLs\libcrypto-3.dll")
        return orig_load(name)

    ctypes.cdll.LoadLibrary = patched_load
    ssl._create_default_https_context = ssl._create_unverified_context

    import otsclient.ots

    ots_path = filepath + ".ots"
    if os.path.exists(ots_path):
        backup = os.path.join(ROOT_DIR, "_TRASH", os.path.basename(ots_path) + ".bak")
        os.replace(ots_path, backup)

    sys.argv = [
        "ots",
        "stamp",
        "-c",
        "https://alice.btc.calendar.opentimestamps.org",
        "-c",
        "https://bob.btc.calendar.opentimestamps.org",
        "-c",
        "https://finney.calendar.eternitywall.com",
        filepath,
    ]
    try:
        otsclient.ots.main()
    except SystemExit as e:
        print("ots stamp exit:", e.code)

    sys.argv = ["ots", "info", ots_path]
    try:
        otsclient.ots.main()
    except SystemExit:
        pass


def main():
    rel_files = [
        "PREREG_v4.sha256",
        "DATA_MANIFEST.sha256",
        "DEVIATIONS.md",
        "RESULTS.md",
        "results/RESULTS.md",
        "MULTIVERSE_PREDICTIONS_PAPER_v2.md",
        "README.md",
        "REVIEW_PACKET.md",
        "requirements.txt",
        "run_all.py",
        "data/MERGERS.csv",
        "data/MANIFEST.csv",
        "data/registered_priors.json",
        "results/validation_gates_g9.json",
        "results/FREEZE_T1.json",
        "results/FREEZE_T2.json",
        "results/FREEZE_T4.json",
        "results/FREEZE_T5.json",
        "results/FREEZE_T6.json",
        "results/FIXED_VALUES.json",
        "results/part9_cosmology_results.json",
        "results/results.json",
        "results/figures/fig1_t1_unwinding_vs_desi.png",
        "results/figures/fig2_t2_strand_budget_tension.png",
        "results/figures/fig3_t4b_cluster_mergers.png",
        "results/figures/fig4_t5_sparc_rotation_curves.png",
        "results/figures/fig5_t6_regional_h0_and_coincidence.png",
        "scripts/cosmology.py",
        "scripts/clusters_t4.py",
        "scripts/sparc_t5.py",
        "scripts/local_h0_t6.py",
        "scripts/run_part8_fixes.py",
        "scripts/run_part9_cosmology_tests.py",
        "scripts/run_part10_astrophysics_and_verdict.py",
        "scripts/freeze_data_manifest.py",
        "scripts/freeze_results_v1.py",
        "tests/test_gates_g9.py",
        "tests/test_clusters_synthetic.py",
        "tests/test_sparc_synthetic.py",
    ]

    lines = [
        "# Stage 4 Final Results & Code Manifest (RESULTS_v1.sha256)",
        f"# Generated at: {datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}",
        "# Overall Model Verdict: MODEL FALSIFIED (FAIL)",
        "# Format: <sha256_hex>  <relative_path>",
    ]

    for rel in rel_files:
        p = os.path.join(ROOT_DIR, rel.replace("/", os.sep))
        assert os.path.exists(p), f"Missing required deliverable: {rel}"
        with open(p, "rb") as f:
            h = hashlib.sha256(f.read()).hexdigest()
        lines.append(f"{h}  {rel}")

    out_path = os.path.join(ROOT_DIR, "RESULTS_v1.sha256")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")

    with open(out_path, "rb") as f:
        h_master = hashlib.sha256(f.read()).hexdigest()
    print(f"Wrote RESULTS_v1.sha256 ({len(rel_files)} files), Master SHA-256 = {h_master}")

    stamp_with_ots("RESULTS_v1.sha256")


if __name__ == "__main__":
    main()
