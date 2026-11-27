import os, sys, math, json
B = "/tmp/claude-0/-home-claude/74ceeba7-2031-5376-9b47-8e17893fae9d/scratchpad/wtpr/assets/clean-a-cat/blender"
sys.path.insert(0, B); sys.path.insert(0, "/tmp/claude-0/-home-claude/74ceeba7-2031-5376-9b47-8e17893fae9d/scratchpad/qadbg"); sys.path.append(B+"/../../../.claude/skills/blender-asset-qa/scripts")
import bpy, qa_check, common, palette, ui_renders, hotel, backdoor, qa_check
from mathutils import Vector
out = sys.argv[-1]; os.makedirs(out, exist_ok=True)
common.reset_scene()
mat = common.palette_material(os.path.join(B, "..", "exports", palette.TEXTURE_NAME + ".png"))
objs = hotel.build_hotel(mat)
q = qa_check.run(objects=[o.name for o in objs], profile="roblox", uv=False)
print("QA", q["errors"], q["warnings"])
print("TRIS", sum(len(o.data.polygons) for o in objs))
