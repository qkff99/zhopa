## 2.0.0 — 2026-06-10

### General
- The project has been renamed and published as **Z.H.O.P.A. ALIFE 2.0**.
- The mod now lives in the standalone `qkff99/zhopa` repository with an MIT license, new documentation, and Russian/English README files.
- The architecture has been reworked, trading lower invasiveness for better performance.
- Added a deferred runtime readiness system: heavy subsystems wait until context, indexes, callbacks, and configs are actually ready.
- Added Debug HUD support and dedicated diagnostic scripts for tasks, buckets, trade, loot, mutants, and artifacts.

### Artifacts
- Added a new artifact task contour for both online and offline squads.
- Online squads now move to the target smart, then toward a valid point near the target artifact, and only then start pickup with detector animation.
- Added virtual offline artifacts: offline squads can collect anomaly-zone-generated virtual artifacts without affecting real artifact spawn.
- If a squad enters online while travelling to a virtual artifact, the artifact contour either converts the target into a real pickup path or safely fails the task if the target cannot exist.
- Fixed artifact smart buckets: artifacts no longer collapse into a single resource smart and are assigned to the nearest suitable smart instead.
- Added retargeting for missing artifacts: if the current smart has another free artifact, the task is reassigned instead of failing immediately.
- Added guards against unrelated pickup completion: artifact tasks validate the target artifact, squad, and the actual NPC inventory.

### Economy And Trade
- Added online NPC economy: NPCs sell real items to traders and buy basic supplies.
- Squad leaders now trade for the whole squad, pool member money, and can buy supplies for members.
- Online selling uses real items and changes the trader's inventory; basic supply purchases may be spawned virtually so player-facing stock is not drained.
- Added offline trade on smarts with live traders: server-side inventory is sold and change is represented with money item sections.
- Offline money item sections are converted into NPC balance when squads return online.
- Added the targeted `TRADE` task: its chance scales with sellable inventory value, while opportunistic trade may also run during rest/base camping.
- Added config and MCM control for the NPC sell price multiplier. Default value: `0.2`.
- Added dynamic-news / console trade messages close to vanilla NPC trade output.

### Loot
- Online looting has been moved into the compatible runtime patching contour.
- Added offline looting of real items with results written into squad inventories.
- Added guards against endless loot loops on corpses and containers that still contain non-pickable or quest items.
- Added anti-stall handling for cases where an NPC keeps looking at an item but cannot reach it.

### Tasks And ALife
- Reworked task selection, weighted target selection, and debug reasons for stalker and mutant task contours.
- Fixed `HUNT` pursuit: target coordinates now refresh from the actual target squad position instead of only using the position from task assignment time.
- Fixed faction checks, enemy aliases, blacklists, and mutant task flow after the move to monkey patching.
- Level and smart blacklists now match their intended semantics: globally blocked levels do not admit squads into managed state, and tasks do not select blocked targets.
- `FORCE_EXIT` is now reserved for cases that really need a level-exit task.
- Added or refined `REVENGE`, `TRADE`, `ARTIFACT`, `BASE_CAMPING`, `POPULATE`, and mutant `HUNT/PATROL/REST` behavior.

### Bases, Services, And Story
- Added service filler: occupied bases can refill missing service NPCs for the current owner faction.
- Added dynamic base ownership and post-emission replacement of dead service NPCs.
- Added the psy watchdog: before the Brain Scorcher is disabled, human squads on psy levels can turn into zombified squads.
- Added north migration: after the Brain Scorcher shutdown, part of the population can move to northern bases.
- Story modules are gated by story mode and do not run in freeplay.

### Save Migration
- Added a legacy save cleanup module for saves that previously used older SISKI/ZHOPA versions.
- Added initial migration rules for removing old runtime keys that can prevent the new version from starting correctly.

### Compatibility And QA
- Tested against vanilla Anomaly and the GAMMA profile.
- Fixed GAMMA trade conflicts, wrong trader selection, post-service/trade job stalls, and smart job desynchronization.
- Restored old ZHOPA 1.x changelog history below as the legacy section.

## 1.0.1

### Fixes
- Blocked some broken smarts in the Pripyat Outskirts.
- Cured Azot's hemorrhoids at Yanov (it hurt for him to sit, so he kept standing up and sitting back down trying to find a comfortable position).
- Deleted Alife plus compat layer.

## 1.0

### New
- Added Smart tasks. The first smart task type is `control`: you can now configure control points on smarts and define which squads may occupy them.
  - Control points support white and black lists, a max-squads-per-faction limit, and two working modes: active squad search or claiming only squads that pass nearby.
  - Smart tasks work not only near the player, but also fully offline on other levels.
  - `POPULATE` now treats control points as valid targets and more often sends friendly squads to already occupied important smarts.
  - Points of interest (smart terrains) for `control` are declared in `gamedata\configs\zhopa_smart_tasklist.ltx`. By default it only includes points from vanilla Anomaly levels. If your modpack adds extra levels, you will need to extend this config manually, otherwise those new levels will simply have no points of interest for `control`.
- Added a story zombification module tied to the Brain Scorcher. Until the player disables it, regular human squads on Radar, Red Forest, and Limansk can turn zombified.
  - Be careful when you first reach those levels with ZHOPA enabled: they are very likely to be full of zombies. If you do not want that, just disable the feature in MCM.
- Added the `Story Events` module for squads.
  - The first story event is `North migration`. After the first Brain Scorcher shutdown, part of the human squads moves north to base smarts in Zaton, Jupiter, and Pripyat.
  - `North migration` now has MCM settings, including `North migration: selected squads (%)`.
  - On an old save where the Brain Scorcher has already been disabled, the migration will not trigger. Starting a new game is recommended.

### Fixes
- Fixed task persistence when loading saves and when the player changes levels.
- Added quest item / quest corpse protection in `zhopa_loot`. NPCs will no longer loot bodies the player needs for quests, such as the corpses used by RF Receiver jobs.
  - The option is in `MCM` -> `ZHOPA` -> `Loot` -> `General` -> `Loot: protect quest corpses`. Enabled by default.
- Removed the `xcvb's Guards Spawner` patch from the ModDB ZIP package. With the new Smart task type `control`, this patch is no longer needed because all defender spawn points are already covered by `control` point lists. The mod itself is no longer needed either: `control` fully handles that job, so you can disable it to avoid that mod's console log spam.

## 0.9.5

### New
- Full migration to a decentralized runtime model built around `squad_on_update`. Previously the simulation relied on one main loop that distributed tasks between squads; now each squad individually asks ZHOPA for a task. This gives a major performance boost and noticeably reduces ZHOPA-caused lag, stutter, and FPS drops.
- Added compatibility with Alife Plus. `zhopa_ap_bridge` now hands squads over to Alife Plus when it wants to control them, and takes them back when it no longer needs them.
- Added the `smart_service_slot_doctor` runtime module. It looks for NPCs stuck after trading or mechanic service; when it finds one, it checks how long the NPC has been standing there and detaches the stuck NPC if nothing is happening.
- Refactored MCM settings. Removed all options that became pointless under the new architecture. Performance tuning is now reduced to a single slider, `Off-level squad update skipping`: the higher the value, the less often offline squads are updated, which significantly reduces ZHOPA load on weaker PCs or in heavily overpopulated Zone scenarios. Recommended value for 1500-1700 stalkers or the `Anthology` modpack is `3`. If you play without `AOE` / `MT-TEST`, the recommended value is `3-4`.

### Fixes
- Removed the dead `notify` module. It was originally intended as a future notification system, but in practice vanilla `dynamic_news_manager` is enough.
- Removed hardcoded neighboring levels. Neighbor detection is now fully runtime-driven. This is mostly a technical change that gives out-of-the-box compatibility with new levels and non-vanilla location transitions. Errors may still surface on levels with broken AI maps or game graph data; if you use such level mods, add problematic levels to the blacklists in `zhopa_smart_blacklists.ltx` under `[zhopa_global_level_blacklists]`.
- Removed a lot of dead code.
- Offline mutants no longer go to stalker bases.
- `NIGHT_REST` now triggers instantly, so players will actually notice that stalkers look for a campfire to rest at night.

## 0.9.4.4

### New
- Added new MCM/LTX controls `base_filler_npc_min` and `base_filler_npc_max` to adjust the size of newly spawned `base_filler` camper squads without editing `squad_descr_zhopa.ltx`.

### Fixes
- Fixed a regression in `dynamic_bases` that could drop non-`faction_controlled_*` smart respawn bookkeeping, including helicopter respawn entries, which could later crash on `se_heli:on_unregister`.

## 0.9.4.3

### New
- Reduced `configs\mod_system_zhopa_offline_movement.ltx` to a parent-only DLTX patch on `[online_offline_group]`.
- NPC upgrading their guns more often now.
- Added optional `dynamic_bases` module: runtime rebuild of vanilla base respawns under the current smart owner plus friendly factions.
- Added optional `service_filler` module: one-per-role service NPC respawn on occupied bases only, backed by new `*_sim_squad_service_*` sections for all ZHOPA factions.
- Added new MCM/LTX controls for `dynamic_bases_*` and `service_filler_*`.
- Added `mega_world_mode_enabled` MCM/LTX switch for very large worldspaces. In this mode ZHOPA uses level-local scheduling for `sim`, `memory`, `tasks`, `mutants`, `service_filler`, and `dynamic_bases` to reduce world-wide rebuild spikes and microstutter.
- Fully refactored ZHOPA MCM into a multi-panel layout (`General`, `Tasks`, `Mutants`, `Trade`, `Bases and Services`, `Loot`, `Performance`, `Debug`) backed by a shared schema-driven path map instead of one flat option manuscript.

### Fixes
- Simplified ZHOPA `TRADE` completion: once a squad reaches the trader smart, completion now relies on either a guarded `trade_job` start signal from `axr_trade_manager` or an arrived-timeout fallback, instead of waiting for late `has_items_to_sell/trade_items` cleanup. Follow-up task rotation also blocks immediate repeat `TRADE`, including the `fast_trading` path.
- Refined that completion bridge for `trade -> tech`: if a mechanic follow-up is impossible (`no bonus`, `no technician/service`, or `no free tech job slot`), ZHOPA completes `TRADE` right after the trader phase; if the mechanic phase is viable, completion is deferred until `tech_job` actually starts.
- Closed `trader-without-tech` false handoff: mechanic bonus picks after trade now raise `tech` intent only if the current smart actually has a live technician and a tech job slot.
- Tuned MCM default settings.
- Reduced `zhopa.log` spam.
- `REST` now harder, resting stalkers are resting, not walking away.
- Another try to reduce offline and online mutants dumb behavior.
- Reduced `tasks` hot-path cost without changing gameplay contracts: `loot` no longer runs as a per-squad call inside `operator`, `memory` snapshots are split into cheap/runtime and identity-by-TTL layers, and both `operator.recovery_scan` and online-intent reassert are no longer hit more often than needed.
- Removed duplicate work from the first-task path: `tasks` now uses once-per-tick prep, a per-squad `BuildContext`, and shared runtime caches for level searches, smart buckets, populate anchors, and trade search so one squad-build no longer recalculates the same neighbors, safe checks, and candidate buckets over and over.
- New-game cold start now builds first tasks more cheaply: bootstrap reuses the shared `BuildContext`, cheap roam builders run first, and expensive `TRADE/POPULATE` passes are delayed until at least the next sim cycle instead of all trying to start across the whole map immediately.
- Finished the hot-path cleanup: shared `tasks` prep is now primed before `operator`, and both trade rerolls and patrol retargets now reuse the same `BuildContext` instead of recalculating search/safety state again.
- Added another regular hot-path optimization pass: `tasks` no longer rebuilds the capability index as a synchronous spike, `POPULATE` now uses cached candidate bundles and per-build distance memoization, `memory` sweep is phased by freshness state, and mutant `hunt` refresh now reuses snapshot-first pass caches instead of repeating live object resolution.
- Finished the `mega_world_mode_enabled` refactor into a fuller locality-first path: `board_index` now owns shared board-wide enumeration, `world_scale` tracks hot-promotion epochs, `tasks` use per-level logic shards instead of mega global logic scans, and `sim/service_filler/dynamic_bases/mutants` all consume level-local shards and cadence gates instead of rebuilding their own world-wide queues in steady state.
- Added authoritative runtime topology fallback for levels missing ZHOPA config: `board_index` now scans `level_changer` and `graph_point` server objects, `world_scale` resolves effective neighbors with strict `config -> runtime topology -> observed transitions` precedence, and `tasks/mutants` use that shared neighbor layer instead of raw config-only adjacency.
- Fixed stuck NPC worker schemes after NPC-to-NPC trade or mechanic service jobs: once `trade_job_sell_items` / `tech_job_upgrade_items` finishes and clears the worker intent, `axr_trade_manager` now queues a deferred smart-terrain job re-evaluation on `npc_on_update`, clears the old job `idle` cooldown, and forces `setup_logic` if needed so the worker leaves the service `beh` contour without waiting for a save reload.
- Hardened the same worker-job exit path against trader<->mechanic ping-pong: before the deferred scheme reset, `axr_trade_manager` now always force-clears the sell-side intent (`has_items_to_sell` + queued trade items), clears the tech-side intent only after an actual tech job completion, resets provider job ids, and keeps a short guard that suppresses immediate re-flagging from `npc_on_item_take`.
- Fixed the `trade -> tech` handoff under the self-spawn guard: trader-bought mechanic bonus items now seed `tech` intent directly, and the deferred job-reset path now always reapplies `setup_logic()` after `select_npc_job()` so a new smart job is not left half-applied in runtime.
- Strengthened the service-worker unstuck path further: the deferred reset now also flushes stale `beh`/movement state (`path_index`, desired target, patrol path, desired position/direction) and performs a full smart `unregister_npc/register_npc` reseat after service completion.
- Reworked `service_filler` into a read-only live-job module: it no longer patches provider `suitable` in runtime, no longer writes into `npc_by_job_section`, no longer does runtime reseat, and no longer calls `setup_logic`. Compatibility for named trader/mechanic/medic provider slots is now handled by narrow static logic/DLTX patches.
- Fixed ZHOPA service NPC seating in vanilla provider jobs without runtime reseat: generic `check_npc_trader/mechanic/medic/barman` now accept them by `profile_name()` too, not only by `name()`.
- Prevented ZHOPA sections from `squad_descr_zhopa.ltx` from becoming invulnerable through smart/job logic by adding a double guard in both `stalker_generic.is_need_invulnerability()` and `sim_squad_scripted:check_invulnerability()`.
- Fixed post-spawn drift of service NPCs away from their bases: `service_filler` now keeps only a squad-level pin to the home smart, adds a short pending-grace to suppress duplicate respawns, and always excludes `*_sim_squad_service_*` from warfare without bringing back runtime job reseat.
- Added `axr_task_manager` monkey patch for ZHOPA `medic`/`barman`/`leader` service NPCs: when they occupy a named service slot, AXR now resolves tasks from that slot's donor identity instead of falling back to `sim_default_*`. For leaders the patch also forces named donor tasks instead of `simulation_task_*`.
- Temporarily disabled `guide` and `leader` roles in `service_filler`: guides and leaders are no longer auto-spawned until proper dialog/route support and a safe service contour exist.
- Fixed an AXR trade feedback loop where NPCs could re-flag their own just-bought items as fresh trade/service pickups, causing repeated re-trade churn, live trader stock refreshes and heavy spawn noise on crowded bases.
- Wired `perf_preset_mode` into the adaptive governor too: `Safe` now throttles earlier and harder, `Balanced` sits in the middle, and the old governor defaults are preserved as the `Aggressive` profile.
- Fixed `perf_preset_mode` MCM apply flow: preset selection no longer writes back into MCM controls from inside the apply callback, which could break the Apply button and crash some modpacks/UI stacks.
- Removed the stalker cold-start herd on new game: first assignment now goes through a cold-start bootstrap with smart-index warm-up and budgeted initial task distribution instead of mass synchronized `REST`.
- Fixed `Safe` preset task starvation in `sim/operator`: `operator` no longer uses the unfair `swap-pop` queue, `sim` preserves its unscanned tail across rebuilds, and performance presets no longer run `sim` faster than `operator`. Added runtime stats and soft `sim -> operator` backpressure without introducing governor hard-blocks.
- Removed `loot.update_squad` from the per-squad `operator` hot path: loot maintenance now runs once per ZHOPA tick through `zhopa.loot.on_update()` instead of on every stalker squad.
- Added a shared runtime `logic_index` inside `tasks`: faction-task runners, trade smart occupancy, enemy/safe fallback and faction quotas now all reuse one TTL-cached `iter_logic_squads(...)` pass instead of each doing their own full logic scan.
- Split squad snapshot refresh in `memory` into a cheap runtime pass and a TTL/dirty-driven identity refresh, so `operator/sim` no longer rebuild section/community/allowed on every pass.
- Added throttling only for `enforce_online_task_intent` and an interval gate for `operator.recovery_scan`, without touching immediate `apply_task`, `validate_live_squad`, or the overall gameplay task contract.

## 0.9.3

### New
- Now NPC can buy/sell food, drugs, tools, ammo, consumables and more.

### Fixes
- Fixed `TRADE` target picking to reject hostile smart targets more reliably (including hostile ZHOPA squads anchored to the smart), validate cached/deferred picks against the same safety rule, and fall back to neighbor levels when the current level has no safe trader smart.
- Fixed false-positive trade-smart detection when `npc_faction_override` is enabled: `TRADE` now requires both a regular visitor `trade` slot and a separate live provider NPC (trader/barman) on that smart, instead of treating any NPC forced into `trader` community as a valid trade point.
- Fixed `TRADE` collapsing into the actor's active level: strict live-provider validation is now applied only on the currently loaded level, while off-level target picking falls back to static `trade` slot detection again.
- Added explicit off-level `[trade_smarts]` index for `TRADE`, so trade target selection no longer depends on incomplete `level_smarts_*` lists or on whichever level the actor currently has loaded.
- Replaced deprecated ZHOPA trade monkey patch with local `axr_trade_manager` override, added toggle `trade_axr_buy_all_enabled`, and removed obsolete `trade_buy_all_*` config/MCM/localization keys.
- Removed legacy ZHOPA `trade_force_buy_*` / `trade_extra_buy_*` behavior and settings; ZHOPA now only forces trade-task intent while buy/sell decisions are handled by `axr_trade_manager`.

## 0.9.2 Hotfix2

### New
- Added optional runtime faction override for configured `squad section -> faction` pairs, disabled by default and intended mainly for old saves.
- `POPULATE` updated to account for `base_filler`-squads.
- `EXPLORE` for both stalkers and mutants now targets neighbors only (no same-level explore targets).
- Added optional `base_filler` module: keeps one dedicated base camper squad on each smart from `[level_bases]`, re-pins squad target, and refills on a daily in-game timer.
- Added LTX cfg `squad_descr_zhopa.ltx` with new `*_base_camper_{novice|advanced}` sections for all human factions.
- Debug HUD hints now append `BASE_CAMPER` marker for camper sections (icons are unchanged).
- Added conservative `base_filler` job rebalance for camper NPCs: soft job reseat on missing/conflicted/stalled job links without taking jobs from non-camper squads.
- Added stage-2 `base_filler` route unstuck (`assign nil -> repin`) for long camper squad stalls, with budget and cooldown controls.
- Added new `base_filler` MCM/LTX tuning keys for job rebalance and route unstuck behavior.
- Reworked `FACTION_TASK` into a single persistent `ALLY_RUNNER` loop: `TO_ALLY -> TO_BASE -> repeat`.
- Replaced percentage quota with fixed count per `level+community` via `faction_task_squads_per_level` (default `1`).
- Removed user-facing `FACTION_TASK` role-layer toggles (`faction_task_share_percent`, `intel_sharing_enabled`, `home_region_attachment_enabled`, `incident_chains_enabled`).
- NPCs with `ARTEFACT` task now actually loot artifacts if they exist in the anomaly they're heading to, without animations for now.

### Fixes
- Fixed endless trading loop (again, honestly I don't know why this bug keeps appearing and disappearing from version to version).
- Console mcm spam fix.
- Fixed `base_filler` refill cadence: camper spawns now persist their per-level cooldown through save/load, keep the initial new-game wave only, and skip spawning within 50m of the actor without retrying until the next configured window.

## 0.9.1

### Fixes
- Fixed `smart_terrain.script:1496: attempt to call method 'get_script_target' (a nil value)` crash.
- Fixed endless npc trading loop.

### Performance
- Distributed hardcoded throttling across heavy operations.
- Redesigned enemy check in smarts during task building - it is now lighter, cheaper, and more logical.
- Retuned the `adaptive governor` - the main ZHOPA loop can now process more squads at lower frame time cost.

### New
- New task - `FAST_TRADE`, if NPC found expensive sellable item he will get `TRADE` task immediatly, after selling he will continue last task. (Artefacts only for now, af_).

## 0.9

### Fixes
- Added Ghost Squad Integrity + Memory Vacuum infrastructure: mandatory live squad validation before memory writes, purge of phantom/broken entries from `STATE.squads`, and removal of their impact on tasks/HUD/recovery scans.
- Added memory APIs `validate_live_squad`, `touch_squad_validated`, and `purge_squad_entry`; service mutations (`set_task_*`, `mark_dirty`, `set_surge_lock`) no longer auto-create entries from raw `sid`.
- Stale/orphan sweep now uses `stale_since_tg` age for cleanup/purge, and load-vacuum purges loaded entries with no live heartbeat using a fast 5s window.
- `sim/operator/tasks/mutants` now use centralized integrity guards; hard-invalid `object_nil/empty squad` paths purge entries instead of looping in missed-state forever.
- `TRADE` is no longer forced immediately after `REST_1H`; it now participates as a regular roam candidate in task rotation.

### Performance
- Added Global Budget Broker 2.0 with stage EWMA profiler + auto backoff (`sim/operator/memory/tasks/debug_hud/loot` budgets are now pressure-aware).
- Added dirty-flags pipeline (`memory -> tasks`) plus TTL-gated expensive checks for trade/watchdog/revalidate paths.
- Added capability smart index (`trade_slot/trader/anomaly/base/kamp/safe`) to reduce repeated full-list smart scans.
- Added delta save for memory state (`STATE_VERSION 0.9`): compact entries/tasks and dropped transient scheduler fields.

### New

- QoL: performance presets (`perf_preset_mode`) and one-shot runtime resync (`debug_resync_now`).
- Added `FACTION_TASK` framework with dynamic per-level+faction quota (`faction_task_share_percent`) and 10 roles in one task type.
- Added systemic layers for `FACTION_TASK`: Intel Sharing, Home Region Attachment, and Dynamic Incident Chains.
- Added a separate simplified mutant contour (`zhopa_mutants`) with `REST_1H/EXPLORE/PATROL` and safe fallback rotation.
- Added new mutant task `HUNT`: day-time roam task and night-time priority forced behavior.
- Night transition now preempts mutant tasks immediately into `HUNT`; morning transition auto-releases any active `HUNT` back to normal rotation.
- Mutant target building (`EXPLORE/PATROL/HUNT`) is now blacklist-aware (global/level/faction blacklists).
- Added budgeted + adaptive stalker-presence scanner for `HUNT` targets (`current + neighbors`, on-smart and near-smart within 50m).
- MTI fix for mutants: `HUNT` now picks nearest valid targets with current-level priority; target tasks (`HUNT/EXPLORE/PATROL`) no longer complete/rotate offline; added lightweight online intent/watchdog without forced `switch_online`.
- `HUNT` now uses strict priority buckets: `IN_SMART -> 5m -> 10m -> 30m -> 50m`; inside the first non-empty bucket, target selection is weighted by stalker-squad presence count per smart.
- Mutants now support faction blacklists via `monster` (and `mutant/mutants` aliases) in `[zhopa_faction_level_blacklists]` and `[zhopa_faction_smart_blacklists]`.
- Added section-based blacklist rules: `[zhopa_section_level_blacklists]` and `[zhopa_section_smart_blacklists]` for precise per-`section` restrictions (for both stalkers and mutants).
- Added mutant section allowlist in `zhopa_settings.ltx`: `[spawner_allowed_sections_mutants]`.
- Added `predator_day/predator_night` phase gate: mutant squads inactive for current time-of-day are force-held in `REST_1H` (day predators at night, night predators by day) using live squad/commander identity.
- Expanded mutant phase resolver aliases: supports `monster_predatory_*`, `monster_zombied_*`, `predatory_*`, `zombied_*` variants and prioritizes `squad.player_id` detection (fixes cases like `simulation_fracture`).
- Debug HUD now resolves spot colors by type/faction (mutants: black `circle_zombied`, stalkers: `warfare_*_spot`) using strict ownership.

## 0.8

### Fixes
- Fixed long-standing online squad stalls where some squads would stand still or wander with an active target, especially on cross-level travel.
- Fixed watchdog escalation loop: `ONLINE_STALL_SOFT` no longer resets stall progress, so escalation now reliably reaches `MEDIUM/HARD` stages.
- Added route-deadlock diagnostics (`ONLINE_ROUTE_DEADLOCK`) for cases with no distance signal and no game-vertex movement.
- Strengthened hard recovery for stalled online squads: full steering reset, bridge retarget on current level first, then fallback retarget/rebuild.
- Added force-rebuild fallback path in task update flow after hard watchdog fallback to prevent infinite "has target but does nothing" states.
- Fixed smart resolve in enemy check (`board.smarts[e.smart_id]` + `node.smrt`) to remove ineffective expensive scans.
- Reduced duplicate expensive safety checks during trade target selection by memoizing roam-allow checks per call.
- Added Squad Freshness Authority (SFA): stale/ghost squad entries no longer participate in task decision scans; memory now uses a freshness state machine (`ACTIVE/GRACE/STALE/ORPHAN`) with staged stale clear/purge and load-state migration.
- Isolated Debug HUD map spots from engine quest task spots: HUD now uses strict ownership and no longer removes/rewrites non-owned map spots, preventing task/map-location link corruption on save/load or simulator restart.


### Performance
- Added hard bounds for loot event backlog and incremental cleanup to avoid long post-surge cleanup spikes.
- Added budgeted + round-robin scanning in loot evaluator patches to remove full-table hot-path scans.
- Added optional surge-aware loot event collection gate with post-surge grace window.
- Added cache sizing/pruning for heavy runtime caches in task registry.
- Added cached surge checks and rate-limited PERF warnings (`PERF_LOOT_BACKLOG`, `PERF_LOOT_SCAN_BUDGET_HIT`, `PERF_TASK_ENEMY_SCAN_HEAVY`, `PERF_SURGE_CHECK_FALLBACK`).
- Added hardcoded hot-path throttling in `operator/tasks/loot` (watchdog and target revalidation intervals, operator frame time guard, throttled loot override/config snapshot) to reduce regular frame spikes without adding new user settings.
- Added adaptive governor (`adaptive_throttle_enabled`) with one switch: it auto-throttles heavy `operator/tasks` lanes under pressure using defer-only policy and anti-starvation force-runs.

### New
- Smart blacklists for problematical smarts `zhopa_smart_blacklists.ltx`

## 0.7.4

### Fixes
- NPCs no longer leave cover during surge (emission) or psi-storm.
- NPCs no longer go to enemy bases: all tasks check for enemies within 50m.

## 0.7.3

### Fixes
- Adjusted the list of anomaly-zone NPC smarts available for exploration; they will now find artifacts more often.
- Removed dead code, unused settings, and obsolete localization keys
- Fixed Patrol and Camping tasks; they now participate in the general NPC task-issuing cycle.
- Simplified enemy-presence checks in target smarts for tasks; NPCs will visit potentially dangerous places more often, reducing fallback counts.

### New
- Added Bivouacs: at night stalkers now prefer to stay in safe spots/bases and avoid wandering the level until morning. The feature is optional and can be disabled.
- Added a static list of “bases” in ltx configs.

## 0.7.2

### Fixes
- Trading migrated to vanilla rails; fixed trading crashes and bugs
- Improved task rotation system

## 0.7.1

### Fixes
- Closed all potential nil-related crashes (~100 unsafe spots)
- Protected trading when several NPCs try to trade with the same trader

## 0.7

### Removed
- Spawner: no longer needed for better compatibility; use vanilla spawn settings or alternatives like ZCP.
- Monkey patches and all functionality that required them (for compatibility).
- Complex path math (for performance); migrated to vanilla methods.
- Excessive NPC tasks (for performance and less macro-level chaos).
- Dead code and other junk.
- Unnecessary functions and settings.

### Key changes
- Refactor and adaptation of everything to the new architecture.
- Significantly improved performance, stability, and compatibility.
- Simplified settings and made them more user-friendly.
- Busy hands protection and reduced load in `actor_on_update`.
- Moved a large part of the functionality to vanilla callbacks.

## 0.6.2

### Fixes
- Fixed a rare `pure virtual function call` crash in Debug HUD by removing `:name()`/`alife_object()` calls on potentially stale server objects.
- Fixed post-trade “sticking to a point”: force-clears `desired_position/desired_direction` and handles `FAILED/NO_SINK` with leader release/cleanup.
- Fixed selling rules: NPCs no longer sell active/equipped weapons/armor and will not sell their last gun (ensures at least one `wpn_` remains).
- Fixed a regression that could break offline updates and memory dumps: `safe_run` now uses Lua 5.1 `unpack` and preserves `nil` args; dump hotkey no longer relies on raw `ui_mcm.get`.

### Performance
- Buffered file logging to reduce `io.open/io.close` overhead via batched writes.
- Added a TTL cache for MCM reads (`get_config`) to reduce frequent polling cost.
- Optimized squad level resolution during `sync_to_memory` by caching the level name per `m_game_vertex_id`.
- Optimized Debug HUD: skip non-current-level squads, avoid map hint updates when unchanged, add cooldown on `try_register_brain`.
- Tuned global artifact scan: fewer empty steps and larger processing blocks.

### Stability / Diagnostics
- Added `xpcall + debug.traceback` for core ZHOPA updates (brain/debug/scanner) and `brain:update()`: errors are logged with full traceback and should not crash the game due to ZHOPA.
- Added safety guards for memory `perf` caches (auto-reset on abnormal growth).

## 0.6.1

### Fixes
- MOVE now reliably binds squads to a smart via `assign_squad_to_smart` even when SIMBOARD lacks a stable `name -> id` lookup (added a unified resolver via SIMBOARD → intel/memory).
- Reduced MOVE “stalls”: added progress tracking by distance-to-target, periodic smart rebind when stuck, and a fallback degradation to `MOVE_TO_POS` after prolonged stagnation.
- Improved `MOVE_TO_POS` robustness: added staged degradation (retry / smart-based fallback) instead of silent force-complete; for offline squads `MOVE_TO_POS` is converted into smart-based MOVE to the nearest smart.
- Retargeting policy updated: no longer exclusive to `af_hunter` — urgency/priority are considered and a cooldown prevents target “thrashing” (separate tuning for online/offline).
- Trading stability fix: removed inventory item removal via release when no trader NPC is found (source of `SV: can't find child ... of parent ...` warnings); selling now uses safe transfers to a live “sink” NPC at the smart, or is deferred if none exists.

### Added
- Implemented a full NPC-to-NPC trading system.
- Cross-level routing: if a target smart is on another level, the squad first moves to the nearest level changer on the current level (`MOVE_TO_POS`), then automatically queues the final smart-based task.
- Movement diagnostics: added stuck/timer metrics for MOVE and `MOVE_TO_POS` degradation stages into memory and exposed them in reporter/debug output, including “retarget age”.
