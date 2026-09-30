#!/bin/bash
# /Users/han/justmysocks/scripts/cron_autopilot.sh
# 100% Automated Local SEO Freshness, Node Diagnostics & GitHub Committer

set -e

REPO_DIR="/Users/han/justmysocks"
LOG_FILE="/Users/han/justmysocks/autopilot.log"

echo "=== [$(date '+%Y-%m-%d %H:%M:%S')] Starting JustMySocks SEO Autopilot ===" >> "$LOG_FILE"

cd "$REPO_DIR"

# Ensure repo is up to date
git pull --rebase origin main >> "$LOG_FILE" 2>&1 || true

# Run AI Freshness and Node Connectivity Diagnostics
python3 "$REPO_DIR/scripts/seo_refresh.py" >> "$LOG_FILE" 2>&1

# Check specifically if README.md has modified content
if ! git diff --quiet README.md; then
    echo "[*] Freshness updates detected in README.md, committing and pushing..." >> "$LOG_FILE"
    git add README.md
    git commit -m "chore(seo): automated monthly freshness & node status refresh [skip ci]" >> "$LOG_FILE" 2>&1
    git push origin main >> "$LOG_FILE" 2>&1
    echo "[+] Successfully pushed SEO freshness update to GitHub." >> "$LOG_FILE"
else
    echo "[*] No freshness content changes required today (README.md is already up to date)." >> "$LOG_FILE"
fi

echo "=== [$(date '+%Y-%m-%d %H:%M:%S')] Finished SEO Autopilot Run ===" >> "$LOG_FILE"
