---
title: "MULTIVERSE Stage 1 Tightened Equations, Assumptions, Parameter Table, and Recovery Limits"
subtitle: "Self-Contained Theoretical Formulation of the Mandarano Model (v1.0.1) for Independent Cold Review"
author: "Gregory Mandarano / WickedAI (Model Author) — Mathematical Derivations by Gemini 4 Argon"
date: "2026-10-30"
---

# Overview & Cold-Reviewer Orientation

This document is the complete, self-contained Stage 1 mathematical formulation of the **Mandarano Model** ("the cable", package version 1.0.1). It was produced before any dataset was downloaded and before any analysis code was written.

Every equation in this document carries:
1. **Honesty Classification:** `[Established]` (standard published physics, mathematics, or empirical fits) or `[Model Ansatz]` (a form chosen to represent the Mandarano Model).
2. **Tier Tag:** **Tier 1** (established physics and measurements), **Tier 2** (peer-reviewed published speculation), or **Tier 3** (this model). The $1:6:12$ cosmic budget match is explicitly labeled **numerology**.
3. **Explicit Assumption Cross-References:** `[A1]` through `[A20]`, listed in full in Section 10.
4. **$\Lambda\text{CDM}$ and Newtonian Recovery Limits:** Summarized in Section 9.

Where an exploratory theoretical extension is derived (such as combining strand unwinding with the perturbation-stable interacting dark energy coupling $Q_{\rm de} = \xi_e H \rho_{\rm de}$ in Section 4.4, or the linear-growth signature of $\epsilon_{\rm far}$ in Section 8.2), it is explicitly marked **`[EXPLORATORY — Not Pre-Registered in v1]`** and may never be used in the pre-registered v1 tests (T1–T6).

---

# 1. Conventions and Shared Parameter Names

- **Metric & Cosmological Coordinates:** Spatially flat FLRW geometry ($k = 0$), cosmic time $t$, overdot $\dot{} \equiv d/dt$, scale factor $a(t)$ normalized to $a_0 \equiv a(t_0) = 1$ today, redshift $1 + z = 1/a$, Hubble rate $H(t) \equiv \dot{a}/a$, dimensionless expansion rate $E(a) \equiv H(a)/H_0$, present critical density $\rho_{\rm crit,0} \equiv \frac{3H_0^2}{8\pi G}$, dimensionless density shares $\Omega_i \equiv \frac{\rho_{i,0}}{\rho_{\rm crit,0}}$, physical density parameters $\omega_i \equiv \Omega_i h^2$ with $h \equiv \frac{H_0}{100\text{ km s}^{-1}\text{ Mpc}^{-1}}$.
- **Subscripts:** $b$ = ordinary baryonic matter; $\rm dm$ (or $\rm sh$) = dark matter (the gravitational shadow of the six touching neighbor strings); $\rm de$ = dark energy (outer-ring strand tension); $\gamma$ = photons; $\nu$ = neutrinos; $r = \gamma + \nu_{\rm rel}$ = radiation; $m = b + {\rm dm}$ = pressureless matter.
- **Shared Parameter Names (Identical Across All Package Files):**
  $$N_s = 19, \qquad N_r = 133, \qquad f_{\rm leak}, \qquad \epsilon_{\rm far}, \qquad w_0, \qquad w_a, \qquad \tau_{\rm lag}, \qquad \sigma_{\rm ref}.$$

---

# 2. Section (a): Background Cosmology

**Section Tier:** **Tier 1** for equations (a1)–(a5); **Tier 3** for the dark-sector mapping (a6).

## (a1) Flat FLRW Metric `[Established | Tier 1 | Assumption A1]`
$$ds^2 = -c^2\,dt^2 + a^2(t)\left[dr^2 + r^2\left(d\theta^2 + \sin^2\theta\,d\phi^2\right)\right].$$

## (a2) First Friedmann Equation `[Established | Tier 1 | Assumptions A1, A2]`
$$H^2(a) = \frac{8\pi G}{3}\sum_i \rho_i(a), \qquad E^2(a) \equiv \frac{H^2(a)}{H_0^2} = \Omega_\gamma a^{-4} + \Omega_\nu f_\nu(a) + \Omega_b a^{-3} + \Omega_{\rm dm} f_{\rm dm}(a) + \Omega_{\rm de}\,g(a),$$
subject to flatness closure $\sum_i \Omega_i = 1$, where $g(a) \equiv \rho_{\rm de}(a)/\rho_{\rm de,0}$ ($g(1) = 1$) and $f_{\rm dm}(a) \equiv \rho_{\rm dm}(a)/\rho_{\rm dm,0}$. In the locked v1 **Static Form** of the leak ($Q = 0$, Section 3.3), dark matter is uncoupled and $f_{\rm dm}(a) = a^{-3}$ at all epochs:
$$E^2(a) = \Omega_\gamma a^{-4} + \Omega_\nu f_\nu(a) + \Omega_m a^{-3} + \Omega_{\rm de}\,g(a), \qquad \Omega_m \equiv \Omega_b + \Omega_{\rm dm}.$$
Here $\Omega_\gamma = 2.4728\times 10^{-5}/h^2$ (for $T_{\rm CMB,0} = 2.7255\text{ K}$) and $\Omega_\nu f_\nu(a)$ describes standard cosmic neutrinos with $N_{\rm eff} = 3.044$ and $\sum m_\nu = 0.06\text{ eV}$ ($\Omega_{\nu,0} = \frac{\sum m_\nu}{93.14\,h^2\text{ eV}} \approx 0.00142$ at $z = 0$, scaling as radiation $a^{-4}$ for $z \gg z_{\rm nr}$ and as matter $a^{-3}$ for $z \ll z_{\rm nr}$).

## (a3) Uncoupled Fluid Continuity Equation `[Established | Tier 1]`
For any uncoupled fluid $i$ with equation of state $w_i(a) \equiv \frac{p_i(a)}{\rho_i(a)c^2}$,
$$\dot{\rho}_i + 3H\left(1 + w_i(a)\right)\rho_i = 0 \quad \Longleftrightarrow \quad \frac{d\ln\rho_i}{d\ln a} = -3\left(1 + w_i(a)\right).$$

## (a4) Chevallier–Polarski–Linder (CPL) Parametrization `[Established | Tier 1]`
For an uncoupled dark energy component with $w(a) = w_0 + w_a(1 - a) = w_0 + w_a\frac{z}{1+z}$ (Chevallier & Polarski 2001; Linder 2003), integrating (a3) yields
$$g_{\rm CPL}(a) = a^{-3(1 + w_0 + w_a)}\exp\!\left[-3w_a(1 - a)\right] = (1 + z)^{3(1 + w_0 + w_a)}\exp\!\left(-\frac{3w_a z}{1 + z}\right).$$

## (a5) Distance, Sound-Horizon, and Compressed CMB Observables `[Established | Tier 1 | Assumptions A1, A2]`
$$D_M(z) = \frac{c}{H_0}\int_0^z \frac{dz'}{E(z')}, \qquad D_H(z) = \frac{c}{H(z)}, \qquad D_V(z) = \left[z\,D_M^2(z)\,D_H(z)\right]^{1/3},$$
$$D_L(z) = (1 + z)\,D_M(z), \qquad \mu(z) = 5\log_{10}\!\left(\frac{D_L(z)}{1\text{ Mpc}}\right) + 25,$$
$$r_s(z) = \int_z^\infty \frac{c_s(z')}{H(z')}\,dz', \qquad c_s(z) = \frac{c}{\sqrt{3\left(1 + \frac{3\omega_b}{4\omega_\gamma(1 + z)}\right)}}, \qquad r_d \equiv r_s(z_d).$$
The compressed CMB distance priors (Chen, Huang & Wang 2019) at recombination redshift $z_*$ are
$$R = \frac{\sqrt{\Omega_m H_0^2}}{c}\,D_M(z_*) = \sqrt{\Omega_m}\int_0^{z_*}\frac{dz'}{E(z')}, \qquad \ell_A = \frac{\pi\,D_M(z_*)}{r_s(z_*)}, \qquad \omega_b = \Omega_b h^2.$$
*(In Test T2, the fixing fit uses only the $2\times 2$ $(R, \ell_A)$ block marginalized over $\omega_b$, combined with the BBN deuterium prior $100\omega_b = 2.166 \pm 0.019$ of Cooke, Pettini & Steidel 2018.)*

## (a6) Mandarano Model Background Mapping `[Model Ansatz | Tier 3 | Assumption A3]`
Neglecting $\Omega_{\gamma,0}$ and $\Omega_{\nu,0}$ in the three-component present-day strand budget, the cosmic background consists of ordinary baryons ($w_b = 0$), the pressureless shadow of the 6 touching neighbor strings ($w_{\rm dm} = 0$), and outer-ring longitudinal string tension ($w_{\rm de} = w(a)$).

---

# 3. Section (b): The Leak as Interacting Dark Energy (Static vs. Transfer Analysis)

**Section Tier:** **Tier 1** for covariant conservation (b1, b2); **Tier 2** for published IDE kernels and perturbation stability theorems (b3, b4); **Tier 3** for the model's leak mapping (b5).

## (b1) Coupled Dark-Sector Continuity Equations `[Established | Tier 1]`
With $Q > 0$ defined as energy transfer **from shadow dark matter ($\rm dm$) to outer-ring tension ($\rm de$)** (matching Boehmer et al. 2008; opposite to Gavela et al. 2009 where $Q_{\rm G} = -Q$):
$$\dot{\rho}_{\rm dm} + 3H\rho_{\rm dm} = -Q, \qquad \dot{\rho}_{\rm de} + 3H(1 + w)\rho_{\rm de} = +Q, \qquad \dot{\rho}_b + 3H\rho_b = 0.$$

## (b2) Effective Equations of State `[Established | Tier 1]`
$$w_{\rm dm}^{\rm eff}(a) = \frac{Q}{3H\rho_{\rm dm}}, \qquad w_{\rm de}^{\rm eff}(a) = w(a) - \frac{Q}{3H\rho_{\rm de}}.$$
For $Q > 0$, $w_{\rm dm}^{\rm eff} > 0$ (dark matter dilutes faster than $a^{-3}$) and $w_{\rm de}^{\rm eff} < w(a)$ (energy injection lowers the effective equation of state of dark energy).

## (b5-S) Locked v1 Mechanism: The Static Form (Transit Efficiency, $Q \equiv 0$) `[Model Ansatz | Tier 3 | Assumption A4]`
In the pre-registered v1 model, $f_{\rm leak} \in [0, 1)$ is a constant geometric transmission loss across the inter-string gap ($Q(a) \equiv 0$):
$$\rho_{\rm dm}(a) = (1 - f_{\rm leak})\,N_{\rm in}\,\rho_b(a) = 6(1 - f_{\rm leak})\,\rho_{b,0}\,a^{-3}, \qquad N_{\rm in} = 6.$$
1. **Zero Ratio Drift:** $\mathcal{R}_{\rm static}(a) \equiv \frac{\rho_{\rm dm}(a)}{\rho_b(a)} = 6(1 - f_{\rm leak}) = \text{const}$ at all scale factors $a > 0$ ($d\mathcal{R}_{\rm static}/da = 0$).
2. **Bookkeeping of Non-Diluting Tension (Assumption [A4]):** A naive epoch-by-epoch addition of $6f_{\rm leak}\rho_b(a) \propto a^{-3}$ to $\rho_{\rm de}(a)$ would dilute as pressureless dust ($w = 0$). In the Static Form, the 19-string geometry acts as a **boundary partition of stress-energy modes**: $(1 - f_{\rm leak})$ of the 6 inner interfaces transmits transverse Newtonian attraction proportional to localized baryon density ($\Omega_{\rm dm} = \frac{6}{19}(1 - f_{\rm leak})$, diluting as $a^{-3}$), while the remaining strand capacity ($\Omega_{\rm de,0} = \frac{12 + 6f_{\rm leak}}{19}$) is stored as bulk longitudinal helical tension governed by its intrinsic equation of state $w(a)$ (Section 4). Consequently, the share match $\Omega_b : \Omega_{\rm dm} : \Omega_{\rm de} = 1 : 6(1 - f_{\rm leak}) : (12 + 6f_{\rm leak})$ holds only near $a = 1$ today (Section 6), while $\mathcal{R}(a) = 6(1 - f_{\rm leak})$ holds at all epochs.
3. **Exact Validity of Compressed CMB Priors:** Because $\rho_{\rm dm}(a) \propto a^{-3}$ and $Q = 0$ at all redshifts $z \in [0, \infty)$, pre-recombination physics is 100% standard and the Chen, Huang & Wang (2019) compressed CMB distance priors $(R, \ell_A)$ are strictly valid.

## (b3, b4, b5-T) Transfer Form Analysis (Dynamic IDE, $Q > 0$) `[Established IDE / Model Ansatz | Tier 2 & 3 | Assumption A5]`
If the leak is modeled instead as a continuous energy transfer $Q > 0$ starting from an un-leaked initial ratio $\mathcal{R}(a_i) = 6$ at $a = a_i$ and accumulating a comoving transferred fraction
$$f_{\rm leak} = 1 - \frac{\rho_{\rm dm}(1)}{\rho_{\rm dm}(a_i)\,a_i^3} = \frac{1}{6\rho_{b,0}}\int_{a_i}^1 \frac{Q(a)\,a^2}{H(a)}\,da,$$
subject to the non-rising dark energy density requirement today ($\dot{\rho}_{\rm de}(t_0) \le 0 \iff w_{\rm de}^{\rm eff}(1) \ge -1$), the four published couplings behave as follows:

1. **$Q_{\rm dm} = \xi_m H \rho_{\rm dm}$ ($\xi_m > 0$):**
   - **Background Evolution & Ratio Drift:** $\rho_{\rm dm}(a) = \rho_{\rm dm,0}\,a^{-(3+\xi_m)}$ and $\mathcal{R}(z) = 6(1 - f_{\rm leak})(1 + z)^{\xi_m}$ with $\xi_m = -\frac{\ln(1 - f_{\rm leak})}{\ln(1 + z_i)}$.
   - **Negative Dark Energy Pathology:** Integrating (b1) for constant bare $w < 0$ yields
     $$\rho_{\rm de}(a) = \left(\rho_{\rm de,0} + \frac{\xi_m\,\rho_{\rm dm,0}}{3|w| + \xi_m}\right)a^{-3(1+w)} - \frac{\xi_m\,\rho_{\rm dm,0}}{3|w| + \xi_m}\,a^{-(3+\xi_m)},$$
     which becomes **strictly negative ($\rho_{\rm de}(a) < 0$)** for $a < a_{\rm neg} = \left(1 + \frac{3|w|+\xi_m}{\xi_m}\frac{\Omega_{\rm de,0}}{\Omega_{\rm dm,0}}\right)^{-\frac{1}{3|w|+\xi_m}}$ ($z_{\rm neg} \approx 5.6$ for $f_{\rm leak} = 1/6, z_i = 1089, w = -1$).
   - **Early-Time Perturbation Instability & Invalidity of Compressed CMB Priors:** The Gavela et al. (2009) doom factor $d = -\frac{\xi_m\rho_{\rm dm}}{3(1+w)\rho_{\rm de}}$ diverges at $a = a_{\rm neg}$ and changes sign, triggering early-time super-Hubble curvature blow-up (Valiviita, Majerotto & Maartens 2008). Because $\rho_{\rm dm} \propto a^{-(3+\xi_m)}$ alters pre-recombination expansion and $r_s(z_*)$, compressed CMB priors $(R, \ell_A)$ are invalid for $Q_{\rm dm}$.

2. **$Q_{\rm de} = \xi_e H \rho_{\rm de}$ ($\xi_e > 0$):**
   - **Background Evolution:** $\rho_{\rm de}(a) = \rho_{\rm de,0}\,a^{-3(1 + w_{\rm de}^{\rm eff})}$ with $w_{\rm de}^{\rm eff} = w - \frac{\xi_e}{3}$ (strictly positive $\rho_{\rm de}(a) > 0$ for all $a > 0$). Non-rising density today ($\dot{\rho}_{\rm de}(t_0) \le 0$) requires $0 < \xi_e \le 3(1 + w_0)$.
   - **Shadow Evolution & Late-Time Ratio Drift:**
     $$\mathcal{R}(a) = \mathcal{R}_0 + \frac{\xi_e}{3|w_{\rm de}^{\rm eff}|}\frac{\Omega_{\rm de,0}}{\Omega_{b,0}}\left(1 - a^{3|w_{\rm de}^{\rm eff}|}\right).$$
     Because $a_*^{3|w_{\rm de}^{\rm eff}|} \sim 10^{-9}$ at $z_* = 1089$, almost zero transfer occurs before recombination; all transfer happens at $z \lesssim 1$. Generating $f_{\rm leak} = 1/6$ dynamically requires $\xi_e = \frac{3|w_{\rm de}^{\rm eff}|f_{\rm leak}}{2 + f_{\rm leak}} \approx \frac{3}{13} \approx 0.2308$, which implies $\mathcal{R}(z_*) = 6.0$ at recombination vs. $\mathcal{R}(0) = 5.0$ today.
   - **Perturbation Stability:** For $\xi_e > 0$ and bare $w > -1$, the doom factor is $d = -\frac{\xi_e}{3(1 + w)} < 0$, which lies inside the **instability-free branch** of Gavela et al. (2009).

3. **$Q_{\rm rate} = \Gamma \rho_{\rm dm}$ ($\Gamma > 0$):** Yields $\mathcal{R}(t) = 6\,e^{-\Gamma t}$ ($\Gamma t_0 = -\ln(1 - f_{\rm leak}) \approx 0.1823$), turns $\rho_{\rm de}(a) < 0$ at early times, triggers perturbation instabilities, and violates Planck + BAO decaying-DM bounds ($\Gamma^{-1} \gtrsim 150\text{–}260\text{ Gyr}$) by $> 5\sigma$.

4. **Full Boltzmann Route (`CLASS`/`CAMB`) Requirement for Pre-Recombination Couplings:** Any model with pre-recombination $Q \ne 0$ cannot use compressed priors $(R, \ell_A)$ and instead requires evolving the coupled synchronous-gauge linear perturbation equations $\nabla_\nu T^{\mu\nu}_{(A)} = Q^\mu_{(A)}$ in `CLASS` (`perturbations.c`) with rest-frame dark-energy sound speed $c_{s,{\rm de}}^2 = 1$ and PPF phantom-crossing closure against full Planck 2018 likelihoods:
   $$\delta'_{\rm dm} + \theta_{\rm dm} + \frac{h'}{2} = -\frac{aQ}{\rho_{\rm dm}}\left(\frac{\delta Q}{Q} - \delta_{\rm dm}\right), \qquad \theta'_{\rm dm} + \mathcal{H}\theta_{\rm dm} = 0,$$
   $$\delta'_{\rm de} + 3\mathcal{H}\left(c_{s,{\rm de}}^2 - w\right)\delta_{\rm de} + (1 + w)\left(\theta_{\rm de} + \frac{h'}{2}\right) + 3\mathcal{H}(1 + w)\left(c_{s,{\rm de}}^2 - c_a^2\right)\frac{\theta_{\rm de}}{k^2}\mathcal{H} = +\frac{aQ}{\rho_{\rm de}}\left(\frac{\delta Q}{Q} - \delta_{\rm de}\right),$$
   $$\theta'_{\rm de} + \left[\mathcal{H}(1 - 3c_{s,{\rm de}}^2) + \frac{aQ}{\rho_{\rm de}}\frac{1 + c_{s,{\rm de}}^2}{1 + w}\right]\theta_{\rm de} - \frac{k^2 c_{s,{\rm de}}^2}{1 + w}\delta_{\rm de} = \frac{aQ}{(1 + w)\rho_{\rm de}}\,\theta_{\rm dm}.$$

---

# 4. Section (c): The Fixed Dark-to-Ordinary Ratio and the Ratio Tension

**Section Tier:** **Tier 1** for (c1); **Tier 3** for (c2)–(c4), with the $1:6:12$ budget match labeled **numerology**.

## (c1) Standard Uncoupled Dark-to-Ordinary Ratio `[Established | Tier 1 | Assumption A18]`
$$\mathcal{R} \equiv \frac{\rho_{\rm dm}(a)}{\rho_b(a)} = \frac{\omega_c}{\omega_b} = \text{const}.$$
From Planck 2018 (`TT,TE,EE+lowE+lensing`, Planck Collaboration 2020, Table 2), $\omega_b = 0.02237 \pm 0.00015$ and $\omega_c = 0.1200 \pm 0.0012$, giving
$$\mathcal{R}_{\rm Planck} = \frac{0.1200}{0.02237} = 5.36 \pm 0.065 \quad (\text{errors propagated in quadrature as registered in T2}).$$

## (c2) Model Dark-to-Ordinary Ratio `[Model Ansatz | Tier 3 | Assumption A6]`
$$\mathcal{R}_{\rm model} = N_{\rm in}(1 - f_{\rm leak}) = 6(1 - f_{\rm leak}).$$

## (c3) Present-Day Cosmic Budget Shares `[Model Ansatz | Tier 3 | Numerology | Assumptions A3, A7]`
$$\Omega_b = \frac{1}{N_s} = \frac{1}{19}, \qquad \Omega_{\rm dm} = \frac{6(1 - f_{\rm leak})}{19}, \qquad \Omega_{\rm de} = \frac{12 + 6 f_{\rm leak}}{19}, \qquad N_s = 19, \qquad \Omega_b + \Omega_{\rm dm} + \Omega_{\rm de} = 1.$$

## (c4) Pre-Registered Fixing and Testing Relation for $f_{\rm leak}$ (Test T2) `[Model Ansatz | Tier 3]`
From (c3), the model's total pressureless matter share today is $\Omega_m = \Omega_b + \Omega_{\rm dm} = \frac{7 - 6f_{\rm leak}}{19}$. Inverting yields:
$$f_{\rm leak} = 1 - \frac{19\,\Omega_m - 1}{6} = \frac{7 - 19\,\Omega_m}{6}, \qquad \sigma_f = \frac{19}{6}\,\sigma_{\Omega_m},$$
$$\mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak}) = 19\,\Omega_m - 1, \qquad \sigma_{\mathcal{R}_{\rm pred}} = 6\,\sigma_f = 19\,\sigma_{\Omega_m}.$$
**Test T2 Criterion:** $\text{PASS}$ if $|\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm Planck}| \le 2\sigma_{\rm comb}$ in both the Pantheon+ and DES-Dovekie runs, where $\sigma_{\rm comb} = \sqrt{(6\sigma_f)^2 + \sigma_{\rm Planck}^2}$ and $\sigma_{\rm Planck} = 0.065$; $\text{FAIL}$ otherwise.

## Plain Mathematical Statement of the Ratio Tension (Open Problem 10)
Because the parameter-free baryon share $\Omega_b = 1/19 = 0.05263$ is **$6.75\%$ higher** than Planck's measured $\Omega_b = \omega_b/h^2 = 0.04930 \pm 0.00086$, one value of $f_{\rm leak}$ cannot match both $\Omega_m$ and $\mathcal{R} = \omega_c/\omega_b$:
- Matching the cosmic shares ($\Omega_m = 6/19 \approx 0.3158$ at $f_{\rm leak} = 1/6$) predicts $\mathcal{R}_{\rm pred} = 5.00$, which sits **$5.5\sigma_{\rm Planck}$ below $\mathcal{R}_{\rm Planck} = 5.36 \pm 0.065$**.
- Matching $\mathcal{R}_{\rm Planck} = 5.36$ requires $f_{\rm leak} = 0.1067$, which forces $\Omega_m = (1 + 5.36)/19 = 0.3347$, missing Planck's $\Omega_m = 0.3153 \pm 0.0073$ by $+2.7\sigma$.

---

# 5. Section (d): The Unwinding — Outer-Ring Tension and CPL Mapping

**Section Tier:** **Tier 1** for (d1, d2); **Tier 3** for (d3–d5).

## (d1 & d2) Cosmological Tension and Uncoupled Equation of State `[Established | Tier 1]`
$$p_{\rm de} = w(a)\,\rho_{\rm de}c^2, \qquad w(a) = -1 - \frac{1}{3}\frac{d\ln\rho_{\rm de}}{d\ln a} = -1 - \frac{1}{3}\frac{d\ln g(a)}{d\ln a}.$$

## (d3) Twist–Tension Power Law `[Model Ansatz | Tier 3 | Assumption A8]`
$$g(a) \equiv \frac{\rho_{\rm de}(a)}{\rho_{\rm de,0}} = \left(\frac{\theta(a)}{\theta_0}\right)^n \quad (n > 0) \implies w(a) = -1 - \frac{n}{3}\frac{d\ln\theta}{d\ln a} = -1 - \frac{n}{3H(a)}\frac{\dot{\theta}}{\theta}.$$
For any uncoupled ($Q = 0$) monotonic unwinding ($\dot{\theta} < 0, n > 0$), **$w(a) > -1$ at all epochs $a > 0$** (never crosses $w = -1$).

## (d4 & d5) $(w_0, w_a)$ Relations for Three Unwinding Laws `[Model Ansatz | Tier 3 | Assumption A9]`
Using $w_0 \equiv w(1)$ and $w_a \equiv -\left.\frac{dw}{da}\right|_{a=1}$:

1. **Law 1 (d4 Baseline — Constant Cosmic-Time Relaxation Rate, $\dot{\theta} = -\Gamma_u\theta$, $\Gamma_u > 0$):**
   $$w(a) = -1 + \frac{n\Gamma_u}{3H_0\,E(a)}, \qquad w_0 = -1 + \frac{n\Gamma_u}{3H_0} > -1, \qquad w_a = -\frac{3}{2}(1 + w_0)\left[\Omega_m + (1 + w_0)(1 - \Omega_m)\right] < 0.$$
   Here $n$ and $\Gamma_u$ are completely degenerate in $\gamma_u \equiv \frac{n\Gamma_u}{3H_0} = 1 + w_0$, so **Law 1 predicts a 1D curve (narrow band over $\Omega_m$) in the $(w_0 > -1, w_a < 0)$ quadrant** with slope $\left.\frac{dw_a}{dw_0}\right|_{w_0=-1} = -\frac{3}{2}\Omega_m \approx -0.474$.
2. **Law 2 (Alternative A — Nonlinear Viscoelastic Torque, $\dot{\theta} = -\Gamma_u\theta_0(\theta/\theta_0)^p$, $p > 0$):**
   $$w(a) = -1 + (1 + w_0)\,\frac{\left[g(a)\right]^q}{E(a)}, \qquad w_a = -\frac{3}{2}(1 + w_0)\left[\Omega_m + \left(1 - \Omega_m - 2q\right)(1 + w_0)\right], \qquad q \equiv \frac{p - 1}{n}.$$
3. **Law 3 (Alternative B — Expansion-Driven Pitch Stretching, $\frac{d\ln\theta}{d\ln a} = -\alpha_u a^\beta$, $\alpha_u > 0, \beta \ge 0$):**
   $$w(a) = -1 + (1 + w_0)\,a^\beta, \qquad w_0 = -1 + \frac{n\alpha_u}{3} > -1, \qquad w_a = -\beta(1 + w_0) \le 0.$$
   For $\beta = 1$, $w(a) = w_0 - (1 + w_0)(1 - a)$ is exact CPL at all redshifts with $w_a = -(1 + w_0)$ and $w(a \to 0) = -1$. More generally, any uncoupled monotonic unwinding law respecting $w(0) = w_0 + w_a \ge -1$ lies inside the **Uncoupled Non-Phantom Wedge** $w_0 > -1, -(1 + w_0) \le w_a \le 0$.

## (d-Exp) EXPLORATORY: Unwinding (d4) + Stable Transfer Coupling ($Q_{\rm de} = \xi_e H \rho_{\rm de}$) `[Model Ansatz | Tier 2/3 | EXPLORATORY — Not Pre-Registered in v1]`
Combining bare unwinding $w_{\rm bare}(a) = -1 + \frac{\gamma_u}{E(a)}$ ($\gamma_u = \frac{n\Gamma_u}{3H_0} > 0$) with $Q_{\rm de} = \xi_e H \rho_{\rm de}$ ($\xi_e > 0$) via (b2) yields:
$$w_{\rm de}^{\rm eff}(a) = -1 + \frac{\gamma_u}{E(a)} - \frac{\xi_e}{3}, \qquad w_0^{\rm eff} = -1 + \gamma_u - \frac{\xi_e}{3}, \qquad w_a^{\rm eff} = -\frac{3}{2}\left(1 + w_0^{\rm eff} + \frac{\xi_e}{3}\right)\left[\Omega_m + \left(1 + w_0^{\rm eff}\right)(1 - \Omega_m)\right].$$
For $\gamma_u > \frac{\xi_e}{3} > 0$, dark energy weakens today ($w_0^{\rm eff} > -1$), crosses $w_{\rm de}^{\rm eff} = -1$ at redshift $E(z_{\rm cross}) = \frac{3\gamma_u}{\xi_e} = 1 + \frac{3(1 + w_0^{\rm eff})}{\xi_e} > 1$, and exhibits an effective phantom past ($w_{\rm de}^{\rm eff}(z) < -1$ for $z > z_{\rm cross}$, i.e., a rise-then-fall density history, Open Problem 11) while keeping bare tension non-phantom ($w_{\rm bare} > -1$) and linear perturbations stable ($d < 0$).

---

# 6. Section (e): The Shadow in Merging Galaxy Clusters

**Section Tier:** **Tier 1** for (e1, e2); **Tier 2** for nonlocal kernel precedent (Hehl & Mashhoon 2009); **Tier 3** for (e3–e7).

## (e1–e5) Convolved Velocity-Extrapolated Shadow Density `[Established (e1, e2) / Model Ansatz (e3–e5) | Tier 1 & 3 | Assumptions A10, A12]`
$$\nabla^2\Phi(\mathbf{x}, t) = 4\pi G\left[\rho_b(\mathbf{x}, t) + \rho_{\rm sh}(\mathbf{x}, t)\right], \qquad \rho_{\rm sh}(\mathbf{x}, t) = 6(1 - f_{\rm leak})\int_{\mathbb{R}^3} d^3y\;K_\sigma(\mathbf{x} - \mathbf{y})\,\tilde{\rho}_b(\mathbf{y}, t),$$
$$\tilde{\rho}_b(\mathbf{y}, t) = \sum_j m_j\,\delta^3\!\left(\mathbf{y} - \left[\mathbf{x}_j(t - \tau_{\rm lag}) + \mathbf{v}_j(t - \tau_{\rm lag})\,\tau_{\rm lag}\right]\right), \qquad K_\sigma(\mathbf{r}) = \left(2\pi\sigma_{\rm ref}^2\right)^{-3/2}\exp\!\left(-\frac{|\mathbf{r}|^2}{2\sigma_{\rm ref}^2}\right).$$

## (e6 & e7) Dynamical Merger Model and Explicit $\beta(T; \tau_{\rm lag})$ `[Model Ansatz | Tier 3 | Assumptions A12, A13, A14]`
Along the 1D merger axis $+x$ with pericenter at $t = t_p$ ($x = 0, v_p > 0$), time since pericenter $T \equiv t - t_p \ge 0$, stellar mass fraction $f_S = 1 - f_G$, gas mass fraction $f_G = \frac{M_G}{M_S + M_G}$, and $\mathcal{R} = 6(1 - f_{\rm leak})$:
$$\tilde{x}_c(T; \tau_{\rm lag}) = x_c(T - \tau_{\rm lag}) + v_c(T - \tau_{\rm lag})\,\tau_{\rm lag}, \qquad \Delta\tilde{x}_c(T; \tau_{\rm lag}) \equiv \tilde{x}_c(T; \tau_{\rm lag}) - x_c(T) = -\int_{T - \tau_{\rm lag}}^{T} (T - t')\,\ddot{x}_c(t')\,dt'.$$
With $\delta_{SG}(T) \equiv x_G(T) - x_S(T) = -|\delta_{SG}(T)| < 0$, $\delta_{SI}(T) \equiv x_I(T) - x_S(T)$, and $\beta(T) \equiv \frac{\delta_{SI}(T)}{\delta_{SG}(T)}$, the T4a projected offset (positive = ahead of stars, away from gas) is $\Delta_{SI}^{\parallel}(T) = |\delta_{SG}(T)|(-\beta(T))$.
- **Stellar Extrapolation Shift $\Delta\tilde{x}_S(T; \tau_{\rm lag})$:**
  - *Terminal pre-pericenter infall + post-pericenter deceleration $a_{\rm dec} > 0$ (Assumption **[A13a]**):*
    $$\Delta\tilde{x}_S^{\rm (A13a)}(T; \tau_{\rm lag}) = \begin{cases} +\frac{1}{2}a_{\rm dec}T^2 > 0, & 0 < T \le \tau_{\rm lag}, \\ +\frac{1}{2}a_{\rm dec}\tau_{\rm lag}^2 > 0, & T > \tau_{\rm lag}. \end{cases}$$
  - *Symmetric harmonic core passage $x_S(t) = \frac{v_p}{\omega_0}\sin(\omega_0 t)$ (Assumption **[A13b]**):*
    $$\Delta\tilde{x}_S^{\rm (A13b)}(T; \tau_{\rm lag}) = \frac{1}{6}\omega_0^2 v_p\,\tau_{\rm lag}^2\left(3T - 2\tau_{\rm lag}\right) + \mathcal{O}(\omega_0^4\tau_{\rm lag}^5),$$
    which is negative for $0 < T < \frac{2}{3}\tau_{\rm lag}$ and positive for $\frac{2}{3}\tau_{\rm lag} < T \le \tau_{\rm lag}$.
- **Explicit Fractional Offset Curve $\beta(T; \tau_{\rm lag})$:**
  - *Global Centroids:*
    $$\beta_{\rm centroid}(T; \tau_{\rm lag}) = \begin{cases}
    \displaystyle \frac{f_G}{1 + \mathcal{R}} - \frac{\mathcal{R}}{1 + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|}, & 0 < T \le \tau_{\rm lag}, \\[10pt]
    \displaystyle f_G - \frac{\mathcal{R}}{1 + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|}, & T > \tau_{\rm lag} \quad (\text{impulsive shock A14a}), \\[10pt]
    \displaystyle f_G\left[1 - \frac{\mathcal{R}}{1 + \mathcal{R}}\left(\frac{\tau_{\rm lag}}{T}\right)^2\right] - \frac{\mathcal{R}}{1 + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|}, & T > \tau_{\rm lag} \quad (\text{continuous drag A14b}).
    \end{cases}$$
  - *Resolved Lensing Convergence Peaks ($|\delta_{SG}| \gtrsim \sigma_{\rm ref}$):*
    $$\beta_{\rm peak}(T; \tau_{\rm lag}) = -\frac{\mathcal{R}}{f_S + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|} \quad (0 < T \le \tau_{\rm lag}), \qquad \beta_{\rm peak}(T; \tau_{\rm lag}) \to 1 \quad (T > \tau_{\rm lag}).$$

---

# 7. Section (f): Galaxy Rotation Curves, the Cap Theorem, and Orbital Extrapolation

**Section Tier:** **Tier 1** for (f1, f2); **Tier 3** for (f3, f4).

## (f1 & f2) Spherical Circular Speed and Empirical RAR Benchmark `[Established | Tier 1 | Assumption A15]`
$$v_c^2(r) = v_{\rm bar}^2(r) + v_{\rm sh}^2(r) = \frac{G\left[M_b(< r) + M_{\rm sh}(< r)\right]}{r}, \qquad v_{\rm bar}^2(r) = v_{\rm gas}|v_{\rm gas}| + 0.5\,v_{\rm disk}^2 + 0.7\,v_{\rm bul}^2,$$
$$g_{\rm obs}^{\rm RAR}(r) = \frac{g_{\rm bar}(r)}{1 - \exp\!\left(-\sqrt{g_{\rm bar}(r)/g_\dagger}\right)}, \qquad g_\dagger = 1.20\times 10^{-10}\text{ m s}^{-2}.$$

## (f3) Enclosed Shadow Mass Kernel and the Saturation Cap Theorem `[Model Ansatz | Tier 3 | Assumptions A15, A16]`
For any galaxy with radial baryonic mass distribution $dM_b(r')$, the spherical enclosed shadow mass under the 3D isotropic Gaussian kernel (e5) is
$$M_{\rm sh}(< r) = 6(1 - f_{\rm leak})\int_0^\infty \mathcal{F}_\sigma(r, r')\,dM_b(r'),$$
$$\mathcal{F}_\sigma(r, r') = \frac{1}{2}\left[\operatorname{erf}\!\left(\frac{r + r'}{\sqrt{2}\,\sigma_{\rm ref}}\right) + \operatorname{erf}\!\left(\frac{r - r'}{\sqrt{2}\,\sigma_{\rm ref}}\right)\right] - \sqrt{\frac{2}{\pi}}\,\frac{\sigma_{\rm ref}}{r'}\left[\exp\!\left(-\frac{(r - r')^2}{2\sigma_{\rm ref}^2}\right) - \exp\!\left(-\frac{(r + r')^2}{2\sigma_{\rm ref}^2}\right)\right].$$
- **Registered Variants in Test T5:** **T5-A:** universal constant $\sigma_{\rm ref}$ in kpc; **T5-B:** scaled width $\sigma_{\rm ref} = k\,R_d$ with universal dimensionless constant $k$ and SPARC disk scale length $R_d$.
- **Saturation Cap Theorem:** Because $K_\sigma$ is normalized to $1$ and acts as a 3D diffusion operator, for any isolated galaxy with outward-decreasing spherically averaged baryon density, $M_{\rm sh}(< r) \le 6(1 - f_{\rm leak})M_b(< r)$ at all radii $r > 0$, enforcing the strict ceiling:
  $$\frac{g_{\rm obs}(r)}{g_{\rm bar}(r)} = 1 + \frac{M_{\rm sh}(< r)}{M_b(< r)} \le 1 + 6(1 - f_{\rm leak}) \underset{f_{\rm leak}=1/6}{=} 6.0 \qquad \forall\,r > 0.$$
  Isolated galaxies in T5 therefore cannot reach the $g_{\rm obs}/g_{\rm bar} > 6$ regime observed at the low-acceleration end of SPARC ($g_{\rm bar} \lesssim 3\times 10^{-12}\text{ m s}^{-2}$).

## (f4) Carried Motion on Circular Orbits `[Model Ansatz Analysis | Tier 3 | Assumption A16]`
$$r_{\rm ext} = r\sqrt{1 + \left(\frac{v_c\,\tau_{\rm lag}}{r}\right)^2}, \qquad v_c\,\tau_{\rm lag} = 30.68\text{ kpc}\times\left(\frac{v_c}{200\text{ km s}^{-1}}\right)\left(\frac{\tau_{\rm lag}}{150\text{ Myr}}\right).$$
Because $t_{\rm orb}/(2\pi) = r/v_c \sim 15\text{ Myr} \ll \tau_{\rm lag} \ge 150\text{ Myr}$ violates Carlip (2000)'s uniform-motion condition and a rotating axisymmetric disk has stationary coarse-grained density ($\partial\rho_b/\partial t = 0$), the galaxy-frame scalar source density is unshifted ($\tilde{\rho}_b(\mathbf{x}) = \rho_b(\mathbf{x})$) as registered in Test T5.

---

# 8. Sections (g), (h), and (i): Locality, Coincidence Window, and Parameter Table

## (g1–g4) Difference Bubbles and Regional $H_0$ Estimator `[Established (g1) / Model Ansatz (g2–g4) | Tier 1 & 3 | Assumptions A10, A20]`
$$\chi_{\rm diff}(z; z_s) = D_M(z_s) - D_M(z), \qquad R_{\rm diff}(z; z_s) = \frac{D_M(z_s) - D_M(z)}{1 + z} \underset{\Delta t \ll H^{-1}}{\approx} c\,\Delta t_{\rm split}.$$
In Test T6, across the 12 HEALPix $N_{\rm side} = 1$ sky regions with frozen SH0ES calibrator absolute magnitude $M_B^{\rm fixed}$ and Pantheon+ Hubble-flow covariance block $\mathbf{C}_{\rm HF}$ ($0.023 \le z_{\rm HD} \le 0.15$), the log-Hubble vector $\eta_i = 5\log_{10} H_{0,i}$ is estimated by generalized least squares:
$$\hat{\boldsymbol{\eta}} = \left(\mathbf{P}^T \mathbf{C}_{\rm HF}^{-1} \mathbf{P}\right)^{-1} \mathbf{P}^T \mathbf{C}_{\rm HF}^{-1} \mathbf{y}, \qquad \mathbf{C}_\eta = \left(\mathbf{P}^T \mathbf{C}_{\rm HF}^{-1} \mathbf{P}\right)^{-1}, \qquad \chi^2_{\rm het} = \left(\hat{\mathbf{H}}_0 - \bar{H}_0\mathbf{1}\right)^T \mathbf{C}_{H_0}^{-1} \left(\hat{\mathbf{H}}_0 - \bar{H}_0\mathbf{1}\right) \quad (\text{dof} = 11).$$

## (h1 & h2) Coincidence Window Method `[Established (h1) / Diagnostic (h2) | Tier 1 & 3 | Assumption A11]`
$$\Omega_b(a) = \frac{\Omega_{b,0}\,a^{-3}}{E^2(a)}, \qquad \Omega_{\rm dm}(a) = \frac{\Omega_{{\rm dm},0}\,a^{-3}}{E^2(a)}, \qquad \Omega_{\rm de}(a) = \frac{\Omega_{{\rm de},0}\,g(a)}{E^2(a)}, \qquad \Delta t_{\rm coinc} = \frac{1}{H_0}\int_{a_{\rm min}}^{a_{\rm max}} \frac{da}{a\,E(a)},$$
evaluated for Criterion H-Abs ($\max_i |\Omega_i(a) - s_i^{\rm target}| \le 0.05$) and Criterion H-Rel ($\max_i |\Omega_i(a) - s_i^{\rm target}|/s_i^{\rm target} \le 0.10$).

## (i-Exp) Measurable Linear-Growth Form for $\epsilon_{\rm far}$ `[Model Ansatz | Tier 3 | Assumption A17 | Proposal for v2]`
For an unclustered far-string shadow fraction $\epsilon_{\rm far} = \Omega_{\rm dm,far}/\Omega_{\rm dm} \ll 1$ with $\sigma_{\rm far} \gg 10\text{ Mpc}$:
$$f(a) \simeq \left[\Omega_m(a)\right]^{\gamma_L}\left(1 - \frac{3}{5}\frac{\Omega_{\rm dm}}{\Omega_m}\epsilon_{\rm far}\right), \qquad \frac{S_8^{\rm LSS} - S_8^{\rm CMB}}{S_8^{\rm CMB}} \simeq -\frac{3}{5}\frac{\Omega_{\rm dm}}{\Omega_m}\ln\!\left(\frac{1 + z_{\rm eq}}{1 + z_{\rm de}}\right)\epsilon_{\rm far} \approx -3.8\,\epsilon_{\rm far}.$$

## (i) Master Parameter Table

| Parameter | Symbol | Role / Status in v1 | Fixing Dataset (`FIX`) | Testing Dataset (`TEST`) | Test ID |
|---|---|---|---|---|---|
| Strings per strand | $N_s = 19$ | Structural constant ($1+6+12$); never varied | None (geometry) | Planck 2018 shares (numerology only) | None |
| Strings per rope | $N_r = 133$ | Structural constant ($7\times 19$); never varied | None (geometry) | No v1 observable | None |
| Transit leak fraction | $f_{\rm leak}$ | $f_{\rm leak} = 1 - \frac{19\Omega_m - 1}{6}$ (Static Form $Q=0$) | DESI DR2 BAO + CMB $(R, \ell_A)$ + SNe (Pantheon+ / DES-Dovekie separately) + BBN $\omega_b$ | Planck 2018 $\omega_c/\omega_b = 5.36 \pm 0.065$ vs. $\mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak})$ | **T2** |
| CPL Dark Energy | $w_0, w_a$ | Unwinding summary ($w_0 > -1$ tested; $w_a < 0$ expected) | Sign fixed by model; Planck 2018 supplies CMB prior | DESI DR2 BAO + Ly$\alpha$ (incl. AP) + Pantheon+ (Run 1) / DES-Dovekie (Run 2) | **T1** |
| Unwinding rate / exp | $n\Gamma_u$ | Degenerate product $\gamma_u = \frac{n\Gamma_u}{3H_0} = 1 + w_0$ in Law 1 | Not registered separately in v1 | Implies 1D curve $w_a(w_0; \Omega_m)$ | (Report) |
| IDE Coupling | $\xi_e$ | Exploratory transfer $Q_{\rm de} = \xi_e H \rho_{\rm de}$ | **Not registered in v1 (Exploratory)** | Candidate for v2 phantom-crossing test | None |
| Far-string fraction | $\epsilon_{\rm far}$ | Smooth shadow fraction ($\Delta S_8/S_8 \approx -3.8\epsilon_{\rm far}$) | **Not registered in v1 (Proposal)** | Candidate for v2 $S_8 / f\sigma_8$ test | None |
| Shadow crossing lag | $\tau_{\rm lag}$ | Universal delay ($\ge 150\text{ Myr}$) | Bullet Cluster lower bound (T4a); Bullet + training half of aged mergers (T4b) | Harvey et al. 2015 & Wittman et al. 2018 (T4a); test half of aged mergers (T4b) | **T4a, T4b** |
| Refraction halo width | $\sigma_{\rm ref}$ | 3D Gaussian kernel width (kpc) | SPARC training half (odd indices, 88 galaxies) | SPARC held-out half (even indices, 87 galaxies) + NGC 1052-DF2 (T5c) | **T5-A, T5c** |
| Scaled halo width | $k$ | $\sigma_{\rm ref} = k\,R_d$ | SPARC training half (odd indices, 88 galaxies) | SPARC held-out half (even indices, 87 galaxies) | **T5-B** |

---

# 9. $\Lambda\text{CDM}$ and Newtonian Recovery Limits

1. **Background Expansion Recovery of $\Lambda\text{CDM}$:**  
   In the Static Form ($Q = 0$), taking the zero-unwinding limit $\Gamma_u \to 0^+$ (or $n \to 0^+$) gives $w_0 \to -1$, $w_a \to 0$, and $g(a) \to 1$. With $\Omega_m = \Omega_b + \Omega_{\rm dm} = \frac{7 - 6f_{\rm leak}}{19}$ and $\Omega_\Lambda = \frac{12 + 6f_{\rm leak}}{19}$, the Friedmann equation (a2) recovers flat $\Lambda\text{CDM}$ identically at all redshifts $z \in [0, \infty)$.
2. **Transfer-Form Recovery of Static Form:**  
   Taking $\xi_m \to 0^+, \xi_e \to 0^+, \Gamma \to 0^+$ gives $Q(a) \to 0$, recovering standard uncoupled conservation $\rho_{\rm dm} \propto a^{-3}$ and $w_{\rm de}^{\rm eff}(a) \to w(a)$.
3. **Cluster Merger Recovery of Collisionless CDM ($\tau_{\rm lag} \to 0^+$ vs. $\tau_{\rm lag} \to \infty$):**  
   - As $\tau_{\rm lag} \to 0^+$, $\tilde{x}_S(T) \to x_S(T)$ and $\tilde{x}_G(T) \to x_G(T)$ at all $T > 0$, so the shadow tracks the instantaneous baryons ($\beta_{\rm centroid} \to f_G$).
   - For $0 < T < \tau_{\rm lag}$ in the limit of negligible core acceleration ($\omega_0\tau_{\rm lag} \to 0$), $\Delta\tilde{x}_S \to 0$ and $\beta_{\rm peak} \to 0$, recovering the collisionless CDM peak position on the galaxies.
4. **Galaxy Rotation Curve Recovery Limits ($\sigma_{\rm ref} \to 0^+$ and $\sigma_{\rm ref} \to \infty$):**  
   - As $\sigma_{\rm ref} \to 0^+$, $\mathcal{F}_\sigma(r, r') \to \Theta(r - r')$ and $v_c^2(r) \to [1 + 6(1 - f_{\rm leak})]v_{\rm bar}^2(r)$ (constant mass-follows-light boost).
   - As $\sigma_{\rm ref} \to \infty$, $\mathcal{F}_\sigma(r, r') \to 0$ at any finite radius $r$ and $v_c^2(r) \to v_{\rm bar}^2(r)$ (pure Newtonian baryons with no dark halo).

---

# 10. Complete Registry of Stage 1 Assumptions (`[A1]`–`[A20]`)

- **[A1] Flat FLRW Background Geometry (`Tier 1`):** Spatially flat ($k = 0$), homogeneous, isotropic metric (a1), identifying cosmic time $t$ with the physical preferred present ("the blade", `Tier 3`) without altering metric observables. Drives (a1)–(a5); T1, T2, T6.
- **[A2] Standard Relativistic Species & Massive Neutrinos (`Tier 1`):** $T_{\rm CMB,0} = 2.7255\text{ K}$, $N_{\rm eff} = 3.044$, $\sum m_\nu = 0.06\text{ eV}$. Drives (a2), (a5); T1, T2.
- **[A3] Negligible Present-Day Radiation/Neutrino Share in 1:6:12 Closure (`Tier 3`):** $\Omega_b + \Omega_{\rm dm} + \Omega_{\rm de} = 1$ in (c3)–(c4) neglects $\Omega_{\gamma,0} \approx 5\times 10^{-5}$ and absorbs/neglects $\Omega_{\nu,0} \approx 0.0014$ in $\Omega_m$. Drives (c3), (c4); T2.
- **[A4] Static-Form Leak as Boundary Stress-Energy Partition (`Tier 3`, Model Ansatz):** In the locked v1 Static Form ($Q = 0$), $(1 - f_{\rm leak})$ is the constant transverse transmission efficiency of the 6 touching neighbors' baryon pull ($\rho_{\rm dm} = 6(1 - f_{\rm leak})\rho_b \propto a^{-3}$), while $\Omega_{\rm de,0} = (12 + 6f_{\rm leak})/19$ is partitioned into bulk longitudinal string tension governed by $w(a)$. Drives (b5-S), (c2)–(c4), validity of $(R, \ell_A)$ priors; T2, T5.
- **[A5] Transfer-Form Initial Condition and Non-Rising Density Constraint (`Tier 3`, Exploratory Alternative):** In dynamic IDE ($Q > 0$), $\mathcal{R}(a_i) = 6$ transfers cumulative fraction $f_{\rm leak}$ by $a = 1$ subject to $\dot{\rho}_{\rm de}(t_0) \le 0$. Drives (b1)–(b5-T), (d-Exp).
- **[A6] Cosmological Homogeneity of the Six Touching Neighbors (`Tier 3`, Model Ansatz):** Averaged over cosmological volumes, $\bar{\rho}_b^{(k)}(a) = \bar{\rho}_b(a)$ and $f_{\rm leak}^{(k)} = f_{\rm leak}$ for $k = 1,\dots,6$. Drives (b5), (c2), (e4); T2, T4, T5.
- **[A7] Fixed Strand Geometry $N_s = 19$ and $N_r = 133$ (`Tier 3`, Model Ansatz / Numerology):** Planar equal-circle packing ($1+6+12=19$) maps directly to present-day budget shares (c3). Drives (c2)–(c4), Open Problem 10; T2.
- **[A8] Power-Law Dependence of Tension on Strand Twist (`Tier 3`, Model Ansatz):** $\rho_{\rm de}(a) = \rho_{\rm de,0}(\theta(a)/\theta_0)^n$ with $n > 0$ and $\dot{\theta} < 0$. Drives (d3)–(d5); T1.
- **[A9] Candidate Unwinding Rate Laws (`Tier 3`, Model Ansatz):** Baseline constant relaxation rate $\dot{\theta} = -\Gamma_u\theta$ (Law 1 / d4) and alternatives (Law 2 nonlinear torque, Law 3 expansion-driven pitch). Drives (d4), (d5); T1.
- **[A10] Causal Difference Bubbles & Macroscopic Neighbor Identity (`Tier 3`, Model Ansatz):** $R_{\rm diff}(z; z_s) = [D_M(z_s) - D_M(z)]/(1+z)$ is sub-galactic or microscopic for the 6 touching neighbors, so $\rho_b^{(k)}(\mathbf{x}, t) = \rho_b(\mathbf{x}, t)$ on scales $\gtrsim 1\text{ kpc}$. Drives (g1)–(g3), (e4); T4a, T4b, T5.
- **[A11] Fixed Pre-Registered Tolerances for the Coincidence Window (`Tier 3`, Diagnostic Rule):** Criterion H-Abs ($\Delta_{\rm abs} = 0.05$) and Criterion H-Rel ($\delta_{\rm rel} = 0.10$). Drives (h2).
- **[A12] Substitution of $\tau_{\rm lag}$ into Linear Velocity Extrapolation (`Tier 3`, Model Ansatz):** $\tilde{\mathbf{x}}_j(t) = \mathbf{x}_j(t - \tau_{\rm lag}) + \mathbf{v}_j(t - \tau_{\rm lag})\tau_{\rm lag}$ with universal $\tau_{\rm lag} > 0$, neglecting $\mathcal{O}(\mathbf{a}\tau_{\rm lag}^2)$. Drives (e2)–(e7), (f4); T4a, T4b.
- **[A13] Pre-Pericenter vs. Post-Pericenter Merger Kinematics (`Tier 3`, Dynamical Merger Model):** Terminal pre-pericenter infall with post-pericenter deceleration (**[A13a]**) gives $\Delta\tilde{x}_S > 0$ for all $0 < T \le \tau_{\rm lag}$; symmetric harmonic core passage (**[A13b]**) gives $\Delta\tilde{x}_S < 0$ for $0 < T < \frac{2}{3}\tau_{\rm lag}$ and $\Delta\tilde{x}_S > 0$ for $\frac{2}{3}\tau_{\rm lag} < T \le \tau_{\rm lag}$. Drives (e6), (e7); T4a, T4b.
- **[A14] Collisional Gas Shock / Ram-Pressure Profile (`Tier 3`, Dynamical Merger Model):** Impulsive pericenter velocity drop (**[A14a]**) or continuous deceleration (**[A14b]**) governs the transition of $\beta(T; \tau_{\rm lag})$ at $T > \tau_{\rm lag}$. Drives (e6), (e7); T4b.
- **[A15] Isolated Galaxy Approximation, Spherical Circular Speed, and Fixed SPARC $M/L$ (`Tier 1 & 3`, Pre-Registered T5 Rule):** $\Upsilon_{\rm disk} = 0.5, \Upsilon_{\rm bul} = 0.7$, isolated galaxies (except DF2 in T5c), enforcing the diffusive cap $g_{\rm obs}/g_{\rm bar} \le 1 + 6(1 - f_{\rm leak})$. Drives (f1), (f3); T5-A, T5-B, T5c.
- **[A16] Stationarity of Axisymmetric Rotating Disks Over $\tau_{\rm lag}$ (`Tier 3`, Model Ansatz):** Bound circular orbits with $r/v_c \ll \tau_{\rm lag}$ have stationary coarse-grained disk density $\tilde{\rho}_b(\mathbf{x}) = \rho_b(\mathbf{x})$ in the galaxy rest frame. Drives (f3), (f4); T5-A, T5-B.
- **[A17] Far-String Contribution $\epsilon_{\rm far}$ as Smooth Shadow Component (`Tier 3`, Exploratory Proposal for v2):** $\Omega_{\rm dm,far} = \epsilon_{\rm far}\Omega_{\rm dm}$ with $\sigma_{\rm far} \gg 10\text{ Mpc}$ suppresses linear growth ($\Delta S_8/S_8 \approx -3.8\epsilon_{\rm far}$). Not used in v1 tests.
- **[A18] Uncorrelated Error Propagation for $\mathcal{R}_{\rm Planck}$ (`Tier 1/3`, Pre-Registered T2 Rule):** $\mathcal{R}_{\rm Planck} = 5.36 \pm 0.065$ and $\sigma_{\rm comb} = \sqrt{(19\sigma_{\Omega_m})^2 + 0.065^2}$. Drives (c4); T2.
- **[A19] Full-Sample SPARC Primary Split (`Tier 3`, Pre-Registered G8 Resolution):** All 175 SPARC galaxies ordered alphabetically by name (odd = 88 training, even = 87 test), with the 153-galaxy quality-cut sample reported alongside for the RAR benchmark. Drives T5-A, T5-B.
- **[A20] HEALPix $N_{\rm side} = 1$ Coordinate Convention (`Tier 3`, Pre-Registered G8 Resolution):** Galactic $(l, b)$ `RING` ordering on Pantheon+ Hubble-flow SNe ($0.023 \le z_{\rm HD} \le 0.15$, non-calibrators) with full Pantheon+ covariance. Drives (g4); T6.
