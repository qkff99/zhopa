# Z.H.O.P.A. ALIFE 2.0 Function Reference

[README](../README_EN.md) | [Architecture document](zhopa_alife_2_design_document_en.md) | [Russian README](../README.md)

This document is generated from the current ZHOPA ALIFE 2.0 Lua sources. It lists named function declarations and named function assignments found in runtime scripts under `gamedata/scripts` and diagnostic scripts under `debugscripts`. Anonymous inline closures, for example `pcall(function() ... end)`, are intentionally excluded because they have no standalone callable contract.

Regenerate it with:

```bash
python tools/generate_function_reference.py
```

- Runtime script functions: 1898
- Diagnostic script functions: 576
- Total documented named functions: 2474

## Reading Notes

- **Kind** describes how the function is declared: local helper, module export, script hook/global, or assigned wrapper.
- **Parameters** are copied from the declaration line and may omit internal closures or later vararg handling.
- **Description** is a short generated operational summary based on the function name and module role. The Lua source remains the final authority for exact behavior and edge cases.

## Script Index

| Scope | Script | Named functions | Role |
| --- | --- | ---: | --- |
| Runtime | `gamedata/scripts/axr_trade_manager.script` | 71 | SISKI-derived vanilla trade-manager override that executes online squad trade and technician service through real smart customer jobs. |
| Runtime | `gamedata/scripts/zhopa2_artifacts.script` | 76 | artifact target selection, real/virtual artifact handling, and online/offline pickup flow. |
| Runtime | `gamedata/scripts/zhopa2_bootstrap.script` | 19 | master enable/disable lifecycle, cleanup coordination, and startup bridge into the runtime patch orchestrator. |
| Runtime | `gamedata/scripts/zhopa2_cfg.script` | 27 | configuration, MCM defaults, faction aliases, and blacklist access. |
| Runtime | `gamedata/scripts/zhopa2_debug_hud.script` | 27 | debug PDA map markers and squad status hints. |
| Runtime | `gamedata/scripts/zhopa2_economy.script` | 291 | online customer-job preparation, offline trade execution, pricing, virtual cargo/money, queues, routing, and trade-job path recovery. |
| Runtime | `gamedata/scripts/zhopa2_index.script` | 134 | thin access layer over SIMBOARD-owned squad/smart buckets plus artifact, ownership, and trade-smart state. |
| Runtime | `gamedata/scripts/zhopa2_loot.script` | 160 | online loot integration, offline virtual loot accounting, artifact cargo, and loot-loop protection. |
| Runtime | `gamedata/scripts/zhopa2_mcm.script` | 5 | MCM menu registration and settings bridge. |
| Runtime | `gamedata/scripts/zhopa2_mcm_schema.script` | 2 | MCM option schema and defaults. |
| Runtime | `gamedata/scripts/zhopa2_memory.script` | 30 | serializable squad state, cargo, virtual loot, virtual money, and save/load helpers. |
| Runtime | `gamedata/scripts/zhopa2_perception.script` | 130 | target discovery, weighted candidate selection, path levels, and faction/blacklist checks. |
| Runtime | `gamedata/scripts/zhopa2_revenge.script` | 63 | revenge event detection, responder selection, and actor hostility scope coordinated through server ids. |
| Runtime | `gamedata/scripts/zhopa2_runtime_patches.script` | 308 | chain-friendly runtime patching of vanilla/pack scripts. |
| Runtime | `gamedata/scripts/zhopa2_service_fillers.script` | 70 | base service NPC detection, adoption, and filler spawning. |
| Runtime | `gamedata/scripts/zhopa2_smart_service_slot_doctor.script` | 104 | bounded observation and vanilla smart-job reselection for stalled trade/technician customer jobs. |
| Runtime | `gamedata/scripts/zhopa2_story_north_migration.script` | 84 | story-gated northern migration task selection and recovery. |
| Runtime | `gamedata/scripts/zhopa2_story_psy_watchdog.script` | 69 | story-gated psi-level squad conversion into zombied squads. |
| Runtime | `gamedata/scripts/zhopa2_task_scoring.script` | 47 | bounded task-target scoring, runtime level geometry, faction-presence snapshots, and configurable lore preferences. |
| Runtime | `gamedata/scripts/zhopa2_tasks.script` | 160 | task constants, task FSM, assignment, completion, fallback rules, and server-side revenge relations. |
| Runtime | `gamedata/scripts/zhopa2_topology.script` | 21 | level topology, neighbor levels, and route helpers. |
| Diagnostic | `debugscripts/zhopa2_artifact_diag.script` | 26 | artifact diag diagnostics or helpers. |
| Diagnostic | `debugscripts/zhopa2_artifact_flow_diag.script` | 64 | artifact flow diag diagnostics or helpers. |
| Diagnostic | `debugscripts/zhopa2_bucket_diag.script` | 54 | bucket diag diagnostics or helpers. |
| Diagnostic | `debugscripts/zhopa2_loot_loop_diag.script` | 52 | loot loop diag diagnostics or helpers. |
| Diagnostic | `debugscripts/zhopa2_loot_post_job_diag.script` | 39 | loot post job diag diagnostics or helpers. |
| Diagnostic | `debugscripts/zhopa2_mutant_diag.script` | 47 | mutant diag diagnostics or helpers. |
| Diagnostic | `debugscripts/zhopa2_offline_inventory_diag.script` | 29 | offline inventory diag diagnostics or helpers. |
| Diagnostic | `debugscripts/zhopa2_runtime_hud_diag.script` | 23 | runtime hud diag diagnostics or helpers. |
| Diagnostic | `debugscripts/zhopa2_trade_live_state_diag.script` | 44 | trade live state diag diagnostics or helpers. |
| Diagnostic | `debugscripts/zhopa2_trade_post_trace_diag.script` | 42 | trade post trace diag diagnostics or helpers. |
| Diagnostic | `debugscripts/zhopa2_trade_route_diag.script` | 106 | trade route diag diagnostics or helpers. |
| Diagnostic | `debugscripts/zhopa2_trade_smart_diag.script` | 50 | trade smart diag diagnostics or helpers. |

## Runtime Scripts

### `gamedata/scripts/axr_trade_manager.script`

Role: SISKI-derived vanilla trade-manager override that executes online squad trade and technician service through real smart customer jobs.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 53 | `zhopa2_economy_mod` | local helper | `` | Supports axr trade manager subsystem behavior. |
| 62 | `zhopa_surge_active` | local helper | `` | Supports axr trade manager subsystem behavior. |
| 67 | `zhopa2_service_doctor_mod` | local helper | `` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 76 | `zhopa2_cfg_mod` | local helper | `` | Reads or normalizes configuration data for the axr trade manager subsystem. |
| 85 | `axr_object_alive` | script hook/global | `obj` | Supports axr trade manager subsystem behavior. |
| 96 | `begin_item_take_suppress` | local helper | `npc, reason` | Supports axr trade manager subsystem behavior. |
| 113 | `end_item_take_suppress` | local helper | `st` | Supports axr trade manager subsystem behavior. |
| 128 | `is_trade_intent_suppressed_storage` | local helper | `st` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 139 | `is_item_take_suppressed_storage` | local helper | `st` | Supports axr trade manager subsystem behavior. |
| 148 | `is_item_take_suppressed` | local helper | `npc` | Supports axr trade manager subsystem behavior. |
| 156 | `create_item_self_suppressed` | local helper | `section, npc, reason` | Supports axr trade manager subsystem behavior. |
| 168 | `begin_members_item_take_suppress` | local helper | `members, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 179 | `end_members_item_take_suppress` | local helper | `states` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 185 | `parse_bool` | local helper | `v` | Supports axr trade manager subsystem behavior. |
| 202 | `zhopa_master_enabled` | local helper | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 247 | `read_zhopa_buy_all_from_ltx` | local helper | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 269 | `get_zhopa_buy_all_enabled` | local helper | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 310 | `pick_random_buy_candidate` | local helper | `valid_items, item_list, money, bw_ammos, buy_all_enabled, last_buy_sec, stats` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 399 | `get_smart_name_safe` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 410 | `resolve_squad_id_from_npc` | local helper | `npc` | Safely resolves an ALife/server-side object or runtime reference. |
| 424 | `publish_trade_service_event` | local helper | `npc, smart, source, phase, status, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 449 | `notify_zhopa_facade_trade_started` | local helper | `npc, smart, source` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 468 | `notify_zhopa_fast_trade_candidate` | local helper | `npc, smart, item_section, source` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 492 | `contains_token_plain` | local helper | `haystack, needle` | Supports axr trade manager subsystem behavior. |
| 498 | `read_job_ini_string_from` | local helper | `ini_obj, section, key` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 517 | `read_job_ini_string` | local helper | `job_or_section, key, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 537 | `classify_provider_job_role` | local helper | `job_or_section, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 612 | `resolve_npc_provider_role` | local helper | `npc, smart, npc_id` | Safely resolves an ALife/server-side object or runtime reference. |
| 651 | `npc_is_blocked_service_customer` | local helper | `npc, smart, npc_id` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 656 | `clear_trade_item_intent` | local helper | `st` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 666 | `clear_tech_item_intent` | local helper | `st` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 676 | `has_service_items` | local helper | `tbl` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 680 | `mark_tech_item_intent` | local helper | `st, sec` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 707 | `emit_prefixed_log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 729 | `emit_zhopa_axr_trade_log` | local helper | `level_name, fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 743 | `log_trade_info` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 747 | `log_trade_warn` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 751 | `print_debug` | assigned wrapper | `...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 757 | `log_always` | assigned wrapper | `...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 763 | `print_trade_event` | assigned wrapper | `...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 790 | `log_handler_binding_state` | local helper | `tag, force` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 806 | `clear_service_intents` | local helper | `st, npc_info, kind, reason` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 831 | `finalize_service_session` | local helper | `npc, kind, reason` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 899 | `init_settings` | script hook/global | `` | Reads or normalizes configuration data for the axr trade manager subsystem. |
| 914 | `npc_on_item_take` | local helper | `npc,item` | Supports axr trade manager subsystem behavior. |
| 928 | `on_game_start` | script hook/global | `` | Runtime hook for axr trade manager lifecycle integration. |
| 947 | `check_trade_item` | script hook/global | `npc,item` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1014 | `zhopa_npc_has_items_to_sell` | assigned wrapper | `actor,npc,p` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1060 | `zhopa_axr_trade_job_sell_items` | assigned wrapper | `actor,npc,p` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1074 | `zhopa_axr_trade_job_give_id` | assigned wrapper | `actor,npc,p` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1096 | `axr_object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 1110 | `axr_online_object_by_id` | script hook/global | `id` | Resolves an online game object through db.storage or level lookups. |
| 1130 | `axr_npc_money` | local helper | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1140 | `zhopa2_economy_active` | local helper | `economy` | Supports axr trade manager subsystem behavior. |
| 1151 | `zhopa2_managed_trade_storage` | local helper | `st` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1158 | `zhopa2_axr_trade_context` | local helper | `economy, npc, smart, st` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1210 | `zhopa2_transfer_all_money_to` | local helper | `economy, from_npc, to_npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1228 | `zhopa2_sell_member_plan` | local helper | `economy, member, seller, collect_to` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1273 | `zhopa2_execute_squad_trade` | local helper | `npc, seller, smart, st` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1332 | `ZHOPA_AXR_RUNTIME.vanilla_trade` | assigned wrapper | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1403 | `itr` | local helper | `owner, item` | Supports axr trade manager subsystem behavior. |
| 1447 | `zhopa_npc_trade_buy_sell_impl` | assigned wrapper | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1615 | `itr` | local helper | `npc,itm` | Supports axr trade manager subsystem behavior. |
| 1724 | `picked_unchecked` | local helper | `t,gr,ind` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1727 | `picked_set` | local helper | `t,gr,ind` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1732 | `check_tech_item` | script hook/global | `npc,item` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 1791 | `xr_conditions.npc_has_tech_items` | assigned wrapper | `actor,npc,p` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 1841 | `xr_effects.tech_job_upgrade_items` | assigned wrapper | `actor,npc,p` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 1848 | `xr_effects.tech_job_give_id` | assigned wrapper | `actor,npc,p` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 1865 | `npc_tech_upgrade_sell` | script hook/global | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2016 | `functor` | local helper | `t,a,b` | Supports axr trade manager subsystem behavior. |

### `gamedata/scripts/zhopa2_artifacts.script`

Role: artifact target selection, real/virtual artifact handling, and online/offline pickup flow.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 11 | `index_mod` | local helper | `` | Supports artifacts subsystem behavior. |
| 20 | `perception_mod` | local helper | `` | Supports artifacts subsystem behavior. |
| 29 | `memory_mod` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 38 | `loot_mod` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 47 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the artifacts subsystem. |
| 56 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 61 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 69 | `M.offline_enabled` | module export | `` | Supports artifacts subsystem behavior. |
| 73 | `gather_mod` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 85 | `now_ms` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 89 | `simboard_squad_object` | local helper | `id, stored` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 104 | `runtime_ready` | local helper | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 116 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 133 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 152 | `object_clsid` | local helper | `obj` | Supports artifacts subsystem behavior. |
| 163 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 172 | `object_position` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 180 | `object_is_artifact` | local helper | `obj` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 185 | `item_cost` | local helper | `obj_or_section` | Supports artifacts subsystem behavior. |
| 205 | `artifact_valid` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 223 | `artifact_same_level_as_squad` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 240 | `artifact_target_blacklisted` | local helper | `squad, smart` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 256 | `artifact_id_target_blacklisted` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 272 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 279 | `named_id` | local helper | `id` | Formats names or display text for diagnostics and UI output. |
| 292 | `bool_text` | local helper | `value` | Formats names or display text for diagnostics and UI output. |
| 296 | `artifact_bucket_debug` | local helper | `idx, smart_id, focus_id` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 329 | `artifact_pool_debug` | local helper | `idx` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 349 | `artifact_object_debug` | local helper | `idx, artifact_id` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 373 | `debug_artifact_error` | local helper | `squad, reason, artifact_id, npc, extra` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 410 | `debug_artifact_offline_success` | local helper | `squad, artifact_id, section` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 427 | `squad_has_artifact_cargo` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 432 | `squad_member_server` | local helper | `squad, prefer_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 451 | `squad_member_online_object` | local helper | `member` | Resolves an online game object through db.storage or level lookups. |
| 463 | `squad_member_alive_online` | local helper | `obj` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 471 | `add_online_looter` | local helper | `list, seen, obj` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 479 | `squad_online_looters` | local helper | `squad, prefer_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 494 | `release_artifact_reservation` | local helper | `squad, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 502 | `add_artifact_cargo` | local helper | `squad, section, value, artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 516 | `reset_online_target_tracking` | local helper | `squad` | Clears transient state, reservations, or stale runtime references. |
| 526 | `clear_online_approach_fields` | local helper | `squad` | Clears transient state, reservations, or stale runtime references. |
| 544 | `remember_artifact_reservation` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 566 | `sync_task_artifact_metadata` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 606 | `artifact_matches_task_smart` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 621 | `artifact_from_task_smart` | local helper | `squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 644 | `recover_task_artifact_id` | local helper | `squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 663 | `cancel_online_pickup` | local helper | `squad` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 673 | `recover_vanilla_artifact_pickup` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 682 | `online_inventory_recovery_pending` | local helper | `squad` | Supports artifacts subsystem behavior. |
| 705 | `clear_online_pickup_state` | local helper | `squad` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 721 | `retarget_missing_artifact_to_current_smart` | local helper | `squad, old_artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 755 | `stale_virtual_artifact_id` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 764 | `gather_item_active` | local helper | `npc, artifact_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 774 | `gather_item_failure_reason` | local helper | `npc, artifact_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 784 | `gather_item_debug_status` | local helper | `npc, artifact_id` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 794 | `pickup_stalled` | local helper | `squad, npc, now` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 842 | `online_pickup_pending` | local helper | `squad, artifact_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 874 | `online_arrived_idle_timeout` | local helper | `squad, artifact_id, reason, allow_started` | Supports artifacts subsystem behavior. |
| 908 | `current_artifact_id` | assigned wrapper | `squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 926 | `online_artifact_pickup_ready` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 944 | `all_failures_contested` | local helper | `failures` | Supports artifacts subsystem behavior. |
| 956 | `call_parent_zone_take` | local helper | `se_artifact` | Supports artifacts subsystem behavior. |
| 970 | `release_ground_artifact` | local helper | `se_artifact` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 980 | `rollback_created_artifact_cargo_item` | local helper | `se_item, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 995 | `virtual_artifact_data` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1003 | `unregister_virtual_artifact` | local helper | `artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1011 | `materialize_virtual_artifact_online` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1035 | `M.release_reservation` | module export | `squad, reason` | Clears transient state, reservations, or stale runtime references. |
| 1039 | `M.pick_target` | module export | `squad, opts` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1099 | `M.offline_collect` | module export | `squad, artifact_id, reason` | Supports artifacts subsystem behavior. |
| 1159 | `M.offline_collect_virtual` | module export | `squad, artifact_id, reason` | Supports artifacts subsystem behavior. |
| 1214 | `M.try_collect` | module export | `squad` | Supports artifacts subsystem behavior. |
| 1379 | `M.complete` | module export | `squad, reason` | Supports artifacts subsystem behavior. |
| 1390 | `M.on_game_start` | module export | `` | Runtime hook for artifacts lifecycle integration. |
| 1398 | `M.on_master_disable` | module export | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 1411 | `on_game_start` | script hook/global | `` | Runtime hook for artifacts lifecycle integration. |

### `gamedata/scripts/zhopa2_bootstrap.script`

Role: master enable/disable lifecycle, cleanup coordination, and startup bridge into the runtime patch orchestrator.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 24 | `safe_require` | local helper | `name` | Validates safety gates and controlled fallback conditions. |
| 35 | `configured_enabled` | local helper | `` | Reads or normalizes configuration data for the bootstrap subsystem. |
| 46 | `log_line` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 52 | `notify` | local helper | `text_id` | Supports bootstrap subsystem behavior. |
| 70 | `unregister_first_update` | local helper | `` | Maintains indexed runtime state by adding or removing entries. |
| 77 | `register_first_update` | local helper | `` | Maintains indexed runtime state by adding or removing entries. |
| 85 | `stop_modules` | local helper | `reason` | Supports bootstrap subsystem behavior. |
| 108 | `M.state` | module export | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 115 | `M.is_enabled` | module export | `` | Supports bootstrap subsystem behavior. |
| 120 | `M.is_disabled` | module export | `` | Supports bootstrap subsystem behavior. |
| 124 | `M.disable` | module export | `reason` | Supports bootstrap subsystem behavior. |
| 148 | `M.enable` | module export | `reason` | Supports bootstrap subsystem behavior. |
| 180 | `M._actor_on_first_update` | module export | `` | Supports bootstrap subsystem behavior. |
| 188 | `M._on_game_load` | module export | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 198 | `M._on_option_change` | module export | `` | Supports bootstrap subsystem behavior. |
| 209 | `register_lifecycle_callback` | local helper | `` | Maintains indexed runtime state by adding or removing entries. |
| 222 | `M.on_game_start` | module export | `` | Runtime hook for bootstrap lifecycle integration. |
| 240 | `on_game_start` | script hook/global | `` | Runtime hook for bootstrap lifecycle integration. |
| 244 | `_G.zhopa2_master_enabled` | assigned wrapper | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |

### `gamedata/scripts/zhopa2_cfg.script`

Role: configuration, MCM defaults, faction aliases, and blacklist access.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 87 | `section_faction` | local helper | `section` | Supports cfg subsystem behavior. |
| 95 | `squad_section_name` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 113 | `squad_faction` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 124 | `is_monster_or_zombied` | local helper | `squad` | Handles story-gated squad events, conversion, migration, or recovery. |
| 140 | `bool_from_value` | local helper | `v, default` | Supports cfg subsystem behavior. |
| 151 | `mcm_path_for_key` | local helper | `key` | Supports cfg subsystem behavior. |
| 163 | `read_mcm` | local helper | `key` | Supports cfg subsystem behavior. |
| 181 | `read_ltx` | local helper | `key, default` | Supports cfg subsystem behavior. |
| 195 | `get` | script hook/global | `key, default` | Supports cfg subsystem behavior. |
| 208 | `get_bool` | script hook/global | `key, default` | Supports cfg subsystem behavior. |
| 212 | `get_num` | script hook/global | `key, default` | Supports cfg subsystem behavior. |
| 216 | `get_string` | script hook/global | `key, default` | Supports cfg subsystem behavior. |
| 221 | `get_faction_alias` | script hook/global | `faction` | Supports cfg subsystem behavior. |
| 229 | `reset_blacklist_cache` | local helper | `` | Validates safety gates and controlled fallback conditions. |
| 234 | `cache_key` | local helper | `section, key` | Supports cfg subsystem behavior. |
| 238 | `section_value` | local helper | `section, key` | Supports cfg subsystem behavior. |
| 252 | `list_set` | local helper | `value` | Supports cfg subsystem behavior. |
| 272 | `section_set` | local helper | `section, key` | Supports cfg subsystem behavior. |
| 283 | `section_has` | local helper | `section, key, value` | Supports cfg subsystem behavior. |
| 294 | `section_is_true` | local helper | `section, key` | Supports cfg subsystem behavior. |
| 299 | `smart_name_for_blacklist` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 320 | `is_global_level_blacklisted` | script hook/global | `level_name` | Validates safety gates and controlled fallback conditions. |
| 324 | `is_level_blacklisted_for_squad` | script hook/global | `squad, level_name` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 347 | `is_smart_blacklisted_for_squad` | script hook/global | `squad, smart, level_name` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 379 | `is_trade_smart_blacklisted` | script hook/global | `smart, level_name` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 394 | `is_trade_provider_section_blacklisted` | script hook/global | `section` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 400 | `reload` | script hook/global | `` | Reads, writes, clears, or migrates serializable runtime state. |

### `gamedata/scripts/zhopa2_debug_hud.script`

Role: debug PDA map markers and squad status hints.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 24 | `enabled` | local helper | `` | Supports debug hud subsystem behavior. |
| 32 | `is_monster_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 52 | `spot_for_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 64 | `safe_squad_spot_id` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 85 | `forget_spot_owner` | local helper | `id, squad_id` | Supports debug hud subsystem behavior. |
| 102 | `remove_spot` | local helper | `id, squad_id` | Maintains indexed runtime state by adding or removing entries. |
| 116 | `cleanup_squad_id` | script hook/global | `squad_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 130 | `smart_name` | local helper | `id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 134 | `squad_debug_name` | local helper | `squad` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 145 | `perception` | local helper | `` | Supports debug hud subsystem behavior. |
| 154 | `elapsed_time` | local helper | `started` | Supports debug hud subsystem behavior. |
| 166 | `obj_level` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 174 | `format_time` | local helper | `sec` | Formats names or display text for diagnostics and UI output. |
| 182 | `pad2` | local helper | `value` | Supports debug hud subsystem behavior. |
| 195 | `route_state` | local helper | `squad` | Resolves level, graph, route, distance, or position data. |
| 212 | `task_timer` | local helper | `squad` | Calculates time, cooldown, or tick-throttling values. |
| 225 | `base_ownership` | local helper | `squad` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 239 | `base_presence` | local helper | `squad` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 250 | `story_status_line` | local helper | `squad` | Handles story-gated squad events, conversion, migration, or recovery. |
| 264 | `build_hint` | local helper | `squad` | Supports debug hud subsystem behavior. |
| 290 | `update_squad` | script hook/global | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 352 | `cleanup_squad` | script hook/global | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 365 | `cleanup_all` | script hook/global | `` | Clears transient state, reservations, or stale runtime references. |
| 372 | `actor_on_first_update` | script hook/global | `` | Runtime hook for debug hud lifecycle integration. |
| 376 | `on_game_load` | script hook/global | `` | Runtime hook for debug hud lifecycle integration. |
| 380 | `on_game_start` | script hook/global | `` | Runtime hook for debug hud lifecycle integration. |
| 395 | `on_master_disable` | local helper | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |

### `gamedata/scripts/zhopa2_economy.script`

Role: online customer-job preparation, offline trade execution, pricing, virtual cargo/money, queues, routing, and trade-job path recovery.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 58 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the economy subsystem. |
| 67 | `M.perception_mod` | module export | `` | Supports economy subsystem behavior. |
| 76 | `runtime_mod` | local helper | `` | Supports economy subsystem behavior. |
| 85 | `service_doctor_mod` | local helper | `` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 94 | `memory_mod` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 103 | `runtime_ready` | local helper | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 115 | `runtime_not_ready_reason` | local helper | `` | Supports economy subsystem behavior. |
| 127 | `surge_active` | local helper | `` | Supports economy subsystem behavior. |
| 132 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 140 | `trade_path.trade_smart_blacklisted` | assigned wrapper | `smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 155 | `trade_path.trade_provider_section_blacklisted` | assigned wrapper | `section` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 164 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 168 | `M.enabled` | module export | `` | Supports economy subsystem behavior. |
| 172 | `M.squad_trade_allowed` | module export | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 189 | `tg` | local helper | `` | Supports economy subsystem behavior. |
| 193 | `ensure_trade_ini` | local helper | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 213 | `clear_table` | local helper | `t` | Clears transient state, reservations, or stale runtime references. |
| 222 | `slower` | local helper | `value` | Supports economy subsystem behavior. |
| 226 | `contains_plain` | local helper | `haystack, needle` | Supports economy subsystem behavior. |
| 230 | `M.emit_trade_event_text` | module export | `text` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 251 | `M.queue_trade_event` | module export | `text` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 258 | `M.flush_trade_events` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 270 | `M.print_trade_event` | module export | `fmt, ...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 283 | `print_trade_error` | local helper | `fmt, ...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 294 | `print_trade_debug` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 301 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 324 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 343 | `object_clsid` | local helper | `obj` | Supports economy subsystem behavior. |
| 359 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 378 | `M.is_squad_object` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 387 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 400 | `server_object_by_id` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 408 | `live_object` | local helper | `obj` | Supports economy subsystem behavior. |
| 421 | `read_ini_string_from` | local helper | `ini, section, key` | Supports economy subsystem behavior. |
| 439 | `read_job_ini_string` | local helper | `job_or_section, key, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 462 | `find_smart_job_by_section` | local helper | `smart, section` | Resolves a safe section name for runtime classification. |
| 476 | `item_in_slots` | local helper | `npc, item_id` | Supports economy subsystem behavior. |
| 489 | `active_item` | local helper | `npc` | Supports economy subsystem behavior. |
| 502 | `best_weapon` | local helper | `npc` | Supports economy subsystem behavior. |
| 512 | `active_item_id` | local helper | `npc` | Supports economy subsystem behavior. |
| 516 | `buy_sell_params` | local helper | `section` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 568 | `sys_string` | local helper | `section, key` | Supports economy subsystem behavior. |
| 579 | `sys_float` | local helper | `section, key, default` | Supports economy subsystem behavior. |
| 590 | `is_item_type` | local helper | `typ, section, obj` | Supports economy subsystem behavior. |
| 601 | `object_is_weapon` | local helper | `item` | Supports economy subsystem behavior. |
| 609 | `object_is_outfit` | local helper | `item` | Supports economy subsystem behavior. |
| 617 | `object_is_headgear` | local helper | `item` | Supports economy subsystem behavior. |
| 625 | `item_kind` | local helper | `section` | Supports economy subsystem behavior. |
| 629 | `section_has_prefix` | local helper | `section, prefix` | Supports economy subsystem behavior. |
| 633 | `section_contains` | local helper | `section, needle` | Supports economy subsystem behavior. |
| 637 | `M.npc_sell_price_multiplier` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 647 | `item_condition` | local helper | `item` | Supports economy subsystem behavior. |
| 674 | `item_cost` | local helper | `item, section` | Supports economy subsystem behavior. |
| 690 | `section_is_ammo` | local helper | `section` | Supports economy subsystem behavior. |
| 694 | `section_is_degraded_ammo` | local helper | `section` | Supports economy subsystem behavior. |
| 698 | `section_is_clean_buckshot` | local helper | `section` | Supports economy subsystem behavior. |
| 705 | `section_is_clean_fmj` | local helper | `section` | Supports economy subsystem behavior. |
| 711 | `section_is_disfavored_fallback_ammo` | local helper | `section` | Supports economy subsystem behavior. |
| 726 | `section_is_needed_ammo` | local helper | `section, needed_ammo` | Supports economy subsystem behavior. |
| 730 | `ammo_candidate` | local helper | `section` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 737 | `pick_buy_ammo` | local helper | `weapon_ammo` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 763 | `preferred_ammo_for_weapon_section` | local helper | `weapon_section` | Resolves a safe section name for runtime classification. |
| 774 | `needed_ammo_for_npc` | local helper | `npc` | Supports economy subsystem behavior. |
| 782 | `add_weapon_ammo` | local helper | `weapon` | Maintains indexed runtime state by adding or removing entries. |
| 812 | `section_is_grenade` | local helper | `section` | Supports economy subsystem behavior. |
| 820 | `section_is_bandage` | local helper | `section` | Supports economy subsystem behavior. |
| 824 | `section_is_medkit` | local helper | `section` | Supports economy subsystem behavior. |
| 828 | `section_is_other_med` | local helper | `section` | Supports economy subsystem behavior. |
| 855 | `section_is_food` | local helper | `section` | Supports economy subsystem behavior. |
| 862 | `section_is_drink` | local helper | `section` | Supports economy subsystem behavior. |
| 872 | `section_is_never_sell` | local helper | `section, item` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 883 | `section_is_upgrade` | local helper | `section` | Supports economy subsystem behavior. |
| 887 | `section_is_artifact` | local helper | `section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 891 | `section_is_mutant_part` | local helper | `section` | Supports economy subsystem behavior. |
| 896 | `trade_smart_for_npc` | local helper | `npc, params` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 909 | `trade_seller_for_npc` | local helper | `npc, params` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 922 | `add_plan_item` | local helper | `plan, item, section, reason` | Maintains indexed runtime state by adding or removing entries. |
| 930 | `mark_surplus` | local helper | `entries, keep_count, plan, reason` | Supports economy subsystem behavior. |
| 942 | `classify_provider_job_role` | local helper | `job_or_section, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1023 | `trade_path.role_is_auto_trade_provider` | assigned wrapper | `role` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1027 | `trade_path.job_is_auto_trade_provider` | assigned wrapper | `job_or_section, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1035 | `resolve_npc_provider_role` | local helper | `npc, smart, npc_id` | Safely resolves an ALife/server-side object or runtime reference. |
| 1063 | `M.provider_role` | module export | `npc, smart` | Supports economy subsystem behavior. |
| 1067 | `npc_service_candidate_blocked` | local helper | `npc, npc_id, params` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 1092 | `npc_is_trade_provider` | local helper | `npc, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1129 | `M.build_online_sell_plan` | module export | `npc, params` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1157 | `add_generic` | local helper | `item, section, params` | Maintains indexed runtime state by adding or removing entries. |
| 1173 | `scan` | local helper | `_, item` | Supports economy subsystem behavior. |
| 1276 | `M.online_trade_sell_item_price` | module export | `npc, trader, item` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1288 | `M.online_trade_buy_item_price` | module export | `npc, trader, item` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1300 | `M.online_trade_buy_section_price` | module export | `section` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1309 | `sell_plan_should_start_auto_trade` | local helper | `npc, plan` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1326 | `inventory_section_counts` | local helper | `npc` | Supports economy subsystem behavior. |
| 1331 | `scan` | local helper | `_, item` | Supports economy subsystem behavior. |
| 1341 | `npc_money` | local helper | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1351 | `transfer_money_between` | local helper | `from_npc, to_npc, amount` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1363 | `transfer_all_money_to` | local helper | `from_npc, to_npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1371 | `M.transfer_all_money_to` | module export | `from_npc, to_npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1375 | `transfer_trade_money` | local helper | `npc, trader, price` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1383 | `spawn_trade_item_to_npc` | local helper | `npc, section` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1391 | `dynamic_news_nearby_activity_enabled` | local helper | `` | Supports economy subsystem behavior. |
| 1399 | `emit_bought_items_news` | local helper | `npc, trader, bought_items` | Supports economy subsystem behavior. |
| 1417 | `buy_missing_section` | local helper | `npc, trader, section, target_count, counts, payer, bought_items` | Resolves a safe section name for runtime classification. |
| 1444 | `ammo_buy_target` | local helper | `bs` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1452 | `M.execute_online_buy` | module export | `npc, trader, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1483 | `build_online_buy_needs` | local helper | `npc, counts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1486 | `add_need` | local helper | `section, target` | Maintains indexed runtime state by adding or removing entries. |
| 1506 | `offline_round_money` | local helper | `amount` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1511 | `virtual_money` | local helper | `squad` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 1519 | `add_virtual_money` | local helper | `squad, amount, reason` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 1536 | `take_virtual_money` | local helper | `squad, amount, reason` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 1553 | `offline_trade_item_price` | local helper | `item` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1561 | `offline_buy_section_price` | local helper | `section` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1565 | `offline_collect_members` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1592 | `offline_member_children` | local helper | `member` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1609 | `offline_collect_wallet` | local helper | `squad` | Supports economy subsystem behavior. |
| 1613 | `virtual_loot_raw_value` | local helper | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 1621 | `virtual_loot_count` | local helper | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 1629 | `virtual_loot_sell_price` | local helper | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 1633 | `virtual_loot_detail` | local helper | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 1651 | `clear_virtual_loot` | local helper | `squad, reason` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 1666 | `give_online_trade_money` | local helper | `npc, amount` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1678 | `materialize_virtual_money_to_npc` | local helper | `squad, npc, reason` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 1691 | `execute_virtual_squad_sale` | local helper | `squad, pay_to, trader, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1722 | `M.execute_online_virtual_squad_sale` | module export | `squad, pay_to, trader, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1729 | `section_is_weapon_entry` | local helper | `section, item` | Supports economy subsystem behavior. |
| 1738 | `section_is_outfit_entry` | local helper | `section, item` | Supports economy subsystem behavior. |
| 1750 | `section_is_headgear_entry` | local helper | `section, item` | Supports economy subsystem behavior. |
| 1763 | `offline_gear_score` | local helper | `item, section, ammo_counts` | Supports economy subsystem behavior. |
| 1772 | `offline_best_gear` | local helper | `member, children` | Supports economy subsystem behavior. |
| 1788 | `add_candidate` | local helper | `list, item, section` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1815 | `keep_best` | local helper | `list` | Supports economy subsystem behavior. |
| 1838 | `add_ammo` | local helper | `entry` | Maintains indexed runtime state by adding or removing entries. |
| 1849 | `offline_needed_ammo_for_gear` | local helper | `gear` | Supports economy subsystem behavior. |
| 1853 | `offline_build_sell_plan` | local helper | `members` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1869 | `add_member_plan` | local helper | `item, section, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1934 | `offline_sell_plan_should_start` | local helper | `plan` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1950 | `offline_build_buy_needs` | local helper | `members, snapshots` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1967 | `add_need` | local helper | `section, target` | Maintains indexed runtime state by adding or removing entries. |
| 1986 | `trade_path.clear_offline_trade_profile_cache` | assigned wrapper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1993 | `trade_path.cleanup_offline_trade_profile_cache` | assigned wrapper | `now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2006 | `trade_path.offline_sell_plan_value` | assigned wrapper | `plan` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2014 | `trade_path.offline_needs_value` | assigned wrapper | `needs` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2022 | `trade_path.offline_trade_profile_needs` | assigned wrapper | `profile` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2029 | `trade_path.offline_trade_profile_for_squad` | assigned wrapper | `squad, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2113 | `offline_trade_detail_list` | local helper | `entries, field, max_count` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2129 | `set_offline_trade_detail` | local helper | `squad, result, members, plan, wallet, needs` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2151 | `execute_offline_sell_plan` | local helper | `plan, squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2179 | `execute_offline_buy_needs` | local helper | `squad, members, needs` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2217 | `M.offline_squad_has_trade_work` | module export | `squad, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2232 | `M.execute_offline_squad_trade` | module export | `squad, smart, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2283 | `trade_path.clear_trade_storage` | assigned wrapper | `st` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2302 | `clear_npc_trade_state` | local helper | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2308 | `suppress_npc_trade_state` | local helper | `npc, until_tg` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2319 | `trade_path.session_ban_id` | assigned wrapper | `npc_or_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2323 | `trade_path.npc_session_banned` | assigned wrapper | `npc_or_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2328 | `trade_path.ban_npc_for_session` | assigned wrapper | `npc_or_id, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2339 | `trade_context_active` | local helper | `st` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2346 | `squad_accepts_managed_trade_signal` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2350 | `squad_for_online_npc` | local helper | `npc` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2363 | `squad_for_spawned_npc` | local helper | `npc, se_obj` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2374 | `M.materialize_online_virtual_money` | module export | `npc, squad, reason` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 2385 | `set_trade_job_idle` | local helper | `npc, params` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2396 | `finalize_online_trade_session` | local helper | `npc, smart, status, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2409 | `execute_online_sell_only` | local helper | `npc, trader, params, collect_to` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2452 | `M.execute_online_trade_with_trader` | module export | `npc, trader, params, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2456 | `M.execute_online_trade` | module export | `npc, params, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2460 | `squad_member_id_set` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2477 | `trade_result_terminal` | local helper | `result` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2486 | `clear_squad_prepared_trade_state` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2498 | `finalize_squad_trade_task` | local helper | `squad, result, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2519 | `mark_squad_trade_result` | assigned wrapper | `squad, result, reason, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2534 | `online_squad_trade_members` | local helper | `squad, smart, include_session_banned` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2552 | `online_trade_members_from_ids` | local helper | `member_ids` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2566 | `squad_trade_member_ids` | local helper | `members` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2577 | `trade_member_ids_count` | local helper | `member_ids` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2581 | `ensure_trade_source_member` | local helper | `members, source_npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2600 | `find_online_squad_trade_npc` | local helper | `squad, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2605 | `squad_members_money` | local helper | `members` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2613 | `squad_members_have_trade_work` | local helper | `members, squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2641 | `M._online_squad_members` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2659 | `M.axr_online_trade_context` | module export | `npc, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2686 | `M.has_active_prepared_trade` | module export | `npc_or_id, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2703 | `M._online_trade_profile` | module export | `members, squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2749 | `M._offline_trade_profile` | module export | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2754 | `M.squad_trade_route_profile` | module export | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2768 | `find_online_trader_at_smart` | local helper | `smart, ignore_ids` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2773 | `check_id` | local helper | `npc_id` | Supports economy subsystem behavior. |
| 2808 | `smart_trade_flags` | local helper | `smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2822 | `smart_has_indexed_trade_route` | local helper | `smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2830 | `smart_has_trade_provider_job` | local helper | `smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2866 | `job_is_trade_customer` | local helper | `job, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2879 | `smart_has_trade_customer_job` | local helper | `smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2903 | `find_trade_customer_job` | local helper | `smart, npc_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2925 | `smart_has_vanilla_trade_route` | local helper | `smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2929 | `queue_remove_squad` | local helper | `q, squad_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2942 | `queue_contains_squad` | local helper | `q, squad_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2954 | `smart_trade_queue` | local helper | `smart_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2963 | `mark_squad_queue_state` | local helper | `squad, state, smart_id, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2972 | `acquire_smart_trade_slot` | local helper | `squad, smart, reason, now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3008 | `release_smart_trade_slot` | local helper | `smart_id, squad_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3030 | `set_smart_trade_slot_remaining` | local helper | `smart_id, squad_id, count` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3037 | `set_squad_trade_cooldown` | local helper | `squad, now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3044 | `smart_by_id` | local helper | `id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 3055 | `squad_for_npc_or_id` | local helper | `npc_or_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 3074 | `prepared_trade_matches` | local helper | `squad, npc_id, smart_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3089 | `trade_path.priority_boost_key` | assigned wrapper | `smart_id, section` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3096 | `trade_path.job_priority` | assigned wrapper | `job` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3112 | `trade_path.max_stalker_job_priority` | assigned wrapper | `smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3127 | `trade_path.selected_trade_customer_section` | assigned wrapper | `smart, npc_id, npc_info` | Resolves a safe section name for runtime classification. |
| 3142 | `trade_path.select_trade_customer_job` | assigned wrapper | `smart, npc_id, npc_info, stage` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3165 | `trade_path.prepare_selected_trade_job_path` | assigned wrapper | `npc, smart, section, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3189 | `trade_path.apply_trade_priority_boost` | assigned wrapper | `smart, job, npc_info, squad, npc_id, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3232 | `trade_path.restore_trade_priority_boost` | assigned wrapper | `smart, section, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3255 | `trade_path.restore_trade_priority_boosts` | assigned wrapper | `smart_id, squad_id, npc_id, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3275 | `trade_path.prepared_trade_cancel_reason` | assigned wrapper | `squad, smart_id, npc_id, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3306 | `trade_path.npc_name` | assigned wrapper | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3316 | `trade_path.set_patrol_mode` | assigned wrapper | `npc, enabled` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3329 | `trade_path.save_point` | assigned wrapper | `npc, index, value` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3341 | `trade_path.trim` | assigned wrapper | `value` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3345 | `trade_path.has_patrol_mode` | assigned wrapper | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3353 | `trade_path.reset_beh_trade_entry` | assigned wrapper | `npc, st, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3380 | `trade_path.ini_string` | assigned wrapper | `ini, section, field` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3388 | `trade_path.parse_pos` | assigned wrapper | `line` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3400 | `trade_path.object_position` | assigned wrapper | `obj` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3410 | `trade_path.position_accessible` | assigned wrapper | `npc, pos` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3418 | `trade_path.vertex_position` | assigned wrapper | `vid` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3427 | `trade_path.vertex_accessible` | assigned wrapper | `npc, vid` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3442 | `trade_path.direct_accessible_vertex` | assigned wrapper | `npc, pos` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3459 | `trade_path.direction_accessible_vertex` | assigned wrapper | `npc, pos` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3493 | `trade_path.nearest_accessible_vertex` | assigned wrapper | `npc, pos` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3514 | `trade_path.accessible_vertex` | assigned wrapper | `npc, pos, fallback_pos` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3540 | `trade_path.line_head_tail` | assigned wrapper | `line` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3548 | `trade_path.head_tokens` | assigned wrapper | `head` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3559 | `trade_path.drop_pos_tail` | assigned wrapper | `tail` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3567 | `trade_path.rewrite_line` | assigned wrapper | `npc, line, fallback_pos, force_override` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3597 | `trade_path.prepare` | assigned wrapper | `npc, st, ini, fallback_pos, force_override` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3635 | `trade_path.acceptable_prepare_result` | assigned wrapper | `reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3639 | `trade_path.prepare_active` | assigned wrapper | `npc, smart, st, trader, force_override` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3667 | `trade_path.clear` | assigned wrapper | `npc, st` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3685 | `M.clear_prepared_trade_job` | module export | `smart, npc_id, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3709 | `trade_path.activate_selected_trade_job` | assigned wrapper | `npc, smart, npc_info, section, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3770 | `M.release_online_trade_npc_to_smart` | module export | `npc, smart, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3780 | `recover_stale_prepared_trade` | local helper | `squad, now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3849 | `M.recover_prepared_trade` | module export | `squad, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3853 | `squad_current_trade_smart` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3857 | `server_object_alive` | local helper | `obj` | Safely resolves an ALife/server-side object or runtime reference. |
| 3870 | `find_live_trader_at_smart` | local helper | `smart, ignore_ids` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3882 | `check_id` | local helper | `npc_id, job` | Supports economy subsystem behavior. |
| 3923 | `can_try_auto_trade_now` | local helper | `squad, now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3930 | `smart_for_squad_trade` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3939 | `M.squad_has_trade_smart` | module export | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3947 | `M.squad_has_trade_work` | module export | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3969 | `M._trade_route_current_level` | module export | `squad, board` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3981 | `M._trade_route_levels` | module export | `current_level, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3994 | `M._trade_route_smart_allowed` | module export | `squad, smart, level_name` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4017 | `M.collect_trade_route_smarts` | module export | `squad, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4055 | `M.pick_trade_route_smart` | module export | `squad, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4067 | `M.trade_route_task_weight` | module export | `squad, base_weight, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4089 | `mark_trade_lookup_failure` | local helper | `squad, result, reason, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4094 | `resolve_auto_trade_context` | local helper | `squad, reason, now` | Safely resolves an ALife/server-side object or runtime reference. |
| 4130 | `resolve_auto_trade_pair` | local helper | `squad, reason` | Safely resolves an ALife/server-side object or runtime reference. |
| 4150 | `M.resolve_auto_trade_pair` | module export | `squad, reason` | Safely resolves an ALife/server-side object or runtime reference. |
| 4155 | `prepare_npc_vanilla_trade` | local helper | `npc, squad, smart, trader, reason, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4201 | `prepare_online_trade_job` | local helper | `npc, squad, members, smart, trader, reason, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4261 | `prepare_squad_vanilla_trade` | local helper | `squad, members, trader, smart, reason, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4293 | `execute_offline_auto_trade` | local helper | `squad, smart, reason, now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4343 | `try_auto_trade_resolved` | local helper | `squad, reason, opts, now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4361 | `alive_online_pair` | local helper | `npc, trader` | Supports economy subsystem behavior. |
| 4380 | `resolve_explicit_pair` | local helper | `npc, trader` | Safely resolves an ALife/server-side object or runtime reference. |
| 4387 | `M.can_auto_trade_now` | module export | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4391 | `M.debug_resolve_auto_trade_pair` | module export | `squad, reason` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 4396 | `M.try_auto_trade_npc` | module export | `npc, trader, reason, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4436 | `M.try_auto_trade` | module export | `squad, reason, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4468 | `refresh_trade_items_from_inventory` | local helper | `npc, params, force` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4528 | `M.refresh_online_trade_inventory` | module export | `npc, params, force` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4532 | `suppress_online_squad_trade_members` | local helper | `squad, smart, until_tg` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4539 | `M.complete_axr_online_trade` | module export | `npc, smart, result, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4576 | `M.patch_trade_condition` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4581 | `M.patch_trade_effect` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4588 | `M.watch_recent_trade_release` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4638 | `M.actor_on_update` | module export | `` | Runtime hook for economy lifecycle integration. |
| 4642 | `npc_on_net_spawn` | local helper | `npc, se_obj` | Supports economy subsystem behavior. |
| 4647 | `on_game_load` | script hook/global | `` | Runtime hook for economy lifecycle integration. |
| 4658 | `M.materialize_online_squad_virtual_money` | module export | `` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 4671 | `actor_on_first_update` | script hook/global | `` | Runtime hook for economy lifecycle integration. |
| 4678 | `register_trade_callbacks` | local helper | `force` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4701 | `M.ensure_runtime_ready` | module export | `force_callbacks` | Checks the shared runtime readiness barrier before context-dependent work. |
| 4708 | `M.on_game_start` | module export | `` | Runtime hook for economy lifecycle integration. |
| 4719 | `M.on_master_disable` | module export | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 4764 | `on_game_start` | script hook/global | `` | Runtime hook for economy lifecycle integration. |

### `gamedata/scripts/zhopa2_index.script`

Role: thin access layer over SIMBOARD-owned squad/smart buckets plus artifact, ownership, and trade-smart state.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 69 | `M.get_revision` | module export | `` | Supports index subsystem behavior. |
| 73 | `reset_base_camping_target_smarts_cache` | local helper | `` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 79 | `mark_base_camping_registry_changed` | local helper | `` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 87 | `mark_artifact_registry_changed` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 94 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the index subsystem. |
| 103 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 111 | `M.offline_artifacts_enabled` | module export | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 115 | `smart_blacklisted_for_squad` | local helper | `squad, smart, level_name` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 127 | `tasks_mod` | local helper | `` | Supports index subsystem behavior. |
| 136 | `M.quest_protected_squad` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 145 | `surge_active` | local helper | `` | Supports index subsystem behavior. |
| 151 | `service_fillers_mod` | local helper | `` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 164 | `obj_level` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 182 | `current_level_name` | local helper | `` | Resolves level, graph, route, distance, or position data. |
| 192 | `virtual_artifact_level_allowed` | local helper | `level_name` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 197 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 211 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 230 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 239 | `object_is_artifact` | local helper | `obj` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 247 | `zone_object` | local helper | `zone` | Supports index subsystem behavior. |
| 251 | `artifact_parent_zone` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 260 | `zone_key` | local helper | `zone` | Supports index subsystem behavior. |
| 275 | `object_position` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 305 | `artifact_distance_to_sqr` | local helper | `a, b` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 317 | `artifact_is_valid` | local helper | `id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 339 | `section_exists` | local helper | `section` | Supports index subsystem behavior. |
| 343 | `section_is_artifact` | local helper | `section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 351 | `artefact_settings` | local helper | `` | Reads or normalizes configuration data for the index subsystem. |
| 364 | `name_list` | local helper | `value` | Formats names or display text for diagnostics and UI output. |
| 378 | `num_list` | local helper | `value` | Supports index subsystem behavior. |
| 392 | `artifact_sections_for_token` | local helper | `token` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 414 | `anomaly_cfg_from_spawn_ini` | local helper | `obj` | Reads or normalizes configuration data for the index subsystem. |
| 426 | `zone_level_bucket` | local helper | `level_name` | Resolves level, graph, route, distance, or position data. |
| 438 | `remove_virtual_zone_from_level` | local helper | `zkey, level_name` | Resolves level, graph, route, distance, or position data. |
| 448 | `virtual_storage_state` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 469 | `cargo_sections_append` | local helper | `existing, section` | Supports index subsystem behavior. |
| 491 | `cargo_sections_after_consume` | local helper | `existing, consumed, remaining` | Supports index subsystem behavior. |
| 515 | `persist_virtual_artifact` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 533 | `remove_persisted_virtual_artifact` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 543 | `clear_artifact_reservation_owner` | local helper | `artifact_id, squad_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 555 | `artifact_reservation_live` | local helper | `artifact_id, squad_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 583 | `artifact_reserved` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 589 | `artifact_reserved_for_other_squad` | local helper | `artifact_id, squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 601 | `smart_is_base` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 613 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 621 | `squad_cached_npc_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 632 | `is_monster_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 637 | `mutant_cycle_active` | local helper | `squad` | Supports index subsystem behavior. |
| 645 | `squad_zhopa2_manageable` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 685 | `squad_zhopa2_manageable_soft` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 713 | `squad_targets_smart_id` | local helper | `squad, smart_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 726 | `squad_base_camping_at_smart` | local helper | `squad, smart_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 736 | `object_community` | local helper | `obj` | Supports index subsystem behavior. |
| 752 | `relation_faction` | local helper | `community` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 760 | `squad_relation_faction` | local helper | `squad` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 771 | `add_count` | local helper | `counts, community, amount` | Maintains indexed runtime state by adding or removing entries. |
| 778 | `each_level` | local helper | `levels, fn` | Resolves level, graph, route, distance, or position data. |
| 804 | `limit_value` | local helper | `limit` | Supports index subsystem behavior. |
| 812 | `now_ms` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 819 | `current_frame_key` | local helper | `` | Supports index subsystem behavior. |
| 833 | `reset_frame_scratch` | script hook/global | `` | Clears transient state, reservations, or stale runtime references. |
| 838 | `levels_key` | local helper | `levels` | Resolves level, graph, route, distance, or position data. |
| 848 | `current_frame_scratch` | local helper | `` | Supports index subsystem behavior. |
| 857 | `frame_reader` | local helper | `kind, levels, limit, build_fn` | Supports index subsystem behavior. |
| 870 | `simboard` | local helper | `` | Supports index subsystem behavior. |
| 874 | `available_by_id` | local helper | `` | Supports index subsystem behavior. |
| 879 | `vanilla_smart_entry` | local helper | `board, smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 883 | `smart_available` | local helper | `board, smart, available` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 893 | `smart_kind_matches` | local helper | `smart, smart_kind` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 918 | `add_smart_from_bucket` | local helper | `out, seen, board, available, smart_id, smart, smart_kind, max_count` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 931 | `read_smart_bucket` | local helper | `levels, smart_kind, max_count` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 969 | `M.smarts_on_levels` | module export | `levels, limit, smart_kind` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 976 | `M.base_smarts_on_levels` | module export | `levels, limit` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 982 | `M.squads_on_levels` | module export | `levels, limit` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1018 | `M.squad_level_names` | module export | `` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1037 | `M.unregister_base_camping_target` | module export | `squad` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1062 | `M.register_base_camping_target` | module export | `squad, target_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1083 | `base_camping_target_has_live_squad` | local helper | `smart_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1108 | `M.base_camping_target_smarts_on_levels` | module export | `levels` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1166 | `smart_artifact_bucket_empty` | local helper | `smart_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1177 | `recalc_smart_artefact_flag` | local helper | `smart_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1208 | `remove_artifact_from_zone_bucket` | local helper | `artifact_id, zone_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1220 | `remove_artifact_from_smart_bucket` | local helper | `artifact_id, smart_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1229 | `remove_artifact_from_other_smart_buckets` | local helper | `artifact_id, keep_smart_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1243 | `add_artifact_to_bucket` | local helper | `bucket_table, key, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1258 | `restore_persisted_virtual_artifacts` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1327 | `nearest_artifact_smart` | local helper | `anchor, level_name` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1345 | `resolve_artifact_smart` | local helper | `artifact_id, artifact_obj, level_name, zone` | Safely resolves an ALife/server-side object or runtime reference. |
| 1362 | `virtual_artifact_id` | local helper | `zone_id, slot` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1368 | `virtual_artifact_zone_key` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1377 | `virtual_spawn_chance` | local helper | `` | Supports index subsystem behavior. |
| 1395 | `read_virtual_zone_entry` | local helper | `zone, cfg_file, source` | Supports index subsystem behavior. |
| 1447 | `choose_virtual_artifact_section` | local helper | `entry` | Resolves a safe section name for runtime classification. |
| 1465 | `register_virtual_artifact` | local helper | `entry, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1503 | `try_spawn_virtual_artifacts` | local helper | `entry` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1531 | `ensure_virtual_artifacts_for_levels` | local helper | `level_set` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1548 | `restore_virtual_artifact_for_squad` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1594 | `M.register_anomaly_zone` | module export | `zone, cfg_file, source` | Maintains indexed runtime state by adding or removing entries. |
| 1612 | `M.is_virtual_artifact` | module export | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1620 | `M.virtual_artifact_data` | module export | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1628 | `M.virtual_artifacts_for_zone` | module export | `zone, only_reserved` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1653 | `M.materialize_virtual_artifact` | module export | `virtual_id, real_id, zone, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1688 | `M.register_artifact` | module export | `artifact_id, zone, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1720 | `M.refresh_artifact_entity` | module export | `se_obj` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1764 | `M.unregister_artifact` | module export | `artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1791 | `M.unregister_zone_artifacts` | module export | `zone, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1807 | `M.smart_artefact_available` | module export | `smart` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1813 | `M.reserve_artifact_for_squad` | module export | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1852 | `M.release_artifact_reservation` | module export | `squad_or_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1882 | `restore_virtual_artifact_reservations_from_squads` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1908 | `repair_real_artifact_smart` | local helper | `artifact_id, level_set` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1942 | `M.available_artifact_for_smart` | module export | `smart_or_id, squad, opts` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1980 | `M.artifact_candidate_smarts_on_levels` | module export | `levels, squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2070 | `M.add_artifact_cargo` | module export | `squad, section, value, artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2090 | `M.sync_artifact_cargo` | module export | `squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2109 | `M.consume_artifact_cargo` | module export | `squad, count, value, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2137 | `M.clear_artifact_cargo` | module export | `squad, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2150 | `M.squad_has_artifact_cargo` | module export | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2172 | `M.unregister_smart` | module export | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2188 | `M.unregister_squad` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2200 | `M.base_ownership` | module export | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2204 | `M.update_base_ownership` | module export | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2295 | `distance_to_sqr` | local helper | `a, b` | Resolves level, graph, route, distance, or position data. |
| 2305 | `current_base_pull_valid` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2323 | `M.try_empty_base_pull` | module export | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2402 | `M.on_smart_update` | module export | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2414 | `server_entity_is_artifact` | local helper | `se_obj, type_name` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2425 | `server_entity_on_register` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 2439 | `server_entity_on_unregister` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 2450 | `M.on_game_load` | module export | `` | Runtime hook for index lifecycle integration. |
| 2455 | `M.actor_on_first_update` | module export | `` | Runtime hook for index lifecycle integration. |
| 2460 | `M.on_game_start` | module export | `` | Runtime hook for index lifecycle integration. |
| 2481 | `M.on_master_disable` | module export | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 2524 | `on_game_start` | script hook/global | `` | Runtime hook for index lifecycle integration. |

### `gamedata/scripts/zhopa2_loot.script`

Role: online loot integration, offline virtual loot accounting, artifact cargo, and loot-loop protection.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 27 | `load_module` | local helper | `name` | Reads, writes, clears, or migrates serializable runtime state. |
| 36 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the loot subsystem. |
| 40 | `memory_mod` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 44 | `index_mod` | local helper | `` | Supports loot subsystem behavior. |
| 48 | `complete_pickup_recovery` | local helper | `npc_or_id, request, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 52 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 60 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 68 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 72 | `now_ms` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 76 | `runtime_ready` | local helper | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 88 | `surge_active` | local helper | `` | Supports loot subsystem behavior. |
| 93 | `alife_sim` | local helper | `` | Safely resolves an ALife/server-side object or runtime reference. |
| 101 | `M.online_enabled` | module export | `` | Supports loot subsystem behavior. |
| 105 | `M.offline_enabled` | module export | `` | Supports loot subsystem behavior. |
| 109 | `M.enabled` | module export | `` | Supports loot subsystem behavior. |
| 113 | `valid_id` | local helper | `id` | Validates safety gates and controlled fallback conditions. |
| 118 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 132 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 147 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 156 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 163 | `object_level_name` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 191 | `offline_loot_level_log` | local helper | `se_victim, se_looter, attacker_squad` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 198 | `object_clsid` | local helper | `obj` | Supports loot subsystem behavior. |
| 209 | `object_section_exists` | local helper | `section` | Resolves a safe section name for runtime classification. |
| 213 | `split_colon` | local helper | `text` | Supports loot subsystem behavior. |
| 222 | `table_contains` | local helper | `t, value` | Supports loot subsystem behavior. |
| 234 | `object_alive` | local helper | `obj` | Supports loot subsystem behavior. |
| 242 | `valid_squad_object` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 250 | `item_cost` | local helper | `item` | Supports loot subsystem behavior. |
| 258 | `object_is_artifact` | local helper | `obj` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 263 | `mark_artifact_cargo_for_squad` | local helper | `squad, item, section, value, artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 287 | `ensure_death_ini` | local helper | `` | Supports loot subsystem behavior. |
| 300 | `ensure_loadout_ini` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 311 | `ini_section_exists` | local helper | `ini, section` | Supports loot subsystem behavior. |
| 315 | `ini_read_string` | local helper | `ini, section, key` | Supports loot subsystem behavior. |
| 323 | `ini_line_count` | local helper | `ini, section` | Supports loot subsystem behavior. |
| 331 | `ini_line` | local helper | `ini, section, idx` | Supports loot subsystem behavior. |
| 342 | `load_death_item_counts` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 362 | `death_section_items` | local helper | `section` | Supports loot subsystem behavior. |
| 379 | `loadout_slot_items` | local helper | `section` | Reads, writes, clears, or migrates serializable runtime state. |
| 403 | `is_monster_player_id` | local helper | `player_id` | Supports loot subsystem behavior. |
| 416 | `looter_squad` | local helper | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 428 | `squad_by_id` | local helper | `squad_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 443 | `managed_stalker_squad_for_looter` | local helper | `npc, require_loot_enabled` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 483 | `M.trade_context_active` | module export | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 493 | `M.should_manage_looter` | module export | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 500 | `section_is_quest` | local helper | `section` | Supports loot subsystem behavior. |
| 532 | `section_has_inventory_icon` | local helper | `section` | Supports loot subsystem behavior. |
| 539 | `object_is_inventory_item` | local helper | `obj` | Supports loot subsystem behavior. |
| 552 | `section_is_lootable_inventory` | local helper | `section, obj` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 568 | `object_is_story` | local helper | `obj, id` | Handles story-gated squad events, conversion, migration, or recovery. |
| 573 | `cleanup_exclusive_item_reservations` | local helper | `` | Clears transient state, reservations, or stale runtime references. |
| 586 | `exclusive_item_owner` | local helper | `item_id` | Supports loot subsystem behavior. |
| 599 | `item_reserved_for_other` | local helper | `obj, looter` | Supports loot subsystem behavior. |
| 615 | `M.can_take_section` | module export | `section, obj, looter` | Resolves a safe section name for runtime classification. |
| 637 | `is_stalker_server_object` | local helper | `obj` | Safely resolves an ALife/server-side object or runtime reference. |
| 649 | `offline_squad_can_loot` | local helper | `squad` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 666 | `member_server_object` | local helper | `member` | Safely resolves an ALife/server-side object or runtime reference. |
| 673 | `pick_offline_looter` | local helper | `squad, se_attacker` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 688 | `collect_child_ids` | local helper | `se_owner` | Supports loot subsystem behavior. |
| 702 | `owner_create_args` | local helper | `se_owner` | Supports loot subsystem behavior. |
| 709 | `set_item_condition_from_source` | local helper | `se_src, se_dst` | Supports loot subsystem behavior. |
| 724 | `create_section_to_looter` | local helper | `section, se_looter, props` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 751 | `clone_ammo_to_looter` | local helper | `section, se_item, se_looter` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 781 | `clone_weapon_to_looter` | local helper | `section, se_item, se_looter` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 785 | `clone_item_to_looter` | local helper | `section, se_item, se_looter` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 803 | `created_item_valid` | local helper | `se_new, se_looter` | Validates safety gates and controlled fallback conditions. |
| 815 | `created_item_transfer_log_entry` | local helper | `section, se_new, value, tag` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 832 | `offline_loot_item_log_entry` | local helper | `section, se_item, value` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 851 | `offline_loot_item_transfer_log_entry` | local helper | `section, se_item, se_new, value` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 860 | `section_class` | local helper | `section` | Supports loot subsystem behavior. |
| 868 | `section_is_weapon` | local helper | `section, obj` | Supports loot subsystem behavior. |
| 882 | `section_is_ammo` | local helper | `section` | Supports loot subsystem behavior. |
| 886 | `npc_squad` | local helper | `se_npc` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 894 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 905 | `split_artifact_sections` | local helper | `sections` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 913 | `consume_artifact_cargo_from_squad` | local helper | `squad, count, value, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 939 | `transfer_remaining_artifact_cargo` | local helper | `attacker_squad, victim_squad, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 963 | `squad_virtual_money` | local helper | `squad` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 971 | `transfer_remaining_virtual_money` | local helper | `attacker_squad, victim_squad, reason` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 992 | `death_community` | local helper | `se_npc` | Supports loot subsystem behavior. |
| 1007 | `death_rank` | local helper | `se_npc` | Supports loot subsystem behavior. |
| 1026 | `pick_existing_section` | local helper | `ini, preferred, fallback` | Resolves a safe section name for runtime classification. |
| 1036 | `create_generated_loot` | local helper | `section, se_looter, moved_items, tag` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1049 | `add_virtual_loot_section` | local helper | `squad, section, count, value, moved_items, tag` | Resolves a safe section name for runtime classification. |
| 1082 | `spawn_death_section` | local helper | `section, se_looter, moved_items` | Resolves a safe section name for runtime classification. |
| 1107 | `virtual_death_section` | local helper | `section, squad, moved_items` | Resolves a safe section name for runtime classification. |
| 1132 | `spawn_death_table_loot` | local helper | `se_victim, se_looter, moved_items` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1162 | `virtual_death_table_loot` | local helper | `se_victim, squad, moved_items` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1192 | `pick_loadout_entry` | local helper | `slot_section` | Reads, writes, clears, or migrates serializable runtime state. |
| 1205 | `victim_loadout_section` | local helper | `se_victim, comm, rank` | Resolves a safe section name for runtime classification. |
| 1225 | `spawn_loadout_fallback_loot` | local helper | `se_victim, se_looter, moved_items` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1257 | `virtual_loadout_fallback_loot` | local helper | `se_victim, squad, moved_items` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1289 | `offline_loot_clone_valid` | local helper | `se_new, se_looter` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1304 | `offline_loot_items_log` | local helper | `items` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 1320 | `M.offline_loot_victim` | module export | `attacker_squad, se_attacker, se_victim, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1421 | `object_is_online_inventory_owner` | local helper | `obj` | Supports loot subsystem behavior. |
| 1438 | `corpse_has_quest_item` | local helper | `corpse` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1443 | `inspect` | local helper | `owner, item` | Supports loot subsystem behavior. |
| 1455 | `M.is_protected_corpse` | module export | `corpse, corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1465 | `store_for` | local helper | `kind` | Supports loot subsystem behavior. |
| 1469 | `compact_store` | local helper | `store` | Supports loot subsystem behavior. |
| 1486 | `cleanup_store` | local helper | `kind` | Clears transient state, reservations, or stale runtime references. |
| 1505 | `trim_total_cap` | local helper | `` | Supports loot subsystem behavior. |
| 1507 | `count` | local helper | `` | Supports loot subsystem behavior. |
| 1529 | `add_event` | local helper | `kind, id` | Maintains indexed runtime state by adding or removing entries. |
| 1553 | `remove_event` | local helper | `kind, id` | Maintains indexed runtime state by adding or removing entries. |
| 1565 | `recent_ids` | local helper | `kind` | Supports loot subsystem behavior. |
| 1581 | `M.mark_corpse_ignored` | module export | `id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1604 | `M.corpse_ignored` | module export | `id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1614 | `M.recent_corpse_ids` | module export | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1618 | `M.consume_corpse_event_id` | module export | `id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1622 | `M.forget_corpse_id` | module export | `id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1627 | `M.recent_item_ids` | module export | `` | Supports loot subsystem behavior. |
| 1631 | `M.has_recent_item_events` | module export | `` | Supports loot subsystem behavior. |
| 1637 | `M.consume_item_event_id` | module export | `id` | Supports loot subsystem behavior. |
| 1641 | `M.is_recent_item_id` | module export | `id` | Supports loot subsystem behavior. |
| 1647 | `M.has_targeted_item_requests` | module export | `` | Supports loot subsystem behavior. |
| 1652 | `cleanup_targeted_item_requests` | assigned wrapper | `` | Clears transient state, reservations, or stale runtime references. |
| 1668 | `forget_targeted_item_request` | local helper | `item_id` | Supports loot subsystem behavior. |
| 1679 | `targeted_gather_prepare` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1689 | `targeted_gather_clear` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1699 | `M.reserve_item_for_npc` | module export | `npc, item_id, reason` | Supports loot subsystem behavior. |
| 1727 | `M.release_item_reservation` | module export | `item_id, npc_or_id` | Clears transient state, reservations, or stale runtime references. |
| 1745 | `M.item_reserved_for_other` | module export | `npc, item_id` | Supports loot subsystem behavior. |
| 1754 | `M.request_item_pickup` | module export | `npc, item_id, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1810 | `M.targeted_item_ids_for_npc` | module export | `npc` | Supports loot subsystem behavior. |
| 1832 | `M.cancel_item_pickup` | module export | `npc_or_id, item_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1859 | `targeted_request_for_item` | local helper | `item, keep_parented` | Supports loot subsystem behavior. |
| 1870 | `cleanup_vanilla_artifact_pickups` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1882 | `inventory_section_count` | local helper | `owner, section` | Supports loot subsystem behavior. |
| 1888 | `inspect` | local helper | `_, item` | Supports loot subsystem behavior. |
| 1903 | `inventory_item_by_section` | local helper | `owner, section, excluded_id` | Resolves a safe section name for runtime classification. |
| 1910 | `inspect` | local helper | `_, item` | Supports loot subsystem behavior. |
| 1927 | `inventory_item_by_id` | local helper | `owner, item_id` | Supports loot subsystem behavior. |
| 1934 | `inspect` | local helper | `_, item` | Supports loot subsystem behavior. |
| 1944 | `add_online_member` | local helper | `out, seen, id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1961 | `squad_online_member_objects` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1973 | `artifact_pickup_recovery_context` | local helper | `squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1986 | `M.note_vanilla_artifact_pickup` | module export | `npc, artifact_id, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2022 | `record_targeted_artifact_pickup` | local helper | `npc, item, request, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2041 | `record_task_artifact_pickup_by_section` | local helper | `npc, item, request, reason` | Resolves a safe section name for runtime classification. |
| 2072 | `record_task_artifact_pickup` | local helper | `npc, item, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2096 | `recover_task_artifact_from_squad_inventory` | local helper | `squad, artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2135 | `M.recover_pending_vanilla_artifact_pickup` | module export | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2159 | `M.corpse_detect_dist_sqr` | module export | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 2164 | `M.item_detect_dist_sqr` | module export | `` | Supports loot subsystem behavior. |
| 2169 | `M.record_loot` | module export | `npc, source, item, value, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 2201 | `M.record_offline_combat_loot` | module export | `squad, target, killed_count, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 2226 | `materialize_virtual_loot_to_npc` | local helper | `npc, reason` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 2297 | `on_npc_death` | local helper | `npc, who` | Supports loot subsystem behavior. |
| 2307 | `on_monster_death` | local helper | `obj, who` | Supports loot subsystem behavior. |
| 2316 | `on_npc_item_drop` | local helper | `npc, item` | Supports loot subsystem behavior. |
| 2325 | `on_actor_item_drop` | local helper | `item` | Supports loot subsystem behavior. |
| 2334 | `on_item_take` | local helper | `npc, item` | Supports loot subsystem behavior. |
| 2354 | `on_actor_item_take` | local helper | `item` | Supports loot subsystem behavior. |
| 2363 | `M.on_game_load` | module export | `` | Runtime hook for loot lifecycle integration. |
| 2373 | `M.on_game_start` | module export | `` | Runtime hook for loot lifecycle integration. |
| 2398 | `M.on_master_disable` | module export | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 2412 | `on_game_start` | script hook/global | `` | Runtime hook for loot lifecycle integration. |

### `gamedata/scripts/zhopa2_mcm.script`

Role: MCM menu registration and settings bridge.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 1 | `ensure_schema` | local helper | `` | Supports mcm subsystem behavior. |
| 16 | `clone_option` | local helper | `meta, key` | Supports mcm subsystem behavior. |
| 25 | `make_group` | local helper | `schema, group` | Supports mcm subsystem behavior. |
| 41 | `make_panel` | local helper | `schema, panel` | Supports mcm subsystem behavior. |
| 61 | `on_mcm_load` | script hook/global | `` | Runtime hook for mcm lifecycle integration. |

### `gamedata/scripts/zhopa2_mcm_schema.script`

Role: MCM option schema and defaults.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 101 | `get_path` | script hook/global | `key` | Supports mcm schema subsystem behavior. |
| 105 | `get_option` | script hook/global | `key` | Supports mcm schema subsystem behavior. |

### `gamedata/scripts/zhopa2_memory.script`

Role: serializable squad state, cargo, virtual loot, virtual money, and save/load helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 15 | `write_string` | local helper | `packet, value` | Supports memory subsystem behavior. |
| 19 | `read_string` | local helper | `packet` | Supports memory subsystem behavior. |
| 27 | `index_mod` | local helper | `` | Supports memory subsystem behavior. |
| 36 | `M.reset_squad` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 87 | `pack_recent` | local helper | `values` | Supports memory subsystem behavior. |
| 103 | `unpack_recent` | local helper | `value` | Supports memory subsystem behavior. |
| 118 | `M.add_recent_smart` | module export | `squad, smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 127 | `M.recent_has_smart` | module export | `squad, smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 141 | `M.add_recent_target` | module export | `squad, target_id` | Maintains indexed runtime state by adding or removing entries. |
| 150 | `M.recent_has_target` | module export | `squad, target_id` | Supports memory subsystem behavior. |
| 164 | `M.add_loot_value` | module export | `squad, value, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 175 | `unpack_virtual_loot` | local helper | `value` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 194 | `trim_artifact_cargo_sections` | local helper | `existing, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 216 | `pack_virtual_loot` | local helper | `entries` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 228 | `virtual_loot_section_count` | local helper | `entries` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 236 | `clamp_virtual_loot_state` | local helper | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 247 | `M.add_virtual_loot` | module export | `squad, section, count, value, reason` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 285 | `M.virtual_loot_entries` | module export | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 312 | `M.virtual_loot_count` | module export | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 316 | `M.virtual_loot_value` | module export | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 320 | `M.clear_virtual_loot` | module export | `squad, reason` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 331 | `M.virtual_money` | module export | `squad` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 335 | `M.add_virtual_money` | module export | `squad, amount, reason` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 348 | `M.take_virtual_money` | module export | `squad, amount, reason` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 365 | `M.add_artifact_cargo` | module export | `squad, section, value, artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 383 | `M.snapshot_task` | module export | `squad, reason` | Supports memory subsystem behavior. |
| 399 | `M.clear_resume` | module export | `squad` | Clears transient state, reservations, or stale runtime references. |
| 411 | `M.resume_task` | module export | `squad, reason` | Supports memory subsystem behavior. |
| 438 | `M.write_squad` | module export | `packet, squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 488 | `M.read_squad` | module export | `packet, squad` | Handles squad lookup, membership, task state, or squad-level accounting. |

### `gamedata/scripts/zhopa2_perception.script`

Role: target discovery, weighted candidate selection, path levels, and faction/blacklist checks.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 47 | `squad_section_name` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 65 | `section_faction` | local helper | `section` | Supports perception subsystem behavior. |
| 73 | `M.squad_player_id` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 84 | `M.squad_relation_faction` | module export | `squad` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 93 | `cfg` | local helper | `` | Supports perception subsystem behavior. |
| 103 | `now_ms` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 110 | `cleanup_runtime_hunt_cache` | local helper | `now` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 128 | `M.cleanup_base_populate_pick_cache` | module export | `now` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 141 | `current_frame_key` | local helper | `` | Supports perception subsystem behavior. |
| 155 | `current_frame_cache` | local helper | `` | Supports perception subsystem behavior. |
| 164 | `cached_frame_value` | local helper | `key, build_fn` | Supports perception subsystem behavior. |
| 178 | `cached_frame_pair` | local helper | `key, build_fn` | Supports perception subsystem behavior. |
| 189 | `obj_cache_key` | local helper | `obj` | Supports perception subsystem behavior. |
| 197 | `memory_mod` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 206 | `index_mod` | local helper | `` | Supports perception subsystem behavior. |
| 215 | `M.is_monster_squad` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 220 | `M.mutant_cycle_active` | module export | `squad` | Supports perception subsystem behavior. |
| 239 | `plain_sim_stalker_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 250 | `M.game_time` | module export | `` | Supports perception subsystem behavior. |
| 254 | `M.elapsed` | module export | `start_time` | Supports perception subsystem behavior. |
| 262 | `M.obj_level` | module export | `obj` | Resolves level, graph, route, distance, or position data. |
| 282 | `M.obj_same_level` | module export | `a, b` | Resolves level, graph, route, distance, or position data. |
| 287 | `add_level` | local helper | `set, list, level_name` | Resolves level, graph, route, distance, or position data. |
| 299 | `target_maps` | local helper | `level_name` | Supports perception subsystem behavior. |
| 317 | `target_maps_has` | local helper | `level_name, target_level` | Supports perception subsystem behavior. |
| 327 | `topology_neighbors` | local helper | `level_name` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 338 | `topology_revision` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 349 | `add_neighbor_sources` | local helper | `level_name, add_fn` | Maintains indexed runtime state by adding or removing entries. |
| 361 | `scan_reverse_edges` | local helper | `target_level, add_fn` | Validates safety gates and controlled fallback conditions. |
| 378 | `M.nearby_levels` | module export | `level_name` | Resolves level, graph, route, distance, or position data. |
| 398 | `add_direct` | local helper | `other_level` | Maintains indexed runtime state by adding or removing entries. |
| 404 | `add_nearby` | local helper | `other_level` | Maintains indexed runtime state by adding or removing entries. |
| 426 | `smart_population` | local helper | `smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 442 | `has_prey_squad` | local helper | `squad, smart` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 459 | `smart_is_base` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 477 | `base_smarts_on_level` | local helper | `level_name` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 495 | `distance_to_sqr` | local helper | `a, b` | Resolves level, graph, route, distance, or position data. |
| 512 | `target_near_base_smart` | local helper | `target, target_level` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 537 | `smart_kind_ok` | local helper | `squad, smart, kind` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 567 | `vanilla_nearby` | local helper | `squad, smart` | Supports perception subsystem behavior. |
| 576 | `level_mode_ok` | local helper | `mode, current_level, target_level, neighbors, squad, smart` | Validates safety gates and controlled fallback conditions. |
| 604 | `M.level_names_for_mode` | module export | `current_level, mode, neighbors` | Resolves level, graph, route, distance, or position data. |
| 607 | `add` | local helper | `level_name` | Maintains indexed runtime state by adding or removing entries. |
| 652 | `mode_needs_neighbors` | local helper | `mode` | Supports perception subsystem behavior. |
| 657 | `ensure_option_neighbors` | local helper | `options` | Supports perception subsystem behavior. |
| 664 | `index_squads_on_levels` | local helper | `levels` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 672 | `index_smarts_on_levels` | local helper | `levels, smart_kind` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 680 | `base_smarts_on_levels` | assigned wrapper | `levels` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 688 | `levels_for_options` | local helper | `options` | Resolves level, graph, route, distance, or position data. |
| 696 | `list_key` | local helper | `list` | Supports perception subsystem behavior. |
| 708 | `bool_key` | local helper | `value` | Supports perception subsystem behavior. |
| 712 | `smart_options_signature` | local helper | `squad, options, levels` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 733 | `hunt_options_signature` | local helper | `squad, options, levels` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 747 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 755 | `squad_member_registered_at_smart` | local helper | `smart, squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 771 | `squad_member_id_set` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 786 | `M.quest_protected_squad` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 825 | `is_online_offline_group` | local helper | `squad` | Supports perception subsystem behavior. |
| 833 | `is_zhopa2_managed_scripted_target` | local helper | `squad` | Supports perception subsystem behavior. |
| 841 | `is_common_sim_squad` | local helper | `target` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 854 | `is_blacklisted_for_hunt` | local helper | `squad, level_name, smart` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 868 | `safe_zone_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 872 | `hunt_target_profile` | local helper | `target` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 916 | `squad_targets_smart` | local helper | `other, smart` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 929 | `squad_target_smart_id` | local helper | `other` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 939 | `squad_near_smart` | local helper | `other, smart` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 957 | `factions_hostile` | local helper | `faction, target_faction` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 986 | `M.squad_relation_hostile` | module export | `squad, target` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 990 | `M.faction_relation_kind` | module export | `owner_faction, other_faction` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 1011 | `faction_relation_rank` | local helper | `faction, owner` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 1039 | `hostile_squad_at_smart` | local helper | `squad, other, smart` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1048 | `smart_has_hostile_squad` | local helper | `squad, smart` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1080 | `base_camping_squad_at_smart` | local helper | `squad, other, smart` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1090 | `base_camping_target_candidates_on_levels` | local helper | `levels, current_level` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1128 | `base_camping_populate_level_rank` | local helper | `squad, smart, options` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1144 | `base_camping_populate_candidates` | local helper | `squad, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1196 | `base_camping_target_map` | local helper | `squad, candidates` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1249 | `smart_owner_relation_rank` | local helper | `squad, smart` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 1267 | `nonexclusive_job_capacity` | local helper | `jobs` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1280 | `smart_stalker_job_capacity` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1291 | `occupied_stalker_jobs` | local helper | `smart, ignore_squad` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1296 | `ignored` | local helper | `npc_id` | Supports perception subsystem behavior. |
| 1328 | `targeted_stalker_squads_on_levels` | assigned wrapper | `levels` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1346 | `smart_incoming_stalker_npc_load` | local helper | `squad, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1353 | `add_other` | local helper | `other` | Maintains indexed runtime state by adding or removing entries. |
| 1396 | `M.smart_stalker_free_job_slots` | module export | `squad, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1411 | `base_camping_populate_score` | local helper | `squad, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1429 | `count_rest_load_squad` | local helper | `squad, other, seen` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1449 | `M.smart_rest_load` | module export | `squad, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1481 | `smart_owner_hostile_or_unstable` | local helper | `squad, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1504 | `safe_rest_smart` | local helper | `squad, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1514 | `hunt_profile_prey_ok` | local helper | `squad, profile, prey, hunter_faction` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1527 | `M.valid_hunt_target` | module export | `squad, target, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1583 | `M.valid_revenge_target` | module export | `squad, target, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1632 | `M.index_squads_for_options` | module export | `options, levels` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1638 | `hunt_candidate_pool` | local helper | `squad, options, levels` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1693 | `M.collect_hunt_targets` | module export | `squad, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1712 | `squad_distance_uncached` | local helper | `squad, target` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1734 | `squad_distance` | local helper | `squad, target` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1743 | `route_smart_ok` | local helper | `squad, smart, target_level` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1764 | `smart_from_target_id` | local helper | `target_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1775 | `target_route_smart` | local helper | `squad, target, target_level` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1800 | `actor_server_object` | local helper | `` | Safely resolves an ALife/server-side object or runtime reference. |
| 1809 | `M.actor_script_target` | module export | `squad, opts` | Supports perception subsystem behavior. |
| 1832 | `M.hunt_script_target` | module export | `squad, target, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1858 | `M.revenge_script_target` | module export | `squad, target, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1880 | `pick_hunt_target_once` | local helper | `squad, options` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1914 | `M.pick_hunt_target` | module export | `squad, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1962 | `M.valid_smart` | module export | `squad, smart, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2010 | `M.safe_rest_target_valid` | module export | `squad, target_id` | Validates safety gates and controlled fallback conditions. |
| 2024 | `M.index_smarts_for_options` | module export | `options, levels` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2030 | `valid_smart_cached` | local helper | `squad, smart, options, signature` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2040 | `M.collect_smarts` | module export | `squad, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2082 | `pick_smart_from_options` | local helper | `squad, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2104 | `M.pick_smart` | module export | `squad, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2108 | `artifact_clone_opts` | local helper | `src` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2116 | `M.collect_artifact_targets` | module export | `squad, opts` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2151 | `M.pick_artifact_target` | module export | `squad, opts` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2177 | `M.pick_closest_smart` | module export | `squad, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2192 | `M.pick_balanced_rest_smart` | module export | `squad, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2213 | `M.pick_base_camping_populate_smart` | module export | `squad, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2263 | `M.base_camping_populate_target_valid` | module export | `squad, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2282 | `M.pick_final_prior_smart` | module export | `squad, smart_or_list, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2309 | `clone_opts` | local helper | `src` | Supports perception subsystem behavior. |
| 2317 | `M.pick_weighted_smart` | module export | `squad, opts, fallback_opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2338 | `M.pack_ids` | module export | `list` | Supports perception subsystem behavior. |
| 2346 | `M.unpack_ids` | module export | `value` | Supports perception subsystem behavior. |
| 2362 | `M.is_night` | module export | `` | Supports perception subsystem behavior. |
| 2367 | `M.make_patrol` | module export | `squad, kind, opts` | Supports perception subsystem behavior. |
| 2394 | `M.on_master_disable` | module export | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |

### `gamedata/scripts/zhopa2_revenge.script`

Role: revenge event detection, responder selection, and actor hostility scope coordinated through server ids.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 8 | `load_module` | local helper | `name` | Reads, writes, clears, or migrates serializable runtime state. |
| 17 | `perception_mod` | local helper | `` | Supports revenge subsystem behavior. |
| 21 | `index_mod` | local helper | `` | Supports revenge subsystem behavior. |
| 25 | `tasks_mod` | local helper | `` | Supports revenge subsystem behavior. |
| 29 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the revenge subsystem. |
| 33 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 41 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 49 | `hour_is_night` | local helper | `hour` | Supports revenge subsystem behavior. |
| 54 | `current_hour` | local helper | `` | Supports revenge subsystem behavior. |
| 58 | `runtime_ready` | local helper | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 70 | `is_night_now` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 78 | `revenge_disabled_for_night` | local helper | `` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 82 | `sleep_touches_night` | local helper | `hours, start_hour` | Supports revenge subsystem behavior. |
| 103 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 136 | `master_enabled` | local helper | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 148 | `death_key` | local helper | `victim_squad, offender_target_id` | Supports revenge subsystem behavior. |
| 155 | `mark_death_processed` | local helper | `victim_squad, offender_target_id` | Supports revenge subsystem behavior. |
| 174 | `death_processed` | local helper | `victim_squad, offender_target_id` | Supports revenge subsystem behavior. |
| 179 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 187 | `squad_member_count_soft` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 195 | `squad_commander_id` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 206 | `obj_level` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 231 | `squad_section_name` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 247 | `service_squad_soft` | local helper | `squad` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 258 | `scripted_target_manageable_soft` | local helper | `squad` | Supports revenge subsystem behavior. |
| 269 | `global_level_blacklisted_soft` | local helper | `squad` | Validates safety gates and controlled fallback conditions. |
| 283 | `responder_manageable_soft` | local helper | `squad` | Supports revenge subsystem behavior. |
| 315 | `position_distance` | local helper | `a, b` | Resolves level, graph, route, distance, or position data. |
| 335 | `graph_distance` | local helper | `a, b` | Resolves level, graph, route, distance, or position data. |
| 345 | `squad_distance` | local helper | `victim_squad, responder` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 349 | `actor_killer` | local helper | `se_killer` | Supports revenge subsystem behavior. |
| 357 | `squad_from_member` | local helper | `se_obj` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 385 | `killer_squad_and_target` | local helper | `se_killer` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 393 | `responder_ok` | local helper | `candidate, victim_squad, offender_squad` | Validates safety gates and controlled fallback conditions. |
| 415 | `level_pool` | local helper | `victim_squad` | Resolves level, graph, route, distance, or position data. |
| 430 | `consider_candidate` | local helper | `victim_squad, offender_squad, candidate, best, best_dist` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 449 | `scan_vanilla_squads` | local helper | `levels, victim_squad, offender_squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 466 | `find_responder` | local helper | `victim_squad, offender_squad` | Supports revenge subsystem behavior. |
| 472 | `actor_revenge_roll_passed` | local helper | `` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 483 | `actor_revenge_squad_active` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 491 | `rebuild_active_actor_revenge_squad_id` | local helper | `` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 506 | `active_actor_revenge_exists` | local helper | `` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 515 | `current_actor_level` | local helper | `` | Resolves level, graph, route, distance, or position data. |
| 525 | `each_revenge_squad` | local helper | `actor_only, fn` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 530 | `visit_squad_id` | local helper | `squad_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 551 | `M.cancel_active_revenge` | module export | `reason, actor_only` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 573 | `actor_revenge_squad_id_for_sleep` | local helper | `` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 583 | `pause_actor_revenge_for_sleep` | local helper | `hours` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 600 | `restore_paused_actor_revenge_after_sleep` | local helper | `` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 619 | `M.apply_online_revenge_hostility` | module export | `` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 647 | `consider_squad_id` | local helper | `squad_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 670 | `sleep_hours_from_ui` | local helper | `ui` | Supports revenge subsystem behavior. |
| 681 | `install_sleep_hook` | local helper | `` | Supports revenge subsystem behavior. |
| 707 | `wrapper` | local helper | `self, ...` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 724 | `uninstall_sleep_hook` | local helper | `` | Supports revenge subsystem behavior. |
| 737 | `actor_on_sleep` | local helper | `hours` | Supports revenge subsystem behavior. |
| 751 | `actor_on_update` | script hook/global | `` | Runtime hook for revenge lifecycle integration. |
| 766 | `M.assign_revenge` | module export | `responder, offender_target_id, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 793 | `M.on_squad_npc_death` | module export | `victim_squad, se_npc, se_killer` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 855 | `M.on_npc_death_callback` | module export | `victim, who` | Supports revenge subsystem behavior. |
| 866 | `M.on_game_start` | module export | `` | Runtime hook for revenge lifecycle integration. |
| 886 | `M.on_master_disable` | module export | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 905 | `on_game_start` | script hook/global | `` | Runtime hook for revenge lifecycle integration. |

### `gamedata/scripts/zhopa2_runtime_patches.script`

Role: chain-friendly runtime patching of vanilla/pack scripts.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 54 | `safe_require` | local helper | `name` | Validates safety gates and controlled fallback conditions. |
| 65 | `M.task_scoring` | module export | `` | Supports runtime patches subsystem behavior. |
| 69 | `M.notify_task_scoring` | module export | `event, ...` | Supports runtime patches subsystem behavior. |
| 76 | `M.master_enabled` | module export | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 90 | `class_candidate` | local helper | `candidate, required_method` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 104 | `script_class` | local helper | `script_name, class_name, required_method` | Supports runtime patches subsystem behavior. |
| 140 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 158 | `server_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 179 | `simboard_squad_object` | local helper | `id, stored` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 187 | `M.zhopa2_online_object_by_id` | module export | `id` | Resolves an online game object through db.storage or level lookups. |
| 203 | `runtime_object_alive` | local helper | `obj` | Supports runtime patches subsystem behavior. |
| 211 | `runtime_object_dead` | local helper | `obj` | Supports runtime patches subsystem behavior. |
| 219 | `M.zhopa2_first_squad_member_id` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 235 | `M.zhopa2_first_online_squad_member` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 240 | `M.zhopa2_object_location` | module export | `obj` | Supports runtime patches subsystem behavior. |
| 277 | `M.zhopa2_direct_hunt_target_anchor` | module export | `target` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 289 | `direct_hunt_target_signature` | local helper | `target` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 308 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 316 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 324 | `object_level_name` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 339 | `global_level_blacklisted` | local helper | `level_name` | Validates safety gates and controlled fallback conditions. |
| 349 | `zhopa2_debug_printf` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 355 | `zhopa2_valid_script_target_id` | local helper | `target_id` | Validates safety gates and controlled fallback conditions. |
| 376 | `runtime_time_ms` | local helper | `` | Supports runtime patches subsystem behavior. |
| 380 | `runtime_log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 390 | `runtime_item_key` | local helper | `stage, item` | Supports runtime patches subsystem behavior. |
| 394 | `mark_runtime_item` | local helper | `stage, item, ok, reason, detail` | Supports runtime patches subsystem behavior. |
| 414 | `runtime_item_ready` | local helper | `stage, item` | Supports runtime patches subsystem behavior. |
| 418 | `runtime_error_enabled` | local helper | `` | Supports runtime patches subsystem behavior. |
| 422 | `runtime_mark_context` | local helper | `` | Formats names or display text for diagnostics and UI output. |
| 445 | `runtime_missing_item` | local helper | `` | Supports runtime patches subsystem behavior. |
| 466 | `required_script_class` | local helper | `script_name, class_name, surface, required_method` | Supports runtime patches subsystem behavior. |
| 477 | `start_zhopa_module` | local helper | `name` | Supports runtime patches subsystem behavior. |
| 508 | `M.ensure_zhopa_modules` | module export | `` | Supports runtime patches subsystem behavior. |
| 519 | `upvalue` | local helper | `fn, name` | Supports runtime patches subsystem behavior. |
| 535 | `set_upvalue` | local helper | `fn, name, value` | Supports runtime patches subsystem behavior. |
| 552 | `M.function_chain_contains` | module export | `fn, target, depth, seen` | Supports runtime patches subsystem behavior. |
| 578 | `M.patch_method` | module export | `owner, method, patch_id, wrapper_factory` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 613 | `wrapper` | local helper | `...` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 627 | `install_class_method` | local helper | `cls, name, fn` | Supports runtime patches subsystem behavior. |
| 651 | `M.restore_runtime_patches` | module export | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 692 | `patch_required_method` | local helper | `owner, method, patch_id, wrapper_factory, surface` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 717 | `game_time` | local helper | `` | Supports runtime patches subsystem behavior. |
| 721 | `elapsed` | local helper | `start_time` | Supports runtime patches subsystem behavior. |
| 729 | `perception` | local helper | `` | Supports runtime patches subsystem behavior. |
| 733 | `memory` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 737 | `tasks` | local helper | `` | Supports runtime patches subsystem behavior. |
| 741 | `zhopa2_surge_active` | local helper | `` | Supports runtime patches subsystem behavior. |
| 746 | `index` | local helper | `` | Supports runtime patches subsystem behavior. |
| 750 | `cache_squad_section_name` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 768 | `object_debug_name` | local helper | `obj` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 787 | `cache_squad_member_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 803 | `squad_player_id` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 824 | `is_monster_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 844 | `plain_sim_stalker_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 858 | `service_squad` | local helper | `squad` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 869 | `managed_stalker_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 876 | `task_invalid_for_monster` | local helper | `squad, task` | Validates safety gates and controlled fallback conditions. |
| 884 | `is_night` | local helper | `` | Supports runtime patches subsystem behavior. |
| 889 | `write_string` | local helper | `packet, value` | Supports runtime patches subsystem behavior. |
| 893 | `read_string` | local helper | `packet` | Supports runtime patches subsystem behavior. |
| 901 | `unpack_ids` | local helper | `value` | Supports runtime patches subsystem behavior. |
| 918 | `squad_methods.zhopa2_cleanup_debug` | assigned wrapper | `self` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 925 | `squad_methods.zhopa2_release_task_rush` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 932 | `squad_methods.zhopa2_release_revenge_hostility` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 939 | `squad_methods.zhopa2_unregister_base_camping_registry` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 946 | `squad_methods.zhopa2_sync_base_camping_registry` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 960 | `squad_methods.zhopa2_is_managed_scripted_target` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 964 | `squad_methods.zhopa2_reset_state` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 993 | `squad_methods.zhopa2_task_requires_rush` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 999 | `squad_methods.zhopa2_sync_task_rush` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1017 | `squad_methods.zhopa2_clear_task` | assigned wrapper | `self, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1066 | `squad_methods.zhopa2_reconcile_mutant_cycle` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1115 | `squad_methods.zhopa2_sanitize_task_owner` | assigned wrapper | `self, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1123 | `squad_methods.zhopa2_global_level_blacklisted` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1128 | `squad_methods.zhopa2_purge_global_level_blacklist` | assigned wrapper | `self, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1146 | `squad_methods.zhopa2_can_manage` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1198 | `squad_methods.zhopa2_assign_task` | assigned wrapper | `self, task, target_id, duration_sec, reason, patrol` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1256 | `squad_methods.zhopa2_assign_rest` | assigned wrapper | `self, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1261 | `squad_methods.zhopa2_reached_target` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1268 | `squad_methods.zhopa2_patrol_next` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1286 | `squad_methods.zhopa2_task_completed` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1326 | `squad_methods.zhopa2_target_is_alive` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1353 | `squad_methods.zhopa2_update_task` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1374 | `squad_methods.zhopa2_get_script_target` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1421 | `squad_methods.zhopa2_prepare_hunt_target` | assigned wrapper | `self, script_target_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1457 | `squad_methods.zhopa2_apply_revenge_hostility` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1465 | `squad_methods.zhopa2_state_write` | assigned wrapper | `self, packet` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1481 | `squad_methods.zhopa2_state_read` | assigned wrapper | `self, packet` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1514 | `squad_methods.zhopa2_debug_offline_inventory_update_dump` | assigned wrapper | `self` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 1518 | `install_squad_methods` | local helper | `cls` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1524 | `wrapped_returns` | local helper | `original, self, ...` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 1529 | `retrofit_existing_squads` | local helper | `` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1549 | `M.patch_sim_squad_scripted` | module export | `` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1710 | `M.patch_axr_companions` | module export | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 1717 | `squad_from_npc` | local helper | `npc` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1725 | `online_npc_id` | local helper | `npc` | Supports runtime patches subsystem behavior. |
| 1730 | `vanilla_guide_complete` | local helper | `npc` | Supports runtime patches subsystem behavior. |
| 1753 | `pda_guide_complete` | local helper | `npc` | Supports runtime patches subsystem behavior. |
| 1775 | `mark_post_guide_rest` | local helper | `npc, reason, target_id` | Supports runtime patches subsystem behavior. |
| 1796 | `maybe_mark` | local helper | `npc` | Supports runtime patches subsystem behavior. |
| 1821 | `obj_level` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 1836 | `prop_value` | local helper | `props, key` | Supports runtime patches subsystem behavior. |
| 1840 | `smart_is_base` | local helper | `smart, props` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1852 | `smart_kind_flags` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1878 | `level_bucket` | local helper | `root, level_name` | Resolves level, graph, route, distance, or position data. |
| 1886 | `kind_bucket` | local helper | `root, level_name, kind` | Supports runtime patches subsystem behavior. |
| 1895 | `trim` | local helper | `value` | Supports runtime patches subsystem behavior. |
| 1902 | `lower` | local helper | `value` | Supports runtime patches subsystem behavior. |
| 1906 | `contains` | local helper | `haystack, needle` | Supports runtime patches subsystem behavior. |
| 1910 | `ini_string` | local helper | `ini, section, key` | Supports runtime patches subsystem behavior. |
| 1924 | `ini_section_exists` | local helper | `ini, section` | Supports runtime patches subsystem behavior. |
| 1932 | `open_ini` | local helper | `path` | Supports runtime patches subsystem behavior. |
| 1941 | `smart_cfg_filename` | local helper | `smart` | Reads or normalizes configuration data for the runtime patches subsystem. |
| 1961 | `smart_ini` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1970 | `beh_ini` | local helper | `` | Supports runtime patches subsystem behavior. |
| 1978 | `read_job_string` | local helper | `job_or_section, key, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1991 | `M.trade_provider_section_blacklisted` | module export | `section` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2000 | `M.trade_smart_blacklisted` | module export | `smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2009 | `trade_job_flags` | local helper | `job, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2039 | `merge_trade_flags` | local helper | `flags, job_flags` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2050 | `scan_loaded_trade_jobs` | local helper | `smart, flags` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2060 | `scan_exclusive_trade_job` | local helper | `smart, flags, work_field, work_path` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2071 | `scan_smart_ini_trade_jobs` | local helper | `smart, flags` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2099 | `scan_beh_trade_jobs` | local helper | `smart, flags` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2117 | `remove_smart_from_level_buckets` | local helper | `board, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2144 | `board_methods.zhopa2_ensure_buckets` | assigned wrapper | `self` | Supports runtime patches subsystem behavior. |
| 2160 | `board_methods.zhopa2_register_trade_smart` | assigned wrapper | `self, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2205 | `board_methods.zhopa2_unregister_trade_smart` | assigned wrapper | `self, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2220 | `board_methods.zhopa2_register_smart` | assigned wrapper | `self, obj` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2248 | `board_methods.zhopa2_unregister_smart` | assigned wrapper | `self, obj` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2268 | `board_methods.zhopa2_update_squad_level` | assigned wrapper | `self, squad, level_name` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2310 | `board_methods.zhopa2_unregister_squad` | assigned wrapper | `self, squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2324 | `board_methods.zhopa2_rebuild_buckets` | assigned wrapper | `self` | Supports runtime patches subsystem behavior. |
| 2354 | `install_board_methods` | local helper | `cls` | Supports runtime patches subsystem behavior. |
| 2360 | `M.patch_sim_board` | module export | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 2435 | `service_fillers` | local helper | `` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 2439 | `service_job_fallback` | local helper | `npc_info, job, smart` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 2450 | `debug_service_job` | local helper | `smart, npc_info, job, source` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 2495 | `M.npc_storage_from_info` | module export | `npc_info` | Supports runtime patches subsystem behavior. |
| 2500 | `M.has_targeted_gather_state` | module export | `npc_info` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 2507 | `live_targeted_gather_id` | local helper | `npc_info` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 2534 | `targeted_gather_blocks_job` | local helper | `smart, npc_info` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 2550 | `M.safe_section_name` | module export | `obj` | Resolves a safe section name for runtime classification. |
| 2561 | `M.service_job_check_relevant` | module export | `npc_info` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 2574 | `try_service_fallback_job` | local helper | `smart, npc_info` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 2620 | `ensure_service_job` | local helper | `smart, npc_info` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 2645 | `refresh_job_capacity` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2678 | `M.patch_smart_terrain` | module export | `` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2727 | `artifact_index` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2731 | `register_artifact` | local helper | `artifact_id, zone, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2738 | `unregister_artifact` | local helper | `artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2745 | `unregister_zone_artifacts` | local helper | `zone, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2752 | `register_anomaly_zone` | local helper | `zone, cfg_file, source` | Maintains indexed runtime state by adding or removing entries. |
| 2759 | `virtual_artifacts_for_zone` | local helper | `zone` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2768 | `materialize_virtual_artifact` | local helper | `virtual_id, real_id, zone, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2775 | `zone_key` | local helper | `zone` | Supports runtime patches subsystem behavior. |
| 2781 | `M.zhopa2_sync_existing_anomaly_zones` | module export | `source` | Supports runtime patches subsystem behavior. |
| 2816 | `zhopa2_materialize_virtual_artifact_online` | script hook/global | `virtual_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2835 | `anomaly_spawn_artefact_section` | local helper | `self, section` | Resolves a safe section name for runtime classification. |
| 2858 | `anomaly_materialize_virtual_artifacts` | local helper | `self` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2873 | `M.patch_bind_anomaly_zone` | module export | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 2965 | `M.zhopa2_direct_hunt_live_location` | module export | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2989 | `M.zhopa2_direct_hunt_commander_execute` | module export | `self, squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 3024 | `M.patch_xr_reach_task` | module export | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 3042 | `task_run` | local helper | `squad` | Supports runtime patches subsystem behavior. |
| 3050 | `direct_monster_update` | local helper | `self` | Supports runtime patches subsystem behavior. |
| 3119 | `M.patch_bind_monster` | module export | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 3136 | `offline_loot_attacker_squad` | local helper | `killer` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3151 | `ignore_offline_loot_detail` | local helper | `detail` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3162 | `offline_loot_on_death` | local helper | `victim, killer` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3203 | `patch_death_class` | local helper | `cls, patch_name` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 3215 | `M.patch_sim_offline_combat` | module export | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 3238 | `gather_mod` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3242 | `corpse_mod` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3246 | `module_member` | local helper | `mod, name` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 3250 | `export_script_function` | local helper | `mod, name, fn` | Supports runtime patches subsystem behavior. |
| 3280 | `gather_original_func` | local helper | `mod, name` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3296 | `gather_upvalue` | local helper | `name` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3302 | `set_gather_upvalue` | local helper | `name, value` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3308 | `gather_items_table` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3317 | `zhopa2_loot_mod` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3321 | `M.zhopa2_has_recent_item_events` | module export | `` | Supports runtime patches subsystem behavior. |
| 3326 | `M.zhopa2_has_targeted_item_requests` | module export | `` | Supports runtime patches subsystem behavior. |
| 3331 | `zhopa2_loot_active` | local helper | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3336 | `zhopa2_loot_globally_enabled` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3341 | `M.zhopa2_sync_gather_runtime_state` | module export | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3404 | `zhopa2_can_take_section` | local helper | `npc, item, section` | Resolves a safe section name for runtime classification. |
| 3412 | `zhopa2_event_item_ids` | local helper | `` | Supports runtime patches subsystem behavior. |
| 3420 | `zhopa2_consume_item_event_id` | local helper | `item_id` | Supports runtime patches subsystem behavior. |
| 3427 | `zhopa2_targeted_item_ids` | local helper | `npc` | Supports runtime patches subsystem behavior. |
| 3435 | `zhopa2_item_targeted_for_npc` | local helper | `npc, item_id, ids` | Supports runtime patches subsystem behavior. |
| 3457 | `zhopa2_item_reserved_for_other` | local helper | `npc, item_id` | Supports runtime patches subsystem behavior. |
| 3465 | `zhopa2_item_clsid` | local helper | `item` | Supports runtime patches subsystem behavior. |
| 3473 | `zhopa2_item_detect_dist_sqr` | local helper | `` | Supports runtime patches subsystem behavior. |
| 3481 | `zhopa2_record_loot` | local helper | `npc, item, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3489 | `M.zhopa2_note_vanilla_artifact_pickup` | module export | `npc, artifact_id, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3498 | `zhopa2_should_skip_overweight` | local helper | `npc` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 3502 | `zhopa2_should_skip_condlist` | local helper | `npc` | Supports runtime patches subsystem behavior. |
| 3506 | `zhopa2_item_reserved_by` | local helper | `item_id` | Supports runtime patches subsystem behavior. |
| 3512 | `zhopa2_reservation_is_live` | local helper | `owner_id, item_id` | Supports runtime patches subsystem behavior. |
| 3529 | `zhopa2_clear_artifact_scan` | local helper | `st` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3539 | `zhopa2_reset_artifact_approach` | local helper | `st` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3557 | `zhopa2_mark_approach_failed` | local helper | `st, item_id, reason` | Supports runtime patches subsystem behavior. |
| 3565 | `zhopa2_clear_approach_failure` | local helper | `st, item_id` | Clears transient state, reservations, or stale runtime references. |
| 3576 | `zhopa2_object_vertex` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 3593 | `zhopa2_valid_accessible_vertex` | local helper | `npc, vid` | Validates safety gates and controlled fallback conditions. |
| 3607 | `zhopa2_nearest_accessible_vertex` | local helper | `npc, pos` | Resolves level, graph, route, distance, or position data. |
| 3629 | `zhopa2_vertex_in_direction` | local helper | `npc, from_vid, dir, dist` | Resolves level, graph, route, distance, or position data. |
| 3642 | `zhopa2_select_artifact_approach` | local helper | `npc, item, item_pos, start_index, bad_vids` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3680 | `zhopa2_safe_look_position` | local helper | `npc, pos` | Validates safety gates and controlled fallback conditions. |
| 3691 | `zhopa2_artifact_approach_reached` | local helper | `npc, st` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3698 | `zhopa2_artifact_pickup_ready` | local helper | `npc, st` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3706 | `M.zhopa2_artifact_vanilla_pickup_reachable` | module export | `npc, st, item` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3727 | `zhopa2_artifact_approach_progress_ok` | local helper | `npc, st` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3750 | `M.zhopa2_gather_stalled` | module export | `npc, st, item_id, target_pos` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3792 | `zhopa2_prepare_next_artifact_approach` | local helper | `npc, st, item, item_pos, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3815 | `zhopa2_send_to_artifact_vertex` | local helper | `npc, st, invalid_reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3833 | `zhopa2_evaluator_camper_end_for_gather:__init` | assigned wrapper | `name` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3835 | `zhopa2_evaluator_camper_end_for_gather:evaluate` | assigned wrapper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3856 | `zhopa2_apply_camper_end_override` | local helper | `manager` | Supports runtime patches subsystem behavior. |
| 3870 | `zhopa2_add_gather_precondition` | local helper | `manager, action_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3887 | `zhopa2_job_action_key` | local helper | `root` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 3898 | `zhopa2_suspend_active_scheme_for_targeted_gather` | local helper | `npc, st` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3922 | `zhopa2_restore_active_scheme_after_targeted_gather` | local helper | `npc, st` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3940 | `zhopa2_apply_job_preconditions` | local helper | `npc, st` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 3984 | `zhopa2_start_artifact_scan` | local helper | `npc, st, item, now` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3995 | `zhopa2_update_artifact_scan` | local helper | `npc, st, item, now` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 4016 | `zhopa2_begin_artifact_pickup` | local helper | `npc, st, item, now, force` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 4028 | `M.zhopa2_try_artifact_force_pickup` | module export | `npc, st, item, now, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 4044 | `zhopa2_reset_gather_state` | local helper | `st` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4075 | `M.zhopa2_mark_ground_gather_release` | module export | `npc, item_id, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4091 | `M.zhopa2_peek_ground_gather_release` | module export | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4100 | `M.zhopa2_ground_gather_settling` | module export | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4113 | `M.zhopa2_take_ground_gather_release` | module export | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4124 | `M.zhopa2_ground_gather_release_ready` | module export | `npc, st, entry` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4144 | `M.zhopa2_watch_ground_gather_release` | module export | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4172 | `M.zhopa2_smart_for_online_npc` | module export | `npc` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 4193 | `M.zhopa2_clear_pickup_state` | module export | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4211 | `M.zhopa2_refresh_meet_after_pickup` | module export | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4243 | `M.zhopa2_mark_ground_gather_meet_refresh` | module export | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4259 | `M.zhopa2_watch_ground_gather_meet_refresh` | module export | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4287 | `M.zhopa2_release_ground_gather_npc` | module export | `npc, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4304 | `zhopa2_item_reservation_owner_impl` | local helper | `item_id` | Supports runtime patches subsystem behavior. |
| 4314 | `zhopa2_prepare_targeted_gather_impl` | local helper | `npc, item_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4328 | `zhopa2_force_gather_item` | script hook/global | `npc, item_id, targeted` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4412 | `zhopa2_clear_gather_item` | script hook/global | `npc, item_id, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4433 | `M.zhopa2_trade_context_active` | module export | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4443 | `M.zhopa2_trade_gather_blocked` | module export | `npc, st` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4461 | `M.patch_state_mgr_trade_run` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4465 | `M.zhopa2_try_force_online_gather_item` | module export | `npc, st` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4487 | `consider` | local helper | `item_id` | Supports runtime patches subsystem behavior. |
| 4534 | `M.zhopa2_gather_item_active` | module export | `npc, item_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4562 | `zhopa2_gather_item_failure_reason_impl` | local helper | `npc, item_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4573 | `zhopa2_gather_item_debug_status_impl` | local helper | `npc, item_id` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 4611 | `M.zhopa2_debug_force_pickup` | module export | `npc, st, item, reason` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 4645 | `zhopa2_gather_item_replacement` | local helper | `original, force_selected, force_reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4765 | `patch_gather_classes` | local helper | `mod` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5080 | `M.patch_xr_gather_items` | module export | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5101 | `mod.zhopa2_wrapped_near_actor` | assigned wrapper | `obj, npc, ...` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 5124 | `zhopa2_is_protected_corpse` | local helper | `corpse, corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5132 | `zhopa2_event_corpse_ids` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5140 | `zhopa2_forget_corpse_id` | local helper | `corpse_id, consume_only` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5149 | `zhopa2_mark_corpse_checked` | local helper | `corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5156 | `M.zhopa2_mark_corpse_exhausted` | module export | `corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5179 | `M.zhopa2_corpse_exhausted` | module export | `corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5185 | `zhopa2_reject_corpse_candidate` | local helper | `mod, st, corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5237 | `M.zhopa2_reset_corpse_detection_state` | module export | `st` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5257 | `zhopa2_corpse_detect_dist_sqr` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5265 | `zhopa2_corpse_already_looted` | local helper | `corpse` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5272 | `zhopa2_is_inventory_owner` | local helper | `obj` | Supports runtime patches subsystem behavior. |
| 5289 | `zhopa2_corpse_has_money` | local helper | `corpse` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5298 | `M.zhopa2_corpse_can_take_item` | module export | `npc, item, section` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5311 | `zhopa2_corpse_has_takeable_item` | local helper | `npc, corpse, active` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5321 | `check_item` | local helper | `owner, item` | Supports runtime patches subsystem behavior. |
| 5336 | `zhopa2_corpse_has_candidate_loot` | local helper | `npc, corpse, corpse_id, active` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5356 | `zhopa2_corpse_record_loot` | local helper | `npc, corpse, item, value, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5364 | `zhopa2_item_value` | local helper | `section` | Supports runtime patches subsystem behavior. |
| 5371 | `corpse_original_func` | local helper | `mod, name` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5382 | `zhopa2_get_all_from_corpse_replacement` | local helper | `original` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5442 | `get_item` | local helper | `owner, item` | Supports runtime patches subsystem behavior. |
| 5484 | `patch_corpse_classes` | local helper | `mod` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5485 | `corpse_object` | local helper | `corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5492 | `reject_if_protected` | local helper | `st, corpse_id` | Supports runtime patches subsystem behavior. |
| 5501 | `cleanup_protected_state` | local helper | `st` | Reads, writes, clears, or migrates serializable runtime state. |
| 5639 | `M.patch_xr_corpse_detection` | module export | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5651 | `mod.zhopa2_wrapped_near_actor` | assigned wrapper | `obj, npc, ...` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 5667 | `M.patch_se_level_changer` | module export | `` | Resolves level, graph, route, distance, or position data. |
| 5673 | `run_runtime_patch` | local helper | `patch` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 5737 | `M.clear_prefixed_table` | module export | `tbl` | Clears transient state, reservations, or stale runtime references. |
| 5755 | `M.purge_squad_state` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 5776 | `M.purge_runtime_state` | module export | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 5843 | `M.unregister_runtime_callbacks` | module export | `` | Maintains indexed runtime state by adding or removing entries. |
| 5852 | `M.reset_runtime_ready_state` | module export | `` | Checks the shared runtime readiness barrier before context-dependent work. |
| 5864 | `M.ensure_all` | module export | `reason` | Supports runtime patches subsystem behavior. |
| 5880 | `M._on_game_load` | module export | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 5890 | `M._actor_on_first_update` | module export | `` | Supports runtime patches subsystem behavior. |
| 5903 | `M._actor_on_update` | module export | `` | Supports runtime patches subsystem behavior. |
| 5914 | `M._runtime_recheck_due` | module export | `reason` | Supports runtime patches subsystem behavior. |
| 5932 | `M.runtime_not_ready_reason` | module export | `` | Supports runtime patches subsystem behavior. |
| 5937 | `M.runtime_ready` | module export | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 5949 | `M.runtime_gate_ready` | module export | `reason` | Supports runtime patches subsystem behavior. |
| 5953 | `M.on_game_start` | module export | `` | Runtime hook for runtime patches lifecycle integration. |
| 5973 | `M.on_master_disable` | module export | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 5983 | `M.on_master_enable` | module export | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 5988 | `on_game_start` | script hook/global | `` | Runtime hook for runtime patches lifecycle integration. |
| 5992 | `_G.zhopa2_runtime_ready` | assigned wrapper | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 5996 | `_G.zhopa2_runtime_not_ready_reason` | assigned wrapper | `` | Supports runtime patches subsystem behavior. |

### `gamedata/scripts/zhopa2_service_fillers.script`

Role: base service NPC detection, adoption, and filler spawning.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 89 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the service fillers subsystem. |
| 98 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 106 | `debug_service_guard` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 113 | `runtime_ready` | local helper | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 125 | `surge_active` | local helper | `` | Supports service fillers subsystem behavior. |
| 130 | `cfg_alias` | local helper | `name` | Reads or normalizes configuration data for the service fillers subsystem. |
| 141 | `normalize_key` | local helper | `name` | Supports service fillers subsystem behavior. |
| 154 | `owner_engine` | local helper | `name` | Supports service fillers subsystem behavior. |
| 163 | `service_alias` | local helper | `engine` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 168 | `vanilla_prefix` | local helper | `engine` | Supports service fillers subsystem behavior. |
| 173 | `tg` | local helper | `` | Supports service fillers subsystem behavior. |
| 177 | `safe_manager` | local helper | `module_name, getter_name` | Validates safety gates and controlled fallback conditions. |
| 188 | `manager_time_due` | local helper | `mgr, last_field` | Supports service fillers subsystem behavior. |
| 208 | `callback_from_start` | local helper | `` | Supports service fillers subsystem behavior. |
| 221 | `surge_event_due` | local helper | `` | Supports service fillers subsystem behavior. |
| 226 | `psi_storm_event_due` | local helper | `` | Supports service fillers subsystem behavior. |
| 231 | `queue_emission_fill` | local helper | `kind, due` | Supports service fillers subsystem behavior. |
| 240 | `flush_pending_emission_fill` | local helper | `` | Supports service fillers subsystem behavior. |
| 258 | `smart_is_base` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 262 | `smart_name` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 279 | `object_debug_name` | local helper | `obj` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 299 | `object_debug_id` | local helper | `obj` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 316 | `section_exists` | local helper | `section` | Supports service fillers subsystem behavior. |
| 329 | `read_ini_string_from` | local helper | `ini, section, key` | Supports service fillers subsystem behavior. |
| 348 | `read_ini_string` | local helper | `job_or_section, key, smart` | Supports service fillers subsystem behavior. |
| 368 | `contains` | local helper | `haystack, needle` | Supports service fillers subsystem behavior. |
| 372 | `strip_inline_comment` | local helper | `value` | Supports service fillers subsystem behavior. |
| 383 | `plain_unique_provider_suitable` | local helper | `job_or_section, smart` | Supports service fillers subsystem behavior. |
| 398 | `role_from_level_spot` | local helper | `level_spot` | Resolves level, graph, route, distance, or position data. |
| 405 | `normalize_role` | local helper | `role` | Supports service fillers subsystem behavior. |
| 419 | `classify_job_role` | local helper | `job_or_section, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 496 | `role_from_section` | local helper | `section` | Resolves a safe section name for runtime classification. |
| 515 | `zhop_service_squad` | local helper | `squad, section` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 523 | `safe_npc_section` | local helper | `se_obj` | Resolves a safe section name for runtime classification. |
| 536 | `safe_squad_by_id` | local helper | `id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 561 | `online_object` | local helper | `se_obj` | Resolves an online game object through db.storage or level lookups. |
| 579 | `is_stalker_se` | local helper | `se_obj` | Supports service fillers subsystem behavior. |
| 589 | `se_object_alive` | local helper | `se_obj` | Supports service fillers subsystem behavior. |
| 602 | `set_online_community` | local helper | `se_obj, engine_owner` | Supports service fillers subsystem behavior. |
| 616 | `service_squad_from_member` | local helper | `se_obj` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 624 | `same_id` | local helper | `a, b` | Supports service fillers subsystem behavior. |
| 630 | `pin_service_squad` | local helper | `squad, smart, section` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 687 | `adopt_service_squad` | local helper | `squad, smart, engine_owner, section` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 695 | `adopt_service_member` | local helper | `se_obj, smart, engine_owner, section` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 707 | `collect_allowed_roles` | local helper | `smart` | Supports service fillers subsystem behavior. |
| 722 | `role_from_member_info` | local helper | `info, smart` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 739 | `M.job_accepts_service_npc` | module export | `npc_info, job, smart` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 757 | `collect_existing_roles` | local helper | `smart, engine_owner` | Supports service fillers subsystem behavior. |
| 799 | `roles_from_set` | local helper | `set` | Supports service fillers subsystem behavior. |
| 813 | `missing_roles` | local helper | `allowed, existing` | Supports service fillers subsystem behavior. |
| 824 | `roles_string` | local helper | `roles` | Supports service fillers subsystem behavior. |
| 831 | `clear_smart_fields` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 844 | `mark_smart` | local helper | `smart, engine_owner, missing, reason` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 859 | `unmark_smart` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 865 | `resolve_ownership` | local helper | `smart, ownership` | Safely resolves an ALife/server-side object or runtime reference. |
| 882 | `service_section` | local helper | `engine_owner, role` | Resolves a safe section name for runtime classification. |
| 909 | `spawn_service_squad` | local helper | `smart, engine_owner, role` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 928 | `M.reconcile_smart` | module export | `smart, ownership, allow_spawn, reason` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 989 | `smart_by_id` | local helper | `id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1001 | `M.fill_marked_smarts` | module export | `reason` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1026 | `M.on_smart_update` | module export | `smart, ownership` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1044 | `M.on_smart_unregister` | module export | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1053 | `M.on_before_surge` | module export | `flags` | Supports service fillers subsystem behavior. |
| 1060 | `M.on_before_psi_storm` | module export | `flags` | Supports service fillers subsystem behavior. |
| 1067 | `M.actor_on_update` | module export | `` | Runtime hook for service fillers lifecycle integration. |
| 1074 | `M.on_game_load` | module export | `` | Runtime hook for service fillers lifecycle integration. |
| 1080 | `server_entity_on_unregister` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 1086 | `M.on_game_start` | module export | `` | Runtime hook for service fillers lifecycle integration. |
| 1108 | `M.on_master_disable` | module export | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 1146 | `on_game_start` | script hook/global | `` | Runtime hook for service fillers lifecycle integration. |

### `gamedata/scripts/zhopa2_smart_service_slot_doctor.script`

Role: bounded observation and vanilla smart-job reselection for stalled trade/technician customer jobs.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 48 | `has_intent` | assigned wrapper | `st` | Creates, validates, or clears a bounded runtime intent used by a vanilla scheme or smart job. |
| 74 | `has_intent` | assigned wrapper | `st` | Creates, validates, or clears a bounded runtime intent used by a vanilla scheme or smart job. |
| 115 | `now` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 119 | `surge_active` | local helper | `` | Supports smart service slot doctor subsystem behavior. |
| 124 | `reset_runtime` | local helper | `` | Clears transient state, reservations, or stale runtime references. |
| 139 | `pause_for_surge` | local helper | `` | Supports smart service slot doctor subsystem behavior. |
| 146 | `mark_runtime_ready` | local helper | `` | Checks the shared runtime readiness barrier before context-dependent work. |
| 151 | `get_logger` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 155 | `emit` | local helper | `level_name, tag, line` | Supports smart service slot doctor subsystem behavior. |
| 165 | `info` | assigned wrapper | `tag, line` | Supports smart service slot doctor subsystem behavior. |
| 168 | `warn` | assigned wrapper | `tag, line` | Supports smart service slot doctor subsystem behavior. |
| 174 | `current_level_name` | local helper | `` | Resolves level, graph, route, distance, or position data. |
| 185 | `append_fallback_log` | local helper | `level_name, line` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 197 | `log_with` | local helper | `level_name, fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 220 | `log_info` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 224 | `log_warn` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 228 | `log_smart_skip` | local helper | `smart, reason` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 232 | `starts_with` | local helper | `str, prefix` | Supports smart service slot doctor subsystem behavior. |
| 236 | `string_has` | local helper | `str, fragment` | Supports smart service slot doctor subsystem behavior. |
| 240 | `is_alive_object` | local helper | `obj` | Supports smart service slot doctor subsystem behavior. |
| 251 | `get_level_object` | local helper | `id` | Resolves level, graph, route, distance, or position data. |
| 262 | `get_live_object` | local helper | `id` | Supports smart service slot doctor subsystem behavior. |
| 274 | `normalize_id` | local helper | `id` | Supports smart service slot doctor subsystem behavior. |
| 282 | `resolve_squad_id_from_npc_id` | local helper | `npc_id` | Safely resolves an ALife/server-side object or runtime reference. |
| 324 | `get_current_squad_task_for_npc` | local helper | `npc_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 343 | `economy_mod` | local helper | `` | Supports smart service slot doctor subsystem behavior. |
| 352 | `has_active_prepared_trade` | local helper | `entry, snapshot, npc_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 361 | `has_active_trade_intent` | local helper | `entry, snapshot, npc_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 369 | `resolve_current_smart_for_npc_id` | local helper | `npc_id` | Safely resolves an ALife/server-side object or runtime reference. |
| 403 | `safe_position` | local helper | `obj` | Validates safety gates and controlled fallback conditions. |
| 414 | `safe_current_point_index` | local helper | `obj` | Validates safety gates and controlled fallback conditions. |
| 425 | `safe_path_index` | local helper | `obj` | Validates safety gates and controlled fallback conditions. |
| 436 | `section_to_logic_from_active` | local helper | `active_section` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 443 | `active_section_matches_rule` | local helper | `rule, active_section` | Supports smart service slot doctor subsystem behavior. |
| 447 | `slot_section_matches_rule` | local helper | `rule, slot_section` | Supports smart service slot doctor subsystem behavior. |
| 451 | `read_ini_string` | local helper | `ini_obj, section, key` | Supports smart service slot doctor subsystem behavior. |
| 463 | `read_job_string` | local helper | `job, smart, key` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 475 | `get_service_rule_by_job` | local helper | `job, smart` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 493 | `get_smart_name` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 504 | `get_rule_cache_for_smart` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 541 | `find_job_by_section` | local helper | `smart, section` | Resolves a safe section name for runtime classification. |
| 552 | `clear_job_idle` | local helper | `job` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 558 | `build_smart_snapshot` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 618 | `count_table_entries` | local helper | `t` | Supports smart service slot doctor subsystem behavior. |
| 629 | `get_service_rule_by_active_section` | local helper | `active_section` | Resolves a safe section name for runtime classification. |
| 638 | `log_smart_seen` | local helper | `snapshot` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 642 | `log_service_snapshot` | local helper | `snapshot, issues` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 646 | `clear_runtime_state_for_npc` | local helper | `npc_id` | Reads, writes, clears, or migrates serializable runtime state. |
| 657 | `clear_runtime_state_for_smart` | local helper | `smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 691 | `quantize_coord` | local helper | `v` | Supports smart service slot doctor subsystem behavior. |
| 699 | `quantize_coord_coarse` | local helper | `v` | Supports smart service slot doctor subsystem behavior. |
| 707 | `stable_table_fingerprint` | local helper | `t` | Supports smart service slot doctor subsystem behavior. |
| 734 | `safe_money` | local helper | `obj` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 745 | `safe_best_weapon` | local helper | `obj` | Validates safety gates and controlled fallback conditions. |
| 756 | `safe_item_section` | local helper | `item` | Resolves a safe section name for runtime classification. |
| 767 | `safe_installed_upgrades_fingerprint` | local helper | `item` | Validates safety gates and controlled fallback conditions. |
| 778 | `build_progress_signature` | local helper | `entry, rule` | Supports smart service slot doctor subsystem behavior. |
| 801 | `build_post_tech_signature` | local helper | `npc, info, st` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 816 | `is_ingress_watch_smart` | local helper | `snapshot` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 822 | `get_service_slot_for_rule` | local helper | `snapshot, rule` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 834 | `build_ingress_signature` | local helper | `entry, slot_owner_id` | Supports smart service slot doctor subsystem behavior. |
| 847 | `choose_ingress_rule` | local helper | `snapshot, entry` | Supports smart service slot doctor subsystem behavior. |
| 877 | `maybe_arm_departed_post_tech_watch` | local helper | `snapshot, npc_id, state, tg` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 903 | `refresh_progress_tracking` | local helper | `snapshot` | Supports smart service slot doctor subsystem behavior. |
| 951 | `refresh_ingress_tracking` | local helper | `snapshot` | Supports smart service slot doctor subsystem behavior. |
| 999 | `sanitize_service_slots` | local helper | `snapshot` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 1032 | `make_post_complete_issue` | local helper | `snapshot, entry, rule, slot_section, linked, watch` | Supports smart service slot doctor subsystem behavior. |
| 1049 | `make_orphan_issue` | local helper | `snapshot, entry, rule, slot_section, linked, squad_id, current_task` | Supports smart service slot doctor subsystem behavior. |
| 1067 | `make_no_progress_issue` | local helper | `snapshot, entry, rule, slot_section, linked, stalled_ms` | Supports smart service slot doctor subsystem behavior. |
| 1084 | `make_ingress_issue` | local helper | `snapshot, entry, rule, slot_section, linked, stalled_ms, slot_owner_id` | Supports smart service slot doctor subsystem behavior. |
| 1102 | `clear_completed_watch` | local helper | `npc_id` | Clears transient state, reservations, or stale runtime references. |
| 1109 | `clear_post_tech_watch` | local helper | `npc_id` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 1116 | `arm_completed_watch` | local helper | `npc, smart, kind, status, reason` | Supports smart service slot doctor subsystem behavior. |
| 1149 | `arm_post_tech_watch` | assigned wrapper | `npc, smart, reason, left_service_tg` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 1194 | `arm_post_tech_unknown_watch` | local helper | `npc, smart, kind, status, reason` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 1201 | `detect_post_complete_issues` | local helper | `snapshot, issued` | Supports smart service slot doctor subsystem behavior. |
| 1256 | `detect_orphan_service_issues` | local helper | `snapshot, issued` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 1291 | `detect_no_progress_issues` | local helper | `snapshot, issued` | Supports smart service slot doctor subsystem behavior. |
| 1319 | `detect_ingress_issues` | local helper | `snapshot, issued` | Supports smart service slot doctor subsystem behavior. |
| 1353 | `detect_cleanup_issues` | local helper | `snapshot` | Clears transient state, reservations, or stale runtime references. |
| 1380 | `ensure_state` | local helper | `issue` | Reads, writes, clears, or migrates serializable runtime state. |
| 1419 | `clear_intent_items` | local helper | `items` | Creates, validates, or clears a bounded runtime intent used by a vanilla scheme or smart job. |
| 1432 | `clear_service_intent` | local helper | `st, job, rule` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 1451 | `reselect_npc_smart_job` | local helper | `issue` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1488 | `resolve_issue_with_reselect` | assigned wrapper | `issue, tag` | Safely resolves an ALife/server-side object or runtime reference. |
| 1517 | `resolve_service_post_complete_stuck` | local helper | `issue` | Safely resolves an ALife/server-side object or runtime reference. |
| 1521 | `resolve_service_orphaned_issue` | local helper | `issue` | Safely resolves an ALife/server-side object or runtime reference. |
| 1525 | `resolve_service_no_progress_issue` | local helper | `issue` | Safely resolves an ALife/server-side object or runtime reference. |
| 1529 | `resolve_service_ingress_stuck_issue` | local helper | `issue` | Safely resolves an ALife/server-side object or runtime reference. |
| 1540 | `issue_key` | local helper | `issue` | Supports smart service slot doctor subsystem behavior. |
| 1547 | `queue_repair_issue` | local helper | `issue` | Supports smart service slot doctor subsystem behavior. |
| 1557 | `process_repair_queue` | local helper | `limit` | Supports smart service slot doctor subsystem behavior. |
| 1583 | `clear_resolved_states` | local helper | `snapshot, issued` | Reads, writes, clears, or migrates serializable runtime state. |
| 1596 | `process_smart` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1646 | `on_actor_first_update` | local helper | `` | Supports smart service slot doctor subsystem behavior. |
| 1650 | `on_load_state` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 1654 | `on_actor_update` | local helper | `` | Supports smart service slot doctor subsystem behavior. |
| 1660 | `on_server_entity_unregister` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 1670 | `on_smart_terrain_update` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1674 | `on_npc_update` | local helper | `npc` | Supports smart service slot doctor subsystem behavior. |
| 1774 | `register_callbacks_once` | local helper | `` | Maintains indexed runtime state by adding or removing entries. |
| 1790 | `on_game_start` | script hook/global | `` | Runtime hook for smart service slot doctor lifecycle integration. |
| 1797 | `inst.on_master_disable` | assigned wrapper | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 1814 | `inst.on_axr_service_result` | assigned wrapper | `npc, smart, kind, status, reason` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |

### `gamedata/scripts/zhopa2_story_north_migration.script`

Role: story-gated northern migration task selection and recovery.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 59 | `load_module` | local helper | `name` | Reads, writes, clears, or migrates serializable runtime state. |
| 68 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the story north migration subsystem. |
| 72 | `index_mod` | local helper | `` | Supports story north migration subsystem behavior. |
| 76 | `perception_mod` | local helper | `` | Supports story north migration subsystem behavior. |
| 80 | `topology_mod` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 84 | `runtime_ready` | local helper | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 96 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 104 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 112 | `debug_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 116 | `debug_log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 122 | `now_ms` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 126 | `normalize_id` | local helper | `value` | Supports story north migration subsystem behavior. |
| 134 | `normalize_status` | local helper | `value` | Supports story north migration subsystem behavior. |
| 145 | `normalize_sid_set` | local helper | `src` | Supports story north migration subsystem behavior. |
| 164 | `normalize_status_map` | local helper | `src` | Supports story north migration subsystem behavior. |
| 178 | `event_state` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 191 | `resolve_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 216 | `object_level` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 245 | `safe_name` | local helper | `obj` | Validates safety gates and controlled fallback conditions. |
| 258 | `squad_section_name` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 276 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 284 | `normalize_faction` | local helper | `value` | Supports story north migration subsystem behavior. |
| 299 | `squad_faction` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 310 | `relation_faction` | local helper | `value` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 315 | `relation_allows_coexist` | local helper | `source_faction, other_faction` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 334 | `is_story_mode_active` | local helper | `` | Handles story-gated squad events, conversion, migration, or recovery. |
| 358 | `has_info` | local helper | `info` | Supports story north migration subsystem behavior. |
| 378 | `trigger_active` | local helper | `` | Supports story north migration subsystem behavior. |
| 382 | `feature_enabled_now` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 388 | `percent_value` | local helper | `` | Supports story north migration subsystem behavior. |
| 398 | `is_monster_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 407 | `squad_can_manage` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 422 | `is_ap_owned_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 431 | `is_plain_stalker_sim_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 442 | `eligible_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 456 | `smart_by_id` | local helper | `smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 469 | `target_validation_opts` | local helper | `kind` | Validates safety gates and controlled fallback conditions. |
| 480 | `collect_target_factions` | local helper | `smart` | Supports story north migration subsystem behavior. |
| 511 | `target_safe_for_squad` | local helper | `squad, smart, expected_level, kind` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 535 | `game_graph_distance` | local helper | `a, b` | Resolves level, graph, route, distance, or position data. |
| 558 | `pick_random` | local helper | `list` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 565 | `shuffle_in_place` | local helper | `list` | Supports story north migration subsystem behavior. |
| 578 | `smarts_on_level` | local helper | `level_name, kind` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 586 | `base_smarts_on_level` | local helper | `level_name` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 594 | `projected_load` | local helper | `level_name, exclude_sid` | Reads, writes, clears, or migrates serializable runtime state. |
| 610 | `ordered_north_levels` | local helper | `squad` | Handles story-gated squad events, conversion, migration, or recovery. |
| 647 | `nearest_safe_from_list` | local helper | `squad, level_name, list, kind` | Validates safety gates and controlled fallback conditions. |
| 669 | `safe_random_smart` | local helper | `squad, level_name` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 681 | `pick_safe_target_on_level` | local helper | `squad, level_name` | Validates safety gates and controlled fallback conditions. |
| 696 | `neighbor_levels` | local helper | `level_name` | Resolves level, graph, route, distance, or position data. |
| 707 | `pick_north_target` | local helper | `squad` | Handles story-gated squad events, conversion, migration, or recovery. |
| 734 | `story_task_active` | local helper | `squad` | Handles story-gated squad events, conversion, migration, or recovery. |
| 738 | `set_status` | local helper | `sid, status` | Supports story north migration subsystem behavior. |
| 745 | `M.is_story_task` | module export | `task` | Handles story-gated squad events, conversion, migration, or recovery. |
| 750 | `M.is_sid_selected` | module export | `sid` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 755 | `M.is_sid_locked` | module export | `sid` | Supports story north migration subsystem behavior. |
| 764 | `save_state` | script hook/global | `m_data` | Runtime hook for story north migration lifecycle integration. |
| 779 | `load_state` | script hook/global | `m_data` | Runtime hook for story north migration lifecycle integration. |
| 811 | `clear_story_task` | local helper | `squad, reason` | Handles story-gated squad events, conversion, migration, or recovery. |
| 819 | `assign_rest` | local helper | `squad, reason` | Supports story north migration subsystem behavior. |
| 831 | `sync_live_target` | local helper | `squad` | Supports story north migration subsystem behavior. |
| 847 | `story_arrived` | local helper | `squad, smart` | Handles story-gated squad events, conversion, migration, or recovery. |
| 879 | `assign_story_target` | local helper | `squad, sid, smart, level_name, source` | Handles story-gated squad events, conversion, migration, or recovery. |
| 902 | `retarget_story_task` | local helper | `squad, sid, current_target, reason` | Handles story-gated squad events, conversion, migration, or recovery. |
| 936 | `activate_selected_sid` | local helper | `sid, source, squad` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 995 | `process_rollout_queue` | local helper | `source, limit` | Supports story north migration subsystem behavior. |
| 1017 | `collect_eligible_sids` | local helper | `` | Supports story north migration subsystem behavior. |
| 1040 | `maybe_fire` | local helper | `source` | Supports story north migration subsystem behavior. |
| 1083 | `reconcile_selected` | local helper | `source` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1108 | `M.update_squad_tasks` | module export | `squad, ctx` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1130 | `M.debug_status_line` | module export | `squad` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 1138 | `M.ensure_runtime_ready` | module export | `force_callbacks` | Checks the shared runtime readiness barrier before context-dependent work. |
| 1145 | `request_reconcile` | local helper | `source` | Supports story north migration subsystem behavior. |
| 1155 | `actor_on_update` | script hook/global | `` | Runtime hook for story north migration lifecycle integration. |
| 1170 | `actor_on_first_update` | script hook/global | `` | Runtime hook for story north migration lifecycle integration. |
| 1174 | `on_game_load` | script hook/global | `` | Runtime hook for story north migration lifecycle integration. |
| 1178 | `on_option_change` | script hook/global | `` | Runtime hook for story north migration lifecycle integration. |
| 1182 | `server_entity_on_unregister` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 1192 | `server_entity_on_register` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 1203 | `squad_on_after_level_change` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1211 | `M.on_game_start` | module export | `` | Runtime hook for story north migration lifecycle integration. |
| 1231 | `reg` | local helper | `name, fn` | Supports story north migration subsystem behavior. |
| 1259 | `M.on_master_disable` | module export | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 1292 | `on_game_start` | script hook/global | `` | Runtime hook for story north migration lifecycle integration. |

### `gamedata/scripts/zhopa2_story_psy_watchdog.script`

Role: story-gated psi-level squad conversion into zombied squads.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 40 | `load_module` | local helper | `name` | Reads, writes, clears, or migrates serializable runtime state. |
| 49 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the story psy watchdog subsystem. |
| 53 | `index_mod` | local helper | `` | Supports story psy watchdog subsystem behavior. |
| 57 | `perception_mod` | local helper | `` | Supports story psy watchdog subsystem behavior. |
| 61 | `tasks_mod` | local helper | `` | Supports story psy watchdog subsystem behavior. |
| 65 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 73 | `cfg_string` | local helper | `key, default` | Reads or normalizes configuration data for the story psy watchdog subsystem. |
| 81 | `runtime_ready` | local helper | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 93 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 97 | `debug_log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 103 | `now_ms` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 107 | `normalize_id` | local helper | `value` | Supports story psy watchdog subsystem behavior. |
| 115 | `lower_trim` | local helper | `value` | Supports story psy watchdog subsystem behavior. |
| 126 | `parse_csv_set` | local helper | `value` | Supports story psy watchdog subsystem behavior. |
| 138 | `invalidate_runtime_caches` | local helper | `` | Validates safety gates and controlled fallback conditions. |
| 143 | `get_psi_levels` | local helper | `` | Resolves level, graph, route, distance, or position data. |
| 150 | `get_immune_factions` | local helper | `` | Supports story psy watchdog subsystem behavior. |
| 157 | `has_info` | local helper | `info` | Supports story psy watchdog subsystem behavior. |
| 178 | `is_story_mode_active` | local helper | `` | Handles story-gated squad events, conversion, migration, or recovery. |
| 189 | `feature_enabled_now` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 205 | `resolve_alife_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 226 | `get_board` | local helper | `` | Supports story psy watchdog subsystem behavior. |
| 239 | `clone_position` | local helper | `pos` | Resolves level, graph, route, distance, or position data. |
| 254 | `safe_position` | local helper | `obj` | Validates safety gates and controlled fallback conditions. |
| 270 | `safe_name` | local helper | `obj` | Validates safety gates and controlled fallback conditions. |
| 286 | `section_faction` | local helper | `section` | Supports story psy watchdog subsystem behavior. |
| 294 | `squad_section_name` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 315 | `squad_community` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 330 | `cfg_alias` | local helper | `value` | Reads or normalizes configuration data for the story psy watchdog subsystem. |
| 341 | `is_immune_faction` | local helper | `community` | Supports story psy watchdog subsystem behavior. |
| 350 | `is_already_zombied` | local helper | `squad, community` | Handles story-gated squad events, conversion, migration, or recovery. |
| 360 | `is_target_level` | local helper | `level_name` | Resolves level, graph, route, distance, or position data. |
| 365 | `level_name_by_gvid` | local helper | `gvid` | Resolves level, graph, route, distance, or position data. |
| 377 | `squad_level_name` | local helper | `squad, known_level` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 387 | `extract_member_candidate_id` | local helper | `k, v` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 397 | `squad_member_ids` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 403 | `push` | local helper | `id` | Supports story psy watchdog subsystem behavior. |
| 426 | `squad_member_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 438 | `squad_can_manage` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 455 | `is_plain_stalker_sim_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 467 | `is_ap_owned_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 476 | `pick_zombied_squad_section` | local helper | `source_section` | Resolves a safe section name for runtime classification. |
| 494 | `pick_zombied_member_section` | local helper | `zombied_squad_section` | Resolves a safe section name for runtime classification. |
| 502 | `smart_object_by_id` | local helper | `smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 518 | `smart_level_name` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 525 | `build_context` | local helper | `squad, community, level_name` | Formats names or display text for diagnostics and UI output. |
| 570 | `create_empty_squad` | local helper | `section, position, lvid, gvid` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 590 | `populate_zombied_squad` | local helper | `squad, context` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 603 | `assign_squad_to_smart` | local helper | `squad, smart_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 613 | `finalize_spawned_squad` | local helper | `squad, context` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 649 | `cleanup_source_task` | local helper | `squad` | Clears transient state, reservations, or stale runtime references. |
| 662 | `unregister_released_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 673 | `release_squad_safe` | local helper | `squad, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 704 | `log_mutation_error` | local helper | `sid, context, source, reason, new_squad, extra` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 731 | `candidate_context` | local helper | `squad, source, known_level` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 769 | `M.convert_squad_to_zombied` | module export | `squad, context, source` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 828 | `M.try_process_squad` | module export | `squad, source, known_level` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 836 | `M.reconcile_all_levels` | module export | `source` | Resolves level, graph, route, distance, or position data. |
| 867 | `request_reconcile` | local helper | `source` | Supports story psy watchdog subsystem behavior. |
| 876 | `actor_on_update` | script hook/global | `` | Runtime hook for story psy watchdog lifecycle integration. |
| 888 | `actor_on_first_update` | script hook/global | `` | Runtime hook for story psy watchdog lifecycle integration. |
| 893 | `on_game_load` | script hook/global | `` | Runtime hook for story psy watchdog lifecycle integration. |
| 898 | `on_option_change` | script hook/global | `` | Runtime hook for story psy watchdog lifecycle integration. |
| 903 | `squad_on_after_level_change` | local helper | `squad, old_level, new_level` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 914 | `server_entity_on_register` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 922 | `M.on_game_start` | module export | `` | Runtime hook for story psy watchdog lifecycle integration. |
| 940 | `register_callback` | local helper | `name, fn` | Maintains indexed runtime state by adding or removing entries. |
| 966 | `M.on_master_disable` | module export | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 984 | `on_game_start` | script hook/global | `` | Runtime hook for story psy watchdog lifecycle integration. |

### `gamedata/scripts/zhopa2_task_scoring.script`

Role: bounded task-target scoring, runtime level geometry, faction-presence snapshots, and configurable lore preferences.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 16 | `cfg` | local helper | `` | Supports task scoring subsystem behavior. |
| 26 | `perception` | local helper | `` | Supports task scoring subsystem behavior. |
| 36 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 44 | `debug_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 48 | `debug_printf` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 54 | `reset_runtime` | local helper | `` | Clears transient state, reservations, or stale runtime references. |
| 65 | `reload_ini` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 69 | `ini_string` | local helper | `section, key` | Supports task scoring subsystem behavior. |
| 77 | `ini_number` | local helper | `section, key` | Supports task scoring subsystem behavior. |
| 86 | `comma_set` | local helper | `value` | Supports task scoring subsystem behavior. |
| 100 | `smart_point` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 123 | `rebuild_geometry` | local helper | `board` | Supports task scoring subsystem behavior. |
| 151 | `ensure_geometry` | local helper | `` | Supports task scoring subsystem behavior. |
| 160 | `squad_section_name` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 177 | `squad_strength` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 208 | `squad_faction` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 217 | `geography_excluded` | local helper | `squad` | Supports task scoring subsystem behavior. |
| 222 | `add_presence` | local helper | `level_name, faction, strength` | Maintains indexed runtime state by adding or removing entries. |
| 231 | `remove_presence` | local helper | `squad_id` | Maintains indexed runtime state by adding or removing entries. |
| 243 | `track_presence` | local helper | `squad, level_name` | Supports task scoring subsystem behavior. |
| 258 | `rebuild_presence` | local helper | `board` | Supports task scoring subsystem behavior. |
| 269 | `ensure_presence` | local helper | `` | Supports task scoring subsystem behavior. |
| 278 | `profile_name_for_faction` | local helper | `faction` | Formats names or display text for diagnostics and UI output. |
| 291 | `M.profile_for_squad` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 298 | `M.profile_task_weight` | module export | `squad, task` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 311 | `M.hunt_options` | module export | `squad, fallback_prey, fallback_level_mode` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 323 | `M.faction_relation` | module export | `owner_faction, other_faction` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 334 | `M.level_metadata` | module export | `level_name` | Resolves level, graph, route, distance, or position data. |
| 362 | `M.target_level` | module export | `target` | Resolves level, graph, route, distance, or position data. |
| 378 | `geography_modifier` | local helper | `squad, target_level` | Supports task scoring subsystem behavior. |
| 404 | `presence_modifier` | local helper | `squad, target_level` | Supports task scoring subsystem behavior. |
| 439 | `lore_modifier` | local helper | `squad, candidate` | Supports task scoring subsystem behavior. |
| 464 | `M.make_candidate` | module export | `squad, choice, base_weight, selection_class` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 484 | `weighted_pick` | local helper | `candidates` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 503 | `M.select_candidate` | module export | `squad, candidates, context` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 539 | `M.materialize` | module export | `candidate` | Supports task scoring subsystem behavior. |
| 543 | `M.collect_trade_route_candidates` | module export | `squad, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 555 | `M.allow_conditional_target` | module export | `squad, task, target` | Supports task scoring subsystem behavior. |
| 589 | `M.on_smart_registered` | module export | `_, _` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 593 | `M.on_smart_unregistered` | module export | `_, _` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 597 | `M.on_squad_level_changed` | module export | `squad, old_level, new_level` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 606 | `M.on_squad_unregistered` | module export | `squad, _` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 614 | `M.on_buckets_rebuilt` | module export | `board` | Supports task scoring subsystem behavior. |
| 619 | `M.on_game_start` | module export | `` | Runtime hook for task scoring lifecycle integration. |
| 634 | `M.on_master_disable` | module export | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 643 | `on_game_load` | script hook/global | `` | Runtime hook for task scoring lifecycle integration. |
| 647 | `on_game_start` | script hook/global | `` | Runtime hook for task scoring lifecycle integration. |

### `gamedata/scripts/zhopa2_tasks.script`

Role: task constants, task FSM, assignment, completion, fallback rules, and server-side revenge relations.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 40 | `cfg` | local helper | `` | Supports tasks subsystem behavior. |
| 50 | `perception` | local helper | `` | Supports tasks subsystem behavior. |
| 59 | `memory_mod` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 68 | `offline_combat_mod` | local helper | `` | Supports tasks subsystem behavior. |
| 77 | `loot_mod` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 86 | `artifacts_mod` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 95 | `economy_mod` | local helper | `` | Supports tasks subsystem behavior. |
| 104 | `index_mod` | local helper | `` | Supports tasks subsystem behavior. |
| 113 | `story_north_mod` | local helper | `` | Handles story-gated squad events, conversion, migration, or recovery. |
| 124 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 132 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 140 | `scoring_pipeline_enabled` | local helper | `` | Supports tasks subsystem behavior. |
| 146 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 154 | `is_night_now` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 164 | `revenge_expired_by_night` | local helper | `` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 168 | `surge_active_uncached` | local helper | `` | Supports tasks subsystem behavior. |
| 214 | `task_scoring` | local helper | `` | Supports tasks subsystem behavior. |
| 223 | `M.surge_active` | module export | `force_refresh` | Supports tasks subsystem behavior. |
| 233 | `squad_section_name` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 251 | `config_faction_for_section` | local helper | `section` | Reads or normalizes configuration data for the tasks subsystem. |
| 259 | `mutant_behavior_id` | local helper | `squad` | Supports tasks subsystem behavior. |
| 274 | `now_ms` | assigned wrapper | `` | Calculates time, cooldown, or tick-throttling values. |
| 281 | `safe_alife_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 290 | `M.direct_target_allowed` | module export | `squad, task, target_or_id` | Supports tasks subsystem behavior. |
| 306 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 325 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 341 | `object_is_smart` | local helper | `obj` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 354 | `named_id` | local helper | `obj_or_id` | Formats names or display text for diagnostics and UI output. |
| 365 | `debug_trade_log` | local helper | `squad, stage, result, detail` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 408 | `current_frame_key` | local helper | `` | Supports tasks subsystem behavior. |
| 425 | `assignment_budget_open` | local helper | `squad` | Supports tasks subsystem behavior. |
| 438 | `mark_task_no_target` | local helper | `squad, task` | Supports tasks subsystem behavior. |
| 447 | `clear_task_no_target` | local helper | `squad, task` | Clears transient state, reservations, or stale runtime references. |
| 454 | `task_no_target_cooldown_active` | local helper | `squad, task` | Calculates time, cooldown, or tick-throttling values. |
| 467 | `target_valid_cache_key` | local helper | `squad, task, target` | Validates safety gates and controlled fallback conditions. |
| 477 | `target_valid_cache_hit` | local helper | `squad, key` | Validates safety gates and controlled fallback conditions. |
| 484 | `target_valid_cache_store` | local helper | `squad, key` | Validates safety gates and controlled fallback conditions. |
| 491 | `target_valid_cache_clear` | local helper | `squad` | Validates safety gates and controlled fallback conditions. |
| 498 | `is_monster_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 518 | `mutant_cycle_active` | local helper | `squad` | Supports tasks subsystem behavior. |
| 539 | `mutant_has_stalker_task` | local helper | `squad, task` | Supports tasks subsystem behavior. |
| 543 | `make_choice` | local helper | `task, target, weight, reason, duration, patrol` | Supports tasks subsystem behavior. |
| 561 | `task_weight` | local helper | `key, default` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 581 | `registry_weight_meta` | local helper | `pool, name` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 586 | `register_task` | local helper | `pool, name, builder, weight_fn` | Maintains indexed runtime state by adding or removing entries. |
| 600 | `pick_weighted` | local helper | `list` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 620 | `builder_choice` | local helper | `built` | Supports tasks subsystem behavior. |
| 630 | `registry_entry_weight` | local helper | `entry, squad, context` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 651 | `pick_registry_entry` | local helper | `list, tried, squad, context` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 666 | `update_debug` | script hook/global | `squad` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 673 | `M.should_skip_task_update` | module export | `squad` | Supports tasks subsystem behavior. |
| 716 | `assign_rest` | local helper | `squad, reason` | Supports tasks subsystem behavior. |
| 724 | `mark_rest_trade_done` | local helper | `squad, result` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 734 | `mark_rest_trade_wait` | local helper | `squad, result` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 743 | `rest_trade_result_is_final` | local helper | `result` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 759 | `sync_rest_trade_done_from_economy` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 776 | `rest_trade_smart_available` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 785 | `try_auto_trade_at_rest_smart` | local helper | `squad, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 797 | `recover_prepared_trade_if_any` | local helper | `squad, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 809 | `tick_rest_auto_trade` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 849 | `rest_trade_blocks_completion` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 871 | `try_after_night_rest_auto_trade` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 903 | `tick_base_camping_auto_trade` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 932 | `trade_route_allowed_from_context` | local helper | `context` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 937 | `trade_route_task_weight` | local helper | `squad, context, base_weight, route_candidates` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 973 | `trade_route_result_waiting` | local helper | `result` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 981 | `mark_trade_route_wait` | local helper | `squad, result` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 990 | `complete_trade_route` | local helper | `squad, result` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1002 | `sync_trade_route_done_from_economy` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1010 | `tick_trade_route` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1037 | `final_smart` | local helper | `p, squad, smart, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1044 | `force_exit_target` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1083 | `target_blacklisted_for_squad` | local helper | `squad, target_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1100 | `task_target_blacklisted` | local helper | `squad` | Validates safety gates and controlled fallback conditions. |
| 1107 | `clear_post_guide_rest` | local helper | `squad, result` | Clears transient state, reservations, or stale runtime references. |
| 1119 | `post_guide_rest_target` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1152 | `apply_post_guide_rest` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1174 | `clone_task_options` | local helper | `src` | Supports tasks subsystem behavior. |
| 1182 | `build_smart_target_choices` | local helper | `squad, task, total_weight, reason, opts, level_modes` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1210 | `build_stalker_explore` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1225 | `build_stalker_populate` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1263 | `build_stalker_patrol` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1276 | `pick_hunt_target_with_policy` | local helper | `squad, p, options` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1300 | `build_stalker_hunt` | local helper | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1325 | `build_stalker_artefact` | local helper | `squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1373 | `build_stalker_trade` | local helper | `squad, context` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1425 | `build_mutant_hunt` | local helper | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1450 | `build_mutant_patrol` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1463 | `build_mutant_explore` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1481 | `build_stalker_profile_rest` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1507 | `select_from_registry_legacy` | local helper | `pool, squad, context` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1528 | `append_scored_choices` | local helper | `out, scoring, squad, entry_weight, built` | Supports tasks subsystem behavior. |
| 1529 | `append` | local helper | `choice, candidate_weight` | Supports tasks subsystem behavior. |
| 1556 | `select_from_registry` | local helper | `pool, squad, context` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1592 | `select_stalker_task` | local helper | `squad, reason` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1610 | `select_stalker_night_rest` | script hook/global | `squad` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1650 | `select_mutant_task` | local helper | `squad, reason` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1667 | `mutant_night_hunt_only` | local helper | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1672 | `night_rest_target_unsafe` | local helper | `squad` | Validates safety gates and controlled fallback conditions. |
| 1683 | `assign_choice` | local helper | `squad, choice, fallback_reason` | Supports tasks subsystem behavior. |
| 1737 | `assign_stalker_hunt_or_rest` | local helper | `squad, reason` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1746 | `repair_invalid_mutant_task` | local helper | `squad` | Validates safety gates and controlled fallback conditions. |
| 1762 | `clear_zhopa2_movement_target` | local helper | `squad, clear_any` | Clears transient state, reservations, or stale runtime references. |
| 1789 | `pause_for_surge` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1817 | `M.interrupt_task` | module export | `squad, task, target_id, duration_sec, reason, patrol, opts` | Supports tasks subsystem behavior. |
| 1879 | `M.assign_revenge_interrupt` | module export | `responder, offender_target_id, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1891 | `M.assign_base_camping_permanent` | module export | `squad, smart, reason` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1916 | `hunt_prey_for` | local helper | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1920 | `actor_target_alive` | local helper | `` | Supports tasks subsystem behavior. |
| 1938 | `game_vertex_level_id` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 1946 | `squad_community` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1963 | `same_smart_or_close` | local helper | `squad, target` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1977 | `artefact_offline_collect_ready` | local helper | `squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1994 | `factions_hostile` | local helper | `community_1, community_2` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2002 | `member_server_object` | local helper | `member` | Safely resolves an ALife/server-side object or runtime reference. |
| 2009 | `is_inventory_owner_object` | local helper | `obj` | Supports tasks subsystem behavior. |
| 2024 | `member_inventory_owner_server_object` | local helper | `member` | Safely resolves an ALife/server-side object or runtime reference. |
| 2029 | `force_server_goodwill` | local helper | `source, goodwill, target_id` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 2041 | `force_member_to_actor` | local helper | `member` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2046 | `force_member_to_member` | local helper | `member_1, member_2, goodwill` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2059 | `actor_on_squad_level` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2069 | `current_actor_level_name` | local helper | `` | Resolves level, graph, route, distance, or position data. |
| 2086 | `actor_community_goodwill` | local helper | `community` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 2094 | `set_actor_community_goodwill` | local helper | `community, goodwill` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 2102 | `member_actor_goodwill` | local helper | `member` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 2115 | `restore_member_actor_goodwill` | local helper | `member_id, goodwill` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 2123 | `squad_member_id_set` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2137 | `encode_number_map` | local helper | `map` | Supports tasks subsystem behavior. |
| 2156 | `decode_number_map` | local helper | `value` | Supports tasks subsystem behavior. |
| 2172 | `encode_id_set` | local helper | `set` | Supports tasks subsystem behavior. |
| 2190 | `decode_id_set` | local helper | `value` | Supports tasks subsystem behavior. |
| 2204 | `set_empty` | local helper | `set` | Supports tasks subsystem behavior. |
| 2208 | `persist_actor_revenge_relation_scope` | local helper | `squad, scope` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 2220 | `snapshot_member_actor_goodwill` | local helper | `member, bucket` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 2232 | `for_each_actor_level_squad` | local helper | `fn` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2269 | `snapshot_actor_revenge_relation_scope` | local helper | `squad, scope` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 2304 | `ensure_actor_revenge_relation_scope` | local helper | `squad` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 2333 | `stored_actor_revenge_relation_scope` | local helper | `squad` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 2362 | `restore_actor_revenge_relation_scope` | local helper | `squad, force, include_revenge` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 2386 | `clear_actor_revenge_relation_scope` | local helper | `squad` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 2400 | `same_level_for_hostility` | local helper | `squad, target` | Resolves level, graph, route, distance, or position data. |
| 2408 | `M.apply_revenge_hostility` | module export | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2454 | `M.release_revenge_hostility` | module export | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2468 | `record_offline_combat_loot` | local helper | `squad, target, target_count_before, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 2481 | `M.hunt_offline_tick` | module export | `squad, target, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2535 | `M.hunt_target_valid` | module export | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2577 | `revenge_wait_route` | local helper | `squad, reason` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2585 | `M.revenge_target_valid` | module export | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2645 | `abort_hunt` | local helper | `squad, reason` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2656 | `complete_hunt` | local helper | `squad, mem, target_id, reason` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2673 | `complete_revenge` | local helper | `squad, mem, target_id, reason` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2687 | `complete_populate` | local helper | `squad, target_id` | Supports tasks subsystem behavior. |
| 2699 | `complete_artefact` | local helper | `squad, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2710 | `M.cancel_revenge` | module export | `squad, reason` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2719 | `M.release_artifact_task` | module export | `squad, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2741 | `M.assign_next_task` | module export | `squad, reason` | Supports tasks subsystem behavior. |
| 2766 | `M.update_squad` | module export | `squad, memory` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 3014 | `revenge_script_target_fallback` | local helper | `squad, route_reason` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 3021 | `M.get_script_target` | module export | `squad` | Supports tasks subsystem behavior. |
| 3089 | `M.on_master_disable` | module export | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |

### `gamedata/scripts/zhopa2_topology.script`

Role: level topology, neighbor levels, and route helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 12 | `level_from_object` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 32 | `append_edge` | local helper | `map, source_level, dest_level` | Supports topology subsystem behavior. |
| 48 | `edge_sets_to_arrays` | local helper | `src` | Supports topology subsystem behavior. |
| 67 | `rebuild_neighbors` | local helper | `` | Supports topology subsystem behavior. |
| 81 | `get_utils_stpk` | local helper | `` | Supports topology subsystem behavior. |
| 95 | `get_level_changer_data` | local helper | `se_obj` | Resolves level, graph, route, distance, or position data. |
| 106 | `is_level_changer` | local helper | `se_obj, type_name` | Resolves level, graph, route, distance, or position data. |
| 121 | `remove_level_changer` | local helper | `se_obj` | Resolves level, graph, route, distance, or position data. |
| 150 | `set_level_changer` | local helper | `se_obj` | Resolves level, graph, route, distance, or position data. |
| 176 | `server_entity_on_register` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 182 | `server_entity_on_unregister` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 188 | `rebuild_current_level_changers` | local helper | `` | Resolves level, graph, route, distance, or position data. |
| 211 | `actor_on_first_update` | script hook/global | `` | Runtime hook for topology lifecycle integration. |
| 215 | `on_game_load` | script hook/global | `` | Runtime hook for topology lifecycle integration. |
| 219 | `M.get_level_neighbors` | module export | `level_name` | Resolves level, graph, route, distance, or position data. |
| 226 | `M.get_revision` | module export | `` | Supports topology subsystem behavior. |
| 230 | `M.set_level_changer` | module export | `se_obj` | Resolves level, graph, route, distance, or position data. |
| 234 | `M.remove_level_changer` | module export | `se_obj` | Resolves level, graph, route, distance, or position data. |
| 238 | `M.on_game_start` | module export | `` | Runtime hook for topology lifecycle integration. |
| 257 | `M.on_master_disable` | module export | `` | Stops, cleans, or restarts module-owned runtime state for the MCM master lifecycle. |
| 272 | `on_game_start` | script hook/global | `` | Runtime hook for topology lifecycle integration. |

## Diagnostic Scripts

### `debugscripts/zhopa2_artifact_diag.script`

Role: artifact diag diagnostics or helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 6 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 15 | `log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 26 | `safe_call` | local helper | `obj, fn_name, ...` | Validates safety gates and controlled fallback conditions. |
| 40 | `safe_field` | local helper | `obj, field` | Validates safety gates and controlled fallback conditions. |
| 53 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 64 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 75 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 94 | `named_id` | local helper | `obj_or_id` | Formats names or display text for diagnostics and UI output. |
| 109 | `table_count` | local helper | `t` | Supports artifact diag subsystem behavior. |
| 117 | `sorted_keys` | local helper | `t` | Supports artifact diag subsystem behavior. |
| 128 | `obj_level` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 144 | `current_level_name` | local helper | `` | Resolves level, graph, route, distance, or position data. |
| 154 | `object_position` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 184 | `pos_text` | local helper | `pos` | Formats names or display text for diagnostics and UI output. |
| 191 | `distance_sqr` | local helper | `a, b` | Resolves level, graph, route, distance, or position data. |
| 203 | `dump_artifact_candidate_smarts` | local helper | `idx, artifact_id, art` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 246 | `artifact_valid` | local helper | `idx, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 257 | `dump_storage` | local helper | `` | Supports artifact diag subsystem behavior. |
| 281 | `dump_virtual_zones` | local helper | `idx` | Supports artifact diag subsystem behavior. |
| 315 | `dump_artifacts` | local helper | `idx` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 359 | `dump_simboard_tasks` | local helper | `idx` | Supports artifact diag subsystem behavior. |
| 389 | `M.dump` | module export | `` | Supports artifact diag subsystem behavior. |
| 407 | `M.actor_on_first_update` | module export | `` | Runtime hook for artifact diag lifecycle integration. |
| 415 | `M.on_game_start` | module export | `` | Runtime hook for artifact diag lifecycle integration. |
| 425 | `actor_on_first_update` | script hook/global | `` | Runtime hook for artifact diag lifecycle integration. |
| 429 | `on_game_start` | script hook/global | `` | Runtime hook for artifact diag lifecycle integration. |

### `debugscripts/zhopa2_artifact_flow_diag.script`

Role: artifact flow diag diagnostics or helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 21 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the artifact flow diag subsystem. |
| 30 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 35 | `log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 46 | `tg` | local helper | `` | Supports artifact flow diag subsystem behavior. |
| 50 | `safe_require` | local helper | `name` | Validates safety gates and controlled fallback conditions. |
| 63 | `safe_field` | local helper | `obj, field` | Validates safety gates and controlled fallback conditions. |
| 73 | `safe_call` | local helper | `obj, fn_name, ...` | Validates safety gates and controlled fallback conditions. |
| 82 | `safe_alife_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 91 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 107 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 128 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 144 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 167 | `object_level` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 201 | `object_parent_id` | local helper | `obj` | Supports artifact flow diag subsystem behavior. |
| 212 | `named_id` | local helper | `obj_or_id` | Formats names or display text for diagnostics and UI output. |
| 222 | `bool_text` | local helper | `value` | Formats names or display text for diagnostics and UI output. |
| 226 | `table_count` | local helper | `t` | Supports artifact flow diag subsystem behavior. |
| 234 | `sorted_keys` | local helper | `t` | Supports artifact flow diag subsystem behavior. |
| 245 | `vector_text` | local helper | `pos` | Formats names or display text for diagnostics and UI output. |
| 258 | `object_position` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 273 | `idx_mod` | local helper | `` | Supports artifact flow diag subsystem behavior. |
| 277 | `artifacts_mod` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 281 | `loot_mod` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 285 | `gather_mod` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 289 | `artifact_bucket_memberships` | local helper | `idx, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 301 | `artifact_pos` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 307 | `smart_pos` | local helper | `smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 313 | `squad_pos` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 317 | `artifact_bucket_match` | local helper | `idx, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 327 | `artifact_state` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 354 | `smart_state` | local helper | `smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 369 | `squad_state` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 389 | `looter_squad` | local helper | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 404 | `gather_state` | local helper | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 426 | `storage_gather_state` | local helper | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 431 | `state_mgr_text` | local helper | `npc` | Reads, writes, clears, or migrates serializable runtime state. |
| 439 | `npc_position` | local helper | `npc` | Resolves level, graph, route, distance, or position data. |
| 447 | `online_item_pos` | local helper | `item_id` | Supports artifact flow diag subsystem behavior. |
| 452 | `distance_text` | local helper | `pos_a, pos_b` | Resolves level, graph, route, distance, or position data. |
| 460 | `route_summary` | local helper | `squad, npc, task_smart_id, artifact_id` | Resolves level, graph, route, distance, or position data. |
| 491 | `vertex_state` | local helper | `npc, vid` | Resolves level, graph, route, distance, or position data. |
| 505 | `gather_detail` | local helper | `npc, item_id, st` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 520 | `should_log_gather_execute` | local helper | `npc, st, item_id` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 541 | `patch_table_method` | local helper | `tbl, method, tag, wrapper` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 565 | `patch_global_function` | local helper | `name, wrapper` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 587 | `patch_exported_function` | local helper | `name, tag, wrapper` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 609 | `patch_index` | local helper | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 647 | `patch_artifacts` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 686 | `patch_loot` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 718 | `patch_force_gather` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 750 | `patch_prepare_gather` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 776 | `patch_gather_item` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 802 | `patch_gather_find` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 841 | `patch_gather_evaluate` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 867 | `patch_gather_action` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 942 | `M.dump_all` | module export | `reason` | Supports artifact flow diag subsystem behavior. |
| 989 | `M.install` | module export | `source` | Supports artifact flow diag subsystem behavior. |
| 1024 | `unregister_update` | local helper | `` | Maintains indexed runtime state by adding or removing entries. |
| 1030 | `M.actor_on_update` | module export | `` | Runtime hook for artifact flow diag lifecycle integration. |
| 1051 | `M.actor_on_first_update` | module export | `` | Runtime hook for artifact flow diag lifecycle integration. |
| 1067 | `M.on_game_start` | module export | `` | Runtime hook for artifact flow diag lifecycle integration. |
| 1084 | `actor_on_first_update` | script hook/global | `` | Runtime hook for artifact flow diag lifecycle integration. |
| 1088 | `actor_on_update` | script hook/global | `` | Runtime hook for artifact flow diag lifecycle integration. |
| 1092 | `on_game_start` | script hook/global | `` | Runtime hook for artifact flow diag lifecycle integration. |

### `debugscripts/zhopa2_bucket_diag.script`

Role: bucket diag diagnostics or helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 16 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the bucket diag subsystem. |
| 25 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 30 | `log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 41 | `safe_field` | local helper | `obj, field` | Validates safety gates and controlled fallback conditions. |
| 51 | `safe_call` | local helper | `obj, fn_name, ...` | Validates safety gates and controlled fallback conditions. |
| 60 | `safe_alife_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 69 | `field_value` | local helper | `obj, field` | Supports bucket diag subsystem behavior. |
| 81 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 102 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 131 | `named_id` | local helper | `obj_or_id` | Formats names or display text for diagnostics and UI output. |
| 144 | `table_count` | local helper | `t` | Supports bucket diag subsystem behavior. |
| 155 | `sorted_keys` | local helper | `t` | Supports bucket diag subsystem behavior. |
| 174 | `bucket_stats` | local helper | `bucket` | Supports bucket diag subsystem behavior. |
| 187 | `kind_bucket_stats` | local helper | `kind_bucket` | Supports bucket diag subsystem behavior. |
| 204 | `smart_from_board` | local helper | `board, id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 212 | `squad_from_board` | local helper | `board, id, stored` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 223 | `level_name_for_obj` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 251 | `bool_text` | local helper | `value` | Formats names or display text for diagnostics and UI output. |
| 255 | `flags_text` | local helper | `flags` | Formats names or display text for diagnostics and UI output. |
| 271 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 289 | `storage_by_id` | local helper | `id` | Supports bucket diag subsystem behavior. |
| 294 | `current_action_id` | local helper | `npc` | Supports bucket diag subsystem behavior. |
| 306 | `current_state` | local helper | `npc` | Reads, writes, clears, or migrates serializable runtime state. |
| 314 | `current_point_index` | local helper | `npc` | Supports bucket diag subsystem behavior. |
| 322 | `path_index` | local helper | `npc` | Supports bucket diag subsystem behavior. |
| 330 | `trade_slot_for_npc` | local helper | `smart, npc_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 350 | `binding_state` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 365 | `dump_level_bucket` | local helper | `name, bucket, resolver, level_map` | Resolves level, graph, route, distance, or position data. |
| 403 | `economy_mod` | local helper | `` | Supports bucket diag subsystem behavior. |
| 412 | `smart_id_for_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 416 | `target_id_for_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 423 | `current_smart_for_squad` | local helper | `board, squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 431 | `trade_flags_for_smart` | local helper | `board, smart_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 438 | `trade_state_relevant` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 448 | `pcall_profile` | local helper | `fn, ...` | Supports bucket diag subsystem behavior. |
| 459 | `online_member_count` | local helper | `economy, squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 470 | `dump_trade_squad_candidates` | local helper | `board` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 561 | `dump_prepared_trade_squads` | local helper | `board` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 635 | `dump_kind_bucket` | local helper | `board` | Supports bucket diag subsystem behavior. |
| 664 | `dump_trade_flags` | local helper | `board` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 711 | `dump_board_consistency` | local helper | `board` | Supports bucket diag subsystem behavior. |
| 755 | `dump_index_summary` | local helper | `` | Supports bucket diag subsystem behavior. |
| 788 | `dump_index_buckets` | local helper | `` | Supports bucket diag subsystem behavior. |
| 815 | `M.refresh_simboard_buckets` | module export | `` | Supports bucket diag subsystem behavior. |
| 824 | `M.refresh_trade_buckets` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 840 | `M.dump` | module export | `reason` | Supports bucket diag subsystem behavior. |
| 898 | `M.refresh_and_dump` | module export | `` | Supports bucket diag subsystem behavior. |
| 905 | `now_ms` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 909 | `M.actor_on_update` | module export | `` | Runtime hook for bucket diag lifecycle integration. |
| 931 | `M.actor_on_first_update` | module export | `` | Runtime hook for bucket diag lifecycle integration. |
| 948 | `M.on_game_start` | module export | `` | Runtime hook for bucket diag lifecycle integration. |
| 958 | `actor_on_first_update` | script hook/global | `` | Runtime hook for bucket diag lifecycle integration. |
| 962 | `actor_on_update` | script hook/global | `` | Runtime hook for bucket diag lifecycle integration. |
| 966 | `on_game_start` | script hook/global | `` | Runtime hook for bucket diag lifecycle integration. |

### `debugscripts/zhopa2_loot_loop_diag.script`

Role: loot loop diag diagnostics or helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 29 | `safe_mod` | local helper | `name` | Validates safety gates and controlled fallback conditions. |
| 38 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the loot loop diag subsystem. |
| 42 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 47 | `log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 62 | `tg` | local helper | `` | Supports loot loop diag subsystem behavior. |
| 66 | `safe_field` | local helper | `obj, field` | Validates safety gates and controlled fallback conditions. |
| 76 | `safe_call` | local helper | `obj, fn_name, ...` | Validates safety gates and controlled fallback conditions. |
| 88 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 103 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 119 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 139 | `safe_alife_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 148 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 166 | `named_id` | local helper | `obj_or_id` | Formats names or display text for diagnostics and UI output. |
| 176 | `boolstr` | local helper | `value` | Supports loot loop diag subsystem behavior. |
| 185 | `safe_bool` | local helper | `fn, ...` | Validates safety gates and controlled fallback conditions. |
| 193 | `dist_to_actor` | local helper | `obj` | Supports loot loop diag subsystem behavior. |
| 206 | `object_alive` | local helper | `obj` | Supports loot loop diag subsystem behavior. |
| 211 | `is_stalker` | local helper | `obj` | Supports loot loop diag subsystem behavior. |
| 219 | `is_monster` | local helper | `obj` | Supports loot loop diag subsystem behavior. |
| 227 | `table_count` | local helper | `t` | Supports loot loop diag subsystem behavior. |
| 238 | `list_has` | local helper | `list, id` | Supports loot loop diag subsystem behavior. |
| 251 | `append_unique` | local helper | `list, seen, id` | Supports loot loop diag subsystem behavior. |
| 260 | `short_ids` | local helper | `memory` | Supports loot loop diag subsystem behavior. |
| 281 | `root_storage` | local helper | `id` | Supports loot loop diag subsystem behavior. |
| 286 | `corpse_storage_state` | local helper | `corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 291 | `corpse_detection_state` | local helper | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 296 | `vanilla_has_valuable` | local helper | `corpse_id` | Supports loot loop diag subsystem behavior. |
| 306 | `vanilla_lootable` | local helper | `section` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 312 | `zhopa_corpse_ignored` | local helper | `corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 321 | `zhopa_can_take` | local helper | `section, item, looter` | Validates safety gates and controlled fallback conditions. |
| 330 | `zhopa_protected_corpse` | local helper | `corpse, corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 339 | `section_is_quest` | local helper | `section` | Supports loot loop diag subsystem behavior. |
| 347 | `object_is_story` | local helper | `obj` | Handles story-gated squad events, conversion, migration, or recovery. |
| 356 | `recent_corpse_ids` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 365 | `looter_sample_for_corpse` | local helper | `corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 384 | `corpse_inventory_signature` | local helper | `corpse, looter` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 395 | `inspect_item` | local helper | `owner, item` | Supports loot loop diag subsystem behavior. |
| 441 | `should_log_sig` | local helper | `kind, key, sig, force` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 453 | `dump_corpse` | local helper | `corpse_id, reason, looter, force` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 500 | `dump_npc` | local helper | `npc, reason, force, out_corpses, seen_corpses` | Supports loot loop diag subsystem behavior. |
| 553 | `dump_runtime` | local helper | `reason` | Supports loot loop diag subsystem behavior. |
| 572 | `M.dump` | module export | `reason, force` | Supports loot loop diag subsystem behavior. |
| 609 | `patch_function` | local helper | `mod, fn_name, patch_id, wrapper_factory` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 623 | `M.install` | module export | `` | Supports loot loop diag subsystem behavior. |
| 672 | `M.start_watch` | module export | `duration_ms` | Supports loot loop diag subsystem behavior. |
| 680 | `M.stop_watch` | module export | `` | Supports loot loop diag subsystem behavior. |
| 686 | `M.actor_on_update` | module export | `` | Runtime hook for loot loop diag lifecycle integration. |
| 705 | `M.actor_on_first_update` | module export | `` | Runtime hook for loot loop diag lifecycle integration. |
| 725 | `M.on_game_start` | module export | `` | Runtime hook for loot loop diag lifecycle integration. |
| 735 | `actor_on_update` | script hook/global | `` | Runtime hook for loot loop diag lifecycle integration. |
| 739 | `actor_on_first_update` | script hook/global | `` | Runtime hook for loot loop diag lifecycle integration. |
| 743 | `on_game_start` | script hook/global | `` | Runtime hook for loot loop diag lifecycle integration. |

### `debugscripts/zhopa2_loot_post_job_diag.script`

Role: loot post job diag diagnostics or helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 19 | `safe_mod` | local helper | `name` | Validates safety gates and controlled fallback conditions. |
| 28 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the loot post job diag subsystem. |
| 32 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 40 | `log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 55 | `tg` | local helper | `` | Supports loot post job diag subsystem behavior. |
| 59 | `safe_field` | local helper | `obj, field` | Validates safety gates and controlled fallback conditions. |
| 69 | `safe_call` | local helper | `obj, fn_name, ...` | Validates safety gates and controlled fallback conditions. |
| 81 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 96 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 112 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 132 | `object_label` | local helper | `obj_or_id` | Supports loot post job diag subsystem behavior. |
| 144 | `bool_text` | local helper | `value` | Formats names or display text for diagnostics and UI output. |
| 153 | `safe_alife_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 162 | `server_object_by_id` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 183 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 201 | `smart_by_id` | local helper | `id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 217 | `smart_for_npc` | local helper | `npc_or_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 235 | `object_position_text` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 245 | `object_vertex_text` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 263 | `load_saved_value` | local helper | `obj, key` | Reads, writes, clears, or migrates serializable runtime state. |
| 281 | `current_state_value` | local helper | `npc` | Reads, writes, clears, or migrates serializable runtime state. |
| 299 | `current_action_id` | local helper | `obj` | Supports loot post job diag subsystem behavior. |
| 311 | `current_point_index` | local helper | `obj` | Supports loot post job diag subsystem behavior. |
| 319 | `table_count` | local helper | `t` | Supports loot post job diag subsystem behavior. |
| 330 | `owned_job_sections` | local helper | `smart, npc_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 346 | `smart_info_text` | local helper | `info` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 360 | `gather_text` | local helper | `st` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 375 | `squad_text` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 392 | `arm_trace` | local helper | `npc, source, item, value, reason` | Supports loot post job diag subsystem behavior. |
| 423 | `trace_npc` | local helper | `npc_id, entry, now` | Supports loot post job diag subsystem behavior. |
| 462 | `wrap_record_loot` | local helper | `original` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 480 | `M.install` | module export | `` | Supports loot post job diag subsystem behavior. |
| 502 | `M.uninstall` | module export | `` | Supports loot post job diag subsystem behavior. |
| 515 | `M.actor_on_update` | module export | `` | Runtime hook for loot post job diag lifecycle integration. |
| 543 | `M.actor_on_first_update` | module export | `` | Runtime hook for loot post job diag lifecycle integration. |
| 559 | `M.on_game_start` | module export | `` | Runtime hook for loot post job diag lifecycle integration. |
| 569 | `actor_on_update` | script hook/global | `` | Runtime hook for loot post job diag lifecycle integration. |
| 573 | `actor_on_first_update` | script hook/global | `` | Runtime hook for loot post job diag lifecycle integration. |
| 577 | `on_game_start` | script hook/global | `` | Runtime hook for loot post job diag lifecycle integration. |

### `debugscripts/zhopa2_mutant_diag.script`

Role: mutant diag diagnostics or helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 17 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the mutant diag subsystem. |
| 26 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 31 | `log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 42 | `safe_field` | local helper | `obj, field` | Validates safety gates and controlled fallback conditions. |
| 52 | `safe_call` | local helper | `obj, fn_name, ...` | Validates safety gates and controlled fallback conditions. |
| 64 | `safe_mod` | local helper | `name` | Validates safety gates and controlled fallback conditions. |
| 73 | `safe_alife_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 82 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 97 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 117 | `named_id` | local helper | `obj_or_id` | Formats names or display text for diagnostics and UI output. |
| 123 | `table_count` | local helper | `t` | Supports mutant diag subsystem behavior. |
| 133 | `sorted_keys` | local helper | `t` | Supports mutant diag subsystem behavior. |
| 144 | `join_ids` | local helper | `list, limit` | Supports mutant diag subsystem behavior. |
| 156 | `prop_num` | local helper | `props, key` | Supports mutant diag subsystem behavior. |
| 160 | `smart_mutant_props` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 168 | `smart_flags` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 182 | `obj_level` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 200 | `squad_section_name` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 209 | `squad_player_id` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 220 | `squad_relation_faction` | local helper | `squad` | Reads, applies, snapshots, or restores faction/personal relations through safe ids or validated objects. |
| 231 | `is_monster_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 252 | `mutation_time_state` | local helper | `player_id` | Reads, writes, clears, or migrates serializable runtime state. |
| 262 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 273 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 284 | `runtime_ready_state` | local helper | `context` | Checks the shared runtime readiness barrier before context-dependent work. |
| 304 | `log_runtime` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 319 | `log_cfg` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 333 | `board_smart` | local helper | `board, smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 338 | `bucket_count` | local helper | `bucket` | Supports mutant diag subsystem behavior. |
| 342 | `log_board` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 383 | `list_levels_for` | local helper | `p, squad, mode` | Resolves level, graph, route, distance, or position data. |
| 395 | `count_index_smarts` | local helper | `idx, levels, kind` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 403 | `collect_smarts` | local helper | `p, squad, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 411 | `count_hunt_targets` | local helper | `p, idx, squad, level_name` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 439 | `smart_reject_reason` | local helper | `cfg, squad, smart, level_name` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 472 | `log_smart_sample` | local helper | `squad, level_name` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 501 | `dump_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 617 | `collect_mutant_squads` | local helper | `` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 649 | `M.dump` | module export | `reason` | Supports mutant diag subsystem behavior. |
| 669 | `M.dump_squad` | module export | `squad_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 681 | `now_ms` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 685 | `M.actor_on_update` | module export | `` | Runtime hook for mutant diag lifecycle integration. |
| 716 | `M.actor_on_first_update` | module export | `` | Runtime hook for mutant diag lifecycle integration. |
| 733 | `M.on_game_start` | module export | `` | Runtime hook for mutant diag lifecycle integration. |
| 743 | `actor_on_first_update` | script hook/global | `` | Runtime hook for mutant diag lifecycle integration. |
| 747 | `actor_on_update` | script hook/global | `` | Runtime hook for mutant diag lifecycle integration. |
| 751 | `on_game_start` | script hook/global | `` | Runtime hook for mutant diag lifecycle integration. |

### `debugscripts/zhopa2_offline_inventory_diag.script`

Role: offline inventory diag diagnostics or helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 60 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the offline inventory diag subsystem. |
| 69 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 74 | `log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 85 | `safe_field` | local helper | `obj, field` | Validates safety gates and controlled fallback conditions. |
| 95 | `safe_call` | local helper | `obj, fn_name, ...` | Validates safety gates and controlled fallback conditions. |
| 107 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 122 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 134 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 154 | `object_clsid` | local helper | `obj` | Supports offline inventory diag subsystem behavior. |
| 163 | `named_id` | local helper | `obj_or_id` | Formats names or display text for diagnostics and UI output. |
| 178 | `table_count` | local helper | `t` | Supports offline inventory diag subsystem behavior. |
| 186 | `sorted_keys` | local helper | `t` | Supports offline inventory diag subsystem behavior. |
| 197 | `member_server_object` | local helper | `member` | Safely resolves an ALife/server-side object or runtime reference. |
| 204 | `collect_squad_members` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 216 | `collect_child_ids` | local helper | `se_owner` | Supports offline inventory diag subsystem behavior. |
| 230 | `probe_value` | local helper | `obj, key, call_allowed` | Supports offline inventory diag subsystem behavior. |
| 245 | `probe_write_same` | local helper | `obj, key` | Supports offline inventory diag subsystem behavior. |
| 256 | `dump_owner_probes` | local helper | `se_owner, prefix` | Supports offline inventory diag subsystem behavior. |
| 274 | `dump_item_probes` | local helper | `se_item, prefix` | Supports offline inventory diag subsystem behavior. |
| 307 | `dump_member_inventory` | local helper | `squad, member, member_index` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 350 | `squad_online_state` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 359 | `squad_has_offline_member` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 370 | `M.dump` | module export | `` | Supports offline inventory diag subsystem behavior. |
| 413 | `M.dump_squad` | module export | `squad, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 436 | `M.dump_squad_on_update` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 455 | `M.actor_on_first_update` | module export | `` | Runtime hook for offline inventory diag lifecycle integration. |
| 462 | `M.on_game_start` | module export | `` | Runtime hook for offline inventory diag lifecycle integration. |
| 472 | `actor_on_first_update` | script hook/global | `` | Runtime hook for offline inventory diag lifecycle integration. |
| 476 | `on_game_start` | script hook/global | `` | Runtime hook for offline inventory diag lifecycle integration. |

### `debugscripts/zhopa2_runtime_hud_diag.script`

Role: runtime hud diag diagnostics or helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 6 | `log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 14 | `safe_field` | local helper | `obj, key` | Validates safety gates and controlled fallback conditions. |
| 24 | `safe_method` | local helper | `obj, name, ...` | Validates safety gates and controlled fallback conditions. |
| 32 | `safe_function` | local helper | `fn, ...` | Validates safety gates and controlled fallback conditions. |
| 39 | `safe_mod` | local helper | `name` | Validates safety gates and controlled fallback conditions. |
| 48 | `safe_alife_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 57 | `table_count` | local helper | `value` | Supports runtime hud diag subsystem behavior. |
| 67 | `bool_text` | local helper | `value` | Formats names or display text for diagnostics and UI output. |
| 71 | `current_level_name` | local helper | `` | Resolves level, graph, route, distance, or position data. |
| 79 | `object_story_id` | local helper | `id` | Handles story-gated squad events, conversion, migration, or recovery. |
| 87 | `squad_section` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 96 | `squad_level` | local helper | `squad, perception` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 102 | `squad_members` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 121 | `resolve_squad` | local helper | `key, stored` | Safely resolves an ALife/server-side object or runtime reference. |
| 129 | `cfg_bool` | local helper | `cfg, key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 134 | `quest_state` | local helper | `perception, squad` | Reads, writes, clears, or migrates serializable runtime state. |
| 142 | `rejection_reason` | local helper | `squad, section, members, quest_protected, quest_reason, cfg, can_manage` | Supports runtime hud diag subsystem behavior. |
| 200 | `dump_modules` | local helper | `` | Supports runtime hud diag subsystem behavior. |
| 214 | `dump_buckets` | local helper | `board` | Supports runtime hud diag subsystem behavior. |
| 232 | `M.dump` | module export | `` | Supports runtime hud diag subsystem behavior. |
| 359 | `M.on_key_press` | module export | `key` | Supports runtime hud diag subsystem behavior. |
| 365 | `M.on_game_start` | module export | `` | Runtime hook for runtime hud diag lifecycle integration. |
| 376 | `on_game_start` | script hook/global | `` | Runtime hook for runtime hud diag lifecycle integration. |

### `debugscripts/zhopa2_trade_live_state_diag.script`

Role: trade live state diag diagnostics or helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 22 | `safe_mod` | local helper | `name` | Validates safety gates and controlled fallback conditions. |
| 31 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the trade live state diag subsystem. |
| 35 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 43 | `log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 58 | `tg` | local helper | `` | Supports trade live state diag subsystem behavior. |
| 62 | `safe_field` | local helper | `obj, field` | Validates safety gates and controlled fallback conditions. |
| 72 | `safe_call` | local helper | `obj, fn_name, ...` | Validates safety gates and controlled fallback conditions. |
| 84 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 99 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 115 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 135 | `object_label` | local helper | `obj_or_id` | Supports trade live state diag subsystem behavior. |
| 144 | `bool_text` | local helper | `value` | Formats names or display text for diagnostics and UI output. |
| 153 | `table_count` | local helper | `t` | Supports trade live state diag subsystem behavior. |
| 164 | `safe_alife_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 173 | `server_object_by_id` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 194 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 212 | `smart_by_id` | local helper | `id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 228 | `smart_for_npc` | local helper | `npc_or_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 246 | `squad_for_npc_id` | local helper | `npc_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 255 | `object_position_text` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 265 | `vector_text` | local helper | `pos` | Formats names or display text for diagnostics and UI output. |
| 272 | `load_saved_value` | local helper | `npc, key` | Reads, writes, clears, or migrates serializable runtime state. |
| 280 | `current_state` | local helper | `npc` | Reads, writes, clears, or migrates serializable runtime state. |
| 285 | `current_action_id` | local helper | `npc` | Supports trade live state diag subsystem behavior. |
| 290 | `current_point_index` | local helper | `npc` | Supports trade live state diag subsystem behavior. |
| 295 | `has_info` | local helper | `npc, info` | Supports trade live state diag subsystem behavior. |
| 303 | `beh_trace_text` | local helper | `st` | Formats names or display text for diagnostics and UI output. |
| 337 | `smart_brief` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 341 | `owner_for_job` | local helper | `smart, section` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 348 | `trace_key` | local helper | `npc_id, squad_id` | Supports trade live state diag subsystem behavior. |
| 352 | `M.watch_npc` | module export | `npc_or_id, ctx` | Supports trade live state diag subsystem behavior. |
| 376 | `watch_prepared_squad` | local helper | `squad, source` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 393 | `trace_state` | local helper | `entry, now` | Reads, writes, clears, or migrates serializable runtime state. |
| 455 | `scan_prepared_squads` | local helper | `` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 473 | `M.install` | module export | `` | Supports trade live state diag subsystem behavior. |
| 484 | `economy.try_auto_trade` | assigned wrapper | `squad, reason, opts, ...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 500 | `economy.try_auto_trade_npc` | assigned wrapper | `npc, trader, reason, opts, ...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 520 | `M.uninstall` | module export | `` | Supports trade live state diag subsystem behavior. |
| 537 | `M.actor_on_update` | module export | `` | Runtime hook for trade live state diag lifecycle integration. |
| 565 | `M.actor_on_first_update` | module export | `` | Runtime hook for trade live state diag lifecycle integration. |
| 581 | `M.on_game_start` | module export | `` | Runtime hook for trade live state diag lifecycle integration. |
| 591 | `actor_on_update` | script hook/global | `` | Runtime hook for trade live state diag lifecycle integration. |
| 595 | `actor_on_first_update` | script hook/global | `` | Runtime hook for trade live state diag lifecycle integration. |
| 599 | `on_game_start` | script hook/global | `` | Runtime hook for trade live state diag lifecycle integration. |

### `debugscripts/zhopa2_trade_post_trace_diag.script`

Role: trade post trace diag diagnostics or helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 19 | `safe_mod` | local helper | `name` | Validates safety gates and controlled fallback conditions. |
| 28 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the trade post trace diag subsystem. |
| 32 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 37 | `log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 52 | `tg` | local helper | `` | Supports trade post trace diag subsystem behavior. |
| 56 | `safe_field` | local helper | `obj, field` | Validates safety gates and controlled fallback conditions. |
| 66 | `safe_call` | local helper | `obj, fn_name, ...` | Validates safety gates and controlled fallback conditions. |
| 78 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 93 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 105 | `object_label` | local helper | `obj` | Supports trade post trace diag subsystem behavior. |
| 109 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 127 | `server_object_by_id` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 150 | `smart_by_id` | local helper | `id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 168 | `smart_from_trade_params` | local helper | `params` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 173 | `smart_for_npc` | local helper | `npc_or_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 191 | `bool_text` | local helper | `value` | Formats names or display text for diagnostics and UI output. |
| 195 | `table_count` | local helper | `t` | Supports trade post trace diag subsystem behavior. |
| 206 | `time_left` | local helper | `value, now` | Supports trade post trace diag subsystem behavior. |
| 214 | `object_position_text` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 224 | `object_vertex_text` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 242 | `load_saved_value` | local helper | `obj, key` | Reads, writes, clears, or migrates serializable runtime state. |
| 260 | `current_state_value` | local helper | `npc` | Reads, writes, clears, or migrates serializable runtime state. |
| 278 | `current_action_id` | local helper | `obj` | Supports trade post trace diag subsystem behavior. |
| 290 | `current_point_index` | local helper | `obj` | Supports trade post trace diag subsystem behavior. |
| 298 | `owned_job_sections` | local helper | `smart, npc_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 314 | `gather_text` | local helper | `st` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 329 | `trade_text` | local helper | `st, now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 347 | `squad_text` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 364 | `smart_info_text` | local helper | `info` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 378 | `actual_trade_seller_id` | local helper | `npc_or_id, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 388 | `trace_trade_state` | local helper | `npc_id, entry, now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 432 | `M.trace_after_trade` | module export | `npc_or_id, smart, ctx` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 455 | `M.install` | module export | `` | Supports trade post trace diag subsystem behavior. |
| 463 | `effects.trade_job_sell_items` | assigned wrapper | `actor, npc, params` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 496 | `economy.clear_prepared_trade_job` | assigned wrapper | `smart, npc_id, reason, slot_section` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 519 | `M.uninstall` | module export | `` | Supports trade post trace diag subsystem behavior. |
| 535 | `M.actor_on_update` | module export | `` | Runtime hook for trade post trace diag lifecycle integration. |
| 559 | `M.actor_on_first_update` | module export | `` | Runtime hook for trade post trace diag lifecycle integration. |
| 575 | `M.on_game_start` | module export | `` | Runtime hook for trade post trace diag lifecycle integration. |
| 585 | `actor_on_update` | script hook/global | `` | Runtime hook for trade post trace diag lifecycle integration. |
| 589 | `actor_on_first_update` | script hook/global | `` | Runtime hook for trade post trace diag lifecycle integration. |
| 593 | `on_game_start` | script hook/global | `` | Runtime hook for trade post trace diag lifecycle integration. |

### `debugscripts/zhopa2_trade_route_diag.script`

Role: trade route diag diagnostics or helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 35 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the trade route diag subsystem. |
| 44 | `safe_mod` | local helper | `name` | Validates safety gates and controlled fallback conditions. |
| 53 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 58 | `log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 69 | `can_log` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 77 | `tg` | local helper | `` | Supports trade route diag subsystem behavior. |
| 81 | `bounded_log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 87 | `priority_log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 95 | `safe_field` | local helper | `obj, field` | Validates safety gates and controlled fallback conditions. |
| 105 | `safe_call` | local helper | `obj, fn_name, ...` | Validates safety gates and controlled fallback conditions. |
| 117 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 132 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 144 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 164 | `safe_alife_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 173 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 191 | `item_price` | local helper | `item` | Supports trade route diag subsystem behavior. |
| 214 | `section_has_prefix` | local helper | `section, prefix` | Supports trade route diag subsystem behavior. |
| 218 | `is_artifact_item` | local helper | `item, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 230 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 238 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 246 | `join` | local helper | `list, limit` | Supports trade route diag subsystem behavior. |
| 262 | `table_count` | local helper | `t` | Supports trade route diag subsystem behavior. |
| 270 | `sorted_keys` | local helper | `t` | Supports trade route diag subsystem behavior. |
| 281 | `squad_matches` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 296 | `is_post_rest_reason` | local helper | `reason` | Supports trade route diag subsystem behavior. |
| 300 | `current_level_for_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 319 | `M.stalker_trade_diag_squad` | module export | `squad` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 330 | `route_levels_for_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 343 | `smart_brief` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 350 | `squad_brief` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 357 | `smart_by_id` | local helper | `id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 373 | `current_action_id` | local helper | `npc` | Supports trade route diag subsystem behavior. |
| 385 | `current_state` | local helper | `npc` | Reads, writes, clears, or migrates serializable runtime state. |
| 393 | `current_point_index` | local helper | `npc` | Supports trade route diag subsystem behavior. |
| 401 | `path_index` | local helper | `npc` | Supports trade route diag subsystem behavior. |
| 409 | `dump_beh_runtime_snapshot` | local helper | `smart, npc, st, job, stage` | Supports trade route diag subsystem behavior. |
| 410 | `ini_string` | local helper | `ini, section, field` | Supports trade route diag subsystem behavior. |
| 417 | `pos_brief` | local helper | `pos` | Supports trade route diag subsystem behavior. |
| 429 | `npc_pos` | local helper | `` | Supports trade route diag subsystem behavior. |
| 436 | `npc_vertex` | local helper | `fn_name` | Resolves level, graph, route, distance, or position data. |
| 443 | `parse_pt_pos` | local helper | `line` | Supports trade route diag subsystem behavior. |
| 454 | `dist_to_pt` | local helper | `pos, line` | Supports trade route diag subsystem behavior. |
| 469 | `reached` | local helper | `index` | Supports trade route diag subsystem behavior. |
| 476 | `target_brief` | local helper | `target` | Supports trade route diag subsystem behavior. |
| 490 | `npc_info` | local helper | `info` | Supports trade route diag subsystem behavior. |
| 497 | `npc_name` | local helper | `` | Formats names or display text for diagnostics and UI output. |
| 506 | `pathpoint` | local helper | `index` | Supports trade route diag subsystem behavior. |
| 577 | `has_info` | local helper | `npc, info` | Supports trade route diag subsystem behavior. |
| 585 | `brief_target_value` | local helper | `value` | Supports trade route diag subsystem behavior. |
| 602 | `brief_state_arg` | local helper | `arg` | Reads, writes, clears, or migrates serializable runtime state. |
| 631 | `mark_trade_npc_for_state_watch` | local helper | `npc_id, role, squad_id, trader_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 644 | `trade_state_watch_info` | local helper | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 664 | `service_slot_for_npc` | local helper | `smart, npc_id` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 684 | `lower_text` | local helper | `value` | Formats names or display text for diagnostics and UI output. |
| 688 | `contains_plain` | local helper | `value, needle` | Supports trade route diag subsystem behavior. |
| 693 | `job_section` | local helper | `job` | Resolves a safe section name for runtime classification. |
| 700 | `job_ini_string` | local helper | `job, smart, field` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 719 | `job_is_trade_customer` | local helper | `job, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 728 | `provider_role` | local helper | `job, smart` | Supports trade route diag subsystem behavior. |
| 757 | `find_trade_customer_job_diag` | local helper | `smart, npc_id` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 778 | `first_trade_provider_diag` | local helper | `smart, ignore_ids` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 805 | `binding_state` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 825 | `log_binding` | local helper | `stage, reason` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 835 | `unwrap_effect_wrappers` | local helper | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 845 | `M.trade_job_sell_items_diag_wrapper` | module export | `actor, npc, params` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 860 | `M.trade_job_give_id_diag_wrapper` | module export | `actor, npc, params` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 875 | `install_effect_wrappers` | local helper | `reason` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 892 | `prepared_signature` | local helper | `squad` | Supports trade route diag subsystem behavior. |
| 908 | `dump_prepared_snapshot` | local helper | `squad, stage, reason` | Supports trade route diag subsystem behavior. |
| 992 | `member_ids` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1007 | `online_members` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1026 | `inventory_scan` | local helper | `npc` | Supports trade route diag subsystem behavior. |
| 1036 | `scan` | local helper | `_, item` | Supports trade route diag subsystem behavior. |
| 1051 | `sell_plan_summary` | local helper | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1085 | `dump_members` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1111 | `id_set` | local helper | `ids` | Supports trade route diag subsystem behavior. |
| 1119 | `plain_online_members` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1131 | `dump_trade_job_candidates` | local helper | `smart, stage, wanted_npc_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1184 | `dump_trade_intent_snapshot` | local helper | `squad, stage, reason, result_reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1268 | `registry_weight` | local helper | `entry, squad, context` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1291 | `dump_registry_weights` | local helper | `squad, reason` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1311 | `dump_trade_profile` | local helper | `squad, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1339 | `dump_route_candidates` | local helper | `squad` | Resolves level, graph, route, distance, or position data. |
| 1380 | `M.dump_squad` | module export | `squad, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1418 | `M.dump_squad_id` | module export | `squad_id, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1427 | `squad_from_board` | local helper | `id, stored` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1434 | `M.dump_all` | module export | `reason` | Supports trade route diag subsystem behavior. |
| 1465 | `patch_tasks` | local helper | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 1475 | `tasks.assign_next_task` | assigned wrapper | `squad, reason, ...` | Supports trade route diag subsystem behavior. |
| 1496 | `patch_economy` | local helper | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 1504 | `economy.trade_route_task_weight` | assigned wrapper | `squad, base_weight, opts, ...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1525 | `economy.patch_trade_effect` | assigned wrapper | `...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1537 | `economy.patch_trade_condition` | assigned wrapper | `...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1547 | `economy.try_auto_trade` | assigned wrapper | `squad, reason, opts, ...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1577 | `economy.try_auto_trade_npc` | assigned wrapper | `npc, trader, reason, opts, ...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1606 | `patch_state_mgr` | local helper | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 1615 | `state_mgr.set_state` | assigned wrapper | `npc, state_name, callback, timeout, target, extra, ...` | Reads, writes, clears, or migrates serializable runtime state. |
| 1654 | `M.install` | module export | `` | Supports trade route diag subsystem behavior. |
| 1668 | `unregister_update` | local helper | `` | Maintains indexed runtime state by adding or removing entries. |
| 1674 | `M.watch_prepared_trades` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1708 | `M.actor_on_update` | module export | `` | Runtime hook for trade route diag lifecycle integration. |
| 1732 | `M.actor_on_first_update` | module export | `` | Runtime hook for trade route diag lifecycle integration. |
| 1748 | `M.on_game_start` | module export | `` | Runtime hook for trade route diag lifecycle integration. |
| 1761 | `actor_on_first_update` | script hook/global | `` | Runtime hook for trade route diag lifecycle integration. |
| 1765 | `actor_on_update` | script hook/global | `` | Runtime hook for trade route diag lifecycle integration. |
| 1769 | `on_game_start` | script hook/global | `` | Runtime hook for trade route diag lifecycle integration. |

### `debugscripts/zhopa2_trade_smart_diag.script`

Role: trade smart diag diagnostics or helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 17 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the trade smart diag subsystem. |
| 26 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 31 | `log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 42 | `safe_field` | local helper | `obj, field` | Validates safety gates and controlled fallback conditions. |
| 52 | `safe_call` | local helper | `obj, fn_name, ...` | Validates safety gates and controlled fallback conditions. |
| 64 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 79 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 91 | `safe_alife_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 100 | `named_id` | local helper | `obj_or_id` | Formats names or display text for diagnostics and UI output. |
| 115 | `table_count` | local helper | `t` | Supports trade smart diag subsystem behavior. |
| 123 | `sorted_keys` | local helper | `t` | Supports trade smart diag subsystem behavior. |
| 134 | `now_ms` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 144 | `level_name` | local helper | `` | Resolves level, graph, route, distance, or position data. |
| 154 | `trim` | local helper | `value` | Supports trade smart diag subsystem behavior. |
| 161 | `smart_cfg_filename` | local helper | `smart` | Reads or normalizes configuration data for the trade smart diag subsystem. |
| 179 | `open_ini` | local helper | `path` | Supports trade smart diag subsystem behavior. |
| 188 | `smart_ini` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 200 | `section_line_count` | local helper | `ini, section` | Supports trade smart diag subsystem behavior. |
| 212 | `obj_level` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 235 | `smart_from_board` | local helper | `board, smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 250 | `smart_jobs_count` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 258 | `flag_text` | local helper | `flags` | Formats names or display text for diagnostics and UI output. |
| 272 | `lower_text` | local helper | `value` | Formats names or display text for diagnostics and UI output. |
| 276 | `contains_plain` | local helper | `value, needle` | Supports trade smart diag subsystem behavior. |
| 281 | `job_field` | local helper | `job, field` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 288 | `job_section` | local helper | `job` | Resolves a safe section name for runtime classification. |
| 292 | `job_suitable` | local helper | `job, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 317 | `job_is_trade_customer` | local helper | `job, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 325 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 343 | `storage_by_id` | local helper | `id` | Supports trade smart diag subsystem behavior. |
| 348 | `current_action_id` | local helper | `npc` | Supports trade smart diag subsystem behavior. |
| 360 | `current_state` | local helper | `npc` | Reads, writes, clears, or migrates serializable runtime state. |
| 368 | `current_point_index` | local helper | `npc` | Supports trade smart diag subsystem behavior. |
| 376 | `path_index` | local helper | `npc` | Supports trade smart diag subsystem behavior. |
| 384 | `binding_state` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 399 | `route_bucket_count` | local helper | `buckets` | Resolves level, graph, route, distance, or position data. |
| 409 | `flag_counts` | local helper | `flags_by_smart` | Supports trade smart diag subsystem behavior. |
| 439 | `dump_service_slots_for_smart` | local helper | `smart, tag` | Handles service-provider classification, customer intent, completion, or smart-job recovery. |
| 490 | `dump_route_buckets` | local helper | `board` | Resolves level, graph, route, distance, or position data. |
| 525 | `dump_flagged_smarts` | local helper | `board` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 556 | `M.dump` | module export | `reason` | Supports trade smart diag subsystem behavior. |
| 595 | `M.refresh_trade_smart_index` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 611 | `M.refresh_and_dump` | module export | `` | Supports trade smart diag subsystem behavior. |
| 617 | `unregister_update` | local helper | `` | Maintains indexed runtime state by adding or removing entries. |
| 623 | `M.actor_on_update` | module export | `` | Runtime hook for trade smart diag lifecycle integration. |
| 642 | `M.actor_on_first_update` | module export | `` | Runtime hook for trade smart diag lifecycle integration. |
| 662 | `M.on_game_start` | module export | `` | Runtime hook for trade smart diag lifecycle integration. |
| 675 | `actor_on_first_update` | script hook/global | `` | Runtime hook for trade smart diag lifecycle integration. |
| 679 | `actor_on_update` | script hook/global | `` | Runtime hook for trade smart diag lifecycle integration. |
| 683 | `on_game_start` | script hook/global | `` | Runtime hook for trade smart diag lifecycle integration. |
