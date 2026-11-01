# Row 11 — CIZA J2242.8+5301 (Sausage), N subcluster (Group C)

**Paper:** Jee, Stroe, Dawson, Wittman, Hoekstra, Brüggen, Röttgering, Sobral & van Weeren 2015, ApJ 802, 46 — "MC²: Constraining the Dark Matter Distribution of the Violent Merging Galaxy Cluster CIZA J2242.8+5301 by Piercing through the Milky Way" (arXiv:1410.2898). Journal ref matches.
Source used: `data/papers/jee2015_ciza2242/src_clean_C/ms.tex` (byte-identical to `src/ms.tex`).

| Item | Found? | Value | Location |
|---|---|---|---|
| z_cl | yes | z~0.19 (N clump biweight 0.18794±0.00053) | §1 last para; §7.1 |
| x_I (N mass centroid) | **no coords** | — | — |
| x_S (N luminosity centre/centroid) | **no coords** | — | §6, §7.3 |
| I–S offset | approx. | "~1′ (~190 kpc)" — "in both northern and southern sub-clusters" / "mean offset" | Abstract; §5; §7.3 |
| x_G | **no** | — | — |
| any σ | **no numbers** | contours in Fig. 9 only | — |

Key quotes:
- Abstract: "When the mass and galaxy centroids are compared in detail, we detect ~1′ (~190 kpc) offsets in both northern and southern sub-clusters. … the galaxy luminosity-mass offset for the northern clump is statistically significant at the ≳2σ level"
- §5: "The mean offset between the mass and luminosity/number density peaks is ~1′."
- §6: "We choose the galaxy luminosity center as an initial centroid … a bounding box 200″×200″ centered on the luminosity peak."
- Table 3 (p-values, null = centroids coincide): `North & 0.082 & 0.310` (Mass-Luminosity, Mass-Number)

The only coordinates in the paper are for the whole cluster: (22h42m49.1s, 53°00′51″) in §2, and the mean of the two halos (22h42m47.3s, 53°01′56″) in §6. Neither is a subcluster position.
Pointer note: Table 1 holds the 1D mass fits. §3.2 is CFHT data reduction. Fig. 5 is the mass-over-galaxy map (figure only).
Ambiguity: the "luminosity center" comes from a smoothed (FWHM ~3.4′) luminosity map. The authors call it both a peak and a centroid, so the protocol's centroid rule is unclear here. No BCG position is given.
Contamination: `src/` later held foreign El Gordo files. I did not open them.
