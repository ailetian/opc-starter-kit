# Before vs. After: With and Without opc-starter-kit

> Real scenarios where founders make costly mistakes, and how this skill prevents them.

---

## Scenario 1: The "Just Build It" Trap / "直接开造"陷阱

```
WITHOUT this skill:
─────────────────────────────────────────────────
Day 1:   "I have an idea!"
Day 1:   → Ask AI to write code
Day 3:   → Working prototype done
Day 7:   → Ship it
Day 30:  → Nobody uses it
Day 31:  → "Why didn't it work? AI validated my idea..."

WITH this skill:
─────────────────────────────────────────────────
Day 1:   "I have an idea!" → opc
Day 1:   → Skill: "Let's test if this problem is real first."
Day 1-3: → Problem hypothesis refinement → docs/01-problem-statement.md
Day 3-5: → Devil's advocate challenges your assumption
Day 5-7: → Competitive landscape → docs/02-competitive-map.md
Day 7-14:→ Customer interviews with structured questions
Day 14:  → 5 interviews synthesized → docs/05-problem-hypothesis.md
Day 14:  → Exit criteria check: "Do you have enough signal?"
Day 15:  → Only NOW do you start building
Day 45:  → Product built on validated evidence, not faith
```

**The difference**: 2 weeks of validation saves you from building something nobody wants. The 42% failure rate starts here.

---

## Scenario 2: The "AI Validated My Idea" Trap / "AI帮我验证了"陷阱

```
WITHOUT this skill:
─────────────────────────────────────────────────
You: "AI, is this a good idea?"
AI: "The market is large, the problem is real, and your approach
     is differentiated. Here's supporting data..."
You: "Great, validated! Let's build it."
→ Confirmation bias + AI amplifier
→ You found evidence for what you already believed

WITH this skill:
─────────────────────────────────────────────────
You: "AI, is this a good idea?"
Skill: "Before we look at supporting evidence, let me argue
       against your idea from three angles:"
  1. "This problem isn't worth building a company for, because..."
  2. "There are already good solutions; your differentiation
      doesn't hold because..."
  3. "Your target users won't pay for this, because..."
You: "Hmm, point 2 is actually valid..."
→ Genuine understanding of risks and blind spots
→ Decision based on evidence, not confirmation
```

**The difference**: The devil's advocate is mandatory and cannot be skipped. It argues from the competition's perspective with specific evidence, not generic doubt.

---

## Scenario 3: The "We Have PMF" Trap / "我觉得PMF了"陷阱

```
WITHOUT this skill:
─────────────────────────────────────────────────
Week 2:  100 signups after Product Hunt launch
Week 3:  "We have PMF! Let's scale!"
Week 4:  Hire 3 people, start expansion
Week 8:  80% of users have churned
         → Early traction was from HN traffic, not real demand
         → Now you have 3 salaries to pay and no real users

WITH this skill:
─────────────────────────────────────────────────
Week 2:  100 signups after Product Hunt launch
Week 2:  → Skill: "Let's check if this is real PMF."
         → Sean Ellis test: "How would you feel if you could
            never use this product again?"
         → Result: Only 22% say "very disappointed" (threshold: 40%)
         → False positive check: 80 signups but only 15 activated
         → Effort test: You're still personally onboarding every user
         → "This is NOT PMF yet. Here's what to iterate on."
Week 6:  After 3 iterations, Sean Ellis hits 45%
         → Retention, revenue, AND referral all present
         → NOW you can scale with confidence
```

**The difference**: One test prevents you from scaling on false signals and burning runway.

---

## Scenario 4: The "Feature Factory" Trap / "功能工厂"陷阱

```
WITHOUT this skill:
─────────────────────────────────────────────────
Week 1:  MVP scope: 3 core features
Week 2:  "Let's also add dark mode" — 1 afternoon
Week 3:  "Users asked for CSV export" — 1 afternoon
Week 4:  "Wouldn't notifications be nice?" — 1 afternoon
Week 6:  12 features, none polished
         → Product is a mile wide and an inch deep
         → Original value proposition is diluted
         → Each feature alone looks reasonable

WITH this skill:
─────────────────────────────────────────────────
Week 1:  MVP scope locked: docs/07-scope-doc.md
         → Core: 3 features
         → Explicitly NOT doing: dark mode, CSV export, notifications
         → Feature addition criteria: "Enough users have told us
            they can't get value without it"
Week 3:  "Users asked for CSV export"
         → Skill: "How many users? Is this a core need or nice-to-have?
            What specific evidence do you have?"
         → "2 out of 15 users mentioned it" → Not sufficient
         → Documented in metrics framework
Week 5:  "8 out of 15 users say they can't complete their workflow
         without CSV export"
         → Skill: "Sufficient evidence. Update scope document."
```

**The difference**: The decision point changes from "Should we build this?" to "Do we have enough user evidence that this is needed?"

---

## Scenario 5: The "Founder Bottleneck" Trap / "创始人瓶颈"陷阱

```
WITHOUT this skill:
─────────────────────────────────────────────────
Month 1-3: You handle everything personally
Month 4:   Support tickets pile up — only you know the answers
Month 5:   Product decisions wait a week because they need your sign-off
Month 6:   You're working 80-hour weeks but the company is stalled
           → You ARE the company, and you can't scale yourself

WITH this skill:
─────────────────────────────────────────────────
Month 3:   Launch stage entry → Skill triggers bottleneck audit
           → Lists all workflows/decisions passing through you
           → Classifies each:
             ✓ Can be fully automated (3 items)
             ✓ Needs a person, but not necessarily you (5 items)
             ✓ Truly needs founder judgment (2 items)
           → For the first two categories: designs handoff/automation
Month 4:   You focus on the 2 things only you can do
           → Everything else runs without you
```

**The difference**: The goal isn't to remove yourself from the company — it's to free your attention for decisions only you can make.

---

## Scenario 6: The "Lost Context" Trap / "上下文丢失"陷阱

```
WITHOUT this skill:
─────────────────────────────────────────────────
Session 1: Build feature A with AI
Session 2: AI doesn't remember Session 1 → Builds feature B differently
Session 3: Features A and B don't work together
Session 4: Start over or patch endlessly
           → Agentic technical debt compounds with every session

WITH this skill:
─────────────────────────────────────────────────
Session 1: Load architecture context doc → Build feature A → Log decisions
Session 2: Load architecture context doc → Build feature B consistently
Session 3: Features A and B fit together because they share
           the same architectural decisions
           → Every session builds on the same foundation
```

**The difference**: 5 minutes of documentation per session is cheap insurance against architectural drift that compounds into an unmaintainable codebase.

---

## Summary: The Core Trade-off

| | Without guardrails | With guardrails |
|---|---|---|
| **Speed** | Fast to build, slow to find product-market fit | Slower to start, faster to reach validated PMF |
| **Evidence** | Anecdotal and self-confirming | Structured, challenged, and documented |
| **Risk** | Unknown unknowns | Known risks with explicit acknowledgment |
| **Context** | Lost between sessions | Persistent and auto-saved |
| **Decisions** | Gut-driven | Evidence-based with documented reasoning |
| **Outcome** | 42% chance of building something nobody wants | Significantly reduced failure mode exposure |

The bottleneck is no longer "what you can build" — it's "what you choose to build." This skill helps you choose wisely.

---

> 本文件内容提炼封装自 Anthropic 创始人行动手册（2026.05）——Anthropic 官方发布的、面向 AI-Native 一人公司的创始人行动指南。中文译本来自花叔 x Claude Code，仅供个人学习与内部研究使用，不做商业发行。原版下载请到 [claude.com/blog/the-founders-playbook](https://claude.com/blog/the-founders-playbook)
