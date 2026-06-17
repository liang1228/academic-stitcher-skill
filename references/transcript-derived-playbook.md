# Core Distilled Playbook

This is the retained core distillation from the audited 75-video transcript set. It keeps only reusable method rules and excludes unavailable, too-short, or likely mismatched source material from method distillation.

The repository intentionally omits intermediate artifacts such as raw transcripts, per-video distilled notes, subtitle coverage CSVs, and acquisition audit tables. Use this file as the compact source-informed rule summary.

## Coverage

| Bucket | Count |
| --- | ---: |
| Distilled files generated | 75 |
| Used for method distillation | 26 |
| Recorded but not used | 49 |
| likely_relevant | 23 |
| mixed_review | 3 |
| too_short | 19 |
| likely_mismatch | 25 |
| unavailable | 5 |

## Reusable Rules

| Theme | Evidence hits | Safe rule | Example BVIDs |
| --- | ---: | --- | --- |
| 目标层级与发表定位 | 24 | 先确定最低可接受目标和真实资源，再反推论文故事、工作量和实验深度。 | `BV11D421J79N`, `BV12xPceUEDn`, `BV16y421q7jy`, `BV17s421N7am`, `BV19jCrYsEoE`, `BV1CP411G7VX`, `BV1GX4y1k7jn`, `BV1MX4y1p7UY` |
| 继承链与基线选择 | 23 | 先找到可复现、可引用、可解释的基座；没有基座时先补文献和复现实验，不直接编创新。 | `BV12xPceUEDn`, `BV16y421q7jy`, `BV17s421N7am`, `BV19jCrYsEoE`, `BV1CP411G7VX`, `BV1GX4y1k7jn`, `BV1MX4y1p7UY`, `BV1Qs4y1d7BF` |
| 模块拼接与变量设计 | 22 | 每个新增模块都必须对应一个失败模式、机制解释和可验证的增量贡献。 | `BV12xPceUEDn`, `BV16y421q7jy`, `BV17s421N7am`, `BV19jCrYsEoE`, `BV1CP411G7VX`, `BV1GX4y1k7jn`, `BV1MX4y1p7UY`, `BV1UB4y1j7Vv` |
| 论文故事与写作主线 | 26 | 把模块列表改写成问题-机制-证据链；相关工作按论证角色组织，而不是堆论文。 | `BV11D421J79N`, `BV12xPceUEDn`, `BV16y421q7jy`, `BV17s421N7am`, `BV19jCrYsEoE`, `BV1CP411G7VX`, `BV1GX4y1k7jn`, `BV1MX4y1p7UY` |
| 实验与证据链 | 24 | 每个关键 claim 至少绑定一种证据：主结果、消融、鲁棒性、复杂度或失败案例。 | `BV11D421J79N`, `BV12xPceUEDn`, `BV16y421q7jy`, `BV17s421N7am`, `BV19jCrYsEoE`, `BV1CP411G7VX`, `BV1MX4y1p7UY`, `BV1Qs4y1d7BF` |
| 检索、投稿与返修流程 | 19 | 把论文工作拆成可执行流程：检索矩阵、证据补齐、选刊匹配、返修逐点响应。 | `BV11D421J79N`, `BV12xPceUEDn`, `BV17s421N7am`, `BV19jCrYsEoE`, `BV1CP411G7VX`, `BV1MX4y1p7UY`, `BV1Qs4y1d7BF`, `BV1YT411T7MD` |
| 学术诚信与风险边界 | 22 | 所有复用必须有引用和真实增量；数据、引用、署名、实验结果不允许虚构或隐藏。 | `BV11D421J79N`, `BV12xPceUEDn`, `BV17s421N7am`, `BV19jCrYsEoE`, `BV1CP411G7VX`, `BV1GX4y1k7jn`, `BV1MX4y1p7UY`, `BV1UB4y1j7Vv` |

## Final Distillation

- Start with the realistic venue or graduation target; do not inflate claims beyond evidence.
- Build a paper matrix before proposing modules; every module needs a cited origin and a reason to exist.
- Convert A+B into a mechanism: name A's failure mode, why B addresses it, and how the experiment proves it.
- Write related work as an argument for the gap, not as an unordered literature dump.
- Bind every claim to evidence: main result, ablation, robustness, complexity, qualitative cases, or explicit limitation.
- Treat all shortcut or misconduct-adjacent wording as a refusal boundary and replace it with attribution, reproducibility, and bounded claims.

## Excluded Intermediate Artifacts

- Do not import raw transcript text.
- Do not import rules from rows that were marked `likely_mismatch`, `too_short`, or `unavailable` during audit without manual review.
- Do not turn grey-area statements into operational advice.
- Do not use title-only evidence as proof that a transcript contains that topic.
