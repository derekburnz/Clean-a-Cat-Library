"""Tub and wash stands with a 1.5 scale cat in each: python tubsheet.py <module dir> <out dir> <tag>"""
import sys, os
sys.path.insert(0, sys.argv[1])
import bpy
import common, palette, stations, worker_stations as ws, dirt, scenes, cats
out, tag = sys.argv[2], sys.argv[3]
png = os.path.join(out, palette.TEXTURE_NAME + ".png")
common.reset_scene(); palette.write_palette_png(png)
mat = common.palette_material(png)
seat_t = getattr(stations, "TUB_SEAT", stations.SEAT_Z)
allo = []
tub = stations.build_tub(mat)
cat = dirt.build_dirty("Smudge", mat, "sit")[0]
scenes._move(cat, (0, 0, seat_t), 1.5)
allo += tub + cat
for i, (who, name) in enumerate((("Jo", "Muffin"), ("Sam", "Inky"), ("Lou", "Cotton"))):
    x = 8.0 + 7.5 * i
    st = [o for o in ws.build_stand(who, mat) if not o.name.endswith("_Barrier")]
    scenes._move(st, (x, 0, 0))
    seat = ws.seat() if hasattr(ws, "seat") else (ws.BX, ws.BY, ws.SEAT)
    c = dirt.build_dirty(name, mat, "sit")[0]
    scenes._move(c, (x + seat[0], seat[1], seat[2]), 1.5)
    allo += st + c
bpy.context.view_layer.update()
scenes.shot(allo, f"{out}/tub-{tag}.png", (10.5, -36, 13), (10.5, 0, 1.8), 42, res=(2400, 900), samples=24, hide=("_Barrier",))
