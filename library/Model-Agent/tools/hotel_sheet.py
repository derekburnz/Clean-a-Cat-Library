import os, sys, math
B = "/tmp/claude-0/-home-claude/74ceeba7-2031-5376-9b47-8e17893fae9d/scratchpad/wtpr/assets/clean-a-cat/blender"
sys.path.insert(0, B)
import bpy, bmesh, common, palette, ui_renders, hotel, backdoor, cats, scenes
from mathutils import Vector, Matrix
out = sys.argv[-1]; os.makedirs(out, exist_ok=True)
common.reset_scene()
mat = common.palette_material(os.path.join(B, "..", "exports", palette.TEXTURE_NAME + ".png"))
objs = hotel.build_hotel(mat)
n = [0]
def put(o2, x, y, z, turn=0.0, tag="p"):
    n[0] += 1
    bpy.context.view_layer.update()
    M = Matrix.Translation((x, y, z)) @ Matrix.Rotation(math.radians(turn), 4, "Z")
    for o in o2:
        o.matrix_world = M @ o.matrix_world; o.name = f"{tag}{n[0]}_{o.name}"
    return o2
extra = put(backdoor.build_open(mat), 0, 0, 0)
mx, my = hotel.MAT_AT
extra += put(cats.build_cat("Muffin", mat, body="sit"), mx, my, hotel.FLOOR_UP + 0.05, 90)
extra += put(hotel.build_suitcase(mat), mx - 0.2, my - 1.1, hotel.FLOOR_UP + 0.05, 60)
extra += put(cats.build_cat("Cotton", mat, body="sit"), hotel.ROOM_X[0], hotel.BED_Y, hotel.BED_TOP, 180)
extra += put(cats.build_cat("Sherbet", mat, body="sit"), hotel.ROOM_X[1], hotel.BED_Y, hotel.BED_TOP, 180)
main = objs[0]; bm = bmesh.new(); bm.from_mesh(main.data)
kill = [f for f in bm.faces if all(v.co.z > 11.9 for v in f.verts) or (min(v.co.z for v in f.verts) > 12.0)]
bmesh.ops.delete(bm, geom=kill, context="FACES")
kill = [f for f in bm.faces if max(v.co.z for v in f.verts) >= 6.0 and max(v.co.y for v in f.verts) < 12.5 and (min(v.co.y for v in f.verts) < 1.2 or abs(sum(v.co.x for v in f.verts)/len(f.verts)) > 8.3 or min(v.co.z for v in f.verts) > 9)]
bmesh.ops.delete(bm, geom=kill, context="FACES"); bm.to_mesh(main.data); bm.free()
allo = [o for o in objs if "WallArt" not in o.name] + extra
F = (Vector((-9, 0, 0)), Vector((9, 12.5, 8)))
SKIP = 1
if 0:
  ui_renders.shot(allo, os.path.join(out, "top.png"), 800, (0, 86), focus=F, pad=1.05, samples=32)
  ui_renders.shot(allo, os.path.join(out, "left.png"), 800, (-20, 48), focus=F, pad=1.05, samples=32)
  ui_renders.shot(allo, os.path.join(out, "desk.png"), 800, (-30, 28), focus=(Vector((1.5, 0.8, 0)), Vector((8.6, 6.5, 6))), pad=1.05, samples=32)
nob = [o for o in allo if "Build_Decor" not in o.name]
ui_renders.shot(nob, os.path.join(out, "locked.png"), 800, (-12, 52), focus=(Vector((0, 6.0, 0)), Vector((8.6, 12, 5))), pad=1.05, samples=32)
ui_renders.shot(allo, os.path.join(out, "building.png"), 800, (-12, 52), focus=(Vector((0, 6.0, 0)), Vector((8.6, 12, 5))), pad=1.05, samples=32)
ui_renders.shot(nob, os.path.join(out, "rooms.png"), 800, (12, 52), focus=(Vector((-8.6, 6.0, 0)), Vector((0, 12, 5))), pad=1.05, samples=32)
ui_renders._clear()
common.reset_scene(); mat = common.palette_material(os.path.join(B, "..", "exports", palette.TEXTURE_NAME + ".png"))
b = common.Builder()
for x0, x1 in ((-9, -3), (3, 9)):
    b.box_base(((x0 + x1) / 2, 0, 0), (x1 - x0, 1.0, 12), "spa_cream", bevel=False)
b.box_base((0, 0, 9), (6, 1.0, 3), "spa_cream", bevel=False)
b.box_base((0, -4, -0.1), (18, 8, 0.1), "floor_tile", bevel=False)
w = b.finalize("Wall", mat, bevel=0)
o2 = [o for o in hotel.build_door_building(mat) if not o.hide_render] + [w]
ui_renders.shot(o2, os.path.join(out, "doorbuild.png"), 800, (18, 14), focus=(Vector((-4.5, -3.5, 0)), Vector((4.5, 1, 10))), pad=1.05, samples=32)
ui_renders._clear()
common.reset_scene(); mat = common.palette_material(os.path.join(B, "..", "exports", palette.TEXTURE_NAME + ".png"))
o3 = hotel.build_hotel(mat) + put(backdoor.build_open(mat), 0, 0, 0)
ui_renders.shot([o for o in o3 if not o.hide_render], os.path.join(out, "outside.png"), 800, (150, 22), samples=32)

