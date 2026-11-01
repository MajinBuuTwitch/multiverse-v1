import json, statistics as st, sys
R = json.load(open(sys.argv[1]))['universes']
K = json.load(open(sys.argv[2]))
T = K['truths']
U = {u['universe_id']: u for u in K['universes']}
by = {}
for uid, u in U.items(): by.setdefault(u['truth'], []).append(uid)
for k in by: by[k].sort(key=lambda x: U[x]['round'])
out = []
def P(*a): out.append(' '.join(str(x) for x in a))

def s1(label, vals, truth):
    # vals: list of (mean, std, ci95)
    n = len(vals); inside = sum(1 for m, s, ci in vals if ci[0] <= truth <= ci[1])
    bias = st.mean(m for m, s, ci in vals) - truth; msig = st.mean(s for m, s, ci in vals)
    ok = inside >= n - 1 and abs(bias) < msig
    P(f"  S1 {label:45s} truth={truth:<10.5g} inside95={inside}/{n} bias={bias:+.4g} meanσ={msig:.4g} |bias|/σ={abs(bias)/msig:.2f} -> {'PASS' if ok else 'MISS'}")
    return ok

res = {}
P("=== S1 COSMO ===")
for tr, model_fit, params in [('C1', 'Law1', ['Omega_bc', 'h', '100_omega_b', 'gamma_u']),
                              ('C2', 'Law1', ['Omega_bc', 'h', '100_omega_b', 'gamma_u']),
                              ('C1', 'CPL', ['w0', 'wa']), ('C3', 'CPL', ['w0', 'wa']),
                              ('C1', 'T2A_CPL', ['Omega_bc']), ('C2', 'T2A_CPL', ['Omega_bc']), ('C3', 'T2A_CPL', ['Omega_bc'])]:
    t = T[tr]
    tv = {'Omega_bc': t['Obc'], 'h': t['h'], '100_omega_b': t['wb100'], 'gamma_u': t.get('gam', 0.0),
          'w0': t.get('w0', -1.0), 'wa': t.get('wa', 0.0)}
    for rd in ('Reading_B', 'Reading_A'):
        for sn in ('PantheonPlus', 'DES_Dovekie'):
            for p in params:
                vals = []
                for uid in by[tr]:
                    run = R[uid][rd][sn].get(model_fit)
                    if run is None: break
                    q = run['parameters'][p]; vals.append((q['mean'], q['std'], q['ci95']))
                if len(vals) == len(by[tr]):
                    res[(tr, model_fit, rd, sn, p)] = s1(f"{tr} {model_fit} {rd[-1]} {sn[:4]} {p}", vals, tv[p])

P("=== S2 COSMO verdicts (joint, per realization) ===")
exp = {'C1': {'T2_A': 'FAIL', 'T2_N1': 'FAIL', 'T2_N2': 'FAIL', 'T1_L1': '!PASS'},
       'C2': {'T2_A': 'PASS', 'T2_N1': 'PASS', 'T2_N2': 'PASS', 'T1_L1': '!FAIL', 'T1_Sign': 'PASS'},
       'C3': {'T1_L1': 'FAIL', 'T1_Sign': 'PASS', 'T2_A': 'FAIL'}}
s2 = {}
for rd in ('Reading_B', 'Reading_A'):
    for tr, tests in exp.items():
        for test, want in tests.items():
            got = []
            for uid in by[tr]:
                jv = R[uid][rd]['joint_verdicts']
                v = jv[test]['verdict'] if test in jv else R[uid][test]['verdict']
                got.append(v)
            match = sum((g != want[1:]) if want.startswith('!') else (g == want) for g in got)
            ok = match >= 4
            s2[(rd, tr, test)] = ok
            P(f"  S2 {rd[-1]} {tr} {test:7s} want {want:6s} got {got} match {match}/5 -> {'PASS' if ok else 'MISS'}")
    # C1 gamma_u 95% includes 0
    got = []
    for uid in by['C1']:
        g = [R[uid][rd][sn]['Law1']['parameters']['gamma_u']['ci95'][0] <= 0.0 for sn in ('PantheonPlus', 'DES_Dovekie')]
        got.append(all(g))
    m = sum(got); s2[(rd, 'C1', 'gamma_ci_includes_0')] = m >= 4
    P(f"  S2 {rd[-1]} C1 γ_u 95% includes 0 (both SN): {got} -> {m}/5 {'PASS' if m>=4 else 'MISS'}")

P("=== GALAXY ===")
for tr in ('G1', 'G2', 'G3'):
    v = [R[uid]['T5_A']['verdict'] for uid in by[tr]]
    med = [R[uid]['T5_A']['test_median_chi2_red'] for uid in by[tr]]
    fr = [R[uid]['T5_A']['test_frac_chi2_red_lt_2'] for uid in by[tr]]
    sig = [R[uid]['T5_A']['fitted_sigma_ref_kpc'] for uid in by[tr]]
    want = 'FAIL' if tr == 'G3' else 'PASS'
    m = sum(x == want for x in v); s2[('B', tr, 'T5_A')] = m >= 4
    P(f"  S2 {tr} T5-A want {want} got {v} -> {m}/5 {'PASS' if m>=4 else 'MISS'}; median χ²_red {[round(x,3) for x in med]}; F<2 {[round(x,3) for x in fr]}; σ_ref {[round(x,3) for x in sig]}")
    if tr != 'G3':
        for meth in ('posterior_sum_chi2_red', 'bootstrap_train_galaxies', 'posterior_total_chi2'):
            vals = [(R[uid]['T5_A']['sigma_ref_uncertainty'][meth]['mean'], R[uid]['T5_A']['sigma_ref_uncertainty'][meth]['std'],
                     R[uid]['T5_A']['sigma_ref_uncertainty'][meth]['ci95']) for uid in by[tr]]
            res[(tr, 'sigma_ref', meth)] = s1(f"{tr} σ_ref [{meth}]", vals, T[tr]['sigma_ref_kpc'])

P("=== REGIONAL ===")
for tr in ('H1', 'H2', 'H3'):
    v = [R[uid]['T6']['verdict'] for uid in by[tr]]
    p = [R[uid]['T6']['p_het'] for uid in by[tr]]
    Z = [R[uid]['T6']['Z_all_sky_vs_Planck'] for uid in by[tr]]
    P(f"  {tr} T6 verdicts {v} p_het {[float('%.3g'%x) for x in p]} Z_allsky {[round(x,2) for x in Z]}")
    if tr == 'H1': m = sum(x == 'FAIL' for x in v); s2[('B','H1','T6')] = m>=4; P(f"    S2 H1 want FAIL -> {m}/5 {'PASS' if m>=4 else 'MISS'}")
    if tr == 'H3': m = sum(x == 'PASS' for x in v); s2[('B','H3','T6')] = m>=4; P(f"    S2 H3 want PASS -> {m}/5 {'PASS' if m>=4 else 'MISS'}")
    if tr == 'H2': P(f"    H2 detection rate (PASS) = {sum(x=='PASS' for x in v)}/5")
    # S1 regional H0 per region
    ins = tot = 0; biases = []; sigs = []
    for uid in by[tr]:
        truthH = U[uid]['H0_regions']
        for r in R[uid]['T6']['regional_H0']:
            k = str(r['pixel_ring_id']); 
            if k not in truthH: continue
            h, s = r['H0_kms_Mpc'], r['sigma_H0_total_incl_cal']
            tot += 1; ins += abs(h - truthH[k]) <= 1.96 * s; biases.append(h - truthH[k]); sigs.append(s)
    P(f"    S1 regional H0: inside95 {ins}/{tot}; mean bias {st.mean(biases):+.3f}; mean σ_total {st.mean(sigs):.3f}")
    res[(tr,'regional_H0')] = ins/tot
json.dump({'s1': {'|'.join(map(str,k)): v for k, v in res.items()}, 's2': {'|'.join(map(str,k)): v for k, v in s2.items()}},
          open('/home/claude/p3score/score_summary.json', 'w'), indent=1)
print('\n'.join(out))
