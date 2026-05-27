#!/usr/bin/env python3
"""Generate a task file for the opc-starter-kit sub-window mode.

Usage:
    python create_task_file.py <task_name> [--stage <stage>]

Creates a task file at docs/task-<task_name>.md with:
    - Current project context (from .opc-state.json)
    - Stage information
    - Task instructions
    - Expected output format

This file is then loaded by the sub-window AI session via:
    opc task task-<task_name>.md  (or opc 执行任务 task-<task_name>.md)
"""

import json
import os
import sys
from datetime import datetime, timezone


STATE_FILE = ".opc-state.json"
DOCS_DIR = "docs"

TASK_TEMPLATES = {
    "competitive-analysis": {
        "title": "竞品格局分析",
        "stage": "idea",
        "instructions": """
## 任务：竞品格局分析

### 背景
基于当前问题陈述（见下方），执行完整的四层竞品格局分析。

### 操作步骤
1. 阅读问题陈述，理解目标用户和核心痛点
2. **第一层：直接竞品** — 找出至少3个解决完全相同问题的产品
3. **第二层：间接竞品** — 找出用不同方式解决同类问题的产品
4. **第三层：潜在收购方** — 找出可能进入这个市场的大公司
5. **第四层：相邻玩家** — 找出当前不竞争但未来可能进入的玩家
6. 为每层至少选1个代表性竞品，写出"为什么他们会赢"的论证
7. 识别差异化空间并评估其可行性

### 输出要求
保存为 `docs/competitive-map.md`，使用以下结构：

```markdown
# 竞品格局分析

## 第一层：直接竞品
| 竞品 | 核心功能 | 优势 | "为什么他们会赢" |
|------|---------|------|-----------------|
| ... | ... | ... | ... |

## 第二层：间接竞品
...

## 第三层：潜在收购方
...

## 第四层：相邻玩家
...

## 差异化空间
- 发现的空白：[描述]
- 可行性评估：[竞品能否轻松进入？需要多久？]
- 竞品软肋：[战略选择导致的不可覆盖的盲区]
```

### 完成后
输出摘要，告知主控窗口任务已完成。
"""
    },
    "scope-pressure-test": {
        "title": "范围压力测试",
        "stage": "mvp",
        "instructions": """
## 任务：范围压力测试

### 背景
用户提议新增一个功能。需要执行范围压力测试来判断是否应该添加。

### 操作步骤
1. 确认新增功能的具体描述
2. 检查现有范围文档（docs/scope-doc.md）的锁定内容
3. 评估该功能是否在原始MVP范围内
4. 追问：有多少用户明确要求这个功能？
5. 评估添加这个功能的隐藏成本（维护、文档、测试、用户教育）

### 输出要求
将评估结果追加到 `docs/scope-doc.md` 的"范围变更记录"部分：

```markdown
## 范围变更记录

### [日期] 提议：[功能名]
- 提议理由：[用户描述]
- 用户需求证据：[几个用户/什么场景]
- 评估：[通过/不通过]
- 理由：[如果通过，为什么值得扩展；如果不通过，为什么现在不做]
```

### 完成后
输出摘要，告知主控窗口。
"""
    },
    "tech-debt-audit": {
        "title": "技术债审计",
        "stage": "launch",
        "instructions": """
## 任务：技术债审计

### 背景
发布阶段开始，需要对代码库中的技术债进行全面审计。

### 操作步骤
1. 扫描项目结构，识别以下维度的问题：
   - 结构性弱点：哪些模块改动会导致连锁反应？
   - 测试覆盖缺口：哪些关键路径缺少测试？
   - 性能瓶颈：哪些操作在生产负载下会出问题？
   - 依赖风险：哪些关键依赖不受控制？

2. 三档分类：
   - 🔴 发布前必须修
   - 🟡 可等一个冲刺
   - 🟢 可接受的持续债务

### 输出要求
保存为 `docs/tech-debt-audit.md`。

### 完成后
输出摘要，告知主控窗口。
"""
    },
    "moat-pressure-test": {
        "title": "护城河压力测试",
        "stage": "scale",
        "instructions": """
## 任务：护城河压力测试

### 背景
模拟5000万美元资金的竞品进入市场，推演防御能力。

### 操作步骤
1. 基于 docs/moat-scorecard.md 的当前数据
2. 在T=0、T=30、T=90三个时间点推演：
   - 竞品最先攻击哪类客户？
   - 哪类客户最脆弱？
   - 每个时间点后你的护城河还在吗？

### 输出要求
更新 `docs/moat-scorecard.md`，追加压力测试结果。

### 完成后
输出摘要，告知主控窗口。
"""
    },
    "interview-guide": {
        "title": "客户访谈引导",
        "stage": "idea",
        "instructions": """
## 任务：客户访谈引导

### 背景
需要为用户生成客户访谈问题清单和引导文档。

### 操作步骤
1. 阅读当前问题陈述（docs/problem-statement.md）
2. 审查用户草拟的问题，检查四类问题：
   - 诱导性问题（暗示答案的问题）
   - 面向未来的问题（"你会用吗？"）
   - 过宽的问题（无法得到具体信息）
   - 社会期许问题（引导用户说"正确"答案）
3. 将不合格问题修正为追问过去行为的开放问题
4. 针对不同用户画像生成定制问题组

### 输出要求
保存为 `docs/interview-guide.md`，使用 assets/templates/interview-guide.md 作为模板。

### 完成后
输出摘要，告知主控窗口。
"""
    },
    "metrics-framework": {
        "title": "度量框架定义",
        "stage": "mvp",
        "instructions": """
## 任务：度量框架定义

### 背景
在第一个用户来之前，需要定义什么是 PMF 的度量标准。

### 操作步骤
1. 基于问题陈述和产品方向，定义：
   - 留存基准：什么算活跃用户？DAU/WAU/MAU 标准
   - 激活标准：用户做了什么才算激活？
   - 时间目标：第7天/第30天/第90天目标
   - 假阳性模式：哪些信号看起来像 PMF 但不是
2. 如果项目是非 SaaS 类型，调整指标定义

### 输出要求
保存为 `docs/metrics-framework.md`，使用 assets/templates/metrics-framework.md 作为模板。

### 完成后
输出摘要，告知主控窗口。
"""
    },
    "pmf-assessment": {
        "title": "PMF 判定",
        "stage": "mvp",
        "instructions": """
## 任务：PMF 判定

### 背景
用户宣称可能达到 PMF，需要执行完整的 PMF 判定流程。

### 操作步骤
1. **Sean Ellis 测试**：引导用户想活跃用户发调查
2. **假阳性排查**：检查四类假阳性模式
3. **多信号确认**：留存/付费/推荐三者至少有其二
4. **三角验证**：故事+数字+反例
5. **努力测试**：用户是"被推"还是"被拉"

### 输出要求
保存为 `docs/pmf-assessment.md`，使用 assets/templates/pmf-assessment.md 作为模板。

### 完成后
输出摘要和判定结论，告知主控窗口。
"""
    },
    "bottleneck-audit": {
        "title": "创始人瓶颈审计",
        "stage": "launch",
        "instructions": """
## 任务：创始人瓶颈审计

### 背景
发布阶段需要识别所有卡在创始人身上的流程和决策。

### 操作步骤
1. 列出所有经过创始人的工作流/决策/审批/操作
2. 按"若一周不在"分类：🔴一定会停 / 🟡可能卡住 / 🟢不受影响
3. 识别三类事项：能自动化的 / 需人但不一定需你 / 确实需你的
4. 对每项 🔴 给出解除建议

### 输出要求
保存为 `docs/bottleneck-audit.md`，使用 assets/templates/bottleneck-audit.md 作为模板。

### 完成后
输出摘要（含 🔴🟡🟢 统计），告知主控窗口。
"""
    },
    "moat-narrative": {
        "title": "护城河叙事",
        "stage": "scale",
        "instructions": """
## 任务：护城河叙事

### 背景
规模化阶段需要生成供投资人和大客户使用的护城河论证。

### 操作步骤
1. 基于 docs/moat-scorecard.md 的当前数据
2. 从三个维度展开论证：
   - 数据飞轮：运转时间、独特数据资产、复制难度
   - 工作流锁定：客户分层（L1/L2/L3）、切换成本估算
   - 领域知识壁垒：通用竞品会做错的边缘案例
3. 生成对外版护城河声明（一段简洁文字）
4. 推演 5000万竞品入侵场景

### 输出要求
保存为 `docs/moat-narrative.md`，使用 assets/templates/moat-narrative.md 作为模板。

### 完成后
输出摘要，告知主控窗口。
"""
    },
    "one-pager": {
        "title": "一页纸摘要",
        "stage": "any",
        "instructions": """
## 任务：生成一页纸摘要

### 背景
用户需要快速生成可分享的项目当前状态摘要。

### 操作步骤
1. 读取 .opc-state.json 和 docs/ 下的所有产物
2. 生成紧凑摘要，包含：
   - 我在做什么
   - 卡在哪
   - 最有信心的发现
   - 最不确定的事
   - 我在找什么帮助
3. 格式紧凑，适合截图分享

### 输出要求
保存为 `docs/one-pager.md`。

### 完成后
输出摘要，告知主控窗口可截图分享。
"""
    },
    "peer-review": {
        "title": "盲审报告",
        "stage": "any",
        "instructions": """
## 任务：生成盲审报告

### 背景
用户需要外部反馈但不想暴露身份。

### 操作步骤
1. 读取所有阶段产物
2. 剥离创始人身份信息（姓名、公司名、具体产品名）
3. 生成匿名化的：问题陈述 + 假设 + 证据摘要 + 不确定问题
4. 语言保持客观中立

### 输出要求
保存为 `docs/peer-review-package.md`。

### 完成后
输出摘要，告知主控窗口可发给社区/导师获取反馈。
"""
    },
}


def load_state():
    """Load state file."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def create_task_file(task_name, stage=None):
    """Create a task file."""
    state = load_state()
    os.makedirs(DOCS_DIR, exist_ok=True)

    filename = f"docs/task-{task_name}.md"
    now = datetime.now(timezone.utc).isoformat()

    # Get template or create generic one
    template = TASK_TEMPLATES.get(task_name)
    if template:
        title = template["title"]
        instructions = template["instructions"]
        task_stage = template["stage"]
    else:
        title = task_name.replace("-", " ").title()
        instructions = f"""
## 任务：{title}

请根据当前阶段上下文完成此任务。

完成后保存产出到 docs/ 目录下，并输出摘要。
"""
        task_stage = stage or (state["current_stage"] if state else "idea")

    # Build context section
    context = ""
    if state:
        context = f"""
## 项目上下文

- **项目名称**：{state.get('project_name', '(未命名)')}
- **项目类型**：{state.get('project_type', 'saas')}
- **当前阶段**：{state.get('current_stage', 'idea')}
- **阶段状态**：{state.get('stage_status', 'in_progress')}
- **已完成任务**：{state['stages'][state['current_stage']]['tasks_completed']}
- **风险等级**：{state['risk_profile']['overall_risk']}

> 生成时间：{now}
"""

    content = f"""# {title} — 任务文件

> 阶段：{task_stage} | 创建时间：{now}

{context}
{instructions}
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Task file created: {filename}")
    print(f"Stage: {task_stage}")

    # List available templates if the task_name wasn't recognized
    if task_name not in TASK_TEMPLATES:
        print(f"\nNote: '{task_name}' is not a known task template. Using generic template.")
        print(f"Known templates: {', '.join(TASK_TEMPLATES.keys())}")

    return filename


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_task_file.py <task_name> [--stage <stage>]")
        print(f"Known task names: {', '.join(TASK_TEMPLATES.keys())}")
        sys.exit(1)

    task_name = sys.argv[1]
    stage = None
    if "--stage" in sys.argv:
        idx = sys.argv.index("--stage")
        if idx + 1 < len(sys.argv):
            stage = sys.argv[idx + 1]

    create_task_file(task_name, stage)