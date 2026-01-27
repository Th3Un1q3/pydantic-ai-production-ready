#!/usr/bin/env python3
"""Init and validate learning materials directory structure.

Usage examples:
  python scripts/init_learning_structure.py --path ./learning --init-all
  python scripts/init_learning_structure.py --path ./learning --add-module 05-ml-deployment --title "ML Deployment"
  python scripts/init_learning_structure.py --path ./learning --validate
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path
from typing import List, Optional

DEFAULT_MODULES = [
    ("01-fundamentals", "Fundamentals"),
    ("02-core-concepts", "Core Concepts"),
    ("03-advanced-patterns", "Advanced Patterns"),
    ("04-production-deployment", "Production & Deployment"),
]

TEMPLATE_README = """# {title}

**Learning objectives**

- TODO: list learning objectives

## Overview

A short description of the module.

## Exercises

See the `exercises/` directory for hands-on tasks.
"""


def create_module(root: Path, name: str, title: Optional[str] = None, dry_run: bool = False) -> Path:
    """Create a module skeleton under root with given name and optional title."""
    mod_path = root / name
    readme_path = mod_path / "README.md"
    exercises_path = mod_path / "exercises"
    resources_path = mod_path / "resources"

    if dry_run:
        print(f"[dry-run] Would create: {mod_path}")
        return mod_path

    mod_path.mkdir(parents=True, exist_ok=True)
    exercises_path.mkdir(parents=True, exist_ok=True)
    resources_path.mkdir(parents=True, exist_ok=True)

    if not readme_path.exists():
        title_text = title or name.replace('-', ' ').strip()
        readme_path.write_text(TEMPLATE_README.format(title=title_text), encoding="utf8")
        print(f"Created README: {readme_path}")
    else:
        print(f"README exists: {readme_path}")

    # Ensure exercises README exists
    ex_readme = exercises_path / "README.md"
    if not ex_readme.exists():
        ex_readme.write_text("# Exercises\n\nAdd exercises for this module.", encoding="utf8")
        print(f"Created exercises README: {ex_readme}")
    else:
        print(f"Exercises README exists: {ex_readme}")

    return mod_path


def validate_structure(root: Path) -> bool:
    """Validate root has expected top-level modules and that each module has README and exercises/ directory."""
    ok = True
    if not root.exists():
        print(f"Path does not exist: {root}")
        return False

    for child in sorted(root.iterdir()):
        if child.is_dir():
            readme = child / "README.md"
            exercises = child / "exercises"
            if not readme.exists():
                print(f"Missing README in module: {child}")
                ok = False
            if not exercises.exists() or not exercises.is_dir():
                print(f"Missing exercises/ in module: {child}")
                ok = False
    if ok:
        print("Validation passed: structure looks good.")
    else:
        print("Validation failed: see messages above.")
    return ok


def init_all(root: Path, dry_run: bool = False) -> None:
    for name, title in DEFAULT_MODULES:
        create_module(root, name, title, dry_run=dry_run)


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Init and validate learning materials structure")
    p.add_argument("--path", "-p", default="./learning", help="Root learning path")
    p.add_argument("--init-all", action="store_true", help="Create the default set of modules")
    p.add_argument("--add-module", help="Add a module folder (name, e.g., 05-ml-deployment)")
    p.add_argument("--title", help="Optional title to put into module README")
    p.add_argument("--validate", action="store_true", help="Validate existing structure")
    p.add_argument("--dry-run", action="store_true", help="Show actions without writing files")
    return p.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    root = Path(args.path)

    if args.init_all:
        init_all(root, dry_run=args.dry_run)
        return 0

    if args.add_module:
        create_module(root, args.add_module, title=args.title, dry_run=args.dry_run)
        return 0

    if args.validate:
        ok = validate_structure(root)
        return 0 if ok else 2

    print("Nothing to do. Use --help to see options.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
