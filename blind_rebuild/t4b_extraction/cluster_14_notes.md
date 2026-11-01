# Row 14 – MACS J1149.5+2223, NW subcluster (= "subcluster one")

**Paper:** Golovich et al. 2016, ApJ 831, 110 (arXiv:1608.01329, DOI 10.3847/0004-637X/831/1/110). The journal reference matches.
**Source used:** `data/papers/golovich2016_macs1149/src_D/MACSJ1149_final.tex`
**z_cl = 0.544** (§1: "at a redshift of 0.544"; 1′ = 383 kpc).

## Summary
| Quantity | Found? | Where | Value |
|---|---|---|---|
| x_I | **no position**. This paper has no lensing map | §6.4 | Only: "[Smith09] shows the X-ray peak ... to be offset from the lensing mass peak by 15″ along the merger axis to the northwest". No error given. The value is cited from another paper |
| x_G | **no coordinates** | §5.1, §6.4, §6.5 | qualitative only: "peaked ahead of the BCG" |
| S: NW luminosity-weighted density **peak** | yes | §3.2 | 11h49m36.81s (+4.3/−8.5 s), +22°23′57.2″ (+2.4/−6.1″), bootstrap errors |
| S: GMM subcluster-1 centre | yes | Table 3 | 11h49m35.6s ± 4.5 s, +22°24′11.0″ ± 6.0″ (marginal 1σ) |
| BCG | **no coordinates** | §5.1 | "The luminosity peak is very near the location of the BCG." |

- RA errors are printed in seconds of time (1 s = 13.87″ at δ = 22.4°). The Table 3 RA error of ±4.5 s (≈62″) against the Dec error of ±6″ may be a unit typo. I have flagged this but not resolved it.
- Pointer check: Table 2 in the arXiv version is the BIC/membership table; positions are in §3.2 and Table 3. §4 has no subsections. Fig. 8 is a reproduction of the Ogrean+16 Chandra map with plusses only.

## Verbatim
§3.2: "The northwestern peak is located at RA$=$11$^{h}$49$^{m}$36.81$^{+\text{4.3}}_{-\text{8.5}}$$^{s}$, DEC$=$22$^{\circ}$23$\arcmin$57.2$^{+\text{2.4}}_{-\text{6.1}}\arcsec$ and the southeastern peak is located at RA$=$11$^{h}$49$^{m}$42.9$^{+\text{4.3}}_{-\text{12.7}}$$^{s}$, DEC$=$22$^{\circ}$21$\arcmin$56.0$^{+\text{13.3}}_{-\text{9.7}}\arcsec$."

Table 3 (table:results):
```
1 	& 133 	& 11$^{h}$49$^{m}$35.6$\pm$4.5$^{s}$ 	& 22$^{\circ}$24$^{\prime}$11.0$\pm$6.0$^{\prime\prime}$	& 0.54256$^{+0.00085}_{-0.00077}$ & 1260$^{+31}_{-42}$	& 16.71$^{+1.25}_{-1.60}$ 	& -504$\pm$158 \\
2 	& 59		& 11$^{h}$49$^{m}$43.2$\pm$2.9$^{s}$ 	& 22$^{\circ}$21$^{\prime}$51.4$\pm$0.9$^{\prime\prime}$ 	& ...
3	& 14 		& 11$^{h}$49$^{m}$35.5$\pm$6.5$^{s}$ 	& 22$^{\circ}$24$^{\prime}$49.5$\pm$1.6$^{\prime\prime}$ 	& ...
```
§6.4: "\cite{Smith09} shows the X-ray peak in MACS J1149 to be offset from the lensing mass peak by 15$\arcsec$ along the merger axis to the northwest (i.e. further from the center of mass of the cluster)."
