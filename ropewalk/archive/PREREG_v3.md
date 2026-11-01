---
title: "MULTIVERSE Master Pre-Registration Protocol (PREREG.md)"
subtitle: "Frozen Analysis Choices, Single Deciding Test Versions, Likelihoods, and Pass/Fail Thresholds (v1.0.1, Revised Post-Review V2)"
author: "Gregory Mandarano / WickedAI — Pre-Registration Compiled by Gemini 4 Argon"
date: "2026-10-30"
---

# 1. Purpose, Precedence Clause, and Deliberate Amendments from `MULTIVERSE_TESTS_v1.md`

## 1.1 Immutability & Precedence Declaration (Resolving Finding N3)
This document (`PREREG.md`) is written, SHA-256 hashed (`PREREG_v3.sha256`), and externally timestamped (`PREREG_v3.sha256.ots`) at the end of Stage 1 **before any dataset is downloaded or read by analysis code**.

> **Precedence Clause (N3):** Where this file (`PREREG.md`) and any earlier or companion file (`MULTIVERSE_TESTS_v1.md`, `MULTIVERSE_ARGON_HANDOFF.txt`, `GEMINI.md` Rule R12, or any `STAGE1_PART*.md` file) disagree, **this file (`PREREG.md`) governs. `MULTIVERSE_TESTS_v1.md` is superseded for every test it shares with this file.** `MULTIVERSE_STAGE1_EQUATIONS.md` governs all mathematical equations. The `STAGE1_PART*.md` files are historical derivation notes with no governing force.

> **One Deciding Version Per Test Rule:** Every scored test in this protocol has **exactly one registered deciding version** (one dataset combination, one prior choice, one statistic, one error formula, and one mutually exclusive and collectively exhaustive `PASS` / `FAIL` / `INCONCLUSIVE` partition). Additional variants listed under **`Sensitivity Analyses`** are computed and reported for completeness, but **can never change any test's `PASS`, `FAIL`, or `INCONCLUSIVE` verdict**.

## 1.2 Numbered List of Deliberate Pre-Data Amendments to `MULTIVERSE_TESTS_v1.md` (Finding N3)
All amendments below were required by the two independent pre-data cold reviews (`REVIEW_COLD.md` and `REVIEW_V2.md`) before any data were downloaded:
1. **Test T1 Replaced by `T1-L1` (Primary) and `T1-Sign` Demoted to Secondary (`B4`, `N5`):** Because the v1 sign check ($w_0 > -1$ in unconstrained $w_0w_a\text{CDM}$) was already known from published DESI papers to pass and did not test the model's derived unwinding law $w(a) = -1 + \gamma_u/E(a)$, the direct 1-parameter fit of Law 1 (`T1-L1`) is registered as **Pillar 1**, while the CPL sign check (`T1-Sign`, with explicit one-sided 95% threshold $P(w_0 > -1 \mid \text{data}) \ge 0.95$) is demoted to a non-deciding secondary check.
2. **Test T2 Refined to `T2-A` with Explicit $\Omega_{bc}$, Conditional CMB Likelihood, and DESI/LUNA BBN Prior (`M1`, `M9`, `N1`, `N7`):** To prevent massive neutrinos ($\Omega_{\nu,0} \approx 0.00142$) and the $3.6\sigma$ CMB–Cooke(2018) BBN discrepancy from biasing $f_{\rm leak}$, the deciding **Pillar 2 (`T2-A`)** uses $\Omega_{bc} \equiv \Omega_{m,{\rm tot}} - \Omega_{\nu,0}$, the conditional likelihood $(R, \ell_A \mid \omega_b)$ from Chen et al. (2019), the DESI DR2 / post-LUNA BBN prior ($100\omega_b = 2.218 \pm 0.055$), and the original v1 uncorrelated error formula $\sigma_{\rm comb} = \sqrt{(19\sigma_{\Omega_{bc}})^2 + 0.065^2}$. **The original v1 dual-run rule (`PASS` if both SN runs pass; `FAIL` if either SN run fails) is preserved.** Direct tests of $\Omega_b = 1/19$ (`T2-N1`) and $H_0^{\rm pred} = 100\sqrt{19\omega_b}$ (`T2-N2`) are registered as secondary tests.
3. **Test T4a Unconditionally Demoted to `EXPLORATORY` (`B3`):** Under the energy-conserving symmetric harmonic core-passage trajectory (`A13b`), the shadow offset trails *behind* the stars for $0 < T \lesssim \frac{2}{3}\tau_{\rm lag}$, and excluding the Bullet Cluster leaves only $N = 1$ cluster below the original $150\text{ Myr}$ cut. T4a is therefore **unscored (`EXPLORATORY`) in v1 regardless of sample size $N$, age cut, or catalog**.
4. **Test T4b Bullet Cluster Age Updated to Dawson (2013) Temporal Prior with $235\text{ Myr}$ Grid Floor (`M6`, `N2`, `N8`):** The Bullet Cluster age is fixed to the median $t_p = 0.40\text{ Gyr}$ ($\sigma_{t_p} = 0.10\text{ Gyr}$) of Dawson (2013, Table 2, temporal prior), and the $\tau_{\rm lag}$ search grid floor is fixed to the one-sided 95% lower confidence bound of that posterior, **$\tau_{\rm lag,\min} = 235\text{ Myr}$** (replacing $150\text{ Myr}$).
5. **Test T5 Split into `T5-A` (Sole Primary Pillar 4) and `T5-B` (Secondary Sensitivity) (`M10`, `N9`):** To prevent multiple-testing inflation across two kernel-width parametrizations, `T5-A` (constant $\sigma_{\rm ref}$ in kpc) is the sole deciding rotation-curve pillar test, while `T5-B` ($\sigma_{\rm ref} = k\,R_d$) is a secondary test that cannot rescue a `T5-A` failure.
6. **Test T6 Sparse-Pixel Merging and Mechanical FAIL Rule (`M14`, `N9`):** Low-Galactic-latitude HEALPix $N_{\rm side} = 1$ pixels with $N_{\rm SN,i} < 10$ are merged into adjacent same-quadrant higher-$|b|$ pixels ($\text{dof} = N_{\rm pix} - 1$), the non-mechanical sociological SH0ES clause is removed, and the FAIL condition is made unconditional on $p_{\rm het} > 0.3173$.

---

# 2. General Rules (G1–G9, Tightened per Review Findings B1, M8, M10, N3)

- **G1. No tuning after seeing the test data.** No parameter, kernel shape, sample cut, error model, or criterion may change after a test dataset has been loaded; any change voids the test.
- **G2. Fix on one dataset, test on another.** A dataset used to fix a parameter is never used to test that same parameter. In `T2-A`, the Planck CMB enters the fix only through the conditional distance likelihood $(R, \ell_A \mid \omega_b)$ coupled to the external DESI/LUNA BBN $\omega_b$ prior, and the test only through $\omega_c/\omega_b$. In cluster tests, the Bullet Cluster (`1E 0657-558`) is never included in any test sample.
- **G3. Freeze before testing.** Before a test dataset is opened, write the fixed values (with uncertainties), the analysis code version (SHA-256 of `scripts/`), and the date to `results/FREEZE_<test>.json`, and record its SHA-256. The test run must load the frozen values directly from that file.
- **G4. Thresholds are fixed and exhaustive.** Three outcomes, all reported with equal prominence: `PASS`, `FAIL`, `INCONCLUSIVE`. Every test's outcome rules partition the space of converged results into three mutually exclusive and collectively exhaustive sets.
- **G5. Structural constants are not free.** $N_s = 19$ and $N_r = 133$ may not be varied.
- **G6. No double counting.** Pantheon+ and DES SN (`DES-Dovekie`) are never combined in one fit; every supernova test is run separately with each, and both results are reported. In DESI DR2 BAO, the $z_{\rm eff} = 2.33$ Ly$\alpha$ BAO row in `desi_bao_dr2` is removed and replaced by the joint Ly$\alpha$ BAO+AP vector of Cuceu et al. (2025, arXiv:2607.27410) so Ly$\alpha$ BAO is never double-counted (`M7`).
- **G7. Significance language.** "$n\sigma$" means the two-sided Gaussian-equivalent significance computed with each dataset's published likelihood and covariance (except in `T1-Sign`, where the one-sided $95\%$ posterior tail $P(w_0 > -1 \mid \text{data}) \ge 0.95$, $z \ge 1.645$, is stated explicitly).
- **G8. Strict Mechanical Trigger for `INCONCLUSIVE` (No Post-Unblinding Escape Hatch, `M10`, `N3`).** Every model and analysis choice is resolved in writing in this document before the freeze. Post-unblinding invocation of G8 to label a test `INCONCLUSIVE` is **forbidden**. A test may return `INCONCLUSIVE` **only** if one of the following four mechanical numerical conditions is triggered:
  1. MCMC convergence failure (Gelman–Rubin $R - 1 \ge 0.01$ or $\text{ESS} \le 1000$ after maximum step extension);
  2. Failure of a mandatory pre-test validation gate (`G9-a` through `G9-d` below);
  3. Fewer than the pre-registered minimum sample size ($< 6$ classified test clusters in `T4b`);
  4. The computed test statistic falls strictly inside the pre-registered `INCONCLUSIVE` numerical interval defined for that test (or fails the Holm–Bonferroni discovery threshold under Section 3.2).
- **G9. Mandatory Pre-Test Validation Gates and Convergence Criteria (`B1`, `M8`, `Review V2 Minor`).** Before any model test is executed, the analysis pipeline must pass all four validation gates:
  - **Gate G9-a (DESI DR2 BAO Validation):** Reproduce the published DESI DR2 BAO-only flat $\Lambda\text{CDM}$ constraint $\Omega_m = 0.2975 \pm 0.0086$ (DESI Collaboration 2025b, Table V) to within $0.3\sigma$.
  - **Gate G9-b (Compressed CMB Prior & $r_s(z_*)$ Validation):** Reproduce the Chen, Huang & Wang (2019, Table 2) flat $\Lambda\text{CDM}$ parameter posteriors ($\Omega_m, h, \omega_b$) from their Table 1 $\Lambda\text{CDM}$ $(R, \ell_A, 100\omega_b)$ prior to within $0.3\sigma$.
  - **Gate G9-c (Full DESI + CMB + SNe $w_0w_a\text{CDM}$ Validation):** Reproduce the published DESI DR2 + Planck CMB + DES-Dovekie $w_0w_a\text{CDM}$ $(w_0, w_a)$ posterior ($w_0 = -0.803 \pm 0.054, w_a = -0.72 \pm 0.21$, Popovic et al. 2025, Table 11) to within $0.3\sigma$.
  - **Gate G9-d (Rotation-Curve Kernel Unit Test Including $r' = 0$ Branch, `B1` & `Review V2 Minor`):** Verify that the coded piecewise 1D radial enclosed-mass kernel $\mathcal{F}_\sigma(r, r')$ (with coefficient $\frac{1}{\sqrt{2\pi}}$ for $r'/\sigma_{\rm ref} \ge 10^{-4}$ and the analytical point-mass limit for $r'/\sigma_{\rm ref} < 10^{-4}$, implemented in `verify_b1_kernel_mc.py`) agrees with `scipy.stats.ncx2.cdf((r/sigma)**2, df=3, nc=(rp/sigma)**2)` to absolute tolerance $< 10^{-10}$ across the $5\times 7$ grid $(r/\sigma_{\rm ref}) \in \{0.2, 0.5, 1.0, 2.0, 4.0\} \times (r'/\sigma_{\rm ref}) \in \{0.0, 10^{-5}, 0.2, 0.5, 1.0, 2.0, 4.0\}$.

---

# 3. Model-Level Decision Rule, Operational Holm–Bonferroni Control, and Exhaustive Verdict Map (Findings M10, N5, N6, N9)

## 3.1 Classification of Tests (Single Deciding Version Per Test)
1. **Four Primary Pillar Tests (Decide the Overall Model-Level Verdict):**
   - **Pillar 1 (`T1-L1`):** Direct fit of the derived 1-parameter strand-unwinding dark-energy curve $w(a) = -1 + \gamma_u/E(a)$. *(Pre-test forecast: `INCONCLUSIVE` or `FAIL`, most likely joint `INCONCLUSIVE`.)*
   - **Pillar 2 (`T2-A`):** Test of the $1:6:12$ strand budget share and transit leak ($\Omega_b = 1/19$, $\mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak}) = 19\Omega_{bc} - 1$ vs. Planck $\omega_c/\omega_b$, using DESI/LUNA BBN and uncorrelated $\sigma_{\rm comb}$). *(Pre-test forecast: `FAIL` at $3.8\text{–}3.9\sigma$.)*
   - **Pillar 3 (`T4b`):** Out-of-sample hard-step subcluster accuracy of the universal shadow crossing delay $\tau_{\rm lag} \in [235, 1500]\text{ Myr}$ on the test half of the 16 dissociative galaxy cluster mergers. *(No clean pre-test forecast because of literature age and core-classification uncertainties.)*
   - **Pillar 4 (`T5-A`):** Out-of-sample test of the universal constant 3D Gaussian refraction kernel width $\sigma_{\rm ref}$ (in kpc) on the held-out half of SPARC galaxy rotation curves. *(Pre-test forecast: `FAIL` or `INCONCLUSIVE` due to the $1 + \mathcal{R} \approx 6.0$ saturation cap.)*
2. **Scored Secondary & Direct-Tension Tests (Reported in Full; Cannot Rescue Any Pillar `FAIL`):**
   - **`T1-Sign`:** One-sided 95% CPL check $P(w_0 > -1 \mid \text{data}) \ge 0.95$ (already known before registration to `PASS`).
   - **`T2-N1`:** Direct parameter-free test of $\Omega_b^{\rm model} = 1/19 = 0.052632$ vs. Planck $\Omega_b = 0.04930 \pm 0.00086$ (already known before registration to `FAIL` at $+3.87\sigma$).
   - **`T2-N2`:** Direct parameter-free test of $H_0^{\rm pred} = 100\sqrt{19\omega_b} = 65.19 \pm 0.22\text{ km s}^{-1}\text{ Mpc}^{-1}$ (for Planck $\omega_b$) vs. Planck $\Lambda\text{CDM}$ $H_0 = 67.36 \pm 0.54\text{ km s}^{-1}\text{ Mpc}^{-1}$ (already known before registration to `FAIL` at $-3.72\sigma$).
   - **`T5-B`:** Scaled refraction width $\sigma_{\rm ref,g} = k\,R_{d,g}$ on SPARC held-out galaxies using the same `1.5 / 70%` thresholds as `T5-A`.
   - **`T5c`:** NGC 1052-DF2 enclosed dynamical mass check.
   - **`T6`:** Regional $H_0$ heterogeneity across the $N_{\rm pix}$ well-sampled HEALPix $N_{\rm side} = 1$ Galactic `RING` sky regions.
3. **Unscored Sensitivity & Exploratory Analyses (Never Enter Verdicts):**
   - **`T2-B`** (constrained fit with $\omega_b = h^2/19$ inside the likelihood), Cooke et al. (2018) BBN prior runs, $w\text{CDM}$ Table 1 CMB prior runs, `T4b` Monte Carlo age-posterior-weighted accuracy and system-level classification, `T6` Equatorial and $z_{\rm CMB}$ runs, and **`T4a` (`EXPLORATORY` regardless of $N$, age cut, or catalog)**.

## 3.2 Operational Holm–Bonferroni Procedure for Null-Rejection Discovery Tests (Resolving Finding N6)
Among the scored tests, goodness-of-fit and equivalence survival gates (`T2-A`, `T5-A`, `T5-B`, `T5c`, `T2-N1`, `T2-N2`) test whether the model is *consistent* with data (where smaller discrepancy is better, not rejection of a null hypothesis). By contrast, three scored tests claim a positive *discovery / departure from a baseline null hypothesis* (`T1-L1` vs. $\Lambda\text{CDM}$, `T4b` vs. random $50\%$ coin-flip classification, and `T6` vs. spatially uniform $H_0$). To control family-wise false-positive discoveries across these $K_{\rm disc} = 3$ null-rejection tests at $\alpha_{\rm FWE} = 0.05$, we define an exact mechanical $p$-value for each:
1. **`T1-L1` Discovery $p$-value:** $p_{\rm T1-L1} \equiv \max_{r \in \{\text{Pantheon+}, \text{DES-Dovekie}\}} \left[1 - F_{\chi^2_1}\!\left(\max\!\left(0,\; -\Delta\chi^2_{\min,r}(\text{Law 1} - \Lambda\text{CDM})\right)\right)\right]$.
2. **`T4b` Discovery $p$-value:** Exact one-sided binomial tail probability against a $50\%$ coin-flip null on the $n_{\rm test}$ classified test-half clusters ($k_{\rm obs}$ correct classifications): $p_{\rm T4b} \equiv \sum_{k = k_{\rm obs}}^{n_{\rm test}} \binom{n_{\rm test}}{k} 0.5^{n_{\rm test}}$.
3. **`T6` Discovery $p$-value:** Exact chi-squared survival probability on the $N_{\rm pix}$ well-sampled Galactic regions: $p_{\rm T6} \equiv p_{\rm het} = 1 - F_{\chi^2_{N_{\rm pix}-1}}\!\left(\chi^2_{\rm het}\right)$.

**Mechanical Holm–Bonferroni Step-Down Rule (`N6`):**  
Sort $(p_{\rm T1-L1}, p_{\rm T4b}, p_{\rm T6})$ in ascending order $p_{(1)} \le p_{(2)} \le p_{(3)}$, with corresponding thresholds $\alpha_{(1)} = \frac{0.05}{3} = 0.01667$, $\alpha_{(2)} = \frac{0.05}{2} = 0.0250$, and $\alpha_{(3)} = 0.050$. Let $m^*$ be the smallest index $m \in \{1, 2, 3\}$ for which $p_{(m)} > \alpha_{(m)}$. If such an $m^*$ exists, **every discovery test with rank $m \ge m^*$ that met its raw `PASS` criterion is mechanically downgraded to `INCONCLUSIVE (Failed Holm–Bonferroni Control)`**.

## 3.3 Exhaustive Three-Way Model-Level Verdict Map (Resolving Finding N6)
Across the four primary pillar tests (`T1-L1`, `T2-A`, `T4b`, `T5-A`), every possible combination of individual verdicts maps to **one and only one** model-level verdict:
1. **`MODEL FALSIFIED (FAIL)`:** At least one of the four primary pillar tests (`T1-L1`, `T2-A`, `T4b`, or `T5-A`) ends in `FAIL`.
2. **`MODEL SUPPORTED (PASS)`:** All four primary pillar tests (`T1-L1`, `T2-A`, `T4b`, and `T5-A`) end in `PASS` (after applying the Section 3.2 Holm–Bonferroni rule).
3. **`MODEL INCONCLUSIVE (NOT FALSIFIED, NOT SUPPORTED)`:** Zero primary pillar tests end in `FAIL`, and at least one primary pillar test ends in `INCONCLUSIVE`.

---

# 4. Global Numerical, Optimizer, Random Seed, and Hardware Settings

- **Master Random Seed:** `SEED = 20261030` (used for all MCMC walker initializations and Monte Carlo uncertainty propagations).
- **MCMC Sampler (`emcee`) & $\chi^2_{\min}$ Optimizer (`N5`):** Ensemble sampler with $N_{\rm walkers} = 32$, burn-in discarded after $5\tau_{\rm autocorr}$ (minimum 1,000 steps per walker), production chain length sufficient to achieve Gelman–Rubin $R - 1 < 0.01$ and $\text{ESS} > 1000$ per parameter (minimum 4,000 production steps per walker = 128,000 samples). For every $\Delta\chi^2_{\min}$ comparison (`T1-L1` and `T2-B`), $\chi^2_{\min}$ is computed by running `scipy.optimize.minimize(..., method='Nelder-Mead', options={'xatol': 1e-6, 'fatol': 1e-6, 'maxiter': 10000})` initialized from the 5 highest-likelihood MCMC samples, followed by bounded `L-BFGS-B` polishing (`ftol=1e-12`).
- **Hardware & Thread Cap:** All Python scripts set `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1` before importing numerical libraries, cap multiprocessing pools at `N_CORES = 12`, and set worker priority to `psutil.BELOW_NORMAL_PRIORITY_CLASS`.

---

# 5. Pre-Registered Test Specifications, Single Deciding Rules, Forecasts, and Sensitivity Analyses

## 5.1 Test T1: Dark Energy Unwinding (`T1-L1` Primary Pillar 1, `T1-Sign` Secondary; Prediction P1)

### Shared Single Deciding Datasets and Likelihood Construction (`M7`, `M8`)
- **DESI DR2 BAO + Joint Ly$\alpha$ BAO+AP (`M7`):** Load `CobayaSampler/bao_data/desi_bao_dr2` for all $z_{\rm eff} < 2.3$ tracers (BGS, LRG1, LRG2, LRG3+ELG1, ELG2, QSO), **remove** the $z_{\rm eff} = 2.33$ Ly$\alpha$ row from `desi_bao_dr2`, and replace it with the joint Ly$\alpha$ BAO + full-shape Alcock–Paczyński constraint of Cuceu et al. (2025, arXiv:2607.27410):
  $$D_H(2.33)/r_d = 8.600 \pm 0.066, \qquad D_M(2.33)/r_d = 39.32 \pm 0.33, \qquad r_{D_H, D_M} = -0.43.$$
- **Single Deciding Planck 2018 Compressed CMB Distance Prior (`M8`):** Chen, Huang & Wang (2019), JCAP 02 (2019) 028, Table 1 $\Lambda\text{CDM}$ column (`Planck 2018 TT,TE,EE+lowE`):
  $$\boldsymbol{\mu}_{\rm CMB}^{\Lambda{\rm CDM}} = \begin{pmatrix} R \\ \ell_A \\ 100\omega_b \end{pmatrix} = \begin{pmatrix} 1.7502 \\ 301.471 \\ 2.236 \end{pmatrix}, \qquad \boldsymbol{\sigma}_{\rm CMB}^{\Lambda{\rm CDM}} = \begin{pmatrix} 0.0046 \\ 0.090 \\ 0.015 \end{pmatrix}, \qquad \mathbf{R}_{\rm CMB}^{\Lambda{\rm CDM}} = \begin{pmatrix} 1.00 & 0.46 & -0.66 \\ 0.46 & 1.00 & -0.33 \\ -0.66 & -0.33 & 1.00 \end{pmatrix}.$$
  *(Sensitivity Analysis: The $w\text{CDM}$ Table 1 column $(1.7493, 301.462, 2.239)^T$ is evaluated and reported as a non-deciding sensitivity check.)*
- **Supernova Runs (Separate per G6):**
  1. **Run 1 (`Pantheon+`):** Pantheon+ supernovae ($z_{\rm HD} > 0.01$, `IS_CALIBRATOR == 0`, full `STAT+SYS` covariance, analytically marginalized over $\mathcal{M}$).
  2. **Run 2 (`DES-Dovekie`):** DES SN 5-year recalibrated compilation (`DES-Dovekie`, `4_DISTANCES_COVMAT`, full `STAT+SYS` covariance, analytically marginalized over $\mathcal{M}$).

### Primary Pillar 1 (`T1-L1`): Direct Test of the Derived Unwinding Curve $w(a) = -1 + \gamma_u/E(a)$ (Resolving B4 & N5)
- **Model Equations & How the Model's Own $w_0$ Is Set (`MULTIVERSE_STAGE1_EQUATIONS.md` §5, Law 1 / d4, `N5`):**  
  Fit the 1-parameter uncoupled unwinding dark-energy law directly:
  $$w(a) = -1 + \frac{\gamma_u}{E(a)}, \qquad g(a) = \exp\!\left[3\gamma_u\int_a^1 \frac{da'}{a'\,E(a')}\right], \qquad \gamma_u \equiv \frac{n\Gamma_u}{3H_0} \ge 0,$$
  where $g(a)$ is integrated via 4th-order Runge–Kutta on a 1,000-point log-$a$ grid from $\frac{d\ln g}{d\ln a} = -3\frac{\gamma_u}{E(a)}$ with $g(1) = 1$. When `T1-L1` is fitted to the data, $\gamma_u \in [0.0, 2.0]$ is a free parameter fitted jointly with $\Omega_m \in [0.1, 0.6]$, $h \in [0.5, 0.9]$, and $100\omega_b \in [1.8, 2.6]$ ($\sum m_\nu = 0.06\text{ eV}$), so **the model's own present-day equation of state is set by the fitted parameter $\hat{\gamma}_u$ as $w_0^{\rm fit} = -1 + \hat{\gamma}_u \ge -1$**, with implied tangent $w_a^{\rm fit} = -\frac{3}{2}\hat{\gamma}_u[\hat{\Omega}_m + \hat{\gamma}_u(1 - \hat{\Omega}_m)] \le 0$.
- **Exhaustive Per-Run and Joint Decision Rules for `T1-L1` (Resolving Finding N5a & N5d):**  
  For each supernova run $r \in \{\text{Pantheon+}, \text{DES-Dovekie}\}$, compute $A_r \equiv \Delta\chi^2_{\min,r}(\text{Law 1} - \Lambda\text{CDM})$ and $B_r \equiv \Delta\chi^2_{\min,r}(\text{Law 1} - w_0w_a\text{CDM})$ (where unconstrained $w_0w_a\text{CDM}$ has priors $w_0 \in [-3.0, 1.0], w_a \in [-3.0, 2.0], w_0 + w_a < 0$). Each run $r$ is assigned a per-run outcome in strict priority order:
  1. **Per-Run `FAIL` (evaluated first; takes precedence):** $B_r > +9.0$ **or** $A_r > -1.0$.
  2. **Per-Run `PASS`:** Not per-run `FAIL`, **and** $A_r \le -4.0$ **and** $B_r \le +4.0$.
  3. **Per-Run `INCONCLUSIVE`:** Every other converged per-run outcome (specifically: $(A_r \in (-4.0, -1.0] \text{ and } B_r \le +9.0)$ **or** $(A_r \le -4.0 \text{ and } B_r \in (+4.0, +9.0])$).
  **Joint `T1-L1` Verdict Across the Two Supernova Runs:**
  - **Joint `PASS`:** Both `Pantheon+` and `DES-Dovekie` are per-run `PASS` (and $p_{\rm T1-L1}$ survives Section 3.2 Holm–Bonferroni control).
  - **Joint `FAIL`:** Both `Pantheon+` and `DES-Dovekie` are per-run `FAIL`.
  - **Joint `INCONCLUSIVE`:** Any other combination of converged per-run outcomes (i.e., at least one run is per-run `INCONCLUSIVE`, or one run is `PASS` and the other is `FAIL`).
- **Pre-Test Forecast for `T1-L1` (Corrected per Finding N5b & N5c):**  
  In published DESI DR2 + CMB + SNe fits (DESI Collaboration 2025b, arXiv:2503.14738, Table V; Popovic et al. 2025, arXiv:2511.07517v2, Tables 10–11), unconstrained $w_0w_a\text{CDM}$ yields $w_0 = -0.838 \pm 0.055, w_a = -0.62^{+0.22}_{-0.19}$ ($\Delta\chi^2(w_0w_a - \Lambda\text{CDM}) = -10.7$) for `Pantheon+`, and $w_0 = -0.803 \pm 0.054, w_a = -0.72 \pm 0.21$ ($\Delta\chi^2(w_0w_a - \Lambda\text{CDM}) = -13.5$) for `DES-Dovekie` (while $w_a = -0.86 \pm 0.25$ was the original pre-Dovekie DESY5 value). Projecting those $(w_0, w_a)$ posteriors onto the shallow Law 1 curve pulls the Law 1 best fit to $w_0^{\rm fit} \approx -0.90\text{ to }-0.93$ ($w_a^{\rm fit} \approx -0.04\text{ to }-0.06$; whereas evaluated at DESI's CPL $w_0 = -0.84$, Law 1 gives $w_a = -0.102$), yielding a forecast penalty $B_{\rm Pantheon+} \approx 7\text{–}8$ (inside the $(4.0, 9.0]$ per-run `INCONCLUSIVE` band) and $B_{\rm Dovekie} \approx 9\text{–}10$ (near the `FAIL` / `INCONCLUSIVE` boundary). **Therefore, `T1-L1` is forecast to end in `INCONCLUSIVE` or `FAIL` (most likely joint `INCONCLUSIVE`).**

### Secondary Check `T1-Sign`: Unconstrained CPL $w_0 > -1$ Check (`B4`, `N5b`)
- **Sampled Parameters & Uniform Priors (`m8`):** Flat $w_0w_a\text{CDM}$ with $\Omega_m \in [0.1, 0.6]$, $h \in [0.5, 0.9]$, $100\omega_b \in [1.8, 2.6]$, $w_0 \in [-3.0, 1.0]$, $w_a \in [-3.0, 2.0]$, $w_0 + w_a < 0$.
- **Exhaustive Thresholds:**
  - **PASS:** In both supernova runs, $P(w_0 > -1 \mid \text{data}) \ge 0.95$ (one-sided Gaussian $z \ge 1.645$) and not `FAIL`.
  - **FAIL:** In either run, $P(w_0 < -1 \mid \text{data}) \ge 0.95$; **or**, in any release where $\sigma_{w_0} \le 0.03$, $(w_0, w_a) = (-1, 0)$ lies inside the $68\%$ credible region in both runs.
  - **INCONCLUSIVE:** Anything else.
- **Pre-Test Note (`N5b`):** Published posteriors give $w_0 = -0.838 \pm 0.055$ (`Pantheon+`, $z = +2.95\sigma$) and $w_0 = -0.803 \pm 0.054$ (`DES-Dovekie`, $z = +3.65\sigma$), so **`T1-Sign` is already known before registration to PASS** and cannot rescue `T1-L1`.

---

## 5.2 Test T2: The Leak and the Dark-to-Ordinary Ratio (`T2-A` Single Deciding Pillar 2; Resolving M1, M2, M9, N1, N7, N9)

### Algebraic Identity Statement (`M1`)
In `MULTIVERSE_STAGE1_EQUATIONS.md` §4 (c3)–(c4), $\Omega_b = 1/19$, $\Omega_{\rm dm} = \frac{6}{19}(1 - f_{\rm leak})$, and $\Omega_{bc} \equiv \Omega_b + \Omega_{\rm dm} = \Omega_{m,{\rm tot}} - \Omega_{\nu,0} = \frac{7 - 6f_{\rm leak}}{19}$:
$$f_{\rm leak} = 1 - \frac{19\,\Omega_{bc} - 1}{6}, \qquad \sigma_f = \frac{19}{6}\,\sigma_{\Omega_{bc}}, \qquad \mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak}) = 19\,\Omega_{bc} - 1, \qquad \sigma_{\mathcal{R}_{\rm pred}} = 19\,\sigma_{\Omega_{bc}}.$$
Because $\Omega_{bc} = \Omega_b(1 + \mathcal{R}_{\rm true})$, $\mathcal{R}_{\rm pred} = \mathcal{R}_{\rm true} \iff \Omega_b = 1/19$: **$f_{\rm leak}$ cancels out of $\mathcal{R}_{\rm pred}$, making T2 algebraically a test of $\Omega_b = 1/19$.** If any fit yields $\Omega_{bc} > 7/19$ ($f_{\rm leak} < 0$), the raw negative value is reported without clipping (`m12`).

### Primary Pillar 2 (`T2-A`): Single Registered Deciding Version of Test T2 (Resolving N1 & N7)
- **Why `T2-A` with DESI/LUNA BBN and Uncorrelated $\sigma_{\rm comb}$ Is Chosen (`N1`, `N7`):**  
  `T2-A` implements the pre-registered expansion-history extraction of $\Omega_{bc}$ in flat $w_0w_a\text{CDM}$. Under the conditional CMB likelihood $(R, \ell_A \mid \omega_b)$, the older Cooke et al. (2018) prior ($100\omega_b = 2.166 \pm 0.019$) sits $3.6\sigma$ below Planck's $100\omega_b = 2.236 \pm 0.015$ and shifts the conditional $R$ mean by $+0.014$ ($+3.1\sigma_R$), biasing $\Omega_{bc}$ and $f_{\rm leak}$ (`N7`). Therefore, the **DESI DR2 / post-LUNA BBN prior ($100\omega_b = 2.218 \pm 0.055$, Schöneberg 2024; DESI Collaboration 2025b, Eq. 14) is the single registered deciding BBN prior**, and the **uncorrelated error formula $\sigma_{\rm comb} = \sqrt{(19\sigma_{\Omega_{bc}})^2 + \sigma_{\rm Planck}^2}$ ($\sigma_{\rm Planck} = 0.065$) is the single registered deciding error formula** (since computing an exact cross-covariance with $\omega_c/\omega_b$ would require loading Planck test chains).
- **Single Deciding Fixing Dataset (`FIX`):** Flat $w_0w_a\text{CDM}$ fit ($\Omega_m \in [0.1, 0.6], h \in [0.5, 0.9], 100\omega_b \in [1.8, 2.6], w_0 \in [-3.0, 1.0], w_a \in [-3.0, 2.0], w_0 + w_a < 0$, $\sum m_\nu = 0.06\text{ eV}$) to:
  1. DESI DR2 BAO with the joint Ly$\alpha$ BAO+AP vector at $z_{\rm eff} = 2.33$ (`M7`);
  2. The **exact conditional Gaussian likelihood $(R, \ell_A \mid 100\omega_b)$** from Chen, Huang & Wang (2019)'s $3\times 3$ Planck 2018 $\Lambda\text{CDM}$ Table 1 covariance matrix (`M9`):
     $$\boldsymbol{\mu}_{R,\ell_A \mid \omega_b}(\omega_b) = \begin{pmatrix} 1.7502 \\ 301.471 \end{pmatrix} + \mathbf{C}_{12}\,C_{22}^{-1}\left(100\omega_b - 2.236\right), \qquad \mathbf{C}_{R,\ell_A \mid \omega_b} = \mathbf{C}_{11} - \mathbf{C}_{12}\,C_{22}^{-1}\mathbf{C}_{21},$$
     where $\mathbf{C}_{11}$ is the $2\times 2$ $(R, \ell_A)$ block, $\mathbf{C}_{12} = (-0.66(0.0046)(0.015),\; -0.33(0.090)(0.015))^T$, and $C_{22} = 0.015^2$;
  3. The single deciding **DESI DR2 / post-LUNA BBN prior**: $100\omega_b = 2.218 \pm 0.055$;
  4. Supernovae run separately: **Run T2-A-Pantheon+** and **Run T2-A-DES-Dovekie**.
  From the MCMC posterior of $\Omega_{bc} \equiv \Omega_{m,{\rm tot}} - \Omega_{\nu,0}$ in each run, extract the median $\Omega_{bc}$ and $68\%$ half-width $\sigma_{\Omega_{bc}} = \frac{1}{2}(\Omega_{bc,84} - \Omega_{bc,16})$, and freeze $f_{\rm leak}$, $\sigma_f$, and $\mathcal{R}_{\rm pred} = 19\Omega_{bc} - 1$ in `results/FREEZE_T2.json`.
  - **Single Frozen $f_{\rm leak}$ Passed to Test T5 (`N1`):** Test T5 (`T5-A`, `T5-B`, `T5c`) uses the single $f_{\rm leak}$ frozen from **Run `T2-A-Pantheon+` (with the DESI DR2 / post-LUNA BBN prior)**.
- **Single Deciding Testing Dataset (`TEST`):** Planck 2018 base $\Lambda\text{CDM}$ `TT,TE,EE+lowE+lensing` (Planck Collaboration 2020, Table 2): $\mathcal{R}_{\rm Planck} = 5.36 \pm 0.065$, combined via $\sigma_{\rm comb} = \sqrt{(19\sigma_{\Omega_{bc}})^2 + 0.065^2}$.
- **Exhaustive Deciding Thresholds for `T2-A` (Original v1 "Either Run" FAIL Rule Restored per N1 & N3):**
  - **PASS:** $\left|\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm Planck}\right| \le 2\,\sigma_{\rm comb}$ in **both** `T2-A-Pantheon+` and `T2-A-DES-Dovekie`.
  - **FAIL:** $\left|\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm Planck}\right| > 2\,\sigma_{\rm comb}$ in **either** `T2-A-Pantheon+` **or** `T2-A-DES-Dovekie`.
  - **INCONCLUSIVE:** Only if validation (`G9`) or MCMC convergence fails.
- **Pre-Test Forecast for `T2-A` (Corrected per Review V2 Minor):** **Forecast to FAIL at $\sim 3.8\sigma$ (`Pantheon+`, $\mathcal{R}_{\rm pred} \approx 4.89$) and $\sim 3.9\sigma$ (`DES-Dovekie`, $\mathcal{R}_{\rm pred} \approx 4.92$).**

### Direct Parameter-Free Secondary Tests `T2-N1` and `T2-N2` (Resolving M2 & N9)
- **Test `T2-N1` (Direct Baryon Share Check):** Single deciding comparison of $\Omega_b^{\rm model} = 1/19 = 0.052632$ against Planck 2018 $\Omega_b = 0.04930 \pm 0.00086$:
  - **PASS:** $|\Omega_b^{\rm model} - 0.04930| \le 2(0.00086)$. **FAIL:** $|\Omega_b^{\rm model} - 0.04930| > 2(0.00086)$. *(Pre-test value: $+3.87\sigma \implies$ **FAIL**.)*
- **Test `T2-N2` (Implied Hubble Constant Check, Single Deciding Pair per N9):** Single deciding comparison of $H_0^{\rm pred} = 100\sqrt{19\omega_b} = 65.19 \pm 0.22\text{ km s}^{-1}\text{ Mpc}^{-1}$ (computed from Planck 2018 $100\omega_b = 2.237 \pm 0.015$) against Planck 2018 $\Lambda\text{CDM}$ $H_0 = 67.36 \pm 0.54\text{ km s}^{-1}\text{ Mpc}^{-1}$, with $\sigma_{\rm comb,H_0} = \sqrt{0.22^2 + 0.54^2} = 0.583\text{ km s}^{-1}\text{ Mpc}^{-1}$:
  - **PASS:** $|H_0^{\rm pred} - 67.36| \le 2\sigma_{\rm comb,H_0}$. **FAIL:** $|H_0^{\rm pred} - 67.36| > 2\sigma_{\rm comb,H_0}$. *(Pre-test value: $-3.72\sigma \implies$ **FAIL**.)*
  - *(Non-Deciding Sensitivity Comparisons for `T2-N2`: Using DESI/LUNA BBN $100\omega_b = 2.218 \pm 0.055$ gives $H_0^{\rm pred} = 64.92 \pm 0.81$, which is $2.51\sigma$ below Planck $H_0$; using Cooke+18 BBN $100\omega_b = 2.166 \pm 0.019$ gives $H_0^{\rm pred} = 64.15 \pm 0.28$, which is $5.29\sigma$ below Planck $H_0$ and $6.84\sigma$ below DESI+BBN $H_0 = 68.52 \pm 0.62$, where DESI+BBN shares the BBN prior.)*

### Non-Deciding Sensitivity Analyses for Test T2 (`N1`)
1. **Sensitivity Test `T2-B` (Self-Consistent Constrained Fit):** Fit the `T2-A` datasets while imposing $\omega_b = h^2/19$ and $\Omega_{bc} = \frac{7 - 6f_{\rm leak}}{19}$ inside the likelihood. Complete outcome rule for `T2-B`: **PASS** if in both SN runs $|\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm Planck}| \le 2\sigma_{\rm comb}$ **and** $\Delta\chi^2_{\min}(\text{T2-B} - w_0w_a\text{CDM}) \le +9.0$; **FAIL** if in either SN run $|\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm Planck}| > 2\sigma_{\rm comb}$ **or** $\Delta\chi^2_{\min}(\text{T2-B} - w_0w_a\text{CDM}) > +9.0$. (`T2-B` is reported in full but cannot alter the `T2-A` pillar verdict.)
2. **Cooke et al. (2018) BBN Prior & Marginal $(R, \ell_A)$ Block:** Re-running `T2-A` with $100\omega_b = 2.166 \pm 0.019$ and/or the marginal $2\times 2$ $(R, \ell_A)$ block is reported as a sensitivity analysis only.

---

## 5.3 Test T3: No Direct Detection (Prediction P2)
- Tracked externally by Gregory from LUX-ZEPLIN (LZ) and other direct-detection experiments; no computation in this package.

---

## 5.4 Test T4a: Offset Sign in Young Mergers (Unconditionally `EXPLORATORY`, Resolving B2 & B3)

- **Unconditional Exploratory Lock (`B3`):** **Test T4a is unscored (`EXPLORATORY`) in v1 regardless of sample size $N$, age cut ($150\text{ Myr}$, $235\text{ Myr}$, or $400\text{ Myr}$), or catalog; any scored version of T4a requires a new pre-registration in v2.**
- **Why T4a Is Unscored in v1 (`B3`):** (1) Under the energy-conserving symmetric harmonic core-passage trajectory `A13b` ($x_S(t) = \frac{v_p}{\omega_0}\sin(\omega_0 t)$), the exact offset $\Delta\tilde{x}_S^{\rm (A13b)}(T; \tau_{\rm lag}) = \frac{v_p}{\omega_0}[\sin(\omega_0(T-\tau_{\rm lag})) + \omega_0\tau_{\rm lag}\cos(\omega_0(T-\tau_{\rm lag})) - \sin(\omega_0 T)]$ is negative (shadow trailing behind the stars) for $0 < T \lesssim \frac{2}{3}\tau_{\rm lag}$ and positive only for $\frac{2}{3}\tau_{\rm lag} \lesssim T \le \tau_{\rm lag}$, so the model does not predict a uniform positive sign across all young mergers; and (2) under the original $150\text{ Myr}$ cut with the Bullet Cluster excluded per Rule G2, only $N = 1$ system (`Abell 2744`) remains.
- **Single Exploratory Recipe:** Excluding `1E 0657-558`, compute the inverse-variance-weighted mean of $\Delta_{SI}^{\parallel} \equiv (\mathbf{x}_I - \mathbf{x}_S)\cdot\hat{\mathbf{s}}_{G\to S} = \delta_{SI} = \delta_{SG}\beta = -|\delta_{SG}|\beta$ for non-Bullet systems with $t_p \le 235\text{ Myr}$ (and $t_p \le 400\text{ Myr}$) using **Wittman, Golovich & Dawson (2018, ApJ 869, 104, Table 1)** as the primary catalog (and Harvey et al. 2015, Table S1 as a sensitivity comparison).

---

## 5.5 Test T4b: The Age Cutoff ($\tau_{\rm lag}$, Primary Pillar 3; Resolving M6, N2, N8, N10)

- **Known Sample-Selection Limitation (Resolving Finding M6a & N10):**  
  *Plain Statement:* The 16 dissociative merging clusters in the table below were compiled from the literature (Golovich et al. 2019b; Harvey et al. 2015; Wittman et al. 2018; Dawson 2013) by an author who had prior knowledge of published lensing-vs.-gas offsets in well-known systems such as the Bullet Cluster, El Gordo, and the Sausage Cluster. Because no blinded, flux-limited, all-sky catalog of dissociative mergers with uniform MCMAC dynamical ages exists, T4b cannot be completely free of literature selection bias; this limitation is stated plainly here and in the final report.
- **Deterministic Byte-Wise ASCII Sort Rule (`M6`):**  
  The 16 clusters are ordered by **Python byte-wise ASCII `sorted()` on the exact `Catalog Designation` string** (`'1E 0657-558'` sits naturally at position 1 with zero manual swapping). Odd positions ($1, 3, \dots, 15$) form the **Training Half (8 clusters)** and even positions ($2, 4, \dots, 16$) form the **Test Half (8 clusters)**.
- **Single Deciding Choices for All Four T4b Forks (Resolving Findings N2 & N8):**
  1. **Single Bullet Cluster Age (`N2b`, `N8`):** We use the **Dawson (2013, ApJ 772, 131, Table 2) temporal-prior median $t_p = 0.40\text{ Gyr}$** ($\sigma_{t_p} = 0.10\text{ Gyr}$; 68% interval $0.30\text{–}0.50\text{ Gyr}$; 95% interval $0.20\text{–}0.60\text{ Gyr}$) as the **single deciding age** for `1E 0657-558`. The Markevitch et al. (2002) $0.15\text{ Gyr}$ bow-shock estimate is dropped from the decision path because shock propagation speed overstates the subcluster speed (Springel & Farrar 2007; Dawson 2013 §3.2.2).
  2. **Single $\tau_{\rm lag}$ Grid Floor (`N2a`, `N8`):** Because Dawson (2013)'s Bullet Cluster age is a probability distribution rather than a hard floor, we register the **one-sided 95% lower confidence bound of Dawson's temporal-prior distribution, $\tau_{\rm lag,\min} = 0.40 - 1.645(0.10) = 0.235\text{ Gyr} = 235\text{ Myr}$, as the single deciding grid floor**. The training search evaluates $\tau_{\rm lag}$ on the uniform grid $[235, 1500]\text{ Myr}$ in steps of $5\text{ Myr}$ (ties go to the smallest $\tau_{\rm lag}$).
  3. **Single Deciding Accuracy Metric (`N2c`):** **Hard-step classification accuracy** (comparing each classified cluster's point estimate $t_{p,i}$ in the table below against the step $\tau_{\rm lag}$: `dark mass with galaxies` for $t_{p,i} < \tau_{\rm lag}$, `dark mass with gas` for $t_{p,i} \ge \tau_{\rm lag}$) is the **single deciding accuracy metric** compared against the $80\%$ and $60\%$ thresholds. *(Monte Carlo age-posterior-weighted accuracy is a non-deciding Sensitivity Analysis only.)*
  4. **Single Deciding Classification Level (`N2d`):** **Subcluster-level classification of the primary high-Mach ("bullet") subcluster** (where ram-pressure stripping of gas from stars is maximal) using the single listed **Primary $(S, G, I)$ Position Source** in the table below is the **single deciding classification** for each of the 16 clusters. *(System-level classification and secondary position sources are non-deciding Sensitivity Analyses only.)*

| # | Catalog Designation | Common Name | Split Half | Deciding $t_p$ (Gyr) | $\sigma_{t_p}$ (Gyr) | Dynamical Age Source | Single Deciding $(S, G, I)$ Position Source |
|---|---|---|---|---|---|---|---|
| 1 | `1E 0657-558` | Bullet Cluster | **Training (Odd)** | `0.40` | `0.10` | Dawson 2013 (ApJ 772, 131, Table 2, temporal prior) | Clowe et al. 2006 (ApJ 648, L109) |
| 2 | `ACT-CL J0102-4915` | El Gordo | **Test (Even)** | `0.75` | `0.15` | Ng et al. 2015 (MNRAS 453, 1531) | Jee et al. 2014 (ApJ 785, 20, Table 1, SE peak) |
| 3 | `Abell 1240` | Abell 1240 | **Training (Odd)** | `0.45` | `0.15` | Cho et al. 2022 (ApJ 925, 68) | Cho et al. 2022 (ApJ 925, 68, Table 2, S subcluster) |
| 4 | `Abell 1758N` | Abell 1758N | **Test (Even)** | `0.40` | `0.15` | Monteiro-Oliveira et al. 2017a (MNRAS 466, 2614) | Ragozzine et al. 2012 (ApJ 744, 94, NW subcluster) |
| 5 | `Abell 2034` | Abell 2034 | **Training (Odd)** | `0.30` | `0.10` | Monteiro-Oliveira et al. 2018 (MNRAS 481, 1097) | Monteiro-Oliveira et al. 2018 (MNRAS 481, 1097, N subcluster) |
| 6 | `Abell 2146` | Abell 2146 | **Test (Even)** | `0.25` | `0.08` | Russell et al. 2010; White et al. 2015 | Coleman et al. 2017 (MNRAS 464, 2469, NW bullet subcluster) |
| 7 | `Abell 2744` | Pandora's Cluster | **Training (Odd)** | `0.15` | `0.05` | Merten et al. 2011 (MNRAS 417, 333) | Merten et al. 2011 (MNRAS 417, 333, Table 2, NW/Core) |
| 8 | `Abell 3376` | Abell 3376 | **Test (Even)** | `0.55` | `0.15` | Machado & Lima Neto 2013 (MNRAS 430, 3249) | Monteiro-Oliveira et al. 2017b (MNRAS 468, 4566, Table 2, E peak) |
| 9 | `Abell 520` | Train Wreck | **Training (Odd)** | `0.80` | `0.25` | Markevitch et al. 2005 (ApJ 627, 733) | Jee et al. 2014 (ApJ 783, 78, P3/SW subcluster) *[Clowe+12 sensitivity]* |
| 10 | `Abell 754` | Abell 754 | **Test (Even)** | `0.30` | `0.10` | Macario et al. 2011 (ApJ 728, 82) | Okabe & Umetsu 2008 (PASJ 60, 345, E shock peak) |
| 11 | `CIZA J2242.8+5301` | Sausage Cluster | **Training (Odd)** | `0.80` | `0.15` | Dawson et al. 2015 (ApJ 805, 143) | Jee et al. 2015 (ApJ 802, 46, Table 1, N subcluster) |
| 12 | `DLSCL J0916.2+2951` | Musket Ball | **Test (Even)** | `1.10` | `0.65` | Dawson 2013 (ApJ 772, 131, Table 2) | Dawson et al. 2012 (ApJL 747, L42, Table 1, S subcluster) |
| 13 | `MACS J0025.4-1222` | Baby Bullet | **Training (Odd)** | `0.50` | `0.20` | Bradač et al. 2008 (ApJ 687, 959) | Bradač et al. 2008 (ApJ 687, 959, SE subcluster) |
| 14 | `MACS J1149.5+2223` | MACS J1149 | **Test (Even)** | `1.16` | `0.38` | Golovich et al. 2016 (ApJ 831, 110) | Golovich et al. 2016 (ApJ 831, 110); Rau et al. 2014 |
| 15 | `RX J0603.3+4214` | Toothbrush Cluster | **Training (Odd)** | `1.50` | `0.30` | Brüggen et al. 2012; Jee et al. 2016 | Jee et al. 2016 (ApJ 817, 179, Table 2, N subcluster) |
| 16 | `ZwCl 0008.8+5215` | ZwCl 0008 | **Test (Even)** | `0.76` | `0.21` | Golovich et al. 2017 (ApJ 838, 110) | Golovich et al. 2017 (ApJ 838, 110, Table 4, E subcluster) |

- **Per-Cluster Classification Rule:** With $d_{IG} = |\mathbf{x}_I - \mathbf{x}_G|$, $d_{IS} = |\mathbf{x}_I - \mathbf{x}_S|$, and $\sigma_{\rm diff} = \sqrt{\sigma_I^2 + \sigma_G^2 + \sigma_S^2}$:
  - `"dark mass with gas"` if $d_{IS} - d_{IG} > 2\sigma_{\rm diff}$;
  - `"dark mass with galaxies"` if $d_{IG} - d_{IS} > 2\sigma_{\rm diff}$;
  - `"unclassified"` (excluded) otherwise.
- **Exhaustive Deciding Thresholds for `T4b` (Evaluated in Strict Priority Order, Resolving N2):**
  Let $n_{\rm train}$ and $n_{\rm test}$ be the number of classified clusters in the training and test halves, and let $\text{Acc}_{\rm train}(\tau_{\rm lag})$ and $\text{Acc}_{\rm test}(\hat{\tau}_{\rm lag})$ be their hard-step classification accuracies:
  1. **FAIL (evaluated first; takes precedence):**
     - (a) $\max_{\tau_{\rm lag} \in [235, 1500]\text{ Myr}} \text{Acc}_{\rm train}(\tau_{\rm lag}) < 0.80$; **or**
     - (b) $n_{\rm test} \ge 6$ **and** $\text{Acc}_{\rm test}(\hat{\tau}_{\rm lag}) < 0.60$; **or**
     - (c) On the **test half**, $n_{\rm test} \ge 6$ and every classified test system (including at least one classified test system with $t_p \ge 1.0\text{ Gyr}$, such as `DLSCL J0916.2+2951` or `MACS J1149.5+2223`) is classified as `"dark mass with galaxies"`.
  2. **PASS:** Not `FAIL`, $n_{\rm test} \ge 6$, $\text{Acc}_{\rm test}(\hat{\tau}_{\rm lag}) \ge 0.80$, **and** $p_{\rm T4b}$ survives Section 3.2 Holm–Bonferroni control.
  3. **INCONCLUSIVE:** Every other outcome (specifically: not `FAIL`, and either $n_{\rm test} < 6$, $0.60 \le \text{Acc}_{\rm test}(\hat{\tau}_{\rm lag}) < 0.80$, or $\text{Acc}_{\rm test} \ge 0.80$ but fails Holm–Bonferroni control).

---

## 5.6 Test T5: Halo Widths from the Refraction Kernel (`T5-A` Primary Pillar 4, `T5-B` & `T5c` Secondary; Resolving B1, M3, M4, M5, M15, N9, Review V2 Minor)

- **Model & Single Frozen $f_{\rm leak}$:** Each galaxy in SPARC (`MassModels_Lelli2016c.mrt` and `SPARC_Lelli2016c.mrt`, Lelli, McGaugh & Schombert 2016) is treated as isolated in its rest frame ($\tilde{\rho}_b = \rho_b$ under `[A12]` & `[A16]`), with fixed mass-to-light ratios $\Upsilon_{\rm disk} = 0.5\,M_\odot/L_\odot$ and $\Upsilon_{\rm bul} = 0.7\,M_\odot/L_\odot$, and **$f_{\rm leak}$ frozen from the single deciding `T2-A-Pantheon+` (DESI/LUNA BBN) run**. Enclosed shadow mass $M_{\rm sh}(< r)$ is computed via the piecewise 3D Gaussian error-function kernel $\mathcal{F}_\sigma(r, r')$ (verified in Gate `G9-d`, with the analytical point-mass limit used for $r'/\sigma_{\rm ref} < 10^{-4}$ to prevent $0/0$ division at $r' = 0$):
  $$\mathcal{F}_\sigma(r, r') = \begin{cases}
  \displaystyle \frac{1}{2}\left[\operatorname{erf}\!\left(\frac{r + r'}{\sqrt{2}\,\sigma_{\rm ref}}\right) + \operatorname{erf}\!\left(\frac{r - r'}{\sqrt{2}\,\sigma_{\rm ref}}\right)\right] - \frac{1}{\sqrt{2\pi}}\,\frac{\sigma_{\rm ref}}{r'}\left[\exp\!\left(-\frac{(r - r')^2}{2\sigma_{\rm ref}^2}\right) - \exp\!\left(-\frac{(r + r')^2}{2\sigma_{\rm ref}^2}\right)\right], & \dfrac{r'}{\sigma_{\rm ref}} \ge 10^{-4}, \\[14pt]
  \displaystyle \operatorname{erf}\!\left(\frac{r}{\sqrt{2}\,\sigma_{\rm ref}}\right) - \sqrt{\frac{2}{\pi}}\,\frac{r}{\sigma_{\rm ref}}\exp\!\left(-\frac{r^2}{2\sigma_{\rm ref}^2}\right), & \dfrac{r'}{\sigma_{\rm ref}} < 10^{-4}.
  \end{cases}$$
- **Exact Numerical Specification for $dM_b^{\rm mono}(r')$ and Self-Consistent $v_c(r)$ (`M4` & `Review V2 Minor`):**
  1. **Non-Negative Monotonic Baryon Shell Construction:** For each SPARC galaxy $g$ with radial grid $r_1 < r_2 < \dots < r_{N_g} \equiv r_{\max}$, compute the raw spherical baryon mass $M_b^{\rm raw}(< r_j) = \frac{r_j\,v_{{\rm bar,raw}}^2(r_j)}{G}$ where $v_{{\rm bar,raw}}^2(r_j) = v_{\rm gas}(r_j)|v_{\rm gas}(r_j)| + 0.5\,v_{\rm disk}^2(r_j) + 0.7\,v_{\rm bul}^2(r_j)$, and enforce strict radial monotonicity via $M_b^{\rm mono}(< r_j) = \max_{1 \le m \le j}\!\left(0,\; M_b^{\rm raw}(< r_m)\right)$ so every shell mass $\Delta M_{b,j} \ge 0$ is non-negative. Both the baryonic circular velocity and the shadow circular velocity are evaluated self-consistently from $M_b^{\rm mono}(< r)$:
     $$v_{\rm model}^2(r_j) = \frac{G\left[M_b^{\rm mono}(< r_j) + M_{\rm sh}(< r_j)\right]}{r_j}.$$
  2. **500-Point Quadrature Grid & Exponential Tail Continuation Beyond $r_{\max}$:** Interpolate $M_b^{\rm mono}(< r')$ onto a 400-point linear-plus-log radial grid on $[0, r_{\max}]$ via monotonic PCHIP (`scipy.interpolate.PchipInterpolator`), and continue from $r_{\max}$ to $r_{\rm upper} = r_{\max} + 5\sigma_{\rm ref}$ on a 100-point grid using an exponential disk tail $\Sigma_{\rm tail}(r') = \Sigma_b(r_{\max})\exp(-(r' - r_{\max})/R_d)$, evaluated by composite Simpson/trapezoidal quadrature.
  3. **Velocity Error Model & Global Optimizer:** Use only SPARC `errV` for $\sigma_{V,g}(r_j)$. Scan a 200-point log grid over $\sigma_{\rm ref} \in [0.1, 100.0]\text{ kpc}$ (`T5-A`) or $k \in [0.05, 50.0]$ (`T5-B`) on the 88 training galaxies, followed by `scipy.optimize.minimize_scalar(..., method='bounded', options={'xatol': 1e-5})`.
- **Sample Split & Reduced $\chi^2$ Definition (`M4`, `m9`):**
  - Order all 175 unique galaxy identifiers in `MassModels_Lelli2016c.mrt` by **Python byte-wise ASCII `sorted()` on `gal_id.strip()`** (Odd = 88 training galaxies; Even = 87 held-out test galaxies).
  - For each held-out galaxy $g$ with $N_g$ radial points (0 parameters fitted per held-out galaxy), $\chi^2_{{\rm red},g} = \frac{1}{N_g}\sum_{j=1}^{N_g} \left(\frac{V_{{\rm obs},g}(r_j) - v_{{\rm model},g}(r_j)}{\sigma_{V,g}(r_j)}\right)^2$.
- **Exhaustive Deciding Thresholds for Primary Pillar 4 (`T5-A`) and Secondary Test (`T5-B`) (`N9`):**
  Both `T5-A` (sole deciding rotation-curve pillar test) and `T5-B` (secondary test, unable to rescue `T5-A`) use the exact same exhaustive 3-way partition on the 87 held-out galaxies (let $M_{\chi^2}$ be the median of $\chi^2_{{\rm red},g}$ and $F_{<2}$ be the fraction of held-out galaxies with $\chi^2_{{\rm red},g} < 2.0$):
  - **PASS:** $M_{\chi^2} \le 1.5$ **and** $F_{<2} \ge 0.70$.
  - **FAIL:** $M_{\chi^2} > 3.0$ **or** $F_{<2} < 0.40$.
  - **INCONCLUSIVE:** Every other outcome (neither `PASS` nor `FAIL`).
- **Saturation Cap Premise & Forecast for Test T5 (`M3` & `Review V2 Minor`):**  
  For any galaxy whose spherically averaged baryon density decreases outward ($d\bar{\rho}_b/dr \le 0$), Gaussian diffusion enforces $g_{\rm obs}(r)/g_{\rm bar}(r) = 1 + M_{\rm sh}(< r)/M_b^{\rm mono}(< r) \le 1 + 6(1 - f_{\rm leak})$ at every radius $r > 0$ (and for galaxies with an inner H I ring where $d\bar{\rho}_b/dr > 0$ at small $r$, the cap holds at all outer radii $r \gtrsim R_{\rm ring}$). Because SPARC dwarf and low-surface-brightness galaxies reach $g_{\rm obs}/g_{\rm bar} \sim 10\text{–}20$ below $g_{\rm bar}^{\rm cap} \approx 3.7\text{–}4.0\times 10^{-12}\text{ m s}^{-2}$, **`T5-A` and `T5-B` are forecast to end in `FAIL` or `INCONCLUSIVE`**.

### Secondary Test `T5c`: NGC 1052-DF2 Stress Check (Corrected per M15 & Review V2 Minor)
- **DF2 Parameters & Literature Citations (`M15`):** Distance $D = 20.0\text{ Mpc}$, stellar mass $M_{*,{\rm DF2}} = 2.0\times 10^8\,M_\odot$ modeled as a 3D Plummer sphere with projected half-light radius $R_e = 2.2\text{ kpc}$ (3D half-mass radius $r_{1/2} = 1.3048\,R_e = 2.87\text{ kpc}$), enclosed stellar mass $M_b(< r) = M_{*,{\rm DF2}}\frac{r^3}{(r^2 + R_e^2)^{3/2}}$.
  - **Danieli et al. (2019, ApJL 874, L12) Benchmark:** $M_{\rm dyn}(< 2.7\text{ kpc}) = (1.3 \pm 0.8)\times 10^8\,M_\odot$ at $r_{\rm eval,1} = 2.7\text{ kpc}$.
  - **van Dokkum et al. (2018, Nature 555, 629) Upper-Limit Benchmarks:** 90% confidence upper limits $M_{\rm dyn}(< 3.1\text{ kpc}) < 3.2\times 10^8\,M_\odot$ ($r_{\rm eval,2} = 3.1\text{ kpc}$) and $M_{\rm dyn}(< 7.6\text{ kpc}) < 3.4\times 10^8\,M_\odot$.
- **Frozen NGC 1052 Group Baryon Model & Exact Kernel Thresholds (`Review V2 Minor`):** Massive elliptical NGC 1052 with $M_{b,{\rm NGC1052}} = 1.0\times 10^{11}\,M_\odot$ at $d_{3\rm D} = \sqrt{3/2}(80\text{ kpc}) = 98.0\text{ kpc}$, contributing $M_{\rm sh,group}(< r_{\rm eval}) = 6(1 - f_{\rm leak}) M_{b,{\rm NGC1052}}\,\mathcal{F}_{\sigma_{\rm ref}}(r_{\rm eval}, d_{3\rm D})$ (which peaks at $4.9\times 10^6\,M_\odot$ across $\sigma_{\rm ref} \in [1, 100]\text{ kpc}$, $< 1.6\%$ of the limit). Using the `T5-A` frozen $\sigma_{\rm ref}$, let $M_{\rm pred}(< r) = M_b(< r) + M_{\rm sh,DF2}(< r) + M_{\rm sh,group}(< r)$:
  - **PASS:** $M_{\rm pred}(< 2.7\text{ kpc}) \le (1.3 + 2\times 0.8)\times 10^8 = 2.9\times 10^8\,M_\odot$ **and** $M_{\rm pred}(< 3.1\text{ kpc}) < 3.2\times 10^8\,M_\odot$ *(with the corrected kernel at $\mathcal{R} \approx 5.0$, the $3.1\text{ kpc}$ limit binds and requires $\sigma_{\rm ref} \gtrsim 2.2\text{ kpc}$, while the $2.7\text{ kpc}$ bound requires $\sigma_{\rm ref} \gtrsim 1.9\text{ kpc}$)*.
  - **FAIL:** $M_{\rm pred}(< 2.7\text{ kpc}) > (1.3 + 3\times 0.8)\times 10^8 = 3.7\times 10^8\,M_\odot$ *(which occurs for $\sigma_{\rm ref} < 1.4\text{ kpc}$)*.
  - **INCONCLUSIVE:** Every other outcome (neither `PASS` nor `FAIL`).

---

## 5.7 Secondary Test T6: The Hubble Tension as a Local Reading (Prediction P7; Resolving M14 & N9)

- **Fixing Dataset (`FIX`):** SH0ES Cepheid-calibrated supernova host sample (`IS_CALIBRATOR == 1` in `Pantheon+SH0ES.dat`, Riess et al. 2022), fitting and freezing the GLS weighted-mean Type Ia absolute magnitude $M_B^{\rm fixed}$ (and variance $\sigma_{M_B^{\rm fixed}}^2$) using the calibrator block of `Pantheon+SH0ES_STAT+SYS.cov`.
- **Single Deciding Configuration (`TEST`, Resolving Finding N9):**
  - **Coordinates & Sparse-Pixel Rule:** Partition Pantheon+ Hubble-flow supernovae (`0.023 <= z_HD <= 0.15`, `IS_CALIBRATOR == 0`) into the 12 equal-area sky regions of a HEALPix $N_{\rm side} = 1$ grid in **Galactic coordinates $(l, b)$ (`RING` ordering)**. Any pixel with $N_{\rm SN,i} < 10$ is merged into its adjacent same-longitude-quadrant higher-$|b|$ neighbor pixel before inversion, giving $N_{\rm pix} \le 12$ well-sampled regions ($\text{dof} = N_{\rm pix} - 1$).
  - **Redshift Frame & Covariance:** Use peculiar-velocity-corrected **$z_{\rm HD}$** and the **bare Pantheon+ Hubble-flow covariance block $\mathbf{C}_{\rm HF}$** (which already incorporates the peculiar-velocity covariance matrix $\mathbf{C}_{\rm pvel}$ of Carr et al. 2022 / Peterson et al. 2022) to compute $\hat{\mathbf{H}}_0$, $\mathbf{C}_{H_0}$, the GLS mean $\bar{H}_0 \equiv \frac{\mathbf{1}^T \mathbf{C}_{H_0}^{-1}\hat{\mathbf{H}}_0}{\mathbf{1}^T \mathbf{C}_{H_0}^{-1}\mathbf{1}}$ with $\sigma_{\bar{H}_0}^2 = (\mathbf{1}^T \mathbf{C}_{H_0}^{-1}\mathbf{1})^{-1} + (\frac{\ln 10}{5}\bar{H}_0)^2\sigma_{M_B^{\rm fixed}}^2$, and $p_{\rm het} = 1 - F_{\chi^2_{N_{\rm pix}-1}}(\chi^2_{\rm het})$.
  - *(Non-Deciding Sensitivity Analyses: Equatorial RA/Dec `RING` coordinates and pure CMB-frame $z_{\rm CMB}$ are evaluated and reported as sensitivity checks only.)*
- **Exhaustive Deciding Thresholds for `T6` (Gap-Free Partition per N9):**
  Let $Z_{\rm all-sky} \equiv \frac{\bar{H}_0 - 67.36}{\sqrt{\sigma_{\bar{H}_0}^2 + 0.54^2}}$ be the all-sky tension against Planck 2018 $\Lambda\text{CDM}$ ($67.36 \pm 0.54\text{ km s}^{-1}\text{ Mpc}^{-1}$):
  1. **FAIL (evaluated first):** $p_{\rm het} > 0.3173$ ($< 1\sigma$ regional heterogeneity).
  2. **PASS:** $p_{\rm het} \le 0.00270$ ($\ge 3\sigma$ regional heterogeneity), $Z_{\rm all-sky} \ge 3.0$, **and** $p_{\rm T6} = p_{\rm het}$ survives Section 3.2 Holm–Bonferroni control.
  3. **INCONCLUSIVE:** Every other outcome ($0.00270 < p_{\rm het} \le 0.3173$, or $p_{\rm het} \le 0.00270$ with $Z_{\rm all-sky} < 3.0$ or failing Holm–Bonferroni control).

---

# 6. Pre-Registered Coincidence Window Tolerances (Section 8.2 Diagnostic)

With Planck 2018 base $\Lambda\text{CDM}$ parameters ($\omega_b = 0.02237, \omega_c = 0.1200, H_0 = 67.36, \Omega_{bc} = 0.3138, \Omega_{m,{\rm tot}} = 0.3153, \Omega_\Lambda = 0.6847$), compute the cosmic time span $\Delta t_{\rm coinc}$ during which all three instantaneous shares $\Omega_b(a), \Omega_{\rm dm}(a), \Omega_{\rm de}(a)$ remain simultaneously within:
1. **Criterion H-Abs:** $\max_{i \in \{b, {\rm dm}, {\rm de}\}} |\Omega_i(a) - s_i^{\rm target}| \le 0.05$ ($\pm 5$ percentage points),
2. **Criterion H-Rel:** $\max_{i \in \{b, {\rm dm}, {\rm de}\}} |\Omega_i(a) - s_i^{\rm target}| / s_i^{\rm target} \le 0.10$ ($\pm 10\%$ fractional),
evaluated both for $f_{\rm leak} = 1/6$ ($s^{\rm target} = (1/19, 5/19, 13/19)$) and for the `T2-A-Pantheon+`-frozen $f_{\rm leak}$.
