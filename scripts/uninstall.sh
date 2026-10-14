#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf .venv
echo "Removed this project's virtual environment only. Bettercap and system packages were not removed."
