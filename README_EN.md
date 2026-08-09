# Z.H.O.P.A. ALIFE 2.0

[Русский](README.md) | [Changelog](changelog_en.md) | [Architecture](docs/zhopa_alife_2_design_document_en.md) | [Function reference](docs/zhopa_alife_2_function_reference_en.md)

[![DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/qkff99/zhopa)

> **Zone Hostile Operations & Population AI** - a modular ALife extension for S.T.A.L.K.E.R. Anomaly 1.5.3 + Modded Exes.

Z.H.O.P.A. makes life in the Zone more connected: squads receive purposeful tasks, pursue moving targets, collect loot and artefacts, trade, occupy bases, and react to story events. Movement, smart jobs, online/offline transitions, pathfinding, and core combat behavior remain under game control.

## Features

| Subsystem | Behavior |
| --- | --- |
| Squad tasks | Stalkers explore the Zone, populate smart terrains, patrol, rest, hunt, take revenge, collect artefacts, and travel to trade. Mutants use a separate task pool. |
| Task balance | Valid task-target pairs are weighted by squad strength, local faction pressure, and optional faction preferences. Story and safety tasks remain outside this random selection. |
| Hunt and revenge | Targets are tracked by their actual squad position, including level transitions. Actor revenge makes only the assigned squad hostile, not its entire faction. |
| Loot | Online logic extends vanilla pickup and prevents loops on rejected items. Offline loot is bounded virtual cargo and consumes no engine object IDs. |
| Economy | The leader trades for the whole squad, sells real and virtual goods, pools member money, and buys basic supplies. |
| Artefacts | Real and virtual offline artefacts are supported, including smart assignment and online pickup by a selected NPC with detector animation. |
| Bases and services | The addon tracks base ownership and can refill suitable service roles after an emission. |
| Story events | Story mode enables psi zombification and northern migration after the Brain Scorcher shutdown. These systems do not run in freeplay. |

Current tasks: `REST`, `EXPLORE`, `FORCE_EXIT`, `POPULATE`, `BASE_CAMPING`, `PATROL`, `NIGHT_REST`, `ARTEFACT`, `TRADE`, `HUNT`, `REVENGE`, `STORY_NORTH_MIGRATION`.

## Trade and Economy

- Online deals run through a vanilla trade customer job and the SISKI-derived `axr_trade_manager.script`.
- The smart job selects the actual seller through `npc_info.job.seller_id`; ZHOPA does not replace it with a preselected NPC.
- Only traders and barmen are regular trade providers. Medics, mechanics, and faction leaders are not treated as ordinary sellers.
- A mechanic visit can be triggered only by a real `i_upgrade` item held by the NPC. Ordinary supply purchases do not create synthetic tech intent.
- Offline deals sell serializable virtual cargo and use virtual squad money.
- `npc_sell_price_multiplier` controls NPC sale income; the default value is `0.2`.

## Looting

Online looting uses vanilla pickup schemes whenever they can complete normally. ZHOPA adds targeted pickup, anti-stall handling, and memory cleanup after rejected or completed loot so an NPC cannot retry the same corpse or item forever.

After offline combat, loot is recorded in a bounded virtual ledger. It is sold through the economy or materialized only in a controlled scenario, such as an online NPC death. This prevents long playthroughs from exhausting the engine object-ID pool.

## Artefacts

Real artefacts are registered in runtime indexes and belong to exactly one suitable smart bucket. A real artefact is preferred whenever one is available. Virtual artefacts are generated from anomaly-zone settings for the offline economy only and do not reduce real artefact spawn.

## Requirements

- S.T.A.L.K.E.R. Anomaly 1.5.3.
- Current Modded Exes for Anomaly 1.5.3.
- MCM is optional; without it, defaults come from `gamedata/configs/zhopa2_settings.ltx`.

## Installation

### Mod Organizer 2

1. Disable or remove old REZNYA, SISKI, and ZHOPA versions.
2. In MO2, select `File` -> `Install Mod...`.
3. Select the Z.H.O.P.A. ALIFE 2.0 archive and confirm installation.
4. Place the addon below conflicting mods when its bundled `axr_trade_manager.script` must win the conflict.

### Manual

Copy the `gamedata` directory into the Anomaly root. Verify the resulting files under `gamedata/scripts`, `gamedata/configs`, `gamedata/configs/text`, and `gamedata/textures`.

## Settings

Settings are available in MCM -> `ZHOPA ALIFE 2` and mirrored in `gamedata/configs/zhopa2_settings.ltx`.

Main MCM sections:

- core systems;
- economy and helper systems;
- story events;
- stalker and mutant simulation;
- task weights, balance, and durations;
- combat, routing, and target following;
- debugging.

Task balance is enabled by default. Its numeric tuning, level overrides, squad strength overrides, and faction profiles are kept in `gamedata/configs/zhopa2_population_profiles.ltx`; MCM exposes only the three gameplay switches and the Soft / Balanced / Strict direct-target policy.

Online managed looting is experimental and disabled by default. Leave it disabled to use vanilla looting, the more predictable choice for large mod packs; artefact tasks continue to use their separate targeted pickup path. After updating the addon, use MCM's **Reset to defaults** before changing options so the current recommended defaults take effect.

## Compatibility

| Status | Mods and builds |
| --- | --- |
| Tested | Vanilla Anomaly 1.5.3, G.A.M.M.A. 0.9.4/0.9.5, Anthology 2.1 |
| Compatible | ZCP, the REDONE family, New Levels |
| Incompatible | Alife Plus |
| Requires testing | Mods that fully replace `sim_squad_scripted`, `smart_terrain`, `sim_board`, `xr_gather_items`, `xr_corpse_detection`, `axr_trade_manager`, or related callbacks |

Additional notes:

- NPC loot restrictions, including `NPC Loot Claim`, `NPC Stop Looting Dead Bodies`, and the Useful Idiots option that allows only companions to search bodies, reduce the amount of functioning economy. ZHOPA looting or economy can be disabled separately in MCM.
- `xcvb's Guards Spawner` does not block the addon, but it may write log messages about squads after ZHOPA begins managing them.
- Combat AI addons are usually safer as long as they do not replace SIMBOARD, smart terrain, or core lifecycle callbacks.

## Saves and Uninstallation

ZHOPA can cleanly leave a running game and prepare the next save for addon removal:

1. Load the save while ZHOPA is still installed and enabled.
2. Open MCM and turn off **Run ZHOPA ALIFE 2**.
3. Wait for the successful cleanup notification. If cleanup reports an error, keep the addon installed, reload the game, and retry.
4. Create a new manual save after cleanup succeeds.
5. Exit the game before disabling or removing the addon in MO2.

The switch immediately cancels managed tasks, removes service squads created by ZHOPA, clears ZHOPA fields from squads and script storage, unregisters its callbacks, and restores runtime-patched functions where no later addon has replaced them. While disabled, ZHOPA remains dormant; enabling it again rebuilds its runtime from the current world state.

Cleanup cannot reverse events that already changed the world, including deaths, spawned or collected items, faction relations changed by other systems, zombification, or completed migration. It does not migrate SISKI/ZHOPA1 saves. Do not continue playing after a BusyHands warning; reload a save or return to the main menu.

## Verification and Debugging

Enable `debug_hud_enabled` in MCM. Managed squad markers will appear on the PDA map; their tooltips show task, target, smart, reason, and last result. This mode is intended for diagnostics and can reveal otherwise hidden simulation behavior.

Additional diagnostic scripts live in `debugscripts`. They are not part of a normal user installation and are enabled only for focused subsystem testing.

## Documentation

- [Architecture document](docs/zhopa_alife_2_design_document_en.md)
- [Архитектурный документ](docs/zhopa_alife_2_design_document.md)
- [Function reference](docs/zhopa_alife_2_function_reference_en.md)
- [Changelog](changelog_en.md)
- [Список изменений](changelog_ru.md)

## Development

Before changing behavior, look for a vanilla extension point first. New subsystems must respect the shared readiness barrier, register and unregister their own callbacks, implement the master-disable cleanup contract, avoid broad scans in hot paths, and persist only serializable values. New runtime patches must retain their original function and be restorable. A full override requires a documented reason; `axr_trade_manager.script` is the current intentional exception.

## License

[MIT](LICENSE), Copyright (c) 2026 qkff99.
