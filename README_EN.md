# SISKI ALIFE (System for Intelligent Squad Kinesis & Intellect)

## Description
SISKI is a mod for Anomaly 1.5.3. It is a modular simulation and “brain” system for simulation squads (sim_squads) in Anomaly. The mod attaches autonomous behavior to squads via a task queue, distributes targets, and keeps the Zone lively through spawning and background activities.

## Concept Revision
You flooded me with reports about errors, bugs, busy hands, etc., and I realized one simple truth: nobody plays plain Anomaly without mods. So I thoroughly revised the project, cut out ABSOLUTELY EVERYTHING except the core mechanic, and wrapped ABSOLUTELY ALL calls, callbacks, and similar engine interactions with safety checks. I also started profiling using special utilities. As a result, I significantly improved stability, performance, compatibility, and crash resistance. Below will be a list of key changes compared to the previous version.

## Key Changes in SISKI ALIFE 0.6
- Removed Epic Fight and Enhanced AI modules that controlled NPC behavior in combat.
- Removed the Ambient module that pushed stalkers to play more animations around campfires.
- Removed the Relations module that patched NPC relations to avoid massacres in quest locations (e.g., Military and Rookies on Cordon). As it turned out, that patch often crashed the engine.
- Improved the task management logic for sim squads: stalkers will move more on the active level, offline, and also travel to other levels to explore them.
- Added throttling and other optimizations everywhere possible to reduce load, micro-stutters, and improve performance (this does not mean you can spawn 100 stalkers per level — it will still kill your PC).
- Protected all accesses to alive/non-alive objects to reduce red console spam and lower the chance of crashes when processing invalid objects from “random mods”.
- Improved debugging methods: spread logging through the code and added DEV TOOLS support for profiling (regular players don’t need this).
- Reworked spawner mechanisms: added fallbacks and campfire spawning to avoid overcrowding bases at the start of a new game.
- Expanded the list of banned sections/smarts/factions/levels in `siski_settings.ltx`.
- Added ALIFE to the name on this page.

## Settings
Settings are available via `siski_settings.ltx` and MCM (Mod Configuration Menu) -> SISKI.
Default settings are neutral for gameplay and hardware-friendly. If you don’t know what you’re doing, don’t touch anything.
If you previously installed older versions of SISKI or REZNYA, after installing the new version you must reset the mod settings in MCM.
- Story protection (NPC -> trader) — turns all NPCs with a story_id into traders. This is a bulletproof way to protect them from simulation, but some NPCs may have a story_id when they shouldn’t, which can break your playthrough.
- Section protection (NPC -> trader) — a safer way to protect traders and important characters without breaking the story. Protects only the pre-listed sections from `siski_settings.ltx` (currently ~99% of vanilla Anomaly traders and important NPCs). Using both options at the same time makes no sense — pick one.
- Faction sliders in the population control section define how many squads the spawner will spawn for that faction on each level. For example, if you set 10, the spawner will spawn 10 squads of that faction per location.

## Features
- Squad “brains”: task queue, states, execution of MOVE/MOVE_TO_POS and other actions.
- Strategic layer: tasks like base reinforcement and campfire patrol, with per-level limits.
- Faction lore behavior: background tasks distributed to neighboring levels with anti-stacking on the current location.
- Population control: target limits per faction with safe spawning at smarts/campfires/level changers.
- Special squads (AF Hunters): a dedicated artifact hunter class with configurable per-level amount (currently does almost nothing; I’ll improve it later).
- Protector: story NPC protection and protection by section list (traders/technicians/medics/guides) from wandering off their roles.
- Optional: “ALife for vanilla squads” — attach SISKI brains to squads spawned by the base game/other mods (restricted by a whitelist of sections).
- Stalkers loot: they pick up anything that’s lying around (will be improved later).
- Debugging and reports: extended logging, HUD diagnostics, and an HTML simulation dashboard.

## How to Install

## Compatibility
- Anomaly 1.5.3 + Modded Exes
- Should be compatible with most Anomaly 1.5.3 + Modded Exes modpacks at the moment.
  - Please do not report crashes/bugs if you tested in conditions different from what is described above.
- I removed everything I could to avoid conflicts with popular mods, crashes, and busy hands.
- Redone AI, Enhanced Combat AI and similar mods modify NPC combat behavior and do not affect the simulation, so they should be compatible out of the box — but no promises.

## Important
- Some people claimed the mod “breaks the game” by writing logs into `bin/overwrite`. Logs are just text files — don’t listen to them. Logs are needed to understand when something goes wrong. With debug disabled, logs may still be created, but they won’t be filled.
- If you have lots of freezes or low FPS, use AOEngine and ALAO, disable population control and enable ALife for vanilla squads. This way the mod will work only with vanilla spawns or with your modpack’s spawner (zcp, etc.).
- Comments like “mod is trash, not immersive, breaks the game” are ignored. The mod’s main goal is to make the Zone chaotic and unpredictable in a good way. Don’t like it — don’t play it.
- You can use this mod in your modpacks and modify its code however you want — I believe SISKI should be open and easy to access. But I’m not going to ship a billion micro-patches for every separate modpack by some “random guy”. Still, I’m open to communication: ping me in AOEngine Discord with @qkff99. If I’m not busy, I’ll help with setup, explain how things work, and maybe help make a compatibility patch if possible.

