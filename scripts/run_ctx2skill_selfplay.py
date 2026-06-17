#!/usr/bin/env python3
"""Run a guarded local Ctx2Skill self-play pass for this skill."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from build_ctx2skill_input import main as build_input_main
from summarize_ctx2skill_run import load_records, summarize


def _timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _write_summary(input_path: Path, output_path: Path) -> tuple[str, list[str]]:
    records, errors = load_records(input_path)
    text = summarize(records, errors)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    return text, errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build input, run Ctx2Skill self-play, and summarize the result.")
    parser.add_argument("--root", default=".", help="Skill repository root.")
    parser.add_argument("--work-dir", required=True, help="Local output directory for generated inputs, runs, logs, and summaries.")
    parser.add_argument("--context-id", default="academic-stitcher-core", help="Ctx2Skill context_id.")
    parser.add_argument("--selfplay-cmd", default="ctx2skill-selfplay", help="Ctx2Skill self-play command.")
    parser.add_argument("--api-key-env", default="OPENAI_API_KEY", help="Environment variable that holds the API key.")
    parser.add_argument("--base-url-env", default="OPENAI_BASE_URL", help="Optional environment variable that holds the API base URL.")
    parser.add_argument("--max-samples", type=int, default=1)
    parser.add_argument("--num-iterations", type=int, default=1)
    parser.add_argument("--num-tasks", type=int, default=1)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--skip-skill-selection", action="store_true")
    parser.add_argument("--allow-missing-key", action="store_true", help="Build input and summary but return success when the API key is missing.")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    work_dir = Path(args.work_dir).resolve()
    stamp = _timestamp()
    safe_context = args.context_id.replace("/", "_").replace("\\", "_")
    input_path = work_dir / "inputs" / f"{safe_context}_{stamp}.jsonl"
    run_path = work_dir / "runs" / f"{safe_context}_{stamp}.jsonl"
    skills_dir = work_dir / "skills" / f"{safe_context}_{stamp}"
    log_path = work_dir / "logs" / f"{safe_context}_{stamp}.log"
    summary_path = work_dir / "summaries" / f"{safe_context}_{stamp}.md"

    build_rc = build_input_main(
        [
            "--root",
            str(root),
            "--output",
            str(input_path),
            "--context-id",
            args.context_id,
        ]
    )
    if build_rc != 0:
        return build_rc

    api_key_present = bool(os.getenv(args.api_key_env))
    base_url = os.getenv(args.base_url_env)
    if not api_key_present:
        warning = (
            "# Ctx2Skill Run Summary\n\n"
            "- Run status: not completed\n"
            "- Records: 0\n"
            "- Contexts: none\n"
            "- Total tasks: 0\n"
            "- Passed tasks: 0\n"
            "- Failed tasks: 0\n"
            "- Failed checks: 0\n"
            "- Failed API calls: 0\n\n"
            "## Warnings\n"
            f"- missing API key environment variable: {args.api_key_env}\n\n"
            "## Generated Artifacts\n"
            f"- Input: {input_path}\n"
            f"- Intended run output: {run_path}\n"
            f"- Intended log: {log_path}\n"
        )
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        summary_path.write_text(warning, encoding="utf-8")
        print(f"Wrote {summary_path}")
        print(f"Missing API key environment variable: {args.api_key_env}", file=sys.stderr)
        return 0 if args.allow_missing_key else 2

    command = [
        args.selfplay_cmd,
        "--input",
        str(input_path),
        "--output",
        str(run_path),
        "--skills-dir",
        str(skills_dir),
        "--max-samples",
        str(args.max_samples),
        "--num-iterations",
        str(args.num_iterations),
        "--num-tasks",
        str(args.num_tasks),
        "--workers",
        str(args.workers),
    ]
    if base_url:
        command.extend(["--base-url", base_url])
    if args.skip_skill_selection:
        command.append("--skip-skill-selection")

    log_path.parent.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env.setdefault("PYTHONUTF8", "1")
    env.setdefault("PYTHONIOENCODING", "utf-8")

    completed = subprocess.run(command, cwd=str(root), env=env, capture_output=True, text=True)
    log_text = [
        "command: " + " ".join(command),
        f"returncode: {completed.returncode}",
        "",
        "## stdout",
        completed.stdout,
        "",
        "## stderr",
        completed.stderr,
    ]
    log_path.write_text("\n".join(log_text), encoding="utf-8")

    summary_text, summary_errors = _write_summary(run_path, summary_path)
    print(f"Wrote {summary_path}")
    print(summary_text, end="")

    stdout_lower = completed.stdout.lower()
    stderr_lower = completed.stderr.lower()
    credential_error = "please set" in stdout_lower + stderr_lower and "--api-key" in stdout_lower + stderr_lower
    if completed.returncode != 0 or credential_error or summary_errors or not run_path.exists():
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
