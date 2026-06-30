# Route: Reviewer Audit

Use for pre-submission review, advisor defense preparation, rejection-risk audit, rebuttal preparation, or checking whether a story is defensible.

## Independent Lenses

1. **Methodology**: protocol, controls, metrics, ablations, reproducibility, statistics.
2. **Domain**: relevance, baseline currency, field fit, prior-work positioning.
3. **Skeptical reviewer**: likely rejection reasons, hidden assumptions, overclaims.
4. **Integrity**: citation, data provenance, reused code, negative evidence, authorship boundary.

## Seven Reviewer Personas

| Persona | Focus | What to check |
|---|---|---|
| Devil's Advocate | Contradictions | Internal consistency, hidden assumptions |
| Domain Expert | Field fit | Baseline currency, terminology accuracy |
| Methodological | Rigor | Protocol, controls, statistics, reproducibility |
| Editorial | Presentation | Structure, clarity, figure quality |
| Perspective | Broader impact | Significance, generalizability |
| Field Analyst | Positioning | Related work completeness, novelty claim |
| EIC | Acceptance decision | Overall contribution, venue fit |

## Synthesis Rule

Write independent findings before synthesis. Preserve minority or skeptical concerns unless resolved by evidence.

---

## Common Reviewer Attack Vectors

| Attack vector | What reviewer looks for | Recommended response |
|---|---|---|
| Awkward or unclear sentences | Language quality signals carelessness | Have someone else proofread before submission; never rely on self-review alone. [BV1EV4y1P7PQ] |
| Cited concepts without explanation | Unfamiliar terminology left undefined | Every cited concept must be explained or removed. If you wrote it, verify it is correct. [BV1EV4y1P7PQ] |
| Theory and results without derivation | Missing process or derivation steps | Include derivation or rationale for every formula; never show equation + result alone. [BV1EV4y1P7PQ] |
| Formatting inconsistency | Layout signals lack of discipline | Format is the first thing reviewers notice; poor formatting triggers attitude-based rejection. [BV1mP411Z7tn] |
| Weak abstract | Failure to summarize contribution clearly | Abstract is the core gate; write it so a non-specialist can understand. Poor abstract gives reviewers a reason to reject. [BV1mP411Z7tn, BV17s4y127VF] |
| Source code requests | Reproducibility or data concern | Provide partial code (claim you are cleaning up or annotating); never volunteer that only partial code is available. [BV18Ve6zvEBT] |
| Insufficient novelty | Incremental contribution framing | Never state what you did objectively; frame as "discovered a gap -> designed a method -> solved the problem." [BV1cH4y1j742] |

## Reviewer Psychology Insights

- **First impression gate**: Reviewers scan abstract and formatting first. If those are poor, they look for reasons to reject. [BV1mP411Z7tn]
- **Proportional rejection**: Blind review rejects a fixed ratio (roughly 10-30%). You only need to be better than the bottom tier of submissions in that cycle. [BV1mP411Z7tn]
- **Fatigue exploitation**: By the time reviewers reach the method section they are often fatigued. Front-load your strongest evidence in the introduction (results figures, not formulas) to anchor them before they see the technical details. [BV1cH4y1j742]
- **Curiosity vs scrutiny**: Reviewers question what looks unfamiliar. If a concept is cited but unexplained, it invites deep probing. Every term you use must be defensible. [BV1EV4y1P7PQ]
- **Defense attitude signals**: In thesis defense, examiners evaluate attitude more than content after blind review already passed. Respectful, non-confrontational responses reduce risk. [BV1eD421A7Bh]

## Rebuttal Strategy Patterns

| Principle | Detail | Source |
|---|---|---|
| Defer, do not debate | Accept criticism when possible. Only push back when a fix is genuinely impossible. Core rule: "do not argue, satisfy, and excessive reasoning breeds tolerance." | [BV12M4y1J737] |
| Evidence-based pushback | When you must disagree, cite specific literature or data. Never say "I think this is unnecessary" without references. | [BV12M4y1J737] |
| Add recommended references | Include every reference the reviewer suggests, even if loosely relevant. Cost is low; perceived compliance is high. | [BV12M4y1J737] |
| Gratitude per comment | Thank the reviewer in every single response point. | [BV12M4y1J737] |
| Upload first, explain later | Submit the revised files before writing the explanation. Order matters: revision first, justification second. | [BV18Ve6zvEBT] |
| Response file structure | (1) Thank the editor. (2) Copy reviewer comments verbatim, highlight in red, reply point-by-point. (3) Paste screenshots of changes. (4) Highlight all modifications in manuscript. | [BV12M4y1J737] |

## Integrity Check Specifics

What reviewers actually check vs. what they claim:

| Claimed check | What actually triggers rejection | Source |
|---|---|---|
| "Novelty of contribution" | Framing, not raw novelty. A simple module wrapped in a strong narrative passes; a novel idea with poor framing fails. | [BV1cH4y1j742] |
| "Reproducibility" | Formatting and code availability signals. Full reproducibility is rarely verified; perceived willingness matters more. | [BV18Ve6zvEBT] |
| "Technical correctness" | Whether derivation steps are shown. Reviewers rarely re-derive formulas; missing derivations suggest sloppiness. | [BV1EV4y1P7PQ] |
| "Writing quality" | Abstract quality and chapter summaries. Many reviewers focus on these surface elements rather than full-text depth. | [BV1mP411Z7tn] |
| "Data integrity" | Dataset choice (public vs. private) and baseline recency. Outdated baselines signal weak benchmarking. | [BV19jCrYsEoE] |

## Audit Checklist

1. Run all four lenses independently before synthesis.
2. Check abstract readability for a non-specialist audience.
3. Verify every cited term is defined or contextually obvious.
4. Ensure derivation steps exist for all formulas.
5. Confirm formatting matches target journal template exactly.
6. Validate baseline models are recent and from the same domain.
7. Confirm every claim is supported by evidence shown in the paper.
8. Prepare rebuttal response file structure before submission.
