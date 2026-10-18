$ErrorActionPreference = 'Stop'
$exe = 'C:\Windows\System32\ntoskrnl.exe'
python (Join-Path $PSScriptRoot 'build_reports.py') --exe $exe
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
python (Join-Path $PSScriptRoot 'add_beta_style.py') --exe $exe
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
python (Join-Path $PSScriptRoot 'build_control_panel.py')
exit $LASTEXITCODE
