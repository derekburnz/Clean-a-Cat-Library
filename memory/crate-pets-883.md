---
name: crate-pets-883
description: The eight crate pets remade for issue 883 (2026-11-27): names, PR, portrait ids, and the rename and old model removal order.
metadata:
  type: project
  modified: 2026-11-27T00:36:25.516Z
---

Derek asked on dev 2026-11-26 (#883) for cool pets like the old Catch a Cat Cafe secret cats. Model-Agent built eight new pets in PR 962 (2026-11-27). Names come from Design-Agent: Clover and Ghost (Common), Ooze and Glitch (Uncommon), Angler and Nebula (Rare), Dragon (Epic), Blaze (Legendary). Blaze is not called Phoenix, so it is never confused with the special customer's Phoenix.

Face portraits were uploaded to the group 2026-11-27 (CleanACat_UI_Portrait_Pet_<Name>.png):
- Clover 87691200049996
- Ghost 85397860599687
- Ooze 129987399664489
- Glitch 115707461545852
- Angler 107617453014958
- Nebula 118688157626872
- Dragon 119730475255717
- Blaze 133643213662061

Design-Agent adds them to Portraits.luau after the rename.

Order of the switch:
1. Gameplay-Engineer renames CrateRules and maps saved old ids to the new ones. Their PR goes up after their PR 963.
2. Then Model-Agent removes the old eight models: Cozy, Scrubby, Pebble, Pickle, Koi, Bamboo, Coral and Nimbus.

Until then both sets stay in rbx/. See also [[milestone-1-models]].
