# Freeze Timing Audit (`FREEZE_TIMING_AUDIT.md`)

**Date:** `2026-11-01`  
**Scope:** Read-only forensic audit explaining why `results/FREEZE_T1.json`, `results/FREEZE_T2.json`, `results/FREEZE_T4.json`, `results/FREEZE_T5.json`, `results/FREEZE_T6.json`, and `results/FIXED_VALUES.json` each contain `"frozen_at": "2026-10-30T06:29:35"`, while their filesystem modification times (`LastWriteTime`) are `2026-10-30T07:04:55`–`2026-10-30T07:06:21` (prior to `RESULTS_v1.sha256` at `07:59:19`).  
**Constraint Compliance:** Read-only audit. No existing files were modified, and no code or analysis was re-run.

---

## 1. File Metadata: `frozen_at`, File Modification Time (`LastWriteTime`), Creation Time (`CreationTime`), Size, and SHA-256

All six freeze files in `D:\Argon_Code\Ropewalk\results\` (the four requested files `FREEZE_T1.json`, `FREEZE_T2.json`, `FREEZE_T4.json`, `FREEZE_T6.json`, plus companion files `FREEZE_T5.json` and `FIXED_VALUES.json` written by the same script) have the following exact values on disk:

| File | `frozen_at` JSON Field | NTFS `CreationTime` (Local) | NTFS `LastWriteTime` / Modification Time (Local) | Size (Bytes) | SHA-256 |
| :--- | :--- | :--- | :--- | ---: | :--- |
| `results/FREEZE_T1.json` | `"2026-10-30T06:29:35"` (line 3) | `2026-10-30T06:25:21.6850683` | `2026-10-30T07:04:55.8766875` | `1,632` | `bfc4e2531f1cc1ac2d2853253564676227ad786186c2e0039b18f86630cfc0d1` |
| `results/FREEZE_T2.json` | `"2026-10-30T06:29:35"` (line 3) | `2026-10-30T06:25:21.6870678` | `2026-10-30T07:04:55.8766875` | `13,603` | `ea12e85f5a9334cb8495d1ad0f52bdc024c5efb329990bddcd12363abdc7d970` |
| `results/FREEZE_T4.json` | `"2026-10-30T06:29:35"` (line 3) | `2026-10-30T06:25:21.6880687` | `2026-10-30T07:04:55.8776874` | `1,351` | `ba0312c8fd604668c01b5ba004ca7c329b641b7e780868f1d3600a533b63141b` |
| `results/FREEZE_T5.json` *(companion)* | `"2026-10-30T06:29:35"` (line 3) | `2026-10-30T06:26:52.0739730` | `2026-10-30T07:06:18.0522497` | `5,119` | `42555e320386a4eb9fdedb8a4cc5592594d066e0162b00efbb20726dac768743` |
| `results/FREEZE_T6.json` | `"2026-10-30T06:29:35"` (line 3) | `2026-10-30T06:26:55.9866204` | `2026-10-30T07:06:21.2723400` | `1,168` | `30125149716c3b1de0932ac3e7b247f5ec5f1a04316f77d025cbb6b488478e3a` |
| `results/FIXED_VALUES.json` *(companion)* | `"2026-10-30T06:29:35"` (line 2) | `2026-10-30T06:26:56.0066206` | `2026-10-30T07:06:21.2923399` | `2,137` | `c95b127261b355268a282b90179d141e0f147aaf3670d785f3a32cdc48db2059` |

*(Note: There is no `FREEZE_T3.json` because Section 5.3 of `PREREG.md` specifies `"Test T3 — Omitted (No Test)"`.)*

### Verification Against `FIXED_VALUES.json` and `RESULTS_v1.sha256`
- Every SHA-256 above is identical to the hash recorded in `results/FIXED_VALUES.json` (lines 4–10, written at `2026-10-30T07:06:21.2923399`):
  ```json
    "freeze_file_sha256": {
      "FREEZE_T1.json": "bfc4e2531f1cc1ac2d2853253564676227ad786186c2e0039b18f86630cfc0d1",
      "FREEZE_T2.json": "ea12e85f5a9334cb8495d1ad0f52bdc024c5efb329990bddcd12363abdc7d970",
      "FREEZE_T4.json": "ba0312c8fd604668c01b5ba004ca7c329b641b7e780868f1d3600a533b63141b",
      "FREEZE_T5.json": "42555e320386a4eb9fdedb8a4cc5592594d066e0162b00efbb20726dac768743",
      "FREEZE_T6.json": "30125149716c3b1de0932ac3e7b247f5ec5f1a04316f77d025cbb6b488478e3a"
    },
  ```
- Every SHA-256 above is also identical to `RESULTS_v1.sha256` (lines 19–24, generated at `2026-10-30T07:59:19`, `LastWriteTime = 2026-10-30T07:59:20.1308457`):
  ```text
  bfc4e2531f1cc1ac2d2853253564676227ad786186c2e0039b18f86630cfc0d1  results/FREEZE_T1.json
  ea12e85f5a9334cb8495d1ad0f52bdc024c5efb329990bddcd12363abdc7d970  results/FREEZE_T2.json
  ba0312c8fd604668c01b5ba004ca7c329b641b7e780868f1d3600a533b63141b  results/FREEZE_T4.json
  42555e320386a4eb9fdedb8a4cc5592594d066e0162b00efbb20726dac768743  results/FREEZE_T5.json
  30125149716c3b1de0932ac3e7b247f5ec5f1a04316f77d025cbb6b488478e3a  results/FREEZE_T6.json
  c95b127261b355268a282b90179d141e0f147aaf3670d785f3a32cdc48db2059  results/FIXED_VALUES.json
  ```

---

## 2. Verbatim Quotes of Every `ACTIVITY_LOG.md` Line and `DEVIATIONS.md` Entry Between `06:25` and `07:10` on `2026-10-30`

### 2a. `ACTIVITY_LOG.md` (Lines 156–158, plus Boundary Lines 155 and 159)
Between `06:25` and `07:10` on `2026-10-30`, `ACTIVITY_LOG.md` contains **exactly three lines** (lines 156, 157, and 158). Quoted verbatim below (with immediately adjacent lines 155 and 159 included to show the exact window boundaries):

```text
155: 2026-10-30T05:47:20 Created run_all.py master reproducibility pipeline script.
156: 2026-10-30T06:28:52 Vectorized comoving-distance cumulative Hermite quadrature in scripts/cosmology.py.
157: 2026-10-30T06:29:25 Updated split-Rhat quadrant block diagnostic in scripts/run_part8_fixes.py.
158: 2026-10-30T07:06:21 Completed scripts/run_part8_fixes.py: saved FREEZE_T1.json, FREEZE_T2.json, FREEZE_T4.json, FREEZE_T5.json, FREEZE_T6.json, and FIXED_VALUES.json with all chains converged (Rhat-1 < 0.01, ESS > 1000) (Part 8 complete).
159: 2026-10-30T07:45:35 Completed scripts/run_part9_cosmology_tests.py: saved results/part9_cosmology_results.json (T1-L1: INCONCLUSIVE; T1-Sign: PASS; T2-A: FAIL; T2-N1: FAIL; T2-N2: FAIL; T6: FAIL) (Part 9 complete).
```

### 2b. `DEVIATIONS.md` (and `_TRASH/DEVIATIONS_v1.md`)
- **Between `06:25` and `07:10` on `2026-10-30`:** **Zero entries** were written to `DEVIATIONS.md`. The original file (`_TRASH/DEVIATIONS_v1.md`) was created at `2026-10-30T05:23:40` (`LastWriteTime = 2026-10-30T05:23:40.6817441`, `ACTIVITY_LOG.md` line 137) containing only entry `D1`, and was not modified again until `2026-10-30T09:05:35` (`ACTIVITY_LOG.md` line 175).
- **Later post-review reference to `2026-10-30T06:29:35` in `DEVIATIONS.md`:** In the post-review updates to `DEVIATIONS.md` (added at `11:11:04`, `ACTIVITY_LOG.md` line 193), bullet `C5` (line 58 of `DEVIATIONS.md`) mentions the `06:29:35` timestamp. Quoted verbatim:
  ```text
  58: - **`C5` (Post-Parameter-Freeze Modification of `scripts/run_part10_astrophysics_and_verdict.py`):** `scripts/run_part10_astrophysics_and_verdict.py` was modified after the `2026-10-30T06:29:35` parameter freeze (at `07:46:30` and `07:47:15`, `ACTIVITY_LOG.md` lines 161–162, to complete the Part 10 figure/verdict formatting and fix mathtext `\ge/\le` and the `baryon_only_test` key lookup), so its SHA-256 hash recorded in `results/FIXED_VALUES.json` (`ccc6a7dcf6a8202e91c279411f2a445b472c616fe703d4e6437a75ab5bb009c5`) differs from its final hash in `RESULTS_v1.sha256`–`RESULTS_v4.sha256` (`2b27fe212f6912392e67939b1c262fb0dd73a32d34aea7c2b9865dc8ee198c4f`). All frozen parameters and test verdicts are unaffected.
  ```

---

## 3. Script Identification, Execution Timeline, and Verbatim Code Lines

### 3a. Which Script Wrote the Files
All six files (`FREEZE_T1.json`, `FREEZE_T2.json`, `FREEZE_T4.json`, `FREEZE_T5.json`, `FREEZE_T6.json`, and `FIXED_VALUES.json`) were written by **`scripts/run_part8_fixes.py`** (`SHA-256: 0bd1702119f1348e12ff796fa2bd16d133f349c70cb4ff0c04f51f5f736d12e8`, `CreationTime = 2026-10-30T05:42:33.6305974`, `LastWriteTime = 2026-10-30T06:29:25.4693164`).

### 3b. Why `frozen_at` Is `2026-10-30T06:29:35` While `LastWriteTime` Is `07:04:55`–`07:06:21` (And Why `CreationTime` Is `06:25:21`–`06:26:56`)
The filesystem timestamps and `scripts/run_part8_fixes.py` source code establish two facts:

1. **Why the final run (Run 2) has a 35–37 minute gap between `frozen_at` (`06:29:35`) and `LastWriteTime` (`07:04:55`–`07:06:21`):**
   - In `scripts/run_part8_fixes.py`, `now_iso = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")` is called **once at the very start of `main()` on line 250**, **before** any MCMC chains or training-half fits execute.
   - Run 2 of `scripts/run_part8_fixes.py` was launched at **`2026-10-30T06:29:35`** (10 seconds after `scripts/run_part8_fixes.py` was saved at `06:29:25.4693164`). This launch time is independently confirmed by `scripts/__pycache__/cosmology.cpython-314.pyc`, which has `CreationTime = LastWriteTime = 2026-10-30T06:29:35.9201379` (created when Python imported the newly vectorized `scripts/cosmology.py` at the start of the `06:29:35` run).
   - After capturing `now_iso = "2026-10-30T06:29:35"` on line 250, `main()` executed sequentially:
     - **Step 1 (`06:29:35` to `07:04:55.876`, duration 35m 20s):** Lines 304–305 ran the 6 parallel `T2-A` MCMC chains (`run_single_t2a_mcmc_worker`: 32 walkers, 1,000 burn-in + 4,000 production steps = 160,000 likelihood evaluations per chain) across `multiprocessing.Pool`.
     - **Steps 2–4 (`07:04:55.876` to `07:04:55.877`, duration ~1 ms):** As soon as `pool.map(...)` returned at `07:04:55.876`, `main()` wrote `FREEZE_T1.json` (line 334, `LastWriteTime = 07:04:55.8766875`), wrote `FREEZE_T2.json` (line 356, `LastWriteTime = 07:04:55.8766875`), ran the fast 8-cluster `T4b` training grid search (lines 360–363), and wrote `FREEZE_T4.json` (line 374, `LastWriteTime = 07:04:55.8776874`). All three files used `"frozen_at": now_iso` (`"2026-10-30T06:29:35"`).
     - **Step 5 (`07:04:55.877` to `07:06:18.052`, duration 1m 22.17s):** Lines 378–389 ran 7 `T5-A` and `T5-B` SPARC rotation-curve training-half grid fits (88 galaxies × 500 grid points per fit), and line 412 wrote `FREEZE_T5.json` (`LastWriteTime = 07:06:18.0522497`) using `"frozen_at": now_iso` (`"2026-10-30T06:29:35"`).
     - **Steps 6–7 (`07:06:18.052` to `07:06:21.292`, duration 3.24s):** Lines 416–417 loaded the full Pantheon+ table and ran the `T6` SH0ES Cepheid calibrator GLS fit, line 427 wrote `FREEZE_T6.json` (`LastWriteTime = 07:06:21.2723400`), and line 453 wrote `FIXED_VALUES.json` (`LastWriteTime = 07:06:21.2923399`), both using `"frozen_at": now_iso` (`"2026-10-30T06:29:35"`).
     - At `07:06:21`, `ACTIVITY_LOG.md` line 158 logged completion of `scripts/run_part8_fixes.py`.

2. **What the NTFS `CreationTime` (`06:25:21`–`06:26:56`) reveals about an earlier unlogged execution (Run 1):**
   - On Windows NTFS, overwriting an existing file via `Path.write_text()` updates `LastWriteTime` while preserving the file's original `CreationTime`.
   - The `CreationTime` values on `FREEZE_T1.json` (`06:25:21.6850683`), `FREEZE_T2.json` (`06:25:21.6870678`), `FREEZE_T4.json` (`06:25:21.6880687`), `FREEZE_T5.json` (`06:26:52.0739730`), `FREEZE_T6.json` (`06:26:55.9866204`), and `FIXED_VALUES.json` (`06:26:56.0066206`) show the exact same internal step spacing (T1/T2/T4 written together in 3 ms at `06:25:21`, T5 written 90.39 s later at `06:26:52`, T6 and FIXED_VALUES written 3.91 s later at `06:26:55`–`06:26:56`).
   - This proves that an **initial, unlogged execution (Run 1)** of `scripts/run_part8_fixes.py` (started after `run_all.py` was created at `05:47:20`, `ACTIVITY_LOG.md` line 155) completed between `06:25:21` and `06:26:56`.
   - Two minutes after Run 1 finished at `06:26:56`, `scripts/cosmology.py` was edited at `06:28:52` (line 156: `"Vectorized comoving-distance cumulative Hermite quadrature in scripts/cosmology.py"`) and `scripts/run_part8_fixes.py` was edited at `06:29:25` (line 157: `"Updated split-Rhat quadrant block diagnostic in scripts/run_part8_fixes.py"`). Run 2 was then launched at `06:29:35`, overwriting the six files in place at `07:04:55`–`07:06:21`.

### 3c. Verbatim Code Lines from `scripts/run_part8_fixes.py` (Lines 243–459)

```python
243: def main():
244:     set_below_normal_priority()
245:     root = Path(__file__).resolve().parent.parent
246:     data_dir = str(root / "data")
247:     results_dir = root / "results"
248:     results_dir.mkdir(parents=True, exist_ok=True)
249:     scripts_hashes = compute_scripts_sha256(root / "scripts")
250:     now_iso = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
251: 
252:     print("1. Running T2-A MCMC fixing chains in parallel across worker pool...")
253:     tasks = [
254:         {
255:             "run_id": "T2-A-Pantheon+_deciding",
256:             "sn_name": "Pantheon+",
257:             "cmb_mode": "conditional_2x2",
258:             "bbn_prior": (2.218, 0.055),
259:             "data_dir": data_dir,
260:             "seed_offset": 101,
261:         },
262:         {
263:             "run_id": "T2-A-DES-Dovekie_deciding",
264:             "sn_name": "DES-Dovekie",
265:             "cmb_mode": "conditional_2x2",
266:             "bbn_prior": (2.218, 0.055),
267:             "data_dir": data_dir,
268:             "seed_offset": 102,
269:         },
270:         {
271:             "run_id": "T2-A-Pantheon+_Cooke18_sensitivity",
272:             "sn_name": "Pantheon+",
273:             "cmb_mode": "conditional_2x2",
274:             "bbn_prior": (2.166, 0.019),
275:             "data_dir": data_dir,
276:             "seed_offset": 103,
277:         },
278:         {
279:             "run_id": "T2-A-DES-Dovekie_Cooke18_sensitivity",
280:             "sn_name": "DES-Dovekie",
281:             "cmb_mode": "conditional_2x2",
282:             "bbn_prior": (2.166, 0.019),
283:             "data_dir": data_dir,
284:             "seed_offset": 104,
285:         },
286:         {
287:             "run_id": "T2-A-Pantheon+_MarginalCMB_sensitivity",
288:             "sn_name": "Pantheon+",
289:             "cmb_mode": "marginal_2x2",
290:             "bbn_prior": (2.218, 0.055),
291:             "data_dir": data_dir,
292:             "seed_offset": 105,
293:         },
294:         {
295:             "run_id": "T2-A-DES-Dovekie_MarginalCMB_sensitivity",
296:             "sn_name": "DES-Dovekie",
297:             "cmb_mode": "marginal_2x2",
298:             "bbn_prior": (2.218, 0.055),
299:             "data_dir": data_dir,
300:             "seed_offset": 106,
301:         },
302:     ]
303: 
304:     with mp.Pool(processes=min(len(tasks), N_CORES), initializer=set_below_normal_priority) as pool:
305:         t2_results_list = pool.map(run_single_t2a_mcmc_worker, tasks)
306: 
307:     t2_by_id = {r["run_id"]: r for r in t2_results_list}
308:     f_leak_frozen = t2_by_id["T2-A-Pantheon+_deciding"]["frozen_quantities"]["f_leak"]
309:     sigma_f_leak_frozen = t2_by_id["T2-A-Pantheon+_deciding"]["frozen_quantities"]["sigma_f_leak"]
310:     print(f"   T2-A-Pantheon+ frozen f_leak = {f_leak_frozen:.6f} +/- {sigma_f_leak_frozen:.6f}")
311: 
312:     # 2. Freeze T1 structural parameters (FREEZE_T1.json)
313:     freeze_t1 = {
314:         "test_id": "T1 (T1-L1 Primary Pillar 1 & T1-Sign Secondary)",
315:         "frozen_at": now_iso,
316:         "structural_constants": {"N_s": 19, "N_r": 133, "Omega_b_structural": 1.0 / 19.0},
317:         "law1_priors": {
318:             "Omega_m_tot": [0.1, 0.6],
319:             "h": [0.5, 0.9],
320:             "100_omega_b": [1.8, 2.6],
321:             "gamma_u": [0.0, 2.0],
322:         },
323:         "cpl_priors": {
324:             "Omega_m_tot": [0.1, 0.6],
325:             "h": [0.5, 0.9],
326:             "100_omega_b": [1.8, 2.6],
327:             "w0": [-3.0, 1.0],
328:             "wa": [-3.0, 2.0],
329:             "constraint": "w0 + wa < 0",
330:         },
331:         "scripts_sha256": scripts_hashes,
332:     }
333:     freeze_t1_path = results_dir / "FREEZE_T1.json"
334:     freeze_t1_path.write_text(json.dumps(freeze_t1, indent=2), encoding="utf-8")
335: 
336:     # 3. Freeze T2 parameters (FREEZE_T2.json)
337:     freeze_t2 = {
338:         "test_id": "T2 (T2-A Primary Pillar 2, T2-N1, T2-N2)",
339:         "frozen_at": now_iso,
340:         "deciding_PantheonPlus": t2_by_id["T2-A-Pantheon+_deciding"],
341:         "deciding_DES_Dovekie": t2_by_id["T2-A-DES-Dovekie_deciding"],
342:         "single_frozen_f_leak_for_T5": {
343:             "source_run": "T2-A-Pantheon+_deciding",
344:             "f_leak": f_leak_frozen,
345:             "sigma_f_leak": sigma_f_leak_frozen,
346:         },
347:         "sensitivity_runs": {
348:             "PantheonPlus_Cooke18": t2_by_id["T2-A-Pantheon+_Cooke18_sensitivity"],
349:             "DES_Dovekie_Cooke18": t2_by_id["T2-A-DES-Dovekie_Cooke18_sensitivity"],
350:             "PantheonPlus_MarginalCMB": t2_by_id["T2-A-Pantheon+_MarginalCMB_sensitivity"],
351:             "DES_Dovekie_MarginalCMB": t2_by_id["T2-A-DES-Dovekie_MarginalCMB_sensitivity"],
352:         },
353:         "scripts_sha256": scripts_hashes,
354:     }
355:     freeze_t2_path = results_dir / "FREEZE_T2.json"
356:     freeze_t2_path.write_text(json.dumps(freeze_t2, indent=2), encoding="utf-8")
357: 
358:     # 4. Run T4b training-half fit and freeze (FREEZE_T4.json)
359:     print("2. Running T4b training-half fit...")
360:     mergers = load_mergers_csv(root / "data" / "MERGERS.csv")
361:     train_mergers = [c for c in mergers if c["split"] == "train"]
362:     t4_fit_deciding = fit_tau_lag_hard_step(train_mergers, tau_min_myr=235, tau_max_myr=1500, step_myr=5)
363:     t4_fit_400 = fit_tau_lag_hard_step(train_mergers, tau_min_myr=400, tau_max_myr=1500, step_myr=5)
364:     print(f"   T4b frozen tau_lag = {t4_fit_deciding['tau_lag_myr']} Myr (train_acc = {t4_fit_deciding['train_acc']:.4f})")
365: 
366:     freeze_t4 = {
367:         "test_id": "T4b (Cluster Merger Age Cutoff Primary Pillar 3)",
368:         "frozen_at": now_iso,
369:         "deciding_training_fit": t4_fit_deciding,
370:         "sensitivity_Bullet_median_400Myr_fit": t4_fit_400,
371:         "scripts_sha256": scripts_hashes,
372:     }
373:     freeze_t4_path = results_dir / "FREEZE_T4.json"
374:     freeze_t4_path.write_text(json.dumps(freeze_t4, indent=2), encoding="utf-8")
375: 
376:     # 5. Run T5-A and T5-B training-half fits using frozen f_leak and freeze (FREEZE_T5.json)
377:     print("3. Running T5-A and T5-B SPARC training-half fits...")
378:     sparc_galaxies = parse_sparc_catalog(root / "data" / "sparc")
379:     sparc_train = [g for g in sparc_galaxies if g["split"] == "train"]
380: 
381:     t5a_deciding = fit_sparc_parameter(sparc_train, "T5A", f_leak_frozen, loss_metric="sum_chi2_red")
382:     t5b_deciding = fit_sparc_parameter(sparc_train, "T5B", f_leak_frozen, loss_metric="sum_chi2_red")
383: 
384:     # Sensitivity training objectives (PREREG.md line 272) and f_leak = 1/6 sensitivity
385:     t5a_tot_chi2 = fit_sparc_parameter(sparc_train, "T5A", f_leak_frozen, loss_metric="total_chi2")
386:     t5a_med_chi2 = fit_sparc_parameter(sparc_train, "T5A", f_leak_frozen, loss_metric="median_chi2_red")
387:     t5a_fleak_1_6 = fit_sparc_parameter(sparc_train, "T5A", 1.0 / 6.0, loss_metric="sum_chi2_red")
388:     t5b_tot_chi2 = fit_sparc_parameter(sparc_train, "T5B", f_leak_frozen, loss_metric="total_chi2")
389:     t5b_med_chi2 = fit_sparc_parameter(sparc_train, "T5B", f_leak_frozen, loss_metric="median_chi2_red")
390: 
391:     print(
392:         f"   T5-A frozen sigma_ref = {t5a_deciding['fitted_param']:.6f} kpc; "
393:         f"T5-B frozen k = {t5b_deciding['fitted_param']:.6f}"
394:     )
395: 
396:     freeze_t5 = {
397:         "test_id": "T5 (T5-A Primary Pillar 4, T5-B & T5c Secondary)",
398:         "frozen_at": now_iso,
399:         "f_leak_frozen_from_T2A_PantheonPlus": f_leak_frozen,
400:         "T5A_deciding_training_fit": t5a_deciding,
401:         "T5B_deciding_training_fit": t5b_deciding,
402:         "sensitivity_training_fits": {
403:             "T5A_total_chi2_loss": t5a_tot_chi2,
404:             "T5A_median_chi2_red_loss": t5a_med_chi2,
405:             "T5A_f_leak_1_over_6": t5a_fleak_1_6,
406:             "T5B_total_chi2_loss": t5b_tot_chi2,
407:             "T5B_median_chi2_red_loss": t5b_med_chi2,
408:         },
409:         "scripts_sha256": scripts_hashes,
410:     }
411:     freeze_t5_path = results_dir / "FREEZE_T5.json"
412:     freeze_t5_path.write_text(json.dumps(freeze_t5, indent=2), encoding="utf-8")
413: 
414:     # 6. Run T6 SH0ES calibrator fit and freeze (FREEZE_T6.json)
415:     print("4. Running T6 SH0ES Cepheid calibrator fit...")
416:     pantheon_full = load_pantheon_plus_full(root / "data" / "pantheon_plus")
417:     t6_cal_fit = fit_t6_calibrators(pantheon_full)
418:     print(f"   T6 frozen M_B = {t6_cal_fit['M_B_fixed']:.6f} +/- {t6_cal_fit['sigma_M_B_fixed']:.6f} mag")
419: 
420:     freeze_t6 = {
421:         "test_id": "T6 (Local H0 Regional Heterogeneity Secondary Test)",
422:         "frozen_at": now_iso,
423:         "calibrator_fit": t6_cal_fit,
424:         "scripts_sha256": scripts_hashes,
425:     }
426:     freeze_t6_path = results_dir / "FREEZE_T6.json"
427:     freeze_t6_path.write_text(json.dumps(freeze_t6, indent=2), encoding="utf-8")
428: 
429:     # 7. Write master FIXED_VALUES.json with SHA-256 of each FREEZE_*.json file
430:     freeze_files = ["FREEZE_T1.json", "FREEZE_T2.json", "FREEZE_T4.json", "FREEZE_T5.json", "FREEZE_T6.json"]
431:     freeze_hashes = {
432:         fname: hashlib.sha256((results_dir / fname).read_bytes()).hexdigest()
433:         for fname in freeze_files
434:     }
435: 
436:     fixed_values = {
437:         "frozen_at": now_iso,
438:         "seed": SEED,
439:         "freeze_file_sha256": freeze_hashes,
440:         "summary_of_frozen_parameters": {
441:             "T2_A_PantheonPlus": t2_by_id["T2-A-Pantheon+_deciding"]["frozen_quantities"],
442:             "T2_A_DES_Dovekie": t2_by_id["T2-A-DES-Dovekie_deciding"]["frozen_quantities"],
443:             "T4b_tau_lag_myr": t4_fit_deciding["tau_lag_myr"],
444:             "T4b_tau_lag_gyr": t4_fit_deciding["tau_lag_gyr"],
445:             "T5_A_sigma_ref_kpc": t5a_deciding["fitted_param"],
446:             "T5_B_k": t5b_deciding["fitted_param"],
447:             "T6_M_B_fixed_mag": t6_cal_fit["M_B_fixed"],
448:             "T6_sigma_M_B_fixed_mag": t6_cal_fit["sigma_M_B_fixed"],
449:         },
450:         "scripts_sha256": scripts_hashes,
451:     }
452:     fixed_values_path = results_dir / "FIXED_VALUES.json"
453:     fixed_values_path.write_text(json.dumps(fixed_values, indent=2), encoding="utf-8")
454:     print("ALL PART 8 FIXES COMPLETED AND FROZEN.")
455:     print(json.dumps(fixed_values["summary_of_frozen_parameters"], indent=2))
456: 
457: 
458: if __name__ == "__main__":
459:     main()
```

---

## 4. Could Any Frozen Parameter Value Have Changed Between `06:29:35` and the Last Write (`07:06:21`)? Comparison Against Earlier Records

### 4a. Existence of Earlier Records Prior to `07:06:21`
- **No earlier record (hash, printed value, backup file in `_TRASH/`, or log line in `ACTIVITY_LOG.md`) of the frozen parameters exists in the workspace prior to `07:06:21`.**
- Specifically:
  1. The files created by the unlogged Run 1 (`CreationTime` `06:25:21`–`06:26:56`) were overwritten in place by Run 2 (`LastWriteTime` `07:04:55`–`07:06:21`) without being backed up to `_TRASH/` and without having their values or SHA-256 hashes recorded in `ACTIVITY_LOG.md`.
  2. `ACTIVITY_LOG.md` line 158 (logged at `07:06:21`) records completion (`Rhat-1 < 0.01, ESS > 1000`) but does not print the numerical parameter values or file hashes.
  3. The earliest record on disk of the frozen parameter values and `FREEZE_*.json` SHA-256 hashes is `results/FIXED_VALUES.json` itself (`LastWriteTime = 2026-10-30T07:06:21.2923399`), followed by `_TRASH/RESULTS_v1_superseded.md` (`CreationTime = 2026-10-30T07:52:12` on `results/RESULTS.md`, `LastWriteTime = 2026-10-30T07:54:40.7428420`) and `RESULTS_v1.sha256` (`LastWriteTime = 2026-10-30T07:59:20.1308457`). All three contain identical parameter values and identical SHA-256 hashes.

### 4b. Whether Any Frozen Parameter Value Could Have Changed
We evaluate both (i) the interval `06:29:35` to `07:06:21` **within Run 2**, and (ii) the overwrite of **unlogged Run 1 (`06:25:21`–`06:26:56`) by Run 2 (`07:04:55`–`07:06:21`)**:

1. **Within Run 2 (`06:29:35` start to `07:04:55`–`07:06:21` file writes):**
   - At `06:29:35`, Run 2 had just started (`main()` line 250) and had not yet computed its `T2-A`, `T4b`, `T5`, or `T6` fits. Each `FREEZE_*.json` file was written **once** during Run 2 as its step finished (`07:04:55.876` for T1/T2/T4, `07:06:18.052` for T5, `07:06:21.272` for T6) and was never modified after `07:06:21.292`.

2. **Between Unlogged Run 1 (`06:25:21`–`06:26:56`) and Logged Run 2 (`07:04:55`–`07:06:21`):**
   - **`FREEZE_T1.json` (`N_s = 19`, `N_r = 133`, `Omega_b_structural = 0.05263157894736842`, and prior bounds):** **Could NOT have changed.** These are literal constants hardcoded in `scripts/run_part8_fixes.py` lines 316–330.
   - **`FREEZE_T4.json` (`tau_lag_myr = 805`, `tau_lag_gyr = 0.805`, `train_acc = 0.875`, `n_train_classified = 8`, `n_train_correct = 7`):** **Could NOT have changed.** `FREEZE_T4.json` is computed deterministically by `load_mergers_csv()` and `fit_tau_lag_hard_step()` in `scripts/clusters_t4.py` (`LastWriteTime = 2026-10-30T05:33:06.5289804`, `__pycache__/clusters_t4.cpython-314.pyc` `LastWriteTime = 2026-10-30T05:33:34.1812833`) from `data/MERGERS.csv` (`LastWriteTime = 2026-10-30T05:31:42.9962503`). Neither `scripts/clusters_t4.py` nor `data/MERGERS.csv` was modified after `05:33:06`, and neither uses `cosmology.py` or `compute_split_rhat_and_ess()`.
   - **`FREEZE_T6.json` (`n_calibrators = 77`, `M_B_fixed = -19.24888455`, `sigma_M_B_fixed = 0.03010569`, `var_M_B_fixed = 0.0009063526713554595`):** **Could NOT have changed.** `FREEZE_T6.json` is computed deterministically by `load_pantheon_plus_full()` and `fit_t6_calibrators()` in `scripts/local_h0_t6.py` (`LastWriteTime = 2026-10-30T05:37:45.8417485`, `__pycache__/local_h0_t6.cpython-314.pyc` `LastWriteTime = 2026-10-30T05:38:17.9453097`) from `data/pantheon_plus/`. Neither `scripts/local_h0_t6.py` nor `data/pantheon_plus/` was modified after `05:37:45`, and neither uses `cosmology.py` or `compute_split_rhat_and_ess()`.
   - **`FREEZE_T2.json` (`Omega_bc_median = 0.308725`, `f_leak = 0.189038`, `R_pred = 4.865772`, etc.) and `FREEZE_T5.json` (`fitted_param` depending on `f_leak_frozen`):** **Could have changed between Run 1 (`06:25:21`) and Run 2 (`07:04:55`), and whether they changed is NOT RECORDED.** Between Run 1 (`06:26:56`) and Run 2 (`06:29:35`), two code edits were made:
     1. `2026-10-30T06:28:52`: `Vectorized comoving-distance cumulative Hermite quadrature in scripts/cosmology.py.` (`ACTIVITY_LOG.md` line 156; `scripts/cosmology.py` `LastWriteTime = 2026-10-30T06:28:52.0120000`).
     2. `2026-10-30T06:29:25`: `Updated split-Rhat quadrant block diagnostic in scripts/run_part8_fixes.py.` (`ACTIVITY_LOG.md` line 157; `scripts/run_part8_fixes.py` `LastWriteTime = 2026-10-30T06:29:25.4693164`).
     In `scripts/run_part8_fixes.py` (lines 171–175), `compute_split_rhat_and_ess(chain)` directly controls a `while` loop that extends the `emcee` chain by 2,000 steps up to 2 times (`n_prod` = 6,000 or 8,000 instead of 4,000) whenever `diag["max_rhat_minus_1"] >= 0.01 or diag["min_ess"] <= 1000.0`:
     ```python
     171:     while (diag["max_rhat_minus_1"] >= 0.01 or diag["min_ess"] <= 1000.0) and ext_count < 2:
     172:         state = sampler.run_mcmc(state, 2000, progress=False)
     173:         chain = sampler.get_chain()
     174:         diag = compute_split_rhat_and_ess(chain)
     175:         ext_count += 1
     ```
     If the pre-`06:29:25` split-$\hat{R}$ calculation triggered chain extension in Run 1 (or if the `06:28:52` vectorization in `cosmology.py` altered floating-point rounding along the 160,000 MCMC steps), then `Omega_bc_median` and `f_leak` in `FREEZE_T2.json` (and `FREEZE_T5.json` which takes `f_leak_frozen` as input) would have differed between Run 1 (`06:25:21`–`06:26:52`) and Run 2 (`07:04:55`–`07:06:18`). Because Run 1's files were overwritten without logging or backup, any difference is **not recorded**.

---

## 5. Which Test Results (`T1`–`T6`) Were Computed Before vs. After `07:06:21`

From `ACTIVITY_LOG.md`, `results/part9_cosmology_results.json`, `results/results.json`, and filesystem timestamps:

### 5a. Computed BEFORE `07:06:21`
- **Test Verdicts / Held-Out Test Evaluations (`T1`–`T6`):** **NONE.** Zero test verdicts or held-out test evaluations were computed before `07:06:21`.
- **Pre-Test Validation Gates (`G9-a` to `G9-d`):** Computed at `2026-10-30T05:02:56` (`ACTIVITY_LOG.md` line 134; `results/validation_gates_g9.json` `LastWriteTime = 2026-10-30T05:02:56.8045128`).
- **Part 8 Parameter-Fixing / Training-Half Fits (`scripts/run_part8_fixes.py`, completed at `07:06:21`):**
  - `T1` structural constants and priors (`FREEZE_T1.json`, `LastWriteTime = 07:04:55.8766875`).
  - `T2-A` background flat $w_0 w_a\text{CDM}$ MCMC chains fixing $\Omega_{bc,\text{med}}$, $f_{\text{leak}}$, and $R_{\text{pred}}$ (`FREEZE_T2.json`, `LastWriteTime = 07:04:55.8766875`). *(Note: Although the posterior medians `R_pred = 4.865772 +/- 0.114933` and `4.904531 +/- 0.109383` were fixed in `FREEZE_T2.json` at `07:04:55`, the formal comparison against Planck $R_{\text{Planck}} = 5.36 \pm 0.05$ and the `T2-A`, `T2-N1`, `T2-N2`, and `T2-B` test evaluations ran in Part 9 after `07:06:21`.)*
  - `T4b` odd-cluster training-half cutoff fit $\hat{\tau}_{\text{lag}} = 805\text{ Myr}$ (`FREEZE_T4.json`, `LastWriteTime = 07:04:55.8776874`).
  - `T5-A` and `T5-B` SPARC training-half (`88` galaxies) grid fits $\hat{\sigma}_{\text{ref}} = 9.212795\text{ kpc}$ and $\hat{k} = 2.928045$ (`FREEZE_T5.json`, `LastWriteTime = 07:06:18.0522497`).
  - `T6` SH0ES Cepheid calibrator fit $M_B = -19.24888455 \pm 0.03010569\text{ mag}$ (`FREEZE_T6.json`, `LastWriteTime = 07:06:21.2723400`).

### 5b. Computed AFTER `07:06:21` (All Test Results `T1`–`T6`)
| Test / Sub-Test | Script | Start Time (Local) | Completion / Write Time (Local) | Output File & Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **`T1-L1`** (Primary Pillar 1), **`T1-Sign`** (Secondary), **`T1` Sensitivity** | `scripts/run_part9_cosmology_tests.py` | `2026-10-30T07:06:57` (`__pycache__/run_part8_fixes.cpython-314.pyc` created at `07:06:57.4973934` on import) | `2026-10-30T07:45:34.8158655` (`ACTIVITY_LOG.md` line 159: `07:45:35`) | `results/part9_cosmology_results.json` line 2: `"completed_at": "2026-10-30T07:45:34"` |
| **`T2-A`** (Primary Pillar 2), **`T2-N1`** (Secondary), **`T2-N2`** (Secondary), **`T2-B`** (Sensitivity) | `scripts/run_part9_cosmology_tests.py` | `2026-10-30T07:06:57` | `2026-10-30T07:45:34.8158655` (`ACTIVITY_LOG.md` line 159: `07:45:35`) | `results/part9_cosmology_results.json` line 2: `"completed_at": "2026-10-30T07:45:34"` |
| **`T6`** (Secondary: Hubble-flow regional $H_0$ heterogeneity) & **Section 6 Coincidence Window** | `scripts/run_part9_cosmology_tests.py` | `2026-10-30T07:06:57` | `2026-10-30T07:45:34.8158655` (`ACTIVITY_LOG.md` line 159: `07:45:35`) | `results/part9_cosmology_results.json` line 2: `"completed_at": "2026-10-30T07:45:34"` |
| **`T4b`** (Primary Pillar 3 held-out test evaluation & sensitivity variants) & **`T4a`** (Exploratory) | `scripts/run_part10_astrophysics_and_verdict.py` | After `07:46:30` / `07:47:15` (`ACTIVITY_LOG.md` lines 161–162) | `2026-10-30T07:47:30.6690619` (`ACTIVITY_LOG.md` line 163: `07:47:30`) | `results/results.json` line 3: `"generated_at": "2026-10-30T07:47:30"` |
| **`T5-A`** (Primary Pillar 4 held-out test evaluation), **`T5-B`** (Secondary), **`T5c`** (Secondary DF2), **RAR Benchmark** | `scripts/run_part10_astrophysics_and_verdict.py` | After `07:46:30` / `07:47:15` (`ACTIVITY_LOG.md` lines 161–162) | `2026-10-30T07:47:30.6690619` (`ACTIVITY_LOG.md` line 163: `07:47:30`) | `results/results.json` line 3: `"generated_at": "2026-10-30T07:47:30"` |
| **Holm-Bonferroni Control, Overall Model Verdict (`MODEL FALSIFIED (FAIL)`), and Figures 1–5** | `scripts/run_part10_astrophysics_and_verdict.py` | After `07:46:30` / `07:47:15` (`ACTIVITY_LOG.md` lines 161–162) | `2026-10-30T07:47:26.588`–`07:47:30.669` (`ACTIVITY_LOG.md` line 163: `07:47:30`) | `results/results.json` & `results/figures/fig1..fig5.png` |

---

## 6. Conclusion in Plain Language

1. **Why `frozen_at` is `06:29:35` while `LastWriteTime` is `07:04:55`–`07:06:21` (Within the Final Logged Run):**
   - Inside the final run of `scripts/run_part8_fixes.py` (Run 2), `2026-10-30T06:29:35` is **not** an earlier file-write timestamp; it is the timestamp captured **at the start of `main()` (line 250)** before the fits began (`now_iso = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")`, corroborated by `scripts/__pycache__/cosmology.cpython-314.pyc` compiled at `2026-10-30T06:29:35.9201379`).
   - The script then took **35 minutes and 20 seconds** (`06:29:35` to `07:04:55.876`) to run the six `T2-A` MCMC chains (`lines 304–305`) before writing `FREEZE_T1.json`, `FREEZE_T2.json`, and `FREEZE_T4.json` at `07:04:55.876`–`07:04:55.877`, took **1 minute and 22 seconds** (`07:04:55.877` to `07:06:18.052`) to run the seven `T5` SPARC training-half grid fits (`lines 381–389`) before writing `FREEZE_T5.json` at `07:06:18.052`, and took **3.2 seconds** (`07:06:18.052` to `07:06:21.272`) to run the `T6` Cepheid calibrator fit (`lines 416–417`) before writing `FREEZE_T6.json` (`07:06:21.272`) and `FIXED_VALUES.json` (`07:06:21.292`). Every file was stamped with the single `now_iso` string (`"2026-10-30T06:29:35"`) captured when `main()` started.
   - None of these files were modified after `07:06:21.292` (their SHA-256 hashes in `FIXED_VALUES.json` match `RESULTS_v1.sha256` at `07:59:19` and the current files on disk).

2. **What Happened Between `06:25` and `07:06` Across Runs (Run 1 vs. Run 2 Verdict by File):**
   - NTFS `CreationTime` metadata proves that an earlier, unlogged run of `scripts/run_part8_fixes.py` (Run 1) first created `FREEZE_T1.json`, `FREEZE_T2.json`, and `FREEZE_T4.json` at `06:25:21.685`–`06:25:21.688`, `FREEZE_T5.json` at `06:26:52.073`, `FREEZE_T6.json` at `06:26:55.986`, and `FIXED_VALUES.json` at `06:26:56.006`.
   - Between Run 1 (`06:26:56`) and Run 2 (`06:29:35`), `scripts/cosmology.py` was modified at `06:28:52` (`ACTIVITY_LOG.md` line 156: `"Vectorized comoving-distance cumulative Hermite quadrature in scripts/cosmology.py"`) and `scripts/run_part8_fixes.py` was modified at `06:29:25` (`ACTIVITY_LOG.md` line 157: `"Updated split-Rhat quadrant block diagnostic in scripts/run_part8_fixes.py"`). Run 2 then overwrote all six files at `07:04:55`–`07:06:21`.
   - Therefore, comparing the `07:04:55`–`07:06:21` files against the overwritten `06:25:21`–`06:26:56` files:
     - **`FREEZE_T1.json`, `FREEZE_T4.json`, and `FREEZE_T6.json`:** **Innocent rewrite (same parameter values, written later).** Their parameter values come from hardcoded constants (`FREEZE_T1.json`, `run_part8_fixes.py` lines 316–330) or deterministic fits in `scripts/clusters_t4.py` (`LastWriteTime = 05:33:06.5289804`) and `scripts/local_h0_t6.py` (`LastWriteTime = 05:37:45.8417485`) on unmodified datasets (`data/MERGERS.csv` `LastWriteTime = 05:31:42.9962503` and `data/pantheon_plus/`). Neither script was modified after `05:37:45` and neither calls `cosmology.py` or `compute_split_rhat_and_ess()`; only the `"frozen_at"` timestamp and `"scripts_sha256"` dictionary changed when Run 2 overwrote them.
     - **`FREEZE_T2.json` (and `f_leak`-dependent `FREEZE_T5.json`):** **Undeterminable (`not recorded`).** Because `scripts/cosmology.py` was modified at `06:28:52` and the `compute_split_rhat_and_ess()` convergence check (which controls whether `run_single_t2a_mcmc_worker` extends the MCMC chain from 4,000 to 6,000 or 8,000 production steps on lines 171–175 of `scripts/run_part8_fixes.py`) was modified at `06:29:25`, and because no values or hashes from the `06:25:21` Run 1 files were logged or backed up before Run 2 overwrote them at `07:04:55`, whether the `T2-A` MCMC parameter values in `FREEZE_T2.json` (and the resulting `T5` fit values in `FREEZE_T5.json`) changed between `06:25:21` and `07:04:55` is **not recorded** and therefore **undeterminable**.
   - **Pre-Test Ordering Guarantee:** All held-out test evaluations and test verdicts (`T1-L1`, `T1-Sign`, `T2-A`, `T2-N1`, `T2-N2`, `T2-B`, `T4b`, `T4a`, `T5-A`, `T5-B`, `T5c`, `T6`) were computed **after** `07:06:21` (Part 9 ran `07:06:57`–`07:45:34`; Part 10 finished at `07:47:30`), and no `FREEZE_*.json` file was modified after `07:06:21.292`.
