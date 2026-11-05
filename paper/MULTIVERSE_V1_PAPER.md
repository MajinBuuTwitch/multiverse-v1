---
title: "A Pre-Registered Falsification of a Speculative Multiverse Model"
subtitle: "The Mandarano Model (v1, the 19-strand \"Ropewalk\" formulation) tested against cosmological and galactic data, with a blind independent rebuild, a Bayesian head-to-head against ΛCDM, and blind injection tests"
author: "Gregory Mandarano (WickedAI)"
date: "Version 6.0.2 · 4 November 2026"
geometry: margin=1in
fontsize: 11pt
mainfont: "DejaVu Serif"
sansfont: "DejaVu Sans"
monofont: "DejaVu Sans Mono"
mathfont: "Latin Modern Math"
colorlinks: true
linkcolor: "blue"
urlcolor: "blue"
numbersections: true
header-includes:
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \usepackage{amsmath}
  - \usepackage{float}
  - \setlength{\emergencystretch}{3em}
---

\begin{center}
\fbox{\parbox{0.92\textwidth}{\small\textbf{Status of this document.} This is the public paper for version 1 of the Mandarano Model. DOI: \href{https://doi.org/10.5281/zenodo.23868218}{10.5281/zenodo.23868218} (the complete record: rules, code, frozen results and timestamp proofs). It supersedes, as the readable account, the frozen results report \texttt{MULTIVERSE\_PREDICTIONS\_PAPER\_v4.md} (version 5.0.0, SHA-256 \texttt{a0744ca7\ldots}, frozen in \texttt{RESULTS\_v5.sha256}), which is preserved unchanged as part of the record. Nothing in this paper changes a registered verdict. Section~8 reports the blind injection tests. Version 6.0.2 corrects one reference: Croker et al.\ (2024) is JCAP 10, 094 (arXiv:2405.12282); version 6.0.1 gave arXiv:2407.03508, the number of an unrelated paper. Nothing else changes.}}
\end{center}

# Plain summary {.unnumbered}

A screenwriter proposed a speculative picture of the multiverse in which our universe is one string in a bundle of nineteen, and in which dark matter and dark energy are effects of the neighbouring strings. Before any data were downloaded, the model's equations, the datasets, and the pass/fail rule for every test were written down, fingerprinted with SHA-256 and sent to be timestamped in the Bitcoin blockchain, so that nobody (the author included) could move the goalposts afterwards. That does not make every test blind: several datasets had been public for years, and the one-in-nineteen failures were forecast from published numbers before any test ran. Two AI systems from different model families then ran the tests separately under written blindness rules, one of them without access to the other's code and results.

**Version 1 fails.** Its prediction for how galaxies rotate fits only 6 of 87 held-out galaxies. Its core assumption, that ordinary matter is exactly one part in nineteen of the universe, is about 3.9σ above the measured value. The model's dark-energy curve is neither confirmed nor ruled out. What is falsified is version 1 as registered, including its specific Gaussian "shadow" kernel; the broader multiverse picture is not tested here. That verdict follows the gate rules as written; under one alternative reading of how a failed validation gate propagates, logged by the rebuild before the galaxy test ran, the strictest combination of readings would give inconclusive instead (Section 5). One ambiguity in the rulebook, the convention for the early-universe sound horizon, made one validation gate pass in one pipeline and fail in the other, so the affected tests are reported under both readings; the verdict is the same under both. A supplementary Bayesian comparison finds that standard ΛCDM is preferred over every version of the model's background expansion that was tested (two narrow-prior runs are inconclusive), strongly so when the one-in-nineteen rule is imposed. That comparison and the blind injection tests are supplementary: the verdict rests on the pre-registered tests alone. Every file, fingerprint and timestamp is public, so every step can be checked.

# Honesty statement and tier labels {.unnumbered}

1. **Who wrote this.** The author is a screenwriter, not a physicist. The model began as a way to make sense of time-travel stories. It accompanies a long-form documentary. The analysis, the independent rebuild and the reviews were carried out by AI systems under the author's direction (Section 2.6).
2. **What it is.** A speculative model, not a theory. Not peer reviewed. Nothing in it claims that established physics is wrong.
3. **What it is for.** It was written to be broken, and it was.
4. **Numerology stays numerology.** The match between the 1 : 6 : 12 string count and the cosmic energy budget motivated the model. It is not evidence for it.

Every claim carries one of three labels. **Tier 1, Established:** measured or textbook physics, cited. **Tier 2, Published speculation:** ideas published by working physicists that are not established. **Tier 3, This model:** the Mandarano Model's own claims. In the equations, *[Established]* and *[Model Ansatz]* mark Tier 1 and Tier 3 respectively.

# Introduction

Speculative models that claim to explain dark matter and dark energy are common; tests of them that are fixed in advance are not. This paper reports a complete pre-registered test of version 1 of the Mandarano Model, built so that every pass/fail line was locked before any data were seen, and so that anyone can verify that claim without trusting the author.

The study has four layers:

1. **Pre-registration (Stage 1).** Every equation was derived from explicit assumptions (A1 to A20), classified as Established or Model Ansatz, and revised through three rounds of pre-data review. Every scored test was given a single mechanical decision rule. The complete specification was hashed into `PREREG_v4.sha256` and timestamped with OpenTimestamps before any dataset was downloaded; the dataset manifest was then hashed and stamped before any fit (Section 3).
2. **Execution (Stages 2 and 3).** The primary pipeline (Gemini, as the agent "Argon") ran four validation gates, fixed each free parameter on its registered training data, and ran all scored tests.
3. **Independent replication (Stage 4).** A blind rebuild (Claude) implemented the entire analysis from the frozen rulebook alone, without access to the primary pipeline's code or results, and froze its own results before comparison (Section 6).
4. **Supplementary analyses, labelled as such.** A Bayesian head-to-head against ΛCDM (Section 7) and blind injection tests (Section 8). Neither changes a registered verdict.

The registered decision hierarchy is strict: **a single primary pillar ending in FAIL falsifies the model.**

# The model and its predictions

## The 19-strand bundle and the static leak partition (T2)

In the model, histories that branched recently stay in step and bundle into strands. The present-day cosmic budget is modelled as a close-packed hexagonal bundle of $N_s = 1 + 6 + 12 = 19$ strings *[Model Ansatz, Numerology]*: our own string carries ordinary (baryonic) matter; the 6 touching neighbours supply dark matter as a gravitational "shadow" transmitted across the gap with efficiency $(1 - f_{\rm leak})$; the 12 outer strings store tension that acts as dark energy:
$$\Omega_b = \frac{1}{19}, \qquad \Omega_{\rm dm} = \frac{6(1 - f_{\rm leak})}{19}, \qquad \Omega_{\rm de} = \frac{12 + 6 f_{\rm leak}}{19}. \qquad \text{[Model Ansatz]}$$
In the locked static form, dark matter dilutes as ordinary pressureless matter at all epochs, so early-universe physics is standard and the compressed CMB distance priors remain valid. Excluding massive neutrinos from the share relation, the baryon-plus-dark-matter share $\Omega_{bc} = (7 - 6f_{\rm leak})/19$ fixes the leak and the predicted dark-to-ordinary ratio:
$$f_{\rm leak} = 1 - \frac{19\,\Omega_{bc} - 1}{6}, \qquad \mathcal{R}_{\rm pred} = 6(1 - f_{\rm leak}) = 19\,\Omega_{bc} - 1. \qquad \text{[Model Ansatz]}$$
Because $\Omega_{bc} = \Omega_b(1 + \mathcal{R}_{\rm true})$ in any universe, the leak cancels out of $\mathcal{R}_{\rm pred}$: **test T2-A is algebraically a test of $\Omega_b = 1/19$.** Combined with $\omega_b \equiv \Omega_b h^2$ *[Established]*, it also predicts a Hubble constant with no free parameter:
$$H_0^{\rm pred} = 100\sqrt{19\,\omega_b}\ \ {\rm km\,s^{-1}\,Mpc^{-1}}. \qquad \text{[Model Ansatz]}$$

## Unwinding dark energy (T1)

In a flat FLRW background *[Established]*,
$$E^2(a) = \Omega_\gamma a^{-4} + \Omega_\nu f_\nu(a) + \Omega_{bc}\,a^{-3} + \Omega_{\rm de}\exp\!\left[3\int_a^1 \frac{1 + w(a')}{a'}\,da'\right].$$
The model reads dark energy as stored twist: a power-law tension $\rho_{\rm de}\propto\theta^n$ ($n>0$) relaxing at a constant cosmic-time rate $\dot\theta = -\Gamma_u\theta$ gives **Unwinding Law 1** *[Model Ansatz]*:
$$w(a) = -1 + \frac{\gamma_u}{E(a)}, \qquad \gamma_u \equiv \frac{n\Gamma_u}{3H_0} \ge 0,$$
which traces a one-parameter curve in the $(w_0, w_a)$ plane,
$$w_0 = -1 + \gamma_u, \qquad w_a = -\tfrac{3}{2}\gamma_u\left[\Omega_m + \gamma_u(1 - \Omega_m)\right] \le 0,$$
never crosses $w = -1$, and has one fewer free parameter than the CPL form $w(a) = w_0 + w_a(1 - a)$ *[Established parametrization]*.

## The shadow in galaxies (T5)

The shadow density is a 3D Gaussian blur of width $\sigma_{\rm ref}$ of the coarse-grained baryon density *[Model Ansatz]*. For an isolated galaxy with stellar mass-to-light ratios $\Upsilon_{\rm disk} = 0.50$ and $\Upsilon_{\rm bul} = 0.70$,
$$v_c^2(r) = \frac{G\left[M_b(<r) + M_{\rm sh}(<r)\right]}{r}, \qquad M_{\rm sh}(<r) = \mathcal{R}_{\rm pred}\int_0^\infty \mathcal{F}_\sigma(r, r')\,dM_b(r'),$$
where the exact enclosed-mass kernel (a non-central $\chi^2_3$ CDF, verified against a 3D Monte Carlo integral before the freeze) is
$$\mathcal{F}_\sigma(r,r') = \tfrac{1}{2}\!\left[\operatorname{erf}\!\frac{r+r'}{\sqrt2\,\sigma_{\rm ref}} + \operatorname{erf}\!\frac{r-r'}{\sqrt2\,\sigma_{\rm ref}}\right] - \frac{1}{\sqrt{2\pi}}\frac{\sigma_{\rm ref}}{r'}\left[e^{-(r-r')^2/2\sigma_{\rm ref}^2} - e^{-(r+r')^2/2\sigma_{\rm ref}^2}\right]$$
(with the point-mass limit used for $r'/\sigma_{\rm ref} < 10^{-4}$). Because the kernel is a normalized diffusion operator, any galaxy whose baryon density falls outward obeys a **saturation cap**,
$$\frac{g_{\rm tot}(r)}{g_{\rm bar}(r)} \le 1 + \mathcal{R}_{\rm pred}, \qquad \text{[mathematical property of the kernel]}$$
which is 5.87 for the primary pipeline's fitted leak (5.91 in the rebuild; 6.00 for $f_{\rm leak} = 1/6$).

## Colliding clusters (T4)

Each coherent baryonic component's shadow source is extrapolated from a retarded time $t - \tau_{\rm lag}$ *[Model Ansatz]*. In young mergers ($t_p < \tau_{\rm lag}$) the shadow stays with the collisionless galaxies; in old mergers it relaxes onto the X-ray gas. Lensing, galaxy and gas peak positions classify each subcluster as "with galaxies", "with gas" or unclassified using $\sigma_{\rm diff} = (\sigma_I^2 + \sigma_G^2 + \sigma_S^2)^{1/2}$; any cluster lacking complete positions and uncertainties is unclassified.

## Regional expansion (T6)

The model attributes the Hubble tension to a "local accent": the expansion rate should vary by sky region. Pantheon+SH0ES Hubble-flow supernovae ($0.023 \le z \le 0.15$, non-calibrators) are split into HEALPix $N_{\rm side}=1$ Galactic regions, with a registered merging rule for sparse pixels, and tested with the generalized least-squares statistic *[Established]*
$$\chi^2_{\rm het} = \left(\hat{\mathbf H}_0 - \bar H_0\mathbf 1\right)^{T}\mathbf C_{H_0}^{-1}\left(\hat{\mathbf H}_0 - \bar H_0\mathbf 1\right), \qquad {\rm dof} = N_{\rm pix}-1.$$

## Who did what

The author proposed the model and made every design decision. The equations and rules were formalized and executed by Gemini (Google) operating as the agent "Argon" in Google Antigravity (Gemini 4 Argon, instructed to run at the High thinking level; the logs record no finer version string). The blind rebuild was implemented by Claude Opus 5.5 (Anthropic; claude-opus-5-5) at high effort: for its first half hour in Google Antigravity through Antigravity's access to third-party models, then, when that allowance ran out, in Claude Code with access to the same folder and the same initial instructions (the author's account; the rebuild's own logs record only the Claude Code stage). The Claude Code session also wrote the Phase 3 mock generator. The independent Phase 3 re-score was run by a separate Gemini session (as reported by the author; its files name no model), and Grok (xAI) reviewed the paper. Pre-data reviews, the final review, the comparison, and this paper were prepared in a separate planning session with Claude Opus 5.5 (Anthropic; model ID claude-opus-5-5). Agents' chat summaries were never treated as results: every number in this paper was checked against the frozen files.

# Pre-registration, data freeze and validation gates

## The cryptographic record

The governing rulebook (`PREREG.md` v1.0.2, `MULTIVERSE_STAGE1_EQUATIONS.md` v1.0.2, `ASSUMPTIONS.md` v1.0.2 and the three Stage 1 parts) was hashed into `PREREG_v4.sha256` (SHA-256 `53ce966a…`) and stamped with OpenTimestamps (calendar-attested 2026-10-30 08:44:36 UTC; anchored in Bitcoin blocks 973800 and 973821) **before any observational data were downloaded**. The public datasets were then downloaded and hashed into `DATA_MANIFEST.sha256` (`73135698…`, stamped 08:59:53 UTC, the same blocks) before any fit. Results were frozen in five chained manifests (`RESULTS_v1` to `RESULTS_v5`), the first anchored in block 973822. Appendix A lists every manifest and Appendix B explains how to verify them.

A timestamp proves that a file existed *on or before* a block's time. It does not prove that nobody had seen the data beforehand: several datasets (notably Planck) were public for years, and Stage 1 itself forecast the T2 failures from published numbers before any test ran. Those tests formalize what was already known. The genuinely blind tests are those on held-out data (T5-A, T5-B), the cluster sample (T4b) and the regional test (T6).

## Datasets

- **DESI DR2 BAO** (DESI Collaboration 2025, arXiv:2503.14738), with the $z_{\rm eff} = 2.33$ Lyα row replaced in the deciding T1 and T2 runs by the joint Lyα BAO + Alcock–Paczyński measurement (arXiv:2607.27410).
- **Planck 2018 compressed CMB**: the Chen, Huang & Wang (2019) distance priors $(R, \ell_A, 100\omega_b)$ with covariance, plus registered reference values ($\Omega_b = 0.04930 \pm 0.00086$, $100\omega_b = 2.237 \pm 0.015$, $H_0 = 67.36 \pm 0.54$, $\mathcal R = \omega_c/\omega_b = 5.36 \pm 0.065$) and BBN priors.
- **Supernovae**: Pantheon+ and SH0ES (Brout et al. 2022; Riess et al. 2022) and DES-SN5YR Dovekie (Popovic et al. 2025), always analysed separately, never combined.
- **Galaxies**: SPARC (Lelli et al. 2016), 175 galaxies and 3391 radial points, split into 88 training (odd rows) and 87 test (even rows) galaxies; NGC 1052-DF2.
- **Clusters**: a 16-merger dissociative catalogue compiled from the literature, and the Wittman, Golovich & Dawson (2018) ensemble.

## Validation gates and the two readings of gate G9-b

Four gates check the numerical machinery before any scored test. Both pipelines pass G9-a (BAO-only $\Omega_m$), G9-c and G9-d (the kernel limit, $1.44\times10^{-11}$ against a $10^{-10}$ limit).

**Gate G9-b** requires the pipeline's flat-ΛCDM CMB likelihood, run on the Chen et al. Table 1 prior alone, to reproduce their Table 2 posteriors within $0.3\sigma$. Here the two pipelines differ, and the difference exposed an ambiguity in the rulebook (Finding 1):

- The primary pipeline evaluates the recombination sound horizon $r_s(z_*)$ with Chen et al.'s own early-universe form ($\omega_r = 1/24185$, about 1.1% below the physical radiation density, and the 0.06 eV neutrino counted as matter). This gives an $r_s(z_*)$ about 0.17–0.18% larger than the registered full integral (a5), and G9-b passes ($0.17\sigma$ against the registered G9-b target, $h = 0.6727 \pm 0.0060$; the frozen gate reported $0.025\sigma$ against Planck 2018 values, an erratum noted in Section 9). The change was logged as a "bug fix" ten seconds before the gates passed and was not logged as a departure from (a5) at the time.
- The blind rebuild coded (a5) literally (agreeing with CAMB to $4.9\times10^{-5}$). Under that reading G9-b **fails**: $h$ is off by $0.577\sigma$.

By the registered gate-mapping rule, a failed G9-b makes the scored tests T1-L1, T1-Sign and T2-A (and the unscored sensitivity check T2-B) INCONCLUSIVE. **Both readings are reported throughout.** The model-level verdict is the same under both (Section 5).

# Results

## Dark-energy expansion (T1)

Law 1, flat ΛCDM and CPL were fitted to DESI DR2 BAO (joint Lyα) + compressed CMB + each supernova compilation.

| | Pantheon+ | DES-Dovekie |
|:----------------------------------|:-----------------------:|:-----------------------:|
| $\Delta\chi^2$ (Law 1 − ΛCDM), primary / rebuild | $-1.71$ / $-1.35$ | $-2.58$ / $-2.08$ |
| $\Delta\chi^2$ (Law 1 − CPL), primary / rebuild | $+5.46$ / $+5.55$ | $+7.36$ / $+7.48$ |
| Law 1 $\gamma_u$ (posterior median, primary) | $0.043 \pm 0.026$ | $0.045 \pm 0.026$ |
| CPL $w_0$ (primary) | $-0.854 \pm 0.056$ | $-0.825 \pm 0.056$ |
| CPL $w_a$ (primary) | $-0.51 \pm 0.22$ | $-0.62 \pm 0.22$ |
| $P(w_0 > -1)$, primary / rebuild | $0.9960$ / $0.9964$ | $0.9992$ / $0.9991$ |

Law 1 fits slightly better than a cosmological constant but worse than the free CPL curve; its fitted slope $w_a \approx -0.02$ is 24–27 times shallower than CPL's. **T1-L1 is INCONCLUSIVE under both readings.** The data favour $w_0 > -1$ at 99.6–99.9%: **T1-Sign** is PASS under the Chen reading and INCONCLUSIVE under (a5). That direction was already known from published DESI results and cannot rescue T1-L1.

## The strand budget (T2)

- **T2-N1 (ordinary-matter share):** $\Omega_b = 1/19 = 0.0526$ is $+3.87\sigma$ above Planck's $0.04930 \pm 0.00086$ (6.8% too high). **FAIL** in both pipelines.
- **T2-N2 (implied Hubble constant):** $H_0^{\rm pred} = 65.19 \pm 0.22$ is $-3.72\sigma$ ($-3.71\sigma$ in the rebuild) below Planck's $67.36 \pm 0.54$, moving away from the local value near 73, not toward it. **FAIL** in both pipelines.
- **T2-A (leak ratio):** the fitted $\Omega_{bc}$ gives $\mathcal R_{\rm pred} = 4.87 \pm 0.11$ (Pantheon+) and $4.90 \pm 0.11$ (DES-Dovekie) in the primary pipeline (4.91 and 4.94 in the rebuild) against Planck's $5.36 \pm 0.065$: $-3.74\sigma$ / $-3.58\sigma$ in the primary pipeline and $-3.45\sigma$ / $-3.22\sigma$ in the rebuild. Every run lies 3.2–3.7σ from Planck, past the 2σ FAIL line. **FAIL** under the Chen reading; **INCONCLUSIVE** under (a5) by the gate rule. Sensitivity variants (a constrained fit with $\omega_b = h^2/19$, the Cooke et al. BBN prior, a marginal 2×2 CMB prior) all miss by 2.3–3.5σ in the primary pipeline; in the rebuild they miss by 1.8–3.4σ, the constrained $\omega_b = h^2/19$ fit landing at 1.9σ and 1.8σ.

## Colliding clusters (T4)

Of the 16 mergers in the registered catalogue, applying the registered missing-data rule strictly leaves **one** cluster (MACS J0025.4-1222) with complete positions and uncertainties, and that one rests on reading Bradač et al. (2008)'s "galaxies" row as the galaxy centre. With $n_{\rm train} = 1$, $n_{\rm test} = 0$, **T4b is INCONCLUSIVE**; if that reading is rejected, $n_{\rm train} = 0$ and the registered clause gives FAIL. The primary pipeline's 13-cluster set ($n_{\rm train} = 8$, $n_{\rm test} = 5 < 6$, also INCONCLUSIVE) relied on default or zero positional errors where source papers gave none (Finding 2), so no claim is based on it. The young-merger offset test T4a was registered as exploratory before analysis. **Too few colliding clusters have complete measurements to test the lag.** This is the registered missing-data rule doing its job: without it, default or zero errors would have manufactured a test from incomplete inputs.

## Galaxy rotation curves (T5): the decisive failure

| | Primary | Rebuild |
|:--------------------------------------------------|:------------:|:------------:|
| Fitted $\sigma_{\rm ref}$ (88 training galaxies) | 9.21 kpc | 9.34 kpc |
| Held-out median $\chi^2_{\rm red}$ (87 test galaxies; PASS needs $\le 1.5$) | 45.1 | 45.9 |
| Fraction with $\chi^2_{\rm red} < 2$ (PASS needs $\ge 0.70$) | 6/87 | 6/87 |
| T5-B (width scaled to disk size): held-out median $\chi^2_{\rm red}$ | 23.7 | 23.4 |

**T5-A FAILS decisively in both pipelines**, and so does T5-B (7/87). The primary pipeline's frozen report states that even the best universal width chosen directly on the held-out set only reaches a median of about 37, so this is not a tuning problem. The cause is structural: under the saturation cap, the boost $g_{\rm tot}/g_{\rm bar}$ can never exceed 5.87, yet in the primary pipeline 67 of 175 SPARC galaxies have at least one radius where the observed boost exceeds it (442 of 3391 points, 13%; the rebuild's differently defined diagnostic gives 72 galaxies and 433 points). What this rules out is the registered Gaussian-blur shadow, whose cap is a mathematical property of the kernel; other forms of shadow are untested (Section 10).

**T5c (NGC 1052-DF2)** passes in both pipelines ($M(<2.7\,{\rm kpc}) \approx 0.99\times10^8\,M_\odot \le 2.9\times10^8\,M_\odot$), but only because the same wide blur that fails the rotation curves spreads DF2's shadow thin.

## Regional expansion (T6)

Across the 9 retained regions (491 supernovae), regional $H_0$ ranges from 72.5 to 75.1 km s$^{-1}$ Mpc$^{-1}$, with $\chi^2_{\rm het} = 8.93$ for 8 degrees of freedom, $p = 0.348$, identical in both pipelines. **No regional variation is detected: T6 FAILS.** The local all-sky value ($73.5 \pm 1.0$) sits 5.2σ above Planck as one uniform offset, not a patchwork.

# Model-level verdict

| Primary pillar | Chen reading of G9-b | Literal (a5) reading |
|:--------------------------|:-------------------------:|:-------------------------:|
| T1-L1 (unwinding curve) | INCONCLUSIVE | INCONCLUSIVE |
| T2-A (leak ratio) | **FAIL** | INCONCLUSIVE (3.2–3.4σ miss) |
| T4b (cluster lag) | INCONCLUSIVE (FAIL if the Bradač row is rejected) | same |
| T5-A (rotation curves) | **FAIL** | **FAIL** |
| **Model** | **FALSIFIED** | **FALSIFIED** |

Under the registered rule that one failed pillar falsifies the model, **version 1 of the Mandarano Model is falsified under every combination of the open readings**, through T5-A, which fails decisively in both independent pipelines. This holds with the gate-mapping rule read as written: a failed G9-b reaches T5 only if T2-A-Pantheon+ "fails to produce a converged $f_{\rm leak}$", and in both pipelines it converged (the rebuild logged this literal reading as deviation D11 before computing T5). The rebuild also logged an alternative reading, in which a failed G9-b invalidates $f_{\rm leak}$ itself. Under that reading the literal-(a5) column has T5-A INCONCLUSIVE, and with the Bradač row accepted the model verdict there is INCONCLUSIVE rather than falsified. Under the Chen reading the model is falsified either way. The T5-A failure does not hinge on the precise leak: the injection universes with the leak fixed at 1/6 fail in the same way (Section 8).

# Independent replication

The blind rebuild (frozen manifest `REBUILD_RESULTS_v1`, `93a154fb…`) was implemented from the frozen rulebook alone, under written blindness rules, with deliberately different numerical methods where the rulebook allowed a choice (an ODE integration of the Friedmann equation cross-checked by quadrature; a closed-form kernel validated against Monte Carlo and the non-central χ² CDF). It froze its results before any comparison.

| Test | Primary (Gemini) | Rebuild (Claude) | Agree? |
|:------------|:----------------------|:----------------------|:------------------|
| G9-a | PASS | PASS | Yes |
| G9-b | PASS (Chen $r_s$) | FAIL (literal a5) | No: Finding 1 |
| G9-c, G9-d | PASS | PASS | Yes |
| T1-L1 | INCONCLUSIVE | INCONCLUSIVE | Yes |
| T1-Sign | PASS | INCONCLUSIVE (gate) | Numbers yes |
| T2-A | FAIL ($-3.74/-3.58\sigma$) | INCONCLUSIVE ($-3.45/-3.22\sigma$) | Both past the 2σ line |
| T2-N1, T2-N2 | FAIL | FAIL | Yes |
| T4b | INCONCLUSIVE (13 clusters) | INCONCLUSIVE (1 cluster) | Verdict yes: Finding 2 |
| T5-A, T5-B | FAIL | FAIL | Yes |
| T5c | PASS | PASS | Yes |
| T6 | FAIL ($p = 0.3478$) | FAIL ($p = 0.34784$) | Yes |
| Model | FALSIFIED | FALSIFIED | Yes |

The two pipelines disagree on two substantive inputs (the G9-b benchmark values also differed; see the erratum in Section 9), and both disagreements are reported rather than resolved in either pipeline's favour: the sound-horizon convention in G9-b (Finding 1) and the treatment of missing cluster uncertainties (Finding 2). Neither changes the model-level verdict.

# Supplementary analysis: Bayesian head-to-head against ΛCDM

*Supplementary, not pre-registered. Background expansion only; it says nothing about galaxies, clusters or regional $H_0$, and the T5-A failure stands whatever it shows.*

## Design

A plan with all priors and settings was hashed (`HEAD_TO_HEAD_PLAN.sha256`, `60e3e9c6…`) and stamped before the first run. Four flat models were compared on the registered T1 likelihood (DESI DR2 BAO with joint Lyα + compressed CMB + one supernova compilation), under both sound-horizon readings:

- **ΛCDM:** $\Omega_{bc}$, $h$, $100\omega_b$.
- **CPL** ($w_0w_a$CDM), for context: plus $w_0 \in [-3, 1]$, $w_a \in [-3, 2]$, $w_0 + w_a < 0$.
- **M1, Law 1:** plus $\gamma_u \in [0, 2]$ (the registered range).
- **M2, the structural model:** Law 1 with $\Omega_b = 1/19$ imposed as $\omega_b = h^2/19$ inside the likelihood; free $\Omega_{bc}$, $h$, $\gamma_u$.

Priors were uniform ($\Omega_{bc} \in [0.10, 0.50]$, $h \in [0.50, 0.90]$, $100\omega_b \in [1.80, 2.60]$), with a prior-sensitivity repeat for M1 and M2 at $\gamma_u \in [0, 0.5]$. Evidence was computed with dynesty (static nested sampling, $n_{\rm live} = 1000$, $\Delta\ln Z = 0.01$), three seeds per run (72 runs). The adopted uncertainty on $\ln Z$ is the larger of dynesty's error and the seed scatter. Validation: the literal (a5) integral agrees between two quadratures to $1.6\times10^{-12}$; G9-b under (a5) fails at $0.571\sigma$ against the registered G9-b target for $h$, matching the rebuild's $0.577\sigma$; the nested-sampling ΛCDM $\chi^2_{\min}$ reproduces Stage 2 to within 0.0006.

## Results

$\ln B = \ln Z_{\rm model} - \ln Z_{\Lambda{\rm CDM}}$; negative values favour ΛCDM. Scale: $|\ln B| < 1$ inconclusive, 1–2.5 weak, 2.5–5 moderate, $> 5$ strong.

| SN | $r_s$ reading | CPL $\ln B$ | M1 $\ln B$ | M2 $\ln B$ |
|:------------------|:----------------|:--------------:|:--------------:|:--------------:|
| Pantheon+ | A (literal a5) | $-2.66 \pm 0.20$ | $-2.71 \pm 0.17$ | $-8.40 \pm 0.20$ |
| Pantheon+ | B (Chen) | $-2.49 \pm 0.18$ | $-2.61 \pm 0.17$ | $-7.01 \pm 0.29$ |
| DES-Dovekie | A (literal a5) | $-1.11 \pm 0.17$ | $-2.35 \pm 0.19$ | $-8.46 \pm 0.19$ |
| DES-Dovekie | B (Chen) | $-1.01 \pm 0.19$ | $-2.14 \pm 0.18$ | $-6.90 \pm 0.23$ |

Best-fit $\Delta\chi^2$ relative to ΛCDM (negative = better fit), same runs:

| SN | $r_s$ reading | CPL $\Delta\chi^2$ | M1 $\Delta\chi^2$ | M2 $\Delta\chi^2$ |
|:------------------|:----------------|:--------------:|:--------------:|:--------------:|
| Pantheon+ | A (literal a5) | $-6.9$ | $-1.4$ | $+14.3$ |
| Pantheon+ | B (Chen) | $-7.2$ | $-1.7$ | $+11.4$ |
| DES-Dovekie | A (literal a5) | $-9.6$ | $-2.1$ | $+14.7$ |
| DES-Dovekie | B (Chen) | $-9.9$ | $-2.6$ | $+11.4$ |

With the narrower prior $\gamma_u \in [0, 0.5]$, M1's $\ln B$ rises by 1.2–1.4 to between $-1.52$ and $-0.72$ (weak to inconclusive), and M2's to between $-7.09$ and $-5.44$ (still strong). Posterior means: M1 $\gamma_u = 0.041$–$0.047 \pm 0.025$; M2 $\gamma_u = 0.140$–$0.147 \pm 0.010$ with $h = 0.656 \pm 0.002$.

## Interpretation

1. **The unwinding curve alone (M1)** fits slightly better than ΛCDM but not by enough to pay for its extra parameter: ΛCDM is favoured weakly to moderately, and the preference shrinks to borderline with a narrower prior. The mainstream CPL alternative is in a similar position on evidence despite its larger $\chi^2$ improvement, a known feature of evidence comparisons with wide priors.
2. **The structural model (M2)**, with one-in-nineteen imposed, fits worse than ΛCDM in all eight configurations and is **strongly disfavoured** ($\ln B$ from $-6.9$ to $-8.5$ with the registered $\gamma_u$ range, and from $-5.4$ to $-7.1$ with the narrow prior).
3. **The sound-horizon ambiguity does not matter here:** both readings give the same conclusions.

# Supplementary analysis: blind injection tests

*Supplementary, not pre-registered in Stage 1. Truths, success criteria and analysis plan were each hashed and stamped before the first mock was analysed; nothing here changes a registered verdict.*

**Purpose.** To check that the frozen primary pipeline returns the right answers when the right answers are known, in the spirit of LIGO's blind injections. Forty-five mock universes (nine truths in three families, five noise realizations each) were generated from the real data's structure by the blind rebuild's own forward models and analysed blind by the frozen primary pipeline, so generator and analyser share no code. The record is three stamped manifests in order: the sealed truths and criteria (`PHASE3_INJECTION_v1.sha256`, Bitcoin block 973967), the analysis plan (`PHASE3_ANALYSIS_PLAN.sha256`, block 973969) and the frozen results (`PHASE3_RESULTS_v1.sha256`, block 974047); see Appendix A. One clarification was logged before the plan was stamped (P3-C1, no runs affected). The answer key was opened only after the results were frozen, and the results were scored read-only, with no rerun or refit.

**Families.** Cosmology: C1 ΛCDM (Planck 2018); C2 the model exactly true ($\gamma_u = 0.10$, $\Omega_b = 1/19$); C3 off-curve weakening dark energy ($w_0 = -0.75$, $w_a = -1$). Galaxies: G1 and G2 the shadow kernel true at $\sigma_{\rm ref} = 9$ and 3 kpc; G3 galaxies following the observed radial acceleration relation. Regional expansion: H1 no variation; H2 and H3 injected variation of $\pm 2$ and $\pm 5$ km s$^{-1}$ Mpc$^{-1}$.

**Locked criteria.** S1: each planted parameter lies inside its registered 95% interval ($[p_{2.5}, p_{97.5}]$) in at least 4 of 5 realizations, with mean bias below one mean posterior $\sigma$. S2: each truth returns its expected verdicts in at least 4 of 5 realizations. S3: the pipeline is validated if S1 and S2 hold for T5-A (G1–G3), T2-A (C1, C2) and T1-L1 (C2, C3). S4: real-data verdicts never change.

| Truth | Expected verdicts (S2) | Reading B | Reading A |
|:------------------|:-----------------------------------------|:--------------:|:--------------:|
| C1 ΛCDM | T2-A, T2-N1, T2-N2 FAIL; T1-L1 not PASS | 5/5 each | 5/5 each |
| C1 ΛCDM | $\gamma_u$ 95% interval includes 0 | 0/5 (miss) | 0/5 (miss) |
| C2 model true | T2-A PASS | 4/5 | 4/5 |
| C2 model true | T2-N1, T2-N2 PASS; T1-L1 not FAIL | 5/5 each | 5/5 each |
| C2 model true | T1-Sign PASS | 4/5 | 3/5 (miss) |
| C3 off-curve | T1-L1 FAIL; T1-Sign PASS; T2-A FAIL | 5/5 each | 5/5 each |
| G1, G2 kernel true | T5-A PASS | 5/5, 5/5 | |
| G3 RAR true | T5-A FAIL | 5/5 | |
| H1 null | T6 FAIL | 3/5 (miss) | |
| H3 $\pm 5$ | T6 PASS | 4/5 | |
| H2 $\pm 2$ | power (no criterion) | 4/5 PASS | |

**Galaxies (T5-A).** The planted kernel width is recovered to within 0.3% in every realization, with a mean bias of at most 0.05% ($\sigma_{\rm ref} = 8.976$–$9.013$ kpc for 9.0; $2.991$–$3.003$ kpc for 3.0), inside the 95% interval in at least 4 of 5 realizations under each of the three reported uncertainty methods (S1 holds). Of those three, only the training-galaxy bootstrap matches the actual realization-to-realization scatter (0.014 vs 0.017 kpc at 9 kpc; 0.005 vs 0.005 kpc at 3 kpc); the summed-$\chi^2_{\rm red}$ posterior overstates the uncertainty about fourfold and the total-$\chi^2$ posterior understates it by 1.4–1.7 times, so the bootstrap is the one to quote. When galaxies follow the radial acceleration relation, the model fails every time, at a held-out median $\chi^2_{\rm red}$ of 47.0–56.1, with 0–1% of galaxies below 2. The real data gave about 45. **The real-data failure is what this pipeline produces when galaxies obey the standard empirical law, and the pipeline passes the model whenever the model is true.**

**Cosmology.** Verdicts behave as registered. C3's off-curve dark energy is rejected by T1-L1 in 10 of 10 runs, with $w_0$ and $w_a$ recovered to within 0.2$\sigma$. In the model-true universes, T1-L1 never fails and T2-N1/N2 always pass. T2-A gives a direct reading of the real-data miss: the ΛCDM mocks give a mean tension of $-3.29\sigma$ (Reading B) and $-2.97\sigma$ (Reading A), scatter 0.52, while the model-true mocks give $-0.89\sigma$ and $-0.61\sigma$, scatter 1.02, worst run $-2.39\sigma$. The real runs ($-3.2$ to $-3.7\sigma$) sit with the ΛCDM mocks.

**Regional expansion (T6).** A $\pm 5$ variation is detected in every universe ($p_{\rm het} \approx 0$); the one INCONCLUSIVE came from the all-sky significance condition ($Z = 2.98$), from a bright (low-$H_0$) calibrator draw ($-1.9\sigma$) combined with a downward bias in the weighted all-sky mean: because each region's error scales with its own $H_0$, inverse-variance weighting favours low-$H_0$ regions, pulling the mean down by about 0.7 km s$^{-1}$ Mpc$^{-1}$ when real variation is large (about 0.25 at $\pm 2$, negligible when there is none, as in the real data). A $\pm 2$ variation reached $p_{\rm het} \le 0.013$ in all five universes. No universe without variation produced a false detection. The real data's $p = 0.348$ resembles the null universes.

**Misses, reported as findings and not patched.**

1. **$\Omega_{bc}$ from the Law 1 fit scatters more than its error bar in the model-true universes.** C2's Law 1 $\Omega_{bc}$ is centred on the truth (bias $\le 0.86\sigma$) but its realization-to-realization scatter is 1.8–1.9 times the quoted posterior $\sigma$ ($\chi^2 = 14.7$ and 16.9 for five realizations), so coverage is 3 of 5 in every run. It is one flag at roughly $p \approx 0.01$ among about 25 checks, so chance is not excluded. The fits that feed T2-A are well calibrated: pooled over all fifteen cosmology universes, the CPL and T2-A chains give standardized-residual scatter of 1.0–1.16 for $\Omega_{bc}$, and the T2-A tension statistic itself has scatter 0.90–0.93 about its expected value. The excess is largest in the Law 1 fit (3 of 5 in all four runs); the same model-true realizations also give 3 of 5 $\Omega_{bc}$ coverage in the DES-Dovekie CPL fits and in the Chen-reading DES-Dovekie T2-A chain (bias $1.03\sigma$). Five realizations cannot separate a real effect from chance.
2. **T2-A leans slightly toward FAIL when the model is true.** The model-true tensions average $-0.89\sigma$ and $-0.61\sigma$, about two standard errors below zero, which is the direction of the real-data miss. The real runs remain 2.3–2.8 scatters beyond the model-true distribution even using its widened scatter.
3. **A criterion that could not be met (design error).** The registered prior is $\gamma_u \in [0, 2]$ and the 95% interval runs from the 2.5th percentile, so for a ΛCDM truth at $\gamma_u = 0$ the interval can never include zero (observed lower edges 0.0007–0.0047). The same prior edge pushes the mean of $\gamma_u$ positive and, through degeneracies, shifts $h$ and $100\omega_b$ by 0.9–1.3$\sigma$, producing S1 misses on C1's Law 1 fit. Every C1 $\gamma_u$ posterior lies within about $1.9\sigma$ of zero, and C1's T1-L1 never passes.
4. **A criterion with 49% success for a perfect pipeline (design error).** T6 fails only when $p_{\rm het} > 0.3173$; with no variation $p_{\rm het}$ is uniform, so "FAIL in 4 of 5" happens about half the time by chance. The observed values (0.74, 0.24, 0.30, 0.71, 0.89) look uniform, and the two non-FAILs were INCONCLUSIVE, not false detections.
5. **T1-Sign is at its power edge for $w_0 = -0.90$.** Reading A returned 3 of 5 (posterior probabilities 0.90–0.95 against a 0.95 line). The ΛCDM mocks never produced a false T1-Sign PASS; the real data reached 0.996–0.999.
6. **The two sound-horizon readings differ systematically.** The mocks were generated with the rebuild's (a5) forward model. Across all thirty cosmology runs, the frozen Chen reading shifts the T2-A chain's $100\omega_b$ by $+0.011$ and the T2-A tension by $-0.29\sigma$ relative to (a5), which produces the Chen reading's small $100\omega_b$ biases ($1.0$–$1.3\sigma$) in its ΛCDM and T2-A chains. This is the G9-b reading difference already reported (Section 3) seen from the other side; the real-data T2-A runs remain past the FAIL line under both readings.
7. **A mild projection effect in CPL.** For a ΛCDM truth, CPL posterior means sit near $w_0 \approx -0.95$, $w_a \approx -0.18$ (about $0.9\sigma$, toward the quadrant DESI favours), from the prior bounds; one run crosses the 1$\sigma$ line ($1.05\sigma$). One of 27 regional-$H_0$ cells also misses coverage (3 of 5).

**Outcome.** T5-A, the pillar that falsifies version 1, is validated: S1 and S2 hold for G1, G2 and G3. **S3 as locked is not met**, because S1 misses on T1-L1 and T2-A (items 1, 3 and 6). Under S4 no real-data verdict changes. The practical reading is that the falsification rests on the validated pillar, that the real T2-A miss looks like a ΛCDM universe rather than a model-true one, and that the cosmology error bars should be treated with the caution in item 1. **Independent re-score.** A separate Gemini session, given only the six frozen files (results, answer key, sealed criteria, analysis plan and both manifests) and none of this scoring, verified every hash, wrote its own scoring code and reproduced every S1 and S2 count above, the G3 medians, and S3 as not met under the locked reading. Its additional checks are folded into items 1 and 6 and the galaxy and regional paragraphs. One further suggestion from the re-score, that the mock generator left the massive neutrino out of the sound-horizon integral, was checked against the rebuild's code and against CAMB and did not hold: the neutrino enters every background calculation through its exact Fermi–Dirac density, the generator's values reproduce to about $10^{-10}$, and CAMB agrees to 0.007 Mpc. Two of the misses are flaws in the injection design, not the pipeline; version 2's injection design will check every criterion's pass rate on a perfect pipeline before it is locked, and will use more realizations per truth.

# Limitations and process record

The study is not described as fully blind, manipulation-free or free of researcher choices. In particular:

1. **Public data.** Several datasets were public before the rules were written, and the T2 failures were forecast from published numbers in Stage 1. The blind tests are T5-A/B (held-out galaxies), T4b and T6.
2. **The G9-b sound-horizon departure** (Finding 1) was introduced during the gate stage, logged as a bug fix, and not logged as a departure from (a5) at the time. Both readings are reported; the verdict holds under both.
3. **The G9-b target value (erratum).** The registered rule cites Chen et al.'s "Table 2" posteriors, but that paper has no Table 2. The rebuild used the Planck 2018 TT,TE,EE+lowE posteriors that Chen et al. compare against ($h = 0.6727 \pm 0.0060$; rebuild deviation D2), and the primary pipeline's code labels the same $h$ as Chen's Table 2. The frozen primary gate output (`validation_gates_g9_final.json`) shows that the primary pipeline actually compared against the Planck 2018 TT,TE,EE+lowE+lensing values ($h = 0.6736 \pm 0.0054$, $\Omega_m = 0.3153 \pm 0.0073$). Against the registered target, the primary pipeline's Chen-reading offset on $h$ is $0.17\sigma$ rather than $0.025\sigma$ (still a PASS), and its literal-(a5) offset is $0.571\sigma$ (FAIL), matching the rebuild's $0.577\sigma$. G9-b's outcome is unchanged under either target and either reading.
4. **Cluster inputs** were hand-compiled by an analyst who knew the well-known mergers, with default or zero errors where papers gave none (Finding 2). Eight replacement cluster source archives were downloaded after the data freeze (deviation D1) and are covered by later results manifests. More fundamentally, **T4 was under-powered by design**: the registered 16-merger catalogue was never checked, before registration, for how many mergers report gas, galaxy and lensing positions with uncertainties, and a simple pre-registration power check would have shown that the test could not reach its required sample size. The INCONCLUSIVE verdict is the correct outcome of the rules, but the pillar should not have been registered as decisive-capable without that check; version 2's pre-registration adds a power check for every pillar.
5. **Post-gate refactoring.** The cosmology code was refactored after the first gate run; all four gates were re-run on the final code and pass. The parameter-fixing script ran twice. An earlier run, not recorded in the activity log, wrote the freeze files by 10:27 UTC; after two logged code edits (a vectorized distance integral and an updated convergence diagnostic) the logged run overwrote them without a backup, finishing at 11:06 UTC, and its `frozen_at` field (10:29:35 UTC) records when that run started. The logs and file creation times place every test after 11:06 UTC: the first test-output file was created at 11:45 UTC. The structural, cluster and regional values could not have differed between the two runs; whether the T2 and T5 training values did is not recorded. One analysis script (the Part 10 scoring and figure script) was completed and edited after the parameter freeze (figure formatting and a dictionary key-lookup fix; deviation C5); no frozen parameter or verdict is affected.
6. **AI execution.** The agents' chat summaries repeatedly misstated numbers that their files had correct, and one comparison draft was first written from a summary before the files were available; a separate check caught two errors in it (these episodes are recorded in the planning session's history rather than in the pipelines' logs). All reported numbers were checked against frozen files. During the head-to-head, the primary agent had read the comparison document, so its literal-(a5) result reproduces a known target rather than being a blind second confirmation.
7. **Shared training data.** The two pipelines come from different model families, but such models learn from much of the same public material; much of the independence comes from the blindness rules and from deliberately different numerical methods.

# What version 1 points to (exploratory)

No unregistered mechanism is used to soften any verdict. Two directions are noted for future, separately registered tests: the vacuum-proportional dark-sector transfer recorded in Stage 1 as exploratory, which allows an effective crossing of $w = -1$ while keeping the bare unwinding non-phantom; and a non-Gaussian kernel, named as an unregistered candidate in the input equation sheet, which the T5 result suggests would need to be acceleration-dependent, since the Gaussian kernel's saturation cap cannot produce flat outer rotation curves. For reference, the empirical radial acceleration relation (McGaugh et al. 2016) reaches a held-out median $\chi^2_{\rm red}$ of 9.4 on the same SPARC split. A design charter for version 2 has been written, and a list of test datasets that version 2 may not use during its design (fenced data) was hashed and stamped on 31 October 2026 (`MULTIVERSE_V2_FENCE_v1.sha256`). Version 2's complete design log, with a timestamp for every entry, is released with this record; nothing in it has been tested. The closest published idea to version 2's dark-energy sector is cosmologically coupled black holes (Farrah et al. 2023; Croker et al. 2024) *[Published speculation]*, and version 2's registered comparison will include it by name. Its observational case has been challenged by black-hole mass constraints from Gaia (Andrae & El-Badry 2023), a globular cluster (Rodriguez 2023) and gravitational-wave observations (Amendola et al. 2024).

# Conclusion

Under rules frozen before any data were downloaded and anchored in the Bitcoin blockchain before any result existed, version 1 of the Mandarano Model is falsified (with the gate rules read as written; Section 5), through the decisive failure of its galaxy rotation-curve pillar in two independent pipelines, alongside the 3.9σ and 3.7σ failures of its one-in-nineteen predictions and a 3.2–3.7σ miss in its leak ratio. Its dark-energy curve remains neither confirmed nor ruled out, and on Bayesian evidence ΛCDM is preferred over every tested version of its background expansion, except two narrow-prior runs where the comparison is inconclusive. The value of the exercise is that all of this can be checked by anyone.

# Appendix A: Cryptographic record {.unnumbered}

The complete record, with every manifest, proof and file listed below, is archived on Zenodo at [doi.org/10.5281/zenodo.23868218](https://doi.org/10.5281/zenodo.23868218).

| Manifest | SHA-256 (prefix) | Anchor |
|:-------------------------------------|:----------------------|:----------------------|
| `PREREG_v3.sha256` (rulebook before the third pre-data review's fixes) | `ab445f9a…` | Bitcoin blocks 973793, 973821 |
| `PREREG_v4.sha256` (rulebook) | `53ce966a…` | Bitcoin blocks 973800, 973821 |
| `DATA_MANIFEST.sha256` | `73135698…` | Bitcoin blocks 973800, 973821 |
| `RESULTS_v1.sha256` | `b02000c9…` | Bitcoin block 973822 |
| `RESULTS_v2` to `v4.sha256` | `499026f0…`, `baec3ff5…`, `806d1ef1…` | v2: Bitcoin blocks 973830, 973864; v3 and v4: 973844, 973864 |
| `RESULTS_v5.sha256` | `1ce42ac5…` | Bitcoin blocks 973844, 973864 |
| `REBUILD_RESULTS_v1.sha256` | `93a154fb…` | Bitcoin block 973824 |
| `HEAD_TO_HEAD_PLAN.sha256` | `60e3e9c6…` | Bitcoin blocks 973880, 973901 |
| `HEAD_TO_HEAD_RESULTS_v1.sha256` | `6f3b76f6…` | Bitcoin blocks 973958, 973973 |
| `PHASE3_SPEC_LOCK_v1.sha256` (criteria locked) | `57a25000…` | Bitcoin blocks 973966, 973973 |
| `PHASE3_INJECTION_v1.sha256` (sealed truths) | `ca63ae04…` | Bitcoin blocks 973967, 974019 |
| `PHASE3_ANALYSIS_PLAN.sha256` | `4eab04e3…` | Bitcoin blocks 973969, 973973 |
| `PHASE3_RESULTS_v1.sha256` | `8d4a38df…` | Bitcoin blocks 974047, 974048 |
| `MULTIVERSE_V2_FENCE_v1.sha256` | `6d5c5879…` | Bitcoin blocks 973965, 973973 |

Full 64-character hashes appear in the release files.

# Appendix B: How to verify {.unnumbered}

1. **Fingerprints.** For each manifest, recompute the SHA-256 of every listed file (e.g. `sha256sum -c PREREG_v4.sha256`) and confirm they match. Four details avoid false alarms: append-only logs are checked over the frozen prefix length the manifest records (`head -c N file | sha256sum`); some manifest lines carry trailing `#` comments to remove first; the superseded manifests (`RESULTS_v1` to `v4`, `PREREG_v1` to `v3`) list earlier file versions, which ship in the release's archive folder; and two results manifests list plan proofs by their pre-upgrade fingerprint, which ship as `.ots.bak` beside the upgraded proofs.
2. **Timestamps.** With the OpenTimestamps client, run `ots verify <manifest>.sha256.ots`. It reports the Bitcoin block whose time the manifest existed by.
3. **Order.** The rulebook (`PREREG_v4`) and the data manifest share their first Bitcoin block (973800), so the blockchain alone cannot order them; their order (rulebook submitted 08:44 UTC, data downloaded 08:56–08:57 UTC and stamped 08:59 UTC) rests on the activity log. The previous rulebook version, `PREREG_v3`, is anchored earlier, in block 973793 (08:22 UTC). Every results manifest is anchored later (block 973822 onward), and Phase 3's sealed truths precede its analysis plan, which precedes its results.
4. **Data.** Re-download the public datasets with the release's download script and check them against `DATA_MANIFEST.sha256`.
5. **Results.** Rerun the pipelines from the release and compare against the frozen results files.

# References {.unnumbered}

Amendola, L., Rodrigues, D. C., Kumar, S., & Quartin, M. 2024, MNRAS, 528, 2377 · Andrae, R., & El-Badry, K. 2023, A&A, 673, L10 · Bradač, M., et al. 2008, ApJ, 687, 959 · Brout, D., et al. 2022, ApJ, 938, 110 · Chen, L., Huang, Q.-G., & Wang, K. 2019, JCAP, 02, 028 · Chevallier, M., & Polarski, D. 2001, IJMPD, 10, 213 · Cooke, R. J., Pettini, M., & Steidel, C. C. 2018, ApJ, 855, 102 · Croker, K. S., et al. 2024, JCAP, 10, 094 (arXiv:2405.12282) · DESI Collaboration 2025, arXiv:2503.14738 · DESI Collaboration 2026, arXiv:2607.27410 · Farrah, D., et al. 2023, ApJL, 944, L31 (arXiv:2302.07878) · Lelli, F., McGaugh, S. S., & Schombert, J. M. 2016, AJ, 152, 157 · Linder, E. V. 2003, PRL, 90, 091301 · McGaugh, S. S., Lelli, F., & Schombert, J. M. 2016, PRL, 117, 201101 · Planck Collaboration 2020, A&A, 641, A6 · Popovic, B., et al. 2025 (DES-SN5YR Dovekie) · Riess, A. G., et al. 2022, ApJ, 934, L7 · Rodriguez, C. L. 2023, ApJL (arXiv:2302.12386) · Schöneberg, N. 2024, JCAP, 06, 006 · Skilling, J. 2006, Bayesian Analysis, 1, 833 · Speagle, J. S. 2020, MNRAS, 493, 3132 (dynesty) · van Dokkum, P., et al. 2018, Nature, 555, 629 · Wittman, D., Golovich, N., & Dawson, W. A. 2018, ApJ, 869, 104. The full cluster-source reference list is in the frozen results report.
