---
name: solve-issue-loop
description: "Run one GitHub issue loop using an explicit issue, mode, implementation ponytail thread, and review ponytail thread. Implement, verify, call $pr, then heartbeat until review passes. Use when $solve-issue hands off a single ready issue or when the user explicitly provides one issue plus the two threads."
---

# Solve Issue Loop

Inputs: one issue, mode (`internal` or `external`), implementation thread, review thread.

Implementation thread:

1. Read the issue, comments, linked PRs, and relevant code.
2. Implement, verify with repo checks, and capture before/after media for user-facing changes.
3. Use `$pr` with the supplied mode.
4. Enter heartbeat mode and resolve review comments until review passes.

Review thread:

1. Internal: review the draft GitHub PR and comment on it.
2. External: review `DRAFT.md` and write gitignored `REVIEW.md`.
3. When review passes, signal the implementation thread to stop.
