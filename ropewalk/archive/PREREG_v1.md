---
title: "MULTIVERSE Master Pre-Registration Protocol (PREREG.md)"
subtitle: "Frozen Analysis Choices, Likelihood Specifications, Sample Splits, and Pass/Fail Thresholds (v1.0.1)"
author: "Gregory Mandarano / WickedAI — Pre-Registration Compiled by Gemini 4 Argon"
date: "2026-10-30"
---

# 1. Purpose and Immutability Declaration (Rule R4 & G1–G9)

This document (`PREREG.md`) is written and SHA-256 hashed at the end of Stage 1 **before any dataset is downloaded or read by analysis code**. It incorporates:
1. All General Rules (G1–G9) and Test Thresholds (T1–T6) from `MULTIVERSE_TESTS_v1.md` (Version 1.0.1, October 2026) **without alteration**.
2. The written resolution of every methodological, likelihood, sample-selection, and numerical choice required by Rule G8 so that Stage 2 and Stage 3 execute deterministically with zero post-hoc tuning.

---

# 2. Restatement of General Rules (G1–G9, Unchanged from `MULTIVERSE_TESTS_v1.md`)

- **G1. No tuning after seeing the test data.** No parameter, kernel shape, sample cut, error model, or criterion may change after a test dataset has been loaded; any change voids the test.
- **G2. Fix on one dataset, test on another.** A dataset used to fix a parameter is never used to test that same parameter. One partial overlap is registered and stated plainly: in T2, the Planck CMB enters the fix only through the compressed distance priors $(R, \ell_A)$ and the test only through $\omega_c/\omega_b$.
- **G3. Freeze before testing.** Before a test dataset is opened, write the fixed values (with uncertainties), the analysis code version (git commit hash or SHA-256 of `scripts/`), and the date to `results/FREEZE_<test>.json`, and record its SHA-256. The test run must load the frozen values directly from that file.
- **G4. Thresholds are fixed.** Three outcomes, all reported with equal prominence: `PASS`, `FAIL`, `INCONCLUSIVE`.
- **G5. Structural constants are not free.** $N_s = 19$ and $N_r = 133$ may not be varied.
- **G6. No double counting.** Pantheon+ and DES SN are never combined in one fit; every supernova test is run separately with each, and both results are reported. Planck's $\omega_b$ and $\omega_c$ are used only to test $f_{\rm leak}$ (T2), never to fix it; the T2 fix uses Planck only through $(R, \ell_A)$. Planck also serves as the CMB prior in T1.
- **G7. Significance language.** "$n\sigma$" means the two-sided Gaussian-equivalent significance computed with each dataset's published likelihood and covariance.
- **G8. Ambiguities count as of the freeze.** Every model or analysis ambiguity is resolved in writing in this document before the freeze; anything left unresolved defaults to `INCONCLUSIVE`.
- **G9. Validation and convergence before any test run.** Background code must reproduce a published $\Lambda\text{CDM}$ result from the same data (specifically the DESI DR2 BAO-only flat $\Lambda\text{CDM}$ $\Omega_m = 0.2975 \pm 0.0086$ of DESI Collaboration 2025b, Table V) to within $0.3\sigma$. MCMC runs must converge with Gelman–Rubin $R - 1 < 0.01$ or effective sample size $\text{ESS} > 1000$ per parameter; an unconverged run is `INCONCLUSIVE`, not `PASS`.

---

# 3. Global Numerical, Random Seed, and Hardware Settings

- **Master Random Seed:** `SEED = 20261030` (used for all MCMC walker initializations and Monte Carlo uncertainty propagations).
- **MCMC Sampler (`emcee`):** Ensemble sampler with $N_{\rm walkers} = 32$, burn-in discarded after $5\tau_{\rm autocorr}$ (minimum 1,000 steps per walker), production chain length sufficient to achieve Gelman–Rubin $R - 1 < 0.01$ and $\text{ESS} > 1000$ per parameter (minimum 4,000 production steps per walker = 128,000 samples).
- **Hardware & Thread Cap:** All Python scripts set `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1` before importing numerical libraries, cap multiprocessing pools at `N_CORES = 12`, and set worker priority to `psutil.BELOW_NORMAL_PRIORITY_CLASS`.

---

# 4. Pre-Registered Test Specifications, Likelihoods, and Thresholds

## Test T1: Dark Energy Weakening ($w_0, w_a$, Prediction P1)

- **Model Prediction Fixed in Advance:** $w_0 > -1$ (dark energy density falling today) in flat $w_0w_a\text{CDM}$ with $w(a) = w_0 + w_a(1 - a)$. (Per `MULTIVERSE_TESTS_v1.md`, v1 does not specify whether $w(a) < -1$ was allowed in the past, so only $w_0$ is tested; DESI's phantom crossing is reported under Open Problem 11.)
- **Fixing Dataset (`FIX`):** None fitted to the model. Planck 2018 enters as the standard compressed CMB prior $(R, \ell_A, 100\omega_b)$ of Chen, Huang & Wang (2019), JCAP 02 (2019) 028, Table 1 (`Planck 2018 TT,TE,EE+lowE` in $w\text{CDM}$):
  $$\boldsymbol{\mu}_{\rm CMB} = \begin{pmatrix} R \\ \ell_A \\ 100\omega_b \end{pmatrix} = \begin{pmatrix} 1.7502 \\ 301.471 \\ 2.236 \end{pmatrix}, \qquad \boldsymbol{\sigma}_{\rm CMB} = \begin{pmatrix} 0.0046 \\ 0.090 \\ 0.015 \end{pmatrix}, \qquad \mathbf{R}_{\rm CMB} = \begin{pmatrix} 1.00 & 0.46 & -0.66 \\ 0.46 & 1.00 & -0.33 \\ -0.66 & -0.33 & 1.00 \end{pmatrix}.$$
- **Testing Datasets (`TEST`):**
  1. **Run T1-Pantheon+:** DESI DR2 BAO (`CobayaSampler/bao_data/desi_bao_dr2`, including Ly$\alpha$ BAO at $z_{\rm eff} = 2.33$ and the Ly$\alpha$ Alcock–Paczyński constraint $D_H(2.33)/r_d = 8.600 \pm 0.066, D_M(2.33)/r_d = 39.32 \pm 0.33$ of arXiv:2607.27410 as specified in the T1 note) + Planck 2018 $(R, \ell_A, 100\omega_b)$ prior + Pantheon+ supernovae ($z_{\rm HD} > 0.01$, `IS_CALIBRATOR == 0`, full `STAT+SYS` covariance, analytically marginalized over absolute magnitude offset $\mathcal{M}$).
  2. **Run T1-DES-Dovekie:** Same DESI DR2 + Ly$\alpha$ + Planck 2018 prior combined with DES SN 5-year (`DES-Dovekie` recalibrated compilation, `4_DISTANCES_COVMAT`, full `STAT+SYS` covariance, analytically marginalized over $\mathcal{M}$).
- **Sampled Parameters & Uniform Priors:** $\Omega_m \in [0.1, 0.6]$, $h \in [0.5, 0.9]$, $100\omega_b \in [1.8, 2.6]$, $w_0 \in [-3.0, 1.0]$, $w_a \in [-5.0, 3.0]$ (with standard physical requirement $w_0 + w_a < 0$ so dark energy is subdominant at early times), and fixed $\sum m_\nu = 0.06\text{ eV}$.
- **Pre-Registered Thresholds (Unchanged):**
  - **PASS:** In both supernova runs, $w_0 > -1$ at $95\%$ credibility (i.e., the marginalized posterior probability $P(w_0 > -1 \mid \text{data}) \ge 0.95$, or two-sided equivalent $w_0 = -1$ excluded below the 2.5th percentile / $2\sigma$ lower tail).
  - **FAIL:** In either run, $w_0 < -1$ at $95\%$ credibility; **or**, in any release where the $68\%$ uncertainty on $w_0$ is $\le 0.03$, $(w_0, w_a) = (-1, 0)$ lies inside the $68\%$ credible region in both runs.
  - **INCONCLUSIVE:** Anything else.

---

## Test T2: The Leak and the Dark-to-Ordinary Ratio ($f_{\rm leak}$, Prediction P3)

- **Parameter & Model Relations:** $f_{\rm leak}$ in the locked Static Form ($Q = 0$), with
  $$f_{\rm leak} = 1 - \frac{19\,\Omega_m - 1}{6}, \qquad \sigma_f = \frac{19}{6}\,\sigma_{\Omega_m}, \qquad \mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak}) = 19\,\Omega_m - 1, \qquad \sigma_{\mathcal{R}_{\rm pred}} = 6\,\sigma_f = 19\,\sigma_{\Omega_m}.$$
- **Fixing Dataset (`FIX`):** Flat $w_0w_a\text{CDM}$ fit ($\sum m_\nu = 0.06\text{ eV}$) to:
  1. DESI DR2 BAO (`desi_bao_dr2`),
  2. The $2\times 2$ $(R, \ell_A)$ block of the Chen, Huang & Wang (2019) Planck 2018 distance priors marginalized over $\omega_b$:
     $$\boldsymbol{\mu}_{R,\ell_A} = \begin{pmatrix} 1.7502 \\ 301.471 \end{pmatrix}, \qquad \mathbf{C}_{R,\ell_A} = \begin{pmatrix} 0.0046^2 & 0.46(0.0046)(0.090) \\ 0.46(0.0046)(0.090) & 0.090^2 \end{pmatrix},$$
  3. The BBN deuterium baryon density prior of Cooke, Pettini & Steidel (2018), ApJ 855, 102:
     $$100\,\omega_b = 2.166 \pm 0.019,$$
  4. Supernovae run separately: **Run T2-Pantheon+** and **Run T2-DES-Dovekie** (never combined). Planck's $\omega_b$ and $\omega_c$ are never used in the fix.
  From the marginalized posterior of $\Omega_m$ in each run, extract the median $\Omega_m$ and $68\%$ half-width $\sigma_{\Omega_m} = \frac{1}{2}\left(\Omega_{m,84} - \Omega_{m,16}\right)$, freeze $f_{\rm leak}$ and $\sigma_f$ in `results/FREEZE_T2.json`. *(Downstream rule: Test T5 uses $f_{\rm leak}$ frozen from the Pantheon+ run.)*
- **Testing Dataset (`TEST`):** Planck 2018 base $\Lambda\text{CDM}$ `TT,TE,EE+lowE+lensing` (Planck Collaboration 2020, Table 2):
  $$\omega_b = 0.02237 \pm 0.00015, \qquad \omega_c = 0.1200 \pm 0.0012 \implies \mathcal{R}_{\rm Planck} = 5.36 \pm 0.065.$$
- **Pre-Registered Thresholds (Unchanged):**
  - **PASS:** $\left|\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm Planck}\right| \le 2\,\sigma_{\rm comb}$, where $\sigma_{\rm comb} = \sqrt{(6\sigma_f)^2 + \sigma_{\rm Planck}^2}$ and $\sigma_{\rm Planck} = 0.065$, in **both** supernova runs.
  - **FAIL:** Otherwise ($\left|\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm Planck}\right| > 2\,\sigma_{\rm comb}$ in either supernova run).
  - **INCONCLUSIVE:** Only if validation (G9) or MCMC convergence fails.

---

## Test T3: No Direct Detection (Prediction P2)
- Tracked externally by Gregory from LUX-ZEPLIN (LZ) and other direct-detection experiments; no computation in this package.

---

## Test T4a: Offset Sign in Young Mergers ($\tau_{\rm lag}$, Prediction P4)

- **Fixing Dataset (`FIX`):** Bullet Cluster (1E 0657-558), time since core passage $0.1\text{–}0.2\text{ Gyr}$ (Markevitch et al. 2002) with lensing mass on the galaxies (Clowe et al. 2006), fixing $\tau_{\rm lag} > 150\text{ Myr}$.
- **Testing Dataset (`TEST`):** Star ($S$), gas ($G$), and lensing ($I$) positions from (1) Harvey et al. (2015), Science 347, 1462, and (2) the re-measurement of Wittman, Golovich & Dawson (2018), ApJ 869, 104.
  - **Primary Sample:** Subclusters in systems with an independently published time since pericenter $t_p \le 150\text{ Myr}$ (from the frozen merger age table in Section 4.5 below: 1E 0657-558 and Abell 2744, excluding the Bullet Cluster itself if required to avoid fix/test overlap, with both Bullet-excluded and Bullet-included reported transparently).
  - **Secondary Sample:** All measured subclusters in each catalog (reported; alone can only yield `INCONCLUSIVE`).
- **Statistic:** Inverse-variance-weighted mean (and unweighted sample mean with bootstrap/SEM error) of the dark-mass-minus-stars offset projected along the axis from the gas to the stars, $\Delta_{SI}^{\parallel} = -\delta_{SG}\,\beta$ (positive = away from the gas, ahead of the stars).
- **Pre-Registered Thresholds (Unchanged):**
  - **PASS:** Positive at $\ge 2\sigma$ in the primary sample in **both** catalogs.
  - **FAIL:** Negative (toward the gas) at $\ge 2\sigma$ in the primary sample in **both** catalogs.
  - **INCONCLUSIVE:** Consistent with zero ($< 2\sigma$), or the two catalogs disagree.

---

## Test T4b: The Age Cutoff ($\tau_{\rm lag}$, Prediction P4)

- **Frozen Sample List and Published Ages Since Pericenter ($t_p$):**  
  The 16 well-studied dissociative merging clusters with published dynamical times since pericenter $t_p$ and lensing + X-ray + optical maps are ordered alphabetically by catalog designation below. Per the pre-registered split rule (`MULTIVERSE_TESTS_v1.md` T4b: *"odd positions form the training half, even positions the test half; the Bullet Cluster is always in the training half"*), swapping 1E 0657-558 (position 2) with ACT-CL J0102-4915 (position 1) or indexing so 1E 0657-558 sits at position 1 places 8 systems in the Training Half and 8 systems in the Test Half:

| # | Catalog Designation | Common Name | Split Half | $t_p$ (Gyr) | $\sigma_{t_p}$ (Gyr) | Primary Dynamical Age & Lensing/X-Ray Sources |
|---|---|---|---|---|---|---|
| 1 | `1E 0657-558` | Bullet Cluster | **Training (Odd)** | 0.15 | 0.05 | Markevitch et al. 2002 (ApJ 567, L27); Clowe et al. 2006 (ApJ 648, L109); Dawson 2013 (ApJ 772, 131) |
| 2 | `ACT-CL J0102-4915` | El Gordo | **Test (Even)** | 0.75 | 0.15 | Ng et al. 2015 (MNRAS 453, 1531); Jee et al. 2014 (ApJ 785, 20); Kim et al. 2021 (ApJ 923, 101) |
| 3 | `Abell 520` | Train Wreck | **Training (Odd)** | 0.80 | 0.25 | Markevitch et al. 2005 (ApJ 627, 733); Jee et al. 2014 (ApJ 783, 78) [Clowe et al. 2012 stress test] |
| 4 | `Abell 754` | Abell 754 | **Test (Even)** | 0.30 | 0.10 | Macario et al. 2011 (ApJ 728, 82); Okabe & Umetsu 2008 (PASJ 60, 345); Harvey et al. 2015 |
| 5 | `Abell 1240` | Abell 1240 | **Training (Odd)** | 0.45 | 0.15 | Cho et al. 2022 (ApJ 925, 68); Golovich et al. 2019b (ApJ 882, 69) |
| 6 | `Abell 1758N` | Abell 1758N | **Test (Even)** | 0.40 | 0.15 | Monteiro-Oliveira et al. 2017a (MNRAS 466, 2614); Ragozzine et al. 2012 (ApJ 744, 94) |
| 7 | `Abell 2034` | Abell 2034 | **Training (Odd)** | 0.30 | 0.10 | Monteiro-Oliveira et al. 2018 (MNRAS 481, 1097); Owers et al. 2014 (ApJ 780, 163) |
| 8 | `Abell 2146` | Abell 2146 | **Test (Even)** | 0.25 | 0.08 | Russell et al. 2010 (MNRAS 406, 1721); King et al. 2016 (MNRAS 459, 517); Coleman et al. 2017 |
| 9 | `Abell 2744` | Pandora's Cluster | **Training (Odd)** | 0.15 | 0.05 | Merten et al. 2011 (MNRAS 417, 333); Jauzac et al. 2016 (MNRAS 463, 3876); Golovich et al. 2019b |
| 10 | `Abell 3376` | Abell 3376 | **Test (Even)** | 0.55 | 0.15 | Monteiro-Oliveira et al. 2017b (MNRAS 468, 4566); Machado & Lima Neto 2013 (MNRAS 430, 3249) |
| 11 | `CIZA J2242.8+5301` | Sausage Cluster | **Training (Odd)** | 0.80 | 0.15 | Dawson et al. 2015 (ApJ 805, 143); Jee et al. 2015 (ApJ 802, 46); Golovich et al. 2019b |
| 12 | `DLSCL J0916.2+2951` | Musket Ball | **Test (Even)** | 0.96 | 0.28 | Dawson 2013 (ApJ 772, 131); Dawson et al. 2012 (ApJL 747, L42) |
| 13 | `MACS J0025.4-1222` | Baby Bullet | **Training (Odd)** | 0.50 | 0.20 | Bradač et al. 2008 (ApJ 687, 959); Harvey et al. 2015 |
| 14 | `MACS J1149.5+2223` | MACS J1149 | **Test (Even)** | 1.16 | 0.38 | Golovich et al. 2016 (ApJ 831, 110); Golovich et al. 2019b (ApJ 882, 69) |
| 15 | `RX J0603.3+4214` | Toothbrush Cluster | **Training (Odd)** | 1.50 | 0.30 | Jee et al. 2016 (ApJ 817, 179); Brüggen et al. 2012 (MNRAS 425, L76); Golovich et al. 2019b |
| 16 | `ZwCl 0008.8+5215` | ZwCl 0008 | **Test (Even)** | 0.76 | 0.21 | Golovich et al. 2017 (ApJ 838, 110); Golovich et al. 2019b (ApJ 882, 69) |

- **Classification Rule (Unchanged):** Let $d_{IG} = |\mathbf{x}_I - \mathbf{x}_G|$ be the distance between the main lensing peak and X-ray gas peak, $d_{IS} = |\mathbf{x}_I - \mathbf{x}_S|$ be the distance between the main lensing peak and galaxy luminosity centroid, and $\sigma_{\rm diff} = \sqrt{\sigma_I^2 + \sigma_G^2 + \sigma_S^2}$ be the combined positional uncertainty:
  - `"dark mass with gas"` if $d_{IS} - d_{IG} > 2\sigma_{\rm diff}$;
  - `"dark mass with galaxies"` if $d_{IG} - d_{IS} > 2\sigma_{\rm diff}$;
  - `"unclassified"` (excluded) otherwise.
- **Fixing Rule (`FIX`):** On the training half (odd rows), search $\tau_{\rm lag}$ on a uniform grid from $150\text{ Myr}$ to $1500\text{ Myr}$ in steps of $5\text{ Myr}$ and select the value that maximizes the fraction of classified training systems predicted correctly (`dark mass with galaxies` for $t_p < \tau_{\rm lag}$, `dark mass with gas` for $t_p > \tau_{\rm lag}$); ties go to the smallest $\tau_{\rm lag}$.
- **Pre-Registered Thresholds (Unchanged):**
  - **PASS:** On the test half, the frozen step $\tau_{\rm lag}$ classifies $\ge 80\%$ of classified systems correctly, with $\ge 6$ classified test systems.
  - **FAIL:** (a) No step $\ge 150\text{ Myr}$ classifies $\ge 80\%$ of the training half correctly; **or** (b) the frozen step classifies $< 60\%$ of the test half correctly; **or** (c) every classified system, including at least one with $t_p \ge 1\text{ Gyr}$, has its dark mass with the galaxies (no cutoff below $1\text{ Gyr}$).
  - **INCONCLUSIVE:** Fewer than 6 classified test systems, or test accuracy between $60\%$ and $80\%$.

---

## Test T5: Halo Widths from the Refraction Kernel ($\sigma_{\rm ref}$, Prediction P5)

- **Model & Fixed Parameters:** Each galaxy in SPARC (`MassModels_Lelli2016c.mrt` and `SPARC_Lelli2016c.mrt`, Lelli, McGaugh & Schombert 2016) is treated as isolated, with fixed mass-to-light ratios $\Upsilon_{\rm disk} = 0.5\,M_\odot/L_\odot$ and $\Upsilon_{\rm bul} = 0.7\,M_\odot/L_\odot$, and $f_{\rm leak}$ frozen from the Test T2 Pantheon+ run. Enclosed shadow mass $M_{\rm sh}(< r)$ is computed via the exact 3D Gaussian error-function kernel $\mathcal{F}_\sigma(r, r')$ of Section (f3) applied to the radial baryonic mass distribution $dM_b(r')$.
- **Registered Variants:**
  - **T5-A:** Universal constant $\sigma_{\rm ref}$ in $\text{kpc}$ (searched over $\sigma_{\rm ref} \in [0.1, 100.0]\text{ kpc}$ via `scipy.optimize.minimize_scalar` to minimize total training $\chi^2$).
  - **T5-B:** Scaled width $\sigma_{\rm ref,g} = k\,R_{d,g}$ with universal dimensionless constant $k$ (searched over $k \in [0.05, 50.0]$ to minimize total training $\chi^2$).
- **Sample Split (Rule G8 Resolution):** All 175 galaxies in SPARC ordered lexicographically by exact SPARC galaxy name:
  - **Training Half (`FIX`):** Odd positions ($1, 3, \dots, 175$; 88 galaxies).
  - **Held-Out Half (`TEST`):** Even positions ($2, 4, \dots, 174$; 87 galaxies).
  - For each held-out galaxy $g$ with $N_g$ radial data points, reduced $\chi^2$ is $\chi^2_{{\rm red},g} = \frac{1}{N_g}\sum_{j=1}^{N_g} \left(\frac{V_{{\rm obs},g}(r_j) - V_{{\rm model},g}(r_j)}{\sigma_{V,g}(r_j)}\right)^2$.
- **Pre-Registered Thresholds for T5-A and T5-B (Unchanged):**
  - **PASS:** On the held-out half, median $\chi^2_{\rm red} \le 1.5$ **and** $\ge 70\%$ of galaxies have $\chi^2_{\rm red} < 2.0$.
  - **FAIL:** On the held-out half, median $\chi^2_{\rm red} > 3.0$, **or** $< 40\%$ of galaxies have $\chi^2_{\rm red} < 2.0$.
  - **INCONCLUSIVE:** Between these thresholds.
- **Test T5c: NGC 1052-DF2 Stress Check (Frozen Group-Baryon Model):**
  - **DF2 Parameters (van Dokkum et al. 2018, Nature 555, 629):** Distance $D = 20.0\text{ Mpc}$, stellar mass $M_{*,{\rm DF2}} = 2.0\times 10^8\,M_\odot$ modeled as a Plummer sphere with projected half-light radius $R_e = 2.2\text{ kpc}$ ($M_b(< r) = M_{*,{\rm DF2}}\frac{r^3}{(r^2 + R_e^2)^{3/2}}$), evaluated at the dynamical measurement radius $r_{\rm eval} = 3.1\text{ kpc}$ (and $r_{1/2} = 2.7\text{ kpc}$), compared against the published dynamical mass $M_{\rm dyn}(< 3.1\text{ kpc}) = (1.3 \pm 0.8)\times 10^8\,M_\odot$ (90% upper limit $< 3.4\times 10^8\,M_\odot$).
  - **Frozen NGC 1052 Group Baryon Model:** Massive elliptical NGC 1052 with baryonic mass $M_{b,{\rm NGC1052}} = 1.0\times 10^{11}\,M_\odot$ at projected separation $d_{\rm proj} = 80\text{ kpc}$ (expected 3D separation $d_{3\rm D} = \sqrt{3/2}\,d_{\rm proj} = 98.0\text{ kpc}$), contributing an external shadow mass within $r_{\rm eval}$ of $M_{\rm sh,group}(< r_{\rm eval}) = 6(1 - f_{\rm leak}) M_{b,{\rm NGC1052}}\,\mathcal{F}_{\sigma_{\rm ref}}(r_{\rm eval}, d_{3\rm D})$.
  - **T5c Thresholds (Unchanged):** **PASS** if $M_{\rm pred} = M_b(< r_{\rm eval}) + M_{\rm sh,DF2}(< r_{\rm eval}) + M_{\rm sh,group}(< r_{\rm eval})$ is within $2\sigma$ of $M_{\rm dyn}$; **FAIL** if $M_{\rm pred}$ exceeds $M_{\rm dyn}$ by $> 3\sigma$; **INCONCLUSIVE** otherwise.

---

## Test T6: The Hubble Tension as a Local Reading (Prediction P7)

- **Fixing Dataset (`FIX`):** SH0ES Cepheid-calibrated supernova host sample (`IS_CALIBRATOR == 1` in `Pantheon+SH0ES.dat`, Riess et al. 2022), fitting and freezing the weighted-mean Type Ia absolute magnitude $M_B^{\rm fixed}$ using the calibrator block of `Pantheon+SH0ES_STAT+SYS.cov`.
- **Testing Dataset (`TEST`):** Pantheon+ Hubble-flow supernovae (`0.023 <= z_HD <= 0.15`, `IS_CALIBRATOR == 0`), partitioned into the 12 equal-area sky regions of a HEALPix $N_{\rm side} = 1$ grid in Galactic coordinates $(l, b)$ (`RING` ordering).
- **Statistic:** Generalized least-squares fit of the 12 regional Hubble constants $\hat{\mathbf{H}}_0 = (\hat{H}_{0,1}, \dots, \hat{H}_{0,12})^T$ using $M_B^{\rm fixed}$ and the full Hubble-flow covariance block $\mathbf{C}_{\rm HF}$, yielding the $12\times 12$ covariance matrix $\mathbf{C}_{H_0}$ and heterogeneity statistic $\chi^2_{\rm het} = (\hat{\mathbf{H}}_0 - \bar{H}_0\mathbf{1})^T \mathbf{C}_{H_0}^{-1} (\hat{\mathbf{H}}_0 - \bar{H}_0\mathbf{1})$ ($\text{dof} = 11$).
- **Pre-Registered Thresholds (Unchanged):**
  - **PASS:** Regional heterogeneity significant at $\ge 3\sigma$ ($p_{\rm het} \le 0.00270$), while all-sky local $\bar{H}_0$ exceeds Planck 2018 $\Lambda\text{CDM}$ ($67.36 \pm 0.54\text{ km s}^{-1}\text{ Mpc}^{-1}$) at $\ge 3\sigma$.
  - **FAIL:** Regional heterogeneity consistent with zero ($p_{\rm het} > 0.32$, i.e. $< 1\sigma$) while all-sky tension remains $\ge 3\sigma$; or a published distance-ladder systematic resolution accepted by the SH0ES team.
  - **INCONCLUSIVE:** Anything else.

---

# 5. Pre-Registered Coincidence Window Tolerances (Section h2 Diagnostic)

With Planck 2018 base $\Lambda\text{CDM}$ parameters ($\omega_b = 0.02237, \omega_c = 0.1200, H_0 = 67.36, \Omega_m = 0.3153, \Omega_\Lambda = 0.6847$), compute the cosmic time span $\Delta t_{\rm coinc}$ during which all three instantaneous shares $\Omega_b(a), \Omega_{\rm dm}(a), \Omega_{\rm de}(a)$ remain simultaneously within:
1. **Criterion H-Abs:** $\max_{i \in \{b, {\rm dm}, {\rm de}\}} |\Omega_i(a) - s_i^{\rm target}| \le 0.05$ ($\pm 5$ percentage points),
2. **Criterion H-Rel:** $\max_{i \in \{b, {\rm dm}, {\rm de}\}} |\Omega_i(a) - s_i^{\rm target}| / s_i^{\rm target} \le 0.10$ ($\pm 10\%$ fractional),
evaluated both for $f_{\rm leak} = 1/6$ ($s^{\rm target} = (1/19, 5/19, 13/19)$) and for the T2-frozen $f_{\rm leak}$.
