#!/usr/bin/env bash
set -euo pipefail

# Extracted from repository `justfile` — runs multiple Copilot prompts in parallel
# Usage: ./scripts/agent-parallel.sh "prompt 1" "prompt 2" ...

model="gpt-5-mini"

allowed_tools=(
    "context7"
    "tavily"
)

cmd_args=("copilot" "--model" "$model")

for tool in "${allowed_tools[@]}"; do
    cmd_args+=("--allow-tool" "$tool")
done

# Build --additional-mcp-config from transformed .vscode/mcp.json (use standalone Python helper)
mcp_file="./.vscode/mcp.json"
[ -f "$mcp_file" ] || mcp_file="/workspace/.vscode/mcp.json"
if [ -f "$mcp_file" ]; then
    additional_mcp_config=$(python3 "scripts/transform_mcp.py" "$mcp_file" 2>/tmp/agent-parallel-mcp.err || true)
    if [ $? -eq 0 ] && [ -n "$additional_mcp_config" ]; then
        # pass modified JSON string directly
        cmd_args+=("--additional-mcp-config" "$additional_mcp_config")
    else
        # fallback to passing the file path (use @file to indicate file input)
        cmd_args+=("--additional-mcp-config" "@$mcp_file")
        # surface any Python helper warnings/errors
        if [ -s /tmp/agent-parallel-mcp.err ]; then
            cat /tmp/agent-parallel-mcp.err >&2 || true
        fi
    fi
fi

max_tasks=5
num_tasks=$#
if [ "$num_tasks" -gt "$max_tasks" ]; then
    echo "⚠️ Limiting to first $max_tasks tasks (out of $num_tasks provided)."
    num_tasks=$max_tasks
fi

echo "🚀 Running $num_tasks tasks in parallel."

tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT

# Run prompts in background and capture PIDs
declare -a pids outputs statuses exit_codes prompts commands
i=0
for prompt in "${@:1:$num_tasks}"; do
    i=$((i+1))

    iteration_cmd_args=("${cmd_args[@]}" "-p" "$prompt")
    echo "[ TASK $i ] — starting: $prompt"

    # record prompt and the full command (for debugging on failure)
    prompts[$i]="$prompt"
    commands[$i]="${iteration_cmd_args[*]}"

    "${iteration_cmd_args[@]}" > "$tmpdir/output_$i.tmp" 2>&1 &

    pids[$i]=$!
done

# Wait for all and collect results (capture exit codes and outputs)
any_failed=0
for j in $(seq 1 "$i"); do
    if wait "${pids[$j]}"; then
        statuses[$j]=OK
        exit_codes[$j]=0
    else
        rc=$?
        statuses[$j]=FAILED
        exit_codes[$j]=$rc
        any_failed=1
    fi
    outputs[$j]=$(cat "$tmpdir/output_$j.tmp" 2>/dev/null || true)
    rm -f "$tmpdir/output_$j.tmp" 2>/dev/null || true

    # Heuristic: if command exited with 0 but output contains error-like words, mark as FAILED
    if [ "${exit_codes[$j]}" -eq 0 ]; then
        if printf '%s\n' "${outputs[$j]}" | grep -iE '(^|\b)(error|failed|invalid|exception|traceback)\b' >/dev/null 2>&1; then
            statuses[$j]=FAILED
            exit_codes[$j]=2
            any_failed=1
        fi
    fi
done

echo -e "\n=== MERGED OUTPUT ===\n"

for j in $(seq 1 "$i"); do
    if [ "${statuses[$j]}" = "OK" ]; then
        echo "[ TASK $j SUCCESS ] prompt: ${prompts[$j]}"
        echo "command: ${commands[$j]}"
        printf '%s\n' "${outputs[$j]}"
        echo -e "\n---\n"
    else
        echo "[ TASK $j FAILED (exit ${exit_codes[$j]}) ] prompt: ${prompts[$j]}" >&2
        echo "command: ${commands[$j]}" >&2
        printf '%s\n' "${outputs[$j]}" >&2
        echo -e "\n---\n" >&2
    fi
done

[ "$any_failed" -eq 0 ] || { echo -e "\n⚠️ Some tasks failed."; exit 1; }
