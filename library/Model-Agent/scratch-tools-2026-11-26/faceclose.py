"""Two faces close up: python faceclose.py <module dir> <out png>"""
import sys, os
sys.path.insert(0, sys.argv[1])
import bpy
from mathutils import Matrix, Vector
import common, palette, cats, scenes
out = sys.argv[2]; d = os.path.dirname(out)
png = os.path.join(d, palette.TEXTURE_NAME + ".png")
common.reset_scene(); palette.write_palette_png(png)
mat = common.palette_material(png)
allo = []
for c, name in enumerate(["Toffee", "Muffin", "Inky"]):
    cat = cats.build_cat(name, mat, body="sit")
    P = Matrix.Translation(Vector((c * 1.5, 0, 0)))
    for o in cat:
        o.matrix_world = P @ o.matrix_basis
        o.hide_render = "_Fluff" in o.name or "_Claw" in o.name
        o.name = f"V{c}_{o.name}"
    allo += cat
bpy.context.view_layer.update()
scenes.shot(allo, out, (1.5, -30.0, 2.6), (1.5, 0.0, 1.42), 200, res=(1900, 520), hide=())
