"""calibrate_rd.py -- one-time CAMB calibration of the EH98-z_d sound horizon (never called in a sampling loop).

factor = r_drag(CAMB) / r_s(z_d^EH98) at the Planck 2018 TT,TE,EE+lowE+lensing mean cosmology
(omega_b=0.02237, omega_c=0.1200, H0=67.36, sum m_nu=0.06 eV one massive, N_eff=3.044, T_CMB=2.7255).
Validation: the same factor is applied over a grid in (omega_b, omega_c, h) and compared with CAMB.
Output: results_rebuild/validation/rd_calibration.json
"""
import os, json, sys
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
import camb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cosmo

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results_rebuild", "validation")
os.makedirs(OUT, exist_ok=True)


def camb_rdrag(ombh2, omch2, h):
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=100 * h, ombh2=ombh2, omch2=omch2, mnu=0.06, num_massive_neutrinos=1,
                       nnu=cosmo.N_EFF, TCMB=cosmo.T_CMB, omk=0.0)
    pars.WantTransfer = False
    res = camb.get_background(pars)
    d = res.get_derived_params()
    return d["rdrag"], d["zdrag"], d["rstar"], d["zstar"]


def mine(ombh2, omch2, h):
    onu = cosmo.M_NU / (cosmo.NU93 * h * h)
    Om = (ombh2 + omch2) / h ** 2 + onu
    p = cosmo.Params(Om, h, ombh2)
    zd = cosmo.z_drag_eh98(ombh2, Om * h * h)
    return cosmo.sound_horizon(p, zd), zd


if __name__ == "__main__":
    ob, oc, h = 0.02237, 0.1200, 0.6736
    rd_c, zd_c, rs_c, zs_c = camb_rdrag(ob, oc, h)
    rs_m, zd_m = mine(ob, oc, h)
    factor = rd_c / rs_m
    print("fiducial CAMB rdrag", rd_c, "zdrag", zd_c, "| EH98 zd", zd_m, "r_s(zd)", rs_m, "factor", factor)
    rows = []
    for ob_ in np.linspace(0.0200, 0.0250, 6):
        for oc_ in np.linspace(0.100, 0.140, 5):
            for h_ in (0.60, 0.6736, 0.75):
                rc = camb_rdrag(ob_, oc_, h_)[0]
                rm = mine(ob_, oc_, h_)[0] * factor
                rows.append([ob_, oc_, h_, rc, rm, rm / rc - 1])
    rows = np.array(rows)
    near = (np.abs(rows[:, 0] - 0.0224) <= 0.0011) & (np.abs(rows[:, 1] - 0.12) <= 0.011)
    out = dict(factor=factor, fiducial=dict(ombh2=ob, omch2=oc, h=h, camb_rdrag=rd_c, camb_zdrag=zd_c,
                                            eh98_zd=zd_m, rs_at_eh98_zd=rs_m, camb_rstar=rs_c, camb_zstar=zs_c),
               camb_version=camb.__version__,
               grid_max_abs_frac_err=float(np.max(np.abs(rows[:, 5]))),
               grid_near_fiducial_max_abs_frac_err=float(np.max(np.abs(rows[near, 5]))),
               grid=rows.tolist(),
               grid_columns=["ombh2", "omch2", "h", "camb_rdrag", "calibrated_rebuild_rd", "frac_err"])
    json.dump(out, open(os.path.join(OUT, "rd_calibration.json"), "w"), indent=1)
    print("max |frac err| over grid:", out["grid_max_abs_frac_err"],
          " near fiducial:", out["grid_near_fiducial_max_abs_frac_err"])
    # also check HS96 z_* + my r_s(z_*) against CAMB r_star at fiducial (for information)
    p = cosmo.Params((ob + oc) / h ** 2 + 0.06 / (93.14 * h * h), h, ob)
    zs = cosmo.z_star_hs96(ob, p.Om * h * h)
    print("HS96 z*", zs, "r_s(z*)", cosmo.sound_horizon(p, zs), "CAMB z*", zs_c, "r*", rs_c)
