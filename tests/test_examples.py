# SPDX-License-Identifier: Apache-2.0
"""Checks that the worked example tells the truth and that the shipped files are well formed.

Standard library only: python -m unittest discover -s tests
"""
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAMPLE = ROOT / "examples" / "sample-delivery"
SKILL_DIR = ROOT / "skills" / "prove-it-review"

COUNT_SNIPPET = """
from fetcher import fetch
calls = []
def once():
    calls.append(1)
    raise ConnectionError("down")
try:
    fetch(once, retries=%d)
except ConnectionError:
    pass
print(len(calls))
"""


def run(args, cwd):
    proc = subprocess.run([sys.executable, "-B", *args], cwd=str(cwd), capture_output=True)
    return proc.returncode, (proc.stdout + proc.stderr).decode("utf-8", "replace")


class TestWorkedExample(unittest.TestCase):
    def test_delivery_tests_pass(self):
        code, out = run(["-m", "unittest", "-v"], SAMPLE)
        self.assertEqual(code, 0, out)
        self.assertIn("Ran 1 test", out)

    def test_claim_one_is_false_as_the_review_says(self):
        code, out = run(["-c", COUNT_SNIPPET % 3], SAMPLE)
        self.assertEqual(code, 0, out)
        self.assertEqual(out.strip(), "3")  # review-output.md: "attempts: 3", expected 4

    def test_mutant_without_retry_also_passes_the_suite(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            shutil.copy(SAMPLE / "test_fetcher.py", work / "test_fetcher.py")
            (work / "fetcher.py").write_text("def fetch(fetch_once, retries=3):\n    return fetch_once()\n", encoding="utf-8")
            code, out = run(["-m", "unittest", "-v"], work)
        self.assertEqual(code, 0, out)

    def test_review_cites_the_lines_it_names(self):
        review = (ROOT / "examples" / "review-output.md").read_text(encoding="utf-8")
        fetcher_lines = (SAMPLE / "fetcher.py").read_text(encoding="utf-8").splitlines()
        test_lines = (SAMPLE / "test_fetcher.py").read_text(encoding="utf-8").splitlines()
        self.assertIn("range(retries)", fetcher_lines[10])  # fetcher.py:11
        self.assertIn("def test_returns_value_on_first_success", test_lines[8])  # test_fetcher.py:9
        self.assertIn("`fetcher.py:11`", review)
        self.assertIn("`test_fetcher.py:9`", review)

    def test_review_uses_the_documented_finding_format(self):
        review = (ROOT / "examples" / "review-output.md").read_text(encoding="utf-8")
        for field in ("**Verdict:", "**Scope:", "Skipped checks", "VERIFIED", "FALSE", "UNVERIFIED"):
            with self.subTest(field=field):
                self.assertIn(field, review)
        skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        for field in ("**Verdict:**", "**Scope:**", "**Evidence:**", "**Severity:**", "**Skipped checks:**", "**Suggested fix:**"):
            with self.subTest(skill_field=field):
                self.assertIn(field, skill)


class TestShippedFiles(unittest.TestCase):
    @staticmethod
    def frontmatter(path):
        text = path.read_text(encoding="utf-8")
        match = re.match(r"---\n(.*?)\n---\n", text, re.S)
        assert match, "no frontmatter in %s" % path
        return match.group(1)

    def test_skill_frontmatter(self):
        front = self.frontmatter(SKILL_DIR / "SKILL.md")
        self.assertRegex(front, r"(?m)^name: prove-it-review$")
        description = re.search(r'(?m)^description: "(.*)"$', front)
        self.assertIsNotNone(description)
        self.assertTrue(0 < len(description.group(1)) <= 1024)

    def test_skill_directory_name_matches_skill_name(self):
        self.assertEqual(SKILL_DIR.name, "prove-it-review")

    def test_agent_definition(self):
        front = self.frontmatter(ROOT / "agents" / "prove-it-reviewer.md")
        self.assertRegex(front, r"(?m)^name: prove-it-reviewer$")
        self.assertRegex(front, r"(?m)^description: .+")
        self.assertRegex(front, r"(?m)^tools: Read, Grep, Glob, Bash$")
        self.assertIn("- prove-it-review", front)
        self.assertNotRegex(front, r"(?m)^model:")  # model is left to the user; see references/hosts.md

    def test_relative_links_in_skill_resolve(self):
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)#]+)\)", text):
            if "://" in target:
                continue
            with self.subTest(target=target):
                self.assertTrue((SKILL_DIR / target).resolve().exists())

    def test_referenced_script_exists(self):
        self.assertTrue((SKILL_DIR / "scripts" / "sample_bound.py").is_file())
        self.assertIn("scripts/sample_bound.py", (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8"))

    def test_skill_numbers_match_the_script(self):
        sys.path.insert(0, str(SKILL_DIR / "scripts"))
        import sample_bound
        skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("n=40 gives %.1f %%" % (sample_bound.upper_bound(40) * 100), skill)
        self.assertIn("n=10 gives %.1f %%" % (sample_bound.upper_bound(10) * 100), skill)
        # The shortcut quoted for n=10 must be the 3/n value, not the exact bound.
        self.assertIn("(n=10: %.0f %%)" % (sample_bound.rule_of_three(10) * 100), skill)


class TestInstalledLayout(unittest.TestCase):
    """The README tells users to copy only skills/prove-it-review/. Everything the skill points to must still work there."""

    LINK = re.compile(r"\]\(([^)\s]+)\)")

    def test_links_resolve_in_a_copied_skill_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            installed = Path(tmp) / ".claude" / "skills" / "prove-it-review"
            shutil.copytree(SKILL_DIR, installed, ignore=shutil.ignore_patterns("__pycache__"))
            documents = sorted(installed.rglob("*.md"))
            self.assertGreaterEqual(len(documents), 3)
            checked = 0
            for document in documents:
                for target in self.LINK.findall(document.read_text(encoding="utf-8")):
                    if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                        continue  # absolute URL or in-page anchor
                    with self.subTest(document=document.relative_to(installed).as_posix(), target=target):
                        resolved = (document.parent / target.split("#")[0]).resolve()
                        self.assertTrue(resolved.exists(), "dangling link after install")
                        self.assertTrue(installed.resolve() in resolved.parents or resolved == installed.resolve())
                        checked += 1
            self.assertGreaterEqual(checked, 3)

    def test_skill_text_does_not_point_outside_its_folder(self):
        for document in sorted(SKILL_DIR.rglob("*.md")):
            with self.subTest(document=document.relative_to(SKILL_DIR).as_posix()):
                text = document.read_text(encoding="utf-8")
                self.assertNotIn("](../../", text)  # a link that leaves skills/prove-it-review/
                self.assertNotIn("](/", text)

    def test_script_runs_from_a_copied_skill_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            installed = Path(tmp) / "prove-it-review"
            shutil.copytree(SKILL_DIR, installed, ignore=shutil.ignore_patterns("__pycache__"))
            code, out = run(["-I", str(installed / "scripts" / "sample_bound.py"), "40"], installed)
        self.assertEqual(code, 0, out)
        self.assertIn("7.2%", out)


if __name__ == "__main__":
    unittest.main()
