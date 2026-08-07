from __future__ import annotations

import json
from pathlib import Path

import yaml

from .compiler import CompileResult
from .providers.apimart import GeneratedImage


def prepare_output(result: CompileResult, output_dir: str | Path) -> tuple[Path, Path]:
    root = Path(output_dir).expanduser().resolve()
    prompt_path = root / "prompts" / f"{result.job.mode}.md"
    prompt_path.parent.mkdir(parents=True, exist_ok=True)
    prompt_path.write_text(result.prompt, encoding="utf-8")
    job_path = root / "job.yaml"
    job_path.write_text(
        yaml.safe_dump(result.job.to_mapping(), allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    manifest = {
        "schema_version": 1,
        "mode": result.job.mode,
        "style": result.style.to_manifest(),
        "prompt_path": str(prompt_path),
        "status": "prompt_ready",
    }
    (root / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return root, prompt_path


def save_result(output_dir: Path, image: GeneratedImage) -> Path:
    path = output_dir / "result.json"
    path.write_text(json.dumps(image.to_mapping(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest_path = output_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.update({"status": "generated", "image_path": str(image.saved_path)})
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path

