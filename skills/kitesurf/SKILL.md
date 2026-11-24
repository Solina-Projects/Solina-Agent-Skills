---
name: kitesurf
description: Use Cloudflare's Kitesurf cloud browser as a fallback when Muse's own browser cannot read a site — it fetches the page, runs JavaScript, renders it, and speaks the Chrome DevTools Protocol.
---

# Kitesurf — Cloudflare open-source cloud browser (agent fallback)

## What it is
Kitesurf is Cloudflare's experimental browser engine that runs entirely on
Cloudflare Workers — no Chromium process or container. It fetches a page,
runs its JavaScript, lays it out and paints it. It speaks the Chrome
DevTools Protocol (CDP), so Puppeteer, Playwright and chrome-devtools-mcp
can drive it. Repo: https://github.com/cloudflare/kitesurf (Apache-2.0,
~2.5k stars, created 2026-09-30). Playground: https://kitesurf.dev/

## When to use it
Fallback when Muse's own browser cannot read a site: `browser.open` fails,
the page is JS-rendered and returns nothing useful, or the live browser is
blocked. Kitesurf renders the page and can return a screenshot, a PDF, the
rendered HTML, or console output.

## How to use it
- **Playground (no account):** open `https://kitesurf.dev/?url=<target-url>`
  in the live browser — DevTools opens on that page. From there take a
  screenshot, export a PDF, read the rendered HTML, or check the console.
- **CDP (agent-driven):** point chrome-devtools-mcp at
  `wss://kitesurf.dev/devtools/browser` (playground, no account), or at
  Cloudflare Browser Run
  (`wss://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/browser-run/devtools/browser?browser=kitesurf`
  with `Authorization: Bearer <CLOUDFLARE_API_TOKEN>`).
- **Local Docker (no Cloudflare account):**
  `docker run --rm -p 127.0.0.1:8787:8787 ghcr.io/cloudflare/kitesurf`,
  then connect Playwright/Puppeteer to
  `ws://127.0.0.1:8787/devtools/browser`. Health: `http://127.0.0.1:8787/health`.

## Limits (do not forget)
- **Does NOT pass CAPTCHA.** If a page is behind a bot check, Kitesurf
  will not get through it either — use the live browser takeover instead.
- Experimental: some DevTools features do not work yet; rendering may
  differ from real Chrome.
- Running Kitesurf on Cloudflare needs Dynamic Workers (Workers Paid plan).
  The Docker image needs no account.
- Security: locally it runs page JS in workerd, which is NOT a hardened
  sandbox — do not open untrusted sites with a local instance. The engine
  has no authentication — never publish its port (8787) on a public network.
- It is a page reader/renderer, not a login agent: it cannot sign in to
  the user's accounts for them.
