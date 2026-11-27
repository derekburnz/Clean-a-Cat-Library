"""Street with six big plots and the backdrop: streettop.py <module dir> <out> <big|wide>"""
import sys, os
sys.path.insert(0, sys.argv[1])
import bpy
from mathutils import Matrix
import common, palette, plot, street, backdrop, scenes
out, kind = sys.argv[2], sys.argv[3]
png = os.path.join(out, palette.TEXTURE_NAME + ".png")
common.reset_scene(); palette.write_palette_png(png)
mat = common.palette_material(png)
lay = street.big_layout if kind == "big" else street.wide_layout
with plot.big_layout():
    p0 = [o for o in plot.build_plot(mat) if not any(s in o.name for s in ("_Barrier",))]
allo = list(p0)
with lay():
    xs = list(street.XS)
    allo += [o for o in street.build_street(mat) if not o.name.endswith("_Barrier")]
allo += (backdrop.build_backdrop_big if kind == "big" else backdrop.build_backdrop_wide)(mat)
for x in xs[1:]:
    for o in p0:
        c = o.copy(); bpy.context.scene.collection.objects.link(c)
        c.matrix_world = Matrix.Translation((x, 0, 0)) @ o.matrix_world
        allo.append(c)
_rs = common.render_still
def _still(*a, **k):
    fl = bpy.data.objects.get('_PreviewFloor')
    if fl: fl.hide_render = True
    bpy.context.scene.camera.data.clip_end = 6000.0
    return _rs(*a, **k)
common.render_still = _still
import rbx_export
for o in list(allo):
    lk = rbx_export.LOOKS.get(o.name.split('.')[0])
    if lk and o.type == 'MESH':
        m = bpy.data.materials.new(o.name + '_look'); m.use_nodes = True
        bs = m.node_tree.nodes.get('Principled BSDF'); bs.inputs['Base Color'].default_value = (*[c ** 2.2 for c in lk[0]], 1)
        bs.inputs['Roughness'].default_value = 0.9
        o.data.materials.clear(); o.data.materials.append(m)
bpy.context.view_layer.update()
cx = (min(xs) + max(xs)) / 2
V = [("air", (cx, -330, 260), (cx, 10, 0), 30), ("back", (cx + 20, -20, 28), (cx + 20, 400, 4), 18), ("front", (cx - 30, 40, 28), (cx - 30, -400, 4), 18), ("road", (cx + 40, -50, 6), (900, -40, 12), 18), ("orbit", (cx - 700, -1100, 600), (cx, 0, 0), 30)]
for nm, e, t, l in V:
    if nm in os.environ.get("VIEWS", "air,back,front,road,orbit").split(","):
        scenes.shot(allo, f"{out}/edge-{kind}-{nm}.png", e, t, l, res=(1600, 900), samples=12, hide=("_Barrier",))
