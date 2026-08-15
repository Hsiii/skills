---
name: forward-port
description: Manage Cloudflare Quick Tunnels for local HTTP ports. Use when the user asks to expose, inspect, or stop localhost forwarding, including `html+` and `html-` workflows.
---

# Forward Port

Run the bundled script:

```text
scripts/forward-port [port]
scripts/forward-port --file <html-file> [preview-name]
```

Use the repository name for ports and a short task-specific preview name for HTML when concurrent artifacts need separate URLs. Keep the command running and retain its execution session. Treat the reported `quick_url` as public. Close the exact session when asked or after its associated PR is confirmed merged.
