# Z.H.O.P.A. ALIFE 2.0

[Russian](README.md)
[Changelog](changelog_en.md)

**Zone Hostile Operations & Population AI (Z.H.O.P.A.) ALIFE 2.0** is a modular ALife layer for S.T.A.L.K.E.R. Anomaly 1.5.3 + Modded Exes.

The addon works on top of SIMBOARD, smart terrain, and squad update: it chooses squad tasks, keeps memory, adds economy, looting, hunting, artefacts, dynamic base ownership, and some story reactions. Vanilla still owns movement, smart jobs, online/offline transitions, and core combat behavior.

## What It Does

- Assigns stalker squads exploration, smart population, patrol, rest, hunt, revenge, trade, and artefact tasks.
- Gives mutants a separate task pool: roaming, patrol, hunt, and rest.
- Updates hunt targets by their real online/offline position, so the target can be pursued across the whole Zone with level transitions during the chase.
- Extends online looting and adds offline looting of real items.
- Adds NPC economy: real item sales, supply purchases, trade routes, and offline trade.
- Adds artefact logic: real artefacts, virtual offline artefacts, online pickup with a selected NPC and detector animation.
- Tracks dynamic base ownership and service NPCs for suitable bases. Killed traders can be replaced after an emission by new ones from the faction that currently owns the smart.
- Adds story systems: psi-level squad zombification and northern migration after the Brain Scorcher is disabled. This works only if story mode was enabled when the new game was created.
- Provides a debug HUD and diagnostic scripts for tasks, indexes, trade, looting, and artefacts. Diagnostic scripts are kept in the repository and will not be included in release builds; they are mainly for bug hunting and development.

## Main Systems

### Squad Tasks

Current tasks: `REST`, `EXPLORE`, `FORCE_EXIT`, `POPULATE`, `BASE_CAMPING`, `PATROL`, `NIGHT_REST`, `ARTEFACT`, `TRADE`, `HUNT`, `REVENGE`, `STORY_NORTH_MIGRATION`.

Some tasks are selected by weight, while others are assigned as direct reactions. For example, `REVENGE` comes from a revenge event, `NIGHT_REST` interrupts stalkers at night, `BASE_CAMPING` binds a squad to a base, and `STORY_NORTH_MIGRATION` is owned by the story module.

### Economy and Trade

Squads can sell excess artefacts, weapons, outfits, ammo, medicine, food, and other loot. The squad leader can trade for the whole squad. Offline trade sells serializable virtual loot cargo and uses virtual squad money so long saves do not inflate the engine object id pool.

NPC sale income is controlled by `npc_sell_price_multiplier`; the default value is `0.2`.

### Looting

Online looting works on top of vanilla pickup behavior and tries to preserve normal NPC logic. Offline looting records bounded virtual cargo after offline combat; that cargo is sold by trade or materialized only when an online NPC death needs real items. The system also clears rejected loot targets so NPCs do not loop forever on one corpse or item.

### Artefacts

Real artefacts are registered in indexes and assigned to a suitable smart terrain. The offline economy can use virtual artefacts generated from anomaly settings. If a real artefact is available, it is preferred over a virtual one.

### Story Events

The psi watchdog can convert unprotected stalker squads on psi levels into zombified squads. Northern migration after the Brain Scorcher sends a selected percentage of eligible squads toward northern levels.

Both systems should run only in story mode and must not fire in freeplay.

## Settings

Settings are available through:

- `gamedata/configs/zhopa2_settings.ltx`
- MCM -> `ZHOPA ALIFE 2`

Main MCM groups:

- core systems;
- economy and helper systems;
- story events;
- stalker simulation;
- task weights;
- task timing;
- combat and target following;
- mutant simulation.

## Installation

With Mod Organizer 2:

1. Make sure old ZHOPA/SISKI/REZNYA versions are disabled or removed, and disable incompatible mods listed below.
2. `MO2` -> `File` -> `Install Mod...` -> select the downloaded archive -> press `OK`.

Manual install:

1. Copy `gamedata` into the Anomaly root.
2. Verify that files landed under `gamedata/scripts`, `gamedata/configs`, and `gamedata/configs/text`.

What is better to disable in your build:

- `Alife Plus` must be disabled. It is not compatible with `ZHOPA`.
- Mods such as `NPC Loot claim` and `NPC stop looting dead bodies`. In `Useful Idiots` settings, disable the option that allows only companions to search bodies. A large part of NPC economic interaction depends on NPC inventory contents, so loot restrictions will interfere. This is not mandatory; if you do not like ZHOPA's looting or economy, you can disable those systems in MCM.
- `xcvb's Guards Spawner` does not block ZHOPA, but it will constantly spam the log because ZHOPA takes over its squads.

How to check that the addon is working:

- Enable the debug HUD in the addon MCM. Squad markers should appear on the PDA map. Hovering over a squad should show a tooltip with the squad's current target. The debug HUD is mainly for debugging and is not recommended for normal play, because it can spoil the natural feel of the simulation. Use it if you want to see how the system is working.

## Compatibility

- Target version: Anomaly 1.5.3 + Modded Exes.
- Tested on `G.A.M.M.A 0.9.5/0.9.4` and `Anthology 2.1`.
- Compatible with `ZCP`, all `REDONE` mods, and `New Levels`.
- Not compatible with `Alife Plus`, and it never will be.
- Mods that fully replace `sim_squad_scripted`, `smart_terrain`, `sim_board`, `xr_gather_items`, `xr_corpse_detection`, or related callbacks may conflict.
- Combat AI mods are usually less risky if they do not break SIMBOARD, smart terrain, or core callbacks.

## Debugging

Enable `debug_hud_enabled` to inspect runtime behavior. It displays squad state on map markers and enables additional diagnostic console output.

Additional diagnostic scripts live in `debugscripts`. They are not meant to be part of a normal user install and are intended for testing specific subsystems.

## Documentation

- [Architecture document](docs/zhopa_alife_2_design_document_en.md)
- [Russian architecture document](docs/zhopa_alife_2_design_document.md)
- [Function reference](docs/zhopa_alife_2_function_reference_en.md)

## Development Notes

Before changing behavior, check whether there is a vanilla extension point or an existing runtime patch. New systems should:

- respect the shared runtime readiness barrier;
- register their own callbacks;
- avoid global scans in hot paths;
- store only serializable values in saves;
- update MCM, localization, and documentation when adding user-facing settings.

