#!/usr/bin/env python3
"""CLI and functions to list files in a directory sorted by size."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Iterable, List, Tuple


def sizeof_fmt(num: int) -> str:
    # human friendly format
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if num < 1024.0:
            return f"{num:.0f} {unit}" if unit == 'B' else f"{num:.1f} {unit}"
        num /= 1024.0
    return f"{num:.1f} PB"


def iter_files(directory: Path, recursive: bool = False) -> Iterable[Path]:
    directory = Path(directory)
    if recursive:
        for root, dirs, files in os.walk(directory):
            for name in files:
                yield Path(root) / name
    else:
        for entry in directory.iterdir():
            if entry.is_file():
                yield entry


def sort_files_by_size(directory: Path | str = '.', recursive: bool = False, reverse: bool = False, limit: int | None = None) -> List[Tuple[Path, int]]:
    """Return a list of (Path, size) sorted by size.

    - directory: directory to scan
    - recursive: include files from subdirectories
    - reverse: True == largest first
    - limit: maximum number of results (None == all)
    """
    files_with_size: List[Tuple[Path, int]] = []
    for p in iter_files(Path(directory), recursive=recursive):
        try:
            size = p.stat().st_size
        except OSError:
            # skip files we cannot stat
            continue
        files_with_size.append((p, size))

    files_with_size.sort(key=lambda t: t[1], reverse=reverse)
    if limit is not None and limit >= 0:
        return files_with_size[:limit]
    return files_with_size


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="List files in a directory sorted by file size")
    parser.add_argument('directory', nargs='?', default='.', help='Directory to scan (default: current dir)')
    parser.add_argument('-r', '--recursive', action='store_true', help='Scan recursively')
    parser.add_argument('-n', '--limit', type=int, default=None, help='Limit number of results')
    parser.add_argument('-l', '--largest', action='store_true', help='Show largest first (default smallest first)')
    parser.add_argument('-H', '--human', action='store_true', help='Show human-readable sizes')
    args = parser.parse_args(argv)

    results = sort_files_by_size(args.directory, recursive=args.recursive, reverse=args.largest, limit=args.limit)
    for p, s in results:
        size_str = sizeof_fmt(s) if args.human else str(s)
        print(f"{size_str}\t{p}")

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
