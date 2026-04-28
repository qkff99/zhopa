#!/usr/bin/env python3
"""
Create a game-ready release folder from the obfuscated sidecar bytecode.

The working source files stay in gamedata/scripts/*.script. The release folder
gets bytecode under the normal .script names, because XRay loads .script files.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SIDECAR_SCRIPTS = {
    Path("gamedata/scripts/zhopa.script"): Path("gamedata/scripts/zhopa.script.ljbc"),
    Path("gamedata/scripts/zhopa_mcm.script"): Path("gamedata/scripts/zhopa_mcm.script.ljbc"),
}

STUB_SOURCE = """local n = script_name()
local root = getFS():update_path("$game_scripts$", "")
local f, err = loadfile(root .. n .. ".script.ljbc")
if not f then error(err) end
if setfenv then setfenv(f, getfenv(1)) end
return f()
"""


def ensure_inside(child: Path, parent: Path) -> None:
    child = child.resolve()
    parent = parent.resolve()
    if child != parent and parent not in child.parents:
        raise RuntimeError(f"refusing to remove outside release root: {child}")


def should_skip(relative_path: Path) -> bool:
    if relative_path in SIDECAR_SCRIPTS:
        return True
    return False


def copy_tree(project_root: Path, output_root: Path) -> None:
    source_root = project_root / "gamedata"
    for source in source_root.rglob("*"):
        if not source.is_file():
            continue
        relative = source.relative_to(project_root)
        if should_skip(relative):
            continue
        destination = output_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def copy_sidecars_and_stubs(project_root: Path, output_root: Path) -> None:
    for destination_relative, sidecar_relative in SIDECAR_SCRIPTS.items():
        sidecar = project_root / sidecar_relative
        if not sidecar.exists():
            raise FileNotFoundError(f"missing sidecar: {sidecar}")
        stub_destination = output_root / destination_relative
        sidecar_destination = output_root / sidecar_relative
        stub_destination.parent.mkdir(parents=True, exist_ok=True)
        stub_destination.write_text(STUB_SOURCE, encoding="ascii", newline="\n")
        shutil.copy2(sidecar, sidecar_destination)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path("dist/zhopa_obfuscated"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_root = args.project_root.resolve()
    output_root = args.output
    if not output_root.is_absolute():
        output_root = project_root / output_root
    output_root = output_root.resolve()

    dist_root = (project_root / "dist").resolve()
    ensure_inside(output_root, dist_root)
    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    copy_tree(project_root, output_root)
    copy_sidecars_and_stubs(project_root, output_root)
    print(f"release: {output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
