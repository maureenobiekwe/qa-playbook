# Dates and time zones

- Which time zone does each date use: the user's, the organisation's, UTC? It must be written down.
- Store timestamps in UTC; display in a stated zone. Check the label shown to the user.
- Cut-off times: to the minute or the end of the day? Inclusive or exclusive?
- Daylight saving changes (even if one zone has none, travellers and servers do).
- Users abroad: a deadline set in one zone viewed from another.
- Scheduled sends: what happens if the app was down at send time? Sent late, skipped or duplicated?
- Date-only fields: no hidden time that shifts the day when converted.
- Expiry of links and codes: tested by ageing a record, not by waiting. Ask for a way to age a token in the test environment.
- Sorting and filtering by date across the day boundary.
- Date formats and locale (DD/MM vs MM/DD) in forms, exports and emails.
