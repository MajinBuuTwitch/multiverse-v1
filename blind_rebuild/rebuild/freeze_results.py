"""freeze_results.py -- REBUILD_RESULTS_v1.sha256: SHA-256 of every output, code file, manifest and REBUILD_RESULTS.md."""
import os, glob, hashlib, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


pats = ["REBUILD_RESULTS.md", "DEVIATIONS_REBUILD.md", "REBUILD_RULES.md", "CLAUDE.md", "run_all_rebuild.py",
        "download_data_rebuild.py", "make_manifest_rebuild.py", "requirements_rebuild.txt",
        "DATA_MANIFEST_REBUILD.sha256", "DATA_MANIFEST_REBUILD.sha256.ots",
        "DATA_MANIFEST_REBUILD_PAPERS.sha256", "DATA_MANIFEST_REBUILD_PAPERS.sha256.ots",
        "rebuild/*.py", "results_rebuild/*.json", "results_rebuild/*/*", "t4b_extraction/*"]
files = sorted({os.path.relpath(p, ROOT).replace("\\", "/") for pat in pats for p in glob.glob(os.path.join(ROOT, pat))
                if os.path.isfile(p)})
log = os.path.join(ROOT, "ACTIVITY_LOG_REBUILD.md")
now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
out = ["# REBUILD_RESULTS_v1.sha256 -- PHASE 1 freeze of the blind rebuild",
       f"# Generated: {now}",
       f"# ACTIVITY_LOG_REBUILD.md is append-only; it is hashed at its byte length at freeze time "
       f"({os.path.getsize(log)} bytes). Verify later entries against that byte prefix."]
out += [f"{sha256(os.path.join(ROOT, f))}  {f}" for f in files]
out.append(f"{sha256(log)}  ACTIVITY_LOG_REBUILD.md")
open(os.path.join(ROOT, "REBUILD_RESULTS_v1.sha256"), "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print(len(files) + 1, "files hashed")
