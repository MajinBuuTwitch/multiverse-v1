# Review V3: Final Pre-Data Gate Check (Mandarano Model Stage 1)

Scope: REVIEW_V2.md, REVIEW_RESPONSE_v2.md, PREREG.md, ASSUMPTIONS.md, MULTIVERSE_STAGE1_EQUATIONS.md (EQ), STAGE1_PART1/2/3. I checked everything against the governing text, not against the response's claims. Numerics were rerun in python/scipy 1.18.1. Cited numbers were checked against arXiv:2503.14738 (DESI DR2) and arXiv:2607.27410. Hash integrity was out of scope.

## Verdict: FIX FIRST

The V2 forks are closed in the text. T2-A, T1-L1, T4b ages, floor and metric, T2-N2, T5-B and the T6 configuration each have one deciding version. The precedence clause appears in every file. T4a is locked. N10 is disclosed. The model-level map is exhaustive. Four gaps remain where a pillar or a scored test still depends on a choice that would be made after the data are seen. All four are text fixes that need no new analysis. After they are made, re-hash and re-timestamp.

---

## BLOCKER

**B1. The T5-A fitting step (Pillar 4) is underspecified.** PREREG §5.6 item 3 names the σ_ref grid and the optimizer but **not the quantity it minimizes on the 88 training galaxies**. Total χ² over all points, the sum of per-galaxy χ²_red, and the median χ²_red each give a different σ̂_ref. That σ̂_ref then decides T5-A, T5-B (k) and T5c. EQ and the PART files don't define it either, and TESTS_v1 is superseded for T5. Two smaller gaps sit in the same step. In the tail, Σ_b(r_max) is undefined, because SPARC gives SBdisk and SBbul but no gas surface density, and the text doesn't say whether the tail mass enters v_bar or only M_sh. The split of the "400-point linear-plus-log" grid is also not stated.
*Fix:* "σ̂_ref (k̂) = argmin Σ_{g∈train} Σ_j [(V_obs − v_model)/errV]² (total χ² over all training points)" (or name another objective now). Define Σ_b(r_max) from named SPARC columns (e.g. Υ_d·SBdisk + Υ_b·SBbul + 1.33·Σ_HI, with its source), state that the tail enters M_sh only (or both), and give the grid split (e.g. 200 linear on [0, r_1] + 200 log on [r_1, r_max]).

**B2. The T4b observables (Pillar 3) are not mechanically defined.** The classification uses x_S, x_G, x_I and σ_S, σ_G, σ_I (§5.5), but the table registers only a source paper and subcluster. Nothing says whether I is the lensing **peak** or the **centroid** (EQ treats β_peak and β_centroid as different predictions), whether S is the BCG or a luminosity or number-weighted centroid, whether G is the X-ray peak or the centroid, or which uncertainty enters σ_diff (1σ radial, per axis, or bootstrap). Nothing covers a named source that lacks one of the three positions or its error. With a hand-built sample whose outcomes are known (the N10 disclosure), each of these is a live choice that can flip a classification.
*Fix:* Before Stage 2, tabulate the 48 positions and 48 σ values with table and row pointers, or register a rule: "I = weak-lensing convergence peak, G = X-ray surface-brightness peak, S = luminosity-weighted galaxy centroid (BCG if no centroid is given), σ = the source's 68% positional error. A system whose primary source lacks any of the three, or any σ, is unclassified."

**B3. Gate failure (G9) is an escape hatch with no defined scope.** G9 says all four gates must pass "before any model test is executed", and T2-A goes INCONCLUSIVE "only if validation (G9) ... fails". As written, a failure of **any** gate makes **every** test INCONCLUSIVE, including T2-A (forecast FAIL at ~3.7σ) and T4b. That forces MODEL INCONCLUSIVE. G9-c is a real risk. It asks the pipeline, with the Chen 2019 compressed PR3 ΛCDM-derived prior, to reproduce a full-likelihood DESI+CMB+Dovekie w0wa result to within 0.3σ. It is also undefined whether G9-a and G9-c run with the standard DESI Lyα rows or with the registered 2607.27410 replacement (G6). The text also doesn't say whether an analyst may change anything and rerun after a gate fails.
*Fix:* (i) Map each gate to the tests that depend on it: G9-a/b/c to T1-L1, T1-Sign, T2-A and T2-B; G9-d to T5-A/B/c; T4b, T6, T2-N1 and T2-N2 depend on no gate. T5 also needs a converged T2-A-Pantheon+. (ii) State the dataset configuration of G9-a and G9-c. (iii) Code bug fixes are allowed and logged, but no registered dataset, prior, likelihood, formula or threshold may change to pass a gate. A gate that still fails makes only its mapped tests INCONCLUSIVE. (iv) Optionally make G9-c report-only or widen its tolerance, decided now.

**B4. The T6 sparse-pixel merge target is undefined.** In HEALPix N_side = 1 RING, each equatorial pixel (4–7, centred on b = 0, l = 0°/90°/180°/270°) spans two longitude quadrants and shares edges with two north and two south polar pixels. That gives four candidates, so "adjacent same-longitude-quadrant higher-|b| neighbour" names none. These are exactly the zone-of-avoidance pixels, and with roughly 300–500 Hubble-flow SNe at 0.023–0.15 over 12 pixels the < 10 trigger is plausible. T6 is scored, and p_T6 enters the three-test Holm family that can downgrade a T1-L1 or T4b PASS.
*Fix:* "A pixel with N_SN < 10 is dropped (or: merged into the edge-sharing polar pixel with the lowest RING index); if a merged pixel is still < 10 it is dropped; N_pix and dof count only retained pixels."

---

## MAJOR

**M1. The T1-L1 joint FAIL rule is asymmetric, undeclared and misreported.** PREREG §5.1: joint FAIL needs **both** runs to be per-run FAIL. REVIEW_RESPONSE_v2 N5 states "joint FAIL if **either** run is FAIL". T2-A and T1-Sign both use "either". The forecast is B ≈ 7–8 for Pantheon+ (INCONCLUSIVE) and ≈ 9–10 for Dovekie (around FAIL), so this rule alone likely decides FAIL vs INCONCLUSIVE for Pillar 1. Precedence locks it at "both", so it is mechanical, but the intent is contradicted. *Fix now:* keep "both" and add an amendment line with the reason (and correct the response), or change PREREG to "either" before any data.

**M2. Holm turns T4b's "≥ 80%" into roughly 100%.** One-sided binomial p: 5/6 = 0.109, 6/7 = 0.0625 and 7/8 = 0.035. Only 6/6, 7/7 or 8/8 survive at Holm rank 1, and 7/8 survives only at rank 3. That rank needs both other discovery p-values below 0.0167 and 0.025. The decision is still mechanical, but PREREG and the film text should state the effective bar.

**M3. REVIEW_RESPONSE_v2 misdescribes the registered package.** The governing files are mutually consistent, but the response says:
- K = 9 scored tests with p-values for T2-A, T5-A and T5c. PREREG §3.2 has K_disc = 3 (T1-L1, T4b, T6).
- T6 is a 48-pixel N_side = 2 map with dof = 47. PREREG §5.7, EQ, A20 and PART2 (g4) all say N_side = 1, 12 pixels.
- The optimizer is a "50×50 grid + L-BFGS-B tol 1e-10". PREREG §4 says Nelder–Mead from the 5 best MCMC samples, then L-BFGS-B with ftol 1e-12.
- w_a^fit = (1+w0)(3/2)Ωm/[1 − ½Ωm(1+w0)]. That has the wrong sign and value: +0.078 vs the governing −(3/2)γ[Ωm + γ(1−Ωm)] = −0.102.
- Decision rules live in "EQ §8.1–8.8". EQ §8 has no decision rules.
- The group-term peak is at σ ≈ 80 kpc. It is at ≈ 57 kpc.

The "31 FIXED" count therefore can't be taken at face value. *Fix:* an unhashed errata note saying PREREG governs on each item. No change to any decision.

---

## MINOR (8)

1. The T2-A Dovekie forecast with the stated inputs (Ω_m,tot = 0.313 ± 0.006) is z ≈ 3.35σ, not 3.9σ. Pantheon+ is 3.72σ. The film line should read "about 3.4–3.7σ". This is not a deciding number.
2. The T2-N2 sensitivity value "Cooke vs DESI+BBN 6.84σ" reproduces as 6.42σ from the listed inputs. The deciding T2-N2 value (−3.72σ) treats Planck ω_b and H0, which come from the same chain, as uncorrelated. State this.
3. "Cooke sits 3.6σ below Planck" uses Cooke's σ only. With both errors combined it is 2.9σ.
4. The Lyα BAO+AP source is cited as "Cuceu et al. (2025)". arXiv:2607.27410 is DESI Collaboration, *DR2 Results IV* (July 2026). The values 8.600 ± 0.066 and 39.32 ± 0.33 match. I could not verify r = −0.43. Fix the citation and confirm r.
5. "One-sided 95% lower confidence bound" (235 Myr) is a Gaussian approximation to a Bayesian credible bound built from intervals quoted to 0.1 Gyr. The construction is reasonable: Dawson's 68% and 95% intervals are symmetric about 0.40, consistent with σ = 0.10, and the 5th percentile is ≈ 0.2355. Reword it. The number itself stands.
6. Pin the scipy version. G9-d relies on `ncx2.cdf(..., nc=0)`. It works in 1.18.1 (max |Δ| = 1.4×10⁻¹¹ on the registered 5×7 grid), but older versions may differ.
7. Define two edge cases: T4b with n_train = 0 (Acc_train is 0/0), and the Holm p of a test that didn't converge (set p = 1).
8. A20 calls the bare Pantheon+ covariance "C_H0". PREREG and EQ use C_HF for the SN-level matrix and C_H0 for the pixel-level one.

---

## Verified correct (no action)

- **Precedence.** The clause is present in PREREG §1.1, EQ, ASSUMPTIONS and all three PART files. The stale PART1 rules 9, 16, 18 and 22 are gone. No "defaults to INCONCLUSIVE" text survives. G8 lists only mechanical triggers (B3 concerns their scope).
- **One version per test.** This holds for T1-L1 (data, priors, optimizer, thresholds), T2-A (DESI DR2 BBN prior, uncorrelated σ_comb, either-run FAIL, f_leak from T2-A-Pantheon+), T2-N1, T2-N2 (Planck ω_b vs Planck H0), T4b (age 0.40, floor 235 Myr, hard-step metric, subcluster level, FAIL (c) on the test half), T5-B (1.5 / 70%), T5c and T6 (Galactic RING, z_HD, C_HF). The exceptions are B1, B2 and B4. Every alternate is listed as non-deciding in §3.1 item 3.
- **Decision logic.** The T1-L1 per-run partition is exhaustive and exclusive (0 mismatches on a 0.25-step grid of A and B). The T2-A, T4b, T5-A/B, T5c and T6 partitions are exhaustive. The model-level map covers "no FAIL, some INCONCLUSIVE".
- **Numbers.**
  - Supernova labels are correct: Pantheon+ −0.838 / −0.62; Dovekie −0.803 ± 0.054 / −0.72 ± 0.21 (z = 3.65).
  - T1-L1's w0 is now −1 + γ̂_u, and −0.84 appears only as an illustration (Law 1 w_a = −0.1019).
  - T2-N2 = −3.72σ. T2-N1 = +3.87σ.
  - T5c: PASS needs σ_ref > 2.24 kpc (3.1 kpc limit) and > 1.89 kpc (2.7 kpc limit). FAIL below 1.41 kpc. Group term peaks at 4.9×10⁶ M☉.
  - The r′ → 0 kernel branch equals the χ²₃ CDF exactly.
  - The "old value" column reproduces (−0.212653, −0.071614, −0.051392, +0.083317).
  - R_Planck = 5.3643 ± 0.0646. σ_comb algebra is correct.
  - The BBN prior 100ω_b = 2.218 ± 0.055 is DESI DR2 Eq. 14.
- **T4a** is unscored regardless of N, cut or catalog (§1.2.3, §3.1, §5.4, EQ, PART3), outside the Holm family, with no route back.
- **N10/M6** is disclosed in PREREG §5.5.
