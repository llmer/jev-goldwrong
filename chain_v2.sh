#!/bin/zsh
cd "$(dirname "$0")"
set -a; . ./.env; set +a
export BUDGET_USD=3
uv run run_v2.py --concurrency 16
echo "=== CHAIN DONE $(date)"
