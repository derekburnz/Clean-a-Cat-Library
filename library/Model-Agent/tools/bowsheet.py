"""Bows on the head piece cats as the game wears them: python bowsheet.py <module dir> <out dir> <tag> [bow]"""
import sys, os, math
sys.path.insert(0, sys.argv[1])
import bpy
from mathutils import Matrix, Vector
import common, palette, cats, props, scenes
out, tag = sys.argv[2], sys.argv[3]
bn = sys.argv[4] if len(sys.argv) > 4 else "CleanACat_Bow_PinkRoyal"
png = os.path.join(out, palette.TEXTURE_NAME + ".png")
common.reset_scene(); palette.write_palette_png(png)
mat = common.palette_material(png)
names = [n for n in cats.SPECIAL_CATS if props.slot(n) in ("Head", "Face")]
if os.environ.get("NAMES"): names = os.environ["NAMES"].split(",")
_bk = lambda n: props.bow_scale(n) if hasattr(props, "bow_scale") else props.BOW_SCALE  # noqa: E731
allo = []
for c, name in enumerate(names):
    spec = cats.SPECIAL_CATS[name]
    k = cats.scale_of(spec, "sit")
    at, turn = props.bow_corner(spec, "sit", name)
    M = Matrix.Translation(Vector(cats.joints(spec, "sit")["Head"]) + Vector(at) * k) @ turn.to_4x4()
    cat = cats.build_cat(name, mat, body="sit")
    bow = props.build_bow(bn, mat) if bn in props.BOWS else props.build_tier_bow(bn, mat)
    bow = [o for o in bow if not o.name.endswith("_Fan")]
    P = Matrix.Translation(Vector((c * 2.0, 0, 0)))
    for o in cat:
        o.matrix_world = P @ o.matrix_basis
    for o in bow:
        o.matrix_world = P @ M @ Matrix.Scale(spec.get("scale", 1.0) * _bk(name), 4) @ o.matrix_basis
    for o in cat + bow:
        o.hide_render = "_Fluff" in o.name or "_Claw" in o.name
        o.name = f"V{c}_{o.name}"
    allo += cat + bow
bpy.context.view_layer.update()
cx = 2.0 * (len(names) - 1) / 2
L = 104 * 10 / len(names)
scenes.shot(allo, os.path.join(out, f"front_{tag}.png"), (cx, -60.0, 2.4), (cx, 0.0, 1.15), L, res=(2400, 520), samples=32)
scenes.shot(allo, os.path.join(out, f"above_{tag}.png"), (cx - 14, -44.0, 26.0), (cx, 0.0, 1.0), L * 0.94, res=(2400, 620), samples=32)
