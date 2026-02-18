#!/bin/bash

# Log session end event

set -euo pipefail

# Skip if logging disabled
if [[ "${SKIP_LOGGING:-}" == "true" ]]; then
  exit 0
fi

# Read input from Copilot
INPUT=$(cat)

# Create logs directory if it doesn't exist
mkdir -p logs/copilot

# Extract timestamp
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Log session end
## Determine session id (if provided) or create one
SESSION_ID=$(jq -r '.sessionId // empty' <<<"$INPUT")
if [[ -z "${SESSION_ID}" ]]; then
  SESSION_ID="sess-$(date -u +%Y%m%dT%H%M%SZ)-$RANDOM"
fi

SESSION_FILE="logs/copilot/sessions/${SESSION_ID}.ndjson"
mkdir -p "$(dirname "$SESSION_FILE")"

# Log session end to aggregate session log
jq -Rn --arg timestamp "$TIMESTAMP" --arg sessionId "$SESSION_ID" '{"timestamp":$timestamp,"event":"sessionEnd","sessionId":$sessionId}' >> logs/copilot/session.log

# Append end marker to per-session file
echo "{\"timestamp\":\"$TIMESTAMP\",\"event\":\"sessionEnd\",\"sessionId\":\"$SESSION_ID\"}" >> "$SESSION_FILE"

# If incoming payload contains closing messages, append them
if echo "$INPUT" | jq -e 'has("messages")' >/dev/null 2>&1; then
  echo "$INPUT" | jq -c '.messages[]' | while read -r msg; do
    echo "{\"timestamp\":\"$TIMESTAMP\",\"event\":\"message\",\"sessionId\":\"$SESSION_ID\",\"message\":$msg}" >> "$SESSION_FILE"
  done
fi

echo "📝 Session end logged to $SESSION_FILE"
exit 0
