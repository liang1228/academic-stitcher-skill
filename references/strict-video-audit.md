# Strict Source Audit

## Scope

The task was to summarize the uploader's videos about `缝论文` and `论文故事` and distill them into a Codex skill. The strict version uses only public, reproducible evidence and records what could not be obtained.

## Acquisition Result

| Item | Result |
| --- | --- |
| Public space URL | `https://space.bilibili.com/383551518/upload/video` |
| Visible upload total | 547 videos, 14 pages |
| Verified public records | 528 unique BV IDs |
| Missing relative to visible total | 19 BV records |
| Primary API attempted | `x/space/wbi/arc/search` |
| Blocking observed | `code=-352` in shell; browser upload pagination showed `Request Error: [412]` |
| Fallback used | Bilibili public search API plus view API, filtered by `mid=383551518` |

This audit does not claim that the missing 19 videos were summarized. It claims that all target-topic videos found in the 528 verified public records were classified and distilled, and that the unresolved 19-record gap is explicitly preserved.

## Classification Result

| Label | Count | Meaning |
| --- | ---: | --- |
| core | 33 | Direct `学术裁缝` / `缝论文` / `论文故事` / paper-combination / paper-reading-for-writing videos |
| support | 88 | Thesis, journal, SCI, related-work, method-reading, submission, and graduate-writing workflow videos |
| background | 104 | Graduate-school and research-survival context that informs tone but not the core method |
| out | 303 | Non-target videos excluded from distillation |

Classification was title-led. Search tags were not enough for core classification because broad uploader/search tags overmatched unrelated videos. Description hits were allowed only as support context.

## Subtitle And BiliGPT Check

The user pointed to `Yuiffy/BiliGPT`. The repo's Bilibili path is useful for single-video evidence: fetch video metadata, choose `aid/cid`, query player metadata, inspect subtitle entries, fetch subtitle JSON when available, then reduce timestamped text.

Initial no-login check applied to the 33 core videos:

| Metric | Result |
| --- | ---: |
| Core videos checked | 33 |
| Videos exposing subtitle entries | 0 |
| Videos without subtitles | 33 |
| Request errors | 0 |

After the user provided a temporary Bilibili `SESSDATA`, the 75 BVIDs represented in `work/transcripts_raw/` were retried through the same metadata/player/subtitle path. The credential was used only as an environment variable for the run and was not written into deliverables.

| Metric | Result |
| --- | ---: |
| Raw transcript BVIDs checked | 75 |
| Downloadable AI subtitles | 70 |
| Empty subtitle URL | 4 |
| No subtitle entry | 1 |
| Heuristic likely relevant | 23 |
| Heuristic mixed review | 3 |
| Heuristic too short | 19 |
| Heuristic likely mismatch | 25 |
| Unavailable | 5 |
| Regenerated distilled notes | 75 |
| Used for method distillation | 26 |
| Evidence-boundary records | 49 |

The subtitle result is therefore evidence for selective transcript use, not a blanket approval. Some downloadable subtitles are unrelated to the paper-topic title. `transcripts_distilled/` has been regenerated with explicit used/not-used decisions, and the aggregated safe rules live in `transcript-derived-playbook.md`. See `ai-transcript-coverage.csv` and `transcript-distillation-audit.md`.

## Distillation Policy

The skill keeps the useful teaching pattern while converting unsafe wording into compliant academic practice:

- `学术裁缝` becomes literature-informed modular design with attribution and experiments.
- `编故事` becomes problem-mechanism-evidence narrative construction.
- `水论文` becomes choosing a realistic venue and bounded claim instead of overclaiming.
- `降重` or hidden reuse is treated as a refusal boundary unless the user reframes it as legitimate synthesis and citation.
- Every suggested paper plan must name inheritance, delta, mechanism, evidence, and risk.

## Package Files

- `SKILL.md`: executable skill instructions.
- `references/video-index.md`: strict source index and core/support table.
- `references/strict-video-catalog.csv`: all 528 verified records with labels.
- `references/biligpt-core-evidence.csv`: subtitle availability evidence for the 33 core videos.
- `references/ai-transcript-coverage.csv`: SESSDATA-based subtitle coverage and relevance audit for 75 selected transcript BVIDs.
- `references/transcript-distillation-audit.md`: audit of the current distilled transcript directory.
- `references/transcript-derived-playbook.md`: aggregated safe rules from the 26 usable transcript records.
- `references/playbook.md`: reusable templates and operating patterns.
- `agents/openai.yaml`: optional agent metadata.
