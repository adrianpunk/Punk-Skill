from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from punk_skill.providers.apimart import APIMartConfig, APIMartProvider, normalize_ratio


class FakeProvider(APIMartProvider):
    def __init__(self, responses: list[dict]):
        super().__init__(
            APIMartConfig(api_key="TOKEN", timeout_seconds=2, poll_interval_seconds=0),
            sleep=lambda _seconds: None,
        )
        self.responses = list(responses)
        self.requests: list[tuple[str, str, dict | None]] = []

    def _request_json(self, url: str, method: str = "GET", payload: dict | None = None) -> dict:
        self.requests.append((url, method, payload))
        return self.responses.pop(0)

    def _download(self, source_url: str, output_stem: Path) -> Path:
        destination = output_stem.with_suffix(".png")
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(b"PNG")
        return destination


class APIMartTests(unittest.TestCase):
    def test_ratio_normalization(self) -> None:
        self.assertEqual(normalize_ratio("2.35:1"), "21:9")
        self.assertEqual(normalize_ratio("5:2"), "21:9")
        self.assertEqual(normalize_ratio("3:4"), "3:4")

    def test_immediate_result(self) -> None:
        provider = FakeProvider([{"data": [{"url": "https://example.test/image.png"}]}])
        with tempfile.TemporaryDirectory() as directory:
            result = provider.generate("prompt", "3:4", Path(directory) / "cover")
            self.assertTrue(result.saved_path.is_file())
        self.assertEqual(provider.requests[0][1], "POST")
        self.assertEqual(provider.requests[0][2]["size"], "3:4")

    def test_task_polling_result(self) -> None:
        provider = FakeProvider([
            {"data": [{"task_id": "task-1"}]},
            {"data": {"status": "processing"}},
            {"data": {"status": "completed", "result": {"images": [{"url": ["https://example.test/final.png"]}]}}},
        ])
        with tempfile.TemporaryDirectory() as directory:
            result = provider.generate("prompt", "2.35:1", Path(directory) / "cover")
            self.assertEqual(result.task_id, "task-1")
            self.assertTrue(result.saved_path.is_file())
        self.assertEqual(len(provider.requests), 3)


if __name__ == "__main__":
    unittest.main()
