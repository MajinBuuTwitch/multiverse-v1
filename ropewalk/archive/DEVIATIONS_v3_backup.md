# Pre-Registration Deviations Log (`DEVIATIONS.md`)

**Governing Pre-Registration:** `PREREG.md` (v1.0.2), `MULTIVERSE_STAGE1_EQUATIONS.md` (v1.0.2), `ASSUMPTIONS.md` (v1.0.2) — frozen in `PREREG_v4.sha256` (`53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b`) and `PREREG_v4.sha256.ots`.

Per the Stage 2 governing rules, any departure from the frozen pre-registration forced by external data availability, file formats, or execution environment is logged in this file **before** computing the affected test's result, stating what changed, why, and the expected effect.

---

## Logged Deviations (During Execution)

### D1 — Retrieval of Exact arXiv Source Archives for 8 `T4b` Cluster Literature Papers (Logged Prior to Part 6 `T4b`/`T4a` Execution)
- **Affected Test:** `T4b` (Cluster Merger Two-Regime Transition Test) — data acquisition step only.
- **What Changed:** In Part 4, the automated download script `scripts/get_data.py` mapped 8 of the 16 `T4b` author-year citations to approximate arXiv IDs when populating `data/clusters_arxiv/`. Before constructing `data/MERGERS.csv` or writing `scripts/clusters_t4.py`, the 8 exact arXiv `.eprint` source archives corresponding to the registered papers in `PREREG.md` Section 5.5 were downloaded into `data/clusters_arxiv_exact/`:
  1. `Cho et al. (2022)` (`Abell 1240`) $\rightarrow$ `arXiv:2109.06879`
  2. `Monteiro-Oliveira et al. (2017a)` (`Abell 1758N`) $\rightarrow$ `arXiv:1605.07595`
  3. `Monteiro-Oliveira et al. (2018)` (`Abell 2034`) $\rightarrow$ `arXiv:1808.09449`
  4. `Coleman et al. (2017)` (`Abell 2146`) $\rightarrow$ `arXiv:1609.06765`
  5. `Monteiro-Oliveira et al. (2017b)` (`Abell 3376`) $\rightarrow$ `arXiv:1612.07935`
  6. `Golovich et al. (2016)` (`MACS J1149.5+2223`) $\rightarrow$ `arXiv:1608.01329`
  7. `Jee et al. (2016)` (`RX J0603.3+4214`) $\rightarrow$ `arXiv:1510.03486`
  8. `Golovich et al. (2017)` (`ZwCl 0008.8+5215`) $\rightarrow$ `arXiv:1703.04803`
- **Why:** To extract the exact tables and figures specified in `PREREG.md` Section 5.5 while leaving `data/clusters_arxiv/` untouched so `DATA_MANIFEST.sha256` remains bit-for-bit valid.
- **Expected Effect:** Zero change to the pre-registered protocol.

---

## IDENTIFIED IN FINAL REVIEW, NOT LOGGED AT THE TIME (Added `2026-10-30` per `REVIEW_FINAL.md` and `COMPARISON_ARGON_vs_REBUILD.md`)

> **Note on `D1` above (`REVIEW_FINAL m7` & `M7`):** The original `D1` text cited `PREREG.md` Section 5.4 for `T4b`; the `T4b` rules are in `PREREG.md` Section 5.5 (`Section 5.4` is `T4a`). Furthermore, because the 8 replacement `.eprint` archives in `data/clusters_arxiv_exact/` were downloaded after `DATA_MANIFEST.sha256` was stamped (`04:59:53` local / `08:59:53Z`), they were not covered by the pre-fit `DATA_MANIFEST.sha256` hash; they are hashed in `RESULTS_v2.sha256` and `RESULTS_v3.sha256`.

### D2 (`REVIEW_FINAL M3` & `COMPARISON_ARGON_vs_REBUILD.md` Finding 2) — `T4b` Positional Uncertainty Entries ($\sigma_S = 0.0\text{ kpc}$ and $\sigma_G = 5.0\text{ kpc}$) vs. Strict Missing-Data Rule in `data/MERGERS.csv`
- **Status:** **IDENTIFIED IN FINAL REVIEW, NOT LOGGED AT THE TIME** (Updated `2026-10-30T10:38:00` per `REVIEW_FINAL.md` and `COMPARISON_ARGON_vs_REBUILD.md` Finding 2).
- **Affected Test:** `T4b` (Cluster Merger Two-Regime Transition Test, `PREREG.md` Section 5.5).
- **What Happened:**
  1. In `data/MERGERS.csv`, 13 clusters were marked classifiable (`n_train = 8`, `n_test = 5`) by relying on default or zero positional errors where the source paper did not report an explicit positional uncertainty: specifically, three clusters have galaxy positional uncertainty set to $\sigma_S = 0.0\text{ kpc}$ (`#4 Abell 1758N`, `#5 Abell 2034`, `#8 Abell 3376`), five clusters carry an identical default X-ray gas positional uncertainty $\sigma_G = 5.0\text{ kpc}$ (`#1 1E 0657-558`, `#2 ACT-CL J0102-4915`, `#4 Abell 1758N`, `#5 Abell 2034`, `#8 Abell 3376`), and the remaining clusters other than `MACS J0025.4-1222` lacked a complete set of explicitly reported positions and uncertainties across all three components (`L`, `G`, `S`) in their registered tables/figures.
  2. As demonstrated by the blind independent rebuild (`COMPARISON_ARGON_vs_REBUILD.md` Finding 2), applying the registered missing-data rule in `PREREG.md` Section 5.5 item 5 strictly leaves **only one cluster (`#11 MACS J0025.4-1222`, in the odd/training half)** with complete positions and errors (`n_train = 1`, `n_test = 0`).
  3. In addition, an unregistered sensitivity split (`S7_First8_vs_Last8_split`) was included in `scripts/clusters_t4.py` and `results/results.json` (`REVIEW_FINAL M6`); `S7` was not registered in `PREREG.md` and is a post-hoc check.
- **Effect on Verdict:** **Zero change to the `T4b` verdict (`INCONCLUSIVE` either way).**
  - Under the strict missing-data rule (`n_train = 1`, `n_test = 0`, only `MACS J0025.4-1222` complete) and under the 13-cluster set (`n_train = 8`, `n_test = 5`), `T4b` is **`INCONCLUSIVE`** ($n_{\rm test} < 6$). All claims based on `"13 classifiable clusters"` have been removed from `RESULTS.md` and the paper.

### D3 (`COMPARISON_ARGON_vs_REBUILD.md` Finding 1 & `REVIEW_FINAL m2`) — Sound-Horizon Integral $r_s(z_*)$ in Validation Gate `G9-b` (`Chen, Huang & Wang 2019` Early-Universe Form vs. Registered Equation `a5`)
- **Status:** **IDENTIFIED IN FINAL REVIEW, NOT LOGGED AT THE TIME** (Logged `2026-10-30T10:38:00` per `COMPARISON_ARGON_vs_REBUILD.md` Finding 1).
- **Affected Gate & Tests:** Validation Gate `G9-b` (`DESI DR2 BAO` + Compressed CMB Flat $\Lambda\text{CDM}$ Recovery), which maps to `T2-A`, `T1-L1`, and `T1-Sign` under `PREREG.md` Section 7.2.
- **What Happened:**
  1. The registered sound-horizon equation in `MULTIVERSE_STAGE1_EQUATIONS.md` (`a5`) is the full integral using the registered radiation density $\Omega_r h^2 = 4.183 \times 10^{-5}$ (`\omega_r \approx 1/23906`) and the physical neutrino treatment.
  2. During Part 5 gate execution, `scripts/cosmology.py` (`sound_horizon_rs_chen`) was modified at `05:02:46` (logged in `ACTIVITY_LOG.md` as a "bug fix" ten seconds before the gates passed at `05:02:56`, rather than logged in `DEVIATIONS.md` as a departure from `a5`) to use `Chen, Huang & Wang (2019)`'s own early-universe $r_s(z_*)$ formula ($\omega_r = 1/24185$, about $1.1\%$ below the physical radiation density, and the $0.06\text{ eV}$ neutrino counted as pure matter at $z \ge z_*$).
  3. That Chen et al. form produces an $r_s(z_*)$ about **$0.18\%$ larger** than the registered `(a5)` integral ($+0.29\%$ from the lower $\omega_r$, $-0.12\%$ from the neutrino treatment; dark energy contributes $< 10^{-7}$). Because $\ell_A = \pi D_M(z_*)/r_s(z_*)$ is fixed by the compressed CMB prior, a $0.18\%$ larger $r_s(z_*)$ lowers the inferred $h$, allowing `G9-b` to pass in Argon's pipeline ($\max \Delta = 0.025\sigma$).
  4. The blind independent rebuild (`COMPARISON_ARGON_vs_REBUILD.md`, `REBUILD_RESULTS_v1`, `93a154fb...`) coded the registered integral `(a5)` literally (matching `CAMB`'s $r_s(z_*)$ to $4.9 \times 10^{-5}$ with no calibration factor). Under literal `(a5)`, Gate `G9-b` **fails** ($h$ off by $0.577\sigma$ against a $0.3\sigma$ tolerance).
- **Effect on Verdicts (Both Readings Reported Plainly in `RESULTS.md` and the Paper):**
  - **Reading 1 — Literal Registered `(a5)` Integral (Blind Rebuild):** Gate `G9-b` **FAILS** ($0.577\sigma$), which by the gate-to-test mapping rule renders **`T2-A` `INCONCLUSIVE`**, **`T1-L1` `INCONCLUSIVE`**, and **`T1-Sign` `INCONCLUSIVE`** — even though the `T2-A` leak-ratio statistic sits at $-3.447\sigma$ (`Pantheon+`) and $-3.224\sigma$ (`DES-Dovekie`) from the Planck value, well past the $2\sigma$ `FAIL` threshold.
  - **Reading 2 — `Chen, Huang & Wang (2019)` Early-Universe $r_s(z_*)$ Form (Argon):** Gate `G9-b` **PASSES** ($0.025\sigma$), **`T2-A` is `FAIL`** ($-3.7445\sigma$ on `Pantheon+`, $-3.5801\sigma$ on `DES-Dovekie`), **`T1-Sign` is `PASS`** ($P(w_0 > -1) = 0.9960 / 0.9992$), and **`T1-L1` is `INCONCLUSIVE`**.
  - **Invariant Across Both Readings:** In every run of both pipelines, `T2-A`'s statistic lies **$3.2\sigma\text{--}3.7\sigma$ from the Planck value** (past the $2\sigma$ `FAIL` line), `T1-L1` is **`INCONCLUSIVE`**, `T5-A` is **`FAIL`** (median $\chi^2_{\rm red} = 45.13$ in Argon, $45.91$ in Rebuild; $F_{<2} = 0.0690$ in both), and the overall model-level verdict is **`MODEL FALSIFIED (FAIL)`** under both readings.

### C1, C3, C4 (`REVIEW_FINAL m1, m3, m4`) — Additional Implementation Clarifications Identified in Final Review
- **`C1` (`m1` — `T6` Sequential Sparse-Pixel Merge Chain):** In `scripts/local_h0_t6.py`, following the literal pre-registered neighbor map in `PREREG.md` Section 5.7 in increasing `RING` pixel order (`0` to `11`), sparse pixel `4` (`3` SNe `< 10`) merges into pixel `0` (`63 + 3 = 66` SNe), pixel `7` (`8` SNe `< 10`) merges into pixel `2` (`61 + 8 = 69` SNe), and pixel `11` (`5` SNe `< 10`) merges into its mapped neighbor pixel `4` (`0 + 5 = 5` SNe), which remains `< 10` after the single pass and is dropped (`491` of `496` SNe retained across `N_pix = 9` regions; $\chi^2_{\rm het} = 8.9347$, $p_{\rm het} = 0.347838 \implies$ `FAIL`, identical in both Argon and the blind rebuild). Chaining `11 -> 4 -> 0` so all `496` SNe are retained gives $\chi^2_{\rm het} = 8.83$, $p_{\rm het} = 0.357$, which is also `FAIL`.
- **`C3` (`m3` — `T1-L1` RK4 Shared Grid Size):** In `scripts/cosmology.py`, the fast vectorized Law 1 RK4 integration (`joint_chi2_law1`) runs on `_SHARED_Z_GRID` (`1401` nodes: `1001` linear on $z \in [0, 3]$ plus `400` log-spaced on $z \in (3, 1150]$) rather than the `1000`-point log-$a$ grid in `solve_law1_de_grid`. This agrees with an independent adaptive `DOP853`/`quad` integration to within $10^{-4}$ in $\chi^2$.
- **`C4` (`m4` — `T4b` Freeze Loading in `run_part10`):** In `scripts/run_part10_astrophysics_and_verdict.py`, `clusters_t4.run_all_t4()` recomputes $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ deterministically from `data/MERGERS.csv` rather than reading `results/FREEZE_T4.json` from disk; both give the identical value $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ (`0.805 Gyr`).
