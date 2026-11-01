# Row 09 — Abell 520, P4/SW subcluster (Group C)

**Paper:** Jee, Hoekstra, Mahdavi & Babul 2014, ApJ 783, 78 — "HST/ACS Confirmation of the Dark Substructure in A520" (arXiv:1401.3356v2). Journal ref matches the assigned one.
Source used: `data/papers/jee2014_a520/src_clean_C/ms.tex` (byte-identical to `src/ms.tex`; archive SHA-256 verified).

| Item | Found? | Value | Location |
|---|---|---|---|
| z_cl | yes | 0.2 | §1 last para: "at the redshift (z=0.2) of Abell 520" |
| x_I | yes | P4 = (04 54 04.32, +02 53 51.0) | Table 1 |
| σ_I | yes | (Δα, Δδ) = (3.0, 4.4) arcsec, per-axis, bootstrap, 1σ | Table 1 header/comment; §1 "All the quoted uncertainties are at the 1-σ (~68%) level" |
| x_G | **no** | — | no X-ray position for P4 anywhere |
| x_S | **no** | — | no luminosity centroid / BCG position for P4 |

Verbatim Table 1 (ms.tex l.723–749):
```
\tablecaption{Mass Properties of Substructure ($r<150$~kpc)}
\tablehead{Substructure & $\alpha, \delta$ & $\Delta \alpha, \Delta \delta$ & Projected Mass & Gas Mass \\
            & ($^h~^m~^s$, $\degr~ \arcmin~ \arcsec$) & ($\arcsec,\arcsec$) & ($h_{70}^{-1} 10^{13} M_{\sun}$) & $(h_{70}^{-5/2} 10^{13} M_{\sun})$}
P3' (new centroid) & (04 54 07.51, +02 54 41.3) & (5.1,6.2) & $3.94\pm0.30$ & $<0.85$ \\
P4  & (04 54 04.32,  +02 53 51.0)  & (3.0,4.4)   & $4.23\pm0.28$ & $ <0.34$ \\
\tablecomments{The positional uncertainty is estimated from bootstrapping. ...}
```
Only qualitative galaxy statement (§5.1): "the location of P4 in C12 is offset from the peak in the luminosity distribution, whereas the position in our mass reconstruction coincides better with the light."

Pointer note: Table 1 sits in §4 (Mass reconstruction); §3.2 is "PSF Model" (nothing on positions).
Contamination: `src/` later held foreign El Gordo files from another group — not opened; only my clean `ms.tex` was used.
