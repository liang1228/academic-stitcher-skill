---
name: Academic-Stitcher-Skill
description: >-
  Triggered when the user wants to brainstorm or generate new academic/scientific research ideas by stitching existing domain problems with new methodologies. Use this skill to deconstruct research topics and recombine them with catalyst technologies to produce high-impact, Nature-level innovation concepts.
triggers:
  - "When the user provides a research target/abstract and a catalyst technology"
  - "When the user asks to stitch or combine two different research domains or methods"
  - "When the user requests brainstorming of top-tier academic research ideas (Nature-level)"
---

# Academic Stitcher Skill

## Core Instructions

1.  **Isolate Execution Layers**:
    *   Initialize the static constraints from `references/constraints.md` and `references/nature_benchmarks.md` at start.
    *   Execute the dynamic stitching logic based on user-provided Target and Catalyst parameters.
2.  **Execute Two-Stage Workflow**:
    *   **Stage 1 (Deconstruction & Stitching)**: Run `scripts/academic_stitcher.py` to parse inputs into Object, Method, and Scenario. Apply the catalyst technology to resolve identified pain points.
    *   **Stage 2 (Rigorous Review)**: Pass results through the criteria defined in `references/nature_benchmarks.md`. Reject any idea that fails to demonstrate step-change innovation.
3.  **Refine Writing Quality**:
    *   Adhere strictly to style rules in `references/writing_quality.md`.
    *   Eliminate subjective hype, AI-generated filler, and banned phrases.
    *   Format output using concise, fact-driven prose.
