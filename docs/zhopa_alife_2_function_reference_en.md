# Z.H.O.P.A. ALIFE 2.0 Function Reference

[Architecture document](zhopa_alife_2_design_document_en.md)

This document describes every named function declaration and named function assignment found in the ZHOPA ALIFE 2.0 scripts. It covers runtime scripts under `gamedata/scripts` and diagnostic scripts under `debugscripts`. One-off anonymous closures used inline, for example `pcall(function() ... end)`, are intentionally excluded because they have no standalone name or callable contract.

- Runtime script functions: 1507
- Diagnostic script functions: 428
- Total documented named functions: 1935

## Reading Notes

- **Kind** describes how the function is declared: local helper, module export, script hook/global, or assigned wrapper.
- **Parameters** are copied from the declaration line and may omit internal closures or later vararg handling.
- **Description** is an operational summary based on the function name, module role, and surrounding subsystem. The Lua source remains the final authority for edge cases.

## Runtime Scripts

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_artifacts.script`

Role: artifact target selection, real/virtual artifact handling, and online/offline pickup flow.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 11 | `index_mod` | local helper | `` | Resolves the ZHOPA index module if it is loaded or can be required safely. |
| 20 | `perception_mod` | local helper | `` | Resolves the ZHOPA perception module if it is loaded or can be required safely. |
| 29 | `memory_mod` | local helper | `` | Resolves the ZHOPA memory module if it is loaded or can be required safely. |
| 38 | `loot_mod` | local helper | `` | Handles loot selection, pickup, accounting, or diagnostics in the artifact target selection module. |
| 47 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 56 | `debug_print_enabled` | local helper | `` | Checks whether ZHOPA debug output is enabled for this module. |
| 61 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 69 | `M.offline_enabled` | module export | `` | Internal helper for offline enabled in the artifact target selection module. |
| 73 | `gather_mod` | local helper | `` | Internal helper for gather mod in the artifact target selection module. |
| 85 | `now_ms` | local helper | `` | Returns the current game or device time in milliseconds for throttling and cooldown checks. |
| 89 | `runtime_ready` | local helper | `reason` | Checks the shared ZHOPA runtime readiness barrier before running context-dependent work. |
| 101 | `object_id` | local helper | `obj` | Extracts a stable numeric id from a server object, online object, id-like table, number, or string. |
| 118 | `object_section` | local helper | `obj` | Returns a safe section name for an object. |
| 137 | `object_clsid` | local helper | `obj` | Internal helper for object clsid in the artifact target selection module. |
| 148 | `online_object_by_id` | local helper | `id` | Returns an online game object by id through db.storage/level lookups. |
| 157 | `object_position` | local helper | `obj` | Internal helper for object position in the artifact target selection module. |
| 165 | `object_is_artifact` | local helper | `obj` | Handles artifact-related state in the artifact target selection module. |
| 170 | `item_cost` | local helper | `obj_or_section` | Internal helper for item cost in the artifact target selection module. |
| 190 | `artifact_valid` | local helper | `artifact_id` | Handles artifact-related state in the artifact target selection module. |
| 204 | `artifact_same_level_as_squad` | local helper | `squad, artifact_id` | Handles artifact-related state in the artifact target selection module. |
| 218 | `artifact_target_blacklisted` | local helper | `squad, smart` | Handles artifact-related state in the artifact target selection module. |
| 234 | `artifact_id_target_blacklisted` | local helper | `squad, artifact_id` | Handles artifact-related state in the artifact target selection module. |
| 250 | `object_name` | local helper | `obj` | Returns a safe display name for an object or id. |
| 263 | `named_id` | local helper | `id` | Formats an object or id as a compact diagnostic name/id string. |
| 272 | `bool_text` | local helper | `value` | Internal helper for bool text in the artifact target selection module. |
| 276 | `artifact_bucket_debug` | local helper | `idx, smart_id, focus_id` | Handles artifact-related state in the artifact target selection module. |
| 309 | `artifact_pool_debug` | local helper | `idx` | Handles artifact-related state in the artifact target selection module. |
| 329 | `artifact_object_debug` | local helper | `idx, artifact_id` | Handles artifact-related state in the artifact target selection module. |
| 352 | `debug_artifact_error` | local helper | `squad, reason, artifact_id, npc, extra` | Handles artifact-related state in the artifact target selection module. |
| 389 | `debug_artifact_offline_success` | local helper | `squad, artifact_id, section` | Handles artifact-related state in the artifact target selection module. |
| 406 | `squad_has_artifact_cargo` | local helper | `squad, artifact_id` | Handles artifact-related state in the artifact target selection module. |
| 411 | `squad_member_server` | local helper | `squad, prefer_id` | Handles squad lookup, state, membership, or task coordination. |
| 430 | `squad_member_online_object` | local helper | `member` | Handles squad lookup, state, membership, or task coordination. |
| 442 | `squad_member_alive_online` | local helper | `obj` | Handles squad lookup, state, membership, or task coordination. |
| 450 | `add_online_looter` | local helper | `list, seen, obj` | Handles loot selection, pickup, accounting, or diagnostics in the artifact target selection module. |
| 458 | `squad_online_looters` | local helper | `squad, prefer_id` | Handles loot selection, pickup, accounting, or diagnostics in the artifact target selection module. |
| 477 | `release_artifact_reservation` | local helper | `squad, reason` | Releases artifact reservation and removes ownership/reservation state. |
| 485 | `add_artifact_cargo` | local helper | `squad, section, value, artifact_id, reason` | Handles artifact-related state in the artifact target selection module. |
| 499 | `reset_online_target_tracking` | local helper | `squad` | Resets online target tracking to its default safe state. |
| 509 | `clear_online_approach_fields` | local helper | `squad` | Clears online approach fields from module or squad state. |
| 527 | `remember_artifact_reservation` | local helper | `squad, artifact_id` | Handles artifact-related state in the artifact target selection module. |
| 549 | `sync_task_artifact_metadata` | local helper | `squad, artifact_id` | Synchronizes task artifact metadata between memory, indexes, and runtime state. |
| 589 | `artifact_matches_task_smart` | local helper | `squad, artifact_id` | Handles artifact-related state in the artifact target selection module. |
| 604 | `artifact_from_task_smart` | local helper | `squad` | Handles artifact-related state in the artifact target selection module. |
| 627 | `recover_task_artifact_id` | local helper | `squad` | Handles artifact-related state in the artifact target selection module. |
| 646 | `cancel_online_pickup` | local helper | `squad` | Cancels online pickup and clears or releases related state. |
| 656 | `recover_vanilla_artifact_pickup` | local helper | `squad, artifact_id` | Handles artifact-related state in the artifact target selection module. |
| 665 | `online_inventory_recovery_pending` | local helper | `squad` | Scans, classifies, or mutates NPC/server inventory state. |
| 688 | `clear_online_pickup_state` | local helper | `squad` | Clears online pickup state from module or squad state. |
| 704 | `retarget_missing_artifact_to_current_smart` | local helper | `squad, old_artifact_id, reason` | Handles artifact-related state in the artifact target selection module. |
| 738 | `gather_item_active` | local helper | `npc, artifact_id` | Internal helper for gather item active in the artifact target selection module. |
| 748 | `gather_item_failure_reason` | local helper | `npc, artifact_id` | Internal helper for gather item failure reason in the artifact target selection module. |
| 758 | `gather_item_debug_status` | local helper | `npc, artifact_id` | Controls debug output or debug-only state for diagnostics. |
| 768 | `pickup_stalled` | local helper | `squad, npc, now` | Internal helper for pickup stalled in the artifact target selection module. |
| 816 | `online_pickup_pending` | local helper | `squad, artifact_id` | Internal helper for online pickup pending in the artifact target selection module. |
| 848 | `online_arrived_idle_timeout` | local helper | `squad, artifact_id, reason, allow_started` | Internal helper for online arrived idle timeout in the artifact target selection module. |
| 882 | `current_artifact_id` | assigned wrapper | `squad` | Handles artifact-related state in the artifact target selection module. |
| 900 | `online_artifact_pickup_ready` | local helper | `squad, artifact_id` | Handles artifact-related state in the artifact target selection module. |
| 918 | `all_failures_contested` | local helper | `failures` | Internal helper for all failures contested in the artifact target selection module. |
| 930 | `call_parent_zone_take` | local helper | `se_artifact` | Internal helper for call parent zone take in the artifact target selection module. |
| 944 | `release_ground_artifact` | local helper | `se_artifact` | Releases ground artifact and removes ownership/reservation state. |
| 954 | `virtual_artifact_data` | local helper | `artifact_id` | Handles artifact-related state in the artifact target selection module. |
| 962 | `unregister_virtual_artifact` | local helper | `artifact_id, reason` | Unregisters virtual artifact and cleans stale references. |
| 970 | `materialize_virtual_artifact_online` | local helper | `squad, artifact_id` | Handles artifact-related state in the artifact target selection module. |
| 994 | `M.release_reservation` | module export | `squad, reason` | Releases reservation and removes ownership/reservation state. |
| 998 | `M.pick_target` | module export | `squad, opts` | Selects target from validated candidates. |
| 1058 | `M.offline_collect` | module export | `squad, artifact_id, reason` | Internal helper for offline collect in the artifact target selection module. |
| 1113 | `M.offline_collect_virtual` | module export | `squad, artifact_id, reason` | Internal helper for offline collect virtual in the artifact target selection module. |
| 1168 | `M.try_collect` | module export | `squad` | Attempts collect and returns a controlled result instead of hard-failing. |
| 1332 | `M.complete` | module export | `squad, reason` | Internal helper for complete in the artifact target selection module. |
| 1343 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 1348 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_bootstrap.script`

Role: bootstrap entry point that starts the runtime patch orchestrator.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 1 | `runtime_patches` | local helper | `` | Internal helper for runtime patches in the bootstrap entry point that starts the runtime patch orchestrator module. |
| 12 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_cfg.script`

Role: configuration defaults, MCM-backed getters, blacklists, aliases, and numeric settings.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 86 | `section_faction` | local helper | `section` | Internal helper for section faction in the configuration defaults module. |
| 94 | `squad_section_name` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 112 | `squad_faction` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 123 | `is_monster_or_zombied` | local helper | `squad` | Checks whether monster or zombied in the configuration defaults context. |
| 139 | `bool_from_value` | local helper | `v, default` | Internal helper for bool from value in the configuration defaults module. |
| 150 | `mcm_path_for_key` | local helper | `key` | Builds or reads MCM configuration data. |
| 158 | `read_mcm` | local helper | `key` | Reads mcm from serialized state, config, or engine data. |
| 176 | `read_ltx` | local helper | `key, default` | Reads ltx from serialized state, config, or engine data. |
| 190 | `get` | script hook/global | `key, default` | Internal helper for get in the configuration defaults module. |
| 203 | `get_bool` | script hook/global | `key, default` | Returns bool for the current configuration defaults state. |
| 207 | `get_num` | script hook/global | `key, default` | Returns num for the current configuration defaults state. |
| 211 | `get_string` | script hook/global | `key, default` | Returns string for the current configuration defaults state. |
| 216 | `get_faction_alias` | script hook/global | `faction` | Returns faction alias for the current configuration defaults state. |
| 224 | `reset_blacklist_cache` | local helper | `` | Resets blacklist cache to its default safe state. |
| 229 | `cache_key` | local helper | `section, key` | Internal helper for cache key in the configuration defaults module. |
| 233 | `section_value` | local helper | `section, key` | Internal helper for section value in the configuration defaults module. |
| 247 | `list_set` | local helper | `value` | Internal helper for list set in the configuration defaults module. |
| 267 | `section_set` | local helper | `section, key` | Internal helper for section set in the configuration defaults module. |
| 278 | `section_has` | local helper | `section, key, value` | Internal helper for section has in the configuration defaults module. |
| 289 | `section_is_true` | local helper | `section, key` | Internal helper for section is true in the configuration defaults module. |
| 294 | `smart_name_for_blacklist` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 315 | `is_global_level_blacklisted` | script hook/global | `level_name` | Checks whether global level blacklisted in the configuration defaults context. |
| 319 | `is_level_blacklisted_for_squad` | script hook/global | `squad, level_name` | Checks whether level blacklisted for squad in the configuration defaults context. |
| 342 | `is_smart_blacklisted_for_squad` | script hook/global | `squad, smart, level_name` | Checks whether smart blacklisted for squad in the configuration defaults context. |
| 374 | `reload` | script hook/global | `` | Internal helper for reload in the configuration defaults module. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_debug_hud.script`

Role: map/debug HUD rendering and cleanup for ZHOPA squad state.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 24 | `enabled` | local helper | `` | Internal helper for enabled in the map/debug HUD rendering and cleanup for ZHOPA squad state module. |
| 32 | `is_monster_squad` | local helper | `squad` | Checks whether monster squad in the map/debug HUD rendering and cleanup for ZHOPA squad state context. |
| 52 | `spot_for_squad` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 64 | `forget_spot_owner` | local helper | `id, squad_id` | Internal helper for forget spot owner in the map/debug HUD rendering and cleanup for ZHOPA squad state module. |
| 81 | `remove_spot` | local helper | `id, squad_id` | Internal helper for remove spot in the map/debug HUD rendering and cleanup for ZHOPA squad state module. |
| 95 | `cleanup_squad_id` | script hook/global | `squad_id` | Cleans up squad id and removes stale runtime state. |
| 109 | `smart_name` | local helper | `id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 114 | `perception` | local helper | `` | Internal helper for perception in the map/debug HUD rendering and cleanup for ZHOPA squad state module. |
| 123 | `elapsed_time` | local helper | `started` | Internal helper for elapsed time in the map/debug HUD rendering and cleanup for ZHOPA squad state module. |
| 135 | `obj_level` | local helper | `obj` | Resolves or validates level names, ids, or level buckets. |
| 143 | `format_time` | local helper | `sec` | Formats time for logging or display. |
| 151 | `pad2` | local helper | `value` | Internal helper for pad2 in the map/debug HUD rendering and cleanup for ZHOPA squad state module. |
| 164 | `route_state` | local helper | `squad` | Builds, validates, or diagnoses a route. |
| 181 | `task_timer` | local helper | `squad` | Internal helper for task timer in the map/debug HUD rendering and cleanup for ZHOPA squad state module. |
| 194 | `base_ownership` | local helper | `squad` | Internal helper for base ownership in the map/debug HUD rendering and cleanup for ZHOPA squad state module. |
| 208 | `base_presence` | local helper | `squad` | Internal helper for base presence in the map/debug HUD rendering and cleanup for ZHOPA squad state module. |
| 219 | `story_status_line` | local helper | `squad` | Handles story-gated state, tasks, or diagnostic output. |
| 233 | `build_hint` | local helper | `squad` | Builds hint for the current map/debug HUD rendering and cleanup for ZHOPA squad state flow. |
| 259 | `update_squad` | script hook/global | `squad` | Updates squad during the module tick or callback flow. |
| 321 | `cleanup_squad` | script hook/global | `squad` | Cleans up squad and removes stale runtime state. |
| 333 | `cleanup_all` | script hook/global | `` | Cleans up all and removes stale runtime state. |
| 340 | `actor_on_first_update` | script hook/global | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 344 | `on_game_load` | script hook/global | `` | Game-load callback; schedules reconciliation or clears stale runtime-only state after loading a save. |
| 348 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_economy.script`

Role: online/offline NPC economy, trade routing, sell/buy policy, money, and dynamic news feedback.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 66 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 75 | `M.perception_mod` | module export | `` | Resolves the ZHOPA perception module if it is loaded or can be required safely. |
| 84 | `runtime_mod` | local helper | `` | Internal helper for runtime mod in the online/offline NPC economy module. |
| 93 | `runtime_ready` | local helper | `reason` | Checks the shared ZHOPA runtime readiness barrier before running context-dependent work. |
| 105 | `runtime_not_ready_reason` | local helper | `` | Internal helper for runtime not ready reason in the online/offline NPC economy module. |
| 117 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 125 | `debug_print_enabled` | local helper | `` | Checks whether ZHOPA debug output is enabled for this module. |
| 129 | `M.enabled` | module export | `` | Internal helper for enabled in the online/offline NPC economy module. |
| 133 | `M.squad_trade_allowed` | module export | `squad` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 150 | `tg` | local helper | `` | Returns the current time value used by throttled diagnostics. |
| 154 | `ensure_trade_ini` | local helper | `` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 174 | `clear_table` | local helper | `t` | Clears table from module or squad state. |
| 183 | `slower` | local helper | `value` | Internal helper for slower in the online/offline NPC economy module. |
| 187 | `contains_plain` | local helper | `haystack, needle` | Internal helper for contains plain in the online/offline NPC economy module. |
| 191 | `M.emit_trade_event_text` | module export | `text` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 212 | `M.queue_trade_event` | module export | `text` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 219 | `M.flush_trade_events` | module export | `` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 231 | `M.print_trade_event` | module export | `fmt, ...` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 244 | `print_trade_error` | local helper | `fmt, ...` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 255 | `object_id` | local helper | `obj` | Extracts a stable numeric id from a server object, online object, id-like table, number, or string. |
| 278 | `object_section` | local helper | `obj` | Returns a safe section name for an object. |
| 297 | `object_clsid` | local helper | `obj` | Internal helper for object clsid in the online/offline NPC economy module. |
| 313 | `object_name` | local helper | `obj` | Returns a safe display name for an object or id. |
| 332 | `M.is_squad_object` | module export | `squad` | Checks whether squad object in the online/offline NPC economy context. |
| 341 | `online_object_by_id` | local helper | `id` | Returns an online game object by id through db.storage/level lookups. |
| 352 | `server_object_by_id` | local helper | `id` | Internal helper for server object by id in the online/offline NPC economy module. |
| 360 | `live_object` | local helper | `obj` | Internal helper for live object in the online/offline NPC economy module. |
| 373 | `read_ini_string_from` | local helper | `ini, section, key` | Reads ini string from from serialized state, config, or engine data. |
| 391 | `read_job_ini_string` | local helper | `job_or_section, key, smart` | Reads job ini string from serialized state, config, or engine data. |
| 414 | `find_smart_job_by_section` | local helper | `smart, section` | Finds smart job by section in indexed, runtime, or engine data. |
| 428 | `item_in_slots` | local helper | `npc, item_id` | Internal helper for item in slots in the online/offline NPC economy module. |
| 441 | `active_item` | local helper | `npc` | Internal helper for active item in the online/offline NPC economy module. |
| 454 | `best_weapon` | local helper | `npc` | Classifies or protects weapon inventory state. |
| 464 | `active_item_id` | local helper | `npc` | Internal helper for active item id in the online/offline NPC economy module. |
| 468 | `buy_sell_params` | local helper | `section` | Internal helper for buy sell params in the online/offline NPC economy module. |
| 520 | `sys_string` | local helper | `section, key` | Internal helper for sys string in the online/offline NPC economy module. |
| 531 | `sys_float` | local helper | `section, key, default` | Internal helper for sys float in the online/offline NPC economy module. |
| 542 | `is_item_type` | local helper | `typ, section, obj` | Checks whether item type in the online/offline NPC economy context. |
| 553 | `object_is_weapon` | local helper | `item` | Classifies or protects weapon inventory state. |
| 561 | `object_is_outfit` | local helper | `item` | Classifies or protects outfit inventory state. |
| 569 | `object_is_headgear` | local helper | `item` | Internal helper for object is headgear in the online/offline NPC economy module. |
| 577 | `item_kind` | local helper | `section` | Internal helper for item kind in the online/offline NPC economy module. |
| 581 | `section_has_prefix` | local helper | `section, prefix` | Internal helper for section has prefix in the online/offline NPC economy module. |
| 585 | `section_contains` | local helper | `section, needle` | Internal helper for section contains in the online/offline NPC economy module. |
| 589 | `M.npc_sell_price_multiplier` | module export | `` | Internal helper for npc sell price multiplier in the online/offline NPC economy module. |
| 599 | `item_condition` | local helper | `item` | Internal helper for item condition in the online/offline NPC economy module. |
| 626 | `item_cost` | local helper | `item, section` | Internal helper for item cost in the online/offline NPC economy module. |
| 642 | `section_is_ammo` | local helper | `section` | Classifies, counts, sells, or buys ammunition for NPC supply logic. |
| 646 | `section_is_degraded_ammo` | local helper | `section` | Classifies, counts, sells, or buys ammunition for NPC supply logic. |
| 650 | `section_is_clean_buckshot` | local helper | `section` | Internal helper for section is clean buckshot in the online/offline NPC economy module. |
| 657 | `section_is_clean_fmj` | local helper | `section` | Internal helper for section is clean fmj in the online/offline NPC economy module. |
| 663 | `section_is_disfavored_fallback_ammo` | local helper | `section` | Classifies, counts, sells, or buys ammunition for NPC supply logic. |
| 678 | `section_is_needed_ammo` | local helper | `section, needed_ammo` | Classifies, counts, sells, or buys ammunition for NPC supply logic. |
| 682 | `ammo_candidate` | local helper | `section` | Classifies, counts, sells, or buys ammunition for NPC supply logic. |
| 689 | `pick_buy_ammo` | local helper | `weapon_ammo` | Selects buy ammo from validated candidates. |
| 715 | `preferred_ammo_for_weapon_section` | local helper | `weapon_section` | Classifies, counts, sells, or buys ammunition for NPC supply logic. |
| 726 | `needed_ammo_for_npc` | local helper | `npc` | Classifies, counts, sells, or buys ammunition for NPC supply logic. |
| 734 | `add_weapon_ammo` | local helper | `weapon` | Classifies, counts, sells, or buys ammunition for NPC supply logic. |
| 764 | `section_is_grenade` | local helper | `section` | Internal helper for section is grenade in the online/offline NPC economy module. |
| 772 | `section_is_bandage` | local helper | `section` | Internal helper for section is bandage in the online/offline NPC economy module. |
| 776 | `section_is_medkit` | local helper | `section` | Internal helper for section is medkit in the online/offline NPC economy module. |
| 780 | `section_is_other_med` | local helper | `section` | Internal helper for section is other med in the online/offline NPC economy module. |
| 807 | `section_is_food` | local helper | `section` | Internal helper for section is food in the online/offline NPC economy module. |
| 814 | `section_is_drink` | local helper | `section` | Internal helper for section is drink in the online/offline NPC economy module. |
| 824 | `section_is_never_sell` | local helper | `section, item` | Internal helper for section is never sell in the online/offline NPC economy module. |
| 836 | `section_is_upgrade` | local helper | `section` | Internal helper for section is upgrade in the online/offline NPC economy module. |
| 840 | `section_is_artifact` | local helper | `section` | Handles artifact-related state in the online/offline NPC economy module. |
| 844 | `section_is_mutant_part` | local helper | `section` | Internal helper for section is mutant part in the online/offline NPC economy module. |
| 849 | `trade_smart_for_npc` | local helper | `npc, params` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 862 | `trade_seller_for_npc` | local helper | `npc, params` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 891 | `add_plan_item` | local helper | `plan, item, section, reason` | Internal helper for add plan item in the online/offline NPC economy module. |
| 899 | `mark_surplus` | local helper | `entries, keep_count, plan, reason` | Marks surplus for later processing or diagnostics. |
| 911 | `classify_provider_job_role` | local helper | `job_or_section, smart` | Internal helper for classify provider job role in the online/offline NPC economy module. |
| 978 | `resolve_npc_provider_role` | local helper | `npc, smart, npc_id` | Resolves npc provider role into a usable runtime object or value. |
| 1006 | `M.provider_role` | module export | `npc, smart` | Internal helper for provider role in the online/offline NPC economy module. |
| 1010 | `npc_service_candidate_blocked` | local helper | `npc, npc_id, params` | Internal helper for npc service candidate blocked in the online/offline NPC economy module. |
| 1035 | `npc_is_trade_provider` | local helper | `npc, smart` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 1063 | `M.build_online_sell_plan` | module export | `npc, params` | Builds online sell plan for the current online/offline NPC economy flow. |
| 1091 | `add_generic` | local helper | `item, section, params` | Internal helper for add generic in the online/offline NPC economy module. |
| 1107 | `scan` | local helper | `_, item` | Internal helper for scan in the online/offline NPC economy module. |
| 1210 | `M.online_trade_sell_item_price` | module export | `npc, trader, item` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 1222 | `M.online_trade_buy_item_price` | module export | `npc, trader, item` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 1234 | `M.online_trade_buy_section_price` | module export | `section` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 1243 | `sell_plan_should_start_auto_trade` | local helper | `npc, plan` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 1260 | `inventory_section_counts` | local helper | `npc` | Scans, classifies, or mutates NPC/server inventory state. |
| 1265 | `scan` | local helper | `_, item` | Internal helper for scan in the online/offline NPC economy module. |
| 1275 | `npc_money` | local helper | `npc` | Reads, writes, or transfers NPC money/economy state. |
| 1285 | `transfer_money_between` | local helper | `from_npc, to_npc, amount` | Reads, writes, or transfers NPC money/economy state. |
| 1297 | `transfer_all_money_to` | local helper | `from_npc, to_npc` | Reads, writes, or transfers NPC money/economy state. |
| 1305 | `transfer_trade_money` | local helper | `npc, trader, price` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 1313 | `spawn_trade_item_to_npc` | local helper | `npc, section` | Spawns trade item to npc through guarded server-side creation logic. |
| 1321 | `dynamic_news_nearby_activity_enabled` | local helper | `` | Internal helper for dynamic news nearby activity enabled in the online/offline NPC economy module. |
| 1329 | `emit_bought_items_news` | local helper | `npc, trader, bought_items` | Internal helper for emit bought items news in the online/offline NPC economy module. |
| 1347 | `buy_missing_section` | local helper | `npc, trader, section, target_count, counts, payer, bought_items` | Internal helper for buy missing section in the online/offline NPC economy module. |
| 1374 | `ammo_buy_target` | local helper | `bs` | Classifies, counts, sells, or buys ammunition for NPC supply logic. |
| 1382 | `M.execute_online_buy` | module export | `npc, trader, opts` | Internal helper for execute online buy in the online/offline NPC economy module. |
| 1413 | `build_online_buy_needs` | local helper | `npc, counts` | Builds online buy needs for the current online/offline NPC economy flow. |
| 1416 | `add_need` | local helper | `section, target` | Internal helper for add need in the online/offline NPC economy module. |
| 1436 | `offline_money_value` | local helper | `section` | Reads, writes, or transfers NPC money/economy state. |
| 1440 | `offline_round_money` | local helper | `amount` | Reads, writes, or transfers NPC money/economy state. |
| 1445 | `offline_trade_item_price` | local helper | `item` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 1453 | `offline_buy_section_price` | local helper | `section` | Internal helper for offline buy section price in the online/offline NPC economy module. |
| 1457 | `offline_collect_members` | local helper | `squad` | Handles squad member lookup, inventory ownership, or relation state. |
| 1484 | `offline_member_children` | local helper | `member` | Handles squad member lookup, inventory ownership, or relation state. |
| 1501 | `offline_collect_wallet` | local helper | `members` | Internal helper for offline collect wallet in the online/offline NPC economy module. |
| 1526 | `offline_spawn_money_to_member` | local helper | `member, amount` | Handles squad member lookup, inventory ownership, or relation state. |
| 1551 | `offline_take_money_from_wallet` | local helper | `wallet, amount, change_owner` | Reads, writes, or transfers NPC money/economy state. |
| 1616 | `section_is_weapon_entry` | local helper | `section, item` | Classifies or protects weapon inventory state. |
| 1625 | `section_is_outfit_entry` | local helper | `section, item` | Classifies or protects outfit inventory state. |
| 1637 | `section_is_headgear_entry` | local helper | `section, item` | Internal helper for section is headgear entry in the online/offline NPC economy module. |
| 1650 | `offline_gear_score` | local helper | `item, section, ammo_counts` | Internal helper for offline gear score in the online/offline NPC economy module. |
| 1659 | `offline_best_gear` | local helper | `member, children` | Internal helper for offline best gear in the online/offline NPC economy module. |
| 1675 | `add_candidate` | local helper | `list, item, section` | Internal helper for add candidate in the online/offline NPC economy module. |
| 1702 | `keep_best` | local helper | `list` | Internal helper for keep best in the online/offline NPC economy module. |
| 1725 | `add_ammo` | local helper | `entry` | Classifies, counts, sells, or buys ammunition for NPC supply logic. |
| 1736 | `offline_needed_ammo_for_gear` | local helper | `gear` | Classifies, counts, sells, or buys ammunition for NPC supply logic. |
| 1740 | `offline_build_sell_plan` | local helper | `members` | Internal helper for offline build sell plan in the online/offline NPC economy module. |
| 1754 | `add_member_plan` | local helper | `item, section, reason` | Handles squad member lookup, inventory ownership, or relation state. |
| 1815 | `offline_sell_plan_should_start` | local helper | `plan` | Internal helper for offline sell plan should start in the online/offline NPC economy module. |
| 1831 | `offline_build_buy_needs` | local helper | `members` | Internal helper for offline build buy needs in the online/offline NPC economy module. |
| 1845 | `add_need` | local helper | `section, target` | Internal helper for add need in the online/offline NPC economy module. |
| 1864 | `offline_trade_detail_list` | local helper | `entries, field, max_count` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 1880 | `set_offline_trade_detail` | local helper | `squad, result, members, plan, wallet, needs` | Sets offline trade detail for the current online/offline NPC economy state. |
| 1902 | `execute_offline_sell_plan` | local helper | `plan, pay_to` | Internal helper for execute offline sell plan in the online/offline NPC economy module. |
| 1930 | `execute_offline_buy_needs` | local helper | `members, needs, payer` | Internal helper for execute offline buy needs in the online/offline NPC economy module. |
| 1968 | `M.offline_squad_has_trade_work` | module export | `squad, smart` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 1999 | `M.execute_offline_squad_trade` | module export | `squad, smart, reason` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2043 | `release_online_money_note` | local helper | `item` | Releases online money note and removes ownership/reservation state. |
| 2052 | `offline_transfer_money_notes_to_online_npc` | local helper | `npc` | Reads, writes, or transfers NPC money/economy state. |
| 2058 | `scan` | local helper | `_, item` | Internal helper for scan in the online/offline NPC economy module. |
| 2091 | `M.convert_online_money_notes` | module export | `npc` | Reads, writes, or transfers NPC money/economy state. |
| 2098 | `clear_npc_trade_state` | local helper | `npc` | Clears npc trade state from module or squad state. |
| 2117 | `suppress_npc_trade_state` | local helper | `npc, until_tg` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2128 | `trade_context_active` | local helper | `st` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2132 | `squad_accepts_managed_trade_signal` | local helper | `squad` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2136 | `squad_for_online_npc` | local helper | `npc` | Handles squad lookup, state, membership, or task coordination. |
| 2149 | `set_trade_job_idle` | local helper | `npc, params` | Sets trade job idle for the current online/offline NPC economy state. |
| 2159 | `execute_online_sell_only` | local helper | `npc, trader, params, collect_to` | Internal helper for execute online sell only in the online/offline NPC economy module. |
| 2202 | `M.execute_online_trade_with_trader` | module export | `npc, trader, params, opts` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2227 | `M.execute_online_trade` | module export | `npc, params, opts` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2236 | `squad_member_id_set` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 2253 | `trade_result_terminal` | local helper | `result` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2261 | `clear_squad_prepared_trade_state` | local helper | `squad` | Clears squad prepared trade state from module or squad state. |
| 2272 | `finalize_squad_trade_task` | local helper | `squad, result, reason` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2293 | `mark_squad_trade_result` | assigned wrapper | `squad, result, reason, smart` | Marks squad trade result for later processing or diagnostics. |
| 2308 | `online_squad_trade_members` | local helper | `squad, smart` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2326 | `online_trade_members_from_ids` | local helper | `member_ids` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2340 | `squad_trade_member_ids` | local helper | `members` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2351 | `trade_member_ids_count` | local helper | `member_ids` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2355 | `ensure_trade_source_member` | local helper | `members, source_npc` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2374 | `find_online_squad_trade_npc` | local helper | `squad, smart` | Finds online squad trade npc in indexed, runtime, or engine data. |
| 2379 | `squad_members_money` | local helper | `members` | Handles squad lookup, state, membership, or task coordination. |
| 2387 | `squad_members_have_trade_work` | local helper | `members` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2412 | `M._online_squad_members` | module export | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 2430 | `M._online_trade_profile` | module export | `members` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2471 | `M._offline_trade_profile` | module export | `squad` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2509 | `M.squad_trade_route_profile` | module export | `squad` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2523 | `find_online_trader_at_smart` | local helper | `smart, ignore_ids` | Finds online trader at smart in indexed, runtime, or engine data. |
| 2528 | `check_id` | local helper | `npc_id` | Internal helper for check id in the online/offline NPC economy module. |
| 2563 | `smart_trade_flags` | local helper | `smart` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2577 | `smart_has_indexed_trade_route` | local helper | `smart` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2582 | `smart_has_trade_provider_job` | local helper | `smart` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2614 | `job_is_trade_customer` | local helper | `job, smart` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2627 | `smart_has_trade_customer_job` | local helper | `smart` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2651 | `find_trade_customer_job` | local helper | `smart, npc_id` | Finds trade customer job in indexed, runtime, or engine data. |
| 2673 | `smart_has_vanilla_trade_route` | local helper | `smart` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2677 | `queue_remove_squad` | local helper | `q, squad_id` | Handles squad lookup, state, membership, or task coordination. |
| 2690 | `queue_contains_squad` | local helper | `q, squad_id` | Handles squad lookup, state, membership, or task coordination. |
| 2702 | `smart_trade_queue` | local helper | `smart_id` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2711 | `mark_squad_queue_state` | local helper | `squad, state, smart_id, reason` | Marks squad queue state for later processing or diagnostics. |
| 2720 | `acquire_smart_trade_slot` | local helper | `squad, smart, reason, now` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 2756 | `release_smart_trade_slot` | local helper | `smart_id, squad_id` | Releases smart trade slot and removes ownership/reservation state. |
| 2778 | `set_smart_trade_slot_remaining` | local helper | `smart_id, squad_id, count` | Sets smart trade slot remaining for the current online/offline NPC economy state. |
| 2785 | `set_squad_trade_cooldown` | local helper | `squad, now` | Sets squad trade cooldown for the current online/offline NPC economy state. |
| 2792 | `smart_by_id` | local helper | `id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 2803 | `trade_path.force_until` | script hook/global | `` | Internal helper for force until in the online/offline NPC economy module. |
| 2807 | `trade_path.trim` | script hook/global | `value` | Internal helper for trim in the online/offline NPC economy module. |
| 2811 | `trade_path.npc_name` | script hook/global | `npc` | Internal helper for npc name in the online/offline NPC economy module. |
| 2821 | `trade_path.has_patrol_mode` | script hook/global | `npc` | Checks whether patrol mode is present in the online/offline NPC economy context. |
| 2829 | `trade_path.set_patrol_mode` | script hook/global | `npc, enabled` | Sets patrol mode for the current online/offline NPC economy state. |
| 2842 | `trade_path.save_point` | script hook/global | `npc, index, value` | Saves point for the online/offline NPC economy module. |
| 2854 | `trade_path.clear` | script hook/global | `npc, st` | Internal helper for clear in the online/offline NPC economy module. |
| 2872 | `trade_path.ini_string` | script hook/global | `ini, section, field` | Internal helper for ini string in the online/offline NPC economy module. |
| 2880 | `trade_path.parse_pos` | script hook/global | `line` | Parses pos from config, string, or diagnostic input. |
| 2892 | `trade_path.object_position` | script hook/global | `obj` | Internal helper for object position in the online/offline NPC economy module. |
| 2902 | `trade_path.vertex_accessible` | script hook/global | `npc, vid` | Internal helper for vertex accessible in the online/offline NPC economy module. |
| 2920 | `trade_path.direct_accessible_vertex` | script hook/global | `npc, pos` | Internal helper for direct accessible vertex in the online/offline NPC economy module. |
| 2931 | `trade_path.nearest_accessible_vertex` | script hook/global | `npc, pos` | Internal helper for nearest accessible vertex in the online/offline NPC economy module. |
| 2945 | `trade_path.accessible_vertex` | script hook/global | `npc, pos, fallback_pos` | Internal helper for accessible vertex in the online/offline NPC economy module. |
| 2969 | `trade_path.line_head_tail` | script hook/global | `line` | Internal helper for line head tail in the online/offline NPC economy module. |
| 2977 | `trade_path.head_tokens` | script hook/global | `head` | Internal helper for head tokens in the online/offline NPC economy module. |
| 2988 | `trade_path.drop_pos_tail` | script hook/global | `tail` | Internal helper for drop pos tail in the online/offline NPC economy module. |
| 2996 | `trade_path.rewrite_line` | script hook/global | `npc, line, fallback_pos` | Internal helper for rewrite line in the online/offline NPC economy module. |
| 3020 | `trade_path.prepare` | script hook/global | `npc, st, ini, fallback_pos` | Internal helper for prepare in the online/offline NPC economy module. |
| 3058 | `trade_path.acceptable_prepare_result` | script hook/global | `reason` | Internal helper for acceptable prepare result in the online/offline NPC economy module. |
| 3062 | `trade_path.prepare_active` | script hook/global | `npc, smart, st, trader` | Internal helper for prepare active in the online/offline NPC economy module. |
| 3090 | `M.clear_prepared_trade_job` | module export | `smart, npc_id, reason` | Clears prepared trade job from module or squad state. |
| 3129 | `M.release_online_trade_npc_to_smart` | module export | `npc, smart, reason` | Releases online trade npc to smart and removes ownership/reservation state. |
| 3162 | `recover_stale_prepared_trade` | local helper | `squad, now` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3203 | `squad_current_trade_smart` | local helper | `squad` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3207 | `server_object_alive` | local helper | `obj` | Internal helper for server object alive in the online/offline NPC economy module. |
| 3220 | `find_live_trader_at_smart` | local helper | `smart, ignore_ids` | Finds live trader at smart in indexed, runtime, or engine data. |
| 3229 | `check_id` | local helper | `npc_id, job` | Internal helper for check id in the online/offline NPC economy module. |
| 3270 | `can_try_auto_trade_now` | local helper | `squad, now` | Determines whether try auto trade now is allowed in the online/offline NPC economy context. |
| 3277 | `smart_for_squad_trade` | local helper | `squad` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3286 | `M.squad_has_trade_smart` | module export | `squad` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3294 | `M.squad_has_trade_work` | module export | `squad` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3316 | `M._trade_route_current_level` | module export | `squad, board` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3328 | `M._trade_route_levels` | module export | `current_level, opts` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3341 | `M._trade_route_smart_allowed` | module export | `squad, smart, level_name` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3364 | `M.pick_trade_route_smart` | module export | `squad, opts` | Selects trade route smart from validated candidates. |
| 3403 | `M.trade_route_task_weight` | module export | `squad, base_weight, opts` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3420 | `mark_trade_lookup_failure` | local helper | `squad, result, reason, smart` | Marks trade lookup failure for later processing or diagnostics. |
| 3425 | `resolve_auto_trade_context` | local helper | `squad, reason, now` | Resolves auto trade context into a usable runtime object or value. |
| 3458 | `resolve_auto_trade_pair` | local helper | `squad, reason` | Resolves auto trade pair into a usable runtime object or value. |
| 3478 | `M.resolve_auto_trade_pair` | module export | `squad, reason` | Resolves auto trade pair into a usable runtime object or value. |
| 3483 | `prepare_npc_vanilla_trade` | local helper | `npc, squad, smart, trader, reason, opts` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3527 | `unlink_npc_smart_job` | local helper | `smart, npc_id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 3540 | `setup_assigned_trade_job` | local helper | `npc, smart, info, job, slot_section, trader` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3593 | `force_trade_job_reselect` | local helper | `npc, smart, trader` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3636 | `prepare_squad_vanilla_trade` | local helper | `squad, members, trader, smart, reason, opts` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3684 | `execute_offline_auto_trade` | local helper | `squad, smart, reason, now` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3734 | `try_auto_trade_resolved` | local helper | `squad, reason, opts, now` | Attempts auto trade resolved and returns a controlled result instead of hard-failing. |
| 3752 | `alive_online_pair` | local helper | `npc, trader` | Internal helper for alive online pair in the online/offline NPC economy module. |
| 3771 | `resolve_explicit_pair` | local helper | `npc, trader` | Resolves explicit pair into a usable runtime object or value. |
| 3778 | `M.can_auto_trade_now` | module export | `squad` | Determines whether auto trade now is allowed in the online/offline NPC economy context. |
| 3782 | `M.debug_resolve_auto_trade_pair` | module export | `squad, reason` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3787 | `M.try_auto_trade_npc` | module export | `npc, trader, reason, opts` | Attempts auto trade npc and returns a controlled result instead of hard-failing. |
| 3807 | `M.try_auto_trade` | module export | `squad, reason, opts` | Attempts auto trade and returns a controlled result instead of hard-failing. |
| 3836 | `refresh_trade_items_from_inventory` | local helper | `npc, params, force` | Refreshes trade items from inventory from current runtime or indexed data. |
| 3892 | `M.refresh_online_trade_inventory` | module export | `npc, params, force` | Refreshes online trade inventory from current runtime or indexed data. |
| 3896 | `M.npc_has_items_to_sell` | module export | `actor, npc, params` | Internal helper for npc has items to sell in the online/offline NPC economy module. |
| 3926 | `execute_online_squad_trade` | local helper | `source_npc, trader, params, squad_id, smart_id, member_ids` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3981 | `suppress_online_squad_trade_members` | local helper | `squad, smart, until_tg` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3988 | `squad_id_for_trade_signal` | local helper | `npc, st` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 3999 | `squad_accepts_recovered_trade_signal` | local helper | `squad` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 4003 | `resolve_trade_signal_context` | local helper | `npc, params, st` | Resolves trade signal context into a usable runtime object or value. |
| 4034 | `resolve_trade_signal_trader` | local helper | `npc, params, st, ctx` | Resolves trade signal trader into a usable runtime object or value. |
| 4046 | `trade_job_customer_from_params` | local helper | `params` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 4053 | `trade_context_already_completed` | local helper | `st` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 4057 | `complete_trade_context` | local helper | `npc, params, st, ctx, trader, reason` | Completes trade context and applies the related consequence/fallback. |
| 4112 | `M.trade_job_give_id` | module export | `actor, npc, params` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 4147 | `M.trade_job_sell_items` | module export | `actor, npc, params` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 4203 | `M.patch_trade_condition` | module export | `` | Installs or maintains the chain-friendly patch for trade condition. |
| 4217 | `M.patch_trade_effect` | module export | `` | Installs or maintains the chain-friendly patch for trade effect. |
| 4239 | `M.watch_recent_trade_release` | module export | `` | Handles trade routing, trade state, or trade diagnostics in the online/offline NPC economy module. |
| 4286 | `M.actor_on_update` | module export | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 4290 | `npc_on_net_spawn` | local helper | `npc, se_obj` | Internal helper for npc on net spawn in the online/offline NPC economy module. |
| 4294 | `on_game_load` | local helper | `` | Game-load callback; schedules reconciliation or clears stale runtime-only state after loading a save. |
| 4300 | `M.convert_online_squad_money_notes` | module export | `` | Handles squad lookup, state, membership, or task coordination. |
| 4313 | `actor_on_first_update` | local helper | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 4320 | `register_trade_callbacks` | local helper | `force` | Registers trade callbacks in the module indexes or callbacks. |
| 4343 | `M.ensure_runtime_ready` | module export | `force_callbacks` | Internal helper for ensure runtime ready in the online/offline NPC economy module. |
| 4350 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 4358 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_index.script`

Role: event-driven world buckets for squads, smarts, bases, traders, artifacts, virtual artifacts, and cargo.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 67 | `M.get_revision` | module export | `` | Returns revision for the current event-driven world buckets for squads state. |
| 71 | `reset_base_camping_target_smarts_cache` | local helper | `` | Resets base camping target smarts cache to its default safe state. |
| 77 | `mark_base_camping_registry_changed` | local helper | `` | Marks base camping registry changed for later processing or diagnostics. |
| 85 | `mark_artifact_registry_changed` | local helper | `` | Marks artifact registry changed for later processing or diagnostics. |
| 92 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 101 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 109 | `M.offline_artifacts_enabled` | module export | `` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 113 | `smart_blacklisted_for_squad` | local helper | `squad, smart, level_name` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 125 | `tasks_mod` | local helper | `` | Resolves the ZHOPA task module if it is loaded or can be required safely. |
| 135 | `service_fillers_mod` | local helper | `` | Internal helper for service fillers mod in the event-driven world buckets for squads module. |
| 148 | `obj_level` | local helper | `obj` | Resolves or validates level names, ids, or level buckets. |
| 166 | `current_level_name` | local helper | `` | Resolves or validates level names, ids, or level buckets. |
| 176 | `virtual_artifact_level_allowed` | local helper | `level_name` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 181 | `object_id` | local helper | `obj` | Extracts a stable numeric id from a server object, online object, id-like table, number, or string. |
| 195 | `object_section` | local helper | `obj` | Returns a safe section name for an object. |
| 214 | `online_object_by_id` | local helper | `id` | Returns an online game object by id through db.storage/level lookups. |
| 223 | `object_is_artifact` | local helper | `obj` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 231 | `zone_object` | local helper | `zone` | Internal helper for zone object in the event-driven world buckets for squads module. |
| 235 | `artifact_parent_zone` | local helper | `artifact_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 244 | `zone_key` | local helper | `zone` | Internal helper for zone key in the event-driven world buckets for squads module. |
| 259 | `object_position` | local helper | `obj` | Internal helper for object position in the event-driven world buckets for squads module. |
| 289 | `artifact_distance_to_sqr` | local helper | `a, b` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 301 | `artifact_is_valid` | local helper | `id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 323 | `section_exists` | local helper | `section` | Internal helper for section exists in the event-driven world buckets for squads module. |
| 327 | `section_is_artifact` | local helper | `section` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 335 | `artefact_settings` | local helper | `` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 348 | `name_list` | local helper | `value` | Internal helper for name list in the event-driven world buckets for squads module. |
| 362 | `num_list` | local helper | `value` | Internal helper for num list in the event-driven world buckets for squads module. |
| 376 | `artifact_sections_for_token` | local helper | `token` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 398 | `anomaly_cfg_from_spawn_ini` | local helper | `obj` | Internal helper for anomaly cfg from spawn ini in the event-driven world buckets for squads module. |
| 410 | `zone_level_bucket` | local helper | `level_name` | Resolves or validates level names, ids, or level buckets. |
| 422 | `remove_virtual_zone_from_level` | local helper | `zkey, level_name` | Resolves or validates level names, ids, or level buckets. |
| 432 | `virtual_storage_state` | local helper | `` | Reads, writes, or repairs runtime state. |
| 450 | `persist_virtual_artifact` | local helper | `artifact_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 468 | `remove_persisted_virtual_artifact` | local helper | `artifact_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 478 | `clear_artifact_reservation_owner` | local helper | `artifact_id, squad_id` | Clears artifact reservation owner from module or squad state. |
| 490 | `artifact_reservation_live` | local helper | `artifact_id, squad_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 518 | `artifact_reserved` | local helper | `artifact_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 524 | `artifact_reserved_for_other_squad` | local helper | `artifact_id, squad` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 536 | `smart_is_base` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 548 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 556 | `squad_commander_id` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 564 | `is_monster_squad` | local helper | `squad` | Checks whether monster squad in the event-driven world buckets for squads context. |
| 569 | `squad_zhopa2_manageable` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 579 | `squad_targets_smart_id` | local helper | `squad, smart_id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 592 | `squad_base_camping_at_smart` | local helper | `squad, smart_id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 598 | `object_community` | local helper | `obj` | Internal helper for object community in the event-driven world buckets for squads module. |
| 614 | `relation_faction` | local helper | `community` | Internal helper for relation faction in the event-driven world buckets for squads module. |
| 622 | `squad_relation_faction` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 633 | `add_count` | local helper | `counts, community, amount` | Internal helper for add count in the event-driven world buckets for squads module. |
| 640 | `each_level` | local helper | `levels, fn` | Resolves or validates level names, ids, or level buckets. |
| 666 | `limit_value` | local helper | `limit` | Internal helper for limit value in the event-driven world buckets for squads module. |
| 674 | `now_ms` | local helper | `` | Returns the current game or device time in milliseconds for throttling and cooldown checks. |
| 681 | `current_frame_key` | local helper | `` | Internal helper for current frame key in the event-driven world buckets for squads module. |
| 695 | `reset_frame_scratch` | script hook/global | `` | Resets frame scratch to its default safe state. |
| 700 | `levels_key` | local helper | `levels` | Resolves or validates level names, ids, or level buckets. |
| 710 | `current_frame_scratch` | local helper | `` | Internal helper for current frame scratch in the event-driven world buckets for squads module. |
| 719 | `frame_reader` | local helper | `kind, levels, limit, build_fn` | Internal helper for frame reader in the event-driven world buckets for squads module. |
| 732 | `simboard` | local helper | `` | Internal helper for simboard in the event-driven world buckets for squads module. |
| 736 | `available_by_id` | local helper | `` | Internal helper for available by id in the event-driven world buckets for squads module. |
| 741 | `vanilla_smart_entry` | local helper | `board, smart_id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 745 | `smart_available` | local helper | `board, smart, available` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 755 | `smart_kind_matches` | local helper | `smart, smart_kind` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 780 | `add_smart_from_bucket` | local helper | `out, seen, board, available, smart_id, smart, smart_kind, max_count` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 793 | `read_smart_bucket` | local helper | `levels, smart_kind, max_count` | Reads smart bucket from serialized state, config, or engine data. |
| 831 | `M.smarts_on_levels` | module export | `levels, limit, smart_kind` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 838 | `M.base_smarts_on_levels` | module export | `levels, limit` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 844 | `M.squads_on_levels` | module export | `levels, limit` | Handles squad lookup, state, membership, or task coordination. |
| 880 | `M.squad_level_names` | module export | `` | Handles squad lookup, state, membership, or task coordination. |
| 899 | `M.unregister_base_camping_target` | module export | `squad` | Unregisters base camping target and cleans stale references. |
| 924 | `M.register_base_camping_target` | module export | `squad, target_id` | Registers base camping target in the module indexes or callbacks. |
| 945 | `base_camping_target_has_live_squad` | local helper | `smart_id` | Handles squad lookup, state, membership, or task coordination. |
| 970 | `M.base_camping_target_smarts_on_levels` | module export | `levels` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1028 | `smart_artifact_bucket_empty` | local helper | `smart_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1039 | `recalc_smart_artefact_flag` | local helper | `smart_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1070 | `remove_artifact_from_zone_bucket` | local helper | `artifact_id, zone_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1082 | `remove_artifact_from_smart_bucket` | local helper | `artifact_id, smart_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1091 | `remove_artifact_from_other_smart_buckets` | local helper | `artifact_id, keep_smart_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1105 | `add_artifact_to_bucket` | local helper | `bucket_table, key, artifact_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1120 | `restore_persisted_virtual_artifacts` | local helper | `` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1189 | `nearest_artifact_smart` | local helper | `anchor, level_name` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1207 | `resolve_artifact_smart` | local helper | `artifact_id, artifact_obj, level_name, zone` | Resolves artifact smart into a usable runtime object or value. |
| 1224 | `virtual_artifact_id` | local helper | `zone_id, slot` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1230 | `virtual_artifact_zone_key` | local helper | `artifact_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1239 | `virtual_spawn_chance` | local helper | `` | Internal helper for virtual spawn chance in the event-driven world buckets for squads module. |
| 1257 | `read_virtual_zone_entry` | local helper | `zone, cfg_file, source` | Reads virtual zone entry from serialized state, config, or engine data. |
| 1309 | `choose_virtual_artifact_section` | local helper | `entry` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1327 | `register_virtual_artifact` | local helper | `entry, section` | Registers virtual artifact in the module indexes or callbacks. |
| 1365 | `try_spawn_virtual_artifacts` | local helper | `entry` | Attempts spawn virtual artifacts and returns a controlled result instead of hard-failing. |
| 1393 | `ensure_virtual_artifacts_for_levels` | local helper | `level_set` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1410 | `restore_virtual_artifact_for_squad` | local helper | `squad, artifact_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1456 | `M.register_anomaly_zone` | module export | `zone, cfg_file, source` | Registers anomaly zone in the module indexes or callbacks. |
| 1474 | `M.is_virtual_artifact` | module export | `artifact_id` | Checks whether virtual artifact in the event-driven world buckets for squads context. |
| 1482 | `M.virtual_artifact_data` | module export | `artifact_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1490 | `M.virtual_artifacts_for_zone` | module export | `zone, only_reserved` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1515 | `M.materialize_virtual_artifact` | module export | `virtual_id, real_id, zone, section` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1550 | `M.register_artifact` | module export | `artifact_id, zone, section` | Registers artifact in the module indexes or callbacks. |
| 1582 | `M.refresh_artifact_entity` | module export | `se_obj` | Refreshes artifact entity from current runtime or indexed data. |
| 1626 | `M.unregister_artifact` | module export | `artifact_id, reason` | Unregisters artifact and cleans stale references. |
| 1653 | `M.unregister_zone_artifacts` | module export | `zone, reason` | Unregisters zone artifacts and cleans stale references. |
| 1669 | `M.smart_artefact_available` | module export | `smart` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1675 | `M.reserve_artifact_for_squad` | module export | `squad, artifact_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1714 | `M.release_artifact_reservation` | module export | `squad_or_id, reason` | Releases artifact reservation and removes ownership/reservation state. |
| 1744 | `restore_virtual_artifact_reservations_from_squads` | local helper | `` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1770 | `repair_real_artifact_smart` | local helper | `artifact_id, level_set` | Repairs real artifact smart when runtime state becomes stale or inconsistent. |
| 1804 | `M.available_artifact_for_smart` | module export | `smart_or_id, squad, opts` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1842 | `M.artifact_candidate_smarts_on_levels` | module export | `levels, squad` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1932 | `M.add_artifact_cargo` | module export | `squad, section, value, artifact_id, reason` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1952 | `M.sync_artifact_cargo` | module export | `squad` | Synchronizes artifact cargo between memory, indexes, and runtime state. |
| 1971 | `M.consume_artifact_cargo` | module export | `squad, count, value, reason` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 1994 | `M.clear_artifact_cargo` | module export | `squad, reason` | Clears artifact cargo from module or squad state. |
| 2007 | `M.squad_has_artifact_cargo` | module export | `squad, artifact_id` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 2029 | `M.unregister_smart` | module export | `smart` | Unregisters smart and cleans stale references. |
| 2045 | `M.unregister_squad` | module export | `squad` | Unregisters squad and cleans stale references. |
| 2057 | `M.base_ownership` | module export | `smart` | Internal helper for base ownership in the event-driven world buckets for squads module. |
| 2061 | `M.update_base_ownership` | module export | `smart` | Updates base ownership during the module tick or callback flow. |
| 2148 | `distance_to_sqr` | local helper | `a, b` | Internal helper for distance to sqr in the event-driven world buckets for squads module. |
| 2158 | `current_base_pull_valid` | local helper | `smart` | Internal helper for current base pull valid in the event-driven world buckets for squads module. |
| 2176 | `M.try_empty_base_pull` | module export | `smart` | Attempts empty base pull and returns a controlled result instead of hard-failing. |
| 2252 | `M.on_smart_update` | module export | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 2263 | `server_entity_is_artifact` | local helper | `se_obj, type_name` | Handles artifact-related state in the event-driven world buckets for squads module. |
| 2274 | `server_entity_on_register` | local helper | `se_obj, type_name` | Server-entity register callback; indexes or reconciles newly registered ALife objects. |
| 2288 | `server_entity_on_unregister` | local helper | `se_obj, type_name` | Server-entity unregister callback; removes stale ids and releases runtime ownership for disappearing objects. |
| 2299 | `M.on_game_load` | module export | `` | Game-load callback; schedules reconciliation or clears stale runtime-only state after loading a save. |
| 2304 | `M.actor_on_first_update` | module export | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 2309 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 2327 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_loot.script`

Role: online/offline looting, targeted pickups, corpse loop prevention, and loot accounting.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 26 | `load_module` | local helper | `name` | Loads an optional Lua module through raw globals or guarded require. |
| 35 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 39 | `memory_mod` | local helper | `` | Resolves the ZHOPA memory module if it is loaded or can be required safely. |
| 43 | `index_mod` | local helper | `` | Resolves the ZHOPA index module if it is loaded or can be required safely. |
| 47 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 55 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 63 | `debug_print_enabled` | local helper | `` | Checks whether ZHOPA debug output is enabled for this module. |
| 67 | `now_ms` | local helper | `` | Returns the current game or device time in milliseconds for throttling and cooldown checks. |
| 71 | `runtime_ready` | local helper | `reason` | Checks the shared ZHOPA runtime readiness barrier before running context-dependent work. |
| 83 | `alife_sim` | local helper | `` | Internal helper for alife sim in the online/offline looting module. |
| 91 | `M.online_enabled` | module export | `` | Internal helper for online enabled in the online/offline looting module. |
| 95 | `M.offline_enabled` | module export | `` | Internal helper for offline enabled in the online/offline looting module. |
| 99 | `M.offline_real_enabled` | module export | `` | Internal helper for offline real enabled in the online/offline looting module. |
| 103 | `M.enabled` | module export | `` | Internal helper for enabled in the online/offline looting module. |
| 107 | `valid_id` | local helper | `id` | Checks validity of id for the current online/offline looting flow. |
| 112 | `object_id` | local helper | `obj` | Extracts a stable numeric id from a server object, online object, id-like table, number, or string. |
| 126 | `object_section` | local helper | `obj` | Returns a safe section name for an object. |
| 141 | `online_object_by_id` | local helper | `id` | Returns an online game object by id through db.storage/level lookups. |
| 150 | `object_name` | local helper | `obj` | Returns a safe display name for an object or id. |
| 157 | `object_level_name` | local helper | `obj` | Resolves or validates level names, ids, or level buckets. |
| 185 | `offline_loot_level_log` | local helper | `se_victim, se_looter, attacker_squad` | Handles loot selection, pickup, accounting, or diagnostics in the online/offline looting module. |
| 192 | `object_clsid` | local helper | `obj` | Internal helper for object clsid in the online/offline looting module. |
| 203 | `object_section_exists` | local helper | `section` | Internal helper for object section exists in the online/offline looting module. |
| 207 | `split_colon` | local helper | `text` | Internal helper for split colon in the online/offline looting module. |
| 216 | `table_contains` | local helper | `t, value` | Internal helper for table contains in the online/offline looting module. |
| 228 | `object_alive` | local helper | `obj` | Internal helper for object alive in the online/offline looting module. |
| 236 | `valid_squad_object` | local helper | `squad` | Checks validity of squad object for the current online/offline looting flow. |
| 244 | `item_cost` | local helper | `item` | Internal helper for item cost in the online/offline looting module. |
| 252 | `object_is_artifact` | local helper | `obj` | Handles artifact-related state in the online/offline looting module. |
| 257 | `mark_artifact_cargo_for_squad` | local helper | `squad, item, section, value, artifact_id, reason` | Marks artifact cargo for squad for later processing or diagnostics. |
| 281 | `ensure_death_ini` | local helper | `` | Internal helper for ensure death ini in the online/offline looting module. |
| 294 | `ensure_loadout_ini` | local helper | `` | Internal helper for ensure loadout ini in the online/offline looting module. |
| 305 | `ini_section_exists` | local helper | `ini, section` | Internal helper for ini section exists in the online/offline looting module. |
| 309 | `ini_read_string` | local helper | `ini, section, key` | Internal helper for ini read string in the online/offline looting module. |
| 317 | `ini_line_count` | local helper | `ini, section` | Internal helper for ini line count in the online/offline looting module. |
| 325 | `ini_line` | local helper | `ini, section, idx` | Internal helper for ini line in the online/offline looting module. |
| 336 | `load_death_item_counts` | local helper | `` | Loads death item counts for the online/offline looting module. |
| 356 | `death_section_items` | local helper | `section` | Internal helper for death section items in the online/offline looting module. |
| 373 | `loadout_slot_items` | local helper | `section` | Internal helper for loadout slot items in the online/offline looting module. |
| 397 | `is_monster_player_id` | local helper | `player_id` | Checks whether monster player id in the online/offline looting context. |
| 410 | `looter_squad` | local helper | `npc` | Handles loot selection, pickup, accounting, or diagnostics in the online/offline looting module. |
| 422 | `squad_by_id` | local helper | `squad_id` | Handles squad lookup, state, membership, or task coordination. |
| 437 | `managed_stalker_squad_for_looter` | local helper | `npc, require_loot_enabled` | Handles loot selection, pickup, accounting, or diagnostics in the online/offline looting module. |
| 477 | `M.should_manage_looter` | module export | `npc` | Decides whether manage looter should run for the current online/offline looting state. |
| 481 | `section_is_quest` | local helper | `section` | Internal helper for section is quest in the online/offline looting module. |
| 513 | `section_has_inventory_icon` | local helper | `section` | Scans, classifies, or mutates NPC/server inventory state. |
| 520 | `object_is_inventory_item` | local helper | `obj` | Scans, classifies, or mutates NPC/server inventory state. |
| 533 | `section_is_lootable_inventory` | local helper | `section, obj` | Handles loot selection, pickup, accounting, or diagnostics in the online/offline looting module. |
| 547 | `object_is_story` | local helper | `obj, id` | Handles story-gated state, tasks, or diagnostic output. |
| 552 | `cleanup_exclusive_item_reservations` | local helper | `` | Cleans up exclusive item reservations and removes stale runtime state. |
| 565 | `exclusive_item_owner` | local helper | `item_id` | Internal helper for exclusive item owner in the online/offline looting module. |
| 578 | `item_reserved_for_other` | local helper | `obj, looter` | Internal helper for item reserved for other in the online/offline looting module. |
| 594 | `M.can_take_section` | module export | `section, obj, looter` | Determines whether take section is allowed in the online/offline looting context. |
| 616 | `is_stalker_server_object` | local helper | `obj` | Checks whether stalker server object in the online/offline looting context. |
| 628 | `offline_squad_can_loot` | local helper | `squad` | Handles loot selection, pickup, accounting, or diagnostics in the online/offline looting module. |
| 641 | `member_server_object` | local helper | `member` | Handles squad member lookup, inventory ownership, or relation state. |
| 648 | `pick_offline_looter` | local helper | `squad, se_attacker` | Selects offline looter from validated candidates. |
| 670 | `collect_child_ids` | local helper | `se_owner` | Collects child ids from indexed or runtime data. |
| 684 | `owner_create_args` | local helper | `se_owner` | Internal helper for owner create args in the online/offline looting module. |
| 691 | `set_item_condition_from_source` | local helper | `se_src, se_dst` | Sets item condition from source for the current online/offline looting state. |
| 706 | `create_section_to_looter` | local helper | `section, se_looter, props` | Creates section to looter for the module flow. |
| 733 | `clone_ammo_to_looter` | local helper | `section, se_item, se_looter` | Copies ammo to looter into a safe plain value. |
| 763 | `clone_weapon_to_looter` | local helper | `section, se_item, se_looter` | Copies weapon to looter into a safe plain value. |
| 767 | `clone_item_to_looter` | local helper | `section, se_item, se_looter` | Copies item to looter into a safe plain value. |
| 785 | `created_item_valid` | local helper | `se_new, se_looter` | Internal helper for created item valid in the online/offline looting module. |
| 797 | `created_item_transfer_log_entry` | local helper | `section, se_new, value, tag` | Internal helper for created item transfer log entry in the online/offline looting module. |
| 814 | `offline_loot_item_log_entry` | local helper | `section, se_item, value` | Handles loot selection, pickup, accounting, or diagnostics in the online/offline looting module. |
| 833 | `offline_loot_item_transfer_log_entry` | local helper | `section, se_item, se_new, value` | Handles loot selection, pickup, accounting, or diagnostics in the online/offline looting module. |
| 842 | `section_class` | local helper | `section` | Internal helper for section class in the online/offline looting module. |
| 850 | `section_is_weapon` | local helper | `section, obj` | Classifies or protects weapon inventory state. |
| 864 | `section_is_ammo` | local helper | `section` | Classifies, counts, sells, or buys ammunition for NPC supply logic. |
| 868 | `npc_squad` | local helper | `se_npc` | Handles squad lookup, state, membership, or task coordination. |
| 876 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 887 | `split_artifact_sections` | local helper | `sections` | Handles artifact-related state in the online/offline looting module. |
| 895 | `consume_artifact_cargo_from_squad` | local helper | `squad, count, value, reason` | Handles artifact-related state in the online/offline looting module. |
| 921 | `transfer_remaining_artifact_cargo` | local helper | `attacker_squad, victim_squad, reason` | Handles artifact-related state in the online/offline looting module. |
| 945 | `death_community` | local helper | `se_npc` | Internal helper for death community in the online/offline looting module. |
| 960 | `death_rank` | local helper | `se_npc` | Internal helper for death rank in the online/offline looting module. |
| 979 | `pick_existing_section` | local helper | `ini, preferred, fallback` | Selects existing section from validated candidates. |
| 989 | `create_generated_loot` | local helper | `section, se_looter, moved_items, tag` | Creates generated loot for the module flow. |
| 1002 | `spawn_death_section` | local helper | `section, se_looter, moved_items` | Spawns death section through guarded server-side creation logic. |
| 1027 | `spawn_death_table_loot` | local helper | `se_victim, se_looter, moved_items` | Spawns death table loot through guarded server-side creation logic. |
| 1057 | `pick_loadout_entry` | local helper | `slot_section` | Selects loadout entry from validated candidates. |
| 1070 | `victim_loadout_section` | local helper | `se_victim, comm, rank` | Internal helper for victim loadout section in the online/offline looting module. |
| 1090 | `spawn_loadout_fallback_loot` | local helper | `se_victim, se_looter, moved_items` | Spawns loadout fallback loot through guarded server-side creation logic. |
| 1122 | `offline_loot_clone_valid` | local helper | `se_new, se_looter` | Handles loot selection, pickup, accounting, or diagnostics in the online/offline looting module. |
| 1137 | `offline_loot_items_log` | local helper | `items` | Handles loot selection, pickup, accounting, or diagnostics in the online/offline looting module. |
| 1153 | `M.offline_loot_victim` | module export | `attacker_squad, se_attacker, se_victim, reason` | Handles loot selection, pickup, accounting, or diagnostics in the online/offline looting module. |
| 1266 | `object_is_online_inventory_owner` | local helper | `obj` | Scans, classifies, or mutates NPC/server inventory state. |
| 1283 | `corpse_has_quest_item` | local helper | `corpse` | Handles corpse target filtering, looting, or loop prevention. |
| 1288 | `inspect` | local helper | `owner, item` | Internal helper for inspect in the online/offline looting module. |
| 1300 | `M.is_protected_corpse` | module export | `corpse, corpse_id` | Checks whether protected corpse in the online/offline looting context. |
| 1310 | `store_for` | local helper | `kind` | Internal helper for store for in the online/offline looting module. |
| 1314 | `compact_store` | local helper | `store` | Internal helper for compact store in the online/offline looting module. |
| 1331 | `cleanup_store` | local helper | `kind` | Cleans up store and removes stale runtime state. |
| 1350 | `trim_total_cap` | local helper | `` | Internal helper for trim total cap in the online/offline looting module. |
| 1352 | `count` | local helper | `` | Internal helper for count in the online/offline looting module. |
| 1374 | `add_event` | local helper | `kind, id` | Internal helper for add event in the online/offline looting module. |
| 1398 | `remove_event` | local helper | `kind, id` | Internal helper for remove event in the online/offline looting module. |
| 1407 | `recent_ids` | local helper | `kind` | Internal helper for recent ids in the online/offline looting module. |
| 1423 | `M.mark_corpse_ignored` | module export | `id` | Marks corpse ignored for later processing or diagnostics. |
| 1446 | `M.corpse_ignored` | module export | `id` | Handles corpse target filtering, looting, or loop prevention. |
| 1456 | `M.recent_corpse_ids` | module export | `` | Handles corpse target filtering, looting, or loop prevention. |
| 1460 | `M.consume_corpse_event_id` | module export | `id` | Handles corpse target filtering, looting, or loop prevention. |
| 1464 | `M.forget_corpse_id` | module export | `id` | Handles corpse target filtering, looting, or loop prevention. |
| 1469 | `M.recent_item_ids` | module export | `` | Internal helper for recent item ids in the online/offline looting module. |
| 1473 | `M.is_recent_item_id` | module export | `id` | Checks whether recent item id in the online/offline looting context. |
| 1479 | `cleanup_targeted_item_requests` | local helper | `` | Cleans up targeted item requests and removes stale runtime state. |
| 1495 | `forget_targeted_item_request` | local helper | `item_id` | Resolves, validates, or formats a task target. |
| 1506 | `targeted_gather_prepare` | local helper | `` | Resolves, validates, or formats a task target. |
| 1516 | `targeted_gather_clear` | local helper | `` | Resolves, validates, or formats a task target. |
| 1526 | `M.reserve_item_for_npc` | module export | `npc, item_id, reason` | Internal helper for reserve item for npc in the online/offline looting module. |
| 1554 | `M.release_item_reservation` | module export | `item_id, npc_or_id` | Releases item reservation and removes ownership/reservation state. |
| 1572 | `M.item_reserved_for_other` | module export | `npc, item_id` | Internal helper for item reserved for other in the online/offline looting module. |
| 1581 | `M.request_item_pickup` | module export | `npc, item_id, reason` | Internal helper for request item pickup in the online/offline looting module. |
| 1631 | `M.targeted_item_ids_for_npc` | module export | `npc` | Resolves, validates, or formats a task target. |
| 1647 | `M.cancel_item_pickup` | module export | `npc_or_id, item_id` | Cancels item pickup and clears or releases related state. |
| 1669 | `targeted_request_for_item` | local helper | `item, keep_parented` | Resolves, validates, or formats a task target. |
| 1680 | `cleanup_vanilla_artifact_pickups` | local helper | `` | Cleans up vanilla artifact pickups and removes stale runtime state. |
| 1692 | `inventory_section_count` | local helper | `owner, section` | Scans, classifies, or mutates NPC/server inventory state. |
| 1698 | `inspect` | local helper | `_, item` | Internal helper for inspect in the online/offline looting module. |
| 1713 | `inventory_item_by_section` | local helper | `owner, section, excluded_id` | Scans, classifies, or mutates NPC/server inventory state. |
| 1720 | `inspect` | local helper | `_, item` | Internal helper for inspect in the online/offline looting module. |
| 1737 | `add_online_member` | local helper | `out, seen, id` | Handles squad member lookup, inventory ownership, or relation state. |
| 1754 | `squad_online_member_objects` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 1772 | `artifact_pickup_recovery_context` | local helper | `squad` | Handles artifact-related state in the online/offline looting module. |
| 1785 | `M.note_vanilla_artifact_pickup` | module export | `npc, artifact_id, section` | Handles artifact-related state in the online/offline looting module. |
| 1821 | `record_targeted_artifact_pickup` | local helper | `npc, item, request, reason` | Handles artifact-related state in the online/offline looting module. |
| 1839 | `record_task_artifact_pickup_by_section` | local helper | `npc, item, request, reason` | Handles artifact-related state in the online/offline looting module. |
| 1869 | `record_task_artifact_pickup` | local helper | `npc, item, reason` | Handles artifact-related state in the online/offline looting module. |
| 1893 | `recover_task_artifact_from_squad_inventory` | local helper | `squad, artifact_id, reason` | Handles artifact-related state in the online/offline looting module. |
| 1926 | `M.recover_pending_vanilla_artifact_pickup` | module export | `squad, artifact_id` | Handles artifact-related state in the online/offline looting module. |
| 1950 | `M.corpse_detect_dist_sqr` | module export | `` | Handles corpse target filtering, looting, or loop prevention. |
| 1955 | `M.item_detect_dist_sqr` | module export | `` | Internal helper for item detect dist sqr in the online/offline looting module. |
| 1960 | `M.record_loot` | module export | `npc, source, item, value, reason` | Handles loot selection, pickup, accounting, or diagnostics in the online/offline looting module. |
| 1992 | `M.record_offline_combat_loot` | module export | `squad, target, killed_count, reason` | Handles loot selection, pickup, accounting, or diagnostics in the online/offline looting module. |
| 2019 | `on_npc_death` | local helper | `npc, who` | Internal helper for on npc death in the online/offline looting module. |
| 2028 | `on_monster_death` | local helper | `obj, who` | Internal helper for on monster death in the online/offline looting module. |
| 2037 | `on_npc_item_drop` | local helper | `npc, item` | Internal helper for on npc item drop in the online/offline looting module. |
| 2046 | `on_actor_item_drop` | local helper | `item` | Internal helper for on actor item drop in the online/offline looting module. |
| 2055 | `on_item_take` | local helper | `npc, item` | Internal helper for on item take in the online/offline looting module. |
| 2073 | `on_actor_item_take` | local helper | `item` | Internal helper for on actor item take in the online/offline looting module. |
| 2082 | `M.on_game_load` | module export | `` | Game-load callback; schedules reconciliation or clears stale runtime-only state after loading a save. |
| 2092 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 2114 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_mcm.script`

Role: MCM integration wrapper and option-tree registration.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 1 | `ensure_schema` | local helper | `` | Internal helper for ensure schema in the MCM integration wrapper and option-tree registration module. |
| 14 | `clone_option` | local helper | `meta, key` | Copies option into a safe plain value. |
| 23 | `make_group` | local helper | `schema, group` | Builds group for the current MCM integration wrapper and option-tree registration flow. |
| 39 | `make_panel` | local helper | `schema, panel` | Builds panel for the current MCM integration wrapper and option-tree registration flow. |
| 59 | `on_mcm_load` | script hook/global | `` | Builds or reads MCM configuration data. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_mcm_schema.script`

Role: MCM option schema, paths, defaults, and panel layout.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 101 | `get_path` | script hook/global | `key` | Returns path for the current MCM option schema state. |
| 105 | `get_option` | script hook/global | `key` | Returns option for the current MCM option schema state. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_memory.script`

Role: serializable per-squad memory, recent targets, cargo summaries, and task snapshots.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 11 | `write_string` | local helper | `packet, value` | Writes string into serialized state or module data. |
| 15 | `read_string` | local helper | `packet` | Reads string from serialized state, config, or engine data. |
| 23 | `index_mod` | local helper | `` | Resolves the ZHOPA index module if it is loaded or can be required safely. |
| 32 | `M.reset_squad` | module export | `squad` | Resets squad to its default safe state. |
| 68 | `pack_recent` | local helper | `values` | Internal helper for pack recent in the serializable per-squad memory module. |
| 84 | `unpack_recent` | local helper | `value` | Internal helper for unpack recent in the serializable per-squad memory module. |
| 99 | `M.add_recent_smart` | module export | `squad, smart_id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 108 | `M.recent_has_smart` | module export | `squad, smart_id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 122 | `M.add_recent_target` | module export | `squad, target_id` | Resolves, validates, or formats a task target. |
| 131 | `M.recent_has_target` | module export | `squad, target_id` | Resolves, validates, or formats a task target. |
| 145 | `M.add_loot_value` | module export | `squad, value, reason` | Handles loot selection, pickup, accounting, or diagnostics in the serializable per-squad memory module. |
| 156 | `M.add_artifact_cargo` | module export | `squad, section, value, artifact_id, reason` | Handles artifact-related state in the serializable per-squad memory module. |
| 177 | `M.snapshot_task` | module export | `squad, reason` | Internal helper for snapshot task in the serializable per-squad memory module. |
| 193 | `M.clear_resume` | module export | `squad` | Clears resume from module or squad state. |
| 205 | `M.resume_task` | module export | `squad, reason` | Internal helper for resume task in the serializable per-squad memory module. |
| 232 | `M.write_squad` | module export | `packet, squad` | Writes squad into serialized state or module data. |
| 267 | `M.read_squad` | module export | `packet, squad` | Reads squad from serialized state, config, or engine data. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_perception.script`

Role: shared perception, relation checks, smart/target validation, scoring, and route selection.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 40 | `squad_section_name` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 58 | `section_faction` | local helper | `section` | Internal helper for section faction in the shared perception module. |
| 66 | `M.squad_player_id` | module export | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 77 | `M.squad_relation_faction` | module export | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 86 | `cfg` | local helper | `` | Internal helper for cfg in the shared perception module. |
| 96 | `now_ms` | local helper | `` | Returns the current game or device time in milliseconds for throttling and cooldown checks. |
| 103 | `current_frame_key` | local helper | `` | Internal helper for current frame key in the shared perception module. |
| 117 | `current_frame_cache` | local helper | `` | Internal helper for current frame cache in the shared perception module. |
| 126 | `cached_frame_value` | local helper | `key, build_fn` | Internal helper for cached frame value in the shared perception module. |
| 140 | `cached_frame_pair` | local helper | `key, build_fn` | Internal helper for cached frame pair in the shared perception module. |
| 151 | `obj_cache_key` | local helper | `obj` | Internal helper for obj cache key in the shared perception module. |
| 159 | `memory_mod` | local helper | `` | Resolves the ZHOPA memory module if it is loaded or can be required safely. |
| 168 | `index_mod` | local helper | `` | Resolves the ZHOPA index module if it is loaded or can be required safely. |
| 177 | `M.is_monster_squad` | module export | `squad` | Checks whether monster squad in the shared perception context. |
| 182 | `plain_sim_stalker_squad` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 193 | `M.game_time` | module export | `` | Internal helper for game time in the shared perception module. |
| 197 | `M.elapsed` | module export | `start_time` | Internal helper for elapsed in the shared perception module. |
| 205 | `M.obj_level` | module export | `obj` | Resolves or validates level names, ids, or level buckets. |
| 225 | `M.obj_same_level` | module export | `a, b` | Resolves or validates level names, ids, or level buckets. |
| 230 | `add_level` | local helper | `set, list, level_name` | Resolves or validates level names, ids, or level buckets. |
| 242 | `target_maps` | local helper | `level_name` | Resolves, validates, or formats a task target. |
| 260 | `target_maps_has` | local helper | `level_name, target_level` | Resolves, validates, or formats a task target. |
| 270 | `topology_neighbors` | local helper | `level_name` | Handles level-neighbor topology data. |
| 281 | `topology_revision` | local helper | `` | Handles level-neighbor topology data. |
| 292 | `add_neighbor_sources` | local helper | `level_name, add_fn` | Internal helper for add neighbor sources in the shared perception module. |
| 304 | `scan_reverse_edges` | local helper | `target_level, add_fn` | Internal helper for scan reverse edges in the shared perception module. |
| 321 | `M.nearby_levels` | module export | `level_name` | Resolves or validates level names, ids, or level buckets. |
| 341 | `add_direct` | local helper | `other_level` | Internal helper for add direct in the shared perception module. |
| 347 | `add_nearby` | local helper | `other_level` | Internal helper for add nearby in the shared perception module. |
| 369 | `smart_population` | local helper | `smart_id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 385 | `has_prey_squad` | local helper | `squad, smart` | Checks whether prey squad is present in the shared perception context. |
| 402 | `smart_is_base` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 420 | `base_smarts_on_level` | local helper | `level_name` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 438 | `distance_to_sqr` | local helper | `a, b` | Internal helper for distance to sqr in the shared perception module. |
| 455 | `target_near_base_smart` | local helper | `target, target_level` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 480 | `smart_kind_ok` | local helper | `squad, smart, kind` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 510 | `vanilla_nearby` | local helper | `squad, smart` | Internal helper for vanilla nearby in the shared perception module. |
| 519 | `level_mode_ok` | local helper | `mode, current_level, target_level, neighbors, squad, smart` | Resolves or validates level names, ids, or level buckets. |
| 542 | `M.level_names_for_mode` | module export | `current_level, mode, neighbors` | Resolves or validates level names, ids, or level buckets. |
| 545 | `add` | local helper | `level_name` | Internal helper for add in the shared perception module. |
| 586 | `index_squads_on_levels` | local helper | `levels` | Handles squad lookup, state, membership, or task coordination. |
| 594 | `index_smarts_on_levels` | local helper | `levels, smart_kind` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 602 | `base_smarts_on_levels` | assigned wrapper | `levels` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 610 | `levels_for_options` | local helper | `options` | Resolves or validates level names, ids, or level buckets. |
| 617 | `list_key` | local helper | `list` | Internal helper for list key in the shared perception module. |
| 629 | `bool_key` | local helper | `value` | Internal helper for bool key in the shared perception module. |
| 633 | `smart_options_signature` | local helper | `squad, options, levels` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 654 | `hunt_options_signature` | local helper | `squad, options, levels` | Handles hunt target validation, combat consequences, or pursuit state. |
| 668 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 676 | `squad_member_registered_at_smart` | local helper | `smart, squad` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 692 | `squad_member_id_set` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 707 | `squad_commander_id` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 715 | `is_online_offline_group` | local helper | `squad` | Checks whether online offline group in the shared perception context. |
| 723 | `is_zhopa2_managed_scripted_target` | local helper | `squad` | Checks whether managed scripted target in the shared perception context. |
| 731 | `is_common_sim_squad` | local helper | `target` | Checks whether common sim squad in the shared perception context. |
| 744 | `is_blacklisted_for_hunt` | local helper | `squad, level_name, smart` | Checks whether blacklisted for hunt in the shared perception context. |
| 758 | `safe_zone_squad` | local helper | `squad` | Safely resolves zone squad with nil and pcall guards. |
| 762 | `squad_targets_smart` | local helper | `other, smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 775 | `squad_target_smart_id` | local helper | `other` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 785 | `squad_near_smart` | local helper | `other, smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 803 | `factions_hostile` | local helper | `faction, target_faction` | Internal helper for factions hostile in the shared perception module. |
| 832 | `M.squad_relation_hostile` | module export | `squad, target` | Handles squad lookup, state, membership, or task coordination. |
| 836 | `faction_relation_rank` | local helper | `faction, owner` | Internal helper for faction relation rank in the shared perception module. |
| 864 | `hostile_squad_at_smart` | local helper | `squad, other, smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 873 | `smart_has_hostile_squad` | local helper | `squad, smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 905 | `base_camping_squad_at_smart` | local helper | `squad, other, smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 915 | `base_camping_target_candidates_on_levels` | local helper | `levels, current_level` | Resolves or validates level names, ids, or level buckets. |
| 953 | `base_camping_populate_level_rank` | local helper | `squad, smart, options` | Resolves or validates level names, ids, or level buckets. |
| 969 | `base_camping_populate_candidates` | local helper | `squad, opts` | Internal helper for base camping populate candidates in the shared perception module. |
| 1021 | `base_camping_target_map` | local helper | `squad, candidates` | Resolves, validates, or formats a task target. |
| 1074 | `smart_owner_relation_rank` | local helper | `squad, smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1092 | `nonexclusive_job_capacity` | local helper | `jobs` | Internal helper for nonexclusive job capacity in the shared perception module. |
| 1105 | `smart_stalker_job_capacity` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1116 | `occupied_stalker_jobs` | local helper | `smart, ignore_squad` | Internal helper for occupied stalker jobs in the shared perception module. |
| 1121 | `ignored` | local helper | `npc_id` | Internal helper for ignored in the shared perception module. |
| 1153 | `targeted_stalker_squads_on_levels` | assigned wrapper | `levels` | Handles squad lookup, state, membership, or task coordination. |
| 1171 | `smart_incoming_stalker_npc_load` | local helper | `squad, smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1178 | `add_other` | local helper | `other` | Internal helper for add other in the shared perception module. |
| 1221 | `M.smart_stalker_free_job_slots` | module export | `squad, smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1236 | `base_camping_populate_score` | local helper | `squad, smart` | Internal helper for base camping populate score in the shared perception module. |
| 1254 | `count_rest_load_squad` | local helper | `squad, other, seen` | Handles squad lookup, state, membership, or task coordination. |
| 1274 | `M.smart_rest_load` | module export | `squad, smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1306 | `smart_owner_hostile_or_unstable` | local helper | `squad, smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1329 | `safe_rest_smart` | local helper | `squad, smart` | Safely resolves rest smart with nil and pcall guards. |
| 1339 | `hunt_prey_ok` | local helper | `squad, target, prey` | Handles hunt target validation, combat consequences, or pursuit state. |
| 1348 | `M.valid_hunt_target` | module export | `squad, target, opts` | Checks validity of hunt target for the current shared perception flow. |
| 1403 | `M.valid_revenge_target` | module export | `squad, target, opts` | Checks validity of revenge target for the current shared perception flow. |
| 1444 | `M.index_squads_for_options` | module export | `options, levels` | Handles squad lookup, state, membership, or task coordination. |
| 1450 | `M.collect_hunt_targets` | module export | `squad, opts` | Collects hunt targets from indexed or runtime data. |
| 1468 | `squad_distance_uncached` | local helper | `squad, target` | Handles squad lookup, state, membership, or task coordination. |
| 1490 | `squad_distance` | local helper | `squad, target` | Handles squad lookup, state, membership, or task coordination. |
| 1499 | `route_smart_ok` | local helper | `squad, smart, target_level` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1520 | `smart_from_target_id` | local helper | `target_id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1531 | `target_route_smart` | local helper | `squad, target, target_level` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1556 | `actor_server_object` | local helper | `` | Internal helper for actor server object in the shared perception module. |
| 1565 | `M.actor_script_target` | module export | `squad, opts` | Resolves, validates, or formats a task target. |
| 1588 | `M.hunt_script_target` | module export | `squad, target, opts` | Handles hunt target validation, combat consequences, or pursuit state. |
| 1614 | `M.revenge_script_target` | module export | `squad, target, opts` | Handles revenge targeting, hostility, or cleanup in the shared perception module. |
| 1636 | `pick_hunt_target_once` | local helper | `squad, options` | Selects hunt target once from validated candidates. |
| 1667 | `M.pick_hunt_target` | module export | `squad, opts` | Selects hunt target from validated candidates. |
| 1685 | `M.valid_smart` | module export | `squad, smart, opts` | Checks validity of smart for the current shared perception flow. |
| 1733 | `M.safe_rest_target_valid` | module export | `squad, target_id` | Safely resolves rest target valid with nil and pcall guards. |
| 1747 | `M.index_smarts_for_options` | module export | `options, levels` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1753 | `valid_smart_cached` | local helper | `squad, smart, options, signature` | Checks validity of smart cached for the current shared perception flow. |
| 1763 | `M.collect_smarts` | module export | `squad, opts` | Collects smarts from indexed or runtime data. |
| 1789 | `pick_smart_from_options` | local helper | `squad, opts` | Selects smart from options from validated candidates. |
| 1811 | `M.pick_smart` | module export | `squad, opts` | Selects smart from validated candidates. |
| 1815 | `M.pick_artifact_target` | module export | `squad, opts` | Selects artifact target from validated candidates. |
| 1821 | `artefact_clone_opts` | local helper | `src` | Handles artifact-related state in the shared perception module. |
| 1867 | `M.pick_closest_smart` | module export | `squad, opts` | Selects closest smart from validated candidates. |
| 1882 | `M.pick_balanced_rest_smart` | module export | `squad, opts` | Selects balanced rest smart from validated candidates. |
| 1903 | `M.pick_base_camping_populate_smart` | module export | `squad, opts` | Selects base camping populate smart from validated candidates. |
| 1934 | `M.base_camping_populate_target_valid` | module export | `squad, smart` | Resolves, validates, or formats a task target. |
| 1953 | `M.pick_final_prior_smart` | module export | `squad, smart_or_list, opts` | Selects final prior smart from validated candidates. |
| 1980 | `clone_opts` | local helper | `src` | Copies opts into a safe plain value. |
| 1988 | `M.pick_weighted_smart` | module export | `squad, opts, fallback_opts` | Selects weighted smart from validated candidates. |
| 2009 | `M.pack_ids` | module export | `list` | Internal helper for pack ids in the shared perception module. |
| 2017 | `M.unpack_ids` | module export | `value` | Internal helper for unpack ids in the shared perception module. |
| 2033 | `M.is_night` | module export | `` | Checks whether night in the shared perception context. |
| 2038 | `M.make_patrol` | module export | `squad, kind, opts` | Builds patrol for the current shared perception flow. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_revenge.script`

Role: revenge event detection, offender tracking, assignment, cooldowns, and callbacks.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 8 | `load_module` | local helper | `name` | Loads an optional Lua module through raw globals or guarded require. |
| 17 | `perception_mod` | local helper | `` | Resolves the ZHOPA perception module if it is loaded or can be required safely. |
| 21 | `index_mod` | local helper | `` | Resolves the ZHOPA index module if it is loaded or can be required safely. |
| 25 | `tasks_mod` | local helper | `` | Resolves the ZHOPA task module if it is loaded or can be required safely. |
| 29 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 33 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 41 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 49 | `hour_is_night` | local helper | `hour` | Internal helper for hour is night in the revenge event detection module. |
| 54 | `current_hour` | local helper | `` | Internal helper for current hour in the revenge event detection module. |
| 58 | `runtime_ready` | local helper | `reason` | Checks the shared ZHOPA runtime readiness barrier before running context-dependent work. |
| 70 | `is_night_now` | local helper | `` | Checks whether night now in the revenge event detection context. |
| 78 | `revenge_disabled_for_night` | local helper | `` | Handles revenge targeting, hostility, or cleanup in the revenge event detection module. |
| 82 | `sleep_touches_night` | local helper | `hours, start_hour` | Internal helper for sleep touches night in the revenge event detection module. |
| 103 | `object_id` | local helper | `obj` | Extracts a stable numeric id from a server object, online object, id-like table, number, or string. |
| 133 | `death_key` | local helper | `victim_squad, offender_target_id` | Internal helper for death key in the revenge event detection module. |
| 140 | `mark_death_processed` | local helper | `victim_squad, offender_target_id` | Marks death processed for later processing or diagnostics. |
| 159 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 167 | `squad_commander_id` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 175 | `obj_level` | local helper | `obj` | Resolves or validates level names, ids, or level buckets. |
| 200 | `position_distance` | local helper | `a, b` | Internal helper for position distance in the revenge event detection module. |
| 220 | `graph_distance` | local helper | `a, b` | Internal helper for graph distance in the revenge event detection module. |
| 230 | `squad_distance` | local helper | `victim_squad, responder` | Handles squad lookup, state, membership, or task coordination. |
| 234 | `actor_killer` | local helper | `se_killer` | Internal helper for actor killer in the revenge event detection module. |
| 242 | `squad_from_member` | local helper | `se_obj` | Handles squad lookup, state, membership, or task coordination. |
| 270 | `killer_squad_and_target` | local helper | `se_killer` | Handles squad lookup, state, membership, or task coordination. |
| 278 | `responder_ok` | local helper | `candidate, victim_squad, offender_squad` | Internal helper for responder ok in the revenge event detection module. |
| 303 | `level_pool` | local helper | `victim_squad` | Resolves or validates level names, ids, or level buckets. |
| 318 | `consider_candidate` | local helper | `victim_squad, offender_squad, candidate, best, best_dist` | Internal helper for consider candidate in the revenge event detection module. |
| 329 | `scan_vanilla_squads` | local helper | `levels, victim_squad, offender_squad` | Handles squad lookup, state, membership, or task coordination. |
| 346 | `find_responder` | local helper | `victim_squad, offender_squad` | Finds responder in indexed, runtime, or engine data. |
| 352 | `actor_revenge_roll_passed` | local helper | `` | Handles revenge targeting, hostility, or cleanup in the revenge event detection module. |
| 363 | `actor_revenge_squad_active` | local helper | `squad` | Handles revenge targeting, hostility, or cleanup in the revenge event detection module. |
| 371 | `active_actor_revenge_exists` | local helper | `` | Handles revenge targeting, hostility, or cleanup in the revenge event detection module. |
| 380 | `current_actor_level` | local helper | `` | Resolves or validates level names, ids, or level buckets. |
| 390 | `each_revenge_squad` | local helper | `actor_only, fn` | Handles revenge targeting, hostility, or cleanup in the revenge event detection module. |
| 395 | `visit_squad_id` | local helper | `squad_id` | Handles squad lookup, state, membership, or task coordination. |
| 416 | `M.cancel_active_revenge` | module export | `reason, actor_only` | Cancels active revenge and clears or releases related state. |
| 438 | `actor_revenge_squad_id_for_sleep` | local helper | `` | Handles revenge targeting, hostility, or cleanup in the revenge event detection module. |
| 448 | `pause_actor_revenge_for_sleep` | local helper | `hours` | Handles revenge targeting, hostility, or cleanup in the revenge event detection module. |
| 465 | `restore_paused_actor_revenge_after_sleep` | local helper | `` | Handles revenge targeting, hostility, or cleanup in the revenge event detection module. |
| 487 | `M.apply_online_revenge_hostility` | module export | `` | Handles revenge targeting, hostility, or cleanup in the revenge event detection module. |
| 515 | `consider_squad_id` | local helper | `squad_id` | Handles squad lookup, state, membership, or task coordination. |
| 538 | `sleep_hours_from_ui` | local helper | `ui` | Internal helper for sleep hours from ui in the revenge event detection module. |
| 549 | `install_sleep_hook` | local helper | `` | Installs sleep hook wrappers, callbacks, or diagnostic hooks. |
| 574 | `ui_class.OnButtonSleep` | script hook/global | `self, ...` | Internal helper for OnButtonSleep in the revenge event detection module. |
| 583 | `actor_on_sleep` | local helper | `hours` | Internal helper for actor on sleep in the revenge event detection module. |
| 597 | `actor_on_update` | local helper | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 612 | `M.assign_revenge` | module export | `responder, offender_target_id` | Assigns revenge and updates related ZHOPA state. |
| 633 | `M.on_squad_npc_death` | module export | `victim_squad, se_npc, se_killer` | Handles squad lookup, state, membership, or task coordination. |
| 683 | `M.on_npc_death_callback` | module export | `victim, who` | Registers, unregisters, or wraps callback handling for this module. |
| 694 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 711 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_runtime_patches.script`

Role: chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 46 | `safe_require` | local helper | `name` | Safely resolves require with nil and pcall guards. |
| 57 | `class_candidate` | local helper | `candidate, required_method` | Internal helper for class candidate in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 71 | `script_class` | local helper | `script_name, class_name, required_method` | Internal helper for script class in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 107 | `object_id` | local helper | `obj` | Extracts a stable numeric id from a server object, online object, id-like table, number, or string. |
| 125 | `server_object` | local helper | `id` | Internal helper for server object in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 146 | `M.zhopa2_online_object_by_id` | module export | `id` | Internal helper for online object by id in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 161 | `M.zhopa2_object_location` | module export | `obj` | Internal helper for object location in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 198 | `M.zhopa2_direct_hunt_target_anchor` | module export | `target` | Handles hunt target validation, combat consequences, or pursuit state. |
| 212 | `direct_hunt_target_signature` | local helper | `target` | Handles hunt target validation, combat consequences, or pursuit state. |
| 231 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 239 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 247 | `object_level_name` | local helper | `obj` | Resolves or validates level names, ids, or level buckets. |
| 262 | `global_level_blacklisted` | local helper | `level_name` | Checks or applies blacklist rules for target selection and task safety. |
| 272 | `zhopa2_debug_printf` | local helper | `fmt, ...` | Controls debug output or debug-only state for diagnostics. |
| 278 | `zhopa2_valid_script_target_id` | local helper | `target_id` | Resolves, validates, or formats a task target. |
| 299 | `runtime_time_ms` | local helper | `` | Internal helper for runtime time ms in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 303 | `runtime_log` | local helper | `fmt, ...` | Internal helper for runtime log in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 313 | `runtime_item_key` | local helper | `stage, item` | Internal helper for runtime item key in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 317 | `mark_runtime_item` | local helper | `stage, item, ok, reason, detail` | Marks runtime item for later processing or diagnostics. |
| 337 | `runtime_item_ready` | local helper | `stage, item` | Internal helper for runtime item ready in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 341 | `runtime_error_enabled` | local helper | `` | Internal helper for runtime error enabled in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 345 | `runtime_mark_context` | local helper | `` | Internal helper for runtime mark context in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 368 | `runtime_missing_item` | local helper | `` | Internal helper for runtime missing item in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 389 | `required_script_class` | local helper | `script_name, class_name, surface, required_method` | Internal helper for required script class in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 400 | `start_zhopa_module` | local helper | `name` | Internal helper for start zhopa module in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 428 | `M.ensure_zhopa_modules` | module export | `` | Internal helper for ensure zhopa modules in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 436 | `upvalue` | local helper | `fn, name` | Internal helper for upvalue in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 452 | `set_upvalue` | local helper | `fn, name, value` | Sets upvalue for the current chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration state. |
| 469 | `M.patch_method` | module export | `owner, method, patch_id, wrapper_factory` | Installs or maintains the chain-friendly patch for method. |
| 505 | `install_class_method` | local helper | `cls, name, fn` | Installs class method wrappers, callbacks, or diagnostic hooks. |
| 520 | `patch_required_method` | local helper | `owner, method, patch_id, wrapper_factory, surface` | Installs or maintains the chain-friendly patch for required method. |
| 543 | `game_time` | local helper | `` | Internal helper for game time in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 547 | `elapsed` | local helper | `start_time` | Internal helper for elapsed in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 555 | `perception` | local helper | `` | Internal helper for perception in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 559 | `memory` | local helper | `` | Internal helper for memory in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 563 | `tasks` | local helper | `` | Internal helper for tasks in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 567 | `index` | local helper | `` | Internal helper for index in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 571 | `cache_squad_section_name` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 589 | `squad_player_id` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 610 | `is_monster_squad` | local helper | `squad` | Checks whether monster squad in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration context. |
| 630 | `plain_sim_stalker_squad` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 641 | `managed_stalker_squad` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 645 | `task_invalid_for_monster` | local helper | `squad, task` | Internal helper for task invalid for monster in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 653 | `is_night` | local helper | `` | Checks whether night in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration context. |
| 658 | `write_string` | local helper | `packet, value` | Writes string into serialized state or module data. |
| 662 | `read_string` | local helper | `packet` | Reads string from serialized state, config, or engine data. |
| 670 | `unpack_ids` | local helper | `value` | Internal helper for unpack ids in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 687 | `squad_methods.zhopa2_cleanup_debug` | script hook/global | `self` | Controls debug output or debug-only state for diagnostics. |
| 694 | `squad_methods.zhopa2_release_task_rush` | script hook/global | `self` | Internal helper for release task rush in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 701 | `squad_methods.zhopa2_release_revenge_hostility` | script hook/global | `self` | Handles revenge targeting, hostility, or cleanup in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 708 | `squad_methods.zhopa2_unregister_base_camping_registry` | script hook/global | `self` | Internal helper for unregister base camping registry in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 715 | `squad_methods.zhopa2_sync_base_camping_registry` | script hook/global | `self` | Internal helper for sync base camping registry in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 729 | `squad_methods.zhopa2_is_managed_scripted_target` | script hook/global | `self` | Resolves, validates, or formats a task target. |
| 733 | `squad_methods.zhopa2_reset_state` | script hook/global | `self` | Reads, writes, or repairs runtime state. |
| 761 | `squad_methods.zhopa2_task_requires_rush` | script hook/global | `self` | Internal helper for task requires rush in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 767 | `squad_methods.zhopa2_sync_task_rush` | script hook/global | `self` | Internal helper for sync task rush in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 785 | `squad_methods.zhopa2_clear_task` | script hook/global | `self, reason` | Internal helper for clear task in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 833 | `squad_methods.zhopa2_sanitize_task_owner` | script hook/global | `self, reason` | Internal helper for sanitize task owner in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 841 | `squad_methods.zhopa2_global_level_blacklisted` | script hook/global | `self` | Checks or applies blacklist rules for target selection and task safety. |
| 846 | `squad_methods.zhopa2_purge_global_level_blacklist` | script hook/global | `self, reason` | Checks or applies blacklist rules for target selection and task safety. |
| 864 | `squad_methods.zhopa2_can_manage` | script hook/global | `self` | Internal helper for can manage in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 901 | `squad_methods.zhopa2_assign_task` | script hook/global | `self, task, target_id, duration_sec, reason, patrol` | Internal helper for assign task in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 943 | `squad_methods.zhopa2_assign_rest` | script hook/global | `self, reason` | Internal helper for assign rest in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 948 | `squad_methods.zhopa2_reached_target` | script hook/global | `self` | Resolves, validates, or formats a task target. |
| 955 | `squad_methods.zhopa2_patrol_next` | script hook/global | `self` | Internal helper for patrol next in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 973 | `squad_methods.zhopa2_task_completed` | script hook/global | `self` | Internal helper for task completed in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1013 | `squad_methods.zhopa2_target_is_alive` | script hook/global | `self` | Resolves, validates, or formats a task target. |
| 1040 | `squad_methods.zhopa2_update_task` | script hook/global | `self` | Internal helper for update task in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1058 | `squad_methods.zhopa2_get_script_target` | script hook/global | `self` | Resolves, validates, or formats a task target. |
| 1105 | `squad_methods.zhopa2_prepare_hunt_target` | script hook/global | `self, script_target_id` | Handles hunt target validation, combat consequences, or pursuit state. |
| 1137 | `squad_methods.zhopa2_apply_revenge_hostility` | script hook/global | `self` | Handles revenge targeting, hostility, or cleanup in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1145 | `squad_methods.zhopa2_state_write` | script hook/global | `self, packet` | Reads, writes, or repairs runtime state. |
| 1165 | `squad_methods.zhopa2_state_read` | script hook/global | `self, packet` | Reads, writes, or repairs runtime state. |
| 1198 | `squad_methods.zhopa2_debug_offline_inventory_update_dump` | script hook/global | `self` | Scans, classifies, or mutates NPC/server inventory state. |
| 1202 | `install_squad_methods` | local helper | `cls` | Installs squad methods wrappers, callbacks, or diagnostic hooks. |
| 1208 | `wrapped_returns` | local helper | `original, self, ...` | Internal helper for wrapped returns in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1213 | `retrofit_existing_squads` | local helper | `` | Handles squad lookup, state, membership, or task coordination. |
| 1232 | `M.patch_sim_squad_scripted` | module export | `` | Installs or maintains the chain-friendly patch for sim squad scripted. |
| 1412 | `obj_level` | local helper | `obj` | Resolves or validates level names, ids, or level buckets. |
| 1427 | `prop_value` | local helper | `props, key` | Internal helper for prop value in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1431 | `smart_is_base` | local helper | `smart, props` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1443 | `smart_kind_flags` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1469 | `level_bucket` | local helper | `root, level_name` | Resolves or validates level names, ids, or level buckets. |
| 1477 | `kind_bucket` | local helper | `root, level_name, kind` | Internal helper for kind bucket in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1486 | `trim` | local helper | `value` | Internal helper for trim in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1493 | `lower` | local helper | `value` | Internal helper for lower in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1497 | `contains` | local helper | `haystack, needle` | Internal helper for contains in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1501 | `ini_string` | local helper | `ini, section, key` | Internal helper for ini string in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1515 | `ini_section_exists` | local helper | `ini, section` | Internal helper for ini section exists in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1523 | `open_ini` | local helper | `path` | Internal helper for open ini in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1532 | `smart_cfg_filename` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1552 | `smart_ini` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1561 | `beh_ini` | local helper | `` | Internal helper for beh ini in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1569 | `read_job_string` | local helper | `job_or_section, key, smart` | Reads job string from serialized state, config, or engine data. |
| 1582 | `trade_job_flags` | local helper | `job, smart` | Handles trade routing, trade state, or trade diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1610 | `merge_trade_flags` | local helper | `flags, job_flags` | Handles trade routing, trade state, or trade diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1621 | `scan_loaded_trade_jobs` | local helper | `smart, flags` | Handles trade routing, trade state, or trade diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1631 | `scan_exclusive_trade_job` | local helper | `smart, flags, work_field, work_path` | Handles trade routing, trade state, or trade diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1642 | `scan_smart_ini_trade_jobs` | local helper | `smart, flags` | Handles trade routing, trade state, or trade diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1670 | `scan_beh_trade_jobs` | local helper | `smart, flags` | Handles trade routing, trade state, or trade diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1688 | `remove_smart_from_level_buckets` | local helper | `board, smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1715 | `board_methods.zhopa2_ensure_buckets` | script hook/global | `self` | Internal helper for ensure buckets in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1730 | `board_methods.zhopa2_register_trade_smart` | script hook/global | `self, smart` | Handles trade routing, trade state, or trade diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1759 | `board_methods.zhopa2_unregister_trade_smart` | script hook/global | `self, smart` | Handles trade routing, trade state, or trade diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1774 | `board_methods.zhopa2_register_smart` | script hook/global | `self, obj` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1800 | `board_methods.zhopa2_unregister_smart` | script hook/global | `self, obj` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1818 | `board_methods.zhopa2_update_squad_level` | script hook/global | `self, squad, level_name` | Handles squad lookup, state, membership, or task coordination. |
| 1856 | `board_methods.zhopa2_unregister_squad` | script hook/global | `self, squad` | Handles squad lookup, state, membership, or task coordination. |
| 1868 | `board_methods.zhopa2_rebuild_buckets` | script hook/global | `self` | Internal helper for rebuild buckets in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1895 | `install_board_methods` | local helper | `cls` | Installs board methods wrappers, callbacks, or diagnostic hooks. |
| 1901 | `M.patch_sim_board` | module export | `` | Installs or maintains the chain-friendly patch for sim board. |
| 1975 | `service_fillers` | local helper | `` | Internal helper for service fillers in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1979 | `service_job_fallback` | local helper | `npc_info, job, smart` | Internal helper for service job fallback in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 1988 | `live_targeted_gather_id` | local helper | `npc_info` | Resolves, validates, or formats a task target. |
| 2015 | `targeted_gather_blocks_job` | local helper | `smart, npc_info` | Resolves, validates, or formats a task target. |
| 2031 | `clear_trade_path_override` | local helper | `st` | Clears trade path override from module or squad state. |
| 2057 | `clear_forced_trade_job` | local helper | `st` | Clears forced trade job from module or squad state. |
| 2074 | `reset_beh_path_index` | local helper | `npc` | Resets beh path index to its default safe state. |
| 2081 | `reassign_forced_trade_job` | local helper | `smart, npc_info, st, npc_id, force_section` | Handles trade routing, trade state, or trade diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2117 | `forced_trade_blocks_job` | local helper | `smart, npc_info` | Handles trade routing, trade state, or trade diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2154 | `try_service_fallback_job` | local helper | `smart, npc_info` | Attempts service fallback job and returns a controlled result instead of hard-failing. |
| 2199 | `ensure_service_job` | local helper | `smart, npc_info` | Internal helper for ensure service job in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2223 | `refresh_job_capacity` | local helper | `smart` | Refreshes job capacity from current runtime or indexed data. |
| 2256 | `M.patch_smart_terrain` | module export | `` | Installs or maintains the chain-friendly patch for smart terrain. |
| 2307 | `artifact_index` | local helper | `` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2311 | `register_artifact` | local helper | `artifact_id, zone, section` | Registers artifact in the module indexes or callbacks. |
| 2318 | `unregister_artifact` | local helper | `artifact_id, reason` | Unregisters artifact and cleans stale references. |
| 2325 | `unregister_zone_artifacts` | local helper | `zone, reason` | Unregisters zone artifacts and cleans stale references. |
| 2332 | `register_anomaly_zone` | local helper | `zone, cfg_file, source` | Registers anomaly zone in the module indexes or callbacks. |
| 2339 | `virtual_artifacts_for_zone` | local helper | `zone` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2348 | `materialize_virtual_artifact` | local helper | `virtual_id, real_id, zone, section` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2355 | `zone_key` | local helper | `zone` | Internal helper for zone key in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2361 | `M.zhopa2_sync_existing_anomaly_zones` | module export | `source` | Internal helper for sync existing anomaly zones in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2396 | `zhopa2_materialize_virtual_artifact_online` | script hook/global | `virtual_id` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2415 | `anomaly_spawn_artefact_section` | local helper | `self, section` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2438 | `anomaly_materialize_virtual_artifacts` | local helper | `self` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2453 | `M.patch_bind_anomaly_zone` | module export | `` | Installs or maintains the chain-friendly patch for bind anomaly zone. |
| 2545 | `M.zhopa2_direct_hunt_live_location` | module export | `squad` | Handles hunt target validation, combat consequences, or pursuit state. |
| 2569 | `M.zhopa2_direct_hunt_commander_execute` | module export | `self, squad` | Handles hunt target validation, combat consequences, or pursuit state. |
| 2604 | `M.patch_xr_reach_task` | module export | `` | Installs or maintains the chain-friendly patch for xr reach task. |
| 2622 | `task_run` | local helper | `squad` | Internal helper for task run in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2630 | `direct_monster_update` | local helper | `self` | Internal helper for direct monster update in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2694 | `M.patch_bind_monster` | module export | `` | Installs or maintains the chain-friendly patch for bind monster. |
| 2711 | `offline_loot_on_death` | local helper | `victim, killer` | Handles loot selection, pickup, accounting, or diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2715 | `debug_name` | local helper | `obj` | Controls debug output or debug-only state for diagnostics. |
| 2783 | `patch_death_class` | local helper | `cls, patch_name` | Installs or maintains the chain-friendly patch for death class. |
| 2795 | `M.patch_sim_offline_combat` | module export | `` | Installs or maintains the chain-friendly patch for sim offline combat. |
| 2818 | `gather_mod` | local helper | `` | Internal helper for gather mod in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2822 | `corpse_mod` | local helper | `` | Handles corpse target filtering, looting, or loop prevention. |
| 2826 | `module_member` | local helper | `mod, name` | Handles squad member lookup, inventory ownership, or relation state. |
| 2830 | `export_script_function` | local helper | `mod, name, fn` | Internal helper for export script function in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2840 | `gather_original_func` | local helper | `mod, name` | Internal helper for gather original func in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2856 | `gather_upvalue` | local helper | `name` | Internal helper for gather upvalue in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2862 | `set_gather_upvalue` | local helper | `name, value` | Sets gather upvalue for the current chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration state. |
| 2868 | `gather_items_table` | local helper | `` | Internal helper for gather items table in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2877 | `zhopa2_loot_mod` | local helper | `` | Handles loot selection, pickup, accounting, or diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2881 | `zhopa2_loot_active` | local helper | `npc` | Handles loot selection, pickup, accounting, or diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2886 | `zhopa2_loot_globally_enabled` | local helper | `` | Handles loot selection, pickup, accounting, or diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2891 | `M.zhopa2_sync_gather_runtime_state` | module export | `` | Reads, writes, or repairs runtime state. |
| 2954 | `zhopa2_can_take_section` | local helper | `npc, item, section` | Internal helper for can take section in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2962 | `zhopa2_event_item_ids` | local helper | `` | Internal helper for event item ids in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 2970 | `zhopa2_targeted_item_ids` | local helper | `npc` | Resolves, validates, or formats a task target. |
| 2978 | `zhopa2_item_targeted_for_npc` | local helper | `npc, item_id, ids` | Resolves, validates, or formats a task target. |
| 3000 | `zhopa2_item_reserved_for_other` | local helper | `npc, item_id` | Internal helper for item reserved for other in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3008 | `zhopa2_item_clsid` | local helper | `item` | Internal helper for item clsid in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3016 | `zhopa2_item_detect_dist_sqr` | local helper | `` | Internal helper for item detect dist sqr in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3024 | `zhopa2_record_loot` | local helper | `npc, item, reason` | Handles loot selection, pickup, accounting, or diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3032 | `M.zhopa2_note_vanilla_artifact_pickup` | module export | `npc, artifact_id, section` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3041 | `zhopa2_should_skip_overweight` | local helper | `npc` | Internal helper for should skip overweight in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3045 | `zhopa2_should_skip_condlist` | local helper | `npc` | Internal helper for should skip condlist in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3049 | `zhopa2_item_reserved_by` | local helper | `item_id` | Internal helper for item reserved by in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3055 | `zhopa2_reservation_is_live` | local helper | `owner_id, item_id` | Internal helper for reservation is live in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3072 | `zhopa2_clear_artifact_scan` | local helper | `st` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3082 | `zhopa2_reset_artifact_approach` | local helper | `st` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3100 | `zhopa2_mark_approach_failed` | local helper | `st, item_id, reason` | Internal helper for mark approach failed in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3108 | `zhopa2_clear_approach_failure` | local helper | `st, item_id` | Internal helper for clear approach failure in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3119 | `zhopa2_object_vertex` | local helper | `obj` | Internal helper for object vertex in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3136 | `zhopa2_valid_accessible_vertex` | local helper | `npc, vid` | Internal helper for valid accessible vertex in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3150 | `zhopa2_nearest_accessible_vertex` | local helper | `npc, pos` | Internal helper for nearest accessible vertex in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3172 | `zhopa2_vertex_in_direction` | local helper | `npc, from_vid, dir, dist` | Internal helper for vertex in direction in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3185 | `zhopa2_select_artifact_approach` | local helper | `npc, item, item_pos, start_index, bad_vids` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3223 | `zhopa2_safe_look_position` | local helper | `npc, pos` | Internal helper for safe look position in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3234 | `zhopa2_artifact_approach_reached` | local helper | `npc, st` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3241 | `zhopa2_artifact_pickup_ready` | local helper | `npc, st` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3249 | `M.zhopa2_artifact_vanilla_pickup_reachable` | module export | `npc, st, item` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3270 | `zhopa2_artifact_approach_progress_ok` | local helper | `npc, st` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3293 | `M.zhopa2_gather_stalled` | module export | `npc, st, item_id, target_pos` | Internal helper for gather stalled in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3335 | `zhopa2_prepare_next_artifact_approach` | local helper | `npc, st, item, item_pos, reason` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3358 | `zhopa2_send_to_artifact_vertex` | local helper | `npc, st, invalid_reason` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3376 | `zhopa2_evaluator_camper_end_for_gather:__init` | script hook/global | `name` | Internal helper for init in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3378 | `zhopa2_evaluator_camper_end_for_gather:evaluate` | script hook/global | `` | Internal helper for evaluate in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3399 | `zhopa2_apply_camper_end_override` | local helper | `manager` | Internal helper for apply camper end override in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3413 | `zhopa2_add_gather_precondition` | local helper | `manager, action_id` | Internal helper for add gather precondition in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3430 | `zhopa2_job_action_key` | local helper | `root` | Internal helper for job action key in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3441 | `zhopa2_suspend_active_scheme_for_targeted_gather` | local helper | `npc, st` | Resolves, validates, or formats a task target. |
| 3465 | `zhopa2_restore_active_scheme_after_targeted_gather` | local helper | `npc, st` | Resolves, validates, or formats a task target. |
| 3483 | `zhopa2_apply_job_preconditions` | local helper | `npc, st` | Internal helper for apply job preconditions in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3527 | `zhopa2_start_artifact_scan` | local helper | `npc, st, item, now` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3538 | `zhopa2_update_artifact_scan` | local helper | `npc, st, item, now` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3559 | `zhopa2_begin_artifact_pickup` | local helper | `npc, st, item, now, force` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3571 | `M.zhopa2_try_artifact_force_pickup` | module export | `npc, st, item, now, reason` | Handles artifact-related state in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3587 | `zhopa2_reset_gather_state` | local helper | `st` | Reads, writes, or repairs runtime state. |
| 3618 | `zhopa2_item_reservation_owner_impl` | local helper | `item_id` | Internal helper for item reservation owner impl in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3628 | `zhopa2_prepare_targeted_gather_impl` | local helper | `npc, item_id` | Resolves, validates, or formats a task target. |
| 3639 | `zhopa2_force_gather_item` | script hook/global | `npc, item_id, targeted` | Internal helper for force gather item in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3720 | `zhopa2_clear_gather_item` | script hook/global | `npc, item_id, reason` | Internal helper for clear gather item in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3741 | `M.zhopa2_try_force_online_gather_item` | module export | `npc, st` | Internal helper for try force online gather item in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3749 | `consider` | local helper | `item_id` | Internal helper for consider in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3799 | `M.zhopa2_gather_item_active` | module export | `npc, item_id` | Internal helper for gather item active in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3827 | `zhopa2_gather_item_failure_reason_impl` | local helper | `npc, item_id` | Internal helper for gather item failure reason impl in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3838 | `zhopa2_gather_item_debug_status_impl` | local helper | `npc, item_id` | Controls debug output or debug-only state for diagnostics. |
| 3876 | `zhopa2_gather_item_replacement` | local helper | `original, force_selected` | Internal helper for gather item replacement in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 3975 | `patch_gather_classes` | local helper | `mod` | Installs or maintains the chain-friendly patch for gather classes. |
| 4248 | `M.patch_xr_gather_items` | module export | `` | Installs or maintains the chain-friendly patch for xr gather items. |
| 4268 | `mod.zhopa2_wrapped_near_actor` | assigned wrapper | `obj, npc, ...` | Internal helper for wrapped near actor in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4288 | `zhopa2_is_protected_corpse` | local helper | `corpse, corpse_id` | Handles corpse target filtering, looting, or loop prevention. |
| 4296 | `zhopa2_event_corpse_ids` | local helper | `` | Handles corpse target filtering, looting, or loop prevention. |
| 4304 | `zhopa2_forget_corpse_id` | local helper | `corpse_id, consume_only` | Handles corpse target filtering, looting, or loop prevention. |
| 4313 | `zhopa2_mark_corpse_checked` | local helper | `corpse_id` | Handles corpse target filtering, looting, or loop prevention. |
| 4320 | `M.zhopa2_mark_corpse_exhausted` | module export | `corpse_id` | Handles corpse target filtering, looting, or loop prevention. |
| 4343 | `M.zhopa2_corpse_exhausted` | module export | `corpse_id` | Handles corpse target filtering, looting, or loop prevention. |
| 4349 | `zhopa2_reject_corpse_candidate` | local helper | `mod, st, corpse_id` | Handles corpse target filtering, looting, or loop prevention. |
| 4401 | `zhopa2_corpse_detect_dist_sqr` | local helper | `` | Handles corpse target filtering, looting, or loop prevention. |
| 4409 | `zhopa2_corpse_already_looted` | local helper | `corpse` | Handles loot selection, pickup, accounting, or diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4416 | `zhopa2_is_inventory_owner` | local helper | `obj` | Scans, classifies, or mutates NPC/server inventory state. |
| 4433 | `zhopa2_corpse_has_money` | local helper | `corpse` | Reads, writes, or transfers NPC money/economy state. |
| 4442 | `M.zhopa2_corpse_can_take_item` | module export | `npc, item, section` | Handles corpse target filtering, looting, or loop prevention. |
| 4455 | `zhopa2_corpse_has_takeable_item` | local helper | `npc, corpse, active` | Handles corpse target filtering, looting, or loop prevention. |
| 4465 | `check_item` | local helper | `owner, item` | Internal helper for check item in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4480 | `zhopa2_corpse_has_candidate_loot` | local helper | `npc, corpse, corpse_id, active` | Handles loot selection, pickup, accounting, or diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4500 | `zhopa2_corpse_record_loot` | local helper | `npc, corpse, item, value, reason` | Handles loot selection, pickup, accounting, or diagnostics in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4508 | `zhopa2_item_value` | local helper | `section` | Internal helper for item value in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4515 | `corpse_original_func` | local helper | `mod, name` | Handles corpse target filtering, looting, or loop prevention. |
| 4526 | `zhopa2_get_all_from_corpse_replacement` | local helper | `original` | Handles corpse target filtering, looting, or loop prevention. |
| 4580 | `get_item` | local helper | `owner, item` | Returns item for the current chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration state. |
| 4622 | `patch_corpse_classes` | local helper | `mod` | Installs or maintains the chain-friendly patch for corpse classes. |
| 4623 | `corpse_object` | local helper | `corpse_id` | Handles corpse target filtering, looting, or loop prevention. |
| 4630 | `reject_if_protected` | local helper | `st, corpse_id` | Internal helper for reject if protected in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4639 | `cleanup_protected_state` | local helper | `st` | Cleans up protected state and removes stale runtime state. |
| 4765 | `M.patch_xr_corpse_detection` | module export | `` | Installs or maintains the chain-friendly patch for xr corpse detection. |
| 4777 | `mod.zhopa2_wrapped_near_actor` | assigned wrapper | `obj, npc, ...` | Internal helper for wrapped near actor in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4790 | `M.patch_se_level_changer` | module export | `` | Installs or maintains the chain-friendly patch for se level changer. |
| 4796 | `run_runtime_patch` | local helper | `patch` | Internal helper for run runtime patch in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4823 | `M.ensure_all` | module export | `reason` | Internal helper for ensure all in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4835 | `M._on_game_load` | module export | `` | Internal helper for on game load in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4840 | `M._actor_on_first_update` | module export | `` | Internal helper for actor on first update in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4850 | `M._runtime_recheck_due` | module export | `reason` | Internal helper for runtime recheck due in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4868 | `M.runtime_not_ready_reason` | module export | `` | Internal helper for runtime not ready reason in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4873 | `M.runtime_ready` | module export | `reason` | Checks the shared ZHOPA runtime readiness barrier before running context-dependent work. |
| 4882 | `M.runtime_gate_ready` | module export | `reason` | Internal helper for runtime gate ready in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4886 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 4901 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 4905 | `_G.zhopa2_runtime_ready` | assigned wrapper | `reason` | Internal helper for runtime ready in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |
| 4909 | `_G.zhopa2_runtime_not_ready_reason` | assigned wrapper | `` | Internal helper for runtime not ready reason in the chain-friendly runtime patches over vanilla/GAMMA scripts and readiness orchestration module. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_save_cleanup.script`

Role: legacy save detection and cleanup for SISKI/old ZHOPA/ZHOPA2 migration paths.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 106 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 117 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 125 | `debug_enabled` | local helper | `` | Controls debug output or debug-only state for diagnostics. |
| 129 | `debug_log` | local helper | `fmt, ...` | Emits a guarded debug log line for this module. |
| 135 | `cleanup_enabled` | local helper | `` | Cleans up enabled and removes stale runtime state. |
| 139 | `cleanup_dry_run` | local helper | `` | Cleans up dry run and removes stale runtime state. |
| 143 | `remove_zhopa2_state` | local helper | `` | Reads, writes, or repairs runtime state. |
| 147 | `mark_legacy_squad_id` | local helper | `id` | Marks legacy squad id for later processing or diagnostics. |
| 154 | `collect_squad_ids_from_state` | local helper | `data` | Collects squad ids from state from indexed or runtime data. |
| 172 | `add_found` | local helper | `result, key, source, squad_count` | Internal helper for add found in the legacy save detection and cleanup for SISKI/old ZHOPA/ZHOPA2 migration paths module. |
| 181 | `scan_keys` | local helper | `m_data, keys, source, result` | Internal helper for scan keys in the legacy save detection and cleanup for SISKI/old ZHOPA/ZHOPA2 migration paths module. |
| 193 | `M.scan_m_data` | module export | `m_data` | Internal helper for scan m data in the legacy save detection and cleanup for SISKI/old ZHOPA/ZHOPA2 migration paths module. |
| 207 | `log_scan_result` | local helper | `result, source, dry_run` | Internal helper for log scan result in the legacy save detection and cleanup for SISKI/old ZHOPA/ZHOPA2 migration paths module. |
| 220 | `M.cleanup_m_data` | module export | `m_data, opts` | Cleans up m data and removes stale runtime state. |
| 239 | `server_object` | local helper | `id` | Internal helper for server object in the legacy save detection and cleanup for SISKI/old ZHOPA/ZHOPA2 migration paths module. |
| 258 | `cleanup_table_fields` | local helper | `tbl, fields, dry_run` | Cleans up table fields and removes stale runtime state. |
| 275 | `cleanup_storage_entry` | local helper | `st, dry_run` | Cleans up storage entry and removes stale runtime state. |
| 286 | `cleanup_db_storage` | local helper | `dry_run` | Cleans up db storage and removes stale runtime state. |
| 297 | `cleanup_legacy_squad` | local helper | `squad, dry_run` | Cleans up legacy squad and removes stale runtime state. |
| 319 | `cleanup_zhopa2_squad` | local helper | `squad, dry_run` | Cleans up squad and removes stale runtime state. |
| 342 | `cleanup_pending_legacy_squads` | local helper | `dry_run` | Cleans up pending legacy squads and removes stale runtime state. |
| 353 | `cleanup_all_zhopa2_squads` | local helper | `dry_run` | Cleans up all zhopa2 squads and removes stale runtime state. |
| 366 | `M.cleanup_runtime_objects` | module export | `source` | Cleans up runtime objects and removes stale runtime state. |
| 387 | `M.should_write_squad_state` | module export | `` | Decides whether write squad state should run for the current legacy save detection and cleanup for SISKI/old ZHOPA/ZHOPA2 migration paths state. |
| 391 | `load_state` | local helper | `m_data` | Load callback; restores this module's serializable global state from the save packet/table. |
| 398 | `save_state` | local helper | `m_data` | Save callback; writes this module's serializable global state into the save packet/table. |
| 404 | `on_game_load` | local helper | `` | Game-load callback; schedules reconciliation or clears stale runtime-only state after loading a save. |
| 408 | `actor_on_first_update` | local helper | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 412 | `on_option_change` | local helper | `` | MCM option-change callback; invalidates cached settings and reschedules affected runtime work. |
| 416 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 442 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_service_fillers.script`

Role: dynamic service NPC placement and service job repair for owned bases.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 87 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 96 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 104 | `runtime_ready` | local helper | `reason` | Checks the shared ZHOPA runtime readiness barrier before running context-dependent work. |
| 116 | `cfg_alias` | local helper | `name` | Reads or resolves configuration data for alias. |
| 127 | `normalize_key` | local helper | `name` | Normalizes key into a stable internal representation. |
| 140 | `owner_engine` | local helper | `name` | Internal helper for owner engine in the dynamic service NPC placement and service job repair for owned bases module. |
| 149 | `service_alias` | local helper | `engine` | Internal helper for service alias in the dynamic service NPC placement and service job repair for owned bases module. |
| 154 | `vanilla_prefix` | local helper | `engine` | Internal helper for vanilla prefix in the dynamic service NPC placement and service job repair for owned bases module. |
| 159 | `tg` | local helper | `` | Returns the current time value used by throttled diagnostics. |
| 163 | `safe_manager` | local helper | `module_name, getter_name` | Safely resolves manager with nil and pcall guards. |
| 174 | `manager_time_due` | local helper | `mgr, last_field` | Internal helper for manager time due in the dynamic service NPC placement and service job repair for owned bases module. |
| 194 | `callback_from_start` | local helper | `` | Registers, unregisters, or wraps callback handling for this module. |
| 207 | `surge_event_due` | local helper | `` | Internal helper for surge event due in the dynamic service NPC placement and service job repair for owned bases module. |
| 212 | `psi_storm_event_due` | local helper | `` | Internal helper for psi storm event due in the dynamic service NPC placement and service job repair for owned bases module. |
| 217 | `queue_emission_fill` | local helper | `kind, due` | Internal helper for queue emission fill in the dynamic service NPC placement and service job repair for owned bases module. |
| 226 | `flush_pending_emission_fill` | local helper | `` | Internal helper for flush pending emission fill in the dynamic service NPC placement and service job repair for owned bases module. |
| 241 | `smart_is_base` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 245 | `smart_name` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 262 | `section_exists` | local helper | `section` | Internal helper for section exists in the dynamic service NPC placement and service job repair for owned bases module. |
| 275 | `read_ini_string_from` | local helper | `ini, section, key` | Reads ini string from from serialized state, config, or engine data. |
| 294 | `read_ini_string` | local helper | `job_or_section, key, smart` | Reads ini string from serialized state, config, or engine data. |
| 314 | `contains` | local helper | `haystack, needle` | Internal helper for contains in the dynamic service NPC placement and service job repair for owned bases module. |
| 318 | `strip_inline_comment` | local helper | `value` | Internal helper for strip inline comment in the dynamic service NPC placement and service job repair for owned bases module. |
| 329 | `plain_unique_provider_suitable` | local helper | `job_or_section, smart` | Internal helper for plain unique provider suitable in the dynamic service NPC placement and service job repair for owned bases module. |
| 344 | `role_from_level_spot` | local helper | `level_spot` | Resolves or validates level names, ids, or level buckets. |
| 351 | `normalize_role` | local helper | `role` | Normalizes role into a stable internal representation. |
| 365 | `classify_job_role` | local helper | `job_or_section, smart` | Internal helper for classify job role in the dynamic service NPC placement and service job repair for owned bases module. |
| 442 | `role_from_section` | local helper | `section` | Internal helper for role from section in the dynamic service NPC placement and service job repair for owned bases module. |
| 461 | `safe_npc_section` | local helper | `se_obj` | Safely resolves npc section with nil and pcall guards. |
| 474 | `safe_squad_by_id` | local helper | `id` | Safely resolves squad by id with nil and pcall guards. |
| 499 | `online_object` | local helper | `se_obj` | Internal helper for online object in the dynamic service NPC placement and service job repair for owned bases module. |
| 517 | `is_stalker_se` | local helper | `se_obj` | Checks whether stalker se in the dynamic service NPC placement and service job repair for owned bases context. |
| 527 | `set_online_community` | local helper | `se_obj, engine_owner` | Sets online community for the current dynamic service NPC placement and service job repair for owned bases state. |
| 541 | `service_squad_from_member` | local helper | `se_obj` | Handles squad lookup, state, membership, or task coordination. |
| 549 | `pin_service_squad` | local helper | `squad, smart, section` | Handles squad lookup, state, membership, or task coordination. |
| 573 | `adopt_service_squad` | local helper | `squad, smart, engine_owner, section` | Handles squad lookup, state, membership, or task coordination. |
| 581 | `adopt_service_member` | local helper | `se_obj, smart, engine_owner, section` | Handles squad member lookup, inventory ownership, or relation state. |
| 593 | `collect_allowed_roles` | local helper | `smart` | Collects allowed roles from indexed or runtime data. |
| 608 | `role_from_member_info` | local helper | `info, smart` | Handles squad member lookup, inventory ownership, or relation state. |
| 625 | `M.job_accepts_service_npc` | module export | `npc_info, job, smart` | Internal helper for job accepts service npc in the dynamic service NPC placement and service job repair for owned bases module. |
| 643 | `collect_existing_roles` | local helper | `smart, engine_owner` | Collects existing roles from indexed or runtime data. |
| 682 | `roles_from_set` | local helper | `set` | Internal helper for roles from set in the dynamic service NPC placement and service job repair for owned bases module. |
| 696 | `missing_roles` | local helper | `allowed, existing` | Internal helper for missing roles in the dynamic service NPC placement and service job repair for owned bases module. |
| 707 | `roles_string` | local helper | `roles` | Internal helper for roles string in the dynamic service NPC placement and service job repair for owned bases module. |
| 714 | `clear_smart_fields` | local helper | `smart` | Clears smart fields from module or squad state. |
| 726 | `mark_smart` | local helper | `smart, engine_owner, missing, reason` | Marks smart for later processing or diagnostics. |
| 741 | `unmark_smart` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 747 | `resolve_ownership` | local helper | `smart, ownership` | Resolves ownership into a usable runtime object or value. |
| 764 | `service_section` | local helper | `engine_owner, role` | Internal helper for service section in the dynamic service NPC placement and service job repair for owned bases module. |
| 791 | `spawn_service_squad` | local helper | `smart, engine_owner, role` | Spawns service squad through guarded server-side creation logic. |
| 810 | `M.reconcile_smart` | module export | `smart, ownership, allow_spawn, reason` | Reconciles smart after load, registration, or delayed readiness. |
| 867 | `smart_by_id` | local helper | `id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 879 | `M.fill_marked_smarts` | module export | `reason` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 904 | `M.on_smart_update` | module export | `smart, ownership` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 911 | `M.on_smart_unregister` | module export | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 916 | `M.on_before_surge` | module export | `flags` | Internal helper for on before surge in the dynamic service NPC placement and service job repair for owned bases module. |
| 923 | `M.on_before_psi_storm` | module export | `flags` | Internal helper for on before psi storm in the dynamic service NPC placement and service job repair for owned bases module. |
| 930 | `M.actor_on_update` | module export | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 937 | `M.on_game_load` | module export | `` | Game-load callback; schedules reconciliation or clears stale runtime-only state after loading a save. |
| 942 | `server_entity_on_unregister` | local helper | `se_obj, type_name` | Server-entity unregister callback; removes stale ids and releases runtime ownership for disappearing objects. |
| 948 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 967 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_story_north_migration.script`

Role: story-gated north migration event, selected squad locking, retargeting, and save recovery.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 58 | `load_module` | local helper | `name` | Loads an optional Lua module through raw globals or guarded require. |
| 67 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 71 | `index_mod` | local helper | `` | Resolves the ZHOPA index module if it is loaded or can be required safely. |
| 75 | `perception_mod` | local helper | `` | Resolves the ZHOPA perception module if it is loaded or can be required safely. |
| 79 | `topology_mod` | local helper | `` | Handles level-neighbor topology data. |
| 83 | `runtime_ready` | local helper | `reason` | Checks the shared ZHOPA runtime readiness barrier before running context-dependent work. |
| 95 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 103 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 111 | `debug_enabled` | local helper | `` | Controls debug output or debug-only state for diagnostics. |
| 115 | `debug_log` | local helper | `fmt, ...` | Emits a guarded debug log line for this module. |
| 121 | `now_ms` | local helper | `` | Returns the current game or device time in milliseconds for throttling and cooldown checks. |
| 125 | `normalize_id` | local helper | `value` | Normalizes id into a stable internal representation. |
| 133 | `normalize_status` | local helper | `value` | Normalizes status into a stable internal representation. |
| 144 | `normalize_sid_set` | local helper | `src` | Normalizes sid set into a stable internal representation. |
| 163 | `normalize_status_map` | local helper | `src` | Normalizes status map into a stable internal representation. |
| 177 | `event_state` | local helper | `` | Reads, writes, or repairs runtime state. |
| 190 | `resolve_object` | local helper | `id` | Resolves object into a usable runtime object or value. |
| 215 | `object_level` | local helper | `obj` | Resolves or validates level names, ids, or level buckets. |
| 244 | `safe_name` | local helper | `obj` | Safely resolves name with nil and pcall guards. |
| 257 | `squad_section_name` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 275 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 283 | `normalize_faction` | local helper | `value` | Normalizes faction into a stable internal representation. |
| 298 | `squad_faction` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 309 | `relation_faction` | local helper | `value` | Internal helper for relation faction in the story-gated north migration event module. |
| 314 | `relation_allows_coexist` | local helper | `source_faction, other_faction` | Internal helper for relation allows coexist in the story-gated north migration event module. |
| 333 | `is_story_mode_active` | local helper | `` | Checks whether story mode active in the story-gated north migration event context. |
| 357 | `has_info` | local helper | `info` | Checks whether info is present in the story-gated north migration event context. |
| 377 | `trigger_active` | local helper | `` | Internal helper for trigger active in the story-gated north migration event module. |
| 381 | `feature_enabled_now` | local helper | `` | Internal helper for feature enabled now in the story-gated north migration event module. |
| 387 | `percent_value` | local helper | `` | Internal helper for percent value in the story-gated north migration event module. |
| 397 | `is_monster_squad` | local helper | `squad` | Checks whether monster squad in the story-gated north migration event context. |
| 406 | `squad_can_manage` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 421 | `is_ap_owned_squad` | local helper | `squad` | Checks whether ap owned squad in the story-gated north migration event context. |
| 430 | `is_plain_stalker_sim_squad` | local helper | `squad` | Checks whether plain stalker sim squad in the story-gated north migration event context. |
| 441 | `eligible_squad` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 455 | `smart_by_id` | local helper | `smart_id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 468 | `target_validation_opts` | local helper | `kind` | Resolves, validates, or formats a task target. |
| 479 | `collect_target_factions` | local helper | `smart` | Collects target factions from indexed or runtime data. |
| 510 | `target_safe_for_squad` | local helper | `squad, smart, expected_level, kind` | Handles squad lookup, state, membership, or task coordination. |
| 534 | `game_graph_distance` | local helper | `a, b` | Internal helper for game graph distance in the story-gated north migration event module. |
| 557 | `pick_random` | local helper | `list` | Selects random from validated candidates. |
| 564 | `shuffle_in_place` | local helper | `list` | Internal helper for shuffle in place in the story-gated north migration event module. |
| 577 | `smarts_on_level` | local helper | `level_name, kind` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 585 | `base_smarts_on_level` | local helper | `level_name` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 593 | `projected_load` | local helper | `level_name, exclude_sid` | Internal helper for projected load in the story-gated north migration event module. |
| 609 | `ordered_north_levels` | local helper | `squad` | Handles north migration story event selection, routing, or recovery. |
| 646 | `nearest_safe_from_list` | local helper | `squad, level_name, list, kind` | Internal helper for nearest safe from list in the story-gated north migration event module. |
| 668 | `safe_random_smart` | local helper | `squad, level_name` | Safely resolves random smart with nil and pcall guards. |
| 680 | `pick_safe_target_on_level` | local helper | `squad, level_name` | Selects safe target on level from validated candidates. |
| 695 | `neighbor_levels` | local helper | `level_name` | Resolves or validates level names, ids, or level buckets. |
| 706 | `pick_north_target` | local helper | `squad` | Selects north target from validated candidates. |
| 733 | `story_task_active` | local helper | `squad` | Handles story-gated state, tasks, or diagnostic output. |
| 737 | `set_status` | local helper | `sid, status` | Sets status for the current story-gated north migration event state. |
| 744 | `M.is_story_task` | module export | `task` | Checks whether story task in the story-gated north migration event context. |
| 749 | `M.is_sid_selected` | module export | `sid` | Checks whether sid selected in the story-gated north migration event context. |
| 754 | `M.is_sid_locked` | module export | `sid` | Checks whether sid locked in the story-gated north migration event context. |
| 763 | `save_state` | local helper | `m_data` | Save callback; writes this module's serializable global state into the save packet/table. |
| 778 | `load_state` | local helper | `m_data` | Load callback; restores this module's serializable global state from the save packet/table. |
| 810 | `clear_story_task` | local helper | `squad, reason` | Clears story task from module or squad state. |
| 818 | `assign_rest` | local helper | `squad, reason` | Assigns rest and updates related ZHOPA state. |
| 830 | `sync_live_target` | local helper | `squad` | Synchronizes live target between memory, indexes, and runtime state. |
| 846 | `story_arrived` | local helper | `squad, smart` | Handles story-gated state, tasks, or diagnostic output. |
| 878 | `assign_story_target` | local helper | `squad, sid, smart, level_name, source` | Assigns story target and updates related ZHOPA state. |
| 901 | `retarget_story_task` | local helper | `squad, sid, current_target, reason` | Handles story-gated state, tasks, or diagnostic output. |
| 935 | `activate_selected_sid` | local helper | `sid, source, squad` | Internal helper for activate selected sid in the story-gated north migration event module. |
| 994 | `collect_eligible_sids` | local helper | `` | Collects eligible sids from indexed or runtime data. |
| 1017 | `maybe_fire` | local helper | `source` | Internal helper for maybe fire in the story-gated north migration event module. |
| 1062 | `reconcile_selected` | local helper | `source` | Reconciles selected after load, registration, or delayed readiness. |
| 1087 | `M.update_squad_tasks` | module export | `squad, ctx` | Updates squad tasks during the module tick or callback flow. |
| 1109 | `M.debug_status_line` | module export | `squad` | Controls debug output or debug-only state for diagnostics. |
| 1117 | `M.ensure_runtime_ready` | module export | `force_callbacks` | Internal helper for ensure runtime ready in the story-gated north migration event module. |
| 1124 | `request_reconcile` | local helper | `source` | Internal helper for request reconcile in the story-gated north migration event module. |
| 1134 | `actor_on_update` | local helper | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 1147 | `actor_on_first_update` | local helper | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 1151 | `on_game_load` | local helper | `` | Game-load callback; schedules reconciliation or clears stale runtime-only state after loading a save. |
| 1155 | `on_option_change` | local helper | `` | MCM option-change callback; invalidates cached settings and reschedules affected runtime work. |
| 1159 | `server_entity_on_unregister` | local helper | `se_obj, type_name` | Server-entity unregister callback; removes stale ids and releases runtime ownership for disappearing objects. |
| 1169 | `server_entity_on_register` | local helper | `se_obj, type_name` | Server-entity register callback; indexes or reconciles newly registered ALife objects. |
| 1180 | `squad_on_after_level_change` | local helper | `squad` | Squad level-change callback; updates level buckets and reconciles tasks affected by the transition. |
| 1188 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 1205 | `reg` | local helper | `name, fn` | Internal helper for reg in the story-gated north migration event module. |
| 1233 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_story_psy_watchdog.script`

Role: story-gated psi-level squad conversion into zombied squads.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 40 | `load_module` | local helper | `name` | Loads an optional Lua module through raw globals or guarded require. |
| 49 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 53 | `index_mod` | local helper | `` | Resolves the ZHOPA index module if it is loaded or can be required safely. |
| 57 | `perception_mod` | local helper | `` | Resolves the ZHOPA perception module if it is loaded or can be required safely. |
| 61 | `tasks_mod` | local helper | `` | Resolves the ZHOPA task module if it is loaded or can be required safely. |
| 65 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 73 | `cfg_string` | local helper | `key, default` | Reads a string ZHOPA setting with a safe default fallback. |
| 81 | `runtime_ready` | local helper | `reason` | Checks the shared ZHOPA runtime readiness barrier before running context-dependent work. |
| 93 | `debug_print_enabled` | local helper | `` | Checks whether ZHOPA debug output is enabled for this module. |
| 97 | `debug_log` | local helper | `fmt, ...` | Emits a guarded debug log line for this module. |
| 103 | `now_ms` | local helper | `` | Returns the current game or device time in milliseconds for throttling and cooldown checks. |
| 107 | `normalize_id` | local helper | `value` | Normalizes id into a stable internal representation. |
| 115 | `lower_trim` | local helper | `value` | Normalizes trim to lowercase text for comparisons. |
| 126 | `parse_csv_set` | local helper | `value` | Parses csv set from config, string, or diagnostic input. |
| 138 | `invalidate_runtime_caches` | local helper | `` | Internal helper for invalidate runtime caches in the story-gated psi-level squad conversion into zombied squads module. |
| 143 | `get_psi_levels` | local helper | `` | Returns psi levels for the current story-gated psi-level squad conversion into zombied squads state. |
| 150 | `get_immune_factions` | local helper | `` | Returns immune factions for the current story-gated psi-level squad conversion into zombied squads state. |
| 157 | `has_info` | local helper | `info` | Checks whether info is present in the story-gated psi-level squad conversion into zombied squads context. |
| 178 | `is_story_mode_active` | local helper | `` | Checks whether story mode active in the story-gated psi-level squad conversion into zombied squads context. |
| 189 | `feature_enabled_now` | local helper | `` | Internal helper for feature enabled now in the story-gated psi-level squad conversion into zombied squads module. |
| 205 | `resolve_alife_object` | local helper | `id` | Resolves alife object into a usable runtime object or value. |
| 226 | `get_board` | local helper | `` | Returns board for the current story-gated psi-level squad conversion into zombied squads state. |
| 239 | `clone_position` | local helper | `pos` | Copies position into a safe plain value. |
| 254 | `safe_position` | local helper | `obj` | Safely resolves position with nil and pcall guards. |
| 270 | `safe_name` | local helper | `obj` | Safely resolves name with nil and pcall guards. |
| 286 | `section_faction` | local helper | `section` | Internal helper for section faction in the story-gated psi-level squad conversion into zombied squads module. |
| 294 | `squad_section_name` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 315 | `squad_community` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 330 | `cfg_alias` | local helper | `value` | Reads or resolves configuration data for alias. |
| 341 | `is_immune_faction` | local helper | `community` | Checks whether immune faction in the story-gated psi-level squad conversion into zombied squads context. |
| 350 | `is_already_zombied` | local helper | `squad, community` | Checks whether already zombied in the story-gated psi-level squad conversion into zombied squads context. |
| 360 | `is_target_level` | local helper | `level_name` | Checks whether target level in the story-gated psi-level squad conversion into zombied squads context. |
| 365 | `level_name_by_gvid` | local helper | `gvid` | Resolves or validates level names, ids, or level buckets. |
| 376 | `squad_level_name` | local helper | `squad, known_level` | Handles squad lookup, state, membership, or task coordination. |
| 386 | `read_commander_id` | local helper | `squad` | Reads commander id from serialized state, config, or engine data. |
| 400 | `extract_member_candidate_id` | local helper | `k, v` | Handles squad member lookup, inventory ownership, or relation state. |
| 410 | `squad_member_ids` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 416 | `push` | local helper | `id` | Internal helper for push in the story-gated psi-level squad conversion into zombied squads module. |
| 439 | `squad_member_count` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 451 | `squad_can_manage` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 468 | `is_plain_stalker_sim_squad` | local helper | `squad` | Checks whether plain stalker sim squad in the story-gated psi-level squad conversion into zombied squads context. |
| 480 | `is_ap_owned_squad` | local helper | `squad` | Checks whether ap owned squad in the story-gated psi-level squad conversion into zombied squads context. |
| 489 | `pick_zombied_squad_section` | local helper | `source_section` | Selects zombied squad section from validated candidates. |
| 507 | `pick_zombied_member_section` | local helper | `zombied_squad_section` | Selects zombied member section from validated candidates. |
| 515 | `smart_object_by_id` | local helper | `smart_id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 531 | `smart_level_name` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 538 | `build_context` | local helper | `squad, community, level_name` | Builds context for the current story-gated psi-level squad conversion into zombied squads flow. |
| 582 | `create_empty_squad` | local helper | `section, position, lvid, gvid` | Creates empty squad for the module flow. |
| 602 | `populate_zombied_squad` | local helper | `squad, context` | Populates zombied squad with generated or indexed entries. |
| 615 | `assign_squad_to_smart` | local helper | `squad, smart_id` | Assigns squad to smart and updates related ZHOPA state. |
| 625 | `finalize_spawned_squad` | local helper | `squad, context` | Handles squad lookup, state, membership, or task coordination. |
| 661 | `cleanup_source_task` | local helper | `squad` | Cleans up source task and removes stale runtime state. |
| 674 | `unregister_released_squad` | local helper | `squad` | Unregisters released squad and cleans stale references. |
| 685 | `release_squad_safe` | local helper | `squad, reason` | Releases squad safe and removes ownership/reservation state. |
| 712 | `log_mutation_error` | local helper | `sid, context, source, reason, new_squad, extra` | Internal helper for log mutation error in the story-gated psi-level squad conversion into zombied squads module. |
| 739 | `candidate_context` | local helper | `squad, source, known_level` | Internal helper for candidate context in the story-gated psi-level squad conversion into zombied squads module. |
| 777 | `M.convert_squad_to_zombied` | module export | `squad, context, source` | Handles squad lookup, state, membership, or task coordination. |
| 855 | `M.try_process_squad` | module export | `squad, source, known_level` | Attempts process squad and returns a controlled result instead of hard-failing. |
| 863 | `M.reconcile_all_levels` | module export | `source` | Reconciles all levels after load, registration, or delayed readiness. |
| 894 | `request_reconcile` | local helper | `source` | Internal helper for request reconcile in the story-gated psi-level squad conversion into zombied squads module. |
| 903 | `actor_on_update` | local helper | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 915 | `actor_on_first_update` | local helper | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 920 | `on_game_load` | local helper | `` | Game-load callback; schedules reconciliation or clears stale runtime-only state after loading a save. |
| 925 | `on_option_change` | local helper | `` | MCM option-change callback; invalidates cached settings and reschedules affected runtime work. |
| 930 | `squad_on_after_level_change` | local helper | `squad, old_level, new_level` | Squad level-change callback; updates level buckets and reconciles tasks affected by the transition. |
| 941 | `server_entity_on_register` | local helper | `se_obj, type_name` | Server-entity register callback; indexes or reconciles newly registered ALife objects. |
| 953 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 968 | `register_callback` | local helper | `name, fn` | Registers callback in the module indexes or callbacks. |
| 994 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_tasks.script`

Role: core task FSM, weighted task registry, interrupts, completion, hunt/revenge/artifact/trade coordination.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 37 | `cfg` | local helper | `` | Internal helper for cfg in the core task FSM module. |
| 47 | `perception` | local helper | `` | Internal helper for perception in the core task FSM module. |
| 56 | `memory_mod` | local helper | `` | Resolves the ZHOPA memory module if it is loaded or can be required safely. |
| 65 | `offline_combat_mod` | local helper | `` | Internal helper for offline combat mod in the core task FSM module. |
| 74 | `loot_mod` | local helper | `` | Handles loot selection, pickup, accounting, or diagnostics in the core task FSM module. |
| 83 | `artifacts_mod` | local helper | `` | Handles artifact-related state in the core task FSM module. |
| 92 | `economy_mod` | local helper | `` | Resolves the ZHOPA economy module if it is loaded or can be required safely. |
| 101 | `index_mod` | local helper | `` | Resolves the ZHOPA index module if it is loaded or can be required safely. |
| 110 | `story_north_mod` | local helper | `` | Handles story-gated state, tasks, or diagnostic output. |
| 121 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 129 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 137 | `squad_npc_count` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 145 | `is_night_now` | local helper | `` | Checks whether night now in the core task FSM context. |
| 155 | `revenge_expired_by_night` | local helper | `` | Handles revenge targeting, hostility, or cleanup in the core task FSM module. |
| 159 | `current_hour` | local helper | `` | Internal helper for current hour in the core task FSM module. |
| 164 | `surge_active_uncached` | local helper | `` | Internal helper for surge active uncached in the core task FSM module. |
| 219 | `M.surge_active` | module export | `force_refresh` | Internal helper for surge active in the core task FSM module. |
| 229 | `mutant_time_active` | local helper | `start_hour, end_hour` | Internal helper for mutant time active in the core task FSM module. |
| 239 | `squad_section_name` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 257 | `config_faction_for_section` | local helper | `section` | Internal helper for config faction for section in the core task FSM module. |
| 265 | `mutant_behavior_id` | local helper | `squad` | Internal helper for mutant behavior id in the core task FSM module. |
| 280 | `now_ms` | assigned wrapper | `` | Returns the current game or device time in milliseconds for throttling and cooldown checks. |
| 287 | `safe_alife_object` | local helper | `id` | Returns a server object by id through guarded ALife lookups. |
| 296 | `object_id` | local helper | `obj` | Extracts a stable numeric id from a server object, online object, id-like table, number, or string. |
| 315 | `object_name` | local helper | `obj` | Returns a safe display name for an object or id. |
| 331 | `object_is_smart` | local helper | `obj` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 344 | `named_id` | local helper | `obj_or_id` | Formats an object or id as a compact diagnostic name/id string. |
| 355 | `debug_trade_log` | local helper | `squad, stage, result, detail` | Handles trade routing, trade state, or trade diagnostics in the core task FSM module. |
| 397 | `current_frame_key` | local helper | `` | Internal helper for current frame key in the core task FSM module. |
| 414 | `assignment_budget_open` | local helper | `squad` | Internal helper for assignment budget open in the core task FSM module. |
| 427 | `mark_task_no_target` | local helper | `squad, task` | Marks task no target for later processing or diagnostics. |
| 436 | `clear_task_no_target` | local helper | `squad, task` | Clears task no target from module or squad state. |
| 443 | `task_no_target_cooldown_active` | local helper | `squad, task` | Resolves, validates, or formats a task target. |
| 456 | `target_valid_cache_key` | local helper | `squad, task, target` | Resolves, validates, or formats a task target. |
| 466 | `target_valid_cache_hit` | local helper | `squad, key` | Resolves, validates, or formats a task target. |
| 473 | `target_valid_cache_store` | local helper | `squad, key` | Resolves, validates, or formats a task target. |
| 480 | `target_valid_cache_clear` | local helper | `squad` | Resolves, validates, or formats a task target. |
| 487 | `is_monster_squad` | local helper | `squad` | Checks whether monster squad in the core task FSM context. |
| 520 | `mutant_has_stalker_task` | local helper | `squad, task` | Internal helper for mutant has stalker task in the core task FSM module. |
| 524 | `make_choice` | local helper | `task, target, weight, reason, duration, patrol` | Builds choice for the current core task FSM flow. |
| 542 | `task_weight` | local helper | `key, default` | Internal helper for task weight in the core task FSM module. |
| 562 | `registry_weight_meta` | local helper | `pool, name` | Internal helper for registry weight meta in the core task FSM module. |
| 567 | `register_task` | local helper | `pool, name, builder, weight_fn` | Registers task in the module indexes or callbacks. |
| 581 | `pick_weighted` | local helper | `list` | Selects weighted from validated candidates. |
| 601 | `registry_entry_weight` | local helper | `entry, squad, context` | Internal helper for registry entry weight in the core task FSM module. |
| 622 | `pick_registry_entry` | local helper | `list, tried, squad, context` | Selects registry entry from validated candidates. |
| 637 | `update_debug` | script hook/global | `squad` | Updates debug during the module tick or callback flow. |
| 644 | `assign_rest` | local helper | `squad, reason` | Assigns rest and updates related ZHOPA state. |
| 652 | `mark_rest_trade_done` | local helper | `squad, result` | Marks rest trade done for later processing or diagnostics. |
| 662 | `mark_rest_trade_wait` | local helper | `squad, result` | Marks rest trade wait for later processing or diagnostics. |
| 671 | `rest_trade_result_is_final` | local helper | `result` | Handles trade routing, trade state, or trade diagnostics in the core task FSM module. |
| 686 | `sync_rest_trade_done_from_economy` | local helper | `squad` | Synchronizes rest trade done from economy between memory, indexes, and runtime state. |
| 703 | `rest_trade_smart_available` | local helper | `squad` | Handles trade routing, trade state, or trade diagnostics in the core task FSM module. |
| 712 | `try_auto_trade_at_rest_smart` | local helper | `squad, reason` | Attempts auto trade at rest smart and returns a controlled result instead of hard-failing. |
| 724 | `tick_rest_auto_trade` | local helper | `squad` | Runs one bounded tick of rest auto trade. |
| 764 | `rest_trade_blocks_completion` | local helper | `squad` | Handles trade routing, trade state, or trade diagnostics in the core task FSM module. |
| 786 | `try_after_night_rest_auto_trade` | local helper | `squad` | Attempts after night rest auto trade and returns a controlled result instead of hard-failing. |
| 818 | `tick_base_camping_auto_trade` | local helper | `squad` | Runs one bounded tick of base camping auto trade. |
| 847 | `trade_route_allowed_from_context` | local helper | `context` | Handles trade routing, trade state, or trade diagnostics in the core task FSM module. |
| 852 | `trade_route_task_weight` | local helper | `squad, context, base_weight` | Handles trade routing, trade state, or trade diagnostics in the core task FSM module. |
| 867 | `trade_route_result_waiting` | local helper | `result` | Handles trade routing, trade state, or trade diagnostics in the core task FSM module. |
| 875 | `mark_trade_route_wait` | local helper | `squad, result` | Marks trade route wait for later processing or diagnostics. |
| 884 | `complete_trade_route` | local helper | `squad, result` | Completes trade route and applies the related consequence/fallback. |
| 896 | `sync_trade_route_done_from_economy` | local helper | `squad` | Synchronizes trade route done from economy between memory, indexes, and runtime state. |
| 904 | `tick_trade_route` | local helper | `squad` | Runs one bounded tick of trade route. |
| 931 | `final_smart` | local helper | `p, squad, smart, opts` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 938 | `force_exit_target` | local helper | `squad` | Resolves, validates, or formats a task target. |
| 977 | `target_blacklisted_for_squad` | local helper | `squad, target_id` | Handles squad lookup, state, membership, or task coordination. |
| 994 | `task_target_blacklisted` | local helper | `squad` | Checks or applies blacklist rules for target selection and task safety. |
| 1001 | `build_stalker_explore` | local helper | `squad` | Builds stalker explore for the current core task FSM flow. |
| 1013 | `build_stalker_populate` | local helper | `squad` | Builds stalker populate for the current core task FSM flow. |
| 1044 | `build_stalker_patrol` | local helper | `squad` | Builds stalker patrol for the current core task FSM flow. |
| 1057 | `build_stalker_hunt` | local helper | `squad` | Builds stalker hunt for the current core task FSM flow. |
| 1074 | `build_stalker_artefact` | local helper | `squad` | Builds stalker artefact for the current core task FSM flow. |
| 1096 | `build_stalker_trade` | local helper | `squad, context` | Builds stalker trade for the current core task FSM flow. |
| 1115 | `build_mutant_hunt` | local helper | `squad` | Builds mutant hunt for the current core task FSM flow. |
| 1132 | `build_mutant_patrol` | local helper | `squad` | Builds mutant patrol for the current core task FSM flow. |
| 1145 | `build_mutant_explore` | local helper | `squad` | Builds mutant explore for the current core task FSM flow. |
| 1166 | `select_from_registry` | local helper | `pool, squad, context` | Selects from registry from weighted or prioritized candidates. |
| 1186 | `select_stalker_task` | local helper | `squad, reason` | Selects stalker task from weighted or prioritized candidates. |
| 1204 | `select_stalker_night_rest` | script hook/global | `squad` | Selects stalker night rest from weighted or prioritized candidates. |
| 1244 | `select_mutant_task` | local helper | `squad, reason` | Selects mutant task from weighted or prioritized candidates. |
| 1261 | `mutant_night_hunt_only` | local helper | `squad` | Handles hunt target validation, combat consequences, or pursuit state. |
| 1266 | `night_rest_target_unsafe` | local helper | `squad` | Resolves, validates, or formats a task target. |
| 1277 | `assign_choice` | local helper | `squad, choice, fallback_reason` | Assigns choice and updates related ZHOPA state. |
| 1318 | `assign_stalker_hunt_or_rest` | local helper | `squad, reason` | Assigns stalker hunt or rest and updates related ZHOPA state. |
| 1326 | `repair_invalid_mutant_task` | local helper | `squad` | Repairs invalid mutant task when runtime state becomes stale or inconsistent. |
| 1342 | `mutant_time_inactive` | local helper | `squad` | Internal helper for mutant time inactive in the core task FSM module. |
| 1355 | `clear_zhopa2_movement_target` | local helper | `squad, clear_any` | Clears movement target from module or squad state. |
| 1382 | `pause_for_surge` | local helper | `squad` | Internal helper for pause for surge in the core task FSM module. |
| 1413 | `park_inactive_mutant` | local helper | `squad` | Internal helper for park inactive mutant in the core task FSM module. |
| 1437 | `M.interrupt_task` | module export | `squad, task, target_id, duration_sec, reason, patrol, opts` | Internal helper for interrupt task in the core task FSM module. |
| 1478 | `M.assign_revenge_interrupt` | module export | `responder, offender_target_id` | Assigns revenge interrupt and updates related ZHOPA state. |
| 1488 | `M.assign_base_camping_permanent` | module export | `squad, smart, reason` | Assigns base camping permanent and updates related ZHOPA state. |
| 1513 | `hunt_prey_for` | local helper | `squad` | Handles hunt target validation, combat consequences, or pursuit state. |
| 1517 | `actor_target_alive` | local helper | `` | Resolves, validates, or formats a task target. |
| 1535 | `game_vertex_level_id` | local helper | `obj` | Resolves or validates level names, ids, or level buckets. |
| 1543 | `squad_community` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 1560 | `same_smart_or_close` | local helper | `squad, target` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 1574 | `artefact_offline_collect_ready` | local helper | `squad` | Handles artifact-related state in the core task FSM module. |
| 1591 | `factions_hostile` | local helper | `community_1, community_2` | Internal helper for factions hostile in the core task FSM module. |
| 1599 | `member_server_object` | local helper | `member` | Handles squad member lookup, inventory ownership, or relation state. |
| 1606 | `member_online_object` | local helper | `member` | Handles squad member lookup, inventory ownership, or relation state. |
| 1618 | `is_inventory_owner_object` | local helper | `obj` | Checks whether inventory owner object in the core task FSM context. |
| 1633 | `member_inventory_owner_server_object` | local helper | `member` | Handles squad member lookup, inventory ownership, or relation state. |
| 1638 | `inventory_owner_target` | local helper | `target` | Scans, classifies, or mutates NPC/server inventory state. |
| 1648 | `force_goodwill` | local helper | `source, goodwill, target` | Internal helper for force goodwill in the core task FSM module. |
| 1661 | `is_online_relation_stalker` | local helper | `obj` | Checks whether online relation stalker in the core task FSM context. |
| 1672 | `online_relation_matches` | local helper | `source, target, relation` | Internal helper for online relation matches in the core task FSM module. |
| 1679 | `set_online_relation` | local helper | `source, target, relation, goodwill` | Sets online relation for the current core task FSM state. |
| 1696 | `force_member_to_actor` | local helper | `member` | Handles squad member lookup, inventory ownership, or relation state. |
| 1706 | `force_member_to_member` | local helper | `member_1, member_2, goodwill` | Handles squad member lookup, inventory ownership, or relation state. |
| 1729 | `actor_on_squad_level` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 1739 | `current_actor_id` | local helper | `` | Internal helper for current actor id in the core task FSM module. |
| 1750 | `current_actor_level_name` | local helper | `` | Resolves or validates level names, ids, or level buckets. |
| 1767 | `actor_community_goodwill` | local helper | `community` | Internal helper for actor community goodwill in the core task FSM module. |
| 1775 | `set_actor_community_goodwill` | local helper | `community, goodwill` | Sets actor community goodwill for the current core task FSM state. |
| 1783 | `online_actor_goodwill` | local helper | `obj` | Internal helper for online actor goodwill in the core task FSM module. |
| 1800 | `restore_member_actor_goodwill` | local helper | `member_id, goodwill` | Handles squad member lookup, inventory ownership, or relation state. |
| 1812 | `squad_member_id_set` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 1826 | `snapshot_member_actor_goodwill` | local helper | `member, bucket` | Handles squad member lookup, inventory ownership, or relation state. |
| 1839 | `for_each_actor_level_squad` | local helper | `fn` | Handles squad lookup, state, membership, or task coordination. |
| 1876 | `snapshot_actor_revenge_relation_scope` | local helper | `squad, scope` | Handles revenge targeting, hostility, or cleanup in the core task FSM module. |
| 1911 | `ensure_actor_revenge_relation_scope` | local helper | `squad` | Handles revenge targeting, hostility, or cleanup in the core task FSM module. |
| 1939 | `stored_actor_revenge_relation_scope` | local helper | `squad` | Handles revenge targeting, hostility, or cleanup in the core task FSM module. |
| 1965 | `restore_actor_revenge_relation_scope` | local helper | `squad, force, include_revenge` | Handles revenge targeting, hostility, or cleanup in the core task FSM module. |
| 1989 | `clear_actor_revenge_relation_scope` | local helper | `squad` | Clears actor revenge relation scope from module or squad state. |
| 2000 | `same_level_for_hostility` | local helper | `squad, target` | Resolves or validates level names, ids, or level buckets. |
| 2008 | `M.apply_revenge_hostility` | module export | `squad` | Handles revenge targeting, hostility, or cleanup in the core task FSM module. |
| 2054 | `M.release_revenge_hostility` | module export | `squad` | Releases revenge hostility and removes ownership/reservation state. |
| 2068 | `record_offline_combat_loot` | local helper | `squad, target, target_count_before, reason` | Handles loot selection, pickup, accounting, or diagnostics in the core task FSM module. |
| 2081 | `M.hunt_offline_tick` | module export | `squad, target, opts` | Handles hunt target validation, combat consequences, or pursuit state. |
| 2127 | `M.hunt_target_valid` | module export | `squad` | Handles hunt target validation, combat consequences, or pursuit state. |
| 2159 | `revenge_wait_route` | local helper | `squad, reason` | Handles revenge targeting, hostility, or cleanup in the core task FSM module. |
| 2167 | `M.revenge_target_valid` | module export | `squad` | Handles revenge targeting, hostility, or cleanup in the core task FSM module. |
| 2217 | `abort_hunt` | local helper | `squad, reason` | Aborts hunt through a controlled failure path. |
| 2228 | `complete_hunt` | local helper | `squad, mem, target_id, reason` | Completes hunt and applies the related consequence/fallback. |
| 2245 | `complete_revenge` | local helper | `squad, mem, target_id, reason` | Completes revenge and applies the related consequence/fallback. |
| 2259 | `complete_populate` | local helper | `squad, target_id` | Completes populate and applies the related consequence/fallback. |
| 2271 | `complete_artefact` | local helper | `squad, reason` | Completes artefact and applies the related consequence/fallback. |
| 2282 | `M.cancel_revenge` | module export | `squad, reason` | Cancels revenge and clears or releases related state. |
| 2291 | `M.release_artifact_task` | module export | `squad, reason` | Releases artifact task and removes ownership/reservation state. |
| 2313 | `M.assign_next_task` | module export | `squad, reason` | Assigns next task and updates related ZHOPA state. |
| 2335 | `M.update_squad` | module export | `squad, memory` | Updates squad during the module tick or callback flow. |
| 2571 | `revenge_script_target_fallback` | local helper | `squad, route_reason` | Handles revenge targeting, hostility, or cleanup in the core task FSM module. |
| 2578 | `M.get_script_target` | module export | `squad` | Returns script target for the current core task FSM state. |

### `projects/zhopa_alife_2/gamedata/scripts/zhopa2_topology.script`

Role: level topology, level-changer indexing, and neighbor cache.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 12 | `level_from_object` | local helper | `obj` | Resolves or validates level names, ids, or level buckets. |
| 27 | `append_edge` | local helper | `map, source_level, dest_level` | Internal helper for append edge in the level topology module. |
| 43 | `edge_sets_to_arrays` | local helper | `src` | Internal helper for edge sets to arrays in the level topology module. |
| 62 | `rebuild_neighbors` | local helper | `` | Internal helper for rebuild neighbors in the level topology module. |
| 76 | `get_utils_stpk` | local helper | `` | Returns utils stpk for the current level topology state. |
| 90 | `get_level_changer_data` | local helper | `se_obj` | Returns level changer data for the current level topology state. |
| 101 | `is_level_changer` | local helper | `se_obj, type_name` | Checks whether level changer in the level topology context. |
| 116 | `remove_level_changer` | local helper | `se_obj` | Resolves or validates level names, ids, or level buckets. |
| 145 | `set_level_changer` | local helper | `se_obj` | Sets level changer for the current level topology state. |
| 171 | `server_entity_on_register` | local helper | `se_obj, type_name` | Server-entity register callback; indexes or reconciles newly registered ALife objects. |
| 177 | `server_entity_on_unregister` | local helper | `se_obj, type_name` | Server-entity unregister callback; removes stale ids and releases runtime ownership for disappearing objects. |
| 183 | `M.get_level_neighbors` | module export | `level_name` | Returns level neighbors for the current level topology state. |
| 190 | `M.get_revision` | module export | `` | Returns revision for the current level topology state. |
| 194 | `M.set_level_changer` | module export | `se_obj` | Sets level changer for the current level topology state. |
| 198 | `M.remove_level_changer` | module export | `se_obj` | Resolves or validates level names, ids, or level buckets. |
| 202 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 214 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

## Diagnostic Scripts

### `projects/zhopa_alife_2/debugscripts/zhopa2_artifact_diag.script`

Role: artifact registry and anomaly-zone diagnostic dump.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 6 | `debug_print_enabled` | local helper | `` | Checks whether ZHOPA debug output is enabled for this module. |
| 15 | `log` | local helper | `fmt, ...` | Emits a formatted diagnostic log line for the script. |
| 26 | `safe_call` | local helper | `obj, fn_name, ...` | Calls an object method through pcall and returns nil-safe results. |
| 40 | `safe_field` | local helper | `obj, field` | Reads an object field through pcall and returns nil on failure. |
| 53 | `object_id` | local helper | `obj` | Extracts a stable numeric id from a server object, online object, id-like table, number, or string. |
| 64 | `object_name` | local helper | `obj` | Returns a safe display name for an object or id. |
| 75 | `object_section` | local helper | `obj` | Returns a safe section name for an object. |
| 94 | `named_id` | local helper | `obj_or_id` | Formats an object or id as a compact diagnostic name/id string. |
| 109 | `table_count` | local helper | `t` | Counts keys in a Lua table without assuming array layout. |
| 117 | `sorted_keys` | local helper | `t` | Returns table keys in a deterministic sorted order for stable diagnostics. |
| 128 | `obj_level` | local helper | `obj` | Resolves or validates level names, ids, or level buckets. |
| 144 | `current_level_name` | local helper | `` | Resolves or validates level names, ids, or level buckets. |
| 154 | `object_position` | local helper | `obj` | Diagnostic helper for object position in the artifact registry and anomaly-zone diagnostic dump script. |
| 184 | `pos_text` | local helper | `pos` | Diagnostic helper for pos text in the artifact registry and anomaly-zone diagnostic dump script. |
| 191 | `distance_sqr` | local helper | `a, b` | Diagnostic helper for distance sqr in the artifact registry and anomaly-zone diagnostic dump script. |
| 203 | `dump_artifact_candidate_smarts` | local helper | `idx, artifact_id, art` | Prints a diagnostic dump of artifact candidate smarts. |
| 246 | `artifact_valid` | local helper | `idx, artifact_id` | Handles artifact-related state in the artifact registry and anomaly-zone diagnostic dump module. |
| 257 | `dump_storage` | local helper | `` | Prints a diagnostic dump of storage. |
| 281 | `dump_virtual_zones` | local helper | `idx` | Prints a diagnostic dump of virtual zones. |
| 315 | `dump_artifacts` | local helper | `idx` | Prints a diagnostic dump of artifacts. |
| 359 | `dump_simboard_tasks` | local helper | `idx` | Prints a diagnostic dump of simboard tasks. |
| 389 | `M.dump` | module export | `` | Diagnostic helper for dump in the artifact registry and anomaly-zone diagnostic dump script. |
| 407 | `M.actor_on_first_update` | module export | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 415 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 425 | `actor_on_first_update` | script hook/global | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 429 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/debugscripts/zhopa2_artifact_flow_diag.script`

Role: artifact task/flow diagnostic wrappers and trace output.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 20 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 29 | `debug_print_enabled` | local helper | `` | Checks whether ZHOPA debug output is enabled for this module. |
| 34 | `log` | local helper | `fmt, ...` | Emits a formatted diagnostic log line for the script. |
| 45 | `tg` | local helper | `` | Returns the current time value used by throttled diagnostics. |
| 49 | `safe_require` | local helper | `name` | Safely resolves require with nil and pcall guards. |
| 62 | `safe_field` | local helper | `obj, field` | Reads an object field through pcall and returns nil on failure. |
| 72 | `safe_call` | local helper | `obj, fn_name, ...` | Calls an object method through pcall and returns nil-safe results. |
| 81 | `safe_alife_object` | local helper | `id` | Returns a server object by id through guarded ALife lookups. |
| 90 | `online_object_by_id` | local helper | `id` | Returns an online game object by id through db.storage/level lookups. |
| 106 | `object_id` | local helper | `obj` | Extracts a stable numeric id from a server object, online object, id-like table, number, or string. |
| 127 | `object_name` | local helper | `obj` | Returns a safe display name for an object or id. |
| 143 | `object_section` | local helper | `obj` | Returns a safe section name for an object. |
| 166 | `object_level` | local helper | `obj` | Resolves or validates level names, ids, or level buckets. |
| 200 | `object_parent_id` | local helper | `obj` | Diagnostic helper for object parent id in the artifact task/flow diagnostic wrappers and trace output script. |
| 211 | `named_id` | local helper | `obj_or_id` | Formats an object or id as a compact diagnostic name/id string. |
| 221 | `bool_text` | local helper | `value` | Diagnostic helper for bool text in the artifact task/flow diagnostic wrappers and trace output script. |
| 225 | `table_count` | local helper | `t` | Counts keys in a Lua table without assuming array layout. |
| 233 | `sorted_keys` | local helper | `t` | Returns table keys in a deterministic sorted order for stable diagnostics. |
| 244 | `vector_text` | local helper | `pos` | Diagnostic helper for vector text in the artifact task/flow diagnostic wrappers and trace output script. |
| 257 | `object_position` | local helper | `obj` | Diagnostic helper for object position in the artifact task/flow diagnostic wrappers and trace output script. |
| 272 | `idx_mod` | local helper | `` | Diagnostic helper for idx mod in the artifact task/flow diagnostic wrappers and trace output script. |
| 276 | `artifacts_mod` | local helper | `` | Handles artifact-related state in the artifact task/flow diagnostic wrappers and trace output module. |
| 280 | `loot_mod` | local helper | `` | Handles loot selection, pickup, accounting, or diagnostics in the artifact task/flow diagnostic wrappers and trace output module. |
| 284 | `gather_mod` | local helper | `` | Diagnostic helper for gather mod in the artifact task/flow diagnostic wrappers and trace output script. |
| 288 | `artifact_bucket_memberships` | local helper | `idx, artifact_id` | Handles artifact-related state in the artifact task/flow diagnostic wrappers and trace output module. |
| 300 | `artifact_pos` | local helper | `artifact_id` | Handles artifact-related state in the artifact task/flow diagnostic wrappers and trace output module. |
| 306 | `smart_pos` | local helper | `smart_id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 312 | `squad_pos` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 316 | `artifact_bucket_match` | local helper | `idx, artifact_id` | Handles artifact-related state in the artifact task/flow diagnostic wrappers and trace output module. |
| 326 | `artifact_state` | local helper | `artifact_id` | Handles artifact-related state in the artifact task/flow diagnostic wrappers and trace output module. |
| 353 | `smart_state` | local helper | `smart_id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 368 | `squad_state` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 388 | `looter_squad` | local helper | `npc` | Handles loot selection, pickup, accounting, or diagnostics in the artifact task/flow diagnostic wrappers and trace output module. |
| 403 | `gather_state` | local helper | `npc` | Reads, writes, or repairs runtime state. |
| 425 | `storage_gather_state` | local helper | `npc` | Reads, writes, or repairs runtime state. |
| 430 | `state_mgr_text` | local helper | `npc` | Reads, writes, or repairs runtime state. |
| 438 | `npc_position` | local helper | `npc` | Diagnostic helper for npc position in the artifact task/flow diagnostic wrappers and trace output script. |
| 446 | `online_item_pos` | local helper | `item_id` | Diagnostic helper for online item pos in the artifact task/flow diagnostic wrappers and trace output script. |
| 451 | `distance_text` | local helper | `pos_a, pos_b` | Diagnostic helper for distance text in the artifact task/flow diagnostic wrappers and trace output script. |
| 459 | `route_summary` | local helper | `squad, npc, task_smart_id, artifact_id` | Builds, validates, or diagnoses a route. |
| 490 | `vertex_state` | local helper | `npc, vid` | Reads, writes, or repairs runtime state. |
| 504 | `gather_detail` | local helper | `npc, item_id, st` | Diagnostic helper for gather detail in the artifact task/flow diagnostic wrappers and trace output script. |
| 519 | `should_log_gather_execute` | local helper | `npc, st, item_id` | Decides whether log gather execute should run for the current artifact task/flow diagnostic wrappers and trace output state. |
| 533 | `patch_table_method` | local helper | `tbl, method, tag, wrapper` | Installs or maintains the chain-friendly patch for table method. |
| 557 | `patch_global_function` | local helper | `name, wrapper` | Installs or maintains the chain-friendly patch for global function. |
| 579 | `patch_exported_function` | local helper | `name, tag, wrapper` | Installs or maintains the chain-friendly patch for exported function. |
| 601 | `patch_index` | local helper | `` | Installs or maintains the chain-friendly patch for index. |
| 639 | `patch_artifacts` | local helper | `` | Installs or maintains the chain-friendly patch for artifacts. |
| 678 | `patch_loot` | local helper | `` | Installs or maintains the chain-friendly patch for loot. |
| 710 | `patch_force_gather` | local helper | `` | Installs or maintains the chain-friendly patch for force gather. |
| 742 | `patch_prepare_gather` | local helper | `` | Installs or maintains the chain-friendly patch for prepare gather. |
| 768 | `patch_gather_item` | local helper | `` | Installs or maintains the chain-friendly patch for gather item. |
| 794 | `patch_gather_find` | local helper | `` | Installs or maintains the chain-friendly patch for gather find. |
| 833 | `patch_gather_evaluate` | local helper | `` | Installs or maintains the chain-friendly patch for gather evaluate. |
| 859 | `patch_gather_action` | local helper | `` | Installs or maintains the chain-friendly patch for gather action. |
| 934 | `M.dump_all` | module export | `reason` | Prints a diagnostic dump of all. |
| 981 | `M.install` | module export | `source` | Diagnostic helper for install in the artifact task/flow diagnostic wrappers and trace output script. |
| 1016 | `unregister_update` | local helper | `` | Unregisters update and cleans stale references. |
| 1022 | `M.actor_on_update` | module export | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 1043 | `M.actor_on_first_update` | module export | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 1059 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 1076 | `actor_on_first_update` | script hook/global | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 1080 | `actor_on_update` | script hook/global | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 1084 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/debugscripts/zhopa2_bucket_diag.script`

Role: runtime bucket diagnostic dump for index contents.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 16 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 25 | `debug_print_enabled` | local helper | `` | Checks whether ZHOPA debug output is enabled for this module. |
| 30 | `log` | local helper | `fmt, ...` | Emits a formatted diagnostic log line for the script. |
| 41 | `safe_field` | local helper | `obj, field` | Reads an object field through pcall and returns nil on failure. |
| 51 | `safe_call` | local helper | `obj, fn_name, ...` | Calls an object method through pcall and returns nil-safe results. |
| 60 | `safe_alife_object` | local helper | `id` | Returns a server object by id through guarded ALife lookups. |
| 69 | `field_value` | local helper | `obj, field` | Diagnostic helper for field value in the runtime bucket diagnostic dump for index contents script. |
| 81 | `object_id` | local helper | `obj` | Extracts a stable numeric id from a server object, online object, id-like table, number, or string. |
| 102 | `object_name` | local helper | `obj` | Returns a safe display name for an object or id. |
| 131 | `named_id` | local helper | `obj_or_id` | Formats an object or id as a compact diagnostic name/id string. |
| 144 | `table_count` | local helper | `t` | Counts keys in a Lua table without assuming array layout. |
| 155 | `sorted_keys` | local helper | `t` | Returns table keys in a deterministic sorted order for stable diagnostics. |
| 174 | `bucket_stats` | local helper | `bucket` | Diagnostic helper for bucket stats in the runtime bucket diagnostic dump for index contents script. |
| 187 | `kind_bucket_stats` | local helper | `kind_bucket` | Diagnostic helper for kind bucket stats in the runtime bucket diagnostic dump for index contents script. |
| 204 | `smart_from_board` | local helper | `board, id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 212 | `squad_from_board` | local helper | `board, id, stored` | Handles squad lookup, state, membership, or task coordination. |
| 223 | `level_name_for_obj` | local helper | `obj` | Resolves or validates level names, ids, or level buckets. |
| 251 | `bool_text` | local helper | `value` | Diagnostic helper for bool text in the runtime bucket diagnostic dump for index contents script. |
| 255 | `flags_text` | local helper | `flags` | Diagnostic helper for flags text in the runtime bucket diagnostic dump for index contents script. |
| 271 | `online_object_by_id` | local helper | `id` | Returns an online game object by id through db.storage/level lookups. |
| 289 | `storage_by_id` | local helper | `id` | Diagnostic helper for storage by id in the runtime bucket diagnostic dump for index contents script. |
| 294 | `current_action_id` | local helper | `npc` | Diagnostic helper for current action id in the runtime bucket diagnostic dump for index contents script. |
| 306 | `current_state` | local helper | `npc` | Reads, writes, or repairs runtime state. |
| 314 | `current_point_index` | local helper | `npc` | Diagnostic helper for current point index in the runtime bucket diagnostic dump for index contents script. |
| 322 | `path_index` | local helper | `npc` | Diagnostic helper for path index in the runtime bucket diagnostic dump for index contents script. |
| 330 | `trade_slot_for_npc` | local helper | `smart, npc_id` | Handles trade routing, trade state, or trade diagnostics in the runtime bucket diagnostic dump for index contents module. |
| 350 | `binding_state` | local helper | `` | Reads, writes, or repairs runtime state. |
| 370 | `dump_level_bucket` | local helper | `name, bucket, resolver, level_map` | Prints a diagnostic dump of level bucket. |
| 408 | `economy_mod` | local helper | `` | Resolves the ZHOPA economy module if it is loaded or can be required safely. |
| 417 | `smart_id_for_squad` | local helper | `squad` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 421 | `target_id_for_squad` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 428 | `current_smart_for_squad` | local helper | `board, squad` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 436 | `trade_flags_for_smart` | local helper | `board, smart_id` | Handles trade routing, trade state, or trade diagnostics in the runtime bucket diagnostic dump for index contents module. |
| 443 | `trade_state_relevant` | local helper | `squad` | Handles trade routing, trade state, or trade diagnostics in the runtime bucket diagnostic dump for index contents module. |
| 453 | `pcall_profile` | local helper | `fn, ...` | Diagnostic helper for pcall profile in the runtime bucket diagnostic dump for index contents script. |
| 464 | `online_member_count` | local helper | `economy, squad` | Handles squad member lookup, inventory ownership, or relation state. |
| 475 | `dump_trade_squad_candidates` | local helper | `board` | Prints a diagnostic dump of trade squad candidates. |
| 566 | `dump_prepared_trade_squads` | local helper | `board` | Prints a diagnostic dump of prepared trade squads. |
| 640 | `dump_kind_bucket` | local helper | `board` | Prints a diagnostic dump of kind bucket. |
| 669 | `dump_trade_flags` | local helper | `board` | Prints a diagnostic dump of trade flags. |
| 716 | `dump_board_consistency` | local helper | `board` | Prints a diagnostic dump of board consistency. |
| 760 | `dump_index_summary` | local helper | `` | Prints a diagnostic dump of index summary. |
| 793 | `dump_index_buckets` | local helper | `` | Prints a diagnostic dump of index buckets. |
| 820 | `M.refresh_simboard_buckets` | module export | `` | Refreshes simboard buckets from current runtime or indexed data. |
| 829 | `M.refresh_trade_buckets` | module export | `` | Refreshes trade buckets from current runtime or indexed data. |
| 845 | `M.dump` | module export | `reason` | Diagnostic helper for dump in the runtime bucket diagnostic dump for index contents script. |
| 903 | `M.refresh_and_dump` | module export | `` | Refreshes and dump from current runtime or indexed data. |
| 910 | `now_ms` | local helper | `` | Returns the current game or device time in milliseconds for throttling and cooldown checks. |
| 914 | `M.actor_on_update` | module export | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 936 | `M.actor_on_first_update` | module export | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 953 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 963 | `actor_on_first_update` | script hook/global | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 967 | `actor_on_update` | script hook/global | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 971 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/debugscripts/zhopa2_loot_loop_diag.script`

Role: loot loop diagnostics and corpse/item memory tracing.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 29 | `safe_mod` | local helper | `name` | Resolves an optional module without crashing when it is absent. |
| 38 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 42 | `debug_print_enabled` | local helper | `` | Checks whether ZHOPA debug output is enabled for this module. |
| 47 | `log` | local helper | `fmt, ...` | Emits a formatted diagnostic log line for the script. |
| 62 | `tg` | local helper | `` | Returns the current time value used by throttled diagnostics. |
| 66 | `safe_field` | local helper | `obj, field` | Reads an object field through pcall and returns nil on failure. |
| 76 | `safe_call` | local helper | `obj, fn_name, ...` | Calls an object method through pcall and returns nil-safe results. |
| 88 | `object_id` | local helper | `obj` | Extracts a stable numeric id from a server object, online object, id-like table, number, or string. |
| 103 | `object_name` | local helper | `obj` | Returns a safe display name for an object or id. |
| 119 | `object_section` | local helper | `obj` | Returns a safe section name for an object. |
| 139 | `safe_alife_object` | local helper | `id` | Returns a server object by id through guarded ALife lookups. |
| 148 | `online_object_by_id` | local helper | `id` | Returns an online game object by id through db.storage/level lookups. |
| 166 | `named_id` | local helper | `obj_or_id` | Formats an object or id as a compact diagnostic name/id string. |
| 176 | `boolstr` | local helper | `value` | Diagnostic helper for boolstr in the loot loop diagnostics and corpse/item memory tracing script. |
| 185 | `safe_bool` | local helper | `fn, ...` | Safely resolves bool with nil and pcall guards. |
| 193 | `dist_to_actor` | local helper | `obj` | Diagnostic helper for dist to actor in the loot loop diagnostics and corpse/item memory tracing script. |
| 206 | `object_alive` | local helper | `obj` | Diagnostic helper for object alive in the loot loop diagnostics and corpse/item memory tracing script. |
| 211 | `is_stalker` | local helper | `obj` | Checks whether stalker in the loot loop diagnostics and corpse/item memory tracing context. |
| 219 | `is_monster` | local helper | `obj` | Checks whether monster in the loot loop diagnostics and corpse/item memory tracing context. |
| 227 | `table_count` | local helper | `t` | Counts keys in a Lua table without assuming array layout. |
| 238 | `list_has` | local helper | `list, id` | Diagnostic helper for list has in the loot loop diagnostics and corpse/item memory tracing script. |
| 251 | `append_unique` | local helper | `list, seen, id` | Diagnostic helper for append unique in the loot loop diagnostics and corpse/item memory tracing script. |
| 260 | `short_ids` | local helper | `memory` | Diagnostic helper for short ids in the loot loop diagnostics and corpse/item memory tracing script. |
| 281 | `root_storage` | local helper | `id` | Diagnostic helper for root storage in the loot loop diagnostics and corpse/item memory tracing script. |
| 286 | `corpse_storage_state` | local helper | `corpse_id` | Handles corpse target filtering, looting, or loop prevention. |
| 291 | `corpse_detection_state` | local helper | `npc` | Handles corpse target filtering, looting, or loop prevention. |
| 296 | `vanilla_has_valuable` | local helper | `corpse_id` | Diagnostic helper for vanilla has valuable in the loot loop diagnostics and corpse/item memory tracing script. |
| 306 | `vanilla_lootable` | local helper | `section` | Handles loot selection, pickup, accounting, or diagnostics in the loot loop diagnostics and corpse/item memory tracing module. |
| 312 | `zhopa_corpse_ignored` | local helper | `corpse_id` | Handles corpse target filtering, looting, or loop prevention. |
| 321 | `zhopa_can_take` | local helper | `section, item, looter` | Diagnostic helper for zhopa can take in the loot loop diagnostics and corpse/item memory tracing script. |
| 330 | `zhopa_protected_corpse` | local helper | `corpse, corpse_id` | Handles corpse target filtering, looting, or loop prevention. |
| 339 | `section_is_quest` | local helper | `section` | Diagnostic helper for section is quest in the loot loop diagnostics and corpse/item memory tracing script. |
| 347 | `object_is_story` | local helper | `obj` | Handles story-gated state, tasks, or diagnostic output. |
| 356 | `recent_corpse_ids` | local helper | `` | Handles corpse target filtering, looting, or loop prevention. |
| 365 | `looter_sample_for_corpse` | local helper | `corpse_id` | Handles loot selection, pickup, accounting, or diagnostics in the loot loop diagnostics and corpse/item memory tracing module. |
| 384 | `corpse_inventory_signature` | local helper | `corpse, looter` | Scans, classifies, or mutates NPC/server inventory state. |
| 395 | `inspect_item` | local helper | `owner, item` | Diagnostic helper for inspect item in the loot loop diagnostics and corpse/item memory tracing script. |
| 441 | `should_log_sig` | local helper | `kind, key, sig, force` | Decides whether log sig should run for the current loot loop diagnostics and corpse/item memory tracing state. |
| 453 | `dump_corpse` | local helper | `corpse_id, reason, looter, force` | Prints a diagnostic dump of corpse. |
| 500 | `dump_npc` | local helper | `npc, reason, force, out_corpses, seen_corpses` | Prints a diagnostic dump of npc. |
| 553 | `dump_runtime` | local helper | `reason` | Prints a diagnostic dump of runtime. |
| 572 | `M.dump` | module export | `reason, force` | Diagnostic helper for dump in the loot loop diagnostics and corpse/item memory tracing script. |
| 609 | `patch_function` | local helper | `mod, fn_name, patch_id, wrapper_factory` | Installs or maintains the chain-friendly patch for function. |
| 623 | `M.install` | module export | `` | Diagnostic helper for install in the loot loop diagnostics and corpse/item memory tracing script. |
| 672 | `M.start_watch` | module export | `duration_ms` | Diagnostic helper for start watch in the loot loop diagnostics and corpse/item memory tracing script. |
| 680 | `M.stop_watch` | module export | `` | Diagnostic helper for stop watch in the loot loop diagnostics and corpse/item memory tracing script. |
| 686 | `M.actor_on_update` | module export | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 705 | `M.actor_on_first_update` | module export | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 725 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 735 | `actor_on_update` | script hook/global | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 739 | `actor_on_first_update` | script hook/global | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 743 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/debugscripts/zhopa2_mutant_diag.script`

Role: mutant task and blacklist diagnostic dump.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 17 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 26 | `debug_print_enabled` | local helper | `` | Checks whether ZHOPA debug output is enabled for this module. |
| 31 | `log` | local helper | `fmt, ...` | Emits a formatted diagnostic log line for the script. |
| 42 | `safe_field` | local helper | `obj, field` | Reads an object field through pcall and returns nil on failure. |
| 52 | `safe_call` | local helper | `obj, fn_name, ...` | Calls an object method through pcall and returns nil-safe results. |
| 64 | `safe_mod` | local helper | `name` | Resolves an optional module without crashing when it is absent. |
| 73 | `safe_alife_object` | local helper | `id` | Returns a server object by id through guarded ALife lookups. |
| 82 | `object_id` | local helper | `obj` | Extracts a stable numeric id from a server object, online object, id-like table, number, or string. |
| 97 | `object_name` | local helper | `obj` | Returns a safe display name for an object or id. |
| 117 | `named_id` | local helper | `obj_or_id` | Formats an object or id as a compact diagnostic name/id string. |
| 123 | `table_count` | local helper | `t` | Counts keys in a Lua table without assuming array layout. |
| 133 | `sorted_keys` | local helper | `t` | Returns table keys in a deterministic sorted order for stable diagnostics. |
| 144 | `join_ids` | local helper | `list, limit` | Joins ids into a compact diagnostic string. |
| 156 | `prop_num` | local helper | `props, key` | Diagnostic helper for prop num in the mutant task and blacklist diagnostic dump script. |
| 160 | `smart_mutant_props` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 168 | `smart_flags` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 182 | `obj_level` | local helper | `obj` | Resolves or validates level names, ids, or level buckets. |
| 200 | `squad_section_name` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 209 | `squad_player_id` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 220 | `squad_relation_faction` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 231 | `is_monster_squad` | local helper | `squad` | Checks whether monster squad in the mutant task and blacklist diagnostic dump context. |
| 252 | `mutation_time_state` | local helper | `player_id` | Reads, writes, or repairs runtime state. |
| 262 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 273 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 284 | `runtime_ready_state` | local helper | `context` | Reads, writes, or repairs runtime state. |
| 304 | `log_runtime` | local helper | `` | Diagnostic helper for log runtime in the mutant task and blacklist diagnostic dump script. |
| 319 | `log_cfg` | local helper | `` | Diagnostic helper for log cfg in the mutant task and blacklist diagnostic dump script. |
| 333 | `board_smart` | local helper | `board, smart_id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 338 | `bucket_count` | local helper | `bucket` | Diagnostic helper for bucket count in the mutant task and blacklist diagnostic dump script. |
| 342 | `log_board` | local helper | `` | Diagnostic helper for log board in the mutant task and blacklist diagnostic dump script. |
| 383 | `list_levels_for` | local helper | `p, squad, mode` | Resolves or validates level names, ids, or level buckets. |
| 395 | `count_index_smarts` | local helper | `idx, levels, kind` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 403 | `collect_smarts` | local helper | `p, squad, opts` | Collects smarts from indexed or runtime data. |
| 411 | `count_hunt_targets` | local helper | `p, idx, squad, level_name` | Handles hunt target validation, combat consequences, or pursuit state. |
| 439 | `smart_reject_reason` | local helper | `cfg, squad, smart, level_name` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 472 | `log_smart_sample` | local helper | `squad, level_name` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 501 | `dump_squad` | local helper | `squad` | Prints a diagnostic dump of squad. |
| 617 | `collect_mutant_squads` | local helper | `` | Collects mutant squads from indexed or runtime data. |
| 649 | `M.dump` | module export | `reason` | Diagnostic helper for dump in the mutant task and blacklist diagnostic dump script. |
| 669 | `M.dump_squad` | module export | `squad_id` | Prints a diagnostic dump of squad. |
| 681 | `now_ms` | local helper | `` | Returns the current game or device time in milliseconds for throttling and cooldown checks. |
| 685 | `M.actor_on_update` | module export | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 716 | `M.actor_on_first_update` | module export | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 733 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 743 | `actor_on_first_update` | script hook/global | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 747 | `actor_on_update` | script hook/global | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 751 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/debugscripts/zhopa2_offline_inventory_diag.script`

Role: offline inventory probing and server-object diagnostic dump.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 59 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 68 | `debug_print_enabled` | local helper | `` | Checks whether ZHOPA debug output is enabled for this module. |
| 73 | `log` | local helper | `fmt, ...` | Emits a formatted diagnostic log line for the script. |
| 84 | `safe_field` | local helper | `obj, field` | Reads an object field through pcall and returns nil on failure. |
| 94 | `safe_call` | local helper | `obj, fn_name, ...` | Calls an object method through pcall and returns nil-safe results. |
| 106 | `object_id` | local helper | `obj` | Extracts a stable numeric id from a server object, online object, id-like table, number, or string. |
| 121 | `object_name` | local helper | `obj` | Returns a safe display name for an object or id. |
| 133 | `object_section` | local helper | `obj` | Returns a safe section name for an object. |
| 153 | `object_clsid` | local helper | `obj` | Diagnostic helper for object clsid in the offline inventory probing and server-object diagnostic dump script. |
| 162 | `named_id` | local helper | `obj_or_id` | Formats an object or id as a compact diagnostic name/id string. |
| 177 | `table_count` | local helper | `t` | Counts keys in a Lua table without assuming array layout. |
| 185 | `sorted_keys` | local helper | `t` | Returns table keys in a deterministic sorted order for stable diagnostics. |
| 196 | `member_server_object` | local helper | `member` | Handles squad member lookup, inventory ownership, or relation state. |
| 203 | `collect_squad_members` | local helper | `squad` | Collects squad members from indexed or runtime data. |
| 215 | `collect_child_ids` | local helper | `se_owner` | Collects child ids from indexed or runtime data. |
| 229 | `probe_value` | local helper | `obj, key, call_allowed` | Diagnostic helper for probe value in the offline inventory probing and server-object diagnostic dump script. |
| 244 | `probe_write_same` | local helper | `obj, key` | Diagnostic helper for probe write same in the offline inventory probing and server-object diagnostic dump script. |
| 255 | `dump_owner_probes` | local helper | `se_owner, prefix` | Prints a diagnostic dump of owner probes. |
| 271 | `dump_item_probes` | local helper | `se_item, prefix` | Prints a diagnostic dump of item probes. |
| 304 | `dump_member_inventory` | local helper | `squad, member, member_index` | Prints a diagnostic dump of member inventory. |
| 347 | `squad_online_state` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 356 | `squad_has_offline_member` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 367 | `M.dump` | module export | `` | Diagnostic helper for dump in the offline inventory probing and server-object diagnostic dump script. |
| 410 | `M.dump_squad` | module export | `squad, reason` | Prints a diagnostic dump of squad. |
| 433 | `M.dump_squad_on_update` | module export | `squad` | Prints a diagnostic dump of squad on update. |
| 452 | `M.actor_on_first_update` | module export | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 459 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 469 | `actor_on_first_update` | script hook/global | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 473 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/debugscripts/zhopa2_trade_route_diag.script`

Role: trade route, trade job, economy wrapper, and prepared-trade diagnostics.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 35 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 44 | `safe_mod` | local helper | `name` | Resolves an optional module without crashing when it is absent. |
| 53 | `debug_print_enabled` | local helper | `` | Checks whether ZHOPA debug output is enabled for this module. |
| 58 | `log` | local helper | `fmt, ...` | Emits a formatted diagnostic log line for the script. |
| 69 | `can_log` | local helper | `` | Determines whether log is allowed in the trade route context. |
| 77 | `tg` | local helper | `` | Returns the current time value used by throttled diagnostics. |
| 81 | `bounded_log` | local helper | `fmt, ...` | Diagnostic helper for bounded log in the trade route script. |
| 87 | `priority_log` | local helper | `fmt, ...` | Diagnostic helper for priority log in the trade route script. |
| 95 | `safe_field` | local helper | `obj, field` | Reads an object field through pcall and returns nil on failure. |
| 105 | `safe_call` | local helper | `obj, fn_name, ...` | Calls an object method through pcall and returns nil-safe results. |
| 117 | `object_id` | local helper | `obj` | Extracts a stable numeric id from a server object, online object, id-like table, number, or string. |
| 132 | `object_name` | local helper | `obj` | Returns a safe display name for an object or id. |
| 144 | `object_section` | local helper | `obj` | Returns a safe section name for an object. |
| 164 | `safe_alife_object` | local helper | `id` | Returns a server object by id through guarded ALife lookups. |
| 173 | `online_object_by_id` | local helper | `id` | Returns an online game object by id through db.storage/level lookups. |
| 191 | `item_price` | local helper | `item` | Diagnostic helper for item price in the trade route script. |
| 214 | `section_has_prefix` | local helper | `section, prefix` | Diagnostic helper for section has prefix in the trade route script. |
| 218 | `is_artifact_item` | local helper | `item, section` | Checks whether artifact item in the trade route context. |
| 230 | `cfg_bool` | local helper | `key, default` | Reads a boolean ZHOPA setting with a safe default fallback. |
| 238 | `cfg_num` | local helper | `key, default` | Reads a numeric ZHOPA setting with a safe default fallback. |
| 246 | `join` | local helper | `list, limit` | Diagnostic helper for join in the trade route script. |
| 262 | `table_count` | local helper | `t` | Counts keys in a Lua table without assuming array layout. |
| 270 | `sorted_keys` | local helper | `t` | Returns table keys in a deterministic sorted order for stable diagnostics. |
| 281 | `squad_matches` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 296 | `is_post_rest_reason` | local helper | `reason` | Checks whether post rest reason in the trade route context. |
| 300 | `current_level_for_squad` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 319 | `M.stalker_trade_diag_squad` | module export | `squad` | Handles trade routing, trade state, or trade diagnostics in the trade route module. |
| 330 | `route_levels_for_squad` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 343 | `smart_brief` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 350 | `squad_brief` | local helper | `squad` | Handles squad lookup, state, membership, or task coordination. |
| 357 | `smart_by_id` | local helper | `id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 373 | `current_action_id` | local helper | `npc` | Diagnostic helper for current action id in the trade route script. |
| 385 | `current_state` | local helper | `npc` | Reads, writes, or repairs runtime state. |
| 393 | `current_point_index` | local helper | `npc` | Diagnostic helper for current point index in the trade route script. |
| 401 | `path_index` | local helper | `npc` | Diagnostic helper for path index in the trade route script. |
| 409 | `dump_beh_runtime_snapshot` | local helper | `smart, npc, st, job, stage` | Prints a diagnostic dump of beh runtime snapshot. |
| 410 | `ini_string` | local helper | `ini, section, field` | Diagnostic helper for ini string in the trade route script. |
| 417 | `pos_brief` | local helper | `pos` | Diagnostic helper for pos brief in the trade route script. |
| 429 | `npc_pos` | local helper | `` | Diagnostic helper for npc pos in the trade route script. |
| 436 | `npc_vertex` | local helper | `fn_name` | Diagnostic helper for npc vertex in the trade route script. |
| 443 | `parse_pt_pos` | local helper | `line` | Parses pt pos from config, string, or diagnostic input. |
| 454 | `dist_to_pt` | local helper | `pos, line` | Diagnostic helper for dist to pt in the trade route script. |
| 469 | `reached` | local helper | `index` | Diagnostic helper for reached in the trade route script. |
| 476 | `target_brief` | local helper | `target` | Resolves, validates, or formats a task target. |
| 490 | `npc_info` | local helper | `info` | Diagnostic helper for npc info in the trade route script. |
| 497 | `npc_name` | local helper | `` | Diagnostic helper for npc name in the trade route script. |
| 506 | `pathpoint` | local helper | `index` | Diagnostic helper for pathpoint in the trade route script. |
| 577 | `has_info` | local helper | `npc, info` | Checks whether info is present in the trade route context. |
| 585 | `brief_target_value` | local helper | `value` | Resolves, validates, or formats a task target. |
| 602 | `brief_state_arg` | local helper | `arg` | Reads, writes, or repairs runtime state. |
| 631 | `mark_trade_npc_for_state_watch` | local helper | `npc_id, role, squad_id, trader_id` | Marks trade npc for state watch for later processing or diagnostics. |
| 644 | `trade_state_watch_info` | local helper | `npc` | Handles trade routing, trade state, or trade diagnostics in the trade route module. |
| 664 | `service_slot_for_npc` | local helper | `smart, npc_id` | Diagnostic helper for service slot for npc in the trade route script. |
| 684 | `lower_text` | local helper | `value` | Normalizes text to lowercase text for comparisons. |
| 688 | `contains_plain` | local helper | `value, needle` | Diagnostic helper for contains plain in the trade route script. |
| 693 | `job_section` | local helper | `job` | Diagnostic helper for job section in the trade route script. |
| 700 | `job_ini_string` | local helper | `job, smart, field` | Diagnostic helper for job ini string in the trade route script. |
| 719 | `job_is_trade_customer` | local helper | `job, smart` | Handles trade routing, trade state, or trade diagnostics in the trade route module. |
| 728 | `provider_role` | local helper | `job, smart` | Diagnostic helper for provider role in the trade route script. |
| 769 | `find_trade_customer_job_diag` | local helper | `smart, npc_id` | Finds trade customer job diag in indexed, runtime, or engine data. |
| 790 | `first_trade_provider_diag` | local helper | `smart, ignore_ids` | Handles trade routing, trade state, or trade diagnostics in the trade route module. |
| 817 | `binding_state` | local helper | `` | Reads, writes, or repairs runtime state. |
| 835 | `log_binding` | local helper | `stage, reason` | Diagnostic helper for log binding in the trade route script. |
| 845 | `unwrap_effect_wrappers` | local helper | `` | Removes or unwraps diagnostic wrappers for effect wrappers. |
| 855 | `M.trade_job_sell_items_diag_wrapper` | module export | `actor, npc, params` | Handles trade routing, trade state, or trade diagnostics in the trade route module. |
| 871 | `M.trade_job_give_id_diag_wrapper` | module export | `actor, npc, params` | Handles trade routing, trade state, or trade diagnostics in the trade route module. |
| 887 | `install_effect_wrappers` | local helper | `reason` | Installs effect wrappers wrappers, callbacks, or diagnostic hooks. |
| 904 | `prepared_signature` | local helper | `squad` | Diagnostic helper for prepared signature in the trade route script. |
| 920 | `dump_prepared_snapshot` | local helper | `squad, stage, reason` | Prints a diagnostic dump of prepared snapshot. |
| 1004 | `member_ids` | local helper | `squad` | Handles squad member lookup, inventory ownership, or relation state. |
| 1019 | `online_members` | local helper | `squad` | Handles squad member lookup, inventory ownership, or relation state. |
| 1038 | `inventory_scan` | local helper | `npc` | Scans, classifies, or mutates NPC/server inventory state. |
| 1048 | `scan` | local helper | `_, item` | Diagnostic helper for scan in the trade route script. |
| 1063 | `sell_plan_summary` | local helper | `npc` | Diagnostic helper for sell plan summary in the trade route script. |
| 1097 | `dump_members` | local helper | `squad` | Prints a diagnostic dump of members. |
| 1123 | `id_set` | local helper | `ids` | Diagnostic helper for id set in the trade route script. |
| 1131 | `plain_online_members` | local helper | `squad` | Handles squad member lookup, inventory ownership, or relation state. |
| 1143 | `dump_trade_job_candidates` | local helper | `smart, stage, wanted_npc_id` | Prints a diagnostic dump of trade job candidates. |
| 1196 | `dump_trade_intent_snapshot` | local helper | `squad, stage, reason, result_reason` | Prints a diagnostic dump of trade intent snapshot. |
| 1280 | `registry_weight` | local helper | `entry, squad, context` | Diagnostic helper for registry weight in the trade route script. |
| 1303 | `dump_registry_weights` | local helper | `squad, reason` | Prints a diagnostic dump of registry weights. |
| 1323 | `dump_trade_profile` | local helper | `squad, reason` | Prints a diagnostic dump of trade profile. |
| 1351 | `dump_route_candidates` | local helper | `squad` | Prints a diagnostic dump of route candidates. |
| 1392 | `M.dump_squad` | module export | `squad, reason` | Prints a diagnostic dump of squad. |
| 1430 | `M.dump_squad_id` | module export | `squad_id, reason` | Prints a diagnostic dump of squad id. |
| 1439 | `squad_from_board` | local helper | `id, stored` | Handles squad lookup, state, membership, or task coordination. |
| 1446 | `M.dump_all` | module export | `reason` | Prints a diagnostic dump of all. |
| 1477 | `patch_tasks` | local helper | `` | Installs or maintains the chain-friendly patch for tasks. |
| 1487 | `tasks.assign_next_task` | assigned wrapper | `squad, reason, ...` | Assigns next task and updates related ZHOPA state. |
| 1508 | `patch_economy` | local helper | `` | Installs or maintains the chain-friendly patch for economy. |
| 1516 | `economy.trade_route_task_weight` | assigned wrapper | `squad, base_weight, opts, ...` | Handles trade routing, trade state, or trade diagnostics in the trade route module. |
| 1537 | `economy.patch_trade_effect` | assigned wrapper | `...` | Installs or maintains the chain-friendly patch for trade effect. |
| 1549 | `economy.patch_trade_condition` | assigned wrapper | `...` | Installs or maintains the chain-friendly patch for trade condition. |
| 1559 | `economy.try_auto_trade` | assigned wrapper | `squad, reason, opts, ...` | Attempts auto trade and returns a controlled result instead of hard-failing. |
| 1589 | `economy.try_auto_trade_npc` | assigned wrapper | `npc, trader, reason, opts, ...` | Attempts auto trade npc and returns a controlled result instead of hard-failing. |
| 1618 | `patch_state_mgr` | local helper | `` | Installs or maintains the chain-friendly patch for state mgr. |
| 1627 | `state_mgr.set_state` | assigned wrapper | `npc, state_name, callback, timeout, target, extra, ...` | Sets state for the current trade route state. |
| 1666 | `M.install` | module export | `` | Diagnostic helper for install in the trade route script. |
| 1680 | `unregister_update` | local helper | `` | Unregisters update and cleans stale references. |
| 1686 | `M.watch_prepared_trades` | module export | `` | Handles trade routing, trade state, or trade diagnostics in the trade route module. |
| 1720 | `M.actor_on_update` | module export | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 1744 | `M.actor_on_first_update` | module export | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 1760 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 1773 | `actor_on_first_update` | script hook/global | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 1777 | `actor_on_update` | script hook/global | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 1781 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

### `projects/zhopa_alife_2/debugscripts/zhopa2_trade_smart_diag.script`

Role: trade smart and service-slot diagnostic dump.

| Line | Function | Kind | Parameters | Description |
| ---: | --- | --- | --- | --- |
| 17 | `cfg_mod` | local helper | `` | Resolves the ZHOPA configuration module if it is loaded or can be required safely. |
| 26 | `debug_print_enabled` | local helper | `` | Checks whether ZHOPA debug output is enabled for this module. |
| 31 | `log` | local helper | `fmt, ...` | Emits a formatted diagnostic log line for the script. |
| 42 | `safe_field` | local helper | `obj, field` | Reads an object field through pcall and returns nil on failure. |
| 52 | `safe_call` | local helper | `obj, fn_name, ...` | Calls an object method through pcall and returns nil-safe results. |
| 64 | `object_id` | local helper | `obj` | Extracts a stable numeric id from a server object, online object, id-like table, number, or string. |
| 79 | `object_name` | local helper | `obj` | Returns a safe display name for an object or id. |
| 91 | `safe_alife_object` | local helper | `id` | Returns a server object by id through guarded ALife lookups. |
| 100 | `named_id` | local helper | `obj_or_id` | Formats an object or id as a compact diagnostic name/id string. |
| 115 | `table_count` | local helper | `t` | Counts keys in a Lua table without assuming array layout. |
| 123 | `sorted_keys` | local helper | `t` | Returns table keys in a deterministic sorted order for stable diagnostics. |
| 134 | `now_ms` | local helper | `` | Returns the current game or device time in milliseconds for throttling and cooldown checks. |
| 144 | `level_name` | local helper | `` | Resolves or validates level names, ids, or level buckets. |
| 154 | `trim` | local helper | `value` | Diagnostic helper for trim in the trade smart and service-slot diagnostic dump script. |
| 161 | `smart_cfg_filename` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 179 | `open_ini` | local helper | `path` | Diagnostic helper for open ini in the trade smart and service-slot diagnostic dump script. |
| 188 | `smart_ini` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 200 | `section_line_count` | local helper | `ini, section` | Diagnostic helper for section line count in the trade smart and service-slot diagnostic dump script. |
| 212 | `obj_level` | local helper | `obj` | Resolves or validates level names, ids, or level buckets. |
| 235 | `smart_from_board` | local helper | `board, smart_id` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 250 | `smart_jobs_count` | local helper | `smart` | Handles smart-terrain lookup, validation, scoring, or diagnostics. |
| 258 | `flag_text` | local helper | `flags` | Diagnostic helper for flag text in the trade smart and service-slot diagnostic dump script. |
| 272 | `lower_text` | local helper | `value` | Normalizes text to lowercase text for comparisons. |
| 276 | `contains_plain` | local helper | `value, needle` | Diagnostic helper for contains plain in the trade smart and service-slot diagnostic dump script. |
| 281 | `job_field` | local helper | `job, field` | Diagnostic helper for job field in the trade smart and service-slot diagnostic dump script. |
| 288 | `job_section` | local helper | `job` | Diagnostic helper for job section in the trade smart and service-slot diagnostic dump script. |
| 292 | `job_suitable` | local helper | `job, smart` | Diagnostic helper for job suitable in the trade smart and service-slot diagnostic dump script. |
| 317 | `job_is_trade_customer` | local helper | `job, smart` | Handles trade routing, trade state, or trade diagnostics in the trade smart and service-slot diagnostic dump module. |
| 325 | `online_object_by_id` | local helper | `id` | Returns an online game object by id through db.storage/level lookups. |
| 343 | `storage_by_id` | local helper | `id` | Diagnostic helper for storage by id in the trade smart and service-slot diagnostic dump script. |
| 348 | `current_action_id` | local helper | `npc` | Diagnostic helper for current action id in the trade smart and service-slot diagnostic dump script. |
| 360 | `current_state` | local helper | `npc` | Reads, writes, or repairs runtime state. |
| 368 | `current_point_index` | local helper | `npc` | Diagnostic helper for current point index in the trade smart and service-slot diagnostic dump script. |
| 376 | `path_index` | local helper | `npc` | Diagnostic helper for path index in the trade smart and service-slot diagnostic dump script. |
| 384 | `binding_state` | local helper | `` | Reads, writes, or repairs runtime state. |
| 404 | `route_bucket_count` | local helper | `buckets` | Builds, validates, or diagnoses a route. |
| 414 | `flag_counts` | local helper | `flags_by_smart` | Diagnostic helper for flag counts in the trade smart and service-slot diagnostic dump script. |
| 444 | `dump_service_slots_for_smart` | local helper | `smart, tag` | Prints a diagnostic dump of service slots for smart. |
| 495 | `dump_route_buckets` | local helper | `board` | Prints a diagnostic dump of route buckets. |
| 530 | `dump_flagged_smarts` | local helper | `board` | Prints a diagnostic dump of flagged smarts. |
| 561 | `M.dump` | module export | `reason` | Diagnostic helper for dump in the trade smart and service-slot diagnostic dump script. |
| 600 | `M.refresh_trade_smart_index` | module export | `` | Refreshes trade smart index from current runtime or indexed data. |
| 616 | `M.refresh_and_dump` | module export | `` | Refreshes and dump from current runtime or indexed data. |
| 622 | `unregister_update` | local helper | `` | Unregisters update and cleans stale references. |
| 628 | `M.actor_on_update` | module export | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 647 | `M.actor_on_first_update` | module export | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 667 | `M.on_game_start` | module export | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |
| 680 | `actor_on_first_update` | script hook/global | `` | Actor first-update callback; performs one-shot world-ready initialization or schedules the first diagnostic pass. |
| 684 | `actor_on_update` | script hook/global | `` | Actor update callback; runs bounded deferred work, watches pending state, or emits diagnostics. |
| 688 | `on_game_start` | script hook/global | `` | Startup hook; initializes the script, installs callbacks or patches, and prepares module runtime state. |

