# Auth, roles and permissions

## Sign-in and accounts
- Wrong password: same message whether the email exists or not (no account enumeration).
- Lockout after repeated failures: threshold, duration, and whether an attacker can lock a real user out.
- Password rules (length, common-password block) enforced on the server, not only the form.
- Session expiry and inactivity timeout mid-task; sign-out really ends the session on the server.
- Reset link: lifetime, single use, old links dead after a new one, works only for the right account type.
- Email verification: can an unverified user act? Does accepting an invitation count as verification?

## Account states
Draw the matrix: pending, active, deactivated, cancelled, expired. For each state: can sign in, can reset a password, can be re-invited. Missing cells are findings.

## Roles
- Is access decided by permission codes or by role names? Role-name checks hide bugs.
- Test each role against each action, not only the happy path. A 403 must be a real 403, not a hidden button.
- Who may grant a permission they do not hold themselves? They should not be able to.
- Can someone change their own role or remove the last administrator?
- A permission change: does it apply at once or only after the next sign-in?

## Scope
- Scope on the role or on the assignment (platform, organisation, programme)?
- Can one person hold two scopes? What do they see?
- Can a scoped user read or edit a record outside their scope by changing the id in the URL (broken object-level authorisation)?

## Ownership
- Lists of personal records must filter to the caller unless they hold an "all records" permission.
- Test with two users of the same role: can A open B's record by id?
