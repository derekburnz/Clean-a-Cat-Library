"""Grid search a corner bow spot per head piece cat on the Part models. Run from the blender folder."""
import sys, itertools, math
import numpy as np
import rbx_bowfit as B
import os
ONPIECE = bool(os.environ.get('ONPIECE'))
SCALE = float(sys.argv[1]) if len(sys.argv) > 1 else 0.6
only = sys.argv[2].split(",") if len(sys.argv) > 2 else None
C = np.array([[-1, 0, 0], [0, 0, 1], [0, 1, 0]], float)
def Ry(d):
    a = math.radians(d); c, s = math.cos(a), math.sin(a)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
EAR_OK = -0.09
bows = {t: [B.parts(B._load(f"CleanACat_Bow_{c}{t}")) for c in B.COLOURS] for t in B.TIERS}
bows = {t: [[p for p in L if "_Fan" not in p["path"] and "_Fan" not in p["name"]] for L in v] for t, v in bows.items()}
cats = ["Stardust","Sherbet","Rosette","Prism","Jade","Bathtile","Phoenix","Moonstag","Djinn","WhiteTiger"]
def evaluate(tree, delta, tip, scale):
    cp = B.parts(tree)
    head = next(p for p in cp if "BowSlot" in p["atts"])
    S0 = head["m"] @ head["atts"]["BowSlot"]
    S = S0.copy()
    S[:3, :3] = C @ Ry(tip) @ C.T
    S[:3, 3] = S0[:3, 3] + C @ np.array(delta)
    head = dict(head, atts=dict(head["atts"], BowSlot=np.linalg.inv(head["m"]) @ S))
    cp = [head if p is not None and p.get("atts") is not None and "BowSlot" in p["atts"] else p for p in cp]
    worst_prop, worst_ear, hmax, hmin = 9, 9, -9, 9
    for t in B.TIERS:
        for L in bows[t]:
            # B.worn checks pieces incl ears; split them
            base = next(p for p in L if "BowSlot" in p["atts"])
            slot = head["m"] @ head["atts"]["BowSlot"]; own = base["m"] @ base["atts"]["BowSlot"]
            fit = slot @ np.linalg.inv(own)
            pieces = [p for p in cp if p is not head and any(k in p["path"] for k in B.ON_HEAD) and "_Prop2" not in p["path"]]
            on = 9
            for b in L:
                bb = dict(b, size=b["size"] * scale); mb = fit @ B._scaled(b["m"], scale, own[:3, 3])
                on = min(on, B.gap(bb, mb, head, head["m"], "seen"))
                for c in pieces:
                    g = B.gap(bb, mb, c, c["m"], "seen")
                    if "_Ear" in c["path"]: worst_ear = min(worst_ear, g)
                    else: worst_prop = min(worst_prop, g)
            hmax, hmin = max(hmax, on), min(hmin, on)
    return worst_prop, worst_ear, hmax, hmin
DOWNS = (-0.15, -0.12, -0.09, -0.06, -0.03, 0) if ONPIECE else (-0.03, 0, 0.03, 0.06)
for cat in (only or cats):
    trees = []
    for suf, k in (("", 1.0), ("_Sit", 0.95), ("_Sit_Lite", 0.95)):
        tree = B._load(f"CleanACat_Cat_{cat}{suf}")
        a = tree["attributes"]; sc = a["Scale"]["Float64"] if isinstance(a["Scale"], dict) else a["Scale"]
        trees.append((tree, k * sc, sc))
    best = None
    for din, dfwd, down, tip in itertools.product((-0.04, 0, 0.04, 0.08), (0, 0.04, 0.08, 0.12, 0.16, 0.2), DOWNS, (30, 15, 45, 60)):
        ok, score = True, []
        for tree, k, sc in trees:
            delta = np.array([-din, -dfwd, -down]) * k
            wp, we, hx, hn = evaluate(tree, delta, tip, sc * SCALE)
            if ONPIECE:
                bad = wp > 0.004 or wp < -0.06 or we < EAR_OK or hn < B.BURIED
            else:
                bad = wp < 0.005 or we < EAR_OK or hx > 0.004 or hn < B.BURIED
            if bad:
                ok = False; break
            score.append(wp)
        if ok:
            cost = abs(din) + dfwd + abs(down) + abs(tip - 30) / 300
            if best is None or cost < best[0]:
                best = (cost, (din, dfwd, down, tip), [round(s, 3) for s in score])
    print(cat, best, flush=True)
