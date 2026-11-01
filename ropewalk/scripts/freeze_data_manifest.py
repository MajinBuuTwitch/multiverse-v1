import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import csv
import hashlib
import sys
import ctypes
import ssl

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
    manifest_csv = os.path.join(ROOT_DIR, "data", "MANIFEST.csv")
    with open(manifest_csv, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    lines = [
        "# Stage 2 Frozen Data Manifest (DATA_MANIFEST.sha256)",
        "# Generated before any validation gate, fixing fit, or test evaluation.",
        "# Format: <sha256_hex>  <relative_path>  # url=<url> | version=<version> | downloaded=<timestamp> | size=<bytes>",
    ]

    for r in rows:
        rel = r["relative_path"]
        p = os.path.join(ROOT_DIR, rel.replace("/", os.sep))
        with open(p, "rb") as f:
            h_disk = hashlib.sha256(f.read()).hexdigest()
        assert h_disk == r["sha256"], f"SHA256 mismatch on {rel}"
        lines.append(
            f"{h_disk}  {rel}  # url={r['url']} | version={r['version_or_release']} | downloaded={r['download_timestamp']} | size={r['size_bytes']}"
        )

    with open(manifest_csv, "rb") as f:
        h_csv = hashlib.sha256(f.read()).hexdigest()
    lines.append(f"{h_csv}  data/MANIFEST.csv  # Master CSV manifest of all {len(rows)} downloaded files")

    out_path = os.path.join(ROOT_DIR, "DATA_MANIFEST.sha256")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")

    with open(out_path, "rb") as f:
        h_dm = hashlib.sha256(f.read()).hexdigest()
    print("Wrote DATA_MANIFEST.sha256, SHA-256 =", h_dm)

    stamp_with_ots("DATA_MANIFEST.sha256")


if __name__ == "__main__":
    main()
