# Test plan: [release or sprint name]

Status: draft v0.1, pending decisions. Owner: [name]. Date: [date].

## 1. Scope
- In scope: [features and tickets]
- Out of scope: [what is deliberately not tested, and why]
- Not testable yet: [tickets with open blocking findings, with the finding ids]

## 2. Environments and data
- Environments: [name, URL, how to deploy, how to know which build is running]
- Test accounts per role: [roles, never real people]
- Test data rules: test data only; no real user data; how test records are labelled and removed

## 3. Approach
- Functional (UI and API), negative and boundary cases, permissions by role, accessibility, mobile and browser matrix, performance checks where the ticket sets a target.
- Automation: [what is automated and where it runs]
- Exploratory sessions: [charters, time box]

## 4. Entry criteria
- Ticket has a design link and testable acceptance criteria.
- Feature deployed to the test environment and build identified.
- No open blocking ambiguity for the ticket (or an agreed assumption).

## 5. Exit criteria
- All planned cases executed; no open Critical or High defect without a written risk acceptance.
- Regression suite green on the release candidate.
- Open items listed in the readiness report.

## 6. Risks
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|

## 7. Open questions
Link to the ambiguity log. Expected results that depend on an answer stay "TBD" until the ticket or design changes.

## 8. Reporting
Daily status: executed, passed, failed, blocked. Final: release readiness report with a recommendation (sign-off, conditional sign-off, or not ready). QA recommends; the product owner decides.
