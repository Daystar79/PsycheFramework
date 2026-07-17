#!/usr/bin/env python3
"""
Migration: replace framework files with optimized siblings (if present).

Cross-platform. Prefer launching via:
  python scripts/run.py migrate
  scripts/unix/migrate.sh          (Unix)
  scripts/windows/migrate.ps1      (Windows)

Run from the repo root (or any cwd — paths resolve from this file).
"""

from __future__ import annotations

import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent

CORE_REPLACEMENTS = [
    (ROOT / "Framework" / "Main_optimized.md", ROOT / "Framework" / "Main.md"),
    (ROOT / "Framework" / "Rules_Index_optimized.md", ROOT / "Framework" / "Rules_Index.md"),
    (
        ROOT / "Framework" / "Psychology" / "realm_data_optimized.yaml",
        ROOT / "Framework" / "Psychology" / "realm_data.yaml",
    ),
    (
        ROOT / "Simulator" / "CharacterRuntime_optimized.md",
        ROOT / "Simulator" / "CharacterRuntime.md",
    ),
]

DEMO_CHARS = ("cass", "helen", "lior", "nora", "reed", "wren")


def word_count(path: Path) -> int:
    if not path.is_file():
        return 0
    return len(path.read_text(encoding="utf-8").split())


def main() -> int:
    print("=== Cognitive Middleware Optimization Migration ===\n")

    missing = [src for src, _ in CORE_REPLACEMENTS if not src.is_file()]
    char_missing = [
        ROOT / "Characters" / f"{name}_optimized.md"
        for name in DEMO_CHARS
        if not (ROOT / "Characters" / f"{name}_optimized.md").is_file()
    ]
    if missing and char_missing:
        print("[!] No optimized source files found.")
        print("    This migration is only needed when *_optimized.* siblings exist.")
        print("    Current tree already uses the optimized framework layout.")
        return 0

    backup_dir = ROOT / f"backups_{date.today().strftime('%Y%m%d')}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    print(f"Creating backups in {backup_dir.name}/ ...")

    for _, dst in CORE_REPLACEMENTS:
        if dst.is_file():
            shutil.copy2(dst, backup_dir / f"{dst.stem}_original{dst.suffix}")
    for path in (ROOT / "Characters").glob("*.md"):
        shutil.copy2(path, backup_dir / path.name)

    print("Replacing core framework files...")
    for src, dst in CORE_REPLACEMENTS:
        if not src.is_file():
            print(f"    [skip] missing {src.relative_to(ROOT)}")
            continue
        shutil.copy2(src, dst)
        src.unlink()
        print(f"    {dst.relative_to(ROOT)}")

    print("Replacing character cards...")
    for name in DEMO_CHARS:
        src = ROOT / "Characters" / f"{name}_optimized.md"
        dst = ROOT / "Characters" / f"{name}.md"
        if not src.is_file():
            print(f"    [skip] missing {src.name}")
            continue
        shutil.copy2(src, dst)
        src.unlink()
        print(f"    {dst.name}")

    print("\n=== Migration Complete ===\n")
    print("Word count verification (core):")
    for rel in (
        "Framework/Main.md",
        "Framework/Rules_Index.md",
        "Framework/Psychology/realm_data.yaml",
    ):
        p = ROOT / rel
        print(f"  {rel}: {word_count(p)} words")

    print("\nOptimization summary: OPTIMIZATION_SUMMARY.md")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nCancelled.", file=sys.stderr)
        raise SystemExit(130)
