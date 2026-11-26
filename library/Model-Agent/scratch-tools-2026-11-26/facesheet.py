"""Cat faces close up: python facesheet.py <out dir> <tag> [body]"""
import sys, os, math
sys.path.insert(0, "/home/claude/Clean-a-Cat/assets/clean-a-cat/blender")
import bpy
from mathutils import Matrix, Vector
import common, palette, cats, scenes
out, tag = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
body = sys.argv[3] if len(sys.argv) > 3 else "sit"
png = os.path.join(out, palette.TEXTURE_NAME + ".png")
def row(names, key, eye_dz=2.2, lens=120, res=(1900, 560)):
    common.reset_scene(); palette.write_palette_png(png)
    mat = common.palette_material(png)
    allo = []
    for c, name in enumerate(names):
        cat = cats.build_cat(name, mat, body=body)
        P = Matrix.Translation(Vector((c * 1.9, 0, 0)))
        for o in cat:
            o.matrix_world = P @ o.matrix_basis
            o.hide_render = "_Fluff" in o.name or "_Claw" in o.name
            o.name = f"V{c}_{o.name}"
        allo += cat
    bpy.context.view_layer.update()
    cx = 1.9 * (len(names) - 1) / 2
    scenes.shot(allo, os.path.join(out, f"{key}_{tag}.png"), (cx, -40.0, eye_dz + 0.6), (cx, 0.0, 1.3), lens, res=res, hide=())
    scenes.shot(allo, os.path.join(out, f"{key}_far_{tag}.png"), (cx + 6.0, -40.0, 14.0), (cx, 0.0, 0.9), 62, res=(1900, 420), hide=())
row(["Muffin", "Toffee", "LilacCloud", "Inky", "Cotton", "Marble"], "a")
row(["Smudge", "Tux", "Patches", "Starcoat"] + list(cats.SPECIAL_CATS)[:2], "b")
if len(sys.argv) > 4:
    sp = list(cats.SPECIAL_CATS)
    row(sp[2:8], "c")
