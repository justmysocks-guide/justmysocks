---
layout: default
title: "Just My Socks: Plans, Promo Code and Setup Guide (2026)"
description: "Just My Socks (JMS) is BandwagonHost's managed proxy service with CN2 GIA routes and automatic IP rotation. Plans from $5.88/mo, the working promo code JMS9272283 takes 5.2% off every renewal, and setup takes one subscription link."
lang: en
---

# Just My Socks, explained without the hype

Just My Socks (often written justmysocks, or JMS for short) is a managed proxy service run by IT7 Networks, the company behind BandwagonHost. It has been operating since late 2018. The pitch is simple: instead of renting a VPS and maintaining your own proxy setup — and paying to replace the IP every time it gets blocked — you buy a plan, get a subscription link, and the service rotates IPs automatically when one stops working.

This page is the English summary of our full guide. It covers what the service costs, which plan to pick, the one promo code that actually works, and how setup works.

## Plans at a glance

Plan names follow a pattern: location + monthly traffic. LA is Los Angeles, and 500 means 500 GB per month.

| Plan | Location / route | Traffic | Devices | Price | Best for |
| --- | --- | --- | --- | --- | --- |
| LA 500 | Los Angeles, CN2 GIA | 500 GB | 5 | $5.88/mo | Most people: browsing, video, ChatGPT/Claude |
| LA 1000 | Los Angeles, CN2 GIA | 1 TB | Unlimited | $9.88/mo | Households, heavy downloads |
| LA 5000 | Los Angeles, CN2 GIA | 5 TB | Unlimited | $48.99/mo | Small teams and studios |
| Hong Kong 500 (CMI+NTT) | Hong Kong | 500 GB | 5 | $8.99/mo | Lower latency from Asia, moderate use |
| London 500 | London | 500 GB | 5 | $6.80/mo | Europe-facing work |
| Tokyo 100 | Tokyo | 100 GB | 3 | $29.99/mo | Latency-sensitive use only |

Prices are the list prices at the time of writing and can change; the cart total is the source of truth. Tokyo and Hong Kong also have premium IPLC and dedicated CN2 GIA tiers that cost several times more for less traffic — they exist for latency-critical workloads, and most people should skip them.

Not sure which one? Start with LA 500 monthly. Plans can be upgraded later by paying the difference; the reverse is not true, so buying big "just in case" is the expensive way to find out you needed less.

## The promo code situation, honestly

There is exactly one long-running Just My Socks promo code: **`JMS9272283`**, good for **5.2% off**. It is a recurring discount — use it on your first order and every renewal invoice keeps the 5.2% off automatically.

Coupon sites advertising "75% OFF" or "85% OFF" Just My Socks codes are making it up. No such public code exists; clicking through those listings eventually lands you on this same 5.2% code, or on codes that do not work at all. 5.2% sounds small, but stacked on annual billing (an annual plan costs roughly ten months' worth of monthly payments) the effective saving versus paying monthly with no code is about 21%.

To use it: add a plan to the cart, enter `JMS9272283` in the Promotional Code field on the order summary, and click **Validate Code**. Check that the total drops by 5.2% before you pay — entering the code without clicking Validate does nothing, and a code missed on the first order cannot be added to renewals later.

## How buying and setup work

1. **Order** on the official site, justmysocks.net. Watch the domain: lookalike and phishing sites exist, so if the checkout looks off, stop. Payment options include Alipay, UnionPay and PayPal.
2. **Get your subscription link.** After payment, open Services in your account, select your plan, and find the Subscription section on the service details page. That link is the key to everything else.
3. **Import it into a client.** Paste the subscription link into Clash Verge Rev, Sing-box, Shadowrocket or a similar client and all five routes appear at once. Prefer the s3/s4 routes (CN2 GIA / premium routes) over the default s1/s2 for evening-peak stability.

Two things worth knowing about the subscription link: treat it like a password — anyone who has it can use your plan — and always import via the subscription link rather than entering a single node by hand. The automatic IP rotation only reaches you through subscription updates; a manually entered node keeps pointing at the old IP.

## Common questions

**What happens when an IP gets blocked?**
Nothing you need to do. The service monitors its nodes and assigns a fresh IP automatically; refresh your subscription in the client and you are back.

**Is 500 GB enough?**
For text-heavy use and a couple of hours of 1080p video a day, comfortably. If your TV streams 4K for hours daily, go straight to LA 1000 — traffic resets monthly on your billing date, and going over means throttling or a pause until the reset, not an extra charge.

**Can I share a plan?**
Within the device limit, yes. LA 500 allows 5 simultaneous connections; plans marked unlimited do not cap devices.

**Where is the detailed documentation?**
The in-depth guides on this site are in Chinese: [promo code details](../coupon/), [buying walkthrough](../tutorial/), [full plan comparison](../plans/), and the [Clash setup guide](../clash/).

---

*Disclosure: this page contains affiliate links. If you buy through them I may earn a small commission at no extra cost to you. The promo code works the same whether you use a link here or type it in yourself.*
