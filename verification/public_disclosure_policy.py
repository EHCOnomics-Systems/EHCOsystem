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
_DRIVE_ID_CONTEXT = re.compile(
    r"(?im)^\s*(?:google_)?(?:drive|docs?)(?:_(?:document|folder|file|control))?_id\s*[:=]\s*[A-Za-z0-9_-]{20,}\b"
)
_WINDOWS_HOST = re.compile(r"\bDESKTOP-[A-Za-z0-9-]+\b", re.IGNORECASE)
_WINDOWS_ABSOLUTE_PATH = re.compile(r"(?<![A-Za-z0-9_])[A-Za-z]:\\(?:[^\s<>:\"|?*]+\\?)+")
_POSIX_PRIVATE_PATH = re.compile(
    r"(?<![A-Za-z0-9_])/(?:home/[^/\s]+|Users/[^/\s]+|mnt/[A-Za-z](?:/[^/\s]+)?|workspace)(?:/[^\s)\]}>\"']+)+",
    re.IGNORECASE,
)
_PRIVATE_SOURCE_FIELD = re.compile(
    r"(?im)^\s*(?:private_|owning_)?source_(?:repository|repo|url|branch|revision|commit)\s*[:=]"
)
_PRIVATE_CUSTODY_FIELD = re.compile(
    r"(?im)^\s*(?:private_)?(?:evidence|control|governance)_(?:repository|url|drive_id|drive_url|locator)\s*[:=]"
)
_PRIVATE_ENDPOINT_FIELD = re.compile(
    r"(?im)^\s*(?:private|internal)_(?:service_)?endpoint\s*[:=]"
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

    checks = [
        (_DRIVE_URL, "GOOGLE_DRIVE_ROUTING_URL", "Google Drive/Docs routing URL present"),
        (_DRIVE_ID_CONTEXT, "GOOGLE_DRIVE_ROUTING_ID", "Google Drive/Docs routing identifier present"),
        (_WINDOWS_HOST, "PRIVATE_HOST_LOCATOR", "private workstation/host locator present"),
        (_WINDOWS_ABSOLUTE_PATH, "PRIVATE_HOST_PATH", "absolute Windows host path present"),
        (_POSIX_PRIVATE_PATH, "PRIVATE_POSIX_HOST_PATH", "private host/workspace path present"),
        (_PRIVATE_SOURCE_FIELD, "PRIVATE_SOURCE_TOPOLOGY_FIELD", "private/owning source topology field present"),
        (_PRIVATE_CUSTODY_FIELD, "PRIVATE_CUSTODY_ROUTING_FIELD", "private evidence/control custody routing field present"),
        (_PRIVATE_ENDPOINT_FIELD, "PRIVATE_ENDPOINT_FIELD", "private/internal endpoint field present"),
    ]
    for pattern, rule, detail in checks:
        if pattern.search(text):
            violations.append(DisclosureViolation(rule=rule, source=source, detail=detail))

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

    org_prefix = "EHCOnomics-Systems" + "/"
    drive_origin = "https://" + "docs.google.com" + "/"
    windows_host = "DESKTOP-" + "SYNTHETIC"
    windows_path = "C:" + "\\synthetic\\workspace\\file.txt"
    posix_path = "/" + "home/synthetic/workspace/file.txt"
    source_field = "owning_" + "source_revision: SYNTHETIC_REVISION"
    custody_field = "private_" + "evidence_locator: SYNTHETIC_LOCATOR"
    endpoint_field = "internal_" + "endpoint: https://example.invalid"
    drive_id_field = "drive_" + "document_id: SYNTHETIC_IDENTIFIER_1234567890"

    synthetic_cases: Iterable[tuple[str, str]] = [
        (org_prefix + "PRIVATE_EXAMPLE_REPOSITORY", "NON_PUBLIC_EHCONOMICS_REPOSITORY_LOCATOR"),
        (drive_origin + "document/d/SYNTHETIC_ONLY/edit", "GOOGLE_DRIVE_ROUTING_URL"),
        (drive_id_field, "GOOGLE_DRIVE_ROUTING_ID"),
        (windows_host, "PRIVATE_HOST_LOCATOR"),
        (windows_path, "PRIVATE_HOST_PATH"),
        (posix_path, "PRIVATE_POSIX_HOST_PATH"),
        (source_field, "PRIVATE_SOURCE_TOPOLOGY_FIELD"),
        (custody_field, "PRIVATE_CUSTODY_ROUTING_FIELD"),
        (endpoint_field, "PRIVATE_ENDPOINT_FIELD"),
    ]
    for payload, expected_rule in synthetic_cases:
        rules = {item.rule for item in find_disclosure_violations(payload, "synthetic-blocked")}
        assert expected_rule in rules, f"synthetic disclosure rule did not fire: {expected_rule}"
