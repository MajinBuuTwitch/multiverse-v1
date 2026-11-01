#!/usr/bin/env python3
"""
Independent Phase 3 Blind-Injection Rescoring & Diagnostic Audit Script.
Works exclusively inside D:\\Multiverse Review using Python standard library only.
"""

from __future__ import annotations
import hashlib
import json
import math
import pathlib
import statistics
from typing import Any


WORKSPACE = pathlib.Path(__file__).resolve().parent

INPUT_FILES = [
    "ANSWER_KEY.json",
    "PHASE3_ANALYSIS_PLAN.md",
    "PHASE3_INJECTION_SPEC_SEALED.txt",
    "PHASE3_INJECTION_v1.sha256",
    "PHASE3_RESULTS_v1.sha256",
    "results.json",
]


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_manifest(path: pathlib.Path) -> dict[str, list[str]]:
    """Return mapping: sha256_hex -> list of relative paths in manifest."""
    entries: dict[str, list[str]] = {}
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            parts = s.split(None, 1)
            if len(parts) == 2:
                digest, rel_path = parts[0].lower(), parts[1].strip()
                entries.setdefault(digest, []).append(rel_path)
    return entries


def verify_integrity() -> tuple[bool, list[dict[str, Any]]]:
    inj_manifest = parse_manifest(WORKSPACE / "PHASE3_INJECTION_v1.sha256")
    res_manifest = parse_manifest(WORKSPACE / "PHASE3_RESULTS_v1.sha256")

    rows: list[dict[str, Any]] = []
    all_ok = True
    for fname in INPUT_FILES:
        fpath = WORKSPACE / fname
        digest = sha256_file(fpath)
        inj_matches = inj_manifest.get(digest, [])
        res_matches = res_manifest.get(digest, [])
        if fname in ("PHASE3_INJECTION_v1.sha256", "PHASE3_RESULTS_v1.sha256"):
            status = "MANIFEST (SELF)"
        elif inj_matches or res_matches:
            status = "MATCH"
        else:
            status = "NO MATCH"
            all_ok = False
        rows.append({
            "file": fname,
            "sha256": digest,
            "inj_paths": inj_matches,
            "res_paths": res_matches,
            "status": status,
        })
    return all_ok, rows


def score_cosmo_s1(ak: dict[str, Any], res: dict[str, Any]) -> list[dict[str, Any]]:
    u_by_truth: dict[str, list[dict[str, Any]]] = {}
    for u in ak["universes"]:
        u_by_truth.setdefault(u["truth"], []).append(u)

    records: list[dict[str, Any]] = []
    for t_id in ["C1", "C2", "C3"]:
        t_info = ak["truths"][t_id]
        true_map: dict[str, float] = {
            "Omega_bc": t_info["Obc"],
            "Omega_m_tot": t_info["Om_tot"],
            "h": t_info["h"],
            "100_omega_b": t_info["wb100"],
        }
        if t_id == "C1":
            true_map["gamma_u"] = 0.0
            true_map["w0"] = -1.0
            true_map["wa"] = 0.0
        elif t_id == "C2":
            true_map["gamma_u"] = t_info["gam"]
            true_map["w0"] = t_info["w0_fit"]
            true_map["wa"] = t_info["wa_tangent"]
        elif t_id == "C3":
            true_map["w0"] = t_info["w0"]
            true_map["wa"] = t_info["wa"]

        for reading in ["Reading_B", "Reading_A"]:
            for sn in ["PantheonPlus", "DES_Dovekie"]:
                for model in ["Law1", "CPL", "T2A_CPL", "LCDM"]:
                    for pname in ["Omega_bc", "h", "100_omega_b", "gamma_u", "w0", "wa"]:
                        if pname not in true_map:
                            continue
                        first_u = res["universes"][u_by_truth[t_id][0]["universe_id"]]
                        p_dict = first_u[reading][sn][model]["parameters"]
                        if pname not in p_dict:
                            continue
                        t_val = true_map[pname]
                        means, meds, stds, s68s, cis = [], [], [], [], []
                        per_u_in_ci = []
                        per_u_in_sym = []
                        per_u_in_med = []
                        zs = []
                        for u in u_by_truth[t_id]:
                            uid = u["universe_id"]
                            pd = res["universes"][uid][reading][sn][model]["parameters"][pname]
                            m = pd["mean"]
                            md = pd["median"]
                            s = pd["std"]
                            s68 = pd["sigma_68"]
                            lo, hi = pd["ci95"]
                            means.append(m)
                            meds.append(md)
                            stds.append(s)
                            s68s.append(s68)
                            cis.append((lo, hi))
                            per_u_in_ci.append(lo <= t_val <= hi)
                            per_u_in_sym.append(abs(m - t_val) <= 1.96 * s)
                            per_u_in_med.append(abs(md - t_val) <= 1.96 * s68)
                            zs.append((m - t_val) / s)

                        n_in_ci = sum(per_u_in_ci)
                        n_in_sym = sum(per_u_in_sym)
                        n_in_med = sum(per_u_in_med)

                        mean_rec = statistics.mean(means)
                        signed_bias = mean_rec - t_val
                        abs_bias = abs(signed_bias)
                        mean_sig = statistics.mean(stds)
                        ratio = abs_bias / mean_sig

                        med_rec = statistics.mean(meds)
                        signed_bias_med = med_rec - t_val
                        abs_bias_med = abs(signed_bias_med)
                        mean_s68 = statistics.mean(s68s)
                        ratio_med = abs_bias_med / mean_s68

                        emp_sd = statistics.stdev(means)
                        rms_z = math.sqrt(statistics.mean([z * z for z in zs]))

                        pass_primary = (n_in_ci >= 4) and (abs_bias < mean_sig)
                        pass_sym = (n_in_sym >= 4) and (abs_bias < mean_sig)
                        pass_med_ci = (n_in_ci >= 4) and (abs_bias_med < mean_s68)

                        records.append({
                            "truth": t_id,
                            "reading": reading,
                            "sn_set": sn,
                            "model": model,
                            "param": pname,
                            "truth_val": t_val,
                            "mean_rec": mean_rec,
                            "signed_bias": signed_bias,
                            "abs_bias": abs_bias,
                            "mean_sigma": mean_sig,
                            "bias_over_sigma": ratio,
                            "n_in_ci95": n_in_ci,
                            "per_u_in_ci95": per_u_in_ci,
                            "verdict_primary": "PASS" if pass_primary else "MISS",
                            "n_in_sym95": n_in_sym,
                            "verdict_sym95": "PASS" if pass_sym else "MISS",
                            "n_in_med95": n_in_med,
                            "signed_bias_med": signed_bias_med,
                            "mean_s68": mean_s68,
                            "bias_med_over_s68": ratio_med,
                            "verdict_med_ci95": "PASS" if pass_med_ci else "MISS",
                            "emp_sd": emp_sd,
                            "emp_over_post_sig": emp_sd / mean_sig,
                            "rms_z": rms_z,
                        })
    return records


def score_galaxy_s1(ak: dict[str, Any], res: dict[str, Any]) -> list[dict[str, Any]]:
    u_by_truth: dict[str, list[dict[str, Any]]] = {}
    for u in ak["universes"]:
        u_by_truth.setdefault(u["truth"], []).append(u)

    records: list[dict[str, Any]] = []
    for t_id in ["G1", "G2"]:
        t_val = ak["truths"][t_id]["sigma_ref_kpc"]
        pts = [res["universes"][u["universe_id"]]["T5_A"]["fitted_sigma_ref_kpc"] for u in u_by_truth[t_id]]
        emp_sd_pt = statistics.stdev(pts)
        for method in ["bootstrap_train_galaxies", "posterior_sum_chi2_red", "posterior_total_chi2"]:
            means, meds, stds, s68s, cis = [], [], [], [], []
            in_ci_list, in_sym_list, in_pt_sym_list = [], [], []
            for u in u_by_truth[t_id]:
                uid = u["universe_id"]
                t5a = res["universes"][uid]["T5_A"]
                pt = t5a["fitted_sigma_ref_kpc"]
                unc = t5a["sigma_ref_uncertainty"][method]
                m, md, s, s68 = unc["mean"], unc["median"], unc["std"], unc["sigma_68"]
                lo, hi = unc["ci95"]
                means.append(m)
                meds.append(md)
                stds.append(s)
                s68s.append(s68)
                cis.append((lo, hi))
                in_ci_list.append(lo <= t_val <= hi)
                in_sym_list.append(abs(m - t_val) <= 1.96 * s)
                in_pt_sym_list.append(abs(pt - t_val) <= 1.96 * s)

            n_in_ci = sum(in_ci_list)
            n_in_sym = sum(in_sym_list)
            n_in_pt_sym = sum(in_pt_sym_list)
            mean_rec = statistics.mean(means)
            mean_pt = statistics.mean(pts)
            bias_mean = mean_rec - t_val
            bias_pt = mean_pt - t_val
            mean_sig = statistics.mean(stds)
            pass_s1 = (n_in_ci >= 4) and (abs(bias_mean) < mean_sig)
            pass_pt = (n_in_ci >= 4) and (abs(bias_pt) < mean_sig)
            records.append({
                "truth": t_id,
                "method": method,
                "truth_val": t_val,
                "mean_rec": mean_rec,
                "mean_pt": mean_pt,
                "signed_bias_mean": bias_mean,
                "signed_bias_pt": bias_pt,
                "abs_bias_mean": abs(bias_mean),
                "abs_bias_pt": abs(bias_pt),
                "mean_sigma": mean_sig,
                "bias_over_sigma": abs(bias_mean) / mean_sig,
                "pt_bias_over_sigma": abs(bias_pt) / mean_sig,
                "n_in_ci95": n_in_ci,
                "n_in_sym95": n_in_sym,
                "n_in_pt_sym95": n_in_pt_sym,
                "emp_sd_pt": emp_sd_pt,
                "emp_over_sig": emp_sd_pt / mean_sig,
                "verdict": "PASS" if pass_s1 else "MISS",
                "verdict_pt": "PASS" if pass_pt else "MISS",
            })
    return records


def score_regional_s1(ak: dict[str, Any], res: dict[str, Any]) -> dict[str, Any]:
    u_by_truth: dict[str, list[dict[str, Any]]] = {}
    for u in ak["universes"]:
        u_by_truth.setdefault(u["truth"], []).append(u)

    regions = [0, 1, 2, 3, 5, 6, 8, 9, 10]
    out: dict[str, Any] = {"per_region": [], "summary": [], "all_sky_bar": []}

    for t_id in ["H1", "H2", "H3"]:
        us = u_by_truth[t_id]
        for bar_mode in ["total_incl_cal", "hf_only"]:
            in_cnt = 0
            errs = []
            sigs = []
            for u in us:
                t6 = res["universes"][u["universe_id"]]["T6"]
                err = t6["H0_bar_kms_Mpc"] - 73.0
                sig = t6["sigma_H0_bar_total"] if bar_mode == "total_incl_cal" else t6["sigma_H0_bar_hf_only"]
                if abs(err) <= 1.96 * sig:
                    in_cnt += 1
                errs.append(err)
                sigs.append(sig)
            mb = statistics.mean(errs)
            ms = statistics.mean(sigs)
            out["all_sky_bar"].append({
                "truth": t_id,
                "mode": bar_mode,
                "n_in_95": in_cnt,
                "signed_bias": mb,
                "abs_bias": abs(mb),
                "mean_sigma": ms,
                "bias_over_sigma": abs(mb) / ms,
                "verdict": "PASS" if (in_cnt >= 4 and abs(mb) < ms) else "MISS",
            })

        for mode in ["abs_total", "abs_hf", "cal_corr_hf", "rel_count_wt_hf", "rel_gls_bar_hf"]:
            reg_pass = 0
            pooled_in = 0
            all_errs = []
            all_sigs = []
            reg_abs_biases = []
            u_in_counts = [0] * 5

            for r_id in regions:
                rk = str(r_id)
                in_cnt = 0
                errs = []
                sigs = []
                for idx, u in enumerate(us):
                    uid = u["universe_id"]
                    t6 = res["universes"][uid]["T6"]
                    cal = res["universes"][uid]["calibrator_fit"]
                    scale = 10.0 ** (0.2 * (cal["M_B_fixed"] - (-19.253)))
                    counts = u["region_counts_HF"]
                    rec_map = {x["pixel_ring_id"]: x for x in t6["regional_H0"]}
                    rec_r = rec_map[r_id]
                    rec_count_wt = sum(rec_map[int(k)]["H0_kms_Mpc"] * counts[k] for k in counts) / sum(counts.values())

                    tr_val = u["H0_regions"][rk]
                    rc_val = rec_r["H0_kms_Mpc"]
                    if mode == "abs_total":
                        err = rc_val - tr_val
                        sig = rec_r["sigma_H0_total_incl_cal"]
                    elif mode == "abs_hf":
                        err = rc_val - tr_val
                        sig = rec_r["sigma_H0_hf_only"]
                    elif mode == "cal_corr_hf":
                        err = (rc_val / scale) - tr_val
                        sig = rec_r["sigma_H0_hf_only"]
                    elif mode == "rel_count_wt_hf":
                        err = (rc_val - rec_count_wt) - (tr_val - 73.0)
                        sig = rec_r["sigma_H0_hf_only"]
                    elif mode == "rel_gls_bar_hf":
                        err = (rc_val - t6["H0_bar_kms_Mpc"]) - (tr_val - 73.0)
                        sig = rec_r["sigma_H0_hf_only"]

                    if abs(err) <= 1.96 * sig:
                        in_cnt += 1
                        pooled_in += 1
                        u_in_counts[idx] += 1
                    errs.append(err)
                    sigs.append(sig)
                    all_errs.append(err)
                    all_sigs.append(sig)

                mb = statistics.mean(errs)
                ms = statistics.mean(sigs)
                reg_abs_biases.append(abs(mb))
                p_ok = (in_cnt >= 4) and (abs(mb) < ms)
                if p_ok:
                    reg_pass += 1
                out["per_region"].append({
                    "truth": t_id,
                    "mode": mode,
                    "region": r_id,
                    "n_in_95": in_cnt,
                    "signed_bias": mb,
                    "abs_bias": abs(mb),
                    "mean_sigma": ms,
                    "bias_over_sigma": abs(mb) / ms,
                    "verdict": "PASS" if p_ok else "MISS",
                })

            gm_bias = statistics.mean(all_errs)
            gm_sig = statistics.mean(all_sigs)
            mean_abs_reg_bias = statistics.mean(reg_abs_biases)
            u_pass_7of9 = sum(1 for c in u_in_counts if c >= 7)
            u_pass_8of9 = sum(1 for c in u_in_counts if c >= 8)
            out["summary"].append({
                "truth": t_id,
                "mode": mode,
                "regions_passing_s1": reg_pass,
                "pooled_in_95": pooled_in,
                "pooled_pct": pooled_in / 45.0 * 100.0,
                "u_in_counts": u_in_counts,
                "u_pass_8of9": u_pass_8of9,
                "u_pass_7of9": u_pass_7of9,
                "grand_mean_bias": gm_bias,
                "mean_abs_reg_bias": mean_abs_reg_bias,
                "grand_mean_sigma": gm_sig,
                "grand_bias_over_sigma": abs(gm_bias) / gm_sig,
                "mean_abs_reg_bias_over_sigma": mean_abs_reg_bias / gm_sig,
                "verdict_all9_regions": "PASS" if reg_pass == 9 else ("PARTIAL (" + str(reg_pass) + "/9)" if reg_pass >= 7 else "MISS"),
                "verdict_pooled": "PASS" if (pooled_in >= 36 and abs(gm_bias) < gm_sig) else "MISS",
            })
    return out


def score_s2(ak: dict[str, Any], res: dict[str, Any]) -> dict[str, Any]:
    u_by_truth: dict[str, list[dict[str, Any]]] = {}
    for u in ak["universes"]:
        u_by_truth.setdefault(u["truth"], []).append(u)

    cosmo_rows: list[dict[str, Any]] = []
    for t_id in ["C1", "C2", "C3"]:
        us = u_by_truth[t_id]
        for reading in ["Reading_B", "Reading_A"]:
            for sn in ["Joint", "PantheonPlus", "DES_Dovekie"]:
                if sn == "Joint":
                    if t_id == "C1":
                        checks = [
                            ("T2-A FAIL (T2A_CPL)", lambda u_obj, jv: jv["T2_A"]["verdict"] == "FAIL", lambda u_obj, jv: jv["T2_A"]["verdict"]),
                            ("T2-A FAIL (Law1 chain)", lambda u_obj, jv: jv["T2_A"]["verdict_from_Law1_chain"] == "FAIL", lambda u_obj, jv: jv["T2_A"]["verdict_from_Law1_chain"]),
                            ("T2-N1 FAIL", lambda u_obj, jv: u_obj["T2_N1"]["verdict"] == "FAIL", lambda u_obj, jv: u_obj["T2_N1"]["verdict"]),
                            ("T2-N2 FAIL (primary Planck omega_b)", lambda u_obj, jv: u_obj["T2_N2"]["verdict"] == "FAIL", lambda u_obj, jv: u_obj["T2_N2"]["verdict"]),
                            ("T2-N2 FAIL (BBN prior sensitivity |Z|>3)", lambda u_obj, jv: u_obj["T2_N2"]["BBN_prior_sensitivity"]["tension_sigma"] > 3.0, lambda u_obj, jv: f"|Z|={u_obj['T2_N2']['BBN_prior_sensitivity']['tension_sigma']:.2f}"),
                            ("T1-L1 not PASS", lambda u_obj, jv: jv["T1_L1"]["verdict"] != "PASS", lambda u_obj, jv: jv["T1_L1"]["verdict"]),
                        ]
                    elif t_id == "C2":
                        checks = [
                            ("T2-A PASS (T2A_CPL)", lambda u_obj, jv: jv["T2_A"]["verdict"] == "PASS", lambda u_obj, jv: jv["T2_A"]["verdict"]),
                            ("T2-A PASS (Law1 chain)", lambda u_obj, jv: jv["T2_A"]["verdict_from_Law1_chain"] == "PASS", lambda u_obj, jv: jv["T2_A"]["verdict_from_Law1_chain"]),
                            ("T2-N1 PASS", lambda u_obj, jv: u_obj["T2_N1"]["verdict"] == "PASS", lambda u_obj, jv: u_obj["T2_N1"]["verdict"]),
                            ("T2-N2 PASS (primary Planck omega_b)", lambda u_obj, jv: u_obj["T2_N2"]["verdict"] == "PASS", lambda u_obj, jv: u_obj["T2_N2"]["verdict"]),
                            ("T2-N2 PASS (BBN prior sensitivity |Z|<2)", lambda u_obj, jv: u_obj["T2_N2"]["BBN_prior_sensitivity"]["tension_sigma"] < 2.0, lambda u_obj, jv: f"|Z|={u_obj['T2_N2']['BBN_prior_sensitivity']['tension_sigma']:.2f}"),
                            ("T1-Sign PASS", lambda u_obj, jv: jv["T1_Sign"]["verdict"] == "PASS", lambda u_obj, jv: jv["T1_Sign"]["verdict"]),
                            ("T1-L1 not FAIL", lambda u_obj, jv: jv["T1_L1"]["verdict"] != "FAIL", lambda u_obj, jv: jv["T1_L1"]["verdict"]),
                        ]
                    else:  # C3
                        checks = [
                            ("T1-L1 FAIL", lambda u_obj, jv: jv["T1_L1"]["verdict"] == "FAIL", lambda u_obj, jv: jv["T1_L1"]["verdict"]),
                            ("T1-Sign PASS", lambda u_obj, jv: jv["T1_Sign"]["verdict"] == "PASS", lambda u_obj, jv: jv["T1_Sign"]["verdict"]),
                            ("T2-A FAIL (T2A_CPL)", lambda u_obj, jv: jv["T2_A"]["verdict"] == "FAIL", lambda u_obj, jv: jv["T2_A"]["verdict"]),
                            ("T2-A FAIL (Law1 chain)", lambda u_obj, jv: jv["T2_A"]["verdict_from_Law1_chain"] == "FAIL", lambda u_obj, jv: jv["T2_A"]["verdict_from_Law1_chain"]),
                        ]
                    for cname, pred_fn, val_fn in checks:
                        vals = []
                        matches = 0
                        for u in us:
                            u_obj = res["universes"][u["universe_id"]]
                            jv = u_obj[reading]["joint_verdicts"]
                            ok = pred_fn(u_obj, jv)
                            if ok:
                                matches += 1
                            vals.append(val_fn(u_obj, jv))
                        cosmo_rows.append({
                            "truth": t_id,
                            "reading": reading,
                            "sn_set": sn,
                            "criterion": cname,
                            "realizations": vals,
                            "matches": matches,
                            "verdict": "PASS" if matches >= 4 else "MISS",
                        })
                else:
                    if t_id == "C1":
                        checks = [
                            ("T2-A FAIL (T2A_CPL)", lambda d: d["verdicts_and_stats"]["T2_A"]["per_run_verdict"] == "FAIL", lambda d: d["verdicts_and_stats"]["T2_A"]["per_run_verdict"]),
                            ("T2-A FAIL (Law1 chain)", lambda d: d["verdicts_and_stats"]["T2_A"]["from_Law1_chain"]["per_run_verdict"] == "FAIL", lambda d: d["verdicts_and_stats"]["T2_A"]["from_Law1_chain"]["per_run_verdict"]),
                            ("T1-L1 not PASS", lambda d: d["verdicts_and_stats"]["T1_L1"]["verdict"] != "PASS", lambda d: d["verdicts_and_stats"]["T1_L1"]["verdict"]),
                            ("gamma_u ci95 [p2.5,p97.5] includes 0", lambda d: d["Law1"]["parameters"]["gamma_u"]["ci95"][0] <= 0.0 <= d["Law1"]["parameters"]["gamma_u"]["ci95"][1], lambda d: f"[{d['Law1']['parameters']['gamma_u']['ci95'][0]:.4f}, {d['Law1']['parameters']['gamma_u']['ci95'][1]:.4f}]"),
                            ("gamma_u Gaussian 95% (mean+/-1.96*std) includes 0", lambda d: (d["Law1"]["parameters"]["gamma_u"]["mean"] - 1.96 * d["Law1"]["parameters"]["gamma_u"]["std"]) <= 0.0, lambda d: f"z={d['verdicts_and_stats']['T1_Sign']['Law1_z_gamma_u_gt_0']:.2f}"),
                        ]
                    elif t_id == "C2":
                        checks = [
                            ("T2-A PASS (T2A_CPL)", lambda d: d["verdicts_and_stats"]["T2_A"]["per_run_verdict"] == "PASS", lambda d: d["verdicts_and_stats"]["T2_A"]["per_run_verdict"]),
                            ("T2-A PASS (Law1 chain)", lambda d: d["verdicts_and_stats"]["T2_A"]["from_Law1_chain"]["per_run_verdict"] == "PASS", lambda d: d["verdicts_and_stats"]["T2_A"]["from_Law1_chain"]["per_run_verdict"]),
                            ("T1-Sign PASS (CPL P(w0>-1)>=0.95)", lambda d: d["verdicts_and_stats"]["T1_Sign"]["verdict"] == "PASS", lambda d: f"{d['verdicts_and_stats']['T1_Sign']['verdict']} (P={d['verdicts_and_stats']['T1_Sign']['P_w0_gt_minus1_mcmc']:.4f})"),
                            ("T1-Sign PASS (Law1 z_gamma_u>=2.5)", lambda d: d["verdicts_and_stats"]["T1_Sign"]["Law1_z_gamma_u_gt_0"] >= 2.5, lambda d: f"z={d['verdicts_and_stats']['T1_Sign']['Law1_z_gamma_u_gt_0']:.2f}"),
                            ("T1-L1 not FAIL", lambda d: d["verdicts_and_stats"]["T1_L1"]["verdict"] != "FAIL", lambda d: d["verdicts_and_stats"]["T1_L1"]["verdict"]),
                        ]
                    else:  # C3
                        checks = [
                            ("T1-L1 FAIL", lambda d: d["verdicts_and_stats"]["T1_L1"]["verdict"] == "FAIL", lambda d: d["verdicts_and_stats"]["T1_L1"]["verdict"]),
                            ("T1-Sign PASS", lambda d: d["verdicts_and_stats"]["T1_Sign"]["verdict"] == "PASS", lambda d: d["verdicts_and_stats"]["T1_Sign"]["verdict"]),
                            ("T2-A FAIL (T2A_CPL)", lambda d: d["verdicts_and_stats"]["T2_A"]["per_run_verdict"] == "FAIL", lambda d: d["verdicts_and_stats"]["T2_A"]["per_run_verdict"]),
                            ("T2-A FAIL (Law1 chain)", lambda d: d["verdicts_and_stats"]["T2_A"]["from_Law1_chain"]["per_run_verdict"] == "FAIL", lambda d: d["verdicts_and_stats"]["T2_A"]["from_Law1_chain"]["per_run_verdict"]),
                        ]
                    for cname, pred_fn, val_fn in checks:
                        vals = []
                        matches = 0
                        for u in us:
                            d = res["universes"][u["universe_id"]][reading][sn]
                            ok = pred_fn(d)
                            if ok:
                                matches += 1
                            vals.append(val_fn(d))
                        cosmo_rows.append({
                            "truth": t_id,
                            "reading": reading,
                            "sn_set": sn,
                            "criterion": cname,
                            "realizations": vals,
                            "matches": matches,
                            "verdict": "PASS" if matches >= 4 else "MISS",
                        })

    gal_rows: list[dict[str, Any]] = []
    for t_id in ["G1", "G2", "G3"]:
        us = u_by_truth[t_id]
        exp_v = "PASS" if t_id in ("G1", "G2") else "FAIL"
        vals = []
        matches = 0
        test_medians = []
        train_medians = []
        for u in us:
            t5a = res["universes"][u["universe_id"]]["T5_A"]
            v = t5a["verdict"]
            vals.append(v)
            if v == exp_v:
                matches += 1
            test_medians.append(t5a["test_median_chi2_red"])
            train_medians.append(t5a["training_fit"]["train_summary"]["median_chi2_red"])
        gal_rows.append({
            "truth": t_id,
            "criterion": f"T5-A {exp_v}",
            "realizations": vals,
            "matches": matches,
            "verdict": "PASS" if matches >= 4 else "MISS",
            "test_median_chi2_red": test_medians,
            "train_median_chi2_red": train_medians,
        })

    reg_rows: list[dict[str, Any]] = []
    for t_id in ["H1", "H2", "H3"]:
        us = u_by_truth[t_id]
        vals = [res["universes"][u["universe_id"]]["T6"]["verdict"] for u in us]
        chi2s = [res["universes"][u["universe_id"]]["T6"]["chi2_het"] for u in us]
        p_hets = [res["universes"][u["universe_id"]]["T6"]["p_het"] for u in us]
        z_bars = [res["universes"][u["universe_id"]]["T6"]["Z_all_sky_vs_Planck"] for u in us]
        if t_id == "H1":
            m_strict = sum(1 for v in vals if v == "FAIL")
            m_not_pass = sum(1 for v in vals if v != "PASS")
            reg_rows.append({
                "truth": "H1",
                "criterion": "T6 FAIL (strict: p_het > 0.3173)",
                "realizations": vals,
                "matches": m_strict,
                "verdict": "PASS" if m_strict >= 4 else "MISS",
                "chi2_het": chi2s,
                "p_het": p_hets,
            })
            reg_rows.append({
                "truth": "H1",
                "criterion": "T6 no variation detected (not PASS: p_het > 0.0027)",
                "realizations": vals,
                "matches": m_not_pass,
                "verdict": "PASS" if m_not_pass >= 4 else "MISS",
                "chi2_het": chi2s,
                "p_het": p_hets,
            })
        elif t_id == "H3":
            m_strict = sum(1 for v in vals if v == "PASS")
            m_phet = sum(1 for p in p_hets if p <= 0.0027)
            reg_rows.append({
                "truth": "H3",
                "criterion": "T6 PASS (registered rule: p_het <= 0.0027 & Z_all_sky >= 3)",
                "realizations": vals,
                "matches": m_strict,
                "verdict": "PASS" if m_strict >= 4 else "MISS",
                "chi2_het": chi2s,
                "p_het": p_hets,
                "z_bars": z_bars,
            })
            reg_rows.append({
                "truth": "H3",
                "criterion": "T6 heterogeneity only (p_het <= 0.0027)",
                "realizations": [f"p={p:.4g}" for p in p_hets],
                "matches": m_phet,
                "verdict": "PASS" if m_phet >= 4 else "MISS",
                "chi2_het": chi2s,
                "p_het": p_hets,
            })
        elif t_id == "H2":
            m_det = sum(1 for v in vals if v == "PASS")
            reg_rows.append({
                "truth": "H2",
                "criterion": "T6 detection rate (diagnostic, not pass/fail)",
                "realizations": vals,
                "matches": m_det,
                "detection_rate": f"{m_det}/5 ({m_det * 20}%)",
                "verdict": "DIAGNOSTIC (80% detection)",
                "chi2_het": chi2s,
                "p_het": p_hets,
            })

    return {"cosmo": cosmo_rows, "galaxy": gal_rows, "regional": reg_rows}


def audit_step3(ak: dict[str, Any], res: dict[str, Any]) -> dict[str, Any]:
    u_by_truth: dict[str, list[dict[str, Any]]] = {}
    for u in ak["universes"]:
        u_by_truth.setdefault(u["truth"], []).append(u)

    cosmo_us = [u for t in ["C1", "C2", "C3"] for u in u_by_truth[t]]
    # 1. Reading B vs Reading A deterministic shifts across 15 COSMO universes
    shifts: dict[str, list[float]] = {
        "T2A_CPL_Omega_bc": [],
        "T2A_CPL_h": [],
        "T2A_CPL_100_omega_b": [],
        "T2_A_signed_z": [],
    }
    for u in cosmo_us:
        uid = u["universe_id"]
        for sn in ["PantheonPlus", "DES_Dovekie"]:
            rb = res["universes"][uid]["Reading_B"][sn]
            ra = res["universes"][uid]["Reading_A"][sn]
            shifts["T2A_CPL_Omega_bc"].append(rb["T2A_CPL"]["parameters"]["Omega_bc"]["mean"] - ra["T2A_CPL"]["parameters"]["Omega_bc"]["mean"])
            shifts["T2A_CPL_h"].append(rb["T2A_CPL"]["parameters"]["h"]["mean"] - ra["T2A_CPL"]["parameters"]["h"]["mean"])
            shifts["T2A_CPL_100_omega_b"].append(rb["T2A_CPL"]["parameters"]["100_omega_b"]["mean"] - ra["T2A_CPL"]["parameters"]["100_omega_b"]["mean"])
            shifts["T2_A_signed_z"].append(rb["verdicts_and_stats"]["T2_A"]["signed_tension_sigma"] - ra["verdicts_and_stats"]["T2_A"]["signed_tension_sigma"])

    # 2. REGIONAL GLS linear-H0 bias vs SN-count-weighted mean
    gls_shifts: dict[str, list[float]] = {}
    for t_id in ["H1", "H2", "H3"]:
        diffs = []
        for u in u_by_truth[t_id]:
            uid = u["universe_id"]
            t6 = res["universes"][uid]["T6"]
            counts = u["region_counts_HF"]
            rec_map = {x["pixel_ring_id"]: x["H0_kms_Mpc"] for x in t6["regional_H0"]}
            count_wt = sum(rec_map[int(k)] * counts[k] for k in counts) / sum(counts.values())
            diffs.append(t6["H0_bar_kms_Mpc"] - count_wt)
        gls_shifts[t_id] = diffs

    return {
        "reading_B_minus_A_mean_shifts": {k: statistics.mean(v) for k, v in shifts.items()},
        "gls_minus_count_wt_H0_bar": {k: {"per_u": v, "mean": statistics.mean(v)} for k, v in gls_shifts.items()},
    }


def main() -> None:
    ok, int_rows = verify_integrity()
    print("=== STEP 1: INTEGRITY ===")
    for r in int_rows:
        print(f"{r['file']:34s} | {r['sha256']} | {r['status']} | inj={r['inj_paths']} res={r['res_paths']}")
    if not ok:
        print("INTEGRITY FAILURE!")
        return

    ak = json.load((WORKSPACE / "ANSWER_KEY.json").open("r", encoding="utf-8"))
    res = json.load((WORKSPACE / "results.json").open("r", encoding="utf-8"))

    cosmo_s1 = score_cosmo_s1(ak, res)
    gal_s1 = score_galaxy_s1(ak, res)
    reg_s1 = score_regional_s1(ak, res)
    s2 = score_s2(ak, res)
    step3 = audit_step3(ak, res)

    print(f"\nComputed {len(cosmo_s1)} COSMO S1 rows, {len(gal_s1)} GALAXY S1 rows, {len(reg_s1['summary'])} REGIONAL S1 summary rows.")
    print("=== S1 COSMO ===")
    for r in cosmo_s1:
        print(
            f"S1 COSMO {r['truth']} | {r['reading']:9s} | {r['sn_set']:12s} | {r['model']:7s} | {r['param']:11s} | "
            f"true={r['truth_val']:+.6f} | mean={r['mean_rec']:+.6f} | bias={r['signed_bias']:+.6f} | "
            f"sig={r['mean_sigma']:.6f} | |b|/s={r['bias_over_sigma']:.3f} | ci95={r['n_in_ci95']}/5 -> {r['verdict_primary']:4s} | "
            f"sym95={r['n_in_sym95']}/5 -> {r['verdict_sym95']:4s} | med_ci95={r['verdict_med_ci95']:4s} | emp/sig={r['emp_over_post_sig']:.2f}"
        )
    print("\n=== S1 GALAXY ===")
    for r in gal_s1:
        print(
            f"S1 GALAXY {r['truth']} | {r['method']:25s} | true={r['truth_val']:.4f} | mean={r['mean_rec']:.4f} | "
            f"bias_mean={r['signed_bias_mean']:+.4f} | bias_pt={r['signed_bias_pt']:+.4f} | sig={r['mean_sigma']:.4f} | "
            f"|b|/s={r['bias_over_sigma']:.3f} | ci95={r['n_in_ci95']}/5 -> {r['verdict']} | emp_sd={r['emp_sd_pt']:.4f} ({r['emp_over_sig']:.2f}x)"
        )
    print("\n=== S1 REGIONAL SUMMARY ===")
    for r in reg_s1["summary"]:
        print(
            f"S1 REGIONAL {r['truth']} | {r['mode']:16s} | reg_pass={r['regions_passing_s1']}/9 ({r['verdict_all9_regions']}) | "
            f"pooled={r['pooled_in_95']}/45 ({r['pooled_pct']:.1f}%, {r['verdict_pooled']}) | u_in={r['u_in_counts']} | "
            f"gm_bias={r['grand_mean_bias']:+.4f} | mean|b|_reg={r['mean_abs_reg_bias']:.4f} | gm_sig={r['grand_mean_sigma']:.4f}"
        )
    print("\n=== S1 REGIONAL ALL-SKY H0_BAR ===")
    for r in reg_s1["all_sky_bar"]:
        print(
            f"S1 H0_BAR {r['truth']} | {r['mode']:14s} | in95={r['n_in_95']}/5 | bias={r['signed_bias']:+.4f} | "
            f"sig={r['mean_sigma']:.4f} | |b|/s={r['bias_over_sigma']:.3f} -> {r['verdict']}"
        )
    print(f"\nComputed {len(s2['cosmo'])} COSMO S2 rows, {len(s2['galaxy'])} GALAXY S2 rows, {len(s2['regional'])} REGIONAL S2 rows.")
    for r in s2["cosmo"]:
        print(f"S2 COSMO {r['truth']} | {r['reading']:9s} | {r['sn_set']:12s} | {r['criterion']:48s} | {r['matches']}/5 -> {r['verdict']} | {r['realizations']}")
    for r in s2["galaxy"]:
        print(f"S2 GALAXY {r['truth']} | {r['criterion']} | {r['realizations']} | {r['matches']}/5 -> {r['verdict']} | test_med={r['test_median_chi2_red']} | train_med={r['train_median_chi2_red']}")
    for r in s2["regional"]:
        print(f"S2 REGIONAL {r['truth']} | {r['criterion']} | {r['realizations']} | {r['matches']}/5 -> {r['verdict']}")
    print("\n=== STEP 3 DIAGNOSTICS ===")
    print("Reading B minus Reading A mean shifts (across 30 COSMO runs):", step3["reading_B_minus_A_mean_shifts"])
    for k, v in step3["gls_minus_count_wt_H0_bar"].items():
        print(f"GLS H0_bar minus SN-count-weighted mean ({k}): mean={v['mean']:+.4f} km/s/Mpc, per_u={[round(x, 4) for x in v['per_u']]}")


if __name__ == "__main__":
    main()
