#!/usr/bin/env python3
"""Synthetic regression tests for the EHCO pre-publication disclosure gate."""

from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path

from pre_publication_gate import evaluate


def git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return completed.stdout.strip()


def commit_all(root: Path, message: str) -> str:
    git(root, "add", "-A")
    git(root, "commit", "-m", message)
    return git(root, "rev-parse", "HEAD")


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        git(root, "init", "-q")
        git(root, "config", "user.name", "EHCO Synthetic Gate Test")
        git(root, "config", "user.email", "synthetic@example.invalid")

        (root / "public.txt").write_text("public-safe baseline\n", encoding="utf-8")
        base = commit_all(root, "Synthetic safe baseline")

        (root / "public.txt").write_text("public-safe candidate\n", encoding="utf-8")
        clean = commit_all(root, "Synthetic safe candidate")
        receipt_path = root / ".git" / "clearance.json"
        receipt, violations = evaluate(root, base, clean, ["refs/heads/synthetic-clean"], [], receipt_path)
        assert not violations
        assert receipt["candidate_sha"] == clean
        assert json.loads(receipt_path.read_text(encoding="utf-8"))["candidate_sha"] == clean

        private_repo = "EHCOnomics-Systems" + "/" + "PRIVATE_EXAMPLE_REPOSITORY"
        drive_url = "https://" + "docs.google.com" + "/document/d/SYNTHETIC_ONLY/edit"

        git(root, "checkout", "-q", base)
        (root / "transient.txt").write_text(f"repository: {private_repo}\n", encoding="utf-8")
        commit_all(root, "Synthetic transient disclosure")
        (root / "transient.txt").unlink()
        removed = commit_all(root, "Synthetic disclosure removed from final tree")
        _, violations = evaluate(root, base, removed, ["refs/heads/synthetic-history"], [], None)
        assert "NON_PUBLIC_EHCONOMICS_REPOSITORY_LOCATOR" in violations

        git(root, "checkout", "-q", base)
        (root / "safe-again.txt").write_text("safe\n", encoding="utf-8")
        message_candidate = commit_all(root, "Synthetic message " + private_repo)
        _, violations = evaluate(root, base, message_candidate, ["refs/heads/synthetic-message"], [], None)
        assert "NON_PUBLIC_EHCONOMICS_REPOSITORY_LOCATOR" in violations

        git(root, "checkout", "-q", base)
        (root / "metadata-safe.txt").write_text("safe\n", encoding="utf-8")
        metadata_candidate = commit_all(root, "Synthetic metadata candidate")
        metadata = root / "provider-metadata.txt"
        metadata.write_text("PR body: " + drive_url, encoding="utf-8")
        _, violations = evaluate(
            root,
            base,
            metadata_candidate,
            ["refs/heads/synthetic-metadata"],
            [metadata],
            None,
        )
        assert "GOOGLE_DRIVE_ROUTING_URL" in violations

    print("PASS pre-publication disclosure gate synthetic regression suite")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
