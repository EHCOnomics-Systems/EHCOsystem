#!/usr/bin/env python3
"""Install the repository-owned EHCO pre-push publication guard in this clone."""

from __future__ import annotations

import stat
import subprocess
import sys
from pathlib import Path


def run(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return completed.stdout.strip()


def main() -> int:
    try:
        root = Path(run(Path.cwd(), "rev-parse", "--show-toplevel"))
    except subprocess.CalledProcessError:
        print("FAIL publication guard installation: not inside a Git repository", file=sys.stderr)
        return 2

    hook = root / ".githooks" / "pre-push"
    if not hook.is_file():
        print("FAIL publication guard installation: tracked pre-push hook is missing", file=sys.stderr)
        return 2

    try:
        hook.chmod(hook.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        run(root, "config", "--local", "core.hooksPath", ".githooks")
        configured = run(root, "config", "--local", "--get", "core.hooksPath")
    except (OSError, subprocess.CalledProcessError):
        print("FAIL publication guard installation: Git hook configuration failed", file=sys.stderr)
        return 2

    if configured != ".githooks":
        print("FAIL publication guard installation: hook path readback mismatch", file=sys.stderr)
        return 2

    print("PASS EHCO publication guard installed for this clone")
    print("core.hooksPath=.githooks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
