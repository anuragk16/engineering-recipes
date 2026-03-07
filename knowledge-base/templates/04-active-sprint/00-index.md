<!--
  PURPOSE: Tracks the current sprint goal, active issues, and their progress.
  Provides agents with just-in-time context about what is being worked on right now,
  so they can prioritize, avoid conflicts, and surface relevant considerations.
  Used by: implementation-planner, knowledge-base-manager agents.

  WHAT BELONGS HERE:
  - Sprint goal (one sentence)
  - Active issues: ID, title, assignee, status, and brief progress note
  - Blocked items and their blockers
  - Recently completed items (current sprint only)

  WHAT DOES NOT BELONG HERE:
  - Backlog items not yet committed to this sprint
  - Architecture decisions (→ 02-architecture)
  - Risk notes (→ 03-risk-model)

  UPDATE CADENCE: This file is updated by the knowledge-base-manager agent.
  Do not edit manually unless the agent is unavailable.
-->

# Active Sprint: {{PROJECT_NAME}}

**Sprint:** {{SPRINT_NAME_OR_NUMBER}}
**Sprint Goal:** {{SPRINT_GOAL}}
**Period:** {{SPRINT_START_DATE}} → {{SPRINT_END_DATE}}

---

## Active Issues

| Issue | Title | Assignee | Status | Notes |
|-------|-------|----------|--------|-------|
| #{{ISSUE_NUMBER_1}} | {{ISSUE_TITLE_1}} | {{ASSIGNEE_1}} | {{STATUS_1}} | {{PROGRESS_NOTE_1}} |
| #{{ISSUE_NUMBER_2}} | {{ISSUE_TITLE_2}} | {{ASSIGNEE_2}} | {{STATUS_2}} | {{PROGRESS_NOTE_2}} |

<!-- TODO: Populate with issues from the current sprint. Use knowledge-base-manager agent to sync. -->

---

## Blocked Items

| Issue | Blocker | Owner |
|-------|---------|-------|
| #{{BLOCKED_ISSUE}} | {{BLOCKER_DESCRIPTION}} | {{BLOCKER_OWNER}} |

<!-- TODO: List any issues currently blocked and what is blocking them. -->

---

## Completed This Sprint

| Issue | Title | Completed On |
|-------|-------|-------------|
| #{{DONE_ISSUE_1}} | {{DONE_TITLE_1}} | {{DONE_DATE_1}} |

<!-- TODO: Move issues here once closed/merged. -->

---

<!--
  EXAMPLE (delete this block once real sprint data is populated):

  ## Active Issues

  | Issue | Title | Assignee | Status | Notes |
  |-------|-------|----------|--------|-------|
  | #42 | Add leave approval email notifications | @sarah | In Progress | Backend done; frontend wiring pending |
  | #45 | Fix leave balance rollover bug | @james | In Review | PR #88 open; awaiting code review |
  | #47 | Export leave report to CSV | @priya | Backlog | Scheduled for this sprint; not started |

  ## Blocked Items

  | Issue | Blocker | Owner |
  |-------|---------|-------|
  | #43 | Waiting on design mockups from UX team | @design-team |

  ## Completed This Sprint

  | Issue | Title | Completed On |
  |-------|-------|-------------|
  | #39 | Implement leave request form validation | 2026-02-24 |
  | #41 | Add manager dashboard leave overview | 2026-02-25 |
-->
