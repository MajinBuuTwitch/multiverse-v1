"""validate_cosmo.py -- cross-check production RK4 distances/sound horizons against
(i) scipy solve_ivp (DOP853, rtol=1e-12) ODE integration and (ii) Gauss-Legendre quadrature,
for LCDM, CPL and Law 1 at several redshifts.  Law 1 g(a) is also checked against an independent
solve_ivp integration of the coupled (ln g, chi) system.  Output: results_rebuild/validation/cosmo_validation.json
"""
import os, sys, json, math, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
from scipy.integrate import solve_ivp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cosmo

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results_rebuild", "validation")
os.makedirs(OUT, exist_ok=True)
cosmo.load_rd_calibration(os.path.join(OUT, "rd_calibration.json"))

ZTEST = [0.01, 0.1, 0.5, 1.0, 2.33]


def chi_ivp(p, z, law1_selfconsistent=False):
    """solve_ivp in z of dchi/dz = 1/E; for Law 1 optionally integrates d ln g/dz jointly (independent of RK4 grid)."""
    if law1_selfconsistent:
        def rhs(zz, y):
            a = 1.0 / (1.0 + zz)
            E = math.sqrt(float(p.E2_nonde(np.array([a]))[0]) + p.Ode * math.exp(y[1]))
            # d ln g/d ln a = -3 gam/E ; d ln a/dz = -1/(1+z)
            return [1.0 / E, 3.0 * p.gam / E / (1.0 + zz)]
        sol = solve_ivp(rhs, (0.0, max(z)), [0.0, 0.0], method="DOP853", rtol=1e-12, atol=1e-14,
                        dense_output=True)
        return np.array([sol.sol(zz)[0] for zz in z]), sol
    sol = solve_ivp(lambda zz, y: [1.0 / float(p.E(np.array([1.0 / (1.0 + zz)]))[0])], (0.0, max(z)), [0.0],
                    method="DOP853", rtol=1e-12, atol=1e-14, dense_output=True)
    return np.array([sol.sol(zz)[0] for zz in z]), sol


def chi_gl(p, z, n=200):
    x, w = np.polynomial.legendre.leggauss(n)
    out = []
    for zz in z:
        zp = 0.5 * zz * (x + 1.0)
        out.append(0.5 * zz * np.sum(w / p.E(1.0 / (1.0 + zp))))
    return np.array(out)


def rs_gl(p, z, n=400):
    """r_s via Gauss-Legendre in a on [0, a(z)]."""
    a_end = 1.0 / (1.0 + z)
    x, w = np.polynomial.legendre.leggauss(n)
    a = 0.5 * a_end * (x + 1.0)
    R = 3.0 * p.ombh2 / (4.0 * cosmo.OMEGA_GAMMA_H2)
    f = 1.0 / np.sqrt(3.0 * (1.0 + R * a)) / np.sqrt(a ** 4 * p.E2(a))
    return 0.5 * a_end * np.sum(w * f) * cosmo.C_KMS / (100 * p.h)


def rs_ivp(p, z):
    R = 3.0 * p.ombh2 / (4.0 * cosmo.OMEGA_GAMMA_H2)
    a_end = 1.0 / (1.0 + z)
    def rhs(a, y):
        aa = max(a, 1e-12)
        return [1.0 / math.sqrt(3.0 * (1.0 + R * aa)) / math.sqrt(aa ** 4 * float(p.E2(np.array([aa]))[0]))]
    sol = solve_ivp(rhs, (1e-12, a_end), [0.0], method="DOP853", rtol=1e-12, atol=1e-16)
    return sol.y[0, -1] * cosmo.C_KMS / (100 * p.h)


cases = {
    "lcdm": cosmo.Params(0.315, 0.6736, 0.02237),
    "cpl": cosmo.Params(0.315, 0.6736, 0.02237, model="cpl", w0=-0.8, wa=-0.7),
    "law1": cosmo.Params(0.315, 0.6736, 0.02237, model="law1", gam=0.15),
}
report = {}
for name, p in cases.items():
    d = cosmo.Distances(p)
    prod = d.chi_at(np.array(ZTEST))
    ivp, sol = chi_ivp(p, ZTEST, law1_selfconsistent=(name == "law1"))
    gl = chi_gl(p, ZTEST)
    zs = cosmo.z_star_hs96(p.ombh2, p.Om * p.h ** 2)
    chi_s_prod = d.chi_to(zs)
    chi_s_gl = chi_gl(p, [zs], n=2000)[0]
    rs_prod = cosmo.sound_horizon(p, zs)
    rec = dict(z=ZTEST, chi_prod=prod.tolist(), chi_ivp=ivp.tolist(), chi_gl=gl.tolist(),
               max_frac_prod_vs_ivp=float(np.max(np.abs(prod / ivp - 1))),
               max_frac_prod_vs_gl=float(np.max(np.abs(prod / gl - 1))),
               chi_zstar_prod=chi_s_prod, chi_zstar_gl=chi_s_gl, frac_zstar=chi_s_prod / chi_s_gl - 1,
               rs_zstar_prod=rs_prod, rs_zstar_gl=rs_gl(p, zs), rs_zstar_ivp=rs_ivp(p, zs))
    rec["frac_rs_prod_vs_gl"] = rec["rs_zstar_prod"] / rec["rs_zstar_gl"] - 1
    rec["frac_rs_prod_vs_ivp"] = rec["rs_zstar_prod"] / rec["rs_zstar_ivp"] - 1
    if name == "law1":
        # independent check of the RK4 g(a) against the solve_ivp joint system
        zz = np.array([0.5, 1.0, 2.0, 5.0])
        lng_ivp = np.array([sol.sol(z_)[1] for z_ in zz[zz <= max(ZTEST)]])
        rec["lng_check_z"] = zz[zz <= max(ZTEST)].tolist()
        rec["lng_rk4"] = p.lng(1 / (1 + zz[zz <= max(ZTEST)])).tolist()
        rec["lng_ivp"] = lng_ivp.tolist()
        # Law 1 identities: w0 = -1+gam ; wa = -1.5 gam [Om + gam (1-Om)] (Om here = late-time matter share)
        a_ = np.array([1.0 - 1e-4, 1.0, 1.0 + 1e-4])
        w = -1 + p.gam / p.E(np.array([1 - 1e-4, 1.0]))
        rec["w0_numeric"] = float(w[1]); rec["wa_numeric"] = float(-(w[1] - w[0]) / 1e-4)
        rec["wa_formula_Omtot"] = -1.5 * p.gam * (p.Om + p.gam * (1 - p.Om))
    report[name] = rec
    print(name, {k: v for k, v in rec.items() if k.startswith(("max", "frac"))})

# timing
p = cases["law1"]; t = time.time()
for _ in range(200):
    q = cosmo.Params(0.31, 0.68, 0.0224, model="law1", gam=0.1); dd = cosmo.Distances(q); cosmo.cmb_observables(q, dd); cosmo.r_drag(q)
report["timing_law1_ms"] = (time.time() - t) / 200 * 1e3
t = time.time()
for _ in range(200):
    q = cosmo.Params(0.31, 0.68, 0.0224, model="cpl", w0=-0.9, wa=-0.3); dd = cosmo.Distances(q); cosmo.cmb_observables(q, dd); cosmo.r_drag(q)
report["timing_cpl_ms"] = (time.time() - t) / 200 * 1e3
print("timing ms law1/cpl", report["timing_law1_ms"], report["timing_cpl_ms"])
json.dump(report, open(os.path.join(OUT, "cosmo_validation.json"), "w"), indent=1)
