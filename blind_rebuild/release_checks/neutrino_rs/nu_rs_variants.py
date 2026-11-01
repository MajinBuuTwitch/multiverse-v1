"""nu_rs_variants.py -- read-only check: how the 0.06 eV neutrino enters r_s(z*), z*, D_M(z*), l_A, r_d.
Imports the frozen rebuild/cosmo.py unchanged; the variants re-implement ONLY the r_s integrand's E^2(a).
Writes nu_rs_variants.json next to this file. Reads phase3/SEALED/ANSWER_KEY.json read-only."""
import os, sys, json, math
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "rebuild"))
import cosmo  # noqa: E402
cosmo.load_rd_calibration(os.path.join(ROOT, "results_rebuild", "validation", "rd_calibration.json"))

SIG_LA = 0.090   # registered sigma(l_A), Chen+19 Table 1 LCDM column (PREREG 5.1)


def rs_custom(p, z, E2fun, n=600):
    """same RK4-in-a integral as cosmo.sound_horizon, with a replaceable E^2(a) (a > 0 nodes only; the a = 0
    node uses the a^4 E^2 -> const limit of the same E2fun, evaluated at a = 1e-12)."""
    a_end = 1.0 / (1.0 + z)
    a = np.linspace(0.0, a_end, n + 1)
    am = 0.5 * (a[:-1] + a[1:])
    R_fac = 3.0 * p.ombh2 / (4.0 * cosmo.OMEGA_GAMMA_H2)

    def f(aa):
        aa = np.where(aa > 0, aa, 1e-12)
        cs = 1.0 / np.sqrt(3.0 * (1.0 + R_fac * aa))
        return cs / np.sqrt(aa ** 4 * E2fun(aa))

    h = a[1] - a[0]
    return float(np.sum(h / 6.0 * (f(a[:-1]) + 4.0 * f(am) + f(a[1:]))) * cosmo.C_KMS / (100.0 * p.h))


def de(p, a):
    return p.Ode * np.exp(p.lng(a))


def main():
    h, wb, wc = 0.6736, 0.02237, 0.1200
    Om = (wb + wc) / h ** 2 + cosmo.M_NU / (cosmo.NU93 * h * h)
    p = cosmo.Params(Om, h, wb)
    d = cosmo.Distances(p)
    R, lA, wb100, zs, rs = cosmo.cmb_observables(p, d)
    DMs = d.chi_to(zs) * cosmo.C_KMS / (100 * h)
    Onu_rel_one_species = cosmo.OMEGA_GAMMA_H2 * cosmo.NU_PER_SPECIES / h ** 2
    variants = {
        "a_as_coded (exact Fermi-Dirac, cosmo.E2)": lambda x: p.E2(x),
        "b_nu_as_nonrelativistic_matter_in_rs": lambda x: p.Or / x ** 4 + (p.Obc + p.Onu) / x ** 3 + de(p, x),
        "c_nu_as_relativistic_(one massless species)_in_rs": lambda x: (p.Or + Onu_rel_one_species) / x ** 4 + p.Obc / x ** 3 + de(p, x),
        "d_nu_left_out_of_rs_(reviewer_hypothesis)": lambda x: p.Or / x ** 4 + p.Obc / x ** 3 + de(p, x),
    }
    out = {"cosmology": dict(h=h, ombh2=wb, omch2=wc, Om_tot=Om, Onu=p.Onu, omega_nu=p.Onu * h * h, Or=p.Or),
           "z_star_HS96": zs, "omega_m_used_in_zstar": Om * h * h, "D_M_zstar_Mpc": DMs, "R": R,
           "cosmo_sound_horizon_rs_zstar": rs, "cosmo_lA": lA, "variants": {}}
    for k, fn in variants.items():
        r = rs_custom(p, zs, fn)
        la = math.pi * DMs / r
        out["variants"][k] = dict(r_s_zstar=r, l_A=la, d_rs_vs_a=None, d_lA_vs_a=None)
    ra = out["variants"]["a_as_coded (exact Fermi-Dirac, cosmo.E2)"]
    for k, v in out["variants"].items():
        v["d_rs_vs_a"] = v["r_s_zstar"] - ra["r_s_zstar"]
        v["d_lA_vs_a"] = v["l_A"] - ra["l_A"]
        v["d_lA_vs_a_in_sigma"] = v["d_lA_vs_a"] / SIG_LA
    # the massive species' share of E^2 at z*, relative to one massless species (normalisation check)
    a_s = 1 / (1 + zs)
    out["nu_mass_density_at_zstar_over_one_massless_species"] = float(
        p.Onu * cosmo.nu_mass_shape(a_s) / (Onu_rel_one_species / a_s ** 4))
    out["nu_mass_density_early_limit_over_one_massless_species"] = float(
        p.Onu * cosmo.nu_mass_shape(1e-8) / (Onu_rel_one_species / 1e-8 ** 4))
    out["Y_nu_a_at_zstar (m/kT_nu)"] = float(cosmo.Y_NU * a_s)
    out["r_d_as_coded"] = cosmo.r_drag(p)
    out["z_drag_EH98"] = cosmo.z_drag_eh98(wb, Om * h * h)
    # ANSWER_KEY comparison (read-only)
    key = json.load(open(os.path.join(ROOT, "phase3", "SEALED", "ANSWER_KEY.json")))
    c1 = [u for u in key["universes"] if u["truth"] == "C1"][0]
    nl = c1["noiseless"]
    out["answer_key_C1"] = dict(universe=c1["universe_id"], r_s_zstar=nl["r_s_zstar"], z_star=nl["z_star"], l_A=nl["l_A"],
                                R=nl["R"], r_d=nl["r_d"],
                                diff_rs=nl["r_s_zstar"] - ra["r_s_zstar"], diff_zstar=nl["z_star"] - zs,
                                diff_lA=nl["l_A"] - ra["l_A"], diff_rd=nl["r_d"] - out["r_d_as_coded"])
    json.dump(out, open(os.path.join(HERE, "nu_rs_variants.json"), "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
