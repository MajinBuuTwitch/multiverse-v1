# Ropewalk Multiverse Empirical Test Suite — Reproducibility & Audit Guide (`README.md`)

This repository (`D:\Argon_Code\Ropewalk`) contains the pre-registered equations, raw observational datasets, numerical analysis pipelines, unit tests, frozen parameter files, figures, and cryptographic OpenTimestamps proofs for the empirical evaluation of the 19-strand Ropewalk Multiverse (`v1`) model.

- **Overall Model Verdict:** **`MODEL FALSIFIED (FAIL)`** (`Pillar 1 T1-L1`: `INCONCLUSIVE`; `Pillar 2 T2-A`: `FAIL`; `Pillar 3 T4b`: `INCONCLUSIVE` [`FAIL` when $n_{\rm test} \ge 6$]; `Pillar 4 T5-A`: `FAIL`).
- **Precedence Clause:** Where `PREREG.md` (`v1.0.2`) and any earlier document disagree, `PREREG.md` (`v1.0.2`) governs. `MULTIVERSE_TESTS_v1.md` is retained as a historical record only.

---

## 1. Cryptographic Time-Ordering Chain (`OpenTimestamps` + `SHA-256`)

To guarantee that the equations and decision rules were locked before any data were downloaded, and that all datasets were locked before any fit was run, three sequential cryptographic hashes and OpenTimestamps (`OTS`) proofs exist in the root directory:

1. **Stage 1 Pre-Registration Freeze (Before Data Download & Before Code):**
   - `PREREG_v4.sha256` (Master SHA-256: `53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b`)
   - `PREREG_v4.sha256.ots` (OpenTimestamps proof covering `PREREG.md`, `MULTIVERSE_STAGE1_EQUATIONS.md`, `ASSUMPTIONS.md`, `EQUATIONS.md`, and `PART1_RESULTS.md`–`PART3_RESULTS.md`, all at `v1.0.2`).
2. **Stage 2 Data Manifest Freeze (Before Any Parameter Fit or Test):**
   - `DATA_MANIFEST.sha256` (Master SHA-256: `73135698afb833e7e95e6a85c55475480132300e29f8b7b42d159c037067896d`)
   - `DATA_MANIFEST.sha256.ots` (OpenTimestamps proof covering every raw dataset in `data/`).
3. **Stage 4 Final Results & Code Freeze:**
   - `RESULTS_v1.sha256`
   - `RESULTS_v1.sha256.ots` (OpenTimestamps proof covering all scripts, tests, frozen JSONs, `results/results.json`, `RESULTS.md`, `MULTIVERSE_PREDICTIONS_PAPER_v2.md`, `DEVIATIONS.md`, `README.md`, and `REVIEW_PACKET.md`).

---

## 2. Directory Structure

```text
D:\Argon_Code\Ropewalk\
├── PREREG.md                         # Governing Stage 1 Pre-Registration (v1.0.2)
├── MULTIVERSE_STAGE1_EQUATIONS.md    # Governing Stage 1 Equations & Derivations (v1.0.2)
├── ASSUMPTIONS.md                    # Explicit Assumptions A1–A19 & Classifications (v1.0.2)
├── EQUATIONS.md                      # Equation Index & Classification Table (v1.0.2)
├── PART1_RESULTS.md                  # Part 1 Derivations (v1.0.2)
├── PART2_RESULTS.md                  # Part 2 Derivations & Coincidence Window (v1.0.2)
├── PART3_RESULTS.md                  # Part 3 Derivations & Kernel Verification (v1.0.2)
├── DEVIATIONS.md                     # Pre-Compute Deviations Log (Stage 2)
├── RESULTS.md                        # Final Technical Report (identical copy in results/RESULTS.md)
├── MULTIVERSE_PREDICTIONS_PAPER_v2.md # Complete Scientific Paper Draft (v2.0.0)
├── REVIEW_PACKET.md                  # Auditor Verification Packet
├── ACTIVITY_LOG.md                   # Append-Only Timestamped Execution Log
├── PREREG_v4.sha256 / .ots           # Stage 1 Pre-Registration Hash & OpenTimestamps Proof
├── DATA_MANIFEST.sha256 / .ots       # Stage 2 Data Freeze Hash & OpenTimestamps Proof
├── RESULTS_v1.sha256 / .ots          # Stage 4 Final Results Hash & OpenTimestamps Proof
├── requirements.txt                  # Pinned Local Virtual Environment Dependencies
├── run_all.py                        # Single-Command End-to-End Reproducibility Runner
├── data/                             # Frozen Observational Datasets (see DATA_MANIFEST.sha256)
│   ├── desi_bao_dr2/                 # DESI DR2 13x13 Gaussian BAO mean & covariance
│   ├── pantheon_plus/                # Pantheon+SH0ES.dat & 1701x1701 STAT+SYS.cov
│   ├── des_dovekie/                  # DES-SN5YR Dovekie HD.csv & STAT+SYS.npz
│   ├── sparc/                        # SPARC 175-galaxy MassModels & Master Table (.mrt)
│   ├── clusters_arxiv/               # Original arXiv e-print sources for cluster mergers
│   ├── registered_priors.json        # Planck 2018 Chen+19 priors & BBN priors
│   ├── MANIFEST.csv                  # Master CSV manifest of all downloaded datasets
│   └── MERGERS.csv                   # 16-cluster dissociative merger catalog (T4b)
├── scripts/                          # Analysis & Execution Modules
│   ├── cosmology.py                  # FLRW, Law 1, CPL, BAO/CMB/SN likelihoods & MCMC engine
│   ├── clusters_t4.py                # T4b & T4a cluster merger classification & fitting
│   ├── sparc_t5.py                   # T5-A, T5-B, T5c 1D elliptic-integral kernel & RAR
│   ├── local_h0_t6.py                # T6 HEALPix N_side=1 Galactic RING regional H0 GLS
│   ├── run_part8_fixes.py            # Stage 2 parameter fixing (F1–F5 -> FIXED_VALUES.json)
│   ├── run_part9_cosmology_tests.py  # Stage 3 cosmological tests (T1, T2, T6, Sec 6)
│   ├── run_part10_astrophysics_and_verdict.py # Stage 3 T4, T5, Holm-Bonferroni & figures
│   ├── freeze_data_manifest.py       # Stage 2 DATA_MANIFEST.sha256 + .ots generator
│   └── freeze_results_v1.py          # Stage 4 RESULTS_v1.sha256 + .ots generator
├── tests/                            # Pre-Fit Gates & Synthetic Unit Tests
│   ├── test_gates_g9.py              # Validation Gates G9-a, G9-b, G9-c, G9-d
│   ├── test_clusters_synthetic.py    # Synthetic recovery tests for T4b & T4a
│   └── test_sparc_synthetic.py       # Synthetic recovery tests for T5 & T6
└── results/                          # All Computed Outputs & Figures
    ├── validation_gates_g9.json
    ├── FREEZE_T1.json .. FREEZE_T6.json
    ├── FIXED_VALUES.json
    ├── part9_cosmology_results.json
    ├── results.json                  # Master machine-readable results file
    ├── RESULTS.md                    # Master human-readable technical report
    └── figures/                      # Publication figures (fig1 .. fig5 .png)
```

---

## 3. Reproducing the Entire Suite (`run_all.py`)

### 3.1 Environment Setup
All code runs inside the local Python 3.13 virtual environment (`D:\Argon_Code\Ropewalk\.venv`) with single-thread BLAS environment headers (`OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1`) and worker count capped at `N_CORES = 12` at `BELOW_NORMAL_PRIORITY_CLASS`:

```powershell
D:\Argon_Code\Ropewalk\.venv\Scripts\python.exe -m pip install -r D:\Argon_Code\Ropewalk\requirements.txt
```

### 3.2 Running the Full Pipeline End-to-End
To execute all validation gates (`G9-a`–`G9-d`), synthetic recovery unit tests (`T4`, `T5`, `T6`), Stage 2 parameter freezes (`F1`–`F5`), Stage 3 cosmological and astrophysical test suites, Holm–Bonferroni multiple-testing control, and figure generation in a single command:

```powershell
D:\Argon_Code\Ropewalk\.venv\Scripts\python.exe D:\Argon_Code\Ropewalk\run_all.py
```

### 3.3 Verifying SHA-256 Hashes
To verify that the pre-registration files (`PREREG_v4.sha256`), raw datasets (`DATA_MANIFEST.sha256`), and final results (`RESULTS_v1.sha256`) match their cryptographic digests:

```powershell
D:\Argon_Code\Ropewalk\.venv\Scripts\python.exe -c "
import hashlib, pathlib
for manifest in ['PREREG_v4.sha256', 'DATA_MANIFEST.sha256', 'RESULTS_v1.sha256']:
    p = pathlib.Path(manifest)
    if p.exists():
        print(f'{manifest}: MASTER SHA256 = {hashlib.sha256(p.read_bytes()).hexdigest()}')
"
```
