<!--
  PURPOSE: Documents the architectural patterns, tech stack, and structural rules for {{PROJECT_NAME}}.
  Agents use this section to understand how the codebase is organized, what patterns to follow,
  and what constraints must be respected when making changes.
  Used by: implementation-planner, implementation-executor agents.

  WHAT BELONGS HERE:
  - Tech stack with versions
  - Directory structure and layer responsibilities
  - Established patterns (naming, file organization, state management, API design)
  - Integration points with external systems
  - Rules that must not be violated (e.g., "never put business logic in controllers")

  WHAT DOES NOT BELONG HERE:
  - Sprint tasks or issue tracking (→ 04-active-sprint)
  - Business rules or user flows (→ 01-business-flows)
  - Risk assessments (→ 03-risk-model)
-->

# Architecture: {{PROJECT_NAME}}

---

## Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| {{LAYER_1}} | {{TECH_1}} | {{VERSION_1}} |
| {{LAYER_2}} | {{TECH_2}} | {{VERSION_2}} |
| {{LAYER_3}} | {{TECH_3}} | {{VERSION_3}} |

<!-- TODO: Fill in all layers (frontend, backend, database, cache, queue, infra, etc.). -->

---

## Directory Structure

```
{{PROJECT_ROOT}}/
├── {{DIR_1}}/          # {{DIR_1_PURPOSE}}
├── {{DIR_2}}/          # {{DIR_2_PURPOSE}}
└── {{DIR_3}}/          # {{DIR_3_PURPOSE}}
```

<!-- TODO: Replace with actual directory layout and a one-line purpose for each top-level folder. -->

---

## Established Patterns

### Naming Conventions
- {{NAMING_RULE_1}}
- {{NAMING_RULE_2}}

### File Organization Rules
- {{FILE_ORG_RULE_1}}
- {{FILE_ORG_RULE_2}}

### API Design Rules
- {{API_RULE_1}}
- {{API_RULE_2}}

<!-- TODO: Fill in conventions observed in the codebase. -->

---

## Layer Responsibilities

| Layer | Responsibility | Must NOT Contain |
|-------|---------------|-----------------|
| {{LAYER_A}} | {{RESPONSIBILITY_A}} | {{FORBIDDEN_A}} |
| {{LAYER_B}} | {{RESPONSIBILITY_B}} | {{FORBIDDEN_B}} |

<!-- TODO: Define each architectural layer and its boundaries. -->

---

## External Integrations

| System | Purpose | Auth Method |
|--------|---------|-------------|
| {{EXT_SYSTEM_1}} | {{PURPOSE_1}} | {{AUTH_1}} |

<!-- TODO: List all third-party services and APIs this project integrates with. -->

---

## Architectural Rules (Non-Negotiable)

- {{ARCH_RULE_1}}
- {{ARCH_RULE_2}}

<!-- TODO: Document rules that must never be violated (e.g., no direct DB calls from API routes). -->

---

<!--
  EXAMPLE (delete this block once real architecture is documented):

  ## Tech Stack

  | Layer | Technology | Version |
  |-------|-----------|---------|
  | Frontend | Next.js | 14.x |
  | Backend | Laravel | 11.x |
  | Database | PostgreSQL | 15 |
  | Cache | Redis | 7.x |
  | File Storage | AWS S3 | — |

  ## Established Patterns

  ### Naming Conventions
  - React components: PascalCase in `components/` (e.g., `LeaveRequestCard.tsx`)
  - Laravel controllers: singular, suffix `Controller` (e.g., `LeaveRequestController.php`)
  - Database tables: snake_case plural (e.g., `leave_requests`)

  ### Layer Responsibilities

  | Layer | Responsibility | Must NOT Contain |
  |-------|---------------|-----------------|
  | Controllers | Receive HTTP request, delegate to service, return response | Business logic |
  | Services | Business logic and orchestration | Direct DB queries |
  | Repositories | All database access | Business logic |

  ## Architectural Rules (Non-Negotiable)
  - Business logic lives in Service classes only — never in controllers or models
  - All external API calls are wrapped in dedicated client classes under `app/Http/Clients/`
  - Frontend never calls the database directly — always through the backend API
-->
