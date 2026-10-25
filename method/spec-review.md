# Spec review: finding what QA cannot yet test

Goal: find what cannot be turned into an expected result, before development and testing start. The output is an ambiguity log and a short message the product owner can answer.

## Collect first

- The tickets, the PRD, any earlier approved plan, decisions already given, the design file, read-only access to the code.
- Note which design frames you actually opened. Never write "no design" for a frame you did not check.

## Work one ticket at a time

1. **Split compound statements.** One acceptance line becomes one testable fact.
2. **Flag untestable words:** "authorised", "expiring", "appropriate", "where required", "fast", "secure", "large", "etc.". Each needs a number, a list or a rule.
3. **Cross-check in pairs:** ticket vs PRD, ticket vs ticket (frontend vs backend for one feature), ticket vs design, ticket vs earlier decisions, ticket vs code. Contradictions are the most valuable findings.
4. **Check the code before you claim.** If a ticket depends on a queue, a rate limiter, a library or a table, search the repository. Record what exists and what does not.
5. **Walk the standard gaps** for every feature:
   - who may do it (role and scope)
   - what each state looks like (empty, loading, error, expired, duplicate)
   - limits and sizes
   - time zone and dates
   - notifications
   - audit trail
   - personal data: who sees it, how long it is kept
   - a performance target
   - what happens on retry or a change of mind
6. **Definition of Ready.** Design link present, acceptance criteria testable, API agreed, dependencies named. A screen ticket with no design is not ready.
7. **Compare plan versions.** List only tickets whose meaning changed, and quote the changed or dropped line.
8. **Check the schedule.** Release dates vs scope, acceptance windows, environment readiness.

## Classify every finding

- **Blocking:** I cannot write a pass or fail without a decision. This is not a defect.
- **Non-blocking:** I can state an assumption and continue.

Each finding records: an id, the ticket, the source of the conflict (PRD, design, code, other ticket), the exact quote, why it matters, a **suggested default**, and who answers.

## Finding types

| Type | Meaning | Example |
|---|---|---|
| Contradiction | Two documents say different things | PRD: refunds in 14 days. Ticket: 30 days |
| Gap | Nothing says what should happen | No state for an expired link |
| Ambiguity | Wording can be read two ways | "authorised users" |
| Untestable wording | No measurable criterion | "uploads are handled safely" |
| Scope | Ticket adds something the PRD does not have | New field type |
| Dependency | The ticket needs something that does not exist | A queue, a rate limiter |
| Definition of Ready | A process gap | No design link |

## Deliverables

1. The ambiguity log (`templates/ambiguity-log.csv`).
2. A per-ticket view: design link yes or no, ready verdict, number of blocking findings.
3. A message to the product owner (`templates/pm-question-message.md`): grouped by theme, the 10 to 15 questions that block the most testing, each with a plain example and a suggested answer.
4. A heads-up list for engineering on things the tickets assume that do not exist yet.

## After the answers come back

Mark each finding Answered, Partly answered or Open, with who answered and the date. Keep a column "Ticket or design updated?". Until the answer is in the ticket or design and you have re-read it, the expected result in your test case stays "TBD". See `examples/learnloop/` for a worked log.
