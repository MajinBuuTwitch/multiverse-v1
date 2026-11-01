# Pre-Registration Deviations Log (`DEVIATIONS.md`)

**Governing Pre-Registration:** `PREREG.md` (v1.0.2), `MULTIVERSE_STAGE1_EQUATIONS.md` (v1.0.2), `ASSUMPTIONS.md` (v1.0.2) — frozen in `PREREG_v4.sha256` (`53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b`) and `PREREG_v4.sha256.ots`.

Per the Stage 2 governing rules, any departure from the frozen pre-registration forced by external data availability, file formats, or execution environment is logged in this file **before** computing the affected test's result, stating what changed, why, and the expected effect.

---

## Logged Deviations

### D1 — Retrieval of Exact arXiv Source Archives for 8 `T4b` Cluster Literature Papers (Logged Prior to Part 6 `T4b`/`T4a` Execution)
- **Affected Test:** `T4b` (Cluster Merger Two-Regime Transition Test) — data acquisition step only.
- **What Changed:** In Part 4, the automated download script `scripts/get_data.py` mapped 8 of the 16 `T4b` author-year citations to approximate arXiv IDs when populating `data/clusters_arxiv/`. Before constructing `data/MERGERS.csv` or writing `scripts/clusters_t4.py`, the 8 exact arXiv `.eprint` source archives corresponding to the registered papers in `PREREG.md` Section 5.4 were downloaded into `data/clusters_arxiv_exact/`:
  1. `Cho et al. (2022)` (`Abell 1240`) $\rightarrow$ `arXiv:2109.06879`
  2. `Monteiro-Oliveira et al. (2017a)` (`Abell 1758N`) $\rightarrow$ `arXiv:1605.07595`
  3. `Monteiro-Oliveira et al. (2018)` (`Abell 2034`) $\rightarrow$ `arXiv:1808.09449`
  4. `Coleman et al. (2017)` (`Abell 2146`) $\rightarrow$ `arXiv:1609.06765`
  5. `Monteiro-Oliveira et al. (2017b)` (`Abell 3376`) $\rightarrow$ `arXiv:1612.07935`
  6. `Golovich et al. (2016)` (`MACS J1149.5+2223`) $\rightarrow$ `arXiv:1608.01329`
  7. `Jee et al. (2016)` (`RX J0603.3+4214`) $\rightarrow$ `arXiv:1510.03486`
  8. `Golovich et al. (2017)` (`ZwCl 0008.8+5215`) $\rightarrow$ `arXiv:1703.04803`
- **Why:** To extract the exact tables and figures specified in `PREREG.md` Section 5.4 while leaving `data/clusters_arxiv/` untouched so `DATA_MANIFEST.sha256` remains bit-for-bit valid.
- **Expected Effect:** Zero change to the pre-registered protocol. Using the exact `.eprint` source files of the registered papers enforces strict compliance with the registered tables and rules in `PREREG.md` Section 5.4.

---

## IDENTIFIED IN FINAL REVIEW, NOT LOGGED AT THE TIME (Added `2026-10-30T09:05:35` per `REVIEW_FINAL.md`)

> **Note on `D1` above (`REVIEW_FINAL m7`):** `D1` above cited `PREREG.md` Section 5.4 for `T4b`; the `T4b` rules are in `PREREG.md` Section 5.5 (`Section 5.4` is `T4a`). Furthermore, because the 8 replacement `.eprint` archives in `data/clusters_arxiv_exact/` were downloaded after `DATA_MANIFEST.sha256` was stamped (`04:59:53` local / `08:59:53Z`), they were not covered by the pre-fit `DATA_MANIFEST.sha256` hash (`REVIEW_FINAL M7`); they are now hashed in `RESULTS_v2.sha256`.

### D2 (`REVIEW_FINAL M3`) — `T4b` Positional Uncertainty Entries ($\sigma_S = 0.0\text{ kpc}$ and $\sigma_G = 5.0\text{ kpc}$) in `data/MERGERS.csv`
- **Status:** **IDENTIFIED IN FINAL REVIEW, NOT LOGGED AT THE TIME** (Logged `2026-10-30T09:05:35`).
- **Affected Test:** `T4b` (Cluster Merger Two-Regime Transition Test, `PREREG.md` Section 5.5).
- **What Happened:**
  1. In `data/MERGERS.csv`, three clusters have galaxy positional uncertainty set to $\sigma_S = 0.0\text{ kpc}$ where the brightest cluster galaxy (`BCG`) position was used without a reported centroid uncertainty: `#4 Abell 1758N` (even/test), `#5 Abell 2034` (odd/train), and `#8 Abell 3376` (even/test). Under `PREREG.md` Section 5.5 item 5 (Missing-Data Rule), if a source paper does not report a positional uncertainty (or instrument centroiding error) for one of the three components, that cluster must be marked `"unclassified"` rather than assigning $\sigma_S = 0.0\text{ kpc}$.
  2. Five clusters in `data/MERGERS.csv` (`#1 1E 0657-558`, `#2 ACT-CL J0102-4915`, `#4 Abell 1758N`, `#5 Abell 2034`, `#8 Abell 3376`) carry an identical X-ray gas positional uncertainty $\sigma_G = 5.0\text{ kpc}$, which was entered as a default resolution estimate rather than traced to an explicit table entry in each source paper.
  3. In addition, an unregistered sensitivity split (`S7_First8_vs_Last8_split`) was included in `scripts/clusters_t4.py` and `results/results.json` (`REVIEW_FINAL M6`); `S7` was not registered in `PREREG.md` and is a post-hoc check.
- **Effect on Verdict (Confirmed by Independent Reviewer in `REVIEW_FINAL.md` M3):** **Zero change to the `T4b` verdict or frozen threshold.**
  - `#4 Abell 1758N` and `#8 Abell 3376` (both in the test half) are already `"unclassified"` in `data/MERGERS.csv`.
  - Applying the missing-data rule strictly to `#5 Abell 2034` marks it `"unclassified"` in the training half, changing the training accuracy at $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ from $7/8 = 0.875$ to $6/7 = 0.857$ (`>= 0.80`), with the frozen cutoff unchanged at $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ and the test half unchanged ($n_{\rm test} = 5 < 6 \implies$ `INCONCLUSIVE`).
  - Dropping the five $\sigma_G = 5.0\text{ kpc}$ clusters as well still leaves $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ and $n_{\rm test} \le 5 < 6$, so the deciding `T4b` verdict remains `INCONCLUSIVE`.

### C1–C4 (`REVIEW_FINAL m1–m4`) — Implementation Clarifications Identified in Final Review
- **`C1` (`m1` — `T6` Sequential Sparse-Pixel Merge Chain):** In `scripts/local_h0_t6.py`, following the literal pre-registered neighbor map in `PREREG.md` Section 5.7 in increasing `RING` pixel order (`0` to `11`), sparse pixel `4` (`3` SNe `< 10`) merges into pixel `0` (`63 + 3 = 66` SNe), pixel `7` (`8` SNe `< 10`) merges into pixel `2` (`61 + 8 = 69` SNe), and pixel `11` (`5` SNe `< 10`) merges into its mapped neighbor pixel `4` (`0 + 5 = 5` SNe), which remains `< 10` after the single pass and is dropped (`491` of `496` SNe retained across `N_pix = 9` regions; $\chi^2_{\rm het} = 8.9347$, $p_{\rm het} = 0.347838 \implies$ `FAIL`). As confirmed by the reviewer (`m1`), chaining `11 -> 4 -> 0` so all `496` SNe are retained gives $\chi^2_{\rm het} = 8.83$, $p_{\rm het} = 0.357$, which is also `FAIL`.
- **`C2` (`m2` — Early-Universe $r_s(z_*)$ Convention in Compressed CMB Prior):** In `scripts/cosmology.py` (`sound_horizon_rs_chen`), the recombination sound horizon $r_s(z_*)$ used in the `Chen, Huang & Wang (2019)` compressed CMB prior is evaluated using Chen et al.'s early-universe matter+radiation integrand ($\omega_r = 1/24185$, no dark-energy term at $z \ge z_* \approx 1090$), rather than the literal full-$H(z)$ integral in `MULTIVERSE_STAGE1_EQUATIONS.md` (`a5`), which differs by $0.184\%$. This matches the convention used by `Chen, Huang & Wang (2019)` to construct the $(R, l_A, 100\omega_b)$ prior table (`Gate G9-b` passes at $0.025\sigma$). As verified in `REVIEW_FINAL.md` (`m2`), using the literal (`a5`) integral leaves `T1-L1` `INCONCLUSIVE` ($A_r = -1.39 / -2.13$, $B_r = +5.53 / +7.46$).
- **`C3` (`m3` — `T1-L1` RK4 Shared Grid Size):** In `scripts/cosmology.py`, the fast vectorized Law 1 RK4 integration (`joint_chi2_law1`) runs on `_SHARED_Z_GRID` (`1401` nodes: `1001` linear on $z \in [0, 3]$ plus `400` log-spaced on $z \in (3, 1150]$) rather than the `1000`-point log-$a$ grid in `solve_law1_de_grid`. As verified by the reviewer (`m1`/`m3`), this agrees with an independent adaptive `DOP853`/`quad` integration to within $10^{-4}$ in $\chi^2$.
- **`C4` (`m4` — `T4b` Freeze Loading in `run_part10`):** In `scripts/run_part10_astrophysics_and_verdict.py`, `clusters_t4.run_all_t4()` recomputes $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ deterministically from `data/MERGERS.csv` rather than reading `results/FREEZE_T4.json` from disk; both give the identical value $\hat{\tau}_{\rm lag} = 805\text{ Myr}$ (`0.805 Gyr`).
