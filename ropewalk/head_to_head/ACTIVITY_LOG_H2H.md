# Activity Log — Head-to-Head Supplementary Analysis (`head_to_head/ACTIVITY_LOG_H2H.md`)

**Label:** Supplementary analysis, not pre-registered.
**Scope:** Background expansion only (`BAO + compressed CMB + supernovae`). Does not change any registered Stage 2 verdict (`T5-A` failure stands; `RESULTS_v5.sha256` frozen files untouched).

2026-10-30T17:10:09 - Read `D:\Argon_Code\Ropewalk\ARGON_HEAD_TO_HEAD_HANDOFF.txt` and `D:\Argon_Code\Ropewalk\ACTIVITY_LOG.md`.
2026-10-30T17:10:16 - Read frozen manifests `D:\Argon_Code\Ropewalk\RESULTS_v5.sha256` and `D:\Argon_Code\Ropewalk\PREREG_v4.sha256` to verify the complete list of frozen files.
2026-10-30T17:10:28 - Read `D:\Argon_Code\Ropewalk\scripts\cosmology.py` (lines 1-800) and `D:\Argon_Code\Ropewalk\COMPARISON_ARGON_vs_REBUILD.md`.
2026-10-30T17:10:34 - Read `D:\Argon_Code\Ropewalk\scripts\cosmology.py` (lines 800-870), `D:\Argon_Code\Ropewalk\MULTIVERSE_STAGE1_EQUATIONS.md` (lines 1-180), `D:\Argon_Code\Ropewalk\tests\test_gates_g9.py`, and `D:\Argon_Code\Ropewalk\results\part9_cosmology_results.json`.
2026-10-30T17:11:00 - Executed command: created directory `D:\Argon_Code\Ropewalk\head_to_head` and checked Python (`3.14.7`), `numpy` (`2.5.4`), and `scipy` (`1.18.1`) in `.venv`.
2026-10-30T17:11:09 - Executed command: `& "D:\Argon_Code\Ropewalk\.venv\Scripts\pip.exe" install dynesty` — installed `dynesty==3.1.0` inside local `.venv` (preserving `numpy==2.5.4`, `scipy==1.18.1`, `matplotlib==3.11.2`, `psutil==7.2.2`) without modifying frozen `requirements.txt`.
2026-10-30T17:11:54 - Read `D:\Argon_Code\Ropewalk\DEVIATIONS.md`, `D:\Argon_Code\Ropewalk\PREREG.md`, and `D:\Argon_Code\Ropewalk\scripts\freeze_results_v5.py`.
2026-10-30T17:13:22 - Executed command: inspected `dynesty.NestedSampler.__init__` and `__new__` call signatures in `.venv`.
2026-10-30T17:13:56 - Created file `D:\Argon_Code\Ropewalk\head_to_head\DEVIATIONS.md` (initialized prior to plan freeze).
2026-10-30T17:15:01 - Created file `D:\Argon_Code\Ropewalk\head_to_head\HEAD_TO_HEAD_PLAN.md` (and mirrored to `D:\Argon_Code\Ropewalk\HEAD_TO_HEAD_PLAN.md`, SHA-256: `2e58c8caf27522c457f4dc67c65e88dfc37dfe96c5e0be908f6384be034d44d2`).
2026-10-30T17:15:16 - Created file `D:\Argon_Code\Ropewalk\head_to_head\HEAD_TO_HEAD_PLAN.sha256` (and mirrored to `D:\Argon_Code\Ropewalk\HEAD_TO_HEAD_PLAN.sha256`, SHA-256: `60e3e9c67ef00141fd1cfc87cbc3a5968a50fca552bcac8c787cf085bacd3117`).
2026-10-30T17:15:39 - Created file `D:\Argon_Code\Ropewalk\head_to_head\stamp_plan_h2h.py`.
2026-10-30T17:15:56 - Executed command: `& "D:\Argon_Code\Ropewalk\.venv\Scripts\python.exe" "D:\Argon_Code\Ropewalk\head_to_head\stamp_plan_h2h.py"` — stamped `HEAD_TO_HEAD_PLAN.sha256.ots` across 3 OpenTimestamps calendars (`alice`, `bob`, `finney`) prior to the first run.
2026-10-30T17:17:33 - Created file `D:\Argon_Code\Ropewalk\head_to_head\h2h_cosmology.py` (implementing Reading A literal `(a5)` sound-horizon integral `GL128` and `QUAD`, Gate `G9-b` under Reading A, and Reading A/B joint likelihood wrappers).
2026-10-30T17:18:14 - Created file `D:\Argon_Code\Ropewalk\head_to_head\validate_h2h.py` (two-quadrature validation of Reading A `r_s(z_*)`, Gate `G9-b` under Reading A, and `LCDM` nested-sampling `chi2_min` sanity check).
2026-10-30T17:18:25 - Executed command: `& "D:\Argon_Code\Ropewalk\.venv\Scripts\python.exe" "D:\Argon_Code\Ropewalk\head_to_head\validate_h2h.py"` (`task-48`).
2026-10-30T17:20:05 - Created file `D:\Argon_Code\Ropewalk\head_to_head\run_h2h_grid.py` (parallel 72-task `dynesty` nested-sampling runner across 24 model/SN/reading/prior configurations x 3 seeds, `N_CORES = 12`).
2026-10-30T17:21:38 - Created file `D:\Argon_Code\Ropewalk\head_to_head\build_report_and_freeze.py` (report generator for `HEAD_TO_HEAD_RESULTS.md` and `HEAD_TO_HEAD_RESULTS_v1.sha256` + OpenTimestamps freeze).
2026-10-30T17:49:02 - Completed `validate_h2h.py` (`task-48`): Reading A two-quadrature `r_s(z_*)` max relative difference = `1.615e-12 < 1e-6` (`PASS`); Gate `G9-b` under Reading A `h = 0.676124 +- 0.006101` (`0.4673 sigma` vs `0.6736+-0.0054`, `0.5706 sigma` vs `0.6727+-0.0060` -> `FAIL`); `LCDM` nested-sampling `chi2_min` sanity check `Pantheon+` `|diff| = 0.000246 <= 0.1` (`PASS`) and `DES-Dovekie` `|diff| = 0.000582 <= 0.1` (`PASS`); saved `D:\Argon_Code\Ropewalk\head_to_head\validation_h2h.json`.
2026-10-30T17:49:28 - Updated `D:\Argon_Code\Ropewalk\head_to_head\run_h2h_grid.py` task dispatch queue order (`CPL -> M1 -> M2 -> LCDM`) for 12-worker load balancing prior to launching grid.
2026-10-30T17:49:35 - Executed command: `& "D:\Argon_Code\Ropewalk\.venv\Scripts\python.exe" "D:\Argon_Code\Ropewalk\head_to_head\run_h2h_grid.py"`.
2026-10-31T04:27:26 - Completed `run_h2h_grid.py` (`task-61`): finished all 72 `dynesty` nested-sampling tasks (`24` configurations x `3` seeds) across `12` workers, saved all 72 chain archives in `head_to_head/chains/*.npz`, all 72 per-seed run logs in `head_to_head/logs/*.json`, and aggregated `D:\Argon_Code\Ropewalk\head_to_head\results.json`.
2026-10-31T04:28:00 - Executed command: `& "D:\Argon_Code\Ropewalk\.venv\Scripts\python.exe" "D:\Argon_Code\Ropewalk\head_to_head\build_report_and_freeze.py"` — generated `head_to_head/HEAD_TO_HEAD_RESULTS.md` (mirrored to `HEAD_TO_HEAD_RESULTS.md`), computed SHA-256 hashes of all head-to-head outputs, chains, logs, and code into `head_to_head/HEAD_TO_HEAD_RESULTS_v1.sha256` (mirrored to `HEAD_TO_HEAD_RESULTS_v1.sha256`), and stamped `HEAD_TO_HEAD_RESULTS_v1.sha256.ots` with OpenTimestamps.
2026-10-31T04:28:05 - Updated `D:\Argon_Code\Ropewalk\head_to_head\build_report_and_freeze.py` to read `ndim` from `mr['seed_runs'][0]['ndim']` and re-ran `build_report_and_freeze.py`.
2026-10-31T04:28:28 - Escaped `\text{{CDM}}` f-string braces on line 310 of `D:\Argon_Code\Ropewalk\head_to_head\build_report_and_freeze.py` and executed `build_report_and_freeze.py`.
