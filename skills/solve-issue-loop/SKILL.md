---
name: solve-issue-loop
description: "Run the user's issue-building loops for GitHub issues: auto-determine internal vs external repo mode, process ready issues, implement and verify fixes, use $pr for PR output, and run heartbeat review loops. Use when the user says \"solve issue\", \"building loops\", asks Codex to process ready issues, or wants issue-to-PR automation."
---

# Solve Issue Loop

Auto-determine mode: internal for the user's own repos; external otherwise. Ask only if ownership is ambiguous.

For each `ready` issue:

1. Spin up a ponytail thread for implementation.
2. Read the issue, comments, linked PRs, and relevant code.
3. Implement, verify with repo checks, and capture before/after media for user-facing changes.
4. Use `$pr` in the matching mode.
5. Enter heartbeat mode: resolve review comments until review passes, then stop.

Internal mode: `$pr` creates a real draft GitHub PR, then a second ponytail thread reviews the PR and comments on it. Stop when that reviewer passes and signal the implementation thread to stop.

External mode: `$pr` writes gitignored `DRAFT.md` plus prepared media instead of opening a GitHub PR. A second ponytail thread reviews `DRAFT.md` into gitignored `REVIEW.md`. Stop when review passes and signal the implementation thread to stop.
