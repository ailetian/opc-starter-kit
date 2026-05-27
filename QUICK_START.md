# Quick Start Guide / 5 分钟上手指南

**[中文](#中文版) | [English](#english-version)**

---

## English Version

### Prerequisites

- An AI coding assistant that supports custom skills (Comate, or any platform that loads SKILL.md files)
- A project directory where you want to build your startup

### Step 1: Install the Skill

```bash
# One-command install (auto-detects CodeBuddy or Comate)
./install.sh /path/to/your-project

# Or install to current directory:
./install.sh

# Windows:
install.bat C:\path\to\your-project
```

> The installer auto-detects whether you use **CodeBuddy** (`.codebuddy/skills/`) or **Comate** (`.comate/skills/`).

### Step 2: Start Your First Session

In your project directory, open your AI assistant and type:

```
opc
```

The skill will:
1. Check for `.opc-state.json` (your project state file)
2. If not found → Welcome screen + start from Ideation stage
3. If found → Resume from where you left off

### Step 3: Describe Your Idea

```
opc I have an idea — an invoice management tool for indie developers
```

The skill will guide you through problem hypothesis refinement. You'll produce your first document: `docs/01-problem-statement.md`.

### Step 4: Follow the Checkpoints

The skill gives you one task at a time. After each task completes, a document is auto-saved to `docs/`. You always know where you are:

```
Ideation (2/4 complete):
  [x] Problem statement     → docs/01-problem-statement.md
  [x] Competitive landscape  → docs/02-competitive-map.md
  [ ] Interview guide        → Not started
  [ ] Interview synthesis    → Not started
```

### Step 5: Resume Anytime

Close the window. Come back tomorrow. Type one word:

```
opc
```

The skill reads your state file and picks up exactly where you left off. No setup, no re-explanation.

---

### Common Commands

| You say | What happens |
|---|---|
| `opc` | Read state, show current stage and tasks |
| `opc I have an idea` | Start from Ideation Stage, Step 1 |
| `opc Should I add this feature?` | Trigger scope creep pressure test |
| `opc Do I have PMF?` | Trigger PMF assessment flow |
| `opc I'm overwhelmed` | Trigger founder bottleneck audit |
| `opc Skip this step` | Skip current step (with explicit risk acknowledgment) |

### How the Window System Works

- **Main window** (your first conversation): Manages stage transitions, shows task lists, does lightweight tasks
- **Task windows** (separate conversations for deep work): Load a task file, do one deep task, save output, return to main window

When the skill says "I've created a task file: `docs/tasks/task-xxx.md`", it means:
1. Open a new conversation window
2. Type: `opc execute task task-xxx.md`
3. Complete the task
4. Return to the main window

Some tasks can run in parallel (e.g., competitive analysis + market trend analysis). The skill will tell you which ones.

---

## 中文版

### 前提条件

- 支持自定义技能的 AI 编程助手（Comate 或任何能加载 SKILL.md 文件的平台）
- 你想在其中构建创业项目的目录

### 第 1 步：安装技能

```bash
# 一键安装（自动检测 CodeBuddy 或 Comate）
./install.sh /path/to/你的项目

# 或者安装到当前目录：
./install.sh

# Windows：
install.bat C:\path\to\你的项目
```

> 安装脚本会自动检测你用的是 **CodeBuddy**（`.codebuddy/skills/`）还是 **Comate**（`.comate/skills/`）。

### 第 2 步：开始第一次会话

在你的项目目录下，打开 AI 助手，输入：

```
opc
```

技能会：
1. 检查 `.opc-state.json`（你的项目状态文件）
2. 如果不存在 → 欢迎界面 + 从想法阶段开始
3. 如果存在 → 从你上次中断的地方继续

### 第 3 步：描述你的想法

```
opc 我有个想法 — 做一个给独立开发者用的发票管理工具
```

技能会引导你打磨问题假设。你的第一个文档自动产出：`docs/01-problem-statement.md`。

### 第 4 步：跟着检查站走

技能每次只给你一个任务。每个任务完成后，文档自动保存到 `docs/`。你随时知道自己在哪：

```
想法阶段（2/4 完成）：
  [x] 问题陈述打磨  → docs/01-problem-statement.md
  [x] 竞品格局分析  → docs/02-competitive-map.md
  [ ] 客户访谈引导  → 待开始
  [ ] 访谈后合成    → 待开始
```

### 第 5 步：随时回来

关掉窗口。明天再回来。只输一个词：

```
opc
```

技能读取状态文件，从你中断的地方继续。无需设置，无需重新解释。

---

### 常用命令

| 你说 | 技能的行为 |
|---|---|
| `opc` | 读取状态，展示当前阶段和任务 |
| `opc 我有个想法` | 从想法阶段第一步开始 |
| `opc 这个功能该不该加` | 触发范围蔓延压力测试 |
| `opc 我是不是 PMF 了` | 触发 PMF 判定流程 |
| `opc 我忙不过来了` | 触发创始人瓶颈审计 |
| `opc 跳过当前环节` | 跳过当前步骤（需显式确认风险） |

### 窗口工作模式

- **主控窗口**（你打开的第一个对话）：管理阶段转换、展示任务列表、执行轻量任务
- **子窗口**（用于深度工作的独立对话）：加载任务文件、做一件事、保存产出、回到主控窗口

当技能说"我已创建任务文件：`docs/tasks/task-xxx.md`"时，意思是：
1. 打开一个新的对话窗口
2. 输入：`opc 执行任务 task-xxx.md`
3. 完成任务
4. 回到主控窗口继续

有些任务可以并行执行（比如竞品分析 + 市场趋势分析）。技能会告诉你哪些可以。
