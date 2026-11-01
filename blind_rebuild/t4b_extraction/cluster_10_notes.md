# Row 10 — Abell 754, E (shock) subcluster (Group C)

**Paper:** Okabe & Umetsu 2008, PASJ 60, 345 — "Subaru Weak Lensing Study of Seven Merging Clusters: Distributions of Mass and Baryons" (arXiv:astro-ph/0702649v4). The journal ref matches. The OUP journal page returned HTTP 403, so only the arXiv version was checked.
Source used: `data/papers/okabe_umetsu2008/src_clean_C/draft_pub_astroph.tex` (byte-identical to `src/` copy).

| Item | Found? | Value | Location |
|---|---|---|---|
| z_cl | yes | 0.0542 (§3.1: 0.054) | Table 2 "Cluster X-ray Properties" |
| x_I (east mass clump E) | **no coords** | — | §3.1 / Fig. 5, qualitative only |
| x_G (east X-ray clump XE) | **no coords** | — | §3.1 / Fig. 5, qualitative only |
| x_S | **no coords** | "a luminous, large elliptical galaxy" in E | §3.1 |
| any σ | **no** | — | — |

Verbatim Table 2 row: `A754 ~~& 0.0542 & On-going & 63.1 & & $10.0\pm0.3^{\rm a}$ \\`

Key quotes (§3.1 A754):
- "We found moderate signal-to-noise ratios of 5.8 and 5.1 in the κ map for the central and east mass (E in Figure 5) clumps, respectively"
- "The peak locations in the luminosity map of cluster sequence galaxies are in good agreement with these mass substructures (bottom-left panel). The central mass peak coincides with the BCG (top-left panel). The east mass concentration contains a luminous, large elliptical galaxy."
- "The east mass clump is offset from the east X-ray clump towards the southwest, which is opposite to the moving direction of this gas clump"

Generic numbers (these are not peak-centroid errors): Subaru astrometric rms "about 1 pixel (=0.202″)" (§2.1); κ-map Gaussian FWHM 1.67′; the Chandra aspect offset "was then corrected" (no value given).

Pointer note: Table 2 has no positions. A754 is §3.1 / Fig. 5 in the arXiv numbering (§3.2 = A1750).
**Result:** I, G and S are all unavailable, so this row is unclassified under the missing-data rule.
Contamination: `src/` later held foreign files (mnras.tex etc.) from another group. I did not open them.
