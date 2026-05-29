#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


DEFAULT_TEMPLATE = "Hsiii/frontend-template"


def slugify_project_name(name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", name.strip()).strip("-._").lower()
    return slug or "frontend-app"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a new GitHub repo from Hsi's frontend template and clone it.",
    )
    parser.add_argument(
        "repo",
        nargs="?",
        help="New repo name, OWNER/REPO, or local clone path. The basename becomes the repo name.",
    )
    parser.add_argument(
        "--template",
        default=DEFAULT_TEMPLATE,
        help="GitHub template repo in OWNER/REPO form.",
    )
    visibility = parser.add_mutually_exclusive_group()
    visibility.add_argument("--private", action="store_true", default=True)
    visibility.add_argument("--public", action="store_true")
    visibility.add_argument("--internal", action="store_true")
    parser.add_argument("--description", help="GitHub repo description.")
    parser.add_argument("--install", action="store_true", help="Run bun i after cloning.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Run bun run check after cloning.",
    )
    parser.add_argument(
        "--skip-package-rename",
        action="store_true",
        help="Do not rewrite package.json name to the new repo basename.",
    )
    parser.add_argument(
        "--push-package-rename",
        action="store_true",
        help="Push the package.json rename commit when it changes.",
    )
    return parser.parse_args()


def run(command: list[str], cwd: Path) -> None:
    print(f"+ {' '.join(command)}", flush=True)
    subprocess.run(command, cwd=cwd, check=True)


def repo_arg_and_clone_dir(repo: str) -> tuple[str, Path, str]:
    path = Path(repo).expanduser()
    if path.parent == Path(".") and "/" in repo and not repo.startswith((".", "~", "/")):
        repo_name = repo.rsplit("/", 1)[1]
        return repo, Path.cwd() / repo_name, repo_name

    clone_dir = path.resolve()
    repo_name = clone_dir.name
    return repo_name, clone_dir, repo_name


def repo_arg_and_clone_dir_from_cwd() -> tuple[str, Path, str]:
    clone_dir = Path.cwd()
    repo_name = clone_dir.name
    return repo_name, clone_dir, repo_name


def ensure_clone_target_ready(clone_dir: Path) -> None:
    if clone_dir.exists() and any(clone_dir.iterdir()):
        raise SystemExit(f"Clone target is not empty: {clone_dir}")
    clone_dir.parent.mkdir(parents=True, exist_ok=True)


def update_package_name(repo_dir: Path, name: str) -> bool:
    package_json = repo_dir / "package.json"
    if not package_json.exists():
        return False

    data = json.loads(package_json.read_text(encoding="utf-8"))
    package_name = slugify_project_name(name)
    if data.get("name") == package_name:
        return False

    data["name"] = package_name
    package_json.write_text(
        json.dumps(data, indent=4, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return True


def visibility_flag(args: argparse.Namespace) -> str:
    if args.public:
        return "--public"
    if args.internal:
        return "--internal"
    return "--private"


def main() -> int:
    args = parse_args()
    if args.repo:
        repo_arg, clone_dir, repo_name = repo_arg_and_clone_dir(args.repo)
    else:
        repo_arg, clone_dir, repo_name = repo_arg_and_clone_dir_from_cwd()
    ensure_clone_target_ready(clone_dir)

    command = [
        "gh",
        "repo",
        "create",
        repo_arg,
        visibility_flag(args),
        "--template",
        args.template,
    ]
    if args.description:
        command.extend(["--description", args.description])

    run(command, clone_dir.parent)
    run(["gh", "repo", "clone", repo_arg, str(clone_dir)], clone_dir.parent)

    changed_package_name = False
    if not args.skip_package_rename:
        changed_package_name = update_package_name(clone_dir, repo_name)

    if args.install:
        run(["bun", "i"], clone_dir)
    if args.check:
        run(["bun", "run", "check"], clone_dir)
    if changed_package_name:
        run(["git", "add", "package.json"], clone_dir)
        run(["git", "commit", "-m", "chore: rename package"], clone_dir)
    if changed_package_name and args.push_package_rename:
        run(["git", "push"], clone_dir)

    print(f"Initialized frontend repo at {clone_dir}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as error:
        raise SystemExit(error.returncode) from error
