#!/bin/env bash
# Sourcing this file will install relevant packages
set -e
REPO=$(git rev-parse --show-toplevel)
cd "$REPO/backend"
rm -r venv
py -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
