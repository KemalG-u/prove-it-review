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
SKILL_DIR = ROOT / "skills" / "adversarial-review"

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
        self.assertRegex(front, r"(?m)^name: adversarial-review$")
        description = re.search(r'(?m)^description: "(.*)"$', front)
        self.assertIsNotNone(description)
        self.assertTrue(0 < len(description.group(1)) <= 1024)

    def test_skill_directory_name_matches_skill_name(self):
        self.assertEqual(SKILL_DIR.name, "adversarial-review")

    def test_agent_definition(self):
        front = self.frontmatter(ROOT / "agents" / "adversarial-reviewer.md")
        self.assertRegex(front, r"(?m)^name: adversarial-reviewer$")
        self.assertRegex(front, r"(?m)^description: .+")
        self.assertRegex(front, r"(?m)^tools: Read, Grep, Glob, Bash$")
        self.assertIn("- adversarial-review", front)
        self.assertNotRegex(front, r"(?m)^model:")  # model is left to the user; see references/hosts.md

    def test_relative_links_in_skill_resolve(self):
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)#]+)\)", text):
            if "://" in target:
                continue
            with self.subTest(target=target):
                self.assertTrue((SKILL_DIR / target).resolve().exists())

    def test_referenced_script_exists(self):
        self.assertTrue((ROOT / "scripts" / "sample_bound.py").is_file())
        self.assertIn("scripts/sample_bound.py", (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8"))

    def test_skill_numbers_match_the_script(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        import sample_bound
        skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("n=40 gives %.1f %%" % (sample_bound.upper_bound(40) * 100), skill)
        self.assertIn("n=10 gives %.1f %%" % (sample_bound.upper_bound(10) * 100), skill)


if __name__ == "__main__":
    unittest.main()
