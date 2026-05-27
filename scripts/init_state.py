#!/usr/bin/env python3
"""Initialize or restore the opc-starter-kit state file (.opc-state.json).

Usage:
    python init_state.py [project_name] [project_type]

Arguments:
    project_name: Name of the project (default: "")
    project_type: Type of project, e.g. "saas", "hardware" (default: "saas")

If .opc-state.json already exists, prints current state without overwriting.
If it doesn't exist, creates a new one with default values.
"""

import json
import os
import sys
from datetime import datetime, timezone


DEFAULT_STATE = {
    "project_name": "",
    "project_type": "saas",
    "current_stage": "idea",
    "stage_status": "in_progress",
    "skill_version": "2.0",
    "stages": {
        "idea": {"status": "in_progress", "started_at": "", "completed_at": "",
                 "tasks_completed": [], "skipped": []},
        "mvp": {"status": "not_started", "started_at": "", "completed_at": "",
                "tasks_completed": [], "skipped": []},
        "launch": {"status": "not_started", "started_at": "", "completed_at": "",
                   "tasks_completed": [], "skipped": []},
        "scale": {"status": "not_started", "started_at": "", "completed_at": "",
                  "tasks_completed": [], "skipped": []}
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
    "current_task": None,
    "child_tasks": [],
    "decisions_log": []
}


STATE_FILE = ".opc-state.json"


def init_state(project_name="", project_type="saas"):
    """Initialize or load state file."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            state = json.load(f)
        print(f"State file already exists. Current stage: {state.get('current_stage', 'unknown')}")
        print(f"Project: {state.get('project_name', '(unnamed)')}")
        return state

    state = DEFAULT_STATE.copy()
    state["project_name"] = project_name
    state["project_type"] = project_type
    now = datetime.now(timezone.utc).isoformat()
    state["stages"]["idea"]["started_at"] = now

    # Ensure docs/ directory exists
    os.makedirs("docs", exist_ok=True)

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

    print(f"State file created: {STATE_FILE}")
    print(f"Project: {project_name or '(unnamed)'}")
    print(f"Type: {project_type}")
    print(f"Starting stage: idea")
    return state


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else ""
    ptype = sys.argv[2] if len(sys.argv) > 2 else "saas"
    init_state(name, ptype)