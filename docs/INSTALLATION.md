# Installation Guide

This repository stores portable Agent Skills. It does not install software or grant permissions by itself.

## 1. Use with a compatible agent

Copy only the skill folders you need into the skill directory documented by your agent. Skill discovery paths differ between products and versions; verify the current official documentation before copying. Keep each folder name identical to the `name` in its `SKILL.md` frontmatter.

Typical layout:

```text
<agent-skill-root>/
  android-engineering/
    SKILL.md
  phone-device-control/
    SKILL.md
```

The repository uses `.agents/skills/` as its source-of-truth collection. Do not assume every client automatically discovers that repository path.

## 2. Android phone control

For local development and authorized device testing, install Android Platform Tools on a trusted computer or Termux environment. Enable Developer options and USB debugging only when needed. Pair/authorize the device through Android's on-screen prompt.

Verify the connection with:

```sh
adb devices
adb shell getprop ro.product.model
adb shell getprop ro.build.version.release
```

On Android, Termux does not automatically have unrestricted access to other apps or protected app data. ADB over wireless debugging requires pairing and user approval. Root access changes the risk profile and should not be used by default.

## 3. Browser and app automation

Use a supported, explicitly connected browser or test automation framework. For app testing, prefer UIAutomator/Appium or Android intents. Accessibility automation must be visible, consent-based and limited to the task.

## 4. Google and social platforms

Use official OAuth/API integrations with the minimum required scopes. Google account login, a Google AI subscription and API access are separate entitlements. WhatsApp and Instagram API features depend on account type, app review, permissions and platform policy. Telegram bot tokens belong in a secret manager, never in repository files.

## 5. Secrets and permissions

Never commit passwords, access tokens, cookies, recovery codes, signing keys or keystores. Use GitHub Actions secrets for CI credentials and rotate any credential that is accidentally exposed.

## 6. Validate locally

```sh
python3 scripts/validate_skills.py
```

The GitHub Actions workflow runs the same structural check on pushes and pull requests to the default branch.
