#!/usr/bin/env python3
"""
Sync lightweight FigureYa source code into this skill.

Copies only R Markdown and R source files from FigureYa tool directories:
  - .Rmd / .rmd report source
  - .R / .r helper scripts and install_dependencies.R

It intentionally excludes HTML reports, images, data tables, and package caches.
"""
import argparse
import json
import shutil
from pathlib import Path

CODE_SUFFIXES = {'.rmd', '.r'}


def load_tool_ids(skill_dir):
    catalog_path = skill_dir / 'references' / 'figureya_catalog.json'
    with catalog_path.open('r', encoding='utf-8') as handle:
        catalog = json.load(handle)
    return [entry['id'] for entry in catalog]


def iter_code_files(tool_dir):
    for path in sorted(tool_dir.rglob('*')):
        if path.is_file() and path.suffix.lower() in CODE_SUFFIXES:
            yield path


def sync_reference_code(source_root, skill_dir, overwrite=False, dry_run=False):
    code_root = skill_dir / 'references' / 'code'
    copied = 0
    skipped_existing = 0
    missing_tools = []

    for tool_id in load_tool_ids(skill_dir):
        source_dir = source_root / tool_id
        if not source_dir.is_dir():
            missing_tools.append(tool_id)
            continue

        target_dir = code_root / tool_id
        if not dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)

        for source_file in iter_code_files(source_dir):
            rel_path = source_file.relative_to(source_dir)
            target_file = target_dir / rel_path

            if target_file.exists() and not overwrite:
                skipped_existing += 1
                continue

            copied += 1
            if not dry_run:
                target_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_file, target_file)

    return {
        'copied': copied,
        'skipped_existing': skipped_existing,
        'missing_tools': missing_tools,
    }


def main():
    parser = argparse.ArgumentParser(description='Sync FigureYa Rmd/R source files into the skill references/code directory.')
    parser.add_argument('source_root', type=Path, help='FigureYa repository root, e.g. E:/Projects/FigureYa-main')
    parser.add_argument('--skill-dir', type=Path, default=Path(__file__).resolve().parents[1], help='r-plot-gallery skill directory')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing copied source files')
    parser.add_argument('--dry-run', action='store_true', help='Report what would be copied without writing files')
    args = parser.parse_args()

    result = sync_reference_code(args.source_root, args.skill_dir, overwrite=args.overwrite, dry_run=args.dry_run)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
