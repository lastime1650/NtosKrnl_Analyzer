$ErrorActionPreference = 'Stop'
$projectRoot = (Resolve-Path -LiteralPath $PSScriptRoot).Path
$serverScript = Join-Path $projectRoot 'tools\analysis_server.py'
$pythonCommand = Get-Command python -ErrorAction Stop
$pythonPath = $pythonCommand.Source
$baseUrl = 'http://127.0.0.1:8765'

if (-not (Test-Path -LiteralPath $serverScript -PathType Leaf)) {
    throw "Analysis service not found: $serverScript"
}

$serviceReady = $false
try {
    $health = Invoke-RestMethod -Uri "$baseUrl/api/health" -TimeoutSec 2
    if ($health.project_root -ne $projectRoot) {
        throw "Port 8765 is already serving another project root: $($health.project_root)"
    }
    $serviceReady = $true
} catch {
    if ($_.Exception.Message -like 'Port 8765 is already serving*') { throw }
}

if (-not $serviceReady) {
    $arguments = '"{0}" --root "{1}" --port 8765' -f $serverScript, $projectRoot
    Start-Process -FilePath $pythonPath -ArgumentList $arguments -WindowStyle Hidden
    $deadline = (Get-Date).AddSeconds(20)
    while ((Get-Date) -lt $deadline) {
        Start-Sleep -Milliseconds 300
        try {
            $health = Invoke-RestMethod -Uri "$baseUrl/api/health" -TimeoutSec 2
            if ($health.project_root -ne $projectRoot) {
                throw "Port 8765 is already serving another project root: $($health.project_root)"
            }
            $serviceReady = $true
            break
        } catch {
            if ($_.Exception.Message -like 'Port 8765 is already serving*') { throw }
        }
    }
}

if (-not $serviceReady) {
    throw 'The local analysis service did not start. Check that Python is installed and port 8765 is available.'
}

Start-Process $baseUrl
