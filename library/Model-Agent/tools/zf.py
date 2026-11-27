import sys, os
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, os.path.join(sys.argv[1], "..", "..", "..", ".claude", "skills", "blender-asset-qa", "scripts"))
import bpy, bmesh
import common, palette, tools
from mathutils import Vector
png = "/tmp/claude-0/-home-claude/74ceeba7-2031-5376-9b47-8e17893fae9d/scratchpad/pal.png"
common.reset_scene(); palette.write_palette_png(png); mat = common.palette_material(png)
ob = tools.build_soap_bar(mat)[0]
me = ob.data
# list faces with normals and plane d; find coplanar overlapping pairs crudely
fs = [(p.normal.copy(), p.center.copy(), p.index) for p in me.polygons]
seen = {}
for n, c, i in fs:
    key = (round(n.x, 2), round(n.y, 2), round(n.z, 2), round(n.dot(c), 3))
    seen.setdefault(key, []).append(i)
for k, v in seen.items():
    if len(v) > 1 and abs(k[2]) > 0.9 or (len(v) > 1 and abs(k[1]) > 0.9) or (len(v) > 1 and abs(k[0]) > 0.9):
        cs = [tuple(round(x, 3) for x in me.polygons[i].center) for i in v[:4]]
        print(k, len(v), cs)
