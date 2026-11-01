import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import ctypes
import hashlib
import shutil
import ssl
import sys
import time

PHASE3_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(PHASE3_DIR, ".."))


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


def stamp_with_ots(ots_mod, filepath):
    ots_path = filepath + ".ots"
    if os.path.exists(ots_path):
        trash_dir = os.path.join(ROOT_DIR, "_TRASH")
        os.makedirs(trash_dir, exist_ok=True)
        backup = os.path.join(trash_dir, os.path.basename(ots_path) + f"_{int(time.time())}.bak")
        os.replace(ots_path, backup)

    print(f"=== Stamping {filepath} -> {ots_path} ===")
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


def sha256_file(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    plan_p3 = os.path.join(PHASE3_DIR, "PHASE3_ANALYSIS_PLAN.md")
    plan_root = os.path.join(ROOT_DIR, "PHASE3_ANALYSIS_PLAN.md")
    shutil.copy2(plan_p3, plan_root)

    rel_entries = [
        "PHASE3_ANALYSIS_PLAN.md",
        "phase3/PHASE3_ANALYSIS_PLAN.md",
        "phase3/DEVIATIONS.md",
        "MOCKS_FOR_ARGON/MOCK_MANIFEST.csv",
    ]

    lines = [
        "# Phase 3 Injection Tests Analysis Plan Manifest (PHASE3_ANALYSIS_PLAN.sha256)",
        "# Label: Phase 3 injection tests: supplementary, not pre-registered in Stage 1",
        f"# Generated at: {time.strftime('%Y-%m-%dT%H:%M:%S-04:00')} (prior to first run)",
        "# Format: <sha256_hex>  <relative_path>",
    ]
    for rel_p in rel_entries:
        full_p = os.path.join(ROOT_DIR, rel_p.replace("/", os.sep))
        lines.append(f"{sha256_file(full_p)}  {rel_p}")

    manifest_p3 = os.path.join(PHASE3_DIR, "PHASE3_ANALYSIS_PLAN.sha256")
    manifest_root = os.path.join(ROOT_DIR, "PHASE3_ANALYSIS_PLAN.sha256")
    with open(manifest_p3, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    shutil.copy2(manifest_p3, manifest_root)

    mhash = sha256_file(manifest_p3)
    print(f"PHASE3_ANALYSIS_PLAN.sha256 SHA-256 = {mhash}")

    ots_mod = setup_ots()
    stamp_with_ots(ots_mod, manifest_p3)
    ots_p3 = manifest_p3 + ".ots"
    ots_root = manifest_root + ".ots"
    assert os.path.exists(ots_p3), "Failed to create PHASE3_ANALYSIS_PLAN.sha256.ots"
    shutil.copy2(ots_p3, ots_root)
    print(f"Copied {ots_p3} -> {ots_root}")


if __name__ == "__main__":
    main()
