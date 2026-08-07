from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

from .errors import PunkValidationError


def _strings(value: Any, field_name: str) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise PunkValidationError(f"{field_name} must be a list of strings")
    return tuple(value)


@dataclass(frozen=True)
class StyleMeta:
    id: str
    name: str
    input_modes: tuple[str, ...]
    subjects: tuple[str, ...]
    outputs: tuple[str, ...]
    default_ratio: str
    required_fields: tuple[str, ...]
    optional_fields: tuple[str, ...]
    source: tuple[str, ...]
    style_anchors: tuple[str, ...] = ()
    cover_shape_adaptation: tuple[str, ...] = ()
    must_preserve: tuple[str, ...] = ()
    avoid_when_applying_to_cover: tuple[str, ...] = ()
    extra: Mapping[str, Any] = field(default_factory=dict, compare=False)

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "StyleMeta":
        required = ("id", "name", "input_modes", "subjects", "outputs", "default_ratio", "required_fields", "optional_fields", "source")
        missing = [key for key in required if key not in data]
        if missing:
            raise PunkValidationError(f"missing metadata fields: {', '.join(missing)}")
        if not isinstance(data["id"], str) or not data["id"].strip():
            raise PunkValidationError("id must be a non-empty string")
        if not isinstance(data["name"], str) or not data["name"].strip():
            raise PunkValidationError("name must be a non-empty string")
        if not isinstance(data["default_ratio"], str) or not data["default_ratio"].strip():
            raise PunkValidationError("default_ratio must be a non-empty string")
        source_value = data["source"]
        if isinstance(source_value, str):
            source = (source_value.strip(),) if source_value.strip() else ()
        elif isinstance(source_value, list) and all(isinstance(item, str) and item.strip() for item in source_value):
            source = tuple(item.strip() for item in source_value)
        else:
            source = ()
        if not source:
            raise PunkValidationError("source must be a non-empty string or list of strings")

        known = set(required) | {
            "style_anchors",
            "cover_shape_adaptation",
            "must_preserve",
            "avoid_when_applying_to_cover",
        }
        return cls(
            id=data["id"].strip(),
            name=data["name"].strip(),
            input_modes=_strings(data["input_modes"], "input_modes"),
            subjects=_strings(data["subjects"], "subjects"),
            outputs=_strings(data["outputs"], "outputs"),
            default_ratio=data["default_ratio"].strip(),
            required_fields=_strings(data["required_fields"], "required_fields"),
            optional_fields=_strings(data["optional_fields"], "optional_fields"),
            source=source,
            style_anchors=_strings(data.get("style_anchors"), "style_anchors"),
            cover_shape_adaptation=_strings(data.get("cover_shape_adaptation"), "cover_shape_adaptation"),
            must_preserve=_strings(data.get("must_preserve"), "must_preserve"),
            avoid_when_applying_to_cover=_strings(data.get("avoid_when_applying_to_cover"), "avoid_when_applying_to_cover"),
            extra={key: value for key, value in data.items() if key not in known},
        )

    @property
    def mode(self) -> str:
        return "cover" if {"cover", "poster"}.intersection(self.outputs) else "avatar"

    def to_manifest(self, preview: str | None = None) -> dict[str, Any]:
        result: dict[str, Any] = {
            "id": self.id,
            "name": self.name,
            "mode": self.mode,
            "input_modes": list(self.input_modes),
            "subjects": list(self.subjects),
            "outputs": list(self.outputs),
            "default_ratio": self.default_ratio,
            "required_fields": list(self.required_fields),
            "optional_fields": list(self.optional_fields),
        }
        if preview:
            result["preview"] = preview
        return result


@dataclass(frozen=True)
class StyleRecord:
    meta: StyleMeta
    meta_path: Path
    style_path: Path
    meta_markdown: str
    style_markdown: str


@dataclass
class GenerationJob:
    mode: str
    style_id: str
    prompt: str
    ratio: str = ""
    platform: str = ""
    subtitle: str = ""
    language: str = "zh-CN"
    use_case: str = ""
    mood: str = ""
    summary: str = ""
    visual_subject: str = ""
    audience: str = ""
    metaphor: str = ""
    banned_elements: str = ""
    source_image: str = ""
    output_dir: str = ""
    provider: str = "apimart"
    fields: dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "GenerationJob":
        if not isinstance(data, Mapping):
            raise PunkValidationError("job must be a mapping")
        mode = str(data.get("mode", "")).strip()
        style_id = str(data.get("style_id", "")).strip()
        prompt = str(
            data.get("prompt")
            or data.get("title")
            or data.get("title_or_topic")
            or data.get("subject")
            or data.get("description")
            or ""
        ).strip()
        if mode not in {"cover", "avatar"}:
            raise PunkValidationError("mode must be cover or avatar")
        if not style_id:
            raise PunkValidationError("style_id is required")
        if not prompt:
            raise PunkValidationError("prompt, title, or subject is required")
        raw_fields = data.get("fields") or {}
        if not isinstance(raw_fields, Mapping):
            raise PunkValidationError("fields must be a mapping")

        string_fields = {
            "ratio",
            "platform",
            "subtitle",
            "language",
            "use_case",
            "mood",
            "summary",
            "visual_subject",
            "audience",
            "metaphor",
            "banned_elements",
            "source_image",
            "output_dir",
            "provider",
        }
        values = {key: str(data.get(key, "")).strip() for key in string_fields}
        values["language"] = values["language"] or "zh-CN"
        values["provider"] = values["provider"] or "apimart"
        return cls(
            mode=mode,
            style_id=style_id,
            prompt=prompt,
            fields={str(key): str(value) for key, value in raw_fields.items()},
            **values,
        )

    def to_mapping(self) -> dict[str, Any]:
        return {
            "mode": self.mode,
            "style_id": self.style_id,
            "prompt": self.prompt,
            "ratio": self.ratio,
            "platform": self.platform,
            "subtitle": self.subtitle,
            "language": self.language,
            "use_case": self.use_case,
            "mood": self.mood,
            "summary": self.summary,
            "visual_subject": self.visual_subject,
            "audience": self.audience,
            "metaphor": self.metaphor,
            "banned_elements": self.banned_elements,
            "source_image": self.source_image,
            "output_dir": self.output_dir,
            "provider": self.provider,
            "fields": dict(self.fields),
        }
