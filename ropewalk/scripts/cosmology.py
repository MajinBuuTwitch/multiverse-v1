import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import math
import numpy as np
from scipy import linalg, interpolate, integrate

# Physical constants [Established | Tier 1]
C_KM_S = 299792.458  # Speed of light in km/s
T_CMB_0 = 2.7255     # Present CMB temperature in K
OMEGA_GAMMA_H2 = 2.4728e-5 * (T_CMB_0 / 2.7255) ** 4
N_EFF = 3.044
SUM_M_NU = 0.06      # eV (1 massive eigenstate of 0.06 eV + 2 massless)
OMEGA_NU_MASS_H2 = SUM_M_NU / 93.14  # 0.0006441915396177797

# Precompute exact Fermi-Dirac phase-space integral spline for the 1 massive neutrino
# y = m_nu c^2 a / (k_B T_nu,0). Today at a=1:
# k_B T_nu,0 = (4/11)^(1/3) * k_B T_CMB,0 = 1.67638e-4 eV, so y_0 = 0.06 / 1.67638e-4 = 357.9136
_KB_TNU0_EV = 8.617333262e-5 * T_CMB_0 * (4.0 / 11.0) ** (1.0 / 3.0)
_Y0_MASSIVE = SUM_M_NU / _KB_TNU0_EV


def _build_fermi_dirac_spline():
    """Precompute J(y) = [15 / (pi^4 * y)] * int_0^inf x^2 sqrt(x^2 + y^2) / (exp(x) + 1) dx
    normalized to J(y_0) at a=1 so that omega_nu_mass(a) = OMEGA_NU_MASS_H2 * a^-3 * [J(y0*a) / J(y0)].
    Wait: since rho_nu(a) = a^-4 * int p^2 sqrt(p^2 + m^2 a^2) / (e^p + 1) dp,
    at late times (y >> 1), int ~ m a * int p^2 / (e^p + 1) dp, so rho_nu(a) / rho_nu(1) = a^-3 * [I(y0*a) / (a * I(y0))].
    """
    y_grid = np.logspace(-5, 3.5, 400)
    x_nodes, x_weights = np.polynomial.laguerre.laggauss(64)
    # Using Laguerre quadrature: int_0^inf f(x) dx = sum w_i e^{x_i} f(x_i)
    vals = np.empty_like(y_grid)
    for idx, y in enumerate(y_grid):
        integrand = (x_nodes ** 2) * np.sqrt(x_nodes ** 2 + y ** 2) / (1.0 + np.exp(-x_nodes))
        # Note: exp(x) * 1/(exp(x)+1) = 1 / (1 + exp(-x))
        vals[idx] = np.sum(x_weights * integrand)
    # Evaluate at _Y0_MASSIVE
    integrand0 = (x_nodes ** 2) * np.sqrt(x_nodes ** 2 + _Y0_MASSIVE ** 2) / (1.0 + np.exp(-x_nodes))
    val0 = np.sum(x_weights * integrand0)
    # Define ratio R_fd(y) = I(y) / I(y0), so rho_nu_mass(a) = rho_nu_mass(1) * a^-4 * R_fd(y0 * a)
    spl = interpolate.CubicSpline(np.log(y_grid), np.log(vals / val0), extrapolate=True)
    return spl


_FD_LOG_SPLINE = _build_fermi_dirac_spline()


def omega_nu_h2_of_a(a):
    """Total physical neutrino density omega_nu(a) * a^4 / a^4 -> returns omega_nu(a) = rho_nu(a) / rho_crit,0 * h^2.
    Includes 2 massless species + 1 massive species (0.06 eV) with N_eff = 3.044.
    """
    a_arr = np.asarray(a, dtype=float)
    # 2 massless species share (2/3)*N_eff of relativistic neutrino density
    omega_nu_rel_2_h2 = OMEGA_GAMMA_H2 * (7.0 / 8.0) * ((4.0 / 11.0) ** (4.0 / 3.0)) * (2.0 * N_EFF / 3.0)
    # 1 massive species with exact Fermi-Dirac phase space
    y = np.clip(_Y0_MASSIVE * a_arr, 1e-8, 1e4)
    r_fd = np.exp(_FD_LOG_SPLINE(np.log(y)))
    return omega_nu_rel_2_h2 * (a_arr ** -4) + OMEGA_NU_MASS_H2 * (a_arr ** -4) * r_fd


def z_star_hu_sugiyama(omega_b, omega_m):
    """Recombination redshift z_* from Hu & Sugiyama (1996, ApJ 471, 542, Eqs. E-1, E-2),
    matching Chen, Huang & Wang (2019, Eqs. 2.4-2.5) and MULTIVERSE_STAGE1_EQUATIONS.md (a5).
    """
    g1 = (0.0783 * (omega_b ** -0.238)) / (1.0 + 39.5 * (omega_b ** 0.763))
    g2 = 0.560 / (1.0 + 21.1 * (omega_b ** 1.81))
    return 1048.0 * (1.0 + 0.00124 * (omega_b ** -0.738)) * (1.0 + g1 * (omega_m ** g2))


def z_drag_eisenstein_hu(omega_b, omega_m):
    """Baryon drag redshift z_d from Eisenstein & Hu (1998, ApJ 496, 605, Eqs. 4-6),
    matching MULTIVERSE_STAGE1_EQUATIONS.md (a5).
    """
    b1 = 0.313 * (omega_m ** -0.419) * (1.0 + 0.607 * (omega_m ** 0.674))
    b2 = 0.238 * (omega_m ** 0.223)
    return (1291.0 * (omega_m ** 0.251) / (1.0 + 0.659 * (omega_m ** 0.828))) * (1.0 + b1 * (omega_b ** b2))


# Gauss-Legendre nodes on [0, 1] for fast sound-horizon and comoving distance integration
_GL_X64, _GL_W64 = np.polynomial.legendre.leggauss(64)
_GL_U64 = 0.5 * (_GL_X64 + 1.0)
_GL_WU64 = 0.5 * _GL_W64


def sound_horizon_rs_chen(z_target, omega_b, omega_m):
    """Exact sound horizon r_s(z_target) in Mpc using the early-universe expansion rate
    as defined in Chen, Huang & Wang (2019, JCAP 02, 028, Eqs. 2.1-2.6) and (a5):
      r_s(z) = (c / 100) * int_0^{a_target} da / [a^2 * sqrt(omega_r * a^-4 + omega_m * a^-3) * sqrt(3*(1 + R_b*a))]
    where a_eq^-1 = 24185 * omega_m (Chen et al. 2019 Eq. 2.3 => omega_r = omega_m * a_eq = 1.0 / 24185.0)
    and R_b(a) = 3 * omega_b * a / (4 * omega_gamma) = 30312.6 * omega_b * a.
    """
    a_target = 1.0 / (1.0 + z_target)
    a_nodes = a_target * _GL_U64
    omega_r = 1.0 / 24185.0
    # H(a)/100 = a^-2 * sqrt(omega_r + omega_m * a)
    h_over_100_a2 = np.sqrt(omega_r + omega_m * a_nodes)
    r_b = (3.0 * omega_b / (4.0 * OMEGA_GAMMA_H2)) * a_nodes
    cs_over_c = 1.0 / np.sqrt(3.0 * (1.0 + r_b))
    integrand = (C_KM_S / 100.0) * cs_over_c / h_over_100_a2
    return a_target * float(np.sum(_GL_WU64 * integrand))


# Calibrate the drag-scale factor at Planck 2018 fiducial parameters (omega_b=0.02237, omega_m=0.143024, r_d_CAMB=147.09 Mpc)
# per MULTIVERSE_STAGE1_EQUATIONS.md (a5): "calibrated to CLASS/CAMB via the standard post-Planck drag-scale factor"
_ZD_FID = z_drag_eisenstein_hu(0.02237, 0.02237 + 0.1200 + OMEGA_NU_MASS_H2)
_RS_DRAG_RAW_FID = sound_horizon_rs_chen(_ZD_FID, 0.02237, 0.02237 + 0.1200 + OMEGA_NU_MASS_H2)
_DRAG_CALIB_FACTOR = 147.09 / _RS_DRAG_RAW_FID


def r_drag_mpc(omega_b, omega_m):
    """Calibrated baryon drag sound horizon r_d in Mpc (MULTIVERSE_STAGE1_EQUATIONS.md a5)."""
    zd = z_drag_eisenstein_hu(omega_b, omega_m)
    return _DRAG_CALIB_FACTOR * sound_horizon_rs_chen(zd, omega_b, omega_m)


def solve_law1_de_grid(Omega_m_tot, h, gamma_u, z_max=1100.0, n_steps=1000):
    """Integrate Law 1 (d4) dark energy density g(a) on a 1,000-point log-a grid using 4th-order Runge-Kutta
    as specified in PREREG.md Section 5.1:
      d(ln g) / d(ln a) = -3 * gamma_u / E(a), g(1) = 1.
    Returns a CubicSpline for g(a) and E(a).
    """
    h2 = h * h
    Omega_gamma = OMEGA_GAMMA_H2 / h2
    Omega_nu_0 = OMEGA_NU_MASS_H2 / h2
    Omega_bc = Omega_m_tot - Omega_nu_0
    # Radiation + massless neutrinos at a=1
    Omega_nu_rel_0 = (OMEGA_GAMMA_H2 * (7.0 / 8.0) * ((4.0 / 11.0) ** (4.0 / 3.0)) * (2.0 * N_EFF / 3.0)) / h2
    Omega_de = 1.0 - (Omega_gamma + Omega_nu_rel_0 + Omega_nu_0 + Omega_bc)

    # Uniform grid in x = ln(a) from 0 down to -ln(1 + z_max)
    x_min = -np.log(1.0 + z_max)
    x_grid = np.linspace(0.0, x_min, n_steps + 1)  # descending from 0 to x_min
    dx = x_grid[1] - x_grid[0]  # negative step
    a_grid = np.exp(x_grid)

    # Precompute non-DE contribution to E^2(a) on grid and half-steps
    a_half = np.exp(x_grid[:-1] + 0.5 * dx)
    non_de_grid = Omega_gamma * (a_grid ** -4) + (omega_nu_h2_of_a(a_grid) / h2) + Omega_bc * (a_grid ** -3)
    non_de_half = Omega_gamma * (a_half ** -4) + (omega_nu_h2_of_a(a_half) / h2) + Omega_bc * (a_half ** -3)

    ln_g = np.zeros(n_steps + 1, dtype=float)
    if abs(gamma_u) > 1e-14:
        nd_g = non_de_grid.tolist()
        nd_h = non_de_half.tolist()
        ode_fl = float(Omega_de)
        m3_gu = -3.0 * float(gamma_u)
        dx_f = float(dx)
        half_dx = 0.5 * dx_f
        sixth_dx = dx_f / 6.0
        y_i = 0.0
        ln_g_list = [0.0] * (n_steps + 1)
        for i in range(n_steps):
            e2_1 = nd_g[i] + ode_fl * math.exp(y_i)
            if e2_1 <= 0.0:
                return None
            k1 = m3_gu / math.sqrt(e2_1)

            y_2 = y_i + half_dx * k1
            e2_2 = nd_h[i] + ode_fl * math.exp(y_2)
            if e2_2 <= 0.0:
                return None
            k2 = m3_gu / math.sqrt(e2_2)

            y_3 = y_i + half_dx * k2
            e2_3 = nd_h[i] + ode_fl * math.exp(y_3)
            if e2_3 <= 0.0:
                return None
            k3 = m3_gu / math.sqrt(e2_3)

            y_4 = y_i + dx_f * k3
            e2_4 = nd_g[i + 1] + ode_fl * math.exp(y_4)
            if e2_4 <= 0.0:
                return None
            k4 = m3_gu / math.sqrt(e2_4)

            y_i = y_i + sixth_dx * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
            ln_g_list[i + 1] = y_i
        ln_g = np.array(ln_g_list, dtype=float)

    g_grid = np.exp(ln_g)
    e2_grid = non_de_grid + Omega_de * g_grid
    if np.any(e2_grid <= 0.0):
        return None
    e_grid = np.sqrt(e2_grid)
    # Build spline in increasing ln(a)
    spl_E = interpolate.CubicSpline(x_grid[::-1], e_grid[::-1], extrapolate=True)
    return spl_E


def E_of_z_cpl(z, Omega_m_tot, h, w0=-1.0, wa=0.0):
    """Dimensionless Hubble rate E(z) = H(z)/H0 for flat w0waCDM (CPL) or LCDM."""
    z_arr = np.asarray(z, dtype=float)
    a = 1.0 / (1.0 + z_arr)
    h2 = h * h
    Omega_gamma = OMEGA_GAMMA_H2 / h2
    Omega_nu_0 = OMEGA_NU_MASS_H2 / h2
    Omega_bc = Omega_m_tot - Omega_nu_0
    Omega_nu_rel_0 = (OMEGA_GAMMA_H2 * (7.0 / 8.0) * ((4.0 / 11.0) ** (4.0 / 3.0)) * (2.0 * N_EFF / 3.0)) / h2
    Omega_de = 1.0 - (Omega_gamma + Omega_nu_rel_0 + Omega_nu_0 + Omega_bc)
    if w0 == -1.0 and wa == 0.0:
        g_de = 1.0
    else:
        g_de = (a ** (-3.0 * (1.0 + w0 + wa))) * np.exp(-3.0 * wa * (1.0 - a))
    e2 = Omega_gamma * (a ** -4) + (omega_nu_h2_of_a(a) / h2) + Omega_bc * (a ** -3) + Omega_de * g_de
    if np.any(e2 <= 0.0):
        return None
    return np.sqrt(e2)


def comoving_distances_cpl(z_targets, Omega_m_tot, h, w0=-1.0, wa=0.0):
    """Compute D_M(z) and D_H(z) in Mpc for an array or scalar of z_targets under CPL/LCDM."""
    z_arr = np.atleast_1d(np.asarray(z_targets, dtype=float))
    z_max = float(np.max(z_arr))
    # Build dense grid up to min(z_max, 3.0) + log grid above if z_max > 3.0
    if z_max <= 3.0:
        z_grid = np.linspace(0.0, max(z_max, 0.01), 401)
    else:
        z_low = np.linspace(0.0, 3.0, 301)
        z_high = np.logspace(np.log10(3.0), np.log10(z_max), 201)[1:]
        z_grid = np.concatenate([z_low, z_high])
    E_grid = E_of_z_cpl(z_grid, Omega_m_tot, h, w0=w0, wa=wa)
    if E_grid is None:
        return None, None
    inv_E_spl = interpolate.CubicSpline(z_grid, 1.0 / E_grid)
    anti_spl = inv_E_spl.antiderivative()
    dh0 = C_KM_S / (100.0 * h)
    DM = dh0 * anti_spl(z_arr)
    E_targets = E_of_z_cpl(z_arr, Omega_m_tot, h, w0=w0, wa=wa)
    if E_targets is None:
        return None, None
    DH = dh0 / E_targets
    return DM, DH


def comoving_distances_law1(z_targets, Omega_m_tot, h, gamma_u):
    """Compute D_M(z) and D_H(z) in Mpc for an array of z_targets under Law 1 (d4): w(a) = -1 + gamma_u / E(a)."""
    z_arr = np.atleast_1d(np.asarray(z_targets, dtype=float))
    z_max = max(float(np.max(z_arr)), 3.0)
    spl_E = solve_law1_de_grid(Omega_m_tot, h, gamma_u, z_max=max(z_max, 1150.0), n_steps=1000)
    if spl_E is None:
        return None, None, None
    if z_max <= 3.5:
        z_grid = np.linspace(0.0, z_max, 401)
    else:
        z_low = np.linspace(0.0, 3.0, 301)
        z_high = np.logspace(np.log10(3.0), np.log10(z_max), 201)[1:]
        z_grid = np.concatenate([z_low, z_high])
    x_grid = -np.log(1.0 + z_grid)
    E_grid = spl_E(x_grid)
    if np.any(E_grid <= 0.0):
        return None, None, None
    inv_E_spl = interpolate.CubicSpline(z_grid, 1.0 / E_grid)
    anti_spl = inv_E_spl.antiderivative()
    dh0 = C_KM_S / (100.0 * h)
    DM = dh0 * anti_spl(z_arr)
    E_targets = spl_E(-np.log(1.0 + z_arr))
    DH = dh0 / E_targets
    return DM, DH, spl_E


def cmb_priors_observable_cpl(Omega_m_tot, h, omega_b, w0=-1.0, wa=0.0):
    """Compute (R, l_A, 100*omega_b) at z_* for flat CPL / LCDM (MULTIVERSE_STAGE1_EQUATIONS.md a5)."""
    omega_m = Omega_m_tot * (h ** 2)
    z_star = z_star_hu_sugiyama(omega_b, omega_m)
    DM_arr, _ = comoving_distances_cpl([z_star], Omega_m_tot, h, w0=w0, wa=wa)
    if DM_arr is None:
        return None
    DM_star = float(DM_arr[0])
    dh0 = C_KM_S / (100.0 * h)
    R_shift = np.sqrt(Omega_m_tot) * (DM_star / dh0)
    rs_star = sound_horizon_rs_chen(z_star, omega_b, omega_m)
    l_A = np.pi * DM_star / rs_star
    return np.array([R_shift, l_A, 100.0 * omega_b], dtype=float)


def cmb_priors_observable_law1(Omega_m_tot, h, omega_b, gamma_u, spl_E=None):
    """Compute (R, l_A, 100*omega_b) at z_* for Law 1 (d4)."""
    omega_m = Omega_m_tot * (h ** 2)
    z_star = z_star_hu_sugiyama(omega_b, omega_m)
    if spl_E is None:
        DM_arr, _, _ = comoving_distances_law1([z_star], Omega_m_tot, h, gamma_u)
        if DM_arr is None:
            return None
        DM_star = float(DM_arr[0])
    else:
        z_low = np.linspace(0.0, 3.0, 301)
        z_high = np.logspace(np.log10(3.0), np.log10(z_star), 201)[1:]
        z_grid = np.concatenate([z_low, z_high])
        E_grid = spl_E(-np.log(1.0 + z_grid))
        if np.any(E_grid <= 0.0):
            return None
        inv_E_spl = interpolate.CubicSpline(z_grid, 1.0 / E_grid)
        dh0 = C_KM_S / (100.0 * h)
        DM_star = float(dh0 * inv_E_spl.antiderivative()(z_star))
    dh0 = C_KM_S / (100.0 * h)
    R_shift = np.sqrt(Omega_m_tot) * (DM_star / dh0)
    rs_star = sound_horizon_rs_chen(z_star, omega_b, omega_m)
    l_A = np.pi * DM_star / rs_star
    return np.array([R_shift, l_A, 100.0 * omega_b], dtype=float)


class CMBLikelihood:
    """Chen, Huang & Wang (2019, Table 1) compressed CMB distance prior likelihood.
    Supports:
      - mode='full_3x3': full 3x3 (R, l_A, 100*omega_b) prior (for T1-L1, T1-Sign, Gates G9-b, G9-c)
      - mode='conditional_2x2': exact conditional (R, l_A | 100*omega_b) prior (for T2-A, T2-B per PREREG.md §5.2)
      - mode='marginal_2x2': marginal 2x2 (R, l_A) block (for T2 sensitivity analysis)
    """

    def __init__(self, table="lcdm", mode="full_3x3"):
        if table == "lcdm":
            self.mu = np.array([1.7502, 301.471, 2.236], dtype=float)
            self.sig = np.array([0.0046, 0.090, 0.015], dtype=float)
            self.corr = np.array(
                [
                    [1.00, 0.46, -0.66],
                    [0.46, 1.00, -0.33],
                    [-0.66, -0.33, 1.00],
                ],
                dtype=float,
            )
        elif table == "wcdm":
            self.mu = np.array([1.7493, 301.462, 2.239], dtype=float)
            self.sig = np.array([0.0046, 0.090, 0.015], dtype=float)
            self.corr = np.array(
                [
                    [1.00, 0.47, -0.66],
                    [0.47, 1.00, -0.34],
                    [-0.66, -0.34, 1.00],
                ],
                dtype=float,
            )
        else:
            raise ValueError(f"Unknown CMB table: {table}")

        self.cov3 = np.outer(self.sig, self.sig) * self.corr
        self.inv_cov3 = linalg.inv(self.cov3)
        self.mode = mode

        # Precompute conditional 2x2 (R, l_A | 100*omega_b) parameters per PREREG.md §5.2
        self.c11 = self.cov3[:2, :2]
        self.c12 = self.cov3[:2, 2]
        self.c22 = self.cov3[2, 2]
        self.cond_cov2 = self.c11 - np.outer(self.c12, self.c12) / self.c22
        self.inv_cond_cov2 = linalg.inv(self.cond_cov2)
        self.inv_marg_cov2 = linalg.inv(self.c11)

    def chi2(self, vec3):
        if vec3 is None:
            return np.inf
        if self.mode == "full_3x3":
            diff = vec3 - self.mu
            return float(diff @ self.inv_cov3 @ diff)
        elif self.mode == "conditional_2x2":
            wb100 = vec3[2]
            mu_cond = self.mu[:2] + (self.c12 / self.c22) * (wb100 - self.mu[2])
            diff2 = vec3[:2] - mu_cond
            return float(diff2 @ self.inv_cond_cov2 @ diff2)
        elif self.mode == "marginal_2x2":
            diff2 = vec3[:2] - self.mu[:2]
            return float(diff2 @ self.inv_marg_cov2 @ diff2)
        else:
            raise ValueError(f"Unknown mode: {self.mode}")


class DESIBAOLikelihood:
    """DESI DR2 BAO likelihood from CobayaSampler/bao_data/desi_bao_dr2.
    Supports:
      - lya_mode='unmodified': exact 13-point BAO-only vector (used in Gates G9-a, G9-c, and sensitivity check)
      - lya_mode='joint_ap_deciding': replaces z=2.33 Lya block with arXiv:2607.27410 (DH/rd=8.600+-0.066, DM/rd=39.32+-0.33, r=-0.431)
      - lya_mode='joint_ap_r0': same replacement with r=0.0 (sensitivity check per PREREG.md §5.1)
    """

    def __init__(self, data_dir, lya_mode="joint_ap_deciding"):
        mean_file = os.path.join(data_dir, "desi_bao_dr2", "desi_gaussian_bao_ALL_GCcomb_mean.txt")
        cov_file = os.path.join(data_dir, "desi_bao_dr2", "desi_gaussian_bao_ALL_GCcomb_cov.txt")

        z_list = []
        val_list = []
        qty_list = []
        with open(mean_file, "r", encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if not s or s.startswith("#"):
                    continue
                parts = s.split()
                z_list.append(float(parts[0]))
                val_list.append(float(parts[1]))
                qty_list.append(parts[2])

        self.z = np.array(z_list, dtype=float)
        self.mean = np.array(val_list, dtype=float)
        self.qty = qty_list
        self.cov = np.loadtxt(cov_file, dtype=float)
        self.lya_mode = lya_mode

        if lya_mode in ("joint_ap_deciding", "joint_ap_r0"):
            # Identify z=2.33 indices
            idx_dm = [i for i, (zv, q) in enumerate(zip(self.z, self.qty)) if abs(zv - 2.33) < 0.05 and "DM" in q]
            idx_dh = [i for i, (zv, q) in enumerate(zip(self.z, self.qty)) if abs(zv - 2.33) < 0.05 and "DH" in q]
            assert len(idx_dm) == 1 and len(idx_dh) == 1, "Could not locate unique z=2.33 Lya DM and DH rows"
            idm, idh = idx_dm[0], idx_dh[0]
            # Replace mean values per PREREG.md Section 5.1:
            # D_H(2.33)/r_d = 8.600 +- 0.066, D_M(2.33)/r_d = 39.32 +- 0.33
            self.mean[idm] = 39.32
            self.mean[idh] = 8.600
            sig_dm = 0.33
            sig_dh = 0.066
            r_corr = -0.431 if lya_mode == "joint_ap_deciding" else 0.0
            # Zero any cross-covariance with other tracers (already 0 in desi_bao_dr2) and set 2x2 block
            self.cov[idm, :] = 0.0
            self.cov[:, idm] = 0.0
            self.cov[idh, :] = 0.0
            self.cov[:, idh] = 0.0
            self.cov[idm, idm] = sig_dm ** 2
            self.cov[idh, idh] = sig_dh ** 2
            self.cov[idm, idh] = r_corr * sig_dm * sig_dh
            self.cov[idh, idm] = r_corr * sig_dm * sig_dh

        self.inv_cov = linalg.inv(self.cov)
        self.unique_z = np.unique(self.z)
        self.z_idx_map = [int(np.where(self.unique_z == zv)[0][0]) for zv in self.z]

    def _model_vector(self, DM_u, DH_u, rd):
        pred = np.empty_like(self.mean)
        for i, (q, uidx) in enumerate(zip(self.qty, self.z_idx_map)):
            dm = DM_u[uidx]
            dh = DH_u[uidx]
            zv = self.z[i]
            if q == "DV_over_rs":
                dv = ((zv * (dm ** 2) * dh) ** (1.0 / 3.0))
                pred[i] = dv / rd
            elif q == "DM_over_rs":
                pred[i] = dm / rd
            elif q == "DH_over_rs":
                pred[i] = dh / rd
            else:
                raise ValueError(f"Unknown BAO quantity: {q}")
        return pred

    def chi2_cpl(self, Omega_m_tot, h, omega_b, w0=-1.0, wa=0.0, rd_override=None):
        DM_u, DH_u = comoving_distances_cpl(self.unique_z, Omega_m_tot, h, w0=w0, wa=wa)
        if DM_u is None:
            return np.inf
        if rd_override is not None:
            rd = rd_override
        else:
            rd = r_drag_mpc(omega_b, Omega_m_tot * (h ** 2))
        pred = self._model_vector(DM_u, DH_u, rd)
        diff = pred - self.mean
        return float(diff @ self.inv_cov @ diff)

    def chi2_law1(self, Omega_m_tot, h, omega_b, gamma_u, spl_E=None):
        if spl_E is None:
            DM_u, DH_u, spl_E = comoving_distances_law1(self.unique_z, Omega_m_tot, h, gamma_u)
        else:
            z_max = float(np.max(self.unique_z))
            z_grid = np.linspace(0.0, z_max, 301)
            E_grid = spl_E(-np.log(1.0 + z_grid))
            inv_E_spl = interpolate.CubicSpline(z_grid, 1.0 / E_grid)
            dh0 = C_KM_S / (100.0 * h)
            DM_u = dh0 * inv_E_spl.antiderivative()(self.unique_z)
            DH_u = dh0 / spl_E(-np.log(1.0 + self.unique_z))
        if DM_u is None:
            return np.inf, None
        rd = r_drag_mpc(omega_b, Omega_m_tot * (h ** 2))
        pred = self._model_vector(DM_u, DH_u, rd)
        diff = pred - self.mean
        return float(diff @ self.inv_cov @ diff), spl_E


class PantheonPlusLikelihood:
    """Pantheon+ cosmology likelihood (z_HD > 0.01, IS_CALIBRATOR == 0, full STAT+SYS covariance,
    analytically marginalized over nuisance offset M per PREREG.md Section 5.1).
    """

    def __init__(self, data_dir):
        dat_path = os.path.join(data_dir, "pantheon_plus", "Pantheon+SH0ES.dat")
        cov_path = os.path.join(data_dir, "pantheon_plus", "Pantheon+SH0ES_STAT+SYS.cov")

        with open(dat_path, "r", encoding="utf-8") as f:
            header = f.readline().strip().split()
            rows = [line.strip().split() for line in f if line.strip()]

        col_zhd = header.index("zHD")
        col_zhel = header.index("zHEL")
        col_mb = header.index("m_b_corr")
        col_calib = header.index("IS_CALIBRATOR")

        zhd_all = np.array([float(r[col_zhd]) for r in rows], dtype=float)
        zhel_all = np.array([float(r[col_zhel]) for r in rows], dtype=float)
        mb_all = np.array([float(r[col_mb]) for r in rows], dtype=float)
        calib_all = np.array([int(r[col_calib]) for r in rows], dtype=int)

        mask = (zhd_all > 0.01) & (calib_all == 0)
        self.mask = mask
        self.z_hd = zhd_all[mask]
        self.z_hel = zhel_all[mask]
        self.m_obs = mb_all[mask]
        self.n_sn = int(np.sum(mask))

        # Load full covariance matrix (first line is N=1701)
        raw = np.loadtxt(cov_path, dtype=float)
        n_tot = int(round(raw[0]))
        cov_full = raw[1:].reshape((n_tot, n_tot))
        cov_sub = cov_full[np.ix_(mask, mask)]

        # Precompute inverse covariance and 1^T C^-1 1 for fast analytical marginalization over M
        self.inv_cov = linalg.inv(cov_sub, check_finite=False)
        ones = np.ones(self.n_sn, dtype=float)
        self.cinv_ones = self.inv_cov @ ones
        self.ones_cinv_ones = float(np.dot(ones, self.cinv_ones))
        self.z_max = float(np.max(self.z_hd))
        self.z_grid = np.linspace(0.0, self.z_max * 1.01, 351)

    def _chi2_from_Iz(self, I_z):
        mu_shape = 5.0 * np.log10((1.0 + self.z_hel) * I_z)
        delta = self.m_obs - mu_shape
        cinv_delta = self.inv_cov @ delta
        a_term = float(np.dot(delta, cinv_delta))
        b_term = float(np.dot(delta, self.cinv_ones))
        return a_term - (b_term * b_term) / self.ones_cinv_ones

    def _chi2_from_E_grid(self, E_grid):
        if E_grid is None or np.any(E_grid <= 0.0):
            return np.inf
        inv_E_spl = interpolate.CubicSpline(self.z_grid, 1.0 / E_grid)
        I_z = inv_E_spl.antiderivative()(self.z_hd)
        return self._chi2_from_Iz(I_z)

    def chi2_cpl(self, Omega_m_tot, h, w0=-1.0, wa=0.0):
        E_grid = E_of_z_cpl(self.z_grid, Omega_m_tot, h, w0=w0, wa=wa)
        return self._chi2_from_E_grid(E_grid)

    def chi2_law1(self, Omega_m_tot, h, gamma_u, spl_E=None):
        if spl_E is None:
            spl_E = solve_law1_de_grid(Omega_m_tot, h, gamma_u, z_max=1150.0, n_steps=1000)
        if spl_E is None:
            return np.inf
        E_grid = spl_E(-np.log(1.0 + self.z_grid))
        return self._chi2_from_E_grid(E_grid)


class DESDovekieLikelihood:
    """DES-Dovekie 5-year SN likelihood from des-science/DES-SN5YR/4_DISTANCES_COVMAT
    (DES-Dovekie_HD.csv + STAT+SYS.npz, following official DES-Dovekie-SN_Likelihood.py,
    analytically marginalized over nuisance offset M per PREREG.md Section 5.1).
    """

    def __init__(self, data_dir):
        hd_path = os.path.join(data_dir, "des_dovekie", "DES-Dovekie_HD.csv")
        cov_path = os.path.join(data_dir, "des_dovekie", "STAT+SYS.npz")

        with open(hd_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]
        # Find header line starting with VARNAMES: or column names
        header_idx = 0
        for i, ln in enumerate(lines):
            if "zHD" in ln:
                header_idx = i
                break
        header = lines[header_idx].replace("VARNAMES:", "").replace(",", " ").split()
        col_zhd = header.index("zHD")
        col_zhel = header.index("zHEL")
        col_mu = header.index("MU")
        col_muerr = header.index("MUERR") if "MUERR" in header else header.index("MUERR_FINAL")

        data_rows = []
        for ln in lines[header_idx + 1 :]:
            if ln.startswith("SN:"):
                ln = ln[3:].strip()
            parts = ln.replace(",", " ").split()
            if len(parts) >= len(header):
                data_rows.append(parts)

        self.z_hd = np.array([float(r[col_zhd]) for r in data_rows], dtype=float)
        self.z_hel = np.array([float(r[col_zhel]) for r in data_rows], dtype=float)
        self.mu_obs = np.array([float(r[col_mu]) for r in data_rows], dtype=float)
        self.mu_err = np.array([float(r[col_muerr]) for r in data_rows], dtype=float)
        self.n_sn = len(self.z_hd)

        # Load STAT+SYS.npz exactly as in DES-Dovekie-SN_Likelihood.py (lines 77-85):
        # Covtot_inv is stored directly in upper triangular format in d['cov'].
        npz = np.load(cov_path)
        nsn_npz = int(npz[npz.files[0]][0]) if np.ndim(npz[npz.files[0]]) > 0 else int(npz[npz.files[0]])
        assert nsn_npz == self.n_sn, f"Mismatch between HD ({self.n_sn}) and npz ({nsn_npz})"
        inv_cov_mat = np.zeros((self.n_sn, self.n_sn), dtype=float)
        inv_cov_mat[np.triu_indices(self.n_sn)] = npz[npz.files[1]]
        inv_cov_mat[np.tril_indices(self.n_sn, -1)] = inv_cov_mat.T[np.tril_indices(self.n_sn, -1)]
        self.inv_cov = inv_cov_mat
        self.use_cho = False
        ones = np.ones(self.n_sn, dtype=float)
        self.cinv_ones = self.inv_cov @ ones
        self.ones_cinv_ones = float(np.dot(ones, self.cinv_ones))

        self.z_max = float(np.max(self.z_hd))
        self.z_grid = np.linspace(0.0, self.z_max * 1.01, 301)

    def _chi2_from_Iz(self, I_z):
        mu_shape = 5.0 * np.log10((1.0 + self.z_hel) * I_z)
        delta = self.mu_obs - mu_shape
        cinv_delta = self.inv_cov @ delta
        a_term = float(np.dot(delta, cinv_delta))
        b_term = float(np.dot(delta, self.cinv_ones))
        return a_term - (b_term * b_term) / self.ones_cinv_ones

    def _chi2_from_E_grid(self, E_grid):
        if E_grid is None or np.any(E_grid <= 0.0):
            return np.inf
        inv_E_spl = interpolate.CubicSpline(self.z_grid, 1.0 / E_grid)
        I_z = inv_E_spl.antiderivative()(self.z_hd)
        return self._chi2_from_Iz(I_z)

    def chi2_cpl(self, Omega_m_tot, h, w0=-1.0, wa=0.0):
        E_grid = E_of_z_cpl(self.z_grid, Omega_m_tot, h, w0=w0, wa=wa)
        return self._chi2_from_E_grid(E_grid)

    def chi2_law1(self, Omega_m_tot, h, gamma_u, spl_E=None):
        if spl_E is None:
            spl_E = solve_law1_de_grid(Omega_m_tot, h, gamma_u, z_max=1150.0, n_steps=1000)
        if spl_E is None:
            return np.inf
        E_grid = spl_E(-np.log(1.0 + self.z_grid))
        return self._chi2_from_E_grid(E_grid)


_SHARED_Z_GRID = np.concatenate([
    np.linspace(0.0, 3.0, 1001),
    np.logspace(np.log10(3.0), np.log10(1150.0), 401)[1:],
])
_SHARED_X_GRID = -np.log(1.0 + _SHARED_Z_GRID)
_SHARED_DZ = np.diff(_SHARED_Z_GRID)
_SHARED_HALF_DZ = 0.5 * _SHARED_DZ
_SHARED_DZ2_12 = (_SHARED_DZ ** 2) / 12.0
_SHARED_SPAN_2 = _SHARED_Z_GRID[2:] - _SHARED_Z_GRID[:-2]


def _fast_cum_integral_inv_E(inv_E: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Compute 4th-order cubic-Hermite cumulative integral I(z) = int_0^z dz'/E(z')
    on _SHARED_Z_GRID in pure vectorized NumPy (< 20 us per call, < 1e-9 accuracy).
    """
    yp = np.empty_like(inv_E)
    yp[1:-1] = (inv_E[2:] - inv_E[:-2]) / _SHARED_SPAN_2
    yp[0] = (inv_E[1] - inv_E[0]) / _SHARED_DZ[0]
    yp[-1] = (inv_E[-1] - inv_E[-2]) / _SHARED_DZ[-1]

    dI = _SHARED_HALF_DZ * (inv_E[:-1] + inv_E[1:]) + _SHARED_DZ2_12 * (yp[:-1] - yp[1:])
    cum_I = np.empty_like(inv_E)
    cum_I[0] = 0.0
    np.cumsum(dI, out=cum_I[1:])
    return cum_I, inv_E


def _eval_cum_integral_at(z_targets: np.ndarray, cum_I: np.ndarray, inv_E: np.ndarray, idx: np.ndarray, u: np.ndarray, dz_idx: np.ndarray) -> np.ndarray:
    """Evaluate I(z_targets) using precomputed grid indices idx and fractional offsets u."""
    y0 = inv_E[idx]
    y1 = inv_E[idx + 1]
    return cum_I[idx] + dz_idx * (u * y0 + 0.5 * (u * u) * (y1 - y0))


_SHARED_X_DX = np.diff(_SHARED_X_GRID)
_SHARED_X_HALF = 0.5 * (_SHARED_X_GRID[:-1] + _SHARED_X_GRID[1:])
_SHARED_A_GRID = np.exp(_SHARED_X_GRID)
_SHARED_A_HALF = np.exp(_SHARED_X_HALF)
_SHARED_A_M4 = _SHARED_A_GRID ** -4
_SHARED_A_M3 = _SHARED_A_GRID ** -3
_SHARED_AH_M4 = _SHARED_A_HALF ** -4
_SHARED_AH_M3 = _SHARED_A_HALF ** -3
_SHARED_ONU_GRID = omega_nu_h2_of_a(_SHARED_A_GRID)
_SHARED_ONU_HALF = omega_nu_h2_of_a(_SHARED_A_HALF)
_SHARED_NU_REL_COEFF = OMEGA_GAMMA_H2 * (7.0 / 8.0) * ((4.0 / 11.0) ** (4.0 / 3.0)) * (2.0 * N_EFF / 3.0)


def _ensure_grid_lookup(obj, z_arr: np.ndarray):
    if not hasattr(obj, "_shared_idx"):
        idx = np.clip(np.searchsorted(_SHARED_Z_GRID, z_arr) - 1, 0, len(_SHARED_Z_GRID) - 2)
        dz_idx = _SHARED_DZ[idx]
        u = (z_arr - _SHARED_Z_GRID[idx]) / dz_idx
        obj._shared_idx = idx
        obj._shared_dz = dz_idx
        obj._shared_u = u


def _eval_scalar_cum_integral(z_val: float, cum_I: np.ndarray, inv_E: np.ndarray) -> float:
    idx = int(np.searchsorted(_SHARED_Z_GRID, z_val) - 1)
    idx = max(0, min(idx, len(_SHARED_Z_GRID) - 2))
    dz = float(_SHARED_DZ[idx])
    u = (z_val - float(_SHARED_Z_GRID[idx])) / dz
    y0 = float(inv_E[idx])
    y1 = float(inv_E[idx + 1])
    return float(cum_I[idx]) + dz * (u * y0 + 0.5 * (u * u) * (y1 - y0))


def joint_chi2_cpl(
    Omega_m_tot: float,
    h: float,
    wb100: float,
    w0: float,
    wa: float,
    bao_like: DESIBAOLikelihood,
    cmb_like: CMBLikelihood | None,
    sn_like: PantheonPlusLikelihood | DESDovekieLikelihood | None,
    bbn_prior: tuple[float, float] | None = None,
) -> float:
    """
    Fast vectorized joint chi2 evaluation for flat CPL / LCDM across BAO + CMB + SNe + BBN.
    """
    omega_b = wb100 / 100.0
    h2 = h * h
    omega_m = Omega_m_tot * h2
    Omega_gamma = OMEGA_GAMMA_H2 / h2
    Omega_nu_0 = OMEGA_NU_MASS_H2 / h2
    Omega_bc = Omega_m_tot - Omega_nu_0
    Omega_de = 1.0 - (Omega_gamma + (_SHARED_NU_REL_COEFF / h2) + Omega_nu_0 + Omega_bc)

    if w0 == -1.0 and wa == 0.0:
        g_de = 1.0
    else:
        g_de = (_SHARED_A_GRID ** (-3.0 * (1.0 + w0 + wa))) * np.exp(-3.0 * wa * (1.0 - _SHARED_A_GRID))

    e2_grid = Omega_gamma * _SHARED_A_M4 + (_SHARED_ONU_GRID / h2) + Omega_bc * _SHARED_A_M3 + Omega_de * g_de
    if np.any(e2_grid <= 0.0):
        return np.inf
    E_grid = np.sqrt(e2_grid)
    cum_I, inv_E = _fast_cum_integral_inv_E(1.0 / E_grid)
    dh0 = C_KM_S / (100.0 * h)

    # 1. BAO chi2
    _ensure_grid_lookup(bao_like, bao_like.unique_z)
    I_bao = _eval_cum_integral_at(bao_like.unique_z, cum_I, inv_E, bao_like._shared_idx, bao_like._shared_u, bao_like._shared_dz)
    DM_u = dh0 * I_bao
    E_u = E_of_z_cpl(bao_like.unique_z, Omega_m_tot, h, w0=w0, wa=wa)
    if E_u is None:
        return np.inf
    DH_u = dh0 / E_u
    rd = r_drag_mpc(omega_b, omega_m)
    pred_bao = bao_like._model_vector(DM_u, DH_u, rd)
    diff_bao = pred_bao - bao_like.mean
    chi2_tot = float(diff_bao @ bao_like.inv_cov @ diff_bao)

    # 2. CMB chi2
    if cmb_like is not None:
        z_star = z_star_hu_sugiyama(omega_b, omega_m)
        DM_star = dh0 * _eval_scalar_cum_integral(z_star, cum_I, inv_E)
        R_shift = math.sqrt(Omega_m_tot) * (DM_star / dh0)
        rs_star = sound_horizon_rs_chen(z_star, omega_b, omega_m)
        l_A = math.pi * DM_star / rs_star
        chi2_tot += cmb_like.chi2(np.array([R_shift, l_A, wb100], dtype=float))

    # 3. SN chi2
    if sn_like is not None:
        _ensure_grid_lookup(sn_like, sn_like.z_hd)
        I_z = _eval_cum_integral_at(sn_like.z_hd, cum_I, inv_E, sn_like._shared_idx, sn_like._shared_u, sn_like._shared_dz)
        chi2_tot += sn_like._chi2_from_Iz(I_z)

    # 4. External BBN prior on 100*omega_b
    if bbn_prior is not None:
        mu_bbn, sig_bbn = bbn_prior
        chi2_tot += ((wb100 - mu_bbn) / sig_bbn) ** 2

    return float(chi2_tot)


def joint_chi2_law1(
    Omega_m_tot: float,
    h: float,
    wb100: float,
    gamma_u: float,
    bao_like: DESIBAOLikelihood,
    cmb_like: CMBLikelihood | None,
    sn_like: PantheonPlusLikelihood | DESDovekieLikelihood | None,
    bbn_prior: tuple[float, float] | None = None,
) -> float:
    """
    Fast vectorized joint chi2 evaluation for Law 1 (w(a) = -1 + gamma_u / E(a))
    across BAO + CMB + SNe + BBN.
    """
    omega_b = wb100 / 100.0
    h2 = h * h
    omega_m = Omega_m_tot * h2
    Omega_gamma = OMEGA_GAMMA_H2 / h2
    Omega_nu_0 = OMEGA_NU_MASS_H2 / h2
    Omega_bc = Omega_m_tot - Omega_nu_0
    Omega_de = 1.0 - (Omega_gamma + (_SHARED_NU_REL_COEFF / h2) + Omega_nu_0 + Omega_bc)
    if Omega_bc <= 0.0 or Omega_de <= 0.0:
        return np.inf

    non_de_grid = Omega_gamma * _SHARED_A_M4 + (_SHARED_ONU_GRID / h2) + Omega_bc * _SHARED_A_M3
    if abs(gamma_u) <= 1e-14:
        e2_grid = non_de_grid + Omega_de
    else:
        non_de_half = Omega_gamma * _SHARED_AH_M4 + (_SHARED_ONU_HALF / h2) + Omega_bc * _SHARED_AH_M3
        nd_g = non_de_grid.tolist()
        nd_h = non_de_half.tolist()
        dx_list = _SHARED_X_DX.tolist()
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
    cum_I, inv_E = _fast_cum_integral_inv_E(1.0 / E_grid)
    dh0 = C_KM_S / (100.0 * h)

    # 1. BAO chi2
    _ensure_grid_lookup(bao_like, bao_like.unique_z)
    I_bao = _eval_cum_integral_at(bao_like.unique_z, cum_I, inv_E, bao_like._shared_idx, bao_like._shared_u, bao_like._shared_dz)
    DM_u = dh0 * I_bao
    # Linear interpolation of inv_E at bao_like.unique_z (dz = 0.003 -> < 1e-7 accuracy)
    inv_E_bao = (1.0 - bao_like._shared_u) * inv_E[bao_like._shared_idx] + bao_like._shared_u * inv_E[bao_like._shared_idx + 1]
    DH_u = dh0 * inv_E_bao
    rd = r_drag_mpc(omega_b, omega_m)
    pred_bao = bao_like._model_vector(DM_u, DH_u, rd)
    diff_bao = pred_bao - bao_like.mean
    chi2_tot = float(diff_bao @ bao_like.inv_cov @ diff_bao)

    # 2. CMB chi2
    if cmb_like is not None:
        z_star = z_star_hu_sugiyama(omega_b, omega_m)
        DM_star = dh0 * _eval_scalar_cum_integral(z_star, cum_I, inv_E)
        R_shift = math.sqrt(Omega_m_tot) * (DM_star / dh0)
        rs_star = sound_horizon_rs_chen(z_star, omega_b, omega_m)
        l_A = math.pi * DM_star / rs_star
        chi2_tot += cmb_like.chi2(np.array([R_shift, l_A, wb100], dtype=float))

    # 3. SN chi2
    if sn_like is not None:
        _ensure_grid_lookup(sn_like, sn_like.z_hd)
        I_z = _eval_cum_integral_at(sn_like.z_hd, cum_I, inv_E, sn_like._shared_idx, sn_like._shared_u, sn_like._shared_dz)
        chi2_tot += sn_like._chi2_from_Iz(I_z)

    # 4. External BBN prior on 100*omega_b
    if bbn_prior is not None:
        mu_bbn, sig_bbn = bbn_prior
        chi2_tot += ((wb100 - mu_bbn) / sig_bbn) ** 2

    return float(chi2_tot)
