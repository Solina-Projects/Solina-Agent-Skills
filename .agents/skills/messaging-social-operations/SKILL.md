---
name: messaging-social-operations
description: Coordinate user-authorized tasks across Telegram, WhatsApp, Instagram and other messaging/social apps while protecting privacy and preventing unintended sends or posts.
---

# Messaging and Social Operations

## Capability check
Identify the app, account type and available authorized connector/API. UI access, notifications, accessibility and official APIs are different capabilities; never imply that one grants the others.

## Private data
Read only the conversations, contacts, media or account data explicitly requested. Do not perform broad inbox surveillance, export entire contact books or infer sensitive traits. Summarize minimally and avoid retaining personal data unnecessarily.

## Outbound actions
Before sending a message, posting content, replying, forwarding, inviting members or deleting content, present the destination/account, exact content and attachments and request confirmation. For recurring or bulk sends, require explicit scope, opt-in evidence, schedule and stop conditions.

## Automation boundaries
Respect platform terms, API permissions, rate limits and anti-spam rules. No stealth monitoring, credential/session theft, impersonation, mass unsolicited messaging or bypass of MFA/CAPTCHA.

## Audit trail
Record only the minimum operational metadata needed. Report sent/failed/pending distinctly and verify delivery status where the platform exposes it.
