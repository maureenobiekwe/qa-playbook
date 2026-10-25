# Test case template

| Field | Content |
|---|---|
| ID | TC-001 |
| Title | One behaviour, written as "X does Y when Z" |
| Ticket / requirement | Ticket id and acceptance line |
| Priority | High / Medium / Low |
| Type | Functional / Negative / Boundary / Permission / Accessibility |
| Preconditions | Role, data, state |
| Steps | 1. ... 2. ... 3. ... |
| Expected result | Exact and checkable: status code, text, state. **TBD (AMB-xxx)** while a decision is open |
| Actual result | Filled in at run time |
| Status | Not run / Pass / Fail / Blocked / Deferred |
| Evidence | Screenshot, response, run link |
| Defect | Bug id if failed |

## Writing rules
- One behaviour per case. If the title has "and", split it.
- Exact status codes. Never "any 2xx".
- Include the negative case next to the happy path (wrong role, missing field, expired link).
- Each case traces to a ticket line. A case with no ticket is either a gap in the ticket or out of scope: say which.

## Example

| Field | Content |
|---|---|
| ID | TC-014 |
| Title | An expired invitation link shows the "link expired" page |
| Ticket | LL-101, acceptance line 4 |
| Preconditions | Invitation created, then aged beyond its lifetime (needs a way to age a token in QA) |
| Steps | 1. Open the invitation link. |
| Expected result | The "link expired" page with a way to request a new link. No account is created. |
| Status | Not run |
