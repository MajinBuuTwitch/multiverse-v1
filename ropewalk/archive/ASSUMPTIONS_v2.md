# Running List of Explicit Assumptions (`ASSUMPTIONS.md`)

Every theoretical and numerical assumption in the Ropewalk / Mandarano Model analysis is numbered sequentially here (`[A1]` through `[A20]`), classified by Tier, and mapped to the equations and pre-registered tests it drives. Updated post-cold-review (`REVIEW_COLD.md`).

---

## Stage 1, Part 1 Assumptions (Sections a, b, c)

- **[A1] Flat FLRW Background Geometry (`Tier 1`):**  
  *Statement:* On cosmological scales, our universe's spacetime is spatially flat ($k = 0$), homogeneous, and isotropic, described by the FLRW metric (a1). Simultaneously, cosmic time $t$ is identified with the Mandarano Model's physical preferred present ("the blade", `Tier 3` interpretation) without altering any general-relativistic metric observable.  
  *Drives:* Equations (a1)–(a5); Tests T1-L1, T1-Sign, T2, T6.

- **[A2] Standard Relativistic Species & Massive Neutrino Sector (`Tier 1`):**  
  *Statement:* The radiation and neutrino sectors follow standard cosmology with $T_{\rm CMB,0} = 2.7255\text{ K}$, $N_{\rm eff} = 3.044$, and a minimal normal-hierarchy neutrino mass sum $\sum m_\nu = 0.06\text{ eV}$ ($\Omega_{\nu,0} = \sum m_\nu / (93.14\,h^2\text{ eV})$), modeled with one massive eigenstate and two massless eigenstates via the exact Fermi–Dirac phase-space integral $f_\nu(a)$.  
  *Drives:* Equation (a2), sound horizon $r_s(z)$ and fitting formulas $z_*, z_d$ in (a5); Tests T1-L1, T1-Sign, T2.

- **[A3] Explicit Exclusion of $\Omega_{\nu,0}$ from the Three-Component $1:6:12$ Closure Rule (`Tier 3`, Resolving M1 & m7):**  
  *Statement:* In the $N_s = 19$ present-day budget relations (c3)–(c4), the pressureless baryon-plus-cold-dark-matter share is explicitly defined as $\Omega_{bc} \equiv \Omega_b + \Omega_{\rm dm} = \Omega_{m,{\rm tot}} - \Omega_{\nu,0} = (7 - 6f_{\rm leak})/19$, so that massive neutrinos ($\Omega_{\nu,0} \approx 0.00142$, which shift $19\Omega_m$ by $+0.027 \approx 0.42\sigma_{\rm Planck}$) never bias $f_{\rm leak}$ or $\mathcal{R}_{\rm pred} = 19\Omega_{bc} - 1$.  
  *Drives:* Equations (c3), (c4); Tests T2-A, T2-B.

- **[A4] Static-Form Leak as Boundary Stress-Energy Partition (`Tier 3`, Model Ansatz):**  
  *Statement:* In the locked v1 Static Form of the leak (b5-S), $f_{\rm leak} \in [0, 1)$ is a time-independent transit loss on the transverse gravitational pull of the 6 touching neighbor strings ($\rho_{\rm dm}(a) = 6(1 - f_{\rm leak})\rho_b(a) \propto a^{-3}$, $Q \equiv 0$), while the leaked capacity is partitioned at the strand level into bulk longitudinal outer-ring tension ($\Omega_{\rm de,0} = (12 + 6f_{\rm leak})/19$) governed by the tension equation of state $w(a)$ rather than diluting as $a^{-3}$ dust.  
  *Drives:* Equations (b5-S), (c2)–(c4), validity of Chen, Huang & Wang (2019) compressed CMB priors $(R, \ell_A)$; Tests T2, T5.

- **[A5] Transfer-Form Initial Condition and Non-Rising Density Constraint (`Tier 3`, Exploratory Alternative):**  
  *Statement:* If the Transfer Form ($Q > 0$ in (b1)) is used instead of the Static Form, the shadow starts at an initial epoch $a_i$ with un-leaked ratio $\mathcal{R}(a_i) = 6$ and transfers a cumulative comoving fraction $f_{\rm leak}$ of its energy into dark energy by $a = 1$, subject to the constraint that dark energy density does not rise today ($\dot{\rho}_{\rm de}(t_0) \le 0 \iff w_{\rm de}^{\rm eff}(1) \ge -1$).  
  *Drives:* Equations (b1)–(b5-T); exploratory effective equation of state $w_{\rm de}^{\rm eff}(a)$ in Section 5.4 `(d-Exp)`.

- **[A6] Cosmological Homogeneity of the Six Touching Neighbor Strings (`Tier 3`, Model Ansatz):**  
  *Statement:* Averaged over cosmological volumes much larger than difference bubbles ($R_{\rm diff} \approx c\,\Delta t_{\rm split}$), each of the $N_{\rm in} = 6$ touching neighbor strings has the exact same mean baryon density as our string ($\bar{\rho}_b^{(k)}(a) = \bar{\rho}_b(a)$ for $k = 1,\dots,6$) and identical inter-string transmission $(1 - f_{\rm leak})$.  
  *Drives:* Equations (b5), (c2), (e4); Tests T2, T4b, T5.

- **[A7] Fixed Strand Geometry $N_s = 1 + 6 + 12 = 19$ and $N_r = 7 \times 19 = 133$ (`Tier 3`, Model Ansatz / Numerology, Resolving M1 & M2):**  
  *Statement:* Histories pack in two transverse sideways dimensions as equal circles (1 central string, 6 touching neighbors, 12 outer-ring strings, $N_s = 19$), and today's cosmic budget shares equal the string counts modified by $f_{\rm leak}$ (c3). This parameter-free assumption fixes $\Omega_b = 1/19 = 0.052632$ and $H_0^{\rm pred} = 100\sqrt{19\omega_b}\text{ km s}^{-1}\text{ Mpc}^{-1}$, which are tested directly in **T2, T2-N1, and T2-N2**.  
  *Drives:* Equations (c2)–(c4) and the Ratio Tension (Open Problem 10); Tests T2-A, T2-B, T2-N1, T2-N2.

---

## Stage 1, Part 2 Assumptions (Sections d, g, h)

- **[A8] Power-Law Dependence of Outer-Ring Tension on Strand Twist (`Tier 3`, Model Ansatz):**  
  *Statement:* The outer-ring dark energy density scales with the dimensionless strand twist $\theta(t)$ as $\rho_{\rm de}(a) = \rho_{\rm de,0}(\theta(a)/\theta_0)^n$ with $n > 0$ (where $n = 2$ is the linear-elastic rod analogy), and the strand unwinds monotonically ($\dot{\theta} < 0$).  
  *Drives:* Equations (d3)–(d5), the non-phantom bound $w(a) > -1$ for uncoupled unwinding; Tests T1-L1, T1-Sign.

- **[A9] Baseline Constant Cosmic-Time Unwinding Rate Law (`Tier 3`, Model Ansatz, Resolving B4 & M13):**  
  *Statement:* The baseline unwinding rate is constant exponential relaxation in cosmic time, $\dot{\theta} = -\Gamma_u\theta$ ($\Gamma_u \ge 0$, Law 1 / d4), which makes $n$ and $\Gamma_u$ degenerate in $\gamma_u \equiv n\Gamma_u/(3H_0) = 1 + w_0 \ge 0$, yields the exact 1-parameter dark-energy equation of state $w(a) = -1 + \gamma_u/E(a)$, and predicts the 1D curve $w_a = -\frac{3}{2}\gamma_u[\Omega_m + \gamma_u(1-\Omega_m)]$, registered directly as **Primary Test T1-L1**.  
  *Drives:* Equations (d4), (d5); Primary Test T1-L1 and Open Problem 11.

- **[A10] Causal Difference Bubbles & Macroscopic Identity of Touching Neighbors (`Tier 3`, Model Ansatz):**  
  *Statement:* Splits between histories spread at most at the speed of light, $R_{\rm diff}(z; z_s) = [D_M(z_s) - D_M(z)]/(1+z)$. For the 6 touching neighbor strings in our strand, difference bubbles do not alter coarse-grained galaxy or cluster baryon distributions on scales $\gtrsim 1\text{ kpc}$, so $\rho_b^{(k)}(\mathbf{x}, t) = \rho_b(\mathbf{x}, t)$ for $k = 1,\dots,6$.  
  *Drives:* Equations (g1)–(g3), (e4); Tests T4b, T5, and Exploratory T4a.

- **[A11] Fixed Pre-Registered Tolerance Definitions for the Coincidence Window Diagnostic (`Tier 3`, Diagnostic Rule):**  
  *Statement:* Because the parameter-free baryon share $1/19 \approx 0.052632$ differs from Planck's $\Omega_{b,0} \approx 0.04930$ by $0.00333$ ($6.76\%$) at $a=1$, the coincidence time window $\Delta t_{\rm coinc}$ in Section 8.2 (h2) is evaluated under two fixed, non-tuned tolerances declared in `PREREG.md`: Criterion H-Abs ($\max_i |\Omega_i(a) - s_i^{\rm target}| \le 0.05$) and Criterion H-Rel ($\max_i |\Omega_i(a) - s_i^{\rm target}|/s_i^{\rm target} \le 0.10$).  
  *Drives:* Equation (h2); Coincidence window report (Open Problem 5).

---

## Stage 1, Part 3 Assumptions (Sections e, f, i, and Pre-Registration)

- **[A12] Unified Coarse-Grained Component Velocity Extrapolation Over $\tau_{\rm lag}$ (`Tier 3`, Model Ansatz, Resolving M5):**  
  *Statement:* Because the inter-string gravity kernel $K_\sigma$ smooths over physical scale $\sigma_{\rm ref}$, linear velocity extrapolation over the universal crossing delay $\tau_{\rm lag} > 0$ acts on the **center-of-mass bulk velocity $\mathbf{V}_{{\rm bulk},c}(t - \tau_{\rm lag})$ of each macroscopically coherent baryonic component $c$** smoothed on scale $\sigma_{\rm ref}$ ($\tilde{\rho}_{b,c}(\mathbf{y}, t) = \rho_{b,c}(\mathbf{y} - \mathbf{V}_{{\rm bulk},c}(t - \tau_{\rm lag})\tau_{\rm lag}, t - \tau_{\rm lag})$), rather than on internal thermal, virial, or bound circular velocities that violate uniform motion over $\tau_{\rm lag}$.  
  *Drives:* Equations (e2)–(e7), (f4); Tests T4b, T5, and Exploratory T4a.

- **[A13b] Symmetric Harmonic Core-Passage Trajectory in Merging Clusters (`Tier 3`, Selected Physical Merger Model, Resolving B3):**  
  *Statement:* Because collisionless galaxies move in a conservative cluster gravitational potential that accelerates them during pre-pericenter infall ($\ddot{x}_S > 0$ for $t' < 0$) and decelerates them after pericenter ($\ddot{x}_S < 0$ for $t' > 0$), **Model A13b ($x_S(t) = \frac{v_p}{\omega_0}\sin(\omega_0 t)$) is selected over A13a**. Under A13b, $\Delta\tilde{x}_S(T; \tau_{\rm lag}) \approx \frac{1}{6}\omega_0^2 v_p\tau_{\rm lag}^2(3T - 2\tau_{\rm lag})$ is negative (shadow behind stars) for $0 < T < \frac{2}{3}\tau_{\rm lag}$ and positive (shadow ahead of stars) only for $\frac{2}{3}\tau_{\rm lag} < T \le \tau_{\rm lag}$.  
  *Drives:* Equations (e6), (e7), $\beta(T; \tau_{\rm lag})$; Exploratory Test T4a and Test T4b.

- **[A14] Collisional Gas Shock / Ram-Pressure Deceleration Profile (`Tier 3`, Dynamical Merger Modeling, Resolving m14):**  
  *Statement:* Before pericenter ($t \le t_p$), cluster gas moves with the collisionless galaxies ($x_G = x_S, v_G = v_S$). At and after pericenter ($T = t - t_p > 0$), ram pressure decelerates the gas via an impulsive bow-shock drop $\Delta v_{\rm ram}$ at $T = 0$ with either shared post-shock gravitational deceleration $\ddot{x}_G = \ddot{x}_S$ (**[A14a-grav]**, $\tilde{x}_G = \tilde{x}_S + \delta_{SG}$ for $T > \tau_{\rm lag}$) or hydrostatic coasting $\ddot{x}_G = 0$ (**[A14a-coast]**, $\tilde{x}_G = x_G$ for $T > \tau_{\rm lag}$), or via continuous drag $a_{\rm ram}$ (**[A14b]**).  
  *Drives:* Equations (e6), (e7), $\beta(T; \tau_{\rm lag})$ age-cutoff step at $T = \tau_{\rm lag}$; Test T4b.

- **[A15] Isolated Galaxy Approximation, Monotonic Baryon Shell Construction, and Fixed SPARC Mass-to-Light Ratios (`Tier 1 & 3`, Pre-Registered T5 Model, Resolving M3 & M4):**  
  *Statement:* In Test T5, each SPARC galaxy is modeled as isolated (except NGC 1052-DF2 in T5c), with spherical circular velocity $v_c^2(r) = v_{\rm bar}^2(r) + G M_{\rm sh}(< r)/r$, fixed $3.6\,\mu\text{m}$ mass-to-light ratios $\Upsilon_{\rm disk} = 0.5\,M_\odot/L_\odot$ and $\Upsilon_{\rm bul} = 0.7\,M_\odot/L_\odot$, and non-negative radial shell masses $dM_b(r') \ge 0$ continued exponentially from $r_{\max}$ to $r_{\max} + 5\sigma_{\rm ref}$. Because the 3D Gaussian kernel $K_\sigma$ is normalized and diffusive, isolated galaxies obey the strict saturation cap $g_{\rm obs}(r)/g_{\rm bar}(r) \le 1 + 6(1 - f_{\rm leak})$ at all radii $r > 0$, making a full T5 PASS very unlikely.  
  *Drives:* Equations (f1), (f3); Tests T5-A, T5-B, T5c.

- **[A16] Rest-Frame Stationarity of Isolated Galactic Disks Under `[A12]` (`Tier 3`, Model Ansatz, Resolving M5):**  
  *Statement:* Under the unified coarse-grained component velocity extrapolation rule `[A12]`, an isolated galaxy in its center-of-mass rest frame has $\mathbf{V}_{\rm bulk} = \mathbf{0}$ and $\partial\rho_b/\partial t = 0$, so its coarse-grained scalar baryon density is unshifted ($\tilde{\rho}_b(\mathbf{x}) = \rho_b(\mathbf{x})$), as registered in Test T5.  
  *Drives:* Equations (f3), (f4); Tests T5-A, T5-B.

- **[A17] Far-String Contribution $\epsilon_{\rm far}$ as an Unclustered Background Shadow Component (`Tier 3`, Exploratory Proposal for v2, Resolving m11 & m13):**  
  *Statement:* Strings beyond the 6 touching neighbors contribute a fraction $\epsilon_{\rm far} \equiv \Omega_{\rm dm,far}/\Omega_{\rm dm} \ll 1$ with macroscopic refraction width $\sigma_{\rm far} \gg 10\text{ Mpc}$, which gravitates in the homogeneous background $H(a)$ but does not cluster on galaxy/cluster scales ($k \gg \sigma_{\rm far}^{-1}$), suppressing linear structure growth $f\sigma_8(z)$ and $S_8$ by $-3.80\,\epsilon_{\rm far}$ to $-3.94\,\epsilon_{\rm far}$. Not registered or used in v1 tests.  
  *Drives:* Section 8.3 `(i-Exp)` $\epsilon_{\rm far}$ proposal (Prediction P6).

- **[A18] Error Propagation and Overlap Correlation for $\mathcal{R}_{\rm Planck}$ in Test T2 (`Tier 1/3`, Pre-Registered T2 Rule, Resolving M1):**  
  *Statement:* As locked in `MULTIVERSE_TESTS_v1.md` (T2), $\mathcal{R}_{\rm Planck} = \omega_c/\omega_b = 0.1200 / 0.02237 = 5.36 \pm 0.065$, and T2 is evaluated both with the locked uncorrelated formula $\sigma_{\rm comb} = \sqrt{(19\sigma_{\Omega_{bc}})^2 + 0.065^2}$ and with the exact Planck $(R, \ell_A)$–$(\omega_c/\omega_b)$ overlap correlation $\rho_{\rm overlap}$ included in $\sigma_{\rm comb}^2 = (19\sigma_{\Omega_{bc}})^2 + \sigma_{\rm Planck}^2 - 2\rho_{\rm overlap}(19\sigma_{\Omega_{bc}})\sigma_{\rm Planck}$.  
  *Drives:* Equation (c4); Test T2 outcome.

- **[A19] Byte-Wise ASCII SPARC Primary Split and Quality-Cut Benchmark (`Tier 3`, Pre-Registered G8 Resolution, Resolving M4):**  
  *Statement:* The primary T5-A/T5-B evaluation uses all 175 SPARC galaxies in `MassModels_Lelli2016c.mrt` sorted by Python byte-wise `sorted()` on the raw stripped SPARC galaxy identifier string (odd = 88 training, even = 87 test), while the McGaugh et al. (2016) quality-cut sample ($Q \in \{1, 2\}, i \ge 30^\circ$) is evaluated alongside for the RAR benchmark.  
  *Drives:* Tests T5-A, T5-B.

- **[A20] HEALPix $N_{\rm side} = 1$ Coordinate Convention & Minimum Pixel Occupancy for Test T6 (`Tier 3`, Pre-Registered G8 Resolution, Resolving M14):**  
  *Statement:* In Test T6, the 12 equal-area sky regions of the HEALPix $N_{\rm side} = 1$ grid are defined in Galactic coordinates $(l, b)$ using `RING` ordering on Pantheon+ Hubble-flow supernovae ($0.023 \le z_{\rm HD} \le 0.15$, non-calibrators) with minimum pixel count $N_{{\rm SN},i} \ge 10$ (merging sparse low-$|b|$ pixels into adjacent pixels to give $N_{\rm pix}$ well-sampled regions), GLS mean $\bar{H}_0$, cosmic-variance floor in the null covariance, and both $z_{\rm HD}$ and $z_{\rm CMB}$ evaluated.  
  *Drives:* Equation (g4); Test T6 outcome.
