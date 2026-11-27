import os, sys, math
B = "/tmp/claude-0/-home-claude/74ceeba7-2031-5376-9b47-8e17893fae9d/scratchpad/wtpr/assets/clean-a-cat/blender"
sys.path.insert(0, B)
import bpy, common, palette, ui_renders, backdoor
from mathutils import Vector
out = sys.argv[-1]; os.makedirs(out, exist_ok=True)
common.reset_scene()
mat = common.palette_material(os.path.join(B, "..", "exports", palette.TEXTURE_NAME + ".png"))
def wall():
    b = common.Builder()
    for x0, x1 in ((-9, -3), (3, 9)):
        b.box_base(((x0 + x1) / 2, 0, 0), (x1 - x0, 1.0, 12), "spa_cream", bevel=False)
    b.box_base((0, 0, 9), (6, 1.0, 3), "spa_cream", bevel=False)
    b.box_base((0, -4, -0.1), (18, 8, 0.1), "floor_tile", bevel=False)
    b.box_base((0, 6, -0.1), (18, 12, 0.1), "eye_green", bevel=False)
    return b.finalize("Wall", mat, bevel=0)
F = (Vector((-4.5, -3.5, 0)), Vector((4.5, 1, 10)))
w = wall()
ui_renders.shot([w], os.path.join(out, "before.png"), 640, (18, 14), focus=F, pad=1.05, samples=32); ui_renders._clear()
for name, fn in (("locked", backdoor.build_locked), ("open", backdoor.build_open)):
    w = wall(); objs = [o for o in fn(mat) if not o.hide_render] + [w]
    ui_renders.shot(objs, os.path.join(out, f"{name}_front.png"), 640, (18, 14), focus=F, pad=1.05, samples=32)
    ui_renders.shot(objs, os.path.join(out, f"{name}_side.png"), 640, (-35, 28), focus=F, pad=1.05, samples=32)
    if name == "open":
        ui_renders.shot(objs, os.path.join(out, "open_yard.png"), 640, (160, 25), focus=(Vector((-9.5, -1, 0)), Vector((4.5, 1.5, 10))), pad=1.05, samples=32)
    else:
        ui_renders.shot(objs, os.path.join(out, "locked_close.png"), 640, (10, 10), focus=(Vector((-3.2, -3.2, 0)), Vector((3.2, 0, 4.2))), pad=1.05, samples=32)
    ui_renders._clear()
