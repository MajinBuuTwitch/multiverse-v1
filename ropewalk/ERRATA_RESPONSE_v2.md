# Errata Note on `REVIEW_RESPONSE_v2.md` (`ERRATA_RESPONSE_v2.md`)

**Date:** 2026-10-30  
**Purpose:** Document every place where the summary text in `REVIEW_RESPONSE_v2.md` misdescribed the actual governing Stage 1 files (`PREREG.md`, `MULTIVERSE_STAGE1_EQUATIONS.md`, `ASSUMPTIONS.md`, and `STAGE1_PART1/2/3`), as identified in `REVIEW_V3.md` (`M1` and `M3`). Per the non-destructive file policy (`GEMINI.md` §4), `REVIEW_RESPONSE_v2.md` itself is left untouched on disk and in the hash chain; this errata note records the exact governing text for each item.

> **Governing Rule:** Where `REVIEW_RESPONSE_v2.md` (or any response summary) and the governing files (`PREREG.md` and `MULTIVERSE_STAGE1_EQUATIONS.md`) disagree, **`PREREG.md` (for test definitions, thresholds, priors, datasets, optimizers, and decision rules) and `MULTIVERSE_STAGE1_EQUATIONS.md` (for mathematical equations) govern in every instance.**

---

## Itemized Corrections to `REVIEW_RESPONSE_v2.md`

1. **Number of Tests in the Holm–Bonferroni Family (`REVIEW_RESPONSE_v2.md` entries `N6`, `N9`, `M10`):**
   - **What `REVIEW_RESPONSE_v2.md` claimed:** Stated that $K = 9$ scored tests (including equivalence/goodness-of-fit survival gates `T2-A`, `T2-N1`, `T2-N2`, `T5-A`, and `T5c`) were included in the Holm–Bonferroni step-down family.
   - **What the governing `PREREG.md` §3.2 actually registers (and governs):** `PREREG.md` §3.2 registers **$K_{\rm disc} = 3$ null-rejection discovery tests** (`T1-L1` vs. $\Lambda\text{CDM}$, `T4b` vs. a $50\%$ coin-flip null, and `T6` vs. spatially uniform $H_0$) in the Holm–Bonferroni family ($\alpha_{(1)} = 0.01667$, $\alpha_{(2)} = 0.0250$, $\alpha_{(3)} = 0.050$), because goodness-of-fit and equivalence survival gates (`T2-A`, `T5-A`, `T5-B`, `T5c`, `T2-N1`, `T2-N2`) test consistency with a prediction (where smaller discrepancy is better, not rejection of a null hypothesis).

2. **`T6` HEALPix Pixel Count and Degrees of Freedom (`REVIEW_RESPONSE_v2.md` entries `N3`, `N9`):**
   - **What `REVIEW_RESPONSE_v2.md` claimed:** Stated that `T6` and `STAGE1_PART2_SECTIONS_DGH.md` `(g4)` were changed to a 48-pixel `HEALPix` $N_{\rm side} = 2$ map with $\text{dof} = 47$.
   - **What the governing files (`PREREG.md` §1.2, §5.7; `MULTIVERSE_STAGE1_EQUATIONS.md` §8.1 `(g4)`; `ASSUMPTIONS.md` `[A20]`; `STAGE1_PART2_SECTIONS_DGH.md` `(g4)`) actually register (and govern):** All governing and part files specify the **12-pixel `HEALPix` $N_{\rm side} = 1$ Galactic `RING` grid** ($N_{\rm pix} \le 12$ retained regions after sparse-pixel handling, with $\text{dof} = N_{\rm pix} - 1 \le 11$).

3. **$\chi^2_{\min}$ Optimizer Specification (`REVIEW_RESPONSE_v2.md` entry `N5`):**
   - **What `REVIEW_RESPONSE_v2.md` claimed:** Described the optimizer as a `50 x 50` grid search followed by `scipy.optimize.minimize(..., method="L-BFGS-B", tol=1e-10)` restarted from the 5 best grid nodes.
   - **What the governing `PREREG.md` §4 actually registers (and governs):** `PREREG.md` §4 specifies `scipy.optimize.minimize(..., method='Nelder-Mead', options={'xatol': 1e-6, 'fatol': 1e-6, 'maxiter': 10000})` initialized from the **5 highest-likelihood MCMC samples**, followed by bounded **`L-BFGS-B` polishing (`ftol=1e-12`)**.

4. **Sign and Formula for $w_a^{\rm fit}$ in `T1-L1` (`REVIEW_RESPONSE_v2.md` entry `B4`):**
   - **What `REVIEW_RESPONSE_v2.md` claimed:** Wrote the formula $w_a^{\rm fit} = (1 + w_0^{\rm fit})\frac{3}{2}\hat{\Omega}_m / [1 - \frac{1}{2}\hat{\Omega}_m(1 + w_0^{\rm fit})]$, which has the wrong sign and evaluates to $+0.078$ at $w_0 = -0.84, \Omega_m = 0.315$.
   - **What the governing files (`PREREG.md` §5.1; `MULTIVERSE_STAGE1_EQUATIONS.md` §5 `(d4 & d5)`; `ASSUMPTIONS.md` `[A9]`; `STAGE1_PART2_SECTIONS_DGH.md` `(d4)`) actually register (and govern):** All governing files have the exact derived formula:
     $$w_a^{\rm fit} = -\frac{3}{2}\hat{\gamma}_u\left[\hat{\Omega}_m + \hat{\gamma}_u\left(1 - \hat{\Omega}_m\right)\right] = -\frac{3}{2}\left(1 + w_0^{\rm fit}\right)\left[\hat{\Omega}_m + \left(1 + w_0^{\rm fit}\right)\left(1 - \hat{\Omega}_m\right)\right] \le 0,$$
     which evaluates to **$-0.1019$** ($\approx -0.102$) at $w_0 = -0.84$ and $\Omega_m = 0.315$.

5. **Non-Existent Section Citations in `MULTIVERSE_STAGE1_EQUATIONS.md` (`REVIEW_RESPONSE_v2.md` entries `B3`, `B4`, `N1`, `N2`, `N5`, `N6`, `N7`, `N8`, `N9`, `N10`, `m_v2-3`, `m_v2-4`, `m_v2-6`):**
   - **What `REVIEW_RESPONSE_v2.md` claimed:** Cited `MULTIVERSE_STAGE1_EQUATIONS.md` §§4.2–4.3, §5.2, §§6.1–6.5, §§7.2–7.6, and §§8.1–8.8 as containing test decision rules.
   - **What the governing files actually contain (and govern):** In `MULTIVERSE_STAGE1_EQUATIONS.md`, Section 4 has subsections `(c1)–(c4)`, Section 5 has `(d1 & d2)`, `(d3)`, `(d4 & d5)`, and `5.4 (d-Exp)`, Section 6 has `(e1–e5)` and `(e6 & e7)`, Section 7 has `(f1 & f2)`, `(f3)`, and `(f4)`, and Section 8 has subsections `8.1 (g1–g4)`, `8.2 (h1 & h2)`, `8.3 (i-Exp)`, and `8.4 (i) Master Parameter Table`. All test decision rules live in **`PREREG.md` §3 and §§5.1–5.7**.

6. **Peak Radius of the NGC 1052 Group Shadow Term in `T5c` (`REVIEW_RESPONSE_v2.md` entry `m_v2-4`):**
   - **What `REVIEW_RESPONSE_v2.md` claimed:** Stated that $M_{\rm sh,group}(< 3.1\text{ kpc})$ peaks at $4.9\times 10^6\,M_\odot$ at $\sigma_{\rm ref} \approx d_{\rm sep} = 80\text{ kpc}$.
   - **What the governing `PREREG.md` §5.6 actually registers (and governs):** For $d_{3\rm D} = \sqrt{3/2}(80\text{ kpc}) = 98.0\text{ kpc}$, $M_{\rm sh,group}(< 3.1\text{ kpc})$ peaks at $4.9\times 10^6\,M_\odot$ at **$\sigma_{\rm ref} = d_{3\rm D}/\sqrt{3} \approx 56.6\text{ kpc}$** (explicitly noted in `PREREG.md` §5.6).

7. **`T1-L1` Joint `FAIL` Rule Across the Two Supernova Runs (`REVIEW_RESPONSE_v2.md` entry `N5` vs. `PREREG.md` v3 §5.1, Resolved in v4 per `Review V3 M1`):**
   - **What `REVIEW_RESPONSE_v2.md` claimed:** Entry `N5` stated that `T1-L1` had joint `FAIL` if *either* supernova run was `FAIL`, whereas `PREREG.md` v3 §5.1 line 119 said joint `FAIL` required *both* runs to be per-run `FAIL`.
   - **Resolution in `PREREG.md` v4 (`Review V3 M1`):** Per Gregory's decision before any data access, `PREREG.md` §1.2 (Amendment 1) and §5.1 (along with `MULTIVERSE_STAGE1_EQUATIONS.md` §5 and §8.4 and `STAGE1_PART2_SECTIONS_DGH.md`) are now updated so that **`T1-L1` fails if *either* supernova run (`Pantheon+` or `DES-Dovekie`) fails its per-run `FAIL` condition**, matching `T2-A` and `T1-Sign`.
