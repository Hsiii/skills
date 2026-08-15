---
name: forward-port
description: Manage Cloudflare Quick Tunnels for local HTTP ports. Use when the user asks to expose, inspect, or stop localhost forwarding, including `html+` and `html-` workflows.
---

# Forward Port

Run the bundled script:

```text
scripts/forward-port [port] [project-name]
scripts/forward-port --file <html-file> [project-name]
```

Keep the command running and retain its execution session. Treat the URL as public. Report `dev_url` when emitted; otherwise report `quick_url`. Close the exact session when asked or after its associated PR is confirmed merged.
