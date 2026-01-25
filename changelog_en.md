## 0.6.2 — 2026-01-26

### Fixes
- Fixed a rare `pure virtual function call` crash in Debug HUD by removing `:name()`/`alife_object()` calls on potentially stale server objects.
- Fixed post-trade “sticking to a point”: force-clears `desired_position/desired_direction` and handles `FAILED/NO_SINK` with leader release/cleanup.
- Fixed selling rules: NPCs no longer sell active/equipped weapons/armor and will not sell their last gun (ensures at least one `wpn_` remains).
- Fixed a regression that could break offline updates and memory dumps: `safe_run` now uses Lua 5.1 `unpack` and preserves `nil` args; dump hotkey no longer relies on raw `ui_mcm.get`.

### Performance
- Buffered file logging to reduce `io.open/io.close` overhead via batched writes.
- Added a TTL cache for MCM reads (`get_config`) to reduce frequent polling cost.
- Optimized squad level resolution during `sync_to_memory` by caching the level name per `m_game_vertex_id`.
- Optimized Debug HUD: skip non-current-level squads, avoid map hint updates when unchanged, add cooldown on `try_register_brain`.
- Tuned global artifact scan: fewer empty steps and larger processing blocks.

### Stability / Diagnostics
- Added `xpcall + debug.traceback` for core SISKI updates (brain/debug/scanner) and `brain:update()`: errors are logged with full traceback and should not crash the game due to SISKI.
- Added safety guards for memory `perf` caches (auto-reset on abnormal growth).

## 0.6.1 — 2026-01-25

### Fixes
- MOVE now reliably binds squads to a smart via `assign_squad_to_smart` even when SIMBOARD lacks a stable `name -> id` lookup (added a unified resolver via SIMBOARD → intel/memory).
- Reduced MOVE “stalls”: added progress tracking by distance-to-target, periodic smart rebind when stuck, and a fallback degradation to `MOVE_TO_POS` after prolonged stagnation.
- Improved `MOVE_TO_POS` robustness: added staged degradation (retry / smart-based fallback) instead of silent force-complete; for offline squads `MOVE_TO_POS` is converted into smart-based MOVE to the nearest smart.
- Retargeting policy updated: no longer exclusive to `af_hunter` — urgency/priority are considered and a cooldown prevents target “thrashing” (separate tuning for online/offline).
- Trading stability fix: removed inventory item removal via release when no trader NPC is found (source of `SV: can't find child ... of parent ...` warnings); selling now uses safe transfers to a live “sink” NPC at the smart, or is deferred if none exists.

### Added
- Implemented a full NPC-to-NPC trading system.
- Cross-level routing: if a target smart is on another level, the squad first moves to the nearest level changer on the current level (`MOVE_TO_POS`), then automatically queues the final smart-based task.
- Movement diagnostics: added stuck/timer metrics for MOVE and `MOVE_TO_POS` degradation stages into memory and exposed them in reporter/debug output, including “retarget age”.
