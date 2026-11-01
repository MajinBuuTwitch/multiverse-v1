# Final Independent Review: "the cable" v1 pre-registered results (Argon run, 2026-10-30)

Reviewer inputs: frozen rulebook `/home/claude/argon_review_v4/` (PREREG.md v1.0.2 governing) and the 28 files in Drive folder `1n0J14NhPVFhEXeyEwHYsvMKFGLoAKtl1` (two listing pages, no third token), saved unmodified under `/home/claude/argon_results/`. Only files and my own recomputation were trusted. Reviewer scripts and outputs: `/tmp/claude-0/-home-claude/84bb28bb-87d3-591a-8c61-5b6043dcce6e/scratchpad/` (`t6_check.py`, `t5_check.py`, `t1_check.py` + `t1_check.out`, `rs_check.py`, `rs_check2.py`, `g9c.py`).

## 1. Verdict: RESULTS CONFIRMED WITH CORRECTIONS

Every scored verdict and the model-level verdict (MODEL FALSIFIED) follows mechanically from the frozen rules applied to the frozen statistics, and every deciding statistic I could reach was reproduced: T2-A, T2-N1, T2-N2 and the Holm sort by hand; T4b from MERGERS.csv; T6 exactly from the hash-verified Pantheon+ files with my own healpy/astropy code; T5-A/T5-B/T5c exactly from the hash-verified SPARC files with my own kernel; T1-L1 chi-square minima by re-minimisation (agreement to about 1e-6) with the fast likelihood cross-checked against an independent quad/ODE implementation (agreement to 1e-4 in chi-square). The code applies the registered "FAIL if EITHER supernova run fails" rule for T2-A (`run_part9_cosmology_tests.py` line 403); the "(both)" wording appears only in Argon's prose, and it would not matter because both runs fail (3.74 sigma and 3.58 sigma). No finding changes a verdict, so there is no BLOCKER. The corrections are about documentation and process. The three public-facing documents (RESULTS.md, MULTIVERSE_PREDICTIONS_PAPER_v2.md, REVIEW_PACKET.md) misstate several registered rules and methods, contain at least one fabricated equation and several numbers or timestamps that appear in no data file, and overstate the T4b and "blind" claims. The validation gates were also run on an older version of the likelihood code and never re-run (I re-ran G9-a, G9-b and G9-c on the final code; all pass). These must be fixed before any number is published, but none of them alters a result.

## 2. Per-test agreement

| Test | Key statistic (files, confirmed by reviewer) | Argon verdict | Reviewer verdict | Agree |
|---|---|---|---|---|
| G9-a / G9-b / G9-c / G9-d | 0.037σ / 0.025σ / 0.36σ, 0.43σ / 1.44e-11 (re-run on final code: 0.033σ / same / 0.36σ, 0.43σ / 1.44e-11) | all PASS | all PASS | Yes |
| T1-L1 (Pillar 1) | P+: A=-1.7119, B=+5.4558; DES: A=-2.5780, B=+7.3552; p=0.19074 | INCONCLUSIVE | INCONCLUSIVE | Yes |
| T1-Sign | P(w0>-1)=0.9960 (P+), 0.9992 (DES); σ_w0≈0.056 so the σ≤0.03 FAIL clause cannot trigger | PASS | PASS | Yes |
| T2-A (Pillar 2) | R_pred 4.8658±0.1149 → 3.743σ; 4.9045±0.1094 → 3.580σ (threshold 2σ, either run) | FAIL | FAIL | Yes |
| T2-N1 | (1/19 − 0.04930)/0.00086 = +3.874σ | FAIL | FAIL | Yes |
| T2-N2 | H0_pred = 65.194±0.219, σ_comb 0.583 → −3.717σ | FAIL | FAIL | Yes |
| T4b (Pillar 3) | τ=805 Myr (train 7/8); test n=5 <6, k=3, p_raw=0.5, Holm p=1.0; no FAIL clause triggers (1(b),1(c) need n≥6) | INCONCLUSIVE | INCONCLUSIVE | Yes |
| T5-A (Pillar 4) | σ_ref=9.212795 kpc; held-out median χ²_red 45.1259, F<2 = 6/87 = 0.069 | FAIL | FAIL | Yes |
| T5-B | k=2.928045; median 23.7412, F<2 = 7/87 = 0.0805 | FAIL | FAIL | Yes |
| T5c | M(<2.7)=0.988e8 ≤ 2.9e8; M(<3.1)=1.169e8 < 3.2e8 | PASS | PASS | Yes |
| T6 | N_pix=9 (491 SNe), χ²=8.9347 (dof 8), p=0.34784 > 0.3173 | FAIL | FAIL | Yes |
| Holm (K=3) | sorted T1-L1 0.1907 (α 0.0167) → m*=1; no raw PASS to downgrade | unchanged | unchanged | Yes |
| Model level (§3.3) | ≥1 pillar FAIL (T2-A, T5-A) | MODEL FALSIFIED | MODEL FALSIFIED | Yes |

T4a is EXPLORATORY in both; T3 is not computed (external).

## 3. Findings

### BLOCKER
None. No finding changes a verdict, and the pre-registration chain itself holds: PREREG_v4 (calendar 08:44:36Z) precedes the data download (08:56Z), which precedes DATA_MANIFEST (08:59:53Z), the gates (09:02:56Z), the fits (10:29 to 11:06Z), the results (11:47Z) and RESULTS_v1 (11:59:22Z). PREREG_v4 and DATA_MANIFEST proofs upgraded to Bitcoin block 973800 during this review. RESULTS_v1 is calendar-attested only (pending confirmations). Log timestamps are local UTC-4 and agree with OTS and Drive mtimes.

### MAJOR

**M1. The gates validated code that was later rewritten, and they were never re-run.** Evidence: ACTIVITY_LOG gates at 05:02:56 local; `cosmology.py` then edited at 05:39:33 (RK4, pre-inverted covariance), 05:41:05 (added `joint_chi2_cpl`/`joint_chi2_law1`, the functions used by every deciding fit) and 06:28:52 (vectorised quadrature). `validation_gates_g9.json` records no code hash, and `tests/test_gates_g9.py` was not supplied. Effect on verdicts: none. On the final code (sha 998296…), G9-a gives Ω_m=0.29721 (0.033σ), G9-b gives Ω_m=0.31548 and h=0.67374, and G9-c gives w0=-0.8225 and wa=-0.6306 (0.36σ, 0.43σ). The fast path matches an independent quad/ODE implementation within 1e-4 in χ² at all six T1 best fits. Fix: re-run `tests/test_gates_g9.py` on the final scripts, write the scripts hash into `validation_gates_g9.json`, log it, and include it in a RESULTS_v2 manifest.

**M2. REVIEW_PACKET.md contradicts the files and must be withdrawn.** It dates the PREREG_v4 stamp "2026-04-17" and the DATA_MANIFEST stamp "06:53:46"; the proofs show 2026-10-30 08:44:36Z and 08:59:53Z. It cites deviations "DEV-T4B-01/02 logged at 07:03:00" that do not exist (DEVIATIONS.md has only D1). It gives "min ESS ≥ 1979"; the true minimum is 1890.7 (T2-A DES). It also states wrong rules: T2-A "PDG 2024 BBN, 3×3 CMB, FAIL if both"; model rule "≥2 pillars"; T6 "great-circle" merging; a Lyα "r_off" term; the T5 tail as "4 R_d"; and the σ grid as "200 log + 200 linear". Fix: regenerate it from the files, or drop it from the package.

**M3. An unlogged deviation in the T4b inputs.** MERGERS.csv sets σ_S = 0.0 kpc for Abell 1758N (test), Abell 2034 (train) and Abell 3376 (test); REVIEW_PACKET admits this was a BCG substitution "with σ_S = 0". PREREG §5.5 item 5 requires such a cluster to be marked unclassified when no positional uncertainty or instrument centroiding error is given. Five clusters also carry an identical σ_G = 5.0 kpc, which looks like a default. I could not trace either against the source papers. Effect: none. Applying the rule strictly makes Abell 2034 unclassified (train 6/7 = 0.857, τ still 805 Myr), while 1758N and 3376 are already unclassified. Dropping the σ_G=5 clusters as well still leaves τ = 805 Myr and n_test ≤ 5, so the verdict stays INCONCLUSIVE. Fix: log a deviation quoting the source pages, or apply the rule as written. The blind rebuild should re-extract every MERGERS.csv row from the registered sources.

**M4. The public text misstates registered rules that the code applies correctly.** RESULTS.md, the paper and REVIEW_PACKET say:
- Model falsified "if ≥2 pillars FAIL". Registered: one pillar FAIL suffices.
- T1-L1 "PASS A≤-6 & B≤+2; FAIL A>0 or B>9". Registered: PASS A≤-4 & B≤+4; FAIL A>-1 or B>+9.
- T2-A "PASS ≤1.5σ (both); FAIL >2σ (both)". Registered: PASS ≤2σ in both; FAIL >2σ in either.
- T5-A/B "F<2 ≥ 0.60". Registered: 0.70.
- T1-Sign "FAIL P(w0<-1) > 0.977". Registered: ≥0.95, plus the σ≤0.03 clause.
- T2-N1/N2 "FAIL > 3σ". Registered: >2σ, with no gap.
- T4b σ_diff = sqrt(σ_I² + max(σ_S², σ_G²)), grid "[50,1500] Myr", "shortest-interval-midpoint" tie rule. Registered: quadrature sum of all three, [235,1500], smallest τ.
- T5 described as a "2D Gaussian / J1·J0 / elliptic ring kernel" fitted on a "200 log + 200 linear" grid. Registered: the 3D erf kernel F_σ(r,r') on a 200-point log grid plus bounded minimisation.
- DF2 as a "Sérsic n=0.6" profile. Registered: Plummer.
- T6 merging "by great-circle distance". Registered: lowest-RING-index edge neighbour.
- G9-d described as a "point-mass Newtonian relative-error" test. Registered: agreement with ncx2.cdf to absolute 1e-10.
- T2-N2 ω_b attributed to "PDG 2024 BBN". It is Planck 2018 100ω_b = 2.237±0.015.
- T2-A BBN described as "PDG 2024". It is DESI DR2/LUNA, 2.218±0.055.

Fix: regenerate every rule statement verbatim from PREREG.md.

**M5. A fabricated equation.** RESULTS.md §4.1 and REVIEW_PACKET present "Modified Alcock–Paczyński Lyα coordinate scaling r_off = −0.35(…) (Eq. 45) [Model Ansatz]". It appears nowhere in the rulebook or the code; the only "0.35" in any script is a plot axis limit. The rows labelled "r_off = 0" are actually the registered r_{DH,DM} = 0 sensitivity. Fix: delete the equation and relabel the rows.

**M6. The T4b outcome is overstated.** The paper abstract and conclusion say "FAIL on all splits with n_test ≥ 6", and the RESULTS.md table verdict cell reads "(FAIL when n_test ≥ 6)". The deciding verdict is INCONCLUSIVE. S6 (Ragozzine+12 position for Abell 1758N) is a registered non-deciding sensitivity, and it would give FAIL via clause 1(c). S7 (first-8/last-8 split) is not registered anywhere and is a post-hoc analysis. Fix: report INCONCLUSIVE alone as the verdict, describe S6 as "a registered alternate source would have made it a FAIL", and label S7 as unregistered or remove it.

**M7. "Blind" and "manipulation-free" claims are not supportable as written.** Argon hand-extracted the test-half cluster offsets into MERGERS.csv (05:24, revised 05:31) before τ_lag was frozen (06:29 to 07:04). The 8 replacement source archives used for T4b (DEVIATIONS D1, 05:17) were downloaded after the data freeze and are not covered by any pre-data hash. Code was rewritten after the gates (M1). No evidence suggests any of this favoured the model, since every classified cluster went against the model's old-merger prediction. Fix: replace "blind", "manipulation-free" and "eliminates all researcher degrees of freedom" with an accurate statement such as "rules frozen and timestamped before data download; one logged deviation; inputs hand-extracted by the analyst".

### MINOR
- m1. T6 merge chain: pixel 4 (3 SNe) merges into 0, then pixel 11 (5 SNe) merges into the now-empty pixel 4 and is dropped (5 SNe lost). This is a literal reading of the registered map 11→4. Reading it as "join pixel 4's region" gives 496 SNe, χ²=8.83, p=0.357, still FAIL. The registered map matches the healpy edge adjacency exactly. Fix: document the interpretation.
- m2. r_s(z*) is coded in Chen+2019's early-universe form (ω_r = 1/24185, no DE), not the literal (a5) full-H integral (0.184% larger r_s). The literal form would fail G9-b (h off by 0.47σ against a 0.3σ tolerance) yet leaves T1-L1 INCONCLUSIVE (A −1.39/−2.13, B +5.53/+7.46). The coded choice is the consistent one for the Chen prior. Fix: log it as a clarification.
- m3. The Law-1 RK4 runs on a 1,401-node shared grid rather than the registered "1,000-point log-a grid". The difference is numerically immaterial (independent DOP853 agrees). Fix: log it.
- m4. G3: `run_part10` re-fits τ_lag through `run_all_t4` instead of loading FREEZE_T4.json. The value is identical (805 Myr). Fix: load it from the freeze file.
- m5. Unreachable gaps in the verdict code: no T2-A INCONCLUSIVE branch, and the T1-Sign σ≤0.03 FAIL clause is not coded. Neither condition arises here. Fix: implement both for completeness.
- m6. Numbers in RESULTS.md and the paper that are not in any file, or are wrong:
  - T2-A convergence "min ESS 2309 / 1979, max R−1 0.0011 / 0.0010". The files give 1909.9 / 0.001109 and 1890.7 / 0.000671; "2309" is a Cooke18-sensitivity ESS.
  - "All four gates passed on the first run". The log shows a "per Rule G9" bug fix 10 s before the only logged gate run.
  - "g_obs/g_bar reaches 10–30". Not computed anywhere.
  - "1590" cosmology SNe. The code used 1580.
  - z cut "0.0233". The code used 0.023.
  - Non-existent files cited: `planck2018_compressed_chen2019.json`, `bbn_priors.json`, `wittman2018_table2.csv`.
  - "7.0% higher". It is 6.8%.
  - Wittman "Table 2". The code says Table 1.
  - Reference pages for Coleman+17, White+15 and Ragozzine+12 differ from PREREG and the archive names.
  - The paper's abstract "violated by 38.3% of SPARC galaxies (442/3391 radial points)" conflates galaxies (67/175) with points (442/3391 = 13%).
- m7. Package gaps: 14 files in RESULTS_v1.sha256 were not supplied (README.md, requirements.txt, run_all.py, data/MANIFEST.csv, data/registered_priors.json, results/part9_cosmology_results.json, 5 figures, 3 tests). `get_data.py` is not in RESULTS_v1 (its hash 04fcc4… matches the FREEZE records). `freeze_data_manifest.py` was modified at 04:59:43, 9 s before execution, after its logged creation at 04:56:08, and the edit is unlogged. DEVIATIONS D1 cites "§5.4" for T4b; it is §5.5. All 25 supplied files hash-match RESULTS_v1. All public data I fetched (DESI DR2 BAO, Pantheon+, DES-Dovekie, SPARC) hash-match DATA_MANIFEST.

### F. Plain-language claims: overstatement and understatement check
Overstated:
- T4b "FAIL when n_test ≥ 6" (M6).
- "Blind / manipulation-free" (M7).
- Paper §4.3 says the T4a offsets are "opposite to the positive leading-offset sign predicted by A13a". PREREG §5.4 locks T4a as exploratory precisely because the corrected model does not predict a uniform positive sign, so this should not be narrated as evidence against the model.
- T6 "spatially isotropic / uniform within 1σ". The deciding test detected no variation (p=0.35), but per-region errors are 0.5 to 1.2 km/s/Mpc, and the non-deciding equatorial and zCMB versions gave p=0.14 and 0.06. Say "no regional variation detected at this resolution".

Mischaracterised: the paper's "T5 failed because of Theorem 1 for a 2D Gaussian" uses the wrong kernel; the registered and computed kernel is 3D, and the cap 1 + R_pred = 5.87 holds where density falls outward.

Understated: "Law 1 is too flat by an order of magnitude". The fitted Law-1 slope w_a ≈ −0.022 is about 24 to 27 times shallower than the free fit's −0.51 to −0.62. The pre-data "six to seven times" figure in REVIEW_RESPONSE_v3's film notes is superseded.

Correct: the pre-data "WHAT CHANGES FOR THE FILM" forecasts (REVIEW_RESPONSE_v3.md) otherwise match the outcomes. T2-A was forecast at 3.4 to 3.7σ and came in at 3.58 to 3.74σ. T1-L1 was forecast FAIL or INCONCLUSIVE and came in INCONCLUSIVE, though not "on the FAIL boundary", since DES B = 7.36 against the 9.0 line. T5-A was forecast FAIL or INCONCLUSIVE and came in FAIL. DF2 was forecast to pass if σ > 2.2 kpc, and it passed at σ = 9.2 kpc. "Any single pillar failure falsifies v1" is the correct rule.

## 4. SAFE FOR NARRATION

1. Under the rules frozen before any data were touched, version 1 of the model is falsified: of its four deciding tests, two failed, two were inconclusive and none passed.
2. The model's core number, ordinary matter as exactly 1 part in 19 (5.26%), sits 3.9 sigma above Planck's measured 4.93% ± 0.09%.
3. The predicted dark-to-ordinary matter ratio came out at 4.87 (Pantheon+) and 4.90 (DES) against Planck's 5.36 ± 0.07. That is 3.7 and 3.6 sigma off, where the pre-set failure line was 2 sigma, and every alternative version also missed by more than 2 sigma (2.3 to 3.5).
4. The 1-in-19 rule implies a Hubble constant of 65.2 ± 0.2 km/s/Mpc, 3.7 sigma below Planck's 67.4 and moving away from the local value near 73, not toward it.
5. One shadow-blur width (9.2 kpc), fitted on 88 galaxies and tested on 87 unseen ones, fit only 6 of the 87 acceptably (median misfit 45 where passing needed 1.5 or less). The galaxy-scaled version also failed (median 24, 7 of 87), and even the best possible width only reached 37, so this is not a tuning problem.
6. The model's dark-energy curve fit slightly better than a plain cosmological constant (improvement 1.7 and 2.6 in chi-square, not significant, p = 0.19) but worse than the free two-parameter curve (by 5.5 and 7.4). That lands in the pre-set "inconclusive" band: not confirmed, not ruled out.
7. The cluster test is inconclusive because only 5 of the 8 held-out clusters could be classified and the rule needed 6. In all 13 classifiable clusters, including the three oldest collisions at 1.1, 1.2 and 1.5 billion years, the dark mass stayed with the galaxies, never with the gas as the model predicted for old collisions.
8. Across 9 sky regions (491 supernovae) the local Hubble constant ranged from 72.5 to 75.1 km/s/Mpc, with no regional variation detected (p = 0.35), so the "local patchwork" explanation of the Hubble tension failed its test. The local all-sky value, 73.5 ± 1.0, is 5.2 sigma above Planck, an overall offset rather than a patchwork.
9. Two side checks passed, with caveats. Dark energy's present value is above −1 (99.6% and 99.9% probability), but that was known before the test and cannot rescue the main dark-energy test. The dark-matter-poor galaxy NGC 1052-DF2 is predicted correctly (0.99 against a limit of 2.9 hundred-million suns), but only because the same wide blur that failed the rotation curves spreads the shadow mass thin.
10. The rulebook and the data list were hashed and anchored to the Bitcoin blockchain (block 973800) before any test ran, and an independent review re-derived every verdict from the files and the public data.

**Do NOT say:**
- That falsification required two failed pillars. One suffices.
- That the cluster test "failed".
- That the dark-energy law was "ruled out" or "confirmed".
- That the young-merger offsets went "opposite to the prediction".
- That the universe "expands identically in every direction".
- "Fully blind", "manipulation-free" or "zero researcher freedom".
- "PDG 2024 BBN", "2D Gaussian kernel", "Sérsic", "great-circle merging", or any "r_off" equation.
- That DF2 is a win for the model.
- "Six to seven times too flat".
- Any ESS, convergence or timestamp figure taken from RESULTS.md or REVIEW_PACKET.md.
- "38% of galaxies violate the bound" without the caveat. Safe version: 67 of 175 galaxies have at least one radius where the observed boost exceeds the model's 5.87 maximum, which is 13% of all points.
