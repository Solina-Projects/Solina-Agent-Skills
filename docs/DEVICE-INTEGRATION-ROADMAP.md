# Device Integration Roadmap

## Goal

Connect an agent to an Android device through an explicit, auditable control channel without confusing skill instructions with actual permissions.

## Phase A — Read-only baseline

- Install/verify Android Platform Tools.
- Pair ADB over USB or Android Wireless Debugging.
- Capture model, codename, Android version, build fingerprint and ABI.
- Confirm the connected serial and test read-only commands.
- Keep logs private and redact identifiers before sharing.

## Phase B — Controlled operations

Add and test one capability at a time:
- Launch an app using package/activity information.
- Read basic device diagnostics and logcat.
- Transfer files only to user-selected locations.
- Install a known APK after verifying its source and checksum.
- Use UIAutomator/Appium for repeatable app testing.

Require confirmation before uninstalling apps, clearing data, changing security settings, sending messages, publishing content, deleting files or flashing partitions.

## Phase C — Root-only capabilities (optional)

Root is not required for normal ADB/app testing. If a task genuinely requires root, document the exact command, target path, expected effect, rollback and backup first. Never disable verified boot, SELinux, encryption or other protections as a default workaround.

## Phase D — Messaging and cloud services

Connect each platform separately through its supported connector or official API. Start read-only, request minimum scopes, then add narrowly scoped write actions with confirmation gates. Do not scrape private app databases or automate personal accounts through unsupported interfaces.

## Acceptance criteria

- Device identity is verified before every device-specific operation.
- Read and write permissions are separated.
- Destructive actions require explicit confirmation.
- No secrets or private message contents appear in CI logs.
- Every operation reports verified success, failure or user action required.
