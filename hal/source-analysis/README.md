# hal.dll analysis summary

- Image: `C:\Windows\System32\hal.dll`
- File version: `10.0.26100.1`
- Architecture: `x64`
- Image SHA-256: `6f8ec8f2fba2ad2ea678fa8e97e6f1ee677f6b99e4868ee2e94ebf175815a5bb`
- Matching Microsoft PDB: `symbols/hal.pdb`
- PDB identity: `ff0f78af-4301-9c3e-04c0-84da6e04995f` age `1` (key `FF0F78AF43019C3E04C084DA6E04995F1`)
- PDB size: `77,824` bytes; MSF 7.0 validated; DbgHelp symbols: `1`
- Exports: **91** (91 forwarders)
- Imports: **0**
- Executable PE sections: **0**
- x64 runtime function records: **0**
- PDB function records in executable sections: **0**
- Forwarders resolved to system `ntoskrnl.exe` exports: **91 / 91**
- Linked to existing ntoskrnl function reports: **89 / 91**
- Current ntoskrnl PDB key matches the existing project: **True**

## Interpretation

This `hal.dll` is a PE export-forwarder layer. Each exported name redirects to the same-named export in the system `ntoskrnl.exe`. It contains no executable code section, so there are no HAL function bodies to disassemble or translate into C. Per-export Markdown files document the forwarding target and link to the existing ntoskrnl analysis when available.

PDB symbols name compiled entities; they do not recover Microsoft's original private source. The export-directory RVA is not an executable code address.
