#!/usr/bin/env python3
"""Update the opc-starter-kit state file with new values.

Usage:
    python update_state.py --stage <stage> --status <status>
    python update_state.py --task <task_name>
    python update_state.py --complete-task <task_name>
    python update_state.py --skip <item_name>
    python update_state.py --decision <decision_description>
    python update_state.py --hard-evidence <evidence_name>
    python update_state.py --risk <overall_risk>

Updates are applied to the existing .opc-state.json file.
Creates the file if it doesn't exist.
"""

import json
import os
import sys
from datetime import datetime, timezone


STATE_FILE = ".opc-state.json"
VALID_STAGES = ["idea", "mvp", "launch", "scale"]
VALID_STATUSES = ["not_started", "in_progress", "completed"]


def load_state():
    """Load state file or auto-initialize if missing."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        print("State file not found. Auto-initializing...")
        try:
            from init_state import init_state as do_init
            return do_init()
        except ImportError:
            print("Error: .opc-state.json not found and init_state.py unavailable. Run init_state.py first.", file=sys.stderr)
            sys.exit(1)


def save_state(state):
    """Save state to file."""
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    print(f"State updated: {STATE_FILE}")


def update_stage(state, stage, status):
    """Update a specific stage's status."""
    if stage not in VALID_STAGES:
        print(f"Error: Invalid stage '{stage}'. Valid: {VALID_STAGES}", file=sys.stderr)
        sys.exit(1)
    if status not in VALID_STATUSES:
        print(f"Error: Invalid status '{status}'. Valid: {VALID_STATUSES}", file=sys.stderr)
        sys.exit(1)

    state["stages"][stage]["status"] = status
    if status == "in_progress" or status == "completed":
        if not state["stages"][stage]["started_at"]:
            state["stages"][stage]["started_at"] = datetime.now(timezone.utc).isoformat()
    if status == "completed":
        state["stages"][stage]["completed_at"] = datetime.now(timezone.utc).isoformat()
    state["current_stage"] = stage
    state["stage_status"] = status


def add_task(state, task_name):
    """Set the current task."""
    state["current_task"] = task_name


def complete_task(state, task_name):
    """Mark a task as completed in current stage."""
    stage = state["current_stage"]
    tasks = state["stages"][stage]["tasks_completed"]
    if task_name not in tasks:
        tasks.append(task_name)
    if state["current_task"] == task_name:
        state["current_task"] = None
    print(f"Task completed: {task_name} in stage '{stage}'")


def skip_item(state, item_name):
    """Record a skipped item."""
    state["risk_profile"]["skip_count"] += 1
    state["risk_profile"]["skipped_items"].append({
        "item": item_name,
        "stage": state["current_stage"],
        "skipped_at": datetime.now(timezone.utc).isoformat()
    })
    print(f"Skipped: {item_name} (total skips: {state['risk_profile']['skip_count']})")


def add_decision(state, description):
    """Add a decision to the log."""
    state["decisions_log"].append({
        "time": datetime.now(timezone.utc).isoformat(),
        "stage": state["current_stage"],
        "decision": description
    })
    print(f"Decision logged: {description}")


def add_hard_evidence(state, evidence_name):
    """Record hard evidence."""
    state["risk_profile"]["hard_evidence_count"] += 1
    if evidence_name in state["risk_profile"]["hard_evidence_missing"]:
        state["risk_profile"]["hard_evidence_missing"].remove(evidence_name)
    print(f"Hard evidence added: {evidence_name}")


if __name__ == "__main__":
    state = load_state()

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--stage" and i + 2 < len(args):
            update_stage(state, args[i + 1], args[i + 2])
            i += 3
        elif args[i] == "--task" and i + 1 < len(args):
            add_task(state, args[i + 1])
            i += 2
        elif args[i] == "--complete-task" and i + 1 < len(args):
            complete_task(state, args[i + 1])
            i += 2
        elif args[i] == "--skip" and i + 1 < len(args):
            skip_item(state, args[i + 1])
            i += 2
        elif args[i] == "--decision" and i + 1 < len(args):
            add_decision(state, args[i + 1])
            i += 2
        elif args[i] == "--hard-evidence" and i + 1 < len(args):
            add_hard_evidence(state, args[i + 1])
            i += 2
        elif args[i] == "--risk" and i + 1 < len(args):
            state["risk_profile"]["overall_risk"] = args[i + 1]
            i += 2
        else:
            print(f"Unknown or incomplete argument: {args[i]}", file=sys.stderr)
            i += 1

    save_state(state)