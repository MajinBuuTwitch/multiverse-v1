# Row 06 – Abell 2146, subcluster A2146-A

**Reference check:** Coleman et al. 2017, MNRAS 464, 2469 = arXiv:1609.06765, "The mass distribution of the unusual merging cluster Abell 2146 from strong lensing" (doi:10.1093/mnras/stw2425, checked against Crossref). A first download, arXiv:1609.06734 (King et al. 2016, MNRAS 459, 517, weak lensing), does **not** match the reference and was **not used**.

Source: `data/papers/A2146_Coleman2017_SL/src_clean/abell2146_SL.tex`. z_cl = 0.2323 ("At the redshift of z = 0.2323 ... 1 arcsec = 3.702 kpc").

| Obs | Found? | Value | Uncertainty |
|---|---|---|---|
| I (strong-lensing DM halo A centroid, Lenstool) | yes (abs. deg) | Model 2: 239.05860, 66.348183 | error matrix σ²_RA=0.5, σ²_Dec=0.2, Cov=0.3 ("arcsec") |
| G (X-ray peak/cool core A) | separation only | 30.3 kpc from I (Model 2) | NOT GIVEN |
| S (BCG-A, SExtractor barycentre) | separation only | 1.63 kpc from I (Model 2) | "within an error of 1 pixel" (~0.05″) |

## Verbatim table (label `tblModelResults`)
```
\multicolumn{4}{l}{Mean Position (deg)} \\
RA        & $239\fdg05789$ & $239\fdg05860$ & $239\fdg05861$ \\
Dec       &  $66\fdg348371$  & $66\fdg348183$ & $66\fdg348171$ \\
\multicolumn{4}{l}{Error Matrix (arcsec)}\\
$\sigma^{2}_{\rmn{RA}}$  & 0.7 & 0.5 & 0.5 \\
$\sigma^{2}_{\rmn{Dec}}$ & 0.3 & 0.2 & 0.2 \\
$\rmn{Cov(RA,Dec)}$      & 0.4 & 0.3 & 0.3 \\
\multicolumn{4}{l}{Separation Distances (kpc)} \\
\bcga{}     & 4.19 &  1.63  & 1.59 \\
X-ray peak  & 34.5 &  30.3  & 30.2 \\
Ln(Evidence) & 36.8 & 41.1 & 37.8 \\
$\chi^{2} / \text{dof}$ & 0.51 & 0.38 & 0.18 \\
```
(columns = Model 1, Model 2, Model 3)

## Ambiguities
- x_I is a strong-lensing centroid, not a WL κ peak.
- Which model to use: Model 2 has highest evidence; Model 1 best χ²/dof.
- Units of the error matrix: labelled "(arcsec)", entries are variances.
- Assignment calls A2146-A "NW"; the paper says BCG-B lies NW of BCG-A.
- glafic cross-check: DM–BCG ≈5, 3, 6 kpc; DM–X-ray 28, 29, 26 kpc.
