---
name: custom-rom-development
description: Research, build, bring up, debug and validate AOSP-based custom Android ROMs, kernels, recoveries, device trees and vendor integrations.
---

# Custom ROM Development

## Identify the exact target
Record device codename, board/platform, SoC, region/carrier variant, current firmware/build fingerprint, bootloader state, partition layout (A/B, dynamic partitions, retrofit), kernel version and Android base. Never assume two retail variants are interchangeable.

## Source and build
- Prefer official AOSP and maintained device/vendor/kernel sources; verify branch compatibility, manifests, commit history and licenses.
- Inspect repo manifests, lunch targets, build environment, toolchain, proprietary blob extraction requirements and documented build instructions.
- Keep local modifications in tracked patches/branches; document provenance of proprietary blobs.
- Build reproducibly where possible and capture environment, commands, logs and artifact hashes.

## Bring-up and debugging
Investigate boot chains, AVB/vbmeta, boot/vendor_boot/init_boot, fstab, SELinux policy, init services, HALs, VINTF, overlays, kernel modules, device permissions, radio, camera, audio, sensors, graphics and power.
Use logcat, dmesg, tombstones, bugreports and kernel logs only with authorized access; redact identifiers and secrets before sharing.

## Flashing safety
- Verify exact device codename and image compatibility, checksum, slot, partition names and recovery path.
- Explain bootloader unlock data wipe and warranty/security implications.
- Require explicit confirmation before unlock, erase, format, sideload or flash.
- Never recommend flashing an image intended for a different device variant.
- Preserve a recovery/rollback plan and verify backups before destructive steps.

## Output
Provide source references, reproducible commands, known hardware limitations, test matrix and recovery instructions. Do not promise a successful boot without device validation.
