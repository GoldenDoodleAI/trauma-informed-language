# Installing the standard

This file is written for an AI agent helping a person set this up. If you are a person reading it, the short version is in the README. On Claude, paste `https://github.com/GoldenDoodleAI/trauma-informed-language` and ask it to fetch the repo and walk you through install (verified Oct 2026: Claude can read the public repo in chat but cannot register a skill on your account). On ChatGPT or Gemini, paste the URL and ask it to follow the README steps for your tool.

Agent: ask the questions below one at a time and wait for an answer. Three questions, plain language. Do not name SAMHSA, the Dart Center, or OKF in the questions. Do not dump all three at once.

## Question 1: which layer

Ask: **"Does your work involve people who've been through something hard? Shelter, domestic violence, foster care, recovery, crisis response, that kind of thing."**

- Yes, or anything close to yes: **Trauma-informed standard**. It includes everything in the base.
- No, or unsure: **Human-centered language standard**. Say they can add the other layer later without redoing anything.
- If they hesitate or say "sort of," take the yes. The extra practices are quiet when there is nothing for them to catch.

Do not read them the difference between the layers unless they ask. If they ask, answer in two sentences: the base is about writing respectfully about people in general, the trauma-informed standard adds practices for fundraising, storytelling, and crisis content when the people you serve have been through trauma.

## Question 2: where it lives

Ask: **"Do you want this on all your writing, or just one project?"**

Then explain the tradeoff in a line each:

- **Everything.** Install as a skill (Claude) or set it in custom instructions (ChatGPT, Gemini). Applies by default, every conversation.
- **One project.** Put it in a single Claude Project or ChatGPT Project. Applies only inside that workspace. Good if they share an account with people writing about other things.
- **Whole organization.** If they mention a team, or their Claude account is Team or Enterprise, tell them an admin can set policy under **Organization settings → Plugins & skills** so people do not each install it alone.

## Question 3: sector vocabulary

Ask: **"What does your organization work on, in a few words?"**

Match their answer against `okf/standard/vocabulary/`. Files exist for housing, substance use, disability, and mental health, and more may have been added; check the folder. If there's a match, load it and tell them what it does: preferred terms for their field so the standard uses the words their community actually uses. If nothing matches, skip it and say the base vocabulary covers them, and that they can contribute a file for their sector if they want one.

## Install

**Claude, as a skill.** Download `human-centered-language.zip`, `trauma-informed-communications.zip`, or `human-voice.zip` from the latest GitHub release (or fetch this repo in chat and read `packaging/releases/`). Walk them through: left sidebar **Customize → Skills**, **Add → Upload skill**, then select the zip on the **Upload a skill** page (zip must include `SKILL.md`). Skills live under Customize, not Settings. **Settings → Capabilities** varies by plan and may only say skills moved to Customize; do not insist on code execution or file-creation toggles if the account does not show them. Zip upload is the official install. Verified Oct 2026: you can fetch and inspect this public repo in Claude's sandbox; you **cannot** install a skill on the user's account from chat. You may help them choose or assemble the zip and explain upload; they must upload via **Customize → Skills → Add → Upload skill**. Never claim one-click install from a pasted URL.

**Claude, as a project.** Create the project, paste `packaging/compiled/human-centered-language.md` or `trauma-informed-communications.md` into project instructions, and add the sector vocabulary file as a project file.

**ChatGPT.** Create a Project. Open **••• → Project settings** and paste `packaging/chatgpt/human-centered-language.md` or `trauma-informed-communications.md` into the project instructions. Upload the sector vocabulary as a project file. Do not send them to Custom GPTs. Personal Free, Go, Plus, and Pro accounts cannot create new custom GPTs; retirement is scheduled for December 11, 2026 (some Enterprise later). Cite OpenAI Help: [Custom GPT retirement and migration FAQ](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq). Prefer Projects.

**Gemini.** In Gemini Skills (when available), upload `packaging/gemini/human-centered-language.zip` or `trauma-informed-communications.zip` (each contains `SKILL.md` and `standard.md`). Optional human voice: `packaging/gemini/human-voice.zip`. The same release zips under `packaging/releases/` also work if your client accepts them.

**Anything else.** Paste `packaging/compiled/human-centered-language.md` or `trauma-informed-communications.md` as system context.

## Prove it works

Do not stop at "installed." Run one test so they see it do something.

Pull a prompt from `tests/prompts/` that matches their sector, or use their own words if they've already given you a sentence about their work. Show them the output the standard produces and the output it replaced, side by side, and name the one practice that made the difference.

Then say what happens next. Two lines:

- It applies on its own now. They do not have to ask for it. They can also call it by name: "use the human-centered language skill."
- Models change. `MODELS.md` carries a monthly bench of how current models hold up against the standard. Worth a look before they switch models.

## Offer a voice profile

Last step, and only if the install went smoothly. Tell them the standard governs how they write about people, and a voice profile governs how they sound. Offer to build one with `okf/templates/voice-interview.md`. If they say yes, run the interview. If they say not now, leave it.

Their voice profile can set terms and tone. It cannot loosen the standard. Say that once, plainly, because it is the reason the two work together instead of fighting.
