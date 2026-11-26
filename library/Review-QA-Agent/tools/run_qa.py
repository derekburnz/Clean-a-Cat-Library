# usage: python3 run_qa.py <fbx> [qa args...]  imports the FBX, applies the import's unit scale, runs qa_check
import sys, runpy, bpy
fbx = sys.argv[1]; extra = sys.argv[2:]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.fbx(filepath=fbx)
for o in bpy.data.objects:
    o.select_set(o.type == 'MESH')
bpy.context.view_layer.objects.active = next(o for o in bpy.data.objects if o.type == 'MESH')
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
for o in bpy.data.objects:
    if o.type == 'MESH':
        o.scale = (100, 100, 100); o.location = o.location * 100
bpy.context.view_layer.update()
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
for o in bpy.data.objects:
    if o.type == 'MESH':
        print("DIMS", o.name, [round(v, 3) for v in o.dimensions], file=sys.stderr)
sys.argv = ["qa_check.py", "--"] + extra
runpy.run_path(__import__("os").environ.get("GAME_REPO","/home/claude/Clean-a-Cat")+"/.claude/skills/blender-asset-qa/scripts/qa_check.py", run_name="__main__")
