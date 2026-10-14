#!/usr/bin/env bash
set -u
printf '%s\n' "== Bettercap Toolkit environment check =="
command -v python3 >/dev/null 2>&1 && python3 --version || echo "Python 3 not found"
command -v bettercap >/dev/null 2>&1 && bettercap -version || echo "Bettercap not found in PATH"
command -v ip >/dev/null 2>&1 && ip -brief address || echo "'ip' command not found"
