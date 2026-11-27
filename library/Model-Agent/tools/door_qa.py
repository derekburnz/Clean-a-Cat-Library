import os, sys, json
B = "/tmp/claude-0/-home-claude/74ceeba7-2031-5376-9b47-8e17893fae9d/scratchpad/wtpr/assets/clean-a-cat/blender"
sys.path.insert(0, B); sys.path.insert(0, B+"/../../../.claude/skills/blender-asset-qa/scripts")
import bpy, common, palette, backdoor, qa_check, ui_renders
common.reset_scene()
mat = common.palette_material(os.path.join(B, "..", "exports", palette.TEXTURE_NAME + ".png"))
for off in ("_tape", "_sawhorse", "_planks", "_pot", "_cone"):
    keep = getattr(backdoor, off)
    setattr(backdoor, off, (lambda *a, **k: 2.67))
    objs = backdoor.build_locked(mat)
    q = qa_check.run(objects=[o.name for o in objs], profile="roblox", uv=False)
    print("WITHOUT", off, q["zfighting"])
    setattr(backdoor, off, keep)
    ui_renders._clear()
