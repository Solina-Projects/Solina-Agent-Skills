---
name: phone-device-control
description: Operate and troubleshoot Android phones through explicitly connected ADB, device-management, accessibility or automation tools, including settings, files, apps and system diagnostics.
---

# Phone and Android Device Control

## Establish the control path
- First determine which capability is actually available: ADB over USB/Wi-Fi, Android Debug Bridge in a local shell, an approved device-management API, accessibility automation, or a user-guided procedure.
- Confirm device identity/model, Android version, connection state and the scope of access before acting.
- Distinguish read-only inspection from changes. Start read-only and explain any permission or pairing step that the user must complete.
- A GitHub skill or chat instruction does not create a live connection to the user's handset.

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

## Safe operations
- Read device properties, app/package inventory, storage status, logs and connectivity only through available authorized tools.
- For settings changes, state the exact setting and expected effect; obtain confirmation for sensitive changes.
- Before install/uninstall, app-data clearing, file overwrite/deletion, factory reset, bootloader unlock, partition writes or flashing, explain impact and obtain explicit confirmation.
- Back up relevant data and verify device/variant/slot before firmware or partition operations.
- Never disable screen lock, Play Protect, verified boot, SELinux, encryption, anti-theft or security updates as a convenience.
- Do not extract app-private data, tokens, notifications or personal messages without a specific legitimate purpose and explicit authorization.

## Accessibility and UI automation
- Use accessibility services only with clear user consent and a legitimate task.
- Avoid hidden/background surveillance, keylogging, stealth capture, covert recording or bypassing Android permission prompts.
- Prefer official intents, documented APIs and user-visible controls over brittle screen-coordinate automation.
- Stop and ask when an action could send, publish, delete, purchase, change account security or disclose private data.

## Reporting
Separate actions completed, actions attempted but blocked, and instructions requiring user action. Never imply full-phone control unless a working authorized device tool is connected.
