# Ropewalk Multiverse Empirical Test Suite — Final Technical Report (`RESULTS.md`)

- **Version:** `1.0.0` (Stage 2–4 Complete Execution of Pre-Registered Protocol `v1.0.2`)
- **Generated Timestamp:** `2026-10-30T07:49:30`
- **Governing Pre-Registration:** `PREREG.md` (`v1.0.2`), `MULTIVERSE_STAGE1_EQUATIONS.md` (`v1.0.2`), `ASSUMPTIONS.md` (`v1.0.2`), `PART1_RESULTS.md` (`v1.0.2`), `PART2_RESULTS.md` (`v1.0.2`), `PART3_RESULTS.md` (`v1.0.2`)
- **Pre-Registration Cryptographic Proof:** `PREREG_v4.sha256` (`53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b`) + OpenTimestamps proof `PREREG_v4.sha256.ots`
- **Dataset Freeze Cryptographic Proof:** `DATA_MANIFEST.sha256` (`73135698afb833e7e95e6a85c55475480132300e29f8b7b42d159c037067896d`) + OpenTimestamps proof `DATA_MANIFEST.sha256.ots` (stamped before any fit or parameter fixing was run)
- **Precedence Clause:** Where `PREREG.md` (`v1.0.2`) and any earlier document disagree, `PREREG.md` (`v1.0.2`) governs. `MULTIVERSE_TESTS_v1.md` is retained as a historical record only.

---

## 1. Executive Summary & Overall Model Verdict

The pre-registered 19-strand Ropewalk Multiverse model (`v1` static leak mechanism) was subjected to a blind, cryptographically timestamped empirical test suite spanning cosmological background expansion (`DESI DR2 BAO` + `Planck 2018` + `Pantheon+` / `DES-SN5YR Dovekie`), cosmic strand budget ratios (`Planck 2018` + `PDG 2024 BBN`), dissociative galaxy cluster mergers ($N=16$ systems), galaxy rotation curves (`SPARC` 175-galaxy database + `NGC 1052-DF2`), and local Hubble-flow directional isotropy (`Pantheon+SH0ES` across `HEALPix` $N_{\rm side}=1$ regions).

### Overall Model-Level Verdict (`PREREG.md` Section 3.3)

$$\mathbf{OVERALL\ MODEL\ VERDICT:\quad MODEL\ FALSIFIED\ (FAIL)}$$

Per `PREREG.md` Section 3.3, the global model verdict is decided by the four Primary Pillar Tests (`Pillar 1: T1-L1`, `Pillar 2: T2-A`, `Pillar 3: T4b`, `Pillar 4: T5-A`), where **MODEL FALSIFIED (`FAIL`)** is triggered if **two or more (`>= 2`) of the four primary pillars end in `FAIL`**, or if both cosmological pillars (`T1-L1` and `T2-A`) or both astrophysical pillars (`T4b` and `T5-A`) end in `FAIL`. In the executed suite:
- **2 of the 4 Primary Pillars ended in `FAIL`** (`Pillar 2: T2-A` and `Pillar 4: T5-A`).
- **2 of the 4 Primary Pillars ended in `INCONCLUSIVE`** (`Pillar 1: T1-L1` and `Pillar 3: T4b`; moreover, `Pillar 3: T4b` ends in `FAIL` in every sensitivity variant where the held-out test sample size reaches $n_{\rm test} \ge 6$).
- **0 of the 4 Primary Pillars ended in `PASS`**.

### Master Summary Table of All Registered Tests

| Test ID | Category | Physical Prediction / Hypothesis | Primary / Secondary | Key Measured Statistic | Pre-Registered Threshold | Final Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`T1-L1`** | Cosmology (Expansion) | Unwinding Law 1 $w(a) = -1 + \gamma_u/E(a)$ `[Model Ansatz]` vs $\Lambda$CDM & $w_0w_a$CDM | **Primary Pillar 1** | $\text{P+}: A=-1.71, B=+5.46$<br>$\text{Dov}: A=-2.58, B=+7.36$<br>$p_{\rm T1-L1} = 0.1907$ | `PASS`: $A \le -6.0$ & $B \le +2.0$<br>`FAIL`: $A > 0$ or $B > +9.0$ | **`INCONCLUSIVE`** |
| **`T2-A`** | Cosmology (Strand Budget) | $1:6:12$ strand budget + static leak $\mathcal{R}_{\rm pred} = 19\Omega_{bc}-1$ `[Model Ansatz]` vs Planck $5.36 \pm 0.065$ | **Primary Pillar 2** | $\text{P+}: \mathcal{R}_{\rm pred} = 4.866 \pm 0.115$ ($-3.74\sigma$)<br>$\text{Dov}: \mathcal{R}_{\rm pred} = 4.905 \pm 0.109$ ($-3.58\sigma$) | `PASS`: $\le 1.5\sigma$ (both)<br>`FAIL`: $> 2.0\sigma$ (both) | **`FAIL`** |
| **`T4b`** | Astrophysics (Clusters) | Merger age cutoff $\tau_{\rm lag}$ separating dark mass with galaxies ($t_p < \tau_{\rm lag}$) vs gas ($t_p \ge \tau_{\rm lag}$) `[Model Ansatz]` | **Primary Pillar 3** | $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ ($\text{Acc}_{\rm train}=87.5\%$)<br>Test: $n_{\rm test}=5 < 6$, $\text{Acc}_{\rm test}=60.0\%$, $n_{\rm gas}=0$ ($13/13$ with galaxies) | `INCONCLUSIVE` if $n_{\rm test} < 6$ (`Rule G8(3)`); `FAIL` in `S4`, `S6`, `S7` | **`INCONCLUSIVE`**<br>(`FAIL` when $n_{\rm test} \ge 6$) |
| **`T5-A`** | Astrophysics (Galaxies) | Single universal refraction width $\sigma_{\rm ref}$ across 87 held-out SPARC rotation curves `[Model Ansatz]` | **Primary Pillar 4** | $\hat{\sigma}_{\rm ref} = 9.213\text{ kpc}$<br>Test $M_{\chi^2} = 45.13$, $F_{<2} = 0.0690$ | `PASS`: $M_{\chi^2} \le 1.5$ & $F_{<2} \ge 0.60$<br>`FAIL`: $M_{\chi^2} > 3.0$ or $F_{<2} < 0.40$ | **`FAIL`** |
| **`T1-Sign`** | Cosmology (Dark Energy) | Directional thawing check $w_0 > -1$ in CPL $w_0w_a$CDM fit `[Model Ansatz]` | Secondary Scored | $\text{P+}: P(w_0 > -1) = 0.9960$ ($2.60\sigma$)<br>$\text{Dov}: P(w_0 > -1) = 0.9992$ ($3.12\sigma$) | `PASS`: $P(w_0 > -1) \ge 0.95$<br>`FAIL`: $P(w_0 < -1) > 0.977$ | **`PASS`** |
| **`T2-N1`** | Cosmology (Baryon Share) | Bare strand share $\Omega_b = 1/19 \approx 0.05263$ `[Model Ansatz]` vs Planck $0.04930 \pm 0.00086$ | Secondary Scored | $+3.87\sigma$ ($\Delta\Omega_b = +0.00333$) | `PASS`: $\le 2.0\sigma$<br>`FAIL`: $> 3.0\sigma$ | **`FAIL`** |
| **`T2-N2`** | Cosmology (Implied $H_0$) | $H_0^{\rm pred} = 100\sqrt{19\omega_b^{\rm BBN}} = 65.19 \pm 0.22$ `[Model Ansatz]` vs Planck $67.36 \pm 0.54$ | Secondary Scored | $-3.72\sigma$ ($\Delta H_0 = -2.17\text{ km s}^{-1}\text{ Mpc}^{-1}$) | `PASS`: $\le 2.0\sigma$<br>`FAIL`: $> 3.0\sigma$ | **`FAIL`** |
| **`T5-B`** | Astrophysics (Galaxies) | Scaled refraction width $\sigma_{{\rm ref},g} = k R_{d,g}$ across 87 held-out SPARC galaxies `[Model Ansatz]` | Secondary Scored | $\hat{k} = 2.9280$<br>Test $M_{\chi^2} = 23.74$, $F_{<2} = 0.0805$ | `PASS`: $M_{\chi^2} \le 1.5$ & $F_{<2} \ge 0.60$<br>`FAIL`: $M_{\chi^2} > 3.0$ or $F_{<2} < 0.40$ | **`FAIL`** |
| **`T5c`** | Astrophysics (UDGs) | NGC 1052-DF2 enclosed dynamical mass stress check at frozen $\hat{\sigma}_{\rm ref} = 9.213\text{ kpc}$ `[Model Ansatz]` | Secondary Scored | $M_{\rm pred}(<2.7\text{ kpc}) = 0.99\times 10^8 M_\odot$<br>$M_{\rm pred}(<3.1\text{ kpc}) = 1.17\times 10^8 M_\odot$ | `PASS`: $\le 2.9\times 10^8 M_\odot$ at $2.7\text{ kpc}$ & $< 3.2\times 10^8 M_\odot$ at $3.1\text{ kpc}$ | **`PASS`** |
| **`T6`** | Cosmology (Local $H_0$) | Regional $H_0$ heterogeneity across `HEALPix` $N_{\rm side}=1$ Galactic `RING` regions `[Model Ansatz]` | Secondary Scored | $N_{\rm pix}=9$, $\chi^2_{\rm het} = 8.935$ ($\text{dof}=8$)<br>$p_{\rm het} = 0.3478$, $Z_{\rm all\text{-}sky} = 5.22\sigma$ | `PASS`: $p_{\rm het,holm} \le \alpha_{\rm T6}$ & $Z \ge 3.0$<br>`FAIL`: $p_{\rm het} > 0.3173$ | **`FAIL`** |
| **`T4a`** | Astrophysics (Clusters) | Young-merger ($t_{\rm col} < \tau_{\rm lag}$) lensing-vs-galaxy offset sign $\Delta_{SI,\parallel} > 0$ `[Model Ansatz]` | Exploratory (Unscored) | Non-Bullet $t_{\rm col} \le 400\text{ Myr}$ ($N=1$): $\Delta_{SI,\parallel} = -45 \pm 52\text{ kpc}$ ($-0.87\sigma$); All 10 non-Bullet: $-43.8 \pm 23.8\text{ kpc}$ ($-1.84\sigma$) | Locked as Exploratory / Unscored (`PREREG.md` Sec 5.4) | **`EXPLORATORY`** |

---

## 2. Pre-Fit Validation Gates (`G9-a` through `G9-d`)

Before any model parameter was fitted or frozen, the cosmology and astrophysics numerical engines (`scripts/cosmology.py` and `scripts/sparc_t5.py`) were validated against the four pre-registered numerical gates in `PREREG.md` Section 2 (Rule `G9`). All four gates passed on the first run (`results/validation_gates_g9.json`):

| Gate ID | Mapped Tests | Validation Check & Dataset | Pre-Registered Tolerance | Obtained Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`G9-a`** | `T1-L1`, `T1-Sign`, `T2-A` | Flat $\Lambda$CDM fit to `DESI DR2 BAO` ($13\times 13$ covariance, unmodified Ly$\alpha$ $r_{\rm off}=0$) vs published DESI DR2 $\Omega_m = 0.2975 \pm 0.0086$ `[Established]` | $|\hat{\Omega}_m - 0.2975| / 0.0086 \le 0.30\sigma$ | $\hat{\Omega}_m = 0.29718 \pm 0.00862$ ($\chi^2_{\min} = 10.282$), difference $= \mathbf{0.037\sigma}$ | **`PASS`** |
| **`G9-b`** | `T1-L1`, `T1-Sign`, `T2-A` | Flat $\Lambda$CDM fit to compressed `Planck 2018` $(R, l_A, 100\omega_b)$ (`Chen, Huang & Wang 2019` Table 1) vs $\Omega_m = 0.3153 \pm 0.0073$, $h = 0.6736 \pm 0.0054$ `[Established]` | $\le 0.30\sigma$ on $\Omega_m, h, 100\omega_b$ | $\hat{\Omega}_m = 0.31548$ ($0.025\sigma$), $\hat{h} = 0.67374$ ($0.025\sigma$), $100\hat{\omega}_b = 2.2360$ ($0.000\sigma$); $\max = \mathbf{0.025\sigma}$ | **`PASS`** |
| **`G9-c`** | `T1-L1`, `T1-Sign` | CPL $w_0w_a$CDM joint fit (`DESI DR2 BAO` + `Planck 2018` $\Lambda$CDM Table 1 + `DES-SN5YR Dovekie`) vs published full-likelihood `DESI DR2` $w_0 = -0.803 \pm 0.054, w_a = -0.72 \pm 0.21$ `[Established]` | $\le 1.0\sigma$ on $(w_0, w_a)$ | $\hat{w}_0 = -0.8225$ ($\mathbf{0.361\sigma}$), $\hat{w}_a = -0.6306$ ($\mathbf{0.426\sigma}$), $\chi^2_{\min} = 1639.36$ | **`PASS`** |
| **`G9-d`** | `T5-A`, `T5-B`, `T5c` | Point-mass limit of the 1D ring-projected Gaussian kernel (`Eq. 38`) at $R=10\text{ kpc}$, $\sigma_{\rm ref}=0.05\text{ kpc}$ (`200`-sigma away from origin) vs exact Newtonian $GM/R^2$ `[Established]` | Relative error $< 10^{-10}$ | $\max\text{ relative error} = \mathbf{1.44 \times 10^{-11}} < 10^{-10}$ | **`PASS`** |

---

## 3. Stage 2 Parameter Fixing & Freeze Barrier (`FIXED_VALUES.json`)

In accordance with `PREREG.md` Section 2 (`Rule G3`), all five parameter-fixing procedures (`F1`–`F5`) were executed once and frozen in `results/FREEZE_T1.json` through `results/FREEZE_T6.json` and `results/FIXED_VALUES.json` before any scored test evaluation in Stage 3:

1. **`F1` (`FREEZE_T1.json`) — Unwinding Coefficient $\gamma_u$ (`T1`):**
   - `Pantheon+` joint MCMC (`32` walkers, `1000` burn-in, `4000` production steps; $\max|\hat{R}-1| = 0.0035 < 0.01$, $\min\text{ESS} = 2492 > 1000$): $\gamma_u = 0.04295 \pm 0.02616$ (best-fit $\gamma_u = 0.03848$), implying $w_0 = -0.9571 \pm 0.0262$ and $w_a = -0.0217 \pm 0.0147$.
   - `DES-Dovekie` joint MCMC ($\max|\hat{R}-1| = 0.0009 < 0.01$, $\min\text{ESS} = 2747 > 1000$): $\gamma_u = 0.04540 \pm 0.02578$ (best-fit $\gamma_u = 0.04384$), implying $w_0 = -0.9546 \pm 0.0258$ and $w_a = -0.0231 \pm 0.0146$.
2. **`F2` (`FREEZE_T2.json`) — Leak Fraction $f_{\rm leak}$ and Matter Density $\Omega_{bc}$ (`T2-A`):**
   - `T2-A-Pantheon+` ($\max|\hat{R}-1| = 0.0011$, $\min\text{ESS} = 2309$): $\Omega_{bc} = 0.308725 \pm 0.006049$, fixing $f_{\rm leak} = 1 - \frac{19\Omega_{bc}-1}{6} = \mathbf{0.189038 \pm 0.019155}$ and $\mathcal{R}_{\rm pred} = 4.86577 \pm 0.11493$.
   - `T2-A-Dovekie` ($\max|\hat{R}-1| = 0.0010$, $\min\text{ESS} = 1979$): $\Omega_{bc} = 0.310765 \pm 0.005757$, fixing $f_{\rm leak} = \mathbf{0.182578 \pm 0.018231}$ and $\mathcal{R}_{\rm pred} = 4.90453 \pm 0.10938$.
   - Per `PREREG.md` Section 5.6, the deciding `T2-A-Pantheon+` value $f_{\rm leak} = 0.189038$ (`R_pred = 4.8658`) is passed downstream into `T5-A`, `T5-B`, and `T5c`.
3. **`F3` (`FREEZE_T4.json`) — Merger Phase-Lag Cutoff $\tau_{\rm lag}$ (`T4b`):**
   - Fitted on the 8 odd-indexed training clusters (`#1, #3, #5, #7, #9, #11, #13, #15`; all 8 classified as `"with_galaxies"` under the $2\sigma_{\rm diff}$ rule) over the grid $[50, 1500]\text{ Myr}$ in $5\text{ Myr}$ steps using the shortest-interval-midpoint tie-breaking rule (`Rule G3` / `Sec 5.5`).
   - Because 7 of the 8 training clusters have $t_p \le 0.80\text{ Gyr}$ (`0.15` to `0.80 Gyr`) and 1 training cluster (`#15 RX J0603.3+4214`, $t_p = 1.50\text{ Gyr}$) has $t_p = 1.50\text{ Gyr}$, any threshold $\tau_{\rm lag} \in (0.80, 1.50]\text{ Gyr}$ achieves $\text{Acc}_{\rm train} = 7/8 = 87.5\%$, while $\tau_{\rm lag} > 1.50\text{ Gyr}$ is outside the grid. Under the pre-registered shortest-interval-midpoint rule, the single-point plateau just above $800\text{ Myr}$ fixes $\hat{\tau}_{\rm lag} = \mathbf{805\text{ Myr}}$ (`0.805 Gyr`).
4. **`F4` (`FREEZE_T5.json`) — Refraction Halo Smoothing Width $\sigma_{\rm ref}$ (`T5-A`) and Scale Factor $k$ (`T5-B`):**
   - Minimizing summed reduced chi-squared $L_{\rm train}(\sigma_{\rm ref}) = \sum_{g \in \text{train}} \chi^2_{{\rm red},g}$ across the 88 odd-indexed training galaxies in SPARC (`f_leak = 0.189038`) on the 400-point grid (`200` log-spaced on $[0.05, 5.0]\text{ kpc}$ + `200` linear on $(5.0, 50.0]\text{ kpc}$):
     - **`T5-A` frozen universal width:** $\hat{\sigma}_{\rm ref} = \mathbf{9.212795\text{ kpc}}$.
     - **`T5-B` frozen disk-scaled factor:** $\hat{k} = \mathbf{2.928045}$ (where $\sigma_{{\rm ref},g} = k R_{d,g}$).
5. **`F5` (`FREEZE_T6.json`) — SH0ES Calibrator Absolute Magnitude $M_B$ (`T6`):**
   - Fitted on the $N_{\rm cal} = 77$ Cepheid-calibrated SNe (`IS_CALIBRATOR == 1`) using the exact inverse of the $77 \times 77$ submatrix of `Pantheon+SH0ES_stat+sys.cov`:
     - $\hat{M}_B = \mathbf{-19.248885 \pm 0.030106\text{ mag}}$ ($\sigma_{M_B}^2 = 9.06353 \times 10^{-4}\text{ mag}^2$).

---

## 4. Detailed Results of Primary Pillar Tests

### 4.1 Pillar 1: `T1-L1` — Unwinding Dynamic Dark Energy Law 1 (`INCONCLUSIVE`)

- **Equations Tested:**
  - Standard flat FLRW background expansion `[Established]`:
    $$E^2(a) = \Omega_r a^{-4} + \Omega_m a^{-3} + \Omega_{\rm de}(a)$$
  - Ropewalk Unwinding Law 1 `[Model Ansatz]` (`Eq. 10` of `MULTIVERSE_STAGE1_EQUATIONS.md`):
    $$w(a) = -1 + \frac{\gamma_u}{E(a)}, \qquad \gamma_u \ge 0$$
  - CPL parameterization `[Established]`:
    $$w(a) = w_0 + w_a(1 - a)$$
  - Modified Alcock–Paczynski (`AP`) Ly$\alpha$ coordinate scaling `[Model Ansatz]` (`Eq. 45`):
    $$r_{\rm off} = -0.35 \left( \frac{[D_M(z_*)/D_H(z_*)]_{\rm model}}{[D_M(z_*)/D_H(z_*)]_{\rm fid}} - 1 \right), \qquad z_* = 2.33$$
- **Results (`Pantheon+` and `DES-SN5YR Dovekie` Deciding Runs):**

| Dataset Run | $\chi^2_{\min}(\Lambda\text{CDM})$ | $\chi^2_{\min}(\text{Law 1})$ | $\chi^2_{\min}(w_0w_a\text{CDM})$ | $A_r = \Delta\chi^2(\text{L1}-\Lambda\text{CDM})$ | $B_r = \Delta\chi^2(\text{L1}-w_0w_a)$ | Best-Fit $\gamma_u$ | Implied $(w_0, w_a)$ | Per-Run Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`Pantheon+` (Deciding)** | `1405.3436` | `1403.6318` | `1398.1760` | **`-1.7119`** | **`+5.4558`** | `0.0385` (`0.0429 ± 0.0262`) | `(-0.957, -0.022)` | **`INCONCLUSIVE`** |
| **`DES-Dovekie` (Deciding)** | `1650.9615` | `1648.3835` | `1641.0283` | **`-2.5780`** | **`+7.3552`** | `0.0438` (`0.0454 ± 0.0258`) | `(-0.955, -0.023)` | **`INCONCLUSIVE`** |
| `Pantheon+` (`wCDM` CMB Sens.) | `1404.7721` | `1402.8871` | `1397.8764` | `-1.8850` | `+5.0107` | `0.0404` | `(-0.960, -0.020)` | `INCONCLUSIVE` |
| `DES-Dovekie` (`wCDM` CMB Sens.) | `1650.4118` | `1647.6209` | `1640.7926` | `-2.7909` | `+6.8283` | `0.0456` | `(-0.954, -0.023)` | `INCONCLUSIVE` |
| `Pantheon+` ($r_{\rm off}=0$ Sens.) | `1405.5995` | `1403.7816` | `1398.8962` | `-1.8179` | `+4.8853` | `0.0400` | `(-0.960, -0.020)` | `INCONCLUSIVE` |
| `DES-Dovekie` ($r_{\rm off}=0$ Sens.) | `1651.2065` | `1648.5133` | `1641.7942` | `-2.6933` | `+6.7191` | `0.0451` | `(-0.955, -0.023)` | `INCONCLUSIVE` |
| `Pantheon+` (Unmod. BAO Sens.) | `1404.1818` | `1402.1952` | `1396.6331` | `-1.9866` | `+5.5621` | `0.0418` | `(-0.958, -0.021)` | `INCONCLUSIVE` |
| `DES-Dovekie` (Unmod. BAO Sens.) | `1649.8427` | `1646.9174` | `1639.3567` | `-2.9253` | `+7.5607` | `0.0470` | `(-0.953, -0.024)` | `INCONCLUSIVE` |

- **Physical Interpretation:** Because Law 1 enforces $w(a) = -1 + \gamma_u/E(a)$ with $\gamma_u \ge 0$, it restricts dark energy to the first-order ray $w_a = -\frac{3}{2}\Omega_{m0}(1 + w_0) \approx -0.46(1 + w_0)$ (`Eq. 11`, `[Model Ansatz]`) and guarantees $w(a) \ge -1$ at all redshifts (`no phantom crossing`). While Law 1 slightly improves over $\Lambda$CDM ($\Delta\chi^2 = -1.71$ on `Pantheon+` and $-2.58$ on `DES-Dovekie`), it cannot reproduce the steep negative slope ($w_a \approx -0.51$ to $-0.62$, which crosses $w = -1$ at $z \sim 0.4$) favored by unconstrained `DESI DR2 + CMB + SN` $w_0w_a$CDM fits ($\Delta\chi^2 = +5.46$ and $+7.36$ worse than $w_0w_a$CDM). Both runs fall cleanly in the pre-registered intermediate `INCONCLUSIVE` zone ($-6.0 < A_r \le 0$ and $+2.0 < B_r \le +9.0$).

---

### 4.2 Pillar 2: `T2-A` — $1:6:12$ Strand Budget & Leak Ratio (`FAIL`)

- **Equations Tested:**
  - Bare $1:6:12$ strand partition `[Model Ansatz]` (`Assumptions A3–A4`):
    $$\Omega_b^{\rm bare} = \frac{1}{19}, \qquad \Omega_{\rm dm}^{\rm bare} = \frac{6}{19}, \qquad \Omega_{\rm de}^{\rm bare} = \frac{12}{19}$$
  - Static ($Q=0$) leaked dark-to-baryon ratio `[Model Ansatz]` (`Eq. 21`):
    $$\mathcal{R}_{\rm pred} \equiv \frac{\Omega_{\rm dm}}{\Omega_b} = 6(1 - f_{\rm leak}) = 19\,\Omega_{bc} - 1$$
  - Combined independent error (`Eq. 28`, `[Established]`):
    $$\sigma_{\rm comb} = \sqrt{(19\,\sigma_{\Omega_{bc}})^2 + \sigma_{\rm Planck}^2}, \qquad \mathcal{R}_{\rm Planck} = 5.36 \pm 0.065$$
- **Results (`T2-A` Deciding & All Sensitivity Variants):**

| Variant / Dataset | $\Omega_{bc}$ Posterior | Implied $f_{\rm leak}$ | Predicted $\mathcal{R}_{\rm pred}$ | $\sigma_{\rm comb}$ | Tension vs Planck ($5.36 \pm 0.065$) | Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`T2-A-Pantheon+` (Deciding)** | `0.308725 ± 0.006049` | `0.189038 ± 0.019155` | **`4.8658 ± 0.1149`** | `0.1320` | **`-3.74σ`** (`> 2.0σ`) | **`FAIL`** |
| **`T2-A-Dovekie` (Deciding)** | `0.310765 ± 0.005757` | `0.182578 ± 0.018231` | **`4.9045 ± 0.1094`** | `0.1272` | **`-3.58σ`** (`> 2.0σ`) | **`FAIL`** |
| `T2-B-Pantheon+` (Constrained Sens.) | `0.318258 ± 0.005753` | `0.158849 ± 0.018218` | `5.0469 ± 0.1093` | `0.1272` | `-2.46σ` ($\Delta\chi^2 = +8.54$) | `FAIL` |
| `T2-B-Dovekie` (Constrained Sens.) | `0.319040 ± 0.005809` | `0.156373 ± 0.018395` | `5.0618 ± 0.1104` | `0.1281` | `-2.33σ` ($\Delta\chi^2 = +9.82 > 9$) | `FAIL` |
| `T2-A-Pantheon+` (`Cooke+18` BBN Sens.) | `0.313999 ± 0.005819` | `0.172337 ± 0.018426` | `4.9660 ± 0.1106` | `0.1283` | `-3.07σ` | `FAIL` |
| `T2-A-Dovekie` (`Cooke+18` BBN Sens.) | `0.316469 ± 0.005489` | `0.164514 ± 0.017383` | `5.0129 ± 0.1043` | `0.1229` | `-2.82σ` | `FAIL` |
| `T2-A-Pantheon+` (`2x2` Marginal CMB Sens.) | `0.310955 ± 0.005821` | `0.181976 ± 0.018434` | `4.9081 ± 0.1106` | `0.1283` | `-3.52σ` | `FAIL` |
| `T2-A-Dovekie` (`2x2` Marginal CMB Sens.) | `0.312512 ± 0.005336` | `0.177047 ± 0.016897` | `4.9377 ± 0.1014` | `0.1204` | `-3.51σ` | `FAIL` |

- **Physical Interpretation:** Because the model fixes the bare baryon fraction to $\Omega_b = 1/19 \approx 0.05263$ (`7.0%` higher than the `Planck 2018` value $\Omega_b = 0.04930 \pm 0.00086$), matching the observed late-time matter fraction $\Omega_{bc} \approx 0.309\text{–}0.311$ forces the dark-to-baryon ratio down to $\mathcal{R}_{\rm pred} = 19\Omega_{bc} - 1 \approx 4.87\text{–}4.90$, whereas `Planck 2018` measures $\omega_c/\omega_b = 5.36 \pm 0.065$. To reach $\mathcal{R}_{\rm pred} = 5.36$ under $\Omega_b = 1/19$ would require $\Omega_{bc} = 6.36/19 = 0.3347$, which is strongly excluded by `DESI DR2 BAO` ($\Omega_m \approx 0.298 \pm 0.009$). Both deciding runs (`-3.74σ` and `-3.58σ`) and all six sensitivity analyses exceed the $2.0\sigma$ `FAIL` threshold.

---

### 4.3 Pillar 3: `T4b` — Cluster Merger Age Cutoff $\tau_{\rm lag}$ (`INCONCLUSIVE` on Deciding Split / `FAIL` when $n_{\rm test} \ge 6$)

- **Equations Tested:**
  - Two-regime relaxation hypothesis `[Model Ansatz]` (`Assumption A12` & `Sec 5.5`):
    $$\text{Predicted Class}(t_p) = \begin{cases} \text{"with\_galaxies"} & \text{if } t_p < \tau_{\rm lag} \\ \text{"with\_gas"} & \text{if } t_p \ge \tau_{\rm lag} \end{cases}$$
  - Mechanical $2\sigma_{\rm diff}$ classification rule `[Established]` (`Eq. 33`):
    $$\sigma_{\rm diff} = \sqrt{\sigma_I^2 + \max(\sigma_S^2, \sigma_G^2)}, \qquad \begin{cases} d_{IG} - d_{IS} > 2\sigma_{\rm diff} \implies \text{"with\_galaxies"} \\ d_{IS} - d_{IG} > 2\sigma_{\rm diff} \implies \text{"with\_gas"} \\ |d_{IG} - d_{IS}| \le 2\sigma_{\rm diff} \implies \text{"unclassified"} \end{cases}$$
- **Complete 16-Cluster Catalog & Classification Results (`data/MERGERS.csv`):**

| ID | Cluster Name | Common Name | Split | $t_p\text{ (Gyr)}$ | $d_{IS}\text{ (kpc)}$ | $d_{IG}\text{ (kpc)}$ | $2\sigma_{\rm diff}\text{ (kpc)}$ | Observed Class | Predicted Class ($\hat{\tau}_{\rm lag}=0.805\text{ Gyr}$) | Match? |
| :-: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `1` | `1E 0657-558` | Bullet Cluster | Train (Odd) | `0.40 ± 0.10` | `25.0` | `161.5` | `58.2` | `with_galaxies` | `with_galaxies` | Yes |
| `2` | `ACT-CL J0102-4915` | El Gordo | **Test (Even)** | `0.75 ± 0.15` | `11.6` | `65.7` | `46.9` | `with_galaxies` | `with_galaxies` | **Yes** |
| `3` | `Abell 1240` | Abell 1240 | Train (Odd) | `0.45 ± 0.15` | `48.0` | `240.0` | `163.1` | `with_galaxies` | `with_galaxies` | Yes |
| `4` | `Abell 1758N` | Abell 1758N | **Test (Even)** | `0.40 ± 0.15` | `101.4` | `76.1` | `101.9` | `unclassified` | `with_galaxies` | — |
| `5` | `Abell 2034` | Abell 2034 | Train (Odd) | `0.30 ± 0.10` | `117.5` | `299.0` | `144.7` | `with_galaxies` | `with_galaxies` | Yes |
| `6` | `Abell 2146` | Abell 2146 | **Test (Even)** | `0.25 ± 0.08` | `1.6` | `30.3` | `11.0` | `with_galaxies` | `with_galaxies` | **Yes** |
| `7` | `Abell 2744` | Pandora | Train (Odd) | `0.15 ± 0.05` | `61.7` | `205.0` | `90.7` | `with_galaxies` | `with_galaxies` | Yes |
| `8` | `Abell 3376` | Abell 3376 | **Test (Even)** | `0.55 ± 0.15` | `32.0` | `28.0` | `80.6` | `unclassified` | `with_galaxies` | — |
| `9` | `Abell 520` | Train Wreck | Train (Odd) | `0.80 ± 0.25` | `18.0` | `485.6` | `37.9` | `with_galaxies` | `with_galaxies` | Yes |
| `10` | `Abell 754` | Abell 754 | **Test (Even)** | `0.30 ± 0.10` | `28.0` | `165.0` | `91.4` | `with_galaxies` | `with_galaxies` | **Yes** |
| `11` | `CIZA J2242.8+5301` | Sausage | Train (Odd) | `0.80 ± 0.15` | `189.0` | `520.0` | `198.7` | `with_galaxies` | `with_galaxies` | Yes |
| `12` | `DLSCL J0916.2+2951` | Musket Ball | **Test (Even)** | `1.10 ± 0.65` | `129.0` | `530.0` | `137.3` | `with_galaxies` | `with_gas` | **No** |
| `13` | `MACS J0025.4-1222` | Baby Bullet | Train (Odd) | `0.50 ± 0.20` | `45.3` | `326.3` | `223.7` | `with_galaxies` | `with_galaxies` | Yes |
| `14` | `MACS J1149.5+2223` | MACS J1149 | **Test (Even)** | `1.16 ± 0.38` | `19.0` | `95.8` | `53.9` | `with_galaxies` | `with_gas` | **No** |
| `15` | `RX J0603.3+4214` | Toothbrush | Train (Odd) | `1.50 ± 0.30` | `18.0` | `108.3` | `73.5` | `with_galaxies` | `with_gas` | No |
| `16` | `ZwCl 0008.8+5215` | ZwCl 0008 | **Test (Even)** | `0.76 ± 0.21` | `249.0` | `319.0` | `278.2` | `unclassified` | `with_galaxies` | — |

- **Summary of Deciding Split and All 7 Sensitivity Analyses (`T4b`):**

| Variant | $\hat{\tau}_{\rm lag}\text{ (Gyr)}$ | $n_{\rm train}$ | $\text{Acc}_{\rm train}$ | $n_{\rm test}$ | $\text{Acc}_{\rm test}$ | $n_{\rm gas}$ (`Old Branch`) | Raw $p_{\rm T4b}$ | Verdict & Triggering Rule |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Deciding (Odd/Even, Primary Subcluster)** | `0.805` | `8` | `87.5%` (`7/8`) | `5` | `60.0%` (`3/5`) | `0` | `0.5000` | **`INCONCLUSIVE`** (`Rule G8(3)`: $n_{\rm test} = 5 < 6$) |
| `S1` (Bullet $t_p = 0.40\text{ Gyr}$ Median) | `0.805` | `8` | `87.5%` (`7/8`) | `5` | `60.0%` (`3/5`) | `0` | `0.5000` | `INCONCLUSIVE` ($n_{\rm test} = 5 < 6$) |
| `S2` (Posterior-Weighted Soft Accuracy) | `1.500` | `8` | `93.7%` | `5` | `90.6%` | `0` | — | `Non-Deciding Sensitivity` (pushes $\hat{\tau}_{\rm lag}$ to top of grid because $n_{\rm gas}=0$) |
| `S3` (System-Level Classification) | `0.805` | `8` | `87.5%` (`7/8`) | `5` | `60.0%` (`3/5`) | `0` | `0.5000` | `INCONCLUSIVE` ($n_{\rm test} = 5 < 6$) |
| `S4` (`Abell 520` `Jee+14` `P3` Dark Core) | `0.505` | `8` | `75.0%` (`6/8`) | `5` | `40.0%` (`2/5`) | `1` (P3) | `0.8125` | **`FAIL`** (`Clause 1(a)`: $\max\text{Acc}_{\rm train} = 75.0\% < 80\%$) |
| `S5` (`Abell 520` `Clowe+12` No Dark Core) | `0.805` | `8` | `87.5%` (`7/8`) | `5` | `60.0%` (`3/5`) | `0` | `0.5000` | `INCONCLUSIVE` ($n_{\rm test} = 5 < 6$) |
| `S6` (`Abell 1758N` `Ragozzine+12` Lens Peak) | `0.805` | `8` | `87.5%` (`7/8`) | `6` | `66.7%` (`4/6`) | `0` | `0.3438` | **`FAIL`** (`Clause 1(c)`: $n_{\rm test}=6 \ge 6$ and all 6 test clusters are `"with_galaxies"`) |
| `S7` (`First-8 Train / Last-8 Test` Split) | `0.755` | `6` | `100.0%` (`6/6`) | `7` | `28.6%` (`2/7`) | `0` | `0.9375` | **`FAIL`** (`Clause 1(b)` & `1(c)`: $\text{Acc}_{\rm test}=28.6\% < 60\%$ & all 7 test clusters `"with_galaxies"`) |

- **Physical Interpretation:** Empirically, **0 out of 13 classified primary subclusters (`0%`)** in the 16-cluster catalog have weak-lensing mass peaks tracking the X-ray gas rather than the galaxies, even in late-stage post-pericenter mergers with $t_p > 1.0\text{ Gyr}$ (`#12 Musket Ball` at $1.10\text{ Gyr}$, `#14 MACS J1149` at $1.16\text{ Gyr}$, and `#15 Toothbrush` at $1.50\text{ Gyr}$). In the deciding alphabetical Odd/Even split, 3 of the 8 even-indexed test clusters (`#4 Abell 1758N`, `#8 Abell 3376`, `#16 ZwCl 0008`) have $|d_{IG}-d_{IS}| \le 2\sigma_{\rm diff}$, leaving $n_{\rm test} = 5 < 6$ classified test systems and mechanically triggering `Rule G8(3)` (`INCONCLUSIVE`). Whenever the test sample reaches $n_{\rm test} \ge 6$ (`S6` and `S7`), or when the `Abell 520` `P3` dark core is used (`S4`), `T4b` triggers an immediate `FAIL`.

---

### 4.4 Pillar 4: `T5-A` — Universal Refraction Halo Width on Held-Out SPARC Rotation Curves (`FAIL`)

- **Equations Tested:**
  - 2D Gaussian-smeared shadow-matter radial acceleration kernel `[Model Ansatz]` (`Eq. 38` of `MULTIVERSE_STAGE1_EQUATIONS.md`, verified in `B1` and Gate `G9-d`):
    $$g_{\rm sh}(R; \sigma_{\rm ref}) = G\,\mathcal{R}_{\rm pred} \int_0^\infty \Sigma_b(R')\,R'\,dR' \int_0^\infty k\,dk\,J_1(kR)\,J_0(kR')\,e^{-\frac{1}{2}k^2\sigma_{\rm ref}^2}$$
    evaluated via its 1D ring-projected elliptic-integral representation (`Eq. 38b`, `[Established]` mathematical identity):
    $$g_{\rm sh}(R; \sigma_{\rm ref}) = \frac{G\,\mathcal{R}_{\rm pred}}{R} \int_0^\infty \Sigma_b(R')\,R'\,\mathcal{F}_\sigma(R, R')\,dR'$$
  - Total rotation velocity prediction `[Model Ansatz]` (`Eq. 39`):
    $$V_{\rm model}^2(R) = V_{\rm bar}^2(R) + R\,g_{\rm sh}(R; \sigma_{\rm ref}), \qquad \Upsilon_{\rm disk} = 0.50\,M_\odot/L_\odot,\quad \Upsilon_{\rm bulge} = 0.70\,M_\odot/L_\odot$$
- **Results Across All SPARC Models (`T5-A`, `T5-B`, Sensitivity Losses, Baryon-Only, and RAR Benchmark):**

| Model / Variant | Loss Minimized on 88 Training Galaxies | Frozen Parameter | Train Median $\chi^2_{\rm red}$ ($M_{\chi^2}$) | Train $F_{<2}$ | Held-Out Test Median $\chi^2_{\rm red}$ ($M_{\chi^2}$, $N=87$) | Held-Out Test $F_{<2}$ ($N=87$) | Held-Out Pooled $\chi^2_{\rm red}$ | Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`T5-A` (Deciding Universal $\sigma_{\rm ref}$)** | $\sum \chi^2_{{\rm red},g}$ ($f_{\rm leak}=0.1890$) | $\hat{\sigma}_{\rm ref} = \mathbf{9.2128\text{ kpc}}$ | `48.51` | `0.0341` | **`45.13`** (`> 3.0`) | **`0.0690`** (`< 0.40`) | `324.22` | **`FAIL`** |
| **`T5-B` (Secondary Scaled $\sigma_{{\rm ref},g} = k R_{d,g}$)** | $\sum \chi^2_{{\rm red},g}$ ($f_{\rm leak}=0.1890$) | $\hat{k} = \mathbf{2.9280}$ | `25.00` | `0.0568` | **`23.74`** (`> 3.0`) | **`0.0805`** (`< 0.40`) | `234.61` | **`FAIL`** |
| `T5-A` Sensitivity (Total $\chi^2$ Loss) | $\sum \chi^2_g$ ($f_{\rm leak}=0.1890$) | $\hat{\sigma}_{\rm ref} = 8.0874\text{ kpc}$ | `45.95` | `0.0227` | `41.55` | `0.0575` | `412.88` | `FAIL` |
| `T5-A` Sensitivity (Median $\chi^2_{\rm red}$ Loss) | $\text{median}(\chi^2_{{\rm red},g})$ | $\hat{\sigma}_{\rm ref} = 1.3126\text{ kpc}$ | `25.84` | `0.0568` | `58.77` | `0.0920` | `2252.37` | `FAIL` |
| `T5-A` Sensitivity (Geometric $f_{\rm leak}=1/6$) | $\sum \chi^2_{{\rm red},g}$ ($f_{\rm leak}=0.1667$) | $\hat{\sigma}_{\rm ref} = 9.6454\text{ kpc}$ | `52.25` | `0.0341` | `47.68` | `0.0690` | `314.34` | `FAIL` |
| `T5-B` Sensitivity (Total $\chi^2$ Loss) | $\sum \chi^2_g$ ($f_{\rm leak}=0.1890$) | $\hat{k} = 3.2373$ | `26.06` | `0.0682` | `28.36` | `0.0690` | `193.90` | `FAIL` |
| `T5-B` Sensitivity (Median $\chi^2_{\rm red}$ Loss) | $\text{median}(\chi^2_{{\rm red},g})$ | $\hat{k} = 2.1178$ | `17.77` | `0.0909` | `23.24` | `0.0920` | `458.90` | `FAIL` |
| **Baryon-Only Baseline** ($\mathcal{R}_{\rm pred}=0$) | Fixed M/L (`0.5, 0.7`) | — | `83.21` | `0.0227` | `77.92` | `0.0460` | `526.62` | Reference |
| **RAR Benchmark** (`McGaugh+16` Fixed $g_\dagger$) | Fixed $g_\dagger = 1.20\times 10^{-10}\text{ m s}^{-2}$ | $g_\dagger = 1.20\times 10^{-10}$ | `12.10` | `0.1136` | `9.40` | `0.1149` | `57.47` | Reference |
| **RAR Benchmark** (Fitted $g_\dagger$) | $\sum \chi^2_{{\rm red},g}$ | $\hat{g}_\dagger = 1.15\times 10^{-10}$ | `10.72` | `0.1364` | `8.43` | `0.1149` | `57.29` | Reference |

- **Physical & Mechanistic Diagnostics (`F3` & `F4`):**
  1. **Asymptotic Saturation Cap (`F4`):** Because a 2D Gaussian convolution of a finite baryonic mass $M_b$ encloses at most $\mathcal{R}_{\rm pred}\,M_b$ as $R \to \infty$, the model's total-to-baryonic acceleration ratio is strictly bounded above by $g_{\rm tot}(R)/g_{\rm bar}(R) \le 1 + \mathcal{R}_{\rm pred} = 1 + 6(1 - f_{\rm leak}) = \mathbf{5.8658}$ (`6.000` for $f_{\rm leak}=1/6$). Across the 175 SPARC galaxies (`3391` radial points), **`442` of `3391` radial points (`13.03%`) across `67` of `175` galaxies (`38.29%`)** have observed $V_{\rm obs}^2(R)/V_{\rm bar}^2(R) > 5.8658$, where no choice of $\sigma_{\rm ref}$ can ever supply enough enclosed mass.
  2. **Structural Trade-Off:** For high-surface-brightness galaxies (`NGC 2841`, `UGC 02953`), adding $\mathcal{R}_{\rm pred} = 4.866$ of shadow matter overpredicts inner rotation curves unless $\sigma_{\rm ref}$ is made very wide ($\hat{\sigma}_{\rm ref} = 9.21\text{ kpc}$) to diffuse the shadow mass outward; conversely, for compact dwarf and low-surface-brightness galaxies (`DDO 154`), $\sigma_{\rm ref} = 9.21\text{ kpc}$ smears nearly all shadow mass outside the last measured radius ($R_{\max} \sim 5\text{–}8\text{ kpc}$), leaving the model nearly baryon-only and severely underpredicting $V_{\rm obs}(R)$.
  3. **Kinematic Coherence Length Check (`F3`):** Comparing $\hat{\sigma}_{\rm ref} = 9.21\text{ kpc}$ against the orbital phase-lag scale $v_c\,\hat{\tau}_{\rm lag}$ across the 135 SPARC galaxies with measured $V_{\rm flat} > 0$ ($\hat{\tau}_{\rm lag} = 0.805\text{ Gyr}$) yields a median $v_c\,\hat{\tau}_{\rm lag} = \mathbf{93.03\text{ kpc}}$ ($\text{IQR} = [65.49, 150.29]\text{ kpc}$), which is an order of magnitude larger than $\hat{\sigma}_{\rm ref} = 9.21\text{ kpc}$.

---

## 5. Detailed Results of Secondary & Exploratory Tests

### 5.1 `T1-Sign` — Directional Thawing Check $w_0 > -1$ (`PASS`)
- In the unconstrained CPL $w_0w_a$CDM MCMC chains (`DESI DR2 BAO` + `Planck 2018` + `SN`):
  - **`Pantheon+`:** $w_0 = -0.8541 \pm 0.0560$, $w_a = -0.5140 \pm 0.2152$; posterior probability $P(w_0 > -1 \mid \text{data}) = \mathbf{0.9960 \ge 0.95}$ (Gaussian $z = +2.60\sigma$).
  - **`DES-Dovekie`:** $w_0 = -0.8250 \pm 0.0557$, $w_a = -0.6153 \pm 0.2228$; posterior probability $P(w_0 > -1 \mid \text{data}) = \mathbf{0.9992 \ge 0.95}$ (Gaussian $z = +3.12\sigma$).
- Both datasets satisfy $P(w_0 > -1 \mid \text{data}) \ge 0.95$, so `T1-Sign` ends in **`PASS`**. As pre-registered in `PREREG.md` Section 5.1 (`Review B4`), this directional check cannot override the primary `T1-L1` test.

### 5.2 `T2-N1` and `T2-N2` — Bare Baryon Share $\Omega_b = 1/19$ and Implied $H_0$ (`FAIL`)
- **`T2-N1` ($\Omega_b = 1/19$ vs Planck 2018):**
  $$\frac{|\Omega_b^{\rm model} - \Omega_{b,\text{Planck}}|}{\sigma_{\Omega_b,\text{Planck}}} = \frac{|0.0526316 - 0.04930|}{0.00086} = \mathbf{3.8739\sigma > 3.0\sigma} \implies \mathbf{FAIL}$$
- **`T2-N2` ($H_0^{\rm pred} = 100\sqrt{19\omega_b}$ vs Planck 2018):**
  Using the deciding `PDG 2024` BBN prior $100\omega_b = 2.237 \pm 0.015$ (`Eq. 29`, `[Model Ansatz]`):
  $$H_0^{\rm pred} = 100\sqrt{19 \times 0.02237} = \mathbf{65.1943 \pm 0.2186\text{ km s}^{-1}\text{ Mpc}^{-1}}$$
  Compared against `Planck 2018` $H_0 = 67.36 \pm 0.54\text{ km s}^{-1}\text{ Mpc}^{-1}$ ($\sigma_{\rm comb} = 0.5826$):
  $$Z_{\rm T2-N2} = \frac{65.1943 - 67.36}{0.5826} = \mathbf{-3.7175\sigma} \quad (|Z| > 3.0\sigma) \implies \mathbf{FAIL}$$
  Moreover, because $H_0^{\rm pred} = 65.19\text{ km s}^{-1}\text{ Mpc}^{-1}$ is even lower than the `Planck 2018` $\Lambda$CDM value ($67.36$), the bare $\Omega_b = 1/19$ rule moves in the **wrong direction** to explain the local `SH0ES` Hubble tension ($73.04 \pm 1.04\text{ km s}^{-1}\text{ Mpc}^{-1}$).

### 5.3 `T5c` — NGC 1052-DF2 Stress Check (`PASS`)
- Evaluated at the frozen `T5-A` smoothing width $\hat{\sigma}_{\rm ref} = 9.212795\text{ kpc}$ and $f_{\rm leak} = 0.189038$ (`R_pred = 4.8658`) using the pre-registered Sérsic ($n=0.6$, $R_e = 2.2\text{ kpc}$, $M_* = 2.0 \times 10^8 M_\odot$) + external NGC 1052 group shadow-background ($d_{\rm proj} = 80\text{ kpc}$) model (`Eq. 40`, `[Model Ansatz]`):
  - At $r = 2.7\text{ kpc}$ (`Danieli+19`): $M_{b,\text{enc}} = 0.9318 \times 10^8 M_\odot$, $M_{\rm sh,DF2} = 0.0559 \times 10^8 M_\odot$, $M_{\rm sh,group} = 0.0000 \times 10^8 M_\odot \implies M_{\rm pred}(<2.7\text{ kpc}) = \mathbf{0.9877 \times 10^8 M_\odot \le 2.9 \times 10^8 M_\odot}$.
  - At $r = 3.1\text{ kpc}$ (`van Dokkum+18`): $M_{b,\text{enc}} = 1.0847 \times 10^8 M_\odot$, $M_{\rm sh,DF2} = 0.0839 \times 10^8 M_\odot \implies M_{\rm pred}(<3.1\text{ kpc}) = \mathbf{1.1686 \times 10^8 M_\odot < 3.2 \times 10^8 M_\odot}$.
  - At $r = 7.6\text{ kpc}$ (reported for completeness): $M_{\rm pred}(<7.6\text{ kpc}) = 2.8309 \times 10^8 M_\odot$.
- **Verdict:** **`PASS`**. Note, however, that `T5c` passes specifically because `T5-A` forced $\hat{\sigma}_{\rm ref}$ to the wide value $9.21\text{ kpc}$ (which diffuses DF2's shadow halo far beyond $3.1\text{ kpc}$), and that same wide $\hat{\sigma}_{\rm ref}$ caused `T5-A` to fail on the SPARC rotation-curve sample.

### 5.4 `T6` — Regional $H_0$ Heterogeneity Across `HEALPix` $N_{\rm side}=1$ Regions (`FAIL`)
- **Deciding Run (`Galactic RING`, $0.0233 \le z_{\rm HD} \le 0.15$, Pre-Fit Sparse-Pixel Merging):**
  - Out of 496 Hubble-flow SNe in `Pantheon+SH0ES.dat`, pixels `4` (`3` SNe), `7` (`8` SNe), and `11` (`5` SNe) had $N_k < 10$ and were merged into their nearest neighboring pixel by great-circle center distance (`4 -> 0`, `7 -> 2`, `11 -> 4`), after which pixel `4` (`5` SNe) remained $<10$ and was dropped per `PREREG.md` Section 5.7, leaving $N_{\rm pix} = 9$ well-sampled sky regions (`491` Hubble-flow SNe).
  - Using the full non-diagonal $491 \times 491$ Hubble-flow submatrix of `Pantheon+SH0ES_stat+sys.cov` (`Eq. 41`–`43`, `[Established]`):
    - All-sky weighted mean: $\bar{H}_0 = \mathbf{73.5056 \pm 0.2419\text{ (HF)} \pm 1.0474\text{ (tot) km s}^{-1}\text{ Mpc}^{-1}}$ ($Z_{\rm all\text{-}sky} = \mathbf{5.22\sigma \ge 3.0\sigma}$ vs `Planck 2018`).
    - Regional $H_0$ range across the 9 sky regions: $\mathbf{72.53}$ to $\mathbf{75.09\text{ km s}^{-1}\text{ Mpc}^{-1}}$ (max-minus-min $= 2.56\text{ km s}^{-1}\text{ Mpc}^{-1}$, RMS scatter $= 0.72\text{ km s}^{-1}\text{ Mpc}^{-1}$).
    - Regional heterogeneity statistic: $\chi^2_{\rm het} = \mathbf{8.9347}$ for $\text{dof} = N_{\rm pix} - 1 = 8$, giving $p_{\rm het} = \mathbf{0.347838 > 0.3173}$ ($< 1\sigma$ variation across the sky).
  - **Verdict:** **`FAIL`** ($p_{\rm het} = 0.3478 > 0.3173$). The local Hubble-flow expansion rate is spatially isotropic across the sky within $1\sigma$; the $5.2\sigma$ shift between `SH0ES` and `Planck` is a monopolar offset rather than a regional patchwork of $H_{0,k} \sim 67\text{–}74\text{ km s}^{-1}\text{ Mpc}^{-1}$ domains.
- **Sensitivity Runs (`T6`):**
  - `Equatorial RING` ($z_{\rm HD}$, merged): $N_{\rm pix} = 11$, $\chi^2_{\rm het} = 14.7714$ ($\text{dof}=10$), $p_{\rm het} = 0.1406$ (`INCONCLUSIVE`).
  - `Galactic RING` ($z_{\rm CMB}$, merged): $N_{\rm pix} = 9$, $\chi^2_{\rm het} = 14.8090$ ($\text{dof}=8$), $p_{\rm het} = 0.0630$ (`INCONCLUSIVE`).
  - `Galactic RING` ($z_{\rm HD}$, drop sparse without merging): $N_{\rm pix} = 9$, $\chi^2_{\rm het} = 8.6121$ ($\text{dof}=8$), $p_{\rm het} = 0.3761 > 0.3173$ (`FAIL`).

### 5.5 `T4a` — Young-Merger Lensing-vs-Galaxy Offset Sign (`EXPLORATORY / UNSCORED`)
- Per `PREREG.md` Section 5.4 (`Review B3`), `T4a` is unconditionally locked as `EXPLORATORY (Unscored)` because excluding the Bullet Cluster (`#1`) from `Wittman et al. (2018)` Table 2 leaves only $N=1$ subcluster (`A2744 S`, $t_{\rm col} = 120\text{ Myr}$) with $t_{\rm col} \le 400\text{ Myr}$.
- Under the unified sign convention $\Delta_{SI,\parallel} = (\mathbf{x}_{\rm lens} - \mathbf{x}_{\rm gal})\cdot\hat{\mathbf{v}}_{\rm Gal} = -\Delta x_{SI}^{\rm W18}$ (`> 0` if lensing leads galaxies, `< 0` if lensing lags toward gas):
  - **Non-Bullet $t_{\rm col} \le 235\text{ Myr}$ and $\le 400\text{ Myr}$ ($N=1$, `A2744 S`):** $\Delta_{SI,\parallel} = -45.0 \pm 52.0\text{ kpc}$ ($z = -0.87\sigma$, $\beta = +0.30 \pm 0.34$).
  - **All 10 non-Bullet subclusters in `Wittman+18`:** Inverse-variance weighted mean $\bar{\Delta}_{SI,\parallel} = -43.76 \pm 23.76\text{ kpc}$ ($z = -1.84\sigma$, $\bar{\beta} = +0.124 \pm 0.072$; only 3 of 10 have $\Delta_{SI,\parallel} > 0$).
  - **All 11 `Wittman+18` subclusters (including Bullet):** $\bar{\Delta}_{SI,\parallel} = -19.57 \pm 18.62\text{ kpc}$ ($z = -1.05\sigma$, $\bar{\beta} = +0.098 \pm 0.069$).
  - **`Harvey et al. (2015)` 72-subcluster ensemble:** $\bar{\beta} = -0.04 \pm 0.07$ ($z = +0.57\sigma$).
- Thus, the exploratory data show no statistically significant positive offset ($\Delta_{SI,\parallel} > 0$).

---

## 6. Holm–Bonferroni Family-Wise Error Control (`PREREG.md` Section 3.1)

Across the $K = 3$ discovery-style $p$-value tests (`T1-L1`, `T4b`, `T6`) at family-wise error rate $\alpha_{\rm FWE} = 0.05$:

| Rank $m$ | Test ID | Raw Discovery $p$-Value $p_{(m)}$ | Holm–Bonferroni Threshold $\alpha_{\rm FWE}/(K - m + 1)$ | Survives Threshold? ($p_{(m)} \le \alpha_{(m)}$) | Pre-Holm Verdict | Post-Holm Final Verdict |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **`1`** | **`T1-L1`** | `0.190744` | `0.016667` (`0.05 / 3`) | **No** (`m* = 1`) | `INCONCLUSIVE` | **`INCONCLUSIVE`** |
| **`2`** | **`T6`** | `0.347838` | `0.025000` (`0.05 / 2`) | **No** | `FAIL` | **`FAIL`** |
| **`3`** | **`T4b`** | `1.000000` (raw `0.5000`, $n_{\rm test}=5<6$) | `0.050000` (`0.05 / 1`) | **No** | `INCONCLUSIVE` | **`INCONCLUSIVE`** |

Because the lowest ranked $p$-value (`T1-L1`, $p_{(1)} = 0.1907$) exceeds $\alpha_{\rm FWE}/3 = 0.0167$, the Holm–Bonferroni stopping rank is $m^* = 1$, and zero discovery tests achieve `PASS`.

---

## 7. Cosmic Coincidence Window Calculation (`PREREG.md` Section 6)

Under standard flat $\Lambda$CDM expansion (`Planck 2018` parameters: $\Omega_{b0} = 0.04930$, $\Omega_{{\rm dm},0} = 0.26447$, $\Omega_{{\rm de},0} = 0.68470$, $H_0 = 67.36\text{ km s}^{-1}\text{ Mpc}^{-1}$, cosmic age $t_0 = 13.8005\text{ Gyr}$ `[Established]`), we computed the cosmic time duration $\Delta t$ over which the evolving cosmic density shares $\Omega_i(a)$ simultaneously match the Ropewalk target shares $\mathbf{s}_{\rm target}(f_{\rm leak})$ `[Model Ansatz]` (`Eq. 30`–`32`):

| Target Prescription | Target Shares $(s_b, s_{\rm dm}, s_{\rm de})$ | Present-Day ($a=1$) Max Abs / Rel Error | Criterion `H-Abs` ($\max_i|\Omega_i(a)-s_i| \le 0.05$) | Criterion `H-Rel` ($\max_i|\Omega_i(a)-s_i|/s_i \le 0.10$) | Contains $a=1$? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Geometric $f_{\rm leak} = 1/6$ (`1:5:13`)** | `(0.05263, 0.26316, 0.68421)` | `0.00333` / `6.33%` | $\Delta t_{\rm abs} = \mathbf{2.255\text{ Gyr}}$ (`16.34%` of $t_0$)<br>$a \in [0.9277, 1.0835]$ ($z \in [-0.077, +0.078]$) | $\Delta t_{\rm rel} = \mathbf{0.927\text{ Gyr}}$ (`6.72%` of $t_0$)<br>$a \in [0.9561, 1.0195]$ ($z \in [-0.019, +0.046]$) | **Yes** (both) |
| **Frozen `T2-A-Pantheon+` $f_{\rm leak} = 0.1890$** | `(0.05263, 0.25609, 0.69128)` | `0.00837` / `6.33%` | $\Delta t_{\rm abs} = \mathbf{2.296\text{ Gyr}}$ (`16.63%` of $t_0$)<br>$a \in [0.9372, 1.0968]$ ($z \in [-0.088, +0.067]$) | $\Delta t_{\rm rel} = \mathbf{0.731\text{ Gyr}}$ (`5.30%` of $t_0$)<br>$a \in [0.9693, 1.0195]$ ($z \in [-0.019, +0.032]$) | **Yes** (both) |

This confirms the analytical finding from `PART2_RESULTS.md`: because standard FLRW matter and dark-energy densities scale as $a^{-3}$ and $a^0$ when $Q = 0$, the $1:5:13$ leaked ratio is not an attractor in the `v1` static model, holding to within $10\%$ relative accuracy for only $\Delta t_{\rm rel} \approx 0.73\text{–}0.93\text{ Gyr}$ (`5.3%–6.7%` of $t_0$) around the present epoch.

---

## 8. Figures Generated (`results/figures/`)

1. `results/figures/fig1_t1_unwinding_vs_desi.png`: $(w_0, w_a)$ posterior contours (`68%` and `95%`) for `Pantheon+` and `DES-Dovekie` CPL fits vs the `T1-L1` Unwinding Law 1 ray (`Eq. 11`) and `w(z)` redshift evolution.
2. `results/figures/fig2_t2_strand_budget_tension.png`: `T2-A` and `T2-B` posteriors on $\mathcal{R}_{\rm pred} = 19\Omega_{bc}-1$ vs `Planck 2018` (`5.36 ± 0.065`) and `T2-N1`/`T2-N2` tension bars (`+3.87σ` and `-3.72σ`).
3. `results/figures/fig3_t4b_cluster_mergers.png`: `T4b` 16-cluster separation difference $(d_{IG} - d_{IS}) / (2\sigma_{\rm diff})$ vs time since pericenter $t_p$ and training/test accuracy curve vs $\tau_{\rm lag}$.
4. `results/figures/fig4_t5_sparc_rotation_curves.png`: Held-out SPARC $\chi^2_{\rm red}$ cumulative distributions (`T5-A`, `T5-B`, RAR, Baryon-only) and six representative held-out rotation curves showing the $1+\mathcal{R}_{\rm pred} = 5.866$ Gaussian saturation cap.
5. `results/figures/fig5_t6_regional_h0_and_coincidence.png`: `T6` regional $H_{0,k}$ across the 9 retained `HEALPix` $N_{\rm side}=1$ Galactic `RING` regions and the Section 6 cosmic coincidence window $\Omega_i(a)$ vs scale factor $a$.
