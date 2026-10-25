**Subject:** Release 2: 8 decisions I need before I can write test cases

Hi Dana,

I read all 8 Release 2 tickets against the PRD, the designs and the code. **Nothing here is a bug.** These are places where the documents disagree or say nothing, so I cannot write an expected result. The full log (14 items) is in the shared sheet. These 8 block the most testing, and each has a suggested answer, so a "yes" or "no, do X" is enough.

## A. The documents disagree

**1. How long is the refund window?**
- PRD says: "within 14 days of purchase".
- LL-103 says: "within 30 days".
- *Why it matters:* a learner on day 20 either gets a refund or does not, so I cannot write the case.
- *Suggested:* 14 days, and the ticket is corrected.

**2. Who can invite instructors?**
- PRD: "Only an Owner".
- LL-101: "authorised administrators".
- *Suggested:* Owner only for this release.

**3. Import size.** The PRD says up to 5,000 students; the ticket gives no limit. *Suggested:* 5,000 rows, with a clear error at 5,001.

## B. Rules I need written down

**4. What does "processed quickly" mean for a refund?** *Suggested:* status becomes Approved within 1 working day, payout time is shown separately.

**5. How long does an invitation link last?** The ticket says "expires". *Suggested:* 7 days. I also need a way to age a link in the test environment so I do not wait a week.

**6. Which time zone do discount codes end in?** *Suggested:* end of day in the company time zone, inclusive.

## C. Design

**7. The import screen has no design,** but the ticket says it must match one. I cannot test the screen until there is a design.

## D. Heads-up for engineering

The import ticket assumes a job queue. The repository has none and the deployment notes say there is no worker. Certificates are "audited", but the only audit code writes to the log, so there is nothing stored to test.

**8. Which of these two should come first, the queue or the audit store?** They decide how much of Release 2 I can test.

Thanks. A 30-minute call would also work.

Priya (QA)
