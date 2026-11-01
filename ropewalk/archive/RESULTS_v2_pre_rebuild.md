# Ropewalk Multiverse Empirical Test Suite — Final Technical Report (`RESULTS.md`)

- **Version:** `2.0.0` (Revised Post-Final Independent Review `REVIEW_FINAL.md`; All Verdicts and Statistics Unchanged)
- **Original Results Timestamp:** `2026-10-30T07:47:30` (`results/results.json`)
- **Final Review Revision Timestamp:** `2026-10-30T09:10:00`
- **Governing Pre-Registration:** `PREREG.md` (`v1.0.2`), `MULTIVERSE_STAGE1_EQUATIONS.md` (`v1.0.2`), `ASSUMPTIONS.md` (`v1.0.2`)
- **Pre-Registration Cryptographic Proof:** `PREREG_v4.sha256` (`53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b`) + OpenTimestamps proof `PREREG_v4.sha256.ots` (calendar-attested `2026-10-30T08:44:36Z`, anchored at Bitcoin block `973800`)
- **Dataset Freeze Cryptographic Proof:** `DATA_MANIFEST.sha256` (`73135698afb833e7e95e6a85c55475480132300e29f8b7b42d159c037067896d`) + OpenTimestamps proof `DATA_MANIFEST.sha256.ots` (calendar-attested `2026-10-30T08:59:53Z`, anchored at Bitcoin block `973800`)
- **Precedence Clause:** Where `PREREG.md` (`v1.0.2`) and any earlier document disagree, `PREREG.md` (`v1.0.2`) governs. `MULTIVERSE_TESTS_v1.md` is retained as a historical record only.

---

## 1. Executive Summary & Overall Model Verdict

The pre-registered 19-strand Ropewalk Multiverse model (`v1` static leak mechanism) was evaluated under the rules frozen and cryptographically timestamped before data download (`PREREG.md` `v1.0.2`), with one logged runtime deviation (`D1` in `DEVIATIONS.md`), one post-hoc review-logged deviation (`D2`), and cluster inputs hand-extracted by the analyst (`data/MERGERS.csv`). The test suite spans cosmological background expansion (`DESI DR2 BAO` + `Planck 2018` + `Pantheon+` / `DES-SN5YR Dovekie`), cosmic strand budget ratios (`Planck 2018` + `DESI DR2 / post-LUNA BBN`), dissociative galaxy cluster mergers ($N=16$ systems), galaxy rotation curves (`SPARC` 175-galaxy database + `NGC 1052-DF2`), and local Hubble-flow regional heterogeneity (`Pantheon+SH0ES` across `HEALPix` $N_{\rm side}=1$ Galactic `RING` regions).

### Overall Model-Level Verdict (`PREREG.md` Section 3.3)

$$\mathbf{OVERALL\ MODEL\ VERDICT:\quad MODEL\ FALSIFIED\ (FAIL)}$$

Per `PREREG.md` Section 3.3, the global model verdict is decided by the four Primary Pillar Tests (`Pillar 1: T1-L1`, `Pillar 2: T2-A`, `Pillar 3: T4b`, `Pillar 4: T5-A`), where:
- **`MODEL FALSIFIED (FAIL)`:** **At least one (`>= 1`)** of the four primary pillar tests (`T1-L1`, `T2-A`, `T4b`, or `T5-A`) ends in `FAIL`.
- **`MODEL SUPPORTED (PASS)`:** All four primary pillar tests end in `PASS` (after Holm–Bonferroni family-wise error control).
- **`MODEL INCONCLUSIVE`:** Zero primary pillar tests end in `FAIL`, and at least one primary pillar test ends in `INCONCLUSIVE`.

In the executed suite:
- **2 of the 4 Primary Pillars ended in `FAIL`** (`Pillar 2: T2-A` and `Pillar 4: T5-A`).
- **2 of the 4 Primary Pillars ended in `INCONCLUSIVE`** (`Pillar 1: T1-L1` and `Pillar 3: T4b`).
- **0 of the 4 Primary Pillars ended in `PASS`**.

### Master Summary Table of All Registered Tests

| Test ID | Category | Physical Prediction / Hypothesis | Primary / Secondary | Key Measured Statistic | Pre-Registered Threshold (`PREREG.md` `v1.0.2`) | Final Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`T1-L1`** | Cosmology (Expansion) | Unwinding Law 1 $w(a) = -1 + \gamma_u/E(a)$ `[Model Ansatz]` vs $\Lambda$CDM & $w_0w_a$CDM | **Primary Pillar 1** | $\text{P+}: A_r=-1.7119, B_r=+5.4558$<br>$\text{Dov}: A_r=-2.5780, B_r=+7.3552$<br>$p_{\rm T1-L1} = 0.190744$ | Per-run `FAIL`: $B_r > +9.0$ or $A_r > -1.0$<br>Per-run `PASS`: not `FAIL` & $A_r \le -4.0$ & $B_r \le +4.0$<br>Joint `FAIL` if either `FAIL`; `PASS` if both `PASS` + Holm | **`INCONCLUSIVE`** |
| **`T2-A`** | Cosmology (Strand Budget) | $1:6:12$ strand budget + static leak $\mathcal{R}_{\rm pred} = 19\Omega_{bc}-1$ `[Model Ansatz]` vs Planck $5.36 \pm 0.065$ | **Primary Pillar 2** | $\text{P+}: \mathcal{R}_{\rm pred} = 4.8658 \pm 0.1149$ ($3.743\sigma$)<br>$\text{Dov}: \mathcal{R}_{\rm pred} = 4.9045 \pm 0.1094$ ($3.580\sigma$) | `PASS`: $\le 2.0\sigma_{\rm comb}$ in both SN runs<br>`FAIL`: $> 2.0\sigma_{\rm comb}$ in either SN run | **`FAIL`** |
| **`T4b`** | Astrophysics (Clusters) | Merger age cutoff $\tau_{\rm lag}$ separating dark mass with galaxies ($t_p < \tau_{\rm lag}$) vs gas ($t_p \ge \tau_{\rm lag}$) `[Model Ansatz]` | **Primary Pillar 3** | $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ ($\text{Acc}_{\rm train}=87.5\%, 7/8$)<br>Test: $n_{\rm test}=5 < 6$, $k=3$ ($\text{Acc}_{\rm test}=60.0\%$), $n_{\rm gas}=0$ ($13/13$ with galaxies) | `INCONCLUSIVE` if $n_{\rm test} < 6$ (`Rule G8(3)` & `§5.5(3)`); `FAIL` Clauses `1(b)`/`1(c)` require $n_{\rm test} \ge 6$ | **`INCONCLUSIVE`** |
| **`T5-A`** | Astrophysics (Galaxies) | Single universal refraction width $\sigma_{\rm ref}$ across 87 held-out SPARC rotation curves `[Model Ansatz]` | **Primary Pillar 4** | $\hat{\sigma}_{\rm ref} = 9.212795\text{ kpc}$<br>Test $M_{\chi^2} = 45.1259$, $F_{<2} = 0.0690$ (`6/87`) | `PASS`: $M_{\chi^2} \le 1.5$ & $F_{<2} \ge 0.70$<br>`FAIL`: $M_{\chi^2} > 3.0$ or $F_{<2} < 0.40$ | **`FAIL`** |
| **`T1-Sign`** | Cosmology (Dark Energy) | Directional thawing check $w_0 > -1$ in CPL $w_0w_a$CDM fit `[Model Ansatz]` | Secondary Scored | $\text{P+}: P(w_0 > -1) = 0.9960$ ($\sigma_{w_0}=0.0560$)<br>$\text{Dov}: P(w_0 > -1) = 0.9992$ ($\sigma_{w_0}=0.0557$) | `PASS`: $P(w_0 > -1) \ge 0.95$ in both & not `FAIL`<br>`FAIL`: $P(w_0 < -1) \ge 0.95$ in either, or $\sigma_{w_0} \le 0.03$ & $(-1,0) \in 68\%$ CR in both | **`PASS`** |
| **`T2-N1`** | Cosmology (Baryon Share) | Bare strand share $\Omega_b = 1/19 = 0.052632$ `[Model Ansatz]` vs Planck $0.04930 \pm 0.00086$ | Secondary Scored | $+3.8739\sigma$ ($\Delta\Omega_b = +0.003332$, $+6.76\%$) | `PASS`: $\le 2.0\sigma$<br>`FAIL`: $> 2.0\sigma$ (no gap) | **`FAIL`** |
| **`T2-N2`** | Cosmology (Implied $H_0$) | $H_0^{\rm pred} = 100\sqrt{19\omega_b} = 65.1943 \pm 0.2186$ (`Planck 2018` $\omega_b$) `[Model Ansatz]` vs Planck $67.36 \pm 0.54$ | Secondary Scored | $-3.7175\sigma$ ($\Delta H_0 = -2.1657\text{ km s}^{-1}\text{ Mpc}^{-1}$, $\sigma_{\rm comb}=0.5826$) | `PASS`: $\le 2.0\sigma$<br>`FAIL`: $> 2.0\sigma$ (no gap) | **`FAIL`** |
| **`T5-B`** | Astrophysics (Galaxies) | Scaled refraction width $\sigma_{{\rm ref},g} = k R_{d,g}$ across 87 held-out SPARC galaxies `[Model Ansatz]` | Secondary Scored | $\hat{k} = 2.928045$<br>Test $M_{\chi^2} = 23.7412$, $F_{<2} = 0.0805$ (`7/87`) | `PASS`: $M_{\chi^2} \le 1.5$ & $F_{<2} \ge 0.70$<br>`FAIL`: $M_{\chi^2} > 3.0$ or $F_{<2} < 0.40$ | **`FAIL`** |
| **`T5c`** | Astrophysics (UDGs) | NGC 1052-DF2 3D Plummer + NGC 1052 group enclosed dynamical mass check at frozen $\hat{\sigma}_{\rm ref} = 9.212795\text{ kpc}$ `[Model Ansatz]` | Secondary Scored | $M_{\rm pred}(<2.7\text{ kpc}) = 0.9877\times 10^8 M_\odot$<br>$M_{\rm pred}(<3.1\text{ kpc}) = 1.1686\times 10^8 M_\odot$ | `PASS`: $\le 2.9\times 10^8 M_\odot$ at $2.7\text{ kpc}$ & $< 3.2\times 10^8 M_\odot$ at $3.1\text{ kpc}$ | **`PASS`** |
| **`T6`** | Cosmology (Local $H_0$) | Regional $H_0$ heterogeneity across `HEALPix` $N_{\rm side}=1$ Galactic `RING` regions ($0.023 \le z_{\rm HD} \le 0.15$) `[Model Ansatz]` | Secondary Scored | $N_{\rm pix}=9$ (`491` SNe), $\chi^2_{\rm het} = 8.9347$ ($\text{dof}=8$)<br>$p_{\rm het} = 0.347838$, $Z_{\rm all\text{-}sky} = 5.2152\sigma$ | `PASS`: $p_{\rm T6,holm} \le \alpha_{\rm T6}$ & $Z_{\rm all\text{-}sky} \ge 3.0$<br>`FAIL`: $p_{\rm het} > 0.3173$ | **`FAIL`** |
| **`T4a`** | Astrophysics (Clusters) | Young-merger ($t_{\rm col} < \tau_{\rm lag}$) lensing-vs-galaxy offset sign $\Delta_{SI}^{\parallel}$ (`A13b`) `[Model Ansatz]` | Exploratory (Unscored) | Non-Bullet $t_{\rm col} \le 235\text{ Myr}$ / $\le 400\text{ Myr}$ ($N=1$): $\Delta_{SI}^{\parallel} = -45.0 \pm 52.0\text{ kpc}$ ($-0.8654\sigma$); All 10 non-Bullet: $-43.76 \pm 23.76\text{ kpc}$ ($-1.8418\sigma$) | Locked as Exploratory / Unscored (`PREREG.md` Sec 5.4) | **`EXPLORATORY`** |

---

## 2. Pre-Fit Validation Gates (`G9-a` through `G9-d`)

Per `PREREG.md` Section 2 (Rule `G9`), the cosmology and astrophysics numerical engines (`scripts/cosmology.py` and `scripts/sparc_t5.py`) were validated against four numerical gates (`tests/test_gates_g9.py`). As noted in `ACTIVITY_LOG.md`, during the initial gate run (`2026-10-30T05:02:45`) a bug fix was logged to use the Chen, Huang & Wang (2019) early-universe sound-horizon radiation constant ($\omega_r = 1/24185$) for the compressed CMB prior (`Clarification C2` in `DEVIATIONS.md`), after which all four gates passed (`results/validation_gates_g9.json` at `2026-10-30T05:02:56`). Because `scripts/cosmology.py` was subsequently refactored (`2026-10-30T05:39:33` to `06:28:52`) to add vectorized quadrature and pre-inverted SN covariance matrices (`joint_chi2_cpl` and `joint_chi2_law1`), all four gates (plus direct verification of the `joint_chi2_cpl` fast path and `sparc_t5.kernel_f_sigma`) were re-executed on the final unmodified code in `scripts/run_gates_g9_final.py` (`results/validation_gates_g9_final.json` at `2026-10-30T09:05:02`, addressing `REVIEW_FINAL M1`). All four gates pass on both the initial and final code:

| Gate ID | Mapped Tests (`PREREG.md` §2) | Validation Check & Dataset (`PREREG.md` §2) | Pre-Registered Tolerance | Obtained Result (`validation_gates_g9.json` & `validation_gates_g9_final.json`) | Status |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **`G9-a`** | `T1-L1`, `T1-Sign`, `T2-A` | Flat $\Lambda$CDM fit to `DESI DR2 BAO` (unmodified 13-point vector and $13\times 13$ covariance) vs published DESI DR2 $\Omega_m = 0.2975 \pm 0.0086$ (`DESI Collaboration 2025b` Table IV) `[Established]` | $|\hat{\Omega}_m - 0.2975| / 0.0086 \le 0.30\sigma$ | $\hat{\Omega}_m = 0.297180 \pm 0.008616$ ($\chi^2_{\min} = 10.2823$), diff $= \mathbf{0.0373\sigma}$ (fast path: $\hat{\Omega}_m = 0.297180$, diff $= \mathbf{0.0373\sigma}$) | **`PASS`** |
| **`G9-b`** | `T1-L1`, `T1-Sign`, `T2-A` | Flat $\Lambda$CDM fit to compressed `Planck 2018` $(R, \ell_A, 100\omega_b)$ (`Chen, Huang & Wang 2019` Table 1) vs $\Omega_m = 0.3153 \pm 0.0073$, $h = 0.6736 \pm 0.0054$, $100\omega_b = 2.236 \pm 0.015$ `[Established]` | $\le 0.30\sigma$ on $\Omega_m, h, 100\omega_b$ | $\hat{\Omega}_m = 0.315483$ ($0.0251\sigma$), $\hat{h} = 0.673737$ ($0.0254\sigma$), $100\hat{\omega}_b = 2.236000$ ($0.0000\sigma$); $\max = \mathbf{0.0254\sigma}$ (fast path: $\max = \mathbf{0.0254\sigma}$) | **`PASS`** |
| **`G9-c`** | `T1-L1`, `T1-Sign` | CPL $w_0w_a$CDM joint fit (`DESI DR2 BAO` + `Planck 2018` $\Lambda$CDM Table 1 + `DES-SN5YR Dovekie`) vs published full-likelihood `DESI DR2` $w_0 = -0.803 \pm 0.054, w_a = -0.72 \pm 0.21$ (`Popovic et al. 2025` Tables 10–11) `[Established]` | $\le 1.0\sigma$ on $(w_0, w_a)$ | $\hat{w}_0 = -0.822485$ ($\mathbf{0.3608\sigma}$), $\hat{w}_a = -0.630612$ ($\mathbf{0.4257\sigma}$), $\chi^2_{\min} = 1639.3568$ (fast path: $\hat{w}_0 = -0.822493$ [`0.3610σ`], $\hat{w}_a = -0.630584$ [`0.4258σ`]) | **`PASS`** |
| **`G9-d`** | `T5-A`, `T5-B`, `T5c` | Piecewise 3D Gaussian enclosed-mass kernel $\mathcal{F}_\sigma(r, r')$ (`(f3)`) vs `scipy.stats.ncx2.cdf((r/sigma)**2, df=3, nc=(rp/sigma)**2)` (and `chi2.cdf` at $r'=0$) across $(r/\sigma_{\rm ref}) \in \{0.2, 0.5, 1.0, 2.0, 4.0\} \times (r'/\sigma_{\rm ref}) \in \{0.0, 10^{-5}, 0.2, 0.5, 1.0, 2.0, 4.0\}$ `[Established]` | Absolute error $< 10^{-10}$ | $\max\text{ abs error} = \mathbf{1.4397 \times 10^{-11}} < 10^{-10}$ (`max_diff` between `sparc_t5.kernel_f_sigma` and `test_gates_g9.F_sigma_kernel` $= 0.0$) | **`PASS`** |

---

## 3. Stage 2 Parameter Fixing & Freeze Barrier (`FIXED_VALUES.json`)

In accordance with `PREREG.md` Section 2 (`Rule G3`), parameter-fixing procedures were executed and frozen in `results/FREEZE_T1.json` through `results/FREEZE_T6.json` and `results/FIXED_VALUES.json` (`2026-10-30T06:29:35`):

1. **`F1` (`FREEZE_T1.json` & `results.json["T1"]`) — Structural Constants & Unwinding Coefficient $\gamma_u$ (`T1`):**
   - `FREEZE_T1.json` locks the structural constants $N_s = 19$, $N_r = 133$, $\Omega_b^{\rm structural} = 1/19 = 0.05263157894736842$, and the uniform prior bounds $\Omega_{m,{\rm tot}} \in [0.1, 0.6]$, $h \in [0.5, 0.9]$, $100\omega_b \in [1.8, 2.6]$, $\gamma_u \in [0.0, 2.0]$ (Law 1), and $w_0 \in [-3.0, 1.0], w_a \in [-3.0, 2.0]$ with $w_0 + w_a < 0$ (CPL).
   - In the deciding `T1-L1` fits (`results/results.json["T1"]["T1_L1_deciding"]`, `32` walkers, `1000` burn-in, `4000` production steps = `128,000` post-burn-in samples):
     - `Pantheon+` Law 1 chain ($\max|\hat{R}-1| = 0.003458 < 0.01$, $\min\text{ESS} = 2491.6 > 1000$): posterior median $\gamma_u = 0.042946 \pm 0.026160$ (mean $0.044610 \pm 0.025040$, best-fit $\hat{\gamma}_u = 0.038481$), implying $w_0 = -0.957054 \pm 0.026160$ and $w_a = -0.021748 \pm 0.014720$ (mean $-0.023462$).
     - `DES-Dovekie` Law 1 chain ($\max|\hat{R}-1| = 0.000882 < 0.01$, $\min\text{ESS} = 2746.8 > 1000$): posterior median $\gamma_u = 0.045401 \pm 0.025781$ (mean $0.046813 \pm 0.024888$, best-fit $\hat{\gamma}_u = 0.043843$), implying $w_0 = -0.954599 \pm 0.025781$ and $w_a = -0.023131 \pm 0.014626$ (mean $-0.024689$).
2. **`F2` (`FREEZE_T2.json`) — Leak Fraction $f_{\rm leak}$ and Matter Density $\Omega_{bc}$ (`T2-A`):**
   - Fitted using `DESI DR2 BAO` (joint Ly$\alpha$) + conditional $2\times 2$ `Planck 2018` $(R, \ell_A \mid 100\omega_b)$ (`Chen, Huang & Wang 2019` Table 1) + `DESI DR2 / post-LUNA BBN` prior $100\omega_b = 2.218 \pm 0.055$:
     - `T2-A-Pantheon+_deciding` ($\max|\hat{R}-1| = 0.001109$, $\min\text{ESS} = 1909.9$): $\Omega_{bc} = 0.308725 \pm 0.006049$, fixing $f_{\rm leak} = 1 - \frac{19\Omega_{bc}-1}{6} = \mathbf{0.189038 \pm 0.019155}$ and $\mathcal{R}_{\rm pred} = \mathbf{4.865772 \pm 0.114933}$.
     - `T2-A-DES-Dovekie_deciding` ($\max|\hat{R}-1| = 0.000671$, $\min\text{ESS} = 1890.7$ — the minimum ESS across all chains in the study): $\Omega_{bc} = 0.310765 \pm 0.005757$, fixing $f_{\rm leak} = \mathbf{0.182578 \pm 0.018231}$ and $\mathcal{R}_{\rm pred} = \mathbf{4.904531 \pm 0.109383}$.
   - Per `PREREG.md` Section 5.6, the deciding `T2-A-Pantheon+` value $f_{\rm leak} = 0.189038$ ($\mathcal{R}_{\rm pred} = 4.865772$) is passed downstream into `T5-A`, `T5-B`, and `T5c`.
3. **`F3` (`FREEZE_T4.json`) — Merger Phase-Lag Cutoff $\tau_{\rm lag}$ (`T4b`):**
   - Fitted on the 8 odd-indexed training clusters (`#1, #3, #5, #7, #9, #11, #13, #15`; all 8 classified as `"with_galaxies"` under the $2\sigma_{\rm diff}$ rule) over the registered grid $[235, 1500]\text{ Myr}$ in $5\text{ Myr}$ steps (`254` grid points), with ties broken by the **smallest $\tau_{\rm lag}$** (`PREREG.md` §5.5 item 2).
   - Because 7 of the 8 training clusters have $t_p \le 0.80\text{ Gyr}$ (`0.15` to `0.80 Gyr`) and 1 training cluster (`#15 RX J0603.3+4214`) has $t_p = 1.50\text{ Gyr}$, any threshold $\tau_{\rm lag} \in (800, 1500]\text{ Myr}$ achieves the maximum training accuracy $\text{Acc}_{\rm train} = 7/8 = 87.5\%$. Breaking the tie on $(800, 1500]\text{ Myr}$ by the smallest $\tau_{\rm lag}$ fixes $\hat{\tau}_{\rm lag} = \mathbf{805\text{ Myr}}$ (`0.805 Gyr`).
4. **`F4` (`FREEZE_T5.json`) — Refraction Halo Smoothing Width $\sigma_{\rm ref}$ (`T5-A`) and Scale Factor $k$ (`T5-B`):**
   - Minimizing summed reduced chi-squared $\mathcal{L}_{\rm train} = \sum_{g \in \text{train}} \chi^2_{{\rm red},g}$ across the 88 odd-indexed training galaxies in SPARC ($f_{\rm leak} = 0.189038$) via a 200-point log-spaced grid scan over $\sigma_{\rm ref} \in [0.1, 100.0]\text{ kpc}$ (`T5-A`) or $k \in [0.05, 50.0]$ (`T5-B`) followed by bounded `scipy.optimize.minimize_scalar` refinement (`xatol = 1e-5`), with each galaxy's spherical baryon mass profile $M_b^{\rm mono}(<r')$ integrated on the registered 400-point interior grid (`200` linear on $[0, r_1]$ + `200` log on $[r_1, r_{\max}]$) plus 100-point stellar-only exponential tail on $[r_{\max}, r_{\max} + 5\sigma_{\rm ref}]$ (`PREREG.md` §5.6):
     - **`T5-A` frozen universal width:** $\hat{\sigma}_{\rm ref} = \mathbf{9.212795\text{ kpc}}$.
     - **`T5-B` frozen disk-scaled factor:** $\hat{k} = \mathbf{2.928045}$ (where $\sigma_{{\rm ref},g} = k R_{d,g}$).
5. **`F5` (`FREEZE_T6.json`) — SH0ES Calibrator Absolute Magnitude $M_B$ (`T6`):**
   - Fitted on the $N_{\rm cal} = 77$ Cepheid-calibrated SNe (`IS_CALIBRATOR == 1`) using the exact inverse of the $77 \times 77$ submatrix of `Pantheon+SH0ES_stat+sys.cov`:
     - $\hat{M}_B = \mathbf{-19.24888455 \pm 0.03010569\text{ mag}}$ ($\sigma_{M_B}^2 = 9.063527 \times 10^{-4}\text{ mag}^2$).

---

## 4. Detailed Results of Primary Pillar Tests

### 4.1 Pillar 1: `T1-L1` — Unwinding Dynamic Dark Energy Law 1 (`INCONCLUSIVE`)

- **Equations & Likelihood Specification (`PREREG.md` §5.1 & `MULTIVERSE_STAGE1_EQUATIONS.md` §2, §5):**
  - Standard flat FLRW background expansion `[Established, (a2)]`:
    $$E^2(a) = \Omega_\gamma a^{-4} + \Omega_\nu f_\nu(a) + \Omega_{bc}\,a^{-3} + \Omega_{\rm de}\,g(a)$$
  - Ropewalk Unwinding Law 1 `[Model Ansatz, (d4)]`:
    $$w(a) = -1 + \frac{\gamma_u}{E(a)}, \qquad g(a) = \exp\!\left[3\gamma_u\int_a^1 \frac{da'}{a'\,E(a')}\right], \qquad \gamma_u \ge 0$$
    which predicts the exact 1D locus in the $(w_0, w_a)$ plane `[Model Ansatz, (d4)]`:
    $$w_0 = -1 + \gamma_u \ge -1, \qquad w_a = -\frac{3}{2}\gamma_u\left[\Omega_m + \gamma_u(1 - \Omega_m)\right] = -\frac{3}{2}(1 + w_0)\left[\Omega_m + (1 + w_0)(1 - \Omega_m)\right] \le 0$$
  - CPL parameterization `[Established, (a4)]`:
    $$w(a) = w_0 + w_a(1 - a)$$
  - **Ly$\alpha$ BAO + Alcock–Paczyński Specification (`PREREG.md` §5.1):** In `T1-L1`, `T1-Sign`, `T2-A`, and `T2-B`, the $z_{\rm eff} = 2.33$ Ly$\alpha$ row of `desi_bao_dr2` (`8.632 ± 0.101`, `38.99 ± 0.53`, $r = -0.431$) is replaced by the joint 3D correlation + Alcock–Paczyński measurement of `DESI Collaboration (2026, arXiv:2607.27410)`: $D_H(2.33)/r_d = 8.600 \pm 0.066$, $D_M(2.33)/r_d = 39.32 \pm 0.33$, with correlation $r_{D_H,D_M} = -0.431$ (`lya_mode = "joint_ap_deciding"`). Two registered non-deciding sensitivity checks vary this treatment: setting the off-diagonal correlation to $r_{D_H,D_M} = 0.0$ (`lya_mode = "joint_ap_r0"`, labeled `Lya_r0`), and retaining the unmodified 13-row DESI DR2 BAO vector (`lya_mode = "unmodified"`, labeled `unmodified_BAO`).
- **Pre-Registered Decision Rule (`PREREG.md` §5.1):**
  - **Per-run `FAIL` (evaluated first):** $B_r \equiv \chi^2_{\min}(\text{Law 1}) - \chi^2_{\min}(w_0w_a\text{CDM}) > +9.0$ **or** $A_r \equiv \chi^2_{\min}(\text{Law 1}) - \chi^2_{\min}(\Lambda\text{CDM}) > -1.0$.
  - **Per-run `PASS`:** Not per-run `FAIL`, **and** $A_r \le -4.0$ **and** $B_r \le +4.0$.
  - **Per-run `INCONCLUSIVE`:** Neither `PASS` nor `FAIL` (i.e., $-4.0 < A_r \le -1.0$ with $B_r \le +9.0$, or $A_r \le -4.0$ with $+4.0 < B_r \le +9.0$).
  - **Joint `T1-L1` Verdict:** `FAIL` if **either** `Pantheon+` or `DES-Dovekie` is per-run `FAIL`; `PASS` if **both** are per-run `PASS` and $p_{\rm T1\text{-}L1,holm} \le \alpha_{\rm T1\text{-}L1}$; otherwise `INCONCLUSIVE`.
- **Results (`Pantheon+` and `DES-SN5YR Dovekie` Deciding Runs & Sensitivity Variants):**

| Dataset Run | $\chi^2_{\min}(\Lambda\text{CDM})$ | $\chi^2_{\min}(\text{Law 1})$ | $\chi^2_{\min}(w_0w_a\text{CDM})$ | $A_r = \Delta\chi^2(\text{L1}-\Lambda\text{CDM})$ | $B_r = \Delta\chi^2(\text{L1}-w_0w_a)$ | Best-Fit $\hat{\gamma}_u$ (Posterior Median $\pm \sigma_{68}$) | Implied $(w_0, w_a)$ Median | Per-Run Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`Pantheon+` (Deciding)** | `1405.3436` | `1403.6318` | `1398.1760` | **`-1.7119`** | **`+5.4558`** | `0.0385` (`0.0429 ± 0.0262`) | `(-0.9571, -0.0217)` | **`INCONCLUSIVE`** |
| **`DES-Dovekie` (Deciding)** | `1650.9615` | `1648.3835` | `1641.0283` | **`-2.5780`** | **`+7.3552`** | `0.0438` (`0.0454 ± 0.0258`) | `(-0.9546, -0.0231)` | **`INCONCLUSIVE`** |
| `Pantheon+` (`wCDM` CMB Sens.) | `1404.7721` | `1402.8871` | `1397.8764` | `-1.8850` | `+5.0107` | `0.0404` | — | `INCONCLUSIVE` |
| `DES-Dovekie` (`wCDM` CMB Sens.) | `1650.4118` | `1647.6209` | `1640.7926` | `-2.7909` | `+6.8283` | `0.0456` | — | `INCONCLUSIVE` |
| `Pantheon+` (`Lya_r0`: $r_{D_H,D_M}=0$ Sens.) | `1405.5995` | `1403.7816` | `1398.8962` | `-1.8179` | `+4.8853` | `0.0400` | — | `INCONCLUSIVE` |
| `DES-Dovekie` (`Lya_r0`: $r_{D_H,D_M}=0$ Sens.) | `1651.2065` | `1648.5133` | `1641.7942` | `-2.6933` | `+6.7191` | `0.0451` | — | `INCONCLUSIVE` |
| `Pantheon+` (`unmodified_BAO` Sens.) | `1404.1818` | `1402.1952` | `1396.6331` | `-1.9866` | `+5.5621` | `0.0418` | — | `INCONCLUSIVE` |
| `DES-Dovekie` (`unmodified_BAO` Sens.) | `1649.8427` | `1646.9174` | `1639.3567` | `-2.9253` | `+7.5607` | `0.0470` | — | `INCONCLUSIVE` |

- **Physical Interpretation:** Because Law 1 enforces $w(a) = -1 + \gamma_u/E(a)$ with $\gamma_u \ge 0$, it restricts dark energy to $w(a) \ge -1$ at all redshifts (`no phantom crossing`) along the shallow locus `(d4)`. In the deciding fits, the fitted Law 1 implied slope is $w_a = -0.021748 \pm 0.014720$ (`Pantheon+`) and $w_a = -0.023131 \pm 0.014626$ (`DES-Dovekie`), which is **23.6 to 26.6 times shallower** than the unconstrained CPL fits ($w_a = -0.513975 \pm 0.215181$ on `Pantheon+`, best-fit $-0.492555$; and $w_a = -0.615279 \pm 0.222775$ on `DES-Dovekie`, best-fit $-0.596283$). Law 1 improves slightly over $\Lambda$CDM ($A_r = -1.7119$ and $-2.5780$, $p_{\rm T1\text{-}L1} = 0.190744$) but fits worse than the free two-parameter CPL curve by $B_r = +5.4558$ and $+7.3552$. Both runs land in the pre-registered `INCONCLUSIVE` band ($-4.0 < A_r \le -1.0$ and $+4.0 < B_r \le +9.0$): neither confirmed nor ruled out.

---

### 4.2 Pillar 2: `T2-A` — $1:6:12$ Strand Budget & Leak Ratio (`FAIL`)

- **Equations & Priors Tested (`PREREG.md` §5.2 & `MULTIVERSE_STAGE1_EQUATIONS.md` §4):**
  - Present-day $1:6:12$ strand partition with static ($Q=0$) leak `[Model Ansatz, (c3)]`:
    $$\Omega_b = \frac{1}{19}, \qquad \Omega_{\rm dm}(f_{\rm leak}) = \frac{6(1 - f_{\rm leak})}{19}, \qquad \Omega_{\rm de}(f_{\rm leak}) = \frac{12 + 6f_{\rm leak}}{19}$$
  - Leaked dark-to-baryon ratio `[Model Ansatz, (c4)]`:
    $$f_{\rm leak} = 1 - \frac{19\,\Omega_{bc} - 1}{6}, \qquad \mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak}) = 19\,\Omega_{bc} - 1, \qquad \Omega_{bc} \equiv \Omega_{m,{\rm tot}} - \Omega_{\nu,0}$$
  - Single deciding uncorrelated error formula (`PREREG.md` §5.2 & `[A18]`, `[Established]`):
    $$\sigma_{\rm comb} = \sqrt{(19\,\sigma_{\Omega_{bc}})^2 + 0.065^2}, \qquad \mathcal{R}_{\rm Planck} = 5.36 \pm 0.065$$
  - **Fixing Priors (`PREREG.md` §5.2):** `T2-A` fits $\Omega_{bc}$ using `DESI DR2 BAO` (joint Ly$\alpha$) + the conditional $2 \times 2$ `Planck 2018` compressed likelihood $(R, \ell_A \mid 100\omega_b)$ (`Chen, Huang & Wang 2019` Table 1) + the **DESI DR2 / post-LUNA BBN prior** $100\omega_b = 2.218 \pm 0.055$ (`Schöneberg 2024; DESI Collaboration 2025b Eq. 14`).
  - **Pre-Registered Decision Rule (`PREREG.md` §5.2):**
    - **`FAIL`:** $|\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm Planck}| > 2.0\,\sigma_{\rm comb}$ in **either** `Pantheon+` or `DES-Dovekie`.
    - **`PASS`:** $|\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm Planck}| \le 2.0\,\sigma_{\rm comb}$ in **both** `Pantheon+` and `DES-Dovekie`.
- **Results (`T2-A` Deciding & All Sensitivity Variants):**

| Variant / Dataset | BBN Prior & CMB Mode | $\Omega_{bc}$ Posterior | Implied $f_{\rm leak}$ | Predicted $\mathcal{R}_{\rm pred}$ | $\sigma_{\rm comb}$ | Tension vs Planck ($5.36 \pm 0.065$) | Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`T2-A-Pantheon+` (Deciding)** | `DESI/LUNA` (`2.218±0.055`), Cond. $2\times 2$ | `0.308725 ± 0.006049` | `0.189038 ± 0.019155` | **`4.8658 ± 0.1149`** | `0.13204` | **`3.7430σ`** (`> 2.0σ`) | **`FAIL`** |
| **`T2-A-Dovekie` (Deciding)** | `DESI/LUNA` (`2.218±0.055`), Cond. $2\times 2$ | `0.310765 ± 0.005757` | `0.182578 ± 0.018231` | **`4.9045 ± 0.1094`** | `0.12724` | **`3.5796σ`** (`> 2.0σ`) | **`FAIL`** |
| `T2-B-Pantheon+` (Constrained Sens.) | $\omega_b = h^2/19$ imposed in likelihood | `0.318258 ± 0.005753` | `0.158849 ± 0.018218` | `5.0469 ± 0.1093` | `0.12718` | `2.4619σ` ($\Delta\chi^2 = +8.5391$) | `FAIL` |
| `T2-B-Dovekie` (Constrained Sens.) | $\omega_b = h^2/19$ imposed in likelihood | `0.319040 ± 0.005809` | `0.156373 ± 0.018395` | `5.0618 ± 0.1104` | `0.12809` | `2.3284σ` ($\Delta\chi^2 = +9.8219 > 9$) | `FAIL` |
| `T2-A-Pantheon+` (`Cooke+18` BBN Sens.) | `Cooke+18` (`2.166±0.019`), Cond. $2\times 2$ | `0.313999 ± 0.005819` | `0.172337 ± 0.018426` | `4.9660 ± 0.1106` | `0.12825` | `3.0723σ` | `FAIL` |
| `T2-A-Dovekie` (`Cooke+18` BBN Sens.) | `Cooke+18` (`2.166±0.019`), Cond. $2\times 2$ | `0.316469 ± 0.005489` | `0.164514 ± 0.017383` | `5.0129 ± 0.1043` | `0.12290` | `2.8242σ` | `FAIL` |
| `T2-A-Pantheon+` (Marginal $2\times 2$ CMB Sens.) | `DESI/LUNA` (`2.218±0.055`), Marg. $2\times 2$ | `0.310955 ± 0.005821` | `0.181976 ± 0.018434` | `4.9081 ± 0.1106` | `0.12829` | `3.5222σ` | `FAIL` |
| `T2-A-Dovekie` (Marginal $2\times 2$ CMB Sens.) | `DESI/LUNA` (`2.218±0.055`), Marg. $2\times 2$ | `0.312512 ± 0.005336` | `0.177047 ± 0.016897` | `4.9377 ± 0.1014` | `0.12043` | `3.5065σ` | `FAIL` |

- **Physical Interpretation:** Because the model fixes the bare baryon fraction to $\Omega_b = 1/19 = 0.052632$ (`6.76%` higher, i.e., `6.8%` higher than the `Planck 2018` value $\Omega_b = 0.04930 \pm 0.00086$), matching the observed late-time matter fraction $\Omega_{bc} \approx 0.3087\text{–}0.3108$ forces the predicted dark-to-baryon ratio down to $\mathcal{R}_{\rm pred} = 19\Omega_{bc} - 1 = 4.8658\text{–}4.9045$, whereas `Planck 2018` measures $\omega_c/\omega_b = 5.36 \pm 0.065$. Both deciding runs (`3.7430σ` and `3.5796σ`) and all six sensitivity variants miss by more than the $2.0\sigma$ `FAIL` threshold (`2.33σ` to `3.52σ`).

---

### 4.3 Pillar 3: `T4b` — Cluster Merger Age Cutoff $\tau_{\rm lag}$ (`INCONCLUSIVE`)

- **Equations & Rules Tested (`PREREG.md` §5.5 & `MULTIVERSE_STAGE1_EQUATIONS.md` §6):**
  - Two-regime relaxation hypothesis `[Model Ansatz, (e6)–(e7)]`:
    $$\text{Predicted Class}(t_p) = \begin{cases} \text{"with\_galaxies"} & \text{if } t_p < \tau_{\rm lag} \\ \text{"with\_gas"} & \text{if } t_p \ge \tau_{\rm lag} \end{cases}$$
  - Mechanical $2\sigma_{\rm diff}$ classification rule `[Established, PREREG.md §5.5 item 4]`:
    $$\sigma_{\rm diff} = \sqrt{\sigma_I^2 + \sigma_G^2 + \sigma_S^2}, \qquad \begin{cases} d_{IG} - d_{IS} > 2\sigma_{\rm diff} \implies \text{"with\_galaxies"} \\ d_{IS} - d_{IG} > 2\sigma_{\rm diff} \implies \text{"with\_gas"} \\ |d_{IG} - d_{IS}| \le 2\sigma_{\rm diff} \implies \text{"unclassified"} \end{cases}$$
  - **Pre-Registered Decision Rules (`PREREG.md` §5.5):**
    - **FAIL Clause 1(a):** $n_{\rm train} < 6$ or $\max_{\tau_{\rm lag}} \text{Acc}_{\rm train}(\tau_{\rm lag}) < 0.80$.
    - **FAIL Clause 1(b):** $n_{\rm test} \ge 6$ and $\text{Acc}_{\rm test}(\hat{\tau}_{\rm lag}) < 0.60$.
    - **FAIL Clause 1(c):** $n_{\rm test} \ge 6$ and all $n_{\rm test}$ classified test clusters are classified `"with_galaxies"`.
    - **PASS Clause 2:** Not `FAIL`, $n_{\rm test} \ge 6$, $\text{Acc}_{\rm test}(\hat{\tau}_{\rm lag}) \ge 0.80$, $p_{\rm T4b,holm} \le \alpha_{\rm T4b}$, and at least one test cluster with $t_p \ge \hat{\tau}_{\rm lag}$ is observed `"with_gas"`.
    - **INCONCLUSIVE Clause 3 (`Rule G8(3)`):** $n_{\rm test} < 6$ (if Clause 1(a) did not already trigger `FAIL`), or intermediate test accuracy / $p$-value.
- **Complete 16-Cluster Catalog & Classification Results (`data/MERGERS.csv` & `results/results.json["T4"]`):**

| ID | Cluster Name | Common Name | Split | $t_p\text{ (Gyr)}$ | $d_{IS}\text{ (kpc)}$ | $d_{IG}\text{ (kpc)}$ | $\sigma_{\rm diff}\text{ (kpc)}$ | $2\sigma_{\rm diff}\text{ (kpc)}$ | Observed Class | Predicted Class ($\hat{\tau}_{\rm lag}=0.805\text{ Gyr}$) | Match? |
| :-: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `1` | `1E 0657-558` | Bullet Cluster | Train (Odd) | `0.40 ± 0.10` | `25.0` | `161.5` | `29.09` | `58.17` | `with_galaxies` | `with_galaxies` | Yes |
| `2` | `ACT-CL J0102-4915` | El Gordo | **Test (Even)** | `0.75 ± 0.15` | `11.6` | `65.7` | `23.47` | `46.94` | `with_galaxies` | `with_galaxies` | **Yes** |
| `3` | `Abell 1240` | Abell 1240 | Train (Odd) | `0.45 ± 0.15` | `48.0` | `240.0` | `81.55` | `163.10` | `with_galaxies` | `with_galaxies` | Yes |
| `4` | `Abell 1758N` | Abell 1758N | **Test (Even)** | `0.40 ± 0.15` | `101.4` | `76.1` | `50.95` | `101.89` | `unclassified` | `with_galaxies` | — |
| `5` | `Abell 2034` | Abell 2034 | Train (Odd) | `0.30 ± 0.10` | `117.5` | `299.0` | `72.37` | `144.75` | `with_galaxies` | `with_galaxies` | Yes |
| `6` | `Abell 2146` | Abell 2146 | **Test (Even)** | `0.25 ± 0.08` | `1.63` | `30.3` | `5.48` | `10.95` | `with_galaxies` | `with_galaxies` | **Yes** |
| `7` | `Abell 2744` | Pandora's Cluster | Train (Odd) | `0.15 ± 0.05` | `61.7` | `205.0` | `45.36` | `90.72` | `with_galaxies` | `with_galaxies` | Yes |
| `8` | `Abell 3376` | Abell 3376 | **Test (Even)** | `0.55 ± 0.15` | `32.0` | `28.0` | `40.31` | `80.62` | `unclassified` | `with_galaxies` | — |
| `9` | `Abell 520` | Train Wreck | Train (Odd) | `0.80 ± 0.25` | `18.0` | `485.6` | `18.94` | `37.88` | `with_galaxies` | `with_galaxies` | Yes |
| `10` | `Abell 754` | Abell 754 | **Test (Even)** | `0.30 ± 0.10` | `28.0` | `165.0` | `45.71` | `91.41` | `with_galaxies` | `with_galaxies` | **Yes** |
| `11` | `CIZA J2242.8+5301` | Sausage Cluster | Train (Odd) | `0.80 ± 0.15` | `189.0` | `520.0` | `99.37` | `198.75` | `with_galaxies` | `with_galaxies` | Yes |
| `12` | `DLSCL J0916.2+2951` | Musket Ball | **Test (Even)** | `1.10 ± 0.65` | `129.0` | `530.0` | `68.65` | `137.30` | `with_galaxies` | `with_gas` | **No** |
| `13` | `MACS J0025.4-1222` | Baby Bullet | Train (Odd) | `0.50 ± 0.20` | `45.3` | `326.3` | `111.87` | `223.73` | `with_galaxies` | `with_galaxies` | Yes |
| `14` | `MACS J1149.5+2223` | MACS J1149 | **Test (Even)** | `1.16 ± 0.38` | `19.0` | `95.8` | `26.96` | `53.91` | `with_galaxies` | `with_gas` | **No** |
| `15` | `RX J0603.3+4214` | Toothbrush Cluster | Train (Odd) | `1.50 ± 0.30` | `18.0` | `108.3` | `36.73` | `73.46` | `with_galaxies` | `with_gas` | No |
| `16` | `ZwCl 0008.8+5215` | ZwCl 0008 | **Test (Even)** | `0.76 ± 0.21` | `249.0` | `319.0` | `139.10` | `278.21` | `unclassified` | `with_galaxies` | — |

- **Summary of Deciding Split and Sensitivity Analyses (`T4b`):**

| Variant | Registration Status (`PREREG.md` §5.5) | $\hat{\tau}_{\rm lag}\text{ (Gyr)}$ | $n_{\rm train}$ | $\text{Acc}_{\rm train}$ | $n_{\rm test}$ | $\text{Acc}_{\rm test}$ | $n_{\rm gas}$ (`Old Branch`) | Raw $p_{\rm T4b}$ | Verdict & Triggering Rule |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Deciding (Odd/Even, Primary Subcluster)** | **Deciding Primary Test** | `0.805` | `8` | `87.5%` (`7/8`) | `5` | `60.0%` (`3/5`) | `0` | `0.5000` | **`INCONCLUSIVE`** (`Rule G8(3)`: $n_{\rm test} = 5 < 6$) |
| `S1` (Bullet $t_p = 0.40\text{ Gyr}$ Median) | Registered Sensitivity (`1`) | `0.805` | `8` | `87.5%` (`7/8`) | `5` | `60.0%` (`3/5`) | `0` | `0.5000` | `INCONCLUSIVE` ($n_{\rm test} = 5 < 6$) |
| `S2` (Posterior-Weighted Soft Accuracy) | Registered Sensitivity (`2`) | `1.500` | `8` | `93.72%` | `5` | `90.65%` | `0` | — | `Non-Deciding Sensitivity` (pushes $\hat{\tau}_{\rm lag}$ to top of grid because $n_{\rm gas}=0$) |
| `S3` (System-Level Classification) | Registered Sensitivity (`3`) | `0.805` | `8` | `87.5%` (`7/8`) | `5` | `60.0%` (`3/5`) | `0` | `0.5000` | `INCONCLUSIVE` ($n_{\rm test} = 5 < 6$) |
| `S4` (`Abell 520` `Jee+14` `P3` Dark Core) | Registered Sensitivity (`4`) | `0.505` | `8` | `75.0%` (`6/8`) | `5` | `40.0%` (`2/5`) | `1` (`P3`) | `0.8125` | `FAIL` (`Clause 1(a)`: $\max\text{Acc}_{\rm train} = 75.0\% < 80\%$) |
| `S5` (`Abell 520` `Clowe+12` No Dark Core) | Registered Sensitivity (`4`) | `0.805` | `8` | `87.5%` (`7/8`) | `5` | `60.0%` (`3/5`) | `0` | `0.5000` | `INCONCLUSIVE` ($n_{\rm test} = 5 < 6$) |
| `S6` (`Abell 1758N` `Ragozzine+12` Lens Peak) | Registered Sensitivity (`4`) | `0.805` | `8` | `87.5%` (`7/8`) | `6` | `66.7%` (`4/6`) | `0` | `0.34375` | `FAIL` (`Clause 1(c)`: $n_{\rm test}=6 \ge 6$ and all 6 test clusters are `"with_galaxies"`) |
| `S7` (`First-8 Train / Last-8 Test` Split) | **Unregistered Post-Hoc Check** | `0.755` | `6` | `100.0%` (`6/6`) | `7` | `28.57%` (`2/7`) | `0` | `0.9375` | `FAIL` (`Clause 1(b)` & `1(c)`, non-deciding post-hoc split) |

- **Physical Interpretation & Deviation `D2` (`REVIEW_FINAL M3, M6`):**
  1. **Deciding Verdict is `INCONCLUSIVE`:** Because only $n_{\rm test} = 5$ of the 8 held-out even-indexed clusters are classified at $>2\sigma_{\rm diff}$ confidence and `PREREG.md` §5.5 requires $n_{\rm test} \ge 6$ for both `PASS` and `FAIL` Clauses `1(b)` and `1(c)`, the deciding verdict for `T4b` is **`INCONCLUSIVE`**.
  2. **Empirical Absence of `"with_gas"` Mergers:** Across all 13 classifiable primary subclusters (`8` train + `5` test), including the three oldest collisions (`#12 Musket Ball` at $1.10\text{ Gyr}$, `#14 MACS J1149` at $1.16\text{ Gyr}$, and `#15 Toothbrush` at $1.50\text{ Gyr}$), the weak-lensing mass peak stayed with the galaxies (`13/13`), never with the X-ray gas as the model predicted for old collisions. Using the registered alternate `Ragozzine et al. (2012, ApJ 747, 18)` lensing position for `Abell 1758N` (`S6`, non-deciding sensitivity check) classifies 6 held-out clusters and would have made `T4b` a `FAIL` via Clause `1(c)`. (`S7`, the First-8/Last-8 split, was not registered in `PREREG.md` and is an unregistered post-hoc check.)
  3. **Review-Identified Deviation `D2` (`DEVIATIONS.md`):** As documented in `DEVIATIONS.md` (`D2`), `data/MERGERS.csv` recorded $\sigma_S = 0.0\text{ kpc}$ for `Abell 1758N` (test), `Abell 2034` (train), and `Abell 3376` (test) where BCG coordinates were used without an explicit positional error bar, and recorded $\sigma_G = 5.0\text{ kpc}$ for five clusters. Strictly applying the missing-uncertainty rule (`PREREG.md` §5.5 item 5) marks `Abell 2034` `"unclassified"` ($n_{\rm train} = 7$, $\text{Acc}_{\rm train} = 6/7 = 85.7\% \ge 80\%$, $\hat{\tau}_{\rm lag} = 805\text{ Myr}$) while `Abell 1758N` and `Abell 3376` are already `"unclassified"`, and dropping the five $\sigma_G = 5.0\text{ kpc}$ clusters likewise leaves $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ and $n_{\rm test} \le 5$, leaving the `INCONCLUSIVE` verdict unchanged (`REVIEW_FINAL.md` §3 `M3`).

---

### 4.4 Pillar 4: `T5-A` — Universal Refraction Halo Width on Held-Out SPARC Rotation Curves (`FAIL`)

- **Equations & Numerical Protocol Tested (`PREREG.md` §5.6 & `MULTIVERSE_STAGE1_EQUATIONS.md` §7):**
  - Spherical circular velocity from monotonically clipped non-negative baryonic shell masses $dM_b^{\rm mono}(r') \ge 0$ (`\Upsilon_{\rm disk} = 0.50\,M_\odot/L_\odot$, $\Upsilon_{\rm bul} = 0.70\,M_\odot/L_\odot$) `[Established, (f1)]`:
    $$v_c^2(r) = v_{\rm bar}^2(r) + v_{\rm sh}^2(r) = \frac{G\left[M_b^{\rm mono}(< r) + M_{\rm sh}(< r)\right]}{r}$$
  - Enclosed shadow mass under the 3D isotropic Gaussian kernel $K_\sigma(\mathbf{r}) = (2\pi\sigma_{\rm ref}^2)^{-3/2}\exp(-|\mathbf{r}|^2/(2\sigma_{\rm ref}^2))$ `[Model Ansatz, (f3)]`:
    $$M_{\rm sh}(< r) = 6(1 - f_{\rm leak})\int_0^\infty \mathcal{F}_\sigma(r, r')\,dM_b^{\rm mono}(r')$$
    where the piecewise 1D radial enclosed-mass kernel $\mathcal{F}_\sigma(r, r')$ (`[Established]` mathematical identity, non-central $\chi'^2_3(r'^2/\sigma_{\rm ref}^2)$ CDF evaluated at $r^2/\sigma_{\rm ref}^2$) is:
    $$\mathcal{F}_\sigma(r, r') = \begin{cases}
    \displaystyle \frac{1}{2}\left[\operatorname{erf}\!\left(\frac{r + r'}{\sqrt{2}\,\sigma_{\rm ref}}\right) + \operatorname{erf}\!\left(\frac{r - r'}{\sqrt{2}\,\sigma_{\rm ref}}\right)\right] - \frac{1}{\sqrt{2\pi}}\,\frac{\sigma_{\rm ref}}{r'}\left[\exp\!\left(-\frac{(r - r')^2}{2\sigma_{\rm ref}^2}\right) - \exp\!\left(-\frac{(r + r')^2}{2\sigma_{\rm ref}^2}\right)\right], & \dfrac{r'}{\sigma_{\rm ref}} \ge 10^{-4}, \\[12pt]
    \displaystyle \operatorname{erf}\!\left(\frac{r}{\sqrt{2}\,\sigma_{\rm ref}}\right) - \sqrt{\frac{2}{\pi}}\,\frac{r}{\sigma_{\rm ref}}\exp\!\left(-\frac{r^2}{2\sigma_{\rm ref}^2}\right), & \dfrac{r'}{\sigma_{\rm ref}} < 10^{-4}.
    \end{cases}$$
  - **Pre-Registered Quadrature & Tail Rule (`PREREG.md` §5.6):** $M_b^{\rm mono}(<r')$ is evaluated on a 400-point interior grid (`200` linear nodes on $[0, r_1]$ plus `200` log-spaced nodes on $[r_1, r_{\max}]$) and continued on a 100-point linear grid over $[r_{\max}, r_{\max} + 5\sigma_{\rm ref}]$ using the stellar-only exponential tail $\Sigma_b^{\rm tail}(r_{\max}) = 10^6[\Upsilon_{\rm disk}\text{SBdisk}(r_{N_g}) + \Upsilon_{\rm bul}\text{SBbul}(r_{N_g})]\,M_\odot\text{ kpc}^{-2}$, which enters $M_{\rm sh}(<r_j)$ only.
  - **Pre-Registered Decision Rule (`PREREG.md` §5.6):**
    - **`PASS`:** Held-out median $M_{\chi^2} \equiv \text{median}_{g\in{\rm test}}(\chi^2_{{\rm red},g}) \le 1.5$ **and** fraction $F_{<2} \equiv \frac{1}{87}\sum_{g\in{\rm test}}\mathbb{I}(\chi^2_{{\rm red},g} < 2.0) \ge 0.70$.
    - **`FAIL`:** Held-out median $M_{\chi^2} > 3.0$ **or** $F_{<2} < 0.40$.
    - **`INCONCLUSIVE`:** Neither `PASS` nor `FAIL`.
- **Results Across All SPARC Models (`T5-A`, `T5-B`, Sensitivity Losses, Baryon-Only, and RAR Benchmark):**

| Model / Variant | Loss Minimized on 88 Training Galaxies | Frozen Parameter | Train Median $\chi^2_{\rm red}$ ($M_{\chi^2}$) | Train $F_{<2}$ | Held-Out Test Median $\chi^2_{\rm red}$ ($M_{\chi^2}$, $N=87$) | Held-Out Test $F_{<2}$ ($N=87$) | Held-Out Pooled $\chi^2_{\rm red}$ | Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`T5-A` (Deciding Universal $\sigma_{\rm ref}$)** | $\sum \chi^2_{{\rm red},g}$ ($f_{\rm leak}=0.189038$) | $\hat{\sigma}_{\rm ref} = \mathbf{9.212795\text{ kpc}}$ | `48.5128` | `0.0341` (`3/88`) | **`45.1259`** (`> 3.0`) | **`0.0690`** (`6/87`, `< 0.40`) | `324.2171` | **`FAIL`** |
| **`T5-B` (Secondary Scaled $\sigma_{{\rm ref},g} = k R_{d,g}$)** | $\sum \chi^2_{{\rm red},g}$ ($f_{\rm leak}=0.189038$) | $\hat{k} = \mathbf{2.928045}$ | `25.0021` | `0.0568` (`5/88`) | **`23.7412`** (`> 3.0`) | **`0.0805`** (`7/87`, `< 0.40`) | `234.6098` | **`FAIL`** |
| `T5-A` Sensitivity (Total $\chi^2$ Loss) | $\sum \chi^2_g$ ($f_{\rm leak}=0.189038$) | $\hat{\sigma}_{\rm ref} = 8.087430\text{ kpc}$ | `45.9452` | `0.0227` | `41.5529` | `0.0575` (`5/87`) | `412.8754` | `FAIL` |
| `T5-A` Sensitivity (Median $\chi^2_{\rm red}$ Loss) | $\text{median}(\chi^2_{{\rm red},g})$ | $\hat{\sigma}_{\rm ref} = 1.312603\text{ kpc}$ | `25.8421` | `0.0568` | `58.7721` | `0.0920` (`8/87`) | `2252.3747` | `FAIL` |
| `T5-A` Sensitivity (Geometric $f_{\rm leak}=1/6$) | $\sum \chi^2_{{\rm red},g}$ ($f_{\rm leak}=0.166667$) | $\hat{\sigma}_{\rm ref} = 9.645406\text{ kpc}$ | `52.2456` | `0.0341` | `47.6820` | `0.0690` (`6/87`) | `314.3435` | `FAIL` |
| `T5-B` Sensitivity (Total $\chi^2$ Loss) | $\sum \chi^2_g$ ($f_{\rm leak}=0.189038$) | $\hat{k} = 3.237289$ | `26.0623` | `0.0682` | `28.3588` | `0.0690` (`6/87`) | `193.8992` | `FAIL` |
| `T5-B` Sensitivity (Median $\chi^2_{\rm red}$ Loss) | $\text{median}(\chi^2_{{\rm red},g})$ | $\hat{k} = 2.117797$ | `17.7729` | `0.0909` | `23.2360` | `0.0920` (`8/87`) | `458.8992` | `FAIL` |
| **Baryon-Only Baseline** ($\mathcal{R}_{\rm pred}=0$) | Fixed M/L (`0.5, 0.7`) | — | — | — | `77.9221` | `0.0460` (`4/87`) | `526.6150` | Reference |
| **RAR Benchmark** (`McGaugh+16` Fixed $g_\dagger$) | Fixed $g_\dagger = 1.20\times 10^{-10}\text{ m s}^{-2}$ | $g_\dagger = 1.20\times 10^{-10}$ | `12.1025` | `0.1136` | `9.4001` | `0.1149` (`10/87`) | `57.4688` | Reference |
| **RAR Benchmark** (Fitted $g_\dagger$) | $\sum \chi^2_{{\rm red},g}$ | $\hat{g}_\dagger = 1.1478\times 10^{-10}$ | `10.7192` | `0.1364` | `8.4263` | `0.1149` (`10/87`) | `57.2854` | Reference |

- **Physical & Mechanistic Diagnostics (`(f3)` & `(f4)`):**
  1. **Saturation Cap (`(f3)`):** Because $K_\sigma$ is a normalized 3D Gaussian diffusion operator, for any galaxy whose spherically averaged baryon density decreases monotonically outward ($d\bar{\rho}_b/dr \le 0$), the enclosed shadow mass satisfies $M_{\rm sh}(<r) \le \mathcal{R}_{\rm pred}\,M_b^{\rm mono}(<r)$ at every radius $r > 0$, bounding the model's total-to-baryonic acceleration ratio above by $g_{\rm tot}(r)/g_{\rm bar}(r) \le 1 + \mathcal{R}_{\rm pred} = 1 + 6(1 - f_{\rm leak}) = \mathbf{5.8658}$ (`6.000` for $f_{\rm leak}=1/6$). Across the 175 SPARC galaxies (`3391` radial data points), **67 of 175 galaxies (`38.29%`) have at least one radius where the observed boost $V_{\rm obs}^2(r)/V_{\rm bar}^2(r)$ exceeds the model's 5.8658 cap, which is 442 of all 3391 radial points (`13.03%`)**. Moreover, as confirmed by independent review (`REVIEW_FINAL.md` §4 item 5), even choosing the best possible universal width directly on the held-out set only reaches a median reduced chi-squared of $\sim 37$, proving the failure is structural rather than a parameter-tuning artifact.
  2. **Structural Trade-Off:** For high-surface-brightness galaxies (`NGC 2841`, `UGC 02953`), adding $\mathcal{R}_{\rm pred} = 4.8658$ of shadow matter overpredicts inner rotation curves unless $\sigma_{\rm ref}$ is made wide ($\hat{\sigma}_{\rm ref} = 9.2128\text{ kpc}$) to diffuse the shadow mass outward; conversely, for compact dwarf and low-surface-brightness galaxies (`DDO 154`), $\sigma_{\rm ref} = 9.2128\text{ kpc}$ smears nearly all shadow mass outside the last measured radius, leaving the model nearly baryon-only and severely underpredicting $V_{\rm obs}(r)$.
  3. **Kinematic Coherence Length Check (`(f4)`):** Comparing $\hat{\sigma}_{\rm ref} = 9.2128\text{ kpc}$ against the orbital displacement scale $v_c\,\hat{\tau}_{\rm lag}$ across the 135 SPARC galaxies with measured $V_{\rm flat} > 0$ ($\hat{\tau}_{\rm lag} = 0.805\text{ Gyr}$) yields a median $v_c\,\hat{\tau}_{\rm lag} = \mathbf{93.031\text{ kpc}}$ ($\text{IQR} = [65.492, 150.290]\text{ kpc}$), ten times larger than $\hat{\sigma}_{\rm ref} = 9.2128\text{ kpc}$.

---

## 5. Detailed Results of Secondary & Exploratory Tests

### 5.1 `T1-Sign` — Directional Thawing Check $w_0 > -1$ (`PASS`)
- **Pre-Registered Rule (`PREREG.md` §5.1):** `PASS` if in both supernova runs $P(w_0 > -1 \mid \text{data}) \ge 0.95$ and not `FAIL`; `FAIL` if in either run $P(w_0 < -1 \mid \text{data}) \ge 0.95$, or if $\sigma_{w_0} \le 0.03$ and $(w_0, w_a) = (-1, 0)$ lies inside the $68\%$ credible region in both runs.
- In the unconstrained CPL $w_0w_a$CDM MCMC chains (`DESI DR2 BAO` + `Planck 2018` $\Lambda$CDM Table 1 + `SN`):
  - **`Pantheon+`:** $w_0 = -0.854092 \pm 0.055958$ (mean $-0.853765 \pm 0.056226$), $w_a = -0.513975 \pm 0.215181$; posterior probability $P(w_0 > -1 \mid \text{data}) = \mathbf{0.995984 \ge 0.95}$ ($P(w_0 < -1) = 0.004016$, Gaussian $z = +2.6008\sigma$). Because $\sigma_{w_0} = 0.055958 > 0.03$, the $\sigma_{w_0} \le 0.03$ `FAIL` clause does not trigger.
  - **`DES-Dovekie`:** $w_0 = -0.825007 \pm 0.055675$ (mean $-0.824755 \pm 0.056178$), $w_a = -0.615279 \pm 0.222775$; posterior probability $P(w_0 > -1 \mid \text{data}) = \mathbf{0.999219 \ge 0.95}$ ($P(w_0 < -1) = 0.000781$, Gaussian $z = +3.1195\sigma$). Because $\sigma_{w_0} = 0.055675 > 0.03$, the $\sigma_{w_0} \le 0.03$ `FAIL` clause does not trigger.
- Both datasets satisfy $P(w_0 > -1 \mid \text{data}) \ge 0.95$, so `T1-Sign` ends in **`PASS`**. As pre-registered in `PREREG.md` Section 5.1 (`Review B4`), this directional check was already known from published DESI DR2 results and cannot override or rescue the primary `T1-L1` test.

### 5.2 `T2-N1` and `T2-N2` — Bare Baryon Share $\Omega_b = 1/19$ and Implied $H_0$ (`FAIL`)
- **Pre-Registered Rule (`PREREG.md` §5.2):** Both `T2-N1` and `T2-N2` use a two-sided $2.0\sigma$ threshold with no intermediate gap: `PASS` if $\le 2.0\sigma$, `FAIL` if $> 2.0\sigma$.
- **`T2-N1` ($\Omega_b = 1/19$ vs Planck 2018 $\Omega_b = 0.04930 \pm 0.00086$):**
  $$\frac{|\Omega_b^{\rm model} - \Omega_{b,\text{Planck}}|}{\sigma_{\Omega_b,\text{Planck}}} = \frac{|0.0526316 - 0.04930|}{0.00086} = \mathbf{3.8739\sigma > 2.0\sigma} \implies \mathbf{FAIL}$$
- **`T2-N2` ($H_0^{\rm pred} = 100\sqrt{19\omega_b}$ vs Planck 2018 $H_0 = 67.36 \pm 0.54\text{ km s}^{-1}\text{ Mpc}^{-1}$):**
  Using the registered deciding `Planck 2018` physical baryon density $100\omega_b = 2.237 \pm 0.015$ (`PREREG.md` §5.2 & `data/registered_priors.json`, `[Model Ansatz, (c4)]`):
  $$H_0^{\rm pred} = 100\sqrt{19 \times 0.02237} = \mathbf{65.1943 \pm 0.2186\text{ km s}^{-1}\text{ Mpc}^{-1}}$$
  Compared against `Planck 2018` $H_0 = 67.36 \pm 0.54\text{ km s}^{-1}\text{ Mpc}^{-1}$ with uncorrelated combined error $\sigma_{\rm comb} = \sqrt{0.2186^2 + 0.54^2} = 0.5826\text{ km s}^{-1}\text{ Mpc}^{-1}$:
  $$Z_{\rm T2-N2} = \frac{65.1943 - 67.36}{0.5826} = \mathbf{-3.7175\sigma} \quad (|Z| = 3.7175\sigma > 2.0\sigma) \implies \mathbf{FAIL}$$
  *(Sensitivity checks in `results.json["T2"]["T2_N2_secondary"]["sensitivity"]`: using `DESI DR2 / post-LUNA BBN` $100\omega_b = 2.218 \pm 0.055$ gives $H_0^{\rm pred} = 64.9169 \pm 0.8049\text{ km s}^{-1}\text{ Mpc}^{-1}$, which is $-2.5207\sigma$ below Planck $H_0$; using `Cooke+18 BBN` $100\omega_b = 2.166 \pm 0.019$ gives $H_0^{\rm pred} = 64.1514 \pm 0.2814\text{ km s}^{-1}\text{ Mpc}^{-1}$, which is $-5.2695\sigma$ below Planck $H_0$ and $-6.4163\sigma$ below DESI+BBN $H_0 = 68.52 \pm 0.62\text{ km s}^{-1}\text{ Mpc}^{-1}$.)* Because $H_0^{\rm pred} = 65.19\text{ km s}^{-1}\text{ Mpc}^{-1}$ sits below `Planck 2018` ($67.36$), the bare $\Omega_b = 1/19$ rule moves away from the local Hubble value near $73\text{ km s}^{-1}\text{ Mpc}^{-1}$, not toward it.

### 5.3 `T5c` — NGC 1052-DF2 Stress Check (`PASS`)
- Evaluated at the frozen `T5-A` smoothing width $\hat{\sigma}_{\rm ref} = 9.212795\text{ kpc}$ and $f_{\rm leak} = 0.189038$ ($\mathcal{R}_{\rm pred} = 4.8658$) using the pre-registered **3D Plummer sphere** ($M_{*,{\rm DF2}} = 2.0 \times 10^8 M_\odot$, projected half-light radius $R_e = 2.2\text{ kpc}$, $M_b^{\rm DF2}(<r) = M_{*,{\rm DF2}}\,r^3/(r^2 + R_e^2)^{3/2}$) plus the external `NGC 1052` group background ($M_{b,{\rm NGC1052}} = 1.0 \times 10^{11} M_\odot$ at 3D separation $d_{\rm 3D} = \sqrt{3/2}\,d_{\rm proj} = \sqrt{3/2}(80\text{ kpc}) = 98.0\text{ kpc}$) (`PREREG.md` §5.6):
  - At $r = 2.7\text{ kpc}$ (`Danieli+19`): $M_{b,\text{enc}} = 0.9318 \times 10^8 M_\odot$, $M_{\rm sh,DF2} = 0.0559 \times 10^8 M_\odot$, $M_{\rm sh,group} = 0.0 \times 10^8 M_\odot \implies M_{\rm pred}(<2.7\text{ kpc}) = \mathbf{0.9877 \times 10^8 M_\odot \le 2.9 \times 10^8 M_\odot}$.
  - At $r = 3.1\text{ kpc}$ (`van Dokkum+18`): $M_{b,\text{enc}} = 1.0847 \times 10^8 M_\odot$, $M_{\rm sh,DF2} = 0.0839 \times 10^8 M_\odot$, $M_{\rm sh,group} = 0.0 \times 10^8 M_\odot \implies M_{\rm pred}(<3.1\text{ kpc}) = \mathbf{1.1686 \times 10^8 M_\odot < 3.2 \times 10^8 M_\odot}$.
  - At $r = 7.6\text{ kpc}$ (reported for completeness): $M_{b,\text{enc}} = 1.7726 \times 10^8 M_\odot$, $M_{\rm sh,DF2} = 1.0583 \times 10^8 M_\odot \implies M_{\rm pred}(<7.6\text{ kpc}) = 2.8309 \times 10^8 M_\odot$.
- **Verdict:** **`PASS`**. However, `T5c` is not an independent win for the model: it passes only because `T5-A` forced $\hat{\sigma}_{\rm ref}$ to the wide blur $9.2128\text{ kpc}$ (which spreads DF2's shadow mass thin beyond $3.1\text{ kpc}$), and that same wide blur caused `T5-A` to fail on the SPARC rotation curves.

### 5.4 `T6` — Regional $H_0$ Heterogeneity Across `HEALPix` $N_{\rm side}=1$ Regions (`FAIL`)
- **Deciding Run (`Galactic RING`, $0.023 \le z_{\rm HD} \le 0.15$, `IS_CALIBRATOR == 0`, Pre-Fit Sparse-Pixel Merging):**
  - Out of `496` Hubble-flow SNe in `Pantheon+SH0ES.dat` ($0.023 \le z_{\rm HD} \le 0.15$, `IS_CALIBRATOR == 0`), pixels `4` (`3` SNe), `7` (`8` SNe), and `11` (`5` SNe) had $0 < N_{{\rm SN},i} < 10$. Per `PREREG.md` Section 5.7 (`Clarification C1` in `DEVIATIONS.md`), in a single pass in increasing `RING` order $i \in \{0, \dots, 11\}$, each sparse pixel was merged into its edge-sharing neighbor pixel of lowest `RING` index (`4 -> 0`, `7 -> 2`, `11 -> 4`), after which pixel `4` (holding the `5` SNe moved from pixel `11` after its own `3` SNe moved to pixel `0`) remained $<10$ and was dropped, leaving $N_{\rm pix} = 9$ sky regions (`491` Hubble-flow SNe, $\text{dof} = N_{\rm pix} - 1 = 8$). *(Joining pixel `11` transitively into pixel `0`'s merged region retains all `496` SNe across the same $N_{\rm pix} = 9$ regions, giving $\chi^2_{\rm het} = 8.83$, $p_{\rm het} = 0.357 > 0.3173$, also `FAIL`; see `REVIEW_FINAL m1`.)*
  - Using the full non-diagonal $491 \times 491$ Hubble-flow submatrix of `Pantheon+SH0ES_stat+sys.cov` (`(g4)`, `[Established]`):
    - All-sky GLS mean: $\bar{H}_0 = \mathbf{73.5056 \pm 0.2419\text{ (HF)} \pm 1.0474\text{ (tot) km s}^{-1}\text{ Mpc}^{-1}}$ ($Z_{\rm all\text{-}sky} = \mathbf{5.2152\sigma \ge 3.0\sigma}$ vs `Planck 2018` $67.36 \pm 0.54$).
    - Regional $H_0$ range across the 9 sky regions: $\mathbf{72.5255}$ to $\mathbf{75.0888\text{ km s}^{-1}\text{ Mpc}^{-1}}$ (max-minus-min $= 2.5633\text{ km s}^{-1}\text{ Mpc}^{-1}$, RMS scatter $= 0.7232\text{ km s}^{-1}\text{ Mpc}^{-1}$, per-region Hubble-flow errors $0.4665$ to $1.1821\text{ km s}^{-1}\text{ Mpc}^{-1}$).
    - Regional heterogeneity statistic: $\chi^2_{\rm het} = \mathbf{8.9347}$ for $\text{dof} = 8$, giving $p_{\rm het} = \mathbf{0.347838 > 0.3173}$.
  - **Verdict:** **`FAIL`** ($p_{\rm het} = 0.347838 > 0.3173$). No regional variation in $H_0$ is detected at this resolution; the local all-sky value ($73.51 \pm 1.05\text{ km s}^{-1}\text{ Mpc}^{-1}$, $5.22\sigma$ above Planck) reflects an overall offset rather than a regional patchwork.
- **Sensitivity Runs (`T6`):**
  - `Equatorial RING` ($z_{\rm HD}$, merged): $N_{\rm pix} = 11$ (`496` SNe), $\chi^2_{\rm het} = 14.7714$ ($\text{dof}=10$), $p_{\rm het} = 0.140621$ (`INCONCLUSIVE`).
  - `Galactic RING` ($z_{\rm CMB}$, merged): $N_{\rm pix} = 9$ (`487` SNe retained of `492`), $\chi^2_{\rm het} = 14.8090$ ($\text{dof}=8$), $p_{\rm het} = 0.062968$ (`INCONCLUSIVE`).
  - `Galactic RING` ($z_{\rm HD}$, drop sparse without merging): $N_{\rm pix} = 9$ (`480` SNe retained of `496`), $\chi^2_{\rm het} = 8.6121$ ($\text{dof}=8$), $p_{\rm het} = 0.376068 > 0.3173$ (`FAIL`).

### 5.5 `T4a` — Young-Merger Lensing-vs-Galaxy Offset Sign (`EXPLORATORY / UNSCORED`)
- Per `PREREG.md` Section 5.4 (`Review B3`), `T4a` was unconditionally locked as `EXPLORATORY (Unscored)` before data analysis for two reasons: (1) under the physical symmetric harmonic core-passage trajectory `A13b` (`MULTIVERSE_STAGE1_EQUATIONS.md` §6 (e6)), the model predicts a negative offset for $0 < T \lesssim \frac{2}{3}\tau_{\rm lag}$ and a positive offset only for $\frac{2}{3}\tau_{\rm lag} \lesssim T \le \tau_{\rm lag}$, so it does not predict a uniform positive sign across all young mergers; and (2) excluding the Bullet Cluster (`1E 0657-558`) from `Wittman, Golovich & Dawson (2018, ApJ 869, 104)` Table 1 leaves only $N=1$ subcluster (`A2744 S`, $t_{\rm col} = 120\text{ Myr}$) with $t_{\rm col} \le 235\text{ Myr}$ (or $\le 400\text{ Myr}$).
- Under the unified sign convention $\Delta_{SI}^{\parallel} = (\mathbf{x}_I - \mathbf{x}_S)\cdot\hat{\mathbf{s}}_{G\to S} = -\Delta x_{SI}^{\rm W18}$ (`> 0` if dark mass sits ahead of the galaxies away from the gas, `< 0` if dark mass lags toward the gas):
  - **Non-Bullet $t_{\rm col} \le 235\text{ Myr}$ and $\le 400\text{ Myr}$ ($N=1$, `A2744 S`):** $\Delta_{SI}^{\parallel} = -45.0 \pm 52.0\text{ kpc}$ ($z = -0.8654\sigma$, $\beta = +0.2961 \pm 0.3421$).
  - **All 10 non-Bullet subclusters in `Wittman+18` Table 1:** Inverse-variance weighted mean $\bar{\Delta}_{SI}^{\parallel} = -43.7569 \pm 23.7576\text{ kpc}$ ($z = -1.8418\sigma$, $\bar{\beta} = +0.1236 \pm 0.0720$; 3 of 10 have $\Delta_{SI}^{\parallel} > 0$).
  - **All 11 `Wittman+18` Table 1 subclusters (including Bullet):** $\bar{\Delta}_{SI}^{\parallel} = -19.5689 \pm 18.6247\text{ kpc}$ ($z = -1.0507\sigma$, $\bar{\beta} = +0.0984 \pm 0.0685$; 4 of 11 have $\Delta_{SI}^{\parallel} > 0$).
  - **`Harvey et al. (2015)` 72-subcluster ensemble:** $\bar{\beta} = -0.04 \pm 0.07$ ($z = +0.5714\sigma$).
- Because `T4a` was locked as exploratory in `PREREG.md` §5.4 precisely because `A13b` does not predict a uniform positive sign, these offsets are reported as an exploratory diagnostic and are not scored as evidence for or against the model.

---

## 6. Holm–Bonferroni Family-Wise Error Control (`PREREG.md` Section 3.1)

Across the $K = 3$ discovery-style $p$-value tests (`T1-L1`, `T4b`, `T6`) at family-wise error rate $\alpha_{\rm FWE} = 0.05$:

| Rank $m$ | Test ID | Raw Discovery $p$-Value $p_{(m)}$ | Holm–Bonferroni Threshold $\alpha_{\rm FWE}/(K - m + 1)$ | Survives Threshold? ($p_{(m)} \le \alpha_{(m)}$) | Pre-Holm Verdict | Post-Holm Final Verdict |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **`1`** | **`T1-L1`** | `0.19074448` | `0.016667` (`0.05 / 3`) | **No** ($m^* = 1$) | `INCONCLUSIVE` | **`INCONCLUSIVE`** |
| **`2`** | **`T6`** | `0.34783764` | `0.025000` (`0.05 / 2`) | **No** | `FAIL` | **`FAIL`** |
| **`3`** | **`T4b`** | `1.000000` (raw `0.5000`, $n_{\rm test}=5<6 \to p=1.0$) | `0.050000` (`0.05 / 1`) | **No** | `INCONCLUSIVE` | **`INCONCLUSIVE`** |

Because the lowest ranked $p$-value (`T1-L1`, $p_{(1)} = 0.190744$) exceeds $\alpha_{\rm FWE}/3 = 0.016667$, the Holm–Bonferroni stopping rank is $m^* = 1$, and no discovery test achieves `PASS`.

---

## 7. Cosmic Coincidence Window Calculation (`PREREG.md` Section 6)

Under standard flat $\Lambda$CDM expansion (`Planck 2018` parameters: $\Omega_{b,0} = 0.049302$, $\Omega_{{\rm dm},0} = 0.264470$, $\Omega_{{\rm de},0} = 0.684700$, $H_0 = 67.36\text{ km s}^{-1}\text{ Mpc}^{-1}$, cosmic age $t_0 = 13.8005\text{ Gyr}$ `[Established, (h1)]`), we computed the cosmic time duration $\Delta t_{\rm coinc}$ over which the evolving cosmic density shares $\Omega_i(a)$ simultaneously match the Ropewalk target shares $\mathbf{s}_{\rm target}(f_{\rm leak})$ `[Model Ansatz, (h2)]`:

| Target Prescription | Target Shares $(s_b, s_{\rm dm}, s_{\rm de})$ | Present-Day ($a=1$) Max Abs / Rel Error | Criterion `H-Abs` ($\max_i|\Omega_i(a)-s_i| \le 0.05$) | Criterion `H-Rel` ($\max_i|\Omega_i(a)-s_i|/s_i \le 0.10$) | Contains $a=1$? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Geometric $f_{\rm leak} = 1/6$ (`1:5:13`)** | `(0.052632, 0.263158, 0.684211)` | `0.00333` / `6.329%` | $\Delta t_{\rm abs} = \mathbf{2.2549\text{ Gyr}}$ (`16.34%` of $t_0$)<br>$a \in [0.9277, 1.0835]$ ($z \in [-0.0771, +0.0779]$) | $\Delta t_{\rm rel} = \mathbf{0.9269\text{ Gyr}}$ (`6.72%` of $t_0$)<br>$a \in [0.9561, 1.0195]$ ($z \in [-0.0191, +0.0460]$) | **Yes** (both) |
| **Frozen `T2-A-Pantheon+` $f_{\rm leak} = 0.189038$** | `(0.052632, 0.256093, 0.691275)` | `0.00837` / `6.329%` | $\Delta t_{\rm abs} = \mathbf{2.2956\text{ Gyr}}$ (`16.63%` of $t_0$)<br>$a \in [0.9372, 1.0968]$ ($z \in [-0.0882, +0.0670]$) | $\Delta t_{\rm rel} = \mathbf{0.7308\text{ Gyr}}$ (`5.30%` of $t_0$)<br>$a \in [0.9693, 1.0195]$ ($z \in [-0.0191, +0.0317]$) | **Yes** (both) |

Because standard FLRW matter and dark-energy densities scale as $a^{-3}$ and $a^0$ when $Q = 0$, the $1:5:13$ leaked ratio is not an attractor in the `v1` static model, holding to within $10\%$ relative accuracy for only $\Delta t_{\rm rel} = 0.7308\text{–}0.9269\text{ Gyr}$ (`5.30%–6.72%` of $t_0$) around the present epoch.

---

## 8. Limitations & Process Record (`REVIEW_FINAL M1, M3, M7, m1–m4, m7`)

In accordance with `REVIEW_FINAL.md` (`M1`, `M3`, `M7`), we state the scope and limitations of the pre-registration and execution record plainly, without calling the study "fully blind" or "manipulation-free":

1. **What Was Frozen Before Data Download:** The mathematical equations (`MULTIVERSE_STAGE1_EQUATIONS.md` `v1.0.2`), assumptions (`ASSUMPTIONS.md` `v1.0.2`), and decision rules (`PREREG.md` `v1.0.2`) were frozen in `PREREG_v4.sha256` (`53ce966a...`) and calendar-attested via OpenTimestamps (`2026-10-30T08:44:36Z`, anchored at Bitcoin block `973800`) prior to data download (`08:56Z`) and prior to the dataset manifest freeze `DATA_MANIFEST.sha256` (`08:59:53Z`, also anchored at Bitcoin block `973800`).
2. **Cluster Catalog Compilation and Hand-Extraction (`T4b`):**
   - As disclosed in `PREREG.md` Section 5.5 (`N10`), the 16-cluster merger catalog was compiled from the literature by an analyst with prior knowledge of well-known dissociative mergers.
   - During Stage 2, the 8 replacement arXiv TeX/PDF cluster source archives in `data/clusters_arxiv_exact/` (`DEVIATIONS.md` entry `D1`, `2026-10-30T05:17:04` local) were downloaded after `DATA_MANIFEST.sha256` was frozen (`04:59:52` local) and are therefore covered by `RESULTS_v2.sha256` rather than the pre-fit `DATA_MANIFEST.sha256`.
   - The analyst hand-extracted both the odd-indexed training-half and even-indexed test-half cluster positions and offsets into `data/MERGERS.csv` (`05:24:22`, revised `05:31:50` local) before $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ was frozen (`06:29:35` local).
   - As documented in `DEVIATIONS.md` (`D2`, identified during final review), `data/MERGERS.csv` set $\sigma_S = 0.0\text{ kpc}$ for `Abell 1758N` (test), `Abell 2034` (train), and `Abell 3376` (test) instead of marking those rows `"unclassified"` under `PREREG.md` §5.5 item 5, and set $\sigma_G = 5.0\text{ kpc}$ for five clusters. Re-evaluating `T4b` with strict enforcement of `PREREG.md` §5.5 item 5 leaves $\hat{\tau}_{\rm lag} = 805\text{ Myr}$, $n_{\rm test} \le 5$, and the `INCONCLUSIVE` verdict unchanged (`REVIEW_FINAL.md` §3 `M3`).
3. **Post-Gate Code Refactoring and Final-Code Gate Verification (`M1`):**
   - The initial validation gate run (`results/validation_gates_g9.json`, `05:02:56` local) was executed before `scripts/cosmology.py` was refactored (`05:39:33` to `06:28:52` local) to add vectorized quadrature and pre-inverted covariance routines (`joint_chi2_cpl`, `joint_chi2_law1`). Re-running all four validation gates on the final unmodified codebase (`scripts/run_gates_g9_final.py` $\to$ `results/validation_gates_g9_final.json`) confirmed that all four gates pass on both the standard and fast likelihood paths.
4. **Independent Re-Derivation:** An independent reviewer (`REVIEW_FINAL.md`) recomputed `T6` and `T5-A/B/c` from the hash-verified public data files using independent code, re-minimized the `T1-L1` likelihoods against an independent quad/ODE integrator, and verified `T2-A`, `T2-N1`, `T2-N2`, `T4b`, and the Holm–Bonferroni sort, confirming every scored test verdict and the overall `MODEL FALSIFIED (FAIL)` verdict.

---

## 9. What Changes for the Film (`REVIEW_FINAL.md` Section 4)

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

## 10. Figures Generated (`results/figures/`)

1. `results/figures/fig1_t1_unwinding_vs_desi.png`: $(w_0, w_a)$ posterior contours (`68%` and `95%`) for `Pantheon+` and `DES-Dovekie` CPL fits vs the `T1-L1` Unwinding Law 1 curve (`(d4)`) and `w(z)` redshift evolution.
2. `results/figures/fig2_t2_strand_budget_tension.png`: `T2-A` and `T2-B` posteriors on $\mathcal{R}_{\rm pred} = 19\Omega_{bc}-1$ vs `Planck 2018` (`5.36 ± 0.065`) and `T2-N1`/`T2-N2` tension bars (`+3.87σ` and `-3.72σ`).
3. `results/figures/fig3_t4b_cluster_mergers.png`: `T4b` 16-cluster separation difference $(d_{IG} - d_{IS}) / (2\sigma_{\rm diff})$ vs time since pericenter $t_p$ and training/test accuracy curve vs $\tau_{\rm lag}$.
4. `results/figures/fig4_t5_sparc_rotation_curves.png`: Held-out SPARC $\chi^2_{\rm red}$ cumulative distributions (`T5-A`, `T5-B`, RAR, Baryon-only) and six representative held-out rotation curves showing the $1+\mathcal{R}_{\rm pred} = 5.8658$ 3D Gaussian saturation cap.
5. `results/figures/fig5_t6_regional_h0_and_coincidence.png`: `T6` regional $H_{0,k}$ across the 9 retained `HEALPix` $N_{\rm side}=1$ Galactic `RING` regions and the Section 6 cosmic coincidence window $\Omega_i(a)$ vs scale factor $a$.
