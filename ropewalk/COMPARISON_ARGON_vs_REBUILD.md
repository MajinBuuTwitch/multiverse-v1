# MULTIVERSE v1 — Argon vs Blind Rebuild: Comparison
2026-10-30 · Argon (Gemini) results: RESULTS_v1 (b02000c9…) · Blind rebuild (Claude Opus, Antigravity then Claude Code): REBUILD_RESULTS_v1 (93a154fb…)
The rebuild was built from the frozen v4 rulebook only, without access to Argon's code or results, and froze its numbers before this comparison.

## Test by test

| Test | Argon | Rebuild | Agree? |
|---|---|---|---|
| G9-a (BAO-only Ωm) | 0.29718 ± 0.0086, PASS | 0.2977 ± 0.0088, PASS | Yes |
| G9-b (compressed CMB vs Chen+19) | PASS (max 0.025σ) | **FAIL** (h 0.577σ vs 0.3σ tolerance) | **No (see Finding 1)** |
| G9-c | PASS | PASS | Yes |
| G9-d (kernel limit) | 1.44e-11, PASS | 1.440e-11, PASS | Yes |
| T1-L1 (unwinding curve) | A −1.71/−2.58, B +5.46/+7.36 → INCONCLUSIVE | A −1.35/−2.08, B +5.55/+7.48 → INCONCLUSIVE | Verdict yes |
| T1-Sign (w0 > −1) | 0.9960/0.9992 → PASS | 0.99638/0.99909 → INCONCLUSIVE (gate) | Numbers yes; verdict differs via G9-b |
| T2-A (leak ratio vs Planck) | −3.74σ/−3.58σ → FAIL | −3.447σ/−3.224σ → INCONCLUSIVE (gate) | Both beyond the 2σ FAIL line; verdict differs via G9-b |
| T2-N1 (Ωb = 1/19 vs Planck) | +3.87σ FAIL | 3.874σ FAIL | Yes |
| T2-N2 (implied H0 vs Planck) | −3.72σ FAIL | −3.714σ FAIL | Yes |
| T4b (cluster lag) | n_train 8, n_test 5 → INCONCLUSIVE | n_train 1, n_test 0 → INCONCLUSIVE | Verdict yes; inputs differ (Finding 2) |
| T5-A (rotation curves) | σ_ref 9.213 kpc, median χ²_red 45.13, F<2 0.0690 → FAIL | σ_ref 9.344 kpc, median 45.91, F<2 0.0690 → FAIL | Yes |
| T5-B | median 23.74 → FAIL | median 23.43 → FAIL | Yes |
| T5c (NGC 1052-DF2) | 0.99e8 M☉ → PASS | 0.986e8 M☉ → PASS | Yes |
| T6 (regional H0) | p = 0.3478 → FAIL | p = 0.34784 → FAIL | Yes (identical) |
| Model level | MODEL FALSIFIED | MODEL FALSIFIED (MODEL INCONCLUSIVE only under the non-literal reading of D11) | Yes under the literal rulebook |

## Finding 1 — the one real disagreement: how r_s(z*) is computed for gate G9-b
- The registered equation (a5) is the full sound-horizon integral. The rebuild coded it literally; G9-b then fails (h off by 0.58σ against a 0.3σ tolerance). Argon's code uses Chen, Huang & Wang (2019)'s own early-universe form (ω_r = 1/24185, about 1.1% below the physical radiation density, and the 0.06 eV neutrino counted as pure matter), which gives an r_s(z*) about 0.18% LARGER than the registered integral (+0.29% from the low ω_r, −0.12% from the neutrino treatment; dark energy contributes <1e-7). A larger r_s lowers h at fixed ℓ_A, which is why Argon's h passes G9-b. Argon's log records this function at the gate stage as a "bug fix" (05:02:46) ten seconds before the gates passed (05:02:56); it was not logged as a departure from (a5).
- The final reviewer judged Argon's form "the consistent one for the Chen prior" (reproducing Chen's posteriors with Chen's own method), and also confirmed the literal form fails G9-b.
- Consequence: under the literal (a5), G9-b fails, so T2-A, T1-L1 and T1-Sign are INCONCLUSIVE by the gate rule, even though T2-A's statistic sits 3.2–3.4σ from the Planck value, about 1.2–1.4σ past its 2σ FAIL line. Under Argon's form, T2-A is FAIL and T1-Sign PASS.
- What does not change: T1-L1 is INCONCLUSIVE either way, and the model is FALSIFIED either way, through T5-A (both pipelines agree it fails by a wide margin).
- Required: the paper must state this ambiguity plainly and report both readings. It must not present T2-A's FAIL as unconditional.

- Verification: the rebuild's numbers in this table were checked against its frozen files (REBUILD_RESULTS.md, results.json; hashes match the frozen manifest 93a154fb…). Its validation script confirms its r_s(z*) is the registered full integral (agreement ~1e-11) and matches CAMB to 4.9e-5, with no calibration factor on r_s(z*).

## Finding 2 — T4b inputs: how many clusters have complete measurements
- Argon classified 13 clusters using default or zero positional errors where the source paper gave none (flagged as M3 in the final review). The rebuild applied the registered missing-data rule strictly and found only one cluster (MACS J0025.4-1222) with complete positions and errors.
- Both end INCONCLUSIVE. Any public claim based on "13 classifiable clusters" depends on Argon's lenient inputs and should not be made.

## Robust across both pipelines (safe to state)
1. Version 1 is falsified under its own frozen rules: the galaxy rotation-curve pillar fails decisively in both (median misfit ~45 against a pass line of 1.5; fits 6 of 87 held-out galaxies).
2. The one-in-nineteen ordinary-matter share is ~3.9σ above Planck; the implied Hubble constant (~65.2) is ~3.7σ below Planck.
3. The leak-ratio prediction lands 3.2–3.7σ from Planck (past the 2σ FAIL line in every run). It's a FAIL under one reading of the gate rules and INCONCLUSIVE under the other, so describe the miss, not the verdict.
4. The unwinding dark-energy curve is neither confirmed nor ruled out; the data favour w0 > −1 at ~99.6–99.9%.
5. No regional variation in the local expansion rate (p ≈ 0.35, identical in both).
6. NGC 1052-DF2 is allowed (with the same caveat: only via the wide blur that fails the rotation curves).
7. Too few colliding clusters have complete measurements to test the lag.
