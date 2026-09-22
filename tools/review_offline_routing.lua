-- Run from project root. Read-only probes of the real modules, with small engine fixtures.
-- Optional arg[1]: installed gamedata/scripts directory for comparison.
local scripts = (arg[1] or "gamedata/scripts") .. "/"
local objects, smarts, squads, flags, clock = {}, {}, {}, {}, 1000
function time_global() return clock end
function printf() end
function alife_object(id) return objects[tonumber(id)] end
function game_graph() return {valid_vertex_id = function() return true end,
    vertex = function(_, id) return {level_id = function() return id end} end} end
function alife() return {level_name = function(_, id) return "L" .. id end} end
level = {name = function() return "L1" end, get_time_hours = function() return 12 end}
db = {actor = {}, storage = {}}
is_squad_monster = {}
game_relations = {is_factions_enemies = function() return false end,
    is_factions_friends = function(a, b) return a == b end}
zhopa2_cfg = {get_bool = function(key, default)
    if flags[key] ~= nil then return flags[key] end
    if key == "base_camping_enabled" or key == "geographic_balance_enabled"
        or key == "faction_presence_balance_enabled" or key == "faction_lore_preferences_enabled" then return false end
    return default
end, get_num = function(_, default) return default end,
is_level_blacklisted_for_squad = function() return false end,
is_smart_blacklisted_for_squad = function() return false end}
zhopa2_topology = {get_revision = function() return 1 end,
    get_level_neighbors = function(lvl)
        return ({L1 = {"L2"}, L2 = {"L1", "L3"}, L3 = {"L2", "L4"}, L4 = {"L3"}})[lvl] or {}
    end}
zhopa2_service_fillers = {is_service_base = function(s) return s.service == true end}
zhopa2_index = {base_ownership = function(s) return s.ownership end,
    squads_on_levels = function(levels)
        local result = {}
        for _, lvl in ipairs(levels) do
            for _, q in pairs(squads) do if lvl == "L" .. q.m_game_vertex_id then result[#result + 1] = q end end
        end
        return result
    end,
    smarts_on_levels = function(levels)
        local result = {}
        for _, lvl in ipairs(levels) do
            for _, s in pairs(smarts) do if lvl == "L" .. s.m_game_vertex_id then result[#result + 1] = s end end
        end
        return result
    end}
simulation_objects = {available_by_id = {}, base_smarts = {}}
SIMBOARD = {smarts = {}, squads = {}}
local function pos(x)
    return {x = x, y = 0, z = 0, distance_to_sqr = function(a, b) return (a.x-b.x)^2 end}
end
local function smart(id, lvl, jobs)
    local s = {id = id, m_game_vertex_id = lvl, position = pos(0), service = true, max_population = 1,
        props = {base = 1}, npc_info = {}, npc_by_job_section = {},
        ownership = {state = "owned", owner = "stalker", updated = clock}}
    function s:name() return "base_" .. self.id end
    function s:target_precondition() return true end
    if jobs then
        s.stalker_jobs = {}
        for i = 1, jobs do s.stalker_jobs[i] = {section = "walker_" .. i} end
    end
    objects[id], smarts[id], SIMBOARD.smarts[id] = s, s, {smrt = s, squads = {}, population = 0}
    return s
end
local function squad(id, lvl, size)
    local q = {id = id, m_game_vertex_id = lvl, position = pos(300), player_id = "stalker"}
    function q:npc_count() return size end
    function q:section_name() return "stalker_sim_squad_veteran" end
    function q:squad_members() return function() return nil end end
    objects[id], squads[id] = q, q
    return q
end
local function upvalue(fn, name)
    for i = 1, 100 do
        local key, value = debug.getupvalue(fn, i)
        if not key then break end
        if key == name then return value end
    end
    error("missing upvalue " .. name)
end
local function tick()
    clock = clock + 1
    for _, s in pairs(smarts) do s.ownership.updated = clock end
end
local p = assert(loadfile(scripts .. "zhopa2_perception.script"))()
local visitor = squad(100, 1, 2)
local base = smart(10, 1, 8)
local score = upvalue(p.base_camping_populate_target_valid, "base_camping_populate_score")
local online_rank, online_free = score(visitor, base)
base.stalker_jobs = nil; tick()
local offline_rank, offline_free = score(visitor, base)
print(string.format("BASE_CAMPING same empty base: loaded rank=%s free=%s; unloaded rank=%s free=%s",
    tostring(online_rank), tostring(online_free), tostring(offline_rank), tostring(offline_free)))
if p.smart_settlement_capacity then
    assert(online_rank ~= nil and offline_rank == online_rank and online_free == offline_free, "online/offline camping mismatch")
else
    assert(online_rank ~= nil and offline_rank == nil, "baseline changed: re-review offline camping")
end

if p.service_base_roam_weight then
    local resident = squad(110, 1, 2)
    resident.smart_id = base.id
    base.npc_info[111], base.npc_info[112] = {}, {}
    function resident:squad_members()
        local id = 110
        return function() id = id + 1; if id <= 112 then return {id = id} end end
    end
    SIMBOARD.smarts[base.id].squads[resident.id] = true
    base.stalker_jobs = {}
    for i = 1, 8 do base.stalker_jobs[i] = {section = "walker_" .. i} end
    base.npc_by_job_section = {walker_1 = 111, walker_2 = 112}
    tick(); local online_weight = p.service_base_roam_weight(visitor, base)
    base.stalker_jobs, base.npc_by_job_section = nil, {}
    tick(); local offline_weight = p.service_base_roam_weight(visitor, base)
    print(string.format("SERVICE same base (8 jobs, max_population=1, 1 resident squad): loaded=%s unloaded=%s",
        tostring(online_weight), tostring(offline_weight)))
    if p.smart_settlement_capacity then assert(online_weight == offline_weight, "capacity depends on job loading")
    else assert(online_weight == 2.5 and offline_weight == 0, "baseline changed: re-review capacity units") end
    squads[resident.id], SIMBOARD.smarts[base.id].squads[resident.id] = nil, nil
end

-- First non-empty geographic tier wins before scoring.
smarts, SIMBOARD.smarts = {}, {}
local local_base, neighbor, remote = smart(20, 1, 8), smart(21, 2, 8), smart(22, 3, 8)
flags.geographic_balance_enabled = true
tick()
local tasks = assert(loadfile(scripts .. "zhopa2_tasks.script"))()
local function builder(name)
    for _, entry in ipairs(tasks.task_registry.stalker) do if entry.name == name then return entry.build end end
    error("missing builder " .. name)
end
for _, name in ipairs({"EXPLORE", "POPULATE"}) do
    local result = assert(builder(name)(visitor))
    local choices = result.task and {result} or result
    local targets = {}
    for _, choice in ipairs(choices) do targets[#targets + 1] = tostring(choice.target) end
    print(name .. " offered targets: " .. table.concat(targets, ","))
    if p.collect_roam_smarts then
        local found = {}
        for _, choice in ipairs(choices) do found[choice.target] = true end
        assert(found[neighbor.id] and found[remote.id], "near and far must compete")
        if name == "POPULATE" then assert(found[local_base.id]) end
    else
        assert(#choices == 1 and choices[1].target == (name == "EXPLORE" and neighbor.id or local_base.id))
    end
end

-- Existing presence balancing rewards concentration, rather than distributing allies.
flags.geographic_balance_enabled, flags.faction_presence_balance_enabled = false, true
local scoring = assert(loadfile(scripts .. "zhopa2_task_scoring.script"))()
local bucket = {}
for i = 1, 5 do local q = squad(300 + i, 1, 2); bucket[q.id] = q end
scoring.on_buckets_rebuilt({zhopa2_squads_by_level = {L1 = bucket}})
local a = scoring.make_candidate(visitor, {task = "TRADE", target = local_base.id, target_level = "L1"}, 10)
local b = scoring.make_candidate(visitor, {task = "TRADE", target = neighbor.id, target_level = "L2"}, 10)
scoring.select_candidate(visitor, {a, b})
print(string.format("NON-ROAM SAFETY (TRADE) unchanged: allied populated level=%s; empty level=%s", a.final_weight, b.final_weight))
assert(a.final_weight == 15 and b.final_weight == 10)
print("Review probes complete; observations are code-level, not long-session telemetry.")
