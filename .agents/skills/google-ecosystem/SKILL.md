---
name: google-ecosystem
description: Help integrate and operate Google services and Android apps such as Gmail, Drive, Calendar, Contacts, Photos, Maps, Play services and Google account workflows.
---

# Google Ecosystem

## Choose the correct interface
Prefer official Google APIs, supported connectors and Android intents. Identify whether the task concerns a personal Google account, Workspace account, Android app, or developer project. Do not assume a Gmail subscription grants API access or OAuth scopes.

## Authentication and data
- Use OAuth consent and the minimum required scopes; explain what data each scope exposes.
- Never request passwords, one-time codes, backup codes, cookies or refresh tokens in chat.
- Keep client secrets and service-account keys out of source control; use secure secret storage.
- Respect user consent, Workspace admin policies, API quotas, data retention and deletion requirements.

## Service guidance
- Gmail: use supported Gmail API or connected mail tools; distinguish reading, drafting, sending and deleting.
- Drive: preserve ownership/sharing permissions; confirm before moving, deleting or externally sharing.
- Calendar: confirm attendees, timezone, visibility and invitation side effects before creating or changing events.
- Contacts/Photos: treat personal data as sensitive; limit retrieval and sharing to the requested scope.
- Maps/Location: request location only when necessary; do not infer precise location from unrelated signals.
- Play services/Play Store: distinguish app distribution, Play Integrity, billing and account policy constraints.

## Verify
Check API availability, OAuth scopes, account type and current platform limitations against official documentation. Clearly state when an action needs user approval or cannot be performed by the available connector.
