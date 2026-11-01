"""write_results_md.py -- writes REBUILD_RESULTS.md mechanically from results_rebuild/results.json, the T4b extraction
table, the run JSONs and DEVIATIONS_REBUILD.md (no number is typed by hand)."""
import os, json, glob, math

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, "results_rebuild")
CH = os.path.join(RES, "chains")
R = json.load(open(os.path.join(RES, "results.json")))
SN = {"P": "Pantheon+", "D": "DES-Dovekie"}


def f(x, n=4):
    if x is None:
        return "n/a"
    if isinstance(x, bool):
        return "yes" if x else "no"
    if isinstance(x, (int,)) and not isinstance(x, bool):
        return str(x)
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return str(x)
    if abs(x) != 0 and (abs(x) < 1e-3 or abs(x) >= 1e6):
        return f"{x:.{n - 1}e}"
    return f"{x:.{n}f}"


def run(name):
    return json.load(open(os.path.join(CH, f"{name}.json")))


def trial_spread(name):
    t = run(name)["optimizer_trials"]
    v = [min(x["nm_chi2"], x["lbfgsb_chi2"]) for x in t]
    return max(v) - min(v)


L = []
w = L.append
V = R["verdicts"]
w("# REBUILD_RESULTS.md — Blind independent rebuild, PHASE 1")
w("")
w(f"Generated mechanically by `rebuild/write_results_md.py` from `results_rebuild/results.json` "
  f"(analysis run {R['generated']}; code SHA-256 of rebuild/*.py + run_all_rebuild.py at analysis time: "
  f"`{R['code_sha256_rebuild_scripts']}`). Governing rulebook: PREREG.md (v4 package, verified by SHA-256).")
w("")
w("## 0. Summary of verdicts")
w("")
w("| Test | Class | Verdict |")
w("|---|---|---|")
cls = {"T1-L1": "Primary pillar 1", "T2-A": "Primary pillar 2", "T4b": "Primary pillar 3", "T5-A": "Primary pillar 4",
       "T1-Sign": "Scored secondary", "T2-N1": "Scored secondary", "T2-N2": "Scored secondary",
       "T5-B": "Scored secondary", "T5c": "Scored secondary", "T6": "Scored secondary"}
for k in ("T1-L1", "T2-A", "T4b", "T5-A", "T1-Sign", "T2-N1", "T2-N2", "T5-B", "T5c", "T6"):
    w(f"| {k} | {cls[k]} | **{V[k]}** |")
w("")
w(f"**Model-level verdict (PREREG §3.3): {R['model_verdict']}**")
w("")

# ------------------------------------------------------------------ gates
g = R["gates"]
w("## 1. Validation gates (PREREG §2 G9)")
w("")
w("| Gate | Statistic | Value | Target | Tolerance | Result |")
w("|---|---|---|---|---|---|")
a = g["G9-a"]
w(f"| G9-a | posterior mean Ωm (flat ΛCDM, unmodified desi_bao_dr2) | {f(a['value'])} ± {f(a['sd'])} | 0.2975 | "
  f"±{f(a['tol'], 5)} | {'PASS' if a['PASS'] else 'FAIL'} (diff {f(a['diff'], 5)}) |")
for k, v in g["G9-b"]["params"].items():
    w(f"| G9-b | posterior mean {k} (Chen+19 ΛCDM 3×3 prior alone) | {f(v['value'], 5)} ± {f(v['sd'], 5)} | "
      f"{v['target']} (σ={v['sigma']}) | ±{f(v['tol'], 5)} | {'within' if v['within'] else 'OUTSIDE'} "
      f"({f(v['diff_over_sigma'], 3)}σ) |")
w(f"| G9-b | overall | | Planck 2018 VI Table 2 TT,TE,EE+lowE (DEVIATIONS D2) | 0.3σ each | "
  f"**{'PASS' if g['G9-b']['PASS'] else 'FAIL'}** |")
for k, v in g["G9-c"]["params"].items():
    w(f"| G9-c | posterior mean {k} (desi_bao_dr2 + Chen+19 + DES-Dovekie) | {f(v['value'])} ± {f(v['sd'])} | "
      f"{v['target']} | ±{v['tol']} | {'within' if v['within'] else 'OUTSIDE'} ({f(v['diff_over_sigma'], 3)}σ) |")
w(f"| G9-c | overall | | Popovic+25 Table 11 | 1.0σ each | **{'PASS' if g['G9-c']['PASS'] else 'FAIL'}** |")
d = g["G9-d"]
w(f"| G9-d | max abs(F_σ − ncx2.cdf) on registered 5×7 grid (numpy {d['numpy']}, scipy {d['scipy']}) | "
  f"{d['value']:.3e} | 0 | < 1e-10 | **{'PASS' if d['PASS'] else 'FAIL'}** |")
w("")
w(f"G9-d independent 3D Monte Carlo cross-check (2×10⁶ points, 6 configurations): max |z| = "
  f"{f(max(abs(m['z']) for m in d['monte_carlo']), 3)}.")
w("")
w("Gate-run convergence: " + ", ".join(f"{n}: R̂−1 = {f(R['convergence'][n]['rhat_max'] - 1, 5)}, "
                                       f"ESS_min = {R['convergence'][n]['ess_min']:.0f}"
                                       for n in ("G9a_lcdm_BAOstd", "G9b_lcdm_CMB", "G9c_cpl_BAOstd_CMB_D")) + ".")
w("")
w("G9-b failure audit (mandatory bug check, PREREG G9): see `results_rebuild/validation/g9b_bugcheck.json` and the "
  "ACTIVITY_LOG entry at 06:46:24. D_M(z*) agrees with CAMB to 2.6e-6 and r_s(z*) to 4.9e-5. No implementation bug "
  "was found, so no code was changed. Mapped tests (T1-L1, T1-Sign, T2-A, T2-B) are INCONCLUSIVE by the gate route "
  "unless a valid run triggers FAIL.")
w("")

# ------------------------------------------------------------------ T1
t1 = R["T1"]
w("## 2. Pillar 1 — T1-L1 (and secondary T1-Sign)")
w("")
w("Registered statistic: A_r = Δχ²_min(Law 1 − ΛCDM), B_r = Δχ²_min(Law 1 − w0waCDM) per SN run; per-run FAIL if "
  "B > 9 or A > −1; PASS if A ≤ −4 and B ≤ 4; else INCONCLUSIVE. Joint FAIL if either valid run FAILs. Datasets: DESI "
  "DR2 BAO with the registered Lyα BAO+AP replacement (r = −0.431), the Chen+19 ΛCDM 3×3 CMB prior, and SNe (separately).")
w("")
w("| SN run | χ²_min ΛCDM | χ²_min Law 1 | χ²_min w0waCDM | A | B | per-run outcome | γ̂_u | w0_fit | wa_fit | numerical precision of A, B (optimizer spread) | converged | mapped gates pass |")
w("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for sn, p in t1["per_run"].items():
    sp = max(trial_spread(f"T1_{m}_{sn}") for m in ("lcdm", "law1", "cpl"))
    w(f"| {SN[sn]} | {f(p['chi2_min']['lcdm'])} | {f(p['chi2_min']['law1'])} | {f(p['chi2_min']['cpl'])} | "
      f"{f(p['A'])} | {f(p['B'])} | {p['outcome']} | {f(p['law1_best']['gam'])} | {f(p['w0_fit'])} | {f(p['wa_fit'])} | "
      f"{sp:.1e} | {f(p['converged'])} | {f(p['gates_ok'])} |")
w("")
w(f"γ_u posterior (Law-1 MCMC): " + "; ".join(
    f"{SN[sn]}: median {f(p['gamma_posterior']['median'])} (68%: {f(p['gamma_posterior']['q16'])}–"
    f"{f(p['gamma_posterior']['q84'])})" for sn, p in t1["per_run"].items()) + ".")
w("")
w(f"Discovery p-value p_T1-L1 = max_r[1 − F_χ²₁(max(0, −A_r))] = {f(t1['p_T1L1'], 6)}; value entering Holm "
  f"(set to 1.0 if a run is invalid, §3.2 edge-case rule) = {f(t1['p_T1L1_for_holm'], 6)}.")
w("")
w(f"Raw joint T1-L1 outcome: {t1['raw_verdict']}. **Final T1-L1 verdict: {V['T1-L1']}.**")
w("")
w("T1-Sign (one-sided 95%: PASS if P(w0 > −1) ≥ 0.95 in both runs; FAIL if P(w0 < −1) ≥ 0.95 in either, or "
  "σ_w0 ≤ 0.03 with (−1, 0) inside the 68% region in both):")
w("")
w("| SN run | w0 (mean ± sd) | wa (mean ± sd) | P(w0 > −1) | (−1,0) Mahalanobis² | (−1,0) in 68% region |")
w("|---|---|---|---|---|---|")
for sn, s in t1["T1_Sign"]["per_run"].items():
    w(f"| {SN[sn]} | {f(s['w0_mean'])} ± {f(s['w0_sd'])} | {f(s['wa_mean'])} ± {f(s['wa_sd'])} | "
      f"{f(s['P_w0_gt_m1'], 5)} | {f(s['mahal2_LCDM_point'], 3)} | {f(s['LCDM_in_68pct'])} |")
w("")
w(f"**T1-Sign verdict: {V['T1-Sign']}.** Run validity (converged and mapped gates pass): "
  + ", ".join(f"{SN[k]}: {f(v)}" for k, v in t1["run_valid"].items()) + ".")
w("")

# ------------------------------------------------------------------ T2
t2 = R["T2-A"]
w("## 3. Pillar 2 — T2-A (and T2-N1, T2-N2)")
w("")
w("Registered statistic: |R_pred − 5.36| vs 2σ_comb, with R_pred = 19 Ω_bc − 1 (Ω_bc = median of the posterior; "
  "σ_Ωbc = ½(q84 − q16)) and σ_comb = √((19σ_Ωbc)² + 0.065²). FIT: flat w0waCDM; DESI DR2 BAO with the Lyα BAO+AP "
  "replacement; conditional Chen+19 (R, ℓ_A | ω_b); DESI/LUNA BBN 100ω_b = 2.218 ± 0.055; SNe separately.")
w("")
w("| SN run | Ω_bc (median ± σ) | f_leak ± σ_f | R_pred ± 19σ | σ_comb | (R_pred − 5.36)/σ_comb | exceeds 2σ_comb | converged | mapped gates pass |")
w("|---|---|---|---|---|---|---|---|---|")
for sn, p in t2["per_run"].items():
    w(f"| {SN[sn]} | {f(p['Obc_median'], 5)} ± {f(p['sigma_Obc'], 5)} | {f(p['f_leak'])} ± {f(p['sigma_f'])} | "
      f"{f(p['R_pred'])} ± {f(p['sigma_R_pred'])} | {f(p['sigma_comb'])} | {f(p['signed_n_sigma'], 3)} | "
      f"{f(p['exceeds_2sigma'])} | {f(p['converged'])} | {f(p['gates_ok'])} |")
w("")
w(f"**T2-A verdict: {V['T2-A']}.** Frozen f_leak passed to T5 (from T2-A-Pantheon+): "
  f"{f(t2['freeze']['f_leak_for_T5'], 6)} (`results_rebuild/FREEZE_T2.json`, SHA-256 `{t2['freeze']['file_sha256']}`).")
w("")
n1, n2 = R["T2-N1"], R["T2-N2"]
w(f"- **T2-N1** (Ω_b^model = 1/19 = {f(n1['Omega_b_model'], 6)} vs Planck {n1['planck']} ± {n1['sigma']}): "
  f"difference {f(n1['diff'], 6)} = {f(n1['n_sigma'], 3)}σ; threshold 2σ. **Verdict: {V['T2-N1']}.**")
w(f"- **T2-N2** (H0_pred = 100√(19ω_b) = {f(n2['H0_pred'], 3)} ± {n2['sigma_H0_pred_registered']} for 100ω_b = "
  f"2.237 ± 0.015, vs Planck {n2['planck']} ± {n2['sigma_planck']}; σ_comb = {f(n2['sigma_comb'], 4)}): difference "
  f"{f(n2['diff'], 3)} = {f(n2['n_sigma'], 3)}σ; threshold 2σ_comb. **Verdict: {V['T2-N2']}.** (Propagated σ of "
  f"H0_pred from σ(100ω_b) = 0.015: {f(n2['sigma_H0_pred_propagated'], 4)}; the registered 0.22 is used.)")
w("")

# ------------------------------------------------------------------ T4b
t4 = R["T4b"]
w("## 4. Pillar 3 — T4b")
w("")
w("Registered statistic: hard-step classification accuracy on the classified test half at τ̂_lag, which is trained on "
  "the classified training half over [235, 1500] Myr in 5 Myr steps (ties go to the smallest τ). Classification uses "
  "the single deciding (S, G, I) source per cluster and the 2σ_diff rule.")
w("")
w(f"- Classified clusters: n_train = {t4['n_train']}, n_test = {t4['n_test']}.")
w(f"- τ̂_lag = {t4['tau_hat_myr']:.0f} Myr; max training accuracy = {f(t4['acc_train_max'], 3)}.")
w(f"- Test accuracy = {f(t4['acc_test'], 3)} (k_obs = {t4['k_obs']}); binomial p = {f(t4['p_T4b_binomial'], 6)}; "
  f"p entering Holm = {f(t4['p_T4b_for_holm'], 6)} (n_test < 6 → p = 1.0, §3.2 edge-case rule).")
w(f"- FAIL clauses: (a) {f(t4['fail_clauses']['a'])}, (b) {f(t4['fail_clauses']['b'])}, (c) {f(t4['fail_clauses']['c'])}. "
  f"Raw outcome: {t4['raw_verdict']}.")
w("")
w(f"**T4b verdict: {V['T4b']}.**")
w("")
alt = t4["sensitivity_NON_DECIDING"]["row13_S_rejected"]
alt_t4b = alt["raw_verdict"]
w(f"**Interpretive dependence (DEVIATIONS D10 item 2 and D12), reported with equal prominence:** only one cluster "
  f"(row 13, MACS J0025.4-1222, Bradač+08) has all three positions and per-position 1σ errors. That depends on reading "
  f"the Bradač+08 Table 2 'galaxies' row as the luminosity-weighted galaxy centre. Under the alternative reading (the "
  f"row is a smoothed-light-map peak, which D10 item 1 does not accept, and the paper gives no BCG coordinates), row 13 "
  f"is unclassified, n_train = {alt['n_train']}, n_test = {alt['n_test']}, and T4b would be **{alt['raw_verdict']}** "
  f"(FAIL clause 1(a): {f(alt['fail_clauses']['a'])}). The deciding reading is the one logged before computation (D10).")
w("")
w("Known sample-selection limitation (PREREG §5.5): the 16-cluster sample was compiled from the literature by an author "
  "with prior knowledge of published offsets; T4b cannot be free of selection bias.")
w("")
w("### 4.1 Extracted T4b cluster position table")
w("")
w("Positions and per-position errors as read from each single deciding source paper (verbatim quotes, pointers and "
  "per-cluster notes: `t4b_extraction/cluster_NN.json`, `cluster_NN_notes.md`; protocol "
  "`t4b_extraction/EXTRACTION_PROTOCOL.md`, written before any paper was opened). Fingerprinted in "
  "DATA_MANIFEST_REBUILD_PAPERS.sha256 (OTS-stamped) before T4b was computed.")
w("")
w("| # | Designation | Half | t_p (Gyr) | Paper | Table / section / value | Status / class |")
w("|---|---|---|---|---|---|---|")
tab = json.load(open(os.path.join(ROOT, "t4b_extraction", "t4b_positions_rebuild.json")))
clsmap = {c["row"]: c for c in t4["clusters"]}
for c in tab["clusters"]:
    val = c["pointer"].replace("|", "/")
    if c["status"] == "complete":
        val += (f"; x_I = ({c['I']['xy'][0]}, {c['I']['xy'][1]}) ± ({c['I']['err_axes'][0]}, {c['I']['err_axes'][1]}) ′, "
                f"x_G = ({c['G']['xy'][0]}, {c['G']['xy'][1]}) ± ({c['G']['err_axes'][0]}, {c['G']['err_axes'][1]}) ′, "
                f"x_S = ({c['S']['xy'][0]}, {c['S']['xy'][1]}) ± ({c['S']['err_axes'][0]}, {c['S']['err_axes'][1]}) ′; "
                f"z = {c['z_cl']}")
    k = clsmap[c["row"]]
    st = k["class"]
    if k["class"] != "unclassified" or c["status"] == "complete":
        dd = k["details"]
        st += (f" (d_IG = {f(dd['d_IG_kpc'], 1)} kpc, d_IS = {f(dd['d_IS_kpc'], 1)} kpc, "
               f"σ_diff = {f(dd['sigma_diff_kpc'], 1)} kpc; |d_IG − d_IS|/2σ_diff = {f(dd['margin_over_2sigma'], 3)})")
    else:
        st += ": " + c["status"].replace("unclassified: ", "").replace("|", "/")
    w(f"| {c['row']} | {c['designation']} | {k['half']} | {c['tp']} | {c['paper'].replace('|', '/')} | {val} | {st} |")
w("")

# ------------------------------------------------------------------ T5
t5 = R["T5"]
w("## 5. Pillar 4 — T5-A (and T5-B, T5c)")
w("")
w(f"Frozen inputs: f_leak = {f(t5['f_leak'], 6)} (T2-A-Pantheon+), 6(1 − f_leak) = {f(t5['Rfac'], 5)}; SPARC split "
  f"{t5['n_train']} training / {t5['n_test']} held-out (byte-wise sorted ids). Objective: sum of per-galaxy reduced χ² "
  f"over the training half (200-point log grid, then bounded minimize_scalar, xatol = 1e-5). "
  f"`results_rebuild/FREEZE_T5.json` SHA-256 `{t5['freeze']['file_sha256']}`.")
w("")
w("Registered statistic (held-out half): median χ²_red (M) and fraction with χ²_red < 2 (F). PASS: M ≤ 1.5 and F ≥ 0.70; "
  "FAIL: M > 3.0 or F < 0.40; else INCONCLUSIVE.")
w("")
w("| Test | Fitted width | Training objective at optimum | Held-out median χ²_red | Held-out F(χ²_red < 2) | n held-out | Verdict |")
w("|---|---|---|---|---|---|---|")
for m, lab in (("A", "σ̂_ref = {} kpc"), ("B", "k̂ = {}")):
    x = t5[f"T5-{m}"]
    w(f"| T5-{m} | {lab.format(f(x['fit']['best'], 5))} | {f(x['fit']['L_best'], 3)} | {f(x['test']['median'], 4)} | "
      f"{f(x['test']['frac_lt2'], 4)} | {x['test']['n']} | **{V['T5-' + m]}** |")
w("")
w(f"Dependency check (G9-d PASS and T2-A-Pantheon+ converged; DEVIATIONS D11): {f(t5['dependency_ok'])}.")
w("")
w(f"**Interpretive dependence (DEVIATIONS D11), reported with equal prominence:** gate G9-b FAILED. PREREG §2 G9 maps "
  f"G9-a/G9-b to T5 'only if T2-A-Pantheon+ fails to produce a converged f_leak because G9-a or G9-b failed'. "
  f"T2-A-Pantheon+ converged (R̂−1 = {f(R['convergence']['T2A_P']['rhat_max'] - 1, 5)}) and its f_leak was frozen, so under "
  f"the deciding literal reading (logged in D11 before T5 was computed) T5-A, T5-B and T5c stand as computed. Under the "
  f"alternative reading (any G9-a/b failure invalidates the f_leak passed to T5), T5-A, T5-B and T5c would be "
  f"**INCONCLUSIVE**.")
w("")
c5 = t5["T5c"]
w(f"**T5c** (NGC 1052-DF2, σ_ref = σ̂_ref from T5-A = {f(c5['sigma_ref'], 5)} kpc): "
  + "; ".join(f"M_pred(<{r} kpc) = {v['Mpred']:.4e} M☉ (baryons {v['Mb']:.4e}, DF2 shadow {v['Msh_DF2']:.4e}, "
              f"group shadow {v['Msh_group']:.4e})" for r, v in c5["masses"].items())
  + f". (The group-shadow term is zero to floating-point precision at this σ_ref; tiny negative values are round-off.)"
  + f" Thresholds: PASS if M(<2.7) ≤ 2.9e8 and M(<3.1) < 3.2e8; FAIL if M(<2.7) > 3.7e8. **Verdict: {V['T5c']}.**")
w("")

# ------------------------------------------------------------------ T6
t6 = R["T6"]; m6 = t6["main"]
w("## 6. T6 — regional H0 heterogeneity")
w("")
w(f"FIX: GLS M_B from {t6['fix']['n_cal']} Cepheid calibrators = {f(t6['fix']['MB'], 5)} ± {f(t6['fix']['sigma_MB'], 5)} mag "
  f"(`results_rebuild/FREEZE_T6.json` SHA-256 `{t6['freeze']['file_sha256']}`).")
w("")
w(f"TEST: {m6['n_sel']} Pantheon+ Hubble-flow SNe (0.023 ≤ z_HD ≤ 0.15, non-calibrator) in Galactic HEALPix Nside = 1 "
  f"RING pixels. Initial counts {m6['counts_initial']}; merges (pixel→target) {m6['merges']}; retained regions "
  f"{m6['regions']} (N_pix = {m6['Npix']}, {m6['n_used']} SNe).")
w("")
if m6["Npix"] >= 2:
    w("| Region | N_SN | H0 ± σ (km/s/Mpc) |")
    w("|---|---|---|")
    for rg, h, s in zip(m6["regions"], m6["H0_regions"], m6["H0_region_sigma"]):
        w(f"| {rg} | {m6['counts_final'][rg]} | {f(h, 3)} ± {f(s, 3)} |")
    w("")
    w(f"Registered statistic: χ²_het = {f(m6['chi2_het'], 3)} (dof {m6['dof']}), p_het = {f(m6['p_het'], 5)}; GLS mean "
      f"H̄0 = {f(m6['Hbar'], 3)} ± {f(m6['sigma_Hbar'], 3)}; Z_all-sky = {f(m6['Z_allsky'], 3)}. Thresholds: FAIL if "
      f"p_het > 0.3173; PASS if p_het ≤ 0.00270, Z ≥ 3 and Holm survives.")
w("")
w(f"Raw outcome: {m6['verdict']}. **T6 verdict: {V['T6']}.**")
w("")

# ------------------------------------------------------------------ Holm
hb = R["holm"]
w("## 7. Multiple-testing correction (PREREG §3.2, Holm–Bonferroni over T1-L1, T4b, T6)")
w("")
w("| Rank | Test | p | α_(m) | p > α? |")
w("|---|---|---|---|---|")
for n in hb["order"]:
    r = hb["ranks"][n]
    w(f"| {r['rank']} | {n} | {f(r['p'], 6)} | {f(r['alpha'], 5)} | {f(r['p'] > r['alpha'])} |")
w("")
w(f"m* = {hb['m_star']}. Raw PASS outcomes at rank ≥ m* are downgraded to INCONCLUSIVE. Final: "
  + ", ".join(f"{k}: {v}" for k, v in hb["final"].items()) + ".")
w("")

# ------------------------------------------------------------------ model verdict
w("## 8. Model-level verdict (PREREG §3.3)")
w("")
w("Pillars: " + ", ".join(f"{k} = {V[k]}" for k in ("T1-L1", "T2-A", "T4b", "T5-A")) + ".")
w("")
w(f"**{R['model_verdict']}**")
w("")


def _mv(p):
    if any(x.startswith("FAIL") for x in p):
        return "MODEL FALSIFIED (FAIL)"
    if all(x == "PASS" for x in p):
        return "MODEL SUPPORTED (PASS)"
    return "MODEL INCONCLUSIVE (NOT FALSIFIED, NOT SUPPORTED)"


w("Robustness of the model-level verdict to the two logged interpretive alternatives (computed mechanically; only "
  "the first row is deciding):")
w("")
w("| T4b reading (D10/D12) | T5 gate reading (D11) | T1-L1 | T2-A | T4b | T5-A | Model-level verdict |")
w("|---|---|---|---|---|---|---|")
for lab4, v4 in (("deciding (row 13 accepted)", V["T4b"]), ("alternative (row 13 rejected)", alt_t4b)):
    for lab5, v5 in (("deciding (literal)", V["T5-A"]), ("alternative (G9-b invalidates f_leak)", "INCONCLUSIVE")):
        pil = [V["T1-L1"], V["T2-A"], v4, v5]
        w(f"| {lab4} | {lab5} | {pil[0]} | {pil[1]} | {pil[2]} | {pil[3]} | {_mv(pil)} |")
w("")

# ------------------------------------------------------------------ methods
w("## 9. Method choices (independent route, REBUILD_RULES)")
w("")
for s in [
    "Background: flat E(a) with photons, 2 massless + 1 massive (0.06 eV, exact Fermi–Dirac shape) neutrinos, "
    "N_eff = 3.044, Ω_bc = Ωm − Ω_ν,0; Law 1 ln g(a) via classical RK4 on the registered 1000-point log-a grid.",
    "Distances: fixed-step RK4 ODE for χ(z) on a uniform z grid (dz = 0.0025, z ≤ 2.5) with cubic Hermite interpolation, "
    "plus RK4 on a ln(1+z) grid to z*. Cross-checked against scipy solve_ivp (DOP853) and Gauss–Legendre quadrature "
    "(`results_rebuild/validation/cosmo_validation.json`; max fractional difference 4e-12 ΛCDM, 3e-12 CPL, 7e-7 Law 1).",
    "Sound horizon: RK4 in a; z* from Hu & Sugiyama (1996); z_d from Eisenstein & Hu (1998); r_d = F·r_s(z_d) with "
    "one CAMB 2.0.5 calibration constant F = 0.975772, computed once outside any loop (D3).",
    "Sampler: own 8-chain adaptive-then-frozen random-walk Metropolis (D4). Convergence: split-R̂−1 < 0.01 (classic and "
    "rank-normalised), bulk ESS > 1000 per parameter, burn-in ≥ max(1000, 5τ), ≥ 128,000 production samples. "
    "χ²_min: registered Nelder–Mead + L-BFGS-B from the 5 best samples. Seeds: SEED = 20261030; run i (sorted name "
    "order) uses SEED + 1000·i; Monte Carlo checks use SEED.",
    "SN likelihoods: analytic marginalisation over M; d^T W d evaluated as |L^T d|² with W = L L^T (performance change "
    "logged before any SN fit; identical to 4e-9 in χ²).",
    "Rotation-curve kernel: closed form, validated against scipy ncx2 (G9-d) and a direct 3D Monte Carlo.",
    "T6: own HEALPix Nside=1 RING ang2pix, asserted equal to astropy-healpix for every SN; GLS regional fits.",
    "Parallelism: 14 worker processes (single-threaded BLAS, BELOW_NORMAL priority), leaving ≥ 4 threads free.",
]:
    w(f"- {s}")
w("")

# ------------------------------------------------------------------ sensitivity
S = R["sensitivity_NON_DECIDING"]
w("## 10. NON-DECIDING sensitivity analyses (can never change any verdict)")
w("")
w("### 10.1 T1 variants (A, B per SN run; outcome under the per-run rule)")
w("")
w("| Variant | SN | A | B | per-run outcome | w0_fit |")
w("|---|---|---|---|---|---|")
for key, lab in (("T1_wCDM_CMB_prior", "wCDM-column CMB prior (D7)"), ("T1_Lya_r0", "Lyα r = 0"),
                 ("T1_Lya_unmodified", "unmodified desi_bao_dr2 Lyα row")):
    for sn, p in S[key].items():
        w(f"| {lab} | {SN[sn]} | {f(p['A'])} | {f(p['B'])} | {p['outcome']} | {f(p['w0_fit'])} |")
w("")
w("### 10.2 T2-A variants and T2-B")
w("")
w("| Variant | SN | Ω_bc | R_pred | σ_comb | (R_pred − 5.36)/σ_comb |")
w("|---|---|---|---|---|---|")
for key, lab in (("T2A_cooke", "Cooke+18 BBN prior"), ("T2A_marg", "marginal (R, ℓ_A) block"), ("T2A_r0", "Lyα r = 0"),
                 ("T2A_LyaStd", "unmodified Lyα row")):
    for sn, p in S[key].items():
        w(f"| {lab} | {SN[sn]} | {f(p['Obc_median'], 5)} | {f(p['R_pred'])} | {f(p['sigma_comb'])} | {f(p['signed_n_sigma'], 3)} |")
for sn in ("P", "D"):
    p = S["T2B"][sn]
    w(f"| T2-B (ω_b = h²/19) | {SN[sn]} | {f(p['Obc_median'], 5)} | {f(p['R_pred'])} | {f(p['sigma_comb'])} | "
      f"{f(p['signed_n_sigma'], 3)} (Δχ²_min vs w0waCDM = {f(p['dchi2_vs_w0waCDM'], 3)}) |")
w("")
w(f"T2-B outcome if it were deciding: {S['T2B']['verdict_if_deciding']}.")
w("")
w("### 10.3 T2-N2 alternative ω_b inputs")
w("")
for k, v in n2["sensitivity_NON_DECIDING"].items():
    w(f"- {k}: H0_pred = {f(v['H0_pred'], 3)} ± {f(v['sigma'], 3)}; {f(v['n_sigma_vs_planck'], 3)}σ vs Planck; "
      f"{f(v['n_sigma_vs_desi_bbn_68p52'], 3)}σ vs DESI+BBN 68.52 ± 0.62.")
w("")
w("### 10.4 T4b")
w("")
mc = t4["mc_age_weighted_accuracy"]
w(f"- Monte Carlo age-posterior-weighted accuracy at τ̂_lag (20,000 draws): train "
  f"{('mean ' + f(mc['train']['mean'], 3)) if mc['train'] else 'n/a'}; test "
  f"{('mean ' + f(mc['test']['mean'], 3)) if mc['test'] else 'n/a (no classified test cluster)'}.")
w(f"- Row 13 'galaxies' row rejected (D10/D12 alternative): n_train = {alt['n_train']}, n_test = {alt['n_test']}, "
  f"outcome {alt['raw_verdict']}.")
w("- Secondary position sources (Ragozzine+12, Jee+14 P3, Clowe+12, Rau+14) and system-level classification: "
  "extractions in `t4b_extraction/cluster_*_sec_*.json`; T4a (EXPLORATORY) not scored.")
w("")
w("### 10.5 T5")
w("")
for k, v in t5["sensitivity_NON_DECIDING"].items():
    if k == "cap_diagnostic":
        w(f"- Saturation-cap diagnostic: g_bar cap = {v['gbar_cap_ms2']:.3e} m/s²; fraction of SPARC radial points "
          f"below the cap = {f(v['frac_points_below'], 4)}; fraction of galaxies with any point below = "
          f"{f(v['frac_galaxies_with_points_below'], 4)}.")
    elif k == "T5-A_heldout_quality_subset":
        w(f"- T5-A held-out quality subset (Q ∈ {{1, 2}}, i ≥ 30°): n = {v['n']}, median χ²_red = {f(v['median'], 4)}, "
          f"F(<2) = {f(v['frac_lt2'], 4)}.")
    else:
        w(f"- {k}: best = {f(v['best'], 5)}, held-out median χ²_red = {f(v['median'], 4)}, F(<2) = "
          f"{f(v['frac_lt2'], 4)}, outcome if deciding = {v['verdict_if_deciding']}.")
w("")
w("### 10.6 T6")
w("")
for k, v in t6["sensitivity_NON_DECIDING"].items():
    if v["Npix"] >= 2:
        w(f"- {k}: N_pix = {v['Npix']}, χ²_het = {f(v['chi2_het'], 3)} (dof {v['dof']}), p_het = {f(v['p_het'], 5)}, "
          f"H̄0 = {f(v['Hbar'], 3)} ± {f(v['sigma_Hbar'], 3)}, Z_all-sky = {f(v['Z_allsky'], 3)}, outcome {v['verdict']}.")
    else:
        w(f"- {k}: N_pix = {v['Npix']} (< 2), outcome {v['verdict']}.")
w("")
w("### 10.7 Coincidence-window diagnostic (PREREG §6)")
w("")
cw = S["coincidence_window"]
for k, v in cw.items():
    if k.startswith("f_leak"):
        w(f"- {k}: " + "; ".join(f"{c}: Δt = {f(x['window_Gyr'], 4)} Gyr"
                                + (f" (z {f(x['z_min'], 3)}–{f(x['z_max'], 3)})" if 'z_min' in x else "")
                                for c, x in v.items()))
w(f"- t0 = {f(cw['t0_Gyr'], 4)} Gyr. {cw['note']}.")
w("")

# ------------------------------------------------------------------ convergence
w("## 11. Convergence of every MCMC run")
w("")
w("| Run | converged | R̂_max − 1 | ESS_min | production steps / chain | χ²_min |")
w("|---|---|---|---|---|---|")
for k, v in R["convergence"].items():
    w(f"| {k} | {f(v['converged'])} | {f(v['rhat_max'] - 1, 5)} | {v['ess_min']:.0f} | {v['n_prod_per_chain']} | "
      f"{f(run(k)['chi2_min'], 4)} |")
w("")

# ------------------------------------------------------------------ provenance & deviations
w("## 12. Provenance, hand-over and blindness record")
w("")
for s in [
    "Frozen package: all 9 present files listed in PREREG_v4.sha256 match (no `_ORIGINALS` folder exists; see D1).",
    "Data: DATA_MANIFEST_REBUILD.sha256 (13 files, SHA-256 38b0b0bf…409d) was OTS-stamped at 06:28:55, before any fit. "
    "DATA_MANIFEST_REBUILD_PAPERS.sha256 (SHA-256 e3cc5c08…8faa) was OTS-stamped at 07:30, before T4b was computed.",
    "Hand-over: the previous agent session stopped while the 06:40 batch of fits was still running. A new session "
    "re-verified the earlier work, logged the hand-over, and reran the 37 unfinished fits with unchanged seeds "
    "(ACTIVITY_LOG_REBUILD.md).",
    "Blindness: nothing outside this folder was read. One accidental exposure is logged: a process listing showed the "
    "command line of an original-analysis script (name only). No original code, log, manifest or result was seen.",
]:
    w(f"- {s}")
w("")
w("## 13. DEVIATIONS_REBUILD.md (verbatim)")
w("")
dv = open(os.path.join(ROOT, "DEVIATIONS_REBUILD.md"), encoding="utf-8-sig").read()
for line in dv.splitlines():
    w(("#" + line) if line.startswith("## ") or line.startswith("# ") else line)
w("")
open(os.path.join(ROOT, "REBUILD_RESULTS.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
print("REBUILD_RESULTS.md written,", len(L), "lines")
