#!/usr/bin/env python3
"""Restore the third-party covariance files that the Phase 3 mock folders omit.

The 45 mock universes in MOCKS_FOR_ARGON/ used unmodified copies of three public
covariance files. To keep the repository small, those 60 copies per mock set are
not shipped. After downloading the public data, this script copies each file back
into every mock subfolder that held it, then checks every restored copy:
  - against the SHA-256 of the original third-party file (below), and
  - against blind_rebuild/phase3/PHASE3_INJECTION_v1.sha256, which lists every mock file.

Usage (from the repository root):
    python restore_mock_covariances.py [--data DIR] [--dry-run]

--data is the folder holding the downloaded datasets (default: ropewalk/data, where
ropewalk/scripts/get_data.py writes them). It must contain
    pantheon_plus/Pantheon+SH0ES_STAT+SYS.cov
    des_dovekie/STAT+SYS.npz
    desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt
Existing files are never overwritten: a target that already exists is checked and skipped.
Standard library only.
"""
import argparse
import hashlib
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MOCK_SETS = ["ropewalk/MOCKS_FOR_ARGON", "blind_rebuild/phase3/MOCKS_FOR_ARGON"]
# lists every mock file, with paths relative to blind_rebuild/phase3
INJECTION_MANIFEST = "blind_rebuild/phase3/PHASE3_INJECTION_v1.sha256"

# file name in a mock folder -> (path under the data folder, SHA-256, bytes)
ORIGINALS = {
    "Pantheon+SH0ES_STAT+SYS.cov": ("pantheon_plus/Pantheon+SH0ES_STAT+SYS.cov",
        "abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc", 33284960),
    "STAT+SYS.npz": ("des_dovekie/STAT+SYS.npz",
        "ffd3124b32148b1372bd95fda9299269f0352a9f8eee02d416c610e38495463b", 6244951),
    "desi_gaussian_bao_ALL_GCcomb_cov.txt": ("desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
        "252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509", 2547),
}

# every mock file that held a copy (the same 60 paths in both mock sets)
TARGETS = [
    "U-099J/des_dovekie/STAT+SYS.npz",
    "U-099J/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "U-099J/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-2B0Y/des_dovekie/STAT+SYS.npz",
    "U-2B0Y/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "U-2B0Y/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-44A3/des_dovekie/STAT+SYS.npz",
    "U-44A3/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "U-44A3/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-4JZF/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-51CN/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-6VMC/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-8Z6F/des_dovekie/STAT+SYS.npz",
    "U-8Z6F/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "U-8Z6F/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-B485/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-BKI0/des_dovekie/STAT+SYS.npz",
    "U-BKI0/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "U-BKI0/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-CUIZ/des_dovekie/STAT+SYS.npz",
    "U-CUIZ/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "U-CUIZ/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-EATJ/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-GL5Z/des_dovekie/STAT+SYS.npz",
    "U-GL5Z/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "U-GL5Z/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-IBCC/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-J8TH/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-J91F/des_dovekie/STAT+SYS.npz",
    "U-J91F/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "U-J91F/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-JNXP/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-KCY8/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-KPN8/des_dovekie/STAT+SYS.npz",
    "U-KPN8/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "U-KPN8/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-LH19/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-LMB5/des_dovekie/STAT+SYS.npz",
    "U-LMB5/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "U-LMB5/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-LYTB/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-NBRH/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-OEDW/des_dovekie/STAT+SYS.npz",
    "U-OEDW/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "U-OEDW/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-PAKD/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-SU9K/des_dovekie/STAT+SYS.npz",
    "U-SU9K/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "U-SU9K/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-Y2N1/des_dovekie/STAT+SYS.npz",
    "U-Y2N1/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "U-Y2N1/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-YIG4/des_dovekie/STAT+SYS.npz",
    "U-YIG4/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "U-YIG4/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-YNED/des_dovekie/STAT+SYS.npz",
    "U-YNED/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "U-YNED/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-ZJBO/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
    "U-ZY0Y/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov",
]

MANIFEST_LINE = re.compile(r"^([0-9a-f]{64})\s+\*?(\S.*?)\s*$")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def injection_hashes():
    want = {}
    with open(os.path.join(ROOT, INJECTION_MANIFEST), encoding="utf-8") as f:
        for line in f:
            m = MANIFEST_LINE.match(line.strip())
            if m and m.group(2).startswith("MOCKS_FOR_ARGON/"):
                want[m.group(2)[len("MOCKS_FOR_ARGON/"):]] = m.group(1)
    return want


def main():
    ap = argparse.ArgumentParser(description="Restore the omitted Phase 3 mock covariance copies.")
    ap.add_argument("--data", default=os.path.join(ROOT, "ropewalk", "data"),
                    help="folder holding the downloaded datasets (default: ropewalk/data)")
    ap.add_argument("--dry-run", action="store_true", help="list what would be copied, change nothing")
    args = ap.parse_args()

    sources = {}
    for name, (rel, digest, _size) in ORIGINALS.items():
        src = os.path.join(args.data, rel)
        if not os.path.isfile(src):
            sys.exit(f"missing {src}: download the data first (ropewalk/scripts/get_data.py)")
        got = sha256(src)
        if got != digest:
            sys.exit(f"{src} is not the original third-party file (sha256 {got}, expected {digest})")
        sources[name] = src

    want = injection_hashes()
    copied = present = 0
    failures = []
    for mock_set in MOCK_SETS:
        base = os.path.join(ROOT, mock_set)
        if not os.path.isdir(base):
            print(f"note: {mock_set} not present, skipped")
            continue
        for rel in TARGETS:
            name = rel.rsplit("/", 1)[-1]
            dest = os.path.join(base, rel)
            if os.path.exists(dest):
                present += 1
            elif args.dry_run:
                print("would copy", sources[name], "->", dest)
                continue
            else:
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copyfile(sources[name], dest)
                copied += 1
            got = sha256(dest)
            if got != ORIGINALS[name][1] or want.get(rel) != got:
                failures.append(f"{mock_set}/{rel}: sha256 {got}")

    print(f"restored {copied}, already present {present} ({len(TARGETS)} targets per mock set)")
    if failures:
        print("FAILED checks:")
        print("\n".join(failures))
        sys.exit(1)
    if not args.dry_run:
        print("every restored copy matches its original and PHASE3_INJECTION_v1.sha256")


if __name__ == "__main__":
    main()
