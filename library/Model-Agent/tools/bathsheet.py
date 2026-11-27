"""Bathtile with each bow tier as the game wears it: python bathsheet.py <module dir> <out dir> <tag>"""
import sys, os
sys.path.insert(0, sys.argv[1])
import bpy
from mathutils import Matrix, Vector
import common, palette, cats, props, scenes
out, tag = sys.argv[2], sys.argv[3]
png = os.path.join(out, palette.TEXTURE_NAME + ".png")
common.reset_scene(); palette.write_palette_png(png)
mat = common.palette_material(png)
name = "Bathtile"; spec = cats.SPECIAL_CATS[name]
bk = props.bow_scale(name) if hasattr(props, "bow_scale") else getattr(props, "BOW_SCALE", 1.0)
allo = []
for c, bn in enumerate(("CleanACat_Bow_Pink", "CleanACat_Bow_PinkDouble", "CleanACat_Bow_PinkRoyal", "CleanACat_Bow_PinkGolden")):
    k = cats.scale_of(spec, "sit")
    at, turn = props.bow_corner(spec, "sit", name)
    M = Matrix.Translation(Vector(cats.joints(spec, "sit")["Head"]) + Vector(at) * k) @ turn.to_4x4()
    cat = cats.build_cat(name, mat, body="sit")
    bow = props.build_bow(bn, mat) if bn in props.BOWS else props.build_tier_bow(bn, mat)
    bow = [o for o in bow if not o.name.endswith("_Fan")]
    P = Matrix.Translation(Vector((c * 2.2, 0, 0)))
    for o in cat:
        o.matrix_world = P @ o.matrix_basis
    for o in bow:
        o.matrix_world = P @ M @ Matrix.Scale(spec.get("scale", 1.0) * bk, 4) @ o.matrix_basis
    for o in cat + bow:
        o.hide_render = "_Fluff" in o.name or "_Claw" in o.name
        o.name = f"V{c}_{o.name}"
    allo += cat + bow
bpy.context.view_layer.update()
cx = 2.2 * 1.5
scenes.shot(allo, os.path.join(out, f"front_{tag}.png"), (cx, -40.0, 3.0), (cx, 0.0, 1.3), 110, res=(1600, 560), samples=32)
scenes.shot(allo, os.path.join(out, f"left_{tag}.png"), (cx - 26.0, -30.0, 8.0), (cx, 0.0, 1.3), 110, res=(1600, 560), samples=32)
