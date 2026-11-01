# Stage 1, Part 2: Theoretical Derivations for Sections (d), (g), and (h)

**Date:** 2026-10-30  
**Workspace:** `D:\Argon_Code\Ropewalk`  
**Package Version:** 1.0.1  
**Locked Leak Mechanism (per Gregory's Part 1 Decision):** Static Form ($Q = 0$). The combination of unwinding with $Q_{\rm de} = \xi_e H \rho_{\rm de}$ below is explicitly labeled **EXPLORATORY** (not pre-registered in v1 and never used in Tests T1–T6).

---

## Section (d): The Unwinding — Dark Energy as Outer-Ring Tension Tied to a Twist Variable

**Section Tier:** **Tier 1** for relativistic acceleration and uncoupled continuity (d1, d2); **Tier 3** for the twist-tension ansätze and CPL mappings (d3–d5).

### (d1) Cosmological Tension and the Second Friedmann Equation `[Established | Tier 1]`
A relativistic fluid with equation of state $p_{\rm de} = w\,\rho_{\rm de}c^2$ acts as an isotropic spatial tension when $w < 0$ (reducing to a cosmological constant when $w = -1$, $p_{\rm de} = -\rho_{\rm de}c^2$). In a flat FLRW universe, the acceleration equation is
$$\frac{\ddot{a}}{a} = -\frac{4\pi G}{3}\sum_i\left(\rho_i + \frac{3p_i}{c^2}\right) = -\frac{H_0^2}{2}\left[2\Omega_r a^{-4} + \Omega_m a^{-3} + \Omega_{\rm de}\left(1 + 3w(a)\right)g(a)\right].$$
Cosmic acceleration ($\ddot{a} > 0$) today requires $\Omega_{\rm de}(1 + 3w_0) + \Omega_m < 0 \iff w_0 < -\frac{1}{3(1 - \Omega_m)}$.

### (d2) Uncoupled Equation of State from Density Evolution `[Established | Tier 1]`
In the locked v1 Static Form ($Q = 0$), outer-ring tension satisfies uncoupled energy conservation $\dot{\rho}_{\rm de} + 3H(1 + w(a))\rho_{\rm de} = 0$, which inverts to
$$w(a) = -1 - \frac{1}{3}\frac{d\ln\rho_{\rm de}}{d\ln a} = -1 - \frac{1}{3}\frac{d\ln g(a)}{d\ln a}.$$
A tension density that decreases with cosmic time ($\dot{\rho}_{\rm de} < 0 \iff \frac{d\ln\rho_{\rm de}}{d\ln a} < 0$) has $w(a) > -1$; constant density has $w(a) = -1$.

### (d3) Twist–Tension Power-Law Relation `[Model Ansatz | Tier 3]`
Under Assumption **[A8]**, the outer-ring tension energy density $\rho_{\rm de}(a)$ is a power law of a dimensionless strand twist variable $\theta(t) > 0$ normalized to today's twist $\theta_0 \equiv \theta(t_0)$:
$$\rho_{\rm de}(a) = \rho_{\rm de,0}\left(\frac{\theta(a)}{\theta_0}\right)^n \quad \Longleftrightarrow \quad g(a) \equiv \frac{\rho_{\rm de}(a)}{\rho_{\rm de,0}} = \left(\frac{\theta(a)}{\theta_0}\right)^n, \qquad n > 0.$$
*(Physical analogy: $n = 2$ corresponds to the linear-elastic torsional strain energy density $U \propto \theta^2$ of a twisted cylindrical rod or wire strand.)*  
Substituting (d3) into (d2) yields the general uncoupled unwinding equation of state:
$$w(a) = -1 - \frac{n}{3}\frac{d\ln\theta}{d\ln a} = -1 - \frac{n}{3H(a)}\frac{\dot{\theta}}{\theta}.$$
**Fundamental Non-Phantom Theorem for Uncoupled Unwinding:** For any $n > 0$, $H(a) > 0$, and strictly monotonic unwinding ($\dot{\theta} < 0$ at all cosmic times), **$w(a) > -1$ at all epochs $a > 0$**. Pure uncoupled unwinding can never cross the phantom divide $w = -1$.

---

### (d4 & d5) Derivation of $(w_0, w_a)$ for Candidate Unwinding Laws

In the CPL parametrization (a4), any smooth equation of state $w(a)$ maps onto $(w_0, w_a)$ via its Taylor expansion at $a = 1$ (`[Model Ansatz | Tier 3]`):
$$w_0 \equiv w(a=1), \qquad w_a \equiv -\left.\frac{dw}{da}\right|_{a=1} = -\left.\frac{dw}{d\ln a}\right|_{a=1}.$$

#### Law 1 (d4 Baseline): Constant Cosmic-Time Relaxation Rate, $\dot{\theta} = -\Gamma_u\,\theta$ ($\Gamma_u > 0$) `[Model Ansatz | Tier 3]`
1. **Exact Evolution of $\theta(t)$, $g(a)$, and $w(a)$:**  
   Under Assumption **[A9]** (constant exponential relaxation rate $\Gamma_u > 0$ in cosmic time $t$),
   $$\frac{\dot{\theta}}{\theta} = -\Gamma_u \implies \theta(t) = \theta_0\,e^{-\Gamma_u(t - t_0)}, \qquad g(a) = \exp\!\left[-n\Gamma_u\left(t(a) - t_0\right)\right] = \exp\!\left[\frac{n\Gamma_u}{H_0}\int_a^1 \frac{da'}{a'\,E(a')}\right].$$
   Substituting $\dot{\theta}/\theta = -\Gamma_u$ into (d3) gives the exact scale-factor dependence of $w(a)$:
   $$w(a) = -1 + \frac{n\Gamma_u}{3H(a)} = -1 + \frac{n\Gamma_u}{3H_0\,E(a)}, \qquad E(a) \equiv \frac{H(a)}{H_0}.$$
   **Parameter Degeneracy:** Notice that $n$ and $\Gamma_u$ enter $g(a)$ and $w(a)$ **solely through the single product $n\Gamma_u$** (or the dimensionless combination $\gamma_u \equiv \frac{n\Gamma_u}{3H_0} > 0$). Thus Law 1 has **only one effective free parameter**, $\gamma_u$.

2. **Exact Derivation of $w_0$ and $w_a$:**  
   Evaluating $w(a)$ at $a = 1$ (where $E(1) = 1$) gives
   $$w_0 = -1 + \frac{n\Gamma_u}{3H_0} = -1 + \gamma_u > -1.$$
   Differentiating $w(a) = -1 + (1 + w_0)\,E^{-1}(a)$ with respect to $a$ gives
   $$\frac{dw}{da} = -(1 + w_0)\,\frac{1}{E^2(a)}\frac{dE}{da} = -\frac{1 + w_0}{2E^2(a)}\frac{d(E^2)}{da}.$$
   In the late-time background $E^2(a) = \Omega_m a^{-3} + (1 - \Omega_m)g(a)$ (with $g(1) = 1$ and $g'(1) = -3(1 + w_0)$), evaluating $\frac{d(E^2)}{da}$ at $a = 1$ yields
   $$\left.\frac{d(E^2)}{da}\right|_{a=1} = -3\Omega_m - 3(1 + w_0)(1 - \Omega_m) = -3\left[\Omega_m + (1 + w_0)(1 - \Omega_m)\right] = -3\left[1 + w_0(1 - \Omega_m)\right].$$
   Therefore, the exact CPL derivative parameter $w_a$ implied by Law 1 (d4) is
   $$w_a = \frac{1 + w_0}{2}\left.\frac{d(E^2)}{da}\right|_{a=1} = -\frac{3}{2}(1 + w_0)\left[\Omega_m + (1 + w_0)(1 - \Omega_m)\right] = -\frac{3}{2}(1 + w_0)\left[1 + w_0(1 - \Omega_m)\right].$$

3. **Sign, Quadrant, and $\Lambda\text{CDM}$ Recovery Limit:**
   - Since $\gamma_u = \frac{n\Gamma_u}{3H_0} > 0$, **$w_0 > -1$**.
   - For any accelerating universe ($w_0 < -\frac{1}{3(1 - \Omega_m)} \approx -0.49$), $1 + w_0(1 - \Omega_m) > \frac{2}{3} > 0$, so **$w_a < 0$**.
   - **$\Lambda\text{CDM}$ Recovery Limit:** As $\Gamma_u \to 0^+$ (or $n \to 0^+$), $\gamma_u \to 0$, recovering $(w_0, w_a) = (-1, 0)$ identically.

---

#### Law 2 (Alternative A): Nonlinear Viscoelastic Torque Relaxation, $\dot{\theta} = -\Gamma_u\,\theta_0\left(\frac{\theta}{\theta_0}\right)^p$ ($p > 0$) `[Model Ansatz | Tier 3]`
In nonlinear elasticity or plastic creep, the untwisting rate scales as a power $p$ of the twist angle $\theta$ ($p = 1$ recovers Law 1; $p = 0$ is constant untwisting speed $\dot{\theta} = -\Gamma_u\theta_0$; $p > 1$ is stress-accelerated relaxation at high twist).
1. **Equation of State $w(a)$:**  
   Since $\frac{\theta(a)}{\theta_0} = [g(a)]^{1/n}$, we have $\frac{\dot{\theta}}{\theta} = -\Gamma_u\left(\frac{\theta}{\theta_0}\right)^{p-1} = -\Gamma_u\,[g(a)]^q$ with $q \equiv \frac{p - 1}{n}$. Substituting into (d3) gives
   $$w(a) = -1 + (1 + w_0)\,\frac{\left[g(a)\right]^q}{E(a)}, \qquad w_0 = -1 + \frac{n\Gamma_u}{3H_0} > -1.$$
2. **Exact $(w_0, w_a)$ Relation:**  
   Differentiating at $a = 1$ (using $g'(1) = -3(1 + w_0)$) yields
   $$w_a = -\frac{3}{2}(1 + w_0)\left[\Omega_m + \left(1 - \Omega_m - 2q\right)(1 + w_0)\right], \qquad q \equiv \frac{p - 1}{n}.$$
   - For $p = 1$ ($q = 0$): reduces to Law 1.
   - For $0 \le p < 1$ ($q < 0$, e.g. constant unwinding speed $p = 0 \implies q = -1/n$): $-2q > 0$, steepening the negative slope $w_a < 0$.
   - Requiring $w_a < 0$ imposes the upper bound $q = \frac{p - 1}{n} < \frac{\Omega_m}{2(1 + w_0)} + \frac{1 - \Omega_m}{2}$.

---

#### Law 3 (Alternative B): Expansion-Driven Pitch Stretching, $\frac{d\ln\theta}{d\ln a} = -\alpha_u\,a^\beta$ ($\alpha_u > 0, \beta \ge 0$) `[Model Ansatz | Tier 3]`
If the strand's helical twist unwinds kinematically as cosmic expansion stretches the coil along the blade:
1. **Equation of State $w(a)$ and Density $g(a)$:**
   $$w(a) = -1 - \frac{n}{3}\frac{d\ln\theta}{d\ln a} = -1 + \frac{n\alpha_u}{3}\,a^\beta = -1 + (1 + w_0)\,a^\beta,$$
   $$g(a) = \exp\!\left[\frac{3(1 + w_0)}{\beta}\left(1 - a^\beta\right)\right] \quad (\text{for }\beta > 0), \qquad g(a) = a^{-3(1 + w_0)} \quad (\text{for }\beta = 0).$$
2. **Exact $(w_0, w_a)$ Relation:**
   $$w_0 = -1 + \frac{n\alpha_u}{3} > -1, \qquad w_a = -\left.\frac{dw}{da}\right|_{a=1} = -\beta(1 + w_0).$$
   - For $\beta = 0$: $w(a) = w_0 = \text{const}$ ($w_a = 0$).
   - For $\beta = 1$: $w(a) = -1 + (1 + w_0)a = w_0 - (1 + w_0)(1 - a)$ is **exact CPL at all redshifts** with $w_a = -(1 + w_0) < 0$ and high-redshift asymptote $w(a \to 0) = -1$.

---

### Does the Model Predict a Band in the $(w_0, w_a)$ Plane?

**Yes — and this is a sharp, falsifiable structural property of the unwinding mechanism:**
1. **Law 1 (d4) Predicts a 1D Curve (Narrow Band Fixed by $\Omega_m$):**  
   Because $n$ and $\Gamma_u$ enter only as the product $n\Gamma_u = 3H_0(1 + w_0)$, Law 1 has **zero freedom in $w_a$ once $w_0$ and $\Omega_m$ are specified**:
   $$w_a^{\rm (d4)}(w_0; \Omega_m) = -\frac{3}{2}(1 + w_0)\left[\Omega_m + (1 + w_0)(1 - \Omega_m)\right].$$
   At the model's expected matter share $\Omega_m = 6/19 \approx 0.3158$, this curve has linear slope $\left.\frac{dw_a}{dw_0}\right|_{w_0 = -1} = -\frac{3}{2}\Omega_m = -0.474$ (and across the plausible range $\Omega_m \in [0.29, 0.34]$, forms a razor-thin band of width $\Delta w_a \approx \pm 0.038(1 + w_0)$).
2. **Why Tangent CPL Parameters $(w_0, w_a)$ Are Not Confined to a Universal Wedge (Correction of M13):**  
   While $w(a) \ge -1$ holds at all scale factors $a > 0$ for any uncoupled monotonic unwinding law ($\dot{\theta} \le 0, n > 0$), the tangent parameter $w_a \equiv -\left.\frac{dw}{da}\right|_{a=1}$ is only a local first derivative at $a = 1$. Only if $w(a)$ is restricted to be globally linear in $a$ ($w(a) = w_0 + w_a(1 - a)$, Law 3 with $\beta = 1$) does $w(0) \ge -1$ imply $w_0 + w_a \ge -1$. For general smooth curves with $w(a) \ge -1$:
   - Law 3 with $\beta > 1$ ($w(a) = -1 + (1 + w_0)a^\beta \ge -1$ for all $a \in [0, 1]$) has tangent $w_a = -\beta(1 + w_0)$, so $w_0 + w_a = -1 - (\beta - 1)(1 + w_0) < -1$.
   - Law 2 with $q > \frac{\Omega_m}{2(1+w_0)} + \frac{1-\Omega_m}{2}$ has $w(a) > -1$ everywhere but $w_a > 0$.
   Thus no universal "Uncoupled Non-Phantom Wedge" theorem exists for tangent $(w_0, w_a)$ parameters; instead, the baseline Law 1 (d4) makes the specific 1D prediction $w_a^{\rm (d4)}(w_0; \Omega_m) = -\frac{3}{2}(1 + w_0)[\Omega_m + (1 + w_0)(1 - \Omega_m)]$, which is registered directly as **Primary Test T1-L1**.
3. **Comparison with DESI DR2 (Open Problem 11 & Forecast for T1-L1):**  
   Published DESI DR2 + CMB + SNe CPL contours lie in the $w_0 > -1, w_a < 0$ quadrant ($w_0 \approx -0.84 \pm 0.06, w_a \approx -0.62 \text{ to } -0.86$), whereas at $w_0 = -0.84$ and $\Omega_m = 0.315$, Law 1 predicts $w_a^{\rm (d4)} \approx -0.102$ (a shallow curve that never crosses $w = -1$). Consequently, when fitted directly against DESI DR2 + CMB + SNe in Primary Test T1-L1, Law 1 is **forecast to be disfavored relative to $w_0w_a\text{CDM}$ by $\Delta\chi^2 \approx 7\text{–}12$ ($\sim 2.6\text{–}3.5\sigma$, FAIL or INCONCLUSIVE)**.

---

### EXPLORATORY Analysis: Combining Unwinding (d4) with the Stable Transfer Coupling ($Q_{\rm de} = \xi_e H \rho_{\rm de}$)

> **[EXPLORATORY — Not Pre-Registered in v1 | Tier 2/3]:** Derived per B6 Part 2 to test whether combining bare unwinding (d4) with the perturbation-stable IDE coupling $Q_{\rm de} = \xi_e H \rho_{\rm de}$ ($\xi_e > 0$) can produce an effective phantom crossing ($w_{\rm de}^{\rm eff} < -1$ in the past, $w_{\rm de}^{\rm eff} > -1$ today). This introduces the unregistered parameter $\xi_e$ and is **excluded from all pre-registered tests T1–T6**.

Combining bare unwinding $w_{\rm bare}(a) = -1 + \frac{\gamma_u}{E(a)}$ ($\gamma_u \equiv \frac{n\Gamma_u}{3H_0} > 0$) with $Q_{\rm de} = \xi_e H \rho_{\rm de}$ ($\xi_e > 0$) via (b2) gives `[Model Ansatz | Tier 3 | EXPLORATORY]`:
$$w_{\rm de}^{\rm eff}(a) = w_{\rm bare}(a) - \frac{Q_{\rm de}}{3H\rho_{\rm de}} = -1 + \frac{\gamma_u}{E(a)} - \frac{\xi_e}{3}.$$
1. **Rise-Then-Fall Dark Energy Density & Phantom Crossing:**
   - **Today ($a = 1, E(1) = 1$):** $w_0^{\rm eff} = -1 + \gamma_u - \frac{\xi_e}{3}$. Provided $\gamma_u > \frac{\xi_e}{3} > 0$, we have **$w_0^{\rm eff} > -1$**, so $\dot{\rho}_{\rm de}(t_0) < 0$ (**dark energy density is falling today**).
   - **Phantom Crossing at $z_{\rm cross} > 0$:** Because $E(z) = H(z)/H_0$ increases monotonically with redshift $z$, the positive unwinding term $+\frac{\gamma_u}{E(z)}$ decays with redshift while the negative leak shift $-\frac{\xi_e}{3}$ remains constant. Therefore, $w_{\rm de}^{\rm eff}(z)$ **crosses $-1$** at the exact redshift $z_{\rm cross}$ where
     $$E(z_{\rm cross}) = \frac{3\gamma_u}{\xi_e} = 1 + \frac{3\left(1 + w_0^{\rm eff}\right)}{\xi_e} > 1.$$
   - **Phantom Past ($z > z_{\rm cross}$):** For all $z > z_{\rm cross}$, $w_{\rm de}^{\rm eff}(z) < -1$ (approaching $-1 - \frac{\xi_e}{3}$ as $z \to \infty$), meaning $\rho_{\rm de}(z)$ **rose with cosmic time in the past, reached a maximum at $z = z_{\rm cross}$, and is falling today** — reproducing the qualitative rise-then-fall shape of Open Problem 11 while keeping bare tension non-phantom ($w_{\rm bare}(a) > -1$) and linear perturbations stable ($d = -\frac{\xi_e}{3(1 + w_{\rm bare})} < 0$, Gavela et al. 2009)!
2. **Effective CPL Parameters $(w_0^{\rm eff}, w_a^{\rm eff})$:**  
   Because $Q_{\rm de}$ transfers energy out of dark matter (`b1`), $\rho_{\rm dm}'(1) = -(3\rho_{{\rm dm},0} + \xi_e\rho_{{\rm de},0})$ while $\rho_{\rm de}'(1) = -3(1 + w_0^{\rm eff})\rho_{{\rm de},0}$. Summing the two gives $\left.\frac{d(E^2)}{da}\right|_{a=1} = -3\Omega_m - [3(1 + w_0^{\rm eff}) + \xi_e](1 - \Omega_m) = -3[\Omega_m + (1 + w_0^{\rm eff} + \frac{\xi_e}{3})(1 - \Omega_m)] = -3[\Omega_m + \gamma_u(1 - \Omega_m)]$. Therefore:
   $$w_0^{\rm eff} = -1 + \gamma_u - \frac{\xi_e}{3}, \qquad w_a^{\rm eff} = -\frac{3}{2}\left(1 + w_0^{\rm eff} + \frac{\xi_e}{3}\right)\left[\Omega_m + \left(1 + w_0^{\rm eff} + \frac{\xi_e}{3}\right)(1 - \Omega_m)\right] < 0.$$

---

## Section (g): Locality — Difference Bubbles and Local Hubble Reading (Code-Ready Form)

**Section Tier:** **Tier 1** for relativistic light-cone propagation and low-$z$ Hubble-flow kinematics (g1, g4-kin); **Tier 2** for local Everettian information flow (Deutsch & Hayden 2000); **Tier 3** for the strand locality approximation and regional $H_0$ interpretation (g2–g4).

### (g1 & g2) Difference-Bubble Radius in Code-Ready Form `[Established (g1) / Model Ansatz (g2) | Tier 1 & 3]`
For a split event occurring at spacetime point $(t_s, \mathbf{x}_s)$ corresponding to scale factor $a_s = (1 + z_s)^{-1}$, causal locality (Assumption **[A10]**) restricts differences between the two branched histories at later cosmic time $t$ (scale factor $a = (1 + z)^{-1}$, $z < z_s$) to a sphere of proper radius $R_{\rm diff}(z; z_s)$ equal to the proper light-travel horizon $R_{\rm light}(t; t_s)$:
$$\left|\mathbf{x} - \mathbf{x}_s\right| \le R_{\rm diff}(z; z_s) \equiv R_{\rm light}(t; t_s) = a(t)\int_{t_s}^{t}\frac{c\,dt'}{a(t')} = \frac{c}{1 + z}\int_{z}^{z_s}\frac{dz'}{H(z')}.$$
**Code-Ready Form via Comoving Distance $D_M(z)$:**  
Using the transverse comoving distance $D_M(z) = \frac{c}{H_0}\int_0^z \frac{dz'}{E(z')}$ from Section (a5), the comoving difference radius $\chi_{\rm diff}(z; z_s)$ and proper difference radius $R_{\rm diff}(z; z_s)$ require no separate integration routine:
$$\chi_{\rm diff}(z; z_s) = D_M(z_s) - D_M(z), \qquad R_{\rm diff}(z; z_s) = \frac{D_M(z_s) - D_M(z)}{1 + z}.$$
At $z = 0$ today, $R_{\rm diff}(0; z_s) = D_M(z_s)$. In the small-split-age regime $\Delta t_{\rm split} \equiv t - t_s \ll H(z)^{-1}$, expansion is negligible and the code uses the linear proper-time conversion:
$$R_{\rm diff}(\Delta t_{\rm split}) \approx c\,\Delta t_{\rm split} = 306.601\text{ kpc}\times\left(\frac{\Delta t_{\rm split}}{1\text{ Myr}}\right) = 1.02271\text{ pc}\times\left(\frac{c}{1\text{ km s}^{-1}}\right)\left(\frac{\Delta t_{\rm split}}{1\text{ Myr}}\right).$$

### (g3) Justification of the Six-Neighbor Locality Approximation (e4) `[Model Ansatz | Tier 3]`
Outside the union of active difference bubbles, $\rho_b^{(k)}(\mathbf{x}, t) = \rho_b(\mathbf{x}, t)$ for each of the $k = 1,\dots,6$ touching neighbor strings. Under Assumption **[A10]**, splits between touching strand-mates do not alter macroscopic galaxy or cluster baryon distributions on scales $\gtrsim 1\text{ kpc}$, justifying the replacement $\sum_{k=1}^6 \tilde{\rho}_b^{(k)}(\mathbf{x}, t) = 6\,\tilde{\rho}_b(\mathbf{x}, t)$ in (e4).

### (g4) Code-Ready Formulation for Test T6 (Regional $H_0$ on HEALPix $N_{\rm side} = 1$) `[Established Estimator / Model Ansatz | Tier 1 & 3]`
In Test T6, the sky is divided into the $N_{\rm pix} = 12\,N_{\rm side}^2 = 12$ equal-area regions of a HEALPix $N_{\rm side} = 1$ grid (in galactic or equatorial coordinates as specified in `PREREG.md`).
1. **FIX Step (SH0ES Calibrators Only):** From the SH0ES Cepheid-calibrated supernova sample (Riess et al. 2022), freeze the fiducial Type Ia supernova absolute magnitude $M_B^{\rm fixed}$ (and its calibrator variance $\sigma_{M_B}^2$).
2. **TEST Step (Pantheon+ Hubble-Flow Supernovae Split into 12 Sky Regions):** For each Hubble-flow supernova $\alpha$ ($z_{\rm min} = 0.023 \le z_{\rm HD,\alpha} \le 0.15 = z_{\rm max}$, the standard SH0ES Hubble-flow cut using peculiar-velocity-corrected CMB-frame redshift $z_{\rm HD}$ and heliocentric redshift $z_{\rm hel}$) located in HEALPix pixel $i(\alpha) \in \{1,\dots,12\}$, the predicted apparent magnitude is `[Established | Tier 1, Riess et al. 2022]`:
   $$m_{B,\alpha}^{\rm model}\!\left(H_{0,i(\alpha)}\right) = M_B^{\rm fixed} + 25 + 5\log_{10}\!\left[\frac{c(1 + z_{{\rm hel},\alpha})}{(1 + z_{{\rm HD},\alpha})H_{0,i(\alpha)}}\,z_{{\rm HD},\alpha}\left(1 + \frac{1 - q_0}{2}z_{{\rm HD},\alpha} - \frac{1 - q_0 - 3q_0^2 + j_0}{6}z_{{\rm HD},\alpha}^2\right)\right],$$
   with standard kinematic parameters $q_0 = -0.55$ and $j_0 = 1.0$ (where distances are in $\text{Mpc}$).
3. **Full-Covariance Generalized Least Squares Across the 12 Regions:**  
   Define the log-Hubble parameter vector $\boldsymbol{\eta} = (\eta_1, \dots, \eta_{12})^T$ with $\eta_i \equiv 5\log_{10} H_{0,i}$, so $m_{B,\alpha}^{\rm model}(\boldsymbol{\eta}) = \mu_{0,\alpha} - \eta_{i(\alpha)}$ is strictly **linear** in $\boldsymbol{\eta}$. Let $\mathbf{y}$ be the $N_{\rm HF}$-vector of residuals $y_\alpha \equiv \mu_{0,\alpha} - m_{B,\alpha}^{\rm obs}$, $\mathbf{P}$ be the $N_{\rm HF} \times 12$ pixel-indicator matrix ($P_{\alpha i} = 1$ if supernova $\alpha$ belongs to pixel $i$, $0$ otherwise), and $\mathbf{C}_{\rm HF}$ be the $N_{\rm HF} \times N_{\rm HF}$ Hubble-flow block of the published Pantheon+ statistical-plus-systematic covariance matrix. The exact maximum-likelihood estimator for $\boldsymbol{\eta}$ and its $12 \times 12$ covariance matrix $\mathbf{C}_\eta$ are:
   $$\hat{\boldsymbol{\eta}} = \left(\mathbf{P}^T \mathbf{C}_{\rm HF}^{-1} \mathbf{P}\right)^{-1} \mathbf{P}^T \mathbf{C}_{\rm HF}^{-1} \mathbf{y}, \qquad \mathbf{C}_\eta = \left(\mathbf{P}^T \mathbf{C}_{\rm HF}^{-1} \mathbf{P}\right)^{-1},$$
   converting to $\hat{H}_{0,i} = 10^{\hat{\eta}_i / 5}$ with covariance $\left(\mathbf{C}_{H_0}\right)_{ij} = \left(\frac{\ln 10}{5}\right)^2 \hat{H}_{0,i}\hat{H}_{0,j}\left(\mathbf{C}_\eta\right)_{ij}$.
4. **Pre-Registered T6 Heterogeneity $\chi^2$ Statistic:**  
   With $\mathbf{1} = (1,\dots,1)^T \in \mathbb{R}^{12}$, the inverse-covariance-weighted mean $\bar{H}_0$ and the heterogeneity $\chi^2$ (for $\nu = 12 - 1 = 11$ degrees of freedom) are:
   $$\bar{H}_0 = \frac{\mathbf{1}^T \mathbf{C}_{H_0}^{-1} \hat{\mathbf{H}}_0}{\mathbf{1}^T \mathbf{C}_{H_0}^{-1} \mathbf{1}}, \qquad \chi^2_{\rm het} = \left(\hat{\mathbf{H}}_0 - \bar{H}_0\mathbf{1}\right)^T \mathbf{C}_{H_0}^{-1} \left(\hat{\mathbf{H}}_0 - \bar{H}_0\mathbf{1}\right), \qquad p_{\rm het} = 1 - F_{\chi^2_{11}}\!\left(\chi^2_{\rm het}\right),$$
   with two-sided Gaussian significance $Z_{\rm het} = \sqrt{2}\,\text{erfc}^{-1}(p_{\rm het})$.

---

## Section (h): The Coincidence — Exact Method for Computing the Coincidence Window

**Section Tier:** **Tier 1** for background share evolution (h1); **Tier 3** for the 1:6:12 coincidence window diagnostic (h2).

### (h1) Evolution of Instantaneous Cosmic Budget Shares `[Established | Tier 1]`
At any scale factor $a$, the instantaneous share $\Omega_i(a) \equiv \frac{\rho_i(a)}{\rho_{\rm crit}(a)}$ of component $i \in \{r, b, {\rm dm}, {\rm de}\}$ in a flat FLRW universe is
$$\Omega_b(a) = \frac{\Omega_{b,0}\,a^{-3}}{E^2(a)}, \qquad \Omega_{\rm dm}(a) = \frac{\Omega_{{\rm dm},0}\,a^{-3}}{E^2(a)}, \qquad \Omega_{\rm de}(a) = \frac{\Omega_{{\rm de},0}\,g(a)}{E^2(a)},$$
where $E^2(a) = \Omega_{r,0}a^{-4} + \left(\Omega_{b,0} + \Omega_{{\rm dm},0}\right)a^{-3} + \Omega_{{\rm de},0}\,g(a)$ (with $g(a) = 1$ in base $\Lambda\text{CDM}$).

### (h2) Exact Method to Compute the Coincidence Time Span $\Delta t_{\rm coinc}$ `[Model Ansatz / Diagnostic | Tier 3]`
In Section (c3), the model's target cosmic shares are
$$s_b^{\rm target} = \frac{1}{19} \approx 0.05263, \qquad s_{\rm dm}^{\rm target} = \frac{6(1 - f_{\rm leak})}{19}, \qquad s_{\rm de}^{\rm target} = \frac{12 + 6f_{\rm leak}}{19}.$$
Because the parameter-free baryon share $s_b^{\rm target} = 1/19 = 0.05263$ already differs from Planck's present-day baryon share $\Omega_{b,0} = \omega_b/h^2 = 0.04930$ by $|\Omega_{b,0} - s_b^{\rm target}| = 0.00333$ ($6.75\%$ relative difference) at $a = 1$, any tolerance tighter than $0.00333$ (absolute) or $6.75\%$ (relative) would yield a coincidence window of **zero duration ($\Delta t_{\rm coinc} = 0$)** even today!

To evaluate the coincidence window transparently without tuning (Assumption **[A11]**), `PREREG.md` will declare two fixed, standard tolerance definitions (evaluated both at the headline $f_{\rm leak} = 1/6$ where $s^{\rm target} = (1/19, 5/19, 13/19)$ and at the T2-frozen $f_{\rm leak}$):
1. **Criterion H-Abs (Absolute Share Tolerance $\Delta_{\rm abs} = 0.05$, i.e., $\pm 5$ percentage points on all three shares simultaneously):**
   $$\mathcal{W}_{\rm abs} = \left\{a > 0 \;\middle|\; \max_{i \in \{b, {\rm dm}, {\rm de}\}} \left|\Omega_i(a) - s_i^{\rm target}\right| \le 0.05\right\}.$$
2. **Criterion H-Rel (Relative Share Tolerance $\delta_{\rm rel} = 0.10$, i.e., $\pm 10\%$ fractional tolerance on all three shares simultaneously):**
   $$\mathcal{W}_{\rm rel} = \left\{a > 0 \;\middle|\; \max_{i \in \{b, {\rm dm}, {\rm de}\}} \frac{\left|\Omega_i(a) - s_i^{\rm target}\right|}{s_i^{\rm target}} \le 0.10\right\}.$$

#### Step-by-Step Computational Algorithm (Ready for Stage 2 Code)
1. **Determine the Permissible Interval $[L_i, U_i]$ for Each Share $i \in \{b, {\rm dm}, {\rm de}\}$:**
   - Under Criterion H-Abs: $L_i = s_i^{\rm target} - \Delta_{\rm abs}$, $U_i = s_i^{\rm target} + \Delta_{\rm abs}$.
   - Under Criterion H-Rel: $L_i = s_i^{\rm target}(1 - \delta_{\rm rel})$, $U_i = s_i^{\rm target}(1 + \delta_{\rm rel})$.
2. **Solve for the Scale-Factor Bounds $[a_{\rm min}, a_{\rm max}]$:**  
   In the post-radiation era ($\Omega_{r,0}a^{-4} \ll \Omega_{m,0}a^{-3}$), $\Omega_b(a)$ and $\Omega_{\rm dm}(a)$ decrease monotonically with $a$ while $\Omega_{\rm de}(a)$ increases monotonically with $a$. For base $\Lambda\text{CDM}$ ($g(a) = 1$), the exact analytical root for each component is:
   $$a_{i,{\rm min}} = \left[\frac{1}{\Omega_{\Lambda,0}}\,\max\!\left(0,\; \frac{\Omega_{i,0}}{U_i} - \Omega_{m,0}\right)\right]^{1/3}, \qquad a_{i,{\rm max}} = \left[\frac{1}{\Omega_{\Lambda,0}}\,\max\!\left(0,\; \frac{\Omega_{i,0}}{L_i} - \Omega_{m,0}\right)\right]^{1/3} \quad (i \in \{b, {\rm dm}\}),$$
   $$a_{{\rm de},{\rm min}} = \left(\frac{\Omega_{m,0}}{\Omega_{\Lambda,0}}\frac{L_{\rm de}}{1 - L_{\rm de}}\right)^{1/3}, \qquad a_{{\rm de},{\rm max}} = \left(\frac{\Omega_{m,0}}{\Omega_{\Lambda,0}}\frac{U_{\rm de}}{1 - U_{\rm de}}\right)^{1/3}.$$
   The joint scale-factor window $[a_{\rm min}, a_{\rm max}]$ is the intersection:
   $$a_{\rm min} = \max_{i \in \{b, {\rm dm}, {\rm de}\}} a_{i,{\rm min}}, \qquad a_{\rm max} = \min_{i \in \{b, {\rm dm}, {\rm de}\}} a_{i,{\rm max}}.$$
   *(In the Python code, these roots are also polished to machine precision via `scipy.optimize.brentq` including the radiation term $\Omega_{r,0}a^{-4}$.)*
3. **Integrate to Cosmic Time Span $\Delta t_{\rm coinc}$:**  
   If $a_{\rm min} < a_{\rm max}$, the cosmic time duration of the coincidence window (and its fraction of the present age of the universe $t_0$) is
   $$\Delta t_{\rm coinc} = t(a_{\rm max}) - t(a_{\rm min}) = \frac{1}{H_0}\int_{a_{\rm min}}^{a_{\rm max}} \frac{da}{a\,E(a)}, \qquad f_{\rm coinc} \equiv \frac{\Delta t_{\rm coinc}}{t_0}.$$
   In flat $\Lambda\text{CDM}$ (neglecting $\Omega_{r,0}$ at $a \sim 1$), this integral has the exact analytical check formula:
   $$\Delta t_{\rm coinc} = \frac{2}{3H_0\sqrt{\Omega_{\Lambda,0}}}\left[\operatorname{arsinh}\!\left(\sqrt{\frac{\Omega_{\Lambda,0}}{\Omega_{m,0}}\,a_{\rm max}^3}\right) - \operatorname{arsinh}\!\left(\sqrt{\frac{\Omega_{\Lambda,0}}{\Omega_{m,0}}\,a_{\rm min}^3}\right)\right].$$
