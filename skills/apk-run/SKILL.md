---
name: apk-run
description: |
  Run an APK file end-to-end: static checks on this VM, then install, launch,
  screenshot and logcat-crash-check on the user's POCO F3 through phone-harness
  on hermes-server. Use whenever the user asks to run, test or check an APK,
  or asks whether an APK launches / crashes / shows its UI.
---

# APK Run

## Why this skill exists

There is NO local Android emulator on this VM, and there cannot be one:

- No `/dev/kvm`, no vmx/svm CPU flags — no hardware virtualization.
- Only ~700 MB RAM free — an emulator guest needs 1.5 GB+.
- Software emulation would be unusably slow and would OOM.

So "running an APK" means: static checks here + install and run on the
user's real phone (POCO F3, <device-codename>) via phone-harness on hermes-server.
That is a real device test, which is better than an emulator anyway.

## Route

```
APK file/URL
  -> static checks on this VM (aapt2, apksigner, zipalign, dexdump)
  -> hermes-server (<server-ip>, via EC2 Instance Connect in the browser)
  -> ~/apk-run.sh <apk-url-or-path>
  -> adb install on POCO F3 (through the Termux reverse tunnel)
  -> launch, wait, screencap, logcat crash check
  -> screenshot + verdict back to the user
```

## Prerequisite — the phone link

The phone must be connected before any run. The user does this on the phone:

1. Termux: run `sshd`
2. Termux: `ssh -i ~/.ssh/server-key -R 8022:127.0.0.1:8022 ubuntu@<server-ip>`
3. Keep the Termux session open. The link dies if Termux closes, the phone
   sleeps, Wi-Fi drops, or the phone reboots (wireless debugging turns off).

On the server, verify first: `adb devices` must list the phone, and
`phone-harness doctor android` must be all clear. If the phone is not
listed, STOP and tell the user to reconnect — do not keep retrying.

## Static checks (this VM, before any install)

SDK tools live in `~/android-sdk` (build-tools 37.0.0, platform-tools):

```bash
AAPT=~/android-sdk/build-tools/37.0.0/aapt2
APKSIGNER=~/android-sdk/build-tools/37.0.0/apksigner
ZIPALIGN=~/android-sdk/build-tools/37.0.0/zipalign

$AAPT dump badging app.apk | head -20   # package, version, minSdk, permissions
$APKSIGNER verify --verbose app.apk      # signature OK?
$ZIPALIGN -c -v 4 app.apk | tail -3      # 4-byte alignment (install error -124 if bad)
~/android-sdk/build-tools/37.0.0/dexdump -d classes.dex | head  # dex sanity
```

Also check: `unzip -l app.apk` — native `.so` files must be stored
uncompressed (compress_type 0) and 4-byte aligned, or Android 11+ refuses
to install / load them. Verify with python zipfile: `info.compress_type`
and `info.header_offset % 4 == 0` for every `.so` and `resources.arsc`.

For a crash whose cause is in smali (e.g. VerifyError), assemble the full
smali tree locally with smali 2.5.2 and baksmali-round-trip it to verify the
fix, the same way the CF-Bridge VerifyError was fixed.

## The server script — ~/apk-run.sh

Created on hermes-server via a browser task. Usage:

```bash
~/apk-run.sh <apk-url-or-local-path> [package-name]
```

What it does:

1. Downloads the APK if given a URL (curl, GitHub release assets work).
2. Runs `adb devices`; exits with a clear message if the phone is missing.
3. `adb install -r <apk>` — reports install errors verbatim (e.g. -124).
4. Finds the launcher activity (`aapt2 dump badging | grep launchable-activity`)
   and launches it (`adb shell am start -n <pkg>/<activity>`), or falls back
   to `adb shell monkey -p <pkg> -c android.intent.category.LAUNCHER 1`.
5. Sleeps 8 seconds, then `adb exec-out screencap -p > /tmp/apk-run-<pkg>.png`.
6. Crash check: `adb logcat -d -t 2000 | grep -iE "FATAL EXCEPTION|AndroidRuntime|VerifyError"`
   scoped to the app pid; prints matching lines or "no crash".
7. Prints: package, version, install result, launch result, crash lines,
   screenshot path. The screenshot is then shown to the user.

## Reporting to the user (simple Persian)

- Say plainly: installed or not, launched or not, crashed or not.
- Show the screenshot. Do NOT claim the app "works" from a single launch —
  say what was actually seen (home screen visible / crash dialog / black screen).
- Never send the APK file itself in chat — GitHub Actions run link or
  release link only, per his standing rule for his own apps.
- If the phone is not connected, tell him the one step: open Termux and
  start the tunnel — do not pretend the run happened.

## Limits

- One Android version only: whatever the POCO F3 runs. Multi-version
  testing needs Firebase Test Lab (free Spark: 10 virtual + 5 physical
  runs/day; deprecated, shuts down 2027-09-30) or Appetize.io (free:
  30 min/month, 3-minute sessions) — neither is set up yet.
- The tunnel is fragile: phone sleep / Wi-Fi drop / reboot kills it.
- First launch after install can be slow; wait at least 8 s before the
  screenshot, 15 s for heavy apps.
