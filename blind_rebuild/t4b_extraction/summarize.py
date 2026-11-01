import json, glob, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def u(x):
    if not isinstance(x, dict):
        return str(x)
    return "%s val=%s comp=%s %s" % (x.get('kind'), x.get('value'), x.get('components'), x.get('unit'))
def pos(x):
    if not isinstance(x, dict):
        return str(x)[:80]
    lab = str(x.get('type') or x.get('label'))[:90]
    return "[%s] ra=%s dec=%s off=%s | unc: %s" % (lab, x.get('ra'), x.get('dec'), x.get('offset'), u(x.get('uncertainty')))
pat = sys.argv[1] if len(sys.argv) > 1 else 'cluster_[0-9][0-9].json'
for f in sorted(glob.glob(pat)):
    d = json.load(open(f, encoding='utf-8'))
    z = d['z_cl'].get('value') if isinstance(d['z_cl'], dict) else d['z_cl']
    print('=== row', d['row'], d['designation'], 'z=', z, '| file', f)
    print('  I:', pos(d.get('I')))
    print('  G:', pos(d.get('G')))
    for s in d.get('S_candidates', []):
        print('  S:', pos(s))
    for k in d:
        if k not in ('row', 'designation', 'paper_ref', 'paper_found', 'subcluster_designated', 'z_cl', 'I', 'G', 'S_candidates', 'notes'):
            print('  extra key:', k, str(d[k])[:300])
