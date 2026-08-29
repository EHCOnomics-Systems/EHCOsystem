#!/usr/bin/env python3
"""Validate the EHCOsystem public architecture and evidence estate."""

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

AFFIRMATIVE_PUBLIC_TEXT = [
    "README.md",
    "LIBRARY.md",
    "ECOSYSTEM-DILIGENCE.md",
    "GOVERNANCE.md",
    "SECURITY.md",
    "NOTICE.md",
    "PROVENANCE.md",
    "TECHNICAL-DILIGENCE.md",
    "AGENTS.md",
    ".github/pull_request_template.md",
    "getting-started/START-HERE.md",
    "getting-started/reading-order.md",
    "getting-started/repository-map.md",
    "architecture/INSTANTIATED-AI.md",
    "architecture/EHCO-TECHNOLOGY-ESTATE.md",
    "architecture/diagrams/README.md",
    "architecture/EHCO-AI-OS-INSTANTIATED-SYSTEM.md",
    "architecture/EHCO-AI-OS-SYSTEM-CARD.md",
    "architecture/GOVERNED-RUNTIME-ARCHITECTURE.md",
    "architecture/SYSTEM-INVARIANTS.md",
    "architecture/instantiated-proof-range.md",
    "architecture/ecosystem-components-and-participation.md",
    "architecture/proof-and-status-classes.md",
    "architecture/runtime-repository-and-test-estate-boundary.md",
    "language-model/README.md",
    "language-model/evidence/public-test-snapshot-v1/README.md",
    "language-model/evidence/public-test-snapshot-v1/QUALIFICATION_TEST_INDEX_2026-08-24.md",
    "assurance/README.md",
    "assurance/CLAIM-EVIDENCE-MATRIX.md",
    "assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md",
    "dossiers/README.md",
    "evidence/README.md",
    "verification/README.md",
    "releases/PUBLIC-RELEASE-REGISTER.md",
]

LM_MATURITY_PUBLIC_TEXT = [
    "README.md",
    "ECOSYSTEM-DILIGENCE.md",
    "architecture/EHCO-TECHNOLOGY-ESTATE.md",
    "architecture/ecosystem-components-and-participation.md",
    "architecture/diagrams/README.md",
    "language-model/README.md",
    "assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md",
    "verification/README.md",
]

TEXT_EXTENSIONS = {".md", ".txt", ".py", ".json", ".yaml", ".yml"}
PRIVATE_PROGRAM_HASHES = {
    "a0ab87611e3650a456af99ece0ea7cb9f24e9a38f2135ba005f765b4d41c36ad",
    "78656f1234f565253c32e16ce139165b5dfb60412e55fd14869c7728a82001d5",
    "42c0877fa495c86d47844aa1179dfdf23cff40f9a709169faeb3b0f0c7766846",
}

DASHBOARD_ASSETS = {
    "architecture/assets/dashboard/overview-june-2026-public.webp":
        "F70838036001A79064C3F2EE86D301655C44C9E1F87811FF507869B2B1A30F4A",
    "architecture/assets/dashboard/services-coordination-june-2026-public.webp":
        "1E1592A1FC209D31FA10FFAE6BA8CC14645B230038BA58D821D2093AA1DA0526",
    "architecture/assets/dashboard/authority-boundary-june-2026-public.webp":
        "6304053C6764C757E66B6917C043372DEB32F1B744308F1EB418B35A08B6754C",
    "architecture/assets/dashboard/receipts-evidence-june-2026-public.webp":
        "00843121212E99CFEF6A9DC653F0F22655D9A8E01910F9F4172F83014611F790",
    "architecture/assets/dashboard/health-registry-june-2026-public.webp":
        "615BF7449A793C9CE2F760D9E178ABD0DFA176A7DCF3BEA43D3BC6457FCC2244",
    "architecture/assets/dashboard/replacement-readiness-june-2026-public.webp":
        "906A5E5671F9F9BF54063B05885F9CAD109B957A7666680576C09CE3FD885F86",
    "architecture/assets/dashboard/prime-relationship-june-2026-public.webp":
        "EEFA86B3F8DBBC6309342EE87CAC72541AFC6679AAEAD49322E1EF08A96798CE",
    "architecture/assets/dashboard/agent-connect-coordination-june-2026-public.webp":
        "F2AF589E9706786EF38B8D1AE08AF8A967F5249173EE59C8CA5E565D9B485003",
}
DASHBOARD_README_ROUTES = (
    "architecture/assets/dashboard/overview-june-2026-public.webp",
    "architecture/assets/dashboard/services-coordination-june-2026-public.webp",
)
DASHBOARD_SYSTEM_CARD_ROUTES = (
    "assets/dashboard/authority-boundary-june-2026-public.webp",
    "assets/dashboard/receipts-evidence-june-2026-public.webp",
    "assets/dashboard/health-registry-june-2026-public.webp",
    "assets/dashboard/replacement-readiness-june-2026-public.webp",
    "assets/dashboard/prime-relationship-june-2026-public.webp",
    "assets/dashboard/agent-connect-coordination-june-2026-public.webp",
)
DASHBOARD_CAPTION = (
    "EHCO Dashboard — Tier Three projection/interface view. Public-safe derivative from an "
    "owner-supplied June 2026 EHCO Dashboard capture. Tier One Runtime authority and current "
    "Runtime-state ownership remain with `INSTANTIATED_EHCO_RUNTIME`."
)

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


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        ERRORS.append(f"JSON parse failure: {path.relative_to(ROOT)}: {exc}")
        return {}


def read_text(relative: str) -> str:
    path = ROOT / relative
    checked(path.is_file(), f"Required public text missing: {relative}")
    if not path.is_file():
        return ""
    try:
        return path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        ERRORS.append(f"Text read failure: {relative}: {exc}")
        return ""


def prose_only(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]*`", " ", text)
    return text


def validate_repository_residue() -> None:
    forbidden_exact = {
        "UPLOAD_INSTRUCTIONS_DO_NOT_COMMIT.txt",
        "PACKAGE_SHA256SUMS_DO_NOT_COMMIT.txt",
    }
    forbidden_dirs = {
        EVIDENCE_ROOT / "evidence",
        EVIDENCE_ROOT / "dossiers",
        ROOT / ".import-staging",
    }
    for directory in forbidden_dirs:
        checked(not directory.exists(), f"Forbidden directory present: {directory.relative_to(ROOT)}")

    wrong_pdf = ROOT / "evidence" / "public-evidence-companion" / DOSSIER_NAME
    checked(not wrong_pdf.exists(), f"Legacy PDF path present: {wrong_pdf.relative_to(ROOT)}")

    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        checked(path.name not in forbidden_exact, f"Upload helper present: {relative}")
        checked(path.suffix.lower() != ".zip", f"ZIP archive present: {relative}")
        checked(re.fullmatch(r"part-\d+", path.name) is None, f"Transfer chunk present: {relative}")


def validate_dossier() -> None:
    paths = [
        ROOT / "dossiers" / DOSSIER_NAME,
        EVIDENCE_ROOT / "00_DOSSIER_IDENTITY_AND_BOUNDARY" / "source_document" / DOSSIER_NAME,
    ]
    hashes: list[str] = []
    for path in paths:
        checked(path.is_file(), f"Canonical dossier missing: {path.relative_to(ROOT)}")
        if path.is_file():
            digest = sha256_file(path)
            hashes.append(digest)
            checked(digest == DOSSIER_SHA256, f"Dossier SHA-256 mismatch: {path.relative_to(ROOT)}")
    if len(hashes) == 2:
        checked(hashes[0] == hashes[1], "Canonical dossier copies differ")


def safe_manifest_path(value: str) -> bool:
    pure = PurePosixPath(value)
    return bool(value) and not pure.is_absolute() and ".." not in pure.parts and "\\" not in value


def validate_packets_and_manifests() -> dict[str, str]:
    checked(EVIDENCE_ROOT.is_dir(), "Public Evidence Companion directory missing")
    actual = sorted(path.name for path in EVIDENCE_ROOT.iterdir() if path.is_dir()) if EVIDENCE_ROOT.is_dir() else []
    checked(actual == EXPECTED_PACKETS, f"Packet directory set mismatch: {actual}")

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
        if not isinstance(manifest, dict):
            ERRORS.append(f"Manifest object invalid: {packet_name}")
            continue
        entries = manifest.get("files")
        checked(isinstance(entries, list), f"Manifest files list invalid: {packet_name}")
        if not isinstance(entries, list):
            continue
        checked(manifest.get("file_count") == len(entries), f"Manifest file_count mismatch: {packet_name}")
        self_reference = manifest.get("manifest_self_reference", manifest.get("self_reference"))
        checked(self_reference is False, f"Manifest self-reference flag mismatch: {packet_name}")

        seen: set[str] = set()
        for entry in entries:
            if not isinstance(entry, dict):
                ERRORS.append(f"Manifest entry invalid: {packet_name}")
                continue
            value = entry.get("path")
            if not isinstance(value, str) or not safe_manifest_path(value):
                ERRORS.append(f"Manifest path invalid: {packet_name}: {value!r}")
                continue
            checked(value not in seen, f"Duplicate manifest path: {packet_name}: {value}")
            seen.add(value)
            target = packet.joinpath(*PurePosixPath(value).parts)
            checked(target.is_file(), f"Manifest target missing: {target.relative_to(ROOT)}")
            if target.is_file():
                checked(target.stat().st_size == entry.get("bytes"), f"Byte count mismatch: {target.relative_to(ROOT)}")
                checked(sha256_file(target) == str(entry.get("sha256", "")).upper(), f"SHA-256 mismatch: {target.relative_to(ROOT)}")

        digest = sha256_file(manifest_path)
        manifest_hashes[packet_name] = digest
        if detached_path.is_file():
            token = detached_path.read_text(encoding="utf-8-sig").strip().split()[0].upper()
            checked(token == digest, f"Detached manifest hash mismatch: {packet_name}")
        if verification_path.is_file():
            verification = load_json(verification_path)
            if isinstance(verification, dict):
                checked(verification.get("status") == "PASS", f"Verification status mismatch: {packet_name}")
    return manifest_hashes


def validate_json_syntax() -> None:
    for path in sorted(EVIDENCE_ROOT.rglob("*.json")):
        global CHECKS
        CHECKS += 1
        load_json(path)


def validate_suite(manifest_hashes: dict[str, str]) -> None:
    suite_path = EVIDENCE_ROOT / EXPECTED_PACKETS[8] / "SUITE_MANIFEST.json"
    suite = load_json(suite_path)
    checked(isinstance(suite, dict), "Suite manifest object invalid")
    if not isinstance(suite, dict):
        return
    dossier = suite.get("dossier", {})
    checked(isinstance(dossier, dict) and str(dossier.get("sha256", "")).upper() == DOSSIER_SHA256, "Suite dossier hash mismatch")
    checked(suite.get("prior_packet_count") == 8, "Suite prior_packet_count mismatch")
    checked(suite.get("total_packet_count") == 9, "Suite total_packet_count mismatch")
    packets = suite.get("packets")
    checked(isinstance(packets, list) and len(packets) == 8, "Suite packet enumeration mismatch")
    if isinstance(packets, list):
        for index, entry in enumerate(packets):
            if not isinstance(entry, dict):
                ERRORS.append(f"Suite packet entry invalid at index {index}")
                continue
            expected = EXPECTED_PACKETS[index]
            checked(entry.get("sequence") == index, f"Suite sequence mismatch: {expected}")
            checked(entry.get("directory") == expected, f"Suite directory mismatch: {expected}")
            checked(str(entry.get("manifest_sha256", "")).upper() == manifest_hashes.get(expected), f"Suite manifest hash mismatch: {expected}")
            checked(entry.get("verification_status") == "PASS", f"Suite verification status mismatch: {expected}")


def validate_markdown_links() -> None:
    link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError):
            continue
        for raw in link_re.findall(text):
            target = raw.strip().split()[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            resolved = (path.parent / target).resolve()
            checked(resolved.exists(), f"Broken Markdown link in {path.relative_to(ROOT)}: {raw}")


def validate_dashboard_visual_orientation() -> None:
    dashboard_dir = ROOT / "architecture" / "assets" / "dashboard"
    checked(dashboard_dir.is_dir(), "Dashboard public asset directory missing")

    actual = (
        sorted(path.name for path in dashboard_dir.iterdir() if path.is_file())
        if dashboard_dir.is_dir()
        else []
    )
    expected = sorted(PurePosixPath(relative).name for relative in DASHBOARD_ASSETS)
    checked(actual == expected, f"Dashboard public asset set mismatch: {actual}")

    for relative, expected_sha256 in DASHBOARD_ASSETS.items():
        path = ROOT / relative
        checked(path.is_file(), f"Dashboard public asset missing: {relative}")
        if path.is_file():
            checked(path.suffix.lower() == ".webp", f"Dashboard public asset encoding mismatch: {relative}")
            checked(sha256_file(path) == expected_sha256, f"Dashboard SHA-256 mismatch: {relative}")

    readme = read_text("README.md")
    system_card = read_text("architecture/EHCO-AI-OS-SYSTEM-CARD.md")
    for route in DASHBOARD_README_ROUTES:
        checked(route in readme, f"README Dashboard route missing: {route}")
    for route in DASHBOARD_SYSTEM_CARD_ROUTES:
        checked(route in system_card, f"System-card Dashboard route missing: {route}")

    image_re = re.compile(r"!\[([^\]]+)\]\(([^)]+)\)")
    readme_images = {target.strip(): alt.strip() for alt, target in image_re.findall(readme)}
    system_card_images = {target.strip(): alt.strip() for alt, target in image_re.findall(system_card)}
    for route in DASHBOARD_README_ROUTES:
        checked(bool(readme_images.get(route)), f"README Dashboard alt text missing: {route}")
    for route in DASHBOARD_SYSTEM_CARD_ROUTES:
        checked(bool(system_card_images.get(route)), f"System-card Dashboard alt text missing: {route}")

    checked(readme.count(DASHBOARD_CAPTION) == 2, "README Dashboard projection caption count mismatch")
    checked(system_card.count(DASHBOARD_CAPTION) == 6, "System-card Dashboard projection caption count mismatch")

    framing_phrases = (
        "Tier Three projection/interface view",
        "June 2026 EHCO Dashboard capture",
        "Tier One Runtime authority",
        "current Runtime-state ownership remain with `INSTANTIATED_EHCO_RUNTIME`",
    )
    for phrase in framing_phrases:
        checked(phrase in readme, f"README Dashboard framing missing: {phrase}")
        checked(phrase in system_card, f"System-card Dashboard framing missing: {phrase}")


def validate_disclosure_safety() -> None:
    high_confidence = [
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
        re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b"),
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    ]
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        try:
            text = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError):
            continue
        for pattern in high_confidence:
            checked(pattern.search(text) is None, f"High-confidence secret indicator: {path.relative_to(ROOT)}")


def validate_private_program_scope() -> None:
    word_re = re.compile(r"[a-z0-9]+")
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        try:
            words = word_re.findall(path.read_text(encoding="utf-8-sig").lower())
        except (OSError, UnicodeError):
            continue
        for width in (2, 3):
            for index in range(0, max(0, len(words) - width + 1)):
                phrase = " ".join(words[index : index + width])
                digest = hashlib.sha256(phrase.encode("utf-8")).hexdigest()
                checked(digest not in PRIVATE_PROGRAM_HASHES, f"Private program marker present in current source: {path.relative_to(ROOT)}")


def validate_affirmative_public_representation() -> None:
    texts = {relative: read_text(relative) for relative in AFFIRMATIVE_PUBLIC_TEXT}
    negative_patterns = [
        re.compile(r"\bnot\b", re.IGNORECASE),
        re.compile(r"\bno\b", re.IGNORECASE),
        re.compile(r"\bnever\b", re.IGNORECASE),
        re.compile(r"\bcannot\b", re.IGNORECASE),
        re.compile(r"\bcan['’]t\b", re.IGNORECASE),
        re.compile(r"\bdon['’]t\b", re.IGNORECASE),
        re.compile(r"\bdoesn['’]t\b", re.IGNORECASE),
        re.compile(r"\bwithout\b", re.IGNORECASE),
        re.compile(r"\bnon[- ]?claim", re.IGNORECASE),
        re.compile(r"\bunproven\b", re.IGNORECASE),
        re.compile(r"\bunresolved\b", re.IGNORECASE),
        re.compile(r"\bpending\b", re.IGNORECASE),
    ]
    for relative, text in texts.items():
        prose = prose_only(text)
        for pattern in negative_patterns:
            checked(pattern.search(prose) is None, f"Negative-pressure prose pattern in {relative}: {pattern.pattern}")

    combined = "\n".join(texts.values())
    private_locator = re.compile(r"\bEHCOnomics-Systems/[A-Za-z0-9_.-]*(?:AI[-_]?OS|AIOS)[A-Za-z0-9_.-]*\b", re.IGNORECASE)
    personal_locator = re.compile(r"\behconomics/[A-Za-z0-9_.-]+\b", re.IGNORECASE)
    legacy_tier = re.compile(r"\bTier [123]\b", re.IGNORECASE)
    checked(private_locator.search(combined) is None, "Protected AI-OS source locator present in active public text")
    checked(personal_locator.search(combined) is None, "Personal-account repository locator present in active public text")
    checked(legacy_tier.search(combined) is None, "Legacy numeric tier terminology present in active public text")

    lm_internal_patterns = [
        re.compile(r"\bDeep Final Completion\b", re.IGNORECASE),
        re.compile(r"\bDF-\d+(?:\s+Unit\s+\d+)?\b", re.IGNORECASE),
        re.compile(r"\bDF-\d+\s+through\s+DF-\d+\b", re.IGNORECASE),
        re.compile(r"\bcurrent[_ -]?unit\b", re.IGNORECASE),
        re.compile(r"\bcurrent[_ -]?stage\b", re.IGNORECASE),
    ]
    for relative in LM_MATURITY_PUBLIC_TEXT:
        prose = prose_only(texts[relative])
        for pattern in lm_internal_patterns:
            checked(pattern.search(prose) is None, f"Internal Language Model development-stage maturity prose in {relative}: {pattern.pattern}")

    required = {
        "README.md": [
            "EHCO AI-OS is the realized Tier One Runtime",
            "foundational and shared EHCOsystem spine is substantially established",
            "ZERO_WEIGHT_ONLY / ZERO WEIGHTS TRAINED",
            "advanced near-final maturation cycle",
        ],
        "architecture/INSTANTIATED-AI.md": [
            "Instantiated AI creates the computational conditions under which artificial intelligence may lawfully operate.",
            "EHCOsystem is EHCOnomics' Instantiated AI ecosystem.",
            "the model supplies intelligence; the instantiated system supplies the conditions governing that intelligence",
        ],
        "architecture/EHCO-TECHNOLOGY-ESTATE.md": [
            "EHCO AI-OS is the realized Tier One Runtime",
            "PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION",
            "advanced near-final maturation cycle",
            "23 of 23",
        ],
        "architecture/ecosystem-components-and-participation.md": [
            "advanced near-final maturation cycle",
            "Stage 1 implementation active",
            "Stage 8 production-build/rehearsal hardening",
        ],
        "language-model/README.md": [
            "DETERMINISTIC_COMPUTATIONAL_LANGUAGE / SINGLE_PATH / EXPLICIT_EHCO_COMPUTATION / ZERO_WEIGHT_ONLY / ZERO WEIGHTS TRAINED",
            "advanced near-final maturation cycle",
            "seven exact synthetic fixtures covering 62 cases",
            "Public maturity is expressed through established capability and evidence",
        ],
        "assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md": [
            "Affirmative public claim",
            "Evidence scope",
            "Advanced near-final maturation",
            "Accepted 23/23 controlled baseline",
        ],
        "architecture/diagrams/README.md": [
            "EHCO AI-OS",
            "PRIMARY_ACCESSIBLE_RUNTIME_PROJECTION",
            "advanced near-final maturation",
        ],
        "verification/README.md": [
            "Language Model capability-based advanced near-final maturation representation",
            "absence of internal Language Model stage/unit/program mechanics",
        ],
    }
    for relative, phrases in required.items():
        text = texts[relative]
        for phrase in phrases:
            checked(phrase in text, f"Required affirmative representation missing in {relative}: {phrase}")


def validate_required_controls() -> None:
    checked((ROOT / "LICENSE").is_file(), "Root LICENSE missing")
    checked((ROOT / "architecture" / "runtime-repository-and-test-estate-boundary.md").is_file(), "Boundary record missing")
    readme = read_text("README.md")
    for link in [
        "architecture/INSTANTIATED-AI.md",
        "architecture/EHCO-TECHNOLOGY-ESTATE.md",
        "architecture/diagrams/README.md",
        "assurance/ECOSYSTEM-CLAIM-EVIDENCE-MATRIX.md",
        "ECOSYSTEM-DILIGENCE.md",
        "architecture/runtime-repository-and-test-estate-boundary.md",
        "(LICENSE)",
    ]:
        checked(link in readme, f"README navigation link missing: {link}")


def main() -> int:
    validate_repository_residue()
    validate_required_controls()
    validate_dossier()
    manifest_hashes = validate_packets_and_manifests()
    validate_json_syntax()
    validate_suite(manifest_hashes)
    validate_markdown_links()
    validate_dashboard_visual_orientation()
    validate_disclosure_safety()
    validate_private_program_scope()
    validate_affirmative_public_representation()

    if ERRORS:
        print(f"EHCOsystem public validation: FAIL ({len(ERRORS)} errors / {CHECKS} checks)")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print(f"EHCOsystem public validation: PASS ({CHECKS} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
