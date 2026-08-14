---
name: forward-port
description: Manage Cloudflare Quick Tunnels for local HTTP ports. Use when the user asks to expose, inspect, or stop localhost forwarding, including `html+` and `html-` workflows.
---

# Forward Port

Run the bundled script:

```text
scripts/forward-port publish <html-file> [project-name]
scripts/forward-port start <port> [project-name]
scripts/forward-port status [project-name]
scripts/forward-port stop [project-name]
```

Use `publish` for HTML artifacts; it manages the file, port, preview reuse, and tunnel. Treat the URL as public. Report `artifact_path` and `dev_url` when emitted; otherwise report `quick_url`.

Keep previews running across iterations. Stop one when asked or after its associated PR is confirmed merged. `stop` verifies recorded processes before stopping them and moves managed artifacts into recoverable temporary trash.
