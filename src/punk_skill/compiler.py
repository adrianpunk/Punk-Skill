from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable

from .errors import PunkValidationError
from .models import GenerationJob, StyleMeta, StyleRecord
from .repository import PLACEHOLDER, PunkRepository, unresolved_placeholders

HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


@dataclass(frozen=True)
class CompileResult:
    prompt: str
    job: GenerationJob
    style: StyleMeta

    def to_mapping(self) -> dict[str, object]:
        return {
            "prompt": self.prompt,
            "job": self.job.to_mapping(),
            "style": self.style.to_manifest(),
        }


def _platform_ratio(platform: str) -> str:
    normalized = platform.lower().replace(" ", "")
    if any(token in normalized for token in ("xiaohongshu", "小红书", "xhs")):
        return "3:4"
    if any(token in normalized for token in ("wechat", "微信公众号", "公众号")):
        return "2.35:1"
    if normalized in {"x", "twitter", "x/twitter"} or "twitter" in normalized:
        return "5:2"
    return ""


def resolve_ratio(job: GenerationJob, meta: StyleMeta) -> str:
    if job.ratio:
        return job.ratio
    if job.mode == "avatar":
        return "1:1"
    ratio = _platform_ratio(job.platform)
    if ratio:
        return ratio
    raise PunkValidationError("cover job requires ratio or a known platform")


def _field_match(label: str, fields: dict[str, str]) -> str:
    normalized = label.replace(" ", "").lower()
    for key, value in fields.items():
        key_normalized = key.replace(" ", "").lower()
        if key_normalized == normalized or key_normalized in normalized or normalized in key_normalized:
            if value.strip():
                return value.strip()
    return ""


def _common_value(label: str, job: GenerationJob, ratio: str) -> str:
    direct = _field_match(label, job.fields)
    if direct:
        return direct
    text = label.lower()
    if any(token in text for token in ("上传", "照片", "图片", "引用路径", "source image")):
        return job.source_image
    if any(token in text for token in ("画幅", "比例", "aspect")):
        return ratio
    if any(token in text for token in ("副标题", "subtitle")):
        return job.subtitle
    if any(token in text for token in ("语言", "language")):
        return job.language
    if any(token in text for token in ("用途", "平台", "use case")):
        return job.use_case or job.platform or ("文章封面" if job.mode == "cover" else "头像")
    if any(token in text for token in ("不想出现", "禁用", "避免", "avoid")):
        return job.banned_elements
    if any(token in text for token in ("情绪", "气质", "mood")):
        return job.mood
    if any(token in text for token in ("补充背景", "内容背景", "行业", "场景", "context")):
        return job.summary
    if any(token in text for token in ("隐喻", "metaphor")):
        return job.metaphor
    if any(token in text for token in ("视觉主体", "核心主体", "主体类型", "主视觉物件")):
        return job.visual_subject or job.prompt
    if any(token in text for token in ("主题", "主标题", "核心文字", "主题词", "核心表达")):
        return job.prompt
    return ""


def _required_value(field_name: str, job: GenerationJob, ratio: str) -> str:
    return _common_value(field_name, job, ratio)


def validate_job_for_style(job: GenerationJob, record: StyleRecord, ratio: str) -> None:
    if record.meta.mode != job.mode:
        raise PunkValidationError(
            f"style {record.meta.id} belongs to {record.meta.mode}, not {job.mode}"
        )
    if "image" in record.meta.input_modes and "text" not in record.meta.input_modes and not job.source_image:
        raise PunkValidationError(f"style {record.meta.id} requires source_image")
    missing = [
        field_name
        for field_name in record.meta.required_fields
        if not _required_value(field_name, job, ratio)
    ]
    if missing:
        raise PunkValidationError(
            f"job is missing required fields for {record.meta.id}: {', '.join(missing)}"
        )


def _placeholder_value(label: str, job: GenerationJob, ratio: str) -> str:
    value = _common_value(label, job, ratio)
    if value:
        return value
    if "可留空" in label:
        return "无"
    if "填写" in label and _field_match(label.replace("填写", ""), job.fields):
        return _field_match(label.replace("填写", ""), job.fields)
    return "根据主题和所选风格自动判断"


def _fill_placeholders(text: str, job: GenerationJob, ratio: str) -> str:
    return PLACEHOLDER.sub(lambda match: _placeholder_value(match.group(0)[2:-2].strip(), job, ratio), text)


def _remove_input_variables(style_markdown: str) -> str:
    lines = style_markdown.splitlines()
    output: list[str] = []
    skipping_level: int | None = None
    for index, line in enumerate(lines):
        match = HEADING.match(line)
        if index == 0 and match and len(match.group(1)) == 1:
            continue
        if match:
            level = len(match.group(1))
            title = match.group(2).strip().lower()
            if skipping_level is not None and level <= skipping_level:
                skipping_level = None
            if title in {"输入变量", "input variables"}:
                skipping_level = level
                continue
        if skipping_level is None:
            output.append(line)
    return "\n".join(output).strip()


def _bullets(values: Iterable[str], fallback: str = "Follow the selected style atom.") -> str:
    items = [value.strip() for value in values if value.strip()]
    if not items:
        return f"- {fallback}"
    return "\n".join(f"- {value}" for value in items)


def _cover_prompt(job: GenerationJob, record: StyleRecord, ratio: str, style_body: str) -> str:
    meta = record.meta
    platform = job.platform or "custom platform"
    summary = job.summary or "Use the title and supplied fields only."
    subject = job.visual_subject or "Derive one visual subject from the title."
    mood = job.mood or "Follow the selected style."
    metaphor = job.metaphor or "Derive one visual metaphor from the title."
    banned = job.banned_elements or "watermarks, platform UI, unrelated decoration"
    subtitle = job.subtitle or "None"
    return f"""# {meta.name} cover generation brief

Create one single {platform} cover image. Aspect ratio: {ratio}.
Use one style only: {meta.name} / {meta.id}.

## Content

- Main title or topic: {job.prompt}
- Subtitle: {subtitle}
- Language: {job.language}
- Use case: {job.use_case or platform}
- Context summary: {summary}
- Visual subject: {subject}
- Audience: {job.audience or "General readers of the target platform"}
- Mood: {mood}
- Visual metaphor: {metaphor}
- Banned elements: {banned}

The complete main title must remain readable and accurate. Use only the supplied fields. Do not copy a long article body into the image or small-text system.

## Style anchors

{_bullets(meta.style_anchors)}

## Cover adaptation

{_bullets(meta.cover_shape_adaptation)}

## Must preserve

{_bullets(meta.must_preserve)}

## Style implementation

{style_body}

## Negative constraints

{_bullets(meta.avoid_when_applying_to_cover)}
- Avoid: {banned}.
- No generic PPT cover, course cover, e-commerce advertisement, contact sheet, grid, watermark, or extra option.
- Do not combine a second style.

## Final output

Generate one final image only. Do not output explanations or alternatives.
""".strip() + "\n"


def _avatar_prompt(job: GenerationJob, record: StyleRecord, ratio: str, style_body: str) -> str:
    meta = record.meta
    source_mode = "image-based" if job.source_image else "description-based"
    return f"""# {meta.name} avatar generation brief

Create one single avatar or avatar-derived keepsake image. Aspect ratio: {ratio}.
Use one style only: {meta.name} / {meta.id}.

## Subject

- Generation mode: {source_mode}
- Subject description: {job.prompt}
- Source image: {job.source_image or "None"}
- Intended use: {job.use_case or "profile image"}
- Mood: {job.mood or "Follow the selected style."}
- Background preference: {job.fields.get("背景", "Simplified background")}
- Preserve: {job.fields.get("保留", "Recognizable subject traits")}
- Avoid: {job.banned_elements or "complex background and unrelated subjects"}

For image-based input, preserve recognizable traits while translating them into the selected style. For description-based input, follow the supplied description without claiming photo likeness.

## Style implementation

{style_body}

## Avatar constraints

- Keep a clear silhouette and safe crop at profile-picture size.
- Do not crop important facial features, ears, paws, hair, accessories, or object edges.
- Use one primary subject unless the user explicitly supplied more.
- Do not use cover-title hierarchy, poster layout, grids, contact sheets, or unrelated text.
- Do not combine a second style.

## Final output

Generate one final image only. Do not output explanations or alternatives.
""".strip() + "\n"


def compile_prompt(repository: PunkRepository, job: GenerationJob) -> CompileResult:
    record = repository.load_style(job.style_id)
    ratio = resolve_ratio(job, record.meta)
    job.ratio = ratio
    validate_job_for_style(job, record, ratio)
    style_body = _fill_placeholders(_remove_input_variables(record.style_markdown), job, ratio)
    prompt = (
        _cover_prompt(job, record, ratio, style_body)
        if job.mode == "cover"
        else _avatar_prompt(job, record, ratio, style_body)
    )
    unresolved = unresolved_placeholders(prompt)
    if unresolved:
        raise PunkValidationError(f"compiled prompt contains unresolved placeholders: {', '.join(unresolved)}")
    return CompileResult(prompt=prompt, job=job, style=record.meta)

