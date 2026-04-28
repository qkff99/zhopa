# ZHOPA ALIFE

# [Русский](README.md)
## [Changelog RU](changelog_ru.md)
## [Changelog EN](changelog_en.md)

## Description
ZHOPA is a modular ALife layer for Anomaly 1.5.3 that drives simulation squads through a decentralized runtime model.

Gameplay-wise ZHOPA:
- assigns squad tasks and targets;
- runs a stalker task FSM and a separate mutant FSM;

## Settings
Settings are available through `gamedata/configs/zhopa_settings.ltx` and MCM -> `ZHOPA`.

Current user-facing groups:
- general toggles;
- stalker tasks and targeting;
- mutant behavior;
- trade and fast trading;
- base/dynamic/service fillers;
- loot;
- cache/debug/logging knobs that are still used by the current runtime.

## Compatibility
- Anomaly 1.5.3 + Modded Exes.
- Target environment: vanilla ALife + modpacks that keep the core engine callbacks and `SIMBOARD` intact.
- Combat AI mods such as Redone AI / Enhanced Combat AI usually do not conflict directly, because ZHOPA operates at the simulation-squad layer rather than replacing all online combat behavior.
