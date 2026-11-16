#!/usr/bin/env python3
"""Strict checks on every SKILL.md we ship, loose or zipped.

Claude, Gemini and Microsoft 365 Copilot Chat all read the same SKILL.md
format. A front matter block that a strict YAML parser rejects can fail the
upload, so this test parses with PyYAML safe_load, not a line scanner.

Checks, per the shared skill format (Microsoft documents the same limits):
- front matter is --- delimited YAML that safe_load accepts
- name: 1-64 chars, lowercase letters, digits, single hyphens
- name matches its folder (or zip stem, except legacy alias zips)
- description: string, 1-1,024 chars
- zips: SKILL.md at the zip root, no enclosing folder, no directories
"""
import re
import unittest
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

SKILL_DIRS = (
    ROOT / "plugins",
    ROOT / "packaging" / "claude-skill",
    ROOT / "packaging" / "gemini",
)
ZIP_DIRS = (
    ROOT / "packaging" / "releases",
    ROOT / "packaging" / "gemini",
)
# Legacy alias zips are byte copies of the current zips under old file names
# (see LAYERS legacy_zip in scripts/build.py). Their stem can't match the name.
LEGACY_ALIAS_ZIPS = {"dignified-language.zip", "trauma-informed.zip"}


def front_matter(text):
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise AssertionError("SKILL.md must start with --- delimited front matter")
    return yaml.safe_load(match.group(1))


class SkillFrontMatterTests(unittest.TestCase):
    def check_skill(self, text, expected_name, where):
        data = front_matter(text)
        self.assertIsInstance(data, dict, where)
        name = data.get("name")
        desc = data.get("description")
        self.assertIsInstance(name, str, f"{where}: name")
        self.assertTrue(1 <= len(name) <= 64, f"{where}: name length")
        self.assertRegex(name, NAME_RE, f"{where}: name format")
        if expected_name is not None:
            self.assertEqual(name, expected_name, f"{where}: name must match folder")
        self.assertIsInstance(desc, str, f"{where}: description")
        self.assertTrue(1 <= len(desc) <= 1024, f"{where}: description length")

    def test_skill_folders(self):
        found = 0
        for base in SKILL_DIRS:
            for skill_md in sorted(base.glob("*/SKILL.md")):
                found += 1
                with self.subTest(path=str(skill_md.relative_to(ROOT))):
                    self.check_skill(
                        skill_md.read_text(encoding="utf-8"),
                        skill_md.parent.name,
                        str(skill_md.relative_to(ROOT)),
                    )
        self.assertGreater(found, 0)

    def test_skill_zips(self):
        found = 0
        for base in ZIP_DIRS:
            for zip_path in sorted(base.glob("*.zip")):
                found += 1
                where = str(zip_path.relative_to(ROOT))
                with self.subTest(path=where), zipfile.ZipFile(zip_path) as zf:
                    names = [i.filename for i in zf.infolist()]
                    self.assertIn("SKILL.md", names, f"{where}: SKILL.md must be at the zip root")
                    for n in names:
                        self.assertNotIn("/", n, f"{where}: no folders inside the zip ({n})")
                        self.assertFalse(n.startswith(".") or "__MACOSX" in n, f"{where}: {n}")
                    expected = None if zip_path.name in LEGACY_ALIAS_ZIPS else zip_path.stem
                    self.check_skill(zf.read("SKILL.md").decode("utf-8"), expected, where)
        self.assertGreater(found, 0)


if __name__ == "__main__":
    unittest.main()
