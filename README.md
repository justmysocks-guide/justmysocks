# justmysocks-guide/justmysocks — 指南站源码与文档仓库

<p align="center">
  <img src="https://raw.githubusercontent.com/justmysocks-guide/.github/main/assets/logo.png" width="120" height="120" alt="Just My Socks Guide Logo" />
</p>

<p align="center">
  <a href="https://justmysocks-guide.github.io/justmysocks/"><img src="https://img.shields.io/badge/Live%20Website-Online%20Guide-success.svg?style=flat-square" alt="Live Website" /></a>
  <a href="https://github.com/justmysocks-guide/justmysocks/stargazers"><img src="https://img.shields.io/github/stars/justmysocks-guide/justmysocks?style=flat-square" alt="GitHub Stars" /></a>
  <a href="https://justmysocks-guide.github.io/justmysocks/coupon/"><img src="https://img.shields.io/badge/Promo%20Code-JMS9272283%20(5.2%25%20OFF)-red.svg?style=flat-square" alt="Just My Socks Promo Code" /></a>
</p>

<!-- AUTO_FRESHNESS_START -->
> 🕒 **自动化有效性巡检报告（最后核验：2026年10月25日）**：
> - ✅ **官方最新专属优惠码**：`JMS9272283`（**5.2% 永久循环折扣**，首购与续费全网 100% 真实有效）；
> - 🌐 **官方存活安全通道**：`justmysocks.net`（探针延迟 65.6ms，已自动对齐最新官方镜像直达跳板）；
> - ⚡️ **三网路由状态**：洛杉矶 CN2 GIA / 联通 9929 顶级优化专线正常，日本软银/香港 IPLC 延迟优异；
> - 🛡️ **自动化防护体系**：搬瓦工后台 7×24 秒级探活运转中，IP 异常自动秒切，保障访问 ChatGPT / Claude 0 阻断。
<!-- AUTO_FRESHNESS_END -->

## 这个仓库是什么

这里是 **Just My Socks 中文指南站的源码仓库**：线上站点 [justmysocks-guide.github.io/justmysocks](https://justmysocks-guide.github.io/justmysocks/) 的每一页都由本仓库的 Markdown 源文件经 GitHub Pages（Jekyll）构建生成。想读指南请直接访问线上站；想查某页的原文、历史版本或提交纠错，来这里。

与组织里其他仓库的分工：

| 仓库 | 角色 |
| --- | --- |
| **justmysocks**（本仓库） | 指南站源码：套餐、优惠码、购买教程等页面的源文件 |
| [jms-speedtest](https://github.com/justmysocks-guide/jms-speedtest) | 节点一键测速与 AI / 流媒体解锁检测脚本 |
| [clash-rules](https://github.com/justmysocks-guide/clash-rules) | Clash Verge Rev / Mihomo 分流规则集 |
| [.github](https://github.com/justmysocks-guide/.github) | 组织主页与 FAQ 问答（Issues 区） |

## 线上页面索引（源文件 → 线上地址）

| 源文件 | 线上页面 | 内容一句话 |
| --- | --- | --- |
| `index.md` | [指南首页](https://justmysocks-guide.github.io/justmysocks/) | 全站导航与快速入口 |
| `coupon/index.md` | [优惠码专页](https://justmysocks-guide.github.io/justmysocks/coupon/) | 循环码 `JMS9272283` 的到手价核算与付款前验码方法 |
| `tutorial/index.md` | [购买教程](https://justmysocks-guide.github.io/justmysocks/tutorial/) | 从选套餐、填码、付款到导入订阅的完整流程 |
| `plans/index.md` | [套餐对比](https://justmysocks-guide.github.io/justmysocks/plans/) | 各机房套餐的价格、流量与设备数对比 |
| `en/index.md` | [English Guide](https://justmysocks-guide.github.io/justmysocks/en/) | Plans, promo code and setup guide in English |
| `clash/` | [Clash 教程](https://justmysocks-guide.github.io/justmysocks/clash/) | 订阅导入与 s3 / s4 线路切换 |
| `chatgpt-claude/` | [AI 解锁说明](https://justmysocks-guide.github.io/justmysocks/chatgpt-claude/) | ChatGPT / Claude 403 的成因与处理 |

## 更新日志

- **2026-10-24**：新增英文页 `/en/`；组织 FAQ 问答扩充至 8 篇（新增订阅安全、流量说明、官网辨别、客户端选择、合用拼车）。
- **2026-10-24**：新增套餐对比页 `/plans/`，价格只收录多来源核对一致的条目。
- **2026-10-24**：新增购买教程页 `/tutorial/`，与优惠码页互链。
- **2026-10-24**：新增优惠码专页 `/coupon/`：辟谣虚假高折扣、公布各套餐用码后到手价、附付款前 10 秒验码法。
- **2026-09-28**：仓库建立，指南首页、Clash 教程、AI 解锁三页上线。

## 纠错与提问

- 内容有误或价格过期：在 [.github 仓库的 Issues](https://github.com/justmysocks-guide/.github/issues) 里提问，那里也是 FAQ 问答区（优惠码、线路、流量、订阅安全等 8 个主题）。
- 测速脚本的问题请去 [jms-speedtest](https://github.com/justmysocks-guide/jms-speedtest)，规则集的问题请去 [clash-rules](https://github.com/justmysocks-guide/clash-rules)。

## 维护说明

- 本仓库由 GitHub Pages 直接构建，推送到 `main` 分支即自动发布；`sitemap.xml` 由 Jekyll 插件按页面自动生成。
- 优惠码与价格类信息以官网下单页为准，本仓库的核对日期标注在各页面正文中。

---

*披露：本指南为独立第三方整理，与 Just My Socks 官方无隶属关系；文中部分链接为推广链接，站方可能获得佣金，不影响文中价格与结论。*
