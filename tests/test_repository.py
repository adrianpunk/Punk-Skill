from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from punk_skill.repository import PunkRepository
from punk_skill.validator import error_count, validate_repository


ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = PunkRepository(ROOT)

    def test_current_repository_validates(self) -> None:
        issues = validate_repository(self.repository)
        self.assertEqual(error_count(issues), 0, issues)
        self.assertEqual(len(self.repository.styles("cover")), 23)
        self.assertEqual(len(self.repository.styles("avatar")), 5)

    def test_manifest_contains_all_styles(self) -> None:
        manifest = self.repository.manifest()
        self.assertEqual(manifest["style_count"], 28)
        ids = {item["id"] for item in manifest["styles"]}
        self.assertIn("anthropic-research-style", ids)
        self.assertIn("pixel-avatar", ids)

    def test_manifest_can_be_written(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "manifest.json"
            self.repository.write_manifest(output)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(payload["schema_version"], 1)
            self.assertEqual(payload["style_count"], 28)


if __name__ == "__main__":
    unittest.main()
