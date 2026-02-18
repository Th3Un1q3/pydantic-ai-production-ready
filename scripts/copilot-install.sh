#!/bin/bash
set -euo pipefail

URL="$1"

if [[ -z "$URL" ]]; then
    echo "Usage: $0 <github-url>"
    echo "Example: $0 https://github.com/anthropics/skills/tree/main/skills/skill-creator"
    exit 1
fi

# Example URL: https://github.com/github/awesome-copilot/tree/main/hooks/session-logger

if [[ "$URL" == *"/tree/"* ]]; then
    REPO_URL="${URL%%/tree/*}"
    REST="${URL#*/tree/}"
    BRANCH="${REST%%/*}"
    # The path is everything after the branch
    PATH_IN_REPO="${REST#*/}"
    NAME="${PATH_IN_REPO##*/}"
else
    # Handle root repo case (e.g., https://github.com/owner/repo)
    REPO_URL="$URL"
    BRANCH="main" # Default assumption
    PATH_IN_REPO=""
    NAME="${URL##*/}"
    NAME="${NAME%.git}"
fi

# Extract Repository Name for display (e.g. github/awesome-copilot)
REPO_DISPLAY="${REPO_URL#*github.com/}"
REPO_DISPLAY="${REPO_DISPLAY%.git}"

# Detection of TYPE
TYPE="copilot skill"
TARGET_BASE_DIR=".github/skills"
if [[ "$PATH_IN_REPO" == *"hooks/"* ]]; then
    TYPE="copilot hook"
    TARGET_BASE_DIR=".github/hooks"
fi

TARGET_DIR="$TARGET_BASE_DIR/$NAME"
ABS_TARGET_DIR="/workspace/$TARGET_DIR"

# Pre-installation confirmation
echo "> Please confirm you want to install:"
echo "Type: $TYPE"
echo "Name: $NAME"
echo "Source:"
echo "- Repository: $REPO_DISPLAY"
echo "- Branch: ${BRANCH:-main}(default)"
echo "Destination directory:"
echo "$TARGET_DIR"

HOOKS_CONFIG=".github/hooks/hooks.json"
if [[ "$TYPE" == "copilot hook" && -f "/workspace/$HOOKS_CONFIG" ]]; then
    echo "There is already .$HOOKS_CONFIG with the following hooks configured:"
    cat "/workspace/$HOOKS_CONFIG"
    echo
fi

echo "Do you want to proceed?"
read -p "Type 'y' to continue: " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 1
fi

if [ -d "$ABS_TARGET_DIR" ]; then
    echo "Warning: Directory $TARGET_DIR already exists."
    # Simple prompt
    read -p "Overwrite? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 1
    fi
    rm -rf "$ABS_TARGET_DIR"
fi

TMP_DIR=$(mktemp -d)
trap "rm -rf $TMP_DIR" EXIT

echo "Cloning..."

GIT_ARGS=(clone --depth 1 --filter=blob:none --sparse)
if [[ -n "$BRANCH" ]]; then
    GIT_ARGS+=(--branch "$BRANCH")
fi
GIT_ARGS+=("$REPO_URL" "$TMP_DIR")

git "${GIT_ARGS[@]}"

cd "$TMP_DIR"

if [[ -n "$PATH_IN_REPO" ]]; then
    git sparse-checkout set "$PATH_IN_REPO"
    # Verify path exists
    if [ ! -d "$PATH_IN_REPO" ]; then
        echo "Error: Path '$PATH_IN_REPO' not found in repository."
        exit 1
    fi
    SOURCE_PATH="$PATH_IN_REPO"
else
    git sparse-checkout set "/*"
    SOURCE_PATH="."
fi

# If it's a hook, check if there's a hooks.json in the source to update local hooks.json
if [[ "$TYPE" == "copilot hook" && -f "$SOURCE_PATH/hooks.json" && -f "/workspace/$HOOKS_CONFIG" ]]; then
    echo "Do you want:"
    echo "- override with new hooks(replace with the $NAME/hooks.json) (o)"
    echo "- modify manually as needed (m)"
    read -p "Selection (o/m): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Oo]$ ]]; then
        echo "Updating ./$HOOKS_CONFIG..."
        cp "$SOURCE_PATH/hooks.json" "/workspace/$HOOKS_CONFIG"
    else
        echo "Please modify ./$HOOKS_CONFIG manually after installation if needed."
    fi
fi

echo "Installing..."
mkdir -p "$(dirname "$ABS_TARGET_DIR")"
cp -r "$SOURCE_PATH" "$ABS_TARGET_DIR"

echo "✅ Installed to '$TARGET_DIR'"
