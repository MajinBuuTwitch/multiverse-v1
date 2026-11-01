# T4b position-extraction protocol (written before any paper is opened)

Applies PREREG.md §5.5 item 5 and the per-cluster classification rule mechanically.

## Sources
- For each cluster, ONLY the "Single Deciding (S, G, I) Position Source" paper listed in PREREG.md §5.5 table
  (journal reference given there). The paper is fetched from arXiv (e-print source preferred, PDF fallback)
  or the journal page if no arXiv version exists. No other paper may be used to supply a position or error.
- Redshift z_cl for the kpc conversion: taken from the same primary source paper (if absent there, from the
  dynamical-age source paper named in the same table row; this is only a unit-conversion input).

## Observables (designated primary subcluster as named in the PREREG table)
- x_I: weak-lensing convergence (kappa) / surface-mass-density peak of that subcluster (as reported in the paper).
- x_G: X-ray surface-brightness (emission-measure) peak of that subcluster, or its stripped X-ray gas core /
  cold-front clump as identified in the paper.
- x_S: luminosity-weighted galaxy centroid of that subcluster as tabulated in the paper. Only a position the paper
  explicitly describes as a luminosity-weighted centroid/centre qualifies (a luminosity *peak* of a smoothed map is
  NOT a centroid). If no such centroid is tabulated, the subcluster BCG position from the same paper is used.
- A position may be given as absolute coordinates (RA, Dec) or as a stated offset/distance between two of the
  three positions (e.g. "the mass peak lies 25 arcsec from the BCG"), since the classification needs only
  d_IG = |x_I - x_G| and d_IS = |x_I - x_S|. Positions read off a figure by eye are NOT acceptable (not reported values).

## Uncertainties
- sigma_c = 1D 68% sky positional uncertainty. If 2D errors (sigma_RA*, sigma_Dec) or 1-sigma ellipse semi-axes
  (a, b) are given: sigma_c = sqrt((s1^2 + s2^2)/2). 90% radius -> divide by 1.645; 95% radius -> divide by 1.960.
- Arcsec -> kpc with flat LCDM D_A(z_cl), H0 = 67.36, Om = 0.315 (computed in code).
- If an uncertainty is not given for a position, but the text states the instrument's X-ray/optical centroiding
  (positional) error, that stated value is used.
- Otherwise the cluster is "unclassified" (missing-data rule). No ad-hoc supplementation.

## Classification (computed in code, not by hand)
sigma_diff = sqrt(sI^2 + sG^2 + sS^2);
"dark mass with gas" if d_IS - d_IG > 2 sigma_diff; "dark mass with galaxies" if d_IG - d_IS > 2 sigma_diff;
otherwise "unclassified".
