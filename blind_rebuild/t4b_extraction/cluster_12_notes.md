# Row 12 — DLSCL J0916.2+2951 (Musket Ball), S subcluster (Group C)

**Paper:** Dawson, Wittman, Jee, Gee, Hughes, Tyson, Schmidt, Thorman, Bradač, Miyazaki, Lemaux, Utsumi & Margoniner 2012, ApJL 747, L42 — "Discovery of a Dissociative Galaxy Cluster Merger with Large Physical Separation" (arXiv:1110.4391v2). Journal ref matches.
Source used: `data/papers/dawson2012_musketball/src_clean_C/MusketBallRev2b.tex` (byte-identical to `src/` copy).

| Item | Found? | Value | Location |
|---|---|---|---|
| z_cl | yes | 0.53 (South: 0.53414 +0.00065/−0.00064) | Abstract, §1; Table 1 |
| x_I (South HST WL mass peak) | yes | 09h16m15s ±8.0s, +29°49′34″ ±6.9″ | §5 first sentence |
| σ_I | yes, 1σ per-axis | RA ±8.0 "s" (unit ambiguous), Dec ±6.9″ | §5; Fig. 3 caption ("one sigma errors") |
| x_G (South X-ray concentration) | **no coords** | — | §4, Table 1 (L_X, T_X only) |
| alt. G: overall gas peak (Central) | yes | 09h16m15s ±5.5s, +29°50′59″ ±5.0″; offset 1.4′ ±0.14 from South WL peak | §5 |
| x_S | **no** | — | — |

Verbatim §5 (ms l.296):
```
The peak of the gas distribution ($09\fh16\fm15\fs\pm5.5\fs, 29\fdg50\farcm59\farcs\pm5.0\farcs$) derived from X-rays is offset
$1.4\arcmin\pm0.49$ from the North HST WL mass peak ($09\fh16\fm10\fs\pm30\fs, 29\fdg52\farcm10\farcs\pm30\farcs$), and
$1.4\arcmin\pm0.14$ from the South HST WL mass peak ($09\fh16\fm15\fs\pm8.0\fs, 29\fdg49\farcm34\farcs\pm6.9\farcs$), and is located
near a local minimum in the mass
```
Verbatim Table 1 South row: `South & $0.53414^{+0.00065}_{-0.00064}$ & $770^{+110}_{-92}$ & $4.1\pm1.6$& $3.1^{+1.2}_{-0.79}$ & 2.1 & $2.7^{+1.2}_{-0.7}$ & 7.0 & 6.7\\`

Issues:
1. **RA error unit.** It is printed as seconds of time. Read literally, 8.0 s ≈ 104″ on the sky; read as arcsec, it is 8.0″. The ±0.14′ (≈8″) offset error only fits the arcsec reading.
2. **Which gas peak.** The only X-ray position is the Central gas peak, which lies between N and S in a mass underdensity. The paper does not call it the South subcluster's stripped core.
3. **Coordinate precision.** Coordinates are quantised to 1 s of RA (≈13″) and 1″ of Dec.
4. **No galaxy position.** The paper gives no galaxy position for S (no BCG or centroid).
5. **Pointer mismatch.** Table 1 has no positions. The positions are in the §5 text, not §3.

Contamination: `src/` later held foreign files (1e0657.emapj.tex = Clowe 2006; f1a/f1b .ps). I did not open them.
