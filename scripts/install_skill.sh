#!/bin/bash
set -euo pipefail

URL="$1"

if [[ -z "$URL" ]]; then
    echo "Usage: $0 <github-url>"
    echo "Example: $0 https://github.com/anthropics/skills/tree/main/skills/skill-creator"
    exit 1
fi

# Example URL: https://github.com/anthropics/skills/tree/main/skills/skill-creator

if [[ "$URL" == *"/tree/"* ]]; then
    REPO_URL="${URL%%/tree/*}"
    REST="${URL#*/tree/}"
    BRANCH="${REST%%/*}"
    # The path is everything after the branch
    PATH_IN_REPO="${REST#*/}"
    
    # If the path is the same as the branch (e.g. no path), handle it
    if [[ "$BRANCH" == "$PATH_IN_REPO" ]]; then
        PATH_IN_REPO=""
        SKILL_NAME="${REPO_URL##*/}"
    else
        SKILL_NAME="${PATH_IN_REPO##*/}"
    fi
else
    # Handle root repo case (e.g., https://github.com/owner/repo)
    REPO_URL="$URL"
    BRANCH="main" # Default assumption, or we could query it, but let's default to main or master logic if git clone handles it.
    # Actually, for sparse checkout of a specific subdirectory, we usually need the path. 
    # If the user gives a root URL, maybe they want to install the whole repo as a skill?
    # Let's simplify: require tree/structure for now as per request pattern, or just clone the whole thing if no tree.
    echo "Attempting to clone full repository..."
    REPO_URL="$URL"
    BRANCH=""
    PATH_IN_REPO=""
    SKILL_NAME="${URL##*/}"
    SKILL_NAME="${SKILL_NAME%.git}"
fi

TARGET_DIR=".github/skills/$SKILL_NAME"
ABS_TARGET_DIR="/workspace/$TARGET_DIR"

echo "Repo: $REPO_URL"
if [[ -n "$BRANCH" ]]; then echo "Branch: $BRANCH"; fi
if [[ -n "$PATH_IN_REPO" ]]; then echo "Path: $PATH_IN_REPO"; fi
echo "Target: $TARGET_DIR"

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

echo "Installing..."
mkdir -p "$(dirname "$ABS_TARGET_DIR")"
cp -r "$SOURCE_PATH" "$ABS_TARGET_DIR"

echo "✅ Skill '$SKILL_NAME' installed to '$TARGET_DIR'"
