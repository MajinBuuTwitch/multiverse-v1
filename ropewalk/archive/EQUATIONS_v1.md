---
title: "MULTIVERSE Stage 1 Tightened Equations (EQUATIONS.md)"
subtitle: "Complete Mathematical Formulation of the Mandarano Model (v1.0.1)"
author: "Gregory Mandarano / WickedAI — Mathematical Derivations by Gemini 4 Argon"
date: "2026-10-30"
---

> **Note for Cold Reviewer:** This file (`EQUATIONS.md`, specified in `MULTIVERSE_ARGON_HANDOFF.txt` B6/B7) is identical in mathematical content to `MULTIVERSE_STAGE1_EQUATIONS.md` (specified in `SESSION_BOOTSTRAP_HANDOFF.md`), ensuring that every tightened equation, label (`[Established]` or `[Model Ansatz]`), tier tag, $\Lambda\text{CDM}$/Newtonian recovery limit, parameter table, and assumption reference (`[A1]`–`[A20]`) is present in both locations.

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

## (b5-S) Locked v1 Mechanism: The Static Form (Transit Efficiency, $Q \equiv 0$) `[Model Ansatz | Tier 3 | Assumption A4]`
In the pre-registered v1 model, $f_{\rm leak} \in [0, 1)$ is a constant geometric transmission loss across the inter-string gap ($Q(a) \equiv 0$):
$$\rho_{\rm dm}(a) = (1 - f_{\rm leak})\,N_{\rm in}\,\rho_b(a) = 6(1 - f_{\rm leak})\,\rho_{b,0}\,a^{-3}, \qquad N_{\rm in} = 6, \qquad \mathcal{R}_{\rm static}(a) \equiv \frac{\rho_{\rm dm}(a)}{\rho_b(a)} = 6(1 - f_{\rm leak}) = \text{const}.$$
Under Assumption **[A4]**, the 19-string geometry partitions the strand's stress-energy modes at the boundary level into transverse Newtonian shadow attraction ($\Omega_{\rm dm} = \frac{6}{19}(1 - f_{\rm leak})$, diluting as $a^{-3}$) and longitudinal outer-ring tension ($\Omega_{\rm de,0} = \frac{12 + 6f_{\rm leak}}{19}$, evolving with $g(a)$). Because $\rho_{\rm dm}(a) \propto a^{-3}$ at all epochs, pre-recombination physics is standard and the Chen, Huang & Wang (2019) compressed CMB distance priors $(R, \ell_A)$ are strictly valid.

## (b3, b4, b5-T) Transfer Form Analysis (Dynamic IDE, $Q > 0$) `[Established IDE / Model Ansatz | Tier 2 & 3 | Assumption A5]`
1. **$Q_{\rm dm} = \xi_m H \rho_{\rm dm}$ ($\xi_m > 0$):** Gives $\rho_{\rm dm}(a) = \rho_{\rm dm,0}\,a^{-(3+\xi_m)}$, $\mathcal{R}(z) = 6(1 - f_{\rm leak})(1 + z)^{\xi_m}$, and
   $$\rho_{\rm de}(a) = \left(\rho_{\rm de,0} + \frac{\xi_m\,\rho_{\rm dm,0}}{3|w| + \xi_m}\right)a^{-3(1+w)} - \frac{\xi_m\,\rho_{\rm dm,0}}{3|w| + \xi_m}\,a^{-(3+\xi_m)},$$
   which turns negative at $z > z_{\rm neg} \approx 5.6$, triggers the Valiviita et al. (2008) early-time super-Hubble perturbation instability, and invalidates compressed CMB priors $(R, \ell_A)$.
2. **$Q_{\rm de} = \xi_e H \rho_{\rm de}$ ($\xi_e > 0$):** Gives $\rho_{\rm de}(a) = \rho_{\rm de,0}\,a^{-3(1 + w - \xi_e/3)} > 0$, is perturbation-stable for $\xi_e > 0$ and bare $w > -1$ ($d = -\frac{\xi_e}{3(1+w)} < 0$, Gavela et al. 2009), and yields late-time ratio evolution
   $$\mathcal{R}(a) = \mathcal{R}_0 + \frac{\xi_e}{3|w_{\rm de}^{\rm eff}|}\frac{\Omega_{\rm de,0}}{\Omega_{b,0}}\left(1 - a^{3|w_{\rm de}^{\rm eff}|}\right).$$
3. **$Q_{\rm rate} = \Gamma \rho_{\rm dm}$ ($\Gamma > 0$):** Gives $\mathcal{R}(t) = 6\,e^{-\Gamma t}$, turns $\rho_{\rm de} < 0$ at early times, and violates decaying-DM bounds for $f_{\rm leak} \approx 1/6$.

---

# 4. Section (c): The Fixed Dark-to-Ordinary Ratio and the Ratio Tension

## (c1) Standard Uncoupled Ratio `[Established | Tier 1 | Assumption A18]`
$$\mathcal{R} \equiv \frac{\rho_{\rm dm}(a)}{\rho_b(a)} = \frac{\omega_c}{\omega_b} = \text{const}, \qquad \mathcal{R}_{\rm Planck} = \frac{0.1200}{0.02237} = 5.36 \pm 0.065.$$

## (c2–c4) Model Ratio, Shares, and Pre-Registered T2 Relation `[Model Ansatz | Tier 3 | Numerology | Assumptions A3, A6, A7]`
$$\mathcal{R}_{\rm model} = 6(1 - f_{\rm leak}), \qquad \Omega_b = \frac{1}{19}, \qquad \Omega_{\rm dm} = \frac{6(1 - f_{\rm leak})}{19}, \qquad \Omega_{\rm de} = \frac{12 + 6 f_{\rm leak}}{19},$$
$$\Omega_m = \Omega_b + \Omega_{\rm dm} = \frac{7 - 6 f_{\rm leak}}{19} \implies f_{\rm leak} = 1 - \frac{19\,\Omega_m - 1}{6}, \qquad \sigma_f = \frac{19}{6}\,\sigma_{\Omega_m},$$
$$\mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak}) = 19\,\Omega_m - 1, \qquad \sigma_{\mathcal{R}_{\rm pred}} = 6\,\sigma_f = 19\,\sigma_{\Omega_m}.$$
**Ratio Tension (Open Problem 10):** Because $\Omega_b = 1/19 = 0.05263$ exceeds Planck's $\Omega_b = 0.04930$ by $6.75\%$, $f_{\rm leak} = 1/6$ ($\Omega_m = 6/19 \approx 0.3158$) predicts $\mathcal{R}_{\rm pred} = 5.00$ ($5.5\sigma_{\rm Planck}$ below $5.36$), whereas matching $\mathcal{R}_{\rm Planck} = 5.36$ requires $f_{\rm leak} = 0.1067$ ($\Omega_m = 0.3347$).

---

# 5. Section (d): The Unwinding — Outer-Ring Tension and CPL Mapping

## (d1–d3) Tension Equation of State `[Established (d1, d2) / Model Ansatz (d3) | Tier 1 & 3 | Assumption A8]`
$$w(a) = -1 - \frac{1}{3}\frac{d\ln g(a)}{d\ln a}, \qquad g(a) = \left(\frac{\theta(a)}{\theta_0}\right)^n \quad (n > 0) \implies w(a) = -1 - \frac{n}{3H(a)}\frac{\dot{\theta}}{\theta}.$$

## (d4 & d5) CPL Parameters $(w_0, w_a)$ for Unwinding Laws `[Model Ansatz | Tier 3 | Assumption A9]`
- **Law 1 (d4 Baseline, $\dot{\theta} = -\Gamma_u\theta$):**
  $$w(a) = -1 + \frac{n\Gamma_u}{3H_0\,E(a)}, \qquad w_0 = -1 + \frac{n\Gamma_u}{3H_0} > -1, \qquad w_a = -\frac{3}{2}(1 + w_0)\left[\Omega_m + (1 + w_0)(1 - \Omega_m)\right] < 0.$$
- **Law 2 (Nonlinear Torque, $\dot{\theta} = -\Gamma_u\theta_0(\theta/\theta_0)^p$):**
  $$w(a) = -1 + (1 + w_0)\,\frac{\left[g(a)\right]^q}{E(a)}, \qquad w_a = -\frac{3}{2}(1 + w_0)\left[\Omega_m + \left(1 - \Omega_m - 2q\right)(1 + w_0)\right], \qquad q \equiv \frac{p - 1}{n}.$$
- **Law 3 (Expansion-Driven Pitch, $\frac{d\ln\theta}{d\ln a} = -\alpha_u a^\beta$):**
  $$w(a) = -1 + (1 + w_0)\,a^\beta, \qquad w_0 = -1 + \frac{n\alpha_u}{3} > -1, \qquad w_a = -\beta(1 + w_0) \le 0.$$
- **EXPLORATORY Unwinding + $Q_{\rm de} = \xi_e H \rho_{\rm de}$ (`[Not Pre-Registered in v1]`):**
  $$w_{\rm de}^{\rm eff}(a) = -1 + \frac{\gamma_u}{E(a)} - \frac{\xi_e}{3}, \qquad w_0^{\rm eff} = -1 + \gamma_u - \frac{\xi_e}{3}, \qquad w_a^{\rm eff} = -\frac{3}{2}\left(1 + w_0^{\rm eff} + \frac{\xi_e}{3}\right)\left[\Omega_m + \left(1 + w_0^{\rm eff}\right)(1 - \Omega_m)\right],$$
  crossing $w_{\rm de}^{\rm eff} = -1$ at $E(z_{\rm cross}) = \frac{3\gamma_u}{\xi_e} = 1 + \frac{3(1 + w_0^{\rm eff})}{\xi_e} > 1$.

---

# 6. Section (e): The Shadow in Merging Galaxy Clusters

## (e1–e5) Convolved Velocity-Extrapolated Shadow `[Established (e1, e2) / Model Ansatz (e3–e5) | Tier 1 & 3 | Assumptions A10, A12]`
$$\nabla^2\Phi = 4\pi G\left(\rho_b + \rho_{\rm sh}\right), \qquad \rho_{\rm sh}(\mathbf{x}, t) = 6(1 - f_{\rm leak})\int_{\mathbb{R}^3} d^3y\;K_\sigma(\mathbf{x} - \mathbf{y})\,\tilde{\rho}_b(\mathbf{y}, t),$$
$$\tilde{\rho}_b(\mathbf{y}, t) = \sum_j m_j\,\delta^3\!\left(\mathbf{y} - \left[\mathbf{x}_j(t - \tau_{\rm lag}) + \mathbf{v}_j(t - \tau_{\rm lag})\,\tau_{\rm lag}\right]\right), \qquad K_\sigma(\mathbf{r}) = \left(2\pi\sigma_{\rm ref}^2\right)^{-3/2}\exp\!\left(-\frac{|\mathbf{r}|^2}{2\sigma_{\rm ref}^2}\right).$$

## (e6 & e7) Dynamical Merger Offset $\beta(T; \tau_{\rm lag})$ `[Model Ansatz | Tier 3 | Assumptions A12, A13, A14]`
With $\Delta\tilde{x}_c(T; \tau_{\rm lag}) \equiv \tilde{x}_c(T; \tau_{\rm lag}) - x_c(T) = -\int_{T - \tau_{\rm lag}}^T (T - t')\ddot{x}_c(t')\,dt'$, $\mathcal{R} = 6(1 - f_{\rm leak})$, $f_G = \frac{M_G}{M_S + M_G}$, $\delta_{SG}(T) = x_G(T) - x_S(T) < 0$, and $\Delta_{SI}^{\parallel}(T) = |\delta_{SG}(T)|(-\beta(T))$:
$$\beta_{\rm centroid}(T; \tau_{\rm lag}) = \begin{cases}
\displaystyle \frac{f_G}{1 + \mathcal{R}} - \frac{\mathcal{R}}{1 + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|}, & 0 < T \le \tau_{\rm lag}, \\[10pt]
\displaystyle f_G - \frac{\mathcal{R}}{1 + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|}, & T > \tau_{\rm lag} \quad (\text{impulsive shock A14a}), \\[10pt]
\displaystyle f_G\left[1 - \frac{\mathcal{R}}{1 + \mathcal{R}}\left(\frac{\tau_{\rm lag}}{T}\right)^2\right] - \frac{\mathcal{R}}{1 + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|}, & T > \tau_{\rm lag} \quad (\text{continuous drag A14b}),
\end{cases}$$
$$\beta_{\rm peak}(T; \tau_{\rm lag}) = -\frac{\mathcal{R}}{f_S + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|} \quad (0 < T \le \tau_{\rm lag}), \qquad \beta_{\rm peak}(T; \tau_{\rm lag}) \to 1 \quad (T > \tau_{\rm lag}).$$

---

# 7. Section (f): Galaxy Rotation Curves, Cap Theorem, and Orbital Extrapolation

## (f1–f4) Enclosed Shadow Mass and Saturation Cap `[Established (f1, f2) / Model Ansatz (f3, f4) | Tier 1 & 3 | Assumptions A15, A16]`
$$v_c^2(r) = v_{\rm bar}^2(r) + \frac{G\,M_{\rm sh}(< r)}{r}, \qquad M_{\rm sh}(< r) = 6(1 - f_{\rm leak})\int_0^\infty \mathcal{F}_\sigma(r, r')\,dM_b(r'),$$
$$\mathcal{F}_\sigma(r, r') = \frac{1}{2}\left[\operatorname{erf}\!\left(\frac{r + r'}{\sqrt{2}\,\sigma_{\rm ref}}\right) + \operatorname{erf}\!\left(\frac{r - r'}{\sqrt{2}\,\sigma_{\rm ref}}\right)\right] - \sqrt{\frac{2}{\pi}}\,\frac{\sigma_{\rm ref}}{r'}\left[\exp\!\left(-\frac{(r - r')^2}{2\sigma_{\rm ref}^2}\right) - \exp\!\left(-\frac{(r + r')^2}{2\sigma_{\rm ref}^2}\right)\right],$$
$$\frac{g_{\rm obs}(r)}{g_{\rm bar}(r)} = 1 + \frac{M_{\rm sh}(< r)}{M_b(< r)} \le 1 + 6(1 - f_{\rm leak}) \quad \forall\,r > 0, \qquad r_{\rm ext} = r\sqrt{1 + \left(\frac{v_c\,\tau_{\rm lag}}{r}\right)^2}.$$

---

# 8. Sections (g), (h), and (i): Locality, Coincidence Window, and $\epsilon_{\rm far}$

## (g1–g4) Difference Bubbles and HEALPix $N_{\rm side} = 1$ Regional $H_0$ `[Established / Model Ansatz | Tier 1 & 3 | Assumptions A10, A20]`
$$R_{\rm diff}(z; z_s) = \frac{D_M(z_s) - D_M(z)}{1 + z}, \qquad \hat{\boldsymbol{\eta}} = \left(\mathbf{P}^T \mathbf{C}_{\rm HF}^{-1} \mathbf{P}\right)^{-1} \mathbf{P}^T \mathbf{C}_{\rm HF}^{-1} \mathbf{y}, \qquad \chi^2_{\rm het} = \left(\hat{\mathbf{H}}_0 - \bar{H}_0\mathbf{1}\right)^T \mathbf{C}_{H_0}^{-1} \left(\hat{\mathbf{H}}_0 - \bar{H}_0\mathbf{1}\right).$$

## (h1 & h2) Coincidence Time Span `[Established (h1) / Diagnostic (h2) | Tier 1 & 3 | Assumption A11]`
$$\Omega_i(a) = \frac{\rho_i(a)}{\rho_{\rm crit}(a)}, \qquad \Delta t_{\rm coinc} = \frac{1}{H_0}\int_{a_{\rm min}}^{a_{\rm max}} \frac{da}{a\,E(a)}.$$

## (i-Exp) Measurable Form for $\epsilon_{\rm far}$ `[Model Ansatz | Tier 3 | Assumption A17 | Proposal for v2]`
$$f(a) \simeq \left[\Omega_m(a)\right]^{\gamma_L}\left(1 - \frac{3}{5}\frac{\Omega_{\rm dm}}{\Omega_m}\epsilon_{\rm far}\right), \qquad \frac{S_8^{\rm LSS} - S_8^{\rm CMB}}{S_8^{\rm CMB}} \simeq -3.8\,\epsilon_{\rm far}.$$
