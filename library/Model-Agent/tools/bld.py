import sys, os, math
sys.path.insert(0, sys.argv[1])
import bpy
from mathutils import Matrix
import common, palette, scenes, npc_builder, build_props, townsfolk, spa_staff
out = sys.argv[2]
png = os.path.join(out, palette.TEXTURE_NAME + ".png")
common.reset_scene(); palette.write_palette_png(png)
mat = common.palette_material(png)
def place(objs, P, pre):
    for o in objs:
        o.matrix_world = P @ o.matrix_basis
        o.name = f"{pre}_{o.name}"
    return objs
g = []
for c, deg in enumerate((0, 35, 90, 180, -90)):
    g += place(npc_builder.build_builder(mat), Matrix.Translation((c * 3.4, 0, 0)) @ Matrix.Rotation(math.radians(deg), 4, "Z"), f"v{c}")
g += place(townsfolk.build_customer("Rae", mat), Matrix.Translation((5 * 3.4, 0, 0)), "rae")
g += place(spa_staff.build_staff("Jo", mat), Matrix.Translation((6 * 3.4, 0, 0)), "jo")
bpy.context.view_layer.update()
cx = 3.4 * 6 / 2
scenes.shot(g, f"{out}/builder-views.png", (cx, -120, 3.4), (cx, 0, 3.2), 120, res=(2600, 560), samples=32)
