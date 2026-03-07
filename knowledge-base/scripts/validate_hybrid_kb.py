#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

TREE_REQUIRED = [
    "knowledge-base/00-master.md",
    "knowledge-base/01-business-flows/00-index.md",
    "knowledge-base/02-architecture/00-index.md",
    "knowledge-base/03-risk-model/00-index.md",
    "knowledge-base/04-active-sprint/00-index.md",
    "knowledge-base/.kb-config.yml",
]
FLAT_REQUIRED = [
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
TREE_ENTRY_REFS = [
    "01-business-flows/00-index.md",
    "02-architecture/00-index.md",
    "03-risk-model/00-index.md",
    "04-active-sprint/00-index.md",
]
FLAT_ENTRY_REFS = [
    "architecture.md",
    "business-flows.md",
    "active-sprint.md",
    "risks.md",
]


def read_enabled_tier2(config_path: Path) -> list[str]:
    enabled = []
    in_block = False
    for raw in config_path.read_text().splitlines():
        stripped = raw.strip()
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


def detect_layout(root: Path) -> str | None:
    tree_entry = root / "knowledge-base/00-master.md"
    flat_entry = root / "knowledge-base/00-index.md"
    if tree_entry.exists():
        return "tree"
    if flat_entry.exists():
        return "flat"
    return None


def validate_required(root: Path, required: list[str], errors: list[str]) -> None:
    for rel in required:
        if not (root / rel).exists():
            errors.append(f"missing required file: {rel}")


def validate_config(root: Path, errors: list[str]) -> None:
    config_path = root / "knowledge-base/.kb-config.yml"
    if not config_path.exists():
        return
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


def validate_entry(entry: Path, refs: list[str], errors: list[str]) -> None:
    if not entry.exists():
        return
    entry_text = entry.read_text()
    for ref in refs:
        if ref not in entry_text:
            errors.append(f"entry file does not reference: {ref}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a hybrid KB installation")
    parser.add_argument("project_root", help="Path to the target project root")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    errors: list[str] = []
    layout = detect_layout(root)

    if layout == "tree":
        validate_required(root, TREE_REQUIRED, errors)
        validate_entry(root / "knowledge-base/00-master.md", TREE_ENTRY_REFS, errors)
    elif layout == "flat":
        validate_required(root, FLAT_REQUIRED, errors)
        validate_entry(root / "knowledge-base/00-index.md", FLAT_ENTRY_REFS, errors)
    else:
        errors.append("knowledge base entry file not found: expected knowledge-base/00-master.md or knowledge-base/00-index.md")

    validate_config(root, errors)

    if errors:
        print("Hybrid KB validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Hybrid KB validation passed ({layout} layout).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
