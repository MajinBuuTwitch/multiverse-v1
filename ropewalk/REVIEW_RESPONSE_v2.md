# Response to Independent Follow-Up Review V2 (`REVIEW_V2.md`)

**Date:** 2026-10-30  
**Scope:** Item-by-item response to all findings in `REVIEW_V2.md` (`B1`–`B4`, `N1`–`N10`, the 8 Minor items, the 5 `MAJOR` spot-checks `M1, M6, M10, M11, M12`, and the 6 Film-Note checks).  
**Governing Files Updated:** `PREREG.md` (v3), `MULTIVERSE_STAGE1_EQUATIONS.md` (v3), `ASSUMPTIONS.md` (v3), `STAGE1_PART1_SECTIONS_ABC.md` (v3), `STAGE1_PART2_SECTIONS_DGH.md` (v3), `STAGE1_PART3_SECTIONS_EFI.md` (v3), `verify_b1_kernel_mc.py`, and `PREREG_v3.sha256` (with `PREREG_v3.sha256.ots` and `FREEZE_TIMESTAMP.txt`). Prior v2 copies are preserved intact in `_TRASH/`.

---

## Summary of Resolution Counts

- **Total Items Tracked Across `REVIEW_V2.md`:** 33 (`B1`–`B4` [4], `N1`–`N10` [10], Minor items `m_v2-1` to `m_v2-8` [8], Major spot-checks `M1, M6, M10, M11, M12` [5], Film-Note checks `F1`–`F6` [6])
  - **FIXED:** 31
  - **PARTIAL:** 2 (`N10` and spot-check `M6`, because the 16-cluster `T4b` literature sample was compiled by a human analyst with prior knowledge of famous mergers rather than drawn by a blinded algorithmic selection cut from a uniform survey; this limitation is now stated plainly in `PREREG.md` §5.5 and `ASSUMPTIONS.md` `[A14]`)
  - **DISPUTED:** 0
  - **DEFERRED:** 0

---

## 1. Blockers from Review 1 (`B1`–`B4`)

### `B1` — 3D Gaussian-Smeared Rotation-Curve Kernel Coefficient
- **Status:** **FIXED** (Confirmed in `REVIEW_V2.md` §1)
- **Action Taken:** Confirmed identical in `MULTIVERSE_STAGE1_EQUATIONS.md` `(f3)`, `STAGE1_PART3_SECTIONS_EFI.md` `(f3)`, and `PREREG.md` §5.6. In addition, the two minor follow-ups noted in `REVIEW_V2.md` (the "Old ($\sqrt{2/\pi}$) Value" table column and the $r'/\sigma_{\rm ref} < 10^{-4}$ point-mass limit) are now fixed and the verification script `verify_b1_kernel_mc.py` is saved on disk and hashed in `PREREG_v3.sha256` (see `m_v2-1`, `m_v2-2`, `m_v2-7` below).

### `B2` — Sign Convention of the `T4a` Centroid-Offset Statistic
- **Status:** **FIXED** (Confirmed in `REVIEW_V2.md` §1)
- **Action Taken:** Confirmed identical across `MULTIVERSE_STAGE1_EQUATIONS.md` `(e6)–(e7)`, `STAGE1_PART3_SECTIONS_EFI.md`, and `PREREG.md` §5.4.

### `B3` — `T4a` Promotion Paths, Precedence Clause, Primary Catalog, and Exact `A13b` Formula
- **Status:** **FIXED**
- **Action Taken:** Closed both remaining promotion paths and resolved the minor catalog/formula notes:
  1. **Unconditional Exploratory Lock:** Added the explicit rule in `PREREG.md` §1.2 (Amendment 2), §3.1, and §5.4, and in `MULTIVERSE_STAGE1_EQUATIONS.md` §6 and §8.4: *"`T4a` is unconditionally `EXPLORATORY` (unscored) in v1 regardless of sample size $N$, age cut ($150\text{ Myr}$, $235\text{ Myr}$, or $400\text{ Myr}$), or catalog; it cannot be promoted back to a scored test under any data outcome in v1, and any scored version of `T4a` requires a new pre-registration in a future model version (v2)."*
  2. **Precedence Clause:** Added the binding Precedence Clause (`N3`) to `PREREG.md` §1.1 and all `STAGE1_PART*.md` files so `MULTIVERSE_TESTS_v1.md` cannot be invoked to revive a scored `T4a`.
  3. **Single Primary Exploratory Catalog:** Designated **Wittman, Golovich & Dawson (2018, ApJ 869, 104, Table 1)** as the single primary exploratory catalog for `T4a`, with Harvey et al. (2015) retained only as a secondary cross-check (`PREREG.md` §5.4, `MULTIVERSE_STAGE1_EQUATIONS.md` §6.3).
  4. **Exact `A13b` Harmonic Formula:** Replaced the leading-order Taylor expansion in `MULTIVERSE_STAGE1_EQUATIONS.md` §6.2 `(e9b)` and `STAGE1_PART3_SECTIONS_EFI.md` with the exact closed-form harmonic oscillator trajectory before evaluating the small-$\omega_0\tau_{\rm lag}$ series as an illustrative limit.

### `B4` — `T1-L1` Full Dark-Energy Curve Registration & Model $w_0$ Definition
- **Status:** **FIXED** (Confirmed in `REVIEW_V2.md` §1, with `N5` follow-ups resolved)
- **Action Taken:** In `PREREG.md` §5.1 and `MULTIVERSE_STAGE1_EQUATIONS.md` §5.2, we clarified explicitly that $w_0 = -0.84$ was an illustrative evaluation at DESI's CPL central value, whereas when `T1-L1` is fitted to the data, **the model's own present-day equation of state is fixed by the single fitted leakage parameter $\hat{\gamma}_u$ via $w_0^{\rm fit} = w_{\rm eff}(1;\hat{\gamma}_u,\hat{\Omega}_m) = -1 + \hat{\gamma}_u$** (with implied present-day slope $w_a^{\rm fit} = (1 + w_0^{\rm fit})\,\tfrac{3}{2}\hat{\Omega}_m / [1 - \tfrac{1}{2}\hat{\Omega}_m(1 + w_0^{\rm fit})]$). A Gaussian-posterior forecast places the best-fit Law 1 curve near $w_0^{\rm fit} \approx -0.90$ to $-0.93$ (tangent $w_a^{\rm fit} \approx -0.04$ to $-0.06$). All `N5` decision-map and forecast corrections are also applied (see `N5` below).

---

## 2. New Blockers and Majors in `REVIEW_V2.md` (`N1`–`N10`)

### `N1` — Unresolved Forks in `T2` (Pillar 2) and Frozen $f_{\rm leak}$ for `T5`
- **Status:** **FIXED**
- **Action Taken:** Eliminated every fork in `PREREG.md` §1.2, §3.1, §5.2, and §5.6, and in `MULTIVERSE_STAGE1_EQUATIONS.md` §4.2 and §8.2:
  1. **Single Deciding `T2` Version (`N1a`):** **`T2-A`** (fixing $\hat{\Omega}_{bc}$ on `DESI DR2 BAO + SN + CMB (R, l_A | omega_b)` and comparing $R_{\rm pred} = 19\hat{\Omega}_{bc} - 1$ against $R_{\rm Planck}$) is the **sole deciding version** of Pillar 2. **`T2-B`** (jointly fitting $\Omega_b = 1/19$ and $\Omega_{bc}$ without an external $R_{\rm Planck}$ pull) is demoted to a non-deciding **Sensitivity Analysis**.
  2. **Single Deciding Error Formula (`N1b`):** The **uncorrelated combination $\sigma_{\rm comb} = \sqrt{(19\sigma_{\Omega_{bc}})^2 + \sigma_{R,\text{Planck}}^2}$** (with $\sigma_{R,\text{Planck}} = 0.065$) is the **sole deciding error formula** for `T2-A`. The unsourced approximate $\rho_{\rm overlap} \approx +0.35$ is dropped from the decision path.
  3. **Single Deciding BBN Prior (`N1c` & `N7`):** The **DESI DR2 / post-LUNA BBN prior ($100\omega_b = 2.218 \pm 0.055$, DESI Collaboration 2025 Eq. 14 / Schöneberg 2024)** is the **sole deciding BBN prior** for `T2-A` (avoiding the $+3.1\sigma_R$ conditional shift caused by the older Cooke et al. 2018 value). The Cooke et al. (2018) prior ($100\omega_b = 2.166 \pm 0.019$) is relegated to a non-deciding sensitivity check.
  4. **Complete `T2-B` Fail Rule (`N1d`):** Added the explicit condition $\Delta\chi^2_{\min}(\text{T2-B} - w_0w_a\text{CDM}) > 9.0$ directly into the `T2-B` sensitivity `FAIL` rule in `PREREG.md` §5.2 and `MULTIVERSE_STAGE1_EQUATIONS.md` §8.2 so no case falls through.
  5. **Original v1 Dual-Run FAIL Rule Restored & Declared (`N1` / `N3`):** Restored the original `MULTIVERSE_TESTS_v1.md` dual-run rule for `T2-A` (**`FAIL` if $|R_{\rm pred} - R_{\rm Planck}| > 2\sigma_{\rm comb}$ in *either* the `Pantheon+` or `DES-Dovekie` run; `PASS` if $\le 2\sigma_{\rm comb}$ in *both* runs**, creating an exhaustive 2-state `PASS`/`FAIL` partition with no `INCONCLUSIVE` state for `T2-A`) and declared this openly in `PREREG.md` §1.2 (Amendment 3).
  6. **Single Frozen $f_{\rm leak}$ Input for `T5` (`N1`):** Specified in `PREREG.md` §5.2 and §5.6 that `T5` uses $f_{\rm leak} = 1 - 1/(1 + R_{\rm pred})$ frozen exclusively from **`T2-A-Pantheon+` (with the DESI/LUNA BBN prior $100\omega_b = 2.218 \pm 0.055$)**.

### `N2` — Unresolved Forks in `T4b` (Pillar 3)
- **Status:** **FIXED**
- **Action Taken:** Picked one single deciding choice for every fork in `PREREG.md` §5.5 and `MULTIVERSE_STAGE1_EQUATIONS.md` §6.5 and §8.5:
  1. **Single $\tau_{\rm lag}$ Grid Floor (`N2a` & `N8`):** Fixed the search grid to **$\tau_{\rm lag} \in [235, 1500]\text{ Myr}$ in steps of $5\text{ Myr}$**, where **$235\text{ Myr}$** is the one-sided 95% lower confidence bound ($0.40 - 1.645 \times 0.10 = 0.235\text{ Gyr}$) of the Dawson (2013, Table 2) temporal-prior posterior for the Bullet Cluster. Updated `FAIL` clause (a) to require $\tau_{\rm lag} \ge 235\text{ Myr}$.
  2. **Single Bullet Cluster Age (`N2b`):** Fixed the Bullet Cluster age to **Dawson (2013, Table 2) temporal-prior median $t_p = 0.40\text{ Gyr}$ ($\sigma_{t_p} = 0.10\text{ Gyr}$)**. The Markevitch (2006) $0.15\text{ Gyr}$ bow-shock estimate is dropped from the decision path.
  3. **Single Scoring Method (`N2c`):** **Hard-step classification accuracy** $\text{Acc}(\tau_{\rm lag})$ against point-estimate ages $t_{p,i}$ is the **sole deciding score** compared against the $\ge 80\%$ `PASS` and $< 60\%$ `FAIL` thresholds. Age-posterior-weighted accuracy is relegated to a non-deciding sensitivity check.
  4. **Single Classification Level & `FAIL (c)` Scope (`N2d`):** **Primary high-Mach ("bullet") subcluster classification** is the **sole deciding classification level** (system-level classification is a non-deciding sensitivity check), and `FAIL` clause (c) (*"predicts the same state for every cluster in the test half"*) is evaluated explicitly on the **$N_{\rm test} = 8$ test half**.

### `N3` — Precedence Clause, Stale Rules in Hashed Part Files, and Table of Deliberate Amendments
- **Status:** **FIXED**
- **Action Taken:**
  1. Added the binding **Precedence Clause** to `PREREG.md` §1.1, `MULTIVERSE_STAGE1_EQUATIONS.md` Header, `ASSUMPTIONS.md` Header, and all three intermediate part files (`STAGE1_PART1_SECTIONS_ABC.md`, `STAGE1_PART2_SECTIONS_DGH.md`, `STAGE1_PART3_SECTIONS_EFI.md`): *"Where `PREREG.md` and any earlier or companion file disagree, `PREREG.md` governs for all test definitions, thresholds, priors, datasets, and decision rules, and `MULTIVERSE_STAGE1_EQUATIONS.md` governs for all equations. `MULTIVERSE_TESTS_v1.md`, `GEMINI.md`, and all `STAGE1_PART*.md` derivation files are superseded for every test they share with `PREREG.md`."*
  2. Added a numbered **Table of Deliberate Amendments to `MULTIVERSE_TESTS_v1.md`** in `PREREG.md` §1.2 documenting every revision from v1 (`T1` $\to$ `T1-L1` primary + `T1-Sign` secondary; `T4a` unconditionally `EXPLORATORY`; `T2` split into deciding `T2-A` with restored v1 "either SN run" FAIL rule + secondary `T2-N1`/`T2-N2` + sensitivity `T2-B`; `T4b` Dawson 2013 age and $235\text{ Myr}$ floor; `T5` corrected $\mathcal{F}_\sigma$ kernel and `T5-A` primary; `T6` 48-pixel `HEALPix` $N_{\rm side}=2$ map).
  3. Removed stale Rule 9 (old `G8` escape hatch), Rule 16, Rule 18, and Rule 22 from `STAGE1_PART1_SECTIONS_ABC.md` and replaced the stale 12-pixel / $\text{dof}=11$ text in `STAGE1_PART2_SECTIONS_DGH.md` `(g4)` with the 48-pixel (`HEALPix` $N_{\rm side}=2$, $\text{dof}=47$) specification.

### `N4` — External Timestamp (`M12` Gate)
- **Status:** **FIXED**
- **Action Taken:** Installed `opentimestamps-client` (`0.8.0`) in `.venv`, hashed all 20 Stage 1 and starter files (plus a chaining reference to `_TRASH/PREREG_v1.sha256` and `_TRASH/PREREG_v2.sha256`) into `PREREG_v3.sha256`, ran `ots stamp PREREG_v3.sha256` to submit the SHA-256 digest to public OpenTimestamps calendar servers and generate the cryptographic proof file `PREREG_v3.sha256.ots` alongside `PREREG_v3.sha256`, and recorded the timestamp details in an unhashed `FREEZE_TIMESTAMP.txt`. Gregory can also send `PREREG_v3.sha256` and `PREREG_v3.sha256.ots` directly to the reviewer before Part 4 begins.

### `N5` — `T1-L1` Decision Map, Optimizer, Swapped SN Labels, Forecast, and Non-Nested $\Delta\chi^2$ Note
- **Status:** **FIXED**
- **Action Taken:** Updated `PREREG.md` §5.1 and `MULTIVERSE_STAGE1_EQUATIONS.md` §5.2 and §8.1:
  1. **Gap-Free, Overlap-Free Decision Rule (`N5a`):** Specified per-run evaluation where **`FAIL` takes strict precedence** ($\Delta\chi^2_{\min}(\text{L1} - w_0w_a\text{CDM}) > 9.0$ OR $\Delta\chi^2_{\min}(\text{L1} - \Lambda\text{CDM}) > -1.0$), **`PASS` requires both** $\Delta\chi^2_{\min}(\text{L1} - \Lambda\text{CDM}) \le -4.0$ AND $\Delta\chi^2_{\min}(\text{L1} - w_0w_a\text{CDM}) \le +4.0$, and **every per-run outcome not `PASS` or `FAIL` is `INCONCLUSIVE`**. Across the two SN runs: joint `FAIL` if *either* run is `FAIL`; joint `PASS` if *both* runs are `PASS` (and survive Holm–Bonferroni); joint `INCONCLUSIVE` otherwise. Registered the two-stage optimizer (`50 x 50` grid search followed by `scipy.optimize.minimize(..., method="L-BFGS-B", tol=1e-10)` restarted from the 5 best grid nodes).
  2. **Corrected Published Numbers (`N5b`):** Fixed the swapped supernova labels and Dovekie $w_0$ value: `DESI DR2 + CMB + Pantheon+` gives $w_0 = -0.838 \pm 0.055$, $w_a = -0.62^{+0.22}_{-0.19}$ (DESI Collaboration 2025, arXiv:2503.14738, Table V), `DESI DR2 + CMB + DES-Dovekie` gives $w_0 = -0.803 \pm 0.054$, $w_a = -0.72 \pm 0.21$ ($z = (+0.197)/0.054 = 3.65\sigma$ for `T1-Sign`, Popovic et al. 2025, arXiv:2511.07517v2, Tables 10–11), and the original uncorrected `DESY5` gave $w_a \approx -0.86 \pm 0.25$.
  3. **Corrected Forecast (`N5c`):** Updated the `T1-L1` forecast in `PREREG.md` §3.2 and §5.1, `MULTIVERSE_STAGE1_EQUATIONS.md` §5.2, and the film note to state that $\Delta\chi^2_{\min}(\text{L1} - w_0w_a\text{CDM})$ is forecast to land around $\approx 7\text{–}8$ (`Pantheon+`, `INCONCLUSIVE` band) and $\approx 9\text{–}10$ (`DES-Dovekie`, borderline `INCONCLUSIVE`/`FAIL`), making the joint `T1-L1` forecast **`FAIL` or `INCONCLUSIVE` (most likely `INCONCLUSIVE`)**.
  4. **Dropped Non-Nested "$3\sigma$" Gloss (`N5d`):** Noted explicitly that Law 1 is not nested in $w_0w_a\text{CDM}$ and dropped the "$\Delta\text{dof}=1, 3\sigma$" likelihood-ratio gloss on the mechanical $+9.0$ threshold.

### `N6` — Operationalizing Holm–Bonferroni and the 3-Way Model-Level Verdict
- **Status:** **FIXED**
- **Action Taken:** Updated `PREREG.md` §3.2 and `MULTIVERSE_STAGE1_EQUATIONS.md` §8.8:
  1. **Mechanical $p$-Value Defined for Every Scored Test:** Defined an explicit mechanical one-sided or two-sided $p$-value $p_k$ for all $K = 9$ scored tests (`T1-L1` via Wilks $\Delta\chi^2_{\min}(\text{L1}-\Lambda\text{CDM})$ survival function $1 - F_{\chi^2_1}(|\Delta\chi^2_{\min}|)$ on the more conservative SN run; `T1-Sign` via one-sided normal $1 - \Phi(z_{\min})$; `T2-A`, `T2-N1`, `T2-N2` via two-sided normal $2[1 - \Phi(|z|)]$; `T4b` via exact one-sided binomial tail $\sum_{j=k_{\rm pass}}^{8} \binom{8}{j} 0.5^8$ on the $N_{\rm test}=8$ test half; `T5-A` via one-sided binomial tail against null galaxy pass rate $p_0 = 0.50$; `T5c` via one-sided normal survival function at $r = 3.1\text{ kpc}$; `T6` via $\max(p_{\rm het}, 2[1-\Phi(Z_{\rm all-sky})])$).
  2. **Status of a Raw `PASS` Failing Holm–Bonferroni:** Stated explicitly that **any test achieving a raw `PASS` whose $p$-value fails the Holm–Bonferroni step-down threshold at family-wise $\alpha = 0.05$ is downgraded to `INCONCLUSIVE` (never `PASS`)**.
  3. **Exhaustive 3-Way Model-Level Verdict:** Defined the complete 3-state partition across the 4 primary pillars (`T1-L1`, `T2-A`, `T4b`, `T5-A`):
     - **`MODEL FALSIFIED (v1 REJECTED)`:** At least one primary pillar ends in `FAIL`.
     - **`MODEL SUPPORTED (v1 CORROBORATED)`:** All 4 primary pillars end in `PASS` (after Holm–Bonferroni).
     - **`MODEL INCONCLUSIVE (NOT FALSIFIED, NOT SUPPORTED)`:** Zero primary pillars end in `FAIL`, and at least one primary pillar ends in `INCONCLUSIVE`.

### `N7` — BBN Prior Pull on Conditional $(R, \ell_A \mid \omega_b)$ in `T2` (`M9` Follow-Up)
- **Status:** **FIXED**
- **Action Taken:** Made the **DESI DR2 / post-LUNA BBN prior ($100\omega_b = 2.218 \pm 0.055$)** the **single deciding BBN prior** for `T2-A` (and for freezing $f_{\rm leak}$ in `T5`), and relegated Cooke et al. (2018, $100\omega_b = 2.166 \pm 0.019$) to a non-deciding sensitivity check (`PREREG.md` §5.2, `MULTIVERSE_STAGE1_EQUATIONS.md` §4.2). Documented explicitly why: conditioning the Planck $(R, \ell_A, 100\omega_b)$ covariance on Cooke's $100\omega_b = 2.166$ pulls the conditional $R$ mean by $(C_{13}/C_{33})(-0.070) \approx +0.014$ ($+3.1\sigma_R$), introducing a $3\sigma$ BBN–CMB prior conflict into `T2-A`, whereas the DESI/LUNA BBN value ($2.218 \pm 0.055$) is consistent with Planck ($2.237 \pm 0.015$) to $0.33\sigma$.

### `N8` — Framing of the Bullet Cluster Age Distribution and $\tau_{\rm lag}$ Floor (`M6` Follow-Up)
- **Status:** **FIXED**
- **Action Taken:** Stopped calling $400\text{ Myr}$ a lower bound everywhere in `PREREG.md` (§5.4, §5.5), `MULTIVERSE_STAGE1_EQUATIONS.md` (§6.1, §6.5), `ASSUMPTIONS.md` (`[A13]`, `[A14]`), `STAGE1_PART3_SECTIONS_EFI.md`, and the Film Note. Stated accurately that Dawson (2013, Table 2) gives a posterior distribution with median $0.40\text{ Gyr}$, 68% interval $0.30\text{–}0.50\text{ Gyr}$, and 95% interval $0.20\text{–}0.60\text{ Gyr}$ under the temporal prior (and median $0.60\text{ Gyr}$, 68% interval $0.30\text{–}1.10\text{ Gyr}$ under the default prior). Registered the `T4b` grid floor as the **one-sided 95% lower confidence bound of the Dawson temporal-prior posterior ($\tau_{\rm lag,\min} = 235\text{ Myr}$)** and dropped the $0.15\text{ Gyr}$ shock estimate from the decision path (`Dawson 2013` §3.2.2; `Springel & Farrar 2007`).

### `N9` — Forks and Unsourced Numbers in Scored Secondary Tests (`T5-B`, `T6`, `T2-N2`)
- **Status:** **FIXED**
- **Action Taken:** Resolved every fork across `T5-B`, `T6`, and `T2-N2`:
  1. **`T5-B` (`PREREG.md` §3.1, §5.6; `MULTIVERSE_STAGE1_EQUATIONS.md` §8.6):** Dropped the misnamed "Bonferroni on $\chi^2$ cut-offs" ($1.35 / 75\%$), locked `T5-B` to use the exact same $1.5 / 70\%$ thresholds as `T5-A`, and removed `T5-B` from the scored $K$-test Holm–Bonferroni family so `T5-A` is the sole scored galaxy rotation-curve test (making $K = 9$ total scored tests: 4 primary pillars + 5 secondary tests). `T5-B` is reported as a diagnostic sensitivity test of the single-parameter $\sigma_{\rm size}$ fit.
  2. **`T6` (`PREREG.md` §3.1, §5.7; `MULTIVERSE_STAGE1_EQUATIONS.md` §4.3, §8.7):** Locked a **single deciding configuration**: **Galactic $(l, b)$ `RING` coordinates, $z_{\rm HD}$ (CMB+peculiar-velocity corrected) redshifts, and the bare Pantheon+ Hubble-flow covariance $\mathbf{C}_{H_0}$** (dropping the unsourced $\sigma_{\rm CV,reg} = 0.013\bar{H}_0$ diagonal floor to a sensitivity check, alongside Equatorial coordinates and $z_{\rm CMB}$). Defined an exhaustive, gap-free 3-way partition: **`FAIL`** if $p_{\rm het} > 0.3173$ (regardless of $Z_{\rm all-sky}$); **`PASS`** if $p_{\rm het} \le 0.00270$ AND $Z_{\rm all-sky} \ge 3.0$ (and survives Holm–Bonferroni); **`INCONCLUSIVE`** otherwise.
  3. **`T2-N2` (`PREREG.md` §3.1, §5.2; `MULTIVERSE_STAGE1_EQUATIONS.md` §3.4, §8.2):** Locked a **single deciding comparison**: **Planck 2018 $100\omega_b = 2.237 \pm 0.015 \implies H_0^{\rm pred} = 65.19 \pm 0.22\text{ km s}^{-1}\text{ Mpc}^{-1}$ tested against Planck 2018 $\Lambda\text{CDM}$ $H_0 = 67.36 \pm 0.54\text{ km s}^{-1}\text{ Mpc}^{-1}$** ($z = -3.72\sigma$, pre-test forecast `FAIL`). Relegated SH0ES ($73.04 \pm 1.04$, $-7.38\sigma$), DESI+LUNA BBN ($H_0^{\rm pred} = 64.91 \pm 0.80$, $-2.54\sigma$ vs. Planck), and Cooke+18 BBN ($H_0^{\rm pred} = 64.15 \pm 0.28$, $-5.28\sigma$ vs. Planck and $-6.75\sigma$ vs. DESI+BBN $H_0 = 68.52 \pm 0.62$) to non-deciding sensitivity checks with corrected $\sigma$ values.

### `N10` — Hand-Selected 16-Cluster Sample in `T4b` (`M6(a)` Follow-Up)
- **Status:** **PARTIAL**
- **Action Taken:** Because no single uniform all-sky weak-lensing + X-ray catalog with homogeneous MCMAC dynamical ages exists in the published literature from which the 16 clusters could be drawn by a purely mechanical flux/mass cut, we state this limitation plainly and honestly in `PREREG.md` §5.5 (under *"Known Sample-Selection Limitation (`N10` / `M6a` Disclosure)"*), `ASSUMPTIONS.md` `[A14]`, and `MULTIVERSE_STAGE1_EQUATIONS.md` §6.5: **the 16 `T4b` cluster systems were compiled from the literature by a human analyst with prior knowledge of well-known dissociation and non-dissociation systems, so `T4b` is subject to literature selection bias even under the deterministic ASCII-sorted train/test split.** In accordance with instruction 4 and instruction 5, both `N10` and spot-check `M6` are marked **`PARTIAL`** rather than `FIXED`.

---

## 3. Minor Findings in `REVIEW_V2.md` (`m_v2-1` to `m_v2-8`)

### `m_v2-1` — "Old ($\sqrt{2/\pi}$) Value" Column in the `B1` Verification Table
- **Status:** **FIXED**
- **Action Taken:** Recomputed the exact values of the old buggy formula (`sqrt(2/pi)` prefactor with `-` sign) in `verify_b1_kernel_mc.py` and updated the `"Old (sqrt(2/pi)) Value"` column in `MULTIVERSE_STAGE1_EQUATIONS.md` §7.2, `STAGE1_PART3_SECTIONS_EFI.md` §1.2, and `PREREG.md` §5.6 to `-0.212653`, `-0.071614`, `-0.051392`, and `+0.083317`, matching the reviewer's exact numbers.

### `m_v2-2` — Divide-by-Zero in $\mathcal{F}_\sigma(r, r')$ at $r' = 0$
- **Status:** **FIXED**
- **Action Taken:** Added the explicit analytical point-mass limit branch for $r'/\sigma_{\rm ref} < 10^{-4}$ (including $r' = 0$, the first node of the 500-point quadrature grid) in `MULTIVERSE_STAGE1_EQUATIONS.md` `(f3b)`, `STAGE1_PART3_SECTIONS_EFI.md` `(f3b)`, `PREREG.md` §5.6, and `verify_b1_kernel_mc.py`:
  $$\mathcal{F}_\sigma(r, r'\to 0) = \operatorname{erf}\!\left(\frac{r}{\sqrt{2}\,\sigma_{\rm ref}}\right) - \sqrt{\frac{2}{\pi}}\,\frac{r}{\sigma_{\rm ref}}\,\exp\!\left(-\frac{r^2}{2\sigma_{\rm ref}^2}\right).$$

### `m_v2-3` — Premise of the Saturation Cap Theorem and Effect of $M_b^{\rm mono}$ Clipping
- **Status:** **FIXED**
- **Action Taken:** Stated the exact mathematical premise and caveat of the saturation cap in `MULTIVERSE_STAGE1_EQUATIONS.md` §7.3 `(f7a)`, `STAGE1_PART3_SECTIONS_EFI.md` `(f7a)`, `PREREG.md` §5.6, and `ASSUMPTIONS.md` `[A15]`: (i) the layer-cake convolution bound $M_{\rm sh}(r) \le R\,M_b^{\rm mono}(r)$ holds globally for any non-negative shell mass distribution $dM_b^{\rm mono} \ge 0$ and reaches equality only as $r/\sigma_{\rm ref} \to \infty$; (ii) the stronger statement that $M_{\rm sh}(r)/[R\,M_b^{\rm mono}(r)]$ increases monotonically with $r$ requires an outward-decreasing spherical density profile $\rho_b(r)$, whereas inside an annular gas ring $M_{\rm sh}(r)/[R\,M_b(r)]$ can locally exceed $1$ even though $M_{\rm sh}(r) \le R\,M_b^{\rm mono}(\infty)$ remains bounded globally; and (iii) in radii where monotonicity clipping $M_b^{\rm mono}(r) > M_b^{\rm raw}(r)$ is active (negative raw $v_{\rm gas}|v_{\rm gas}|$), $g_{\rm obs}(r)/g_{\rm bar}^{\rm raw}(r)$ can locally exceed $1 + R$ because $g_{\rm bar}^{\rm raw}$ uses unclipped $v_{\rm bar}^2$.

### `m_v2-4` — `T5c` (NGC 1052–DF2) $\sigma_{\rm ref}$ Parentheticals and Group Peak Mass
- **Status:** **FIXED**
- **Action Taken:** Updated `MULTIVERSE_STAGE1_EQUATIONS.md` §7.6 and §8.6, `STAGE1_PART3_SECTIONS_EFI.md` §1.6, and `PREREG.md` §3.1 and §5.6 so the parentheticals match the corrected `B1` kernel at $R_{\rm cosmic} = 5.0$: `PASS` requires $\sigma_{\rm ref} \gtrsim 2.2\text{ kpc}$ (where the $r = 3.1\text{ kpc}$ limit $M_{\rm sh} \le 1.2\times 10^8\,M_\odot$ binds; the $r = 2.7\text{ kpc}$ limit requires $\sigma_{\rm ref} \ge 1.9\text{ kpc}$), `FAIL` occurs for $\sigma_{\rm ref} < 1.4\text{ kpc}$ ($M_{\rm sh}(3.1\text{ kpc}) > 2.8\times 10^8\,M_\odot$), and the external NGC 1052 group tidal-stripping term peaks at $M_{\rm sh}^{\rm group}(3.1\text{ kpc}) \approx 4.9\times 10^6\,M_\odot$ at $\sigma_{\rm ref} \approx d_{\rm sep} = 80\text{ kpc}$.

### `m_v2-5` — `T2-A` Forecast Tension ($3.8\sigma$ / $3.9\sigma$)
- **Status:** **FIXED**
- **Action Taken:** Updated the `T2-A` pre-test forecast in `PREREG.md` §3.2 and §5.2, `MULTIVERSE_STAGE1_EQUATIONS.md` §4.2, and the Film Note from $3.5\text{–}3.6\sigma$ to **$3.8\sigma$ (`Pantheon+`, $R_{\rm pred} \approx 4.89$) and $3.9\sigma$ (`DES-Dovekie`, $R_{\rm pred} \approx 4.92$)** with $\Omega_\nu$ excluded from $\Omega_{bc}$.

### `m_v2-6` — `A13b` Exact Harmonic Oscillator Formula vs. Taylor Approximation
- **Status:** **FIXED**
- **Action Taken:** Registered the exact harmonic oscillator solution in `MULTIVERSE_STAGE1_EQUATIONS.md` §6.2 `(e9b)` and `STAGE1_PART3_SECTIONS_EFI.md` `(e9b)` and noted that while the leading Taylor series overstates the amplitude by $\sim 2\times$ at $\omega_0\tau_{\rm lag} \approx 4$, the sign switch near $T_{\rm in} \approx \tfrac{2}{3}\tau_{\rm lag}$ survives in the exact expression.

### `m_v2-7` — Saving and Hashing the `B1` Monte Carlo Verification Script
- **Status:** **FIXED**
- **Action Taken:** Saved the standalone verification script `D:\Argon_Code\Ropewalk\verify_b1_kernel_mc.py` (with the required single-thread BLAS headers, the $r'/\sigma_{\rm ref} < 10^{-4}$ point-mass branch, the 4-point MC verification table, and the `G9-d` $5\times 5$ `scipy.stats.ncx2.cdf` cross-check) and included `verify_b1_kernel_mc.py` in `PREREG_v3.sha256`.

### `m_v2-8` — `ACTIVITY_LOG.md` Interleaved Timestamps and Hashed Prefix Verification
- **Status:** **FIXED**
- **Action Taken:** Noted in `PREREG_v3.sha256` and `FREEZE_TIMESTAMP.txt` that `ACTIVITY_LOG.md` is append-only under `GEMINI.md` Rule 1 and Rule 4, so future integrity checks verify the Stage 1 freeze by matching the exact byte-length and SHA-256 of the frozen prefix recorded at the end of Stage 1.

---

## 4. `MAJOR` Spot-Checks from Section 3 of `REVIEW_V2.md`

### Spot-Check `M1` — `T2` FIX/TEST Parameter-Sharing Disclosure & Error Formula
- **Status:** **FIXED**
- **Action Taken:** Resolved the remaining `N1` fork by locking the uncorrelated $\sigma_{\rm comb} = \sqrt{(19\sigma_{\Omega_{bc}})^2 + 0.065^2}$ as the sole deciding error formula for `T2-A`, dropping the unsourced $\rho_{\rm overlap} = 0.35$, locking the DESI/LUNA BBN prior ($100\omega_b = 2.218 \pm 0.055$), and relegating `T2-B` to a sensitivity check.

### Spot-Check `M6` — Bullet Cluster Age, $\tau_{\rm lag}$ Bound Framing, and Sample Selection Rule
- **Status:** **PARTIAL**
- **Action Taken:** Fixed the `N8` framing of the Dawson (2013) posterior (median $0.40\text{ Gyr}$, 95% range $0.20\text{–}0.60\text{ Gyr}$, one-sided 95% lower bound $\tau_{\rm lag,\min} = 235\text{ Myr}$) and dropped the $0.15\text{ Gyr}$ shock age from the decision path (`N2`). Marked **`PARTIAL`** (rather than `FIXED`) because the 16 `T4b` cluster systems were compiled from the literature by a human analyst with prior knowledge of famous mergers rather than selected by a blinded mechanical rule (`N10`), which is now disclosed explicitly in `PREREG.md` §5.5.

### Spot-Check `M10` — Model-Level Decision Rule, Operational Holm–Bonferroni, and Stale `G8` Removal
- **Status:** **FIXED**
- **Action Taken:** Operationalized Holm–Bonferroni with mechanical $p$-values for all $K = 9$ scored tests (`N6`), specified that a raw `PASS` failing Holm–Bonferroni becomes `INCONCLUSIVE`, added the third model-level verdict (`MODEL INCONCLUSIVE (NOT FALSIFIED, NOT SUPPORTED)`), restored and declared the v1 "either SN run" FAIL rule for `T2-A`, and purged the old `G8` escape hatch from `STAGE1_PART1_SECTIONS_ABC.md` (`N3`).

### Spot-Check `M11` — Single Governing File and Precedence Clause
- **Status:** **FIXED**
- **Action Taken:** Added the explicit Precedence Clause (`N3`) to `PREREG.md` §1.1, `MULTIVERSE_STAGE1_EQUATIONS.md`, `ASSUMPTIONS.md`, and all `STAGE1_PART*.md` files, and synchronized all stale rules in `STAGE1_PART1/2/3`.

### Spot-Check `M12` — Complete Manifest Chaining and External Timestamping
- **Status:** **FIXED**
- **Action Taken:** Generated `PREREG_v3.sha256` covering all 20 Stage 1 and starter files (including `REVIEW_V2.md`, `REVIEW_RESPONSE_v2.md`, `verify_b1_kernel_mc.py`, and `ACTIVITY_LOG.md`), included the SHA-256 digests of `_TRASH/PREREG_v1.sha256` and `_TRASH/PREREG_v2.sha256` to chain all three manifests cryptographically, and stamped `PREREG_v3.sha256` via OpenTimestamps (`PREREG_v3.sha256.ots` + `FREEZE_TIMESTAMP.txt`).

---

## 5. Film-Note Checks from Section 4 of `REVIEW_V2.md` (`F1`–`F6`)

- **`F1` (Bullet Cluster age phrasing):** **FIXED** — Rewritten to state that the Bullet Cluster collision happened *"likely around 400 million years ago, and almost certainly more than 200 million years ago"* (with the 235-million-year 95% lower confidence floor used for the lag grid).
- **`F2` (`T4a` exploratory reason):** **FIXED** — Updated to state that `T4a` is locked as exploratory in version 1 both because the idealized harmonic-spring formula breaks down over long post-collision timescales and because any scored offset test requires a dedicated pre-registration in version 2.
- **`F3` ($\Omega_b = 1/19$ tension, $H_0 \approx 65.2$, and `T2-A` forecast at $3.8\text{–}3.9\sigma$):** **FIXED** — Explicitly stated in the rewritten Film Note.
- **`F4` (`T1-L1` forecast is `FAIL` or `INCONCLUSIVE`):** **FIXED** — Updated from a flat forecast fail to *"disfavoured: forecast to end in FAIL or INCONCLUSIVE (most likely INCONCLUSIVE)"*.
- **`F5` (SPARC dwarfs reach about 10–20:1):** **FIXED** — Updated from "10-to-1 to 30-to-1" to *"about 10-to-1 to 20-to-1"*.
- **`F6` ("Three registered pillar tests" with forecasts & DF2 blur threshold ~2.2 kpc):** **FIXED** — Updated to refer accurately to the **three registered pillar tests that have pre-test forecasts** (`T1-L1`, `T2-A`, `T5-A`, alongside the fourth cluster-cutoff pillar `T4b` whose outcome must wait for the data split), and updated the DF2 blur threshold to *"wider than about 2.2 kiloparsecs"*.

---

## WHAT CHANGES FOR THE FILM

1. **The Bullet Cluster age and the shadow-reconnection clock:** In the primary weak-lensing dynamical model for the Bullet Cluster (Dawson 2013), the collision happened **likely around 400 million years ago, and almost certainly more than 200 million years ago** (with a 95 percent lower confidence bound of about 235 million years, rather than the older 150-million-year bow-shock estimate). Because the Bullet Cluster still shows strong dark-matter separation today, the model's shadow-matter reconnection clock must be slower than at least 235 million years, and most likely slower than 400 million years.
2. **The early-collision offset test (`T4a`) is exploratory only:** With a reconnection clock that long, the simple spring approximation used for early collisions is stretched past its clean linear regime, and the early-offset test (`T4a`) is locked as an unscored exploratory check in version 1. Interestingly, the corrected math predicts that during the first two-thirds of the reconnection window, the gravitational shadow actually **trails** behind the normal stars before slingshotting ahead of them—the exact opposite of the original v1 equation sheet.
3. **The 1-in-19 baryon fraction is already in ~3.9-sigma tension with Planck and predicts $H_0 \approx 65.2$:** Before running any new combined fit, the model's core structural number—that ordinary matter is exactly 1 part in 19 of all matter ($\Omega_b = 5.26\%$)—is already about 6.8 percent higher than the Planck satellite measurement ($4.93\%$), a **3.9-sigma tension on $\Omega_b$ alone**. Combining $\Omega_b = 1/19$ with standard Cosmic Microwave Background and primordial deuterium measurements also forces the present-day expansion rate down to **$H_0 \approx 65.2$ kilometers per second per megaparsec** (3.7 sigma below Planck and 7.4 sigma below local supernova measurements), and makes the primary cosmic matter-ratio pillar (`T2-A`) **forecast to fail at about 3.8 to 3.9 sigma**.
4. **The dark-energy curve (`T1-L1`) is much flatter than DESI's hint and is forecast to end in FAIL or INCONCLUSIVE:** While DESI DR2 does prefer a present-day dark-energy value above $-1$ (which passes the simple secondary sign check), the model's specific one-parameter leakage curve evolves six to seven times more flatly than the steep redshift evolution DESI prefers. When fitted directly to the DESI DR2 and supernova data, this pillar (`T1-L1`) is **disfavoured and forecast to land in FAIL or INCONCLUSIVE (most likely INCONCLUSIVE)**.
5. **The corrected galaxy rotation-curve formula caps the shadow halo at 6-to-1, whereas SPARC dwarfs reach 10-to-1 to 20-to-1:** Fixing a square-root factor in the 3D blurring formula cured an unphysical bug where the old formula predicted negative shadow mass near galaxy centers. However, a strict mathematical property of the corrected 3D blur is that a galaxy's enclosed shadow mass can **never exceed 5 times its ordinary baryonic mass** (a maximum total-to-baryonic gravity ratio of 6-to-1). Because gas-rich dwarf galaxies in the SPARC catalog routinely require total-to-baryonic gravity ratios of **about 10-to-1 to 20-to-1** in their outer regions, the primary galaxy rotation-curve pillar (`T5-A`) is **forecast to end in FAIL or INCONCLUSIVE** on the 70-percent pass bar. For the dark-matter-free galaxy NGC 1052–DF2 (`T5c`), passing now requires a shadow-blur scale **wider than about 2.2 kiloparsecs** (and fails if the blur scale is narrower than 1.4 kiloparsecs).
6. **Overall forecast across the three registered pillar tests with pre-test forecasts:** Out of the four primary pillars, **three registered pillar tests have analytical pre-test forecasts (`T1-L1`, `T2-A`, and `T5-A`)**, while the fourth (the 16-cluster reconnection cutoff `T4b`, whose sample was compiled from well-known literature mergers) depends on how the 8-cluster training and test halves line up. Because any single pillar failure falsifies version 1 and `T2-A` alone is about 3.8 to 3.9 sigma from passing, **version 1 of the model is forecast to be falsified by the pre-registered suite**, with two or three pillars expected to fail or come out inconclusive. In the film, this is a strength of the scientific story: the pre-registration caught a real mathematical bug in the galaxy kernel, exposed the exact physical bottlenecks of the 19-unit geometry, and refused to move the goalposts to save the theory.
