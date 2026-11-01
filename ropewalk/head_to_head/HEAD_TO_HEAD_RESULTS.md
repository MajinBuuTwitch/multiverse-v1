---
title: "MULTIVERSE v1: Head-to-Head Bayesian Evidence Comparison Results (HEAD_TO_HEAD_RESULTS.md)"
subtitle: "Supplementary Analysis, Not Pre-Registered — Background Expansion Comparison Against Standard ΛCDM"
author: "Gregory Mandarano / WickedAI — Executed by Gemini 4 Argon"
date: "2026-10-30"
---

# MULTIVERSE v1: HEAD-TO-HEAD RESULTS (`supplementary analysis, not pre-registered`)

> **STATUS LABEL:** **Supplementary analysis, not pre-registered.**
>
> **SCOPE STATEMENT:** This report is a supplementary Bayesian evidence comparison of **cosmological background expansion only** (`DESI DR2 BAO` with joint Ly$\alpha$ BAO+AP + `Chen, Huang & Wang 2019` compressed CMB distance priors + one supernova compilation per run: `Pantheon+` or `DES-Dovekie`, never combined). It says **nothing** about galaxy rotation curves (`T5-A`), dissociative galaxy cluster mergers (`T4b`), or regional $H_0$ heterogeneity (`T6`). **The `T5-A` rotation-curve failure and the Stage 2 overall verdict (`MODEL FALSIFIED (FAIL)`, frozen in `RESULTS_v5.sha256`) stand unchanged regardless of what this background comparison shows.**

---

## 1. Main Head-to-Head Tables (Per Supernova Compilation and Per $r_s$ Reading)

**Conventions & Priors (`HEAD_TO_HEAD_PLAN.md`):**
- All models are spatially flat FLRW models (`[Established]` metric, `[Model Ansatz]` dark-sector mappings for `M1` and `M2`) with $\Omega_{bc} \equiv \Omega_b + \Omega_{\rm dm} \sim \mathcal{U}(0.10, 0.50)$, $h \sim \mathcal{U}(0.50, 0.90)$, and massive neutrinos added separately ($\sum m_\nu = 0.06\text{ eV}$, $\Omega_{\nu,0} = \omega_{\nu,{\rm mass},0}/h^2$).
- For $\Lambda\text{CDM}$, $\text{CPL}$, and $\text{M1}$, $100\omega_b \sim \mathcal{U}(1.80, 2.60)$ is free. For $\text{M2}$ (the structural version of the model), $\Omega_b = 1/19$ is imposed inside the likelihood as $\omega_b = h^2/19$ ($100\omega_b = 100h^2/19$).
- In the main runs below, $\text{M1}$ and $\text{M2}$ use the registered `T1-L1` prior $\gamma_u \sim \mathcal{U}(0, 2)$, and $\text{CPL}$ uses the uniform prior on $w_0 \in [-3, 1], w_a \in [-3, 2]$ with $w_0 + w_a < 0$ (area $15.5$).
- Each run is aggregated across 3 fixed seeds (`20261030`, `20261031`, `20261032`) using static `dynesty` (`nlive = 1000`, `bound = 'multi'`, `sample = 'rwalk'`, `dlogz = 0.01`). The adopted uncertainty on $\ln Z$ is $\sigma_{\ln Z} = \max(\sigma_{\rm dyn}, \sigma_{\rm scatter})$, where $\sigma_{\rm dyn}$ is the RMS of `dynesty`'s internal error and $\sigma_{\rm scatter}$ is the sample standard deviation (`ddof=1`) across the 3 seeds. Positive $\ln B = \ln Z_{\rm model} - \ln Z_{\Lambda\text{CDM}} > 0$ means the model is favoured over $\Lambda\text{CDM}$; negative $\ln B < 0$ means $\Lambda\text{CDM}$ is favoured over the model.

### 1.1.A — `Pantheon+` · Reading A (Literal Registered `a5` Full Sound-Horizon Integral)

| Model | $d$ | $\ln Z$ (mean) | $\sigma_{\rm dyn}$ | $\sigma_{\rm scatter}$ | $\sigma_{\ln Z}$ (adopted) | $\ln B$ vs. $\Lambda\text{CDM}$ | Best-Fit $\chi^2_{\min}$ (NS / Opt) | $\Delta\chi^2_{\min}$ vs. $\Lambda\text{CDM}$ (NS / Opt) | Key Posterior Mean $\pm 1\sigma$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| $\Lambda\text{CDM}$ | 3 | $-715.315$ | $0.111$ | $0.055$ | $0.111$ | $0.000$ (baseline) | $1404.28$ / $1404.28$ | $0.00$ / $0.00$ | $\Omega_{bc} = 0.3029 ± 0.0038$, $h = 0.6843 ± 0.0029$, $100\omega_b = 2.2486 ± 0.0123$ |
| $\text{CPL}$ ($w_0w_a\text{CDM}$) | 5 | $-717.977$ | $0.134$ | $0.167$ | $0.167$ | $-2.662 \pm 0.201$ | $1397.38$ / $1397.36$ | $-6.91$ / $-6.92$ | $w_0 = -0.8553 ± 0.0556$, $w_a = -0.5309 ± 0.2177$ ($\Omega_{bc} = 0.3116 ± 0.0058$, $h = 0.6773 ± 0.0060$) |
| $\text{M1}$ (Law 1, $\gamma_u \in [0, 2]$) | 4 | $-718.024$ | $0.125$ | $0.113$ | $0.125$ | $-2.709 \pm 0.168$ | $1402.90$ / $1402.90$ | $-1.38$ / $-1.39$ | $\gamma_u = 0.0414 ± 0.0245$ ($\Omega_{bc} = 0.3083 ± 0.0050$, $h = 0.6770 ± 0.0052$, $100\omega_b = 2.2534 ± 0.0127$) |
| $\text{M2}$ (Law 1 + $\Omega_b = 1/19$, $\gamma_u \in [0, 2]$) | 3 | $-723.715$ | $0.117$ | $0.164$ | $0.164$ | $-8.400 \pm 0.199$ | $1418.62$ / $1418.62$ | $+14.33$ / $+14.33$ | $\gamma_u = 0.1469 ± 0.0103$, $\Omega_b h^2 = 0.022666 ± 0.000126$ ($100\omega_b = 2.2666 ± 0.0126$, $\Omega_{bc} = 0.3267 ± 0.0027$, $h = 0.6562 ± 0.0018$) |

### 1.1.B — `Pantheon+` · Reading B (`Chen, Huang & Wang 2019` Early-Universe Form in Frozen Code)

| Model | $d$ | $\ln Z$ (mean) | $\sigma_{\rm dyn}$ | $\sigma_{\rm scatter}$ | $\sigma_{\ln Z}$ (adopted) | $\ln B$ vs. $\Lambda\text{CDM}$ | Best-Fit $\chi^2_{\min}$ (NS / Opt) | $\Delta\chi^2_{\min}$ vs. $\Lambda\text{CDM}$ (NS / Opt) | Key Posterior Mean $\pm 1\sigma$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| $\Lambda\text{CDM}$ | 3 | $-715.855$ | $0.112$ | $0.114$ | $0.114$ | $0.000$ (baseline) | $1405.34$ / $1405.34$ | $0.00$ / $0.00$ | $\Omega_{bc} = 0.3012 ± 0.0038$, $h = 0.6832 ± 0.0029$, $100\omega_b = 2.2504 ± 0.0124$ |
| $\text{CPL}$ ($w_0w_a\text{CDM}$) | 5 | $-718.342$ | $0.133$ | $0.052$ | $0.133$ | $-2.487 \pm 0.176$ | $1398.18$ / $1398.18$ | $-7.17$ / $-7.17$ | $w_0 = -0.8526 ± 0.0560$, $w_a = -0.5254 ± 0.2173$ ($\Omega_{bc} = 0.3103 ± 0.0058$, $h = 0.6755 ± 0.0061$) |
| $\text{M1}$ (Law 1, $\gamma_u \in [0, 2]$) | 4 | $-718.461$ | $0.125$ | $0.067$ | $0.125$ | $-2.606 \pm 0.170$ | $1403.63$ / $1403.63$ | $-1.71$ / $-1.71$ | $\gamma_u = 0.0439 ± 0.0252$ ($\Omega_{bc} = 0.3069 ± 0.0050$, $h = 0.6755 ± 0.0052$, $100\omega_b = 2.2556 ± 0.0128$) |
| $\text{M2}$ (Law 1 + $\Omega_b = 1/19$, $\gamma_u \in [0, 2]$) | 3 | $-722.870$ | $0.118$ | $0.269$ | $0.269$ | $-7.015 \pm 0.292$ | $1416.78$ / $1416.78$ | $+11.44$ / $+11.43$ | $\gamma_u = 0.1403 ± 0.0104$, $\Omega_b h^2 = 0.022675 ± 0.000126$ ($100\omega_b = 2.2675 ± 0.0126$, $\Omega_{bc} = 0.3238 ± 0.0027$, $h = 0.6564 ± 0.0018$) |

### 1.2.A — `DES-Dovekie` · Reading A (Literal Registered `a5` Full Sound-Horizon Integral)

| Model | $d$ | $\ln Z$ (mean) | $\sigma_{\rm dyn}$ | $\sigma_{\rm scatter}$ | $\sigma_{\ln Z}$ (adopted) | $\ln B$ vs. $\Lambda\text{CDM}$ | Best-Fit $\chi^2_{\min}$ (NS / Opt) | $\Delta\chi^2_{\min}$ vs. $\Lambda\text{CDM}$ (NS / Opt) | Key Posterior Mean $\pm 1\sigma$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| $\Lambda\text{CDM}$ | 3 | $-838.149$ | $0.112$ | $0.028$ | $0.112$ | $0.000$ (baseline) | $1649.80$ / $1649.80$ | $0.00$ / $0.00$ | $\Omega_{bc} = 0.3033 ± 0.0037$, $h = 0.6840 ± 0.0029$, $100\omega_b = 2.2480 ± 0.0124$ |
| $\text{CPL}$ ($w_0w_a\text{CDM}$) | 5 | $-839.256$ | $0.133$ | $0.048$ | $0.133$ | $-1.107 \pm 0.174$ | $1640.22$ / $1640.21$ | $-9.58$ / $-9.59$ | $w_0 = -0.8263 ± 0.0573$, $w_a = -0.6388 ± 0.2340$ ($\Omega_{bc} = 0.3132 ± 0.0055$, $h = 0.6759 ± 0.0055$) |
| $\text{M1}$ (Law 1, $\gamma_u \in [0, 2]$) | 4 | $-840.501$ | $0.125$ | $0.149$ | $0.149$ | $-2.352 \pm 0.186$ | $1647.68$ / $1647.67$ | $-2.13$ / $-2.13$ | $\gamma_u = 0.0439 ± 0.0240$ ($\Omega_{bc} = 0.3086 ± 0.0047$, $h = 0.6766 ± 0.0049$, $100\omega_b = 2.2534 ± 0.0128$) |
| $\text{M2}$ (Law 1 + $\Omega_b = 1/19$, $\gamma_u \in [0, 2]$) | 3 | $-846.608$ | $0.117$ | $0.149$ | $0.149$ | $-8.459 \pm 0.187$ | $1664.53$ / $1664.53$ | $+14.72$ / $+14.72$ | $\gamma_u = 0.1465 ± 0.0103$, $\Omega_b h^2 = 0.022678 ± 0.000124$ ($100\omega_b = 2.2678 ± 0.0124$, $\Omega_{bc} = 0.3266 ± 0.0027$, $h = 0.6564 ± 0.0018$) |

### 1.2.B — `DES-Dovekie` · Reading B (`Chen, Huang & Wang 2019` Early-Universe Form in Frozen Code)

| Model | $d$ | $\ln Z$ (mean) | $\sigma_{\rm dyn}$ | $\sigma_{\rm scatter}$ | $\sigma_{\ln Z}$ (adopted) | $\ln B$ vs. $\Lambda\text{CDM}$ | Best-Fit $\chi^2_{\min}$ (NS / Opt) | $\Delta\chi^2_{\min}$ vs. $\Lambda\text{CDM}$ (NS / Opt) | Key Posterior Mean $\pm 1\sigma$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| $\Lambda\text{CDM}$ | 3 | $-838.697$ | $0.112$ | $0.130$ | $0.130$ | $0.000$ (baseline) | $1650.96$ / $1650.96$ | $0.00$ / $0.00$ | $\Omega_{bc} = 0.3017 ± 0.0037$, $h = 0.6829 ± 0.0029$, $100\omega_b = 2.2496 ± 0.0124$ |
| $\text{CPL}$ ($w_0w_a\text{CDM}$) | 5 | $-839.705$ | $0.133$ | $0.060$ | $0.133$ | $-1.008 \pm 0.186$ | $1641.04$ / $1641.03$ | $-9.92$ / $-9.93$ | $w_0 = -0.8239 ± 0.0560$, $w_a = -0.6319 ± 0.2269$ ($\Omega_{bc} = 0.3121 ± 0.0054$, $h = 0.6740 ± 0.0055$) |
| $\text{M1}$ (Law 1, $\gamma_u \in [0, 2]$) | 4 | $-840.840$ | $0.125$ | $0.046$ | $0.125$ | $-2.143 \pm 0.180$ | $1648.39$ / $1648.38$ | $-2.57$ / $-2.58$ | $\gamma_u = 0.0473 ± 0.0246$ ($\Omega_{bc} = 0.3074 ± 0.0048$, $h = 0.6749 ± 0.0050$, $100\omega_b = 2.2557 ± 0.0130$) |
| $\text{M2}$ (Law 1 + $\Omega_b = 1/19$, $\gamma_u \in [0, 2]$) | 3 | $-845.602$ | $0.117$ | $0.188$ | $0.188$ | $-6.905 \pm 0.228$ | $1662.34$ / $1662.34$ | $+11.38$ / $+11.37$ | $\gamma_u = 0.1402 ± 0.0104$, $\Omega_b h^2 = 0.022687 ± 0.000123$ ($100\omega_b = 2.2687 ± 0.0123$, $\Omega_{bc} = 0.3236 ± 0.0026$, $h = 0.6565 ± 0.0018$) |

---

## 2. Prior-Sensitivity Table for `M1` and `M2` ($\gamma_u \in [0, 2]$ vs. $\gamma_u \in [0, 0.5]$)

Because the likelihood for $\gamma_u$ is concentrated well below $\gamma_u = 0.5$ ($\gamma_u \sim 0.03\text{--}0.05$), narrowing the uniform prior width by a factor of $4$ from $[0, 2]$ to $[0, 0.5]$ reduces the prior-volume (Occam) penalty by $\approx \ln(2.0 / 0.5) = \ln 4 \approx +1.386$ in $\ln Z$ and $\ln B$ while leaving the best-fit $\chi^2_{\min}$ and posterior moments unchanged:

| SN Compilation | $r_s$ Reading | Model | Prior $\gamma_u$ | $\ln Z$ (mean $\pm$ adopted) | $\sigma_{\rm dyn}$ / $\sigma_{\rm scatter}$ | $\ln B$ vs. $\Lambda\text{CDM}$ | Shift $\Delta\ln B(\text{narrow} - \text{wide})$ | Best-Fit $\chi^2_{\min}$ (NS / Opt) | Posterior $\gamma_u$ and Derived $\Omega_b h^2$ (for `M2`) |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| `Pantheon+` | Reading A | `M1` | $[0, 2.0]$ (wide) | $-718.024 \pm 0.125$ | $0.125$ / $0.113$ | $-2.709 \pm 0.168$ | — | $1402.90$ / $1402.90$ | $\gamma_u = 0.0414 ± 0.0245$ |
| `Pantheon+` | Reading A | `M1` | $[0, 0.5]$ (narrow) | $-716.834 \pm 0.214$ | $0.120$ / $0.214$ | $-1.519 \pm 0.241$ | $+1.190$ | $1402.90$ / $1402.90$ | $\gamma_u = 0.0422 ± 0.0248$ |
| `Pantheon+` | Reading A | `M2` | $[0, 2.0]$ (wide) | $-723.715 \pm 0.164$ | $0.117$ / $0.164$ | $-8.400 \pm 0.199$ | — | $1418.62$ / $1418.62$ | $\gamma_u = 0.1469 ± 0.0103$, $\Omega_b h^2 = 0.022666 ± 0.000126$ ($100\omega_b = 2.2666 ± 0.0126$) |
| `Pantheon+` | Reading A | `M2` | $[0, 0.5]$ (narrow) | $-722.377 \pm 0.189$ | $0.111$ / $0.189$ | $-7.062 \pm 0.220$ | $+1.338$ | $1418.62$ / $1418.62$ | $\gamma_u = 0.1468 ± 0.0104$, $\Omega_b h^2 = 0.022667 ± 0.000124$ ($100\omega_b = 2.2667 ± 0.0124$) |
| `Pantheon+` | Reading B | `M1` | $[0, 2.0]$ (wide) | $-718.461 \pm 0.125$ | $0.125$ / $0.067$ | $-2.606 \pm 0.170$ | — | $1403.63$ / $1403.63$ | $\gamma_u = 0.0439 ± 0.0252$ |
| `Pantheon+` | Reading B | `M1` | $[0, 0.5]$ (narrow) | $-717.128 \pm 0.178$ | $0.119$ / $0.178$ | $-1.273 \pm 0.212$ | $+1.333$ | $1403.63$ / $1403.63$ | $\gamma_u = 0.0441 ± 0.0252$ |
| `Pantheon+` | Reading B | `M2` | $[0, 2.0]$ (wide) | $-722.870 \pm 0.269$ | $0.118$ / $0.269$ | $-7.015 \pm 0.292$ | — | $1416.78$ / $1416.78$ | $\gamma_u = 0.1403 ± 0.0104$, $\Omega_b h^2 = 0.022675 ± 0.000126$ ($100\omega_b = 2.2675 ± 0.0126$) |
| `Pantheon+` | Reading B | `M2` | $[0, 0.5]$ (narrow) | $-721.372 \pm 0.111$ | $0.111$ / $0.102$ | $-5.517 \pm 0.159$ | $+1.498$ | $1416.78$ / $1416.78$ | $\gamma_u = 0.1404 ± 0.0104$, $\Omega_b h^2 = 0.022678 ± 0.000124$ ($100\omega_b = 2.2678 ± 0.0124$) |
| `DES-Dovekie` | Reading A | `M1` | $[0, 2.0]$ (wide) | $-840.501 \pm 0.149$ | $0.125$ / $0.149$ | $-2.352 \pm 0.186$ | — | $1647.68$ / $1647.67$ | $\gamma_u = 0.0439 ± 0.0240$ |
| `DES-Dovekie` | Reading A | `M1` | $[0, 0.5]$ (narrow) | $-839.125 \pm 0.177$ | $0.119$ / $0.177$ | $-0.977 \pm 0.210$ | $+1.376$ | $1647.67$ / $1647.67$ | $\gamma_u = 0.0441 ± 0.0241$ |
| `DES-Dovekie` | Reading A | `M2` | $[0, 2.0]$ (wide) | $-846.608 \pm 0.149$ | $0.117$ / $0.149$ | $-8.459 \pm 0.187$ | — | $1664.53$ / $1664.53$ | $\gamma_u = 0.1465 ± 0.0103$, $\Omega_b h^2 = 0.022678 ± 0.000124$ ($100\omega_b = 2.2678 ± 0.0124$) |
| `DES-Dovekie` | Reading A | `M2` | $[0, 0.5]$ (narrow) | $-845.241 \pm 0.111$ | $0.111$ / $0.108$ | $-7.092 \pm 0.157$ | $+1.367$ | $1664.53$ / $1664.53$ | $\gamma_u = 0.1465 ± 0.0104$, $\Omega_b h^2 = 0.022678 ± 0.000124$ ($100\omega_b = 2.2678 ± 0.0124$) |
| `DES-Dovekie` | Reading B | `M1` | $[0, 2.0]$ (wide) | $-840.840 \pm 0.125$ | $0.125$ / $0.046$ | $-2.143 \pm 0.180$ | — | $1648.39$ / $1648.38$ | $\gamma_u = 0.0473 ± 0.0246$ |
| `DES-Dovekie` | Reading B | `M1` | $[0, 0.5]$ (narrow) | $-839.421 \pm 0.142$ | $0.119$ / $0.142$ | $-0.724 \pm 0.193$ | $+1.419$ | $1648.39$ / $1648.38$ | $\gamma_u = 0.0472 ± 0.0246$ |
| `DES-Dovekie` | Reading B | `M2` | $[0, 2.0]$ (wide) | $-845.602 \pm 0.188$ | $0.117$ / $0.188$ | $-6.905 \pm 0.228$ | — | $1662.34$ / $1662.34$ | $\gamma_u = 0.1402 ± 0.0104$, $\Omega_b h^2 = 0.022687 ± 0.000123$ ($100\omega_b = 2.2687 ± 0.0123$) |
| `DES-Dovekie` | Reading B | `M2` | $[0, 0.5]$ (narrow) | $-844.135 \pm 0.110$ | $0.110$ / $0.056$ | $-5.437 \pm 0.170$ | $+1.468$ | $1662.34$ / $1662.34$ | $\gamma_u = 0.1403 ± 0.0104$, $\Omega_b h^2 = 0.022686 ± 0.000124$ ($100\omega_b = 2.2686 ± 0.0124$) |

---

## 3. Plain-Language Verdicts on the Jeffreys / Kass–Raftery Scale

**Scale (`ARGON_HEAD_TO_HEAD_HANDOFF.txt`):** $|\ln B| < 1.0$ = **inconclusive**; $1.0 \le |\ln B| < 2.5$ = **weak**; $2.5 \le |\ln B| \le 5.0$ = **moderate**; $|\ln B| > 5.0$ = **strong**. Positive $\ln B > 0$ favours the alternative model over $\Lambda\text{CDM}$; negative $\ln B < 0$ favours $\Lambda\text{CDM}$.

### 3.1 Main Runs ($\gamma_u \in [0, 2]$)

- **Pantheon+ · Reading A · CPL (w0waCDM) vs. ΛCDM:** **Moderate** (`|ln B| = 2.662`) — **ΛCDM** is favoured over **CPL (w0waCDM)** (moderate evidence, ln B = -2.662 ± 0.201).
- **Pantheon+ · Reading A · M1 (Law 1, γ_u ∈ [0, 2]) vs. ΛCDM:** **Moderate** (`|ln B| = 2.709`) — **ΛCDM** is favoured over **M1 (Law 1, γ_u ∈ [0, 2])** (moderate evidence, ln B = -2.709 ± 0.168).
- **Pantheon+ · Reading A · M2 (Law 1 + Ω_b = 1/19, γ_u ∈ [0, 2]) vs. ΛCDM:** **Strong** (`|ln B| = 8.400`) — **ΛCDM** is favoured over **M2 (Law 1 + Ω_b = 1/19, γ_u ∈ [0, 2])** (strong evidence, ln B = -8.400 ± 0.199).
- **Pantheon+ · Reading B · CPL (w0waCDM) vs. ΛCDM:** **Weak** (`|ln B| = 2.487`) — **ΛCDM** is favoured over **CPL (w0waCDM)** (weak evidence, ln B = -2.487 ± 0.176).
- **Pantheon+ · Reading B · M1 (Law 1, γ_u ∈ [0, 2]) vs. ΛCDM:** **Moderate** (`|ln B| = 2.606`) — **ΛCDM** is favoured over **M1 (Law 1, γ_u ∈ [0, 2])** (moderate evidence, ln B = -2.606 ± 0.170).
- **Pantheon+ · Reading B · M2 (Law 1 + Ω_b = 1/19, γ_u ∈ [0, 2]) vs. ΛCDM:** **Strong** (`|ln B| = 7.015`) — **ΛCDM** is favoured over **M2 (Law 1 + Ω_b = 1/19, γ_u ∈ [0, 2])** (strong evidence, ln B = -7.015 ± 0.292).
- **DES-Dovekie · Reading A · CPL (w0waCDM) vs. ΛCDM:** **Weak** (`|ln B| = 1.107`) — **ΛCDM** is favoured over **CPL (w0waCDM)** (weak evidence, ln B = -1.107 ± 0.174).
- **DES-Dovekie · Reading A · M1 (Law 1, γ_u ∈ [0, 2]) vs. ΛCDM:** **Weak** (`|ln B| = 2.352`) — **ΛCDM** is favoured over **M1 (Law 1, γ_u ∈ [0, 2])** (weak evidence, ln B = -2.352 ± 0.186).
- **DES-Dovekie · Reading A · M2 (Law 1 + Ω_b = 1/19, γ_u ∈ [0, 2]) vs. ΛCDM:** **Strong** (`|ln B| = 8.459`) — **ΛCDM** is favoured over **M2 (Law 1 + Ω_b = 1/19, γ_u ∈ [0, 2])** (strong evidence, ln B = -8.459 ± 0.187).
- **DES-Dovekie · Reading B · CPL (w0waCDM) vs. ΛCDM:** **Weak** (`|ln B| = 1.008`) — **ΛCDM** is favoured over **CPL (w0waCDM)** (weak evidence, ln B = -1.008 ± 0.186).
- **DES-Dovekie · Reading B · M1 (Law 1, γ_u ∈ [0, 2]) vs. ΛCDM:** **Weak** (`|ln B| = 2.143`) — **ΛCDM** is favoured over **M1 (Law 1, γ_u ∈ [0, 2])** (weak evidence, ln B = -2.143 ± 0.180).
- **DES-Dovekie · Reading B · M2 (Law 1 + Ω_b = 1/19, γ_u ∈ [0, 2]) vs. ΛCDM:** **Strong** (`|ln B| = 6.905`) — **ΛCDM** is favoured over **M2 (Law 1 + Ω_b = 1/19, γ_u ∈ [0, 2])** (strong evidence, ln B = -6.905 ± 0.228).

### 3.2 Prior-Sensitivity Runs ($\gamma_u \in [0, 0.5]$)

- **Pantheon+ · Reading A · M1 (narrow prior γ_u ∈ [0, 0.5]) vs. ΛCDM:** **Weak** (`|ln B| = 1.519`) — **ΛCDM** is favoured over **M1 (narrow prior γ_u ∈ [0, 0.5])** (weak evidence, ln B = -1.519 ± 0.241).
- **Pantheon+ · Reading A · M2 (narrow prior γ_u ∈ [0, 0.5]) vs. ΛCDM:** **Strong** (`|ln B| = 7.062`) — **ΛCDM** is favoured over **M2 (narrow prior γ_u ∈ [0, 0.5])** (strong evidence, ln B = -7.062 ± 0.220).
- **Pantheon+ · Reading B · M1 (narrow prior γ_u ∈ [0, 0.5]) vs. ΛCDM:** **Weak** (`|ln B| = 1.273`) — **ΛCDM** is favoured over **M1 (narrow prior γ_u ∈ [0, 0.5])** (weak evidence, ln B = -1.273 ± 0.212).
- **Pantheon+ · Reading B · M2 (narrow prior γ_u ∈ [0, 0.5]) vs. ΛCDM:** **Strong** (`|ln B| = 5.517`) — **ΛCDM** is favoured over **M2 (narrow prior γ_u ∈ [0, 0.5])** (strong evidence, ln B = -5.517 ± 0.159).
- **DES-Dovekie · Reading A · M1 (narrow prior γ_u ∈ [0, 0.5]) vs. ΛCDM:** **Inconclusive** (`|ln B| = 0.977`) — neither model is meaningfully favoured (nominal preference toward ΛCDM, ln B = -0.977 ± 0.210, |ln B| = 0.977 < 1).
- **DES-Dovekie · Reading A · M2 (narrow prior γ_u ∈ [0, 0.5]) vs. ΛCDM:** **Strong** (`|ln B| = 7.092`) — **ΛCDM** is favoured over **M2 (narrow prior γ_u ∈ [0, 0.5])** (strong evidence, ln B = -7.092 ± 0.157).
- **DES-Dovekie · Reading B · M1 (narrow prior γ_u ∈ [0, 0.5]) vs. ΛCDM:** **Inconclusive** (`|ln B| = 0.724`) — neither model is meaningfully favoured (nominal preference toward ΛCDM, ln B = -0.724 ± 0.193, |ln B| = 0.724 < 1).
- **DES-Dovekie · Reading B · M2 (narrow prior γ_u ∈ [0, 0.5]) vs. ΛCDM:** **Strong** (`|ln B| = 5.437`) — **ΛCDM** is favoured over **M2 (narrow prior γ_u ∈ [0, 0.5])** (strong evidence, ln B = -5.437 ± 0.170).

---

## 4. Validation Results

### 4.1 Two-Quadrature Validation of $r_s(z_*)$ Under Reading A (`GL128` vs. `scipy.integrate.quad`)
- **Requirement:** Relative agreement better than $10^{-6}$ between two independent quadratures of the literal registered `(a5)` sound-horizon integral.
- **Obtained Maximum Relative Difference Across All 5 Test Points:** **`1.615e-12`** ($< 10^{-6} \implies$ **PASS**).
- **Baryon Drag Calibration Factor (`147.09 Mpc` at Planck 2018 fiducial):** Reading A `_DRAG_CALIB_FACTOR_A5` = `0.97556814` vs. Reading B `_DRAG_CALIB_FACTOR` = `0.97403995`.

| Test Point | $(\Omega_{bc}, h, 100\omega_b)$ | $z_*$ | $r_s(z_*)$ Reading A `GL128` (Mpc) | $r_s(z_*)$ Reading A `QUAD` (Mpc) | Relative Diff `|GL128 - QUAD| / QUAD` | $r_s(z_*)$ Reading B `Chen+19` (Mpc) | `(Chen - a5) / a5` |
|---|---|---:|---:|---:|---:|---:|---:|
| `Planck_2018_fiducial` | `(0.31380, 0.6736, 2.2370)` | `1091.9092` | `144.29107513` | `144.29107513` | `1.510e-12` | `144.52973399` | `+0.16540%` |
| `Chen_2019_Table1_mean` | `(0.31388, 0.6727, 2.2360)` | `1091.8940` | `144.38466129` | `144.38466129` | `1.513e-12` | `144.62358123` | `+0.16547%` |
| `Prior_low_corner` | `(0.15000, 0.5500, 1.8500)` | `1086.4887` | `183.93531609` | `183.93531609` | `2.508e-13` | `184.28886751` | `+0.19222%` |
| `Prior_high_corner` | `(0.45000, 0.8500, 2.5500)` | `1099.4047` | `112.34979295` | `112.34979295` | `3.615e-13` | `112.50422470` | `+0.13746%` |
| `M2_structural_fiducial` | `(0.31000, 0.6520, 2.2374)` | `1090.9761` | `147.11046359` | `147.11046359` | `1.615e-12` | `147.35730421` | `+0.16779%` |

### 4.2 Gate `G9-b` Recomputed Under Reading A vs. Reading B
- **Reading A (Literal Registered `a5` Full Sound-Horizon Integral):**
  - Best-fit flat $\Lambda\text{CDM}$ parameters on the Chen, Huang & Wang (2019) Table 1 $\Lambda\text{CDM}$ $3\times 3$ prior: $\hat{\Omega}_{m,\text{tot}} = 0.315384 \pm 0.008436$, $\hat{h} = 0.676124 \pm 0.006101$, $100\hat{\omega}_b = 2.236000 \pm 0.015000$.
  - Sound horizon at recombination: $r_s^{\text{(A)}}(z_*) = 144.001390\text{ Mpc}$ vs. $r_s^{\text{(B)}}(z_*) = 144.239204\text{ Mpc}$ (Reading B is $+0.1651\%$ larger).
  - Offset on $h$: **`0.4673\sigma`** against the registered target $h = 0.6736 \pm 0.0054$ (and **`0.5706\sigma`** against Chen et al. Table 2 $h = 0.6727 \pm 0.0060$; $\Omega_m$ offset = `0.0115\sigma`, $100\omega_b$ offset = `0.0000\sigma`).
  - Gate `G9-b` outcome under Reading A: **`FAIL`** ($\max \Delta = 0.4673\sigma > 0.3\sigma$ tolerance, reproducing the $\approx 0.58\sigma$ $h$ offset noted in `COMPARISON_ARGON_vs_REBUILD.md` Finding 1).
- **Reading B (`Chen, Huang & Wang 2019` Early-Universe Form in Frozen Code):**
  - $\hat{\Omega}_{m,\text{tot}} = 0.315483$, $\hat{h} = 0.673737$, $100\hat{\omega}_b = 2.236000$, $\max \Delta = 0.0254\sigma \le 0.3\sigma \implies$ **`PASS`**.

### 4.3 Pre-Run $\Lambda\text{CDM}$ Nested-Sampling $\chi^2_{\min}$ Sanity Check
- **Requirement:** For $\Lambda\text{CDM}$ (Reading B), the best-fit $\chi^2_{\min}$ from the `dynesty` nested-sampling run must match the Stage 2 $\Lambda\text{CDM}$ $\chi^2_{\min}$ to within `0.1`.
- **`Pantheon+` (`Reading B`, `seed = 20261030`):** Nested-sampling $\chi^2_{\min} = 1405.343880$ vs. Stage 2 $\chi^2_{\min} = 1405.343634$ ($|\Delta\chi^2| = 0.000246 \le 0.1 \implies$ **PASS**).
- **`DES-Dovekie` (`Reading B`, `seed = 20261030`):** Nested-sampling $\chi^2_{\min} = 1650.962073$ vs. Stage 2 $\chi^2_{\min} = 1650.961491$ ($|\Delta\chi^2| = 0.000582 \le 0.1 \implies$ **PASS**).

---

## 5. Per-Seed Breakdown Across All 24 Runs (72 Nested-Sampling Chains)

| Run ID | Group | SN | Reading | Model | $\ln Z_{s_1}$ (`20261030`) | $\ln Z_{s_2}$ (`20261031`) | $\ln Z_{s_3}$ (`20261032`) | $\overline{\ln Z}$ | $\sigma_{\rm dyn}$ | $\sigma_{\rm scatter}$ | $\sigma_{\ln Z}$ |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| `main__PantheonPlus__reading_A__LCDM` | `main` | `Pantheon+` | `A` | `LCDM` | $-715.360 \pm 0.112$ | $-715.254 \pm 0.111$ | $-715.331 \pm 0.111$ | $-715.315$ | $0.111$ | $0.055$ | $0.111$ |
| `main__PantheonPlus__reading_A__CPL` | `main` | `Pantheon+` | `A` | `CPL` | $-718.142 \pm 0.134$ | $-717.807 \pm 0.133$ | $-717.982 \pm 0.133$ | $-717.977$ | $0.134$ | $0.167$ | $0.167$ |
| `main__PantheonPlus__reading_A__M1` | `main` | `Pantheon+` | `A` | `M1` | $-718.060 \pm 0.125$ | $-717.897 \pm 0.125$ | $-718.115 \pm 0.125$ | $-718.024$ | $0.125$ | $0.113$ | $0.125$ |
| `main__PantheonPlus__reading_A__M2` | `main` | `Pantheon+` | `A` | `M2` | $-723.796 \pm 0.118$ | $-723.526 \pm 0.116$ | $-723.823 \pm 0.118$ | $-723.715$ | $0.117$ | $0.164$ | $0.164$ |
| `main__PantheonPlus__reading_B__LCDM` | `main` | `Pantheon+` | `B` | `LCDM` | $-715.802 \pm 0.111$ | $-715.986 \pm 0.112$ | $-715.776 \pm 0.111$ | $-715.855$ | $0.112$ | $0.114$ | $0.114$ |
| `main__PantheonPlus__reading_B__CPL` | `main` | `Pantheon+` | `B` | `CPL` | $-718.353 \pm 0.133$ | $-718.285 \pm 0.133$ | $-718.388 \pm 0.133$ | $-718.342$ | $0.133$ | $0.052$ | $0.133$ |
| `main__PantheonPlus__reading_B__M1` | `main` | `Pantheon+` | `B` | `M1` | $-718.517 \pm 0.126$ | $-718.387 \pm 0.125$ | $-718.479 \pm 0.125$ | $-718.461$ | $0.125$ | $0.067$ | $0.125$ |
| `main__PantheonPlus__reading_B__M2` | `main` | `Pantheon+` | `B` | `M2` | $-722.841 \pm 0.117$ | $-722.616 \pm 0.116$ | $-723.151 \pm 0.119$ | $-722.870$ | $0.118$ | $0.269$ | $0.269$ |
| `main__DES_Dovekie__reading_A__LCDM` | `main` | `DES-Dovekie` | `A` | `LCDM` | $-838.130 \pm 0.112$ | $-838.135 \pm 0.112$ | $-838.181 \pm 0.112$ | $-838.149$ | $0.112$ | $0.028$ | $0.112$ |
| `main__DES_Dovekie__reading_A__CPL` | `main` | `DES-Dovekie` | `A` | `CPL` | $-839.223 \pm 0.133$ | $-839.311 \pm 0.133$ | $-839.234 \pm 0.133$ | $-839.256$ | $0.133$ | $0.048$ | $0.133$ |
| `main__DES_Dovekie__reading_A__M1` | `main` | `DES-Dovekie` | `A` | `M1` | $-840.338 \pm 0.125$ | $-840.534 \pm 0.126$ | $-840.631 \pm 0.126$ | $-840.501$ | $0.125$ | $0.149$ | $0.149$ |
| `main__DES_Dovekie__reading_A__M2` | `main` | `DES-Dovekie` | `A` | `M2` | $-846.628 \pm 0.117$ | $-846.450 \pm 0.116$ | $-846.746 \pm 0.118$ | $-846.608$ | $0.117$ | $0.149$ | $0.149$ |
| `main__DES_Dovekie__reading_B__LCDM` | `main` | `DES-Dovekie` | `B` | `LCDM` | $-838.558 \pm 0.111$ | $-838.720 \pm 0.112$ | $-838.814 \pm 0.112$ | $-838.697$ | $0.112$ | $0.130$ | $0.130$ |
| `main__DES_Dovekie__reading_B__CPL` | `main` | `DES-Dovekie` | `B` | `CPL` | $-839.661 \pm 0.133$ | $-839.682 \pm 0.133$ | $-839.773 \pm 0.134$ | $-839.705$ | $0.133$ | $0.060$ | $0.133$ |
| `main__DES_Dovekie__reading_B__M1` | `main` | `DES-Dovekie` | `B` | `M1` | $-840.852 \pm 0.125$ | $-840.789 \pm 0.125$ | $-840.879 \pm 0.125$ | $-840.840$ | $0.125$ | $0.046$ | $0.125$ |
| `main__DES_Dovekie__reading_B__M2` | `main` | `DES-Dovekie` | `B` | `M2` | $-845.515 \pm 0.117$ | $-845.474 \pm 0.117$ | $-845.818 \pm 0.118$ | $-845.602$ | $0.117$ | $0.188$ | $0.188$ |
| `sens__PantheonPlus__reading_A__M1_gamma0p5` | `prior_sensitivity` | `Pantheon+` | `A` | `M1_narrow` | $-716.786 \pm 0.119$ | $-716.648 \pm 0.119$ | $-717.068 \pm 0.121$ | $-716.834$ | $0.120$ | $0.214$ | $0.214$ |
| `sens__PantheonPlus__reading_A__M2_gamma0p5` | `prior_sensitivity` | `Pantheon+` | `A` | `M2_narrow` | $-722.429 \pm 0.111$ | $-722.167 \pm 0.110$ | $-722.534 \pm 0.112$ | $-722.377$ | $0.111$ | $0.189$ | $0.189$ |
| `sens__PantheonPlus__reading_B__M1_gamma0p5` | `prior_sensitivity` | `Pantheon+` | `B` | `M1_narrow` | $-717.040 \pm 0.119$ | $-717.011 \pm 0.119$ | $-717.333 \pm 0.120$ | $-717.128$ | $0.119$ | $0.178$ | $0.178$ |
| `sens__PantheonPlus__reading_B__M2_gamma0p5` | `prior_sensitivity` | `Pantheon+` | `B` | `M2_narrow` | $-721.395 \pm 0.111$ | $-721.260 \pm 0.110$ | $-721.461 \pm 0.111$ | $-721.372$ | $0.111$ | $0.102$ | $0.111$ |
| `sens__DES_Dovekie__reading_A__M1_gamma0p5` | `prior_sensitivity` | `DES-Dovekie` | `A` | `M1_narrow` | $-839.114 \pm 0.119$ | $-838.954 \pm 0.119$ | $-839.308 \pm 0.120$ | $-839.125$ | $0.119$ | $0.177$ | $0.177$ |
| `sens__DES_Dovekie__reading_A__M2_gamma0p5` | `prior_sensitivity` | `DES-Dovekie` | `A` | `M2_narrow` | $-845.260 \pm 0.111$ | $-845.124 \pm 0.110$ | $-845.338 \pm 0.111$ | $-845.241$ | $0.111$ | $0.108$ | $0.111$ |
| `sens__DES_Dovekie__reading_B__M1_gamma0p5` | `prior_sensitivity` | `DES-Dovekie` | `B` | `M1_narrow` | $-839.328 \pm 0.119$ | $-839.350 \pm 0.119$ | $-839.585 \pm 0.120$ | $-839.421$ | $0.119$ | $0.142$ | $0.142$ |
| `sens__DES_Dovekie__reading_B__M2_gamma0p5` | `prior_sensitivity` | `DES-Dovekie` | `B` | `M2_narrow` | $-844.177 \pm 0.111$ | $-844.070 \pm 0.110$ | $-844.157 \pm 0.111$ | $-844.135$ | $0.110$ | $0.056$ | $0.110$ |

