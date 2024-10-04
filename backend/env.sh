#!/bin/env bash
REPO=$(git rev-parse --show-toplevel)
cd "$REPO/backend"

# Sourcing this file will install relevant packages
rm -rf venv
py -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Exclude changes to apikey.txt to avoid accidental commits of sensitive information
git update-index --assume-unchanged "$REPO/backend/gpt/apikey.txt"
