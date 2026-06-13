# Z.H.O.P.A. ALIFE 2.0 Function Reference

[Architecture document](zhopa_alife_2_design_document_en.md)

This document is generated from the current ZHOPA ALIFE 2.0 Lua sources. It lists named function declarations and named function assignments found in runtime scripts under `gamedata/scripts` and diagnostic scripts under `debugscripts`. Anonymous inline closures, for example `pcall(function() ... end)`, are intentionally excluded because they have no standalone callable contract.

Regenerate it with:

```bash
python tools/generate_function_reference.py
```

- Runtime script functions: 1540
- Diagnostic script functions: 428
- Total documented named functions: 1968

## Reading Notes

- **Kind** describes how the function is declared: local helper, module export, script hook/global, or assigned wrapper.
- **Parameters** are copied from the declaration line and may omit internal closures or later vararg handling.
- **Description** is a short generated operational summary based on the function name and module role. The Lua source remains the final authority for exact behavior and edge cases.

## Runtime Scripts

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
| 89 | `runtime_ready` | local helper | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 101 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 118 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 137 | `object_clsid` | local helper | `obj` | Supports artifacts subsystem behavior. |
| 148 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 157 | `object_position` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 165 | `object_is_artifact` | local helper | `obj` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 170 | `item_cost` | local helper | `obj_or_section` | Supports artifacts subsystem behavior. |
| 190 | `artifact_valid` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 208 | `artifact_same_level_as_squad` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 225 | `artifact_target_blacklisted` | local helper | `squad, smart` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 241 | `artifact_id_target_blacklisted` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 257 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 264 | `named_id` | local helper | `id` | Formats names or display text for diagnostics and UI output. |
| 277 | `bool_text` | local helper | `value` | Formats names or display text for diagnostics and UI output. |
| 281 | `artifact_bucket_debug` | local helper | `idx, smart_id, focus_id` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 314 | `artifact_pool_debug` | local helper | `idx` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 334 | `artifact_object_debug` | local helper | `idx, artifact_id` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 358 | `debug_artifact_error` | local helper | `squad, reason, artifact_id, npc, extra` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 395 | `debug_artifact_offline_success` | local helper | `squad, artifact_id, section` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 412 | `squad_has_artifact_cargo` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 417 | `squad_member_server` | local helper | `squad, prefer_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 436 | `squad_member_online_object` | local helper | `member` | Resolves an online game object through db.storage or level lookups. |
| 448 | `squad_member_alive_online` | local helper | `obj` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 456 | `add_online_looter` | local helper | `list, seen, obj` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 464 | `squad_online_looters` | local helper | `squad, prefer_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 479 | `release_artifact_reservation` | local helper | `squad, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 487 | `add_artifact_cargo` | local helper | `squad, section, value, artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 501 | `reset_online_target_tracking` | local helper | `squad` | Clears transient state, reservations, or stale runtime references. |
| 511 | `clear_online_approach_fields` | local helper | `squad` | Clears transient state, reservations, or stale runtime references. |
| 529 | `remember_artifact_reservation` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 551 | `sync_task_artifact_metadata` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 591 | `artifact_matches_task_smart` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 606 | `artifact_from_task_smart` | local helper | `squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 629 | `recover_task_artifact_id` | local helper | `squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 648 | `cancel_online_pickup` | local helper | `squad` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 658 | `recover_vanilla_artifact_pickup` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 667 | `online_inventory_recovery_pending` | local helper | `squad` | Supports artifacts subsystem behavior. |
| 690 | `clear_online_pickup_state` | local helper | `squad` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 706 | `retarget_missing_artifact_to_current_smart` | local helper | `squad, old_artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 740 | `stale_virtual_artifact_id` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 749 | `gather_item_active` | local helper | `npc, artifact_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 759 | `gather_item_failure_reason` | local helper | `npc, artifact_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 769 | `gather_item_debug_status` | local helper | `npc, artifact_id` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 779 | `pickup_stalled` | local helper | `squad, npc, now` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 827 | `online_pickup_pending` | local helper | `squad, artifact_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 859 | `online_arrived_idle_timeout` | local helper | `squad, artifact_id, reason, allow_started` | Supports artifacts subsystem behavior. |
| 893 | `current_artifact_id` | assigned wrapper | `squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 911 | `online_artifact_pickup_ready` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 929 | `all_failures_contested` | local helper | `failures` | Supports artifacts subsystem behavior. |
| 941 | `call_parent_zone_take` | local helper | `se_artifact` | Supports artifacts subsystem behavior. |
| 955 | `release_ground_artifact` | local helper | `se_artifact` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 965 | `virtual_artifact_data` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 973 | `unregister_virtual_artifact` | local helper | `artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 981 | `materialize_virtual_artifact_online` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1005 | `M.release_reservation` | module export | `squad, reason` | Clears transient state, reservations, or stale runtime references. |
| 1009 | `M.pick_target` | module export | `squad, opts` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1069 | `M.offline_collect` | module export | `squad, artifact_id, reason` | Supports artifacts subsystem behavior. |
| 1125 | `M.offline_collect_virtual` | module export | `squad, artifact_id, reason` | Supports artifacts subsystem behavior. |
| 1180 | `M.try_collect` | module export | `squad` | Supports artifacts subsystem behavior. |
| 1345 | `M.complete` | module export | `squad, reason` | Supports artifacts subsystem behavior. |
| 1356 | `M.on_game_start` | module export | `` | Runtime hook for artifacts lifecycle integration. |
| 1361 | `on_game_start` | script hook/global | `` | Runtime hook for artifacts lifecycle integration. |

### `gamedata/scripts/zhopa2_bootstrap.script`

Role: minimal startup bridge into the runtime patch orchestrator.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 1 | `runtime_patches` | local helper | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 12 | `on_game_start` | script hook/global | `` | Runtime hook for bootstrap lifecycle integration. |

### `gamedata/scripts/zhopa2_cfg.script`

Role: configuration, MCM defaults, faction aliases, and blacklist access.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 82 | `section_faction` | local helper | `section` | Supports cfg subsystem behavior. |
| 90 | `squad_section_name` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 108 | `squad_faction` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 119 | `is_monster_or_zombied` | local helper | `squad` | Handles story-gated squad events, conversion, migration, or recovery. |
| 135 | `bool_from_value` | local helper | `v, default` | Supports cfg subsystem behavior. |
| 146 | `mcm_path_for_key` | local helper | `key` | Supports cfg subsystem behavior. |
| 154 | `read_mcm` | local helper | `key` | Supports cfg subsystem behavior. |
| 172 | `read_ltx` | local helper | `key, default` | Supports cfg subsystem behavior. |
| 186 | `get` | script hook/global | `key, default` | Supports cfg subsystem behavior. |
| 199 | `get_bool` | script hook/global | `key, default` | Supports cfg subsystem behavior. |
| 203 | `get_num` | script hook/global | `key, default` | Supports cfg subsystem behavior. |
| 207 | `get_string` | script hook/global | `key, default` | Supports cfg subsystem behavior. |
| 212 | `get_faction_alias` | script hook/global | `faction` | Supports cfg subsystem behavior. |
| 220 | `reset_blacklist_cache` | local helper | `` | Validates safety gates and controlled fallback conditions. |
| 225 | `cache_key` | local helper | `section, key` | Supports cfg subsystem behavior. |
| 229 | `section_value` | local helper | `section, key` | Supports cfg subsystem behavior. |
| 243 | `list_set` | local helper | `value` | Supports cfg subsystem behavior. |
| 263 | `section_set` | local helper | `section, key` | Supports cfg subsystem behavior. |
| 274 | `section_has` | local helper | `section, key, value` | Supports cfg subsystem behavior. |
| 285 | `section_is_true` | local helper | `section, key` | Supports cfg subsystem behavior. |
| 290 | `smart_name_for_blacklist` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 311 | `is_global_level_blacklisted` | script hook/global | `level_name` | Validates safety gates and controlled fallback conditions. |
| 315 | `is_level_blacklisted_for_squad` | script hook/global | `squad, level_name` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 338 | `is_smart_blacklisted_for_squad` | script hook/global | `squad, smart, level_name` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 370 | `reload` | script hook/global | `` | Reads, writes, clears, or migrates serializable runtime state. |

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

### `gamedata/scripts/zhopa2_economy.script`

Role: online/offline trade policy, sellable inventory scanning, virtual cargo, and trade routing.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 57 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the economy subsystem. |
| 66 | `M.perception_mod` | module export | `` | Supports economy subsystem behavior. |
| 75 | `runtime_mod` | local helper | `` | Supports economy subsystem behavior. |
| 84 | `memory_mod` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 93 | `runtime_ready` | local helper | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 105 | `runtime_not_ready_reason` | local helper | `` | Supports economy subsystem behavior. |
| 117 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 125 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 129 | `M.enabled` | module export | `` | Supports economy subsystem behavior. |
| 133 | `M.squad_trade_allowed` | module export | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 150 | `tg` | local helper | `` | Supports economy subsystem behavior. |
| 154 | `ensure_trade_ini` | local helper | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 174 | `clear_table` | local helper | `t` | Clears transient state, reservations, or stale runtime references. |
| 183 | `slower` | local helper | `value` | Supports economy subsystem behavior. |
| 187 | `contains_plain` | local helper | `haystack, needle` | Supports economy subsystem behavior. |
| 191 | `M.emit_trade_event_text` | module export | `text` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 212 | `M.queue_trade_event` | module export | `text` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 219 | `M.flush_trade_events` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 231 | `M.print_trade_event` | module export | `fmt, ...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 244 | `print_trade_error` | local helper | `fmt, ...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 255 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 278 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 297 | `object_clsid` | local helper | `obj` | Supports economy subsystem behavior. |
| 313 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 332 | `M.is_squad_object` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 341 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 352 | `server_object_by_id` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 360 | `live_object` | local helper | `obj` | Supports economy subsystem behavior. |
| 373 | `read_ini_string_from` | local helper | `ini, section, key` | Supports economy subsystem behavior. |
| 391 | `read_job_ini_string` | local helper | `job_or_section, key, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 414 | `find_smart_job_by_section` | local helper | `smart, section` | Resolves a safe section name for runtime classification. |
| 428 | `item_in_slots` | local helper | `npc, item_id` | Supports economy subsystem behavior. |
| 441 | `active_item` | local helper | `npc` | Supports economy subsystem behavior. |
| 454 | `best_weapon` | local helper | `npc` | Supports economy subsystem behavior. |
| 464 | `active_item_id` | local helper | `npc` | Supports economy subsystem behavior. |
| 468 | `buy_sell_params` | local helper | `section` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 520 | `sys_string` | local helper | `section, key` | Supports economy subsystem behavior. |
| 531 | `sys_float` | local helper | `section, key, default` | Supports economy subsystem behavior. |
| 542 | `is_item_type` | local helper | `typ, section, obj` | Supports economy subsystem behavior. |
| 553 | `object_is_weapon` | local helper | `item` | Supports economy subsystem behavior. |
| 561 | `object_is_outfit` | local helper | `item` | Supports economy subsystem behavior. |
| 569 | `object_is_headgear` | local helper | `item` | Supports economy subsystem behavior. |
| 577 | `item_kind` | local helper | `section` | Supports economy subsystem behavior. |
| 581 | `section_has_prefix` | local helper | `section, prefix` | Supports economy subsystem behavior. |
| 585 | `section_contains` | local helper | `section, needle` | Supports economy subsystem behavior. |
| 589 | `M.npc_sell_price_multiplier` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 599 | `item_condition` | local helper | `item` | Supports economy subsystem behavior. |
| 626 | `item_cost` | local helper | `item, section` | Supports economy subsystem behavior. |
| 642 | `section_is_ammo` | local helper | `section` | Supports economy subsystem behavior. |
| 646 | `section_is_degraded_ammo` | local helper | `section` | Supports economy subsystem behavior. |
| 650 | `section_is_clean_buckshot` | local helper | `section` | Supports economy subsystem behavior. |
| 657 | `section_is_clean_fmj` | local helper | `section` | Supports economy subsystem behavior. |
| 663 | `section_is_disfavored_fallback_ammo` | local helper | `section` | Supports economy subsystem behavior. |
| 678 | `section_is_needed_ammo` | local helper | `section, needed_ammo` | Supports economy subsystem behavior. |
| 682 | `ammo_candidate` | local helper | `section` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 689 | `pick_buy_ammo` | local helper | `weapon_ammo` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 715 | `preferred_ammo_for_weapon_section` | local helper | `weapon_section` | Resolves a safe section name for runtime classification. |
| 726 | `needed_ammo_for_npc` | local helper | `npc` | Supports economy subsystem behavior. |
| 734 | `add_weapon_ammo` | local helper | `weapon` | Maintains indexed runtime state by adding or removing entries. |
| 764 | `section_is_grenade` | local helper | `section` | Supports economy subsystem behavior. |
| 772 | `section_is_bandage` | local helper | `section` | Supports economy subsystem behavior. |
| 776 | `section_is_medkit` | local helper | `section` | Supports economy subsystem behavior. |
| 780 | `section_is_other_med` | local helper | `section` | Supports economy subsystem behavior. |
| 807 | `section_is_food` | local helper | `section` | Supports economy subsystem behavior. |
| 814 | `section_is_drink` | local helper | `section` | Supports economy subsystem behavior. |
| 824 | `section_is_never_sell` | local helper | `section, item` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 835 | `section_is_upgrade` | local helper | `section` | Supports economy subsystem behavior. |
| 839 | `section_is_artifact` | local helper | `section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 843 | `section_is_mutant_part` | local helper | `section` | Supports economy subsystem behavior. |
| 848 | `trade_smart_for_npc` | local helper | `npc, params` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 861 | `trade_seller_for_npc` | local helper | `npc, params` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 890 | `add_plan_item` | local helper | `plan, item, section, reason` | Maintains indexed runtime state by adding or removing entries. |
| 898 | `mark_surplus` | local helper | `entries, keep_count, plan, reason` | Supports economy subsystem behavior. |
| 910 | `classify_provider_job_role` | local helper | `job_or_section, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 977 | `resolve_npc_provider_role` | local helper | `npc, smart, npc_id` | Safely resolves an ALife/server-side object or runtime reference. |
| 1005 | `M.provider_role` | module export | `npc, smart` | Supports economy subsystem behavior. |
| 1009 | `npc_service_candidate_blocked` | local helper | `npc, npc_id, params` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1034 | `npc_is_trade_provider` | local helper | `npc, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1062 | `M.build_online_sell_plan` | module export | `npc, params` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1090 | `add_generic` | local helper | `item, section, params` | Maintains indexed runtime state by adding or removing entries. |
| 1106 | `scan` | local helper | `_, item` | Supports economy subsystem behavior. |
| 1209 | `M.online_trade_sell_item_price` | module export | `npc, trader, item` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1221 | `M.online_trade_buy_item_price` | module export | `npc, trader, item` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1233 | `M.online_trade_buy_section_price` | module export | `section` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1242 | `sell_plan_should_start_auto_trade` | local helper | `npc, plan` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1259 | `inventory_section_counts` | local helper | `npc` | Supports economy subsystem behavior. |
| 1264 | `scan` | local helper | `_, item` | Supports economy subsystem behavior. |
| 1274 | `npc_money` | local helper | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1284 | `transfer_money_between` | local helper | `from_npc, to_npc, amount` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1296 | `transfer_all_money_to` | local helper | `from_npc, to_npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1304 | `transfer_trade_money` | local helper | `npc, trader, price` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1312 | `spawn_trade_item_to_npc` | local helper | `npc, section` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1320 | `dynamic_news_nearby_activity_enabled` | local helper | `` | Supports economy subsystem behavior. |
| 1328 | `emit_bought_items_news` | local helper | `npc, trader, bought_items` | Supports economy subsystem behavior. |
| 1346 | `buy_missing_section` | local helper | `npc, trader, section, target_count, counts, payer, bought_items` | Resolves a safe section name for runtime classification. |
| 1373 | `ammo_buy_target` | local helper | `bs` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1381 | `M.execute_online_buy` | module export | `npc, trader, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1412 | `build_online_buy_needs` | local helper | `npc, counts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1415 | `add_need` | local helper | `section, target` | Maintains indexed runtime state by adding or removing entries. |
| 1435 | `offline_round_money` | local helper | `amount` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1440 | `virtual_money` | local helper | `squad` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 1448 | `add_virtual_money` | local helper | `squad, amount, reason` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 1465 | `take_virtual_money` | local helper | `squad, amount, reason` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 1482 | `offline_trade_item_price` | local helper | `item` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1490 | `offline_buy_section_price` | local helper | `section` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1494 | `offline_collect_members` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1521 | `offline_member_children` | local helper | `member` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1538 | `offline_collect_wallet` | local helper | `squad` | Supports economy subsystem behavior. |
| 1542 | `virtual_loot_raw_value` | local helper | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 1550 | `virtual_loot_count` | local helper | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 1558 | `virtual_loot_sell_price` | local helper | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 1562 | `virtual_loot_detail` | local helper | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 1580 | `clear_virtual_loot` | local helper | `squad, reason` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 1595 | `give_online_trade_money` | local helper | `npc, amount` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1607 | `materialize_virtual_money_to_npc` | local helper | `squad, npc, reason` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 1620 | `execute_virtual_squad_sale` | local helper | `squad, pay_to, trader, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1651 | `section_is_weapon_entry` | local helper | `section, item` | Supports economy subsystem behavior. |
| 1660 | `section_is_outfit_entry` | local helper | `section, item` | Supports economy subsystem behavior. |
| 1672 | `section_is_headgear_entry` | local helper | `section, item` | Supports economy subsystem behavior. |
| 1685 | `offline_gear_score` | local helper | `item, section, ammo_counts` | Supports economy subsystem behavior. |
| 1694 | `offline_best_gear` | local helper | `member, children` | Supports economy subsystem behavior. |
| 1710 | `add_candidate` | local helper | `list, item, section` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1737 | `keep_best` | local helper | `list` | Supports economy subsystem behavior. |
| 1760 | `add_ammo` | local helper | `entry` | Maintains indexed runtime state by adding or removing entries. |
| 1771 | `offline_needed_ammo_for_gear` | local helper | `gear` | Supports economy subsystem behavior. |
| 1775 | `offline_build_sell_plan` | local helper | `members` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1789 | `add_member_plan` | local helper | `item, section, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1850 | `offline_sell_plan_should_start` | local helper | `plan` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1866 | `offline_build_buy_needs` | local helper | `members` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1880 | `add_need` | local helper | `section, target` | Maintains indexed runtime state by adding or removing entries. |
| 1899 | `trade_path.clear_offline_trade_profile_cache` | assigned wrapper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1906 | `trade_path.cleanup_offline_trade_profile_cache` | assigned wrapper | `now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1919 | `trade_path.offline_sell_plan_value` | assigned wrapper | `plan` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1927 | `trade_path.offline_needs_value` | assigned wrapper | `needs` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1935 | `trade_path.offline_trade_profile_needs` | assigned wrapper | `profile` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1942 | `trade_path.offline_trade_profile_for_squad` | assigned wrapper | `squad, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2014 | `offline_trade_detail_list` | local helper | `entries, field, max_count` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2030 | `set_offline_trade_detail` | local helper | `squad, result, members, plan, wallet, needs` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2052 | `execute_offline_sell_plan` | local helper | `plan, squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2080 | `execute_offline_buy_needs` | local helper | `squad, members, needs` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2118 | `M.offline_squad_has_trade_work` | module export | `squad, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2130 | `M.execute_offline_squad_trade` | module export | `squad, smart, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2181 | `clear_npc_trade_state` | local helper | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2200 | `suppress_npc_trade_state` | local helper | `npc, until_tg` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2211 | `trade_context_active` | local helper | `st` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2215 | `squad_accepts_managed_trade_signal` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2219 | `squad_for_online_npc` | local helper | `npc` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2232 | `squad_for_spawned_npc` | local helper | `npc, se_obj` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2243 | `M.materialize_online_virtual_money` | module export | `npc, squad, reason` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 2254 | `set_trade_job_idle` | local helper | `npc, params` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2264 | `execute_online_sell_only` | local helper | `npc, trader, params, collect_to` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2307 | `M.execute_online_trade_with_trader` | module export | `npc, trader, params, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2332 | `M.execute_online_trade` | module export | `npc, params, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2341 | `squad_member_id_set` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2358 | `trade_result_terminal` | local helper | `result` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2366 | `clear_squad_prepared_trade_state` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2377 | `finalize_squad_trade_task` | local helper | `squad, result, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2398 | `mark_squad_trade_result` | assigned wrapper | `squad, result, reason, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2413 | `online_squad_trade_members` | local helper | `squad, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2431 | `online_trade_members_from_ids` | local helper | `member_ids` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2445 | `squad_trade_member_ids` | local helper | `members` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2456 | `trade_member_ids_count` | local helper | `member_ids` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2460 | `ensure_trade_source_member` | local helper | `members, source_npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2479 | `find_online_squad_trade_npc` | local helper | `squad, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2484 | `squad_members_money` | local helper | `members` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2492 | `squad_members_have_trade_work` | local helper | `members, squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2520 | `M._online_squad_members` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2538 | `M._online_trade_profile` | module export | `members, squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2584 | `M._offline_trade_profile` | module export | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2589 | `M.squad_trade_route_profile` | module export | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2603 | `find_online_trader_at_smart` | local helper | `smart, ignore_ids` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2608 | `check_id` | local helper | `npc_id` | Supports economy subsystem behavior. |
| 2643 | `smart_trade_flags` | local helper | `smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2657 | `smart_has_indexed_trade_route` | local helper | `smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2662 | `smart_has_trade_provider_job` | local helper | `smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2694 | `job_is_trade_customer` | local helper | `job, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2707 | `smart_has_trade_customer_job` | local helper | `smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2731 | `find_trade_customer_job` | local helper | `smart, npc_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2753 | `smart_has_vanilla_trade_route` | local helper | `smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2757 | `queue_remove_squad` | local helper | `q, squad_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2770 | `queue_contains_squad` | local helper | `q, squad_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2782 | `smart_trade_queue` | local helper | `smart_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2791 | `mark_squad_queue_state` | local helper | `squad, state, smart_id, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2800 | `acquire_smart_trade_slot` | local helper | `squad, smart, reason, now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2836 | `release_smart_trade_slot` | local helper | `smart_id, squad_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2858 | `set_smart_trade_slot_remaining` | local helper | `smart_id, squad_id, count` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2865 | `set_squad_trade_cooldown` | local helper | `squad, now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2872 | `smart_by_id` | local helper | `id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2883 | `trade_path.force_until` | assigned wrapper | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2887 | `trade_path.trim` | assigned wrapper | `value` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2891 | `trade_path.npc_name` | assigned wrapper | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2901 | `trade_path.has_patrol_mode` | assigned wrapper | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2909 | `trade_path.set_patrol_mode` | assigned wrapper | `npc, enabled` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2922 | `trade_path.save_point` | assigned wrapper | `npc, index, value` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2934 | `trade_path.clear` | assigned wrapper | `npc, st` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2952 | `trade_path.ini_string` | assigned wrapper | `ini, section, field` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2960 | `trade_path.parse_pos` | assigned wrapper | `line` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2972 | `trade_path.object_position` | assigned wrapper | `obj` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2982 | `trade_path.vertex_accessible` | assigned wrapper | `npc, vid` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3000 | `trade_path.direct_accessible_vertex` | assigned wrapper | `npc, pos` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3011 | `trade_path.nearest_accessible_vertex` | assigned wrapper | `npc, pos` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3025 | `trade_path.accessible_vertex` | assigned wrapper | `npc, pos, fallback_pos` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3049 | `trade_path.line_head_tail` | assigned wrapper | `line` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3057 | `trade_path.head_tokens` | assigned wrapper | `head` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3068 | `trade_path.drop_pos_tail` | assigned wrapper | `tail` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3076 | `trade_path.rewrite_line` | assigned wrapper | `npc, line, fallback_pos` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3100 | `trade_path.prepare` | assigned wrapper | `npc, st, ini, fallback_pos` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3138 | `trade_path.acceptable_prepare_result` | assigned wrapper | `reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3142 | `trade_path.prepare_active` | assigned wrapper | `npc, smart, st, trader` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3170 | `M.clear_prepared_trade_job` | module export | `smart, npc_id, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3209 | `M.release_online_trade_npc_to_smart` | module export | `npc, smart, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3242 | `recover_stale_prepared_trade` | local helper | `squad, now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3283 | `squad_current_trade_smart` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3287 | `server_object_alive` | local helper | `obj` | Safely resolves an ALife/server-side object or runtime reference. |
| 3300 | `find_live_trader_at_smart` | local helper | `smart, ignore_ids` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3309 | `check_id` | local helper | `npc_id, job` | Supports economy subsystem behavior. |
| 3350 | `can_try_auto_trade_now` | local helper | `squad, now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3357 | `smart_for_squad_trade` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3366 | `M.squad_has_trade_smart` | module export | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3374 | `M.squad_has_trade_work` | module export | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3396 | `M._trade_route_current_level` | module export | `squad, board` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3408 | `M._trade_route_levels` | module export | `current_level, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3421 | `M._trade_route_smart_allowed` | module export | `squad, smart, level_name` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3444 | `M.pick_trade_route_smart` | module export | `squad, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3483 | `M.trade_route_task_weight` | module export | `squad, base_weight, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3500 | `mark_trade_lookup_failure` | local helper | `squad, result, reason, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3505 | `resolve_auto_trade_context` | local helper | `squad, reason, now` | Safely resolves an ALife/server-side object or runtime reference. |
| 3538 | `resolve_auto_trade_pair` | local helper | `squad, reason` | Safely resolves an ALife/server-side object or runtime reference. |
| 3558 | `M.resolve_auto_trade_pair` | module export | `squad, reason` | Safely resolves an ALife/server-side object or runtime reference. |
| 3563 | `prepare_npc_vanilla_trade` | local helper | `npc, squad, smart, trader, reason, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3609 | `unlink_npc_smart_job` | local helper | `smart, npc_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 3622 | `setup_assigned_trade_job` | local helper | `npc, smart, info, job, slot_section, trader` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3675 | `force_trade_job_reselect` | local helper | `npc, smart, trader` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3718 | `prepare_squad_vanilla_trade` | local helper | `squad, members, trader, smart, reason, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3766 | `execute_offline_auto_trade` | local helper | `squad, smart, reason, now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3816 | `try_auto_trade_resolved` | local helper | `squad, reason, opts, now` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3834 | `alive_online_pair` | local helper | `npc, trader` | Supports economy subsystem behavior. |
| 3853 | `resolve_explicit_pair` | local helper | `npc, trader` | Safely resolves an ALife/server-side object or runtime reference. |
| 3860 | `M.can_auto_trade_now` | module export | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3864 | `M.debug_resolve_auto_trade_pair` | module export | `squad, reason` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 3869 | `M.try_auto_trade_npc` | module export | `npc, trader, reason, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3889 | `M.try_auto_trade` | module export | `squad, reason, opts` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3918 | `refresh_trade_items_from_inventory` | local helper | `npc, params, force` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3976 | `M.refresh_online_trade_inventory` | module export | `npc, params, force` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 3980 | `M.npc_has_items_to_sell` | module export | `actor, npc, params` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4010 | `execute_online_squad_trade` | local helper | `source_npc, trader, params, squad_id, smart_id, member_ids` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4070 | `suppress_online_squad_trade_members` | local helper | `squad, smart, until_tg` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4077 | `squad_id_for_trade_signal` | local helper | `npc, st` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4088 | `squad_accepts_recovered_trade_signal` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4092 | `resolve_trade_signal_context` | local helper | `npc, params, st` | Safely resolves an ALife/server-side object or runtime reference. |
| 4123 | `resolve_trade_signal_trader` | local helper | `npc, params, st, ctx` | Safely resolves an ALife/server-side object or runtime reference. |
| 4135 | `trade_job_customer_from_params` | local helper | `params` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4142 | `trade_context_already_completed` | local helper | `st` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4146 | `complete_trade_context` | local helper | `npc, params, st, ctx, trader, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4201 | `M.trade_job_give_id` | module export | `actor, npc, params` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4236 | `M.trade_job_sell_items` | module export | `actor, npc, params` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4292 | `M.patch_trade_condition` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4306 | `M.patch_trade_effect` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4328 | `M.watch_recent_trade_release` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4375 | `M.actor_on_update` | module export | `` | Runtime hook for economy lifecycle integration. |
| 4379 | `npc_on_net_spawn` | local helper | `npc, se_obj` | Supports economy subsystem behavior. |
| 4384 | `on_game_load` | script hook/global | `` | Runtime hook for economy lifecycle integration. |
| 4392 | `M.materialize_online_squad_virtual_money` | module export | `` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 4405 | `actor_on_first_update` | script hook/global | `` | Runtime hook for economy lifecycle integration. |
| 4412 | `register_trade_callbacks` | local helper | `force` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 4435 | `M.ensure_runtime_ready` | module export | `force_callbacks` | Checks the shared runtime readiness barrier before context-dependent work. |
| 4442 | `M.on_game_start` | module export | `` | Runtime hook for economy lifecycle integration. |
| 4450 | `on_game_start` | script hook/global | `` | Runtime hook for economy lifecycle integration. |

### `gamedata/scripts/zhopa2_index.script`

Role: event-driven SIMBOARD buckets for squads, smarts, artifacts, ownership, and trade smart flags.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 67 | `M.get_revision` | module export | `` | Supports index subsystem behavior. |
| 71 | `reset_base_camping_target_smarts_cache` | local helper | `` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 77 | `mark_base_camping_registry_changed` | local helper | `` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 85 | `mark_artifact_registry_changed` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 92 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the index subsystem. |
| 101 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 109 | `M.offline_artifacts_enabled` | module export | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 113 | `smart_blacklisted_for_squad` | local helper | `squad, smart, level_name` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 125 | `tasks_mod` | local helper | `` | Supports index subsystem behavior. |
| 135 | `service_fillers_mod` | local helper | `` | Supports index subsystem behavior. |
| 148 | `obj_level` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 166 | `current_level_name` | local helper | `` | Resolves level, graph, route, distance, or position data. |
| 176 | `virtual_artifact_level_allowed` | local helper | `level_name` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 181 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 195 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 214 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 223 | `object_is_artifact` | local helper | `obj` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 231 | `zone_object` | local helper | `zone` | Supports index subsystem behavior. |
| 235 | `artifact_parent_zone` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 244 | `zone_key` | local helper | `zone` | Supports index subsystem behavior. |
| 259 | `object_position` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 289 | `artifact_distance_to_sqr` | local helper | `a, b` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 301 | `artifact_is_valid` | local helper | `id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 323 | `section_exists` | local helper | `section` | Supports index subsystem behavior. |
| 327 | `section_is_artifact` | local helper | `section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 335 | `artefact_settings` | local helper | `` | Reads or normalizes configuration data for the index subsystem. |
| 348 | `name_list` | local helper | `value` | Formats names or display text for diagnostics and UI output. |
| 362 | `num_list` | local helper | `value` | Supports index subsystem behavior. |
| 376 | `artifact_sections_for_token` | local helper | `token` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 398 | `anomaly_cfg_from_spawn_ini` | local helper | `obj` | Reads or normalizes configuration data for the index subsystem. |
| 410 | `zone_level_bucket` | local helper | `level_name` | Resolves level, graph, route, distance, or position data. |
| 422 | `remove_virtual_zone_from_level` | local helper | `zkey, level_name` | Resolves level, graph, route, distance, or position data. |
| 432 | `virtual_storage_state` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 450 | `persist_virtual_artifact` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 468 | `remove_persisted_virtual_artifact` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 478 | `clear_artifact_reservation_owner` | local helper | `artifact_id, squad_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 490 | `artifact_reservation_live` | local helper | `artifact_id, squad_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 518 | `artifact_reserved` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 524 | `artifact_reserved_for_other_squad` | local helper | `artifact_id, squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 536 | `smart_is_base` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 548 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 556 | `squad_cached_npc_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 567 | `is_monster_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 572 | `squad_zhopa2_manageable` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 594 | `squad_zhopa2_manageable_soft` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 616 | `squad_targets_smart_id` | local helper | `squad, smart_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 629 | `squad_base_camping_at_smart` | local helper | `squad, smart_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 639 | `object_community` | local helper | `obj` | Supports index subsystem behavior. |
| 655 | `relation_faction` | local helper | `community` | Supports index subsystem behavior. |
| 663 | `squad_relation_faction` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 674 | `add_count` | local helper | `counts, community, amount` | Maintains indexed runtime state by adding or removing entries. |
| 681 | `each_level` | local helper | `levels, fn` | Resolves level, graph, route, distance, or position data. |
| 707 | `limit_value` | local helper | `limit` | Supports index subsystem behavior. |
| 715 | `now_ms` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 722 | `current_frame_key` | local helper | `` | Supports index subsystem behavior. |
| 736 | `reset_frame_scratch` | script hook/global | `` | Clears transient state, reservations, or stale runtime references. |
| 741 | `levels_key` | local helper | `levels` | Resolves level, graph, route, distance, or position data. |
| 751 | `current_frame_scratch` | local helper | `` | Supports index subsystem behavior. |
| 760 | `frame_reader` | local helper | `kind, levels, limit, build_fn` | Supports index subsystem behavior. |
| 773 | `simboard` | local helper | `` | Supports index subsystem behavior. |
| 777 | `available_by_id` | local helper | `` | Supports index subsystem behavior. |
| 782 | `vanilla_smart_entry` | local helper | `board, smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 786 | `smart_available` | local helper | `board, smart, available` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 796 | `smart_kind_matches` | local helper | `smart, smart_kind` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 821 | `add_smart_from_bucket` | local helper | `out, seen, board, available, smart_id, smart, smart_kind, max_count` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 834 | `read_smart_bucket` | local helper | `levels, smart_kind, max_count` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 872 | `M.smarts_on_levels` | module export | `levels, limit, smart_kind` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 879 | `M.base_smarts_on_levels` | module export | `levels, limit` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 885 | `M.squads_on_levels` | module export | `levels, limit` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 921 | `M.squad_level_names` | module export | `` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 940 | `M.unregister_base_camping_target` | module export | `squad` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 965 | `M.register_base_camping_target` | module export | `squad, target_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 986 | `base_camping_target_has_live_squad` | local helper | `smart_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1011 | `M.base_camping_target_smarts_on_levels` | module export | `levels` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1069 | `smart_artifact_bucket_empty` | local helper | `smart_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1080 | `recalc_smart_artefact_flag` | local helper | `smart_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1111 | `remove_artifact_from_zone_bucket` | local helper | `artifact_id, zone_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1123 | `remove_artifact_from_smart_bucket` | local helper | `artifact_id, smart_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1132 | `remove_artifact_from_other_smart_buckets` | local helper | `artifact_id, keep_smart_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1146 | `add_artifact_to_bucket` | local helper | `bucket_table, key, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1161 | `restore_persisted_virtual_artifacts` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1230 | `nearest_artifact_smart` | local helper | `anchor, level_name` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1248 | `resolve_artifact_smart` | local helper | `artifact_id, artifact_obj, level_name, zone` | Safely resolves an ALife/server-side object or runtime reference. |
| 1265 | `virtual_artifact_id` | local helper | `zone_id, slot` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1271 | `virtual_artifact_zone_key` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1280 | `virtual_spawn_chance` | local helper | `` | Supports index subsystem behavior. |
| 1298 | `read_virtual_zone_entry` | local helper | `zone, cfg_file, source` | Supports index subsystem behavior. |
| 1350 | `choose_virtual_artifact_section` | local helper | `entry` | Resolves a safe section name for runtime classification. |
| 1368 | `register_virtual_artifact` | local helper | `entry, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1406 | `try_spawn_virtual_artifacts` | local helper | `entry` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1434 | `ensure_virtual_artifacts_for_levels` | local helper | `level_set` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1451 | `restore_virtual_artifact_for_squad` | local helper | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1497 | `M.register_anomaly_zone` | module export | `zone, cfg_file, source` | Maintains indexed runtime state by adding or removing entries. |
| 1515 | `M.is_virtual_artifact` | module export | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1523 | `M.virtual_artifact_data` | module export | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1531 | `M.virtual_artifacts_for_zone` | module export | `zone, only_reserved` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1556 | `M.materialize_virtual_artifact` | module export | `virtual_id, real_id, zone, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1591 | `M.register_artifact` | module export | `artifact_id, zone, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1623 | `M.refresh_artifact_entity` | module export | `se_obj` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1667 | `M.unregister_artifact` | module export | `artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1694 | `M.unregister_zone_artifacts` | module export | `zone, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1710 | `M.smart_artefact_available` | module export | `smart` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1716 | `M.reserve_artifact_for_squad` | module export | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1755 | `M.release_artifact_reservation` | module export | `squad_or_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1785 | `restore_virtual_artifact_reservations_from_squads` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1811 | `repair_real_artifact_smart` | local helper | `artifact_id, level_set` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1845 | `M.available_artifact_for_smart` | module export | `smart_or_id, squad, opts` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1883 | `M.artifact_candidate_smarts_on_levels` | module export | `levels, squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1973 | `M.add_artifact_cargo` | module export | `squad, section, value, artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1993 | `M.sync_artifact_cargo` | module export | `squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2012 | `M.consume_artifact_cargo` | module export | `squad, count, value, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2035 | `M.clear_artifact_cargo` | module export | `squad, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2048 | `M.squad_has_artifact_cargo` | module export | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2070 | `M.unregister_smart` | module export | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2086 | `M.unregister_squad` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2098 | `M.base_ownership` | module export | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2102 | `M.update_base_ownership` | module export | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2193 | `distance_to_sqr` | local helper | `a, b` | Resolves level, graph, route, distance, or position data. |
| 2203 | `current_base_pull_valid` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2221 | `M.try_empty_base_pull` | module export | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2297 | `M.on_smart_update` | module export | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2308 | `server_entity_is_artifact` | local helper | `se_obj, type_name` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2319 | `server_entity_on_register` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 2333 | `server_entity_on_unregister` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 2344 | `M.on_game_load` | module export | `` | Runtime hook for index lifecycle integration. |
| 2349 | `M.actor_on_first_update` | module export | `` | Runtime hook for index lifecycle integration. |
| 2354 | `M.on_game_start` | module export | `` | Runtime hook for index lifecycle integration. |
| 2372 | `on_game_start` | script hook/global | `` | Runtime hook for index lifecycle integration. |

### `gamedata/scripts/zhopa2_loot.script`

Role: online loot integration, offline virtual loot accounting, artifact cargo, and loot-loop protection.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 27 | `load_module` | local helper | `name` | Reads, writes, clears, or migrates serializable runtime state. |
| 36 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the loot subsystem. |
| 40 | `memory_mod` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 44 | `index_mod` | local helper | `` | Supports loot subsystem behavior. |
| 48 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 56 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 64 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 68 | `now_ms` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 72 | `runtime_ready` | local helper | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 84 | `alife_sim` | local helper | `` | Safely resolves an ALife/server-side object or runtime reference. |
| 92 | `M.online_enabled` | module export | `` | Supports loot subsystem behavior. |
| 96 | `M.offline_enabled` | module export | `` | Supports loot subsystem behavior. |
| 100 | `M.enabled` | module export | `` | Supports loot subsystem behavior. |
| 104 | `valid_id` | local helper | `id` | Validates safety gates and controlled fallback conditions. |
| 109 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 123 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 138 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 147 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 154 | `object_level_name` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 182 | `offline_loot_level_log` | local helper | `se_victim, se_looter, attacker_squad` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 189 | `object_clsid` | local helper | `obj` | Supports loot subsystem behavior. |
| 200 | `object_section_exists` | local helper | `section` | Resolves a safe section name for runtime classification. |
| 204 | `split_colon` | local helper | `text` | Supports loot subsystem behavior. |
| 213 | `table_contains` | local helper | `t, value` | Supports loot subsystem behavior. |
| 225 | `object_alive` | local helper | `obj` | Supports loot subsystem behavior. |
| 233 | `valid_squad_object` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 241 | `item_cost` | local helper | `item` | Supports loot subsystem behavior. |
| 249 | `object_is_artifact` | local helper | `obj` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 254 | `mark_artifact_cargo_for_squad` | local helper | `squad, item, section, value, artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 278 | `ensure_death_ini` | local helper | `` | Supports loot subsystem behavior. |
| 291 | `ensure_loadout_ini` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 302 | `ini_section_exists` | local helper | `ini, section` | Supports loot subsystem behavior. |
| 306 | `ini_read_string` | local helper | `ini, section, key` | Supports loot subsystem behavior. |
| 314 | `ini_line_count` | local helper | `ini, section` | Supports loot subsystem behavior. |
| 322 | `ini_line` | local helper | `ini, section, idx` | Supports loot subsystem behavior. |
| 333 | `load_death_item_counts` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 353 | `death_section_items` | local helper | `section` | Supports loot subsystem behavior. |
| 370 | `loadout_slot_items` | local helper | `section` | Reads, writes, clears, or migrates serializable runtime state. |
| 394 | `is_monster_player_id` | local helper | `player_id` | Supports loot subsystem behavior. |
| 407 | `looter_squad` | local helper | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 419 | `squad_by_id` | local helper | `squad_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 434 | `managed_stalker_squad_for_looter` | local helper | `npc, require_loot_enabled` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 474 | `M.should_manage_looter` | module export | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 478 | `section_is_quest` | local helper | `section` | Supports loot subsystem behavior. |
| 510 | `section_has_inventory_icon` | local helper | `section` | Supports loot subsystem behavior. |
| 517 | `object_is_inventory_item` | local helper | `obj` | Supports loot subsystem behavior. |
| 530 | `section_is_lootable_inventory` | local helper | `section, obj` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 544 | `object_is_story` | local helper | `obj, id` | Handles story-gated squad events, conversion, migration, or recovery. |
| 549 | `cleanup_exclusive_item_reservations` | local helper | `` | Clears transient state, reservations, or stale runtime references. |
| 562 | `exclusive_item_owner` | local helper | `item_id` | Supports loot subsystem behavior. |
| 575 | `item_reserved_for_other` | local helper | `obj, looter` | Supports loot subsystem behavior. |
| 591 | `M.can_take_section` | module export | `section, obj, looter` | Resolves a safe section name for runtime classification. |
| 613 | `is_stalker_server_object` | local helper | `obj` | Safely resolves an ALife/server-side object or runtime reference. |
| 625 | `offline_squad_can_loot` | local helper | `squad` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 642 | `member_server_object` | local helper | `member` | Safely resolves an ALife/server-side object or runtime reference. |
| 649 | `pick_offline_looter` | local helper | `squad, se_attacker` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 664 | `collect_child_ids` | local helper | `se_owner` | Supports loot subsystem behavior. |
| 678 | `owner_create_args` | local helper | `se_owner` | Supports loot subsystem behavior. |
| 685 | `set_item_condition_from_source` | local helper | `se_src, se_dst` | Supports loot subsystem behavior. |
| 700 | `create_section_to_looter` | local helper | `section, se_looter, props` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 727 | `clone_ammo_to_looter` | local helper | `section, se_item, se_looter` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 757 | `clone_weapon_to_looter` | local helper | `section, se_item, se_looter` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 761 | `clone_item_to_looter` | local helper | `section, se_item, se_looter` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 779 | `created_item_valid` | local helper | `se_new, se_looter` | Validates safety gates and controlled fallback conditions. |
| 791 | `created_item_transfer_log_entry` | local helper | `section, se_new, value, tag` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 808 | `offline_loot_item_log_entry` | local helper | `section, se_item, value` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 827 | `offline_loot_item_transfer_log_entry` | local helper | `section, se_item, se_new, value` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 836 | `section_class` | local helper | `section` | Supports loot subsystem behavior. |
| 844 | `section_is_weapon` | local helper | `section, obj` | Supports loot subsystem behavior. |
| 858 | `section_is_ammo` | local helper | `section` | Supports loot subsystem behavior. |
| 862 | `npc_squad` | local helper | `se_npc` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 870 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 881 | `split_artifact_sections` | local helper | `sections` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 889 | `consume_artifact_cargo_from_squad` | local helper | `squad, count, value, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 915 | `transfer_remaining_artifact_cargo` | local helper | `attacker_squad, victim_squad, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 939 | `squad_virtual_money` | local helper | `squad` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 947 | `transfer_remaining_virtual_money` | local helper | `attacker_squad, victim_squad, reason` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 968 | `death_community` | local helper | `se_npc` | Supports loot subsystem behavior. |
| 983 | `death_rank` | local helper | `se_npc` | Supports loot subsystem behavior. |
| 1002 | `pick_existing_section` | local helper | `ini, preferred, fallback` | Resolves a safe section name for runtime classification. |
| 1012 | `create_generated_loot` | local helper | `section, se_looter, moved_items, tag` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1025 | `add_virtual_loot_section` | local helper | `squad, section, count, value, moved_items, tag` | Resolves a safe section name for runtime classification. |
| 1058 | `spawn_death_section` | local helper | `section, se_looter, moved_items` | Resolves a safe section name for runtime classification. |
| 1083 | `virtual_death_section` | local helper | `section, squad, moved_items` | Resolves a safe section name for runtime classification. |
| 1108 | `spawn_death_table_loot` | local helper | `se_victim, se_looter, moved_items` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1138 | `virtual_death_table_loot` | local helper | `se_victim, squad, moved_items` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1168 | `pick_loadout_entry` | local helper | `slot_section` | Reads, writes, clears, or migrates serializable runtime state. |
| 1181 | `victim_loadout_section` | local helper | `se_victim, comm, rank` | Resolves a safe section name for runtime classification. |
| 1201 | `spawn_loadout_fallback_loot` | local helper | `se_victim, se_looter, moved_items` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1233 | `virtual_loadout_fallback_loot` | local helper | `se_victim, squad, moved_items` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1265 | `offline_loot_clone_valid` | local helper | `se_new, se_looter` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1280 | `offline_loot_items_log` | local helper | `items` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 1296 | `M.offline_loot_victim` | module export | `attacker_squad, se_attacker, se_victim, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1397 | `object_is_online_inventory_owner` | local helper | `obj` | Supports loot subsystem behavior. |
| 1414 | `corpse_has_quest_item` | local helper | `corpse` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1419 | `inspect` | local helper | `owner, item` | Supports loot subsystem behavior. |
| 1431 | `M.is_protected_corpse` | module export | `corpse, corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1441 | `store_for` | local helper | `kind` | Supports loot subsystem behavior. |
| 1445 | `compact_store` | local helper | `store` | Supports loot subsystem behavior. |
| 1462 | `cleanup_store` | local helper | `kind` | Clears transient state, reservations, or stale runtime references. |
| 1481 | `trim_total_cap` | local helper | `` | Supports loot subsystem behavior. |
| 1483 | `count` | local helper | `` | Supports loot subsystem behavior. |
| 1505 | `add_event` | local helper | `kind, id` | Maintains indexed runtime state by adding or removing entries. |
| 1529 | `remove_event` | local helper | `kind, id` | Maintains indexed runtime state by adding or removing entries. |
| 1538 | `recent_ids` | local helper | `kind` | Supports loot subsystem behavior. |
| 1554 | `M.mark_corpse_ignored` | module export | `id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1577 | `M.corpse_ignored` | module export | `id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1587 | `M.recent_corpse_ids` | module export | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1591 | `M.consume_corpse_event_id` | module export | `id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1595 | `M.forget_corpse_id` | module export | `id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1600 | `M.recent_item_ids` | module export | `` | Supports loot subsystem behavior. |
| 1604 | `M.is_recent_item_id` | module export | `id` | Supports loot subsystem behavior. |
| 1610 | `cleanup_targeted_item_requests` | local helper | `` | Clears transient state, reservations, or stale runtime references. |
| 1626 | `forget_targeted_item_request` | local helper | `item_id` | Supports loot subsystem behavior. |
| 1637 | `targeted_gather_prepare` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1647 | `targeted_gather_clear` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1657 | `M.reserve_item_for_npc` | module export | `npc, item_id, reason` | Supports loot subsystem behavior. |
| 1685 | `M.release_item_reservation` | module export | `item_id, npc_or_id` | Clears transient state, reservations, or stale runtime references. |
| 1703 | `M.item_reserved_for_other` | module export | `npc, item_id` | Supports loot subsystem behavior. |
| 1712 | `M.request_item_pickup` | module export | `npc, item_id, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1762 | `M.targeted_item_ids_for_npc` | module export | `npc` | Supports loot subsystem behavior. |
| 1778 | `M.cancel_item_pickup` | module export | `npc_or_id, item_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 1800 | `targeted_request_for_item` | local helper | `item, keep_parented` | Supports loot subsystem behavior. |
| 1811 | `cleanup_vanilla_artifact_pickups` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1823 | `inventory_section_count` | local helper | `owner, section` | Supports loot subsystem behavior. |
| 1829 | `inspect` | local helper | `_, item` | Supports loot subsystem behavior. |
| 1844 | `inventory_item_by_section` | local helper | `owner, section, excluded_id` | Resolves a safe section name for runtime classification. |
| 1851 | `inspect` | local helper | `_, item` | Supports loot subsystem behavior. |
| 1868 | `add_online_member` | local helper | `out, seen, id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1885 | `squad_online_member_objects` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1897 | `artifact_pickup_recovery_context` | local helper | `squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1910 | `M.note_vanilla_artifact_pickup` | module export | `npc, artifact_id, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1946 | `record_targeted_artifact_pickup` | local helper | `npc, item, request, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1964 | `record_task_artifact_pickup_by_section` | local helper | `npc, item, request, reason` | Resolves a safe section name for runtime classification. |
| 1994 | `record_task_artifact_pickup` | local helper | `npc, item, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2018 | `recover_task_artifact_from_squad_inventory` | local helper | `squad, artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2051 | `M.recover_pending_vanilla_artifact_pickup` | module export | `squad, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2075 | `M.corpse_detect_dist_sqr` | module export | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 2080 | `M.item_detect_dist_sqr` | module export | `` | Supports loot subsystem behavior. |
| 2085 | `M.record_loot` | module export | `npc, source, item, value, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 2117 | `M.record_offline_combat_loot` | module export | `squad, target, killed_count, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 2142 | `materialize_virtual_loot_to_npc` | local helper | `npc, reason` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 2213 | `on_npc_death` | local helper | `npc, who` | Supports loot subsystem behavior. |
| 2223 | `on_monster_death` | local helper | `obj, who` | Supports loot subsystem behavior. |
| 2232 | `on_npc_item_drop` | local helper | `npc, item` | Supports loot subsystem behavior. |
| 2241 | `on_actor_item_drop` | local helper | `item` | Supports loot subsystem behavior. |
| 2250 | `on_item_take` | local helper | `npc, item` | Supports loot subsystem behavior. |
| 2268 | `on_actor_item_take` | local helper | `item` | Supports loot subsystem behavior. |
| 2277 | `M.on_game_load` | module export | `` | Runtime hook for loot lifecycle integration. |
| 2287 | `M.on_game_start` | module export | `` | Runtime hook for loot lifecycle integration. |
| 2309 | `on_game_start` | script hook/global | `` | Runtime hook for loot lifecycle integration. |

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
| 96 | `get_path` | script hook/global | `key` | Supports mcm schema subsystem behavior. |
| 100 | `get_option` | script hook/global | `key` | Supports mcm schema subsystem behavior. |

### `gamedata/scripts/zhopa2_memory.script`

Role: serializable squad state, cargo, virtual loot, virtual money, and save/load helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 14 | `write_string` | local helper | `packet, value` | Supports memory subsystem behavior. |
| 18 | `read_string` | local helper | `packet` | Supports memory subsystem behavior. |
| 26 | `index_mod` | local helper | `` | Supports memory subsystem behavior. |
| 35 | `M.reset_squad` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 80 | `pack_recent` | local helper | `values` | Supports memory subsystem behavior. |
| 96 | `unpack_recent` | local helper | `value` | Supports memory subsystem behavior. |
| 111 | `M.add_recent_smart` | module export | `squad, smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 120 | `M.recent_has_smart` | module export | `squad, smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 134 | `M.add_recent_target` | module export | `squad, target_id` | Maintains indexed runtime state by adding or removing entries. |
| 143 | `M.recent_has_target` | module export | `squad, target_id` | Supports memory subsystem behavior. |
| 157 | `M.add_loot_value` | module export | `squad, value, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 168 | `unpack_virtual_loot` | local helper | `value` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 187 | `pack_virtual_loot` | local helper | `entries` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 199 | `virtual_loot_section_count` | local helper | `entries` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 207 | `clamp_virtual_loot_state` | local helper | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 218 | `M.add_virtual_loot` | module export | `squad, section, count, value, reason` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 256 | `M.virtual_loot_entries` | module export | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 283 | `M.virtual_loot_count` | module export | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 287 | `M.virtual_loot_value` | module export | `squad` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 291 | `M.clear_virtual_loot` | module export | `squad, reason` | Reads, writes, sells, clears, or materializes serializable virtual loot cargo. |
| 302 | `M.virtual_money` | module export | `squad` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 306 | `M.add_virtual_money` | module export | `squad, amount, reason` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 319 | `M.take_virtual_money` | module export | `squad, amount, reason` | Reads, writes, spends, or materializes serializable virtual squad money. |
| 336 | `M.add_artifact_cargo` | module export | `squad, section, value, artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 357 | `M.snapshot_task` | module export | `squad, reason` | Supports memory subsystem behavior. |
| 373 | `M.clear_resume` | module export | `squad` | Clears transient state, reservations, or stale runtime references. |
| 385 | `M.resume_task` | module export | `squad, reason` | Supports memory subsystem behavior. |
| 412 | `M.write_squad` | module export | `packet, squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 456 | `M.read_squad` | module export | `packet, squad` | Handles squad lookup, membership, task state, or squad-level accounting. |

### `gamedata/scripts/zhopa2_perception.script`

Role: target discovery, weighted candidate selection, path levels, and faction/blacklist checks.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 44 | `squad_section_name` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 62 | `section_faction` | local helper | `section` | Supports perception subsystem behavior. |
| 70 | `M.squad_player_id` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 81 | `M.squad_relation_faction` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 90 | `cfg` | local helper | `` | Supports perception subsystem behavior. |
| 100 | `now_ms` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 107 | `cleanup_runtime_hunt_cache` | local helper | `now` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 125 | `current_frame_key` | local helper | `` | Supports perception subsystem behavior. |
| 139 | `current_frame_cache` | local helper | `` | Supports perception subsystem behavior. |
| 148 | `cached_frame_value` | local helper | `key, build_fn` | Supports perception subsystem behavior. |
| 162 | `cached_frame_pair` | local helper | `key, build_fn` | Supports perception subsystem behavior. |
| 173 | `obj_cache_key` | local helper | `obj` | Supports perception subsystem behavior. |
| 181 | `memory_mod` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 190 | `index_mod` | local helper | `` | Supports perception subsystem behavior. |
| 199 | `M.is_monster_squad` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 204 | `plain_sim_stalker_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 215 | `M.game_time` | module export | `` | Supports perception subsystem behavior. |
| 219 | `M.elapsed` | module export | `start_time` | Supports perception subsystem behavior. |
| 227 | `M.obj_level` | module export | `obj` | Resolves level, graph, route, distance, or position data. |
| 247 | `M.obj_same_level` | module export | `a, b` | Resolves level, graph, route, distance, or position data. |
| 252 | `add_level` | local helper | `set, list, level_name` | Resolves level, graph, route, distance, or position data. |
| 264 | `target_maps` | local helper | `level_name` | Supports perception subsystem behavior. |
| 282 | `target_maps_has` | local helper | `level_name, target_level` | Supports perception subsystem behavior. |
| 292 | `topology_neighbors` | local helper | `level_name` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 303 | `topology_revision` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 314 | `add_neighbor_sources` | local helper | `level_name, add_fn` | Maintains indexed runtime state by adding or removing entries. |
| 326 | `scan_reverse_edges` | local helper | `target_level, add_fn` | Validates safety gates and controlled fallback conditions. |
| 343 | `M.nearby_levels` | module export | `level_name` | Resolves level, graph, route, distance, or position data. |
| 363 | `add_direct` | local helper | `other_level` | Maintains indexed runtime state by adding or removing entries. |
| 369 | `add_nearby` | local helper | `other_level` | Maintains indexed runtime state by adding or removing entries. |
| 391 | `smart_population` | local helper | `smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 407 | `has_prey_squad` | local helper | `squad, smart` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 424 | `smart_is_base` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 442 | `base_smarts_on_level` | local helper | `level_name` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 460 | `distance_to_sqr` | local helper | `a, b` | Resolves level, graph, route, distance, or position data. |
| 477 | `target_near_base_smart` | local helper | `target, target_level` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 502 | `smart_kind_ok` | local helper | `squad, smart, kind` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 532 | `vanilla_nearby` | local helper | `squad, smart` | Supports perception subsystem behavior. |
| 541 | `level_mode_ok` | local helper | `mode, current_level, target_level, neighbors, squad, smart` | Validates safety gates and controlled fallback conditions. |
| 569 | `M.level_names_for_mode` | module export | `current_level, mode, neighbors` | Resolves level, graph, route, distance, or position data. |
| 572 | `add` | local helper | `level_name` | Maintains indexed runtime state by adding or removing entries. |
| 617 | `mode_needs_neighbors` | local helper | `mode` | Supports perception subsystem behavior. |
| 622 | `ensure_option_neighbors` | local helper | `options` | Supports perception subsystem behavior. |
| 629 | `index_squads_on_levels` | local helper | `levels` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 637 | `index_smarts_on_levels` | local helper | `levels, smart_kind` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 645 | `base_smarts_on_levels` | assigned wrapper | `levels` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 653 | `levels_for_options` | local helper | `options` | Resolves level, graph, route, distance, or position data. |
| 661 | `list_key` | local helper | `list` | Supports perception subsystem behavior. |
| 673 | `bool_key` | local helper | `value` | Supports perception subsystem behavior. |
| 677 | `smart_options_signature` | local helper | `squad, options, levels` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 698 | `hunt_options_signature` | local helper | `squad, options, levels` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 712 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 720 | `squad_member_registered_at_smart` | local helper | `smart, squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 736 | `squad_member_id_set` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 751 | `is_online_offline_group` | local helper | `squad` | Supports perception subsystem behavior. |
| 759 | `is_zhopa2_managed_scripted_target` | local helper | `squad` | Supports perception subsystem behavior. |
| 767 | `is_common_sim_squad` | local helper | `target` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 780 | `is_blacklisted_for_hunt` | local helper | `squad, level_name, smart` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 794 | `safe_zone_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 798 | `hunt_target_profile` | local helper | `target` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 836 | `squad_targets_smart` | local helper | `other, smart` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 849 | `squad_target_smart_id` | local helper | `other` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 859 | `squad_near_smart` | local helper | `other, smart` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 877 | `factions_hostile` | local helper | `faction, target_faction` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 906 | `M.squad_relation_hostile` | module export | `squad, target` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 910 | `faction_relation_rank` | local helper | `faction, owner` | Supports perception subsystem behavior. |
| 938 | `hostile_squad_at_smart` | local helper | `squad, other, smart` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 947 | `smart_has_hostile_squad` | local helper | `squad, smart` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 979 | `base_camping_squad_at_smart` | local helper | `squad, other, smart` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 989 | `base_camping_target_candidates_on_levels` | local helper | `levels, current_level` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1027 | `base_camping_populate_level_rank` | local helper | `squad, smart, options` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1043 | `base_camping_populate_candidates` | local helper | `squad, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1095 | `base_camping_target_map` | local helper | `squad, candidates` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1148 | `smart_owner_relation_rank` | local helper | `squad, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1166 | `nonexclusive_job_capacity` | local helper | `jobs` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1179 | `smart_stalker_job_capacity` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1190 | `occupied_stalker_jobs` | local helper | `smart, ignore_squad` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1195 | `ignored` | local helper | `npc_id` | Supports perception subsystem behavior. |
| 1227 | `targeted_stalker_squads_on_levels` | assigned wrapper | `levels` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1245 | `smart_incoming_stalker_npc_load` | local helper | `squad, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1252 | `add_other` | local helper | `other` | Maintains indexed runtime state by adding or removing entries. |
| 1295 | `M.smart_stalker_free_job_slots` | module export | `squad, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1310 | `base_camping_populate_score` | local helper | `squad, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1328 | `count_rest_load_squad` | local helper | `squad, other, seen` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1348 | `M.smart_rest_load` | module export | `squad, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1380 | `smart_owner_hostile_or_unstable` | local helper | `squad, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1403 | `safe_rest_smart` | local helper | `squad, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1413 | `hunt_profile_prey_ok` | local helper | `squad, profile, prey, hunter_faction` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1422 | `M.valid_hunt_target` | module export | `squad, target, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1470 | `M.valid_revenge_target` | module export | `squad, target, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1511 | `M.index_squads_for_options` | module export | `options, levels` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1517 | `hunt_candidate_pool` | local helper | `options, levels` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1575 | `M.collect_hunt_targets` | module export | `squad, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1593 | `squad_distance_uncached` | local helper | `squad, target` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1615 | `squad_distance` | local helper | `squad, target` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1624 | `route_smart_ok` | local helper | `squad, smart, target_level` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1645 | `smart_from_target_id` | local helper | `target_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1656 | `target_route_smart` | local helper | `squad, target, target_level` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1681 | `actor_server_object` | local helper | `` | Safely resolves an ALife/server-side object or runtime reference. |
| 1690 | `M.actor_script_target` | module export | `squad, opts` | Supports perception subsystem behavior. |
| 1713 | `M.hunt_script_target` | module export | `squad, target, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1739 | `M.revenge_script_target` | module export | `squad, target, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1761 | `pick_hunt_target_once` | local helper | `squad, options` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1795 | `M.pick_hunt_target` | module export | `squad, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1843 | `M.valid_smart` | module export | `squad, smart, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1891 | `M.safe_rest_target_valid` | module export | `squad, target_id` | Validates safety gates and controlled fallback conditions. |
| 1905 | `M.index_smarts_for_options` | module export | `options, levels` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1911 | `valid_smart_cached` | local helper | `squad, smart, options, signature` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1921 | `M.collect_smarts` | module export | `squad, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1947 | `pick_smart_from_options` | local helper | `squad, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1969 | `M.pick_smart` | module export | `squad, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1973 | `M.pick_artifact_target` | module export | `squad, opts` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1979 | `artefact_clone_opts` | local helper | `src` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2025 | `M.pick_closest_smart` | module export | `squad, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2040 | `M.pick_balanced_rest_smart` | module export | `squad, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2061 | `M.pick_base_camping_populate_smart` | module export | `squad, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2098 | `M.base_camping_populate_target_valid` | module export | `squad, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2117 | `M.pick_final_prior_smart` | module export | `squad, smart_or_list, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2144 | `clone_opts` | local helper | `src` | Supports perception subsystem behavior. |
| 2152 | `M.pick_weighted_smart` | module export | `squad, opts, fallback_opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2173 | `M.pack_ids` | module export | `list` | Supports perception subsystem behavior. |
| 2181 | `M.unpack_ids` | module export | `value` | Supports perception subsystem behavior. |
| 2197 | `M.is_night` | module export | `` | Supports perception subsystem behavior. |
| 2202 | `M.make_patrol` | module export | `squad, kind, opts` | Supports perception subsystem behavior. |

### `gamedata/scripts/zhopa2_revenge.script`

Role: revenge event detection, responder selection, and actor hostility scope.

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
| 133 | `death_key` | local helper | `victim_squad, offender_target_id` | Supports revenge subsystem behavior. |
| 140 | `mark_death_processed` | local helper | `victim_squad, offender_target_id` | Supports revenge subsystem behavior. |
| 159 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 167 | `squad_member_count_soft` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 175 | `obj_level` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 200 | `squad_section_name` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 216 | `service_squad_soft` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 227 | `scripted_target_manageable_soft` | local helper | `squad` | Supports revenge subsystem behavior. |
| 238 | `global_level_blacklisted_soft` | local helper | `squad` | Validates safety gates and controlled fallback conditions. |
| 252 | `responder_manageable_soft` | local helper | `squad` | Supports revenge subsystem behavior. |
| 280 | `position_distance` | local helper | `a, b` | Resolves level, graph, route, distance, or position data. |
| 300 | `graph_distance` | local helper | `a, b` | Resolves level, graph, route, distance, or position data. |
| 310 | `squad_distance` | local helper | `victim_squad, responder` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 314 | `actor_killer` | local helper | `se_killer` | Supports revenge subsystem behavior. |
| 322 | `squad_from_member` | local helper | `se_obj` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 350 | `killer_squad_and_target` | local helper | `se_killer` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 358 | `responder_ok` | local helper | `candidate, victim_squad, offender_squad` | Validates safety gates and controlled fallback conditions. |
| 380 | `level_pool` | local helper | `victim_squad` | Resolves level, graph, route, distance, or position data. |
| 395 | `consider_candidate` | local helper | `victim_squad, offender_squad, candidate, best, best_dist` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 406 | `scan_vanilla_squads` | local helper | `levels, victim_squad, offender_squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 423 | `find_responder` | local helper | `victim_squad, offender_squad` | Supports revenge subsystem behavior. |
| 429 | `actor_revenge_roll_passed` | local helper | `` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 440 | `actor_revenge_squad_active` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 447 | `active_actor_revenge_exists` | local helper | `` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 456 | `current_actor_level` | local helper | `` | Resolves level, graph, route, distance, or position data. |
| 466 | `each_revenge_squad` | local helper | `actor_only, fn` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 471 | `visit_squad_id` | local helper | `squad_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 492 | `M.cancel_active_revenge` | module export | `reason, actor_only` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 514 | `actor_revenge_squad_id_for_sleep` | local helper | `` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 524 | `pause_actor_revenge_for_sleep` | local helper | `hours` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 541 | `restore_paused_actor_revenge_after_sleep` | local helper | `` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 560 | `M.apply_online_revenge_hostility` | module export | `` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 588 | `consider_squad_id` | local helper | `squad_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 611 | `sleep_hours_from_ui` | local helper | `ui` | Supports revenge subsystem behavior. |
| 622 | `install_sleep_hook` | local helper | `` | Supports revenge subsystem behavior. |
| 647 | `ui_class.OnButtonSleep` | assigned wrapper | `self, ...` | Supports revenge subsystem behavior. |
| 656 | `actor_on_sleep` | local helper | `hours` | Supports revenge subsystem behavior. |
| 670 | `actor_on_update` | script hook/global | `` | Runtime hook for revenge lifecycle integration. |
| 685 | `M.assign_revenge` | module export | `responder, offender_target_id` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 706 | `M.on_squad_npc_death` | module export | `victim_squad, se_npc, se_killer` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 756 | `M.on_npc_death_callback` | module export | `victim, who` | Supports revenge subsystem behavior. |
| 767 | `M.on_game_start` | module export | `` | Runtime hook for revenge lifecycle integration. |
| 784 | `on_game_start` | script hook/global | `` | Runtime hook for revenge lifecycle integration. |

### `gamedata/scripts/zhopa2_runtime_patches.script`

Role: chain-friendly runtime patching of vanilla/pack scripts.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 46 | `safe_require` | local helper | `name` | Validates safety gates and controlled fallback conditions. |
| 57 | `class_candidate` | local helper | `candidate, required_method` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 71 | `script_class` | local helper | `script_name, class_name, required_method` | Supports runtime patches subsystem behavior. |
| 107 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 125 | `server_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 146 | `M.zhopa2_online_object_by_id` | module export | `id` | Resolves an online game object through db.storage or level lookups. |
| 161 | `M.zhopa2_first_squad_member_id` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 177 | `M.zhopa2_first_online_squad_member` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 182 | `M.zhopa2_object_location` | module export | `obj` | Supports runtime patches subsystem behavior. |
| 219 | `M.zhopa2_direct_hunt_target_anchor` | module export | `target` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 231 | `direct_hunt_target_signature` | local helper | `target` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 250 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 258 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 266 | `object_level_name` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 281 | `global_level_blacklisted` | local helper | `level_name` | Validates safety gates and controlled fallback conditions. |
| 291 | `zhopa2_debug_printf` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 297 | `zhopa2_valid_script_target_id` | local helper | `target_id` | Validates safety gates and controlled fallback conditions. |
| 318 | `runtime_time_ms` | local helper | `` | Supports runtime patches subsystem behavior. |
| 322 | `runtime_log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 332 | `runtime_item_key` | local helper | `stage, item` | Supports runtime patches subsystem behavior. |
| 336 | `mark_runtime_item` | local helper | `stage, item, ok, reason, detail` | Supports runtime patches subsystem behavior. |
| 356 | `runtime_item_ready` | local helper | `stage, item` | Supports runtime patches subsystem behavior. |
| 360 | `runtime_error_enabled` | local helper | `` | Supports runtime patches subsystem behavior. |
| 364 | `runtime_mark_context` | local helper | `` | Formats names or display text for diagnostics and UI output. |
| 387 | `runtime_missing_item` | local helper | `` | Supports runtime patches subsystem behavior. |
| 408 | `required_script_class` | local helper | `script_name, class_name, surface, required_method` | Supports runtime patches subsystem behavior. |
| 419 | `start_zhopa_module` | local helper | `name` | Supports runtime patches subsystem behavior. |
| 447 | `M.ensure_zhopa_modules` | module export | `` | Supports runtime patches subsystem behavior. |
| 455 | `upvalue` | local helper | `fn, name` | Supports runtime patches subsystem behavior. |
| 471 | `set_upvalue` | local helper | `fn, name, value` | Supports runtime patches subsystem behavior. |
| 488 | `M.patch_method` | module export | `owner, method, patch_id, wrapper_factory` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 524 | `install_class_method` | local helper | `cls, name, fn` | Supports runtime patches subsystem behavior. |
| 539 | `patch_required_method` | local helper | `owner, method, patch_id, wrapper_factory, surface` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 562 | `game_time` | local helper | `` | Supports runtime patches subsystem behavior. |
| 566 | `elapsed` | local helper | `start_time` | Supports runtime patches subsystem behavior. |
| 574 | `perception` | local helper | `` | Supports runtime patches subsystem behavior. |
| 578 | `memory` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 582 | `tasks` | local helper | `` | Supports runtime patches subsystem behavior. |
| 586 | `index` | local helper | `` | Supports runtime patches subsystem behavior. |
| 590 | `cache_squad_section_name` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 608 | `object_debug_name` | local helper | `obj` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 627 | `cache_squad_member_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 643 | `squad_player_id` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 664 | `is_monster_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 684 | `plain_sim_stalker_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 698 | `service_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 709 | `managed_stalker_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 716 | `task_invalid_for_monster` | local helper | `squad, task` | Validates safety gates and controlled fallback conditions. |
| 724 | `is_night` | local helper | `` | Supports runtime patches subsystem behavior. |
| 729 | `write_string` | local helper | `packet, value` | Supports runtime patches subsystem behavior. |
| 733 | `read_string` | local helper | `packet` | Supports runtime patches subsystem behavior. |
| 741 | `unpack_ids` | local helper | `value` | Supports runtime patches subsystem behavior. |
| 758 | `squad_methods.zhopa2_cleanup_debug` | assigned wrapper | `self` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 765 | `squad_methods.zhopa2_release_task_rush` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 772 | `squad_methods.zhopa2_release_revenge_hostility` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 779 | `squad_methods.zhopa2_unregister_base_camping_registry` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 786 | `squad_methods.zhopa2_sync_base_camping_registry` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 800 | `squad_methods.zhopa2_is_managed_scripted_target` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 804 | `squad_methods.zhopa2_reset_state` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 832 | `squad_methods.zhopa2_task_requires_rush` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 838 | `squad_methods.zhopa2_sync_task_rush` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 856 | `squad_methods.zhopa2_clear_task` | assigned wrapper | `self, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 904 | `squad_methods.zhopa2_sanitize_task_owner` | assigned wrapper | `self, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 912 | `squad_methods.zhopa2_global_level_blacklisted` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 917 | `squad_methods.zhopa2_purge_global_level_blacklist` | assigned wrapper | `self, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 935 | `squad_methods.zhopa2_can_manage` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 980 | `squad_methods.zhopa2_assign_task` | assigned wrapper | `self, task, target_id, duration_sec, reason, patrol` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1022 | `squad_methods.zhopa2_assign_rest` | assigned wrapper | `self, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1027 | `squad_methods.zhopa2_reached_target` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1034 | `squad_methods.zhopa2_patrol_next` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1052 | `squad_methods.zhopa2_task_completed` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1092 | `squad_methods.zhopa2_target_is_alive` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1119 | `squad_methods.zhopa2_update_task` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1137 | `squad_methods.zhopa2_get_script_target` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1184 | `squad_methods.zhopa2_prepare_hunt_target` | assigned wrapper | `self, script_target_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1216 | `squad_methods.zhopa2_apply_revenge_hostility` | assigned wrapper | `self` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1224 | `squad_methods.zhopa2_state_write` | assigned wrapper | `self, packet` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1240 | `squad_methods.zhopa2_state_read` | assigned wrapper | `self, packet` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1273 | `squad_methods.zhopa2_debug_offline_inventory_update_dump` | assigned wrapper | `self` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 1277 | `install_squad_methods` | local helper | `cls` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1283 | `wrapped_returns` | local helper | `original, self, ...` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 1288 | `retrofit_existing_squads` | local helper | `` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1308 | `M.patch_sim_squad_scripted` | module export | `` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1490 | `M.patch_axr_companions` | module export | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 1497 | `squad_from_npc` | local helper | `npc` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1505 | `online_npc_id` | local helper | `npc` | Supports runtime patches subsystem behavior. |
| 1510 | `vanilla_guide_complete` | local helper | `npc` | Supports runtime patches subsystem behavior. |
| 1533 | `pda_guide_complete` | local helper | `npc` | Supports runtime patches subsystem behavior. |
| 1555 | `mark_post_guide_rest` | local helper | `npc, reason, target_id` | Supports runtime patches subsystem behavior. |
| 1576 | `maybe_mark` | local helper | `npc` | Supports runtime patches subsystem behavior. |
| 1601 | `obj_level` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 1616 | `prop_value` | local helper | `props, key` | Supports runtime patches subsystem behavior. |
| 1620 | `smart_is_base` | local helper | `smart, props` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1632 | `smart_kind_flags` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1658 | `level_bucket` | local helper | `root, level_name` | Resolves level, graph, route, distance, or position data. |
| 1666 | `kind_bucket` | local helper | `root, level_name, kind` | Supports runtime patches subsystem behavior. |
| 1675 | `trim` | local helper | `value` | Supports runtime patches subsystem behavior. |
| 1682 | `lower` | local helper | `value` | Supports runtime patches subsystem behavior. |
| 1686 | `contains` | local helper | `haystack, needle` | Supports runtime patches subsystem behavior. |
| 1690 | `ini_string` | local helper | `ini, section, key` | Supports runtime patches subsystem behavior. |
| 1704 | `ini_section_exists` | local helper | `ini, section` | Supports runtime patches subsystem behavior. |
| 1712 | `open_ini` | local helper | `path` | Supports runtime patches subsystem behavior. |
| 1721 | `smart_cfg_filename` | local helper | `smart` | Reads or normalizes configuration data for the runtime patches subsystem. |
| 1741 | `smart_ini` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1750 | `beh_ini` | local helper | `` | Supports runtime patches subsystem behavior. |
| 1758 | `read_job_string` | local helper | `job_or_section, key, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1771 | `trade_job_flags` | local helper | `job, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1799 | `merge_trade_flags` | local helper | `flags, job_flags` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1810 | `scan_loaded_trade_jobs` | local helper | `smart, flags` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1820 | `scan_exclusive_trade_job` | local helper | `smart, flags, work_field, work_path` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1831 | `scan_smart_ini_trade_jobs` | local helper | `smart, flags` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1859 | `scan_beh_trade_jobs` | local helper | `smart, flags` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1877 | `remove_smart_from_level_buckets` | local helper | `board, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1904 | `board_methods.zhopa2_ensure_buckets` | assigned wrapper | `self` | Supports runtime patches subsystem behavior. |
| 1919 | `board_methods.zhopa2_register_trade_smart` | assigned wrapper | `self, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1948 | `board_methods.zhopa2_unregister_trade_smart` | assigned wrapper | `self, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1963 | `board_methods.zhopa2_register_smart` | assigned wrapper | `self, obj` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1989 | `board_methods.zhopa2_unregister_smart` | assigned wrapper | `self, obj` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2007 | `board_methods.zhopa2_update_squad_level` | assigned wrapper | `self, squad, level_name` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2045 | `board_methods.zhopa2_unregister_squad` | assigned wrapper | `self, squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2057 | `board_methods.zhopa2_rebuild_buckets` | assigned wrapper | `self` | Supports runtime patches subsystem behavior. |
| 2085 | `install_board_methods` | local helper | `cls` | Supports runtime patches subsystem behavior. |
| 2091 | `M.patch_sim_board` | module export | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 2165 | `service_fillers` | local helper | `` | Supports runtime patches subsystem behavior. |
| 2169 | `service_job_fallback` | local helper | `npc_info, job, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2180 | `debug_service_job` | local helper | `smart, npc_info, job, source` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 2225 | `live_targeted_gather_id` | local helper | `npc_info` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 2252 | `targeted_gather_blocks_job` | local helper | `smart, npc_info` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 2268 | `clear_trade_path_override` | local helper | `st` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2294 | `clear_forced_trade_job` | local helper | `st` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2311 | `reset_beh_path_index` | local helper | `npc` | Clears transient state, reservations, or stale runtime references. |
| 2318 | `reassign_forced_trade_job` | local helper | `smart, npc_info, st, npc_id, force_section` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2354 | `forced_trade_blocks_job` | local helper | `smart, npc_info` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 2391 | `try_service_fallback_job` | local helper | `smart, npc_info` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2437 | `ensure_service_job` | local helper | `smart, npc_info` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2462 | `refresh_job_capacity` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2495 | `M.patch_smart_terrain` | module export | `` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 2546 | `artifact_index` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2550 | `register_artifact` | local helper | `artifact_id, zone, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2557 | `unregister_artifact` | local helper | `artifact_id, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2564 | `unregister_zone_artifacts` | local helper | `zone, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2571 | `register_anomaly_zone` | local helper | `zone, cfg_file, source` | Maintains indexed runtime state by adding or removing entries. |
| 2578 | `virtual_artifacts_for_zone` | local helper | `zone` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2587 | `materialize_virtual_artifact` | local helper | `virtual_id, real_id, zone, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2594 | `zone_key` | local helper | `zone` | Supports runtime patches subsystem behavior. |
| 2600 | `M.zhopa2_sync_existing_anomaly_zones` | module export | `source` | Supports runtime patches subsystem behavior. |
| 2635 | `zhopa2_materialize_virtual_artifact_online` | script hook/global | `virtual_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2654 | `anomaly_spawn_artefact_section` | local helper | `self, section` | Resolves a safe section name for runtime classification. |
| 2677 | `anomaly_materialize_virtual_artifacts` | local helper | `self` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2692 | `M.patch_bind_anomaly_zone` | module export | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 2784 | `M.zhopa2_direct_hunt_live_location` | module export | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2808 | `M.zhopa2_direct_hunt_commander_execute` | module export | `self, squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2843 | `M.patch_xr_reach_task` | module export | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 2861 | `task_run` | local helper | `squad` | Supports runtime patches subsystem behavior. |
| 2869 | `direct_monster_update` | local helper | `self` | Supports runtime patches subsystem behavior. |
| 2934 | `M.patch_bind_monster` | module export | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 2951 | `offline_loot_attacker_squad` | local helper | `killer` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 2966 | `ignore_offline_loot_detail` | local helper | `detail` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 2977 | `offline_loot_on_death` | local helper | `victim, killer` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3018 | `patch_death_class` | local helper | `cls, patch_name` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 3030 | `M.patch_sim_offline_combat` | module export | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 3053 | `gather_mod` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3057 | `corpse_mod` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3061 | `module_member` | local helper | `mod, name` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 3065 | `export_script_function` | local helper | `mod, name, fn` | Supports runtime patches subsystem behavior. |
| 3075 | `gather_original_func` | local helper | `mod, name` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3091 | `gather_upvalue` | local helper | `name` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3097 | `set_gather_upvalue` | local helper | `name, value` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3103 | `gather_items_table` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3112 | `zhopa2_loot_mod` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3116 | `zhopa2_loot_active` | local helper | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3121 | `zhopa2_loot_globally_enabled` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3126 | `M.zhopa2_sync_gather_runtime_state` | module export | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3189 | `zhopa2_can_take_section` | local helper | `npc, item, section` | Resolves a safe section name for runtime classification. |
| 3197 | `zhopa2_event_item_ids` | local helper | `` | Supports runtime patches subsystem behavior. |
| 3205 | `zhopa2_targeted_item_ids` | local helper | `npc` | Supports runtime patches subsystem behavior. |
| 3213 | `zhopa2_item_targeted_for_npc` | local helper | `npc, item_id, ids` | Supports runtime patches subsystem behavior. |
| 3235 | `zhopa2_item_reserved_for_other` | local helper | `npc, item_id` | Supports runtime patches subsystem behavior. |
| 3243 | `zhopa2_item_clsid` | local helper | `item` | Supports runtime patches subsystem behavior. |
| 3251 | `zhopa2_item_detect_dist_sqr` | local helper | `` | Supports runtime patches subsystem behavior. |
| 3259 | `zhopa2_record_loot` | local helper | `npc, item, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3267 | `M.zhopa2_note_vanilla_artifact_pickup` | module export | `npc, artifact_id, section` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3276 | `zhopa2_should_skip_overweight` | local helper | `npc` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 3280 | `zhopa2_should_skip_condlist` | local helper | `npc` | Supports runtime patches subsystem behavior. |
| 3284 | `zhopa2_item_reserved_by` | local helper | `item_id` | Supports runtime patches subsystem behavior. |
| 3290 | `zhopa2_reservation_is_live` | local helper | `owner_id, item_id` | Supports runtime patches subsystem behavior. |
| 3307 | `zhopa2_clear_artifact_scan` | local helper | `st` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3317 | `zhopa2_reset_artifact_approach` | local helper | `st` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3335 | `zhopa2_mark_approach_failed` | local helper | `st, item_id, reason` | Supports runtime patches subsystem behavior. |
| 3343 | `zhopa2_clear_approach_failure` | local helper | `st, item_id` | Clears transient state, reservations, or stale runtime references. |
| 3354 | `zhopa2_object_vertex` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 3371 | `zhopa2_valid_accessible_vertex` | local helper | `npc, vid` | Validates safety gates and controlled fallback conditions. |
| 3385 | `zhopa2_nearest_accessible_vertex` | local helper | `npc, pos` | Resolves level, graph, route, distance, or position data. |
| 3407 | `zhopa2_vertex_in_direction` | local helper | `npc, from_vid, dir, dist` | Resolves level, graph, route, distance, or position data. |
| 3420 | `zhopa2_select_artifact_approach` | local helper | `npc, item, item_pos, start_index, bad_vids` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3458 | `zhopa2_safe_look_position` | local helper | `npc, pos` | Validates safety gates and controlled fallback conditions. |
| 3469 | `zhopa2_artifact_approach_reached` | local helper | `npc, st` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3476 | `zhopa2_artifact_pickup_ready` | local helper | `npc, st` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3484 | `M.zhopa2_artifact_vanilla_pickup_reachable` | module export | `npc, st, item` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3505 | `zhopa2_artifact_approach_progress_ok` | local helper | `npc, st` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3528 | `M.zhopa2_gather_stalled` | module export | `npc, st, item_id, target_pos` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3570 | `zhopa2_prepare_next_artifact_approach` | local helper | `npc, st, item, item_pos, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3593 | `zhopa2_send_to_artifact_vertex` | local helper | `npc, st, invalid_reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3611 | `zhopa2_evaluator_camper_end_for_gather:__init` | assigned wrapper | `name` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3613 | `zhopa2_evaluator_camper_end_for_gather:evaluate` | assigned wrapper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3634 | `zhopa2_apply_camper_end_override` | local helper | `manager` | Supports runtime patches subsystem behavior. |
| 3648 | `zhopa2_add_gather_precondition` | local helper | `manager, action_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3665 | `zhopa2_job_action_key` | local helper | `root` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 3676 | `zhopa2_suspend_active_scheme_for_targeted_gather` | local helper | `npc, st` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3700 | `zhopa2_restore_active_scheme_after_targeted_gather` | local helper | `npc, st` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3718 | `zhopa2_apply_job_preconditions` | local helper | `npc, st` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 3762 | `zhopa2_start_artifact_scan` | local helper | `npc, st, item, now` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3773 | `zhopa2_update_artifact_scan` | local helper | `npc, st, item, now` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3794 | `zhopa2_begin_artifact_pickup` | local helper | `npc, st, item, now, force` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3806 | `M.zhopa2_try_artifact_force_pickup` | module export | `npc, st, item, now, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 3822 | `zhopa2_reset_gather_state` | local helper | `st` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3853 | `zhopa2_item_reservation_owner_impl` | local helper | `item_id` | Supports runtime patches subsystem behavior. |
| 3863 | `zhopa2_prepare_targeted_gather_impl` | local helper | `npc, item_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3874 | `zhopa2_force_gather_item` | script hook/global | `npc, item_id, targeted` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3955 | `zhopa2_clear_gather_item` | script hook/global | `npc, item_id, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3976 | `M.zhopa2_try_force_online_gather_item` | module export | `npc, st` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 3984 | `consider` | local helper | `item_id` | Supports runtime patches subsystem behavior. |
| 4034 | `M.zhopa2_gather_item_active` | module export | `npc, item_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4062 | `zhopa2_gather_item_failure_reason_impl` | local helper | `npc, item_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4073 | `zhopa2_gather_item_debug_status_impl` | local helper | `npc, item_id` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 4111 | `zhopa2_gather_item_replacement` | local helper | `original, force_selected` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4210 | `patch_gather_classes` | local helper | `mod` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4483 | `M.patch_xr_gather_items` | module export | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4503 | `mod.zhopa2_wrapped_near_actor` | assigned wrapper | `obj, npc, ...` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 4523 | `zhopa2_is_protected_corpse` | local helper | `corpse, corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4531 | `zhopa2_event_corpse_ids` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4539 | `zhopa2_forget_corpse_id` | local helper | `corpse_id, consume_only` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4548 | `zhopa2_mark_corpse_checked` | local helper | `corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4555 | `M.zhopa2_mark_corpse_exhausted` | module export | `corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4578 | `M.zhopa2_corpse_exhausted` | module export | `corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4584 | `zhopa2_reject_corpse_candidate` | local helper | `mod, st, corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4636 | `zhopa2_corpse_detect_dist_sqr` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4644 | `zhopa2_corpse_already_looted` | local helper | `corpse` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4651 | `zhopa2_is_inventory_owner` | local helper | `obj` | Supports runtime patches subsystem behavior. |
| 4668 | `zhopa2_corpse_has_money` | local helper | `corpse` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4677 | `M.zhopa2_corpse_can_take_item` | module export | `npc, item, section` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4690 | `zhopa2_corpse_has_takeable_item` | local helper | `npc, corpse, active` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4700 | `check_item` | local helper | `owner, item` | Supports runtime patches subsystem behavior. |
| 4715 | `zhopa2_corpse_has_candidate_loot` | local helper | `npc, corpse, corpse_id, active` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4735 | `zhopa2_corpse_record_loot` | local helper | `npc, corpse, item, value, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4743 | `zhopa2_item_value` | local helper | `section` | Supports runtime patches subsystem behavior. |
| 4750 | `corpse_original_func` | local helper | `mod, name` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4761 | `zhopa2_get_all_from_corpse_replacement` | local helper | `original` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4815 | `get_item` | local helper | `owner, item` | Supports runtime patches subsystem behavior. |
| 4857 | `patch_corpse_classes` | local helper | `mod` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4858 | `corpse_object` | local helper | `corpse_id` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 4865 | `reject_if_protected` | local helper | `st, corpse_id` | Supports runtime patches subsystem behavior. |
| 4874 | `cleanup_protected_state` | local helper | `st` | Reads, writes, clears, or migrates serializable runtime state. |
| 5000 | `M.patch_xr_corpse_detection` | module export | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 5012 | `mod.zhopa2_wrapped_near_actor` | assigned wrapper | `obj, npc, ...` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 5025 | `M.patch_se_level_changer` | module export | `` | Resolves level, graph, route, distance, or position data. |
| 5031 | `run_runtime_patch` | local helper | `patch` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 5058 | `M.ensure_all` | module export | `reason` | Supports runtime patches subsystem behavior. |
| 5070 | `M._on_game_load` | module export | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 5075 | `M._actor_on_first_update` | module export | `` | Supports runtime patches subsystem behavior. |
| 5085 | `M._runtime_recheck_due` | module export | `reason` | Supports runtime patches subsystem behavior. |
| 5103 | `M.runtime_not_ready_reason` | module export | `` | Supports runtime patches subsystem behavior. |
| 5108 | `M.runtime_ready` | module export | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 5117 | `M.runtime_gate_ready` | module export | `reason` | Supports runtime patches subsystem behavior. |
| 5121 | `M.on_game_start` | module export | `` | Runtime hook for runtime patches lifecycle integration. |
| 5136 | `on_game_start` | script hook/global | `` | Runtime hook for runtime patches lifecycle integration. |
| 5140 | `_G.zhopa2_runtime_ready` | assigned wrapper | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 5144 | `_G.zhopa2_runtime_not_ready_reason` | assigned wrapper | `` | Supports runtime patches subsystem behavior. |

### `gamedata/scripts/zhopa2_service_fillers.script`

Role: base service NPC detection, adoption, and filler spawning.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 87 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the service fillers subsystem. |
| 96 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 104 | `debug_service_guard` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 111 | `runtime_ready` | local helper | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 123 | `cfg_alias` | local helper | `name` | Reads or normalizes configuration data for the service fillers subsystem. |
| 134 | `normalize_key` | local helper | `name` | Supports service fillers subsystem behavior. |
| 147 | `owner_engine` | local helper | `name` | Supports service fillers subsystem behavior. |
| 156 | `service_alias` | local helper | `engine` | Supports service fillers subsystem behavior. |
| 161 | `vanilla_prefix` | local helper | `engine` | Supports service fillers subsystem behavior. |
| 166 | `tg` | local helper | `` | Supports service fillers subsystem behavior. |
| 170 | `safe_manager` | local helper | `module_name, getter_name` | Validates safety gates and controlled fallback conditions. |
| 181 | `manager_time_due` | local helper | `mgr, last_field` | Supports service fillers subsystem behavior. |
| 201 | `callback_from_start` | local helper | `` | Supports service fillers subsystem behavior. |
| 214 | `surge_event_due` | local helper | `` | Supports service fillers subsystem behavior. |
| 219 | `psi_storm_event_due` | local helper | `` | Supports service fillers subsystem behavior. |
| 224 | `queue_emission_fill` | local helper | `kind, due` | Supports service fillers subsystem behavior. |
| 233 | `flush_pending_emission_fill` | local helper | `` | Supports service fillers subsystem behavior. |
| 248 | `smart_is_base` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 252 | `smart_name` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 269 | `object_debug_name` | local helper | `obj` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 289 | `object_debug_id` | local helper | `obj` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 306 | `section_exists` | local helper | `section` | Supports service fillers subsystem behavior. |
| 319 | `read_ini_string_from` | local helper | `ini, section, key` | Supports service fillers subsystem behavior. |
| 338 | `read_ini_string` | local helper | `job_or_section, key, smart` | Supports service fillers subsystem behavior. |
| 358 | `contains` | local helper | `haystack, needle` | Supports service fillers subsystem behavior. |
| 362 | `strip_inline_comment` | local helper | `value` | Supports service fillers subsystem behavior. |
| 373 | `plain_unique_provider_suitable` | local helper | `job_or_section, smart` | Supports service fillers subsystem behavior. |
| 388 | `role_from_level_spot` | local helper | `level_spot` | Resolves level, graph, route, distance, or position data. |
| 395 | `normalize_role` | local helper | `role` | Supports service fillers subsystem behavior. |
| 409 | `classify_job_role` | local helper | `job_or_section, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 486 | `role_from_section` | local helper | `section` | Resolves a safe section name for runtime classification. |
| 505 | `safe_npc_section` | local helper | `se_obj` | Resolves a safe section name for runtime classification. |
| 518 | `safe_squad_by_id` | local helper | `id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 543 | `online_object` | local helper | `se_obj` | Resolves an online game object through db.storage or level lookups. |
| 561 | `is_stalker_se` | local helper | `se_obj` | Supports service fillers subsystem behavior. |
| 571 | `set_online_community` | local helper | `se_obj, engine_owner` | Supports service fillers subsystem behavior. |
| 585 | `service_squad_from_member` | local helper | `se_obj` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 593 | `same_id` | local helper | `a, b` | Supports service fillers subsystem behavior. |
| 599 | `pin_service_squad` | local helper | `squad, smart, section` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 656 | `adopt_service_squad` | local helper | `squad, smart, engine_owner, section` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 664 | `adopt_service_member` | local helper | `se_obj, smart, engine_owner, section` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 676 | `collect_allowed_roles` | local helper | `smart` | Supports service fillers subsystem behavior. |
| 691 | `role_from_member_info` | local helper | `info, smart` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 708 | `M.job_accepts_service_npc` | module export | `npc_info, job, smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 726 | `collect_existing_roles` | local helper | `smart, engine_owner` | Supports service fillers subsystem behavior. |
| 765 | `roles_from_set` | local helper | `set` | Supports service fillers subsystem behavior. |
| 779 | `missing_roles` | local helper | `allowed, existing` | Supports service fillers subsystem behavior. |
| 790 | `roles_string` | local helper | `roles` | Supports service fillers subsystem behavior. |
| 797 | `clear_smart_fields` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 809 | `mark_smart` | local helper | `smart, engine_owner, missing, reason` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 824 | `unmark_smart` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 830 | `resolve_ownership` | local helper | `smart, ownership` | Safely resolves an ALife/server-side object or runtime reference. |
| 847 | `service_section` | local helper | `engine_owner, role` | Resolves a safe section name for runtime classification. |
| 874 | `spawn_service_squad` | local helper | `smart, engine_owner, role` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 893 | `M.reconcile_smart` | module export | `smart, ownership, allow_spawn, reason` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 950 | `smart_by_id` | local helper | `id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 962 | `M.fill_marked_smarts` | module export | `reason` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 987 | `M.on_smart_update` | module export | `smart, ownership` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 994 | `M.on_smart_unregister` | module export | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 999 | `M.on_before_surge` | module export | `flags` | Supports service fillers subsystem behavior. |
| 1006 | `M.on_before_psi_storm` | module export | `flags` | Supports service fillers subsystem behavior. |
| 1013 | `M.actor_on_update` | module export | `` | Runtime hook for service fillers lifecycle integration. |
| 1020 | `M.on_game_load` | module export | `` | Runtime hook for service fillers lifecycle integration. |
| 1025 | `server_entity_on_unregister` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 1031 | `M.on_game_start` | module export | `` | Runtime hook for service fillers lifecycle integration. |
| 1050 | `on_game_start` | script hook/global | `` | Runtime hook for service fillers lifecycle integration. |

### `gamedata/scripts/zhopa2_story_north_migration.script`

Role: story-gated northern migration task selection and recovery.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 58 | `load_module` | local helper | `name` | Reads, writes, clears, or migrates serializable runtime state. |
| 67 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the story north migration subsystem. |
| 71 | `index_mod` | local helper | `` | Supports story north migration subsystem behavior. |
| 75 | `perception_mod` | local helper | `` | Supports story north migration subsystem behavior. |
| 79 | `topology_mod` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 83 | `runtime_ready` | local helper | `reason` | Checks the shared runtime readiness barrier before context-dependent work. |
| 95 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 103 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 111 | `debug_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 115 | `debug_log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 121 | `now_ms` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 125 | `normalize_id` | local helper | `value` | Supports story north migration subsystem behavior. |
| 133 | `normalize_status` | local helper | `value` | Supports story north migration subsystem behavior. |
| 144 | `normalize_sid_set` | local helper | `src` | Supports story north migration subsystem behavior. |
| 163 | `normalize_status_map` | local helper | `src` | Supports story north migration subsystem behavior. |
| 177 | `event_state` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 190 | `resolve_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 215 | `object_level` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 244 | `safe_name` | local helper | `obj` | Validates safety gates and controlled fallback conditions. |
| 257 | `squad_section_name` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 275 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 283 | `normalize_faction` | local helper | `value` | Supports story north migration subsystem behavior. |
| 298 | `squad_faction` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 309 | `relation_faction` | local helper | `value` | Supports story north migration subsystem behavior. |
| 314 | `relation_allows_coexist` | local helper | `source_faction, other_faction` | Supports story north migration subsystem behavior. |
| 333 | `is_story_mode_active` | local helper | `` | Handles story-gated squad events, conversion, migration, or recovery. |
| 357 | `has_info` | local helper | `info` | Supports story north migration subsystem behavior. |
| 377 | `trigger_active` | local helper | `` | Supports story north migration subsystem behavior. |
| 381 | `feature_enabled_now` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 387 | `percent_value` | local helper | `` | Supports story north migration subsystem behavior. |
| 397 | `is_monster_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 406 | `squad_can_manage` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 421 | `is_ap_owned_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 430 | `is_plain_stalker_sim_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 441 | `eligible_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 455 | `smart_by_id` | local helper | `smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 468 | `target_validation_opts` | local helper | `kind` | Validates safety gates and controlled fallback conditions. |
| 479 | `collect_target_factions` | local helper | `smart` | Supports story north migration subsystem behavior. |
| 510 | `target_safe_for_squad` | local helper | `squad, smart, expected_level, kind` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 534 | `game_graph_distance` | local helper | `a, b` | Resolves level, graph, route, distance, or position data. |
| 557 | `pick_random` | local helper | `list` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 564 | `shuffle_in_place` | local helper | `list` | Supports story north migration subsystem behavior. |
| 577 | `smarts_on_level` | local helper | `level_name, kind` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 585 | `base_smarts_on_level` | local helper | `level_name` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 593 | `projected_load` | local helper | `level_name, exclude_sid` | Reads, writes, clears, or migrates serializable runtime state. |
| 609 | `ordered_north_levels` | local helper | `squad` | Handles story-gated squad events, conversion, migration, or recovery. |
| 646 | `nearest_safe_from_list` | local helper | `squad, level_name, list, kind` | Validates safety gates and controlled fallback conditions. |
| 668 | `safe_random_smart` | local helper | `squad, level_name` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 680 | `pick_safe_target_on_level` | local helper | `squad, level_name` | Validates safety gates and controlled fallback conditions. |
| 695 | `neighbor_levels` | local helper | `level_name` | Resolves level, graph, route, distance, or position data. |
| 706 | `pick_north_target` | local helper | `squad` | Handles story-gated squad events, conversion, migration, or recovery. |
| 733 | `story_task_active` | local helper | `squad` | Handles story-gated squad events, conversion, migration, or recovery. |
| 737 | `set_status` | local helper | `sid, status` | Supports story north migration subsystem behavior. |
| 744 | `M.is_story_task` | module export | `task` | Handles story-gated squad events, conversion, migration, or recovery. |
| 749 | `M.is_sid_selected` | module export | `sid` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 754 | `M.is_sid_locked` | module export | `sid` | Supports story north migration subsystem behavior. |
| 763 | `save_state` | script hook/global | `m_data` | Runtime hook for story north migration lifecycle integration. |
| 778 | `load_state` | script hook/global | `m_data` | Runtime hook for story north migration lifecycle integration. |
| 810 | `clear_story_task` | local helper | `squad, reason` | Handles story-gated squad events, conversion, migration, or recovery. |
| 818 | `assign_rest` | local helper | `squad, reason` | Supports story north migration subsystem behavior. |
| 830 | `sync_live_target` | local helper | `squad` | Supports story north migration subsystem behavior. |
| 846 | `story_arrived` | local helper | `squad, smart` | Handles story-gated squad events, conversion, migration, or recovery. |
| 878 | `assign_story_target` | local helper | `squad, sid, smart, level_name, source` | Handles story-gated squad events, conversion, migration, or recovery. |
| 901 | `retarget_story_task` | local helper | `squad, sid, current_target, reason` | Handles story-gated squad events, conversion, migration, or recovery. |
| 935 | `activate_selected_sid` | local helper | `sid, source, squad` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 994 | `collect_eligible_sids` | local helper | `` | Supports story north migration subsystem behavior. |
| 1017 | `maybe_fire` | local helper | `source` | Supports story north migration subsystem behavior. |
| 1062 | `reconcile_selected` | local helper | `source` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1087 | `M.update_squad_tasks` | module export | `squad, ctx` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1109 | `M.debug_status_line` | module export | `squad` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 1117 | `M.ensure_runtime_ready` | module export | `force_callbacks` | Checks the shared runtime readiness barrier before context-dependent work. |
| 1124 | `request_reconcile` | local helper | `source` | Supports story north migration subsystem behavior. |
| 1134 | `actor_on_update` | script hook/global | `` | Runtime hook for story north migration lifecycle integration. |
| 1147 | `actor_on_first_update` | script hook/global | `` | Runtime hook for story north migration lifecycle integration. |
| 1151 | `on_game_load` | script hook/global | `` | Runtime hook for story north migration lifecycle integration. |
| 1155 | `on_option_change` | script hook/global | `` | Runtime hook for story north migration lifecycle integration. |
| 1159 | `server_entity_on_unregister` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 1169 | `server_entity_on_register` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 1180 | `squad_on_after_level_change` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1188 | `M.on_game_start` | module export | `` | Runtime hook for story north migration lifecycle integration. |
| 1205 | `reg` | local helper | `name, fn` | Supports story north migration subsystem behavior. |
| 1233 | `on_game_start` | script hook/global | `` | Runtime hook for story north migration lifecycle integration. |

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
| 376 | `squad_level_name` | local helper | `squad, known_level` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 386 | `extract_member_candidate_id` | local helper | `k, v` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 396 | `squad_member_ids` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 402 | `push` | local helper | `id` | Supports story psy watchdog subsystem behavior. |
| 425 | `squad_member_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 437 | `squad_can_manage` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 454 | `is_plain_stalker_sim_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 466 | `is_ap_owned_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 475 | `pick_zombied_squad_section` | local helper | `source_section` | Resolves a safe section name for runtime classification. |
| 493 | `pick_zombied_member_section` | local helper | `zombied_squad_section` | Resolves a safe section name for runtime classification. |
| 501 | `smart_object_by_id` | local helper | `smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 517 | `smart_level_name` | local helper | `smart` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 524 | `build_context` | local helper | `squad, community, level_name` | Formats names or display text for diagnostics and UI output. |
| 569 | `create_empty_squad` | local helper | `section, position, lvid, gvid` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 589 | `populate_zombied_squad` | local helper | `squad, context` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 602 | `assign_squad_to_smart` | local helper | `squad, smart_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 612 | `finalize_spawned_squad` | local helper | `squad, context` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 648 | `cleanup_source_task` | local helper | `squad` | Clears transient state, reservations, or stale runtime references. |
| 661 | `unregister_released_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 672 | `release_squad_safe` | local helper | `squad, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 699 | `log_mutation_error` | local helper | `sid, context, source, reason, new_squad, extra` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 726 | `candidate_context` | local helper | `squad, source, known_level` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 764 | `M.convert_squad_to_zombied` | module export | `squad, context, source` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 842 | `M.try_process_squad` | module export | `squad, source, known_level` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 850 | `M.reconcile_all_levels` | module export | `source` | Resolves level, graph, route, distance, or position data. |
| 881 | `request_reconcile` | local helper | `source` | Supports story psy watchdog subsystem behavior. |
| 890 | `actor_on_update` | script hook/global | `` | Runtime hook for story psy watchdog lifecycle integration. |
| 902 | `actor_on_first_update` | script hook/global | `` | Runtime hook for story psy watchdog lifecycle integration. |
| 907 | `on_game_load` | script hook/global | `` | Runtime hook for story psy watchdog lifecycle integration. |
| 912 | `on_option_change` | script hook/global | `` | Runtime hook for story psy watchdog lifecycle integration. |
| 917 | `squad_on_after_level_change` | local helper | `squad, old_level, new_level` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 928 | `server_entity_on_register` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 940 | `M.on_game_start` | module export | `` | Runtime hook for story psy watchdog lifecycle integration. |
| 955 | `register_callback` | local helper | `name, fn` | Maintains indexed runtime state by adding or removing entries. |
| 981 | `on_game_start` | script hook/global | `` | Runtime hook for story psy watchdog lifecycle integration. |

### `gamedata/scripts/zhopa2_tasks.script`

Role: task constants, task FSM, assignment, completion, and fallback rules.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 37 | `cfg` | local helper | `` | Supports tasks subsystem behavior. |
| 47 | `perception` | local helper | `` | Supports tasks subsystem behavior. |
| 56 | `memory_mod` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 65 | `offline_combat_mod` | local helper | `` | Supports tasks subsystem behavior. |
| 74 | `loot_mod` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 83 | `artifacts_mod` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 92 | `economy_mod` | local helper | `` | Supports tasks subsystem behavior. |
| 101 | `index_mod` | local helper | `` | Supports tasks subsystem behavior. |
| 110 | `story_north_mod` | local helper | `` | Handles story-gated squad events, conversion, migration, or recovery. |
| 121 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 129 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 137 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 145 | `is_night_now` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 155 | `revenge_expired_by_night` | local helper | `` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 159 | `current_hour` | local helper | `` | Supports tasks subsystem behavior. |
| 164 | `surge_active_uncached` | local helper | `` | Supports tasks subsystem behavior. |
| 219 | `M.surge_active` | module export | `force_refresh` | Supports tasks subsystem behavior. |
| 229 | `mutant_time_active` | local helper | `start_hour, end_hour` | Supports tasks subsystem behavior. |
| 239 | `squad_section_name` | local helper | `squad` | Resolves a safe section name for runtime classification. |
| 257 | `config_faction_for_section` | local helper | `section` | Reads or normalizes configuration data for the tasks subsystem. |
| 265 | `mutant_behavior_id` | local helper | `squad` | Supports tasks subsystem behavior. |
| 280 | `now_ms` | assigned wrapper | `` | Calculates time, cooldown, or tick-throttling values. |
| 287 | `safe_alife_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 296 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 315 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 331 | `object_is_smart` | local helper | `obj` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 344 | `named_id` | local helper | `obj_or_id` | Formats names or display text for diagnostics and UI output. |
| 355 | `debug_trade_log` | local helper | `squad, stage, result, detail` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 397 | `current_frame_key` | local helper | `` | Supports tasks subsystem behavior. |
| 414 | `assignment_budget_open` | local helper | `squad` | Supports tasks subsystem behavior. |
| 427 | `mark_task_no_target` | local helper | `squad, task` | Supports tasks subsystem behavior. |
| 436 | `clear_task_no_target` | local helper | `squad, task` | Clears transient state, reservations, or stale runtime references. |
| 443 | `task_no_target_cooldown_active` | local helper | `squad, task` | Calculates time, cooldown, or tick-throttling values. |
| 456 | `target_valid_cache_key` | local helper | `squad, task, target` | Validates safety gates and controlled fallback conditions. |
| 466 | `target_valid_cache_hit` | local helper | `squad, key` | Validates safety gates and controlled fallback conditions. |
| 473 | `target_valid_cache_store` | local helper | `squad, key` | Validates safety gates and controlled fallback conditions. |
| 480 | `target_valid_cache_clear` | local helper | `squad` | Validates safety gates and controlled fallback conditions. |
| 487 | `is_monster_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 520 | `mutant_has_stalker_task` | local helper | `squad, task` | Supports tasks subsystem behavior. |
| 524 | `make_choice` | local helper | `task, target, weight, reason, duration, patrol` | Supports tasks subsystem behavior. |
| 542 | `task_weight` | local helper | `key, default` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 562 | `registry_weight_meta` | local helper | `pool, name` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 567 | `register_task` | local helper | `pool, name, builder, weight_fn` | Maintains indexed runtime state by adding or removing entries. |
| 581 | `pick_weighted` | local helper | `list` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 601 | `registry_entry_weight` | local helper | `entry, squad, context` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 622 | `pick_registry_entry` | local helper | `list, tried, squad, context` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 637 | `update_debug` | script hook/global | `squad` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 644 | `assign_rest` | local helper | `squad, reason` | Supports tasks subsystem behavior. |
| 652 | `mark_rest_trade_done` | local helper | `squad, result` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 662 | `mark_rest_trade_wait` | local helper | `squad, result` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 671 | `rest_trade_result_is_final` | local helper | `result` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 686 | `sync_rest_trade_done_from_economy` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 703 | `rest_trade_smart_available` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 712 | `try_auto_trade_at_rest_smart` | local helper | `squad, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 724 | `tick_rest_auto_trade` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 764 | `rest_trade_blocks_completion` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 786 | `try_after_night_rest_auto_trade` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 818 | `tick_base_camping_auto_trade` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 847 | `trade_route_allowed_from_context` | local helper | `context` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 852 | `trade_route_task_weight` | local helper | `squad, context, base_weight` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 867 | `trade_route_result_waiting` | local helper | `result` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 875 | `mark_trade_route_wait` | local helper | `squad, result` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 884 | `complete_trade_route` | local helper | `squad, result` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 896 | `sync_trade_route_done_from_economy` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 904 | `tick_trade_route` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 931 | `final_smart` | local helper | `p, squad, smart, opts` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 938 | `force_exit_target` | local helper | `squad` | Supports tasks subsystem behavior. |
| 977 | `target_blacklisted_for_squad` | local helper | `squad, target_id` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 994 | `task_target_blacklisted` | local helper | `squad` | Validates safety gates and controlled fallback conditions. |
| 1001 | `clear_post_guide_rest` | local helper | `squad, result` | Clears transient state, reservations, or stale runtime references. |
| 1013 | `post_guide_rest_target` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1046 | `apply_post_guide_rest` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1068 | `build_stalker_explore` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1080 | `build_stalker_populate` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1111 | `build_stalker_patrol` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1124 | `build_stalker_hunt` | local helper | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1141 | `build_stalker_artefact` | local helper | `squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1163 | `build_stalker_trade` | local helper | `squad, context` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1182 | `build_mutant_hunt` | local helper | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1199 | `build_mutant_patrol` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1212 | `build_mutant_explore` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1233 | `select_from_registry` | local helper | `pool, squad, context` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1253 | `select_stalker_task` | local helper | `squad, reason` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1271 | `select_stalker_night_rest` | script hook/global | `squad` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1311 | `select_mutant_task` | local helper | `squad, reason` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1328 | `mutant_night_hunt_only` | local helper | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1333 | `night_rest_target_unsafe` | local helper | `squad` | Validates safety gates and controlled fallback conditions. |
| 1344 | `assign_choice` | local helper | `squad, choice, fallback_reason` | Supports tasks subsystem behavior. |
| 1385 | `assign_stalker_hunt_or_rest` | local helper | `squad, reason` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1393 | `repair_invalid_mutant_task` | local helper | `squad` | Validates safety gates and controlled fallback conditions. |
| 1409 | `mutant_time_inactive` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1422 | `clear_zhopa2_movement_target` | local helper | `squad, clear_any` | Clears transient state, reservations, or stale runtime references. |
| 1449 | `pause_for_surge` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1480 | `park_inactive_mutant` | local helper | `squad` | Supports tasks subsystem behavior. |
| 1504 | `M.interrupt_task` | module export | `squad, task, target_id, duration_sec, reason, patrol, opts` | Supports tasks subsystem behavior. |
| 1545 | `M.assign_revenge_interrupt` | module export | `responder, offender_target_id` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1555 | `M.assign_base_camping_permanent` | module export | `squad, smart, reason` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1580 | `hunt_prey_for` | local helper | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1584 | `actor_target_alive` | local helper | `` | Supports tasks subsystem behavior. |
| 1602 | `game_vertex_level_id` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 1610 | `squad_community` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1627 | `same_smart_or_close` | local helper | `squad, target` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 1641 | `artefact_offline_collect_ready` | local helper | `squad` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 1658 | `factions_hostile` | local helper | `community_1, community_2` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1666 | `member_server_object` | local helper | `member` | Safely resolves an ALife/server-side object or runtime reference. |
| 1673 | `member_online_object` | local helper | `member` | Resolves an online game object through db.storage or level lookups. |
| 1685 | `is_inventory_owner_object` | local helper | `obj` | Supports tasks subsystem behavior. |
| 1700 | `member_inventory_owner_server_object` | local helper | `member` | Safely resolves an ALife/server-side object or runtime reference. |
| 1705 | `inventory_owner_target` | local helper | `target` | Supports tasks subsystem behavior. |
| 1715 | `force_goodwill` | local helper | `source, goodwill, target` | Supports tasks subsystem behavior. |
| 1728 | `is_online_relation_stalker` | local helper | `obj` | Supports tasks subsystem behavior. |
| 1739 | `online_relation_matches` | local helper | `source, target, relation` | Supports tasks subsystem behavior. |
| 1746 | `set_online_relation` | local helper | `source, target, relation, goodwill` | Supports tasks subsystem behavior. |
| 1763 | `force_member_to_actor` | local helper | `member` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1773 | `force_member_to_member` | local helper | `member_1, member_2, goodwill` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1796 | `actor_on_squad_level` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1806 | `current_actor_id` | local helper | `` | Supports tasks subsystem behavior. |
| 1817 | `current_actor_level_name` | local helper | `` | Resolves level, graph, route, distance, or position data. |
| 1834 | `actor_community_goodwill` | local helper | `community` | Supports tasks subsystem behavior. |
| 1842 | `set_actor_community_goodwill` | local helper | `community, goodwill` | Supports tasks subsystem behavior. |
| 1850 | `online_actor_goodwill` | local helper | `obj` | Supports tasks subsystem behavior. |
| 1867 | `restore_member_actor_goodwill` | local helper | `member_id, goodwill` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1879 | `squad_member_id_set` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1893 | `snapshot_member_actor_goodwill` | local helper | `member, bucket` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1906 | `for_each_actor_level_squad` | local helper | `fn` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1943 | `snapshot_actor_revenge_relation_scope` | local helper | `squad, scope` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 1978 | `ensure_actor_revenge_relation_scope` | local helper | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2006 | `stored_actor_revenge_relation_scope` | local helper | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2032 | `restore_actor_revenge_relation_scope` | local helper | `squad, force, include_revenge` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2056 | `clear_actor_revenge_relation_scope` | local helper | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2067 | `same_level_for_hostility` | local helper | `squad, target` | Resolves level, graph, route, distance, or position data. |
| 2075 | `M.apply_revenge_hostility` | module export | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2121 | `M.release_revenge_hostility` | module export | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2135 | `record_offline_combat_loot` | local helper | `squad, target, target_count_before, reason` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 2148 | `M.hunt_offline_tick` | module export | `squad, target, opts` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2194 | `M.hunt_target_valid` | module export | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2226 | `revenge_wait_route` | local helper | `squad, reason` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2234 | `M.revenge_target_valid` | module export | `squad` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2284 | `abort_hunt` | local helper | `squad, reason` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2295 | `complete_hunt` | local helper | `squad, mem, target_id, reason` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2312 | `complete_revenge` | local helper | `squad, mem, target_id, reason` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2326 | `complete_populate` | local helper | `squad, target_id` | Supports tasks subsystem behavior. |
| 2338 | `complete_artefact` | local helper | `squad, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2349 | `M.cancel_revenge` | module export | `squad, reason` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2358 | `M.release_artifact_task` | module export | `squad, reason` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 2380 | `M.assign_next_task` | module export | `squad, reason` | Supports tasks subsystem behavior. |
| 2402 | `M.update_squad` | module export | `squad, memory` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 2643 | `revenge_script_target_fallback` | local helper | `squad, route_reason` | Handles hostile target selection, revenge state, or pursuit behavior. |
| 2650 | `M.get_script_target` | module export | `squad` | Supports tasks subsystem behavior. |

### `gamedata/scripts/zhopa2_topology.script`

Role: level topology, neighbor levels, and route helpers.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 12 | `level_from_object` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 27 | `append_edge` | local helper | `map, source_level, dest_level` | Supports topology subsystem behavior. |
| 43 | `edge_sets_to_arrays` | local helper | `src` | Supports topology subsystem behavior. |
| 62 | `rebuild_neighbors` | local helper | `` | Supports topology subsystem behavior. |
| 76 | `get_utils_stpk` | local helper | `` | Supports topology subsystem behavior. |
| 90 | `get_level_changer_data` | local helper | `se_obj` | Resolves level, graph, route, distance, or position data. |
| 101 | `is_level_changer` | local helper | `se_obj, type_name` | Resolves level, graph, route, distance, or position data. |
| 116 | `remove_level_changer` | local helper | `se_obj` | Resolves level, graph, route, distance, or position data. |
| 145 | `set_level_changer` | local helper | `se_obj` | Resolves level, graph, route, distance, or position data. |
| 171 | `server_entity_on_register` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 177 | `server_entity_on_unregister` | local helper | `se_obj, type_name` | Maintains indexed runtime state by adding or removing entries. |
| 183 | `M.get_level_neighbors` | module export | `level_name` | Resolves level, graph, route, distance, or position data. |
| 190 | `M.get_revision` | module export | `` | Supports topology subsystem behavior. |
| 194 | `M.set_level_changer` | module export | `se_obj` | Resolves level, graph, route, distance, or position data. |
| 198 | `M.remove_level_changer` | module export | `se_obj` | Resolves level, graph, route, distance, or position data. |
| 202 | `M.on_game_start` | module export | `` | Runtime hook for topology lifecycle integration. |
| 214 | `on_game_start` | script hook/global | `` | Runtime hook for topology lifecycle integration. |

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
| 20 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the artifact flow diag subsystem. |
| 29 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 34 | `log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 45 | `tg` | local helper | `` | Supports artifact flow diag subsystem behavior. |
| 49 | `safe_require` | local helper | `name` | Validates safety gates and controlled fallback conditions. |
| 62 | `safe_field` | local helper | `obj, field` | Validates safety gates and controlled fallback conditions. |
| 72 | `safe_call` | local helper | `obj, fn_name, ...` | Validates safety gates and controlled fallback conditions. |
| 81 | `safe_alife_object` | local helper | `id` | Safely resolves an ALife/server-side object or runtime reference. |
| 90 | `online_object_by_id` | local helper | `id` | Resolves an online game object through db.storage or level lookups. |
| 106 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 127 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 143 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 166 | `object_level` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 200 | `object_parent_id` | local helper | `obj` | Supports artifact flow diag subsystem behavior. |
| 211 | `named_id` | local helper | `obj_or_id` | Formats names or display text for diagnostics and UI output. |
| 221 | `bool_text` | local helper | `value` | Formats names or display text for diagnostics and UI output. |
| 225 | `table_count` | local helper | `t` | Supports artifact flow diag subsystem behavior. |
| 233 | `sorted_keys` | local helper | `t` | Supports artifact flow diag subsystem behavior. |
| 244 | `vector_text` | local helper | `pos` | Formats names or display text for diagnostics and UI output. |
| 257 | `object_position` | local helper | `obj` | Resolves level, graph, route, distance, or position data. |
| 272 | `idx_mod` | local helper | `` | Supports artifact flow diag subsystem behavior. |
| 276 | `artifacts_mod` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 280 | `loot_mod` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 284 | `gather_mod` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 288 | `artifact_bucket_memberships` | local helper | `idx, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 300 | `artifact_pos` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 306 | `smart_pos` | local helper | `smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 312 | `squad_pos` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 316 | `artifact_bucket_match` | local helper | `idx, artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 326 | `artifact_state` | local helper | `artifact_id` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 353 | `smart_state` | local helper | `smart_id` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 368 | `squad_state` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 388 | `looter_squad` | local helper | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 403 | `gather_state` | local helper | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 425 | `storage_gather_state` | local helper | `npc` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 430 | `state_mgr_text` | local helper | `npc` | Reads, writes, clears, or migrates serializable runtime state. |
| 438 | `npc_position` | local helper | `npc` | Resolves level, graph, route, distance, or position data. |
| 446 | `online_item_pos` | local helper | `item_id` | Supports artifact flow diag subsystem behavior. |
| 451 | `distance_text` | local helper | `pos_a, pos_b` | Resolves level, graph, route, distance, or position data. |
| 459 | `route_summary` | local helper | `squad, npc, task_smart_id, artifact_id` | Resolves level, graph, route, distance, or position data. |
| 490 | `vertex_state` | local helper | `npc, vid` | Resolves level, graph, route, distance, or position data. |
| 504 | `gather_detail` | local helper | `npc, item_id, st` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 519 | `should_log_gather_execute` | local helper | `npc, st, item_id` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 533 | `patch_table_method` | local helper | `tbl, method, tag, wrapper` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 557 | `patch_global_function` | local helper | `name, wrapper` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 579 | `patch_exported_function` | local helper | `name, tag, wrapper` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 601 | `patch_index` | local helper | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 639 | `patch_artifacts` | local helper | `` | Handles artifact task state, bucket registration, cargo, pickup, or retargeting. |
| 678 | `patch_loot` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 710 | `patch_force_gather` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 742 | `patch_prepare_gather` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 768 | `patch_gather_item` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 794 | `patch_gather_find` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 833 | `patch_gather_evaluate` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 859 | `patch_gather_action` | local helper | `` | Handles loot target selection, pickup integration, accounting, or anti-loop cleanup. |
| 934 | `M.dump_all` | module export | `reason` | Supports artifact flow diag subsystem behavior. |
| 981 | `M.install` | module export | `source` | Supports artifact flow diag subsystem behavior. |
| 1016 | `unregister_update` | local helper | `` | Maintains indexed runtime state by adding or removing entries. |
| 1022 | `M.actor_on_update` | module export | `` | Runtime hook for artifact flow diag lifecycle integration. |
| 1043 | `M.actor_on_first_update` | module export | `` | Runtime hook for artifact flow diag lifecycle integration. |
| 1059 | `M.on_game_start` | module export | `` | Runtime hook for artifact flow diag lifecycle integration. |
| 1076 | `actor_on_first_update` | script hook/global | `` | Runtime hook for artifact flow diag lifecycle integration. |
| 1080 | `actor_on_update` | script hook/global | `` | Runtime hook for artifact flow diag lifecycle integration. |
| 1084 | `on_game_start` | script hook/global | `` | Runtime hook for artifact flow diag lifecycle integration. |

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
| 370 | `dump_level_bucket` | local helper | `name, bucket, resolver, level_map` | Resolves level, graph, route, distance, or position data. |
| 408 | `economy_mod` | local helper | `` | Supports bucket diag subsystem behavior. |
| 417 | `smart_id_for_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 421 | `target_id_for_squad` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 428 | `current_smart_for_squad` | local helper | `board, squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 436 | `trade_flags_for_smart` | local helper | `board, smart_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 443 | `trade_state_relevant` | local helper | `squad` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 453 | `pcall_profile` | local helper | `fn, ...` | Supports bucket diag subsystem behavior. |
| 464 | `online_member_count` | local helper | `economy, squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 475 | `dump_trade_squad_candidates` | local helper | `board` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 566 | `dump_prepared_trade_squads` | local helper | `board` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 640 | `dump_kind_bucket` | local helper | `board` | Supports bucket diag subsystem behavior. |
| 669 | `dump_trade_flags` | local helper | `board` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 716 | `dump_board_consistency` | local helper | `board` | Supports bucket diag subsystem behavior. |
| 760 | `dump_index_summary` | local helper | `` | Supports bucket diag subsystem behavior. |
| 793 | `dump_index_buckets` | local helper | `` | Supports bucket diag subsystem behavior. |
| 820 | `M.refresh_simboard_buckets` | module export | `` | Supports bucket diag subsystem behavior. |
| 829 | `M.refresh_trade_buckets` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 845 | `M.dump` | module export | `reason` | Supports bucket diag subsystem behavior. |
| 903 | `M.refresh_and_dump` | module export | `` | Supports bucket diag subsystem behavior. |
| 910 | `now_ms` | local helper | `` | Calculates time, cooldown, or tick-throttling values. |
| 914 | `M.actor_on_update` | module export | `` | Runtime hook for bucket diag lifecycle integration. |
| 936 | `M.actor_on_first_update` | module export | `` | Runtime hook for bucket diag lifecycle integration. |
| 953 | `M.on_game_start` | module export | `` | Runtime hook for bucket diag lifecycle integration. |
| 963 | `actor_on_first_update` | script hook/global | `` | Runtime hook for bucket diag lifecycle integration. |
| 967 | `actor_on_update` | script hook/global | `` | Runtime hook for bucket diag lifecycle integration. |
| 971 | `on_game_start` | script hook/global | `` | Runtime hook for bucket diag lifecycle integration. |

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
| 220 | `squad_relation_faction` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
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
| 59 | `cfg_mod` | local helper | `` | Reads or normalizes configuration data for the offline inventory diag subsystem. |
| 68 | `debug_print_enabled` | local helper | `` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 73 | `log` | local helper | `fmt, ...` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 84 | `safe_field` | local helper | `obj, field` | Validates safety gates and controlled fallback conditions. |
| 94 | `safe_call` | local helper | `obj, fn_name, ...` | Validates safety gates and controlled fallback conditions. |
| 106 | `object_id` | local helper | `obj` | Extracts a stable numeric id from supported object/id values. |
| 121 | `object_name` | local helper | `obj` | Formats names or display text for diagnostics and UI output. |
| 133 | `object_section` | local helper | `obj` | Resolves a safe section name for runtime classification. |
| 153 | `object_clsid` | local helper | `obj` | Supports offline inventory diag subsystem behavior. |
| 162 | `named_id` | local helper | `obj_or_id` | Formats names or display text for diagnostics and UI output. |
| 177 | `table_count` | local helper | `t` | Supports offline inventory diag subsystem behavior. |
| 185 | `sorted_keys` | local helper | `t` | Supports offline inventory diag subsystem behavior. |
| 196 | `member_server_object` | local helper | `member` | Safely resolves an ALife/server-side object or runtime reference. |
| 203 | `collect_squad_members` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 215 | `collect_child_ids` | local helper | `se_owner` | Supports offline inventory diag subsystem behavior. |
| 229 | `probe_value` | local helper | `obj, key, call_allowed` | Supports offline inventory diag subsystem behavior. |
| 244 | `probe_write_same` | local helper | `obj, key` | Supports offline inventory diag subsystem behavior. |
| 255 | `dump_owner_probes` | local helper | `se_owner, prefix` | Supports offline inventory diag subsystem behavior. |
| 271 | `dump_item_probes` | local helper | `se_item, prefix` | Supports offline inventory diag subsystem behavior. |
| 304 | `dump_member_inventory` | local helper | `squad, member, member_index` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 347 | `squad_online_state` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 356 | `squad_has_offline_member` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 367 | `M.dump` | module export | `` | Supports offline inventory diag subsystem behavior. |
| 410 | `M.dump_squad` | module export | `squad, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 433 | `M.dump_squad_on_update` | module export | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 452 | `M.actor_on_first_update` | module export | `` | Runtime hook for offline inventory diag lifecycle integration. |
| 459 | `M.on_game_start` | module export | `` | Runtime hook for offline inventory diag lifecycle integration. |
| 469 | `actor_on_first_update` | script hook/global | `` | Runtime hook for offline inventory diag lifecycle integration. |
| 473 | `on_game_start` | script hook/global | `` | Runtime hook for offline inventory diag lifecycle integration. |

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
| 664 | `service_slot_for_npc` | local helper | `smart, npc_id` | Supports trade route diag subsystem behavior. |
| 684 | `lower_text` | local helper | `value` | Formats names or display text for diagnostics and UI output. |
| 688 | `contains_plain` | local helper | `value, needle` | Supports trade route diag subsystem behavior. |
| 693 | `job_section` | local helper | `job` | Resolves a safe section name for runtime classification. |
| 700 | `job_ini_string` | local helper | `job, smart, field` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 719 | `job_is_trade_customer` | local helper | `job, smart` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 728 | `provider_role` | local helper | `job, smart` | Supports trade route diag subsystem behavior. |
| 769 | `find_trade_customer_job_diag` | local helper | `smart, npc_id` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 790 | `first_trade_provider_diag` | local helper | `smart, ignore_ids` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 817 | `binding_state` | local helper | `` | Reads, writes, clears, or migrates serializable runtime state. |
| 835 | `log_binding` | local helper | `stage, reason` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 845 | `unwrap_effect_wrappers` | local helper | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 855 | `M.trade_job_sell_items_diag_wrapper` | module export | `actor, npc, params` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 871 | `M.trade_job_give_id_diag_wrapper` | module export | `actor, npc, params` | Formats or emits debug/diagnostic output, normally gated by debug settings. |
| 887 | `install_effect_wrappers` | local helper | `reason` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 904 | `prepared_signature` | local helper | `squad` | Supports trade route diag subsystem behavior. |
| 920 | `dump_prepared_snapshot` | local helper | `squad, stage, reason` | Supports trade route diag subsystem behavior. |
| 1004 | `member_ids` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1019 | `online_members` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1038 | `inventory_scan` | local helper | `npc` | Supports trade route diag subsystem behavior. |
| 1048 | `scan` | local helper | `_, item` | Supports trade route diag subsystem behavior. |
| 1063 | `sell_plan_summary` | local helper | `npc` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1097 | `dump_members` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1123 | `id_set` | local helper | `ids` | Supports trade route diag subsystem behavior. |
| 1131 | `plain_online_members` | local helper | `squad` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1143 | `dump_trade_job_candidates` | local helper | `smart, stage, wanted_npc_id` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1196 | `dump_trade_intent_snapshot` | local helper | `squad, stage, reason, result_reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1280 | `registry_weight` | local helper | `entry, squad, context` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1303 | `dump_registry_weights` | local helper | `squad, reason` | Builds, scores, or selects candidates for weighted simulation decisions. |
| 1323 | `dump_trade_profile` | local helper | `squad, reason` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1351 | `dump_route_candidates` | local helper | `squad` | Resolves level, graph, route, distance, or position data. |
| 1392 | `M.dump_squad` | module export | `squad, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1430 | `M.dump_squad_id` | module export | `squad_id, reason` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1439 | `squad_from_board` | local helper | `id, stored` | Handles squad lookup, membership, task state, or squad-level accounting. |
| 1446 | `M.dump_all` | module export | `reason` | Supports trade route diag subsystem behavior. |
| 1477 | `patch_tasks` | local helper | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 1487 | `tasks.assign_next_task` | assigned wrapper | `squad, reason, ...` | Supports trade route diag subsystem behavior. |
| 1508 | `patch_economy` | local helper | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 1516 | `economy.trade_route_task_weight` | assigned wrapper | `squad, base_weight, opts, ...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1537 | `economy.patch_trade_effect` | assigned wrapper | `...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1549 | `economy.patch_trade_condition` | assigned wrapper | `...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1559 | `economy.try_auto_trade` | assigned wrapper | `squad, reason, opts, ...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1589 | `economy.try_auto_trade_npc` | assigned wrapper | `npc, trader, reason, opts, ...` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1618 | `patch_state_mgr` | local helper | `` | Installs or supports a chain-friendly runtime patch around vanilla behavior. |
| 1627 | `state_mgr.set_state` | assigned wrapper | `npc, state_name, callback, timeout, target, extra, ...` | Reads, writes, clears, or migrates serializable runtime state. |
| 1666 | `M.install` | module export | `` | Supports trade route diag subsystem behavior. |
| 1680 | `unregister_update` | local helper | `` | Maintains indexed runtime state by adding or removing entries. |
| 1686 | `M.watch_prepared_trades` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 1720 | `M.actor_on_update` | module export | `` | Runtime hook for trade route diag lifecycle integration. |
| 1744 | `M.actor_on_first_update` | module export | `` | Runtime hook for trade route diag lifecycle integration. |
| 1760 | `M.on_game_start` | module export | `` | Runtime hook for trade route diag lifecycle integration. |
| 1773 | `actor_on_first_update` | script hook/global | `` | Runtime hook for trade route diag lifecycle integration. |
| 1777 | `actor_on_update` | script hook/global | `` | Runtime hook for trade route diag lifecycle integration. |
| 1781 | `on_game_start` | script hook/global | `` | Runtime hook for trade route diag lifecycle integration. |

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
| 404 | `route_bucket_count` | local helper | `buckets` | Resolves level, graph, route, distance, or position data. |
| 414 | `flag_counts` | local helper | `flags_by_smart` | Supports trade smart diag subsystem behavior. |
| 444 | `dump_service_slots_for_smart` | local helper | `smart, tag` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 495 | `dump_route_buckets` | local helper | `board` | Resolves level, graph, route, distance, or position data. |
| 530 | `dump_flagged_smarts` | local helper | `board` | Handles smart-terrain lookup, job selection, base ownership, or service logic. |
| 561 | `M.dump` | module export | `reason` | Supports trade smart diag subsystem behavior. |
| 600 | `M.refresh_trade_smart_index` | module export | `` | Handles NPC trade policy, pricing, route selection, or payment accounting. |
| 616 | `M.refresh_and_dump` | module export | `` | Supports trade smart diag subsystem behavior. |
| 622 | `unregister_update` | local helper | `` | Maintains indexed runtime state by adding or removing entries. |
| 628 | `M.actor_on_update` | module export | `` | Runtime hook for trade smart diag lifecycle integration. |
| 647 | `M.actor_on_first_update` | module export | `` | Runtime hook for trade smart diag lifecycle integration. |
| 667 | `M.on_game_start` | module export | `` | Runtime hook for trade smart diag lifecycle integration. |
| 680 | `actor_on_first_update` | script hook/global | `` | Runtime hook for trade smart diag lifecycle integration. |
| 684 | `actor_on_update` | script hook/global | `` | Runtime hook for trade smart diag lifecycle integration. |
| 688 | `on_game_start` | script hook/global | `` | Runtime hook for trade smart diag lifecycle integration. |
