Published by **GoldenDoodle AI**. For the full install guide (every tool, compiled files, and trauma-informed layering), start at [Install (start here)](https://github.com/GoldenDoodleAI/trauma-informed-language#install-start-here) in the upstream monorepo.

# Human-centered language standard (agent skill)

## If you are an AI assistant

The person you are helping shared this repository link. They may not be technical. You can follow `SKILL.md` and the reference file in this folder for the rest of this conversation right away. For a permanent install in their tool, walk them through the steps in the install guide for their platform and offer to do any step you can automate.

This repository packages the **human-centered language standard** as an agent skill for Claude and other tools that load `SKILL.md` plus companion files.

## What you get

- `SKILL.md`: entry point the agent reads first.
- `standard.md`: full standard text for the skill to follow.
- `AGENTS.md`: instructions for repo-based agents (Cursor and similar).
- `SOURCES.md`: organizations whose published guidance informed the standard.
- `PROVENANCE`: which commit of the upstream monorepo produced this export.

## Install

1. Download or clone this repository.
2. **Claude (Skills):** left sidebar **Customize → Skills**, **Add → Upload skill**, then choose a `.zip` that includes `SKILL.md` and `standard.md` (release zips from the upstream monorepo work as-is). Skills are managed under Customize; **Settings → Capabilities** varies by plan.
3. **Other agents:** load `SKILL.md`, then load `standard.md` when the skill activates.

For compiled single-file installs and trauma-informed layering, see the upstream monorepo at https://github.com/GoldenDoodleAI/trauma-informed-language.

## License

See `LICENSE`. Standard content is CC BY 4.0 unless noted there.

## Updates

Re-exports track commits of `GoldenDoodleAI/trauma-informed-language`. Compare `PROVENANCE` in this repo with the monorepo release you intend to match.
