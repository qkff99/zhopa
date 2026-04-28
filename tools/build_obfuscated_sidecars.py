#!/usr/bin/env python3
"""
Build obfuscated LuaJIT sidecar bytecode for the zhopa runtime scripts.

The source .script files are left untouched. The generated files are written
next to them as .script.ljbc.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_INPUTS = (
    Path("gamedata/scripts/zhopa.script"),
    Path("gamedata/scripts/zhopa_mcm.script"),
)

BLACKLIST_TERMS = (
    "zhopa",
    "zhopa_mcm",
    "smart_service_slot_doctor",
    "board_index",
    "story_psy_watchdog",
    "story_events",
    "smart_tasks",
    "tasks_registry",
    "base_filler",
    "dynamic_bases",
    "service_filler",
    "fast_trading",
    "debug_hud",
    "axr_task_patch",
    "loot_patch",
    "on_game_start",
    "on_mcm_load",
    "_resolve",
    "_get_trade",
    "gamedata",
    ".script",
    "roocode",
)


VM_CONFIG = r"""
return {
  LuaVersion = "Lua51",
  VarNamePrefix = "",
  NameGenerator = "MangledShuffled",
  PrettyPrint = false,
  Seed = 1234567,
  Steps = {
    { Name = "EncryptStrings", Settings = {} },
    { Name = "Vmify", Settings = {} },
    { Name = "ConstantArray", Settings = { Threshold = 1, StringsOnly = true, Shuffle = true, Rotate = true, LocalWrapperThreshold = 0 } },
    { Name = "NumbersToExpressions", Settings = {} },
    { Name = "WrapInFunction", Settings = {} },
  },
}
"""


NOVM_CONFIG = r"""
return {
  LuaVersion = "Lua51",
  VarNamePrefix = "",
  NameGenerator = "MangledShuffled",
  PrettyPrint = false,
  Seed = 1234567,
  Steps = {
    { Name = "EncryptStrings", Settings = {} },
    { Name = "ConstantArray", Settings = { Threshold = 1, StringsOnly = true, Shuffle = true, Rotate = true, LocalWrapperThreshold = 0 } },
    { Name = "NumbersToExpressions", Settings = {} },
    { Name = "WrapInFunction", Settings = {} },
  },
}
"""


@dataclass(frozen=True)
class Toolchain:
    lua51: Path
    luajit: Path
    prometheus: Path


@dataclass(frozen=True)
class Segment:
    name: str
    source: str


@dataclass(frozen=True)
class BuiltChunk:
    name: str
    mode: str
    bytecode: Path


class BuildError(RuntimeError):
    pass


def run_process(
    args: list[str],
    *,
    cwd: Path | None = None,
    allow_fail: bool = False,
) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        args,
        cwd=str(cwd) if cwd else None,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0 and not allow_fail:
        command = " ".join(args)
        output = (result.stdout + result.stderr).strip()
        raise BuildError(f"command failed ({result.returncode}): {command}\n{output}")
    return result


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def first_existing(candidates: Iterable[Path | None]) -> Path | None:
    for candidate in candidates:
        if candidate and candidate.exists():
            return candidate.resolve()
    return None


def which_path(name: str) -> Path | None:
    found = shutil.which(name)
    return Path(found).resolve() if found else None


def find_luajit(explicit: str | None) -> Path:
    temp = Path(tempfile.gettempdir())
    temp_matches = sorted(
        temp.glob("xray-luajit-build-*/luajit-2/src/luajit.exe"),
        key=lambda p: p.stat().st_mtime if p.exists() else 0,
        reverse=True,
    )
    candidates: list[Path | None] = [
        Path(explicit) if explicit else None,
        Path(os.environ["LUAJIT_EXE"]) if os.environ.get("LUAJIT_EXE") else None,
        *temp_matches,
        Path(r"D:\roocode\testprojects\siski\siski_lite\.gitignore\src\3rd party\luajit-2\src\luajit.exe"),
        which_path("luajit.exe"),
        which_path("luajit"),
    ]
    found = first_existing(candidates)
    if not found:
        raise BuildError("LuaJIT 2.0.4 compiler was not found. Pass --luajit or set LUAJIT_EXE.")
    return found


def find_lua51(explicit: str | None) -> Path:
    candidates: list[Path | None] = [
        Path(explicit) if explicit else None,
        Path(os.environ["LUA51_EXE"]) if os.environ.get("LUA51_EXE") else None,
        Path(r"C:\Program Files (x86)\Lua\5.1\lua.exe"),
        which_path("lua5.1.exe"),
        which_path("lua5.1"),
        which_path("lua.exe"),
        which_path("lua"),
    ]
    found = first_existing(candidates)
    if not found:
        raise BuildError("Lua 5.1 was not found. Pass --lua51 or set LUA51_EXE.")
    return found


def find_prometheus(explicit: str | None) -> Path:
    temp = Path(tempfile.gettempdir())
    candidates: list[Path | None] = [
        Path(explicit) if explicit else None,
        Path(os.environ["PROMETHEUS_ROOT"]) if os.environ.get("PROMETHEUS_ROOT") else None,
        temp / "lua-obf-tools" / "Prometheus",
        Path("vendor/Prometheus"),
        Path("tools/Prometheus"),
    ]
    found = first_existing(candidates)
    if not found or not (found / "cli.lua").exists():
        raise BuildError("Prometheus was not found. Pass --prometheus-root or set PROMETHEUS_ROOT.")
    return found


def verify_toolchain(toolchain: Toolchain) -> None:
    version = run_process([str(toolchain.luajit), "-v"], cwd=toolchain.luajit.parent).stdout
    if "LuaJIT 2.0.4" not in version:
        print(f"warning: expected LuaJIT 2.0.4, got: {version.strip()}", file=sys.stderr)
    lua_version = run_process([str(toolchain.lua51), "-v"], allow_fail=True)
    if lua_version.returncode not in (0, 1):
        raise BuildError("Lua 5.1 executable did not start correctly.")


def patch_prometheus(source_root: Path, work_root: Path) -> Path:
    patched = work_root / "Prometheus-patched"
    shutil.copytree(source_root, patched)
    emit = patched / "src" / "prometheus" / "compiler" / "emit.lua"
    text = emit.read_text(encoding="utf-8")
    patched_text, count = re.subn(
        r"(?m)^\s*blocks\[id\]\s*=\s*block;\s*$",
        "            -- patched by build_obfuscated_sidecars.py: sparse id keys break table.sort",
        text,
    )
    if count != 1:
        raise BuildError(f"Prometheus emit.lua patch did not match exactly once, matched {count}")
    emit.write_text(patched_text, encoding="utf-8", newline="\n")
    return patched


def find_long_bracket_end(source: str, start: int) -> tuple[int, str] | None:
    if start >= len(source) or source[start] != "[":
        return None
    i = start + 1
    while i < len(source) and source[i] == "=":
        i += 1
    if i >= len(source) or source[i] != "[":
        return None
    marker = "]" + ("=" * (i - start - 1)) + "]"
    end = source.find(marker, i + 1)
    if end == -1:
        return len(source), marker
    return end + len(marker), marker


def transform_code_segment(code: str) -> str:
    def colon_definition(match: re.Match[str]) -> str:
        path = re.sub(r"\s+", "", match.group(1))
        method = match.group(2)
        args = match.group(3).strip()
        if args:
            args = "self, " + args
        else:
            args = "self"
        return f"{path}.{method} = function({args})"

    def dotted_definition(match: re.Match[str]) -> str:
        path = re.sub(r"\s+", "", match.group(1))
        return f"{path} = function("

    def empty_colon_call(match: re.Match[str]) -> str:
        receiver = re.sub(r"\s+", "", match.group(1))
        method = match.group(2)
        return f'{receiver}["{method}"]({receiver})'

    def colon_call(match: re.Match[str]) -> str:
        receiver = re.sub(r"\s+", "", match.group(1))
        method = match.group(2)
        return f'{receiver}["{method}"]({receiver},'

    code = re.sub(
        r"\bfunction\s+([A-Za-z_][A-Za-z0-9_]*(?:\s*\.\s*[A-Za-z_][A-Za-z0-9_]*)*)\s*:\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(([^)]*)\)",
        colon_definition,
        code,
    )
    code = re.sub(
        r"\bfunction\s+([A-Za-z_][A-Za-z0-9_]*(?:\s*\.\s*[A-Za-z_][A-Za-z0-9_]*)+)\s*\(",
        dotted_definition,
        code,
    )
    code = re.sub(r"\bsmart_service_slot_doctor\b", "__z_svc", code)
    code = re.sub(r"\bzhopa\b", "__z_root", code)
    code = re.sub(
        r"(\b[A-Za-z_][A-Za-z0-9_]*(?:\s*(?:\.\s*[A-Za-z_][A-Za-z0-9_]*|\[[^\]]+\]))*)\s*:\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(\s*\)",
        empty_colon_call,
        code,
    )
    code = re.sub(
        r"(\b[A-Za-z_][A-Za-z0-9_]*(?:\s*(?:\.\s*[A-Za-z_][A-Za-z0-9_]*|\[[^\]]+\]))*)\s*:\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(",
        colon_call,
        code,
    )
    code = re.sub(r"(?<![\d.])\.([A-Za-z_][A-Za-z0-9_]*)", r'["\1"]', code)
    return code


def protect_lua_source(source: str) -> str:
    output: list[str] = []
    code: list[str] = []
    saw_zhopa = re.search(r"\bzhopa\b", source) is not None
    saw_service = re.search(r"\bsmart_service_slot_doctor\b", source) is not None

    def flush_code() -> None:
        if code:
            output.append(transform_code_segment("".join(code)))
            code.clear()

    i = 0
    while i < len(source):
        if source.startswith("--", i):
            flush_code()
            long_end = find_long_bracket_end(source, i + 2)
            if long_end:
                end, _ = long_end
                output.append(source[i:end])
                i = end
                continue
            end = source.find("\n", i)
            if end == -1:
                output.append(source[i:])
                break
            output.append(source[i:end + 1])
            i = end + 1
            continue

        ch = source[i]
        if ch in ("'", '"'):
            flush_code()
            quote = ch
            start = i
            i += 1
            while i < len(source):
                if source[i] == "\\":
                    i += 2
                    continue
                if source[i] == quote:
                    i += 1
                    break
                i += 1
            output.append(source[start:i])
            continue

        long_end = find_long_bracket_end(source, i)
        if long_end:
            flush_code()
            end, _ = long_end
            output.append(source[i:end])
            i = end
            continue

        code.append(ch)
        i += 1

    flush_code()
    transformed = "".join(output)

    prelude: list[str] = []
    if saw_zhopa:
        prelude.append('local __z_root = _G["zhopa"] or {}')
        prelude.append('_G["zhopa"] = __z_root')
    if saw_service:
        prelude.append('local __z_svc = _G["smart_service_slot_doctor"] or {}')
        prelude.append('_G["smart_service_slot_doctor"] = __z_svc')
    if prelude:
        return "\n".join(prelude) + "\n" + transformed
    return transformed


def split_main_script(source: str) -> list[Segment]:
    lines = source.splitlines(keepends=True)
    begin_indices: list[int] = []
    end_indices: list[int] = []
    for index, line in enumerate(lines):
        if line.startswith("-- BEGIN module "):
            begin_indices.append(index)
        elif line.startswith("-- END module "):
            end_indices.append(index)

    if not begin_indices:
        return [Segment("000_full", source)]
    if len(begin_indices) != len(end_indices):
        raise BuildError(f"module marker mismatch: {len(begin_indices)} BEGIN vs {len(end_indices)} END")

    head_tail = "".join(lines[: begin_indices[0]] + lines[end_indices[-1] + 1 :])
    segments = [Segment("000_head_tail", head_tail)]
    for number, (begin, end) in enumerate(zip(begin_indices, end_indices), start=1):
        module_name = lines[begin].removeprefix("-- BEGIN module ").strip()
        safe_name = re.sub(r"[^A-Za-z0-9_]+", "_", module_name)
        body = "local zhopa_bundle_module\n" + "".join(lines[begin : end + 1])
        segments.append(Segment(f"{number:03d}_{safe_name}", body))
    return segments


def split_script(relative_path: Path, source: str) -> list[Segment]:
    if relative_path.name == "zhopa.script":
        return split_main_script(source)
    safe_name = re.sub(r"[^A-Za-z0-9_]+", "_", relative_path.name)
    return [Segment(f"000_{safe_name}", source)]


def write_config_files(work_root: Path) -> tuple[Path, Path]:
    vm_config = work_root / "prometheus-vm.lua"
    novm_config = work_root / "prometheus-novm.lua"
    vm_config.write_text(VM_CONFIG.strip() + "\n", encoding="ascii")
    novm_config.write_text(NOVM_CONFIG.strip() + "\n", encoding="ascii")
    return vm_config, novm_config


def obfuscate_with_prometheus(
    toolchain: Toolchain,
    prometheus_root: Path,
    config: Path,
    source: Path,
    output: Path,
    log: Path,
) -> subprocess.CompletedProcess[str]:
    result = run_process(
        [
            str(toolchain.lua51),
            str(prometheus_root / "cli.lua"),
            "--nocolors",
            "--config",
            str(config),
            "--out",
            str(output),
            str(source),
        ],
        allow_fail=True,
    )
    log.write_text(result.stdout + result.stderr, encoding="utf-8", newline="\n")
    return result


def compile_luajit(toolchain: Toolchain, source: Path, output: Path) -> subprocess.CompletedProcess[str]:
    return run_process(
        [
            str(toolchain.luajit),
            "-b",
            "-s",
            "-t",
            "raw",
            "-n",
            "_",
            str(source),
            str(output),
        ],
        cwd=toolchain.luajit.parent,
        allow_fail=True,
    )


def build_segment(
    segment: Segment,
    *,
    segment_source: Path,
    toolchain: Toolchain,
    prometheus_root: Path,
    vm_config: Path,
    novm_config: Path,
    output_root: Path,
    mode: str,
) -> BuiltChunk:
    vm_lua = output_root / f"{segment.name}.vm.lua"
    vm_bc = output_root / f"{segment.name}.ljbc"

    if mode in ("chunk-vm-auto", "vm"):
        result = obfuscate_with_prometheus(
            toolchain,
            prometheus_root,
            vm_config,
            segment_source,
            vm_lua,
            output_root / f"{segment.name}.vm.log",
        )
        if result.returncode == 0:
            compiled = compile_luajit(toolchain, vm_lua, vm_bc)
            (output_root / f"{segment.name}.vm.compile.log").write_text(
                compiled.stdout + compiled.stderr, encoding="utf-8", newline="\n"
            )
            if compiled.returncode == 0:
                return BuiltChunk(segment.name, "vm", vm_bc)
            if mode == "vm":
                raise BuildError(f"{segment.name}: VM output did not compile with LuaJIT")
        elif mode == "vm":
            raise BuildError(f"{segment.name}: Prometheus VM failed")

    novm_lua = output_root / f"{segment.name}.novm.lua"
    result = obfuscate_with_prometheus(
        toolchain,
        prometheus_root,
        novm_config,
        segment_source,
        novm_lua,
        output_root / f"{segment.name}.novm.log",
    )
    if result.returncode != 0:
        raise BuildError(f"{segment.name}: Prometheus no-VM fallback failed")
    compiled = compile_luajit(toolchain, novm_lua, vm_bc)
    (output_root / f"{segment.name}.novm.compile.log").write_text(
        compiled.stdout + compiled.stderr, encoding="utf-8", newline="\n"
    )
    if compiled.returncode != 0:
        raise BuildError(f"{segment.name}: no-VM fallback did not compile with LuaJIT")
    return BuiltChunk(segment.name, "novm", vm_bc)


def pack_chunks(chunks: list[BuiltChunk]) -> bytes:
    blob = bytearray()
    blob += struct.pack("<I", len(chunks))
    for chunk in chunks:
        data = chunk.bytecode.read_bytes()
        blob += struct.pack("<I", len(data))
        blob += data
    return bytes(blob)


def make_loader_source(blob: bytes) -> str:
    key = os.urandom(32)
    encoded = bytes(value ^ key[index % len(key)] for index, value in enumerate(blob))
    hexed = encoded.hex()
    pieces = [hexed[index : index + 4096] for index in range(0, len(hexed), 4096)]
    key_values = ",".join(str(value) for value in key)
    piece_lines = "\n".join(f'  "{piece}",' for piece in pieces)
    return f"""do
local p = {{
{piece_lines}
}}
local k = {{{key_values}}}
local h = table.concat(p)
local bx = bit and bit.bxor or require("bit").bxor
local sub = string.sub
local byte = string.byte
local char = string.char
local tonumber = tonumber
local env = getfenv and getfenv(1) or _G
local setfenv = setfenv
local out = {{}}
local buf = {{}}
local n = 0
for i = 1, #h, 2 do
  n = n + 1
  buf[#buf + 1] = char(bx(tonumber(sub(h, i, i + 1), 16), k[((n - 1) % #k) + 1]))
  if #buf >= 4096 then
    out[#out + 1] = table.concat(buf)
    buf = {{}}
  end
end
if #buf > 0 then
  out[#out + 1] = table.concat(buf)
end
local b = table.concat(out)
local pos = 1
local function u32()
  local a, c, d, e = byte(b, pos, pos + 3)
  pos = pos + 4
  return a + c * 256 + d * 65536 + e * 16777216
end
local count = u32()
for _ = 1, count do
  local len = u32()
  local chunk = sub(b, pos, pos + len - 1)
  pos = pos + len
  local fn, err = loadstring(chunk, "@_")
  if not fn then error(err) end
  if setfenv then setfenv(fn, env) end
  fn()
end
end
"""


def ascii_contains(path: Path, terms: Iterable[str]) -> list[str]:
    text = path.read_bytes().decode("ascii", errors="ignore").lower()
    return [term for term in terms if term.lower() in text]


def validate_bytecode_load(toolchain: Toolchain, path: Path) -> None:
    escaped = str(path).replace("\\", "\\\\").replace("]", "\\]")
    code = f'assert(loadfile([==[{escaped}]==]))'
    result = run_process([str(toolchain.luajit), "-e", code], cwd=toolchain.luajit.parent, allow_fail=True)
    if result.returncode != 0:
        raise BuildError(f"LuaJIT loadfile validation failed for {path}\n{result.stdout}{result.stderr}")


def build_script_sidecar(
    relative_path: Path,
    *,
    project_root: Path,
    toolchain: Toolchain,
    prometheus_root: Path,
    vm_config: Path,
    novm_config: Path,
    work_root: Path,
    mode: str,
    fail_on_inner_leaks: bool,
) -> None:
    source_path = (project_root / relative_path).resolve()
    output_path = Path(str(source_path) + ".ljbc")
    source_hash = sha256_file(source_path)
    source_text = source_path.read_text(encoding="utf-8")

    script_work = work_root / re.sub(r"[^A-Za-z0-9_]+", "_", str(relative_path))
    segments_root = script_work / "segments"
    output_root = script_work / "built"
    segments_root.mkdir(parents=True, exist_ok=True)
    output_root.mkdir(parents=True, exist_ok=True)

    segments = split_script(relative_path, source_text)
    built_chunks: list[BuiltChunk] = []
    mode_counts: dict[str, int] = {}

    for segment in segments:
        protected = protect_lua_source(segment.source)
        segment_source = segments_root / f"{segment.name}.lua"
        segment_source.write_text(protected, encoding="utf-8", newline="\n")
        built = build_segment(
            segment,
            segment_source=segment_source,
            toolchain=toolchain,
            prometheus_root=prometheus_root,
            vm_config=vm_config,
            novm_config=novm_config,
            output_root=output_root,
            mode=mode,
        )
        built_chunks.append(built)
        mode_counts[built.mode] = mode_counts.get(built.mode, 0) + 1

    blob = pack_chunks(built_chunks)
    loader_source = output_root / "loader.lua"
    loader_source.write_text(make_loader_source(blob), encoding="ascii", newline="\n")
    staged_output = output_root / (source_path.name + ".ljbc")
    compiled = compile_luajit(toolchain, loader_source, staged_output)
    (output_root / "loader.compile.log").write_text(compiled.stdout + compiled.stderr, encoding="utf-8", newline="\n")
    if compiled.returncode != 0:
        raise BuildError(f"loader did not compile for {relative_path}")

    shutil.copy2(staged_output, output_path)
    validate_bytecode_load(toolchain, output_path)

    final_hits = ascii_contains(output_path, BLACKLIST_TERMS)
    if final_hits:
        raise BuildError(f"{output_path} still contains readable final terms: {', '.join(final_hits)}")

    inner_hits: dict[str, list[str]] = {}
    for built in built_chunks:
        hits = ascii_contains(built.bytecode, BLACKLIST_TERMS)
        if hits:
            inner_hits[built.name] = hits
    if inner_hits:
        details = "; ".join(f"{name}: {', '.join(hits)}" for name, hits in inner_hits.items())
        if fail_on_inner_leaks:
            raise BuildError(f"decoded inner bytecode still contains readable terms: {details}")
        print(f"warning: decoded inner bytecode has readable terms: {details}", file=sys.stderr)

    if sha256_file(source_path) != source_hash:
        raise BuildError(f"source file changed unexpectedly: {source_path}")

    modes = ", ".join(f"{name}={count}" for name, count in sorted(mode_counts.items()))
    print(f"built {output_path} ({len(built_chunks)} chunks; {modes}; {output_path.stat().st_size} bytes)")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--lua51", help="Path to Lua 5.1 executable used to run Prometheus")
    parser.add_argument("--luajit", help="Path to xray LuaJIT 2.0.4 executable")
    parser.add_argument("--prometheus-root", help="Path to prometheus-lua/Prometheus checkout")
    parser.add_argument(
        "--mode",
        choices=("chunk-vm-auto", "vm", "novm"),
        default="chunk-vm-auto",
        help="Obfuscation mode. chunk-vm-auto uses VM where LuaJIT accepts it and falls back per chunk.",
    )
    parser.add_argument("--work-root", type=Path, help="Directory for intermediate files")
    parser.add_argument("--keep-work", action="store_true", help="Print and keep intermediate files")
    parser.add_argument("--fail-on-inner-leaks", action="store_true", help="Fail if decoded inner chunks contain blacklist terms")
    parser.add_argument("inputs", nargs="*", type=Path, default=list(DEFAULT_INPUTS))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_root = args.project_root.resolve()
    work_root = args.work_root or Path(tempfile.gettempdir()) / ("zhopa-obfuscation-" + os.urandom(8).hex())
    work_root.mkdir(parents=True, exist_ok=True)

    toolchain = Toolchain(
        lua51=find_lua51(args.lua51),
        luajit=find_luajit(args.luajit),
        prometheus=find_prometheus(args.prometheus_root),
    )
    verify_toolchain(toolchain)
    patched_prometheus = patch_prometheus(toolchain.prometheus, work_root)
    vm_config, novm_config = write_config_files(work_root)

    print(f"work: {work_root}")
    print(f"lua51: {toolchain.lua51}")
    print(f"luajit: {toolchain.luajit}")
    print(f"prometheus: {toolchain.prometheus}")

    for relative_path in args.inputs:
        build_script_sidecar(
            relative_path,
            project_root=project_root,
            toolchain=toolchain,
            prometheus_root=patched_prometheus,
            vm_config=vm_config,
            novm_config=novm_config,
            work_root=work_root,
            mode=args.mode,
            fail_on_inner_leaks=args.fail_on_inner_leaks,
        )

    if args.keep_work:
        print(f"kept work directory: {work_root}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BuildError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
