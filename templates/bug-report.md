# Bug report template

**Title:** [Area] short description of the wrong behaviour (not the cause)

| Field | Content |
|---|---|
| ID | BUG-001 |
| Severity | Critical / High / Medium / Low (see severity-guide.md) |
| Build / environment | Environment, build or commit, date and time |
| Role / account | Which test role |
| Related ticket / test case | LL-xxx, TC-xxx |

**Steps to reproduce**
1. ...
2. ...

**Expected result:** what the ticket or decision says should happen (quote it).

**Actual result:** what happened, with the exact message or status code.

**Evidence:** screenshot, request and response (remove tokens and personal data), console error.

**Reproducibility:** always / sometimes (how often) / once.

**Notes:** workaround, related findings, whether it is a regression.

## Rules
- Separate a defect from a gap. If the expected result is not written anywhere, log an ambiguity, not a bug.
- One defect per report.
- Never paste a real token, password or personal data. Refer to the file and line, not the secret.
- A security issue goes to the product owner privately, not into a shared ticket.
- A fix is closed only after QA re-tests it on the build that contains it.
