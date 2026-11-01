# Independent Auditor Verification Packet (`REVIEW_PACKET.md`)

- **Project:** Ropewalk Multiverse Empirical Test Suite (`v1.0.2` Execution)
- **Generated Timestamp:** `2026-10-30T07:58:00`
- **Overall Model Verdict:** **`MODEL FALSIFIED (FAIL)`**
- **Precedence Clause:** Where `PREREG.md` (`v1.0.2`) and any earlier document disagree, `PREREG.md` (`v1.0.2`) governs. `MULTIVERSE_TESTS_v1.md` is retained as a historical record only.

---

## 1. Cryptographic Time-Ordering Audit Trail

| Stage | Artifact / Manifest | Master SHA-256 Digest | OpenTimestamps Proof | Timestamp & Verification Status |
| :--- | :--- | :--- | :--- | :--- |
| **Stage 1: Pre-Registration Freeze** | `PREREG_v4.sha256` | `53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b` | `PREREG_v4.sha256.ots` | Frozen & OTS-stamped (`2026-04-17`) **before** any data download or analysis code |
| **Stage 2: Raw Data Freeze** | `DATA_MANIFEST.sha256` | `73135698afb833e7e95e6a85c55475480132300e29f8b7b42d159c037067896d` | `DATA_MANIFEST.sha256.ots` | Frozen & OTS-stamped (`2026-10-30T06:53:46`) **before** any gate, fit, or test execution |
| **Stage 4: Final Results Freeze** | `RESULTS_v1.sha256` | Recorded in `RESULTS_v1.sha256` | `RESULTS_v1.sha256.ots` | Frozen & OTS-stamped (`2026-10-30`) at completion of Part 11 |

---

## 2. Audit Checklist: Compliance with Stage 1 Reviews (`REVIEW_COLD`, `REVIEW_V2`, `REVIEW_V3`) & `PREREG.md` (`v1.0.2`)

| Requirement / Review Item | Pre-Registered Rule (`PREREG.md` `v1.0.2`) | Implementation & Output Artifact | Audit Verification Result |
| :--- | :--- | :--- | :--- |
| **Validation Gates (`G9-a`–`G9-d`, `V3-B3`)** | Gate-to-test mapping (`Sec 2`); `G9-a` $\le 0.3\sigma$; `G9-b` $\le 0.3\sigma$; `G9-c` $\le 1.0\sigma$; `G9-d` $< 10^{-10}$. | `tests/test_gates_g9.py` $\to$ `results/validation_gates_g9.json` | **`ALL 4 PASSED`** (`G9-a`: `0.037σ`; `G9-b`: `0.025σ`; `G9-c`: `0.361σ / 0.426σ`; `G9-d`: `1.44e-11`). Zero tests rendered `INCONCLUSIVE` by gate failure. |
| **Fast Cosmology & MCMC Diagnostics (`Rule G6`)** | `Hu & Sugiyama (1996)` fitting formulas (`Eq. 7`–`9`), 32 walkers, $\ge 1000$ burn-in, $\ge 4000$ prod steps, split $\hat{R}-1 < 0.01$, $\text{ESS} > 1000$. | `scripts/cosmology.py`, `scripts/run_part8_fixes.py`, `scripts/run_part9_cosmology_tests.py` | **`VERIFIED`**: All 14 MCMC chains converged with $\max|\hat{R}-1| \le 0.0035 < 0.01$ and $\min\text{ESS} \ge 1979 > 1000$. |
| **`T1-L1` Primary vs `T1-Sign` Secondary (`B4`, `V3-m1`)** | `T1-L1` tests $w(a) = -1 + \gamma_u/E(a)$ ($\gamma_u \ge 0$) via $A_r, B_r$; `T1-Sign` ($w_0 > -1$) is secondary only; Ly$\alpha$ $r_{\rm off}$ (`Eq. 45`) applied at $z_* = 2.33$. | `scripts/cosmology.py`, `results/part9_cosmology_results.json` | **`VERIFIED`**: `T1-L1` = `INCONCLUSIVE` (`P+`: $A=-1.71, B=+5.46$; `Dov`: $A=-2.58, B=+7.36$); `T1-Sign` = `PASS` ($P(w_0>-1) = 0.9960, 0.9992$). |
| **`T2-A` Single Deciding Version & `T2-N1`/`T2-N2` (`N1`, `M2`)** | `T2-A` is deciding (`PDG 2024` BBN, `Planck 2018` $3\times 3$ Table 1, independent $\sigma_{\rm comb}$); `FAIL` if $> 2.0\sigma$ in both runs. `T2-N1` ($\Omega_b=1/19$) and `T2-N2` ($H_0^{\rm pred}$) scored. | `scripts/run_part8_fixes.py`, `scripts/run_part9_cosmology_tests.py`, `results/FREEZE_T2.json` | **`VERIFIED`**: `T2-A` = `FAIL` (`P+`: $-3.74\sigma$, `Dov`: $-3.58\sigma$); `T2-N1` = `FAIL` ($+3.87\sigma$); `T2-N2` = `FAIL` ($65.19 \pm 0.22$, $-3.72\sigma$). |
| **`T4a` Locked as Exploratory (`B3`, `N8`)** | `T4a` is unconditionally `EXPLORATORY (Unscored)` with zero route back to a scored test (`Sec 5.4`); unified sign $\Delta_{SI,\parallel} > 0$ (`B2`). | `scripts/clusters_t4.py`, `results/results.json` (`T4.T4a_exploratory`) | **`VERIFIED`**: Reported as `EXPLORATORY (Unscored)`; non-Bullet $t_{\rm col} \le 400\text{ Myr}$ ($N=1$): $-45 \pm 52\text{ kpc}$ ($-0.87\sigma$). |
| **`T4b` Single Global Position Rules & Citations (`N2`, `V3-B2`)** | Global peak/centroid rules (`I`: lensing peak; `S`: luminosity-weighted centroid or BCG with logged substitution; `G`: X-ray peak/centroid); `16` clusters in `data/MERGERS.csv`. | `DEVIATIONS.md` (`DEV-T4B-01`, `DEV-T4B-02` logged before compute), `data/MERGERS.csv`, `scripts/clusters_t4.py` | **`VERIFIED`**: Deciding Odd/Even split $\hat{\tau}_{\rm lag} = 805\text{ Myr}$, $n_{\rm test} = 5 < 6 \implies$ `INCONCLUSIVE` (`Rule G8(3)`). Sensitivity splits with $n_{\rm test} \ge 6$ (`S6`, `S7`) $\implies$ `FAIL`. |
| **`T5-A` Single Mechanical Fitting Rule & Kernel (`B1`, `V3-B1`)** | Corrected $1/\sqrt{2\pi}$ factor in $\mathcal{F}_\sigma$ (`Eq. 38b`); minimize $\sum \chi^2_{{\rm red},g}$ on 88 odd-indexed training galaxies; exponential outer stellar tail (`4 R_d`), zero outer gas tail; 200 log + 200 linear $\sigma_{\rm ref}$ grid. | `scripts/sparc_t5.py`, `results/FREEZE_T5.json`, `results/results.json` (`T5`) | **`VERIFIED`**: $\hat{\sigma}_{\rm ref} = 9.2128\text{ kpc}$; held-out 87 test galaxies $M_{\chi^2} = 45.13 > 3.0$, $F_{<2} = 0.0690 < 0.40 \implies$ `FAIL` (`T5-B` also `FAIL`, $M_{\chi^2}=23.74$; `T5c` DF2 = `PASS`). |
| **`T6` Great-Circle Sparse-Pixel Merging (`V3-B4`)** | `HEALPix` $N_{\rm side}=1$ Galactic `RING`; merge pixels with $N_k < 10$ into nearest pixel by great-circle center distance (`Eq. 40c`) in increasing pixel index order before fitting $H_{0,k}$. | `scripts/local_h0_t6.py`, `results/FREEZE_T6.json`, `results/part9_cosmology_results.json` | **`VERIFIED`**: Pixels `4->0`, `7->2`, `11->4` merged, pixel `4` (`5` SNe) dropped $\to N_{\rm pix} = 9$ (`491` SNe), $\chi^2_{\rm het} = 8.9347$ ($\text{dof}=8$), $p_{\rm het} = 0.3478 > 0.3173 \implies$ `FAIL`. |
| **Holm–Bonferroni & Overall Verdict (`Sec 3.1` & `Sec 3.3`)** | $K=3$ discovery family (`T1-L1`, `T4b`, `T6`) at $\alpha_{\rm FWE}=0.05$; `MODEL FALSIFIED (FAIL)` if $\ge 2$ Primary Pillars `FAIL`. | `scripts/run_part10_astrophysics_and_verdict.py`, `results/results.json` | **`VERIFIED`**: 2 Primary Pillars `FAIL` (`T2-A`, `T5-A`), 2 `INCONCLUSIVE` (`T1-L1`, `T4b`), 0 `PASS` $\implies$ **`MODEL FALSIFIED (FAIL)`**. |
| **Workspace & Hardware Guardrails (`GEMINI.md`)** | Never delete any file; never touch `_ORIGINALS/`; single-thread BLAS headers; cap workers at `N_CORES = 12` at `BELOW_NORMAL_PRIORITY_CLASS`; append all actions to `ACTIVITY_LOG.md`. | All scripts in `scripts/` and `tests/`; `ACTIVITY_LOG.md` | **`VERIFIED`**: `_ORIGINALS/` untouched; zero deletions; all scripts carry BLAS single-thread headers and `N_CORES = 12` cap. |

---

## 3. Pre-Compute Deviations Summary (`DEVIATIONS.md`)

Only two minor pre-registered catalog-compilation entries were logged in `DEVIATIONS.md` **before** any cluster test was computed (`2026-10-30T07:03:00`):
1. **`DEV-T4B-01`:** Application of the pre-registered `PREREG.md` Section 5.5 Fallback Substitution Rule (brightest cluster galaxy `BCG` position with $\sigma_S = 0\text{ kpc}$ used where a separate luminosity-weighted galaxy centroid table was not published in `Monteiro-Oliveira+17a,b,18` for `#4 Abell 1758N`, `#5 Abell 2034`, and `#8 Abell 3376`).
2. **`DEV-T4B-02`:** Application of the pre-registered `PREREG.md` Section 5.5 Multi-Paper Priority Rule (`Clowe+06` + `Dawson 2013` for `#1 Bullet Cluster`; `Jee+14` for `#2 El Gordo` and `#9 Abell 520`; `Monteiro-Oliveira+17a` for `#4 Abell 1758N` with `Ragozzine+12` run as Sensitivity `S6`; `Coleman+17` + `White+15` for `#6 Abell 2146`; `Okabe & Umetsu 2008` + `Macario+11` for `#10 Abell 754`; `Jee+15` + `Dawson+15` for `#11 Sausage`).

Zero deviations occurred in `T1`, `T2`, `T5`, `T6`, or `Section 6`.
