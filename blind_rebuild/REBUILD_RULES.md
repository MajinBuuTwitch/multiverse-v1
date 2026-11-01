# REBUILD_RULES.md — Blind Independent Rebuild (read this first, follow it always)

## What this workspace is
An independent re-implementation of a pre-registered set of cosmology tests for a speculative model
("the cable" / Mandarano Model v1). Another agent, in a different workspace, built the original analysis.
Your job is to build your OWN analysis from the frozen rulebook alone, run it, and report results.
The value of this work comes from your being blind to the original analysis. Protect that.

## Inputs you may use
- ONLY the files inside this folder and its `_ORIGINALS` subfolder.
- The governing files are, in order of precedence: PREREG.md, MULTIVERSE_STAGE1_EQUATIONS.md, ASSUMPTIONS.md,
  then STAGE1_PART1/2/3. Where any earlier file (MULTIVERSE_TESTS_v1.md, MULTIVERSE_EQUATION_SHEET_v1.md,
  MULTIVERSE_DATASETS_v1.md) disagrees with them, the governing files win.
- The web: ONLY to download the datasets the governing files register, to read the source papers they
  cite (including the tables named for the T4b cluster positions), and to read package documentation.

## Forbidden (blindness rules)
- Never read, list, search, or open anything outside this folder. In particular, never touch anything under
  `D:\Argon_Code\` or any folder named Ropewalk, and never search the disk for related files.
- Never look for, request, or use the original analysis's code, logs, data manifest, or results.
  If you come across any of them by accident, stop reading, log it in ACTIVITY_LOG_REBUILD.md, and continue.
- Don't ask Gregory for the original results. They are compared outside this workspace after you freeze yours.

## First step
Verify the frozen package: compute the SHA-256 of every file in `_ORIGINALS` that is listed in
PREREG_v4.sha256 and confirm each one matches. Log the result. If any governing file fails, stop and report.

## How to build (independence by design)
- Write your own code from the equations and decision rules. Don't reuse any code you didn't write here.
- Where the rulebook allows a choice of numerical method, deliberately take an independent route and log it:
  - expansion history and distances: integrate the Friedmann equation as an ODE (e.g. solve_ivp) and
    cross-check against a separate quadrature (e.g. Gauss–Legendre) at a few redshifts;
  - the 3D Gaussian rotation-curve kernel: implement the closed form AND validate it against a direct
    Monte Carlo and the noncentral chi-square CDF;
  - samplers: your own choice; log which one and why; use the registered convergence criteria
    (if none, Gelman–Rubin R̂ − 1 < 0.01 and report effective sample sizes).
- Sound horizon / recombination redshift: use the registered fast method. Never call a full Boltzmann code
  (CAMB/CLASS) inside a sampling loop; if a Boltzmann-level value is required, build an interpolation table
  once, validate it, and sample from the table.
- Run independent fits in parallel across CPU cores, leaving about 4 threads free.

## Rules that never bend
- Never change a registered input, prior, dataset, threshold, sample, selection rule, or decision rule.
- Any unavoidable departure goes in DEVIATIONS_REBUILD.md BEFORE computing the affected test, with what,
  why, and expected effect. Then continue.
- Bug fixes only as logged fixes. Never change code because a result came out a particular way.
- Validation gates: follow the registered gate-to-test mapping exactly.
- If a test truly cannot be run, apply its registered INCONCLUSIVE trigger, log why, and continue.

## Files and logging
- `_ORIGINALS` is read-only. Never delete anything anywhere: move unwanted files to `_TRASH\`.
- ACTIVITY_LOG_REBUILD.md is append-only: log every action with a timestamp.
- Data: download every registered dataset yourself. Record source URL, version/release, download time and
  SHA-256 of each file in DATA_MANIFEST_REBUILD.sha256, and stamp it with OpenTimestamps
  (pip install opentimestamps-client; `ots stamp`) BEFORE running any fit.

## PHASE 1: Rebuild (do this now)
1. Verify the frozen package (above).
2. Download and fingerprint the data (above).
3. Implement and run every SCORED test, the validation gates, the multiple-testing correction, and the
   model-level verdict exactly as PREREG.md defines them. Sensitivity analyses: run them and report them in a
   separate section labelled NON-DECIDING.
4. One entry point (run_all_rebuild.py) reproduces everything from the downloaded data. Pin package versions
   in requirements_rebuild.txt, fix and log all random seeds, and save chains, tables and figures under
   results_rebuild/.
5. REBUILD_RESULTS.md: for every scored test, the registered statistic, its value with uncertainty, the
   threshold, the verdict (PASS / FAIL / INCONCLUSIVE), then the multiple-testing correction, then the
   model-level verdict. Also include your extracted T4b cluster position table (with the paper, table/figure
   and value for each entry), the method choices you made, and every DEVIATIONS_REBUILD.md entry.
6. Freeze: hash all outputs, code and REBUILD_RESULTS.md into REBUILD_RESULTS_v1.sha256, and stamp it with
   OpenTimestamps.
7. Report in chat, then STOP and wait for Gregory. Your report must quote numbers exactly as they appear in
   REBUILD_RESULTS.md. Don't summarize from memory.

## PHASE 2: Head-to-head (only after Phase 1 is frozen AND Gregory says go)
A supplementary, NOT pre-registered comparison of the model against standard ΛCDM on the same registered
data: Bayesian evidence via nested sampling (e.g. dynesty or nautilus), for each supernova compilation
separately. Write the priors for both models into HEAD_TO_HEAD_PLAN.md and hash it BEFORE running.
Report ln(Bayes factor) with uncertainty, labelled "supplementary analysis, not pre-registered", in
HEAD_TO_HEAD_RESULTS.md, then freeze and stamp it the same way.

## PHASE 3: Injection tests (later; Gregory will supply what's needed)
Not now. Instructions will come separately.
