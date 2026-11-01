# Pre-Registered Empirical Falsification of the 19-Strand Ropewalk Multiverse Model Across Cosmological and Astrophysical Scales

- **Document:** `MULTIVERSE_PREDICTIONS_PAPER_v2.md` (Version `2.0.0`)
- **Date:** `2026-10-30`
- **Governing Pre-Registration:** `PREREG.md` (`v1.0.2`), frozen in `PREREG_v4.sha256` (`53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b`) and OpenTimestamps proof `PREREG_v4.sha256.ots` prior to data download (`DATA_MANIFEST.sha256` + `DATA_MANIFEST.sha256.ots`).
- **Precedence Clause:** Where `PREREG.md` (`v1.0.2`) and any earlier document disagree, `PREREG.md` (`v1.0.2`) governs. `MULTIVERSE_TESTS_v1.md` is retained as a historical record only.

---

## Abstract

We report the complete, pre-registered empirical evaluation of the 19-strand "Ropewalk" Multiverse model (`v1` static leak formulation), a speculative geometric framework in which our observable universe is one strand of a 19-strand twisted bundle (`1` self strand, `6` nearest-neighbor shadow-matter strands, and `12` outer dark-energy strands). Prior to downloading any observational dataset or writing any analysis code, the model's field-equation mappings, assumptions (`A1`–`A19`), parameter-fixing rules (`F1`–`F5`), validation gates (`G9-a`–`G9-d`), and pass/fail criteria were frozen and cryptographically timestamped on the Bitcoin blockchain via OpenTimestamps (`PREREG_v4.sha256.ots`), followed by a second cryptographic freeze of all raw data files (`DATA_MANIFEST.sha256.ots`). We test four primary pillars and seven secondary/exploratory predictions against `DESI DR2 BAO`, `Planck 2018`, `Pantheon+`, `DES-SN5YR (Dovekie)`, a 16-cluster dissociative merger catalog (`MERGERS.csv`), the `SPARC` 175-galaxy rotation-curve database, `NGC 1052-DF2`, and local Hubble-flow directional isotropy (`Pantheon+SH0ES`).

Under the pre-registered decision hierarchy (`PREREG.md` Section 3.3), the `v1` Ropewalk Multiverse model is **empirically falsified (`MODEL FALSIFIED (FAIL)`)**, with **two of the four primary pillars ending in `FAIL`**, **two ending in `INCONCLUSIVE`**, and **zero ending in `PASS`**:
1. **Pillar 1 (`T1-L1` — Unwinding Law 1 $w(a) = -1 + \gamma_u/E(a)$):** **`INCONCLUSIVE`**. Because $\gamma_u \ge 0$ restricts the dark-energy equation of state to $w(a) \ge -1$ along the ray $w_a \approx -\frac{3}{2}\Omega_{m0}(1+w_0)$, it improves slightly over $\Lambda$CDM ($\Delta\chi^2 = -1.71$ on `Pantheon+`, $-2.58$ on `DES-Dovekie`, $p = 0.1907$) but is disfavored by $\Delta\chi^2 = +5.46$ and $+7.36$ relative to unconstrained $w_0w_a$CDM fits, which prefer a steeper phantom-crossing slope ($w_a \approx -0.51$ to $-0.62$).
2. **Pillar 2 (`T2-A` — $1:6:12$ Strand Budget & Leak Ratio):** **`FAIL`**. Fixing the bare baryon share to $\Omega_b = 1/19 \approx 0.05263$ (`+3.87σ` above `Planck 2018` in `T2-N1` [`FAIL`], and implying $H_0^{\rm pred} = 65.19 \pm 0.22\text{ km s}^{-1}\text{ Mpc}^{-1}$ via `PDG 2024` BBN, `-3.72σ` below `Planck 2018` in `T2-N2` [`FAIL`]) forces the predicted dark-to-baryon ratio $\mathcal{R}_{\rm pred} = 19\Omega_{bc}-1$ to $4.866 \pm 0.115$ (`Pantheon+`, **$-3.74\sigma$**) and $4.905 \pm 0.109$ (`DES-Dovekie`, **$-3.58\sigma$**) against the `Planck 2018` ratio $\omega_c/\omega_b = 5.36 \pm 0.065$.
3. **Pillar 3 (`T4b` — Cluster Merger Age Cutoff $\tau_{\rm lag}$):** **`INCONCLUSIVE`** on the deciding Odd/Even split ($n_{\rm test} = 5 < 6$ classified test clusters after $2\sigma_{\rm diff}$ filtering, $\hat{\tau}_{\rm lag} = 805\text{ Myr}$, $\text{Acc}_{\rm test} = 60.0\%$) and **`FAIL`** in every sensitivity variant where $n_{\rm test} \ge 6$ (`S6`, `S7`) or where the `Abell 520` dark core is used (`S4`). Across the entire 16-cluster sample, **0 of 13 classified mergers (`0%`)** exhibit weak-lensing mass peaks tracking the collisional X-ray gas rather than the galaxies, even at post-pericenter ages $t_p = 1.10\text{–}1.50\text{ Gyr}$.
4. **Pillar 4 (`T5-A` — Universal Refraction Halo Width $\sigma_{\rm ref}$ on SPARC):** **`FAIL`**. Training on 88 odd-indexed SPARC galaxies fixes $\hat{\sigma}_{\rm ref} = 9.213\text{ kpc}$, which yields a held-out median reduced chi-squared $M_{\chi^2} = 45.13 > 3.0$ and fraction $F_{<2} = 6.90\% < 40\%$ across the 87 even-indexed test galaxies (and `FAIL` for the disk-scaled secondary test `T5-B` with $\hat{k} = 2.928$, $M_{\chi^2} = 23.74$). We prove analytically and numerically that any 2D Gaussian convolution of baryonic surface density is bounded above by the asymptotic acceleration ratio $g_{\rm tot}/g_{\rm bar} \le 1 + \mathcal{R}_{\rm pred} = 5.866$, which is violated by $38.3\%$ of SPARC galaxies (`442/3391` radial points).

Among secondary tests, the directional thawing check `T1-Sign` ($P(w_0 > -1) > 0.996$) and the `NGC 1052-DF2` enclosed-mass stress check `T5c` ($M_{\rm pred}(<2.7\text{ kpc}) = 0.99 \times 10^8 M_\odot$) end in **`PASS`**, whereas the regional $H_0$ heterogeneity test `T6` across `HEALPix` $N_{\rm side}=1$ Galactic `RING` regions ends in **`FAIL`** ($\chi^2_{\rm het} = 8.935$, $\text{dof}=8$, $p_{\rm het} = 0.3478 > 0.3173$). We conclude by documenting why each failed mechanism broke down and isolating exploratory `v2` candidates strictly for future out-of-sample testing.

---

## 1. Introduction & Pre-Registration Architecture

Speculative cosmological models that aim to unify dark matter and dark energy through geometric or extra-dimensional ansätze face a persistent methodological hazard: post-hoc parameter tuning, selective dataset choice, and flexible pass/fail thresholds after inspecting observational data. To eliminate all researcher degrees of freedom, this study was conducted under a strict **four-stage pre-registered blind protocol**:

1. **Stage 1 (Theoretical Formulation & Cryptographic Pre-Registration):** Every equation in the model was derived from explicit assumptions (`A1`–`A19` in `ASSUMPTIONS.md`), classified as either `[Established]` (standard general relativity, FLRW cosmology, and Newtonian potential theory) or `[Model Ansatz]` (specific to the 19-strand Ropewalk hypothesis), and subjected to three rounds of independent adversarial review (`REVIEW_COLD.md`, `REVIEW_V2.md`, `REVIEW_V3.md`). All forks were closed so that every test had exactly one mechanical deciding rule. The complete Stage 1 specification (`PREREG.md` `v1.0.2`, `MULTIVERSE_STAGE1_EQUATIONS.md` `v1.0.2`, `ASSUMPTIONS.md` `v1.0.2`, and `PART1`–`PART3` derivations) was hashed into `PREREG_v4.sha256` (`53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b`) and anchored via OpenTimestamps (`PREREG_v4.sha256.ots`) before any observational data were downloaded or any analysis code was written.
2. **Stage 2 (Data Freeze, Validation Gates, and Parameter Fixing):** All observational datasets were downloaded and cryptographically frozen in `DATA_MANIFEST.sha256` (`73135698afb833e7e95e6a85c55475480132300e29f8b7b42d159c037067896d`) and `DATA_MANIFEST.sha256.ots` prior to any fitting. The numerical codebase (`scripts/cosmology.py`, `scripts/sparc_t5.py`) was required to pass four pre-fit validation gates (`G9-a` through `G9-d`, saved in `results/validation_gates_g9.json`). Finally, each model free parameter ($\gamma_u$, $f_{\rm leak}$, $\tau_{\rm lag}$, $\sigma_{\rm ref}$, $k$, and $M_B$) was fitted once on its designated training dataset and locked in `results/FIXED_VALUES.json`.
3. **Stage 3 (Blind Execution of Scored & Exploratory Tests):** All primary pillar tests (`T1-L1`, `T2-A`, `T4b`, `T5-A`), secondary scored tests (`T1-Sign`, `T2-N1`, `T2-N2`, `T5-B`, `T5c`, `T6`), sensitivity analyses, and Holm–Bonferroni multiple-testing corrections were executed mechanically from the frozen parameters.
4. **Stage 4 (Plain Reporting & Final Cryptographic Stamp):** In accordance with our standing scientific integrity rules (`GEMINI.md`), every failed test is reported with the same prominence and precision as every passed test, without post-hoc threshold adjustments or rescue parameters.

---

## 2. Theoretical Framework & Equation Classification

### 2.1 The 19-Strand Bundle & Static Leak Partition (`T2`)

In the Ropewalk hypothesis (`Assumptions A1–A4`), spacetime is modeled as a close-packed hexagonal bundle of $N_{\rm strands} = 1 + 6 + 12 = 19$ four-dimensional FLRW strands (`[Model Ansatz]`):
- **1 Self Strand (`Baryonic Sector`):** Carries standard-model baryonic matter with bare cosmic energy share `[Model Ansatz]`:
  $$\Omega_b^{\rm bare} = \frac{1}{19} \approx 0.0526316 \qquad \text{[Model Ansatz, Eq. 17]}$$
- **6 Nearest-Neighbor Strands (`Shadow-Matter Sector`):** Couple gravitationally across the inter-strand boundary via a transverse Green's function kernel (`Assumptions A3, A8, A14`), contributing a bare dark-matter share `[Model Ansatz]`:
  $$\Omega_{\rm dm}^{\rm bare} = \frac{6}{19} \approx 0.3157895 \qquad \text{[Model Ansatz, Eq. 18]}$$
- **12 Outer-Ring Strands (`Unwinding Dark-Energy Sector`):** Contribute a bare vacuum/torsion energy share `[Model Ansatz]`:
  $$\Omega_{\rm de}^{\rm bare} = \frac{12}{19} \approx 0.6315789 \qquad \text{[Model Ansatz, Eq. 19]}$$

To account for the difference between the bare $1:6:12$ partition and the late-time ~`1:5:13` partition ($\Omega_b : \Omega_{\rm dm} : \Omega_{\rm de} \approx 0.05 : 0.26 : 0.69$), the `v1` model posits a static (`Q = 0`, `Assumption A7`) geometric leak fraction $f_{\rm leak} \in [0, 1)$ from the 6 nearest-neighbor strands into the 12 outer strands prior to recombination (`[Model Ansatz]`):
$$\Omega_b = \frac{1}{19}, \qquad \Omega_{\rm dm}(f_{\rm leak}) = \frac{6(1 - f_{\rm leak})}{19}, \qquad \Omega_{\rm de}(f_{\rm leak}) = \frac{12 + 6 f_{\rm leak}}{19} \qquad \text{[Model Ansatz, Eq. 20]}$$
Consequently, the total matter fraction $\Omega_{bc} \equiv \Omega_b + \Omega_{\rm dm} = \frac{1 + 6(1 - f_{\rm leak})}{19}$ uniquely fixes $f_{\rm leak}$ and the predicted dark-to-baryon abundance ratio $\mathcal{R}_{\rm pred} \equiv \Omega_{\rm dm}/\Omega_b$ (`[Model Ansatz]`):
$$f_{\rm leak} = 1 - \frac{19\,\Omega_{bc} - 1}{6}, \qquad \mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak}) = 19\,\Omega_{bc} - 1 \qquad \text{[Model Ansatz, Eq. 21]}$$
Furthermore, combining $\Omega_b \equiv \omega_b / h^2 = 1/19$ with an independent Big Bang Nucleosynthesis (`BBN`) measurement of the physical baryon density $\omega_b \equiv \Omega_b h^2$ `[Established]` yields a zero-free-parameter prediction for the Hubble constant (`[Model Ansatz]`):
$$H_0^{\rm pred} = 100\,\sqrt{19\,\omega_b^{\rm BBN}}\;\;\text{km s}^{-1}\text{ Mpc}^{-1} \qquad \text{[Model Ansatz, Eq. 29]}$$

### 2.2 Unwinding Dark Energy Equation of State (`T1`)

In a spatially flat FLRW background `[Established]`, the dimensionless Hubble expansion rate $E(a) \equiv H(a)/H_0$ obeys Friedmann's equation `[Established]`:
$$E^2(a) = \Omega_{r0}\,a^{-4} + \Omega_{m0}\,a^{-3} + \Omega_{{\rm de},0}\,\exp\!\left[3\int_a^1 \frac{1 + w(a')}{a'}\,da'\right] \qquad \text{[Established, Eq. 2]}$$
Under `Assumptions A5–A6`, the mechanical unwinding of the 19-strand rope releases torsional potential energy at a rate proportional to the bundle twist relaxation per Hubble time, yielding **Unwinding Law 1** (`[Model Ansatz]`):
$$w(a) = -1 + \frac{\gamma_u}{E(a)}, \qquad \gamma_u \ge 0 \qquad \text{[Model Ansatz, Eq. 10]}$$
Matching $w(a)$ and $dw/da|_{a=1}$ to the standard Chevallier–Polarski–Linder (`CPL`) parameterization $w(a) = w_0 + w_a(1-a)$ `[Established]` yields the exact first-order trajectory in the $(w_0, w_a)$ plane (`[Model Ansatz]`):
$$w_0 = -1 + \gamma_u \ge -1, \qquad w_a = \left.\frac{dw}{da}\right|_{a=1} = -\frac{\gamma_u\,E'(1)}{E^2(1)} = -\frac{3}{2}\,\Omega_{m0}\,\gamma_u = -\frac{3}{2}\,\Omega_{m0}\,(1 + w_0) \le 0 \qquad \text{[Model Ansatz, Eq. 11]}$$
Crucially, because $\gamma_u \ge 0$ and $E(a) > 0$, Unwinding Law 1 strictly forbids phantom crossing ($w(a) \ge -1$ for all $a > 0$) and predicts a shallow negative slope $w_a \approx -0.46(1 + w_0)$.

### 2.3 Cross-Strand Gravitational Refraction in Galaxies (`T5`)

For a thin axisymmetric galactic disk + bulge + gas distribution with total baryonic surface mass density $\Sigma_b(R) = \Upsilon_{\rm disk}\Sigma_{\rm disk}(R) + \Upsilon_{\rm bulge}\Sigma_{\rm bulge}(R) + \Sigma_{\rm gas}(R)$ `[Established]`, `Assumptions A14–A16` model the gravitational pull of the 6 nearest-neighbor shadow strands as a 2D isotropic Gaussian smoothing of width $\sigma_{\rm ref}$ (`refraction halo width`) weighted by $\mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak})$ (`[Model Ansatz]`):
$$\Sigma_{\rm sh}(\mathbf{R}; \sigma_{\rm ref}) = \frac{\mathcal{R}_{\rm pred}}{2\pi\sigma_{\rm ref}^2} \int_{\mathbb{R}^2} \Sigma_b(\mathbf{R}')\,\exp\!\left(-\frac{|\mathbf{R}-\mathbf{R}'|^2}{2\sigma_{\rm ref}^2}\right) d^2R' \qquad \text{[Model Ansatz, Eq. 36]}$$
Inserting this smoothed surface density into the cylindrical Poisson equation `[Established]` yields the radial shadow-matter acceleration (`[Model Ansatz]`):
$$g_{\rm sh}(R; \sigma_{\rm ref}) = G\,\mathcal{R}_{\rm pred} \int_0^\infty \Sigma_b(R')\,R'\,dR' \int_0^\infty k\,dk\,J_1(kR)\,J_0(kR')\,e^{-\frac{1}{2}k^2\sigma_{\rm ref}^2} \qquad \text{[Model Ansatz, Eq. 38]}$$
As proved in Stage 1 (`Review B1` fix in `MULTIVERSE_STAGE1_EQUATIONS.md` Section 5.1), `Eq. 38` can be evaluated via the 1D ring-projected elliptic-integral kernel $\mathcal{F}_\sigma(R, R')$ with prefactor $1/\sqrt{2\pi}$ (`[Established]` mathematical identity):
$$g_{\rm sh}(R; \sigma_{\rm ref}) = \frac{G\,\mathcal{R}_{\rm pred}}{R} \int_0^\infty \Sigma_b(R')\,R'\,\mathcal{F}_\sigma(R, R')\,dR' \qquad \text{[Established Identity, Eq. 38b]}$$
where:
$$\mathcal{F}_\sigma(R, R') = \frac{1}{\sqrt{2\pi}\,\sigma_{\rm ref}} \int_0^\infty \frac{u\,du}{\sqrt{u^2 + R^2}}\,\mathcal{I}_{\rm ring}(R, u)\,\exp\!\left(-\frac{(u - R')^2}{2\sigma_{\rm ref}^2}\right)\left[1 + \exp\!\left(-\frac{2uR'}{\sigma_{\rm ref}^2}\right)\right]$$
and $\mathcal{I}_{\rm ring}(R, u)$ is the exact Newtonian circular-ring Green's function in terms of complete elliptic integrals $K(m)$ and $E(m)$ `[Established]`. The circular rotation velocity is then `[Model Ansatz]`:
$$V_{\rm model}(R) = \sqrt{V_{\rm bar}(R)\,|V_{\rm bar}(R)| + R\,g_{\rm sh}(R; \sigma_{\rm ref})} \qquad \text{[Model Ansatz, Eq. 39]}$$

#### Theorem 1 (Asymptotic Gaussian Saturation Bound `[Established]` Mathematical Property of `[Model Ansatz]` `Eq. 38`)
For any localized baryonic mass distribution of total finite mass $M_b = 2\pi\int_0^\infty \Sigma_b(R')\,R'\,dR'$ and any positive smoothing scale $\sigma_{\rm ref} > 0$, the total enclosed shadow mass at $R \gg R_{\max} + \sigma_{\rm ref}$ approaches $\mathcal{R}_{\rm pred}\,M_b$, so the asymptotic ratio of total predicted rotation velocity squared to baryonic rotation velocity squared cannot exceed:
$$\lim_{R \to \infty} \frac{V_{\rm model}^2(R)}{V_{\rm bar}^2(R)} = 1 + \mathcal{R}_{\rm pred} = 1 + 6(1 - f_{\rm leak}) \qquad \text{[Model Ansatz Bound, Eq. 39b]}$$
In particular, because Gaussian smoothing strictly diffuses mass outward relative to a point mass, at every finite radius $R$ where the baryonic disk is centrally concentrated, $V_{\rm model}^2(R)/V_{\rm bar}^2(R) \le 1 + \mathcal{R}_{\rm pred}$ (`= 5.8658` for the frozen $f_{\rm leak} = 0.189038$, or `6.000` for $f_{\rm leak} = 1/6$).

### 2.4 Dissociative Galaxy Cluster Mergers (`T4a` & `T4b`)

Under `Assumptions A12–A13`, shadow matter in adjacent strands is coupled to the local baryon potential with a cross-strand relaxation lag time $\tau_{\rm lag}$ (`[Model Ansatz]`):
- **Regime I (Young Mergers, $t_p < \tau_{\rm lag}$):** Following a high-velocity cluster pericenter passage where the collisional X-ray intracluster medium (`G`) is ram-pressure stripped from the collisionless galaxies (`S`), the shadow halo has not yet relaxed to the stripped gas potential and remains bound to the collisionless galaxy potential (`"with_galaxies"`, `[Model Ansatz]`).
- **Regime II (Old Mergers, $t_p \ge \tau_{\rm lag}$):** Once the time since pericenter $t_p$ exceeds $\tau_{\rm lag}$, since the X-ray gas (`G`) contains $\sim 85\%$ of the cluster's baryonic mass, the cross-strand shadow halo is predicted to relax into the dominant gas potential (`"with_gas"`, `[Model Ansatz]`).

Using published weak-lensing mass peak (`I`), galaxy (`S`), and X-ray gas (`G`) positions (`data/MERGERS.csv`), each subcluster'sprojected separation $d_{IS} = |\mathbf{x}_I - \mathbf{x}_S|$ and $d_{IG} = |\mathbf{x}_I - \mathbf{x}_G|$ is tested against the $2\sigma_{\rm diff}$ rule (`Eq. 33`, `[Established]`, where $\sigma_{\rm diff} = \sqrt{\sigma_I^2 + \max(\sigma_S^2, \sigma_G^2)}$).

### 2.5 Regional Hubble-Flow Heterogeneity (`T6`)

Under `Assumptions A17–A19`, if local variations in the inter-strand twist density create domain-scale variations in the effective local expansion rate $H_{0,k}$ across the sky (`[Model Ansatz]`), partitioning the `Pantheon+SH0ES` Hubble-flow supernovae ($0.0233 \le z_{\rm HD} \le 0.15$) into `HEALPix` $N_{\rm side}=1$ Galactic `RING` regions (`12` equal-area sky regions of $3437.75\text{ deg}^2$) and evaluating the full non-diagonal generalized least-squares (`GLS`) heterogeneity statistic `[Established]`:
$$\chi^2_{\rm het} = \left(\hat{\mathbf{H}}_0 - \bar{H}_0\,\mathbf{1}\right)^T \mathbf{C}_{H_0,{\rm HF}}^{-1} \left(\hat{\mathbf{H}}_0 - \bar{H}_0\,\mathbf{1}\right) \sim \chi^2_{N_{\rm pix}-1} \qquad \text{[Established, Eq. 43]}$$
tests whether the observed `SH0ES` vs `Planck` Hubble tension arises from directional domain heterogeneity.

---

## 3. Data Freeze, Validation Gates, and Parameter Freeze

All datasets were downloaded and hashed in `DATA_MANIFEST.sha256` (`73135698afb833e7e95e6a85c55475480132300e29f8b7b42d159c037067896d`) and stamped with OpenTimestamps (`DATA_MANIFEST.sha256.ots`) before any fit:
- **`DESI DR2 BAO`:** `desi_gaussian_bao_ALL_GCcomb_mean.txt` and `desi_gaussian_bao_ALL_GCcomb_cov.txt` ($13 \times 13$ exact Gaussian BAO mean vector and covariance matrix from `DESI Collaboration 2025`, `arXiv:2503.14738`).
- **`Pantheon+` & `SH0ES`:** `Pantheon+SH0ES.dat` ($1701$ rows; $1590$ Cosmology SNe with $z_{\rm HD} > 0.01$; $77$ Cepheid calibrators; $496$ Hubble-flow SNe in $0.0233 \le z_{\rm HD} \le 0.15$) and `Pantheon+SH0ES_stat+sys.cov` (`Brout et al. 2022`, `Riess et al. 2022`).
- **`DES-SN5YR Dovekie`:** `DES-Dovekie_HD.csv` ($1820$ SNe Ia) and `STAT+SYS.npz` (`DES Collaboration 2024/2025`).
- **`Planck 2018` Compressed Likelihood & BBN:** `Chen, Huang & Wang (2019)` Table 1 ($\Lambda$CDM) and Table 2 ($w$CDM) $(R, l_A, 100\omega_b)$ distance priors (`data/planck2018_compressed_chen2019.json`) and `PDG 2024` / `Cooke+18` / `DESI+LUNA` BBN priors (`data/bbn_priors.json`).
- **Galaxy Clusters & Rotation Curves:** `data/MERGERS.csv` ($16$ dissociative cluster mergers) + `data/wittman2018_table2.csv` ($11$ subclusters) and `data/sparc/MassModels_Lelli2016c.mrt` + `SPARC_Lelli2016c.mrt` ($175$ galaxies, $3391$ radial points).

All four pre-fit validation gates (`G9-a`: $0.037\sigma \le 0.30\sigma$; `G9-b`: $0.025\sigma \le 0.30\sigma$; `G9-c`: $0.361\sigma / 0.426\sigma \le 1.0\sigma$; `G9-d`: $1.44 \times 10^{-11} < 10^{-10}$) passed (`Section 2` of `RESULTS.md`), unlocking Stage 2 parameter fixing (`results/FIXED_VALUES.json`).

---

## 4. Empirical Results & Failure Analysis

### 4.1 Cosmological Expansion (`T1-L1` `INCONCLUSIVE`, `T1-Sign` `PASS`)

Fitting Unwinding Law 1 ($w(a) = -1 + \gamma_u/E(a)$, $\gamma_u \ge 0$), flat $\Lambda$CDM, and CPL $w_0w_a$CDM to `DESI DR2 BAO + Planck 2018 + SN` yields:
- **`Pantheon+`:** $\chi^2_{\min}(\Lambda\text{CDM}) = 1405.34$, $\chi^2_{\min}(\text{Law 1}) = 1403.63$ ($\hat{\gamma}_u = 0.0385$, posterior $\gamma_u = 0.0429 \pm 0.0262$), $\chi^2_{\min}(w_0w_a\text{CDM}) = 1398.18$ ($w_0 = -0.854 \pm 0.056$, $w_a = -0.514 \pm 0.215$). Thus $A_{\rm P+} = -1.71$ and $B_{\rm P+} = +5.46$.
- **`DES-Dovekie`:** $\chi^2_{\min}(\Lambda\text{CDM}) = 1650.96$, $\chi^2_{\min}(\text{Law 1}) = 1648.38$ ($\hat{\gamma}_u = 0.0438$, posterior $\gamma_u = 0.0454 \pm 0.0258$), $\chi^2_{\min}(w_0w_a\text{CDM}) = 1641.03$ ($w_0 = -0.825 \pm 0.056$, $w_a = -0.615 \pm 0.223$). Thus $A_{\rm Dov} = -2.58$ and $B_{\rm Dov} = +7.36$.

While the secondary directional test `T1-Sign` passes ($P(w_0 > -1) = 0.9960$ and $0.9992$), the primary test `T1-L1` is **`INCONCLUSIVE`** across both deciding runs and all 6 sensitivity variants (`Figure 1`). Physically, the single-parameter unwinding law $w(a) = -1 + \gamma_u/E(a)$ couples the present-day offset $1+w_0 = \gamma_u$ rigidly to the derivative $w_a = -\frac{3}{2}\Omega_{m0}\gamma_u \approx -0.46\gamma_u$, which is too flat by an order of magnitude to match the rapid redshift evolution ($w_a \approx -0.51$ to $-0.62$) preferred by `DESI DR2 + CMB + SN`.

### 4.2 Strand Budget & Leak Ratio (`T2-A` `FAIL`, `T2-N1` `FAIL`, `T2-N2` `FAIL`)

Evaluating the $1:6:12$ strand budget and static leak relation $\mathcal{R}_{\rm pred} = 19\Omega_{bc} - 1$ (`Eq. 21`) produces a decisive falsification across every variant (`Figure 2`):
1. **Bare Baryon Share (`T2-N1`):** $\Omega_b^{\rm model} = 1/19 = 0.052632$ exceeds the `Planck 2018` value $\Omega_b = 0.04930 \pm 0.00086$ by **$+3.87\sigma$** (`> 3.0σ` $\implies$ **`FAIL`**).
2. **Implied Hubble Constant (`T2-N2`):** Combining $\Omega_b = 1/19$ with the deciding `PDG 2024` BBN prior $100\omega_b = 2.237 \pm 0.015$ gives $H_0^{\rm pred} = 65.19 \pm 0.22\text{ km s}^{-1}\text{ Mpc}^{-1}$, which lies **$-3.72\sigma$** below `Planck 2018` ($67.36 \pm 0.54$, **`FAIL`**) and moves away from `SH0ES` ($73.04 \pm 1.04$).
3. **Leaked Dark-to-Baryon Ratio (`T2-A` Primary Pillar 2):**
   - `Pantheon+`: $\Omega_{bc} = 0.308725 \pm 0.006049 \implies f_{\rm leak} = 0.1890 \pm 0.0192$ and $\mathcal{R}_{\rm pred} = 4.8658 \pm 0.1149$, which is **$-3.74\sigma$** below `Planck 2018` $\mathcal{R}_{\rm Planck} = 5.36 \pm 0.065$ (`> 2.0σ` $\implies$ **`FAIL`**).
   - `DES-Dovekie`: $\Omega_{bc} = 0.310765 \pm 0.005757 \implies f_{\rm leak} = 0.1826 \pm 0.0182$ and $\mathcal{R}_{\rm pred} = 4.9045 \pm 0.1094$, which is **$-3.58\sigma$** below `Planck 2018` (`> 2.0σ` $\implies$ **`FAIL`**).
   - Even when the early-time CMB acoustic likelihood is forced to obey $\omega_c/\omega_b = 19\Omega_{bc}-1$ in the constrained sensitivity test `T2-B`, both runs still end in **`FAIL`** (`-2.46σ` with $\Delta\chi^2 = +8.54$ on `Pantheon+`; `-2.33σ` with $\Delta\chi^2 = +9.82 > 9$ on `DES-Dovekie`).

**Why `T2` Failed:** The failure of Pillar 2 is structural. In a 19-strand equal-partition bundle where baryons occupy 1 strand ($\Omega_b = 1/19$), the sum of baryons and dark matter is $\Omega_{bc} = (1 + \mathcal{R}_{\rm pred})/19$. Because `DESI DR2 BAO` and `SN` pin $\Omega_{bc} \approx 0.309$ while early-universe CMB acoustic peaks pin $\mathcal{R}_{\rm Planck} = \omega_c/\omega_b = 5.36$, the product $19\,\Omega_{bc} - 1 \approx 4.87$ is irreconcilable with $5.36$ unless either (a) the bare baryon share is smaller than $1/19$ ($\Omega_b \approx 1/20.3$) or (b) dark matter/dark energy exchange energy dynamically between $z_* \approx 1090$ and $z = 0$ (`Q != 0`).

### 4.3 Cluster Merger Relaxation Cutoff (`T4b` `INCONCLUSIVE` / `FAIL`, `T4a` `EXPLORATORY`)

Across the 16 dissociative galaxy cluster mergers in `data/MERGERS.csv` (`Figure 3`), 13 primary subclusters are classified at $> 2\sigma_{\rm diff}$ confidence (`8` in the odd-indexed training set and `5` in the even-indexed test set), and 3 even-indexed test clusters (`#4 Abell 1758N`, `#8 Abell 3376`, `#16 ZwCl 0008`) are `"unclassified"` ($|d_{IG}-d_{IS}| \le 2\sigma_{\rm diff}$).
- **Complete Absence of the Old-Merger `"with_gas"` Branch:** All 13 classified primary subclusters (`100%`) have weak-lensing mass peaks coincident with the collisionless galaxies (`"with_galaxies"`), including all three late-stage post-pericenter systems with $t_p > 1.0\text{ Gyr}$ (`#12 Musket Ball` at $1.10\text{ Gyr}$, `#14 MACS J1149` at $1.16\text{ Gyr}$, and `#15 Toothbrush` at $1.50\text{ Gyr}$).
- **Deciding Split Outcome:** Training on the 8 odd-indexed clusters fixes $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ ($\text{Acc}_{\rm train} = 7/8 = 87.5\%$). On the held-out even-indexed test set, $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ correctly classifies the 3 young test mergers ($t_p \le 0.75\text{ Gyr}$) and misclassifies both old test mergers (`Musket Ball` and `MACS J1149`), giving $\text{Acc}_{\rm test} = 3/5 = 60.0\%$ ($p_{\rm raw} = 0.50$). Because $n_{\rm test} = 5 < 6$, `Rule G8(3)` mechanically assigns **`INCONCLUSIVE`**.
- **Sensitivity Splits with $n_{\rm test} \ge 6$ (`S6` & `S7`) and `Abell 520` Dark Core (`S4`):** When `Abell 1758N` uses the `Ragozzine+12` lensing peak (`S6`, $n_{\rm test} = 6$), when the catalog is split First-8 vs Last-8 (`S7`, $n_{\rm test} = 7$, $\text{Acc}_{\rm test} = 28.6\%$), or when `Abell 520` uses the `Jee+14` `P3` dark core (`S4`, $\text{Acc}_{\rm train} = 75.0\% < 80\%$), `T4b` triggers an explicit **`FAIL`**.
- **Exploratory Young-Merger Offset Sign (`T4a`):** In `Wittman et al. (2018)` Table 2, the non-Bullet young merger (`A2744 S`, $t_{\rm col} = 120\text{ Myr}$) has $\Delta_{SI,\parallel} = -45 \pm 52\text{ kpc}$ ($-0.87\sigma$), and the 10-subcluster non-Bullet ensemble has $\bar{\Delta}_{SI,\parallel} = -43.8 \pm 23.8\text{ kpc}$ ($-1.84\sigma$), opposite to the positive leading-offset sign predicted by `Assumption A13a`.

### 4.4 Galactic Rotation Curves & Ultra-Diffuse Galaxies (`T5-A` `FAIL`, `T5-B` `FAIL`, `T5c` `PASS`)

Evaluating the 2D Gaussian-smeared shadow-matter kernel (`Eq. 38`) across the 175 SPARC galaxies (`Figure 4`) yields:
- **Primary Pillar 4 (`T5-A`, Universal $\sigma_{\rm ref}$):** Minimizing $\sum \chi^2_{{\rm red},g}$ across the 88 odd-indexed training galaxies fixes $\hat{\sigma}_{\rm ref} = 9.2128\text{ kpc}$ ($\text{train } M_{\chi^2} = 48.51$). Evaluated blindly on the 87 held-out even-indexed test galaxies, `T5-A` yields a median reduced chi-squared **$M_{\chi^2} = 45.13 > 3.0$** and fraction **$F_{<2} = 0.0690 < 0.40$** (pooled $\chi^2_{\rm red} = 324.22$), resulting in a decisive **`FAIL`**.
- **Secondary Disk-Scaled Width (`T5-B`, $\sigma_{{\rm ref},g} = k R_{d,g}$):** Training fixes $\hat{k} = 2.9280$ ($\text{train } M_{\chi^2} = 25.00$). On the 87 held-out test galaxies, `T5-B` yields **$M_{\chi^2} = 23.74 > 3.0$** and **$F_{<2} = 0.0805 < 0.40$** (pooled $\chi^2_{\rm red} = 234.61$), also ending in **`FAIL`**. Every alternative loss function (`total_chi2`, `median_chi2_red`) and leak fraction ($f_{\rm leak} = 1/6$) likewise ends in **`FAIL`**.
- **Secondary `NGC 1052-DF2` Stress Check (`T5c`):** At the frozen $\hat{\sigma}_{\rm ref} = 9.2128\text{ kpc}$, the predicted enclosed dynamical mass of `NGC 1052-DF2` is $M_{\rm pred}(<2.7\text{ kpc}) = 0.99 \times 10^8 M_\odot \le 2.9 \times 10^8 M_\odot$ and $M_{\rm pred}(<3.1\text{ kpc}) = 1.17 \times 10^8 M_\odot < 3.2 \times 10^8 M_\odot$, ending in **`PASS`**.

**Why `T5` Failed:** The failure of Pillar 4 is a direct mathematical consequence of **Theorem 1** (`Section 2.3`). A single-scale 2D Gaussian convolution of a galaxy's baryonic surface density is a linear spatial low-pass filter whose enclosed mass cannot exceed $\mathcal{R}_{\rm pred}\,M_b$, bounding $V_{\rm model}^2(R)/V_{\rm bar}^2(R) \le 1 + \mathcal{R}_{\rm pred} = 5.866$. In the outer disks of gas-rich dwarf and low-surface-brightness galaxies (`38.3%` of SPARC galaxies), the observed acceleration ratio $g_{\rm obs}/g_{\rm bar}$ reaches $10\text{–}30$, which is impossible for any Gaussian kernel with $\mathcal{R}_{\rm pred} \approx 5$ to reach. Simultaneously, preventing inner-disk overprediction in high-surface-brightness spirals forces $\hat{\sigma}_{\rm ref} = 9.21\text{ kpc}$, which diffuses the shadow halo out of dwarf galaxies (and out of `NGC 1052-DF2`, explaining why `T5c` passed while `T5-A` failed).

### 4.5 Regional Hubble-Flow Isotropy (`T6` `FAIL`) and Cosmic Coincidence Window (`Section 6`)

- **Regional $H_0$ Heterogeneity (`T6`, `Figure 5a`):** Across the $N_{\rm pix} = 9$ retained `HEALPix` $N_{\rm side}=1$ Galactic `RING` regions (`491` Hubble-flow SNe after pre-fit merging of sparse pixels `4, 7, 11`), regional $H_{0,k}$ values span the narrow interval $[72.53, 75.09]\text{ km s}^{-1}\text{ Mpc}^{-1}$ (all-sky $\bar{H}_0 = 73.51 \pm 0.24\text{ (HF)} \pm 1.05\text{ (tot) km s}^{-1}\text{ Mpc}^{-1}$, $Z_{\rm all\text{-}sky} = 5.22\sigma$). The GLS heterogeneity statistic is $\chi^2_{\rm het} = 8.9347$ ($\text{dof}=8$), corresponding to $p_{\rm het} = 0.3478 > 0.3173$ ($< 1\sigma$ variation), which triggers a **`FAIL`**.
- **Cosmic Coincidence Window (`Section 6`, `Figure 5b`):** Under `Planck 2018` $\Lambda$CDM expansion ($t_0 = 13.80\text{ Gyr}$), the cosmic density shares $\Omega_i(a)$ match the Ropewalk target partition to within $5\%$ absolute error (`H-Abs`) for $\Delta t_{\rm abs} = 2.255\text{ Gyr}$ (`16.3%` of $t_0$) and to within $10\%$ relative error (`H-Rel`) for only $\Delta t_{\rm rel} = 0.927\text{ Gyr}$ (`6.7%` of $t_0$) for $f_{\rm leak} = 1/6$ (`0.731 Gyr` or `5.3%` of $t_0$ for $f_{\rm leak} = 0.1890$). Thus, the static `v1` leak mechanism does not resolve the cosmic coincidence problem.

---

## 5. Candidate Exploratory Extensions for a Future `v2` Model (`EXPLORATORY`)

Per our pre-registration rules (`GEMINI.md` Rule 2 and User Directive 3), no unregistered mechanism or parameter may be used to alter, soften, or rescue any `v1` test verdict (`MODEL FALSIFIED (FAIL)`). For completeness and to guide potential future out-of-sample pre-registrations, we record two strictly **EXPLORATORY** mathematical extensions identified during Stage 1 (`PART2_RESULTS.md` and `ASSUMPTIONS.md`):

1. **Dynamic Vacuum-Proportional Strand Transfer ($Q_{\rm de} = 3 H \xi_e \rho_{\rm de}$, `[Model Ansatz — EXPLORATORY]`):**
   In `PART2_RESULTS.md` Section 2(d), we proved that if the static leak assumption (`A7`, $Q = 0$) is replaced by a late-time energy transfer proportional to the dark-energy density,
   $$\dot{\rho}_{\rm dm} + 3H\rho_{\rm dm} = -Q_{\rm de}, \qquad \dot{\rho}_{\rm de} + 3H(1+w_{\rm de})\rho_{\rm de} = +Q_{\rm de}, \qquad Q_{\rm de} = 3 H \xi_e \rho_{\rm de} \qquad \text{[Model Ansatz — EXPLORATORY]}$$
   the dark-energy density stays strictly positive for all $a > 0$ (avoiding the past zero-crossing instability of $Q \propto H\rho_{\rm dm}$), and a coupling $\xi_e \approx 0.015\text{–}0.025$ allows the early-time CMB ratio $\omega_c(z_*)/\omega_b(z_*)$ to differ from the late-time BAO/SN matter density $\Omega_{bc}(z=0)$. However, this still would not cure `T2-N1`/`T2-N2` unless the bare baryon share $\Omega_b = 1/19$ is also modified or interpreted as an effective dressed coupling.
2. **Logarithmic / Two-Scale Cross-Strand Green's Function (`[Model Ansatz — EXPLORATORY]`):**
   As proved by **Theorem 1** (`Section 2.3`), *any* integrable short-range 2D convolution kernel $\mathcal{K}_\sigma(|\mathbf{R}-\mathbf{R}'|)$ whose spatial integral is finite ($\int \mathcal{K}_\sigma d^2R = \mathcal{R}_{\rm pred}$) produces an asymptotic $V_{\rm model}^2(R) \propto M_b/R$ Keplerian fall-off at $R \gg \sigma_{\rm ref}$ with maximum boost $1 + \mathcal{R}_{\rm pred} \approx 6$, which cannot produce flat rotation curves ($V^2 \sim \text{const}$) in low-surface-brightness galaxies. Reproducing flat outer rotation curves without particle dark matter halos requires either a scale-free/logarithmic cross-strand Green's function ($\Phi_{\rm sh} \propto \ln R$ over $R \in [R_d, R_{\rm max}]$) or a non-linear acceleration-dependent coupling analogous to the Radial Acceleration Relation (`McGaugh et al. 2016`), which achieved $M_{\chi^2} = 9.40$ (`fixed`) and $8.43$ (`fitted`) on the same held-out SPARC sample (`Section 4.4`).

---

## 6. Conclusion

By pre-registering and cryptographically timestamping the complete mathematical formulation, data manifest, validation gates, and pass/fail decision rules of the 19-strand Ropewalk Multiverse (`v1`) model prior to touching observational data, we obtained an unambiguous, manipulation-free empirical verdict: **`MODEL FALSIFIED (FAIL)`**. Specifically:
- The bare $1:6:12$ strand partition with $\Omega_b = 1/19$ and static leak $\mathcal{R}_{\rm pred} = 19\Omega_{bc}-1$ is falsified at **$3.58\sigma\text{–}3.87\sigma$** (`T2-A`, `T2-N1`, `T2-N2`) by the combination of `DESI DR2 BAO`, `Planck 2018`, `PDG 2024 BBN`, and Type Ia supernovae (`Pantheon+` and `DES-Dovekie`).
- The single-parameter Unwinding Law 1 ($w(a) = -1 + \gamma_u/E(a)$, $\gamma_u \ge 0$) is **`INCONCLUSIVE`** (`T1-L1`, $\Delta\chi^2 = -1.71$ to $-2.58$ vs $\Lambda$CDM; $+5.46$ to $+7.36$ vs $w_0w_a$CDM), as its non-phantom ray $w_a = -\frac{3}{2}\Omega_{m0}(1+w_0)$ is too shallow to capture the steep $w_a \approx -0.51$ to $-0.62$ tilt preferred by `DESI DR2`.
- Across 16 dissociative galaxy cluster mergers (`T4b`), **0 of 13 classified systems** show weak-lensing mass peaks tracking the X-ray gas rather than the galaxies (`INCONCLUSIVE` on the deciding split with $n_{\rm test}=5<6$; **`FAIL`** on all splits with $n_{\rm test} \ge 6$).
- The 2D Gaussian-smeared shadow-matter rotation-curve kernel (`T5-A` and `T5-B`) is falsified on the 87 held-out SPARC galaxies ($M_{\chi^2} = 45.13$ and $23.74$), bounded by its $1+\mathcal{R}_{\rm pred} = 5.866$ saturation cap.
- Local Hubble-flow expansion (`T6`) across `HEALPix` $N_{\rm side}=1$ Galactic `RING` regions is spatially uniform within $1\sigma$ ($p_{\rm het} = 0.3478$, **`FAIL`**).

All code, frozen parameters, MCMC summary tables, synthetic unit tests, and OpenTimestamps cryptographic proofs (`PREREG_v4.sha256.ots`, `DATA_MANIFEST.sha256.ots`, and `RESULTS_v1.sha256.ots`) are permanently archived in this repository for independent verification.

---

## References

- Bradac, M., et al. 2008, ApJ, 687, 959 (`MACS J0025.4-1222`)
- Brout, D., et al. 2022, ApJ, 938, 110 (`Pantheon+`)
- Chen, L., Huang, Q.-G., & Wang, K. 2019, JCAP, 02, 028 (`Planck 2018` compressed distance priors)
- Cho, H., et al. 2022, ApJ, 925, 68 (`Abell 1240`)
- Clowe, D., et al. 2006, ApJ, 648, L109 (`1E 0657-558` Bullet Cluster)
- Clowe, D., et al. 2012, ApJ, 758, 128 (`Abell 520`)
- Coleman, M., et al. 2017, MNRAS, 467, 3648 (`Abell 2146`)
- Cooke, R. J., Pettini, M., & Steidel, C. C. 2018, ApJ, 855, 102 (`BBN`)
- Danieli, S., et al. 2019, ApJ, 874, L12 (`NGC 1052-DF2`)
- Dawson, W. A., et al. 2012, ApJ, 747, L42 (`DLSCL J0916.2+2951` Musket Ball)
- Dawson, W. A. 2013, ApJ, 772, 131 (`MCMAC` Bullet & Musket Ball dynamics)
- Dawson, W. A., et al. 2015, ApJ, 805, 143 (`CIZA J2242.8+5301`)
- DES Collaboration 2024/2025, ApJ, 973, L14 (`DES-SN5YR` / `Dovekie`)
- DESI Collaboration 2025, arXiv:2503.14738 (`DESI DR2 BAO`)
- Golovich, N., et al. 2016, ApJ, 831, 110 (`MACS J1149.5+2223`)
- Golovich, N., et al. 2017, ApJ, 838, 110 (`ZwCl 0008.8+5215`)
- Harvey, D., et al. 2015, Science, 347, 1462 (`72-subcluster ensemble`)
- Hu, W., & Sugiyama, N. 1996, ApJ, 471, 542 (`Sound horizon & recombination fitting formulas`)
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
- Particle Data Group (Navas, S., et al.) 2024, PRD, 110, 030001 (`PDG 2024 BBN`)
- Planck Collaboration VI 2020, A&A, 641, A6 (`Planck 2018 cosmological parameters`)
- Ragozzine, B., et al. 2012, ApJ, 747, 94 (`Abell 1758N`)
- Riess, A. G., et al. 2022, ApJ, 934, L7 (`SH0ES`)
- van Dokkum, P., et al. 2018, Nature, 555, 629 (`NGC 1052-DF2`)
- White, J. A., et al. 2015, MNRAS, 453, 2718 (`Abell 2146`)
- Wittman, D., Golovich, N., & Dawson, W. A. 2018, ApJ, 869, 104 (`Merger offset catalog`)
