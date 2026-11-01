---
title: "MULTIVERSE Datasets, v1"
subtitle: "Public data that can fix or test the Mandarano Model"
author: "Gregory Mandarano / WickedAI"
date: "Version 1.0.1, October 2026"
---

**License:** CC BY 4.0 (this list). Each dataset keeps its own license and citation requirements; cite the original teams when you use their data.

# How to use this list

This folder links to data; it does not copy it. Each entry gives the official source, what the data constrain, which of the paper's predictions (P1 to P9) and parameters it bears on, and its role in the pre-registered tests (MULTIVERSE_TESTS_v1.md): whether it **fixes** a parameter, **tests** one, or both in different tests. A dataset used to fix a parameter is never also used to test that same parameter (one partial overlap is registered and stated plainly: Planck in T2, see MULTIVERSE_TESTS_v1.md).

Parameter names, shared across the package: $N_s$ (19 strings per strand), $N_r$ (133 strings per rope), $f_{\rm leak}$ (fraction of the touching neighbors' pull lost in transit and stored as outer-ring tension), $\epsilon_{\rm far}$ (far-string contribution), $w_0$, $w_a$ (CPL dark energy parameters), $\tau_{\rm lag}$ (shadow crossing delay), $\sigma_{\rm ref}$ (refraction spreading width).

Links were checked in October 2026. Release versions change; always record the exact version, file names and download date you used.

# Summary table

| Dataset | Constrains | Predictions | Parameters | Role in tests |
|---|---|---|---|---|
| DESI DR2 BAO | Expansion history $D_M/r_d$, $D_H/r_d$, $D_V/r_d$, $0.1 < z < 4.2$ | P1, P3, P6, P7 | $w_0$, $w_a$, $f_{\rm leak}$ | Tests $w_0, w_a$ (T1); fixes $f_{\rm leak}$ through $\Omega_m$ (T2) |
| DESI DR2 Lyman-alpha (BAO and AP, incl. arXiv:2607.27410) | High-redshift expansion at $z_{\rm eff} \approx 2.33$ | P1 | $w_0$, $w_a$ | Part of the T1 test set |
| Planck 2018 | Early-universe densities $\Omega_b h^2$, $\Omega_c h^2$; $H_0$ under $\Lambda$CDM; acoustic scale | P1, P3, P7 | $f_{\rm leak}$ | Tests $f_{\rm leak}$ through $\omega_c/\omega_b$ (T2); its compressed distance priors $R$, $\ell_A$ enter the T2 fix; CMB prior in T1 |
| Compressed CMB distance priors (Chen, Huang & Wang 2019) | $R$, $\ell_A$, $\omega_b$ from Planck 2018 | P3 | $f_{\rm leak}$ | $R$ and $\ell_A$ only, in the T2 fix |
| BBN deuterium (Cooke, Pettini & Steidel 2018) | Baryon density $\omega_b$ from primordial deuterium | P3 | $f_{\rm leak}$ | $\omega_b$ prior in the T2 fix |
| Pantheon+ | Relative distances from 1550 Type Ia supernovae | P1, P3, P7 | $w_0$, $w_a$, $f_{\rm leak}$ | Part of the T1 test set and of the T2 fix (one SN sample at a time) |
| DES SN 5-year (and DES-Dovekie) | Relative distances from about 1600 DES supernovae plus low-z | P1, P3 | $w_0$, $w_a$, $f_{\rm leak}$ | Alternative SN sample in T1 and in the T2 fix |
| SPARC | Rotation curves and baryonic mass models, 175 disk galaxies | P5, P8 | $\sigma_{\rm ref}$ | Fixes on a training half, tests on a held-out half (T5) |
| Harvey et al. 2015 | Star, gas and lensing-mass offsets in 72 collisions in 30 systems | P4 | $\tau_{\rm lag}$ | Tests offset sign (T4a) |
| Wittman, Golovich & Dawson 2018 | Re-measured offsets for the same kind of sample | P4 | $\tau_{\rm lag}$ | Cross-check of T4a |
| Merging Cluster Collaboration (Golovich et al. 2019a, b) | Spectroscopy, substructure and merger geometry of 29 radio-relic mergers; dynamical ages | P4 | $\tau_{\rm lag}$ | Supplies merger ages for T4b |
| Bullet Cluster (Clowe et al. 2006; Markevitch et al. 2002) | Lensing mass with galaxies; time since core passage 0.1 to 0.2 Gyr | P4 | $\tau_{\rm lag}$ | Fixes the lower bound on $\tau_{\rm lag}$ (T4b) |
| LZ | Direct-detection rate of nuclear recoils in liquid xenon | P2 | none | Tests P2 (T3) |
| SH0ES | Local $H_0$ from Cepheid-calibrated supernovae | P7 | none (local reading) | Tests P7 (T6) |

# Expansion history and dark energy

## DESI DR2 BAO

- **What it is:** baryon acoustic oscillation distances from the first three years of the Dark Energy Spectroscopic Instrument (more than 14 million galaxies and quasars).
- **Reference:** DESI Collaboration 2025, "DESI DR2 Results II: measurements of baryon acoustic oscillations and cosmological constraints," Physical Review D 112, 083515, arXiv:2503.14738.
- **Official links:** DESI data releases, https://data.desi.lbl.gov/doc/releases/ (DR1 is the latest full public spectroscopic release; DR2 cosmology products and chains are linked from this page). Ready-to-use DR2 BAO mean vectors and covariances are distributed in the `desi_bao_dr2` folder of the Cobaya BAO data repository, https://github.com/CobayaSampler/bao_data.
- **Constrains:** the expansion rate and distance scale relative to the sound horizon; combined with a CMB prior, $\Omega_m$, $H_0 r_d$ and the CPL parameters $w_0$, $w_a$.
- **Published status (Tier 1):** DESI plus CMB prefers $w_0 > -1$, $w_a < 0$ over $\Lambda$CDM at 3.1 $\sigma$; 2.8 to 4.2 $\sigma$ with supernovae, depending on the sample.
- **Tests and fixes:** tests P1 (weakening); fixes $f_{\rm leak}$ through $\Omega_m$ for the P3 ratio test (T2, with the compressed CMB priors, supernovae and a BBN prior); P6, P7.

## DESI DR2 Lyman-alpha forest

- **What it is:** BAO from the Lyman-alpha forest of more than 820,000 quasar spectra at $z_{\rm eff} = 2.33$, and the July 2026 Alcock-Paczyński measurement from the same data.
- **References:** DESI Collaboration 2025, "DESI DR2 Results I: baryon acoustic oscillations from the Lyman alpha forest," arXiv:2503.14739. DESI Collaboration 2026, "DESI DR2 Results IV: Alcock-Paczyński measurements from the Lyman alpha forest and cosmological constraints," arXiv:2607.27410 (submitted 29 July 2026).
- **Official links:** https://arxiv.org/abs/2607.27410 and https://data.desi.lbl.gov/doc/releases/.
- **Constrains:** $D_H/r_d$ and $D_M/r_d$ at high redshift (the AP paper reports $D_H/r_d = 8.600 \pm 0.066$ and $D_M/r_d = 39.32 \pm 0.33$ jointly with BAO). Its combined analysis reports a preference for evolving dark energy of 2.7 $\sigma$ (DESI plus CMB) and 3.2 $\sigma$ with supernovae, lower than the DR2 BAO paper's figures.
- **Tests:** P1.

## Planck 2018

- **What it is:** the final full-mission cosmic microwave background analysis from the Planck satellite.
- **Reference:** Planck Collaboration 2020, "Planck 2018 results. VI. Cosmological parameters," Astronomy & Astrophysics 641, A6, arXiv:1807.06209.
- **Official links:** Planck Legacy Archive, https://pla.esac.esa.int/ ; parameter chains and tables, https://wiki.cosmos.esa.int/planck-legacy-archive/index.php/Cosmological_Parameters.
- **Constrains:** $\Omega_b h^2 \approx 0.0224$, $\Omega_c h^2 \approx 0.120$, $\Omega_m \approx 0.315$, $H_0 \approx 67.4$ km s$^{-1}$ Mpc$^{-1}$ under $\Lambda$CDM, and the acoustic angular scale to 0.03%. The dark-to-baryon ratio $\omega_c/\omega_b = 0.1200/0.02237 \approx 5.36$ (TT,TE,EE+lowE+lensing) is the test of $f_{\rm leak}$; Planck's $\omega_b$ and $\omega_c$ are never used to fix it.
- **Tests and fixes:** tests $f_{\rm leak}$ (T2); its compressed distance priors $R$ and $\ell_A$ (below) enter the T2 fix, a partial overlap stated in T2's independence caveat; serves as the CMB prior in T1; supplies the early-universe $H_0$ for P7.

## Compressed CMB distance priors

- **What it is:** the Planck 2018 TT,TE,EE+lowE data compressed into the shift parameter $R$, the acoustic scale $\ell_A$ and $\omega_b$, with their correlation matrix.
- **Reference:** Chen, Huang & Wang 2019, "Distance priors from Planck final release," JCAP 02 (2019) 028, arXiv:1808.05724.
- **Official link:** https://arxiv.org/abs/1808.05724 (values and correlation matrix in the paper's tables).
- **Use:** the T2 fix uses the $(R, \ell_A)$ block only, marginalized over $\omega_b$, so that the baryon density comes from BBN rather than from Planck.

## BBN baryon density (primordial deuterium)

- **What it is:** a one percent determination of the primordial deuterium abundance and the baryon density it implies under standard big-bang nucleosynthesis.
- **Reference:** Cooke, Pettini & Steidel 2018, "One percent determination of the primordial deuterium abundance," ApJ 855, 102, arXiv:1710.11129 (headline $100\,\omega_b = 2.166 \pm 0.015 \pm 0.011$).
- **Official link:** https://arxiv.org/abs/1710.11129.
- **Use:** the $\omega_b$ prior in the T2 fix (the two errors added in quadrature, as registered in MULTIVERSE_TESTS_v1.md).

## Pantheon+

- **What it is:** 1701 light curves of 1550 spectroscopically confirmed Type Ia supernovae from 18 surveys, $0.001 < z < 2.26$.
- **References:** Scolnic et al. 2022, ApJ 938, 113, arXiv:2112.03863 (data and light curves); Brout et al. 2022, ApJ 938, 110, arXiv:2202.04077 (cosmology).
- **Official link:** https://github.com/PantheonPlusSH0ES/DataRelease (folders `Pantheon+_Data`, `SH0ES_Data`, and `Cosmology` with likelihood inputs).
- **Constrains:** the shape of the distance-redshift relation, and so $\Omega_m$ and $w_0$, $w_a$ in combination with BAO and CMB.
- **Tests and fixes:** tests P1, P7; one of the two supernova samples in the T2 fix of $f_{\rm leak}$ (separate runs).

## DES Supernova 5-year sample (and the DES-Dovekie recalibration)

- **What it is:** about 1,600 photometrically classified Type Ia supernovae from the Dark Energy Survey plus low-redshift samples.
- **References:** DES Collaboration 2024, ApJL 973, L14, arXiv:2401.02929; Popovic et al. 2026 (DES-Dovekie recalibration), MNRAS, arXiv:2511.07517, which lowers the DES-based preference for evolving dark energy from 4.2 to 3.2 $\sigma$ in combination with CMB and DESI DR2.
- **Official link:** https://github.com/des-science/DES-SN5YR (the distances and covariance matrices are in `4_DISTANCES_COVMAT`; the repository now carries the DES-Dovekie data vector).
- **Constrains:** as Pantheon+. Pantheon+ and DES SN share low-redshift supernovae, so **never combine them in one fit**; use one or the other and report both.
- **Tests and fixes:** tests P1; the other supernova sample in the T2 fix of $f_{\rm leak}$ (separate runs).

## Context only: DES Year 6 clustering and lensing

- **Reference:** DES Collaboration 2026, arXiv:2601.14559. Finds $S_8 = 0.789 \pm 0.012$ under $\Lambda$CDM and $w = -0.981^{+0.021}_{-0.022}$ in $w$CDM when combined with other data.
- **Use in v1:** context for P1 and P6 only. Not part of any pre-registered test in v1.

# Galaxies

## SPARC

- **What it is:** Spitzer Photometry and Accurate Rotation Curves: 175 nearby disk galaxies with 3.6 $\mu$m photometry, HI and H$\alpha$ rotation curves, and Newtonian baryonic mass models.
- **Reference:** Lelli, McGaugh & Schombert 2016, AJ 152, 157, arXiv:1606.09251. Related: the radial acceleration relation, McGaugh, Lelli & Schombert 2016, PRL 117, 201101.
- **Official link:** http://astroweb.cwru.edu/SPARC/ (Table1 galaxy sample; Newtonian mass models with rotation curves and baryonic contributions per radius).
- **Constrains:** the shape and amplitude of the dark contribution to each rotation curve, given the measured baryons.
- **Tests and fixes:** fixes $\sigma_{\rm ref}$ on a pre-declared training half and tests it on the held-out half (T5). Tests P5.

## Dark-matter-poor galaxies (context for Open Problem 3)

- **References:** van Dokkum et al. 2018, Nature 555, 629 (NGC 1052-DF2); van Dokkum et al. 2019, ApJL 874, L5 (NGC 1052-DF4); van Dokkum et al. 2022, Nature 605, 435 (collision origin about 8 Gyr ago).
- **Use in v1:** a stress test listed in the paper's open problems (Open Problem 3), with a pre-registered PASS/FAIL stress check for DF2 in T5 (T5c).

# Merging galaxy clusters

## Harvey et al. 2015

- **What it is:** Hubble lensing and Chandra X-ray measurements of 72 collisions in 30 merging systems, giving offsets between stars, gas and dark mass.
- **Reference:** Harvey, Massey, Kitching, Taylor & Tittley 2015, Science 347, 1462-1465, arXiv:1503.07675. The offset measurements are in the paper's supplementary material (Science) and the arXiv version.
- **Constrains:** the population-average offset between dark mass and stars (published: within $5.8 \pm 8.2$ kpc) and its direction relative to the gas.
- **Tests:** P4, the sign of the dark-mass offset relative to galaxies (T4a).

## Wittman, Golovich & Dawson 2018

- **What it is:** a re-measurement of merging-cluster offsets, which found measurement problems in the earlier analysis and relaxed the self-interaction limit to roughly $\sigma_{\rm DM}/m \lesssim 2$ cm$^2$ g$^{-1}$.
- **Reference:** ApJ 869, 104, arXiv:1701.05877.
- **Tests:** P4; the required cross-check of T4a. A T4a result counts only if it holds in both Harvey et al. and this re-measurement.

## Merging Cluster Collaboration

- **What it is:** a radio-relic-selected sample of 29 merging clusters ($0.07 < z < 0.55$) with Subaru imaging, Keck spectroscopy (4,431 spectroscopic galaxies), substructure and merger geometry.
- **References:** Golovich et al. 2019a, ApJS 240, 39, arXiv:1711.01347; Golovich et al. 2019b, ApJ 882, 69, arXiv:1806.10619. Dynamical ages (collision speed and time since pericenter) for individual systems come from Monte Carlo dynamical modeling such as Dawson 2013, ApJ 772, 131, arXiv:1210.0014.
- **Official link:** https://www.mergingclustercollaboration.org/ (system summaries and data products).
- **Constrains:** time since pericenter and collision speed for systems whose offsets can be compared.
- **Tests:** P4, the age cutoff (T4b).

## Key individual systems

| System | Published age since pericenter | Note | Reference |
|---|---|---|---|
| Bullet Cluster, 1E 0657-558 | 0.1 to 0.2 Gyr | Mass with galaxies; sets $\tau_{\rm lag} > 150$ Myr | Markevitch et al. 2002; Clowe et al. 2006 |
| Musket Ball, DLSCL J0916.2+2951 | at least $0.7 \pm 0.2$ Gyr | Older merger; first check of the age cutoff | Dawson et al. 2012 |
| MACS J0025.4-1222 | see literature | Bullet-like dissociative merger | to be sourced in the test run |
| El Gordo, ACT-CL J0102-4915 | see literature | Massive, high-redshift merger | to be sourced in the test run |
| Abell 520 | disputed | Reported dark core near the gas (Mahdavi et al. 2007; Jee et al. 2012, 2014), not found by Clowe et al. 2012 | see paper, Open Problem 4 |

Ages for MACS J0025 and El Gordo are deliberately left blank in v1: they must be taken from published dynamical analyses, with the source recorded, before the T4b test is run.

# Dark matter detection

## LZ (LUX-ZEPLIN)

- **What it is:** a seven-tonne liquid xenon time projection chamber at the Sanford Underground Research Facility, South Dakota.
- **References:** LZ Collaboration 2025, "Dark matter search results from 4.2 tonne-years of exposure of the LUX-ZEPLIN (LZ) experiment," PRL 135, 011802, arXiv:2410.17036 (no excess over background). On 1 September 2026, LZ announced a single nuclear-recoil event in data from 220 live days (March 2023 to April 2024), with a global significance of about 2.6 $\sigma$; the collaboration states it is not claiming a detection.
- **Official link:** https://lz.lbl.gov/ (results, papers and slides). Announcement summary: https://www.energy.gov/science/articles/lz-sees-surprising-result-search-dark-matter.
- **Constrains:** the rate of dark matter particle interactions with xenon nuclei.
- **Tests:** P2 (T3).

# Local expansion rate

## SH0ES

- **What it is:** the Hubble Space Telescope distance ladder: Cepheids in the hosts of 42 Type Ia supernovae, calibrated by Gaia parallaxes, NGC 4258 masers and LMC eclipsing binaries.
- **Reference:** Riess et al. 2022, ApJL 934, L7, arXiv:2112.04510 ($H_0 = 73.04 \pm 1.04$ km s$^{-1}$ Mpc$^{-1}$).
- **Official link:** https://github.com/PantheonPlusSH0ES/DataRelease (folder `SH0ES_Data`).
- **Constrains:** the local expansion rate, and, with Pantheon+, its possible dependence on direction and environment.
- **Tests:** P7 (T6). Context for the local-void idea: Keenan, Barger & Cowie 2013, ApJ 775, 62.

# Version note

Version 1.0.1 lists data only (it updates the roles in the leak test, T2, and adds the compressed CMB priors and the BBN prior). No file has been downloaded, fitted or tested for this package. The first analysis run should record, for each dataset, the release tag or commit hash and the download date in its output.
