import os, sys, math
B = "/tmp/claude-0/-home-claude/74ceeba7-2031-5376-9b47-8e17893fae9d/scratchpad/wtpr/assets/clean-a-cat/blender"
sys.path.insert(0, B)
import bpy, common, palette, ui_renders, backdoor
from mathutils import Vector
out = sys.argv[-1]; os.makedirs(out, exist_ok=True)
common.reset_scene()
mat = common.palette_material(os.path.join(B, "..", "exports", palette.TEXTURE_NAME + ".png"))
b = common.Builder()   # a stand-in wall with the opening
for x0, x1 in ((-9, -3), (3, 9)):
    b.box_base(((x0 + x1) / 2, 0, 0), (x1 - x0, 1.0, 12), "spa_cream", bevel=False)
b.box_base((0, 0, 9), (6, 1.0, 3), "spa_cream", bevel=False)
b.box_base((0, -4, -0.1), (18, 8, 0.1), "floor_tile", bevel=False)
wall = b.finalize("Wall", mat, bevel=0)
for name, fn in (("locked", backdoor.build_locked), ("open", backdoor.build_open)):
    objs = fn(mat)
    vis = [o for o in objs if not o.hide_render]
    for view in ((18, 14), (-30, 25)):
        ui_renders.shot(vis + [wall], os.path.join(out, f"{name}_{view[0]}.png"), 640, view, focus=(Vector((-4.5, -3.5, 0)), Vector((4.5, 1, 10))), pad=1.05, samples=16)
    if name == "open":
        ui_renders.shot(vis + [wall], os.path.join(out, f"{name}_back.png"), 640, (160, 25), focus=(Vector((-9.5, -1, 0)), Vector((4.5, 1.5, 10))), pad=1.05, samples=16)
    ui_renders._clear()
    wall = None
    b = common.Builder()
    for x0, x1 in ((-9, -3), (3, 9)):
        b.box_base(((x0 + x1) / 2, 0, 0), (x1 - x0, 1.0, 12), "spa_cream", bevel=False)
    b.box_base((0, 0, 9), (6, 1.0, 3), "spa_cream", bevel=False)
    b.box_base((0, -4, -0.1), (18, 8, 0.1), "floor_tile", bevel=False)
    wall = b.finalize("Wall", mat, bevel=0)
