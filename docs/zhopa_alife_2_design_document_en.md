# Z.H.O.P.A. ALIFE 2.0: Architecture Design Document

[Russian version](zhopa_alife_2_design_document.md)

Full name: **Z.H.O.P.A. ALIFE 2.0 — Zone Hostile Operations & Population AI**.

This document follows the old ZHOPA design document format: it is an engineering map, not a player-facing README. It describes the current ZHOPA ALIFE 2.0 architecture after the migration from full-file overrides to chain-friendly runtime patches.

## 1. Purpose

ZHOPA ALIFE 2.0 does not build a separate ALife layer on top of Anomaly. It is a motive, task, consequence and economy layer integrated into vanilla SIMBOARD, `smart_terrain`, `sim_squad_scripted`, `xr_gather_items` and related callback points.

Vanilla still owns:

- squad movement between smart terrains;
- online/offline transitions;
- smart job assignment;
- pathfinding and concrete NPC animation life inside a smart;
- ordinary combat behavior.

ZHOPA ALIFE 2.0 owns:

- why a squad chooses the next target;
- which tasks are available for stalkers and mutants;
- how a squad remembers loot, trade debt, artifact cargo and interrupted tasks;
- how offline and online branches produce comparable consequences;
- how dynamic base ownership affects targets;
- how squads trade, loot, hunt, collect artifacts and react to story events.

Core loop:

```text
runtime ready -> squad update -> task FSM -> vanilla scripted target -> arrival/result -> consequence -> memory -> next task
```

The main rule is to keep vanilla rails intact. Invalid state must leave through a controlled fallback, write readable `last_reason` / `last_result`, and return the squad to safe behavior.

## 2. Bootstrap and Runtime Flow

### 2.1 Load order

Entry points:

- `zhopa2_bootstrap.script`
- `zhopa2_runtime_patches.script`

`zhopa2_bootstrap` invokes the runtime patch orchestrator. The central integration surface lives in `zhopa2_runtime_patches`, while each runtime module remains self-contained and registers its own callbacks through `on_game_start()`.

Runtime modules:

- `zhopa2_index`
- `zhopa2_topology`
- `zhopa2_loot`
- `zhopa2_economy`
- `zhopa2_revenge`
- `zhopa2_service_fillers`
- `zhopa2_artifacts`
- `zhopa2_story_psy_watchdog`
- `zhopa2_story_north_migration`

Runtime patches:

- `se_level_changer`
- `sim_board`
- `smart_terrain`
- `sim_squad_scripted`
- `bind_anomaly_zone`
- `bind_monster`
- `xr_reach_task`
- `xr_gather_items`
- `xr_corpse_detection`
- `sim_offline_combat`

### 2.2 Runtime readiness

`on_game_start` is too early for some world context. ZHOPA therefore uses a readiness gate:

- patches and runtime modules register early;
- heavy systems wait for required modules, callbacks, actor first update and warmup;
- readiness prints debug progress as `1/x`, `2/x`, ...;
- readiness errors identify the failed item;
- hot paths call `zhopa2_runtime_ready(reason)` when full context is required.

When a new required runtime module or patch is added, it must be added to the readiness list in `zhopa2_runtime_patches.script`. Otherwise a system can start before indexes, MCM defaults, callbacks or save/load recovery are ready.

### 2.3 Callback surface

Main events:

- `server_entity_on_register`
- `server_entity_on_unregister`
- `actor_on_first_update`
- `actor_on_update`
- `on_game_load`
- `save_state`
- `load_state`
- `on_option_change`
- `squad_on_after_level_change`
- smart update / enter / leave / reach target through patched vanilla anchors
- item gather / corpse detection / item take through `xr_gather_items` and `xr_corpse_detection`

Callback registration must be idempotent. Re-registration must not duplicate handlers, and missing optional subsystems must not crash the game.

## 3. Data Model

### 3.1 Squad state

The main state is stored on the squad object and goes through the patched `sim_squad_scripted` save/load path.

Key fields:

- `zhopa2_task`
- `zhopa2_target`
- `zhopa2_target_kind`
- `zhopa2_until`
- `zhopa2_last_reason`
- `zhopa2_last_result`
- `zhopa2_patrol_route`
- `zhopa2_patrol_idx`
- `zhopa2_prev_*` for interrupts and night-rest resume
- `zhopa2_loot_count`
- `zhopa2_loot_value`
- `zhopa2_artifact_*`
- `zhopa2_trade_*`
- `zhopa2_revenge_*`

Save state must never contain engine objects, userdata, online object handles or metatable-backed tables. Only numbers, strings, booleans and plain tables are safe.

### 3.2 Runtime-only index

`zhopa2_index` owns small event-driven buckets. It is not a separate world simulation and not a global scanner.

Core buckets:

- squads by level;
- squads by smart;
- smarts by level;
- base smarts and ownership;
- trader smarts;
- artifact pool;
- smart artifact buckets;
- virtual artifacts;
- artifact reservations;
- artifact cargo;
- base camping targets.

Indexes are updated from vanilla events: squad first update, level change, smart enter/leave/update, artifact spawn/take/destroy and unregister cleanup.

### 3.3 Module-owned runtime

Each module owns its own temporary state:

- `zhopa2_economy` — trade sessions, cooldowns, online trader routing, sell/buy rules;
- `zhopa2_loot` — targeted pickups, anti-loop corpse marks, offline loot effects;
- `zhopa2_artifacts` — artifact pickup stages, virtual artifact collection, detector animation flow;
- `zhopa2_story_north_migration` — story event selection/status;
- `zhopa2_story_psy_watchdog` — conversion queues and pending reconciliation.

Module runtime state must be cleaned on unregister, death and load. Stale ids easily break the task FSM.

## 4. Foundation Modules

### 4.1 `zhopa2_cfg`

Reads LTX defaults and MCM values. MCM is optional: without `ui_mcm`, the game must run on defaults from `zhopa2_settings.ltx`.

Responsibilities:

- feature toggles;
- weights;
- blacklists;
- threshold values;
- price multiplier;
- safe getters.

`ui_mcm.get(...)` must not be called inside `on_mcm_load()`.

### 4.2 `zhopa2_mcm` / `zhopa2_mcm_schema`

Builds the MCM surface. Every new user-facing key needs:

- default in `zhopa2_settings.ltx`;
- schema entry;
- English and Russian localization;
- understandable description;
- runtime getter in `zhopa2_cfg` when the value is not read directly.

### 4.3 `zhopa2_memory`

Owns serializable squad memory:

- reset state;
- recent smart / target memory;
- loot value;
- artifact cargo summary;
- interrupted task snapshot;
- resume after night rest;
- squad read/write.

### 4.4 `zhopa2_perception`

Shared selection and validation layer:

- object level;
- neighbor levels;
- hostile/friendly relation;
- smart validity;
- hunt/revenge target validity;
- smart scoring;
- patrol route building;
- safe rest target checks.

Perception must not perform unbounded world scans in hot paths. It should consume candidates from `zhopa2_index` and topology.

### 4.5 `zhopa2_topology`

Tracks level adjacency:

- `se_level_changer` facts;
- configured target maps;
- vanilla nearby-level helpers;
- cached neighbor lists.

Used by `EXPLORE`, `PATROL`, `HUNT`, `ARTEFACT`, `TRADE` and `STORY_NORTH_MIGRATION`.

### 4.6 `zhopa2_debug_hud`

Displays task, target, smart, level, timer, reason, result and module-specific status. Debug HUD is diagnostics only and must not become a logic source.

## 5. Runtime Patch Orchestrator

`zhopa2_runtime_patches.script` is the central compatibility layer.

Rules:

- load the current vanilla/pack module;
- preserve the original function;
- install an idempotent wrapper;
- call previous/original unless ZHOPA intentionally owns that tick;
- avoid full-file replacement unless there is no narrow alternative;
- do not store engine objects in persistent state;
- do not rely on another addon load order without readiness checks.

Current patch anchors:

- `sim_squad_scripted` — squad lifecycle, ZHOPA task update, state read/write, scripted target adapter;
- `sim_board` — squad/smart registration facts and safety wrappers;
- `smart_terrain` — smart update, arrival facts, ownership, service filler hooks;
- `bind_anomaly_zone` — artifact spawn/take/destroy registration;
- `xr_gather_items` — online loot, targeted gather, artifact pickup bridge;
- `xr_corpse_detection` — corpse target filtering and anti-loop cleanup;
- `sim_offline_combat` — offline combat consequences;
- `xr_reach_task` — targeted reach/pickup compatibility;
- `bind_monster` — mutant identity/lifecycle hooks;
- `se_level_changer` — topology facts.

## 6. Task FSM

`zhopa2_tasks.script` owns task constants, task registry, weighted selection, completion and fallback rules.

Current task set:

- `REST`
- `EXPLORE`
- `FORCE_EXIT`
- `POPULATE`
- `BASE_CAMPING`
- `PATROL`
- `NIGHT_REST`
- `ARTEFACT`
- `TRADE`
- `HUNT`
- `REVENGE`
- `STORY_NORTH_MIGRATION`

### 6.1 Selection rules

Stalker random tasks:

- `EXPLORE`
- `POPULATE`
- `PATROL`
- `HUNT`
- `ARTEFACT`
- `TRADE`

Mutant random tasks:

- `HUNT`
- `PATROL`
- `EXPLORE`

`REST`, `NIGHT_REST`, `FORCE_EXIT`, `BASE_CAMPING`, `REVENGE`, story tasks and some trade flows are assigned by explicit conditions, interrupts, safety gates or story systems rather than ordinary weighted roaming.

### 6.2 Safety order

Typical update order:

1. runtime ready / can manage / protected squad checks;
2. blacklist and force-exit gates;
3. story locks;
4. night rest override;
5. active task validation;
6. task-specific executor;
7. completion/fallback;
8. new weighted task selection.

Blacklists must be respected during selection, active task validation, retargeting and completion fallback.

### 6.3 Task semantics

`REST` holds the squad on a safe current smart and gives the selector a pause.

`EXPLORE` sends the squad to a safe smart on the current, neighbor or nearby level.

`FORCE_EXIT` is only for invalid levels and hard safety exits.

`POPULATE` fills underpopulated smart terrains while respecting job capacity and ownership.

`BASE_CAMPING` keeps one managed squad attached to a base through dynamic ownership. It is not a random weighted roam task.

`PATROL` builds a short route through safe smarts and completes by route index or timer.

`NIGHT_REST` interrupts stalkers at night, stores resumable state, and resumes the previous task if it is still valid.

`HUNT` targets direct squad ids, not stale coordinates. The target route must refresh so hunters chase moving squads.

`REVENGE` is a hard interrupt generated by revenge logic. Actor revenge must scope hostility to the involved squad, not the entire faction.

`ARTEFACT` routes to the artifact smart/zone, then uses artifact-specific online/offline pickup logic.

`TRADE` is a post-rest route task whose weight rises with sellable value. It sends the squad only to safe trader smarts on the current or direct-neighbor levels.

`STORY_NORTH_MIGRATION` is a story lock owned by the north migration module.

## 7. Economy and Trade

`zhopa2_economy` owns online and offline trade policy.

Goals:

- NPCs sell real sellable items, not only items just picked up through vanilla flags;
- the leader can trade for the whole squad;
- squad money can be pooled for the leader;
- online trade uses real NPC inventory where possible;
- offline trade sells virtual cargo and uses virtual squad money without creating unnecessary server-side items;
- trader inventory is not polluted by all sold NPC junk;
- NPC purchases can create bounded supplies so invisible NPC buying does not drain the player-facing shop;
- trade emits vanilla-style console/news feedback when enabled.

Sellable examples:

- artifacts;
- excess ammo not needed by equipped weapons;
- unequipped weapons/outfits;
- excess medicine;
- excess grenades;
- excess food/water;
- virtual loot cargo from offline combat and artifact cargo from artifact collection.

Protected examples:

- quest/story/service items;
- equipped weapon/outfit;
- best/current ammo reserve;
- never-sell sections;
- items that fail runtime validation.

Price:

- `npc_sell_price_multiplier` controls how much traders pay NPCs for sold items;
- default is `0.2`;
- the multiplier affects online and offline NPC sale income;
- NPC purchase prices are not reduced by this sale multiplier.

`TRADE` task:

- generated after rest/night rest selection, not as a permanent smart job;
- requires sellable value or supply need;
- candidate trader smarts are current level plus direct neighbors only;
- weight increases with virtual cargo value, real online inventory value and artifact cargo;
- failure sets cooldown and keeps cargo.

Offline trade:

- allowed only when the squad is actually on a smart recognized as trader-capable;
- sells and clears virtual squad cargo;
- buys bounded supplies through an abstract market without draining the trader's inventory;
- uses virtual squad money instead of money-note sections and transfers it to NPC balance when the squad comes online;
- keeps only serializable numbers, strings and tables in memory, never engine userdata.

## 8. Loot Subsystem

`zhopa2_loot` extends vanilla loot without replacing vanilla behavior wholesale.

Online loot:

- respects feature toggle;
- avoids stealing artifact task pickups from the selected artifact gatherer;
- records loot count/value;
- prevents NPC loops on corpses that cannot be fully looted;
- cleans memory/queues after corpse rejection or completed loot.

Offline loot:

- after offline combat, the winner receives bounded virtual cargo instead of mass-creating server-side items;
- value, count and section summaries are recorded for future trade and debug HUD;
- real items are created only during controlled materialization, for example when an online NPC death needs visible loot.

Important rule: when ZHOPA rejects an item or corpse, it must not leave that target in vanilla memory in a way that makes vanilla retry it forever.

## 9. Artifact Subsystem

`zhopa2_artifacts` and artifact buckets in `zhopa2_index` implement both real and virtual artifact economy.

Real artifacts:

- registered from anomaly zone / server entity events;
- assigned to exactly one smart bucket;
- target selection prefers same level, then neighbor, then nearby levels;
- task stores `artifact_id`, `artifact_section`, `artifact_smart`, `artifact_zone`;
- online pickup uses a chosen NPC, approach stage, detector animation and targeted gather;
- force pickup is used only after vanilla/pathing cannot complete the pickup.

Virtual artifacts:

- generated from anomaly config data for offline economy;
- do not reduce real artifact spawn;
- can be selected by offline squads;
- can be materialized into the real path when the player arrives on the relevant level;
- offline collection adds real artifact cargo to squad inventory/economy state.

Retargeting:

- if the assigned artifact is missing when the squad reaches the target smart, the system checks the current smart bucket before failing;
- if an unreserved artifact is available there, the task retargets to it;
- this avoids false failure on stale saves or artifact id desync.

## 10. Story Systems

### 10.1 `zhopa2_story_psy_watchdog`

Psy watchdog is a story-mode system. It converts eligible non-immune stalker squads on configured psi levels before the relevant story protection is resolved.

Rules:

- enabled by default;
- gated by story/freeplay checks;
- immune factions are excluded;
- squad member count is preserved;
- inventory is not transferred;
- old squad is released/unregistered safely;
- debug mode reports converted squad, level and reason.

### 10.2 `zhopa2_story_north_migration`

North migration is a one-shot story event after the configured story trigger.

Rules:

- selected squads receive `STORY_NORTH_MIGRATION`;
- it is not a weighted random task;
- it must not use the old SISKI `story_events_enabled` gate;
- targets are safe northern smarts, validated through current ZHOPA blacklists and faction checks;
- selected squads remain locked until arrival, invalidation, death or controlled recovery;
- on arrival they rest and do not resume the pre-story task.

## 11. Service Fillers and Dynamic Ownership

Dynamic base ownership is part of the core model. It tracks who effectively owns a base smart from real squad presence and faction compatibility.

`zhopa2_service_fillers` uses ownership to place or maintain service roles:

- trader;
- medic;
- mechanic;
- other service job candidates configured by smart/base rules.

Service fillers must not fight the smart job system every frame. They should assign or repair service logic through bounded events and avoid per-tick job spam.

## 12. Blacklists

Blacklists are config-driven and must match their comments.

Expected categories:

- global level exclusions prevent managed admission/simulation;
- task-specific level/smart blacklists remove candidates before task assignment;
- force-exit is reserved for a squad that is already in an invalid level state and needs a real exit route;
- smart blacklist should normally skip selection or safely finish the task, not turn every blacklisted smart into force-exit.

Every task must respect blacklists during:

- candidate collection;
- weighted selection;
- active target validation;
- retargeting;
- fallback selection;
- story task target validation.

## 13. Save/Load and Cleanup Contract

Save safety rules:

- store only primitives and plain serializable tables;
- never store online object handles or userdata;
- tolerate missing modules during load;
- tolerate stale squad/smart/artifact ids;
- clean stale reservations, cargo and debug HUD markers after unregister/death/load.

## 14. Debug and Diagnostics

Normal logging should stay quiet. Success spam is allowed only where explicitly useful, such as trade/loot/artifact test feedback, and should be debug-gated where practical.

Debug tools:

- Debug HUD for active squad state;
- module-specific diagnostic scripts in `debugscripts`;
- console errors for hard failure reasons;
- runtime readiness progress;
- static tests for Lua/localization/config surfaces.

Diagnostics should answer:

- why this squad was accepted or rejected;
- which task was selected and with what weight;
- which smart/artifact/trader was chosen;
- why an active task failed;
- whether a target came from real, virtual or fallback data.

## 15. Extending the System

When adding a new system:

1. Add config defaults to `zhopa2_settings.ltx`.
2. Add MCM schema and localization if it is user-facing.
3. Add the runtime module to `ZHOPA2_RUNTIME_MODULES` if it needs readiness.
4. Register callbacks in the module itself.
5. Keep hot-path work bounded and index-driven.
6. Store only serializable squad/global state.
7. Add debug HUD/diagnostic output only where it helps testing.
8. Update this document and `implementation_plan.md`.

When adding a new task:

1. Add a task constant in `zhopa2_tasks.script`.
2. Define candidate selection and validation.
3. Define completion and failure semantics.
4. Respect blacklists at selection and active validation.
5. Use `zhopa2_assign_task` / interrupt helpers instead of direct vanilla field writes.
6. Add MCM weight/toggle only if the task is user-tunable.
7. Add debug display fields if needed.

## 16. What Must Not Be Reintroduced

- full-file vanilla overrides without a hard reason;
- global `SIMBOARD` scans in ordinary updates;
- storing engine objects in save state;
- hidden globals;
- task logic inside `sim_squad_scripted` wrappers;
- force-exit as a universal blacklist fallback;
- artifact selection based on stale/random item ids;
- online squads using offline-only artifact fallbacks on the actor level;
- trade that creates endless job/preparation loops;
- loot that leaves rejected corpses/items in memory forever.

## 17. Correctness Criteria

The system is healthy when:

- game start and save/load do not crash;
- runtime readiness reaches complete state;
- debug HUD updates and clears stale squads;
- stalker and mutant task pools both work;
- blacklists affect all task stages;
- `HUNT` follows moving squad targets;
- `ARTEFACT` chooses the right smart/artifact and completes online/offline;
- `LOOT` does not cause corpse/item loops;
- online/offline trade performs bounded, visible deals;
- story systems stay gated by story mode and configured triggers;
- old saves with incompatible state are rejected through controlled diagnostics.

