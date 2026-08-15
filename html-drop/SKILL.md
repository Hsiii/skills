---
name: html-drop
description: Create and manage self-contained HTML artifacts. Use when the user requests an HTML artifact or sends `html`, `html+`, or `html-`.
---

# HTML Drop

Convert the latest relevant deliverable unless another source is specified.

Create one self-contained, mobile-readable HTML file. Use inline CSS and only add inline JavaScript when it materially helps. Never include secrets, private URLs, local paths, or external scripts.

For UI variants, render the actual alternatives together and label them `A`, `B`, `C`...

- For `html`, write the file and report its absolute path.
- For `html+`, create the file, then use the forward-port skill to publish it. Report the path and URL.
- For `html-`, use the forward-port skill to close its preview, then remove its disposable HTML file. Ask which preview only when ambiguous.

Keep the same file across live-preview iterations. Remove it after `html-`, another explicit cleanup request, or a confirmed merge of its associated PR.
