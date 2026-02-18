#!/bin/bash

# Log session start event

set -euo pipefail

# Skip if logging disabled
if [[ "${SKIP_LOGGING:-}" == "true" ]]; then
  exit 0
fi

# Read input from Copilot
INPUT=$(cat)

# Create logs directories if they don't exist
mkdir -p logs/copilot
mkdir -p logs/copilot/sessions

# Extract timestamp and session info
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
CWD=$(pwd)

## Determine session id (if provided) or create one
SESSION_ID=$(jq -r '.sessionId // empty' <<<"$INPUT")
if [[ -z "${SESSION_ID}" ]]; then
  SESSION_ID="sess-$(date -u +%Y%m%dT%H%M%SZ)-$RANDOM"
fi

SESSION_FILE="logs/copilot/sessions/${SESSION_ID}.ndjson"

# Log session start to the aggregate session log (use jq for proper JSON encoding)
jq -Rn --arg timestamp "$TIMESTAMP" --arg cwd "$CWD" --arg sessionId "$SESSION_ID" '{"timestamp":$timestamp,"event":"sessionStart","cwd":$cwd,"sessionId":$sessionId}' >> logs/copilot/session.log

# Create per-session file and record start metadata
echo "{\"timestamp\":\"$TIMESTAMP\",\"event\":\"sessionStart\",\"sessionId\":\"$SESSION_ID\",\"cwd\":\"$CWD\"}" >> "$SESSION_FILE"

# If the incoming payload contains initial messages, append them to the session file
if echo "$INPUT" | jq -e 'has("messages")' >/dev/null 2>&1; then
  echo "$INPUT" | jq -c '.messages[]' | while read -r msg; do
    echo "{\"timestamp\":\"$TIMESTAMP\",\"event\":\"message\",\"sessionId\":\"$SESSION_ID\",\"message\":$msg}" >> "$SESSION_FILE"
  done
fi

echo "📝 Session started and stored in $SESSION_FILE"
exit 0
