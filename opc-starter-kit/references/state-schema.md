# .opc-state.json 状态文件完整 Schema

> 所有项目状态存储在项目根目录的 `.opc-state.json`。此文件由 skill 自动维护，用户无需手动编辑。

---

## 完整 JSON Schema

```json
{
  "project_name": "",
  "project_type": "saas",
  "current_stage": "idea",
  "stage_status": "in_progress",
  "skill_version": "2.0",
  "stages": {
    "idea": { "status": "in_progress", "started_at": "", "completed_at": "", "tasks_completed": [], "skipped": [] },
    "mvp": { "status": "not_started", "started_at": "", "completed_at": "", "tasks_completed": [], "skipped": [] },
    "launch": { "status": "not_started", "started_at": "", "completed_at": "", "tasks_completed": [], "skipped": [] },
    "scale": { "status": "not_started", "started_at": "", "completed_at": "", "tasks_completed": [], "skipped": [] }
  },
  "risk_profile": {
    "skip_count": 0,
    "skipped_items": [],
    "hard_evidence_count": 0,
    "hard_evidence_missing": [],
    "internal_consistency_flags": 0,
    "opc_passive_nudge_rejected_count": 0,
    "overall_risk": "normal"
  },
  "current_task": null,
  "child_tasks": [],
  "decisions_log": []
}
```

---

## 字段说明

### project_name
项目名称，`opc start` 时由用户输入。

### project_type
项目类型，支持：`saas`（默认）、`hardware`、`content`、`api`、`consulting`、`opensource`。影响 PMF 信号的判定标准。

### current_stage
当前所处阶段：`idea` / `mvp` / `launch` / `scale`。

### stage_status
当前阶段状态：`not_started` / `in_progress` / `completed`。

### stages.{stage}
- `status`：该阶段状态
- `started_at`：阶段开始时间（ISO 8601）
- `completed_at`：阶段完成时间
- `tasks_completed`：已完成的微步骤列表
- `skipped`：被跳过的步骤列表

### risk_profile
- `skip_count`：累计跳过次数
- `skipped_items`：跳过的具体内容
- `hard_evidence_count`：已上传的硬证据数量
- `hard_evidence_missing`：缺少硬证据的关键节点
- `internal_consistency_flags`：内部一致性检测的漂移标记数
- `opc_passive_nudge_rejected_count`：用户拒绝被动提醒的次数
- `overall_risk`：综合风险评估（`normal` / `elevated` / `high`）

### current_task
当前正在执行的任务名称。

### child_tasks
子窗口任务列表。

### decisions_log
关键决策记录（也同步写入 `docs/decisions.md`）。

---

## 状态文件丢失恢复规则

1. 扫描 `docs/` 中已有产物，根据文件名推断当前阶段
2. 若 `docs/` 也为空，按新项目处理（重置为想法阶段）
3. 恢复时 `risk_profile` 和 `decisions_log` 可能丢失部分数据，已在 `docs/decisions.md` 中的记录不受影响
