---
title: "MULTIVERSE Master Pre-Registration Protocol (PREREG.md)"
subtitle: "Frozen Analysis Choices, Likelihood Specifications, Sample Splits, and Pass/Fail Thresholds (v1.0.1, Revised Post-Cold-Review)"
author: "Gregory Mandarano / WickedAI — Pre-Registration Compiled by Gemini 4 Argon"
date: "2026-10-30"
---

# 1. Purpose and Immutability Declaration (Rule R4 & G1–G9)

This document (`PREREG.md`) is written and SHA-256 hashed at the end of Stage 1 (`PREREG_v2.sha256`) **before any dataset is downloaded or read by analysis code**. It incorporates:
1. All General Rules (G1–G9) and Test Thresholds (T1–T6) from `MULTIVERSE_TESTS_v1.md` (Version 1.0.1, October 2026) **without softening any threshold or altering any model parameter ($\Omega_b = 1/19$, $f_{\rm leak}$, $N_s = 19$, $N_r = 133$)**.
2. All 33 revisions required by the independent cold review (`REVIEW_COLD.md`, `REVIEW_RESPONSE.md`), including explicit pre-test forecasts for tests expected to fail (`T1-L1`, `T2`, `T2-N1`, `T2-N2`, `T5-A`, `T5-B`), so that Stage 2 and Stage 3 execute deterministically with zero post-hoc tuning and zero escape hatches.

---

# 2. General Rules (G1–G9, Tightened per Review Findings B1, M8, M10)

- **G1. No tuning after seeing the test data.** No parameter, kernel shape, sample cut, error model, or criterion may change after a test dataset has been loaded; any change voids the test.
- **G2. Fix on one dataset, test on another.** A dataset used to fix a parameter is never used to test that same parameter. In T2, the Planck CMB enters the fix only through the conditional distance priors $(R, \ell_A \mid \omega_b)$ coupled to BBN $\omega_b$, and the test only through $\omega_c/\omega_b$ (with their acoustic-scale overlap correlation $\rho_{\rm overlap}$ accounted for explicitly in Section 5.2). In cluster tests, the Bullet Cluster (`1E 0657-558`) is never included in any test sample.
- **G3. Freeze before testing.** Before a test dataset is opened, write the fixed values (with uncertainties), the analysis code version (git commit hash or SHA-256 of `scripts/`), and the date to `results/FREEZE_<test>.json`, and record its SHA-256. The test run must load the frozen values directly from that file.
- **G4. Thresholds are fixed.** Three outcomes, all reported with equal prominence: `PASS`, `FAIL`, `INCONCLUSIVE`.
- **G5. Structural constants are not free.** $N_s = 19$ and $N_r = 133$ may not be varied.
- **G6. No double counting.** Pantheon+ and DES SN (`DES-Dovekie`) are never combined in one fit; every supernova test is run separately with each, and both results are reported. In DESI DR2 BAO, the $z_{\rm eff} = 2.33$ Ly$\alpha$ BAO row in `desi_bao_dr2` is replaced by the joint Ly$\alpha$ BAO+AP vector of arXiv:2607.27410 so Ly$\alpha$ BAO is never double-counted (Finding M7).
- **G7. Significance language.** "$n\sigma$" means the two-sided Gaussian-equivalent significance computed with each dataset's published likelihood and covariance (except in `T1-Sign`, where the one-sided $95\%$ posterior tail $P(w_0 > -1 \mid \text{data}) \ge 0.95$, $z \ge 1.645$, is stated explicitly).
- **G8. Strict Mechanical Trigger for `INCONCLUSIVE` (No Post-Unblinding Escape Hatch, Finding M10).** Every model and analysis choice is resolved in writing in this document before the freeze. Post-unblinding invocation of G8 to label a test `INCONCLUSIVE` is **forbidden**. A test may return `INCONCLUSIVE` **only** if one of the following four mechanical numerical conditions is triggered:
  1. MCMC convergence failure (Gelman–Rubin $R - 1 \ge 0.01$ or $\text{ESS} \le 1000$ after maximum step extension);
  2. Failure of a mandatory pre-test validation gate (`G9-a` through `G9-d` below);
  3. Fewer than the pre-registered minimum sample size ($< 6$ classified test clusters in T4b);
  4. The computed test statistic falls strictly inside the pre-registered numerical interval between the `PASS` and `FAIL` thresholds, or the two supernova compilations yield opposite `PASS`/`FAIL` outcomes under Section 3.3.
- **G9. Mandatory Pre-Test Validation Gates and Convergence Criteria (Findings B1 & M8).** Before any model test is executed, the analysis pipeline must pass all four validation gates:
  - **Gate G9-a (DESI DR2 BAO Validation):** Reproduce the published DESI DR2 BAO-only flat $\Lambda\text{CDM}$ constraint $\Omega_m = 0.2975 \pm 0.0086$ (DESI Collaboration 2025b, Table V) to within $0.3\sigma$.
  - **Gate G9-b (Compressed CMB Prior & $r_s(z_*)$ Validation):** Reproduce the Chen, Huang & Wang (2019, Table 2) flat $\Lambda\text{CDM}$ parameter posteriors ($\Omega_m, h, \omega_b$) from their Table 1 $\Lambda\text{CDM}$ $(R, \ell_A, 100\omega_b)$ prior to within $0.3\sigma$.
  - **Gate G9-c (Full DESI + CMB + SNe $w_0w_a\text{CDM}$ Validation):** Reproduce the published DESI DR2 + Planck CMB + DES-Dovekie $w_0w_a\text{CDM}$ $(w_0, w_a)$ posterior of Popovic et al. (2025) / DESI Collaboration (2025b) to within $0.3\sigma$.
  - **Gate G9-d (Rotation-Curve Kernel Unit Test, Finding B1):** Verify that the coded 1D radial enclosed-mass kernel $\mathcal{F}_\sigma(r, r')$ (with coefficient $\frac{1}{\sqrt{2\pi}}$) agrees with the exact non-central chi-squared CDF `scipy.stats.ncx2.cdf((r/sigma)**2, df=3, nc=(rp/sigma)**2)` to absolute tolerance $< 10^{-10}$ across a $5\times 5$ grid of $(r/\sigma_{\rm ref}, r'/\sigma_{\rm ref}) \in \{0.2, 0.5, 1.0, 2.0, 4.0\}^2$.

---

# 3. Model-Level Decision Rule, Multiple-Testing Control, and Symmetric Dual-Run Logic (Finding M10)

## 3.1 Primary Pillar Tests vs. Secondary / Exploratory Checks
1. **Four Primary Pillar Tests (Decide the Fate of the v1 Model):**
   - **Pillar 1 (`T1-L1`):** Direct test of the derived 1-parameter strand-unwinding dark-energy curve $w(a) = -1 + \gamma_u/E(a)$.
   - **Pillar 2 (`T2`):** Test of the $1:6:12$ strand budget share and transit leak ($\Omega_b = 1/19$, $\mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak}) = 19\Omega_{bc} - 1$ vs. Planck $\omega_c/\omega_b$, evaluated via `T2-A` and `T2-B`).
   - **Pillar 3 (`T4b`):** Out-of-sample test of the universal shadow crossing delay $\tau_{\rm lag}$ age cutoff across dissociative galaxy cluster mergers.
   - **Pillar 4 (`T5-A`):** Out-of-sample test of the universal 3D Gaussian refraction kernel width $\sigma_{\rm ref}$ (in kpc) on the held-out half of SPARC galaxy rotation curves.
2. **Secondary, Direct-Tension, and Stress Tests (Reported in Full):**
   - **`T1-Sign`:** Sign check $w_0 > -1$ in unconstrained $w_0w_a\text{CDM}$ (known before registration to pass in published DESI posteriors; cannot rescue a failure of `T1-L1`).
   - **`T2-N1` & `T2-N2`:** Direct parameter-free tests of $\Omega_b = 1/19$ against Planck $\Omega_b$ (`T2-N1`, known $+3.87\sigma$ `FAIL`) and $H_0^{\rm pred} = 100\sqrt{19\omega_b}$ against Planck and BBN+BAO $H_0$ (`T2-N2`, known $3.7\sigma$ `FAIL`).
   - **`T5-B`:** Scaled refraction width $\sigma_{\rm ref,g} = k\,R_{d,g}$ on SPARC held-out galaxies. Because two kernel width variants (`T5-A` and `T5-B`) are evaluated on the same SPARC split, `T5-A` is designated primary and `T5-B` carries a factor-of-2 Bonferroni trial penalty (requiring median $\chi^2_{\rm red} \le 1.35$ and $\ge 75\%$ of galaxies with $\chi^2_{\rm red} < 2.0$ to claim a secondary pass).
   - **`T5c`:** NGC 1052-DF2 external-shadow stress check.
   - **`T6`:** Regional $H_0$ heterogeneity across the 12 HEALPix $N_{\rm side} = 1$ sky regions.
3. **Exploratory Analysis (Unscored):**
   - **`T4a`:** Young-merger offset sign test. Moved to `EXPLORATORY` per Finding B3 because excluding the Bullet Cluster (`1E 0657-558`, which fixes the lower bound on $\tau_{\rm lag}$) leaves at most $N = 1$ cluster (`Abell 2744`) with published $t_p \le 150\text{ Myr}$, below the minimum $N_{\rm min} = 3$ required for a statistical variance estimate.

## 3.2 Overall Model-Level Decision Rule and Holm–Bonferroni Control
- **Model-Level Falsification (`FAIL`):** The pre-registered v1 Mandarano Model is **falsified overall** if **any one** of the four primary pillar tests (`T1-L1`, `T2`, `T4b`, or `T5-A`) ends in `FAIL`. *(Because `T1-L1`, `T2`, and `T5-A` are already forecast to fail on mathematical and empirical grounds documented below, the v1 model is forecast to be falsified at the model level; running the full pipeline measures the exact quantitative margin of failure on each pillar.)*
- **Model-Level Support (`PASS`) & Family-Wise Error Control:** Claiming overall support for v1 requires that **all four** primary pillar tests end in `PASS`, **and** across all $K$ scored tests (`T1-L1`, `T2`, `T4b`, `T5-A`, `T5-B`, `T5c`, `T6`), any individual test claimed as a statistically significant `PASS` must survive the **Holm–Bonferroni step-down procedure** at family-wise error rate $\alpha_{\rm FWE} = 0.05$ (where the $m$-th smallest $p$-value must satisfy $p_{(m)} \le \frac{0.05}{K - m + 1}$).

## 3.3 Symmetric Combination Rule Across Dual Supernova Runs (Finding M10)
For every test run separately with `Pantheon+` and `DES-Dovekie` (`T1-L1`, `T1-Sign`, `T2-A`, `T2-B`):
- **Joint `PASS`:** Both runs satisfy the `PASS` criterion.
- **Joint `FAIL`:** Both runs satisfy the `FAIL` criterion.
- **Joint `INCONCLUSIVE (Compilation Disagreement)`:** One run satisfies `PASS` while the other satisfies `FAIL` (or either run is `INCONCLUSIVE`). Both individual run outcomes and their difference are reported in the main summary table.

---

# 4. Global Numerical, Random Seed, and Hardware Settings

- **Master Random Seed:** `SEED = 20261030` (used for all MCMC walker initializations and Monte Carlo uncertainty propagations).
- **MCMC Sampler (`emcee`):** Ensemble sampler with $N_{\rm walkers} = 32$, burn-in discarded after $5\tau_{\rm autocorr}$ (minimum 1,000 steps per walker), production chain length sufficient to achieve Gelman–Rubin $R - 1 < 0.01$ and $\text{ESS} > 1000$ per parameter (minimum 4,000 production steps per walker = 128,000 samples).
- **Hardware & Thread Cap:** All Python scripts set `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1` before importing numerical libraries, cap multiprocessing pools at `N_CORES = 12`, and set worker priority to `psutil.BELOW_NORMAL_PRIORITY_CLASS`.

---

# 5. Pre-Registered Test Specifications, Likelihoods, Forecasts, and Thresholds

## 5.1 Test T1: Dark Energy Unwinding (`T1-L1` Primary, `T1-Sign` Secondary; Prediction P1)

### Shared Datasets and Likelihood Construction (Resolving M7 & M8)
- **DESI DR2 BAO + Joint Ly$\alpha$ BAO+AP (`M7`):** Load `CobayaSampler/bao_data/desi_bao_dr2` for all $z_{\rm eff} < 2.3$ tracers (BGS, LRG1, LRG2, LRG3+ELG1, ELG2, QSO), **remove** the $z_{\rm eff} = 2.33$ Ly$\alpha$ row from `desi_bao_dr2`, and replace it with the joint Ly$\alpha$ BAO + full-shape Alcock–Paczyński constraint of Cuceu et al. (2025, arXiv:2607.27410):
  $$D_H(2.33)/r_d = 8.600 \pm 0.066, \qquad D_M(2.33)/r_d = 39.32 \pm 0.33, \qquad r_{D_H, D_M} = -0.43,$$
  so Ly$\alpha$ BAO information is included exactly once.
- **Planck 2018 Compressed CMB Distance Prior (`M8`):** From Chen, Huang & Wang (2019), JCAP 02 (2019) 028, Table 1 (`Planck 2018 TT,TE,EE+lowE`):
  - **Baseline Prior ($\Lambda\text{CDM}$ Table 1 column):**
    $$\boldsymbol{\mu}_{\rm CMB}^{\Lambda{\rm CDM}} = \begin{pmatrix} R \\ \ell_A \\ 100\omega_b \end{pmatrix} = \begin{pmatrix} 1.7502 \\ 301.471 \\ 2.236 \end{pmatrix}, \qquad \boldsymbol{\sigma}_{\rm CMB}^{\Lambda{\rm CDM}} = \begin{pmatrix} 0.0046 \\ 0.090 \\ 0.015 \end{pmatrix}, \qquad \mathbf{R}_{\rm CMB}^{\Lambda{\rm CDM}} = \begin{pmatrix} 1.00 & 0.46 & -0.66 \\ 0.46 & 1.00 & -0.33 \\ -0.66 & -0.33 & 1.00 \end{pmatrix}.$$
  - **Cross-Check Prior ($w\text{CDM}$ Table 1 column):** $\boldsymbol{\mu}_{\rm CMB}^{w{\rm CDM}} = (1.7493, 301.462, 2.239)^T$, $\boldsymbol{\sigma}_{\rm CMB}^{w{\rm CDM}} = (0.0047, 0.089, 0.015)^T$, with Table 1 $w\text{CDM}$ correlation matrix $\mathbf{R}_{\rm CMB}^{w{\rm CDM}}$ ($r_{R,\ell_A} = 0.47, r_{R,\omega_b} = -0.66, r_{\ell_A,\omega_b} = -0.34$).
- **Supernova Runs (Separate per G6):**
  1. **Run 1 (`Pantheon+`):** Pantheon+ supernovae ($z_{\rm HD} > 0.01$, `IS_CALIBRATOR == 0`, full `STAT+SYS` covariance, analytically marginalized over absolute magnitude offset $\mathcal{M}$).
  2. **Run 2 (`DES-Dovekie`):** DES SN 5-year recalibrated compilation (`DES-Dovekie`, `4_DISTANCES_COVMAT`, full `STAT+SYS` covariance, analytically marginalized over $\mathcal{M}$).

### Primary Test `T1-L1`: Direct Test of the Derived Unwinding Curve $w(a) = -1 + \gamma_u/E(a)$ (Resolving B4)
- **Model Equations (`MULTIVERSE_STAGE1_EQUATIONS.md` §5, Law 1 / d4):**  
  Fit the 1-parameter uncoupled unwinding dark-energy law directly:
  $$w(a) = -1 + \frac{\gamma_u}{E(a)}, \qquad g(a) = \exp\!\left[3\gamma_u\int_a^1 \frac{da'}{a'\,E(a')}\right], \qquad \gamma_u \equiv \frac{n\Gamma_u}{3H_0} \ge 0,$$
  which predicts the exact $(w_0, w_a)$ locus:
  $$w_0 = -1 + \gamma_u \ge -1, \qquad w_a^{\rm pred}(\gamma_u, \Omega_m) = -\frac{3}{2}\gamma_u\left[\Omega_m + \gamma_u(1 - \Omega_m)\right] \le 0.$$
  *(Note: $E(a)$ and $g(a)$ are solved self-consistently at each redshift grid point via the coupled first-order ODE $\frac{d\ln g}{d\ln a} = -3\frac{\gamma_u}{E(a)}$ with initial condition $g(1) = 1$, integrated by 4th-order Runge–Kutta on a 1,000-point log-$a$ grid.)*
- **Sampled Parameters & Uniform Priors (`m8`):** $\Omega_m \in [0.1, 0.6]$, $h \in [0.5, 0.9]$, $100\omega_b \in [1.8, 2.6]$, $\gamma_u \in [0.0, 2.0]$ (so $w_0 \in [-1.0, +1.0]$), with fixed $\sum m_\nu = 0.06\text{ eV}$. Compare the minimum $\chi^2_{\min}(\text{Law 1})$ against flat $\Lambda\text{CDM}$ ($\gamma_u = 0$, 1 fewer parameter) and unconstrained flat $w_0w_a\text{CDM}$ ($w_0 \in [-3.0, 1.0], w_a \in [-3.0, 2.0], w_0 + w_a < 0$, 1 more parameter).
- **Pre-Registered Thresholds for Primary Test `T1-L1`:**
  - **PASS:** In **both** supernova runs, Law 1 improves the fit over $\Lambda\text{CDM}$ by $\Delta\chi^2_{\min}(\text{Law 1} - \Lambda\text{CDM}) \le -4.0$ ($\ge 2\sigma$ preference for unwinding over $\Lambda\text{CDM}$) **and** is not disfavored relative to unconstrained $w_0w_a\text{CDM}$ by more than $2\sigma$: $\Delta\chi^2_{\min}(\text{Law 1} - w_0w_a\text{CDM}) \le +4.0$ ($\Delta\text{dof} = 1$).
  - **FAIL:** In **both** supernova runs, $\Delta\chi^2_{\min}(\text{Law 1} - w_0w_a\text{CDM}) > +9.0$ ($> 3\sigma$ rejection of the Law 1 $(w_0, w_a)$ relation relative to $w_0w_a\text{CDM}$) **or** $\Delta\chi^2_{\min}(\text{Law 1} - \Lambda\text{CDM}) > -1.0$ (unwinding provides $< 1\sigma$ improvement over $\Lambda\text{CDM}$).
  - **INCONCLUSIVE:** $4.0 < \Delta\chi^2_{\min}(\text{Law 1} - w_0w_a\text{CDM}) \le 9.0$, or the two supernova compilations disagree (`Section 3.3`).
- **Pre-Test Forecast for `T1-L1`:** **Forecast to FAIL (or land on the FAIL/INCONCLUSIVE boundary at $2.6\text{–}3.5\sigma$).** At $w_0 = -0.84, \Omega_m = 0.315$, Law 1 predicts $w_a = -0.102$ ($w(a) > -1$ at all $a$), whereas DESI DR2 + CMB + SNe prefers $w_a \approx -0.62 \pm 0.22$ (`DES-Dovekie`) to $-0.86 \pm 0.25$ (`Pantheon+`), disfavoring the non-phantom Law 1 curve by $\Delta\chi^2 \approx 7\text{–}12$.

### Secondary Check `T1-Sign`: Unconstrained CPL $w_0 > -1$ Check (Locked v1.0.1 Criterion, Demoted per B4)
- **Sampled Parameters & Uniform Priors (`m8`):** Flat $w_0w_a\text{CDM}$ with $\Omega_m \in [0.1, 0.6]$, $h \in [0.5, 0.9]$, $100\omega_b \in [1.8, 2.6]$, $w_0 \in [-3.0, 1.0]$, $w_a \in [-3.0, 2.0]$ (matching the official DESI DR2 prior range and physical requirement $w_0 + w_a < 0$).
- **Thresholds (One-Sided vs. Two-Sided Convention Stated Explicitly per B4):**
  - **PASS:** In both supernova runs, the one-sided marginalized posterior probability satisfies $P(w_0 > -1 \mid \text{data}) \ge 0.95$ (corresponding to one-sided Gaussian $z = \frac{\hat{w}_0 + 1}{\sigma_{w_0}} \ge 1.645$; the stricter two-sided $2\sigma$ tail $P(w_0 > -1 \mid \text{data}) \ge 0.9772$, $z \ge 2.0$, is also reported alongside).
  - **FAIL:** In both runs, $P(w_0 < -1 \mid \text{data}) \ge 0.95$; **or**, in any release where $\sigma_{w_0} \le 0.03$, $(w_0, w_a) = (-1, 0)$ lies inside the $68\%$ credible region in both runs.
  - **Pre-Test Note:** Published DESI DR2 + CMB + SNe posteriors give $w_0 = -0.838 \pm 0.055$ (`Pantheon+`, $z = +2.95\sigma$) and $w_0 = -0.84 \pm 0.06$ (`DES-Dovekie`, $z = +2.67\sigma$), so **`T1-Sign` is already known before registration to PASS** and serves only as a secondary directional check.

---

## 5.2 Test T2: The Leak and the Dark-to-Ordinary Ratio ($\Omega_b = 1/19$ Algebraic Identity Test, $f_{\rm leak}$, Prediction P3)

### Algebraic Identity Statement (Finding M1)
In `MULTIVERSE_STAGE1_EQUATIONS.md` §4 (c3)–(c4), $\Omega_b = 1/19$, $\Omega_{\rm dm} = \frac{6}{19}(1 - f_{\rm leak})$, and $\Omega_{bc} \equiv \Omega_b + \Omega_{\rm dm} = \Omega_{m,{\rm tot}} - \Omega_{\nu,0} = \frac{7 - 6f_{\rm leak}}{19}$. Therefore:
$$f_{\rm leak} = 1 - \frac{19\,\Omega_{bc} - 1}{6}, \qquad \sigma_f = \frac{19}{6}\,\sigma_{\Omega_{bc}}, \qquad \mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak}) = 19\,\Omega_{bc} - 1, \qquad \sigma_{\mathcal{R}_{\rm pred}} = 19\,\sigma_{\Omega_{bc}}.$$
Because $\Omega_{bc} = \Omega_b(1 + \mathcal{R}_{\rm true})$, $\mathcal{R}_{\rm pred} = \mathcal{R}_{\rm true} \iff \Omega_b = 1/19$: **$f_{\rm leak}$ cancels out of $\mathcal{R}_{\rm pred}$, making T2 algebraically a test of the parameter-free baryon share $\Omega_b = 1/19$.** If any fit yields $\Omega_{bc} > 7/19$ ($f_{\rm leak} < 0$), the raw negative value is reported without clipping (`m12`).

### Test `T2-A`: Locked v1.0.1 Expansion Fit with Exact Conditional $(R, \ell_A \mid \omega_b)$ Likelihood and Overlap Correlation (Resolving M1, M7, M9, m8)
- **Fixing Dataset (`FIX`):** Flat $w_0w_a\text{CDM}$ fit ($\Omega_m \in [0.1, 0.6], h \in [0.5, 0.9], 100\omega_b \in [1.8, 2.6], w_0 \in [-3.0, 1.0], w_a \in [-3.0, 2.0], w_0 + w_a < 0$, $\sum m_\nu = 0.06\text{ eV}$) to:
  1. DESI DR2 BAO with the joint Ly$\alpha$ BAO+AP vector at $z_{\rm eff} = 2.33$ (`M7`);
  2. The **exact conditional Gaussian likelihood $(R, \ell_A \mid 100\omega_b)$** computed from the $3\times 3$ Chen, Huang & Wang (2019) Planck 2018 covariance matrix (`M9`), so that Planck's marginal $\omega_b$ prior is removed while the acoustic-horizon correlation of $(R, \ell_A)$ with $\omega_b$ ($r_{R,\omega_b} = -0.66, r_{\ell_A,\omega_b} = -0.33$) is preserved:
     $$\boldsymbol{\mu}_{R,\ell_A \mid \omega_b}(\omega_b) = \begin{pmatrix} 1.7502 \\ 301.471 \end{pmatrix} + \mathbf{C}_{12}\,C_{22}^{-1}\left(100\omega_b - 2.236\right), \qquad \mathbf{C}_{R,\ell_A \mid \omega_b} = \mathbf{C}_{11} - \mathbf{C}_{12}\,C_{22}^{-1}\mathbf{C}_{21},$$
     where $\mathbf{C}_{11}$ is the $2\times 2$ $(R, \ell_A)$ block, $\mathbf{C}_{12} = (-0.66(0.0046)(0.015),\; -0.33(0.090)(0.015))^T$, and $C_{22} = 0.015^2$. *(The marginal $2\times 2$ block $\mathbf{C}_{11}$ is also evaluated as a cross-check.)*
  3. External BBN deuterium baryon density prior (`M9`):
     - **Primary Locked v1.0.1 BBN Prior:** Cooke, Pettini & Steidel (2018), ApJ 855, 102: $100\omega_b = 2.166 \pm 0.019$.
     - **Updated Post-LUNA / DESI DR2 BBN Prior:** Schöneberg (2024) / DESI Collaboration (2025b): $100\omega_b = 2.218 \pm 0.055$.
  4. Supernovae run separately: **Run T2-Pantheon+** and **Run T2-DES-Dovekie**.
  From the MCMC posterior of $\Omega_{bc} \equiv \Omega_{m,{\rm tot}} - \Omega_{\nu,0}$ in each run, extract the median $\Omega_{bc}$ and $68\%$ half-width $\sigma_{\Omega_{bc}} = \frac{1}{2}(\Omega_{bc,84} - \Omega_{bc,16})$, and freeze $f_{\rm leak}$, $\sigma_f$, and $\mathcal{R}_{\rm pred} = 19\Omega_{bc} - 1$ in `results/FREEZE_T2.json`. *(Downstream rule: Test T5 uses $f_{\rm leak}$ frozen from the Pantheon+ primary run.)*
- **Testing Dataset (`TEST`) & Overlap Correlation (`M1`):** Planck 2018 base $\Lambda\text{CDM}$ `TT,TE,EE+lowE+lensing` (Planck Collaboration 2020, Table 2): $\omega_b = 0.02237 \pm 0.00015, \omega_c = 0.1200 \pm 0.0012 \implies \mathcal{R}_{\rm Planck} = 5.36 \pm 0.065$ (unrounded $5.3643 \pm 0.0646$).  
  Because $R = \sqrt{\Omega_m H_0^2}D_M(z_*)/c$ and $\ell_A = \pi D_M(z_*)/r_s(z_*)$ come from the same Planck CMB acoustic peaks as $\omega_c/\omega_b$, we evaluate both:
  1. **Locked Uncorrelated Formula:** $\sigma_{\rm comb}^{\rm uncorr} = \sqrt{(19\sigma_{\Omega_{bc}})^2 + 0.065^2}$;
  2. **Overlap-Corrected Formula:** $\sigma_{\rm comb}^{\rm corr} = \sqrt{(19\sigma_{\Omega_{bc}})^2 + \sigma_{\rm Planck}^2 - 2\rho_{\rm overlap}(19\sigma_{\Omega_{bc}})\sigma_{\rm Planck}}$, where $\rho_{\rm overlap} \approx +0.35$ is computed by Gaussian Jacobian propagation across the Planck 2018 parameter covariance.

### Test `T2-B`: Self-Consistent Constrained Model Fit (Resolving M1)
Fit the exact same datasets (`DESI DR2 BAO + conditional CMB (R, \ell_A | \omega_b) + BBN \omega_b + SNe`) while **imposing the model's structural equations directly inside the likelihood**:
$$\Omega_b = \frac{1}{19} \implies \omega_b = \frac{h^2}{19}, \qquad \Omega_{\rm dm} = \frac{6}{19}(1 - f_{\rm leak}), \qquad \Omega_{bc} = \frac{7 - 6f_{\rm leak}}{19},$$
sampling $(f_{\rm leak}, h, w_0, w_a)$ and testing both $\mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak})$ against $\mathcal{R}_{\rm Planck}$ and the goodness-of-fit penalty $\Delta\chi^2_{\min}(\text{T2-B} - w_0w_a\text{CDM})$ (which fails if $> 9.0$).

### Direct Parameter-Free Tests `T2-N1` and `T2-N2` (Resolving M2)
- **Test `T2-N1` (Direct Baryon Share Check):** Test $\Omega_b^{\rm model} = 1/19 = 0.052632$ against Planck 2018 $\Omega_b = 0.04930 \pm 0.00086$:
  $$\text{PASS if } \left|\Omega_b^{\rm model} - \Omega_b^{\rm Planck}\right| \le 2\sigma_{\Omega_b}, \qquad \text{FAIL if } > 2\sigma_{\Omega_b}.$$
  *(Known pre-test value: $+0.003332 / 0.00086 = +3.87\sigma \implies$ **FAIL**.)*
- **Test `T2-N2` (Implied Hubble Constant Check):** Test $H_0^{\rm pred} = 100\sqrt{19\omega_b}\text{ km s}^{-1}\text{ Mpc}^{-1}$ against Planck 2018 $H_0 = 67.36 \pm 0.54\text{ km s}^{-1}\text{ Mpc}^{-1}$ and DESI DR2 BAO + BBN $H_0 = 68.52 \pm 0.62\text{ km s}^{-1}\text{ Mpc}^{-1}$:
  $$\text{PASS if } \left|H_0^{\rm pred} - H_0^{\rm obs}\right| \le 2\sigma_{\rm comb}, \qquad \text{FAIL if } > 2\sigma_{\rm comb}.$$
  *(Known pre-test values: $H_0^{\rm pred} = 65.19 \pm 0.22$ for Planck $\omega_b$, $64.92 \pm 0.81$ for LUNA BBN $\omega_b$, $64.15 \pm 0.28$ for Cooke+18 BBN $\implies 3.5\text{–}6.2\sigma$ tension $\implies$ **FAIL**.)*

### Pre-Registered Thresholds and Forecast for Test T2
- **PASS:** $|\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm Planck}| \le 2\sigma_{\rm comb}$ in **both** supernova runs (and $\Delta\chi^2_{\min}(\text{T2-B} - w_0w_a\text{CDM}) \le 9.0$ in `T2-B`).
- **FAIL:** $|\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm Planck}| > 2\sigma_{\rm comb}$ in **both** supernova runs.
- **Pre-Test Forecast for T2:** **Forecast to FAIL at $\sim 3.5\sigma$ (`Pantheon+`) and $\sim 3.6\sigma$ (`DES-Dovekie`).** Published DESI DR2 + CMB + SNe fits give $\Omega_m \approx 0.311 \pm 0.006 \implies \Omega_{bc} \approx 0.3096 \pm 0.006 \implies \mathcal{R}_{\rm pred} \approx 4.88 \pm 0.114$, which misses $\mathcal{R}_{\rm Planck} = 5.36 \pm 0.065$ by $\Delta\mathcal{R} \approx -0.48$ ($3.6\sigma_{\rm comb}$).

---

## 5.3 Test T3: No Direct Detection (Prediction P2)
- Tracked externally by Gregory from LUX-ZEPLIN (LZ) and other direct-detection experiments; no computation in this package.

---

## 5.4 Test T4a: Offset Sign in Young Mergers (`EXPLORATORY`, Resolving B2 & B3)

- **Status (`B3`):** **`EXPLORATORY (Insufficient Independent Young Mergers, N = 1)`**.
- **Physical Trajectory Model Chosen (`B3`):** **Model A13b (Symmetric Harmonic Core Passage, $x_S(t) = \frac{v_p}{\omega_0}\sin(\omega_0 t)$)**, which predicts $\Delta\tilde{x}_S(T; \tau_{\rm lag}) \approx \frac{1}{6}\omega_0^2 v_p\tau_{\rm lag}^2(3T - 2\tau_{\rm lag})$ (negative for $0 < T < \frac{2}{3}\tau_{\rm lag}$ and positive only for $\frac{2}{3}\tau_{\rm lag} < T \le \tau_{\rm lag}$).
- **Fixing Dataset (`FIX`):** Bullet Cluster (`1E 0657-558`), fixing $\tau_{\rm lag} \ge 150\text{ Myr}$ under Markevitch et al. (2002)'s bow-shock age ($0.15 \pm 0.05\text{ Gyr}$) or $\tau_{\rm lag} \ge 400\text{–}600\text{ Myr}$ under Dawson (2013)'s dynamical MCMAC age ($0.40 \pm 0.10\text{ Gyr}$ temporal prior; $0.60^{+0.50}_{-0.30}\text{ Gyr}$ default prior). Per Rule G2, **the Bullet Cluster is unconditionally excluded from the test sample**.
- **Single Registered Statistic (`B2` & `B3`):** Across all non-Bullet subclusters with independently published $t_p \le 150\text{ Myr}$ (which contains only $N = 1$ system, `Abell 2744`, $t_p = 0.15 \pm 0.05\text{ Gyr}$; and $N = 5$ non-Bullet systems with $t_p \le 400\text{ Myr}$ under Dawson's Bullet bound), compute the **inverse-variance-weighted mean** of the projected offset along $\hat{\mathbf{s}}_{G\to S} \equiv \frac{\mathbf{x}_S - \mathbf{x}_G}{|\mathbf{x}_S - \mathbf{x}_G|}$:
  $$\Delta_{SI}^{\parallel} \equiv \left(\mathbf{x}_I - \mathbf{x}_S\right)\cdot\hat{\mathbf{s}}_{G\to S} = \delta_{SI} = \delta_{SG}\,\beta = -\left|\delta_{SG}\right|\beta,$$
  evaluated in both Harvey et al. (2015, Science 347, 1462, Table S1) and Wittman, Golovich & Dawson (2018, ApJ 869, 104, Table 1). Because $N = 1 < N_{\rm min} = 3$ for $t_p \le 150\text{ Myr}$, T4a is reported as an exploratory measurement and does not enter the scored test tally.

---

## 5.5 Test T4b: The Age Cutoff ($\tau_{\rm lag}$, Primary Cluster Pillar Test, Resolving M6)

- **Deterministic Byte-Wise ASCII Sort Rule (`M6`):**  
  The 16 dissociative merging clusters are ordered by **Python byte-wise ASCII `sorted()` on the exact `Catalog Designation` string**. Because ASCII `'1'` (`0x31`) < `'A'` (`0x41`) and `'C'` (`0x43`) < `'b'` (`0x62`), `'1E 0657-558'` naturally sits at position 1 (`Training, Odd`) and `'ACT-CL J0102-4915'` sits at position 2 (`Test, Even`) with **zero manual swapping**. Odd positions ($1, 3, \dots, 15$) form the **Training Half (8 clusters)** and even positions ($2, 4, \dots, 16$) form the **Test Half (8 clusters)**.
- **Frozen Sample List, Corrected Cited Ages (`M6`), and Explicit Position Catalog Sources:**
  - **Bullet Cluster (`1E 0657-558`) Age Update (`M6`):** Dawson (2013, ApJ 772, 131, Table 2) reports $t_p = 0.40 \pm 0.10\text{ Gyr}$ (with temporal prior; $0.60^{+0.50}_{-0.30}\text{ Gyr}$ default prior), whereas Markevitch et al. (2002, ApJ 567, L27) estimated $0.15 \pm 0.05\text{ Gyr}$ from the bow-shock speed. Both the **Dawson (2013) primary dynamical age ($0.40 \pm 0.10\text{ Gyr}$)** and the **Markevitch et al. (2002) shock age ($0.15 \pm 0.05\text{ Gyr}$)** are evaluated and reported.
  - **Musket Ball (`DLSCL J0916.2+2951`) Age Update (`M6`):** Dawson (2013, ApJ 772, 131, Table 2) reports $t_p = 1.10^{+1.30}_{-0.40}\text{ Gyr}$ (68% confidence interval $0.7\text{–}2.4\text{ Gyr}$; symmetric Gaussian approximation $1.10 \pm 0.65\text{ Gyr}$).

| # | Catalog Designation | Common Name | Split Half | $t_p$ (Gyr) | $\sigma_{t_p}$ (Gyr) | Dynamical Age Source | Frozen $(S, G, I)$ Position Source Catalog |
|---|---|---|---|---|---|---|---|
| 1 | `1E 0657-558` | Bullet Cluster | **Training (Odd)** | `0.40` *(0.15 shock)* | `0.10` *(0.05)* | Dawson 2013 Table 2 *(Markevitch+02)* | Clowe et al. 2006 (ApJ 648, L109); Harvey et al. 2015 Table S1 |
| 2 | `ACT-CL J0102-4915` | El Gordo | **Test (Even)** | `0.75` | `0.15` | Ng et al. 2015 (MNRAS 453, 1531) | Jee et al. 2014 (ApJ 785, 20, Table 1); Kim et al. 2021 (ApJ 923, 101) |
| 3 | `Abell 1240` | Abell 1240 | **Training (Odd)** | `0.45` | `0.15` | Cho et al. 2022 (ApJ 925, 68) | Cho et al. 2022 (ApJ 925, 68, Table 2); Barrena et al. 2009 |
| 4 | `Abell 1758N` | Abell 1758N | **Test (Even)** | `0.40` | `0.15` | Monteiro-Oliveira et al. 2017a | Ragozzine et al. 2012 (ApJ 744, 94); Harvey et al. 2015 Table S1 |
| 5 | `Abell 2034` | Abell 2034 | **Training (Odd)** | `0.30` | `0.10` | Monteiro-Oliveira et al. 2018 | Monteiro-Oliveira et al. 2018 (MNRAS 481, 1097); Owers et al. 2014 |
| 6 | `Abell 2146` | Abell 2146 | **Test (Even)** | `0.25` | `0.08` | Russell et al. 2010; White et al. 2015 | King et al. 2016 (MNRAS 459, 517); Coleman et al. 2017 (MNRAS 464, 2469) |
| 7 | `Abell 2744` | Pandora's Cluster | **Training (Odd)** | `0.15` | `0.05` | Merten et al. 2011 (MNRAS 417, 333) | Merten et al. 2011 (NW/Core subclusters); Harvey et al. 2015 Table S1 |
| 8 | `Abell 3376` | Abell 3376 | **Test (Even)** | `0.55` | `0.15` | Machado & Lima Neto 2013 | Monteiro-Oliveira et al. 2017b (MNRAS 468, 4566, Table 2) |
| 9 | `Abell 520` | Train Wreck | **Training (Odd)** | `0.80` | `0.25` | Markevitch et al. 2005 (ApJ 627, 733) | Jee et al. 2014 (ApJ 783, 78) *[primary]*; Clowe et al. 2012 *[stress check]* |
| 10 | `Abell 754` | Abell 754 | **Test (Even)** | `0.30` | `0.10` | Macario et al. 2011 (ApJ 728, 82) | Okabe & Umetsu 2008 (PASJ 60, 345); Harvey et al. 2015 Table S1 |
| 11 | `CIZA J2242.8+5301` | Sausage Cluster | **Training (Odd)** | `0.80` | `0.15` | Dawson et al. 2015 (ApJ 805, 143) | Jee et al. 2015 (ApJ 802, 46, Table 1) |
| 12 | `DLSCL J0916.2+2951` | Musket Ball | **Test (Even)** | `1.10` | `0.65` *(+1.3/-0.4)* | Dawson 2013 (ApJ 772, 131, Table 2) | Dawson et al. 2012 (ApJL 747, L42, Table 1) |
| 13 | `MACS J0025.4-1222` | Baby Bullet | **Training (Odd)** | `0.50` | `0.20` | Bradač et al. 2008 (ApJ 687, 959) | Bradač et al. 2008 (ApJ 687, 959); Harvey et al. 2015 Table S1 |
| 14 | `MACS J1149.5+2223` | MACS J1149 | **Test (Even)** | `1.16` | `0.38` | Golovich et al. 2016 (ApJ 831, 110) | Golovich et al. 2016 (ApJ 831, 110); Rau et al. 2014 (MNRAS 443, 957) |
| 15 | `RX J0603.3+4214` | Toothbrush Cluster | **Training (Odd)** | `1.50` | `0.30` | Brüggen et al. 2012; Jee et al. 2016 | Jee et al. 2016 (ApJ 817, 179, Table 2) |
| 16 | `ZwCl 0008.8+5215` | ZwCl 0008 | **Test (Even)** | `0.76` | `0.21` | Golovich et al. 2017 (ApJ 838, 110) | Golovich et al. 2017 (ApJ 838, 110, Table 4) |

*(Note on byte-wise ASCII sort order: `'1E 0657-558'`, `'ACT-CL J0102-4915'`, `'Abell 1240'`, `'Abell 1758N'`, `'Abell 2034'`, `'Abell 2146'`, `'Abell 2744'`, `'Abell 3376'`, `'Abell 520'`, `'Abell 754'`, `'CIZA J2242.8+5301'`, `'DLSCL J0916.2+2951'`, `'MACS J0025.4-1222'`, `'MACS J1149.5+2223'`, `'RX J0603.3+4214'`, `'ZwCl 0008.8+5215'` is 100% deterministic under Python `sorted()`.)*

- **Subcluster Aggregation & Classification Rule (`M6`):** For bimodal mergers with two colliding subclusters (e.g., Bullet, El Gordo, Baby Bullet, Sausage, Musket Ball, Abell 2146, ZwCl 0008), the classification uses the primary high-mach / smaller ("bullet") subcluster where ram-pressure stripping of gas from stars is maximal; both subcluster-level and system-level classifications are reported. With $d_{IG} = |\mathbf{x}_I - \mathbf{x}_G|$, $d_{IS} = |\mathbf{x}_I - \mathbf{x}_S|$, and $\sigma_{\rm diff} = \sqrt{\sigma_I^2 + \sigma_G^2 + \sigma_S^2}$:
  - `"dark mass with gas"` if $d_{IS} - d_{IG} > 2\sigma_{\rm diff}$;
  - `"dark mass with galaxies"` if $d_{IG} - d_{IS} > 2\sigma_{\rm diff}$;
  - `"unclassified"` (excluded) otherwise.
- **Fixing Rule (`FIX`) & Age-Uncertainty Propagation (`M6`):**  
  On the training half (odd rows), search $\tau_{\rm lag}$ on a uniform grid from $150\text{ Myr}$ (or $400\text{ Myr}$ under Dawson 2013's Bullet Cluster bound) to $1500\text{ Myr}$ in steps of $5\text{ Myr}$ and select the value maximizing the fraction of classified training systems predicted correctly (`dark mass with galaxies` for $t_p < \tau_{\rm lag}$, `dark mass with gas` for $t_p > \tau_{\rm lag}$); ties go to the smallest $\tau_{\rm lag}$. In addition to hard point-estimate classification, compute the **age-posterior-weighted accuracy** using each system's Gaussian/asymmetric age uncertainty $P_i(t_p < \tau_{\rm lag}) = \Phi\!\left(\frac{\tau_{\rm lag} - t_{p,i}}{\sigma_{t_p,i}}\right)$ via 10,000 Monte Carlo draws (`SEED = 20261030`).
- **Pre-Registered Thresholds (Unchanged):**
  - **PASS:** On the test half, the frozen step $\tau_{\rm lag}$ classifies $\ge 80\%$ of classified systems correctly, with $\ge 6$ classified test systems.
  - **FAIL:** (a) No step $\ge 150\text{ Myr}$ classifies $\ge 80\%$ of the training half correctly; **or** (b) the frozen step classifies $< 60\%$ of the test half correctly; **or** (c) every classified system, including at least one with $t_p \ge 1\text{ Gyr}$, has its dark mass with the galaxies (no cutoff below $1\text{ Gyr}$).
  - **INCONCLUSIVE:** Fewer than 6 classified test systems, or test accuracy between $60\%$ and $80\%$.
- **Pre-Test Forecast for T4b:** **Forecast to FAIL under clause (c)** because in standard weak/strong lensing analyses of old dissociative mergers (`CIZA J2242.8+5301`, `DLSCL J0916.2+2951`, `MACS J1149.5+2223`, `RX J0603.3+4214`, all with $t_p \ge 0.8\text{–}1.5\text{ Gyr}$), the mass peaks coincide with the collisionless galaxies rather than the X-ray gas (save for the disputed core of `Abell 520`).

---

## 5.6 Test T5: Halo Widths from the Refraction Kernel ($\sigma_{\rm ref}$, Prediction P5; Resolving B1, M3, M4, M5, M15, m9)

- **Model & Fixed Parameters:** Each galaxy in SPARC (`MassModels_Lelli2016c.mrt` and `SPARC_Lelli2016c.mrt`, Lelli, McGaugh & Schombert 2016) is treated as isolated in its rest frame ($\tilde{\rho}_b = \rho_b$ under the unified coarse-grained velocity rule `[A12]` & `[A16]`), with fixed mass-to-light ratios $\Upsilon_{\rm disk} = 0.5\,M_\odot/L_\odot$ and $\Upsilon_{\rm bul} = 0.7\,M_\odot/L_\odot$, and $f_{\rm leak}$ frozen from the Test T2 Pantheon+ primary run. Enclosed shadow mass $M_{\rm sh}(< r)$ is computed via the **corrected** 3D Gaussian error-function kernel $\mathcal{F}_\sigma(r, r')$ (with coefficient $\frac{1}{\sqrt{2\pi}}$, verified in Gate `G9-d`):
  $$\mathcal{F}_\sigma(r, r') = \frac{1}{2}\left[\operatorname{erf}\!\left(\frac{r + r'}{\sqrt{2}\,\sigma_{\rm ref}}\right) + \operatorname{erf}\!\left(\frac{r - r'}{\sqrt{2}\,\sigma_{\rm ref}}\right)\right] - \frac{1}{\sqrt{2\pi}}\,\frac{\sigma_{\rm ref}}{r'}\left[\exp\!\left(-\frac{(r - r')^2}{2\sigma_{\rm ref}^2}\right) - \exp\!\left(-\frac{(r + r')^2}{2\sigma_{\rm ref}^2}\right)\right].$$
- **Exact Numerical Specification for $dM_b(r')$ and Radial Quadrature (Resolving M4):**
  1. **Non-Negative Monotonic Baryon Shell Construction:** For each SPARC galaxy $g$ with radial grid $r_1 < r_2 < \dots < r_{N_g} \equiv r_{\max}$, compute the cumulative spherical baryon mass at each grid radius $M_b^{\rm raw}(< r_j) = \frac{r_j\,v_{\rm bar}^2(r_j)}{G}$ where $v_{\rm bar}^2(r_j) = v_{\rm gas}(r_j)|v_{\rm gas}(r_j)| + 0.5\,v_{\rm disk}^2(r_j) + 0.7\,v_{\rm bul}^2(r_j)$. Enforce strict radial monotonicity via cumulative running maximum $M_b^{\rm mono}(< r_j) = \max_{1 \le m \le j}\!\left(0,\; M_b^{\rm raw}(< r_m)\right)$ so that every shell mass $\Delta M_{b,j} = M_b^{\rm mono}(< r_j) - M_b^{\rm mono}(< r_{j-1}) \ge 0$ is strictly non-negative (preventing negative shell weights from inner H I depressions or flat-disk multipoleovershoots).
  2. **500-Point Quadrature Grid & Exponential Tail Continuation Beyond $r_{\max}$:** Interpolate $M_b^{\rm mono}(< r')$ onto a 400-point linear-plus-log radial grid on $[0, r_{\max}]$ using monotonic PCHIP interpolation (`scipy.interpolate.PchipInterpolator`), and continue the baryon profile from $r_{\max}$ to $r_{\rm upper} = r_{\max} + 5\sigma_{\rm ref}$ on a 100-point grid using an exponential disk tail $\Sigma_{\rm tail}(r') = \Sigma_b(r_{\max})\exp(-(r' - r_{\max})/R_d)$ (where $\Sigma_b(r_{\max})$ is the total surface density $\Upsilon_{\rm disk}\text{SBdisk}(r_{\max}) + \Upsilon_{\rm bul}\text{SBbul}(r_{\max})$ from `MassModels_Lelli2016c.mrt`, and $R_d$ is the disk scale length from `SPARC_Lelli2016c.mrt`), evaluated by composite trapezoidal/Simpson quadrature.
  3. **Velocity Error Model:** Use only the published observational velocity uncertainty $\sigma_{V,g}(r_j) = \text{errV}$ from `MassModels_Lelli2016c.mrt` (with zero added distance or inclination nuisance parameters).
  4. **Global Optimizer Protocol:** To guarantee finding the global minimum on the 88-galaxy training set, first evaluate $\chi^2_{\rm train}$ on a 200-point log-spaced grid over $\sigma_{\rm ref} \in [0.1, 100.0]\text{ kpc}$ (`T5-A`) or $k \in [0.05, 50.0]$ (`T5-B`), and then polish the global grid minimum using `scipy.optimize.minimize_scalar(..., bounds=(grid_left, grid_right), method='bounded', options={'xatol': 1e-5})`.
- **Sample Split & Reduced $\chi^2$ Definition (Resolving M4 & m9):**
  - Order all 175 unique galaxy identifiers in `MassModels_Lelli2016c.mrt` by **Python byte-wise ASCII `sorted()` on the stripped string ID** (`gal_id.strip()`).
  - **Training Half (`FIX`):** Odd positions ($1\text{-based indices } 1, 3, \dots, 175$; 88 galaxies).
  - **Held-Out Half (`TEST`):** Even positions ($1\text{-based indices } 2, 4, \dots, 174$; 87 galaxies).
  - Because **zero parameters are fitted per individual held-out galaxy** ($\sigma_{\rm ref}$ or $k$ is frozen from the training half and $f_{\rm leak}$ is frozen from T2), each held-out galaxy $g$ has $\text{dof}_g = N_g$ and reduced chi-squared (`m9`):
    $$\chi^2_{{\rm red},g} = \frac{1}{N_g}\sum_{j=1}^{N_g} \left(\frac{V_{{\rm obs},g}(r_j) - V_{{\rm model},g}(r_j)}{\sigma_{V,g}(r_j)}\right)^2.$$
- **Pre-Registered Thresholds for `T5-A` (Primary) and `T5-B` (Secondary):**
  - **PASS (`T5-A` Primary):** On the held-out half, median $\chi^2_{\rm red} \le 1.5$ **and** $\ge 70\%$ of galaxies have $\chi^2_{\rm red} < 2.0$. *(For `T5-B` Secondary, the $2\times$ Bonferroni trial-adjusted thresholds `median <= 1.35` and `>= 75% < 2.0` are also reported alongside the raw `1.5 / 70%` thresholds.)*
  - **FAIL:** On the held-out half, median $\chi^2_{\rm red} > 3.0$, **or** $< 40\%$ of galaxies have $\chi^2_{\rm red} < 2.0$.
  - **INCONCLUSIVE:** Between these thresholds.
- **Saturation Cap Forecast & Mandatory Diagnostic (Resolving M3 & m4):**  
  Because $K_\sigma$ is normalized and diffusive, $g_{\rm obs}(r)/g_{\rm bar}(r) \le 1 + 6(1 - f_{\rm leak})$ at every radius $r > 0$. In the McGaugh et al. (2016) RAR, $g_{\rm obs}^{\rm RAR}/g_{\rm bar}$ exceeds $6.0$ at $g_{\rm bar} < g_{\rm bar}^{\rm cap} = 3.99\times 10^{-12}\text{ m s}^{-2}$ (for $f_{\rm leak} = 1/6$) and exceeds $6.20$ at $g_{\rm bar} < 3.71\times 10^{-12}\text{ m s}^{-2}$ (for $\mathcal{R} = 5.20$). **This mathematical ceiling makes a full T5 PASS very unlikely (Forecast: FAIL).** We report as a mandatory diagnostic: (a) the fraction of held-out radial points and galaxies with $g_{\rm bar} < g_{\rm bar}^{\rm cap}$, and (b) median $\chi^2_{\rm red}$ stratified into high-surface-brightness (`g_bar >= g_bar^cap` everywhere) vs. low-surface-brightness galaxies.

### Test `T5c`: NGC 1052-DF2 Stress Check (Corrected per M15)
- **DF2 Parameters & Literature Citations (`M15`):** Distance $D = 20.0\text{ Mpc}$, stellar mass $M_{*,{\rm DF2}} = 2.0\times 10^8\,M_\odot$ modeled as a 3D Plummer sphere with projected half-light radius $R_e = 2.2\text{ kpc}$ (3D half-mass radius $r_{1/2} = (2^{2/3} - 1)^{-1/2}R_e = 1.3048\,R_e = 2.87\text{ kpc}$), enclosed stellar mass $M_b(< r) = M_{*,{\rm DF2}}\frac{r^3}{(r^2 + R_e^2)^{3/2}}$.
  - **Primary Dynamical Mass Benchmark (Danieli et al. 2019, ApJL 874, L12, KCWI stellar dispersion $\sigma_{\rm stars} = 8.5^{+2.3}_{-3.1}\text{ km s}^{-1}$):** $M_{\rm dyn}(< 2.7\text{ kpc}) = (1.3 \pm 0.8)\times 10^8\,M_\odot$ evaluated at $r_{\rm eval,1} = 2.7\text{ kpc}$.
  - **Globular Cluster Upper-Limit Benchmark (van Dokkum et al. 2018, Nature 555, 629):** 90% confidence upper limits $M_{\rm dyn}(< 3.1\text{ kpc}) < 3.2\times 10^8\,M_\odot$ ($r_{\rm eval,2} = 3.1\text{ kpc}$) and $M_{\rm dyn}(< 7.6\text{ kpc}) < 3.4\times 10^8\,M_\odot$ ($r_{\rm eval,3} = 7.6\text{ kpc}$).
- **Frozen NGC 1052 Group Baryon Model & Scope Note (`M15`):** Massive elliptical NGC 1052 with baryonic mass $M_{b,{\rm NGC1052}} = 1.0\times 10^{11}\,M_\odot$ at projected separation $d_{\rm proj} = 80\text{ kpc}$ (expected 3D separation $d_{3\rm D} = \sqrt{3/2}\,d_{\rm proj} = 98.0\text{ kpc}$), contributing $M_{\rm sh,group}(< r_{\rm eval}) = 6(1 - f_{\rm leak}) M_{b,{\rm NGC1052}}\,\mathcal{F}_{\sigma_{\rm ref}}(r_{\rm eval}, d_{3\rm D})$. *(Note per Finding M15: across $\sigma_{\rm ref} \in [1, 100]\text{ kpc}$, $M_{\rm sh,group}(< 3.1\text{ kpc}) \le 2.5\times 10^6\,M_\odot \ll 0.8\times 10^8\,M_\odot$, so the group term is negligible and T5c purely tests whether the SPARC-frozen $\sigma_{\rm ref}$ satisfies $\sigma_{\rm ref} \gtrsim 3.3\text{ kpc}$ so DF2's own shadow is diffused outside $2.7\text{–}3.1\text{ kpc}$.)*
- **T5c Thresholds (Unchanged):** **PASS** if $M_{\rm pred}(< 2.7\text{ kpc})$ is within $2\sigma$ of $(1.3 \pm 0.8)\times 10^8\,M_\odot$ ($\le 2.9\times 10^8\,M_\odot$, requiring $\sigma_{\rm ref} \ge 3.3\text{ kpc}$) and $M_{\rm pred}(< 3.1\text{ kpc}) < 3.2\times 10^8\,M_\odot$; **FAIL** if $M_{\rm pred}(< 2.7\text{ kpc}) > (1.3 + 3\times 0.8)\times 10^8 = 3.7\times 10^8\,M_\odot$ ($\sigma_{\rm ref} < 2.2\text{ kpc}$); **INCONCLUSIVE** otherwise.

---

## 5.7 Test T6: The Hubble Tension as a Local Reading (Prediction P7; Resolving M14)

- **Fixing Dataset (`FIX`):** SH0ES Cepheid-calibrated supernova host sample (`IS_CALIBRATOR == 1` in `Pantheon+SH0ES.dat`, Riess et al. 2022), fitting and freezing the GLS weighted-mean Type Ia absolute magnitude $M_B^{\rm fixed}$ using the calibrator block of `Pantheon+SH0ES_STAT+SYS.cov`.
- **Testing Dataset (`TEST`) & Minimum Pixel Occupancy Rule (`M14`):** Pantheon+ Hubble-flow supernovae (`0.023 <= z_HD <= 0.15`, `IS_CALIBRATOR == 0`), partitioned into the 12 equal-area sky regions of a HEALPix $N_{\rm side} = 1$ grid in Galactic coordinates $(l, b)$ (`RING` ordering; Equatorial RA/Dec `RING` reported as a cross-check).
  - **Sparse-Pixel Merging Rule (`M14`):** Any HEALPix $N_{\rm side} = 1$ pixel containing fewer than $N_{\rm SN,min} = 10$ Hubble-flow supernovae (e.g., low-Galactic-latitude Zone-of-Avoidance pixels) is merged into its adjacent same-longitude-quadrant higher-$|b|$ neighbor pixel before inversion, yielding $N_{\rm pix} \le 12$ well-sampled sky regions with $\text{dof} = N_{\rm pix} - 1$.
- **GLS Estimator, Cosmic-Variance Floor, and Redshift Frame Check (`M14`):**  
  Fit the $N_{\rm pix}$ regional log-Hubble parameters $\eta_i = 5\log_{10} H_{0,i}$ by generalized least squares using $\mathbf{C}_{\rm HF}$ (`Section 8.1` of `MULTIVERSE_STAGE1_EQUATIONS.md`). To test excess regional variation above standard $\Lambda\text{CDM}$ large-scale-structure bulk flows in the $0.023 \le z \le 0.15$ shell, evaluate $\chi^2_{\rm het}$ both with the bare Pantheon+ covariance $\mathbf{C}_{H_0}$ and with the standard $\Lambda\text{CDM}$ regional cosmic-variance floor $\mathbf{C}_{H_0}^{\rm LSS} = \mathbf{C}_{H_0} + \sigma_{{\rm CV,reg}}^2\mathbf{I}_{N_{\rm pix}}$ ($\sigma_{\rm CV,reg} = 0.013\,\bar{H}_0 \approx 0.95\text{ km s}^{-1}\text{ Mpc}^{-1}$ for a $1/12$-sky cone over $0.023 \le z \le 0.15$), and run both peculiar-velocity-corrected $z_{\rm HD}$ (primary) and pure CMB-frame $z_{\rm CMB}$ (secondary check to ensure no flow-model circularity).
  - **Explicit Definition of All-Sky Local $\bar{H}_0$ (`M14`):** $\bar{H}_0 \equiv \frac{\mathbf{1}^T \mathbf{C}_{H_0}^{-1}\hat{\mathbf{H}}_0}{\mathbf{1}^T \mathbf{C}_{H_0}^{-1}\mathbf{1}}$ with variance $\sigma_{\bar{H}_0}^2 = (\mathbf{1}^T \mathbf{C}_{H_0}^{-1}\mathbf{1})^{-1} + (\frac{\ln 10}{5}\bar{H}_0)^2\sigma_{M_B^{\rm fixed}}^2$.
- **Pre-Registered Thresholds (Mechanical Only per M10 & M14):**
  - **PASS:** Regional heterogeneity is significant at $\ge 3\sigma$ ($p_{\rm het} = 1 - F_{\chi^2_{N_{\rm pix}-1}}(\chi^2_{\rm het}) \le 0.00270$) under both $\mathbf{C}_{H_0}$ and $\mathbf{C}_{H_0}^{\rm LSS}$, while all-sky local $\bar{H}_0$ exceeds Planck 2018 $\Lambda\text{CDM}$ ($67.36 \pm 0.54\text{ km s}^{-1}\text{ Mpc}^{-1}$) at $\ge 3\sigma$.
  - **FAIL:** Regional heterogeneity is consistent with zero ($p_{\rm het} > 0.3173$, i.e. $< 1\sigma$) while all-sky tension remains $\ge 3\sigma$. *(The non-mechanical sociological clause regarding SH0ES team acceptance of a systematic is removed per Finding M14.)*
  - **INCONCLUSIVE:** $0.00270 < p_{\rm het} \le 0.3173$ ($1\sigma\text{–}3\sigma$ regional variation).

---

# 6. Pre-Registered Coincidence Window Tolerances (Section 8.2 Diagnostic)

With Planck 2018 base $\Lambda\text{CDM}$ parameters ($\omega_b = 0.02237, \omega_c = 0.1200, H_0 = 67.36, \Omega_{bc} = 0.3138, \Omega_{m,{\rm tot}} = 0.3153, \Omega_\Lambda = 0.6847$), compute the cosmic time span $\Delta t_{\rm coinc}$ during which all three instantaneous shares $\Omega_b(a), \Omega_{\rm dm}(a), \Omega_{\rm de}(a)$ remain simultaneously within:
1. **Criterion H-Abs:** $\max_{i \in \{b, {\rm dm}, {\rm de}\}} |\Omega_i(a) - s_i^{\rm target}| \le 0.05$ ($\pm 5$ percentage points),
2. **Criterion H-Rel:** $\max_{i \in \{b, {\rm dm}, {\rm de}\}} |\Omega_i(a) - s_i^{\rm target}| / s_i^{\rm target} \le 0.10$ ($\pm 10\%$ fractional),
evaluated both for $f_{\rm leak} = 1/6$ ($s^{\rm target} = (1/19, 5/19, 13/19)$) and for the T2-frozen $f_{\rm leak}$.
