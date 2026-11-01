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
