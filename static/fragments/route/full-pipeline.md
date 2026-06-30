# Route: Full Pipeline

Use when the user asks for end-to-end research-to-paper support.

## Stages

1. Intake and constraints.
2. Literature/paper matrix.
3. Story architecture.
4. Evidence and integrity gate.
5. Section plan.
6. Draft or polish.
7. Reviewer audit.
8. Revision roadmap.
9. Final quality gate.

## Checkpoint Contract

Stop after the requested checkpoint. If the user did not name a checkpoint, complete the current stage and state the next gate.

---

## Stage Details

### Stage 1: Intake and Constraints
**Actions**: Identify domain, target venue, limits, deadline, advisor/graduation requirements. Review author guide for mandatory declarations. [BV1jvxEzaECD]
**Gate**: All constraints documented. **Failure**: Skipping author guide causes desk rejection before review.

### Stage 2: Literature / Paper Matrix
**Actions**: Collect last 2-3 years of papers from target venue. Build matrix: paper, method, dataset, baseline, result, gap. Identify adaptable modules. [BV19jCrYsEoE, BV1vt4y1T7sy]
**Gate**: Baselines are recent; same-domain comparators identified. **Failure**: Outdated baselines or only weak competitors. [BV1dg411p7QP]

### Stage 3: Story Architecture
**Actions**: Build narrative: gap -> motivation -> method -> evidence. Never lead with the method; lead with the problem. [BV1cH4y1j742, BV1ne41157Gn]
**Gate**: Innovation framed as problem resolution, not technical description. **Failure**: "We propose X" without narrative buildup. [BV1cH4y1j742]

### Stage 4: Evidence and Integrity Gate
**Actions**: Verify claims. Check ablation monotonicity. Confirm public datasets. No fabricated results or unsupported statistics. [BV19jCrYsEoE, BV1fV4y1B72F]
**Gate**: Every claim has evidence. Ablation order monotonic. No unsupported absolutes. **Failure**: Inconsistent ablations; selective baseline presentation. [BV14c411A75s]

### Stage 5: Section Plan
**Actions**: Outline jobs: Abstract (plain language), Introduction (gap+motivation+contribution), Related Work (positioning), Method (derivation), Experiments (baselines+ablation), Conclusion (findings+scope). [BV17s4y127VF, BV1JD4y1V7ar]
**Gate**: Abstract readable by non-specialist; conclusion deepens abstract. **Failure**: Jargon-heavy abstract; conclusion repeats abstract. [BV1mP411Z7tn]

### Stage 6: Draft or Polish
**Actions**: Imitate target venue style. Use LaTeX for English. Apply claim verb calibration. Ensure topic-evidence-boundary per paragraph. [BV12M4y1J737, BV1jvxEzaECD]
**Gate**: Formatting matches template; innovations follow gap-method-evidence arc. **Failure**: Poor formatting triggers attitude-based rejection. [BV1mP411Z7tn]

### Stage 7: Reviewer Audit
**Actions**: Run four independent lenses. Prepare rebuttal template for top attack vectors. [See reviewer-audit route]
**Gate**: Lenses completed independently; template covers 7 attack vectors. **Failure**: Fixating on methodology while ignoring formatting/abstract. [BV1mP411Z7tn]

### Stage 8: Revision Roadmap
**Actions**: Prioritize: formatting > abstract > derivations > technical fixes. Prepare response file (editor thank-you, point-by-point, highlighted changes). [BV12M4y1J737]
**Gate**: Response file follows standard format; all reviewer citations added. **Failure**: Arguing with reviewers instead of deferring.

### Stage 9: Final Quality Gate
**Actions**: Verify: abstract readability, formatting, chapter conclusions, mandatory declarations, submission files (manuscript + response + images). [BV1mP411Z7tn, BV1jvxEzaECD]
**Gate**: "Strong abstract + perfect formatting + solid chapter summaries = 90% pass rate." **Failure**: Missing declarations; unreviewed author guide checklist.

## Pipeline Heuristics

- **Submit highest viable venue first**: Use rejection feedback iteratively. [BV16X4y1h7og]
- **Never delay revisions**: Late submission signals poor attitude. [BV12M4y1J737]
- **Public datasets over private**: Faster iteration, less complexity. [BV19jCrYsEoE]
- **Imitate the target venue**: Match recent papers' structure, tone, framing. [BV12M4y1J737]
