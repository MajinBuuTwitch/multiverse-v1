import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import sys
import csv
import json
import time
import ssl
import hashlib
import datetime
import urllib.request
import psutil

try:
    psutil.Process(os.getpid()).nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(ROOT_DIR, "data")

SSL_CTX = ssl._create_unverified_context()

DESI_FILES = [
    "desi_gaussian_bao_ALL_GCcomb_cov.txt",
    "desi_gaussian_bao_ALL_GCcomb_mean.txt",
    "desi_gaussian_bao_BGS_BRIGHT-21.35_GCcomb_cov.txt",
    "desi_gaussian_bao_BGS_BRIGHT-21.35_GCcomb_mean.txt",
    "desi_gaussian_bao_ELG_LOPnotqso_GCcomb_z1.1-1.6_cov.txt",
    "desi_gaussian_bao_ELG_LOPnotqso_GCcomb_z1.1-1.6_mean.txt",
    "desi_gaussian_bao_LRG+ELG_LOPnotqso_GCcomb_cov.txt",
    "desi_gaussian_bao_LRG+ELG_LOPnotqso_GCcomb_mean.txt",
    "desi_gaussian_bao_LRG_GCcomb_z0.4-0.6_cov.txt",
    "desi_gaussian_bao_LRG_GCcomb_z0.4-0.6_mean.txt",
    "desi_gaussian_bao_LRG_GCcomb_z0.6-0.8_cov.txt",
    "desi_gaussian_bao_LRG_GCcomb_z0.6-0.8_mean.txt",
    "desi_gaussian_bao_Lya_GCcomb_cov.txt",
    "desi_gaussian_bao_Lya_GCcomb_mean.txt",
    "desi_gaussian_bao_QSO_GCcomb_cov.txt",
    "desi_gaussian_bao_QSO_GCcomb_mean.txt",
]

PANTHEON_FILES = [
    "Pantheon+SH0ES.dat",
    "Pantheon+SH0ES_STAT+SYS.cov",
    "Pantheon+SH0ES_STATONLY.cov",
    "README",
]

DOVEKIE_FILES = [
    "DES-Dovekie-SN_Likelihood.py",
    "DES-Dovekie_HD.csv",
    "DES-Dovekie_Metadata.csv",
    "STAT+SYS.npz",
    "STATONLY.npz",
    "README.md",
]

SPARC_FILES = [
    "SPARC_Lelli2016c.mrt",
    "MassModels_Lelli2016c.mrt",
]

CLUSTER_ARXIV_PAPERS = [
    ("1503.07675", "Harvey_2015_Science_347_1462"),
    ("1701.05877", "Wittman_2018_ApJ_869_104"),
    ("1210.0014", "Dawson_2013_ApJ_772_131_Bullet_MusketBall"),
    ("astro-ph/0608407", "Clowe_2006_ApJ_648_L109_Bullet"),
    ("1412.1826", "Ng_2015_MNRAS_453_1531_ElGordo"),
    ("1309.5097", "Jee_2014_ApJ_785_20_ElGordo"),
    ("2111.09470", "Cho_2022_ApJ_925_68_A1240"),
    ("1612.01528", "MonteiroOliveira_2017a_MNRAS_466_2614_A1758N"),
    ("1111.4983", "Ragozzine_2012_ApJ_747_18_A1758N"),
    ("1808.00604", "MonteiroOliveira_2018_MNRAS_481_1097_A2034"),
    ("1507.05975", "White_2015_MNRAS_453_2326_A2146"),
    ("1610.04170", "Coleman_2017_MNRAS_464_2469_A2146"),
    ("1103.2772", "Merten_2011_MNRAS_417_333_A2744"),
    ("1301.5007", "Machado_2013_MNRAS_430_3249_A3376"),
    ("1703.08568", "MonteiroOliveira_2017b_MNRAS_468_4566_A3376"),
    ("astro-ph/0412451", "Markevitch_2005_ApJ_627_733_A520"),
    ("1401.3356", "Jee_2014_ApJ_783_78_A520"),
    ("1209.2143", "Clowe_2012_ApJ_758_128_A520"),
    ("1012.1027", "Macario_2011_ApJ_728_82_A754"),
    ("astro-ph/0702649", "Okabe_2008_PASJ_60_345_A754"),
    ("1410.2893", "Dawson_2015_ApJ_805_143_Sausage"),
    ("1410.2898", "Jee_2015_ApJ_802_46_Sausage"),
    ("1110.4391", "Dawson_2012_ApJL_747_L42_MusketBall"),
    ("0806.2320", "Bradac_2008_ApJ_687_959_MACSJ0025"),
    ("1606.00643", "Golovich_2016_ApJ_831_110_MACSJ1149"),
    ("1406.5504", "Rau_2014_MNRAS_443_957_MACSJ1149"),
    ("1509.03310", "Jee_2016_ApJ_817_179_Toothbrush"),
    ("1611.08608", "Golovich_2017_ApJ_838_110_ZwCl0008"),
    ("1711.01347", "Golovich_2019a_ApJS_240_39_MCC"),
    ("1806.10619", "Golovich_2019b_ApJ_882_69_MCC"),
]


def download_file(url, dest_path, version_str):
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (RopewalkStage2/1.0)"})
    with urllib.request.urlopen(req, context=SSL_CTX, timeout=60) as resp:
        content = resp.read()
    with open(dest_path, "wb") as f:
        f.write(content)
    ts = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    sha = hashlib.sha256(content).hexdigest()
    rel_path = os.path.relpath(dest_path, ROOT_DIR).replace("\\", "/")
    print(f"Downloaded {rel_path} ({len(content)} bytes) sha256={sha[:12]}...")
    return {
        "relative_path": rel_path,
        "url": url,
        "version_or_release": version_str,
        "download_timestamp": ts,
        "size_bytes": len(content),
        "sha256": sha,
    }


def write_registered_priors_json():
    """Write the exact pre-registered CMB, BBN, Planck, and DESI Ly-alpha AP numbers from PREREG.md to data/registered_priors.json."""
    priors = {
        "source": "PREREG.md v1.0.2 (Frozen in PREREG_v4.sha256)",
        "desi_dr2_lya_ap_2607_27410": {
            "reference": "DESI Collaboration (2026, DR2 Results IV, arXiv:2607.27410, July 2026) & DESI DR2 Results I (arXiv:2503.14739)",
            "z_eff": 2.33,
            "DH_over_rd": 8.600,
            "sigma_DH_over_rd": 0.066,
            "DM_over_rd": 39.32,
            "sigma_DM_over_rd": 0.33,
            "r_DH_DM_deciding": -0.431,
            "r_DH_DM_sensitivity_zero": 0.0,
        },
        "chen_huang_wang_2019_table1_lcdm": {
            "reference": "Chen, Huang & Wang (2019, JCAP 02 (2019) 028, arXiv:1808.05724, Table 1 LCDM)",
            "mean": [1.7502, 301.471, 2.236],
            "sigma": [0.0046, 0.090, 0.015],
            "corr": [
                [1.00, 0.46, -0.66],
                [0.46, 1.00, -0.33],
                [-0.66, -0.33, 1.00],
            ],
        },
        "chen_huang_wang_2019_table1_wcdm": {
            "reference": "Chen, Huang & Wang (2019, JCAP 02 (2019) 028, arXiv:1808.05724, Table 1 wCDM sensitivity)",
            "mean": [1.7493, 301.462, 2.239],
            "sigma": [0.0046, 0.090, 0.015],
            "corr": [
                [1.00, 0.47, -0.66],
                [0.47, 1.00, -0.34],
                [-0.66, -0.34, 1.00],
            ],
        },
        "bbn_priors": {
            "desi_dr2_luna_deciding": {
                "reference": "Schoneberg (2024, JCAP 06, 006) & DESI Collaboration (2025b, PRD 112, 083515, Eq. 14)",
                "100_omega_b": 2.218,
                "sigma_100_omega_b": 0.055,
            },
            "cooke_2018_sensitivity": {
                "reference": "Cooke, Pettini & Steidel (2018, ApJ 855, 102, arXiv:1710.11129)",
                "100_omega_b": 2.166,
                "sigma_100_omega_b": 0.019,
            },
        },
        "planck_2018_table2_base_lcdm": {
            "reference": "Planck Collaboration (2020, A&A 641, A6, arXiv:1807.06209, Table 2 TT,TE,EE+lowE+lensing)",
            "omega_b": 0.02237,
            "sigma_omega_b": 0.00015,
            "omega_c": 0.1200,
            "sigma_omega_c": 0.0012,
            "H0": 67.36,
            "sigma_H0": 0.54,
            "Omega_m": 0.3153,
            "sigma_Omega_m": 0.0073,
            "Omega_b": 0.04930,
            "sigma_Omega_b": 0.00086,
            "R_Planck_registered": 5.36,
            "sigma_R_Planck_registered": 0.065,
        },
    }
    dest_path = os.path.join(DATA_DIR, "registered_priors.json")
    content = (json.dumps(priors, indent=2) + "\n").encode("utf-8")
    with open(dest_path, "wb") as f:
        f.write(content)
    ts = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    sha = hashlib.sha256(content).hexdigest()
    rel_path = os.path.relpath(dest_path, ROOT_DIR).replace("\\", "/")
    return {
        "relative_path": rel_path,
        "url": "local://PREREG.md#Section-5.1-5.2",
        "version_or_release": "PREREG.md v1.0.2",
        "download_timestamp": ts,
        "size_bytes": len(content),
        "sha256": sha,
    }


def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    records = []

    # 1. DESI DR2 BAO
    for fname in DESI_FILES:
        url = f"https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/{fname}"
        dest = os.path.join(DATA_DIR, "desi_bao_dr2", fname)
        records.append(download_file(url, dest, "CobayaSampler/bao_data master (DESI DR2 2025)"))

    # 2. Pantheon+ and SH0ES
    for fname in PANTHEON_FILES:
        url = f"https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon+_Data/4_DISTANCES_AND_COVAR/{fname}"
        dest = os.path.join(DATA_DIR, "pantheon_plus", fname)
        records.append(download_file(url, dest, "PantheonPlusSH0ES/DataRelease main (Scolnic+22, Brout+22, Riess+22)"))

    # 3. DES-Dovekie
    for fname in DOVEKIE_FILES:
        url = f"https://raw.githubusercontent.com/des-science/DES-SN5YR/main/4_DISTANCES_COVMAT/{fname}"
        dest = os.path.join(DATA_DIR, "des_dovekie", fname)
        records.append(download_file(url, dest, "des-science/DES-SN5YR main (DES-Dovekie Popovic+25 arXiv:2511.07517)"))

    # 4. SPARC
    for fname in SPARC_FILES:
        url = f"https://astroweb.case.edu/SPARC/{fname}"
        dest = os.path.join(DATA_DIR, "sparc", fname)
        records.append(download_file(url, dest, "SPARC v2016c (Lelli, McGaugh & Schombert 2016, AJ 152, 157)"))

    # 5. Registered Priors JSON
    records.append(write_registered_priors_json())

    # 6. Cluster arXiv e-print source packages (tables and LaTeX sources)
    for arxiv_id, label in CLUSTER_ARXIV_PAPERS:
        url = f"https://arxiv.org/e-print/{arxiv_id}"
        safe_id = arxiv_id.replace("/", "_")
        dest = os.path.join(DATA_DIR, "clusters_arxiv", f"{safe_id}_{label}.eprint")
        try:
            records.append(download_file(url, dest, f"arXiv:{arxiv_id} ({label})"))
            time.sleep(0.3)
        except Exception as e:
            print(f"Warning downloading {arxiv_id}: {e}")

    # Write data/MANIFEST.csv
    manifest_csv = os.path.join(DATA_DIR, "MANIFEST.csv")
    with open(manifest_csv, "w", encoding="utf-8", newline="\n") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["relative_path", "url", "version_or_release", "download_timestamp", "size_bytes", "sha256"],
        )
        writer.writeheader()
        for r in records:
            writer.writerow(r)

    print(f"Wrote {manifest_csv} with {len(records)} files.")


if __name__ == "__main__":
    main()
