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
    curl -s -X POST "https://api.day.app/x23x7UumVP3ZZgENJGZ6M8" \
        -H "Content-Type: application/json" \
        -d '{"title":"JMS 仓库自动更新完成","body":"检测到内容变动，已自动提交并推送到 GitHub (main 分支) [skip ci]","group":"JMS-Guide","sound":"bell","url":"https://github.com/justmysocks-guide/justmysocks"}' >> "$LOG_FILE" 2>&1 || true
else
    echo "[*] No freshness content changes required today (README.md is already up to date)." >> "$LOG_FILE"
fi

echo "=== [$(date '+%Y-%m-%d %H:%M:%S')] Finished SEO Autopilot Run ===" >> "$LOG_FILE"
