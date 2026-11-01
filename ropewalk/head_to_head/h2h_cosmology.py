import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import math
import sys
import numpy as np
from scipy import integrate, optimize

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if os.path.join(ROOT_DIR, "scripts") not in sys.path:
    sys.path.insert(0, os.path.join(ROOT_DIR, "scripts"))

import cosmology as cosmo  # Read-only import of frozen Stage 2 likelihood code

# 128-node Gauss-Legendre quadrature on [0, 1] for Reading A literal (a5) sound-horizon integral [Established]
_GL_X128, _GL_W128 = np.polynomial.legendre.leggauss(128)
_GL_U128 = 0.5 * (_GL_X128 + 1.0)
_GL_WU128 = 0.5 * _GL_W128


def sound_horizon_rs_a5_gl128(z_target: float, omega_b: float, omega_bc: float, h: float = 0.6736) -> float:
    """
    Reading A: Literal registered equation (a5) full sound-horizon integral r_s(z_target) in Mpc [Established]:
      r_s(z) = int_0^{a_target} c_s(a) / (a^2 H(a)) da
    using 128-node Gauss-Legendre quadrature on a in [0, a_target], where:
      a^2 H(a) / 100 = sqrt(omega_gamma + a^4 * omega_nu(a) + omega_bc * a + omega_de_0 * a^4)
    with omega_gamma = 2.4728e-5, omega_nu(a) = cosmo.omega_nu_h2_of_a(a) (exact Fermi-Dirac 0.06 eV
    massive eigenstate + 2 massless species, N_eff = 3.044), and c_s(a)/c = 1 / sqrt(3 * (1 + (3*omega_b/(4*omega_gamma))*a)).
    """
    a_target = 1.0 / (1.0 + z_target)
    a_nodes = a_target * _GL_U128
    h2 = h * h
    omega_nu_a4 = (a_nodes ** 4) * cosmo.omega_nu_h2_of_a(a_nodes)
    omega_de_0 = max(0.0, h2 - (cosmo.OMEGA_GAMMA_H2 + cosmo._SHARED_NU_REL_COEFF + cosmo.OMEGA_NU_MASS_H2 + omega_bc))
    h_over_100_a2 = np.sqrt(cosmo.OMEGA_GAMMA_H2 + omega_nu_a4 + omega_bc * a_nodes + omega_de_0 * (a_nodes ** 4))
    r_b = (3.0 * omega_b / (4.0 * cosmo.OMEGA_GAMMA_H2)) * a_nodes
    cs_over_c = 1.0 / np.sqrt(3.0 * (1.0 + r_b))
    integrand = (cosmo.C_KM_S / 100.0) * cs_over_c / h_over_100_a2
    return float(a_target * np.sum(_GL_WU128 * integrand))


def sound_horizon_rs_a5_quad(z_target: float, omega_b: float, omega_bc: float, h: float = 0.6736) -> tuple[float, float]:
    """
    Independent quadrature for Reading A: adaptive Gauss-Kronrod integration (scipy.integrate.quad)
    of the literal registered equation (a5) sound-horizon integral [Established].
    Returns (rs_mpc, abs_err_estimate).
    """
    a_target = 1.0 / (1.0 + z_target)
    h2 = h * h
    omega_de_0 = max(0.0, h2 - (cosmo.OMEGA_GAMMA_H2 + cosmo._SHARED_NU_REL_COEFF + cosmo.OMEGA_NU_MASS_H2 + omega_bc))

    def _integrand(a: float) -> float:
        if a <= 0.0:
            h_over_100_a2 = math.sqrt(cosmo.OMEGA_GAMMA_H2 + cosmo._SHARED_NU_REL_COEFF + cosmo.OMEGA_NU_MASS_H2 * float(np.exp(cosmo._FD_LOG_SPLINE(np.log(1e-8)))))
            return (cosmo.C_KM_S / 100.0) / (math.sqrt(3.0) * h_over_100_a2)
        omega_nu_a4 = (a ** 4) * float(cosmo.omega_nu_h2_of_a(a))
        h_over_100_a2 = math.sqrt(cosmo.OMEGA_GAMMA_H2 + omega_nu_a4 + omega_bc * a + omega_de_0 * (a ** 4))
        r_b = (3.0 * omega_b / (4.0 * cosmo.OMEGA_GAMMA_H2)) * a
        cs_over_c = 1.0 / math.sqrt(3.0 * (1.0 + r_b))
        return (cosmo.C_KM_S / 100.0) * cs_over_c / h_over_100_a2

    val, err = integrate.quad(_integrand, 0.0, a_target, epsabs=1e-12, epsrel=1e-12, limit=200)
    return float(val), float(err)


# Calibrate the baryon drag scale r_d under Reading A at Planck 2018 fiducial parameters
# (omega_b=0.02237, omega_bc=0.02237+0.1200=0.14237, omega_m=0.14237+OMEGA_NU_MASS_H2, r_d_CAMB=147.09 Mpc)
# per MULTIVERSE_STAGE1_EQUATIONS.md (a5) [Established]
_ZD_FID_A5 = cosmo.z_drag_eisenstein_hu(0.02237, 0.02237 + 0.1200 + cosmo.OMEGA_NU_MASS_H2)
_RS_DRAG_RAW_FID_A5 = sound_horizon_rs_a5_gl128(_ZD_FID_A5, 0.02237, 0.02237 + 0.1200, h=0.6736)
_DRAG_CALIB_FACTOR_A5 = 147.09 / _RS_DRAG_RAW_FID_A5


def r_drag_mpc_a5(omega_b: float, omega_bc: float, omega_m: float, h: float = 0.6736) -> float:
    """Calibrated baryon drag sound horizon r_d in Mpc under Reading A [Established]."""
    zd = cosmo.z_drag_eisenstein_hu(omega_b, omega_m)
    return _DRAG_CALIB_FACTOR_A5 * sound_horizon_rs_a5_gl128(zd, omega_b, omega_bc, h=h)


def cmb_priors_observable_cpl_reading_a(Omega_m_tot: float, h: float, omega_b: float, w0: float = -1.0, wa: float = 0.0):
    """Compute (R, l_A, 100*omega_b) at z_* for flat CPL / LCDM under Reading A (literal a5 r_s(z_*)) [Established]."""
    h2 = h * h
    omega_m = Omega_m_tot * h2
    omega_bc = omega_m - cosmo.OMEGA_NU_MASS_H2
    if omega_bc <= 0.0:
        return None
    z_star = cosmo.z_star_hu_sugiyama(omega_b, omega_m)
    DM_arr, _ = cosmo.comoving_distances_cpl([z_star], Omega_m_tot, h, w0=w0, wa=wa)
    if DM_arr is None:
        return None
    DM_star = float(DM_arr[0])
    dh0 = cosmo.C_KM_S / (100.0 * h)
    R_shift = math.sqrt(Omega_m_tot) * (DM_star / dh0)
    rs_star = sound_horizon_rs_a5_gl128(z_star, omega_b, omega_bc, h=h)
    l_A = math.pi * DM_star / rs_star
    return np.array([R_shift, l_A, 100.0 * omega_b], dtype=float)


def run_gate_g9b_reading_a() -> dict:
    """
    Recompute validation gate G9-b under Reading A (literal registered a5 sound-horizon integral) [Established].
    Fits flat LCDM (Omega_m_tot, h, 100*omega_b) to the Chen, Huang & Wang (2019, Table 1) LCDM 3x3 prior.
    """
    cmb = cosmo.CMBLikelihood(table="lcdm", mode="full_3x3")

    def obj(params):
        om, h, wb100 = params
        if not (0.15 < om < 0.50 and 0.55 < h < 0.85 and 1.9 < wb100 < 2.5):
            return 1e12
        vec = cmb_priors_observable_cpl_reading_a(om, h, wb100 / 100.0, w0=-1.0, wa=0.0)
        return cmb.chi2(vec)

    res = optimize.minimize(
        obj,
        [0.3153, 0.6736, 2.236],
        method="Nelder-Mead",
        options={"xatol": 1e-9, "fatol": 1e-11, "maxiter": 5000},
    )
    om_best, h_best, wb100_best = [float(x) for x in res.x]

    # Compute numerical Jacobian of (R, l_A, 100*omega_b) wrt (om, h, wb100) for Fisher covariance
    p0 = np.array([om_best, h_best, wb100_best])
    steps = np.array([1e-4, 1e-4, 1e-4])
    J = np.zeros((3, 3))
    for j in range(3):
        dp = np.zeros(3)
        dp[j] = steps[j]
        v_plus = cmb_priors_observable_cpl_reading_a(*(p0 + dp)[:2], (p0[2] + dp[2]) / 100.0)
        v_minus = cmb_priors_observable_cpl_reading_a(*(p0 - dp)[:2], (p0[2] - dp[2]) / 100.0)
        J[:, j] = (v_plus - v_minus) / (2.0 * steps[j])
    cov_params = np.linalg.inv(J.T @ cmb.inv_cov3 @ J)
    sig_om, sig_h, sig_wb100 = [float(np.sqrt(cov_params[i, i])) for i in range(3)]

    # Comparison against Stage 2 registered G9-b target (Omega_m = 0.3153 +- 0.0073, h = 0.6736 +- 0.0054, 100*omega_b = 2.236 +- 0.015)
    diff_om_sig = abs(om_best - 0.3153) / 0.0073
    diff_h_sig = abs(h_best - 0.6736) / 0.0054
    diff_wb_sig = abs(wb100_best - 2.236) / 0.015
    max_diff_sig = max(diff_om_sig, diff_h_sig, diff_wb_sig)
    passed = bool(max_diff_sig <= 0.3)

    # Also record comparison against Chen+19 Table 2 distance-prior column (h = 0.6727 +- 0.0060)
    diff_h_chen_table2_sig = abs(h_best - 0.6727) / 0.0060

    z_star_best = cosmo.z_star_hu_sugiyama(wb100_best / 100.0, om_best * (h_best ** 2))
    rs_a5_best = sound_horizon_rs_a5_gl128(
        z_star_best,
        wb100_best / 100.0,
        om_best * (h_best ** 2) - cosmo.OMEGA_NU_MASS_H2,
        h=h_best,
    )
    rs_chen_best = cosmo.sound_horizon_rs_chen(z_star_best, wb100_best / 100.0, om_best * (h_best ** 2))

    return {
        "gate": "G9-b (Reading A: literal a5 integral)",
        "obtained_Omega_m": om_best,
        "obtained_sigma_Omega_m": sig_om,
        "obtained_h": h_best,
        "obtained_sigma_h": sig_h,
        "obtained_100_omega_b": wb100_best,
        "obtained_sigma_100_omega_b": sig_wb100,
        "diff_Omega_m_sigma": diff_om_sig,
        "diff_h_sigma_vs_0p6736_0p0054": diff_h_sig,
        "diff_h_sigma_vs_0p6727_0p0060": diff_h_chen_table2_sig,
        "diff_wb_sigma": diff_wb_sig,
        "max_diff_sigma": max_diff_sig,
        "tolerance_sigma": 0.3,
        "passed": passed,
        "verdict": "PASS" if passed else "FAIL",
        "z_star_at_best": float(z_star_best),
        "rs_star_reading_a_Mpc": float(rs_a5_best),
        "rs_star_reading_b_Mpc": float(rs_chen_best),
        "rs_ratio_b_over_a": float(rs_chen_best / rs_a5_best),
    }


def joint_chi2_cpl_reading(
    Omega_bc: float,
    h: float,
    wb100: float,
    w0: float,
    wa: float,
    reading: str,
    bao_like: cosmo.DESIBAOLikelihood,
    cmb_like: cosmo.CMBLikelihood,
    sn_like: cosmo.PantheonPlusLikelihood | cosmo.DESDovekieLikelihood,
) -> float:
    """
    Joint chi2 evaluation for flat LCDM / CPL with sampled parameter Omega_bc = Omega_b + Omega_dm
    (neutrinos added separately: Omega_m_tot = Omega_bc + OMEGA_NU_MASS_H2 / h^2) [Established].
    Supports reading='A' (literal a5 sound horizon) and reading='B' (Chen+19 sound horizon).
    """
    h2 = h * h
    Omega_nu_0 = cosmo.OMEGA_NU_MASS_H2 / h2
    Omega_m_tot = Omega_bc + Omega_nu_0

    if reading == "B":
        return cosmo.joint_chi2_cpl(Omega_m_tot, h, wb100, w0, wa, bao_like, cmb_like, sn_like, bbn_prior=None)
    elif reading != "A":
        raise ValueError(f"Unknown sound-horizon reading: {reading}")

    omega_b = wb100 / 100.0
    omega_bc = Omega_bc * h2
    omega_m = Omega_m_tot * h2
    Omega_gamma = cosmo.OMEGA_GAMMA_H2 / h2
    Omega_de = 1.0 - (Omega_gamma + (cosmo._SHARED_NU_REL_COEFF / h2) + Omega_nu_0 + Omega_bc)
    if Omega_bc <= 0.0 or Omega_de <= 0.0:
        return np.inf

    if w0 == -1.0 and wa == 0.0:
        g_de = 1.0
    else:
        g_de = (cosmo._SHARED_A_GRID ** (-3.0 * (1.0 + w0 + wa))) * np.exp(-3.0 * wa * (1.0 - cosmo._SHARED_A_GRID))

    e2_grid = Omega_gamma * cosmo._SHARED_A_M4 + (cosmo._SHARED_ONU_GRID / h2) + Omega_bc * cosmo._SHARED_A_M3 + Omega_de * g_de
    if np.any(e2_grid <= 0.0):
        return np.inf
    E_grid = np.sqrt(e2_grid)
    cum_I, inv_E = cosmo._fast_cum_integral_inv_E(1.0 / E_grid)
    dh0 = cosmo.C_KM_S / (100.0 * h)

    # 1. BAO chi2
    cosmo._ensure_grid_lookup(bao_like, bao_like.unique_z)
    I_bao = cosmo._eval_cum_integral_at(
        bao_like.unique_z, cum_I, inv_E, bao_like._shared_idx, bao_like._shared_u, bao_like._shared_dz
    )
    DM_u = dh0 * I_bao
    E_u = cosmo.E_of_z_cpl(bao_like.unique_z, Omega_m_tot, h, w0=w0, wa=wa)
    if E_u is None:
        return np.inf
    DH_u = dh0 / E_u
    rd = r_drag_mpc_a5(omega_b, omega_bc, omega_m, h=h)
    pred_bao = bao_like._model_vector(DM_u, DH_u, rd)
    diff_bao = pred_bao - bao_like.mean
    chi2_tot = float(diff_bao @ bao_like.inv_cov @ diff_bao)

    # 2. CMB chi2 (Reading A: literal a5 r_s(z_*))
    z_star = cosmo.z_star_hu_sugiyama(omega_b, omega_m)
    DM_star = dh0 * cosmo._eval_scalar_cum_integral(z_star, cum_I, inv_E)
    R_shift = math.sqrt(Omega_m_tot) * (DM_star / dh0)
    rs_star = sound_horizon_rs_a5_gl128(z_star, omega_b, omega_bc, h=h)
    l_A = math.pi * DM_star / rs_star
    chi2_tot += cmb_like.chi2(np.array([R_shift, l_A, wb100], dtype=float))

    # 3. SN chi2
    cosmo._ensure_grid_lookup(sn_like, sn_like.z_hd)
    I_z = cosmo._eval_cum_integral_at(
        sn_like.z_hd, cum_I, inv_E, sn_like._shared_idx, sn_like._shared_u, sn_like._shared_dz
    )
    chi2_tot += sn_like._chi2_from_Iz(I_z)

    return float(chi2_tot)


def joint_chi2_law1_reading(
    Omega_bc: float,
    h: float,
    wb100: float,
    gamma_u: float,
    reading: str,
    bao_like: cosmo.DESIBAOLikelihood,
    cmb_like: cosmo.CMBLikelihood,
    sn_like: cosmo.PantheonPlusLikelihood | cosmo.DESDovekieLikelihood,
) -> float:
    """
    Joint chi2 evaluation for Law 1 (M1 and M2: w(a) = -1 + gamma_u / E(a)) with sampled parameter
    Omega_bc = Omega_b + Omega_dm (neutrinos added separately: Omega_m_tot = Omega_bc + OMEGA_NU_MASS_H2 / h^2)
    [Model Ansatz | Stage 1 d4].
    Supports reading='A' (literal a5 sound horizon) and reading='B' (Chen+19 sound horizon).
    """
    h2 = h * h
    Omega_nu_0 = cosmo.OMEGA_NU_MASS_H2 / h2
    Omega_m_tot = Omega_bc + Omega_nu_0

    if reading == "B":
        return cosmo.joint_chi2_law1(Omega_m_tot, h, wb100, gamma_u, bao_like, cmb_like, sn_like, bbn_prior=None)
    elif reading != "A":
        raise ValueError(f"Unknown sound-horizon reading: {reading}")

    omega_b = wb100 / 100.0
    omega_bc = Omega_bc * h2
    omega_m = Omega_m_tot * h2
    Omega_gamma = cosmo.OMEGA_GAMMA_H2 / h2
    Omega_de = 1.0 - (Omega_gamma + (cosmo._SHARED_NU_REL_COEFF / h2) + Omega_nu_0 + Omega_bc)
    if Omega_bc <= 0.0 or Omega_de <= 0.0:
        return np.inf

    non_de_grid = Omega_gamma * cosmo._SHARED_A_M4 + (cosmo._SHARED_ONU_GRID / h2) + Omega_bc * cosmo._SHARED_A_M3
    if abs(gamma_u) <= 1e-14:
        e2_grid = non_de_grid + Omega_de
    else:
        non_de_half = Omega_gamma * cosmo._SHARED_AH_M4 + (cosmo._SHARED_ONU_HALF / h2) + Omega_bc * cosmo._SHARED_AH_M3
        nd_g = non_de_grid.tolist()
        nd_h = non_de_half.tolist()
        dx_list = cosmo._SHARED_X_DX.tolist()
        ode_fl = float(Omega_de)
        m3_gu = -3.0 * float(gamma_u)
        n_steps = len(dx_list)
        y_i = 0.0
        g_list = [1.0] * (n_steps + 1)
        for i in range(n_steps):
            dx_f = dx_list[i]
            half_dx = 0.5 * dx_f
            e2_1 = nd_g[i] + ode_fl * g_list[i]
            if e2_1 <= 0.0:
                return np.inf
            k1 = m3_gu / math.sqrt(e2_1)

            e2_2 = nd_h[i] + ode_fl * math.exp(y_i + half_dx * k1)
            if e2_2 <= 0.0:
                return np.inf
            k2 = m3_gu / math.sqrt(e2_2)

            e2_3 = nd_h[i] + ode_fl * math.exp(y_i + half_dx * k2)
            if e2_3 <= 0.0:
                return np.inf
            k3 = m3_gu / math.sqrt(e2_3)

            e2_4 = nd_g[i + 1] + ode_fl * math.exp(y_i + dx_f * k3)
            if e2_4 <= 0.0:
                return np.inf
            k4 = m3_gu / math.sqrt(e2_4)

            y_i = y_i + (dx_f / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
            g_list[i + 1] = math.exp(y_i)
        e2_grid = non_de_grid + Omega_de * np.array(g_list, dtype=float)

    if np.any(e2_grid <= 0.0):
        return np.inf
    E_grid = np.sqrt(e2_grid)
    cum_I, inv_E = cosmo._fast_cum_integral_inv_E(1.0 / E_grid)
    dh0 = cosmo.C_KM_S / (100.0 * h)

    # 1. BAO chi2
    cosmo._ensure_grid_lookup(bao_like, bao_like.unique_z)
    I_bao = cosmo._eval_cum_integral_at(
        bao_like.unique_z, cum_I, inv_E, bao_like._shared_idx, bao_like._shared_u, bao_like._shared_dz
    )
    DM_u = dh0 * I_bao
    inv_E_bao = (1.0 - bao_like._shared_u) * inv_E[bao_like._shared_idx] + bao_like._shared_u * inv_E[bao_like._shared_idx + 1]
    DH_u = dh0 * inv_E_bao
    rd = r_drag_mpc_a5(omega_b, omega_bc, omega_m, h=h)
    pred_bao = bao_like._model_vector(DM_u, DH_u, rd)
    diff_bao = pred_bao - bao_like.mean
    chi2_tot = float(diff_bao @ bao_like.inv_cov @ diff_bao)

    # 2. CMB chi2 (Reading A: literal a5 r_s(z_*))
    z_star = cosmo.z_star_hu_sugiyama(omega_b, omega_m)
    DM_star = dh0 * cosmo._eval_scalar_cum_integral(z_star, cum_I, inv_E)
    R_shift = math.sqrt(Omega_m_tot) * (DM_star / dh0)
    rs_star = sound_horizon_rs_a5_gl128(z_star, omega_b, omega_bc, h=h)
    l_A = math.pi * DM_star / rs_star
    chi2_tot += cmb_like.chi2(np.array([R_shift, l_A, wb100], dtype=float))

    # 3. SN chi2
    cosmo._ensure_grid_lookup(sn_like, sn_like.z_hd)
    I_z = cosmo._eval_cum_integral_at(
        sn_like.z_hd, cum_I, inv_E, sn_like._shared_idx, sn_like._shared_u, sn_like._shared_dz
    )
    chi2_tot += sn_like._chi2_from_Iz(I_z)

    return float(chi2_tot)
