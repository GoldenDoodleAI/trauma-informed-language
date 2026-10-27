# Skill repository exports

The monorepo at `GoldenDoodleAI/trauma-informed-language` publishes two standalone skill repositories:

| Export name | Downstream repo | Packaging folder |
|---|---|---|
| `human-centered` | `GoldenDoodleAI/human-centered-language` | `packaging/claude-skill/human-centered-language/` |
| `human-voice` | `GoldenDoodleAI/human-voice` | `packaging/claude-skill/human-voice/` |

## Export locally

From the repository root, after `okf/` changes run `python3 scripts/build.py` (or let the export script run it for you):

```bash
python3 scripts/export_skill.py --skill human-centered
python3 scripts/export_skill.py --skill human-voice
```

Options:

- `--commit <ref>`: git commit to export (default `HEAD`). Uses a detached worktree when not on that commit.
- `--output <dir>`: write tree here (default `dist/export/<skill>/`).

Each export contains `SKILL.md`, the reference file (`standard.md` or `module.md`), `README.md`, `AGENTS.md`, `LICENSE`, `SOURCES.md`, and `PROVENANCE`.

## Staged export trees (launch handoff)

After `export_skill.py`, maintainers can copy the output into `packaging/skill-exports/staged/<skill>/` on a branch so reviewers can push to downstream repos without re-running export. Replace the whole directory when the lock commit changes.

Push to a downstream repo (example):

```bash
git clone git@github.com:GoldenDoodleAI/human-centered-language.git
rsync -a packaging/skill-exports/staged/human-centered/ human-centered-language/
cd human-centered-language && git add -A && git commit -m "chore: re-export from trauma-informed-language @ <commit>"
```

## Lock file

`packaging/skill-exports/lock.json` records the `source_commit` each downstream repo should match. After you push a new export to a skill repo, update the lock entry to that commit in the same pull request (or immediately after).

## CI verification

Workflow: `.github/workflows/skill-export.yml`

1. Check out this repository.
2. Run `python3 scripts/verify_skill_exports.py`.

The verifier exports each skill at the locked commit and builds a SHA-256 manifest of the published files. When the downstream repository exists and is readable, it clones the repo, checks that `PROVENANCE` names the same `source_commit`, and fails on any byte-level drift.

### When skill repos are not public yet

By default, verification only checks that exports build cleanly at the locked commit. Remote comparison is skipped if `gh repo view` cannot see the downstream repo.

To require remote drift checks (once the repos exist and contain a matching `PROVENANCE`):

```yaml
env:
  SKILL_EXPORT_VERIFY_REMOTE: "1"
```

### GitHub Actions permissions and secrets

| Need | Purpose |
|---|---|
| `permissions: contents: read` | Checkout this monorepo |
| `GITHUB_TOKEN` (default) | Enough to clone **public** downstream repos from Actions |
| Optional PAT in `GH_TOKEN` | Read access if skill repos are private |

Install `gh` is not required locally; the verify script uses `git clone` with `https://github.com/...` when a token is set.

### Enabling strict mode on `main`

After the first export lands in each skill repo, set repository variable `SKILL_EXPORT_VERIFY_REMOTE` to `1` (or add the env block to the workflow job) so CI fails when downstream trees drift from a fresh export.
