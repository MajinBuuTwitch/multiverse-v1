# Neutrino / sound-horizon check (read-only) — report

**Verdict:** (i) and (ii). The as-coded treatment is deliberate and physically defensible, and it is a literal implementation of registered (a2)/(a5). The 0.06 eV neutrino is **not** left out of H(a) in the r_s(z*) integral: one exact Fermi–Dirac E²(a) is used in r_s, D_M and r_d alike, so there is no internal inconsistency.

No frozen file was edited, moved or regenerated. Nothing outside this folder was read. Files: `nu_rs_variants.py` (imports the frozen `rebuild/cosmo.py` unchanged), `nu_rs_variants.json`, `LOG.md`, this report.

## 1. Code (`rebuild/cosmo.py`)

There is a single background function, and every observable calls it:

```
26  NU_PER_SPECIES = (7.0 / 8.0) * (4.0 / 11.0) ** (4.0 / 3.0) * (N_EFF / 3.0)
71  self.Or = OMEGA_GAMMA_H2 * (1.0 + 2.0 * NU_PER_SPECIES) / h2   # photons + 2 massless nu
72  self.Onu = M_NU / (NU93 * h2)
73  self.Obc = self.Om - self.Onu
81  return self.Or / a ** 4 + self.Onu * nu_mass_shape(a) + self.Obc / a ** 3      # E2_nonde
97  return self.E2_nonde(a) + self.Ode * np.exp(self.lng(a))                       # E2
```

`nu_mass_shape(a)` returns a⁻⁴ F(Y a)/F(Y), where F(Y) = ∫ x² √(x² + Y²)/(eˣ + 1) dx and Y = m_ν/(k T_ν0). This is the exact Fermi–Dirac energy density, relativistic at early times and non-relativistic today.

How the massive neutrino enters each function:

| Function | Line(s) building H / E | How the massive ν enters |
|---|---|---|
| `sound_horizon(p, z)` → r_s(z*) and r_d | `165  out[nz] = cs / np.sqrt(an ** 4 * p.E2(an))`; a = 0 node: `167  lim = p.Or + p.Onu * (_F_GRID[0] / _F_TODAY)` | Full Fermi–Dirac, through `p.E2` (the a → 0 limit uses the relativistic F(0)) |
| `Distances` → D_M(z) for z ≤ 2.5 | `invE = 1.0 / p.E(1.0 / (1.0 + z))` | Full Fermi–Dirac (`p.E` = √`p.E2`) |
| `Distances.chi_to` → D_M(z*) | `226  f = lambda uu: np.exp(uu) / self.p.E(np.exp(-uu))` | Full Fermi–Dirac |
| `z_star_hs96(ombh2, omh2)`, called with `241  omh2 = p.Om * p.h * p.h` | fitting formula, no H(a) | As non-relativistic matter: ω_m = (Ω_bc + Ω_ν,0) h², as registered |
| `z_drag_eh98(ombh2, omh2)`, called from `r_drag` with `p.Om * p.h * p.h` | fitting formula, no H(a) | As non-relativistic matter in ω_m, as registered |
| `r_drag(p)` | `185  rs = sound_horizon(p, zd)`, then × F = 0.975772 (D3) | Full Fermi–Dirac in the integral; ω_m including ν in z_d |
| `cmb_observables`, R | `244  R = math.sqrt(p.Om) * chi_s` | Ω_m,tot includes Ω_ν,0 (registered) |

Normalisation check (from `nu_rs_variants.json`):
- At z* (Y·a = 0.326, so the species is still mostly relativistic), the massive species' density is 1.0065× one massless species.
- In the early-time limit it is 0.9990×. The 0.1% gap comes from the registered 93.14 eV normalisation against the N_eff = 3.044 temperature. It is negligible.

## 2. Rulebook

- **(a2), MULTIVERSE_STAGE1_EQUATIONS.md (Tier 1):** "E²(a) = Ω_γ a⁻⁴ + Ω_ν f_ν(a) + Ω_bc a⁻³ + Ω_de g(a)". Here Ω_ν f_ν(a) describes "standard cosmic neutrinos with N_eff = 3.044 and Σm_ν = 0.06 eV (modeled with one massive eigenstate … Ω_ν,mass,0 = 0.06/(93.14 h²), and two massless eigenstates, using the exact Fermi–Dirac phase-space integral f_ν(a))".
- **(a5):** "r_s(z) = ∫_z^∞ c_s(z′)/H(z′) dz′, c_s = c/√(3(1 + 3ω_b/(4ω_γ(1+z)))), r_d ≡ r_s(z_d)". z* is the Hu & Sugiyama fit and z_d the Eisenstein & Hu fit, "where ω_m ≡ Ω_m,tot h² = (Ω_bc + Ω_ν,0) h²". R = √Ω_m,tot ∫₀^{z*} dz′/E(z′) and ℓ_A = π D_M(z*)/r_s(z*).
- **ASSUMPTIONS [A2]:** N_eff = 3.044, Σm_ν = 0.06 eV, one massive and two massless eigenstates with the exact Fermi–Dirac integral. It "Drives: Equation (a2), sound horizon r_s(z) and fitting formulas z*, z_d in (a5)".
- **PREREG §2 G9-b** names the gate "Compressed CMB Prior & r_s(z*) Validation" and adds no neutrino rule.
- **Match:** literal. The H(z) inside the (a5) r_s integral is the (a2) H, which contains Ω_ν f_ν(a) with the exact Fermi–Dirac shape. ω_m in the fitting formulas includes Ω_ν,0 exactly as (a5) defines it. The only "mixed" element is the fitting formulas treating ν as matter, and that is written into (a5) itself.

## 3. Numbers (C1: h = 0.6736, ω_b = 0.02237, ω_c = 0.1200, 0.06 eV)

Only the E²(a) inside the r_s integrand changes between variants. z* = 1091.9081 (HS96 with ω_m = 0.1430142, including ω_ν = 0.000644) and D_M(z*) = 13873.200 Mpc are as coded in all rows. σ(ℓ_A) = 0.090.

| Variant (r_s integrand) | r_s(z*) [Mpc] | ℓ_A | Δr_s vs (a) | Δℓ_A vs (a) | Δℓ_A / σ |
|---|---|---|---|---|---|
| (a) as coded: exact Fermi–Dirac | 144.2763 | 302.0867 | 0 | 0 | 0 |
| (b) ν as non-relativistic matter (a⁻³) instead of Fermi–Dirac | 149.4110 | 291.7051 | +5.1347 | −10.3816 | −115.35 |
| (c) ν as fully relativistic (one massless species) | 144.2775 | 302.0841 | +0.0012 | −0.0026 | −0.028 |
| (d) ν left out entirely (reviewer's hypothesis) | 149.5866 | 291.3627 | +5.3103 | −10.7240 | −119.16 |

**ANSWER_KEY.json check.** The C1 universe U-YIG4 (noiseless) records r_s_zstar = 144.27626950, z_star = 1091.90811074 and l_A = 302.08669904. Variant (a) reproduces these to 1.4e-10 Mpc, 0 and 2.9e-10 respectively; r_d = 147.10270 also matches exactly.

**Independent check (already frozen, `results_rebuild/validation/g9b_bugcheck.json`).** At the Planck mean point, CAMB 2.0.5 (full massive-neutrino treatment) gives r_s(z*) = 144.22535 Mpc against the rebuild's 144.23236, a difference of 0.0070 Mpc (4.9e-5). D_M(z*) agrees to 2.6e-6.

Reading the table: removing the neutrino from the r_s integrand, as in (d), would move r_s by +5.3 Mpc, about 22× the reviewer's +0.242 Mpc, and would break the CAMB agreement by about 760×. The data therefore exclude the hypothesis that ν is left out.

The reviewer's +0.242 Mpc is about the size of counting ω_ν = 0.000644 a second time as matter on top of a relativistic species (δω_m/ω_m ≈ 0.45% acting on the matter part of H near z*). That would happen if their reference counted all N_eff = 3.044 as radiation and also put ω_ν in ω_m. **This explanation is not verified here:** the confirmatory variant was blocked by the workspace's delete guard (see LOG.md) and was not run another way.

## 4. Verdict

**(i) deliberate and physically defensible, and (ii) a literal reading of (a5).** It is not (iii).

- **Physics.** At z* ≈ 1090 a 0.06 eV neutrino has m/(kT_ν) ≈ 0.33, so it is close to relativistic but slightly heavier. The exact Fermi–Dirac shape gives it 1.0065× the energy density of a massless species there. That is what Boltzmann codes do, and CAMB agrees to 0.007 Mpc.
- **Consistency.** The same E²(a) feeds r_s, D_M and r_d, so the treatment is internally consistent.
- **The one debatable element** is that the HS96 and EH98 fitting formulas take ω_m including ω_ν as if it were matter. This is the registered definition in (a5), not a code choice. Its effect on z* is the fitting formula's own convention.

## 5. Impact recomputation

Not performed. It is required only for verdict (iii).

On Phase 3: the mocks and any rebuild-side analysis of them use this same `cosmo.E2`, so rebuild-side Reading A is self-consistent by construction (noiseless χ²_CMB ≈ 3e-10 for C1). An analyser whose forward model treats ν differently, for example as variant (d) or (b), would see an ℓ_A offset of about −10 (more than 100σ) against these mocks. That would be a model mismatch in the analyser, not a mock defect.
