# Row 01 — 1E 0657-558 (Bullet), W subcluster — Clowe et al. 2006, ApJ 648, L109 (astro-ph/0608407)

Source: `data/papers/clowe2006/src_clean/1e0657.emapj.tex` (arXiv e-print source). z_cl = 0.296 (Abstract, §1).

**Pointer mismatch:** Table 1 is "Optical Imaging Sets"; positions are in **Table 2 "Component Masses"** (label `table2`).

| Quantity | Value | Where |
|---|---|---|
| I (kappa peak, subcluster) | 7.1" E, 6.5" N of subcluster BCG (total 9.63" — extractor-derived) | §3 para 1 |
| G (subcluster plasma / "X-ray plasma peak") | 06:58:21.2, −55:56:30.0 | Table 2 |
| S (subcluster BCG) | 06:58:16.0, −55:56:35.1 | Table 2 |
| S (luminosity centroid) | mentioned, not tabulated | §3 para 1 |
| Uncertainties | **none numerical** for I, G, S; only "~2σ from BCG", "within 1σ of luminosity centroid", "~8σ from plasma centre of mass"; Fig. 1 contours 68.3/95.5/99.7% | §3, Fig. 1 caption |

Verbatim rows (Table 2):
```
Main cluster BCG & $06:58:35.3$ & $-55:56:56.3$ & $5.5\pm 0.6$ & $0.54\pm 0.08$ & $0.36\pm 0.06$\\
Main cluster plasma & $06:58:30.2$ & $-55:56:35.9$ & $6.6\pm 0.7$ & $0.23\pm 0.02$ & $0.05\pm 0.06$\\
Subcluster BCG & $06:58:16.0$ & $-55:56:35.1$ & $2.7\pm 0.3$ & $0.58\pm 0.09$ & $0.20\pm 0.05$\\
Subcluster plasma & $06:58:21.2$ & $-55:56:30.0$ & $5.8\pm 0.6$ & $0.12\pm 0.01$ & $0.02\pm 0.06$\\
```
Verbatim text (§3):
> Two major peaks are clearly visible in the reconstruction, one centered $7\farcs1$ east and $6\farcs5$ north of the subcluster's brightest cluster galaxy (BCG) and detected at $8\sigma$ significance ... We estimate centroid uncertainties by repeating bootstrap samplings of the background galaxy catalog ... Both peaks are offset from their respective BCG by $\sim 2\sigma$, but are within $1\sigma$ of the luminosity centroid of the respective component's galaxies ... Both peaks are also offset at $\sim 8\sigma$ from the center of mass of their respective plasma clouds.

> The projected cluster galaxy stellar mass and plasma mass within 100 kpc apertures centered on the BCGs and X-ray plasma peaks are shown in Table~\ref{table2}.

Ambiguity: σ is never given in numbers; under the protocol the cluster probably counts as missing-uncertainty unless the analyst accepts some other reading.
