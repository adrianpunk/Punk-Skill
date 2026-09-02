from __future__ import annotations

import json
import shutil
from pathlib import Path

from .repository import PunkRepository


def _copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def export_xingji(repository: PunkRepository, project_root: str | Path) -> dict[str, str | int]:
    target = Path(project_root).expanduser().resolve()
    runtime = target / "resources" / "punk-runtime"
    public_library = target / "public" / "punk-library"
    public_previews = target / "public" / "punk-previews"

    if runtime.exists():
        shutil.rmtree(runtime)
    runtime.mkdir(parents=True, exist_ok=True)

    shutil.copytree(repository.root / "src" / "punk_skill", runtime / "src" / "punk_skill", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    for mode in ("cover", "avatar"):
        blueprint = repository.blueprint_path(mode)
        relative = blueprint.relative_to(repository.root)
        _copy_file(blueprint, runtime / relative)
        _copy_file(blueprint, public_library / "blueprints" / blueprint.name)

    for record in repository.styles():
        style_runtime = runtime / "styles" / record.meta.id
        style_public = public_library / "styles" / record.meta.id
        for destination in (style_runtime, style_public):
            _copy_file(record.meta_path, destination / "META.md")
            _copy_file(record.style_path, destination / "STYLE.md")
        (style_runtime / "META.json").write_text(
            json.dumps(record.meta.to_mapping(), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

        preview = repository.preview_for(record)
        if preview:
            source = repository.root / preview
            _copy_file(source, public_previews / f"punk-{record.meta.mode}-styles" / source.name)

    manifest = repository.manifest()
    manifest_text = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    (runtime / "manifest.json").write_text(manifest_text, encoding="utf-8")
    public_library.mkdir(parents=True, exist_ok=True)
    (public_library / "manifest.json").write_text(manifest_text, encoding="utf-8")
    return {
        "style_count": manifest["style_count"],
        "runtime": str(runtime),
        "public_manifest": str(public_library / "manifest.json"),
    }

