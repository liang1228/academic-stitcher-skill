# Strict Video Index

This index records the strict public-video evidence used to distill `academic-stitcher-skill` from `水论文的程序猿-水导`'s Bilibili uploads. It focuses on videos about `学术裁缝`, `缝论文`, paper-story construction, reading papers for writing, related work, method sections, journals, and thesis survival.

## Coverage Boundary

As of 2026-06-17, the public upload page for `mid=383551518` displayed `547` uploads and `14` pages. Direct upload pagination through Bilibili's `x/space/wbi/arc/search` path was blocked by risk controls in this environment: shell requests returned `code=-352`, and browser page-2 loading surfaced `Request Error: [412]`. The strict dataset therefore records the verified public-access boundary instead of claiming a private scrape.

| Evidence bucket | Count | Handling |
| --- | ---: | --- |
| Official visible upload total | 547 | Browser-visible count on the public upload page |
| Verified public records | 528 | Public search/view API records filtered by `mid=383551518` |
| Unresolved upload gap | 19 | Not reachable through the public methods available in this run |
| Core target videos | 33 | Main source set distilled into the skill |
| Supporting target videos | 88 | Secondary evidence for thesis, journal, reading, and workflow tactics |
| Background/context videos | 104 | Used only for audience, tone, and boundary context |
| Out-of-scope videos | 303 | Excluded from the distilled method |
| Initial no-login core subtitle exposure | 0/33 | Earlier BiliGPT-style check without SESSDATA exposed no subtitle list |
| User-provided SESSDATA transcript set | 75 | Selected core/support BVIDs from `work/transcripts_raw/` |
| Downloadable AI subtitles in transcript set | 70/75 | Technical fetch success; relevance still requires audit |
| Likely relevant AI subtitles in transcript set | 23/75 | Heuristic only; see `ai-transcript-coverage.csv` |
| Regenerated distilled transcript notes | 75/75 | 26 used for method distillation, 49 kept as evidence-boundary records |

Full exported catalog: `strict-video-catalog.csv`.
BiliGPT no-login subtitle evidence for the 33 core videos: `biligpt-core-evidence.csv`.
User-provided SESSDATA transcript coverage: `ai-transcript-coverage.csv`.
Transcript distillation audit: `transcript-distillation-audit.md`.
Transcript-derived method playbook: `transcript-derived-playbook.md`.
Detailed acquisition notes: `strict-video-audit.md`.

## Core Target Videos

| # | Date | Duration | BV | Title | Initial no-login subtitle status |
| --- | --- | ---: | --- | --- | --- |
| 1 | 2022-09-20 | 16:29 | [BV1YT411T7MD](https://www.bilibili.com/video/BV1YT411T7MD/) | 学术妲己拯救你做一个优秀的学术裁缝，没有继承且无法复现论文模型怎么办？ | no_subtitle |
| 2 | 2022-09-22 | 22:24 | [BV11g41127Zn](https://www.bilibili.com/video/BV11g41127Zn/) | 教你做称职的学术裁缝(纯干货)，明白顶刊和水刊的意义~ | no_subtitle |
| 3 | 2022-10-10 | 15:09 | [BV1ne41157Gn](https://www.bilibili.com/video/BV1ne41157Gn/) | 水论文如何吹一个好故事，伟大者剽窃，核心思想是复刻 | no_subtitle |
| 4 | 2023-01-15 | 11:30 | [BV1mK411C7WH](https://www.bilibili.com/video/BV1mK411C7WH/) | 缝(水)完论文模型一眼被拒，怎么去写水文真的很重要 | no_subtitle |
| 5 | 2023-04-08 | 34:56 | [BV1qv4y1n7dx](https://www.bilibili.com/video/BV1qv4y1n7dx/) | 35分钟教你从0到1，水出SCI（精品），学术裁缝必修课 | no_subtitle |
| 6 | 2023-05-25 | 04:04 | [BV1fV4y1B72F](https://www.bilibili.com/video/BV1fV4y1B72F/) | 学术裁缝调参术，轻松解决消融难题 | no_subtitle |
| 7 | 2023-08-05 | 09:47 | [BV1xz4y1p7Fj](https://www.bilibili.com/video/BV1xz4y1p7Fj/) | 学术裁缝，水论文保毕业的，可行性分析，首次解读 | no_subtitle |
| 8 | 2023-08-07 | 11:46 | [BV1yk4y1g7KS](https://www.bilibili.com/video/BV1yk4y1g7KS/) | 新老粉丝专享，学术裁缝中的基准模型，手把手教你找 | no_subtitle |
| 9 | 2023-08-08 | 09:23 | [BV1b14y1q7ju](https://www.bilibili.com/video/BV1b14y1q7ju/) | 手把手带你找，学术裁缝中的模块，Sci真不难系列 | no_subtitle |
| 10 | 2023-11-01 | 08:40 | [BV1a94y1G7Xp](https://www.bilibili.com/video/BV1a94y1G7Xp/) | 学术裁缝是学术不端？我的视频误人子弟？ | no_subtitle |
| 11 | 2024-05-10 | 09:54 | [BV17s421N7am](https://www.bilibili.com/video/BV17s421N7am/) | 学术裁缝(财富)让你保底毕业，学会编故事让你的论文更上一个级别，CVPR带读 | no_subtitle |
| 12 | 2024-07-31 | 09:59 | [BV1ir421K7kC](https://www.bilibili.com/video/BV1ir421K7kC/) | 生动形象的说清楚，学术论文如何编一个好故事 | no_subtitle |
| 13 | 2024-10-21 | 43:54 | [BV1tUy5YkEXe](https://www.bilibili.com/video/BV1tUy5YkEXe/) | 论文A+B的组合能发新论文吗？顶刊更看重什么？没有导师带怎么发顶刊？ | no_subtitle |
| 14 | 2024-11-05 | 04:25 | [BV1jQD8Y7Exh](https://www.bilibili.com/video/BV1jQD8Y7Exh/) | 如何高效学习，高效阅读论文，实现科研上的自由 | no_subtitle |
| 15 | 2025-02-06 | 49:00 | [BV1dzNWewExA](https://www.bilibili.com/video/BV1dzNWewExA/) | 学术裁缝的核心，不是缝模块，而是编故事，20250126(2) | no_subtitle |
| 16 | 2025-02-21 | 43:32 | [BV12xPceUEDn](https://www.bilibili.com/video/BV12xPceUEDn/) | 研究生们，学术裁缝绝不是学术不端，除非你想学术不端，20250216(2)， | no_subtitle |
| 17 | 2025-04-03 | 11:25 | [BV1UZZUY6E6X](https://www.bilibili.com/video/BV1UZZUY6E6X/) | 你看的论文我看的论文不一样，学术裁缝要看哪类论文，001 | no_subtitle |
| 18 | 2025-05-03 | 22:54 | [BV1rPGdz3E2V](https://www.bilibili.com/video/BV1rPGdz3E2V/) | 看论文咬文嚼字？谁爱搞科研谁搞去，我就搞学术裁缝！！！005，相关工作 | no_subtitle |
| 19 | 2025-05-04 | 06:57 | [BV1B1VAzxELR](https://www.bilibili.com/video/BV1B1VAzxELR/) | 学术裁缝虽好用，但不兴搬到台面上来讲呀！小不忍则乱大谋 | no_subtitle |
| 20 | 2025-05-05 | 27:10 | [BV16KVzzfEPh](https://www.bilibili.com/video/BV16KVzzfEPh/) | 学术裁缝不仅可以缝模块，还有一种新颖的水论文工作量的方法，006， | no_subtitle |
| 21 | 2025-05-12 | 43:29 | [BV1inEJzLEcG](https://www.bilibili.com/video/BV1inEJzLEcG/) | 不做实验的学术裁缝是不端，做实验的学术裁缝是基操，20250507， | no_subtitle |
| 22 | 2025-05-13 | 19:52 | [BV1W5EAzLErh](https://www.bilibili.com/video/BV1W5EAzLErh/) | 学术裁缝新人看完这期，至此已成艺术，论文方法章节怎么阅读，007 | no_subtitle |
| 23 | 2025-05-21 | 17:46 | [BV12WJ6zoEa6](https://www.bilibili.com/video/BV12WJ6zoEa6/) | 如何读论文进而水论文，成为优秀的学术裁缝，完结撒花，009 | no_subtitle |
| 24 | 2025-06-04 | 47:54 | [BV13RTjzKEPZ](https://www.bilibili.com/video/BV13RTjzKEPZ/) | 看完视频只有一个感想：读论文从未如此简单过，010 | no_subtitle |
| 25 | 2025-06-11 | 34:06 | [BV1rDMHzTEEd](https://www.bilibili.com/video/BV1rDMHzTEEd/) | 清华联合腾讯的一篇顶会，标准的学术裁缝，做的实验也不过如此，011 | no_subtitle |
| 26 | 2025-06-21 | 32:20 | [BV1U9N1zrEQW](https://www.bilibili.com/video/BV1U9N1zrEQW/) | 学术裁缝搜哪些论文，又该如何一篇篇下载并整理 | no_subtitle |
| 27 | 2025-06-26 | 54:49 | [BV1npKfzPEuC](https://www.bilibili.com/video/BV1npKfzPEuC/) | 当你开始仅论文论，缝论文从未如此简单过，学术裁缝速成入门，012 | no_subtitle |
| 28 | 2025-07-02 | 28:52 | [BV1ut34zuEfS](https://www.bilibili.com/video/BV1ut34zuEfS/) | 学术裁缝的话，论文方法部分如何写作，013 | no_subtitle |
| 29 | 2025-08-13 | 17:50 | [BV1mxbezeEhV](https://www.bilibili.com/video/BV1mxbezeEhV/) | 论文不就是，模仿、抄和降重吗，真不知道有啥难度，相关工作，015 | no_subtitle |
| 30 | 2025-10-16 | 04:53 | [BV1evWizBEvd](https://www.bilibili.com/video/BV1evWizBEvd/) | 水论文保毕业不是学术裁缝上限，顶刊顶会包也适用的 | no_subtitle |
| 31 | 2025-12-26 | 06:57 | [BV1FKBXBCE84](https://www.bilibili.com/video/BV1FKBXBCE84/) | 仅想快速毕业，如何高效阅读论文 | no_subtitle |
| 32 | 2026-01-29 | 14:42 | [BV1Ht6wBVES1](https://www.bilibili.com/video/BV1Ht6wBVES1/) | 当你开始仅论文论，一年百篇不是梦！ | no_subtitle |
| 33 | 2026-02-08 | 49:38 | [BV1nhFZz7E8D](https://www.bilibili.com/video/BV1nhFZz7E8D/) | 二探川大83页举报信，给研究生们的启发！当你仅论文论，论文发表好像很简单！严厉抵制学术不端！ | no_subtitle |

## Supporting Target Sample

The full supporting set has 88 videos. The sample below shows the newest 20; see `strict-video-catalog.csv` for the complete classification.

| # | Date | Duration | BV | Title |
| --- | --- | ---: | --- | --- |
| 1 | 2026-03-15 | 12:27 | [BV1ihw3zUEDy](https://www.bilibili.com/video/BV1ihw3zUEDy/) | 毕业大论文，盲审通过概率+100%，最后一次应该检查的内容，佛渡有缘研究生，过了这村，没这个店 |
| 2 | 2026-03-08 | 10:33 | [BV1KBNGzCELr](https://www.bilibili.com/video/BV1KBNGzCELr/) | S.H.I.T期刊，假期刊出现“真”论文？ |
| 3 | 2026-02-16 | 11:34 | [BV15eZTBxErS](https://www.bilibili.com/video/BV15eZTBxErS/) | 教水论文救不了研究生，反复熏陶才能看清答案 |
| 4 | 2026-02-13 | 31:10 | [BV1r4cEz6ETb](https://www.bilibili.com/video/BV1r4cEz6ETb/) | 大论文盲审专家，会质疑数据真假吗？20260209 |
| 5 | 2026-02-09 | 06:16 | [BV1j9cKzeEUn](https://www.bilibili.com/video/BV1j9cKzeEUn/) | 三探川大王竹卿硕士论文，现在的研究生太难了 |
| 6 | 2025-12-17 | 08:32 | [BV1Fuq5BPEye](https://www.bilibili.com/video/BV1Fuq5BPEye/) | 我必须发顶刊，你咋不当院士，给我点背景，当代研究生该硬硬 |
| 7 | 2025-10-09 | 05:47 | [BV1jvxEzaECD](https://www.bilibili.com/video/BV1jvxEzaECD/) | 手把手带你给论文，选择合适的期刊，再带你走通投稿流程 |
| 8 | 2025-09-11 | 14:48 | [BV1NoHvzmETH](https://www.bilibili.com/video/BV1NoHvzmETH/) | 论文这么简单，为啥你看不懂，为啥你写不来？论文摘要和总结怎么写，017， |
| 9 | 2025-09-06 | 41:44 | [BV1rAYKznEcK](https://www.bilibili.com/video/BV1rAYKznEcK/) | 研三的同学们，大论文要开始动笔了，就业更要时刻盯着，20250901， |
| 10 | 2025-07-26 | 29:00 | [BV1fk8bz3EyW](https://www.bilibili.com/video/BV1fk8bz3EyW/) | 读研一定要明确，你是来认真搞科研，还是水论文保毕业，20250721， |
| 11 | 2025-05-28 | 04:31 | [BV1i5jqzxEbu](https://www.bilibili.com/video/BV1i5jqzxEbu/) | 哪个研究生这年头，还自己搜论文去看，自己从0到1写论文呀！ |
| 12 | 2025-05-26 | 40:27 | [BV1T7j7zXEst](https://www.bilibili.com/video/BV1T7j7zXEst/) | 大论文盲审过了，别想太多，毕业答辩过了，更不要想太多，20250523 |
| 13 | 2025-04-18 | 25:37 | [BV1zB5EzgED4](https://www.bilibili.com/video/BV1zB5EzgED4/) | 看论文咬文嚼字？谁爱搞科研谁搞去，我不搞！！！003 |
| 14 | 2025-04-04 | 09:47 | [BV1ooZoYVEeX](https://www.bilibili.com/video/BV1ooZoYVEeX/) | 仅适用于仅想水一篇论文保毕业的研究生，不适合正儿八经搞科研的，002 |
| 15 | 2025-03-21 | 19:03 | [BV1xhXkYTERF](https://www.bilibili.com/video/BV1xhXkYTERF/) | 助力大论文盲审最后一步，剖析大论文盲审细则表 |
| 16 | 2025-03-07 | 11:00 | [BV1bn92YWEy1](https://www.bilibili.com/video/BV1bn92YWEy1/) | 复旦大学博后，四篇硕论一字不漏的抄，发表成四篇顶刊，一些小启发吧！ |
| 17 | 2025-01-06 | 07:20 | [BV1crrLYxE5Z](https://www.bilibili.com/video/BV1crrLYxE5Z/) | 每个研究生都要明白的道理，努力推动科研发展，还是水论文保毕业 |
| 18 | 2024-12-30 | 34:49 | [BV1c263YkEce](https://www.bilibili.com/video/BV1c263YkEce/) | 延毕只有老实人，佛也只渡有缘人，他们如何1个月写出1篇大论文 |
| 19 | 2024-12-26 | 43:02 | [BV19jCrYsEoE](https://www.bilibili.com/video/BV19jCrYsEoE/) | 水论文1个原则，能用公共数据集，不用私有数据集，20241222 |
| 20 | 2024-12-08 | 41:27 | [BV1iaqWYfEGq](https://www.bilibili.com/video/BV1iaqWYfEGq/) | 没数据能发论文吗？没代码能发论文吗？没结果能发论文吗？20241204 |

## Distilled Themes

- Venue level comes before story ambition: graduation, course paper, SCI, conference, and top venue require different claims and evidence.
- Inheritance chain comes before innovation theater: every new paper plan needs a baseline, paper family, dataset, and reusable lineage.
- Module stitching is acceptable only when a failure mode, mechanism, and experiment connect the parts.
- A+B is not a contribution by itself; the contribution is the reason B repairs A and the evidence that proves it.
- Related work should be organized by argumentative role, not as a flat paper list.
- Method reading should extract input, output, assumptions, variables, ablations, and reusable deltas.
- Paper stories should be narrow, testable, and bounded by available experiments.
- Ethical boundaries are non-negotiable: no fabricated data, fake citations, hidden reuse, or claims beyond evidence.
