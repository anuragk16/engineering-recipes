#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REQUIRED_FILES = [
    "knowledge-base/00-index.md",
    "knowledge-base/architecture.md",
    "knowledge-base/business-flows.md",
    "knowledge-base/active-sprint.md",
    "knowledge-base/risks.md",
    "knowledge-base/.kb-config.yml",
]
OPTIONAL_BY_KEY = {
    "decision-log": "knowledge-base/advanced/decision-log.md",
    "incident-log": "knowledge-base/advanced/incident-log.md",
    "feature-history": "knowledge-base/advanced/feature-history.md",
    "integration-map": "knowledge-base/advanced/integration-map.md",
    "metrics": "knowledge-base/advanced/metrics.md",
    "known-constraints": "knowledge-base/advanced/known-constraints.md",
}


def read_enabled_tier2(config_path: Path) -> list[str]:
    enabled = []
    in_block = False
    for raw in config_path.read_text().splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if stripped == "enabled_tier2:":
            in_block = True
            continue
        if in_block:
            if stripped.startswith("-"):
                enabled.append(stripped[1:].strip())
                continue
            if stripped and not raw.startswith(" "):
                break
    return enabled


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a hybrid KB installation")
    parser.add_argument("project_root", help="Path to the target project root")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    errors = []

    for rel in REQUIRED_FILES:
        path = root / rel
        if not path.exists():
            errors.append(f"missing required file: {rel}")

    config_path = root / "knowledge-base/.kb-config.yml"
    if config_path.exists():
        contents = config_path.read_text()
        for key in ["version:", "source_of_truth:", "loading_defaults:"]:
            if key not in contents:
                errors.append(f"missing config key: {key.rstrip(':')}")
        for module in read_enabled_tier2(config_path):
            rel = OPTIONAL_BY_KEY.get(module)
            if rel is None:
                errors.append(f"unknown enabled Tier 2 module in config: {module}")
            elif not (root / rel).exists():
                errors.append(f"enabled Tier 2 file missing: {rel}")

    entry = root / "knowledge-base/00-index.md"
    if entry.exists():
        entry_text = entry.read_text()
        for ref in ["architecture.md", "business-flows.md", "active-sprint.md", "risks.md"]:
            if ref not in entry_text:
                errors.append(f"entry file does not reference: {ref}")

    if errors:
        print("Hybrid KB validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Hybrid KB validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
