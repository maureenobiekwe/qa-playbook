"""Stop hook: ask the assistant to update the context file before it finishes a task.

Set QA_CONTEXT_FILE to the full path of your context file.
"""
import json
import os
import sys

data = json.load(sys.stdin)

# The second stop (after the update ran) must pass, or the hook would loop forever.
if data.get("stop_hook_active"):
    sys.exit(0)

path = os.environ.get("QA_CONTEXT_FILE", "the context file")
reason = (
    "Before you finish: if this task changed any decision, status, file, bug, "
    f"open item or fact, update {path} (edit the relevant section, refresh "
    "'Open items', add one line to 'Log' and bump 'Last updated'). Never write "
    "secrets or real user data. If nothing changed, make no edit. Then finish "
    "with a one-line note."
)
print(json.dumps({"decision": "block", "reason": reason}))
