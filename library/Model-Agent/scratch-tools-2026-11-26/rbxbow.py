"""Box level clearance between a worn bow and a cat's head pieces, from the model files (what Studio's part check sees).
python rbxbow.py  with CANDS=out:down:tip[:fwd],... (Blender units, as props.bow_corner)  ONLY=..  TIERS=..  BODY=_Sit|''"""
import json, os, sys, math, itertools
import numpy as np
R = "/home/claude/Clean-a-Cat/assets/clean-a-cat/rbx/"
CUR = (0.015, 0.12, 75.0, 0.13)
def cf(p):
    c = p["CFrame"]["CFrame"] if "CFrame" in p["CFrame"] else p["CFrame"]
    M = np.eye(4); M[:3, :3] = np.array(c["orientation"]); M[:3, 3] = c["position"]; return M
def parts(n, path="", out=None):
    out = [] if out is None else out
    nm = n.get("name") or ""
    if n.get("className") == "Part":
        p = n["properties"]
        atts = {c["name"]: cf(c["properties"]) for c in n.get("children", []) if c.get("className") == "Attachment"}
        sm = [c for c in n.get("children", []) if c.get("className") == "SpecialMesh"]
        q = {"Cylinder": "cyl", "Ball": "ball"}.get(p.get("Shape"), "box")
        v = "ell" if (sm and sm[0]["properties"].get("MeshType") == "Sphere") else q
        out.append(dict(path=path, name=nm, M=cf(p), size=np.array(p["Size"]), atts=atts, q=q, v=v))
    for c in n.get("children", []):
        parts(c, path + "/" + nm if n.get("className") == "Model" else path, out)
    return out
def _dirs(n=900):
    i = np.arange(n) + 0.5; ph = np.arccos(1 - 2 * i / n); th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(ph), np.sin(th) * np.sin(ph), np.cos(ph)], 1)
DIRS = _dirs()
def supp(M, size, kind, D):
    L = D @ M[:3, :3]; h = size / 2
    if kind == "box": return np.abs(L) @ h
    if kind == "ell": return np.sqrt(((L * h) ** 2).sum(1))
    if kind == "ball": return np.full(len(D), h.min())
    return h[0] * np.abs(L[:, 0]) + h[1] * np.sqrt(L[:, 1] ** 2 + L[:, 2] ** 2)          # a cylinder along its X
def sat(A, B, mode="v"):
    """Signed gap between two convex parts (M, size, part): positive apart, negative the least overlap."""
    Ra, Rb = A[0][:3, :3], B[0][:3, :3]
    D = np.vstack([DIRS, Ra.T, Rb.T])
    d = B[0][:3, 3] - A[0][:3, 3]
    return float(np.max(np.abs(D @ d) - supp(A[0], A[1], A[2][mode], D) - supp(B[0], B[1], B[2][mode], D)))
def rotz(deg):
    c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg)); M = np.eye(4); M[:2, :2] = [[c, -s], [s, c]]; return M
names = os.environ.get("ONLY", "Bathtile,Sherbet,Stardust,Rosette,Prism,Jade,Phoenix,Moonstag,Djinn,WhiteTiger").split(",")
tiers = os.environ.get("TIERS", ",Double,Royal,Golden").split(",")
BODY = os.environ.get("BODY", "_Sit")
MODE = os.environ.get("MODE", "v")
CANDS = [tuple(float(x) for x in c.split(":")) for c in os.environ["CANDS"].split(",")]
KS = json.load(open(os.path.dirname(os.path.abspath(__file__)) + "/catk.json"))
for name in names:
    cat = json.load(open(f"{R}CleanACat_Cat_{name}{BODY}.model.json"))
    cp = parts(cat)
    head = next(p for p in cp if "BowSlot" in p["atts"])
    k = 0.95 if "_Sit" in BODY else 1.0
    pieces = [p for p in cp if any(x in p["path"] for x in ("_Prop/", "_Prop", "_Glow", "_Ear")) and "_Prop2" not in p["path"] and p is not head]
    for cand in CANDS:
        cand = cand + CUR[len(cand):]
        A = head["atts"]["BowSlot"].copy()
        A[:3, 3] += k * np.array([-(cand[0] - CUR[0]), -(cand[1] - CUR[1]), (cand[3] - CUR[3])])
        A[:3, :3] = rotz(cand[2])[:3, :3]
        W = head["M"] @ A
        row = []; vals = []; heads = []
        for tier in tiers:
            bow = json.load(open(f"{R}CleanACat_Bow_Pink{tier}.model.json"))
            bp = [p for p in parts(bow) if "_Fan" not in p["path"] and "_Fan" not in p["name"]]
            b0 = next(p for p in bp if "BowSlot" in p["atts"])
            inv = np.linalg.inv(b0["M"] @ b0["atts"]["BowSlot"])
            worst = (9, "")
            for b in bp:
                Mb = W @ inv @ b["M"]
                for c in pieces:
                    g = sat((Mb, b["size"], b), (c["M"], c["size"], c), MODE)
                    if g < worst[0]: worst = (g, c["path"].split("_")[-1] + ":" + "x".join(f"{s:.2f}" for s in c["size"]))
            hg = min(sat((W @ inv @ b["M"], b["size"], b), (head["M"], head["size"], head), MODE) for b in bp)
            row.append(f"{tier or 'Plain'} {worst[0]:+.3f} {worst[1]} head {hg:+.3f}")
            vals.append(worst[0]); heads.append(hg)
        if os.environ.get("BRIEF"):
            print("RES", name, cand, f"min {min(vals):+.3f} head {min(heads):+.3f}..{max(heads):+.3f}", " ".join(f"{v:+.3f}" for v in vals), flush=True)
        else:
            print("RES", name, cand[:3] if cand[3] == 0.13 else cand, " | ".join(row), flush=True)
