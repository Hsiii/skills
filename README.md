# Skills

Three small Codex skills for GitHub issue-building loops.

## Skills

- `solve-issue`: triggered by "solve issue" or "building loops"; fetches `ready` issues, determines internal/external mode, creates two ponytail threads per issue, and calls `$solve-issue-loop`.
- `solve-issue-loop`: runs one issue only; it receives the issue, mode, implementation thread, and review thread, then coordinates implementation and review heartbeat until pass.
- `pr`: triggered by "pr"; internal mode uses the repo template and Yeet to create a real draft PR, while external mode writes gitignored `DRAFT.md` and media without opening a GitHub PR.

## Why

The orchestrator owns issue queues. The loop skill owns only one two-thread interaction. The PR skill owns maintainer-focused PR output, so internal repos can publish draft PRs while external repos can prepare reviewable drafts safely.
