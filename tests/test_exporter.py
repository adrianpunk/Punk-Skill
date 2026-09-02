from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from punk_skill.exporter import export_xingji
from punk_skill.repository import PunkRepository


ROOT = Path(__file__).resolve().parents[1]


class ExporterTests(unittest.TestCase):
    def test_export_contains_runtime_and_public_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = export_xingji(PunkRepository(ROOT), directory)
            runtime = Path(result["runtime"])
            self.assertTrue((runtime / "src" / "punk_skill" / "cli.py").is_file())
            self.assertTrue((runtime / "styles" / "anthropic-research-style" / "META.json").is_file())
            manifest = json.loads(Path(result["public_manifest"]).read_text(encoding="utf-8"))
            self.assertEqual(manifest["style_count"], 28)


if __name__ == "__main__":
    unittest.main()
