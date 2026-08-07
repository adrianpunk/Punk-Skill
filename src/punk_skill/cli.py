from __future__ import annotations

import argparse
import getpass
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

from .compiler import compile_prompt
from .errors import PunkError
from .exporter import export_xingji
from .models import GenerationJob
from .providers.apimart import APIMartConfig, APIMartProvider, save_keychain_key
from .repository import PunkRepository
from .storage import prepare_output, save_result
from .validator import error_count, validate_repository


def _repository(args: argparse.Namespace) -> PunkRepository:
    return PunkRepository(args.root)


def command_validate(args: argparse.Namespace) -> int:
    repository = _repository(args)
    issues = validate_repository(repository)
    errors = error_count(issues)
    warnings = sum(issue.level == "warning" for issue in issues)
    if args.json:
        print(json.dumps({
            "ok": errors == 0,
            "style_count": len(repository.style_ids()),
            "errors": errors,
            "warnings": warnings,
            "issues": [issue.to_mapping() for issue in issues],
        }, ensure_ascii=False, indent=2))
    else:
        for issue in issues:
            print(f"{issue.level.upper()}: {issue.path}: {issue.message}")
        print(f"Validated {len(repository.style_ids())} styles: {errors} errors, {warnings} warnings.")
    return 1 if errors else 0


def command_styles(args: argparse.Namespace) -> int:
    records = _repository(args).styles(args.mode)
    if args.json:
        print(json.dumps([record.meta.to_manifest() for record in records], ensure_ascii=False, indent=2))
    else:
        for record in records:
            print(f"{record.meta.id}\t{record.meta.name}\t{record.meta.mode}\t{record.meta.default_ratio}")
    return 0


def command_manifest(args: argparse.Namespace) -> int:
    repository = _repository(args)
    if args.output:
        path = repository.write_manifest(args.output, args.mode)
        print(path)
    else:
        print(json.dumps(repository.manifest(args.mode), ensure_ascii=False, indent=2))
    return 0


def _read_job(path: Path | None, use_stdin: bool) -> GenerationJob:
    if use_stdin:
        text = sys.stdin.read()
    elif path:
        text = path.read_text(encoding="utf-8")
    else:
        raise PunkError("provide a job file or --stdin")
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        if yaml is None:
            raise PunkError("job input must be JSON because PyYAML is not installed")
        try:
            payload = yaml.safe_load(text)
        except yaml.YAMLError as error:
            raise PunkError(f"job file is not valid YAML or JSON: {error}") from error
    return GenerationJob.from_mapping(payload)


def command_prompt(args: argparse.Namespace) -> int:
    job = _read_job(args.job, args.stdin)
    result = compile_prompt(_repository(args), job)
    output = args.output
    if not output and job.output_dir:
        output = Path(job.output_dir) / "prompts" / f"{job.mode}.md"
    if output:
        output = output.expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(result.prompt, encoding="utf-8")
    if args.json:
        payload = result.to_mapping()
        if output:
            payload["prompt_path"] = str(output)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    elif output:
        print(output)
    else:
        print(result.prompt, end="")
    return 0


def command_generate(args: argparse.Namespace) -> int:
    job = _read_job(args.job, args.stdin)
    result = compile_prompt(_repository(args), job)
    output_dir = args.output_dir or (Path(job.output_dir) if job.output_dir else None)
    if not output_dir:
        raise PunkError("generate requires --output-dir or output_dir in the job")
    root, prompt_path = prepare_output(result, output_dir)
    if job.provider != "apimart":
        raise PunkError(f"unsupported provider: {job.provider}")
    provider = APIMartProvider(APIMartConfig.from_environment())
    image = provider.generate(
        prompt=result.prompt,
        ratio=result.job.ratio,
        output_stem=root / result.job.mode,
        source_image=result.job.source_image,
    )
    result_path = save_result(root, image)
    payload = {
        "status": "generated",
        "prompt_path": str(prompt_path),
        "result_path": str(result_path),
        **image.to_mapping(),
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(image.saved_path)
    return 0


def command_config_set_key(args: argparse.Namespace) -> int:
    value = getpass.getpass("APIMart API key: ")
    save_keychain_key(value)
    print("APIMart API key saved in macOS Keychain.")
    return 0


def command_export_xingji(args: argparse.Namespace) -> int:
    payload = export_xingji(_repository(args), args.target)
    print(json.dumps(payload, ensure_ascii=False, indent=2) if args.json else payload["runtime"])
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="punk", description="Local runtime for Punk visual styles")
    parser.add_argument("--root", type=Path, help="Punk-Skill repository root")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="validate style metadata and files")
    validate.add_argument("--json", action="store_true")
    validate.set_defaults(handler=command_validate)

    styles = subparsers.add_parser("styles", help="list available styles")
    styles.add_argument("--mode", choices=("cover", "avatar"))
    styles.add_argument("--json", action="store_true")
    styles.set_defaults(handler=command_styles)

    manifest = subparsers.add_parser("manifest", help="build a machine-readable style manifest")
    manifest.add_argument("--mode", choices=("cover", "avatar"))
    manifest.add_argument("--output", type=Path)
    manifest.set_defaults(handler=command_manifest)

    prompt = subparsers.add_parser("prompt", help="compile one structured job into an image prompt")
    prompt.add_argument("job", nargs="?", type=Path)
    prompt.add_argument("--stdin", action="store_true", help="read YAML or JSON job data from stdin")
    prompt.add_argument("--output", type=Path)
    prompt.add_argument("--json", action="store_true")
    prompt.set_defaults(handler=command_prompt)

    generate = subparsers.add_parser("generate", help="compile a job and generate one image")
    generate.add_argument("job", nargs="?", type=Path)
    generate.add_argument("--stdin", action="store_true", help="read YAML or JSON job data from stdin")
    generate.add_argument("--output-dir", type=Path)
    generate.add_argument("--json", action="store_true")
    generate.set_defaults(handler=command_generate)

    config = subparsers.add_parser("config", help="manage local provider configuration")
    config_subparsers = config.add_subparsers(dest="config_command", required=True)
    set_key = config_subparsers.add_parser("set-key", help="save the APIMart API key in macOS Keychain")
    set_key.set_defaults(handler=command_config_set_key)

    export = subparsers.add_parser("export-xingji", help="export the Python runtime and style library to Xingji Liubai")
    export.add_argument("target", type=Path, help="Xingji Liubai project root")
    export.add_argument("--json", action="store_true")
    export.set_defaults(handler=command_export_xingji)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.handler(args))
    except PunkError as error:
        print(f"punk: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
