# Blind rebuild: environment and commands

Everything here is taken from the rebuild's own files: `requirements_rebuild.txt`, `ACTIVITY_LOG_REBUILD.md`, `REBUILD_RULES.md`, `run_all_rebuild.py`, `phase3/SEALED/generate_mocks.py`, `phase3/SEALED/GENERATION_LOG.md` and `release_checks/neutrino_rs/LOG.md`. Anything those files don't record is marked **not recorded**. This file was added for the public release (2026-11-01) and is not part of any frozen manifest.

## Environment

| Item | Value | Source |
|:--|:--|:--|
| Operating system | Windows | `requirements_rebuild.txt` header |
| Windows version, CPU, RAM | not recorded | |
| Python | 3.14.7, in a local venv `.venv` | `ACTIVITY_LOG_REBUILD.md` (2026-10-30 06:22:23) |
| Parallel workers | 14 cosmology workers (`--ncores 14`), keeping about 4 threads free | `ACTIVITY_LOG_REBUILD.md` (07:28 hand-over note, 07:34), `REBUILD_RULES.md` |
| Master random seed | 20261030; run *i* (sorted by name) uses 20261030 + 1000 *i*; Monte Carlo checks use the master seed | `run_all_rebuild.py` docstring |

Install, as recorded in `requirements_rebuild.txt`:

```
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements_rebuild.txt
```

Pinned packages (`requirements_rebuild.txt`, exact versions):

| Package | Version | Package | Version |
|:--|:--|:--|:--|
| astropy | 8.0.2 | numpy | 2.5.4 |
| astropy-iers-data | 0.2026.10.19.0.52.1 | opentimestamps | 0.5.0 |
| astropy_healpix | 2.0.1 | opentimestamps-client | 0.8.0 |
| camb | 2.0.5 | packaging | 26.3 |
| certifi | 2026.10.23 | pandas | 3.1.0 |
| charset-normalizer | 3.5.2 | pillow | 13.0.0 |
| contourpy | 1.4.0 | platformdirs | 4.14.0 |
| cycler | 0.12.1 | psutil | 7.2.2 |
| emcee | 3.1.6 | pycryptodomex | 3.24.1 |
| fonttools | 4.68.0 | pyerfa | 2.0.1.5 |
| gitdb | 4.0.12 | pyparsing | 3.3.3 |
| GitPython | 3.2.1 | pypdf | 6.21.4 |
| idna | 3.20 | PySocks | 1.7.1 |
| kiwisolver | 1.5.1 | python-bitcoinlib | 0.12.2 |
| matplotlib | 3.11.2 | python-dateutil | 3.0.0 |
| mpmath | 1.3.0 | PyYAML | 6.0.3 |
| requests | 2.34.2 | scipy | 1.18.1 |
| six | 1.17.0 | smmap | 5.0.3 |
| sympy | 1.14.0 | tzdata | 2026.6 |
| urllib3 | 2.8.0 | | |

Notes recorded with the environment:

- `emcee` is installed but not used: the rebuild uses its own sampler (`rebuild/sampler.py`, DEVIATIONS D4). `camb` is used once, outside any sampling loop, to calibrate r_d (D3) (`requirements_rebuild.txt` header).
- OpenTimestamps on Windows: `ots stamp` failed at import because python-bitcoinlib could not find an OpenSSL library. The recorded fix was to copy `C:\Python314\DLLs\libcrypto-3.dll` to `.venv\ssl_shim\libeay32.dll` and put that folder first on `PATH` for the `ots` call (`ACTIVITY_LOG_REBUILD.md`, 06:28:55).

## Commands

### Phase 1: the blind rebuild

One entry point reproduces the rebuild from the downloaded data (`run_all_rebuild.py` docstring):

```
.venv\Scripts\python.exe run_all_rebuild.py [--force] [--ncores 14]
```

Its steps, each skipped when its output already exists unless `--force` is given:

1. Verify the frozen rulebook against `PREREG_v4.sha256`.
2. Verify the data against `DATA_MANIFEST_REBUILD.sha256` (and `DATA_MANIFEST_REBUILD_PAPERS.sha256`). If `data/pantheonplus/Pantheon+SH0ES.dat` is missing, it runs `download_data_rebuild.py`.
3. Calibrate r_d once with CAMB (`rebuild/calibrate_rd.py`) and validate the integrators (`rebuild/validate_cosmo.py`).
4. Run every expansion-history fit in parallel (`rebuild/cosmo_runs.py all <ncores>`), then `rebuild/g9b_bugcheck.py`.
5. Analysis (`rebuild/analysis.py`) → `results_rebuild/results.json`.
6. Tables and figures (`rebuild/make_outputs.py`).
7. `REBUILD_RESULTS.md`, written mechanically from the results (`rebuild/write_results_md.py`).

Steps recorded in the log but run outside `run_all_rebuild.py`:

- Data manifest: `DATA_MANIFEST_REBUILD.sha256` (13 files), then `ots stamp DATA_MANIFEST_REBUILD.sha256` (06:28). The log doesn't name the script that wrote the manifest; `make_manifest_rebuild.py` in this folder is the one listed in `REBUILD_RESULTS_v1.sha256`.
- Literature manifest: `rebuild/make_papers_manifest.py` → `DATA_MANIFEST_REBUILD_PAPERS.sha256`, then `ots stamp` (07:30, before any T4b statistic).
- Freeze: `rebuild/freeze_results.py` → `REBUILD_RESULTS_v1.sha256`, then `ots stamp` (09:02).
- T4b literature extraction: the scripts in `t4b_extraction/` (`dl_groupC.ps1`, `dl_groupE.ps1`, `extract_groupC.py`, `reextract_groupC.py`, `pdfcheck_groupC.py`, `pdf2txt_groupE.py`, `summarize.py`) under `t4b_extraction/EXTRACTION_PROTOCOL.md`. Their exact invocations are **not recorded**.
- The exact interpreter command line for the three manifest and freeze scripts is **not recorded** beyond the venv above.

### Phase 3: the mock generator

From `phase3/SEALED/generate_mocks.py` (usage line) and `GENERATION_LOG.md`:

```
python generate_mocks.py generate      # writes MOCKS_FOR_ARGON/ + SEALED/ANSWER_KEY.json
python generate_mocks.py selfcheck     # spec section 6 checks, appended to GENERATION_LOG.md
```

Then `hash_phase3.py` hashed every file in `MOCKS_FOR_ARGON/` (196) and `SEALED/` (5) into `phase3/PHASE3_INJECTION_v1.sha256`, followed by `ots stamp` (2026-10-31 06:29). The exact `hash_phase3.py` command line is **not recorded**.

### Release check: neutrino and sound horizon

`release_checks/neutrino_rs/nu_rs_variants.py` imports the frozen `rebuild/cosmo.py` unchanged and writes `nu_rs_variants.json` (`LOG.md`, 2026-11-01 11:35). The exact command line is **not recorded**.

## Rerunning from this repository

- Get the data first with `python download_data.py` from the repository root. That way step 2 finds the files and never calls `download_data_rebuild.py`, which appends to the tracked `data/download_log.json`.
- A rerun rewrites tracked outputs (`results_rebuild/`, `REBUILD_RESULTS.md`). Run it in a copy of the repository and compare the results with the frozen ones through `REBUILD_RESULTS_v1.sha256`.
- The Phase 3 mocks need the omitted covariance copies back: `python restore_mock_covariances.py` from the repository root.
