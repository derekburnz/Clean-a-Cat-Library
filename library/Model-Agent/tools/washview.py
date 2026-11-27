"""The wash room as the wash camera sees it, with the tub and a cat: python washview.py <module dir> <out dir> <tag>"""
import sys, os, math
sys.path.insert(0, sys.argv[1])
import bpy
from mathutils import Matrix, Vector
import common, palette, cats, stations, wash_room, scenes
out, tag = sys.argv[2], sys.argv[3]
png = os.path.join(out, palette.TEXTURE_NAME + ".png")
common.reset_scene(); palette.write_palette_png(png)
mat = common.palette_material(png)
if os.environ.get("PLACEHOLDER"):
    from common import Builder
    pb = Builder(); H, T = 13.0, 1.0; sp = 2 * H + 2 * T
    pb.box_base((0, 0, 0.05 - T), (sp, sp, T), "spa_tile", bevel=False)
    pb.box_base((0, 0, 12.0), (sp - 0.1, sp - 0.1, T), "spa_mint", bevel=False)
    for sy in (1, -1):
        pb.box_base((0, sy * (H + T / 2), 0), (sp - 0.2, T, 12.0), "spa_mint", bevel=False)
        pb.box_base((sy * (H + T / 2), 0, 0), (T, sp - 0.3, 12.0), "spa_mint", bevel=False)
    room = [pb.finalize("PH_Room", mat)]
else:
    room = wash_room.build_wash_room(mat)
tub = stations.build_tub(mat)
for o in tub:
    o.matrix_world = Matrix.Scale(1.3, 4) @ o.matrix_basis
cat = cats.build_cat(os.environ.get("CAT", "Bathtile"), mat, body="sit")
for o in cat:
    o.matrix_world = Matrix.Translation((0, 0, stations.SEAT_Z * 1.3)) @ Matrix.Scale(1.5, 4) @ o.matrix_basis
    o.hide_render = "_Fluff" in o.name or "_Claw" in o.name
for o in room:
    o.visible_shadow = False
objs = room + tub + cat
bpy.context.view_layer.update()
_real = common.render_still
def _still(*a, **k):
    f = bpy.data.objects.get("_PreviewFloor")
    if f: f.hide_render = True
    return _real(*a, **k)
common.render_still = _still
eye = Vector((0, -9.0, 4.2)); tgt = Vector((0, 0, 2.6))
scenes.shot(objs, os.path.join(out, f"phone_{tag}.png"), eye, tgt, 11.8, res=(1560, 720), samples=48)
if os.environ.get("WIDE"): scenes.shot(objs, os.path.join(out, f"wide_{tag}.png"), (9.0, -12.4, 9.5), (0, 3.0, 3.5), 14, res=(1400, 900), samples=48)
