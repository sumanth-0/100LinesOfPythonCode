"""
Scan a project for file or directory names that collide on a
case-insensitive filesystem (e.g., Windows, macOS with default settings).

This helps contributors avoid clone errors by highlighting locations where
multiple entries differ only by letter casing.
"""

from __future__ import annotations

import argparse
import os
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


Collision = Tuple[Path, Sequence[Sequence[str]]]


def list_entries(
    names: Iterable[str],
    include_hidden: bool,
) -> List[str]:
    """Return names filtered according to the hidden flag."""
    if include_hidden:
        return list(names)
    return [name for name in names if not name.startswith(".")]


def collect_collisions(root: Path, include_hidden: bool) -> List[Collision]:
    """Walk the tree under root and gather case-insensitive collisions."""
    collisions: List[Collision] = []

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = list_entries(dirnames, include_hidden)
        visible_files = list_entries(filenames, include_hidden)

        grouped: Dict[str, List[str]] = defaultdict(list)
        for name in (*dirnames, *visible_files):
            grouped[name.casefold()].append(name)

        duplicates = [tuple(sorted(names, key=str.casefold)) for names in grouped.values() if len(names) > 1]
        if duplicates:
            current = Path(dirpath)
            relative = current.relative_to(root)
            collisions.append((relative, duplicates))

    return collisions


def format_report(collisions: Sequence[Collision], root: Path) -> str:
    """Turn the collisions list into a printable report."""
    lines: List[str] = []
    for relative, variants in collisions:
        location = "." if relative == Path(".") else str(relative)
        lines.append(f"[{location}]")
        for names in variants:
            variants_str = ", ".join(names)
            lines.append(f"  - {variants_str}")
    if not lines:
        return f"No case-insensitive conflicts found under {root}"
    header = f"Conflicts found under {root} (case-insensitive check):"
    return "\n".join([header, *lines])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Detect filename collisions that break on case-insensitive filesystems.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Project directory to scan (defaults to current working directory).",
    )
    parser.add_argument(
        "--include-hidden",
        action="store_true",
        help="Also report entries that start with a dot.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(args.path).resolve()

    if not root.exists():
        raise SystemExit(f"Path does not exist: {root}")
    if not root.is_dir():
        raise SystemExit(f"Path is not a directory: {root}")

    collisions = collect_collisions(root, args.include_hidden)
    print(format_report(collisions, root))


if __name__ == "__main__":
    main()
