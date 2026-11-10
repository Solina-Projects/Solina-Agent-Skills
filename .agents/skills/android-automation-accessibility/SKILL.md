---
name: android-automation-accessibility
description: Design and use Android automation through intents, ADB, UIAutomator, Appium, MacroDroid or accessibility services with visible consent and safe action gates.
---

# Android Automation and Accessibility

Choose the least invasive mechanism that reliably performs the task:
1. Android intents/deep links and official APIs.
2. ADB for developer-authorized device workflows.
3. UIAutomator/Appium for test automation.
4. Accessibility services only for user-facing assistive or explicitly consented automation.

Document required permissions, Android version limitations and setup steps. Never hide the service's operation, capture keystrokes, intercept credentials, record calls, bypass permission dialogs or collect notifications/messages in the background without clear authorization.

For every action, classify read/write and reversible/destructive. Ask confirmation before sending, posting, deleting, purchasing, installing unknown APKs, changing security settings or modifying system partitions. Keep logs free of personal message content and tokens.
