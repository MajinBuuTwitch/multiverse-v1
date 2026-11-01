---
title: "MULTIVERSE Pre-registered Tests, v1"
subtitle: "Pass and fail criteria for the Mandarano Model, set before any data are examined"
author: "Gregory Mandarano / WickedAI"
date: "Version 1.0.1, October 2026"
---

**License:** CC BY 4.0. **Status:** no test in this file has been run. Every result is "untested in v1." Version 1.0.1 changes only T2 (and the rules and rows that refer to it), before any test was run; the reason is in the README changelog.

# The rules

These rules govern every test below and every future version of this file.

1. **No tuning after seeing the test data.** No parameter, kernel shape, sample cut, error model or criterion may be changed after the test dataset has been loaded. A change made afterward voids the test; the test must be re-registered in a new version of this file and run on data not yet examined.
2. **Fix on one dataset, test on another.** Each free parameter is fixed on a named fixing dataset and then tested, frozen, on a different, named test dataset. A dataset used to fix a parameter is never used to test that same parameter. One partial overlap is registered and stated plainly: in T2, the Planck CMB enters the fix only through its compressed distance priors ($R$, $\ell_A$) and the test only through $\omega_c/\omega_b$ (see the T2 independence caveat).
3. **Freeze before testing.** Before a test dataset is opened, the fixed values (with uncertainties), the analysis code version (commit hash), and the date are written to a freeze file, and the file's SHA-256 hash is recorded publicly (in the README changelog of the public folder). The test run must load the frozen values from that file.
4. **Criteria are set now.** The PASS and FAIL thresholds below are part of this version (1.0.1). They can only be changed in a new version, with the reason in the changelog, and only for tests that have not yet been run.
5. **Three outcomes, all reported.** Every test ends as PASS, FAIL, or INCONCLUSIVE (the region between the PASS and FAIL thresholds, or insufficient data). Failures are published with the same prominence as passes.
6. **Structural constants are not free.** $N_s = 19$ and $N_r = 133$ are fixed by the model's geometry and may not be varied to rescue a test.
7. **No double counting.** Pantheon+ and DES SN share low-redshift supernovae and are never combined in one fit; any test that uses supernovae is run separately with each and both results are reported. Planck's $\omega_b$ and $\omega_c$ are used only to test $f_{\rm leak}$ (T2), never to fix it; the T2 fix may use Planck only through the compressed distance priors $R$ and $\ell_A$. Planck also serves as the CMB prior in T1, a test of a different parameter.
8. **Significance language.** "$n\sigma$" means the two-sided Gaussian-equivalent significance of the stated statistic, computed as the analysis paper of each dataset recommends (published likelihoods and covariances).
9. **Model statements count as of the freeze.** If a prediction is ambiguous (for example, whether the model allows a past phantom phase in P1), the ambiguity must be resolved in writing before the freeze, or the affected part of the test is INCONCLUSIVE by default.

Shared parameter names: $N_s$, $N_r$, $f_{\rm leak}$, $\epsilon_{\rm far}$, $w_0$, $w_a$, $\tau_{\rm lag}$, $\sigma_{\rm ref}$. Dataset links are in MULTIVERSE_DATASETS_v1.md; predictions P1 to P9 are in the paper.

# Overview

| Test | Prediction | Parameter fixed or tested | Fixing dataset | Test dataset |
|---|---|---|---|---|
| T1 | P1 dark energy weakening | tests $w_0$, $w_a$ (sign and quadrant) | none from data: the sign is fixed by the model text; Planck 2018 supplies the CMB prior | DESI DR2 BAO + DESI DR2 Lyman-alpha (incl. arXiv:2607.27410) + one SN sample |
| T2 | P3 the ratio; the leak | fixes and then tests $f_{\rm leak}$ | DESI DR2 BAO + compressed CMB priors ($R$, $\ell_A$) + SNe (one sample per run) + BBN $\omega_b$ | Planck 2018 $\omega_c/\omega_b$ |
| T3 | P2 no particle detection | none | none | LZ, and other direct-detection results |
| T4a | P4 young-merger offset sign | tests $\tau_{\rm lag}$ (sign of carried motion) | Bullet Cluster (fixes $\tau_{\rm lag} > 150$ Myr) | Harvey et al. 2015, cross-checked with Wittman, Golovich & Dawson 2018 |
| T4b | P4 age cutoff | fixes and then tests $\tau_{\rm lag}$ | Bullet Cluster (lower bound) + training half of aged mergers | test half of aged mergers (Merging Cluster Collaboration and literature) |
| T5 | P5 halo widths | fixes and then tests $\sigma_{\rm ref}$ | SPARC training half | SPARC held-out half; NGC 1052-DF2 stress check |
| T6 | P7 local Hubble reading | none fitted; SN absolute magnitude fixed | SH0ES Cepheid calibrators | Pantheon+ Hubble-flow supernovae split by sky region |
| none | P6, P8, P9 | $\epsilon_{\rm far}$ and others | not yet registered | see Section "Not yet testable" |

# T1. Dark energy weakening (P1)

- **Parameter tested:** $w_0$, $w_a$ in $w(a) = w_0 + w_a(1-a)$, flat FLRW background.
- **Fixed in advance:** the model's prediction, stated in v1: $w_0 > -1$ (dark energy density falling today). The model does not, in v1, say whether $w(a) < -1$ was allowed in the past, so only $w_0$ is tested (rule 9). DESI's rise-then-fall dark energy history (a phantom past and a crossing of $w = -1$) is not tested here; it is listed in the paper's open problems.
- **Fixing dataset:** none fitted to the model. Planck 2018 enters only as the standard CMB prior (the compressed or full likelihood used by the DESI DR2 analysis).
- **Test dataset:** DESI DR2 BAO and DESI DR2 Lyman-alpha (including the Alcock-Paczyński constraints of arXiv:2607.27410), plus Pantheon+ in one run and DES SN 5-year (DES-Dovekie version) in a second run.
- **PASS:** in both supernova runs, $w_0 > -1$ at 95% credibility (marginalized over $w_a$ and the standard parameters).
- **FAIL:** in either run, $w_0 < -1$ at 95% credibility (dark energy strengthening); **or** in any future data release in which the 68% uncertainty on $w_0$ is 0.03 or smaller, the point $(w_0, w_a) = (-1, 0)$ lies inside the 68% credible region in both supernova runs.
- **INCONCLUSIVE:** anything else.
- **Re-run rule:** T1 is re-run, unchanged, on each new DESI or successor release. A re-analysis of already-published data mostly reproduces the published result, so the decisive versions of T1 are the future ones.

# T2. The leak and the dark-to-ordinary ratio (P3, $f_{\rm leak}$)

- **Parameter:** $f_{\rm leak}$, with model shares $s_b = 1/19$, $s_{\rm dm} = 6(1 - f_{\rm leak})/19$, $s_{\rm de} = (12 + 6 f_{\rm leak})/19$. It has one pre-registered role: fixed from the expansion history, then tested on the dark-to-ordinary ratio. "About one sixth" is the expected value, not a fitted one.
- **Fixing dataset:** DESI DR2 BAO + the compressed CMB distance priors + supernovae, with a BBN baryon density, in flat $w_0w_a$CDM (the background of T1) with the sum of neutrino masses fixed at 0.06 eV. Declared now:
  - the CMB enters only through the shift parameter $R$ and the acoustic scale $\ell_A$: the $(R, \ell_A)$ block of the Planck 2018 distance priors of Chen, Huang & Wang 2019 (JCAP 02 (2019) 028), marginalized over their $\omega_b$;
  - $\omega_b$ comes from the BBN prior of Cooke, Pettini & Steidel 2018 (ApJ 855, 102): $100\,\omega_b = 2.166 \pm 0.019$ (their headline value, statistical and BBN-calculation errors of 0.015 and 0.011 added in quadrature). Planck's $\omega_b$ and $\omega_c$ are not used anywhere in the fix;
  - the fit is run separately with Pantheon+ and with DES SN 5-year (DES-Dovekie version), never combined (rule 7);
  - from the marginalized posterior of the total matter density today, $\Omega_m$ (median and 68% half-width), $f_{\rm leak} = 1 - (19\,\Omega_m - 1)/6$ and $\sigma_f = 19\,\sigma_{\Omega_m}/6$. At exactly one sixth, $\Omega_m = 6/19 \approx 0.316$.
- **Test dataset:** Planck 2018 base $\Lambda$CDM, TT,TE,EE+lowE+lensing (Planck Collaboration 2020, Table 2): $\omega_b = 0.02237 \pm 0.00015$, $\omega_c = 0.1200 \pm 0.0012$, so $R_{\rm Planck} = \omega_c/\omega_b = 5.36 \pm 0.065$ (relative errors added in quadrature, the correlation between the two ignored; this value and uncertainty are fixed now).
- **Prediction:** $R_{\rm pred} = 6(1 - f_{\rm leak})$, equivalently $19\,\Omega_m - 1$, with uncertainty $6\sigma_f$.
- **PASS:** $|R_{\rm pred} - R_{\rm Planck}| \le 2\sigma_{\rm comb}$, where $\sigma_{\rm comb} = \sqrt{(6\sigma_f)^2 + \sigma_{\rm Planck}^2}$ and $\sigma_{\rm Planck} = 0.065$, in both supernova runs.
- **FAIL:** otherwise ($|R_{\rm pred} - R_{\rm Planck}| > 2\sigma_{\rm comb}$ in either supernova run).
- **INCONCLUSIVE:** only for insufficient data (a fixing run whose code fails to reproduce a published $\Lambda$CDM result from the same data, or whose sampling does not converge). T2 has no threshold region between PASS and FAIL.
- **Stated in advance, honestly:** at $f_{\rm leak} = 1/6$ the prediction is $6 \times 5/6 = 5.0$, which sits about 5.6 $\sigma$ below Planck's 5.36 counting Planck's uncertainty alone. The combined $\sigma$ also contains $6\sigma_f$, so the final margin depends on how tightly the expansion fit pins $f_{\rm leak}$, but this test is expected to FAIL unless the expansion fit lands well below one sixth. This is the ratio tension listed in the paper's open problems. A FAIL here does not touch the other tests, but it would mean the leak, in its v1 form, does not work.
- **Independence caveat:** $R$ and $\ell_A$ are derived from the same Planck maps as the test's $\omega_c/\omega_b$, and $R$ depends on the matter density, so the fix and the test are not fully independent. Keeping Planck's $\omega_b$ and $\omega_c$ out of the fix (BBN supplies $\omega_b$) reduces the overlap; it does not remove it.
- **Downstream use:** T5 uses the $f_{\rm leak}$ frozen in the Pantheon+ run (declared now).
- **Variant forbidden:** $f_{\rm leak}$ has no other fix and no alternative value. It may not be refitted to the ratio or fixed on Planck's $\omega_b$ or $\omega_c$, and $\epsilon_{\rm far}$ may not be introduced to absorb a T2 failure, unless such a change is registered in a later version and tested on new data.

# T3. No direct detection (P2)

- **Parameter:** none.
- **Test dataset:** LZ results (the 2025 PRL and all later releases, including the full analysis of the event announced on 1 September 2026), and published results of other direct-detection experiments.
- **PASS (ongoing, assessed at each release):** no confirmed non-gravitational detection of a particle that can account for the cosmological dark matter.
- **FAIL:** a detection at 5 $\sigma$ or more in one experiment, or at 3 $\sigma$ or more independently in two experiments using different target materials, of a signal consistent with a single dark matter particle, accepted by the collaborations concerned as a detection.
- **INCONCLUSIVE:** excesses below these thresholds, including the 2026 LZ event at about 2.6 $\sigma$.

# T4a. Offset sign in young mergers (P4, carried motion)

- **Parameter tested:** the carried-motion form of the lag, which predicts the dark mass sits slightly *ahead* of the galaxies (away from the gas) in mergers younger than $\tau_{\rm lag}$.
- **Fixing dataset:** the Bullet Cluster: time since core passage 0.1 to 0.2 Gyr (Markevitch et al. 2002) with lensing mass on the galaxies (Clowe et al. 2006) fixes $\tau_{\rm lag} > 150$ Myr.
- **Test dataset:** the star, gas and lensing-mass positions of Harvey et al. 2015, with the same analysis repeated on the re-measurement of Wittman, Golovich & Dawson 2018. Primary sample: systems with an independently published time since pericenter below 150 Myr. Secondary sample: all systems (reported, but a secondary-sample result alone can only give INCONCLUSIVE, because some systems may be older than $\tau_{\rm lag}$).
- **Statistic:** the mean dark-mass-minus-stars offset projected on the axis from the gas to the stars (positive = away from the gas).
- **PASS:** positive at 2 $\sigma$ or more in the primary sample in both catalogs.
- **FAIL:** negative (toward the gas, the self-interacting dark matter sign) at 2 $\sigma$ or more in the primary sample in both catalogs.
- **INCONCLUSIVE:** consistent with zero, or the two catalogs disagree. v1 gives no predicted magnitude, so a null result cannot fail the model; this weakness is recorded, and a magnitude must be registered before T4a can fail on a null.

# T4b. The age cutoff (P4, $\tau_{\rm lag}$)

- **Parameter:** $\tau_{\rm lag}$, assumed universal.
- **Prediction:** a single $\tau_{\rm lag} \geq 150$ Myr separates mergers whose dark mass sits with the galaxies ($t_p < \tau_{\rm lag}$) from mergers whose dark mass has shifted toward the gas ($t_p > \tau_{\rm lag}$).
- **Sample:** every merging cluster with (i) a published time since pericenter from a dynamical analysis and (ii) a published lensing mass map and X-ray gas map; sources include the Merging Cluster Collaboration systems, the Bullet Cluster, the Musket Ball, MACS J0025.4-1222, El Gordo and Abell 520. The sample list and every age, with its source, is frozen before any classification is done.
- **Classification rule (declared now):** a system is "dark mass with gas" if its main lensing peak lies closer to the X-ray gas peak than to the galaxy luminosity centroid and the difference in distance exceeds twice the combined positional uncertainty; "dark mass with galaxies" by the mirror rule; otherwise unclassified and excluded.
- **Fix/test split:** systems are ordered by name (alphabetically, catalog designation); odd positions form the training half, even positions the test half. The Bullet Cluster is always in the training half.
- **Fixing:** on the training half, $\tau_{\rm lag}$ is the step location (searched on a grid starting at 150 Myr) that classifies the most systems correctly; ties go to the smallest value.
- **PASS:** on the test half, the frozen step classifies at least 80% of classified systems correctly, with at least six classified test systems.
- **FAIL:** (a) no step at or above 150 Myr classifies at least 80% of the training half correctly; or (b) the frozen step classifies fewer than 60% of the test half correctly; or (c) every classified system, including at least one with $t_p \geq 1$ Gyr, has its dark mass with the galaxies (no cutoff below 1 Gyr), unless the model has registered $\tau_{\rm lag} > 1$ Gyr before this test.
- **INCONCLUSIVE:** fewer than six classified test systems, or test accuracy between 60% and 80%.

# T5. Halo widths from the refraction kernel (P5, $\sigma_{\rm ref}$)

- **Parameter:** $\sigma_{\rm ref}$.
- **Model declared now:** each galaxy is treated as isolated. The shadow mass distribution is $6(1 - f_{\rm leak})$ times the galaxy's baryonic mass distribution convolved with a normalized three-dimensional Gaussian of width $\sigma_{\rm ref}$; $f_{\rm leak}$ is the T2 frozen value (Pantheon+ run). Baryons come from the SPARC mass models with fixed 3.6 $\mu$m mass-to-light ratios of 0.5 (disk) and 0.7 (bulge) and the SPARC gas component; no per-galaxy mass-to-light freedom. Two variants are registered and both are reported: **T5-A**, a single constant $\sigma_{\rm ref}$ in kpc; **T5-B**, $\sigma_{\rm ref} = k\,R_d$ with one constant $k$ and $R_d$ the SPARC disk scale length. No other variants.
- **Fixing dataset:** the SPARC training half: galaxies ordered by SPARC name, odd positions. $\sigma_{\rm ref}$ (or $k$) minimizes the total $\chi^2$ of the rotation curves using SPARC's quoted velocity errors.
- **Test dataset:** the SPARC held-out half (even positions), with the frozen value.
- **PASS:** on the test half, the median reduced $\chi^2$ is at most 1.5 and at least 70% of galaxies have reduced $\chi^2$ below 2.
- **FAIL:** on the test half, the median reduced $\chi^2$ exceeds 3, or fewer than 40% of galaxies have reduced $\chi^2$ below 2.
- **INCONCLUSIVE:** between these.
- **T5c, stress check (NGC 1052-DF2):** with the frozen $f_{\rm leak}$ and $\sigma_{\rm ref}$ (T5-A), and including the shadow of the published baryonic mass of the NGC 1052 group within the convolution, compute the predicted mass within DF2's stellar half-light radius. **PASS** if it is within 2 $\sigma$ of the published dynamical mass (van Dokkum et al. 2018); **FAIL** if it exceeds the published dynamical mass by more than 3 $\sigma$; INCONCLUSIVE otherwise. Any group-baryon model used here is frozen before DF2's dynamical mass is compared.

# T6. The Hubble tension as a local reading (P7)

- **Parameter:** none fitted (v1 gives no amplitude).
- **Fixing dataset:** the SH0ES Cepheid-calibrated supernova absolute magnitude, from the calibrator sample only (Riess et al. 2022), frozen.
- **Test dataset:** Pantheon+ Hubble-flow supernovae (the redshift range used by SH0ES for the Hubble flow), with the published peculiar-velocity corrections, split into the 12 equal-area sky regions of a HEALPix $N_{\rm side} = 1$ grid (declared now). $H_0$ is fitted in each region with the frozen absolute magnitude.
- **Statistic:** the $\chi^2$ of the regional $H_0$ values about their weighted mean, using the full covariance.
- **PASS:** heterogeneity significant at 3 $\sigma$ or more, while the all-sky local $H_0$ still exceeds the Planck 2018 $\Lambda$CDM value at 3 $\sigma$ or more.
- **FAIL:** heterogeneity consistent with zero ($p > 0.32$) while the all-sky tension remains at 3 $\sigma$ or more (the tension would then be global rather than local); **or** a published resolution of the tension traced to distance-ladder systematics, accepted by the SH0ES team.
- **INCONCLUSIVE:** anything else.

# Not yet testable

The paper's honesty requires saying which predictions cannot fail yet.

- **P6, the far-string contribution ($\epsilon_{\rm far}$):** v1 gives no target value or clustering signature. No test is registered. Registering one requires a numerical target for $\epsilon_{\rm far}$ and the observable it changes, recorded before any data are examined.
- **P8, locality of differences:** a consistency requirement. Its concrete content is tested through T4 and T5.
- **P9, departure from standard quantum mechanics inside a rope:** v1 gives no size or form. No test is registered.

Until these are registered, they are not evidence for the model in any sense, because they cannot fail.

# Reporting format for any test run

Each test run should report: the test ID and version of this file; the freeze file's SHA-256 and date; dataset releases and download dates; the frozen parameter values; the statistic, its uncertainty and the outcome (PASS, FAIL or INCONCLUSIVE) against the thresholds above; and any deviation from this protocol, which automatically marks the result as not pre-registered.
