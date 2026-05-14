# ZHOPA: дизайн-документ архитектуры

Английская версия: `docs/zhopa_0.7_design_document_en.md`

Примечание: имя файла историческое. Этот документ описывает текущую runtime-архитектуру ZHOPA в этой рабочей копии, а не старую 0.7-ветку.

## 1. Назначение
ZHOPA - это децентрализованный reactive ALife layer для Anomaly 1.5.3.

Базовый контур такой:
- engine callbacks приходят в `zhopa.core`;
- `zhopa.core` напрямую маршрутизирует callbacks в методы модулей;
- модули держат только локальное runtime state за явными методами `zhopa.*`;
- отложенная логика выполняется через keyed timers из `zhopa.timers`;
- steady-state central dispatcher отсутствует;
- whole-world scan loop отсутствует;
- cadence-based world traversal policy отсутствует.

Архитектурные инварианты:
- nil safety везде, где участвует движок;
- save safety: в сейв попадает только сериализуемое состояние;
- bounded hot paths;
- vanilla-first compatibility;
- `TRADE`, smart jobs и fillers не должны требовать глобального maintenance loop.

## 2. Bootstrap и runtime поток

### 2.1 Порядок загрузки
`gamedata/scripts/zhopa.script` теперь монолитный runtime bundle. Внутренний порядок логических блоков:
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

`axr_trade_manager.script` остается отдельным внешним bridge, который подключается при startup. `zhopa_mcm.script` остается отдельным MCM adapter. `zhopa_mcm_schema.script` теперь единственный источник schema для runtime config и MCM.

### 2.2 Порядок startup hooks
1. `zhopa.loot.on_game_start()`
2. `zhopa.loot_patch.on_game_start()`
3. `zhopa.fast_trading.on_game_start()`
4. `zhopa.npc_faction_override.on_game_start()`
5. `zhopa.heli_guard_patch.on_game_start()`
6. `zhopa.board_index.on_game_start()`
7. `axr_trade_manager.on_game_start()`
8. `zhopa.core.on_game_start()`

`zhopa_story_events`, `zhopa_smart_tasks` и `zhopa_story_psy_watchdog` открывают прямые методы, которые вызывает `zhopa.core`.

### 2.3 Callback surface
`zhopa.core` - центральный hub engine callbacks:
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

Ключевое правило:
- `squad_on_update` - основной gameplay decision point;
- `enter_smart`, `leave_smart` и `after_level_change` только мутируют save-safe state;
- глобального `on_update` dispatcher нет;
- `axr_trade_manager` дополнительно цепляет свой `npc_on_item_take` hook;
- `zhopa.core` только маршрутизирует события, а не выполняет глобальную симуляцию.

## 3. Модель данных

### 3.1 `zhopa_memory`
`zhopa.memory` - authority layer для squad entries и task state.

Он хранит только сериализуемые данные:
- identity/snapshot поля;
- task state;
- freshness flags;
- save-safe runtime metadata.

Удалены старые:
- sweep wheel;
- global freshness sweeps;
- per-level logic shards;
- любые скрытые steady-state maintenance loops.

### 3.2 `zhopa_board_index`
`zhopa.board_index` - reactive world index owner.

Он держит:
- `smarts_by_level`
- `base_smarts_by_level`
- `respawn_base_smarts_by_level`
- `squads_by_level`
- `smart_level_by_name`
- `smart_name_by_id`
- `squad_level_by_id`
- topology neighbors

Поведение:
- hydration из `SIMBOARD` на bootstrap и load;
- дальнейшее обновление через register/update/enter/leave/level-change callbacks;
- topology строится из level-changer events и сохраняется в save state;
- старые `smart_scan`, `squad_scan`, `static_scan` runtime-структуры удалены.

### 3.3 Module-owned runtime
Некоторые подсистемы владеют своим runtime state сами, но обязаны оставаться save-safe:
- `zhopa_story_events` хранит собственный state blob;
- `zhopa_smart_tasks` хранит claim cache и dirty-smart state;
- `zhopa_story_psy_watchdog` держит только transient caches;
- fillers держат собственные reconcile queues и timestamp-метки.

## 4. Фундаментальные модули

### 4.1 `zhopa_oop`
Локальный helper для class/singleton-обвязки. Нужен только для одинакового создания модулей и их методов. На runtime-архитектуру не влияет.

### 4.2 `zhopa_switches`
Матрица включения модулей. Делает feature-gating на runtime и на старте. Если подсистема кажется выключенной, сначала проверяется именно этот слой.

### 4.3 `zhopa_timers`
Ключевой timer registry.

Используется для:
- debounce;
- cooldown;
- timeout;
- reevaluate;
- cleanup;
- delayed continuation.

Требование: keyed timers, а не общий polling loop.

### 4.4 `zhopa_safe`
Nil-safe wrapper слой вокруг движка и engine objects. Его роль - снять из кода дублирование проверок `type(...)`, `pcall`, `nil`-guard и безопасных fallback'ов.

### 4.5 `zhopa_log`
Централизованный логгер и gating по уровню логов. При `log_level = 0` файл лога не должен создаваться.

### 4.6 `zhopa_config`
Слой чтения конфигурации.

Семантика чтения:
1. runtime override;
2. MCM;
3. LTX default.

Он же отвечает за:
- `level_smarts_*`;
- `level_neighbors`;
- `anomaly_smarts`;
- `level_bases`;
- smart-task blacklist/whitelist maps;
- trade/base/service/loot knobs;
- feature toggles.

Ключевые группы helper-ов:
- чтение LTX/MCM и кеширование;
- CSV/section parsing;
- normalized blacklist rules;
- smart-task maps;
- runtime override cache;
- MCM path resolution.

## 5. Оркестратор: `zhopa.core`

### Назначение
`zhopa.core` - точка входа runtime. Он:
- регистрирует engine callbacks;
- синхронизирует log level;
- bootstraps enabled runtime;
- напрямую маршрутизирует callbacks в методы модулей;
- делает save/load routing;
- маршрутизирует `squad_on_update` в специализированные FSM.

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
- `on_server_entity_unregister(...)`

### Key helpers
- `can_run(name)` - проверяет switches/config gating;
- `safe_call(tag, fn, ...)` - безопасный вызов движка;
- `route_*` helpers - ограниченный прямой fan-out в методы модулей;
- `update_memory_snapshot(squad, source)` - обновляет `zhopa_memory`;
- `dispatch_direct_squad_fsm(squad, source)` - отправляет squad в FSM chain;
- `apply_runtime_fixes()` - runtime shims/fixes;
- `get_offlevel_squad_update_skip_count()` и related helpers - защита от лишних off-level обновлений;
- `debug_hud_enabled()` - runtime gate для HUD.

### Алгоритм
1. На game start включает зависимости в правильном порядке.
2. На first update выполняет one-shot hydration.
3. На `squad_on_update`:
   - сначала story events;
   - потом smart tasks;
   - затем mutant task FSM или stalker task FSM;
   - только потом локальные post-actions.
4. `enter_smart` / `leave_smart` / `after_level_change` не являются decision points - они только синхронизируют state.

## 6. Реактивный индекс мира: `zhopa.board_index`

### Назначение
Модуль владеет актуальной картой мира для ZHOPA: смарты, squads, topology, revisions.

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

### Основные алгоритмы
- bootstrap hydration из `SIMBOARD`;
- incremental upsert/remove на register/unregister;
- squad level tracking на enter/leave/after_level_change;
- neighbor topology rebuild from level changer data;
- cached view materialization with per-level revisions;
- diagnostics counters для tracking broken data.

### Ключевые helper-кластеры
- bucket helpers: `append_level_value`, `set_level_value`, `unset_level_value`, `build_sorted_bucket_array`;
- topology helpers: `merge_unique_arrays`, `append_level_edge`, `edge_sets_to_arrays`, `copy_edge_map`, `copy_array_map`, `copy_level_changer_edges`;
- state packet helpers: `make_state_packet`, `get_level_changer_data`, `get_level_changer_data_fallback`;
- filtering helpers: `is_base_smart`, `is_respawn_base_smart`, `is_level_name`, `level_from_object`, `object_name`;
- runtime/diag helpers: `create_runtime`, `ensure_diag`, `diag_inc`, `diag_push`, `diag_fail`, `diag_last`.

## 7. Authority layer: `zhopa.memory`

### Назначение
Это save-safe authority store для squad lifecycle, task state и runtime indexes.

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

### Что хранится
- entry snapshot;
- task.current / task.prev / task.next;
- dirty flags;
- last seen time;
- trade/anchor/occupancy indexes;
- protected squad markers;
- surge lock markers;
- normalized loaded state.

### Ключевые helper-кластеры
- sanitization: `clone_serializable`, `compact_task`, `compact_entry`, `_normalize_loaded_task`, `_normalize_loaded_entry`;
- index lifecycle: `_index_entry`, `_unindex_entry`, `_reindex_entry`, `_rebuild_runtime_indexes`;
- entry lifecycle: `_validate_live_squad`, `_touch_squad`, `_touch_squad_validated`, `_purge_squad_entry`, `_prune_missing_squads_once`;
- task lifecycle: `_set_task_current`, `_clear_tasks`, `reset_task_scheduler_fields`, `_ensure_tasks_shape`;
- arrival/level lifecycle: `_mark_arrived_to_target`, `_mark_left_target`, `_mark_level_changed`;
- persistence: `_save_state`, `_load_state`;
- protection logic: `_is_protected_squad`, `_should_manage_squad`, `_is_monster_squad_live`, `_is_companion_squad_id`;
- surge control: `_set_surge_lock`, `_get_surge_lock`.

### Алгоритм
`memory` не принимает решения о задачах сам по себе. Он:
1. нормализует live squad snapshot;
2. валидирует serializable fields;
3. индексирует entry по level/smart/community;
4. отмечает dirty state для consumers;
5. отдает save/load blob без userdata и engine references.

## 8. Stalker task FSM: `zhopa.tasks_registry`

### Назначение
Это главный stalker task engine. Он строит, выбирает, проверяет и завершает задачи для обычных squad-ов.

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

### Основные task types
- `REST_1H`
- `EXPLORE`
- `ARTEFACT`
- `BASE_CAMPING`
- `PATROL`
- `POPULATE`
- `TRADE`
- `NIGHT_REST`

### Алгоритмический конвейер
1. Собирается `ReactiveContext`.
2. Читается entry из `zhopa.memory`.
3. Строится кандидат текущей задачи и проверяется ее валидность.
4. При завершении вызывается `rotate_task_on_complete`.
5. Если задача требует real-time intent, выставляется `scripted_target`.
6. `TRADE` остается trigger-driven и не возвращается в generic roam rotation.

### Ключевые helper-кластеры
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
- `REST_1H`: играющийся отдых с clamp по игровым секундами при необходимости.
- `EXPLORE`: переход на соседний level и выбор безопасного смарта.
- `ARTEFACT`: переход на anomaly smart и проверка nearby artefact/online pickup path.
- `BASE_CAMPING`: ожидание на безопасной базе.
- `PATROL`: обход smarts без повторов.
- `POPULATE`: поход к союзному присутствию.
- `TRADE`: переход в smarts с trader job slot.
- `NIGHT_REST`: ночной fallback-only rest.

## 9. Trade contract: `zhopa.trade`

### Назначение
`zhopa.trade` владеет task-side service contract для `TRADE` и local timeout timers.

### Public API
- `notify_trade_started(npc_id, smart_name, source)`
- `consume_trade_started(squad_id, expected_target)`
- `reset_runtime()`
- `consume_service_event(squad_id, expected_target)`
- `can_trade_now(se_squad)`
- `tick(se_squad, entry, task)`

### Алгоритм
1. `npc_on_item_take` или service callbacks создают service event.
2. `trade` проверяет surge lock и live state.
3. `can_trade_now` решает, можно ли стартовать `TRADE`.
4. На старте и конце session данные синхронизируются через memory и прямые core routes.
5. Таймауты и cooldown решаются keyed timers, а не глобальным polling loop.

### Helper-кластеры
- service result storage: `apply_service_event_to_memory`, `remember_service_event`;
- surge gate: `surge_started_uncached`, `is_surge_started`, `get_surge_lock`;
- smart/job inference: `infer_seller_id_from_smart`, `smart_has_trader_job_slot`, `resolve_live_trader_for_trade_smart`, `evict_leader_from_trade_job`;
- trade state: `prepare_trade_flags`, `is_trade_job`, `is_tech_job`, `is_trader_job`, `has_service_items`, `get_service_state`, `get_trade_phase`.

## 10. Vanilla trade bridge: `axr_trade_manager`

### Назначение
Этот модуль расширяет vanilla NPC-to-NPC trade/service flow. Он не заменяет ванилу, а дописывает интенты, service flags и conditions/effects.

### Главные публичные точки
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

### Что делает модуль
- ставит per-NPC trade/tech intent в `db.storage`;
- поддерживает service job lifecycle;
- связывает NPC item take с ванильными trade hooks;
- восстанавливает `seller_id`/service bindings, если ваниль их потеряла;
- завершает session и чистит storage;
- фильтрует provider NPC, чтобы они не попадали в собственный customer path.

### Почему важен guard для provider NPC
Именно здесь находится класс бага, когда service NPC могли получить свой же `has_tech_items` или `has_items_to_sell`, после чего smart terrain начинал гонять их по кругу между креслом и рабочим местом. Provider-role должен быть исключен из customer intent path.

### Ключевые helper-кластеры
- suppression: `begin_item_take_suppress`, `end_item_take_suppress`, `is_item_take_suppressed`, `create_item_self_suppressed`;
- job classification: `is_trade_job`, `is_tech_job`, `is_trader_job`, `smart_has_trader_job_slot`, `smart_has_tech_job_slot`, `smart_has_free_tech_job_slot`;
- candidate selection: `pick_random_buy_candidate`, `pick_random_mechanic_bonus_candidate`;
- state update: `mark_tech_item_intent`, `clear_service_intents`, `finalize_service_session`, `notify_zhopa_trade_service_result`, `notify_zhopa_trade_started`;
- logging: `emit_prefixed_log`, `emit_zhopa_trade_log`, `log_trade_info`, `log_trade_warn`, `log_handler_binding_state`.

## 11. Smart control tasks: `zhopa.smart_tasks`

### Назначение
`zhopa.smart_tasks` владеет smart-terrain `control` task type.

### Public API
- `update_squad_tasks(se_squad, ctx)`
- `on_game_start()`

### Основные правила
- smart control живет через claim cache;
- dirty smart state reconciles через прямые core routes и timers;
- conflict resolution идет по текущему live occupancy;
- task assignment не должен требовать scan loop;
- `control` - это не roam task, а ownership/occupation task.

### Алгоритм
1. Собирается smart context.
2. На основании memory и live board строится claim snapshot.
3. Проверяются конфликты и relation rules.
4. Выбирается кандидат для control.
5. Создается или обновляется `control` task.
6. Если current task устарел, он валидируется или снимается.

### Ключевые helper-кластеры
- target sync: `is_target_sync_enabled`, `get_online_intent_enforce_enabled`, `set_scripted_target`, `set_squad_always_arrived`;
- online squad checks: `is_online_squad`, `try_soft_register_squad_to_smart`, `try_soft_assign_free_stalker_jobs_once`, `enforce_online_task_intent`, `clear_live_task_state`;
- blacklists and filters: `smart_blacklists_global_set`, `smart_blacklists_rule`, `faction_level_blacklists_rule`, `faction_smart_blacklists_rule`, `section_level_blacklists_rule`, `section_smart_blacklists_rule`, `entry_allowed_for_smart_task`;
- identity and claims: `build_identity_from_entry`, `build_identity_from_task`, `is_enemy_identity`, `current_identity_count`, `add_runtime_claim`, `remove_runtime_claim`;
- candidate flow: `candidate_distance`, `candidate_position_distance`, `candidate_reject_reason`, `pick_control_candidate`;
- conflict resolution: `validate_current_control_claim`, `build_control_claim_snapshot`, `sort_control_claim_snapshots`, `resolve_control_conflicts`, `reconcile_control_smart`, `reconcile_smart`, `try_fill_control_smart_jobs_once`;
- runtime maintenance: `dirty_smart_names`, `process_dirty_smarts`, `rebuild_runtime_claims_from_memory`, `mark_all_known_smarts_dirty`, `reactivate_runtime`.

## 12. Story subsystem: `zhopa.story_events`

### Назначение
`story_events` владеет отдельным story FSM. Сейчас это не generic side-effect layer, а конкретный сюжетный механизм.

### Current story event
Основной текущий сценарий - `North migration`.

### Public API
- `update_squad_tasks(se_squad, ctx)`

### Алгоритм
1. Модуль восстанавливает свой state blob.
2. Выбирает eligible sid-ы.
3. Проверяет, не занят ли squad защищенным или transient состоянием.
4. Подбирает безопасную цель по level/community/terrain policy.
5. Назначает story task или ретаргетит существующую.
6. При отключении feature или завершении сценария очищает state.

### Ключевые helper-кластеры
- state blob: `new_state`, `get_state_event`, `load_state_blob`, `save_state_blob`, `normalize_sid_set`, `normalize_status_map`, `set_sid_status`;
- validation: `is_story_mode_active`, `feature_enabled_now`, `migration_trigger_active`, `is_protected_squad`, `is_sid_selected`, `is_sid_locked`;
- target selection: `get_level_base_smarts`, `get_level_smarts`, `get_level_territory_smarts`, `get_level_neighbors`, `pick_nearest_safe_base_on_level`, `pick_nearest_safe_territory_on_level`, `pick_random_safe_smart_on_level`, `pick_safe_target_on_level`, `pick_north_migration_target`;
- live sync: `make_story_task`, `set_scripted_target`, `sync_story_task_live_state`, `entry_arrived_to_smart`, `consume_story_live_arrival_signal`, `is_story_arrived`;
- completion and retargeting: `maybe_finish_as_rest`, `clear_story_task_if_present`, `assign_story_task`, `retarget_story_task`, `clear_story_task_when_disabled`;
- runtime filters: `surge_active_uncached`, `is_surge_active_now`, `relation_allows_coexist`, `collect_smart_communities`, `is_story_target_safe`, `level_order_for_squad`.

## 13. Psi watchdog: `zhopa.story_psy_watchdog`

### Назначение
Реактивный story-level modifier, который конвертирует squads на настроенных psi levels в zombied squads.

### Public API
- `on_game_start()`
- `reconcile_all_levels()`

### Алгоритм
1. Читает psi-levels и immune factions из конфигурации.
2. Сверяет live squads с board/memory.
3. Для подходящих squad-ов создаёт zombied replacement.
4. Пересобирает squad composition и smart binding.
5. Не использует отдельный scan runtime и не держит steady-state polling.

### Ключевые helper-кластеры
- parsing/config: `get_cfg_value`, `get_psi_levels`, `get_immune_factions`, `parse_csv_set`, `feature_enabled_now`;
- squad snapshot: `build_snapshot_context`, `read_commander_id`, `get_squad_member_ids`, `read_member_count`, `candidate_should_convert`;
- zombification: `pick_zombied_squad_section`, `pick_zombied_member_section`, `create_empty_squad`, `populate_zombied_squad`, `finalize_spawned_squad`, `convert_squad_to_zombied`;
- safe release/reassign: `release_squad_safe`, `assign_squad_to_smart`, `resolve_smart_object_by_id`, `resolve_smart_name_by_id`;
- scan orchestration: `try_process_squad`, `reconcile_level_once`, `reconcile_all_levels`.

## 14. Dynamic worlds and fillers

### 15.1 `zhopa.base_filler`
Реактивный dirty-target reconcile для dedicated camper squads.

Публичные точки:
- `on_first_update()`
- `save_state(m_data)`
- `load_state(m_data)`
- `is_base_camper_section(section)`
- `get_runtime_stats()`

Алгоритм:
- индексирует target smarts;
- выбирает safe base campers;
- спавнит/reconciles squads только для dirty targets;
- держит spawn override только локально на короткий участок кода;
- защищает actor-level area от лишнего заполнения.

Ключевые helper-кластеры:
- spawn override: `active_spawn_override_count_range`, `should_override_spawn_count`, `build_ini_sys_proxy`;
- target mapping: `refresh_sections_index`, `remember_mapping`, `clear_smart_mapping`, `pick_faction_for_smart`, `pick_camper_section`;
- reconcile: `mark_target_dirty`, `consume_dirty_targets`, `reconcile`, `run_dirty_reconcile`, `spawn_camper`, `pin_squad_to_smart`.

### 15.2 `zhopa.dynamic_bases`
Reactive owner recompute для dynamic bases.

Публичные точки:
- `on_first_update()`
- `reset_runtime(reason)`
- `save_state(m_data)`
- `load_state(m_data)`
- `get_runtime_stats()`
- `get_effective_owner(smart)`

Алгоритм:
- собирает target list;
- вычисляет effective owner alias;
- пересобирает respawn params;
- обновляет only dirty targets;
- хранит original entries отдельно от runtime-generated state.

### 15.3 `zhopa.service_filler`
Reactive per-smart service-role populate module.

Публичные точки:
- `on_first_update()`
- `reset_runtime(reason)`
- `save_state(m_data)`
- `load_state(m_data)`
- `get_runtime_stats()`
- `is_service_section(section)`
- `get_task_proxy_seed(npc)`

Алгоритм:
- классифицирует provider jobs по роли;
- смотрит live population и existing service squads;
- спавнит missing service squads only when target is due;
- respects smart ownership / AP bridge / non-service population;
- keeps pending spawn state and retry cooldowns local.

Ключевые helper-кластеры:
- role classification: `section_role`, `section_owner_alias`, `classify_provider_job_role`, `classify_job_role`, `role_profile`;
- spawn gating: `smart_has_non_service_population`, `skip_retry_ready`, `set_skip_retry`, `clear_skip_retry`, `ensure_warfare_ignore`;
- pending state: `pending_bucket`, `get_pending_spawn`, `set_pending_spawn`, `clear_pending_spawn`, `resolve_holder_squad`, `pin_service_squad`, `sync_pending_for_role`;
- target sync: `sync_targets_from_index`, `mark_target_dirty`, `mark_all_index_targets_dirty`, `process_smart`, `run_dirty_reconcile`.

## 16. Loot subsystem

### 16.1 `zhopa.loot`
Event producer and lootability state manager.

Публичные точки:
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

Алгоритм:
- помечает corpse/item events;
- ведет TTL-based event queues;
- умеет временно снимать actor proximity limit;
- может открывать трупы для AI loot;
- не переносит предметы сам по себе, а только улучшает оценку целевых объектов.

### 16.2 `zhopa_loot_patch`
Точечный patch layer для `xr_corpse_detection` и `eva_gather_itm`.

Публичные точки:
- `apply()`
- `on_game_start()`

Алгоритм:
- подмешивает loot events в выборку целей;
- фильтрует по scan cooldown/radius;
- уважает quest corpse protection;
- использует retry apply если патчи не смогли примениться с первого раза.

## 17. Compatibility patches

### 17.1 `zhopa_npc_faction_override`
Подменяет vanilla role checks для trader/mechanic/medic/barman и применяет override на squad/member уровне.

Публичные точки:
- `on_game_start()`
- `on_option_change()`
- `on_load_state()`
- `on_server_entity_register(...)`
- `on_server_entity_unregister(...)`
- `on_squad_npc_creation(...)`
- `on_squad_npc_death(...)`

### 17.2 `zhopa_xr_conditions_patch`
Патчит role conditions и invulnerability handling для ZHOPA squads.

Публичные точки:
- `Patch.apply()`

### 17.3 `zhopa_axr_task_patch`
Narrow patch layer around vanilla task helpers, чтобы SIKI мог работать без замены целых систем.

Публичные точки:
- `Patch.apply()`

## 18. Debug HUD
`zhopa.debug_hud` - observational only.

Публичные точки:
- `on_load_state()`
- `on_save_state()`
- `on_option_change()`

Алгоритм:
- строит map spots по memory state;
- умеет удалять и пересоздавать споты;
- не должен становиться source of truth;
- должен оставаться ownership-safe.

## 19. Config surface and save contract

### 19.1 User-facing config
Сейчас exposed knobs включают:
- global enable / logging;
- task toggles and durations;
- targeting / anti-stuck / online intent timeouts;
- mutant behavior toggles and timings;
- trade / fast trading;
- base filler settings;
- dynamic bases toggle;
- service filler settings;
- loot distances / TTL / limits / patch size;
- cache and diagnostic knobs that still affect runtime.

### 19.2 Save/load owners
`zhopa.core` делегирует save/load сюда:
- `zhopa.board_index`
- `zhopa.memory`
- `zhopa.dynamic_bases`
- `zhopa.base_filler`
- `zhopa.service_filler`
- `zhopa.debug_hud` hooks when enabled

Правило:
- в save state попадает только serializable data;
- userdata, closures, engine refs, transient caches и handles запрещены.

## 20. Как расширять систему

### 20.1 Добавление новой задачи
Сначала задается contract:
- type;
- target semantics;
- completion conditions;
- apply semantics;
- save-safe params.

Дальше:
1. builder;
2. assignment;
3. rotation on completion;
4. target validation;
5. cheap completion check;
6. apply path;
7. config/UI/docs, если поведение user-facing.

### 20.2 Что нельзя делать
- не возвращать central dispatcher;
- не делать whole-world scan в steady state;
- не хранить userdata в save state;
- не скрывать long-lived runtime state в неявных global tables;
- не вводить legacy loops под новым именем.

## 21. Критерии корректности
Изменение считается нормальным, если:
1. поведение правильное и nil-safe;
2. hot path bounded;
3. save/load safety сохранена;
4. config/UI/docs синхронизированы;
5. diff остается сфокусированным на нужной подсистеме.

## 22. Остальные runtime-скрипты

### `zhopa_fast_trading`
Immediate helper around `npc_on_item_take`.

Публичные точки:
- `process_check(npc_id, data)`
- `on_npc_item_take(npc, item)`
- `on_trade_completed(squad_id, result)`
- `consume_pending_trigger(squad_id)`
- `on_game_start()`
- `get_runtime_stats()`
- `reset_cache()`

Алгоритм:
- проверяет триггеры по item take;
- выдерживает short delay before re-check;
- запускает quick trade only when squad is eligible;
- ставит cooldown after trigger;
- никогда не должен превращаться в постоянный polling loop.

### `zhopa_mutants`
Отдельный mutant FSM, не связанный с stalker roam logic.

Публичные точки:
- `update_squad_tasks(se_squad, ctx)`
- `get_runtime_stats()`
- `reset_runtime(reason)`

Ключевые функции и кластеры:
- night/day detection: `is_night_now`, `is_predator_phase_inactive`;
- phase detection: `normalize_predator_phase_alias_key`, `detect_predator_phase_from_text`, `_resolve_predator_phase`;
- board/safety: `validate_live_squad_with_memory`, `resolve_entry_level`, `is_hunt_enabled`, `is_surge_active`;
- blacklists: `smart_blacklists_*`, `faction_*_blacklists_*`, `section_*_blacklists_*`;
- task flow: `make_task`, `build_rest_task`, `_build_hunt_task`, `_build_explore_task`, `_build_patrol_task`, `_pick_day_roam_task`, `_pick_first_task`, `_rotate_task`, `_is_task_target_valid`, `_is_task_completed`, `_apply_task`;
- presence model: `_ensure_hunt_presence_slot`, `_add_hunt_presence`, `_apply_hunt_presence_marks`, `_clear_hunt_presence_for_sid`, `_process_stalker_presence`, `_bootstrap_presence_from_board`;
- runtime maintenance: `_trim_filtered_smarts_cache`, `_get_filtered_smarts_for_level`, `_invalidate_hunt_level_smarts_cache`, `_refresh_presence_for_live_squad`, `_mark_mutant_dirty_if_managed`.

Алгоритм:
1. Снимает night/surge/board context.
2. Ставит or updates predator phase.
3. Строит task from current phase and local presence.
4. Проверяет arrival/completion through cheap state checks.
5. Обновляет presence cache реактивно.

### `zhopa_mcm_schema`
Схема для MCM surface.

Публичные точки:
- `get_path(key)`
- `get_option(key)`

Роль:
- задает structured key map для `zhopa/<panel>/<key>`;
- служит источником truth для MCM UI и текстовых ключей;
- не должна содержать gameplay logic.

### `zhopa_heli_guard_patch`
Точечный guard для heli respawn/callback edge cases.

Ключевые функции:
- `apply_se_heli_patch()`
- `apply_bind_heli_patch()`
- `apply_patch()`
- `master_enabled()`
- `on_game_start()`

Алгоритм:
- проверяет heli respawn counter entries;
- чистит stale references;
- патчит SE heli и bind heli code paths;
- включается только при master enabled.

### `zhopa_safe`
Nil-safe wrapper utilities.

Публичные точки:
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

Роль:
- стандартизует безопасный доступ к engine objects;
- centralizes `pcall` and fallback behavior.

### `zhopa_log`
Logger and file sink.

Публичные точки:
- `set_level(lvl)`
- `get_level()`
- `set_file(filename)`
- `flush()`
- `error(module, fmt, ...)`
- `warn(module, fmt, ...)`
- `info(module, fmt, ...)`
- `debug(module, fmt, ...)`
- `trace(module, fmt, ...)`

Ключевые helper-ы:
- `now_tg()`
- `level_name(lvl)`
- `truncate_file(path)`
- `Logger:_emit(...)`
- `Logger:_schedule_flush()`

### `zhopa_oop`
Публичная точка:
- `zhopa.class(name)`

Роль:
- минимальный class helper для singleton modules.
