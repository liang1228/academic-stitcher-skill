# Academic Stitcher Skill

`academic-stitcher-skill` is a Codex skill for turning related papers, baseline models, modules, experiment results, and rough thesis ideas into a defensible academic paper story.

The skill is distilled from public Bilibili videos by `水论文的程序猿-水导`, especially the `学术裁缝`, `缝论文`, and paper-story videos. It deliberately converts grey-area wording into compliant research practice: attribution, real deltas, reproducible experiments, bounded claims, and refusal of fabricated data or plagiarism.

## Structure

- `SKILL.md`: skill entrypoint, trigger description, workflow, and safety boundaries.
- `agents/openai.yaml`: UI metadata for Codex skill listings.
- `references/video-index.md`: strict source index and core/support video table.
- `references/strict-video-audit.md`: acquisition boundary for the 547 visible uploads and 528 verified public records.
- `references/strict-video-catalog.csv`: all 528 verified public records with classification labels.
- `references/ai-transcript-coverage.csv`: AI subtitle coverage and relevance audit for 75 selected core/support BVIDs.
- `references/transcript-distillation-audit.md`: audit of regenerated transcript distillations.
- `references/transcript-derived-playbook.md`: safe rules distilled from the 26 usable transcript records.
- `references/playbook.md`: reusable templates for paper matrices, story spines, sections, and evidence checks.
- `transcripts_distilled/`: 75 audited per-video distillation notes; 26 are used for method extraction and 49 are evidence-boundary records.

## Evidence Boundary

The public uploader page showed 547 uploads. Public search/view paths verified 528 records in this environment; 19 upload records remain unresolved because Bilibili upload pagination triggered risk controls.

For the 75 transcript BVIDs:

- 70 had downloadable AI subtitles.
- 5 were unavailable.
- 26 were used for method distillation.
- 49 were retained only as evidence-boundary records.

Do not treat a downloadable subtitle as automatically relevant. Check `references/ai-transcript-coverage.csv` and the matching file under `transcripts_distilled/` before using any video as evidence.

## Validation

Validated with:

```powershell
$env:PYTHONUTF8='1'
D:\software\Anaconda3\envs\pytorch_env\python.exe C:\Users\zeooon3\.codex\skills\.system\skill-creator\scripts\quick_validate.py .
```

Expected result:

```text
Skill is valid!
```
