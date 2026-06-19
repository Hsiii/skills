---
name: solve-issue
description: "Orchestrate GitHub ready issue processing: auto-determine internal vs external repo mode, fetch ready issues, create two ponytail threads per issue, and call $solve-issue-loop for each issue. Use when the user says \"solve issue\", \"building loops\", asks to process ready issues, or wants issue-to-PR automation."
---

# Solve Issue

Auto-determine mode once per repo: internal for the user's own repos; external otherwise. Ask only if ownership is ambiguous.

For each `ready` issue:

1. Fetch the issue and determine the mode.
2. Create two ponytail threads: implementation and review.
3. Call `$solve-issue-loop` with only the issue, mode, implementation thread, and review thread.
4. Move to the next ready issue only after that loop stops.

Do not implement inside this skill; it only schedules isolated per-issue loops.
