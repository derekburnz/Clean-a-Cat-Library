"""Tangles and fluff check: python furcheck.py <module dir> <out dir> <tag>. Env CATS=Muffin,Inky,Rosette BODY=sit"""
import sys, os
sys.path.insert(0, sys.argv[1])
import bpy
from mathutils import Matrix, Vector
import common, palette, cats, scenes, dirt
out, tag = sys.argv[2], sys.argv[3]
png = os.path.join(out, palette.TEXTURE_NAME + ".png")
common.reset_scene(); palette.write_palette_png(png)
mat = common.palette_material(png)
names = os.environ.get("CATS", "Muffin,Inky,Rosette").split(",")
body = os.environ.get("BODY", "sit")
dirty, brushed = [], []
for row, coll in ((0, dirty), (1, brushed)):
    for c, name in enumerate(names):
        objs, nest, attrs = dirt.build_dirty(name, mat, body)
        P = Matrix.Translation(Vector((c * 1.7, row * 0.0, 0)))
        for o in objs:
            o.matrix_world = P @ o.matrix_basis
            n = o.name
            if row == 0:
                o.hide_render = "_Fluff" in n or "_Claw" in n
            else:
                o.hide_render = "_Mud" in n or "_Tangle" in n or "_Claw" in n
            o.name = f"R{row}C{c}_{n}"
        coll += [o for o in objs if not o.hide_render]
        if row == 0:
            for o in objs: o.location.z += 0
bpy.context.view_layer.update()
cx = 1.7 * (len(names) - 1) / 2
W = (int(640 * len(names)), 640)
for label, objs in (("dirty", dirty), ("brushed", brushed)):
    others = [o for o in bpy.context.scene.objects if o.type == "MESH"]
    # front close (tub close up), then the play camera: high and three quarter
    scenes.shot(objs, f"{out}/{tag}-{label}-front.png", (cx, -26.0, 2.0), (cx, 0.0, 0.85), 150, res=W, samples=32)
    scenes.shot(objs, f"{out}/{tag}-{label}-play.png", (cx + 9, -17.0, 11.0), (cx, 0.0, 0.95), 100, res=W, samples=32)
