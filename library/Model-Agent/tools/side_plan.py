import os, sys
sys.path.insert(0, os.environ["BL"])
import bpy
from mathutils import Vector
import common, palette, hotel, garden, scenes
common.reset_scene()
mat = common.palette_material(os.path.join(os.environ["BL"], "..", "exports", palette.TEXTURE_NAME + ".png"))
which = os.environ.get("G", "garden")
g = []
h = hotel.build_hotel(mat)
g = garden.ASSETS[os.environ.get("GN", "CleanACat_Area_GardenSide")][0](mat)
bpy.context.view_layer.update()
for o in g: o.location.x += 19.0
objs = [o for o in g + h if not o.name.endswith(("_Barrier", "_Canopy")) and "Roof" not in o.name]
ex, ey, ez = [float(v) for v in os.environ.get("EYE", "9.5,6.5,46").split(",")]
tx, ty, tz = [float(v) for v in os.environ.get("TGT", "9.5,6.6,0").split(",")]
scenes.shot(objs, os.environ["OUT"], Vector((ex, ey, ez)), Vector((tx, ty, tz)), lens=float(os.environ.get("LENS", 32)), res=(1280, 720), samples=12, hide=tuple(os.environ.get("HIDE", "Zzz").split(",")))
