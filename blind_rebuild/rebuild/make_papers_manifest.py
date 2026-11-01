"""make_papers_manifest.py -- DATA_MANIFEST_REBUILD_PAPERS.sha256 (DEVIATIONS D6): fingerprints every T4b/T4a
literature source downloaded by the rebuild, the text derived from them, and the frozen T4b extraction files.
Chen+19 and Planck 2018 VI are already in DATA_MANIFEST_REBUILD.sha256 and are not repeated."""
import os, glob, hashlib, time, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def main():
    meta = {}
    for tsv in sorted(glob.glob(os.path.join(ROOT, "t4b_extraction", "downloads_*.tsv"))):
        for line in open(tsv, encoding="utf-8-sig").read().splitlines()[1:]:
            p = line.strip().split("\t")
            if len(p) >= 3:
                rel = os.path.relpath(p[0], ROOT).replace("\\", "/")
                meta[rel] = (p[1], p[2])
    files = []
    for p in sorted(glob.glob(os.path.join(ROOT, "data", "papers", "*", "*"))):
        if os.path.isdir(p):
            continue
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        if rel.startswith("data/papers/chen2019/") or rel.startswith("data/papers/planck2018_VI/"):
            continue
        files.append(rel)
    ext = sorted(os.path.relpath(p, ROOT).replace("\\", "/") for p in
                 glob.glob(os.path.join(ROOT, "t4b_extraction", "*")) if not os.path.isdir(p))
    now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    out = ["# DATA_MANIFEST_REBUILD_PAPERS -- literature sources for T4b/T4a + frozen T4b extraction (DEVIATIONS D6)",
           f"# Generated: {now} (before any T4b statistic is computed)",
           "# Format: <sha256_hex>  <relative_path>   (metadata in the comment line above each file)"]
    for rel in files:
        if rel in meta:
            url, t = meta[rel]
            m = f"url={url} | downloaded_utc={t}"
        elif rel.endswith(".gz") or rel.endswith(".pdf"):
            arx = os.path.basename(rel).split("_")[0].replace(".pdf", "")
            m = (f"url=https://arxiv.org/e-print/{arx} (download time not recorded in the sub-agent TSV; "
                 f"file mtime {time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(os.path.getmtime(os.path.join(ROOT, rel))))} local)")
        else:
            m = "derived text extracted locally from the PDF/e-print in the same folder"
        out.append(f"# {m} | bytes={os.path.getsize(os.path.join(ROOT, rel))}")
        out.append(f"{sha256(os.path.join(ROOT, rel))}  {rel}")
    out.append("# ---- frozen T4b extraction (protocol, per-cluster records, structured table)")
    for rel in ext:
        out.append(f"{sha256(os.path.join(ROOT, rel))}  {rel}")
    open(os.path.join(ROOT, "DATA_MANIFEST_REBUILD_PAPERS.sha256"), "w", encoding="utf-8", newline="\n").write(
        "\n".join(out) + "\n")
    print(len(files), "paper files,", len(ext), "extraction files")


if __name__ == "__main__":
    main()
