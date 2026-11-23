---
name: tiktok-photo-edit-codes
description: "Treat a short code sent with a photo as an instruction to edit that photo: separate subject from effect, handle unverified codes carefully, and deliver the edited still photo."
---

# TikTok Photo Edit Codes

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


## Treat the code as a photo edit

- Treat a short code sent with a photo as an instruction to edit that photo.

- Edit the original pixels and change only what the code specifies.

- Return a still photo rather than a video or a regenerated image.

## Separate the subject from the effect

- Separate the subject from the background before you apply any effect.

- Apply the effect only to the region the code names.

- Keep the subject sharp and unchanged for a background only effect.

- Compare the result with the original and confirm that every unchanged area still matches.

## Handle an unverified code carefully

- Apply horizontal motion blur to the background only when the code is /whipmotion.

- State the effect and the region you plan to change before you edit a code you have not verified.

- Ask the user to confirm that reading when the effect or the region is unclear.

- Wait for confirmation instead of inventing an effect for an unknown code.

## Deliver the edited photo

- Return the edited photo itself.

- Describe the effect you applied and the region it changed in one short sentence.

- Name the parts of the photo you left unchanged.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Ask for a reference image when a code is ambiguous and use it only to clarify the effect and the region.

- Offer a weaker or stronger version of the same effect after the first result when the user wants adjustment.
