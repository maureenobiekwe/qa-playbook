# Worked example: LearnLoop

LearnLoop is an **invented** online course platform. Everything here is made up to show the method. Nothing comes from a real client.

Release 2 adds instructor invitations, checkout, refunds, discount codes, student CSV import, certificates and notification settings.

## Files

| File | What it is |
|---|---|
| `tickets.md` | 8 invented tickets, with the PRD lines they should match |
| `ambiguity-log.csv` | 14 findings from reviewing them, in the template format |
| `pm-message.md` | The message sent to the product owner, 8 questions |
| `test-plan-excerpt.md` | The part of the test plan that follows, with "TBD" markers |

## What the review found

- 1 contradiction between the PRD and a ticket (refund window)
- 5 gaps where nothing says what should happen
- 3 untestable wordings
- 2 ambiguities ("authorised administrators", the import limit)
- 2 dependencies on things the codebase does not have (a job queue, a stored audit record)
- 1 ticket with no design

Ten of the fourteen are blocking: QA cannot write an expected result until someone decides.
