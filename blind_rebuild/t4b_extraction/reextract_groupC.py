import gzip, tarfile, io, os, hashlib, re
base = r"d:\Blind_Rebuild\data\papers"
expected = {
 "jee2014_a520": "A464CDEB6CB99A73B8498A0489C86BBDFFEF928D10B46703E6F274E24D8927DF",
 "okabe_umetsu2008": "C938926EAB0BE0DC60744DF56E6DE873295D54AF0B4B97E2198BBFFD781A8933",
 "jee2015_ciza2242": "59222128D9F9D80F3E0AF5938FC909EC86DA82123826B4313DAA206A0315C8F2",
 "dawson2012_musketball": "5C14F294D01CB7F19AAA533CD991DF937BB35B91D1E6F325F1FCC737FB225CB8",
}
for name, h in expected.items():
    d = os.path.join(base, name)
    p = os.path.join(d, name + ".eprint.gz")
    data = open(p, "rb").read()
    hh = hashlib.sha256(data).hexdigest().upper()
    print(name, "archive sha256 match:", hh == h)
    raw = gzip.decompress(data)
    out = os.path.join(d, "src_clean_C")
    if os.path.exists(out):
        print("  exists already:", out)
    os.makedirs(out, exist_ok=True)
    tf = tarfile.open(fileobj=io.BytesIO(raw))
    members = [m for m in tf.getmembers() if m.isfile() and not m.name.startswith(("/", "..")) and ".." not in m.name]
    tf.extractall(out, members=members)
    for m in members:
        if m.name.endswith(".tex"):
            t = open(os.path.join(out, m.name), encoding="latin-1").read()
            ti = re.search(r"\\title\{(.{0,200})", t, re.S)
            au = re.findall(r"\\author\{([^}]*)\}", t)[:3]
            print("  ", m.name, "| title:", ti.group(1).replace("\n", " ")[:150] if ti else None, "| authors:", au)
            # compare with src/
            old = os.path.join(d, "src", m.name)
            if os.path.exists(old):
                print("   identical to src/ copy:", open(old, "rb").read() == open(os.path.join(out, m.name), "rb").read())
    print("  src/ listing now:", sorted(os.listdir(os.path.join(d, "src"))))
