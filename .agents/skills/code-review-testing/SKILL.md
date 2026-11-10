---
name: code-review-testing
description: Review code, diagnose defects, design tests and verify correctness, security, performance and release readiness.
---

# Code Review and Testing

Prioritize findings by severity and impact. Cite file paths and line ranges where available. Explain reproducible conditions and practical fixes.

Review for correctness, edge cases, race conditions, lifecycle/resource leaks, input validation, authorization, privacy, cryptography misuse, dependency risk, performance, accessibility and maintainability.

Testing strategy:
- Unit tests for deterministic logic.
- Integration tests for boundaries, persistence and network behavior.
- UI/end-to-end tests for critical user journeys.
- Regression tests for each fixed defect.
- Negative tests for permissions, invalid input, offline state and failure recovery.

Do not label a suspected issue as confirmed without evidence. Do not claim tests ran unless the tool output shows it. Avoid destructive test data and production actions.
