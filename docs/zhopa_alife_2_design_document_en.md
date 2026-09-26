# Z.H.O.P.A. ALIFE 2.3: Architecture Design Document

[README](../README_EN.md) | [Russian version](zhopa_alife_2_design_document.md) | [Function reference](zhopa_alife_2_function_reference_en.md)

Full name: **Z.H.O.P.A. ALIFE 2.3 — Zone Hostile Operations & Population AI**.

This document follows the old ZHOPA design document format: it is an engineering map, not a player-facing README. It describes the current ZHOPA ALIFE 2.3 architecture after the migration from full-file overrides to chain-friendly runtime patches.

> Document status: current development baseline as of September 22, 2026. The current Lua source and the [generated function reference](zhopa_alife_2_function_reference_en.md) remain authoritative for exact callable contracts.

| Layer | Primary files | Responsibility |
| --- | --- | --- |
| Bootstrap and settings | `zhopa2_bootstrap`, `zhopa2_cfg`, `zhopa2_mcm*` | Startup, readiness, LTX/MCM, and user-facing controls |
| Integration | `zhopa2_runtime_patches`, `zhopa2_index`, `zhopa2_topology` | Chain-friendly patches, runtime buckets, and inter-level routing |
| Simulation | `zhopa2_tasks`, `zhopa2_task_scoring`, `zhopa2_perception`, `zhopa2_memory` | Task FSM, bounded task-target scoring, target selection, and serializable squad state |
| Interaction | `zhopa2_npc_quests`, `zhopa2_squad_dialogue`, `modxml_zhopa2_squad_dialogue` | Trader contracts, commander dialogue, destination cards, and joint travel |
| Economy | `zhopa2_economy`, `axr_trade_manager`, `zhopa2_smart_service_slot_doctor` | Online/offline trade, customer jobs, and post-service recovery |
| Items | `zhopa2_loot`, `zhopa2_artifacts` | Online pickup, virtual offline cargo, and artifact flow |
| World and story | `zhopa2_bases`, `zhopa2_service_fillers`, `zhopa2_service_recruitment`, `zhopa2_guard_refill`, `zhopa2_service_quests`, `zhopa2_revenge`, `zhopa2_story_*` | Base ownership, services, revenge, and story events |

## 1. Purpose

ZHOPA ALIFE 2.3 does not build a separate ALife layer on top of Anomaly. It is a motive, task, consequence and economy layer integrated into vanilla SIMBOARD, `smart_terrain`, `sim_squad_scripted`, `xr_gather_items` and related callback points.

Vanilla still owns:

- squad movement between smart terrains;
- online/offline transitions;
- smart job assignment;
- pathfinding and concrete NPC animation life inside a smart;
- ordinary combat behavior.

ZHOPA ALIFE 2.3 owns:

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

`zhopa2_bootstrap` owns the master lifecycle and invokes the runtime patch orchestrator only while the addon is enabled. The central integration surface lives in `zhopa2_runtime_patches`, while each runtime module remains self-contained and registers its own callbacks through `on_game_start()`.

Runtime modules:

- `zhopa2_bases`
- `zhopa2_index`
- `zhopa2_topology`
- `zhopa2_task_scoring`
- `zhopa2_loot`
- `zhopa2_economy`
- `zhopa2_smart_service_slot_doctor`
- `zhopa2_revenge`
- `zhopa2_service_recruitment`
- `zhopa2_service_fillers`
- `zhopa2_guard_refill`
- `zhopa2_service_quests`
- `zhopa2_artifacts`
- `zhopa2_story_psy_watchdog`
- `zhopa2_story_north_migration`
- `zhopa2_npc_quests`
- `zhopa2_squad_dialogue`
- `zhopa2_debug_hud`

Runtime patches:

- `se_level_changer`
- `sim_board`
- `smart_terrain`
- `sim_squad_scripted`
- `axr_companions`
- `bind_anomaly_zone`
- `bind_monster`
- `xr_reach_task`
- `xr_gather_items`
- `xr_corpse_detection`
- `sim_offline_combat`

### 2.2 Master disable lifecycle

The MCM master switch is a runtime transition rather than a passive config gate. Disabling the addon:

1. Sets the global hard gate before any cleanup begins.
2. Stops module-owned work in dependency order and unregisters module callbacks.
3. Cancels managed squad tasks, clears ZHOPA squad/storage/smart fields and returns recruits to ordinary squads and removes legacy spawned service squads.
4. Restores chain-friendly runtime patches only when the current function is still the wrapper installed by ZHOPA. A later foreign wrapper is never overwritten.
5. Keeps only the MCM option-change listener alive so the addon can be enabled again without reloading.

If any cleanup step fails, the addon stays disabled, reports the failed module and retries after the next actor first update. A successful transition guarantees that a newly created save contains no supported ZHOPA runtime state. Re-enabling rebuilds modules, patches, indexes and readiness state from the current world.

The lifecycle does not remove the `axr_trade_manager.script` override from the loaded VM. That file must therefore preserve vanilla behavior behind the master gate. It also cannot reverse consequences already committed to the world.

### 2.3 Runtime readiness

`on_game_start` is too early for some world context. ZHOPA therefore uses a readiness gate:

- patches and runtime modules register early;
- heavy systems wait for required modules, callbacks, actor first update and warmup;
- readiness prints debug progress as `1/x`, `2/x`, ...;
- readiness errors identify the failed item;
- hot paths call `zhopa2_runtime_ready(reason)` when full context is required.

When a new required runtime module or patch is added, it must be added to the readiness list in `zhopa2_runtime_patches.script`. Otherwise a system can start before indexes, MCM defaults, callbacks or save/load recovery are ready.

### 2.4 Callback surface

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
- `zhopa2_previous_task` / `zhopa2_previous_target`
- `zhopa2_npc_quest_id`
- `zhopa2_revenge_*`
- `zhopa2_hunt_prey` for the selected hunt profile, so saved HUNT routing uses the same prey rules after load.

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
- per-level faction-strength snapshots used by the optional destination balance.

Indexes are updated from vanilla events: squad first update, level change, smart enter/leave/update, artifact spawn/take/destroy and unregister cleanup.

### 3.3 Module-owned runtime

Each module owns its own temporary state:

- `zhopa2_economy` - trade queues, customer-job preparation and routing, cooldowns, sell/buy rules, and offline execution;
- `zhopa2_smart_service_slot_doctor` - trade/tech customer-job observation and a deferred vanilla smart-job reselection queue;
- `zhopa2_loot` — targeted pickups, anti-loop corpse marks, offline loot effects;
- `zhopa2_artifacts` — artifact pickup stages, virtual artifact collection, detector animation flow;
- `zhopa2_story_north_migration` — story event selection/status;
- `zhopa2_story_psy_watchdog` — conversion queues and pending reconciliation.
- `zhopa2_npc_quests` — global contract pool, daily revision, reservations, service phases, and bounded retired history;
- `zhopa2_squad_dialogue` — non-serialized travel offer, UI lock, arrival safety, and deferred cross-level finalization.

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
- paid joint travel;
- global and per-faction task switches/weights;
- task-balance MCM switches;
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

Actor-target protection is derived once per frame from active `task_manager.task_info` records, current markers and saved quest targets. Historical `sim_offline_combat.task_squads` or bounty entries left by previews/cancellation do not independently block management. Area quests additionally match the smart/level and target factions. While the task manager is unavailable during loading, marked targets retain a conservative guard. OCS-owned data is never modified; story NPC and hostage protection remains independent.

### 4.5 `zhopa2_topology`

Tracks level adjacency:

- `se_level_changer` facts;
- configured target maps;
- vanilla nearby-level helpers;
- cached neighbor lists.

Used by `EXPLORE`, `PATROL`, `HUNT`, `ARTEFACT`, `TRADE`, `QUEST`, and `STORY_NORTH_MIGRATION`. On load, the level-changer map is rebuilt through exported `alife():iterate_objects()`; the unavailable `object_count()` API is not used.

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
- `tasks_assault`, `tasks_smart_control`, `tasks_dominance`, `xr_conditions` — scoped actor-quest target compatibility: selection and status checks ignore only an ordinary squad's ZHOPA-owned scripted target. Story squads, service NPCs, companions and hostages retain native behavior. Squad fields are untouched; the context is restored on errors and does not apply during movement updates;
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
- `QUEST`
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
- `QUEST`

Mutant random tasks:

- `HUNT`
- `PATROL`
- `EXPLORE`

`REST` enters ordinary weighted selection only when the enabled faction profile gives it a positive weight. Otherwise it remains a direct fallback or pause state. `QUEST` participates only when a compatible published contract exists on the current or neighboring level; once reserved, ordinary tasks cannot interrupt it. `NIGHT_REST`, `FORCE_EXIT`, `BASE_CAMPING`, `REVENGE`, story tasks and some trade flows are assigned through explicit conditions, interrupts, safety gates, or story systems.

Ordinary selection is a bounded candidate pipeline. Builders first expose valid `task + target` pairs without reserving artefacts, modifying trade state, or assigning a job. Each candidate retains its task-specific level priority and carries a base weight, payload, target level, and selection class. `zhopa2_task_scoring` then applies the enabled modifiers to that concrete pair and picks one final candidate; only the selected candidate is materialized. Artefact reservation therefore happens after task assignment, never while targets are being scored.

The optional balance layers are independent:

- geographic balance derives level danger from registered smart game points on the configured north axis, with LTX overrides for levels and squad sections;
- faction-presence balance consumes only incremental SIMBOARD buckets and rewards allied support while discouraging overwhelming hostile presence;
- lore profiles supply task multipliers, prey rules, and directional preferences from `zhopa2_population_profiles.ltx`.

`monster` and `zombied` remain distinct presence factions. They affect presence snapshots but have no geographic or lore profile by default. Direct `HUNT` and `REVENGE` assignments use the Soft / Balanced / Strict geography policy only when they are first accepted; an already accepted route is not cancelled merely because the target moves or local influence changes. Story, surge, and force-exit flows never go through this policy.

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

Automatic selection uses the same non-interruptible-task list as camping assignment, so a nearby hunter or other ineligible candidate cannot block a valid squad farther away. Indirect assignments, including `POPULATE` arrival and camping return, honor current global/faction task toggles. A zero weight alone does not prohibit forced or resumed actions. Generic `resume_task` reports success and clears its snapshot only after confirmed assignment; rejection returns `false` and preserves retry data.

Ordinary base filling, `POPULATE` arrival and `occupy` completion use the shared `assign_base_camping`. `base_camping_timed_enabled` controls the mode (default `true`); `base_camping_duration_game_hours` controls duration (default `6`, range 0.25–72 in-game hours). Both settings are available in LTX and the MCM tasks tab, directly below the base-camping toggle, and apply to all factions and mutants. Disabling makes current and new stays permanent. Enabling starts a fresh timer of the selected duration for permanent garrisons. Changing hours affects new stays without resetting an ongoing remaining timer.

The timer starts after arrival. Its start is stored in `zhopa2_started`, independently of diagnostic reasons, so trading cannot restart it. Interrupted camping resumes its remaining duration. Expiry prevents that smart from automatically pulling the same squad back until it moves beyond 50 meters or changes level. Only this squad–smart pair is blocked; other candidates remain eligible. One ID, `zhopa2_base_camping_release_smart`, survives save/load and clears on departure or master purge.

Completing a timed stay starts an individual squad cooldown on `BASE_CAMPING` at every base. `base_camping_cooldown_game_hours = 12` is LTX-only; `0` disables the time cooldown but not the previous base's 50-meter departure guard. Its start is stored in `zhopa2_base_camping_cooldown_started` as game time through native `w_CTime`/`r_CTime`; level transitions, online/offline switching and save/load do not restart it. Shared eligibility blocks base pulls, `POPULATE` conversion and taking new `occupy` work. An unavailable `occupy` contract is skipped only for that executor, not deleted from the shared pool. Interrupted or permanent stays do not start the cooldown; expiry uses the current LTX value.

When a moving squad is intercepted, its `EXPLORE`, `POPULATE`, `PATROL`, `TRADE` or `ARTEFACT` task is stored separately in `zhopa2_base_camping_return`: one string snapshot of the task, target, remaining duration, patrol and artifact data. Night rest and save/load preserve it. Camping completion resumes it through normal assignment, rechecking the target, blacklists and artifact reservation; otherwise it falls back to ordinary rest. Stationary squads and completed `occupy` contracts create no return task. Squad serialization uses version 19 with 49 fields; older versions default missing fields to nil.

`PATROL` builds a short route through safe smarts and completes by route index or timer.

`NIGHT_REST` interrupts stalkers at night, stores resumable state, and resumes the previous task if it is still valid.

`HUNT` targets direct squad ids, not stale coordinates. The target route must refresh so hunters chase moving squads.

`REVENGE` is a hard interrupt generated by revenge logic. Actor revenge must scope hostility to the involved squad, not the entire faction. Goodwill snapshots, changes, and restoration use ALife/server ids; transient online wrappers must not be used for `general_goodwill` or `set_relation` in this hot path.

`ARTEFACT` routes to the artifact smart/zone, then uses artifact-specific online/offline pickup logic.

`TRADE` is a post-rest route task whose weight rises with sellable value. It sends the squad only to safe trader smarts on the current or direct-neighbor levels.

`QUEST` reserves one published trader contract and runs its FSM from giver to objective and, when required, back for reporting. The concrete kind and phase belong to `zhopa2_npc_quests`; `zhopa2_tasks` protects the route and delegates updates.

`STORY_NORTH_MIGRATION` is a story lock owned by the north migration module.

### 6.4 NPC squad quests

`zhopa2_npc_quests` stores a versioned global pool and supports five kinds: `documents`, `clear`, `occupy`, `hunt`, and `delivery`. A trader publishes a bounded number of jobs from its profile; squads select only existing `AVAILABLE` contracts on their current or directly adjacent level. An active contract moves through `RESERVED`, `IN_PROGRESS`, `RETURNING`, `COMPLETED`, or `FAILED` and has exactly one executor.

Online interaction uses a real trade customer job only for approach and animation. `axr_trade_manager` recognizes the quest token and completes the service phase before monetary trade; path/intent state is then cleared, the NPC immediately receives `select_npc_job`, and the service doctor remains a fallback. Offline or unsafe online preparation uses a one-minute smart-level fallback.

Documents and packages are real ZHOPA-specific sections. Online, the commander picks the document from the top of its backpack through pickup animation, while a delivery package is issued into commander inventory during the giver service phase; offline, the equivalent server transfer completes the phase. A reward is added exactly once to `zhopa2_virtual_money`. `clear` returns for reporting, `occupy` transitions the winner into `BASE_CAMPING` using the shared mode and duration settings, `hunt` follows the target squad, and `delivery` carries a selected package between compatible traders.

### 6.5 Commander dialogue and joint travel

`modxml_zhopa2_squad_dialogue` adds a dedicated dialogue without overriding `dialog_manager`. It is available only to the living commander of a managed squad. The response shows current/previous activity, NPC-quest kind, and a destination card with area image, level name, and localized smart name when available.

Travel uses the moving squad's actual `assigned_target_id` and revalidates it at confirmation. Combat, emission/psi storm, relations, money, and Story Mode psi levels are checked. Ordinary arrival temporarily suppresses threats within 30 meters; `HUNT`, `REVENGE`, and combat NPC quests instead place actor and squad at a safe offset from the target without deleting it.

Time uses global distance and `squad_travel_minutes_per_100m`. Optional price equals distance in meters times `squad_travel_price_multiplier`, therefore 1,000 RU per kilometer at multiplier `1`. Same-level travel can roll back position/payment after a late error. Cross-level time advancement finishes after the actor successfully netspawns on the destination level, while a rejected `ChangeLevel` restores the squad to its origin.

## 7. Economy and Trade

The trade contour has split ownership:

- `zhopa2_economy` owns queueing, online trade-intent preparation, temporary customer-job priority boost, runtime path-point repair, pricing, cooldown/results, virtual cargo/money, and offline execution;
- `axr_trade_manager.script` is the intentional SISKI-derived vanilla manager override and the only online deal executor;
- the selected game trade job supplies the actual seller through `npc_info.job.seller_id`; ZHOPA2 does not replace it with a preselected NPC.

Goals:

- NPCs sell real sellable items, not only items just picked up through vanilla flags;
- the leader can trade for the whole squad;
- squad money can be pooled for the leader;
- online trade uses real NPC inventory where possible;
- offline trade sells virtual cargo and uses virtual squad money without creating unnecessary server-side items;
- trader inventory is not polluted by all sold NPC junk;
- NPC purchases can create bounded supplies so invisible NPC buying does not drain the player-facing shop;
- trade emits vanilla-style console/news feedback when enabled.

Mechanics are not regular trade providers. Tech customer intent is created only for a real `i_upgrade` item already held by the NPC; ordinary supply purchases do not create a synthetic repair item or route the customer to a mechanic.

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

Online preparation:

- when the customer slot is busy or the squad is not first in queue, no NPC state is changed;
- normal vanilla job selection is attempted first;
- only after native selection fails may ZHOPA2 temporarily raise the priority of a free exclusive trade-customer job;
- when the configured job point has no valid level vertex, only runtime path data is rewritten to the nearest accessible vertex toward the trade point;
- original priority and prepared metadata are restored on success, cancel, and timeout.

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

## 11. Service NPCs and Dynamic Ownership

Dynamic ownership covers the whole compound base and one vote from the local player's actual faction. `zhopa2_service_fillers` queues trader, technician, medic and cook/barman vacancies; guides are not supported yet. Smart updates and population events refresh the queue. `zhopa2_service_recruitment` owns the shared existing-NPC transfer, load restoration and rollback. Production recruitment creates no NPCs and is not triggered by emissions.

`service_filler_enabled` controls the system; `service_filler_interval_sec` sets the retry interval (15 real seconds by default). Services and guards share a 0.5-second timer: up to eight queue entries are examined, with at most one smart processed/appointment made per step. Catalogs and presence are cached; vacancies are rechecked before transfer. Offline entries remain unconfirmed until the level and job tables load; incomplete data defers recruitment.

Eligible owner-faction donors across the whole base have priority, followed by factions neutral or allied to the owner and existing services and guards. Relations are checked in both directions. The NPC must be alive, online and physically near a member smart; its registration may belong to a neighboring smart. Story, quest and companion NPCs remain protected. Donor faction, ID and inventory are retained. Only an empty squad container is created; one NPC is detached while remaining members continue simulation. A singleton can also donate; its empty source squad is removed after successful transfer.

The original workplace supplies the service profile, dialogue, stock and tasks. `zhopa2_service_quests` supports task offers, turn-in and cancellation with giver checks; DXML modules adapt branches only for recruited services. Lua replenishes trade funds, while GAMMA repair restrictions remain respected. Unknown or unconfirmed jobs are skipped; named NPCs without a suitable native job are not automatically replaced.

Migration removes services spawned by the old filler, preserving originals and existing recruits. Recruitment records contain serializable data only (limit 2048), including the source smart for rollback. Disabling an individual option stops new appointments; the ZHOPA master switch returns living recruited services and guards to ordinary squads, including offline recruits.

Read-only diagnostics `zhopa2_service_recruitment.audit_level()` and the compatible alias `zhopa2_recruit_trader_probe.audit_level()` ship in the release. `test_smart()` is a separate destructive test command: it kills services and creates ordinary donor squads, then uses the same recruitment mechanism. Guard diagnostics are available through `zhopa2_guard_refill.audit_level()`.

`zhopa2_smart_service_slot_doctor` handles visitors, not providers, in trade/tech customer jobs. It recognizes customer jobs by section name or their `suitable` condition, waits for confirmed completion/stall, and clears only the completed intent. Recovery goes through vanilla `smart:select_npc_job(npc_info, true)`; direct `state_mgr` resets, forced `idle`, and vertex teleporting are forbidden.

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

The master switch provides bounded ZHOPA2 uninstall preparation for the currently loaded world. The supported procedure is to load the save with the addon enabled, disable it in MCM, wait for successful cleanup, create a new manual save, exit the game, and only then remove the addon. A cleanup error blocks safe removal.

Cleanup covers ZHOPA tasks and fields, the global NPC-quest pool, temporary service/travel tables, script storage, recruitment rollback and legacy spawned service squads, callbacks, indexes, debug markers and restorable monkey patches. It does not reverse deaths, spawned or collected objects, completed trade, zombification, migration or changes owned by another addon. It is not a SISKI/ZHOPA1 save migration system; old-save compatibility remains non-destructive and best-effort.

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
- which NPC-quest phase is active and why a service/travel operation was accepted, cancelled, or recovered.

## 15. Extending the System

When adding a new system:

1. Add config defaults to `zhopa2_settings.ltx`.
2. Add MCM schema and localization if it is user-facing.
3. Add the runtime module to `ZHOPA2_RUNTIME_MODULES` if it needs readiness.
4. Register callbacks in the module itself and unregister them from `on_master_disable`.
5. Clear every module-owned runtime/save field from `on_master_disable`.
6. Register runtime patches through the restorable patch helpers and preserve foreign wrappers.
7. Keep hot-path work bounded and index-driven.
8. Store only serializable squad/global state.
9. Add debug HUD/diagnostic output only where it helps testing.
10. Update this document and `implementation_plan.md`.

When adding a new task:

1. Add a task constant in `zhopa2_tasks.script`.
2. Define a bounded valid candidate builder and validation; one-candidate legacy builders remain supported.
3. Define completion and failure semantics.
4. Respect blacklists at selection and active validation.
5. Use `zhopa2_assign_task` / interrupt helpers instead of direct vanilla field writes.
6. Add MCM weight/toggle only if the task is user-tunable.
7. Add debug display fields if needed.

## 16. What Must Not Be Reintroduced

- full-file vanilla overrides without a hard reason; the current `axr_trade_manager.script` is the documented exception required for the tested SISKI/vanilla trade flow;
- global `SIMBOARD` scans in ordinary updates;
- storing engine objects in save state;
- hidden globals;
- task logic inside `sim_squad_scripted` wrappers;
- force-exit as a universal blacklist fallback;
- artifact selection based on stale/random item ids;
- online squads using offline-only artifact fallbacks on the actor level;
- trade that creates endless job/preparation loops;
- goodwill reads or writes through transient online NPC wrappers inside revenge actor updates; use server ids instead;
- loot that leaves rejected corpses/items in memory forever.
- destructive `_G` or `package.loaded` cleanup used as an uninstall mechanism;
- module callbacks or runtime patches that cannot be removed by the master lifecycle.

## 17. Correctness Criteria

The system is healthy when:

- game start and save/load do not crash;
- disabling the master switch immediately stops ZHOPA, clears supported save state, and can be reversed by enabling it again;
- runtime readiness reaches complete state;
- debug HUD updates and clears stale squads;
- stalker and mutant task pools both work;
- blacklists affect all task stages;
- `HUNT` follows moving squad targets;
- `ARTEFACT` chooses the right smart/artifact and completes online/offline;
- `LOOT` does not cause corpse/item loops;
- online/offline trade performs bounded, visible deals;
- all five NPC-quest kinds complete online/offline without duplicate rewards or a stuck customer job;
- joint travel keeps actor and squad together, computes time/price correctly, and restores state on failure;
- completed trade/tech customer jobs return to smart terrain through the vanilla job lifecycle;
- revenge causes no BusyHands and does not change the entire faction's attitude toward the actor;
- story systems stay gated by story mode and configured triggers;
- old saves are read best-effort without destructive cleanup; invalid ids and missing fields must not break runtime.


## Compound Bases

`zhopa2_bases.script` reads the approved `zhopa2_base_clusters.ltx` and resolves names through native `SIMBOARD.smarts_by_names`. No object references are saved. Missing members and members on another level are excluded; ungrouped smarts retain their own identity.

The index calculates ownership, population and garrison presence across the compound, deduplicating NPC registrations, squads and the player's vote. Capacity remains local: roaming uses aggregate base occupancy, but a full or unavailable member remains an invalid destination. Candidate collection and scoring count each physical base once.

Service Filler retains per-smart vacancies and searches local donors before other members of the same compound. Transfer unregisters only the selected NPC and assigns its service squad/job at the destination. `donor_smart_id` records the rollback origin; older records without it keep the previous behavior. `audit_level()` emits `audit_base` membership records.

After BASE_CAMPING ends, the departure guard covers the whole compound. Automatic settlement honors a garrison already reserved by a sibling smart and shares its retry interval, preventing multiple parts from intercepting additional squads at once.

`simulation_objects.available_by_id` / `sim_avail` controls simulation target selection and native respawning. It does not by itself forbid assigning an existing NPC to a confirmed service job: recruitment checks `disabled`, `respawn_only_smart`, online data and the job conditions. Roaming still respects `sim_avail`. `audit_donor` reports the selected donor or specific rejection counts.

Donor selection considers all owner-faction squads before non-hostile factions. Live game_relations checks run in both directions against the owner and existing service factions; unknown relations defer recruitment. The container and saved service_faction follow the donor, while owner remains the base-ownership snapshot. A registered NPC physically inside the base may donate even when registered elsewhere; donor_smart_id preserves the original registration for rollback.

## Guard Refill

`zhopa2_guard_refill` maintains a cached defensive-post catalog and a scalar-ID queue. Smart updates/population events feed it through the service filler; it shares that timer and the one-appointment-per-step budget. All core service roles across the compound must be filled first. A step checks up to eight queued IDs and processes at most one smart; retry spacing uses service_filler_interval_sec. Occupancy is collected in one pass and refreshed after load.

Generated guard/sniper/camper jobs and guard/security/sniper/camper-named exclusive jobs are recognized. Followers, attacker jobs, trading and monster/heli jobs are excluded. Paths/covers must exist; beh posts use pt1 coordinates. Physical path aliases share one vacancy. Section owners, registered NPCs, saved jobs, native active logic and persistent reservations prevent duplicates. An ordinary transient occupant can be promoted in place; native scripted/story guards are retained.

Transfer, identity, serialization and rollback use `zhopa2_service_recruitment` with role=guard and saved guard_post/job_section. *_sim_squad_guard containers are excluded from simulation management even before runtime flags restore. scripted_target/always_arrived pin the squad; narrow job-selection, setup and precondition hooks pin the post against Redone rotation. Native surge shelter jobs remain available, with return to the post afterward. Normal combat remains enabled. Guards receive no service dialogue, stock or money refills.

Normal dialogue-based companion hiring is blocked for guards. The underlying join action remains available to guide quests and debug commands. Disabling guard_refill_enabled stops new appointments but retains existing records. Master-disable uses the common undo path, including offline guards. No all.spawn change, story-ID spoofing or NPC creation is used. Third-party code that directly teleports NPCs without job changes is outside these hooks.
