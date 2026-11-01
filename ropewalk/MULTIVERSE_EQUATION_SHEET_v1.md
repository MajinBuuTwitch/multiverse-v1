---
title: "MULTIVERSE Equation Sheet v1 (starter)"
author: "Gregory Mandarano / WickedAI"
date: "Version 1.0.1, October 2026"
---

License: CC BY 4.0 (Creative Commons Attribution 4.0 International).

# What this sheet is

This is a starter sheet for the Mandarano Model (nickname: the cable), a speculative multiverse model written by a screenwriter. It is not peer reviewed. It maps each mechanism of the model onto existing, published mathematical frameworks, names the free parameters, and states the targets each parameter must hit and the data that should fix it and test it.

It derives nothing new. It claims nothing fitted. Version 1.0.1 contains no computation and reports no results. Where the sheet says "Stage 1" or "Stage 2", it means the follow-up math work that this version hands on: first deriving and tightening these equations, then writing the analysis code. Where a number appears, it is either a published measurement or simple arithmetic on the model's own counting rules, shown so that the targets are explicit.

Every equation carries one of two labels:

- **Established:** a standard equation from published physics, used as it appears in the literature (sign conventions adapted where stated).
- **Model ansatz:** a form chosen to represent the model. It is a proposal to be derived, tightened or rejected, not a result.

Every section carries a tier:

| Tier | Meaning |
|---|---|
| Tier 1 | Established physics and measurements |
| Tier 2 | Published speculation (peer-reviewed ideas that are not established) |
| Tier 3 | This model |

## Shared parameter names

These names are used identically in every file of the v1 package.

| Name | Symbol | Short meaning |
|---|---|---|
| N_s | $N_s$ | Strings per strand: $1+6+12 = 19$ (fixed by the model's geometry) |
| N_r | $N_r$ | Strings per rope: $7 \times 19 = 133$ (fixed by the model's geometry) |
| f_leak | $f_{\rm leak}$ | Fraction of the six touching neighbors' pull lost in transit and stored as outer-ring tension (expected about $1/6$; fixed from the expansion history, section (c4)) |
| epsilon_far | $\epsilon_{\rm far}$ | Faint pull from farther strings, arriving mostly as tension |
| w0, wa | $w_0$, $w_a$ | CPL dark energy parameters (the model expects weakening from unwinding) |
| tau_lag | $\tau_{\rm lag}$ | Shadow crossing delay (must exceed about 150 Myr) |
| sigma_ref | $\sigma_{\rm ref}$ | Refraction spreading width of the shadow (sets halo widths) |

## Conventions

Flat spatial sections. Scale factor $a$ with $a_0 = 1$ today, redshift $1+z = 1/a$, cosmic time $t$, overdot $= d/dt$, Hubble rate $H = \dot a / a$. Density parameters $\Omega_i = \rho_{i,0}/\rho_{\rm crit,0}$ with $\rho_{\rm crit,0} = 3H_0^2/(8\pi G)$ and $\omega_i = \Omega_i h^2$. Subscripts: $b$ baryons (ordinary matter), $\rm dm$ the dark matter component (in this model, the shadow), $\rm de$ dark energy (in this model, tension), $r$ radiation. "Neighbors" means the six strings touching ours in the strand.

## The model in one paragraph (Tier 3)

Each history of the universe is a string. Histories that split recently stay close and in step. Nineteen strings make a strand: ours at the center, six touching it, twelve around those ($N_s = 19$). Seven strands make a rope ($N_r = 133$). In this model, gravity crosses mainly where strings touch, so the six neighbors' matter, which sits almost exactly where ours does, pulls on our universe: that pull is the dark matter (the "shadow"). Crossing the tiny void between strings spreads the pull into a wide halo ("refraction") and takes time ("the lag"); a lagged shadow carries its source's motion. About a sixth (the expected value; the registered value is fitted, section (c4)) of the neighbors' pull leaks in transit and is stored as tension in the outer twelve ("the leak"). Dark energy is that tension, not mass. The strand is slowly unwinding, so the tension, and with it dark energy, should be weakening. Differences between histories spread no faster than light ("locality"). The 1:6:12 match to the cosmic budget is labeled numerology.

# (a) Background cosmology

**Tier 1** for the equations; **Tier 3** for the mapping in (a6).

**(a1) Established.** Flat FLRW metric:
$$ds^2 = -c^2\,dt^2 + a^2(t)\left[dr^2 + r^2\left(d\theta^2 + \sin^2\theta\, d\phi^2\right)\right].$$

**(a2) Established.** Friedmann equation (flat):
$$H^2(a) = \frac{8\pi G}{3}\sum_i \rho_i(a), \qquad \frac{H^2(a)}{H_0^2} = \Omega_r a^{-4} + \left(\Omega_b + \Omega_{\rm dm}\right) a^{-3} + \Omega_{\rm de}\, g(a), \qquad \sum_i \Omega_i = 1,$$
where $g(a) \equiv \rho_{\rm de}(a)/\rho_{\rm de,0}$. The $a^{-3}$ scaling of $\rho_{\rm dm}$ holds only when dark matter is uncoupled; section (b) changes it.

**(a3) Established.** Continuity equation for each uncoupled fluid with equation of state $w_i = p_i/(\rho_i c^2)$:
$$\dot\rho_i + 3H(1+w_i)\rho_i = 0.$$

**(a4) Established.** CPL parametrization (Chevallier and Polarski 2001; Linder 2003) and the dark energy density it implies when dark energy is uncoupled:
$$w(a) = w_0 + w_a(1-a), \qquad g(a) = a^{-3(1+w_0+w_a)}\exp\!\left[-3w_a(1-a)\right].$$
A cosmological constant is $w_0 = -1$, $w_a = 0$.

**(a5) Established.** Distance observables (flat):
$$D_M(z) = c\int_0^z \frac{dz'}{H(z')}, \qquad D_H(z) = \frac{c}{H(z)}, \qquad D_V(z) = \left[z\,D_M^2(z)\,D_H(z)\right]^{1/3},$$
$$D_L(z) = (1+z)D_M(z), \qquad \mu(z) = 5\log_{10}\!\left(\frac{D_L(z)}{10\ {\rm pc}}\right),$$
$$r_d = \int_{z_d}^{\infty}\frac{c_s(z)}{H(z)}\,dz.$$
BAO surveys report $D_M/r_d$, $D_H/r_d$ and $D_V/r_d$ (DESI Collaboration 2025a, 2025b). Supernova compilations report $\mu(z)$ up to an absolute-magnitude offset (Scolnic et al. 2022; Brout et al. 2022; DES Collaboration 2024). Compressed CMB distance priors (Chen, Huang and Wang 2019) use
$$R = \frac{\sqrt{\Omega_m H_0^2}}{c}\,D_M(z_*), \qquad \ell_A = \frac{\pi D_M(z_*)}{r_s(z_*)}, \qquad \omega_b,$$
with $z_*$ the photon decoupling redshift and $r_s$ the sound horizon. These priors assume standard physics before recombination; a model that changes early-time dark matter (some couplings in section (b) do) must not use them without checking that assumption. The fix of $f_{\rm leak}$ (section (c4)) uses only $R$ and $\ell_A$ from these priors, with $\omega_b$ taken from big-bang nucleosynthesis instead of from the CMB.

**(a6) Model ansatz.** The model's background contains three components besides radiation and neutrinos: baryons; the shadow, which gravitates like pressureless matter ($w_{\rm dm} = 0$) in the static form of section (b5); and outer-ring tension, which plays dark energy and is described by $w_0, w_a$ (section (d)) or by a coupled fluid (section (b)).

**Reference values (Tier 1).** Planck 2018 base $\Lambda$CDM, TT,TE,EE+lowE+lensing (Planck Collaboration 2020, Table 2):

| Quantity | Value |
|---|---|
| $\omega_b = \Omega_b h^2$ | $0.02237 \pm 0.00015$ |
| $\omega_c = \Omega_c h^2$ | $0.1200 \pm 0.0012$ |
| $H_0$ | $67.36 \pm 0.54$ km s$^{-1}$ Mpc$^{-1}$ |
| $\Omega_m$ | $0.3153 \pm 0.0073$ |
| $\Omega_\Lambda$ | $0.6847 \pm 0.0073$ |

From these, $\Omega_b \approx 0.049$, $\Omega_c \approx 0.265$ and $\omega_c/\omega_b \approx 5.36$. Rounded shares: about 4.9 / 26.5 / 68.5 percent (massive neutrinos carry the remaining tenth of a percent).

# (b) The leak as an interacting dark energy model

**Tier 1** for the conservation law; **Tier 2** for the coupling forms; **Tier 3** for the link to $f_{\rm leak}$.

**(b1) Established.** Coupled continuity equations. Sign convention for this sheet: $Q > 0$ means energy flows **from dark matter to dark energy**, the direction of the model's leak.
$$\dot\rho_{\rm dm} + 3H\rho_{\rm dm} = -Q, \qquad \dot\rho_{\rm de} + 3H(1+w)\rho_{\rm de} = +Q, \qquad \dot\rho_b + 3H\rho_b = 0.$$
The total dark-sector energy is conserved. Published papers use both sign conventions; Gavela et al. (2009) write $+Q$ on the dark matter side, so their $Q$ is minus ours, while Boehmer et al. (2008) use the same direction as this sheet.

**(b2) Established.** Effective equations of state, with signs adapted to (b1) (Gavela et al. 2009, their Eqs. 5 and 6):
$$w_{\rm dm}^{\rm eff} = \frac{Q}{3H\rho_{\rm dm}}, \qquad w_{\rm de}^{\rm eff} = w - \frac{Q}{3H\rho_{\rm de}}.$$
Energy flowing into dark energy lowers its effective equation of state. A fit that ignores the coupling can then infer $w < -1$ ("phantom") even when the uncoupled $w$ is above $-1$ (Das, Corasaniti and Khoury 2006).

**(b3) Established (published phenomenological forms, Tier 2 as physics).** Couplings studied in the literature, written in the convention of (b1):

| Label | Form | Notes and sources |
|---|---|---|
| Q-dm | $Q = \xi_m H \rho_{\rm dm}$ | Dark matter decays into dark energy at rate $\xi_m H$ for $\xi_m > 0$ (Boehmer et al. 2008, their model II); see also Valiviita, Majerotto and Maartens (2008) |
| Q-de | $Q = \xi_e H \rho_{\rm de}$ | Proportional to dark energy density (Gavela et al. 2009, who write $Q = \xi H\rho_{\rm de}$ with the opposite sign, so $\xi_e = -\xi$) |
| Q-rate | $Q = \Gamma \rho_{\rm dm}$ | Constant rate $\Gamma$ (Boehmer et al. 2008, their model III; Valiviita, Majerotto and Maartens 2008) |
| Q-field | $Q \propto \beta\,\rho_{\rm dm}\dot\phi$ | Coupled quintessence with a scalar field $\phi$ (Amendola 2000) |

For Q-dm with constant $\xi_m$, (b1) integrates to $\rho_{\rm dm} \propto a^{-3-\xi_m}$, so the dark-to-ordinary ratio drifts as $\rho_{\rm dm}/\rho_b \propto a^{-\xi_m}$. Review: Wang, Abdalla, Atrio-Barandela and Pavon (2016).

**(b4) Established (known problems).** Stability of perturbations:

- Valiviita, Majerotto and Maartens (2008): for constant-$w$ fluid dark energy coupled to dark matter through these simple forms, large-scale (super-Hubble) curvature perturbations blow up at early times, however weak the coupling.
- Gavela et al. (2009) trace such early-time non-adiabatic instabilities to the sign of a "doom factor", in their convention $d = Q_{\rm G}/[3H\rho_{\rm de}(1+w)]$ with $Q_{\rm G} = -Q$. Instability appears when $d$ is positive and large. For Q-de they identify an instability-free region with (in their notation) $\xi < 0$ and $w > -1$. Translated to (b1), that is **energy flowing from dark matter to dark energy with $w > -1$**, which is the model's direction.
- For couplings proportional to $\rho_{\rm dm}$, the factor $\rho_{\rm dm}/\rho_{\rm de}$ makes $|d|$ large at early times even for tiny couplings, and Gavela et al. note that with energy flowing from dark matter to dark energy the dark energy density turns negative in the past.

Consequence for this model: the form that reads most naturally from the narration (a fixed fraction of the shadow's pull, which suggests $Q \propto \rho_{\rm dm}$) is the form with the known problems. The form with a published stable branch in the model's direction is Q-de. This is an open choice for Stage 1, not a result.

**(b5) Model ansatz.** One definition of $f_{\rm leak}$, two candidate mechanisms. $f_{\rm leak}$ has a single definition and a single pre-registered role: it is the parameter of today's shares in (c3), fixed from the expansion history and tested on the ratio (section (c4)). What the model has not chosen is the mechanism behind it.

*Static form (transit efficiency).* The leak is a fixed efficiency loss on the gravitational coupling between strings; nothing is transferred in the background equations. The gravitating shadow density is
$$\rho_{\rm dm}(a) = (1-f_{\rm leak})\,N_{\rm in}\,\rho_b(a), \qquad N_{\rm in} = 6,$$
and the leaked share is counted with the tension. The static form keeps the dark-to-ordinary ratio fixed at all times at $6(1-f_{\rm leak})$, the value T2 tests. It does not say how the leaked energy becomes a non-diluting tension; that bookkeeping is a Stage 1 task.

*Transfer form (dynamic).* The leak is a continuous energy transfer $Q$ from (b3). The coupling must then reproduce today's shares with the fixed $f_{\rm leak}$; the transferred fraction of the shadow's energy between an initial epoch $a_i$ and today, relative to no coupling, is
$$1 - \frac{\rho_{\rm dm}(a=1)}{\rho_{\rm dm}(a_i)\,a_i^{3}} = \frac{1}{\rho_{\rm dm}(a_i)a_i^3}\int_{t_i}^{t_0} Q\,a^3\,dt,$$
which for Q-dm with constant $\xi_m$ is $1 - a_i^{\xi_m}$. The choice of $a_i$ is itself an assumption that must be stated. The transfer form breaks the fixed ratio of section (c) at a level set by the coupling; for Q-de the breaking is concentrated at late times, when $\rho_{\rm de}$ is not negligible.

**Model constraint (from the project's decision log).** The leaked pull must raise dark energy's **share**, not make dark energy density **rise** with time; a rising density would contradict the weakening expected in section (d). In the transfer form, $\dot\rho_{\rm de} = -3H(1+w)\rho_{\rm de} + Q$ must stay negative or near zero today. Stage 1 must check this.

**Targets.** Expected value $f_{\rm leak} \approx 1/6$ (the narration's "about a sixth"); the value the model is held to is fitted from the expansion history (section (c4)).

# (c) The fixed dark-to-ordinary ratio, and how the leak alters it

**Tier 1** for the scaling; **Tier 3** for the count; the 1:6:12 share match is **numerology**.

**(c1) Established.** Uncoupled baryons and dark matter both dilute as $a^{-3}$, so
$$\mathcal{R} \equiv \frac{\rho_{\rm dm}}{\rho_b} = \frac{\omega_c}{\omega_b} = {\rm constant}.$$
Observed: $\mathcal{R} \approx 5.36$ (Planck 2018).

**(c2) Model ansatz.** A fixed number of touching neighbors gives a fixed ratio:
$$\mathcal{R}_{\rm model} = N_{\rm in}\,(1-f_{\rm leak}) = 6\,(1-f_{\rm leak}).$$
With no leak, $\mathcal{R} = 6$. With $f_{\rm leak} = 1/6$, $\mathcal{R} = 5$, under the observed 5.36. With $f_{\rm leak}$ fixed as in (c4), $\mathcal{R}_{\rm model}$ is a prediction, tested against Planck in T2 (the ratio tension is listed in the paper's open problems).

**(c3) Model ansatz (numerology).** Shares of the cosmic budget by count, today:
$$\Omega_b = \frac{1}{N_s}, \qquad \Omega_{\rm dm} = \frac{6}{N_s}(1-f_{\rm leak}), \qquad \Omega_{\rm de} = \frac{12}{N_s} + \frac{6}{N_s}f_{\rm leak}, \qquad N_s = 19.$$
The sum is 1 for any $f_{\rm leak}$, so one fitted number moves the dark matter and dark energy shares together by construction.

| Quantity | Count only ($f_{\rm leak}=0$) | $f_{\rm leak} = 1/6$ | Planck 2018 |
|---|---|---|---|
| $\Omega_b$ | 0.053 | 0.053 | 0.049 |
| $\Omega_{\rm dm}$ | 0.316 | 0.263 | 0.265 |
| $\Omega_{\rm de}$ | 0.632 | 0.684 | 0.685 |
| $\mathcal{R}$ | 6 | 5.0 | 5.36 |

**What is real information here.** Because the shares sum to one, $f_{\rm leak}$ cannot be tested on the shares it is fixed on. What remains: (1) the baryon share $1/19 \approx 0.053$ against the measured 0.049, a parameter-free number that differs from Planck by about 7 percent, far outside Planck's sub-percent uncertainty on $\omega_b$, which is why it stays labeled numerology; (2) the ratio, $\mathcal{R} = 5.0$ at one sixth against 5.36, the registered test of (c4); (3) the epoch: the shares line up only near today (section (h)), while the ratio is epoch-free.

**(c4) Model ansatz (how $f_{\rm leak}$ is fixed and tested; one pre-registered role).** From (c3), the model's total matter share is $\Omega_m = \Omega_b + \Omega_{\rm dm} = (7 - 6f_{\rm leak})/19$. The fix inverts this:
$$f_{\rm leak} = 1 - \frac{19\,\Omega_m - 1}{6}, \qquad \sigma_f = \frac{19}{6}\,\sigma_{\Omega_m}.$$
At exactly $f_{\rm leak} = 1/6$, $\Omega_m = 6/19 \approx 0.316$.

- *FIX:* $\Omega_m$ from a flat $w_0w_a$CDM fit to DESI DR2 BAO, the compressed CMB distance priors $R$ and $\ell_A$ only (a5), and supernovae (Pantheon+ and DES SN in separate runs, never combined), with $\omega_b$ from a BBN prior (Cooke, Pettini and Steidel 2018). Planck's $\omega_b$ and $\omega_c$ are not used.
- *TEST:* the predicted ratio
$$\mathcal{R}_{\rm pred} = 6\,(1 - f_{\rm leak}) = 19\,\Omega_m - 1, \qquad \sigma_{\rm pred} = 6\,\sigma_f,$$
against Planck 2018 (TT,TE,EE+lowE+lensing): $\mathcal{R}_{\rm Planck} = \omega_c/\omega_b = 0.1200/0.02237 = 5.36 \pm 0.065$ (propagated as uncorrelated). PASS if $|\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm Planck}| \le 2\sigma_{\rm comb}$ with $\sigma_{\rm comb} = \sqrt{(6\sigma_f)^2 + \sigma_{\rm Planck}^2}$; FAIL otherwise (T2 in MULTIVERSE_TESTS_v1.md, which governs).
- *Stated in advance:* at $f_{\rm leak} = 1/6$, $\mathcal{R}_{\rm pred} = 5.0$, about 5.6 $\sigma$ below Planck counting Planck's uncertainty alone. T2 is expected to fail unless the expansion fit lands well below one sixth.
- *Independence caveat:* $R$ and $\ell_A$ come from the same Planck data as $\omega_c/\omega_b$, and $R$ depends on the matter density. Keeping Planck's $\omega_b$ and $\omega_c$ out of the fix reduces the overlap between fix and test; it does not remove it.

**Local reading (Tier 3).** The model says each place has its own six neighbors, so $\mathcal{R}$ may vary from galaxy to galaxy while its cosmic average stays fixed. In equations, $\mathcal{R}(\mathbf{x})$ is a field whose sky average is (c2). No form for its variation is proposed in v1.

# (d) The unwinding: dark energy as tension tied to a twist variable

**Tier 1** for (d1) and (d2); **Tier 3** for (d3) to (d5).

**(d1) Established.** A cosmological constant is a tension in space: $p_{\rm de} = -\rho_{\rm de}c^2$, i.e. $w = -1$. Negative pressure drives accelerated expansion through
$$\frac{\ddot a}{a} = -\frac{4\pi G}{3}\sum_i\left(\rho_i + \frac{3p_i}{c^2}\right).$$

**(d2) Established.** For any uncoupled component, the equation of state follows from how its density changes with expansion:
$$w(a) = -1 - \frac{1}{3}\frac{d\ln\rho_{\rm de}}{d\ln a}.$$
A density that falls with time gives $w > -1$; constant density gives $w = -1$.

**(d3) Model ansatz.** Dark energy is the strand's stored tension, a function of a dimensionless twist variable $\theta(t)$ (twist relative to today, $\theta_0 \equiv \theta(t_0)$):
$$\rho_{\rm de}(a) = \rho_{\rm de,0}\left(\frac{\theta(a)}{\theta_0}\right)^{n}.$$
The exponent $n$ is free. As an analogy only, $n = 2$ is the elastic case: the strain energy of a twisted elastic rod is quadratic in the twist.

**(d4) Model ansatz.** The strand unwinds: $\dot\theta < 0$. A first candidate law is relaxation at a constant rate $\Gamma_u$:
$$\dot\theta = -\Gamma_u\,\theta.$$
Combining (d2) and (d3) for any unwinding law gives
$$w(a) = -1 - \frac{n}{3}\frac{d\ln\theta}{d\ln a},$$
so any monotonic unwinding with $n > 0$ gives $w > -1$ at all times, with $w$ never crossing $-1$ on its own.

**(d5) Model ansatz (mapping to CPL).** $w_0$ and $w_a$ are the CPL summary of the unwinding: $w_0 = w(a=1)$ and $w_a = -\,dw/da\,|_{a=1}$. Stage 1 must derive the $(w_0, w_a)$ relation implied by each candidate unwinding law and state whether the model predicts a band in the $w_0$ to $w_a$ plane rather than two free numbers.

**Targets.** The model expects $w_0 > -1$ and $w_a < 0$ (dark energy weakening today). DESI DR2 BAO combined with CMB and supernovae prefers this quadrant at 2.8 to 4.2 sigma depending on the supernova sample (DESI Collaboration 2025b). The July 2026 DESI Lyman-alpha Alcock-Paczynski analysis (DESI Collaboration 2026) reports a preference for evolving dark energy of 2.7 to 3.2 sigma depending on the datasets combined. Published CPL fits in this quadrant cross $w = -1$ in the past; pure unwinding (d4) cannot cross, while a coupling (b2) can make the effective $w$ look phantom. Whether leak plus unwinding together reproduce the fitted shape is open. T1 tests only $w_0$; DESI's rise-then-fall history (a phantom past, a crossing of $w = -1$, weakening today) is listed in the paper's open problems.

**Not mapped in v1.** The narration also ties the pace of time to the rate of unwinding, the arrow of time to "wound to unwound" (Penrose's low-entropy beginning as maximum twist), and a rewinding between cycles (by analogy with the Steinhardt and Turok cyclic model). None of these has an equation here.

# (e) The shadow: dark matter as a lagged, refracted copy of the neighbors' baryons

**Tier 1** for (e1) and (e2); **Tier 2** for the nonlocal-kernel precedent; **Tier 3** for (e3) to (e7).

**(e1) Established.** Weak-field gravity with an extra gravitating density:
$$\nabla^2\Phi = 4\pi G\left(\rho_b + \rho_{\rm sh}\right).$$

**(e2) Established (the analogy).** In general relativity, the field of a uniformly moving source points almost exactly at the source's current, extrapolated position, not at its retarded position, because velocity-dependent terms cancel the aberration (Carlip 2000). The model borrows this behavior for the shadow, with the crossing delay $\tau_{\rm lag}$ in place of the light travel time. That substitution is the ansatz, not a result of general relativity.

**(e3) Model ansatz.** Shadow density from the six touching neighbors, $k = 1, \dots, 6$:
$$\rho_{\rm sh}(\mathbf{x},t) = (1-f_{\rm leak})\sum_{k=1}^{6}\int d^3y\;K_{\sigma}(\mathbf{x}-\mathbf{y})\;\tilde\rho^{(k)}_b(\mathbf{y},t),$$
where the delayed, motion-extrapolated neighbor baryon density is
$$\tilde\rho^{(k)}_b(\mathbf{y},t) = \sum_j m^{(k)}_j\,\delta^3\!\left(\mathbf{y} - \left[\mathbf{x}^{(k)}_j(t-\tau_{\rm lag}) + \mathbf{v}^{(k)}_j(t-\tau_{\rm lag})\,\tau_{\rm lag}\right]\right),$$
with $j$ running over baryonic mass elements of neighbor $k$. Each element contributes at the position it would have reached had it kept its velocity from time $t - \tau_{\rm lag}$.

**(e4) Model ansatz.** Locality approximation: recently split neighbors hold the same matter in the same places, $\rho^{(k)}_b \approx \rho_b$ for all six, so
$$\rho_{\rm sh}(\mathbf{x},t) \approx 6\,(1-f_{\rm leak})\,\left[K_\sigma * \tilde\rho_b\right](\mathbf{x},t).$$

**(e5) Model ansatz.** Refraction kernel. Default: a normalized isotropic Gaussian of width $\sigma_{\rm ref}$,
$$K_\sigma(\mathbf{r}) = \left(2\pi\sigma_{\rm ref}^2\right)^{-3/2}\exp\!\left(-\frac{|\mathbf{r}|^2}{2\sigma_{\rm ref}^2}\right), \qquad \int K_\sigma\,d^3r = 1.$$
Normalization makes the total shadow mass $6(1-f_{\rm leak})$ times the baryonic mass, consistent with section (c). Whether $\sigma_{\rm ref}$ is a fixed physical length, a comoving length, or scales with the source is open; see section (f). A published precedent for gravity sourced by an integral transform of ordinary matter is nonlocal gravity (Hehl and Mashhoon 2009, Tier 2).

**(e6) Model ansatz.** Merging clusters, one-dimensional along the merger axis. Components: stars and galaxies $S$, gas $G$, lensing-inferred mass $I$ (the labels of Harvey et al. 2015). Because a symmetric kernel and a linear extrapolation both preserve centroids, the shadow of component $c$ has centroid
$$\tilde x_c(t) = x_c(t-\tau_{\rm lag}) + v_c(t-\tau_{\rm lag})\,\tau_{\rm lag}, \qquad c \in \{S, G\},$$
and the lensing centroid is
$$x_I(t) = \frac{M_S x_S + M_G x_G + 6(1-f_{\rm leak})\left(M_S\tilde x_S + M_G\tilde x_G\right)}{\left[1 + 6(1-f_{\rm leak})\right]\left(M_S + M_G\right)}.$$
Observables (Harvey et al. 2015): $\delta_{SG} = x_G - x_S$, $\delta_{SI} = x_I - x_S$, and the fractional offset $\beta \equiv \delta_{SI}/\delta_{SG}$. Lensing analyses measure peaks, not centroids; the difference must be handled in Stage 2.

**(e7) Model ansatz (the two regimes and the age cutoff).** Let $T = t - t_p$ be the time since first pericenter.

- *Young mergers, $T < \tau_{\rm lag}$.* Both shadows are extrapolated from before the collision, so the gas's shadow did not stop when the gas did. The project's stated expectation is that the shadow keeps its pre-crash speed and sits slightly **ahead** of the galaxies, by more the older and faster the collision (up to $T = \tau_{\rm lag}$), giving $\beta \le 0$. The sign depends on the infall history (velocities at $t - \tau_{\rm lag}$ may be lower than at pericenter), so Stage 1 must compute it with a dynamical merger model rather than assume it.
- *Old mergers, $T > \tau_{\rm lag}$.* The shadows are extrapolated from after the collision. If $\tilde x_G \approx x_G$ and $\tilde x_S \approx x_S$, (e6) reduces to the baryon centroid and
$$\beta \to \frac{M_G}{M_S + M_G},$$
the baryonic gas fraction: the mass "snaps back onto the gas". Collisionless cold dark matter instead predicts $\beta \approx 0$ at all ages.

A fixed $\tau_{\rm lag}$ is therefore an **age cutoff**: offsets as a function of $T$ should change regime near $T = \tau_{\rm lag}$.

**Targets.** $\tau_{\rm lag} \gtrsim 150$ Myr, because the Bullet Cluster subcluster crossed the main core 0.1 to 0.2 Gyr ago (Markevitch et al. 2002) and its mass sits with the galaxies (Clowe et al. 2006). Ensemble constraint to respect: across 72 collisions in 30 systems, the dark mass lies within $5.8 \pm 8.2$ kpc of the stars (Harvey et al. 2015), with the systematics revisited by Wittman, Golovich and Dawson (2018). Older systems bound $\tau_{\rm lag}$: Dawson (2013) finds the Musket Ball merger further progressed than the Bullet Cluster by at least about 0.8 Gyr, with large uncertainty. Abell 520 is a stress test: a dark core near the gas is reported by Jee et al. (2014) and not detected by Clowe et al. (2012); in the model a mass peak at the gas is natural only for $T > \tau_{\rm lag}$, and then the galaxies should carry correspondingly less mass.

**Open (stated, not solved).** $\tau_{\rm lag}$ is underived. NGC 1052-DF2 and DF4, galaxies with very little dark matter, are a problem: recently split neighbors share them, so their shadow should give them dark matter.

# (f) Rotation curves: what sigma_ref must do

**Tier 1** for (f1) and (f2); **Tier 3** for (f3) and (f4).

**(f1) Established.** Circular speed in the spherical approximation:
$$v_c^2(r) = \frac{G\left[M_b(<r) + M_{\rm sh}(<r)\right]}{r}.$$
A flat rotation curve over a range of radii requires $M_b(<r) + M_{\rm sh}(<r) \propto r$ over that range.

**(f2) Established (empirical).** The radial acceleration relation for 2693 points in 153 SPARC galaxies (McGaugh, Lelli and Schombert 2016):
$$g_{\rm obs} = \frac{g_{\rm bar}}{1 - \exp\!\left(-\sqrt{g_{\rm bar}/g_\dagger}\right)}, \qquad g_\dagger = 1.20 \pm 0.02\,({\rm random}) \pm 0.24\,({\rm systematic}) \times 10^{-10}\ {\rm m\,s^{-2}}.$$

**(f3) Model ansatz.** In the model, $g_{\rm obs} = g_{\rm bar} + g_{\rm sh}$, with $g_{\rm sh}$ computed from (e4) and (e5) applied to each galaxy's measured baryon distribution (stars and gas, SPARC mass models; Lelli, McGaugh and Schombert 2016). Targets for $\sigma_{\rm ref}$:

1. Flat outer curves: $M_{\rm sh}(<r)$ must grow roughly in proportion to $r$ out to the last measured point.
2. The radial acceleration relation: one rule for $\sigma_{\rm ref}$ must reproduce (f2) across the sample, including its low-acceleration end.
3. The cap. With a normalized kernel, a single isolated galaxy's shadow totals $6(1-f_{\rm leak})M_b \approx 5M_b$. Beyond the radius where the shadow saturates, the curve must fall as $r^{-1/2}$. At the low-acceleration end of SPARC, $g_{\rm obs}/g_{\rm bar}$ exceeds 6; Stage 1 must check whether the cap allows that, or whether overlapping shadows of neighboring structures, the local variation of $\mathcal{R}$, or a different kernel are needed.

**(f4) Model ansatz (carried motion on orbits).** For a circular orbit of radius $r$ and speed $v_c$, linear extrapolation over $\tau_{\rm lag}$ places the shadow at radius
$$r_{\rm ext} = r\sqrt{1 + \left(\frac{v_c\,\tau_{\rm lag}}{r}\right)^2} > r,$$
pushing shadows outward. Useful conversion: 1 km s$^{-1}$ for 1 Myr is about 1.02 pc. Stage 1 must evaluate $v_c\tau_{\rm lag}$ for disk galaxies with $\tau_{\rm lag} \gtrsim 150$ Myr and decide whether this effect helps or ruins the halo shapes. The analogy in (e2) holds for uniform motion; orbits are accelerated, so the extrapolation rule itself is a further assumption here.

**Candidate extensions.** A size-scaled width $\sigma_{\rm ref} = k\,R_d$ with $R_d$ the disk scale length and $k$ dimensionless (registered as variant T5-B in MULTIVERSE_TESTS_v1.md); a non-Gaussian kernel (not registered). Any further variant adds a free parameter and must be registered before fitting.

# (g) Locality: difference bubbles

**Tier 1** for (g1); **Tier 2** for the local many-worlds receipt; **Tier 3** for (g2) to (g4).

**(g1) Established.** Proper radius reached by a light signal emitted at $t_s$, in an expanding universe:
$$R_{\rm light}(t; t_s) = a(t)\int_{t_s}^{t}\frac{c\,dt'}{a(t')},$$
which reduces to $c\,(t - t_s)$ when expansion is negligible over the interval.

**(g2) Model ansatz.** Two histories that split at time $t_s$, because of an event at $\mathbf{x}_s$, differ only inside a bubble around $\mathbf{x}_s$:
$$|\mathbf{x} - \mathbf{x}_s| \le R_{\rm diff}(t) = R_{\rm light}(t; t_s) \approx c\,(t - t_s).$$
Receipt (Tier 2): Deutsch and Hayden (2000) describe many-worlds locally, with splits spreading no faster than light.

**(g3) Model ansatz.** Sideways distance tracks the age of a split ("family-tree distance"): recent splits are strand-mates, older ones lie across the gaps between strands, the oldest are other ropes. With bubble sizes from (g2), recently split neighbors are identical on galaxy scales except inside small bubbles, which is what justifies (e4).

**(g4) Model ansatz (the local reading).** Measured dark-sector quantities may depend on location. Target for the Hubble tension: local $H_0 = 73.04 \pm 1.04$ km s$^{-1}$ Mpc$^{-1}$ (Riess et al. 2022) against $67.36 \pm 0.54$ (Planck 2018), about 8 percent. The model attributes this to a local accent in the expansion, compatible with the published local-void idea. No equation links the neighbors to a local expansion rate in v1.

# (h) The coincidence

**Tier 1** for (h1); stated as an **open problem** for the model.

**(h1) Established.** The dark energy share at scale factor $a$:
$$\Omega_{\rm de}(a) = \frac{\Omega_{\rm de}\,g(a)}{\Omega_r a^{-4} + \Omega_m a^{-3} + \Omega_{\rm de}\,g(a)}.$$
In $\Lambda$CDM, $\rho_{\rm dm}/\rho_{\rm de} \propto a^{-3}$, so the dark matter and dark energy shares are comparable only during a limited era, which includes today. Why we live in that era is the coincidence problem.

**(h2) Model statement.** The 1:6:12 shares (with the leak) match the measured shares only near today. The model has no mechanism that selects today. Stage 1 task: with Planck 2018 parameters, compute the span of cosmic time during which all three shares stay within a tolerance declared in advance of the section (c) values, and report it without tuning.

**Tier 2 note.** Interacting dark energy has been proposed as a route to the coincidence problem, for example through late-time attractors with a constant ratio of dark matter to dark energy (Boehmer et al. 2008; Wang et al. 2016). The model's leak is an interacting dark energy model, so this is a possible lead. v1 does not claim it.

# (i) Free parameters

"Fixed" means set by the model's construction, not by data. "FIX" is the dataset that should set a parameter; "TEST" is independent data on which the fixed value is then checked. No parameter may be retuned after the test data have been examined. The pre-registered pass and fail criteria, the test IDs (T1 to T6) and the sample splits are in MULTIVERSE_TESTS_v1.md, which governs where this table is less specific.

| Parameter | Meaning | Target or constraint | Dataset that should FIX it | Dataset that should TEST it |
|---|---|---|---|---|
| $N_s$ | Strings per strand | Fixed at 19 by geometry ($1+6+12$) | None (fixed; may not be varied to rescue a test) | Planck 2018 shares; numerology only, already off by about 7 percent in $\Omega_b$ |
| $N_r$ | Strings per rope | Fixed at 133 ($7 \times 19$) | None (fixed) | No cosmological observable identified in v1 |
| $f_{\rm leak}$ | Leaked fraction of the six neighbors' pull, stored as tension | Expected about $1/6$; fitted value $f_{\rm leak} = 1 - (19\,\Omega_m - 1)/6$ (c4); one registered role | DESI DR2 BAO + compressed CMB priors ($R$, $\ell_A$ only) + SNe (Pantheon+ and DES SN in separate runs) (+BBN $\omega_b$), flat $w_0w_a$CDM (T2) | Planck 2018 $\omega_c/\omega_b$ ratio against $\mathcal{R}_{\rm pred} = 6(1-f_{\rm leak})$ (T2) |
| $\xi_m$ or $\xi_e$ | Coupling strength (transfer form only) | Sign fixed: energy from dark matter to dark energy; must satisfy the stability conditions of (b4) | Not registered in v1 | Not registered in v1 (would need its own test in a later version) |
| $w_0$, $w_a$ | CPL summary of the unwinding | $w_0 > -1$ (tested); $w_a < 0$ expected | None from data: the sign is fixed by the model text; Planck 2018 enters only as the CMB prior | DESI DR2 BAO and Lyman-alpha (including arXiv:2607.27410), with Pantheon+ in one run and DES SN (DES-Dovekie) in another (T1) |
| $n$, $\Gamma_u$ | Twist exponent and unwinding rate (ansatz (d3), (d4)) | $n > 0$, $\Gamma_u > 0$; must land in the $w_0 > -1$, $w_a < 0$ quadrant | Not registered in v1 | Not registered in v1 |
| $\epsilon_{\rm far}$ | Faint pull from strings beyond the touching six, mostly arriving as tension | Small and positive; no numerical target yet | Not registered in v1 | Not registered in v1 (needs a target and an observable first) |
| $\tau_{\rm lag}$ | Shadow crossing delay | $\gtrsim 150$ Myr (Bullet Cluster); one value for all systems | Bullet Cluster lower bound plus the training half of aged mergers (T4b); Bullet Cluster alone for the offset sign (T4a) | Test half of aged mergers (T4b); Harvey et al. 2015 and Wittman et al. 2018 offsets (T4a); Abell 520 as a stress test |
| $\sigma_{\rm ref}$ | Refraction spreading width | Flat curves and the radial acceleration relation with one rule | SPARC training half (T5-A, constant width) | SPARC held-out half; NGC 1052-DF2 stress check (T5c) |
| $k$ (variant) | $\sigma_{\rm ref} = k\,R_d$, width scaled by the disk scale length | Registered as variant T5-B | SPARC training half | SPARC held-out half |

Parameters the model hopes to tie together: the decision log's goal is one underlying quantity (for example the twist, or a void width between strings) that sets $f_{\rm leak}$, $\tau_{\rm lag}$ and $\sigma_{\rm ref}$ at once. No such relation is proposed in v1.

# References

- Amendola, L. 2000, "Coupled quintessence", Physical Review D 62, 043511. arXiv:astro-ph/9908023.
- Boehmer, C. G., Caldera-Cabral, G., Lazkoz, R., and Maartens, R. 2008, "Dynamics of dark energy with a coupling to dark matter", Physical Review D 78, 023505. arXiv:0801.1565.
- Brout, D., et al. 2022, "The Pantheon+ Analysis: Cosmological Constraints", The Astrophysical Journal 938, 110. arXiv:2202.04077.
- Carlip, S. 2000, "Aberration and the speed of gravity", Physics Letters A 267, 81 to 87. arXiv:gr-qc/9909087.
- Chen, L., Huang, Q.-G., and Wang, K. 2019, "Distance priors from Planck final release", Journal of Cosmology and Astroparticle Physics 02 (2019) 028. arXiv:1808.05724.
- Chevallier, M., and Polarski, D. 2001, "Accelerating universes with scaling dark matter", International Journal of Modern Physics D 10, 213 to 224. arXiv:gr-qc/0009008.
- Clowe, D., et al. 2006, "A direct empirical proof of the existence of dark matter", The Astrophysical Journal 648, L109 to L113. arXiv:astro-ph/0608407.
- Clowe, D., et al. 2012, "On dark peaks and missing mass: a weak-lensing mass reconstruction of the merging cluster system A520", The Astrophysical Journal 758, 128. arXiv:1209.2143.
- Cooke, R. J., Pettini, M., and Steidel, C. C. 2018, "One percent determination of the primordial deuterium abundance", The Astrophysical Journal 855, 102. arXiv:1710.11129.
- Das, S., Corasaniti, P. S., and Khoury, J. 2006, "Super-acceleration as signature of dark sector interaction", Physical Review D 73, 083509. arXiv:astro-ph/0510628.
- Dawson, W. A. 2013, "The dynamics of merging clusters: a Monte Carlo solution applied to the Bullet and Musket Ball clusters", The Astrophysical Journal 772, 131. arXiv:1210.0014.
- DES Collaboration (Abbott, T. M. C., et al.) 2024, "The Dark Energy Survey: cosmology results with about 1500 new high-redshift Type Ia supernovae using the full 5-year dataset", The Astrophysical Journal Letters 973, L14. arXiv:2401.02929.
- DESI Collaboration (Abdul-Karim, M., et al.) 2025a, "DESI DR2 Results I: Baryon acoustic oscillations from the Lyman alpha forest", arXiv:2503.14739.
- DESI Collaboration (Abdul-Karim, M., et al.) 2025b, "DESI DR2 Results II: Measurements of baryon acoustic oscillations and cosmological constraints", Physical Review D 112, 083515. arXiv:2503.14738.
- DESI Collaboration 2026, "DESI DR2 Results IV: Alcock-Paczynski measurements from the Lyman alpha forest and cosmological constraints", arXiv:2607.27410.
- Deutsch, D., and Hayden, P. 2000, "Information flow in entangled quantum systems", Proceedings of the Royal Society of London A 456, 1759 to 1774. arXiv:quant-ph/9906007.
- Dodelson, S., and Schmidt, F. 2020, Modern Cosmology, 2nd edition (Academic Press). Standard reference for (a1) to (a5) and (h1).
- Gavela, M. B., Hernandez, D., Lopez Honorez, L., Mena, O., and Rigolin, S. 2009, "Dark coupling", Journal of Cosmology and Astroparticle Physics 07 (2009) 034; erratum 05 (2010) E01. arXiv:0901.1611.
- Harvey, D., Massey, R., Kitching, T., Taylor, A., and Tittley, E. 2015, "The non-gravitational interactions of dark matter in colliding galaxy clusters", Science 347, 1462 to 1465. arXiv:1503.07675.
- Hehl, F. W., and Mashhoon, B. 2009, "Nonlocal gravity simulates dark matter", Physics Letters B 673, 279 to 282. arXiv:0812.1059.
- Jee, M. J., Hoekstra, H., Mahdavi, A., and Babul, A. 2014, "Hubble Space Telescope/Advanced Camera for Surveys confirmation of the dark substructure in A520", The Astrophysical Journal 783, 78. arXiv:1401.3356.
- Lelli, F., McGaugh, S. S., and Schombert, J. M. 2016, "SPARC: mass models for 175 disk galaxies with Spitzer photometry and accurate rotation curves", The Astronomical Journal 152, 157. arXiv:1606.09251.
- Linder, E. V. 2003, "Exploring the expansion history of the universe", Physical Review Letters 90, 091301. arXiv:astro-ph/0208512.
- Markevitch, M., et al. 2002, "A textbook example of a bow shock in the merging galaxy cluster 1E0657-56", The Astrophysical Journal 567, L27. arXiv:astro-ph/0110468.
- McGaugh, S. S., Lelli, F., and Schombert, J. M. 2016, "The radial acceleration relation in rotationally supported galaxies", Physical Review Letters 117, 201101. arXiv:1609.05917.
- Planck Collaboration (Aghanim, N., et al.) 2020, "Planck 2018 results. VI. Cosmological parameters", Astronomy and Astrophysics 641, A6. arXiv:1807.06209.
- Riess, A. G., et al. 2022, "A comprehensive measurement of the local value of the Hubble constant with 1 km/s/Mpc uncertainty from the Hubble Space Telescope and the SH0ES team", The Astrophysical Journal Letters 934, L7. arXiv:2112.04510.
- Scolnic, D., et al. 2022, "The Pantheon+ Analysis: The Full Data Set and Light-curve Release", The Astrophysical Journal 938, 113. arXiv:2112.03863.
- Valiviita, J., Majerotto, E., and Maartens, R. 2008, "Large-scale instability in interacting dark energy and dark matter fluids", Journal of Cosmology and Astroparticle Physics 07 (2008) 020. arXiv:0804.0232.
- Wang, B., Abdalla, E., Atrio-Barandela, F., and Pavon, D. 2016, "Dark matter and dark energy interactions: theoretical challenges, cosmological implications and observational signatures", Reports on Progress in Physics 79, 096901. arXiv:1603.08299.
- Wittman, D., Golovich, N., and Dawson, W. A. 2018, "The mismeasure of mergers: revised limits on self-interacting dark matter in merging galaxy clusters", The Astrophysical Journal 869, 104. arXiv:1701.05877.

Data products referred to in section (i) (official links in MULTIVERSE_DATASETS_v1.md): Golovich, N., et al. 2019, "Merging Cluster Collaboration: optical and spectroscopic survey of a radio-selected sample of twenty nine merging galaxy clusters", The Astrophysical Journal Supplement Series 240, 39 (arXiv:1711.01347); and Golovich, N., et al. 2019, "Merging Cluster Collaboration: a panchromatic atlas of radio relic mergers", The Astrophysical Journal 882, 69 (arXiv:1806.10619).
