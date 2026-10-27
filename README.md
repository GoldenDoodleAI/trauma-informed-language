# Trauma-informed language standard

An open, machine-readable trauma-informed language standard for how organizations talk about people, including the full human-centered language standard as its base.

Maintained by [GoldenDoodle AI](https://goldendoodleai.com). Editor: Laura Braden.

## Install (start here)

**Pick one layer:**

| Layer | When to use |
|---|---|
| **Human-centered language standard** (base) | Any organization that cares how it speaks about people |
| **Trauma-informed standard** | Organizations serving people affected by trauma (shelter, DV program, foster care nonprofit). Includes the base automatically. |

**Then grab the ready-to-load file for your tool:**

| Tool | What to paste or upload |
|---|---|
| **Any model** (system prompt, RAG, API) | `packaging/compiled/human-centered-language.md` or `packaging/compiled/trauma-informed-communications.md` |
| **Claude** | `packaging/releases/human-centered-language.zip`, `trauma-informed-communications.zip`, or `human-voice.zip` (or [GitHub Releases](https://github.com/GoldenDoodleAI/trauma-informed-language/releases) when published). Upload the zip under **Settings → Customize → Skills** (see steps below). |
| **ChatGPT** | Paste `packaging/chatgpt/human-centered-language.md` or `trauma-informed-communications.md` into a Project's instructions (**••• → Project settings**). Upload sector vocabulary from `okf/standard/vocabulary/` if needed. |
| **Gemini** | Paste `packaging/gemini/human-centered-language.md` or `trauma-informed-communications.md` as a Gem's instructions today. Google is moving personal accounts from Gems toward Skills around November 2026; when your account shows Skills, you can upload the same `SKILL.md` zip used for Claude. |
| **Cursor / repo agent** | Read [AGENTS.md](AGENTS.md). Load `packaging/compiled/` by default. |
| **Brand voice** (optional, step 9) | Interview: `okf/templates/voice-interview.md`. Blank profile: `okf/templates/voice-profile.md`. |

All install paths live under [`packaging/`](packaging/). See [packaging/README.md](packaging/README.md) for what each folder contains.

**Legacy filenames (one release):** `packaging/compiled/dignified-language.md` and `packaging/compiled/trauma-informed.md` are byte-identical copies of the new primary files for backward compatibility.

Per-model packaging files are intentionally separate. They may drift slightly in preamble or formatting; `okf/` is the authoring source (see below).

**Agents already at this repo:** load `packaging/compiled/human-centered-language.md` or `packaging/compiled/trauma-informed-communications.md`. Do not run setup or git publish steps.

Model behavior changes with each release. Before choosing a model, check [MODELS.md](MODELS.md) for the current roster.

### Claude (claude.ai)

**Prerequisites:** **Settings → Capabilities**. Turn on **Code execution** and **Create and edit files** (shown as file creation in some builds). Skills do not run without them.

1. Download `human-centered-language.zip`, `trauma-informed-communications.zip`, or `human-voice.zip` from `packaging/releases/` (or [GitHub Releases](https://github.com/GoldenDoodleAI/trauma-informed-language/releases) when published). Each layer zip contains `SKILL.md` and `standard.md`.
2. Go to **Settings → Customize → Skills → + → + Create skill → Upload a skill** and select the zip. Zip upload is the official install path.
3. Toggle the skill on. Claude applies the standard to writing about the people you serve, or you can invoke it directly.

**Helper (optional):** With file creation on, Claude can help you assemble the zip and walk through the upload steps. You still upload the zip yourself under **Customize → Skills**.

On Claude Team or Enterprise, an admin can set org-wide policy under **Organization settings → Plugins & skills**.

### ChatGPT

1. Create a Project.
2. Open **••• → Project settings** and paste the contents of `packaging/chatgpt/human-centered-language.md` or `trauma-informed-communications.md` into the project instructions field.
3. If your sector has its own vocabulary file under `okf/standard/vocabulary/` (housing, disability, substance use, mental health), upload it too as a project file.

Custom GPTs are not the recommended path. Personal accounts on Free, Go, Plus, or Pro cannot create new custom GPTs. OpenAI is retiring custom GPTs, with standard retirement on **December 11, 2026** (some Enterprise workspaces later). See OpenAI Help: [Custom GPT retirement and migration FAQ](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq). Prefer Projects.

### Gemini

1. Create a Gem (or follow the Skills flow if that is what your account shows today).
2. Paste `packaging/gemini/human-centered-language.md` or `trauma-informed-communications.md` as its instructions.

Google is transitioning personal Gemini accounts from Gems toward Skills around **November 2026**. When Skills are available on your account, you can upload the same Claude-style zip (`SKILL.md` plus `standard.md`) from `packaging/releases/`. Use whichever path your account offers today.

### Any other agent or RAG pipeline

Paste `packaging/compiled/human-centered-language.md` or `trauma-informed-communications.md` as system context. For platform-specific formatting, use the matching folder under `packaging/`.

## What this is

Most organizations that serve people have opinions about language. Very few have written them down in a form an AI model can follow. This repository is that form.

It is a directory of markdown files with YAML frontmatter, following the [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) conventions, so it can be loaded into Claude, ChatGPT, Gemini, an open-weight model, or any agent that reads files. Humans can read it too. That is the point.

There are two layers:

**The human-centered language standard** is the base. Person-first language, no deficit framing, the organization is never the hero, plain language by default, and reporting standards for sensitive topics. Any organization that cares how it speaks about people can adopt it. A medical association, a housing coalition, and a trade group can all run on it.

**The trauma-informed standard** sits on top of the base and requires it. It adds SAMHSA's Four R's and Six Principles, four additional practices aimed at fundraising and storytelling, and a Crisis protocol. It is written for organizations serving people affected by trauma and for the communicators who work alongside them.

The base is a subset of the trauma-informed standard, not a lighter version of it. If you adopt trauma-informed, you have adopted the base.

## How the standard is tested

Every month, the standard is run on the current production models from each major vendor and the leading open-weight models. Each run uses a **core set of 30 writing prompts** plus a **rotating set of 10 to 15** additional prompts. Each prompt runs three ways: with no standard loaded, with the human-centered language base, and with the trauma-informed standard on top. Outputs are scored by a **three-family judge panel** (Anthropic Opus, OpenAI GPT, and Muse families) against the practice files in this repo.

Maintainers keep a larger golden prompt library in `tests/prompts/` for CI and practice development; the monthly bench uses the core plus rotating set above.

**The Human-Centered Language Benchmark** publishes methodology, judge configuration, and raw outputs with each report so anyone can regrade. Benchmark engineered by MKTNG.

<!-- TODO: replace with the public methodology URL when published on goldendoodleai.com -->

## Source of truth (maintainers and scoring)

**End users should install from [`packaging/`](packaging/), not by picking individual files under `okf/`.**

`okf/` is the machine-readable source catalog. It is what maintainers edit, what `scripts/build.py` renders into `packaging/`, and what the monthly benchmark scores against. If compiled or platform packaging disagrees with `okf/`, trust `okf/` and regenerate packaging.

```
okf/
  index.md             Bundle directory listing (OKF v0.2)
  load-order.md        Sequencing playbook for fine-grained loads
  standard/            Human-centered language standard (base)
    principles.md      What the standard is for
    precedence.md      How these practices interact with brand voice and user requests
    rules/             One file per practice (maintainer path; public text says practices)
    vocabulary/        Swappable sector vocabulary (housing, substance use, ...)
    protocols/         Rewrite protocol
  trauma-informed/     Trauma-informed standard (requires standard/)
    four-rs.md
    six-principles.md
    rules/             Fundraising and storytelling practices
    protocols/         Crisis protocol
  modules/             Optional add-ons
  templates/           Brand voice templates (profile blank + interview megaprompt)
packaging/             Ready-to-load versions for each platform (what users install)
plugins/               Marketplace plugin stubs (one skill per plugin)
tests/                 Golden prompts and the scoring rubric
scripts/               Build script that renders packaging/
```

For fine-grained control (custom loaders, scoring, or contributing), walk `okf/` using [okf/load-order.md](okf/load-order.md). [okf/index.md](okf/index.md) lists bundle contents.

**Optional modules:** Human voice (`okf/modules/human-voice.md`) ships in `packaging/releases/human-voice.zip` and marketplace manifests alongside the two standards.

## Model behavior

Instructions land differently across models and change with each release. See [How the standard is tested](#how-the-standard-is-tested) for the monthly benchmark and [MODELS.md](MODELS.md) for the current model roster.

## Contributing

Practices change when practitioners say they should. See [CONTRIBUTING.md](CONTRIBUTING.md). Sector vocabulary contributions are especially welcome.

## License

Content (everything under `okf/`, `packaging/`, `tests/`): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Use it, adapt it, credit GoldenDoodle AI.
Code (`scripts/`): MIT.

SAMHSA's trauma-informed framework is a work of the United States government and is in the public domain. Reporting standards reference the Dart Center for Journalism and Trauma; their guidance is cited, not reproduced.
