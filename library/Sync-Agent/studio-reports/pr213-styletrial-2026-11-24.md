# PR #213 style trial capture, head 7c45539 (2026-11-24)
Pictures: https://github.com/derekburnz/Clean-a-Cat/pull/216 (draft, branch claude/styletrial-2026-11-24-captures; 13 jpgs + README in docs/concepts/clean-a-cat/styletrial-2026-11-24/). No assignee, no review requests.
Fresh local place, never saved. Switch LiveFlag_styleSheetUi.

Finding: switching it on mid-session does not show the card; UI.init builds it only if the switch is already on at client start. Live, a player sees it only after rejoining. Captures used StyleTrial.build(gui,true) and (gui,false).

Measured (points; top bar 58 on every preset). Card 340x256, Done 160x52, X 52x52, centred.
- iPhone 14 750x390: card (205,38), Done (295,228), X (483,48); fits with 38 px spare at the bottom.
- iPad 10th gen 1180x820: card (420,253), Done (510,443), X (698,263).
- Xbox One 1920x1080: card (790,383), Done (880,573), X (1068,393). Card is small for a TV (~18% of width).
- PC 1366x768: card (513,227), Done (603,417), X (791,237).
Nothing cut off or under the top bar or touch controls. Text fits.

Styled vs plain: identical at every preset. Note: reading styled buttons' properties from a script returns defaults (grey, text size 8) since the sheet styles at draw time.

Hover/press (styled, PC): hover darkens, press goes pale; opposite of the sheet (:Hover lighter 5AD45A/EF6A64, :Press darker 2A8A2E). Likely Roblox default AutoButtonColor=true mixing in. Suggested fix: AutoButtonColor=false on styled buttons.
Clip possible: 9.4 s, 1360x768, 283 frames, on PC only (styletrial-styled-pc-hover-press.mp4), not in the PR.
Console: no errors.
