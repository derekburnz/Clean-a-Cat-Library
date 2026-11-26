"""Royal bow on the head piece cats: python crownbows.py <out dir> <tag> <dx> <dz> <tip>"""
import sys, os, math
sys.path.insert(0, "/home/claude/Clean-a-Cat/assets/clean-a-cat/blender")
import bpy
from mathutils import Matrix, Vector
import common, palette, cats, props, scenes
out, tag, dx, dz, tip = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
bn = sys.argv[6] if len(sys.argv) > 6 else "CleanACat_Bow_PinkRoyal"
os.makedirs(out, exist_ok=True)
png = os.path.join(out, palette.TEXTURE_NAME + ".png")
common.reset_scene(); palette.write_palette_png(png)
mat = common.palette_material(png)
names = [n for n in cats.SPECIAL_CATS if props.slot(n) in ("Head", "Face") and (not os.environ.get("ONLY") or n in os.environ["ONLY"].split(","))]
print("CATS", names)
allo = []
for c, name in enumerate(names):
    spec = cats.SPECIAL_CATS[name]
    k = cats.scale_of(spec, "sit")
    h = cats.dims(spec, "sit")["head"]
    at = (h["s"][0] / 2 + dx, h["fy"] + 0.13, h["top"] + dz)
    M = Matrix.Translation(Vector(cats.joints(spec, "sit")["Head"]) + Vector(at) * k) @ Matrix.Rotation(math.radians(tip), 4, "Y")
    cat = cats.build_cat(name, mat, body="sit")
    bow = props.build_bow(bn, mat) if bn in props.BOWS else props.build_tier_bow(bn, mat)
    bow = [o for o in bow if not o.name.endswith("_Fan")]
    P = Matrix.Translation(Vector((c * 2.4, 0, 0)))
    for o in cat:
        o.matrix_world = P @ o.matrix_basis
    for o in bow:
        o.matrix_world = P @ M @ Matrix.Scale(float(os.environ.get("BOWK", "1.0")), 4) @ o.matrix_basis
    for o in cat + bow:
        o.hide_render = "_Fluff" in o.name or "_Claw" in o.name
        o.name = f"V{c}_{o.name}"
    allo += cat + bow
bpy.context.view_layer.update()
cx = 2.4 * (len(names) - 1) / 2
w = 1900
scenes.shot(allo, os.path.join(out, f"front_{tag}.png"), (cx, -44.0, 3.6), (cx, 0.0, 1.45), 60 * 10 / max(len(names), 2.2), res=(w, 520), hide=())
scenes.shot(allo, os.path.join(out, f"above_{tag}.png"), (cx + 9.0, -36.0, 17.0), (cx, 0.0, 1.2), 55 * 10 / max(len(names), 2.2), res=(w, 560), hide=())
