# Output Format

Default to the user's language unless the requested prose is explicitly English.

Before any route-specific heading, write one compact detection line:

`Route: <route>; paper_type=<paper_type>; section=<section or none>; language=<language>`

This line satisfies the `SKILL.md` route announcement requirement. It does not replace the required headings below.

## Planning Output

```markdown
Route: stitch-plan; paper_type=<paper_type>; section=none; language=<language>

## Route
- Route:
- Paper type:
- Target:
- Evidence state:
- Checkpoint:

## Paper Stitching Map
- Inheritance:
- Failure mode:
- Delta:
- Mechanism:
- Evidence:
- Boundary:

## Claim-Evidence Map
| Claim | Evidence | Status | Boundary |
| --- | --- | --- | --- |

## Next Work Packages
| Work package | Output | Evidence needed | Risk |
| --- | --- | --- | --- |

## Quality Gates
- Evidence:
- Attribution:
- Fair comparison:
- Reviewer pressure:

## Missing Inputs
- Dataset / corpus:
- Metrics:
- Baselines:
- Compute / time budget:
- Advisor / venue constraints:
```

## Section Draft Output

```markdown
Route: section-draft; paper_type=<paper_type>; section=<section>; language=<language>

## Route
- Route:
- Paper type:
- Section:
- Language:

## Section Outline
- ...

## Source Trace
| Source phrase | Draft detail | Status |
| --- | --- | --- |

## Draft
...

## Claim-Evidence Map
| Claim | Evidence | Status | Boundary |
| --- | --- | --- | --- |

## Missing Inputs
- ...
```

## Review Output

```markdown
Route: reviewer-audit; paper_type=<paper_type>; section=<section or none>; language=<language>

## Independent Reviewer: Methodology
...

## Independent Reviewer: Domain
...

## Independent Reviewer: Skeptical
...

## Editorial Synthesis
...

## Revision Roadmap
...
```
