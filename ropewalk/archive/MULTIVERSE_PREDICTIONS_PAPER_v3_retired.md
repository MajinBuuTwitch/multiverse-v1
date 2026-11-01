# Pre-Registered Empirical Falsification of the 19-Strand Ropewalk Multiverse Model Across Cosmological and Astrophysical Scales

- **Document:** `MULTIVERSE_PREDICTIONS_PAPER_v3.md` (Version `3.1.0` / `v4.0.0`, Revised Post-Final Review `REVIEW_FINAL.md` and Blind Independent Rebuild `COMPARISON_ARGON_vs_REBUILD.md`)
- **Date:** `2026-10-30`
- **Governing Pre-Registration:** `PREREG.md` (`v1.0.2`), `MULTIVERSE_STAGE1_EQUATIONS.md` (`v1.0.2`), and `ASSUMPTIONS.md` (`v1.0.2`), frozen in `PREREG_v4.sha256` (`53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b`) and OpenTimestamps proof `PREREG_v4.sha256.ots` (calendar-attested `2026-10-30T08:44:36Z`, anchored at Bitcoin block `973800` / `973821`) prior to data download (`DATA_MANIFEST.sha256` + `DATA_MANIFEST.sha256.ots`, calendar-attested `2026-10-30T08:59:53Z`, anchored at Bitcoin block `973800`).
- **Precedence Clause:** Where `PREREG.md` (`v1.0.2`) and any earlier document disagree, `PREREG.md` (`v1.0.2`) governs. `MULTIVERSE_TESTS_v1.md` is retained as a historical record only.

---

## Abstract

We report the complete, pre-registered empirical evaluation of the 19-strand "Ropewalk" Multiverse model (`v1` static leak formulation), a speculative geometric framework in which our observable universe is one strand of a 19-strand twisted bundle (`1` self strand, `6` nearest-neighbor shadow-matter strands, and `12` outer dark-energy strands), together with a blind independent rebuild constructed from the frozen rulebook alone (`COMPARISON_ARGON_vs_REBUILD.md`, `REBUILD_RESULTS_v1`, `93a154fb...`). Prior to downloading any observational dataset or writing any analysis code, the model's field-equation mappings (`MULTIVERSE_STAGE1_EQUATIONS.md` `v1.0.2`), assumptions (`A1`–`A20` in `ASSUMPTIONS.md` `v1.0.2`), parameter-fixing rules (`F1`–`F5`), validation gates (`G9-a`–`G9-d`), and pass/fail criteria (`PREREG.md` `v1.0.2`) were frozen and cryptographically timestamped on the Bitcoin blockchain via OpenTimestamps (`PREREG_v4.sha256.ots`, block `973800` / `973821`), followed by a second cryptographic freeze of the public dataset manifest (`DATA_MANIFEST.sha256.ots`, block `973800`). We test four primary pillars and seven secondary/exploratory predictions against `DESI DR2 BAO` (with joint Ly$\alpha$ `arXiv:2607.27410`), `Planck 2018`, `Pantheon+`, `DES-SN5YR (Dovekie)`, a 16-cluster dissociative merger catalog (`data/MERGERS.csv`), the `SPARC` 175-galaxy rotation-curve database, `NGC 1052-DF2`, and local Hubble-flow regional heterogeneity (`Pantheon+SH0ES`).

Under the pre-registered decision hierarchy (`PREREG.md` Section 3.3, where **at least one** primary pillar ending in `FAIL` falsifies the model), the `v1` Ropewalk Multiverse model is **empirically falsified (`MODEL FALSIFIED (FAIL)`) under both readings of Validation Gate `G9-b` (through `T5-A`)**:
1. **Two Readings of Gate `G9-b` (`COMPARISON_ARGON_vs_REBUILD.md` Finding 1 & `DEVIATIONS.md` `D3`):** Argon's code evaluated the recombination sound horizon $r_s(z_*)$ using `Chen, Huang & Wang (2019)`'s early-universe formula ($\omega_r = 1/24185$, about $1.1\%$ below the physical radiation density, and the $0.06\text{ eV}$ neutrino counted as pure matter), which gives an $r_s(z_*)$ about $0.18\%$ larger than the registered `(a5)` integral and allows Gate `G9-b` to pass ($\max \Delta = 0.025\sigma$). The blind rebuild coded `(a5)` literally (matching `CAMB`'s $r_s(z_*)$ to $4.9 \times 10^{-5}$), under which `G9-b` fails ($h$ off by $0.577\sigma \approx 0.58\sigma$ against a $0.3\sigma$ tolerance) and its mapped tests **`T2-A`, `T1-L1`, and `T1-Sign` become `INCONCLUSIVE`** (`1` primary pillar `FAIL` via `T5-A`, `3` `INCONCLUSIVE`). Under the Chen form, **`T2-A` is `FAIL`**, **`T5-A` is `FAIL`**, `T1-L1` and `T4b` are `INCONCLUSIVE`, and secondary `T1-Sign` is `PASS` (`2` primary pillars `FAIL`, `2` `INCONCLUSIVE`).
2. **Pillar 1 (`T1-L1` — Unwinding Law 1 $w(a) = -1 + \gamma_u/E(a)$):** **`INCONCLUSIVE` (under both readings)**. Because $\gamma_u \ge 0$ restricts the dark-energy equation of state to $w(a) \ge -1$ along the 1D curve $w_a = -\frac{3}{2}\gamma_u[\Omega_m + \gamma_u(1-\Omega_m)]$, it improves slightly over $\Lambda$CDM ($A_r = -1.7119 / -2.5780$ in Argon, $-1.35 / -2.08$ in the blind rebuild; $p_{\rm T1\text{-}L1} = 0.190744$) but fits worse than the free two-parameter CPL curve by $B_r = +5.4558 / +7.3552$ (Argon) and $+5.55 / +7.48$ (rebuild), landing in the pre-set `INCONCLUSIVE` band.
3. **Pillar 2 (`T2-A` — $1:6:12$ Strand Budget & Leak Ratio):** **`FAIL` under the Chen $r_s(z_*)$ reading / `INCONCLUSIVE` via `G9-b` under literal `(a5)`**. Fixing the bare baryon share to $\Omega_b = 1/19 = 0.052632$ (`+3.8739σ` in Argon, `+3.874σ` in the rebuild above `Planck 2018` $\Omega_b = 0.04930 \pm 0.00086$ in `T2-N1` [`FAIL` in both], and implying $H_0^{\rm pred} = 65.1943 \pm 0.2186\text{ km s}^{-1}\text{ Mpc}^{-1}$ from `Planck 2018` $100\omega_b = 2.237 \pm 0.015$, `-3.7175σ` in Argon and `-3.714σ` in the rebuild below `Planck 2018` $H_0 = 67.36 \pm 0.54$ in `T2-N2` [`FAIL` in both]) forces the predicted dark-to-baryon ratio $\mathcal{R}_{\rm pred} = 19\Omega_{bc}-1$ to $4.8658 \pm 0.1149$ (`Pantheon+`, **$-3.7430\sigma$** in Argon; **$-3.447\sigma$** in the rebuild) and $4.9045 \pm 0.1094$ (`DES-Dovekie`, **$-3.5796\sigma$** in Argon; **$-3.224\sigma$** in the rebuild) against `Planck 2018` $\omega_c/\omega_b = 5.36 \pm 0.065$. Thus `T2-A`'s statistic lies **$3.2\sigma\text{--}3.7\sigma$ from the Planck value** (past the $2\sigma$ `FAIL` line) in every run of both pipelines.
4. **Pillar 3 (`T4b` — Cluster Merger Age Cutoff $\tau_{\rm lag}$):** **`INCONCLUSIVE` (under both pipelines)**. Applying the registered missing-data rule (`PREREG.md` §5.5 item 5) strictly leaves **only one cluster (`MACS J0025.4-1222`)** with complete positions and errors (`n_train = 1, n_test = 0` in the blind rebuild), whereas Argon's 13-cluster set (`n_train = 8, n_test = 5 < 6`, $\hat{\tau}_{\rm lag} = 805\text{ Myr}$) relied on default ($\sigma_G = 5.0\text{ kpc}$) or zero ($\sigma_S = 0.0\text{ kpc}$) errors where source papers gave none (`COMPARISON_ARGON_vs_REBUILD.md` Finding 2 & `DEVIATIONS.md` `D2`). `T4b` is `INCONCLUSIVE` either way.
5. **Pillar 4 (`T5-A` — Universal Refraction Halo Width $\sigma_{\rm ref}$ on SPARC):** **`FAIL` (in both pipelines)**. Minimizing $\sum \chi^2_{{\rm red},g}$ across the 88 odd-indexed training galaxies under the 3D Gaussian enclosed-mass error-function kernel $\mathcal{F}_\sigma(r, r')$ fixes $\hat{\sigma}_{\rm ref} = 9.212795\text{ kpc}$ in Argon ($9.344\text{ kpc}$ in the blind rebuild), which yields a held-out median reduced chi-squared $M_{\chi^2} = 45.1259 > 3.0$ ($45.91$ in the rebuild) and fraction $F_{<2} = 0.0690 < 0.40$ (`6/87` in both pipelines, where passing required $M_{\chi^2} \le 1.5$ and $F_{<2} \ge 0.70$) across the 87 even-indexed test galaxies (and `FAIL` for the disk-scaled secondary test `T5-B` with $\hat{k} = 2.928045$, $M_{\chi^2} = 23.7412$ in Argon and $23.43$ in the rebuild, $F_{<2} = 0.0805$ [`7/87`]). For outward-decreasing spherical baryon density, 3D Gaussian diffusion bounds $g_{\rm tot}(r)/g_{\rm bar}(r) \le 1 + \mathcal{R}_{\rm pred} = 5.8658$; **67 of 175 SPARC galaxies (`38.29%`) have at least one radial point where the observed boost exceeds this 5.8658 maximum, which is 442 of all 3391 radial points (`13.03%`)**.

Among secondary tests, the directional check `T1-Sign` ($P(w_0 > -1) = 0.9960 / 0.9992$ in Argon and $0.99638 / 0.99909$ in the rebuild, `PASS` under the Chen $r_s$ reading of `G9-b` and `INCONCLUSIVE` under literal `(a5)`, known prior to the test and unable to rescue `T1-L1`) and the `NGC 1052-DF2` 3D Plummer enclosed-mass check `T5c` ($M_{\rm pred}(<2.7\text{ kpc}) = 0.9877 \times 10^8 M_\odot$ in Argon and $0.986 \times 10^8 M_\odot$ in the rebuild $\le 2.9 \times 10^8 M_\odot$, `PASS` in both, only because the wide $9.21\text{–}9.34\text{ kpc}$ blur that failed `T5-A` spreads the shadow mass thin) are consistent across both pipelines, while the regional $H_0$ heterogeneity test `T6` across 9 `HEALPix` $N_{\rm side}=1$ Galactic `RING` regions (`491` supernovae in $0.023 \le z_{\rm HD} \le 0.15$) ends in **`FAIL` identically in both pipelines** ($\chi^2_{\rm het} = 8.9347$, $\text{dof}=8$, $p_{\rm het} = 0.347838 > 0.3173$).

---

## 1. Introduction & Pre-Registration Architecture

Speculative cosmological models that aim to unify dark matter and dark energy through geometric or extra-dimensional ansätze require explicit pre-registration so that parameter-fixing rules, datasets, and pass/fail thresholds are locked before seeing the test outcomes. This study was conducted under a four-stage pre-registered protocol (`PREREG.md` `v1.0.2`), with rules frozen and timestamped before data download, one logged runtime deviation (`D1`), two post-hoc review-logged deviations (`D2` and `D3` in `DEVIATIONS.md`), cluster inputs hand-extracted by the analyst (`Section 7`), and a complete blind independent rebuild constructed from the frozen rulebook alone (`Section 6`):

1. **Stage 1 (Theoretical Formulation & Cryptographic Pre-Registration):** Every equation in the model was derived from explicit assumptions (`A1`–`A20` in `ASSUMPTIONS.md` `v1.0.2`), classified as either `[Established]` (standard general relativity, FLRW cosmology, and Newtonian potential theory) or `[Model Ansatz]` (specific to the 19-strand Ropewalk hypothesis), and revised through three rounds of pre-data independent review (`REVIEW_COLD.md`, `REVIEW_V2.md`, `REVIEW_V3.md`). All forks were closed so that every scored test had a single mechanical deciding rule. The complete Stage 1 specification (`PREREG.md` `v1.0.2`, `MULTIVERSE_STAGE1_EQUATIONS.md` `v1.0.2`, `ASSUMPTIONS.md` `v1.0.2`, and `STAGE1_PART1`–`PART3`) was hashed into `PREREG_v4.sha256` (`53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b`) and anchored via OpenTimestamps (`PREREG_v4.sha256.ots`, calendar-attested `2026-10-30T08:44:36Z`, Bitcoin block `973800` / `973821`) before any observational data were downloaded or any analysis code was written.
2. **Stage 2 (Data Freeze, Validation Gates, and Parameter Fixing):** Public observational datasets were downloaded (`08:56Z`) and frozen in `DATA_MANIFEST.sha256` (`73135698afb833e7e95e6a85c55475480132300e29f8b7b42d159c037067896d`) and `DATA_MANIFEST.sha256.ots` (`08:59:53Z`, Bitcoin block `973800`) prior to any fitting. The numerical codebase (`scripts/cosmology.py`, `scripts/sparc_t5.py`) was checked against four validation gates (`G9-a` through `G9-d`, saved in `results/validation_gates_g9.json` and re-verified on the final refactored code in `results/validation_gates_g9_final.json`). Each model free parameter ($f_{\rm leak}$, $\tau_{\rm lag}$, $\sigma_{\rm ref}$, $k$, and $M_B$) was fitted on its designated training dataset and locked in `results/FIXED_VALUES.json` (`results/FREEZE_T1.json`–`FREEZE_T6.json`).
3. **Stage 3 (Execution of Scored & Exploratory Tests):** All primary pillar tests (`T1-L1`, `T2-A`, `T4b`, `T5-A`), secondary scored tests (`T1-Sign`, `T2-N1`, `T2-N2`, `T5-B`, `T5c`, `T6`), sensitivity analyses, and Holm–Bonferroni multiple-testing corrections were computed from the frozen parameters (`results/results.json`).
4. **Stage 4 (Independent Final Review & Blind Independent Rebuild):** An independent reviewer (`REVIEW_FINAL.md`) and a blind independent rebuild built solely from the frozen `v4` rulebook (`COMPARISON_ARGON_vs_REBUILD.md`, `REBUILD_RESULTS_v1`, `93a154fb...`) independently evaluated the entire test suite (`Section 6` and `Section 7`), confirming the overall **`MODEL FALSIFIED (FAIL)`** verdict and identifying the two findings documented in Sections 3, 4.2, 4.3, and 6.

---

## 2. Theoretical Framework & Equation Classification

### 2.1 The 19-Strand Bundle & Static Leak Partition (`T2`)

In the Ropewalk hypothesis (`Assumptions A3, A4, A6, A7` in `MULTIVERSE_STAGE1_EQUATIONS.md` §4), the present-day cosmic budget is modeled by a close-packed hexagonal bundle of $N_s = 1 + 6 + 12 = 19$ four-dimensional FLRW strings (`[Model Ansatz | Tier 3 | Numerology]`):
- **1 Self Strand (`Baryonic Sector`):** Carries standard-model baryonic matter with present-day share `[Model Ansatz, (c3)]`:
  $$\Omega_b = \frac{1}{N_s} = \frac{1}{19} \approx 0.0526316$$
- **6 Nearest-Neighbor Strands (`Shadow-Matter Sector`):** Transmit transverse Newtonian gravity across the inter-strand gap with transmission efficiency $(1 - f_{\rm leak})$, contributing a pressureless cold dark matter share `[Model Ansatz, (b5-S), (c3)]`:
  $$\Omega_{\rm dm}(f_{\rm leak}) = \frac{6(1 - f_{\rm leak})}{19}$$
- **12 Outer-Ring Strands (`Unwinding Dark-Energy Sector`):** Store bulk longitudinal helical tension governed by $w(a)$, with present-day share `[Model Ansatz, (b5-S), (c3)]`:
  $$\Omega_{\rm de}(f_{\rm leak}) = \frac{12 + 6 f_{\rm leak}}{19}$$

In the locked `v1` **Static Form** ($Q \equiv 0$, `[A4]`), $\rho_{\rm dm}(a) = 6(1 - f_{\rm leak})\rho_{b,0}\,a^{-3}$ dilutes as standard pressureless matter at all epochs, so pre-recombination physics is standard and the `Chen, Huang & Wang (2019)` compressed CMB distance priors $(R, \ell_A)$ are valid (`(b5-S)`). Explicitly excluding massive neutrinos $\Omega_{\nu,0} = \frac{0.06}{93.14\,h^2}$ from the three-component share relation (`[A3]`), the pressureless baryon-plus-CDM share $\Omega_{bc} \equiv \Omega_b + \Omega_{\rm dm} = \Omega_{m,{\rm tot}} - \Omega_{\nu,0} = \frac{7 - 6f_{\rm leak}}{19}$ uniquely fixes $f_{\rm leak}$ and the predicted dark-to-baryon ratio $\mathcal{R}_{\rm pred} \equiv \Omega_{\rm dm}/\Omega_b$ (`[Model Ansatz, (c4)]`):
$$f_{\rm leak} = 1 - \frac{19\,\Omega_{bc} - 1}{6}, \qquad \mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak}) = 19\,\Omega_{bc} - 1 \qquad \text{[Model Ansatz, (c4)]}$$
Because $\Omega_{bc} = \Omega_b(1 + \mathcal{R}_{\rm true})$ in any universe, $\mathcal{R}_{\rm pred} = 19\Omega_b(1 + \mathcal{R}_{\rm true}) - 1$, so $6(1 - f_{\rm leak})$ cancels identically out of $\mathcal{R}_{\rm pred} = 19\Omega_{bc} - 1$: **`T2-A` is algebraically a test of $\Omega_b = 1/19$** (`(c4)`). Furthermore, combining $\Omega_b \equiv \omega_b / h^2 = 1/19$ with the physical baryon density $\omega_b \equiv \Omega_b h^2$ `[Established]` yields the parameter-free Hubble constant prediction (`[Model Ansatz, (c4)]`):
$$H_0^{\rm pred} = 100\,\sqrt{19\,\omega_b}\;\;\text{km s}^{-1}\text{ Mpc}^{-1} \qquad \text{[Model Ansatz, (c4)]}$$

### 2.2 Unwinding Dark Energy Equation of State (`T1`)

In a spatially flat FLRW background `[Established, (a2)]`, the dimensionless Hubble expansion rate $E(a) \equiv H(a)/H_0$ obeys:
$$E^2(a) = \Omega_\gamma\,a^{-4} + \Omega_\nu\,f_\nu(a) + \Omega_{bc}\,a^{-3} + \Omega_{\rm de}\,\exp\!\left[3\int_a^1 \frac{1 + w(a')}{a'}\,da'\right] \qquad \text{[Established, (a2)]}$$
Under `Assumptions A8–A9` (`MULTIVERSE_STAGE1_EQUATIONS.md` §5), a power-law twist tension $\rho_{\rm de} \propto \theta^n$ relaxing at constant cosmic-time rate $\dot{\theta} = -\Gamma_u\theta$ ($\Gamma_u \ge 0$) yields **Unwinding Law 1** (`[Model Ansatz, (d4)]`):
$$w(a) = -1 + \frac{\gamma_u}{E(a)}, \qquad \gamma_u \equiv \frac{n\Gamma_u}{3H_0} \ge 0 \qquad \text{[Model Ansatz, (d4)]}$$
Evaluating $w_0 \equiv w(1)$ and $w_a \equiv -dw/da|_{a=1}$ yields the exact 1D curve in the $(w_0, w_a)$ plane (`[Model Ansatz, (d4)]`):
$$w_0 = -1 + \gamma_u \ge -1, \qquad w_a = -\frac{3}{2}\gamma_u\left[\Omega_m + \gamma_u(1 - \Omega_m)\right] = -\frac{3}{2}(1 + w_0)\left[\Omega_m + (1 + w_0)(1 - \Omega_m)\right] \le 0 \qquad \text{[Model Ansatz, (d4)]}$$
Because $\gamma_u \ge 0$ and $E(a) > 0$, Unwinding Law 1 forbids phantom crossing ($w(a) \ge -1$ for all $a > 0$) and has one fewer free parameter than the Chevallier–Polarski–Linder (`CPL`) parametrization $w(a) = w_0 + w_a(1-a)$ `[Established, (a4)]`.

### 2.3 Cross-Strand Gravitational Refraction in Galaxies (`T5`)

Under `Assumptions A10, A12, A15, A16` (`MULTIVERSE_STAGE1_EQUATIONS.md` §6–§7), the shadow matter density is given by the 3D isotropic Gaussian convolution $K_\sigma(\mathbf{r}) = (2\pi\sigma_{\rm ref}^2)^{-3/2}\exp(-|\mathbf{r}|^2/(2\sigma_{\rm ref}^2))$ of the coarse-grained baryon density (`[Model Ansatz, (e3)–(e5)]`). For an isolated axisymmetric galaxy in its rest frame ($\mathbf{V}_{\rm bulk} = \mathbf{0}$, `[A16]`) with monotonically clipped non-negative spherical baryon shell masses $dM_b^{\rm mono}(r') \ge 0$ (`\Upsilon_{\rm disk} = 0.50\,M_\odot/L_\odot$, $\Upsilon_{\rm bul} = 0.70\,M_\odot/L_\odot$, `[A15]`), the circular rotation speed is (`[Established (f1) / Model Ansatz (f3)]`):
$$v_c^2(r) = v_{\rm bar}^2(r) + v_{\rm sh}^2(r) = \frac{G\left[M_b^{\rm mono}(< r) + M_{\rm sh}(< r)\right]}{r}, \qquad M_{\rm sh}(< r) = \mathcal{R}_{\rm pred}\int_0^\infty \mathcal{F}_\sigma(r, r')\,dM_b^{\rm mono}(r')$$
where $\mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak})$ and the exact piecewise 1D radial enclosed-mass kernel $\mathcal{F}_\sigma(r, r')$ (`[Established]` mathematical identity, non-central $\chi'^2_3(r'^2/\sigma_{\rm ref}^2)$ CDF evaluated at $r^2/\sigma_{\rm ref}^2$, verified by 3D Monte Carlo in Stage 1 `B1` and Gate `G9-d`) is:
$$\mathcal{F}_\sigma(r, r') = \begin{cases}
\displaystyle \frac{1}{2}\left[\operatorname{erf}\!\left(\frac{r + r'}{\sqrt{2}\,\sigma_{\rm ref}}\right) + \operatorname{erf}\!\left(\frac{r - r'}{\sqrt{2}\,\sigma_{\rm ref}}\right)\right] - \frac{1}{\sqrt{2\pi}}\,\frac{\sigma_{\rm ref}}{r'}\left[\exp\!\left(-\frac{(r - r')^2}{2\sigma_{\rm ref}^2}\right) - \exp\!\left(-\frac{(r + r')^2}{2\sigma_{\rm ref}^2}\right)\right], & \dfrac{r'}{\sigma_{\rm ref}} \ge 10^{-4}, \\[12pt]
\displaystyle \operatorname{erf}\!\left(\frac{r}{\sqrt{2}\,\sigma_{\rm ref}}\right) - \sqrt{\frac{2}{\pi}}\,\frac{r}{\sigma_{\rm ref}}\exp\!\left(-\frac{r^2}{2\sigma_{\rm ref}^2}\right), & \dfrac{r'}{\sigma_{\rm ref}} < 10^{-4}.
\end{cases}$$

#### Saturation Cap Property (`(f3)` `[Established]` Mathematical Property of 3D Gaussian Kernel `K_\sigma`)
Because $K_\sigma(\mathbf{r})$ is normalized to unity and acts as a 3D diffusion operator, for any isolated galaxy whose spherically averaged baryon density decreases monotonically outward ($d\bar{\rho}_b/dr \le 0$), $M_{\rm sh}(<r) \le \mathcal{R}_{\rm pred}\,M_b^{\rm mono}(<r)$ at every radius $r > 0$ (and asymptotically beyond any central gas hole/ring), enforcing the ceiling:
$$\frac{g_{\rm tot}(r)}{g_{\rm bar}(r)} = 1 + \frac{M_{\rm sh}(< r)}{M_b^{\rm mono}(< r)} \le 1 + \mathcal{R}_{\rm pred} = 1 + 6(1 - f_{\rm leak}) \qquad \text{[Model Ansatz Bound, (f3)]}$$
which equals **$5.8658$** for the frozen `T2-A-Pantheon+` leak fraction $f_{\rm leak} = 0.189038$ (or $6.000$ for $f_{\rm leak} = 1/6$).

### 2.4 Dissociative Galaxy Cluster Mergers (`T4a` & `T4b`)

Under `Assumptions A12, A13b, A14` (`MULTIVERSE_STAGE1_EQUATIONS.md` §6), each coherent baryonic component $c \in \{S, G\}$ in a colliding cluster has its shadow source linearly extrapolated from retarded time $t - \tau_{\rm lag}$ at bulk velocity $\mathbf{V}_{{\rm bulk},c}(t - \tau_{\rm lag})$ (`(e3)`). For `T4b` (`PREREG.md` §5.5):
- **Young Mergers ($t_p < \tau_{\rm lag}$):** The shadow halo remains centered on the collisionless galaxy component (`"with_galaxies"`, `[Model Ansatz]`).
- **Old Mergers ($t_p \ge \tau_{\rm lag}$):** Once the time since pericenter $t_p$ exceeds $\tau_{\rm lag}$, the shadow halo relaxes into the dominant X-ray gas potential (`"with_gas"`, `[Model Ansatz]`).

Using weak-lensing convergence peak (`I`), galaxy (`S`), and X-ray gas peak (`G`) positions, each primary subcluster's separations $d_{IS} = |\mathbf{x}_I - \mathbf{x}_S|$ and $d_{IG} = |\mathbf{x}_I - \mathbf{x}_G|$ are classified via the quadrature-sum uncertainty (`PREREG.md` §5.5 item 4, `[Established]`):
$$\sigma_{\rm diff} = \sqrt{\sigma_I^2 + \sigma_G^2 + \sigma_S^2}$$
into `"with_galaxies"` ($d_{IG} - d_{IS} > 2\sigma_{\rm diff}$), `"with_gas"` ($d_{IS} - d_{IG} > 2\sigma_{\rm diff}$), or `"unclassified"` ($|d_{IG} - d_{IS}| \le 2\sigma_{\rm diff}$), with any cluster lacking a complete set of reported positions and uncertainties marked `"unclassified"` (`PREREG.md` §5.5 item 5).

### 2.5 Regional Hubble-Flow Heterogeneity (`T6`)

Under `Assumptions A10, A20` (`MULTIVERSE_STAGE1_EQUATIONS.md` §8.1 & `PREREG.md` §5.7), `T6` partitions the `Pantheon+SH0ES` non-calibrator Hubble-flow supernovae ($0.023 \le z_{\rm HD} \le 0.15$, `IS_CALIBRATOR == 0`) into the 12 `HEALPix` $N_{\rm side}=1$ Galactic $(l, b)$ `RING` pixels. In a single pre-fit pass in increasing `RING` order $i \in \{0, \dots, 11\}$, any pixel with $0 < N_{{\rm SN},i} < 10$ is merged into its edge-sharing neighbor pixel of lowest `RING` index (`4->0, 7->2, 11->4`), and any pixel remaining $< 10$ after that pass is dropped, leaving $N_{\rm pix}$ regions. Using the full non-diagonal Hubble-flow covariance block $\mathbf{C}_{\rm HF}$ (`(g4)`), the generalized least-squares (`GLS`) heterogeneity statistic `[Established]`
$$\chi^2_{\rm het} = \left(\hat{\mathbf{H}}_0 - \bar{H}_0\,\mathbf{1}\right)^T \mathbf{C}_{H_0}^{-1} \left(\hat{\mathbf{H}}_0 - \bar{H}_0\,\mathbf{1}\right) \quad (\text{dof} = N_{\rm pix} - 1) \qquad \text{[Established, (g4)]}$$
tests whether local Hubble-flow expansion exhibits significant regional variation.

---

## 3. Data Freeze, Validation Gates, and the Two Readings of Gate `G9-b` (`Finding 1`)

All primary public datasets were downloaded and hashed in `DATA_MANIFEST.sha256` (`73135698afb833e7e95e6a85c55475480132300e29f8b7b42d159c037067896d`) and stamped with OpenTimestamps (`DATA_MANIFEST.sha256.ots`, block `973800`) before any fit:
- **`DESI DR2 BAO`:** `desi_gaussian_bao_ALL_GCcomb_mean.txt` and `desi_gaussian_bao_ALL_GCcomb_cov.txt` ($13 \times 13$ Gaussian BAO mean vector and covariance matrix from `DESI Collaboration 2025b`, `arXiv:2503.14738`), with the $z_{\rm eff} = 2.33$ Ly$\alpha$ row replaced in the deciding `T1` and `T2` runs by the joint Ly$\alpha$ BAO+AP measurement (`8.600 ± 0.066`, `39.32 ± 0.33`, $r_{D_H,D_M} = -0.431$) from `DESI Collaboration (2026, arXiv:2607.27410)`.
- **`Pantheon+` & `SH0ES`:** `Pantheon+SH0ES.dat` ($1701$ light-curve rows; $1580$ non-calibrator cosmology SNe with $z_{\rm HD} > 0.01$ and `IS_CALIBRATOR == 0`; $77$ Cepheid calibrators with `IS_CALIBRATOR == 1`; $496$ non-calibrator Hubble-flow SNe in $0.023 \le z_{\rm HD} \le 0.15$) and `Pantheon+SH0ES_stat+sys.cov` (`Brout et al. 2022`, `Riess et al. 2022`).
- **`DES-SN5YR Dovekie`:** `DES-Dovekie_HD.csv` ($1820$ SNe Ia) and `STAT+SYS.npz` (`Popovic et al. 2025`).
- **`Planck 2018` Compressed Likelihood & Registered Priors:** `Chen, Huang & Wang (2019)` Table 1 ($\Lambda$CDM and $w$CDM) $(R, \ell_A, 100\omega_b)$ distance priors, `DESI DR2 / post-LUNA BBN` ($100\omega_b = 2.218 \pm 0.055$), `Cooke+18 BBN` ($100\omega_b = 2.166 \pm 0.019$), and `Planck 2018` parameters ($\Omega_b = 0.04930 \pm 0.00086$, $100\omega_b = 2.237 \pm 0.015$, $H_0 = 67.36 \pm 0.54$), stored in `data/registered_priors.json`.
- **Galaxy Clusters & Rotation Curves:** `data/MERGERS.csv` ($16$ dissociative cluster mergers) + `Wittman, Golovich & Dawson (2018, ApJ 869, 104)` Table 1 (`11` subclusters) and `data/sparc/MassModels_Lelli2016c.mrt` + `SPARC_Lelli2016c.mrt` ($175$ galaxies, $3391$ radial points).

### Validation Gates & Finding 1 (`G9-b` Sound-Horizon Integral $r_s(z_*)$)
Both Argon (`results/validation_gates_g9.json` and `results/validation_gates_g9_final.json`) and the blind rebuild (`REBUILD_RESULTS_v1`) pass Gates `G9-a` (`0.0373σ` in Argon, `0.2977 ± 0.0088` in the rebuild), `G9-c` (`0.3608σ` on $w_0$, `0.4257σ` on $w_a$), and `G9-d` (`1.4397e-11` in Argon, `1.440e-11` in the rebuild vs `1e-10` limit).

For **Gate `G9-b`** (reproducing `Planck 2018` flat $\Lambda\text{CDM}$ parameters from the `Chen, Huang & Wang 2019` compressed CMB prior to within $0.30\sigma$), the comparison with the blind rebuild (`COMPARISON_ARGON_vs_REBUILD.md` Finding 1, logged in `DEVIATIONS.md` as `D3`) identified a key difference in how $r_s(z_*)$ is evaluated:
- **Argon's `Chen, Huang & Wang (2019)` Early-Universe $r_s(z_*)$ Form:** Argon's code (`sound_horizon_rs_chen` in `scripts/cosmology.py`, recorded at `05:02:46` during the gate stage as a "bug fix" ten seconds before the gates passed at `05:02:56`, and not logged as a departure from `(a5)` at the time) uses Chen et al.'s early-universe $r_s(z_*)$ formula, which sets $\omega_r = 1/24185$ (about $1.1\%$ below the physical radiation density) and counts the $0.06\text{ eV}$ neutrino as pure matter at $z \ge z_*$. This yields an $r_s(z_*)$ about **$0.18\%$ larger** than `(a5)` ($+0.29\%$ from the lower $\omega_r$, $-0.12\%$ from the neutrino treatment; dark energy contributes $< 10^{-7}$), lowering $h$ at fixed $\ell_A$ so that `G9-b` passes (`0.0254σ`).
- **Blind Rebuild's Literal `(a5)` Integral:** The blind rebuild coded `(a5)` literally (matching `CAMB`'s $r_s(z_*)$ to $4.9 \times 10^{-5}$ with no calibration factor). Under literal `(a5)`, Gate `G9-b` **fails** ($h$ off by $0.577\sigma \approx 0.58\sigma$ against a $0.30\sigma$ tolerance).
- **Both Readings Reported Plainly:** Under literal `(a5)`, `G9-b` fails and its mapped tests **`T2-A`, `T1-L1`, and `T1-Sign` are `INCONCLUSIVE`**. Under the Chen form, **`T2-A` is `FAIL`**, **`T1-Sign` is `PASS`**, and **`T1-L1` is `INCONCLUSIVE`**. In every run of both pipelines, `T2-A`'s statistic lies **$3.2\sigma\text{--}3.7\sigma$ from the Planck value** (past the $2\sigma$ `FAIL` line), and the model-level verdict is **`MODEL FALSIFIED (FAIL)`** under both readings (through `T5-A`).

---

## 4. Empirical Results & Failure Analysis

### 4.1 Cosmological Expansion (`T1-L1` `INCONCLUSIVE` under Both Readings; `T1-Sign` `PASS` under Chen $r_s$ / `INCONCLUSIVE` via `G9-b` under Literal `a5`)

Fitting Unwinding Law 1 ($w(a) = -1 + \gamma_u/E(a)$, $\gamma_u \ge 0$), flat $\Lambda$CDM, and CPL $w_0w_a$CDM to `DESI DR2 BAO (joint Lyα) + Planck 2018 ΛCDM Table 1 + SN` yields (`results/results.json["T1"]` and `COMPARISON_ARGON_vs_REBUILD.md`):
- **`Pantheon+`:** In Argon (Chen $r_s$), $\chi^2_{\min}(\Lambda\text{CDM}) = 1405.3436$, $\chi^2_{\min}(\text{Law 1}) = 1403.6318$ ($\hat{\gamma}_u = 0.038481$, posterior median $\gamma_u = 0.042946 \pm 0.026160$, implied $w_0 = -0.957054 \pm 0.026160$, $w_a = -0.021748 \pm 0.014720$), $\chi^2_{\min}(w_0w_a\text{CDM}) = 1398.1760$ ($w_0 = -0.854092 \pm 0.055958$, $w_a = -0.513975 \pm 0.215181$), giving $A_{\rm P+} = -1.7119$ and $B_{\rm P+} = +5.4558$. In the blind rebuild (literal `a5`), $A_{\rm P+} = -1.35$ and $B_{\rm P+} = +5.55$.
- **`DES-Dovekie`:** In Argon (Chen $r_s$), $\chi^2_{\min}(\Lambda\text{CDM}) = 1650.9615$, $\chi^2_{\min}(\text{Law 1}) = 1648.3835$ ($\hat{\gamma}_u = 0.043843$, posterior median $\gamma_u = 0.045401 \pm 0.025781$, implied $w_0 = -0.954599 \pm 0.025781$, $w_a = -0.023131 \pm 0.014626$), $\chi^2_{\min}(w_0w_a\text{CDM}) = 1641.0283$ ($w_0 = -0.825007 \pm 0.055675$, $w_a = -0.615279 \pm 0.222775$), giving $A_{\rm Dov} = -2.5780$ and $B_{\rm Dov} = +7.3552$. In the blind rebuild (literal `a5`), $A_{\rm Dov} = -2.08$ and $B_{\rm Dov} = +7.48$.

For the secondary directional check `T1-Sign`, the data favor $w_0 > -1$ at $P(w_0 > -1) = 0.995984 / 0.999219$ in Argon and $0.99638 / 0.99909$ in the blind rebuild ($\sigma_{w_0} \approx 0.056 > 0.03$), which is a **`PASS`** under the Chen $r_s$ reading of `G9-b` and **`INCONCLUSIVE`** via `G9-b` under the literal `(a5)` reading (and was already known from published DESI DR2 data, so it cannot rescue `T1-L1`). In `T1-L1`, the fitted Law 1 slope ($w_a = -0.0217$ and $-0.0231$) is **23.6 to 26.6 times shallower** than the free CPL fits ($w_a = -0.5140$ and $-0.6153$). Under both readings of `G9-b`, `T1-L1` ends in **`INCONCLUSIVE`** (`Figure 1`).

### 4.2 Strand Budget & Leak Ratio (`T2-A` `FAIL` under Chen $r_s$ / `INCONCLUSIVE` via `G9-b` under Literal `a5`; `T2-N1` `FAIL`; `T2-N2` `FAIL`)

Evaluating the $1:6:12$ strand budget and static leak relation $\mathcal{R}_{\rm pred} = 19\Omega_{bc} - 1$ (`(c4)`) yields (`Figure 2`):
1. **Bare Baryon Share (`T2-N1`, Independent of `G9-b`):** $\Omega_b^{\rm model} = 1/19 = 0.052632$ sits **$+3.8739\sigma$** in Argon (**$+3.874\sigma$** in the blind rebuild; `+6.76%`, i.e., `6.8%` higher) above `Planck 2018` $\Omega_b = 0.04930 \pm 0.00086$ (`FAIL` threshold $> 2.0\sigma \implies$ **`FAIL`** in both pipelines).
2. **Implied Hubble Constant (`T2-N2`, Independent of `G9-b`):** Combining $\Omega_b = 1/19$ with the deciding `Planck 2018` physical baryon density $100\omega_b = 2.237 \pm 0.015$ gives $H_0^{\rm pred} = 65.1943 \pm 0.2186\text{ km s}^{-1}\text{ Mpc}^{-1}$, which sits **$-3.7175\sigma$** in Argon (**$-3.714\sigma$** in the blind rebuild) below `Planck 2018` $H_0 = 67.36 \pm 0.54\text{ km s}^{-1}\text{ Mpc}^{-1}$ ($\sigma_{\rm comb} = 0.5826$, `FAIL` threshold $> 2.0\sigma \implies$ **`FAIL`** in both pipelines) and moves away from the local Hubble value near $73\text{ km s}^{-1}\text{ Mpc}^{-1}$.
3. **Leaked Dark-to-Baryon Ratio (`T2-A` Primary Pillar 2 — Both Readings Reported):**
   - **Argon (Chen $r_s(z_*)$ Form):**
     - `Pantheon+` ($\max|\hat{R}-1| = 0.001109$, $\min\text{ESS} = 1909.9$): $\Omega_{bc} = 0.308725 \pm 0.006049 \implies f_{\rm leak} = 0.189038 \pm 0.019155$ and $\mathcal{R}_{\rm pred} = 4.8658 \pm 0.1149$ ($\sigma_{\rm comb} = 0.13204$), which is **$-3.7430\sigma$** from `Planck 2018` $\mathcal{R}_{\rm Planck} = 5.36 \pm 0.065$.
     - `DES-Dovekie` ($\max|\hat{R}-1| = 0.000671$, $\min\text{ESS} = 1890.7$): $\Omega_{bc} = 0.310765 \pm 0.005757 \implies f_{\rm leak} = 0.182578 \pm 0.018231$ and $\mathcal{R}_{\rm pred} = 4.9045 \pm 0.1094$ ($\sigma_{\rm comb} = 0.12724$), which is **$-3.5796\sigma$** from `Planck 2018`.
   - **Blind Rebuild (Literal `(a5)` Integral):**
     - `Pantheon+`: **$-3.447\sigma$** from `Planck 2018`; `DES-Dovekie`: **$-3.224\sigma$** from `Planck 2018`.
   - **Sensitivity Variants (Argon):** `T2-B` constrained $\omega_b = h^2/19$ (`2.4619σ` and `2.3284σ` with $\Delta\chi^2 = +9.8219 > 9$), `Cooke+18 BBN` (`3.0723σ` and `2.8242σ`), and marginal $2\times 2$ CMB (`3.5222σ` and `3.5065σ`) all miss by `2.33σ` to `3.52σ`.
   - **Summary of Both Readings for `T2-A`:** In every run of both pipelines, `T2-A`'s statistic lies **$3.2\sigma\text{--}3.7\sigma$ from the Planck value** (past the $2.0\sigma$ `FAIL` line). Under the Chen $r_s(z_*)$ reading (`G9-b` `PASS`), `T2-A` is **`FAIL`**; under the literal `(a5)` reading (`G9-b` `FAIL`), `T2-A` is **`INCONCLUSIVE`** by the gate mapping rule. The overall model verdict is **`MODEL FALSIFIED (FAIL)`** under both readings (through `T5-A`).

### 4.3 Cluster Merger Relaxation Cutoff (`T4b` `INCONCLUSIVE` in Both Pipelines; `T4a` `EXPLORATORY`)

- **Finding 2 (`COMPARISON_ARGON_vs_REBUILD.md` & `DEVIATIONS.md` `D2`): Strict Missing-Data Rule (`1` Cluster Complete) vs. Default/Zero-Error Set (`13` Clusters):**
  - Applying the registered missing-data rule (`PREREG.md` §5.5 item 5) strictly leaves **only one cluster (`MACS J0025.4-1222`)** with complete positions and errors reported across all three components in its registered source paper (`n_train = 1, n_test = 0` in the blind rebuild).
  - The 13-cluster set in `data/MERGERS.csv` (`n_train = 8`, `n_test = 5`, $\hat{\tau}_{\rm lag} = 805\text{ Myr}$, $\text{Acc}_{\rm train} = 7/8 = 87.5\%$, $\text{Acc}_{\rm test} = 3/5 = 60.0\%$, raw $p = 0.5000$, Holm $p = 1.0000$) relied on default ($\sigma_G = 5.0\text{ kpc}$ for five clusters) or zero ($\sigma_S = 0.0\text{ kpc}$ for `Abell 1758N`, `Abell 2034`, and `Abell 3376`) positional errors where the source paper gave none.
  - **`T4b` Verdict Under Both:** **`T4b` is `INCONCLUSIVE` either way** (`n_train = 1, n_test = 0` under the strict rule; `n_train = 8, n_test = 5 < 6` under `data/MERGERS.csv`). Because the 13-cluster set relied on default or zero errors, no claim based on `"13 classifiable clusters"` is made; too few colliding clusters have complete measurements to test the lag.
- **Exploratory Young-Merger Offset Sign (`T4a`):** `PREREG.md` §5.4 locked `T4a` as exploratory before data analysis because under the physical symmetric harmonic trajectory `A13b` (`(e6)`), the model predicts a negative offset for $0 < T \lesssim \frac{2}{3}\tau_{\rm lag}$ and does not predict a uniform positive sign across all young mergers, and because excluding the Bullet Cluster from `Wittman, Golovich & Dawson (2018, ApJ 869, 104)` Table 1 leaves only $N=1$ subcluster (`A2744 S`, $t_{\rm col} = 120\text{ Myr}$) with $t_{\rm col} \le 235\text{ Myr}$ (or $\le 400\text{ Myr}$), where $\Delta_{SI}^{\parallel} = -45.0 \pm 52.0\text{ kpc}$ ($-0.8654\sigma$; all 10 non-Bullet subclusters: $\bar{\Delta}_{SI}^{\parallel} = -43.7569 \pm 23.7576\text{ kpc}$, $-1.8418\sigma$).

### 4.4 Galactic Rotation Curves & Ultra-Diffuse Galaxies (`T5-A` `FAIL`, `T5-B` `FAIL`, `T5c` `PASS` in Both Pipelines)

Evaluating the 3D Gaussian enclosed-mass error-function kernel $\mathcal{F}_\sigma(r, r')$ (`(f3)`) across the 175 SPARC galaxies (`Figure 4`) yields decisive agreement between Argon and the blind rebuild:
- **Primary Pillar 4 (`T5-A`, Universal $\sigma_{\rm ref}$):** Minimizing $\sum \chi^2_{{\rm red},g}$ across the 88 odd-indexed training galaxies fixes $\hat{\sigma}_{\rm ref} = 9.212795\text{ kpc}$ in Argon ($\text{train } M_{\chi^2} = 48.5128$, $F_{<2} = 0.0341$ [`3/88`]) and $\hat{\sigma}_{\rm ref} = 9.344\text{ kpc}$ in the blind rebuild. Tested on the 87 unseen even-indexed galaxies, `T5-A` fits only 6 of the 87 acceptably ($F_{<2} = 0.0690 < 0.40$ in both pipelines, where passing needed $F_{<2} \ge 0.70$) with a median reduced chi-squared **$M_{\chi^2} = 45.1259 > 3.0$** in Argon and **$M_{\chi^2} = 45.91 > 3.0$** in the blind rebuild (where passing needed $M_{\chi^2} \le 1.5$; pooled $\chi^2_{\rm red} = 324.2171$), resulting in a decisive **`FAIL`** in both pipelines. Even choosing the best possible universal width directly on the held-out set only reaches a median reduced chi-squared of $\sim 37$, confirming this is not a tuning problem.
- **Secondary Disk-Scaled Width (`T5-B`, $\sigma_{{\rm ref},g} = k R_{d,g}$):** Training fixes $\hat{k} = 2.928045$ ($\text{train } M_{\chi^2} = 25.0021$, $F_{<2} = 0.0568$ [`5/88`]). On the 87 unseen test galaxies, `T5-B` yields **$M_{\chi^2} = 23.7412 > 3.0$** in Argon and **$M_{\chi^2} = 23.43 > 3.0$** in the blind rebuild, with **$F_{<2} = 0.0805 < 0.40$** (`7/87`, pooled $\chi^2_{\rm red} = 234.6098$), also ending in **`FAIL`** in both pipelines. All sensitivity loss functions (`total_chi2`, `median_chi2_red`) and $f_{\rm leak} = 1/6$ likewise end in **`FAIL`**.
- **Saturation Cap Diagnostic (`(f3)`):** Under the 3D Gaussian kernel, outward-decreasing spherical baryon density bounds $g_{\rm tot}(r)/g_{\rm bar}(r) \le 1 + \mathcal{R}_{\rm pred} = 5.8658$. Across SPARC, **67 of 175 galaxies (`38.29%`) have at least one radius where the observed boost $V_{\rm obs}^2(r)/V_{\rm bar}^2(r)$ exceeds the model's 5.8658 maximum, which is 442 of all 3391 radial points (`13.03%`)**.
- **Secondary `NGC 1052-DF2` Stress Check (`T5c`):** Using the registered 3D Plummer profile ($M_{*,{\rm DF2}} = 2.0 \times 10^8 M_\odot$, $R_e = 2.2\text{ kpc}$) plus external `NGC 1052` group mass at the frozen $\hat{\sigma}_{\rm ref}$, the predicted enclosed mass at $2.7\text{ kpc}$ is $M_{\rm pred}(<2.7\text{ kpc}) = 0.9877 \times 10^8 M_\odot$ in Argon and $0.986 \times 10^8 M_\odot$ in the blind rebuild ($\le 2.9 \times 10^8 M_\odot$; and $M_{\rm pred}(<3.1\text{ kpc}) = 1.1686 \times 10^8 M_\odot < 3.2 \times 10^8 M_\odot$), ending in **`PASS`** in both pipelines — but only because the same wide $9.21\text{–}9.34\text{ kpc}$ blur that failed the SPARC rotation curves spreads DF2's shadow mass thin.

### 4.5 Regional Hubble-Flow Heterogeneity (`T6` `FAIL` Identically in Both Pipelines) and Cosmic Coincidence Window (`Section 6`)

- **Regional $H_0$ Heterogeneity (`T6`, `Figure 5a`):** Across the $N_{\rm pix} = 9$ retained `HEALPix` $N_{\rm side}=1$ Galactic `RING` regions (`491` Hubble-flow SNe in $0.023 \le z_{\rm HD} \le 0.15$ after single-pass lowest-`RING`-index edge-neighbor merging `4->0, 7->2, 11->4` and dropping pixel `4` with `5` SNe), regional $H_{0,k}$ values range from $72.5255$ to $75.0888\text{ km s}^{-1}\text{ Mpc}^{-1}$ (per-region Hubble-flow errors $0.4665$ to $1.1821\text{ km s}^{-1}\text{ Mpc}^{-1}$; all-sky GLS mean $\bar{H}_0 = 73.5056 \pm 0.2419\text{ (HF)} \pm 1.0474\text{ (tot) km s}^{-1}\text{ Mpc}^{-1}$, $Z_{\rm all\text{-}sky} = 5.2152\sigma$ above `Planck 2018`). The GLS heterogeneity statistic is $\chi^2_{\rm het} = 8.9347$ ($\text{dof}=8$), giving $p_{\rm het} = 0.347838 > 0.3173$ in Argon and $p_{\rm het} = 0.34784 > 0.3173$ in the blind rebuild, which triggers an identical **`FAIL`** in both pipelines. No regional variation is detected at this resolution.
- **Cosmic Coincidence Window (`Section 6`, `Figure 5b`):** Under `Planck 2018` $\Lambda$CDM expansion ($t_0 = 13.8005\text{ Gyr}$), the cosmic density shares $\Omega_i(a)$ match the Ropewalk target partition to within $5\%$ absolute error (`H-Abs`) for $\Delta t_{\rm abs} = 2.2549\text{ Gyr}$ (`16.34%` of $t_0$) and to within $10\%$ relative error (`H-Rel`) for $\Delta t_{\rm rel} = 0.9269\text{ Gyr}$ (`6.72%` of $t_0$) for $f_{\rm leak} = 1/6$ ($\Delta t_{\rm abs} = 2.2956\text{ Gyr}$ [`16.63%`] and $\Delta t_{\rm rel} = 0.7308\text{ Gyr}$ [`5.30%`] for $f_{\rm leak} = 0.189038$).

---

## 5. Candidate Exploratory Extensions for a Future `v2` Model (`EXPLORATORY`)

Per our pre-registration rules (`GEMINI.md` Rule 2 and `PREREG.md`), no unregistered mechanism or parameter may be used to alter, soften, or rescue any `v1` test verdict (`MODEL FALSIFIED (FAIL)`). Two strictly **EXPLORATORY** mathematical extensions derived during Stage 1 (`MULTIVERSE_STAGE1_EQUATIONS.md` §5.4 and §8.3) are recorded solely for potential future out-of-sample testing:

1. **Dynamic Vacuum-Proportional Strand Transfer ($Q_{\rm de} = \xi_e H \rho_{\rm de}$, `[Model Ansatz — EXPLORATORY, §5.4 (d-Exp)]`):**
   Combining bare unwinding $w_{\rm bare}(a) = -1 + \gamma_u/E(a)$ with dark-sector energy transfer $Q_{\rm de} = \xi_e H \rho_{\rm de}$ ($\xi_e > 0$) yields $w_{\rm de}^{\rm eff}(a) = -1 + \gamma_u/E(a) - \xi_e/3$, which remains perturbation-stable ($d < 0$) and allows an effective phantom crossing ($w_{\rm de}^{\rm eff} = -1$) at $E(z_{\rm cross}) = 3\gamma_u/\xi_e$ while keeping $\rho_{\rm de}(a) > 0$ at all $a > 0$. However, it adds an unregistered parameter $\xi_e$ and does not resolve the bare $\Omega_b = 1/19$ tension in `T2-N1`/`T2-N2`.
2. **Smooth Far-String Shadow Component ($\epsilon_{\rm far}$, `[Model Ansatz — EXPLORATORY, §8.3 (i-Exp)]`) and Non-Gaussian Galaxy Kernel:**
   Because any normalized 3D Gaussian kernel $K_\sigma$ enforces the saturation cap $g_{\rm tot}(r)/g_{\rm bar}(r) \le 1 + \mathcal{R}_{\rm pred} = 5.8658$ whenever $d\bar{\rho}_b/dr \le 0$, reproducing flat outer rotation curves in low-surface-brightness galaxies requires replacing the 3D Gaussian kernel with a scale-free/logarithmic cross-strand potential or an acceleration-dependent coupling analogous to the Radial Acceleration Relation (`McGaugh et al. 2016`), which achieved held-out $M_{\chi^2} = 9.4001$ (`fixed`) and $8.4263$ (`fitted`) on the same SPARC sample.

---

## 6. Independent Replication (`COMPARISON_ARGON_vs_REBUILD.md`)

A complete blind independent rebuild of the entire analysis (`REBUILD_RESULTS_v1`, frozen manifest SHA-256 `93a154fb...`) was built from the frozen Stage 1 `v4` rulebook alone (`PREREG.md`, `MULTIVERSE_STAGE1_EQUATIONS.md`, `ASSUMPTIONS.md`), without access to Argon's code or results, and froze its outputs before comparison (`COMPARISON_ARGON_vs_REBUILD.md`). Its files were verified against its frozen manifest, and its validation script confirmed that its $r_s(z_*)$ matches the registered full `(a5)` integral to $\sim 10^{-11}$ and matches `CAMB` to $4.9 \times 10^{-5}$ with no calibration factor.

### Table 1: Argon (`RESULTS_v1`, `b02000c9…`) vs. Blind Rebuild (`REBUILD_RESULTS_v1`, `93a154fb…`)

| Test | Argon | Rebuild | Agree? |
| :--- | :--- | :--- | :--- |
| **`G9-a`** (BAO-only $\Omega_m$) | `0.29718 ± 0.0086`, **`PASS`** | `0.2977 ± 0.0088`, **`PASS`** | **Yes** |
| **`G9-b`** (compressed CMB vs Chen+19) | **`PASS`** (`max 0.025σ`, Chen $r_s$) | **`FAIL`** ($h$ `0.577σ` vs `0.3σ` tolerance, literal `a5`) | **No (see Finding 1)** |
| **`G9-c`** | **`PASS`** | **`PASS`** | **Yes** |
| **`G9-d`** (kernel limit) | `1.44e-11`, **`PASS`** | `1.440e-11`, **`PASS`** | **Yes** |
| **`T1-L1`** (unwinding curve) | $A_r$ `-1.71/-2.58`, $B_r$ `+5.46/+7.36` $\to$ **`INCONCLUSIVE`** | $A_r$ `-1.35/-2.08`, $B_r$ `+5.55/+7.48` $\to$ **`INCONCLUSIVE`** | **Verdict yes** |
| **`T1-Sign`** ($w_0 > -1$) | `0.9960/0.9992` $\to$ **`PASS`** | `0.99638/0.99909` $\to$ **`INCONCLUSIVE`** (gate) | **Numbers yes; verdict differs via `G9-b`** |
| **`T2-A`** (leak ratio vs Planck) | `-3.74σ/-3.58σ` $\to$ **`FAIL`** | `-3.447σ/-3.224σ` $\to$ **`INCONCLUSIVE`** (gate) | **Both beyond the $2\sigma$ `FAIL` line; verdict differs via `G9-b`** |
| **`T2-N1`** ($\Omega_b = 1/19$ vs Planck) | `+3.87σ` **`FAIL`** | `3.874σ` **`FAIL`** | **Yes** |
| **`T2-N2`** (implied $H_0$ vs Planck) | `-3.72σ` **`FAIL`** | `-3.714σ` **`FAIL`** | **Yes** |
| **`T4b`** (cluster lag) | `n_train 8, n_test 5` $\to$ **`INCONCLUSIVE`** | `n_train 1, n_test 0` $\to$ **`INCONCLUSIVE`** | **Verdict yes; inputs differ (Finding 2)** |
| **`T5-A`** (rotation curves) | $\sigma_{\rm ref}$ `9.213 kpc`, median $\chi^2_{\rm red}$ `45.13`, $F_{<2}$ `0.0690` $\to$ **`FAIL`** | $\sigma_{\rm ref}$ `9.344 kpc`, median `45.91`, $F_{<2}$ `0.0690` $\to$ **`FAIL`** | **Yes** |
| **`T5-B`** | median `23.74` $\to$ **`FAIL`** | median `23.43` $\to$ **`FAIL`** | **Yes** |
| **`T5c`** (NGC 1052-DF2) | `0.99e8 M☉` $\to$ **`PASS`** | `0.986e8 M☉` $\to$ **`PASS`** | **Yes** |
| **`T6`** (regional $H_0$) | $p = 0.3478$ $\to$ **`FAIL`** | $p = 0.34784$ $\to$ **`FAIL`** | **Yes (identical)** |
| **Model level** | **`MODEL FALSIFIED`** | **`MODEL FALSIFIED`** (`MODEL INCONCLUSIVE` only under the non-literal reading of D11) | **Yes under the literal rulebook** |

---

## 7. Limitations & Process Record (`REVIEW_FINAL M1, M3, M7, m1–m4, m7` & `COMPARISON_ARGON_vs_REBUILD.md`)

We state the methodological scope and process limitations of this execution plainly, without claiming the study was "fully blind", "manipulation-free", or had "zero researcher freedom":

1. **Pre-Data Cryptographic Freeze:** The governing rulebook (`PREREG.md` `v1.0.2`), mathematical formulation (`MULTIVERSE_STAGE1_EQUATIONS.md` `v1.0.2`), and assumptions (`ASSUMPTIONS.md` `v1.0.2`) were hashed in `PREREG_v4.sha256` (`53ce966a...`) and calendar-attested via OpenTimestamps (`2026-10-30T08:44:36Z`, anchored at Bitcoin block `973800` / `973821`) prior to data download (`08:56Z`) and prior to the dataset manifest freeze `DATA_MANIFEST.sha256` (`08:59:53Z`, anchored at Bitcoin block `973800`).
2. **Sound-Horizon Departure in Gate `G9-b` (`DEVIATIONS.md` `D3` / Finding 1):** During the Part 5 gate stage, `scripts/cosmology.py` (`sound_horizon_rs_chen`) was updated (`05:02:46` local, logged in `ACTIVITY_LOG.md` as a "bug fix" ten seconds before the gates passed at `05:02:56`, and not logged in `DEVIATIONS.md` as a departure from `a5` at the time) to use `Chen, Huang & Wang (2019)`'s early-universe $r_s(z_*)$ formula ($\omega_r = 1/24185$, about $1.1\%$ below the physical radiation density, and the $0.06\text{ eV}$ neutrino counted as pure matter), giving an $r_s(z_*)$ about $0.18\%$ larger than `(a5)`. Under literal `(a5)` (coded in the blind rebuild), `G9-b` fails ($h$ off by $0.58\sigma$ vs $0.30\sigma$ tolerance) and `T2-A`, `T1-L1`, and `T1-Sign` are `INCONCLUSIVE`; under the Chen form, `T2-A` is `FAIL` and `T1-Sign` is `PASS`. Under both readings, `T2-A`'s statistic sits $3.2\text{–}3.7\sigma$ from Planck (past the $2\sigma$ `FAIL` line in every run of both pipelines), and the model-level verdict is **`MODEL FALSIFIED (FAIL)`** through `T5-A`.
3. **Cluster Sample Compilation, Post-Freeze Source Archives, and Missing-Data Rule (`T4b` / Finding 2):**
   - As disclosed in `PREREG.md` Section 5.5 (`N10`), the 16-cluster merger catalog was compiled from the literature by an analyst with prior knowledge of well-known dissociative mergers.
   - The 8 replacement arXiv TeX/PDF cluster source archives in `data/clusters_arxiv_exact/` (`DEVIATIONS.md` entry `D1`, `2026-10-30T05:17:04` local) were downloaded after `DATA_MANIFEST.sha256` was frozen (`04:59:52` local) and are covered by `RESULTS_v2.sha256` and `RESULTS_v3.sha256`.
   - Both the training-half and test-half cluster positions and uncertainties in `data/MERGERS.csv` were hand-extracted by the analyst (`05:24:22`, revised `05:31:50` local) before $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ was frozen (`06:29:35` local), using default ($\sigma_G = 5.0\text{ kpc}$) or zero ($\sigma_S = 0.0\text{ kpc}$) errors where source papers gave none (`DEVIATIONS.md` `D2`). Applying the registered missing-data rule strictly leaves **only one cluster (`MACS J0025.4-1222`)** with complete positions and errors (`n_train = 1, n_test = 0`). `T4b` is `INCONCLUSIVE` either way.
4. **Post-Gate Code Refactoring and Re-Verification (`M1`):**
   - The initial validation gate run (`results/validation_gates_g9.json`, `05:02:56` local) was executed before `scripts/cosmology.py` was refactored (`05:39:33` to `06:28:52` local) to add vectorized quadrature and pre-inverted covariance routines (`joint_chi2_cpl`, `joint_chi2_law1`). Re-running all four validation gates on the final unmodified scripts (`scripts/run_gates_g9_final.py` $\to$ `results/validation_gates_g9_final.json`) confirmed that all four gates pass on Argon's final code.

---

## 8. What Changes for the Film (`REVIEW_FINAL.md` Section 4 & `COMPARISON_ARGON_vs_REBUILD.md`)

### Robust Across Both Pipelines (Safe for Narration)
1. **Model Falsified Under Its Frozen Rules:** Version 1 of the model is falsified under its own frozen rules across both the primary analysis and the blind independent rebuild: the galaxy rotation-curve pillar (`T5-A`) fails decisively in both pipelines (one shadow-blur width, $9.21\text{ kpc}$ in Argon and $9.34\text{ kpc}$ in the blind rebuild, fitted on 88 galaxies and tested on 87 unseen ones, fits only 6 of the 87 acceptably, with median reduced chi-squared $45.13$ and $45.91$ against a pass line of $1.5$ or less; the galaxy-scaled version `T5-B` also fails with median $23.74$ and $23.43$, fitting 7 of 87, and even the best possible universal width only reaches $\sim 37$, so this is not a tuning problem).
2. **Ordinary-Matter Share (`T2-N1`) and Implied Hubble Constant (`T2-N2`):** The model's core number, ordinary matter as exactly 1 part in 19 ($5.26\%$), sits $3.87\sigma$ ($\sim 3.9\sigma$) above Planck's measured $4.93\% \pm 0.09\%$ in both pipelines. The 1-in-19 rule implies a Hubble constant of $65.2 \pm 0.2\text{ km s}^{-1}\text{ Mpc}^{-1}$, $3.72\sigma$ ($\sim 3.7\sigma$) below Planck's $67.4\text{ km s}^{-1}\text{ Mpc}^{-1}$ and moving away from the local value near $73$, not toward it.
3. **Leak-Ratio Prediction (`T2-A` — Describe the Miss, Not an Unconditional Verdict):** The leak-ratio prediction ($\mathcal{R}_{\rm pred} = 4.87$ on `Pantheon+` and $4.90$ on `DES-Dovekie` against Planck's $5.36 \pm 0.065$) lands **$3.2\text{ to }3.7\sigma$ from the Planck value** ($-3.74\sigma / -3.58\sigma$ in Argon; $-3.45\sigma / -3.22\sigma$ in the blind rebuild, and $2.3\text{ to }3.5\sigma$ across all sensitivity variants), past the pre-set $2\sigma$ failure line in every run of both pipelines. Because it is a formal `FAIL` under the Chen et al. $r_s(z_*)$ reading of gate `G9-b` and `INCONCLUSIVE` under the literal `(a5)` reading of `G9-b`, narration should describe the $3.2\text{–}3.7\sigma$ miss rather than presenting `T2-A`'s `FAIL` verdict as unconditional.
4. **Unwinding Dark-Energy Curve (`T1-L1` and `T1-Sign`):** The model's unwinding dark-energy curve (`T1-L1`) is neither confirmed nor ruled out (`INCONCLUSIVE` in both pipelines: it fits slightly better than a plain cosmological constant by $1.35\text{–}2.58$ in chi-square, $p = 0.19$, but worse than the free two-parameter curve by $5.46\text{–}7.48$). The data favor $w_0 > -1$ at $99.6\%\text{–}99.9\%$ (`T1-Sign`, `PASS` under the Chen $r_s$ reading of `G9-b` and `INCONCLUSIVE` under literal `(a5)`), which was already known before the test and cannot rescue the main dark-energy test.
5. **Local Hubble Constant Patchwork Test (`T6`):** Across 9 sky regions (`491` supernovae), the local Hubble constant ranged from $72.5$ to $75.1\text{ km s}^{-1}\text{ Mpc}^{-1}$, with no regional variation detected ($p = 0.3478$, identical in both pipelines), so the "local patchwork" explanation of the Hubble tension failed its test. The local all-sky value, $73.5 \pm 1.0\text{ km s}^{-1}\text{ Mpc}^{-1}$, is $5.2\sigma$ above Planck — an overall offset rather than a regional patchwork.
6. **NGC 1052-DF2 (`T5c`):** The dark-matter-poor galaxy NGC 1052-DF2 is allowed ($0.99 \times 10^8 M_\odot$ in both pipelines against an upper limit of $2.9 \times 10^8 M_\odot$), but only with the caveat that the same wide blur ($9.2\text{–}9.3\text{ kpc}$) that failed the SPARC rotation curves spreads the shadow mass thin.
7. **Cluster Merger Lag Test (`T4b`):** Too few colliding clusters have complete measurements to test the lag (`T4b` is `INCONCLUSIVE` in both pipelines): applying the registered missing-data rule strictly leaves only one cluster (`MACS J0025.4-1222`) with complete positions and errors, while the 13-cluster set relied on default or zero positional errors where source papers gave none.
8. **Blockchain Anchoring & Independent Replication:** The rulebook and the data manifest were hashed and anchored to the Bitcoin blockchain (block `973800` / `973821`) before any test ran, and both an independent final review and a blind independent rebuild from the frozen rulebook alone verified the results.

### Do NOT Say
- That `T2-A`'s `FAIL` verdict is unconditional (describe the $3.2\text{–}3.7\sigma$ miss past the $2\sigma$ line, and note that `T2-A` is `FAIL` under the Chen $r_s$ reading of `G9-b` and `INCONCLUSIVE` under literal `(a5)`).
- Any claim based on `"13 classifiable clusters"` in `T4b` (the 13-cluster set relied on default or zero errors; applying the registered missing-data rule strictly leaves only 1 cluster, `MACS J0025.4-1222`, with complete positions and errors).
- That falsification required two failed pillars. One suffices (`T5-A` fails decisively in both pipelines).
- That the cluster test "failed".
- That the dark-energy law was "ruled out" or "confirmed".
- That the young-merger offsets went "opposite to the prediction".
- That the universe "expands identically in every direction".
- "Fully blind", "manipulation-free" or "zero researcher freedom".
- "PDG 2024 BBN", "2D Gaussian kernel", "Sérsic", "great-circle merging", or any "r_off" equation.
- That DF2 is a win for the model.
- "Six to seven times too flat".
- Any ESS, convergence or timestamp figure taken from the superseded `v1` `RESULTS.md` or withdrawn `REVIEW_PACKET.md`.
- "38% of galaxies violate the bound" without the caveat. Safe version: 67 of 175 galaxies have at least one radius where the observed boost exceeds the model's 5.87 maximum, which is 13% of all points.

---

## 9. Conclusion

Under the rules frozen and anchored to the Bitcoin blockchain (`PREREG_v4.sha256.ots` and `DATA_MANIFEST.sha256.ots`, block `973800` / `973821`) before any test was run, version 1 of the 19-strand Ropewalk Multiverse model is falsified (`MODEL FALSIFIED (FAIL)`) under both readings of Validation Gate `G9-b` (through the decisive failure of the galaxy rotation-curve pillar `T5-A` in both pipelines, alongside the $3.2\text{–}3.7\sigma$ leak-ratio miss in `T2-A` and the $3.9\sigma / 3.7\sigma$ failures of `T2-N1` and `T2-N2`). Every deciding statistic and verdict has been independently verified by both a final code/data review (`REVIEW_FINAL.md`) and a blind independent rebuild constructed from the frozen rulebook alone (`COMPARISON_ARGON_vs_REBUILD.md`).

---

## References

- Bradac, M., et al. 2008, ApJ, 687, 959 (`MACS J0025.4-1222`)
- Brout, D., et al. 2022, ApJ, 938, 110 (`Pantheon+`)
- Chen, L., Huang, Q.-G., & Wang, K. 2019, JCAP, 02, 028 (`Planck 2018` compressed distance priors)
- Cho, H., et al. 2022, ApJ, 925, 68 (`Abell 1240`)
- Clowe, D., et al. 2006, ApJ, 648, L109 (`1E 0657-558` Bullet Cluster)
- Clowe, D., et al. 2012, ApJ, 758, 128 (`Abell 520`)
- Coleman, M., et al. 2017, MNRAS, 464, 2469 (`Abell 2146`)
- Cooke, R. J., Pettini, M., & Steidel, C. C. 2018, ApJ, 855, 102 (`BBN`)
- Danieli, S., et al. 2019, ApJ, 874, L12 (`NGC 1052-DF2`)
- Dawson, W. A., et al. 2012, ApJ, 747, L42 (`DLSCL J0916.2+2951` Musket Ball)
- Dawson, W. A. 2013, ApJ, 772, 131 (`MCMAC` Bullet & Musket Ball dynamics)
- Dawson, W. A., et al. 2015, ApJ, 805, 143 (`CIZA J2242.8+5301`)
- DESI Collaboration 2025b, arXiv:2503.14738 (`DESI DR2 BAO`)
- DESI Collaboration 2026, arXiv:2607.27410 (`DESI DR2 Lyα BAO + Alcock–Paczyński`)
- Eisenstein, D. J., & Hu, W. 1998, ApJ, 496, 605 (`Baryon drag redshift fitting formula`)
- Golovich, N., et al. 2016, ApJ, 831, 110 (`MACS J1149.5+2223`)
- Golovich, N., et al. 2017, ApJ, 838, 110 (`ZwCl 0008.8+5215`)
- Harvey, D., et al. 2015, Science, 347, 1462 (`72-subcluster ensemble`)
- Hu, W., & Sugiyama, N. 1996, ApJ, 471, 542 (`Recombination redshift fitting formula`)
- Jee, M. J., et al. 2014, ApJ, 783, 78 (`Abell 520` & `ACT-CL J0102-4915` El Gordo)
- Jee, M. J., et al. 2015, ApJ, 802, 46 (`CIZA J2242.8+5301` Sausage)
- Jee, M. J., et al. 2016, ApJ, 817, 179 (`RX J0603.3+4214` Toothbrush)
- Lelli, F., McGaugh, S. S., & Schombert, J. M. 2016, AJ, 152, 157 (`SPARC`)
- Macario, G., et al. 2011, ApJ, 728, 82 (`Abell 754`)
- Machado, R. E. G., & Lima Neto, G. B. 2013, MNRAS, 430, 3249 (`Abell 3376`)
- Markevitch, M., et al. 2005, ApJ, 627, 733 (`Abell 520`)
- McGaugh, S. S., Lelli, F., & Schombert, J. M. 2016, PRL, 117, 201101 (`Radial Acceleration Relation`)
- Merten, J., et al. 2011, MNRAS, 417, 333 (`Abell 2744` Pandora)
- Monteiro-Oliveira, R., et al. 2017a, MNRAS, 466, 2614 (`Abell 1758N`)
- Monteiro-Oliveira, R., et al. 2017b, MNRAS, 468, 4566 (`Abell 3376`)
- Monteiro-Oliveira, R., et al. 2018, MNRAS, 481, 1097 (`Abell 2034`)
- Ng, K. Y., et al. 2015, MNRAS, 453, 1531 (`El Gordo`)
- Okabe, N., & Umetsu, K. 2008, PASJ, 60, 345 (`Abell 754`)
- Planck Collaboration VI 2020, A&A, 641, A6 (`Planck 2018 cosmological parameters`)
- Popovic, B., et al. (DES Collaboration) 2025 (`DES-SN5YR Dovekie`)
- Ragozzine, B., et al. 2012, ApJ, 747, 18 (`Abell 1758N`)
- Riess, A. G., et al. 2022, ApJ, 934, L7 (`SH0ES`)
- Schöneberg, N. 2024, JCAP, 06, 006 (`Post-LUNA BBN`)
- van Dokkum, P., et al. 2018, Nature, 555, 629 (`NGC 1052-DF2`)
- Wittman, D., Golovich, N., & Dawson, W. A. 2018, ApJ, 869, 104 (`Dissociative cluster ensemble`)
