import sys, os, math
sys.path.insert(0, sys.argv[1])
import bpy
from mathutils import Matrix
import common, palette, townsfolk, scenes
out = sys.argv[2]
png = os.path.join(out, palette.TEXTURE_NAME + ".png")
common.reset_scene(); palette.write_palette_png(png)
mat = common.palette_material(png)
names = ("Sunny", "Mo", "Pip", "Rae", "Juno", "Bea", "Theo", "Kit")
def place(objs, P, pre):
    for o in objs:
        o.matrix_world = P @ o.matrix_basis
        o.name = f"{pre}_{o.name}"
    return objs
for r, (view, deg) in enumerate({"back": 180, "backq": 145, "side": 90}.items()):
    g = []
    for c, n in enumerate(names):
        g += place(townsfolk.build_customer(n, mat), Matrix.Translation((c * 3.2, r * 40, 0)) @ Matrix.Rotation(math.radians(deg), 4, "Z"), f"{view}{c}")
    bpy.context.view_layer.update()
    cx = 3.2 * (len(names) - 1) / 2
    scenes.shot(g, f"{out}/{view}.png", (cx, r * 40 - 120, 5.2), (cx, r * 40, 3.0), 130, res=(2400, 600), samples=24)
