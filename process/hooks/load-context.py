"""SessionStart hook: load the project context file into a new session.

Set QA_CONTEXT_FILE to the full path of your context file.
"""
import json
import os
import sys

path = os.environ.get("QA_CONTEXT_FILE")
if not path or not os.path.exists(path):
    sys.exit(0)  # nothing to load; start the session normally

with open(path, encoding="utf-8") as f:
    text = f.read()

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": "Running project context (from the context file):\n\n" + text,
    }
}))
