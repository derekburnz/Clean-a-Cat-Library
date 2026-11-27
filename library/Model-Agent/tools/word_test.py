import os, sys
B = "/tmp/claude-0/-home-claude/74ceeba7-2031-5376-9b47-8e17893fae9d/scratchpad/wtpr/assets/clean-a-cat/blender"
sys.path.insert(0, B)
import bpy, common, palette, ui_renders, shop_art
out = sys.argv[-1]; os.makedirs(out, exist_ok=True)
common.reset_scene()
mat = common.palette_material(os.path.join(B, "..", "exports", palette.TEXTURE_NAME + ".png"))
objs = shop_art.word("2x", 1.5, (0,0,0), mat)
for o in objs:
    me=o.data; print(o.name, len(me.polygons), [round(c,2) for c in o.matrix_world.translation], me.uv_layers[0].data[0].uv[:], palette.uv_center(palette.idx(shop_art.WHITE)))
    import mathutils
    print(" bounds y", min((o.matrix_world@v.co).y for v in me.vertices), max((o.matrix_world@v.co).y for v in me.vertices))
ui_renders.shot(objs[:1], os.path.join(out, "face.png"), 256, shop_art.VIEW, samples=8)
