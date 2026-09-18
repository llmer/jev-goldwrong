#!/bin/zsh
cd "$(dirname "$0")"
set -a; . ./.env; set +a
export BUDGET_USD=4
uv run run_v3.py --concurrency 16
echo "=== CHAIN DONE $(date)"
