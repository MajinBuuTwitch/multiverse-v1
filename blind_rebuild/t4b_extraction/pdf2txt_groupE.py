import sys, pypdf
# usage: pdf2txt_groupE.py in.pdf out.txt
r = pypdf.PdfReader(sys.argv[1])
with open(sys.argv[2], 'w', encoding='utf-8') as f:
    for i, p in enumerate(r.pages):
        f.write(f'\n===== PAGE {i+1} =====\n')
        f.write(p.extract_text() or '')
print(len(r.pages))
