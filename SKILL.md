---
name: Academic-Stitcher-Skill
description: >-
  Triggered when the user wants to brainstorm or generate new academic/scientific research ideas by stitching existing domain problems with new methodologies. Use this skill to deconstruct research topics and recombine them with catalyst technologies to produce high-impact, Nature-level innovation concepts.
---

# Academic Stitcher Skill

## Core Instructions

1.  **Strict Layer Split**: Operate using a Static/Dynamic split.
    *   **Static Layer**: Use `references/stitching_rules.md` and `references/nature_benchmarks.md` as the fixed framework for innovation logic.
    *   **Dynamic Layer**: Adapt the execution based on the specific 'Target' abstract and 'Catalyst' technology provided by the user.
2.  **Two-Stage Workflow**:
    *   **Stage 1: Deconstruction & Stitching**: Run `scripts/stitcher.py` to parse inputs into Object, Method, and Scenario. Apply the catalyst technology to solve identified pain points.
    *   **Stage 2: Rigorous Review**: Validate every generated idea against `references/nature_benchmarks.md`. Reject any idea that lacks "Step-Change" innovation or relies on incremental improvements.
3.  **Scientific Prose Standard**:
    *   Adhere strictly to `references/writing_quality.md`.
    *   Prioritize process and methodology over speed and fluff.
    *   Use fact-driven claims. Eliminate all AI-generated filler (e.g., "In the rapidly evolving landscape", "It is worth noting").

## Behavioral Boundaries

*   **DO NOT** invent non-existent technologies or invalid scientific combinations.
*   **DO NOT** use generic descriptions. Every stitched idea must include a specific mechanism of action.
*   **DO NOT** include meta-comments or conversational filler (e.g., "Sure, I can help with that", "Here are your ideas").
*   **DO** provide specific, verifiable links between the Catalyst and the Target's pain points.

## Anti-Patterns to Avoid

*   **Buzzword Overload**: Avoid terms like "revolutionize", "game-changer", or "seamless integration".
*   **The "Recent Years" Trap**: Never start sentences with "In recent years" or "With the development of".
*   **Surface-Level Stitching**: Simply putting A and B together without a technical bridge is forbidden.
