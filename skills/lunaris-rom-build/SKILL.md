# Lunaris Custom ROM Build

## Settle the target and machine first

- Build Lunaris-AOSP version 3.13 on Android 16 for alioth, which is POCO F3 and Mi 11X and Redmi K40.

- Treat the work as a build and port from existing device trees, not a port from zero, because no 3.13 alioth build exists yet and the 3.12 trees are the base.

- Use hermes-server as the build machine only when the user says so, and warn plainly that it is below the usual minimums with 2 cores and about 7.6 GB RAM.

- Check disk and RAM before any long step with `df -h` and `free -h`, and stop when free disk falls below 20 GB because a full sync needs 250 to 400 GB free.

- Present every result to the user in simple Persian and translate every English label, because the user reads almost no English.

## Prepare the build environment

- Use Ubuntu 24.04 on hermes-server with git 2.43.0 and Python 3.12.3 and OpenJDK 17 and repo launcher 2.71 in `~/bin/repo`.

- Keep the 16 GB swap file at `/swapfile` active and registered in fstab, because the server has no swap by default and a ROM build runs out of RAM without it.

- Install all 33 AOSP build packages before the first sync, and recheck the install when a later step fails on a missing tool.

- Keep the work directory at `~/lunaris-3.13` and keep Vaultwarden and FreeLLMAPI running unless a build needs the RAM they use.

- Stop heavy services only for the build itself and restart them after, and tell the user which services were stopped.

## Sync the source and add the device trees

- Initialise the Lunaris manifest with `repo init -u https://github.com/Lunaris-AOSP/android -b 16.2 --git-lfs` and add `--depth=1` to the init for a shallow sync.

- Sync with `repo sync -c -j2 --force-sync --no-clone-bundle --no-tags` on this 2 core server, and run it in the background with a log at `~/lunaris-3.13/sync.log`.

- Never pass `--depth` to `repo sync`, because that flag belongs to `repo init` only and the sync fails at once when it is used there.

- Add the five Tsaritsa-Prjkt trees for alioth in `.repo/local_manifests/alioth.xml` with revision `lineage-23.2` for all five, because that is the only Android 16 branch common to device and common device and vendor and common vendor and kernel.

- Verify the five trees by name after the manifest is written, and sync again after any manifest change.

- Check a long sync once an hour with process state and folder size and the tail of the log, and stop the hourly check itself when the sync finishes or fails.

## Build for alioth

- Enter the source directory and run `. build/envsetup.sh` before any lunch or build command.

- Choose the target with `lunch lineage_alioth-bp4a-user` and note that the prefix is `lineage_` and not `lunaris_`.

- Build with `m bacon` after lunch succeeds, and build GMS with `WITH_GMS := true` plus the known Lunaris GMS settings from the build plan.

- Keep the build job count low on this server and keep ccache small or off, because a large ccache fills the disk and a high job count exhausts RAM.

- Expect the first build to take 12 to 24 hours or more on hermes-server, and say so before starting instead of promising a fast build.

- Treat the bacon build as untested until the first successful build, because sync and environment setup are verified and the build itself has not run yet.

## Diagnose failures and resume

- Read the failing stage from the log before changing anything, and fix only that stage instead of repeating the previous fix.

- Treat `[Errno 28] No space left on device` as a disk full failure, and resume the sync from the same directory after expanding the disk instead of deleting the downloaded source.

- When lunch fails with `hardware/dolby/dolby.mk does not exist`, know that the Lunaris 16.2 manifest has no dolby project and LineageOS ships no Dolby at all: the only reference is `device/xiaomi/sm8250-common/kona.mk:185`, which unconditionally inherits `hardware/dolby/dolby.mk`. Fix it by adding `hardware/dolby` from `crdroidandroid/android_hardware_dolby` at revision `16.0` to `.repo/local_manifests/alioth.xml` (dolby.mk at the repo root is verified), syncing just that project, and retrying lunch. The LineageOS and DerpFest repos under that name do not exist. A `LunarisDolby` branch also exists in the crDroid repo as a fallback.

- When lunch fails on a missing tree, do not fix one at a time: scan ALL inherit-product references in the device trees at once (grep for `$(call inherit-product,` in device/xiaomi/alioth and device/xiaomi/sm8250-common, then test each path's existence) so the full missing list is known before editing anything. For alioth the scan found only one more missing tree after Dolby: `packages/apps/GameBar/gamebar.mk` (kona.mk:212, "GameBar Performance Overlay"), fixed the same way from `crdroidandroid/android_packages_apps_GameBar` at revision `16.0`, path `packages/apps/GameBar` (gamebar.mk verified at the repo root; the LineageOS and Evolution-X repos under that name do not exist). Note the grep also matches a truncated `"$(SRC_TARGET_DIR"` artifact — check the real `$(SRC_TARGET_DIR)/product/...` paths separately, and ignore conditional `inherit-product-if-exists` references (e.g. miuicamera.mk) since they cannot break lunch.

- When services are stopped for a build that never starts, restart them right away: FreeLLMAPI and Vaultwarden with `docker start`, the Hermes dashboard with `systemctl --user start hermes-dashboard.service`, and the Hermes gateway with `hermes gateway ensure` (there is no gateway systemd unit, so the gateway runs manually and a stale gateway_state.json may need handling). Verify each one (docker ps healthy, dashboard HTTP 200 on 9119, `hermes status` shows the gateway running) before moving on.

- Disable ccache explicitly in the build command with `CCACHE_DISABLE=1`, because sourcing envsetup auto-enables it with a 40 GB limit even when the plan says to leave it off.

- The first bacon build for alioth started on 2026-11-08 (lunch succeeded: LUNARIS_VERSION 3.13, PLATFORM_VERSION 16, TARGET_PRODUCT lineage_alioth, user, arm64) with `m bacon` running detached under nohup (PID 303488), logging to `~/lunaris-3.13/build.log`, GMS environment exports set, services stopped for the build. Soong bootstrap reached 99% within 3 minutes with no errors. Expected duration 12–24+ hours on the 2-core server. After the build, restart FreeLLMAPI, Vaultwarden, the Hermes dashboard and the Hermes gateway before anything else, then verify the zip under `out/target/product/alioth/` and compute its SHA-256.

- The second bacon build FAILED on 2026-11-08 at ~10:58 UTC, after 2h04m, the same way: `Got signal: hangup`, `soong bootstrap failed with: signal: killed`, `FAILED: out/soong/build.lineage_alioth.ninja` — no zip produced. Swap was 100% full (31Gi used, 9Mi free) even with the second 16G swap file, so more swap alone does NOT fix Soong bootstrap on a 7.6G-RAM server: the bootstrap's memory use grew from 3.1G to 31G over two hours and kept going. Before a third attempt, change the approach instead of only adding swap: cap the Go heap with GOMEMLIMIT/GOGC for soong_build (it is a Go binary), and/or move the build to a machine with more real RAM (at least 16G). The hourly-check cron was removed after the failure and the services were restored and verified.

- The third bacon build started on 2026-11-08 at ~12:46 UTC (PID 3863, log ~/lunaris-3.13/build3.log) with GOMEMLIMIT=6GiB and GOGC=50 added to the same GMS exports — the Go heap cap for soong_build, chosen after the instance-type upgrade and the AWS plan upgrade both turned out to need a bank card the user does not have. After 180s it was alive ("Running globs..."), swap 3.3Gi/31Gi (~11%). Hourly-check cron lunaris-build-hourly-check re-created (every 1h). Expected 12–24h+. First hourly check ~1h10m in: still alive but log stuck at "Running globs...", swap already 22Gi/31Gi (71%) and climbing — GOMEMLIMIT=6GiB/GOGC=50 did NOT stop swap growth. Build 3 FAILED on 2026-11-08 at 14:54:32 UTC, after 2h06m, the same way: "soong bootstrap failed with: exit status 1", "Killed", "failed to build some targets (02:06:10)". No zip produced. Three builds, three OOM kills at Soong bootstrap on this 7.6G-RAM server — it cannot build this ROM; a bigger machine is needed. Services were restored and verified after the failure; the hourly-check cron was removed.

- The fourth build will run on a separate boxd machine (2026-11-08): solina-build, 4 vCPU/16G RAM, 400G data disk at /mnt/data, Ubuntu 24.04.5, SSH `ssh solina-build.boxd`; 35 AOSP packages, repo 2.71, 16G swap on the data disk; repo init (Lunaris 16.2) + local_manifest (Tsaritsa lineage-23.2, crDroid 16.0) done, sync running (PID 5349, log /mnt/data/lunaris-3.13/sync.log). Credit $4.99 may run out mid-build. Hourly-check cron lunaris-boxd-build-check starts build 4 automatically when the sync finishes. Commands on the machine run via `boxd machine exec solina-build -- <cmd>`; the boxd CLI is at ~/.local/bin/boxd.

- hardware/xiaomi is NOT in the Lunaris manifest; lunch auto-generates `.repo/local_manifests/roomservice.xml` from the device tree's `lineage.dependencies`, declaring `LineageOS/android_hardware_xiaomi` (no revision). Do NOT add hardware/xiaomi to alioth.xml — that causes a `duplicate path hardware/xiaomi` error on `repo sync`/`repo manifest`. If the tree is missing after a sync, run `repo sync hardware/xiaomi` (PATH must include ~/bin for the repo launcher). Build 4 (2026-11-08, boxd) failed after 1m04s at Soong bootstrap with `namespace hardware/xiaomi does not exist` because the sync predated the roomservice file; the fix above resolved it. The hourly-check cron was removed by the failing run. Build 4 retry started 2026-11-08 20:26 +0330 with the user's approval (PID 51709, log build4-retry.log, same GMS exports + CCACHE_DISABLE=1, no GOMEMLIMIT); 180s check: PID alive, lunch GMS confirmed, hardware/xiaomi in PRODUCT_SOONG_NAMESPACES, past the previous failure point; hourly-check cron recreated (build-only). Build 4 retry FAILED 2026-11-08 18:09:05 UTC after 1h11m52s: OOM 'Killed' at Soong bootstrap despite 16G real RAM + 16G swap (swap hit 100% during bootstrap) — same failure as builds 1–3; no zip. Soong bootstrap needs more than 16G RAM + 16G swap for this tree. Credit $4.01 left; hourly-check cron removed by the failing run.

- The sixth build (2026-11-09, boxd, user approved after a $25 credit grant brought the balance to $23.86): VINTF fix — added `<instance>dolby</instance>` to the android.hardware.media.c2 hal in hardware/dolby/dolby_framework_matrix.xml (already referenced by dolby.mk:31 via DEVICE_FRAMEWORK_COMPATIBILITY_MATRIX_FILE; the dolby instance is declared by device/xiaomi/sm8250-common/configs/vintf/c2_manifest_vendor.xml, while the framework matrices only cover default/software). The edit is local to the synced crDroid hardware/dolby repo (16.0) — a force-sync would wipe it, re-apply if that happens. Build 6 started (PID 1922336, log build6.log, same GMS exports + CCACHE_DISABLE=1, no GOMEMLIMIT); 180s check: lunch confirmed (lineage_alioth, BP4A.251205.006), Soong re-globbing, RAM 30/31Gi, disk 77G free. Hourly-check cron recreated (build-only). out/ was 99% built, so the retry should be fast. Build 6 SUCCEEDED 2026-11-09 03:29:48 UTC in 34m27s: zip Lunaris-AOSP-alioth-Community-3.13-GMS-2026110903.zip (2.3G, SHA-256 9a9536398eee3140a77eb086ac8cbaca5fd63490bc65a03bbaa1d665bea42cf0). Credit $23.24 after build. Hourly-check cron removed (verified gone). Flashing/testing still pending. Transfer to the user (2026-11-09): the user downloaded the zip himself directly from the server via https://solina-build.boxd.sh/Lunaris-AOSP-alioth-Community-3.13-GMS-2026110903.zip (temporary python http.server on solina-build:8000, stopped afterward); PixelDrain upload + Telegram link no longer needed. Lessons: boxd machine cp is unreliable for a 2.3GB file (attempt 1 died with h2 protocol error; attempt 2 killed after ~10 min with no visible progress — cp shows no progress and writes nothing until the end); boxd's subdomain proxy puts Cloudflare Turnstile in front — automated browsers cannot pass it (Error 600010, ~20 failed attempts) and curl cannot either; raw TCP proxy ports are blocked from this VM's egress; PixelDrain API upload requires an API key (anonymous PUT/POST both return 401). For future transfers, prefer the user downloading directly, or a PixelDrain API key.

- The fifth build runs on the same boxd machine resized (2026-11-08): `boxd new` failed with 'Without a payment method an organization can have 2 machines' (org already had solina-build + solina-boxd), so solina-build was resized with `boxd machine resize` on the stopped machine from 4 vCPU/16G to 8 vCPU/32G, same data disk, nothing deleted. Correction: machine size is NOT set only at creation — resize works on stopped machines. Build 5 started (PID 420, log build5.log, same GMS exports + CCACHE_DISABLE=1, no GOMEMLIMIT); 180s check: lunch GMS confirmed, Soong bootstrap Go compile 97% (138/141), RAM 31/31Gi, swap 4.2/32Gi (13%). Repo launcher auto-updated to 2.72. Credit $3.96 left. Hourly-check cron recreated (build-only). Build 5 FAILED 2026-11-09 00:28:49 UTC after 5h17m at 99% (208208/209862) — NOT OOM: VINTF check_vintf failed — android.hardware.media.c2@1.0::IComponentStore/dolby is in the device manifest but not in the framework compatibility matrix (build5.log:266199). Fix: add the Dolby C2 HAL to a framework compatibility matrix (FCM >= 7) or remove the dolby instance from the device manifest. out/ is 99% built, so a retry after the fix reuses almost everything. Credit -$0.53 (negative) — machine may suspend at any moment; connect a payment method before any rebuild. Hourly-check cron removed by the failing run.

- Temporary instance-type upgrade is BLOCKED on this account (2026-11-08): the account is on an AWS free plan; the EC2 console only offers free-plan eligible types and CloudShell `modify-instance-attribute` fails with FreeTierRestrictionError ("This operation is not available for free plan accounts. To perform this action, please upgrade your account plan."). Do not retry the same change — it needs an account plan upgrade, a payment/account change the user must explicitly approve. Plan upgrade attempt 2026-11-08: Billing shows the account on plan "Free" (178 days left to 2027-05-04, $189.93 credits, $0 due). The upgrade itself is free and keeps the credits, but completing it requires adding a payment method — the user has no bank card, so it cannot be completed. The card-free fallback is the Go memory limit retry on the current server. After any server stop/start, the Hermes gateway does NOT come back on its own and needs `hermes gateway ensure`; FreeLLMAPI, Vaultwarden, the dashboard, sing-box and x-ui all come back on their own.

- Keep the 119 GB already downloaded when a sync fails on disk space, because a resumed sync continues from that data and does not start from zero.

- Do not claim that freeing a few gigabytes fixes a full disk, because the sync needs far more space than a small cleanup gives.

- Check the exact error text in the log when a build fails, and re-read the changed file from disk after every fix before starting the next run.

- Record the commit hash and the run outcome for every change, so the user can match a built file to the exact source that produced it.

## Test the finished build

- Never flash from the server, because flashing needs a USB connection from a computer to the phone and the server can only build and download the file.

- Tell the user to back up the phone fully and use OrangeFox or TWRP for alioth with an unlocked bootloader and firmware 1.0.2 TKHMIXM before a clean flash.

- Ask the user to test boot and Wi-Fi and SIM and camera and fingerprint and sound and Dolby and Leica Camera and battery after flashing, and collect the exact failure report for any item that does not work.

- Treat a failed test item as the next build task, and fix one item at a time with a new build instead of changing many things at once.

- Ship the final zip with a changelog and a SHA-256 hash, and name the GMS or Vanilla variant plainly in the file name.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for reading the Lunaris manifest and the Tsaritsa-Prjkt device trees and for checking commits and branches.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [GitHub](https://github.com/Lunaris-AOSP/android) for the Lunaris manifest and the build README. Carry the branch 16.2 and the exact init and lunch and bacon commands into any browser task and verify the file saved there.

- [GitHub](https://github.com/Tsaritsa-Prjkt) for the five alioth device trees. Carry the revision lineage-23.2 into any browser task and verify each tree exists before adding it to the manifest.

## Alternatives for better results

- Build on a stronger machine with at least 16 GB RAM and 8 cores and 300 GB free SSD when the user accepts it, because the first build is far faster and far less likely to run out of RAM or disk.

- Sync the source once and reuse it for later builds, because a full sync takes hours and a later build only needs the changed files.

- Ask one question when the GMS choice or the build machine or the lunch target is unclear, and let that answer decide the next step.
