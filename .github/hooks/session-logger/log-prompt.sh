#!/bin/bash

# Log user prompt submission

set -euo pipefail

# Skip if logging disabled
if [[ "${SKIP_LOGGING:-}" == "true" ]]; then
  exit 0
fi

# Read input from Copilot (contains prompt info)
INPUT=$(cat)

# Create logs directory if it doesn't exist
mkdir -p logs/copilot

# Extract timestamp
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Log prompt (you can parse INPUT for more details)
echo "{\"timestamp\":\"$TIMESTAMP\",\"event\":\"userPromptSubmitted\",\"level\":\"${LOG_LEVEL:-INFO}\"}" >> logs/copilot/prompts.log

## Determine session file to append full conversation content
SESSION_ID=$(jq -r '.sessionId // empty' <<<"$INPUT")
if [[ -z "${SESSION_ID}" ]]; then
  # fall back to ad-hoc session id so messages are still preserved
  SESSION_ID="adhoc-$(date -u +%Y%m%dT%H%M%SZ)-$RANDOM"
fi

SESSION_FILE="logs/copilot/sessions/${SESSION_ID}.ndjson"
mkdir -p "$(dirname "$SESSION_FILE")"

# Try to use the incoming payload as JSON; if it's not JSON, encode as a string
if echo "$INPUT" | jq -e . >/dev/null 2>&1; then
  PAYLOAD_JSON=$(echo "$INPUT" | jq -c '.')
else
  PAYLOAD_JSON=$(jq -Rn --arg s "$INPUT" '$s')
fi

# Append the prompt payload to the per-session file (ndjson line)
echo "{\"timestamp\":\"$TIMESTAMP\",\"event\":\"userMessage\",\"sessionId\":\"$SESSION_ID\",\"payload\":$PAYLOAD_JSON}" >> "$SESSION_FILE"

exit 0
