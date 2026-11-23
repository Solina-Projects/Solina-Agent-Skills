---
name: telegram-integration
description: Build and operate Telegram bots and integrations using official Bot API capabilities and user-authorized workflows.
---

# Telegram Integration

Use Telegram's official Bot API and documented platform capabilities. Identify bot versus user-account requirements; do not automate personal accounts through unofficial session scraping.

<!-- MUSE-ADAPT -->

## Muse adaptation — read first

This skill runs inside Muse's own environment, for Nasser. Where the original instructions below conflict with these points, these points win.

- Host: Linux VM (4 CPU, ~7 GB RAM, x86_64), no GPU. Toolchains live under the home directory only; never rely on system installs. For npm, always set npm_config_cache=/tmp/npm-cache.
- The user (Nasser) is Persian-speaking and phone-only; he has no computer. Deliverables reach him as files in this chat. Explain everything in simple Persian and translate every English label - his English is effectively zero.
- Register: two-way, comfortable, street-style, blunt and honest. No formalities.
- Never ask design-detail questions. Decide, build, then report shortly.
- For Nasser's own work, follow the decisions already recorded in memory (Solina-Player design, Lunaris alioth kernel and ROM, Solina-Launcher).
- UI copy: Persian first, Western (English) digits only, no em dashes in UI copy.
- Apply quality gates silently. Never paste internal gate or lint reports to the user; report outcomes in a few lines.
- Secrets never go into files, memory or chat output. Publishing anything publicly needs his explicit approval first.
- The original skill may name Claude Code tools (Read, Write, Edit, Glob, Grep, Bash) or other agents' commands. Use Muse's own tools instead (file read/write/edit, shell, browser). Use the browser tools for live pages and real-site screenshots.

Protect bot tokens in secret storage. Never paste them into chat, logs, commits or issue reports. Rotate exposed tokens through BotFather.

Design for webhook or long-polling reliability, idempotency, rate limits, retries, privacy, command authorization and safe handling of attachments. Validate webhook authenticity where supported.

Before sending messages, broadcasting, changing group permissions or deleting content, confirm recipients, scope and content. Do not spam, scrape private groups, evade rate limits or impersonate users. Respect opt-in and platform policies.
