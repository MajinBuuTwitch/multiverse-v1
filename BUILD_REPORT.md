# MULTIVERSE v1 release repo: build report

Built 2026-11-01 by Claude Code (claude-opus-5-5) from the read-only workspaces D:\Argon_Code\Ropewalk, D:\Blind_Rebuild and D:\Multiverse Review plus RELEASE_KIT_v3.zip. Every action is in `BUILD_LOG.md`. Nothing is public: no Zenodo publication, no GitHub release.

## Summary

| Item | Result |
|:--|:--|
| Repository | https://github.com/MajinBuuTwitch/multiverse-v1 (PRIVATE; created and pushed 2026-11-01; remote main f5ef4d6 had 1,023 files with a path-to-blob map identical to staging; no GitHub release, nothing on Zenodo) |
| Files and size | 1023 files, 208.0 MB (207,970,144 bytes) including this report and BUILD_LOG.md; largest file 2.25 MB; none over 95 MB |
| Manifests verified | 73 manifests, 2211 lines: **0 FAIL**; every non-PASS line is an expected exception (table below) |
| Timestamp proofs | 89 `.ots`/`.ots.bak` files read with `ots info` (no upgrades, no new stamps); every proof commits to its manifest's exact SHA-256 |
| Scrub | no API keys, tokens, passwords, private keys or `.env` files; one Drive folder ID (frozen, shipped); no email except the README contact line and the GitHub no-reply address in BUILD_LOG.md |
| Third-party data | not shipped; re-downloaded today into a temp folder outside the repo: DATA_MANIFEST.sha256 58/58 PASS, rebuild data 10/10 fetched PASS, arXiv sources 44/44 PASS |
| Mock covariance restore | `restore_mock_covariances.py` tested in a temp copy: 120 restored, idempotent rerun, GNU `sha256sum -c` passes all 200 mock lines in both mock sets |
| Snapshot | `D:\MULTIVERSE_RELEASE_SNAPSHOT.zip` (167,979,208 bytes), SHA-256 `54cf9f2d79310cadc68d385e7d96eb80ab266603724d2d0e597a4bc72408ac82` (also in `D:\MULTIVERSE_RELEASE_SNAPSHOT.zip.sha256`); `git archive` of commit `b00925f` (the repo before this report's final snapshot line) |

## Commit identity

Commits are by "Gregory Mandarano" <177835534+MajinBuuTwitch@users.noreply.github.com> (GitHub account MajinBuuTwitch, id 177835534). The Gmail address appears only in the README contact line. Line endings are stored byte-for-byte (`.gitattributes`: `* -text`; repo `core.autocrlf=false`), because the system git default (`autocrlf=true`) would have changed frozen files.

## Layout

`README.md`, `CITATION.cff`, `.zenodo.json` (kit), `LICENSE` (MIT, Gregory Mandarano, 2026), `LICENSE-DOCS` (CC BY 4.0 legal code, creativecommons.org), `.gitattributes`, `restore_mock_covariances.py`, `paper/`, `ropewalk/` (+ `ropewalk/archive/` with `PATH_MAP.txt`), `blind_rebuild/`, `multiverse_review/`, `planner/`, `v2_design/`, `BUILD_LOG.md`, `BUILD_REPORT.md`.

## What I changed in kit files (none of them frozen)

- README.md line 3: the paper path read `paper/MULTIVERSE_V1_PAPER_FINAL.pdf`; the kit ships `paper/MULTIVERSE_V1_PAPER.pdf`, so the path now matches.
- README.md step 4: it pointed at `data_manifest/download_data.py` and `data_manifest/DATA_MANIFEST.sha256`, which don't exist; it now points at `ropewalk/scripts/get_data.py` (run from a copy: it rewrites the frozen `data/MANIFEST.csv` and `data/registered_priors.json`), `ropewalk/DATA_MANIFEST.sha256` and the restore script.
- CITATION.cff `repository-code` set to the GitHub URL; `.zenodo.json` gained a `related_identifiers` entry with the GitHub URL.
- DOI: none supplied, so the placeholders stay: README `[ZENODO DOI]`, CITATION `10.5281/zenodo.XXXXXXX` and `date-released: "YYYY-MM-DD"`. The README contact line already read GregoryMandarano@gmail.com in the kit (there was no `[CONTACT TO ADD]`).

## Exclusions

**Ropewalk:** `.venv/`, `_ORIGINALS/`, every `__pycache__/` (root, scripts, tests, head_to_head, phase3), `FOR_PLANNER/` (duplicate copies), `_TRASH/` (except the 36 files in `archive/`), documentary production material: `assets/` (78 images), `translation/` (captions), `source_multiverse_archival.py`, `fetch_archival_replacements.py`, `fetch_fallback_portraits.py`, `fetch_fallback_portraits_v2.py`, `build_archival_catalog_b.py`, `update_replacements_and_credits.py`, `MASTER_CREDIT_CATALOG.md/.txt`, `MULTIVERSE_ARCHIVAL_CATALOG_B.csv/.md`, `MULTIVERSE_ARCHIVAL_IMAGE_BREAKDOWN.txt`, `MULTIVERSE_PHOTO_CANDIDATES.json`, `MULTIVERSE_PHOTO_GALLERY.html`, `MULTIVERSE_PHOTO_SOURCING.csv`. Third-party data: `data/clusters_arxiv/` (30 e-prints), `data/clusters_arxiv_exact/` (8), `data/des_dovekie/`, `data/desi_bao_dr2/`, `data/pantheon_plus/`, `data/sparc/`. The empty `runs/` folder is not tracked (git keeps no empty folders).

**Kept in `ropewalk/data/` (decision):** `MANIFEST.csv` (Argon's download log, listed in DATA_MANIFEST and RESULTS_v2-v5), `MERGERS.csv` (Argon's curated cluster table, listed in RESULTS_v1-v5) and `registered_priors.json` (the pre-registered prior numbers written from PREREG.md, listed in DATA_MANIFEST and RESULTS_v2-v5). None is a third-party download.

**Mock folders:** the 60 unmodified copies of three third-party covariance files in each mock set (`ropewalk/MOCKS_FOR_ARGON/` and `blind_rebuild/phase3/MOCKS_FOR_ARGON/`, 120 files, 2.18 GB) were left out after checking each was byte-identical to its original (Pantheon+ STAT+SYS.cov abf806d9..., DES-Dovekie STAT+SYS.npz ffd3124b..., DESI ALL_GCcomb_cov.txt 252a1432...). The mocks' own synthetic data vectors are all shipped. Both mock sets ship, because each pipeline's manifests list its own copy (the two sets are byte-identical).

**Blind_Rebuild:** `.venv/`, `rebuild/__pycache__/`, `_TRASH/` (24 stale partial run logs from 06:40 on 2026-10-30, 28 KB, listed in no manifest), third-party data `data/pantheonplus/`, `data/des_dovekie/` (incl. `docs/`), `data/desi_bao_dr2/`, `data/sparc/`, `data/papers/` (952 files, 261 MB: arXiv e-prints, PDFs and the text extracted from them). Kept: `data/download_log.json` and `data/download_log_extra.json` (the rebuild's own download records), all code, results, chains, figures, tables, `t4b_extraction/`, `phase3/SEALED/`, `release_checks/neutrino_rs/`, `CLAUDE.md`.

**Multiverse Review:** nothing excluded; all 9 files ship. Its `results.json` is byte-identical to Argon's Phase 3 `ropewalk/phase3/results.json` (a1e667f5...), not a stray Stage 2 file. Its other inputs (`ANSWER_KEY.json`, `PHASE3_INJECTION_SPEC_SEALED.txt`, `PHASE3_ANALYSIS_PLAN.md`, `PHASE3_INJECTION_v1.sha256`, `PHASE3_RESULTS_v1.sha256`) are byte-identical to their originals.

## Archive (`ropewalk/archive/`)

36 files from Ropewalk `_TRASH`, each matched by SHA-256 to a non-PASS line of RESULTS_v1-v4, PREREG_v2, PREREG_v3, `_TRASH/PREREG_v1` and `_TRASH/PREREG_v3_prelim`, plus the two manifests PREREG_v4 lists by their `_TRASH/` paths (`PREREG_v1.sha256`, `PREREG_v2.sha256`) and the `PREREG_v3_prelim` manifest with its `.ots`/`.ots.bak`. `PATH_MAP.txt` has 51 rows: manifest, line, listed path, archive file, SHA-256, original location. Where two `_TRASH` files had identical bytes, one copy ships (`RESULTS_v3` lines 18 and 19 both map to `MULTIVERSE_PREDICTIONS_PAPER_v3_retired.md`, which is byte-identical to `MULTIVERSE_PREDICTIONS_PAPER_v4_pre_v4fixes_backup.md`).

## Proofs swapped in from the planner kit

- `blind_rebuild/REBUILD_RESULTS_v1.sha256.ots`: the kit's upgraded proof (Bitcoin block 973824); the workspace's pending proof is beside it as `.ots.bak`. The kit's manifest copy is byte-identical to the workspace's (93a154fb...), and the kit's `.ots.bak` equals the workspace proof (9bbb103b...).
- `blind_rebuild/phase3/PHASE3_INJECTION_v1.sha256.ots`: the kit's upgraded proof (blocks 973967, 974019); original as `.ots.bak`. Manifest identical (ca63ae04...), kit `.bak` equals the workspace proof (21f721f5...).
- `blind_rebuild/release_checks/neutrino_rs/NEUTRINO_RS_CHECK.sha256.ots`: the workspace had no proof at all; the kit's proof (blocks 974151, 974152) is placed beside the identical manifest (8fddf928...).

## Verification table

Every `.sha256` manifest in the tree, checked from inside its own folder (falling back to its workspace root, as the original pipelines did). Statuses: PASS; **prefix** = append-only log checked over a frozen byte prefix; **archive** = superseded version in `ropewalk/archive/` via PATH_MAP; **.ots.bak** = a plan proof listed by its pre-upgrade hash; **3rd-party** = excluded third-party data; **home** = a copy of a manifest whose files live in another folder, checked at that folder's exact path; **elsewhere** = a planner manifest whose listed file ships under another name (matched by SHA-256). FAIL: none.

| Manifest | Lines | PASS | prefix | archive | .ots.bak | 3rd-party | home | elsewhere | FAIL |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| `blind_rebuild/DATA_MANIFEST_REBUILD.sha256` | 13 | 0 |  |  |  | 13 |  |  | 0 |
| `blind_rebuild/DATA_MANIFEST_REBUILD_PAPERS.sha256` | 96 | 50 |  |  |  | 46 |  |  | 0 |
| `blind_rebuild/PREREG_v4.sha256` | 26 | 9 | 1 |  |  |  | 16 |  | 0 |
| `blind_rebuild/REBUILD_RESULTS_v1.sha256` | 218 | 217 | 1 |  |  |  |  |  | 0 |
| `blind_rebuild/phase3/PHASE3_INJECTION_v1.sha256` | 201 | 140 | 1 |  |  | 60 |  |  | 0 |
| `blind_rebuild/release_checks/neutrino_rs/NEUTRINO_RS_CHECK.sha256` | 4 | 4 |  |  |  |  |  |  | 0 |
| `multiverse_review/P3_RESCORE.sha256` | 2 | 2 |  |  |  |  |  |  | 0 |
| `multiverse_review/PHASE3_INJECTION_v1.sha256` | 201 | 0 | 1 |  |  | 60 | 140 |  | 0 |
| `multiverse_review/PHASE3_RESULTS_v1.sha256` | 63 | 1 |  |  | 2 |  | 60 |  | 0 |
| `planner/phase3_scoring/PHASE3_SCORING_ADDENDUM_1.sha256` | 1 | 1 |  |  |  |  |  |  | 0 |
| `planner/phase3_scoring/PHASE3_SCORING_ADDENDUM_2.sha256` | 1 | 1 |  |  |  |  |  |  | 0 |
| `planner/phase3_scoring/PHASE3_SCORING_v1.sha256` | 6 | 4 |  |  |  |  |  | 2 | 0 |
| `planner/stamps/NEUTRINO_RS_CHECK.sha256` | 4 | 0 |  |  |  |  |  | 4 | 0 |
| `planner/stamps/PHASE3_INJECTION_v1.sha256` | 201 | 0 | 1 |  |  | 60 | 140 |  | 0 |
| `planner/stamps/PHASE3_SPEC_LOCK_v1.sha256` | 2 | 0 |  |  |  |  |  | 2 | 0 |
| `planner/stamps/REBUILD_RESULTS_v1.sha256` | 218 | 0 | 1 |  |  |  | 217 |  | 0 |
| `ropewalk/DATA_MANIFEST.sha256` | 60 | 2 |  |  |  | 58 |  |  | 0 |
| `ropewalk/HEAD_TO_HEAD_PLAN.sha256` | 3 | 3 |  |  |  |  |  |  | 0 |
| `ropewalk/HEAD_TO_HEAD_RESULTS_v1.sha256` | 162 | 160 |  |  | 2 |  |  |  | 0 |
| `ropewalk/PHASE3_ANALYSIS_PLAN.sha256` | 4 | 4 |  |  |  |  |  |  | 0 |
| `ropewalk/PHASE3_RESULTS_v1.sha256` | 63 | 61 |  |  | 2 |  |  |  | 0 |
| `ropewalk/PREREG_v2.sha256` | 17 | 10 | 1 | 6 |  |  |  |  | 0 |
| `ropewalk/PREREG_v3.sha256` | 22 | 13 | 1 | 8 |  |  |  |  | 0 |
| `ropewalk/PREREG_v4.sha256` | 26 | 23 | 1 | 2 |  |  |  |  | 0 |
| `ropewalk/RESULTS_v1.sha256` | 39 | 34 |  | 5 |  |  |  |  | 0 |
| `ropewalk/RESULTS_v2.sha256` | 56 | 43 |  | 5 |  | 8 |  |  | 0 |
| `ropewalk/RESULTS_v3.sha256` | 60 | 46 |  | 6 |  | 8 |  |  | 0 |
| `ropewalk/RESULTS_v4.sha256` | 62 | 49 | 1 | 4 |  | 8 |  |  | 0 |
| `ropewalk/RESULTS_v5.sha256` | 64 | 56 |  |  |  | 8 |  |  | 0 |
| `ropewalk/archive/PREREG_v1.sha256` | 4 | 0 |  | 4 |  |  |  |  | 0 |
| `ropewalk/archive/PREREG_v2.sha256` | 17 | 10 | 1 | 6 |  |  |  |  | 0 |
| `ropewalk/archive/PREREG_v3_prelim.sha256` | 22 | 13 | 1 | 8 |  |  |  |  | 0 |
| `ropewalk/head_to_head/HEAD_TO_HEAD_PLAN.sha256` | 3 | 3 |  |  |  |  |  |  | 0 |
| `ropewalk/head_to_head/HEAD_TO_HEAD_RESULTS_v1.sha256` | 162 | 160 |  |  | 2 |  |  |  | 0 |
| `ropewalk/phase3/PHASE3_ANALYSIS_PLAN.sha256` | 4 | 4 |  |  |  |  |  |  | 0 |
| `ropewalk/phase3/PHASE3_RESULTS_v1.sha256` | 63 | 61 |  |  | 2 |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e10.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e11.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e12.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e13.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e14.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e15.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e16.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e17.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e18.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e19.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e2.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e20.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e21.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e22.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e23.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e24.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e25.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e26.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e27.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e28.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e29.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e3.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e30.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e31.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e32.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e33.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e34.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e35.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e36.sha256` | 2 | 1 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e4.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e5.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e6.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e7.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e8.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e9.sha256` | 1 | 0 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_DE_FREEZE_F1.sha256` | 3 | 2 | 1 |  |  |  |  |  | 0 |
| `v2_design/MULTIVERSE_V2_FENCE_v1.sha256` | 2 | 2 |  |  |  |  |  |  | 0 |
| **Total (73 manifests)** | 2211 | 1189 | 48 | 54 | 10 | 329 | 573 | 8 | **0** |

**Append-only prefixes.** Recorded in the manifest header: PREREG_v3 ACTIVITY_LOG.md 17,891 B; PREREG_v4 23,542 B; RESULTS_v4 38,017 B; PREREG_v3_prelim 15,814 B; REBUILD_RESULTS_v1 ACTIVITY_LOG_REBUILD.md 16,271 B; PHASE3_INJECTION_v1 SEALED/GENERATION_LOG.md 28,402 B. **Not recorded in the manifest (found by searching every prefix):** PREREG_v2 (and its archive copy) ACTIVITY_LOG.md 10,154 B; every v2 design-log entry manifest, which hashes a prefix of `MULTIVERSE_V2_DESIGN_LOG.txt`:

| Manifest | File | Prefix bytes |
|:--|:--|--:|
| MULTIVERSE_V2_DESIGN_LOG_e2 | MULTIVERSE_V2_DESIGN_LOG.txt | 3,562 |
| MULTIVERSE_V2_DESIGN_LOG_e3 | MULTIVERSE_V2_DESIGN_LOG.txt | 7,220 |
| MULTIVERSE_V2_DESIGN_LOG_e4 | MULTIVERSE_V2_DESIGN_LOG.txt | 8,850 |
| MULTIVERSE_V2_DESIGN_LOG_e5 | MULTIVERSE_V2_DESIGN_LOG.txt | 11,106 |
| MULTIVERSE_V2_DESIGN_LOG_e6 | MULTIVERSE_V2_DESIGN_LOG.txt | 13,272 |
| MULTIVERSE_V2_DESIGN_LOG_e7 | MULTIVERSE_V2_DESIGN_LOG.txt | 15,265 |
| MULTIVERSE_V2_DESIGN_LOG_e8 | MULTIVERSE_V2_DESIGN_LOG.txt | 15,843 |
| MULTIVERSE_V2_DESIGN_LOG_e9 | MULTIVERSE_V2_DESIGN_LOG.txt | 18,856 |
| MULTIVERSE_V2_DESIGN_LOG_e10 | MULTIVERSE_V2_DESIGN_LOG.txt | 22,392 |
| MULTIVERSE_V2_DESIGN_LOG_e11 | MULTIVERSE_V2_DESIGN_LOG.txt | 25,664 |
| MULTIVERSE_V2_DESIGN_LOG_e12 | MULTIVERSE_V2_DESIGN_LOG.txt | 26,684 |
| MULTIVERSE_V2_DESIGN_LOG_e13 | MULTIVERSE_V2_DESIGN_LOG.txt | 28,082 |
| MULTIVERSE_V2_DESIGN_LOG_e14 | MULTIVERSE_V2_DESIGN_LOG.txt | 29,781 |
| MULTIVERSE_V2_DESIGN_LOG_e15 | MULTIVERSE_V2_DESIGN_LOG.txt | 31,001 |
| MULTIVERSE_V2_DESIGN_LOG_e16 | MULTIVERSE_V2_DESIGN_LOG.txt | 33,068 |
| MULTIVERSE_V2_DESIGN_LOG_e17 | MULTIVERSE_V2_DESIGN_LOG.txt | 34,894 |
| MULTIVERSE_V2_DESIGN_LOG_e18 | MULTIVERSE_V2_DESIGN_LOG.txt | 36,498 |
| MULTIVERSE_V2_DESIGN_LOG_e19 | MULTIVERSE_V2_DESIGN_LOG.txt | 38,091 |
| MULTIVERSE_V2_DESIGN_LOG_e20 | MULTIVERSE_V2_DESIGN_LOG.txt | 39,869 |
| MULTIVERSE_V2_DESIGN_LOG_e21 | MULTIVERSE_V2_DESIGN_LOG.txt | 42,226 |
| MULTIVERSE_V2_DESIGN_LOG_e22 | MULTIVERSE_V2_DESIGN_LOG.txt | 45,531 |
| MULTIVERSE_V2_DESIGN_LOG_e23 | MULTIVERSE_V2_DESIGN_LOG.txt | 48,106 |
| MULTIVERSE_V2_DESIGN_LOG_e24 | MULTIVERSE_V2_DESIGN_LOG.txt | 49,513 |
| MULTIVERSE_V2_DESIGN_LOG_e25 | MULTIVERSE_V2_DESIGN_LOG.txt | 51,908 |
| MULTIVERSE_V2_DESIGN_LOG_e26 | MULTIVERSE_V2_DESIGN_LOG.txt | 53,001 |
| MULTIVERSE_V2_DESIGN_LOG_e27 | MULTIVERSE_V2_DESIGN_LOG.txt | 54,030 |
| MULTIVERSE_V2_DESIGN_LOG_e28 | MULTIVERSE_V2_DESIGN_LOG.txt | 55,106 |
| MULTIVERSE_V2_DESIGN_LOG_e29 | MULTIVERSE_V2_DESIGN_LOG.txt | 57,365 |
| MULTIVERSE_V2_DESIGN_LOG_e30 | MULTIVERSE_V2_DESIGN_LOG.txt | 58,751 |
| MULTIVERSE_V2_DESIGN_LOG_e31 | MULTIVERSE_V2_DESIGN_LOG.txt | 60,416 |
| MULTIVERSE_V2_DESIGN_LOG_e32 | MULTIVERSE_V2_DESIGN_LOG.txt | 61,421 |
| MULTIVERSE_V2_DESIGN_LOG_e33 | MULTIVERSE_V2_DESIGN_LOG.txt | 63,923 |
| MULTIVERSE_V2_DESIGN_LOG_e34 | MULTIVERSE_V2_DESIGN_LOG.txt | 64,610 |
| MULTIVERSE_V2_DESIGN_LOG_e35 | MULTIVERSE_V2_DESIGN_LOG.txt | 65,498 |
| MULTIVERSE_V2_DESIGN_LOG_e36 | MULTIVERSE_V2_PAPER_NOTES.txt | 8,788 |
| MULTIVERSE_V2_DE_FREEZE_F1 | MULTIVERSE_V2_DESIGN_LOG.txt | 55,106 |

Verify a prefix with `head -c N file | sha256sum`. These lengths are not stated in the README yet (the planner's README text says it states them).

**Third-party data, checked after downloading into a temp folder outside the repo** (`get_data.py` and `download_data_rebuild.py` run from copies):

- `ropewalk/DATA_MANIFEST.sha256`: 58 PASS, 0 FAIL, 0 not fetched by the pipeline's download script
- `ropewalk/RESULTS_v5.sha256`: 0 PASS, 0 FAIL, 8 not fetched by the pipeline's download script
- `blind_rebuild/DATA_MANIFEST_REBUILD.sha256`: 10 PASS, 0 FAIL, 3 not fetched by the pipeline's download script
- `blind_rebuild/DATA_MANIFEST_REBUILD_PAPERS.sha256`: 0 PASS, 0 FAIL, 46 not fetched by the pipeline's download script
- Sources not covered by either script (RESULTS_v5's 8 `clusters_arxiv_exact` e-prints, the rebuild's arXiv papers and 2 tarballs): fetched from arXiv at the URLs the manifests record (one request per 3 s): 44 PASS, 0 differ, 0 errors. 12 entries have no URL because they are text the rebuild extracted from PDFs (`pdf.txt`, `*_pdftext.txt`, `FigureS*.txt`); they can only be regenerated with the `t4b_extraction/` scripts.
- `DES-Dovekie-SN_Likelihood.py` (rebuild `data/des_dovekie/docs/`) is the one third-party file neither script nor arXiv covers; it is in the DES-SN5YR GitHub repo.

## Bitcoin heights (`ots info`)

Earliest attestation is the block the manifest existed by. "pending only" = calendar attestations, no Bitcoin block yet in the file (ots upgrade would complete them; not done, per the brief).

| Proof | Bitcoin blocks | Note |
|:--|:--|:--|
| `blind_rebuild/DATA_MANIFEST_REBUILD.sha256.ots` | - | pending only |
| `blind_rebuild/DATA_MANIFEST_REBUILD_PAPERS.sha256.ots` | - | pending only |
| `blind_rebuild/PREREG_v4.sha256.ots` | - | pending only |
| `blind_rebuild/REBUILD_RESULTS_v1.sha256.ots` | 973824 |  |
| `blind_rebuild/REBUILD_RESULTS_v1.sha256.ots.bak` | - | pre-upgrade original |
| `blind_rebuild/phase3/PHASE3_INJECTION_v1.sha256.ots` | 973967, 974019 |  |
| `blind_rebuild/phase3/PHASE3_INJECTION_v1.sha256.ots.bak` | - | pre-upgrade original |
| `blind_rebuild/release_checks/neutrino_rs/NEUTRINO_RS_CHECK.sha256.ots` | 974151, 974152 |  |
| `planner/phase3_scoring/PHASE3_SCORING_ADDENDUM_1.sha256.ots` | 974150, 974152 |  |
| `planner/phase3_scoring/PHASE3_SCORING_ADDENDUM_2.sha256.ots` | 974151, 974152 |  |
| `planner/phase3_scoring/PHASE3_SCORING_v1.sha256.ots` | 974088, 974103, 974104 |  |
| `planner/stamps/NEUTRINO_RS_CHECK.sha256.ots` | 974151, 974152 |  |
| `planner/stamps/PHASE3_INJECTION_v1.sha256.ots` | 973967, 974019 |  |
| `planner/stamps/PHASE3_INJECTION_v1.sha256.ots.bak` | - | pre-upgrade original |
| `planner/stamps/PHASE3_SPEC_LOCK_v1.sha256.ots` | 973966, 973973, 974019 |  |
| `planner/stamps/PHASE3_SPEC_LOCK_v1.sha256.ots.bak` | - | pre-upgrade original |
| `planner/stamps/REBUILD_RESULTS_v1.sha256.ots` | 973824 |  |
| `planner/stamps/REBUILD_RESULTS_v1.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/DATA_MANIFEST.sha256.ots` | 973800, 973821 |  |
| `ropewalk/DATA_MANIFEST.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/HEAD_TO_HEAD_PLAN.sha256.ots` | 973880, 973901 |  |
| `ropewalk/HEAD_TO_HEAD_PLAN.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/HEAD_TO_HEAD_RESULTS_v1.sha256.ots` | 973958, 973973 |  |
| `ropewalk/HEAD_TO_HEAD_RESULTS_v1.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/PHASE3_ANALYSIS_PLAN.sha256.ots` | 973969, 973973 |  |
| `ropewalk/PHASE3_ANALYSIS_PLAN.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/PHASE3_RESULTS_v1.sha256.ots` | 974047, 974048 |  |
| `ropewalk/PHASE3_RESULTS_v1.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/PREREG_v3.sha256.ots` | 973793, 973821 |  |
| `ropewalk/PREREG_v3.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/PREREG_v4.sha256.ots` | 973800, 973821 |  |
| `ropewalk/PREREG_v4.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/RESULTS_v1.sha256.ots` | 973822 |  |
| `ropewalk/RESULTS_v1.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/RESULTS_v2.sha256.ots` | 973830, 973864 |  |
| `ropewalk/RESULTS_v2.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/RESULTS_v3.sha256.ots` | 973844, 973864 |  |
| `ropewalk/RESULTS_v3.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/RESULTS_v4.sha256.ots` | 973844, 973864 |  |
| `ropewalk/RESULTS_v4.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/RESULTS_v5.sha256.ots` | 973844, 973864 |  |
| `ropewalk/RESULTS_v5.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/archive/PREREG_v3_prelim.sha256.ots` | 973793, 973821 |  |
| `ropewalk/archive/PREREG_v3_prelim.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/head_to_head/HEAD_TO_HEAD_PLAN.sha256.ots` | 973880, 973901 |  |
| `ropewalk/head_to_head/HEAD_TO_HEAD_PLAN.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/head_to_head/HEAD_TO_HEAD_RESULTS_v1.sha256.ots` | 973958, 973973 |  |
| `ropewalk/head_to_head/HEAD_TO_HEAD_RESULTS_v1.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/phase3/PHASE3_ANALYSIS_PLAN.sha256.ots` | 973969, 973973 |  |
| `ropewalk/phase3/PHASE3_ANALYSIS_PLAN.sha256.ots.bak` | - | pre-upgrade original |
| `ropewalk/phase3/PHASE3_RESULTS_v1.sha256.ots` | 974047, 974048 |  |
| `ropewalk/phase3/PHASE3_RESULTS_v1.sha256.ots.bak` | - | pre-upgrade original |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e10.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e11.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e12.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e13.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e14.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e15.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e16.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e17.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e18.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e19.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e2.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e20.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e21.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e22.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e23.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e24.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e25.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e26.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e27.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e28.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e29.sha256.ots` | 974006, 974008, 974019 |  |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e3.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e30.sha256.ots` | 974015, 974019, 974047 |  |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e31.sha256.ots` | 974015, 974019, 974047 |  |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e32.sha256.ots` | 974087, 974103, 974104 |  |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e33.sha256.ots` | 974088, 974103, 974104 |  |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e34.sha256.ots` | 974088, 974103, 974104 |  |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e35.sha256.ots` | 974151, 974152 |  |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e36.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e4.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e5.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e6.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e7.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e8.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DESIGN_LOG_e9.sha256.ots` | - | pending only |
| `v2_design/MULTIVERSE_V2_DE_FREEZE_F1.sha256.ots` | 974006, 974008, 974019 |  |
| `v2_design/MULTIVERSE_V2_FENCE_v1.sha256.ots` | 973965, 973973, 974019 |  |

**Pending-only proofs (no Bitcoin block in the file):** `blind_rebuild/DATA_MANIFEST_REBUILD.sha256.ots`, `blind_rebuild/DATA_MANIFEST_REBUILD_PAPERS.sha256.ots`, `blind_rebuild/PREREG_v4.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e10.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e11.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e12.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e13.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e14.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e15.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e16.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e17.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e18.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e19.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e2.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e20.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e21.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e22.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e23.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e24.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e25.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e26.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e27.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e28.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e3.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e36.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e4.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e5.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e6.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e7.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e8.sha256.ots`, `v2_design/MULTIVERSE_V2_DESIGN_LOG_e9.sha256.ots`. `blind_rebuild/PREREG_v4.sha256.ots` is the pending copy of Ropewalk's; `ropewalk/PREREG_v4.sha256.ots` is the upgraded proof of the same manifest (blocks 973800, 973821).

## Scrub hits

Report only; no frozen file was edited.

- **Secrets:** none. No API keys, tokens, passwords, private keys, `.env`, `.pem` or credential files anywhere in the tree. Nothing was held back.
- **Google Drive ID:** one, `ropewalk/REVIEW_FINAL.md` line 3 (`1n0J***tl1`), in a frozen file; shipped unchanged as the checklist directs (keep that Drive folder private). Thirteen other "ID-like" hits were arXiv identifiers inside file names (e.g. `1412.1826_Ng_2015...`), not Drive IDs.
- **Email:** `GregoryMandarano@gmail.com` in README.md (the contact line, as instructed); `177835534+MajinBuuTwitch@users.noreply.github.com` in BUILD_LOG.md line 15 (the commit identity). The `c***@wickedai.com` address in the archival scripts is excluded with them. Four "emails" inside compressed `.npz` chains are random bytes, not addresses.
- **Paths (shipped unchanged; the frozen ones would break their hashes if edited):**

#### /home/... (reviewer sandbox): 8 hits in 4 files
- planner/phase3_scoring/PHASE3_SCORING_REPORT.txt: lines 8
- planner/phase3_scoring/score.py: lines 101
- ropewalk/RELEASE_PREP_REPORT.md: lines 491, 498, 500
- ropewalk/REVIEW_FINAL.md: lines 3
#### C:/Python314 (interpreter/DLL): 12 hits in 12 files
- blind_rebuild/ACTIVITY_LOG_REBUILD.md: lines 34
- ropewalk/RELEASE_PREP_REPORT.md: lines 501
- ropewalk/head_to_head/build_report_and_freeze.py: lines 24
- ropewalk/head_to_head/stamp_plan_h2h.py: lines 22
- ropewalk/phase3/build_report_and_freeze.py: lines 24
- ropewalk/phase3/stamp_plan_phase3.py: lines 23
- ropewalk/scripts/freeze_data_manifest.py: lines 22
- ropewalk/scripts/freeze_results_v1.py: lines 22
- ropewalk/scripts/freeze_results_v2.py: lines 22
- ropewalk/scripts/freeze_results_v3.py: lines 22
- ropewalk/scripts/freeze_results_v4.py: lines 23
- ropewalk/scripts/freeze_results_v5.py: lines 23
#### C:/Users/... (user profile): 6 hits in 5 files
- BUILD_LOG.md: lines 6, 13
- blind_rebuild/phase3/SEALED/GENERATION_LOG.md: lines 12
- ropewalk/MULTIVERSE_ARGON_HANDOFF.txt: lines 35
- ropewalk/PAPER_REVIEW_ARGON.md: lines 34
- ropewalk/RELEASE_PREP_REPORT.md: lines 499
#### D:/Argon_Code/Ropewalk (workspace): 326 hits in 42 files
- BUILD_LOG.md: lines 3
- blind_rebuild/ACTIVITY_LOG_REBUILD.md: lines 62
- blind_rebuild/DEVIATIONS_REBUILD.md: lines 52
- blind_rebuild/FREEZE_TIMESTAMP.txt: lines 3, 4, 5, 6
- blind_rebuild/PREREG.md: lines 97
- blind_rebuild/REBUILD_RESULTS.md: lines 359
- blind_rebuild/REBUILD_RULES.md: lines 19
- blind_rebuild/STAGE1_PART1_SECTIONS_ABC.md: lines 4, 23
- blind_rebuild/STAGE1_PART2_SECTIONS_DGH.md: lines 4
- blind_rebuild/STAGE1_PART3_SECTIONS_EFI.md: lines 4
- multiverse_review/PHASE3_ANALYSIS_PLAN.md: lines 18, 26
- ropewalk/ACTIVITY_LOG.md: lines 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27 ... (+86 more)
- ropewalk/ACTIVITY_LOG_RELEASE.md: lines 1, 47, 49, 53, 55, 56, 57, 61, 62
- ropewalk/CREATION_TIME_CHECK.md: lines 50
- ropewalk/FREEZE_TIMESTAMP.txt: lines 3, 4, 5, 6
- ropewalk/FREEZE_TIMING_AUDIT.md: lines 11
- ropewalk/GEMINI.md: lines 3, 18, 19, 24
- ropewalk/HEAD_TO_HEAD_PLAN.md: lines 18, 25
- ropewalk/PAPER_REVIEW_ARGON.md: lines 3, 4, 26, 72, 75, 85
- ropewalk/PAPER_REVIEW_ARGON_v2.md: lines 3, 4, 36
- ropewalk/PHASE3_ANALYSIS_PLAN.md: lines 18, 26
- ropewalk/PREREG.md: lines 97
- ropewalk/README.md: lines 3, 29, 85, 88, 95, 102
- ropewalk/RELEASE_PREP_REPORT.md: lines 39, 342, 487, 513, 533
- ropewalk/REVIEW_RESPONSE.md: lines 4, 7, 150, 157
- ropewalk/REVIEW_RESPONSE_v2.md: lines 142
- ropewalk/REVIEW_RESPONSE_v3.md: lines 81, 116
- ropewalk/SESSION_BOOTSTRAP_HANDOFF.md: lines 1, 12, 20, 45, 50, 65, 66, 71, 94, 95, 98, 99, 103, 108, 111, 114, 115, 116, 122
- ropewalk/STAGE1_PART1_SECTIONS_ABC.md: lines 4, 23
- ropewalk/STAGE1_PART2_SECTIONS_DGH.md: lines 4
- ropewalk/STAGE1_PART3_SECTIONS_EFI.md: lines 4
- ropewalk/archive/STAGE1_PART1_SECTIONS_ABC_v2.md: lines 4, 21
- ropewalk/archive/STAGE1_PART1_SECTIONS_ABC_v3.md: lines 4, 23
- ropewalk/archive/STAGE1_PART2_SECTIONS_DGH_v2.md: lines 4
- ropewalk/archive/STAGE1_PART2_SECTIONS_DGH_v3.md: lines 4
- ropewalk/archive/STAGE1_PART3_SECTIONS_EFI_v2.md: lines 4
- ropewalk/archive/STAGE1_PART3_SECTIONS_EFI_v3.md: lines 4
- ropewalk/head_to_head/ACTIVITY_LOG_H2H.md: lines 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
- ropewalk/head_to_head/HEAD_TO_HEAD_PLAN.md: lines 18, 25
- ropewalk/phase3/ACTIVITY_LOG_PHASE3.md: lines 5, 6, 7, 8, 9, 10, 11, 12, 21, 22, 23, 24, 25, 26, 27, 29, 85, 86
- ropewalk/phase3/PHASE3_ANALYSIS_PLAN.md: lines 18, 26
- ropewalk/phase3/build_report_and_freeze.py: lines 328, 329
#### D:/Blind_Rebuild (workspace): 51 hits in 19 files
- BUILD_LOG.md: lines 3
- blind_rebuild/ACTIVITY_LOG_REBUILD.md: lines 6, 22
- blind_rebuild/DEVIATIONS_REBUILD.md: lines 52
- blind_rebuild/REBUILD_RESULTS.md: lines 359
- blind_rebuild/t4b_extraction/cluster_01.json: lines 10
- blind_rebuild/t4b_extraction/cluster_02.json: lines 10
- blind_rebuild/t4b_extraction/cluster_03.json: lines 10
- blind_rebuild/t4b_extraction/cluster_04.json: lines 10
- blind_rebuild/t4b_extraction/dl_groupC.ps1: lines 8, 11
- blind_rebuild/t4b_extraction/dl_groupE.ps1: lines 11, 20
- blind_rebuild/t4b_extraction/downloads_A.tsv: lines 2, 3, 4, 5
- blind_rebuild/t4b_extraction/downloads_B.tsv: lines 1, 2, 3, 4, 5, 6
- blind_rebuild/t4b_extraction/downloads_C.tsv: lines 2, 3, 4, 5, 6, 7, 8, 9
- blind_rebuild/t4b_extraction/downloads_D.tsv: lines 2, 3, 4, 5
- blind_rebuild/t4b_extraction/downloads_E.tsv: lines 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
- blind_rebuild/t4b_extraction/extract_groupC.py: lines 2
- blind_rebuild/t4b_extraction/pdfcheck_groupC.py: lines 7
- blind_rebuild/t4b_extraction/reextract_groupC.py: lines 2
- planner/phase3_scoring/PHASE3_SCORING_ADDENDUM_2.txt: lines 4
#### D:/Multiverse Review (workspace): 10 hits in 4 files
- BUILD_LOG.md: lines 3, 5, 6, 15
- multiverse_review/P3_RESCORE_REPORT.md: lines 3, 11, 39
- multiverse_review/score_phase3.py: lines 4
- planner/phase3_scoring/PHASE3_SCORING_ADDENDUM_1.txt: lines 2
#### file:/// link: 134 hits in 2 files
- ropewalk/CREATION_TIME_CHECK.md: lines 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36 ... (+7 more)
- ropewalk/RELEASE_PREP_REPORT.md: lines 3, 4, 16, 20, 29, 30, 31, 32, 33, 34, 35, 36, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61 ... (+45 more)


- Hardcoded `C:\Python314\DLLs\libcrypto-3.dll` in Argon's OpenTimestamps helpers (12 files) is a Windows workaround for python-bitcoinlib, not personal data.

## Things I was unsure about, or that need someone else

1. **Ropewalk was being edited when I started** (ACTIVITY_LOG_RELEASE.md 15:45, CREATION_TIME_CHECK.md 15:47; I copied at about 15:58). I rechecked all 977 copies against the sources before committing: none had changed. If Argon writes more release-prep files, they are not in the repo.
2. **`get_data.py` overwrites frozen files** if run inside the repo (`data/MANIFEST.csv` gets new timestamps; `registered_priors.json` is rewritten). The README now says to run it from a copy. It also disables TLS certificate checks (`ssl._create_unverified_context`); the SHA-256 manifest still protects the files' contents.
3. **Data the download scripts don't fetch:** RESULTS_v5's 8 `clusters_arxiv_exact` e-prints, the rebuild's 46 paper files and 3 of its 13 data files. They verify from arXiv (above), but an outsider has no script for them. The checklist's `download_data.py` (item 5, owner C) is still to be written; it should cover these and the PDF-text regeneration.
4. **Per-pipeline README with pinned environment** (README step 5, checklist item 5): `ropewalk/README.md` is Argon's frozen one; `blind_rebuild/` has no README (only `requirements_rebuild.txt` and `run_all_rebuild.py`). Still open.
5. **Model-version placeholders in the README stay:** `[VERSION FROM LOGS]` for Claude Code and for Argon. The rebuild log records `claude-opus-5-5` (ACTIVITY_LOG_REBUILD.md lines 83-84); Argon's workspace records only the name "Gemini 4 Argon" (RELEASE_PREP_REPORT.md section 3). `COMPARISON_ARGON_vs_REBUILD.md` describes the rebuild as "Claude Opus, Antigravity then Claude Code", which the README's credit line should reflect. Left for the planner.
6. **README gaps for the planner:** it says append-only prefix lengths are stated but doesn't list them (table above); it describes four exception cases but verification also needs the manifest-copy case (`blind_rebuild/PREREG_v4.sha256`, `multiverse_review/` copies, `planner/stamps/` copies list files held in other folders) and the planner's `PHASE3_SCORING_v1.sha256`, which lists `p3_results.json` and `ANSWER_KEY.json` that ship as `multiverse_review/results.json` and `blind_rebuild/phase3/SEALED/ANSWER_KEY.json` (same bytes). Adding renamed copies to `planner/phase3_scoring/` would let that manifest pass on its own; I didn't add files to the planner's folder.
7. **`ropewalk/_TRASH/` paths:** PREREG_v3, PREREG_v3_prelim and PREREG_v4 list `_TRASH/PREREG_v1.sha256` and `_TRASH/PREREG_v2.sha256`. I followed the layout (archive/ + PATH_MAP), so a bare `sha256sum -c PREREG_v4.sha256` reports those two lines missing. The alternative is a two-file `ropewalk/_TRASH/` folder so the terminal rulebook manifest passes without PATH_MAP. Your call.
8. **Ropewalk's `.ots.bak` files** exist for every manifest, but only HEAD_TO_HEAD_RESULTS_v1 and PHASE3_RESULTS_v1 list a plan proof by its pre-upgrade hash; the rest are simply backups. Shipped as Argon left them.
9. **FREEZE_T*.json timing audit** (checklist O5) is Argon's; `FREEZE_TIMING_AUDIT.md` and `CREATION_TIME_CHECK.md` ship as they stood at copy time.
10. **The guard change.** Pushing was blocked by the house delete guard (rule "we never push"). On Gregory's instruction I added an exception: plain pushes to `origin` from a top-level `<drive>:\<NAME>_RELEASE` folder or a folder listed in `.claude\hooks\release_push_roots.txt`; force, delete, mirror, prune and `+`/`:` refspecs stay blocked everywhere. Backup and 16 new tests are noted in BUILD_LOG.md.

## Follow-up 2026-11-01: CODE_PUSH_REPO_FIXES

The sections above describe the first build; this section records what changed afterwards. The snapshot line above is the first build's; the snapshot is rebuilt on release day.

- **DOI 10.5281/zenodo.23868218** (reserved; resolves after release day): README line 3 links it; CITATION.cff `doi` set; `date-released` stays a placeholder. `.zenodo.json` unchanged and matches the draft (title, creator "Mandarano, Gregory", affiliation WickedAI, licence cc-by-4.0; no DOI field).
- **Paper:** `paper/MULTIVERSE_V1_PAPER.md` (sha256 778ab424fd6d97965ee835183f9fc38c1ecee97124ef08a315d47ee7175f70f2) and `.pdf` (178b227994a4c88e1f17fa24b2bf2b7f004fec01fc17e86292962ef95aa0fdfe) replaced with Gregory's "MULTIVERSE PAPER FOR RELEASE" copies; both carry the DOI.
- **Credits:** README "Who did what" now has Gregory's exact lines for the rebuild (Claude Opus 5.5, Antigravity then Claude Code) and for Argon (Gemini 4, Google Antigravity, High thinking level).
- **README:** new "Append-only logs" table; data step now points to `download_data.py`.
- **New files:** `download_data.py` (safe downloader, TLS verified, never writes a tracked or existing file, verifies the four data manifests), `.gitignore` (third-party data and restored mock covariances), `blind_rebuild/README_ENVIRONMENT.md` (pinned environment and commands from the rebuild's own records).
- **Download test (fresh clone outside the repo):** 113 files fetched, 113 PASS, 0 FAIL, 0 missing; 12 PDF-extracted text entries have nothing to download. `git status` stayed clean after the download, after `restore_mock_covariances.py` (120 restored) and after a rerun.
- **Verification:** all manifests re-verified on staging: 0 FAIL.
- **Not done: `ropewalk/_TRASH/`.** Copying `PREREG_v1.sha256` and `PREREG_v2.sha256` out of Ropewalk's `_TRASH` was blocked by the house delete guard ("touching _TRASH's contents"); per house rule C1-14 it was not retried another way. PREREG_v4 lines 28-29 still verify through `archive/` and `PATH_MAP.txt`. Note that line 27 (`ACTIVITY_LOG.md`, frozen at a 23,542-byte prefix of a now 40,544-byte log) can never pass a bare `sha256sum -c`; it needs the `head -c` check in the table.
