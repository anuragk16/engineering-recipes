# Architecture: {{PROJECT_NAME}}

## Purpose
Capture the current architectural shape in a compact, implementation-facing format.

## Brevity Rules
- Target: under 250 lines
- Prefer tables and short bullets
- Do not paste full schemas or long narratives

## Stack Summary
| Layer | Technology | Notes |
|---|---|---|
| Frontend | {{FRONTEND_TECH}} | {{FRONTEND_NOTES}} |
| Backend | {{BACKEND_TECH}} | {{BACKEND_NOTES}} |
| Data | {{DATA_TECH}} | {{DATA_NOTES}} |
| Infra / Runtime | {{INFRA_TECH}} | {{INFRA_NOTES}} |

## Module Map
| Module / Directory | Responsibility | Must Not Contain |
|---|---|---|
| {{MODULE_1}} | {{RESPONSIBILITY_1}} | {{FORBIDDEN_1}} |
| {{MODULE_2}} | {{RESPONSIBILITY_2}} | {{FORBIDDEN_2}} |
| {{MODULE_3}} | {{RESPONSIBILITY_3}} | {{FORBIDDEN_3}} |

## Integration Points
| System | Purpose | Auth / Trust Boundary |
|---|---|---|
| {{INTEGRATION_1}} | {{PURPOSE_1}} | {{AUTH_1}} |

## Non-Negotiable Rules
- {{ARCH_RULE_1}}
- {{ARCH_RULE_2}}
- {{ARCH_RULE_3}}

## Example Entry Style
- Good: "Business logic lives in services; controllers stay thin."
- Bad: multi-paragraph history of why services exist.
