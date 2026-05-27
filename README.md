# ⛔ opc-starter-kit

> *你的 AI 一个下午就能造出任何东西。正因如此，你更需要一个检查站，拦住它别造错东西。*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![4 Stages](https://img.shields.io/badge/阶段-4-green)]()
[![27 Failure Modes Guarded](https://img.shields.io/badge/防御失败模式-27-orange)]()
[![Based on Anthropic Founder's Playbook](https://img.shields.io/badge/来源-Anthropic%20创始人行动手册(2026.05)-blue)](https://claude.com/blog/the-founders-playbook)

中文 | **[English](README.en.md)**

---

## 这个 Skill 从哪来

2026 年 5 月，**Anthropic**（Claude 的母公司）的核心高层亲自领衔发布了 **[《创始人行动手册》](https://claude.com/blog/the-founders-playbook)**——一份 36 页的官方指南，系统讲述如何打造一家 AI-Native 一人公司。

这不是一篇博客。不是某个 KOL 的经验分享。这是 **Claude 背后那家公司**，把自己内部实践和最前沿 AI-Native 创业公司的实战经验，浓缩成的一套方法论。

**这个 skill，就是把这份手册变成了代码。**

每一章、每一个失败模式、每一个检查站，都被提炼封装成了一个可直接安装到 AI 编程工具中的纪律工具。它不是手册的摘要——它是手册的**强制执行**。

---

## 它解决什么问题

**42% 的创业失败是因为做了没人要的东西。** AI 让这个数字只会更高。当你一个下午就能从"我有个想法"走到"我有个产品"，跳过验证的诱惑是压倒性的。

opc-starter-kit 就是那个敢跟你说真话的合伙人。它把一套**四阶段门控流程**装进你的 AI 工具，证据不够，绝不放行：

```
你的想法
   ↓
🛑 阶段 1：想法验证  — "证明这个问题真实存在"
   ↓  红队攻击你的假设。绿队审查你的证据。
🛑 阶段 2：MVP      — "证明真的有人要这个"
   ↓  红队追猎假阳性。绿队要求真实的 PMF 信号。
🛑 阶段 3：发布      — "证明这能成为一门生意"
   ↓  红队压测你的运营。绿队验证增长可重复。
🛑 阶段 4：规模化    — "证明你的护城河是真的"
   ↓
一家有护城河的公司。而不只是一个产品。
```

每个关口：**🔴 红队**（反方代言人）+ **🟢 绿队**（退出标准）。证据不充分，不许通过。

---

## 防住的 5 个致命失败模式（共 27 个）

| 你正在做的事 | 实际发生的后果 | 它怎么拦住你 |
|---|---|---|
| *"让 AI 直接写代码"* | 做出来了但没人要 | 门控锁死，问题验证不过不许建造 |
| *"我觉得 PMF 了"* | 把早期热度当真需求 | Sean Ellis 测试 + 假阳性排查 + 努力测试 |
| *"加个功能吧反正快"* | 范围失控，产品没了焦点 | 每次加功能被追问"几个用户明确要的？" |
| *"AI 帮我验证了想法"* | 确认偏误配上 AI 放大器 | 强制反方代言人：为竞品写出获胜论证 |
| *"度量以后再说"* | 分不清真 PMF 和噪音 | 第一个用户来之前必须建好度量框架 |

**[完整目录：27 个失败模式 →](FAILURE_MODES.md)**

---

## 🚀 安装

把链接发给你的 AI IDE，说 **"帮我安装这个 skill"**：

```
https://github.com/ailetian/opc-starter-kit
```

或用命令行：

```bash
npx skills add ailetian/opc-starter-kit -y
```

然后输入 **`opc`** 开始使用。

---

## 30 秒看懂区别

| 没有 opc-starter-kit | 有 opc-starter-kit |
|---|---|
| AI 写代码 → "产品出来了" → 没人要 | 4 道检查站全过，才写第一行代码 |
| "AI 帮我验证了" → 回声室效应 | 反方代言人从 3 个角度攻击你的假设 |
| 数据涨了 → 宣布胜利 | Sean Ellis 测试 + 努力测试 + 假阳性排查 |
| 文件散落，换个窗口就断片 | docs/ 里是一整条决策追溯链，随时可续 |
| 没人挑战你的盲区 | 红队主动为竞品构建获胜论证 |

---

## 命令速查

| 命令 (英文) | 中文 | 行为 |
|---|---|---|
| `opc` | `opc` | 仪表盘：你在哪、该做什么 |
| `opc start` | `opc 启动` | 初始化新项目 |
| `opc idea` | `opc 我有个想法` | 进入想法验证阶段 |
| `opc pmf` | `opc 我是不是 PMF 了` | 完整 PMF 判定 |
| `opc scope-check` | `opc 这个功能该不该加` | 范围蔓延压力测试 |
| `opc bottleneck` | `opc 我忙不过来了` | 创始人瓶颈审计 |
| `opc moat-test` | `opc 护城河压力测试` | 模拟 5000 万美元竞品入侵 |
| `opc retrospective` | `opc 事后诊断` | 已造了产品？诊断跳过了什么 |
| `opc help` | `opc 帮助` | 显示全部命令 |

---

## 来源

**[Anthropic — The Founder's Playbook (2026.05)](https://claude.com/blog/the-founders-playbook)**

由 Anthropic 核心高层亲自撰写并发布。本 skill 忠实提炼了手册的完整框架——全部四个阶段、全部 27 个失败模式、对抗性思维方法论——封装为可安装、可执行的 AI 纪律工具。

中文译本：花叔 × Claude Code。

---

## 许可证

[MIT](LICENSE) —— 随便用、随便改、随便传。但别跳过验证。
