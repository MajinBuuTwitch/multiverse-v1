---
title: "MULTIVERSE Stage 1 Tightened Equations, Assumptions, Parameter Table, and Recovery Limits"
subtitle: "Single Governing Mathematical Formulation of the Mandarano Model (v1.0.2, Revised Post-Review V3)"
author: "Gregory Mandarano / WickedAI (Model Author) — Mathematical Derivations by Gemini 4 Argon"
date: "2026-10-30"
---

# Overview, Precedence Clause, & Cold-Reviewer Orientation

This document (`MULTIVERSE_STAGE1_EQUATIONS.md`) is the **single governing Stage 1 mathematical formulation** of the **Mandarano Model** ("the cable", package version 1.0.2), revised to resolve all findings of the three independent pre-data cold reviews (`REVIEW_COLD.md`, `REVIEW_V2.md`, `REVIEW_V3.md`) before any dataset was downloaded and before any analysis code was written.

> **Precedence Clause (Resolving Finding N3):** Where `PREREG.md` and any earlier or companion file (`MULTIVERSE_TESTS_v1.md`, `MULTIVERSE_ARGON_HANDOFF.txt`, `GEMINI.md` Rule R12, or any `STAGE1_PART*.md` file) disagree on a test definition, sample split, prior, statistic, threshold, or decision rule, **`PREREG.md` governs and `MULTIVERSE_TESTS_v1.md` is superseded for every test it shares with `PREREG.md`**. `MULTIVERSE_STAGE1_EQUATIONS.md` governs all mathematical equations. The `STAGE1_PART*.md` files are historical derivation notes with no governing force.

Every equation in this document carries:
1. **Honesty Classification:** `[Established]` (standard published physics, mathematics, or empirical fits) or `[Model Ansatz]` (a form chosen to represent the Mandarano Model).
2. **Tier Tag:** **Tier 1** (established physics and measurements), **Tier 2** (peer-reviewed published speculation), or **Tier 3** (this model). The $1:6:12$ cosmic budget match is explicitly labeled **numerology**.
3. **Explicit Assumption Cross-References:** `[A1]` through `[A20]`, listed in full in Section 10 and in `ASSUMPTIONS.md`.
4. **$\Lambda\text{CDM}$ and Newtonian Recovery Limits:** Summarized in Section 9.

Where an exploratory theoretical extension is derived (such as combining strand unwinding with the perturbation-stable interacting dark energy coupling $Q_{\rm de} = \xi_e H \rho_{\rm de}$ in Section 5.4, or the linear-growth signature of $\epsilon_{\rm far}$ in Section 8.3), it is explicitly marked **`[EXPLORATORY — Not Pre-Registered in v1]`** and may never be used in the pre-registered v1 tests.

---

# 1. Conventions and Shared Parameter Names

- **Metric & Cosmological Coordinates:** Spatially flat FLRW geometry ($k = 0$), cosmic time $t$, overdot $\dot{} \equiv d/dt$, scale factor $a(t)$ normalized to $a_0 \equiv a(t_0) = 1$ today, redshift $1 + z = 1/a$, Hubble rate $H(t) \equiv \dot{a}/a$, dimensionless expansion rate $E(a) \equiv H(a)/H_0$, present critical density $\rho_{\rm crit,0} \equiv \frac{3H_0^2}{8\pi G}$, dimensionless density shares $\Omega_i \equiv \frac{\rho_{i,0}}{\rho_{\rm crit,0}}$, physical density parameters $\omega_i \equiv \Omega_i h^2$ with $h \equiv \frac{H_0}{100\text{ km s}^{-1}\text{ Mpc}^{-1}}$.
- **Subscripts & Matter Share Distinction (Finding m7):** $b$ = ordinary baryonic matter; $\rm dm$ (or $\rm sh$) = dark matter (the gravitational shadow of the six touching neighbor strings); $\rm de$ = dark energy (outer-ring strand tension); $\gamma$ = photons; $\nu$ = neutrinos; $r = \gamma + \nu_{\rm rel}$ = radiation; $\Omega_{bc} \equiv \Omega_b + \Omega_{\rm dm}$ = pressureless baryon-plus-cold-dark-matter share entering the $1:6:12$ strand budget; $\Omega_{m,{\rm tot}} \equiv \Omega_{bc} + \Omega_{\nu,0}$ = total non-relativistic matter today including massive neutrinos ($\Omega_{\nu,0} = \frac{\sum m_\nu}{93.14\,h^2\text{ eV}}$). Where $\Omega_m$ is written in late-time neglect of $\Omega_{\nu,0}$, its exact operational meaning ($\Omega_{bc}$ vs. $\Omega_{m,{\rm tot}}$) is stated in the equation.
- **Shared Parameter Names (Identical Across All Package Files):**
  $$N_s = 19, \qquad N_r = 133, \qquad f_{\rm leak}, \qquad \epsilon_{\rm far}, \qquad \gamma_u, \qquad w_0, \qquad w_a, \qquad \tau_{\rm lag}, \qquad \sigma_{\rm ref}.$$

---

# 2. Section (a): Background Cosmology

**Section Tier:** **Tier 1** for equations (a1)–(a5); **Tier 3** for the dark-sector mapping (a6).

## (a1) Flat FLRW Metric `[Established | Tier 1 | Assumption A1]`
$$ds^2 = -c^2\,dt^2 + a^2(t)\left[dr^2 + r^2\left(d\theta^2 + \sin^2\theta\,d\phi^2\right)\right].$$

## (a2) First Friedmann Equation `[Established | Tier 1 | Assumptions A1, A2]`
$$H^2(a) = \frac{8\pi G}{3}\sum_i \rho_i(a), \qquad E^2(a) \equiv \frac{H^2(a)}{H_0^2} = \Omega_\gamma a^{-4} + \Omega_\nu f_\nu(a) + \Omega_b a^{-3} + \Omega_{\rm dm} f_{\rm dm}(a) + \Omega_{\rm de}\,g(a),$$
subject to flatness closure $\Omega_\gamma + \Omega_{\nu,0} + \Omega_b + \Omega_{\rm dm} + \Omega_{\rm de} = 1$, where $g(a) \equiv \rho_{\rm de}(a)/\rho_{\rm de,0}$ ($g(1) = 1$) and $f_{\rm dm}(a) \equiv \rho_{\rm dm}(a)/\rho_{\rm dm,0}$. In the locked v1 **Static Form** of the leak ($Q = 0$, Section 3.3), dark matter is uncoupled and $f_{\rm dm}(a) = a^{-3}$ at all epochs:
$$E^2(a) = \Omega_\gamma a^{-4} + \Omega_\nu f_\nu(a) + \Omega_{bc}\,a^{-3} + \Omega_{\rm de}\,g(a), \qquad \Omega_{bc} \equiv \Omega_b + \Omega_{\rm dm}.$$
Here $\Omega_\gamma = 2.4728\times 10^{-5}/h^2$ (for $T_{\rm CMB,0} = 2.7255\text{ K}$) and $\Omega_\nu f_\nu(a)$ describes standard cosmic neutrinos with $N_{\rm eff} = 3.044$ and $\sum m_\nu = 0.06\text{ eV}$ (modeled with one massive eigenstate of $m_\nu = 0.06\text{ eV}$, $\Omega_{\nu,{\rm mass},0} = \frac{0.06}{93.14\,h^2}$, and two massless eigenstates, using the exact Fermi–Dirac phase-space integral $f_\nu(a)$).

## (a3) Uncoupled Fluid Continuity Equation `[Established | Tier 1]`
For any uncoupled fluid $i$ with equation of state $w_i(a) \equiv \frac{p_i(a)}{\rho_i(a)c^2}$,
$$\dot{\rho}_i + 3H\left(1 + w_i(a)\right)\rho_i = 0 \quad \Longleftrightarrow \quad \frac{d\ln\rho_i}{d\ln a} = -3\left(1 + w_i(a)\right).$$

## (a4) Chevallier–Polarski–Linder (CPL) Parametrization `[Established | Tier 1]`
For an uncoupled dark energy component with $w(a) = w_0 + w_a(1 - a) = w_0 + w_a\frac{z}{1+z}$ (Chevallier & Polarski 2001; Linder 2003), integrating (a3) yields
$$g_{\rm CPL}(a) = a^{-3(1 + w_0 + w_a)}\exp\!\left[-3w_a(1 - a)\right] = (1 + z)^{3(1 + w_0 + w_a)}\exp\!\left(-\frac{3w_a z}{1 + z}\right).$$

## (a5) Distance, Sound-Horizon, and Compressed CMB Observables (Findings M8, M9, N1, N7) `[Established | Tier 1 | Assumptions A1, A2]`
$$D_M(z) = \frac{c}{H_0}\int_0^z \frac{dz'}{E(z')}, \qquad D_H(z) = \frac{c}{H(z)}, \qquad D_V(z) = \left[z\,D_M^2(z)\,D_H(z)\right]^{1/3},$$
$$D_L(z) = (1 + z)\,D_M(z), \qquad \mu(z) = 5\log_{10}\!\left(\frac{D_L(z)}{1\text{ Mpc}}\right) + 25,$$
$$r_s(z) = \int_z^\infty \frac{c_s(z')}{H(z')}\,dz', \qquad c_s(z) = \frac{c}{\sqrt{3\left(1 + \frac{3\omega_b}{4\omega_\gamma(1 + z)}\right)}}, \qquad r_d \equiv r_s(z_d).$$
The recombination redshift $z_*$ (Hu & Sugiyama 1996, ApJ 471, 542, Eqs. E-1–E-2, matching Chen, Huang & Wang 2019 Eqs. 2.4–2.5) and baryon drag redshift $z_d$ (Eisenstein & Hu 1998, ApJ 496, 605, Eqs. 4–6; calibrated to `CLASS`/`CAMB` via the standard post-Planck drag-scale factor) are fixed in advance as:
$$z_* = 1048\left(1 + 0.00124\,\omega_b^{-0.738}\right)\left(1 + g_1\,\omega_m^{g_2}\right), \qquad g_1 = \frac{0.0783\,\omega_b^{-0.238}}{1 + 39.5\,\omega_b^{0.763}}, \qquad g_2 = \frac{0.560}{1 + 21.1\,\omega_b^{1.81}},$$
$$z_d = \frac{1291\,\omega_m^{0.251}}{1 + 0.659\,\omega_m^{0.828}}\left(1 + b_1\,\omega_b^{b_2}\right), \qquad b_1 = 0.313\,\omega_m^{-0.419}\left(1 + 0.607\,\omega_m^{0.674}\right), \qquad b_2 = 0.238\,\omega_m^{0.223},$$
where $\omega_m \equiv \Omega_{m,{\rm tot}}h^2 = (\Omega_{bc} + \Omega_{\nu,0})h^2$. The compressed CMB distance priors (Chen, Huang & Wang 2019, JCAP 02 (2019) 028, Table 1) at $z_*$ are
$$R = \frac{\sqrt{\Omega_{m,{\rm tot}} H_0^2}}{c}\,D_M(z_*) = \sqrt{\Omega_{m,{\rm tot}}}\int_0^{z_*}\frac{dz'}{E(z')}, \qquad \ell_A = \frac{\pi\,D_M(z_*)}{r_s(z_*)}, \qquad \omega_b = \Omega_b h^2.$$
*(In Test T1, the single registered deciding prior is the $\Lambda\text{CDM}$-derived Table 1 vector $\boldsymbol{\mu}_{\rm CMB}^{\Lambda{\rm CDM}} = (1.7502, 301.471, 2.236)^T$, while the $w\text{CDM}$-derived Table 1 vector $\boldsymbol{\mu}_{\rm CMB}^{w{\rm CDM}} = (1.7493, 301.462, 2.239)^T$ is a non-deciding sensitivity check. In Test T2-A, the single registered deciding fixing fit uses the conditional $2\times 2$ Gaussian likelihood $(R, \ell_A \mid \omega_b)$ coupled to the DESI DR2 / post-LUNA BBN prior $100\omega_b = 2.218 \pm 0.055$ per Findings M9 & N7 so that Planck's marginal $\omega_b$ prior is removed without introducing a $3.1\sigma_R$ pull from outdated BBN values.)*

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
2. **Bookkeeping of Non-Diluting Tension (Assumption [A4]):** A naive epoch-by-epoch addition of $6f_{\rm leak}\rho_b(a) \propto a^{-3}$ to $\rho_{\rm de}(a)$ would dilute as pressureless dust ($w = 0$). In the Static Form, the 19-string geometry acts as a **boundary partition of stress-energy modes**: $(1 - f_{\rm leak})$ of the 6 inner interfaces transmits transverse Newtonian attraction proportional to localized baryon density ($\Omega_{\rm dm} = \frac{6}{19}(1 - f_{\rm leak})$, diluting as $a^{-3}$), while the remaining strand capacity ($\Omega_{\rm de,0} = \frac{12 + 6f_{\rm leak}}{19}$) is stored as bulk longitudinal helical tension governed by its intrinsic equation of state $w(a)$ (Section 5). Consequently, the share match $\Omega_b : \Omega_{\rm dm} : \Omega_{\rm de} = 1 : 6(1 - f_{\rm leak}) : (12 + 6f_{\rm leak})$ holds only near $a = 1$ today (Section 8.2), while $\mathcal{R}(a) = 6(1 - f_{\rm leak})$ holds at all epochs.
3. **Exact Validity of Compressed CMB Priors:** Because $\rho_{\rm dm}(a) \propto a^{-3}$ and $Q = 0$ at all redshifts $z \in [0, \infty)$, pre-recombination physics is 100% standard and the Chen, Huang & Wang (2019) compressed CMB distance priors $(R, \ell_A)$ are strictly valid.

## (b3, b4, b5-T) Transfer Form Analysis (Dynamic IDE, $Q > 0$, Findings m2, m3, m6, m10) `[Established IDE / Model Ansatz | Tier 2 & 3 | Assumption A5]`
If the leak is modeled instead as a continuous energy transfer $Q > 0$ starting from an un-leaked initial ratio $\mathcal{R}(a_i) = 6$ at $a = a_i$ and accumulating a comoving transferred fraction
$$f_{\rm leak} = 1 - \frac{\rho_{\rm dm}(1)}{\rho_{\rm dm}(a_i)\,a_i^3} = \frac{1}{6\rho_{b,0}}\int_{a_i}^1 \frac{Q(a)\,a^2}{H(a)}\,da,$$
subject to the non-rising dark energy density requirement today ($\dot{\rho}_{\rm de}(t_0) \le 0 \iff w_{\rm de}^{\rm eff}(1) \ge -1$), all four published couplings in (b3) behave as follows:

1. **$Q_{\rm dm} = \xi_m H \rho_{\rm dm}$ ($\xi_m > 0$):**
   - **Background Evolution & Ratio Drift:** $\rho_{\rm dm}(a) = \rho_{\rm dm,0}\,a^{-(3+\xi_m)}$ and $\mathcal{R}(z) = 6(1 - f_{\rm leak})(1 + z)^{\xi_m}$ with $\xi_m = -\frac{\ln(1 - f_{\rm leak})}{\ln(1 + z_i)}$.
   - **Negative Dark Energy Pathology:** Integrating (b1) for constant bare $w < 0$ yields
     $$\rho_{\rm de}(a) = \left(\rho_{\rm de,0} + \frac{\xi_m\,\rho_{\rm dm,0}}{3|w| + \xi_m}\right)a^{-3(1+w)} - \frac{\xi_m\,\rho_{\rm dm,0}}{3|w| + \xi_m}\,a^{-(3+\xi_m)},$$
     which becomes **strictly negative ($\rho_{\rm de}(a) < 0$)** for $a < a_{\rm neg} = \left(1 + \frac{3|w|+\xi_m}{\xi_m}\frac{\Omega_{\rm de,0}}{\Omega_{\rm dm,0}}\right)^{-\frac{1}{3|w|+\xi_m}}$ ($z_{\rm neg} = 5.606$ at $w = -1$ and $z_{\rm neg} = 5.58$ at non-degenerate $w = -0.99$ for $f_{\rm leak} = 1/6, z_i = 1089$).
   - **Early-Time Perturbation Instability & Invalidity of Compressed CMB Priors:** For non-phantom bare $w > -1$ (e.g., $w = -0.99$), the Gavela et al. (2009) doom factor $d = -\frac{\xi_m\rho_{\rm dm}}{3(1+w)\rho_{\rm de}}$ diverges at $a = a_{\rm neg}$ ($z_{\rm neg} = 5.58$) and flips to $d > +1$ for $a < a_{\rm neg}$, triggering early-time super-Hubble curvature blow-up (Valiviita, Majerotto & Maartens 2008). Because $\rho_{\rm dm} \propto a^{-(3+\xi_m)}$ alters pre-recombination expansion and $r_s(z_*)$, compressed CMB priors $(R, \ell_A)$ are invalid for $Q_{\rm dm}$.

2. **$Q_{\rm de} = \xi_e H \rho_{\rm de}$ ($\xi_e > 0$):**
   - **Background Evolution:** $\rho_{\rm de}(a) = \rho_{\rm de,0}\,a^{-3(1 + w_{\rm de}^{\rm eff})}$ with $w_{\rm de}^{\rm eff} = w - \frac{\xi_e}{3}$ (strictly positive $\rho_{\rm de}(a) > 0$ for all $a > 0$). Non-rising density today ($\dot{\rho}_{\rm de}(t_0) \le 0$) requires $0 < \xi_e \le 3(1 + w_0)$.
   - **Shadow Evolution & Late-Time Ratio Drift:**
     $$\mathcal{R}(a) = \mathcal{R}_0 + \frac{\xi_e}{3|w_{\rm de}^{\rm eff}|}\frac{\Omega_{\rm de,0}}{\Omega_{b,0}}\left(1 - a^{3|w_{\rm de}^{\rm eff}|}\right).$$
     Because $a_*^{3|w_{\rm de}^{\rm eff}|} \sim 10^{-9}$ at $z_* = 1089$, almost zero transfer occurs before recombination; all transfer happens at $z \lesssim 1$. Generating $f_{\rm leak} = 1/6$ dynamically requires $\xi_e = \frac{3|w_{\rm de}^{\rm eff}|f_{\rm leak}}{2 + f_{\rm leak}} \approx \frac{3}{13} \approx 0.2308$, which implies $\mathcal{R}(z_*) = 6.0$ at recombination vs. $\mathcal{R}(0) = 5.0$ today.
   - **Perturbation Stability:** For $\xi_e > 0$ and bare $w > -1$, the doom factor is $d = -\frac{\xi_e}{3(1 + w)} < 0$, which lies inside the **instability-free branch** of Gavela et al. (2009).

3. **$Q_{\rm rate} = \Gamma \rho_{\rm dm}$ ($\Gamma > 0$):** Yields $\mathcal{R}(t) = 6\,e^{-\Gamma t}$ ($\Gamma t_0 = -\ln(1 - f_{\rm leak}) \approx 0.1823$, corresponding to $\Gamma^{-1} = t_0 / 0.1823 \approx 75.7\text{ Gyr}$ for $t_0 = 13.8\text{ Gyr}$). Like $Q_{\rm dm}$, it turns $\rho_{\rm de}(a) < 0$ at $z \gtrsim 2.3$ and triggers early-time perturbation instabilities ($d > 0$ for $a < a_{\rm neg}$). *(Note per Finding m3: published bounds $\Gamma^{-1} \gtrsim 150\text{–}260\text{ Gyr}$ apply to dark matter decaying into dark radiation $w_{\rm dr} = 1/3$, whereas $Q_{\rm rate}$ into dark energy is ruled out at the background and linear-perturbation level by its $z \gtrsim 2.3$ negative dark-energy density and Valiviita et al. 2008 adiabatic instability.)*

4. **$Q_{\rm field} = \beta_\phi \rho_{\rm dm}\dot{\phi} / M_{\rm Pl}$ (Wetterich 1995; Amendola 2000; Finding m6):** For a scalar twist field $\phi = M_{\rm Pl}\ln(\theta/\theta_0)$ with $\dot{\phi} = M_{\rm Pl}\dot{\theta}/\theta$, during any scaling or tracker regime where $\dot{\phi}/(H M_{\rm Pl}) \simeq \text{const}$, $Q_{\rm field}$ reduces directly to $Q_{\rm dm} = \xi_m H \rho_{\rm dm}$ with $\xi_m = \beta_\phi \dot{\phi}/(H M_{\rm Pl})$ and suffers the same early-time $\rho_{\rm de}(a) < 0$ and $d > 0$ curvature instability; under constant cosmic-time unwinding $\dot{\theta}/\theta = -\Gamma_u$ (Law 1), it reduces to $Q_{\rm rate} = \Gamma \rho_{\rm dm}$ with $\Gamma = -\beta_\phi\Gamma_u$. It also introduces an unregistered scalar potential $V(\phi)$ and coupling $\beta_\phi$.

5. **Full Boltzmann Route (`CLASS`/`CAMB`) Requirement for Pre-Recombination Couplings (Finding m2):** Any model with pre-recombination $Q \ne 0$ cannot use compressed priors $(R, \ell_A)$ and instead requires evolving the coupled synchronous-gauge linear perturbation equations $\nabla_\nu T^{\mu\nu}_{(A)} = Q^\mu_{(A)}$ in `CLASS` (`perturbations.c`) with rest-frame dark-energy sound speed $c_{s,{\rm de}}^2 = 1$ and PPF phantom-crossing closure against full Planck 2018 likelihoods:
   $$\delta'_{\rm dm} + \theta_{\rm dm} + \frac{h'}{2} = -\frac{aQ}{\rho_{\rm dm}}\left(\frac{\delta Q}{Q} - \delta_{\rm dm}\right), \qquad \theta'_{\rm dm} + \mathcal{H}\theta_{\rm dm} = 0,$$
   $$\delta'_{\rm de} + 3\mathcal{H}\left(c_{s,{\rm de}}^2 - w\right)\delta_{\rm de} + (1 + w)\left(\theta_{\rm de} + \frac{h'}{2}\right) + 9\mathcal{H}^2(1 + w)\left(c_{s,{\rm de}}^2 - c_a^2\right)\frac{\theta_{\rm de}}{k^2} = +\frac{aQ}{\rho_{\rm de}}\left(\frac{\delta Q}{Q} - \delta_{\rm de}\right),$$
   $$\theta'_{\rm de} + \left[\mathcal{H}(1 - 3c_{s,{\rm de}}^2) + \frac{aQ}{\rho_{\rm de}}\frac{1 + c_{s,{\rm de}}^2}{1 + w}\right]\theta_{\rm de} - \frac{k^2 c_{s,{\rm de}}^2}{1 + w}\delta_{\rm de} = \frac{aQ}{(1 + w)\rho_{\rm de}}\,\theta_{\rm dm}.$$

---

# 4. Section (c): The Fixed Dark-to-Ordinary Ratio, the $\Omega_b = 1/19$ Identity, and the Ratio Tension

**Section Tier:** **Tier 1** for (c1); **Tier 3** for (c2)–(c4), with the $1:6:12$ budget match labeled **numerology**.

## (c1) Standard Uncoupled Dark-to-Ordinary Ratio `[Established | Tier 1 | Assumption A18]`
$$\mathcal{R} \equiv \frac{\rho_{\rm dm}(a)}{\rho_b(a)} = \frac{\omega_c}{\omega_b} = \text{const}.$$
From Planck 2018 (`TT,TE,EE+lowE+lensing`, Planck Collaboration 2020, Table 2), $\omega_b = 0.02237 \pm 0.00015$ and $\omega_c = 0.1200 \pm 0.0012$, giving
$$\mathcal{R}_{\rm Planck} = \frac{0.1200}{0.02237} = 5.3643 \pm 0.0646 \quad (\text{registered in T2 as } 5.36 \pm 0.065\text{, errors propagated in quadrature}).$$

## (c2) Model Dark-to-Ordinary Ratio `[Model Ansatz | Tier 3 | Assumption A6]`
$$\mathcal{R}_{\rm model} = N_{\rm in}(1 - f_{\rm leak}) = 6(1 - f_{\rm leak}).$$

## (c3) Present-Day Cosmic Budget Shares `[Model Ansatz | Tier 3 | Numerology | Assumptions A3, A7]`
$$\Omega_b = \frac{1}{N_s} = \frac{1}{19}, \qquad \Omega_{\rm dm} = \frac{6(1 - f_{\rm leak})}{19}, \qquad \Omega_{\rm de} = \frac{12 + 6 f_{\rm leak}}{19}, \qquad N_s = 19, \qquad \Omega_b + \Omega_{\rm dm} + \Omega_{\rm de} = 1.$$

## (c4) Pre-Registered Fixing and Testing Relation for $f_{\rm leak}$ and Algebraic Identity (Findings M1, M2, N1, N7, N9) `[Model Ansatz | Tier 3]`
From (c3), the model's pressureless baryon-plus-CDM share today (explicitly excluding $\Omega_{\nu,0}$) is $\Omega_{bc} \equiv \Omega_b + \Omega_{\rm dm} = \Omega_{m,{\rm tot}} - \Omega_{\nu,0} = \frac{7 - 6f_{\rm leak}}{19}$. Inverting yields:
$$f_{\rm leak} = 1 - \frac{19\,\Omega_{bc} - 1}{6} = \frac{7 - 19\,\Omega_{bc}}{6}, \qquad \sigma_f = \frac{19}{6}\,\sigma_{\Omega_{bc}},$$
$$\mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak}) = 19\,\Omega_{bc} - 1, \qquad \sigma_{\mathcal{R}_{\rm pred}} = 6\,\sigma_f = 19\,\sigma_{\Omega_{bc}}, \qquad \sigma_{\rm comb} = \sqrt{\left(19\,\sigma_{\Omega_{bc}}\right)^2 + 0.065^2}.$$
- **Boundary Rule (Finding m12):** If an unclipped fit ever returns $\Omega_{bc} > 7/19 \approx 0.36842$ ($f_{\rm leak} < 0$), $f_{\rm leak}$ is reported as its raw negative value without clipping or reinterpretation.
- **Exact Algebraic Identity & Single Registered T2 Version (`N1`):** Because in any universe $\Omega_{bc} = \Omega_b(1 + \mathcal{R}_{\rm true})$, the T2 prediction is
  $$\mathcal{R}_{\rm pred} = 19\,\Omega_b\left(1 + \mathcal{R}_{\rm true}\right) - 1 \quad \Longrightarrow \quad \mathcal{R}_{\rm pred} = \mathcal{R}_{\rm true} \iff \Omega_b = \frac{1}{19}.$$
  Notice that $6(1 - f_{\rm leak})$ cancels identically out of $\mathcal{R}_{\rm pred} = 19\Omega_{bc} - 1$: **Test T2 (`T2-A`, the single deciding pillar test) is algebraically a test of $\Omega_b = 1/19$**, evaluated using the DESI DR2 / post-LUNA BBN prior ($100\omega_b = 2.218 \pm 0.055$) and the single uncorrelated error formula $\sigma_{\rm comb} = \sqrt{(19\sigma_{\Omega_{bc}})^2 + 0.065^2}$ (`PASS` if $|\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm Planck}| \le 2\sigma_{\rm comb}$ in both SN runs; `FAIL` if $> 2\sigma_{\rm comb}$ in either SN run). The self-consistent constrained fit **`T2-B`** ($\omega_b = h^2/19$ imposed inside the likelihood) and the Cooke et al. (2018) BBN prior are non-deciding sensitivity checks (`PREREG.md` §5.2).
- **Direct Parameter-Free Predictions of $\Omega_b = 1/19$ Registered Under Findings M2 & N9:**
  1. **Test `T2-N1` (Direct Baryon Share Check):** $\Omega_b^{\rm model} = \frac{1}{19} = 0.052632$ vs. Planck 2018 $\Omega_b = 0.04930 \pm 0.00086$: **already in $+3.87\sigma$ tension (Result: FAIL)**.
  2. **Test `T2-N2` (Implied Hubble Constant Check, Single Deciding Pair per N9 & Review V3 Minor 2):** Combining $\Omega_b = 1/19$ with $\omega_b \equiv \Omega_b h^2$ yields $H_0^{\rm pred} = 100\sqrt{19\omega_b}\text{ km s}^{-1}\text{ Mpc}^{-1}$. The single registered deciding comparison for `T2-N2` uses **Planck 2018 $100\omega_b = 2.237 \pm 0.015$** ($H_0^{\rm pred} = 65.19 \pm 0.22\text{ km s}^{-1}\text{ Mpc}^{-1}$) tested against **Planck 2018 $\Lambda\text{CDM}$ $H_0 = 67.36 \pm 0.54\text{ km s}^{-1}\text{ Mpc}^{-1}$** with uncorrelated error $\sigma_{\rm comb,H_0} = \sqrt{0.22^2 + 0.54^2} = 0.583\text{ km s}^{-1}\text{ Mpc}^{-1}$, which is in **$-3.72\sigma$ tension (Result: FAIL)** (and $7.4\sigma$ below SH0ES $73.04 \pm 1.04$; note that treating Planck's $\omega_b$ and $H_0$ from the same $\Lambda\text{CDM}$ chain as uncorrelated is conservative because their positive correlation makes the true tension larger than $3.72\sigma$). *(Sensitivity comparisons: using DESI/LUNA BBN $100\omega_b = 2.218 \pm 0.055$ gives $H_0^{\rm pred} = 64.92 \pm 0.81$, which is $2.51\sigma$ below Planck $H_0$; using Cooke+18 BBN $100\omega_b = 2.166 \pm 0.019$ gives $H_0^{\rm pred} = 64.15 \pm 0.28$, which is $5.29\sigma$ below Planck $H_0$ and $6.42\sigma$ below DESI+BBN $H_0 = 68.52 \pm 0.62$, where DESI+BBN shares the BBN prior.)*

## Plain Mathematical Statement of the Ratio Tension (Open Problem 10)
Because the parameter-free baryon share $\Omega_b = 1/19 = 0.052632$ is **$6.76\%$ ($+3.87\sigma$) higher** than Planck's measured $\Omega_b = \omega_b/h^2 = 0.04930 \pm 0.00086$, one value of $f_{\rm leak}$ cannot match both $\Omega_{bc}$ and $\mathcal{R} = \omega_c/\omega_b$:
- Matching the cosmic shares ($\Omega_{bc} = 6/19 \approx 0.31579$ at $f_{\rm leak} = 1/6$) predicts $\mathcal{R}_{\rm pred} = 5.0000$, which sits **$5.64\sigma_{\rm Planck}$ below unrounded $\mathcal{R}_{\rm Planck} = 5.3643 \pm 0.0646$** (or **$5.54\sigma_{\rm Planck}$ below rounded $5.36 \pm 0.065$**).
- Matching unrounded $\mathcal{R}_{\rm Planck} = 5.3643$ requires $f_{\rm leak} = 1 - 5.3643/6 = 0.1059$ (or $0.1067$ for rounded $5.36$), which forces $\Omega_{bc} = (1 + 5.3643)/19 = 0.3350$ ($0.3347$ for $5.36$), missing Planck's $\Omega_{bc} = 0.3138 \pm 0.0073$ by $+2.9\sigma$.
- **Forecast for Decisive Test `T2-A` (Review V3 Minor 1):** With $\Omega_{\nu,0} \approx 0.00142$ subtracted from published DESI DR2 + CMB + SNe fits ($\Omega_{m,{\rm tot}} \approx 0.3114 \pm 0.0057$ for `Pantheon+` and $0.313 \pm 0.006$ for `DES-Dovekie`), $\mathcal{R}_{\rm pred} = 19\Omega_{bc} - 1 \approx 4.89$ (`Pantheon+`) and $4.92$ (`DES-Dovekie`), so **`T2-A` is forecast to FAIL at $3.72\sigma$ (`Pantheon+`) and $3.35\sigma$ (`DES-Dovekie`), i.e., about $3.4\text{–}3.7\sigma$**.

---

# 5. Section (d): The Unwinding — Outer-Ring Tension and CPL Mapping

**Section Tier:** **Tier 1** for (d1, d2); **Tier 3** for (d3–d5).

## (d1 & d2) Cosmological Tension and Uncoupled Equation of State `[Established | Tier 1]`
$$p_{\rm de} = w(a)\,\rho_{\rm de}c^2, \qquad w(a) = -1 - \frac{1}{3}\frac{d\ln\rho_{\rm de}}{d\ln a} = -1 - \frac{1}{3}\frac{d\ln g(a)}{d\ln a}.$$

## (d3) Twist–Tension Power Law `[Model Ansatz | Tier 3 | Assumption A8]`
$$g(a) \equiv \frac{\rho_{\rm de}(a)}{\rho_{\rm de,0}} = \left(\frac{\theta(a)}{\theta_0}\right)^n \quad (n > 0) \implies w(a) = -1 - \frac{n}{3}\frac{d\ln\theta}{d\ln a} = -1 - \frac{n}{3H(a)}\frac{\dot{\theta}}{\theta}.$$
For any uncoupled ($Q = 0$) monotonic unwinding ($\dot{\theta} < 0, n > 0$), **$w(a) > -1$ at all epochs $a > 0$** (never crosses $w = -1$).

## (d4 & d5) $(w_0, w_a)$ Relations for Three Unwinding Laws and Primary Test `T1-L1` (Findings B4, M13, N5, Review V3 M1) `[Model Ansatz | Tier 3 | Assumption A9]`
Using $w_0 \equiv w(1)$ and $w_a \equiv -\left.\frac{dw}{da}\right|_{a=1}$:

1. **Law 1 (d4 Baseline — Constant Cosmic-Time Relaxation Rate, $\dot{\theta} = -\Gamma_u\theta$, $\Gamma_u \ge 0$, Registered as Primary Test `T1-L1`):**
   $$w(a) = -1 + \frac{\gamma_u}{E(a)}, \qquad g(a) = \exp\!\left[3\gamma_u\int_a^1 \frac{da'}{a'\,E(a')}\right], \qquad \gamma_u \equiv \frac{n\Gamma_u}{3H_0} \ge 0.$$
   At $a = 1$, this 1-parameter dark-energy model predicts the exact $(w_0, w_a)$ locus:
   $$w_0 = -1 + \gamma_u \ge -1, \qquad w_a = -\frac{3}{2}\gamma_u\left[\Omega_m + \gamma_u(1 - \Omega_m)\right] = -\frac{3}{2}(1 + w_0)\left[\Omega_m + (1 + w_0)(1 - \Omega_m)\right] \le 0.$$
   Here $n$ and $\Gamma_u$ are completely degenerate in $\gamma_u = 1 + w_0$, so **Law 1 has 1 fewer free parameter than $w_0w_a\text{CDM}$ and predicts a 1D curve in the $(w_0 \ge -1, w_a \le 0)$ quadrant** with slope $\left.\frac{dw_a}{dw_0}\right|_{w_0=-1} = -\frac{3}{2}\Omega_m \approx -0.474$.
   - **How the Model's Own $w_0$ Is Set in `T1-L1` & Forecast (`N5`, `Review V3 M1`):** When `T1-L1` is fitted to the data, $\gamma_u \in [0, 2]$ is a free parameter fitted jointly with $(\Omega_m, h, \omega_b)$, so the model's best-fit present-day equation of state is $w_0^{\rm fit} = -1 + \hat{\gamma}_u$. Because $(w_0, w_a)$ are strongly anti-correlated in BAO+CMB+SNe data along the pivot degeneracy $w_p = w_0 + (1 - a_p)w_a$, projecting the unconstrained CPL posterior ($w_0 = -0.838 \pm 0.055, w_a = -0.62^{+0.22}_{-0.19}$ for `Pantheon+`; $w_0 = -0.803 \pm 0.054, w_a = -0.72 \pm 0.21$ for `DES-Dovekie`, DESI Collaboration 2025b Table V & Popovic et al. 2025 Tables 10–11) onto the shallow Law 1 curve pulls the Law 1 best fit to **$w_0^{\rm fit} \approx -0.90\text{ to }-0.93$** ($w_a^{\rm fit} \approx -0.04\text{ to }-0.06$), whereas evaluated at DESI's CPL $w_0 = -0.84$ and $\Omega_m = 0.315$, Law 1 gives $w_a = -0.102$. Thus Law 1 is forecast to yield $\Delta\chi^2_{\min}(\text{Law 1} - w_0w_a\text{CDM}) \approx 7\text{–}8$ in `Pantheon+` (per-run `INCONCLUSIVE`) and $\approx 9\text{–}10$ in `DES-Dovekie` (right at the $\Delta\chi^2 > 9.0$ per-run `FAIL` boundary); because `T1-L1` fails if **either** supernova run fails (`PREREG.md` §5.1), the joint `T1-L1` outcome is **forecast to be `FAIL` or `INCONCLUSIVE`**.
2. **Law 2 (Alternative A — Nonlinear Viscoelastic Torque, $\dot{\theta} = -\Gamma_u\theta_0(\theta/\theta_0)^p$, $p > 0$):**
   $$w(a) = -1 + (1 + w_0)\,\frac{\left[g(a)\right]^q}{E(a)}, \qquad w_a = -\frac{3}{2}(1 + w_0)\left[\Omega_m + \left(1 - \Omega_m - 2q\right)(1 + w_0)\right], \qquad q \equiv \frac{p - 1}{n}.$$
3. **Law 3 (Alternative B — Expansion-Driven Pitch Stretching, $\frac{d\ln\theta}{d\ln a} = -\alpha_u a^\beta$, $\alpha_u > 0, \beta \ge 0$):**
   $$w(a) = -1 + (1 + w_0)\,a^\beta, \qquad w_0 = -1 + \frac{n\alpha_u}{3} > -1, \qquad w_a = -\beta(1 + w_0) \le 0.$$
   - **Correction of M13 (No Universal Tangent Wedge):** Only for globally linear CPL ($\beta = 1$, $w(a) = w_0 - (1 + w_0)(1 - a)$) does $w(0) \ge -1$ imply $w_a = -(1 + w_0)$. For general smooth curves with $w(a) \ge -1$ everywhere, the tangent $w_a = -w'(1)$ is not confined to $-(1 + w_0) \le w_a \le 0$: Law 3 with $\beta > 1$ has $w(a) \ge -1$ for all $a \in [0, 1]$ but tangent $w_0 + w_a = -1 - (\beta - 1)(1 + w_0) < -1$, while Law 2 with $q > \frac{\Omega_m}{2(1+w_0)} + \frac{1-\Omega_m}{2}$ has $w(a) > -1$ everywhere but $w_a > 0$.

## 5.4 (d-Exp) `[EXPLORATORY — Not Pre-Registered in v1]` Unwinding (d4) + Stable Transfer Coupling ($Q_{\rm de} = \xi_e H \rho_{\rm de}$, Finding m1) `[Model Ansatz | Tier 2/3]`
Combining bare unwinding $w_{\rm bare}(a) = -1 + \frac{\gamma_u}{E(a)}$ ($\gamma_u = \frac{n\Gamma_u}{3H_0} > 0$) with $Q_{\rm de} = \xi_e H \rho_{\rm de}$ ($\xi_e > 0$) via (b2) yields:
$$w_{\rm de}^{\rm eff}(a) = -1 + \frac{\gamma_u}{E(a)} - \frac{\xi_e}{3}, \qquad w_0^{\rm eff} = -1 + \gamma_u - \frac{\xi_e}{3}, \qquad w_a^{\rm eff} = -\frac{3}{2}\left(1 + w_0^{\rm eff} + \frac{\xi_e}{3}\right)\left[\Omega_m + \left(1 + w_0^{\rm eff} + \frac{\xi_e}{3}\right)(1 - \Omega_m)\right].$$
*(Here $\left.\frac{d(E^2)}{da}\right|_{a=1} = -3\Omega_m - [3(1 + w_0^{\rm eff}) + \xi_e](1 - \Omega_m)$ includes the coupled dark-matter derivative $\rho_{\rm dm}'(1) = -3\rho_{{\rm dm},0} - \xi_e\rho_{{\rm de},0}$ per Finding m1.)* For $\gamma_u > \frac{\xi_e}{3} > 0$, dark energy weakens today ($w_0^{\rm eff} > -1$), crosses $w_{\rm de}^{\rm eff} = -1$ at redshift $E(z_{\rm cross}) = \frac{3\gamma_u}{\xi_e} = 1 + \frac{3(1 + w_0^{\rm eff})}{\xi_e} > 1$, and exhibits an effective phantom past ($w_{\rm de}^{\rm eff}(z) < -1$ for $z > z_{\rm cross}$, Open Problem 11) while keeping bare tension non-phantom ($w_{\rm bare} > -1$) and linear perturbations stable ($d < 0$).

---

# 6. Section (e): The Shadow in Merging Galaxy Clusters

**Section Tier:** **Tier 1** for (e1, e2); **Tier 2** for nonlocal kernel precedent (Hehl & Mashhoon 2009); **Tier 3** for (e3–e7).

## (e1–e5) Unified Coarse-Grained Velocity-Extrapolated Shadow Density (Finding M5) `[Established (e1, e2) / Model Ansatz (e3–e5) | Tier 1 & 3 | Assumptions A10, A12, A16]`
$$\nabla^2\Phi(\mathbf{x}, t) = 4\pi G\left[\rho_b(\mathbf{x}, t) + \rho_{\rm sh}(\mathbf{x}, t)\right], \qquad \rho_{\rm sh}(\mathbf{x}, t) = 6(1 - f_{\rm leak})\int_{\mathbb{R}^3} d^3y\;K_\sigma(\mathbf{x} - \mathbf{y})\,\tilde{\rho}_b(\mathbf{y}, t),$$
$$\tilde{\rho}_b(\mathbf{y}, t) = \sum_{c} \rho_{b,c}\!\left(\mathbf{y} - \mathbf{V}_{{\rm bulk},c}(t - \tau_{\rm lag})\,\tau_{\rm lag},\; t - \tau_{\rm lag}\right), \qquad K_\sigma(\mathbf{r}) = \left(2\pi\sigma_{\rm ref}^2\right)^{-3/2}\exp\!\left(-\frac{|\mathbf{r}|^2}{2\sigma_{\rm ref}^2}\right).$$
Because inter-string gravity transfer is smoothed on scale $\sigma_{\rm ref}$, linear extrapolation acts on the **center-of-mass bulk velocity $\mathbf{V}_{{\rm bulk},c}(t - \tau_{\rm lag})$ of each coherent baryonic component $c$** (applying one identical rule to colliding cluster components where $\mathbf{V}_{{\rm bulk},c} \ne \mathbf{0}$ and isolated galaxies where $\mathbf{V}_{\rm bulk} = \mathbf{0} \implies \tilde{\rho}_b = \rho_b$).

## (e6 & e7) Dynamical Merger Model, Unified Sign Convention, and Exact Harmonic A13b (Findings B2, B3, m14) `[Model Ansatz | Tier 3 | Assumptions A12, A13b, A14]`
Along the 1D merger axis $+x$ with pericenter at $t = t_p$ ($x = 0, v_p > 0$), time since pericenter $T \equiv t - t_p \ge 0$, stellar mass fraction $f_S = 1 - f_G$, gas mass fraction $f_G = \frac{M_G}{M_S + M_G}$, and $\mathcal{R} = 6(1 - f_{\rm leak})$:
$$\tilde{x}_c(T; \tau_{\rm lag}) = x_c(T - \tau_{\rm lag}) + v_c(T - \tau_{\rm lag})\,\tau_{\rm lag}, \qquad \Delta\tilde{x}_c(T; \tau_{\rm lag}) \equiv \tilde{x}_c(T; \tau_{\rm lag}) - x_c(T) = -\int_{T - \tau_{\rm lag}}^{T} (T - t')\,\ddot{x}_c(t')\,dt'.$$
- **Unified Offset Sign Convention (Finding B2):** With $\hat{\mathbf{s}}_{G\to S} \equiv \frac{\mathbf{x}_S - \mathbf{x}_G}{|\mathbf{x}_S - \mathbf{x}_G|}$ ($= +\hat{\mathbf{x}}$ in 1D), $\delta_{SG}(T) \equiv x_G(T) - x_S(T) = -|\delta_{SG}(T)| < 0$, $\delta_{SI}(T) \equiv x_I(T) - x_S(T)$, and $\beta(T) \equiv \frac{\delta_{SI}(T)}{\delta_{SG}(T)}$, the projected offset is defined identically in all files as:
  $$\Delta_{SI}^{\parallel}(T) \equiv \left(\mathbf{x}_I(T) - \mathbf{x}_S(T)\right)\cdot\hat{\mathbf{s}}_{G\to S} = \delta_{SI}(T) = \delta_{SG}(T)\,\beta(T) = -\left|\delta_{SG}(T)\right|\,\beta(T),$$
  where $\Delta_{SI}^{\parallel}(T) > 0 \iff \delta_{SI}(T) > 0 \iff \beta(T) < 0$ means dark mass sits **ahead of the stars (away from the gas)**.
- **Physical Selection of Model A13b (Exact Symmetric Harmonic Core Passage, Finding B3):** In a conservative cluster gravitational potential, pre-pericenter infall accelerates the subcluster ($\ddot{x}_S > 0$ for $t' < 0$) and post-pericenter climb decelerates it ($\ddot{x}_S < 0$ for $t' > 0$); assuming constant pre-pericenter speed (A13a) violates energy conservation. Therefore **A13b ($x_S(t) = \frac{v_p}{\omega_0}\sin(\omega_0 t)$) is selected as the physical v1 trajectory model**, evaluated via its **exact closed-form expression**:
  $$\Delta\tilde{x}_S^{\rm (A13b)}(T; \tau_{\rm lag}) = \frac{v_p}{\omega_0}\left[\sin\!\left(\omega_0(T - \tau_{\rm lag})\right) + \omega_0\tau_{\rm lag}\cos\!\left(\omega_0(T - \tau_{\rm lag})\right) - \sin(\omega_0 T)\right].$$
  *(The cubic Taylor approximation $\frac{1}{6}\omega_0^2 v_p\tau_{\rm lag}^2(3T - 2\tau_{\rm lag})$ holds only for $\omega_0\tau_{\rm lag} \ll 1$, whereas $\omega_0\tau_{\rm lag} \sim 2\text{–}4$ for $\tau_{\rm lag} \ge 235\text{ Myr}$; the exact trigonometric formula governs and preserves the sign switch near $T \approx \frac{2}{3}\tau_{\rm lag}$.)* Because `A13b` predicts a negative offset for $0 < T \lesssim \frac{2}{3}\tau_{\rm lag}$ and because only $N = 1$ non-Bullet cluster has $t_p \le 150\text{ Myr}$, **T4a is unconditionally `EXPLORATORY` (unscored) in v1 regardless of $N$, age cut, or catalog (`PREREG.md` §3.1 & §5.4)**.
- **Explicit Fractional Offset Curve $\beta(T; \tau_{\rm lag})$ (Including Both Post-Shock Gas Cases per m14):**
  - *Global Centroids:*
    $$\beta_{\rm centroid}(T; \tau_{\rm lag}) = \begin{cases}
    \displaystyle \frac{f_G}{1 + \mathcal{R}} - \frac{\mathcal{R}}{1 + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|}, & 0 < T \le \tau_{\rm lag}, \\[10pt]
    \displaystyle f_G - \frac{\mathcal{R}}{1 + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|}, & T > \tau_{\rm lag} \quad (\text{A14a-grav: }\ddot{x}_G = \ddot{x}_S), \\[10pt]
    \displaystyle f_G - \frac{f_S\,\mathcal{R}}{1 + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|}, & T > \tau_{\rm lag} \quad (\text{A14a-coast: }\ddot{x}_G = 0), \\[10pt]
    \displaystyle f_G\left[1 - \frac{\mathcal{R}}{1 + \mathcal{R}}\left(\frac{\tau_{\rm lag}}{T}\right)^2\right] - \frac{\mathcal{R}}{1 + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|}, & T > \tau_{\rm lag} \quad (\text{continuous drag A14b}).
    \end{cases}$$
  - *Resolved Lensing Convergence Peaks ($|\delta_{SG}| \gtrsim \sigma_{\rm ref}$):*
    $$\beta_{\rm peak}(T; \tau_{\rm lag}) = -\frac{\mathcal{R}}{f_S + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|} \quad (0 < T \le \tau_{\rm lag}), \qquad \beta_{\rm peak}(T; \tau_{\rm lag}) \to 1 \quad (T > \tau_{\rm lag}).$$

---

# 7. Section (f): Galaxy Rotation Curves, the Cap Theorem, and Orbital Extrapolation

**Section Tier:** **Tier 1** for (f1, f2); **Tier 3** for (f3, f4).

## (f1 & f2) Spherical Circular Speed and Empirical RAR Benchmark `[Established | Tier 1 | Assumption A15]`
$$v_c^2(r) = v_{\rm bar}^2(r) + v_{\rm sh}^2(r) = \frac{G\left[M_b^{\rm mono}(< r) + M_{\rm sh}(< r)\right]}{r}, \qquad v_{{\rm bar,raw}}^2(r) = v_{\rm gas}|v_{\rm gas}| + 0.5\,v_{\rm disk}^2 + 0.7\,v_{\rm bul}^2,$$
$$g_{\rm obs}^{\rm RAR}(r) = \frac{g_{\rm bar}(r)}{1 - \exp\!\left(-\sqrt{g_{\rm bar}(r)/g_\dagger}\right)}, \qquad g_\dagger = 1.20\times 10^{-10}\text{ m s}^{-2}.$$

## (f3) Enclosed Shadow Mass Kernel (Corrected per B1 & Point-Mass Branch) and the Saturation Cap Theorem (Findings B1, M3, m4) `[Model Ansatz | Tier 3 | Assumptions A15, A16]`
For any galaxy with non-negative radial baryonic shell mass distribution $dM_b^{\rm mono}(r')$, the spherical enclosed shadow mass under the 3D isotropic Gaussian kernel (e5) is
$$M_{\rm sh}(< r) = 6(1 - f_{\rm leak})\int_0^\infty \mathcal{F}_\sigma(r, r')\,dM_b^{\rm mono}(r'),$$
where the exact piecewise 1D radial enclosed-mass kernel (`[Established Math | Tier 1]`, non-central $\chi'^2_3(r'^2/\sigma_{\rm ref}^2)$ CDF evaluated at $r^2/\sigma_{\rm ref}^2$, with the Gaussian prefactor corrected from $\sqrt{2/\pi}$ to $\frac{1}{\sqrt{2\pi}}$ per Finding B1 and the analytical $r' \to 0^+$ limit used for $r'/\sigma_{\rm ref} < 10^{-4}$ to prevent $0/0$ division at $r' = 0$) is:
$$\mathcal{F}_\sigma(r, r') = \begin{cases}
\displaystyle \frac{1}{2}\left[\operatorname{erf}\!\left(\frac{r + r'}{\sqrt{2}\,\sigma_{\rm ref}}\right) + \operatorname{erf}\!\left(\frac{r - r'}{\sqrt{2}\,\sigma_{\rm ref}}\right)\right] - \frac{1}{\sqrt{2\pi}}\,\frac{\sigma_{\rm ref}}{r'}\left[\exp\!\left(-\frac{(r - r')^2}{2\sigma_{\rm ref}^2}\right) - \exp\!\left(-\frac{(r + r')^2}{2\sigma_{\rm ref}^2}\right)\right], & \dfrac{r'}{\sigma_{\rm ref}} \ge 10^{-4}, \\[14pt]
\displaystyle \operatorname{erf}\!\left(\frac{r}{\sqrt{2}\,\sigma_{\rm ref}}\right) - \sqrt{\frac{2}{\pi}}\,\frac{r}{\sigma_{\rm ref}}\exp\!\left(-\frac{r^2}{2\sigma_{\rm ref}^2}\right), & \dfrac{r'}{\sigma_{\rm ref}} < 10^{-4}.
\end{cases}$$

- **Direct 3D Monte Carlo Verification of the Corrected Kernel (`verify_b1_kernel_mc.py`, $N = 500{,}000$ samples, `SEED = 20261030`, Finding B1):**
  | $(r, r', \sigma_{\rm ref})$ | Corrected $\mathcal{F}_\sigma(r, r')$ | 3D Monte Carlo Mean $\pm$ SE | Diff / SE | Old ($\sqrt{2/\pi}$) Value (Wrong) |
  |---|---|---|---|---|
  | $(1.0, 1.0, 1.0)$ | `0.132299` | `0.131790 ± 0.000478` | `-1.06 SE` | `-0.212653` (unphysical $<0$) |
  | $(2.0, 1.0, 1.5)$ | `0.326572` | `0.327212 ± 0.000664` | `+0.96 SE` | `-0.071614` (unphysical $<0$) |
  | $(0.5, 2.0, 1.0)$ | `0.004603` | `0.004680 ± 0.000097` | `+0.80 SE` | `-0.051392` (unphysical $<0$) |
  | $(3.0, 0.5, 2.0)$ | `0.468804` | `0.469172 ± 0.000706` | `+0.52 SE` | `+0.083317` (`-546 SE`) |

- **Registered Variants & Training Objective in Test T5 (Review V3 B1):** **T5-A (Sole Primary Rotation-Curve Pillar Test):** universal constant $\sigma_{\rm ref}$ in kpc; **T5-B (Secondary / Sensitivity Test):** scaled width $\sigma_{\rm ref} = k\,R_d$ with universal dimensionless constant $k$ and SPARC disk scale length $R_d$. In both variants, $\hat{\sigma}_{\rm ref}$ (`T5-A`) and $\hat{k}$ (`T5-B`) are fixed on the 88 training galaxies by minimizing the sum of per-galaxy reduced chi-squared $\mathcal{L}_{\rm train} = \sum_{g\in{\rm train}}\chi^2_{{\rm red},g}$, with $M_b^{\rm mono}(< r')$ evaluated on a 400-point interior grid (200 linear nodes on $[0, r_1]$ plus 200 log nodes on $[r_1, r_{\max}]$) and continued on a 100-point linear grid over $[r_{\max}, r_{\max} + 5\sigma_{\rm ref}]$ using the stellar-only surface density $\Sigma_b^{\rm tail}(r_{\max}) = 10^6[\Upsilon_{\rm disk}\text{SBdisk}(r_{N_g}) + \Upsilon_{\rm bul}\text{SBbul}(r_{N_g})]\,M_\odot\text{ kpc}^{-2}$ (entering $M_{\rm sh}(< r)$ only; see `PREREG.md` §5.6).
- **Saturation Cap Theorem & Forecast for Test T5 (Findings M3, m4, Review V2 Minor):** Because $K_\sigma$ is normalized to $1$ and acts as a 3D diffusion operator, **for any isolated galaxy whose spherically averaged baryon density decreases monotonically outward ($d\bar{\rho}_b/dr \le 0$)**, $M_{\rm sh}(< r) \le 6(1 - f_{\rm leak})M_b(< r)$ at all radii $r > 0$ (and for any profile with a central gas hole/ring, the outer halo at $r \gtrsim R_{\rm ring}$ is likewise bounded by $6(1 - f_{\rm leak})M_{b,{\rm tot}}$), enforcing the ceiling:
  $$\frac{g_{\rm obs}(r)}{g_{\rm bar}(r)} = 1 + \frac{M_{\rm sh}(< r)}{M_b^{\rm mono}(< r)} \le 1 + 6(1 - f_{\rm leak}) \underset{f_{\rm leak}=1/6}{=} 6.0 \qquad \forall\,r > 0 \;\;(\text{when } d\bar{\rho}_b/dr \le 0).$$
  In the McGaugh et al. (2016) RAR, $g_{\rm obs}^{\rm RAR}/g_{\rm bar}$ exceeds $6.0$ at $g_{\rm bar} < g_{\rm bar}^{\rm cap} = 3.99\times 10^{-12}\text{ m s}^{-2}$ (for $f_{\rm leak} = 1/6$) and exceeds $6.20$ at $g_{\rm bar} < 3.71\times 10^{-12}\text{ m s}^{-2}$ (for $\mathcal{R} = 5.20$). Because SPARC low-surface-brightness, dwarf, and outer-disk points routinely sit below $g_{\rm bar}^{\rm cap}$ with $g_{\rm obs}/g_{\rm bar} \sim 10\text{–}20$, **this saturation cap makes a full T5 PASS very unlikely (Forecast: FAIL or INCONCLUSIVE)**.

## (f4) Carried Motion on Circular Orbits and Unified Coarse-Grained Rule (Finding M5) `[Model Ansatz Analysis | Tier 3 | Assumptions A12, A16]`
$$r_{\rm ext} = r\sqrt{1 + \left(\frac{v_c\,\tau_{\rm lag}}{r}\right)^2}, \qquad v_c\,\tau_{\rm lag} = 30.68\text{ kpc}\times\left(\frac{v_c}{200\text{ km s}^{-1}}\right)\left(\frac{\tau_{\rm lag}}{150\text{ Myr}}\right).$$
Because the orbital acceleration timescale $t_{\rm accel} = r/v_c$ is $14.7\text{ Myr}$ at $r = 3\text{ kpc}, v_c = 200\text{ km s}^{-1}$ (and $195.6\text{ Myr}$ at $r = 30\text{ kpc}, v_c = 150\text{ km s}^{-1}$), internal bound orbital velocities violate uniform motion over $\tau_{\rm lag} \ge 235\text{ Myr}$. Under the unified coarse-grained component velocity rule (e3), an isolated galaxy in its center-of-mass frame has $\mathbf{V}_{\rm bulk} = \mathbf{0}$ and $\partial\rho_b/\partial t = 0$, so $\tilde{\rho}_b(\mathbf{x}) = \rho_b(\mathbf{x})$ identically.

---

# 8. Sections (g), (h), and (i): Locality, Coincidence Window, and Parameter Table

## 8.1 (g1–g4) Difference Bubbles and Regional $H_0$ Estimator (Findings M14 & N9) `[Established (g1) / Model Ansatz (g2–g4) | Tier 1 & 3 | Assumptions A10, A20]`
$$\chi_{\rm diff}(z; z_s) = D_M(z_s) - D_M(z), \qquad R_{\rm diff}(z; z_s) = \frac{D_M(z_s) - D_M(z)}{1 + z} \underset{\Delta t \ll H^{-1}}{\approx} c\,\Delta t_{\rm split}.$$
In Test T6, across the $N_{\rm pix}$ well-sampled HEALPix $N_{\rm side} = 1$ Galactic $(l, b)$ `RING` sky regions ($N_{\rm SN,i} \ge 10$) with frozen SH0ES calibrator absolute magnitude $M_B^{\rm fixed}$ and Pantheon+ Hubble-flow covariance block $\mathbf{C}_{\rm HF}$ ($0.023 \le z_{\rm HD} \le 0.15$), the log-Hubble vector $\eta_i = 5\log_{10} H_{0,i}$ is estimated by generalized least squares:
$$\hat{\boldsymbol{\eta}} = \left(\mathbf{P}^T \mathbf{C}_{\rm HF}^{-1} \mathbf{P}\right)^{-1} \mathbf{P}^T \mathbf{C}_{\rm HF}^{-1} \mathbf{y}, \qquad \mathbf{C}_\eta = \left(\mathbf{P}^T \mathbf{C}_{\rm HF}^{-1} \mathbf{P}\right)^{-1}, \qquad \bar{H}_0 = \frac{\mathbf{1}^T \mathbf{C}_{H_0}^{-1}\hat{\mathbf{H}}_0}{\mathbf{1}^T \mathbf{C}_{H_0}^{-1}\mathbf{1}},$$
$$\chi^2_{\rm het} = \left(\hat{\mathbf{H}}_0 - \bar{H}_0\mathbf{1}\right)^T \mathbf{C}_{H_0}^{-1} \left(\hat{\mathbf{H}}_0 - \bar{H}_0\mathbf{1}\right) \quad (\text{dof} = N_{\rm pix} - 1).$$

## 8.2 (h1 & h2) Coincidence Window Method `[Established (h1) / Diagnostic (h2) | Tier 1 & 3 | Assumption A11]`
$$\Omega_b(a) = \frac{\Omega_{b,0}\,a^{-3}}{E^2(a)}, \qquad \Omega_{\rm dm}(a) = \frac{\Omega_{{\rm dm},0}\,a^{-3}}{E^2(a)}, \qquad \Omega_{\rm de}(a) = \frac{\Omega_{{\rm de},0}\,g(a)}{E^2(a)}, \qquad \Delta t_{\rm coinc} = \frac{1}{H_0}\int_{a_{\rm min}}^{a_{\rm max}} \frac{da}{a\,E(a)},$$
evaluated for Criterion H-Abs ($\max_i |\Omega_i(a) - s_i^{\rm target}| \le 0.05$) and Criterion H-Rel ($\max_i |\Omega_i(a) - s_i^{\rm target}|/s_i^{\rm target} \le 0.10$).

## 8.3 (i-Exp) `[EXPLORATORY — Not Pre-Registered in v1]` Measurable Linear-Growth Form for $\epsilon_{\rm far}$ (Findings m11, m13) `[Model Ansatz | Tier 3 | Assumption A17]`
For an unclustered far-string shadow fraction $\epsilon_{\rm far} = \Omega_{\rm dm,far}/\Omega_{\rm dm} \ll 1$ with $\sigma_{\rm far} \gg 10\text{ Mpc}$:
$$f(a) \simeq \left[\Omega_m(a)\right]^{\gamma_L}\left(1 - \frac{3}{5}\frac{\Omega_{\rm dm}}{\Omega_m}\epsilon_{\rm far}\right), \qquad \frac{S_8^{\rm LSS} - S_8^{\rm CMB}}{S_8^{\rm CMB}} \simeq -\frac{3}{5}\frac{\Omega_{\rm dm}}{\Omega_m}\ln\!\left(\frac{1 + z_{\rm eq}}{1 + z_{\rm cut}}\right)\epsilon_{\rm far},$$
which with $\frac{\Omega_{\rm dm}}{\Omega_m} = \frac{5}{6}$ and $z_{\rm eq} = 3402$ gives $-3.94\,\epsilon_{\rm far}$ when integrated to $z_{\rm de} = 0.294$ (or $-3.80\,\epsilon_{\rm far}$ for effective matter-era growth cutoff $z_{\rm cut} = 0.70$).

## 8.4 (i) Master Parameter Table (Single Deciding Version Per Test)

| Parameter | Symbol | Role / Status in v1 | Single Deciding Fixing Dataset (`FIX`) | Single Deciding Testing Dataset (`TEST`) | Test ID & Forecast |
|---|---|---|---|---|---|
| Strings per strand | $N_s = 19$ | Structural constant ($1+6+12$); fixes $\Omega_b = 1/19$ | None (geometry) | Planck 2018 $\Omega_b = 0.04930 \pm 0.00086$ & Planck $H_0 = 67.36 \pm 0.54$ | **T2-A (Pillar 2)**; **T2-N1, T2-N2** *(Forecast: FAIL at 3.35–3.87$\sigma$)* |
| Strings per rope | $N_r = 133$ | Structural constant ($7\times 19$); never varied | None (geometry) | No v1 observable | None |
| Transit leak fraction | $f_{\rm leak}$ | $f_{\rm leak} = 1 - \frac{19\Omega_{bc} - 1}{6}$ (Static Form $Q=0$) | `T2-A`: DESI DR2 BAO (joint Ly$\alpha$) + CMB $(R, \ell_A \mid \omega_b)$ + SNe + DESI/LUNA BBN $\omega_b$ | Planck 2018 $\omega_c/\omega_b = 5.36 \pm 0.065$ via uncorrelated $\sigma_{\rm comb}$ | **T2-A (Pillar 2)** *(Forecast: FAIL at 3.72$\sigma$ Pantheon+, 3.35$\sigma$ Dovekie)*; `T2-B` (Sensitivity) |
| Unwinding parameter | $\gamma_u$ | $\gamma_u = \frac{n\Gamma_u}{3H_0} = 1 + w_0^{\rm fit} \ge 0$ in Law 1 (`d4`) | Fitted in 1-parameter Law 1 $w(a) = -1 + \gamma_u/E(a)$ | DESI DR2 BAO (joint Ly$\alpha$) + Planck 2018 $\Lambda\text{CDM}$ $(R, \ell_A, 100\omega_b)$ + Pantheon+ / DES-Dovekie | **T1-L1 (Pillar 1)** *(Forecast: FAIL or INCONCLUSIVE; fails if either SN run fails)* |
| CPL Dark Energy | $w_0, w_a$ | Unconstrained CPL summary ($w_0 > -1$ sign check) | Sign fixed by model; Planck 2018 supplies CMB prior | DESI DR2 BAO (joint Ly$\alpha$) + Pantheon+ / DES-Dovekie | **T1-Sign (Secondary)** *(Known PASS)* |
| IDE Coupling | $\xi_e$ | Exploratory transfer $Q_{\rm de} = \xi_e H \rho_{\rm de}$ | **Not registered in v1 (Exploratory)** | Candidate for v2 phantom-crossing test | None |
| Far-string fraction | $\epsilon_{\rm far}$ | Smooth shadow fraction ($\Delta S_8/S_8 \approx -3.8\epsilon_{\rm far}$) | **Not registered in v1 (Exploratory)** | Candidate for v2 $S_8 / f\sigma_8$ test | None |
| Shadow crossing lag | $\tau_{\rm lag}$ | Universal delay (grid floor $235\text{ Myr}$ = Gaussian-approximated 95% lower credible bound of Dawson 2013 Bullet age $0.40 \pm 0.10\text{ Gyr}$) | Training half of 16 aged mergers (odd rows, Bullet at $t_p = 0.40\text{ Gyr}$, hard-step subcluster accuracy) | Test half of 16 aged mergers (even rows, hard-step subcluster accuracy; after Holm control, requires 100% test score unless rank 3); T4a unconditionally `EXPLORATORY` | **T4b (Pillar 3)** *(No clean forecast)*; T4a (`EXPLORATORY`) |
| Refraction halo width | $\sigma_{\rm ref}$ | 3D Gaussian kernel width (kpc) | SPARC training half (odd indices, 88 galaxies, minimizing $\sum_{g\in{\rm train}}\chi^2_{{\rm red},g}$, $f_{\rm leak}$ from `T2-A` Pantheon+ DESI-BBN) | SPARC held-out half (even indices, 87 galaxies) + NGC 1052-DF2 (T5c) | **T5-A (Pillar 4)** *(Forecast: FAIL or INCONCLUSIVE)*; **T5c (Secondary)** |
| Scaled halo width | $k$ | $\sigma_{\rm ref} = k\,R_d$ | SPARC training half (odd indices, 88 galaxies, minimizing $\sum_{g\in{\rm train}}\chi^2_{{\rm red},g}$) | SPARC held-out half (even indices, 87 galaxies) | **T5-B (Secondary)** |

---

# 9. $\Lambda\text{CDM}$ and Newtonian Recovery Limits

1. **Background Expansion Recovery of $\Lambda\text{CDM}$:**  
   In the Static Form ($Q = 0$), taking the zero-unwinding limit $\Gamma_u \to 0^+$ (or $n \to 0^+$) gives $\gamma_u \to 0$, $w_0 \to -1$, $w_a \to 0$, and $g(a) \to 1$. With $\Omega_{bc} = \Omega_b + \Omega_{\rm dm} = \frac{7 - 6f_{\rm leak}}{19}$ and $\Omega_\Lambda = \frac{12 + 6f_{\rm leak}}{19}$, the Friedmann equation (a2) recovers flat $\Lambda\text{CDM}$ identically at all redshifts $z \in [0, \infty)$.
2. **Transfer-Form Recovery of Static Form:**  
   Taking $\xi_m \to 0^+, \xi_e \to 0^+, \Gamma \to 0^+, \beta_\phi \to 0^+$ gives $Q(a) \to 0$, recovering standard uncoupled conservation $\rho_{\rm dm} \propto a^{-3}$ and $w_{\rm de}^{\rm eff}(a) \to w(a)$.
3. **Cluster Merger Recovery of Collisionless CDM ($\tau_{\rm lag} \to 0^+$ vs. $\omega_0\tau_{\rm lag} \to 0$):**  
   - As $\tau_{\rm lag} \to 0^+$, $\tilde{x}_S(T) \to x_S(T)$ and $\tilde{x}_G(T) \to x_G(T)$ at all $T > 0$, so the shadow tracks the instantaneous baryons ($\beta_{\rm centroid} \to f_G$).
   - For $0 < T < \tau_{\rm lag}$ in the limit of negligible core acceleration ($\omega_0\tau_{\rm lag} \to 0$), $\Delta\tilde{x}_S \to 0$ and $\beta_{\rm peak} \to 0$, recovering the collisionless CDM peak position on the galaxies.
4. **Galaxy Rotation Curve Recovery Limits ($\sigma_{\rm ref} \to 0^+$ and $\sigma_{\rm ref} \to \infty$, Finding M4):**  
   - As $\sigma_{\rm ref} \to 0^+$, $\mathcal{F}_\sigma(r, r') \to \Theta(r - r')$ and the enclosed shadow mass recovers $M_{\rm sh}(< r) \to 6(1 - f_{\rm leak})M_b^{\rm mono}(< r)$, so in the spherical approximation (f1) $v_c^2(r) \to [1 + 6(1 - f_{\rm leak})]G M_b^{\rm mono}(< r)/r$ (constant mass-follows-light boost of the spherical baryon mass profile).
   - As $\sigma_{\rm ref} \to \infty$, $\mathcal{F}_\sigma(r, r') \to 0$ at any finite radius $r$, so $M_{\rm sh}(< r) \to 0$ and $v_c^2(r) \to v_{\rm bar}^2(r)$ (pure Newtonian baryons with no dark halo).

---

# 10. Complete Registry of Stage 1 Assumptions (`[A1]`–`[A20]`)

- **[A1] Flat FLRW Background Geometry (`Tier 1`):** Spatially flat ($k = 0$), homogeneous, isotropic metric (a1), identifying cosmic time $t$ with the physical preferred present ("the blade", `Tier 3`) without altering metric observables. Drives (a1)–(a5); T1-L1, T1-Sign, T2-A, T6.
- **[A2] Standard Relativistic Species & Massive Neutrinos (`Tier 1`):** $T_{\rm CMB,0} = 2.7255\text{ K}$, $N_{\rm eff} = 3.044$, $\sum m_\nu = 0.06\text{ eV}$ ($\Omega_{\nu,0} = \frac{0.06}{93.14\,h^2}$). Drives (a2), (a5); T1-L1, T1-Sign, T2-A.
- **[A3] Explicit Exclusion of $\Omega_{\nu,0}$ from the Three-Component 1:6:12 Share Relation (`Tier 3`, Findings M1 & m7):** In (c3)–(c4), $\Omega_{bc} \equiv \Omega_b + \Omega_{\rm dm} = \Omega_{m,{\rm tot}} - \Omega_{\nu,0} = (7 - 6f_{\rm leak})/19$. Drives (c3), (c4); T2-A, T2-B.
- **[A4] Static-Form Leak as Boundary Stress-Energy Partition (`Tier 3`, Model Ansatz):** In the locked v1 Static Form ($Q = 0$), $(1 - f_{\rm leak})$ is the constant transverse transmission efficiency of the 6 touching neighbors' baryon pull ($\rho_{\rm dm} = 6(1 - f_{\rm leak})\rho_b \propto a^{-3}$), while $\Omega_{\rm de,0} = (12 + 6f_{\rm leak})/19$ is partitioned into bulk longitudinal string tension governed by $w(a)$. Drives (b5-S), (c2)–(c4), validity of $(R, \ell_A)$ priors; T2-A, T5-A.
- **[A5] Transfer-Form Initial Condition and Non-Rising Density Constraint (`Tier 3`, Exploratory Alternative):** In dynamic IDE ($Q > 0$), $\mathcal{R}(a_i) = 6$ transfers cumulative fraction $f_{\rm leak}$ by $a = 1$ subject to $\dot{\rho}_{\rm de}(t_0) \le 0$. Drives (b1)–(b5-T), (d-Exp).
- **[A6] Cosmological Homogeneity of the Six Touching Neighbors (`Tier 3`, Model Ansatz):** Averaged over cosmological volumes, $\bar{\rho}_b^{(k)}(a) = \bar{\rho}_b(a)$ and $f_{\rm leak}^{(k)} = f_{\rm leak}$ for $k = 1,\dots,6$. Drives (b5), (c2), (e4); T2-A, T4b, T5-A.
- **[A7] Fixed Strand Geometry $N_s = 19$ and $N_r = 133$ (`Tier 3`, Model Ansatz / Numerology):** Planar equal-circle packing ($1+6+12=19$) maps directly to present-day budget shares (c3), implying the parameter-free predictions $\Omega_b = 1/19$ and $H_0^{\rm pred} = 100\sqrt{19\omega_b}$. Drives (c2)–(c4), Open Problem 10; T2-A, T2-N1, T2-N2.
- **[A8] Power-Law Dependence of Tension on Strand Twist (`Tier 3`, Model Ansatz):** $\rho_{\rm de}(a) = \rho_{\rm de,0}(\theta(a)/\theta_0)^n$ with $n > 0$ and $\dot{\theta} < 0$. Drives (d3)–(d5); T1-L1, T1-Sign.
- **[A9] Baseline Constant Cosmic-Time Unwinding Rate Law (`Tier 3`, Model Ansatz, Findings B4, M13, N5):** Baseline Law 1 (`d4`) sets $\dot{\theta} = -\Gamma_u\theta$ ($\gamma_u = \frac{n\Gamma_u}{3H_0} = 1 + w_0^{\rm fit} \ge 0$), yielding $w(a) = -1 + \gamma_u/E(a)$ and the 1D curve $w_a = -\frac{3}{2}\gamma_u[\Omega_m + \gamma_u(1 - \Omega_m)]$, registered directly as Primary Test T1-L1. Drives (d4), (d5); T1-L1.
- **[A10] Causal Difference Bubbles & Macroscopic Neighbor Identity (`Tier 3`, Model Ansatz):** $R_{\rm diff}(z; z_s) = [D_M(z_s) - D_M(z)]/(1+z)$ is sub-galactic or microscopic for the 6 touching neighbors, so $\rho_b^{(k)}(\mathbf{x}, t) = \rho_b(\mathbf{x}, t)$ on scales $\gtrsim 1\text{ kpc}$. Drives (g1)–(g3), (e4); T4b, T5-A, Exploratory T4a.
- **[A11] Fixed Pre-Registered Tolerances for the Coincidence Window (`Tier 3`, Diagnostic Rule):** Criterion H-Abs ($\Delta_{\rm abs} = 0.05$) and Criterion H-Rel ($\delta_{\rm rel} = 0.10$). Drives (h2).
- **[A12] Unified Coarse-Grained Component Velocity Extrapolation Over $\tau_{\rm lag}$ (`Tier 3`, Model Ansatz, Finding M5):** Because $K_\sigma$ smooths over $\sigma_{\rm ref}$, linear extrapolation acts on the center-of-mass bulk velocity $\mathbf{V}_{{\rm bulk},c}(t - \tau_{\rm lag})$ of each coherent baryonic component $c$ smoothed on scale $\sigma_{\rm ref}$, $\tilde{\rho}_{b,c}(\mathbf{y}, t) = \rho_{b,c}(\mathbf{y} - \mathbf{V}_{{\rm bulk},c}(t - \tau_{\rm lag})\tau_{\rm lag}, t - \tau_{\rm lag})$. Drives (e2)–(e7), (f4); T4b, T5-A.
- **[A13b] Exact Symmetric Harmonic Core-Passage Trajectory in Merging Clusters (`Tier 3`, Selected Physical Model, Finding B3):** A conservative cluster gravitational potential accelerates the infalling subcluster before pericenter and decelerates it after pericenter ($x_S(t) = \frac{v_p}{\omega_0}\sin(\omega_0 t)$), yielding the exact harmonic shift $\Delta\tilde{x}_S^{\rm (A13b)} = \frac{v_p}{\omega_0}[\sin(\omega_0(T-\tau_{\rm lag})) + \omega_0\tau_{\rm lag}\cos(\omega_0(T-\tau_{\rm lag})) - \sin(\omega_0 T)]$ (negative for $0 < T \lesssim \frac{2}{3}\tau_{\rm lag}$, positive for $\frac{2}{3}\tau_{\rm lag} \lesssim T \le \tau_{\rm lag}$). Drives (e6), (e7); Exploratory T4a, T4b.
- **[A14] Collisional Gas Shock / Ram-Pressure Profile and T4b Observable Rules (`Tier 3`, Dynamical Merger Model, Findings m14, N10, Review V3 B2):** Impulsive pericenter velocity drop with shared gravitational field (**[A14a-grav]**) or hydrostatic coasting (**[A14a-coast]**), or continuous deceleration (**[A14b]**), governs the transition of $\beta(T; \tau_{\rm lag})$ at $T > \tau_{\rm lag}$; in Test T4b (whose 16-cluster sample was compiled from the literature by an analyst with prior knowledge of well-known mergers, `N10`), the positions of the primary high-Mach subcluster are defined globally as $I =$ weak-lensing convergence ($\kappa$) peak, $G =$ X-ray surface-brightness peak, and $S =$ luminosity-weighted galaxy centroid (with BCG position as the mechanical fallback if no centroid is tabulated), with 1D $68\%$ sky positional errors $\sigma_c$, and any cluster whose primary source paper lacks any of $(S, G, I)$ or its error is mechanically marked `"unclassified"`. Drives (e6), (e7); T4b.
- **[A15] Isolated Galaxy Approximation, Monotonic Baryon Shells, Quadrature/Tail Rule, and Outward-Decreasing Premise of the Cap Theorem (`Tier 1 & 3`, Pre-Registered T5 Rule, Findings M3, M4, Review V2 Minor, Review V3 B1):** $\Upsilon_{\rm disk} = 0.5, \Upsilon_{\rm bul} = 0.7$, monotonically clipped non-negative shell masses $dM_b^{\rm mono}(r') \ge 0$ on a 400-point interior grid (200 linear nodes on $[0, r_1]$ plus 200 log nodes on $[r_1, r_{\max}]$) used consistently in both $v_{\rm bar}^2(r) = G M_b^{\rm mono}(< r)/r$ and $M_{\rm sh}(< r)$, plus a 100-point stellar-only exponential tail $\Sigma_b^{\rm tail}(r_{\max}) = 10^6[\Upsilon_{\rm disk}\text{SBdisk}(r_{N_g}) + \Upsilon_{\rm bul}\text{SBbul}(r_{N_g})]\,M_\odot\text{ kpc}^{-2}$ on $[r_{\max}, r_{\max} + 5\sigma_{\rm ref}]$ that enters only $M_{\rm sh}(< r)$, with $\hat{\sigma}_{\rm ref}$ (`T5-A`) and $\hat{k}$ (`T5-B`) fixed by minimizing $\sum_{g\in{\rm train}}\chi^2_{{\rm red},g}$ across the 88 training galaxies; for outward-decreasing spherical baryon density ($d\bar{\rho}_b/dr \le 0$), Gaussian diffusion enforces $g_{\rm obs}/g_{\rm bar} \le 1 + 6(1 - f_{\rm leak})$ at every radius (and asymptotically beyond any inner gas ring). Drives (f1), (f3); T5-A, T5-B, T5c.
- **[A16] Rest-Frame Stationarity of Isolated Galaxies Under Coarse-Grained Extrapolation (`Tier 3`, Model Ansatz, Finding M5):** In an isolated galaxy's center-of-mass rest frame, $\mathbf{V}_{\rm bulk} = \mathbf{0}$ and $\partial\rho_b/\partial t = 0$, so the unified rule `[A12]` yields $\tilde{\rho}_b(\mathbf{x}) = \rho_b(\mathbf{x})$ identically. Drives (f3), (f4); T5-A, T5-B.
- **[A17] Far-String Contribution $\epsilon_{\rm far}$ as Smooth Shadow Component (`Tier 3`, Exploratory Proposal for v2):** $\Omega_{\rm dm,far} = \epsilon_{\rm far}\Omega_{\rm dm}$ with $\sigma_{\rm far} \gg 10\text{ Mpc}$ suppresses linear growth ($\Delta S_8/S_8 \approx -3.80\,\epsilon_{\rm far}$ to $-3.94\,\epsilon_{\rm far}$). Not used in v1 tests.
- **[A18] Single Uncorrelated Error Propagation Formula for $\mathcal{R}_{\rm Planck}$ in Test T2-A (`Tier 1/3`, Pre-Registered T2 Rule, Finding N1):** $\mathcal{R}_{\rm Planck} = 5.36 \pm 0.065$, evaluated with the single deciding uncorrelated formula $\sigma_{\rm comb} = \sqrt{(19\sigma_{\Omega_{bc}})^2 + 0.065^2}$. Drives (c4); T2-A.
- **[A19] Byte-Wise ASCII SPARC Primary Split (`Tier 3`, Pre-Registered G8 Resolution, Finding M4):** All 175 SPARC galaxies ordered by Python byte-wise `sorted()` on stripped SPARC galaxy IDs (odd = 88 training, even = 87 test), with the 153-galaxy quality-cut sample reported alongside for the RAR benchmark. Drives T5-A, T5-B.
- **[A20] Single Deciding Configuration for Test T6 (`Tier 3`, Pre-Registered G8 Resolution, Findings M14, N9, Review V3 B4 & Minor 8):** Galactic $(l, b)$ `RING` ordering (12 pixels at `HEALPix` $N_{\rm side} = 1$) on Pantheon+ Hubble-flow SNe ($0.023 \le z_{\rm HD} \le 0.15$, non-calibrators) with minimum pixel occupancy $N_{{\rm SN},i} \ge 10$ (merging any sparse pixel with $0 < N_{{\rm SN},i} < 10$ into its edge-sharing neighbor pixel of lowest `RING` index and dropping any region that remains $< 10$, giving $N_{\rm pix}$ retained regions with $\text{dof} = N_{\rm pix} - 1$), GLS mean $\bar{H}_0$, and the bare Pantheon+ Hubble-flow supernova covariance block $\mathbf{C}_{\rm HF}$ (which already includes peculiar-velocity covariance, propagated to the $N_{\rm pix} \times N_{\rm pix}$ regional $H_0$ covariance $\mathbf{C}_{H_0}$). Drives (g4); T6.
