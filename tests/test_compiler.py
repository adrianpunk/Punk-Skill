from __future__ import annotations

import unittest
from pathlib import Path

from punk_skill.compiler import compile_prompt
from punk_skill.errors import PunkValidationError
from punk_skill.models import GenerationJob
from punk_skill.repository import PunkRepository, unresolved_placeholders


ROOT = Path(__file__).resolve().parents[1]


class CompilerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = PunkRepository(ROOT)

    def test_cover_prompt_is_compiled(self) -> None:
        job = GenerationJob.from_mapping({
            "mode": "cover",
            "style_id": "anthropic-research-style",
            "title": "AI Agent 正在改变内容生产方式",
            "platform": "微信公众号",
            "summary": "一篇讨论 Agent 如何改变内容工作流的文章。",
            "metaphor": "一条手绘路径连接多个知识节点",
        })
        result = compile_prompt(self.repository, job)
        self.assertEqual(result.job.ratio, "2.35:1")
        self.assertIn(job.prompt, result.prompt)
        self.assertIn("anthropic-research-style", result.prompt)
        self.assertEqual(unresolved_placeholders(result.prompt), [])

    def test_avatar_prompt_is_compiled(self) -> None:
        job = GenerationJob.from_mapping({
            "mode": "avatar",
            "style_id": "pixel-avatar",
            "subject": "一只戴蓝色帽子的橘猫",
            "source_image": "/tmp/cat.png",
        })
        result = compile_prompt(self.repository, job)
        self.assertEqual(result.job.ratio, "1:1")
        self.assertIn("image-based", result.prompt)
        self.assertEqual(unresolved_placeholders(result.prompt), [])

    def test_cover_requires_platform_or_ratio(self) -> None:
        job = GenerationJob.from_mapping({
            "mode": "cover",
            "style_id": "black-white-minimal-concept",
            "title": "测试标题",
        })
        with self.assertRaises(PunkValidationError):
            compile_prompt(self.repository, job)

    def test_style_mode_must_match(self) -> None:
        job = GenerationJob.from_mapping({
            "mode": "cover",
            "style_id": "pixel-avatar",
            "title": "测试标题",
            "ratio": "1:1",
            "source_image": "/tmp/input.png",
        })
        with self.assertRaises(PunkValidationError):
            compile_prompt(self.repository, job)

    def test_every_cover_style_resolves_placeholders(self) -> None:
        for record in self.repository.styles("cover"):
            fields = {field: "自动判断" for field in record.meta.required_fields + record.meta.optional_fields}
            job = GenerationJob.from_mapping({
                "mode": "cover",
                "style_id": record.meta.id,
                "title": "结构化生图测试",
                "ratio": "5:2",
                "fields": fields,
            })
            result = compile_prompt(self.repository, job)
            self.assertEqual(unresolved_placeholders(result.prompt), [], record.meta.id)

    def test_every_avatar_style_resolves_placeholders(self) -> None:
        for record in self.repository.styles("avatar"):
            fields = {field: "自动判断" for field in record.meta.required_fields + record.meta.optional_fields}
            job = GenerationJob.from_mapping({
                "mode": "avatar",
                "style_id": record.meta.id,
                "subject": "一只用于结构化测试的宠物",
                "source_image": "/tmp/input.png",
                "fields": fields,
            })
            result = compile_prompt(self.repository, job)
            self.assertEqual(unresolved_placeholders(result.prompt), [], record.meta.id)


if __name__ == "__main__":
    unittest.main()
