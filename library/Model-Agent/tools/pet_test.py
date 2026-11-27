import os, sys
B = "/tmp/claude-0/-home-claude/74ceeba7-2031-5376-9b47-8e17893fae9d/scratchpad/wtpr/assets/clean-a-cat/blender"
sys.path.insert(0, B)
import bpy, common, palette, build_all, pets
common.reset_scene()
mat = common.palette_material(os.path.join(B, "..", "exports", palette.TEXTURE_NAME + ".png"))
makers = build_all.all_assets()
objs = makers[pets.PREFIX + "Clover"][0](mat)
bpy.context.view_layer.update()
for o in objs: print(o.name, o.parent.name if o.parent else None, [round(c,2) for c in o.matrix_world.translation], [round(c,2) for c in o.dimensions])
