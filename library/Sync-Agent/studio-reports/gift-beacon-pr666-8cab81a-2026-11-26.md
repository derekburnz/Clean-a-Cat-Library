# Gift beacon (PR 666) on main 8cab81a, 2026-11-26
Method: PR 666's only client file (Effects/GiftStand.luau) put into the open 2a34a8e place, not saved. PR 665's VIP server changes not in that place. Seeded at 6:45 so the stand lit at 7:00. iPhone 13 frame. Pictures 06 to 08 on draft PR 667.
1. Reads clearly: FAIL at the spawn, PASS elsewhere. At the spawn the camera is inside the wall panel behind it (same bug as #670, picture 03/06), screen light blue, nothing shows. From 4.5 studs in from the spawn: gold sparkle 33 px at 27 studs, nothing in front (07). From the tub, camera turned to the stand: 36 px at 35 studs, nothing in front; stand hidden behind the window shelf but sparkle shows above it (08). Own stand only; breathes 31 to 37 px.
2. Gone once claimed: PASS (simulated: GiftClaimed set true on the server). Sparkle went at once, lamp and light stayed; back to false brought it back. Real claim needs a favourite.
3. Neighbour's stand: NOT RUN (one player). Simulated: Lit true on Plot2's stand on my client, lamp lit, no sparkle.
4. Console: nothing new.
Fixing the camera (#670) would fix check 1 at the spawn.
