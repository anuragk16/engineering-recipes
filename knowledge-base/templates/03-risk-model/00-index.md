<!--
  PURPOSE: Classifies areas of the codebase by risk level and documents the rules agents
  must apply when making changes. Ensures high-risk areas receive appropriate caution,
  review gates, and testing coverage.
  Used by: code-reviewer agent.

  WHAT BELONGS HERE:
  - Risk classification of modules/areas (High / Medium / Low)
  - Rules for what constitutes a high-risk change
  - Mandatory review or testing requirements per risk level
  - Known fragile areas or historical incident patterns

  WHAT DOES NOT BELONG HERE:
  - Business process descriptions (→ 01-business-flows)
  - Architecture patterns (→ 02-architecture)
  - Sprint tasks (→ 04-active-sprint)
-->

# Risk Model: {{PROJECT_NAME}}

---

## Risk Classification

| Area / Module | Risk Level | Reason | Required Review Gate |
|---------------|-----------|--------|---------------------|
| {{MODULE_1}} | High | {{REASON_1}} | {{GATE_1}} |
| {{MODULE_2}} | Medium | {{REASON_2}} | {{GATE_2}} |
| {{MODULE_3}} | Low | {{REASON_3}} | None |

<!-- TODO: Classify all major modules or functional areas by risk level. -->

---

## What Makes a Change High-Risk

A change is classified as **High Risk** if it meets any of the following conditions:

- {{HIGH_RISK_CONDITION_1}}
- {{HIGH_RISK_CONDITION_2}}
- {{HIGH_RISK_CONDITION_3}}

<!-- TODO: Define the project-specific conditions that elevate a change to high risk. -->

---

## Required Actions by Risk Level

| Risk Level | Required Actions |
|-----------|-----------------|
| High | {{HIGH_REQUIRED_ACTIONS}} |
| Medium | {{MEDIUM_REQUIRED_ACTIONS}} |
| Low | Standard PR review |

<!-- TODO: Define what must happen before a high- or medium-risk change is merged. -->

---

## Known Fragile Areas

Areas with a history of regressions or incidents that require extra care:

| Area | Known Issue Pattern | Mitigation |
|------|--------------------|-----------|
| {{FRAGILE_AREA_1}} | {{ISSUE_PATTERN_1}} | {{MITIGATION_1}} |

<!-- TODO: Document any areas that have caused incidents in the past. -->

---

## Sensitive Data Handling Rules

- {{SENSITIVE_DATA_RULE_1}}
- {{SENSITIVE_DATA_RULE_2}}

<!-- TODO: List rules around PII, financial data, auth tokens, or any sensitive data this project handles. -->

---

<!--
  EXAMPLE (delete this block once real risk data is documented):

  ## Risk Classification

  | Area / Module | Risk Level | Reason | Required Review Gate |
  |---------------|-----------|--------|---------------------|
  | Payment processing | High | Handles financial transactions; PCI scope | Senior dev review + QA sign-off |
  | Authentication / session management | High | Security surface; affects all users | Security review |
  | Leave balance calculation | Medium | Business-critical logic with edge cases | Unit test coverage required |
  | UI component library | Low | Isolated; no data mutations | Standard PR review |

  ## What Makes a Change High-Risk

  - Touches payment, billing, or subscription logic
  - Modifies authentication, authorization, or session handling
  - Changes database migrations on tables with > 100k rows
  - Modifies shared utility functions used across 5+ modules

  ## Known Fragile Areas

  | Area | Known Issue Pattern | Mitigation |
  |------|--------------------|-----------|
  | Leave balance rollover | Off-by-one errors at fiscal year boundary | Always add a boundary test case covering Dec 31 → Jan 1 |
  | Email notification queue | Duplicate sends during retry storms | Check idempotency key before enqueueing |
-->
