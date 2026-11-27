import sys, os, math
sys.path.insert(0, sys.argv[1])
import bpy
from mathutils import Matrix
import common, palette, townsfolk, scenes, spa_staff
out, tag = sys.argv[2], sys.argv[3]
png = os.path.join(out, palette.TEXTURE_NAME + ".png")
common.reset_scene(); palette.write_palette_png(png)
mat = common.palette_material(png)
items = [("c", n) for n in ("Pip", "Juno", "Rae", "Kit", "Rex")] + [("s", n) for n in ("Jo", "Sam", "Lou")]
def build(k, n):
    return townsfolk.build_customer(n, mat) if k == "c" else spa_staff.build_staff(n, mat)
def place(objs, P, pre):
    for o in objs:
        o.matrix_world = P @ o.matrix_basis
        o.name = f"{pre}_{o.name}"
    return objs
for r, (view, deg) in enumerate({"side": 90, "back": 180}.items()):
    g = []
    for c, (k, n) in enumerate(items):
        g += place(build(k, n), Matrix.Translation((c * 3.2, r * 40, 0)) @ Matrix.Rotation(math.radians(deg), 4, "Z"), f"{view}{c}")
    bpy.context.view_layer.update()
    cx = 3.2 * (len(items) - 1) / 2
    scenes.shot(g, f"{out}/s-{view}-{tag}.png", (cx, r * 40 - 120, 3.2), (cx, r * 40, 3.2), 130, res=(2400, 560), samples=24)
