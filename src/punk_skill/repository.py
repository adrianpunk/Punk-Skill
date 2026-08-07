from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable

import yaml

from .errors import PunkValidationError
from .models import StyleMeta, StyleRecord

YAML_BLOCK = re.compile(r"```yaml\s*\n(?P<body>[\s\S]*?)\n```", re.IGNORECASE)
PLACEHOLDER = re.compile(r"\{\{[^{}]+\}\}")


def default_repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


class PunkRepository:
    def __init__(self, root: str | Path | None = None):
        self.root = Path(root).expanduser().resolve() if root else default_repository_root()
        self.styles_dir = self.root / "styles"

    def style_ids(self) -> list[str]:
        if not self.styles_dir.is_dir():
            return []
        return sorted(path.name for path in self.styles_dir.iterdir() if path.is_dir())

    def load_style(self, style_id: str) -> StyleRecord:
        directory = self.styles_dir / style_id
        meta_path = directory / "META.md"
        style_path = directory / "STYLE.md"
        if not meta_path.is_file():
            raise PunkValidationError(f"missing metadata: {meta_path.relative_to(self.root)}")
        if not style_path.is_file():
            raise PunkValidationError(f"missing style file: {style_path.relative_to(self.root)}")
        meta_markdown = meta_path.read_text(encoding="utf-8")
        match = YAML_BLOCK.search(meta_markdown)
        if not match:
            raise PunkValidationError(f"missing fenced yaml: {meta_path.relative_to(self.root)}")
        try:
            data = yaml.safe_load(match.group("body"))
        except yaml.YAMLError as error:
            raise PunkValidationError(f"invalid yaml in {meta_path.relative_to(self.root)}: {error}") from error
        if not isinstance(data, dict):
            raise PunkValidationError(f"metadata must be a mapping: {meta_path.relative_to(self.root)}")
        meta = StyleMeta.from_mapping(data)
        return StyleRecord(
            meta=meta,
            meta_path=meta_path,
            style_path=style_path,
            meta_markdown=meta_markdown,
            style_markdown=style_path.read_text(encoding="utf-8"),
        )

    def styles(self, mode: str | None = None) -> list[StyleRecord]:
        records = [self.load_style(style_id) for style_id in self.style_ids()]
        return [record for record in records if mode is None or record.meta.mode == mode]

    def blueprint_path(self, mode: str) -> Path:
        if mode not in {"cover", "avatar"}:
            raise PunkValidationError("mode must be cover or avatar")
        return self.root / "skills" / f"punk-{mode}" / "references" / f"{mode}-prompt-blueprint.md"

    def blueprint(self, mode: str) -> str:
        path = self.blueprint_path(mode)
        if not path.is_file():
            raise PunkValidationError(f"missing blueprint: {path.relative_to(self.root)}")
        return path.read_text(encoding="utf-8")

    def preview_for(self, record: StyleRecord) -> str | None:
        directory = self.root / "screenshots" / f"punk-{record.meta.mode}-styles"
        for suffix in (".png", ".jpg", ".jpeg", ".webp"):
            candidate = directory / f"{record.meta.id}{suffix}"
            if candidate.is_file():
                return candidate.relative_to(self.root).as_posix()
        return None

    def manifest(self, mode: str | None = None) -> dict[str, Any]:
        records = self.styles(mode)
        return {
            "schema_version": 1,
            "style_count": len(records),
            "styles": [record.meta.to_manifest(self.preview_for(record)) for record in records],
        }

    def write_manifest(self, output: str | Path, mode: str | None = None) -> Path:
        destination = Path(output).expanduser().resolve()
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(self.manifest(mode), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return destination


def unresolved_placeholders(text: str) -> list[str]:
    return sorted(set(PLACEHOLDER.findall(text)))


def unique(values: Iterable[str]) -> list[str]:
    return list(dict.fromkeys(values))

