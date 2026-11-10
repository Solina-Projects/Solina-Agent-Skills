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
