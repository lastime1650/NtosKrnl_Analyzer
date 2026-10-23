# HalRequestIpi

> HAL export forwarder · ordinal 55 · export-directory RVA 0x00003FCC

## Identification

- Image: `hal.dll` (C:\Windows\System32\hal.dll)
- Export type: `forwarder`
- Forward destination: `ntoskrnl.HalRequestIpi`
- Matched system `ntoskrnl.exe` export RVA: `0x002D1720`
- Existing ntoskrnl analysis: [HalRequestIpi](../../analyses/NtKrnl2C-PDBFix2/functions/text/2D/HalRequestIpi_function_002D1720.md)

## 1. Dependencies

The HAL export directory forwards this name to `ntoskrnl.HalRequestIpi`. Its RVA points to a forwarder string in the export directory, not to executable instructions.

## 2. Cross-module path

`caller → hal.dll!HalRequestIpi (export resolution) → ntoskrnl.exe!HalRequestIpi`

This is the PE forwarding relationship, not a claim that the DLL executes a wrapper or that every runtime caller has the same stack.

## 3. Assembly

This export has no function-body disassembly in `hal.dll`. The image has no executable section; the export is a forwarder entry.

## 4. Pseudocode

The loader resolves this export to `ntoskrnl.HalRequestIpi`. There is no HAL function body in this image to decompile.

## 5. (Beta) C Style

A C implementation cannot be reconstructed from this HAL image because this entry is forwarding metadata, not code. See the linked `ntoskrnl.exe` report for the implementation analysis when available.

## Symbol evidence

- HAL PDB: `hal.pdb`, GUID `ff0f78af-4301-9c3e-04c0-84da6e04995f`, age `1`
- PDB key: `FF0F78AF43019C3E04C084DA6E04995F1`
- Executable-section function records in this image: 0
