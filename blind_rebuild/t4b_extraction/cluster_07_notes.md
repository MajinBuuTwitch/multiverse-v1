# Row 07 – Abell 2744, "Core/NW subcluster"

Paper: Merten et al. 2011, MNRAS 417, 333 (arXiv:1103.2772) – matches the given reference. Source: `data/papers/A2744_Merten2011/src_clean/a2744_rev3.tex`.
z_cl = 0.308 ("At the cluster's redshift $z=0.308$, one arcsecond corresponds to $4.536$~kpc.").

Designation "Core/NW" is ambiguous, so both clumps are extracted.

| Obs | Core | NW ("dark") |
|---|---|---|
| I | x,y = (−13 +11/−8, −4 +6/−13)″ relative to BCG; 68% bootstrap | (71 +11/−10, 84 +15/−7)″ relative to BCG; 68% (WL mesh pixel size) |
| G | Owers+11 X-ray peak 22±12″ from mass peak (also "projected 17″ separation") | NW interloper: >150 kpc (NW2), ≥400 kpc (NW1); no coordinates |
| S | BCG at α=3.58611°, δ=−30.40024° (reference point); no σ | none given ("clear separation ... any cluster member galaxies") |

## Verbatim Table 2 (label `STRUCTURES`)
```
Name & $x$ & $y$&$M(r<250\textrm{kpc})$ \\
&(\arcsec)&(\arcsec)&($10^{14}~M_{\odot}$)\\
Core&$-13^{+11}_{-8}$&$-4^{+6}_{-13}$&$2.24\pm0.55$\\[1ex]
NW&$71^{+11}_{-10}$&$84^{+15}_{-7}$&$1.15\pm0.23$\\[1ex]
W&$177^{+23}_{-17}$&$-30^{+11}_{-15}$&$1.11\pm0.28$\\[1ex]
N&$34^{+23}_{-32}$&$170^{+10}_{-28}$&$0.86\pm0.22$\\
```
Note: "The x-and y-coordinates are provided in arcseconds, relative to the BCG position ($\alpha_{\textrm{J2000}} =3.58611^{\circ}$, $\delta_{\textrm{J2000}} =-30.40024^{\circ}$). The 68\% confidence limits on peak positions are derived from 500 bootstrap realisations for the Core peak, and from the pixel size of the coarse weak lensing mesh in the reconstruction outskirts for the other mass peaks."

Sec. 4.1: "The mass peak is centred amongst the bright cluster member galaxies (within $1\sigma$ errors, it is consistent with the position of the BCG) and only $22\pm12$ arcseconds from a peak of X-ray emission identified by \citet{Owers2011}." ... "In the Core of Abell~2744, we observe a projected $17\arcsec$ separation".

## Caveats
- The tex has a commented-out (not compiled) separations table (Core 17±10 / 10±10″; NW 103±10 / 36±10″). It is not part of the paper and was not used.
- The x/y sign convention is not stated.
- In the tex, Sec. 4.2 is "Northern, the bullet" and Fig. 7 is the W-box X-ray figure, so the pointer's section and figure numbers do not line up with this version.
