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
    return _rs(*a, **k)
common.render_still = _still
bpy.context.view_layer.update()
cx = (min(xs) + max(xs)) / 2
scenes.shot(allo, f"{out}/street-{kind}-air.png", (cx, -330, 260), (cx, 10, 0), 30, res=(1800, 1000), samples=16, hide=("_Barrier",))
scenes.shot(allo, f"{out}/street-{kind}-walk.png", (42, -52, 9), (-20, 10, 4), 24, res=(1600, 900), samples=16, hide=("_Barrier",))
