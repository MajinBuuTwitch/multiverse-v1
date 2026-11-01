# Running List of Explicit Assumptions (`ASSUMPTIONS.md`)

Every theoretical and numerical assumption in the Ropewalk / Mandarano Model analysis is numbered sequentially here (`[A1]`, `[A2]`, …), classified by Tier, and mapped to the equations and pre-registered tests it drives.

---

## Stage 1, Part 1 Assumptions (Sections a, b, c)

- **[A1] Flat FLRW Background Geometry (`Tier 1`):**  
  *Statement:* On cosmological scales, our universe's spacetime is spatially flat ($k = 0$), homogeneous, and isotropic, described by the FLRW metric (a1). Simultaneously, cosmic time $t$ is identified with the Mandarano Model's physical preferred present ("the blade", `Tier 3` interpretation) without altering any general-relativistic metric observable.  
  *Drives:* Equations (a1)–(a5); Tests T1, T2, T6.

- **[A2] Standard Relativistic Species & Massive Neutrino Sector (`Tier 1`):**  
  *Statement:* The radiation and neutrino sectors follow standard cosmology with $T_{\rm CMB,0} = 2.7255\text{ K}$, $N_{\rm eff} = 3.044$, and a minimal normal-hierarchy neutrino mass sum $\sum m_\nu = 0.06\text{ eV}$ ($\Omega_{\nu,0} = \sum m_\nu / (93.14\,h^2\text{ eV})$), as registered in T2.  
  *Drives:* Equation (a2), sound horizon $r_s(z)$ in (a5); Tests T1, T2.

- **[A3] Negligible Present-Day Radiation/Neutrino Share in the $1:6:12$ Closure Rule (`Tier 3`):**  
  *Statement:* In the $N_s = 19$ present-day budget relations (c3)–(c4), $\Omega_b + \Omega_{\rm dm} + \Omega_{\rm de} = 1$ neglects $\Omega_{\gamma,0} \approx 5\times 10^{-5}$ and absorbs or neglects $\Omega_{\nu,0} \approx 0.0014$ when writing $\Omega_m = \Omega_b + \Omega_{\rm dm} = (7 - 6f_{\rm leak})/19$.  
  *Drives:* Equations (c3), (c4); Test T2 ($f_{\rm leak}$ extraction from $\Omega_m$).

- **[A4] Static-Form Leak as Boundary Stress-Energy Partition (`Tier 3`, Model Ansatz):**  
  *Statement:* In the Static Form of the leak (b5-S1, b5-S2), $f_{\rm leak} \in [0, 1)$ is a time-independent transit loss on the transverse gravitational pull of the 6 touching neighbor strings ($\rho_{\rm dm}(a) = 6(1 - f_{\rm leak})\rho_b(a) \propto a^{-3}$, $Q \equiv 0$), while the leaked capacity is partitioned at the strand level into bulk longitudinal outer-ring tension ($\Omega_{\rm de,0} = (12 + 6f_{\rm leak})/19$) governed by the tension equation of state $w(a)$ rather than diluting as $a^{-3}$ dust.  
  *Drives:* Equations (b5-S1), (c2)–(c4), validity of Chen, Huang & Wang (2019) compressed CMB priors $(R, \ell_A)$; Tests T2, T5.

- **[A5] Transfer-Form Initial Condition and Non-Rising Density Constraint (`Tier 3`, Alternative Model Ansatz):**  
  *Statement:* If the Transfer Form ($Q > 0$ in (b1)) is used instead of the Static Form, the shadow starts at an initial epoch $a_i$ with un-leaked ratio $\mathcal{R}(a_i) = 6$ and transfers a cumulative comoving fraction $f_{\rm leak}$ of its energy into dark energy by $a = 1$, subject to the constraint that dark energy density does not rise today ($\dot{\rho}_{\rm de}(t_0) \le 0 \iff w_{\rm de}^{\rm eff}(1) \ge -1$).  
  *Drives:* Equations (b1)–(b5); effective equation of state $w_{\rm de}^{\rm eff}(a)$ in Section (d).

- **[A6] Cosmological Homogeneity of the Six Touching Neighbor Strings (`Tier 3`, Model Ansatz):**  
  *Statement:* Averaged over cosmological volumes much larger than difference bubbles ($R_{\rm diff} \approx c\,\Delta t_{\rm split}$), each of the $N_{\rm in} = 6$ touching neighbor strings has the exact same mean baryon density as our string ($\bar{\rho}_b^{(k)}(a) = \bar{\rho}_b(a)$ for $k = 1,\dots,6$) and identical inter-string transmission $(1 - f_{\rm leak})$.  
  *Drives:* Equations (b5), (c2), (e4); Tests T2, T4a, T4b, T5.

- **[A7] Fixed Strand Geometry $N_s = 1 + 6 + 12 = 19$ and $N_r = 7 \times 19 = 133$ (`Tier 3`, Model Ansatz / Numerology):**  
  *Statement:* Histories pack in two transverse sideways dimensions as equal circles (1 central string, 6 touching neighbors, 12 outer-ring strings, $N_s = 19$), and today's cosmic budget shares equal the string counts modified by $f_{\rm leak}$ (c3).  
  *Drives:* Equations (c2)–(c4) and the Ratio Tension (Open Problem 10); Test T2.

---

## Stage 1, Part 2 Assumptions (Sections d, g, h)

- **[A8] Power-Law Dependence of Outer-Ring Tension on Strand Twist (`Tier 3`, Model Ansatz):**  
  *Statement:* The outer-ring dark energy density scales with the dimensionless strand twist $\theta(t)$ as $\rho_{\rm de}(a) = \rho_{\rm de,0}(\theta(a)/\theta_0)^n$ with $n > 0$ (where $n = 2$ is the linear-elastic rod analogy), and the strand unwinds monotonically ($\dot{\theta} < 0$).  
  *Drives:* Equations (d3)–(d5), the non-phantom bound $w(a) > -1$ for uncoupled unwinding; Test T1.

- **[A9] Candidate Unwinding Rate Laws (`Tier 3`, Model Ansatz):**  
  *Statement:* The baseline unwinding rate is constant exponential relaxation in cosmic time, $\dot{\theta} = -\Gamma_u\theta$ ($\Gamma_u > 0$, Law 1 / d4), which makes $n$ and $\Gamma_u$ degenerate in $\gamma_u \equiv n\Gamma_u/(3H_0) = 1 + w_0$ and predicts the 1D curve $w_a = -\frac{3}{2}(1+w_0)[\Omega_m + (1+w_0)(1-\Omega_m)]$. Alternative laws (Law 2 nonlinear torque $\dot{\theta} = -\Gamma_u\theta_0(\theta/\theta_0)^p$, Law 3 expansion-driven pitch $\frac{d\ln\theta}{d\ln a} = -\alpha_u a^\beta$) generalize the slope $w_a/(1+w_0)$ while remaining within the uncoupled non-phantom wedge $w_0 > -1, w_a < 0, w_0 + w_a \ge -1$.  
  *Drives:* Equations (d4), (d5); Test T1 and Open Problem 11.

- **[A10] Causal Difference Bubbles & Macroscopic Identity of Touching Neighbors (`Tier 3`, Model Ansatz):**  
  *Statement:* Splits between histories spread at most at the speed of light, $R_{\rm diff}(z; z_s) = [D_M(z_s) - D_M(z)]/(1+z)$. For the 6 touching neighbor strings in our strand, difference bubbles do not alter coarse-grained galaxy or cluster baryon distributions on scales $\gtrsim 1\text{ kpc}$, so $\rho_b^{(k)}(\mathbf{x}, t) = \rho_b(\mathbf{x}, t)$ for $k = 1,\dots,6$.  
  *Drives:* Equations (g1)–(g3), (e4); Tests T4a, T4b, T5.

- **[A11] Fixed Pre-Registered Tolerance Definitions for the Coincidence Window Diagnostic (`Tier 3`, Diagnostic Rule):**  
  *Statement:* Because the parameter-free baryon share $1/19 \approx 0.05263$ differs from Planck's $\Omega_{b,0} \approx 0.04930$ by $0.00333$ ($6.75\%$) at $a=1$, the coincidence time window $\Delta t_{\rm coinc}$ in Section (h2) is evaluated under two fixed, non-tuned tolerances declared in `PREREG.md`: Criterion H-Abs ($\max_i |\Omega_i(a) - s_i^{\rm target}| \le 0.05$) and Criterion H-Rel ($\max_i |\Omega_i(a) - s_i^{\rm target}|/s_i^{\rm target} \le 0.10$).  
  *Drives:* Equation (h2); Coincidence window report (Open Problem 5).

---

## Stage 1, Part 3 Assumptions (Sections e, f, i, and Pre-Registration)

- **[A12] Substitution of Inter-String Delay $\tau_{\rm lag}$ into Linear Velocity Extrapolation (`Tier 3`, Model Ansatz):**  
  *Statement:* By analogy with Carlip (2000)'s GR aberration cancellation for uniformly moving sources, each neighbor baryon mass element $m_j$ sources a shadow at its linearly extrapolated position $\tilde{\mathbf{x}}_j(t) = \mathbf{x}_j(t - \tau_{\rm lag}) + \mathbf{v}_j(t - \tau_{\rm lag})\tau_{\rm lag}$ with a universal crossing delay $\tau_{\rm lag} > 0$, neglecting $\mathcal{O}(\mathbf{a}\tau_{\rm lag}^2)$ acceleration corrections.  
  *Drives:* Equations (e2), (e3), (e6), (e7), (f4); Tests T4a, T4b.

- **[A13] Pre-Pericenter vs. Post-Pericenter Infall Kinematics in Merging Clusters (`Tier 3`, Dynamical Merger Modeling):**  
  *Statement:* The sign of the stellar shadow offset $\Delta\tilde{x}_S(T; \tau_{\rm lag}) = \tilde{x}_S(T) - x_S(T)$ in young mergers ($0 < T \le \tau_{\rm lag}$) depends on the infall velocity profile: under terminal pre-pericenter infall with post-pericenter deceleration (**[A13a]**), $\Delta\tilde{x}_S = +\frac{1}{2}a_{\rm dec}T^2 > 0$ (shadow strictly ahead of stars for all $0 < T \le \tau_{\rm lag}$); under symmetric harmonic core passage (**[A13b]**, $x_S(t) = \frac{v_p}{\omega_0}\sin(\omega_0 t)$), $\Delta\tilde{x}_S \approx \frac{1}{6}\omega_0^2 v_p\tau_{\rm lag}^2(3T - 2\tau_{\rm lag})$ is negative for $0 < T < \frac{2}{3}\tau_{\rm lag}$ and positive for $\frac{2}{3}\tau_{\rm lag} < T \le \tau_{\rm lag}$.  
  *Drives:* Equations (e6), (e7), $\beta(T; \tau_{\rm lag})$; Tests T4a, T4b.

- **[A14] Collisional Gas Shock / Ram-Pressure Deceleration Profile (`Tier 3`, Dynamical Merger Modeling):**  
  *Statement:* Before pericenter ($t \le t_p$), cluster gas moves with the collisionless galaxies ($x_G = x_S, v_G = v_S$). At and after pericenter ($T = t - t_p > 0$), ram pressure decelerates the gas either via an impulsive shock drop $\Delta v_{\rm ram}$ at $T = 0$ (**[A14a]**, giving $\tilde{x}_G = \tilde{x}_S + \delta_{SG}$ for $T > \tau_{\rm lag}$) or continuous deceleration $a_{\rm ram}$ (**[A14b]**, giving $\tilde{x}_G = \tilde{x}_S + \delta_{SG}(1 - \tau_{\rm lag}^2/T^2)$ for $T > \tau_{\rm lag}$).  
  *Drives:* Equations (e6), (e7), $\beta(T; \tau_{\rm lag})$ age-cutoff step at $T = \tau_{\rm lag}$; Test T4b.

- **[A15] Isolated Galaxy Approximation, Spherical Circular Speed, and Fixed SPARC Mass-to-Light Ratios (`Tier 1 & 3`, Pre-Registered T5 Model):**  
  *Statement:* In Test T5, each SPARC galaxy is modeled as isolated (except NGC 1052-DF2 in T5c, which includes the NGC 1052 group baryons), with spherical circular velocity $v_c^2(r) = v_{\rm bar}^2(r) + G M_{\rm sh}(< r)/r$ and fixed $3.6\,\mu\text{m}$ mass-to-light ratios $\Upsilon_{\rm disk} = 0.5\,M_\odot/L_\odot$ and $\Upsilon_{\rm bul} = 0.7\,M_\odot/L_\odot$. Because the 3D Gaussian kernel $K_\sigma$ is normalized and diffusive, isolated galaxies with outward-decreasing baryon density obey the strict saturation cap $g_{\rm obs}(r)/g_{\rm bar}(r) \le 1 + 6(1 - f_{\rm leak})$ at all radii $r > 0$.  
  *Drives:* Equations (f1), (f3); Tests T5-A, T5-B, T5c.

- **[A16] Stationarity of Axisymmetric Rotating Disks Over $\tau_{\rm lag}$ (`Tier 3`, Model Ansatz):**  
  *Statement:* For stars and gas on bound circular orbits in a stationary axisymmetric galactic disk ($\partial\rho_b/\partial t = 0$ in the galaxy center-of-mass frame, where orbital periods $2\pi r/v_c \sim 50\text{–}100\text{ Myr} \lesssim \tau_{\rm lag}$), linear tangent extrapolation (f4) violates Carlip (2000)'s uniform-motion condition; the coarse-grained scalar baryon density in the galaxy rest frame is stationary ($\tilde{\rho}_b(\mathbf{x}) = \rho_b(\mathbf{x})$), as registered in Test T5.  
  *Drives:* Equations (f3), (f4); Tests T5-A, T5-B.

- **[A17] Far-String Contribution $\epsilon_{\rm far}$ as an Unclustered Background Shadow Component (`Tier 3`, Exploratory Proposal for v2):**  
  *Statement:* Strings beyond the 6 touching neighbors contribute a fraction $\epsilon_{\rm far} \equiv \Omega_{\rm dm,far}/\Omega_{\rm dm} \ll 1$ with macroscopic refraction width $\sigma_{\rm far} \gg 10\text{ Mpc}$, which gravitates in the homogeneous background $H(a)$ but does not cluster on galaxy/cluster scales ($k \gg \sigma_{\rm far}^{-1}$), suppressing linear structure growth $f\sigma_8(z)$ and $S_8$. Not registered or used in v1 tests.  
  *Drives:* Section (i) $\epsilon_{\rm far}$ proposal (Prediction P6).

- **[A18] Uncorrelated Gaussian Error Propagation for $\mathcal{R}_{\rm Planck}$ in Test T2 (`Tier 1/3`, Pre-Registered T2 Rule):**  
  *Statement:* As locked in `MULTIVERSE_TESTS_v1.md` (T2), $\mathcal{R}_{\rm Planck} = \omega_c/\omega_b = 0.1200 / 0.02237 = 5.36 \pm 0.065$ propagates Planck 2018 `TT,TE,EE+lowE+lensing` uncertainties on $\omega_c$ and $\omega_b$ in quadrature ignoring their posterior covariance, and combines with $6\sigma_f = 19\sigma_{\Omega_m}$ via $\sigma_{\rm comb} = \sqrt{(19\sigma_{\Omega_m})^2 + 0.065^2}$.  
  *Drives:* Equation (c4); Test T2 outcome.

- **[A19] Full-Sample SPARC Primary Split and Quality-Cut Benchmark (`Tier 3`, Pre-Registered G8 Resolution):**  
  *Statement:* Because `MULTIVERSE_TESTS_v1.md` (T5) specifies ordering SPARC galaxies alphabetically without a quality filter, the primary T5-A/T5-B evaluation uses all 175 SPARC galaxies in `MassModels_Lelli2016c.mrt` sorted by galaxy name (odd = 88 training, even = 87 test), while the McGaugh et al. (2016) quality-cut sample ($Q \in \{1, 2\}, i \ge 30^\circ$) is evaluated alongside for the RAR benchmark.  
  *Drives:* Tests T5-A, T5-B.

- **[A20] HEALPix $N_{\rm side} = 1$ Coordinate Convention for Test T6 (`Tier 3`, Pre-Registered G8 Resolution):**  
  *Statement:* In Test T6, the 12 equal-area sky regions of the HEALPix $N_{\rm side} = 1$ grid are defined in standard Galactic coordinates $(l, b)$ using the HEALPix `RING` ordering scheme (with Equatorial RA/Dec `RING` reported as a secondary check), evaluated on Pantheon+ Hubble-flow supernovae ($0.023 \le z_{\rm HD} \le 0.15$, non-calibrators) with the full Pantheon+ covariance matrix.  
  *Drives:* Equation (g4); Test T6 outcome.
