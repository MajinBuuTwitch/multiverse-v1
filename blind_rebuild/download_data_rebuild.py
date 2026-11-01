"""download_data_rebuild.py -- download every registered dataset and fingerprint it.

Writes data/<group>/<file>, and appends one record per file to data/download_log.json.
DATA_MANIFEST_REBUILD.sha256 is generated from that log by make_manifest() below.
"""
import hashlib, json, os, sys, datetime, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")

# Pinned commits (resolved via the GitHub API on 2026-10-30 just before download)
BAO_COMMIT = "bb0c1c9009dc76d1391300e169e8df38fd1096db"      # CobayaSampler/bao_data
PPLUS_COMMIT = "c447f0fea703fcd0fff57de5000947b5ca81286b"    # PantheonPlusSH0ES/DataRelease
DES_COMMIT = "c9a4fcafc4cbd19bd750dee47fc76194a45c181f"      # des-science/DES-SN5YR

FILES = [
    # (group, filename, url, version string)
    ("desi_bao_dr2", "desi_gaussian_bao_ALL_GCcomb_mean.txt",
     f"https://raw.githubusercontent.com/CobayaSampler/bao_data/{BAO_COMMIT}/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt",
     f"CobayaSampler/bao_data@{BAO_COMMIT}"),
    ("desi_bao_dr2", "desi_gaussian_bao_ALL_GCcomb_cov.txt",
     f"https://raw.githubusercontent.com/CobayaSampler/bao_data/{BAO_COMMIT}/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
     f"CobayaSampler/bao_data@{BAO_COMMIT}"),
    ("pantheonplus", "Pantheon+SH0ES.dat",
     f"https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/{PPLUS_COMMIT}/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES.dat",
     f"PantheonPlusSH0ES/DataRelease@{PPLUS_COMMIT}"),
    ("pantheonplus", "Pantheon+SH0ES_STAT+SYS.cov",
     f"https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/{PPLUS_COMMIT}/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES_STAT%2BSYS.cov",
     f"PantheonPlusSH0ES/DataRelease@{PPLUS_COMMIT}"),
    ("pantheonplus", "README",
     f"https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/{PPLUS_COMMIT}/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/README",
     f"PantheonPlusSH0ES/DataRelease@{PPLUS_COMMIT}"),
    ("des_dovekie", "DES-Dovekie_HD.csv",
     f"https://raw.githubusercontent.com/des-science/DES-SN5YR/{DES_COMMIT}/4_DISTANCES_COVMAT/DES-Dovekie_HD.csv",
     f"des-science/DES-SN5YR@{DES_COMMIT}"),
    ("des_dovekie", "STAT+SYS.npz",
     f"https://raw.githubusercontent.com/des-science/DES-SN5YR/{DES_COMMIT}/4_DISTANCES_COVMAT/STAT%2BSYS.npz",
     f"des-science/DES-SN5YR@{DES_COMMIT}"),
    ("des_dovekie", "README.md",
     f"https://raw.githubusercontent.com/des-science/DES-SN5YR/{DES_COMMIT}/4_DISTANCES_COVMAT/README.md",
     f"des-science/DES-SN5YR@{DES_COMMIT}"),
    ("sparc", "MassModels_Lelli2016c.mrt",
     "https://astroweb.cwru.edu/SPARC/MassModels_Lelli2016c.mrt", "SPARC (Lelli+2016c), astroweb.cwru.edu"),
    ("sparc", "SPARC_Lelli2016c.mrt",
     "https://astroweb.cwru.edu/SPARC/SPARC_Lelli2016c.mrt", "SPARC (Lelli+2016c), astroweb.cwru.edu"),
]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download_all():
    logp = os.path.join(DATA, "download_log.json")
    log = json.load(open(logp)) if os.path.exists(logp) else []
    have = {r["path"] for r in log}
    for group, fn, url, ver in FILES:
        d = os.path.join(DATA, group)
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, fn)
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        if os.path.exists(p):
            if rel in have:
                print("exists, skipping:", p)
                continue
            # file downloaded by an earlier interrupted run (log not written): record with file mtime
            t = datetime.datetime.fromtimestamp(os.path.getmtime(p), datetime.timezone.utc).isoformat(timespec="seconds")
        else:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 blind-rebuild"})
            with urllib.request.urlopen(req, timeout=300) as r, open(p, "wb") as f:
                f.write(r.read())
            t = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
        rec = dict(path=rel, url=url, version=ver,
                   downloaded_utc=t, bytes=os.path.getsize(p), sha256=sha256(p))
        log.append(rec)
        print(rec)
        json.dump(log, open(logp, "w"), indent=1)   # save after every file


if __name__ == "__main__":
    download_all()
