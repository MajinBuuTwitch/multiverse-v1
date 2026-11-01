# Stage 1, Part 3: Theoretical Derivations for Sections (e), (f), and (i)

**Date:** 2026-10-30  
**Workspace:** `D:\Argon_Code\Ropewalk`  
**Package Version:** 1.0.1  

---

## Section (e): The Shadow in Merging Galaxy Clusters (Lag, Carried Motion, and Dynamical Merger Model)

**Section Tier:** **Tier 1** for Newtonian Poisson gravity and GR aberration cancellation (e1, e2); **Tier 2** for nonlocal integral-kernel gravity precedent (Hehl & Mashhoon 2009); **Tier 3** for the inter-string shadow ansatz and merger offset model (e3–e7).

### (e1) Weak-Field Poisson Equation with Shadow Density `[Established | Tier 1]`
In the weak-field Newtonian regime ($|\Phi|/c^2 \ll 1, v/c \ll 1$), the gravitational potential $\Phi(\mathbf{x}, t)$ is sourced by the sum of ordinary baryonic density $\rho_b(\mathbf{x}, t)$ and the shadow density $\rho_{\rm sh}(\mathbf{x}, t)$:
$$\nabla^2\Phi(\mathbf{x}, t) = 4\pi G\left[\rho_b(\mathbf{x}, t) + \rho_{\rm sh}(\mathbf{x}, t)\right].$$

### (e2) Coarse-Grained Component Velocity Extrapolation (Carlip Analogy) `[Established GR Analogy (Tier 1) / Model Ansatz Substitution (Tier 3)]`
In general relativity, the field of a uniformly moving mass at retarded time $t_{\rm ret} = t - r/c$ points toward its linearly extrapolated instantaneous position $\mathbf{x}(t_{\rm ret}) + \mathbf{v}(t_{\rm ret})(t - t_{\rm ret})$ up to acceleration terms of order $\mathcal{O}(\mathbf{a}(t - t_{\rm ret})^2)$ (Carlip 2000). Under the unified coarse-grained extrapolation rule (Assumptions **[A12]** and **[A16]**, resolving Review Finding M5), because the inter-string refraction kernel $K_\sigma$ smooths over physical width $\sigma_{\rm ref}$, linear velocity extrapolation over the universal crossing delay $\tau_{\rm lag} > 0$ acts on the **center-of-mass bulk velocity $\mathbf{V}_{{\rm bulk},c}(t - \tau_{\rm lag})$ of each macroscopically coherent baryonic component $c$** (smoothed on scale $\sigma_{\rm ref}$), rather than on random thermal or bound internal virial/orbital velocities ($\sigma_v \sim 1000\text{ km s}^{-1}$ in clusters or $v_c \sim 200\text{ km s}^{-1}$ in galaxies, which violate uniform motion over $\tau_{\rm lag}$):
$$\tilde{\mathbf{X}}_c^{(k)}(t) \equiv \mathbf{X}_c^{(k)}(t - \tau_{\rm lag}) + \mathbf{V}_{{\rm bulk},c}^{(k)}(t - \tau_{\rm lag})\,\tau_{\rm lag}.$$

### (e3 & e4) Six-Neighbor Convolved Shadow Density `[Model Ansatz | Tier 3]`
Summing over the $k = 1,\dots,6$ touching neighbor strings with static transit efficiency $(1 - f_{\rm leak})$ and applying the locality identity $\rho_{b,c}^{(k)}(\mathbf{x}, t) = \rho_{b,c}(\mathbf{x}, t)$ (Assumption **[A10]**) gives one single rule applied identically to galaxy clusters and isolated galaxies:
$$\rho_{\rm sh}(\mathbf{x}, t) = 6(1 - f_{\rm leak})\int_{\mathbb{R}^3} d^3y\;K_\sigma(\mathbf{x} - \mathbf{y})\,\tilde{\rho}_b(\mathbf{y}, t),$$
$$\tilde{\rho}_b(\mathbf{y}, t) = \sum_{c} \rho_{b,c}\!\left(\mathbf{y} - \mathbf{V}_{{\rm bulk},c}(t - \tau_{\rm lag})\,\tau_{\rm lag},\; t - \tau_{\rm lag}\right).$$
- **Cluster Merger Application:** Each colliding subcluster component $c \in \{S, G\}$ has bulk velocity $\mathbf{V}_{{\rm bulk},c}(t - \tau_{\rm lag})$, so its shadow centroid is shifted to $\tilde{\mathbf{X}}_c(t) = \mathbf{X}_c(t - \tau_{\rm lag}) + \mathbf{V}_{{\rm bulk},c}(t - \tau_{\rm lag})\tau_{\rm lag}$ without an unphysical $\sigma_v\tau_{\rm lag} \approx 150\text{–}600\text{ kpc}$ internal velocity-dispersion blow-up.
- **Isolated Galaxy Application:** In the galaxy's center-of-mass rest frame, $\mathbf{V}_{\rm bulk} = \mathbf{0}$ and $\rho_b(\mathbf{y}, t - \tau_{\rm lag}) = \rho_b(\mathbf{y})$, yielding $\tilde{\rho}_b(\mathbf{y}) = \rho_b(\mathbf{y})$ identically.

### (e5) Normalized 3D Gaussian Refraction Kernel `[Model Ansatz | Tier 3]`
The default refraction kernel is a normalized 3D isotropic Gaussian of physical width $\sigma_{\rm ref} > 0$:
$$K_\sigma(\mathbf{r}) = \left(2\pi\sigma_{\rm ref}^2\right)^{-3/2}\exp\!\left(-\frac{|\mathbf{r}|^2}{2\sigma_{\rm ref}^2}\right), \qquad \int_{\mathbb{R}^3} K_\sigma(\mathbf{r})\,d^3r = 1.$$
By normalization, the total integrated shadow mass of a system of baryonic mass $M_b$ is $M_{\rm sh,tot} = 6(1 - f_{\rm leak})M_b \equiv \mathcal{R}\,M_b$.

---

### (e6 & e7) Complete Derivation of the 1D Dynamical Merger Offset Model and $\beta(T; \tau_{\rm lag})$

Consider a subcluster passing through pericenter of a main cluster at $t = t_p$ ($x = 0$) along the 1D merger axis $+x$ with pericenter speed $v_p > 0$. Let $T \equiv t - t_p \ge 0$ denote the time elapsed since first pericenter. The subcluster comprises collisionless stars/galaxies ($S$, mass $M_S$, baryon fraction $f_S = \frac{M_S}{M_S + M_G} = 1 - f_G$) and collisional X-ray gas ($G$, mass $M_G$, baryon fraction $f_G = \frac{M_G}{M_S + M_G} \approx 0.80\text{–}0.88$).

#### 1. Centroids and Unified Offset Sign Convention (Resolving B2) `[Model Ansatz | Tier 3]`
Because convolution with the parity-symmetric kernel $K_\sigma(-\mathbf{r}) = K_\sigma(\mathbf{r})$ preserves centroids, the shadow of component $c \in \{S, G\}$ has centroid
$$\tilde{x}_c(T; \tau_{\rm lag}) = x_c(T - \tau_{\rm lag}) + v_c(T - \tau_{\rm lag})\,\tau_{\rm lag}.$$
With $\mathcal{R} \equiv 6(1 - f_{\rm leak})$, the total gravitating mass centroid $x_I(T)$ is
$$x_I(T) = \frac{f_S\,x_S(T) + f_G\,x_G(T) + \mathcal{R}\left[f_S\,\tilde{x}_S(T; \tau_{\rm lag}) + f_G\,\tilde{x}_G(T; \tau_{\rm lag})\right]}{1 + \mathcal{R}}.$$
In 2D/3D sky coordinates, let $\hat{\mathbf{s}}_{G\to S} \equiv \frac{\mathbf{x}_S - \mathbf{x}_G}{|\mathbf{x}_S - \mathbf{x}_G|}$ denote the unit vector pointing from the X-ray gas peak $\mathbf{x}_G$ to the galaxy centroid $\mathbf{x}_S$ (which equals $+\hat{\mathbf{x}}$ in 1D where $x_S(T) > x_G(T)$ after pericenter). In the convention of `MULTIVERSE_EQUATION_SHEET_v1.md` (e7) and Harvey et al. (2015), where $\delta_{SG}(T) \equiv x_G(T) - x_S(T) = -|\delta_{SG}(T)| < 0$ (gas lags behind stars), $\delta_{SI}(T) \equiv x_I(T) - x_S(T)$, and $\beta(T) \equiv \frac{\delta_{SI}(T)}{\delta_{SG}(T)}$, the projected offset along $\hat{\mathbf{s}}_{G\to S}$ is defined identically everywhere as:
$$\Delta_{SI}^{\parallel}(T) \equiv \left(\mathbf{x}_I(T) - \mathbf{x}_S(T)\right)\cdot\hat{\mathbf{s}}_{G\to S} = x_I(T) - x_S(T) = \delta_{SI}(T) = \delta_{SG}(T)\,\beta(T) = -\left|\delta_{SG}(T)\right|\,\beta(T).$$
Thus **dark mass sitting ahead of the stars (away from the gas)** corresponds to $\Delta_{SI}^{\parallel}(T) > 0 \Longleftrightarrow \delta_{SI}(T) > 0 \Longleftrightarrow \beta(T) < 0$.

#### 2. Exact Taylor–Integral Identity for Linear Extrapolation `[Established Math | Tier 1]`
For any twice-differentiable trajectory $x_c(t)$, integration by parts gives the exact displacement between the linearly extrapolated shadow centroid $\tilde{x}_c(T; \tau_{\rm lag})$ and the true instantaneous position $x_c(T)$:
$$\Delta\tilde{x}_c(T; \tau_{\rm lag}) \equiv \tilde{x}_c(T; \tau_{\rm lag}) - x_c(T) = -\int_{T - \tau_{\rm lag}}^{T} (T - t')\,\ddot{x}_c(t')\,dt'.$$

#### 3. Physical Selection of Model A13b (Symmetric Harmonic Core Passage, Resolving B3) `[Established Dynamics / Model Ansatz Application | Tier 1 & 3]`
In a softened cluster gravitational potential $\Phi_{\rm cl}(x) = -\frac{GM_{\rm main}}{\sqrt{x^2 + R_c^2}}$ with core radius $R_c$ and core frequency $\omega_0 \equiv \sqrt{\frac{GM_{\rm main}}{R_c^3}} \sim \frac{v_p}{R_c}$, the gravitational acceleration is $a_{\rm grav}(x) = -\frac{GM_{\rm main}\,x}{(x^2 + R_c^2)^{3/2}} \approx -\omega_0^2 x$ for $|x| \lesssim R_c$. Notice the mandatory sign reversal across pericenter ($x = 0$):
- **Pre-pericenter infall ($t' < 0, x < 0$):** $a_{\rm grav} > 0$ (the conservative gravitational potential accelerates the infalling subcluster toward $x = 0$, so $v_S(t' < 0) < v_p$, reaching maximum speed $v_p$ at pericenter $t' = 0$).
- **Post-pericenter outbound ($t' > 0, x > 0$):** $a_{\rm grav} < 0$ (the same gravitational potential decelerates the outbound subcluster).

**Pre-Registered Choice (A13b Selected Over A13a per Finding B3):**  
Because collisionless galaxies move solely under conservative gravity, assuming constant speed before pericenter ($\ddot{x}_S(t' < 0) = 0$, Model A13a) violates conservation of mechanical energy in a potential well whose gradient decelerates the outbound subcluster after pericenter. Therefore, **Model A13b (Symmetric Harmonic Core Passage, $x_S(t) = \frac{v_p}{\omega_0}\sin(\omega_0 t)$)** is selected as the physical v1 merger trajectory model:
$$\Delta\tilde{x}_S^{\rm (A13b)}(T; \tau_{\rm lag}) = \frac{v_p}{\omega_0}\left[\sin\!\left(\omega_0(T - \tau_{\rm lag})\right) + \omega_0\tau_{\rm lag}\cos\!\left(\omega_0(T - \tau_{\rm lag})\right) - \sin(\omega_0 T)\right] = \frac{1}{6}\omega_0^2 v_p\,\tau_{\rm lag}^2\left(3T - 2\tau_{\rm lag}\right) + \mathcal{O}(\omega_0^4\tau_{\rm lag}^5).$$
- **Sign Consequence of A13b:** Because $v_S(T - \tau_{\rm lag}) < v_p$ during pre-pericenter infall, $\Delta\tilde{x}_S^{\rm (A13b)}(T; \tau_{\rm lag})$ is **negative (behind the stars, toward the gas)** for $0 < T < \frac{2}{3}\tau_{\rm lag}$ and becomes **positive (ahead of the stars, away from the gas)** only for $\frac{2}{3}\tau_{\rm lag} < T \le \tau_{\rm lag}$ (and remains positive for $\tau_{\rm lag} < T < \frac{\pi}{\omega_0}$).
- *(Model A13a, where $\Delta\tilde{x}_S^{\rm (A13a)} = +\frac{1}{2}a_{\rm dec}T^2$ for $0 < T \le \tau_{\rm lag}$ and $+\frac{1}{2}a_{\rm dec}\tau_{\rm lag}^2$ for $T > \tau_{\rm lag}$, is retained solely as a pedagogical contrast to show why ignoring pre-pericenter acceleration artificially guarantees $\Delta\tilde{x}_S > 0$.)*

#### 4. Gas Trajectory, Shock/Ram-Pressure Deceleration, and Explicit Formula for $\beta(T; \tau_{\rm lag})$ `[Model Ansatz | Tier 3]`
Before pericenter ($t \le 0$), the gas moves with the stars ($x_G(t) = x_S(t), v_G(t) = v_S(t)$). At and after pericenter ($t > 0$), ram pressure decelerates the gas relative to the stars by $\delta_{SG}(T) = x_G(T) - x_S(T) = -|\delta_{SG}(T)| < 0$:
- **Case A14a-grav (Impulsive Shock Drop $\Delta v_{\rm ram}$ + Shared Gravitational Field $\ddot{x}_G = \ddot{x}_S$ for $t > 0$):** At $t = 0^+$, the bow shock reduces gas speed by $\Delta v_{\rm ram} > 0$, after which the post-shock gas also climbs the cluster gravitational potential ($\ddot{x}_G(t > 0) = \ddot{x}_S(t > 0) \implies x_G(T) = x_S(T) - \Delta v_{\rm ram}T$, $|\delta_{SG}(T)| = \Delta v_{\rm ram}T$). Then for $T > \tau_{\rm lag}$, $\tilde{x}_G(T; \tau_{\rm lag}) = \tilde{x}_S(T; \tau_{\rm lag}) + \delta_{SG}(T)$, so $\Delta\tilde{x}_G = \Delta\tilde{x}_S$.
- **Case A14a-coast (Impulsive Shock Into Nearly Hydrostatic Intracluster Medium, $\ddot{x}_G(t > 0) \approx 0$):** If post-shock thermal pressure balances gravity so the stripped gas coasts at constant post-shock velocity ($\ddot{x}_G(t > 0) = 0$), then for $T > \tau_{\rm lag}$, $\tilde{x}_G(T; \tau_{\rm lag}) = x_G(T)$ ($\Delta\tilde{x}_G = 0$), so the stellar extrapolation term in $\beta_{\rm centroid}$ is weighted by $f_S\mathcal{R}/(1 + \mathcal{R})$ instead of $\mathcal{R}/(1 + \mathcal{R})$ (Review Finding m14).
- **Case A14b (Continuous Differential Ram-Pressure Drag $a_{\rm ram} > 0$ plus Shared Gravity):** $|\delta_{SG}(T)| = \frac{1}{2}a_{\rm ram}T^2$ for $T > 0$, giving $\tilde{x}_G(T; \tau_{\rm lag}) = \tilde{x}_S(T; \tau_{\rm lag}) + \delta_{SG}(T)[1 - (\tau_{\rm lag}/T)^2]$ for $T > \tau_{\rm lag}$.

Substituting $\tilde{x}_G(T; \tau_{\rm lag})$ into (e6) yields the **explicit closed-form expressions for $\beta(T; \tau_{\rm lag})$**:

1. **For Global Centroids (`[Model Ansatz | Tier 3]`):**
   $$\beta_{\rm centroid}(T; \tau_{\rm lag}) = \begin{cases}
   \displaystyle \frac{f_G}{1 + \mathcal{R}} - \frac{\mathcal{R}}{1 + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|}, & 0 < T \le \tau_{\rm lag}, \\[12pt]
   \displaystyle f_G - \frac{\mathcal{R}}{1 + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|}, & T > \tau_{\rm lag} \quad (\text{A14a-grav: }\ddot{x}_G = \ddot{x}_S), \\[12pt]
   \displaystyle f_G - \frac{f_S\,\mathcal{R}}{1 + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|}, & T > \tau_{\rm lag} \quad (\text{A14a-coast: }\ddot{x}_G = 0), \\[12pt]
   \displaystyle f_G\left[1 - \frac{\mathcal{R}}{1 + \mathcal{R}}\left(\frac{\tau_{\rm lag}}{T}\right)^2\right] - \frac{\mathcal{R}}{1 + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|}, & T > \tau_{\rm lag} \quad (\text{continuous drag A14b}).
   \end{cases}$$
2. **For Resolved Lensing Convergence Peaks (`[Model Ansatz | Tier 3]`, when $|\delta_{SG}| \gtrsim \sigma_{\rm ref}$ so the gas baryons $M_G$ at $x_G$ are spatially separated from the galaxy+shadow peak):**
   - For $0 < T \le \tau_{\rm lag}$: both shadows ($M_{\rm sh} = \mathcal{R}(M_S + M_G)$) sit at $\tilde{x}_S(T)$, together with the stellar mass $M_S$ at $x_S(T)$, forming a single dominant peak of mass $(f_S + \mathcal{R})M_b \approx 5.15\,M_b$ (vs. $f_G M_b \approx 0.85\,M_b$ at the stripped gas), located at
     $$x_{I,{\rm peak}}(T) = x_S(T) + \frac{\mathcal{R}}{f_S + \mathcal{R}}\,\Delta\tilde{x}_S(T; \tau_{\rm lag}) \implies \beta_{\rm peak}(T; \tau_{\rm lag}) = -\frac{\mathcal{R}}{f_S + \mathcal{R}}\,\frac{\Delta\tilde{x}_S(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|} \qquad (0 < T \le \tau_{\rm lag}).$$
   - For $T > \tau_{\rm lag}$ (once $|\tilde{x}_G - \tilde{x}_S| \gtrsim \sigma_{\rm ref}$): the gas shadow of mass $\mathcal{R} M_G \approx 4.25\,M_b$ lands on the gas at $\tilde{x}_G \approx x_G$, making the gas peak total mass $(1 + \mathcal{R})f_G M_b \approx 5.1\,M_b$ (compared to $(1 + \mathcal{R})f_S M_b \approx 0.9\,M_b$ on the galaxies), so the **main lensing peak switches to the gas**:
     $$\beta_{\rm peak}(T; \tau_{\rm lag}) \underset{T > \tau_{\rm lag}}{\longrightarrow} 1 - \frac{\mathcal{R}}{1 + \mathcal{R}}\,\frac{\Delta\tilde{x}_G(T; \tau_{\rm lag})}{\left|\delta_{SG}(T)\right|} \approx 1 \qquad (\text{main peak on gas}),$$
     while the centroid converges to $\beta_{\rm centroid}(T \gg \tau_{\rm lag}) \to f_G = \frac{M_G}{M_S + M_G} \approx 0.85$.

#### 5. Summary of the Young-Merger Offset Sign and Why T4a Is Moved to EXPLORATORY (Resolving B3)
Under the physically selected symmetric core passage model **[A13b]**, even in a young merger ($0 < T \le \tau_{\rm lag}$), $\Delta\tilde{x}_S^{\rm (A13b)}$ is negative for $0 < T < \frac{2}{3}\tau_{\rm lag}$ and positive only for $\frac{2}{3}\tau_{\rm lag} < T \le \tau_{\rm lag}$. Furthermore, once the Bullet Cluster (`1E 0657-558`, which fixes the lower bound on $\tau_{\rm lag}$) is excluded from the test sample per Rule G2, at most **1 cluster** (`Abell 2744`, $t_p = 0.15 \pm 0.05\text{ Gyr}$) remains below the $150\text{ Myr}$ age cut (and under Dawson 2013's Bullet Cluster dynamical age $t_p = 0.40 \pm 0.10\text{ Gyr}$, any system with $t_p \le 0.27\text{ Gyr}$ lies in the $T < \frac{2}{3}\tau_{\rm lag}$ negative-offset regime of A13b). Therefore, per Gregory's B3 instruction, **Test T4a is moved to `EXPLORATORY (Insufficient Independent Young Mergers, N = 1)`**.

---

## Section (f): Galaxy Rotation Curves, the Cap Theorem, and Orbital Extrapolation

**Section Tier:** **Tier 1** for spherical Newtonian circular speed and the empirical RAR fit (f1, f2); **Tier 3** for the 3D Gaussian shadow convolution, saturation cap, and orbital extrapolation (f3, f4).

### (f1) Spherical Circular Velocity Approximation `[Established | Tier 1]`
$$v_c^2(r) = \frac{G\left[M_b(< r) + M_{\rm sh}(< r)\right]}{r} = v_{\rm bar}^2(r) + v_{\rm sh}^2(r), \qquad g_{\rm obs}(r) = \frac{v_c^2(r)}{r} = g_{\rm bar}(r) + g_{\rm sh}(r).$$
For SPARC mass models (`MassModels_Lelli2016c.mrt`, Assumption **[A15]**) with fixed mass-to-light ratios $\Upsilon_{\rm disk} = 0.5\,M_\odot/L_\odot$ and $\Upsilon_{\rm bul} = 0.7\,M_\odot/L_\odot$:
$$v_{\rm bar}^2(r) = v_{\rm gas}(r)\left|v_{\rm gas}(r)\right| + 0.5\,v_{\rm disk}^2(r) + 0.7\,v_{\rm bul}^2(r), \qquad M_b(< r) = \frac{r\,v_{\rm bar}^2(r)}{G}.$$

### (f2) Empirical Radial Acceleration Relation (RAR Benchmark) `[Established Empirical | Tier 1]`
From McGaugh, Lelli & Schombert (2016):
$$g_{\rm obs}^{\rm RAR}(r) = \frac{g_{\rm bar}(r)}{1 - \exp\!\left(-\sqrt{g_{\rm bar}(r)/g_\dagger}\right)}, \qquad g_\dagger = (1.20 \pm 0.02 \pm 0.24)\times 10^{-10}\text{ m s}^{-2}.$$

### (f3) Exact 3D Gaussian Convolution for a Thin Exponential Disk + Gas + Bulge (Corrected per B1) `[Model Ansatz | Tier 3]`
1. **3D Axisymmetric Density of a Thin Disk Convolved with $K_\sigma$:**  
   For a thin axisymmetric surface density $\Sigma_b(R') = \Sigma_{\rm disk}(R') + \Sigma_{\rm gas}(R')$ in the $z' = 0$ plane, 3D convolution with the isotropic Gaussian (e5) yields
   $$\rho_{{\rm sh,disk}}(R, z) = 6(1 - f_{\rm leak})\,\frac{e^{-z^2/(2\sigma_{\rm ref}^2)}}{\sqrt{2\pi}\,\sigma_{\rm ref}}\int_0^\infty \frac{R'\,dR'}{\sigma_{\rm ref}^2}\,\Sigma_b(R')\,\exp\!\left(-\frac{R^2 + R'^2}{2\sigma_{\rm ref}^2}\right)I_0\!\left(\frac{R R'}{\sigma_{\rm ref}^2}\right).$$
2. **Exact Enclosed Spherical Shadow Mass $M_{\rm sh}(< r)$ via the Radial Error-Function Kernel (B1 Fix Verified by Monte Carlo):**  
   Because $K_\sigma(\mathbf{x} - \mathbf{y})$ is isotropic, the fraction of any source mass element at scalar radius $r' = |\mathbf{y}|$ enclosed within the sphere $|\mathbf{x}| \le r$ is the cumulative distribution function of a non-central chi-squared variable $\chi'^2_3(\lambda = r'^2/\sigma_{\rm ref}^2)$ evaluated at $r^2/\sigma_{\rm ref}^2$. Integrating over polar angle $\cos\theta \in [-1, 1]$ first gives the exact radial shell density
   $$p_{\rm shell}(s \mid r') = \frac{s}{\sqrt{2\pi}\,\sigma_{\rm ref}\,r'}\left[\exp\!\left(-\frac{(s - r')^2}{2\sigma_{\rm ref}^2}\right) - \exp\!\left(-\frac{(s + r')^2}{2\sigma_{\rm ref}^2}\right)\right],$$
   and integrating $s$ from $0$ to $r$ by parts yields the exact 1D analytical kernel `[Established Math | Tier 1]` (with the Gaussian prefactor corrected from $\sqrt{2/\pi}$ to $\frac{1}{\sqrt{2\pi}}$ per Finding B1):
   $$\mathcal{F}_\sigma(r, r') \equiv \int_{|\mathbf{x}| \le r} K_\sigma(\mathbf{x} - \mathbf{y})\,d^3x = \frac{1}{2}\left[\operatorname{erf}\!\left(\frac{r + r'}{\sqrt{2}\,\sigma_{\rm ref}}\right) + \operatorname{erf}\!\left(\frac{r - r'}{\sqrt{2}\,\sigma_{\rm ref}}\right)\right] - \frac{1}{\sqrt{2\pi}}\,\frac{\sigma_{\rm ref}}{r'}\left[\exp\!\left(-\frac{(r - r')^2}{2\sigma_{\rm ref}^2}\right) - \exp\!\left(-\frac{(r + r')^2}{2\sigma_{\rm ref}^2}\right)\right].$$
   **Taylor Check as $r' \to 0^+$:** Expanding both terms to $\mathcal{O}(r'^2)$ using $\frac{d}{du}\operatorname{erf}(u/\sqrt{2}) = \sqrt{\frac{2}{\pi}}e^{-u^2/2}$ gives $\frac{1}{2}[2\operatorname{erf}(\frac{r}{\sqrt{2}\sigma_{\rm ref}})] - \frac{1}{\sqrt{2\pi}}\frac{\sigma_{\rm ref}}{r'}[\frac{2 r r'}{\sigma_{\rm ref}^2}e^{-r^2/(2\sigma_{\rm ref}^2)}] = \operatorname{erf}\!\left(\frac{r}{\sqrt{2}\sigma_{\rm ref}}\right) - \sqrt{\frac{2}{\pi}}\frac{r}{\sigma_{\rm ref}}e^{-r^2/(2\sigma_{\rm ref}^2)} = \mathcal{F}_\sigma(r, 0) > 0$.  
   **Direct 3D Monte Carlo Verification ($N = 500{,}000$ samples, `SEED = 20261030`):**
   | $(r, r', \sigma_{\rm ref})$ | Corrected $\mathcal{F}_\sigma(r, r')$ | 3D Monte Carlo Mean $\pm$ SE | Diff / SE | Old ($\sqrt{2/\pi}$) Value (Wrong) |
   |---|---|---|---|---|
   | $(1.0, 1.0, 1.0)$ | `0.132299` | `0.132254 ± 0.000479` | `-0.09 SE` | `-0.212103` (unphysical $<0$) |
   | $(2.0, 1.0, 1.5)$ | `0.326572` | `0.326040 ± 0.000663` | `-0.80 SE` | `-0.000370` (unphysical $<0$) |
   | $(0.5, 2.0, 1.0)$ | `0.004603` | `0.004596 ± 0.000096` | `-0.07 SE` | `-0.056603` (unphysical $<0$) |
   | $(3.0, 0.5, 2.0)$ | `0.468804` | `0.470328 ± 0.000706` | `+2.16 SE` | `+0.172573` (`-419 SE`) |

   Therefore, for any baryonic radial mass distribution $M_b(< r')$ with non-negative shell mass $dM_b(r')$, the enclosed shadow mass is
   $$M_{\rm sh}(< r) = 6(1 - f_{\rm leak})\int_0^\infty \mathcal{F}_\sigma(r, r')\,dM_b(r'), \qquad v_{\rm sh}^2(r) = \frac{G\,M_{\rm sh}(< r)}{r}.$$
   For an analytical thin exponential disk $\Sigma_d(r') = \frac{M_d}{2\pi R_d^2}e^{-r'/R_d}$ ($dM_d(r') = \frac{M_d}{R_d^2}r' e^{-r'/R_d}dr'$):
   $$M_{{\rm sh},d}(< r) = 6(1 - f_{\rm leak})\,\frac{M_d}{R_d^2}\int_0^\infty \mathcal{F}_\sigma(r, r')\,r'\,e^{-r'/R_d}\,dr'.$$
   **Newtonian Recovery Limits:** As $\sigma_{\rm ref} \to 0^+$, $\mathcal{F}_\sigma(r, r') \to \Theta(r - r')$ and $M_{\rm sh}(< r) \to 6(1 - f_{\rm leak})M_b(< r)$; as $\sigma_{\rm ref} \to \infty$, $\mathcal{F}_\sigma(r, r') \to 0$ at finite $r$ and $v_c(r) \to v_{\rm bar}(r)$ (pure baryons).

3. **Proof of the Saturation Cap Theorem and Forecast for Test T5 (Resolving M3 & m4) `[Model Ansatz Consequence | Tier 3]`:**  
   Because $K_\sigma$ is normalized to $1$ and acts as a 3D heat-diffusion smoothing operator ($\frac{\partial\rho}{\partial(\sigma^2)} = \frac{1}{2}\nabla^2\rho$), for any isolated galaxy whose spherically averaged baryon density decreases outward ($\frac{d\bar{\rho}_b}{dr} \le 0$), Gaussian smoothing strictly moves mass outward ($M_{\rm sh}(< r) \le 6(1 - f_{\rm leak})M_b(< r)$ at every radius $r > 0$, approaching equality as $r \to \infty$ where $M_b(< r) \to M_{b,{\rm tot}}$). Consequently:
   $$\frac{g_{\rm obs}(r)}{g_{\rm bar}(r)} = 1 + \frac{M_{\rm sh}(< r)}{M_b(< r)} \le 1 + 6(1 - f_{\rm leak}) \underset{f_{\rm leak}=1/6}{=} 6.0 \qquad \forall\,r > 0,$$
   and at $r \gg \max(R_d, \sigma_{\rm ref})$, $v_c(r) \simeq \sqrt{G[1 + 6(1 - f_{\rm leak})]M_{b,{\rm tot}}/r} \propto r^{-1/2}$.  
   **Exact Acceleration Threshold & Plain Forecast for Test T5:** Setting $g_{\rm obs}^{\rm RAR}/g_{\rm bar} = [1 - \exp(-\sqrt{g_{\rm bar}/g_\dagger})]^{-1} = 6.0$ gives $\sqrt{g_{\rm bar}^{\rm cap}/g_\dagger} = -\ln(5/6) = 0.182322 \implies g_{\rm bar}^{\rm cap} = 0.033241\,g_\dagger = 3.99\times 10^{-12}\text{ m s}^{-2}$ at $f_{\rm leak} = 1/6$ (or $g_{\rm obs}/g_{\rm bar} = 1 + 5.20 = 6.20 \implies \sqrt{g_{\rm bar}^{\rm cap}/g_\dagger} = -\ln(5.20/6.20) = 0.175891 \implies g_{\rm bar}^{\rm cap} = 0.030938\,g_\dagger = 3.71\times 10^{-12}\text{ m s}^{-2}$ at $\mathcal{R} = 5.20$, and $3.47\times 10^{-12}\text{ m s}^{-2}$ at $\mathcal{R} = 5.36$). Because a large fraction of SPARC low-surface-brightness, dwarf, and outer-disk points lie below $g_{\rm bar}^{\rm cap} \approx 3.7\text{–}4.0\times 10^{-12}\text{ m s}^{-2}$ (where observed $g_{\rm obs}/g_{\rm bar}$ reaches $10\text{–}30$), **this saturation cap makes a full T5 PASS ($\text{median }\chi^2_{\rm red} \le 1.5$ and $\ge 70\%$ with $\chi^2_{\rm red} < 2.0$) very unlikely**. We keep the T5 thresholds unchanged and register the fraction of galaxies and radial points below $g_{\rm bar}^{\rm cap}$ as a mandatory diagnostic.

### (f4) Evaluation of Carried Motion on Circular Orbits and Unified Coarse-Grained Extrapolation (Resolving M5) `[Model Ansatz Analysis | Tier 3]`
For a mass element on a circular orbit of radius $r$ and speed $v_c$, naive element-by-element tangent extrapolation over $\tau_{\rm lag}$ would place its shadow at radius
$$r_{\rm ext} = r\sqrt{1 + \left(\frac{v_c\,\tau_{\rm lag}}{r}\right)^2} = \sqrt{r^2 + \left(v_c\,\tau_{\rm lag}\right)^2} > r.$$
- **Numerical Evaluation at $\tau_{\rm lag} = 150\text{ Myr}$ ($1\text{ km s}^{-1}\times 1\text{ Myr} = 1.02271\times 10^{-3}\text{ kpc}$):**
  - **Spiral disk ($v_c = 200\text{ km s}^{-1}, R_d = 3\text{ kpc}$):** $v_c\tau_{\rm lag} = 30.68\text{ kpc}$, so a star at $r = 3\text{ kpc}$ has radial acceleration timescale $t_{\rm accel} = r/v_c = 14.67\text{ Myr} \ll \tau_{\rm lag}$ (completing $\frac{v_c\tau_{\rm lag}}{2\pi r} = 1.63$ full orbits during $\tau_{\rm lag}$); even at the outer edge $r = 30\text{ kpc}, v_c = 150\text{ km s}^{-1}$, $t_{\rm accel} = r/v_c = 195.6\text{ Myr} \sim \tau_{\rm lag}$ (and $\ll \tau_{\rm lag} \approx 400\text{–}600\text{ Myr}$ under Dawson 2013's Bullet Cluster age).
  - **Dwarf disk ($v_c = 60\text{ km s}^{-1}, R_d = 1\text{ kpc}$):** $v_c\tau_{\rm lag} = 9.20\text{ kpc}$, $t_{\rm accel} = r/v_c = 16.30\text{ Myr} \ll \tau_{\rm lag}$.
- **Why Unified Coarse-Grained Component Extrapolation (e3, Assumptions [A12] & [A16]) Applies One Rule to Both Clusters and Galaxies:**  
  In both clusters and galaxies, applying linear extrapolation to individual particles with internal random or bound orbital velocities ($\sigma_v \sim 1000\text{ km s}^{-1}$ in a cluster subcluster of radius $R_{\rm sub} \sim 250\text{ kpc}$, where $R_{\rm sub}/\sigma_v \approx 244\text{ Myr}$, or $v_c \sim 200\text{ km s}^{-1}$ in a galaxy disk) would blow up any virialized cluster halo to $\sigma_v\tau_{\rm lag} \sim 150\text{–}600\text{ kpc}$ and evacuate any galaxy disk into a hollow ring. Because the inter-string gravity transfer is smoothed over the kernel scale $\sigma_{\rm ref}$, the extrapolated source in (e3) is the **coarse-grained component density shifted by the component's bulk center-of-mass velocity $\mathbf{V}_{{\rm bulk},c}(t - \tau_{\rm lag})\tau_{\rm lag}$**. Under this single rule:
  1. For a colliding cluster subcluster component $c \in \{S, G\}$, $\mathbf{V}_{{\rm bulk},c} \sim 2000\text{–}3000\text{ km s}^{-1}$ shifts the subcluster shadow centroid by $\mathbf{V}_{{\rm bulk},c}\tau_{\rm lag}$.
  2. For an isolated galaxy in its center-of-mass rest frame, $\mathbf{V}_{\rm bulk} = \mathbf{0}$ and $\partial\rho_b/\partial t = 0$, giving $\tilde{\rho}_b(\mathbf{x}) = \rho_b(\mathbf{x})$ identically. Both the primary $\tilde{\rho}_b = \rho_b$ rotation curve and the diagnostic $v_c\tau_{\rm lag}$ curve are reported in Stage 4.

---

## Section (i): Free Parameters and Measurable Proposal for $\epsilon_{\rm far}$

### `[EXPLORATORY — Not Pre-Registered in v1]` Measurable Form for $\epsilon_{\rm far}$ (Stage 1 Proposal for v2) `[Model Ansatz | Tier 3]`
Under Assumption **[A17]**, the $N_r - N_s = 114$ strings in the 6 outer strands of our 133-string rope contribute a fraction $\epsilon_{\rm far} \equiv \frac{\Omega_{\rm dm,far}}{\Omega_{\rm dm}} \ll 1$ of the background shadow dark matter density $\Omega_{\rm dm}$, spread over an inter-strand refraction scale $\sigma_{\rm far} \gg 10\text{ Mpc}$.
- **Background vs. Perturbation Signature:** In Fourier space, the far-string transfer kernel $\hat{K}_{\sigma_{\rm far}}(k) = \exp(-\frac{1}{2}k^2\sigma_{\rm far}^2) \to 0$ on linear structure-formation scales ($k \sim 0.01\text{–}0.2\,h\text{ Mpc}^{-1}$). Thus $\Omega_{\rm dm,far}$ contributes to background expansion $H(a)$ in (a2) while remaining unclustered on galaxy/cluster scales.
- **Exact Linear Growth and $S_8$ Suppression Formula (Resolving m13):** In the linear matter perturbation equation $\ddot{\delta}_m + 2H\dot{\delta}_m = 4\pi G\rho_m(a)\left(1 - \frac{\Omega_{\rm dm}}{\Omega_m}\epsilon_{\rm far}\right)\delta_m$, during the matter-dominated era ($\Omega_m(a) \approx 1$) the growing mode scales as $\delta_m(a) \propto a^{1 - \frac{3}{5}\frac{\Omega_{\rm dm}}{\Omega_m}\epsilon_{\rm far}}$, suppressing the logarithmic growth rate $f(a) = \frac{d\ln\delta_m}{d\ln a}$ and weak-lensing parameter $S_8 \equiv \sigma_8\sqrt{\Omega_m/0.3}$ relative to the CMB-extrapolated $\Lambda\text{CDM}$ value $S_8^{\rm CMB}$ by `[Established Perturbation Math / Model Ansatz Mapping | Tier 1 & 3]`:
  $$f(a) \simeq \left[\Omega_m(a)\right]^{\gamma_L}\left(1 - \frac{3}{5}\frac{\Omega_{\rm dm}}{\Omega_m}\epsilon_{\rm far}\right), \qquad \frac{S_8^{\rm LSS} - S_8^{\rm CMB}}{S_8^{\rm CMB}} \simeq -\frac{3}{5}\frac{\Omega_{\rm dm}}{\Omega_m}\ln\!\left(\frac{1 + z_{\rm eq}}{1 + z_{\rm cut}}\right)\epsilon_{\rm far}.$$
  With the model's $\frac{\Omega_{\rm dm}}{\Omega_m} = \frac{5}{6} = 0.8333$ (at $f_{\rm leak} = 1/6$, so $\frac{3}{5}\frac{\Omega_{\rm dm}}{\Omega_m} = \frac{1}{2}$) and Planck's matter-radiation equality redshift $z_{\rm eq} = 3402$:
  - Evaluating to matter-dark-energy equality $1 + z_{\rm de} = (\Omega_{\Lambda}/\Omega_m)^{1/3} = (13/6)^{1/3} = 1.294 \implies z_{\rm de} = 0.294$ gives $\ln(\frac{3403}{1.294}) = 7.875$, so $\frac{\Delta S_8}{S_8} \simeq -0.5 \times 7.875\,\epsilon_{\rm far} = -3.94\,\epsilon_{\rm far}$ (or $-4.00\,\epsilon_{\rm far}$ if evaluated with Planck's $\Omega_c/\Omega_m = 0.8429$ and $z_{\rm de} = 0.295$).
  - Accounting for the gradual onset of $\Lambda$ suppression prior to $z_{\rm de}$ (equivalent to an effective matter-era growth cutoff at $z_{\rm cut} \approx 0.70$, $\ln(\frac{3403}{1.70}) = 7.602$) gives $\frac{\Delta S_8}{S_8} \simeq -3.80\,\epsilon_{\rm far}$.
  A natural two-crossing geometric target $\epsilon_{\rm far} \approx 0.01\text{–}0.015$ predicts a $4\text{–}6\%$ suppression of $S_8$ ($S_8 \approx 0.78\text{–}0.80$ vs. Planck's $0.832 \pm 0.013$). Per Rule R4, this proposal is recorded for v2 and is not tested or tuned in v1.
