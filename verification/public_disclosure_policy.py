#!/usr/bin/env python3
"""Public-safe disclosure policy for EHCOsystem verification.

This module intentionally contains no real private repository names, private
source revisions, Drive document identifiers, or protected host locators.
It detects prohibited topology structurally and validates itself with synthetic
fixtures only.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable

PUBLIC_REPOSITORY = "EHCOnomics-Systems/EHCOsystem"

_ORG_REPOSITORY = re.compile(r"\bEHCOnomics-Systems/([A-Za-z0-9_.-]+)\b", re.IGNORECASE)
_DRIVE_URL = re.compile(r"https?://(?:(?:drive|docs)\.google\.com)/[^\s)\]}>\"']+", re.IGNORECASE)
_WINDOWS_HOST = re.compile(r"\bDESKTOP-[A-Za-z0-9-]+\b", re.IGNORECASE)
_WINDOWS_ABSOLUTE_PATH = re.compile(r"(?<![A-Za-z0-9_])[A-Za-z]:\\(?:[^\s<>:\"|?*]+\\?)+")
_PRIVATE_SOURCE_FIELD = re.compile(
    r"(?im)^\s*(?:private_|owning_)?source_(?:repository|repo|url|branch|revision|commit)\s*[:=]"
)
_PRIVATE_CUSTODY_FIELD = re.compile(
    r"(?im)^\s*(?:private_)?(?:evidence|control|governance)_(?:repository|url|drive_id|drive_url|locator)\s*[:=]"
)


@dataclass(frozen=True)
class DisclosureViolation:
    rule: str
    source: str
    detail: str


def find_disclosure_violations(text: str, source: str = "<memory>") -> list[DisclosureViolation]:
    """Return structural prohibited-topology findings without echoing matched values."""
    violations: list[DisclosureViolation] = []

    for match in _ORG_REPOSITORY.finditer(text):
        full_name = match.group(0)
        if full_name.casefold() != PUBLIC_REPOSITORY.casefold():
            violations.append(
                DisclosureViolation(
                    rule="NON_PUBLIC_EHCONOMICS_REPOSITORY_LOCATOR",
                    source=source,
                    detail="non-public EHCOnomics repository locator present",
                )
            )

    if _DRIVE_URL.search(text):
        violations.append(
            DisclosureViolation(
                rule="GOOGLE_DRIVE_ROUTING_URL",
                source=source,
                detail="Google Drive/Docs routing URL present",
            )
        )

    if _WINDOWS_HOST.search(text):
        violations.append(
            DisclosureViolation(
                rule="PRIVATE_HOST_LOCATOR",
                source=source,
                detail="private workstation/host locator present",
            )
        )

    if _WINDOWS_ABSOLUTE_PATH.search(text):
        violations.append(
            DisclosureViolation(
                rule="PRIVATE_HOST_PATH",
                source=source,
                detail="absolute Windows host path present",
            )
        )

    if _PRIVATE_SOURCE_FIELD.search(text):
        violations.append(
            DisclosureViolation(
                rule="PRIVATE_SOURCE_TOPOLOGY_FIELD",
                source=source,
                detail="private/owning source topology field present",
            )
        )

    if _PRIVATE_CUSTODY_FIELD.search(text):
        violations.append(
            DisclosureViolation(
                rule="PRIVATE_CUSTODY_ROUTING_FIELD",
                source=source,
                detail="private evidence/control custody routing field present",
            )
        )

    return violations


def assert_public_safe(text: str, source: str = "<memory>") -> None:
    violations = find_disclosure_violations(text, source)
    if violations:
        summary = "; ".join(f"{item.rule} in {item.source}" for item in violations)
        raise AssertionError(summary)


def run_synthetic_policy_self_test() -> None:
    """Prove the policy using synthetic values that disclose no real private topology."""
    safe = f"repository: {PUBLIC_REPOSITORY}\npublic evidence only"
    assert not find_disclosure_violations(safe, "synthetic-safe")

    synthetic_cases: Iterable[tuple[str, str]] = [
        ("repository: EHCOnomics-Systems/PRIVATE_EXAMPLE_REPOSITORY", "NON_PUBLIC_EHCONOMICS_REPOSITORY_LOCATOR"),
        ("reference: https://docs.google.com/document/d/SYNTHETIC_ONLY/edit", "GOOGLE_DRIVE_ROUTING_URL"),
        ("host: DESKTOP-SYNTHETIC", "PRIVATE_HOST_LOCATOR"),
        (r"path: C:\synthetic\workspace\file.txt", "PRIVATE_HOST_PATH"),
        ("owning_source_revision: SYNTHETIC_REVISION", "PRIVATE_SOURCE_TOPOLOGY_FIELD"),
        ("private_evidence_locator: SYNTHETIC_LOCATOR", "PRIVATE_CUSTODY_ROUTING_FIELD"),
    ]
    for payload, expected_rule in synthetic_cases:
        rules = {item.rule for item in find_disclosure_violations(payload, "synthetic-blocked")}
        assert expected_rule in rules, f"synthetic disclosure rule did not fire: {expected_rule}"
