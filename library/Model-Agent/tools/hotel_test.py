import os, sys, math, json
B = "/tmp/claude-0/-home-claude/74ceeba7-2031-5376-9b47-8e17893fae9d/scratchpad/wtpr/assets/clean-a-cat/blender"
sys.path.insert(0, B); sys.path.insert(0, B+"/../../../.claude/skills/blender-asset-qa/scripts")
import bpy, common, palette, ui_renders, hotel, backdoor, qa_check
from mathutils import Vector
out = sys.argv[-1]; os.makedirs(out, exist_ok=True)
common.reset_scene()
mat = common.palette_material(os.path.join(B, "..", "exports", palette.TEXTURE_NAME + ".png"))
objs = hotel.build_hotel(mat)
q = qa_check.run(objects=[o.name for o in objs], profile="roblox", uv=False)
print("QA", q["errors"], q["warnings"])
print("TRIS", sum(len(o.data.polygons) for o in objs))
door = backdoor.build_open(mat)
roofless = os.environ.get("ROOF", "0") == "0"
# cutaway: hide the roof by rendering from above with the main shell split is not possible; use a high view through no roof by clipping
allo = [o for o in objs if 'WallArt' not in o.name] + door
F = (Vector((-9, 0, 0)), Vector((9, 12.5, 8)))
cam_views = {"top": (0, 86), "left": (-20, 48), "right": (25, 40)}
import bmesh
if roofless:
    main = objs[0]; bm = bmesh.new(); bm.from_mesh(main.data)
    kill = [f for f in bm.faces if all(v.co.z > 11.9 for v in f.verts) or (min(v.co.z for v in f.verts) > 12.0)]
    bmesh.ops.delete(bm, geom=kill, context="FACES"); 
    # drop front wall top strip and anything above 9.5 for a cutaway
    kill = [f for f in bm.faces if max(v.co.z for v in f.verts) >= 6.0 and max(v.co.y for v in f.verts) < 12.5 and (min(v.co.y for v in f.verts) < 1.2 or abs(sum(v.co.x for v in f.verts)/len(f.verts)) > 8.3 or min(v.co.z for v in f.verts) > 9)]
    bmesh.ops.delete(bm, geom=kill, context="FACES"); bm.to_mesh(main.data); bm.free()
for n, v in cam_views.items():
    ui_renders.shot(allo, os.path.join(out, n + ".png"), 800, v, focus=F, pad=1.05, samples=24)
