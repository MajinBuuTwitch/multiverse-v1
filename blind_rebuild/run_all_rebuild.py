"""run_all_rebuild.py -- single entry point that reproduces the whole blind rebuild from the downloaded data.

Steps (each step is skipped if its output already exists, unless --force is given):
  1. verify the frozen package against PREREG_v4.sha256
  2. verify every data file against DATA_MANIFEST_REBUILD.sha256 (+ DATA_MANIFEST_REBUILD_PAPERS.sha256);
     missing data are downloaded by download_data_rebuild.py
  3. one-time CAMB calibration of r_d; numerical validation of the cosmology integrators
  4. all expansion-history fits (gates, deciding T1/T2, sensitivity runs) in parallel
  5. analysis: gates, T1-L1, T1-Sign, T2-A, T2-N1, T2-N2, T4b, T5-A/B/c, T6, Holm-Bonferroni, model verdict,
     NON-DECIDING sensitivities -> results_rebuild/results.json
  6. tables and figures -> results_rebuild/tables, results_rebuild/figures
  7. REBUILD_RESULTS.md (written mechanically from results_rebuild/results.json)
The literature manifest DATA_MANIFEST_REBUILD_PAPERS.sha256 is produced once by rebuild/make_papers_manifest.py
(and OTS-stamped) before T4b; step 2 only verifies it.
Random seeds: SEED = 20261030 (registered master seed); run i (sorted name order) uses SEED + 1000 i;
Monte Carlo checks use SEED directly.
Usage:  .venv\\Scripts\\python.exe run_all_rebuild.py [--force] [--ncores 14]
"""
import os, sys, json, hashlib, subprocess, argparse, time

ROOT = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
RES = os.path.join(ROOT, "results_rebuild")


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def verify_manifest(path, base=ROOT, allow_missing=False):
    out = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        h, rel = line.split(None, 1)
        p = os.path.join(base, rel)
        if not os.path.exists(p):
            out.append(dict(file=rel, status="ABSENT"))
            continue
        out.append(dict(file=rel, status="MATCH" if sha256(p) == h else "FAIL", sha256=sha256(p)))
    return out


def step(msg):
    print(time.strftime("%H:%M:%S"), "==", msg, flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--ncores", type=int, default=14)
    a = ap.parse_args()
    os.makedirs(os.path.join(RES, "validation"), exist_ok=True)
    step("1. frozen package verification")
    v = verify_manifest(os.path.join(ROOT, "PREREG_v4.sha256"))
    gov = ["PREREG.md", "MULTIVERSE_STAGE1_EQUATIONS.md", "ASSUMPTIONS.md", "STAGE1_PART1_SECTIONS_ABC.md",
           "STAGE1_PART2_SECTIONS_DGH.md", "STAGE1_PART3_SECTIONS_EFI.md"]
    json.dump(v, open(os.path.join(RES, "validation", "package_verification.json"), "w"), indent=1)
    bad = [x for x in v if x["file"] in gov and x["status"] != "MATCH"]
    if bad:
        raise SystemExit(f"governing file verification failed: {bad}")
    step("2. data verification")
    if not os.path.exists(os.path.join(ROOT, "data", "pantheonplus", "Pantheon+SH0ES.dat")):
        subprocess.check_call([PY, os.path.join(ROOT, "download_data_rebuild.py")])
    dv = verify_manifest(os.path.join(ROOT, "DATA_MANIFEST_REBUILD.sha256"))
    if os.path.exists(os.path.join(ROOT, "DATA_MANIFEST_REBUILD_PAPERS.sha256")):
        dv += verify_manifest(os.path.join(ROOT, "DATA_MANIFEST_REBUILD_PAPERS.sha256"))
    json.dump(dv, open(os.path.join(RES, "validation", "data_verification.json"), "w"), indent=1)
    if any(x["status"] != "MATCH" for x in dv):
        raise SystemExit("data verification failed: " + str([x for x in dv if x["status"] != "MATCH"]))
    step("3. r_d calibration + integrator validation")
    if a.force or not os.path.exists(os.path.join(RES, "validation", "rd_calibration.json")):
        subprocess.check_call([PY, os.path.join(ROOT, "rebuild", "calibrate_rd.py")])
    if a.force or not os.path.exists(os.path.join(RES, "validation", "cosmo_validation.json")):
        subprocess.check_call([PY, os.path.join(ROOT, "rebuild", "validate_cosmo.py")])
    step("4. expansion-history fits")
    subprocess.check_call([PY, os.path.join(ROOT, "rebuild", "cosmo_runs.py"), "all", str(a.ncores)])
    subprocess.check_call([PY, os.path.join(ROOT, "rebuild", "g9b_bugcheck.py")])
    step("5. analysis")
    subprocess.check_call([PY, os.path.join(ROOT, "rebuild", "analysis.py")])
    step("6. tables and figures")
    subprocess.check_call([PY, os.path.join(ROOT, "rebuild", "make_outputs.py")])
    step("7. REBUILD_RESULTS.md")
    subprocess.check_call([PY, os.path.join(ROOT, "rebuild", "write_results_md.py")])
    step("done")


if __name__ == "__main__":
    main()
