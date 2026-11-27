import os, sys, math
B = os.path.dirname(os.path.abspath(__file__)); 
sys.path.insert(0, os.environ["BL"])
import bpy
from mathutils import Matrix, Vector
import common, palette, plot, townsfolk, dirt, cats, scenes, store_art as sa
common.reset_scene()
mat = common.palette_material(os.path.join(os.environ["BL"], "..", "exports", palette.TEXTURE_NAME + ".png"))
objs = [o for o in plot.build_plot_big(mat) if not o.name.endswith(("_Roof", "_Glass", "_Barrier"))]
SP = plot.BIG["SPOTS"]; F = plot.FLOOR
def place(o, spot, lift=0.0, k=1.0, turn=None):
    x, y, z, t = SP[spot]; t = t if turn is None else turn
    M = Matrix.Translation((x, y, F + z + lift)) @ Matrix.Rotation(math.radians(t), 4, "Z") @ Matrix.Scale(k, 4)
    bpy.context.view_layer.update()
    for ob in o: ob.matrix_world = M @ ob.matrix_world
    return sa._fresh(o)
n = sum(1 for k in SP if k.startswith("SpotCounterCat"))
who = ["Bea", "Kit", "Juno", "Theo", "Vivi", "Mo"]; kinds = ["Muffin", "Smudge", "Patches", "Toffee", "Cotton", "Marble"]
for i in range(1, n + 1):
    look = dict(townsfolk.ALL_LOOKS[who[i - 1]]); print("LOOK", sorted(look)) if i == 1 else None; look["gloves"] = look.get("top") or look.get("shirt")
    c = townsfolk.build_figure(townsfolk.PREFIX + who[i - 1], look, mat, carry=False)
    x, y, z, t = SP["SpotCounter%d" % i]; SP["_c"] = (x + 1.6, y + 1.2, z, 180); objs += place(c, "_c")
    cat, _, _ = dirt.build_dirty(kinds[i - 1], mat, "sit")
    cat = [o for o in cat if "_Tangle" not in o.name and "_Fluff" not in o.name]
    objs += place(cat, "SpotCounterCat%d" % i, k=float(os.environ.get("CK", 1.3)), turn=180)
xs = [SP["SpotCounterCat%d" % i][0] for i in range(1, n + 1)]; cy = SP["SpotCounterCat1"][1]; cz = F + SP["SpotCounterCat1"][2]
print("N", n, xs, cy, cz, SP["SpotCounter1"])
cx = sum(xs) / n
eye = Vector((cx + float(os.environ.get("EX", 2)), cy + float(os.environ.get("EY", 9)), cz + float(os.environ.get("EZ", 2.5))))
scenes.shot(objs, os.environ["OUT"], eye, Vector((cx, cy, cz + 1.0)), lens=float(os.environ.get("LENS", 30)), res=(960, 540), samples=16)
