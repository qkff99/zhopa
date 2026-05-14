# ZHOPA: Architecture Design Document

Russian version: `docs/zhopa_0.7_design_document.md`

Note: the filename is historical. This document describes the current runtime architecture implemented in this workspace, not the old 0.7 branch.

## 1. Purpose
ZHOPA is a decentralized reactive ALife layer for Anomaly 1.5.3.

The runtime model is:
- engine callbacks enter `zhopa.core`;
- `zhopa.core` routes engine callbacks directly to module methods;
- modules keep only local runtime state behind explicit `zhopa.*` methods;
- delayed logic uses keyed timers from `zhopa.timers`;
- there is no central steady-state dispatcher;
- there is no whole-world scan loop;
- there is no cadence-based world traversal policy.

Architecture invariants:
- nil safety everywhere engine objects are touched;
- save safety: only serializable data enters save state;
- bounded hot paths;
- vanilla-first compatibility;
- no subsystem should require a global maintenance loop to stay correct.

## 2. Bootstrap and Runtime Flow

### 2.1 Load order
Current `gamedata/scripts/zhopa.script` is a monolithic runtime bundle. Internal logical block order:
1. `zhopa_oop`
2. `zhopa_switches`
3. `zhopa_timers`
4. `zhopa_core`
5. `zhopa_safe`
6. `zhopa_log`
7. `zhopa_heli_guard_patch`
8. `zhopa_config`
9. `zhopa_board_index`
10. `zhopa_npc_faction_override`
11. `zhopa_xr_conditions_patch`
12. `zhopa_memory`
13. `zhopa_story_psy_watchdog`
14. `zhopa_story_events`
15. `zhopa_smart_tasks`
16. `zhopa_trade`
17. `zhopa_tasks_registry`
18. `zhopa_mutants`
19. `zhopa_base_filler`
20. `zhopa_dynamic_bases`
21. `zhopa_service_filler`
22. `zhopa_axr_task_patch`
23. `zhopa_loot`
24. `zhopa_loot_patch`
25. `zhopa_fast_trading`
26. `zhopa_debug_hud`
27. `smart_service_slot_doctor`

`axr_trade_manager.script` remains a separate external bridge required during startup. `zhopa_mcm.script` remains a separate MCM adapter. `zhopa_mcm_schema.script` is the single schema source used by runtime config and MCM.

### 2.2 Startup hook order
1. `zhopa.loot.on_game_start()`
2. `zhopa.loot_patch.on_game_start()`
3. `zhopa.fast_trading.on_game_start()`
4. `zhopa.npc_faction_override.on_game_start()`
5. `zhopa.heli_guard_patch.on_game_start()`
6. `zhopa.board_index.on_game_start()`
7. `axr_trade_manager.on_game_start()`
8. `zhopa.core.on_game_start()`

`zhopa_story_events`, `zhopa_smart_tasks`, and `zhopa_story_psy_watchdog` expose direct methods called by `zhopa.core`.

### 2.3 Callback surface
`zhopa.core` is the central engine callback hub:
- `actor_on_first_update`
- `on_option_change`
- `server_entity_on_register`
- `server_entity_on_unregister`
- `squad_on_first_update`
- `squad_on_update`
- `squad_on_npc_creation`
- `squad_on_npc_death`
- `squad_on_enter_smart`
- `squad_on_leave_smart`
- `squad_on_after_level_change`
- `smart_terrain_on_update`
- `npc_on_update`
- `npc_on_item_take`
- `npc_on_item_drop`
- `npc_on_death_callback`
- `actor_on_item_drop`
- `save_state`
- `load_state`

Important rules:
- `squad_on_update` is the main gameplay decision point;
- `enter_smart`, `leave_smart`, and `after_level_change` only mutate save-safe state;
- there is no global `on_update` dispatcher;
- `axr_trade_manager` also hooks `npc_on_item_take`;
- `zhopa.core` routes events; it does not run the simulation itself.

## 3. Data Model

### 3.1 `zhopa_memory`
`zhopa_memory` is the authority layer for squad entries and task state.

It stores only serializable data:
- identity and snapshot fields;
- task state;
- freshness flags;
- save-safe runtime metadata.

Removed legacy structures:
- sweep wheel;
- global freshness sweeps;
- per-level logic shards;
- hidden steady-state maintenance loops.

### 3.2 `zhopa_board_index`
`zhopa_board_index` owns the reactive world index.

It tracks:
- `smarts_by_level`
- `base_smarts_by_level`
- `respawn_base_smarts_by_level`
- `squads_by_level`
- `smart_level_by_name`
- `smart_name_by_id`
- `squad_level_by_id`
- topology neighbors

Behavior:
- hydrate from `SIMBOARD` on bootstrap and load;
- maintain indexes through register/update/enter/leave/level-change callbacks;
- build topology from level-changer events and save it;
- the old `smart_scan`, `squad_scan`, and `static_scan` runtime is gone.

### 3.3 Module-owned runtime
Some modules own their runtime state directly, but still follow the same save-safe rules:
- `zhopa_story_events` keeps its own state blob;
- `zhopa_smart_tasks` keeps claim caches and dirty-smart state;
- `zhopa_story_psy_watchdog` keeps transient caches only;
- filler modules keep their own reconcile queues and timestamps.

## 4. Foundation Modules

### 4.1 `zhopa_oop`
Local class/singleton helper. It only exists to standardize how modules are instantiated and exposed.

### 4.2 `zhopa_switches`
Runtime module switch matrix. Used for feature gating on boot and at runtime.

### 4.3 `zhopa_timers`
Keyed timer registry.

Used for:
- debounce;
- cooldown;
- timeout;
- reevaluate;
- cleanup;
- delayed continuation.

### 4.4 `zhopa_safe`
Nil-safe wrapper layer around engine access. Its job is to centralize guards, `pcall` boundaries, and fallback handling.

### 4.5 `zhopa_log`
Central logger with log-level gating. At `log_level = 0`, the log file should not be created.

### 4.6 `zhopa_config`
Configuration access layer.

Read order:
1. runtime override;
2. MCM;
3. LTX default.

It owns:
- `level_smarts_*`;
- `level_neighbors`;
- `anomaly_smarts`;
- `level_bases`;
- smart-task blacklist/whitelist maps;
- trade/base/service/loot knobs;
- feature toggles.

Helper groups:
- LTX/MCM reading and caching;
- CSV and section parsing;
- normalized blacklist rules;
- smart-task maps;
- runtime override cache;
- MCM path resolution.

## 5. Orchestrator: `zhopa.core`

### Responsibility
`zhopa.core` is the runtime entry point. It:
- registers engine callbacks;
- syncs log level;
- bootstraps enabled runtime;
- routes callback subjects directly to module methods;
- routes save/load;
- dispatches `squad_on_update` into specialized FSMs.

### Public API
- `is_enabled()`
- `on_game_start()`
- `on_first_update()`
- `on_option_change()`
- `save_state(m_data)`
- `load_state(m_data)`
- `on_squad_npc_death(...)`
- `on_squad_first_update(...)`
- `on_squad_update(...)`
- `on_squad_enter_smart(...)`
- `on_squad_leave_smart(...)`
- `on_squad_after_level_change(...)`
- `on_server_entity_register(...)`
- `on_server_entity_unregister(...)`
- `on_smart_terrain_update(...)`
- `on_npc_update(...)`
- `on_npc_item_take(...)`
- `on_npc_item_drop(...)`
- `on_npc_death(...)`
- `on_actor_item_drop(...)`

### Key helpers
- `can_run(name)` - switch/config gate;
- `safe_call(tag, fn, ...)` - safe engine call;
- `route_*` helpers - bounded direct fan-out to module methods;
- `update_memory_snapshot(squad, source)` - refresh `zhopa_memory`;
- `dispatch_direct_squad_fsm(squad, source)` - route a squad into the FSM chain;
- `apply_runtime_fixes()` - runtime shims/fixes;
- `get_offlevel_squad_update_skip_count()` and related helpers - skip control for off-level updates;
- `debug_hud_enabled()` - runtime gate for the HUD.

### Algorithm
1. On game start, load dependencies in the correct order.
2. On first update, perform one-shot hydration.
3. On `squad_on_update`:
   - story events first;
   - smart tasks second;
   - mutant FSM or stalker FSM next;
   - post-actions last.
4. `enter_smart`, `leave_smart`, and `after_level_change` only sync state; they are not decision points.

## 6. World Index: `zhopa.board_index`

### Responsibility
This module owns ZHOPA's current world map: smarts, squads, topology, and revisions.

### Public API
- `reset_runtime(reason)`
- `save_state(m_data)`
- `load_state(m_data)`
- `on_game_start()`
- `get_level_smarts(level_name, opts_or_fn)`
- `get_base_smarts(level_name, opts_or_fn)`
- `get_respawn_base_smarts(level_name, opts_or_fn)`
- `get_known_smart_levels()`
- `get_level_squads(level_name)`
- `get_smart_level(smart_name)`
- `get_smart_name_by_id(smart_id)`
- `get_level_neighbors(level_name, opts_or_fn)`
- `get_topology_revision(level_name)`
- `get_smart_revision(level_name)`

### Main algorithms
- bootstrap hydration from `SIMBOARD`;
- incremental upsert/remove on register/unregister;
- squad level tracking on enter/leave/after_level_change;
- neighbor topology rebuild from level-changer data;
- cached per-level view materialization with revisions;
- diagnostics counters for broken or missing data.

### Helper clusters
- bucket helpers: `append_level_value`, `set_level_value`, `unset_level_value`, `build_sorted_bucket_array`;
- topology helpers: `merge_unique_arrays`, `append_level_edge`, `edge_sets_to_arrays`, `copy_edge_map`, `copy_array_map`, `copy_level_changer_edges`;
- state packet helpers: `make_state_packet`, `get_level_changer_data`, `get_level_changer_data_fallback`;
- filtering helpers: `is_base_smart`, `is_respawn_base_smart`, `is_level_name`, `level_from_object`, `object_name`;
- diagnostics: `create_runtime`, `ensure_diag`, `diag_inc`, `diag_push`, `diag_fail`, `diag_last`.

## 7. Authority Layer: `zhopa.memory`

### Responsibility
`zhopa_memory` is the save-safe authority store for squad lifecycle, task state, and runtime indexes.

### Public API
- `get_state()`
- `get_runtime()`
- `get_squad_entry(squad_id)`
- `validate_live_squad(se_squad, source)`
- `touch_squad_validated(se_squad, mark_seen, source)`
- `purge_squad_entry(squad_id, reason, source)`
- `touch_squad(squad_id, mark_seen, source)`
- `update_squad_snapshot(squad)`
- `update_squad_snapshot_verified(squad, squad_id)`
- `upsert_snapshot(squad, source)`
- `set_task_current(squad_id, task)`
- `clear_tasks(squad_id)`
- `get_managed_squads_by_level()`
- `get_anchor_index()`
- `get_communities_by_smart_level()`
- `get_trade_target_occupancy()`
- `mark_dirty(squad_id, key)`
- `mark_arrived_to_target(squad_id, smart_ref, source)`
- `mark_left_target(squad_id, smart_ref, source)`
- `mark_level_changed(squad_id, old_level, new_level, source)`
- `prune_missing_squads_once(source)`
- `consume_dirty(entry, key)`
- `get_memory_stats()`
- `is_protected_squad(se_squad)`
- `should_manage_squad(se_squad)`
- `on_squad_npc_death(...)`
- `reset_runtime(reason)`
- `save_state(m_data)`
- `load_state(m_data)`
- `set_surge_lock(squad_id, locked)`
- `get_surge_lock(squad_id)`

### Stored state
- entry snapshots;
- `task.current` / `task.prev` / `task.next`;
- dirty flags;
- last-seen time;
- trade/anchor/occupancy indexes;
- protected squad markers;
- surge lock markers;
- normalized loaded state.

### Helper clusters
- sanitization: `clone_serializable`, `compact_task`, `compact_entry`, `_normalize_loaded_task`, `_normalize_loaded_entry`;
- index lifecycle: `_index_entry`, `_unindex_entry`, `_reindex_entry`, `_rebuild_runtime_indexes`;
- entry lifecycle: `_validate_live_squad`, `_touch_squad`, `_touch_squad_validated`, `_purge_squad_entry`, `_prune_missing_squads_once`;
- task lifecycle: `_set_task_current`, `_clear_tasks`, `reset_task_scheduler_fields`, `_ensure_tasks_shape`;
- arrival/level lifecycle: `_mark_arrived_to_target`, `_mark_left_target`, `_mark_level_changed`;
- persistence: `_save_state`, `_load_state`;
- protection logic: `_is_protected_squad`, `_should_manage_squad`, `_is_monster_squad_live`, `_is_companion_squad_id`;
- surge control: `_set_surge_lock`, `_get_surge_lock`.

### Algorithm
`memory` does not decide gameplay by itself. It:
1. normalizes live squad snapshots;
2. validates serializable fields;
3. indexes entries by level/smart/community;
4. marks dirty state for consumers;
5. exposes save/load blobs with no userdata or engine references.

## 8. Stalker Task FSM: `zhopa.tasks_registry`

### Responsibility
This is the main stalker task engine. It builds, selects, validates, and completes tasks for regular squads.

### Public API
- `update_squad_tasks(se_squad, ctx)`
- `on_first_update()`
- `on_option_change()`
- `get_runtime_stats()`
- `force_rest_after_external_reclaim(se_squad, source)`
- `is_smart_spawn_allowed(smart_name, community, level_name, section_name)`
- `build_base_camping_task(...)`
- `build_patrol_task(...)`
- `build_night_rest_task(...)`
- `build_trade_task(...)`

### Task types
- `REST_1H`
- `EXPLORE`
- `ARTEFACT`
- `BASE_CAMPING`
- `PATROL`
- `POPULATE`
- `TRADE`
- `NIGHT_REST`

### Algorithmic pipeline
1. Build a `ReactiveContext`.
2. Read the entry from `zhopa.memory`.
3. Build or validate the current task.
4. Rotate on completion.
5. Apply live `scripted_target` when needed.
6. Keep `TRADE` trigger-driven and outside the generic roam rotation.

### Key helper clusters
- build-prep runtime: `_reset_build_prep_runtime`, `_ensure_build_prep`, `_get_build_ctx_ttl_ms`, `_get_logic_index`;
- board/context synthesis: `_get_effective_neighbors`, `_get_effective_level_bases`, `_get_level_search_bundle`, `_get_smart_bucket_bundle`, `_get_populate_anchor_bundle`, `_get_populate_candidate_bundle`, `_prepare_reactive_context`;
- safety filters: `smart_has_trader_slot_ltx`, `smart_has_trader_slot_runtime`, `smart_has_tech_slot_runtime`, `smart_has_real_trader`, `smart_has_enemy_for_faction`, `has_enemy_stalker_near_smart`, `is_roam_smart_allowed`;
- target selection: `pick_random_valid`, `pick_random_valid_safe`, `pick_base_camping_target_smart`, `pick_next_patrol_target`, `pick_trade_target_smart`;
- task builders: `build_rest_task`, `build_explore_task`, `build_force_exit_task`, `build_populate_task`, `build_artefact_task`, `build_roam_task`, `build_trade_task`;
- task state: `clear_task_apply_state`, `task_state_timer_name`, `schedule_task_state_timer`, `sync_task_state_timer`, `task_state_delay_ms`, `apply_task_timer_state`;
- target handling: `set_scripted_target`, `resolve_target_smart_id`, `enforce_online_task_intent`, `should_revalidate_target`, `is_task_target_valid`;
- completion: `vanilla_am_i_reached`, `is_squad_arrived_to_smart`, `is_task_completed`;
- runtime flow: `ensure_current_task`, `rotate_task_on_complete`, `apply_task`, `tasks.update_squad_tasks`.

### Task semantics
- `REST_1H`: regular rest with optional clamp by game seconds.
- `EXPLORE`: move to a neighboring level and pick a safe smart.
- `ARTEFACT`: move to an anomaly smart and check nearby artefact / online pickup path.
- `BASE_CAMPING`: wait at a safe base.
- `PATROL`: walk smarts without repeats.
- `POPULATE`: move toward allied presence.
- `TRADE`: move to a smart with a trader job slot.
- `NIGHT_REST`: night-only rest fallback.

## 9. Trade Contract: `zhopa.trade`

### Responsibility
`zhopa.trade` owns the task-side contract for `TRADE` and local timeout timers.

### Public API
- `notify_trade_started(npc_id, smart_name, source)`
- `consume_trade_started(squad_id, expected_target)`
- `reset_runtime()`
- `consume_service_event(squad_id, expected_target)`
- `can_trade_now(se_squad)`
- `tick(se_squad, entry, task)`

### Algorithm
1. `npc_on_item_take` or service callbacks create a service event.
2. `trade` checks surge lock and live state.
3. `can_trade_now` decides whether `TRADE` may start.
4. Start/end sync happens through memory and direct core routes.
5. Timeouts and cooldowns use keyed timers, not a global polling loop.

### Helper clusters
- service result storage: `apply_service_event_to_memory`, `remember_service_event`;
- surge gate: `surge_started_uncached`, `is_surge_started`, `get_surge_lock`;
- smart/job inference: `infer_seller_id_from_smart`, `smart_has_trader_job_slot`, `resolve_live_trader_for_trade_smart`, `evict_leader_from_trade_job`;
- trade state: `prepare_trade_flags`, `is_trade_job`, `is_tech_job`, `is_trader_job`, `has_service_items`, `get_service_state`, `get_trade_phase`.

## 10. Vanilla Trade Bridge: `axr_trade_manager`

### Responsibility
This module extends the vanilla NPC-to-NPC trade/service flow. It does not replace vanilla; it augments intents, service flags, and condition/effect handlers.

### Main entry points
- `on_game_start()`
- `npc_on_item_take(...)`
- `check_trade_item(...)`
- `zhopa_npc_has_items_to_sell`
- `zhopa_trade_job_sell_items`
- `zhopa_trade_job_give_id`
- `zhopa_npc_trade_buy_sell_impl`
- `check_tech_item(...)`
- `xr_conditions.npc_has_tech_items`
- `xr_effects.tech_job_upgrade_items`
- `xr_effects.tech_job_give_id`
- `npc_tech_upgrade_sell(...)`

### What it does
- stores per-NPC trade/tech intent in `db.storage`;
- supports service job lifecycle;
- binds NPC item take to vanilla trade hooks;
- restores `seller_id` / service bindings when vanilla loses them;
- finalizes sessions and clears storage;
- excludes provider NPCs from their own customer path.

### Why the provider guard matters
This is where the class of bug lives where a service NPC can receive its own `has_tech_items` or `has_items_to_sell` flag and get trapped in a stand/sit loop. Provider-role NPCs must be excluded from the customer-intent path.

### Key helper clusters
- suppression: `begin_item_take_suppress`, `end_item_take_suppress`, `is_item_take_suppressed`, `create_item_self_suppressed`;
- job classification: `is_trade_job`, `is_tech_job`, `is_trader_job`, `smart_has_trader_job_slot`, `smart_has_tech_job_slot`, `smart_has_free_tech_job_slot`;
- candidate selection: `pick_random_buy_candidate`, `pick_random_mechanic_bonus_candidate`;
- state update: `mark_tech_item_intent`, `clear_service_intents`, `finalize_service_session`, `notify_zhopa_trade_service_result`, `notify_zhopa_trade_started`;
- logging: `emit_prefixed_log`, `emit_zhopa_trade_log`, `log_trade_info`, `log_trade_warn`, `log_handler_binding_state`.

## 11. Smart Control Tasks: `zhopa.smart_tasks`

### Responsibility
`zhopa.smart_tasks` owns the smart-terrain `control` task type.

### Public API
- `update_squad_tasks(se_squad, ctx)`
- `on_game_start()`

### Main rules
- smart control lives through claim caches;
- dirty smart state reconciles through direct core routes and timers;
- conflict resolution is based on current live occupancy;
- assignment must not require a scan loop;
- `control` is an ownership/occupation task, not a roam task.

### Algorithm
1. Build smart context.
2. Synthesize a claim snapshot from memory and live board.
3. Check conflicts and relation rules.
4. Pick a candidate for control.
5. Create or refresh the `control` task.
6. Validate or drop stale current tasks.

### Key helper clusters
- target sync: `is_target_sync_enabled`, `get_online_intent_enforce_enabled`, `set_scripted_target`, `set_squad_always_arrived`;
- online squad checks: `is_online_squad`, `try_soft_register_squad_to_smart`, `try_soft_assign_free_stalker_jobs_once`, `enforce_online_task_intent`, `clear_live_task_state`;
- blacklists and filters: `smart_blacklists_global_set`, `smart_blacklists_rule`, `faction_level_blacklists_rule`, `faction_smart_blacklists_rule`, `section_level_blacklists_rule`, `section_smart_blacklists_rule`, `entry_allowed_for_smart_task`;
- identity and claims: `build_identity_from_entry`, `build_identity_from_task`, `is_enemy_identity`, `current_identity_count`, `add_runtime_claim`, `remove_runtime_claim`;
- candidate flow: `candidate_distance`, `candidate_position_distance`, `candidate_reject_reason`, `pick_control_candidate`;
- conflict resolution: `validate_current_control_claim`, `build_control_claim_snapshot`, `sort_control_claim_snapshots`, `resolve_control_conflicts`, `reconcile_control_smart`, `reconcile_smart`, `try_fill_control_smart_jobs_once`;
- runtime maintenance: `dirty_smart_names`, `process_dirty_smarts`, `rebuild_runtime_claims_from_memory`, `mark_all_known_smarts_dirty`, `reactivate_runtime`.

## 12. Story Subsystem: `zhopa.story_events`

### Responsibility
`story_events` owns a separate story FSM. This is not a generic side-effect layer; it is a concrete story mechanism.

### Current story event
The current story scenario is `North migration`.

### Public API
- `update_squad_tasks(se_squad, ctx)`

### Algorithm
1. Restore the module state blob.
2. Collect eligible squad ids.
3. Check protection and transient states.
4. Pick a safe target by level/community/terrain policy.
5. Assign or retarget the story task.
6. Clear state when the feature is disabled or the scenario ends.

### Key helper clusters
- state blob: `new_state`, `get_state_event`, `load_state_blob`, `save_state_blob`, `normalize_sid_set`, `normalize_status_map`, `set_sid_status`;
- validation: `is_story_mode_active`, `feature_enabled_now`, `migration_trigger_active`, `is_protected_squad`, `is_sid_selected`, `is_sid_locked`;
- target selection: `get_level_base_smarts`, `get_level_smarts`, `get_level_territory_smarts`, `get_level_neighbors`, `pick_nearest_safe_base_on_level`, `pick_nearest_safe_territory_on_level`, `pick_random_safe_smart_on_level`, `pick_safe_target_on_level`, `pick_north_migration_target`;
- live sync: `make_story_task`, `set_scripted_target`, `sync_story_task_live_state`, `entry_arrived_to_smart`, `consume_story_live_arrival_signal`, `is_story_arrived`;
- completion and retargeting: `maybe_finish_as_rest`, `clear_story_task_if_present`, `assign_story_task`, `retarget_story_task`, `clear_story_task_when_disabled`;
- runtime filters: `surge_active_uncached`, `is_surge_active_now`, `relation_allows_coexist`, `collect_smart_communities`, `is_story_target_safe`, `level_order_for_squad`.

## 13. Psi Watchdog: `zhopa.story_psy_watchdog`

### Responsibility
Reactive story-level modifier that converts squads on configured psi levels into zombied squads.

### Public API
- `on_game_start()`
- `reconcile_all_levels()`

### Algorithm
1. Read psi levels and immune factions from config.
2. Compare live squads against board and memory.
3. Create zombied replacements for eligible squads.
4. Rebuild squad composition and smart binding.
5. Do not use a separate scan runtime or steady-state polling.

### Key helper clusters
- parsing/config: `get_cfg_value`, `get_psi_levels`, `get_immune_factions`, `parse_csv_set`, `feature_enabled_now`;
- squad snapshot: `build_snapshot_context`, `read_commander_id`, `get_squad_member_ids`, `read_member_count`, `candidate_should_convert`;
- zombification: `pick_zombied_squad_section`, `pick_zombied_member_section`, `create_empty_squad`, `populate_zombied_squad`, `finalize_spawned_squad`, `convert_squad_to_zombied`;
- safe release/reassign: `release_squad_safe`, `assign_squad_to_smart`, `resolve_smart_object_by_id`, `resolve_smart_name_by_id`;
- scan orchestration: `try_process_squad`, `reconcile_level_once`, `reconcile_all_levels`.

## 14. Dynamic Worlds and Fillers

### 15.1 `zhopa.base_filler`
Reactive dirty-target reconcile layer for dedicated camper squads.

Public entry points:
- `on_first_update()`
- `save_state(m_data)`
- `load_state(m_data)`
- `is_base_camper_section(section)`
- `get_runtime_stats()`

Algorithm:
- index target smarts;
- choose safe base campers;
- spawn/reconcile squads only for dirty targets;
- keep spawn override local and short-lived;
- protect actor-level area from churn.

Key helper clusters:
- spawn override: `active_spawn_override_count_range`, `should_override_spawn_count`, `build_ini_sys_proxy`;
- target mapping: `refresh_sections_index`, `remember_mapping`, `clear_smart_mapping`, `pick_faction_for_smart`, `pick_camper_section`;
- reconcile: `mark_target_dirty`, `consume_dirty_targets`, `reconcile`, `run_dirty_reconcile`, `spawn_camper`, `pin_squad_to_smart`.

### 15.2 `zhopa.dynamic_bases`
Reactive owner recompute for dynamic bases.

Public entry points:
- `on_first_update()`
- `reset_runtime(reason)`
- `save_state(m_data)`
- `load_state(m_data)`
- `get_runtime_stats()`
- `get_effective_owner(smart)`

Algorithm:
- build target list;
- compute effective owner alias;
- rebuild respawn params;
- update only dirty targets;
- keep original entries separate from runtime-generated state.

### 15.3 `zhopa.service_filler`
Reactive per-smart service-role population module.

Public entry points:
- `on_first_update()`
- `reset_runtime(reason)`
- `save_state(m_data)`
- `load_state(m_data)`
- `get_runtime_stats()`
- `is_service_section(section)`
- `get_task_proxy_seed(npc)`

Algorithm:
- classify provider jobs by role;
- inspect live population and existing service squads;
- spawn missing service squads only when due;
- respect smart ownership, AP bridge, and non-service population;
- keep pending spawn state and retry cooldowns local.

Key helper clusters:
- role classification: `section_role`, `section_owner_alias`, `classify_provider_job_role`, `classify_job_role`, `role_profile`;
- spawn gating: `smart_has_non_service_population`, `skip_retry_ready`, `set_skip_retry`, `clear_skip_retry`, `ensure_warfare_ignore`;
- pending state: `pending_bucket`, `get_pending_spawn`, `set_pending_spawn`, `clear_pending_spawn`, `resolve_holder_squad`, `pin_service_squad`, `sync_pending_for_role`;
- target sync: `sync_targets_from_index`, `mark_target_dirty`, `mark_all_index_targets_dirty`, `process_smart`, `run_dirty_reconcile`.

## 16. Loot Subsystem

### 16.1 `zhopa.loot`
Event producer and lootability state manager.

Public entry points:
- `on_npc_death(victim, who)`
- `on_server_entity_register(se_obj, type_name)`
- `on_npc_item_drop(npc, item)`
- `on_actor_item_drop(item)`
- `on_game_start()`
- `is_recent_item_id(id)`
- `has_corpse_event_id(id)`
- `has_item_event_id(id)`
- `iter_corpse_event_ids()`
- `iter_item_event_ids()`
- `get_corpse_event_ids()`
- `get_item_event_ids()`
- `get_event_stats()`
- `is_protected_corpse(corpse)`
- `is_protected_corpse_id(id)`
- `sync_protected_corpse_lootability(id)`
- `mark_protected_corpse_id(id, reason)`
- `should_skip_event_scan()`

Algorithm:
- record corpse/item events;
- keep TTL-based event queues;
- temporarily remove the actor proximity limit when enabled;
- open corpses for AI loot when configured;
- do not move items directly, only improve target selection.

### 16.2 `zhopa_loot_patch`
Targeted patch layer for `xr_corpse_detection` and `eva_gather_itm`.

Public entry points:
- `apply()`
- `on_game_start()`

Algorithm:
- mix loot events into the target list;
- filter by scan cooldown and radius;
- respect quest corpse protection;
- retry apply when patching is not successful on the first attempt.

## 17. Compatibility Patches

### 17.1 `zhopa_npc_faction_override`
Overrides vanilla role checks for trader/mechanic/medic/barman on squad and member level.

Public entry points:
- `on_game_start()`
- `on_option_change()`
- `on_load_state()`
- `on_server_entity_register(...)`
- `on_server_entity_unregister(...)`
- `on_squad_npc_creation(...)`
- `on_squad_npc_death(...)`

### 17.2 `zhopa_xr_conditions_patch`
Patches role conditions and invulnerability handling for ZHOPA squads.

Public entry points:
- `Patch.apply()`

### 17.3 `zhopa_axr_task_patch`
Narrow patch layer around vanilla task helpers so ZHOPA can integrate without replacing whole systems.

Public entry points:
- `Patch.apply()`

## 18. Debug HUD
`zhopa.debug_hud` is observational only.

Public entry points:
- `on_load_state()`
- `on_save_state()`
- `on_option_change()`

Algorithm:
- build map spots from memory state;
- delete and recreate spots as needed;
- must never become the source of truth;
- must remain ownership-safe.

## 19. Config Surface and Save Contract

### 19.1 User-facing config
Current knobs include:
- global enable / logging;
- task toggles and durations;
- targeting / anti-stuck / online intent timeouts;
- mutant behavior toggles and timings;
- trade / fast trading;
- base filler settings;
- dynamic bases toggle;
- service filler settings;
- loot distances / TTL / limits / patch size;
- cache and diagnostic knobs still used by runtime.

### 19.2 Save/load owners
`zhopa.core` delegates save/load to:
- `zhopa.board_index`
- `zhopa.memory`
- `zhopa.dynamic_bases`
- `zhopa.base_filler`
- `zhopa.service_filler`
- `zhopa.debug_hud` hooks when enabled

Rule:
- only serializable data may enter save state;
- userdata, closures, engine refs, transient caches, and handles are forbidden.

## 20. Extending the System

### 20.1 Adding a new task
Define the contract first:
- type;
- target semantics;
- completion conditions;
- apply semantics;
- save-safe params.

Then implement:
1. builder;
2. assignment;
3. rotation on completion;
4. target validation;
5. cheap completion check;
6. apply path;
7. config/UI/docs if the behavior is user-facing.

### 20.2 What must not be reintroduced
- no central dispatcher;
- no whole-world scan in steady state;
- no userdata in save state;
- no hidden long-lived runtime state in anonymous global tables;
- no legacy loops under a new name.

## 21. Correctness Criteria
A change is acceptable if:
1. behavior is correct and nil-safe;
2. hot path cost is bounded;
3. save/load safety is preserved;
4. config/UI/docs stay in sync;
5. the diff stays focused on the intended subsystem.

## 22. Other Runtime Scripts

### `zhopa_fast_trading`
Immediate helper around `npc_on_item_take`.

Public entry points:
- `process_check(npc_id, data)`
- `on_npc_item_take(npc, item)`
- `on_trade_completed(squad_id, result)`
- `consume_pending_trigger(squad_id)`
- `on_game_start()`
- `get_runtime_stats()`
- `reset_cache()`

Algorithm:
- checks item-take triggers;
- waits for a short delay before re-check;
- starts quick trade only when the squad is eligible;
- applies cooldown after a trigger;
- must never become a permanent polling loop.

### `zhopa_mutants`
Separate mutant FSM, not tied to stalker roam logic.

Public entry points:
- `update_squad_tasks(se_squad, ctx)`
- `get_runtime_stats()`
- `reset_runtime(reason)`

Key functions and clusters:
- night/day detection: `is_night_now`, `is_predator_phase_inactive`;
- phase detection: `normalize_predator_phase_alias_key`, `detect_predator_phase_from_text`, `_resolve_predator_phase`;
- board/safety: `validate_live_squad_with_memory`, `resolve_entry_level`, `is_hunt_enabled`, `is_surge_active`;
- blacklists: `smart_blacklists_*`, `faction_*_blacklists_*`, `section_*_blacklists_*`;
- task flow: `make_task`, `build_rest_task`, `_build_hunt_task`, `_build_explore_task`, `_build_patrol_task`, `_pick_day_roam_task`, `_pick_first_task`, `_rotate_task`, `_is_task_target_valid`, `_is_task_completed`, `_apply_task`;
- presence model: `_ensure_hunt_presence_slot`, `_add_hunt_presence`, `_apply_hunt_presence_marks`, `_clear_hunt_presence_for_sid`, `_process_stalker_presence`, `_bootstrap_presence_from_board`;
- runtime maintenance: `_trim_filtered_smarts_cache`, `_get_filtered_smarts_for_level`, `_invalidate_hunt_level_smarts_cache`, `_refresh_presence_for_live_squad`, `_mark_mutant_dirty_if_managed`.

Algorithm:
1. Read night / surge / board context.
2. Set or update the predator phase.
3. Build a task from current phase and local presence.
4. Check arrival/completion through cheap state checks.
5. Update presence caches reactively.

### `zhopa_mcm_schema`
Schema for the MCM surface.

Public entry points:
- `get_path(key)`
- `get_option(key)`

Role:
- defines the structured `zhopa/<panel>/<key>` map;
- acts as the source of truth for the MCM UI and text keys;
- must not contain gameplay logic.

### `zhopa_heli_guard_patch`
Targeted guard for heli respawn / callback edge cases.

Key functions:
- `apply_se_heli_patch()`
- `apply_bind_heli_patch()`
- `apply_patch()`
- `master_enabled()`
- `on_game_start()`

Algorithm:
- checks heli respawn counter entries;
- clears stale references;
- patches the SE heli and bind heli code paths;
- only runs when master enabled.

### `zhopa_safe`
Nil-safe wrapper utilities.

Public entry points:
- `safe_call(tag, fn, ...)`
- `safe_id(obj)`
- `safe_name(obj)`
- `safe_section(obj)`
- `safe_position(obj)`
- `safe_level_vertex_id(obj)`
- `safe_game_vertex_id(obj)`
- `is_alive(obj)`
- `safe_community(se_obj)`
- `safe_squad_community(se_squad)`

Role:
- standardizes safe access to engine objects;
- centralizes `pcall` and fallback behavior.

### `zhopa_log`
Logger and file sink.

Public entry points:
- `set_level(lvl)`
- `get_level()`
- `set_file(filename)`
- `flush()`
- `error(module, fmt, ...)`
- `warn(module, fmt, ...)`
- `info(module, fmt, ...)`
- `debug(module, fmt, ...)`
- `trace(module, fmt, ...)`

Key helpers:
- `now_tg()`
- `level_name(lvl)`
- `truncate_file(path)`
- `Logger:_emit(...)`
- `Logger:_schedule_flush()`

### `zhopa_oop`
Public entry point:
- `zhopa.class(name)`

Role:
- minimal class helper for singleton modules.
