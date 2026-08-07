from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .errors import PunkError
from .repository import PunkRepository
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

