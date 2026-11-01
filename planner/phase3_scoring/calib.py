import json, sys, statistics as st
from math import sqrt
R = json.load(open(sys.argv[1]))['universes']; K = json.load(open(sys.argv[2])); T = K['truths']
U = {u['universe_id']: u for u in K['universes']}; by = {}
for uid,u in U.items(): by.setdefault(u['truth'],[]).append(uid)
print("Calibration: chi2 = sum((mean-truth)/std)^2 over 5 realizations (expect ~5, p<0.05 above 11.07); scatter ratio = sd(means)/mean(std)")
tv = {'C1':{'Omega_bc':T['C1']['Obc'],'h':T['C1']['h'],'100_omega_b':T['C1']['wb100'],'w0':-1,'wa':0},
      'C2':{'Omega_bc':T['C2']['Obc'],'h':T['C2']['h'],'100_omega_b':T['C2']['wb100'],'gamma_u':0.1},
      'C3':{'Omega_bc':T['C3']['Obc'],'h':T['C3']['h'],'100_omega_b':T['C3']['wb100'],'w0':-0.75,'wa':-1}}
fits = {'C1':['CPL','T2A_CPL'],'C2':['Law1','T2A_CPL'],'C3':['CPL','T2A_CPL']}
for tr in ('C1','C2','C3'):
  for mf in fits[tr]:
    for rd in ('Reading_B',):
      for sn in ('PantheonPlus','DES_Dovekie'):
        row=[]
        for p,t in tv[tr].items():
          try: q=[R[u][rd][sn][mf]['parameters'][p] for u in by[tr]]
          except KeyError: continue
          c2=sum(((x['mean']-t)/x['std'])**2 for x in q); sr=st.stdev(x['mean'] for x in q)/st.mean(x['std'] for x in q)
          row.append(f"{p} χ²={c2:5.1f} ratio={sr:.2f}")
        print(f"  {tr} {mf:7s} {sn[:4]}: "+" | ".join(row))
print("\nT2-A signed Z per run (Reading B / A; PP, DES). Under C2 these should scatter ~N(0,1):")
for tr in ('C1','C2','C3'):
  for rd in ('Reading_B','Reading_A'):
    zs=[]
    for u in sorted(by[tr], key=lambda x:U[x]['round']):
      zs.append(tuple(round(R[u][rd][sn]['verdicts_and_stats']['T2_A']['signed_tension_sigma'],2) for sn in ('PantheonPlus','DES_Dovekie')))
    flat=[z for p in zs for z in p]
    print(f"  {tr} {rd[-1]}: {zs}  mean {st.mean(flat):+.2f} sd {st.stdev(flat):.2f}")
# R_ref noise contribution and R_pred scatter in C2
print("\nC2 decomposition (Reading B, DES): R_pred vs truth 5.0 and R_ref vs truth")
for u in sorted(by['C2'], key=lambda x:U[x]['round']):
  t=R[u]['Reading_B']['DES_Dovekie']['verdicts_and_stats']['T2_A']
  print(f"  {u} R_pred {t['R_pred']:.3f}±{t['sigma_R_pred']:.3f}  R_ref {t['R_ref']:.3f}  Z {t['signed_tension_sigma']:+.2f}")
