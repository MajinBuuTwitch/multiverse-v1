#!/usr/bin/env python3
"""Download the third-party data this record does not redistribute, then check every file against its manifest.

What it fetches (into the folders the manifests expect):
  ropewalk/data/...        everything ropewalk/scripts/get_data.py fetches (its own file lists, read from that
                           script without running it), plus the 8 arXiv e-prints in data/clusters_arxiv_exact/
                           that RESULTS_v2-v5 list
  blind_rebuild/data/...   the rebuild's datasets and source papers, at the URLs its download logs and
                           DATA_MANIFEST_REBUILD_PAPERS.sha256 record

Safety:
  - TLS certificates are verified (Python's default context).
  - A file tracked in git is never written, and an existing file is never overwritten: it is only checked.
    So the frozen data/MANIFEST.csv and data/registered_priors.json that get_data.py would rewrite stay untouched.
  - Downloaded data is git-ignored (.gitignore), so it can't be committed by accident.
  - arXiv is asked politely: one request every 3 seconds.

Usage (from anywhere):  python download_data.py [--dry-run] [--only ropewalk|blind_rebuild]
Then, for the Phase 3 mocks:  python restore_mock_covariances.py
Exit status 0 when every third-party manifest line passes, 1 otherwise. Standard library only.
"""
import argparse
import ast
import hashlib
import json
import os
import re
import ssl
import subprocess
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
RW = os.path.join(ROOT, "ropewalk")
RB = os.path.join(ROOT, "blind_rebuild")
UA = "multiverse-v1-record/1.0 (download_data.py)"
CTX = ssl.create_default_context()  # certificate verification on
LINE = re.compile(r"^([0-9a-f]{64})\s+\*?(\S+)")
DERIVED = set()  # rebuild paper entries with no URL (filled while reading DATA_MANIFEST_REBUILD_PAPERS)

# third-party folders, relative to each workspace (everything else in the manifests ships in the repo)
THIRD_PARTY = {
    "ropewalk": ("data/clusters_arxiv/", "data/clusters_arxiv_exact/", "data/des_dovekie/", "data/desi_bao_dr2/",
                 "data/pantheon_plus/", "data/sparc/"),
    "blind_rebuild": ("data/pantheonplus/", "data/des_dovekie/", "data/desi_bao_dr2/", "data/sparc/", "data/papers/"),
}
MANIFESTS = [
    ("ropewalk", "DATA_MANIFEST.sha256"),
    ("ropewalk", "RESULTS_v5.sha256"),          # adds the 8 clusters_arxiv_exact e-prints
    ("blind_rebuild", "DATA_MANIFEST_REBUILD.sha256"),
    ("blind_rebuild", "DATA_MANIFEST_REBUILD_PAPERS.sha256"),
]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def tracked_files():
    try:
        out = subprocess.run(["git", "-C", ROOT, "ls-files", "-z"], capture_output=True, check=True).stdout
        return {os.path.normcase(os.path.join(ROOT, p)) for p in out.decode("utf-8").split("\0") if p}
    except Exception:
        return None  # not a git checkout: existing files are still never overwritten


def get_data_lists():
    """Read the file lists from the frozen ropewalk/scripts/get_data.py without running it."""
    tree = ast.parse(open(os.path.join(RW, "scripts", "get_data.py"), encoding="utf-8").read())
    lists = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name in ("DESI_FILES", "PANTHEON_FILES", "DOVEKIE_FILES", "SPARC_FILES", "CLUSTER_ARXIV_PAPERS"):
                lists[name] = ast.literal_eval(node.value)
    return lists


def jobs_ropewalk():
    g = get_data_lists()
    # the same URL templates get_data.py uses
    for f in g["DESI_FILES"]:
        yield ("ropewalk", "data/desi_bao_dr2/" + f,
               f"https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/{f}")
    for f in g["PANTHEON_FILES"]:
        yield ("ropewalk", "data/pantheon_plus/" + f,
               f"https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon+_Data/4_DISTANCES_AND_COVAR/{f}")
    for f in g["DOVEKIE_FILES"]:
        yield ("ropewalk", "data/des_dovekie/" + f,
               f"https://raw.githubusercontent.com/des-science/DES-SN5YR/main/4_DISTANCES_COVMAT/{f}")
    for f in g["SPARC_FILES"]:
        yield ("ropewalk", "data/sparc/" + f, f"https://astroweb.case.edu/SPARC/{f}")
    for arxiv_id, label in g["CLUSTER_ARXIV_PAPERS"]:
        yield ("ropewalk", f"data/clusters_arxiv/{arxiv_id.replace('/', '_')}_{label}.eprint",
               f"https://arxiv.org/e-print/{arxiv_id}")
    # the 8 exact e-prints RESULTS_v5 lists (file names start with the arXiv ID)
    for line in open(os.path.join(RW, "RESULTS_v5.sha256"), encoding="utf-8"):
        m = re.match(r"^[0-9a-f]{64}\s+(data/clusters_arxiv_exact/(\d{4}\.\d{4,5})_\S+)", line)
        if m:
            yield ("ropewalk", m.group(1), "https://arxiv.org/e-print/" + m.group(2))


def jobs_rebuild():
    seen = set()
    for log in ("download_log.json", "download_log_extra.json"):
        for rec in json.load(open(os.path.join(RB, "data", log), encoding="utf-8")):
            seen.add(rec["path"])
            yield ("blind_rebuild", rec["path"], rec["url"])
    url = None
    for line in open(os.path.join(RB, "DATA_MANIFEST_REBUILD_PAPERS.sha256"), encoding="utf-8"):
        m = re.match(r"#\s*url=(\S+)", line)
        if m:
            url = m.group(1)
            continue
        m = LINE.match(line.strip())
        if m and m.group(2).startswith("data/papers/"):
            if url and m.group(2) not in seen:
                yield ("blind_rebuild", m.group(2), url)
            elif not url:
                DERIVED.add(m.group(2))  # text the rebuild extracted from a PDF: nothing to download
            url = None


def fetch(url, tries=3):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, context=CTX, timeout=120) as r:
                return r.read()
        except Exception as e:
            if k == tries - 1:
                raise
            time.sleep(10 * (k + 1))


def main():
    ap = argparse.ArgumentParser(description="Download and verify the third-party data.")
    ap.add_argument("--dry-run", action="store_true", help="list what would be downloaded; write nothing")
    ap.add_argument("--only", choices=["ropewalk", "blind_rebuild"])
    args = ap.parse_args()

    tracked = tracked_files()
    jobs = []
    if args.only in (None, "ropewalk"):
        jobs += list(jobs_ropewalk())
    if args.only in (None, "blind_rebuild"):
        jobs += list(jobs_rebuild())

    got = skipped = errors = 0
    last_arxiv = 0.0
    for ws, rel, url in jobs:
        dest = os.path.join(ROOT, ws, rel.replace("/", os.sep))
        if tracked is not None and os.path.normcase(dest) in tracked:
            print(f"SKIP tracked file (never written): {ws}/{rel}")
            skipped += 1
            continue
        if os.path.exists(dest):
            skipped += 1
            continue
        if args.dry_run:
            print("would fetch", url, "->", f"{ws}/{rel}")
            continue
        if "arxiv.org" in url:
            time.sleep(max(0.0, 3.0 - (time.time() - last_arxiv)))
            last_arxiv = time.time()
        try:
            data = fetch(url)
        except Exception as e:
            print(f"ERROR {ws}/{rel}: {url}: {e}")
            errors += 1
            continue
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        tmp = dest + ".part"
        with open(tmp, "wb") as f:
            f.write(data)
        os.replace(tmp, dest)  # dest did not exist (checked above)
        got += 1
        print(f"fetched {ws}/{rel} ({len(data):,} bytes)")
    print(f"\nfetched {got}, already present or skipped {skipped}, download errors {errors}")
    if args.dry_run:
        return

    # verify every third-party line of every data manifest
    npass = nfail = nmiss = nder = 0
    for ws, man in MANIFESTS:
        if args.only and ws != args.only:
            continue
        base = os.path.join(ROOT, ws)
        p_, f_, m_, d_ = 0, [], [], 0
        for line in open(os.path.join(base, man), encoding="utf-8"):
            m = LINE.match(line.strip())
            if not m or not m.group(2).startswith(THIRD_PARTY[ws]):
                continue
            want, rel = m.group(1), m.group(2)
            path = os.path.join(base, rel.replace("/", os.sep))
            if not os.path.isfile(path):
                if ws == "blind_rebuild" and rel in DERIVED:
                    d_ += 1
                else:
                    m_.append(rel)
            elif sha256(path) == want:
                p_ += 1
            else:
                f_.append(rel)
        for rel in f_:
            print(f"FAIL     {ws}/{man}: {rel}")
        for rel in m_:
            print(f"MISSING  {ws}/{man}: {rel}")
        extra = f", {d_} derived (not downloadable)" if d_ else ""
        print(f"{'PASS' if not f_ and not m_ else 'FAIL'}     {ws}/{man}: {p_} PASS, {len(f_)} FAIL, {len(m_)} missing{extra}")
        npass += p_; nfail += len(f_); nmiss += len(m_); nder += d_
    print(f"\nTOTAL: {npass} PASS, {nfail} FAIL, {nmiss} missing, {nder} derived (not downloadable)")
    if nder:
        print("Derived entries are text the rebuild extracted from the downloaded PDFs (pdf.txt, *_pdftext.txt,\n"
              "FigureS*.txt) with the scripts in blind_rebuild/t4b_extraction/; there is nothing to download for them.")
    sys.exit(0 if nfail == 0 and nmiss == 0 else 1)


if __name__ == "__main__":
    main()
