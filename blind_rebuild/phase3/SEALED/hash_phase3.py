"""hash_phase3.py -- PHASE3_INJECTION_v1.sha256: SHA-256 of every file in MOCKS_FOR_ARGON/ and SEALED/."""
import os, hashlib, datetime
PH3 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()
files = []
for top in ("MOCKS_FOR_ARGON", "SEALED"):
    for dp, dn, fn in os.walk(os.path.join(PH3, top)):
        dn.sort()
        for f in sorted(fn):
            files.append(os.path.relpath(os.path.join(dp, f), PH3).replace("\\", "/"))
log = os.path.join(PH3, "SEALED", "GENERATION_LOG.md")
out = ["# PHASE3_INJECTION_v1.sha256 -- Phase 3 injection set (blind-rebuild workspace)",
       f"# Generated: {datetime.datetime.now().astimezone().isoformat(timespec='seconds')}",
       f"# SEALED/GENERATION_LOG.md is append-only; hashed at {os.path.getsize(log)} bytes (verify later entries by prefix)."]
out += [f"{sha(os.path.join(PH3, f))}  {f}" for f in files]
open(os.path.join(PH3, "PHASE3_INJECTION_v1.sha256"), "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
n_m = sum(f.startswith("MOCKS_FOR_ARGON/") for f in files); n_s = sum(f.startswith("SEALED/") for f in files)
print(f"{len(files)} files hashed: MOCKS_FOR_ARGON {n_m}, SEALED {n_s}")
