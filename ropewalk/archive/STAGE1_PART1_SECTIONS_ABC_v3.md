# Stage 1, Part 1: Rule Confirmation (Part 0) & Theoretical Derivations for Sections (a), (b), and (c)

**Date:** 2026-10-30  
**Workspace:** `D:\Argon_Code\Ropewalk`  
**Package Version:** 1.0.1 (Revised Post-Review V2)

> **Precedence Clause (Review V2 Finding N3):** Where `PREREG.md` and any earlier or companion file (`MULTIVERSE_TESTS_v1.md`, `MULTIVERSE_ARGON_HANDOFF.txt`, `GEMINI.md` Rule R12, or this `STAGE1_PART1_SECTIONS_ABC.md` file) disagree, `PREREG.md` governs and `MULTIVERSE_TESTS_v1.md` is superseded for every test it shares with `PREREG.md`. `MULTIVERSE_STAGE1_EQUATIONS.md` governs all mathematical equations. This `STAGE1_PART1_SECTIONS_ABC.md` file is a derivation note with no governing force over test rules or thresholds.

---

## Part 0: Restatement of Project Rules (B0, B5, `GEMINI.md`, and `PREREG.md` Precedence)

1. **Pacing & CONTINUE Protocol (B0.1–B0.4, `GEMINI.md` §1):** Work proceeds one numbered part per turn. Every result is saved to disk at the end of each part, every command and file operation is logged with a local ISO-8601 timestamp in `ACTIVITY_LOG.md`, and execution stops completely at the end of each part with `"END OF PART n. Type CONTINUE for Part n+1: <title>."` until Gregory types `CONTINUE`.
2. **Honesty Labels & Tiers (R1, `GEMINI.md` §2):** Every equation must be marked `[Established]` (standard published physics) or `[Model Ansatz]` (a form chosen to represent the Mandarano Model). Every claim is tagged **Tier 1** (established physics/measurement), **Tier 2** (published peer-reviewed speculation), or **Tier 3** (this model). The $1:6:12$ cosmic budget match is always labeled **numerology**.
3. **Explicit Assumption Tracking (R2, `GEMINI.md` §2):** Every theoretical or numerical assumption is numbered sequentially (`[A1]`, `[A2]`, …) and tracked in `ASSUMPTIONS.md` alongside the specific equations and test outcomes it drives.
4. **No Invented Numbers or Citations (R3):** Every numerical value reported must either be computed directly by project code or read from a cited primary source. Unverified citations are never invented.
5. **Strict Pre-Registration & Freeze Before Testing (R4, G1–G3, `GEMINI.md` §2):** Each free parameter is FIXED on a designated fixing dataset and TESTED on a separate designated test dataset. Before any test dataset is loaded by analysis code, `PREREG.md` (and per-test `FREEZE_<test>.json` files) must be written, hashed with SHA-256, and approved by Gregory. No parameter, kernel shape, sample cut, error model, or threshold may be tuned after seeing test data.
6. **Fixed Thresholds & Plain Failure Reporting (R5, G4, `GEMINI.md` §2, `PREREG.md`):** Every registered test ends in `PASS`, `FAIL`, or `INCONCLUSIVE` using the exact mechanical criteria locked in `PREREG.md` (which supersedes `MULTIVERSE_TESTS_v1.md` wherever amended prior to data access). Failures are reported with the exact same prominence and plainness as passes.
7. **Structural Constants Locked (G5):** $N_s = 19$ and $N_r = 133$ are fixed by the model's geometry and may never be varied to rescue a test.
8. **No Double Counting & Explicit Overlap Disclosure (G2, G6, `PREREG.md` §5.2):** Pantheon+ and DES SN (DES-Dovekie) share low-$z$ supernovae and are never combined in a single fit; every supernova fit is run separately with each and both are reported. Planck's $\omega_b$ and $\omega_c$ are used only to test $f_{\rm leak}$ in T2, never to fix it; the registered T2-A fix uses Planck only via the conditional distance likelihood $(R, \ell_A \mid \omega_b)$ of Chen, Huang & Wang (2019) combined with the primary DESI DR2 / post-LUNA BBN deuterium prior $100\omega_b = 2.218 \pm 0.055$ (with the Cooke, Pettini & Steidel 2018 prior $100\omega_b = 2.166 \pm 0.019$ run as a non-deciding sensitivity check).
9. **Statistical Conventions, Strict Mechanical `INCONCLUSIVE` Triggers, & Code Validation (G7–G9, `PREREG.md` §2):** "$n\sigma$" denotes two-sided Gaussian-equivalent significance from published likelihoods/covariances (except where a one-sided tail is explicitly specified in `PREREG.md`). Every model or analysis choice is resolved in `PREREG.md` before the freeze; post-unblinding invocation of G8 to label a test `INCONCLUSIVE` is forbidden, and `INCONCLUSIVE` is restricted strictly to the mechanical numerical triggers in `PREREG.md` §2 (G8). Analysis code must pass all four validation gates (`G9-a` through `G9-d`), and MCMC chains must satisfy Gelman–Rubin $R - 1 < 0.01$ and $\text{ESS} > 1000$ per parameter.
10. **Official Data Sources, Checksums, & Download Cap (R6, R7):** All datasets come from the official public links in `MULTIVERSE_DATASETS_v1.md` with no paid services or API keys. Every downloaded file is logged in `data/MANIFEST.csv` (URL, date, byte size, SHA-256), download sizes are stated in advance, and any download/install over 1 GB requires prior approval.
11. **Hardware & Resource Isolation (R8, R10, `GEMINI.md` §3, §5):** All work stays strictly inside `D:\Argon_Code\Ropewalk` using a local Windows Python virtual environment (`.venv`). Every Python script starts with single-thread BLAS environment headers (`OMP_NUM_THREADS=1`, etc.), parallel workers are capped at 12 cores (`N_CORES = 12`) at Below Normal priority (`psutil.BELOW_NORMAL_PRIORITY_CLASS`), and WSL2 (`cobaya`/`CLASS`) is only requested if background-only Python is insufficient.
12. **Non-Destructive File Policy & Precedence (R9, R12, `GEMINI.md` §4, `PREREG.md` §1):** Nothing is ever deleted. The six starter files (`00_READ_FIRST.txt`, `MULTIVERSE_ARGON_HANDOFF.txt`, `MULTIVERSE_EQUATION_SHEET_v1.md`, `MULTIVERSE_TESTS_v1.md`, `MULTIVERSE_DATASETS_v1.md`, `MULTIVERSE_PREDICTIONS_PAPER_v1.md`) and `_ORIGINALS/` are never modified. Superseded files are moved to `_TRASH/`, deliverables use new versioned filenames rather than overwriting, and **where `PREREG.md` and any earlier file (including `MULTIVERSE_TESTS_v1.md`) disagree, `PREREG.md` governs**.

**Consistency Check (`MULTIVERSE_TESTS_v1.md` vs. `MULTIVERSE_ARGON_HANDOFF.txt` B5):**  
Both files are at Version 1.0.1 (October 2026). All pre-registered tests (T1, T2, T3, T4a, T4b, T5-A, T5-B, T5c, T6), fixing datasets, test datasets, and PASS/FAIL/INCONCLUSIVE thresholds agree across both documents. At the end of Stage 1 (Part 3), we will produce both the self-contained `MULTIVERSE_STAGE1_EQUATIONS.md` specified in `SESSION_BOOTSTRAP_HANDOFF.md` and the individual `EQUATIONS.md`, `ASSUMPTIONS.md`, and `PREREG.md` files specified in `MULTIVERSE_ARGON_HANDOFF.txt` so that a cold reviewer has every expected file.

**I confirm these rules.**

---

## Section (a): Background Cosmology

**Section Tier:** **Tier 1** for standard relativistic cosmology (a1–a5); **Tier 3** for the dark-sector component mapping (a6).

### (a1) Flat FLRW Metric `[Established | Tier 1]`
Under Assumption **[A1]** (spatially flat, homogeneous, isotropic background geometry on cosmological scales, $k = 0$), the line element in cosmic time $t$ and comoving spherical coordinates $(r, \theta, \phi)$ is
$$ds^2 = -c^2\,dt^2 + a^2(t)\left[dr^2 + r^2\left(d\theta^2 + \sin^2\theta\,d\phi^2\right)\right],$$
where $a(t)$ is the dimensionless scale factor normalized to $a_0 \equiv a(t_0) = 1$ today, related to cosmological redshift $z$ by $1 + z = 1/a$, and the Hubble expansion rate is $H(t) \equiv \dot{a}/a$.

### (a2) First Friedmann Equation `[Established | Tier 1]`
From Einstein's field equations for the metric (a1) with total energy density $\rho_{\rm tot}(a) = \sum_i \rho_i(a)$,
$$H^2(a) = \frac{8\pi G}{3}\sum_i \rho_i(a).$$
Defining present-day critical density $\rho_{\rm crit,0} \equiv \frac{3H_0^2}{8\pi G}$, dimensionless density shares $\Omega_i \equiv \frac{\rho_{i,0}}{\rho_{\rm crit,0}}$, and physical density parameters $\omega_i \equiv \Omega_i h^2$ (with $h \equiv \frac{H_0}{100\text{ km s}^{-1}\text{ Mpc}^{-1}}$), spatial flatness enforces the closure identity
$$\sum_i \Omega_i = \Omega_r + \Omega_\nu + \Omega_b + \Omega_{\rm dm} + \Omega_{\rm de} = 1.$$
When dark matter ($\rm dm$) and dark energy ($\rm de$) are uncoupled ($Q = 0$), the dimensionless expansion rate $E(a) \equiv H(a)/H_0$ is
$$E^2(a) \equiv \frac{H^2(a)}{H_0^2} = \Omega_\gamma a^{-4} + \Omega_\nu f_\nu(a) + \left(\Omega_b + \Omega_{\rm dm}\right)a^{-3} + \Omega_{\rm de}\,g(a),$$
where $g(a) \equiv \rho_{\rm de}(a)/\rho_{\rm de,0}$ with $g(1) = 1$, and $\Omega_\nu f_\nu(a)$ accounts for massive neutrinos (Assumption **[A2]**: standard cosmic neutrino background with $N_{\rm eff} = 3.044$ and $\sum m_\nu = 0.06\text{ eV}$, behaving as radiation $a^{-4}$ at $z \gg z_{\rm nr}$ and as pressureless matter $a^{-3}$ at $z \ll z_{\rm nr}$, where $\Omega_{\nu,0} = \frac{\sum m_\nu}{93.14\,h^2\text{ eV}} \approx 0.00142$ for $h = 0.6736$). When $\rm dm$ and $\rm de$ are coupled ($Q \ne 0$, Section (b)), the replacement $(\Omega_b + \Omega_{\rm dm})a^{-3} + \Omega_{\rm de}g(a) \to \Omega_b a^{-3} + \Omega_{\rm dm}f_{\rm dm}(a) + \Omega_{\rm de}g(a)$ is required.

### (a3) Fluid Continuity Equation (Uncoupled) `[Established | Tier 1]`
For any uncoupled fluid $i$ with equation-of-state parameter $w_i(a) \equiv \frac{p_i(a)}{\rho_i(a)c^2}$, covariant conservation $\nabla_\mu T^{\mu\nu}_{(i)} = 0$ yields
$$\dot{\rho}_i + 3H\left(1 + w_i(a)\right)\rho_i = 0 \quad \Longleftrightarrow \quad \frac{d\ln\rho_i}{d\ln a} = -3\left(1 + w_i(a)\right).$$
For baryons ($w_b = 0$), $\rho_b(a) = \rho_{b,0}\,a^{-3}$; for photons ($w_\gamma = 1/3$), $\rho_\gamma(a) = \rho_{\gamma,0}\,a^{-4}$.

### (a4) Chevallier–Polarski–Linder (CPL) Parametrization `[Established | Tier 1]`
In the CPL parametrization (Chevallier & Polarski 2001; Linder 2003), the dark energy equation of state is expanded to first order in $1 - a = \frac{z}{1+z}$:
$$w(a) = w_0 + w_a(1 - a) = w_0 + w_a\frac{z}{1+z}.$$
Integrating (a3) for an uncoupled dark energy component ($Q = 0$) with $w(a)$ from above gives
$$g_{\rm CPL}(a) \equiv \frac{\rho_{\rm de}(a)}{\rho_{\rm de,0}} = a^{-3(1 + w_0 + w_a)}\exp\!\left[-3w_a(1 - a)\right] = (1+z)^{3(1 + w_0 + w_a)}\exp\!\left(-\frac{3w_a z}{1+z}\right).$$
**$\Lambda\text{CDM}$ Recovery Limit:** Setting $w_0 = -1$ and $w_a = 0$ yields $w(a) = -1$ and $g_{\rm CPL}(a) = 1$ ($\rho_{\rm de}(a) = \rho_{\rm de,0} = \text{const}$).

### (a5) Cosmological Distance & Sound-Horizon Observables `[Established | Tier 1]`
In a flat FLRW background ($k = 0$), the transverse comoving distance $D_M(z)$, Hubble distance $D_H(z)$, angle-averaged BAO distance $D_V(z)$, luminosity distance $D_L(z)$, and distance modulus $\mu(z)$ are
$$D_M(z) = c\int_0^z \frac{dz'}{H(z')}, \qquad D_H(z) = \frac{c}{H(z)}, \qquad D_V(z) = \left[z\,D_M^2(z)\,D_H(z)\right]^{1/3},$$
$$D_L(z) = (1 + z)\,D_M(z), \qquad \mu(z) = 5\log_{10}\!\left(\frac{D_L(z)}{10\text{ pc}}\right) = 5\log_{10}\!\left(\frac{D_L(z)}{1\text{ Mpc}}\right) + 25.$$
The comoving sound horizon at epoch $z$ (evaluating at drag epoch $z_d$ for BAO, $r_d \equiv r_s(z_d)$, and at photon decoupling $z_*$ for the CMB acoustic scale, $r_s(z_*)$) is
$$r_s(z) = \int_z^\infty \frac{c_s(z')}{H(z')}\,dz', \qquad c_s(z) = \frac{c}{\sqrt{3\left(1 + R_b(z)\right)}}, \qquad R_b(z) \equiv \frac{3\rho_b(z)}{4\rho_\gamma(z)} = \frac{3\omega_b}{4\omega_\gamma}(1+z)^{-1}.$$
The compressed CMB distance priors (Chen, Huang & Wang 2019) are the shift parameter $R$ and acoustic scale $\ell_A$:
$$R = \frac{\sqrt{\Omega_m H_0^2}}{c}\,D_M(z_*), \qquad \ell_A = \frac{\pi\,D_M(z_*)}{r_s(z_*)}.$$
*(Sign & formula check: all expressions in (a1)–(a5) match standard cosmology with zero discrepancies.)*

### (a6) Background Component Mapping `[Model Ansatz | Tier 3]`
In the Mandarano Model, the late-time cosmic budget (neglecting $\Omega_\gamma \sim 5\times 10^{-5}$ and $\Omega_\nu \sim 1.4\times 10^{-3}$, Assumption **[A3]**) consists of:
1. **Baryons ($b$):** Ordinary matter on our central string ($w_b = 0$).
2. **The Shadow ($\rm dm$):** The gravitational pull of the $N_{\rm in} = 6$ touching neighbor strings' baryons, diminished by the transit leak $f_{\rm leak}$, acting as pressureless matter ($w_{\rm dm} = 0$).
3. **Outer-Ring Tension ($\rm de$):** Longitudinal tension stored in the $N_{\rm out} = 12$ outer strings of the 19-string strand (augmented by the leaked fraction $f_{\rm leak}$ of the 6 inner neighbors' pull), acting as dark energy with equation of state $w(a)$ governed by strand unwinding (Section (d)).

---

## Section (b): The Leak as Interacting Dark Energy (Static vs. Transfer Mechanisms)

**Section Tier:** **Tier 1** for covariant energy conservation (b1, b2); **Tier 2** for published interacting dark energy (IDE) kernels and perturbation stability theorems (b3, b4); **Tier 3** for the model's leak mapping (b5).

### (b1) Coupled Dark-Sector Continuity Equations `[Established | Tier 1]`
When energy is exchanged exclusively within the dark sector while baryons remain separately conserved ($\nabla_\mu T^{\mu\nu}_{(b)} = 0$), total dark-sector energy conservation $\nabla_\mu\left(T^{\mu\nu}_{({\rm dm})} + T^{\mu\nu}_{({\rm de})}\right) = 0$ in the FLRW background takes the form
$$\dot{\rho}_{\rm dm} + 3H\rho_{\rm dm} = -Q, \qquad \dot{\rho}_{\rm de} + 3H(1 + w)\rho_{\rm de} = +Q, \qquad \dot{\rho}_b + 3H\rho_b = 0.$$
**Sign Convention Check:** Here $Q > 0$ denotes energy transfer **from shadow dark matter ($\rm dm$) to outer-ring tension ($\rm de$)**, which matches the physical direction of the leak. In the notation of Boehmer et al. (2008), $Q$ has the same sign as here; in the notation of Gavela et al. (2009), their coupling $Q_{\rm G}$ sits with $+Q_{\rm G}$ on the $\dot{\rho}_{\rm dm}$ equation, so $Q_{\rm G} = -Q$.

### (b2) Effective Equations of State `[Established | Tier 1]`
Rewriting the coupled equations (b1) in the uncoupled form $\dot{\rho}_i + 3H(1 + w_i^{\rm eff})\rho_i = 0$ defines the effective equations of state (Gavela et al. 2009, Eqs. 5–6, adapted to $Q = -Q_{\rm G}$):
$$w_{\rm dm}^{\rm eff}(a) = \frac{Q}{3H\rho_{\rm dm}}, \qquad w_{\rm de}^{\rm eff}(a) = w(a) - \frac{Q}{3H\rho_{\rm de}}.$$
**Sign & Physical Consequence Check:** For $Q > 0$ (leak from $\rm dm$ to $\rm de$):
- $w_{\rm dm}^{\rm eff} > 0$: shadow dark matter dilutes faster than $a^{-3}$.
- $w_{\rm de}^{\rm eff} < w(a)$: energy injection slows the dilution of $\rho_{\rm de}$, making its effective equation of state more negative than its bare intrinsic tension equation of state $w(a)$. Consequently, even if bare unwinding enforces $w(a) > -1$ everywhere, a sufficiently large $Q/(3H\rho_{\rm de}) > 1 + w(a)$ produces an effective phantom regime $w_{\rm de}^{\rm eff}(a) < -1$ (Das, Corasaniti & Khoury 2006).

---

### Full Derivation of Mechanism 1: The Static Form (Transit Efficiency, $Q \equiv 0$)

#### (b5-S1) Static Shadow Density & Zero Ratio Drift `[Model Ansatz | Tier 3]`
In the Static Form, $f_{\rm leak} \in [0, 1)$ is a constant geometric transmission loss across the inter-string gap (Assumption **[A4]**). No energy is transferred dynamically over cosmic time in the continuity equations ($Q(a) \equiv 0$):
$$\rho_{\rm dm}(a) = (1 - f_{\rm leak})\,N_{\rm in}\,\rho_b(a) = 6(1 - f_{\rm leak})\,\rho_{b,0}\,a^{-3}.$$
Because $\rho_b(a) = \rho_{b,0}\,a^{-3}$ and $\rho_{\rm dm}(a)$ both scale identically as $a^{-3}$, the cosmic dark-to-ordinary ratio is strictly constant at all epochs:
$$\mathcal{R}_{\rm static}(a) \equiv \frac{\rho_{\rm dm}(a)}{\rho_b(a)} = 6(1 - f_{\rm leak}) = \text{const}, \qquad \frac{d\mathcal{R}_{\rm static}}{da} = 0.$$
**$\Lambda\text{CDM}$ Recovery Limit:** In the background expansion, $\rho_m(a) = \rho_b(a) + \rho_{\rm dm}(a) = \left[1 + 6(1 - f_{\rm leak})\right]\rho_{b,0}\,a^{-3} = \rho_{m,0}\,a^{-3}$, which reproduces the exact $\Lambda\text{CDM}$ (or $w_0w_a\text{CDM}$) matter dilution law at all redshifts from BBN and recombination ($z_* \approx 1089$) to $z = 0$.

#### (b5-S2) Bookkeeping of How Leaked Pull Becomes Non-Diluting Tension in the Static Form `[Model Ansatz | Tier 3]`
A critical theoretical question noted in `MULTIVERSE_EQUATION_SHEET_v1.md` (b5) is: *if $f_{\rm leak}$ of the 6 neighbors' gravitational pull is diverted to the outer 12 strings without dynamic transfer $Q$, why does that diverted share behave as non-diluting tension ($w \approx -1$) rather than diluting as $a^{-3}$ like the baryons that sourced it?*

Let us prove why a naive additive density rule fails and state the exact required ansatz:
- **Why naive epoch-by-epoch density addition fails:** Suppose one wrote $\rho_{\rm de}^{\rm naive}(a) = \rho_{\rm de,bare}(a) + 6 f_{\rm leak}\,\rho_b(a)$. Then the leaked piece $6 f_{\rm leak}\,\rho_{b,0}\,a^{-3}$ would satisfy $\dot{\rho}_{\rm leak} + 3H\rho_{\rm leak} = 0$ ($w_{\rm leak} = 0$). It would gravitate as pressureless cold dark matter, contributing to $\Omega_m a^{-3}$ rather than $\Omega_{\rm de} g(a)$, leaving $\Omega_m = 7/19$ unchanged and failing to produce dark energy!
- **Required Static-Form Bookkeeping (`[Model Ansatz]`, Assumption [A4]):** In the Static Form, the 19-string strand geometry determines the **boundary partition of stress-energy modes** rather than converting $a^{-3}$ dust into $a^0$ vacuum energy epoch by epoch:
  1. Transverse inter-string Newtonian attraction from the $N_{\rm in} = 6$ touching strings couples to localized baryonic rest mass with transmission efficiency $(1 - f_{\rm leak})$, yielding the $a^{-3}$ shadow density $\Omega_{\rm dm} = \frac{6}{19}(1 - f_{\rm leak})$.
  2. The remaining capacity of the 19-string strand—comprising the $N_{\rm out} = 12$ outer strings plus the fraction $f_{\rm leak}$ of the 6 inner interfaces redirected into longitudinal helical stretch—carries **bulk longitudinal string tension** with intrinsic equation of state $p_{\rm de} = w(a)\rho_{\rm de}c^2$ ($w(a) \approx -1$), fixing today's tension share at
     $$\Omega_{\rm de,0} = \frac{12 + 6 f_{\rm leak}}{19}, \qquad \rho_{\rm de}(a) = \rho_{\rm crit,0}\,\Omega_{\rm de,0}\,g(a).$$
  3. **Honest Consequence:** Because $\rho_{\rm dm}(a) \propto a^{-3}$ while $\rho_{\rm de}(a) \propto g(a)$, the relation $\Omega_{\rm de}(a) = \frac{12 + 6 f_{\rm leak}}{19}$ holds **only at $a = 1$ (today)** (Open Problem 5, the coincidence problem), whereas $\mathcal{R}(a) = 6(1 - f_{\rm leak})$ holds at **all** $a$.

---

### Full Derivation of Mechanism 2: The Transfer Form (Dynamic IDE, $Q > 0$)

In the Transfer Form (Assumption **[A5]**), the shadow starts at an initial scale factor $a_i$ with the full un-leaked ratio $\mathcal{R}(a_i) = N_{\rm in} = 6$, meaning $\rho_{\rm dm}(a_i) a_i^3 = 6\rho_{b,0}$, and continuously loses energy to outer-ring tension via $Q > 0$ so that by $a = 1$ today the cumulative leaked fraction of comoving shadow energy is $f_{\rm leak}$:
$$f_{\rm leak} \equiv 1 - \frac{\rho_{\rm dm}(1)}{\rho_{\rm dm}(a_i)\,a_i^3} = \frac{1}{6\rho_{b,0}}\int_{t_i}^{t_0} Q(t)\,a^3(t)\,dt = \frac{1}{6\rho_{b,0}}\int_{a_i}^{1} \frac{Q(a)\,a^2}{H(a)}\,da.$$
Furthermore, the model constraint in (b5) requires that dark energy density **not rise today** ($\dot{\rho}_{\rm de}(t_0) \le 0$, so its share grows only because matter dilutes faster):
$$\dot{\rho}_{\rm de}(t_0) = -3H_0\left(1 + w_0\right)\rho_{\rm de,0} + Q_0 \le 0 \quad \Longleftrightarrow \quad w_{\rm de}^{\rm eff}(a=1) = w_0 - \frac{Q_0}{3H_0\rho_{\rm de,0}} \ge -1.$$

Let us solve the exact background evolution, ratio drift $\mathcal{R}(a)$, non-rising condition $\dot{\rho}_{\rm de}(t_0) \le 0$, and perturbation stability for each of the four published coupling forms in (b3).

---

#### Case 1: Coupling Proportional to Shadow Dark Matter, $Q_{\rm dm} = \xi_m H \rho_{\rm dm}$ ($\xi_m > 0$) `[Established IDE form | Tier 2]`

1. **Exact Shadow DM Evolution & Ratio Drift:**
   Substituting $Q = \xi_m H \rho_{\rm dm}$ into (b1) gives
   $$\frac{d\rho_{\rm dm}}{da} + \frac{3 + \xi_m}{a}\rho_{\rm dm} = 0 \implies \rho_{\rm dm}(a) = \rho_{\rm dm,0}\,a^{-(3 + \xi_m)}.$$
   Dividing by $\rho_b(a) = \rho_{b,0}\,a^{-3}$ gives the exact redshift drift of the dark-to-ordinary ratio:
   $$\mathcal{R}(a) = \mathcal{R}_0\,a^{-\xi_m} = 6(1 - f_{\rm leak})\,(1 + z)^{\xi_m}.$$
   Imposing $\mathcal{R}(a_i) = 6$ at initial epoch $a_i = (1 + z_i)^{-1}$ fixes $\xi_m$ in terms of $f_{\rm leak}$ and $a_i$:
   $$1 - f_{\rm leak} = a_i^{\xi_m} \implies \xi_m = \frac{\ln(1 - f_{\rm leak})}{\ln a_i} = -\frac{\ln(1 - f_{\rm leak})}{\ln(1 + z_i)} > 0.$$
   *Numerical check:* For $f_{\rm leak} = 1/6$ ($\ln(5/6) = -0.18232$), if the transfer begins at recombination ($z_i = z_* = 1089$), then $\xi_m = 0.18232 / \ln(1090) = 0.02607$, and $\mathcal{R}(z)$ drifts by $20\%$ between $z = 1089$ ($\mathcal{R} = 6.0$) and $z = 0$ ($\mathcal{R} = 5.0$).

2. **Exact Dark Energy Density Solution & Negative-Energy Pathology:**
   For constant bare tension equation of state $w$, the dark energy continuity equation in (b1) is
   $$\frac{d\rho_{\rm de}}{da} + \frac{3(1 + w)}{a}\rho_{\rm de} = \frac{\xi_m}{a}\rho_{\rm dm,0}\,a^{-(3 + \xi_m)}.$$
   Multiplying by integrating factor $a^{3(1+w)}$ and integrating from $a$ to $1$ yields the exact closed-form solution:
   $$\rho_{\rm de}(a) = \left(\rho_{\rm de,0} + \frac{\xi_m\,\rho_{\rm dm,0}}{\xi_m - 3w}\right)a^{-3(1+w)} - \frac{\xi_m\,\rho_{\rm dm,0}}{\xi_m - 3w}\,a^{-(3 + \xi_m)}.$$
   **Fatal Background Pathology (Gavela et al. 2009):** For any accelerating dark energy ($w < -1/3 < 0$) and $\xi_m > 0$ (leak from $\rm dm$ to $\rm de$), we have $\xi_m - 3w = 3|w| + \xi_m > 0$ and $3 + \xi_m > 3(1 + w)$. Therefore, as $a \to 0$, the second term dominates with a **negative sign**, forcing $\rho_{\rm de}(a) < 0$ for all scale factors earlier than
   $$a_{\rm neg} = \left(1 + \frac{3|w| + \xi_m}{\xi_m}\frac{\Omega_{\rm de,0}}{\Omega_{\rm dm,0}}\right)^{-\frac{1}{3|w| + \xi_m}}.$$
   For $\xi_m = 0.02607$, $w = -1$ (or non-degenerate $w = -0.99$), and $\Omega_{\rm de,0}/\Omega_{\rm dm,0} = 0.684/0.263 = 2.60$, $\rho_{\rm de}(a)$ becomes **negative** at $a_{\rm neg} = (302.3)^{-1/3.026} = 0.151$ ($z_{\rm neg} = 5.606$ at $w = -1$, or $z_{\rm neg} = 5.58$ at $w = -0.99$)! Thus $Q_{\rm dm}$ cannot describe a positive tension energy density prior to $z \approx 5.6$.

3. **Early-Time Super-Horizon Perturbation Instability (Valiviita et al. 2008; Gavela et al. 2009):**
   In the convention of Gavela et al. (2009), where $Q_{\rm G} = -Q = -\xi_m H \rho_{\rm dm}$, the non-adiabatic perturbation "doom factor" (defined for $w \ne -1$) is
   $$d(a) \equiv \frac{Q_{\rm G}}{3H\rho_{\rm de}(1 + w)} = -\frac{\xi_m}{3(1 + w)}\frac{\rho_{\rm dm}(a)}{\rho_{\rm de}(a)}.$$
   For any $w > -1$, because $\rho_{\rm dm}/\rho_{\rm de}$ diverges at $a = a_{\rm neg}$ and changes sign for $a < a_{\rm neg}$ (entering the $d > 0, |d| \gg 1$ unstable regime), constant-$w$ fluid perturbations suffer catastrophic exponential blow-up on super-Hubble scales at early times.

---

#### Case 2: Coupling Proportional to Dark Energy (Tension), $Q_{\rm de} = \xi_e H \rho_{\rm de}$ ($\xi_e > 0$) `[Established IDE form | Tier 2]`

1. **Exact Dark Energy Density Solution:**
   Substituting $Q = \xi_e H \rho_{\rm de}$ into the dark energy continuity equation in (b1) gives
   $$\dot{\rho}_{\rm de} + 3H\left(1 + w(a) - \frac{\xi_e}{3}\right)\rho_{\rm de} = 0 \implies w_{\rm de}^{\rm eff}(a) = w(a) - \frac{\xi_e}{3}.$$
   For constant bare $w$, this integrates directly to
   $$\rho_{\rm de}(a) = \rho_{\rm de,0}\,a^{-3(1 + w - \xi_e/3)} = \rho_{\rm de,0}\,a^{-3(1 + w_{\rm de}^{\rm eff})}.$$
   Unlike $Q_{\rm dm}$, **$\rho_{\rm de}(a)$ remains strictly positive ($\rho_{\rm de}(a) > 0$) for all $a > 0$**.

2. **Non-Rising Dark Energy Density Condition ($\dot{\rho}_{\rm de}(t_0) \le 0$):**
   Evaluating $\dot{\rho}_{\rm de}$ at $a = 1$ gives
   $$\dot{\rho}_{\rm de}(t_0) = -3H_0\left(1 + w_0 - \frac{\xi_e}{3}\right)\rho_{\rm de,0} \le 0 \quad \Longleftrightarrow \quad w_{\rm de}^{\rm eff}(1) = w_0 - \frac{\xi_e}{3} \ge -1 \quad \Longleftrightarrow \quad 0 < \xi_e \le 3(1 + w_0).$$
   Thus, for dark energy density not to rise today while $\xi_e > 0$, the bare unwinding equation of state today must satisfy $w_0 \ge -1 + \xi_e/3 > -1$.

3. **Exact Shadow DM Evolution, Transferred Fraction $f_{\rm leak}$, & Ratio Drift:**
   Substituting $\rho_{\rm de}(a)$ into the shadow dark matter equation $\frac{d}{da}(\rho_{\rm dm}a^3) = -\frac{\xi_e}{a}\rho_{\rm de}(a)a^3$ and integrating from $a_i$ to $a$ (with $w_{\rm de}^{\rm eff} < 0$) yields
   $$\rho_{\rm dm}(a)a^3 = \rho_{\rm dm,0} + \frac{\xi_e\,\rho_{\rm de,0}}{-3w_{\rm de}^{\rm eff}}\left(1 - a^{-3w_{\rm de}^{\rm eff}}\right).$$
   Dividing by $\rho_{b,0}$ gives the exact dark-to-ordinary ratio as a function of scale factor:
   $$\mathcal{R}(a) \equiv \frac{\rho_{\rm dm}(a)}{\rho_b(a)} = \mathcal{R}_0 + \frac{\xi_e}{3|w_{\rm de}^{\rm eff}|}\frac{\Omega_{\rm de,0}}{\Omega_{b,0}}\left(1 - a^{3|w_{\rm de}^{\rm eff}|}\right).$$
   Notice two critical physical properties of $Q_{\rm de}$:
   - **Insensitivity to early start epoch $a_i$:** Because $a_i^{3|w_{\rm de}^{\rm eff}|} \approx a_i^3 \ll 1$ for any early epoch ($a_i \le a_* \approx 1/1090$), virtually ** zero transfer happens before recombination** ($|\mathcal{R}(a_*) - \mathcal{R}(0_{\rm early})| \sim 10^{-9}$). All energy transfer occurs at late times ($z \lesssim 1$) when dark energy becomes comparable to matter.
   - **Required coupling $\xi_e$ if all of $f_{\rm leak}$ is dynamically transferred:** Setting $\mathcal{R}(a_i \to 0) = 6$, $\mathcal{R}_0 = 6(1 - f_{\rm leak})$, and $\Omega_{\rm de,0}/\Omega_{b,0} = 12 + 6f_{\rm leak}$ gives
     $$6 f_{\rm leak} = \frac{\xi_e}{3|w_{\rm de}^{\rm eff}|}\left(12 + 6 f_{\rm leak}\right) \implies \xi_e = \frac{3|w_{\rm de}^{\rm eff}|\,f_{\rm leak}}{2 + f_{\rm leak}}.$$
     For $f_{\rm leak} = 1/6$ and $w_{\rm de}^{\rm eff} \approx -1$, this requires $\xi_e = \frac{3(1/6)}{13/6} = \frac{3}{13} \approx 0.2308$, which in turn requires bare $w_0 \ge -1 + \frac{\xi_e}{3} = -\frac{12}{13} \approx -0.923$ to prevent $\rho_{\rm de}$ from rising today.
   - **Conflict with constant ratio (P3) & T2:** If all of $f_{\rm leak} \approx 1/6$ is generated at late times ($z \lesssim 1$) via $Q_{\rm de}$, then at recombination ($z_* = 1089$) the ratio was still the un-leaked value $\mathcal{R}(z_*) = 6.0$, whereas today at $z = 0$ it is $\mathcal{R}(0) = 5.0$!

4. **Perturbation Stability (Gavela et al. 2009):**
   For $Q_{\rm de} = \xi_e H \rho_{\rm de}$ ($Q_{\rm G} = -\xi_e H \rho_{\rm de}$), the doom factor is
   $$d = \frac{Q_{\rm G}}{3H\rho_{\rm de}(1 + w)} = -\frac{\xi_e}{3(1 + w)}.$$
   When $\xi_e > 0$ (leak from $\rm dm$ to $\rm de$) and bare $w > -1$ (unwinding), **$d < 0$ at all epochs**. As proved by Gavela et al. (2009), $d < 0$ is the **instability-free branch**: early-time super-Hubble perturbations are completely stable.

---

#### Case 3: Constant Physical Decay Rate, $Q_{\rm rate} = \Gamma \rho_{\rm dm}$ ($\Gamma > 0$) `[Established IDE form | Tier 2]`
- **Exact Shadow DM & Ratio Drift:** $\rho_{\rm dm}(t) = \rho_{\rm dm}(t_i)(a_i/a)^3 e^{-\Gamma(t - t_i)}$, so $\mathcal{R}(t) = 6\,e^{-\Gamma t}$ (for $t_i \to 0$). Reproducing $\mathcal{R}(t_0) = 6(1 - f_{\rm leak})$ at $t_0 \approx 13.8\text{ Gyr}$ requires $\Gamma t_0 = -\ln(1 - f_{\rm leak}) \approx 0.1823$ ($\Gamma^{-1} \approx 75.7\text{ Gyr}$).
- **Pathology & Stability:** Because $Q_{\rm rate}/(3H\rho_{\rm de}) = \frac{\Gamma}{3H}\frac{\rho_{\rm dm}}{\rho_{\rm de}}$ scales as $a^{3/2} \cdot a^{-3(1+w)} \sim a^{-3/2}$ during matter domination, $\rho_{\rm de}(a)$ still turns negative at early times and suffers the Valiviita et al. (2008) early-time perturbation instability ($d \propto -a^{-3/2}/(1+w)$ changes sign when $\rho_{\rm de}$ crosses zero). Furthermore, transferring $\sim 16.7\%$ of dark matter into dark energy between recombination ($t_* \approx 380\text{ kyr}$, where $\Gamma t_* \sim 5\times 10^{-6}$) and today shifts the late-time comoving matter density relative to recombination by $\Delta\Omega_m/\Omega_m \approx 14\%$ and modifies the late-time ISW effect and structure growth. *(Note: published $\Gamma^{-1} \gtrsim 150\text{–}260\text{ Gyr}$ bounds apply to dark matter decaying into dark radiation rather than $w \approx -1$ dark energy.)*

#### Case 4: Coupled Quintessence, $Q_{\rm field} = \beta\,\rho_{\rm dm}\,\dot{\phi}/M_{\rm Pl}$ `[Established IDE form | Tier 2]`
- Replaces the fluid description of tension with a canonical scalar field $\phi$ moving in a potential $V(\phi)$ (Amendola 2000). While free of fluid sound-speed instabilities, it introduces an attractive fifth force between shadow dark matter particles with $G_{\rm eff} = G(1 + 2\beta^2)$, modifies the matter power spectrum and $r_s(z_*)$ during matter domination, and introduces unregistered potential parameters not present in v1.

---

### Summary Table: Comparison of Candidate Leak Mechanisms

| Mechanism / Coupling | $\mathcal{R}(a) = \rho_{\rm dm}/\rho_b$ Evolution | $\rho_{\rm de}(a) > 0$ for all $a > 0$? | Early-Time Perturbations Stable? | Pre-Recombination Physics Standard? | Compressed CMB Priors $(R, \ell_A)$ Valid? |
|---|---|---|---|---|---|
| **Static Form ($Q = 0$)** | $\mathcal{R}(a) = 6(1 - f_{\rm leak}) = \text{const}$ | **Yes** | **Yes** | **Yes** ($\rho_{\rm dm} \propto a^{-3}$) | **Yes (Exact)** |
| **Transfer: $Q_{\rm de} = \xi_e H \rho_{\rm de}$** | $\mathcal{R}_0 + \frac{\xi_e \Omega_{\rm de,0}}{3|w_{\rm eff}|\Omega_{b,0}}(1 - a^{3|w_{\rm eff}|})$ (late-time drift) | **Yes** | **Yes** (for $\xi_e > 0, w > -1$) | **Yes** ($\Delta\rho_{\rm dm}/\rho_{\rm dm} < 10^{-9}$ at $z \ge z_*$) | **Approximate** (acoustic scale valid, but $\Omega_{m,{\rm early}} \ne \Omega_{m,0}$) |
| **Transfer: $Q_{\rm dm} = \xi_m H \rho_{\rm dm}$** | $6(1 - f_{\rm leak})(1 + z)^{\xi_m}$ (all-epoch drift) | **No** ($\rho_{\rm de} < 0$ for $z \gtrsim 5.6$) | **No** (Valiviita et al. 2008 blow-up) | **No** (alters $z_{\rm eq}, H(z), r_s(z_*)$) | **No (Invalid)** |
| **Transfer: $Q_{\rm rate} = \Gamma \rho_{\rm dm}$** | $6\,e^{-\Gamma t}$ (late-time exponential drift) | **No** ($\rho_{\rm de} < 0$ at early times) | **No** (diverges when $\rho_{\rm de}=0$) | **Yes** ($\Gamma t_* \sim 10^{-5}$), but alters late ISW | **No** ($\Omega_{m,{\rm early}} \ne \Omega_{m,0}$ by $16.7\%$) |

---

### Crucial Early-Universe Requirement: Validity of Compressed CMB Priors vs. Full Boltzmann (`CLASS`/`CAMB`)

Per `SESSION_BOOTSTRAP_HANDOFF.md` and Section (a5) of `MULTIVERSE_EQUATION_SHEET_v1.md`:
1. **Why Compressed CMB Priors $(R, \ell_A)$ Require a Standard Early Universe:**  
   The Chen, Huang & Wang (2019) distance priors compress the full Planck 2018 CMB temperature and polarization power spectra into $R = \frac{\sqrt{\Omega_m H_0^2}}{c}D_M(z_*)$ and $\ell_A = \frac{\pi D_M(z_*)}{r_s(z_*)}$ under the explicit assumption that pre-recombination dark matter dilutes as $\rho_{\rm dm}(a) = \rho_{\rm dm,0}\,a^{-3}$ and has standard adiabatic perturbations.
2. **Status Under Each Mechanism:**
   - **Static Form ($Q = 0$):** Dark matter dilutes as $\rho_{\rm dm}(a) = 6(1 - f_{\rm leak})\rho_{b,0}\,a^{-3}$ at all redshifts $z \in [0, \infty)$. Pre-recombination physics is 100% standard. **The compressed CMB priors $(R, \ell_A)$ are strictly valid.**
   - **Late-Time Transfer ($Q_{\rm de} = \xi_e H \rho_{\rm de}$):** Because $\rho_{\rm de}(z_*)/\rho_{\rm dm}(z_*) \sim 10^{-9}$, the coupling is dynamically inactive before recombination ($z \ge z_* \approx 1089$), so $r_s(z_*)$ and pre-recombination acoustic oscillations are unmodified. However, if $f_{\rm leak} \approx 1/6$ is transferred between $z \sim 1$ and $z = 0$, then the comoving matter density at recombination $\Omega_{m,{\rm early}} = \Omega_b + 6\Omega_b = 7/19 \approx 0.368$ differs from the late-time matter density today $\Omega_{m,0} = (7 - 6f_{\rm leak})/19 \approx 0.316$ by $\Delta\Omega_m \approx 0.053$, invalidating the identification of $\Omega_{m,0}$ with the pre-recombination matter density in $R$.
   - **All-Epoch Transfer ($Q_{\rm dm} = \xi_m H \rho_{\rm dm}$):** Modifies $\rho_{\rm dm}(a) \propto a^{-(3+\xi_m)}$ prior to recombination, shifting matter-radiation equality $z_{\rm eq}$, altering $H(z)$ and $r_s(z_*)$, and inducing super-horizon perturbation instabilities. **Compressed CMB priors are completely invalid for $Q_{\rm dm}$.**
3. **What the Full Boltzmann Route (`CLASS` / `CAMB`) Would Require Instead:**  
   If an early-active or large-transfer IDE model were tested against the CMB, compressed priors would have to be replaced by a full Boltzmann solver (`CLASS` or `CAMB` coupled to `cobaya` in WSL2) with:
   - **Modified Background Module:** Numerical integration of the coupled system (b1) from $a_{\rm ini} = 10^{-14}$ to $a = 1$, plus a physical regulator (e.g., a phase-space or twist-threshold cutoff) if $Q_{\rm dm}$ is used so $\rho_{\rm de}(a)$ does not turn negative at $a < a_{\rm neg}$.
   - **Modified Linear Perturbation Equations:** Covariant conservation $\nabla_\nu T^{\mu\nu}_{(A)} = Q^\mu_{(A)}$ with energy-momentum transfer 4-vector $Q^\mu_{({\rm de})} = -Q^\mu_{({\rm dm})} = Q u^\mu_{({\rm dm})}$ (where $u^\mu_{({\rm dm})}$ is the dark matter 4-velocity, avoiding momentum violation in the DM rest frame). In synchronous gauge (with metric potentials $h, \eta$ and conformal Hubble rate $\mathcal{H} = aH$), the coupled density contrast $\delta_i \equiv \delta\rho_i/\rho_i$ and velocity divergence $\theta_i$ equations in `CLASS` (`perturbations.c`) become `[Established | Tier 2, Valiviita et al. 2008]`:
     $$\delta'_{\rm dm} + \theta_{\rm dm} + \frac{h'}{2} = -\frac{aQ}{\rho_{\rm dm}}\left(\frac{\delta Q}{Q} - \delta_{\rm dm}\right), \qquad \theta'_{\rm dm} + \mathcal{H}\theta_{\rm dm} = 0,$$
     $$\delta'_{\rm de} + 3\mathcal{H}\left(c_{s,{\rm de}}^2 - w\right)\delta_{\rm de} + (1 + w)\left(\theta_{\rm de} + \frac{h'}{2}\right) + 9\mathcal{H}^2(1 + w)\left(c_{s,{\rm de}}^2 - c_a^2\right)\frac{\theta_{\rm de}}{k^2} = +\frac{aQ}{\rho_{\rm de}}\left(\frac{\delta Q}{Q} - \delta_{\rm de}\right),$$
     $$\theta'_{\rm de} + \left[\mathcal{H}(1 - 3c_{s,{\rm de}}^2) + \frac{aQ}{\rho_{\rm de}}\frac{1 + c_{s,{\rm de}}^2}{1 + w}\right]\theta_{\rm de} - \frac{k^2 c_{s,{\rm de}}^2}{1 + w}\delta_{\rm de} = \frac{aQ}{(1 + w)\rho_{\rm de}}\,\theta_{\rm dm},$$
     where $c_{s,{\rm de}}^2 = 1$ is the rest-frame dark-energy sound speed, $c_a^2 = w - \frac{w'}{3\mathcal{H}(1+w)}$ is the adiabatic sound speed, and theParameterized Post-Friedmann (PPF) formalism is required if $w(a)$ crosses $-1$.
   - **Full Planck 2018 Likelihoods:** Evaluation against the full `plik_rd12_HM_v22_TTTEEE`, `simall_100x143`, and `lensing` likelihoods rather than $(R, \ell_A)$.

---

## Section (c): The Fixed Ratio, the Budget Shares, and the Ratio Tension

**Section Tier:** **Tier 1** for standard uncoupled scaling (c1); **Tier 3** for the model's neighbor count and T2 mapping (c2–c4), with the $1:6:12$ cosmic share match explicitly labeled **numerology**.

### (c1) Standard Uncoupled Dark-to-Ordinary Ratio `[Established | Tier 1]`
When both baryons and cold dark matter are uncoupled pressureless fluids ($\rho_b \propto a^{-3}, \rho_c \propto a^{-3}$), their density ratio is time-independent:
$$\mathcal{R} \equiv \frac{\rho_{\rm dm}(a)}{\rho_b(a)} = \frac{\Omega_{\rm dm}}{\Omega_b} = \frac{\omega_c}{\omega_b} = \text{const}.$$
From Planck 2018 base $\Lambda\text{CDM}$ (`TT,TE,EE+lowE+lensing`, Planck Collaboration 2020, Table 2):
$$\omega_b = 0.02237 \pm 0.00015, \qquad \omega_c = 0.1200 \pm 0.0012,$$
which yields (adding relative uncertainties in quadrature with correlation ignored, as pre-registered in T2):
$$\mathcal{R}_{\rm Planck} = \frac{0.1200}{0.02237} = 5.3643 \pm 0.0646 \quad \text{(registered in T2 as } 5.36 \pm 0.065\text{)}.$$

### (c2) Model Dark-to-Ordinary Ratio `[Model Ansatz | Tier 3]`
In the Static Form with $N_{\rm in} = 6$ touching neighbor strings and transit leak fraction $f_{\rm leak}$ (Assumption **[A6]**: all 6 touching neighbor strings have equal baryonic density $\rho_b^{(k)}(a) = \rho_b(a)$ on cosmological scales and identical coupling $(1 - f_{\rm leak})$),
$$\mathcal{R}_{\rm model} = N_{\rm in}(1 - f_{\rm leak}) = 6(1 - f_{\rm leak}).$$

### (c3) Present-Day Cosmic Budget Shares `[Model Ansatz | Tier 3 | Numerology]`
With $N_s = 1 + 6 + 12 = 19$ strings per strand and the leaked fraction $f_{\rm leak}$ of the 6 inner neighbors' pull added to the 12 outer strings' tension (Assumption **[A7]**: present-day share mapping),
$$\Omega_b = \frac{1}{N_s} = \frac{1}{19}, \qquad \Omega_{\rm dm} = \frac{6}{N_s}(1 - f_{\rm leak}) = \frac{6(1 - f_{\rm leak})}{19}, \qquad \Omega_{\rm de} = \frac{12 + 6 f_{\rm leak}}{N_s} = \frac{12 + 6 f_{\rm leak}}{19}.$$
**Closure Check:** For any $f_{\rm leak}$,
$$\Omega_b + \Omega_{\rm dm} + \Omega_{\rm de} = \frac{1 + 6 - 6 f_{\rm leak} + 12 + 6 f_{\rm leak}}{19} = \frac{19}{19} = 1.$$

### (c4) Pre-Registered Fixing and Testing Relation for $f_{\rm leak}$ (Test T2) `[Model Ansatz | Tier 3]`
Summing the baryon and shadow dark matter shares in (c3) gives the model's pressureless baryon-plus-CDM share today (explicitly excluding $\Omega_{\nu,0} \approx 0.00142$, denoted $\Omega_{bc}$ in `MULTIVERSE_STAGE1_EQUATIONS.md` §4 to distinguish it from total matter $\Omega_{m,{\rm tot}} = \Omega_{bc} + \Omega_{\nu,0}$):
$$\Omega_{bc} \equiv \Omega_b + \Omega_{\rm dm} = \frac{1 + 6(1 - f_{\rm leak})}{19} = \frac{7 - 6 f_{\rm leak}}{19}.$$
Inverting this linear relation for $f_{\rm leak}$ in terms of $\Omega_{bc}$ gives
$$f_{\rm leak} = 1 - \frac{19\,\Omega_{bc} - 1}{6} = \frac{7 - 19\,\Omega_{bc}}{6}, \qquad \sigma_f = \left|\frac{df_{\rm leak}}{d\Omega_{bc}}\right|\sigma_{\Omega_{bc}} = \frac{19}{6}\,\sigma_{\Omega_{bc}}.$$
*(Algebraic & sign check: at $f_{\rm leak} = 1/6$, $\Omega_{bc} = (7 - 1)/19 = 6/19 \approx 0.31579$, and $1 - (19(6/19) - 1)/6 = 1 - 5/6 = 1/6$. Exact match to (c4) in the equation sheet.)*

Substituting $f_{\rm leak}$ into (c2) gives the pre-registered T2 prediction for the dark-to-ordinary ratio:
$$\mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak}) = 19\,\Omega_{bc} - 1, \qquad \sigma_{\mathcal{R}_{\rm pred}} = 6\,\sigma_f = 19\,\sigma_{\Omega_{bc}}.$$
**Algebraic Identity Note:** Because $\Omega_{bc} = \Omega_b(1 + \mathcal{R}_{\rm true})$, $\mathcal{R}_{\rm pred} = 19\Omega_b(1 + \mathcal{R}_{\rm true}) - 1$, so $\mathcal{R}_{\rm pred} = \mathcal{R}_{\rm true}$ if and only if $\Omega_b = 1/19$. Thus Test T2 is algebraically a test of the parameter-free baryon share $\Omega_b = 1/19$ (with $f_{\rm leak}$ canceling out of $\mathcal{R}_{\rm pred} = 19\Omega_{bc} - 1$).

---

### Plain Statement of the Ratio Tension (Open Problem 10)

The leak mechanism in v1 cannot simultaneously match both the observed cosmic budget shares ($\Omega_{bc}, \Omega_{\rm de}$) and the observed dark-to-ordinary ratio ($\mathcal{R} = \omega_c/\omega_b$). The exact mathematical root of this tension is the parameter-free baryon share $\Omega_b = 1/19$:

1. **The Baryon Share Offset:** In standard cosmology, $\Omega_{bc} = \Omega_b(1 + \mathcal{R})$. Planck 2018 measures $\Omega_b = \omega_b/h^2 = 0.02237 / (0.6736)^2 = 0.04930 \pm 0.00086$, whereas the $1:6:12$ strand count fixes $\Omega_b = 1/19 = 0.052632$, which is **$6.76\%$ ($+3.87\sigma$) higher than Planck's $\Omega_b$**.
2. **Consequence When Matching the Shares ($f_{\rm leak} \approx 1/6$):** If $\Omega_{bc} \approx 0.3139$ (Planck $\Omega_b + \Omega_c$) or $\Omega_{bc} \approx 6/19 = 0.3158$ ($f_{\rm leak} = 1/6$), then because the model assigns $1/19 = 0.052632$ to baryons, dividing by $\Omega_b = 1/19$ forces
   $$\mathcal{R}_{\rm pred} = 19\,\Omega_{bc} - 1 \approx 4.964 \text{ to } 5.000,$$
   which sits **$\Delta\mathcal{R} = -0.3643$ ($5.64\sigma_{\rm Planck}$ for unrounded $5.3643 \pm 0.0646$, or $5.54\sigma_{\rm Planck}$ for rounded $5.36 \pm 0.065$) below Planck's $\mathcal{R}_{\rm Planck}$**.
3. **Consequence When Matching the Ratio ($\mathcal{R} = 5.3643$):** Conversely, reproducing $\mathcal{R}_{\rm Planck} = 5.3643$ (or rounded $5.36$) requires
   $$f_{\rm leak} = 1 - \frac{5.3643}{6} = 0.1059 \quad (\text{or } 1 - \frac{5.36}{6} = 0.1067, \text{ well below } 1/6 = 0.1667),$$
   which forces the model's baryon-plus-CDM share to be
   $$\Omega_{bc} = \frac{1 + 5.3643}{19} = 0.3350 \quad (\text{or } 0.3347 \text{ for } 5.36; \;\Omega_{\rm de} = 0.6650),$$
   missing Planck's $\Omega_{bc} = 0.3138 \pm 0.0073$ by $+2.9\sigma$.
4. **Pre-Registered Consequence for T2 (Forecast to FAIL):** Per Rule R4 and T2 ("Forbidden: $f_{\rm leak}$ has no other fix and no alternative value"), we do not propose a second fix or alter $N_s = 19$. Published DESI DR2 + CMB + SNe $w_0w_a\text{CDM}$ fits yield $\Omega_{m,{\rm tot}} \approx 0.3114 \pm 0.0057$ (`Pantheon+`) and $0.313 \pm 0.006$ (`DES-Dovekie`), so after subtracting $\Omega_{\nu,0} \approx 0.00142$, $\mathcal{R}_{\rm pred} = 19\Omega_{bc} - 1 \approx 4.89$ (`Pantheon+`) and $4.92$ (`DES-Dovekie`), and **T2 is forecast to FAIL at $\sim 3.8\sigma$ (`Pantheon+`) and $\sim 3.9\sigma$ (`DES-Dovekie`)**.

---

## Recommendation: Static Form vs. Transfer Form (Gregory Decides)

**Recommendation:** Adopt the **Static Form (Transit Efficiency, $Q = 0$)** as the primary v1 mechanism for the leak, while retaining the stable $Q_{\rm de} = \xi_e H \rho_{\rm de}$ coupling in Part 2 solely as an exploratory Tier 2 analytical comparison for the effective dark energy equation of state $w_{\rm de}^{\rm eff}(a)$.

**Reasons for Recommending the Static Form:**
1. **Direct Alignment with Pre-Registered Test T2 and Prediction P3:** T2 fixes $f_{\rm leak}$ from $\Omega_m$ in an uncoupled flat $w_0w_a\text{CDM}$ expansion fit ($\rho_{\rm dm} \propto a^{-3}$) and tests $\mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak})$ against Planck's $\omega_c/\omega_b$ (anchored at recombination, $z_* \approx 1089$). Only the Static Form preserves $\rho_{\rm dm} \propto a^{-3}$ and keeps $\mathcal{R}(z) = 6(1 - f_{\rm leak})$ invariant between $z = 1089$ and $z = 0$.
2. **Exact Validity of Compressed CMB Distance Priors $(R, \ell_A)$:** Test T2 mandates the Chen, Huang & Wang (2019) compressed CMB priors, which assume standard $\rho_{\rm dm} \propto a^{-3}$ evolution prior to recombination and consistent comoving matter density between $z_*$ and $z = 0$. The Static Form satisfies both assumptions exactly.
3. **Avoidance of Early-Universe Negative Dark Energy & Perturbation Instabilities:** The narrative-suggested coupling $Q_{\rm dm} = \xi_m H \rho_{\rm dm}$ forces $\rho_{\rm de}(a) < 0$ at $z \gtrsim 5.6$ and triggers super-horizon curvature instabilities (Valiviita et al. 2008), while the late-time stable coupling $Q_{\rm de} = \xi_e H \rho_{\rm de}$ yields $\mathcal{R}(z_*) = 6 \ne \mathcal{R}(0) = 6(1 - f_{\rm leak})$ if all of $f_{\rm leak}$ is transferred dynamically.
4. **Zero Unregistered Parameters:** Every transfer form requires at least one unregistered parameter ($\xi_m, \xi_e, \Gamma$, or $a_i$), whereas the Static Form depends solely on the pre-registered parameter $f_{\rm leak}$.
