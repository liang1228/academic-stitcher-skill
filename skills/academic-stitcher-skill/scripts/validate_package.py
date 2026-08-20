#!/usr/bin/env python3
"""Deterministic release validation for academic-stitcher-skill."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml


EXPECTED_VERSION = "2.3.0"
ALLOWED_TOP_LEVEL = {
    "SKILL.md",
    "manifest.yaml",
    "agents",
    "scripts",
    "static",
    "references",
    "tests",
}
ROUTES = {
    "stitch-plan",
    "section-draft",
    "nature-polish",
    "reviewer-audit",
    "story-architecture",
    "full-pipeline",
    "ctx2skill-audit",
}
PAPER_TYPES = {"research", "methods", "algorithmic", "review", "proposal-thesis"}
SECTIONS = {
    "title",
    "abstract",
    "introduction",
    "related-work",
    "method",
    "experiments",
    "discussion",
    "conclusion",
}
LANGUAGES = {"zh-cn", "en"}
BANNED_BEHAVIOR = [
    "pick those whose numbers are most favorable",
    "baseline may use less favorable settings",
    "merge the problematic module",
    "pick best/worst appropriately",
    "copy dataset descriptions",
    "choose the calculation that yields the most favorable",
    "use this to your advantage when reproducing baselines",
    "downplay it or omit it",
    "less conspicuous location",
    "never volunteer that only partial code",
    "fatigue exploitation",
    "90% pass rate",
    "不利的信息要么不写",
    "没写的可以不说",
    "运行时间等不利信息",
]


def resolve_inside(root: Path, rel: str) -> Path:
    item = Path(rel)
    if item.is_absolute():
        raise ValueError(f"absolute manifest path: {rel}")
    resolved = (root / item).resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"manifest path escapes root: {rel}") from exc
    if resolved.is_symlink():
        raise ValueError(f"manifest path is a symlink: {rel}")
    if not resolved.is_file():
        raise ValueError(f"manifest path is not a file: {rel}")
    return resolved


def manifest_paths(manifest: dict) -> list[str]:
    values: list[str] = list(manifest.get("always_load", []))
    for axis in manifest.get("axes", {}).values():
        mapping = axis.get("values", {})
        if isinstance(mapping, dict):
            values.extend(str(path) for path in mapping.values())
    for entry in manifest.get("references", {}).get("on_demand", []):
        values.append(str(entry.get("path", "")))
    return values


def validate_frontmatter(root: Path, issues: list[str]) -> None:
    text = (root / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        issues.append("SKILL.md: invalid or missing YAML frontmatter")
        return
    data = yaml.safe_load(match.group(1)) or {}
    if data.get("name") != "academic-stitcher-skill":
        issues.append("SKILL.md: wrong name")
    description = str(data.get("description", "")).strip()
    if len(description) < 80:
        issues.append("SKILL.md: description is too short for reliable triggering")


def validate_manifest(root: Path, issues: list[str]) -> dict:
    manifest = yaml.safe_load((root / "manifest.yaml").read_text(encoding="utf-8")) or {}
    if manifest.get("name") != "academic-stitcher-skill":
        issues.append("manifest: wrong name")
    if str(manifest.get("version")) != EXPECTED_VERSION:
        issues.append(f"manifest: expected version {EXPECTED_VERSION}")

    axes = manifest.get("axes", {})
    expected_values = {
        "route": ROUTES,
        "paper_type": PAPER_TYPES,
        "section": SECTIONS,
        "language": LANGUAGES,
    }
    for axis, expected in expected_values.items():
        actual = set((axes.get(axis, {}).get("values", {}) or {}).keys())
        if actual != expected:
            issues.append(f"manifest: {axis} values mismatch: {sorted(actual)}")
        default = axes.get(axis, {}).get("default")
        if default is not None and default not in actual:
            issues.append(f"manifest: invalid {axis} default {default!r}")

    paths = manifest_paths(manifest)
    if not paths or len(paths) != len(set(paths)):
        issues.append("manifest: paths are missing or duplicated")
    for rel in paths:
        try:
            resolve_inside(root, rel)
        except ValueError as exc:
            issues.append(str(exc))
    return manifest


def validate_tests(root: Path, issues: list[str]) -> None:
    path = root / "tests/test-prompts.json"
    try:
        cases = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        issues.append(f"tests: cannot parse {path.name}: {exc}")
        return
    if not isinstance(cases, list) or len(cases) < 18:
        issues.append("tests: expected at least 18 cases")
        return
    ids = [str(case.get("id", "")) for case in cases]
    if any(not item for item in ids) or len(ids) != len(set(ids)):
        issues.append("tests: ids are missing or duplicated")
    for case in cases:
        label = case.get("id", "?")
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            issues.append(f"tests {label}: missing prompt")
        if not isinstance(case.get("should_trigger"), bool):
            issues.append(f"tests {label}: should_trigger must be boolean")
        if case.get("should_trigger"):
            if case.get("expected_route") not in ROUTES:
                issues.append(f"tests {label}: invalid expected_route")
            if case.get("expected_paper_type") not in PAPER_TYPES:
                issues.append(f"tests {label}: invalid expected_paper_type")
            if case.get("expected_language") not in LANGUAGES:
                issues.append(f"tests {label}: invalid expected_language")
            bad_sections = set(case.get("expected_sections", [])) - SECTIONS
            if bad_sections:
                issues.append(f"tests {label}: invalid sections {sorted(bad_sections)}")
    kinds = {case.get("kind") for case in cases}
    for required in {"positive", "sibling-lure", "boundary", "negative"}:
        if required not in kinds:
            issues.append(f"tests: missing {required} cases")


def scan_release(root: Path, issues: list[str]) -> None:
    unexpected = {path.name for path in root.iterdir()} - ALLOWED_TOP_LEVEL
    if unexpected:
        issues.append(f"unexpected top-level entries: {sorted(unexpected)}")

    secret_pattern = re.compile(r"(?i)(?:sk-[A-Za-z0-9_-]{16,}|BEGIN (?:RSA |OPENSSH )?PRIVATE KEY)")
    absolute_pattern = re.compile(r"(?i)\b[A-Z]:\\(?:Users|workspace|BaiduNetdiskDownload)\\")
    bvid_pattern = re.compile(r"\bBV1[A-Za-z0-9]{6,}\b")
    for path in root.rglob("*"):
        if path.is_dir() or path.is_symlink() or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        lowered = text.lower()
        if secret_pattern.search(text):
            issues.append(f"{rel}: possible credential/private key")
        if absolute_pattern.search(text):
            issues.append(f"{rel}: local absolute path")
        if bvid_pattern.search(text):
            issues.append(f"{rel}: legacy video marker remains")
        if rel != "scripts/validate_package.py":
            for phrase in BANNED_BEHAVIOR:
                if phrase.lower() in lowered:
                    issues.append(f"{rel}: banned behavior phrase: {phrase}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    issues: list[str] = []
    for required in ("SKILL.md", "manifest.yaml", "agents/openai.yaml"):
        if not (root / required).is_file():
            issues.append(f"missing required file: {required}")
    if not issues:
        validate_frontmatter(root, issues)
        manifest = validate_manifest(root, issues)
        validate_tests(root, issues)
        scan_release(root, issues)
    else:
        manifest = {}

    result = {
        "ok": not issues,
        "version": manifest.get("version"),
        "manifest_paths": len(manifest_paths(manifest)) if manifest else 0,
        "issues": issues,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif issues:
        print("Package validation failed:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print(f"Package is valid: version={result['version']}, manifest_paths={result['manifest_paths']}")
    return 0 if not issues else 1


if __name__ == "__main__":
    sys.exit(main())
