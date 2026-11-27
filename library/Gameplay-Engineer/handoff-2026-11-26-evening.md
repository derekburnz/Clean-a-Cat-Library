# Gameplay-Engineer handoff, 2026-11-26 evening (ET)

Written by the remade Gameplay-Engineer thread for whoever picks this lane up next. The standing rules are in CLAUDE.md and memory.

## Merged tonight (all behind switches, off on live)
| PR | Issue | Switch | Dev and Studio |
|---|---|---|---|
| 898 | 872 | (counterLine needs bigSpa) | live in dev |
| 907 | carry arm | (ArmsStraight) | live in dev |
| 912 | 888, 904 | foamStep | ON 6:33 PM |
| 917 | 908 | (hold to buy) | live in dev |
| 926 | 878 | (bigger tub spots) | live in dev |
| 932 | 923 | (counter cats on their mats) | a restart is needed for running servers; Review-QA asked Derek |
| 933 | 924 | (wash shot framing, under washScreen) | live in dev |
| 935 | 889 | bowDrag | ON 6:54 PM |
| 939 | 892 | (store-setup description) | set on dev; read back matches |
| 942 | 930 | petMenuOnly | ON 7:08 PM |
| 943 | 899 | washSides, showerAim | ON 7:14 PM (Motion-FX's stream 950 rides on showerAim) |
| 946 | 886 | outdoorWalk | ON 7:22 PM |
| 952 | 884 | helperFetch | ON 7:31 PM |
| 955 | 891 | humanBuilder | ON 7:28 PM |
| 958 | 859 | giftCrate | ON 7:31 PM (with giftFlow) |
| 960 | 919 | giftFlow | ON 7:31 PM |
| 963 | 859 | (gift card opens the gift crate window) | live in dev |
| 966 | 883 | (pets renamed, saves mapped on load; claim 965) | live in dev |

## Open or queued (one branch, one PR at a time)
- Issue 887, wideStreet: the switch side is built on local branch wip-887 (SpaLayout.WIDE_*, PlotService, BackdropController). It waits on Model-Agent's CleanACat_Area_StreetWide and BackdropWide (84 stud spacing; the same job as 885's map). The commit says "Part of #887".
- 883 follow ups belong to others: Model-Agent removes the old eight pet models, and Design-Agent adds the eight portraits under the new names.
- Issue 871: carriers floating. 898, 907 and 932 should cover it. It needs Sync-Agent's look on dev and a before and after picture, then it can close (with 850 and 851).
- Issue 856: the wash screen is done in parts (864, 912, 933, 943). Close it once Derek has seen dev.

## Lessons from tonight
- ScrubController's top level has 189 locals of 200. Put new logic in modules (Spa/BowDrag, shared WashSidesRules).
- The local test runner has no CFrame. Pure rules return Vector3.
- Every feature PR adds a LiveFlags line after bowDrag, so a merge of main into the next branch conflicts. Keep both sides. scratchpad/ready.sh did that here.
- prepush.sh merges main. An `--amend` after it amends the merge commit, so commit fixes as new commits.
- A "Closes #N" in a commit message closes the issue on merge, the same as in the PR body. Use "Part of" when the work is not finished.
