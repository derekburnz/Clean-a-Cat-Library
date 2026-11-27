import sys, os, math
sys.path.insert(0, sys.argv[1])
import bpy
from mathutils import Matrix, Vector
import common, palette, townsfolk, scenes, spa_staff
out, tag = sys.argv[2], sys.argv[3]
png = os.path.join(out, palette.TEXTURE_NAME + ".png")
common.reset_scene(); palette.write_palette_png(png)
mat = common.palette_material(png)
items = [("c", n) for n in townsfolk.ALL_LOOKS] + [("s", n) for n in spa_staff.LOOKS]
def build(kind, n):
    return townsfolk.build_customer(n, mat) if kind == "c" else spa_staff.build_staff(n, mat)
def place(objs, P, pre):
    for o in objs:
        o.matrix_world = P @ o.matrix_basis
        o.name = f"{pre}_{o.name}"
    return objs
rows = {"back": 180, "right": 90, "left": -90}
groups = {}
for r, (view, deg) in enumerate(rows.items()):
    g = []
    for c, (k, n) in enumerate(items):
        R = Matrix.Rotation(math.radians(deg), 4, "Z")
        g += place(build(k, n), Matrix.Translation((c * 3.0, r * 40, 0)) @ R, f"{view[0]}{c}")
    groups[view] = (r, g)
bpy.context.view_layer.update()
cx = 3.0 * (len(items) - 1) / 2
for view, (r, g) in groups.items():
    scenes.shot(g, f"{out}/c-{view}-{tag}.png", (cx, r * 40 - 90, 3.0), (cx, r * 40, 2.6), 85, res=(3400, 520), samples=24)
print("ORDER", [n for _, n in items])
