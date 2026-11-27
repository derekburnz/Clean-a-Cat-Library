import sys, os, math
sys.path.insert(0, sys.argv[1])
import bpy
from mathutils import Matrix, Vector
import common, palette, townsfolk, scenes, spa_props
out, tag = sys.argv[2], sys.argv[3]
png = os.path.join(out, palette.TEXTURE_NAME + ".png")
common.reset_scene(); palette.write_palette_png(png)
mat = common.palette_material(png)
names = list(townsfolk.LOOKS)[:8]
allo = []
for c, n in enumerate(names):
    objs = townsfolk.build_customer(n, mat)
    P = Matrix.Translation(Vector((c * 3.0, 0, 0)))
    for o in objs:
        o.matrix_world = P @ o.matrix_basis
        o.name = f"V{c}_{o.name}"
    allo += objs
bpy.context.view_layer.update()
cx = 3.0 * (len(names) - 1) / 2
scenes.shot(allo, f"{out}/cust-front-{tag}.png", (cx, -70, 3.0), (cx, 0, 2.6), 85, res=(2400, 560), samples=24)
scenes.shot(allo, f"{out}/cust-side-{tag}.png", (cx + 70, -8, 3.0), (cx, 0, 2.6), 85, res=(2400, 560), samples=24)
