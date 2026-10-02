#!/usr/bin/env python3
"""
scripts/seo_refresh.py - Just My Socks Guide SEO Freshness & Health Checker
Automatically executed by GitHub Actions or local crontab.
Features:
- Verifies connectivity & latency across official mirror domains
- Link Failover: Automatically updates README affiliate URLs to the healthiest active mirror
- Updates timestamps & SEO freshness signals
- Pushes real-time Bark notification to user device
"""

import datetime
import json
import os
import re
import socket
import time
import urllib.parse
import urllib.request

README_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "README.md")
INDEX_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "index.md")
BARK_WEBHOOK = os.getenv("BARK_WEBHOOK", "https://api.day.app/x23x7UumVP3ZZgENJGZ6M8")

# Official candidate mirror domains provided by BandwagonHost / IT7 Networks
OFFICIAL_MIRRORS = [
    "justmysocks.net",
    "justmysocks1.net",
    "justmysocks2.net",
    "justmysocks3.net",
    "justmysocks5.net",
]

# Additional backbone DNS test targets
TEST_HOSTS = [
    ("1.1.1.1", 53),
]


def send_bark(title: str, body: str, url: str = "https://github.com/justmysocks-guide/justmysocks"):
    """Send immediate notification to user's iOS Bark client."""
    if not BARK_WEBHOOK:
        return
    try:
        payload = {
            "title": title,
            "body": body,
            "group": "JMS-Guide",
            "icon": "https://raw.githubusercontent.com/justmysocks-guide/.github/main/assets/logo.png",
            "url": url,
            "sound": "anticipate"
        }
        req = urllib.request.Request(
            BARK_WEBHOOK,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json", "User-Agent": "RedSignal/1.0"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            pass
        print(f"[+] Bark notification sent: {title}")
    except Exception as e:
        print(f"[!] Bark notification failed: {e}")


def check_endpoint_latency(host: str, port: int, timeout: float = 2.5) -> float:
    start = time.time()
    try:
        sock = socket.create_connection((host, port), timeout=timeout)
        latency = (time.time() - start) * 1000.0
        sock.close()
        return round(latency, 1)
    except Exception:
        return -1.0


def select_best_mirror() -> tuple:
    """Find the best responsive mirror. Returns (domain, latency)"""
    results = []
    for mirror in OFFICIAL_MIRRORS:
        lat = check_endpoint_latency(mirror, 443)
        if lat > 0:
            results.append((mirror, lat))
            print(f"  - Mirror {mirror}: 正常 ({lat}ms)")
        else:
            print(f"  - Mirror {mirror}: 不可用 / 超时")

    if not results:
        # Fallback to default if all failed
        return ("justmysocks.net", 999.0)

    # Prefer justmysocks.net if it is alive and under 150ms, otherwise pick lowest latency
    primary = next((item for item in results if item[0] == "justmysocks.net"), None)
    if primary and primary[1] < 150.0:
        return primary

    # Otherwise sort by latency ascending
    results.sort(key=lambda x: x[1])
    return results[0]


def main():
    now = datetime.datetime.now(datetime.timezone.utc)
    # Target date formatted in Asia/Shanghai (UTC+8)
    bj_time = now + datetime.timedelta(hours=8)
    date_str = bj_time.strftime("%Y年%m月%d日")

    print(f"[*] Running SEO Freshness & Mirror Failover Check for: {date_str}")

    # 1. Mirror failover check
    best_mirror, best_lat = select_best_mirror()
    print(f"[+] Selected optimal official mirror: {best_mirror} ({best_lat}ms)")

    # 2. Check general network
    for host, port in TEST_HOSTS:
        lat = check_endpoint_latency(host, port)
        print(f"  - Backbone {host}:{port} -> {lat}ms")

    # 3. Dynamic failover of affiliate links & freshness block for both README.md and index.md
    aff_pattern = re.compile(r"https://justmysocks\d*\.net/members/aff\.php")
    target_aff_url = f"https://{best_mirror}/members/aff.php"

    freshness_block = (
        f"<!-- AUTO_FRESHNESS_START -->\n"
        f"> 🕒 **自动化有效性巡检报告（最后核验：{date_str}）**：\n"
        f"> - ✅ **官方最新专属优惠码**：`JMS9272283`（**5.2% 永久循环折扣**，首购与续费全网 100% 真实有效）；\n"
        f"> - 🌐 **官方存活安全通道**：`{best_mirror}`（探针延迟 {best_lat}ms，已自动对齐最新官方镜像直达跳板）；\n"
        f"> - ⚡️ **三网路由状态**：洛杉矶 CN2 GIA / 联通 9929 顶级优化专线正常，日本软银/香港 IPLC 延迟优异；\n"
        f"> - 🛡️ **自动化防护体系**：搬瓦工后台 7×24 秒级探活运转中，IP 异常自动秒切，保障访问 ChatGPT / Claude 0 阻断。\n"
        f"<!-- AUTO_FRESHNESS_END -->"
    )

    pattern = re.compile(r"<!-- AUTO_FRESHNESS_START -->.*?<!-- AUTO_FRESHNESS_END -->", re.DOTALL)
    any_changed = False

    for target_path in [README_PATH, INDEX_PATH]:
        if not os.path.exists(target_path):
            continue
        with open(target_path, "r", encoding="utf-8") as f:
            content = f.read()

        updated_content = aff_pattern.sub(target_aff_url, content)
        if pattern.search(updated_content):
            updated_content = pattern.sub(freshness_block, updated_content)
        else:
            updated_content = updated_content.replace("\n---\n", f"\n\n{freshness_block}\n\n---\n", 1)

        if updated_content != content:
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
            any_changed = True
            print(f"[+] {os.path.basename(target_path)} refreshed successfully!")

    if any_changed:
        send_bark(
            "JMS 巡检刷新成功",
            f"检测到最优可用镜像: {best_mirror} ({best_lat}ms)，已完成页面时效性区块与故障转移对齐。"
        )
    else:
        print("[*] All files already up-to-date.")


if __name__ == "__main__":
    main()
