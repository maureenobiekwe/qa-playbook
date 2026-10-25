# Keeping project context across sessions

Long projects outlive any single chat with an AI assistant. A session that starts empty forgets the decisions, the open questions and the rules you agreed. This is the small setup I use so it does not.

## The idea

One short file, `context.md`, holds the facts that matter:

- project and release order
- environments and how a build gets there
- who decides what
- decisions already made (with the date and who made them)
- the state of each piece of work
- open items
- rules that must never be broken (for example, "test data only")
- a dated log of what changed

Two small hooks keep it honest:

1. **At session start,** a script loads the file into the assistant's context, so every new session begins informed.
2. **At the end of each task,** a script asks the assistant to update the file if anything changed (a decision, a status, a file, an open item). It makes no edit if nothing changed.

## Why this works better than "remember everything"

- A long chat is slow and expensive because every message re-reads the whole history. A new session plus a short file is faster and cheaper.
- The file is plain text you can read, correct and version.
- It records decisions, not conversation, so it stays short.

## Rules I keep in the file

- **Verbal is not final.** An answer given in a call or a voice note is "answered, ticket not updated" until the ticket or design changes.
- **Never store secrets or real user data.** Refer to a file and line, not the value.
- **Keep it short.** If it grows past a screen or two per section, move detail into a document and link it.
- **Dates are absolute** (2026-10-25, not "yesterday").

## What goes wrong

- The file drifts from reality if nobody updates it. The end-of-task hook is there for exactly this.
- A hook that blocks the end of a task must not loop. The update script checks a flag and lets the assistant finish on the second pass.
- Project facts must never be copied into a public repository. Keep the file outside any repo you publish.

## Setup

1. Copy `hooks/context.template.md` somewhere outside your public repositories and fill it in.
2. Copy `hooks/load-context.py` and `hooks/update-context.py` to a folder of your choice.
3. Set the environment variable `QA_CONTEXT_FILE` to the full path of your context file.
4. Merge `hooks/settings.example.json` into your assistant's settings, changing the two script paths.
5. Start a new session and confirm the file is loaded. Finish a task and confirm the update prompt appears.

The scripts need Python 3 and nothing else.
