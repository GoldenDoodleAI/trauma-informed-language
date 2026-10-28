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
| **Claude** | `packaging/releases/human-centered-language.zip`, `trauma-informed-communications.zip`, or `human-voice.zip` (or [GitHub Releases](https://github.com/GoldenDoodleAI/trauma-informed-language/releases) when published). Upload via **Customize → Skills → Add → Upload skill** (see steps below). |
| **ChatGPT** | Paste `packaging/chatgpt/human-centered-language.md` or `trauma-informed-communications.md` into a Project's instructions (**••• → Project settings**). Upload sector vocabulary from `okf/standard/vocabulary/` if needed. |
| **Gemini** | Upload `packaging/gemini/human-centered-language.zip`, `trauma-informed-communications.zip`, or `human-voice.zip` (or the matching folder under `packaging/gemini/`) in **Gemini Skills**. |
| **Cursor / repo agent** | Read [AGENTS.md](AGENTS.md). Load `packaging/compiled/` by default. |
| **Brand voice** (optional, step 9) | Interview: `okf/templates/voice-interview.md`. Blank profile: `okf/templates/voice-profile.md`. |

All install paths live under [`packaging/`](packaging/). See [packaging/README.md](packaging/README.md) for what each folder contains.

**Legacy filenames (one release):** `packaging/compiled/dignified-language.md` and `packaging/compiled/trauma-informed.md` are byte-identical copies of the new primary files for backward compatibility.

Per-model packaging files are intentionally separate. They may drift slightly in preamble or formatting; `okf/` is the authoring source (see below).

**Agents already at this repo:** load `packaging/compiled/human-centered-language.md` or `packaging/compiled/trauma-informed-communications.md`. Do not run setup or git publish steps.

Model behavior changes with each release. Before choosing a model, check [MODELS.md](MODELS.md) for the current roster.

### Claude (claude.ai)

Skills are managed from the left sidebar **Customize** tab (**Skills** | Connectors | Plugins). On accounts checked in October 2026, **Settings → Capabilities** only points to Customize and does not list skill upload steps; Capabilities options (tool access, artifacts, and similar) vary by plan. Some older guides mention code execution or file-creation toggles; do not assume those appear on every account.

1. Download `human-centered-language.zip`, `trauma-informed-communications.zip`, or `human-voice.zip` from `packaging/releases/` (or [GitHub Releases](https://github.com/GoldenDoodleAI/trauma-informed-language/releases) when published). Each layer zip contains `SKILL.md` and `standard.md` (a `.zip` with `SKILL.md` is what Claude expects).
2. Open **Customize → Skills**. Use the **Yours** toggle if you are looking for skills you already added. Click **Add**, then **Upload skill**.
3. On **Upload a skill**, choose the zip (drag and drop or browse). Zip upload is the official install path.
4. Turn the skill on when prompted. Claude applies the standard to writing about the people you serve, or you can invoke it directly.

**Helper (verified on Claude Team, Oct 2026):** Paste `https://github.com/GoldenDoodleAI/trauma-informed-language` and ask Claude to fetch the repo and help you set up the skill. Claude can clone and inspect the public repository in its sandbox (read `INSTALL.md`, `packaging/`, release zips, and skill folders). Claude **cannot** add or install a skill on your account from chat. Claude may help you pick the right zip and walk through upload; you still upload it yourself via **Customize → Skills → Add → Upload skill**. There is no one-click install from a pasted URL.

On Claude Team or Enterprise, an admin can set org-wide policy under **Organization settings → Plugins & skills**.

### ChatGPT

1. Create a Project.
2. Open **••• → Project settings** and paste the contents of `packaging/chatgpt/human-centered-language.md` or `trauma-informed-communications.md` into the project instructions field.
3. If your sector has its own vocabulary file under `okf/standard/vocabulary/` (housing, disability, substance use, mental health), upload it too as a project file.

Custom GPTs are not the recommended path. Personal accounts on Free, Go, Plus, or Pro cannot create new custom GPTs. OpenAI is retiring custom GPTs, with standard retirement on **December 11, 2026** (some Enterprise workspaces later). See OpenAI Help: [Custom GPT retirement and migration FAQ](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq). Prefer Projects.

### Gemini

1. Open **Skills** in Gemini (when available in your account).
2. Upload `packaging/gemini/human-centered-language.zip` or `trauma-informed-communications.zip` from this repo (each zip contains `SKILL.md` and `standard.md`). For the optional human voice module, use `packaging/gemini/human-voice.zip` (`SKILL.md` + `module.md`).
3. Toggle the skill on. The same release zips under `packaging/releases/` also work if your client accepts them; the `packaging/gemini/` copies are the Gemini-specific entry points.

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

**The Human-Centered Language Benchmark** runs monthly against the current production models from each major vendor and leading open-weight hosts. The active prompt set is **45 prompts** (all 45 run every month). Each prompt is exercised three ways: with no standard loaded, with the human-centered language base, and with the trauma-informed standard on top.

The optional **human voice** module rotates on a separate arm: one third of the 45 prompts (15 prompts) per monthly run, cycling through three fixed thirds so every prompt gets a human-voice check over the quarter.

Outputs are scored against the practice files in this repo by a **three-family judge panel**: Anthropic (Claude Opus 4.6), OpenAI (GPT-5.5), and Meta (Muse Spark 1.3). Human calibration sits on every run.

Golden prompts for contributors live in `tests/prompts/`. The benchmark repository publishes methodology, judge configuration, and raw outputs with each report so anyone can regrade. Benchmark engineered by MKTNG.

<!-- TODO: replace with the public methodology URL when published on goldendoodleai.com -->

Early monthly runs are a calibration series and are not published as findings.

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
