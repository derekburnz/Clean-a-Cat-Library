import os, sys, math
B = "/tmp/claude-0/-home-claude/74ceeba7-2031-5376-9b47-8e17893fae9d/scratchpad/wtpr/assets/clean-a-cat/blender"
sys.path.insert(0, B)
import bpy, common, palette, ui_renders, backdoor, plot, vip, scenes
from mathutils import Vector, Matrix
out = sys.argv[-1]; os.makedirs(out, exist_ok=True)
common.reset_scene()
mat = common.palette_material(os.path.join(B, "..", "exports", palette.TEXTURE_NAME + ".png"))
def wall():
    b = common.Builder()
    for x0, x1 in ((-9, -3), (3, 9)):
        b.box_base(((x0 + x1) / 2, 0, 0), (x1 - x0, 1.0, 12), "spa_cream", bevel=False)
    b.box_base((0, 0, 9), (6, 1.0, 3), "spa_cream", bevel=False)
    b.box_base((0, -4, -0.1), (18, 8, 0.1), "floor_tile", bevel=False)
    return b.finalize("Wall", mat, bevel=0)
F = (Vector((-4.5, -3.5, 0)), Vector((4.5, 1, 10)))
w = wall(); objs = [o for o in backdoor.build_locked(mat) if not o.hide_render] + [w]
ui_renders.shot(objs, os.path.join(out, "locked_front.png"), 640, (18, 14), focus=F, pad=1.05, samples=32)
ui_renders.shot(objs, os.path.join(out, "locked_side.png"), 640, (-35, 28), focus=F, pad=1.05, samples=32)
ui_renders.shot(objs, os.path.join(out, "locked_close.png"), 640, (10, 10), focus=(Vector((-3.2, -3.2, 0)), Vector((3.2, 0, 6.2))), pad=1.05, samples=32)
ui_renders._clear()
def put(objs, spot):
    x, y, z, t = plot.SPOTS[spot]
    M = Matrix.Translation((x, y, plot.FLOOR + z)) @ Matrix.Rotation(math.radians(t), 4, "Z")
    bpy.context.view_layer.update()
    for o in objs:
        o.matrix_world = M @ o.matrix_world
    return [o for o in objs if not o.hide_render and "_Barrier" not in o.name]
for tag in ("before", "after"):
    common.reset_scene(); mat = common.palette_material(os.path.join(B, "..", "exports", palette.TEXTURE_NAME + ".png"))
    allo = [o for o in plot.build_plot(mat) if not any(s in o.name for s in ("_Roof", "_Barrier", "_Canopy"))]
    allo += put(backdoor.build_locked(mat), "SpotGardenDoor")
    allo += put(vip.build_vip_locked(mat) if tag == "before" else backdoor.build_fill(mat), "SpotVipDoor")
    bpy.context.view_layer.update()
    scenes.shot(allo, f"{out}/wall_{tag}.png", (-2, -13, 9), (-2, 10, 5.5), 15, res=(1280, 640), samples=24, hide=("_Roof", "_Barrier"))
    if tag == "after":
        scenes.shot(allo, f"{out}/wall_outside.png", (16, 34, 12), (4, 10, 4), 24, res=(640, 640), samples=24, hide=("_Roof", "_Barrier"))
