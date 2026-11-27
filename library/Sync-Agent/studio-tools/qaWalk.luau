-- qaWalk v3: move the Studio test character to a named plot spot without getting stuck (QA only, never shipped).
-- Paste into execute_luau on the Client datamodel after the opening is over (a long call during the opening leaves
-- the camera Scriptable). Defines _G.qaSpots, _G.qaPoint, _G.qaWalk and _G.qaWalkNamed for later calls.
--   _G.qaWalkNamed(name, opts) / _G.qaWalk(point, opts) -> result
--     opts    { timeout = math.huge, teleportFallback = true }
-- v3 (2026-11-27, issue 994): no global timeout. Each leg re-sends MoveTo after every 0.5 s standing still (a MoveTo
-- can be dropped as the feet land after stepping off the 0.53 stud plot slab edge) and counts as stuck only after
-- 2 s (4 still checks). result.nudges counts the re-sends.
--     result  { reached, method = "path" | "path+retry" | "teleport" | "none", seconds, stuckEvents, stuckAt?, noPath?,
--               dist, at, goal }
local Players = game:GetService("Players")
local PathfindingService = game:GetService("PathfindingService")
local SpaLayout = require(game:GetService("ReplicatedStorage"):WaitForChild("Shared"):WaitForChild("SpaLayout"))

-- Stand points: the SpaLayout spot an area belongs to plus a WORLD-axis offset (slot 1 is not turned) to clear floor
-- on the room side of the object. Slot 1 world positions (feet) are in the rules file.
_G.qaSpots = {
	Spawn = { spot = "SpotSpawn", offset = Vector3.new(-5, 0, 11.5) }, -- the live spawn (-5, 0.5, -7)
	Tub = { spot = "SpotTub", offset = Vector3.new(0, 0, -4.5) },
	DoorLine = { spot = "SpotQueue1", offset = Vector3.new(3, 0, 0) },
	Window = { spot = "SpotWindow3", offset = Vector3.new(0, -2.5, 3.5) },
	Board = { spot = "SpotBoard", offset = Vector3.new(3, 0, 0) },
	GardenGate = { spot = "SpotGardenDoor", offset = Vector3.new(0, 0, -3) },
	GardenInside = { spot = "SpotGardenDoor", offset = Vector3.new(0, 0, 4) },
	VipDoor = { spot = "SpotVipDoor", offset = Vector3.new(0, 0, -3) },
	VipInside = { spot = "SpotVipDoor", offset = Vector3.new(0, 0, 4) },
	StrayBox = { spot = "SpotStray", offset = Vector3.new(-2.5, 0, 0) },
	PadJo = { spot = "SpotWorkerJo", offset = Vector3.new(0, 0, -3) },
	PadSam = { spot = "SpotWorkerSam", offset = Vector3.new(0, 0, -3) },
	PadLou = { spot = "SpotWorkerLou", offset = Vector3.new(0, 0, -3) },
}

_G.qaPoint = function(name: string, slot: number?): Vector3
	local def = _G.qaSpots[name]
	assert(def, "unknown spot " .. tostring(name))
	return SpaLayout.slotSpot(def.spot, slot or 1).Position + def.offset
end

local function flat(v: Vector3): Vector3
	return Vector3.new(v.X, 0, v.Z)
end

-- Room for a character with its feet at `feet`: floor under it and nothing solid in a 2.6 x 5 x 2.6 body box.
local function clearAt(feet: Vector3, char: Model): boolean
	local params = RaycastParams.new()
	params.FilterType = Enum.RaycastFilterType.Exclude
	params.FilterDescendantsInstances = { char }
	local down = workspace:Raycast(feet + Vector3.new(0, 2, 0), Vector3.new(0, -4, 0), params)
	if not down then
		return false
	end
	local overlap = OverlapParams.new()
	overlap.FilterType = Enum.RaycastFilterType.Exclude
	overlap.FilterDescendantsInstances = { char }
	overlap.RespectCanCollide = true
	local box = CFrame.new(down.Position + Vector3.new(0, 2.9, 0))
	return #workspace:GetPartBoundsInBox(box, Vector3.new(2.6, 5, 2.6), overlap) == 0
end

-- The goal itself if clear, else the nearest clear point on rings around it (up to 6 studs).
local function clearNear(base: Vector3, char: Model): (Vector3?, number)
	if clearAt(base, char) then
		return base, 0
	end
	for _, r in { 1, 1.75, 2.5, 3.5, 4.5, 6 } do
		for i = 0, 15 do
			local a = i / 16 * 2 * math.pi
			local p = base + Vector3.new(math.cos(a) * r, 0, math.sin(a) * r)
			if clearAt(p, char) then
				return p, r
			end
		end
	end
	return nil, -1
end

_G.qaWalk = function(goalIn: Vector3, opts: any?)
	opts = opts or {}
	local char = Players.LocalPlayer.Character or Players.LocalPlayer.CharacterAdded:Wait()
	local hum = char:WaitForChild("Humanoid") :: Humanoid
	local root = char:WaitForChild("HumanoidRootPart") :: BasePart
	local timeout = opts.timeout or math.huge -- no global timeout; per-leg stuck check only
	local goal, moved = clearNear(Vector3.new(goalIn.X, math.max(goalIn.Y, 0.5), goalIn.Z), char)
	local t0 = os.clock()
	local result: any = { target = "", reached = false, method = "none", seconds = 0, stuckEvents = 0 }
	if moved > 0 then
		result.target = string.format("(moved %.1f to clear floor)", moved)
	end
	if not goal then
		result.target = "(no clear floor within 6 studs)"
		return result
	end
	-- the walk must never hop walls, slabs or furniture: auto-jump off while walking, back after
	local autoJump = hum.AutoJumpEnabled
	hum.AutoJumpEnabled = false
	if hum.Sit then
		hum.Sit = false
	end
	local function near(): boolean
		return flat(root.Position - goal).Magnitude < 1.6
	end
	local function grounded()
		local t = os.clock()
		while hum.FloorMaterial == Enum.Material.Air and os.clock() - t < 2 do
			task.wait(0.05) -- a fresh teleport or respawn is still falling; a path from mid-air fails
		end
	end
	grounded()
	local dir = flat(goal - root.Position)
	if dir.Magnitude > 0.1 then
		root.CFrame = CFrame.lookAt(root.Position, root.Position + dir) -- face the goal before moving
	end
	local function follow(): boolean
		grounded()
		local path = PathfindingService:CreatePath({
			AgentRadius = 1.6, -- R15 and R6 are about 2 studs wide; the margin keeps them off edges and posts
			AgentHeight = 5.5,
			AgentCanJump = false,
			AgentCanClimb = false,
			WaypointSpacing = 4,
		})
		local ok = pcall(function()
			path:ComputeAsync(root.Position, goal)
		end)
		if not ok or path.Status ~= Enum.PathStatus.Success then
			result.noPath = (result.noPath or 0) + 1
			return false
		end
		for _, wp in path:GetWaypoints() do
						hum:MoveTo(wp.Position)
			local last, still = root.Position, 0
			while flat(root.Position - wp.Position).Magnitude > 1.2 do
				task.wait(0.5) -- stuck check every 0.5 s
				if flat(root.Position - last).Magnitude < 0.4 then
					still += 1
					hum:MoveTo(wp.Position) -- v3: a MoveTo dropped as the feet land off a ledge is sent again
					result.nudges = (result.nudges or 0) + 1
				else
					still = 0
				end
				last = root.Position
				if still >= 4 or os.clock() - t0 > timeout then
					result.stuckEvents += 1
					result.stuckAt = root.Position
					hum:MoveTo(root.Position) -- cancel; never leave a MoveTo running into a wall
					return near() -- held up right beside the goal still counts
				end
			end
		end
		return near()
	end
	if follow() then
		result.method = "path"
	elseif os.clock() - t0 < timeout and follow() then
		result.method = "path+retry"
	elseif opts.teleportFallback ~= false then
		local look = flat(goal - root.Position)
		local cf = CFrame.new(goal + Vector3.new(0, 3, 0))
		if look.Magnitude > 0.1 then
			cf = CFrame.lookAt(cf.Position, cf.Position + look)
		end
		char:PivotTo(cf)
		root.AssemblyLinearVelocity = Vector3.zero
		task.wait(0.3)
		result.method = "teleport"
	end
	hum:MoveTo(root.Position)
	hum.AutoJumpEnabled = autoJump
	result.reached = near()
	result.seconds = os.clock() - t0
	result.dist = flat(root.Position - goal).Magnitude
	result.at = root.Position
	result.goal = goal
	return result
end

_G.qaWalkNamed = function(name: string, opts: any?)
	local r = _G.qaWalk(_G.qaPoint(name), opts)
	r.target = name .. " " .. r.target
	return r
end

return "qaWalk ready"
