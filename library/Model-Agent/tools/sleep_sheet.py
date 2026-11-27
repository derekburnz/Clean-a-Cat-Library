import os, sys, math
B = "/tmp/claude-0/-home-claude/74ceeba7-2031-5376-9b47-8e17893fae9d/scratchpad/wtpr/assets/clean-a-cat/blender"
sys.path.insert(0, B)
import bpy, bmesh, common, palette, ui_renders, hotel, loaf, cats
from mathutils import Vector, Matrix
out = sys.argv[-1]
common.reset_scene()
mat = common.palette_material(os.path.join(B, "..", "exports", palette.TEXTURE_NAME + ".png"))
objs = hotel.build_hotel(mat)
n = [0]
def put(o2, x, y, z, turn=0.0):
    n[0] += 1
    bpy.context.view_layer.update()
    M = Matrix.Translation((x, y, z)) @ Matrix.Rotation(math.radians(turn), 4, "Z")
    for o in o2:
        o.matrix_world = M @ o.matrix_world; o.name = f"p{n[0]}_{o.name}"
    return o2
extra = []
for i, nm in enumerate(("Muffin", "Inky", "Cotton", "Marble")):
    extra += put(loaf.build_sleep(nm, mat)[0], hotel.ROOM_X[i], hotel.BED_Y - 0.1, hotel.BED_TOP, 0)
main = objs[0]; bm = bmesh.new(); bm.from_mesh(main.data)
kill = [f for f in bm.faces if all(v.co.z > 11.9 for v in f.verts) or (min(v.co.z for v in f.verts) > 12.0)]
bmesh.ops.delete(bm, geom=kill, context="FACES")
kill = [f for f in bm.faces if max(v.co.z for v in f.verts) >= 6.0 and max(v.co.y for v in f.verts) < 12.5 and (min(v.co.y for v in f.verts) < 1.2 or abs(sum(v.co.x for v in f.verts)/len(f.verts)) > 8.3 or min(v.co.z for v in f.verts) > 9)]
bmesh.ops.delete(bm, geom=kill, context="FACES"); bm.to_mesh(main.data); bm.free()
allo = [o for o in objs if not any(s in o.name for s in ("WallArt", "Lock_Decor", "Build_Decor"))] + extra
ui_renders.shot(allo, os.path.join(out, "beds.png"), 1400, (0, 58), focus=(Vector((-8.6, 7.5, 0)), Vector((8.6, 12, 4))), pad=1.03, samples=32)
ui_renders.shot(allo, os.path.join(out, "bed1.png"), 700, (10, 40), focus=(Vector((-8.2, 8.6, 0)), Vector((-4.3, 12, 3.4))), pad=1.03, samples=32)
