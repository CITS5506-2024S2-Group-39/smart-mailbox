#!/usr/bin/env bash
REPO=$(git rev-parse --show-toplevel)
source "$REPO/.githooks/functions.sh"

# Configure git hooks
(
    set -e -x
    git config commit.cleanup strip
    git config core.hooksPath .githooks
)
if [[ $? -eq 0 ]]; then
    success 'Git hooks configured for local repository.'
else
    error 'Failed to configure git hooks for local repository.'
    exit 1
fi

# Install Python code formatter
(
    set -e -x
    if command -v apt >/dev/null; then
        sudo apt install black -y >/dev/null
    else
        py -m pip install black >/dev/null
    fi
)
if [[ $? -eq 0 ]]; then
    success 'Python code formatter installed successfully.'
else
    error 'Failed to install Python code formatter for git hook.'
    error 'Please ensure that Python 3 is installed on your system.'
    exit 1
fi

# Install frontend code formatter
(
    set -e -x
    cd "$REPO/frontend"
    npm install --save-dev prettier prettier-plugin-classnames
)
if [[ $? -eq 0 ]]; then
    success 'Frontend code formatter installed successfully.'
else
    error 'Failed to install frontend code formatter for git hook.'
    error 'Please ensure Node.js and Npm is installed on your system.'
    exit 1
fi
