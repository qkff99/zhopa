# Z.H.O.P.A. ALIFE 2.3

[Русский](README.md) | [Changelog](changelog_en.md) | [Architecture](docs/zhopa_alife_2_design_document_en.md) | [Function reference](docs/zhopa_alife_2_function_reference_en.md)

[![DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/qkff99/zhopa)

> **Zone Hostile Operations & Population AI** - a modular ALife extension for S.T.A.L.K.E.R. Anomaly 1.5.3 + Modded Exes.

Z.H.O.P.A. makes life in the Zone more connected: squads receive purposeful tasks, pursue moving targets, collect loot and artefacts, trade, occupy bases, and react to story events. Movement, smart jobs, online/offline transitions, pathfinding, and core combat behavior remain under game control.

## Features

| Subsystem | Behavior |
| --- | --- |
| Squad tasks | Stalkers explore the Zone, populate smart terrains, patrol, rest, hunt, take revenge, collect artefacts, travel to trade, and perform trader contracts. Mutants use a separate task pool. |
| NPC quests | Traders publish document, clearing, occupation, hunt, and delivery jobs. Squads travel to the giver and objective, use real quest items, and return for payment; the flow works online and offline. |
| Task balance | Valid task-target pairs are weighted by squad strength, local faction pressure, and optional faction preferences. Story and safety tasks remain outside this random selection. |
| Hunt and revenge | Targets are tracked by their actual squad position, including level transitions. Actor revenge makes only the assigned squad hostile, not its entire faction. |
| Dialogue and travel | A managed squad commander reports the current and previous task, including the NPC-quest type, and shows an area/smart destination card. If the squad is moving, the actor can travel to its actual destination with time advancement, optional payment, and Story Mode psi restrictions. |
| Loot | Offline loot is bounded virtual cargo and consumes no engine object IDs. Online native loot can bypass global pack bans and optionally protect player/companion victims; ARTEFACT is independent. |
| Economy | The leader trades for the whole squad, sells real and virtual goods, pools member money, and buys basic supplies. |
| Artefacts | Real and virtual offline artefacts are supported, including smart assignment and online pickup by a selected NPC with detector animation. |
| Bases and services | The addon tracks base vacancies and recruits existing local NPCs as traders, technicians, medics and cooks/barmen, without spawning new NPCs. |
| Story events | Story mode enables psi zombification and northern migration after the Brain Scorcher shutdown. These systems do not run in freeplay. |

Current tasks: `REST`, `EXPLORE`, `FORCE_EXIT`, `POPULATE`, `DYNAMIC_BASE_POPULATE`, `BASE_CAMPING`, `PATROL`, `NIGHT_REST`, `ARTEFACT`, `TRADE`, `QUEST`, `HUNT`, `REVENGE`, `STORY_NORTH_MIGRATION`.

## Guard Refill

“Service Filler: replenish guards” is enabled by default. Once all traders, technicians, medics and cooks/barmen across the base are present, suitable arriving NPCs leave their squads and become permanent guards. The owner faction has priority, followed by non-hostile factions. Native guards remain in place and physical posts are not duplicated. Detached guards do not roam or consume BASE_CAMPING capacity; the remaining donor squad continues its tasks. Combat and surge sheltering do not cancel the permanent assignment. Turning off Guard Refill stops new recruitment; disabling ZHOPA entirely returns recruits to ordinary squads. Diagnostics: `zhopa2_guard_refill.audit_level()`.


## Trade and Economy

- Online deals run through a vanilla trade customer job and the SISKI-derived `axr_trade_manager.script`.
- The smart job selects the actual seller through `npc_info.job.seller_id`; ZHOPA does not replace it with a preselected NPC.
- Only traders and barmen are regular trade providers. Medics, mechanics, and faction leaders are not treated as ordinary sellers.
- A mechanic visit can be triggered only by a real `i_upgrade` item held by the NPC. Ordinary supply purchases do not create synthetic tech intent.
- Offline deals sell serializable virtual cargo and use virtual squad money.
- `npc_sell_price_multiplier` controls NPC sale income; the default value is `0.2`.
- A quest interaction reuses the customer job and animation but exits before a monetary deal. Every service result immediately reselects the NPC's normal smart job and remains covered by the service doctor.

## Service Base Settlement

Compound bases are defined in `gamedata/configs/zhopa2_base_clusters.ltx`. They share ownership and population; squad capacity and service jobs remain local to each smart. The filler can recruit a donor from another smart of the same base. Membership covers vanilla levels and three New Levels maps; absent maps are skipped.

Roaming considers the population of each entire level: living stalkers of all factions and incoming squads. Less populated levels gain weight among nearby and distant reachable destinations, while distance and danger still matter. The population multiplier is bounded between 0.5 and 2. The existing MCM option is now named "Faction and level population balance". Settlement capacity uses `max_population` squad slots identically online and offline, regardless of loaded NPC job tables.

A living local player counts as one member of their real faction at the nearest service-capable base within its arrival radius. Clear a base and wait for suitable squads: the filler separates existing members to fill service vacancies. An emission is no longer required. Leaving before the recruitment check removes the player's presence; disguises do not change ownership faction.

Empty and sparsely occupied service bases gain weight for exploration, population and patrol routes. Night rest uses the bonus to adjust distance between equally crowded options. Empty bases admit any stalker faction, while occupied bases attract the owner's faction and non-hostile factions. Capacity includes incoming squads; ordinary base-tagged smarts without service jobs get no bonus. Together remote players are outside this feature's scope.

### Base Invitations

An empty service base also invites existing squads from its own level and all immediate neighboring levels. A compound base acts as one host. Service NPCs do not prevent an empty-base request; guards, regular stalkers, zombies and mutants count as residents. The player's true faction has priority over distance; selection uses faction relations without personal reputation or disguises.

The first wave invites one human squad friendly or neutral to the player and one hostile squad when available. An invitation closes rest or an eligible roaming task and routes the squad through `DYNAMIC_BASE_POPULATE`, followed by normal `BASE_CAMPING`. Quests, companions, combat, surge sheltering, ordinary `POPULATE` and existing camping remain protected. The other first-wave squad keeps traveling after the first arrives.

Reinforcements support the actual owner and remain peaceful with existing services and defenders. Demand accounts for living members and incoming squads; excess second-wave groups receive `REST`. Zombies and mutants participate in clashes and one finite support wave, but cannot take service or guard jobs; stalkers keep attempting to reclaim their bases. Partially depleted guards can also request help without a hostile first wave, at 40% occupancy or below by default.

The MCM **Base Invitations** group enables the system by default and controls task interruption, the hostile wave, zombie/mutant participation, guard thresholds and reinforcement size. Target occupancy affects invitation budgeting; Guard Refill continues filling available posts normally. Offline population uses living server NPCs: unknown data is not emptiness, and guard capacity comes from a remembered catalog or a bounded estimate until the level is visited. Diagnostics: `zhopa2_base_invitations.audit_level()`; `from_level` and `current_level` show where each invited squad started and where it is now.

## NPC Squad Quests

`zhopa2_npc_quests` supports five contract types: documents, base clearing, base occupation, hunting a specific squad, and delivery. A giver publishes up to three available jobs from its profile. Squads search their current level first and then traders on directly adjacent levels.

Online, the commander physically approaches the trader and plays the service animation. If this cannot be prepared safely or the level is offline, a one-minute simulation fallback completes the interaction at the smart. Documents and packages are real ZHOPA-owned quest items: the commander physically receives them online, while the server-side phase performs the equivalent step offline. Rewards are paid once into shared virtual squad money and then participate in the normal economy.

## Looting

The old managed online looter has been replaced with a narrow native-scheme patch. `loot_enabled` bypasses global game/pack bans, the exclusion distance around the player and extra detection-radius caps. Search uses NPC visual memory; movement, animations and loot transfer remain native. `ARTEFACT` retains its separate targeted pickup with approach, animation and acquired-artifact accounting.

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
3. Select the Z.H.O.P.A. ALIFE 2.3 archive and confirm installation.
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
- per-faction task switches and weights;
- debugging.

Task balance is enabled by default. Numeric tuning, level overrides, squad-strength overrides, and faction profiles are kept in `gamedata/configs/zhopa2_population_profiles.ltx`. The MCM **Faction Weights** tab uses global task settings by default; its master switch enables separate `QUEST`, `EXPLORE`, `POPULATE`, `PATROL`, `NIGHT_REST`, `HUNT`, `ARTEFACT`, and `TRADE` switches and weights for every human faction. Mutants and zombified squads keep their existing shared settings.

Squad dialogue and joint travel are controlled by `squad_dialogue_enabled`. Travel-time tuning remains LTX-only through `squad_travel_minutes_per_100m`; the default is 10 in-game minutes per 100 meters. Paid travel is enabled by default through `squad_travel_paid_enabled`: the base price is 1,000 RU per kilometer and the MCM `squad_travel_price_multiplier` ranges from `0.1` to `10`.

NPC squad quests are controlled by `npc_quests_enabled`; `stalker_quest_weight` sets their relative selection chance. Profiles, enabled types, slot counts, and reward ranges live in `zhopa2_npc_quests.ltx`; a trader smart can be excluded with `smart_name = disabled`.

The MCM key `loot_enabled` enables native online loot and defaults to off. The separate `loot_protect_player_kills` prevents searches of player/companion victims, including mutants; it defaults to off and requires online loot. New kill marks persist with their objects through save/load and level changes. The rule protects corpse searches, not loose ground items. `ARTEFACT` task pickup and offline loot accounting work independently of its value. After updating the addon, use MCM's **Reset to defaults** before changing options so the current recommended defaults take effect.

`debug_hud_enabled` controls all ZHOPA diagnostic prints and manual audits. With it off, only the readiness/warmup counter remains; no separate runtime-log files are created.

## Compatibility

| Status | Mods and builds |
| --- | --- |
| Tested | Vanilla Anomaly 1.5.3, G.A.M.M.A. 0.9.4/0.9.5, Anthology 2.1 |
| Compatible | ZCP, the REDONE family, New Levels |
| Incompatible | Alife Plus |
| Requires testing | Mods that fully replace `sim_squad_scripted`, `smart_terrain`, `sim_board`, `xr_gather_items`, `axr_trade_manager`, or related callbacks |

Additional notes:

- With `loot_enabled`, directly bound native checks bypass `NPC Stop Looting Dead Bodies`, Useful Idiots bans and external search wrappers. Our player-victim rule is controlled by `loot_protect_player_kills`. Complete script or planner-evaluator replacements require separate verification. Economy and offline loot accounting have separate MCM switches.
- `xcvb's Guards Spawner` does not block the addon, but it may write log messages about squads after ZHOPA begins managing them.
- Combat AI addons are usually safer as long as they do not replace SIMBOARD, smart terrain, or core lifecycle callbacks.

## Saves and Uninstallation

ZHOPA can cleanly leave a running game and prepare the next save for addon removal:

1. Load the save while ZHOPA is still installed and enabled.
2. Open MCM and turn off **Run ZHOPA ALIFE 2**.
3. Wait for the successful cleanup notification. If cleanup reports an error, keep the addon installed, reload the game, and retry.
4. Create a new manual save after cleanup succeeds.
5. Exit the game before disabling or removing the addon in MO2.

The switch immediately cancels managed tasks, returns recruited NPCs to ordinary squads and removes old spawned service squads, clears ZHOPA fields from squads and script storage, unregisters its callbacks, and restores runtime-patched functions where no later addon has replaced them. While disabled, ZHOPA remains dormant; enabling it again rebuilds its runtime from the current world state.

Cleanup cannot reverse events that already changed the world, including deaths, spawned or collected items, faction relations changed by other systems, zombification, or completed migration. It does not migrate SISKI/ZHOPA1 saves. Do not continue playing after a BusyHands warning; reload a save or return to the main menu.

## Verification and Debugging

Enable `debug_hud_enabled` in MCM. Managed squad markers will appear on the PDA map; their tooltips show task, target, smart, reason, and last result. This mode is intended for diagnostics and can reveal otherwise hidden simulation behavior.

Additional diagnostic scripts live in `debugscripts`. They are not part of a normal user installation and are enabled only for focused subsystem testing.

Service audits `zhopa2_service_recruitment.audit_level()` (also `zhopa2_recruit_trader_probe.audit_level()`) and guard audits `zhopa2_guard_refill.audit_level()` ship in the release and require no debug package.

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
