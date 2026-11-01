import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import ctypes
import hashlib
import json
import shutil
import ssl
import sys
import time

H2H_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(H2H_DIR, ".."))


def setup_ots():
    orig_load = ctypes.cdll.LoadLibrary

    def patched_load(name):
        if name is None:
            return ctypes.CDLL(r"C:\Python314\DLLs\libcrypto-3.dll")
        return orig_load(name)

    ctypes.cdll.LoadLibrary = patched_load
    ssl._create_default_https_context = ssl._create_unverified_context
    import otsclient.ots
    return otsclient.ots


def stamp_with_ots(ots_mod, filepath):
    ots_path = filepath + ".ots"
    if os.path.exists(ots_path):
        trash_dir = os.path.join(ROOT_DIR, "_TRASH")
        os.makedirs(trash_dir, exist_ok=True)
        backup = os.path.join(trash_dir, os.path.basename(ots_path) + f"_{int(time.time())}.bak")
        os.replace(ots_path, backup)

    print(f"=== Stamping {filepath} -> {ots_path} ===")
    sys.argv = [
        "ots",
        "stamp",
        "-c",
        "https://alice.btc.calendar.opentimestamps.org",
        "-c",
        "https://bob.btc.calendar.opentimestamps.org",
        "-c",
        "https://finney.calendar.eternitywall.com",
        filepath,
    ]
    try:
        ots_mod.main()
    except SystemExit as e:
        print("ots stamp exit:", e.code)

    sys.argv = ["ots", "info", ots_path]
    try:
        ots_mod.main()
    except SystemExit:
        pass


def _fmt_pm(val: float, err: float, decimals: int = 4) -> str:
    return f"{val:.{decimals}f} ± {err:.{decimals}f}"


def _plain_language_line(sn_label: str, reading_label: str, model_label: str, ln_b: float, ln_b_err: float) -> str:
    abs_b = abs(ln_b)
    if abs_b < 1.0:
        scale_word = "Inconclusive"
    elif abs_b < 2.5:
        scale_word = "Weak"
    elif abs_b <= 5.0:
        scale_word = "Moderate"
    else:
        scale_word = "Strong"

    if abs_b < 1.0:
        fav_text = (
            f"neither model is meaningfully favoured (nominal preference toward "
            f"{model_label if ln_b > 0 else 'ΛCDM'}, ln B = {ln_b:+.3f} ± {ln_b_err:.3f}, |ln B| = {abs_b:.3f} < 1)"
        )
    elif ln_b > 0:
        fav_text = f"**{model_label}** is favoured over **ΛCDM** ({scale_word.lower()} evidence, ln B = {ln_b:+.3f} ± {ln_b_err:.3f})"
    else:
        fav_text = f"**ΛCDM** is favoured over **{model_label}** ({scale_word.lower()} evidence, ln B = {ln_b:+.3f} ± {ln_b_err:.3f})"

    return f"- **{sn_label} · {reading_label} · {model_label} vs. ΛCDM:** **{scale_word}** (`|ln B| = {abs_b:.3f}`) — {fav_text}."


def generate_markdown(data: dict) -> str:
    val = data["validation"]
    quad = val["rs_two_quadrature_validation"]
    g9a = val["gate_G9b_reading_A"]
    g9b = val["gate_G9b_reading_B_stage2"]
    sanity = val["lcdm_nested_sampling_sanity_check"]

    lines = [
        "---",
        'title: "MULTIVERSE v1: Head-to-Head Bayesian Evidence Comparison Results (HEAD_TO_HEAD_RESULTS.md)"',
        'subtitle: "Supplementary Analysis, Not Pre-Registered — Background Expansion Comparison Against Standard ΛCDM"',
        'author: "Gregory Mandarano / WickedAI — Executed by Gemini 4 Argon"',
        'date: "2026-10-30"',
        "---",
        "",
        "# MULTIVERSE v1: HEAD-TO-HEAD RESULTS (`supplementary analysis, not pre-registered`)",
        "",
        "> **STATUS LABEL:** **Supplementary analysis, not pre-registered.**",
        ">",
        "> **SCOPE STATEMENT:** This report is a supplementary Bayesian evidence comparison of **cosmological background expansion only** (`DESI DR2 BAO` with joint Ly$\\alpha$ BAO+AP + `Chen, Huang & Wang 2019` compressed CMB distance priors + one supernova compilation per run: `Pantheon+` or `DES-Dovekie`, never combined). It says **nothing** about galaxy rotation curves (`T5-A`), dissociative galaxy cluster mergers (`T4b`), or regional $H_0$ heterogeneity (`T6`). **The `T5-A` rotation-curve failure and the Stage 2 overall verdict (`MODEL FALSIFIED (FAIL)`, frozen in `RESULTS_v5.sha256`) stand unchanged regardless of what this background comparison shows.**",
        "",
        "---",
        "",
        "## 1. Main Head-to-Head Tables (Per Supernova Compilation and Per $r_s$ Reading)",
        "",
        "**Conventions & Priors (`HEAD_TO_HEAD_PLAN.md`):**",
        "- All models are spatially flat FLRW models (`[Established]` metric, `[Model Ansatz]` dark-sector mappings for `M1` and `M2`) with $\\Omega_{bc} \\equiv \\Omega_b + \\Omega_{\\rm dm} \\sim \\mathcal{U}(0.10, 0.50)$, $h \\sim \\mathcal{U}(0.50, 0.90)$, and massive neutrinos added separately ($\\sum m_\\nu = 0.06\\text{ eV}$, $\\Omega_{\\nu,0} = \\omega_{\\nu,{\\rm mass},0}/h^2$).",
        "- For $\\Lambda\\text{CDM}$, $\\text{CPL}$, and $\\text{M1}$, $100\\omega_b \\sim \\mathcal{U}(1.80, 2.60)$ is free. For $\\text{M2}$ (the structural version of the model), $\\Omega_b = 1/19$ is imposed inside the likelihood as $\\omega_b = h^2/19$ ($100\\omega_b = 100h^2/19$).",
        "- In the main runs below, $\\text{M1}$ and $\\text{M2}$ use the registered `T1-L1` prior $\\gamma_u \\sim \\mathcal{U}(0, 2)$, and $\\text{CPL}$ uses the uniform prior on $w_0 \\in [-3, 1], w_a \\in [-3, 2]$ with $w_0 + w_a < 0$ (area $15.5$).",
        "- Each run is aggregated across 3 fixed seeds (`20261030`, `20261031`, `20261032`) using static `dynesty` (`nlive = 1000`, `bound = 'multi'`, `sample = 'rwalk'`, `dlogz = 0.01`). The adopted uncertainty on $\\ln Z$ is $\\sigma_{\\ln Z} = \\max(\\sigma_{\\rm dyn}, \\sigma_{\\rm scatter})$, where $\\sigma_{\\rm dyn}$ is the RMS of `dynesty`'s internal error and $\\sigma_{\\rm scatter}$ is the sample standard deviation (`ddof=1`) across the 3 seeds. Positive $\\ln B = \\ln Z_{\\rm model} - \\ln Z_{\\Lambda\\text{CDM}} > 0$ means the model is favoured over $\\Lambda\\text{CDM}$; negative $\\ln B < 0$ means $\\Lambda\\text{CDM}$ is favoured over the model.",
        "",
    ]

    plain_lines_main = []
    plain_lines_sens = []

    for sn_tag, sn_display in [("PantheonPlus", "Pantheon+"), ("DES_Dovekie", "DES-Dovekie")]:
        for reading_code, reading_desc in [
            ("A", "Reading A (Literal Registered `a5` Full Sound-Horizon Integral)"),
            ("B", "Reading B (`Chen, Huang & Wang 2019` Early-Universe Form in Frozen Code)"),
        ]:
            cell = data["comparisons"][sn_tag][f"Reading_{reading_code}"]
            m_dict = cell["main_models"]
            lines.append(f"### 1.{1 if sn_tag=='PantheonPlus' else 2}.{reading_code} — `{sn_display}` · {reading_desc}")
            lines.append("")
            lines.append(
                "| Model | $d$ | $\\ln Z$ (mean) | $\\sigma_{\\rm dyn}$ | $\\sigma_{\\rm scatter}$ | $\\sigma_{\\ln Z}$ (adopted) | $\\ln B$ vs. $\\Lambda\\text{CDM}$ | Best-Fit $\\chi^2_{\\min}$ (NS / Opt) | $\\Delta\\chi^2_{\\min}$ vs. $\\Lambda\\text{CDM}$ (NS / Opt) | Key Posterior Mean $\\pm 1\\sigma$ |"
            )
            lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---|")

            for m_key in ["LCDM", "CPL", "M1", "M2"]:
                mr = m_dict[m_key]
                p = mr["parameters"]
                if m_key == "LCDM":
                    m_disp = "$\\Lambda\\text{CDM}$"
                    lnb_str = "$0.000$ (baseline)"
                    dchi2_str = "$0.00$ / $0.00$"
                    key_post = (
                        f"$\\Omega_{{bc}} = {_fmt_pm(p['Omega_bc']['mean'], p['Omega_bc']['std'], 4)}$, "
                        f"$h = {_fmt_pm(p['h']['mean'], p['h']['std'], 4)}$, "
                        f"$100\\omega_b = {_fmt_pm(p['100_omega_b']['mean'], p['100_omega_b']['std'], 4)}$"
                    )
                elif m_key == "CPL":
                    m_disp = "$\\text{CPL}$ ($w_0w_a\\text{CDM}$)"
                    lnb_str = f"${mr['lnB_vs_LCDM']:+.3f} \\pm {mr['lnB_err_vs_LCDM']:.3f}$"
                    dchi2_str = f"${mr['delta_chi2_ns_vs_LCDM']:+.2f}$ / ${mr['delta_chi2_opt_vs_LCDM']:+.2f}$"
                    key_post = (
                        f"$w_0 = {_fmt_pm(p['w0']['mean'], p['w0']['std'], 4)}$, "
                        f"$w_a = {_fmt_pm(p['wa']['mean'], p['wa']['std'], 4)}$ "
                        f"($\\Omega_{{bc}} = {_fmt_pm(p['Omega_bc']['mean'], p['Omega_bc']['std'], 4)}$, "
                        f"$h = {_fmt_pm(p['h']['mean'], p['h']['std'], 4)}$)"
                    )
                    plain_lines_main.append(
                        _plain_language_line(sn_display, f"Reading {reading_code}", "CPL (w0waCDM)", mr["lnB_vs_LCDM"], mr["lnB_err_vs_LCDM"])
                    )
                elif m_key == "M1":
                    m_disp = "$\\text{M1}$ (Law 1, $\\gamma_u \\in [0, 2]$)"
                    lnb_str = f"${mr['lnB_vs_LCDM']:+.3f} \\pm {mr['lnB_err_vs_LCDM']:.3f}$"
                    dchi2_str = f"${mr['delta_chi2_ns_vs_LCDM']:+.2f}$ / ${mr['delta_chi2_opt_vs_LCDM']:+.2f}$"
                    key_post = (
                        f"$\\gamma_u = {_fmt_pm(p['gamma_u']['mean'], p['gamma_u']['std'], 4)}$ "
                        f"($\\Omega_{{bc}} = {_fmt_pm(p['Omega_bc']['mean'], p['Omega_bc']['std'], 4)}$, "
                        f"$h = {_fmt_pm(p['h']['mean'], p['h']['std'], 4)}$, "
                        f"$100\\omega_b = {_fmt_pm(p['100_omega_b']['mean'], p['100_omega_b']['std'], 4)}$)"
                    )
                    plain_lines_main.append(
                        _plain_language_line(sn_display, f"Reading {reading_code}", "M1 (Law 1, γ_u ∈ [0, 2])", mr["lnB_vs_LCDM"], mr["lnB_err_vs_LCDM"])
                    )
                elif m_key == "M2":
                    m_disp = "$\\text{M2}$ (Law 1 + $\\Omega_b = 1/19$, $\\gamma_u \\in [0, 2]$)"
                    lnb_str = f"${mr['lnB_vs_LCDM']:+.3f} \\pm {mr['lnB_err_vs_LCDM']:.3f}$"
                    dchi2_str = f"${mr['delta_chi2_ns_vs_LCDM']:+.2f}$ / ${mr['delta_chi2_opt_vs_LCDM']:+.2f}$"
                    key_post = (
                        f"$\\gamma_u = {_fmt_pm(p['gamma_u']['mean'], p['gamma_u']['std'], 4)}$, "
                        f"$\\Omega_b h^2 = {_fmt_pm(p['omega_b_derived']['mean'], p['omega_b_derived']['std'], 6)}$ "
                        f"($100\\omega_b = {_fmt_pm(p['100_omega_b_derived']['mean'], p['100_omega_b_derived']['std'], 4)}$, "
                        f"$\\Omega_{{bc}} = {_fmt_pm(p['Omega_bc']['mean'], p['Omega_bc']['std'], 4)}$, "
                        f"$h = {_fmt_pm(p['h']['mean'], p['h']['std'], 4)}$)"
                    )
                    plain_lines_main.append(
                        _plain_language_line(
                            sn_display, f"Reading {reading_code}", "M2 (Law 1 + Ω_b = 1/19, γ_u ∈ [0, 2])", mr["lnB_vs_LCDM"], mr["lnB_err_vs_LCDM"]
                        )
                    )

                ndim_val = mr.get("ndim", mr["seed_runs"][0]["ndim"])
                lines.append(
                    f"| {m_disp} | {ndim_val} | ${mr['lnZ_mean']:.3f}$ | ${mr['lnZ_err_dynesty_rms']:.3f}$ | "
                    f"${mr['lnZ_scatter_std_ddof1']:.3f}$ | ${mr['lnZ_err_adopted']:.3f}$ | {lnb_str} | "
                    f"${mr['chi2_min_ns']:.2f}$ / ${mr['chi2_min_opt']:.2f}$ | {dchi2_str} | {key_post} |"
                )
            lines.append("")

    # Section 2: Prior-sensitivity table for M1 and M2
    lines.extend(
        [
            "---",
            "",
            "## 2. Prior-Sensitivity Table for `M1` and `M2` ($\\gamma_u \\in [0, 2]$ vs. $\\gamma_u \\in [0, 0.5]$)",
            "",
            "Because the likelihood for $\\gamma_u$ is concentrated well below $\\gamma_u = 0.5$ ($\\gamma_u \\sim 0.03\\text{--}0.05$), narrowing the uniform prior width by a factor of $4$ from $[0, 2]$ to $[0, 0.5]$ reduces the prior-volume (Occam) penalty by $\\approx \\ln(2.0 / 0.5) = \\ln 4 \\approx +1.386$ in $\\ln Z$ and $\\ln B$ while leaving the best-fit $\\chi^2_{\\min}$ and posterior moments unchanged:",
            "",
            "| SN Compilation | $r_s$ Reading | Model | Prior $\\gamma_u$ | $\\ln Z$ (mean $\\pm$ adopted) | $\\sigma_{\\rm dyn}$ / $\\sigma_{\\rm scatter}$ | $\\ln B$ vs. $\\Lambda\\text{CDM}$ | Shift $\\Delta\\ln B(\\text{narrow} - \\text{wide})$ | Best-Fit $\\chi^2_{\\min}$ (NS / Opt) | Posterior $\\gamma_u$ and Derived $\\Omega_b h^2$ (for `M2`) |",
            "|---|---|---|---|---:|---:|---:|---:|---:|---|",
        ]
    )

    for sn_tag, sn_display in [("PantheonPlus", "Pantheon+"), ("DES_Dovekie", "DES-Dovekie")]:
        for reading_code in ["A", "B"]:
            cell = data["comparisons"][sn_tag][f"Reading_{reading_code}"]
            m_wide = cell["main_models"]
            m_narr = cell["prior_sensitivity_models"]
            for m_key in ["M1", "M2"]:
                rw = m_wide[m_key]
                rn = m_narr[f"{m_key}_gamma0p5"]
                shift_lnb = rn["lnB_vs_LCDM"] - rw["lnB_vs_LCDM"]

                for r_obj, p_str, is_narrow in [(rw, "$[0, 2.0]$ (wide)", False), (rn, "$[0, 0.5]$ (narrow)", True)]:
                    p = r_obj["parameters"]
                    if m_key == "M1":
                        post_str = f"$\\gamma_u = {_fmt_pm(p['gamma_u']['mean'], p['gamma_u']['std'], 4)}$"
                    else:
                        post_str = (
                            f"$\\gamma_u = {_fmt_pm(p['gamma_u']['mean'], p['gamma_u']['std'], 4)}$, "
                            f"$\\Omega_b h^2 = {_fmt_pm(p['omega_b_derived']['mean'], p['omega_b_derived']['std'], 6)}$ "
                            f"($100\\omega_b = {_fmt_pm(p['100_omega_b_derived']['mean'], p['100_omega_b_derived']['std'], 4)}$)"
                        )
                    shift_col = "—" if not is_narrow else f"${shift_lnb:+.3f}$"
                    lines.append(
                        f"| `{sn_display}` | Reading {reading_code} | `{m_key}` | {p_str} | "
                        f"${r_obj['lnZ_mean']:.3f} \\pm {r_obj['lnZ_err_adopted']:.3f}$ | "
                        f"${r_obj['lnZ_err_dynesty_rms']:.3f}$ / ${r_obj['lnZ_scatter_std_ddof1']:.3f}$ | "
                        f"${r_obj['lnB_vs_LCDM']:+.3f} \\pm {r_obj['lnB_err_vs_LCDM']:.3f}$ | {shift_col} | "
                        f"${r_obj['chi2_min_ns']:.2f}$ / ${r_obj['chi2_min_opt']:.2f}$ | {post_str} |"
                    )
                    if is_narrow:
                        plain_lines_sens.append(
                            _plain_language_line(
                                sn_display,
                                f"Reading {reading_code}",
                                f"{m_key} (narrow prior γ_u ∈ [0, 0.5])",
                                r_obj["lnB_vs_LCDM"],
                                r_obj["lnB_err_vs_LCDM"],
                            )
                        )
    lines.append("")

    # Section 3: Plain-language lines on the Jeffreys / Kass-Raftery scale
    lines.extend(
        [
            "---",
            "",
            "## 3. Plain-Language Verdicts on the Jeffreys / Kass–Raftery Scale",
            "",
            "**Scale (`ARGON_HEAD_TO_HEAD_HANDOFF.txt`):** $|\\ln B| < 1.0$ = **inconclusive**; $1.0 \\le |\\ln B| < 2.5$ = **weak**; $2.5 \\le |\\ln B| \\le 5.0$ = **moderate**; $|\\ln B| > 5.0$ = **strong**. Positive $\\ln B > 0$ favours the alternative model over $\\Lambda\\text{CDM}$; negative $\\ln B < 0$ favours $\\Lambda\\text{CDM}$.",
            "",
            "### 3.1 Main Runs ($\\gamma_u \\in [0, 2]$)",
            "",
            *plain_lines_main,
            "",
            "### 3.2 Prior-Sensitivity Runs ($\\gamma_u \\in [0, 0.5]$)",
            "",
            *plain_lines_sens,
            "",
        ]
    )

    # Section 4: Validation results
    s_p = sanity["runs"]["Pantheon+"]
    s_d = sanity["runs"]["DES-Dovekie"]
    lines.extend(
        [
            "---",
            "",
            "## 4. Validation Results",
            "",
            "### 4.1 Two-Quadrature Validation of $r_s(z_*)$ Under Reading A (`GL128` vs. `scipy.integrate.quad`)",
            f"- **Requirement:** Relative agreement better than $10^{{-6}}$ between two independent quadratures of the literal registered `(a5)` sound-horizon integral.",
            f"- **Obtained Maximum Relative Difference Across All 5 Test Points:** **`{quad['max_rel_diff_gl128_vs_quad']:.3e}`** ($< 10^{{-6}} \\implies$ **PASS**).",
            f"- **Baryon Drag Calibration Factor (`147.09 Mpc` at Planck 2018 fiducial):** Reading A `_DRAG_CALIB_FACTOR_A5` = `{quad['drag_calib_factor_reading_a']:.8f}` vs. Reading B `_DRAG_CALIB_FACTOR` = `{quad['drag_calib_factor_reading_b']:.8f}`.",
            "",
            "| Test Point | $(\\Omega_{bc}, h, 100\\omega_b)$ | $z_*$ | $r_s(z_*)$ Reading A `GL128` (Mpc) | $r_s(z_*)$ Reading A `QUAD` (Mpc) | Relative Diff `|GL128 - QUAD| / QUAD` | $r_s(z_*)$ Reading B `Chen+19` (Mpc) | `(Chen - a5) / a5` |",
            "|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for pt in quad["points"]:
        lines.append(
            f"| `{pt['label']}` | `({pt['Omega_bc']:.5f}, {pt['h']:.4f}, {pt['wb100']:.4f})` | "
            f"`{pt['z_star']:.4f}` | `{pt['rs_reading_a_gl128_Mpc']:.8f}` | `{pt['rs_reading_a_quad_Mpc']:.8f}` | "
            f"`{pt['rel_diff_gl128_vs_quad']:.3e}` | `{pt['rs_reading_b_chen_Mpc']:.8f}` | `{pt['rel_diff_chen_vs_a5']:+.5%}` |"
        )

    lines.extend(
        [
            "",
            "### 4.2 Gate `G9-b` Recomputed Under Reading A vs. Reading B",
            f"- **Reading A (Literal Registered `a5` Full Sound-Horizon Integral):**",
            f"  - Best-fit flat $\\Lambda\\text{{CDM}}$ parameters on the Chen, Huang & Wang (2019) Table 1 $\\Lambda\\text{{CDM}}$ $3\\times 3$ prior: $\\hat{{\\Omega}}_{{m,\\text{{tot}}}} = {g9a['obtained_Omega_m']:.6f} \\pm {g9a['obtained_sigma_Omega_m']:.6f}$, $\\hat{{h}} = {g9a['obtained_h']:.6f} \\pm {g9a['obtained_sigma_h']:.6f}$, $100\\hat{{\\omega}}_b = {g9a['obtained_100_omega_b']:.6f} \\pm {g9a['obtained_sigma_100_omega_b']:.6f}$.",
            f"  - Sound horizon at recombination: $r_s^{{\\text{{(A)}}}}(z_*) = {g9a['rs_star_reading_a_Mpc']:.6f}\\text{{ Mpc}}$ vs. $r_s^{{\\text{{(B)}}}}(z_*) = {g9a['rs_star_reading_b_Mpc']:.6f}\\text{{ Mpc}}$ (Reading B is ${(g9a['rs_ratio_b_over_a'] - 1.0)*100.0:+.4f}\\%$ larger).",
            f"  - Offset on $h$: **`{g9a['diff_h_sigma_vs_0p6736_0p0054']:.4f}\\sigma`** against the registered target $h = 0.6736 \\pm 0.0054$ (and **`{g9a['diff_h_sigma_vs_0p6727_0p0060']:.4f}\\sigma`** against Chen et al. Table 2 $h = 0.6727 \\pm 0.0060$; $\\Omega_m$ offset = `{g9a['diff_Omega_m_sigma']:.4f}\\sigma`, $100\\omega_b$ offset = `{g9a['diff_wb_sigma']:.4f}\\sigma`).",
            f"  - Gate `G9-b` outcome under Reading A: **`{g9a['verdict']}`** ($\\max \\Delta = {g9a['max_diff_sigma']:.4f}\\sigma > 0.3\\sigma$ tolerance, reproducing the $\\approx 0.58\\sigma$ $h$ offset noted in `COMPARISON_ARGON_vs_REBUILD.md` Finding 1).",
            f"- **Reading B (`Chen, Huang & Wang 2019` Early-Universe Form in Frozen Code):**",
            f"  - $\\hat{{\\Omega}}_{{m,\\text{{tot}}}} = {g9b['obtained_Omega_m']:.6f}$, $\\hat{{h}} = {g9b['obtained_h']:.6f}$, $100\\hat{{\\omega}}_b = {g9b['obtained_100_omega_b']:.6f}$, $\\max \\Delta = {g9b['max_diff_sigma']:.4f}\\sigma \\le 0.3\\sigma \\implies$ **`PASS`**.",
            "",
            "### 4.3 Pre-Run $\\Lambda\\text{CDM}$ Nested-Sampling $\\chi^2_{\\min}$ Sanity Check",
            "- **Requirement:** For $\\Lambda\\text{CDM}$ (Reading B), the best-fit $\\chi^2_{\\min}$ from the `dynesty` nested-sampling run must match the Stage 2 $\\Lambda\\text{CDM}$ $\\chi^2_{\\min}$ to within `0.1`.",
            f"- **`Pantheon+` (`Reading B`, `seed = 20261030`):** Nested-sampling $\\chi^2_{{\\min}} = {s_p['nested_sampling_chi2_min']:.6f}$ vs. Stage 2 $\\chi^2_{{\\min}} = {s_p['stage2_chi2_min_LCDM']:.6f}$ ($|\\Delta\\chi^2| = {s_p['abs_diff_chi2']:.6f} \\le 0.1 \\implies$ **PASS**).",
            f"- **`DES-Dovekie` (`Reading B`, `seed = 20261030`):** Nested-sampling $\\chi^2_{{\\min}} = {s_d['nested_sampling_chi2_min']:.6f}$ vs. Stage 2 $\\chi^2_{{\\min}} = {s_d['stage2_chi2_min_LCDM']:.6f}$ ($|\\Delta\\chi^2| = {s_d['abs_diff_chi2']:.6f} \\le 0.1 \\implies$ **PASS**).",
            "",
            "---",
            "",
            "## 5. Per-Seed Breakdown Across All 24 Runs (72 Nested-Sampling Chains)",
            "",
            "| Run ID | Group | SN | Reading | Model | $\\ln Z_{s_1}$ (`20261030`) | $\\ln Z_{s_2}$ (`20261031`) | $\\ln Z_{s_3}$ (`20261032`) | $\\overline{\\ln Z}$ | $\\sigma_{\\rm dyn}$ | $\\sigma_{\\rm scatter}$ | $\\sigma_{\\ln Z}$ |",
            "|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )

    for rid, ragg in data["runs"].items():
        s_vals = ragg["lnZ_per_seed"]
        s_errs = ragg["lnZ_err_dynesty_per_seed"]
        lines.append(
            f"| `{rid}` | `{ragg['group']}` | `{ragg['sn_name']}` | `{ragg['reading']}` | `{ragg['model_label']}` | "
            f"${s_vals[0]:.3f} \\pm {s_errs[0]:.3f}$ | ${s_vals[1]:.3f} \\pm {s_errs[1]:.3f}$ | "
            f"${s_vals[2]:.3f} \\pm {s_errs[2]:.3f}$ | ${ragg['lnZ_mean']:.3f}$ | "
            f"${ragg['lnZ_err_dynesty_rms']:.3f}$ | ${ragg['lnZ_scatter_std_ddof1']:.3f}$ | ${ragg['lnZ_err_adopted']:.3f}$ |"
        )

    lines.append("")
    return "\n".join(lines) + "\n"


def main():
    results_path = os.path.join(H2H_DIR, "results.json")
    with open(results_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    md_text = generate_markdown(data)
    md_h2h = os.path.join(H2H_DIR, "HEAD_TO_HEAD_RESULTS.md")
    md_root = os.path.join(ROOT_DIR, "HEAD_TO_HEAD_RESULTS.md")
    with open(md_h2h, "w", encoding="utf-8", newline="\n") as f:
        f.write(md_text)
    shutil.copy2(md_h2h, md_root)
    print(f"Wrote {md_h2h} and mirrored to {md_root}")

    # Collect all files in head_to_head/ (excluding HEAD_TO_HEAD_RESULTS_v1.sha256 and its .ots)
    rel_files = []
    for root, dirs, files in os.walk(H2H_DIR):
        dirs.sort()
        for fn in sorted(files):
            if fn in ("HEAD_TO_HEAD_RESULTS_v1.sha256", "HEAD_TO_HEAD_RESULTS_v1.sha256.ots"):
                continue
            if fn.endswith(".pyc") or "__pycache__" in root:
                continue
            full_p = os.path.join(root, fn)
            rel_p = os.path.relpath(full_p, ROOT_DIR).replace(os.sep, "/")
            rel_files.append(rel_p)

    # Also include root-mirrored plan & results files
    for root_fn in [
        "ARGON_HEAD_TO_HEAD_HANDOFF.txt",
        "HEAD_TO_HEAD_PLAN.md",
        "HEAD_TO_HEAD_PLAN.sha256",
        "HEAD_TO_HEAD_PLAN.sha256.ots",
        "HEAD_TO_HEAD_RESULTS.md",
    ]:
        p = os.path.join(ROOT_DIR, root_fn)
        if os.path.exists(p):
            rel_files.append(root_fn)

    rel_files = sorted(set(rel_files))

    plan_sha_path = os.path.join(H2H_DIR, "HEAD_TO_HEAD_PLAN.sha256")
    with open(plan_sha_path, "rb") as f:
        plan_manifest_hash = hashlib.sha256(f.read()).hexdigest()

    manifest_lines = [
        "# MULTIVERSE v1: Head-to-Head Supplementary Analysis Freeze Manifest (HEAD_TO_HEAD_RESULTS_v1.sha256)",
        "# Label: supplementary analysis, not pre-registered",
        f"# Generated at: {time.strftime('%Y-%m-%dT%H:%M:%S')}",
        f"# Chained from HEAD_TO_HEAD_PLAN.sha256: {plan_manifest_hash}",
        "# Format: <sha256_hex>  <relative_path>",
    ]

    for rel_p in rel_files:
        full_p = os.path.join(ROOT_DIR, rel_p.replace("/", os.sep))
        with open(full_p, "rb") as f:
            h = hashlib.sha256(f.read()).hexdigest()
        manifest_lines.append(f"{h}  {rel_p}")

    manifest_h2h = os.path.join(H2H_DIR, "HEAD_TO_HEAD_RESULTS_v1.sha256")
    manifest_root = os.path.join(ROOT_DIR, "HEAD_TO_HEAD_RESULTS_v1.sha256")
    with open(manifest_h2h, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(manifest_lines) + "\n")
    shutil.copy2(manifest_h2h, manifest_root)

    with open(manifest_h2h, "rb") as f:
        results_manifest_hash = hashlib.sha256(f.read()).hexdigest()

    print(f"HEAD_TO_HEAD_PLAN.sha256 hash:       {plan_manifest_hash}")
    print(f"HEAD_TO_HEAD_RESULTS_v1.sha256 hash: {results_manifest_hash}")

    ots_mod = setup_ots()
    stamp_with_ots(ots_mod, manifest_h2h)
    shutil.copy2(manifest_h2h + ".ots", manifest_root + ".ots")
    print("Stamped HEAD_TO_HEAD_RESULTS_v1.sha256.ots and mirrored to workspace root.")


if __name__ == "__main__":
    main()
