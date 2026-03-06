#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = ROOT / "knowledge-base" / "templates"
SCRIPT_ROOT = ROOT / "knowledge-base" / "scripts"
WORKFLOW_ROOT = ROOT / "knowledge-base" / "workflows"
CORE_FILES = [
    "00-index.md",
    "architecture.md",
    "business-flows.md",
    "active-sprint.md",
    "risks.md",
    ".kb-config.yml",
]
ADVANCED_MAP = {
    "decision-log": "advanced/decision-log.md",
    "incident-log": "advanced/incident-log.md",
    "feature-history": "advanced/feature-history.md",
    "integration-map": "advanced/integration-map.md",
    "metrics": "advanced/metrics.md",
    "known-constraints": "advanced/known-constraints.md",
}
CLAUDE_SECTION = TEMPLATES / "CLAUDE.section.md"
SUPPORT_SCRIPTS = [
    "validate_hybrid_kb.py",
    "sync_active_sprint.py",
]


def copy_file(src: Path, dest: Path, overwrite: bool) -> str:
    if dest.exists() and not overwrite:
        return f"skip {dest}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return f"write {dest}"


def ensure_claude_section(project_root: Path) -> str:
    claude_path = project_root / "CLAUDE.md"
    section = CLAUDE_SECTION.read_text()
    if claude_path.exists():
        existing = claude_path.read_text()
        if "## Knowledge Base" in existing:
            return f"skip {claude_path}"
        claude_path.write_text(existing.rstrip() + "\n\n" + section)
        return f"append {claude_path}"
    claude_path.write_text(section)
    return f"create {claude_path}"


def configure_kb_config(config_path: Path, enabled: list[str]) -> str:
    lines = config_path.read_text().splitlines()
    new_lines = []
    in_block = False
    inserted = False
    for line in lines:
        stripped = line.strip()
        if stripped == "enabled_tier2:":
            in_block = True
            inserted = True
            new_lines.append("enabled_tier2:")
            if enabled:
                for module in enabled:
                    new_lines.append(f"  - {module}")
            else:
                new_lines.append("  # Add optional module keys here when enabled for the project.")
            continue
        if in_block:
            if stripped.startswith("-") or stripped.startswith("#"):
                continue
            if stripped and not line.startswith(" "):
                in_block = False
        if not in_block:
            new_lines.append(line)
    if not inserted:
        raise ValueError(f"enabled_tier2 block not found in {config_path}")
    config_path.write_text("\n".join(new_lines) + "\n")
    return f"configure {config_path}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold the hybrid knowledge base into a target project")
    parser.add_argument("project_root", help="Path to the target project root")
    parser.add_argument(
        "--enable",
        default="",
        help="Comma-separated Tier 2 modules to enable (decision-log,incident-log,feature-history,integration-map,metrics,known-constraints)",
    )
    parser.add_argument(
        "--with-workflow",
        action="store_true",
        help="Install the example sprint sync workflow into .github/workflows/",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing KB files")
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    if not project_root.exists():
        print(f"error: project root not found: {project_root}", file=sys.stderr)
        return 1

    kb_root = project_root / "knowledge-base"
    kb_root.mkdir(exist_ok=True)

    enabled = [item.strip() for item in args.enable.split(",") if item.strip()]
    unknown = [item for item in enabled if item not in ADVANCED_MAP]
    if unknown:
        print(f"error: unknown Tier 2 modules: {', '.join(unknown)}", file=sys.stderr)
        return 1

    actions = []
    for rel in CORE_FILES:
        actions.append(copy_file(TEMPLATES / rel, kb_root / rel, args.overwrite))

    for module in enabled:
        rel = ADVANCED_MAP[module]
        actions.append(copy_file(TEMPLATES / rel, kb_root / rel, args.overwrite))

    for script_name in SUPPORT_SCRIPTS:
        actions.append(
            copy_file(
                SCRIPT_ROOT / script_name,
                kb_root / "scripts" / script_name,
                args.overwrite,
            )
        )

    if args.with_workflow:
        actions.append(
            copy_file(
                WORKFLOW_ROOT / "sync-active-sprint.yml",
                project_root / ".github" / "workflows" / "sync-active-sprint.yml",
                args.overwrite,
            )
        )

    actions.append(configure_kb_config(kb_root / ".kb-config.yml", enabled))
    actions.append(ensure_claude_section(project_root))

    print("Hybrid KB scaffold summary:")
    for action in actions:
        print(f"- {action}")
    if enabled:
        print(f"- enabled Tier 2: {', '.join(enabled)}")
    else:
        print("- enabled Tier 2: none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
