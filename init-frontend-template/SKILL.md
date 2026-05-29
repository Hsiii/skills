---
name: init-frontend-template
description: Create a new empty GitHub repository from Hsi's Bun/Vite/React frontend-template GitHub template and clone it locally. Use when the user asks Codex to bootstrap, scaffold, seed, or start a new frontend app/repo from the frontend-template project using the normal GitHub template flow, especially phrases like "use my frontend template", "init an empty repo", "create a repo from frontend-template", or "make a new React/Vite/Bun app".
---

# Init Frontend Template

## Workflow

Use GitHub's template-repo flow, not manual copying and not plain `git clone`.

Default template:

```text
Hsiii/frontend-template
```

Default command:

```bash
python3 /Users/hsi/.codex/skills/init-frontend-template/scripts/init_frontend_template.py --install --check --push-package-rename
```

This runs:

```bash
gh repo create "$(basename "$PWD")" --private --template Hsiii/frontend-template
gh repo clone "$(basename "$PWD")" "$PWD"
```

## Rules

- Use this skill only for creating a new repo from the GitHub template.
- When Codex is already in the intended empty project folder, call the script without a repo argument; the current folder basename is the repo name.
- Do not use it for non-empty folders/repos or retrofitting an existing app.
- Do not plain `git clone` the template repo as the app repo.
- Default to `--private` unless the user asks for public or internal.
- Let `gh repo create --template ...` create the GitHub repo, then `gh repo clone` into the empty target folder.
- After cloning, rewrite `package.json.name` to the new repo basename unless the user asks not to.
- Run `bun i` and `bun run check` when the user expects a fully initialized project.
- If `package.json.name` changes, commit with `chore: rename package`.
- Push the package-name commit only when requested or when using `--push-package-rename`.

## Examples

```bash
python3 /Users/hsi/.codex/skills/init-frontend-template/scripts/init_frontend_template.py my-app
python3 /Users/hsi/.codex/skills/init-frontend-template/scripts/init_frontend_template.py Hsiii/my-app --public
python3 /Users/hsi/.codex/skills/init-frontend-template/scripts/init_frontend_template.py ../my-app --install --check --push-package-rename
python3 /Users/hsi/.codex/skills/init-frontend-template/scripts/init_frontend_template.py my-app --description "Frontend app" --install --check
python3 /Users/hsi/.codex/skills/init-frontend-template/scripts/init_frontend_template.py --install --check
```
