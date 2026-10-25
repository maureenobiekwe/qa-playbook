# LearnLoop tickets (invented)

## PRD extract (invented)
- Refunds: "A learner may request a refund within 14 days of purchase."
- Discount codes: "Codes expire at the end of the campaign."
- Roles: "Only an Owner can invite instructors."
- Imports: "An admin can import up to 5,000 students from a CSV."
- Certificates: "Learners can download a certificate after completing a course."

## Tickets

**LL-101 [BE] Invite instructors**
Authorised administrators can invite instructors by email. The invitation link expires. Resending an invitation invalidates the old link.
Design: https://example.com/design/invite-instructor

**LL-102 [FE] Checkout page**
Show price, discount field and pay button. Handle errors gracefully. Must match the design.
Design: https://example.com/design/checkout

**LL-103 [BE] Refunds**
A learner can request a refund within 30 days. The refund is processed quickly and the learner is emailed.
Design: n/a (API only)

**LL-104 [BE] Discount codes**
Admins create codes with a percentage and an end date. Expired codes are rejected.
Design: n/a

**LL-105 [BE] Student CSV import**
Admins upload a CSV of students. The import runs in the background using the job queue. Uploaded files are handled safely. A report of errors is available afterwards.
Design: n/a

**LL-106 [FE] Student import screen**
Upload a CSV, show progress, download the error report. States must match the design.
Design: (blank)

**LL-107 [BE] Certificates**
After a learner completes a course, a PDF certificate is generated and can be downloaded. Certificates are audited.
Design: https://example.com/design/certificate

**LL-108 [FE] Notification settings**
Learners can switch email notifications on or off. Admins can see who has switched them off.
Design: https://example.com/design/notifications
