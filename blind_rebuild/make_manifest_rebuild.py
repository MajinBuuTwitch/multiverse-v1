"""make_manifest_rebuild.py -- build a sha256 manifest (sha256sum format, metadata in comment lines)."""
import hashlib, json, os, sys, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def write_manifest(out, records, title):
    lines = [f"# {title}",
             f"# Generated: {datetime.datetime.now().astimezone().isoformat(timespec='seconds')}",
             "# Format: <sha256_hex>  <relative_path>   (metadata for each file in the comment line above it)"]
    for r in records:
        p = os.path.join(ROOT, r["path"])
        h = sha256(p)
        if r.get("sha256") and r["sha256"] != h:
            raise SystemExit(f"hash changed since download: {r['path']}")
        lines.append(f"# url={r['url']} | version={r.get('version','')} | downloaded_utc={r['downloaded_utc']} | bytes={os.path.getsize(p)}")
        lines.append(f"{h}  {r['path']}")
    open(os.path.join(ROOT, out), "w", newline="\n").write("\n".join(lines) + "\n")
    print("wrote", out, len(records), "files")


if __name__ == "__main__":
    which = sys.argv[1]
    if which == "data":
        recs = json.load(open(os.path.join(ROOT, "data", "download_log.json")))
        recs += json.load(open(os.path.join(ROOT, "data", "download_log_extra.json")))
        write_manifest("DATA_MANIFEST_REBUILD.sha256", recs,
                       "DATA_MANIFEST_REBUILD -- registered datasets + benchmark/reference sources downloaded by the rebuild")
    elif which == "papers":
        recs = json.load(open(os.path.join(ROOT, "data", "download_log_papers.json")))
        write_manifest("DATA_MANIFEST_REBUILD_PAPERS.sha256", recs,
                       "DATA_MANIFEST_REBUILD_PAPERS -- literature sources for T4b cluster positions / T4a (downloaded by the rebuild)")
