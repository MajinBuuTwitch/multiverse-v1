# Stage 1 Cold Review Response (`REVIEW_RESPONSE.md`)

**Date:** 2026-10-30  
**Workspace:** `D:\Argon_Code\Ropewalk`  
**Review Answered:** `REVIEW_COLD.md` (33 findings: 4 `BLOCKER`, 15 `MAJOR`, 14 `MINOR`)  
**Summary of Resolutions:** **33 `FIXED`, 0 `DISPUTED`, 0 `DEFERRED`**  
**Pre-Data Compliance:** All revisions were completed before downloading any dataset or writing any Stage 2 analysis code. Previous v1 Stage 1 files are preserved in `D:\Argon_Code\Ropewalk\_TRASH\*_v1.md`.

---

## HEADLINE REPORT (Per Instruction M6): New Lower Bound on $\tau_{\rm lag}$ from Corrected Bullet Cluster Dynamical Age

When the Bullet Cluster (`1E 0657-558`) time since pericenter is taken directly from the cited dynamical MCMAC analysis of **Dawson (2013, ApJ 772, 131, Table 2)** rather than the early bow-shock propagation estimate of Markevitch et al. (2002, ApJ 567, L27; $0.1\text{–}0.2\text{ Gyr}$), the Bullet Cluster age is **$t_p = 0.40 \pm 0.10\text{ Gyr}$** (with the temporal prior; **$0.60^{+0.50}_{-0.30}\text{ Gyr}$** with the default prior). Because the Bullet Cluster's lensing mass sits on the collisionless galaxies rather than the X-ray gas, **requiring $t_p({\rm Bullet}) < \tau_{\rm lag}$ raises the lower bound on the inter-string crossing delay $\tau_{\rm lag}$ from $150\text{ Myr}$ to $400\text{–}600\text{ Myr}$** ($300\text{ Myr}$ at the $1\sigma$ lower edge of Dawson's temporal-prior age). Both the Dawson (2013) dynamical lower bound ($\tau_{\rm lag} \ge 400\text{ Myr}$) and the Markevitch et al. (2002) shock lower bound ($\tau_{\rm lag} \ge 150\text{ Myr}$) are now registered in `PREREG.md` §5.4–§5.5 and `MULTIVERSE_STAGE1_EQUATIONS.md` §8.4.

---

## 1. Resolution of All BLOCKER Findings (`B1–B4`)

### `B1` — Coefficient Error in the 1D Radial Gaussian Enclosed-Mass Kernel $\mathcal{F}_\sigma(r, r')$
- **Status:** **`FIXED`**
- **What Changed & Where:**
  1. In `MULTIVERSE_STAGE1_EQUATIONS.md` §7 `(f3)`, `STAGE1_PART3_SECTIONS_EFI.md` §`(f3)`, and `PREREG.md` §5.6, the coefficient of the second (exponential) bracket in $\mathcal{F}_\sigma(r, r')$ was corrected from $\sqrt{\frac{2}{\pi}}$ to **$\frac{1}{\sqrt{2\pi}}$**:
     $$\mathcal{F}_\sigma(r, r') = \frac{1}{2}\left[\operatorname{erf}\!\left(\frac{r + r'}{\sqrt{2}\,\sigma_{\rm ref}}\right) + \operatorname{erf}\!\left(\frac{r - r'}{\sqrt{2}\,\sigma_{\rm ref}}\right)\right] - \frac{1}{\sqrt{2\pi}}\,\frac{\sigma_{\rm ref}}{r'}\left[\exp\!\left(-\frac{(r - r')^2}{2\sigma_{\rm ref}^2}\right) - \exp\!\left(-\frac{(r + r')^2}{2\sigma_{\rm ref}^2}\right)\right].$$
  2. Verified the corrected formula analytically ($r' \to 0^+$ Taylor limit recovers $\mathcal{F}_\sigma(r, 0) = \operatorname{erf}(\frac{r}{\sqrt{2}\sigma_{\rm ref}}) - \sqrt{\frac{2}{\pi}}\frac{r}{\sigma_{\rm ref}}e^{-r^2/(2\sigma_{\rm ref}^2)} > 0$) and numerically against a direct 500,000-sample 3D Monte Carlo simulation (`SEED = 20261030`) of a Gaussian-smeared spherical shell across four test configurations (`(1.0, 1.0, 1.0)`, `(2.0, 1.0, 1.5)`, `(0.5, 2.0, 1.0)`, `(3.0, 0.5, 2.0)`). All four points agree within statistical uncertainty (`-0.09 SE`, `-0.80 SE`, `-0.07 SE`, `+2.16 SE`), and the verification table is embedded directly in `MULTIVERSE_STAGE1_EQUATIONS.md` §7 `(f3)` and `STAGE1_PART3_SECTIONS_EFI.md` §`(f3)`.
  3. Added mandatory Validation Gate **`G9-d`** in `PREREG.md` §2 requiring the coded $\mathcal{F}_\sigma(r, r')$ to match `scipy.stats.ncx2.cdf((r/sigma)**2, df=3, nc=(rp/sigma)**2)` to absolute tolerance $< 10^{-10}$ before any SPARC data are loaded.

---

### `B2` — Opposite Sign Conventions for the T4a Projected Offset $\Delta_{SI}^{\parallel}$
- **Status:** **`FIXED`**
- **What Changed & Where:**
  - In `MULTIVERSE_STAGE1_EQUATIONS.md` §6 `(e6 & e7)`, `STAGE1_PART3_SECTIONS_EFI.md` §`(e6 & e7)`, and `PREREG.md` §5.4, the projected offset along the gas-to-stars unit vector $\hat{\mathbf{s}}_{G\to S} \equiv \frac{\mathbf{x}_S - \mathbf{x}_G}{|\mathbf{x}_S - \mathbf{x}_G|}$ ($= +\hat{\mathbf{x}}$ in 1D where $\delta_{SG} = x_G - x_S = -|\delta_{SG}| < 0$, $\delta_{SI} = x_I - x_S$, and $\beta = \delta_{SI}/\delta_{SG}$) is now written identically everywhere as:
    $$\Delta_{SI}^{\parallel} \equiv \left(\mathbf{x}_I - \mathbf{x}_S\right)\cdot\hat{\mathbf{s}}_{G\to S} = \delta_{SI} = \delta_{SG}\,\beta = -\left|\delta_{SG}\right|\beta,$$
    so $\Delta_{SI}^{\parallel} > 0 \iff \delta_{SI} > 0 \iff \beta < 0$ (dark mass ahead of stars, away from gas) with zero sign ambiguity across all equations, text, and pre-registered statistics.

---

### `B3` — Unresolved Model Choice (`A13a` vs. `A13b`), Sample Size $N = 1$, and Multiple Statistics in Test T4a
- **Status:** **`FIXED`**
- **What Changed & Where:**
  1. **Physical Selection of `A13b` Over `A13a`:** In `MULTIVERSE_STAGE1_EQUATIONS.md` §6 `(e6 & e7)`, `STAGE1_PART3_SECTIONS_EFI.md` §`(e6 & e7)`, `ASSUMPTIONS.md` `[A13b]`, and `PREREG.md` §5.4, we selected **Model `A13b` (Symmetric Harmonic Core Passage, $x_S(t) = \frac{v_p}{\omega_0}\sin(\omega_0 t)$)** on physical grounds: collisionless galaxies move in a conservative cluster gravitational potential that accelerates them during pre-pericenter infall ($\ddot{x}_S > 0$ for $t' < 0$) and decelerates them after pericenter ($\ddot{x}_S < 0$ for $t' > 0$); assuming constant pre-pericenter speed (`A13a`) violates conservation of mechanical energy. Under `A13b`, $\Delta\tilde{x}_S(T; \tau_{\rm lag}) \approx \frac{1}{6}\omega_0^2 v_p\tau_{\rm lag}^2(3T - 2\tau_{\rm lag})$ is **negative (behind the stars)** for $0 < T < \frac{2}{3}\tau_{\rm lag}$ and positive only for $\frac{2}{3}\tau_{\rm lag} < T \le \tau_{\rm lag}$.
  2. **Single Statistic & Unconditional Bullet Cluster Exclusion:** Registered the **inverse-variance-weighted mean** of $\Delta_{SI}^{\parallel}$ as the single statistic, with the Bullet Cluster (`1E 0657-558`) unconditionally excluded from the test sample per Rule G2.
  3. **T4a Moved to `EXPLORATORY`:** Because excluding the Bullet Cluster leaves only $N = 1$ system (`Abell 2744`, $t_p = 0.15 \pm 0.05\text{ Gyr}$) below the $150\text{ Myr}$ age cut (fewer than the minimum $N_{\rm min} = 3$ needed for a statistical test, and lying in the $T < \frac{2}{3}\tau_{\rm lag}$ negative-offset regime under Dawson 2013's Bullet Cluster lower bound $\tau_{\rm lag} \ge 400\text{ Myr}$), **Test T4a is moved to `EXPLORATORY (Insufficient Independent Young Mergers, N = 1)`** in `PREREG.md` §3.1 and §5.4.

---

### `B4` — Test T1 (`w0 > -1`) Was Already Known to Pass and Disconnected from the Derived Unwinding Curve $w(a) = -1 + \gamma_u/E(a)$
- **Status:** **`FIXED`**
- **What Changed & Where:**
  1. **Primary Test `T1-L1` Registered:** In `PREREG.md` §3.1 & §5.1 and `MULTIVERSE_STAGE1_EQUATIONS.md` §5 `(d4 & d5)` & §8.4, we registered **Test `T1-L1`** as the **Primary Dark-Energy Pillar Test**: a direct MCMC fit of the model's derived 1-parameter uncoupled unwinding law $w(a) = -1 + \frac{\gamma_u}{E(a)}$ ($\gamma_u \equiv \frac{n\Gamma_u}{3H_0} \ge 0$, which predicts $w_0 = -1 + \gamma_u$ and tangent $w_a = -\frac{3}{2}\gamma_u[\Omega_m + \gamma_u(1 - \Omega_m)]$) to DESI DR2 BAO (joint Ly$\alpha$ BAO+AP) + Planck 2018 compressed CMB prior + SNe (`Pantheon+` and `DES-Dovekie` separately).
  2. **Fixed Thresholds & Explicit Forecast:** `T1-L1` passes only if in both SN runs $\Delta\chi^2_{\min}(\text{Law 1} - \Lambda\text{CDM}) \le -4.0$ **and** $\Delta\chi^2_{\min}(\text{Law 1} - w_0w_a\text{CDM}) \le +4.0$, and fails if $\Delta\chi^2_{\min}(\text{Law 1} - w_0w_a\text{CDM}) > +9.0$ ($> 3\sigma$ rejection for $\Delta\text{dof} = 1$) or $\Delta\chi^2_{\min}(\text{Law 1} - \Lambda\text{CDM}) > -1.0$. We state plainly next to `T1-L1` that it is **forecast to FAIL / be disfavored at $\sim 2.6\text{–}3.5\sigma$** because Law 1 predicts $w_a \approx -0.102$ at $w_0 = -0.84$ vs. DESI's $w_a \approx -0.62$ to $-0.86$.
  3. **Sign Check Demoted & Tail Convention Fixed:** The unconstrained CPL check $w_0 > -1$ is retained as **Secondary Check `T1-Sign`** (explicitly labeled as a known-before-registration pass that cannot rescue a failure of `T1-L1`), with the one-sided $95\%$ posterior tail $P(w_0 > -1 \mid \text{data}) \ge 0.95$ ($z \ge 1.645$) and two-sided $2\sigma$ tail ($P \ge 0.9772, z \ge 2.0$) distinguished explicitly in `PREREG.md` §2 (G7) and §5.1.

---

## 2. Resolution of All MAJOR Findings (`M1–M15`)

### `M1` — Test T2 Algebraic Cancellation of $f_{\rm leak}$, $\Omega_{bc}$ vs. $\Omega_\nu$, and Planck Overlap Correlation
- **Status:** **`FIXED`**
- **What Changed & Where:**
  1. **Renamed T2 & Stated Algebraic Identity:** In `MULTIVERSE_STAGE1_EQUATIONS.md` §4 `(c4)`, `STAGE1_PART1_SECTIONS_ABC.md` §`(c4)`, and `PREREG.md` §5.2, T2 is titled **"Test T2: The Leak and the Dark-to-Ordinary Ratio ($\Omega_b = 1/19$ Algebraic Identity Test, $f_{\rm leak}$)"**, stating explicitly that $\mathcal{R}_{\rm pred} = 19\Omega_{bc} - 1 = \mathcal{R}_{\rm true} \iff \Omega_b = 1/19$ because $f_{\rm leak}$ cancels out of $\mathcal{R}_{\rm pred}$.
  2. **Explicit Exclusion of $\Omega_{\nu,0}$:** Defined $\Omega_{bc} \equiv \Omega_b + \Omega_{\rm dm} = \Omega_{m,{\rm tot}} - \Omega_{\nu,0}$ in `MULTIVERSE_STAGE1_EQUATIONS.md` §1 & §4, `ASSUMPTIONS.md` `[A3]`, and `PREREG.md` §5.2 so massive neutrinos ($\Omega_{\nu,0} \approx 0.00142$, shifting $19\Omega_m$ by $+0.027 \approx 0.42\sigma_{\rm Planck}$) never bias $f_{\rm leak}$ or $\mathcal{R}_{\rm pred}$.
  3. **Registered Both `T2-A` and Self-Consistent `T2-B`:** Registered `T2-A` (the locked v1.0.1 $w_0w_a\text{CDM}$ expansion fit) and **`T2-B`** (direct self-consistent fit imposing $\omega_b = h^2/19$ and $\Omega_{\rm dm} = \frac{6}{19}(1 - f_{\rm leak})$ inside the likelihood, failing if $|\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm Planck}| > 2\sigma_{\rm comb}$ or $\Delta\chi^2_{\min}(\text{T2-B} - w_0w_a\text{CDM}) > 9.0$) in `PREREG.md` §5.2.
  4. **Included Planck $(R, \ell_A)$–$(\omega_c/\omega_b)$ Overlap Correlation:** Added $\sigma_{\rm comb}^{\rm corr} = \sqrt{(19\sigma_{\Omega_{bc}})^2 + \sigma_{\rm Planck}^2 - 2\rho_{\rm overlap}(19\sigma_{\Omega_{bc}})\sigma_{\rm Planck}}$ in `PREREG.md` §5.2 and `ASSUMPTIONS.md` `[A18]`, stating the explicit forecast (**FAIL at $\sim 3.5\text{–}3.6\sigma$**).

---

### `M2` — Parameter-Free Prediction $\Omega_b = 1/19$ Is Already Falsified at $3.9\sigma$ and Implies $H_0 \approx 65.2\text{ km s}^{-1}\text{ Mpc}^{-1}$
- **Status:** **`FIXED`**
- **What Changed & Where:**
  - In `MULTIVERSE_STAGE1_EQUATIONS.md` §4 `(c4)` & §8.4, `ASSUMPTIONS.md` `[A7]`, and `PREREG.md` §3.1 & §5.2, registered two explicit parameter-free tests of the $1:6:12$ strand count:
    1. **Test `T2-N1` (Direct Baryon Share Test):** $\Omega_b^{\rm model} = 1/19 = 0.052632$ vs. Planck 2018 $\Omega_b = 0.04930 \pm 0.00086$ (**$+3.87\sigma$ tension, Forecast & Result: FAIL**).
    2. **Test `T2-N2` (Implied Hubble Constant Test):** $H_0^{\rm pred} = 100\sqrt{19\omega_b}\text{ km s}^{-1}\text{ Mpc}^{-1} = 65.19 \pm 0.22$ (Planck $\omega_b$), $64.92 \pm 0.81$ (DESI/LUNA BBN $\omega_b$), and $64.15 \pm 0.28$ (Cooke+18 BBN $\omega_b$) vs. Planck $\Lambda\text{CDM}$ $H_0 = 67.36 \pm 0.54$ (**$3.7\sigma$ tension**) and SH0ES $73.04 \pm 1.04$ (**$7.4\sigma$ tension, Forecast & Result: FAIL**).

---

### `M3` — Saturation Cap Theorem ($g_{\rm obs}/g_{\rm bar} \le 6.0$) Guarantees Failure on Low-Surface-Brightness SPARC Galaxies in Test T5
- **Status:** **`FIXED`**
- **What Changed & Where:**
  - In `MULTIVERSE_STAGE1_EQUATIONS.md` §7 `(f3)` & §8.4, `STAGE1_PART3_SECTIONS_EFI.md` §`(f3)`, `ASSUMPTIONS.md` `[A15]`, and `PREREG.md` §5.6, kept the T5 thresholds unchanged, stated plainly that the diffusive ceiling $g_{\rm obs}/g_{\rm bar} \le 1 + 6(1 - f_{\rm leak}) \approx 6.0$ (violated by the empirical RAR below $g_{\rm bar}^{\rm cap} = 3.99\times 10^{-12}\text{ m s}^{-2}$ at $f_{\rm leak} = 1/6$ or $3.71\times 10^{-12}\text{ m s}^{-2}$ at $\mathcal{R} = 5.20$) **makes a full T5 PASS very unlikely (Forecast: FAIL)**, and registered the fraction of held-out radial points and galaxies with $g_{\rm bar} < g_{\rm bar}^{\rm cap}$ (plus $\chi^2_{\rm red}$ stratified by surface brightness) as a mandatory diagnostic.

---

### `M4` — Under-Specified Numerical Procedure for Test T5 ($dM_b(r')$ Construction, $r_{\max}$ Truncation, Error Model, Optimizer, and ASCII Sort)
- **Status:** **`FIXED`**
- **What Changed & Where:**
  1. In `PREREG.md` §5.6 and `ASSUMPTIONS.md` `[A15]` & `[A19]`, specified the exact numerical recipe for T5:
     - **Monotonic Non-Negative Shell Construction:** $M_b^{\rm mono}(< r_j) = \max_{1 \le m \le j}(0, r_m v_{\rm bar}^2(r_m)/G)$ so every shell mass $\Delta M_{b,j} \ge 0$ is non-negative;
     - **Quadrature & Tail Continuation:** 400-point PCHIP-interpolated interior grid on $[0, r_{\max}]$ plus a 100-point exponential disk tail $\Sigma_{\rm tail}(r') = \Sigma_b(r_{\max})e^{-(r'-r_{\max})/R_d}$ from $r_{\max}$ to $r_{\max} + 5\sigma_{\rm ref}$;
     - **Velocity Uncertainties:** SPARC `errV` column only (zero distance/inclination nuisance parameters);
     - **Global Optimizer:** 200-point log grid scan over $[0.1, 100]\text{ kpc}$ (`T5-A`) or $[0.05, 50]$ (`T5-B`) followed by `scipy.optimize.minimize_scalar(..., method='bounded', options={'xatol': 1e-5})`;
     - **Sort Rule:** Python byte-wise ASCII `sorted()` on `gal_id.strip()`.
  2. In `MULTIVERSE_STAGE1_EQUATIONS.md` §9 item 4, corrected the $\sigma_{\rm ref} \to 0^+$ limit statement to read $M_{\rm sh}(< r) \to 6(1 - f_{\rm leak})M_b(< r)$ (and in the spherical approximation (f1), $v_c^2(r) \to [1 + 6(1 - f_{\rm leak})]G M_b(< r)/r$).

---

### `M5` — Inconsistent Velocity-Extrapolation Rule Between Galaxy Clusters (`e3`) and Galaxies (`f3`/`f4`)
- **Status:** **`FIXED`**
- **What Changed & Where:**
  - In `MULTIVERSE_STAGE1_EQUATIONS.md` §6 `(e1–e5)` & §7 `(f4)`, `STAGE1_PART3_SECTIONS_EFI.md` §`(e2–e4)` & §`(f4)`, and `ASSUMPTIONS.md` `[A12]` & `[A16]`, replaced per-particle velocity extrapolation with **one unified coarse-grained component velocity rule applied identically to clusters and galaxies**: because the inter-string kernel $K_\sigma$ smooths over scale $\sigma_{\rm ref}$, linear velocity extrapolation over $\tau_{\rm lag}$ acts on the **center-of-mass bulk velocity $\mathbf{V}_{{\rm bulk},c}(t - \tau_{\rm lag})$ of each macroscopically coherent baryonic component $c$** smoothed on scale $\sigma_{\rm ref}$, $\tilde{\rho}_{b,c}(\mathbf{y}, t) = \rho_{b,c}(\mathbf{y} - \mathbf{V}_{{\rm bulk},c}(t - \tau_{\rm lag})\tau_{\rm lag}, t - \tau_{\rm lag})$. For a colliding cluster subcluster component $c \in \{S, G\}$, this shifts the component centroid by $\mathbf{V}_{{\rm bulk},c}\tau_{\rm lag}$ without a $\sigma_v\tau_{\rm lag} \sim 150\text{–}600\text{ kpc}$ internal velocity-dispersion blow-up; for an isolated galaxy in its center-of-mass rest frame ($\mathbf{V}_{\rm bulk} = \mathbf{0}, \partial\rho_b/\partial t = 0$), it yields $\tilde{\rho}_b(\mathbf{x}) = \rho_b(\mathbf{x})$ identically. Also corrected the orbital timescale numbers ($r/v_c = 14.7\text{ Myr}$ at $r = 3\text{ kpc}, v_c = 200\text{ km s}^{-1}$, and $195.6\text{ Myr}$ at $r = 30\text{ kpc}, v_c = 150\text{ km s}^{-1}$).

---

### `M6` — Incorrectly Cited Cluster Merger Ages, Ad-Hoc Split Swap, and Missing Position Catalog Sources in Test T4b
- **Status:** **`FIXED`**
- **What Changed & Where:**
  1. **Updated Bullet Cluster & Musket Ball Ages to Match Cited Sources:** In `PREREG.md` §5.5 and at the top of this `REVIEW_RESPONSE.md`, updated `1E 0657-558` (Bullet Cluster) to **Dawson (2013, ApJ 772, 131, Table 2)**: $t_p = 0.40 \pm 0.10\text{ Gyr}$ (temporal prior; $0.60^{+0.50}_{-0.30}\text{ Gyr}$ default prior) alongside Markevitch et al. (2002)'s $0.15 \pm 0.05\text{ Gyr}$ bow-shock estimate (reporting the resulting new lower bound $\tau_{\rm lag} \ge 400\text{–}600\text{ Myr}$ at the top of `REVIEW_RESPONSE.md`), and updated `DLSCL J0916.2+2951` (Musket Ball) to **Dawson (2013, Table 2)**: $t_p = 1.10^{+1.30}_{-0.40}\text{ Gyr}$ (symmetric approximation $1.10 \pm 0.65\text{ Gyr}$).
  2. **Deterministic Byte-Wise ASCII Sort (Zero Manual Swap):** Specified Python byte-wise ASCII `sorted()` on `Catalog Designation` in `PREREG.md` §5.5 (`'1E 0657-558'` < `'ACT-CL J0102-4915'` < `'Abell 1240'` < $\dots$), under which the Bullet Cluster sits naturally at position 1 without any swap.
  3. **Explicit Position Catalog Sources & Subcluster/Age-Uncertainty Rules:** Added a dedicated column in the `PREREG.md` §5.5 table naming the exact $(S, G, I)$ position source for every one of the 16 clusters, specified the primary "bullet" subcluster rule for bimodal mergers, and registered 10,000-draw Monte Carlo age-posterior weighting $P_i(t_p < \tau_{\rm lag})$ alongside the point-estimate step.

---

### `M7` — Potential Double-Counting of DESI DR2 Ly$\alpha$ BAO at $z_{\rm eff} = 2.33$ in Test T1 and Test T2
- **Status:** **`FIXED`**
- **What Changed & Where:**
  - In `PREREG.md` §2 (G6), §5.1, and §5.2, specified that the $z_{\rm eff} = 2.33$ Ly$\alpha$ row in `CobayaSampler/bao_data/desi_bao_dr2` is **removed and replaced** by the joint Ly$\alpha$ BAO + Alcock–Paczyński vector of Cuceu et al. (2025, arXiv:2607.27410): $D_H(2.33)/r_d = 8.600 \pm 0.066, D_M(2.33)/r_d = 39.32 \pm 0.33, r = -0.43$.

---

### `M8` — Unspecified $z_*$ and $z_d$ Fitting Formulas and Misattributed Chen et al. (2019) Table 1 Prior Vector
- **Status:** **`FIXED`**
- **What Changed & Where:**
  1. In `MULTIVERSE_STAGE1_EQUATIONS.md` §2 `(a5)`, wrote out the exact Hu & Sugiyama (1996, ApJ 471, 542) $z_*$ fitting formula (with coefficient $0.0783$) and Eisenstein & Hu (1998, ApJ 496, 605) $z_d$ formula, together with numerical $r_s(z)$ quadrature.
  2. In `MULTIVERSE_STAGE1_EQUATIONS.md` §2 `(a5)` and `PREREG.md` §5.1, correctly labeled $(1.7502, 301.471, 2.236)$ as the Chen, Huang & Wang (2019) Table 1 **$\Lambda\text{CDM}$** column and registered their Table 1 **$w\text{CDM}$** column $(1.7493, 301.462, 2.239)$ as a mandatory cross-check.
  3. In `PREREG.md` §2 (G9), added mandatory Validation Gates **`G9-b`** (reproducing Chen et al. Table 2 $\Lambda\text{CDM}$ posteriors from $(R, \ell_A, 100\omega_b)$ to within $0.3\sigma$) and **`G9-c`** (reproducing Popovic et al. 2025 DESI DR2 + CMB + DES-Dovekie $w_0w_a\text{CDM}$ $(w_0, w_a)$ posterior to within $0.3\sigma$).

---

### `M9` — Marginal vs. Conditional $(R, \ell_A)$ Covariance Matrix and Outdated BBN Prior in Test T2
- **Status:** **`FIXED`**
- **What Changed & Where:**
  - In `MULTIVERSE_STAGE1_EQUATIONS.md` §2 `(a5)` and `PREREG.md` §5.2, replaced the marginal $2\times 2$ $(R, \ell_A)$ block with the **exact conditional Gaussian likelihood $(R, \ell_A \mid 100\omega_b)$** derived from Chen et al. (2019)'s $3\times 3$ covariance matrix ($\boldsymbol{\mu}_{R,\ell_A\mid\omega_b} = \boldsymbol{\mu}_{1} + \mathbf{C}_{12}C_{22}^{-1}(100\omega_b - 2.236)$, $\mathbf{C}_{R,\ell_A\mid\omega_b} = \mathbf{C}_{11} - \mathbf{C}_{12}C_{22}^{-1}\mathbf{C}_{21}$) so Planck's marginal $\omega_b$ prior is excluded while the $r_s(z_*)$ correlation with $\omega_b$ ($r_{R,\omega_b} = -0.66, r_{\ell_A,\omega_b} = -0.33$) is preserved. Registered both the locked v1.0.1 Cooke et al. (2018) BBN prior ($100\omega_b = 2.166 \pm 0.019$) and the post-LUNA / DESI DR2 BBN prior ($100\omega_b = 2.218 \pm 0.055$).

---

### `M10` — No Overall Model-Level Decision Rule, No Multiple-Testing Correction, Asymmetric Dual-Run Logic, and G8 Escape Hatch
- **Status:** **`FIXED`**
- **What Changed & Where:**
  - In `PREREG.md` §2 (G8) and §3.1–§3.3:
    1. **Model-Level Decision Rule:** Designated the four primary pillar tests (`T1-L1`, `T2`, `T4b`, `T5-A`) and registered the rule: *"The pre-registered v1 Mandarano Model is falsified overall if any one of the four primary pillar tests ends in `FAIL`."*
    2. **Multiple-Testing Control:** Designated `T5-A` as primary (with a $2\times$ Bonferroni penalty on `T5-B`) and required any claimed `PASS` across all $K$ scored tests to survive the **Holm–Bonferroni step-down procedure** at $\alpha_{\rm FWE} = 0.05$.
    3. **Symmetric Dual-Run Combination:** Enforced symmetric `AND` logic across `Pantheon+` and `DES-Dovekie` (`PASS` if both pass; `FAIL` if both fail; `INCONCLUSIVE (Compilation Disagreement)` if one passes and one fails).
    4. **Removed Post-Unblinding G8 Escape Hatch:** Restricted `INCONCLUSIVE` strictly to the four mechanical numerical triggers in `PREREG.md` §2 (G8).

---

### `M11` — Duplicate Files `MULTIVERSE_STAGE1_EQUATIONS.md` and `EQUATIONS.md`
- **Status:** **`FIXED`**
- **What Changed & Where:**
  - Designated `D:\Argon_Code\Ropewalk\MULTIVERSE_STAGE1_EQUATIONS.md` as the **single governing equation file**, moved `D:\Argon_Code\Ropewalk\EQUATIONS.md` to `D:\Argon_Code\Ropewalk\_TRASH\EQUATIONS_v1.md`, and logged the move in `ACTIVITY_LOG.md`.

---

### `M12` — Incomplete File Coverage in `PREREG.sha256` and Need for External Timestamp
- **Status:** **`FIXED`**
- **What Changed & Where:**
  - Moved the old `PREREG.sha256` to `_TRASH\PREREG_v1.sha256` and generated `D:\Argon_Code\Ropewalk\PREREG_v2.sha256` hashing **every** Stage 1 and starter file in `D:\Argon_Code\Ropewalk` (`00_READ_FIRST.txt`, `MULTIVERSE_ARGON_HANDOFF.txt`, `SESSION_BOOTSTRAP_HANDOFF.md`, `MULTIVERSE_TESTS_v1.md`, `MULTIVERSE_EQUATION_SHEET_v1.md`, `MULTIVERSE_DATASETS_v1.md`, `MULTIVERSE_PREDICTIONS_PAPER_v1.md`, `GEMINI.md`, `REVIEW_COLD.md`, `REVIEW_RESPONSE.md`, `MULTIVERSE_STAGE1_EQUATIONS.md`, `ASSUMPTIONS.md`, `PREREG.md`, `STAGE1_PART1_SECTIONS_ABC.md`, `STAGE1_PART2_SECTIONS_DGH.md`, `STAGE1_PART3_SECTIONS_EFI.md`, and `ACTIVITY_LOG.md`) for Gregory to upload to Google Drive as the external timestamp.

---

### `M13` — False "Uncoupled Non-Phantom Wedge" Theorem ($-(1 + w_0) \le w_a \le 0$)
- **Status:** **`FIXED`**
- **What Changed & Where:**
  - In `MULTIVERSE_STAGE1_EQUATIONS.md` §5 `(d4 & d5)`, `STAGE1_PART2_SECTIONS_DGH.md` §`(d4 & d5)`, and `ASSUMPTIONS.md` `[A9]`, removed the false claim that any smooth curve with $w(a) \ge -1$ has tangent $w_a \equiv -w'(1)$ confined to $-(1 + w_0) \le w_a \le 0$, and included the exact counterexamples: Law 3 with $\beta > 1$ ($w(a) = -1 + (1 + w_0)a^\beta \ge -1$ everywhere, but tangent $w_0 + w_a = -1 - (\beta - 1)(1 + w_0) < -1$) and Law 2 with $q > \frac{\Omega_m}{2(1+w_0)} + \frac{1-\Omega_m}{2}$ ($w(a) > -1$ everywhere, but $w_a > 0$).

---

### `M14` — Undefined $\bar{H}_0$, Sparse Low-$|b|$ Pixels, Non-Mechanical FAIL Clause, Cosmic-Variance Floor, and $z_{\rm HD}$ Circularity in Test T6
- **Status:** **`FIXED`**
- **What Changed & Where:**
  - In `MULTIVERSE_STAGE1_EQUATIONS.md` §8.1, `ASSUMPTIONS.md` `[A20]`, and `PREREG.md` §5.7:
    1. Defined $\bar{H}_0 \equiv \frac{\mathbf{1}^T \mathbf{C}_{H_0}^{-1}\hat{\mathbf{H}}_0}{\mathbf{1}^T \mathbf{C}_{H_0}^{-1}\mathbf{1}}$ explicitly as the GLS mean;
    2. Added a minimum pixel occupancy rule ($N_{\rm SN,min} = 10$), merging sparse low-Galactic-latitude pixels into adjacent same-quadrant higher-$|b|$ pixels and setting $\text{dof} = N_{\rm pix} - 1$;
    3. Removed the non-mechanical sociological clause regarding SH0ES team acceptance of a systematic;
    4. Added the $\Lambda\text{CDM}$ regional cosmic-variance floor $\mathbf{C}_{H_0}^{\rm LSS} = \mathbf{C}_{H_0} + \sigma_{\rm CV,reg}^2\mathbf{I}$ ($\sigma_{\rm CV,reg} = 0.013\bar{H}_0$);
    5. Registered both $z_{\rm HD}$ (primary) and pure CMB-frame $z_{\rm CMB}$ (secondary check without peculiar-velocity flow corrections).

---

### `M15` — Misquoted van Dokkum et al. (2018) / Danieli et al. (2019) Numbers, 3D Plummer Half-Mass Radius, and Negligible Group Term in Test T5c
- **Status:** **`FIXED`**
- **What Changed & Where:**
  - In `PREREG.md` §5.6 (`Test T5c`):
    1. Attributed $M_{\rm dyn}(< 2.7\text{ kpc}) = (1.3 \pm 0.8)\times 10^8\,M_\odot$ to **Danieli et al. (2019, ApJL 874, L12)** and updated the globular-cluster 90% upper limits to **van Dokkum et al. (2018, Nature 555, 629)**: $< 3.2\times 10^8\,M_\odot$ within $3.1\text{ kpc}$ and $< 3.4\times 10^8\,M_\odot$ within $7.6\text{ kpc}$;
    2. Corrected the 3D Plummer half-mass radius to $r_{1/2} = (2^{2/3} - 1)^{-1/2}R_e = 1.3048\,R_e = 2.87\text{ kpc}$;
    3. Stated explicitly that at $d_{3\rm D} = 98.0\text{ kpc}$, the NGC 1052 group term is $\le 2.5\times 10^6\,M_\odot$ for all $\sigma_{\rm ref} \in [1, 100]\text{ kpc}$, so T5c is purely a lower-bound check on $\sigma_{\rm ref} \gtrsim 3.3\text{ kpc}$.

---

## 3. Resolution of All MINOR Findings (`m1–m14`)

- **`m1` (`FIXED`):** In `MULTIVERSE_STAGE1_EQUATIONS.md` §5.4 `(d-Exp)` and `STAGE1_PART2_SECTIONS_DGH.md`, corrected the exploratory coupled $w_a^{\rm eff}$ bracket from $[\Omega_m + (1 + w_0^{\rm eff})(1 - \Omega_m)]$ to $[\Omega_m + (1 + w_0^{\rm eff} + \frac{\xi_e}{3})(1 - \Omega_m)]$ to include the coupled dark-matter derivative $\rho_{\rm dm}'(1) = -3\rho_{{\rm dm},0} - \xi_e\rho_{{\rm de},0}$.
- **`m2` (`FIXED`):** In `MULTIVERSE_STAGE1_EQUATIONS.md` §3 `(b5-T)` item 5 and `STAGE1_PART1_SECTIONS_ABC.md` §`(b)`, corrected the synchronous-gauge $\delta'_{\rm de}$ non-adiabatic term coefficient from $3\mathcal{H}^2$ to $9\mathcal{H}^2$.
- **`m3` (`FIXED`):** In `MULTIVERSE_STAGE1_EQUATIONS.md` §3 `(b5-T)` item 3 and `STAGE1_PART1_SECTIONS_ABC.md` §`(b)`, stated $\Gamma^{-1} = t_0 / 0.1823 \approx 75.7\text{ Gyr}$, clarified that $\Gamma^{-1} \gtrsim 150\text{–}260\text{ Gyr}$ applies to DM decaying into dark radiation, and removed the unsupported "$> 5\sigma$" phrase.
- **`m4` (`FIXED`):** In `MULTIVERSE_STAGE1_EQUATIONS.md` §4 & §7 `(f3)` and `STAGE1_PART1_SECTIONS_ABC.md` / `STAGE1_PART3_SECTIONS_EFI.md`, updated the rounded figures to $5.64\sigma_{\rm Planck}$ (for unrounded $5.3643 \pm 0.0646$, alongside $5.54\sigma_{\rm Planck}$ for rounded $5.36 \pm 0.065$), $f_{\rm leak} = 0.1059$ (for $5.3643$, alongside $0.1067$ for $5.36$), and $g_{\rm bar}^{\rm cap} = 3.99\times 10^{-12}\text{ m s}^{-2}$ at $f_{\rm leak} = 1/6$ ($3.71\times 10^{-12}\text{ m s}^{-2}$ at $\mathcal{R} = 5.20$).
- **`m5` (`FIXED`):** In `MULTIVERSE_STAGE1_EQUATIONS.md`, corrected all internal section cross-references (`Overview` $\to$ Section 5.4 and Section 8.3; §3 `(b5-S)` $\to$ Section 5 and Section 8.2).
- **`m6` (`FIXED`):** In `MULTIVERSE_STAGE1_EQUATIONS.md` §3 `(b5-T)` item 4, added the explicit analysis of the fourth coupling $Q_{\rm field} = \beta_\phi \rho_{\rm dm}\dot{\phi}/M_{\rm Pl}$ matching `STAGE1_PART1_SECTIONS_ABC.md`.
- **`m7` (`FIXED`):** In `MULTIVERSE_STAGE1_EQUATIONS.md` §1 & §4 `(c4)`, `ASSUMPTIONS.md` `[A3]`, and `PREREG.md` §5.2, defined $\Omega_{bc} \equiv \Omega_b + \Omega_{\rm dm} = \Omega_{m,{\rm tot}} - \Omega_{\nu,0}$ explicitly in the 1:6:12 share equations.
- **`m8` (`FIXED`):** In `PREREG.md` §5.1 and §5.2, set the uniform prior on $w_a$ to $[-3.0, 2.0]$ (matching the official DESI DR2 prior) and listed all sampled parameters and priors explicitly in both T1 and T2.
- **`m9` (`FIXED`):** In `PREREG.md` §5.6, stated explicitly that $\chi^2_{{\rm red},g}$ divides by $N_g$ because zero parameters are fitted per individual held-out galaxy.
- **`m10` (`FIXED`):** In `MULTIVERSE_STAGE1_EQUATIONS.md` §3 `(b5-T)` item 1 and `STAGE1_PART1_SECTIONS_ABC.md` §`(b)`, stated both $w = -1$ ($z_{\rm neg} = 5.606$) and the non-degenerate $w = -0.99$ case ($z_{\rm neg} = 5.58$) for the Gavela et al. (2009) doom factor $d$.
- **`m11` (`FIXED`):** In `MULTIVERSE_STAGE1_EQUATIONS.md` §8.3 `(i-Exp)` and `STAGE1_PART3_SECTIONS_EFI.md` §`(i)`, added the explicit `[EXPLORATORY — Not Pre-Registered in v1]` tag to the heading.
- **`m12` (`FIXED`):** In `MULTIVERSE_STAGE1_EQUATIONS.md` §4 `(c4)` and `PREREG.md` §5.2, registered the boundary rule that if $\Omega_{bc} > 7/19$ yields $f_{\rm leak} < 0$, the raw negative value is reported without clipping or reinterpretation.
- **`m13` (`FIXED`):** In `MULTIVERSE_STAGE1_EQUATIONS.md` §8.3 `(i-Exp)` and `STAGE1_PART3_SECTIONS_EFI.md` §`(i)`, stated the exact inputs $\Omega_{\rm dm}/\Omega_m = 5/6$, $z_{\rm eq} = 3402$, $z_{\rm de} = 0.294$ (giving $-3.94\,\epsilon_{\rm far}$), and the effective matter-era growth cutoff $z_{\rm cut} = 0.70$ (giving $-3.80\,\epsilon_{\rm far}$).
- **`m14` (`FIXED`):** In `MULTIVERSE_STAGE1_EQUATIONS.md` §6 `(e6 & e7)`, `STAGE1_PART3_SECTIONS_EFI.md` §`(e6 & e7)`, and `ASSUMPTIONS.md` `[A14]`, stated both post-shock gas sub-cases (`A14a-grav` where gas shares gravitational deceleration $\ddot{x}_G = \ddot{x}_S$, vs. `A14a-coast` where hydrostatic pressure balances gravity so the stellar shift is weighted by $f_S\mathcal{R}/(1 + \mathcal{R})$).

---

## WHAT CHANGES FOR THE FILM

1. **The minimum shadow lag time ($\tau_{\rm lag}$) jumps from 150 million years to 400–600 million years.**  
   Earlier drafts used 150 million years for the Bullet Cluster's age, which came from a 2002 estimate of how fast its X-ray shock wave was moving. Modern dynamical modeling of the Bullet Cluster's galaxies and dark matter (Dawson 2013, which was already in our reference list) puts the time since collision at about 400 million years (or up to 600 million years without a timing prior). Because the Bullet Cluster's dark matter still sits on its galaxies rather than its gas, the model's universal delay before a shadow catches up to stopped gas must be **at least 400 million years**, not 150 million years.

2. **The "dark matter ahead of the stars" test in young cluster collisions (Test T4a) cannot be run as a pass/fail statistical test and is now exploratory.**  
   Two things changed here. First, when you account for the fact that gravity speeds a cluster up as it falls *in* toward a collision just as much as it slows it down on the way *out*, the shadow actually trails slightly *behind* the galaxies for the first two-thirds of the lag window before briefly overshooting ahead of them. Second, once the Bullet Cluster itself is set aside (because it was used to calibrate the lag time), only one young cluster collision in the catalog (Abell 2744) is younger than 150 million years—and you cannot run a statistical average on a sample of one.

3. **The 19-string cosmic share prediction (1 part ordinary matter, 6 parts shadow dark matter, 12 parts outer tension) is already in sharp tension with Planck data.**  
   Fixing ordinary matter at exactly one-nineteenth of the universe (5.26%) is 6.8% higher than Planck's measured 4.93%—a nearly 4-sigma mismatch before any new data are even fitted. It also forces the model to predict a Hubble constant near 65 kilometers per second per megaparsec, which is *lower* than Planck's 67.4 and moves in the wrong direction to help the 73.0 local Hubble tension. Because of this built-in gap, the leak test (Test T2) is forecast to fail.

4. **The strand-unwinding dark energy curve is much flatter than what DESI DR2 sees, so the primary dark energy test (Test T1-L1) is forecast to fail.**  
   While the model correctly points in the general direction that dark energy is weakening today, the actual curve derived from a steadily unwinding strand never crosses the cosmological-constant line in the past and changes roughly six times more slowly than the steep "rise-then-fall" dark energy curve favored by DESI DR2. Testing the model's actual unwinding curve (rather than just checking whether dark energy is weaker today) is therefore forecast to fail or be strongly disfavored, unless the unwinding is combined with a late-time energy transfer in a future version of the model.

5. **The galaxy rotation-curve test (Test T5) is also forecast to fail its overall pass bar because of the six-to-one shadow ceiling.**  
   After fixing a math factor of two in the 3D Gaussian halo formula (which previously made enclosed shadow mass go negative at some radii!), the math is now rock-solid. However, because spreading the shadow of six neighbor galaxies out with a bell-curve blur can never produce more than six times the gravity of the visible stars and gas inside any radius, the model hits a hard ceiling of 6-to-1 total-to-ordinary gravity. Real dwarf and low-surface-brightness galaxies in the SPARC catalog reach 10-to-1 to 30-to-1 in their outer regions, so the model is expected to miss the 70% pass bar across the full galaxy sample while fitting high-surface-brightness spiral galaxies much better.

6. **Bottom line for the documentary narrative:**  
   With all escape hatches removed and every test tied directly to the model's actual equations, **the v1 cable model is forecast to fail all four of its primary pillar tests** (the unwinding dark energy curve, the 1-in-19 baryon and dark-to-ordinary ratio, the cluster merger age cutoff, and the full-sample galaxy rotation curves), leaving only secondary or stress checks (such as the directional sign of dark energy weakening today and the DF2 dark-matter-free galaxy check if the blur scale is wider than 3.3 kiloparsecs) able to pass. For the film, this means the scientific arc is a genuine falsification story: the intuitive geometry of the 19-string cable makes sharp, rigid numerical predictions, and when we refuse to bend the rules, modern precision cosmology and galaxy data show exactly where the simple v1 picture breaks.
