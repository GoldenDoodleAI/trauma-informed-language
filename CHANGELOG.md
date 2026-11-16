# Changelog

## Unreleased

Fix: the trauma-informed-communications `SKILL.md` front matter was not valid YAML. Its description contains "trauma: shelters", and an unquoted colon followed by a space makes strict parsers (PyYAML, js-yaml, the `yaml` npm package, gray-matter) reject the whole block. `scripts/build.py` now quotes a description only when a plain YAML scalar would break, so only the trauma-informed files change. Human-centered and human voice files are byte-identical to v1.0.0.

Model-facing text is unchanged: `packaging/compiled/`, `packaging/chatgpt/`, `standard.md`, `module.md` and the frozen v0.1.1 SKILL bodies are untouched. `verify_request_parity.py` reports NEW_BENCH_BASELINE=no.

New CI test `tests/test_skill_frontmatter.py` parses every shipped SKILL.md (loose and zipped) with PyYAML `safe_load` and checks name format, name-to-folder match, description length, and that zips hold SKILL.md at the root with no enclosing folder. The build now skips rewriting a zip whose contents already match, so unchanged skills keep identical bytes.

## v0.2.0 (October 2026)

Breaking file and folder renames: primary compiled and skill paths are `human-centered-language` and `trauma-informed-communications`. Marketplace packaging (`goldendoodle-ai`, `plugins/`, manifests), `VERSION`, and CI manifest tests. Legacy compiled filenames `dignified-language.md` and `trauma-informed.md` remain byte-identical copies of the new primary files for one release.

Model-facing compiled text (`packaging/compiled/*.md`) is unchanged from v0.1.1. Bench results remain comparable. No new baseline.

After payload analysis showed the weekly bench sends only `packaging/compiled/*.md`, Claude/plugin `SKILL.md` uses public `name` and `description` (folder-matched, denylist-clean) while the **body** stays the frozen v0.1.1 install copy so installed users see the same substance the bench tests. `tests/test_skill_bench_parity.py` enforces compiled bytes == `standard.md`/`module.md` and frozen SKILL bodies.

Docs: install-first README (folded from PR #7), human-facing rename to human-centered language standard and the trauma-informed standard, MKTNG benchmark credit in README testing section.

## v0.1.1 (September 2026)

**Brand voice templates** (`okf/templates/voice-interview.md`, `okf/templates/voice-profile.md`): the user-facing addition. Organizations can interview a model or fill in a blank profile to build their step-9 organization voice file.

Usability and consistency pass: fix leftover OKF index and documentation gaps from the v0.1.0 usability review; wire `scripts/build.py` to keep human-voice packaging in sync with `okf/modules/human-voice.md`. Human voice remains optional evolving module standards (AI writing tells), not a shipped product; tooling forthcoming.

## v0.1.0 (September 2026)

Initial release. Extracted from the GoldenDoodle AI production system prompt and separated into the Dignified Language Standard (base) and the Trauma-Informed layer.

Known items flagged for practitioner review:
- Canonical form for people without housing. The source used three variants; this release standardizes on "people experiencing homelessness" and lists the others as acceptable.
- The sex work / trafficking vocabulary entry asks the writer to make a consent determination the model cannot make from text. Marked as requiring human judgment.
- Capitalization of Black and Indigenous moved from reporting standards to the base style rules.
