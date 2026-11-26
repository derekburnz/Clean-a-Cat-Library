"""Do the tier bows cut into a head piece cat's own pieces? python bowhit.py"""
import sys, math
sys.path.insert(0, "/home/claude/Clean-a-Cat/assets/clean-a-cat/blender")
import bpy, bmesh
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree
import common, palette, cats, props
png = "/tmp/claude-0/-home-claude/af1c4b88-27fa-5077-88ab-48cba264ce26/scratchpad/crownbows/" + palette.TEXTURE_NAME + ".png"
def tree(o):
    bm = bmesh.new(); bm.from_mesh(o.data); bm.transform(o.matrix_world); t = BVHTree.FromBMesh(bm); return t, bm
names = [n for n in cats.SPECIAL_CATS if props.slot(n) in ("Head", "Face")]
bows = list(props.BOWS) + list(props.BOW_TIERS)
print("BOWS", bows)
import os
CANDS = [tuple(float(x) for x in c.split(":")) for c in os.environ["CANDS"].split(",")]
for mode in CANDS:
    for name in names:
        spec = cats.SPECIAL_CATS[name]
        for bn in bows:
            if "Pink" not in bn or (os.environ.get("ONLY") and name not in os.environ["ONLY"]): continue
            common.reset_scene(); mat = common.palette_material(png)
            k = cats.scale_of(spec, "sit"); h = cats.dims(spec, "sit")["head"]
            at, tip = (h["s"][0] / 2 + mode[0], h["fy"] + 0.13, h["top"] - mode[1]), mode[2]
            M = Matrix.Translation(Vector(cats.joints(spec, "sit")["Head"]) + Vector(at) * k) @ Matrix.Rotation(math.radians(tip), 4, "Y")
            cat = cats.build_cat(name, mat, body="sit")
            bow = props.build_bow(bn, mat) if bn in props.BOWS else props.build_tier_bow(bn, mat)
            bow = [o for o in bow if not o.name.endswith("_Fan")]
            for o in bow: o.matrix_world = M @ Matrix.Scale(k, 4) @ o.matrix_basis
            bpy.context.view_layer.update()
            hits = []
            bt = [tree(o) for o in bow if o.type == "MESH"]
            for c in cat:
                if c.type != "MESH" or "_Fluff" in c.name: continue
                ct, cb = tree(c)
                n = sum(len(t.overlap(ct)) for t, _ in bt)
                if n: hits.append((c.name.replace("CleanACat_Cat_", "").replace(name + "_Sit_", ""), n))
                elif c.name.endswith("_Head"):
                    gap = min(ct.find_nearest(v.co)[3] for _, b in bt for v in b.verts)
                    hits.append(("HEADGAP", round(gap, 3)))
                cb.free()
            for _, b in bt: b.free()
            print(mode, name, bn.replace("CleanACat_", ""), hits)
