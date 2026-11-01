# Row 15 – RX J0603.3+4214 (Toothbrush), N subcluster

**Paper:** Jee et al. 2016, ApJ 817, 179 (arXiv:1510.03486, DOI 10.3847/0004-637X/817/2/179). The journal reference matches.
**Source used:** `data/papers/jee2016_toothbrush/src_D/ms.tex`
**z_cl = 0.225** (abstract; 3.61 kpc/″).

## Summary
| Quantity | Found? | Where | Value |
|---|---|---|---|
| x_I: P1 "Centroid" (dominant northern WL peak, 4.39σ) | yes | Table 2 | (90.81674°, 42.24823°) |
| x_I alternate: P3 (2nd northern HST-resolved peak, 3.08σ) | yes | Table 2 | (90.77961°, 42.26730°) |
| σ_I | **NOT GIVEN** | §4.3 + footnote | errors were reportedly estimated with FIATMAP, but no value is given. Text says the P2/P4 centroids agree within ~0.2′ and the merged northern peak shifts ~0.5′, both "consistent with the noise" |
| x_G (northern X-ray peak) | **offset only** | §5.2 | "The northern mass peak is offset toward the northwest with respect to the corresponding X-ray peak by ~0.5′" (approximate, no error) |
| x_S (luminosity peak / BCG) | **no coordinates** | §6, §4.4 | "coincides with the galaxy luminosity peak". The word "BCG" does not appear anywhere in the paper |

- Pointer check: Table 2 matches and Fig. 6 (joint mass map) matches. In the arXiv version the 2D mass section is §4.3, not §3.3. The mass–X-ray comparison is Fig. 8.
- My computation: P1–P3 separation ≈ 120″.

## Verbatim Table 2
```
\tablecaption{Significance of substructures in \tb}
\tablehead{\colhead{Property} &  \colhead{P1} & \colhead{P2} & \colhead{P3} & \colhead{P4} }
Centroid ($\alpha,\delta$)  & $(90\fdg81674, 42\fdg24823)$   &  $(90\fdg85078, 42\fdg15961)$ & $(90\fdg77961, 42\fdg26730)$ & $(90\fdg79856, 42\fdg21122)$ \\
Significance ($\sigma$)  & 4.39 &  3.95    &  3.08   &  2.60
```
§5.2: "We find offsets between X-ray and mass peaks. The northern mass peak is offset toward the northwest with respect to the corresponding X-ray peak by $\mytilde0.5\arcmin$ whereas the the southern mass peak is offset to the south by $\mytilde2\arcmin$."
§6: "The northern mass clump encloses $M_{200}=6.29_{-1.62}^{+2.24}\times 10^{14} M_{\sun}$ and coincides with the galaxy luminosity peak."
