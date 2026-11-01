# Activity Log — Phase 3 Injection Tests (Ropewalk Multiverse Project)
# Phase 3 injection tests: supplementary, not pre-registered in Stage 1
# Format: <YYYY-MM-DDTHH:MM:SS> - <action>

2026-10-31T06:46:19 - Read file `D:\Argon_Code\Ropewalk\ARGON_PHASE3_HANDOFF.txt` (lines 1-76).
2026-10-31T06:46:36 - Read file `D:\Argon_Code\Ropewalk\ACTIVITY_LOG.md` (lines 1-203) to inspect prior Stage 2 / Stage 4 history.
2026-10-31T06:46:41 - Read file `D:\Argon_Code\Ropewalk\RESULTS_v5.sha256` (lines 1-70) to confirm frozen file list (including `ACTIVITY_LOG.md`, which is frozen and must not be modified).
2026-10-31T06:46:55 - Created file `D:\Argon_Code\Ropewalk\phase3\ACTIVITY_LOG_PHASE3.md` as the append-only Phase 3 activity log per `ARGON_PHASE3_HANDOFF.txt`.
2026-10-31T06:47:01 - Read file `D:\Argon_Code\Ropewalk\MOCKS_FOR_ARGON\MOCK_MANIFEST.csv` (lines 1-46) and `D:\Argon_Code\Ropewalk\head_to_head\h2h_cosmology.py` (lines 1-364).
2026-10-31T06:47:07 - Read files `D:\Argon_Code\Ropewalk\scripts\cosmology.py` and `D:\Argon_Code\Ropewalk\scripts\run_part8_fixes.py`.
2026-10-31T06:47:13 - Read files `D:\Argon_Code\Ropewalk\scripts\run_part9_cosmology_tests.py` and `D:\Argon_Code\Ropewalk\scripts\sparc_t5.py`.
2026-10-31T06:47:19 - Read files `D:\Argon_Code\Ropewalk\scripts\local_h0_t6.py` and `D:\Argon_Code\Ropewalk\scripts\run_part10_astrophysics_and_verdict.py`.
2026-10-31T06:47:27 - Executed command: listed files in `head_to_head/` and sample mock universe directories (`U-CUIZ`, `U-8TVY`, `U-IBCC`).
2026-10-31T06:47:36 - Read files `head_to_head/HEAD_TO_HEAD_PLAN.md`, `head_to_head/run_h2h_grid.py`, `head_to_head/stamp_plan_h2h.py`, and `head_to_head/build_report_and_freeze.py`.
2026-10-31T06:47:44 - Read files `MOCKS_FOR_ARGON/U-CUIZ/REFERENCES.json`, `MOCKS_FOR_ARGON/U-CUIZ/cmb_distance_prior/distance_prior.json`, `MOCKS_FOR_ARGON/U-CUIZ/desi_bao_dr2/lya_bao_ap_joint.json`, and `MOCKS_FOR_ARGON/U-CUIZ/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt`.
2026-10-31T06:48:01 - Executed command: listed files in `MOCKS_FOR_ARGON/U-J8TH` and `MOCKS_FOR_ARGON/U-I9FZ`.
2026-10-31T06:48:43 - Read files `COMPARISON_ARGON_vs_REBUILD.md` and `RESULTS.md` (lines 1-180).
2026-10-31T06:48:52 - Received pre-run clarification regarding per-universe `desi_bao_dr2/lya_bao_ap_joint.json` and `cmb_distance_prior/distance_prior.json` in `COSMO` universes (prior to any COSMO run; 0 runs invalidated).
2026-10-31T06:50:06 - Read header lines of `MOCKS_FOR_ARGON/U-8TVY/sparc/SPARC_Lelli2016c.mrt` and `MassModels_Lelli2016c.mrt`.
2026-10-31T06:50:42 - Executed Python environment check in `.venv` (`Python 3.14.7`, `numpy 2.5.4`, `scipy 1.18.1`, `emcee 3.1.6`, `matplotlib 3.11.2`, `psutil 7.2.2`).
2026-10-31T06:52:25 - Created file `D:\Argon_Code\Ropewalk\phase3\DEVIATIONS.md` recording pre-run clarification Entry `P3-C1` (0 runs invalidated).
2026-10-31T06:52:27 - Created file `D:\Argon_Code\Ropewalk\phase3\PHASE3_ANALYSIS_PLAN.md` locking all Phase 3 analysis settings, package versions, seeds, wrappers, and round-by-round run order prior to the first run.
2026-10-31T06:52:33 - Read file `D:\Argon_Code\Ropewalk\head_to_head\HEAD_TO_HEAD_PLAN.sha256`.
2026-10-31T06:52:57 - Created file `D:\Argon_Code\Ropewalk\phase3\stamp_plan_phase3.py`.
2026-10-31T06:53:08 - Executed command: `& "D:\Argon_Code\Ropewalk\.venv\Scripts\python.exe" "D:\Argon_Code\Ropewalk\phase3\stamp_plan_phase3.py"` — generated `phase3/PHASE3_ANALYSIS_PLAN.sha256` (`4eab04e302dfe06b39362d58c091a132ec4a46c6ad6f2a4a525bcdce3eae2b5c`, mirrored to root) and stamped `PHASE3_ANALYSIS_PLAN.sha256.ots` across 3 OpenTimestamps calendars (`alice`, `bob`, `finney`) prior to the first run.
2026-10-31T06:56:11 - Created file `D:\Argon_Code\Ropewalk\phase3\phase3_wrappers.py` implementing thin wrappers (`MockDESIBAOLikelihood`, `MockCMBLikelihood`, `MockPantheonPlusLikelihood`) and family runners (`COSMO`, `GALAXY`, `REGIONAL`).
2026-10-31T06:57:07 - Created file `D:\Argon_Code\Ropewalk\phase3\run_phase3.py` to execute Phase 3 round-by-round across all 45 mock universes (`N_CORES = 12`, `psutil.BELOW_NORMAL_PRIORITY_CLASS`).
2026-10-31T06:57:25 - Starting Round 1 first-universe benchmark across families: U-8TVY (GALAXY), U-CUIZ (COSMO), U-IBCC (REGIONAL).
2026-10-31T06:58:58 - Created file `D:\Argon_Code\Ropewalk\phase3\build_report_and_freeze.py` to generate `PHASE3_RESULTS.md`, compute `PHASE3_RESULTS_v1.sha256`, and stamp `PHASE3_RESULTS_v1.sha256.ots` upon completion of `run_phase3.py`.
2026-10-31T06:59:50 - Completed first GALAXY universe U-8TVY in 145.40s (projected 15 GALAXY universes serial = 2181.1s).
2026-10-31T06:59:57 - Completed first REGIONAL universe U-IBCC in 6.53s (projected 15 REGIONAL universes serial = 97.9s).
2026-10-31T07:57:49 - Completed first COSMO universe U-CUIZ in 3472.66s. Projected 45-universe total wall-clock runtime = 52849.5s (880.83 min; sum of 15x first-universe times = 54368.8s = 906.15 min) << 24h limit (86,400s). Proceeding to complete all 5 rounds.
2026-10-31T07:57:49 - Running Round 1 (6 pending universes: U-I9FZ, U-J8TH, U-LYTB, U-UD33, U-YIG4, U-YNED)...
2026-10-31T08:00:07 - Completed U-UD33 (GALAXY, Round 1) in 137.52s.
2026-10-31T08:00:13 - Completed U-I9FZ (GALAXY, Round 1) in 143.89s.
2026-10-31T08:00:20 - Completed U-LYTB (REGIONAL, Round 1) in 6.27s.
2026-10-31T08:00:20 - Completed U-J8TH (REGIONAL, Round 1) in 6.32s.
2026-10-31T09:49:53 - Completed U-YIG4 (COSMO, Round 1) in 6573.50s wall-clock (sum of 16 chain CPU times = 35593.9s).
2026-10-31T09:49:55 - Completed U-YNED (COSMO, Round 1) in 6575.21s wall-clock (sum of 16 chain CPU times = 36087.5s).
2026-10-31T09:49:55 - Finished Round 1 (all 9 universes complete; Round 1 elapsed = 10350.02s).
2026-10-31T09:49:55 - Running Round 2 (9 pending universes: U-44A3, U-8S92, U-EATJ, U-J0R7, U-JNXP, U-LMB5, U-PAKD, U-TLZU, U-Y2N1)...
2026-10-31T09:52:13 - Completed U-TLZU (GALAXY, Round 2) in 137.82s.
2026-10-31T09:52:14 - Completed U-J0R7 (GALAXY, Round 2) in 138.72s.
2026-10-31T09:52:18 - Completed U-8S92 (GALAXY, Round 2) in 142.94s.
2026-10-31T09:52:25 - Completed U-EATJ (REGIONAL, Round 2) in 6.90s.
2026-10-31T09:52:25 - Completed U-JNXP (REGIONAL, Round 2) in 6.98s.
2026-10-31T09:52:25 - Completed U-PAKD (REGIONAL, Round 2) in 6.99s.
2026-10-31T12:28:06 - Completed U-44A3 (COSMO, Round 2) in 9341.12s wall-clock (sum of 16 chain CPU times = 36650.3s).
2026-10-31T12:28:52 - Completed U-LMB5 (COSMO, Round 2) in 9386.68s wall-clock (sum of 16 chain CPU times = 36921.9s).
2026-10-31T12:29:24 - Completed U-Y2N1 (COSMO, Round 2) in 9418.94s wall-clock (sum of 16 chain CPU times = 35936.2s).
2026-10-31T12:29:24 - Finished Round 2 (all 9 universes complete; Round 2 elapsed = 9568.88s).
2026-10-31T12:29:24 - Running Round 3 (9 pending universes: U-07FN, U-099J, U-278Q, U-4JZF, U-63X5, U-6VMC, U-KPN8, U-SU9K, U-ZJBO)...
2026-10-31T12:31:45 - Completed U-278Q (GALAXY, Round 3) in 141.23s.
2026-10-31T12:31:45 - Completed U-63X5 (GALAXY, Round 3) in 141.25s.
2026-10-31T12:31:49 - Completed U-07FN (GALAXY, Round 3) in 144.72s.
2026-10-31T12:31:56 - Completed U-6VMC (REGIONAL, Round 3) in 6.83s.
2026-10-31T12:31:56 - Completed U-4JZF (REGIONAL, Round 3) in 6.86s.
2026-10-31T12:31:56 - Completed U-ZJBO (REGIONAL, Round 3) in 6.87s.
2026-10-31T15:13:08 - Completed U-099J (COSMO, Round 3) in 9671.51s wall-clock (sum of 16 chain CPU times = 37445.1s).
2026-10-31T15:13:20 - Completed U-KPN8 (COSMO, Round 3) in 9683.51s wall-clock (sum of 16 chain CPU times = 38056.9s).
2026-10-31T15:13:26 - Completed U-SU9K (COSMO, Round 3) in 9689.71s wall-clock (sum of 16 chain CPU times = 37449.6s).
2026-10-31T15:13:26 - Finished Round 3 (all 9 universes complete; Round 3 elapsed = 9841.31s).
2026-10-31T15:13:26 - Running Round 4 (9 pending universes: U-2B0Y, U-51CN, U-85K4, U-B485, U-BKI0, U-GL5Z, U-LH19, U-P0XK, U-YTKL)...
2026-10-31T15:15:43 - Completed U-P0XK (GALAXY, Round 4) in 136.97s.
2026-10-31T15:15:44 - Completed U-85K4 (GALAXY, Round 4) in 138.06s.
2026-10-31T15:15:49 - Completed U-YTKL (GALAXY, Round 4) in 143.51s.
2026-10-31T15:15:59 - Completed U-51CN (REGIONAL, Round 4) in 9.36s.
2026-10-31T15:15:59 - Completed U-B485 (REGIONAL, Round 4) in 9.40s.
2026-10-31T15:15:59 - Completed U-LH19 (REGIONAL, Round 4) in 9.44s.
2026-10-31T17:52:32 - Completed U-2B0Y (COSMO, Round 4) in 9392.70s wall-clock (sum of 16 chain CPU times = 36266.3s).
2026-10-31T17:52:46 - Completed U-BKI0 (COSMO, Round 4) in 9407.45s wall-clock (sum of 16 chain CPU times = 37147.3s).
2026-10-31T17:52:51 - Completed U-GL5Z (COSMO, Round 4) in 9412.08s wall-clock (sum of 16 chain CPU times = 36159.3s).
2026-10-31T17:52:51 - Finished Round 4 (all 9 universes complete; Round 4 elapsed = 9565.05s).
2026-10-31T17:52:51 - Running Round 5 (9 pending universes: U-8Z0S, U-8Z6F, U-J91F, U-KCY8, U-KQF9, U-NBRH, U-NPID, U-OEDW, U-ZY0Y)...
2026-10-31T17:55:06 - Completed U-KQF9 (GALAXY, Round 5) in 134.68s.
2026-10-31T17:55:07 - Completed U-8Z0S (GALAXY, Round 5) in 135.88s.
2026-10-31T17:55:10 - Completed U-NPID (GALAXY, Round 5) in 139.36s.
2026-10-31T17:55:17 - Completed U-ZY0Y (REGIONAL, Round 5) in 6.26s.
2026-10-31T17:55:17 - Completed U-KCY8 (REGIONAL, Round 5) in 6.34s.
2026-10-31T17:55:17 - Completed U-NBRH (REGIONAL, Round 5) in 6.35s.
2026-10-31T20:33:12 - Completed U-8Z6F (COSMO, Round 5) in 9475.61s wall-clock (sum of 16 chain CPU times = 37304.2s).
2026-10-31T20:33:28 - Completed U-J91F (COSMO, Round 5) in 9491.17s wall-clock (sum of 16 chain CPU times = 37637.3s).
2026-10-31T20:33:42 - Completed U-OEDW (COSMO, Round 5) in 9505.65s wall-clock (sum of 16 chain CPU times = 36488.5s).
2026-10-31T20:33:42 - Finished Round 5 (all 9 universes complete; Round 5 elapsed = 9651.38s).
2026-10-31T20:33:42 - Saved master Phase 3 results to D:\Argon_Code\Ropewalk\phase3\results.json (total wall-clock = 48976.88s).
2026-10-31T20:35:14 - Created file `D:\Argon_Code\Ropewalk\phase3\PHASE3_RESULTS.md` (mirrored to `D:\Argon_Code\Ropewalk\PHASE3_RESULTS.md`) and freezing all Phase 3 outputs into `PHASE3_RESULTS_v1.sha256`.
