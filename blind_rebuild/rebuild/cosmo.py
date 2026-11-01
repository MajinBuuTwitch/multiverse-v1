"""cosmo.py -- background cosmology for the blind rebuild (own code, written from MULTIVERSE_STAGE1_EQUATIONS.md).

Production numerics (independent route, see REBUILD_RESULTS.md "Method choices"):
  * E(a) from the Friedmann equation (a2) with photons, 2 massless + 1 massive (0.06 eV) neutrino
    (exact Fermi-Dirac shape), pressureless Omega_bc, and dark energy g(a).
  * Law 1 dark energy: d ln g / d ln a = -3 gamma_u / E(a), g(1)=1, integrated with classical RK4 on the
    registered 1000-point log-a grid (a in [1e-4, 1]); ln g is held constant below a=1e-4.
  * Distances: the ODE d chi/dz = 1/E(z) integrated with fixed-step RK4 (nodes + midpoints) on a uniform
    z grid (late times) and a uniform ln(1+z) grid (out to z_*); cubic Hermite interpolation (chi, chi'=1/E).
  * Sound horizon: ODE d r_s/da = c_s/(a^2 H) integrated with fixed-step RK4 on a uniform grid in a from 0.
  * z_* : Hu & Sugiyama (1996) fit; z_d : Eisenstein & Hu (1998) fit, r_d calibrated by one constant
    factor computed once with CAMB (see calibrate_rd.py and DEVIATIONS_REBUILD.md D3).
Validation of these routines against scipy solve_ivp (DOP853) and Gauss-Legendre quadrature: validate_cosmo.py.
"""
import math
import numpy as np

C_KMS = 299792.458
OMEGA_GAMMA_H2 = 2.4728e-5          # registered (T_CMB = 2.7255 K)
T_CMB = 2.7255
N_EFF = 3.044
M_NU = 0.06                          # eV, one massive eigenstate
NU93 = 93.14                         # registered Omega_nu,0 = 0.06 / (93.14 h^2)
K_B_EV = 8.617333262e-5              # eV / K
# per-species massless neutrino density relative to photons (N_eff spread over 3 species)
NU_PER_SPECIES = (7.0 / 8.0) * (4.0 / 11.0) ** (4.0 / 3.0) * (N_EFF / 3.0)
T_NU0 = (4.0 / 11.0) ** (1.0 / 3.0) * (N_EFF / 3.0) ** 0.25 * T_CMB   # K
Y_NU = M_NU / (K_B_EV * T_NU0)       # m / (k T_nu0)

RD_CALIB = None                      # set by load_rd_calibration()


# ---------------------------------------------------------------- neutrinos (exact Fermi-Dirac shape)
def _fd_energy_integral(Y):
    """F(Y) = int_0^inf x^2 sqrt(x^2+Y^2)/(e^x+1) dx (Gauss-Laguerre-like via dense trapezoid in x)."""
    x = np.linspace(1e-6, 60.0, 60001)
    w = x ** 2 / (np.exp(x) + 1.0)
    Y = np.atleast_1d(Y)
    out = np.array([np.trapezoid(w * np.sqrt(x ** 2 + y ** 2), x) for y in Y])
    return out

_LNY_GRID = np.linspace(math.log(1e-6), math.log(2e4), 4000)
_F_GRID = _fd_energy_integral(np.exp(_LNY_GRID))
_LNF_GRID = np.log(_F_GRID)
_F_TODAY = float(np.exp(np.interp(math.log(Y_NU), _LNY_GRID, _LNF_GRID)))


def nu_mass_shape(a):
    """f_nu(a) = rho_nu,mass(a)/rho_nu,mass(1): a^-4 F(Y a)/F(Y)."""
    a = np.asarray(a, dtype=float)
    lnY = np.log(np.maximum(Y_NU * a, 1e-300))
    F = np.where(lnY < _LNY_GRID[0], _F_GRID[0],
                 np.exp(np.interp(lnY, _LNY_GRID, _LNF_GRID)))
    # beyond the grid top use non-relativistic limit F ~ Y * (3/2) zeta(3)
    big = lnY > _LNY_GRID[-1]
    if np.any(big):
        F = np.where(big, np.exp(lnY) * 1.5 * 1.2020569031595942, F)
    return F / _F_TODAY / a ** 4


# ---------------------------------------------------------------- parameters
class Params:
    """Flat cosmology.  Om = Omega_m,tot (b + c + massive nu today); h; ombh2; DE model."""
    __slots__ = ("Om", "h", "ombh2", "model", "w0", "wa", "gam", "Or", "Onu", "Obc", "Ode",
                 "_lng_x", "_lng_y")

    def __init__(self, Om, h, ombh2, model="lcdm", w0=-1.0, wa=0.0, gam=0.0):
        self.Om, self.h, self.ombh2 = float(Om), float(h), float(ombh2)
        self.model, self.w0, self.wa, self.gam = model, float(w0), float(wa), float(gam)
        h2 = self.h * self.h
        self.Or = OMEGA_GAMMA_H2 * (1.0 + 2.0 * NU_PER_SPECIES) / h2   # photons + 2 massless nu
        self.Onu = M_NU / (NU93 * h2)
        self.Obc = self.Om - self.Onu
        self.Ode = 1.0 - self.Or - self.Om
        self._lng_x = None
        if model == "law1":
            self._solve_law1()

    # non-dark-energy part of E^2
    def E2_nonde(self, a):
        return self.Or / a ** 4 + self.Onu * nu_mass_shape(a) + self.Obc / a ** 3

    def lng(self, a):
        a = np.asarray(a, dtype=float)
        if self.model == "lcdm":
            return np.zeros_like(a)
        if self.model == "cpl":
            return -3.0 * (1.0 + self.w0 + self.wa) * np.log(a) - 3.0 * self.wa * (1.0 - a)
        if self.model == "law1":
            x = np.log(a)
            xs, ys = self._lng_x, self._lng_y      # ascending in x
            y = np.interp(np.clip(x, xs[0], 0.0), xs, ys)
            return y
        raise ValueError(self.model)

    def E2(self, a):
        return self.E2_nonde(a) + self.Ode * np.exp(self.lng(a))

    def E(self, a):
        return np.sqrt(self.E2(a))

    # ---- Law 1: RK4 on the registered 1000-point log-a grid, integrated from a=1 backwards
    def _solve_law1(self, n=1000, amin=1e-4):
        x = np.linspace(0.0, math.log(amin), n)            # descending ln a
        hstep = x[1] - x[0]                                 # negative
        xm = x[:-1] + 0.5 * hstep
        A_nodes = self.E2_nonde(np.exp(x))
        A_mid = self.E2_nonde(np.exp(xm))
        Ode, g3 = self.Ode, -3.0 * self.gam
        y = np.empty(n)
        y[0] = 0.0
        yy = 0.0
        sq, ex = math.sqrt, math.exp
        An = A_nodes.tolist(); Am = A_mid.tolist()
        for i in range(n - 1):
            k1 = g3 / sq(An[i] + Ode * ex(yy))
            k2 = g3 / sq(Am[i] + Ode * ex(yy + 0.5 * hstep * k1))
            k3 = g3 / sq(Am[i] + Ode * ex(yy + 0.5 * hstep * k2))
            k4 = g3 / sq(An[i + 1] + Ode * ex(yy + hstep * k3))
            yy = yy + hstep * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
            y[i + 1] = yy
        self._lng_x = x[::-1].copy()
        self._lng_y = y[::-1].copy()

    def w_of_a(self, a):
        if self.model == "lcdm":
            return -1.0 + 0 * np.asarray(a)
        if self.model == "cpl":
            return self.w0 + self.wa * (1 - np.asarray(a))
        return -1.0 + self.gam / self.E(a)


# ---------------------------------------------------------------- fitting formulae (registered)
def z_star_hs96(ombh2, omh2):
    g1 = 0.0783 * ombh2 ** -0.238 / (1.0 + 39.5 * ombh2 ** 0.763)
    g2 = 0.560 / (1.0 + 21.1 * ombh2 ** 1.81)
    return 1048.0 * (1.0 + 0.00124 * ombh2 ** -0.738) * (1.0 + g1 * omh2 ** g2)


def z_drag_eh98(ombh2, omh2):
    b1 = 0.313 * omh2 ** -0.419 * (1.0 + 0.607 * omh2 ** 0.674)
    b2 = 0.238 * omh2 ** 0.223
    return 1291.0 * omh2 ** 0.251 / (1.0 + 0.659 * omh2 ** 0.828) * (1.0 + b1 * ombh2 ** b2)


# ---------------------------------------------------------------- ODE integrators (fixed-step RK4)
def _rk4_cumulative(f_nodes, f_mid, h):
    """RK4 for y' = f(t) (RHS independent of y): increments h/6 (f0 + 4 fm + f1)."""
    inc = h / 6.0 * (f_nodes[:-1] + 4.0 * f_mid + f_nodes[1:])
    return np.concatenate(([0.0], np.cumsum(inc)))


def sound_horizon(p, z, n=600):
    """r_s(z) in Mpc: ODE d r_s/da = c_s(a) / (a^2 H(a)) from a=0 to a=1/(1+z)."""
    a_end = 1.0 / (1.0 + z)
    a = np.linspace(0.0, a_end, n + 1)
    am = 0.5 * (a[:-1] + a[1:])
    R_fac = 3.0 * p.ombh2 / (4.0 * OMEGA_GAMMA_H2)

    def f(aa):
        out = np.empty_like(aa)
        nz = aa > 0
        an = aa[nz]
        cs = 1.0 / np.sqrt(3.0 * (1.0 + R_fac * an))
        out[nz] = cs / np.sqrt(an ** 4 * p.E2(an))
        if np.any(~nz):   # a -> 0 limit: a^2 E -> sqrt(Or + Onu*F(0)/F(1)) ; c_s -> 1/sqrt(3)
            lim = p.Or + p.Onu * (_F_GRID[0] / _F_TODAY)
            out[~nz] = (1.0 / math.sqrt(3.0)) / math.sqrt(lim)
        return out

    h = a[1] - a[0]
    tot = np.sum(h / 6.0 * (f(a[:-1]) + 4.0 * f(am) + f(a[1:])))
    return tot * C_KMS / (100.0 * p.h)


def load_rd_calibration(path):
    global RD_CALIB
    import json
    RD_CALIB = json.load(open(path))["factor"]
    return RD_CALIB


def r_drag(p, calibrated=True):
    zd = z_drag_eh98(p.ombh2, p.Om * p.h * p.h)
    rs = sound_horizon(p, zd)
    if calibrated:
        if RD_CALIB is None:
            raise RuntimeError("r_d calibration not loaded")
        return rs * RD_CALIB
    return rs


class Distances:
    """chi(z) = int_0^z dz'/E(z') (units of c/H0) via fixed-step RK4 on a uniform z grid [0, zmax]."""

    def __init__(self, p, zmax=2.5, dz=0.0025):
        self.p = p
        n = int(round(zmax / dz))
        self.dz = zmax / n
        z = np.linspace(0.0, zmax, n + 1)
        zm = 0.5 * (z[:-1] + z[1:])
        invE = 1.0 / p.E(1.0 / (1.0 + z))
        invEm = 1.0 / p.E(1.0 / (1.0 + zm))
        self.z = z
        self.invE = invE
        self.chi = _rk4_cumulative(invE, invEm, self.dz)
        self.zmax = zmax

    def chi_at(self, zq):
        zq = np.asarray(zq, dtype=float)
        t = zq / self.dz
        i = np.clip(np.floor(t).astype(int), 0, len(self.z) - 2)
        s = t - i
        h = self.dz
        y0, y1 = self.chi[i], self.chi[i + 1]
        d0, d1 = self.invE[i] * h, self.invE[i + 1] * h
        h00 = 2 * s ** 3 - 3 * s ** 2 + 1; h10 = s ** 3 - 2 * s ** 2 + s
        h01 = -2 * s ** 3 + 3 * s ** 2; h11 = s ** 3 - s ** 2
        return h00 * y0 + h10 * d0 + h01 * y1 + h11 * d1

    def chi_to(self, z_far, n=400):
        """chi(z_far) for z_far > zmax: RK4 on a uniform ln(1+z) grid from zmax."""
        u0, u1 = math.log1p(self.zmax), math.log1p(z_far)
        u = np.linspace(u0, u1, n + 1)
        um = 0.5 * (u[:-1] + u[1:])
        f = lambda uu: np.exp(uu) / self.p.E(np.exp(-uu))     # dchi/du = (1+z)/E
        hstep = u[1] - u[0]
        return self.chi[-1] + np.sum(hstep / 6.0 * (f(u[:-1]) + 4 * f(um) + f(u[1:])))

    def DM(self, zq):      # Mpc
        return self.chi_at(zq) * C_KMS / (100.0 * self.p.h)

    def DH(self, zq):      # Mpc
        return C_KMS / (100.0 * self.p.h) / self.p.E(1.0 / (1.0 + np.asarray(zq)))


def cmb_observables(p, dist=None):
    """(R, l_A, 100 omega_b) with z_* from Hu & Sugiyama (registered)."""
    if dist is None:
        dist = Distances(p)
    omh2 = p.Om * p.h * p.h
    zs = z_star_hs96(p.ombh2, omh2)
    chi_s = dist.chi_to(zs)
    R = math.sqrt(p.Om) * chi_s
    DM = chi_s * C_KMS / (100.0 * p.h)
    rs = sound_horizon(p, zs)
    lA = math.pi * DM / rs
    return R, lA, 100.0 * p.ombh2, zs, rs
