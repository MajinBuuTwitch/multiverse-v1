"""make_outputs.py -- tables (CSV) and figures from results_rebuild/results.json and the chains."""
import os, sys, json, csv, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, "results_rebuild")
FIG = os.path.join(RES, "figures"); TAB = os.path.join(RES, "tables"); CH = os.path.join(RES, "chains")
os.makedirs(FIG, exist_ok=True); os.makedirs(TAB, exist_ok=True)
R = json.load(open(os.path.join(RES, "results.json")))


def wcsv(name, header, rows):
    with open(os.path.join(TAB, name), "w", newline="") as f:
        w = csv.writer(f); w.writerow(header); w.writerows(rows)


# verdict table
wcsv("verdicts.csv", ["test", "verdict"], [[k, v] for k, v in R["verdicts"].items()] + [["MODEL", R["model_verdict"]]])
# gates
g = R["gates"]
rows = [["G9-a", "Om", g["G9-a"]["value"], g["G9-a"]["target"], g["G9-a"]["tol"], g["G9-a"]["PASS"]]]
for k, v in g["G9-b"]["params"].items():
    rows.append(["G9-b", k, v["value"], v["target"], v["tol"], v["within"]])
for k, v in g["G9-c"]["params"].items():
    rows.append(["G9-c", k, v["value"], v["target"], v["tol"], v["within"]])
rows.append(["G9-d", "max|F-ncx2|", g["G9-d"]["value"], 0, g["G9-d"]["tol"], g["G9-d"]["PASS"]])
wcsv("gates.csv", ["gate", "quantity", "value", "target", "tolerance", "pass"], rows)
# T1
rows = []
for sn, p in R["T1"]["per_run"].items():
    rows.append([sn, p["chi2_min"]["lcdm"], p["chi2_min"]["law1"], p["chi2_min"]["cpl"], p["A"], p["B"], p["outcome"],
                 p["w0_fit"], p["wa_fit"], p["sign"]["P_w0_gt_m1"], p["converged"], p["gates_ok"]])
wcsv("T1.csv", ["SN", "chi2min_LCDM", "chi2min_Law1", "chi2min_w0wa", "A", "B", "per_run_outcome", "w0_fit", "wa_fit",
                "P(w0>-1)", "converged", "mapped_gates_pass"], rows)
# T2
rows = [[sn, p["Obc_median"], p["sigma_Obc"], p["f_leak"], p["R_pred"], p["sigma_comb"], p["signed_n_sigma"],
         p["converged"], p["gates_ok"]] for sn, p in R["T2-A"]["per_run"].items()]
wcsv("T2A.csv", ["SN", "Obc_median", "sigma_Obc", "f_leak", "R_pred", "sigma_comb", "(R_pred-5.36)/sigma_comb",
                 "converged", "mapped_gates_pass"], rows)
# T5 per galaxy
for m in ("A", "B"):
    d = R["T5"][f"T5-{m}"]["test"]["chi2_red"]
    wcsv(f"T5{m}_heldout_chi2red.csv", ["galaxy", "chi2_red"], [[k, v] for k, v in d.items()])
# T6
t = R["T6"]["main"]
wcsv("T6_regions.csv", ["region_RING_index", "N_SN", "H0", "sigma_H0"],
     [[rg, t["counts_final"][rg], h, s] for rg, h, s in zip(t["regions"], t["H0_regions"], t["H0_region_sigma"])])
# T4b
wcsv("T4b_clusters.csv", ["row", "designation", "half", "t_p", "class", "paper", "pointer", "details"],
     [[c["row"], c["designation"], c["half"], c["tp"], c["class"], c["paper"], c["pointer"], json.dumps(c["details"])]
      for c in R["T4b"]["clusters"]])
# convergence
wcsv("convergence.csv", ["run", "converged", "Rhat_max", "ESS_min", "n_prod_per_chain"],
     [[k, v["converged"], v["rhat_max"], v["ess_min"], v["n_prod_per_chain"]] for k, v in R["convergence"].items()])

# ---------------- figures
# 1. w0-wa with Law-1 locus
fig, axs = plt.subplots(1, 2, figsize=(11, 4.5))
for ax, sn in zip(axs, ("P", "D")):
    z = np.load(os.path.join(CH, f"T1_cpl_{sn}.npz"))
    fl = z["chains"].reshape(-1, z["chains"].shape[-1])
    ax.hist2d(fl[:, 3], fl[:, 4], bins=80, range=[[-1.3, -0.4], [-2.0, 0.8]], cmap="Greys")
    p = R["T1"]["per_run"][sn]
    Om = p["law1_best"]["Om"]
    gm = np.linspace(0, 0.6, 100)
    ax.plot(-1 + gm, -1.5 * gm * (Om + gm * (1 - Om)), "r-", label="Law 1 locus (tangent)")
    ax.plot(p["w0_fit"], p["wa_fit"], "r*", ms=12, label="Law 1 best fit")
    ax.plot(-1, 0, "bx", ms=10, label="LCDM")
    ax.set_xlabel("w0"); ax.set_ylabel("wa"); ax.set_title(f"T1: BAO(mod)+CMB+{'Pantheon+' if sn == 'P' else 'DES-Dovekie'}")
    ax.legend(fontsize=8)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "T1_w0wa_law1.png"), dpi=130); plt.close()
# 2. T2-A
fig, ax = plt.subplots(figsize=(6, 3.5))
for i, (sn, p) in enumerate(R["T2-A"]["per_run"].items()):
    ax.errorbar(p["R_pred"], i, xerr=p["sigma_comb"], fmt="o", capsize=4, label=f"R_pred ({sn}) +- sigma_comb")
ax.axvline(5.36, color="k"); ax.axvspan(5.36 - 0.065, 5.36 + 0.065, color="grey", alpha=0.3)
ax.set_yticks([0, 1]); ax.set_yticklabels(["Pantheon+", "DES-Dovekie"]); ax.set_xlabel("dark-to-baryon ratio R")
ax.set_title("T2-A: R_pred = 19 Omega_bc - 1 vs Planck 5.36 +- 0.065")
plt.tight_layout(); plt.savefig(os.path.join(FIG, "T2A.png"), dpi=130); plt.close()
# 3. T5 training curves + held-out histogram
fig, axs = plt.subplots(1, 3, figsize=(14, 4))
for ax, m in zip(axs[:2], ("A", "B")):
    f = R["T5"][f"T5-{m}"]["fit"]
    ax.loglog(f["grid"], f["L"]); ax.axvline(f["best"], color="r")
    ax.set_xlabel("sigma_ref [kpc]" if m == "A" else "k = sigma_ref / R_d"); ax.set_ylabel("sum chi2_red (train)")
    ax.set_title(f"T5-{m} training objective")
v = np.array(list(R["T5"]["T5-A"]["test"]["chi2_red"].values()))
axs[2].hist(np.log10(v), bins=30); axs[2].axvline(np.log10(1.5), color="g"); axs[2].axvline(np.log10(3.0), color="r")
axs[2].set_xlabel("log10 chi2_red (held-out, T5-A)"); axs[2].set_title("T5-A held-out galaxies")
plt.tight_layout(); plt.savefig(os.path.join(FIG, "T5.png"), dpi=130); plt.close()
# 4. T6
fig, ax = plt.subplots(figsize=(7, 3.8))
ax.errorbar(range(len(t["regions"])), t["H0_regions"], yerr=t["H0_region_sigma"], fmt="o")
ax.axhline(t["Hbar"], color="r", label=f"GLS mean {t['Hbar']:.2f}")
ax.set_xticks(range(len(t["regions"]))); ax.set_xticklabels([str(r) for r in t["regions"]])
ax.set_xlabel("Galactic HEALPix Nside=1 RING region"); ax.set_ylabel("H0 [km/s/Mpc]"); ax.legend()
ax.set_title(f"T6: chi2_het = {t['chi2_het']:.2f} (dof {t['dof']}), p_het = {t['p_het']:.3f}")
plt.tight_layout(); plt.savefig(os.path.join(FIG, "T6_regions.png"), dpi=130); plt.close()
# 5. G9-b
z = np.load(os.path.join(CH, "G9b_lcdm_CMB.npz")); fl = z["chains"].reshape(-1, 3)
fig, ax = plt.subplots(figsize=(5, 4))
ax.hist2d(fl[:, 0], fl[:, 1], bins=60, cmap="Greys")
ax.errorbar(0.3166, 0.6727, xerr=0.0084, yerr=0.0060, fmt="rs", label="Planck 2018 TT,TE,EE+lowE")
ax.set_xlabel("Omega_m"); ax.set_ylabel("h"); ax.legend(fontsize=8); ax.set_title("G9-b: LCDM from Chen+19 prior")
plt.tight_layout(); plt.savefig(os.path.join(FIG, "G9b.png"), dpi=130); plt.close()
print("outputs written")
