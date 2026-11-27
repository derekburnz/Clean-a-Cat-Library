"""Search a corner bow spot that clears the head piece by both the drawn and the query shapes. Run from blender/."""
import sys, itertools, math
import os; sys.path.insert(0, os.getcwd())
import numpy as np
import rbx_bowfit as B
import bpy  # noqa
import props
C = np.array([[-1, 0, 0], [0, 0, 1], [0, 1, 0]], float)
def Ry(d):
    a = math.radians(d); c, s = math.cos(a), math.sin(a)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
EAR_OK, CLEAR = -0.09, 0.01
SCALE = props.BOW_SCALE
bows = {t: [B.parts(B._load(f"CleanACat_Bow_{c}{t}")) for c in B.COLOURS] for t in B.TIERS}
bows = {t: [[p for p in L if "_Fan" not in p["path"] and "_Fan" not in p["name"]] for L in v] for t, v in bows.items()}
def evaluate(tree, delta, tip, scale, base_tip):
    cp = B.parts(tree)
    head = next(p for p in cp if "BowSlot" in p["atts"])
    S0 = head["m"] @ head["atts"]["BowSlot"]
    S = S0.copy()
    # the model's slot already carries base_tip; replace the turn with `tip`
    S[:3, :3] = S0[:3, :3] @ (C @ Ry(tip - base_tip) @ C.T)
    S[:3, 3] = S0[:3, 3] + C @ np.array(delta)
    head = dict(head, atts=dict(head["atts"], BowSlot=np.linalg.inv(head["m"]) @ S))
    pieces = [p for p in cp if p is not None and p.get("atts") is not None and "BowSlot" not in p["atts"]
              and any(k in p["path"] for k in B.ON_HEAD)]
    wseen, wquery, wear, hmax, hmin = 9, 9, 9, -9, 9
    for t in B.TIERS:
        for L in bows[t]:
            base = next(p for p in L if "BowSlot" in p["atts"])
            slot = head["m"] @ head["atts"]["BowSlot"]; own = base["m"] @ base["atts"]["BowSlot"]
            fit = slot @ np.linalg.inv(own)
            on = 9
            for b in L:
                bb = dict(b, size=b["size"] * scale); mb = fit @ B._scaled(b["m"], scale, own[:3, 3])
                on = min(on, B.gap(bb, mb, head, head["m"], "seen"))
                for c in pieces:
                    if "_Ear" in c["path"]:
                        wear = min(wear, B.gap(bb, mb, c, c["m"], "seen"))
                    else:
                        wseen = min(wseen, B.gap(bb, mb, c, c["m"], "seen"))
                        wquery = min(wquery, B.gap(bb, mb, c, c["m"], "query"))
            hmax, hmin = max(hmax, on), min(hmin, on)
    return wseen, wquery, wear, hmax, hmin
mode = sys.argv[1]
ONP = bool(os.environ.get('ONPIECE'))
cats = sys.argv[2].split(",")
for cat in cats:
    trees = []
    for suf, k in (("", 1.0), ("_Dirty_Sit", 0.95), ("_Sit_Lite", 0.95)):
        try:
            tree = B._load(f"CleanACat_Cat_{cat}{suf}")
        except Exception:
            continue
        a = tree["attributes"]; sc = a["Scale"]["Float64"] if isinstance(a["Scale"], dict) else a["Scale"]
        trees.append((tree, k * sc, sc)); tree["_n"] = suf or "Stand"
    cur = props.BOW_OWN.get(cat, (0, 0, 0, 30.0))
    if mode == "check":
        for tree, k, sc in trees:
            print(cat, tree["_n"], [round(v, 3) for v in evaluate(tree, np.zeros(3), cur[3], sc * SCALE, cur[3])])
        continue
    best = None
    DOWNS = (-0.24, -0.18, -0.12, -0.06, 0.0, 0.06, 0.12) if ONP else (-0.06, -0.03, 0.0, 0.04, 0.08, 0.12, 0.18)
    grid = itertools.product((-0.2, -0.16, -0.12, -0.08, -0.04, 0.0), (-0.04, 0.0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.25),
                             DOWNS, (30, 45, 60, 75))
    for din, dfwd, down, tip in grid:
        ok, rows = True, []
        for tree, k, sc in trees:
            delta = np.array([-(din - cur[0]), -(dfwd - cur[1]), -(down - cur[2])]) * k
            ws, wq, we, hx, hn = evaluate(tree, delta, tip, sc * SCALE, cur[3])
            if ONP:
                bad = ws < 0.0 or wq < 0.0 or wq > 0.03 or we < EAR_OK or hn < B.BURIED
            else:
                bad = ws < CLEAR or wq < CLEAR or we < EAR_OK or hx > 0.004 or hn < B.BURIED
            if bad:
                ok = False; break
            rows.append((round(ws, 3), round(wq, 3), round(hx, 3)))
        if ok:
            cost = abs(din) + abs(dfwd) + abs(down) + abs(tip - 30) / 300
            if best is None or cost < best[0]:
                best = (cost, (din, dfwd, down, tip), rows)
    print(cat, best, flush=True)
