---
name: selfbot-feature-release
description: "Release a new trigger for the Telegram selfbot: register the handler, restart the service, smoke-test the literal trigger, and bump the version and changelog."
---

# Selfbot feature release

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

Skill-specific note: No selfbot is set up in this environment (no bot.py, no selfbot.service unit). Only use this skill when Nasser asks to build or change a selfbot.


## Register every new trigger

- Define the handler and register it with `add_event_handler` in the same edit, never in a follow up.

- Search bot.py for the new trigger text and for its `add_event_handler` call after each edit, and confirm both exist before you restart anything.

- Keep the trigger prefix consistent with the current convention. Since v3.9.0 every selfbot trigger starts with `!` because some channels block `/`.

- When you rewrite a trigger, update both the definition and the registration. A stale registration on the old prefix leaves the new one silent.

## Restart and smoke-test the literal trigger

- Restart the `selfbot.service` systemd unit over SSH, recreating the proxy script from `~/workspace/system/ssh-proxy.py` when the ephemeral copy is missing.

- Invoke each new trigger exactly as a user would, using the exact text including the prefix, in the same chat type it is meant for.

- Treat silence as a failure. Recheck the registration and the service logs before you ask the user to try it.

- Delete the test messages you sent so the test leaves nothing behind.

## Bump the version and the changelog

- Bump VERSION and add a CHANGELOG entry for every bot.py change, with no exceptions.

- Tell the user the feature is live only after the smoke test passes.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Batch several new triggers into one restart to cut deploy cycles and reduce the chance of testing the wrong build.

- Smoke-test each chat type you intend to support when a trigger must work in pv, group and channel chats.