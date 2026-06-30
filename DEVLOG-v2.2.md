# Dev Log: v2.2 蒸馏大更新

> 日期: 2026-06-30
> 工作内容: 从 B 站字幕 + 3 个外部 skill 蒸馏并合成到 academic-stitcher-skill
> 仓库: https://github.com/liang1228/academic-stitcher-skill
> Commits: `b1220f0` (主改动) + `5d95666` (日志)

---

## 一、背景与目标

### 问题
academic-stitcher-skill v2.1.10 架构完整（router + manifest.yaml + progressive loading），但 fragment 内容普遍薄弱：
- 8 个 `section/*.md` 平均仅 ~15 行（只有 job + structure + checks 骨架）
- `reviewer-audit.md` 仅 14 行（4 个 lens + 1 条 synthesis rule）
- `nature-polish.md` 仅 20 行（诊断顺序 + 4 条 style rules）
- `full-pipeline.md` 仅 20 行（9 个 stage 名称 + checkpoint contract）
- `transcript-derived-playbook.md` 仅 47 行（从 75 个视频蒸馏出 6 条粗规则）

### 目标
1. 从 524 个 B 站字幕文件中筛选并蒸馏学术写作相关内容
2. 从 3 个外部 skill 仓库提取不冲突的增量方法论
3. 将所有蒸馏结果合成到现有薄弱 fragment，不新增 route

### 方法论
采用 nuwa-skill (github.com/alchaincyf/nuwa-skill) 的蒸馏方法论：
- **三重验证**: 跨视频复现(3+) + 生成力(能指导新场景) + 排他性(非通用废话)
- **置信度标注**: direct(直接陈述) / inferred(推断) / needs-verification(需验证)
- **BVID 来源追溯**: 每条规则标注来源视频 BV 号

---

## 二、Phase 1: 字幕筛选

### 输入
- 目录: `E:\workspace\bilibili_subtitles\`
- 总文件数: 524 个 `.txt` 字幕文件
- UP主: 慧研格真（水导），百万硕博粉丝的研究生导师
- 文件格式: 时间戳字幕（`[MM:SS] 文本`），带元数据头（# 标题, # BV号, # UP主, # 字幕条数）
- 文件大小范围: ~100 到 ~3800 行（约 5 分钟到 90 分钟视频）

### 筛选方法
编写 Python 脚本 `E:\workspace\bilibili_subtitles\filter_academic.py`，用正则表达式按文件名关键词分类：

```python
CATEGORIES = [
    ("学术裁缝", [r"学术裁缝", r"缝论文", r"模块拼接", r"故事线", ...]),
    ("毕业大论文", [r"毕业论文", r"第[一二三四五]章", r"绪论", ...]),
    ("论文阅读", [r"读论文", r"读文献", r"文献.*梳理", ...]),
    ("选刊投稿", [r"SCI", r"投稿", r"选刊", r"盲审", ...]),
    ("章节写作", [r"摘要.*写作", r"引言.*写作", ...]),
    ("实验设计", [r"实验.*设计", r"消融", r"ablation", ...]),
    ("答辩盲审", [r"答辩", r"盲审", ...]),
    ("AI辅助", [r"ChatGPT", r"AI.*润色", ...]),
    ("研究规划", [r"研究.*方向", r"研[究生].*规划", ...]),
]
```

### 筛选结果

| 类别 | 文件数 | 占比 | 典型内容 |
|------|--------|------|---------|
| 学术裁缝 | 63 | 38% | A+B 模块拼接、编故事、继承链、SOTA |
| 毕业大论文 | 37 | 22% | 绪论/基础理论/方法/实验/总结 逐章写作 |
| 研究规划 | 21 | 13% | 选方向、年度规划、开题、科研入门 |
| 选刊投稿 | 14 | 8% | SCI/CCF/EI 分类、选刊、投稿流程 |
| 论文阅读 | 5 | 3% | 高效读论文、文献矩阵 |
| 实验设计 | 4 | 2% | 实验策略、消融、性能展示 |
| 答辩盲审 | 3 | 2% | 答辩技巧、盲审应对 |
| AI 辅助 | 2 | 1% | ChatGPT 润色/翻译 |
| **总计** | **149** | **100%** | |

### 输出
- 筛选后文件: `E:\workspace\bilibili_subtitles\filtered\{类别名}\` 子目录
- 清单文件: `E:\workspace\bilibili_subtitles\filtered\manifest.json`
  - 含每个文件的 BVID、标题、类别、行数

### 未纳入的文件 (~375 个)
- 研究生生活杂谈 (~200): 导师 PUA、退学焦虑、情绪支持
- 学术不端案例评论 (~35): 武大杨某媛、同济 Nature 造假
- AI/ML 技术教程 (~25): Transformer/BERT/Word2Vec 系列
- 就业 advice (~35): 考公、秋招、简历
- 通用人生哲理 (~40): 励志、恋爱、生活
- 杂项 (~50): 钓鱼、摩托车、天气

---

## 三、Phase 2: 多维度蒸馏

### 蒸馏架构
借鉴 nuwa-skill 的 6-agent 并行研究模式，adapt 为 3 个并行蒸馏 agent，每个 agent 负责一个主题维度。

nuwa-skill 原始 6 维度:
1. Writings（著作）→ adapt 为: 方法论提取
2. Conversations（对话）→ 不适用（单 UP主）
3. Expression DNA（表达 DNA）→ adapt 为: 话术映射
4. External Views（外部评价）→ 不适用
5. Decisions（关键决策）→ adapt 为: 实验设计
6. Timeline（时间线）→ 不适用

### Agent A: 写作方法论 + 章节模板
- **Agent ID**: `a60ba1fbcf7182a98`
- **读取范围**: `filtered/学术裁缝/` (63 文件) + `filtered/毕业大论文/` (37 文件)
- **精读文件数**: 35+ 个（优先读取编号系列 001-018 + 逐章写作 329-339）
- **耗时**: ~5 分钟
- **产出**: `E:\workspace\bilibili_subtitles\distill\A-writing-methodology.md` (20 KB)

#### 产出结构
```
A-writing-methodology.md
├── 核心方法论框架 (7 条规则，均通过三重验证)
│   ├── 规则 1: 论文的 A+B+C 结构模型
│   ├── 规则 2: 读论文的核心是"逐段逐部分"
│   ├── 规则 3: 只看一区和四区论文
│   ├── 规则 4: 先找模块拼上去，再编故事
│   ├── 规则 5: 编故事的核心是"发现问题→解决问题"
│   ├── 规则 6: 方法章节按数据流从输入到输出介绍
│   └── 规则 7: 写作顺序是 方法→实验→相关工作→引言→摘要→总结
├── 论文阅读策略
│   ├── 选择论文的规则 (期刊级别→阅读策略)
│   └── 阅读论文的方法 (逐段/标点划分/转折词)
├── 章节写作模板
│   ├── 标题 (命名模式/好坏对比)
│   ├── 摘要 (4 句框架/摘要 vs 结论)
│   ├── 引言 (漏斗结构/发现问题→解决问题)
│   ├── 相关工作 (按论证角色组织/逻辑衔接)
│   ├── 方法 (数据流/先总后分/模块描述)
│   ├── 实验 (4 部分: 配置→对比→消融→可视化)
│   ├── 讨论 (融入实验分析)
│   └── 结论 (做了什么+怎么做的+效果如何)
├── 毕业大论文章节结构
│   ├── 第一章 绪论 (背景/意义/国内外现状/技术路线/创新点)
│   ├── 第二章 基础理论
│   ├── 第三章 方法 1
│   ├── 第四章 方法 2
│   └── 第五章 总结与展望
├── Story Spine 构建方法
├── 决策启发式
└── 示例与反模式
```

#### 关键 BVID 来源
| BVID | 视频标题 | 提取的核心规则 |
|------|---------|--------------|
| BV1UZZUY6E6X | 学术裁缝要看哪类论文 001 | 只看一区和四区 |
| BV1rPGdz3E2V | 相关工作 005 | 按论证角色组织相关工作 |
| BV1W5EAzLErh | 方法章节怎么阅读 007 | 逐段逐部分阅读 |
| BV12WJ6zoEa6 | 如何读论文 009 | 阅读→写作转化 |
| BV1rDMHzTEEd | 顶会标准的学术裁缝 011 | A+B+C 结构分析 |
| BV1npKfzPEuC | 缝论文从未如此简单 012 | 先找模块再编故事 |
| BV1ut34zuEfS | 方法部分如何写作 013 | 数据流描述模式 |
| BV1U88gzqENC | 实验就是客观陈述 014 | 实验写作方法 |
| BV1mxbezeEhV | 相关工作 015 | 相关工作模仿法 |
| BV1HeazzLEV2 | 引言写作 016 | 漏斗结构 |
| BV1NoHvzmETH | 摘要和总结写作 017 | 摘要 vs 结论区别 |
| BV1JCJ9zHEd5 | 参考文献管理 018 | 引用管理 |
| BV1dzNWewExA | 核心不是缝模块而是编故事 | 故事线构建 |
| BV17s421N7am | CVPR 带读 | 顶会写作分析 |
| BV1fW4y1W7dS | SCI 灌水文每个部分怎么写 | 全章节模板 |
| BV1QhpseMEwr | 第一章绪论怎么写 | 绪论模板 |
| BV1RT4reYEEC | 第二章基础理论 | 基础理论模板 |
| BV1Lgt7eMEZd | 第三章方法1 | 方法章节模板 |
| BV1cpx7eGEyY | 第四章方法2 | 方法章节模板 |
| BV1bt4we2EJf | 第五章总结与展望 | 结论模板 |
| BV1yT421a7JR | 目录结构 | 论文结构规范 |

### Agent B: 话术映射 + 实验设计
- **Agent ID**: `af51a294d4fd7c3e1`
- **读取范围**: `filtered/实验设计/` (4) + `filtered/选刊投稿/` (14) + 学术裁缝关键文件
- **精读文件数**: 28 个
- **耗时**: ~3 分钟
- **产出**: `E:\workspace\bilibili_subtitles\distill\B-rhetoric-experiment.md` (312 行, 21 KB)

#### 产出结构
```
B-rhetoric-experiment.md
├── Grey Vocabulary Map (12 组灰色话术→合规表达映射)
│   ├── 缝论文 → 模块化组合创新
│   ├── 水论文 → 高效产出合规论文
│   ├── 造航母 → 过大过难的课题
│   ├── 数据美化 → 调整参数/条件
│   ├── 编故事 → 构建叙事框架
│   ├── 营造信息差 → 选择性呈现
│   ├── 复刻别人想法 → 借鉴核心思路
│   ├── 堆叠 → 组合多篇模块
│   ├── 炼丹 → 系统性调参
│   ├── SOTA → 最佳性能
│   ├── 开源=造假(反讽) → 警惕未开源结果
│   └── 仿造同行写 → 仿照已发表风格
├── Rhetoric Patterns
│   ├── Claim Calibration (6 条声明校准规则)
│   ├── Limitation Framing (2 条局限性表述规则)
│   ├── Negative Result Presentation (5 条负面结果呈现技巧)
│   └── Chinese-to-English Translation (2 条翻译规则)
├── Experiment Design Rules
│   ├── Baseline Selection (6 条基线选择规则)
│   ├── Ablation Strategy (3 条消融策略)
│   ├── Dataset Principles (5 条数据集原则)
│   ├── Performance Presentation (4 条性能展示技巧)
│   └── Weak Result Handling (3 条弱结果处理)
├── Reviewer Response Patterns
│   ├── Common Attack Vectors (7 种审稿攻击向量)
│   ├── Response Templates (3 种回复模板)
│   └── Rebuttal Strategy (9 条返修策略)
├── Journal Selection Guide
│   ├── Classification System (5 条分类规则)
│   ├── Matching Strategy (5 条匹配策略)
│   └── Submission Workflow (6 步投稿流程)
├── Decision Heuristics (10 条)
└── Examples (4 个详细示例)
```

#### 核心发现: 信息不对称原则
跨 5+ 个视频反复出现的最强规则: **"你知道的，审稿人不一定知道"** — 这一原则支撑了几乎所有策略（基线选择、性能展示、消融实验、叙述策略）。

#### 关键 BVID 来源
| BVID | 视频标题 | 提取的核心规则 |
|------|---------|--------------|
| BV1EV4y1P7PQ | 站在审稿人角度教你水论文 | 审稿人视角写作 |
| BV1ne41157Gn | 如何吹一个好故事 | 信息不对称原则 |
| BV1fV4y1B72F | 调参术轻松解决消融难题 | 消融实验策略 |
| BV1dg411p7QP | 反向提升实验性能 | 性能展示技巧 |
| BV14c411A75s | 结果差也能发论文 | 弱结果处理 |
| BV19jCrYsEoE | 公共数据集原则 | 数据集选择 |
| BV1Ns4y197EM | 灌水论文的核心逻辑 | 信息差叙述策略 |
| BV1cH4y1j742 | 什么才是真正的学术创新 | 创新点包装 |
| BV17s4y127VF | 摘要和结论怎么写 | 摘要写作 |
| BV1JD4y1V7ar | 摘要和总结不被拒稿的写法 | 摘要 vs 总结 |
| BV1mP411Z7tn | 双盲审策略 | 盲审应对 |
| BV12M4y1J737 | 投稿返修 | 投稿流程 |

### Agent C: 投稿生涯 + 答辩盲审
- **Agent ID**: `abe1df17fba8beff9`
- **读取范围**: `filtered/答辩盲审/` (3) + `filtered/AI辅助/` (2) + `filtered/研究规划/` (21) + `filtered/选刊投稿/` (8)
- **精读文件数**: 22 个
- **耗时**: ~5 分钟
- **产出**: `E:\workspace\bilibili_subtitles\distill\C-submission-defense.md` (325 行, 27 KB)

#### 产出结构
```
C-submission-defense.md
├── 一、毕业答辩指南
│   ├── 1.1 答辩心态与总原则 (7 条规则)
│   ├── 1.2 PPT 制作与结构 (6 条规则)
│   ├── 1.3 答辩 Q&A 策略 (6 条规则)
│   ├── 1.4 答辩前盲审意见处理 (5 条规则)
│   └── 1.5 答辩后流程 (3 条规则)
├── 二、盲审导航
│   ├── 比例淘汰制 (~30% 不通过)
│   ├── 格式/摘要作为首要筛选因素
│   └── 盲审准备策略
├── 三、AI 辅助工具
│   ├── ChatGPT 工作流 (英文 prompt, 1000 字限制, 公式处理)
│   └── 局限性 (无推理能力, 伪造引用)
├── 四、研究生规划
│   ├── 年度路线图: 研1=基础+方向, 研2=实验+论文, 研3=大论文+就业
│   ├── 方向选择策略
│   └── 时间管理
├── 五、期刊分类
│   ├── SCI Q1-Q4 / CCF A-C / EI 体系
│   ├── 水刊 vs 顶刊对比
│   └── 会议 vs 期刊差异
├── 六、投稿流程
│   ├── 3 步选刊法
│   ├── 状态流转
│   ├── 返修回复模板
│   └── 拒稿应对
├── 七、决策启发式
├── 八、具体示例 (4 个)
├── 九、矛盾与张力 (4 组)
└── 十、金句 (8 条，跨视频验证)
```

#### 关键 BVID 来源
| BVID | 视频标题 | 提取的核心规则 |
|------|---------|--------------|
| BV1SPLU6ZEk4 | 毕业答辩不要辩 | "只答不辩"原则 |
| BV1eD421A7Bh | 40 分钟毕业答辩 | 答辩全流程 |
| BV11X4y127rB | 答辩舔狗 | "只答不辩"策略细节 |
| BV1wX4y1d7v7 | ChatGPT 真的牛 | AI 辅助写作 |
| BV17k4y1t7sT | ChatGPT 注册和润色 | AI 工具使用 |
| BV1JhbzziERP | 研一研二研三规划 | 年度规划 |
| BV15V411A7AU | 研一挑方向研二换方向 | 方向选择 |
| BV1NV4y1a7Hs | 研二做俩事 | 研二策略 |
| BV1pP411e7aD | 研一搞清楚两件事 | 研一重点 |
| BV1Wr421K7Ho | 研0研一研二规划 | 全周期规划 |
| BV1jvxEzaECD | 手把手选期刊投稿 | 投稿流程 |
| BV1yM41157yT | 水刊顶刊分类 | 期刊分类 |
| BV1ta4y1T7EJ | 论文拒了可再投 | 拒稿应对 |
| BV12M4y1J737 | 投稿返修 | 返修策略 |

---

## 四、Phase 3: 合成到 Skill Fragment

### 执行方式
用 3 个并行 agent 将蒸馏结果写入 `E:\workspace\academic-stitcher-skill\` 的现有 fragment 文件。

### 3a. Section Fragments (8 个文件)

所有 8 个 section fragment 从 ~15 行扩充到 64-78 行，新增内容统一结构:
1. 原有 Job / Structure / Checks 保留
2. 新增 "Video-Derived" 模板（带 BVID 来源）
3. 新增 "Different Evidence State Strategies"（强/中/弱证据状态下的写作策略）
4. 新增 "Common Mistakes"（常见错误）
5. 新增 "Chinese Academic Context"（中文学术写作特殊注意事项）

| 文件 | 原行数 | 新行数 | 新增内容 | Agent |
|------|--------|--------|---------|-------|
| `section/title.md` | 15 | 64 | 4 种命名模式、好坏标题对比、模块命名策略(DCD→ECD)、范围信号 | Agent A |
| `section/abstract.md` | 15 | 66 | 4 句摘要框架表、摘要 vs 结论关键区别表、6 种常见错误 | Agent A |
| `section/introduction.md` | 15 | 77 | 4 部分漏斗+句式起始表、"发现问题→解决问题"框架、One-Sentence Argument | Agent A |
| `section/related-work.md` | 15 | 78 | A/B/C 模块谱系映射表、每组的具体模板、段落→方法连接策略 | Agent A |
| `section/method.md` | 15 | 70 | 章节布局表、概述模板、输入→处理→输出公式模式、借用 vs 新模块表 | Agent A |
| `section/experiments.md` | 15 | 76 | 4 部分实验结构、配置表、基线选择规则表、消融变体表、5 种弱结果策略 | Agent A |
| `section/discussion.md` | 15 | 71 | 解释框架表、3 种先驱工作连接策略、局限性表述规则(好 vs 坏) | Agent A |
| `section/conclusion.md` | 15 | 74 | 摘要 vs 结论表、结论模板、贡献复述表(承诺→证据) | Agent A |

#### 各文件详细结构

**title.md (64 行)**:
```
原有: Job, Checks
新增: Naming Patterns (Video-Derived)
  ├── Common Title Structures (4 种模式)
  ├── What Makes a Good vs Bad Title
  ├── Module Naming Strategy (DCD→ECD)
  ├── How to Signal Scope
  └── Common Mistakes (4 种)
```

**abstract.md (66 行)**:
```
原有: Job, Structure, Checks
新增: 4-Sentence Abstract Framework (Video-Derived)
  ├── Abstract vs Conclusion: Critical Difference
  ├── Common Abstract Mistakes (6 种)
  ├── Different Evidence State Strategies (强/中/弱)
  └── Chinese Academic Context
```

**introduction.md (77 行)**:
```
原有: Job, Default Funnel, Variants
新增: Funnel Structure with Sentence Starters (Video-Derived)
  ├── Part 1: Field Description (1-2 段, 无引用)
  ├── Part 2: Problem Introduction (带引用)
  ├── Part 3: Proposed Solution
  ├── Part 4: Result Preview
  ├── Building the "Field Pressure→Gap→Contribution" Chain
  ├── The "发现问题→解决问题" Framing
  ├── Different Evidence State Strategies
  ├── Common Mistakes (4 种)
  ├── One-Sentence Argument (from nature-skills)
  └── Chinese Academic Context
```

**related-work.md (78 行)**:
```
原有: Job, Structure, Checks
新增: Organizing by Argument Role (Video-Derived)
  ├── The A/B/C Module Lineage Mapping
  ├── Concrete Template (每组的具体写法)
  ├── Connecting Each Paragraph to Your Method
  ├── Different Evidence State Strategies
  ├── Common Mistakes (6 种)
  └── Chinese Academic Context
```

**method.md (70 行)**:
```
原有: Job, Structure, Checks
新增: Data-Flow Description Pattern (Video-Derived)
  ├── Section Layout
  ├── Overview Template
  ├── Module Description (Input→Process→Output)
  ├── Borrowed vs Novel Modules
  ├── Formula Rules
  ├── Evidence State Strategies
  ├── Common Mistakes (4 种)
  └── Chinese Academic Context
```

**experiments.md (76 行)**:
```
原有: Job, Evidence Ladder, Checks
新增: 4-Part Experiment Structure (Video-Derived)
  ├── Part 1: Configuration (数据集/指标/参数)
  ├── Part 2: Comparison Experiments (基线选择/结果分析)
  ├── Part 3: Ablation Studies (消融变体/模块合并规则)
  ├── Part 4: Qualitative / Visualization
  ├── Weak Result Strategies (5 种)
  ├── Common Mistakes (5 种)
  └── Chinese Academic Context
```

**discussion.md (71 行)**:
```
原有: Job, Structure, Checks
新增: Interpreting Results Without Overclaiming (Video-Derived)
  ├── Relating to Prior Work (3 种策略)
  ├── Limitation Framing Rules (好 vs 坏示例)
  ├── Different Evidence State Strategies
  ├── Common Mistakes (4 种)
  └── Chinese Academic Context
```

**conclusion.md (74 行)**:
```
原有: Job, Structure, Checks
新增: Abstract vs Conclusion: The Core Distinction (Video-Derived)
  ├── Conclusion Template
  ├── How to State Contributions Concisely (贡献复述表)
  ├── Different Evidence State Strategies
  ├── Common Mistakes (5 种)
  └── Chinese Academic Context
```

### 3b. Route Fragments (3 个文件)

**reviewer-audit.md** (14→82 行, Agent B + 外部 skill 合入):
```
原有: Independent Lenses (4 lens), Synthesis Rule
新增 (from Bilibili):
  ├── Common Reviewer Attack Vectors (7 种攻击向量+应对)
  ├── Reviewer Psychology Insights (5 条审稿人心理观察)
  ├── Rebuttal Strategy Patterns (6 条返修原则)
  ├── Integrity Check Specifics (审稿人实际检查什么)
  └── Audit Checklist (自检清单)
新增 (from academic-research-skills):
  └── Seven Reviewer Personas (7 种审稿人角色表)
      ├── Devil's Advocate / Domain Expert / Methodological
      ├── Editorial / Perspective / Field Analyst / EIC
```

**nature-polish.md** (20→73 行, Agent B):
```
原有: Diagnosis Order, Style Rules
新增:
  ├── Chinese-to-English Translation Rules (5 条中英转写规则)
  ├── Claim Verb Calibration (4 级证据强度→动词选择表)
  ├── Common Overclaim Patterns and Fixes (5 种过度声称+修正)
  ├── Paragraph Flow Rules (主题-证据-边界 + 叙事弧)
  └── Revision Checklist (修改清单)
注: Failure-Mode Diagnosis 和 Revision by Targeted Edit
    已存在于原文件中（来自之前对 nature-skills 的合入），无需重复添加
```

**full-pipeline.md** (20→66 行, Agent B):
```
原有: Stages (9 stage 名称), Checkpoint Contract
新增:
  ├── Stage Details (每个 stage 的具体动作)
  │   ├── Stage 1: Intake — 约束捕获、缺失输入检查
  │   ├── Stage 2: Literature/Paper Matrix — 文献矩阵构建
  │   ├── Stage 3: Story Architecture — 故事线构建
  │   ├── Stage 4: Evidence Gate — 证据完整性检查
  │   ├── Stage 5: Section Plan — 章节规划
  │   ├── Stage 6: Draft or Polish — 起草/润色
  │   ├── Stage 7: Reviewer Audit — 审稿人审计
  │   ├── Stage 8: Revision Roadmap — 修改路线图
  │   └── Stage 9: Final Quality Gate — 最终质量门
  └── Pipeline Heuristics (4 条流程启发式)
```

### 3c. Other Fragments (3 个文件)

**algorithmic.md** (20→71 行, Agent B):
```
原有: Reader Question, Argument Chain, Required Evidence
新增 (from Bilibili):
  ├── Baseline Selection Rules (6 条: 领域匹配/近年/可复现/可信度 bracket/策略选择/参数对齐)
  ├── Ablation Strategy (5 条: 单调性/失败→合并/分配置调参/粒度/参数敏感性)
  ├── Dataset Principles (4 条: 公开vs私有/领域惯例/基线对齐/数据描述)
  ├── Performance Presentation (5 条: 指标计算/预处理敏感性/硬件差异/选择性报告/格式)
  └── Weak Result Handling (5 条: 迭代组合搜索/重新框架/策略性省略/复现 caveat)
```

**zh-cn.md** (11→80 行, Agent C):
```
原有: Rules (5 条中文写作基本规则)
新增 (from Bilibili):
  ├── Grey Vocabulary Conversion (12 组灰色话术→合规表达映射)
  ├── Chinese Academic Writing Patterns (5 个章节的中文写作范式)
  │   ├── Abstract Pattern (摘要范式)
  │   ├── Introduction Pattern (引言范式)
  │   ├── Related Work Pattern (相关工作范式)
  │   ├── Method Writing Pattern (方法写作范式)
  │   └── Conclusion Pattern (结论范式)
  └── Common Expressions and Their Compliant Versions (6 组风险→合规映射)
```

**transcript-derived-playbook.md** (47→191 行, 重写):
```
原有: 覆盖范围表 + 6 条粗规则 + 排除中间产物
重写为:
  ├── 覆盖范围 (更新: 3 个蒸馏文档 + 50+ 视频)
  ├── 一、核心方法论规则 (7 条，三层验证)
  │   ├── 规则 1: A+B+C 结构模型 (BV1npKfzPEuC 等 5+ 视频)
  │   ├── 规则 2: 逐段逐部分阅读 (BV1rPGdz3E2V 等 4 视频)
  │   ├── 规则 3: 只看一区四区 (BV1UZZUY6E6X 等 2 视频)
  │   ├── 规则 4: 先找模块再编故事 (BV1npKfzPEuC 等 4 视频)
  │   ├── 规则 5: 发现问题→解决问题 (BV1qv4y1n7dx 等 4 视频)
  │   ├── 规则 6: 数据流描述 (BV1ut34zuEfS 等 4 视频)
  │   └── 规则 7: 写作顺序 (BV1fW4y1W7dS 等 3 视频)
  ├── 二、修辞与表达规则
  │   ├── 2.1 灰色话术映射 (Top 8)
  │   ├── 2.2 声明校准规则
  │   └── 2.3 信息不对称原则
  ├── 三、实验设计规则
  │   ├── 3.1 基线选择
  │   ├── 3.2 消融策略
  │   ├── 3.3 数据集原则
  │   └── 3.4 弱结果处理
  ├── 四、投稿与答辩规则
  │   ├── 4.1 答辩"只答不辩"原则
  │   ├── 4.2 盲审准备
  │   └── 4.3 期刊分类与选择
  ├── 五、决策启发式 (Top 10)
  └── 附录: 排除中间产物
```

---

## 五、Phase 3b: 外部 Skill 合入

### 探索阶段
并行启动 3 个 Explore agent 读取外部仓库：

| Agent ID | 仓库 | 读取文件数 | 耗时 |
|----------|------|----------|------|
| `a2001599def86ce4c` | Yuan1z0825/nature-skills | 15+ 文件 | ~3.5 分钟 |
| `afa8e62fa4e6624a8` | wanshuiyin/Auto-claude-code-research-in-sleep | 10+ 文件 | ~1.7 分钟 |
| `a7de89c9c963c43b7` | Imbad0202/academic-research-skills-codex | 10+ 文件 | ~1.2 分钟 |

### 仓库分析摘要

#### nature-skills (Yuan1z0825)
- **定位**: 14 个独立 skill 的 monorepo，覆盖 Nature 期刊级别的学术研究全流程
- **核心架构**: router + manifest + static fragments + `_shared/` 共享层
- **独特价值**: Terminology Ledger、Reader Workflow、AI Traffic-Light、Failure-Mode Diagnosis、One-Sentence Argument、Journal-Specific Formatting

#### Auto-claude-code-research-in-sleep / ARIS (wanshuiyin)
- **定位**: ML 研究工作流自动化系统，79+ skills
- **核心架构**: Workflow-Skill 分离、Research Wiki 持久化知识库、跨模型对抗审稿
- **独特价值**: 5 层审计链、Dual-Axis Control、Assurance Contract、Integration Contract、Cross-Model Adversarial Review

#### academic-research-skills-codex / ARS (Imbad0202)
- **定位**: Codex-native 学术研究助手套件，7 个 workflow
- **核心架构**: 多 agent 编排（13+ agent 深度研究）、Material Passport 交接
- **独特价值**: 7 种审稿人角色、Citation 存在性验证、Socratic Research Question Refinement、Style Calibration Protocol、Mode Spectrum

### 冲突分析与合入决策

#### ✅ 合入 (无冲突, 10 项)

| # | 增量内容 | 来源仓库 | 写入文件 | 理由 |
|---|---------|---------|---------|------|
| 1 | Terminology Ledger (术语锁定表) | nature-skills | `static/core/stance.md` | 扩展已有 section，与现有 "Terminology Ledger" 一致 |
| 2 | Reader Cognitive Model (读者 5 问) | nature-skills | `static/core/workflow.md` | 新增 section，与现有 workflow 互补 |
| 3 | AI Traffic-Light 伦理分级 | nature-skills | `static/core/stance.md` | 新增 section，强化现有 Academic Integrity |
| 4 | One-Sentence Argument 模板 | nature-skills | `section/introduction.md` | 新增 subsection，与漏斗结构互补 |
| 5 | Paragraph-to-Job Mapping | nature-skills | `quality-gates.md` | 新增 subsection in Flow Gate |
| 6 | 7 种审稿人角色 | ARS | `reviewer-audit.md` | 新增 table，补充现有 4 lens |
| 7 | Citation Verification Gate | ARS | `quality-gates.md` | 新增 gate，补充现有 Gate 体系 |
| 8 | Dual-Axis Control | ARIS | `static/core/workflow.md` | 新增 section，与现有 workflow 互补 |
| 9 | 5 层审计链概念 | ARIS | `ctx2skill-evaluation.md` | 概念借鉴，不改变现有结构 |
| 10 | Failure-Mode Diagnosis | nature-skills | `nature-polish.md` | ⏭️ 已存在相同内容，跳过 |

#### ⚠️ 适配后合入 (有潜在冲突但可调和)

| 内容 | 来源 | 冲突点 | 适配方案 |
|------|------|--------|---------|
| Confirmation Gate (起草前确认) | nature-skills | 与自主流程冲突 | 改为"建议确认点"而非强制 |
| Adversarial Review (跨模型对抗审稿) | ARIS | 需要多模型 | 标注为"可选增强" |
| Revision by Targeted Edit | nature-skills | 与全量重写冲突 | 加入 quality gate |
| Material Passport | ARS | 架构差异大 | 仅借鉴 schema 概念 |

#### ❌ 不合入 (与 skill 设计哲学冲突)

| 内容 | 来源 | 原因 |
|------|------|------|
| Research Wiki (持久化知识图谱) | ARIS | 需要持久化基础设施，超出 skill 范围 |
| No Autonomous Research | ARS | 与 stitch-plan 路由冲突（ARS 禁止 AI 提出研究假设） |
| No Paper2X Auto-Generation | ARS | 范围限制，不在当前 skill 职责内 |
| Material Passport 完整实现 | ARS | 架构差异过大（多 agent 编排 vs 单 skill） |
| Mandatory Confirmation Gate | nature-skills | 与用户期望的自主流程冲突 |
| Institutional Format Binding | ARS | 故意不做格式绑定 |
| Cross-Paper Memory | ARIS | ARS 保持无状态设计 |

### 合入执行
- **Agent ID**: `a9d314a6d7d36fd46`
- **读取**: 6 个目标文件
- **编辑**: 4 个文件成功，2 个因已有相同内容自动跳过
- **耗时**: ~2 分钟

---

## 六、最终验证

### Manifest 路径验证
```python
# 验证 manifest.yaml 中所有 25 个路径指向的文件是否存在
OK: 25 paths verified
All manifest paths exist!
```

### 文件行数统计

| 分类 | 文件 | 原行数 | 新行数 | 变化 |
|------|------|--------|--------|------|
| **Core** | stance.md | 37 | 51 | +14 |
| | workflow.md | 34 | 69 | +35 |
| | quality-gates.md | 44 | 57 | +13 |
| | output-format.md | 105 | 105 | 0 (未改) |
| **Section** | title.md | 15 | 64 | +49 |
| | abstract.md | 15 | 66 | +51 |
| | introduction.md | 15 | 77 | +62 |
| | related-work.md | 15 | 78 | +63 |
| | method.md | 15 | 70 | +55 |
| | experiments.md | 15 | 76 | +61 |
| | discussion.md | 15 | 71 | +56 |
| | conclusion.md | 15 | 74 | +59 |
| **Route** | reviewer-audit.md | 14 | 82 | +68 |
| | nature-polish.md | 20 | 73 | +53 |
| | full-pipeline.md | 20 | 66 | +46 |
| | stitch-plan.md | 26 | 26 | 0 (未改) |
| | section-draft.md | 17 | 17 | 0 (未改) |
| | ctx2skill-audit.md | 60 | 60 | 0 (未改) |
| **Paper Type** | algorithmic.md | 20 | 71 | +51 |
| | research.md | 17 | 17 | 0 (未改) |
| | methods.md | 18 | 18 | 0 (未改) |
| | review.md | 18 | 18 | 0 (未改) |
| | proposal-thesis.md | 19 | 19 | 0 (未改) |
| **Language** | zh-cn.md | 11 | 80 | +69 |
| | en.md | 11 | 11 | 0 (未改) |
| **References** | transcript-derived-playbook.md | 47 | 191 | +144 |
| | playbook.md | 217 | 217 | 0 (未改) |
| | writing-suite.md | 197 | 197 | 0 (未改) |
| | ctx2skill-evaluation.md | 164 | 164 | 0 (未改) |

### Git 统计
```
19 files changed, 1125 insertions(+), 68 deletions(-)
Commits: b1220f0 (主改动) + 5d95666 (日志)
```

### BVID 来源统计
- `transcript-derived-playbook.md` 中引用: 36 个独立 BVID
- `static/` 所有 fragment 中引用: 35 个独立 BVID
- 总计覆盖: ~60+ 个独立视频来源（部分 BVID 跨文件复用）

---

## 七、中间产物

### 蒸馏文档 (保留在 `E:\workspace\bilibili_subtitles\distill\`)

| 文件 | 大小 | 行数 | 内容 |
|------|------|------|------|
| `A-writing-methodology.md` | 20 KB | ~450 | 写作方法论 + 章节模板 |
| `B-rhetoric-experiment.md` | 21 KB | 312 | 话术映射 + 实验设计 |
| `C-submission-defense.md` | 27 KB | 325 | 投稿生涯 + 答辩盲审 |

### 筛选产物 (保留在 `E:\workspace\bilibili_subtitles\filtered\`)

| 文件/目录 | 说明 |
|----------|------|
| `manifest.json` | 149 个文件的元数据清单 |
| `学术裁缝/` | 63 个字幕文件副本 |
| `毕业大论文/` | 37 个字幕文件副本 |
| `研究规划/` | 21 个字幕文件副本 |
| `选刊投稿/` | 14 个字幕文件副本 |
| `论文阅读/` | 5 个字幕文件副本 |
| `实验设计/` | 4 个字幕文件副本 |
| `答辩盲审/` | 3 个字幕文件副本 |
| `AI辅助/` | 2 个字幕文件副本 |

### 筛选脚本

| 文件 | 说明 |
|------|------|
| `E:\workspace\bilibili_subtitles\filter_academic.py` | Python 筛选脚本 |

### 打包产物

| 文件 | 大小 | 说明 |
|------|------|------|
| `E:\workspace\academic-stitcher-skill-v2.2.tar.gz` | 64 KB | 完整仓库打包（不含 .git）|

---

## 八、Agent 执行记录

| Agent | 任务 | ID | 耗时 | 读取文件数 | 产出 |
|-------|------|-----|------|----------|------|
| A | 写作方法论蒸馏 | `a60ba1fbcf7182a98` | ~5 min | 35+ | A-writing-methodology.md |
| B | 话术+实验蒸馏 | `af51a294d4fd7c3e1` | ~3 min | 28 | B-rhetoric-experiment.md |
| C | 投稿+答辩蒸馏 | `abe1df17fba8beff9` | ~5 min | 22 | C-submission-defense.md |
| Section | 扩充 8 个 section fragment | `af883a8b1d5c61232` | ~8 min | 85+ | 8 个 section/*.md |
| Route | 扩充 3 个 route fragment | `ab3f29758d7b704aa` | ~2 min | 15+ | reviewer-audit, nature-polish, full-pipeline |
| Other | 扩充其他 fragment | `a168ca365a8271322` | ~2 min | 20+ | algorithmic, zh-cn, transcript-derived-playbook |
| Explore | nature-skills 探索 | `a2001599def86ce4c` | ~3.5 min | 15+ | 仓库分析报告 |
| Explore | ARIS 探索 | `afa8e62fa4e6624a8` | ~1.7 min | 10+ | 仓库分析报告 |
| Explore | ARS 探索 | `a7de89c9c963c43b7` | ~1.2 min | 10+ | 仓库分析报告 |
| Merge | 外部 skill 合入 | `a9d314a6d7d36fd46` | ~2 min | 6 | 4 个文件编辑 |
| **总计** | | **10 agents** | **~33 min** | **~230+** | **19 files changed** |

---

## 九、待后续改进

### 高优先级
- [ ] 补充 `paper_type/*.md` — research(17行), methods(18行), review(18行), proposal-thesis(19行) 仍较薄
- [ ] 补充 `stitch-plan.md` route fragment (26行) — 核心路由但内容不足
- [ ] 跑 Ctx2Skill 自评估验证 — 确认蒸馏后的行为一致性

### 中优先级
- [ ] 新增 `section-draft.md` route 的段落级模板
- [ ] 补充 `language/en.md` (11行) — 英文写作指导
- [ ] 添加完整工作示例 (`examples/`) — 一个 route 的完整输入→输出
- [ ] 新增 rebuttal route fragment — 返修/申诉场景

### 低优先级
- [ ] 新增 figure/table 指导 fragment
- [ ] 新增 citation management 指导
- [ ] 将 `distill/` 中间产物的精华合并到 `references/` 或删除
- [ ] 更新 manifest.yaml version 到 2.2.0
