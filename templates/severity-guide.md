# Severity guide

Severity is about impact. Priority (what to fix first) is the product owner's call.

| Severity | Meaning | Examples |
|---|---|---|
| Critical | Data loss, security breach, or the product cannot be used by anyone | Any user can read another user's records; payment recorded twice; login down |
| High | A main flow is broken for many users, or a rule that protects money or access is bypassed, with no workaround | A user can give themselves a privileged role; learners cannot complete checkout on mobile |
| Medium | A feature is wrong or incomplete but there is a workaround, or the impact is limited | Duplicate profiles allowed; wrong error text on a failed upload |
| Low | Cosmetic or minor | Misaligned label, typo, inconsistent capitalisation |

## Questions that move a defect up or down
- Does it expose or change data a person should not reach? Move up.
- Is there a workaround a normal user would find? Move down.
- Is it a regression of something that worked? Move up.
- Does it affect an accessibility requirement (keyboard, contrast, labels)? Treat as at least Medium.
- Is it only visible in one browser or device? Note the share of users affected.
