#!/usr/bin/env python3
"""Build a Ctx2Skill JSONL context pack for this skill."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - depends on caller environment
    print("PyYAML is required. Run this with the Ctx2Skill venv or install pyyaml.", file=sys.stderr)
    raise


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _unique_paths(paths: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in paths:
        normalized = Path(item).as_posix()
        if normalized not in seen:
            seen.add(normalized)
            out.append(normalized)
    return out


def collect_manifest_paths(root: Path, manifest: dict, include_scripts: bool = True) -> list[str]:
    paths: list[str] = ["SKILL.md", "manifest.yaml"]
    paths.extend(manifest.get("always_load", []))

    for axis in manifest.get("axes", {}).values():
        values = axis.get("values", {})
        if isinstance(values, dict):
            paths.extend(values.values())

    for entry in manifest.get("references", {}).get("on_demand", []):
        path = entry.get("path")
        if path:
            paths.append(path)

    if include_scripts:
        scripts_dir = root / "scripts"
        if scripts_dir.exists():
            paths.extend(str(path.relative_to(root).as_posix()) for path in sorted(scripts_dir.glob("*.py")))

    return _unique_paths(paths)


def assert_clean_pack(files: list[tuple[str, str]]) -> None:
    forbidden_terms = [
        "SESS" + "DATA",
        "transcripts" + "_raw",
        "transcripts" + "_distilled",
    ]
    path_pattern = re.compile(r"\b[A-Za-z]:\\")
    failures: list[str] = []

    for rel_path, text in files:
        for term in forbidden_terms:
            if term in text:
                failures.append(f"{rel_path}: contains forbidden acquisition artifact marker")
        if path_pattern.search(text):
            failures.append(f"{rel_path}: contains a local absolute path")

    if failures:
        joined = "\n".join(failures)
        raise SystemExit(f"Refusing to build Ctx2Skill input:\n{joined}")


def build_prompt(skill_name: str, files: list[tuple[str, str]]) -> str:
    chunks = [
        f"You are evaluating and improving the Codex skill named {skill_name}.",
        "This context contains the skill router, manifest, core rules, fragments, references, and maintenance scripts.",
        "Generate hard Ctx2Skill-style challenger tasks, solve or judge them against the current skill behavior, and propose the smallest evidence-preserving skill update.",
        "Do not invent benchmark results. If an API-dependent self-play loop was not actually run, label that as not run.",
        "",
        "Use the following source files as the complete context pack.",
        "",
    ]

    for rel_path, text in files:
        chunks.append(f"--- FILE: {rel_path} ---")
        chunks.append(text.rstrip())
        chunks.append("")

    return "\n".join(chunks).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build Ctx2Skill JSONL input from an academic-stitcher-skill repo.")
    parser.add_argument("--root", default=".", help="Skill repository root. Defaults to the current directory.")
    parser.add_argument("--output", required=True, help="Output JSONL path.")
    parser.add_argument("--context-id", default="academic-stitcher-core", help="Ctx2Skill context_id metadata value.")
    parser.add_argument("--skip-clean-check", action="store_true", help="Skip local-artifact and local-path scan.")
    parser.add_argument("--no-include-scripts", action="store_true", help="Exclude scripts/*.py from the context pack.")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    manifest_path = root / "manifest.yaml"
    if not manifest_path.exists():
        raise SystemExit(f"Missing manifest: {manifest_path}")

    manifest = yaml.safe_load(_read_text(manifest_path)) or {}
    skill_name = str(manifest.get("name") or root.name)
    rel_paths = collect_manifest_paths(root, manifest, include_scripts=not args.no_include_scripts)

    files: list[tuple[str, str]] = []
    missing: list[str] = []
    for rel_path in rel_paths:
        path = root / rel_path
        if not path.exists():
            missing.append(rel_path)
            continue
        files.append((rel_path, _read_text(path)))

    if missing:
        raise SystemExit("Missing manifest files:\n" + "\n".join(missing))

    if not args.skip_clean_check:
        assert_clean_pack(files)

    prompt = build_prompt(skill_name, files)
    record = {
        "messages": [{"role": "user", "content": prompt}],
        "metadata": {
            "source": f"local {skill_name} manifest files",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "context_id": args.context_id,
            "included_files": [rel for rel, _ in files],
        },
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {output} with {len(files)} files for context_id={args.context_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
