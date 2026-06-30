# Route: Nature-Style Polish

Use when improving an existing draft's structure, argument flow, English, or Chinese-to-English academic expression.

## Diagnosis Order

Fix in this order:

1. paper type logic;
2. section job;
3. paragraph logic;
4. claim/evidence/boundary;
5. sentence clarity and style.

## Style Rules

- Prefer concise, evidence-weighted sentences.
- Calibrate verbs: strong evidence can support "show" or "demonstrate"; indirect trends use "suggest" or "indicate"; untested mechanisms use "may" or "could".
- Remove unsupported absolutes such as "first", "unique", "unprecedented", "complete", "always", and "never".
- Preserve scientific meaning over stylistic flourish.

---

## Chinese-to-English Translation Rules

| Rule | Source |
|---|---|
| Every sentence in a translated paper must be carefully weighed, even if English proficiency is limited. Reviewers may have been away from active research for years and read slowly. | [BV17s4y127VF] |
| When writing in Chinese, reference English sources; when writing in English, reference Chinese sources. Cross-language referencing reduces text-matching overlap. | [BV1EV4y1P7PQ] |
| The abstract must be understandable by a high-school student. The conclusion may use technical jargon and deeper theoretical language. These two sections serve different audiences. | [BV17s4y127VF] |
| Abstract summarizes Introduction + Related Work + Method: what you intended to do and how. Conclusion summarizes Method + Experiments: what you did and what was validated. Abstract sets up the story; conclusion extends it. | [BV1JD4y1V7ar] |
| Do not translate idioms or colloquial phrasing literally. Map Chinese discourse connectors to their English rhetorical equivalents (e.g., "however" for contrast, "furthermore" for extension). | [inferred] |

## Claim Verb Calibration

| Evidence strength | Appropriate verbs | Example |
|---|---|---|
| Direct measurement with controls | show, demonstrate, confirm, establish | "Our results confirm that X improves Y by 12%." |
| Correlational or indirect trend | suggest, indicate, point to, be consistent with | "These data suggest a positive association between X and Y." |
| Plausible but untested mechanism | may, could, might, would be expected to | "X may modulate Y through an as-yet-unknown pathway." |
| Theoretical or computational only | predict, model, predict, be predicted to | "Simulations predict that X will reduce Y under condition Z." |

Sources: [BV17s4y127VF, BV1cH4y1j742]

## Common Overclaim Patterns and Fixes

| Overclaim pattern | Problem | Fix | Source |
|---|---|---|---|
| "We propose the first method to..." | Unverifiable; invites refutation | Use "We present a method that..." or "To our knowledge..." | [BV1cH4y1j742] |
| "Our method achieves SOTA" | SOTA is transient and benchmark-dependent | Specify the benchmark, dataset, and comparison set: "Outperforms X on dataset Y" | [BV1LK9ZYYErM] |
| "This solves the problem" | Absolute claim with no boundary | Add scope: "This addresses the problem in the context of Z" | [BV17s4y127VF] |
| "All existing methods fail" | Overgeneralization | Narrow: "Several recent methods struggle with..." | [inferred] |
| Starting results with "surprisingly" | subjective judgment disguised as fact | Remove or replace with evidence: "Contrary to [ref], we found..." | [inferred] |

## Paragraph Flow Rules

| Element | Rule | Source |
|---|---|---|
| Topic sentence | State the claim or observation first, before evidence. | [BV1cH4y1j742] |
| Evidence body | Present data, figures, or reasoning that supports the topic sentence. One paragraph = one claim. | [BV17s4y127VF] |
| Boundary sentence | End the paragraph with scope, limitation, or transition to the next claim. Prevents overreach. | [inferred] |
| Narrative arc for innovations | Do not state the innovation directly. Build a chain: (1) identify the gap, (2) explain why it matters, (3) introduce the method, (4) show it works. | [BV1cH4y1j742, BV1ne41157Gn] |
| Information asymmetry | Present favorable information prominently. Unfavorable information, if necessary, should appear in a less conspicuous location (e.g., Related Work or a subordinate clause). Everything stated must be true; what is omitted is not fabrication. | [BV1Ns4y197EM] |

## Revision Checklist

1. Scan for absolute claims ("first", "unique", "always") and soften.
2. Verify each paragraph has topic-evidence-boundary structure.
3. Check abstract is readable by a non-specialist.
4. Check conclusion uses appropriate technical depth.
5. Ensure every innovation follows gap-method-evidence arc.
6. Review verb calibration against evidence strength.
7. Confirm no colloquial translation artifacts remain.
