"""People's faces: python peoplefaces.py <module dir> <out prefix>"""
import sys, os
sys.path.insert(0, sys.argv[1])
import bpy
from mathutils import Matrix, Vector
import common, palette, townsfolk, spa_staff, scenes
out = sys.argv[2]; d = os.path.dirname(out)
png = os.path.join(d, palette.TEXTURE_NAME + ".png")
def row(builders, key, close):
    common.reset_scene(); palette.write_palette_png(png)
    mat = common.palette_material(png)
    allo = []
    for c, fn in enumerate(builders):
        objs = fn(mat)
        P = Matrix.Translation(Vector((c * 2.6, 0, 0)))
        for o in objs:
            o.location.x += c * 2.6
            o.name = f"V{c}_{o.name}"
        allo += objs
    bpy.context.view_layer.update()
    cx = 2.6 * (len(builders) - 1) / 2
    if close:
        scenes.shot(allo, f"{out}_{key}.png", (cx, -60.0, 5.2), (cx, 0.0, 4.25), 130, res=(1900, 300), hide=())
    else:
        scenes.shot(allo, f"{out}_{key}.png", (cx + 6, -40.0, 16.0), (cx, 0.0, 2.6), 70, res=(1900, 600), hide=())
names = list(townsfolk.LOOKS)
staff = [lambda m, n=n: spa_staff.build_staff(n, m) for n in spa_staff.LOOKS]
cust = lambda ns: [lambda m, n=n: townsfolk.build_figure("CleanACat_NPC_Customer_" + n, townsfolk.LOOKS[n], m) for n in ns]
row(staff + cust(names[:3]), "a", True)
row(cust(names[3:9]), "b", True)
row(staff + cust(names[:3]), "far", False)
