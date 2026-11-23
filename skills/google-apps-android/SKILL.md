---
name: google-apps-android
description: Help manage and integrate Google apps on Android, including Gmail, Drive, Maps, Photos, Calendar, Contacts, Chrome and Play services, through available authorized device or API tools.
---

# Google Apps on Android

Determine whether the request is to operate an installed app on the phone, access cloud data through an official API, or build an integration. These are not interchangeable.

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

- For local app operation, use an explicitly connected device/browser/accessibility tool and user-visible controls.
- For cloud data, use official APIs/connectors with OAuth scopes and consent.
- For Chrome, respect profile boundaries, password-manager protections, downloads and signed-in account separation.
- For Play Store and Play services, distinguish app installation, updates, integrity, billing and developer publishing.
- For Gmail/Drive/Calendar/Contacts/Photos, minimize access and confirm outbound or destructive actions.
- Do not claim access to all Google account data merely because one Google account is signed in on Android.
