<!--
  PURPOSE: Documents the core business processes and user journeys for {{PROJECT_NAME}}.
  Captures what the system does from a business perspective — not how it is built.
  Used by: business-analyst agent.

  WHAT BELONGS HERE:
  - Named business flows (login, checkout, approval, etc.)
  - Who initiates each flow and what the expected outcome is
  - Key decision points and branching conditions
  - Business rules embedded in each flow

  WHAT DOES NOT BELONG HERE:
  - Technical implementation details (API endpoints, DB schema, code paths)
  - Deployment or infrastructure concerns
-->

# Business Flows: {{PROJECT_NAME}}

**Domain:** {{BUSINESS_DOMAIN}}
**Primary Users:** {{PRIMARY_USER_ROLES}}

---

## Flow Index

| Flow ID | Flow Name | Initiator | Outcome |
|---------|-----------|-----------|---------|
| BF-01 | {{FLOW_NAME_1}} | {{INITIATOR_1}} | {{OUTCOME_1}} |
| BF-02 | {{FLOW_NAME_2}} | {{INITIATOR_2}} | {{OUTCOME_2}} |

<!-- TODO: Add all primary business flows for this project. -->

---

## Flow Details

### BF-01: {{FLOW_NAME_1}}

**Initiator:** {{INITIATOR_1}}
**Trigger:** {{TRIGGER_CONDITION_1}}
**Expected Outcome:** {{OUTCOME_1}}

**Steps:**
1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}

**Business Rules:**
- {{BUSINESS_RULE_1}}
- {{BUSINESS_RULE_2}}

**Edge Cases / Exceptions:**
- {{EDGE_CASE_1}}

---

<!-- TODO: Add detail sections for each flow listed in the index above. -->

---

<!--
  EXAMPLE (delete this block once real flows are added):

  ### BF-01: Leave Approval

  **Initiator:** Employee
  **Trigger:** Employee submits a leave request via the HR portal
  **Expected Outcome:** Leave is approved or rejected; employee is notified by email

  **Steps:**
  1. Employee selects leave type, date range, and reason
  2. System checks available leave balance
  3. Request is routed to employee's direct manager for approval
  4. Manager approves or rejects with an optional note
  5. Employee receives an email notification with the decision

  **Business Rules:**
  - Employees cannot apply for leave less than 24 hours in advance (except emergency leave)
  - Leave balance must cover the requested days at time of submission
  - Requests exceeding 10 days require HR secondary approval

  **Edge Cases / Exceptions:**
  - If manager is on leave, the request escalates to the skip-level manager after 48 hours
  - Emergency leave bypasses the balance check but still requires approval
-->
