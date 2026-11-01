import gzip, tarfile, io, os
base = r"d:\Blind_Rebuild\data\papers"
for name in ["jee2014_a520", "okabe_umetsu2008", "jee2015_ciza2242", "dawson2012_musketball"]:
    d = os.path.join(base, name)
    raw = gzip.open(os.path.join(d, name + ".eprint.gz")).read()
    out = os.path.join(d, "src")
    os.makedirs(out, exist_ok=True)
    try:
        tf = tarfile.open(fileobj=io.BytesIO(raw))
        members = [m for m in tf.getmembers() if m.isfile() and not m.name.startswith(("/", "..")) and ".." not in m.name]
        tf.extractall(out, members=members)
        print(name, [m.name for m in members])
    except tarfile.ReadError:
        open(os.path.join(out, name + ".tex"), "wb").write(raw)
        print(name, "single tex")
