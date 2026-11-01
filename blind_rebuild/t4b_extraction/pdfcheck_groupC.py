import sys
try:
    import pypdf
except ImportError:
    print("NO_PYPDF"); sys.exit(0)
import re
base = r"d:\Blind_Rebuild\data\papers"
checks = {
 "dawson2012_musketball": ["gas distribution", "HST WL mass peak", "Table 1", "0.53"],
 "jee2014_a520": ["P4", "positional uncertainty"],
 "jee2015_ciza2242": ["190", "Table 1", "centroid"],
 "okabe_umetsu2008": ["east mass clump", "Table 2", "0.054"],
}
for name, keys in checks.items():
    r = pypdf.PdfReader(f"{base}\\{name}\\{name}.pdf")
    txt = "\n".join((p.extract_text() or "") for p in r.pages)
    open(f"{base}\\{name}\\{name}_pdftext.txt", "w", encoding="utf-8").write(txt)
    print("=====", name, "pages", len(r.pages), "first line:", txt.strip().splitlines()[0][:120])
    for k in keys:
        for m in list(re.finditer(re.escape(k), txt))[:3]:
            s = txt[max(0, m.start()-150): m.end()+250].replace("\n", " ")
            print("  [", k, "]", s)
