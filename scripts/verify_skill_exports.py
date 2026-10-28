#!/usr/bin/env python3
"""Verify downstream skill repos match a fresh export from the locked source commit.

Reads packaging/skill-exports/lock.json, exports each skill at its recorded commit,
and compares a SHA-256 manifest of the export tree to each skill repository.

When GoldenDoodleAI/human-centered-language or GoldenDoodleAI/human-voice are not
reachable yet, remote verification is skipped unless SKILL_EXPORT_VERIFY_REMOTE=1
(in which case a missing repo fails the check).

Environment:
  SKILL_EXPORT_VERIFY_REMOTE=1  Require clone + byte match against downstream repos.
  GITHUB_TOKEN / GH_TOKEN      Token with read access to the skill repos (public repos: default GITHUB_TOKEN in Actions).
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCK_PATH = ROOT / "packaging" / "skill-exports" / "lock.json"

COMPARE_NAMES = ("SKILL.md", "README.md", "LICENSE", "SOURCES.md", "PROVENANCE", "AGENTS.md")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def tree_manifest(directory: Path, extra_names: tuple[str, ...]) -> dict[str, str]:
    names = set(COMPARE_NAMES) | set(extra_names)
    manifest: dict[str, str] = {}
    for name in sorted(names):
        path = directory / name
        if not path.is_file():
            raise SystemExit(f"Missing expected file in export: {path}")
        manifest[name] = sha256_file(path)
    return manifest


def load_lock() -> dict:
    if not LOCK_PATH.is_file():
        raise SystemExit(f"Missing lock file: {LOCK_PATH}")
    return json.loads(LOCK_PATH.read_text(encoding="utf-8"))


def export_skill(skill_key: str, commit: str, dest: Path) -> None:
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "export_skill.py"),
            "--skill",
            skill_key,
            "--commit",
            commit,
            "--output",
            str(dest),
        ],
        cwd=ROOT,
        check=True,
    )


def parse_provenance(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            data[key.strip()] = value.strip()
    return data


def repo_accessible(full_name: str) -> bool:
    env = os.environ.copy()
    token = env.get("GITHUB_TOKEN") or env.get("GH_TOKEN")
    if token:
        env["GH_TOKEN"] = token
    result = subprocess.run(
        ["gh", "repo", "view", full_name, "--json", "name"],
        capture_output=True,
        text=True,
        env=env,
    )
    return result.returncode == 0


def clone_repo(full_name: str, dest: Path) -> None:
    env = os.environ.copy()
    token = env.get("GITHUB_TOKEN") or env.get("GH_TOKEN")
    url = f"https://github.com/{full_name}.git"
    if token:
        url = f"https://x-access-token:{token}@github.com/{full_name}.git"
    subprocess.run(["git", "clone", "--depth", "1", url, str(dest)], check=True)


def reference_file_for(skill_key: str) -> str:
    return "standard.md" if skill_key == "human-centered" else "module.md"


def verify_one(skill_key: str, entry: dict, require_remote: bool) -> None:
    commit = entry["source_commit"]
    downstream = entry["downstream_repo"]
    ref_file = reference_file_for(skill_key)

    with tempfile.TemporaryDirectory(prefix=f"verify-{skill_key}-") as tmp:
        export_dir = Path(tmp) / "export"
        export_skill(skill_key, commit, export_dir)
        expected = tree_manifest(export_dir, (ref_file,))

        prov = parse_provenance(export_dir / "PROVENANCE")
        if prov.get("source_commit") != commit:
            raise SystemExit(f"{skill_key}: PROVENANCE commit mismatch after export")

        if not repo_accessible(downstream):
            if require_remote:
                raise SystemExit(
                    f"{skill_key}: downstream repo {downstream} is not reachable "
                    "(create the repo or unset SKILL_EXPORT_VERIFY_REMOTE)."
                )
            print(
                f"skip remote: {downstream} not reachable; local export at {commit[:12]} OK"
            )
            return

        clone_dir = Path(tmp) / "downstream"
        clone_repo(downstream, clone_dir)
        downstream_prov = parse_provenance(clone_dir / "PROVENANCE")
        if downstream_prov.get("source_commit") != commit:
            raise SystemExit(
                f"{skill_key}: {downstream} PROVENANCE source_commit "
                f"{downstream_prov.get('source_commit')} != lock {commit}"
            )

        actual = tree_manifest(clone_dir, (ref_file,))
        diffs = []
        for name, digest in expected.items():
            if actual.get(name) != digest:
                diffs.append(name)
        if diffs:
            raise SystemExit(
                f"{skill_key}: drift vs {downstream} at lock commit {commit[:12]}: "
                + ", ".join(sorted(diffs))
            )
        print(f"ok {skill_key}: {downstream} matches export @ {commit[:12]}")


def main() -> None:
    require_remote = os.environ.get("SKILL_EXPORT_VERIFY_REMOTE", "").strip() in (
        "1",
        "true",
        "yes",
    )
    lock = load_lock()
    skills = lock.get("skills") or {}
    for skill_key, entry in skills.items():
        verify_one(skill_key, entry, require_remote)
    print("skill export verification finished")


if __name__ == "__main__":
    main()
