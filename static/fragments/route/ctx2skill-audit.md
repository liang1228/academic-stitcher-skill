# Route: ctx2skill-audit

Use this route to evaluate or improve `academic-stitcher-skill` itself. Treat the skill repository as the artifact under test, not as source material for a paper section.

## Procedure

1. Build a context pack from `SKILL.md`, `manifest.yaml`, loaded core files, route fragments, and any requested references.
2. Generate 3-5 hard challenger tasks that require the context pack, not generic academic-writing ability.
3. Give each task a binary rubric with 8-15 checks covering routing, evidence boundaries, compliance, output contract, and progressive disclosure.
4. Solve or inspect the tasks using the current skill behavior.
5. Classify each failure as one of: content gap, format/structure gap, constraint violation, reasoning error, task misunderstanding, or system-prompt non-compliance.
6. Propose the smallest bounded update to `SKILL.md`, `manifest.yaml`, `static/`, or `references/`.
7. Re-run repository validation and mark which checks were actually executed.

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
- Do not add raw transcripts, temporary evaluation outputs, API keys, local absolute paths, or large benchmark artifacts to the skill package.
- Prefer one reusable reference or fragment over scattering the same rule across files.
