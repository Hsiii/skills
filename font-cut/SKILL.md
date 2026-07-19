---
name: font-cut
description: Audit UI typography variants and propose evidence-backed reductions across font size, typeface, weight, opacity, color, and style. Use when asked to inventory fonts, simplify type tokens, reduce typography drift, consolidate duplicate text styles, review a design system's font matrix, or plan a typography migration in SwiftUI, CSS, Tailwind, React Native, Flutter, Compose, or similar UI code.
---

# Font Cut

Inventory the typography that can actually render, distinguish semantic aliases from visual variants, and propose the smallest safe cut. Audit only unless the user explicitly asks for implementation.

## Define the variant

Represent each authored text variant as:

`size × typeface × weight × opacity × color × style`

Resolve every dimension before deduplicating:

- **Size:** Record the authored size and responsive behavior such as Dynamic Type, `rem`, or minimum scale factors. Do not turn every possible responsive result into a separate variant.
- **Typeface:** Record the family or system design: system/default, serif, rounded, monospaced, or custom family. Treat SF Symbols and other icon fonts separately from text.
- **Weight:** Resolve named tokens and inherited modifiers to the rendered weight.
- **Opacity:** Record effective authored opacity. Combine ancestor and element opacity when knowable; list conditional disabled or hidden values as state variants.
- **Color:** Prefer semantic tokens such as `text`, `muted`, `primary`, and `danger`. Do not multiply one adaptive token into separate light/dark/theme variants.
- **Style:** Record typography-affecting features such as italic, tracking, casing, decoration, font width, line height, and tabular or monospaced digits. Keep layout-only alignment and truncation in notes.

## Inventory workflow

1. Locate typography tokens, raw font declarations, text components, color tokens, opacity modifiers, and inherited container styles. Start with `rg` and inspect the surrounding component code.
2. Separate authored text from platform-controlled surfaces such as native alerts, pickers, and date controls. Report those surfaces as exclusions unless their typography is explicitly styled.
3. Resolve aliases to their underlying values. Follow local modifiers such as `.weight(...)`, responsive classes, and inherited parent styles.
4. Record source locations and usage roles for every tuple. Include conditional colors and opacities without pretending they are always active.
5. Count four layers separately:
   - declared semantic aliases;
   - unique size × typeface × weight constructions;
   - unique rendered text tuples across all six dimensions;
   - state-only variants such as disabled opacity.
6. Group exact duplicates. Preserve evidence about why their semantic names differ even when their pixels do not.
7. Mark unknown or runtime-dependent values instead of guessing.

## Propose the cut

Produce two levels when useful:

- **Safe cut:** Merge exact visual duplicates, redundant aliases, and one-off names without changing rendered output.
- **Aggressive cut:** Remove a weakly justified size, weight, color, or style and state the visible tradeoff.

Use these rules:

- Cut accidental dimensions before meaningful hierarchy.
- Treat a one-off weight or size as a candidate, not an automatic deletion.
- Do not merge text and icon-font tokens solely because their numeric size and weight match.
- Preserve semantic colors for content, muted text, actions, danger, selection, and disabled states when they communicate meaning.
- Preserve tabular or monospaced digits for changing times, prices, counters, and aligned numeric data.
- Prefer one canonical token with semantic aliases when names improve intent but should not create independent values.
- Show a direct current → proposed mapping and identify unused tokens.
- Quantify the reduction at every layer; do not claim a visual reduction when only aliases changed.

## Output format

Lead with a compact summary:

`N aliases → B base constructions → R rendered tuples (+ S state variants)`

Then provide:

1. **Scope and exclusions**
2. **Current matrix** with columns: ID, size, typeface, weight, opacity, color, style, roles, evidence
3. **Cut proposal** with columns: current, proposed, action, rationale, visual impact
4. **Before/after counts** for aliases, base constructions, rendered tuples, sizes, weights, colors, and styles
5. **Migration order and validation** only when implementation is requested

Keep colors semantic in the main table; add resolved theme values only when contrast or brand fidelity is part of the request.

## Validate an implementation

When the user asks to apply the cut:

1. Change tokens before call sites where possible.
2. Remove or alias redundant declarations only after all usages are mapped.
3. Run the project's format, type, build, and test checks.
4. Visually compare representative screens at compact and large widths, light and dark themes, disabled states, long localized text, and dynamic numeric states.
5. Re-run the inventory and report the actual before/after counts.
