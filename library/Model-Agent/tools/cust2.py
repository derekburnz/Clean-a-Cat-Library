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
def place(objs, P, pre):
    for o in objs:
        o.matrix_world = P @ o.matrix_basis
        o.name = f"{pre}_{o.name}"
    return objs
front, side = [], []
for c, n in enumerate(names):
    front += place(townsfolk.build_customer(n, mat), Matrix.Translation((c * 3.0, 0, 0)), f"F{c}")
for c, n in enumerate(names):
    # side: each turned to show its right side to a camera on -X... spaced along X, turned 90 degrees
    R = Matrix.Rotation(math.radians(90), 4, "Z")
    side += place(townsfolk.build_customer(n, mat), Matrix.Translation((c * 3.0, 30, 0)) @ R, f"S{c}")
bpy.context.view_layer.update()
cx = 3.0 * (len(names) - 1) / 2
scenes.shot(front, f"{out}/c874-front-{tag}.png", (cx, -70, 3.0), (cx, 0, 2.6), 85, res=(2400, 560), samples=24)
scenes.shot(side, f"{out}/c874-side-{tag}.png", (cx, 30 - 70, 3.0), (cx, 30, 2.6), 85, res=(2400, 560), samples=24)
