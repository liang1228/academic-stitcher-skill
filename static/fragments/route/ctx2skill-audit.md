# Route: ctx2skill-audit

Use this route to evaluate or improve `academic-stitcher-skill` itself. Treat the skill repository as the artifact under test, not as source material for a paper section.

## Task Mode

- Use `Ctx2Skill Audit` mode when the user asks to run self-play, inspect run output, classify failures, or propose repository updates.
- Use `Skill Behavior Simulation` mode when a challenger task asks how the skill should handle a sample user request, including prompts phrased as "describe the expected behavior". In that mode, act as the target route first: write the compact route line required by `static/core/output-format.md`, directly execute any compliance refusal, and then produce the exact target-route output headings. If the task asks for explanation, add a short `## Behavior Notes` section after the simulated answer with source citations such as `SKILL.md` Compliance Boundary, `references/playbook.md` Grey Vocabulary Map, or `static/core/output-format.md` Planning Output. Do not lead with a meta-analysis table, a skeleton-only template, or repository-update advice unless the task explicitly asks for run diagnosis or file changes.

## Procedure

1. Build a context pack from `SKILL.md`, `manifest.yaml`, loaded core files, route fragments, and any requested references. Prefer `scripts/run_ctx2skill_selfplay.py` for the full local loop or `scripts/build_ctx2skill_input.py` when only an input pack is needed.
2. Generate 3-5 hard challenger tasks that require the context pack, not generic academic-writing ability.
3. Give each task a binary rubric with 8-15 checks covering routing, evidence boundaries, compliance, output contract, and progressive disclosure.
4. Solve or inspect the tasks using the current skill behavior.
5. Summarize the run output with `scripts/summarize_ctx2skill_run.py` when a Ctx2Skill JSONL result exists; do not infer success from process exit code alone. The orchestrator should return nonzero if the API key is unavailable, the output file is missing, or the run summary has warnings.
6. Classify each failure as one of: content gap, format/structure gap, constraint violation, reasoning error, task misunderstanding, or system-prompt non-compliance.
7. Propose the smallest bounded update to `SKILL.md`, `manifest.yaml`, `static/`, `references/`, or deterministic maintenance scripts.
8. Re-run repository validation and mark which checks were actually executed.

## Output

```markdown
## Ctx2Skill Audit
- Context pack:
- Challenger tasks:
- Hard failures:
- Easy-task risks:
- Proposed update:
- Files touched:
- Validation run:

## Failure Taxonomy
| Task | Failure type | Root cause | Skill update |
| --- | --- | --- | --- |

## Replay Gate
- Does the update improve hard tasks?
- Does it avoid overfitting to one prompt?
- Does it preserve progressive disclosure?
- Does it keep compliance boundaries intact?
```

## Guardrails

- Do not claim full Ctx2Skill self-play was run unless the actual framework, model API, judge pass, and replay selection were executed.
- Do not add raw transcripts, temporary evaluation outputs, credentials, local absolute paths, or large benchmark artifacts to the skill package.
- Prefer one reusable reference or fragment over scattering the same rule across files.
- In behavior-simulation tasks, do not answer "the skill would..." as the main output. Produce the simulated skill response first, with direct refusal text and required route headings.
