---
name: telegram-text-safely
description: "Send Telegram text safely: plain text by default, escape every dynamic value, recompute entity offsets, and smoke-test with hostile text."
---

# Send Telegram text safely

<!-- MUSE-ADAPT -->

## Muse adaptation — read first

This skill runs inside Muse's own environment, for Nasser. Where the original instructions below conflict with these points, these points win.

- Host: Linux VM (4 CPU, ~7 GB RAM, x86_64), no GPU. Toolchains live under the home directory only; never rely on system installs. For npm, always set npm_config_cache=/tmp/npm-cache.
- The user (Nasser) is Persian-speaking and phone-only; he has no computer. Deliverables reach him as files in this chat. Explain everything in simple Persian and translate every English label - his English is effectively zero.
- Register: two-way, comfortable, street-style, blunt and honest. No formalities.
- Never ask design-detail questions. Decide, build, then report shortly.
- For Nasser's own apps (Solina-Player, Solina-Launcher), follow the design decisions already recorded in memory (Material 3 Expressive, RTL Persian, Vazirmatn) and never copy another app's branding.
- UI copy: Persian first, Western (English) digits only, no em dashes in UI copy.
- Apply quality gates silently. Never paste internal gate or lint reports to the user; report outcomes in a few lines.
- Secrets never go into files, memory or chat output. Publishing anything publicly needs his explicit approval first.
- The original skill may name Claude Code tools (Read, Write, Edit, Glob, Grep, Bash). Use Muse's own tools instead (file read/write/edit, shell, browser). Use the browser tools for live pages and real-site screenshots.
- Video generation on this host is limited; never promise video output that a code-only path cannot deliver.


## Send plain text by default

- Send messages with no `parse_mode` unless the message genuinely needs formatting.

- Accept unstyled text as the safe default, the way the fake-address articles ship without `parse_mode`.

- Reserve formatting for labels and emphasis the user asked for, not for whole bodies of external text.

## Escape every dynamic value

- Escape all external and dynamic text before you interpolate it into a formatted message.

- Treat model names, prices, addresses, fortune text and API responses as hostile input.

- Use `HTML` parse mode and escape `&`, `<` and `>` when you need formatting, or apply the MarkdownV2 escape set to every special character.

- Never leave a lone underscore, asterisk or bracket from a data value inside legacy Markdown, because one unclosed marker breaks the whole message.

## Recompute entity offsets after any text change

- Compute message entities on the final text, after every edit, never on an earlier draft.

- Remember that Telegram counts entity offsets in UTF-16 code units, so emoji and other multi-byte characters shift them.

- Prefer inline formatting for simple cases over mixing entities produced by another library with your own text edits.

## Smoke test with hostile text

- Test each new template with text containing underscores, asterisks, square brackets, code fences, emoji and Persian RTL runs.

- Send the message exactly as the bot would before you deploy the template change.

- Read the API error when a send fails and fix the template instead of shipping a workaround.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Fall back to plain text in production when a formatted send fails: retry once without `parse_mode` so the user still gets the content, then fix the template.

- Keep user-facing text construction in one helper so escaping rules change in one place instead of in every handler.