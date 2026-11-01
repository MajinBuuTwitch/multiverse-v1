import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import datetime
import json
import math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from run_part8_fixes import set_below_normal_priority
from clusters_t4 import run_all_t4
from sparc_t5 import (
    parse_sparc_catalog,
    evaluate_sparc_sample,
    score_t5_subtest,
    evaluate_t5c_df2,
    evaluate_rar_benchmark,
    compute_saturation_and_vc_tau_diagnostics,
    predict_galaxy_rotation_curve,
)


def run_holm_bonferroni(p_t1_l1: float, p_t4b: float, p_t6: float, raw_verdicts: dict[str, str]) -> dict:
    """
    [Registered Protocol - PREREG.md Sec 3.2 lines 75-85]
    Step-down Holm-Bonferroni procedure across K_disc = 3 discovery tests (T1-L1, T4b, T6)
    at alpha_FWE = 0.05: alpha_(1) = 0.05/3 = 0.0166667, alpha_(2) = 0.025, alpha_(3) = 0.050.
    """
    items = [
        {"test": "T1-L1", "p": float(p_t1_l1)},
        {"test": "T4b", "p": float(p_t4b)},
        {"test": "T6", "p": float(p_t6)},
    ]
    items_sorted = sorted(items, key=lambda d: d["p"])
    alphas = [0.05 / 3.0, 0.05 / 2.0, 0.05 / 1.0]

    m_star = None
    for idx, item in enumerate(items_sorted):
        rank = idx + 1
        alpha_m = alphas[idx]
        item["rank"] = rank
        item["alpha_threshold"] = round(alpha_m, 6)
        if m_star is None and item["p"] > alpha_m:
            m_star = rank
        item["survives_holm"] = bool(m_star is None)

    post_verdicts = dict(raw_verdicts)
    for item in items_sorted:
        tname = item["test"]
        if post_verdicts[tname] == "PASS" and not item["survives_holm"]:
            post_verdicts[tname] = "INCONCLUSIVE (Failed Holm-Bonferroni Control)"

    return {
        "alpha_FWE": 0.05,
        "K_discovery_tests": 3,
        "first_failing_rank_m_star": m_star,
        "sorted_tests": items_sorted,
        "raw_verdicts": raw_verdicts,
        "post_holm_verdicts": post_verdicts,
    }


def generate_all_figures(
    figures_dir: Path,
    part9: dict,
    t4_res: dict,
    t5_res: dict,
    sparc_galaxies: list[dict],
    f_leak_frozen: float,
):
    """Generate the 5 publication-quality diagnostic figures in results/figures/."""
    figures_dir.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.labelsize": 10,
        "figure.dpi": 180,
    })

    # --- Figure 1: T1-L1 Unwinding Curve vs DESI + CMB + SNe w0-wa Posteriors ---
    fig, ax = plt.subplots(figsize=(7.2, 5.2))
    w0_grid = np.linspace(-1.15, -0.50, 300)
    gu_grid = np.maximum(0.0, 1.0 + w0_grid)
    om_fid = 0.311
    wa_law1 = -1.5 * gu_grid * (om_fid + gu_grid * (1.0 - om_fid))

    ax.plot(w0_grid[w0_grid >= -1.0], wa_law1[w0_grid >= -1.0], "k-", lw=2.4, label=r"Model Law 1: $w(a) = -1 + \gamma_u/E(a)$ ($\gamma_u \geq 0$)")
    ax.scatter([-1.0], [0.0], color="black", marker="*", s=130, zorder=6, label=r"Flat $\Lambda$CDM $(w_0=-1, w_a=0)$")

    for sn_key, color, label in [
        ("PantheonPlus", "#1f77b4", "DESI DR2 + CMB + Pantheon+"),
        ("DES_Dovekie", "#d62728", "DESI DR2 + CMB + DES-Dovekie"),
    ]:
        cpl_p = part9["T1"]["T1_Sign_secondary"][sn_key]["CPL_chain"]["parameters"]
        w0_m, w0_s = cpl_p["w0"]["mean"], cpl_p["w0"]["std"]
        wa_m, wa_s = cpl_p["wa"]["mean"], cpl_p["wa"]["std"]
        ax.errorbar([w0_m], [wa_m], xerr=[w0_s], yerr=[wa_s], fmt="o", color=color, capsize=4, lw=1.8, label=f"CPL {label} ($1\\sigma$)")

        l1_p = part9["T1"]["T1_L1_deciding"][sn_key]["Law1_chain"]["parameters"]
        ax.scatter(
            [l1_p["w0_implied"]["median"]],
            [l1_p["wa_implied"]["median"]],
            color=color,
            marker="D",
            s=65,
            zorder=5,
            label=f"Law 1 Best Fit ({sn_key})",
        )

    ax.axvline(-1.0, color="gray", ls="--", lw=0.9, alpha=0.6)
    ax.axhline(0.0, color="gray", ls="--", lw=0.9, alpha=0.6)
    ax.set_xlim(-1.12, -0.65)
    ax.set_ylim(-1.35, 0.35)
    ax.set_xlabel(r"Present Dark-Energy Equation of State $w_0$")
    ax.set_ylabel(r"Time Derivative Parameter $w_a = -dw/da|_{a=1}$")
    ax.set_title("Pillar 1 (T1-L1 & T1-Sign): Unwinding Law 1 vs. Unconstrained CPL Posteriors")
    ax.legend(loc="lower left", fontsize=8.2, frameon=True)
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(figures_dir / "fig1_t1_unwinding_vs_desi.png")
    plt.close(fig)

    # --- Figure 2: T2 Strand Budget & Baryon Share Tensions ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.5))
    t2a_p = part9["T2"]["T2_A_deciding"]["PantheonPlus"]
    t2a_d = part9["T2"]["T2_A_deciding"]["DES_Dovekie"]
    t2a_c_p = part9["T2"]["T2_sensitivity"]["T2_A_alternate_priors"]["PantheonPlus_Cooke18"]
    t2b_p = part9["T2"]["T2_sensitivity"]["T2_B_constrained"]["PantheonPlus"]

    labels = [
        "Planck 2018\n$\\omega_c/\\omega_b$",
        "T2-A Deciding\n(Pantheon+)",
        "T2-A Deciding\n(DES-Dovekie)",
        "T2-A Sens.\n(Cooke+18 BBN)",
        "T2-B Sens.\n(Constrained)",
        "Geometric\n($f_{\\rm leak}=1/6$)",
    ]
    r_vals = [5.36, t2a_p["R_pred"], t2a_d["R_pred"], t2a_c_p["R_pred"], t2b_p["R_pred"], 5.0]
    r_errs = [0.065, t2a_p["sigma_R_pred"], t2a_d["sigma_R_pred"], t2a_c_p["sigma_R_pred"], t2b_p["sigma_R_pred"], 0.0]
    y_pos = np.arange(len(labels))

    ax1.axvspan(5.36 - 2 * 0.065, 5.36 + 2 * 0.065, color="#2ca02c", alpha=0.18, label="Planck $\\pm 2\\sigma$ band")
    ax1.axvline(5.36, color="#2ca02c", lw=1.6, ls="--")
    ax1.errorbar(r_vals, y_pos, xerr=r_errs, fmt="o", color="#1f77b4", capsize=4, lw=1.8)
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(labels, fontsize=8.5)
    ax1.invert_yaxis()
    ax1.set_xlabel(r"Dark-to-Baryon Ratio $\mathcal{R} = \Omega_{\rm dm}/\Omega_b = 19\Omega_{bc} - 1$")
    ax1.set_title("Pillar 2 (T2-A): Dark-to-Ordinary Ratio")
    ax1.grid(True, alpha=0.25)

    # Panel B: Direct Tension Z-scores
    t_names = [
        "T2-A (Pantheon+)",
        "T2-A (DES-Dovekie)",
        "T2-N1 ($\\Omega_b = 1/19$)",
        "T2-N2 ($H_0^{\\rm pred} = 65.19$)",
        "T2-B (Pantheon+)",
    ]
    z_vals = [
        abs(t2a_p["tension_sigma"]),
        abs(t2a_d["tension_sigma"]),
        abs(part9["T2"]["T2_N1_secondary"]["tension_sigma"]),
        abs(part9["T2"]["T2_N2_secondary"]["tension_sigma"]),
        abs(t2b_p["tension_sigma_vs_Planck"]),
    ]
    bars = ax2.barh(np.arange(len(t_names)), z_vals, color="#d62728", alpha=0.82, height=0.55)
    ax2.axvline(2.0, color="black", ls="--", lw=1.5, label="$2.0\\sigma$ FAIL Threshold")
    ax2.set_yticks(np.arange(len(t_names)))
    ax2.set_yticklabels(t_names, fontsize=8.5)
    ax2.invert_yaxis()
    ax2.set_xlabel(r"Discrepancy vs. Planck 2018 ($\sigma$)")
    ax2.set_title("Pillar 2 & Secondary Tension Summary")
    for b, zv in zip(bars, z_vals):
        ax2.text(zv + 0.08, b.get_y() + b.get_height() / 2, f"{zv:.2f}$\\sigma$", va="center", fontsize=8.5)
    ax2.set_xlim(0, max(z_vals) + 0.9)
    ax2.legend(loc="lower right", fontsize=8.5)
    ax2.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(figures_dir / "fig2_t2_strand_budget_tension.png")
    plt.close(fig)

    # --- Figure 3: T4b Cluster Mergers Offset Significance vs Time Since Pericenter ---
    fig, ax = plt.subplots(figsize=(7.8, 5.0))
    cat = t4_res["catalog"]
    tau_frozen = t4_res["T4b_deciding"]["training_fit"]["tau_lag_gyr"]

    ax.axhspan(-2.0, 2.0, color="gray", alpha=0.18, label=r"Unclassified zone ($|d_{IG}-d_{IS}| \leq 2\sigma_{\rm diff}$)")
    ax.axhline(2.0, color="#1f77b4", ls="--", lw=1.2)
    ax.axhline(-2.0, color="#d62728", ls="--", lw=1.2)
    ax.axvline(tau_frozen, color="purple", lw=2.0, ls="-.", label=f"Frozen $\\hat{{\\tau}}_{{\\rm lag}} = {tau_frozen*1000:.0f}$ Myr")

    for c in cat:
        sig_ratio = (c["d_IG_kpc"] - c["d_IS_kpc"]) / max(c["sigma_diff_kpc"], 1e-6)
        sig_ratio_plot = min(sig_ratio, 10.0)
        is_train = c["split"] == "train"
        marker = "o" if is_train else "s"
        color = "#1f77b4" if c["primary_class"] == "with_galaxies" else ("gray" if c["primary_class"] == "unclassified" else "#d62728")
        ax.errorbar(
            [c["t_p_gyr"]],
            [sig_ratio_plot],
            xerr=[c["sigma_t_p_gyr"]],
            fmt=marker,
            color=color,
            markersize=7,
            capsize=3,
            alpha=0.9,
        )
        ax.annotate(
            f"#{c['cluster_id']}",
            (c["t_p_gyr"], sig_ratio_plot),
            textcoords="offset points",
            xytext=(4, 4),
            fontsize=7.5,
        )

    ax.scatter([], [], marker="o", color="#1f77b4", label="Training Half (Odd #) — With Galaxies")
    ax.scatter([], [], marker="s", color="#1f77b4", label="Test Half (Even #) — With Galaxies")
    ax.scatter([], [], marker="s", color="gray", label="Unclassified ($\\leq 2\\sigma_{\\rm diff}$)")
    ax.set_xlabel(r"Time Since Pericenter $t_p$ (Gyr)")
    ax.set_ylabel(r"Offset Significance $(d_{IG} - d_{IS})/\sigma_{\rm diff}$ (capped at +10)")
    ax.set_title("Pillar 3 (T4b): Dissociative Cluster Mergers (Zero Systems in 'With Gas' Zone < -2)")
    ax.set_ylim(-4.5, 11.5)
    ax.legend(loc="upper right", fontsize=8.0, frameon=True)
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(figures_dir / "fig3_t4b_cluster_mergers.png")
    plt.close(fig)

    # --- Figure 4: T5 SPARC Rotation Curves, Saturation Cap, and NGC 1052-DF2 ---
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(11.0, 8.5))

    # Panel A: Held-out CDF of chi2_red
    for label, key, color, ls in [
        (f"T5-A Deciding ($\\hat{{\\sigma}}_{{\\rm ref}}={t5_res['T5A_deciding']['fitted_param']:.2f}$ kpc)", "T5A_deciding", "#d62728", "-"),
        (f"T5-B Secondary ($\\hat{{k}}={t5_res['T5B_secondary']['fitted_param']:.2f}$)", "T5B_secondary", "#ff7f0e", "--"),
        ("Baryon-Only Null ($M_{\\rm sh}=0$)", "baryon_only_test", "gray", ":"),
    ]:
        pg_list = t5_res[key]["per_galaxy"] if key == "baryon_only_test" else t5_res[key]["test_evaluation"]["per_galaxy"]
        arr = np.sort([g["chi2_red"] for g in pg_list])
        cdf = np.arange(1, len(arr) + 1) / len(arr)
        ax1.step(arr, cdf, where="post", color=color, ls=ls, lw=2.0, label=label)

    ax1.axvline(2.0, color="black", ls="--", lw=1.2, label="$\\chi^2_{\\rm red} = 2.0$ bar")
    ax1.axhline(0.70, color="#2ca02c", ls=":", lw=1.2, label="PASS ($F_{<2} \\geq 0.70$)")
    ax1.axhline(0.40, color="#d62728", ls=":", lw=1.2, label="FAIL ($F_{<2} < 0.40$)")
    ax1.set_xscale("log")
    ax1.set_xlim(0.1, 200.0)
    ax1.set_xlabel(r"Held-Out Galaxy Reduced $\chi^2_{{\rm red},g}$ (87 Test Galaxies)")
    ax1.set_ylabel("Cumulative Fraction of Held-Out Galaxies")
    ax1.set_title("(a) Pillar 4 (T5-A & T5-B): Held-Out $\\chi^2_{\\rm red}$ CDF")
    ax1.legend(loc="lower right", fontsize=7.5)
    ax1.grid(True, alpha=0.25)

    # Panel B: Saturation Cap g_obs / g_bar vs g_bar
    cap_val = 1.0 + 6.0 * (1.0 - f_leak_frozen)
    g_bar_all = []
    ratio_obs_all = []
    for gal in sparc_galaxies:
        gb = (gal["v_bar_mono2"] / np.maximum(gal["R"], 1e-6)) * 3.24077929e-14
        ro = (gal["v_obs"] ** 2) / np.maximum(gal["v_bar_mono2"], 1e-4)
        mask = (gb > 1e-13) & (ro > 0.2) & (ro < 100.0)
        g_bar_all.extend(gb[mask].tolist())
        ratio_obs_all.extend(ro[mask].tolist())

    ax2.scatter(g_bar_all, ratio_obs_all, s=4, alpha=0.25, color="#1f77b4", label="SPARC Radial Points")
    ax2.axhline(cap_val, color="#d62728", lw=2.2, ls="-", label=f"Model Diffusion Cap $1+\\mathcal{{R}} = {cap_val:.2f}$")
    gb_curve = np.logspace(-13, -8.5, 200)
    rar_ratio = 1.0 / (1.0 - np.exp(-np.sqrt(gb_curve / 1.20e-10)))
    ax2.plot(gb_curve, rar_ratio, "k--", lw=1.8, label="Empirical RAR ($g_\\dagger = 1.2\\times 10^{-10}$)")
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_xlim(1e-13, 3e-9)
    ax2.set_ylim(0.5, 60.0)
    ax2.set_xlabel(r"Baryonic Acceleration $g_{\rm bar}$ ($\rm m\,s^{-2}$)")
    ax2.set_ylabel(r"Acceleration Boost $g_{\rm obs}/g_{\rm bar} = (V_{\rm obs}/V_{\rm bar})^2$")
    ax2.set_title("(b) Saturation Cap Theorem vs. SPARC Data")
    ax2.legend(loc="upper right", fontsize=7.8)
    ax2.grid(True, alpha=0.25)

    # Panel C: Example held-out galaxy rotation curve (DDO154 or NGC2403)
    test_gals = [g for g in sparc_galaxies if g["split"] == "test"]
    ex_gal = next((g for g in test_gals if g["galaxy"] == "NGC2403"), test_gals[0])
    sig_frozen = t5_res["T5A_deciding"]["fitted_param"]
    v_t5a = predict_galaxy_rotation_curve(ex_gal, sig_frozen, f_leak_frozen)
    v_bar = np.sqrt(np.maximum(ex_gal["v_bar_mono2"], 0.0))
    ax3.errorbar(ex_gal["R"], ex_gal["v_obs"], yerr=ex_gal["e_v_obs"], fmt="ko", ms=4, capsize=2, label=f"{ex_gal['galaxy']} $V_{{\\rm obs}}$")
    ax3.plot(ex_gal["R"], v_t5a, color="#d62728", lw=2.0, label=f"T5-A Model ($\\hat{{\\sigma}}_{{\\rm ref}}={sig_frozen:.2f}$ kpc)")
    ax3.plot(ex_gal["R"], v_bar, color="#1f77b4", ls="--", lw=1.6, label="Baryons Only ($V_{\\rm bar}$)")
    ax3.set_xlabel("Radius $r$ (kpc)")
    ax3.set_ylabel("Circular Velocity (km/s)")
    ax3.set_title(f"(c) Held-Out Galaxy Rotation Curve ({ex_gal['galaxy']})")
    ax3.legend(loc="lower right", fontsize=8.0)
    ax3.grid(True, alpha=0.25)

    # Panel D: T5c NGC 1052-DF2 Dynamical Mass vs sigma_ref
    sig_grid = np.geomspace(0.5, 50.0, 120)
    m27_curve = [evaluate_t5c_df2(float(s), f_leak_frozen)["r_2p7_kpc_danieli19"]["M_pred_1e8_Msun"] for s in sig_grid]
    m31_curve = [evaluate_t5c_df2(float(s), f_leak_frozen)["r_3p1_kpc_vd18"]["M_pred_1e8_Msun"] for s in sig_grid]
    ax4.plot(sig_grid, m27_curve, color="#1f77b4", lw=2.0, label="$M_{\\rm pred}(<2.7\\,\\rm kpc)$")
    ax4.plot(sig_grid, m31_curve, color="#ff7f0e", lw=2.0, ls="--", label="$M_{\\rm pred}(<3.1\\,\\rm kpc)$")
    ax4.axhline(2.9, color="#1f77b4", ls=":", lw=1.2, label="Danieli+19 $2\\sigma$ PASS limit ($2.9\\times 10^8$)")
    ax4.axhline(3.2, color="#ff7f0e", ls=":", lw=1.2, label="van Dokkum+18 PASS limit ($3.2\\times 10^8$)")
    ax4.axhline(3.7, color="#d62728", ls="-.", lw=1.2, label="Danieli+19 $3\\sigma$ FAIL limit ($3.7\\times 10^8$)")
    ax4.axvline(sig_frozen, color="purple", lw=2.0, label=f"Frozen $\\hat{{\\sigma}}_{{\\rm ref}} = {sig_frozen:.2f}$ kpc")
    ax4.set_xscale("log")
    ax4.set_xlabel(r"Refraction Kernel Width $\sigma_{\rm ref}$ (kpc)")
    ax4.set_ylabel(r"Enclosed Mass $M_{\rm pred}(<r)$ ($10^8\,M_\odot$)")
    ax4.set_title("(d) Secondary Test T5c: NGC 1052-DF2 Stress Check")
    ax4.legend(loc="upper right", fontsize=7.2)
    ax4.grid(True, alpha=0.25)

    fig.tight_layout()
    fig.savefig(figures_dir / "fig4_t5_sparc_rotation_curves.png")
    plt.close(fig)

    # --- Figure 5: T6 Regional H0 & Coincidence Window ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.6))
    t6_d = part9["T6"]["T6_deciding"]
    reg = t6_d["regional_H0"]
    pix_ids = [r["pixel_ring_id"] for r in reg]
    h0_vals = [r["H0_kms_Mpc"] for r in reg]
    h0_errs = [r["sigma_H0_hf_only"] for r in reg]
    x_idx = np.arange(len(pix_ids))

    ax1.errorbar(x_idx, h0_vals, yerr=h0_errs, fmt="o", color="#1f77b4", capsize=4, lw=1.8, label="Regional $\\hat{H}_{0,i}$ (HF error)")
    ax1.axhline(t6_d["H0_bar_kms_Mpc"], color="#d62728", lw=2.0, label=f"GLS Mean $\\bar{{H}}_0 = {t6_d['H0_bar_kms_Mpc']:.2f}$ km/s/Mpc")
    ax1.axhline(67.36, color="#2ca02c", ls="--", lw=1.8, label="Planck 2018 $H_0 = 67.36 \\pm 0.54$")
    ax1.set_xticks(x_idx)
    ax1.set_xticklabels([f"Pix {p}\n($N={r['n_sn']}$)" for p, r in zip(pix_ids, reg)], fontsize=8.0)
    ax1.set_ylabel(r"Regional Hubble Constant $H_{0,i}$ ($\rm km\,s^{-1}\,Mpc^{-1}$)")
    ax1.set_title(f"(a) Secondary Test T6: Regional $H_0$ ($\\chi^2_{{\\rm het}}={t6_d['chi2_het']:.2f}, p={t6_d['p_het']:.3f}$)")
    ax1.legend(loc="lower right", fontsize=8.0)
    ax1.grid(True, alpha=0.25)

    # Panel B: Cosmic Coincidence Window
    a_arr = np.linspace(0.1, 2.5, 500)
    e2_arr = 0.3153 * (a_arr ** -3) + 0.6847
    ob_arr = (0.04930 * (a_arr ** -3)) / e2_arr
    odm_arr = (0.26447 * (a_arr ** -3)) / e2_arr
    ode_arr = 0.6847 / e2_arr

    ax2.plot(a_arr, ode_arr, color="#2ca02c", lw=2.0, label=r"$\Omega_{\rm de}(a)$ (Target $13/19 \approx 0.684$)")
    ax2.plot(a_arr, odm_arr, color="#1f77b4", lw=2.0, label=r"$\Omega_{\rm dm}(a)$ (Target $5/19 \approx 0.263$)")
    ax2.plot(a_arr, ob_arr, color="#ff7f0e", lw=2.0, label=r"$\Omega_b(a)$ (Target $1/19 \approx 0.053$)")

    cw_16 = part9["coincidence_window_sec6"]["f_leak_1_over_6"]["Criterion_H_Abs_5pct"]
    if cw_16["a_min"] is not None:
        ax2.axvspan(
            cw_16["a_min"],
            cw_16["a_max"],
            color="gold",
            alpha=0.28,
            label=f"H-Abs ($\\pm 0.05$): $\\Delta t = {cw_16['delta_t_gyr']:.2f}$ Gyr",
        )
    ax2.axvline(1.0, color="black", ls="--", lw=1.2, label="Present Epoch ($a = 1$)")
    ax2.set_xlabel("Scale Factor $a$")
    ax2.set_ylabel(r"Instantaneous Cosmic Energy Share $\Omega_i(a)$")
    ax2.set_title("(b) Section 6 Diagnostic: Cosmic Coincidence Window")
    ax2.legend(loc="center right", fontsize=7.8)
    ax2.grid(True, alpha=0.25)

    fig.tight_layout()
    fig.savefig(figures_dir / "fig5_t6_regional_h0_and_coincidence.png")
    plt.close(fig)


def main():
    set_below_normal_priority()
    root = Path(__file__).resolve().parent.parent
    results_dir = root / "results"

    # Load frozen values and Part 9 results
    freeze_t2 = json.loads((results_dir / "FREEZE_T2.json").read_text(encoding="utf-8"))
    freeze_t4 = json.loads((results_dir / "FREEZE_T4.json").read_text(encoding="utf-8"))
    freeze_t5 = json.loads((results_dir / "FREEZE_T5.json").read_text(encoding="utf-8"))
    part9 = json.loads((results_dir / "part9_cosmology_results.json").read_text(encoding="utf-8"))
    gates_g9 = json.loads((results_dir / "validation_gates_g9.json").read_text(encoding="utf-8"))

    print("1. Evaluating T4b on held-out test half, 7 sensitivity variants, and exploratory T4a...")
    t4_res = run_all_t4(root / "data" / "MERGERS.csv")

    print("2. Evaluating T5-A, T5-B, T5c, and RAR benchmark on held-out SPARC galaxies...")
    f_leak_frozen = freeze_t2["single_frozen_f_leak_for_T5"]["f_leak"]
    sigma_ref_frozen = freeze_t5["T5A_deciding_training_fit"]["fitted_param"]
    k_frozen = freeze_t5["T5B_deciding_training_fit"]["fitted_param"]

    sparc_galaxies = parse_sparc_catalog(root / "data" / "sparc")
    sparc_train = [g for g in sparc_galaxies if g["split"] == "train"]
    sparc_test = [g for g in sparc_galaxies if g["split"] == "test"]

    t5a_test_eval = evaluate_sparc_sample(sparc_test, "T5A", sigma_ref_frozen, f_leak_frozen)
    t5a_verdict, t5a_reasons = score_t5_subtest(t5a_test_eval)

    t5b_test_eval = evaluate_sparc_sample(sparc_test, "T5B", k_frozen, f_leak_frozen)
    t5b_verdict, t5b_reasons = score_t5_subtest(t5b_test_eval)

    baryon_only_test = evaluate_sparc_sample(sparc_test, "BARYON_ONLY", 0.0, f_leak_frozen)

    # Sensitivity evaluations on held-out test half
    sens_fits = freeze_t5["sensitivity_training_fits"]
    t5_sens_test = {}
    for skey, sfit in sens_fits.items():
        mtype = sfit["model_type"]
        f_used = sfit["f_leak"]
        pval = sfit["fitted_param"]
        seval = evaluate_sparc_sample(sparc_test, mtype, pval, f_used)
        seval.pop("per_galaxy", None)
        sv, sr = score_t5_subtest(seval)
        t5_sens_test[skey] = {
            "training_fit": sfit,
            "test_summary": seval,
            "verdict": sv,
            "reasons": sr,
        }

    t5c_res = evaluate_t5c_df2(sigma_ref_frozen, f_leak_frozen)
    rar_res = evaluate_rar_benchmark(sparc_train, sparc_test)
    tau_lag_frozen_gyr = freeze_t4["deciding_training_fit"]["tau_lag_gyr"]
    mechanistic_diag = compute_saturation_and_vc_tau_diagnostics(
        sparc_galaxies, sigma_ref_frozen, f_leak_frozen, tau_lag_frozen_gyr
    )

    t5_res = {
        "f_leak_frozen_used": f_leak_frozen,
        "T5A_deciding": {
            "fitted_param": sigma_ref_frozen,
            "training_fit": freeze_t5["T5A_deciding_training_fit"],
            "test_evaluation": t5a_test_eval,
            "verdict": t5a_verdict,
            "reasons": t5a_reasons,
        },
        "T5B_secondary": {
            "fitted_param": k_frozen,
            "training_fit": freeze_t5["T5B_deciding_training_fit"],
            "test_evaluation": t5b_test_eval,
            "verdict": t5b_verdict,
            "reasons": t5b_reasons,
        },
        "T5c_secondary_DF2": t5c_res,
        "RAR_benchmark": rar_res,
        "baryon_only_test": baryon_only_test,
        "mechanistic_diagnostics_f3_f4": mechanistic_diag,
        "T5_sensitivity": t5_sens_test,
    }

    print("3. Applying Section 3.2 Holm-Bonferroni control and Section 3.3 Model-Level Verdict...")
    p_t1_l1 = part9["T1"]["T1_L1_deciding"]["p_T1_L1_holm"]
    p_t4b = t4_res["T4b_deciding"]["test_evaluation"]["p_T4b_holm"]
    p_t6 = part9["T6"]["T6_deciding"]["p_T6_holm"]

    raw_disc_verdicts = {
        "T1-L1": part9["T1"]["T1_L1_deciding"]["joint_verdict_raw"],
        "T4b": t4_res["T4b_deciding"]["test_evaluation"]["verdict"],
        "T6": part9["T6"]["T6_deciding"]["verdict"],
    }
    holm_res = run_holm_bonferroni(p_t1_l1, p_t4b, p_t6, raw_disc_verdicts)

    pillar_verdicts = {
        "Pillar_1_T1_L1": holm_res["post_holm_verdicts"]["T1-L1"],
        "Pillar_2_T2_A": part9["T2"]["T2_A_deciding"]["joint_verdict"],
        "Pillar_3_T4b": holm_res["post_holm_verdicts"]["T4b"],
        "Pillar_4_T5_A": t5a_verdict,
    }

    secondary_verdicts = {
        "T1_Sign": part9["T1"]["T1_Sign_secondary"]["joint_verdict"],
        "T2_N1": part9["T2"]["T2_N1_secondary"]["verdict"],
        "T2_N2": part9["T2"]["T2_N2_secondary"]["verdict"],
        "T5_B": t5b_verdict,
        "T5c": t5c_res["verdict"],
        "T6": holm_res["post_holm_verdicts"]["T6"],
        "T4a": "EXPLORATORY (Unscored per PREREG.md Sec 5.4)",
    }

    # Section 3.3 Exhaustive Three-Way Model-Level Verdict Map (PREREG.md lines 87-91)
    p_vals = list(pillar_verdicts.values())
    if any(v == "FAIL" for v in p_vals):
        model_verdict = "MODEL FALSIFIED (FAIL)"
    elif all(v == "PASS" for v in p_vals):
        model_verdict = "MODEL SUPPORTED (PASS)"
    else:
        model_verdict = "MODEL INCONCLUSIVE (NOT FALSIFIED, NOT SUPPORTED)"

    print("4. Generating publication-quality figures in results/figures/...")
    generate_all_figures(
        results_dir / "figures",
        part9,
        t4_res,
        t5_res,
        sparc_galaxies,
        f_leak_frozen,
    )

    # Strip bulky per-galaxy arrays for clean master JSON readability while keeping summary stats
    t5_clean = json.loads(json.dumps(t5_res))
    t5_clean["baryon_only_test"].pop("per_galaxy", None)

    master_results = {
        "project": "Ropewalk Multiverse Empirical Test Suite (v1.0.2)",
        "generated_at": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "governing_preregistration": {
            "file": "PREREG.md (v1.0.2)",
            "prereg_v4_sha256": "53ce966a0af648edbc23c88199e275a3195f679a68eb4310bb48fb5fa501fc3b",
            "data_manifest_sha256": "73135698afb833e7e95e6a85c55475480132300e29f8b7b42d159c037067896d",
        },
        "overall_model_verdict": model_verdict,
        "primary_pillar_verdicts": pillar_verdicts,
        "secondary_test_verdicts": secondary_verdicts,
        "holm_bonferroni_control": holm_res,
        "validation_gates_g9": gates_g9,
        "T1": part9["T1"],
        "T2": part9["T2"],
        "T4": t4_res,
        "T5": t5_clean,
        "T6": part9["T6"],
        "coincidence_window_sec6": part9["coincidence_window_sec6"],
    }

    master_path = results_dir / "results.json"
    master_path.write_text(json.dumps(master_results, indent=2), encoding="utf-8")

    print("PART 10 COMPLETED.")
    print("  Pillar Verdicts:", json.dumps(pillar_verdicts, indent=2))
    print("  Secondary Verdicts:", json.dumps(secondary_verdicts, indent=2))
    print("  OVERALL MODEL VERDICT:", model_verdict)


if __name__ == "__main__":
    main()
