---
title: "MULTIVERSE v1: Head-to-Head Bayesian Evidence Comparison Plan (HEAD_TO_HEAD_PLAN.md)"
subtitle: "Supplementary Analysis, Not Pre-Registered — Locked Settings, Package Versions, and Seeds Prior to First Run"
author: "Gregory Mandarano / WickedAI — Executed by Gemini 4 Argon"
date: "2026-10-30"
---

# MULTIVERSE v1: HEAD-TO-HEAD PLAN (`supplementary analysis, not pre-registered`)

> **STATUS LABEL:** **Supplementary analysis, not pre-registered.**
> Stage 2 is finished and frozen (`RESULTS_v5.sha256`). This document locks the settings, exact package versions, likelihood definitions, priors, nested-sampling parameters, and random seeds for the supplementary Bayesian evidence comparison before the first run is executed. It does **not** alter any registered Stage 2 verdict.

---

## 1. Scope & Non-Modification Guarantees

1. **Scope (Background Expansion Only):** This comparison evaluates cosmological background expansion only (`DESI DR2 BAO` with joint Ly$\alpha$ BAO+AP + `Chen, Huang & Wang 2019` compressed CMB distance priors + one supernova compilation per run: `Pantheon+` OR `DES-Dovekie`, never combined). It says nothing about galaxy rotation curves (`T5-A`), dissociative cluster mergers (`T4b`), or regional $H_0$ heterogeneity (`T6`). **The `T5-A` rotation-curve failure and the overall Stage 2 verdict (`MODEL FALSIFIED (FAIL)`) stand regardless of what this background comparison shows.**
2. **Frozen Files Untouched:** No file listed in `PREREG_v4.sha256`, `DATA_MANIFEST.sha256`, or `RESULTS_v5.sha256` will be modified, moved, or overwritten. All new code, chains/samples, logs, and reports are written under `D:\Argon_Code\Ropewalk\head_to_head\`. The frozen likelihood classes in `scripts/cosmology.py` are imported read-only without modification.
3. **Logging & Deviations:** Every action and command is logged with local ISO-8601 timestamps in `head_to_head/ACTIVITY_LOG_H2H.md` (append-only). Any change after `HEAD_TO_HEAD_PLAN.md` is hashed into `HEAD_TO_HEAD_PLAN.sha256` and stamped with OpenTimestamps (`ots stamp`) will be logged in `head_to_head/DEVIATIONS.md` (stating what changed, why, and the expected effect) before the affected run.

---

## 2. Pinned Environment, Exact Package Versions, and Hardware Configuration

- **Workspace & Virtual Environment:** `D:\Argon_Code\Ropewalk\.venv`
- **Python Version:** `3.14.7 (tags/v3.14.7:823f032, Aug 5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)]`
- **Pinned Numerical & Sampling Packages:**
  - `numpy == 2.5.4`
  - `scipy == 1.18.1`
  - `dynesty == 3.1.0`
  - `matplotlib == 3.11.2`
  - `psutil == 7.2.2`
  - `opentimestamps-client == 0.8.0`
- **Hardware & Thread Cap (`GEMINI.md` Rule 5 & Handoff):**
  - Every Python script begins with single-thread BLAS headers (`OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1`) before importing `numpy`, `scipy`, or `dynesty`.
  - Parallel worker pools are capped at `N_CORES = 12` workers (on a 20-physical / 28-logical core CPU, leaving 8 physical / 16 logical threads free) with worker process priority set to `psutil.BELOW_NORMAL_PRIORITY_CLASS`.

---

## 3. Data and Registered `T1-L1` Likelihood

Every run uses the exact registered `T1-L1` background dataset and likelihood (`PREREG.md` §5.1):
1. **DESI DR2 BAO (`lya_mode = 'joint_ap_deciding'`):** `DESIBAOLikelihood(data_dir, lya_mode="joint_ap_deciding")` from `scripts/cosmology.py` — 13 BAO distance ratios across $z_{\rm eff} \in [0.295, 2.33]$, with the $z_{\rm eff} = 2.33$ Ly$\alpha$ block replaced by the joint Ly$\alpha$ BAO+AP measurement of DESI Collaboration (`arXiv:2607.27410`): $D_H(2.33)/r_d = 8.600 \pm 0.066$, $D_M(2.33)/r_d = 39.32 \pm 0.33$, $r = -0.431$.
2. **Compressed CMB Distance Priors (`table = 'lcdm'`, `mode = 'full_3x3'`):** `CMBLikelihood(table="lcdm", mode="full_3x3")` from Chen, Huang & Wang (2019, *JCAP* 02, 028, Table 1 $\Lambda\text{CDM}$):
   $$\boldsymbol{\mu}_{\rm CMB} = \begin{pmatrix} R \\ \ell_A \\ 100\omega_b \end{pmatrix} = \begin{pmatrix} 1.7502 \\ 301.471 \\ 2.236 \end{pmatrix}, \quad \boldsymbol{\sigma}_{\rm CMB} = \begin{pmatrix} 0.0046 \\ 0.090 \\ 0.015 \end{pmatrix}, \quad \mathbf{R}_{\rm CMB} = \begin{pmatrix} 1.00 & 0.46 & -0.66 \\ 0.46 & 1.00 & -0.33 \\ -0.66 & -0.33 & 1.00 \end{pmatrix}. \quad \text{[Established]}$$
3. **Supernova Compilations (One Per Run, Never Combined):**
   - **`Pantheon+`:** `PantheonPlusLikelihood(data_dir)` ($z_{\rm HD} > 0.01$, `IS_CALIBRATOR == 0`, $N = 1590$ SNe, full `STAT+SYS` covariance, analytically marginalized over nuisance offset $M$).
   - **`DES-Dovekie`:** `DESDovekieLikelihood(data_dir)` (`DES-Dovekie_HD.csv` + `STAT+SYS.npz`, $N = 1820$ SNe, analytically marginalized over nuisance offset $M$).
4. **Neutrino Sector:** $\sum m_\nu = 0.06\text{ eV}$ (`N_EFF = 3.044`, 1 massive eigenstate of $0.06\text{ eV}$ with exact Fermi–Dirac phase-space evolution `omega_nu_h2_of_a(a)` + 2 massless species; present-day physical massive-neutrino density $\omega_{\nu,{\rm mass},0} = 0.06 / 93.14 = 6.4419154\times 10^{-4}$ and $\Omega_{\nu,0} = \omega_{\nu,{\rm mass},0} / h^2$). `[Established]`
5. **Log-Likelihood Definition:**
   $$\ln\mathcal{L}(\boldsymbol{\theta}) = -\frac{1}{2}\chi^2_{\rm tot}(\boldsymbol{\theta}) = -\frac{1}{2}\left[\chi^2_{\rm BAO}(\boldsymbol{\theta}) + \chi^2_{\rm CMB}(\boldsymbol{\theta}) + \chi^2_{\rm SN}(\boldsymbol{\theta})\right]. \quad \text{[Established]}$$
   Because the data vectors and covariance matrices are identical across all four models within each `(SN compilation, r_s reading)` cell, the constant Gaussian log-determinant normalization cancels identically in all log Bayes factors $\ln B_{M, \Lambda\text{CDM}} = \ln Z_M - \ln Z_{\Lambda\text{CDM}}$.

---

## 4. Two Sound-Horizon Readings (Both Required)

Both readings of the sound-horizon integral $r_s(z)$ (`COMPARISON_ARGON_vs_REBUILD.md` Finding 1; `DEVIATIONS.md` D3) are implemented and run across the full model grid:

### 4.1 Reading A: Literal Registered `(a5)` Full Sound-Horizon Integral
From `MULTIVERSE_STAGE1_EQUATIONS.md` Equations `(a2)` and `(a5)` (`[Established]`, Assumptions `[A1, A2]`):
$$r_s(z) = \int_z^\infty \frac{c_s(z')}{H(z')}\,dz' = \int_0^{a(z)} \frac{c_s(a)}{a^2 H(a)}\,da, \qquad a(z) = \frac{1}{1 + z}, \qquad c_s(a) = \frac{c}{\sqrt{3\left(1 + \frac{3\omega_b}{4\omega_\gamma}\,a\right)}}, \quad \text{[Established]}$$
where $\omega_\gamma = 2.4728\times 10^{-5}$ and the early-to-late dimensionless expansion rate $E(a) = H(a)/H_0$ follows Equation `(a2)`:
$$a^2\frac{H(a)}{100\text{ km s}^{-1}\text{ Mpc}^{-1}} = \sqrt{\omega_\gamma + a^4\,\omega_\nu(a) + \omega_{bc}\,a + \Omega_{\rm de} h^2 a^4 g(a)}, \quad \text{[Established]}$$
with $\omega_\nu(a) = \text{omega\_nu\_h2\_of\_a}(a)$ (the exact physical density of the 2 massless + 1 massive $0.06\text{ eV}$ neutrino species at scale factor $a$), $\omega_{bc} = \Omega_{bc}h^2$, and $\omega_m = (\Omega_{bc} + \Omega_{\nu,0})h^2 = \omega_{bc} + \omega_{\nu,{\rm mass},0}$ entering $z_*(\omega_b, \omega_m)$ (Hu & Sugiyama 1996) and $z_d(\omega_b, \omega_m)$ (Eisenstein & Hu 1998).
- **Unmodified $r_s(z_*)$ and Calibrated $r_d = r_s(z_d)$:** Under Reading A, $r_s(z_*)$ is evaluated directly from the literal `(a5)` integral with no calibration factor, while the baryon drag scale $r_d$ is calibrated to `CLASS`/`CAMB` (`147.09 Mpc` at Planck 2018 fiducial parameters $\omega_b = 0.02237, \omega_c = 0.1200, \omega_m = 0.02237 + 0.1200 + \omega_{\nu,{\rm mass},0} = 0.14301419$, $h = 0.6736$, $\Lambda\text{CDM}$) via `_DRAG_CALIB_FACTOR_A5 = 147.09 / sound_horizon_rs_a5(z_d_fid, ...)` as specified in Equation `(a5)`.
- **Mandatory Two-Quadrature Validation & Gate `G9-b` Recomputation:**
  1. Compute $r_s(z_*)$ under Reading A using two independent quadratures: (i) 128-node Gauss–Legendre quadrature (`GL128`) on $a \in [0, a_*]$ and (ii) adaptive Gauss–Kronrod quadrature (`scipy.integrate.quad`, `epsabs=1e-12`, `epsrel=1e-12`, `limit=200`). Verify relative agreement $< 10^{-6}$ across fiducial and prior-box test points.
  2. Recompute validation gate `G9-b` under Reading A (fitting flat $\Lambda\text{CDM}$ to the Chen, Huang & Wang 2019 Table 1 $\Lambda\text{CDM}$ $3\times 3$ prior) and log the exact parameter offsets in units of $\sigma$ (expected: `G9-b` `FAIL` with $h$ offset near $0.58\sigma$).

### 4.2 Reading B: `Chen, Huang & Wang (2019)` Early-Universe Form in Frozen Code
Uses the exact frozen functions `sound_horizon_rs_chen`, `r_drag_mpc`, `joint_chi2_cpl`, and `joint_chi2_law1` in `scripts/cosmology.py` ($\omega_r = 1/24185$, with the $0.06\text{ eV}$ neutrino included in $\omega_m a^{-3}$). `[Established]`

---

## 5. Models and Uniform Priors

All four models assume a spatially flat FLRW metric (`Assumption [A1]`), standard General Relativity (`Assumption [A2]`), and the locked v1 Static Form of the dark-matter shadow (`Assumption [A4]`, $Q \equiv 0$, $f_{\rm dm}(a) = a^{-3}$). In all four models, the sampled matter parameter is the baryon-plus-cold-dark-matter share $\Omega_{bc} \equiv \Omega_b + \Omega_{\rm dm}$, with massive neutrinos added separately via $\Omega_{m,{\rm tot}} = \Omega_{bc} + \Omega_{\nu,0} = \Omega_{bc} + \omega_{\nu,{\rm mass},0}/h^2$:

1. **Model 1 — $\Lambda\text{CDM}$ ($d = 3$ free parameters):** `[Established]`
   - Dark energy equation of state: $w(a) = -1$ ($g(a) = 1$).
   - Free parameters & uniform priors:
     $$\Omega_{bc} \sim \mathcal{U}(0.10, 0.50), \qquad h \sim \mathcal{U}(0.50, 0.90), \qquad 100\omega_b \sim \mathcal{U}(1.80, 2.60).$$
   - Prior volume: $V_{\Lambda\text{CDM}} = 0.40 \times 0.40 \times 0.80 = 0.128$.

2. **Model 2 — $\text{CPL}$ ($w_0w_a\text{CDM}$, $d = 5$ free parameters, for context):** `[Established]`
   - Dark energy equation of state (`Equation a4`): $w(a) = w_0 + w_a(1 - a)$, $g_{\rm CPL}(a) = a^{-3(1+w_0+w_a)}\exp[-3w_a(1-a)]$.
   - Free parameters & uniform priors:
     $$\Omega_{bc} \sim \mathcal{U}(0.10, 0.50), \quad h \sim \mathcal{U}(0.50, 0.90), \quad 100\omega_b \sim \mathcal{U}(1.80, 2.60), \quad w_0 \in [-3.0, 1.0], \quad w_a \in [-3.0, 2.0] \text{ with } w_0 + w_a < 0.$$
   - Exact constant-Jacobian prior transform on $\mathcal{P} = \{(w_0, w_a) \in [-3, 1]\times[-3, 2] : w_0 + w_a < 0\}$ (area $A_{\mathcal{P}} = 20 - \frac{1}{2}(3)(3) = 15.5$): for $(u_3, u_4) \in [0, 1]^2$, let $A = 15.5\,u_3$; if $A \le 5$, $w_0 = -3 + A/5$, else $w_0 = 3 - \sqrt{35 - 2A}$; and $w_a = -3 + u_4\min(5.0,\; 3.0 - w_0)$. Because $|\partial(w_0, w_a)/\partial(u_3, u_4)| = 15.5$ everywhere on $[0, 1]^2$, this samples the uniform distribution on $\mathcal{P}$ with 100% prior efficiency and normalized prior density $1/15.5$. (For completeness, we also record the un-renormalized full-rectangle shift $\ln(15.5/20) = -0.254892$ in `results.json`.)

3. **Model 3 — `M1` = Law 1 Unwinding (`Stage 1 d4`, $d = 4$ free parameters):** `[Model Ansatz | Assumptions A3, A8, A9]`
   - Dark energy equation of state (`Equation d4`):
     $$w(a) = -1 + \frac{\gamma_u}{E(a)}, \qquad \frac{d\ln g(a)}{d\ln a} = -\frac{3\gamma_u}{E(a)}, \qquad g(1) = 1. \quad \text{[Model Ansatz]}$$
   - Free parameters & uniform priors:
     $$\Omega_{bc} \sim \mathcal{U}(0.10, 0.50), \qquad h \sim \mathcal{U}(0.50, 0.90), \qquad 100\omega_b \sim \mathcal{U}(1.80, 2.60),$$
     with $\gamma_u \sim \mathcal{U}(0.0, 2.0)$ in the **main runs** (the registered `T1-L1` range) and $\gamma_u \sim \mathcal{U}(0.0, 0.5)$ in the **prior-sensitivity runs**.

4. **Model 4 — `M2` = Structural Version of the Model (`Law 1` + $\Omega_b = 1/19$, $d = 3$ free parameters):** `[Model Ansatz | Assumptions A3, A6, A7, A8, A9]`
   - Combines Law 1 (`Equation d4`, $w(a) = -1 + \gamma_u/E(a)$) with the structural baryon-share identity (`Equation c3`, $\Omega_b = 1/19$), imposed directly inside the likelihood as:
     $$\omega_b = \frac{h^2}{19} \quad \Longleftrightarrow \quad 100\omega_b = \frac{100\,h^2}{19}. \quad \text{[Model Ansatz]}$$
     Here $100\omega_b$ is no longer a free parameter; the derived value $100h^2/19$ is passed directly into $r_d(\omega_b, \omega_m)$, $z_*(\omega_b, \omega_m)$, $r_s(z_*)$, and the $3\times 3$ Chen, Huang & Wang (2019) compressed CMB likelihood $(R, \ell_A, 100\omega_b)$.
   - Free parameters & uniform priors:
     $$\Omega_{bc} \sim \mathcal{U}(0.10, 0.50), \qquad h \sim \mathcal{U}(0.50, 0.90),$$
     with $\gamma_u \sim \mathcal{U}(0.0, 2.0)$ in the **main runs** and $\gamma_u \sim \mathcal{U}(0.0, 0.5)$ in the **prior-sensitivity runs**.

---

## 6. Nested Sampler Settings, Run Grid, and Seeds

1. **Sampler Configuration (`dynesty == 3.1.0`):**
   - Static nested sampler: `dynesty.NestedSampler`
   - Live points: `nlive = 1000`
   - Bounding method: `bound = 'multi'` (multi-ellipsoid bounding)
   - Sampling method: `sample = 'rwalk'` (random-walk sampling)
   - Stopping criterion: `dlogz = 0.01`
2. **Fixed Random Seeds:**
   - Every run in the 24-run grid is executed across **3 independent fixed seeds**:
     $$\texttt{SEEDS} = \left[20261030,\; 20261031,\; 20261032\right],$$
     passed to `dynesty.NestedSampler` via `rstate = np.random.default_rng(seed)`.
3. **Complete Run Grid (24 Runs $\times$ 3 Seeds = 72 Nested-Sampling Runs):**
   - **16 Main Runs:** 4 models ($\Lambda\text{CDM}$, $\text{CPL}$, $\text{M1}[\gamma_u \in [0, 2]]$, $\text{M2}[\gamma_u \in [0, 2]]$) $\times$ 2 SN compilations (`Pantheon+`, `DES-Dovekie`) $\times$ 2 sound-horizon readings (`Reading A`, `Reading B`).
   - **8 Prior-Sensitivity Runs:** 2 models ($\text{M1}[\gamma_u \in [0, 0.5]]$, $\text{M2}[\gamma_u \in [0, 0.5]]$) $\times$ 2 SN compilations (`Pantheon+`, `DES-Dovekie`) $\times$ 2 sound-horizon readings (`Reading A`, `Reading B`).
4. **Pre-Run $\Lambda\text{CDM}$ $\chi^2_{\min}$ Sanity Check:**
   - Before executing the full grid, verify on the Reading B $\Lambda\text{CDM}$ nested-sampling runs that the best-fit $\chi^2_{\min}$ found by `dynesty` matches the Stage 2 $\Lambda\text{CDM}$ $\chi^2_{\min}$ (`1405.343634` for `Pantheon+`, `1650.961491` for `DES-Dovekie`, from `results/part9_cosmology_results.json`) to within `0.1`, and log the exact comparison.
   - Note on parameter equivalence for $\chi^2_{\min}$: Stage 2 sampled $\Omega_{m,{\rm tot}} \in [0.1, 0.6]$, whereas this comparison samples $\Omega_{bc} \in [0.1, 0.5]$ with $\Omega_{m,{\rm tot}} = \Omega_{bc} + \Omega_{\nu,0}$. Because the best-fit $\Omega_{bc} \approx 0.301$ lies deep in the interior of both uniform prior boxes, the global $\chi^2_{\min}$ is identical.

---

## 7. Evidence Aggregation, Uncertainties, and Interpretation Scale

For each of the 24 runs across its 3 seeds $s \in \{1, 2, 3\}$:
1. **Log Evidence and Uncertainty Rule:**
   $$\overline{\ln Z} = \frac{1}{3}\sum_{s=1}^3 \ln Z_s, \qquad \sigma_{\rm dyn} = \sqrt{\frac{1}{3}\sum_{s=1}^3 \sigma_{\ln Z, {\rm dyn}, s}^2}, \qquad \sigma_{\rm scatter} = \sqrt{\frac{1}{2}\sum_{s=1}^3 \left(\ln Z_s - \overline{\ln Z}\right)^2}, \quad \text{[Established]}$$
   $$\sigma_{\ln Z} = \max\!\left(\sigma_{\rm dyn},\; \sigma_{\rm scatter}\right). \quad \text{[Established]}$$
   Both $\sigma_{\rm dyn}$ and $\sigma_{\rm scatter}$ are reported alongside $\sigma_{\ln Z}$, and the larger of the two ($\sigma_{\ln Z}$) is used in all Bayes-factor uncertainties.
2. **Log Bayes Factor Relative to $\Lambda\text{CDM}$ (Within Each SN Compilation and $r_s$ Reading):**
   $$\ln B_{M, \Lambda\text{CDM}} = \overline{\ln Z}_M - \overline{\ln Z}_{\Lambda\text{CDM}}, \qquad \sigma_{\ln B} = \sqrt{\sigma_{\ln Z, M}^2 + \sigma_{\ln Z, \Lambda\text{CDM}}^2}. \quad \text{[Established]}$$
   Positive $\ln B_{M, \Lambda\text{CDM}} > 0$ means model $M$ is favoured over $\Lambda\text{CDM}$; negative $\ln B_{M, \Lambda\text{CDM}} < 0$ means $\Lambda\text{CDM}$ is favoured over model $M$.
3. **Jeffreys / Kass–Raftery Interpretation Scale (`ARGON_HEAD_TO_HEAD_HANDOFF.txt` Line 69):** `[Established]`
   - $|\ln B| < 1.0$: **Inconclusive** (no worth-mentioning preference)
   - $1.0 \le |\ln B| < 2.5$: **Weak** evidence for the favoured model
   - $2.5 \le |\ln B| \le 5.0$: **Moderate** evidence for the favoured model
   - $|\ln B| > 5.0$: **Strong** evidence for the favoured model
4. **Deliverables & Final Freeze:**
   - Write full report to `head_to_head/HEAD_TO_HEAD_RESULTS.md` (with the required tables, prior-sensitivity table, plain-language Jeffreys/Kass–Raftery lines, validation results, scope statement, and `"supplementary analysis, not pre-registered"` header), save `head_to_head/results.json`, all 72 chains/posterior sample archives (`head_to_head/chains/`), and run logs (`head_to_head/logs/`).
   - Hash every output, every new code file, and `HEAD_TO_HEAD_RESULTS.md` into `HEAD_TO_HEAD_RESULTS_v1.sha256` and stamp it with OpenTimestamps (`ots stamp`).
