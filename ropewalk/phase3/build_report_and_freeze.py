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

PHASE3_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(PHASE3_DIR, ".."))


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


def _fmt_param(p_dict: dict, decimals: int = 5) -> str:
    m = p_dict["mean"]
    s = p_dict["std"]
    ci_lo, ci_hi = p_dict["ci95"]
    return f"`{m:.{decimals}f} ± {s:.{decimals}f}` (`[{ci_lo:.{decimals}f}, {ci_hi:.{decimals}f}]`)"


def generate_markdown(data: dict) -> str:
    proj = data["runtime_projection_after_first_per_family"]
    round_rt = data["round_runtimes_sec"]
    u_list = data["universes_in_manifest_order"]

    lines = [
        "---",
        'title: "MULTIVERSE v1: Phase 3 Injection Tests — Blind Analysis Results (PHASE3_RESULTS.md)"',
        'subtitle: "Phase 3 injection tests: supplementary, not pre-registered in Stage 1"',
        'author: "Gregory Mandarano / WickedAI — Executed by Gemini 4 Argon"',
        'date: "2026-10-31"',
        "---",
        "",
        "# MULTIVERSE v1: PHASE 3 INJECTION TEST RESULTS (`Phase 3 injection tests: supplementary, not pre-registered in Stage 1`)",
        "",
        "> **STATUS LABEL:** **Phase 3 injection tests: supplementary, not pre-registered in Stage 1.**",
        ">",
        "> **BLIND PROTOCOL NOTE:** Per `ARGON_PHASE3_HANDOFF.txt`, this report presents the per-universe parameter posteriors, test statistics, registered verdicts, runtime log, and `DEVIATIONS.md` record across the 45 mock universes in `MOCKS_FOR_ARGON/` in exact manifest order, with **no cross-universe summary or interpretation** prior to the answer-key reveal.",
        "",
        "---",
        "",
        "## 1. Runtime Log & First-Universe Runtime Projection",
        "",
        "### 1.1 First-Universe Benchmark & 24-Hour Budget Check (`Round 1`)",
        f"- **First `GALAXY` Universe (`{proj['first_galaxy_universe']}`):** `{proj['first_galaxy_sec']:.3f} s`",
        f"- **First `REGIONAL` Universe (`{proj['first_regional_universe']}`):** `{proj['first_regional_sec']:.3f} s`",
        f"- **First `COSMO` Universe (`{proj['first_cosmo_universe']}`, 16 MCMC chains on 12 workers):** `{proj['first_cosmo_sec']:.3f} s`",
        f"- **Projected 45-Universe Total Wall-Clock Runtime (Parallel Round Execution):** `{proj['projected_total_parallel_sec']:.2f} s` (`{proj['projected_total_parallel_min']:.2f} min`)",
        f"- **Projected 45-Universe Sum of 15× First-Universe Runtimes:** `{proj['projected_total_15x_sum_sec']:.2f} s` (`{proj['projected_total_15x_sum_min']:.2f} min` << `86,400 s` = 24 hours; `fits_within_24h = {proj['fits_within_24h']}`)",
        f"- **Actual Total Wall-Clock Runtime Across All 5 Rounds (45 Universes):** **`{data['total_wall_clock_sec']:.3f} s`** (`{data['total_wall_clock_sec'] / 60.0:.2f} min`)",
        "",
        "### 1.2 Per-Round Wall-Clock Runtimes",
        "",
        "| Round | Universes Analyzed | Wall-Clock Runtime (s) | Wall-Clock Runtime (min) |",
        "|---|---:|---:|---:|",
    ]

    for r_idx in range(1, 6):
        rk = f"Round_{r_idx}"
        r_sec = round_rt[rk]
        lines.append(f"| Round {r_idx} | 9 (`3 COSMO, 3 GALAXY, 3 REGIONAL`) | `{r_sec:.3f}` | `{r_sec / 60.0:.2f}` |")

    lines.extend([
        "",
        "### 1.3 Per-Universe Runtime Table (Manifest Order)",
        "",
        "| # | Universe ID | Family | Round | Runtime (s) |",
        "|---:|---|---|---:|---:|",
    ])
    for idx, u in enumerate(u_list, 1):
        lines.append(f"| {idx} | `{u['universe_id']}` | `{u['family']}` | {u['round']} | `{u['elapsed_sec']:.3f}` |")

    lines.extend([
        "",
        "---",
        "",
        "## 2. `DEVIATIONS.md` Entries",
        "",
        "- **Entry `P3-C1` (`2026-10-31T06:48:52`, Pre-Run Clarification Prior to Stamping `PHASE3_ANALYSIS_PLAN.md` and Prior to Any Run; `0` Runs Invalidated):**",
        "  - Each `COSMO` mock universe in `MOCKS_FOR_ARGON/<universe_id>/` provides its own joint Ly$\\alpha$ BAO+AP measurement in `desi_bao_dr2/lya_bao_ap_joint.json`, its own compressed CMB distance prior in `cmb_distance_prior/distance_prior.json`, its own external reference measurements in `REFERENCES.json`, and its Pantheon+ files in `pantheonplus/` (without underscore). Because frozen Stage 2 files (`scripts/cosmology.py`, `scripts/run_part8_fixes.py`, `scripts/run_part9_cosmology_tests.py`) must never be edited, thin wrappers (`MockDESIBAOLikelihood`, `MockCMBLikelihood`, `MockPantheonPlusLikelihood`) in `phase3/phase3_wrappers.py` override those hard-coded real-universe constants and paths with each universe's own files while leaving all physics and decision rules unchanged.",
        "  - No post-plan deviations occurred during execution (`0` post-plan deviations).",
        "",
        "---",
        "",
        "## 3. Per-Universe Results (Rounds 1 to 5, Manifest Order)",
        "",
    ])

    for idx, u in enumerate(u_list, 1):
        uid = u["universe_id"]
        fam = u["family"]
        rnd = u["round"]
        lines.append(f"### 3.{idx} `{uid}` — Family: `{fam}` · Round {rnd} (`{u['elapsed_sec']:.2f} s`)")
        lines.append("")

        if fam == "COSMO":
            refs = u["references_used"]
            lines.append(
                f"- **External Reference Measurements (`REFERENCES.json`):** "
                f"$\\mathcal{{R}}_{{\\rm ref}} = {refs['R_omegac_over_omegab']['value']} \\pm {refs['R_omegac_over_omegab']['sigma']}$, "
                f"$\\Omega_{{b,{{\\rm ref}}}} = {refs['Omega_b']['value']} \\pm {refs['Omega_b']['sigma']}$, "
                f"$100\\omega_{{b,{{\\rm ref}}}} = {refs['100omega_b']['value']} \\pm {refs['100omega_b']['sigma']}$, "
                f"$H_{{0,{{\\rm ref}}}} = {refs['H0']['value']} \\pm {refs['H0']['sigma']}\\text{{ km s}}^{{-1}}\\text{{ Mpc}}^{{-1}}$, "
                f"$\\text{{BBN }} 100\\omega_b = {refs['BBN_100omega_b_prior']['value']} \\pm {refs['BBN_100omega_b_prior']['sigma']}$."
            )
            lines.append("")
            lines.append("#### Posterior Parameters (`mean ± 1σ` and `[95% interval]`) and $\\chi^2_{\\min}$")
            lines.append("")
            lines.append(
                "| Reading | SN Compilation | Model | $\\chi^2_{\\min}$ | $\\Omega_{bc}$ (`mean ± 1σ`, `[95% CI]`) | $h$ (`mean ± 1σ`, `[95% CI]`) | $100\\omega_b$ (`mean ± 1σ`, `[95% CI]`) | $\\gamma_u$ (`mean ± 1σ`, `[95% CI]`) | $w_0$ (`mean ± 1σ`, `[95% CI]`) | $w_a$ (`mean ± 1σ`, `[95% CI]`) |"
            )
            lines.append("|---|---|---|---:|---|---|---|---|---|---|")

            for r_code, r_key in [("Reading B", "Reading_B"), ("Reading A", "Reading_A")]:
                r_obj = u[r_key]
                for sn_key, sn_disp in [("PantheonPlus", "Pantheon+"), ("DES_Dovekie", "DES-Dovekie")]:
                    sn_obj = r_obj[sn_key]
                    for m_key, m_disp in [
                        ("Law1", "Law 1 (`full_3x3`)"),
                        ("LCDM", "$\\Lambda$CDM (`full_3x3`)"),
                        ("CPL", "CPL (`full_3x3`)"),
                        ("T2A_CPL", "T2-A CPL (`cond_2x2`+BBN)"),
                    ]:
                        ch = sn_obj[m_key]
                        p = ch["parameters"]
                        c2 = ch["chi2_min"]
                        obc_str = _fmt_param(p["Omega_bc"], 5)
                        h_str = _fmt_param(p["h"], 5)
                        wb_str = _fmt_param(p["100_omega_b"], 5)
                        if m_key == "Law1":
                            gu_str = _fmt_param(p["gamma_u"], 5)
                            w0_str = _fmt_param(p["w0_implied"], 5) + " *(implied)*"
                            wa_str = _fmt_param(p["wa_implied"], 5) + " *(implied)*"
                        elif m_key == "LCDM":
                            gu_str = "—"
                            w0_str = "`-1.0` *(fixed)*"
                            wa_str = "`0.0` *(fixed)*"
                        else:
                            gu_str = "—"
                            w0_str = _fmt_param(p["w0"], 5)
                            wa_str = _fmt_param(p["wa"], 5)
                        lines.append(
                            f"| {r_code} | `{sn_disp}` | {m_disp} | `{c2:.4f}` | {obc_str} | {h_str} | {wb_str} | {gu_str} | {w0_str} | {wa_str} |"
                        )

            lines.append("")
            lines.append("#### Registered Verdicts and Test Statistics")
            lines.append("")
            lines.append(
                "| Reading | Test ID | `Pantheon+` Statistic & Per-Run Verdict | `DES-Dovekie` Statistic & Per-Run Verdict | Joint / Universe Verdict |"
            )
            lines.append("|---|---|---|---|---|")

            for r_code, r_key in [("Reading B", "Reading_B"), ("Reading A", "Reading_A")]:
                r_obj = u[r_key]
                vp = r_obj["PantheonPlus"]["verdicts_and_stats"]
                vd = r_obj["DES_Dovekie"]["verdicts_and_stats"]
                jv = r_obj["joint_verdicts"]

                # T1-L1
                t1p = vp["T1_L1"]
                t1d = vd["T1_L1"]
                lines.append(
                    f"| {r_code} | **`T1-L1`** | $A_r = {t1p['A_r_Law1_minus_LCDM']:+.4f}$, $B_r = {t1p['B_r_Law1_minus_CPL']:+.4f}$ ($p={t1p['p_discovery_vs_LCDM']:.4f}$) $\\to$ **`{t1p['verdict']}`** | "
                    f"$A_r = {t1d['A_r_Law1_minus_LCDM']:+.4f}$, $B_r = {t1d['B_r_Law1_minus_CPL']:+.4f}$ ($p={t1d['p_discovery_vs_LCDM']:.4f}$) $\\to$ **`{t1d['verdict']}`** | "
                    f"**`{jv['T1_L1']['verdict']}`** ($p_{{\\rm holm}} = {jv['T1_L1']['p_T1_L1_holm']:.4f}$) |"
                )

                # T1-Sign
                tsp = vp["T1_Sign"]
                tsd = vd["T1_Sign"]
                lines.append(
                    f"| {r_code} | **`T1-Sign`** | $P(w_0 > -1) = {tsp['P_w0_gt_minus1_mcmc']:.4f}$, $z = {tsp['z_gaussian_w0_gt_minus1']:+.2f}\\sigma$ (Law 1 $z_{{\\gamma_u}} = {tsp['Law1_z_gamma_u_gt_0']:+.2f}\\sigma$) $\\to$ **`{tsp['verdict']}`** | "
                    f"$P(w_0 > -1) = {tsd['P_w0_gt_minus1_mcmc']:.4f}$, $z = {tsd['z_gaussian_w0_gt_minus1']:+.2f}\\sigma$ (Law 1 $z_{{\\gamma_u}} = {tsd['Law1_z_gamma_u_gt_0']:+.2f}\\sigma$) $\\to$ **`{tsd['verdict']}`** | "
                    f"**`{jv['T1_Sign']['verdict']}`** |"
                )

                # T2-A
                t2p = vp["T2_A"]
                t2d = vd["T2_A"]
                t2p_l1 = t2p["from_Law1_chain"]
                t2d_l1 = t2d["from_Law1_chain"]
                lines.append(
                    f"| {r_code} | **`T2-A`** | $\\mathcal{{R}}_{{\\rm pred}} = {t2p['R_pred']:.4f} \\pm {t2p['sigma_R_pred']:.4f}$ ($f_{{\\rm leak}} = {t2p['f_leak']:.4f}$), $Z = {t2p['signed_tension_sigma']:+.3f}\\sigma$ ($|Z| = {t2p['tension_sigma']:.3f}\\sigma$) $\\to$ **`{t2p['per_run_verdict']}`** *(Law 1: $\\mathcal{{R}}={t2p_l1['R_pred']:.4f}, Z={t2p_l1['signed_tension_sigma']:+.3f}\\sigma \\to {t2p_l1['per_run_verdict']}$)* | "
                    f"$\\mathcal{{R}}_{{\\rm pred}} = {t2d['R_pred']:.4f} \\pm {t2d['sigma_R_pred']:.4f}$ ($f_{{\\rm leak}} = {t2d['f_leak']:.4f}$), $Z = {t2d['signed_tension_sigma']:+.3f}\\sigma$ ($|Z| = {t2d['tension_sigma']:.3f}\\sigma$) $\\to$ **`{t2d['per_run_verdict']}`** *(Law 1: $\\mathcal{{R}}={t2d_l1['R_pred']:.4f}, Z={t2d_l1['signed_tension_sigma']:+.3f}\\sigma \\to {t2d_l1['per_run_verdict']}$)* | "
                    f"**`{jv['T2_A']['verdict']}`** *(Law 1: `{jv['T2_A']['verdict_from_Law1_chain']}`)* |"
                )

            n1 = u["T2_N1"]
            n2 = u["T2_N2"]
            lines.append(
                f"| External (`REFERENCES.json`) | **`T2-N1`** | $\\Omega_b^{{\\rm model}} = 1/19 = {n1['Omega_b_model']:.6f}$ vs $\\Omega_{{b,\\rm ref}} = {n1['Omega_b_ref']:.6f} \\pm {n1['sigma_Omega_b_ref']:.6f}$ | "
                f"$\\Delta\\Omega_b = {n1['diff']:+.6f}$, $Z = {n1['signed_tension_sigma']:+.4f}\\sigma$ ($|Z| = {n1['tension_sigma']:.4f}\\sigma$) | **`{n1['verdict']}`** |"
            )
            lines.append(
                f"| External (`REFERENCES.json`) | **`T2-N2`** | $H_0^{{\\rm pred}} = {n2['H0_pred_kms_Mpc']:.4f} \\pm {n2['sigma_H0_pred']:.4f}$ vs $H_{{0,\\rm ref}} = {n2['H0_ref_kms_Mpc']:.4f} \\pm {n2['sigma_H0_ref']:.4f}$ | "
                f"$\\Delta H_0 = {n2['diff_H0']:+.4f}$, $\\sigma_{{\\rm comb}} = {n2['sigma_comb_H0']:.4f}$, $Z = {n2['signed_tension_sigma']:+.4f}\\sigma$ ($|Z| = {n2['tension_sigma']:.4f}\\sigma$) | **`{n2['verdict']}`** |"
            )
            lines.append("")

        elif fam == "GALAXY":
            t5a = u["T5_A"]
            t5b = u["T5_B"]
            u_a = t5a["sigma_ref_uncertainty"]
            u_b = t5b["k_uncertainty"]
            lines.append("- **Fixed Input Leak Fraction:** $f_{\\rm leak} = 1/6 = 0.166667$ ($\\mathcal{R} = 6(1 - f_{\\rm leak}) = 5.0$).")
            lines.append("")
            lines.append(
                "| Subtest | Fitted Parameter (Training Half) | Bootstrap `mean ± 1σ` (`[95% CI]`) | Profile Posterior (`sum_chi2_red`) `mean ± 1σ` (`[95% CI]`) | Profile Posterior (`total_chi2`) `mean ± 1σ` (`[95% CI]`) | Test-Half Median $\\chi^2_{\\rm red}$ ($M_{\\chi^2}$) | Test-Half Fraction $\\chi^2_{\\rm red} < 2$ ($F_{<2}$) | Verdict |"
            )
            lines.append("|---|---:|---|---|---|---:|---:|---|")
            lines.append(
                f"| **`T5-A`** | $\\hat{{\\sigma}}_{{\\rm ref}} = {t5a['fitted_sigma_ref_kpc']:.5f}\\text{{ kpc}}$ | "
                f"{_fmt_param(u_a['bootstrap_train_galaxies'], 5)} kpc | "
                f"{_fmt_param(u_a['posterior_sum_chi2_red'], 5)} kpc | "
                f"{_fmt_param(u_a['posterior_total_chi2'], 5)} kpc | "
                f"`{t5a['test_median_chi2_red']:.4f}` | `{t5a['test_frac_chi2_red_lt_2']:.4f}` (`{t5a['n_test_lt_2']}/{t5a['n_test_galaxies']}`) | **`{t5a['verdict']}`** |"
            )
            lines.append(
                f"| **`T5-B`** | $\\hat{{k}} = {t5b['fitted_k']:.5f}$ | "
                f"{_fmt_param(u_b['bootstrap_train_galaxies'], 5)} | "
                f"{_fmt_param(u_b['posterior_sum_chi2_red'], 5)} | "
                f"{_fmt_param(u_b['posterior_total_chi2'], 5)} | "
                f"`{t5b['test_median_chi2_red']:.4f}` | `{t5b['test_frac_chi2_red_lt_2']:.4f}` (`{t5b['n_test_lt_2']}/{t5b['n_test_galaxies']}`) | **`{t5b['verdict']}`** |"
            )
            lines.append("")

        elif fam == "REGIONAL":
            cal = u["calibrator_fit"]
            t6 = u["T6"]
            lines.append(
                f"- **SH0ES Calibrator Fit ($N_{{\\rm cal}} = {cal['n_calibrators']}$):** "
                f"$\\hat{{M}}_B^{{\\rm fixed}} = {cal['M_B_fixed']:.6f} \\pm {cal['sigma_M_B_fixed']:.6f}\\text{{ mag}}$."
            )
            lines.append(
                f"- **Global Summary & Registered Test Statistic (`T6`):** "
                f"$N_{{\\rm pix}} = {t6['N_pix']}$ (`{t6['n_hf_retained']}` retained Hubble-flow SNe, $\\text{{dof}} = {t6['dof']}$), "
                f"GLS weighted mean $\\bar{{H}}_0 = {t6['H0_bar_kms_Mpc']:.4f} \\pm {t6['sigma_H0_bar_hf_only']:.4f}\\text{{ km s}}^{{-1}}\\text{{ Mpc}}^{{-1}}$ "
                f"(total error incl. calibrator $\\pm {t6['sigma_H0_bar_total']:.4f}$), "
                f"$Z_{{\\rm all\\text{{-}}sky}} = {t6['Z_all_sky_vs_Planck']:+.4f}\\sigma$, "
                f"**$\\chi^2_{{\\rm het}} = {t6['chi2_het']:.4f}$**, **$p_{{\\rm het}} = {t6['p_het']:.6f}$**, "
                f"**`T6` Verdict: `{t6['verdict']}`**."
            )
            lines.append("")
            lines.append("| HEALPix $N_{\\rm side}=1$ Galactic `RING` Pixel | $N_{\\rm SN}$ | $\\hat{H}_{0,i}$ ($\\text{km s}^{-1}\\text{ Mpc}^{-1}$) | $\\sigma_{H_{0,i}}$ (Hubble-Flow Only) | $\\sigma_{H_{0,i},{\\rm tot}}$ (Incl. Calibrator) |")
            lines.append("|---:|---:|---:|---:|---:|")
            for reg_row in t6["regional_H0"]:
                lines.append(
                    f"| Pixel `{reg_row['pixel_ring_id']}` | {reg_row['n_sn']} | `{reg_row['H0_kms_Mpc']:.4f}` | `± {reg_row['sigma_H0_hf_only']:.4f}` | `± {reg_row['sigma_H0_total_incl_cal']:.4f}` |"
                )
            lines.append("")

    return "\n".join(lines) + "\n"


def sha256_file(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    results_path = os.path.join(PHASE3_DIR, "results.json")
    with open(results_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    md_text = generate_markdown(data)
    md_p3 = os.path.join(PHASE3_DIR, "PHASE3_RESULTS.md")
    md_root = os.path.join(ROOT_DIR, "PHASE3_RESULTS.md")
    with open(md_p3, "w", encoding="utf-8", newline="\n") as f:
        f.write(md_text)
    shutil.copy2(md_p3, md_root)

    # Log generation of PHASE3_RESULTS.md before hashing into PHASE3_RESULTS_v1.sha256
    log_path = os.path.join(PHASE3_DIR, "ACTIVITY_LOG_PHASE3.md")
    with open(log_path, "a", encoding="utf-8", newline="\n") as f:
        f.write(
            f"{time.strftime('%Y-%m-%dT%H:%M:%S')} - Created file `D:\\Argon_Code\\Ropewalk\\phase3\\PHASE3_RESULTS.md` "
            f"(mirrored to `D:\\Argon_Code\\Ropewalk\\PHASE3_RESULTS.md`) and freezing all Phase 3 outputs into `PHASE3_RESULTS_v1.sha256`.\n"
        )

    # Collect all files in phase3/ (excluding PHASE3_RESULTS_v1.sha256 and its .ots)
    rel_files = []
    for root, dirs, files in os.walk(PHASE3_DIR):
        dirs.sort()
        for fn in sorted(files):
            if fn in ("PHASE3_RESULTS_v1.sha256", "PHASE3_RESULTS_v1.sha256.ots"):
                continue
            if fn.endswith(".pyc") or "__pycache__" in root:
                continue
            full_p = os.path.join(root, fn)
            rel_p = os.path.relpath(full_p, ROOT_DIR).replace(os.sep, "/")
            rel_files.append(rel_p)

    # Also include root-mirrored Phase 3 files & handoff/manifest inputs
    for root_fn in [
        "ARGON_PHASE3_HANDOFF.txt",
        "MOCKS_FOR_ARGON/MOCK_MANIFEST.csv",
        "PHASE3_ANALYSIS_PLAN.md",
        "PHASE3_ANALYSIS_PLAN.sha256",
        "PHASE3_ANALYSIS_PLAN.sha256.ots",
        "PHASE3_RESULTS.md",
    ]:
        p = os.path.join(ROOT_DIR, root_fn.replace("/", os.sep))
        if os.path.exists(p):
            rel_files.append(root_fn)

    rel_files = sorted(set(rel_files))

    plan_sha_path = os.path.join(PHASE3_DIR, "PHASE3_ANALYSIS_PLAN.sha256")
    plan_manifest_hash = sha256_file(plan_sha_path)

    manifest_lines = [
        "# MULTIVERSE v1: Phase 3 Injection Tests Freeze Manifest (PHASE3_RESULTS_v1.sha256)",
        "# Label: Phase 3 injection tests: supplementary, not pre-registered in Stage 1",
        f"# Generated at: {time.strftime('%Y-%m-%dT%H:%M:%S-04:00')}",
        f"# Chained from PHASE3_ANALYSIS_PLAN.sha256: {plan_manifest_hash}",
        "# Format: <sha256_hex>  <relative_path>",
    ]
    for rel_p in rel_files:
        full_p = os.path.join(ROOT_DIR, rel_p.replace("/", os.sep))
        manifest_lines.append(f"{sha256_file(full_p)}  {rel_p}")

    manifest_p3 = os.path.join(PHASE3_DIR, "PHASE3_RESULTS_v1.sha256")
    manifest_root = os.path.join(ROOT_DIR, "PHASE3_RESULTS_v1.sha256")
    with open(manifest_p3, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(manifest_lines) + "\n")
    shutil.copy2(manifest_p3, manifest_root)

    results_manifest_hash = sha256_file(manifest_p3)
    print(f"PHASE3_ANALYSIS_PLAN.sha256 hash: {plan_manifest_hash}")
    print(f"PHASE3_RESULTS_v1.sha256 hash:    {results_manifest_hash}")

    ots_mod = setup_ots()
    stamp_with_ots(ots_mod, manifest_p3)
    shutil.copy2(manifest_p3 + ".ots", manifest_root + ".ots")
    print("Stamped PHASE3_RESULTS_v1.sha256.ots and mirrored to workspace root.")


if __name__ == "__main__":
    main()
