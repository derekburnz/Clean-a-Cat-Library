"""Print where z-fighting tri pairs are, per pet. Run from blender/: python zfwhere.py Nebula,Blaze"""
import sys, os
sys.path.insert(0, os.getcwd())
import bpy  # noqa
import common, palette, crates
from mathutils.bvhtree import BVHTree
common.reset_scene()
png = os.path.join(sys.argv[2] if len(sys.argv) > 2 else "/tmp", palette.TEXTURE_NAME + ".png")
palette.write_palette_png(png)
mat = common.palette_material(png)
for name in sys.argv[1].split(","):
    common.hide_all_meshes()
    objs = crates.build_pet_crate(mat, gift=True)
    dg = bpy.context.evaluated_depsgraph_get()
    verts, tris, meta = [], [], []
    for oi, ob in enumerate(objs):
        me = ob.evaluated_get(dg).to_mesh(); me.calc_loop_triangles()
        base = len(verts)
        verts += [ob.matrix_world @ v.co for v in me.vertices]
        for lt in me.loop_triangles:
            t = tuple(base + i for i in lt.vertices); tris.append(t)
            a, b, c = (verts[i] for i in t); n = (b - a).cross(c - a)
            meta.append((oi, n.normalized() if n.length > 1e-12 else n))
    bvh = BVHTree.FromPolygons(verts, tris, epsilon=0.0)
    from qa_check import _point_in_tri
    out = {}
    for ti, t in enumerate(tris):
        a, b, c = (verts[i] for i in t); n = meta[ti][1]
        if n.length < 0.5: continue
        cen = (a + b + c) / 3
        for p in (cen, cen.lerp(a, .6), cen.lerp(b, .6), cen.lerp(c, .6)):
            for _, _, tj, _ in bvh.find_nearest_range(p, 0.001):
                if tj is None or tj == ti or set(t) & set(tris[tj]): continue
                n2 = meta[tj][1]; d = n.dot(n2)
                if d < 0.999: continue
                a2, b2, c2 = (verts[i] for i in tris[tj])
                q = p - n2 * n2.dot(p - a2)
                if _point_in_tri(q, a2, b2, c2, n2):
                    k = (min(ti, tj), max(ti, tj)); out[k] = (objs[meta[ti][0]].name, objs[meta[tj][0]].name, tuple(round(x, 3) for x in cen), tuple(round(x, 2) for x in n))
    print(name, len(out))
    for v in sorted(out.values()): print("  ", v)
