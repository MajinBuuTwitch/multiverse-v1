# RELEASE PREP: VERIFICATION AND INVENTORY REPORT

- **Action Log:** [ACTIVITY_LOG_RELEASE.md](file:///D:/Argon_Code/Ropewalk/ACTIVITY_LOG_RELEASE.md)
- **Full Line-by-Line Verification Tables (All 668 Manifest Entries):** [RELEASE_PREP_REPORT.md](file:///D:/Argon_Code/Ropewalk/RELEASE_PREP_REPORT.md)

---

## TOP-OF-REPORT SUMMARY: INTEGRITY FAILURES & NOT HELD ITEMS

### A. Terminal / Final Manifests (`DATA_MANIFEST`, `RESULTS_v5`, `HEAD_TO_HEAD_PLAN`, `HEAD_TO_HEAD_RESULTS_v1`, `PHASE3_ANALYSIS_PLAN`, `PHASE3_RESULTS_v1`, `PREREG_v4`)
- **`DATA_MANIFEST.sha256` (`60 / 60` PASS):** **0 failures.**
- **`RESULTS_v5.sha256` (`64 / 64` PASS):** **0 failures.**
- **`HEAD_TO_HEAD_PLAN.sha256` (`3 / 3` PASS):** **0 failures.**
- **`HEAD_TO_HEAD_RESULTS_v1.sha256` (`162 / 162` PASS prior to Step 2 `.ots` upgrade; `160 / 162` after Step 2 `ots upgrade`):**
  - Prior to Step 2 (`ots upgrade`), all `162 / 162` entries matched byte-for-byte.
  - Because `HEAD_TO_HEAD_RESULTS_v1.sha256` lists `HEAD_TO_HEAD_PLAN.sha256.ots` and `head_to_head/HEAD_TO_HEAD_PLAN.sha256.ots` (expected pre-upgrade calendar-only hash `642c160f4e7b1b7f3cde4191ce0a49e687c13eb4b20193da1e3249d9d11d5c97`), upgrading those two `.ots` files in Step 2 changed their active `.ots` hash to `92cd877259c053a989440196e6893420a18bc570fc0445e94b5ab1ba00be0c21` while preserving the exact pre-upgrade `642c160f...` file in [HEAD_TO_HEAD_PLAN.sha256.ots.bak](file:///D:/Argon_Code/Ropewalk/HEAD_TO_HEAD_PLAN.sha256.ots.bak), [head_to_head/HEAD_TO_HEAD_PLAN.sha256.ots.bak](file:///D:/Argon_Code/Ropewalk/head_to_head/HEAD_TO_HEAD_PLAN.sha256.ots.bak), and `_TRASH/ots_pre_release_backup_2026-11-01/`.
- **`PHASE3_ANALYSIS_PLAN.sha256` (`4 / 4` PASS):** **0 failures.**
- **`PHASE3_RESULTS_v1.sha256` (`63 / 63` PASS prior to Step 2 `.ots` upgrade; `61 / 63` after Step 2 `ots upgrade`):**
  - Prior to Step 2 (`ots upgrade`), all `63 / 63` entries matched byte-for-byte.
  - Because `PHASE3_RESULTS_v1.sha256` lists `PHASE3_ANALYSIS_PLAN.sha256.ots` and `phase3/PHASE3_ANALYSIS_PLAN.sha256.ots` (expected pre-upgrade calendar-only hash `304f1f81868ff97c450fdb3f479c9332e248193eb8620e1fdc5a723f142307c8`), upgrading those two `.ots` files in Step 2 changed their active `.ots` hash to `1a59dc42f83cfeb1099fd7b57c162364c406fd1a26c6362c6c56f2a648441f87` while preserving the exact pre-upgrade `304f1f81...` file in [PHASE3_ANALYSIS_PLAN.sha256.ots.bak](file:///D:/Argon_Code/Ropewalk/PHASE3_ANALYSIS_PLAN.sha256.ots.bak), [phase3/PHASE3_ANALYSIS_PLAN.sha256.ots.bak](file:///D:/Argon_Code/Ropewalk/phase3/PHASE3_ANALYSIS_PLAN.sha256.ots.bak), and `_TRASH/ots_pre_release_backup_2026-11-01/`.
- **`PREREG_v4.sha256` (`25 / 26` full-file PASS; `1` full-file FAIL / prefix PASS):**
  - `ACTIVITY_LOG.md`: **FAIL** on full-file SHA-256 (`e8abc5fa69925991515350d43addd305bea94c5791f29b77256572edc8f061bf` at `40,544` bytes vs expected `e9a1dec17d603c23272f1053e766d7eca926f16a973597f44267d04be832657c`); **PASS** on the `23,542`-byte frozen prefix explicitly documented in `PREREG_v4.sha256` line 4 (`# Note (m_v2-8): ACTIVITY_LOG.md is append-only; frozen prefix length = 23542 bytes.`).

### B. Superseded Intermediate Manifests (`RESULTS_v1`–`RESULTS_v4`, `PREREG_v2`–`PREREG_v3`, and `_TRASH/PREREG_v1`–`v3_prelim`)
When evaluated against current active root file paths (which hold the final `v5` documents and `v1.0.2` pre-registration files), the superseded narrative/report files listed in earlier versioned manifests report **FAIL** at the active root path, while every superseded file's exact historical version is preserved intact in `_TRASH/` with a 100% matching SHA-256 (and `ACTIVITY_LOG.md` matches its exact historical byte-prefix in every manifest):

| Manifest | Active-Path Full-File Fails | Files Failing at Active Root Path (All Matched in `_TRASH/` or Prefix) |
|---|---|---|
| [RESULTS_v1.sha256](file:///D:/Argon_Code/Ropewalk/RESULTS_v1.sha256) | `5 / 39` | `DEVIATIONS.md`, `RESULTS.md`, `results/RESULTS.md`, `MULTIVERSE_PREDICTIONS_PAPER_v2.md` (in `_TRASH/`), `REVIEW_PACKET.md` (in `_TRASH/REVIEW_PACKET_withdrawn_v1.md`) |
| [RESULTS_v2.sha256](file:///D:/Argon_Code/Ropewalk/RESULTS_v2.sha256) | `5 / 56` | `DEVIATIONS.md`, `RESULTS.md`, `results/RESULTS.md`, `CLAIMS_CHECK.md`, `MULTIVERSE_PREDICTIONS_PAPER_v3.md` (in `_TRASH/`) |
| [RESULTS_v3.sha256](file:///D:/Argon_Code/Ropewalk/RESULTS_v3.sha256) | `6 / 60` | `DEVIATIONS.md`, `RESULTS.md`, `results/RESULTS.md`, `CLAIMS_CHECK.md`, `MULTIVERSE_PREDICTIONS_PAPER_v3.md` (in `_TRASH/`), `MULTIVERSE_PREDICTIONS_PAPER_v4.md` |
| [RESULTS_v4.sha256](file:///D:/Argon_Code/Ropewalk/RESULTS_v4.sha256) | `5 / 62` | `RESULTS.md`, `results/RESULTS.md`, `CLAIMS_CHECK.md`, `MULTIVERSE_PREDICTIONS_PAPER_v4.md`, `ACTIVITY_LOG.md` (`38,017`-byte prefix matches) |
| [PREREG_v2.sha256](file:///D:/Argon_Code/Ropewalk/PREREG_v2.sha256) | `7 / 17` | `MULTIVERSE_STAGE1_EQUATIONS.md`, `ASSUMPTIONS.md`, `PREREG.md`, `STAGE1_PART1_SECTIONS_ABC.md`, `STAGE1_PART2_SECTIONS_DGH.md`, `STAGE1_PART3_SECTIONS_EFI.md`, `ACTIVITY_LOG.md` (`10,154`-byte prefix matches) |
| [PREREG_v3.sha256](file:///D:/Argon_Code/Ropewalk/PREREG_v3.sha256) | `7 / 22` | `MULTIVERSE_STAGE1_EQUATIONS.md`, `ASSUMPTIONS.md`, `PREREG.md`, `STAGE1_PART1_SECTIONS_ABC.md`, `STAGE1_PART2_SECTIONS_DGH.md`, `STAGE1_PART3_SECTIONS_EFI.md`, `ACTIVITY_LOG.md` (`17,891`-byte prefix matches) |
| [_TRASH/PREREG_v1.sha256](file:///D:/Argon_Code/Ropewalk/_TRASH/PREREG_v1.sha256) | `4 / 4` | `PREREG.md`, `MULTIVERSE_STAGE1_EQUATIONS.md`, `ASSUMPTIONS.md`, `EQUATIONS.md` (all 4 in `_TRASH/*_v1.md`) |
| [_TRASH/PREREG_v3_prelim.sha256](file:///D:/Argon_Code/Ropewalk/_TRASH/PREREG_v3_prelim.sha256) | `7 / 22` | Same 6 Stage 1 markdown files as `PREREG_v3.sha256` (in `_TRASH/*_v3.md`) + `ACTIVITY_LOG.md` (`15,814`-byte prefix matches) |

### C. `NOT HELD` Files (Item 6)
- **0 entries across all manifests held in `D:\Argon_Code\Ropewalk` list external or `SEALED` files.** The Phase 3 `SEALED` truth key folder was never present in `D:\Argon_Code\Ropewalk` and is not referenced in any manifest held in this workspace (`NOT HELD`).

---

## 1. INTEGRITY

### 1.1 Master Table of All Manifests Held in Workspace (Full 64-Character SHA-256)

| Manifest File | Mirror Copy (Byte-Identical) | Manifest Own SHA-256 (64 chars) | Entries | Full-File PASS | Full-File FAIL | Prefix / `_TRASH` Archive Match for Non-PASS |
|---|---|---|---|---|---|---|
| [PREREG_v4.sha256](file:///D:/Argon_Code/Ropewalk/PREREG_v4.sha256) | [FOR_PLANNER/PREREG_v4.sha256](file:///D:/Argon_Code/Ropewalk/FOR_PLANNER/PREREG_v4.sha256) | `53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b` | 26 | 25 | 1 | `1 / 1` (`ACTIVITY_LOG.md` 23,542-byte prefix PASS) |
| [DATA_MANIFEST.sha256](file:///D:/Argon_Code/Ropewalk/DATA_MANIFEST.sha256) | [FOR_PLANNER/DATA_MANIFEST.sha256](file:///D:/Argon_Code/Ropewalk/FOR_PLANNER/DATA_MANIFEST.sha256) | `73135698afb833e7e95e6a85c55475480132300e29f8b7b42d159c037067896d` | 60 | 60 | 0 | — |
| [RESULTS_v1.sha256](file:///D:/Argon_Code/Ropewalk/RESULTS_v1.sha256) | [FOR_PLANNER/RESULTS_v1.sha256](file:///D:/Argon_Code/Ropewalk/FOR_PLANNER/RESULTS_v1.sha256) | `b02000c98008e32ef34265a417e9d7dd724e3ee8472bc3cdf6be494f7477dd4e` | 39 | 34 | 5 | `5 / 5` (exact match in `_TRASH/`) |
| [RESULTS_v2.sha256](file:///D:/Argon_Code/Ropewalk/RESULTS_v2.sha256) | [FOR_PLANNER/RESULTS_v2.sha256](file:///D:/Argon_Code/Ropewalk/FOR_PLANNER/RESULTS_v2.sha256) | `499026f0f39dc64735e5f69bf9113bd4dec05267d907d935aae075a8fdbdcc58` | 56 | 51 | 5 | `5 / 5` (exact match in `_TRASH/`) |
| [RESULTS_v3.sha256](file:///D:/Argon_Code/Ropewalk/RESULTS_v3.sha256) | [FOR_PLANNER/RESULTS_v3.sha256](file:///D:/Argon_Code/Ropewalk/FOR_PLANNER/RESULTS_v3.sha256) | `baec3ff53effc7c11d55b7773b078c0389b707fe0b73790e35a57f5e6b9a93d1` | 60 | 54 | 6 | `6 / 6` (exact match in `_TRASH/`) |
| [RESULTS_v4.sha256](file:///D:/Argon_Code/Ropewalk/RESULTS_v4.sha256) | [FOR_PLANNER/RESULTS_v4.sha256](file:///D:/Argon_Code/Ropewalk/FOR_PLANNER/RESULTS_v4.sha256) | `806d1ef12cb3ed84f681f8bfe5dc3d279e504fb0289aaa086132109187d718ab` | 62 | 57 | 5 | `5 / 5` (`4` in `_TRASH/` + `ACTIVITY_LOG.md` 38,017B prefix) |
| [RESULTS_v5.sha256](file:///D:/Argon_Code/Ropewalk/RESULTS_v5.sha256) | [FOR_PLANNER/RESULTS_v5.sha256](file:///D:/Argon_Code/Ropewalk/FOR_PLANNER/RESULTS_v5.sha256) | `1ce42ac534b6a1766b002f8d064ba76662796227a4094d5f17a0a929c26aa882` | 64 | 64 | 0 | — |
| [HEAD_TO_HEAD_PLAN.sha256](file:///D:/Argon_Code/Ropewalk/HEAD_TO_HEAD_PLAN.sha256) | [head_to_head/HEAD_TO_HEAD_PLAN.sha256](file:///D:/Argon_Code/Ropewalk/head_to_head/HEAD_TO_HEAD_PLAN.sha256) | `60e3e9c67ef00141fd1cfc87cbc3a5968a50fca552bcac8c787cf085bacd3117` | 3 | 3 | 0 | — |
| [HEAD_TO_HEAD_RESULTS_v1.sha256](file:///D:/Argon_Code/Ropewalk/HEAD_TO_HEAD_RESULTS_v1.sha256) | [head_to_head/HEAD_TO_HEAD_RESULTS_v1.sha256](file:///D:/Argon_Code/Ropewalk/head_to_head/HEAD_TO_HEAD_RESULTS_v1.sha256) | `6f3b76f6f3b04e4ed4c664a3e3abace5e62e2b8a9b8bf15eeffbe1ebcea2eb6b` | 162 | 162 (pre-OTS upgrade) / 160 (post) | 0 (pre) / 2 (post) | `2 / 2` (`HEAD_TO_HEAD_PLAN.sha256.ots` pre-upgrade in `.ots.bak`) |
| [PHASE3_ANALYSIS_PLAN.sha256](file:///D:/Argon_Code/Ropewalk/PHASE3_ANALYSIS_PLAN.sha256) | [phase3/PHASE3_ANALYSIS_PLAN.sha256](file:///D:/Argon_Code/Ropewalk/phase3/PHASE3_ANALYSIS_PLAN.sha256) | `4eab04e302dfe06b39362d58c091a132ec4a46c6ad6f2a4a525bcdce3eae2b5c` | 4 | 4 | 0 | — |
| [PHASE3_RESULTS_v1.sha256](file:///D:/Argon_Code/Ropewalk/PHASE3_RESULTS_v1.sha256) | [phase3/PHASE3_RESULTS_v1.sha256](file:///D:/Argon_Code/Ropewalk/phase3/PHASE3_RESULTS_v1.sha256) | `8d4a38dfcbd5d47befd3114b9c269ff63c10c32f20994e459d65da1da45bea08` | 63 | 63 (pre-OTS upgrade) / 61 (post) | 0 (pre) / 2 (post) | `2 / 2` (`PHASE3_ANALYSIS_PLAN.sha256.ots` pre-upgrade in `.ots.bak`) |
| [PREREG_v2.sha256](file:///D:/Argon_Code/Ropewalk/PREREG_v2.sha256) | [_TRASH/PREREG_v2.sha256](file:///D:/Argon_Code/Ropewalk/_TRASH/PREREG_v2.sha256) | `e635658a5727cf98db3675b0d2278e2af995db6ae7b84253200342b005eb6412` | 17 | 10 | 7 | `7 / 7` (`6` in `_TRASH/*_v2.md` + `ACTIVITY_LOG.md` 10,154B prefix) |
| [PREREG_v3.sha256](file:///D:/Argon_Code/Ropewalk/PREREG_v3.sha256) | — | `ab445f9aa11922802f2c8dc7517f6db3e063a579e0a10d92d26bef6eeb348da2` | 22 | 15 | 7 | `7 / 7` (`6` in `_TRASH/*_v3.md` + `ACTIVITY_LOG.md` 17,891B prefix) |
| [_TRASH/PREREG_v1.sha256](file:///D:/Argon_Code/Ropewalk/_TRASH/PREREG_v1.sha256) | — | `f982426a4dc13f9e0662610509e80058b90aab90b6e8a5fa63fbb685ae8378d4` | 4 | 0 | 4 | `4 / 4` (all 4 in `_TRASH/*_v1.md`) |
| [_TRASH/PREREG_v3_prelim.sha256](file:///D:/Argon_Code/Ropewalk/_TRASH/PREREG_v3_prelim.sha256) | — | `4bc12fb61c5b00f07a5cb8c5610e24966bff03a9f3528e7c981365bd1040c3c5` | 22 | 15 | 7 | `7 / 7` (`6` in `_TRASH/*_v3.md` + `ACTIVITY_LOG.md` 15,814B prefix) |
| [data/MANIFEST.csv](file:///D:/Argon_Code/Ropewalk/data/MANIFEST.csv) | — | `0c56b954abd965f988001bab9ae8f8008467f058889af59b6c06ceb2ebb4387f` | 59 | 59 | 0 | — |

---

### 1.2 Per-File Verification by Manifest

*(Note: All 668 individual rows across every manifest—including all 72 chain `.npz` and 72 log `.json` entries in `HEAD_TO_HEAD_RESULTS_v1.sha256` and all 45 universe log `.json` entries in `PHASE3_RESULTS_v1.sha256`—are also saved in full in [RELEASE_PREP_REPORT.md](file:///D:/Argon_Code/Ropewalk/RELEASE_PREP_REPORT.md).)*

#### (1) `PREREG_v4.sha256` (`53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b`)
| # | File | Expected SHA-256 | Recomputed SHA-256 | Status |
|---|---|---|---|---|
| 1 | `00_READ_FIRST.txt` | `75f6d0761bc50bec70e9ab40a23a3c16e7c94a74073e5a3debe062fed692af51` | `75f6d0761bc50bec70e9ab40a23a3c16e7c94a74073e5a3debe062fed692af51` | **PASS** |
| 2 | `MULTIVERSE_ARGON_HANDOFF.txt` | `5623e2d7191b2a5b8cd6e581b136e1cec13d8e6f8aaafd7f86ddf8d17e09e8ed` | `5623e2d7191b2a5b8cd6e581b136e1cec13d8e6f8aaafd7f86ddf8d17e09e8ed` | **PASS** |
| 3 | `SESSION_BOOTSTRAP_HANDOFF.md` | `dd063c6aaf0389d23e8ae721143112e33e37c7864eca25b1478fa6798e09f43a` | `dd063c6aaf0389d23e8ae721143112e33e37c7864eca25b1478fa6798e09f43a` | **PASS** |
| 4 | `MULTIVERSE_TESTS_v1.md` | `5fe5d1d0b749af374d5a7aa5e2e2707275dc39c138197dcda23e91a704b4031a` | `5fe5d1d0b749af374d5a7aa5e2e2707275dc39c138197dcda23e91a704b4031a` | **PASS** |
| 5 | `MULTIVERSE_EQUATION_SHEET_v1.md` | `b779d40d0bd916bfcd3773fe127aa18f75bd9df4b2c2d8d83152a84c2159db43` | `b779d40d0bd916bfcd3773fe127aa18f75bd9df4b2c2d8d83152a84c2159db43` | **PASS** |
| 6 | `MULTIVERSE_DATASETS_v1.md` | `3a93f06180d6bb6d0c8108b8db534057b5a28357b3aa53420df543850f281946` | `3a93f06180d6bb6d0c8108b8db534057b5a28357b3aa53420df543850f281946` | **PASS** |
| 7 | `MULTIVERSE_PREDICTIONS_PAPER_v1.md` | `0cb041958d06c814db97c4a00c6eebac91349c5caba6628c993401d7ef9a88b7` | `0cb041958d06c814db97c4a00c6eebac91349c5caba6628c993401d7ef9a88b7` | **PASS** |
| 8 | `GEMINI.md` | `40d13e8952a10d5af68c080e3565c6ac94353dfdf40eb499924b51d708c7e1bc` | `40d13e8952a10d5af68c080e3565c6ac94353dfdf40eb499924b51d708c7e1bc` | **PASS** |
| 9 | `REVIEW_COLD.md` | `05141d55aea2218ff9428e97e55774dd966038a0c002519872612b066be2c18f` | `05141d55aea2218ff9428e97e55774dd966038a0c002519872612b066be2c18f` | **PASS** |
| 10 | `REVIEW_RESPONSE.md` | `c7c00c28685d9da80d8de5f13373f184956acc2e6db1222a8a963208e27d3b08` | `c7c00c28685d9da80d8de5f13373f184956acc2e6db1222a8a963208e27d3b08` | **PASS** |
| 11 | `REVIEW_V2.md` | `da1cd961ce4602d218849e616e4c4d2707064cc12767e997bc948a14e92b99ce` | `da1cd961ce4602d218849e616e4c4d2707064cc12767e997bc948a14e92b99ce` | **PASS** |
| 12 | `REVIEW_RESPONSE_v2.md` | `4861e0c1c520f7b9c128135efa97b0de3b650ab00fa59402f1b7effc509f5089` | `4861e0c1c520f7b9c128135efa97b0de3b650ab00fa59402f1b7effc509f5089` | **PASS** |
| 13 | `ERRATA_RESPONSE_v2.md` | `09da5931014ee15c72aeb65829cc0da9a1ae7e8b6d1ae7e9a8ba02f0374c1012` | `09da5931014ee15c72aeb65829cc0da9a1ae7e8b6d1ae7e9a8ba02f0374c1012` | **PASS** |
| 14 | `REVIEW_V3.md` | `1044eee027b53b32b3079f2e10f6f5f5f393d21ff0e96f1647f2612cdefa0cf2` | `1044eee027b53b32b3079f2e10f6f5f5f393d21ff0e96f1647f2612cdefa0cf2` | **PASS** |
| 15 | `REVIEW_RESPONSE_v3.md` | `6617fa81c6517870d76d5fb09d2fcd460a9fddf331d73fd414dcf920278c4813` | `6617fa81c6517870d76d5fb09d2fcd460a9fddf331d73fd414dcf920278c4813` | **PASS** |
| 16 | `MULTIVERSE_STAGE1_EQUATIONS.md` | `dbde316bce21f5d31808aeea00870adb1c804b3754a725f1122d92e1739ea632` | `dbde316bce21f5d31808aeea00870adb1c804b3754a725f1122d92e1739ea632` | **PASS** |
| 17 | `ASSUMPTIONS.md` | `26a8f88c646d820ebf69eff83004bfd02ad06b1b6f844ac9cbf3f4ede5b84fa3` | `26a8f88c646d820ebf69eff83004bfd02ad06b1b6f844ac9cbf3f4ede5b84fa3` | **PASS** |
| 18 | `PREREG.md` | `03dc6c5ace3fbb8040fe8d93369c3823be91e5dbefb9526d932631a95da00bad` | `03dc6c5ace3fbb8040fe8d93369c3823be91e5dbefb9526d932631a95da00bad` | **PASS** |
| 19 | `STAGE1_PART1_SECTIONS_ABC.md` | `1ba02d8fcf7727b93f22e305ed7df4dc703715d741c406928b6ccfe52bc478b2` | `1ba02d8fcf7727b93f22e305ed7df4dc703715d741c406928b6ccfe52bc478b2` | **PASS** |
| 20 | `STAGE1_PART2_SECTIONS_DGH.md` | `f9b487619d9b2971c2cf9a65db9f45906f21178f2ee882d6c6363ebb0a7be3a6` | `f9b487619d9b2971c2cf9a65db9f45906f21178f2ee882d6c6363ebb0a7be3a6` | **PASS** |
| 21 | `STAGE1_PART3_SECTIONS_EFI.md` | `fb939176a115556c78cdf5ab67022819bb071d5cb87ddbd585dd9a805a1e3752` | `fb939176a115556c78cdf5ab67022819bb071d5cb87ddbd585dd9a805a1e3752` | **PASS** |
| 22 | `verify_b1_kernel_mc.py` | `2d8bd22c9eba7db7e32dbefc872ce5907fa4d8c3177692daaabb65699d79a501` | `2d8bd22c9eba7db7e32dbefc872ce5907fa4d8c3177692daaabb65699d79a501` | **PASS** |
| 23 | `ACTIVITY_LOG.md` | `e9a1dec17d603c23272f1053e766d7eca926f16a973597f44267d04be832657c` | `e8abc5fa69925991515350d43addd305bea94c5791f29b77256572edc8f061bf` | **FAIL** (Full-file) / **PASS** (23,542B prefix) |
| 24 | `_TRASH/PREREG_v1.sha256` | `f982426a4dc13f9e0662610509e80058b90aab90b6e8a5fa63fbb685ae8378d4` | `f982426a4dc13f9e0662610509e80058b90aab90b6e8a5fa63fbb685ae8378d4` | **PASS** |
| 25 | `_TRASH/PREREG_v2.sha256` | `e635658a5727cf98db3675b0d2278e2af995db6ae7b84253200342b005eb6412` | `e635658a5727cf98db3675b0d2278e2af995db6ae7b84253200342b005eb6412` | **PASS** |
| 26 | `PREREG_v3.sha256` | `ab445f9aa11922802f2c8dc7517f6db3e063a579e0a10d92d26bef6eeb348da2` | `ab445f9aa11922802f2c8dc7517f6db3e063a579e0a10d92d26bef6eeb348da2` | **PASS** |

---

#### (2) `DATA_MANIFEST.sha256` (`73135698afb833e7e95e6a85c55475480132300e29f8b7b42d159c037067896d`) — `60 / 60` PASS
| # | File | Expected & Recomputed SHA-256 (Exact Match) | Status |
|---|---|---|---|
| 1 | `data/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt` | `252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509` | **PASS** |
| 2 | `data/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt` | `9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585` | **PASS** |
| 3 | `data/desi_bao_dr2/desi_gaussian_bao_BGS_BRIGHT-21.35_GCcomb_cov.txt` | `06d7260009fa0030171753fe2f8ece92c5e167da5fdf57f3a98aa2dfe9dc142f` | **PASS** |
| 4 | `data/desi_bao_dr2/desi_gaussian_bao_BGS_BRIGHT-21.35_GCcomb_mean.txt` | `06fc72ca4f4b4a03973c514bf7568c856716ff76a8c05df02e42b93aca769d59` | **PASS** |
| 5 | `data/desi_bao_dr2/desi_gaussian_bao_ELG_LOPnotqso_GCcomb_z1.1-1.6_cov.txt` | `8d1afedca817a80f44c9dd492101d6653f1f353a59da6f24a6bcb0f0d80ad6bc` | **PASS** |
| 6 | `data/desi_bao_dr2/desi_gaussian_bao_ELG_LOPnotqso_GCcomb_z1.1-1.6_mean.txt` | `75d2dd246d2f17145f202fccf80da0bd723a67270a76f83b5be204161e204794` | **PASS** |
| 7 | `data/desi_bao_dr2/desi_gaussian_bao_LRG+ELG_LOPnotqso_GCcomb_cov.txt` | `8c8f5270dc3db24cbecd9aee1e463819a93e4fbfb0805fdf18357c39e5a8e95a` | **PASS** |
| 8 | `data/desi_bao_dr2/desi_gaussian_bao_LRG+ELG_LOPnotqso_GCcomb_mean.txt` | `c34585b9afdb683e68c2522e9715950fd24b63435ceb8a94ae52acd5d2626f4a` | **PASS** |
| 9 | `data/desi_bao_dr2/desi_gaussian_bao_LRG_GCcomb_z0.4-0.6_cov.txt` | `1fc0b21fd34a0e194f3fce2601ea3d1f411b03c7c1006c5b865b9f66991b8740` | **PASS** |
| 10 | `data/desi_bao_dr2/desi_gaussian_bao_LRG_GCcomb_z0.4-0.6_mean.txt` | `86336445497058eee24ecf255e8a7486d8b46d709daa7a919566a58818dbed0c` | **PASS** |
| 11 | `data/desi_bao_dr2/desi_gaussian_bao_LRG_GCcomb_z0.6-0.8_cov.txt` | `16fa8c323f54139ef1249a24f8f9c8663dbac7890d5a6d9c3b97e84ee89847ae` | **PASS** |
| 12 | `data/desi_bao_dr2/desi_gaussian_bao_LRG_GCcomb_z0.6-0.8_mean.txt` | `6d2f38d0727b2aefcd82fdd5a1c6df5a7d34ad8459437c195d575b5ad0c6ab32` | **PASS** |
| 13 | `data/desi_bao_dr2/desi_gaussian_bao_Lya_GCcomb_cov.txt` | `02a049dbf3a1cd391189948516378a694abfd8d5b5cba1a15e97c6c5cf972357` | **PASS** |
| 14 | `data/desi_bao_dr2/desi_gaussian_bao_Lya_GCcomb_mean.txt` | `9b4ab92080d038d0a0a5d76b9abead4e3919d7227e343d1e7feab7103e1f30cb` | **PASS** |
| 15 | `data/desi_bao_dr2/desi_gaussian_bao_QSO_GCcomb_cov.txt` | `7445c6bca01e2732b15ff29e832cc7b682c27d096f3b3ae8a171b63b20e8f6da` | **PASS** |
| 16 | `data/desi_bao_dr2/desi_gaussian_bao_QSO_GCcomb_mean.txt` | `9bffdd0bf27615ab5225e5232fcdf53e16318bf9d06b031a2756d6e89368dadd` | **PASS** |
| 17 | `data/pantheon_plus/Pantheon+SH0ES.dat` | `1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8` | **PASS** |
| 18 | `data/pantheon_plus/Pantheon+SH0ES_STAT+SYS.cov` | `abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc` | **PASS** |
| 19 | `data/pantheon_plus/Pantheon+SH0ES_STATONLY.cov` | `9f177129a332735d3637affd20054080d5260815f3ca0809120c05b2c902297f` | **PASS** |
| 20 | `data/pantheon_plus/README` | `e2b0d262757f01c1794a938c78d32600a21e289b2a0320e5c660c4c6fc9aa87e` | **PASS** |
| 21 | `data/des_dovekie/DES-Dovekie-SN_Likelihood.py` | `78526c0e6013619e3586a5509be504f0bc5f0461d1e55a3d5bec0154353645ff` | **PASS** |
| 22 | `data/des_dovekie/DES-Dovekie_HD.csv` | `2f57019d783eaa976df80a41b0054171a2d994ee9808d715ce850c2df5720aaf` | **PASS** |
| 23 | `data/des_dovekie/DES-Dovekie_Metadata.csv` | `45ad71f8470eaecfe2b386699ef66b26b0717c50f445d5f32941988d32c75388` | **PASS** |
| 24 | `data/des_dovekie/STAT+SYS.npz` | `ffd3124b32148b1372bd95fda9299269f0352a9f8eee02d416c610e38495463b` | **PASS** |
| 25 | `data/des_dovekie/STATONLY.npz` | `ba596d4f035530e53bf5bf2c24359e2dc00ef6449661a30c83bdbe50ae26f6b2` | **PASS** |
| 26 | `data/des_dovekie/README.md` | `7afa1b4c11f465d90eeb0352eb4ca0721f2baa856f545e16ac24af9aa067cf7e` | **PASS** |
| 27 | `data/sparc/SPARC_Lelli2016c.mrt` | `5aa0501f6b0d881fa579030e315e7b5b6ef561a5bd3a07472f9929c7e5728243` | **PASS** |
| 28 | `data/sparc/MassModels_Lelli2016c.mrt` | `9108994b12cc401b94a1768beca61c53ec354779385c9c9cc571049f3043244c` | **PASS** |
| 29 | `data/registered_priors.json` | `3f7b8cab4c726ddeba4eacdcb916ad70f3a92c271a1fab0b0b96f635b60a8615` | **PASS** |
| 30 | `data/clusters_arxiv/1503.07675_Harvey_2015_Science_347_1462.eprint` | `29dd9b68881c24ec895c08f3292fddd16ce8bf44c0e354ab9bf80bf7a8ef30fd` | **PASS** |
| 31 | `data/clusters_arxiv/1701.05877_Wittman_2018_ApJ_869_104.eprint` | `51f5d94d1b761a81c8278c148565259782f20472a37fe1e8b9556810858ca68b` | **PASS** |
| 32 | `data/clusters_arxiv/1210.0014_Dawson_2013_ApJ_772_131_Bullet_MusketBall.eprint` | `66787edc425f2fcf3492a9461476d8f1d43b5cda6127c3244fcbee1afa63e041` | **PASS** |
| 33 | `data/clusters_arxiv/astro-ph_0608407_Clowe_2006_ApJ_648_L109_Bullet.eprint` | `9919979069b417eacc31158825e051cef54e2f50fdd03f6823e09785fa36d204` | **PASS** |
| 34 | `data/clusters_arxiv/1412.1826_Ng_2015_MNRAS_453_1531_ElGordo.eprint` | `167e15415f4d994a2ed05e422e0903a315b29b198137e33ade249bbb31428231` | **PASS** |
| 35 | `data/clusters_arxiv/1309.5097_Jee_2014_ApJ_785_20_ElGordo.eprint` | `cee8d6dd9aeda81efc5c1d6dee43cf74923256ca9c5b89f46fb7c76a17a50335` | **PASS** |
| 36 | `data/clusters_arxiv/2111.09470_Cho_2022_ApJ_925_68_A1240.eprint` | `1d78369c3582e7cf7fc95eedc2f59f856ea2adcec719fca38233b1b8b6b2fb36` | **PASS** |
| 37 | `data/clusters_arxiv/1612.01528_MonteiroOliveira_2017a_MNRAS_466_2614_A1758N.eprint` | `f3a63714f072c50356d2a8cc3dd447c8523bb11a02b7ca9695d8c997d64fdecd` | **PASS** |
| 38 | `data/clusters_arxiv/1111.4983_Ragozzine_2012_ApJ_747_18_A1758N.eprint` | `a5f76a50e6834061e2b56b770b69912243b2f5dc85e6304ef8c5f39ffb5b2d62` | **PASS** |
| 39 | `data/clusters_arxiv/1808.00604_MonteiroOliveira_2018_MNRAS_481_1097_A2034.eprint` | `9bc1da034626e080254df9c90ec7138824441b265ebd778096233868d14a80c7` | **PASS** |
| 40 | `data/clusters_arxiv/1507.05975_White_2015_MNRAS_453_2326_A2146.eprint` | `b7fb774d93aacb73dd7c83ba433a4f6b003abaa5617c52b962e08a89cde83ca5` | **PASS** |
| 41 | `data/clusters_arxiv/1610.04170_Coleman_2017_MNRAS_464_2469_A2146.eprint` | `22280031f2c4c7f3239f0fadec54d8daeec44a9e5da4b2722ab8f4631582767f` | **PASS** |
| 42 | `data/clusters_arxiv/1103.2772_Merten_2011_MNRAS_417_333_A2744.eprint` | `11fba7e09686dd123fa056c482b177d094ee0debbb9eaeccf6a8a38eca138022` | **PASS** |
| 43 | `data/clusters_arxiv/1301.5007_Machado_2013_MNRAS_430_3249_A3376.eprint` | `8cc047800592bc2859b31fff08932dcbd8d61f4be18945f0c5f82e3729f1e846` | **PASS** |
| 44 | `data/clusters_arxiv/1703.08568_MonteiroOliveira_2017b_MNRAS_468_4566_A3376.eprint` | `c9c97feb2c4f918163d52dbc04400821965dceb4fb36a6ccc5783ff18d91c797` | **PASS** |
| 45 | `data/clusters_arxiv/astro-ph_0412451_Markevitch_2005_ApJ_627_733_A520.eprint` | `b1a35e08d6ffbd20e484fb23299ed94f7e50eed9427c1313b089535380f59a0e` | **PASS** |
| 46 | `data/clusters_arxiv/1401.3356_Jee_2014_ApJ_783_78_A520.eprint` | `a464cdeb6cb99a73b8498a0489c86bbdffef928d10b46703e6f274e24d8927df` | **PASS** |
| 47 | `data/clusters_arxiv/1209.2143_Clowe_2012_ApJ_758_128_A520.eprint` | `12bdb6f566b3dd4a7c89f9d96d9e7baaa38be7f9c49dad3d2e8953fbed80cdc9` | **PASS** |
| 48 | `data/clusters_arxiv/1012.1027_Macario_2011_ApJ_728_82_A754.eprint` | `c23a9a23cddeaef4f1f11e59d4fb94fb9302e20770790f287b7c2946163f7f12` | **PASS** |
| 49 | `data/clusters_arxiv/astro-ph_0702649_Okabe_2008_PASJ_60_345_A754.eprint` | `c938926eab0be0dc60744df56e6de873295d54af0b4b97e2198bbffd781a8933` | **PASS** |
| 50 | `data/clusters_arxiv/1410.2893_Dawson_2015_ApJ_805_143_Sausage.eprint` | `2ec3ca0a80f26caae83440a27441856c2fef14d2a4a55d7cbbea809f5fe7068b` | **PASS** |
| 51 | `data/clusters_arxiv/1410.2898_Jee_2015_ApJ_802_46_Sausage.eprint` | `59222128d9f9d80f3e0af5938fc909ec86da82123826b4313daa206a0315c8f2` | **PASS** |
| 52 | `data/clusters_arxiv/1110.4391_Dawson_2012_ApJL_747_L42_MusketBall.eprint` | `5c14f294d01cb7f19aaa533cd991df937bb35b91d1e6f325f1fcc737fb225cb8` | **PASS** |
| 53 | `data/clusters_arxiv/0806.2320_Bradac_2008_ApJ_687_959_MACSJ0025.eprint` | `deb891390496b73a6b02f1c0b67d5d999d25910416cc1da6243a113f6eb0d8b5` | **PASS** |
| 54 | `data/clusters_arxiv/1606.00643_Golovich_2016_ApJ_831_110_MACSJ1149.eprint` | `a5b21f31e74c797c36416caace48b22fcdcb17b96a8fb90575c8509997f887a4` | **PASS** |
| 55 | `data/clusters_arxiv/1406.5504_Rau_2014_MNRAS_443_957_MACSJ1149.eprint` | `2a7a2d9df191d720d1cf587a2c62e24d3c9884a4638c400532c1fe9dc08adf67` | **PASS** |
| 56 | `data/clusters_arxiv/1509.03310_Jee_2016_ApJ_817_179_Toothbrush.eprint` | `29774a6aed544beff4e73d8d3d3f6b5ff97c4e132ed3d7f8e9f6e8bb2f3b5da6` | **PASS** |
| 57 | `data/clusters_arxiv/1611.08608_Golovich_2017_ApJ_838_110_ZwCl0008.eprint` | `328773f837520b19420f89187bba67fd8e217f52dc57657946e0a0c00afe7ffb` | **PASS** |
| 58 | `data/clusters_arxiv/1711.01347_Golovich_2019a_ApJS_240_39_MCC.eprint` | `668cb63eb861e5e676d64a21a561ec535522b444418fc7bb41c49d68f2540714` | **PASS** |
| 59 | `data/clusters_arxiv/1806.10619_Golovich_2019b_ApJ_882_69_MCC.eprint` | `fc0e4037bce6ec454344a62b512557630494549ca1deccc099c03c36d767a9ad` | **PASS** |
| 60 | `data/MANIFEST.csv` | `0c56b954abd965f988001bab9ae8f8008467f058889af59b6c06ceb2ebb4387f` | **PASS** |

---

#### (3) `RESULTS_v1.sha256` through `RESULTS_v5.sha256`
- **`RESULTS_v1.sha256`:** `b02000c98008e32ef34265a417e9d7dd724e3ee8472bc3cdf6be494f7477dd4e` (`34 / 39` PASS at root; `5` superseded narrative files in `_TRASH/`)
- **`RESULTS_v2.sha256`:** `499026f0f39dc64735e5f69bf9113bd4dec05267d907d935aae075a8fdbdcc58` (`51 / 56` PASS at root; `5` superseded narrative files in `_TRASH/`)
- **`RESULTS_v3.sha256`:** `baec3ff53effc7c11d55b7773b078c0389b707fe0b73790e35a57f5e6b9a93d1` (`54 / 60` PASS at root; `6` superseded narrative files in `_TRASH/`)
- **`RESULTS_v4.sha256`:** `806d1ef12cb3ed84f681f8bfe5dc3d279e504fb0289aaa086132109187d718ab` (`57 / 62` PASS at root; `4` superseded narrative files in `_TRASH/` + `ACTIVITY_LOG.md` `38,017`-byte prefix match)
- **`RESULTS_v5.sha256`:** `1ce42ac534b6a1766b002f8d064ba76662796227a4094d5f17a0a929c26aa882` (**`64 / 64` PASS**)

All 64 files in `RESULTS_v5.sha256` (which supersedes `RESULTS_v1`–`v4` and chains their manifest hashes):
| # | File | Expected & Recomputed SHA-256 (`RESULTS_v5.sha256`) | `v1` | `v2` | `v3` | `v4` | `v5` |
|---|---|---|---|---|---|---|---|
| 1 | `PREREG_v4.sha256` | `53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b` | PASS | PASS | PASS | PASS | **PASS** |
| 2 | `DATA_MANIFEST.sha256` | `73135698afb833e7e95e6a85c55475480132300e29f8b7b42d159c037067896d` | PASS | PASS | PASS | PASS | **PASS** |
| 3 | `RESULTS_v1.sha256` | `b02000c98008e32ef34265a417e9d7dd724e3ee8472bc3cdf6be494f7477dd4e` | — | PASS | PASS | PASS | **PASS** |
| 4 | `RESULTS_v2.sha256` | `499026f0f39dc64735e5f69bf9113bd4dec05267d907d935aae075a8fdbdcc58` | — | — | PASS | PASS | **PASS** |
| 5 | `RESULTS_v3.sha256` | `baec3ff53effc7c11d55b7773b078c0389b707fe0b73790e35a57f5e6b9a93d1` | — | — | — | PASS | **PASS** |
| 6 | `RESULTS_v4.sha256` | `806d1ef12cb3ed84f681f8bfe5dc3d279e504fb0289aaa086132109187d718ab` | — | — | — | — | **PASS** |
| 7 | `REVIEW_FINAL.md` | `e932926a7096704cc5fe0b6c347683f7f48d72323708f8457adb43ec03077481` | — | PASS | PASS | PASS | **PASS** |
| 8 | `COMPARISON_ARGON_vs_REBUILD.md` | `500cb5a05c0a118e4a5caeafbda41ae82cd9638f9a54da816c90880b4fdd5862` | — | — | PASS | PASS | **PASS** |
| 9 | `PREREG.md` | `03dc6c5ace3fbb8040fe8d93369c3823be91e5dbefb9526d932631a95da00bad` | PASS | PASS | PASS | PASS | **PASS** |
| 10 | `MULTIVERSE_STAGE1_EQUATIONS.md` | `dbde316bce21f5d31808aeea00870adb1c804b3754a725f1122d92e1739ea632` | PASS | PASS | PASS | PASS | **PASS** |
| 11 | `ASSUMPTIONS.md` | `26a8f88c646d820ebf69eff83004bfd02ad06b1b6f844ac9cbf3f4ede5b84fa3` | PASS | PASS | PASS | PASS | **PASS** |
| 12 | `DEVIATIONS.md` | `047c9629fa56babb5b3b7974bd60c449ecf756d7879743a9127a97f9b48641d6` | FAIL (`93e3740a...`) | FAIL (`1e0aca1b...`) | FAIL (`44878bc7...`) | PASS | **PASS** |
| 13 | `RESULTS.md` | `2f88422ec20f526a78aa4e555c584c35881ae40279fc354373674f54652ad92c` | FAIL (`00da0f9e...`) | FAIL (`0cca007b...`) | FAIL (`d3d64a70...`) | FAIL (`6aaf987b...`) | **PASS** |
| 14 | `results/RESULTS.md` | `2f88422ec20f526a78aa4e555c584c35881ae40279fc354373674f54652ad92c` | FAIL (`00da0f9e...`) | FAIL (`0cca007b...`) | FAIL (`d3d64a70...`) | FAIL (`6aaf987b...`) | **PASS** |
| 15 | `MULTIVERSE_PREDICTIONS_PAPER_v4.md` | `a0744ca70efea8a494351da57480b40d373791ed7acb3bb26d01e56c37a7574a` | — (`v2`: FAIL `34141def...`) | — (`v3`: FAIL `3f14f3ee...`) | FAIL (`b460e92f...`) | FAIL (`308b999a...`) | **PASS** |
| 16 | `CLAIMS_CHECK.md` | `7f4f930599c9d42828da3abd55de4ea837339c04e6f3c2b8eb2f1bcd96aca3bd` | — (`REVIEW_PACKET`: FAIL `015faf4a...`) | FAIL (`21c721c1...`) | FAIL (`7557e359...`) | FAIL (`096c7f37...`) | **PASS** |
| 17 | `ACTIVITY_LOG.md` | `e8abc5fa69925991515350d43addd305bea94c5791f29b77256572edc8f061bf` | — | — | — | FAIL (`85527a2b...`, 38,017B prefix) | **PASS** |
| 18 | `README.md` | `93fe2b3bb698002d8524be863eb5bb0b4df66163f5f4a57b90662ca3665a7fd5` | PASS | PASS | PASS | PASS | **PASS** |
| 19 | `requirements.txt` | `c5fd64e383241605a00d11573a37a2c220a44d53f287a071072e37b13bab8b1a` | PASS | PASS | PASS | PASS | **PASS** |
| 20 | `run_all.py` | `a0b1c8992a6074b3273076c1edf3f2054ae42f504b73a6569d737170ee0b3d02` | PASS | PASS | PASS | PASS | **PASS** |
| 21 | `data/MERGERS.csv` | `71898466b798c8ba442aa88b7e3ceb326c07720c295ebaded4d47c99a60d3f67` | PASS | PASS | PASS | PASS | **PASS** |
| 22 | `data/MANIFEST.csv` | `0c56b954abd965f988001bab9ae8f8008467f058889af59b6c06ceb2ebb4387f` | — | PASS | PASS | PASS | **PASS** |
| 23 | `data/registered_priors.json` | `3f7b8cab4c726ddeba4eacdcb916ad70f3a92c271a1fab0b0b96f635b60a8615` | — | PASS | PASS | PASS | **PASS** |
| 24 | `data/clusters_arxiv_exact/1510.03486_Jee_2016_ApJ_817_179_Toothbrush.eprint` | `e044456e9d233103e1611197ff978c3c06626b84f5b275feb163bf8d744a4e77` | — | PASS | PASS | PASS | **PASS** |
| 25 | `data/clusters_arxiv_exact/1605.07595_MonteiroOliveira_2017a_MNRAS_466_2614_A1758N.eprint` | `1b5d4adbc841013e43f7a6545a33c0f97739ff924a75cd32106fb4da9426ddbd` | — | PASS | PASS | PASS | **PASS** |
| 26 | `data/clusters_arxiv_exact/1608.01329_Golovich_2016_ApJ_831_110_MACSJ1149.eprint` | `4818d9a907c9d408ec1afb40afddafe740b41a758ec096a8659a3c6fd464fa51` | — | PASS | PASS | PASS | **PASS** |
| 27 | `data/clusters_arxiv_exact/1609.06765_Coleman_2017_MNRAS_464_2469_A2146.eprint` | `4073b89bbee9793b6eec4f22d46da0c0f4e93841e9aa20d15c09762e16d3e025` | — | PASS | PASS | PASS | **PASS** |
| 28 | `data/clusters_arxiv_exact/1612.07935_MonteiroOliveira_2017b_MNRAS_468_4566_A3376.eprint` | `31d39155c4c6f796dba1cdf93e4c9caf6f54f0263496f1fc8a2493da5f6d3367` | — | PASS | PASS | PASS | **PASS** |
| 29 | `data/clusters_arxiv_exact/1703.04803_Golovich_2017_ApJ_838_110_ZwCl0008.eprint` | `3d2ef0cc185b489293dfb136dbd3693af257ba4b1b46e6b0db27136d8d592e9f` | — | PASS | PASS | PASS | **PASS** |
| 30 | `data/clusters_arxiv_exact/1808.09449_MonteiroOliveira_2018_MNRAS_481_1097_A2034.eprint` | `c1c3b85dfad35683496b6a83e88df0a5b0248e92446606619e35209996088c10` | — | PASS | PASS | PASS | **PASS** |
| 31 | `data/clusters_arxiv_exact/2109.06879_Cho_2022_ApJ_925_68_A1240.eprint` | `998bc07c1b0fe181902418914789908c750d21ebfdcb8713b0ff85f68c13d698` | — | PASS | PASS | PASS | **PASS** |
| 32 | `results/validation_gates_g9.json` | `392b91cb42fe0b4219664a8a676636002280cb6f4348aa2e384890f1b363e56e` | PASS | PASS | PASS | PASS | **PASS** |
| 33 | `results/validation_gates_g9_final.json` | `624559ccf5896ade9e1429e409c914da5ff5544036c6379fba9b9b72a011a53a` | — | PASS | PASS | PASS | **PASS** |
| 34 | `results/FREEZE_T1.json` | `bfc4e2531f1cc1ac2d2853253564676227ad786186c2e0039b18f86630cfc0d1` | PASS | PASS | PASS | PASS | **PASS** |
| 35 | `results/FREEZE_T2.json` | `ea12e85f5a9334cb8495d1ad0f52bdc024c5efb329990bddcd12363abdc7d970` | PASS | PASS | PASS | PASS | **PASS** |
| 36 | `results/FREEZE_T4.json` | `ba0312c8fd604668c01b5ba004ca7c329b641b7e780868f1d3600a533b63141b` | PASS | PASS | PASS | PASS | **PASS** |
| 37 | `results/FREEZE_T5.json` | `42555e320386a4eb9fdedb8a4cc5592594d066e0162b00efbb20726dac768743` | PASS | PASS | PASS | PASS | **PASS** |
| 38 | `results/FREEZE_T6.json` | `30125149716c3b1de0932ac3e7b247f5ec5f1a04316f77d025cbb6b488478e3a` | PASS | PASS | PASS | PASS | **PASS** |
| 39 | `results/FIXED_VALUES.json` | `c95b127261b355268a282b90179d141e0f147aaf3670d785f3a32cdc48db2059` | PASS | PASS | PASS | PASS | **PASS** |
| 40 | `results/part9_cosmology_results.json` | `bb573febb85322f7493c1f5f7dd017f1917b0f3cd04d0a37a38d41bdf31aefe0` | PASS | PASS | PASS | PASS | **PASS** |
| 41 | `results/results.json` | `7ce8cdb322c14a1fe0c2ca89797b943e81fa523e2839cc5c6b3d7da3f8ae22e2` | PASS | PASS | PASS | PASS | **PASS** |
| 42 | `results/figures/fig1_t1_unwinding_vs_desi.png` | `5b55026c57be0df425d023e38365097369cd0b3f64ce5ba16e4c2c15b1b268cd` | PASS | PASS | PASS | PASS | **PASS** |
| 43 | `results/figures/fig2_t2_strand_budget_tension.png` | `060360082a6b85d93fbf284f625304bdbe0c0b6e6d6cde2f6c58c748ee44edb4` | PASS | PASS | PASS | PASS | **PASS** |
| 44 | `results/figures/fig3_t4b_cluster_mergers.png` | `06c2c8a4cebaf317328dc281497e0d008c2aa31966d0502ab8e7e20c83747fe2` | PASS | PASS | PASS | PASS | **PASS** |
| 45 | `results/figures/fig4_t5_sparc_rotation_curves.png` | `94848543d6cc5ee839fa02f05345e1cb704a55585bc95d64ade15ce78af53b1b` | PASS | PASS | PASS | PASS | **PASS** |
| 46 | `results/figures/fig5_t6_regional_h0_and_coincidence.png` | `ef3a43422d86d4e359809ac39ff82a8d66bed2269c8e23a2517defd5d24ba87c` | PASS | PASS | PASS | PASS | **PASS** |
| 47 | `scripts/get_data.py` | `04fcc4bc18750011a6ea2893407d3ce018f06e39d8f6a3b89e73a7a835d9cdf2` | PASS | PASS | PASS | PASS | **PASS** |
| 48 | `scripts/cosmology.py` | `998296f8916f194ecd0e3974861810425baa3903dc58ea1a624bd0a0c6657f92` | PASS | PASS | PASS | PASS | **PASS** |
| 49 | `scripts/clusters_t4.py` | `b07659e7781322c38577839185c41e542ad162121d187fe73153ca8f5d23bfdd` | PASS | PASS | PASS | PASS | **PASS** |
| 50 | `scripts/sparc_t5.py` | `f992b875a087123f2118086bb8c9105e56d56f671e5926778e136a9bad350642` | PASS | PASS | PASS | PASS | **PASS** |
| 51 | `scripts/local_h0_t6.py` | `c891441736f8971e14a2fb75274e4aa55b6948e139fd6b1198296fb2de6de9c4` | PASS | PASS | PASS | PASS | **PASS** |
| 52 | `scripts/run_part8_fixes.py` | `0bd1702119f1348e12ff796fa2bd16d133f349c70cb4ff0c04f51f5f736d12e8` | PASS | PASS | PASS | PASS | **PASS** |
| 53 | `scripts/run_part9_cosmology_tests.py` | `8da8e3cbcdfeeb6a1b8be53c4730920419411fcfe74250e9b325e4639e818eb5` | PASS | PASS | PASS | PASS | **PASS** |
| 54 | `scripts/run_part10_astrophysics_and_verdict.py` | `2b27fe212f6912392e67939b1c262fb0dd73a32d34aea7c2b9865dc8ee198c4f` | PASS | PASS | PASS | PASS | **PASS** |
| 55 | `scripts/freeze_data_manifest.py` | `8b3eb42c59bdc0f087bf7c18794470e4d2bc44b1e1927eb5709f349c35034330` | PASS | PASS | PASS | PASS | **PASS** |
| 56 | `scripts/freeze_results_v1.py` | `07b27475bbaa4759d098febd00d9f2e11b49743f84da7431d285caac70168a55` | PASS | PASS | PASS | PASS | **PASS** |
| 57 | `scripts/run_gates_g9_final.py` | `0fd64789a1d7fcf606c8c513cf88f054c3aeddf4089c11f31b32fe2fa2da9734` | — | PASS | PASS | PASS | **PASS** |
| 58 | `scripts/freeze_results_v2.py` | `d62691287c4bd2a68ab72e139cf393445bc01939b965d0459304c95fa091388c` | — | PASS | PASS | PASS | **PASS** |
| 59 | `scripts/freeze_results_v3.py` | `025cdcaf882d38439b4f7be9830c715b36f5d9b068f54d6ef161ba4436c0cacf` | — | — | PASS | PASS | **PASS** |
| 60 | `scripts/freeze_results_v4.py` | `013dd1cf2e5e385ac221b20d0d5b2e3b5fa1d95dfe34d2ab4be77b2482fad561` | — | — | — | PASS | **PASS** |
| 61 | `scripts/freeze_results_v5.py` | `a39e9662809343037db0118453386ba73ddb1a3e238087a8259841dcc8e10908` | — | — | — | — | **PASS** |
| 62 | `tests/test_gates_g9.py` | `2ac337d0fa3344a4bbeca6f09fae7daf57eac9984ae4bd0a6c7d42455fa2bdec` | PASS | PASS | PASS | PASS | **PASS** |
| 63 | `tests/test_clusters_synthetic.py` | `5634a33ca51e36e5f9db8fc0553d97a7467923d7a0baa4fff4e1c2ed40a00ba1` | PASS | PASS | PASS | PASS | **PASS** |
| 64 | `tests/test_sparc_synthetic.py` | `1110a57be3f203c751b5268b6988c1d3ee64b51f96a795b827bb5805ccc6208e` | PASS | PASS | PASS | PASS | **PASS** |

---

#### (4) `HEAD_TO_HEAD_PLAN.sha256` (`60e3e9c67ef00141fd1cfc87cbc3a5968a50fca552bcac8c787cf085bacd3117`) — `3 / 3` PASS
| # | File | Expected & Recomputed SHA-256 | Status |
|---|---|---|---|
| 1 | `HEAD_TO_HEAD_PLAN.md` | `2e58c8caf27522c457f4dc67c65e88dfc37dfe96c5e0be908f6384be034d44d2` | **PASS** |
| 2 | `head_to_head/HEAD_TO_HEAD_PLAN.md` | `2e58c8caf27522c457f4dc67c65e88dfc37dfe96c5e0be908f6384be034d44d2` | **PASS** |
| 3 | `head_to_head/DEVIATIONS.md` | `88d6ff2277f7c6e5352fe442a36441ffe86a602fabb9301dd197adc2454460b5` | **PASS** |

---

#### (5) `HEAD_TO_HEAD_RESULTS_v1.sha256` (`6f3b76f6f3b04e4ed4c664a3e3abace5e62e2b8a9b8bf15eeffbe1ebcea2eb6b`) — `162 / 162` PASS (Pre-Upgrade)
| # | File | Expected & Recomputed SHA-256 | Status |
|---|---|---|---|
| 1 | `ARGON_HEAD_TO_HEAD_HANDOFF.txt` | `ae93e999a32fbac2dd5e0d9633760cddc932703036b370e4f1b4248f8005515c` | **PASS** |
| 2 | `HEAD_TO_HEAD_PLAN.md` | `2e58c8caf27522c457f4dc67c65e88dfc37dfe96c5e0be908f6384be034d44d2` | **PASS** |
| 3 | `HEAD_TO_HEAD_PLAN.sha256` | `60e3e9c67ef00141fd1cfc87cbc3a5968a50fca552bcac8c787cf085bacd3117` | **PASS** |
| 4 | `HEAD_TO_HEAD_PLAN.sha256.ots` | `642c160f4e7b1b7f3cde4191ce0a49e687c13eb4b20193da1e3249d9d11d5c97` (pre-upgrade, in `.ots.bak`) / `92cd8772...` (post-upgrade) | **PASS (Pre-Upgrade)** |
| 5 | `HEAD_TO_HEAD_RESULTS.md` | `6a9c8e21a82e16b7cd1e324b5a30655fbf17c8e46f4cdb6c03116958a5d9ffe5` | **PASS** |
| 6 | `head_to_head/ACTIVITY_LOG_H2H.md` | `405f879d6c07cf7ea018346b6f16f7e3dfa11ec69b5bee3c0c5c2d8eb2a68de0` | **PASS** |
| 7 | `head_to_head/DEVIATIONS.md` | `88d6ff2277f7c6e5352fe442a36441ffe86a602fabb9301dd197adc2454460b5` | **PASS** |
| 8 | `head_to_head/HEAD_TO_HEAD_PLAN.md` | `2e58c8caf27522c457f4dc67c65e88dfc37dfe96c5e0be908f6384be034d44d2` | **PASS** |
| 9 | `head_to_head/HEAD_TO_HEAD_PLAN.sha256` | `60e3e9c67ef00141fd1cfc87cbc3a5968a50fca552bcac8c787cf085bacd3117` | **PASS** |
| 10 | `head_to_head/HEAD_TO_HEAD_PLAN.sha256.ots` | `642c160f4e7b1b7f3cde4191ce0a49e687c13eb4b20193da1e3249d9d11d5c97` (pre-upgrade, in `.ots.bak`) / `92cd8772...` (post-upgrade) | **PASS (Pre-Upgrade)** |
| 11 | `head_to_head/HEAD_TO_HEAD_RESULTS.md` | `6a9c8e21a82e16b7cd1e324b5a30655fbf17c8e46f4cdb6c03116958a5d9ffe5` | **PASS** |
| 12 | `head_to_head/build_report_and_freeze.py` | `f4784a0106211a63c3c9adf4bf10c55d2bca47a4b8503d8e5028ba45f77e5f55` | **PASS** |
| 13–84 | `head_to_head/chains/*.npz` (all 72 chain archives; see [RELEASE_PREP_REPORT.md](file:///D:/Argon_Code/Ropewalk/RELEASE_PREP_REPORT.md#L387-L458)) | All 72 match expected SHA-256 exactly | **72 / 72 PASS** |
| 85 | `head_to_head/h2h_cosmology.py` | `a2ab7d5b10256106b99213651f333bd58d465aa4dc4a80bc3800a5815238b118` | **PASS** |
| 86–157 | `head_to_head/logs/*.json` (all 72 seed logs; see [RELEASE_PREP_REPORT.md](file:///D:/Argon_Code/Ropewalk/RELEASE_PREP_REPORT.md#L460-L531)) | All 72 match expected SHA-256 exactly | **72 / 72 PASS** |
| 158 | `head_to_head/results.json` | `5d54d4072fa70efae7a7160de2a97e48f18ef4be40ef1e42de2f0047a495c484` | **PASS** |
| 159 | `head_to_head/run_h2h_grid.py` | `58d6dc92131910dc1442472aa953437f57ac6cf02dd8cf35867785b0f47b78dc` | **PASS** |
| 160 | `head_to_head/stamp_plan_h2h.py` | `a5bf440328a6c0f73a95971f0e39cfca0ca762467c44db9c530e7c8caae772df` | **PASS** |
| 161 | `head_to_head/validate_h2h.py` | `785e7076933fb3c9a7ba50e233b99f98b32b8d55640eb4c25e1e9ca187928258` | **PASS** |
| 162 | `head_to_head/validation_h2h.json` | `dc23c1b3697a4777586dc9502c4ebff925c537bc567f789d7abdd08c61c23131` | **PASS** |

---

#### (6) `PHASE3_ANALYSIS_PLAN.sha256` (`4eab04e302dfe06b39362d58c091a132ec4a46c6ad6f2a4a525bcdce3eae2b5c`) — `4 / 4` PASS
| # | File | Expected & Recomputed SHA-256 | Status |
|---|---|---|---|
| 1 | `PHASE3_ANALYSIS_PLAN.md` | `8476aeb01096c266a683e6baed9788fffdb1e227738b3c653c382c2ff82b431d` | **PASS** |
| 2 | `phase3/PHASE3_ANALYSIS_PLAN.md` | `8476aeb01096c266a683e6baed9788fffdb1e227738b3c653c382c2ff82b431d` | **PASS** |
| 3 | `phase3/DEVIATIONS.md` | `d93fff066adcd43ca1d6593e244cb32eac4d78b796cafdc35d494eebcd21992d` | **PASS** |
| 4 | `MOCKS_FOR_ARGON/MOCK_MANIFEST.csv` | `b7d08d57c24bfea919edefff85a62320ebc364d5cb062a9a343c5525d0f3f352` | **PASS** |

---

#### (7) `PHASE3_RESULTS_v1.sha256` (`8d4a38dfcbd5d47befd3114b9c269ff63c10c32f20994e459d65da1da45bea08`) — `63 / 63` PASS (Pre-Upgrade)
| # | File | Expected & Recomputed SHA-256 | Status |
|---|---|---|---|
| 1 | `ARGON_PHASE3_HANDOFF.txt` | `dff5bd678f9d47304ae85400f93223705b3011312f5edcb13c922e4477ce3968` | **PASS** |
| 2 | `MOCKS_FOR_ARGON/MOCK_MANIFEST.csv` | `b7d08d57c24bfea919edefff85a62320ebc364d5cb062a9a343c5525d0f3f352` | **PASS** |
| 3 | `PHASE3_ANALYSIS_PLAN.md` | `8476aeb01096c266a683e6baed9788fffdb1e227738b3c653c382c2ff82b431d` | **PASS** |
| 4 | `PHASE3_ANALYSIS_PLAN.sha256` | `4eab04e302dfe06b39362d58c091a132ec4a46c6ad6f2a4a525bcdce3eae2b5c` | **PASS** |
| 5 | `PHASE3_ANALYSIS_PLAN.sha256.ots` | `304f1f81868ff97c450fdb3f479c9332e248193eb8620e1fdc5a723f142307c8` (pre-upgrade, in `.ots.bak`) / `1a59dc42...` (post-upgrade) | **PASS (Pre-Upgrade)** |
| 6 | `PHASE3_RESULTS.md` | `fec774e6325f5d919cff8c62c5598ff283f5a5e82785f2938d887bcfb21711cb` | **PASS** |
| 7 | `phase3/ACTIVITY_LOG_PHASE3.md` | `8cd3e2a17aa9a744fd9b631f06c6aefc77ecd92322bbf23674535c70929c420a` | **PASS** |
| 8 | `phase3/DEVIATIONS.md` | `d93fff066adcd43ca1d6593e244cb32eac4d78b796cafdc35d494eebcd21992d` | **PASS** |
| 9 | `phase3/PHASE3_ANALYSIS_PLAN.md` | `8476aeb01096c266a683e6baed9788fffdb1e227738b3c653c382c2ff82b431d` | **PASS** |
| 10 | `phase3/PHASE3_ANALYSIS_PLAN.sha256` | `4eab04e302dfe06b39362d58c091a132ec4a46c6ad6f2a4a525bcdce3eae2b5c` | **PASS** |
| 11 | `phase3/PHASE3_ANALYSIS_PLAN.sha256.ots` | `304f1f81868ff97c450fdb3f479c9332e248193eb8620e1fdc5a723f142307c8` (pre-upgrade, in `.ots.bak`) / `1a59dc42...` (post-upgrade) | **PASS (Pre-Upgrade)** |
| 12 | `phase3/PHASE3_RESULTS.md` | `fec774e6325f5d919cff8c62c5598ff283f5a5e82785f2938d887bcfb21711cb` | **PASS** |
| 13 | `phase3/build_report_and_freeze.py` | `25ea5f7e6db804a7109ba696ce8c8353cd6cf95b67c736d8eae0d7367b7b2fde` | **PASS** |
| 14–58 | `phase3/logs/U-*.json` (all 45 universe logs; see [RELEASE_PREP_REPORT.md](file:///D:/Argon_Code/Ropewalk/RELEASE_PREP_REPORT.md#L563-L607)) | All 45 match expected SHA-256 exactly | **45 / 45 PASS** |
| 59 | `phase3/logs/runtime_projection.json` | `c92b6fc1502b3e72200b5db43048449908c650c5e6501fbf90f014354358280b` | **PASS** |
| 60 | `phase3/phase3_wrappers.py` | `d31e5dfb83c44d4db9a1d0e6cbe6fcfb3863a682f657cc29e595453ae23cea47` | **PASS** |
| 61 | `phase3/results.json` | `a1e667f5cec1a11f77f2b16c91fefd5c21d9a9de1226ce333291f09f8b7dba01` | **PASS** |
| 62 | `phase3/run_phase3.py` | `af0a39674a2a07d22394e39cafa1b538440cfa53e441fa07f6da06f7133fe013` | **PASS** |
| 63 | `phase3/stamp_plan_phase3.py` | `978205f46fc75eb6da811629788935ca821d88ddb7b4d647a50b38cbcf86ae01` | **PASS** |

---

## 2. TIMESTAMPS

All `.ots` files in the workspace were backed up to `_TRASH/ots_pre_release_backup_2026-11-01/` (and have `.ots.bak` counterparts alongside them), upgraded via `ots upgrade`, inspected via `ots info`, and cryptographically verified against the Bitcoin blockchain header Merkle roots. **Every `.ots` proof in the workspace is now anchored in the Bitcoin blockchain (`0` proofs remain unanchored):**

| Manifest | OpenTimestamps Proof File | Manifest SHA-256 (64 chars) | Bitcoin Block Height(s) | Bitcoin Block Time(s) (UTC) | Block Merkle Root Verification |
|---|---|---|---|---|---|
| `PREREG_v3.sha256` | [PREREG_v3.sha256.ots](file:///D:/Argon_Code/Ropewalk/PREREG_v3.sha256.ots) | `ab445f9aa11922802f2c8dc7517f6db3e063a579e0a10d92d26bef6eeb348da2` | **`973793`**, **`973821`** | `2026-10-30T08:22:55Z`, `2026-10-30T12:00:48Z` | Verified (`4f7f1239...`, `4df90706...`) |
| `PREREG_v4.sha256` | [PREREG_v4.sha256.ots](file:///D:/Argon_Code/Ropewalk/PREREG_v4.sha256.ots) | `53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b` | **`973800`**, **`973821`** | `2026-10-30T09:30:47Z`, `2026-10-30T12:00:48Z` | Verified (`d5417175...`, `4df90706...`) |
| `DATA_MANIFEST.sha256` | [DATA_MANIFEST.sha256.ots](file:///D:/Argon_Code/Ropewalk/DATA_MANIFEST.sha256.ots) | `73135698afb833e7e95e6a85c55475480132300e29f8b7b42d159c037067896d` | **`973800`**, **`973821`** | `2026-10-30T09:30:47Z`, `2026-10-30T12:00:48Z` | Verified (`d5417175...`, `4df90706...`) |
| `RESULTS_v1.sha256` | [RESULTS_v1.sha256.ots](file:///D:/Argon_Code/Ropewalk/RESULTS_v1.sha256.ots) | `b02000c98008e32ef34265a417e9d7dd724e3ee8472bc3cdf6be494f7477dd4e` | **`973822`** | `2026-10-30T12:13:07Z` | Verified (`2a52d1c5...`) |
| `RESULTS_v2.sha256` | [RESULTS_v2.sha256.ots](file:///D:/Argon_Code/Ropewalk/RESULTS_v2.sha256.ots) | `499026f0f39dc64735e5f69bf9113bd4dec05267d907d935aae075a8fdbdcc58` | **`973830`**, **`973864`** | `2026-10-30T13:48:06Z`, `2026-10-30T18:58:48Z` | Verified (`ef5f3979...`, `788bccdb...`) |
| `RESULTS_v3.sha256` | [RESULTS_v3.sha256.ots](file:///D:/Argon_Code/Ropewalk/RESULTS_v3.sha256.ots) | `baec3ff53effc7c11d55b7773b078c0389b707fe0b73790e35a57f5e6b9a93d1` | **`973844`**, **`973864`** | `2026-10-30T16:18:01Z`, `2026-10-30T18:58:48Z` | Verified (`1c3109e2...`, `788bccdb...`) |
| `RESULTS_v4.sha256` | [RESULTS_v4.sha256.ots](file:///D:/Argon_Code/Ropewalk/RESULTS_v4.sha256.ots) | `806d1ef12cb3ed84f681f8bfe5dc3d279e504fb0289aaa086132109187d718ab` | **`973844`**, **`973864`** | `2026-10-30T16:18:01Z`, `2026-10-30T18:58:48Z` | Verified (`1c3109e2...`, `788bccdb...`) |
| `RESULTS_v5.sha256` | [RESULTS_v5.sha256.ots](file:///D:/Argon_Code/Ropewalk/RESULTS_v5.sha256.ots) | `1ce42ac534b6a1766b002f8d064ba76662796227a4094d5f17a0a929c26aa882` | **`973844`**, **`973864`** | `2026-10-30T16:18:01Z`, `2026-10-30T18:58:48Z` | Verified (`1c3109e2...`, `788bccdb...`) |
| `HEAD_TO_HEAD_PLAN.sha256` | [HEAD_TO_HEAD_PLAN.sha256.ots](file:///D:/Argon_Code/Ropewalk/HEAD_TO_HEAD_PLAN.sha256.ots) | `60e3e9c67ef00141fd1cfc87cbc3a5968a50fca552bcac8c787cf085bacd3117` | **`973880`**, **`973901`** | `2026-10-30T21:25:03Z`, `2026-10-31T01:10:00Z` | Verified (`cb8cde04...`, `4b2b762b...`) |
| `HEAD_TO_HEAD_RESULTS_v1.sha256` | [HEAD_TO_HEAD_RESULTS_v1.sha256.ots](file:///D:/Argon_Code/Ropewalk/HEAD_TO_HEAD_RESULTS_v1.sha256.ots) | `6f3b76f6f3b04e4ed4c664a3e3abace5e62e2b8a9b8bf15eeffbe1ebcea2eb6b` | **`973958`**, **`973973`** | `2026-10-31T09:38:41Z`, `2026-10-31T12:06:42Z` | Verified (`f35936a1...`, `d9577b80...`) |
| `PHASE3_ANALYSIS_PLAN.sha256` | [PHASE3_ANALYSIS_PLAN.sha256.ots](file:///D:/Argon_Code/Ropewalk/PHASE3_ANALYSIS_PLAN.sha256.ots) | `4eab04e302dfe06b39362d58c091a132ec4a46c6ad6f2a4a525bcdce3eae2b5c` | **`973969`**, **`973973`** | `2026-10-31T11:13:07Z`, `2026-10-31T12:06:42Z` | Verified (`0d870955...`, `d9577b80...`) |
| `PHASE3_RESULTS_v1.sha256` | [PHASE3_RESULTS_v1.sha256.ots](file:///D:/Argon_Code/Ropewalk/PHASE3_RESULTS_v1.sha256.ots) | `8d4a38dfcbd5d47befd3114b9c269ff63c10c32f20994e459d65da1da45bea08` | **`974047`**, **`974048`** | `2026-11-01T00:42:41Z`, `2026-11-01T00:50:07Z` | Verified (`49c3eac2...`, `271ddbda...`) |

*(Retired `.ots` files in `_TRASH/`—`PREREG_v3_1cal.sha256.ots`, `PREREG_v3_prelim.sha256.ots`, and `PREREG_v3_pre_upgrade.sha256.ots`—were also backed up and upgraded, anchoring to Bitcoin blocks `973793` [`2026-10-30T08:22:55Z`] and `973821` [`2026-10-30T12:00:48Z`]. Note that `PREREG_v2.sha256` and `_TRASH/PREREG_v1.sha256` never had `.ots` stamps created.)*

---

## 3. MODEL VERSION

From the files, logs, and configuration inside `D:\Argon_Code\Ropewalk` (staying strictly inside `D:\Argon_Code\Ropewalk` per [GEMINI.md](file:///D:/Argon_Code/Ropewalk/GEMINI.md) Rule 3):

- **Project-Wide Setup Handoff ([MULTIVERSE_ARGON_HANDOFF.txt](file:///D:/Argon_Code/Ropewalk/MULTIVERSE_ARGON_HANDOFF.txt#L51-L52)):**
  - Line 51: `a. In the model selector just below the message box, choose Gemini 4 Argon.`
  - Line 52: `b. Set the thinking level to High (the choices are Low, Medium and High, chosen next to the model). If your picker shows a single entry called "Gemini 4 Argon (High)", pick that.`

- **(a) Stage 2:**
  - Recorded display name in [PREREG.md](file:///D:/Argon_Code/Ropewalk/PREREG.md#L4) line 4:
    > `author: "Gregory Mandarano / WickedAI — Pre-Registration Compiled by Gemini 4 Argon"`
  - Recorded name in [COMPARISON_ARGON_vs_REBUILD.md](file:///D:/Argon_Code/Ropewalk/COMPARISON_ARGON_vs_REBUILD.md#L2) line 2:
    > `2026-10-30 · Argon (Gemini) results: RESULTS_v1 (b02000c9…) · Blind rebuild (Claude Opus, Antigravity then Claude Code): REBUILD_RESULTS_v1 (93a154fb…)`
  - **Exact internal version/build string:** **Not recorded** anywhere in [ACTIVITY_LOG.md](file:///D:/Argon_Code/Ropewalk/ACTIVITY_LOG.md), [RESULTS.md](file:///D:/Argon_Code/Ropewalk/RESULTS.md), or [results/results.json](file:///D:/Argon_Code/Ropewalk/results/results.json) beyond the name `Gemini 4 Argon` / `Argon (Gemini)`.

- **(b) Head-to-Head:**
  - Recorded display name in [HEAD_TO_HEAD_PLAN.md](file:///D:/Argon_Code/Ropewalk/HEAD_TO_HEAD_PLAN.md#L4) line 4 and [HEAD_TO_HEAD_RESULTS.md](file:///D:/Argon_Code/Ropewalk/HEAD_TO_HEAD_RESULTS.md#L4) line 4:
    > `author: "Gregory Mandarano / WickedAI — Executed by Gemini 4 Argon"`
  - **Exact internal version/build string:** **Not recorded** anywhere in [head_to_head/ACTIVITY_LOG_H2H.md](file:///D:/Argon_Code/Ropewalk/head_to_head/ACTIVITY_LOG_H2H.md) or [head_to_head/results.json](file:///D:/Argon_Code/Ropewalk/head_to_head/results.json) beyond `"Gemini 4 Argon"` (only Python/library versions are logged on line 10 of `head_to_head/ACTIVITY_LOG_H2H.md`: `checked Python (3.14.7), numpy (2.5.4), and scipy (1.18.1) in .venv`).

- **(c) Phase 3:**
  - Recorded display name in [PHASE3_ANALYSIS_PLAN.md](file:///D:/Argon_Code/Ropewalk/PHASE3_ANALYSIS_PLAN.md#L4) line 4 and [PHASE3_RESULTS.md](file:///D:/Argon_Code/Ropewalk/PHASE3_RESULTS.md#L4) line 4:
    > `author: "Gregory Mandarano / WickedAI — Executed by Gemini 4 Argon"`
  - **Exact internal version/build string:** **Not recorded** anywhere in [phase3/ACTIVITY_LOG_PHASE3.md](file:///D:/Argon_Code/Ropewalk/phase3/ACTIVITY_LOG_PHASE3.md) or [phase3/results.json](file:///D:/Argon_Code/Ropewalk/phase3/results.json) beyond `"Gemini 4 Argon"`.

---

## 4. RELEASE INVENTORY (FOR A PUBLIC GITHUB REPO)

### 4a. Files and Folders That Belong in a Public Release (Grouped by Stage, with Sizes)

#### Stage 0 / Starter & Governing Specification Files (`198,825` bytes / `194.2 KiB`)
- `README.md` (`7,842` B)
- `requirements.txt` (`539` B)
- `run_all.py` (`1,769` B)
- `00_READ_FIRST.txt` (`1,411` B)
- `MULTIVERSE_ARGON_HANDOFF.txt` (`63,648` B) *(Note: see 4b regarding line 35 local path)*
- `MULTIVERSE_EQUATION_SHEET_v1.md` (`40,492` B)
- `MULTIVERSE_TESTS_v1.md` (`18,780` B)
- `MULTIVERSE_DATASETS_v1.md` (`16,306` B)
- `MULTIVERSE_PREDICTIONS_PAPER_v1.md` (`58,164` B)

#### Stage 1: Pre-Registration, Reviews, Manifests & Bitcoin Stamps (`445,749` bytes / `435.3 KiB`)
- **Governing Stage 1 Rulebook:**
  - `PREREG.md` (`69,416` B)
  - `MULTIVERSE_STAGE1_EQUATIONS.md` (`59,912` B)
  - `ASSUMPTIONS.md` (`16,195` B)
  - `STAGE1_PART1_SECTIONS_ABC.md` (`43,256` B)
  - `STAGE1_PART2_SECTIONS_DGH.md` (`26,407` B)
  - `STAGE1_PART3_SECTIONS_EFI.md` (`29,937` B)
  - `verify_b1_kernel_mc.py` (`2,692` B)
  - `FREEZE_TIMESTAMP.txt` (`2,279` B)
- **Stage 1 Cold Reviews & Responses:**
  - `REVIEW_COLD.md` (`31,493` B), `REVIEW_RESPONSE.md` (`33,460` B)
  - `REVIEW_V2.md` (`17,994` B), `REVIEW_RESPONSE_v2.md` (`33,978` B), `ERRATA_RESPONSE_v2.md` (`6,546` B)
  - `REVIEW_V3.md` (`10,697` B), `REVIEW_RESPONSE_v3.md` (`25,381` B)
- **Stage 1 Manifests & OpenTimestamps Proofs:**
  - `PREREG_v2.sha256` (`1,799` B)
  - `PREREG_v3.sha256` (`2,174` B), `PREREG_v3.sha256.ots` (`2,691` B), `PREREG_v3.sha256.ots.bak` (`654` B)
  - `PREREG_v4.sha256` (`2,512` B), `PREREG_v4.sha256.ots` (`2,797` B), `PREREG_v4.sha256.ots.bak` (`724` B)

#### Stage 2, 3 & 4: Core Empirical Analysis, Frozen Results, Paper, Manifests & Stamps (`1,771,847` bytes / `1.69 MiB`)
- **Dataset Freeze Manifests & Curated Priors/Tables:**
  - `DATA_MANIFEST.sha256` (`19,023` B), `DATA_MANIFEST.sha256.ots` (`2,832` B), `DATA_MANIFEST.sha256.ots.bak` (`759` B)
  - `data/MANIFEST.csv` (`16,554` B)
  - `data/MERGERS.csv` (`3,593` B)
  - `data/registered_priors.json` (`2,247` B)
- **Analysis & Freeze Code (`scripts/` — 15 files, `222,093` B):**
  - `scripts/get_data.py` (`10,104` B)
  - `scripts/cosmology.py` (`36,788` B)
  - `scripts/clusters_t4.py` (`23,047` B)
  - `scripts/sparc_t5.py` (`21,001` B)
  - `scripts/local_h0_t6.py` (`17,051` B)
  - `scripts/run_part8_fixes.py` (`18,485` B)
  - `scripts/run_part9_cosmology_tests.py` (`30,897` B)
  - `scripts/run_part10_astrophysics_and_verdict.py` (`24,424` B)
  - `scripts/run_gates_g9_final.py` (`7,695` B)
  - `scripts/freeze_data_manifest.py` (`2,904` B)
  - `scripts/freeze_results_v1.py` (`3,920` B), `scripts/freeze_results_v2.py` (`5,973` B), `scripts/freeze_results_v3.py` (`5,563` B), `scripts/freeze_results_v4.py` (`6,824` B), `scripts/freeze_results_v5.py` (`7,417` B)
- **Synthetic Unit & Gate Tests (`tests/` — 3 files, `17,489` B):**
  - `tests/test_gates_g9.py` (`9,719` B)
  - `tests/test_clusters_synthetic.py` (`3,443` B)
  - `tests/test_sparc_synthetic.py` (`4,327` B)
- **Frozen Numerical Outputs & Figures (`results/` — 16 files, `1,185,669` B / `1.13 MiB`):**
  - `results/validation_gates_g9.json` (`1,633` B), `results/validation_gates_g9_final.json` (`3,590` B)
  - `results/FREEZE_T1.json` (`1,632` B), `results/FREEZE_T2.json` (`13,603` B), `results/FREEZE_T4.json` (`1,351` B), `results/FREEZE_T5.json` (`5,119` B), `results/FREEZE_T6.json` (`1,168` B)
  - `results/FIXED_VALUES.json` (`2,137` B)
  - `results/part9_cosmology_results.json` (`39,285` B)
  - `results/results.json` (`124,194` B)
  - `results/RESULTS.md` (`83,647` B)
  - `results/figures/fig1_t1_unwinding_vs_desi.png` (`92,046` B), `fig2_t2_strand_budget_tension.png` (`105,656` B), `fig3_t4b_cluster_mergers.png` (`100,379` B), `fig4_t5_sparc_rotation_curves.png` (`434,272` B), `fig5_t6_regional_h0_and_coincidence.png` (`175,957` B)
- **Stage 4 Reports, Reviews, Replication Comparison, Logs, Manifests & Stamps:**
  - `RESULTS.md` (`83,647` B)
  - `MULTIVERSE_PREDICTIONS_PAPER_v4.md` (`61,475` B)
  - `DEVIATIONS.md` (`12,266` B)
  - `CLAIMS_CHECK.md` (`25,445` B)
  - `REVIEW_FINAL.md` (`18,198` B) *(Note: see 4b regarding line 3 Drive folder ID)*
  - `COMPARISON_ARGON_vs_REBUILD.md` (`5,375` B)
  - `ACTIVITY_LOG.md` (`40,544` B)
  - `RESULTS_v1.sha256` (`3,817` B), `RESULTS_v1.sha256.ots` (`1,655` B), `RESULTS_v1.sha256.ots.bak` (`794` B)
  - `RESULTS_v2.sha256` (`5,937` B), `RESULTS_v2.sha256.ots` (`2,690` B), `RESULTS_v2.sha256.ots.bak` (`794` B)
  - `RESULTS_v3.sha256` (`6,414` B), `RESULTS_v3.sha256.ots` (`2,654` B), `RESULTS_v3.sha256.ots.bak` (`619` B)
  - `RESULTS_v4.sha256` (`6,798` B), `RESULTS_v4.sha256.ots` (`2,724` B), `RESULTS_v4.sha256.ots.bak` (`689` B)
  - `RESULTS_v5.sha256` (`7,067` B), `RESULTS_v5.sha256.ots` (`2,759` B), `RESULTS_v5.sha256.ots.bak` (`794` B)

#### Supplementary Stage: Bayesian Head-to-Head (`92,355,661` bytes / `88.08 MiB`, or `0.86 MiB` without `.npz` chain archives)
- **Root Mirrors & Handoff:**
  - `ARGON_HEAD_TO_HEAD_HANDOFF.txt` (`5,139` B)
  - `HEAD_TO_HEAD_PLAN.md` (`16,811` B), `HEAD_TO_HEAD_PLAN.sha256` (`514` B), `HEAD_TO_HEAD_PLAN.sha256.ots` (`2,762` B), `HEAD_TO_HEAD_PLAN.sha256.ots.bak` (`794` B)
  - `HEAD_TO_HEAD_RESULTS.md` (`26,846` B), `HEAD_TO_HEAD_RESULTS_v1.sha256` (`22,459` B), `HEAD_TO_HEAD_RESULTS_v1.sha256.ots` (`2,691` B), `HEAD_TO_HEAD_RESULTS_v1.sha256.ots.bak` (`619` B)
- **`head_to_head/` Directory (`161` files, `92,279,441` B / `88.00 MiB`):**
  - `head_to_head/h2h_cosmology.py` (`15,704` B)
  - `head_to_head/validate_h2h.py` (`8,465` B), `head_to_head/validation_h2h.json` (`6,058` B)
  - `head_to_head/run_h2h_grid.py` (`22,179` B)
  - `head_to_head/build_report_and_freeze.py` (`24,737` B)
  - `head_to_head/stamp_plan_h2h.py` (`2,286` B)
  - `head_to_head/DEVIATIONS.md` (`561` B), `head_to_head/ACTIVITY_LOG_H2H.md` (`5,923` B)
  - `head_to_head/HEAD_TO_HEAD_PLAN.md` (`16,811` B), `.sha256` (`514` B), `.ots` (`2,762` B), `.ots.bak` (`794` B)
  - `head_to_head/HEAD_TO_HEAD_RESULTS.md` (`26,846` B), `_v1.sha256` (`22,459` B), `_v1.sha256.ots` (`2,691` B), `_v1.sha256.ots.bak` (`619` B)
  - `head_to_head/results.json` (`544,244` B)
  - `head_to_head/logs/*.json` (`72` files, `121,397` B total)
  - `head_to_head/chains/*.npz` (`72` files, `91,454,391` B / `87.22 MiB` total; individual files are `1.14–1.42 MiB` each)

#### Phase 3: Blind Mock-Universe Injection Tests (`3,712,065` bytes / `3.54 MiB` for `phase3/` + `24,248,387` bytes / `23.13 MiB` for `MOCKS_FOR_ARGON/` data vectors excluding duplicated covariance matrices)
- **Root Mirrors & Handoff:**
  - `ARGON_PHASE3_HANDOFF.txt` (`4,826` B)
  - `PHASE3_ANALYSIS_PLAN.md` (`25,035` B), `PHASE3_ANALYSIS_PLAN.sha256` (`635` B), `PHASE3_ANALYSIS_PLAN.sha256.ots` (`2,692` B), `PHASE3_ANALYSIS_PLAN.sha256.ots.bak` (`654` B)
  - `PHASE3_RESULTS.md` (`163,446` B), `PHASE3_RESULTS_v1.sha256` (`6,099` B), `PHASE3_RESULTS_v1.sha256.ots` (`2,658` B), `PHASE3_RESULTS_v1.sha256.ots.bak` (`689` B)
- **`phase3/` Directory (`61` files, `3,507,821` B / `3.35 MiB`):**
  - `phase3/phase3_wrappers.py` (`39,686` B)
  - `phase3/run_phase3.py` (`14,154` B)
  - `phase3/build_report_and_freeze.py` (`21,286` B)
  - `phase3/stamp_plan_phase3.py` (`3,354` B)
  - `phase3/DEVIATIONS.md` (`3,002` B), `phase3/ACTIVITY_LOG_PHASE3.md` (`10,072` B)
  - `phase3/PHASE3_ANALYSIS_PLAN.md` (`25,035` B), `.sha256` (`635` B), `.ots` (`2,692` B), `.ots.bak` (`654` B)
  - `phase3/PHASE3_RESULTS.md` (`163,446` B), `_v1.sha256` (`6,099` B), `_v1.sha256.ots` (`2,658` B), `_v1.sha256.ots.bak` (`689` B)
  - `phase3/results.json` (`2,246,780` B / `2.14 MiB`)
  - `phase3/logs/U-*.json` + `runtime_projection.json` (`46` files, `967,579` B total)
- **`MOCKS_FOR_ARGON/` (`MOCK_MANIFEST.csv` + 45 mock folders):**
  - `MOCKS_FOR_ARGON/MOCK_MANIFEST.csv` (`760` B)
  - `150` synthetic mock data vector files (`Pantheon+SH0ES.dat`, `DES-Dovekie_HD.csv`, `SPARC_Lelli2016c.mrt`, `MassModels_Lelli2016c.mrt`, `desi_gaussian_bao_ALL_GCcomb_mean.txt`, `lya_bao_ap_joint.json`, `distance_prior.json`, `REFERENCES.json`): `24,247,627` B (`23.12 MiB`). *(See 4d for the 45 duplicated third-party covariance files inside `MOCKS_FOR_ARGON/` totaling `1,092,223,065` B / `1.02 GiB`.)*

---

### 4b. Items That Must NOT Go Public (Secrets, Personal Paths, Emails, Drive IDs, Non-Release Folders)

1. **API Keys, Tokens, `.env` Files, Credentials:**
   - **None (`0`) found** anywhere in `D:\Argon_Code\Ropewalk`.

2. **Google Drive Folder ID (1 occurrence):**
   - [REVIEW_FINAL.md](file:///D:/Argon_Code/Ropewalk/REVIEW_FINAL.md#L3) **line 3:**
     > ``Reviewer inputs: frozen rulebook `/home/claude/argon_review_v4/` (PREREG.md v1.0.2 governing) and the 28 files in Drive folder `1n0J***[MASKED_DRIVE_ID]***tl1` (two listing pages, no subfolders).``

3. **Email Addresses (2 active non-analysis archival scripts + 3 backups in `_TRASH/`):**
   - [source_multiverse_archival.py](file:///D:/Argon_Code/Ropewalk/source_multiverse_archival.py#L36) **line 36:** `USER_AGENT = "MultiverseDocBot/1.0 (https://youtube.com/@WickedAI; c***@wickedai.com) Python-requests"`
   - [fetch_archival_replacements.py](file:///D:/Argon_Code/Ropewalk/fetch_archival_replacements.py#L30) **line 30:** `USER_AGENT = "MultiverseDocBot/1.0 (https://youtube.com/@WickedAI; c***@wickedai.com) Python-requests"`
   - Backups in `_TRASH/run1_backup/source_multiverse_archival.py` line 35, `_TRASH/run2_backup/source_multiverse_archival.py` line 36, `_TRASH/run3_backup/source_multiverse_archival.py` line 36: `c***@wickedai.com`

4. **Personal / System File Paths Beyond the Project Root (`C:\...` and `/home/...`):**
   - [MULTIVERSE_ARGON_HANDOFF.txt](file:///D:/Argon_Code/Ropewalk/MULTIVERSE_ARGON_HANDOFF.txt#L35) **line 35:** `C:\Users\User\Desktop\Code\multiverse\FOR_ARGON`
   - [REVIEW_FINAL.md](file:///D:/Argon_Code/Ropewalk/REVIEW_FINAL.md#L3) **line 3:** `/home/claude/argon_review_v4/` and `/home/claude/argon_results/`
   - Hardcoded Windows OpenSSL DLL path `C:\Python314\DLLs\libcrypto-3.dll` in the OpenTimestamps helper scripts:
     - [scripts/freeze_data_manifest.py](file:///D:/Argon_Code/Ropewalk/scripts/freeze_data_manifest.py#L22) **line 22**
     - [scripts/freeze_results_v1.py](file:///D:/Argon_Code/Ropewalk/scripts/freeze_results_v1.py#L22) **line 22**
     - [scripts/freeze_results_v2.py](file:///D:/Argon_Code/Ropewalk/scripts/freeze_results_v2.py#L22) **line 22**
     - [scripts/freeze_results_v3.py](file:///D:/Argon_Code/Ropewalk/scripts/freeze_results_v3.py#L22) **line 22**
     - [scripts/freeze_results_v4.py](file:///D:/Argon_Code/Ropewalk/scripts/freeze_results_v4.py#L23) **line 23**
     - [scripts/freeze_results_v5.py](file:///D:/Argon_Code/Ropewalk/scripts/freeze_results_v5.py#L23) **line 23**
     - [head_to_head/stamp_plan_h2h.py](file:///D:/Argon_Code/Ropewalk/head_to_head/stamp_plan_h2h.py#L22) **line 22**
     - [head_to_head/build_report_and_freeze.py](file:///D:/Argon_Code/Ropewalk/head_to_head/build_report_and_freeze.py#L24) **line 24**
     - [phase3/stamp_plan_phase3.py](file:///D:/Argon_Code/Ropewalk/phase3/stamp_plan_phase3.py#L23) **line 23**
     - [phase3/build_report_and_freeze.py](file:///D:/Argon_Code/Ropewalk/phase3/build_report_and_freeze.py#L24) **line 24**

5. **Local Workspace Root Path (`D:\Argon_Code\Ropewalk`) Occurrences:**
   - Appears in [README.md](file:///D:/Argon_Code/Ropewalk/README.md) (lines 3, 29, 85, 88, 95, 102), [GEMINI.md](file:///D:/Argon_Code/Ropewalk/GEMINI.md) (lines 3, 18, 19, 24), [SESSION_BOOTSTRAP_HANDOFF.md](file:///D:/Argon_Code/Ropewalk/SESSION_BOOTSTRAP_HANDOFF.md) (21 lines), [PREREG.md](file:///D:/Argon_Code/Ropewalk/PREREG.md) (line 97), [HEAD_TO_HEAD_PLAN.md](file:///D:/Argon_Code/Ropewalk/HEAD_TO_HEAD_PLAN.md) (lines 18, 25), [PHASE3_ANALYSIS_PLAN.md](file:///D:/Argon_Code/Ropewalk/PHASE3_ANALYSIS_PLAN.md) (lines 18, 26), [phase3/build_report_and_freeze.py](file:///D:/Argon_Code/Ropewalk/phase3/build_report_and_freeze.py) (lines 328, 329), [FREEZE_TIMESTAMP.txt](file:///D:/Argon_Code/Ropewalk/FREEZE_TIMESTAMP.txt) (lines 3–6), [REVIEW_RESPONSE.md](file:///D:/Argon_Code/Ropewalk/REVIEW_RESPONSE.md) (lines 4, 7, 150, 157), [REVIEW_RESPONSE_v2.md](file:///D:/Argon_Code/Ropewalk/REVIEW_RESPONSE_v2.md) (line 142), [REVIEW_RESPONSE_v3.md](file:///D:/Argon_Code/Ropewalk/REVIEW_RESPONSE_v3.md) (lines 81, 116), `STAGE1_PART1..3.md` (line 4), and the activity logs (`ACTIVITY_LOG.md`, `head_to_head/ACTIVITY_LOG_H2H.md`, `phase3/ACTIVITY_LOG_PHASE3.md`). *(Note: any file listed in a frozen `.sha256` manifest cannot be edited in place without changing its frozen hash.)*

6. **Workspace Folders & Non-Physics Production Files That Should Be Excluded from the Public Physics Repo:**
   - `.venv/` (local Python virtual environment)
   - `_ORIGINALS/` (access-locked original starter backup folder)
   - `_TRASH/` (`728` files, `489.8 MB` of retired drafts and backups)
   - `__pycache__/`, `scripts/__pycache__/`, `head_to_head/__pycache__/`, `phase3/__pycache__/`
   - `FOR_PLANNER/` (`24` files, `299.5 KB` duplicate convenience copies of root deliverables)
   - `GEMINI.md` and `SESSION_BOOTSTRAP_HANDOFF.md` (agent workspace guardrails and session bootstrap notes)
   - Documentary video production / archival image sourcing & subtitle translation files (not part of the physics empirical test suite):
     - `assets/` (`78` image files, `49.1 MB`)
     - `translation/` (`32` `.srt` / `.txt` caption translation files, `7.84 MB`)
     - `source_multiverse_archival.py`, `fetch_archival_replacements.py`, `fetch_fallback_portraits.py`, `fetch_fallback_portraits_v2.py`, `build_archival_catalog_b.py`, `update_replacements_and_credits.py`
     - `MASTER_CREDIT_CATALOG.md`, `MASTER_CREDIT_CATALOG.txt`, `MULTIVERSE_ARCHIVAL_CATALOG_B.csv`, `MULTIVERSE_ARCHIVAL_CATALOG_B.md`, `MULTIVERSE_ARCHIVAL_IMAGE_BREAKDOWN.txt`, `MULTIVERSE_PHOTO_CANDIDATES.json`, `MULTIVERSE_PHOTO_GALLERY.html`, `MULTIVERSE_PHOTO_SOURCING.csv`

---

### 4c. Files Over 50 MB (GitHub 100 MB Limit Check)

- **0 files in `D:\Argon_Code\Ropewalk` exceed 50 MB.**
- **Largest individual files in the workspace:**
  1. `data/pantheon_plus/Pantheon+SH0ES_STAT+SYS.cov` (and 30 byte-identical copies in `MOCKS_FOR_ARGON/U-*/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov`): **`33,284,960` bytes (`31.74 MiB` / `33.28 MB`)** each.
  2. `data/pantheon_plus/Pantheon+SH0ES_STATONLY.cov`: **`31,827,416` bytes (`30.35 MiB` / `31.83 MB`)**.
  3. `data/clusters_arxiv/1806.10619_Golovich_2019b_ApJ_882_69_MCC.eprint`: **`10,640,737` bytes (`10.15 MiB` / `10.64 MB`)**.
  4. `data/clusters_arxiv/1210.0014_Dawson_2013_ApJ_772_131_Bullet_MusketBall.eprint`: **`8,254,287` bytes (`7.87 MiB` / `8.25 MB`)**.
  5. `data/des_dovekie/STAT+SYS.npz` (and 15 byte-identical copies in `MOCKS_FOR_ARGON/U-*/des_dovekie/STAT+SYS.npz`): **`6,244,951` bytes (`5.96 MiB` / `6.24 MB`)** each.

---

### 4d. Third-Party Dataset Files Present (To Be Replaced by Download Script + Hashes)

All 66 third-party dataset files in `data/` (`172,612,091` bytes / `164.62 MiB` total, all verified against [DATA_MANIFEST.sha256](file:///D:/Argon_Code/Ropewalk/DATA_MANIFEST.sha256) and [RESULTS_v5.sha256](file:///D:/Argon_Code/Ropewalk/RESULTS_v5.sha256), downloadable via [scripts/get_data.py](file:///D:/Argon_Code/Ropewalk/scripts/get_data.py)):

1. **Pantheon+ & SH0ES (`data/pantheon_plus/` — 4 files, `65,695,715` bytes / `62.65 MiB`):**
   - `data/pantheon_plus/Pantheon+SH0ES.dat` (`579,283` B)
   - `data/pantheon_plus/Pantheon+SH0ES_STAT+SYS.cov` (`33,284,960` B)
   - `data/pantheon_plus/Pantheon+SH0ES_STATONLY.cov` (`31,827,416` B)
   - `data/pantheon_plus/README` (`4,056` B)

2. **DES-SN5YR Dovekie (`data/des_dovekie/` — 6 files, `7,691,504` bytes / `7.34 MiB`):**
   - `data/des_dovekie/DES-Dovekie-SN_Likelihood.py` (`7,674` B)
   - `data/des_dovekie/DES-Dovekie_HD.csv` (`148,002` B)
   - `data/des_dovekie/DES-Dovekie_Metadata.csv` (`1,269,831` B)
   - `data/des_dovekie/STAT+SYS.npz` (`6,244,951` B)
   - `data/des_dovekie/STATONLY.npz` (`19,366` B)
   - `data/des_dovekie/README.md` (`1,680` B)

3. **DESI DR2 BAO (`data/desi_bao_dr2/` — 16 files, `4,098` bytes / `4.00 KiB`):**
   - `desi_gaussian_bao_ALL_GCcomb_cov.txt` (`2,547` B), `desi_gaussian_bao_ALL_GCcomb_mean.txt` (`472` B)
   - `desi_gaussian_bao_BGS_BRIGHT-21.35_GCcomb_cov.txt` (`15` B), `desi_gaussian_bao_BGS_BRIGHT-21.35_GCcomb_mean.txt` (`63` B)
   - `desi_gaussian_bao_ELG_LOPnotqso_GCcomb_z1.1-1.6_cov.txt` (`62` B), `desi_gaussian_bao_ELG_LOPnotqso_GCcomb_z1.1-1.6_mean.txt` (`98` B)
   - `desi_gaussian_bao_LRG+ELG_LOPnotqso_GCcomb_cov.txt` (`62` B), `desi_gaussian_bao_LRG+ELG_LOPnotqso_GCcomb_mean.txt` (`98` B)
   - `desi_gaussian_bao_LRG_GCcomb_z0.4-0.6_cov.txt` (`62` B), `desi_gaussian_bao_LRG_GCcomb_z0.4-0.6_mean.txt` (`98` B)
   - `desi_gaussian_bao_LRG_GCcomb_z0.6-0.8_cov.txt` (`62` B), `desi_gaussian_bao_LRG_GCcomb_z0.6-0.8_mean.txt` (`98` B)
   - `desi_gaussian_bao_Lya_GCcomb_cov.txt` (`102` B), `desi_gaussian_bao_Lya_GCcomb_mean.txt` (`99` B)
   - `desi_gaussian_bao_QSO_GCcomb_cov.txt` (`62` B), `desi_gaussian_bao_QSO_GCcomb_mean.txt` (`98` B)

4. **SPARC Galaxy Rotation Curves (`data/sparc/` — 2 files, `297,777` bytes / `290.8 KiB`):**
   - `data/sparc/MassModels_Lelli2016c.mrt` (`269,518` B)
   - `data/sparc/SPARC_Lelli2016c.mrt` (`28,259` B)

5. **Planck 2018 / Chen, Huang & Wang (2019) & BBN Priors (`data/registered_priors.json` — 1 file, `2,247` bytes):**
   - `data/registered_priors.json` (`2,247` B — curated JSON containing the published Planck 2018 + Chen et al. 2019 compressed CMB distance prior vector/covariance and BBN $\omega_b$ priors).

6. **Dissociative Merger Cluster arXiv e-Print Tarballs (`data/clusters_arxiv/` [30 files, `68,017,763` B] and `data/clusters_arxiv_exact/` [8 files, `30,905,184` B] — 38 files total, `98,922,947` bytes / `94.34 MiB`):**
   - All 30 `.eprint` source tarballs in `data/clusters_arxiv/` (listed in Section 1.2 Table 2 rows 30–59) and all 8 `.eprint` source tarballs in `data/clusters_arxiv_exact/` (listed in Section 1.2 Table 3 rows 24–31).

7. **Duplicated Unmodified Third-Party Covariance Matrices Inside `MOCKS_FOR_ARGON/` (`60` files, `1,092,261,270` bytes / `1.02 GiB`):**
   - `MOCKS_FOR_ARGON/U-*/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov` (`30` files $\times$ `33,284,960` B = `998,548,800` B; 100% byte-identical to `data/pantheon_plus/Pantheon+SH0ES_STAT+SYS.cov`, SHA-256 `abf806d9...`)
   - `MOCKS_FOR_ARGON/U-*/des_dovekie/STAT+SYS.npz` (`15` files $\times$ `6,244,951` B = `93,674,265` B; 100% byte-identical to `data/des_dovekie/STAT+SYS.npz`, SHA-256 `ffd3124b...`)
   - `MOCKS_FOR_ARGON/U-*/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt` (`15` files $\times$ `2,547` B = `38,205` B; 100% byte-identical to `data/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt`, SHA-256 `252a1432...`)
   - Replacing these 60 unmodified third-party covariance copies in `MOCKS_FOR_ARGON/` with a post-download copy step in `scripts/get_data.py` reduces `MOCKS_FOR_ARGON/` from **`1.06 GiB`** to **`23.12 MiB`**.
