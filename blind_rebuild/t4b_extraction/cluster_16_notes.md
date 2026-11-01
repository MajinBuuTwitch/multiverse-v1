# Row 16 – ZwCl 0008.8+5215, E subcluster

**Paper:** Golovich et al. 2017, ApJ 838, 110 (arXiv:1703.04803, DOI 10.3847/1538-4357/aa667f). The journal reference matches.
**Source used:** `data/papers/golovich2017_zwcl0008/src_D/ms.tex`
**z_cl = 0.104** (§1: "At the cluster redshift ($z = 0.104$), 1′ corresponds to 115 kpc").

## Summary (East subcluster)
| Quantity | Found? | Where | Value | 1σ |
|---|---|---|---|---|
| x_I WL peak | yes | Table 3 | 00h12m03.8s, +52°34′16.9″ | RA +18.4/−11.1 s; Dec +27.8/−32.6″ (bootstrap; Fig. 10 says 1σ) |
| x_G X-ray SB peak (disturbed remnant core) | yes | Table 3 | 00h11m53.7s, +52°32′02.2″ | RA ±5.3 s; Dec ±2.0″ (bootstrap) |
| S: red-sequence luminosity **peak** | yes | Table 3 | 00h12m13.9s, +52°33′51.6″ | RA +2.7/−3.8 s; Dec +4.8/−4.2″ |
| S: BCG east | yes | Table 3 (also Table 2 in deg: 3.078217, 52.56305) | 00h12m18.8s, +52°33′46.9″ | NOT GIVEN |
| Offsets (Table 4, kpc, East) | yes | Table 4 | DM–Lum −249 (+126/−141); DM–BCG −319 (+72/−173); DM–ICM 319 (+149/−52); Lum–ICM 420 (+20/−53); BCG–ICM 480 ± 5.0 | |

- RA errors are in seconds of time (1 s = 9.12″ at δ = 52.57°).
- No luminosity-weighted *centroid* is tabulated, only a luminosity-map peak. The protocol fallback is therefore the BCG, which has no stated error.
- Inconsistency: §5.1 says the east gas core is offset "from the BCG in the east by ~320 kpc (see Table 4)", but Table 4 gives BCG–ICM = 480 kpc. The 320 kpc figure matches DM–ICM instead.
- My computation from the Table 3 point positions (115 kpc/′): I–G ≈ 313 kpc, I–Lum ≈ 183 kpc, I–BCG ≈ 268 kpc. The Table 4 bootstrap values differ.
- Pointer check: Table 4 matches and Fig. 9 matches. The positions are in §4.3 of the arXiv version, not §4.1–4.2.

## Verbatim Table 3 (table:offsets)
```
Map & East peak location (J2000) & West peak location (J2000) & Projected separation (kpc) \\
WL massmap & 00$^{\text{h}}$12$^{\text{m}}$03.8$^{+\text{18.4}}_{-\text{11.1}}$$^{\text{s}}$, 52$^{\circ}$34$\arcmin$16.9$^{+\text{27.8}}_{-\text{32.6}}\arcsec$ &  00$^{\text{h}}$11$^{\text{m}}$12.8$^{+\text{11.5}}_{-12.5}$$^{\text{s}}$, 52$^{\circ}$32$\arcmin$11.3$^{+\text{32.1}}_{-\text{28.2}}\arcsec$  & 924$^{+\text{243}}_{-\text{206}}$  \\
Red sequence luminosity & 00$^{\text{h}}$12$^{\text{m}}$13.9$^{+\text{2.7}}_{-\text{3.8}}$$^{\text{s}}$, 52$^{\circ}$33$\arcmin$51.6$^{+\text{4.8}}_{-\text{4.2}}\arcsec$ &  00$^{\text{h}}$11$^{\text{m}}$21.6$\pm0.003$$^{\text{s}}$, 52$^{\circ}$31$\arcmin$42.1$\pm0.00002\arcsec$  & 944$^{+\text{30}}_{-\text{40}}$  \\
BCG	& 00$^{\text{h}}$12$^{\text{m}}$18.8$^{\text{s}}$, 52$^{\circ}$33$\arcmin$46.9$\arcsec$ &  00$^{\text{h}}$11$^{\text{m}}$21.7$^{\text{s}}$, 52$^{\circ}$31$\arcmin$48.5$\arcsec$  & 1020 \\
X-ray surface brightness & 00$^{\text{h}}$11$^{\text{m}}$53.7$\pm5.3$$^{\text{s}}$, 52$^{\circ}$32$\arcmin$02.2$\pm2.0\arcsec$ &  00$^{\text{h}}$11$^{\text{m}}$22.3$^{+\text{0.1}}_{-5.3}$$^{\text{s}}$, 52$^{\circ}$31$\arcmin$44.4$^{+\text{0.2}}_{-\text{0.1}}\arcsec$  & 550$\pm$4.0  \\
```
## Verbatim Table 4 (table:offsets1)
```
Offset &	East (kpc)\footnote{Negative offsets indicate the first component listed is closer to the center of the cluster.} & West  (kpc)  \\
DM--Luminosity &  -249$^{+\text{126}}_{-\text{141}}$  &  170$^{+\text{130}}_{-\text{131}}$\\
DM--BCG	&	-319$^{+\text{72}}_{-\text{173}}$  &  168$^{+\text{131}}_{-\text{133}}$\\
DM--ICM &  319$^{+\text{149}}_{-\text{52}}$  &  176$^{+\text{134}}_{-\text{129}}$\\
Luminosity--ICM &  420$^{+\text{20}}_{-\text{53}}$  &  12$^{+0.5}_{-\text{2.6}}$\\
BCG--ICM &  480$\pm$5.0  &  12$^{+\text{0.5}}_{-\text{2.6}}$
```
Table 2 row: `3.078217	 & 52.56305 	& 0.105983 	&	1.35E-05		&	16.0	 	&	BCG east, H$\beta$, Mg I (B), Fe I, Na I (D), H$\alpha$, [N II]\\`
