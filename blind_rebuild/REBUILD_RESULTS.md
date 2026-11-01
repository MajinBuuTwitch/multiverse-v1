# REBUILD_RESULTS.md — Blind independent rebuild, PHASE 1

Generated mechanically by `rebuild/write_results_md.py` from `results_rebuild/results.json` (analysis run 2026-10-30T09:01:43-0400; code SHA-256 of rebuild/*.py + run_all_rebuild.py at analysis time: `937d0a1163d8e929c1afa56ab32de8c05ba2284f4f7b075dda00226cf3fa0a66`). Governing rulebook: PREREG.md (v4 package, verified by SHA-256).

## 0. Summary of verdicts

| Test | Class | Verdict |
|---|---|---|
| T1-L1 | Primary pillar 1 | **INCONCLUSIVE** |
| T2-A | Primary pillar 2 | **INCONCLUSIVE** |
| T4b | Primary pillar 3 | **INCONCLUSIVE** |
| T5-A | Primary pillar 4 | **FAIL** |
| T1-Sign | Scored secondary | **INCONCLUSIVE** |
| T2-N1 | Scored secondary | **FAIL** |
| T2-N2 | Scored secondary | **FAIL** |
| T5-B | Scored secondary | **FAIL** |
| T5c | Scored secondary | **PASS** |
| T6 | Scored secondary | **FAIL** |

**Model-level verdict (PREREG §3.3): MODEL FALSIFIED (FAIL)**

## 1. Validation gates (PREREG §2 G9)

| Gate | Statistic | Value | Target | Tolerance | Result |
|---|---|---|---|---|---|
| G9-a | posterior mean Ωm (flat ΛCDM, unmodified desi_bao_dr2) | 0.2977 ± 0.0088 | 0.2975 | ±0.00258 | PASS (diff 1.9722e-04) |
| G9-b | posterior mean Om (Chen+19 ΛCDM 3×3 prior alone) | 0.31572 ± 0.00854 | 0.3166 (σ=0.0084) | ±0.00252 | within (-0.104σ) |
| G9-b | posterior mean h (Chen+19 ΛCDM 3×3 prior alone) | 0.67616 ± 0.00617 | 0.6727 (σ=0.006) | ±0.00180 | OUTSIDE (0.577σ) |
| G9-b | posterior mean wb100 (Chen+19 ΛCDM 3×3 prior alone) | 2.23581 ± 0.01505 | 2.236 (σ=0.015) | ±0.00450 | within (-0.013σ) |
| G9-b | overall | | Planck 2018 VI Table 2 TT,TE,EE+lowE (DEVIATIONS D2) | 0.3σ each | **FAIL** |
| G9-c | posterior mean w0 (desi_bao_dr2 + Chen+19 + DES-Dovekie) | -0.8212 ± 0.0579 | -0.803 | ±0.054 | within (-0.337σ) |
| G9-c | posterior mean wa (desi_bao_dr2 + Chen+19 + DES-Dovekie) | -0.6580 ± 0.2422 | -0.72 | ±0.21 | within (0.295σ) |
| G9-c | overall | | Popovic+25 Table 11 | 1.0σ each | **PASS** |
| G9-d | max abs(F_σ − ncx2.cdf) on registered 5×7 grid (numpy 2.5.4, scipy 1.18.1) | 1.440e-11 | 0 | < 1e-10 | **PASS** |

G9-d independent 3D Monte Carlo cross-check (2×10⁶ points, 6 configurations): max |z| = 2.365.

Gate-run convergence: G9a_lcdm_BAOstd: R̂−1 = 5.5315e-04, ESS_min = 10806, G9b_lcdm_CMB: R̂−1 = 9.6326e-04, ESS_min = 10588, G9c_cpl_BAOstd_CMB_D: R̂−1 = 0.00192, ESS_min = 5796.

G9-b failure audit (mandatory bug check, PREREG G9): see `results_rebuild/validation/g9b_bugcheck.json` and the ACTIVITY_LOG entry at 06:46:24. D_M(z*) agrees with CAMB to 2.6e-6 and r_s(z*) to 4.9e-5. No implementation bug was found, so no code was changed. Mapped tests (T1-L1, T1-Sign, T2-A, T2-B) are INCONCLUSIVE by the gate route unless a valid run triggers FAIL.

## 2. Pillar 1 — T1-L1 (and secondary T1-Sign)

Registered statistic: A_r = Δχ²_min(Law 1 − ΛCDM), B_r = Δχ²_min(Law 1 − w0waCDM) per SN run; per-run FAIL if B > 9 or A > −1; PASS if A ≤ −4 and B ≤ 4; else INCONCLUSIVE. Joint FAIL if either valid run FAILs. Datasets: DESI DR2 BAO with the registered Lyα BAO+AP replacement (r = −0.431), the Chen+19 ΛCDM 3×3 CMB prior, and SNe (separately).

| SN run | χ²_min ΛCDM | χ²_min Law 1 | χ²_min w0waCDM | A | B | per-run outcome | γ̂_u | w0_fit | wa_fit | numerical precision of A, B (optimizer spread) | converged | mapped gates pass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pantheon+ | 1404.1852 | 1402.8397 | 1397.2933 | -1.3456 | 5.5464 | INCONCLUSIVE | 0.0343 | -0.9657 | -0.0171 | 1.7e-08 | yes | no |
| DES-Dovekie | 1649.6947 | 1647.6161 | 1640.1409 | -2.0786 | 7.4753 | INCONCLUSIVE | 0.0396 | -0.9604 | -0.0200 | 1.0e-08 | yes | no |

γ_u posterior (Law-1 MCMC): Pantheon+: median 0.0391 (68%: 0.0155–0.0673); DES-Dovekie: median 0.0422 (68%: 0.0187–0.0684).

Discovery p-value p_T1-L1 = max_r[1 − F_χ²₁(max(0, −A_r))] = 0.246053; value entering Holm (set to 1.0 if a run is invalid, §3.2 edge-case rule) = 1.000000.

Raw joint T1-L1 outcome: INCONCLUSIVE. **Final T1-L1 verdict: INCONCLUSIVE.**

T1-Sign (one-sided 95%: PASS if P(w0 > −1) ≥ 0.95 in both runs; FAIL if P(w0 < −1) ≥ 0.95 in either, or σ_w0 ≤ 0.03 with (−1, 0) inside the 68% region in both):

| SN run | w0 (mean ± sd) | wa (mean ± sd) | P(w0 > −1) | (−1,0) Mahalanobis² | (−1,0) in 68% region |
|---|---|---|---|---|---|
| Pantheon+ | -0.8558 ± 0.0552 | -0.5280 ± 0.2152 | 0.99638 | 6.913 | no |
| DES-Dovekie | -0.8270 ± 0.0569 | -0.6397 ± 0.2333 | 0.99909 | 9.232 | no |

**T1-Sign verdict: INCONCLUSIVE.** Run validity (converged and mapped gates pass): Pantheon+: no, DES-Dovekie: no.

## 3. Pillar 2 — T2-A (and T2-N1, T2-N2)

Registered statistic: |R_pred − 5.36| vs 2σ_comb, with R_pred = 19 Ω_bc − 1 (Ω_bc = median of the posterior; σ_Ωbc = ½(q84 − q16)) and σ_comb = √((19σ_Ωbc)² + 0.065²). FIT: flat w0waCDM; DESI DR2 BAO with the Lyα BAO+AP replacement; conditional Chen+19 (R, ℓ_A | ω_b); DESI/LUNA BBN 100ω_b = 2.218 ± 0.055; SNe separately.

| SN run | Ω_bc (median ± σ) | f_leak ± σ_f | R_pred ± 19σ | σ_comb | (R_pred − 5.36)/σ_comb | exceeds 2σ_comb | converged | mapped gates pass |
|---|---|---|---|---|---|---|---|---|
| Pantheon+ | 0.31090 ± 0.00601 | 0.1821 ± 0.0190 | 4.9071 ± 0.1142 | 0.1314 | -3.447 | yes | yes | no |
| DES-Dovekie | 0.31281 ± 0.00588 | 0.1761 ± 0.0186 | 4.9433 ± 0.1117 | 0.1292 | -3.224 | yes | yes | no |

**T2-A verdict: INCONCLUSIVE.** Frozen f_leak passed to T5 (from T2-A-Pantheon+): 0.182146 (`results_rebuild/FREEZE_T2.json`, SHA-256 `83b1bb3929ffae89c3f426daad599fc0e8cf4d8eceb6db8bcaeee85c7181eff3`).

- **T2-N1** (Ω_b^model = 1/19 = 0.052632 vs Planck 0.0493 ± 0.00086): difference 0.003332 = 3.874σ; threshold 2σ. **Verdict: FAIL.**
- **T2-N2** (H0_pred = 100√(19ω_b) = 65.194 ± 0.22 for 100ω_b = 2.237 ± 0.015, vs Planck 67.36 ± 0.54; σ_comb = 0.5831): difference -2.166 = -3.714σ; threshold 2σ_comb. **Verdict: FAIL.** (Propagated σ of H0_pred from σ(100ω_b) = 0.015: 0.2186; the registered 0.22 is used.)

## 4. Pillar 3 — T4b

Registered statistic: hard-step classification accuracy on the classified test half at τ̂_lag, which is trained on the classified training half over [235, 1500] Myr in 5 Myr steps (ties go to the smallest τ). Classification uses the single deciding (S, G, I) source per cluster and the 2σ_diff rule.

- Classified clusters: n_train = 1, n_test = 0.
- τ̂_lag = 505 Myr; max training accuracy = 1.000.
- Test accuracy = nan (k_obs = 0); binomial p = 1.000000; p entering Holm = 1.000000 (n_test < 6 → p = 1.0, §3.2 edge-case rule).
- FAIL clauses: (a) no, (b) no, (c) no. Raw outcome: INCONCLUSIVE.

**T4b verdict: INCONCLUSIVE.**

**Interpretive dependence (DEVIATIONS D10 item 2 and D12), reported with equal prominence:** only one cluster (row 13, MACS J0025.4-1222, Bradač+08) has all three positions and per-position 1σ errors. That depends on reading the Bradač+08 Table 2 'galaxies' row as the luminosity-weighted galaxy centre. Under the alternative reading (the row is a smoothed-light-map peak, which D10 item 1 does not accept, and the paper gives no BCG coordinates), row 13 is unclassified, n_train = 0, n_test = 0, and T4b would be **FAIL** (FAIL clause 1(a): yes). The deciding reading is the one logged before computation (D10).

Known sample-selection limitation (PREREG §5.5): the 16-cluster sample was compiled from the literature by an author with prior knowledge of published offsets; T4b cannot be free of selection bias.

### 4.1 Extracted T4b cluster position table

Positions and per-position errors as read from each single deciding source paper (verbatim quotes, pointers and per-cluster notes: `t4b_extraction/cluster_NN.json`, `cluster_NN_notes.md`; protocol `t4b_extraction/EXTRACTION_PROTOCOL.md`, written before any paper was opened). Fingerprinted in DATA_MANIFEST_REBUILD_PAPERS.sha256 (OTS-stamped) before T4b was computed.

| # | Designation | Half | t_p (Gyr) | Paper | Table / section / value | Status / class |
|---|---|---|---|---|---|---|
| 1 | 1E 0657-558 | train | 0.4 | Clowe et al. 2006, ApJ 648, L109 (astro-ph/0608407) | Table 2 'Component Masses' (subcluster plasma, subcluster BCG); Sec. 3 (kappa peak 7.1" E, 6.5" N of subcluster BCG) | unclassified: no numerical 1-sigma positional uncertainty for I, G or S (only qualitative significance statements and figure contours) |
| 2 | ACT-CL J0102-4915 | test | 0.75 | Jee et al. 2014, ApJ 785, 20 (arXiv:1309.5097) | Sec. 4.1-4.2, Fig. 8 caption (SE shear peak 01:02:56.31 -49:16:23.2; X-ray peak ~8" from mass peak) | unclassified: no galaxy position (no BCG coordinates; only a luminosity PEAK described qualitatively); no sigma_G |
| 3 | Abell 1240 | train | 0.45 | Cho et al. 2022, ApJ 925, 68 (arXiv:2109.06879) | Table 2 (A1240S luminosity-weighted density PEAK 170.903349 +43.061313) | unclassified: no coordinates for the weak-lensing peak or X-ray peak; no uncertainties |
| 4 | Abell 1758N | test | 0.4 | Monteiro-Oliveira et al. 2017a, MNRAS 466, 2614 (arXiv:1605.07595) | Sec. 2.6.2 (NW mass centre 24(+10/-14)" from NW BCG); Table A1 (BCG 13:32:38.3 +50:33:35.8) | unclassified: no NW X-ray peak position; no sigma_G, sigma_S |
| 5 | Abell 2034 | train | 0.3 | Monteiro-Oliveira et al. 2018, MNRAS 481, 1097 (arXiv:1808.09449) | mass-clump table (clump 1 = A2034N, 15:10:13 +33:33:43); appendix catalogue (BCG N 15:10:10.2 +33:34:01.5) | unclassified: paper states no gas concentration is associated with A2034N (no x_G); no per-position sigmas |
| 6 | Abell 2146 | test | 0.25 | Coleman et al. 2017, MNRAS 464, 2469 (arXiv:1609.06765) | model-results table, Model 2 (DM halo A centroid 239.05860 +66.348183, error matrix); separations to X-ray peak 30.3 kpc and to BCG-A 1.63 kpc | unclassified: no per-position uncertainty for the X-ray peak (separation only) |
| 7 | Abell 2744 | train | 0.15 | Merten et al. 2011, MNRAS 417, 333 (arXiv:1103.2772) | Table 2 STRUCTURES (Core peak (-13,-4)" from BCG, +11/-8, +6/-13); Sec. 4.1 (I-G separation 22+-12"); BCG 3.58611 -30.40024 | unclassified: no per-position sigma for the X-ray peak (only the I-G separation error) and none for the BCG; NW alternative equally lacks G and S |
| 8 | Abell 3376 | test | 0.55 | Monteiro-Oliveira et al. 2017b, MNRAS 468, 4566 (arXiv:1612.07935) | no positions tabulated (Table 2 = masses) | unclassified: no coordinates or separations for I, G, S |
| 9 | Abell 520 | train | 0.8 | Jee et al. 2014, ApJ 783, 78 (arXiv:1401.3356) | Table 1 row P4 (04 54 04.32 +02 53 51.0, +-3.0", +-4.4") | unclassified: no X-ray or galaxy position for P4 |
| 10 | Abell 754 | test | 0.3 | Okabe & Umetsu 2008, PASJ 60, 345 (astro-ph/0702649) | Sec. 3.1, Fig. 5 (qualitative only) | unclassified: no coordinates and no uncertainties for I, G, S |
| 11 | CIZA J2242.8+5301 | train | 0.8 | Jee et al. 2015, ApJ 802, 46 (arXiv:1410.2898) | abstract / Sec. 5 (~1' mass-galaxy offset, approximate) | unclassified: no tabulated positions or uncertainties; no X-ray position |
| 12 | DLSCL J0916.2+2951 | test | 1.1 | Dawson et al. 2012, ApJL 747, L42 (arXiv:1110.4391) | Sec. 5 (South WL peak 09h16m15s +-8.0s, +29d49m34s +-6.9") | unclassified: no galaxy position of any kind for the South subcluster; no X-ray position attributed to the South subcluster |
| 13 | MACS J0025.4-1222 | train | 0.5 | Bradac et al. 2008, ApJ 687, 959 (arXiv:0806.2320) | Table 2 'Offsets (with 1 sigma errorbars) of the mass peaks and gas peaks', SE block: total (-0.70+-0.25, -0.43+-0.06), gas (0.0+-0.08, 0.0+-0.08), galaxies (-0.79+-0.20, -0.50+-0.20) arcmin from the gas peak 00:25:29.5 -12:22:36.6 (Sec. 5); Sec. 4.3 'centers of the light distributions (galaxies)'; x_I = (-0.7, -0.43) ± (0.25, 0.06) ′, x_G = (0.0, 0.0) ± (0.08, 0.08) ′, x_S = (-0.79, -0.5) ± (0.2, 0.2) ′; z = 0.586 | dark mass with galaxies (d_IG = 336.7 kpc, d_IS = 46.7 kpc, σ_diff = 115.5 kpc; |d_IG − d_IS|/2σ_diff = 1.255) |
| 14 | MACS J1149.5+2223 | test | 1.16 | Golovich et al. 2016, ApJ 831, 110 (arXiv:1608.01329) | Sec. 3.2 (NW luminosity-density PEAK); Table 3 (GMM centre); lensing offset cited from Smith+09 | unclassified: no lensing position measured in the paper; no X-ray coordinates; no BCG coordinates |
| 15 | RX J0603.3+4214 | train | 1.5 | Jee et al. 2016, ApJ 817, 179 (arXiv:1510.03486) | Table 2 P1 centroid (90.81674, 42.24823); Sec. 5.2 (X-ray ~0.5' from mass peak) | unclassified: no uncertainties for any position; no galaxy coordinates |
| 16 | ZwCl 0008.8+5215 | test | 0.76 | Golovich et al. 2017, ApJ 838, 110 (arXiv:1703.04803) | Table 3 (WL east peak with bootstrap errors; X-ray east peak +-5.3s, +-2.0"; luminosity PEAK; east BCG 00h12m18.8s +52d33m46.9s without error) | unclassified: x_S = BCG (luminosity position is explicitly a map peak, D10 item 1) has no positional uncertainty and no optical centroiding error is stated |

## 5. Pillar 4 — T5-A (and T5-B, T5c)

Frozen inputs: f_leak = 0.182146 (T2-A-Pantheon+), 6(1 − f_leak) = 4.90712; SPARC split 88 training / 87 held-out (byte-wise sorted ids). Objective: sum of per-galaxy reduced χ² over the training half (200-point log grid, then bounded minimize_scalar, xatol = 1e-5). `results_rebuild/FREEZE_T5.json` SHA-256 `13e6ad5bf0645e1657b7474352a646f2230db90f50e37909dc4dd3050ea6819b`.

Registered statistic (held-out half): median χ²_red (M) and fraction with χ²_red < 2 (F). PASS: M ≤ 1.5 and F ≥ 0.70; FAIL: M > 3.0 or F < 0.40; else INCONCLUSIVE.

| Test | Fitted width | Training objective at optimum | Held-out median χ²_red | Held-out F(χ²_red < 2) | n held-out | Verdict |
|---|---|---|---|---|---|---|
| T5-A | σ̂_ref = 9.34361 kpc | 17965.445 | 45.9137 | 0.0690 | 87 | **FAIL** |
| T5-B | k̂ = 2.95090 | 9534.198 | 23.4258 | 0.0805 | 87 | **FAIL** |

Dependency check (G9-d PASS and T2-A-Pantheon+ converged; DEVIATIONS D11): yes.

**Interpretive dependence (DEVIATIONS D11), reported with equal prominence:** gate G9-b FAILED. PREREG §2 G9 maps G9-a/G9-b to T5 'only if T2-A-Pantheon+ fails to produce a converged f_leak because G9-a or G9-b failed'. T2-A-Pantheon+ converged (R̂−1 = 0.00241) and its f_leak was frozen, so under the deciding literal reading (logged in D11 before T5 was computed) T5-A, T5-B and T5c stand as computed. Under the alternative reading (any G9-a/b failure invalidates the f_leak passed to T5), T5-A, T5-B and T5c would be **INCONCLUSIVE**.

**T5c** (NGC 1052-DF2, σ_ref = σ̂_ref from T5-A = 9.34361 kpc): M_pred(<2.7 kpc) = 9.8602e+07 M☉ (baryons 9.3182e+07, DF2 shadow 5.4199e+06, group shadow -4.8983e-13); M_pred(<3.1 kpc) = 1.1661e+08 M☉ (baryons 1.0847e+08, DF2 shadow 8.1425e+06, group shadow -7.5830e-13); M_pred(<7.6 kpc) = 2.8034e+08 M☉ (baryons 1.7726e+08, DF2 shadow 1.0308e+08, group shadow -8.9912e-11). (The group-shadow term is zero to floating-point precision at this σ_ref; tiny negative values are round-off.) Thresholds: PASS if M(<2.7) ≤ 2.9e8 and M(<3.1) < 3.2e8; FAIL if M(<2.7) > 3.7e8. **Verdict: PASS.**

## 6. T6 — regional H0 heterogeneity

FIX: GLS M_B from 77 Cepheid calibrators = -19.24888 ± 0.03011 mag (`results_rebuild/FREEZE_T6.json` SHA-256 `edda246e8ad3361ca1710dcdc8c28f1eedf7cab7cc62abbf0be3d5ed19b8c1dd`).

TEST: 496 Pantheon+ Hubble-flow SNe (0.023 ≤ z_HD ≤ 0.15, non-calibrator) in Galactic HEALPix Nside = 1 RING pixels. Initial counts [63, 52, 61, 46, 3, 20, 16, 8, 77, 103, 42, 5]; merges (pixel→target) [[4, 0], [7, 2], [11, 4]]; retained regions [0, 1, 2, 3, 5, 6, 8, 9, 10] (N_pix = 9, 491 SNe).

| Region | N_SN | H0 ± σ (km/s/Mpc) |
|---|---|---|
| 0 | 66 | 74.079 ± 0.627 |
| 1 | 52 | 73.511 ± 0.665 |
| 2 | 69 | 72.929 ± 0.630 |
| 3 | 46 | 75.089 ± 0.726 |
| 5 | 20 | 73.413 ± 1.177 |
| 6 | 16 | 73.520 ± 1.182 |
| 8 | 77 | 73.510 ± 0.514 |
| 9 | 103 | 73.266 ± 0.466 |
| 10 | 42 | 72.525 ± 0.728 |

Registered statistic: χ²_het = 8.935 (dof 8), p_het = 0.34784; GLS mean H̄0 = 73.506 ± 1.047; Z_all-sky = 5.215. Thresholds: FAIL if p_het > 0.3173; PASS if p_het ≤ 0.00270, Z ≥ 3 and Holm survives.

Raw outcome: FAIL. **T6 verdict: FAIL.**

## 7. Multiple-testing correction (PREREG §3.2, Holm–Bonferroni over T1-L1, T4b, T6)

| Rank | Test | p | α_(m) | p > α? |
|---|---|---|---|---|
| 1 | T6 | 0.347838 | 0.01667 | yes |
| 2 | T1-L1 | 1.000000 | 0.02500 | yes |
| 3 | T4b | 1.000000 | 0.05000 | yes |

m* = 1. Raw PASS outcomes at rank ≥ m* are downgraded to INCONCLUSIVE. Final: T6: FAIL, T1-L1: INCONCLUSIVE, T4b: INCONCLUSIVE.

## 8. Model-level verdict (PREREG §3.3)

Pillars: T1-L1 = INCONCLUSIVE, T2-A = INCONCLUSIVE, T4b = INCONCLUSIVE, T5-A = FAIL.

**MODEL FALSIFIED (FAIL)**

Robustness of the model-level verdict to the two logged interpretive alternatives (computed mechanically; only the first row is deciding):

| T4b reading (D10/D12) | T5 gate reading (D11) | T1-L1 | T2-A | T4b | T5-A | Model-level verdict |
|---|---|---|---|---|---|---|
| deciding (row 13 accepted) | deciding (literal) | INCONCLUSIVE | INCONCLUSIVE | INCONCLUSIVE | FAIL | MODEL FALSIFIED (FAIL) |
| deciding (row 13 accepted) | alternative (G9-b invalidates f_leak) | INCONCLUSIVE | INCONCLUSIVE | INCONCLUSIVE | INCONCLUSIVE | MODEL INCONCLUSIVE (NOT FALSIFIED, NOT SUPPORTED) |
| alternative (row 13 rejected) | deciding (literal) | INCONCLUSIVE | INCONCLUSIVE | FAIL | FAIL | MODEL FALSIFIED (FAIL) |
| alternative (row 13 rejected) | alternative (G9-b invalidates f_leak) | INCONCLUSIVE | INCONCLUSIVE | FAIL | INCONCLUSIVE | MODEL FALSIFIED (FAIL) |

## 9. Method choices (independent route, REBUILD_RULES)

- Background: flat E(a) with photons, 2 massless + 1 massive (0.06 eV, exact Fermi–Dirac shape) neutrinos, N_eff = 3.044, Ω_bc = Ωm − Ω_ν,0; Law 1 ln g(a) via classical RK4 on the registered 1000-point log-a grid.
- Distances: fixed-step RK4 ODE for χ(z) on a uniform z grid (dz = 0.0025, z ≤ 2.5) with cubic Hermite interpolation, plus RK4 on a ln(1+z) grid to z*. Cross-checked against scipy solve_ivp (DOP853) and Gauss–Legendre quadrature (`results_rebuild/validation/cosmo_validation.json`; max fractional difference 4e-12 ΛCDM, 3e-12 CPL, 7e-7 Law 1).
- Sound horizon: RK4 in a; z* from Hu & Sugiyama (1996); z_d from Eisenstein & Hu (1998); r_d = F·r_s(z_d) with one CAMB 2.0.5 calibration constant F = 0.975772, computed once outside any loop (D3).
- Sampler: own 8-chain adaptive-then-frozen random-walk Metropolis (D4). Convergence: split-R̂−1 < 0.01 (classic and rank-normalised), bulk ESS > 1000 per parameter, burn-in ≥ max(1000, 5τ), ≥ 128,000 production samples. χ²_min: registered Nelder–Mead + L-BFGS-B from the 5 best samples. Seeds: SEED = 20261030; run i (sorted name order) uses SEED + 1000·i; Monte Carlo checks use SEED.
- SN likelihoods: analytic marginalisation over M; d^T W d evaluated as |L^T d|² with W = L L^T (performance change logged before any SN fit; identical to 4e-9 in χ²).
- Rotation-curve kernel: closed form, validated against scipy ncx2 (G9-d) and a direct 3D Monte Carlo.
- T6: own HEALPix Nside=1 RING ang2pix, asserted equal to astropy-healpix for every SN; GLS regional fits.
- Parallelism: 14 worker processes (single-threaded BLAS, BELOW_NORMAL priority), leaving ≥ 4 threads free.

## 10. NON-DECIDING sensitivity analyses (can never change any verdict)

### 10.1 T1 variants (A, B per SN run; outcome under the per-run rule)

| Variant | SN | A | B | per-run outcome | w0_fit |
|---|---|---|---|---|---|
| wCDM-column CMB prior (D7) | Pantheon+ | -1.5221 | 5.0475 | INCONCLUSIVE | -0.9635 |
| wCDM-column CMB prior (D7) | DES-Dovekie | -2.2981 | 6.8880 | INCONCLUSIVE | -0.9584 |
| Lyα r = 0 | Pantheon+ | -1.5019 | 4.7360 | INCONCLUSIVE | -0.9635 |
| Lyα r = 0 | DES-Dovekie | -2.2559 | 6.5512 | INCONCLUSIVE | -0.9585 |
| unmodified desi_bao_dr2 Lyα row | Pantheon+ | -1.6793 | 5.2245 | INCONCLUSIVE | -0.9614 |
| unmodified desi_bao_dr2 Lyα row | DES-Dovekie | -2.4941 | 7.1698 | INCONCLUSIVE | -0.9564 |

### 10.2 T2-A variants and T2-B

| Variant | SN | Ω_bc | R_pred | σ_comb | (R_pred − 5.36)/σ_comb |
|---|---|---|---|---|---|
| Cooke+18 BBN prior | Pantheon+ | 0.31557 | 4.9959 | 0.1284 | -2.836 |
| Cooke+18 BBN prior | DES-Dovekie | 0.31806 | 5.0432 | 0.1243 | -2.549 |
| marginal (R, ℓ_A) block | Pantheon+ | 0.31219 | 4.9317 | 0.1276 | -3.356 |
| marginal (R, ℓ_A) block | DES-Dovekie | 0.31391 | 4.9642 | 0.1223 | -3.235 |
| Lyα r = 0 | Pantheon+ | 0.31089 | 4.9069 | 0.1344 | -3.372 |
| Lyα r = 0 | DES-Dovekie | 0.31320 | 4.9509 | 0.1309 | -3.127 |
| unmodified Lyα row | Pantheon+ | 0.30987 | 4.8874 | 0.1336 | -3.536 |
| unmodified Lyα row | DES-Dovekie | 0.31213 | 4.9305 | 0.1297 | -3.312 |
| T2-B (ω_b = h²/19) | Pantheon+ | 0.32166 | 5.1115 | 0.1305 | -1.905 (Δχ²_min vs w0waCDM = 11.680) |
| T2-B (ω_b = h²/19) | DES-Dovekie | 0.32264 | 5.1301 | 0.1296 | -1.773 (Δχ²_min vs w0waCDM = 13.423) |

T2-B outcome if it were deciding: FAIL.

### 10.3 T2-N2 alternative ω_b inputs

- desi_bbn: H0_pred = 64.917 ± 0.805; -2.521σ vs Planck; -3.546σ vs DESI+BBN 68.52 ± 0.62.
- cooke: H0_pred = 64.151 ± 0.281; -5.269σ vs Planck; -6.416σ vs DESI+BBN 68.52 ± 0.62.

### 10.4 T4b

- Monte Carlo age-posterior-weighted accuracy at τ̂_lag (20,000 draws): train mean 0.510; test n/a (no classified test cluster).
- Row 13 'galaxies' row rejected (D10/D12 alternative): n_train = 0, n_test = 0, outcome FAIL.
- Secondary position sources (Ragozzine+12, Jee+14 P3, Clowe+12, Rau+14) and system-level classification: extractions in `t4b_extraction/cluster_*_sec_*.json`; T4a (EXPLORATORY) not scored.

### 10.5 T5

- T5-A_total_chi2: best = 8.16783, held-out median χ²_red = 41.8426, F(<2) = 0.0575, outcome if deciding = FAIL.
- T5-A_median_red: best = 1.32246, held-out median χ²_red = 59.5188, F(<2) = 0.0920, outcome if deciding = FAIL.
- T5-B_total_chi2: best = 3.26213, held-out median χ²_red = 28.3502, F(<2) = 0.0690, outcome if deciding = FAIL.
- T5-B_median_red: best = 2.12269, held-out median χ²_red = 23.0358, F(<2) = 0.0805, outcome if deciding = FAIL.
- T5-A held-out quality subset (Q ∈ {1, 2}, i ≥ 30°): n = 75, median χ²_red = 56.7927, F(<2) = 0.0267.
- Saturation-cap diagnostic: g_bar cap = 4.128e-12 m/s²; fraction of SPARC radial points below the cap = 0.1277; fraction of galaxies with any point below = 0.4114.

### 10.6 T6

- equatorial: N_pix = 11, χ²_het = 14.771 (dof 10), p_het = 0.14062, H̄0 = 73.501 ± 1.047, Z_all-sky = 5.213, outcome INCONCLUSIVE.
- zCMB: N_pix = 9, χ²_het = 14.809 (dof 8), p_het = 0.06297, H̄0 = 73.044 ± 1.041, Z_all-sky = 4.846, outcome INCONCLUSIVE.
- drop_without_merging: N_pix = 9, χ²_het = 8.612 (dof 8), p_het = 0.37607, H̄0 = 73.541 ± 1.048, Z_all-sky = 5.241, outcome FAIL.

### 10.7 Coincidence-window diagnostic (PREREG §6)

- f_leak=0.166667: H-Abs: Δt = 2.2545 Gyr (z -0.077–0.078); H-Rel: Δt = 0.8853 Gyr (z -0.019–0.043)
- f_leak=0.182146: H-Abs: Δt = 2.2824 Gyr (z -0.085–0.070); H-Rel: Δt = 0.7503 Gyr (z -0.019–0.033)
- t0 = 13.7949 Gyr. Planck 2018 base LCDM shares; dark-matter share = Omega_m,tot - Omega_b (massive nu counted with matter).

## 11. Convergence of every MCMC run

| Run | converged | R̂_max − 1 | ESS_min | production steps / chain | χ²_min |
|---|---|---|---|---|---|
| G9a_lcdm_BAOstd | yes | 5.5315e-04 | 10806 | 16000 | 10.2810 |
| G9b_lcdm_CMB | yes | 9.6326e-04 | 10588 | 16000 | 2.835e-10 |
| G9c_cpl_BAOstd_CMB_D | yes | 0.00192 | 5796 | 16000 | 1638.5993 |
| S_T1LyaStd_cpl_D | yes | 0.00309 | 6038 | 16000 | 1638.5993 |
| S_T1LyaStd_cpl_P | yes | 0.00215 | 6363 | 16000 | 1395.8085 |
| S_T1LyaStd_law1_D | yes | 0.00135 | 8490 | 16000 | 1645.7690 |
| S_T1LyaStd_law1_P | yes | 7.4751e-04 | 8399 | 16000 | 1401.0330 |
| S_T1LyaStd_lcdm_D | yes | 5.6958e-04 | 12052 | 16000 | 1648.2631 |
| S_T1LyaStd_lcdm_P | yes | 5.1126e-04 | 11342 | 16000 | 1402.7123 |
| S_T1r0_cpl_D | yes | 0.00122 | 6191 | 16000 | 1640.8314 |
| S_T1r0_cpl_P | yes | 0.00127 | 6195 | 16000 | 1397.8973 |
| S_T1r0_law1_D | yes | 0.00111 | 8359 | 16000 | 1647.3826 |
| S_T1r0_law1_P | yes | 0.00111 | 8406 | 16000 | 1402.6333 |
| S_T1r0_lcdm_D | yes | 3.8860e-04 | 12073 | 16000 | 1649.6386 |
| S_T1r0_lcdm_P | yes | 5.9123e-04 | 11874 | 16000 | 1404.1352 |
| S_T1wcdm_cpl_D | yes | 0.00124 | 6040 | 16000 | 1640.0199 |
| S_T1wcdm_cpl_P | yes | 0.00134 | 5697 | 16000 | 1397.1046 |
| S_T1wcdm_law1_D | yes | 0.00130 | 9088 | 16000 | 1646.9079 |
| S_T1wcdm_law1_P | yes | 0.00177 | 8770 | 16000 | 1402.1521 |
| S_T1wcdm_lcdm_D | yes | 0.00110 | 12073 | 16000 | 1649.2060 |
| S_T1wcdm_lcdm_P | yes | 4.5216e-04 | 12436 | 16000 | 1403.6741 |
| S_T2A_LyaStd_D | yes | 0.00171 | 3889 | 16000 | 1638.5923 |
| S_T2A_LyaStd_P | yes | 0.00267 | 3714 | 16000 | 1395.5700 |
| S_T2A_cooke_D | yes | 7.8480e-04 | 6199 | 16000 | 1645.3981 |
| S_T2A_cooke_P | yes | 0.00172 | 5004 | 16000 | 1403.4456 |
| S_T2A_marg_D | yes | 0.00109 | 6144 | 16000 | 1639.9680 |
| S_T2A_marg_P | yes | 0.00156 | 5883 | 16000 | 1397.1175 |
| S_T2A_r0_D | yes | 0.00144 | 4273 | 16000 | 1640.9007 |
| S_T2A_r0_P | yes | 0.00219 | 4610 | 16000 | 1397.7976 |
| S_T2B_D | yes | 0.00180 | 5728 | 16000 | 1653.6284 |
| S_T2B_P | yes | 0.00133 | 5822 | 16000 | 1408.8882 |
| T1_cpl_D | yes | 0.00161 | 6318 | 16000 | 1640.1409 |
| T1_cpl_P | yes | 0.00130 | 6522 | 16000 | 1397.2933 |
| T1_law1_D | yes | 0.00103 | 8761 | 16000 | 1647.6161 |
| T1_law1_P | yes | 0.00136 | 8243 | 16000 | 1402.8397 |
| T1_lcdm_D | yes | 8.3365e-04 | 11646 | 16000 | 1649.6947 |
| T1_lcdm_P | yes | 7.0037e-04 | 11598 | 16000 | 1404.1852 |
| T2A_D | yes | 0.00225 | 4496 | 16000 | 1640.2052 |
| T2A_P | yes | 0.00241 | 4173 | 16000 | 1397.2078 |

## 12. Provenance, hand-over and blindness record

- Frozen package: all 9 present files listed in PREREG_v4.sha256 match (no `_ORIGINALS` folder exists; see D1).
- Data: DATA_MANIFEST_REBUILD.sha256 (13 files, SHA-256 38b0b0bf…409d) was OTS-stamped at 06:28:55, before any fit. DATA_MANIFEST_REBUILD_PAPERS.sha256 (SHA-256 e3cc5c08…8faa) was OTS-stamped at 07:30, before T4b was computed.
- Hand-over: the previous agent session stopped while the 06:40 batch of fits was still running. A new session re-verified the earlier work, logged the hand-over, and reran the 37 unfinished fits with unchanged seeds (ACTIVITY_LOG_REBUILD.md).
- Blindness: nothing outside this folder was read. One accidental exposure is logged: a process listing showed the command line of an original-analysis script (name only). No original code, log, manifest or result was seen.

## 13. DEVIATIONS_REBUILD.md (verbatim)

## DEVIATIONS_REBUILD.md

Every departure from the frozen package, and every interpretation the rulebook left open, is logged here
BEFORE the affected test is computed. Each entry gives what, why, the expected effect, and when it was logged.

---

### D1 — `_ORIGINALS` subfolder does not exist (package verification)
- **What:** REBUILD_RULES.md says to hash the files in `_ORIGINALS`, but this workspace has no such folder. The frozen files are in the workspace root instead. They were verified there against PREREG_v4.sha256, and all 9 files present match.
- **Why:** Workspace layout as delivered.
- **Expected effect:** None. The hashes match byte-for-byte, and the root copies are treated as read-only originals.
- **Logged:** 2026-10-30T06:19:31-04:00.

### D2 — Gate G9-b reference values: "Chen, Huang & Wang (2019) Table 2" does not exist
- **What:** PREREG.md §2 G9-b says to reproduce the flat-ΛCDM posteriors (Ωm, h, ωb) in "their Table 2" to within 0.3σ. The paper (arXiv:1808.05724, e-print read 2026-10-30T10:25Z) has only one table: Table 1, the distance priors and correlation matrices. Its ΛCDM parameter check is a figure (`lcdm.pdf`, Fig. "Constraints on parameters in the base ΛCDM model"). That figure compares the distance-prior contours with the Planck 2018 `base_plikHM_TTTEEE_lowl_lowE` chains, which are the chains the priors were compressed from.
- **Substitute (single, fixed before the gate is run):** the gate benchmark is the Planck 2018 VI (A&A 641, A6, arXiv:1807.06209) **Table 2, "TT,TE,EE+lowE" column**. This is the same likelihood and chains that Chen et al. compressed and compared against:
  - Ωm = 0.3166 ± 0.0084
  - H0 = 67.27 ± 0.60, i.e. h = 0.6727 ± 0.0060
  - Ωb h² = 0.02236 ± 0.00015
  - The 0.3σ tolerance is unchanged: |ΔΩm| ≤ 0.00252, |Δh| ≤ 0.00180, |Δωb| ≤ 0.000045.
  - The compared statistic is the posterior mean of each parameter.
- **Why:** The registered reference cannot be read off a table, and digitising a figure would add an unregistered free choice. Planck Table 2 TT,TE,EE+lowE is what the Chen et al. figure overlays, so it is the closest published numerical benchmark.
- **Expected effect:** If the compressed prior plus the registered theory computation reproduces Planck, the gate passes. A failure would make T1-L1, T1-Sign, T2-A and T2-B INCONCLUSIVE, per the registered mapping.
- **Note (diagnostic only, recorded before the gate run):** The registered theory computation uses the HS96 z* fit, the registered E(a) with photons, 3.044 neutrinos and one massive ν, and the r_s integral. At the Planck best-fit parameters it gives ℓ_A ≈ 302.07, versus the prior mean 301.471. Our D_M(z*) agrees with CAMB 2.0.5 to 3×10⁻⁶ and our r_s(z*) to 5×10⁻⁵, so this is not an implementation bug. The offset comes from the registered z*/ℓ_A convention relative to how the published prior mean was derived. No change is made: the registered equations are used as written, and the gate decides.
- **Logged:** 2026-10-30T06:37:06-04:00 (before G9-b was computed).

### D3 — r_d: interpretation of "EH98 z_d calibrated to CLASS/CAMB via the standard post-Planck drag-scale factor"
- **What:** r_d = F × r_s(z_d^EH98), where r_s is the registered sound-horizon integral at the registered EH98 z_d.
  - F is one constant, computed once with CAMB 2.0.5 at the Planck 2018 TT,TE,EE+lowE+lensing mean cosmology (ωb = 0.02237, ωc = 0.1200, H0 = 67.36, Σmν = 0.06 eV in one massive state, N_eff = 3.044): F = r_drag(CAMB)/r_s(z_d^EH98) = 147.1027/150.7552 = **0.975772**.
  - CAMB is never called inside a sampling loop.
  - Validation against CAMB over a 6×5×3 grid (ωb 0.020–0.025, ωc 0.10–0.14, h 0.60/0.6736/0.75): maximum |fractional error| is 0.13% over the whole grid and 0.043% within ±0.0011 in ωb and ±0.011 in ωc of the fiducial (`results_rebuild/validation/rd_calibration.json`).
- **Why:** The rulebook does not define the "drag-scale factor" numerically. A single multiplicative CAMB calibration of r_d is the most literal reading. It keeps the registered fast method, and the REBUILD_RULES allow one-off Boltzmann calibration outside the loop.
- **Expected effect:** At most 0.04% in r_d over the posterior region, which is about 0.05σ of the most precise DESI BAO point. Negligible.
- **Logged:** 2026-10-30T06:37:06-04:00 (before any BAO+CMB fit).

### D4 — Sampler: rebuild's own sampler instead of emcee with 32 walkers
- **What:** PREREG §4 names emcee with 32 walkers. REBUILD_RULES.md says samplers are the rebuild's own choice. I used my own multi-chain sampler:
  - 8 independent chains, started from dispersed points.
  - Random-walk Metropolis. The proposal covariance is adapted for 4,000 steps per chain, its scale is tuned to 20–35% acceptance, and then both are frozen. Burn-in is 3,000 steps with the frozen proposal, extended if needed so that it is at least max(1000, 5τ).
  - Production runs in blocks of 4,000 steps per chain. It stops only when classic split-R̂ − 1 < 0.01, rank-normalised split-R̂ − 1 < 0.01, bulk ESS > 1000 for every parameter, and total production ≥ 128,000 samples (the registered production minimum).
  - Maximum extension is 80,000 production steps per chain. Not meeting the criteria by then is the registered G8 non-convergence trigger.
  - χ²_min uses the registered optimiser exactly: Nelder–Mead (xatol = fatol = 1e-6, maxiter = 10,000) from the 5 highest-likelihood MCMC samples, then bounded L-BFGS-B (ftol = 1e-12).
  - Seeds: master SEED = 20261030; the run with sorted index i uses SEED + 1000·i.
- **Why:** Independence by design (REBUILD_RULES). Genuinely independent chains also make the Gelman–Rubin statistic meaningful.
- **Expected effect:** Posterior summaries are unchanged apart from Monte Carlo noise. Deciding Δχ² values come from the optimiser, not the sampler.
- **Logged:** 2026-10-30T06:37:06-04:00.

### D5 — Hardware and environment
- **What:**
  - Up to 24 worker processes on a 28-thread machine, set by the REBUILD_RULES instruction to leave about 4 threads free. The registered cap is 12.
  - Each worker runs single-threaded BLAS at BELOW_NORMAL priority, as registered.
  - The venv is local (`d:\Blind_Rebuild\.venv`, Python 3.14.7) with the registered pins numpy == 2.5.4 and scipy == 1.18.1; the registered path D:\Argon_Code\... is not used.
- **Why:** Blindness rules and REBUILD_RULES.
- **Expected effect:** None on any number.
- **Logged:** 2026-10-30T06:37:06-04:00.

### D6 — Second data manifest for literature sources
- **What:** DATA_MANIFEST_REBUILD.sha256 was written and OTS-stamped at 06:28:55, before any fit. It covers the registered datasets plus the Chen 2019 and Planck 2018 e-prints and the DES-Dovekie format documentation. The T4b position-source papers were still being downloaded by sub-agents at that time. They are fingerprinted in a second manifest, DATA_MANIFEST_REBUILD_PAPERS.sha256, which is OTS-stamped before the T4b classification is computed.
- **Why:** Stamping must precede fits, and the cosmology fits do not depend on the papers.
- **Expected effect:** None.
- **Logged:** 2026-10-30T06:37:06-04:00.

### D7 — wCDM-column CMB prior sensitivity (NON-DECIDING): errors and correlations
- **What:** PREREG gives only the wCDM mean vector (1.7493, 301.462, 2.239). For this non-deciding run I use the wCDM column's own Table 1 errors, symmetrised: R ± 0.00465 (from +0.0046/−0.0047), ℓ_A ± 0.0895 (from +0.089/−0.090), ωb ± 0.00015. I also use that column's correlation matrix (0.47, −0.66, −0.34).
- **Why:** These are the values the rulebook leaves unstated.
- **Expected effect:** Sensitivity only.
- **Logged:** 2026-10-30T06:37:06-04:00.

### D8 — Recorded interpretations (no departure intended)
1. The sampled Ωm is Ωm,tot (baryons + CDM + massive ν today). Ω_ν,0 = 0.06/(93.14 h²) and Ωbc = Ωm − Ω_ν,0. Flatness is closed by Ω_de = 1 − Ω_r − Ωm.
2. Neutrinos: two massless species plus one 0.06 eV species with the exact Fermi–Dirac energy-density shape F(m a/kT_ν)/a⁴. T_ν0 = (4/11)^{1/3}(3.044/3)^{1/4} T_CMB. The amplitude is normalised so the massive species equals the registered Ω_ν,0 today.
3. Pantheon+: μ_model = 5 log10[(1+z_HEL) D_M(z_HD)/Mpc] + 25, compared with `m_b_corr`. Cut: z_HD > 0.01 and IS_CALIBRATOR == 0, giving 1580 SNe. The STAT+SYS covariance sub-block is used.
4. DES-Dovekie: all 1820 SNe in DES-Dovekie_HD.csv, `MU` with the full STAT+SYS inverse covariance (as distributed) and the same μ_model.
5. In both SN samples M is marginalised analytically: χ² = ΔᵀWΔ − (1ᵀWΔ)²/(1ᵀW1). The constant ln term is dropped; it cancels in every Δχ².
6. Gate statistics use the posterior mean.
7. Law-1 g(a): RK4 on the registered 1000-point log-a grid over a ∈ [10⁻⁴, 1]. ln g is held constant for a < 10⁻⁴, where |d ln g/d ln a| = 3γ/E < 10⁻⁵.
8. T2-B (non-deciding): ωb = h²/19 is imposed and the registered 100ωb ∈ [1.8, 2.6] bound is kept. Its Δχ² reference is the T2-A w0waCDM fit on the same datasets.
- **Logged:** 2026-10-30T06:37:06-04:00.

### D9 — Gate G9-d: the registered unit-test script is not available
- **What:** G9-d refers to the kernel "implemented in `verify_b1_kernel_mc.py`". That file belongs to the original analysis and must not be used. I test my own implementation of the registered piecewise kernel on the registered 5×7 grid against `scipy.stats.ncx2.cdf((r/σ)², df=3, nc=(r'/σ)²)`, with absolute tolerance < 1e-10, under numpy 2.5.4 and scipy 1.18.1. The r'/σ = 1e-5 column uses the point-mass branch, as registered. The ncx2 reference at nc = 0 is evaluated as ncx2 with nc = 0.0 if scipy accepts it; otherwise as `chi2.cdf(x, 3)`, which is mathematically identical, and that fallback would be logged.
- **Why:** Blindness rules.
- **Expected effect:** None.
- **Logged:** 2026-10-30T06:37:06-04:00.

### D10 — T4b: mechanical decisions on the extracted position data (logged before the T4b statistic was computed)
These decisions apply the pre-written t4b_extraction/EXTRACTION_PROTOCOL.md (06:23:48) to what the 16 registered source papers contain. Extraction details are in t4b_extraction/cluster_NN.json and cluster_NN_notes.md.
1. **What counts as x_S.** A galaxy position counts as the "luminosity-weighted galaxy centroid" only if the paper calls it a centre or centroid of the galaxy light (luminosity) distribution. Positions the paper explicitly calls a "peak" of a smoothed (luminosity-weighted) density map do not count: Abell 1240 Table 2, MACS J1149 §3.2, ZwCl 0008 Table 3, El Gordo, and the Toothbrush "luminosity peak". For those clusters the BCG fallback applies.
2. **MACS J0025.4-1222 (row 13), Bradač et al. 2008.** The Table 2 "galaxies" rows are introduced in §4.3 as "the centers of the light distributions (galaxies). The measured positions and error bars are given in Table 2". They are read as the luminosity-weighted galaxy centre, with 1σ errors from the Table 2 caption.
   - The X-ray peak error is the Table 2 per-axis 1σ value, ±0.08′. The text separately calls it a top-hat bound of "within 5 arcsec"; the tabulated 1σ value is used.
   - **This decision matters for the verdict.** Row 13 is the only cluster for which all three positions and their uncertainties are available. If the "galaxies" row were rejected, n_train = 0 and T4b would end in FAIL under clause 1(a). Both outcomes are reported; the alternative goes in the NON-DECIDING section.
3. **Positions given as offsets.** Positions given as tabulated (Δx, Δy) offsets from a reference point (row 13) or as stated separations are accepted, because only d_IG and d_IS are needed (protocol).
4. **Errors on separations.** An error quoted on a separation (for example "22 ± 12″" between I and G for Abell 2744, or "57 (+36/−34)″" between I and S for Abell 2034) is not a per-position σ_c. A cluster missing a per-position σ for any of I, G or S, with no instrument centroiding error stated in its text, is marked "unclassified" by the registered missing-data rule. No secondary literature is used to fill gaps.
5. **Asymmetric per-axis errors.** Where a position has asymmetric per-axis errors, each axis uses the mean of the + and − errors, followed by the registered quadrature rule σ_c = sqrt((σ_α*² + σ_δ²)/2). RA errors printed in seconds of time are converted with 15″ cos δ per second.
6. **Subcluster as designated.** The designated subcluster is used as named in the PREREG table. For Abell 2744 the "Core/NW" designation is ambiguous; Core is the primary record and NW is reported as a sensitivity. Neither is classifiable, because G and S lack per-position errors.
- **Logged:** 2026-10-30T06:42:10-04:00.

### D11 — T5 dependence on gates G9-a / G9-b (interpretation, logged before T5 is computed)
- PREREG §2 G9 says gates G9-a/G9-b map to T5 "only if T2-A-Pantheon+ fails to produce a converged f_leak because G9-a or G9-b failed". I read this literally. If the T2-A-Pantheon+ chain converged, the frozen f_leak exists and T5-A/T5-B/T5c are evaluated with it, whatever the outcome of G9-a/b. T5 becomes INCONCLUSIVE by this route only if the T2-A-Pantheon+ run did not converge.
- If a G9-a/b gate fails, the alternative reading (T5 INCONCLUSIVE) is stated next to the T5 verdict.
- **Logged:** 2026-10-30T06:42:10-04:00.

### D12 — Hand-over review of D10 item 2 (row 13 galaxy position); no change made
- **What:** The new agent independently re-checked row 13 against the e-print (`data/papers/bradac2008_macs0025/src_D/ms.tex`, which is byte-identical to the archived e-print). The Table 2 values in t4b_positions_rebuild.json are transcribed correctly.
- **Finding:** The reading is open to doubt.
  - The Table 2 caption reads "Offsets (with 1σ errorbars) of the mass peaks and gas peaks".
  - The only luminosity distribution the paper describes (§6) is a K-band map "smoothed with a Gaussian kernel with FWHM 80 kpc".
  - The wording "centers of the light distributions (galaxies)" (§4.3) is therefore compatible with the "galaxies" row being the peak of a smoothed luminosity map. D10 item 1 does not accept that kind of position for other clusters.
  - The paper never explicitly says "luminosity-weighted".
- **Decision:** D10 item 2 is kept exactly as logged at 06:42:10. It was fixed under the pre-written protocol before any T4b statistic was computed. Re-deciding it now, when its consequence is known, would itself be a post-hoc choice.
  - The alternative reading (row 13 unclassified → n_train = 0 → T4b FAIL by clause 1(a)) is reported next to the T4b verdict in REBUILD_RESULTS.md with equal prominence, not only in the NON-DECIDING section.
- **Expected effect:** None on the computation. It makes clear that the T4b pillar verdict rests on this one interpretive call.
- **Logged:** 2026-10-30T07:30:05-04:00 (before the T4b statistic is computed).

