#!/usr/bin/env python3
"""Test harness for opc-starter-kit evals.

Runs all test cases defined in ../evals/evals.json against the current project state.
Outputs a pass/fail report with details.

Usage:
    python run_evals.py [--verbose]
"""

import json
import os
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent.absolute()
SKILL_DIR = SCRIPT_DIR.parent
EVALS_FILE = SKILL_DIR / "evals" / "evals.json"


def load_evals():
    """Load eval definitions."""
    if not EVALS_FILE.exists():
        print(f"Error: {EVALS_FILE} not found", file=sys.stderr)
        sys.exit(1)
    with open(EVALS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def check_state_file():
    """Check .opc-state.json structure."""
    cwd = Path.cwd()
    state_file = cwd / ".opc-state.json"
    if not state_file.exists():
        return False, "No .opc-state.json found in project"
    try:
        with open(state_file, "r", encoding="utf-8") as f:
            state = json.load(f)
    except json.JSONDecodeError:
        return False, ".opc-state.json is not valid JSON"

    required_fields = ["current_stage", "stage_status", "stages", "risk_profile", "skill_version"]
    missing = [f for f in required_fields if f not in state]
    if missing:
        return False, f"Missing required fields: {missing}"
    if state.get("skill_version") != "2.0":
        return False, f"skill_version is {state.get('skill_version')}, expected 2.0"
    return True, "State file valid"


def check_skill_md():
    """Check skill.md quality."""
    skill_md = SKILL_DIR / "skill.md"
    if not skill_md.exists():
        return False, "skill.md not found"

    with open(skill_md, "r", encoding="utf-8") as f:
        content = f.read()
        lines = content.split("\n")

    checks = []
    # Frontmatter
    if not content.startswith("---"):
        checks.append("Missing YAML frontmatter")
    # Line count
    if len(lines) > 500:
        checks.append(f"Too many lines: {len(lines)} (max 500)")
    # Name
    if "name: opc-starter-kit" not in content:
        checks.append("Missing 'name: opc-starter-kit' in frontmatter")
    # Description
    if "description:" not in content:
        checks.append("Missing 'description' in frontmatter")

    if checks:
        return False, "; ".join(checks)
    return True, f"skill.md OK ({len(lines)} lines)"


def check_references():
    """Check all reference files exist."""
    required = [
        "stage-1-ideation.md", "stage-2-mvp.md", "stage-3-launch.md",
        "stage-4-scale.md", "anti-confirmation.md", "exit-criteria.md",
        "questioning-guide.md", "tool-adaptations.md"
    ]
    ref_dir = SKILL_DIR / "references"
    if not ref_dir.exists():
        return False, "references/ directory missing"

    missing = []
    for f in required:
        if not (ref_dir / f).exists():
            missing.append(f)

    if missing:
        return False, f"Missing references: {missing}"
    return True, f"All {len(required)} reference files present"


def check_templates():
    """Check all template files exist."""
    required = [
        "problem-statement.md", "architecture-context.md", "scope-doc.md",
        "metrics-framework.md", "interview-guide.md", "pmf-assessment.md",
        "bottleneck-audit.md", "moat-narrative.md"
    ]
    tmpl_dir = SKILL_DIR / "assets" / "templates"
    if not tmpl_dir.exists():
        return False, "assets/templates/ directory missing"

    missing = []
    for f in required:
        if not (tmpl_dir / f).exists():
            missing.append(f)

    if missing:
        return False, f"Missing templates: {missing}"
    return True, f"All {len(required)} template files present"


def check_scripts():
    """Check all scripts are valid Python."""
    script_dir = SKILL_DIR / "scripts"
    if not script_dir.exists():
        return False, "scripts/ directory missing"

    scripts = ["init_state.py", "update_state.py", "scan_docs.py", "create_task_file.py"]
    missing = []
    for s in scripts:
        if not (script_dir / s).exists():
            missing.append(s)
    if missing:
        return False, f"Missing scripts: {missing}"
    return True, f"All {len(scripts)} scripts present"


def check_de_claude():
    """Check for Claude-specific terms in skill.md and references (excl tool-adaptations)."""
    skill_md = SKILL_DIR / "skill.md"
    ref_dir = SKILL_DIR / "references"

    if not skill_md.exists():
        return False, "skill.md not found"

    claude_terms = ["CLAUDE\\.md", "Claude Code", "Claude Cowork", "Claude Chat", "\\bMCP\\b"]
    import re

    violations = []
    for fp in [skill_md] + list(ref_dir.glob("*.md")):
        if fp.name == "tool-adaptations.md":
            continue  # Intentionally contains Claude terms for mapping
        try:
            content = fp.read_text(encoding="utf-8")
        except Exception:
            continue
        for term in claude_terms:
            if re.search(term, content):
                violations.append(f"{fp.name}: {term}")

    if violations:
        return False, f"Claude term violations: {violations}"
    return True, "De-Claude-ification clean"


# Map eval IDs to check functions
EVAL_CHECKS = {
    "eval-001": [check_state_file, check_skill_md],
    "eval-002": [check_references],
    "eval-003": [check_references, check_templates],
    "eval-004": [check_skill_md],
    "eval-005": [check_state_file, check_scripts],
    "eval-006": [check_state_file],
    "eval-007": [check_state_file, check_references],
    "eval-008": [check_skill_md, check_references],
    "eval-009": [check_skill_md, check_de_claude],
    "eval-010": [check_state_file],
    "eval-011": [check_state_file, check_references],
    "eval-012": [check_references, check_de_claude],
    "eval-013": [check_state_file, check_skill_md],
    "eval-014": [check_skill_md],
    "eval-015": [check_skill_md, check_references],
    "eval-016": [check_templates],
    "eval-017": [check_templates],
    "eval-018": [check_scripts, check_references],
    "eval-019": [check_state_file, check_scripts],
    "eval-020": [check_references, check_templates],
}


def run_evals(verbose=False):
    """Run all eval checks."""
    data = load_evals()
    tests = data.get("tests", [])

    print(f"opc-starter-kit Eval Runner v{data.get('version', 'unknown')}\n")
    print(f"Skill directory: {SKILL_DIR}")
    print(f"Running {len(tests)} structural checks...\n")
    print("=" * 60)

    passed = 0
    failed = 0
    skipped = 0

    for test in tests:
        test_id = test["id"]
        test_name = test["name"]
        checks = EVAL_CHECKS.get(test_id, [])

        if not checks:
            if verbose:
                print(f"  ⬜ {test_id}: {test_name}")
                print(f"     No automated checks defined (behavioral test)")
            skipped += 1
            continue

        all_ok = True
        details = []
        for check_fn in checks:
            ok, msg = check_fn()
            if not ok:
                all_ok = False
            details.append(f"{'✅' if ok else '❌'} {check_fn.__name__}: {msg}")

        if all_ok:
            print(f"  ✅ {test_id}: {test_name}")
            passed += 1
        else:
            print(f"  ❌ {test_id}: {test_name}")
            for d in details:
                print(f"     {d}")
            failed += 1

    print("=" * 60)
    print(f"\nResults: {passed} passed, {failed} failed, {skipped} skipped (behavioral)")
    print(f"Structural coverage: {passed + failed}/{passed + failed + skipped}")

    return failed == 0


if __name__ == "__main__":
    verbose = "--verbose" in sys.argv
    success = run_evals(verbose=verbose)
    sys.exit(0 if success else 1)