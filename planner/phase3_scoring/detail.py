import json, sys, statistics as st
R = json.load(open(sys.argv[1]))['universes']; K = json.load(open(sys.argv[2])); T = K['truths']
U = {u['universe_id']: u for u in K['universes']}; by = {}
for uid,u in U.items(): by.setdefault(u['truth'],[]).append(uid)
for k in by: by[k].sort(key=lambda x: U[x]['round'])
f = lambda q: f"{q['mean']:.4f}±{q['std']:.4f} [{q['ci95'][0]:.4f},{q['ci95'][1]:.4f}]"
print("C1 Law1 gamma_u (B):")
for uid in by['C1']:
    print(' ', uid, [f(R[uid]['Reading_B'][sn]['Law1']['parameters']['gamma_u']) for sn in ('PantheonPlus','DES_Dovekie')])
print("C2 Law1 Omega_bc (truth 0.315789):")
for rd in ('Reading_B','Reading_A'):
  for uid in by['C2']:
    print(' ', rd[-1], uid, [f(R[uid][rd][sn]['Law1']['parameters']['Omega_bc']) for sn in ('PantheonPlus','DES_Dovekie')])
print("C2 T2-A per-run stats:")
for rd in ('Reading_B','Reading_A'):
  for uid in by['C2']:
    print(' ', rd[-1], uid, {sn: R[uid][rd][sn]['verdicts_and_stats']['T2_A'] for sn in ('PantheonPlus','DES_Dovekie')})
    break
print("C2 T1-Sign per-run:")
for rd in ('Reading_B','Reading_A'):
  for uid in by['C2']:
    print(' ', rd[-1], uid, {sn: R[uid][rd][sn]['verdicts_and_stats']['T1_Sign'] for sn in ('PantheonPlus','DES_Dovekie')})
print("Supplementary: C3 Law1 matter params, C2 CPL w0 vs -0.90")
for tr, mf, ps, tv in [('C3','Law1',['Omega_bc','h','100_omega_b'],{'Omega_bc':T['C3']['Obc'],'h':T['C3']['h'],'100_omega_b':T['C3']['wb100']}),
                       ('C2','CPL',['w0','Omega_bc','h'],{'w0':-0.9,'Omega_bc':T['C2']['Obc'],'h':T['C2']['h']})]:
  for rd in ('Reading_B','Reading_A'):
    for sn in ('PantheonPlus','DES_Dovekie'):
      for p in ps:
        v=[R[u][rd][sn][mf]['parameters'][p] for u in by[tr]]
        ins=sum(q['ci95'][0]<=tv[p]<=q['ci95'][1] for q in v); b=st.mean(q['mean'] for q in v)-tv[p]; s=st.mean(q['std'] for q in v)
        print(f"  {tr} {mf} {rd[-1]} {sn[:4]} {p}: inside {ins}/5 bias/σ {b/s:+.2f}")
print("Regional per-region coverage (total σ / hf-only σ):")
for tr in ('H1','H2','H3'):
  reg={}
  for uid in by[tr]:
    th=U[uid]['H0_regions']
    for r in R[uid]['T6']['regional_H0']:
      k=str(r['pixel_ring_id']); d=r['H0_kms_Mpc']-th[k]
      reg.setdefault(k,[]).append((d, r['sigma_H0_total_incl_cal'], r['sigma_H0_hf_only'], r['n_sn']))
  for k,v in sorted(reg.items()):
    it=sum(abs(d)<=1.96*s for d,s,h,n in v); ih=sum(abs(d)<=1.96*h for d,s,h,n in v)
    b=st.mean(d for d,*_ in v); s=st.mean(x[1] for x in v)
    print(f"  {tr} region {k:>3} n_sn={v[0][3]:4d} inside_tot {it}/5 inside_hf {ih}/5 bias {b:+.2f} meanσtot {s:.2f} {'MISS' if it<4 or abs(b)>=s else ''}")
print("M_B fixed per H universe:", {tr:[round(R[u]['calibrator_fit']['M_B_fixed'],4) for u in by[tr]] for tr in ('H1','H2','H3')})
