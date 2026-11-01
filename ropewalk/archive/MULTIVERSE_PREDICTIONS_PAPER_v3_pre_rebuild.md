# Pre-Registered Empirical Falsification of the 19-Strand Ropewalk Multiverse Model Across Cosmological and Astrophysical Scales

- **Document:** `MULTIVERSE_PREDICTIONS_PAPER_v3.md` (Version `3.0.0`, Revised Post-Final Independent Review `REVIEW_FINAL.md`)
- **Date:** `2026-10-30`
- **Governing Pre-Registration:** `PREREG.md` (`v1.0.2`), `MULTIVERSE_STAGE1_EQUATIONS.md` (`v1.0.2`), and `ASSUMPTIONS.md` (`v1.0.2`), frozen in `PREREG_v4.sha256` (`53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b`) and OpenTimestamps proof `PREREG_v4.sha256.ots` (calendar-attested `2026-10-30T08:44:36Z`, anchored at Bitcoin block `973800`) prior to data download (`DATA_MANIFEST.sha256` + `DATA_MANIFEST.sha256.ots`, calendar-attested `2026-10-30T08:59:53Z`, anchored at Bitcoin block `973800`).
- **Precedence Clause:** Where `PREREG.md` (`v1.0.2`) and any earlier document disagree, `PREREG.md` (`v1.0.2`) governs. `MULTIVERSE_TESTS_v1.md` is retained as a historical record only.

---

## Abstract

We report the complete, pre-registered empirical evaluation of the 19-strand "Ropewalk" Multiverse model (`v1` static leak formulation), a speculative geometric framework in which our observable universe is one strand of a 19-strand twisted bundle (`1` self strand, `6` nearest-neighbor shadow-matter strands, and `12` outer dark-energy strands). Prior to downloading any observational dataset or writing any analysis code, the model's field-equation mappings (`MULTIVERSE_STAGE1_EQUATIONS.md` `v1.0.2`), assumptions (`A1`–`A20` in `ASSUMPTIONS.md` `v1.0.2`), parameter-fixing rules (`F1`–`F5`), validation gates (`G9-a`–`G9-d`), and pass/fail criteria (`PREREG.md` `v1.0.2`) were frozen and cryptographically timestamped on the Bitcoin blockchain via OpenTimestamps (`PREREG_v4.sha256.ots`, block `973800`), followed by a second cryptographic freeze of the public dataset manifest (`DATA_MANIFEST.sha256.ots`, block `973800`). We test four primary pillars and seven secondary/exploratory predictions against `DESI DR2 BAO` (with joint Ly$\alpha$ `arXiv:2607.27410`), `Planck 2018`, `Pantheon+`, `DES-SN5YR (Dovekie)`, a 16-cluster dissociative merger catalog (`data/MERGERS.csv`), the `SPARC` 175-galaxy rotation-curve database, `NGC 1052-DF2`, and local Hubble-flow regional heterogeneity (`Pantheon+SH0ES`).

Under the pre-registered decision hierarchy (`PREREG.md` Section 3.3, where **at least one** primary pillar ending in `FAIL` falsifies the model), the `v1` Ropewalk Multiverse model is **empirically falsified (`MODEL FALSIFIED (FAIL)`)**, with **two of the four primary pillars ending in `FAIL`**, **two ending in `INCONCLUSIVE`**, and **zero ending in `PASS`**:
1. **Pillar 1 (`T1-L1` — Unwinding Law 1 $w(a) = -1 + \gamma_u/E(a)$):** **`INCONCLUSIVE`**. Because $\gamma_u \ge 0$ restricts the dark-energy equation of state to $w(a) \ge -1$ along the 1D curve $w_a = -\frac{3}{2}\gamma_u[\Omega_m + \gamma_u(1-\Omega_m)]$, it improves slightly over $\Lambda$CDM ($A_r = -1.7119$ on `Pantheon+`, $-2.5780$ on `DES-Dovekie`, $p_{\rm T1\text{-}L1} = 0.190744$) but fits worse than the free two-parameter CPL curve by $B_r = +5.4558$ and $+7.3552$ (against per-run `PASS` thresholds $A_r \le -4.0, B_r \le +4.0$ and per-run `FAIL` thresholds $A_r > -1.0$ or $B_r > +9.0$), landing in the pre-set `INCONCLUSIVE` band.
2. **Pillar 2 (`T2-A` — $1:6:12$ Strand Budget & Leak Ratio):** **`FAIL`**. Fixing the bare baryon share to $\Omega_b = 1/19 = 0.052632$ (`+3.8739σ` above `Planck 2018` $\Omega_b = 0.04930 \pm 0.00086$ in `T2-N1` [`FAIL`], and implying $H_0^{\rm pred} = 65.1943 \pm 0.2186\text{ km s}^{-1}\text{ Mpc}^{-1}$ from `Planck 2018` $100\omega_b = 2.237 \pm 0.015$, `-3.7175σ` below `Planck 2018` $H_0 = 67.36 \pm 0.54$ in `T2-N2` [`FAIL`]) forces the predicted dark-to-baryon ratio $\mathcal{R}_{\rm pred} = 19\Omega_{bc}-1$ (fitted with the conditional $2\times 2$ CMB prior and `DESI DR2 / post-LUNA BBN` $100\omega_b = 2.218 \pm 0.055$) to $4.8658 \pm 0.1149$ (`Pantheon+`, **$3.7430\sigma$** off) and $4.9045 \pm 0.1094$ (`DES-Dovekie`, **$3.5796\sigma$** off) against `Planck 2018` $\omega_c/\omega_b = 5.36 \pm 0.065$ (`FAIL` threshold $> 2.0\sigma_{\rm comb}$ in either run).
3. **Pillar 3 (`T4b` — Cluster Merger Age Cutoff $\tau_{\rm lag}$):** **`INCONCLUSIVE`**. Training on the 8 odd-indexed clusters fixes $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ ($\text{Acc}_{\rm train} = 7/8 = 87.5\%$). Because only $n_{\rm test} = 5$ of the 8 held-out even-indexed clusters are classified at $> 2\sigma_{\rm diff}$ confidence and `PREREG.md` §5.5 (`Rule G8(3)`) requires $n_{\rm test} \ge 6$, the deciding test is `INCONCLUSIVE` ($\text{Acc}_{\rm test} = 3/5 = 60.0\%$, raw $p = 0.5000$, Holm $p = 1.0000$). Across all 13 classifiable clusters in the 16-cluster sample, including the three oldest collisions at $1.10, 1.16$, and $1.50\text{ Gyr}$, the weak-lensing mass peak stayed with the galaxies (`13/13`), never with the gas as the model predicted for old collisions; a registered alternate lensing source for `Abell 1758N` (`S6`, `Ragozzine et al. 2012`) gives $n_{\rm test} = 6$ and would have made `T4b` a `FAIL`.
4. **Pillar 4 (`T5-A` — Universal Refraction Halo Width $\sigma_{\rm ref}$ on SPARC):** **`FAIL`**. Minimizing $\sum \chi^2_{{\rm red},g}$ across the 88 odd-indexed training galaxies under the 3D Gaussian enclosed-mass error-function kernel $\mathcal{F}_\sigma(r, r')$ fixes $\hat{\sigma}_{\rm ref} = 9.212795\text{ kpc}$, which yields a held-out median reduced chi-squared $M_{\chi^2} = 45.1259 > 3.0$ and fraction $F_{<2} = 0.0690 < 0.40$ (`6/87`, where passing required $M_{\chi^2} \le 1.5$ and $F_{<2} \ge 0.70$) across the 87 even-indexed test galaxies (and `FAIL` for the disk-scaled secondary test `T5-B` with $\hat{k} = 2.928045$, $M_{\chi^2} = 23.7412$, $F_{<2} = 0.0805$ [`7/87`]). For outward-decreasing spherical baryon density, 3D Gaussian diffusion bounds $g_{\rm tot}(r)/g_{\rm bar}(r) \le 1 + \mathcal{R}_{\rm pred} = 5.8658$; **67 of 175 SPARC galaxies (`38.29%`) have at least one radial point where the observed boost exceeds this 5.8658 maximum, which is 442 of all 3391 radial points (`13.03%`)**.

Among secondary tests, the directional check `T1-Sign` ($P(w_0 > -1) = 0.9960$ and $0.9992$, known prior to the test and unable to rescue `T1-L1`) and the `NGC 1052-DF2` 3D Plummer enclosed-mass check `T5c` ($M_{\rm pred}(<2.7\text{ kpc}) = 0.9877 \times 10^8 M_\odot \le 2.9 \times 10^8 M_\odot$, which passes only because the wide $9.21\text{ kpc}$ blur that failed `T5-A` spreads the shadow mass thin) end in **`PASS`**, whereas the regional $H_0$ heterogeneity test `T6` across 9 `HEALPix` $N_{\rm side}=1$ Galactic `RING` regions (`491` supernovae in $0.023 \le z_{\rm HD} \le 0.15$) ends in **`FAIL`** ($\chi^2_{\rm het} = 8.9347$, $\text{dof}=8$, $p_{\rm het} = 0.347838 > 0.3173$, with no regional variation detected at this resolution).

---

## 1. Introduction & Pre-Registration Architecture

Speculative cosmological models that aim to unify dark matter and dark energy through geometric or extra-dimensional ansätze require explicit pre-registration so that parameter-fixing rules, datasets, and pass/fail thresholds are locked before seeing the test outcomes. This study was conducted under a four-stage pre-registered protocol (`PREREG.md` `v1.0.2`), with rules frozen and timestamped before data download, one logged runtime deviation (`D1`), one post-hoc review-logged deviation (`D2`), and cluster inputs hand-extracted by the analyst (`Section 6`):

1. **Stage 1 (Theoretical Formulation & Cryptographic Pre-Registration):** Every equation in the model was derived from explicit assumptions (`A1`–`A20` in `ASSUMPTIONS.md` `v1.0.2`), classified as either `[Established]` (standard general relativity, FLRW cosmology, and Newtonian potential theory) or `[Model Ansatz]` (specific to the 19-strand Ropewalk hypothesis), and revised through three rounds of pre-data independent review (`REVIEW_COLD.md`, `REVIEW_V2.md`, `REVIEW_V3.md`). All forks were closed so that every scored test had a single mechanical deciding rule. The complete Stage 1 specification (`PREREG.md` `v1.0.2`, `MULTIVERSE_STAGE1_EQUATIONS.md` `v1.0.2`, `ASSUMPTIONS.md` `v1.0.2`, and `STAGE1_PART1`–`PART3`) was hashed into `PREREG_v4.sha256` (`53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b`) and anchored via OpenTimestamps (`PREREG_v4.sha256.ots`, calendar-attested `2026-10-30T08:44:36Z`, Bitcoin block `973800`) before any observational data were downloaded or any analysis code was written.
2. **Stage 2 (Data Freeze, Validation Gates, and Parameter Fixing):** Public observational datasets were downloaded (`08:56Z`) and frozen in `DATA_MANIFEST.sha256` (`73135698afb833e7e95e6a85c55475480132300e29f8b7b42d159c037067896d`) and `DATA_MANIFEST.sha256.ots` (`08:59:53Z`, Bitcoin block `973800`) prior to any fitting. The numerical codebase (`scripts/cosmology.py`, `scripts/sparc_t5.py`) was checked against four validation gates (`G9-a` through `G9-d`, saved in `results/validation_gates_g9.json` and re-verified on the final refactored code in `results/validation_gates_g9_final.json`). Each model free parameter ($f_{\rm leak}$, $\tau_{\rm lag}$, $\sigma_{\rm ref}$, $k$, and $M_B$) was fitted on its designated training dataset and locked in `results/FIXED_VALUES.json` (`results/FREEZE_T1.json`–`FREEZE_T6.json`).
3. **Stage 3 (Execution of Scored & Exploratory Tests):** All primary pillar tests (`T1-L1`, `T2-A`, `T4b`, `T5-A`), secondary scored tests (`T1-Sign`, `T2-N1`, `T2-N2`, `T5-B`, `T5c`, `T6`), sensitivity analyses, and Holm–Bonferroni multiple-testing corrections were computed from the frozen parameters (`results/results.json`).
4. **Stage 4 (Independent Review & Final Cryptographic Stamp):** An independent reviewer (`REVIEW_FINAL.md`) re-derived every deciding statistic and verdict from the frozen rulebook and public data, and identified documentation and process corrections (`M1`–`M7`, `m1`–`m7`), all of which are incorporated in this `v3` paper and stamped in `RESULTS_v2.sha256` + `RESULTS_v2.sha256.ots`.

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

Using weak-lensing convergence peak (`I`), galaxy (`S`), and X-ray gas peak (`G`) positions (`data/MERGERS.csv`), each primary subcluster's separations $d_{IS} = |\mathbf{x}_I - \mathbf{x}_S|$ and $d_{IG} = |\mathbf{x}_I - \mathbf{x}_G|$ are classified via the quadrature-sum uncertainty (`PREREG.md` §5.5 item 4, `[Established]`):
$$\sigma_{\rm diff} = \sqrt{\sigma_I^2 + \sigma_G^2 + \sigma_S^2}$$
into `"with_galaxies"` ($d_{IG} - d_{IS} > 2\sigma_{\rm diff}$), `"with_gas"` ($d_{IS} - d_{IG} > 2\sigma_{\rm diff}$), or `"unclassified"` ($|d_{IG} - d_{IS}| \le 2\sigma_{\rm diff}$).

### 2.5 Regional Hubble-Flow Heterogeneity (`T6`)

Under `Assumptions A10, A20` (`MULTIVERSE_STAGE1_EQUATIONS.md` §8.1 & `PREREG.md` §5.7), `T6` partitions the `Pantheon+SH0ES` non-calibrator Hubble-flow supernovae ($0.023 \le z_{\rm HD} \le 0.15$, `IS_CALIBRATOR == 0`) into the 12 `HEALPix` $N_{\rm side}=1$ Galactic $(l, b)$ `RING` pixels. In a single pre-fit pass in increasing `RING` order $i \in \{0, \dots, 11\}$, any pixel with $0 < N_{{\rm SN},i} < 10$ is merged into its edge-sharing neighbor pixel of lowest `RING` index (`4->0, 7->2, 11->4`), and any pixel remaining $< 10$ after that pass is dropped, leaving $N_{\rm pix}$ regions. Using the full non-diagonal Hubble-flow covariance block $\mathbf{C}_{\rm HF}$ (`(g4)`), the generalized least-squares (`GLS`) heterogeneity statistic `[Established]`
$$\chi^2_{\rm het} = \left(\hat{\mathbf{H}}_0 - \bar{H}_0\,\mathbf{1}\right)^T \mathbf{C}_{H_0}^{-1} \left(\hat{\mathbf{H}}_0 - \bar{H}_0\,\mathbf{1}\right) \quad (\text{dof} = N_{\rm pix} - 1) \qquad \text{[Established, (g4)]}$$
tests whether local Hubble-flow expansion exhibits significant regional variation.

---

## 3. Data Freeze, Validation Gates, and Parameter Freeze

All primary public datasets were downloaded and hashed in `DATA_MANIFEST.sha256` (`73135698afb833e7e95e6a85c55475480132300e29f8b7b42d159c037067896d`) and stamped with OpenTimestamps (`DATA_MANIFEST.sha256.ots`, block `973800`) before any fit:
- **`DESI DR2 BAO`:** `desi_gaussian_bao_ALL_GCcomb_mean.txt` and `desi_gaussian_bao_ALL_GCcomb_cov.txt` ($13 \times 13$ Gaussian BAO mean vector and covariance matrix from `DESI Collaboration 2025b`, `arXiv:2503.14738`), with the $z_{\rm eff} = 2.33$ Ly$\alpha$ row replaced in the deciding `T1` and `T2` runs by the joint Ly$\alpha$ BAO+AP measurement (`8.600 ± 0.066`, `39.32 ± 0.33`, $r_{D_H,D_M} = -0.431$) from `DESI Collaboration (2026, arXiv:2607.27410)`.
- **`Pantheon+` & `SH0ES`:** `Pantheon+SH0ES.dat` ($1701$ light-curve rows; $1580$ non-calibrator cosmology SNe with $z_{\rm HD} > 0.01$ and `IS_CALIBRATOR == 0`; $77$ Cepheid calibrators with `IS_CALIBRATOR == 1`; $496$ non-calibrator Hubble-flow SNe in $0.023 \le z_{\rm HD} \le 0.15$) and `Pantheon+SH0ES_stat+sys.cov` (`Brout et al. 2022`, `Riess et al. 2022`).
- **`DES-SN5YR Dovekie`:** `DES-Dovekie_HD.csv` ($1820$ SNe Ia) and `STAT+SYS.npz` (`Popovic et al. 2025`).
- **`Planck 2018` Compressed Likelihood & Registered Priors:** `Chen, Huang & Wang (2019)` Table 1 ($\Lambda$CDM and $w$CDM) $(R, \ell_A, 100\omega_b)$ distance priors, `DESI DR2 / post-LUNA BBN` ($100\omega_b = 2.218 \pm 0.055$), `Cooke+18 BBN` ($100\omega_b = 2.166 \pm 0.019$), and `Planck 2018` parameters ($\Omega_b = 0.04930 \pm 0.00086$, $100\omega_b = 2.237 \pm 0.015$, $H_0 = 67.36 \pm 0.54$), stored in `data/registered_priors.json`.
- **Galaxy Clusters & Rotation Curves:** `data/MERGERS.csv` ($16$ dissociative cluster mergers) + `Wittman, Golovich & Dawson (2018, ApJ 869, 104)` Table 1 (`11` subclusters) and `data/sparc/MassModels_Lelli2016c.mrt` + `SPARC_Lelli2016c.mrt` ($175$ galaxies, $3391$ radial points).

All four validation gates passed on both the initial pre-fit codebase (`results/validation_gates_g9.json`) and the final refactored codebase (`results/validation_gates_g9_final.json`): `G9-a` ($0.0373\sigma \le 0.30\sigma$), `G9-b` ($0.0254\sigma \le 0.30\sigma$), `G9-c` ($0.3608\sigma$ on $w_0$, $0.4257\sigma$ on $w_a \le 1.0\sigma$), and `G9-d` (max absolute error $1.4397 \times 10^{-11} < 10^{-10}$ against `scipy.stats.ncx2.cdf`).

---

## 4. Empirical Results & Failure Analysis

### 4.1 Cosmological Expansion (`T1-L1` `INCONCLUSIVE`, `T1-Sign` `PASS`)

Fitting Unwinding Law 1 ($w(a) = -1 + \gamma_u/E(a)$, $\gamma_u \ge 0$), flat $\Lambda$CDM, and CPL $w_0w_a$CDM to `DESI DR2 BAO (joint Lyα) + Planck 2018 ΛCDM Table 1 + SN` yields (`results/results.json["T1"]`):
- **`Pantheon+`:** $\chi^2_{\min}(\Lambda\text{CDM}) = 1405.3436$, $\chi^2_{\min}(\text{Law 1}) = 1403.6318$ ($\hat{\gamma}_u = 0.038481$, posterior median $\gamma_u = 0.042946 \pm 0.026160$, implied $w_0 = -0.957054 \pm 0.026160$, $w_a = -0.021748 \pm 0.014720$), $\chi^2_{\min}(w_0w_a\text{CDM}) = 1398.1760$ ($w_0 = -0.854092 \pm 0.055958$, $w_a = -0.513975 \pm 0.215181$). Thus $A_{\rm P+} = -1.7119$ and $B_{\rm P+} = +5.4558$.
- **`DES-Dovekie`:** $\chi^2_{\min}(\Lambda\text{CDM}) = 1650.9615$, $\chi^2_{\min}(\text{Law 1}) = 1648.3835$ ($\hat{\gamma}_u = 0.043843$, posterior median $\gamma_u = 0.045401 \pm 0.025781$, implied $w_0 = -0.954599 \pm 0.025781$, $w_a = -0.023131 \pm 0.014626$), $\chi^2_{\min}(w_0w_a\text{CDM}) = 1641.0283$ ($w_0 = -0.825007 \pm 0.055675$, $w_a = -0.615279 \pm 0.222775$). Thus $A_{\rm Dov} = -2.5780$ and $B_{\rm Dov} = +7.3552$.

While the secondary directional check `T1-Sign` passes ($P(w_0 > -1) = 0.995984$ on `Pantheon+` and $0.999219$ on `DES-Dovekie`, with $\sigma_{w_0} \approx 0.056 > 0.03$), that result was already known from published DESI DR2 data and cannot rescue the main dark-energy test. In `T1-L1`, the fitted Law 1 slope ($w_a = -0.0217$ and $-0.0231$) is **23.6 to 26.6 times shallower** than the free CPL fits ($w_a = -0.5140$ and $-0.6153$). Law 1 improves slightly over $\Lambda$CDM ($A_r = -1.7119$ and $-2.5780$, $p_{\rm T1\text{-}L1} = 0.190744$) but fits worse than the free two-parameter curve by $B_r = +5.4558$ and $+7.3552$, landing in the pre-set **`INCONCLUSIVE`** band ($-4.0 < A_r \le -1.0$ and $+4.0 < B_r \le +9.0$) across both deciding runs and all 6 sensitivity runs (`Figure 1`).

### 4.2 Strand Budget & Leak Ratio (`T2-A` `FAIL`, `T2-N1` `FAIL`, `T2-N2` `FAIL`)

Evaluating the $1:6:12$ strand budget and static leak relation $\mathcal{R}_{\rm pred} = 19\Omega_{bc} - 1$ (`(c4)`) falsifies Pillar 2 across every deciding and sensitivity variant (`Figure 2`):
1. **Bare Baryon Share (`T2-N1`):** $\Omega_b^{\rm model} = 1/19 = 0.052632$ sits **$+3.8739\sigma$** (`+6.76%`, i.e., `6.8%` higher) above `Planck 2018` $\Omega_b = 0.04930 \pm 0.00086$ (`FAIL` threshold $> 2.0\sigma$).
2. **Implied Hubble Constant (`T2-N2`):** Combining $\Omega_b = 1/19$ with the deciding `Planck 2018` physical baryon density $100\omega_b = 2.237 \pm 0.015$ gives $H_0^{\rm pred} = 65.1943 \pm 0.2186\text{ km s}^{-1}\text{ Mpc}^{-1}$, which sits **$-3.7175\sigma$** below `Planck 2018` $H_0 = 67.36 \pm 0.54\text{ km s}^{-1}\text{ Mpc}^{-1}$ ($\sigma_{\rm comb} = 0.5826$, `FAIL` threshold $> 2.0\sigma$) and moves away from the local Hubble value near $73\text{ km s}^{-1}\text{ Mpc}^{-1}$.
3. **Leaked Dark-to-Baryon Ratio (`T2-A` Primary Pillar 2):**
   - `Pantheon+` (with `DESI DR2 / post-LUNA BBN` $100\omega_b = 2.218 \pm 0.055$ and conditional $2\times 2$ CMB prior; $\max|\hat{R}-1| = 0.001109$, $\min\text{ESS} = 1909.9$): $\Omega_{bc} = 0.308725 \pm 0.006049 \implies f_{\rm leak} = 0.189038 \pm 0.019155$ and $\mathcal{R}_{\rm pred} = 4.8658 \pm 0.1149$ ($\sigma_{\rm comb} = 0.13204$), which is **$3.7430\sigma$** below `Planck 2018` $\mathcal{R}_{\rm Planck} = 5.36 \pm 0.065$ (`> 2.0σ` $\implies$ **`FAIL`**).
   - `DES-Dovekie` ($\max|\hat{R}-1| = 0.000671$, $\min\text{ESS} = 1890.7$): $\Omega_{bc} = 0.310765 \pm 0.005757 \implies f_{\rm leak} = 0.182578 \pm 0.018231$ and $\mathcal{R}_{\rm pred} = 4.9045 \pm 0.1094$ ($\sigma_{\rm comb} = 0.12724$), which is **$3.5796\sigma$** below `Planck 2018` (`> 2.0σ` $\implies$ **`FAIL`**).
   - Every alternative sensitivity version (`T2-B` constrained $\omega_b = h^2/19$ at $2.4619\sigma$ and $2.3284\sigma$ with $\Delta\chi^2 = +9.8219 > 9$; `Cooke+18 BBN` at $3.0723\sigma$ and $2.8242\sigma$; marginal $2\times 2$ CMB at $3.5222\sigma$ and $3.5065\sigma$) also misses by more than $2\sigma$ (`2.33σ` to `3.52σ`, all `FAIL`).

### 4.3 Cluster Merger Relaxation Cutoff (`T4b` `INCONCLUSIVE`, `T4a` `EXPLORATORY`)

Across the 16 dissociative galaxy cluster mergers in `data/MERGERS.csv` (`Figure 3`), 13 primary subclusters are classified at $> 2\sigma_{\rm diff}$ confidence (`8` in the odd-indexed training set and `5` in the even-indexed test set), and 3 even-indexed test clusters (`#4 Abell 1758N`, `#8 Abell 3376`, `#16 ZwCl 0008`) are `"unclassified"` ($|d_{IG}-d_{IS}| \le 2\sigma_{\rm diff}$).
- **Deciding Split Outcome (`INCONCLUSIVE`):** Training on the 8 odd-indexed clusters over $[235, 1500]\text{ Myr}$ (with smallest-$\tau_{\rm lag}$ tie-breaking on the $(800, 1500]\text{ Myr}$ plateau) fixes $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ ($\text{Acc}_{\rm train} = 7/8 = 87.5\%$). On the held-out even-indexed test set, $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ classifies $k = 3$ of $n_{\rm test} = 5$ systems correctly ($\text{Acc}_{\rm test} = 60.0\%$, raw $p = 0.5000$, Holm $p = 1.0000$). Because $n_{\rm test} = 5 < 6$ and `PREREG.md` §5.5 (`Rule G8(3)`) requires $n_{\rm test} \ge 6$ to trigger either `PASS` or `FAIL` Clauses `1(b)`/`1(c)`, the deciding verdict for `T4b` is **`INCONCLUSIVE`**.
- **Complete Absence of Old `"with_gas"` Mergers & Sensitivity Checks:** In all 13 classifiable clusters (`8` train + `5` test), including the three oldest collisions (`#12 Musket Ball` at $1.10\text{ Gyr}$, `#14 MACS J1149` at $1.16\text{ Gyr}$, and `#15 Toothbrush` at $1.50\text{ Gyr}$), the dark mass stayed with the galaxies (`13/13`), never with the gas as the model predicted for old collisions. A registered non-deciding sensitivity check using the alternate `Ragozzine et al. (2012, ApJ 747, 18)` lensing position for `Abell 1758N` (`S6`, $n_{\rm test} = 6$) would have made `T4b` a `FAIL` via Clause `1(c)`, and the registered `Abell 520` `P3` dark-core check (`S4`) gives `FAIL` via Clause `1(a)` ($\text{Acc}_{\rm train} = 75.0\% < 80\%$). (`S7`, the First-8/Last-8 split, was not registered in `PREREG.md` and is an unregistered post-hoc check.)
- **Exploratory Young-Merger Offset Sign (`T4a`):** `PREREG.md` §5.4 locked `T4a` as exploratory before data analysis because under the physical symmetric harmonic trajectory `A13b` (`(e6)`), the model predicts a negative offset for $0 < T \lesssim \frac{2}{3}\tau_{\rm lag}$ and does not predict a uniform positive sign across all young mergers, and because excluding the Bullet Cluster from `Wittman, Golovich & Dawson (2018, ApJ 869, 104)` Table 1 leaves only $N=1$ subcluster (`A2744 S`, $t_{\rm col} = 120\text{ Myr}$) with $t_{\rm col} \le 235\text{ Myr}$ (or $\le 400\text{ Myr}$), where $\Delta_{SI}^{\parallel} = -45.0 \pm 52.0\text{ kpc}$ ($-0.8654\sigma$; all 10 non-Bullet subclusters: $\bar{\Delta}_{SI}^{\parallel} = -43.7569 \pm 23.7576\text{ kpc}$, $-1.8418\sigma$).

### 4.4 Galactic Rotation Curves & Ultra-Diffuse Galaxies (`T5-A` `FAIL`, `T5-B` `FAIL`, `T5c` `PASS`)

Evaluating the 3D Gaussian enclosed-mass error-function kernel $\mathcal{F}_\sigma(r, r')$ (`(f3)`) across the 175 SPARC galaxies (`Figure 4`) yields:
- **Primary Pillar 4 (`T5-A`, Universal $\sigma_{\rm ref}$):** Minimizing $\sum \chi^2_{{\rm red},g}$ across the 88 odd-indexed training galaxies fixes $\hat{\sigma}_{\rm ref} = 9.212795\text{ kpc}$ ($\text{train } M_{\chi^2} = 48.5128$, $F_{<2} = 0.0341$ [`3/88`]). Tested on the 87 unseen even-indexed galaxies, `T5-A` fits only 6 of the 87 acceptably ($F_{<2} = 0.0690 < 0.40$, where passing needed $F_{<2} \ge 0.70$) with a median reduced chi-squared **$M_{\chi^2} = 45.1259 > 3.0$** (where passing needed $M_{\chi^2} \le 1.5$; pooled $\chi^2_{\rm red} = 324.2171$), resulting in a decisive **`FAIL`**. Even choosing the best possible universal width directly on the held-out set only reaches a median reduced chi-squared of $\sim 37$, confirming this is not a tuning problem.
- **Secondary Disk-Scaled Width (`T5-B`, $\sigma_{{\rm ref},g} = k R_{d,g}$):** Training fixes $\hat{k} = 2.928045$ ($\text{train } M_{\chi^2} = 25.0021$, $F_{<2} = 0.0568$ [`5/88`]). On the 87 unseen test galaxies, `T5-B` yields **$M_{\chi^2} = 23.7412 > 3.0$** and **$F_{<2} = 0.0805 < 0.40$** (`7/87`, pooled $\chi^2_{\rm red} = 234.6098$), also ending in **`FAIL`**. All sensitivity loss functions (`total_chi2`, `median_chi2_red`) and $f_{\rm leak} = 1/6$ likewise end in **`FAIL`**.
- **Saturation Cap Diagnostic (`(f3)`):** Under the 3D Gaussian kernel, outward-decreasing spherical baryon density bounds $g_{\rm tot}(r)/g_{\rm bar}(r) \le 1 + \mathcal{R}_{\rm pred} = 5.8658$. Across SPARC, **67 of 175 galaxies (`38.29%`) have at least one radius where the observed boost $V_{\rm obs}^2(r)/V_{\rm bar}^2(r)$ exceeds the model's 5.8658 maximum, which is 442 of all 3391 radial points (`13.03%`)**.
- **Secondary `NGC 1052-DF2` Stress Check (`T5c`):** Using the registered 3D Plummer profile ($M_{*,{\rm DF2}} = 2.0 \times 10^8 M_\odot$, $R_e = 2.2\text{ kpc}$) plus external `NGC 1052` group mass at the frozen $\hat{\sigma}_{\rm ref} = 9.212795\text{ kpc}$, the predicted enclosed mass is $M_{\rm pred}(<2.7\text{ kpc}) = 0.9877 \times 10^8 M_\odot \le 2.9 \times 10^8 M_\odot$ and $M_{\rm pred}(<3.1\text{ kpc}) = 1.1686 \times 10^8 M_\odot < 3.2 \times 10^8 M_\odot$, ending in **`PASS`** — but only because the same wide $9.21\text{ kpc}$ blur that failed the SPARC rotation curves spreads DF2's shadow mass thin.

### 4.5 Regional Hubble-Flow Heterogeneity (`T6` `FAIL`) and Cosmic Coincidence Window (`Section 6`)

- **Regional $H_0$ Heterogeneity (`T6`, `Figure 5a`):** Across the $N_{\rm pix} = 9$ retained `HEALPix` $N_{\rm side}=1$ Galactic `RING` regions (`491` Hubble-flow SNe in $0.023 \le z_{\rm HD} \le 0.15$ after single-pass lowest-`RING`-index edge-neighbor merging `4->0, 7->2, 11->4` and dropping pixel `4` with `5` SNe), regional $H_{0,k}$ values range from $72.5255$ to $75.0888\text{ km s}^{-1}\text{ Mpc}^{-1}$ (per-region Hubble-flow errors $0.4665$ to $1.1821\text{ km s}^{-1}\text{ Mpc}^{-1}$; all-sky GLS mean $\bar{H}_0 = 73.5056 \pm 0.2419\text{ (HF)} \pm 1.0474\text{ (tot) km s}^{-1}\text{ Mpc}^{-1}$, $Z_{\rm all\text{-}sky} = 5.2152\sigma$ above `Planck 2018`). The GLS heterogeneity statistic is $\chi^2_{\rm het} = 8.9347$ ($\text{dof}=8$), giving $p_{\rm het} = 0.347838 > 0.3173$, which triggers a **`FAIL`**. No regional variation is detected at this resolution (while the non-deciding Equatorial and $z_{\rm CMB}$ sensitivity variants gave $p_{\rm het} = 0.140621$ and $0.062968$, both `INCONCLUSIVE`).
- **Cosmic Coincidence Window (`Section 6`, `Figure 5b`):** Under `Planck 2018` $\Lambda$CDM expansion ($t_0 = 13.8005\text{ Gyr}$), the cosmic density shares $\Omega_i(a)$ match the Ropewalk target partition to within $5\%$ absolute error (`H-Abs`) for $\Delta t_{\rm abs} = 2.2549\text{ Gyr}$ (`16.34%` of $t_0$) and to within $10\%$ relative error (`H-Rel`) for $\Delta t_{\rm rel} = 0.9269\text{ Gyr}$ (`6.72%` of $t_0$) for $f_{\rm leak} = 1/6$ ($\Delta t_{\rm abs} = 2.2956\text{ Gyr}$ [`16.63%`] and $\Delta t_{\rm rel} = 0.7308\text{ Gyr}$ [`5.30%`] for $f_{\rm leak} = 0.189038$).

---

## 5. Candidate Exploratory Extensions for a Future `v2` Model (`EXPLORATORY`)

Per our pre-registration rules (`GEMINI.md` Rule 2 and `PREREG.md`), no unregistered mechanism or parameter may be used to alter, soften, or rescue any `v1` test verdict (`MODEL FALSIFIED (FAIL)`). Two strictly **EXPLORATORY** mathematical extensions derived during Stage 1 (`MULTIVERSE_STAGE1_EQUATIONS.md` §5.4 and §8.3) are recorded solely for potential future out-of-sample testing:

1. **Dynamic Vacuum-Proportional Strand Transfer ($Q_{\rm de} = \xi_e H \rho_{\rm de}$, `[Model Ansatz — EXPLORATORY, §5.4 (d-Exp)]`):**
   Combining bare unwinding $w_{\rm bare}(a) = -1 + \gamma_u/E(a)$ with dark-sector energy transfer $Q_{\rm de} = \xi_e H \rho_{\rm de}$ ($\xi_e > 0$) yields $w_{\rm de}^{\rm eff}(a) = -1 + \gamma_u/E(a) - \xi_e/3$, which remains perturbation-stable ($d < 0$) and allows an effective phantom crossing ($w_{\rm de}^{\rm eff} = -1$) at $E(z_{\rm cross}) = 3\gamma_u/\xi_e$ while keeping $\rho_{\rm de}(a) > 0$ at all $a > 0$. However, it adds an unregistered parameter $\xi_e$ and does not resolve the bare $\Omega_b = 1/19$ tension in `T2-N1`/`T2-N2`.
2. **Smooth Far-String Shadow Component ($\epsilon_{\rm far}$, `[Model Ansatz — EXPLORATORY, §8.3 (i-Exp)]`) and Non-Gaussian Galaxy Kernel:**
   Because any normalized 3D Gaussian kernel $K_\sigma$ enforces the saturation cap $g_{\rm tot}(r)/g_{\rm bar}(r) \le 1 + \mathcal{R}_{\rm pred} = 5.8658$ whenever $d\bar{\rho}_b/dr \le 0$, reproducing flat outer rotation curves in low-surface-brightness galaxies requires replacing the 3D Gaussian kernel with a scale-free/logarithmic cross-strand potential or an acceleration-dependent coupling analogous to the Radial Acceleration Relation (`McGaugh et al. 2016`), which achieved held-out $M_{\chi^2} = 9.4001$ (`fixed`) and $8.4263$ (`fitted`) on the same SPARC sample.

---

## 6. Limitations & Process Record (`REVIEW_FINAL M1, M3, M7, m1–m4, m7`)

We state the methodological scope and process limitations of this execution plainly, without claiming the study was "fully blind", "manipulation-free", or had "zero researcher freedom":

1. **Pre-Data Cryptographic Freeze:** The governing rulebook (`PREREG.md` `v1.0.2`), mathematical formulation (`MULTIVERSE_STAGE1_EQUATIONS.md` `v1.0.2`), and assumptions (`ASSUMPTIONS.md` `v1.0.2`) were hashed in `PREREG_v4.sha256` (`53ce966a...`) and calendar-attested via OpenTimestamps (`2026-10-30T08:44:36Z`, anchored at Bitcoin block `973800`) prior to data download (`08:56Z`) and prior to the dataset manifest freeze `DATA_MANIFEST.sha256` (`08:59:53Z`, also anchored at Bitcoin block `973800`).
2. **Cluster Sample Compilation, Post-Freeze Source Archives, and Hand-Extraction (`T4b`):**
   - As disclosed in `PREREG.md` Section 5.5 (`N10`), the 16-cluster merger catalog was compiled from the literature by an analyst with prior knowledge of well-known dissociative mergers.
   - The 8 replacement arXiv TeX/PDF cluster source archives in `data/clusters_arxiv_exact/` (`DEVIATIONS.md` entry `D1`, `2026-10-30T05:17:04` local) were downloaded after `DATA_MANIFEST.sha256` was frozen (`04:59:52` local) and are therefore covered by `RESULTS_v2.sha256` rather than the pre-fit `DATA_MANIFEST.sha256`.
   - Both the training-half and test-half cluster positions and uncertainties in `data/MERGERS.csv` were hand-extracted by the analyst (`05:24:22`, revised `05:31:50` local) before $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ was frozen (`06:29:35` local).
   - As documented in `DEVIATIONS.md` (`D2`, identified during final review), `data/MERGERS.csv` set $\sigma_S = 0.0\text{ kpc}$ for `Abell 1758N` (test), `Abell 2034` (train), and `Abell 3376` (test) instead of marking those rows `"unclassified"` under `PREREG.md` §5.5 item 5, and assigned $\sigma_G = 5.0\text{ kpc}$ to five clusters. As verified by the independent reviewer (`REVIEW_FINAL.md` §3 `M3`), applying `PREREG.md` §5.5 item 5 strictly (and/or dropping the $\sigma_G = 5.0\text{ kpc}$ clusters) leaves $\hat{\tau}_{\rm lag} = 805\text{ Myr}$, $n_{\rm test} \le 5$, and the `INCONCLUSIVE` verdict unchanged.
3. **Post-Gate Code Refactoring and Re-Verification (`M1`):**
   - The initial validation gate run (`results/validation_gates_g9.json`, `05:02:56` local) was executed before `scripts/cosmology.py` was refactored (`05:39:33` to `06:28:52` local) to add vectorized quadrature and pre-inverted covariance routines (`joint_chi2_cpl`, `joint_chi2_law1`). Re-running all four validation gates on the final unmodified scripts (`scripts/run_gates_g9_final.py` $\to$ `results/validation_gates_g9_final.json`) confirmed that all four gates pass on both the standard and fast likelihood paths.

---

## 7. What Changes for the Film (`REVIEW_FINAL.md` Section 4)

### Safe for Narration (10 Verified Points)
1. Under the rules frozen before any data were touched, version 1 of the model is falsified: of its four deciding tests, two failed, two were inconclusive and none passed.
2. The model's core number, ordinary matter as exactly 1 part in 19 (5.26%), sits 3.9 sigma above Planck's measured 4.93% ± 0.09%.
3. The predicted dark-to-ordinary matter ratio came out at 4.87 (Pantheon+) and 4.90 (DES) against Planck's 5.36 ± 0.07. That is 3.7 and 3.6 sigma off, where the pre-set failure line was 2 sigma, and every alternative version also missed by more than 2 sigma (2.3 to 3.5).
4. The 1-in-19 rule implies a Hubble constant of 65.2 ± 0.2 km/s/Mpc, 3.7 sigma below Planck's 67.4 and moving away from the local value near 73, not toward it.
5. One shadow-blur width (9.2 kpc), fitted on 88 galaxies and tested on 87 unseen ones, fit only 6 of the 87 acceptably (median misfit 45 where passing needed 1.5 or less). The galaxy-scaled version also failed (median 24, 7 of 87), and even the best possible width only reached 37, so this is not a tuning problem.
6. The model's dark-energy curve fit slightly better than a plain cosmological constant (improvement 1.7 and 2.6 in chi-square, not significant, p = 0.19) but worse than the free two-parameter curve (by 5.5 and 7.4). That lands in the pre-set "inconclusive" band: not confirmed, not ruled out.
7. The cluster test is inconclusive because only 5 of the 8 held-out clusters could be classified and the rule needed 6. In all 13 classifiable clusters, including the three oldest collisions at 1.1, 1.2 and 1.5 billion years, the dark mass stayed with the galaxies, never with the gas as the model predicted for old collisions.
8. Across 9 sky regions (491 supernovae) the local Hubble constant ranged from 72.5 to 75.1 km/s/Mpc, with no regional variation detected (p = 0.35), so the "local patchwork" explanation of the Hubble tension failed its test. The local all-sky value, 73.5 ± 1.0, is 5.2 sigma above Planck, an overall offset rather than a patchwork.
9. Two side checks passed, with caveats. Dark energy's present value is above −1 (99.6% and 99.9% probability), but that was known before the test and cannot rescue the main dark-energy test. The dark-matter-poor galaxy NGC 1052-DF2 is predicted correctly (0.99 against a limit of 2.9 hundred-million suns), but only because the same wide blur that failed the rotation curves spreads the shadow mass thin.
10. The rulebook and the data list were hashed and anchored to the Bitcoin blockchain (block 973800) before any test ran, and an independent review re-derived every verdict from the files and the public data.

### Do NOT Say
- That falsification required two failed pillars. One suffices.
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

## 8. Conclusion

Under the rules frozen and anchored to the Bitcoin blockchain (`PREREG_v4.sha256.ots` and `DATA_MANIFEST.sha256.ots`, block `973800`) before any test was run, version 1 of the 19-strand Ropewalk Multiverse model is falsified (`MODEL FALSIFIED (FAIL)`): two of its four deciding pillar tests failed (`T2-A` and `T5-A`), two were inconclusive (`T1-L1` and `T4b`), and none passed. Every deciding statistic and verdict has been independently reproduced from the frozen rulebook and hash-verified public data (`REVIEW_FINAL.md`).

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
- White, J. A., et al. 2015, MNRAS, 453, 2326 (`Abell 2146`)
- Wittman, D., Golovich, N., & Dawson, W. A. 2018, ApJ, 869, 104 (`Merger offset catalog, Table 1`)
