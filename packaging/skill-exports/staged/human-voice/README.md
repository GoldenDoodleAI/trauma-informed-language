Published by **GoldenDoodle AI**. For the full install guide (every tool, compiled files, and trauma-informed layering), start at [Install (start here)](https://github.com/GoldenDoodleAI/trauma-informed-language#install-start-here) in the upstream monorepo.

# Human voice module (agent skill)

## If you are an AI assistant

The person you are helping shared this repository link. They may not be technical. You can follow `SKILL.md` and the reference file in this folder for the rest of this conversation right away. For a permanent install in their tool, walk them through the steps in the install guide for their platform and offer to do any step you can automate.

This repository packages the **human voice** optional module as an agent skill. Use it on top of the human-centered language standard when you want drafts to read less like generic machine output.

## What you get

- `SKILL.md`: entry point the agent reads first.
- `module.md`: full module text.
- `AGENTS.md`: instructions for repo-based agents (Cursor and similar).
- `SOURCES.md`: upstream attribution for cited organizations.
- `PROVENANCE`: which commit of the upstream monorepo produced this export.

## Install

1. Download or clone this repository.
2. **Claude (Skills):** left sidebar **Customize → Skills**, **Add → Upload skill**, then choose a `.zip` that includes `SKILL.md` and `module.md` (release zips from the upstream monorepo work as-is). Skills are managed under Customize; **Settings → Capabilities** varies by plan.
3. Load the human-centered language skill first if you use both; this module adds style constraints only.

Upstream monorepo: https://github.com/GoldenDoodleAI/trauma-informed-language (`packaging/claude-skill/human-voice/`).

## License

See `LICENSE`.

## Updates

Re-exports track commits of `GoldenDoodleAI/trauma-informed-language`. Compare `PROVENANCE` with the monorepo commit you intend to match.
