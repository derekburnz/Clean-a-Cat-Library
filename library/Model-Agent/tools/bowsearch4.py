"""Bathtile on the cap corner: every tier clears the cap by the block (query >= 0) and looks to rest on it (seen <= TOUCH), at BSCALE x BOW_SCALE."""
import sys, itertools, math, os
sys.path.insert(0, os.getcwd())
import numpy as np
import rbx_bowfit as B
import bpy  # noqa
import props
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_argv = sys.argv; sys.argv = [_argv[0], "check", ""]
from bowsearch2 import C, Ry, bows, SCALE  # noqa
sys.argv = _argv
TOUCH = float(os.environ.get("TOUCH", "0.04"))
BSC = float(os.environ.get("BSCALE", "1.0"))
def per_tier(tree, delta, tip, scale, base_tip):
    cp = B.parts(tree)
    head = next(p for p in cp if "BowSlot" in p["atts"])
    S0 = head["m"] @ head["atts"]["BowSlot"]; S = S0.copy()
    S[:3, :3] = S0[:3, :3] @ (C @ Ry(tip - base_tip) @ C.T); S[:3, 3] = S0[:3, 3] + C @ np.array(delta)
    head = dict(head, atts=dict(head["atts"], BowSlot=np.linalg.inv(head["m"]) @ S))
    pieces = [p for p in cp if p.get("atts") is not None and "BowSlot" not in p["atts"] and any(k in p["path"] for k in B.ON_HEAD)]
    out = []
    for t in B.TIERS:
        ws = wq = hmin = 9; wear = 9
        for L in bows[t]:
            base = next(p for p in L if "BowSlot" in p["atts"])
            slot = head["m"] @ head["atts"]["BowSlot"]; own = base["m"] @ base["atts"]["BowSlot"]
            fit = slot @ np.linalg.inv(own)
            for b in L:
                bb = dict(b, size=b["size"] * scale); mb = fit @ B._scaled(b["m"], scale, own[:3, 3])
                hmin = min(hmin, B.gap(bb, mb, head, head["m"], "seen"))
                for c in pieces:
                    if "_Ear" in c["path"]:
                        wear = min(wear, B.gap(bb, mb, c, c["m"], "seen"))
                    else:
                        ws = min(ws, B.gap(bb, mb, c, c["m"], "seen")); wq = min(wq, B.gap(bb, mb, c, c["m"], "query"))
        out.append((ws, wq, hmin, wear))
    return out
cat = sys.argv[1]
trees = []
for suf, k in (("", 1.0), ("_Dirty_Sit", 0.95), ("_Sit_Lite", 0.95)):
    try: tree = B._load(f"CleanACat_Cat_{cat}{suf}")
    except Exception: continue
    a = tree["attributes"]; sc = a["Scale"]["Float64"] if isinstance(a["Scale"], dict) else a["Scale"]
    trees.append((tree, k * sc, sc))
cur = props.BOW_OWN[cat]
best = None
DINS = [float(x) for x in os.environ.get("DINS", "-0.28,-0.24,-0.2,-0.16,-0.12,-0.08,-0.04,0").split(",")]
E = lambda k, d: [float(x) for x in os.environ.get(k, d).split(",")]   # noqa: E731
for din, dfwd, down, tip in itertools.product(DINS, E("DFWDS", "-0.12,-0.08,-0.04,0,0.04,0.08"),
                                              E("DOWNS", "-0.12,-0.09,-0.06,-0.03,0,0.03,0.06"), E("TIPS", "30,45,60,75,90")):
    ok, rows = True, []
    for tree, k, sc in trees:
        delta = np.array([-(din - cur[0]), -(dfwd - cur[1]), -(down - cur[2])]) * k
        for ws, wq, hmin, wear in per_tier(tree, delta, tip, sc * SCALE * BSC, cur[3]):
            if wq < 0 or ws < 0 or ws > TOUCH or wear < B.EAR_OK or hmin < B.BURIED:
                ok = False; break
            rows.append((round(ws, 3), round(wq, 3), round(hmin, 3)))
        if not ok: break
    if ok:
        c0 = [float(v) for v in os.environ.get('COST0', ','.join(map(str, cur))).split(',')]
        cost = abs(din - c0[0]) + abs(dfwd - c0[1]) + abs(down - c0[2]) + abs(tip - c0[3]) / 60
        if best is None or cost < best[0]:
            best = (cost, (din, dfwd, down, tip), rows); print("cand", best, flush=True)
print(cat, best, flush=True)
