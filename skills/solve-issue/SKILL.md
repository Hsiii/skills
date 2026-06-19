---
name: solve-issue
description: "Run one GitHub issue loop from an explicit task packet containing issue, repo, mode, implementation ponytail thread, review ponytail thread, artifact paths, pass marker, and stop protocol. Implement, verify, call $pr, then heartbeat until review passes. Use when $solve-issues hands off one open issue labeled ready or when the user provides one complete task packet."
---

# Solve Issue

Input: one task packet from `$solve-issues`. Do not fetch queues or infer context.

Implementation thread:

1. Read the issue, comments, linked PRs, and relevant code.
2. Implement, verify with repo checks, and capture before/after media for user-facing changes.
3. Use `$pr` with the supplied mode.
4. After `$pr` returns a PR URL or writes `DRAFT.md`, start review.
5. Heartbeat until the review thread returns the pass marker; resolve comments as they arrive.

Review thread:

1. Internal: review the draft GitHub PR and comment on it.
2. External: review `DRAFT.md` and write gitignored `REVIEW.md`.
3. Write actionable comments or `PASS`.
4. On `PASS`, send the implementation thread the stop message from the task packet.
