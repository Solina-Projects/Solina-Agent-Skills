---
name: telegram-integration
description: Build and operate Telegram bots and integrations using official Bot API capabilities and user-authorized workflows.
---

# Telegram Integration

Use Telegram's official Bot API and documented platform capabilities. Identify bot versus user-account requirements; do not automate personal accounts through unofficial session scraping.

Protect bot tokens in secret storage. Never paste them into chat, logs, commits or issue reports. Rotate exposed tokens through BotFather.

Design for webhook or long-polling reliability, idempotency, rate limits, retries, privacy, command authorization and safe handling of attachments. Validate webhook authenticity where supported.

Before sending messages, broadcasting, changing group permissions or deleting content, confirm recipients, scope and content. Do not spam, scrape private groups, evade rate limits or impersonate users. Respect opt-in and platform policies.
