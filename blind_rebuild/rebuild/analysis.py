"""analysis.py -- turns chains + data into every registered statistic, verdict, Holm correction and the model
verdict (PREREG §§2-5), plus the NON-DECIDING sensitivity analyses.  Output: results_rebuild/results.json,
results_rebuild/tables/*.csv, results_rebuild/figures/*.png, results_rebuild/FREEZE_*.json
"""
import os, sys, json, math, hashlib, time, glob
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
from scipy.stats import chi2 as chi2d, norm
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cosmo, t5, t6, t4b

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, "results_rebuild")
CH = os.path.join(RES, "chains")
FIG = os.path.join(RES, "figures"); TAB = os.path.join(RES, "tables")
for d in (FIG, TAB):
    os.makedirs(d, exist_ok=True)

R_PLANCK, S_PLANCK = 5.36, 0.065


def code_hash():
    h = hashlib.sha256()
    for f in sorted(glob.glob(os.path.join(ROOT, "rebuild", "*.py"))) + [os.path.join(ROOT, "run_all_rebuild.py")]:
        if os.path.exists(f):
            h.update(open(f, "rb").read())
    return h.hexdigest()


def freeze(name, payload):
    payload = dict(payload, code_sha256_rebuild_scripts=code_hash(),
                   written=time.strftime("%Y-%m-%dT%H:%M:%S%z"))
    p = os.path.join(RES, f"FREEZE_{name}.json")
    json.dump(payload, open(p, "w"), indent=1)
    payload["file_sha256"] = hashlib.sha256(open(p, "rb").read()).hexdigest()
    return payload


def run(name):
    return json.load(open(os.path.join(CH, f"{name}.json")))


def conv(r):
    return bool(r["diagnostics"]["converged_final"])


# ================================================================== gates
def gates():
    g = {}
    r = run("G9a_lcdm_BAOstd")
    m = r["summary"]["Om"]["mean"]
    g["G9-a"] = dict(statistic="posterior mean Omega_m (flat LCDM, unmodified desi_bao_dr2 BAO only)",
                     value=m, sd=r["summary"]["Om"]["sd"], target=0.2975, tol=0.3 * 0.0086,
                     diff=m - 0.2975, converged=conv(r))
    g["G9-a"]["PASS"] = bool(abs(m - 0.2975) <= 0.3 * 0.0086 and conv(r))
    r = run("G9b_lcdm_CMB")
    tg = dict(Om=(0.3166, 0.0084), h=(0.6727, 0.0060), wb100=(2.236, 0.015))
    rows = {}
    ok = conv(r)
    for k, (mu, s) in tg.items():
        v = r["summary"][k]["mean"]
        rows[k] = dict(value=v, sd=r["summary"][k]["sd"], target=mu, sigma=s, tol=0.3 * s, diff=v - mu,
                       diff_over_sigma=(v - mu) / s, within=bool(abs(v - mu) <= 0.3 * s))
        ok = ok and rows[k]["within"]
    g["G9-b"] = dict(statistic="posterior means (Omega_m, h, 100 omega_b) from the Chen+19 LCDM 3x3 prior alone",
                     benchmark="Planck 2018 VI Table 2 TT,TE,EE+lowE (DEVIATIONS D2)", params=rows,
                     converged=conv(r), PASS=bool(ok))
    r = run("G9c_cpl_BAOstd_CMB_D")
    rows = {}
    ok = conv(r)
    for k, (mu, s) in dict(w0=(-0.803, 0.054), wa=(-0.72, 0.21)).items():
        v = r["summary"][k]["mean"]
        rows[k] = dict(value=v, sd=r["summary"][k]["sd"], target=mu, tol=s, diff=v - mu,
                       diff_over_sigma=(v - mu) / s, within=bool(abs(v - mu) <= s))
        ok = ok and rows[k]["within"]
    g["G9-c"] = dict(statistic="posterior means (w0, wa): unmodified desi_bao_dr2 + Chen+19 LCDM prior + DES-Dovekie",
                     params=rows, converged=conv(r), PASS=bool(ok))
    gd = t5.gate_G9d()
    g["G9-d"] = dict(statistic="max |F_sigma - ncx2.cdf| on the registered 5x7 grid", value=gd["max_abs_diff"],
                     tol=1e-10, numpy=gd["numpy"], scipy=gd["scipy"], PASS=gd["PASS"],
                     monte_carlo=gd["monte_carlo"], grid=gd["grid"])
    return g


def gates_ok(g, sn):
    ok = g["G9-a"]["PASS"] and g["G9-b"]["PASS"]
    if sn == "D":
        ok = ok and g["G9-c"]["PASS"]
    return ok


# ================================================================== T1
def t1_per_run(prefix, sn, g=None):
    rl, rw, rc = run(f"{prefix}_law1_{sn}"), run(f"{prefix}_lcdm_{sn}"), run(f"{prefix}_cpl_{sn}")
    A = rl["chi2_min"] - rw["chi2_min"]
    B = rl["chi2_min"] - rc["chi2_min"]
    if B > 9.0 or A > -1.0:
        out = "FAIL"
    elif A <= -4.0 and B <= 4.0:
        out = "PASS"
    else:
        out = "INCONCLUSIVE"
    convd = conv(rl) and conv(rw) and conv(rc)
    gam = rl["x_best"][rl["params"].index("gam")]
    Om = rl["x_best"][0]
    res = dict(A=A, B=B, outcome=out, converged=convd,
               chi2_min=dict(law1=rl["chi2_min"], lcdm=rw["chi2_min"], cpl=rc["chi2_min"]),
               law1_best=dict(zip(rl["params"], rl["x_best"])), lcdm_best=dict(zip(rw["params"], rw["x_best"])),
               cpl_best=dict(zip(rc["params"], rc["x_best"])),
               w0_fit=-1 + gam, wa_fit=-1.5 * gam * (Om + gam * (1 - Om)),
               gamma_posterior=rl["summary"]["gam"],
               p_disc=float(chi2d.sf(max(0.0, -A), 1)))
    # T1-Sign from the CPL chain
    s = rc["summary"]
    res["sign"] = dict(P_w0_gt_m1=s["P_w0_gt_m1"], P_w0_lt_m1=1 - s["P_w0_gt_m1"], w0_mean=s["w0"]["mean"],
                       w0_sd=s["w0"]["sd"], wa_mean=s["wa"]["mean"], wa_sd=s["wa"]["sd"])
    # (-1,0) inside 68% credible region? (Gaussian approximation of the 2-D posterior; only used if sd(w0) <= 0.03)
    z = np.load(os.path.join(CH, f"{prefix}_cpl_{sn}.npz"))
    fl = z["chains"].reshape(-1, z["chains"].shape[-1])
    W = fl[:, 3:5]
    mu = W.mean(0); C = np.cov(W.T)
    d2 = float((np.array([-1.0, 0.0]) - mu) @ np.linalg.inv(C) @ (np.array([-1.0, 0.0]) - mu))
    res["sign"]["mahal2_LCDM_point"] = d2
    res["sign"]["LCDM_in_68pct"] = bool(d2 <= chi2d.ppf(0.6827, 2))
    if g is not None:
        res["gates_ok"] = gates_ok(g, sn)
    return res


def t1_verdicts(g, prefix="T1"):
    per = {sn: t1_per_run(prefix, sn, g) for sn in ("P", "D")}
    valid = {sn: per[sn]["converged"] and per[sn]["gates_ok"] for sn in per}
    if any(valid[sn] and per[sn]["outcome"] == "FAIL" for sn in per):
        raw = "FAIL"
    elif all(valid[sn] and per[sn]["outcome"] == "PASS" for sn in per):
        raw = "PASS (raw, before Holm)"
    else:
        raw = "INCONCLUSIVE"
    pdisc = max(per[sn]["p_disc"] for sn in per)
    p_holm = pdisc if all(valid.values()) else 1.0
    # T1-Sign
    sg = {sn: per[sn]["sign"] for sn in per}
    fail_sign = any(valid[sn] and sg[sn]["P_w0_lt_m1"] >= 0.95 for sn in sg) or \
        (all(valid.values()) and any(sg[sn]["w0_sd"] <= 0.03 for sn in sg) and all(sg[sn]["LCDM_in_68pct"] for sn in sg))
    if fail_sign:
        vs = "FAIL"
    elif all(valid[sn] and sg[sn]["P_w0_gt_m1"] >= 0.95 for sn in sg):
        vs = "PASS"
    else:
        vs = "INCONCLUSIVE"
    return dict(per_run=per, run_valid=valid, raw_verdict=raw, p_T1L1=pdisc, p_T1L1_for_holm=p_holm,
                T1_Sign=dict(per_run=sg, verdict=vs))


def t1_sensitivity(prefix):
    out = {}
    for sn in ("P", "D"):
        out[sn] = t1_per_run(prefix, sn)
    return out


# ================================================================== T2
def t2_run(name):
    r = run(name)
    s = r["summary"]["Obc"]
    Obc = s["median"]; sig = 0.5 * (s["q84"] - s["q16"])
    Rp = 19 * Obc - 1
    sc = math.sqrt((19 * sig) ** 2 + S_PLANCK ** 2)
    f = 1 - (19 * Obc - 1) / 6
    return dict(Obc_median=Obc, sigma_Obc=sig, f_leak=f, sigma_f=19 / 6 * sig, R_pred=Rp, sigma_R_pred=19 * sig,
                sigma_comb=sc, n_sigma=abs(Rp - R_PLANCK) / sc, signed_n_sigma=(Rp - R_PLANCK) / sc,
                exceeds_2sigma=bool(abs(Rp - R_PLANCK) > 2 * sc), converged=conv(r),
                Om_median=r["summary"]["Om"]["median"], w0=r["summary"]["w0"] if "w0" in r["summary"] else None,
                wa=r["summary"]["wa"] if "wa" in r["summary"] else None, chi2_min=r["chi2_min"])


def t2a(g):
    per = {sn: t2_run(f"T2A_{sn}") for sn in ("P", "D")}
    for sn in per:
        per[sn]["gates_ok"] = gates_ok(g, sn)
        per[sn]["valid"] = per[sn]["converged"] and per[sn]["gates_ok"]
    if any(per[sn]["valid"] and per[sn]["exceeds_2sigma"] for sn in per):
        v = "FAIL"
    elif all(per[sn]["valid"] and not per[sn]["exceeds_2sigma"] for sn in per):
        v = "PASS"
    else:
        v = "INCONCLUSIVE"
    fz = freeze("T2", dict(test="T2-A", runs={sn: {k: per[sn][k] for k in ("Obc_median", "sigma_Obc", "f_leak",
                                                                              "sigma_f", "R_pred", "sigma_R_pred")}
                                               for sn in per},
                           f_leak_for_T5=per["P"]["f_leak"], f_leak_source="T2-A-Pantheon+ (DESI/LUNA BBN)",
                           T2A_Pantheon_converged=per["P"]["converged"]))
    return dict(per_run=per, verdict=v, freeze=fz)


def t2n():
    ob = 1 / 19
    d1 = ob - 0.04930
    n1 = dict(Omega_b_model=ob, planck=0.04930, sigma=0.00086, diff=d1, n_sigma=d1 / 0.00086,
              verdict="PASS" if abs(d1) <= 2 * 0.00086 else "FAIL")
    def h0pred(wb100, s):
        wb = wb100 / 100
        H = 100 * math.sqrt(19 * wb)
        sH = 100 * 19 / (2 * math.sqrt(19 * wb)) * s / 100
        return H, sH
    H, sH = h0pred(2.237, 0.015)
    sc = math.sqrt(0.22 ** 2 + 0.54 ** 2)
    n2 = dict(H0_pred=H, sigma_H0_pred_propagated=sH, sigma_H0_pred_registered=0.22, planck=67.36, sigma_planck=0.54,
              sigma_comb=sc, diff=H - 67.36, n_sigma=(H - 67.36) / sc,
              verdict="PASS" if abs(H - 67.36) <= 2 * sc else "FAIL")
    sens = {}
    for lab, (wb, s) in dict(desi_bbn=(2.218, 0.055), cooke=(2.166, 0.019)).items():
        Hs, sHs = h0pred(wb, s)
        sens[lab] = dict(H0_pred=Hs, sigma=sHs, n_sigma_vs_planck=(Hs - 67.36) / math.sqrt(sHs ** 2 + 0.54 ** 2),
                         n_sigma_vs_desi_bbn_68p52=(Hs - 68.52) / math.sqrt(sHs ** 2 + 0.62 ** 2))
    n2["sensitivity_NON_DECIDING"] = sens
    return n1, n2


# ================================================================== T5
def t5_all(t2res, g):
    fl = t2res["per_run"]["P"]["f_leak"]
    Rfac = 6 * (1 - fl)
    gals = t5.load_sparc()
    ids, train, test = t5.split_sparc(gals)
    G = {k: t5.Galaxy(gals[k]) for k in ids}
    trg = [G[k] for k in train]; teg = [G[k] for k in test]
    out = dict(f_leak=fl, Rfac=Rfac, n_train=len(train), n_test=len(test), train_ids=train, test_ids=test)
    fits = {}
    for mode in ("A", "B"):
        fits[mode] = t5.train_scan(trg, Rfac, mode, "sum_red")
    fz = freeze("T5", dict(test="T5-A/T5-B/T5c", f_leak=fl, Rfac=Rfac, sigma_ref_hat_kpc=fits["A"]["best"],
                           k_hat=fits["B"]["best"], objective="sum of per-galaxy reduced chi2 over 88 training galaxies"))
    out["freeze"] = fz
    for mode in ("A", "B"):
        ev = t5.evaluate(teg, test, fits[mode]["best"], Rfac, mode)
        tr_ev = t5.evaluate(trg, train, fits[mode]["best"], Rfac, mode)
        out[f"T5-{mode}"] = dict(fit=fits[mode], test=ev, train_eval=dict(median=tr_ev["median"], frac_lt2=tr_ev["frac_lt2"]))
    out["T5c"] = t5.t5c(fits["A"]["best"], Rfac)
    # gate / f_leak dependency (D11)
    ok_dep = g["G9-d"]["PASS"] and t2res["per_run"]["P"]["converged"]
    for k in ("T5-A", "T5-B"):
        out[k]["verdict"] = out[k]["test"]["verdict"] if ok_dep else "INCONCLUSIVE"
    out["T5c"]["final_verdict"] = out["T5c"]["verdict"] if ok_dep else "INCONCLUSIVE"
    out["dependency_ok"] = ok_dep
    # NON-DECIDING: alternative training objectives
    sens = {}
    for mode in ("A", "B"):
        for obj in ("total_chi2", "median_red"):
            f = t5.train_scan(trg, Rfac, mode, obj)
            ev = t5.evaluate(teg, test, f["best"], Rfac, mode)
            sens[f"T5-{mode}_{obj}"] = dict(best=f["best"], median=ev["median"], frac_lt2=ev["frac_lt2"],
                                           verdict_if_deciding=ev["verdict"])
    # quality-cut subset of the held-out half (Q in {1,2}, i >= 30)
    q = [k for k in test if gals[k]["Q"] in (1, 2) and gals[k]["Inc"] >= 30]
    vq = np.array([out["T5-A"]["test"]["chi2_red"][k] for k in q])
    sens["T5-A_heldout_quality_subset"] = dict(n=len(q), median=float(np.median(vq)), frac_lt2=float(np.mean(vq < 2)))
    # cap diagnostic: fraction of radial points / galaxies with g_bar below the cap
    gdag = 1.2e-10
    cap = (math.log((Rfac + 1) / Rfac)) ** 2 * gdag
    npts = nbelow = 0; gal_below = 0
    for k in ids:
        gg = G[k]
        gbar = G_to_ms2(t5.G_KPC * gg.Mmono / gg.R ** 2)
        b = gbar < cap
        npts += len(b); nbelow += int(b.sum()); gal_below += int(b.any())
    sens["cap_diagnostic"] = dict(gbar_cap_ms2=cap, frac_points_below=nbelow / npts, n_points=npts,
                                  frac_galaxies_with_points_below=gal_below / len(ids))
    out["sensitivity_NON_DECIDING"] = sens
    return out


def G_to_ms2(g_kms2_per_kpc):
    # (km/s)^2 / kpc -> m/s^2
    return g_kms2_per_kpc * 1e6 / 3.0856775814913673e19


# ================================================================== T6
def t6_all():
    df, cov = t6.load()
    fx = t6.fix_MB(df, cov)
    fz = freeze("T6", dict(test="T6", M_B_fixed=fx["MB"], sigma_M_B=fx["sigma_MB"], n_calibrators=fx["n_cal"]))
    main = t6.run_T6(df, cov, fx["MB"], fx["sigma_MB"])
    sens = dict(equatorial=t6.run_T6(df, cov, fx["MB"], fx["sigma_MB"], coords="equatorial"),
                zCMB=t6.run_T6(df, cov, fx["MB"], fx["sigma_MB"], zcol="zCMB"),
                drop_without_merging=t6.run_T6(df, cov, fx["MB"], fx["sigma_MB"], merge=False))
    return dict(fix=fx, freeze=fz, main=main, sensitivity_NON_DECIDING=sens)


# ================================================================== T4b
def t4b_all():
    tab = json.load(open(os.path.join(ROOT, "t4b_extraction", "t4b_positions_rebuild.json")))
    res = t4b.run(tab)
    fz = freeze("T4b", dict(test="T4b", tau_lag_hat_myr=res["tau_hat_myr"], n_train=res["n_train"],
                            acc_train_max=res["acc_train_max"]))
    res["freeze"] = fz
    # NON-DECIDING alternative: row 13 galaxy position rejected (D10 item 2)
    alt = json.loads(json.dumps(tab))
    for c in alt["clusters"]:
        if c["row"] == 13:
            c["status"] = "unclassified (alternative reading: 'galaxies' row not accepted as luminosity-weighted centroid; no BCG coordinates)"
    a = t4b.run(alt, label="row13_S_rejected")
    res["sensitivity_NON_DECIDING"] = dict(row13_S_rejected=dict(n_train=a["n_train"], n_test=a["n_test"],
                                                                 raw_verdict=a["raw_verdict"],
                                                                 fail_clauses=a["fail_clauses"]))
    return res


# ================================================================== Holm & model verdict
def holm(pvals, raw):
    names = list(pvals)
    order = sorted(names, key=lambda n: pvals[n])
    alphas = [0.05 / 3, 0.05 / 2, 0.05]
    mstar = None
    for m, n in enumerate(order):
        if pvals[n] > alphas[m]:
            mstar = m
            break
    final = {}
    ranks = {}
    for m, n in enumerate(order):
        ranks[n] = dict(rank=m + 1, p=pvals[n], alpha=alphas[m])
        if raw[n].startswith("PASS"):
            final[n] = "INCONCLUSIVE (Failed Holm-Bonferroni Control)" if (mstar is not None and m >= mstar) else "PASS"
        else:
            final[n] = raw[n]
    return dict(order=order, ranks=ranks, m_star=(None if mstar is None else mstar + 1), final=final)


def model_verdict(v):
    pil = [v["T1-L1"], v["T2-A"], v["T4b"], v["T5-A"]]
    if any(x.startswith("FAIL") for x in pil):
        return "MODEL FALSIFIED (FAIL)"
    if all(x == "PASS" for x in pil):
        return "MODEL SUPPORTED (PASS)"
    return "MODEL INCONCLUSIVE (NOT FALSIFIED, NOT SUPPORTED)"


# ================================================================== sensitivities for T2
def t2_sensitivity():
    out = {}
    for tag in ("cooke", "marg", "r0", "LyaStd"):
        out[f"T2A_{tag}"] = {sn: t2_run(f"S_T2A_{tag}_{sn}") for sn in ("P", "D")}
    t2b = {}
    for sn in ("P", "D"):
        r = t2_run(f"S_T2B_{sn}")
        ref = run(f"T2A_{sn}")
        dchi = run(f"S_T2B_{sn}")["chi2_min"] - ref["chi2_min"]
        r["dchi2_vs_w0waCDM"] = dchi
        t2b[sn] = r
    fail = any(t2b[sn]["exceeds_2sigma"] or t2b[sn]["dchi2_vs_w0waCDM"] > 9 for sn in t2b)
    t2b["verdict_if_deciding"] = "FAIL" if fail else "PASS"
    out["T2B"] = t2b
    return out


# ================================================================== coincidence window diagnostic (§6)
def coincidence(fleak_list):
    from scipy.optimize import brentq
    wb, wc, H0 = 0.02237, 0.1200, 67.36
    h = H0 / 100
    Ob = wb / h ** 2; Odm = wc / h ** 2
    Or = cosmo.OMEGA_GAMMA_H2 * (1 + 3 * cosmo.NU_PER_SPECIES) / h ** 2
    OL = 0.6847
    Om = 0.3153
    def E2(a):
        return Or / a ** 4 + Om / a ** 3 + OL
    def shares(a):
        e = E2(a)
        # Omega_b, Omega_dm (dark matter = all non-baryonic matter incl. massive nu, Omega_m - Omega_b), Omega_de
        return np.array([Ob / a ** 3 / e, (Om - Ob) / a ** 3 / e, OL / e])
    out = {}
    from scipy.integrate import quad
    t0 = quad(lambda a: 1 / (a * math.sqrt(E2(a))), 1e-10, 1, limit=500)[0] / (H0 / 977.792)
    for fl in fleak_list:
        tgt = np.array([1 / 19, 6 * (1 - fl) / 19, (12 + 6 * fl) / 19])
        res = {}
        for crit in ("H-Abs", "H-Rel"):
            def dev(a):
                s = shares(a)
                return np.max(np.abs(s - tgt) if crit == "H-Abs" else np.abs(s - tgt) / tgt)
            tol = 0.05 if crit == "H-Abs" else 0.10
            a = np.geomspace(0.05, 5, 20001)
            ok = np.array([dev(x) <= tol for x in a])
            if not ok.any():
                res[crit] = dict(window_Gyr=0.0)
                continue
            idx = np.where(ok)[0]
            # contiguous window containing the best point
            lo, hi = idx[0], idx[-1]
            amin = brentq(lambda x: dev(x) - tol, a[lo - 1], a[lo]) if lo > 0 else a[lo]
            amax = brentq(lambda x: dev(x) - tol, a[hi], a[hi + 1]) if hi < len(a) - 1 else a[hi]
            dt = quad(lambda x: 1 / (x * math.sqrt(E2(x))), amin, amax)[0] / (H0 / 977.792)
            res[crit] = dict(a_min=amin, a_max=amax, z_max=1 / amin - 1, z_min=1 / amax - 1, window_Gyr=dt,
                             fraction_of_t0=dt / t0, contiguous=bool(len(idx) == hi - lo + 1))
        out[f"f_leak={fl:.6f}"] = res
    out["t0_Gyr"] = t0
    out["note"] = "Planck 2018 base LCDM shares; dark-matter share = Omega_m,tot - Omega_b (massive nu counted with matter)"
    return out


# ================================================================== main
def main():
    cosmo.load_rd_calibration(os.path.join(RES, "validation", "rd_calibration.json"))
    R = {}
    R["gates"] = g = gates()
    R["T1"] = t1 = t1_verdicts(g)
    R["T2-A"] = t2 = t2a(g)
    n1, n2 = t2n()
    R["T2-N1"], R["T2-N2"] = n1, n2
    R["T5"] = t5r = t5_all(t2, g)
    R["T6"] = t6r = t6_all()
    R["T4b"] = t4r = t4b_all()
    pv = {"T1-L1": t1["p_T1L1_for_holm"], "T4b": t4r["p_T4b_for_holm"],
          "T6": (t6r["main"]["p_het"] if t6r["main"]["Npix"] >= 2 else 1.0)}
    raw = {"T1-L1": t1["raw_verdict"], "T4b": t4r["raw_verdict"], "T6": t6r["main"]["verdict"]}
    R["holm"] = hb = holm(pv, raw)
    V = {"T1-L1": hb["final"]["T1-L1"], "T2-A": t2["verdict"], "T4b": hb["final"]["T4b"],
         "T5-A": t5r["T5-A"]["verdict"], "T1-Sign": t1["T1_Sign"]["verdict"], "T2-N1": n1["verdict"],
         "T2-N2": n2["verdict"], "T5-B": t5r["T5-B"]["verdict"], "T5c": t5r["T5c"]["final_verdict"],
         "T6": hb["final"]["T6"]}
    R["verdicts"] = V
    R["model_verdict"] = model_verdict(V)
    # ---------------- NON-DECIDING
    S = {}
    S["T1_wCDM_CMB_prior"] = t1_sensitivity("S_T1wcdm")
    S["T1_Lya_r0"] = t1_sensitivity("S_T1r0")
    S["T1_Lya_unmodified"] = t1_sensitivity("S_T1LyaStd")
    S.update(t2_sensitivity())
    S["coincidence_window"] = coincidence([1 / 6, t2["per_run"]["P"]["f_leak"]])
    R["sensitivity_NON_DECIDING"] = S
    # convergence table
    R["convergence"] = {os.path.basename(f)[:-5]: dict(converged=json.load(open(f))["diagnostics"]["converged_final"],
                                                       rhat_max=json.load(open(f))["diagnostics"]["rhat_max"],
                                                       ess_min=json.load(open(f))["diagnostics"]["ess_min"],
                                                       n_prod_per_chain=json.load(open(f))["diagnostics"]["n_prod_per_chain"])
                        for f in sorted(glob.glob(os.path.join(CH, "*.json")))}
    R["code_sha256_rebuild_scripts"] = code_hash()
    R["generated"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    json.dump(R, open(os.path.join(RES, "results.json"), "w"), indent=1, default=float)
    print(json.dumps(R["verdicts"], indent=1), R["model_verdict"])
    return R


if __name__ == "__main__":
    main()
