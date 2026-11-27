"""Pet crate and gift crate, shut and open: python cratesheet.py <module dir> <out dir>"""
import sys, os, math
sys.path.insert(0, sys.argv[1])
import bpy
from mathutils import Matrix
import common, palette, crates, scenes
out = sys.argv[2]
png = os.path.join(out, palette.TEXTURE_NAME + ".png")
common.reset_scene(); palette.write_palette_png(png)
mat = common.palette_material(png)
allo = []
for c, (gift, opened) in enumerate(((False, False), (True, False), (True, True))):
    objs = crates.build_pet_crate(mat, gift=gift)
    P = Matrix.Translation((c * 3.6, 0, 0))
    for o in objs:
        m = o.matrix_basis.copy()
        if opened and o.name.endswith("_Lid_Swing"):
            m = m @ Matrix.Rotation(math.radians(-crates.LID_OPEN), 4, "X")
        o.matrix_world = P @ m
        o.name = f"V{c}_{o.name}"
    allo += objs
bpy.context.view_layer.update()
scenes.shot(allo, os.path.join(out, "crates.png"), (3.6 - 9.0, -16.0, 7.5), (3.6, 0.0, 0.9), 50, res=(1800, 700), samples=32)
