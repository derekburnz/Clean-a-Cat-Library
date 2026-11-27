import sys, json
sys.path.insert(0, ".")
import build_all, gates
m = json.load(open("../exports/manifest.json"))
gates.write_report("../exports/gates.md", m, build_all.ROOT)
