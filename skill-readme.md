# opc-starter-kit — AI 创业纪律技能

> 基于 Anthropic《创始人行动手册》(The Founder's Playbook, 2026.05)
> 版本：v2.0

---

## 这是什么？

**opc-starter-kit** 是一个 AI 创业纪律检查站。它不教你新知识——它解决的是：**AI 让"跳进建造"太容易了，容易到你会跳过验证、跳过反方论证、跳过退出标准——然后在前方更贵的节点撞上这些债。**

核心机制：
- **红队关卡**：在你最自信时扮演反对者，找漏洞
- **绿队关卡**：退出标准，证据够了才放行
- **四个阶段**：想法 → MVP → 发布 → 规模化，每个阶段都有清晰的进展追踪

---

## 安装

在**你的项目目录**下执行：

```
1. 将 opc-starter-kit/ 文件夹复制到项目的 .comate/skills/ 下

   目标路径：your-project/.comate/skills/opc-starter-kit/

2. 确认文件结构：
   .comate/skills/opc-starter-kit/
   ├── skill.md              # 核心行为定义
   ├── templates/            # 模板文件
   │   ├── stage-map-template.md
   │   ├── progress-summary-template.md
   │   ├── stage-completion-report-template.md
   │   ├── dashboard-template.md
   │   ├── one-pager-template.md
   │   └── moat-scorecard-template.md
   └── README.md             # 本文件
```

**如果你在全局安装（所有项目可用）**：

将 `opc-starter-kit/` 放到 Comate 的全局 skills 目录下即可。

---

## 启动

在对话框输入：

```
opc start  (或 opc 启动)
我的项目：[一句话描述你的项目]
```

opc-starter-kit 会自动判断你的阶段，开始第一个任务。

---

## 常用命令

| 英文 (推荐) | 中文 (别名) | 行为 |
|------|------|------|
| `opc` | `opc` | 展示仪表盘——你在哪、产出多少、下一步 |
| `opc help` | `opc 帮助` | 展示所有命令 |
| `opc start` | `opc 启动` | 初始化新项目 |
| `opc idea` | `opc 我有个想法` | 从想法阶段第一步开始 |
| `opc continue` | `opc 继续` | 继续当前任务 |
| `opc scope-check` | `opc 这个功能该不该加` | 触发范围蔓延压力测试 |
| `opc pmf` | `opc 我是不是 PMF 了` | 触发 PMF 判定流程 |
| `opc bottleneck` | `opc 我忙不过来了` | 触发创始人瓶颈审计 |
| `opc skip` | `opc 跳过当前环节` | 记录跳过，告知后果，继续 |
| `opc retrospective` | `opc 事后诊断` | 已造了产品？倒序检查跳过了什么 |
| `opc one-pager` | `opc 一页纸` | 生成可分享的当前状态摘要 |
| `opc blind-review` | `opc 生成盲审报告` | 生成可发社区的匿名评审包 |
| `opc moat-test` | `opc 护城河压力测试` | 模拟竞品入侵推演 |

---

## 它会做什么

- 每个阶段拆成 3-4 个微步骤，每步都有文件产出
- 自动保存进度（`.opc-state.json`）和产物（`docs/`）
- 主控窗口调度 + 子窗口执行深度任务，防止上下文爆炸
- 红队关卡用多角色多框架交叉质疑
- 阶段通关时生成完整的报告——进入时带着什么、离开时带着什么
- 维护决策日志，追溯每个关键选择

## 它不会做什么

- 替代人类客户访谈
- 替代安全审计或法律合规审查
- 替代真实的市场数据采集
- 假装社区或人脉

---

## 跨窗口恢复

新开窗口后，只需输入：

```
opc
```

它会自动读取状态，知道你在哪、该做什么。如果状态文件丢失，它会扫描 `docs/` 产物推断阶段。

---

## 文件结构

opc-starter-kit 在你的项目中创建：

```
your-project/
├── .opc-state.json              # 项目状态
└── docs/                        # 全部产物
    ├── stage-map.md             # 阶段地图（自动更新）
    ├── decisions.md             # 决策日志
    ├── problem-statement.md     # 想法阶段产物
    ├── competitive-map.md
    ├── interview-guide.md
    ├── problem-hypothesis.md
    ├── stage-1-completion-report.md
    ├── architecture-context.md  # MVP 阶段产物
    ├── scope-doc.md
    ├── metrics-framework.md
    ├── pmf-assessment.md
    ├── stage-2-completion-report.md
    ├── tech-debt-audit.md       # 发布阶段产物
    ├── bottleneck-audit.md
    ├── pm-process.md
    ├── stage-3-completion-report.md
    ├── domain-knowledge.md      # 规模化阶段产物
    ├── workflow-audit.md
    ├── moat-narrative.md
    ├── moat-scorecard.md
    ├── stage-4-completion-report.md
    ├── one-pager.md             # 按需生成
    └── peer-review-package.md   # 按需生成
```