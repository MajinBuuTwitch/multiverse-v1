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

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
H2H_DIR = os.path.abspath(os.path.dirname(__file__))


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
        backup = os.path.join(trash_dir, os.path.basename(ots_path) + ".bak")
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


def main():
    ots_mod = setup_ots()
    plan_manifest_h2h = os.path.join(H2H_DIR, "HEAD_TO_HEAD_PLAN.sha256")
    plan_manifest_root = os.path.join(ROOT_DIR, "HEAD_TO_HEAD_PLAN.sha256")

    with open(plan_manifest_h2h, "rb") as f:
        mhash = hashlib.sha256(f.read()).hexdigest()
    print(f"HEAD_TO_HEAD_PLAN.sha256 SHA-256 = {mhash}")

    stamp_with_ots(ots_mod, plan_manifest_h2h)
    ots_h2h = plan_manifest_h2h + ".ots"
    ots_root = plan_manifest_root + ".ots"
    assert os.path.exists(ots_h2h), "Failed to create HEAD_TO_HEAD_PLAN.sha256.ots"
    shutil.copy2(ots_h2h, ots_root)
    print(f"Copied {ots_h2h} -> {ots_root}")


if __name__ == "__main__":
    main()
