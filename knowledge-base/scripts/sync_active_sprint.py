#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ACTIVE_START = "<!-- AUTO-GENERATED:ACTIVE_ITEMS:START -->"
ACTIVE_END = "<!-- AUTO-GENERATED:ACTIVE_ITEMS:END -->"
BLOCKERS_START = "<!-- AUTO-GENERATED:BLOCKERS:START -->"
BLOCKERS_END = "<!-- AUTO-GENERATED:BLOCKERS:END -->"
DONE_START = "<!-- AUTO-GENERATED:RECENTLY_COMPLETED:START -->"
DONE_END = "<!-- AUTO-GENERATED:RECENTLY_COMPLETED:END -->"


@dataclass
class IssueRow:
    number: int
    title: str
    status: str
    assignee: str
    note: str


@dataclass
class DoneRow:
    ref: str
    title: str
    completed_on: str


def run_gh(args: list[str]) -> list[dict]:
    result = subprocess.run(["gh", *args], check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def detect_status(issue: dict) -> str:
    if issue.get("state") == "CLOSED":
        return "Done"
    labels = {label["name"].lower() for label in issue.get("labels", [])}
    if any(label in labels for label in {"in review", "review", "needs review"}):
        return "In Review"
    if issue.get("assignees") or any(label in labels for label in {"in progress", "doing", "wip"}):
        return "In Progress"
    return "Backlog"


def replace_section(text: str, start: str, end: str, body: str) -> str:
    if start not in text or end not in text:
        raise ValueError(f"markers not found: {start} / {end}")
    prefix, rest = text.split(start, 1)
    _, suffix = rest.split(end, 1)
    return prefix + start + "\n" + body.rstrip() + "\n" + end + suffix


def render_active(rows: list[IssueRow]) -> str:
    lines = ["| Issue | Title | Status | Assignee | Note |", "|---|---|---|---|---|"]
    for row in rows:
        lines.append(f"| #{row.number} | {row.title} | {row.status} | {row.assignee} | {row.note} |")
    return "\n".join(lines)


def render_blockers(rows: list[IssueRow]) -> str:
    lines = ["| Issue | Blocker | Owner |", "|---|---|---|"]
    for row in rows:
        lines.append(f"| #{row.number} | {row.note or 'Label / blocker details missing'} | {row.assignee} |")
    return "\n".join(lines)


def render_done(rows: list[DoneRow]) -> str:
    lines = ["| Issue / PR | Title | Completed On |", "|---|---|---|"]
    for row in rows:
        lines.append(f"| {row.ref} | {row.title} | {row.completed_on} |")
    return "\n".join(lines)


def choose_sprint_file(project_root: Path) -> Path:
    canonical = project_root / "knowledge-base/active-sprint.md"
    legacy = project_root / "knowledge-base/04-active-sprint/00-index.md"
    if canonical.exists():
        return canonical
    if legacy.exists():
        return legacy
    raise FileNotFoundError("No sprint file found in canonical or legacy location")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync the active sprint file from GitHub issues")
    parser.add_argument("project_root", help="Path to the target project root")
    parser.add_argument("--repo", required=True, help="GitHub repository in owner/name format")
    parser.add_argument("--open-limit", type=int, default=30)
    parser.add_argument("--closed-limit", type=int, default=10)
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    sprint_file = choose_sprint_file(project_root)

    open_issues = run_gh([
        "issue", "list",
        "--repo", args.repo,
        "--state", "open",
        "--limit", str(args.open_limit),
        "--json", "number,title,labels,assignees,state",
    ])
    closed_issues = run_gh([
        "issue", "list",
        "--repo", args.repo,
        "--state", "closed",
        "--limit", str(args.closed_limit),
        "--json", "number,title,closedAt",
    ])

    active_rows = []
    blocker_rows = []
    for issue in open_issues:
        status = detect_status(issue)
        assignees = issue.get("assignees", [])
        assignee = ", ".join(person["login"] for person in assignees) if assignees else "—"
        labels = {label["name"].lower() for label in issue.get("labels", [])}
        note = ""
        if "blocked" in labels or "on hold" in labels:
            note = "Blocked / on hold"
            blocker_rows.append(IssueRow(issue["number"], issue["title"], status, assignee, note))
        active_rows.append(IssueRow(issue["number"], issue["title"], status, assignee, note or "—"))

    done_rows = [DoneRow(f"#{issue['number']}", issue["title"], issue.get("closedAt", "")[:10] or "—") for issue in closed_issues]

    text = sprint_file.read_text()
    text = replace_section(text, ACTIVE_START, ACTIVE_END, render_active(active_rows))
    text = replace_section(text, BLOCKERS_START, BLOCKERS_END, render_blockers(blocker_rows))
    text = replace_section(text, DONE_START, DONE_END, render_done(done_rows))
    sprint_file.write_text(text)

    print(f"updated {sprint_file}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(exc.stderr or str(exc), file=sys.stderr)
        raise SystemExit(exc.returncode)
