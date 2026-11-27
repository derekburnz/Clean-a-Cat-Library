import os, sys
B = "/tmp/claude-0/-home-claude/74ceeba7-2031-5376-9b47-8e17893fae9d/scratchpad/wtpr/assets/clean-a-cat/blender"
sys.path.insert(0, B)
import bpy, common, palette, ui_renders, staff_busts
out = sys.argv[-1]; os.makedirs(out, exist_ok=True)
names = os.environ.get("NAMES", "Jo,Sam,Lou").split(",")
common.reset_scene()
mat = common.palette_material(os.path.join(B, "..", "exports", palette.TEXTURE_NAME + ".png"))
for n in names:
    objs = staff_busts.build_bust(n, mat)
    ui_renders.shot(objs, os.path.join(out, f"portrait_Staff_{n}.png"), int(os.environ.get("RES", "512")),
                    ui_renders.PORTRAIT_VIEW, focus=staff_busts.bust_focus(n), pad=1.04, samples=int(os.environ.get("SAMP", "24")))
    ui_renders._clear()
    print("done", n)
