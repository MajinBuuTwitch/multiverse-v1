# Response to Independent Review V3 (`REVIEW_V3.md`)

**Date:** 2026-10-30  
**Scope:** Item-by-item response to all 15 findings in `REVIEW_V3.md` (`B1`–`B4`, `M1`–`M3`, and Minor items `1`–`8`), plus the updated plain-English `WHAT CHANGES FOR THE FILM` section. Every section reference, equation, threshold, and numerical value in this response has been verified line-by-line against the governing files (`PREREG.md` v1.0.2, `MULTIVERSE_STAGE1_EQUATIONS.md` v1.0.2, `ASSUMPTIONS.md`, and `ERRATA_RESPONSE_v2.md`). Prior v3 copies are preserved intact in `_TRASH/`.

---

## Summary of Resolution Counts (`REVIEW_V3.md`)

- **Total Findings in `REVIEW_V3.md`:** 15 (`B1`–`B4` [4], `M1`–`M3` [3], Minor items `1`–`8` [8])
  - **FIXED:** 15
  - **PARTIAL:** 0 *(Note: The Review V2 sample-selection disclosure `N10`/`M6` for the 16-cluster `T4b` literature table remains marked `PARTIAL` from `REVIEW_RESPONSE_v2.md` and was verified as properly disclosed in `REVIEW_V3.md` line 73.)*
  - **DISPUTED:** 0
  - **DEFERRED:** 0

---

## 1. Blockers (`B1`–`B4`)

### `B1` — `T5-A` / `T5-B` Training Objective Function, Stellar-Only Exponential Tail $\Sigma_b^{\rm tail}(r_{\max})$, and 400-Point Grid Split
- **Status:** **FIXED**
- **Where Changed:** `PREREG.md` §1.2 (Amendment 5) and §5.6 (items 2 and 3); `MULTIVERSE_STAGE1_EQUATIONS.md` §7 `(f3)`, §8.4 (Master Parameter Table), and §10 `[A15]`; `ASSUMPTIONS.md` `[A15]`.
- **Single Mechanical Rule Registered:**
  1. **Training Objective Function:** On the 88 training galaxies, $\hat{\sigma}_{\rm ref} \in [0.1, 100.0]\text{ kpc}$ (`T5-A`, which also feeds `T5c`) and $\hat{k} \in [0.05, 50.0]$ (`T5-B`) are fixed by minimizing the **sum of per-galaxy reduced chi-squared across the 88 training galaxies**:
     $$\mathcal{L}_{\rm train}(\sigma_{\rm ref}) \equiv \sum_{g \in {\rm train}} \chi^2_{{\rm red},g}(\sigma_{\rm ref}) = \sum_{g \in {\rm train}} \frac{1}{N_g}\sum_{j=1}^{N_g} \left(\frac{V_{{\rm obs},g}(r_j) - v_{{\rm model},g}(r_j; \sigma_{\rm ref})}{\sigma_{V,g}(r_j)}\right)^2.$$
     *One-sentence reason:* Minimizing the sum of per-galaxy $\chi^2_{{\rm red},g}$ gives every training galaxy equal weight regardless of its number of radial data points $N_g$ while remaining smooth and continuously differentiable for `scipy.optimize.minimize_scalar`. *(Total pooled $\chi^2$ and median $\chi^2_{{\rm red},g}$ training fits are listed in `PREREG.md` §3.1 item 3 and §5.6 item 3 as non-deciding sensitivity checks.)*
  2. **Baryon Surface Density in the Exponential Tail Beyond $r_{\max}$ (Stars Only, Entering $M_{\rm sh}$ Only):** Because SPARC `MassModels_Lelli2016c.mrt` tabulates `SBdisk` and `SBbul` (in $L_\odot\text{ pc}^{-2} = 10^6\,L_\odot\text{ kpc}^{-2}$) and has no gas surface-density column, the tail surface density at $r_{\max} \equiv r_{N_g}$ is defined from the stellar columns only (with zero gas tail beyond $r_{\max}$):
     $$\Sigma_b^{\rm tail}(r_{\max}) \equiv 10^6\left[\Upsilon_{\rm disk}\,\text{SBdisk}(r_{N_g}) + \Upsilon_{\rm bul}\,\text{SBbul}(r_{N_g})\right]\;M_\odot\text{ kpc}^{-2}, \qquad \Sigma_{\rm tail}(r') = \Sigma_b^{\rm tail}(r_{\max})\,\exp\!\left(-\frac{r' - r_{\max}}{R_{d,g}}\right),$$
     discretized on **100 uniformly spaced linear intervals on $[r_{\max}, r_{\max} + 5\sigma_{\rm ref}]$** with shell masses $\Delta M_{b,m}^{\rm tail} = 2\pi r'_{{\rm mid},m}\,\Sigma_{\rm tail}(r'_{{\rm mid},m})\,\Delta r'_m$, and **entering only the nonlocal shadow integral $M_{\rm sh}(< r_j)$ for $r_j \le r_{\max}$** (never altering $M_b^{\rm mono}(< r_j)$ or $v_{\rm bar}(r_j)$).
     *One-sentence reason:* SPARC provides explicit stellar surface-brightness columns (`SBdisk`, `SBbul`) at $r_{\max}$, and by Newton's spherical shell theorem exterior shells at $r' > r_{\max}$ contribute zero local Newtonian force at $r_j \le r_{\max}$ while contributing to the Gaussian-smeared shadow mass $M_{\rm sh}(< r_j)$.
  3. **Exact 400-Point Interior Grid Split:** The 400-point interior grid on $[0, r_{\max}]$ consists of **200 uniformly spaced linear nodes on $[0, r_1]$** (with uniform-core scaling $M_b^{\rm mono}(< r') = M_b^{\rm mono}(< r_1)(r'/r_1)^3$ inside the innermost measured radius $r_1$) joined to **200 logarithmically spaced nodes on $[r_1, r_{\max}]$** (dropping the duplicate endpoint at $r_1$ so there are 400 distinct interior nodes $0 = r'_0 < r'_1 < \dots < r'_{399} = r_{\max}$), interpolated on $[r_1, r_{\max}]$ via monotonic PCHIP (`scipy.interpolate.PchipInterpolator`) with shell masses evaluated at shell midpoints $r'_{{\rm mid},m} = \frac{1}{2}(r'_{m-1} + r'_m)$.

### `B2` — `T4b` Global Mechanical Observable Rules for $(I, G, S)$, Uncertainties, Table/Section Pointers, and Missing-Data Exclusion Rule
- **Status:** **FIXED**
- **Where Changed:** `PREREG.md` §1.2 (Amendment 4) and §5.5 (item 5 and the 16-cluster table); `MULTIVERSE_STAGE1_EQUATIONS.md` §10 `[A14]`; `ASSUMPTIONS.md` `[A14]`.
- **Single Mechanical Rule Registered:**
  - **Mass Position ($\mathbf{x}_I$):** Weak-lensing convergence ($\kappa$) / surface-mass-density peak of the designated primary subcluster.
  - **Gas Position ($\mathbf{x}_G$):** X-ray surface-brightness (emission-measure) peak of the designated primary subcluster (or its stripped X-ray gas core / cold-front clump as identified in the primary source paper).
  - **Galaxy Position ($\mathbf{x}_S$):** Optical/NIR luminosity-weighted galaxy centroid of the designated primary subcluster; if and only if the primary source paper does not tabulate a luminosity-weighted galaxy centroid for that subcluster, the **subcluster brightest cluster galaxy (BCG) position** reported in that paper is used as the mechanical substitute.
  - **Positional Uncertainties ($\sigma_I, \sigma_G, \sigma_S$):** The 1D $68\%$ ($1\sigma$) sky positional error (converted to physical $\text{kpc}$ at $z_{\rm cl}$ using flat $\Lambda\text{CDM}$ with $H_0 = 67.36, \Omega_m = 0.315$ if quoted in arcsec), computed as $\sigma_c \equiv \sqrt{\frac{1}{2}(\sigma_{\alpha^*}^2 + \sigma_\delta^2)} = \sqrt{\frac{1}{2}(a_{1\sigma}^2 + b_{1\sigma}^2)}$ when 2D errors or $1\sigma$ ellipse axes are given (or dividing $90\%$ / $95\%$ error radii by $1.645$ / $1.960$).
  - **Table / Section / Figure Pointers:** Added explicit table, section, and figure pointers for both the dynamical age and the single primary $(S, G, I)$ position source in all 16 rows of the `PREREG.md` §5.5 table (and fixed row 4 `Abell 1758N` and row 14 `MACS J1149.5+2223` so each names a single primary position paper in the main text, with `Ragozzine+12` and `Rau+14` marked as sensitivity checks).
  - **Mechanical Missing-Data Exclusion Rule:** Any cluster whose designated primary source paper lacks any of $(\mathbf{x}_I, \mathbf{x}_G, \mathbf{x}_S)$ (after the centroid $\to$ BCG rule for $\mathbf{x}_S$) or lacks a positional uncertainty $\sigma_c$ needed for $\sigma_{\rm diff} = \sqrt{\sigma_I^2 + \sigma_G^2 + \sigma_S^2}$ is **mechanically marked `"unclassified"` and excluded from $n_{\rm train}$ or $n_{\rm test}$**.
  - *One-sentence reason:* Fixing one global operational definition for $(I, G, S)$ and $\sigma_c$ with automatic exclusion (`"unclassified"`) of any incomplete system removes all post-hoc freedom to flip a cluster's classification.

### `B3` — Validation Gates (`G9`) Test-Specific Mapping, Exact Gate Datasets, Bug-Fix-Only Rule, and `G9-c` $1.0\sigma$ Tolerance
- **Status:** **FIXED**
- **Where Changed:** `PREREG.md` §2 (`G8` item 2 and `G9`), §5.1, §5.2, and §5.6; `STAGE1_PART1_SECTIONS_ABC.md` (Part 0 Rule 9).
- **Single Mechanical Rule Registered:**
  1. **Strict Gate-to-Test Mapping:** A gate failure makes **only the tests mapped to that gate `INCONCLUSIVE`, never the whole suite**:
     - **`G9-a` and `G9-b` map only to:** `T1-L1`, `T1-Sign`, `T2-A`, and `T2-B` (and to `T5-A`, `T5-B`, `T5c` **only** if `T2-A-Pantheon+` fails to produce a converged $f_{\rm leak}$).
     - **`G9-c` maps only to:** the **`DES-Dovekie` runs** of `T1-L1`, `T1-Sign`, `T2-A`, and `T2-B` (not to `Pantheon+` or `T5`; if the `Pantheon+` run passes `G9-a`/`G9-b` and yields per-run `FAIL`, then `T2-A` or `T1-L1` ends in joint `FAIL` regardless of `G9-c`).
     - **`G9-d` maps only to:** `T5-A`, `T5-B`, and `T5c`.
     - **No gate dependency:** **`T4b` (Pillar 3), `T6`, `T2-N1`, and `T2-N2` depend on no `G9` gate.**
  2. **Exact Gate Datasets (Including Ly$\alpha$ Configuration):** Both **`G9-a`** and **`G9-c`** run on the **unmodified official `CobayaSampler/bao_data/desi_bao_dr2` BAO-only dataset** (retaining the standard $z_{\rm eff} = 2.33$ Ly$\alpha$ BAO row $D_M/r_d = 38.99 \pm 0.53$, $D_H/r_d = 8.632 \pm 0.101$, $r = -0.431$, **without** the `arXiv:2607.27410` AP replacement) so they match the exact BAO inputs used by DESI Collaboration (2025b, Table V) and Popovic et al. (2025, Table 11).
  3. **Bug-Fix-Only Rule:** The **only** allowed response to a gate failure is a **logged software bug fix in `scripts/`** (recorded in `ACTIVITY_LOG.md`). **No registered input, prior, dataset, formula, or threshold may ever be changed to pass a gate.**
  4. **`G9-c` Tolerance Set to $1.0\sigma$:** Widened `G9-c`'s tolerance from $0.3\sigma$ to **$1.0\sigma$** ($|\hat{w}_0 - (-0.803)| \le 0.054$ and $|\hat{w}_a - (-0.72)| \le 0.21$), while keeping $0.3\sigma$ for `G9-a` and `G9-b`.
  - *One-sentence reason:* Scoping each gate strictly to its dependent tests and setting `G9-c`'s tolerance to $1.0\sigma$ accounts for the known $\sim 0.3\text{–}0.7\sigma$ shift between Chen et al. (2019) compressed geometric CMB priors and full Planck+lensing likelihoods in $w_0w_a\text{CDM}$ while eliminating any suite-wide `INCONCLUSIVE` escape hatch.

### `B4` — `T6` Mechanical Sparse-Pixel Merging Rule on the 12-Pixel `HEALPix` $N_{\rm side} = 1$ `RING` Grid
- **Status:** **FIXED**
- **Where Changed:** `PREREG.md` §1.2 (Amendment 6) and §5.7; `STAGE1_PART2_SECTIONS_DGH.md` `(g4)`; `MULTIVERSE_STAGE1_EQUATIONS.md` §10 `[A20]`; `ASSUMPTIONS.md` `[A20]`.
- **Single Mechanical Rule Registered:** In increasing order of `HEALPix` $N_{\rm side} = 1$ Galactic `RING` pixel index $i \in \{0, 1, \dots, 11\}$, **any pixel with $0 < N_{{\rm SN},i} < 10$ is merged into the edge-sharing neighbor pixel (sharing a continuous 1D boundary segment of positive length, not a corner vertex) that has the lowest `RING` pixel index** — which uniquely maps `0->1, 1->0, 2->1, 3->0` (north polar cap), **`4->0, 5->0, 6->1, 7->2` (equatorial belt)**, and `8->4, 9->5, 10->6, 11->4` (south polar cap) — and **any empty pixel ($N_{{\rm SN},i} = 0$) or any merged region that still has $N_{\rm SN} < 10$ after this single pass is dropped**, leaving $N_{\rm pix} \le 12$ retained regions with $N_{\rm SN} \ge 10$ and $\text{dof} = N_{\rm pix} - 1$.
  - *One-sentence reason:* Merging any sparse pixel into its edge-sharing neighbor of lowest `RING` index (and dropping any region that remains $< 10$) defines a unique, data-independent target for all 12 `HEALPix` $N_{\rm side}=1$ pixels, breaking the 4-way polar symmetry of the equatorial Zone-of-Avoidance pixels (`4–7`) mechanically.

---

## 2. Majors (`M1`–`M3`)

### `M1` — `T1-L1` Joint `FAIL` Rule Changed to "Either Supernova Run Fails" (Gregory's Decision)
- **Status:** **FIXED**
- **Where Changed:** `PREREG.md` §1.2 (Amendment 1), §3.1, and §5.1; `MULTIVERSE_STAGE1_EQUATIONS.md` §5 `(d4 & d5)` and §8.4 (Master Parameter Table); `STAGE1_PART2_SECTIONS_DGH.md` §d item 3; `ERRATA_RESPONSE_v2.md` item 7.
- **Action Taken:** Per Gregory's instruction, changed the Joint `T1-L1` Verdict across the two supernova runs in `PREREG.md` §5.1 so that **`T1-L1` ends in Joint `FAIL` if *either* `Pantheon+` *or* `DES-Dovekie` meets its per-run `FAIL` condition ($B_r > +9.0$ or $A_r > -1.0$), and ends in Joint `PASS` only if *both* runs meet their per-run `PASS` condition (and survive Holm–Bonferroni)** — matching `T2-A` and `T1-Sign`. Declared this openly in `PREREG.md` §1.2 (Amendment 1) and updated the `T1-L1` forecast to `FAIL` or `INCONCLUSIVE` (since `DES-Dovekie` is forecast around $B \approx 9\text{–}10$, right at the $B > 9.0$ per-run `FAIL` boundary).

### `M2` — Plain Statement of `T4b`'s Effective Perfect-Score Bar After Holm–Bonferroni Control
- **Status:** **FIXED**
- **Where Changed:** `PREREG.md` §3.1 (Pillar 3), §3.2, and §5.5 (threshold 2 `PASS`); `MULTIVERSE_STAGE1_EQUATIONS.md` §8.4 (Master Parameter Table); and the `WHAT CHANGES FOR THE FILM` section below.
- **Action Taken:** Stated plainly in `PREREG.md` §3.2 and §5.5 that because one miss on the test half gives one-sided binomial $p$-values of $5/6 \to p = 0.109375 > 0.050$, $6/7 \to p = 0.0625 > 0.050$, and $7/8 \to p = 0.035156 > 0.0250$, **after the Holm–Bonferroni correction `T4b`'s nominal $\ge 80\%$ bar effectively requires a perfect $100\%$ score on the classified test half ($6/6 \to p = 0.0156$, $7/7 \to p = 0.0078$, or $8/8 \to p = 0.0039$)**, with the single exception that $7/8$ ($87.5\%$, $p = 0.035156 \le \alpha_{(3)} = 0.050$) survives if and only if `T4b` sits at Holm rank 3 because **both** `T1-L1` and `T6` simultaneously achieve discovery $p$-values below $0.01667$ and $0.0250$.

### `M3` — Creation of `ERRATA_RESPONSE_v2.md` Correcting `REVIEW_RESPONSE_v2.md` Discrepancies
- **Status:** **FIXED**
- **Where Changed:** Created `D:\Argon_Code\Ropewalk\ERRATA_RESPONSE_v2.md` (and hashed it in `PREREG_v4.sha256`).
- **Action Taken:** Listed all seven discrepancies between `REVIEW_RESPONSE_v2.md` and the governing files (`K_disc = 3` discovery tests in Holm–Bonferroni vs. 9; `T6` 12-pixel `HEALPix` $N_{\rm side} = 1$ grid vs. 48 pixels; `Nelder-Mead` from 5 best MCMC samples + `L-BFGS-B` `ftol=1e-12` vs. `50x50` grid; exact $w_a^{\rm fit} = -\frac{3}{2}\hat{\gamma}_u[\hat{\Omega}_m + \hat{\gamma}_u(1 - \hat{\Omega}_m)] = -0.1019$ vs. $+0.078$; exact section numbers in `MULTIVERSE_STAGE1_EQUATIONS.md` and `PREREG.md`; `T5c` group peak location $\sigma_{\rm ref} = d_{3\rm D}/\sqrt{3} \approx 56.6\text{ kpc}$ vs. $80\text{ kpc}$; and the `T1-L1` joint `FAIL` rule now unified to "either run fails" in v4) and stated that **`PREREG.md` and `MULTIVERSE_STAGE1_EQUATIONS.md` govern in every instance**.

---

## 3. Minors (`1`–`8`)

### `Minor 1` — `T2-A` `DES-Dovekie` Forecast Is $3.35\sigma$ (and `Pantheon+` Is $3.72\sigma$, About $3.4\text{–}3.7\sigma$)
- **Status:** **FIXED**
- **Where Changed:** `PREREG.md` §3.1 (Pillar 2) and §5.2; `MULTIVERSE_STAGE1_EQUATIONS.md` §4 (Plain Statement of the Ratio Tension) and §8.4 (Master Parameter Table); `STAGE1_PART1_SECTIONS_ABC.md` §c item 4; and the Film Note below.
- **Action Taken:** Updated the `T2-A` pre-test forecast from `~3.8–3.9σ` to **$3.72\sigma$ (`Pantheon+`, $\mathcal{R}_{\rm pred} \approx 4.89$, $\sigma_{\rm comb} = 0.126$) and $3.35\sigma$ (`DES-Dovekie`, $\mathcal{R}_{\rm pred} \approx 4.92$, $\sigma_{\rm comb} = 0.131$), i.e., about $3.4\text{–}3.7\sigma$**.

### `Minor 2` — `T2-N2` Sensitivity Value (`Cooke vs. DESI+BBN = 6.42σ`) and Uncorrelated Planck $(\omega_b, H_0)$ Note
- **Status:** **FIXED**
- **Where Changed:** `PREREG.md` §5.2 (`T2-N2`); `MULTIVERSE_STAGE1_EQUATIONS.md` §4 `(c4)` item 2.
- **Action Taken:** Corrected the non-deciding `Cooke+18` ($H_0^{\rm pred} = 64.15 \pm 0.28$) vs. `DESI+BBN` ($H_0 = 68.52 \pm 0.62$) sensitivity tension from $6.84\sigma$ to **$6.42\sigma$**, and stated explicitly that the deciding `T2-N2` value ($-3.72\sigma$) treats Planck's $\omega_b = 0.02237 \pm 0.00015$ and $H_0 = 67.36 \pm 0.54$ from the same $\Lambda\text{CDM}$ chain as uncorrelated in $\sigma_{\rm comb,H_0} = \sqrt{0.22^2 + 0.54^2} = 0.583$, which is conservative because their positive correlation makes the true tension larger than $3.72\sigma$.

### `Minor 3` — Cooke et al. (2018) vs. Planck $\omega_b$ Tension ($2.9\sigma$ Combined, $3.7\sigma$ in Cooke's $\sigma$)
- **Status:** **FIXED**
- **Where Changed:** `PREREG.md` §1.2 (Amendment 2) and §5.2.
- **Action Taken:** Updated the description of the discrepancy between Cooke et al. (2018) ($100\omega_b = 2.166 \pm 0.019$) and Planck Table 1 ($100\omega_b = 2.236 \pm 0.015$) from `"3.6σ"` to **"$2.9\sigma$ when both errors are combined in quadrature ($3.7\sigma$ in units of Cooke's error alone)"**.

### `Minor 4` — Ly$\alpha$ BAO+AP Citation (`DESI Collaboration 2026, arXiv:2607.27410`) and Correlation Coefficient $r_{D_H, D_M} = -0.431$
- **Status:** **FIXED**
- **Where Changed:** `PREREG.md` §2 (`G6`) and §5.1.
- **Action Taken:** Replaced `"Cuceu et al. (2025, arXiv:2607.27410)"` with **DESI Collaboration (2026, *"DESI DR2 Results IV: Alcock–Paczyński measurements from the Lyman alpha forest and cosmological constraints"*, arXiv:2607.27410, submitted 29 July 2026; `MULTIVERSE_DATASETS_v1.md` line 53)**. Stated explicitly in `PREREG.md` §5.1 that because `MULTIVERSE_DATASETS_v1.md` line 53 quotes the marginal constraints $D_H(2.33)/r_d = 8.600 \pm 0.066$ and $D_M(2.33)/r_d = 39.32 \pm 0.33$ from `arXiv:2607.27410` without an off-diagonal correlation, **$r_{D_H, D_M} = -0.431$ (the published DESI DR2 Ly$\alpha$ BAO correlation from DESI Collaboration 2025a,b, `arXiv:2503.14738` Table IV / `desi_bao_dr2`) is locked as the single deciding correlation coefficient** for the $2\times 2$ block at $z_{\rm eff} = 2.33$, with $r_{D_H, D_M} = 0$ and the unmodified `desi_bao_dr2` BAO-only row registered as non-deciding sensitivity checks.

### `Minor 5` — Rewording the $235\text{ Myr}$ Floor as a Gaussian-Approximated One-Sided 95% Lower Credible Bound
- **Status:** **FIXED**
- **Where Changed:** `PREREG.md` §1.2 (Amendment 4) and §5.5 (item 2); `MULTIVERSE_STAGE1_EQUATIONS.md` §8.4 (Master Parameter Table); `STAGE1_PART3_SECTIONS_EFI.md` `(f4)`.
- **Action Taken:** Reworded `"one-sided 95% lower confidence bound"` to **"Gaussian-approximated one-sided 95% lower credible bound (5th percentile, $0.40 - 1.645(0.10) = 0.2355\text{ Gyr} \approx 235\text{ Myr}$ of the symmetric Dawson 2013 Table 2 temporal-prior Bayesian posterior $0.40 \pm 0.10\text{ Gyr}$)"**.

### `Minor 6` — Pinning `scipy == 1.18.1` and `numpy == 2.5.4`
- **Status:** **FIXED**
- **Where Changed:** `PREREG.md` §2 (`G9-d`) and §4 (Global Numerical Settings).
- **Action Taken:** Pinned **`scipy == 1.18.1`** and **`numpy == 2.5.4`** in `D:\Argon_Code\Ropewalk\.venv` for all Stage 2–4 computations and Gate `G9-d`.

### `Minor 7` — Edge Cases: `T4b` with $n_{\rm train} = 0$ and Holm $p$-Value of a Non-Converged Discovery Test
- **Status:** **FIXED**
- **Where Changed:** `PREREG.md` §3.2 (Holm–Bonferroni edge-case rule) and §5.5 (`T4b` thresholds).
- **Action Taken:**
  1. In `PREREG.md` §5.5: defined $\text{Acc}_{\rm train}(\tau_{\rm lag}) \equiv 0.0$ if $n_{\rm train} = 0$, and added $n_{\rm train} = 0$ explicitly to `FAIL` clause 1(a).
  2. In `PREREG.md` §3.2: specified that if any of the $K_{\rm disc} = 3$ discovery tests (`T1-L1`, `T4b`, `T6`) fails to converge, fails its mapped `G9` validation gate, or has fewer than the minimum sample size ($n_{\rm test} < 6$ in `T4b` or $N_{\rm pix} < 2$ in `T6`), **its discovery $p$-value is mechanically set to $p = 1.0$** in the 3-test Holm–Bonferroni sort.

### `Minor 8` — Covariance Matrix Notation ($\mathbf{C}_{\rm HF}$ vs. $\mathbf{C}_{H_0}$) in `[A20]`
- **Status:** **FIXED**
- **Where Changed:** `ASSUMPTIONS.md` `[A20]` and `MULTIVERSE_STAGE1_EQUATIONS.md` §10 `[A20]`.
- **Action Taken:** Updated `[A20]` to refer to **"the bare Pantheon+ Hubble-flow supernova covariance block $\mathbf{C}_{\rm HF}$ (which already contains peculiar-velocity covariance, propagated to the $N_{\rm pix} \times N_{\rm pix}$ regional $H_0$ covariance $\mathbf{C}_{H_0}$)"**, matching `PREREG.md` §5.7 and `MULTIVERSE_STAGE1_EQUATIONS.md` §8.1 `(g4)`.

---

## WHAT CHANGES FOR THE FILM

1. **The Bullet Cluster age and the shadow-reconnection clock:** In the primary weak-lensing dynamical model for the Bullet Cluster (Dawson 2013), the collision happened **likely around 400 million years ago, and almost certainly more than 200 million years ago** (with a 95 percent lower credible bound of about 235 million years, rather than the older 150-million-year bow-shock estimate). Because the Bullet Cluster still shows strong dark-matter separation today, the model's shadow-matter reconnection clock must be slower than at least 235 million years, and most likely slower than 400 million years.
2. **The early-collision offset test (`T4a`) is exploratory only:** With a reconnection clock that long, the simple spring approximation used for early collisions is stretched past its clean linear regime, and the early-offset test (`T4a`) is locked as an unscored exploratory check in version 1. Interestingly, the corrected math predicts that during the first two-thirds of the reconnection window, the gravitational shadow actually **trails** behind the normal stars before slingshotting ahead of them—the exact opposite of the original v1 equation sheet.
3. **The 1-in-19 baryon fraction is already in ~3.9-sigma tension with Planck and predicts $H_0 \approx 65.2$:** Before running any new combined fit, the model's core structural number—that ordinary matter is exactly 1 part in 19 of all matter ($5.26\%$)—is already about 6.8 percent higher than the Planck satellite measurement ($4.93\%$), a **3.9-sigma tension on ordinary matter alone**. Combining that 1-in-19 share with standard Cosmic Microwave Background and primordial deuterium measurements also forces the present-day expansion rate down to **about 65.2 kilometers per second per megaparsec** (3.7 sigma below Planck and 7.4 sigma below local supernova measurements), and makes the primary cosmic matter-ratio pillar (`T2-A`) **forecast to fail at about 3.4 to 3.7 sigma** (specifically about 3.7 sigma with Pantheon+ supernovae and about 3.35 sigma with DES-Dovekie supernovae).
4. **The dark-energy curve (`T1-L1`) fails if either supernova sample fails, and is forecast to land in FAIL or INCONCLUSIVE:** While DESI DR2 does prefer a present-day dark-energy value above $-1$ (which passes the simple secondary sign check), the model's specific one-parameter leakage curve evolves six to seven times more flatly than the steep redshift evolution DESI prefers. Under Gregory's pre-registered rule, **this pillar (`T1-L1`) fails if either supernova sample (`Pantheon+` or `DES-Dovekie`) fails its goodness-of-fit threshold**. Because the `Pantheon+` run is forecast to land in the inconclusive band while the `DES-Dovekie` run is forecast to land right on the failure boundary, **`T1-L1` is disfavoured and forecast to end in FAIL or INCONCLUSIVE**.
5. **The cluster reconnection cutoff (`T4b`) effectively requires a perfect score on the test half:** For the third pillar (`T4b`, which tests whether a single reconnection delay separates young collisions from old ones across the 16-cluster sample), once the statistical correction for running multiple discovery tests is applied, **the nominal 80-percent accuracy bar effectively requires a perfect 100-percent score on the held-out test clusters** (6 out of 6, 7 out of 7, or 8 out of 8 correct). A single miss on 8 test clusters (7 out of 8, or 87.5 percent) is downgraded to inconclusive unless both of the other two discovery tests (`T1-L1` and the local Hubble map `T6`) also pass with strong statistical significance at the same time.
6. **The corrected galaxy rotation-curve formula caps the shadow halo at 6-to-1, whereas SPARC dwarfs reach 10-to-1 to 20-to-1:** Fixing a square-root factor in the 3D blurring formula cured an unphysical bug where the old formula predicted negative shadow mass near galaxy centers. However, a strict mathematical property of the corrected 3D blur is that a galaxy's enclosed shadow mass can **never exceed 5 times its ordinary baryonic mass** (a maximum total-to-baryonic gravity ratio of 6-to-1). Because gas-rich dwarf galaxies in the SPARC catalog routinely require total-to-baryonic gravity ratios of **about 10-to-1 to 20-to-1** in their outer regions, the primary galaxy rotation-curve pillar (`T5-A`) is **forecast to end in FAIL or INCONCLUSIVE** on the 70-percent pass bar. For the dark-matter-free galaxy NGC 1052–DF2 (`T5c`), passing now requires a shadow-blur scale **wider than about 2.2 kiloparsecs** (and fails if the blur scale is narrower than 1.4 kiloparsecs).
7. **Overall forecast across the three registered pillar tests with pre-test forecasts:** Out of the four primary pillars, **three registered pillar tests have analytical pre-test forecasts (`T1-L1`, `T2-A`, and `T5-A`)**, while the fourth (`T4b`, whose 16-cluster sample was compiled from well-known literature mergers) must overcome an effective perfect-score bar on its test half. Because any single pillar failure falsifies version 1 and `T2-A` alone is about 3.4 to 3.7 sigma from passing, **version 1 of the model is forecast to be falsified by the pre-registered suite**, with two or three pillars expected to fail or come out inconclusive. In the film, this is a strength of the scientific story: the pre-registration caught a real mathematical bug in the galaxy kernel, exposed the exact physical bottlenecks of the 19-unit geometry, and refused to move the goalposts to save the theory.
