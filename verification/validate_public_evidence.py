#!/usr/bin/env python3
"""Validate EHCOsystem public repository integrity, presentation boundaries, and durable semantics."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_ROOT = ROOT / "evidence" / "public-evidence-companion" / "v1"
DOSSIER_NAME = "EHCO_AI_OS_Governed_Operational_Architecture_Public_Edition_v1_8_LOCK_FINAL.pdf"
DOSSIER_SHA256 = "F489BA01961A12CF101B1F1DF57E6958456A0840BEB798B862FA97ACB030892D"
EXPECTED_PACKETS = [
    "00_DOSSIER_IDENTITY_AND_BOUNDARY",
    "01_INSTANTIATED_STANDING",
    "02_CANONICAL_RUNTIME_SOURCE_BINDING",
    "03_TIER1_AUTHORITY_ENFORCEMENT",
    "04_RUNTIME_PACKET_AND_CONTINUITY_ANCHORS",
    "05_PROOF_COLLAPSE_RECOVERY_AND_RELEASE_ANCHORS",
    "06_OBSERVED_LIVE_CAPTURE_AND_RELEASE_STATUS",
    "07_PUBLIC_BOUNDARIES_AND_DELIVERY_STATUS",
    "08_SUITE_VERIFICATION_AND_FINAL_ZIP",
]
ACTIVE_PUBLIC_TEXT = [
    "README.md",
    "NOTICE.md",
    "LIBRARY.md",
    "getting-started/START-HERE.md",
    "getting-started/reading-order.md",
    "architecture/INSTANTIATED-AI.md",
    "architecture/EHCO-TECHNOLOGY-ESTATE.md",
    "architecture/ecosystem-components-and-participation.md",
    "architecture/diagrams/README.md",
    "architecture/EHCO-AI-OS-SYSTEM-CARD.md",
    "architecture/EHCO-AI-OS-INSTANTIATED-SYSTEM.md",
    "architecture/GOVERNED-RUNTIME-ARCHITECTURE.md",
    "architecture/SYSTEM-INVARIANTS.md",
    "architecture/instantiated-proof-range.md",
    "architecture/proof-and-status-classes.md",
    "architecture/runtime-repository-and-test-estate-boundary.md",
    "language-model/README.md",
    "language-model/DETERMINISTIC-CAPABILITY-DEMONSTRATION.md",
    "language-model/evidence/public-test-snapshot-v1/README.md",
    "range-reactor/README.md",
    "range-reactor/evidence/operational-closure-v1/README.md",
    "runtime/README.md",
    "evidence/README.md",
    "evidence/runtime/full-flex/v1/README.md",
    "ECOSYSTEM-DILIGENCE.md",
    "TECHNICAL-DILIGENCE.md",
    "assurance/CLAIM-EVIDENCE-MATRIX.md",
    "assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md",
    "verification/README.md",
    "releases/PUBLIC-RELEASE-REGISTER.md",
    "PROVENANCE.md",
    "GOVERNANCE.md",
]
DASHBOARD_ASSETS = [
    "architecture/assets/dashboard/overview-june-2026-public.webp",
    "architecture/assets/dashboard/services-coordination-june-2026-public.webp",
    "architecture/assets/dashboard/authority-boundary-june-2026-public.webp",
    "architecture/assets/dashboard/receipts-evidence-june-2026-public.webp",
    "architecture/assets/dashboard/health-registry-june-2026-public.webp",
    "architecture/assets/dashboard/replacement-readiness-june-2026-public.webp",
    "architecture/assets/dashboard/prime-relationship-june-2026-public.webp",
    "architecture/assets/dashboard/agent-connect-coordination-june-2026-public.webp",
]
ERRORS: list[str] = []
CHECKS = 0


def checked(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        ERRORS.append(message)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def read_text(relative: str) -> str:
    path = ROOT / relative
    checked(path.is_file(), f"Required public file missing: {relative}")
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8-sig")


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        ERRORS.append(f"JSON parse failure: {path.relative_to(ROOT)}: {exc}")
        return {}
    checked(isinstance(value, dict), f"JSON object expected: {path.relative_to(ROOT)}")
    return value if isinstance(value, dict) else {}


def validate_repository_residue() -> None:
    for forbidden in [
        ROOT / "UPLOAD_INSTRUCTIONS_DO_NOT_COMMIT.txt",
        ROOT / "PACKAGE_SHA256SUMS_DO_NOT_COMMIT.txt",
        ROOT / ".import-staging",
        ROOT / "dossiers" / "public-technical-packaging" / "SCOPE-OF-WORK.md",
    ]:
        checked(not forbidden.exists(), f"Closeout residue present: {forbidden.relative_to(ROOT)}")
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        checked(path.suffix.lower() != ".zip", f"ZIP archive present in source tree: {path.relative_to(ROOT)}")
        checked(re.fullmatch(r"part-\d+", path.name) is None, f"Transfer chunk present: {path.relative_to(ROOT)}")


def validate_dossier_and_historical_packets() -> None:
    dossier_paths = [
        ROOT / "dossiers" / DOSSIER_NAME,
        EVIDENCE_ROOT / "00_DOSSIER_IDENTITY_AND_BOUNDARY" / "source_document" / DOSSIER_NAME,
    ]
    for path in dossier_paths:
        checked(path.is_file(), f"Canonical dossier missing: {path.relative_to(ROOT)}")
        if path.is_file():
            checked(sha256_file(path) == DOSSIER_SHA256, f"Dossier SHA-256 mismatch: {path.relative_to(ROOT)}")

    checked(EVIDENCE_ROOT.is_dir(), "Historical Public Evidence Companion directory missing")
    actual = sorted(p.name for p in EVIDENCE_ROOT.iterdir() if p.is_dir()) if EVIDENCE_ROOT.is_dir() else []
    checked(actual == EXPECTED_PACKETS, f"Historical packet directory set mismatch: {actual}")

    manifest_hashes: dict[str, str] = {}
    for packet_name in EXPECTED_PACKETS:
        packet = EVIDENCE_ROOT / packet_name
        manifest_path = packet / "CONTENT_MANIFEST.json"
        detached_path = packet / "CONTENT_MANIFEST.sha256"
        verification_path = packet / "VERIFICATION_RESULT.json"
        checked(manifest_path.is_file(), f"Manifest missing: {packet_name}")
        checked(detached_path.is_file(), f"Detached manifest hash missing: {packet_name}")
        checked(verification_path.is_file(), f"Verification result missing: {packet_name}")
        if not manifest_path.is_file():
            continue
        manifest = load_json(manifest_path)
        entries = manifest.get("files", [])
        checked(isinstance(entries, list), f"Manifest files invalid: {packet_name}")
        if not isinstance(entries, list):
            continue
        checked(manifest.get("file_count") == len(entries), f"Manifest file_count mismatch: {packet_name}")
        seen: set[str] = set()
        for entry in entries:
            if not isinstance(entry, dict):
                ERRORS.append(f"Manifest entry invalid: {packet_name}")
                continue
            value = entry.get("path")
            pure = PurePosixPath(value) if isinstance(value, str) else None
            valid = bool(value) and pure is not None and not pure.is_absolute() and ".." not in pure.parts and "\\" not in value
            checked(valid, f"Manifest path invalid: {packet_name}: {value!r}")
            if not valid:
                continue
            checked(value not in seen, f"Duplicate manifest path: {packet_name}: {value}")
            seen.add(value)
            target = packet.joinpath(*pure.parts)
            checked(target.is_file(), f"Manifest target missing: {target.relative_to(ROOT)}")
            if target.is_file():
                checked(target.stat().st_size == entry.get("bytes"), f"Byte count mismatch: {target.relative_to(ROOT)}")
                checked(sha256_file(target) == str(entry.get("sha256", "")).upper(), f"SHA-256 mismatch: {target.relative_to(ROOT)}")
        digest = sha256_file(manifest_path)
        manifest_hashes[packet_name] = digest
        if detached_path.is_file():
            checked(detached_path.read_text(encoding="utf-8-sig").strip().split()[0].upper() == digest, f"Detached manifest hash mismatch: {packet_name}")
        if verification_path.is_file():
            checked(load_json(verification_path).get("status") == "PASS", f"Historical packet verification status mismatch: {packet_name}")

    suite = load_json(EVIDENCE_ROOT / EXPECTED_PACKETS[8] / "SUITE_MANIFEST.json")
    checked(suite.get("prior_packet_count") == 8, "Suite prior_packet_count mismatch")
    checked(suite.get("total_packet_count") == 9, "Suite total_packet_count mismatch")
    packets = suite.get("packets", [])
    checked(isinstance(packets, list) and len(packets) == 8, "Suite packet enumeration mismatch")
    if isinstance(packets, list):
        for index, entry in enumerate(packets):
            if not isinstance(entry, dict):
                continue
            expected = EXPECTED_PACKETS[index]
            checked(entry.get("directory") == expected, f"Suite directory mismatch: {expected}")
            checked(str(entry.get("manifest_sha256", "")).upper() == manifest_hashes.get(expected), f"Suite manifest hash mismatch: {expected}")
            checked(entry.get("verification_status") == "PASS", f"Suite verification status mismatch: {expected}")


def validate_markdown_links() -> None:
    link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8-sig")
        for raw in link_re.findall(text):
            target = raw.strip().split()[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            checked((path.parent / target).resolve().exists(), f"Broken Markdown link in {path.relative_to(ROOT)}: {raw}")


def validate_dashboard_assets() -> None:
    for relative in DASHBOARD_ASSETS:
        checked((ROOT / relative).is_file(), f"Dashboard public asset missing: {relative}")
    readme = read_text("README.md")
    checked("architecture/assets/dashboard/overview-june-2026-public.webp" in readme, "README Dashboard overview missing")
    checked("architecture/assets/dashboard/services-coordination-june-2026-public.webp" in readme, "README Dashboard services view missing")


def validate_public_presentation() -> None:
    texts = {relative: read_text(relative) for relative in ACTIVE_PUBLIC_TEXT}
    combined = "\n".join(texts.values())
    lower_combined = combined.lower()

    required = {
        "README.md": ["Instantiated AI", "EHCO AI-OS", "INSTANTIATED_EHCO_RUNTIME", "EHCO Language Model", "EHCO Range Reactor", "verification/verify_all_public.py"],
        "language-model/README.md": ["mature deterministic computational-language system", "governed staging execution and verification", "DETERMINISTIC-CAPABILITY-DEMONSTRATION.md"],
        "language-model/DETERMINISTIC-CAPABILITY-DEMONSTRATION.md": ["RETAIN_AMBIGUITY", "WITHHOLD", "Language Math", "round-trip", "service equivalence"],
        "range-reactor/README.md": ["14.304307x", "14.208722x", "94.755854%", "82 passed / 0 failed"],
        "runtime/README.md": ["EHCO AI-OS Runtime — Accepted Public Evidence", "REALIZED / COMPLETE_IN_ACCEPTED_SCOPE", "52/53", "PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION", "public-safe Full Flex record"],
        "evidence/runtime/full-flex/v1/README.md": ["Accepted Runtime Evidence Index", "PUBLIC_SAFE_RECORD.json", "7F80C27D085AE871A00AED412C6F20EA9A76CB0677C93AEBA381CD1FD70EC8E5"],
        "verification/README.md": ["verification/verify_all_public.py", "Range Reactor operational-closure", "durable public semantics"],
    }
    for relative, phrases in required.items():
        for phrase in phrases:
            checked(phrase in texts[relative], f"Required public representation missing in {relative}: {phrase}")

    forbidden_semantics = [
        ("advanced near-final", "Obsolete advanced-near-final wording remains in active public surfaces"),
        ("staging verification frontier", "Stale Language Model staging-frontier wording remains in active public surfaces"),
        ("current selected lifecycle frontier", "Volatile lifecycle-frontier wording remains in active public surfaces"),
        ("current public evidence projection and synthesis", "Residual Full Flex synthesis wording remains in active public surfaces"),
        ("current public capability-and-evidence synthesis", "Residual Full Flex capability-synthesis wording remains in active public surfaces"),
        ("public synthesis role", "Residual Full Flex synthesis-role wording remains in active public surfaces"),
        ("ehco ai-os owns the governing runtime relationships", "EHCO AI-OS authority-owner collapse remains in active public surfaces"),
        ("ehco ai-os owns:\n\n- admission and standing", "EHCO AI-OS authority-owner list remains in active public surfaces"),
        ("governing relationships owned by ehco ai-os", "System invariants still assign Runtime authority relationships to EHCO AI-OS"),
        ("exact packet-byte insertion awaits lawful byte custody", "Stale Full Flex exact-byte custody wording remains"),
        ("scoped runtime participation relationship are independently tracked", "Language Model Runtime participation remains implied without owning evidence"),
        ("ehco ai-os runtime — current public evidence", "Volatile Runtime front-door label remains in active public surfaces"),
    ]
    for phrase, message in forbidden_semantics:
        checked(phrase not in lower_combined, message)

    private_tokens = [
        "EHCOnomics-Systems/EHCO_AI-OS",
        "EHCOnomics-Systems/EHCO_Range_Reactor",
        "EHCOnomics-Systems/ehco_Language-Model_v1",
        "drive.google.com",
        "1FydQKUNfpQ7oZrgpLDlqRHxFM_f1mFv5uq_akploL38",
        "eae888b784620ed37ed7d6704bcd91dedcf92936",
        "e72b2a29e52878d300b44f0286259466352f73cc",
        "42d7e0d448a59b82d15eade58e11d8de9407f7f2",
    ]
    for token in private_tokens:
        checked(token not in combined, f"Private source/topology token exposed in active public surfaces: {token}")

    raw_full_flex = ROOT / "evidence" / "runtime" / "full-flex" / "v1" / "EHCO_FULL_FLEX_PUBLIC_PACKET_V1.json"
    checked(not raw_full_flex.exists(), "Raw Full Flex packet remains in public tree")
    checked((ROOT / "evidence/runtime/full-flex/v1/PUBLIC_SAFE_RECORD.json").is_file(), "Full Flex public-safe record missing")


def validate_secret_indicators() -> None:
    patterns = [
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
        re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b"),
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    ]
    for relative in ACTIVE_PUBLIC_TEXT:
        text = read_text(relative)
        for pattern in patterns:
            checked(pattern.search(text) is None, f"High-confidence secret indicator: {relative}")


def main() -> int:
    validate_repository_residue()
    validate_dossier_and_historical_packets()
    validate_markdown_links()
    validate_dashboard_assets()
    validate_public_presentation()
    validate_secret_indicators()
    if ERRORS:
        print(f"EHCOsystem public repository validation: FAIL ({len(ERRORS)} errors / {CHECKS} checks)", file=sys.stderr)
        for error in ERRORS:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"EHCOsystem public repository validation: PASS ({CHECKS} checks) [DURABLE_PUBLIC_SEMANTICS]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
