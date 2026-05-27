# ⛔ opc-starter-kit

> *Your AI can build anything in an afternoon. That's exactly why you need a checkpoint before it builds the wrong thing.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![4 Stages](https://img.shields.io/badge/Stages-4-green)]()
[![27 Failure Modes Guarded](https://img.shields.io/badge/Failure%20Modes%20Guarded-27-orange)]()
[![Based on Anthropic Founder's Playbook](https://img.shields.io/badge/Source-Anthropic%20Founder's%20Playbook%20(2026.05)-blue)](https://claude.com/blog/the-founders-playbook)

**[中文](README.zh-CN.md)** | English

---

## Where This Comes From

In May 2026, **Anthropic** — the company behind Claude — published **[The Founder's Playbook](https://claude.com/blog/the-founders-playbook)**, a 36-page official guide written by their core leadership on how to build an AI-native one-person company.

It's not a blog post. It's not influencer advice. It's the playbook from the company that literally builds the AI infrastructure powering the next generation of startups — distilling what they've learned from their own internal practices and the most advanced AI-native companies they serve.

**This skill is that playbook, turned into code.**

Every chapter, every failure mode, every checkpoint has been extracted and encoded into an AI discipline tool that installs directly into your coding environment. It doesn't summarize the playbook — it *enforces* it.

---

## The Problem It Solves

**42% of startups fail because they build something nobody wants.** AI makes this worse, not better. When you can go from "I have an idea" to "I have a product" in a single afternoon, the temptation to skip validation is overwhelming.

opc-starter-kit is the discipline you'd get from a co-founder who's not afraid to tell you the truth. It installs a **4-stage gate process** that blocks you from building until you've proven you should:

```
Your Idea
   ↓
🛑 STAGE 1: IDEATION   — "Prove this problem is real"
   ↓  Red Team attacks your assumptions. Green Team checks your evidence.
🛑 STAGE 2: MVP        — "Prove someone actually wants this"
   ↓  Red Team hunts false positives. Green Team demands real PMF signals.
🛑 STAGE 3: LAUNCH     — "Prove this can become a business"
   ↓  Red Team stress-tests your operations. Green Team verifies repeatable growth.
🛑 STAGE 4: SCALE      — "Prove your moat is real"
   ↓
A defensible company. Not just a product.
```

At every gate: **🔴 Red Team** (devil's advocate) + **🟢 Green Team** (exit criteria). You don't pass until the evidence is sufficient.

---

## 5 Failure Modes It Catches (of 27)

| What you're doing | What's really happening | How it stops you |
|---|---|---|
| *"Let AI just write the code"* | Building something nobody wants | Gate locked until problem validation passes |
| *"I think we have PMF"* | Mistaking early hype for real demand | Sean Ellis test + false positive screening + effort test |
| *"One more feature, it's fast"* | Scope creeps until product has no focus | Every feature challenged: "How many users explicitly asked?" |
| *"AI validated my idea"* | Confirmation bias with an AI amplifier | Mandatory devil's advocate writes the competition's winning argument |
| *"We'll measure later"* | Can't tell real PMF from noise | Metrics framework must exist before the first user arrives |

**[Full catalog: 27 failure modes →](FAILURE_MODES.md)**

---

## 🚀 Install

Send this link to your AI IDE and say **"Install this skill"**:

```
https://github.com/ailetian/opc-starter-kit
```

Or use CLI:

```bash
npx skills add ailetian/opc-starter-kit -y
```

Then type **`opc`** to start.

---

## 30-Second Before/After

| Without opc-starter-kit | With opc-starter-kit |
|---|---|
| AI writes code → "Look, a product!" → nobody wants it | 4 checkpoints passed before a single line of code |
| "AI validated my idea" → echo chamber | Devil's advocate argues against you from 3 angles |
| Early traction → declare victory | Sean Ellis test + effort test + false positive screening |
| Files scattered, context lost | Full decision trail in `docs/`, state auto-saved |
| No one challenges your blind spots | Red team builds the competition's winning argument |

---

## Commands

| Command (EN) | 中文 | What happens |
|---|---|---|
| `opc` | `opc` | Dashboard: where you are, what's next |
| `opc start` | `opc 启动` | Initialize a new project |
| `opc idea` | `opc 我有个想法` | Enter ideation stage |
| `opc pmf` | `opc 我是不是 PMF 了` | Full PMF assessment |
| `opc scope-check` | `opc 这个功能该不该加` | Scope creep pressure test |
| `opc bottleneck` | `opc 我忙不过来了` | Founder bottleneck audit |
| `opc moat-test` | `opc 护城河压力测试` | Simulate $50M competitor invasion |
| `opc retrospective` | `opc 事后诊断` | Already built? Diagnose what you skipped |
| `opc help` | `opc 帮助` | Show all commands |

---

## Source

**[Anthropic — The Founder's Playbook (May 2026)](https://claude.com/blog/the-founders-playbook)**

Written and published by Anthropic's core leadership. This skill faithfully extracts the playbook's complete framework — all four stages, all 27 failure modes, the adversarial thinking methodology — into an installable, enforceable AI discipline tool.

Chinese translation by 花叔 (Huashu) × Claude Code.

---

## License

[MIT](LICENSE) — Fork it, ship it, share it. Just don't skip validation.
