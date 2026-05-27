#!/usr/bin/env python3
"""Scan the docs/ directory to infer the current project stage.

Usage:
    python scan_docs.py

When .opc-state.json is missing or corrupted, this script scans the docs/
directory for stage artifacts to infer which stage the project is in.

Inference logic:
    - If docs/ is empty or doesn't exist → "idea" (new project)
    - Based on the latest completion report found:
      stage-4 → "scale"
      stage-3 → "launch"
      stage-2 → "mvp"
      stage-1 → "idea"
    - If partial artifacts exist (e.g., problem-statement.md but no completion report):
      infer the stage based on which artifacts are present

Output: prints the inferred stage name and confidence level.
"""

import os
import sys
from pathlib import Path


DOCS_DIR = "docs"

# Mapping of artifact files to their stages
STAGE_ARTIFACTS = {
    "idea": [
        "problem-statement.md",
        "competitive-map.md",
        "interview-guide.md",
        "problem-hypothesis.md",
        "stage-1-completion-report.md",
    ],
    "mvp": [
        "architecture-context.md",
        "scope-doc.md",
        "metrics-framework.md",
        "pmf-assessment.md",
        "stage-2-completion-report.md",
    ],
    "launch": [
        "tech-debt-audit.md",
        "bottleneck-audit.md",
        "pm-process.md",
        "stage-3-completion-report.md",
    ],
    "scale": [
        "domain-knowledge.md",
        "workflow-audit.md",
        "moat-narrative.md",
        "moat-scorecard.md",
        "stage-4-completion-report.md",
    ],
}

COMPLETION_REPORTS = {
    "stage-4-completion-report.md": "scale",
    "stage-3-completion-report.md": "launch",
    "stage-2-completion-report.md": "mvp",
    "stage-1-completion-report.md": "idea",
}

STAGE_ORDER = ["idea", "mvp", "launch", "scale"]


def scan_docs():
    """Scan docs/ and infer the current stage."""
    if not os.path.isdir(DOCS_DIR):
        print("stage: idea")
        print("confidence: low")
        print("reason: docs/ directory does not exist — treating as new project")
        return "idea", "low", "docs/ directory does not exist"

    existing_files = set(os.listdir(DOCS_DIR))

    if not existing_files:
        print("stage: idea")
        print("confidence: low")
        print("reason: docs/ directory is empty — treating as new project")
        return "idea", "low", "docs/ directory is empty"

    # Check for completion reports (highest confidence)
    for report, stage in COMPLETION_REPORTS.items():
        if report in existing_files:
            print(f"stage: {stage}")
            print("confidence: high")
            print(f"reason: found completion report {report}")
            return stage, "high", f"found completion report {report}"

    # No completion reports — count artifacts per stage
    stage_scores = {}
    for stage, artifacts in STAGE_ARTIFACTS.items():
        # Exclude completion reports from artifact counting
        non_report_artifacts = [a for a in artifacts if "completion-report" not in a]
        found = [a for a in non_report_artifacts if a in existing_files]
        stage_scores[stage] = len(found)

    # Find the highest stage with any artifacts, going in reverse order
    best_stage = "idea"
    best_score = 0
    for stage in reversed(STAGE_ORDER):
        if stage_scores[stage] > 0:
            best_stage = stage
            best_score = stage_scores[stage]
            break

    print(f"stage: {best_stage}")
    print(f"confidence: medium")
    print(f"reason: found {best_score} artifact(s) matching stage '{best_stage}', no completion reports found")

    # Print summary of what was found and what's missing
    print("\n--- Artifact Summary ---")
    for stage in STAGE_ORDER:
        artifacts = STAGE_ARTIFACTS[stage]
        found = [a for a in artifacts if a in existing_files]
        missing = [a for a in artifacts if a not in existing_files]
        print(f"\n{stage} stage:")
        for f in found:
            print(f"  ✅ {f}")
        for m in missing:
            print(f"  ⬜ {m}")

    return best_stage, "medium", f"found {best_score} artifact(s) matching stage '{best_stage}'"


if __name__ == "__main__":
    scan_docs()