---
name: unslop-css
description: Keep CSS and CSS-like styling changes aligned with the project's tokens, 4px sizing and spacing grid, and existing cascade. Use when explicitly invoked for CSS, Sass, Tailwind, CSS-in-JS, or component-style changes.
---

# Unslop CSS

When changing styling code:

1. Use the project's existing design tokens instead of hardcoded values. Search for the relevant token before adding a literal or creating another token.
2. Keep sizes and spacing in multiples of 4. Preserve intentional hairlines and optical adjustments when their purpose is clear.
3. Check the cascade before and after the edit. Search for the same selector and property, then account for source order, specificity, responsive rules, themes, and interaction states. Confirm the new rule neither gets overridden nor changes unrelated elements.

Stay within the requested styling change. Do not perform a general visual redesign or rewrite unrelated legacy values.
