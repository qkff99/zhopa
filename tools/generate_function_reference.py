#!/usr/bin/env python3
"""Generate the Z.H.O.P.A. ALIFE 2.0 function reference from Lua scripts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


LOCAL_FUNCTION_RE = re.compile(r"^\s*local\s+function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(([^)]*)\)")
FUNCTION_RE = re.compile(r"^\s*function\s+([A-Za-z_][A-Za-z0-9_]*(?:[.:][A-Za-z_][A-Za-z0-9_]*)*)\s*\(([^)]*)\)")
ASSIGN_FUNCTION_RE = re.compile(
    r"^\s*(?:local\s+)?([A-Za-z_][A-Za-z0-9_]*(?:[.:][A-Za-z_][A-Za-z0-9_]*)*)\s*=\s*function\s*\(([^)]*)\)"
)

SCRIPT_HOOKS = {
    "actor_on_first_update",
    "actor_on_update",
    "on_game_start",
    "on_game_load",
    "on_mcm_load",
    "save_state",
    "load_state",
    "on_option_change",
}

SCRIPT_ROLES = {
    "zhopa2_artifacts.script": "artifact target selection, real/virtual artifact handling, and online/offline pickup flow",
    "zhopa2_bootstrap.script": "minimal startup bridge into the runtime patch orchestrator",
    "zhopa2_cfg.script": "configuration, MCM defaults, faction aliases, and blacklist access",
    "zhopa2_debug_hud.script": "debug PDA map markers and squad status hints",
    "zhopa2_economy.script": "online/offline trade policy, sellable inventory scanning, virtual cargo, and trade routing",
    "zhopa2_index.script": "event-driven SIMBOARD buckets for squads, smarts, artifacts, ownership, and trade smart flags",
    "zhopa2_loot.script": "online loot integration, offline virtual loot accounting, artifact cargo, and loot-loop protection",
    "zhopa2_mcm.script": "MCM menu registration and settings bridge",
    "zhopa2_mcm_schema.script": "MCM option schema and defaults",
    "zhopa2_memory.script": "serializable squad state, cargo, virtual loot, virtual money, and save/load helpers",
    "zhopa2_perception.script": "target discovery, weighted candidate selection, path levels, and faction/blacklist checks",
    "zhopa2_revenge.script": "revenge event detection, responder selection, and actor hostility scope",
    "zhopa2_runtime_patches.script": "chain-friendly runtime patching of vanilla/pack scripts",
    "zhopa2_service_fillers.script": "base service NPC detection, adoption, and filler spawning",
    "zhopa2_story_north_migration.script": "story-gated northern migration task selection and recovery",
    "zhopa2_story_psy_watchdog.script": "story-gated psi-level squad conversion into zombied squads",
    "zhopa2_tasks.script": "task constants, task FSM, assignment, completion, and fallback rules",
    "zhopa2_topology.script": "level topology, neighbor levels, and route helpers",
}


def rel_display(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def clean_params(params: str) -> str:
    return " ".join(params.strip().split())


def classify(name: str, declaration_kind: str, is_local: bool) -> str:
    if name.startswith("M."):
        return "module export"
    if name in SCRIPT_HOOKS:
        return "script hook/global"
    if declaration_kind == "assignment" and not is_local:
        return "assigned wrapper"
    if "." in name or ":" in name:
        return "assigned wrapper"
    return "local helper" if is_local else "script hook/global"


def topic_from_filename(path: Path) -> str:
    name = path.name.replace("zhopa2_", "").replace(".script", "").replace("_", " ")
    return name or path.stem


def readable_name(name: str) -> str:
    short = name.split(".")[-1].split(":")[-1]
    return short.replace("_", " ")


def describe(name: str, path: Path) -> str:
    lower = name.lower()
    topic = topic_from_filename(path)

    if lower.startswith("m."):
        lower = lower[2:]
    if lower in SCRIPT_HOOKS:
        return f"Runtime hook for {topic} lifecycle integration."
    if "runtime_ready" in lower:
        return "Checks the shared runtime readiness barrier before context-dependent work."
    if "cfg_bool" in lower:
        return "Reads a boolean ZHOPA setting with a safe default fallback."
    if "cfg_num" in lower:
        return "Reads a numeric ZHOPA setting with a safe default fallback."
    if "cfg_" in lower or "config" in lower or "setting" in lower:
        return f"Reads or normalizes configuration data for the {topic} subsystem."
    if "debug" in lower or "diag" in lower or "printf" in lower or "log" in lower:
        return "Formats or emits debug/diagnostic output, normally gated by debug settings."
    if "object_id" in lower:
        return "Extracts a stable numeric id from supported object/id values."
    if "object_section" in lower or "section_name" in lower or lower.endswith("section"):
        return "Resolves a safe section name for runtime classification."
    if "online_object" in lower:
        return "Resolves an online game object through db.storage or level lookups."
    if "alife" in lower or "server_object" in lower or "resolve_" in lower:
        return "Safely resolves an ALife/server-side object or runtime reference."
    if "virtual_loot" in lower:
        return "Reads, writes, sells, clears, or materializes serializable virtual loot cargo."
    if "virtual_money" in lower:
        return "Reads, writes, spends, or materializes serializable virtual squad money."
    if "artifact" in lower or "artefact" in lower:
        return "Handles artifact task state, bucket registration, cargo, pickup, or retargeting."
    if "loot" in lower or "corpse" in lower or "gather" in lower or "pickup" in lower:
        return "Handles loot target selection, pickup integration, accounting, or anti-loop cleanup."
    if "trade" in lower or "sell" in lower or "buy" in lower or "money" in lower:
        return "Handles NPC trade policy, pricing, route selection, or payment accounting."
    if "squad" in lower or "member" in lower:
        return "Handles squad lookup, membership, task state, or squad-level accounting."
    if "smart" in lower or "job" in lower or "base" in lower:
        return "Handles smart-terrain lookup, job selection, base ownership, or service logic."
    if "hunt" in lower or "revenge" in lower or "hostile" in lower or "enemy" in lower:
        return "Handles hostile target selection, revenge state, or pursuit behavior."
    if "story" in lower or "psy" in lower or "north" in lower or "migration" in lower or "zomb" in lower:
        return "Handles story-gated squad events, conversion, migration, or recovery."
    if "blacklist" in lower or "valid" in lower or "safe" in lower or "can_" in lower or "_ok" in lower:
        return "Validates safety gates and controlled fallback conditions."
    if "level" in lower or "vertex" in lower or "route" in lower or "distance" in lower or "position" in lower:
        return "Resolves level, graph, route, distance, or position data."
    if "patch" in lower or "wrap" in lower or "original" in lower:
        return "Installs or supports a chain-friendly runtime patch around vanilla behavior."
    if "save" in lower or "load" in lower or "memory" in lower or "state" in lower:
        return "Reads, writes, clears, or migrates serializable runtime state."
    if "timer" in lower or "cooldown" in lower or "now" in lower:
        return "Calculates time, cooldown, or tick-throttling values."
    if "weight" in lower or "pick" in lower or "select" in lower or "candidate" in lower:
        return "Builds, scores, or selects candidates for weighted simulation decisions."
    if "clear" in lower or "reset" in lower or "cleanup" in lower or "release" in lower:
        return "Clears transient state, reservations, or stale runtime references."
    if "add" in lower or "remove" in lower or "register" in lower or "unregister" in lower:
        return "Maintains indexed runtime state by adding or removing entries."
    if "name" in lower or "format" in lower or "text" in lower:
        return "Formats names or display text for diagnostics and UI output."
    return f"Supports {topic} subsystem behavior."


def parse_functions(path: Path) -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    text = path.read_text(encoding="utf-8", errors="replace").splitlines()
    for line_no, line in enumerate(text, start=1):
        match = LOCAL_FUNCTION_RE.match(line)
        if match:
            name, params = match.groups()
            entries.append(
                {
                    "line": line_no,
                    "name": name,
                    "params": clean_params(params),
                    "kind": classify(name, "declaration", True),
                    "description": describe(name, path),
                }
            )
            continue

        match = FUNCTION_RE.match(line)
        if match:
            name, params = match.groups()
            entries.append(
                {
                    "line": line_no,
                    "name": name,
                    "params": clean_params(params),
                    "kind": classify(name, "declaration", False),
                    "description": describe(name, path),
                }
            )
            continue

        match = ASSIGN_FUNCTION_RE.match(line)
        if match:
            name, params = match.groups()
            is_local = line.lstrip().startswith("local ")
            entries.append(
                {
                    "line": line_no,
                    "name": name,
                    "params": clean_params(params),
                    "kind": classify(name, "assignment", is_local),
                    "description": describe(name, path),
                }
            )
    return entries


def markdown_escape(value: object) -> str:
    text = str(value if value is not None else "")
    return text.replace("\\", "\\\\").replace("|", "\\|")


def write_section(lines: list[str], root: Path, title: str, files: list[Path]) -> int:
    total = 0
    lines.append(f"## {title}")
    lines.append("")
    for path in files:
        entries = parse_functions(path)
        total += len(entries)
        lines.append(f"### `{rel_display(path, root)}`")
        lines.append("")
        lines.append(f"Role: {SCRIPT_ROLES.get(path.name, topic_from_filename(path) + ' diagnostics or helpers')}.")
        lines.append("")
        if not entries:
            lines.append("No named functions detected.")
            lines.append("")
            continue
        lines.append("| Line | Function | Kind | Parameters | Description |")
        lines.append("| ---: | --- | --- | --- | --- |")
        for entry in entries:
            lines.append(
                "| {line} | `{name}` | {kind} | `{params}` | {description} |".format(
                    line=entry["line"],
                    name=markdown_escape(entry["name"]),
                    kind=markdown_escape(entry["kind"]),
                    params=markdown_escape(entry["params"]),
                    description=markdown_escape(entry["description"]),
                )
            )
        lines.append("")
    return total


def generate(project_root: Path) -> str:
    runtime_files = sorted((project_root / "gamedata" / "scripts").glob("*.script"))
    debug_files = sorted((project_root / "debugscripts").glob("*.script"))
    runtime_count = sum(len(parse_functions(path)) for path in runtime_files)
    debug_count = sum(len(parse_functions(path)) for path in debug_files)

    lines: list[str] = [
        "# Z.H.O.P.A. ALIFE 2.0 Function Reference",
        "",
        "[Architecture document](zhopa_alife_2_design_document_en.md)",
        "",
        "This document is generated from the current ZHOPA ALIFE 2.0 Lua sources. It lists named function declarations and named function assignments found in runtime scripts under `gamedata/scripts` and diagnostic scripts under `debugscripts`. Anonymous inline closures, for example `pcall(function() ... end)`, are intentionally excluded because they have no standalone callable contract.",
        "",
        "Regenerate it with:",
        "",
        "```bash",
        "python tools/generate_function_reference.py",
        "```",
        "",
        f"- Runtime script functions: {runtime_count}",
        f"- Diagnostic script functions: {debug_count}",
        f"- Total documented named functions: {runtime_count + debug_count}",
        "",
        "## Reading Notes",
        "",
        "- **Kind** describes how the function is declared: local helper, module export, script hook/global, or assigned wrapper.",
        "- **Parameters** are copied from the declaration line and may omit internal closures or later vararg handling.",
        "- **Description** is a short generated operational summary based on the function name and module role. The Lua source remains the final authority for exact behavior and edge cases.",
        "",
    ]

    write_section(lines, project_root, "Runtime Scripts", runtime_files)
    write_section(lines, project_root, "Diagnostic Scripts", debug_files)
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Path to projects/zhopa_alife_2",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output markdown path. Defaults to docs/zhopa_alife_2_function_reference_en.md.",
    )
    args = parser.parse_args()

    project_root = args.project_root.resolve()
    output = args.output or (project_root / "docs" / "zhopa_alife_2_function_reference_en.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(generate(project_root), encoding="utf-8", newline="\n")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
