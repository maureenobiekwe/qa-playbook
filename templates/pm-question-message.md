# Message to the product owner: template

**Subject:** [Sprint or release]: [N] decisions I need before I can write test cases

Hi [name],

I read all [N] tickets line by line against the PRD, your earlier decisions, the designs and the code. **Nothing here is a bug.** These are places where the documents disagree, or where no document says what should happen, so I cannot write an expected result. The full log ([M] items) is here: [link]. These are the [10 to 15] that block the most testing. Each has a suggested answer, so a "yes" or "no, do X" is enough.

## A. The documents disagree
**1. [Short question]**
- Document A says: "[quote]"
- Document B says: "[quote]"
- *Why it matters:* [what I cannot test]
- *Suggested:* [my proposed answer]

## B. Access and security
...

## C. Rules I need written down
...

## D. Design and email
...

**Heads-up for engineering and DevOps:** the tickets assume things that do not exist in the code yet: [list, each checked].

Thanks. If a call is easier, I can go through the full list in 30 minutes.

[name]

---

## Rules for writing it
- 10 to 15 questions, ordered by how much testing each blocks.
- Group by theme, not by ticket.
- Every question has a plain example and a suggested answer.
- Say clearly it is not a bug report.
- After replies: record each answer against its finding id, and keep it "verbal only" until the ticket or design changes.
- Draft only. The person decides when and where it is sent.
