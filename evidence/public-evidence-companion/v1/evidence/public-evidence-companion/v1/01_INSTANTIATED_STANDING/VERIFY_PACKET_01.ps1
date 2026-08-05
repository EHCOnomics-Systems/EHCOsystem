param(
    [Parameter(Mandatory = $true)]
    [string]$PacketRoot,

    [Parameter(Mandatory = $true)]
    [string]$BuildRoot
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$Errors = @()
$CheckedFiles = @()

function Write-VerificationJson {
    param(
        [string]$Path,
        $Value
    )

    $Json = $Value | ConvertTo-Json -Depth 16
    [System.IO.File]::WriteAllText($Path, $Json, $Utf8NoBom)
}

try {
    $ManifestPath = Join-Path $PacketRoot "CONTENT_MANIFEST.json"
    $ManifestHashPath = Join-Path $PacketRoot "CONTENT_MANIFEST.sha256"
    $StandingRecordPath = Join-Path $PacketRoot "STANDING_RECORD.json"
    $StandingScopePath = Join-Path $PacketRoot "STANDING_SCOPE_AND_DELIVERY_SEPARATION.json"
    $ParentBindingPath = Join-Path $PacketRoot "PARENT_BINDING.json"

    foreach ($RequiredPath in @(
        $ManifestPath
        $ManifestHashPath
        $StandingRecordPath
        $StandingScopePath
        $ParentBindingPath
    )) {
        if (-not (Test-Path -LiteralPath $RequiredPath -PathType Leaf)) {
            $Errors += "MISSING_REQUIRED_FILE:$RequiredPath"
        }
    }

    if ($Errors.Count -eq 0) {
        $StoredManifestHash = (
            (Get-Content -LiteralPath $ManifestHashPath -Raw).Trim() -split "\s+"
        )[0].ToUpperInvariant()

        $ActualManifestHash = (
            Get-FileHash -LiteralPath $ManifestPath -Algorithm SHA256
        ).Hash.ToUpperInvariant()

        if ($StoredManifestHash -ne $ActualManifestHash) {
            $Errors += "CONTENT_MANIFEST_HASH_MISMATCH"
        }

        $Manifest = Get-Content -LiteralPath $ManifestPath -Raw | ConvertFrom-Json

        foreach ($Entry in @($Manifest.files)) {
            $RelativePath = [string]$Entry.path
            $TargetPath = Join-Path $PacketRoot ($RelativePath -replace "/", "\")

            if (-not (Test-Path -LiteralPath $TargetPath -PathType Leaf)) {
                $Errors += "MISSING_CONTENT_FILE:$RelativePath"
                continue
            }

            $ActualHash = (
                Get-FileHash -LiteralPath $TargetPath -Algorithm SHA256
            ).Hash.ToUpperInvariant()

            $ActualBytes = (Get-Item -LiteralPath $TargetPath).Length
            $FileStatus = "PASS"

            if ($ActualHash -ne ([string]$Entry.sha256).ToUpperInvariant()) {
                $Errors += "HASH_MISMATCH:$RelativePath"
                $FileStatus = "FAIL"
            }

            if ($ActualBytes -ne [int64]$Entry.bytes) {
                $Errors += "BYTE_LENGTH_MISMATCH:$RelativePath"
                $FileStatus = "FAIL"
            }

            $CheckedFiles += [pscustomobject]@{
                path = $RelativePath
                status = $FileStatus
                bytes = $ActualBytes
                sha256 = $ActualHash
            }
        }

        $StandingRecord = Get-Content -LiteralPath $StandingRecordPath -Raw | ConvertFrom-Json
        $StandingScope = Get-Content -LiteralPath $StandingScopePath -Raw | ConvertFrom-Json
        $ParentBinding = Get-Content -LiteralPath $ParentBindingPath -Raw | ConvertFrom-Json

        $ExpectedBaseline = "RUNTIME|GOVERNANCE|PERSISTENCE|OBSERVABILITY|RECOVERY"
        $ActualBaseline = (@($StandingRecord.accepted_baseline) -join "|")

        if ($ActualBaseline -ne $ExpectedBaseline) {
            $Errors += "ACCEPTED_BASELINE_MISMATCH"
        }

        if ([string]$StandingRecord.standing_identity.standing_corridor -ne "52/53") {
            $Errors += "STANDING_CORRIDOR_MISMATCH"
        }

        if ([string]$StandingRecord.standing_identity.runtime_authority_route -ne "V23") {
            $Errors += "RUNTIME_AUTHORITY_ROUTE_MISMATCH"
        }

        if ([string]$StandingRecord.standing_identity.runtime_authority_tier -ne "TIER1") {
            $Errors += "RUNTIME_AUTHORITY_TIER_MISMATCH"
        }

        if ($StandingRecord.authority_boundary.packet_is_runtime_authority -ne $false) {
            $Errors += "PACKET_WRONGLY_DECLARED_AS_RUNTIME_AUTHORITY"
        }

        if ([string]$StandingRecord.authority_boundary.authority_effect -ne "NONE") {
            $Errors += "AUTHORITY_EFFECT_NOT_NONE"
        }

        if ([string]$StandingRecord.authority_boundary.standing_effect -ne "NONE") {
            $Errors += "STANDING_EFFECT_NOT_NONE"
        }

        if ($StandingRecord.authority_boundary.packet_failure_changes_standing -ne $false) {
            $Errors += "PACKET_FAILURE_WRONGLY_CHANGES_STANDING"
        }

        if ($StandingScope.status_law.baseline_implies_all_products_complete -ne $false) {
            $Errors += "PRODUCT_COMPLETION_BOUNDARY_FAILURE"
        }

        if ($StandingScope.status_law.baseline_implies_production_authorized -ne $false) {
            $Errors += "PRODUCTION_AUTHORIZATION_BOUNDARY_FAILURE"
        }

        $ParentVerificationPath = Join-Path $BuildRoot "00_DOSSIER_IDENTITY_AND_BOUNDARY\VERIFICATION_RESULT.json"

        if (-not (Test-Path -LiteralPath $ParentVerificationPath -PathType Leaf)) {
            $Errors += "PARENT_VERIFICATION_RECEIPT_MISSING"
        }
        else {
            $ActualParentHash = (
                Get-FileHash -LiteralPath $ParentVerificationPath -Algorithm SHA256
            ).Hash.ToUpperInvariant()

            if ($ActualParentHash -ne ([string]$ParentBinding.parent_packet.verification_result_sha256).ToUpperInvariant()) {
                $Errors += "PARENT_VERIFICATION_HASH_MISMATCH"
            }

            $ParentVerification = Get-Content -LiteralPath $ParentVerificationPath -Raw | ConvertFrom-Json

            if ([string]$ParentVerification.status -ne "PASS") {
                $Errors += "PARENT_PACKET_NOT_PASS"
            }
        }
    }
}
catch {
    $Errors += "VERIFIER_EXCEPTION:$($_.Exception.Message)"
}

$VerificationStatus = if ($Errors.Count -eq 0) { "PASS" } else { "FAIL" }

$VerificationResult = [pscustomobject]@{
    schema = "EHCO_PACKET_VERIFICATION_RESULT_V1"
    packet_id = "01_INSTANTIATED_STANDING"
    verified_at_utc = [DateTime]::UtcNow.ToString("o")
    status = $VerificationStatus
    checked_file_count = @($CheckedFiles).Count
    checked_files = @($CheckedFiles)
    errors = @($Errors)
    authority_effect = "NONE"
    standing_effect = "NONE"
    live_runtime_reobservation_performed = $false
}

$VerificationResultPath = Join-Path $PacketRoot "VERIFICATION_RESULT.json"
Write-VerificationJson -Path $VerificationResultPath -Value $VerificationResult

if ($VerificationStatus -ne "PASS") {
    exit 1
}

exit 0