# Cold Review: Mandarano Model Stage 1 Pre-Registration Package (v1.0.1)

Reviewer scope: MULTIVERSE_STAGE1_EQUATIONS.md ("MAIN"), EQUATIONS.md ("EQ", added to scope mid-review), ASSUMPTIONS.md, PREREG.md, ACTIVITY_LOG.md, PREREG.sha256. Algebra and numerics were redone in python/sympy/scipy. Published numbers were checked against the primary papers where reachable. Anything taken from reviewer recollection rather than a fetched source is marked [recollection].

## Verdict: PROCEED AFTER FIXES (no data may be opened until the four BLOCKERs are fixed, the package is re-hashed, and the hash is timestamped externally)

The package is unusually explicit, and most of the standard algebra is correct. It still cannot be frozen in its current state. The registered rotation-curve kernel F_σ is wrong by a factor of 2 in one term and returns negative enclosed masses, and T5 registers that formula as "exact". The T4a test statistic has opposite signs in PREREG and in both equation files. The model allows either sign of the T4a offset depending on a kinematic assumption (A13a vs A13b) that is never chosen. T1 tests only w0 > −1, a result already known from published DESI DR2 posteriors (P ≈ 0.998 or higher), and it leaves out the model's own derived w(a), which the same data disfavour. On published numbers the package's main quantitative claims are already in trouble. Ω_b = 1/19 sits 3.9σ above Planck. It implies H0 = 65.2 ± 0.2 km/s/Mpc (3.7σ below Planck ΛCDM, 7.4σ below SH0ES). T2 is forecast to FAIL in both supernova runs (about 3.5σ and 3.6σ). The saturation cap makes a T5 PASS essentially impossible for low-acceleration SPARC galaxies. Pre-registering tests that are likely to fail is legitimate and worth doing, but the tests must be specified correctly before anything is frozen.

Counts: **4 BLOCKER, 15 MAJOR, 14 MINOR.**

---

## BLOCKER

### B1. The registered 3D Gaussian enclosed-mass kernel F_σ is wrong (factor 2), and T5 registers it as "exact"
- **Where:** MAIN §7 (f3); EQ §7 (f1–f4); used by PREREG T5 ("exact 3D Gaussian error-function kernel F_σ(r, r′) of Section (f3)") and T5c (group term).
- **What's wrong:** The exact fraction of a Gaussian-smoothed shell of radius r′ that lies inside radius r is the non-central χ²₃ CDF:
  F(r, r′) = ½[erf((r+r′)/√2σ) + erf((r−r′)/√2σ)] − **(1/√(2π))**·(σ/r′)·[e^{−(r−r′)²/2σ²} − e^{−(r+r′)²/2σ²}].
  Both files print the second coefficient as **√(2/π)**, which is twice the correct value.
- **Evidence:** Against `scipy.stats.ncx2.cdf((r/σ)², 3, (r′/σ)²)` and a 2×10⁶-point Monte Carlo: at r = r′ = σ = 1 the correct value is 0.1323 (MC 0.1324) and the registered formula gives **−0.2127**. On a grid of 0.05 ≤ r, r′ ≤ 10 and σ ∈ {0.5, 1, 3}, the registered F is negative at 36% of points. The corrected formula matches the exact CDF to 1×10⁻¹⁴. The registered F also approaches 0 from below as σ → ∞, so the shadow mass at fixed r is negative for large σ. That breaks the cap theorem and every T5-A, T5-B and T5c number.
- **Fix:** Change the coefficient to 1/√(2π) in both MAIN and EQ. Register a unit test that compares F against `ncx2.cdf` (tolerance 1e-10) and require it to pass as part of G9. Re-hash.

### B2. The T4a statistic has opposite signs in PREREG and in the equation files
- **Where:** PREREG T4a "Statistic": Δ_SI^∥ = **−δ_SG β**. MAIN §6 (e6–e7) and EQ §6: Δ_SI^∥ = **|δ_SG|(−β)**.
- **What's wrong:** With δ_SG < 0 (stated in both files), |δ_SG|(−β) = δ_SG β = δ_SI, which is the intended "positive = ahead of stars". The PREREG expression −δ_SG β = |δ_SG|β = **−δ_SI**. The sign of the primary statistic is reversed relative to the words next to it ("positive = away from the gas"). Under G8 the ambiguity defaults to INCONCLUSIVE, so the test cannot produce a PASS or a FAIL as written.
- **Fix:** Define the statistic once, as Δ_SI^∥ ≡ (x_I − x_S)·ŝ with ŝ the unit vector from gas to stars, and copy that exact expression into all three files.

### B3. T4a is not a determinate test: the predicted sign, the primary sample, and the statistic are all left open
- **Where:** MAIN §6 (A13a vs A13b branches); ASSUMPTIONS [A13]; PREREG T4a.
- **What's wrong:**
  1. *Sign not fixed by the model.* I reproduced both kinematic branches with sympy: A13a gives Δx̃_S = +½a_dec T² > 0 (offset ahead), and A13b gives Δx̃_S = (1/6)ω₀²v_pτ²(3T − 2τ), which is **negative for T < 2τ/3**. τ_lag is only bounded below (≥ 150 Myr) and the primary sample has t_p ≤ 150 Myr, so any τ_lag > 225 Myr makes A13b predict a *negative* offset for a T = 150 Myr system. PREREG never says which branch is the registered prediction. The model therefore accommodates PASS and FAIL alike, so the test can't falsify it.
  2. *Primary sample.* "1E 0657-558 and Abell 2744, excluding the Bullet Cluster itself **if required**, with both … reported." G2 requires the exclusion, because the Bullet is the T4a FIX dataset. That leaves one system, Abell 2744, whose tabulated t_p = 0.15 ± 0.05 Gyr sits exactly on the ≤ 150 Myr cut. PREREG doesn't say which version (Bullet-in or Bullet-out) decides the outcome.
  3. *Statistic.* "Inverse-variance-weighted mean (and unweighted sample mean with bootstrap/SEM error)" names two statistics without saying which one decides.
  4. No predicted amplitude is registered (A13a gives roughly R/(f_S+R)·½a_dec T² ≈ 20 kpc for a_dec ≈ 2000 km/s/Gyr, T = 0.15 Gyr [reviewer estimate]), so the power of the test is unknown.
- **Fix:** Register A13a or A13b as the v1 kinematic law. If neither can be justified, register the sign prediction as conditional on independently published infall kinematics for each system and state the predicted sign per system. Exclude the Bullet unconditionally. Register a minimum sample size (e.g. ≥ 3 independent systems), below which the result is INCONCLUSIVE by design, and state that this is expected. Pick one statistic. Register a predicted offset magnitude with its uncertainty.

### B4. T1 tests only the sign of w0, whose PASS is already known, and leaves out the model's actual dark-energy prediction, which the same data disfavour
- **Where:** PREREG T1; MAIN §5 (d3, d4, Law 1); ASSUMPTIONS [A8], [A9].
- **What's wrong:** The locked v1 model is the Static Form (Q = 0) with uncoupled unwinding. MAIN (d3) derives **w(a) > −1 at all epochs**, and Law 1 (the baseline) predicts a one-parameter curve, w(a) = −1 + γ_u/E(a). PREREG claims v1 "does not specify whether w(a) < −1 was allowed in the past". The package's own derivation does specify it, and T1 tests only w0 > −1.
- **Evidence (forecast from published results):** DESI DR2 + CMB + Pantheon+: w0 = −0.838 ± 0.055 [recollection], giving P(w0 > −1) ≈ 0.998. DESI + CMB + DES-Dovekie: w0 = −0.803 ± 0.054, wa = −0.72 ± 0.21 (Popovic et al. 2025, arXiv:2511.07517, Table 10), giving P ≈ 0.9999. **T1 PASS is therefore already known.** Meanwhile the Law 1 tangent at w0 = −0.84 gives wa = −0.10, against DESI's −0.62 ± 0.20 (about 2.6σ along wa). DESI's w0 + wa ≈ −1.46 to −1.61 points to a phantom past. A T1 PASS would be reported as support for a model whose concrete w(a) the same likelihood disfavours.
- **Fix:** Add a registered primary test T1-L1: fit Law 1 directly (one parameter γ_u ≥ 0, no CPL mapping) to the same DESI + CMB + SN likelihoods and register a Δχ² threshold against flat w0waCDM (e.g. FAIL if Δχ²(Law 1 − w0wa) > 9.0 for 1 fewer parameter in either run; values to be fixed now). Demote the w0 sign to a secondary, reported-only test. If Law 2 or Law 3 are kept as alternatives, register in advance which one counts and apply a trials penalty (see M10).

---

## MAJOR

### M1. T2 is an algebraic test of Ω_b = 1/19, not of f_leak; the fixing fit doesn't impose the model; σ_comb ignores shared Planck information
- **Where:** MAIN §4 (c3, c4); EQ §4; PREREG T2; ASSUMPTIONS [A3], [A18].
- **What's wrong:** Ω_m = Ω_b(1 + R) holds identically, so R_true = Ω_m/Ω_b − 1. The prediction R_pred = 19Ω_m − 1 equals R_true **if and only if Ω_b = 1/19**. f_leak is just a relabelling of Ω_m (any Ω_m gives some f_leak), so T2 carries no information about f_leak beyond Ω_b. The FIX fit is a generic w0waCDM fit in which Ω_b = ω_b(BBN)/h² floats freely (≈ 0.047). Inside the fit the model's own share relation (c3) is violated, so the "fixed" f_leak doesn't come from a fit of the model. Planck TT,TE,EE enter both the FIX (via R, ℓ_A, which depend on ω_m = ω_b + ω_c) and the TEST (ω_c/ω_b). σ_comb adds them in quadrature as if independent. G2 discloses the overlap but the statistics don't account for it.
- **Forecast (published full-CMB posteriors; compressed priors will differ somewhat):** Pantheon+: Ω_m = 0.3114 ± 0.0057 [recollection] gives R_pred = 4.917, σ_comb = 0.126, a deviation of **3.5σ, FAIL**. DES-Dovekie: Ω_m = 0.313 ± 0.005 (arXiv:2511.07517) gives R_pred = 4.947, σ_comb = 0.115, a deviation of **3.6σ, FAIL**. A PASS needs Ω_m ≳ 0.322 at σ_Ωm ≈ 0.006.
- **Fix:** Rename T2 as what it is, "Ω_b = 1/19 test". Either (a) fit the model as specified (impose ω_b = h²/19 and Ω_dm = 6(1 − f)/19, fit f, and register a goodness-of-fit threshold), or (b) keep the current form but estimate the FIX–TEST covariance from Planck chains or by bootstrap and use it in σ_comb. Resolve the neutrino convention (m7).

### M2. Already-tensioned parameter-free predictions are not registered as tests: Ω_b = 1/19 and the implied H0
- **Where:** MAIN §4 "Ratio Tension"; EQ §4; ASSUMPTIONS [A11].
- **Calculation:** Planck 2018 (TT,TE,EE+lowE+lensing): Ω_b = 0.02237/0.6736² = 0.04930 ± 0.00086 (uncorrelated propagation). 1/19 = 0.05263 is +6.75% higher, a **3.9σ** tension. Combining Ω_b = 1/19 with a measured ω_b gives a parameter-free H0 = 100√(19ω_b): **65.19 ± 0.22** (Planck ω_b), **64.15 ± 0.28** (Cooke+18 BBN, the prior PREREG registers), 65.14 ± 0.53 (post-LUNA BBN). That is 3.7σ below Planck ΛCDM's 67.36 ± 0.54 and about 7.4σ below SH0ES 73.04 ± 1.04. It also contradicts the premise of T6 that the global H0 is Planck-like and only the local reading is high. The package's own figure "R_pred = 5.00 is 5.5σ below 5.36" is 5.64σ by my arithmetic (σ = 0.0646).
- **Fix:** Register an explicit test "H0 = 100√(19 ω_b)" against DESI + CMB + BBN H0, with thresholds fixed now. At minimum, state in PREREG that the v1 numerology is already in 3.7–3.9σ tension before any v1 data are opened.

### M3. T5 is effectively pre-falsified by the model's own cap theorem
- **Where:** MAIN §7 (f3, cap theorem); PREREG T5.
- **Calculation:** The cap is g_obs/g_bar ≤ 1 + R ≈ 6.0 (5.92–6.06 for the forecast T2 values). The McGaugh+16 RAR reaches that ratio at **g_bar = 3.74×10⁻¹²** m/s² (the package says ≲ 3×10⁻¹²). At g_bar = 10⁻¹² the RAR ratio is 11.5, so the model's velocity is 28% low; at 5×10⁻¹³ it is 39% low. With typical SPARC σ_V ≈ 5%, each such point contributes χ² ≈ 30. Outside the baryonic edge, M_sh → R·M_b,tot, so the model predicts Keplerian decline where SPARC shows flat curves. A PASS (≥ 70% of held-out galaxies with χ²_red < 2) is not plausible for a sample in which a large fraction of dwarf and LSB galaxies reach g_bar < 4×10⁻¹².
- **Fix:** No change to the thresholds. State the forecast in PREREG, and register the fraction of held-out galaxies with any point at g_bar < 3.7×10⁻¹² as a reported diagnostic, so the reason for a FAIL can be attributed in advance rather than explained after the fact.

### M4. T5 methodology leaves open choices that change χ²
- **Where:** PREREG T5; MAIN (f1, f3), §9 item 4.
- **What's wrong:** (a) How dM_b(r′) is built from SPARC is not specified. SPARC gives thin-disk v_disk, v_bul and v_gas (with v_gas² < 0 at some radii) plus surface brightnesses. MAIN (f1) equates v_bar² with G·M_b(<r)/r, which is false for disks, so the σ → 0 limit "v_c² → (1+R)v_bar²" in §9 is consistent only if M_b(<r) is *defined* as r·v_bar²/G. That definition can give negative or non-monotonic dM_b, which breaks the cap theorem's premise ("outward-decreasing spherically averaged density"). (b) Baryon mass beyond the last measured radius (extrapolation or truncation) is unspecified, yet it feeds M_sh(<r). (c) The error model is unspecified: SPARC errV only, or with distance and inclination propagated. (d) The optimizer is unspecified: `minimize_scalar` on [0.1, 100] kpc with no method or tolerance, and χ²(σ) can be multimodal. (e) "Lexicographic by exact SPARC name" doesn't fix case or numeric handling.
- **Fix:** Register: M_b(r) from SPARC surface-density profiles (or r·v_bar²/G with an explicit monotonic-clipping rule), the extrapolation rule, the error model, `method='bounded'` preceded by a 200-point log grid, and Python `sorted()` on the raw byte names.

### M5. The velocity-extrapolation rule (e3) is applied to clusters and switched off by fiat for galaxies, with no quantitative criterion
- **Where:** MAIN (e3), (f4), ASSUMPTIONS [A12], [A16]; EQ (f1–f4) omits the switch-off entirely.
- **What's wrong:** Applied literally to a disk, (e3) moves every mass element from radius r to r_ext = √(r² + (v_cτ)²). With v_cτ = 30.68 kpc (verified), mass at 3 kpc would be sourced near 31 kpc. MAIN cancels this with "stationary coarse-grained density, ρ̃_b = ρ_b", but (e3) is defined per mass element, not on the coarse-grained density, so the cancellation contradicts the model's own definition. The cluster treatment keeps per-element extrapolation but uses only the subcluster centroid. That drops the dispersion term (e3) implies: σ_v·τ ≈ 1000 km/s × 150 Myr ≈ 150 kpc of smearing, comparable to δ_SG. The supporting numbers are inconsistent too. MAIN says r/v_c ~ 15 Myr ≪ τ (true only at about 3 kpc). ASSUMPTIONS [A16] says periods of 50–100 Myr ≲ τ. At r = 30 kpc and v = 150 km/s, r/v = 196 Myr > τ, so the stated condition fails exactly where rotation curves constrain the model. PREREG T5 doesn't register ρ̃_b = ρ_b, although MAIN says it is "as registered in Test T5".
- **Fix:** Write one rule that applies to both clusters and galaxies (e.g. extrapolate the coarse-grained bulk velocity field smoothed on scale σ_ref, so internal dispersion and rotation are excluded by construction), derive the cluster β with it, and put it in PREREG T5 and T4a/b explicitly.

### M6. The T4b sample, sort rule, ages and position data were all chosen by an author who knew the published outcomes
- **Where:** PREREG T4b table and classification rule.
- **What's wrong:** (a) The 16 systems were hand-selected from literature whose lensing/gas associations are well known (Abell 520's "dark core with gas" is the textbook case). (b) The "alphabetical" order is case-sensitive ASCII with natural numeric sort, and the rule isn't stated. A case-insensitive natural sort moves Abell 520 and Abell 2744 into the test half. The paragraph about "swapping position 1 and 2" is incoherent, because "1E" already sorts first. (c) There is no registered source for the I, G and S positions and σ_I, σ_G, σ_S used by the classification rule. (d) Point-estimate ages ignore σ_tp of up to 0.38 Gyr. (e) **The Bullet age contradicts its own cited source.** The table gives 0.15 ± 0.05 Gyr and cites Dawson 2013, but Dawson 2013 (ApJ 772, 131, Table 2) gives TSC₀ = 0.6 Gyr (68%: 0.3–1.1) with default priors, or 0.4 Gyr (0.3–0.5) with the temporal prior. The Musket Ball entry of 0.96 ± 0.28 is not Dawson 2013's 1.1 Gyr (0.7–2.4). Since the Bullet is the anchor for τ_lag > 150 Myr (T4a FIX), a 0.4–0.6 Gyr Bullet would move the lower bound to 400–600 Myr. (f) Abell 520 and CIZA J2242 share t_p = 0.80, and they are commonly reported with opposite dark-mass associations, so a single step at 0.80 Gyr cannot classify both correctly.
- **Fix:** Use a selection rule written as an algorithm (e.g. every system in Golovich+19b with a published TSC₀ posterior and a lensing peak catalogue), a byte-wise sort, one named catalogue per position type, and a classification that uses the age posterior (e.g. P(t_p < τ) > 0.5). Correct or re-source the Bullet and Musket Ball ages, and record the page or table for every t_p.

### M7. The Lyα AP constraint double-counts the Lyα BAO (violates G6)
- **Where:** PREREG T1 TEST datasets.
- **Evidence:** arXiv:2607.27410 (DESI DR2 Results IV, July 2026) gives D_H/r_d = 8.600 ± 0.066 and D_M/r_d = 39.32 ± 0.33 *from the joint Lyα AP + BAO fit*. `desi_bao_dr2` already contains the Lyα BAO point at z = 2.33 (D_H/r_d = 8.632 ± 0.101, D_M/r_d = 38.988 ± 0.531; arXiv:2503.14738 Table IV). Using both counts the Lyα BAO twice. The D_H–D_M correlation isn't registered, and the "T1 note" in MULTIVERSE_TESTS_v1.md that supposedly mandates this was not provided and is not hashed.
- **Fix:** Replace the Lyα row of the DESI DR2 vector with the joint AP + BAO values and their published 2×2 covariance. Register the correlation coefficient now.

### M8. The CMB-prior and r_d computations are unregistered, the priors are mislabeled, and the G9 validation can't catch errors in either
- **Where:** MAIN (a5); PREREG T1 (CMB prior), T2, G9.
- **What's wrong:** Chen, Huang & Wang (2019) compute R and ℓ_A with z* from the Hu–Sugiyama fit (their text and appendix code disagree on one coefficient, 0.0738 vs 0.0783). The package gives "z* = 1089" in places and registers no formula. ℓ_A has 0.03% precision, so the z* method matters. The r_d method (z_d fit vs Boltzmann code vs a fitting formula) is also unregistered. The vector (1.7502, 301.471, 2.236) with correlations (0.46, −0.66, −0.33) is Chen et al.'s **ΛCDM** set. PREREG labels it "in wCDM" (Chen's wCDM set is 1.7493, 301.462, 0.02239, with ρ = 0.47, −0.66, −0.34), and Chen gives no CPL set at all. The G9 benchmark (DESI DR2 BAO-only ΛCDM Ω_m = 0.2975 ± 0.0086) is independent of r_d, because BAO-only Ω_m marginalises r_d·h. It validates neither r_d nor the CMB priors nor either SN likelihood.
- **Fix:** Register z* (Hu–Sugiyama with the coefficient stated), z_d and the r_d integration (or a named fitting formula with its accuracy). Relabel the priors as ΛCDM and justify their use in w0wa. Add validation targets: reproduce a published DESI DR2 + CMB(compressed) + SN w0wa posterior, or Chen et al.'s own ΛCDM fit, to within 0.3σ before any test run.

### M9. The T2 BBN prior is outdated and conflicts with the CMB block it is paired with
- **Where:** MAIN (a5) note; PREREG T2 FIX item 3.
- **What's wrong:** 100ω_b = 2.166 ± 0.019 (Cooke, Pettini & Steidel 2018) used the pre-LUNA theoretical d(p,γ)³He rate [recollection]. It is 2.9σ below Planck's ω_b (2.237 ± 0.015). Post-LUNA analyses give about 2.23–2.24 (Pitrou+21, Pisanti+21), and DESI DR2 itself uses 0.02218 ± 0.00055. The (R, ℓ_A) block was derived jointly with ω_b = 0.02236. Pairing it with a ω_b about 3σ lower forces r_s(z*), h and Ω_m to absorb the conflict, which biases the very Ω_m that T2 freezes.
- **Fix:** Register DESI's BBN prior (ω_b = 0.02218 ± 0.00055) or a post-LUNA value, and report the sensitivity to Cooke+18 as a secondary run.

### M10. No multiple-testing control, no overall decision rule, and several escape hatches
- **Where:** PREREG §1–4, G4, G8.
- **What's wrong:** There are eight scored tests (T1, T2, T4a, T4b, T5-A, T5-B, T5c, T6) and no rule for combining them into a verdict on the model. With eight independent one-sided 2σ PASS criteria, P(≥ 1 spurious PASS) ≈ 17%. T5-A and T5-B are alternative kernels with no rule saying whether "either passes" counts as a PASS. The AND/OR conventions are inconsistent: T2 FAILs if *either* run fails, but T4a FAILs only if *both* catalogues are ≥ 2σ negative, which makes a T4a FAIL much harder to reach than a T2 FAIL. The T1 PASS wording mixes one-sided 95% (z = 1.645) with "two-sided … 2.5th percentile" (z = 1.96). G8 ("anything left unresolved defaults to INCONCLUSIVE") lets any ambiguity found after unblinding turn a FAIL into INCONCLUSIVE.
- **Fix:** Register a model-level rule (e.g. "v1 is falsified if any of T1-L1, T2, T5 primary FAILs"). Apply Holm or Bonferroni to PASS claims. Choose T5-A *or* T5-B as primary now. Use symmetric AND/OR logic for PASS and FAIL. Pick one T1 threshold. Narrow G8 so that an ambiguity can be declared only before the freeze, and anything found later is resolved by the most literal reading.

### M11. EQUATIONS.md is a second, different frozen equation document that falsely claims to be identical
- **Where:** EQ header note; PREREG.sha256; ACTIVITY_LOG lines 27–28.
- **What's wrong:** EQ (hash verified, 146 lines vs MAIN's 291) states it is "identical in mathematical content", including every recovery limit, the parameter table and A1–A20. It is not. It omits: the A13a/A13b Δx̃_S formulas (so β is undefined in EQ alone); the galaxy stationarity rule ρ̃_b = ρ_b (so EQ read alone implies (e3) applies to disks; see M5); the cap theorem's premise; the T2 2×2-block + BBN note; the Law 1 degeneracy and slope; the non-phantom statement in (d3); the wedge statement; all of §9 (recovery limits), §10 (A1–A20) and the parameter table; the T6 GLS detail; the H-Abs/H-Rel criteria; and the transfer-form derivations. It repeats MAIN's errors (B1 kernel, m1 wa_eff). Nothing says which file governs. The log shows the two files were written one second apart against two different handoff specs (B6/B7 vs SESSION_BOOTSTRAP), neither of which is hashed.
- **Fix:** Delete EQ, or make it a byte-identical copy of MAIN. Add a precedence clause to PREREG ("MAIN governs; EQ is informational"). Re-hash.

### M12. The freeze doesn't cover what it claims, and nothing anchors it in time
- **Where:** PREREG §1–2 ("thresholds … without alteration"); ASSUMPTIONS [A18], [A19]; PREREG.sha256; ACTIVITY_LOG.
- **Checked:** All four manifest hashes match the files exactly (LF line endings, no CR bytes). The log shows no writes after the hash at 02:27:00. Nothing suggests post-hash edits.
- **What's wrong:** The "unchanged" thresholds come from MULTIVERSE_TESTS_v1.md, which is neither provided nor in the manifest. The same goes for the two handoff files, GEMINI.md, the STAGE1_PART1-3 files, and ACTIVITY_LOG.md itself. The claim that no threshold was altered can't be verified. The hashes sit on the author's own disk, so they can be regenerated at any time. That establishes integrity, not when the files were written.
- **Fix:** Add MULTIVERSE_TESTS_v1.md, both handoffs, the PART files and the log to the manifest. Commit and push to a public or third-party-timestamped location (OSF, a GitHub tag, an email to the cold reviewer) *before* any download, and record that timestamp in PREREG.

### M13. The "Uncoupled Non-Phantom Wedge" theorem is false
- **Where:** MAIN (d5) Law 3 paragraph; ASSUMPTIONS [A9].
- **What's wrong:** It claims any uncoupled monotonic unwinding lies in w0 > −1, −(1+w0) ≤ wa ≤ 0. For non-CPL w(a), the tangent-defined wa ≡ −dw/da|₁ doesn't satisfy w0 + wa = w(a → 0). Counterexamples (checked analytically and by integrating the ODE; w(a) ≥ −1 on all of [10⁻³, 1] in each case): Law 2 with 1+w0 = 0.2 and q = −1 gives w0 + wa = **−1.056** (below the wedge). Law 2 with 1+w0 = 0.16 and q = 2 gives wa = **+0.052** (above the wedge). Law 1 itself leaves the wedge for 1+w0 > 0.513. The wedge is therefore not the region the model predicts, and DESI's w0 + wa < −1 neither cleanly falsifies the model nor is it compatible with the wedge as stated.
- **Fix:** Drop the wedge claim. Compare each law's actual w(a) to the data directly (see B4).

### M14. T6 PASS is not specific to the model, and its FAIL is not operational
- **Where:** PREREG T6; MAIN (g1–g4).
- **What's wrong:** The model predicts no amplitude or pattern for regional H0 heterogeneity, so any ≥ 3σ heterogeneity counts as a PASS, whether it comes from unmodelled bulk flows, extinction near the Galactic plane, or survey footprint. The all-sky half (SH0ES-calibrated H0 > Planck at ≥ 3σ) is already known to be satisfied. FAIL branch (b), "a resolution accepted by the SH0ES team", can't be applied mechanically. H̄0 is undefined (GLS mean vs unweighted mean), and the stated dof = 11 holds only for the GLS mean. HEALPix N_side = 1 equatorial pixels straddle b = 0 and may hold very few or no SNe, and no minimum count is set. z_HD already includes peculiar-velocity corrections, which suppress the very signal being tested. The model's own global H0 is about 65 (M2), which changes what "local reading" means here.
- **Fix:** Register a predicted heterogeneity amplitude or pattern from the model. Set the null as ΛCDM with Pantheon+ PV covariance plus simulated cosmic variance. Define H̄0 as the GLS mean, set a minimum of 10 SNe per pixel (merging or flagging the rest), delete FAIL (b), and run both z_HD and uncorrected z_CMB.

### M15. T5c (DF2) inputs are misattributed, and the result depends only on σ_ref
- **Where:** PREREG T5c.
- **Evidence:** van Dokkum+18 (arXiv:1803.10237) gives 90% upper limits of M_dyn < 3.2×10⁸ M☉ within **3.1 kpc** and < 3.4×10⁸ within **7.6 kpc**. PREREG attaches 3.4×10⁸ to 3.1 kpc, and the (1.3 ± 0.8)×10⁸ central value isn't in that paper as fetched. NGC 1052's baryonic mass is not given in vD18. A Plummer 3D half-mass radius is 1.305 R_e = 2.87 kpc, not 2.7 kpc. Treating an asymmetric posterior with a 90% upper limit as a symmetric ±0.8 is an unregistered assumption. With the *corrected* kernel and R = 5, M_b(<3.1 kpc) = 1.08×10⁸: σ_ref = 0.5 kpc gives M_pred = 6.3×10⁸ (6.2σ excess, FAIL); 2 kpc gives 3.6×10⁸ (2.8σ, INCONCLUSIVE); ≥ 5 kpc gives a PASS. The "frozen NGC 1052 group model" contributes ≤ 2.5×10⁶ M☉ for any σ_ref ≤ 100 kpc, so it has no effect on the outcome.
- **Fix:** Use vD18's actual 3.1 kpc limit (or a later stellar-kinematic measurement, e.g. Danieli+19, named now) with its published posterior shape. Fix r_½ at 2.87 kpc. State in PREREG that T5c is a test of σ_ref < about 3 kpc, and drop or justify the group term.

---

## MINOR

- **m1. wa_eff in the exploratory (d-Exp) block is wrong** (MAIN §5, EQ §5). Q cancels in the total-density derivative, so E′(1) depends on the *bare* w0: the bracket should be [Ω_m + (1−Ω_m)(1 + w0_eff + ξ_e/3)]. Difference = γ_u ξ_e(Ω_m − 1)/2. Numerical integration of the coupled system gives E′(1) = −0.7808, against −0.7808 for the corrected bracket and −0.678 for the printed one. It is exploratory but feeds Open Problem 11.
- **m2. Perturbation equation coefficient** (MAIN b5-T item 4): the δ_de non-adiabatic term should be 9𝓗²(1+w)(c_s² − c_a²)θ/k², not 3𝓗². Exploratory and unused in v1; the rest of that block was not verified.
- **m3. Q_rate bounds misapplied:** Γ⁻¹ ≳ 150–260 Gyr are bounds on DM decaying to *dark radiation*, not to w = −1 dark energy, and the "> 5σ" figure is unsupported. Implied Γ⁻¹ = 13.8/0.1823 ≈ 76 Gyr.
- **m4. Rounding:** R_pred = 5.00 is 5.64σ, not 5.5σ. f_leak matching R_Planck = 5.3643 is 0.1059, not 0.1067. The cap regime is g_bar ≲ 3.7×10⁻¹², not 3×10⁻¹².
- **m5. Broken cross-references:** "Section 3.3", "Section 4" (unwinding is §5), "Section 4.4", "Section 8.2", "(Section 6)" for the share match (§6 is clusters), PREREG "Section 4.5 below", ASSUMPTIONS "b5-S1, b5-S2" and "(e4)" (no such labels).
- **m6.** MAIN b5-T says "the four published couplings" but lists three couplings and a Boltzmann note.
- **m7. Neutrinos in Ω_m:** [A3] says "absorbs or neglects" Ω_ν. Standard codes include massive ν in Ω_m, and the choice shifts R_pred by 19Ω_ν = 0.027 (≈ 0.2σ_comb). Pick one.
- **m8. Priors:** T1 uses wa ∈ [−5, 3] (DESI uses [−3, 2]), which affects the marginal w0. T2's sampled priors aren't stated at all.
- **m9. T5 χ²_red** divides by N_g, not N_g − 1 (zero free per-galaxy parameters makes N_g defensible, but say so).
- **m10. Doom-factor example:** the z_neg = 5.6 example uses w = −1, where 1 + w = 0, so d is singular everywhere, not just at a_neg. The value z_neg = 5.606 itself is correct.
- **m11.** MAIN's (i-Exp) heading isn't tagged "EXPLORATORY — Not Pre-Registered", which breaks the package's own §Overview rule. EQ has the same omission.
- **m12.** No rule for unphysical f_leak (Ω_m > 7/19 gives f < 0). Register "report, no reinterpretation".
- **m13. ε_far coefficient:** −3.8 reproduces only for z_de ≈ 0.7 with Ω_dm/Ω_m = 5/6 (range 3.80–3.98 for z_de of 0.3–0.7). Register z_de and which Ω ratio is used before v2.
- **m14. Hidden assumption in β_centroid, A14a branch:** the printed R/(1+R) coefficient on Δx̃_S is correct only if the gas shares the stars' post-pericenter deceleration a_dec after the impulsive drop. If the gas coasts, the coefficient is f_S R/(1+R). State this in [A14a].

---

## Pre-data outcome forecast (published numbers, for the record)

| Test | Forecast | Basis |
|---|---|---|
| T1 (w0 > −1 only) | PASS (already known) | P(w0 > −1) ≈ 0.998 (Pantheon+), ≈ 1.000 (Dovekie) |
| T1-L1 (if added) | likely FAIL or disfavoured | Law 1 wa ≈ −0.10 to −0.18 vs DESI −0.62 to −0.86 |
| T2 | FAIL in both runs | 3.5σ (Pantheon+), 3.6σ (Dovekie) |
| Ω_b = 1/19 / H0 | already 3.7–3.9σ | Ω_b 3.9σ high; H0 = 65.2 vs 67.36 ± 0.54 |
| T5-A/B | PASS essentially excluded | cap 6 vs RAR 11.5 at g_bar = 10⁻¹² |
| T5c | set by σ_ref | FAIL for σ_ref ≲ 1 kpc, PASS for ≳ 5 kpc |

---

## Checked and OK

CPL g(a) (sympy); Ω_γh² = 2.4730×10⁻⁵ at 2.7255 K; Ω_ν = Σm_ν/93.14h² ≈ 0.00142; c_s(z) and the R, ℓ_A definitions; (b1)/(b2) effective equations of state and sign convention (Gavela Q_G = −Q, doom factor d = −Q/[3Hρ_de(1+w)]); the transfer f_leak integral; the Q_dm ρ_de(a) solution (sympy) and z_neg = 5.606; the Q_de R(a) solution and ξ_e = 3/13; the ξ_e ≤ 3(1+w0) bound; (d3) w > −1 for uncoupled unwinding; the Law 1, Law 2 and Law 3 tangent wa formulas (sympy); the slope −(3/2)Ω_m; the d-Exp crossing redshift; Δx̃ as the Taylor remainder; A13a; the A13b series (sympy); β_centroid in all three branches and β_peak (sympy, subject to m14); K_σ normalisation = 1; the cap theorem, which is valid for spherically symmetric, outward-decreasing density with the *correct* kernel (proof: the overlap of two balls is largest when they are concentric); the σ → 0 and σ → ∞ limits of the corrected kernel; v_cτ = 30.68 kpc; r/v = 14.7 Myr at 3 kpc; Planck 2018 Table 2 values; R_Planck = 5.364 ± 0.0646; Ω_b = 0.04930 ± 0.00086; the "+2.7σ" Ω_m figure; RAR form and g† = 1.20×10⁻¹⁰; √(3/2)·80 = 97.98 kpc; the SPARC 88/87 split arithmetic; Chen et al. ΛCDM prior values and correlations; the existence of arXiv:2607.27410 and its quoted values; DES-Dovekie file family; all four SHA-256 hashes match.

Sources consulted: Chen, Huang & Wang 2019 (arXiv:1808.05724); Dawson 2013 (arXiv:1210.0014); van Dokkum et al. 2018 (arXiv:1803.10237); DESI DR2 Results II (arXiv:2503.14738); DESI DR2 Results IV, Lyα AP (arXiv:2607.27410); Popovic et al. 2025, DES-Dovekie (arXiv:2511.07517).
