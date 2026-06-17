# Transcript Distillation Audit

## Verdict

`outputs/academic-stitcher-skill/transcripts_distilled/` has been regenerated and is now complete for the 75-video transcript set.

The regenerated directory is safe to use as an audited evidence layer because every BVID has an explicit source status, relevance status, and distillation decision. Videos with unavailable, too-short, or likely mismatched subtitles are recorded but not used to derive method rules. Grey-area academic wording is converted into compliance boundaries instead of executable advice.

## Coverage

| Item | Count |
| --- | ---: |
| Raw timestamped transcript files in `work/transcripts_raw/` | 75 |
| Regenerated distilled markdown files | 75 |
| Missing distilled files | 0 |
| Extra distilled files without coverage row | 0 |
| Core distilled files | 15 |
| Support distilled files | 60 |
| Used for method distillation | 26 |
| Recorded but not used | 49 |

A backup of the previous 65-file first pass was saved under `work/transcripts_distilled_backup_*`.

## AI Subtitle Fetch Result

Using the temporary Bilibili `SESSDATA`, Bilibili AI subtitle fetching was retried for the 75 raw transcript BVIDs. The credential was not written into scripts, reports, or deliverables.

| Status | Count |
| --- | ---: |
| ok | 70 |
| empty_subtitle_url | 4 |
| no_subtitle | 1 |

Full machine-readable table: `ai-transcript-coverage.csv`.

## Relevance And Use Decision

| Relevance | Count |
| --- | ---: |
| likely_relevant | 23 |
| mixed_review | 3 |
| too_short | 19 |
| likely_mismatch | 25 |
| unavailable | 5 |

Distillation policy:

- `likely_relevant` and `mixed_review` rows are distilled into safe method rules.
- `too_short`, `likely_mismatch`, and `unavailable` rows are retained only as evidence-boundary records.
- No raw transcript text is imported into the skill body.
- Unsafe or misconduct-adjacent wording is rewritten as refusal/compliance boundaries.

## Unavailable AI Subtitle Items

| BVID | Label | Status | Title |
| --- | --- | --- | --- |
| `BV1Cx4y187J8` | support | empty_subtitle_url | 研究生大论文返修延毕名单出来后，聊聊延毕只有老实人这个规律 |
| `BV1F24y1A7kw` | support | empty_subtitle_url | 期刊小论文和毕业大论文的“新”有什么区别 |
| `BV1VvDQYBErA` | support | empty_subtitle_url | 40分钟长视频，关于小论文的粉丝千问千答，错过后悔一辈子 |
| `BV1oP411x7H3` | support | no_subtitle | 求你别再自我意淫学术小论文了！开始带你动笔，纯净干货无广告 |
| `BV1us4y1A75M` | support | empty_subtitle_url | 指导过的双非本三生水完ei论文，两个关键点 |

## Not-Used Records

These records are present in `transcripts_distilled/`, but they are not used for method-rule extraction.

| BVID | Label | Status | Relevance | Title |
| --- | --- | --- | --- | --- |
| `BV11L411Y7j3` | support | ok | likely_mismatch | 一个开源方法，对领域所有可投期刊分类后顶刊水刊一眼明了，超乎你想象 |
| `BV11g41127Zn` | core | ok | likely_mismatch | 教你做称职的学术裁缝(纯干货)，明白顶刊和水刊的意义~ |
| `BV12M4y1J737` | support | ok | likely_mismatch | 手把手教你论文投稿返修，期刊越差审稿周期越长是为什么？ |
| `BV12Z421M7pn` | support | ok | likely_mismatch | 研究生毕业论文从入门到放弃，提前开卷 |
| `BV15eZTBxErS` | support | ok | likely_mismatch | 教水论文救不了研究生，反复熏陶才能看清答案 |
| `BV168411F7j6` | support | ok | likely_mismatch | 给正被催毕业大论文的你，硕士论文真的不难 |
| `BV1B14y1D7EC` | support | ok | likely_mismatch | 怎么选择合适的期刊，课题组有额外要求怎么办 |
| `BV1Cx4y187J8` | support | empty_subtitle_url | unavailable | 研究生大论文返修延毕名单出来后，聊聊延毕只有老实人这个规律 |
| `BV1EV4y1P7PQ` | support | ok | likely_mismatch | 学术造假也请你认真对待，站在审稿人的角度教你水论文 |
| `BV1F24y1A7kw` | support | empty_subtitle_url | unavailable | 期刊小论文和毕业大论文的“新”有什么区别 |
| `BV1FKBXBCE84` | core | ok | too_short | 仅想快速毕业，如何高效阅读论文 |
| `BV1FW4y1Q76J` | support | ok | too_short | 性能好才能发论文？高二生都发SCI了，你还在这想七想八，动不了手 |
| `BV1Fuq5BPEye` | support | ok | likely_mismatch | 我必须发顶刊，你咋不当院士，给我点背景，当代研究生该硬硬 |
| `BV1Ht6wBVES1` | core | ok | too_short | 当你开始仅论文论，一年百篇不是梦！ |
| `BV1Kw1xYqE3n` | support | ok | too_short | 80分钟纯干货长视频，小论文粉丝千问千答，研究生错过后悔一辈子（上） |
| `BV1Lk4y197Fj` | support | ok | likely_mismatch | SCI2区论文是怎么水的，论文剖析实例解读，科研Trick揭秘，摸摸老虎屁股 |
| `BV1MSUTYYEfw` | support | ok | too_short | 导师push每天问进度怎么办，感觉科研毫无意义怎么办，没小论文会影响大论文盲审结果吗 |
| `BV1NV4y1a7Hs` | support | ok | too_short | 研二做俩事，定实验，写论文，然后该干嘛干嘛去！ |
| `BV1Ns4y197EM` | support | ok | likely_mismatch | 灌水论文的核心逻辑，营造信息差，事事不较真，海阔天空，人生也如此 |
| `BV1QH4y1C7iQ` | support | ok | likely_mismatch | 深入讲解科研bug，OA期刊和非OA期刊的区别，毕业神刊OA |
| `BV1SY4y197yA` | support | ok | too_short | 和审稿专家聊完，毕业论文初稿还可以抢救一下再提交 |
| `BV1T7j7zXEst` | support | ok | likely_mismatch | 大论文盲审过了，别想太多，毕业答辩过了，更不要想太多，20250523 |
| `BV1VvDQYBErA` | support | empty_subtitle_url | unavailable | 40分钟长视频，关于小论文的粉丝千问千答，错过后悔一辈子 |
| `BV1YN4y1n726` | support | ok | likely_mismatch | 华中农129页小论文分析，学术不端不过是，学术圈的替死鬼 |
| `BV1Zo4y1L7my` | support | ok | too_short | 科研党不听后悔终生，有继承的科研就像一刀999的传奇，开局就送论文 |
| `BV1bn92YWEy1` | support | ok | likely_mismatch | 复旦大学博后，四篇硕论一字不漏的抄，发表成四篇顶刊，一些小启发吧！ |
| `BV1bu4y1f7We` | support | ok | likely_mismatch | 节省科研时间的，学术论文捆绑销售法 |
| `BV1crrLYxE5Z` | support | ok | too_short | 每个研究生都要明白的道理，努力推动科研发展，还是水论文保毕业 |
| `BV1dg411p7QP` | support | ok | likely_mismatch | 换个角度反向提升实验性能超过顶刊 (水论文小trick) |
| `BV1dx421U7B3` | support | ok | too_short | 接好运~毕业大论文盲审一定能过，根据返稿意见反思为什么会被挂 |
| `BV1eM4m1Q7qy` | support | ok | too_short | 论文写完了，如何找到最适合自己的可投稿期刊呢？ |
| `BV1ihw3zUEDy` | support | ok | likely_mismatch | 毕业大论文，盲审通过概率+100%，最后一次应该检查的内容，佛渡有缘研究生，过了这村，没这个店 |
| `BV1j6421Z7yX` | support | ok | likely_mismatch | 毕业大论文，看你会抄不会抄，毕业论文的前期准备 |
| `BV1j9cKzeEUn` | support | ok | too_short | 三探川大王竹卿硕士论文，现在的研究生太难了 |
| `BV1jy4y1K7gu` | support | ok | likely_mismatch | 实操演示有手就行的Ei会议5天录用，也许ei能打破唯论文论 |
| `BV1kK411s72y` | support | ok | likely_mismatch | 导师不可能和学生讲的秘密，高质量的SCI，对导师有何大用，对学生又有什么用？ |
| `BV1mK4y167Hf` | support | ok | too_short | 研一就发两篇SCI，是天道酬勤，还是另有秘密武器，研究生方向抉择 |
| `BV1ne41157Gn` | core | ok | too_short | 水论文如何吹一个好故事，伟大者剽窃，核心思想是复刻 |
| `BV1nhFZz7E8D` | core | ok | likely_mismatch | 二探川大83页举报信，给研究生们的启发！当你仅论文论，论文发表好像很简单！严厉抵制学术不端！ |
| `BV1oP411x7H3` | support | no_subtitle | unavailable | 求你别再自我意淫学术小论文了！开始带你动笔，纯净干货无广告 |
| `BV1ob4y1g7Cb` | support | ok | too_short | 教会徒弟饿死师傅系列，讲清楚大论文如何无中生有 |
| `BV1rN411H7LD` | support | ok | too_short | 从ei会议到oa期刊，有手就行，谁才是幕后推手？ |
| `BV1st4y1w7u5` | support | ok | too_short | 一份论文两用，无缝切换大小论文 |
| `BV1tUy5YkEXe` | core | ok | too_short | 论文A+B的组合能发新论文吗？顶刊更看重什么？没有导师带怎么发顶刊？ |
| `BV1uM411x7ng` | support | ok | likely_mismatch | 指导过的双非本科生水完sci4区论文，两个关键点 |
| `BV1us4y1A75M` | support | empty_subtitle_url | unavailable | 指导过的双非本三生水完ei论文，两个关键点 |
| `BV1v841117EV` | support | ok | likely_mismatch | 最正确的选择论文投稿级别方法，Sci一区，二区还是四区？亦或者ei会议？ |
| `BV1yN4y1h7td` | support | ok | too_short | 大论文必备收藏技能，Latex公式秒变Word公式，附Word激活方法教学 |
| `BV1yT421a7JR` | support | ok | likely_mismatch | 30分钟，详解毕业大论文全网最正确的目录结构 |

## Derived Playbook

The aggregated method distillation lives in `transcript-derived-playbook.md`. It distills the 26 usable rows into seven safe themes:

- target level and venue positioning;
- inheritance chain and baseline selection;
- module delta and mechanism design;
- paper story and section writing;
- experiment and evidence chain;
- search, submission, and revision workflow;
- academic integrity and risk boundaries.

## Validation

- Distilled files generated: 75/75.
- Used/not-used decisions: 26/49.
- Static scan found no direct high-risk advisory phrases from the old first pass.
- Every file includes BVID, source status, relevance status, decision, and audit conclusion.
