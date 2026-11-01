# Row 13 – MACS J0025.4-1222 (Baby Bullet), SE subcluster

**Paper:** Bradač et al. 2008, ApJ 687, 959 (arXiv:0806.2320, DOI 10.1086/591246). The journal reference matches.
**Source used:** `data/papers/bradac2008_macs0025/src_D/ms.tex` (a clean re-extraction of the e-print; see the incident note below).
**z_cl = 0.586**, from the abstract ("at $z=0.586$"). §3 gives the iterative value z_Cl = 0.5857. Scale: 6.61 kpc/arcsec.

## Summary
| Quantity | Found? | Where | Value |
|---|---|---|---|
| x_I (lensing kappa peak, "total") | offset only | Table 2 | (Δx, Δy) = (−0.70 ± 0.25, −0.43 ± 0.06) arcmin from the gas peak |
| x_G (X-ray SB peak) | yes, absolute | §5, Table 2 comments | 00:25:29.5, −12:22:36.6; ±0.08 arcmin per axis (Table 2). §5 says "within 5 arcsec", treated by the authors as top-hat |
| x_S "galaxies" | offset only | Table 2 | (−0.79 ± 0.20, −0.50 ± 0.20) arcmin from the gas peak. Not defined as a luminosity-weighted centroid |
| BCG1/BCG2 | **no coordinates** | §3, Fig. 3 | only marked in a figure |

- The errors in Table 2 are 1σ according to the caption. They include initial-condition and systematic effects plus the weak-lensing bootstrap.
- The paper does not state the Δx sign convention. The SE row has (−,−) and the NW row has (+,+), so +x is probably west. This does not matter for distances.
- There is a single X-ray peak, shared by both subclusters.
- Pointer check: Table 2 matches. "§3.2 / Fig. 2" do not match the arXiv numbering: lensing is §4.3, X-ray is §5, and Fig. 2 is the LRIS spectrum. The kappa/X-ray/light overlay is Fig. 4.

## Verbatim Table 2 (tab:offset)
```
\tablecaption{Offsets (with 1$\sigma$ errorbars) of the mass peaks and gas peaks.}
\tablehead{ \colhead{} & \colhead{} & \colhead{$\Delta x ([\mbox{arcmin}])$} &  \colhead{$\Delta y ([\mbox{arcmin}])$}}
 & total & $-0.70 \pm 0.25$ & $-0.43 \pm 0.06$ \phn \\
SE & gas& $0.0 \pm 0.08$ & $0.0 \pm 0.08$ \phn \\
 & galaxies & $-0.79\pm 0.20$ & $-0.50\pm 0.20$ \phn\\
\hline
 & total & $0.46 \pm 0.13$ & $0.20 \pm 0.04$ \phn \\
NW & gas & $0.0 \pm 0.08$ & $0.0 \pm 0.08$ \phn \\
 & galaxies &$0.39 \pm 0.20$ & $0.18 \pm 0.20$\phn
\tablecomments{Offsets are calculated from (00:25:29.5, -12:22:36.6) which corresponds to the peak in gas distribution (marked with a white $+$ in Fig.~\ref{fig:arcs}).}
```
§5: "The peak position in the adaptively smoothed X-ray contours is 00:25:29.5, -12:22:36.6. Although the precise position of this peak depends in detail on the smoothing algorithm, we conservatively estimate the accuracy to be better than 5 arcsec (i.e., the X-ray brightness peak is constrained to lie within 5 arcsec of this position)."

## Incident note (Group D)
My first extraction loop wrongly ran over every folder in `data/papers`. It extracted foreign archives into the `src\` folders of other groups (chen2019, dawson2012_musketball, jee2014_a520, jee2015_ciza2242, okabe_umetsu2008). I reported this to the parent straight away. Nothing was deleted. My own `src\` folders may also have been touched by another agent's loop: their creation times are earlier than my extraction. For that reason I re-extracted my four archives into fresh `src_D\` folders and used only those.
