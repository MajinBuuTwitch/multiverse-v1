# Phase 3 Blind-Injection Independent Rescore & Trustworthiness Report

**Workspace**: `D:\Multiverse Review`  
**Scoring Script**: `score_phase3.py` (Python standard library only, deterministic, zero external dependencies)  
**Input Files Audited**: `ANSWER_KEY.json`, `PHASE3_ANALYSIS_PLAN.md`, `PHASE3_INJECTION_SPEC_SEALED.txt`, `PHASE3_INJECTION_v1.sha256`, `PHASE3_RESULTS_v1.sha256`, `results.json`

---

## Executive Summary

1. **Step 1 · Integrity**: **PASS (`MATCH` on all files)**. Every input file in `D:\Multiverse Review` matches its SHA-256 digest in `PHASE3_INJECTION_v1.sha256` and/or `PHASE3_RESULTS_v1.sha256`, and `ANSWER_KEY.json`'s embedded `spec_sha256` matches `PHASE3_INJECTION_SPEC_SEALED.txt`.
2. **Step 2 · Criterion S1 (Parameter Recovery)**:
   - **COSMO (`C1, C2, C3`)**:
     - Under **well-specified unconstrained `CPL` (`full_3x3`)** in `Reading A`, **every fitted parameter ($\Omega_{bc}, h, 100\omega_b, w_0, w_a$) passes S1** in `C1` (both SN sets), `C3` (both SN sets), and `C2` (`Pantheon+`), with only `C2` `DES-Dovekie` $\Omega_{bc}$ missing on 95% CI coverage (`3/5` in CI, despite small mean bias $|b|/\sigma = 0.088$). Under `T2A_CPL` (`Reading A`), all 5 parameters pass S1 across both `Pantheon+` and `DES-Dovekie` in `C1` and `C3`, and all 5 pass in `C2` `DES-Dovekie` (`5/5` in CI) and `C2` `Pantheon+` (`4/5` or `5/5`).
     - In **`Reading B`**, a systematic sound-horizon offset relative to the mock generator pushes `100_omega_b` mean bias slightly above $1\sigma$ in `T2A_CPL` (`|b|/\sigma = 1.08\text{--}1.30`) and `LCDM` (`|b|/\sigma = 1.01\text{--}1.04`), while `CPL` still passes all 5 parameters in `C1` (`Pantheon+`), `C2` (`Pantheon+`), and `C3` (both SN sets).
     - In **`Law 1` fits**, `C1` ($\Lambda\text{CDM}$, true $\gamma_u = 0$) fails S1 on $\gamma_u$ (`0/5` equal-tailed `ci95` coverage, $|b|/\sigma = 1.45\text{--}1.58$), $100\omega_b$ (`|b|/\sigma = 1.15\text{--}1.31$), and $h$ (in 3 of 4 reading×SN combinations) because $\gamma_u = 0$ lies on the hard lower boundary of the prior $\gamma_u \in [0, 2]$, forcing $\gamma_u > 0$ and dragging $h$ down and $100\omega_b$ up. In `C2` (`Law 1` truth, $\gamma_u = 0.10$), `Law 1` recovers $h$, $100\omega_b$, and $\gamma_u$ (`PASS` across all 4 reading×SN combinations), but $\Omega_{bc}$ has `3/5` 95% CI coverage (**MISS** on coverage despite small mean bias $|b|/\sigma = 0.02\text{--}0.86$). In `C3` (off-curve CPL), `Law 1` and `LCDM` are intentionally misspecified models and fail S1 on $\Omega_{bc}$ and $100\omega_b$ (`|b|/\sigma = 2.0\text{--}4.6$).
   - **GALAXY (`G1, G2`)**: **PASS unconditionally (`5/5` in `G1`, `4/5` or `5/5` in `G2`, $|b|/\sigma \le 0.493`)** across all three reported uncertainty methods (`bootstrap_train_galaxies`, `posterior_sum_chi2_red`, `posterior_total_chi2`) and under both posterior-mean and point-estimate bias definitions.
   - **REGIONAL (`H1, H2, H3`)**: Under the primary reading (`sigma_H0_total_incl_cal` on absolute regional $H_{0,i}$), `H1` passes **9/9 regions** (`40/45 = 88.9%` pooled in 95% CI, **PASS**), `H2` passes **9/9 regions** (`41/45 = 91.1%` pooled, **PASS**), and `H3` passes **8/9 regions** (`43/45 = 95.6%` pooled, **PASS** on pooled/universe/all-sky readings, **PARTIAL 8/9** if requiring all 9 regions individually; only Region 0 has `3/5` coverage). Using `sigma_H0_hf_only` on uncalibrated absolute $H_{0,i}$ fails S1 (`1/9` to `3/9` regions) because it omits the common Cepheid zero-point scatter ($\sim 1.0\text{ km/s/Mpc}$); removing the calibrator draw (`cal_corr_hf`) or subtracting the SN-count-weighted universe mean (`rel_count_wt_hf`) restores **9/9 regions PASS** across `H1`, `H2`, and `H3`.
3. **Step 2 · Criterion S2 (Expected Verdicts)**:
   - **Decisive Pillars (`T5-A`, `T2-A`, `T1-L1`)**: **PASS (`4/5` or `5/5` in every case)** across all readings (`Reading B`, `Reading A`) and all supernova sets (`Joint`, `Pantheon+`, `DES-Dovekie`).
   - **Secondary/Auxiliary S2 Checks**:
     - `C1` `γ_u's 95% interval includes 0`: **MISS (`0/5`)** under equal-tailed percentile `ci95 = [p2.5, p97.5]` (which structurally excludes $0$ for any continuous prior on $[0, 2]$), but **PASS (`5/5`)** under Gaussian `mean ± 1.96*std` ($z \in [1.22, 1.87]$).
     - `C1` & `C2` `T2-N1` and `T2-N2`: **PASS (`5/5`)** under primary Planck-$\omega_b$ reference (`T2-N2` misses `1/5` in `C1` only under the secondary wider BBN-prior sensitivity check).
     - `C2` `T1-Sign PASS`: **PASS** in `Reading B` (`5/5` P+, `4/5` DD, `4/5` Joint) and `Reading A` `Pantheon+` (`4/5`) and `Law 1` $z_{\gamma_u} \ge 2.5$ (`5/5`), but **MISS (`3/5`)** in `Reading A` `DES-Dovekie` and `Joint` CPL (`U-BKI0` $P=0.9335$, `U-J91F` $P=0.9048$ vs $0.95$ threshold).
     - `G3` median $\chi^2_{\rm red}$: Test-half medians across the 5 realizations are **`51.02, 51.74, 46.96, 52.22, 56.12`** (mean **`51.61`**); training-half medians are **`46.99, 47.15, 45.27, 48.44, 45.42`** (mean **`46.65`**), closely reproducing the real-data value (`~45`).
     - `H1`: Strict `T6 FAIL` ($p_{\rm het} > 0.3173$) is **MISS (`3/5`: `FAIL, INCONCLUSIVE, INCONCLUSIVE, FAIL, FAIL`)** because a true uniform $p$-value lands in $[0.0027, 0.3173]$ (`INCONCLUSIVE`) $31.46\%$ of the time by chance; under "no variation detected" (`not PASS`, $p_{\rm het} > 0.0027$), `H1` is **PASS (`5/5`)**.
     - `H3`: **PASS (`4/5` registered `T6 PASS`, `5/5` with $p_{\rm het} = 0.0 \le 0.0027$)**. One realization (`U-JNXP`) is labeled `INCONCLUSIVE` solely because a downward GLS bias in $\bar{H}_0$ plus a $-1.91\sigma$ calibrator draw pushed $Z_{\text{all-sky}} = 2.9751 < 3.0$ despite $\chi^2_{\rm het} = 451.44$.
     - `H2` (Diagnostic): Detection rate is **`4/5` (`80%`)** (`INCONCLUSIVE, PASS, PASS, PASS, PASS`).
4. **Step 2 · Criterion S3 (Pipeline Validation)**:
   - **Pillar `T5-A (G1, G2, G3)`**: **MET unconditionally** (both S2 and S1 hold across all readings and uncertainty methods).
   - **Pillar `T2-A (C1, C2)`**: **S2 is MET (`4/5` or `5/5`)** across all readings/SN sets. **S1 is NOT MET under strict all-fit scoring** because `C2` $\Omega_{bc}$ has `3/5` 95% CI coverage in `Law 1` (both SN sets) and `DES-Dovekie` (`Reading B`), and `Reading B` shifts `100_omega_b` by $>1\sigma$ in `T2A_CPL`. Under **matched-model `T2A_CPL`/`CPL` in `Reading A`**, S1 is **MET** in `Pantheon+` (`C1` and `C2`) and `DES-Dovekie` (`T2A_CPL` `5/5` in both `C1` and `C2`).
   - **Pillar `T1-L1 (C2, C3)`**: **S2 is MET (`5/5`)** across all readings/SN sets. **S1 is MET under matched-model `CPL` (`full_3x3`)** in `C3` (both SN sets and readings) and `C2` (`Pantheon+`), but **NOT MET under strict all-fit scoring** due to `C2` `Law 1` $\Omega_{bc}$ (`3/5` coverage) and misspecified `Law 1`/`LCDM` fits on `C3`.
5. **Step 2 · Criterion S4**: Stated verbatim in §2.5 below; Phase 3 does not alter real-data Stage 2 verdicts, and establishes high confidence in `T5-A`, `T2-A`, and `T1-L1` verdicts alongside specific statistical caveats documented in Step 3.

---

## 1. Step 1 · Integrity Verification

All six files in `D:\Multiverse Review` were hashed with SHA-256 and cross-matched by digest against `PHASE3_INJECTION_v1.sha256` (186 file entries) and `PHASE3_RESULTS_v1.sha256` (50 file entries). In addition, `ANSWER_KEY.json` contains `"spec_sha256": "4b00df423c3738d4c7189ac0a883b72169e9f9a66afca5928a06c230f6c9a7a9"`, which matches `PHASE3_INJECTION_SPEC_SEALED.txt` exactly.

| Workspace File | Computed SHA-256 Digest | Matched Path(s) in `PHASE3_INJECTION_v1.sha256` | Matched Path(s) in `PHASE3_RESULTS_v1.sha256` | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ANSWER_KEY.json` | `9238e52bf0597e8183da68b8441310cbc46db1df9f27e204a6dcedd82ec1a914` | `SEALED/ANSWER_KEY.json` | — | **MATCH** |
| `PHASE3_ANALYSIS_PLAN.md` | `8476aeb01096c266a683e6baed9788fffdb1e227738b3c653c382c2ff82b431d` | — | `PHASE3_ANALYSIS_PLAN.md`, `phase3/PHASE3_ANALYSIS_PLAN.md` | **MATCH** |
| `PHASE3_INJECTION_SPEC_SEALED.txt` | `4b00df423c3738d4c7189ac0a883b72169e9f9a66afca5928a06c230f6c9a7a9` | `SEALED/PHASE3_INJECTION_SPEC_SEALED.txt` | — | **MATCH** |
| `results.json` | `a1e667f5cec1a11f77f2b16c91fefd5c21d9a9de1226ce333291f09f8b7dba01` | — | `phase3/results.json` | **MATCH** |
| `PHASE3_INJECTION_v1.sha256` | `ca63ae040004bd57c2f8ec6bd969f599af3acdd7390716028d50ec8aa134c9de` | *(Manifest file itself)* | — | **MANIFEST (MATCH)** |
| `PHASE3_RESULTS_v1.sha256` | `8d4a38dfcbd5d47befd3114b9c269ff63c10c32f20994e459d65da1da45bea08` | — | *(Manifest file itself)* | **MANIFEST (MATCH)** |

---

## 2. Step 2 · Scoring Against Locked Criteria (S1–S4)

### 2.1 Explicit Judgment Calls & Open Choices

Where `PHASE3_INJECTION_SPEC_SEALED.txt` (§4) and `PHASE3_ANALYSIS_PLAN.md` leave choices open, every reasonable reading is scored below without silent selection:

1. **COSMO Reading (`Reading B` vs `Reading A`) & Supernova Dataset (`Pantheon+` vs `DES-Dovekie` vs `Joint`)**:
   - `PHASE3_ANALYSIS_PLAN.md` (§1.3) locks **`Reading B`** (published/cached reference constants + $3\times 3$ Planck $(R, l_A, \omega_b)$ compressed covariance) as the pipeline's primary blind run and **`Reading A`** (per-mock `references.json` + exact Hu–Sugiyama $z_*$ formula) as secondary. However, in Step 3 we show that `Reading A`'s sound-horizon convention matches the mock generator much more closely than `Reading B`. Both readings and both supernova sets (`PantheonPlus` and `DES_Dovekie`, plus `Joint` for S2) are scored in full.
2. **COSMO Fitted Model Selection (`Law 1`, `CPL`, `T2A_CPL`, `LCDM`)**:
   - For each COSMO universe, `results.json` fits four models: `Law 1` ($\Omega_{bc}, h, 100\omega_b, \gamma_u$ with $3\times 3$ Planck prior), `CPL` ($\Omega_{bc}, h, 100\omega_b, w_0, w_a$ with $3\times 3$ Planck prior, used for `T1-L1` and `T1-Sign`), `T2A_CPL` ($\Omega_{bc}, h, 100\omega_b, w_0, w_a$ with conditional $2\times 2$ $(R, l_A)$ covariance + BBN prior, used for `T2-A`), and `LCDM` ($\Omega_{bc}, h, 100\omega_b$).
   - **Primary reading for S1**: Evaluate each truth under its **matched generating model** (`LCDM`, `CPL`, `T2A_CPL`, and `Law 1` for `C1`; `Law 1`, tangent `CPL`, and `T2A_CPL` for `C2`; `CPL` and `T2A_CPL` for `C3`), while also reporting the misspecified fits (`LCDM` on `C2`/`C3` and `Law 1` on `C3`) for completeness. For `C2` under `CPL`/`T2A_CPL`, we score $(w_0, w_a)$ against the truth's locked effective tangent parameters from `ANSWER_KEY.json` (`w0_fit = -0.90`, `wa_tangent = -0.05783068783068783`).
3. **COSMO Interval & Summary Definitions (`ci95` + `mean/std` vs Gaussian `mean ± 1.96*std` vs `median/sigma_68`)**:
   - **Primary reading**: Use the pipeline's reported 95% credible interval `ci95 = [p2.5, p97.5]`, posterior `mean` for bias ($\text{mean}(\hat{\theta}) - \theta_{\rm true}$), and mean posterior `std` for $\sigma$, as defined in `PHASE3_ANALYSIS_PLAN.md` §1.5.
   - **Alternative readings**: (a) Symmetric Gaussian 95% interval `mean ± 1.96 * std` (decisive for boundary parameter $\gamma_u = 0$ in `C1`, where equal-tailed `[p2.5, p97.5]` structurally cannot include `0`); (b) Posterior `median` and `sigma_68 = (p84 - p16)/2`.
4. **GALAXY (`T5-A`) Uncertainty Method (`bootstrap_train_galaxies` vs `posterior_sum_chi2_red` vs `posterior_total_chi2`) & Point Estimate vs Mean**:
   - **Primary reading**: `bootstrap_train_galaxies` (2,000 galaxy-level bootstrap resamples of the 88 training galaxies), because `T5-A` is fit by minimizing the unweighted sum of per-galaxy reduced $\chi^2_{\rm red}$ across galaxies and only the bootstrap estimator reflects the true galaxy-to-galaxy sampling variance. Both `posterior_sum_chi2_red` and `posterior_total_chi2`, and both uncertainty-distribution `mean` and grid point estimate `fitted_sigma_ref_kpc`, are scored alongside it.
5. **REGIONAL (`T6`) Uncertainty Definition & Multi-Region Aggregation (`9` regions × `5` realizations)**:
   - **Primary reading (`abs_total`)**: Compare each region's fitted `H0_kms_Mpc` against `ANSWER_KEY.json`'s `H0_regions[r]` using `sigma_H0_total_incl_cal` ($\text{CI}_{95} = \hat{H}_{0,i} \pm 1.96\,\sigma_{\rm total}$). This is primary because `H0_kms_Mpc` is an absolute $H_0$ value shifted in every universe by the random Cepheid calibrator zero-point draw ($\hat{M}_B - M_{\rm true}$, with $\sigma_{M_B} \approx 0.030\text{ mag} \implies \sigma_{H_0,\text{cal}} \approx 1.0\text{ km/s/Mpc}$).
   - **Alternative error-bar/reference readings**:
     - `abs_hf`: Compare raw `H0_kms_Mpc` against `H0_regions[r]` using `sigma_H0_hf_only` (omits calibrator variance).
     - `cal_corr_hf`: Remove the exact Cepheid calibrator offset ($\hat{H}_{0,i}^{\rm corr} = \hat{H}_{0,i} \cdot 10^{-0.2(\hat{M}_B - M_{\rm true})}$) and score against `H0_regions[r]` with `sigma_H0_hf_only`.
     - `rel_count_wt_hf`: Score regional relative offsets $\Delta H_{0,i} = \hat{H}_{0,i} - \bar{H}_{0,\text{count-wt}}$ against true $\Delta H_{0,i}^{\rm true} = H_{0,i}^{\rm true} - 73.0$ using `sigma_H0_hf_only`.
     - `rel_gls_bar_hf`: Score regional relative offsets $\hat{H}_{0,i} - \bar{H}_0(\text{GLS})$ against $H_{0,i}^{\rm true} - 73.0$ using `sigma_H0_hf_only`.
   - **Multi-region aggregation readings**: We score (i) **Per-region across 5 realizations** (9 regions per truth, each requiring $\ge 4/5$ in 95% CI and $|\text{mean bias}| < \text{mean }\sigma$), (ii) **Pooled across all 45 region-realizations** per truth ($\ge 36/45 = 80\%$ in 95% CI and $|\text{grand mean bias}| < \text{grand mean }\sigma$), (iii) **Universe-level** ($\ge 4/5$ universes having $\ge 8/9$ or $\ge 7/9$ regions in 95% CI), and (iv) **All-sky $\bar{H}_0$** vs $73.0\text{ km/s/Mpc}$.
6. **S2 Open Choices (`C1` $\gamma_u$ interval, `T2-A` chain source, `T2-N2` BBN sensitivity, `H1` `FAIL` vs `not PASS`, `H3` registered rule vs $p_{\rm het}$)**:
   - All variants are scored side by side in §2.3.

---

### 2.2 Criterion S1 · Parameter Recovery Tables

**Locked Rule (S1)**: *"For every truth and every fitted parameter, the true value lies inside the pipeline's reported 95% interval in at least 4 of 5 realizations, and the mean bias across the 5 realizations is smaller than the mean posterior $\sigma$."*

#### 2.2.1 COSMO Family — Truth `C1` ($\Lambda\text{CDM}$: $\Omega_{bc}=0.313772, h=0.6736, 100\omega_b=2.237, \gamma_u=0, w_0=-1, w_a=0$)

Universes (Rounds 1–5): `U-YIG4`, `U-Y2N1`, `U-099J`, `U-2B0Y`, `U-OEDW`.

| Reading | SN Dataset | Fit Model | Parameter | True Value | Mean Recovered | Mean Signed Bias ($b$) | Mean Posterior $\sigma$ | $|b|/\sigma$ | In `ci95` `[p2.5, p97.5]` | Primary Verdict (`ci95` & `mean/std`) | In Gaussian `mean±1.96σ` | Gaussian Verdict | `median` / `σ68` Verdict |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Reading B** | **Pantheon+** | `Law1` | `Omega_bc` | `0.313772` | `0.315374` | `+0.001602` | `0.004722` | `0.339` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `Law1` | `h` | `0.673600` | `0.668132` | `-0.005468` | `0.004501` | `1.215` | `5/5` | **MISS** | `5/5` | **MISS** | **MISS** |
| **Reading B** | **Pantheon+** | `Law1` | `100_omega_b` | `2.237000` | `2.253511` | `+0.016511` | `0.012657` | `1.304` | `4/5` | **MISS** | `4/5` | **MISS** | **MISS** |
| **Reading B** | **Pantheon+** | `Law1` | `gamma_u` | `0.000000` | `0.030889` | `+0.030889` | `0.020855` | `1.481` | `0/5` | **MISS** | `5/5` | **MISS** | **MISS** |
| **Reading B** | **Pantheon+** | `CPL` | `Omega_bc` | `0.313772` | `0.314236` | `+0.000464` | `0.005799` | `0.080` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `CPL` | `h` | `0.673600` | `0.671151` | `-0.002449` | `0.005923` | `0.413` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `CPL` | `100_omega_b` | `2.237000` | `2.247391` | `+0.010391` | `0.013905` | `0.747` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `CPL` | `w0` | `-1.000000` | `-0.953241` | `+0.046759` | `0.053474` | `0.874` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `CPL` | `wa` | `0.000000` | `-0.175350` | `-0.175350` | `0.201078` | `0.872` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `T2A_CPL` | `Omega_bc` | `0.313772` | `0.311587` | `-0.002186` | `0.006258` | `0.349` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `T2A_CPL` | `h` | `0.673600` | `0.671787` | `-0.001813` | `0.005952` | `0.305` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `T2A_CPL` | `100_omega_b` | `2.237000` | `2.277926` | `+0.040926` | `0.033077` | `1.237` | `4/5` | **MISS** | `4/5` | **MISS** | **MISS** |
| **Reading B** | **Pantheon+** | `T2A_CPL` | `w0` | `-1.000000` | `-0.970280` | `+0.029720` | `0.054848` | `0.542` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `T2A_CPL` | `wa` | `0.000000` | `-0.038791` | `-0.038791` | `0.234542` | `0.165` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `LCDM` | `Omega_bc` | `0.313772` | `0.311411` | `-0.002361` | `0.003835` | `0.616` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `LCDM` | `h` | `0.673600` | `0.673321` | `-0.000279` | `0.002877` | `0.097` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `LCDM` | `100_omega_b` | `2.237000` | `2.250015` | `+0.013015` | `0.012468` | `1.044` | `4/5` | **MISS** | `4/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `Law1` | `Omega_bc` | `0.313772` | `0.315654` | `+0.001882` | `0.004588` | `0.410` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `Law1` | `h` | `0.673600` | `0.668016` | `-0.005584` | `0.004215` | `1.325` | `4/5` | **MISS** | `4/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `Law1` | `100_omega_b` | `2.237000` | `2.253526` | `+0.016526` | `0.012640` | `1.307` | `4/5` | **MISS** | `4/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `Law1` | `gamma_u` | `0.000000` | `0.031523` | `+0.031523` | `0.020030` | `1.574` | `0/5` | **MISS** | `5/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `CPL` | `Omega_bc` | `0.313772` | `0.315262` | `+0.001490` | `0.005318` | `0.280` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `CPL` | `h` | `0.673600` | `0.669870` | `-0.003730` | `0.005259` | `0.709` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `CPL` | `100_omega_b` | `2.237000` | `2.248447` | `+0.011447` | `0.013831` | `0.828` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `CPL` | `w0` | `-1.000000` | `-0.946716` | `+0.053284` | `0.050825` | `1.048` | `4/5` | **MISS** | `4/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `CPL` | `wa` | `0.000000` | `-0.161075` | `-0.161075` | `0.203667` | `0.791` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `T2A_CPL` | `Omega_bc` | `0.313772` | `0.312573` | `-0.001199` | `0.005756` | `0.208` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `T2A_CPL` | `h` | `0.673600` | `0.670489` | `-0.003111` | `0.005288` | `0.588` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `T2A_CPL` | `100_omega_b` | `2.237000` | `2.280464` | `+0.043464` | `0.033381` | `1.302` | `4/5` | **MISS** | `4/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `T2A_CPL` | `w0` | `-1.000000` | `-0.964729` | `+0.035271` | `0.052126` | `0.677` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `T2A_CPL` | `wa` | `0.000000` | `-0.017014` | `-0.017014` | `0.237095` | `0.072` | `4/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `LCDM` | `Omega_bc` | `0.313772` | `0.310808` | `-0.002964` | `0.003835` | `0.773` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `LCDM` | `h` | `0.673600` | `0.673761` | `+0.000161` | `0.002883` | `0.056` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `LCDM` | `100_omega_b` | `2.237000` | `2.249519` | `+0.012519` | `0.012418` | `1.008` | `4/5` | **MISS** | `4/5` | **MISS** | **MISS** |
| **Reading A** | **Pantheon+** | `Law1` | `Omega_bc` | `0.313772` | `0.316984` | `+0.003212` | `0.004684` | `0.686` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `Law1` | `h` | `0.673600` | `0.669395` | `-0.004205` | `0.004474` | `0.940` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `Law1` | `100_omega_b` | `2.237000` | `2.251500` | `+0.014500` | `0.012595` | `1.151` | `4/5` | **MISS** | `4/5` | **MISS** | **MISS** |
| **Reading A** | **Pantheon+** | `Law1` | `gamma_u` | `0.000000` | `0.030187` | `+0.030187` | `0.020776` | `1.453` | `0/5` | **MISS** | `5/5` | **MISS** | **MISS** |
| **Reading A** | **Pantheon+** | `CPL` | `Omega_bc` | `0.313772` | `0.315916` | `+0.002143` | `0.005801` | `0.369` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `CPL` | `h` | `0.673600` | `0.672583` | `-0.001017` | `0.005936` | `0.171` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `CPL` | `100_omega_b` | `2.237000` | `2.244890` | `+0.007890` | `0.013878` | `0.569` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `CPL` | `w0` | `-1.000000` | `-0.955794` | `+0.044206` | `0.053559` | `0.825` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `CPL` | `wa` | `0.000000` | `-0.168386` | `-0.168386` | `0.200731` | `0.839` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `T2A_CPL` | `Omega_bc` | `0.313772` | `0.313564` | `-0.000208` | `0.006307` | `0.033` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `T2A_CPL` | `h` | `0.673600` | `0.673282` | `-0.000318` | `0.005975` | `0.053` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `T2A_CPL` | `100_omega_b` | `2.237000` | `2.267332` | `+0.030332` | `0.033163` | `0.915` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `T2A_CPL` | `w0` | `-1.000000` | `-0.971019` | `+0.028981` | `0.055069` | `0.526` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `T2A_CPL` | `wa` | `0.000000` | `-0.053751` | `-0.053751` | `0.234791` | `0.229` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `LCDM` | `Omega_bc` | `0.313772` | `0.312798` | `-0.000975` | `0.003835` | `0.254` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `LCDM` | `h` | `0.673600` | `0.674657` | `+0.001057` | `0.002883` | `0.367` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `LCDM` | `100_omega_b` | `2.237000` | `2.248036` | `+0.011036` | `0.012465` | `0.885` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `Law1` | `Omega_bc` | `0.313772` | `0.317208` | `+0.003435` | `0.004569` | `0.752` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `Law1` | `h` | `0.673600` | `0.669271` | `-0.004329` | `0.004198` | `1.031` | `4/5` | **MISS** | `4/5` | **MISS** | **MISS** |
| **Reading A** | **DES-Dovekie** | `Law1` | `100_omega_b` | `2.237000` | `2.251487` | `+0.014487` | `0.012649` | `1.145` | `4/5` | **MISS** | `4/5` | **MISS** | **MISS** |
| **Reading A** | **DES-Dovekie** | `Law1` | `gamma_u` | `0.000000` | `0.030977` | `+0.030977` | `0.019991` | `1.550` | `0/5` | **MISS** | `5/5` | **MISS** | **MISS** |
| **Reading A** | **DES-Dovekie** | `CPL` | `Omega_bc` | `0.313772` | `0.316913` | `+0.003141` | `0.005315` | `0.591` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `CPL` | `h` | `0.673600` | `0.671300` | `-0.002300` | `0.005264` | `0.437` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `CPL` | `100_omega_b` | `2.237000` | `2.245843` | `+0.008843` | `0.013831` | `0.639` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `CPL` | `w0` | `-1.000000` | `-0.950351` | `+0.049649` | `0.050893` | `0.976` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `CPL` | `wa` | `0.000000` | `-0.148935` | `-0.148935` | `0.203667` | `0.731` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `T2A_CPL` | `Omega_bc` | `0.313772` | `0.314541` | `+0.000769` | `0.005764` | `0.133` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `T2A_CPL` | `h` | `0.673600` | `0.671993` | `-0.001607` | `0.005295` | `0.303` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `T2A_CPL` | `100_omega_b` | `2.237000` | `2.269669` | `+0.032669` | `0.033560` | `0.973` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `T2A_CPL` | `w0` | `-1.000000` | `-0.966611` | `+0.033389` | `0.052266` | `0.639` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `T2A_CPL` | `wa` | `0.000000` | `-0.025795` | `-0.025795` | `0.237432` | `0.109` | `4/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `LCDM` | `Omega_bc` | `0.313772` | `0.312214` | `-0.001558` | `0.003835` | `0.406` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `LCDM` | `h` | `0.673600` | `0.675083` | `+0.001483` | `0.002883` | `0.515` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `LCDM` | `100_omega_b` | `2.237000` | `2.247435` | `+0.010435` | `0.012474` | `0.837` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |

---

#### 2.2.2 COSMO Family — Truth `C2` (`MODEL-TRUE Law 1`: $\Omega_{bc}=6/19\approx 0.315789, h=0.66, 100\omega_b=2.292632, \gamma_u=0.10, w_{0,\text{fit}}=-0.90, w_{a,\text{tan}}=-0.057831$)

Universes (Rounds 1–5): `U-YNED`, `U-LMB5`, `U-KPN8`, `U-BKI0`, `U-J91F`.

| Reading | SN Dataset | Fit Model | Parameter | True Value | Mean Recovered | Mean Signed Bias ($b$) | Mean Posterior $\sigma$ | $|b|/\sigma$ | In `ci95` `[p2.5, p97.5]` | Primary Verdict (`ci95` & `mean/std`) | In Gaussian `mean±1.96σ` | Gaussian Verdict | `median` / `σ68` Verdict |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Reading B** | **Pantheon+** | `Law1` | `Omega_bc` | `0.315789` | `0.313712` | `-0.002078` | `0.004422` | `0.470` | `3/5` | **MISS** *(CI 3/5)* | `3/5` | **MISS** | **MISS** |
| **Reading B** | **Pantheon+** | `Law1` | `h` | `0.660000` | `0.659472` | `-0.000528` | `0.004781` | `0.111` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `Law1` | `100_omega_b` | `2.292632` | `2.298182` | `+0.005550` | `0.012731` | `0.436` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `Law1` | `gamma_u` | `0.100000` | `0.088296` | `-0.011704` | `0.031523` | `0.371` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `CPL` | `Omega_bc` | `0.315789` | `0.313097` | `-0.002692` | `0.005689` | `0.473` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `CPL` | `h` | `0.660000` | `0.661270` | `+0.001270` | `0.005749` | `0.221` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `CPL` | `100_omega_b` | `2.292632` | `2.294312` | `+0.001681` | `0.013895` | `0.121` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `CPL` | `w0` | `-0.900000` | `-0.875942` | `+0.024058` | `0.056603` | `0.425` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `CPL` | `wa` | `-0.057831` | `-0.168259` | `-0.110428` | `0.220265` | `0.501` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `T2A_CPL` | `Omega_bc` | `0.315789` | `0.314380` | `-0.001409` | `0.006172` | `0.228` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `T2A_CPL` | `h` | `0.660000` | `0.660949` | `+0.000949` | `0.005756` | `0.165` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `T2A_CPL` | `100_omega_b` | `2.292632` | `2.279156` | `-0.013476` | `0.032998` | `0.408` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `T2A_CPL` | `w0` | `-0.900000` | `-0.867527` | `+0.032473` | `0.058139` | `0.559` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `T2A_CPL` | `wa` | `-0.057831` | `-0.236264` | `-0.178433` | `0.256411` | `0.696` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `LCDM` *(wrong)* | `Omega_bc` | `0.315789` | `0.301641` | `-0.014149` | `0.003686` | `3.838` | `2/5` | **MISS** | `2/5` | **MISS** | **MISS** |
| **Reading B** | **Pantheon+** | `LCDM` *(wrong)* | `h` | `0.660000` | `0.673110` | `+0.013110` | `0.002859` | `4.585` | `0/5` | **MISS** | `0/5` | **MISS** | **MISS** |
| **Reading B** | **Pantheon+** | `LCDM` *(wrong)* | `100_omega_b` | `2.292632` | `2.307506` | `+0.014875` | `0.012648` | `1.176` | `4/5` | **MISS** | `4/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `Law1` | `Omega_bc` | `0.315789` | `0.312061` | `-0.003728` | `0.004362` | `0.855` | `3/5` | **MISS** *(CI 3/5)* | `3/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `Law1` | `h` | `0.660000` | `0.662135` | `+0.002135` | `0.004503` | `0.474` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `Law1` | `100_omega_b` | `2.292632` | `2.296686` | `+0.004055` | `0.012722` | `0.319` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `Law1` | `gamma_u` | `0.100000` | `0.081900` | `-0.018100` | `0.029855` | `0.606` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `CPL` | `Omega_bc` | `0.315789` | `0.313712` | `-0.002077` | `0.005279` | `0.393` | `3/5` | **MISS** *(CI 3/5)* | `3/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `CPL` | `h` | `0.660000` | `0.660662` | `+0.000662` | `0.005161` | `0.128` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `CPL` | `100_omega_b` | `2.292632` | `2.297434` | `+0.004803` | `0.013895` | `0.346` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `CPL` | `w0` | `-0.900000` | `-0.904664` | `-0.004664` | `0.053724` | `0.087` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `CPL` | `wa` | `-0.057831` | `-0.018636` | `+0.039195` | `0.219428` | `0.179` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `T2A_CPL` | `Omega_bc` | `0.315789` | `0.314726` | `-0.001064` | `0.005725` | `0.186` | `3/5` | **MISS** *(CI 3/5)* | `3/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `T2A_CPL` | `h` | `0.660000` | `0.660417` | `+0.000417` | `0.005169` | `0.081` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `T2A_CPL` | `100_omega_b` | `2.292632` | `2.285305` | `-0.007326` | `0.033290` | `0.220` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `T2A_CPL` | `w0` | `-0.900000` | `-0.897797` | `+0.002203` | `0.055066` | `0.040` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `T2A_CPL` | `wa` | `-0.057831` | `-0.072819` | `-0.014989` | `0.254443` | `0.059` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `LCDM` *(wrong)* | `Omega_bc` | `0.315789` | `0.301407` | `-0.014382` | `0.003685` | `3.903` | `1/5` | **MISS** | `1/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `LCDM` *(wrong)* | `h` | `0.660000` | `0.675469` | `+0.015469` | `0.002875` | `5.381` | `0/5` | **MISS** | `0/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `LCDM` *(wrong)* | `100_omega_b` | `2.292632` | `2.307978` | `+0.015346` | `0.012627` | `1.215` | `5/5` | **MISS** | `5/5` | **MISS** | **MISS** |
| **Reading A** | **Pantheon+** | `Law1` | `Omega_bc` | `0.315789` | `0.315693` | `-0.000097` | `0.004407` | `0.022` | `3/5` | **MISS** *(CI 3/5)* | `3/5` | **MISS** | **MISS** |
| **Reading A** | **Pantheon+** | `Law1` | `h` | `0.660000` | `0.660390` | `+0.000390` | `0.004789` | `0.081` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `Law1` | `100_omega_b` | `2.292632` | `2.296228` | `+0.003596` | `0.012699` | `0.283` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `Law1` | `gamma_u` | `0.100000` | `0.092788` | `-0.007212` | `0.031591` | `0.228` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `CPL` | `Omega_bc` | `0.315789` | `0.314672` | `-0.001118` | `0.005689` | `0.196` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `CPL` | `h` | `0.660000` | `0.662709` | `+0.002709` | `0.005753` | `0.471` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `CPL` | `100_omega_b` | `2.292632` | `2.291663` | `-0.000969` | `0.013866` | `0.070` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `CPL` | `w0` | `-0.900000` | `-0.878093` | `+0.021907` | `0.056603` | `0.387` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `CPL` | `wa` | `-0.057831` | `-0.161533` | `-0.103702` | `0.219822` | `0.472` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `T2A_CPL` | `Omega_bc` | `0.315789` | `0.316370` | `+0.000580` | `0.006171` | `0.094` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `T2A_CPL` | `h` | `0.660000` | `0.662387` | `+0.002387` | `0.005779` | `0.413` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `T2A_CPL` | `100_omega_b` | `2.292632` | `2.268393` | `-0.024239` | `0.032998` | `0.735` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `T2A_CPL` | `w0` | `-0.900000` | `-0.867419` | `+0.032581` | `0.058139` | `0.560` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `T2A_CPL` | `wa` | `-0.057831` | `-0.256411` | `-0.198580` | `0.256411` | `0.774` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `LCDM` *(wrong)* | `Omega_bc` | `0.315789` | `0.303018` | `-0.012771` | `0.003686` | `3.465` | `2/5` | **MISS** | `2/5` | **MISS** | **MISS** |
| **Reading A** | **Pantheon+** | `LCDM` *(wrong)* | `h` | `0.660000` | `0.674425` | `+0.014425` | `0.002859` | `5.045` | `0/5` | **MISS** | `0/5` | **MISS** | **MISS** |
| **Reading A** | **Pantheon+** | `LCDM` *(wrong)* | `100_omega_b` | `2.292632` | `2.305490` | `+0.012858` | `0.012648` | `1.017` | `5/5` | **MISS** | `5/5` | **MISS** | **MISS** |
| **Reading A** | **DES-Dovekie** | `Law1` | `Omega_bc` | `0.315789` | `0.313939` | `-0.001850` | `0.004362` | `0.424` | `3/5` | **MISS** *(CI 3/5)* | `3/5` | **MISS** | **MISS** |
| **Reading A** | **DES-Dovekie** | `Law1` | `h` | `0.660000` | `0.662697` | `+0.002697` | `0.004503` | `0.599` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `Law1` | `100_omega_b` | `2.292632` | `2.294635` | `+0.002003` | `0.012722` | `0.157` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `Law1` | `gamma_u` | `0.100000` | `0.088269` | `-0.011731` | `0.029855` | `0.393` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `CPL` | `Omega_bc` | `0.315789` | `0.315326` | `-0.000463` | `0.005279` | `0.088` | `3/5` | **MISS** *(CI 3/5)* | `3/5` | **MISS** | **MISS** |
| **Reading A** | **DES-Dovekie** | `CPL` | `h` | `0.660000` | `0.662078` | `+0.002078` | `0.005161` | `0.403` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `CPL` | `100_omega_b` | `2.292632` | `2.294827` | `+0.002195` | `0.013895` | `0.158` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `CPL` | `w0` | `-0.900000` | `-0.907323` | `-0.007323` | `0.053724` | `0.136` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `CPL` | `wa` | `-0.057831` | `-0.010200` | `+0.047631` | `0.219428` | `0.217` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `T2A_CPL` | `Omega_bc` | `0.315789` | `0.316670` | `+0.000881` | `0.005725` | `0.154` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `T2A_CPL` | `h` | `0.660000` | `0.661874` | `+0.001874` | `0.005169` | `0.363` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `T2A_CPL` | `100_omega_b` | `2.292632` | `2.274627` | `-0.018005` | `0.033290` | `0.541` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `T2A_CPL` | `w0` | `-0.900000` | `-0.898947` | `+0.001053` | `0.055066` | `0.019` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `T2A_CPL` | `wa` | `-0.057831` | `-0.086475` | `-0.028644` | `0.254443` | `0.113` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `LCDM` *(wrong)* | `Omega_bc` | `0.315789` | `0.302759` | `-0.013030` | `0.003685` | `3.536` | `2/5` | **MISS** | `2/5` | **MISS** | **MISS** |
| **Reading A** | **DES-Dovekie** | `LCDM` *(wrong)* | `h` | `0.660000` | `0.676818` | `+0.016818` | `0.002875` | `5.850` | `0/5` | **MISS** | `0/5` | **MISS** | **MISS** |
| **Reading A** | **DES-Dovekie** | `LCDM` *(wrong)* | `100_omega_b` | `2.292632` | `2.305936` | `+0.013304` | `0.012627` | `1.054` | `5/5` | **MISS** | `5/5` | **MISS** | **MISS** |

---

#### 2.2.3 COSMO Family — Truth `C3` (`OFF-CURVE CPL`: $\Omega_{bc}=0.313772, h=0.6736, 100\omega_b=2.237, w_0=-0.75, w_a=-1.0$)

Universes (Rounds 1–5): `U-CUIZ`, `U-44A3`, `U-SU9K`, `U-GL5Z`, `U-8Z6F`.

| Reading | SN Dataset | Fit Model | Parameter | True Value | Mean Recovered | Mean Signed Bias ($b$) | Mean Posterior $\sigma$ | $|b|/\sigma$ | In `ci95` `[p2.5, p97.5]` | Primary Verdict (`ci95` & `mean/std`) | In Gaussian `mean±1.96σ` | Gaussian Verdict | `median` / `σ68` Verdict |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Reading B** | **Pantheon+** | `CPL` | `Omega_bc` | `0.313772` | `0.310688` | `-0.003084` | `0.005689` | `0.542` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `CPL` | `h` | `0.673600` | `0.675498` | `+0.001898` | `0.005952` | `0.319` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `CPL` | `100_omega_b` | `2.237000` | `2.248857` | `+0.011857` | `0.013905` | `0.853` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `CPL` | `w0` | `-0.750000` | `-0.742992` | `+0.007008` | `0.062857` | `0.111` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `CPL` | `wa` | `-1.000000` | `-1.069447` | `-0.069447` | `0.254443` | `0.273` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `T2A_CPL` | `Omega_bc` | `0.313772` | `0.307043` | `-0.006729` | `0.006171` | `1.091` | `4/5` | **MISS** | `4/5` | **MISS** | **MISS** |
| **Reading B** | **Pantheon+** | `T2A_CPL` | `h` | `0.673600` | `0.677255` | `+0.003655` | `0.005975` | `0.612` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `T2A_CPL` | `100_omega_b` | `2.237000` | `2.272579` | `+0.035579` | `0.032998` | `1.078` | `4/5` | **MISS** | `4/5` | **MISS** | **MISS** |
| **Reading B** | **Pantheon+** | `T2A_CPL` | `w0` | `-0.750000` | `-0.766702` | `-0.016702` | `0.064549` | `0.259` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `T2A_CPL` | `wa` | `-1.000000` | `-0.892011` | `+0.107989` | `0.296648` | `0.364` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `Law1` *(wrong)* | `Omega_bc` | `0.313772` | `0.300592` | `-0.013180` | `0.004422` | `2.981` | `1/5` | **MISS** | `1/5` | **MISS** | **MISS** |
| **Reading B** | **Pantheon+** | `Law1` *(wrong)* | `h` | `0.673600` | `0.673698` | `+0.000098` | `0.004781` | `0.020` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading B** | **Pantheon+** | `Law1` *(wrong)* | `100_omega_b` | `2.237000` | `2.266257` | `+0.029257` | `0.012731` | `2.298` | `1/5` | **MISS** | `1/5` | **MISS** | **MISS** |
| **Reading B** | **Pantheon+** | `LCDM` *(wrong)* | `Omega_bc` | `0.313772` | `0.297719` | `-0.016053` | `0.003686` | `4.355` | `0/5` | **MISS** | `0/5` | **MISS** | **MISS** |
| **Reading B** | **Pantheon+** | `LCDM` *(wrong)* | `h` | `0.673600` | `0.684426` | `+0.010826` | `0.002859` | `3.786` | `0/5` | **MISS** | `0/5` | **MISS** | **MISS** |
| **Reading B** | **Pantheon+** | `LCDM` *(wrong)* | `100_omega_b` | `2.237000` | `2.273611` | `+0.036611` | `0.012648` | `2.895` | `1/5` | **MISS** | `1/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `CPL` | `Omega_bc` | `0.313772` | `0.312573` | `-0.001199` | `0.005279` | `0.227` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `CPL` | `h` | `0.673600` | `0.673432` | `-0.000168` | `0.005161` | `0.033` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `CPL` | `100_omega_b` | `2.237000` | `2.248447` | `+0.011447` | `0.013895` | `0.824` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `CPL` | `w0` | `-0.750000` | `-0.742992` | `+0.007008` | `0.059666` | `0.117` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `CPL` | `wa` | `-1.000000` | `-1.018636` | `-0.018636` | `0.254443` | `0.073` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `T2A_CPL` | `Omega_bc` | `0.313772` | `0.309026` | `-0.004746` | `0.005725` | `0.829` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `T2A_CPL` | `h` | `0.673600` | `0.674989` | `+0.001389` | `0.005169` | `0.269` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `T2A_CPL` | `100_omega_b` | `2.237000` | `2.274957` | `+0.037957` | `0.033290` | `1.140` | `4/5` | **MISS** | `4/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `T2A_CPL` | `w0` | `-0.750000` | `-0.766702` | `-0.016702` | `0.061237` | `0.273` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `T2A_CPL` | `wa` | `-1.000000` | `-0.836475` | `+0.163525` | `0.296648` | `0.551` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `Law1` *(wrong)* | `Omega_bc` | `0.313772` | `0.300592` | `-0.013180` | `0.004362` | `3.022` | `1/5` | **MISS** | `1/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `Law1` *(wrong)* | `h` | `0.673600` | `0.675498` | `+0.001898` | `0.004503` | `0.421` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading B** | **DES-Dovekie** | `Law1` *(wrong)* | `100_omega_b` | `2.237000` | `2.266257` | `+0.029257` | `0.012722` | `2.300` | `2/5` | **MISS** | `2/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `LCDM` *(wrong)* | `Omega_bc` | `0.313772` | `0.296808` | `-0.016964` | `0.003685` | `4.604` | `0/5` | **MISS** | `0/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `LCDM` *(wrong)* | `h` | `0.673600` | `0.685469` | `+0.011869` | `0.002875` | `4.128` | `0/5` | **MISS** | `0/5` | **MISS** | **MISS** |
| **Reading B** | **DES-Dovekie** | `LCDM` *(wrong)* | `100_omega_b` | `2.237000` | `2.274957` | `+0.037957` | `0.012627` | `3.006` | `1/5` | **MISS** | `1/5` | **MISS** | **MISS** |
| **Reading A** | **Pantheon+** | `CPL` | `Omega_bc` | `0.313772` | `0.312262` | `-0.001510` | `0.005689` | `0.265` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `CPL` | `h` | `0.673600` | `0.676984` | `+0.003384` | `0.005952` | `0.569` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `CPL` | `100_omega_b` | `2.237000` | `2.246257` | `+0.009257` | `0.013905` | `0.666` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `CPL` | `w0` | `-0.750000` | `-0.745351` | `+0.004649` | `0.062857` | `0.074` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `CPL` | `wa` | `-1.000000` | `-1.061075` | `-0.061075` | `0.254443` | `0.240` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `T2A_CPL` | `Omega_bc` | `0.313772` | `0.309026` | `-0.004746` | `0.006171` | `0.769` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `T2A_CPL` | `h` | `0.673600` | `0.678761` | `+0.005161` | `0.005975` | `0.864` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `T2A_CPL` | `100_omega_b` | `2.237000` | `2.261874` | `+0.024874` | `0.032998` | `0.754` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `T2A_CPL` | `w0` | `-0.750000` | `-0.766702` | `-0.016702` | `0.064549` | `0.259` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `T2A_CPL` | `wa` | `-1.000000` | `-0.910200` | `+0.089800` | `0.296648` | `0.303` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `Law1` *(wrong)* | `Omega_bc` | `0.313772` | `0.302573` | `-0.011199` | `0.004422` | `2.533` | `2/5` | **MISS** | `2/5` | **MISS** | **MISS** |
| **Reading A** | **Pantheon+** | `Law1` *(wrong)* | `h` | `0.673600` | `0.674657` | `+0.001057` | `0.004781` | `0.221` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **Pantheon+** | `Law1` *(wrong)* | `100_omega_b` | `2.237000` | `2.264257` | `+0.027257` | `0.012731` | `2.141` | `2/5` | **MISS** | `2/5` | **MISS** | **MISS** |
| **Reading A** | **Pantheon+** | `LCDM` *(wrong)* | `Omega_bc` | `0.313772` | `0.299026` | `-0.014746` | `0.003686` | `4.000` | `0/5` | **MISS** | `0/5` | **MISS** | **MISS** |
| **Reading A** | **Pantheon+** | `LCDM` *(wrong)* | `h` | `0.673600` | `0.685761` | `+0.012161` | `0.002859` | `4.254` | `0/5` | **MISS** | `0/5` | **MISS** | **MISS** |
| **Reading A** | **Pantheon+** | `LCDM` *(wrong)* | `100_omega_b` | `2.237000` | `2.271579` | `+0.034579` | `0.012648` | `2.734` | `2/5` | **MISS** | `2/5` | **MISS** | **MISS** |
| **Reading A** | **DES-Dovekie** | `CPL` | `Omega_bc` | `0.313772` | `0.314188` | `+0.000416` | `0.005279` | `0.079` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `CPL` | `h` | `0.673600` | `0.674989` | `+0.001389` | `0.005161` | `0.269` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `CPL` | `100_omega_b` | `2.237000` | `2.245843` | `+0.008843` | `0.013895` | `0.636` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `CPL` | `w0` | `-0.750000` | `-0.745351` | `+0.004649` | `0.059666` | `0.078` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `CPL` | `wa` | `-1.000000` | `-1.010200` | `-0.010200` | `0.254443` | `0.040` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `T2A_CPL` | `Omega_bc` | `0.313772` | `0.310984` | `-0.002788` | `0.005725` | `0.487` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `T2A_CPL` | `h` | `0.673600` | `0.676489` | `+0.002889` | `0.005169` | `0.559` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `T2A_CPL` | `100_omega_b` | `2.237000` | `2.264257` | `+0.027257` | `0.033290` | `0.819` | `4/5` | **PASS** | `4/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `T2A_CPL` | `w0` | `-0.750000` | `-0.766702` | `-0.016702` | `0.061237` | `0.273` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `T2A_CPL` | `wa` | `-1.000000` | `-0.853751` | `+0.146249` | `0.296648` | `0.493` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `Law1` *(wrong)* | `Omega_bc` | `0.313772` | `0.302573` | `-0.011199` | `0.004362` | `2.567` | `2/5` | **MISS** | `2/5` | **MISS** | **MISS** |
| **Reading A** | **DES-Dovekie** | `Law1` *(wrong)* | `h` | `0.673600` | `0.676489` | `+0.002889` | `0.004503` | `0.642` | `5/5` | **PASS** | `5/5` | **PASS** | **PASS** |
| **Reading A** | **DES-Dovekie** | `Law1` *(wrong)* | `100_omega_b` | `2.237000` | `2.264257` | `+0.027257` | `0.012722` | `2.143` | `2/5` | **MISS** | `2/5` | **MISS** | **MISS** |
| **Reading A** | **DES-Dovekie** | `LCDM` *(wrong)* | `Omega_bc` | `0.313772` | `0.298188` | `-0.015584` | `0.003685` | `4.229` | `0/5` | **MISS** | `0/5` | **MISS** | **MISS** |
| **Reading A** | **DES-Dovekie** | `LCDM` *(wrong)* | `h` | `0.673600` | `0.686818` | `+0.013218` | `0.002875` | `4.598` | `0/5` | **MISS** | `0/5` | **MISS** | **MISS** |
| **Reading A** | **DES-Dovekie** | `LCDM` *(wrong)* | `100_omega_b` | `2.237000` | `2.272579` | `+0.035579` | `0.012627` | `2.818` | `2/5` | **MISS** | `2/5` | **MISS** | **MISS** |

---

#### 2.2.4 GALAXY Family — Truths `G1` ($\sigma_{\rm ref}=9.0\text{ kpc}$) & `G2` ($\sigma_{\rm ref}=3.0\text{ kpc}$)

- `G1` Universes (Rounds 1–5): `U-UD33`, `U-TLZU`, `U-63X5`, `U-P0XK`, `U-KQF9` (Point estimates `fitted_sigma_ref_kpc`: `9.0204, 8.9994, 8.9937, 8.9970, 9.0357 kpc`; empirical SD = `0.0174 kpc`).
- `G2` Universes (Rounds 1–5): `U-I9FZ`, `U-8S92`, `U-07FN`, `U-YTKL`, `U-NPID` (Point estimates `fitted_sigma_ref_kpc`: `3.0056, 3.0033, 3.0005, 3.0018, 2.9922 kpc`; empirical SD = `0.0051 kpc`).
- Note: Truth `G3` (`RAR-TRUE`, $g_\dagger = 1.2 \times 10^{-10}\text{ m/s}^2$) is a non-model physical truth with no true $\sigma_{\rm ref}$; its recovery is scored under S2 (`T5-A FAIL` and median $\chi^2_{\rm red}$).

| Truth | Uncertainty Method (`sigma_ref_uncertainty`) | Role | True $\sigma_{\rm ref}$ (kpc) | Mean of Method `mean` (kpc) | Mean of Grid Point Est. (kpc) | Signed Bias (Method `mean`) | Signed Bias (Grid Point Est.) | Mean Posterior $\sigma$ (kpc) | $|b_{\rm mean}|/\sigma$ | $|b_{\rm pt}|/\sigma$ | In `ci95` `[p2.5, p97.5]` | In Gaussian `mean±1.96σ` | S1 Verdict (All Readings) |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`G1`** | `bootstrap_train_galaxies` | **Primary** | `9.0000` | `9.0070` | `9.0092` | `+0.0070` | `+0.0092` | `0.0141` | `0.493` | `0.654` | `5/5` | `5/5` | **PASS** |
| **`G1`** | `posterior_sum_chi2_red` | Secondary | `9.0000` | `9.0079` | `9.0092` | `+0.0079` | `+0.0092` | `0.0522` | `0.151` | `0.177` | `5/5` | `5/5` | **PASS** |
| **`G1`** | `posterior_total_chi2` | Secondary | `9.0000` | `9.0005` | `9.0092` | `+0.0005` | `+0.0092` | `0.0102` | `0.053` | `0.903` | `5/5` | `5/5` | **PASS** |
| **`G2`** | `bootstrap_train_galaxies` | **Primary** | `3.0000` | `3.0002` | `3.0007` | `+0.0002` | `+0.0007` | `0.0054` | `0.036` | `0.129` | `5/5` | `5/5` | **PASS** |
| **`G2`** | `posterior_sum_chi2_red` | Secondary | `3.0000` | `3.0007` | `3.0007` | `+0.0007` | `+0.0007` | `0.0246` | `0.029` | `0.028` | `5/5` | `5/5` | **PASS** |
| **`G2`** | `posterior_total_chi2` | Secondary | `3.0000` | `2.9999` | `3.0007` | `-0.0001` | `+0.0007` | `0.0039` | `0.030` | `0.181` | `4/5` | `4/5` | **PASS** |

---

#### 2.2.5 REGIONAL Family — Truths `H1` (`NULL`, $73.0$), `H2` (`SMALL VARIATION`, $\pm 2$), & `H3` (`LARGE VARIATION`, $\pm 5$)

- `H1` Universes (Rounds 1–5): `U-J8TH`, `U-EATJ`, `U-4JZF`, `U-B485`, `U-ZY0Y`.
- `H2` Universes (Rounds 1–5): `U-LYTB`, `U-PAKD`, `U-6VMC`, `U-51CN`, `U-KCY8`.
- `H3` Universes (Rounds 1–5): `U-IBCC`, `U-JNXP`, `U-ZJBO`, `U-LH19`, `U-NBRH`.
- Active HEALPix Regions ($N_{\rm pix} = 9$): `{0, 1, 2, 3, 5, 6, 8, 9, 10}`.

##### Table 2.2.5A — Regional S1 Summary Across All 5 Error-Bar / Reference Readings & Multi-Region Aggregations

| Truth | Reading / Uncertainty Mode | Role | Regions Passing S1 (`≥4/5` & `|b|<σ`) | Pooled 95% Coverage (`N/45`) | Per-Universe Regions in 95% CI (`R1..R5` of `9`) | Universes w/ `≥8/9` (`≥7/9`) in CI | Grand Mean Bias (km/s/Mpc) | Mean Regional `|Bias|` (km/s/Mpc) | Grand Mean $\sigma$ (km/s/Mpc) | `|Grand b|/σ` (`Mean |b_r|/σ`) | Per-Region Verdict (`All 9`) | Pooled / Universe Verdict |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`H1`** | `abs_total` (`sigma_H0_total_incl_cal`) | **Primary** | **`9/9`** | `40/45` (`88.9%`) | `[9, 9, 8, 5, 9]` | `4/5` (`4/5`) | `-0.046` | `0.351` | `1.267` | `0.036` (`0.277`) | **PASS** | **PASS** |
| **`H1`** | `abs_hf` (`sigma_H0_hf_only`, uncal.) | Secondary | `3/9` | `30/45` (`66.7%`) | `[9, 6, 6, 1, 8]` | `2/5` (`2/5`) | `-0.046` | `0.351` | `0.739` | `0.062` (`0.475`) | **MISS** | **MISS** |
| **`H1`** | `cal_corr_hf` (calibrator-removed, `hf_only`) | Secondary | `8/9` | `44/45` (`97.8%`) | `[9, 8, 9, 9, 9]` | `5/5` (`5/5`) | `-0.353` | `0.412` | `0.739` | `0.477` (`0.557`) | **PARTIAL (`8/9`)** | **PASS** |
| **`H1`** | `rel_count_wt_hf` ($\hat{H}_{0,i}-\bar{H}_{0,\text{cnt}}$, `hf_only`) | Secondary | **`9/9`** | `43/45` (`95.6%`) | `[9, 7, 9, 9, 9]` | `4/5` (`5/5`) | `-0.129` | `0.360` | `0.739` | `0.175` (`0.487`) | **PASS** | **PASS** |
| **`H1`** | `rel_gls_bar_hf` ($\hat{H}_{0,i}-\bar{H}_{0,\text{GLS}}$, `hf_only`) | Secondary | **`9/9`** | `43/45` (`95.6%`) | `[9, 7, 9, 9, 9]` | `4/5` (`5/5`) | `-0.135` | `0.361` | `0.739` | `0.182` (`0.488`) | **PASS** | **PASS** |
| **`H2`** | `abs_total` (`sigma_H0_total_incl_cal`) | **Primary** | **`9/9`** | `41/45` (`91.1%`) | `[9, 9, 5, 9, 9]` | `4/5` (`4/5`) | `+0.900` | `0.900` | `1.285` | `0.700` (`0.700`) | **PASS** | **PASS** |
| **`H2`** | `abs_hf` (`sigma_H0_hf_only`, uncal.) | Secondary | `1/9` | `26/45` (`57.8%`) | `[7, 6, 0, 5, 8]` | `1/5` (`2/5`) | `+0.900` | `0.900` | `0.750` | `1.199` (`1.199`) | **MISS** | **MISS** |
| **`H2`** | `cal_corr_hf` (calibrator-removed, `hf_only`) | Secondary | **`9/9`** | `43/45` (`95.6%`) | `[7, 9, 9, 9, 9]` | `4/5` (`5/5`) | `+0.068` | `0.219` | `0.750` | `0.091` (`0.292`) | **PASS** | **PASS** |
| **`H2`** | `rel_count_wt_hf` ($\hat{H}_{0,i}-\bar{H}_{0,\text{cnt}}$, `hf_only`) | Secondary | **`9/9`** | `44/45` (`97.8%`) | `[9, 9, 9, 9, 8]` | `5/5` (`5/5`) | `+0.035` | `0.223` | `0.750` | `0.047` (`0.297`) | **PASS** | **PASS** |
| **`H2`** | `rel_gls_bar_hf` ($\hat{H}_{0,i}-\bar{H}_{0,\text{GLS}}$, `hf_only`) | Secondary | **`9/9`** | `43/45` (`95.6%`) | `[9, 9, 9, 8, 8]` | `5/5` (`5/5`) | `+0.285` | `0.293` | `0.750` | `0.380` (`0.391`) | **PASS** | **PASS** |
| **`H3`** | `abs_total` (`sigma_H0_total_incl_cal`) | **Primary** | **`8/9`** *(R0: `3/5`)* | `43/45` (`95.6%`) | `[8, 9, 9, 9, 8]` | `5/5` (`5/5`) | `+0.644` | `0.655` | `1.279` | `0.504` (`0.512`) | **PARTIAL (`8/9`)** | **PASS** |
| **`H3`** | `abs_hf` (`sigma_H0_hf_only`, uncal.) | Secondary | `2/9` | `24/45` (`53.3%`) | `[3, 7, 2, 9, 3]` | `1/5` (`2/5`) | `+0.644` | `0.655` | `0.747` | `0.862` (`0.876`) | **MISS** | **MISS** |
| **`H3`** | `cal_corr_hf` (calibrator-removed, `hf_only`) | Secondary | **`9/9`** | `44/45` (`97.8%`) | `[9, 9, 9, 9, 8]` | `5/5` (`5/5`) | `+0.104` | `0.326` | `0.747` | `0.139` (`0.436`) | **PASS** | **PASS** |
| **`H3`** | `rel_count_wt_hf` ($\hat{H}_{0,i}-\bar{H}_{0,\text{cnt}}$, `hf_only`) | Secondary | **`9/9`** | `45/45` (`100.0%`) | `[9, 9, 9, 9, 9]` | `5/5` (`5/5`) | `-0.036` | `0.294` | `0.747` | `0.049` (`0.394`) | **PASS** | **PASS** |
| **`H3`** | `rel_gls_bar_hf` ($\hat{H}_{0,i}-\bar{H}_{0,\text{GLS}}$, `hf_only`) | Secondary | `4/9` | `37/45` (`82.2%`) | `[8, 9, 5, 9, 6]` | `3/5` (`3/5`) | `+0.667` | `0.672` | `0.747` | `0.892` (`0.900`) | **MISS (`4/9`)** | **PASS** |

##### Table 2.2.5B — All-Sky $\bar{H}_0$ Recovery Against True `H0_base = 73.0 km/s/Mpc`

| Truth | Uncertainty Column | In 95% Interval (`N/5`) | Mean Recovered $\bar{H}_0$ (km/s/Mpc) | Mean Signed Bias (km/s/Mpc) | Mean Posterior $\sigma$ (km/s/Mpc) | $|b|/\sigma$ | S1 Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`H1`** | `sigma_H0_bar_total` (**Primary**) | `4/5` | `73.0890` | `+0.0890` | `1.0574` | `0.084` | **PASS** |
| **`H1`** | `sigma_H0_bar_hf_only` (Secondary) | `2/5` | `73.0890` | `+0.0890` | `0.2143` | `0.415` | **MISS** |
| **`H2`** | `sigma_H0_bar_total` (**Primary**) | `5/5` | `73.6143` | `+0.6143` | `1.0660` | `0.576` | **PASS** |
| **`H2`** | `sigma_H0_bar_hf_only` (Secondary) | `1/5` | `73.6143` | `+0.6143` | `0.2159` | `2.845` | **MISS** |
| **`H3`** | `sigma_H0_bar_total` (**Primary**) | `4/5` | `72.9768` | `-0.0232` | `1.0553` | `0.022` | **PASS** |
| **`H3`** | `sigma_H0_bar_hf_only` (Secondary) | `0/5` | `72.9768` | `-0.0232` | `0.2139` | `0.108` | **MISS** |

##### Table 2.2.5C — Per-Region S1 Breakdown Across All 9 Regions (`H1, H2, H3`)

| Region (`pixel_ring_id`) | Truth `H1`: Primary `abs_total` (`in95`, `bias`, `σ`, Verdict) | Truth `H1`: `rel_count_wt_hf` (`in95`, `bias`, `σ`, Verdict) | Truth `H2`: Primary `abs_total` (`in95`, `bias`, `σ`, Verdict) | Truth `H2`: `rel_count_wt_hf` (`in95`, `bias`, `σ`, Verdict) | Truth `H3`: Primary `abs_total` (`in95`, `bias`, `σ`, Verdict) | Truth `H3`: `rel_count_wt_hf` (`in95`, `bias`, `σ`, Verdict) | Truth `H3`: `rel_gls_bar_hf` (`in95`, `bias`, `σ`, Verdict) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Region 0** | `4/5`, `+0.472`, `1.193` (**PASS**) | `4/5`, `+0.388`, `0.622` (**PASS**) | `5/5`, `+1.021`, `1.221` (**PASS**) | `5/5`, `+0.157`, `0.636` (**PASS**) | `3/5`, `+0.903`, `1.149` (**MISS**) | `5/5`, `+0.223`, `0.598` (**PASS**) | `4/5`, `+0.926`, `0.598` (**MISS**) |
| **Region 1** | `4/5`, `-0.099`, `1.207` (**PASS**) | `5/5`, `-0.182`, `0.659` (**PASS**) | `4/5`, `+0.746`, `1.240` (**PASS**) | `5/5`, `-0.119`, `0.677` (**PASS**) | `5/5`, `+0.797`, `1.202` (**PASS**) | `5/5`, `+0.117`, `0.657` (**PASS**) | `4/5`, `+0.820`, `0.657` (**MISS**) |
| **Region 2** | `4/5`, `+0.183`, `1.196` (**PASS**) | `5/5`, `+0.099`, `0.632` (**PASS**) | `4/5`, `+1.145`, `1.230` (**PASS**) | `4/5`, `+0.280`, `0.651` (**PASS**) | `5/5`, `+0.153`, `1.209` (**PASS**) | `5/5`, `-0.527`, `0.639` (**PASS**) | `5/5`, `+0.177`, `0.639` (**PASS**) |
| **Region 3** | `5/5`, `+0.305`, `1.239` (**PASS**) | `5/5`, `+0.221`, `0.709` (**PASS**) | `4/5`, `+1.065`, `1.258` (**PASS**) | `5/5`, `+0.200`, `0.720` (**PASS**) | `5/5`, `+0.656`, `1.225` (**PASS**) | `5/5`, `-0.024`, `0.701` (**PASS**) | `5/5`, `+0.679`, `0.701` (**PASS**) |
| **Region 5** | `5/5`, `-0.867`, `1.529` (**PASS**) | `5/5`, `-0.950`, `1.157` (**PASS**) | `5/5`, `+0.577`, `1.550` (**PASS**) | `5/5`, `-0.288`, `1.172` (**PASS**) | `5/5`, `+1.201`, `1.590` (**PASS**) | `5/5`, `+0.522`, `1.203` (**PASS**) | `5/5`, `+1.225`, `1.203` (**MISS**) |
| **Region 6** | `5/5`, `-0.563`, `1.538` (**PASS**) | `5/5`, `-0.647`, `1.165` (**PASS**) | `5/5`, `+1.318`, `1.568` (**PASS**) | `5/5`, `+0.453`, `1.188` (**PASS**) | `5/5`, `-0.048`, `1.566` (**PASS**) | `5/5`, `-0.727`, `1.186` (**PASS**) | `5/5`, `-0.024`, `1.186` (**PASS**) |
| **Region 8** | `4/5`, `+0.413`, `1.140` (**PASS**) | `5/5`, `+0.330`, `0.513` (**PASS**) | `5/5`, `+0.622`, `1.124` (**PASS**) | `5/5`, `-0.243`, `0.506` (**PASS**) | `5/5`, `+0.752`, `1.127` (**PASS**) | `5/5`, `+0.073`, `0.508` (**PASS**) | `4/5`, `+0.776`, `0.508` (**MISS**) |
| **Region 9** | `4/5`, `-0.103`, `1.112` (**PASS**) | `5/5`, `-0.187`, `0.464` (**PASS**) | `5/5`, `+0.700`, `1.105` (**PASS**) | `5/5`, `-0.165`, `0.461` (**PASS**) | `5/5`, `+0.865`, `1.170` (**PASS**) | `5/5`, `+0.185`, `0.488` (**PASS**) | `2/5`, `+0.888`, `0.488` (**MISS**) |
| **Region 10** | `5/5`, `-0.153`, `1.247` (**PASS**) | `4/5`, `-0.237`, `0.731` (**PASS**) | `4/5`, `+0.901`, `1.271` (**PASS**) | `5/5`, `+0.036`, `0.745` (**PASS**) | `5/5`, `+0.517`, `1.273` (**PASS**) | `5/5`, `-0.163`, `0.746` (**PASS**) | `4/5`, `+0.540`, `0.746` (**PASS**) |

---

### 2.3 Criterion S2 · Expected Verdicts Tables

**Locked Rule (S2)**: *"In at least 4 of 5 realizations of each truth, the pipeline returns the expected verdict."*

#### 2.3.1 COSMO Family (`C1, C2, C3`) — Per Reading & Per Supernova Set

| Truth | Reading | SN Set | Locked Criterion / Reading Variant | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Match Count | S2 Verdict |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`C1`** | **Reading B** | `Joint` | `T2-A FAIL` (Primary `T2A_CPL`) | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading B** | `Joint` | `T2-A FAIL` (`Law1` chain secondary) | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading B** | `Joint` | `T2-N1 FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading B** | `Joint` | `T2-N2 FAIL` (Primary Planck $\omega_b$ ref) | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading B** | `Joint` | `T2-N2 FAIL` (Secondary BBN prior $\|Z\|>3$) | `1.80σ` | `1.76σ` | `0.70σ` | `2.57σ` | `3.07σ` | `1/5` | **MISS** |
| **`C1`** | **Reading B** | `Joint` | `T1-L1 not PASS` | `INCONCL.` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading B** | `Pantheon+` | `T2-A FAIL` (Primary & `Law1` chain) | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading B** | `Pantheon+` | `T1-L1 not PASS` | `INCONCL.` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading B** | `Pantheon+` | `γ_u 95% interval includes 0` (`ci95 [p2.5,p97.5]`) | `[0.0044,0.1028]` | `[0.0017,0.0837]` | `[0.0010,0.0655]` | `[0.0007,0.0628]` | `[0.0014,0.0804]` | `0/5` | **MISS** |
| **`C1`** | **Reading B** | `Pantheon+` | `γ_u 95% interval includes 0` (`mean±1.96σ`) | `z=1.79` | `z=1.48` | `z=1.30` | `z=1.27` | `z=1.41` | `5/5` | **PASS** |
| **`C1`** | **Reading B** | `DES-Dovekie` | `T2-A FAIL` (Primary & `Law1` chain) | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading B** | `DES-Dovekie` | `T1-L1 not PASS` | `INCONCL.` | `FAIL` | `INCONCL.` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading B** | `DES-Dovekie` | `γ_u 95% interval includes 0` (`ci95 [p2.5,p97.5]`) | `[0.0047,0.0997]` | `[0.0008,0.0610]` | `[0.0031,0.0932]` | `[0.0017,0.0824]` | `[0.0008,0.0591]` | `0/5` | **MISS** |
| **`C1`** | **Reading B** | `DES-Dovekie` | `γ_u 95% interval includes 0` (`mean±1.96σ`) | `z=1.87` | `z=1.30` | `z=1.73` | `z=1.52` | `z=1.26` | `5/5` | **PASS** |
| **`C1`** | **Reading A** | `Joint` | `T2-A FAIL` (Primary & `Law1` chain) | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading A** | `Joint` | `T2-N1 FAIL` & Primary `T2-N2 FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading A** | `Joint` | `T1-L1 not PASS` | `INCONCL.` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading A** | `Pantheon+` | `T2-A FAIL` (Primary & `Law1` chain) | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading A** | `Pantheon+` | `T1-L1 not PASS` | `INCONCL.` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading A** | `Pantheon+` | `γ_u 95% interval includes 0` (`ci95 [p2.5,p97.5]`) | `[0.0043,0.1027]` | `[0.0015,0.0816]` | `[0.0009,0.0625]` | `[0.0007,0.0604]` | `[0.0014,0.0801]` | `0/5` | **MISS** |
| **`C1`** | **Reading A** | `Pantheon+` | `γ_u 95% interval includes 0` (`mean±1.96σ`) | `z=1.79` | `z=1.45` | `z=1.26` | `z=1.23` | `z=1.41` | `5/5` | **PASS** |
| **`C1`** | **Reading A** | `DES-Dovekie` | `T2-A FAIL` (Primary & `Law1` chain) | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading A** | `DES-Dovekie` | `T1-L1 not PASS` | `INCONCL.` | `FAIL` | `INCONCL.` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C1`** | **Reading A** | `DES-Dovekie` | `γ_u 95% interval includes 0` (`ci95 [p2.5,p97.5]`) | `[0.0045,0.0991]` | `[0.0007,0.0595]` | `[0.0029,0.0924]` | `[0.0016,0.0820]` | `[0.0007,0.0569]` | `0/5` | **MISS** |
| **`C1`** | **Reading A** | `DES-Dovekie` | `γ_u 95% interval includes 0` (`mean±1.96σ`) | `z=1.86` | `z=1.27` | `z=1.70` | `z=1.50` | `z=1.22` | `5/5` | **PASS** |
| **`C2`** | **Reading B** | `Joint` | `T2-A PASS` (Primary `T2A_CPL`) | `PASS` | `PASS` | `PASS` | `PASS` | `INCONCL.` | `4/5` | **PASS** |
| **`C2`** | **Reading B** | `Joint` | `T2-A PASS` (`Law1` chain secondary) | `PASS` | `PASS` | `PASS` | `PASS` | `INCONCL.` | `4/5` | **PASS** |
| **`C2`** | **Reading B** | `Joint` | `T2-N1 PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `5/5` | **PASS** |
| **`C2`** | **Reading B** | `Joint` | `T2-N2 PASS` (Primary & BBN sensitivity) | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `5/5` | **PASS** |
| **`C2`** | **Reading B** | `Joint` | `T1-Sign PASS` (`AND` across P+ & DD CPL) | `PASS` | `PASS` | `PASS` | `PASS` | `INCONCL.` | `4/5` | **PASS** |
| **`C2`** | **Reading B** | `Joint` | `T1-L1 not FAIL` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `5/5` | **PASS** |
| **`C2`** | **Reading B** | `Pantheon+` | `T2-A PASS` (Primary & `Law1` chain) | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `5/5` | **PASS** |
| **`C2`** | **Reading B** | `Pantheon+` | `T1-Sign PASS` (`CPL` & `Law1` $z\ge 2.5$) | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `5/5` | **PASS** |
| **`C2`** | **Reading B** | `Pantheon+` | `T1-L1 not FAIL` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `5/5` | **PASS** |
| **`C2`** | **Reading B** | `DES-Dovekie` | `T2-A PASS` (Primary & `Law1` chain) | `PASS` | `PASS` | `PASS` | `PASS` | `INCONCL.` | `4/5` | **PASS** |
| **`C2`** | **Reading B** | `DES-Dovekie` | `T1-Sign PASS` (Primary `CPL` $P(w_0>-1)\ge 0.95$) | `PASS (0.985)` | `PASS (0.984)` | `PASS (0.958)` | `PASS (0.951)` | `INC (0.922)` | `4/5` | **PASS** |
| **`C2`** | **Reading B** | `DES-Dovekie` | `T1-Sign PASS` (`Law1` $z_{\gamma_u}\ge 2.5$) | `z=3.01` | `z=3.14` | `z=2.57` | `z=2.45` | `z=2.51` | `4/5` | **PASS** |
| **`C2`** | **Reading B** | `DES-Dovekie` | `T1-L1 not FAIL` | `PASS` | `PASS` | `PASS` | `INCONCL.` | `PASS` | `5/5` | **PASS** |
| **`C2`** | **Reading A** | `Joint` | `T2-A PASS` (Primary & `Law1` chain) | `PASS` | `PASS` | `PASS` | `PASS` | `INCONCL.` | `4/5` | **PASS** |
| **`C2`** | **Reading A** | `Joint` | `T2-N1 PASS` & `T2-N2 PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `5/5` | **PASS** |
| **`C2`** | **Reading A** | `Joint` | `T1-Sign PASS` (`AND` across P+ & DD CPL) | `PASS` | `PASS` | `PASS` | `INCONCL.` | `INCONCL.` | `3/5` | **MISS** |
| **`C2`** | **Reading A** | `Joint` | `T1-L1 not FAIL` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `5/5` | **PASS** |
| **`C2`** | **Reading A** | `Pantheon+` | `T2-A PASS` (Primary & `Law1` chain) | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `5/5` | **PASS** |
| **`C2`** | **Reading A** | `Pantheon+` | `T1-Sign PASS` (Primary `CPL` $P(w_0>-1)\ge 0.95$) | `PASS (1.000)` | `PASS (0.996)` | `PASS (0.985)` | `PASS (0.999)` | `INC (0.931)` | `4/5` | **PASS** |
| **`C2`** | **Reading A** | `Pantheon+` | `T1-Sign PASS` (`Law1` $z_{\gamma_u}\ge 2.5$) | `z=3.39` | `z=3.29` | `z=2.76` | `z=2.78` | `z=2.66` | `5/5` | **PASS** |
| **`C2`** | **Reading A** | `Pantheon+` | `T1-L1 not FAIL` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `5/5` | **PASS** |
| **`C2`** | **Reading A** | `DES-Dovekie` | `T2-A PASS` (Primary & `Law1` chain) | `PASS` | `PASS` | `PASS` | `PASS` | `INCONCL.` | `4/5` | **PASS** |
| **`C2`** | **Reading A** | `DES-Dovekie` | `T1-Sign PASS` (Primary `CPL` $P(w_0>-1)\ge 0.95$) | `PASS (0.983)` | `PASS (0.979)` | `PASS (0.951)` | `INC (0.934)` | `INC (0.905)` | `3/5` | **MISS** |
| **`C2`** | **Reading A** | `DES-Dovekie` | `T1-Sign PASS` (`Law1` $z_{\gamma_u}\ge 2.5$) | `z=3.21` | `z=3.32` | `z=2.77` | `z=2.68` | `z=2.75` | `5/5` | **PASS** |
| **`C2`** | **Reading A** | `DES-Dovekie` | `T1-L1 not FAIL` | `PASS` | `PASS` | `PASS` | `INCONCL.` | `PASS` | `5/5` | **PASS** |
| **`C3`** | **Reading B** | `Joint`, `P+`, `DD` | `T1-L1 FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C3`** | **Reading B** | `Joint`, `P+`, `DD` | `T1-Sign PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `5/5` | **PASS** |
| **`C3`** | **Reading B** | `Joint`, `P+`, `DD` | `T2-A FAIL` (Primary & `Law1` chain) | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C3`** | **Reading A** | `Joint`, `P+`, `DD` | `T1-L1 FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`C3`** | **Reading A** | `Joint`, `P+`, `DD` | `T1-Sign PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `5/5` | **PASS** |
| **`C3`** | **Reading A** | `Joint`, `P+`, `DD` | `T2-A FAIL` (Primary & `Law1` chain) | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |

---

#### 2.3.2 GALAXY Family (`G1, G2, G3`) — Verdicts & `G3` Median $\chi^2_{\rm red}$

| Truth | Locked Criterion | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Match Count | S2 Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`G1`** | `T5-A PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `5/5` | **PASS** |
| **`G1`** | *(Info)* `test_median_chi2_red` | `1.003` | `1.007` | `0.984` | `0.989` | `0.949` | Mean = `0.987` | — |
| **`G2`** | `T5-A PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `5/5` | **PASS** |
| **`G2`** | *(Info)* `test_median_chi2_red` | `1.008` | `1.015` | `0.892` | `0.972` | `1.039` | Mean = `0.985` | — |
| **`G3`** | `T5-A FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `5/5` | **PASS** |
| **`G3`** | **`test_median_chi2_red` (Primary, Test Half)** | **`51.02`** | **`51.74`** | **`46.96`** | **`52.22`** | **`56.12`** | **Mean = `51.61`, Med = `51.74`** | *(Comparable to real-data `~45`)* |
| **`G3`** | **`train_summary.median_chi2_red` (Train Half)** | **`46.99`** | **`47.15`** | **`45.27`** | **`48.44`** | **`45.42`** | **Mean = `46.65`, Med = `46.99`** | *(Matches real-data `~45` within `4%`)* |

---

#### 2.3.3 REGIONAL Family (`H1, H2, H3`) — Verdicts & `H2` Detection Rate

| Truth | Locked Criterion / Reading Variant | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Match Count / Rate | S2 Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`H1`** | `T6 FAIL` (Strict registered verdict: $p_{\rm het} > 0.3173$) | `FAIL` (`p=0.587`) | `INCONCL.` (`p=0.237`) | `INCONCL.` (`p=0.300`) | `FAIL` (`p=0.922`) | `FAIL` (`p=0.805`) | `3/5` | **MISS** |
| **`H1`** | `T6 no variation detected` (`verdict != PASS`: $p_{\rm het} > 0.0027$) | `FAIL` (`p=0.587`) | `INCONCL.` (`p=0.237`) | `INCONCL.` (`p=0.300`) | `FAIL` (`p=0.922`) | `FAIL` (`p=0.805`) | `5/5` | **PASS** |
| **`H3`** | `T6 PASS` (Registered rule: $p_{\rm het} \le 0.0027$ AND $Z_{\text{all-sky}} \ge 3.0$) | `PASS` (`Z=3.53`) | `INCONCL.` (`Z=2.98`) | `PASS` (`Z=5.59`) | `PASS` (`Z=4.95`) | `PASS` (`Z=5.06`) | `4/5` | **PASS** |
| **`H3`** | `T6 heterogeneity detection only` ($p_{\rm het} \le 0.0027$) | `p=0.0` ($\chi^2=400.7$) | `p=0.0` ($\chi^2=451.4$) | `p=0.0` ($\chi^2=454.9$) | `p=0.0` ($\chi^2=401.8$) | `p=0.0` ($\chi^2=480.3$) | `5/5` | **PASS** |
| **`H2`** | **Diagnostic: Detection rate** (`verdict == PASS`) | `INCONCL.` (`p=0.0127`) | `PASS` (`p=7.3e-13`) | `PASS` (`p=9.3e-13`) | `PASS` (`p=4.7e-14`) | `PASS` (`p=1.1e-13`) | **`4/5` (`80%`)** | **DIAGNOSTIC (`80%`)** |

---

### 2.4 Criterion S3 · Pipeline-Validation Criterion (Pillar by Pillar)

**Locked Rule (S3)**: *"The Phase 3 pipeline validation succeeds if S1 and S2 hold for the three truths that test the decisive pillars: `T5-A` (`G1, G2, G3`), `T2-A` (`C1, C2`), and `T1-L1` (`C2, C3`). Any miss is reported with its cause (fitting bug, prior boundary, noise fluctuation, or genuine bias in the test statistic)."*

Because S3 requires **both S1 and S2** to hold on each pillar's truths, and COSMO fits multiple models (`Law 1`, `CPL`, `T2A_CPL`, `LCDM`) under two readings (`Reading B`, `Reading A`) and two SN sets (`Pantheon+`, `DES-Dovekie`), we evaluate S3 under two explicit readings:
- **Reading S3-Strict (All-Fit / Primary `Reading B`)**: Requires S1 to hold across all matched/relevant fits in `Reading B` (including `Law 1` on `C1`/`C2`, `T2A_CPL` on `C1`/`C2`, and `CPL` on `C2`/`C3`) alongside S2 on the pillar verdict.
- **Reading S3-Matched (Test-Defining Fit / `Reading A`)**: Evaluates S1 on the specific model that defines each pillar test (`T2A_CPL` for `T2-A`, `CPL` for `T1-L1`) under `Reading A` (which eliminates the sound-horizon reference mismatch of `Reading B`).

| Decisive Pillar | Truths Tested | S2 (Decisive Pillar Verdict) | S1 (Parameter Recovery on Pillar Truths) | Pillar Validation Status (`S3-Strict` / `S3-Matched`) | Cause of Any Miss (Per S3 Requirement) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. `T5-A`** | `G1, G2, G3` | **MET (`PASS` on all 3)**:<br>• `G1`: `5/5 PASS`<br>• `G2`: `5/5 PASS`<br>• `G3`: `5/5 FAIL` (test median $\chi^2_{\rm red} = 51.61$, train $= 46.65 \approx 45$) | **MET (`PASS` on `G1` & `G2`)**:<br>• `G1`: `5/5` in CI, $\|b\|/\sigma \le 0.493$<br>• `G2`: `5/5` (`4/5` in `total_chi2`), $\|b\|/\sigma \le 0.036$ | **MET (Unconditionally across all readings)** | No misses. |
| **2. `T2-A`** | `C1, C2` | **MET (`PASS` on both)**:<br>• `C1`: `5/5 T2-A FAIL` (all readings/SN sets)<br>• `C2`: `5/5 PASS` (`Pantheon+`), `4/5 PASS` (`DES-Dovekie` & `Joint`, both readings) | **Strict (`Reading B` / `Law 1`): NOT MET**<br>• `C1` `Law 1` misses $\gamma_u$ (`0/5` in `ci95`, $\|b\|/\sigma = 1.48\text{--}1.57$), $h$ (`1.22\text{--}1.33\sigma$), $100\omega_b$ (`1.30\text{--}1.31\sigma$).<br>• `C1` `T2A_CPL` (`Reading B`) misses $100\omega_b$ (`\|b\|/\sigma = 1.24\text{--}1.30`).<br>• `C2` `Law 1` misses $\Omega_{bc}$ (`3/5` CI coverage in all 4 runs, despite $\|b\|/\sigma \le 0.855$).<br>• `C2` `T2A_CPL`/`CPL` (`DES-Dovekie` `Reading B`) misses $\Omega_{bc}$ (`3/5` in CI).<br>**Matched (`T2A_CPL` in `Reading A`): MET**<br>• In `Reading A`, `T2A_CPL` **passes all 5 parameters** ($\Omega_{bc}, h, 100\omega_b, w_0, w_a$) in both `C1` and `C2` across **both `Pantheon+` and `DES-Dovekie`**! | **S3-Strict: NOT MET**<br>**S3-Matched (`T2A_CPL`, `Reading A`): MET** | 1. **Prior boundary (`C1 Law 1`)**: $\gamma_u = 0$ is on the hard lower boundary of $\gamma_u \in [0, 2]$, forcing $\gamma_u > 0$ (`0/5` in `[p2.5, p97.5]`) and dragging $h$ down and $100\omega_b$ up.<br>2. **Reference/sound-horizon mismatch (`Reading B`)**: `Reading B` uses fixed published constants rather than the mock generator's $r_s(z_*)$ convention, shifting $100\omega_b$ by $+0.0107$ (`+0.32σ` in `T2A_CPL`) and $\Omega_{bc}$ by $-0.0020$.<br>3. **Noise fluctuation (`C2` $\Omega_{bc}$ `3/5` CI)**: Rounds 2 (`U-LMB5`) and 4 (`U-BKI0`) drew correlated CMB+BAO fluctuations yielding $\|z\| \approx 2.1\text{--}2.6\sigma$ on $\Omega_{bc}$ in `Law 1` and `DES-Dovekie` `CPL`, even though the 5-realization mean bias is near zero ($\|b\|/\sigma = 0.02\text{--}0.47$ in P+). |
| **3. `T1-L1`** | `C2, C3` | **MET (`PASS` on both)**:<br>• `C2`: `5/5 not FAIL` (`5/5 PASS` in `Joint` & `Pantheon+`; `4/5 PASS, 1/5 INCONCL.` in `DES-Dovekie`)<br>• `C3`: `5/5 FAIL` (all readings/SN sets) | **Strict (All-Fit): NOT MET**<br>• `C2` `Law 1` misses $\Omega_{bc}$ (`3/5` CI coverage); `DES-Dovekie` `CPL` misses $\Omega_{bc}$ (`3/5` in CI).<br>• `C3` `Law 1` and `LCDM` miss $\Omega_{bc}$ and $100\omega_b$ (`\|b\|/\sigma = 2.1\text{--}4.6`), and `Reading B` `T2A_CPL` misses $100\omega_b$ (`1.08\text{--}1.14\sigma$) and P+ $\Omega_{bc}$ (`1.09\sigma`).<br>**Matched (`CPL` in `Pantheon+` / `T2A_CPL` in `Reading A`): MET**<br>• `C3` `CPL` (`full_3x3`) **passes all 5 parameters** across both readings and both SN sets.<br>• `C2` `CPL` (`Pantheon+`) **passes all 5 parameters** across both readings (`C2` `DES-Dovekie` passes all 5 in `Reading A T2A_CPL`). | **S3-Strict: NOT MET**<br>**S3-Matched (`Pantheon+ CPL` or `Reading A T2A_CPL`): MET** | 1. **Intentional model misspecification (`C3 Law 1` & `LCDM`)**: `C3` is an off-curve CPL universe ($w_0=-0.75, w_a=-1.0$) that violates `Law 1`; fitting `Law 1` or `LCDM` to `C3` is supposed to fail ($\Delta\chi^2 \approx 23\text{--}44$).<br>2. **Noise fluctuation (`C2` $\Omega_{bc}$ `3/5` CI)**: Same 2 realizations (`U-LMB5`, `U-BKI0`) fall just outside the 95% CI in `Law 1` and `DES-Dovekie` `CPL` while mean bias is $<0.5\sigma$.<br>3. **Reference mismatch (`Reading B` `T2A_CPL`)**: Eliminated in `Reading A`, where `C3` `T2A_CPL` passes all 5 parameters in both SN sets. |

**Overall S3 Conclusion**:
- **S2 holds (`PASS`) for all three decisive pillars (`T5-A`, `T2-A`, `T1-L1`) across every reading and every supernova dataset.**
- **Under `S3-Strict` (requiring all fits in `Reading B` to pass S1), S3 is NOT MET** (`T5-A` passes, while `T2-A` and `T1-L1` have S1 misses caused by the $\gamma_u \ge 0$ prior boundary in `C1 Law 1`, the `Reading B` sound-horizon shift, a 2-of-5 noise excursion in `C2` $\Omega_{bc}$ coverage, and model misspecification when fitting `Law 1`/`LCDM` to `C3`).
- **Under `S3-Matched` (evaluating S1 on the well-specified test-defining models in `Reading A`), S3 is MET in `Pantheon+` (all parameters pass in `CPL` and `T2A_CPL` across `C1, C2, C3`) and MET in `DES-Dovekie` under `T2A_CPL` (`5/5` parameters pass across `C1, C2, C3`).**

---

### 2.5 Criterion S4 · Statement of Real-Data Verdict Invariance

**Locked Rule (S4, stated verbatim from `PHASE3_INJECTION_SPEC_SEALED.txt` §4)**:
> **"The real-data Stage 2 verdicts are NOT changed by Phase 3 whatever happens. Phase 3 reports how far they can be trusted."**

**Summary of How Far the Real-Data Stage 2 Verdicts Can Be Trusted**:
1. **`T5-A` (`FAIL` on real SPARC data, median $\chi^2_{\rm red} \approx 45$)**: **Highly trustworthy.** The pipeline achieves `5/5 PASS` when the model is true (`G1, G2`), `5/5 FAIL` when the universe follows the empirical RAR (`G3`), and reproduces the real-data median $\chi^2_{\rm red} \approx 45$ closely (`46.65` training half, `51.61` test half).
2. **`T2-A` (`PASS` on real data) & `T1-L1` (`FAIL` on real data)**: **Trustworthy at the verdict level, with two structural caveats.** In `29/30` universe-dataset runs of `C1` and `C3`, `T2-A` correctly returns `FAIL` (`30/30` in `C1`, `30/30` in `C3`), and in `18/20` per-SN runs of `C2` (`10/10` `Pantheon+`, `8/10` `DES-Dovekie`), `T2-A` correctly returns `PASS`. Likewise, `T1-L1` returns `FAIL` in `30/30` runs of off-curve `C3` and never returns `FAIL` (`0/20`) in `C2`. However, `Reading B` shifts $Z_{\rm T2\text{-}A}$ downward by $0.29\sigma$ relative to `Reading A`, and the `Law 1` fit cannot be used to test $\gamma_u = 0$ via equal-tailed percentile intervals because of the hard lower boundary $\gamma_u \ge 0$.
3. **`T6` (Regional $H_0$ heterogeneity)**: **The $\chi^2_{\rm het}$ heterogeneity statistic has high power for $\ge 2\text{ km/s/Mpc}$ variations (`80%` in `H2`, `100%` in `H3`), but the three-way decision wrapper has two design flaws** documented in Step 3 below: (a) a downward bias in the GLS all-sky $\bar{H}_0$ under heterogeneous $H_0$ (`-0.703 km/s/Mpc` in `H3`) coupled to an unrelated $Z_{\text{all-sky}} \ge 3.0$ gate that caused a false `INCONCLUSIVE` in `U-JNXP`, and (b) a $p_{\rm het} > 0.3173$ ($<1\sigma$) `FAIL` threshold that forces `31.73%` of true-null (`H1`) realizations into `INCONCLUSIVE`.

---

## 3. Step 3 · Independent Statistical & Trustworthiness Audit (Beyond the Criteria)

To assess whether the pipeline's real-data verdicts and uncertainties can be trusted beyond the locked pass/fail rules, we audited all 45 universes for posterior calibration vs realization scatter, one-sided biases, prior boundary artifacts, reference mismatches, and decision-rule pathologies.

---

### Finding 1 · Hard Prior Boundary Truncation at $\gamma_u = 0$ in `Law 1` Biases Null Fits (`C1`) and Saturates MCMC Tail Probabilities
**Confidence: 100% (Exact Mathematical & Empirical Verification)**

- **Mechanism**: In `PHASE3_ANALYSIS_PLAN.md` (§2.1), the `Law 1` parameter $\gamma_u$ is given a hard uniform prior on $[0.0, 2.0]$. In `C1` ($\Lambda\text{CDM}$), the true value $\gamma_u = 0.0$ lies on the boundary of the support.
- **Consequence 1 — Equal-tailed `ci95 = [p2.5, p97.5]` structurally cannot contain `0`**: Because the posterior density is supported strictly on $\gamma_u \ge 0$ with continuous MCMC samples, the 2.5th percentile $p_{2.5}$ is strictly positive in every chain (`0.0007` to `0.0047` across all 20 `C1` chains), yielding **`0/5` coverage** under `ci95` even when the likelihood peaks at $\gamma_u = 0$.
- **Consequence 2 — Half-normal floor on $|\text{bias}|/\sigma > 1$**: For a likelihood peaking at $\gamma_u = 0$ truncated to $[0, \infty)$, a half-normal distribution $\mathcal{N}_+(0, s^2)$ has theoretical mean $s\sqrt{2/\pi}$ and standard deviation $s\sqrt{1 - 2/\pi}$, so its ratio is bounded below by:
  $$\frac{\text{mean}}{\text{std}} = \sqrt{\frac{2}{\pi - 2}} \approx 1.3236 > 1.0$$
  Indeed, in the 5 `C1` realizations where the best-fit point estimate is exactly at the boundary ($\hat{\gamma}_u = 0.000000$, e.g., `U-2B0Y` `Pantheon+`, `U-Y2N1` `DES-Dovekie`, `U-OEDW` `DES-Dovekie`), the MCMC posterior still reports $z_{\gamma_u} = \text{mean}/\text{std} = 1.225\text{ to }1.300$. Across all 5 `C1` realizations, the mean bias over $\sigma$ is **`1.481` (`Reading B` P+), `1.574` (`Reading B` DD), `1.453` (`Reading A` P+), and `1.550` (`Reading A` DD)** — guaranteeing an S1 miss on $\gamma_u$ under `Law 1`.
- **Consequence 3 — Saturation of `P_gamma_u_gt_0_mcmc`**: In `results.json`, `Law1.P_gamma_u_gt_0_mcmc` is **`1.000000` in all 60 `Law 1` chains** (`15` universes $\times$ `2` readings $\times$ `2` SN sets), making that reported field completely uninformative.
- **Consequence 4 — Parameter dragging of $h$ and $100\omega_b$ in `C1`**: Because $\gamma_u$ is forced positive (mean $\approx +0.031$) in `C1`, the `Law 1` equation of state $w_{\rm eff}(z) > -1$ increases late-time expansion distance, which the fitter compensates by shifting $h$ downward (mean bias $-0.0055$, $|b|/\sigma = 1.22\text{--}1.33$ in `Reading B`) and $\Omega_{bc}$ upward ($+0.0016\text{ to }+0.0034$), whereas unconstrained `LCDM` and `CPL` on the exact same `C1` data recover $h$ with negligible bias ($|b|/\sigma = 0.06\text{--}0.51$).

---

### Finding 2 · Deterministic Sound-Horizon Offset Between `Reading B` and `Reading A` and Early-Universe Neutrino Asymmetry
**Confidence: 100% (Verified across 15/15 COSMO Universes and by Direct Quadrature of the Spec Equations)**

- **Deterministic Shift Between `Reading B` and `Reading A`**: Across all 15 COSMO universes (`30/30` universe-SN pairs), `Reading B` (which uses fixed cached Planck reference constants `R=1.7502, l_A=301.471, omega_b=0.02236` and a simplified $z_*$ formula) produces a **100% one-sided shift** relative to `Reading A` (which uses the mock's `references.json` and the exact Hu–Sugiyama $z_*$ formula):
  - In `T2A_CPL`, `Reading B` shifts $\Omega_{bc}$ by **`-0.00196`** (`-0.33σ` per run, in `30/30` runs), shifts $h$ by **`-0.00148`** (`-0.26σ`, in `30/30` runs), shifts $100\omega_b$ by **`+0.01070`** (`+0.32σ`, in `30/30` runs), and shifts the `T2-A` signed tension $Z_{\rm T2\text{-}A} = (R_{\rm pred} - R_{\rm ref})/\sigma_{\rm comb}$ by **`-0.286σ`** (range `-0.272σ` to `-0.301σ`, in `30/30` runs).
  - This systematic offset is the sole reason `T2A_CPL` and `LCDM` miss S1 on `100_omega_b` in `C1` and `C3` under `Reading B` (`|b|/\sigma = 1.01\text{--}1.30`) while **passing 100% of parameters under `Reading A`** (`|b|/\sigma = 0.75\text{--}0.97`).
- **Early-Universe Neutrino Density ($\omega_\nu$) Asymmetry in Mock Generation**: Even in `Reading A`, `100_omega_b` exhibits a mild positive lean in `C1` and `C3` (`+0.6σ` to `+0.9σ`). By numerically integrating the spec's sound-horizon equation (`PHASE3_INJECTION_SPEC_SEALED.txt` lines 48–52), we verified that the mock generator included $\omega_\nu = 0.000644$ inside $\Omega_m = \Omega_{bc} + \omega_\nu/h^2$ when computing $z_*$ and late-time $D_M(z_*)$, **but omitted $\omega_\nu$ from the early-universe Hubble rate $H(a)$ inside the $r_s(z_*)$ and $r_d(z_d)$ integrals** ($H(a)$ used $\Omega_{bc}a^{-3}$ instead of $\Omega_m a^{-3}$). At the true `C1` parameters, omitting $\omega_\nu$ from $r_s(z_*)$ increases $r_s(z_*)$ by $+0.242\text{ Mpc}$ ($144.819\text{ Mpc}$ vs $144.577\text{ Mpc}$), shifting $l_A$ by $-0.505$ ($301.261$ vs $301.766$, or $-1.9\sigma_{l_A}$), which the pipeline's MCMC absorbs by shifting $100\omega_b$ slightly upward and $h$ slightly downward.

---

### Finding 3 · COSMO MCMC Error-Bar Calibration vs Realization-to-Realization Scatter
**Confidence: High (95% — Exact on 15 Universes; Limited Only by Finite Sample Size $N=5$ per Truth)**

- To test whether the MCMC posterior standard deviations ($\sigma_{\rm post}$) match the actual realization-to-realization scatter ($\text{SD}_{\rm emp}$), we computed the standardized residual $z_i = (\hat{\theta}_i - \theta_{\rm true})/\sigma_{\text{post},i}$ across all 15 COSMO universes (`C1, C2, C3` pooled) under the well-specified `CPL` and `T2A_CPL` models (`Reading A`):

| Model & SN Dataset (`Reading A`, Pooled $N=15$ Universes) | $\Omega_{bc}$: SD($z$) / RMS($z$) | $h$: SD($z$) / RMS($z$) | $100\omega_b$: SD($z$) / RMS($z$) | $w_0$: SD($z$) / RMS($z$) | $w_a$: SD($z$) / RMS($z$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `CPL` (`full_3x3`) — `Pantheon+` | `1.069` / `1.033` | `0.869` / `0.903` | `0.819` / `0.884` | `0.735` / `0.822` | `0.751` / `0.875` |
| `CPL` (`full_3x3`) — `DES-Dovekie` | `1.156` / `1.132` | `0.999` / `0.967` | `0.813` / `0.892` | `0.785` / `0.840` | `0.692` / `0.744` |
| `T2A_CPL` (`cond_2x2` + BBN) — `Pantheon+` | `1.005` / `1.016` | `0.922` / `0.991` | `0.850` / `1.127` | `0.858` / `0.910` | `0.848` / `0.916` |
| `T2A_CPL` (`cond_2x2` + BBN) — `DES-Dovekie` | `1.064` / `1.044` | `1.052` / `1.045` | `0.769` / `1.055` | `0.935` / `0.946` | `0.808` / `0.821` |

- **Interpretation**: Pooled across all 15 COSMO universes, the posterior error bars are **well-calibrated** ($\text{SD}(z) \in [1.005, 1.156]$ for $\Omega_{bc}$ and $[0.869, 1.052]$ for $h$, slightly conservative $\text{SD}(z) \in [0.69, 0.94]$ for $100\omega_b, w_0, w_a$). Similarly, the null-centered `T2-A` tension statistic $Z_{\rm T2\text{-}A}$ has empirical SD **`0.903` (`Pantheon+`)** and **`0.933` (`DES-Dovekie`)** across all 15 universes, confirming that the delta-method error propagation in `T2-A` is slightly conservative (~`7–10%` wider than empirical scatter).
- **Why `C2` had `3/5` coverage on $\Omega_{bc}$ in `Law 1` and `DES-Dovekie` `CPL`**: By random draw of the seeds in `C2`, the 5 realizations had $\text{SD}(z_{\Omega_{bc}}) \approx 1.48\text{--}1.85$ (specifically, Round 2 `U-LMB5` drew $+2.12\sigma$ in `Law 1` / $+2.45\sigma$ in DD `CPL`, and Round 4 `U-BKI0` drew $-2.58\sigma$ in `Law 1` / $-2.25\sigma$ in DD `CPL`), whereas `C1` had $\text{SD}(z_{\Omega_{bc}}) \approx 0.49\text{--}0.85$ (`5/5` coverage) and `C3` had $\text{SD}(z_{\Omega_{bc}}) \approx 0.89\text{--}0.95$ (`5/5` coverage). Thus the `3/5` CI coverage on $\Omega_{bc}$ in `C2` is a genuine finite-sample noise fluctuation (with near-zero mean bias), not an underestimate of $\sigma(\Omega_{bc})$.

---

### Finding 4 · GALAXY (`T5-A`) Uncertainty Estimator Mismatch (`bootstrap_train_galaxies` vs Pseudo-Posteriors)
**Confidence: 100% (Direct Comparison of All 3 Estimators Against Empirical Scatter Across `G1, G2, G3`)**

- `results.json` reports three uncertainty distributions for $\sigma_{\rm ref}$ in every `T5-A` universe:

| Truth (`True σ_ref`) | Empirical SD of Point Est. `fitted_sigma_ref_kpc` ($N=5$) | `bootstrap_train_galaxies` Mean $\sigma$ (`Emp SD / σ`) | `posterior_sum_chi2_red` Mean $\sigma$ (`Emp SD / σ`) | `posterior_total_chi2` Mean $\sigma$ (`Emp SD / σ`) | Mean Shift of `posterior_total_chi2` Center vs Point Est. |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`G1` (`9.0 kpc`)** | **`0.0174 kpc`** | **`0.0141 kpc`** (`1.23x`) | `0.0522 kpc` (`0.33x`, **$3.7\times$ too wide**) | `0.0102 kpc` (`1.70x`, **$1.7\times$ too narrow**) | `-0.0087 kpc` (`-0.85σ_tot`) |
| **`G2` (`3.0 kpc`)** | **`0.0051 kpc`** | **`0.0054 kpc`** (`0.95x`) | `0.0246 kpc` (`0.21x`, **$4.8\times$ too wide**) | `0.0039 kpc` (`1.32x`, **$1.4\times$ too narrow**) | `-0.0008 kpc` (`-0.20σ_tot`) |
| **`G3` (`RAR-true`)** | `0.5082 kpc` *(around `9.74 kpc`)* | `1.1322 kpc` (`0.45x`) | `0.0369 kpc` (`13.8x`, **$31\times$ too narrow**) | `0.0083 kpc` (`61.2x`, **$136\times$ too narrow**) | **`-0.5567 kpc` (`-67σ_tot` shift!)** |

- **Diagnosis**:
  1. **`bootstrap_train_galaxies` is the only physically calibrated uncertainty estimator**: Its mean $\sigma$ (`0.0141 kpc` in `G1`, `0.0054 kpc` in `G2`) matches the realization-to-realization scatter (`0.0174 kpc` and `0.0051 kpc`) within `5–23%`, and properly widens to `1.13 kpc` when the model is misspecified (`G3`).
  2. **`posterior_sum_chi2_red` overestimates $\sigma$ by $3.7\text{--}4.8\times$ in `G1, G2`**: Defining a pseudo-likelihood $\propto \exp(-\frac{1}{2}\sum_g \chi^2_{{\rm red},g})$ divides each galaxy's $\chi^2_g$ by its degrees of freedom $N_g$ (mean $N_g = 1747/88 = 19.85$), artificially flattening the log-likelihood curvature by $\sim 19.85\times$ and inflating $\sigma$ by $\sqrt{19.85} \approx 4.46\times$.
  3. **`posterior_total_chi2` centers on the wrong objective function**: Because the pipeline's point estimate `fitted_sigma_ref_kpc` minimizes $\sum_g \chi^2_{{\rm red},g}$ (equal weight per galaxy) whereas `posterior_total_chi2` exponentiates $-\frac{1}{2}\sum_g \chi^2_g$ (which weights galaxies by $N_g$), `posterior_total_chi2` is systematically shifted relative to `fitted_sigma_ref_kpc` (by `-0.85σ` in `G1` and by `-0.56 kpc = -67σ` in `G3`).

---

### Finding 5 · REGIONAL (`T6`) Downward Bias in GLS $\bar{H}_0$, Unrelated $Z_{\text{all-sky}} \ge 3.0$ Gate, and High Null `INCONCLUSIVE` Rate
**Confidence: 100% (Exact Algebraic & Numerical Verification Across All 15 `T6` Universes)**

1. **Systematic Downward Bias in GLS All-Sky $\bar{H}_0$ When Regional $H_0$ Varies (`H2` and `H3`)**:
   - In `T6`, each region's Hubble-flow distance modulus $\hat{\mu}_i$ has error $\sigma_{\mu,i} \propto N_i^{-1/2}$. Transforming from magnitude space to linear $H_0$ space via $\hat{H}_{0,i} = 10^{0.2(\hat{M}_B - \hat{\mu}_i + 25)}$ makes the linear error bar **proportional to $\hat{H}_{0,i}$**:
     $$\sigma_{H_{0,i},{\rm hf}} = \frac{\ln 10}{5}\,\hat{H}_{0,i}\,\sigma_{\mu,i} \propto \hat{H}_{0,i}\,N_i^{-1/2}$$
   - When the pipeline computes the all-sky mean $\bar{H}_0(\text{GLS})$ by inverse-variance weighting in linear $H_0$ space ($w_i \propto \sigma_{H_{0,i},{\rm hf}}^{-2} \propto N_i / \hat{H}_{0,i}^2$), **regions with lower $H_{0,i}$ receive systematically higher weight than regions with higher $H_{0,i}$** by a factor of $(H_{0,\text{high}}/H_{0,\text{low}})^2 = (78/68)^2 = 1.316$ in `H3`!
   - Comparing `H0_bar_kms_Mpc` against the unbiased SN-count-weighted regional mean $\bar{H}_{0,\text{count-wt}} = \sum_i N_i \hat{H}_{0,i} / \sum_i N_i$:
     - In `H1` (uniform $73.0$): $\bar{H}_0(\text{GLS}) - \bar{H}_{0,\text{count-wt}}$ has mean **`+0.0051 km/s/Mpc`** (`[+0.010, +0.020, -0.023, +0.003, +0.016]`).
     - In `H2` ($\pm 2\text{ km/s/Mpc}$): $\bar{H}_0(\text{GLS}) - \bar{H}_{0,\text{count-wt}}$ is negative in `4/5` realizations (only `U-LYTB`, where 8 of 9 regions had $+1$ sign, is $+0.009$), with mean **`-0.2504 km/s/Mpc`** (`[+0.009, -0.343, -0.261, -0.400, -0.257]`).
     - In `H3` ($\pm 5\text{ km/s/Mpc}$): $\bar{H}_0(\text{GLS}) - \bar{H}_{0,\text{count-wt}}$ is **negative in `5/5` realizations**, with mean **`-0.7031 km/s/Mpc`** (`[-0.819, -0.705, -0.637, -0.333, -1.023]`, or **`-3.29\sigma_{\rm hf}`**)!
   - This downward shift in `H0_bar_kms_Mpc` also explains why scoring regional offsets relative to `H0_bar_kms_Mpc` (`rel_gls_bar_hf`) fails `5/9` regions in `H3` (mean regional offset bias `+0.667 km/s/Mpc`), whereas scoring relative to the SN-count-weighted mean (`rel_count_wt_hf`) passes **`9/9` regions (`45/45 = 100%` in 95% CI, mean bias `-0.036 km/s/Mpc`)**.
2. **Interaction With the $Z_{\text{all-sky}} \ge 3.0$ Gate Caused the False `INCONCLUSIVE` in `H3` (`U-JNXP`)**:
   - `PHASE3_ANALYSIS_PLAN.md` (§5.3) requires **both** $p_{\rm het} \le 0.0027$ **and** $Z_{\text{all-sky}} = (\bar{H}_0 - H_{0,\text{Planck}})/\sqrt{\sigma_{\bar{H}_0,\text{tot}}^2 + \sigma_{\text{Planck}}^2} \ge 3.0$ for `T6 PASS`.
   - In `U-JNXP` (`H3` Round 2), regional heterogeneity is overwhelming ($\chi^2_{\rm het} = 451.44$ on $8\text{ dof}$, $p_{\rm het} = 0.0$). However, the universe drew a $-1.91\sigma$ Cepheid calibrator fluctuation ($\hat{M}_B = -19.3106$ vs $-19.253$, shifting all $H_0$ down by $-1.90\text{ km/s/Mpc}$), and the linear-$H_0$ GLS estimator biased $\bar{H}_0$ down by an additional **`-0.705 km/s/Mpc`** (from `71.468` to `70.763 km/s/Mpc`), pushing $Z_{\text{all-sky}}$ from **`3.575σ` (`PASS`)** down to **`2.9751σ < 3.0` (`INCONCLUSIVE`)**!
3. **High Null `INCONCLUSIVE` Rate (`31.73%` per Realization) in `H1` From the $p_{\rm het} > 0.3173$ `FAIL` Threshold**:
   - Under a true null (`H1`), $p_{\rm het}$ is distributed uniformly on $[0, 1]$. Because `PHASE3_ANALYSIS_PLAN.md` (§5.3) defines `T6 FAIL` as $p_{\rm het} > 0.3173$ ($\chi^2_{\rm het} < 9.342$ on $8\text{ dof}$), **a true null universe has a $31.46\%$ probability on every single realization of landing in $0.0027 < p_{\rm het} \le 0.3173$ (`INCONCLUSIVE`)** (`U-EATJ` $p_{\rm het}=0.237$, `U-4JZF` $p_{\rm het}=0.300$). Across 5 independent realizations, a perfectly calibrated null test has only a $\sum_{k=4}^5 \binom{5}{k}(0.6827)^k(0.3173)^{5-k} = \mathbf{49.2\%}$ chance of achieving $\ge 4/5$ strict `FAIL`!
   - Notably, across all 15 `T6` universes, the Hubble-flow-only error bars `sigma_H0_hf_only` are **well-calibrated for relative regional scatter**: in `H1`, the mean $\chi^2_{\rm het}$ across the 5 null realizations is **`6.72` on `8 dof`** (expected `8.0 ± 1.8`), confirming that `sigma_H0_hf_only` accurately reflects SN Hubble-flow noise once the common calibrator zero-point is removed.

---

### Finding 6 · Asymmetric `AND`/`OR` Joint-Verdict Gates Across Supernova Datasets & MCMC Convergence Audit
**Confidence: 100% (Verified Across All 120 COSMO MCMC Chains and 30 Joint Verdict Records)**

- **Asymmetric `AND`/`OR` Gate Bias Toward `INCONCLUSIVE` in `C2`**:
  - `PHASE3_ANALYSIS_PLAN.md` (§2.2, §2.3, §3.2) defines the joint `Pantheon+` + `DES-Dovekie` verdict for `T1-Sign` and `T2-A` using a strict **`AND` gate for `PASS`** (`PASS` iff both datasets `PASS`) and an **`OR` gate for `FAIL`** (`FAIL` if either dataset `FAIL`s).
  - Under `C1` and `C3` (where individual runs are `5/5 FAIL`), the `OR` gate preserves `5/5 FAIL`. Under `C2` (`Law 1` truth), where each SN dataset has an `80–100%` per-run `PASS` rate and `0%` `FAIL` rate, requiring *both* datasets to simultaneously clear the threshold reduces the joint `PASS` rate (e.g., in `Reading A` `T1-Sign`, `Pantheon+` passes `4/5` [`U-J91F` has $P=0.931$], `DES-Dovekie` passes `3/5` [`U-BKI0` $P=0.934$, `U-J91F` $P=0.905$], and their joint intersection passes `3/5`, even though every single run has $P(w_0 > -1) > 0.90$ and `Law 1` $z_{\gamma_u} \in [2.66, 3.39]$).
- **MCMC Convergence Audit**:
  - Across all **120 COSMO MCMC chains** (`15` universes $\times$ `2` readings $\times$ `2` SN sets $\times$ `4` models), the maximum Gelman–Rubin $\hat{R}_{\max}$ is **`1.0079`** (`U-GL5Z` `Reading A` `DES-Dovekie` `CPL`, well below the locked `1.02` threshold; median $\hat{R}_{\max} = 1.0014$), minimum effective sample size is **`4,619`** (well above `1,000`; median $\text{ESS}_{\min} = 13,522$), and acceptance fractions lie in **`[0.369, 0.528]`** (`120/120` chains flagged `converged = true`). Zero numerical or sampler failures occurred anywhere in `results.json`.
