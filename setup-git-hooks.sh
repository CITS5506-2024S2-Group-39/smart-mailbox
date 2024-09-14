#!/usr/bin/env bash
REPO=$(git rev-parse --show-toplevel)
source "$REPO/.githooks/functions.sh"

# Configure git hooks
(
    set -e -x
    git config commit.cleanup strip
    git config core.hooksPath .githooks
)
if [ $? -eq 0 ]; then
    success 'Git hooks configured for local repository.'
else
    error 'Failed to configure git hooks for local repository.'
    exit 1
fi

# Install formatters
(
    set -e -x
    py -m pip install black >/dev/null 2>&1
    npm install --global prettier >/dev/null 2>&1
)
if [ $? -eq 0 ]; then
    success 'Code formatters installed successfully.'
else
    error 'Failed to install code formatters for git hook.'
    error 'Please ensure that both Python 3 and Node.js are installed on your system.'
    exit 1
fi
