from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .errors import PunkValidationError
from .repository import PunkRepository


@dataclass(frozen=True)
class ValidationIssue:
    level: str
    path: str
    message: str

    def to_mapping(self) -> dict[str, str]:
        return {"level": self.level, "path": self.path, "message": self.message}


def validate_repository(repository: PunkRepository) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    seen_ids: set[str] = set()
    style_ids = repository.style_ids()
    if not style_ids:
        return [ValidationIssue("error", "styles", "no style directories found")]

    for style_id in style_ids:
        relative = f"styles/{style_id}"
        try:
            record = repository.load_style(style_id)
        except PunkValidationError as error:
            issues.append(ValidationIssue("error", relative, str(error)))
            continue
        meta = record.meta
        if meta.id != style_id:
            issues.append(ValidationIssue("error", f"{relative}/META.md", f"metadata id {meta.id!r} does not match directory"))
        if meta.id in seen_ids:
            issues.append(ValidationIssue("error", f"{relative}/META.md", f"duplicate style id: {meta.id}"))
        seen_ids.add(meta.id)
        if not meta.input_modes:
            issues.append(ValidationIssue("error", f"{relative}/META.md", "input_modes is empty"))
        if not meta.subjects:
            issues.append(ValidationIssue("error", f"{relative}/META.md", "subjects is empty"))
        if not meta.outputs:
            issues.append(ValidationIssue("error", f"{relative}/META.md", "outputs is empty"))
        if meta.mode == "cover":
            cover_fields = {
                "style_anchors": meta.style_anchors,
                "cover_shape_adaptation": meta.cover_shape_adaptation,
                "must_preserve": meta.must_preserve,
                "avoid_when_applying_to_cover": meta.avoid_when_applying_to_cover,
            }
            for field_name, values in cover_fields.items():
                if not values:
                    issues.append(ValidationIssue("error", f"{relative}/META.md", f"{field_name} is empty for cover style"))
        for source in meta.source:
            if source.startswith("styles/") and not (repository.root / source).is_file():
                issues.append(ValidationIssue("error", f"{relative}/META.md", f"source does not exist: {source}"))
            elif source.startswith("exports/") and not (repository.root / source).is_file():
                issues.append(ValidationIssue("warning", f"{relative}/META.md", f"archival source is not included: {source}"))

    for mode in ("cover", "avatar"):
        path = repository.blueprint_path(mode)
        if not path.is_file():
            issues.append(ValidationIssue("error", path.relative_to(repository.root).as_posix(), "blueprint is missing"))
    return issues


def error_count(issues: list[ValidationIssue]) -> int:
    return sum(issue.level == "error" for issue in issues)
