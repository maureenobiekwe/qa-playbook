# QA Playbook

How I approach QA on a product before and during testing: reading specs for gaps, writing a plan the team can agree to, logging defects clearly, and keeping a project's context consistent over weeks.

Everything here is method and templates. The worked example uses an invented product (LearnLoop, an online course platform). No real client, ticket or data appears in this repository.

## What is in it

| Folder | What it gives you |
|---|---|
| `method/` | How I review tickets against a PRD, designs and the code, and how I classify what I find |
| `templates/` | Ambiguity log, test plan, test case, bug report, severity guide, the message I send a product owner |
| `checklists/` | Risk prompts for roles and permissions, imports, dates and time zones, public forms, PWA |
| `examples/learnloop/` | A full worked example: 8 invented tickets, the findings, and the question message |
| `process/` | How I keep project context across sessions, with generic hook scripts |

Start with `method/spec-review.md`, then read `examples/learnloop/` to see it applied.

## Ideas that run through all of it

- **A gap is not a bug.** If the documents disagree or are silent, QA cannot write an expected result. That is a question for the product owner, logged as an ambiguity, not a defect.
- **Verify before you believe.** A ticket that assumes a queue, a rate limit or an audit table gets checked against the code. Say what exists and what does not.
- **Every question comes with a suggested answer,** so the reply can be "yes" or "no, do X".
- **A verbal answer is not final** until the ticket or design changes and QA re-reads it. Expected results stay "TBD" until then.
- **Say what you did not check.** Counts in a summary must match the log.

## Companion repository

`qa-automation-framework`: Playwright and pytest UI and API tests, accessibility checks, a Newman API regression job in CI, and performance notes.
