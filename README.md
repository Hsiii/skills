# Skills

Small, focused skills for Codex.

## Design

`design` routes interface and product design work to the smallest useful set of installed design skills. It can combine specialists for typography, animation, CSS discipline, interface polish, and Product Design workflows without loading the whole group.

Install it with its companion CSS skill:

```text
Install design and unslop-css from https://github.com/sago-cream/skills
```

Its optional capabilities come from [Product Design](https://learn.chatgpt.com/docs/plugins), [animation-vocabulary](https://github.com/emilkowalski/skills/tree/main/skills/animation-vocabulary), [font-cut](https://github.com/sago-cream/skills/tree/main/font-cut), [review-animations](https://github.com/emilkowalski/skills/tree/main/skills/review-animations), [emil-design-eng](https://github.com/emilkowalski/skills/tree/main/skills/emil-design-eng), and [make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better/tree/main/skills/make-interfaces-feel-better). Missing capabilities are skipped rather than installed automatically.

## Unslop CSS

`unslop-css` keeps styling changes on the project's design tokens and 4px grid, then checks the cascade for unintended overrides. It is explicit-only on its own and is selected automatically when `design` routes work that changes styling code.

## Font Cut

`font-cut` audits UI typography and proposes a smaller, more consistent set of text styles without flattening meaningful hierarchy or state.

Ask Codex to install it:

```text
Install font-cut from https://github.com/sago-cream/skills/tree/main/font-cut
```

Then use it in a project:

```text
Use $font-cut to audit this interface and propose a safe typography reduction.
```

## HTML Drop

`html-drop` turns a deliverable into a self-contained HTML artifact. Send `html` for a local file, `html+` for a live mobile-friendly preview, or `html-` to close and clean up the preview.

Install `html-drop` and `forward-port` together to enable the complete `html+` and `html-` workflow:

```text
Install html-drop and forward-port from https://github.com/sago-cream/skills
```

Each skill also works independently: `html-drop` can create local artifacts, while `forward-port` can expose an existing local server.

## Forward Port

`forward-port` exposes an existing local HTTP server through a Cloudflare Quick Tunnel without relying on shell aliases.

```text
Forward port 3000.
Forward this HTML file as homepage.
```
