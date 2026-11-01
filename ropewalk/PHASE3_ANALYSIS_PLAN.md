---
title: "MULTIVERSE v1: Phase 3 Injection Tests — Blind Analysis Plan (PHASE3_ANALYSIS_PLAN.md)"
subtitle: "Phase 3 injection tests: supplementary, not pre-registered in Stage 1"
author: "Gregory Mandarano / WickedAI — Executed by Gemini 4 Argon"
date: "2026-10-31"
---

# MULTIVERSE v1: PHASE 3 ANALYSIS PLAN (`Phase 3 injection tests: supplementary, not pre-registered in Stage 1`)

> **STATUS LABEL:** **Phase 3 injection tests: supplementary, not pre-registered in Stage 1.**
>
> Stage 2 (`RESULTS_v5.sha256`) and the supplementary Bayesian head-to-head comparison (`HEAD_TO_HEAD_RESULTS_v1.sha256`) are frozen and untouched. This document locks all analysis settings, thin-wrapper overrides, exact package versions, random seeds, convergence rules, decision rules, and the round-by-round run order for the blind analysis of the 45 mock universes in `MOCKS_FOR_ARGON/` prior to the first run.

---

## 1. Non-Modification Guarantees & Blind Protocol

1. **Frozen Files Untouched:** No file listed in `PREREG_v4.sha256`, `DATA_MANIFEST.sha256`, `RESULTS_v1.sha256` through `RESULTS_v5.sha256`, or `HEAD_TO_HEAD_RESULTS_v1.sha256` (including root `ACTIVITY_LOG.md`, `scripts/*.py`, and `head_to_head/*.py`) will ever be modified, moved, or overwritten. All Phase 3 code, logs, chains/summaries, and deliverables are written exclusively inside `D:\Argon_Code\Ropewalk\phase3\` (with `PHASE3_ANALYSIS_PLAN.sha256[.ots]` and `PHASE3_RESULTS_v1.sha256[.ots]` also mirrored to workspace root if needed for convenience).
2. **Blind Execution:** Every mock universe is analyzed with the exact registered Stage 2 procedures, priors, samplers, convergence rules, and decision rules, without any per-universe adjustment and without attempting to infer hidden generating truths or searching for any answer key.
3. **Logging & Deviations:** Every action and command is appended with local ISO-8601 timestamps to `phase3/ACTIVITY_LOG_PHASE3.md`. Any change after `PHASE3_ANALYSIS_PLAN.md` is hashed into `phase3/PHASE3_ANALYSIS_PLAN.sha256` and stamped with OpenTimestamps (`ots stamp`) must be recorded in `phase3/DEVIATIONS.md` (with what, why, and expected effect) before the affected run.

---

## 2. Pinned Environment, Exact Package Versions, and Hardware Configuration

- **Workspace & Virtual Environment:** `D:\Argon_Code\Ropewalk\.venv`
- **Python Version:** `3.14.7 (tags/v3.14.7:823f032, Aug 5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)]`
- **Pinned Packages (`requirements.txt`):**
  - `numpy == 2.5.4`
  - `scipy == 1.18.1`
  - `emcee == 3.1.6`
  - `matplotlib == 3.11.2`
  - `psutil == 7.2.2`
  - `opentimestamps-client == 0.8.0`
- **Hardware & Thread Cap (`GEMINI.md` Rule 5 & `ARGON_PHASE3_HANDOFF.txt`):**
  - Every Python script begins with single-thread BLAS environment headers (`OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1`) before importing `numpy`, `scipy`, or `emcee`.
  - Parallel worker pools are capped at `N_CORES = 12` workers (leaving 8 physical / 16 logical threads free on the 20-core / 28-thread machine, exceeding the handoff minimum of ~4 free threads), with worker priority set to `psutil.BELOW_NORMAL_PRIORITY_CLASS`.

---

## 3. Thin Wrappers for Frozen Stage 2 & Head-to-Head Code (`phase3/phase3_wrappers.py`)

Per `ARGON_PHASE3_HANDOFF.txt` lines 16–20 and 27–29 and the pre-run clarification logged in `phase3/DEVIATIONS.md` (`Entry P3-C1`), `scripts/cosmology.py`, `scripts/run_part8_fixes.py`, `scripts/run_part9_cosmology_tests.py`, `scripts/sparc_t5.py`, `scripts/local_h0_t6.py`, and `head_to_head/h2h_cosmology.py` are imported read-only without modification. Where frozen classes hard-code real-universe file paths or external constants, thin subclasses/wrappers in `phase3/phase3_wrappers.py` override **only** the input data loading as follows:

1. **`MockDESIBAOLikelihood(cosmo.DESIBAOLikelihood)`:**
   - Calls `super().__init__(u_dir, lya_mode="unmodified")` to load `<u_dir>/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt` and `desi_gaussian_bao_ALL_GCcomb_cov.txt`.
   - When `lya_mode == "joint_ap_deciding"` (the registered deciding mode), instead of hard-coding the real-universe `arXiv:2607.27410` numbers (`39.32`, `8.600`, `0.33`, `0.066`, `-0.431`), it reads `<u_dir>/desi_bao_dr2/lya_bao_ap_joint.json` and replaces the `z = z_eff` (`2.33`) `DM_over_rs` and `DH_over_rs` mean entries and $2\times 2$ covariance block with `DM_over_rd`, `DH_over_rd`, `sigma_DM_over_rd`, `sigma_DH_over_rd`, and `corr_DH_DM` from that universe's `lya_bao_ap_joint.json`, then recomputes `self.inv_cov = scipy.linalg.inv(self.cov)`. All distance and $\chi^2$ methods (`_model_vector`, `chi2_cpl`, `chi2_law1`) are inherited unmodified.
2. **`MockCMBLikelihood(cosmo.CMBLikelihood)`:**
   - Instead of hard-coding the real-universe Chen, Huang & Wang (2019, Table 1) mean vector `[1.7502, 301.471, 2.236]`, it reads `<u_dir>/cmb_distance_prior/distance_prior.json` and initializes `self.mu = np.array(d["mean"], dtype=float)`, `self.sig = np.array(d["sigma"], dtype=float)`, and `self.corr = np.array(d["correlation"], dtype=float)`, then computes `self.cov3`, `self.inv_cov3`, `self.c11`, `self.c12`, `self.c22`, `self.cond_cov2`, `self.inv_cond_cov2`, and `self.inv_marg_cov2` identically to `cosmo.CMBLikelihood.__init__`. The `chi2(self, vec3)` method (`full_3x3`, `conditional_2x2`, `marginal_2x2`) is inherited unmodified.
3. **`MockPantheonPlusLikelihood(cosmo.PantheonPlusLikelihood)`:**
   - In `MOCKS_FOR_ARGON/<u_id>/`, the Pantheon+ folder is named `pantheonplus/` (without an underscore), whereas `cosmo.PantheonPlusLikelihood.__init__` looks for `pantheon_plus/`. `MockPantheonPlusLikelihood.__init__(self, u_dir)` loads `<u_dir>/pantheonplus/Pantheon+SH0ES.dat` and `<u_dir>/pantheonplus/Pantheon+SH0ES_STAT+SYS.cov` using the exact same selection (`zHD > 0.01` and `IS_CALIBRATOR == 0`) and matrix inversion as `cosmo.PantheonPlusLikelihood.__init__`, and inherits `_chi2_from_Iz`, `_chi2_from_E_grid`, `chi2_cpl`, and `chi2_law1` unmodified.
4. **`cosmo.DESDovekieLikelihood(u_dir)`:**
   - Used directly with no wrapper required because `<u_dir>/des_dovekie/DES-Dovekie_HD.csv` and `<u_dir>/des_dovekie/STAT+SYS.npz` match the exact relative path in `cosmo.DESDovekieLikelihood.__init__`.
5. **External Reference Measurements (`<u_dir>/REFERENCES.json`):**
   - For each `COSMO` universe, `<u_dir>/REFERENCES.json` provides:
     - `R_omegac_over_omegab`: `{"value": R_ref, "sigma": sig_R_ref}` (replaces real Planck `5.36 ± 0.065` in `T2-A`),
     - `Omega_b`: `{"value": Ob_ref, "sigma": sig_Ob_ref}` (replaces real Planck `0.04930 ± 0.00086` in `T2-N1`),
     - `100omega_b`: `{"value": wb100_ref, "sigma": sig_wb100_ref}` (with $\omega_b = \text{wb100\_ref}/100$, $\sigma_{\omega_b} = \text{sig\_wb100\_ref}/100$; replaces real Planck `0.02237 ± 0.00015` in `T2-N2`),
     - `H0`: `{"value": H0_ref, "sigma": sig_H0_ref}` (replaces real Planck `67.36 ± 0.54` in `T2-N2`),
     - `BBN_100omega_b_prior`: `{"value": bbn_mu, "sigma": bbn_sig}` (replaces real DESI/LUNA BBN `2.218 ± 0.055` in `T2-A`).
6. **`GALAXY` and `REGIONAL` Loaders (Used Unmodified):**
   - `GALAXY`: `sparc_t5.parse_sparc_catalog(<u_dir> / "sparc")`, `sparc_t5.fit_sparc_parameter`, `sparc_t5.evaluate_sparc_sample`, and `sparc_t5.score_t5_subtest` are called directly on `<u_dir>/sparc` with fixed `f_leak = 1.0 / 6.0` per `ARGON_PHASE3_HANDOFF.txt` lines 48–50.
   - `REGIONAL`: `local_h0_t6.load_pantheon_plus_full(<u_dir> / "pantheonplus")`, `local_h0_t6.fit_t6_calibrators`, and `local_h0_t6.evaluate_t6_hubble_flow(..., coord_frame="galactic", z_col="zHD", apply_merge=True)` are called directly with no wrapper required.

---

## 4. Exact Procedures, Priors, Samplers, and Verdicts Per Family

### 4.1 Family 1: `COSMO` (15 Universes; Both SN Compilations `Pantheon+` and `DES-Dovekie` Separately)

#### Sampler, Seeds, and Convergence Rules (Identical to Stage 2 `run_part8_fixes.py` & `run_part9_cosmology_tests.py`)
- **MCMC Sampler:** `emcee.EnsembleSampler` with `n_walkers = 32`, `n_burn = 1000`, `n_prod = 4000` (`128,000` post-burn-in samples), initialized around the Nelder–Mead preliminary optimum with the exact Stage 2 step scales.
- **Convergence Gate:** Split Gelman–Rubin $\max|\hat{R} - 1| < 0.01$ and minimum effective sample size $\min\text{ESS} > 1000$ (`compute_split_rhat_and_ess` imported from `scripts/run_part8_fixes.py`), with up to 2 automatic extensions of `2000` steps each if needed.
- **Polished $\chi^2_{\min}$:** `polish_chi2_min` imported from `scripts/run_part9_cosmology_tests.py` (Nelder–Mead `xatol=1e-6, fatol=1e-6, maxiter=10000` from the 5 highest-likelihood MCMC samples, followed by bounded `L-BFGS-B` `ftol=1e-12, maxiter=5000`).
- **Deterministic Seeds:** Base `SEED = 20261030`. For universe index $u \in \{0, \dots, 44\}$ (in `MOCK_MANIFEST.csv` row order) and chain slot $c \in \{1, \dots, 12\}$, the RNG seed is `SEED + 1000 * (u + 1) + c`.
- **Sampled Parameterization & Priors (`PREREG.md` §§5.1–5.2):**
  - Sampled matter parameter in Stage 2 MCMC is $\Omega_{m,{\rm tot}} \in [0.1, 0.6]$, with baryon+CDM share derived sample-by-sample as $\Omega_{bc} = \Omega_{m,{\rm tot}} - \omega_{\nu,{\rm mass},0}/h^2$ ($\omega_{\nu,{\rm mass},0} = 0.06 / 93.14 = 6.4419154\times 10^{-4}$), $h \in [0.5, 0.9]$, and $100\omega_b \in [1.8, 2.6]$.
  - `LCDM` ($d=3$): $(\Omega_{m,{\rm tot}}, h, 100\omega_b)$, $w_0 = -1, w_a = 0$. `[Established]`
  - `LAW1` ($d=4$): $(\Omega_{m,{\rm tot}}, h, 100\omega_b, \gamma_u)$ with $\gamma_u \in [0.0, 2.0]$, $w(a) = -1 + \gamma_u/E(a)$. `[Model Ansatz]`
  - `CPL` ($d=5$): $(\Omega_{m,{\rm tot}}, h, 100\omega_b, w_0, w_a)$ with $w_0 \in [-3.0, 1.0], w_a \in [-3.0, 2.0]$ and $w_0 + w_a < 0$. `[Established]`
- **Reported Posterior Summaries:** For every parameter ($\Omega_{bc}$, $\Omega_{m,{\rm tot}}$, $h$, $100\omega_b$, and $\gamma_u$ for `Law 1` or $w_0, w_a$ for `CPL`), we report:
  - Posterior `mean ± 1σ` (sample mean and sample standard deviation `ddof=1`),
  - Posterior `95% interval` (`[p2.5, p97.5]`, 2.5th and 97.5th percentiles),
  - Posterior `median ± sigma_68` (`p50` and `0.5 * (p84 - p16)`),
  - Polished $\chi^2_{\min}$ and best-fit parameter vector.

#### 1. Reading B (Frozen Stage 2 Code `scripts/cosmology.py`, Unchanged)
For each SN compilation (`Pantheon+` and `DES-Dovekie`):
- **`T1-L1` & `T1-Sign` Fits (`full_3x3` CMB prior + `joint_ap_deciding` BAO + SN):**
  - Run `Law 1`, `LCDM`, and `CPL` chains using `cosmo.joint_chi2_law1` and `cosmo.joint_chi2_cpl`.
  - **`T1-L1` Statistics & Verdicts (`score_t1_l1_per_run` from `scripts/run_part9_cosmology_tests.py`):**
    - $A_r = \chi^2_{\min}(\text{Law 1}) - \chi^2_{\min}(\Lambda\text{CDM})$, $B_r = \chi^2_{\min}(\text{Law 1}) - \chi^2_{\min}(\text{CPL})$.
    - Per-run verdict: `FAIL` if $B_r > +9.0$ or $A_r > -1.0$; `PASS` if not `FAIL` and $A_r \le -4.0$ and $B_r \le +4.0$; else `INCONCLUSIVE`.
    - Joint `T1-L1` verdict across both SN compilations: `FAIL` if either SN run is `FAIL`; `PASS` if both are `PASS`; else `INCONCLUSIVE` (also reporting $p_{\rm disc,r} = \text{chi2.sf}(\max(0, -A_r), \text{df}=1)$ and $p_{\rm T1\text{-}L1,holm} = \max(p_{\rm disc,P+}, p_{\rm disc,Dov})$).
  - **`T1-Sign` Statistics & Verdicts (`PREREG.md` §5.1):**
    - From the `CPL` chain: $P(w_0 > -1)$ and $P(w_0 < -1) = 1 - P(w_0 > -1)$ (plus Gaussian $z_{w_0 > -1} = (\overline{w}_0 - (-1))/\sigma_{w_0}$).
    - Per-run verdict: `FAIL` if $P(w_0 < -1) \ge 0.95$; `PASS` if $P(w_0 > -1) \ge 0.95$; else `INCONCLUSIVE`.
    - Joint `T1-Sign` verdict: `FAIL` if $P(w_0 < -1) \ge 0.95$ in either SN run; `PASS` if $P(w_0 > -1) \ge 0.95$ in both SN runs; else `INCONCLUSIVE`.
- **`T2-A` Fit & Verdict (`conditional_2x2` CMB prior + `BBN_100omega_b_prior` from `REFERENCES.json` + `joint_ap_deciding` BAO + SN):**
  - Run the registered `T2-A` flat `w0waCDM` (`CPL`) chain (`run_single_t2a_mcmc_worker` protocol from `scripts/run_part8_fixes.py`).
  - Extract $\Omega_{bc,{\rm med}} = p_{50}(\Omega_{bc})$, $\sigma_{\Omega_{bc}} = \frac{1}{2}(p_{84} - p_{16})$, $\mathcal{R}_{\rm pred} = 19\,\Omega_{bc,{\rm med}} - 1$, $\sigma_{\mathcal{R}_{\rm pred}} = 19\,\sigma_{\Omega_{bc}}$, $f_{\rm leak} = 1 - \mathcal{R}_{\rm pred}/6$, and $\sigma_{f_{\rm leak}} = (19/6)\sigma_{\Omega_{bc}}$ (also recording posterior `mean ± 1σ` and `95% interval` `[p2.5, p97.5]`).
  - Compare against `REFERENCES.json["R_omegac_over_omegab"]` ($\mathcal{R}_{\rm ref} \pm \sigma_{\mathcal{R}_{\rm ref}}$):
    $$\sigma_{\rm comb} = \sqrt{\sigma_{\mathcal{R}_{\rm pred}}^2 + \sigma_{\mathcal{R}_{\rm ref}}^2}, \qquad \Delta\mathcal{R} = \mathcal{R}_{\rm pred} - \mathcal{R}_{\rm ref}, \qquad Z_{\rm T2\text{-}A} = \frac{\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm ref}}{\sigma_{\rm comb}}, \qquad |Z_{\rm T2\text{-}A}| = \frac{|\Delta\mathcal{R}|}{\sigma_{\rm comb}}. \quad \text{[Model Ansatz / Established]}$$
  - Per-run verdict: `PASS` if $|Z_{\rm T2\text{-}A}| \le 2.0$, else `FAIL`. Joint `T2-A` verdict: `FAIL` if either SN run has $|Z_{\rm T2\text{-}A}| > 2.0$, else `PASS`. (For completeness, we also record the `Law 1`-chain implied $\mathcal{R}_{\rm pred,Law1} = 19\,\Omega_{bc,{\rm Law1}} - 1$ and its $Z$-score.)
- **`T2-N1` Verdict & Statistic (`PREREG.md` §5.2, using `REFERENCES.json["Omega_b"]`):**
  - Model bare baryon share $\Omega_b^{\rm model} = 1/19 = 0.05263158$ `[Model Ansatz]` vs `REFERENCES.json["Omega_b"]` ($\Omega_{b,{\rm ref}} \pm \sigma_{\Omega_{b,{\rm ref}}}$):
    $$Z_{\rm T2\text{-}N1} = \frac{1/19 - \Omega_{b,{\rm ref}}}{\sigma_{\Omega_{b,{\rm ref}}}}. \quad \text{[Model Ansatz / Established]}$$
  - Verdict: `PASS` if $|Z_{\rm T2\text{-}N1}| \le 2.0$, else `FAIL`.
- **`T2-N2` Verdict & Statistic (`PREREG.md` §5.2, using `REFERENCES.json["100omega_b"]` and `REFERENCES.json["H0"]`):**
  - With $\omega_{b,{\rm ref}} = (\text{100omega\_b.value})/100$ and $\sigma_{\omega_{b,{\rm ref}}} = (\text{100omega\_b.sigma})/100$:
    $$H_0^{\rm pred} = 100\sqrt{19\,\omega_{b,{\rm ref}}}, \qquad \sigma_{H_0^{\rm pred}} = \frac{1}{2}H_0^{\rm pred}\frac{\sigma_{\omega_{b,{\rm ref}}}}{\omega_{b,{\rm ref}}}, \qquad \sigma_{{\rm comb},H_0} = \sqrt{\sigma_{H_0^{\rm pred}}^2 + \sigma_{H_{0,{\rm ref}}}^2}, \qquad Z_{\rm T2\text{-}N2} = \frac{H_0^{\rm pred} - H_{0,{\rm ref}}}{\sigma_{{\rm comb},H_0}}. \quad \text{[Model Ansatz / Established]}$$
  - Verdict: `PASS` if $|Z_{\rm T2\text{-}N2}| \le 2.0$, else `FAIL`.

#### 2. Reading A (Literal `(a5)` Sound Horizon from `head_to_head/h2h_cosmology.py`)
Per `ARGON_PHASE3_HANDOFF.txt` lines 46–47 (`"2. Reading A (the literal (a5) sound horizon from head_to_head/h2h_cosmology.py): the Law 1 fit only, with the T1-Sign and T2-A statistics"`):
- For each SN compilation (`Pantheon+` and `DES-Dovekie`), we run the **`Law 1` MCMC fit + polished $\chi^2_{\min}$** under Reading A (`sound_horizon_rs_a5_gl128` and `r_drag_mpc_a5` from `head_to_head/h2h_cosmology.py`), reporting the posterior `mean ± 1σ`, `median ± sigma_68`, and `95% interval` (`[p2.5, p97.5]`) for $\Omega_{bc}$, $\Omega_{m,{\rm tot}}$, $h$, $100\omega_b$, and $\gamma_u$ (plus implied $w_0 = -1 + \gamma_u$ and $w_a$), and $\chi^2_{\min}(\text{Law 1})$.
- For the **`T1-Sign` and `T2-A` statistics under Reading A**, to ensure zero ambiguity between the two possible readings of lines 46–47 vs. lines 61–63, we compute and report **both**:
  1. **From the Reading A `Law 1` fit directly:**
     - `T2-A` statistic from `Law 1` $\Omega_{bc}$: $\mathcal{R}_{\rm pred,Law1} = 19\,\Omega_{bc,{\rm med}} - 1$, $\sigma_{\mathcal{R}_{\rm pred,Law1}} = 19\,\sigma_{\Omega_{bc}}$, $f_{\rm leak,Law1} = 1 - \mathcal{R}_{\rm pred,Law1}/6$, $\sigma_{\rm comb} = \sqrt{\sigma_{\mathcal{R}_{\rm pred,Law1}}^2 + \sigma_{\mathcal{R}_{\rm ref}}^2}$, and $Z_{\rm T2\text{-}A,Law1} = (\mathcal{R}_{\rm pred,Law1} - \mathcal{R}_{\rm ref})/\sigma_{\rm comb}$ (also reporting the mean/std version $(\overline{\mathcal{R}}_{\rm pred,Law1} - \mathcal{R}_{\rm ref})/\sqrt{(19\,\text{std}(\Omega_{bc}))^2 + \sigma_{\mathcal{R}_{\rm ref}}^2}$).
     - `T1-Sign` statistic from `Law 1`: implied $w_0 = -1 + \gamma_u$, Gaussian significance $z_{\gamma_u > 0} = \overline{\gamma}_u / \sigma_{\gamma_u}$, and $P(\gamma_u > 0)$.
  2. **From the Reading A registered `T1-Sign` (`CPL` `full_3x3`) and `T2-A` (`CPL` `conditional_2x2` + BBN prior) fits (and Reading A `LCDM`):**
     - `T1-Sign` (`CPL` under Reading A): $P(w_0 > -1)$, $P(w_0 < -1)$, $z_{w_0 > -1}$, plus $w_0, w_a, \Omega_{bc}, h, 100\omega_b$ posteriors and $\chi^2_{\min}$.
     - `T2-A` (`conditional_2x2` + BBN prior `CPL` under Reading A): $\Omega_{bc,{\rm med}} \pm \sigma_{\Omega_{bc}}$, $f_{\rm leak}$, $\mathcal{R}_{\rm pred} \pm \sigma_{\mathcal{R}_{\rm pred}}$, $\sigma_{\rm comb}$, and $Z_{\rm T2\text{-}A} = (\mathcal{R}_{\rm pred} - \mathcal{R}_{\rm ref})/\sigma_{\rm comb}$.
     - `LCDM` under Reading A: $\chi^2_{\min}(\Lambda\text{CDM})$ and posteriors, giving $A_r$ and $B_r$ under Reading A as well.

---

### 4.2 Family 2: `GALAXY` (15 Universes; Fixed $f_{\rm leak} = 1/6$)

Per `ARGON_PHASE3_HANDOFF.txt` lines 48–50 and 64–65:
1. **Input & Split (`scripts/sparc_t5.py` Unmodified):**
   - Load `<u_dir>/sparc/SPARC_Lelli2016c.mrt` and `MassModels_Lelli2016c.mrt` via `parse_sparc_catalog(<u_dir> / "sparc")` (`175` galaxies sorted by byte-wise ASCII `gal_id.strip()`: odd 1-based positions = `88` training galaxies; even 1-based positions = `87` held-out test galaxies).
   - Fixed Phase 3 leak fraction: $f_{\rm leak} = 1/6 = 0.16666666666666666$ ($\mathcal{R} = 6(1 - f_{\rm leak}) = 5.0$).
2. **Registered `T5-A` and `T5-B` Training-Half Fits and Test-Half Scoring:**
   - **`T5-A` (Universal Kernel Width $\sigma_{\rm ref} \in [0.1, 100.0]\text{ kpc}$):**
     - Fit $\hat{\sigma}_{\rm ref}$ on the 88 training galaxies minimizing $\mathcal{L}_{\rm train}(\sigma_{\rm ref}) = \sum_{g \in \text{train}} \chi^2_{{\rm red},g}(\sigma_{\rm ref})$ via `fit_sparc_parameter(sparc_train, "T5A", 1.0/6.0, loss_metric="sum_chi2_red")`.
     - Score the 87 held-out test galaxies at $\hat{\sigma}_{\rm ref}$ via `evaluate_sparc_sample(sparc_test, "T5A", sigma_ref_hat, 1.0/6.0)` and `score_t5_subtest`:
       - `PASS`: $M_{\chi^2} \le 1.5$ and $F_{<2} \ge 0.70$,
       - `FAIL`: $M_{\chi^2} > 3.0$ or $F_{<2} < 0.40$,
       - `INCONCLUSIVE`: otherwise.
   - **`T5-B` (Disk-Scaled Width $\sigma_{{\rm ref},g} = k\,R_{d,g}$, $k \in [0.05, 50.0]$):**
     - Fit $\hat{k}$ on the 88 training galaxies via `fit_sparc_parameter(sparc_train, "T5B", 1.0/6.0, loss_metric="sum_chi2_red")`.
     - Score the 87 held-out test galaxies at $\hat{k}$ via `evaluate_sparc_sample(sparc_test, "T5B", k_hat, 1.0/6.0)` and `score_t5_subtest` (same thresholds).
3. **Uncertainty Quantification for Fitted $\sigma_{\rm ref}$ (and $\hat{k}$): `mean ± 1σ` and `95% interval`:**
   - Because `fit_sparc_parameter` in Stage 2 (`scripts/sparc_t5.py`) is a deterministic bounded optimizer returning the point estimate $\hat{\sigma}_{\rm ref}$ (which is used unchanged to score the test half), and `ARGON_PHASE3_HANDOFF.txt` line 64 requests `fitted σ_ref (mean ± 1σ, 95% interval)`, we compute and report the `mean ± 1σ` and `95% interval` (`[p2.5, p97.5]`) on the training half using **three complementary methods** (all recorded in `results.json` and `PHASE3_RESULTS.md`):
     1. **Training-Galaxy Bootstrap ($B = 1000$ replicates, deterministic seed `SEED + 2000 * (u + 1)`):** Resample the 88 training galaxies with replacement $1000$ times and minimize $\sum_{g \in \text{boot}} \chi^2_{{\rm red},g}(\sigma_{\rm ref})$ on a fine 1,000-point log grid + parabolic refinement for each replicate, yielding the bootstrap `mean ± 1σ` (sample std `ddof=1`) and `95% interval` `[p2.5, p97.5]`.
     2. **Profile Likelihood / Posterior under Registered Loss $\mathcal{L}_{\rm train}(\sigma_{\rm ref}) = \sum_{g \in \text{train}} \chi^2_{{\rm red},g}(\sigma_{\rm ref})$:** Evaluate $P(\sigma_{\rm ref}) \propto \exp\!\left[-\frac{1}{2}\left(\mathcal{L}_{\rm train}(\sigma_{\rm ref}) - \mathcal{L}_{{\rm train},\min}\right)\right]$ under the uniform prior $\sigma_{\rm ref} \in [0.1, 100.0]\text{ kpc}$ on a 2,000-point grid refined around $\hat{\sigma}_{\rm ref}$, yielding posterior `mean ± 1σ` and `95% credible interval` `[p2.5, p97.5]`.
     3. **Profile Likelihood / Posterior under Unreduced $\chi^2_{\rm tot,train}(\sigma_{\rm ref}) = \sum_{g \in \text{train}} \chi^2_g(\sigma_{\rm ref})$:** Evaluate $P(\sigma_{\rm ref}) \propto \exp\!\left[-\frac{1}{2}\left(\chi^2_{\rm tot,train}(\sigma_{\rm ref}) - \chi^2_{{\rm tot,train},\min}\right)\right]$, yielding posterior `mean ± 1σ` and `95% credible interval` `[p2.5, p97.5]`.
     (The same three uncertainty summaries are also computed for $\hat{k}$ in `T5-B`.)

---

### 4.3 Family 3: `REGIONAL` (15 Universes)

Per `ARGON_PHASE3_HANDOFF.txt` lines 51 and 66:
1. **Input & Calibrator Fix (`scripts/local_h0_t6.py` Unmodified):**
   - Load `<u_dir>/pantheonplus/Pantheon+SH0ES.dat` and `Pantheon+SH0ES_STAT+SYS.cov` via `load_pantheon_plus_full(<u_dir> / "pantheonplus")`.
   - Fit the SH0ES Cepheid calibrator absolute magnitude $\hat{M}_B^{\rm fixed} \pm \sigma_{M_B^{\rm fixed}}$ (`IS_CALIBRATOR == 1`) via `fit_t6_calibrators`.
2. **Hubble-Flow Regional $H_0$ Fit & Verdict (`evaluate_t6_hubble_flow` Unmodified):**
   - Select Hubble-flow SNe (`0.023 <= zHD <= 0.15`, `IS_CALIBRATOR == 0`), map `(RA, DEC)` to Galactic `(l, b)` and `HEALPix` $N_{\rm side} = 1$ `RING` pixels $\{0, \dots, 11\}$, apply the registered single-pass sparse-pixel merge rule (`SPARSE_MERGE_MAP`, merging $0 < N_{{\rm SN},i} < 10$ and retaining regions with $N_{\rm SN} \ge 10$), and compute the GLS regional estimates $\hat{H}_{0,i} \pm \sigma_{H_{0,i}}$ (both Hubble-flow-only diagonal uncertainty $\sigma_{H_{0,i},{\rm hf}}$ and total uncertainty including $\sigma_{M_B^{\rm fixed}}$), the inverse-covariance weighted mean $\bar{H}_0 \pm \sigma_{\bar{H}_0,{\rm tot}}$, the heterogeneity statistic $\chi^2_{\rm het}$ ($\text{dof} = N_{\rm pix} - 1$), $p_{\rm het} = \text{chi2.sf}(\chi^2_{\rm het}, \text{df} = N_{\rm pix} - 1)$, $Z_{\rm all\text{-}sky}$, and the registered `T6` verdict:
     - `FAIL`: $N_{\rm pix} \ge 2$ and $p_{\rm het} > 0.3173$,
     - `PASS`: $N_{\rm pix} \ge 2$, $p_{\rm het} \le 0.00270$, and $Z_{\rm all\text{-}sky} \ge 3.0$,
     - `INCONCLUSIVE`: otherwise.

---

## 5. Run Order (By Round 1 to 5) and Runtime Projection Rule

Per `ARGON_PHASE3_HANDOFF.txt` lines 53–58:
1. **Run Order by Round:** Universes are executed strictly by **ROUND** (`Round 1`, then `Round 2`, `Round 3`, `Round 4`, `Round 5`), following `MOCKS_FOR_ARGON/MOCK_MANIFEST.csv`:
   - **Round 1 (9 universes):** `U-8TVY` (`GALAXY`), `U-CUIZ` (`COSMO`), `U-I9FZ` (`GALAXY`), `U-IBCC` (`REGIONAL`), `U-J8TH` (`REGIONAL`), `U-LYTB` (`REGIONAL`), `U-UD33` (`GALAXY`), `U-YIG4` (`COSMO`), `U-YNED` (`COSMO`).
   - **Round 2 (9 universes):** `U-44A3` (`COSMO`), `U-8S92` (`GALAXY`), `U-EATJ` (`REGIONAL`), `U-J0R7` (`GALAXY`), `U-JNXP` (`REGIONAL`), `U-LMB5` (`COSMO`), `U-PAKD` (`REGIONAL`), `U-TLZU` (`GALAXY`), `U-Y2N1` (`COSMO`).
   - **Round 3 (9 universes):** `U-07FN` (`GALAXY`), `U-099J` (`COSMO`), `U-278Q` (`GALAXY`), `U-4JZF` (`REGIONAL`), `U-63X5` (`GALAXY`), `U-6VMC` (`REGIONAL`), `U-KPN8` (`COSMO`), `U-SU9K` (`COSMO`), `U-ZJBO` (`REGIONAL`).
   - **Round 4 (9 universes):** `U-2B0Y` (`COSMO`), `U-51CN` (`REGIONAL`), `U-85K4` (`GALAXY`), `U-B485` (`REGIONAL`), `U-BKI0` (`COSMO`), `U-GL5Z` (`COSMO`), `U-LH19` (`REGIONAL`), `U-P0XK` (`GALAXY`), `U-YTKL` (`GALAXY`).
   - **Round 5 (9 universes):** `U-8Z0S` (`GALAXY`), `U-8Z6F` (`COSMO`), `U-J91F` (`COSMO`), `U-KCY8` (`REGIONAL`), `U-KQF9` (`GALAXY`), `U-NBRH` (`REGIONAL`), `U-NPID` (`GALAXY`), `U-OEDW` (`COSMO`), `U-ZY0Y` (`REGIONAL`).
2. **First-Universe Benchmark & Runtime Projection:**
   - Before running the remaining universes of Round 1, we run and time the first universe of each family in Round 1 (`U-8TVY` for `GALAXY`, `U-CUIZ` for `COSMO`, `U-IBCC` for `REGIONAL`), log the measured wall-clock runtime of each family's first universe and the projected 45-universe total runtime in `phase3/ACTIVITY_LOG_PHASE3.md` and `phase3/results.json`.
   - If the projected total runtime is $\le 24\text{ hours}$ (projected total is $\sim 12\text{--}18\text{ minutes}$ across all 45 universes on 12 workers), we execute all 5 rounds (all 45 universes) to completion.
3. **Deliverables & Final Freeze:**
   - Save per-universe JSON logs in `phase3/logs/<universe_id>.json`, master `phase3/results.json`, and `phase3/PHASE3_RESULTS.md` (reporting every universe's required statistics and verdicts, runtime log, and `DEVIATIONS.md` entries, with **no cross-universe summary or interpretation**).
   - Hash every output, every new code file in `phase3/`, `PHASE3_ANALYSIS_PLAN.md`, and `PHASE3_RESULTS.md` into `PHASE3_RESULTS_v1.sha256` and stamp it with OpenTimestamps (`ots stamp`).
