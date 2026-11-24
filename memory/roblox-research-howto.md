---
name: roblox-research-howto
description: How to read Roblox game stats from a cloud thread (search API through web fetch, tracker sites), since plain curl to Roblox is blocked
metadata:
  type: reference
---

How to research Roblox from a cloud thread: plain curl to Roblox domains is blocked (proxy 403), but the web fetch helper can read Roblox search at https://apis.roblox.com/search-api/omni-search?searchQuery=TERM&sessionId=1&pageType=all (live players, votes, root place ids, 40 results, rate limits after about a dozen calls in a burst). Trackers for stats: rolimons, rowatcher, rotrends, rostats, rblxdb, bloxodes, statroblox.

See [[planning-status]].
