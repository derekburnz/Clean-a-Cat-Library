# New group key on Derek's other account (drop-in for ROBLOX_GROUP_KEY)

Gameplay-Engineer, 2026-11-26 10 PM ET. I read this list from our workflows; Roblox's on-screen names may differ slightly.

1. **Group role.** On the other account, its role in Creampuff Games needs permission to:
   - create group API keys (the Open Cloud or API keys permission in Configure Group > Roles);
   - create and edit group experiences;
   - create and manage group assets.

   Admin usually has all three.
2. **Make the key under the group:** Creator Hub > Open Cloud > API Keys > Create API Key, with **Creampuff Games** picked as the creator, not the account itself.
3. **Experience APIs.** For each one below, add **both** experiences: Clean a Cat (10778773655) and Clean-a-Cat-Dev (10778775478).

   | API | Tick | What it is for |
   |---|---|---|
   | universe-places | Write | publish |
   | universe | Write | restart servers, server size, the page description |
   | universe-datastores | every object operation: list, read, create, update, delete | the switches |
   | universe-messaging-service | Publish | the restart countdown |
   | Game passes and Developer products | Read and Write | store setup |
   | Secrets store | Read and Write | saving the notification key into the game |
   | User notifications | Write | "your build is ready" |

4. **Group-wide APIs:** assets (Read and Write) for uploads, and asset-permissions (Write).
5. **Accepted IP addresses:** `0.0.0.0/0`, because GitHub has no fixed address. Save, then copy the key.
6. **GitHub** > Clean-a-Cat > Settings > Secrets and variables > Actions:
   - Replace **ROBLOX_GROUP_KEY** with the new key. This covers dev publishes, switches, uploads and store setup.
   - For live as well, add the same key as a new secret, **ROBLOX_PUBLISH_KEY**. It already takes priority over OWNER_KEY for live publishes, switches and restarts, so the suspended owner key is never used.
   - OWNER_KEY can stay as it is.

## What stays unavailable or needs a redo
- **Notification strings** could only be made with OWNER_KEY. The build_done string already exists and its id is in the game, so nothing is lost unless a new string is wanted.
- **The game's notification secret.** CleanACat_NotifyKey still holds the old, blocked key. Once the new key is in, Gameplay-Engineer re-runs notify-key install on dev (and on live only on Derek's word).
- **The flagged like icon.** Don't re-upload it (asset 135826908608436). It needs a different picture.

## After Derek says the key is saved
Gameplay-Engineer runs the read-only introspect once. If the key is not moderated, the publish hold comes off with a one-file PR (delete `.github/publish-hold`).
