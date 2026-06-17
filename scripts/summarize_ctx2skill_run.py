#!/usr/bin/env python3
"""Summarize a Ctx2Skill self-play JSONL result."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from textwrap import shorten


def load_records(path: Path) -> tuple[list[dict], list[str]]:
    records: list[dict] = []
    errors: list[str] = []
    if not path.exists():
        return records, [f"missing input: {path}"]

    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.strip():
        return records, ["input is empty"]

    lowered = text.lower()
    if "please set" in lowered and "--api-key" in lowered:
        errors.append("input appears to contain a credential-configuration error rather than a completed run")

    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            value = json.loads(stripped)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_no}: invalid JSONL record: {exc.msg}")
            continue
        if isinstance(value, dict):
            records.append(value)
        else:
            errors.append(f"line {line_no}: record is not a JSON object")

    return records, errors


def _short(value: object, width: int = 120) -> str:
    return shorten(str(value).replace("\n", " "), width=width, placeholder="...")


def summarize(records: list[dict], errors: list[str]) -> str:
    contexts = sorted({str(r.get("context_id", "unknown")) for r in records})
    task_results: list[tuple[dict, dict]] = []
    proposed: list[tuple[str, dict]] = []

    for record in records:
        for result in record.get("task_results", []) or []:
            if isinstance(result, dict):
                task_results.append((record, result))
        for key in ("proposed_reasoner_skill", "proposed_challenger_skill"):
            value = record.get(key)
            if isinstance(value, dict) and value:
                proposed.append((key, value))

    total_tasks = len(task_results)
    failed_tasks = 0
    failed_checks = 0
    failed_api = sum(int(r.get("failed_api", 0) or 0) for r in records)
    passed_tasks = 0

    for _, result in task_results:
        status = result.get("requirement_status") or []
        if status:
            no_count = sum(1 for item in status if str(item).lower() == "no")
            failed_checks += no_count
            if no_count:
                failed_tasks += 1
            else:
                passed_tasks += 1
        elif int(result.get("judge_score", 0) or 0) == 1:
            passed_tasks += 1
        else:
            failed_tasks += 1

    if errors:
        run_status = "not completed" if not records else "completed with warnings"
    elif failed_tasks or failed_api:
        run_status = "completed with failures"
    else:
        run_status = "completed"

    lines = [
        "# Ctx2Skill Run Summary",
        "",
        f"- Run status: {run_status}",
        f"- Records: {len(records)}",
        f"- Contexts: {', '.join(contexts) if contexts else 'none'}",
        f"- Total tasks: {total_tasks}",
        f"- Passed tasks: {passed_tasks}",
        f"- Failed tasks: {failed_tasks}",
        f"- Failed checks: {failed_checks}",
        f"- Failed API calls: {failed_api}",
    ]

    if errors:
        lines.extend(["", "## Warnings"])
        for error in errors:
            lines.append(f"- {error}")

    failed_rows: list[str] = []
    for record, result in task_results:
        status = result.get("requirement_status") or []
        failed_indices = [idx + 1 for idx, item in enumerate(status) if str(item).lower() == "no"]
        if not failed_indices and int(result.get("judge_score", 0) or 0) == 1:
            continue
        rubrics = result.get("rubrics") or []
        failed_text = "; ".join(_short(rubrics[idx - 1], 90) for idx in failed_indices if idx - 1 < len(rubrics))
        failed_rows.append(
            "| "
            + " | ".join(
                [
                    str(record.get("context_id", "unknown")),
                    str(record.get("iteration", result.get("iteration", ""))),
                    str(result.get("task_idx", "")),
                    ", ".join(map(str, failed_indices)) or "score",
                    failed_text or _short(result.get("judge_rationale", ""), 90),
                ]
            )
            + " |"
        )

    if failed_rows:
        lines.extend(
            [
                "",
                "## Failed Rubrics",
                "",
                "| Context | Iteration | Task | Failed checks | Rubric text |",
                "| --- | ---: | ---: | --- | --- |",
            ]
        )
        lines.extend(failed_rows)

    rationale_rows: list[str] = []
    for record, result in task_results:
        rationale = result.get("judge_rationale")
        if rationale:
            rationale_rows.append(
                "| "
                + " | ".join(
                    [
                        str(record.get("context_id", "unknown")),
                        str(result.get("task_idx", "")),
                        _short(rationale, 180),
                    ]
                )
                + " |"
            )

    if rationale_rows:
        lines.extend(
            [
                "",
                "## Judge Rationales",
                "",
                "| Context | Task | Rationale |",
                "| --- | ---: | --- |",
            ]
        )
        lines.extend(rationale_rows)

    if proposed:
        lines.extend(["", "## Proposed Skills"])
        for kind, value in proposed:
            name = value.get("skill_name") or value.get("target_skill") or "unnamed"
            desc = value.get("skill_description") or value.get("description") or ""
            analysis = value.get("analysis") or value.get("justification") or ""
            lines.extend(
                [
                    "",
                    f"- Kind: {kind}",
                    f"- Name: {name}",
                    f"- Description: {_short(desc, 180)}",
                    f"- Rationale: {_short(analysis, 240)}",
                ]
            )

    lines.extend(
        [
            "",
            "## Replay Leads",
            "",
            "- Convert repeated failed checks into one bounded skill edit.",
            "- Re-run a hard task that failed and one easy task that should not change.",
            "- Mark model-dependent checks as not run when the run output is missing or only contains warnings.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize Ctx2Skill self-play JSONL results.")
    parser.add_argument("--input", required=True, help="Ctx2Skill self-play JSONL output path.")
    parser.add_argument("--output", help="Optional Markdown summary path.")
    parser.add_argument("--fail-on-warning", action="store_true", help="Exit nonzero when warnings are present.")
    args = parser.parse_args()

    records, errors = load_records(Path(args.input))
    summary = summarize(records, errors)

    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(summary, encoding="utf-8")
        print(f"Wrote {output}")
    else:
        print(summary, end="")

    return 1 if errors and args.fail_on_warning else 0


if __name__ == "__main__":
    raise SystemExit(main())
