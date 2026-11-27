"""The big spa from above with the tub and the three stands on their spots: plottop.py <module dir> <out> <tag>"""
import sys, os, math
sys.path.insert(0, sys.argv[1])
import bpy
from mathutils import Matrix
import common, palette, stations, worker_stations as ws, plot, scenes
out, tag = sys.argv[2], sys.argv[3]
png = os.path.join(out, palette.TEXTURE_NAME + ".png")
common.reset_scene(); palette.write_palette_png(png)
mat = common.palette_material(png)
allo = []
with plot.big_layout():
    allo += [o for o in plot.build_plot(mat) if not any(s in o.name for s in ("_Roof", "_Barrier", "_Canopy"))]
    spots = dict(plot.SPOTS)
def put(objs, spot):
    x, y, z, t = spots[spot]
    M = Matrix.Translation((x, y, plot.FLOOR + z)) @ Matrix.Rotation(math.radians(t), 4, "Z")
    for o in objs:
        o.matrix_world = M @ o.matrix_world
    return objs
allo += put(stations.build_tub(mat), "SpotTub")
for who in ("Jo", "Sam", "Lou"):
    allo += put([o for o in ws.build_stand(who, mat) if not o.name.endswith("_Barrier")], "SpotWorker" + who)
bpy.context.view_layer.update()
scenes.shot(allo, f"{out}/plot-{tag}.png", (0, -14, 70), (0, 4, 0), 24, res=(1800, 1400), samples=16, hide=("_Roof", "_Barrier"))
