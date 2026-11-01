# DEVIATIONS_REBUILD.md

Every departure from the frozen package, and every interpretation the rulebook left open, is logged here
BEFORE the affected test is computed. Each entry gives what, why, the expected effect, and when it was logged.

---

## D1 — `_ORIGINALS` subfolder does not exist (package verification)
- **What:** REBUILD_RULES.md says to hash the files in `_ORIGINALS`, but this workspace has no such folder. The frozen files are in the workspace root instead. They were verified there against PREREG_v4.sha256, and all 9 files present match.
- **Why:** Workspace layout as delivered.
- **Expected effect:** None. The hashes match byte-for-byte, and the root copies are treated as read-only originals.
- **Logged:** 2026-10-30T06:19:31-04:00.

## D2 — Gate G9-b reference values: "Chen, Huang & Wang (2019) Table 2" does not exist
- **What:** PREREG.md §2 G9-b says to reproduce the flat-ΛCDM posteriors (Ωm, h, ωb) in "their Table 2" to within 0.3σ. The paper (arXiv:1808.05724, e-print read 2026-10-30T10:25Z) has only one table: Table 1, the distance priors and correlation matrices. Its ΛCDM parameter check is a figure (`lcdm.pdf`, Fig. "Constraints on parameters in the base ΛCDM model"). That figure compares the distance-prior contours with the Planck 2018 `base_plikHM_TTTEEE_lowl_lowE` chains, which are the chains the priors were compressed from.
- **Substitute (single, fixed before the gate is run):** the gate benchmark is the Planck 2018 VI (A&A 641, A6, arXiv:1807.06209) **Table 2, "TT,TE,EE+lowE" column**. This is the same likelihood and chains that Chen et al. compressed and compared against:
  - Ωm = 0.3166 ± 0.0084
  - H0 = 67.27 ± 0.60, i.e. h = 0.6727 ± 0.0060
  - Ωb h² = 0.02236 ± 0.00015
  - The 0.3σ tolerance is unchanged: |ΔΩm| ≤ 0.00252, |Δh| ≤ 0.00180, |Δωb| ≤ 0.000045.
  - The compared statistic is the posterior mean of each parameter.
- **Why:** The registered reference cannot be read off a table, and digitising a figure would add an unregistered free choice. Planck Table 2 TT,TE,EE+lowE is what the Chen et al. figure overlays, so it is the closest published numerical benchmark.
- **Expected effect:** If the compressed prior plus the registered theory computation reproduces Planck, the gate passes. A failure would make T1-L1, T1-Sign, T2-A and T2-B INCONCLUSIVE, per the registered mapping.
- **Note (diagnostic only, recorded before the gate run):** The registered theory computation uses the HS96 z* fit, the registered E(a) with photons, 3.044 neutrinos and one massive ν, and the r_s integral. At the Planck best-fit parameters it gives ℓ_A ≈ 302.07, versus the prior mean 301.471. Our D_M(z*) agrees with CAMB 2.0.5 to 3×10⁻⁶ and our r_s(z*) to 5×10⁻⁵, so this is not an implementation bug. The offset comes from the registered z*/ℓ_A convention relative to how the published prior mean was derived. No change is made: the registered equations are used as written, and the gate decides.
- **Logged:** 2026-10-30T06:37:06-04:00 (before G9-b was computed).

## D3 — r_d: interpretation of "EH98 z_d calibrated to CLASS/CAMB via the standard post-Planck drag-scale factor"
- **What:** r_d = F × r_s(z_d^EH98), where r_s is the registered sound-horizon integral at the registered EH98 z_d.
  - F is one constant, computed once with CAMB 2.0.5 at the Planck 2018 TT,TE,EE+lowE+lensing mean cosmology (ωb = 0.02237, ωc = 0.1200, H0 = 67.36, Σmν = 0.06 eV in one massive state, N_eff = 3.044): F = r_drag(CAMB)/r_s(z_d^EH98) = 147.1027/150.7552 = **0.975772**.
  - CAMB is never called inside a sampling loop.
  - Validation against CAMB over a 6×5×3 grid (ωb 0.020–0.025, ωc 0.10–0.14, h 0.60/0.6736/0.75): maximum |fractional error| is 0.13% over the whole grid and 0.043% within ±0.0011 in ωb and ±0.011 in ωc of the fiducial (`results_rebuild/validation/rd_calibration.json`).
- **Why:** The rulebook does not define the "drag-scale factor" numerically. A single multiplicative CAMB calibration of r_d is the most literal reading. It keeps the registered fast method, and the REBUILD_RULES allow one-off Boltzmann calibration outside the loop.
- **Expected effect:** At most 0.04% in r_d over the posterior region, which is about 0.05σ of the most precise DESI BAO point. Negligible.
- **Logged:** 2026-10-30T06:37:06-04:00 (before any BAO+CMB fit).

## D4 — Sampler: rebuild's own sampler instead of emcee with 32 walkers
- **What:** PREREG §4 names emcee with 32 walkers. REBUILD_RULES.md says samplers are the rebuild's own choice. I used my own multi-chain sampler:
  - 8 independent chains, started from dispersed points.
  - Random-walk Metropolis. The proposal covariance is adapted for 4,000 steps per chain, its scale is tuned to 20–35% acceptance, and then both are frozen. Burn-in is 3,000 steps with the frozen proposal, extended if needed so that it is at least max(1000, 5τ).
  - Production runs in blocks of 4,000 steps per chain. It stops only when classic split-R̂ − 1 < 0.01, rank-normalised split-R̂ − 1 < 0.01, bulk ESS > 1000 for every parameter, and total production ≥ 128,000 samples (the registered production minimum).
  - Maximum extension is 80,000 production steps per chain. Not meeting the criteria by then is the registered G8 non-convergence trigger.
  - χ²_min uses the registered optimiser exactly: Nelder–Mead (xatol = fatol = 1e-6, maxiter = 10,000) from the 5 highest-likelihood MCMC samples, then bounded L-BFGS-B (ftol = 1e-12).
  - Seeds: master SEED = 20261030; the run with sorted index i uses SEED + 1000·i.
- **Why:** Independence by design (REBUILD_RULES). Genuinely independent chains also make the Gelman–Rubin statistic meaningful.
- **Expected effect:** Posterior summaries are unchanged apart from Monte Carlo noise. Deciding Δχ² values come from the optimiser, not the sampler.
- **Logged:** 2026-10-30T06:37:06-04:00.

## D5 — Hardware and environment
- **What:**
  - Up to 24 worker processes on a 28-thread machine, set by the REBUILD_RULES instruction to leave about 4 threads free. The registered cap is 12.
  - Each worker runs single-threaded BLAS at BELOW_NORMAL priority, as registered.
  - The venv is local (`d:\Blind_Rebuild\.venv`, Python 3.14.7) with the registered pins numpy == 2.5.4 and scipy == 1.18.1; the registered path D:\Argon_Code\... is not used.
- **Why:** Blindness rules and REBUILD_RULES.
- **Expected effect:** None on any number.
- **Logged:** 2026-10-30T06:37:06-04:00.

## D6 — Second data manifest for literature sources
- **What:** DATA_MANIFEST_REBUILD.sha256 was written and OTS-stamped at 06:28:55, before any fit. It covers the registered datasets plus the Chen 2019 and Planck 2018 e-prints and the DES-Dovekie format documentation. The T4b position-source papers were still being downloaded by sub-agents at that time. They are fingerprinted in a second manifest, DATA_MANIFEST_REBUILD_PAPERS.sha256, which is OTS-stamped before the T4b classification is computed.
- **Why:** Stamping must precede fits, and the cosmology fits do not depend on the papers.
- **Expected effect:** None.
- **Logged:** 2026-10-30T06:37:06-04:00.

## D7 — wCDM-column CMB prior sensitivity (NON-DECIDING): errors and correlations
- **What:** PREREG gives only the wCDM mean vector (1.7493, 301.462, 2.239). For this non-deciding run I use the wCDM column's own Table 1 errors, symmetrised: R ± 0.00465 (from +0.0046/−0.0047), ℓ_A ± 0.0895 (from +0.089/−0.090), ωb ± 0.00015. I also use that column's correlation matrix (0.47, −0.66, −0.34).
- **Why:** These are the values the rulebook leaves unstated.
- **Expected effect:** Sensitivity only.
- **Logged:** 2026-10-30T06:37:06-04:00.

## D8 — Recorded interpretations (no departure intended)
1. The sampled Ωm is Ωm,tot (baryons + CDM + massive ν today). Ω_ν,0 = 0.06/(93.14 h²) and Ωbc = Ωm − Ω_ν,0. Flatness is closed by Ω_de = 1 − Ω_r − Ωm.
2. Neutrinos: two massless species plus one 0.06 eV species with the exact Fermi–Dirac energy-density shape F(m a/kT_ν)/a⁴. T_ν0 = (4/11)^{1/3}(3.044/3)^{1/4} T_CMB. The amplitude is normalised so the massive species equals the registered Ω_ν,0 today.
3. Pantheon+: μ_model = 5 log10[(1+z_HEL) D_M(z_HD)/Mpc] + 25, compared with `m_b_corr`. Cut: z_HD > 0.01 and IS_CALIBRATOR == 0, giving 1580 SNe. The STAT+SYS covariance sub-block is used.
4. DES-Dovekie: all 1820 SNe in DES-Dovekie_HD.csv, `MU` with the full STAT+SYS inverse covariance (as distributed) and the same μ_model.
5. In both SN samples M is marginalised analytically: χ² = ΔᵀWΔ − (1ᵀWΔ)²/(1ᵀW1). The constant ln term is dropped; it cancels in every Δχ².
6. Gate statistics use the posterior mean.
7. Law-1 g(a): RK4 on the registered 1000-point log-a grid over a ∈ [10⁻⁴, 1]. ln g is held constant for a < 10⁻⁴, where |d ln g/d ln a| = 3γ/E < 10⁻⁵.
8. T2-B (non-deciding): ωb = h²/19 is imposed and the registered 100ωb ∈ [1.8, 2.6] bound is kept. Its Δχ² reference is the T2-A w0waCDM fit on the same datasets.
- **Logged:** 2026-10-30T06:37:06-04:00.

## D9 — Gate G9-d: the registered unit-test script is not available
- **What:** G9-d refers to the kernel "implemented in `verify_b1_kernel_mc.py`". That file belongs to the original analysis and must not be used. I test my own implementation of the registered piecewise kernel on the registered 5×7 grid against `scipy.stats.ncx2.cdf((r/σ)², df=3, nc=(r'/σ)²)`, with absolute tolerance < 1e-10, under numpy 2.5.4 and scipy 1.18.1. The r'/σ = 1e-5 column uses the point-mass branch, as registered. The ncx2 reference at nc = 0 is evaluated as ncx2 with nc = 0.0 if scipy accepts it; otherwise as `chi2.cdf(x, 3)`, which is mathematically identical, and that fallback would be logged.
- **Why:** Blindness rules.
- **Expected effect:** None.
- **Logged:** 2026-10-30T06:37:06-04:00.

## D10 — T4b: mechanical decisions on the extracted position data (logged before the T4b statistic was computed)
These decisions apply the pre-written t4b_extraction/EXTRACTION_PROTOCOL.md (06:23:48) to what the 16 registered source papers contain. Extraction details are in t4b_extraction/cluster_NN.json and cluster_NN_notes.md.
1. **What counts as x_S.** A galaxy position counts as the "luminosity-weighted galaxy centroid" only if the paper calls it a centre or centroid of the galaxy light (luminosity) distribution. Positions the paper explicitly calls a "peak" of a smoothed (luminosity-weighted) density map do not count: Abell 1240 Table 2, MACS J1149 §3.2, ZwCl 0008 Table 3, El Gordo, and the Toothbrush "luminosity peak". For those clusters the BCG fallback applies.
2. **MACS J0025.4-1222 (row 13), Bradač et al. 2008.** The Table 2 "galaxies" rows are introduced in §4.3 as "the centers of the light distributions (galaxies). The measured positions and error bars are given in Table 2". They are read as the luminosity-weighted galaxy centre, with 1σ errors from the Table 2 caption.
   - The X-ray peak error is the Table 2 per-axis 1σ value, ±0.08′. The text separately calls it a top-hat bound of "within 5 arcsec"; the tabulated 1σ value is used.
   - **This decision matters for the verdict.** Row 13 is the only cluster for which all three positions and their uncertainties are available. If the "galaxies" row were rejected, n_train = 0 and T4b would end in FAIL under clause 1(a). Both outcomes are reported; the alternative goes in the NON-DECIDING section.
3. **Positions given as offsets.** Positions given as tabulated (Δx, Δy) offsets from a reference point (row 13) or as stated separations are accepted, because only d_IG and d_IS are needed (protocol).
4. **Errors on separations.** An error quoted on a separation (for example "22 ± 12″" between I and G for Abell 2744, or "57 (+36/−34)″" between I and S for Abell 2034) is not a per-position σ_c. A cluster missing a per-position σ for any of I, G or S, with no instrument centroiding error stated in its text, is marked "unclassified" by the registered missing-data rule. No secondary literature is used to fill gaps.
5. **Asymmetric per-axis errors.** Where a position has asymmetric per-axis errors, each axis uses the mean of the + and − errors, followed by the registered quadrature rule σ_c = sqrt((σ_α*² + σ_δ²)/2). RA errors printed in seconds of time are converted with 15″ cos δ per second.
6. **Subcluster as designated.** The designated subcluster is used as named in the PREREG table. For Abell 2744 the "Core/NW" designation is ambiguous; Core is the primary record and NW is reported as a sensitivity. Neither is classifiable, because G and S lack per-position errors.
- **Logged:** 2026-10-30T06:42:10-04:00.

## D11 — T5 dependence on gates G9-a / G9-b (interpretation, logged before T5 is computed)
- PREREG §2 G9 says gates G9-a/G9-b map to T5 "only if T2-A-Pantheon+ fails to produce a converged f_leak because G9-a or G9-b failed". I read this literally. If the T2-A-Pantheon+ chain converged, the frozen f_leak exists and T5-A/T5-B/T5c are evaluated with it, whatever the outcome of G9-a/b. T5 becomes INCONCLUSIVE by this route only if the T2-A-Pantheon+ run did not converge.
- If a G9-a/b gate fails, the alternative reading (T5 INCONCLUSIVE) is stated next to the T5 verdict.
- **Logged:** 2026-10-30T06:42:10-04:00.

## D12 — Hand-over review of D10 item 2 (row 13 galaxy position); no change made
- **What:** The new agent independently re-checked row 13 against the e-print (`data/papers/bradac2008_macs0025/src_D/ms.tex`, which is byte-identical to the archived e-print). The Table 2 values in t4b_positions_rebuild.json are transcribed correctly.
- **Finding:** The reading is open to doubt.
  - The Table 2 caption reads "Offsets (with 1σ errorbars) of the mass peaks and gas peaks".
  - The only luminosity distribution the paper describes (§6) is a K-band map "smoothed with a Gaussian kernel with FWHM 80 kpc".
  - The wording "centers of the light distributions (galaxies)" (§4.3) is therefore compatible with the "galaxies" row being the peak of a smoothed luminosity map. D10 item 1 does not accept that kind of position for other clusters.
  - The paper never explicitly says "luminosity-weighted".
- **Decision:** D10 item 2 is kept exactly as logged at 06:42:10. It was fixed under the pre-written protocol before any T4b statistic was computed. Re-deciding it now, when its consequence is known, would itself be a post-hoc choice.
  - The alternative reading (row 13 unclassified → n_train = 0 → T4b FAIL by clause 1(a)) is reported next to the T4b verdict in REBUILD_RESULTS.md with equal prominence, not only in the NON-DECIDING section.
- **Expected effect:** None on the computation. It makes clear that the T4b pillar verdict rests on this one interpretive call.
- **Logged:** 2026-10-30T07:30:05-04:00 (before the T4b statistic is computed).
