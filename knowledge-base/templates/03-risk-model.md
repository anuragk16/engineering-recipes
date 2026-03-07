<!--
  PURPOSE: Captures risk classification, fragile areas, and review/testing expectations for {{PROJECT_NAME}}.
  This is a directly maintained Tier 1 file.
  Used by: code-review, implementation-planner, incident-response flows.
-->

# Risk Model: {{PROJECT_NAME}}

## Risk Classification

| Area / Module | Risk Level | Reason | Required Review Gate |
|---------------|------------|--------|----------------------|
| {{MODULE_1}} | High | {{REASON_1}} | {{GATE_1}} |
| {{MODULE_2}} | Medium | {{REASON_2}} | {{GATE_2}} |
| {{MODULE_3}} | Low | {{REASON_3}} | Standard PR review |

## High-Risk Change Triggers
- {{TRIGGER_1}}
- {{TRIGGER_2}}
- {{TRIGGER_3}}

## Required Actions By Risk Level

| Risk Level | Required Actions |
|------------|------------------|
| High | {{HIGH_ACTIONS}} |
| Medium | {{MEDIUM_ACTIONS}} |
| Low | Standard PR review |

## Known Fragile Areas

| Area | Known Issue Pattern | Mitigation |
|------|---------------------|------------|
| {{AREA_1}} | {{PATTERN_1}} | {{MITIGATION_1}} |

## Sensitive Data Rules
- {{DATA_RULE_1}}
- {{DATA_RULE_2}}
