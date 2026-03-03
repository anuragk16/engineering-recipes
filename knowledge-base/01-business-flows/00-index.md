<!--
  PURPOSE: Index of all business processes and user journeys for {{PROJECT_NAME}}.
  This is a REFERENCE TABLE ONLY. Flow details live in individual files in this directory.
  Used by: business-analyst agent.

  CONTENT RULE:
  - This file contains ONLY the index table below — never flow details or steps.
  - Each business flow gets its own file named `bf-XX-<flow-name>.md` in this directory.
  - When adding a new flow: create the individual file first, then add one row here.

  WHAT BELONGS HERE:
  - A row per flow: ID, name, primary user/initiator, expected outcome, link to the flow file

  WHAT DOES NOT BELONG HERE:
  - Flow steps, business rules, edge cases, or any narrative content
  - Those belong in the individual flow files
-->

# Business Flows: {{PROJECT_NAME}}

**Domain:** {{BUSINESS_DOMAIN}}
**Primary Users:** {{PRIMARY_USER_ROLES}}

---

## Flow Index

| Flow ID | Flow Name | Initiator | Outcome | File |
|---------|-----------|-----------|---------|------|
| BF-01 | {{FLOW_NAME_1}} | {{INITIATOR_1}} | {{OUTCOME_1}} | [bf-01-{{flow-slug-1}}.md](bf-01-{{flow-slug-1}}.md) |
| BF-02 | {{FLOW_NAME_2}} | {{INITIATOR_2}} | {{OUTCOME_2}} | [bf-02-{{flow-slug-2}}.md](bf-02-{{flow-slug-2}}.md) |

<!-- TODO: Add a row for each business flow. Create the individual .md file first, then link it here. -->

---

<!--
  EXAMPLE (delete this block once real flows are added):

  | Flow ID | Flow Name        | Initiator | Outcome                                     | File                             |
  |---------|------------------|-----------|---------------------------------------------|----------------------------------|
  | BF-01   | Leave Approval   | Employee  | Leave approved/rejected; employee notified  | [bf-01-leave-approval.md](bf-01-leave-approval.md) |
  | BF-02   | Expense Claim    | Employee  | Claim reimbursed or rejected within 5 days  | [bf-02-expense-claim.md](bf-02-expense-claim.md)   |
  | BF-03   | Employee Onboard | HR Admin  | New hire fully set up in all systems        | [bf-03-employee-onboard.md](bf-03-employee-onboard.md) |
-->
