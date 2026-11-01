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


def setup_ots():
    orig_load = ctypes.cdll.LoadLibrary

    def patched_load(name):
        if name is None:
            return ctypes.CDLL(r"C:\Python314\DLLs\libcrypto-3.dll")
        return orig_load(name)

    ctypes.cdll.LoadLibrary = patched_load
    ssl._create_default_https_context = ssl._create_unverified_context
    import otsclient.ots
    return otsclient.ots


def upgrade_and_info_ots(ots_mod, ots_path):
    print(f"\n=== Checking & Upgrading {ots_path} ===")
    sys.argv = ["ots", "upgrade", ots_path]
    try:
        ots_mod.main()
    except SystemExit as e:
        print(f"ots upgrade({ots_path}) exit:", e.code)
    except Exception as e:
        print(f"ots upgrade({ots_path}) error:", e)

    sys.argv = ["ots", "info", ots_path]
    try:
        ots_mod.main()
    except SystemExit:
        pass


def stamp_with_ots(ots_mod, filepath):
    ots_path = filepath + ".ots"
    if os.path.exists(ots_path):
        backup = os.path.join(ROOT_DIR, "_TRASH", os.path.basename(ots_path) + ".bak")
        os.replace(ots_path, backup)

    print(f"\n=== Stamping {filepath} -> {ots_path} ===")
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
        ots_mod.main()
    except SystemExit as e:
        print("ots stamp exit:", e.code)

    sys.argv = ["ots", "info", ots_path]
    try:
        ots_mod.main()
    except SystemExit:
        pass


def main():
    ots_mod = setup_ots()

    for prev_ots in [
        "PREREG_v4.sha256.ots",
        "DATA_MANIFEST.sha256.ots",
        "RESULTS_v1.sha256.ots",
    ]:
        if os.path.exists(prev_ots):
            upgrade_and_info_ots(ots_mod, prev_ots)

    exact_cluster_files = []
    exact_dir = os.path.join(ROOT_DIR, "data", "clusters_arxiv_exact")
    if os.path.isdir(exact_dir):
        for fn in sorted(os.listdir(exact_dir)):
            full_p = os.path.join(exact_dir, fn)
            if os.path.isfile(full_p):
                exact_cluster_files.append(f"data/clusters_arxiv_exact/{fn}")

    rel_files = [
        # Cryptographic chain manifests & review report
        "PREREG_v4.sha256",
        "DATA_MANIFEST.sha256",
        "RESULTS_v1.sha256",
        "REVIEW_FINAL.md",
        # Frozen Stage 1 pre-registration documents
        "PREREG.md",
        "MULTIVERSE_STAGE1_EQUATIONS.md",
        "ASSUMPTIONS.md",
        # Stage 4 v2 updated/created documentation deliverables
        "DEVIATIONS.md",
        "RESULTS.md",
        "results/RESULTS.md",
        "MULTIVERSE_PREDICTIONS_PAPER_v3.md",
        "CLAIMS_CHECK.md",
        "README.md",
        "requirements.txt",
        "run_all.py",
        # Data tables & manifests
        "data/MERGERS.csv",
        "data/MANIFEST.csv",
        "data/registered_priors.json",
        *exact_cluster_files,
        # Results JSONs & validation gate outputs (unchanged fit outputs + final gate check)
        "results/validation_gates_g9.json",
        "results/validation_gates_g9_final.json",
        "results/FREEZE_T1.json",
        "results/FREEZE_T2.json",
        "results/FREEZE_T4.json",
        "results/FREEZE_T5.json",
        "results/FREEZE_T6.json",
        "results/FIXED_VALUES.json",
        "results/part9_cosmology_results.json",
        "results/results.json",
        # Figures
        "results/figures/fig1_t1_unwinding_vs_desi.png",
        "results/figures/fig2_t2_strand_budget_tension.png",
        "results/figures/fig3_t4b_cluster_mergers.png",
        "results/figures/fig4_t5_sparc_rotation_curves.png",
        "results/figures/fig5_t6_regional_h0_and_coincidence.png",
        # Analysis, data, figure, gate & freeze scripts
        "scripts/get_data.py",
        "scripts/cosmology.py",
        "scripts/clusters_t4.py",
        "scripts/sparc_t5.py",
        "scripts/local_h0_t6.py",
        "scripts/run_part8_fixes.py",
        "scripts/run_part9_cosmology_tests.py",
        "scripts/run_part10_astrophysics_and_verdict.py",
        "scripts/freeze_data_manifest.py",
        "scripts/freeze_results_v1.py",
        "scripts/run_gates_g9_final.py",
        "scripts/freeze_results_v2.py",
        # Unit & synthetic tests
        "tests/test_gates_g9.py",
        "tests/test_clusters_synthetic.py",
        "tests/test_sparc_synthetic.py",
    ]

    lines = [
        "# Stage 4 Corrected Results & Code Manifest (RESULTS_v2.sha256)",
        f"# Generated at: {datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}",
        "# Chains from RESULTS_v1.sha256 (b02000c98008e32ef34265a417e9d7dd724e3ee8472bc3cdf6be494f7477dd4e)",
        "# Overall Model Verdict: MODEL FALSIFIED (FAIL) [Unchanged from v1; per REVIEW_FINAL.md]",
        "# Format: <sha256_hex>  <relative_path>",
    ]

    for rel in rel_files:
        p = os.path.join(ROOT_DIR, rel.replace("/", os.sep))
        assert os.path.exists(p), f"Missing required deliverable: {rel}"
        with open(p, "rb") as f:
            h = hashlib.sha256(f.read()).hexdigest()
        lines.append(f"{h}  {rel}")

    out_path = os.path.join(ROOT_DIR, "RESULTS_v2.sha256")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")

    with open(out_path, "rb") as f:
        h_master = hashlib.sha256(f.read()).hexdigest()
    print(f"\nWrote RESULTS_v2.sha256 ({len(rel_files)} files), Master SHA-256 = {h_master}")

    stamp_with_ots(ots_mod, "RESULTS_v2.sha256")


if __name__ == "__main__":
    main()
