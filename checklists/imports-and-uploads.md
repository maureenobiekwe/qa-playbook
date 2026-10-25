# Imports and uploads

## Limits
- Maximum file size, rows, columns, sheets. What is the error at the limit and one over?
- Accepted types and encodings. Wrong extension with the right content, and the reverse.
- Time: how long may an import take at the stated volume? What does the user see meanwhile?

## Rows
- Required fields missing, one of two contact fields missing, whitespace only.
- Duplicates inside the file and against existing records. Which one wins?
- Mixed formats: dates, phone numbers (national and international), names with accents.
- Partial failure: are good rows kept? Is there an error file with row numbers and reasons?
- Re-uploading the same file: duplicates or a safe no-op?

## Safety
- Spreadsheet formula injection: cells starting with `=`, `+`, `-`, `@` in imports and in exports.
- Macro-enabled files, zip bombs, malformed files, very long cells.
- Uploaded files that carry active content (SVG with script, HTML disguised as an image).
- Who can download an uploaded file or an error report afterwards? How long is it kept? It contains personal data.

## Jobs
- Interrupted job (restart, deploy): does it resume or fail cleanly? Is the status honest?
- Two people importing at once.
- Permission needed to start, cancel and download results.

## Exports
- Format, columns, who may export, whether exports are logged, size limits.
