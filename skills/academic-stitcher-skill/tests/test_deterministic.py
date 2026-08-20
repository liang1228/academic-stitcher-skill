from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run_script(name: str, *args: str, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / name), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
    )


class DeterministicReleaseTests(unittest.TestCase):
    def test_context_pack_builds_from_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "input.jsonl"
            result = run_script(
                "build_ctx2skill_input.py", "--root", str(ROOT), "--output", str(output)
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            record = json.loads(output.read_text(encoding="utf-8"))
            included = record["metadata"]["included_files"]
            self.assertIn("SKILL.md", included)
            self.assertIn("static/core/stance.md", included)
            self.assertNotIn("references/transcript-derived-playbook.md", included)

    def test_context_pack_rejects_root_escape_and_absolute_path(self) -> None:
        bad_paths = ("../outside.md", str(Path(tempfile.gettempdir()) / "outside.md"))
        for bad_path in bad_paths:
            with self.subTest(path=bad_path), tempfile.TemporaryDirectory() as tmp:
                tmp_path = Path(tmp)
                copied = tmp_path / "skill"
                shutil.copytree(ROOT, copied)
                manifest_path = copied / "manifest.yaml"
                manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
                manifest["always_load"].append(bad_path)
                manifest_path.write_text(
                    yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False), encoding="utf-8"
                )
                output = tmp_path / "escaped.jsonl"
                result = subprocess.run(
                    [
                        sys.executable,
                        str(copied / "scripts/build_ctx2skill_input.py"),
                        "--root",
                        str(copied),
                        "--output",
                        str(output),
                    ],
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(output.exists())
                self.assertIn("manifest path", (result.stdout + result.stderr).lower())

    def test_zero_task_run_is_not_completed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_file = Path(tmp) / "zero.jsonl"
            run_file.write_text(
                json.dumps({"context_id": "zero", "task_results": []}) + "\n", encoding="utf-8"
            )
            result = run_script(
                "summarize_ctx2skill_run.py",
                "--input",
                str(run_file),
                "--fail-on-warning",
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Run status: not completed", result.stdout)
            self.assertIn("zero task results", result.stdout)

    def test_malformed_and_empty_runs_fail_with_warning_gate(self) -> None:
        for content in ("", "{not-json}\n", "Please set --api-key first\n"):
            with self.subTest(content=content), tempfile.TemporaryDirectory() as tmp:
                run_file = Path(tmp) / "bad.jsonl"
                run_file.write_text(content, encoding="utf-8")
                result = run_script(
                    "summarize_ctx2skill_run.py",
                    "--input",
                    str(run_file),
                    "--fail-on-warning",
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("Run status: not completed", result.stdout)

    def test_failed_judge_is_nonzero_with_warning_gate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_file = Path(tmp) / "failed.jsonl"
            record = {
                "context_id": "failed",
                "task_results": [
                    {"task_idx": 0, "requirement_status": ["yes", "no"], "judge_score": 0}
                ],
            }
            run_file.write_text(json.dumps(record) + "\n", encoding="utf-8")
            result = run_script(
                "summarize_ctx2skill_run.py",
                "--input",
                str(run_file),
                "--fail-on-warning",
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Run status: completed with failures", result.stdout)

    def test_custom_key_is_forwarded_without_log_leak(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            fake = tmp_path / "fake_selfplay.py"
            fake_lines = [
                "import argparse, json, os",
                "from pathlib import Path",
                "p=argparse.ArgumentParser()",
                "p.add_argument('--input'); p.add_argument('--output'); p.add_argument('--skills-dir')",
                "p.add_argument('--max-samples'); p.add_argument('--num-iterations'); p.add_argument('--num-tasks'); p.add_argument('--workers')",
                "p.add_argument('--base-url'); p.add_argument('--challenger-model'); p.add_argument('--reasoner-model')",
                "p.add_argument('--judge-model'); p.add_argument('--proposer-model'); p.add_argument('--generator-model')",
                "p.add_argument('--skip-skill-selection', action='store_true')",
                "a=p.parse_args()",
                "assert os.environ.get('OPENAI_API_KEY') == os.environ.get('CUSTOM_TEST_KEY')",
                "Path(a.output).parent.mkdir(parents=True, exist_ok=True)",
                "record={'context_id':'fake','task_results':[{'task_idx':0,'requirement_status':['yes'],'judge_score':1}]}",
                "Path(a.output).write_text(json.dumps(record)+'\\n', encoding='utf-8')",
            ]
            fake.write_text("\n".join(fake_lines) + "\n", encoding="utf-8")
            secret = "unit-test-secret-value"
            env = os.environ.copy()
            env.pop("OPENAI_API_KEY", None)
            env["CUSTOM_TEST_KEY"] = secret
            work = tmp_path / "work"
            result = run_script(
                "run_ctx2skill_selfplay.py",
                "--root",
                str(ROOT),
                "--work-dir",
                str(work),
                "--selfplay-cmd",
                str(fake),
                "--api-key-env",
                "CUSTOM_TEST_KEY",
                env=env,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            combined = result.stdout + result.stderr
            for path in work.rglob("*"):
                if path.is_file():
                    combined += path.read_text(encoding="utf-8", errors="replace")
            self.assertNotIn(secret, combined)
            self.assertIn("Run status: completed", combined)

    def test_package_validator_passes(self) -> None:
        result = run_script("validate_package.py", str(ROOT), "--json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["version"], "2.4.0")

    def test_story_architecture_route_is_declared(self) -> None:
        manifest = yaml.safe_load((ROOT / "manifest.yaml").read_text(encoding="utf-8"))
        route_path = manifest["axes"]["route"]["values"]["story-architecture"]
        story_file = ROOT / route_path
        self.assertTrue(story_file.is_file())
        story_text = story_file.read_text(encoding="utf-8")
        for required in ("Story Spine", "Claim-Evidence-Boundary Map", "Reviewer Stress Test"):
            self.assertIn(required, story_text)

    def test_claim_driven_experiment_route_is_declared(self) -> None:
        manifest = yaml.safe_load((ROOT / "manifest.yaml").read_text(encoding="utf-8"))
        route_path = manifest["axes"]["route"]["values"]["claim-driven-experiment"]
        route_file = ROOT / route_path
        self.assertTrue(route_file.is_file())
        route_text = route_file.read_text(encoding="utf-8")
        for required in (
            "Claim Ladder",
            "Claim-Evidence-Experiment Matrix",
            "Run Order And Decision Gates",
            "Analysis And Failure Reflux",
        ):
            self.assertIn(required, route_text)


if __name__ == "__main__":
    unittest.main()
