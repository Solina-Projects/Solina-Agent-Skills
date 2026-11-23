---
name: persian-rtl-design
description: Persian-first and RTL design rules for Nasser's products (Telegram mini-app, bot UI, apps, sites, artifacts). Use on every build whose UI carries Persian or Arabic-script text: RTL layout, mirroring, Arabic-script typography, mixed fa/en runs, digits, and the pre-delivery RTL checklist.
---


# persian-rtl-design

Written for Muse from Nasser's own products and corrections. His products are Persian-first; none of the generic design skills know RTL. Apply this skill on every Persian-carrying build, after design direction (DESIGN.md, Hallmark) and before the antislop gate.

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


## Direction and layout
- Set `dir="rtl"` and `lang="fa"` at the root of Persian surfaces. Design in logical direction from the start; never build LTR and flip at the end.
- Use CSS logical properties everywhere: `margin-inline-start/end`, `padding-inline-*`, `inset-inline-*`, `border-start-start-radius` and friends, `text-align: start/end`. Physical left/right in a Persian UI is a bug waiting for the mirror test.
- Flex and grid follow direction automatically when direction is set; absolute positioning must use inset-inline properties or explicit transforms.
- Progress indicators, timelines and step flows run right to left. Sliders and carousels move in reading direction.

## Mirroring rules
- Flip: back/forward arrows, chevrons, reply and send affordances, breadcrumbs, indentation, list markers.
- Never flip: clocks and time, play/pause and media transport, logos and brand marks, numbers and charts' data axes meaning, phone keypads, the hamyar robot and character art.
- Icons that imply reading direction (text lines, documents) mirror; symmetric icons stay.

## Arabic-script typography
- Display font for Nasser: Lalezar. Body: Vazirmatn or Readex Pro; fall back to a system Arabic-script sans, never to a Latin-only font for Persian text.
- Line height for Arabic script: 1.8 to 2.0. Latin defaults (1.4 to 1.5) clip ascenders and dots.
- Never apply letter-spacing to Arabic-script text; it disconnects joined letters. Tracking is for Latin labels only.
- Avoid kashida justification; use ragged start alignment.
- Persian copy uses ZWNJ where the orthography needs it (می‌شود، خانه‌ها); do not strip ZWNJ from strings, and do not let code formatters join words across it.
- Arabic text is never translated for Nasser; he reads Arabic. Render it as-is with the same typography rules.

## Mixed-direction content
- User-generated or foreign runs inside Persian text get `dir="auto"` or an isolating wrapper (`<bdi>`, `unicode-bidi: isolate`); otherwise punctuation and numbers jump to the wrong end of the line.
- Emails, URLs, phone numbers, codes and Latin brand names stay LTR inside RTL text: wrap them with `dir="ltr"` and keep them visually grouped.
- Inputs for email, phone, OTP and links are LTR fields even in an RTL form; text inputs for Persian stay RTL.

## Numbers and data
- UI digits are Western/English (1,000,000) by Nasser's explicit standing rule; Persian digits in UI were rejected and reverted. Use tabular figures for prices and counters so columns do not wobble.
- Thousand separators on long numbers; currency and unit sit after the number in reading order (price first, then unit label), matching his price lists.
- Dates in his products follow the mini-app convention already shipped; when unsure, mirror the existing screen instead of inventing a format.

## Telegram WebView realities (his client)
- His modded Telegram client renders JS-driven transitions as glitches: animations are transform and opacity only, exactly as DESIGN.md says.
- Judge every Persian layout on a phone-width viewport first; his verdict device is his Android phone, not a desktop preview.
- Bottom bars and tab bars are RTL-ordered (first tab at the right); selection indicators must track inline direction.

## Pre-delivery RTL checklist
1. Root has dir=rtl and lang=fa; no physical left/right remains in new CSS.
2. Back chevrons point right (toward the start edge); forward actions point left.
3. One mixed line tested: Persian + a Latin brand + a number + punctuation; nothing jumps.
4. Arabic-script text has no letter-spacing and line height at least 1.8.
5. Digits render Western and tabular in prices and counters.
6. Screenshot at phone width checked for overflow, clipped dots and mirrored-by-mistake icons.
