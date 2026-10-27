#!/usr/bin/env python3
"""Export a standalone skill repository tree from packaging output.

Runs scripts/build.py at a source commit (default HEAD), then writes a directory
ready to push to GoldenDoodleAI/human-centered-language or GoldenDoodleAI/human-voice.

Example:
  python3 scripts/export_skill.py --skill human-centered
  python3 scripts/export_skill.py --skill human-voice --commit abc1234 --output /tmp/hv
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE_REPO = "GoldenDoodleAI/trauma-informed-language"
INSTALL_GUIDE_URL = f"https://github.com/{SOURCE_REPO}#install-start-here"

SKILLS = {
    "human-centered": {
        "packaging_name": "human-centered-language",
        "reference_file": "standard.md",
        "readme_title": "Human-centered language standard (agent skill)",
    },
    "human-voice": {
        "packaging_name": "human-voice",
        "reference_file": "module.md",
        "readme_title": "Human voice module (agent skill)",
    },
}


def resolve_commit(commit: str, repo_root: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "--verify", commit],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit(f"Could not resolve git commit: {commit}\n{result.stderr}")
    return result.stdout.strip()


def run_build(tree_root: Path) -> None:
    subprocess.run(
        [sys.executable, "scripts/build.py"],
        cwd=tree_root,
        check=True,
    )


def materialize_tree(commit: str) -> tuple[Path, str]:
    """Return (tree_root, sha). Uses a detached worktree when commit is not HEAD."""
    head = resolve_commit("HEAD", ROOT)
    target = resolve_commit(commit, ROOT)
    if target == head:
        run_build(ROOT)
        return ROOT, target

    tmp = Path(tempfile.mkdtemp(prefix="export-skill-"))
    subprocess.run(
        ["git", "worktree", "add", "--detach", str(tmp), target],
        cwd=ROOT,
        check=True,
    )
    run_build(tmp)
    return tmp, target


def readme_lead_and_assistant_block() -> str:
    return (
        f"Published by **GoldenDoodle AI**. For the full install guide (every tool, "
        f"compiled files, and trauma-informed layering), start at "
        f"[Install (start here)]({INSTALL_GUIDE_URL}) in the upstream monorepo.\n\n"
        f"# PLACEHOLDER_TITLE\n\n"
        "## If you are an AI assistant\n\n"
        "The person you are helping shared this repository link. They may not be technical. "
        "You can follow `SKILL.md` and the reference file in this folder for the rest of "
        "this conversation right away. For a permanent install in their tool, walk them "
        "through the steps in the install guide for their platform and offer to do any step "
        "you can automate.\n\n"
    )


def readme_text(skill_key: str, cfg: dict) -> str:
    ref = cfg["reference_file"]
    pname = cfg["packaging_name"]
    lead = readme_lead_and_assistant_block().replace(
        "# PLACEHOLDER_TITLE\n\n",
        f"# {cfg['readme_title']}\n\n",
        1,
    )
    if skill_key == "human-centered":
        body = f"""{lead}This repository packages the **human-centered language standard** as an agent skill for Claude and other tools that load `SKILL.md` plus companion files.

## What you get

- `SKILL.md`: entry point the agent reads first.
- `{ref}`: full standard text for the skill to follow.
- `AGENTS.md`: instructions for repo-based agents (Cursor and similar).
- `SOURCES.md`: organizations whose published guidance informed the standard.
- `PROVENANCE`: which commit of the upstream monorepo produced this export.

## Install

1. Download or clone this repository.
2. **Claude (Skills):** turn on **Settings → Capabilities** (code execution and create/edit files). Upload a zip of `SKILL.md` and `{ref}` via **Settings → Customize → Skills → + → + Create skill → Upload a skill** (release zips from the upstream monorepo work as-is).
3. **Other agents:** load `SKILL.md`, then load `{ref}` when the skill activates.

For compiled single-file installs and trauma-informed layering, see the upstream monorepo at https://github.com/{SOURCE_REPO}.

## License

See `LICENSE`. Standard content is CC BY 4.0 unless noted there.

## Updates

Re-exports track commits of `{SOURCE_REPO}`. Compare `PROVENANCE` in this repo with the monorepo release you intend to match.
"""
    else:
        body = f"""{lead}This repository packages the **human voice** optional module as an agent skill. Use it on top of the human-centered language standard when you want drafts to read less like generic machine output.

## What you get

- `SKILL.md`: entry point the agent reads first.
- `{ref}`: full module text.
- `AGENTS.md`: instructions for repo-based agents (Cursor and similar).
- `SOURCES.md`: upstream attribution for cited organizations.
- `PROVENANCE`: which commit of the upstream monorepo produced this export.

## Install

1. Download or clone this repository.
2. **Claude (Skills):** turn on **Settings → Capabilities** (code execution and create/edit files). Upload a zip of `SKILL.md` and `{ref}` via **Settings → Customize → Skills → + → + Create skill → Upload a skill** (release zips from the upstream monorepo work as-is).
3. Load the human-centered language skill first if you use both; this module adds style constraints only.

Upstream monorepo: https://github.com/{SOURCE_REPO} (`packaging/claude-skill/{pname}/`).

## License

See `LICENSE`.

## Updates

Re-exports track commits of `{SOURCE_REPO}`. Compare `PROVENANCE` with the monorepo commit you intend to match.
"""
    return body.strip() + "\n"


def provenance_text(skill_key: str, sha: str) -> str:
    return (
        f"source_repository={SOURCE_REPO}\n"
        f"source_commit={sha}\n"
        f"exported_skill={skill_key}\n"
    )


def export_files(skill_key: str, tree_root: Path, sha: str, output: Path) -> None:
    cfg = SKILLS[skill_key]
    skill_src = tree_root / "packaging" / "claude-skill" / cfg["packaging_name"]
    if not skill_src.is_dir():
        raise SystemExit(f"Missing skill packaging dir: {skill_src}")

    agents_src = tree_root / "AGENTS.md"
    if not agents_src.is_file():
        raise SystemExit(f"Missing AGENTS.md at {agents_src}")

    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    for path in sorted(skill_src.iterdir()):
        if path.is_file():
            shutil.copy2(path, output / path.name)

    shutil.copy2(tree_root / "LICENSE", output / "LICENSE")
    shutil.copy2(tree_root / "SOURCES.md", output / "SOURCES.md")
    shutil.copy2(agents_src, output / "AGENTS.md")
    (output / "README.md").write_text(readme_text(skill_key, cfg), encoding="utf-8")
    (output / "PROVENANCE").write_text(provenance_text(skill_key, sha), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export a skill repo tree from packaging.")
    parser.add_argument(
        "--skill",
        required=True,
        choices=sorted(SKILLS),
        help="human-centered or human-voice",
    )
    parser.add_argument(
        "--commit",
        default="HEAD",
        help="Source git commit in this repo (default: HEAD)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output directory (default: dist/export/<skill>/)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    out = args.output or (ROOT / "dist" / "export" / args.skill)
    tree_root, sha = materialize_tree(args.commit)
    try:
        export_files(args.skill, tree_root, sha, out.resolve())
    finally:
        if tree_root != ROOT:
            subprocess.run(
                ["git", "worktree", "remove", "--force", str(tree_root)],
                cwd=ROOT,
                check=False,
            )
    print(f"exported {args.skill} @ {sha[:12]} -> {out}")


if __name__ == "__main__":
    main()
