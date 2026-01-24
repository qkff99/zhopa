# SISKI — Design Document (current branch)

This document describes the current SISKI architecture and how it integrates with MCM/configs. It intentionally stays at the “what lives where and how things connect” level (no long function lists) to avoid becoming outdated after refactors.

## 1) Goals
- Give squads a persistent “brain” with a task queue.
- Keep the simulation alive (spawning/movement/background activities) without “herd” behavior.
- Provide safe operation on top of vanilla engine scripts (minimal crashes/spam).
- Make everything controllable via `siski_settings.ltx` and MCM.

## 2) Architecture and Data Flow
**Layers**
- **Core**: startup/callbacks/patches/save-load.
- **Memory**: single source of truth (smart/campfire/anomaly caches, squad state).
- **Brain**: task queue and execution.
- **Strategy**: high-level rules (base/campfire, etc.).
- **Lore**: faction background behavior (when there is no strategy task).
- **Spawner/Classes**: population support + special squads (AF Hunters).

**Main loop**
1. `siski_core` registers updates/callbacks and initializes subsystems.
2. `siski_intel` / scanners populate `siski_memory` with world caches (smarts, campfires, anomalies, level changers).
3. `siski_brain` periodically:
   - updates existing brains,
   - discovers new squads in `SIMBOARD` and attempts to attach a brain.
4. If a squad is `IDLE`, the brain tries strategy (`siski_strategic`), then lore (`siski_lore`).
5. Results are always synced back into `siski_memory` (reporting/limits/diagnostics).

## 3) Current Behavior Rules
### 3.1 Lore and target distribution
`siski_lore` generates background tasks per faction with anti-herding:
- Target candidates are taken from `siski_memory` (not directly from `intel`).
- Rescan is allowed only when memory caches are empty (safe degradation).
- For each lore group (EXPLORE/AMBUSH/PATROL/CONTRACT/ZEAL/CHILL) there is a limit: **at most one such lore activity per faction per level** (others go to neighboring levels).

### 3.2 Campfire patrol distribution
`siski_strategic.check_campfire_patrol`:
- Per level there is a limit: **1 campfire task per faction per level**.
- If the current level slot is taken, an offline squad selects a campfire on a neighboring level (by “level proximity”).

### 3.3 Vanilla squads (optional)
By default SISKI controls only squads spawned by SISKI itself.
If `alife_vanilla_squads` is enabled (MCM), brains can be attached to vanilla/other-mod squads, but:
- only if the squad section is allowed by `[spawner_allowed_sections_*]` from `siski_settings.ltx`;
- the spawner/population still counts **only** `spawned_by_siski=true`, so vanilla squads do not break limits.

## 4) Configs and UI
### 4.1 `gamedata/configs/siski_settings.ltx`
Main config. Key blocks:
- `[spawner_allowed_sections_*]`: allowed squad sections per faction.
- `[allowed_levels]`: per-faction level whitelist.
- `[population]`: target population values.
- `[smart_blacklist]`: smart restrictions.
- `[af_hunter_settings]`: AF Hunters settings (default `target_count_per_level = 1`).
- `[protector_pinned_sections]`: NPC sections that are “pinned” to `trader`.

### 4.2 MCM (`gamedata/scripts/siski_mcm.script`)
`on_mcm_load()` defines the MCM option tree.

**How MCM resolves localization (per AMCM guide)**
- Option names: `ui_mcm_<modid>_<option_id>`
- Tooltip description: `ui_mcm_<modid>_<option_id>_desc`
- For SISKI (`modid = siski`): `ui_mcm_siski_debug_enabled`, `ui_mcm_siski_debug_enabled_desc`, etc.

### 4.3 Localization (`gamedata/configs/text/*/ui_st_siski.xml`)
- `eng/ui_st_siski.xml`: UTF-8.
- `rus/ui_st_siski.xml`: **windows-1251** (important: otherwise the game/AMCM may not pick up strings and will show IDs).

## 5) Modules (short, based on what exists in this branch)
- `siski_core`: startup/callbacks/save-load/safety wrappers and patches.
- `siski_memory`: global state and world/squad caches.
- `siski_settings`: reads `siski_settings.ltx` + MCM (`ui_mcm.get("siski/<key>")`).
- `siski_intel`: world scanners and target selection helpers; fills `memory`.
- `siski_brain`: squad brains, task queue, memory sync, optional vanilla squad registration.
- `siski_strategic`: priority strategies (BASE_DEFENSE, CAMPFIRE and limits).
- `siski_lore`: faction background tasks with anti-herding and inter-level distribution.
- `siski_spawner`: population/spawn, safety checks, AF Hunter spawning.
- `siski_classes`: special squad classes (incl. AF Hunter).
- `siski_vendetta`: feuds and revenge targeting.
- `siski_scanner` + `siski_force_loot` + `siski_inventory` + `siski_trading` + `siski_activities`: economy/loot/trading.
- `siski_protector`: story NPC protection and `[protector_pinned_sections]` protection.
- `siski_debug` / `siski_reporter`: debugging (HUD and HTML report).
- `siski_logger`: logging.
- `siski_patches`: runtime patches to vanilla scripts (stability/compatibility).

## 6) Extending SISKI
### Add a new strategy
1. Add `check_<something>(brain)` to `siski_strategic`.
2. Wire it into `brain:think()` with the desired priority order.
3. Always set `params.reason` so reporter/limits/diagnostics can see the task.

### Add a new lore branch
1. Add a new reason in `siski_lore` and bind it to a limiter group.
2. Build candidates via `siski_memory`; rescan only when caches are empty.

## 7) Debugging and common issues
- If MCM shows IDs instead of localized names: first check `rus/ui_st_siski.xml` encoding (must be windows-1251) and that `ui_mcm_siski_*` and `ui_mcm_siski_*_desc` strings exist.
- If squads “don’t get brains”: check `siski_brain` (the `alife_vanilla_squads` option, section validity, and filters like story/companions/monsters).
- If herding happens on one level: check `siski_lore` and `check_campfire_patrol` limits (current level should be cut down to 1).

