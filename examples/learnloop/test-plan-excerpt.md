# Test plan excerpt: LearnLoop Release 2 (draft v0.1, pending decisions)

## Testable now
| Case | Ticket | Expected result |
|---|---|---|
| TC-001 Owner can invite an instructor | LL-101 | Invitation created, email sent to the invited address |
| TC-002 A non-Owner cannot invite | LL-101 | 403, no invitation created |
| TC-003 Resending invalidates the old link | LL-101 | Old link shows "link expired"; new link works |
| TC-004 An expired discount code is rejected | LL-104 | 400 with the message "code expired" |

## Outlined, expected result TBD
| Case | Ticket | Expected result |
|---|---|---|
| TC-010 Refund requested on day 20 | LL-103 | **TBD (LL-AMB-01)**: refused if 14 days, accepted if 30 |
| TC-011 Invitation link at 8 days | LL-101 | **TBD (LL-AMB-05)**: expired if lifetime is 7 days |
| TC-012 Discount code at 23:59 on the end date | LL-104 | **TBD (LL-AMB-07)**: depends on zone and inclusive end |
| TC-013 Import of 5,001 rows | LL-105 | **TBD (LL-AMB-09)** |

## Not written yet
- Import screen cases (LL-106): no design (LL-AMB-11).
- Background import behaviour (LL-105): no queue exists (LL-AMB-08).
- Certificate audit record (LL-107): nothing stores one (LL-AMB-12).

## Rule
An answer given verbally moves a finding to "Answered" but the expected result stays TBD until the ticket or design changes and QA has re-read it.
