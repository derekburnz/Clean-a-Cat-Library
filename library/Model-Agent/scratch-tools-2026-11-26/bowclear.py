"""Signed clearance between a bow and a head piece cat's own pieces. CANDS=out:down:tip[:fwd],...  ONLY=Name,Name  TIERS=Royal,..."""
import sys, math, os
sys.path.insert(0, "/home/claude/Clean-a-Cat/assets/clean-a-cat/blender")
import bpy, bmesh
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree
import common, palette, cats, props
png = "/tmp/claude-0/-home-claude/af1c4b88-27fa-5077-88ab-48cba264ce26/scratchpad/crownbows/" + palette.TEXTURE_NAME + ".png"
BODY = os.environ.get("BODY", "sit")
def islands(o):
    """Each connected piece of an object as (BVH, sample points), in world space."""
    bm = bmesh.new(); bm.from_mesh(o.data); bm.transform(o.matrix_world); bm.verts.ensure_lookup_table()
    seen, out = set(), []
    for v in bm.verts:
        if v.index in seen: continue
        stack, comp = [v], []
        seen.add(v.index)
        while stack:
            a = stack.pop(); comp.append(a)
            for e in a.link_edges:
                b = e.other_vert(a)
                if b.index not in seen: seen.add(b.index); stack.append(b)
        faces = {f for a in comp for f in a.link_faces}
        idx = {a.index: i for i, a in enumerate(comp)}
        t = BVHTree.FromPolygons([a.co.copy() for a in comp], [[idx[x.index] for x in f.verts] for f in faces])
        pts = [a.co.copy() for a in comp] + [f.calc_center_median() for f in faces]
        pts += [(e.verts[0].co + e.verts[1].co) / 2 for f in faces for e in f.edges]
        c = sum((a.co for a in comp), Vector()) / len(comp)
        pts.append(c)
        out.append((t, pts))
    bm.free(); return out
DIRS = [Vector((0.37, 0.61, 0.70)).normalized(), Vector((-0.58, 0.33, -0.74)).normalized(), Vector((0.21, -0.83, 0.52)).normalized()]
def inside(t, p):
    votes = 0
    for d in DIRS:
        n, o = 0, p.copy()
        while n < 64:
            hit = t.ray_cast(o, d)
            if hit[0] is None: break
            n += 1; o = hit[0] + d * 1e-5
        votes += n % 2
    return votes >= 2
def signed(t, p):
    d = t.find_nearest(p)[3]
    return -d if inside(t, p) else d
def clearance(A, B):
    m = 9.0
    for ta, pa in A:
        for tb, pb in B:
            m = min(m, min(signed(ta, p) for p in pb), min(signed(tb, p) for p in pa))
    return m
names = [n for n in cats.SPECIAL_CATS if props.slot(n) in ("Head", "Face") and (not os.environ.get("ONLY") or n in os.environ["ONLY"].split(","))]
tiers = os.environ.get("TIERS", ",Double,Royal,Golden").split(",")
CANDS = [tuple(float(x) for x in c.split(":")) for c in os.environ["CANDS"].split(",")]
for name in names:
    spec = cats.SPECIAL_CATS[name]
    k = cats.scale_of(spec, BODY); h = cats.dims(spec, BODY)["head"]
    for cand in CANDS:
        row = []
        for tier in tiers:
            bn = "CleanACat_Bow_Pink" + tier
            common.reset_scene(); mat = common.palette_material(png)
            fwd = cand[3] if len(cand) > 3 else 0.13
            at = (h["s"][0] / 2 + cand[0], h["fy"] + fwd, h["top"] - cand[1])
            M = Matrix.Translation(Vector(cats.joints(spec, BODY)["Head"]) + Vector(at) * k) @ Matrix.Rotation(math.radians(cand[2]), 4, "Y")
            cat = cats.build_cat(name, mat, body=BODY)
            bow = props.build_bow(bn, mat) if bn in props.BOWS else props.build_tier_bow(bn, mat)
            bow = [o for o in bow if not o.name.endswith("_Fan") and o.type == "MESH"]
            for o in bow: o.matrix_world = M @ Matrix.Scale(k, 4) @ o.matrix_basis
            bpy.context.view_layer.update()
            B = [i for o in bow for i in islands(o)]
            worst = []
            for c in cat:
                if c.type != "MESH" or "_Fluff" in c.name: continue
                short = c.name.replace("CleanACat_Cat_", "").split("_", 1)[1] if "_" in c.name.replace("CleanACat_Cat_", "") else c.name
                if short.replace("Sit_", "") in ("Head",): 
                    hd = clearance(islands(c), B); continue
                if not any(x in c.name for x in ("Prop", "Glow", "Ear")): continue
                worst.append((round(clearance(islands(c), B), 3), short.replace("Sit_", "")))
            w = min(worst) if worst else (9, "-")
            row.append(f"{tier or 'Plain'} {w[0]:+.3f} {w[1]} head {hd:+.3f}")
        print("RES", name, cand, " | ".join(row), flush=True)
