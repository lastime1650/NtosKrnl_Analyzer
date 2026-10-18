# IopLoadDriver

- RVA: `0x00997B54`–`0x00998528` (길이 `2,516` bytes)
- VA: `0x0000000140997B54`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009938C`
- 디코드: `611`개 명령, `2,516/2,516` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **75**; 고유 호출 대상: **43**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x00997BDE` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00997BE9` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00997BF4` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00997BFF` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00997C19` → [NtQueryKey](../86/NtQueryKey_function_008676E0.md) (function, `0x008676E0`)
- `0x00997C38` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00997C60` → [NtQueryKey](../86/NtQueryKey_function_008676E0.md) (function, `0x008676E0`)
- `0x00997C82` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00997CB6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00997CD2` → [IopBuildFullDriverPath](IopBuildFullDriverPath_function_009998E4.md) (function, `0x009998E4`)
- `0x00997CEB` → [wcsrchr](../../text/50/wcsrchr_function_00501E50.md) (function, `0x00501E50`)
- `0x00997D05` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00997D13` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00997D23` → [PnpDiagnosticTraceObject](../../text/26/PnpDiagnosticTraceObject_function_0026E834.md) (function, `0x0026E834`)
- `0x00997D3B` → [IopGetDriverNameFromKeyNode](IopGetDriverNameFromKeyNode_function_00998808.md) (function, `0x00998808`)
- `0x00997D87` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00997DB1` → [MmLoadSystemImageEx](MmLoadSystemImageEx_function_00999B8C.md) (function, `0x00999B8C`)
- `0x00997DD2` → [PsGetCurrentSilo](../../text/40/PsGetCurrentSilo_function_004094A0.md) (function, `0x004094A0`)
- `0x00997DFC` → [ObOpenObjectByNameEx](../89/ObOpenObjectByNameEx_function_0089A8A0.md) (function, `0x0089A8A0`)
- `0x00997E2F` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00997E3A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00997E4C` → [IopResurrectDriver](../../text/4B/IopResurrectDriver_function_004B138C.md) (function, `0x004B138C`)
- `0x00997E58` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00997E65` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00997E70` → [IopBootLog](../A9/IopBootLog_function_00A90998.md) (function, `0x00A90998`)
- `0x00997E89` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00997EA3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00997F55` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00997F7E` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00997F89` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00997F99` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00997FAA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00997FB4` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00997FC5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00997FEA` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (function, `0x00443B60`)
- `0x00998020` → [PnpPrepareDriverLoading](PnpPrepareDriverLoading_function_00996CC8.md) (function, `0x00996CC8`)
- `0x0099806D` → [ObCreateObjectEx](../89/ObCreateObjectEx_function_0089B1E0.md) (function, `0x0089B1E0`)
- `0x00998088` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009980C7` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (function, `0x00443B60`)
- `0x0099812E` → [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)
- `0x00998138` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00998176` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00998187` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x009981A9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009981CD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009981F2` → [NtQueryObject](../8A/NtQueryObject_function_008A6DB0.md) (function, `0x008A6DB0`)
- `0x0099822E` → [PnpDiagnosticTraceObject](../../text/26/PnpDiagnosticTraceObject_function_0026E834.md) (function, `0x0026E834`)
- `0x00998236` → [VfDifCaptureDriverEntry](../../text/4A/VfDifCaptureDriverEntry_function_004A86F8.md) (function, `0x004A86F8`)
- `0x00998241` → [PnpCallDriverEntry](PnpCallDriverEntry_function_00996AF4.md) (function, `0x00996AF4`)
- `0x0099825D` → [PnpDiagnosticTraceObjectWithStatus](../../text/4A/PnpDiagnosticTraceObjectWithStatus_function_004A9F58.md) (function, `0x004A9F58`)
- `0x009982A7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009982B7` → [ObMakeTemporaryObject](../A7/ObMakeTemporaryObject_function_00A7F860.md) (function, `0x00A7F860`)
- `0x009982BF` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00998337` → [MmUnloadSystemImage](../AA/MmUnloadSystemImage_function_00AA2F60.md) (function, `0x00AA2F60`)
- `0x0099833F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0099834B` → [IopBootLog](../A9/IopBootLog_function_00A90998.md) (function, `0x00A90998`)
- `0x00998361` → [IopBootLog](../A9/IopBootLog_function_00A90998.md) (function, `0x00A90998`)
- `0x0099836A` → [MmFreeDriverInitialization](../A4/MmFreeDriverInitialization_function_00A4AD08.md) (function, `0x00A4AD08`)
- `0x00998372` → [IopReadyDeviceObjects](../AA/IopReadyDeviceObjects_function_00AA68A4.md) (function, `0x00AA68A4`)
- `0x0099837B` → [EtwTiLogDriverObjectLoad](../A9/EtwTiLogDriverObjectLoad_function_00A985E0.md) (function, `0x00A985E0`)
- `0x00998396` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009983DD` → [VfDifCaptureIoCallbacks](../../text/4A/VfDifCaptureIoCallbacks_function_004A8698.md) (function, `0x004A8698`)
- `0x009983EA` → [KseShimDriverIoCallbacks](../95/KseShimDriverIoCallbacks_function_00958BFC.md) (function, `0x00958BFC`)
- `0x00998411` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0099841E` → [ObMakeTemporaryObject](../A7/ObMakeTemporaryObject_function_00A7F860.md) (function, `0x00A7F860`)
- `0x00998426` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00998441` → [IopCheckIfNotNativeDriver](../71/IopCheckIfNotNativeDriver_function_0071AFB4.md) (function, `0x0071AFB4`)
- `0x00998463` → [IopLogBlockedDriverEvent](../71/IopLogBlockedDriverEvent_function_0071BBFC.md) (function, `0x0071BBFC`)
- `0x00998470` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0099847C` → [IopBootLog](../A9/IopBootLog_function_00A90998.md) (function, `0x00A90998`)
- `0x009984B0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x009984B9` → [ObMakeTemporaryObject](../A7/ObMakeTemporaryObject_function_00A7F860.md) (function, `0x00A7F860`)
- `0x009984C1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009984CB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009984F3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [PipCallDriverAddDeviceQueryRoutine](PipCallDriverAddDeviceQueryRoutine_function_00996604.md) at `0x009968A1`
- [IopLoadUnloadDriver](IopLoadUnloadDriver_function_00996B80.md) at `0x00996BF6`
- [IopInitializeSystemDrivers](../../init/C7/IopInitializeSystemDrivers_function_00C73590.md) at `0x00C73731`

### Static image references
- `0x00997B73` → RVA `0x00E0A740` (`.data`; read)
- `0x00997D1C` → RVA `0x00013360` (`.rdata`; read)
- `0x00997D4A` → RVA `0x00E0A9C0` (`.data`; read)
- `0x00997D50` → RVA `0x00F8D3A0` (`.data`; read)
- `0x00997DCB` → RVA `0x00FC6C78` (`ALMOSTRO`; read)
- `0x00997F1F` → RVA `0x00E662D8` (`.data`; read)
- `0x00997F4E` → RVA `0x00013370` (`.rdata`; read)
- `0x0099809B` → RVA `0x0029B590` (`IopInvalidDeviceRequest`; read)
- `0x00998191` → RVA `0x00FD9DE8` (`PAGEDATA`; read)
- `0x00998227` → RVA `0x00013390` (`.rdata`; read)
- `0x00998253` → RVA `0x00013380` (`.rdata`; read)
- `0x009982DD` → RVA `0x00FC41C4` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **47**
  - `0x00997BDE` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00997BE9` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00997BF4` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00997BFF` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00997C38` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00997C82` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00997CB6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00997CEB` → [wcsrchr](../../text/50/wcsrchr_function_00501E50.md) (`PAGE` → `.text`)
  - `0x00997D05` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00997D13` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`PAGE` → `.text`)
  - `0x00997D23` → [PnpDiagnosticTraceObject](../../text/26/PnpDiagnosticTraceObject_function_0026E834.md) (`PAGE` → `.text`)
  - `0x00997D87` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00997DD2` → [PsGetCurrentSilo](../../text/40/PsGetCurrentSilo_function_004094A0.md) (`PAGE` → `.text`)
  - `0x00997E3A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00997E4C` → [IopResurrectDriver](../../text/4B/IopResurrectDriver_function_004B138C.md) (`PAGE` → `.text`)
  - `0x00997E58` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00997E65` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00997E89` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`PAGE` → `.text`)
  - `0x00997EA3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00997F55` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00997F7E` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00997F89` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00997F99` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00997FAA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00997FC5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00997FEA` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (`PAGE` → `.text`)
  - `0x00998088` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009980C7` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (`PAGE` → `.text`)
  - `0x00998138` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00998187` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x009981A9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009981CD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0099822E` → [PnpDiagnosticTraceObject](../../text/26/PnpDiagnosticTraceObject_function_0026E834.md) (`PAGE` → `.text`)
  - `0x00998236` → [VfDifCaptureDriverEntry](../../text/4A/VfDifCaptureDriverEntry_function_004A86F8.md) (`PAGE` → `.text`)
  - `0x0099825D` → [PnpDiagnosticTraceObjectWithStatus](../../text/4A/PnpDiagnosticTraceObjectWithStatus_function_004A9F58.md) (`PAGE` → `.text`)
  - `0x009982A7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009982BF` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0099833F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00998396` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009983DD` → [VfDifCaptureIoCallbacks](../../text/4A/VfDifCaptureIoCallbacks_function_004A8698.md) (`PAGE` → `.text`)
  - `0x00998411` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00998426` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00998470` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009984B0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x009984C1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009984CB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009984F3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x009982EA` → [sub_00B2CB5C](../B2/Unknown_function_00B2CB5C.md) (`tail-transfer`)
  - `0x00998318` → [sub_00B2CB5C + 0xD2](../B2/Unknown_function_00B2CB5C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00997B54  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00997B59  55                              push rbp
00997B5A  56                              push rsi
00997B5B  57                              push rdi
00997B5C  41 54                           push r12
00997B5E  41 55                           push r13
00997B60  41 56                           push r14
00997B62  41 57                           push r15
00997B64  48 8D AC 24 70 FF FF FF         lea rbp, [rsp - 0x90]
00997B6C  48 81 EC 90 01 00 00            sub rsp, 0x190
00997B73  48 8B 05 C6 2B 47 00            mov rax, qword ptr [rip + 0x472bc6]
00997B7A  48 33 C4                        xor rax, rsp
00997B7D  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00997B84  33 FF                           xor edi, edi
00997B86  4C 89 4D E0                     mov qword ptr [rbp - 0x20], r9
00997B8A  0F 57 C0                        xorps xmm0, xmm0
00997B8D  89 7C 24 78                     mov dword ptr [rsp + 0x78], edi
00997B91  44 8A F2                        mov r14b, dl
00997B94  89 7D EC                        mov dword ptr [rbp - 0x14], edi
00997B97  4C 8B F9                        mov r15, rcx
00997B9A  89 7D 04                        mov dword ptr [rbp + 4], edi
00997B9D  0F 57 C9                        xorps xmm1, xmm1
00997BA0  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
00997BA5  33 D2                           xor edx, edx
00997BA7  48 89 7D A0                     mov qword ptr [rbp - 0x60], rdi
00997BAB  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00997BB0  48 89 7D C8                     mov qword ptr [rbp - 0x38], rdi
00997BB4  44 8B EF                        mov r13d, edi
00997BB7  48 89 7D 88                     mov qword ptr [rbp - 0x78], rdi
00997BBB  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00997BC0  44 8B E7                        mov r12d, edi
00997BC3  41 89 39                        mov dword ptr [r9], edi
00997BC6  0F 11 4D 90                     movups xmmword ptr [rbp - 0x70], xmm1
00997BCA  89 7D 80                        mov dword ptr [rbp - 0x80], edi
00997BCD  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
00997BD1  40 88 7C 24 50                  mov byte ptr [rsp + 0x50], dil
00997BD6  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
00997BDA  41 0F B6 F0                     movzx esi, r8b
00997BDE  E8 9D 2B A9 FF                  call 0x14042a780
00997BE3  33 D2                           xor edx, edx
00997BE5  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00997BE9  E8 92 2B A9 FF                  call 0x14042a780
00997BEE  33 D2                           xor edx, edx
00997BF0  48 8D 4D B8                     lea rcx, [rbp - 0x48]
00997BF4  E8 87 2B A9 FF                  call 0x14042a780
00997BF9  33 D2                           xor edx, edx
00997BFB  48 8D 4D A8                     lea rcx, [rbp - 0x58]
00997BFF  E8 7C 2B A9 FF                  call 0x14042a780
00997C04  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00997C09  45 33 C9                        xor r9d, r9d
00997C0C  45 33 C0                        xor r8d, r8d
00997C0F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00997C14  33 D2                           xor edx, edx
00997C16  49 8B CF                        mov rcx, r15
00997C19  E8 C2 FA EC FF                  call 0x1408676e0
00997C1E  3D 05 00 00 80                  cmp eax, 0x80000005
00997C23  0F 85 F4 06 00 00               jne 0x14099831d
00997C29  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
00997C2D  B9 40 00 00 00                  mov ecx, 0x40
00997C32  41 B8 49 6F 4B 65               mov r8d, 0x654b6f49
00997C38  E8 B3 A4 1E 00                  call 0x140b820f0
00997C3D  4C 8B E8                        mov r13, rax
00997C40  48 85 C0                        test rax, rax
00997C43  0F 84 E2 07 00 00               je 0x14099842b
00997C49  44 8B 4C 24 78                  mov r9d, dword ptr [rsp + 0x78]
00997C4E  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00997C53  4D 8B C5                        mov r8, r13
00997C56  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00997C5B  33 D2                           xor edx, edx
00997C5D  49 8B CF                        mov rcx, r15
00997C60  E8 7B FA EC FF                  call 0x1408676e0
00997C65  8B D8                           mov ebx, eax
00997C67  85 C0                           test eax, eax
00997C69  0F 88 E1 06 00 00               js 0x140998350
00997C6F  41 8B 55 0C                     mov edx, dword ptr [r13 + 0xc]
00997C73  B9 00 01 00 00                  mov ecx, 0x100
00997C78  48 83 C2 02                     add rdx, 2
00997C7C  41 B8 49 6F 4E 31               mov r8d, 0x314e6f49
00997C82  E8 69 A4 1E 00                  call 0x140b820f0
00997C87  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00997C8B  48 8B F8                        mov rdi, rax
00997C8E  48 85 C0                        test rax, rax
00997C91  0F 84 94 07 00 00               je 0x14099842b
00997C97  41 0F B7 5D 0C                  movzx ebx, word ptr [r13 + 0xc]
00997C9C  49 8D 55 10                     lea rdx, [r13 + 0x10]
00997CA0  45 8B 45 0C                     mov r8d, dword ptr [r13 + 0xc]
00997CA4  B9 02 00 00 00                  mov ecx, 2
00997CA9  03 CB                           add ecx, ebx
00997CAB  66 89 5D 90                     mov word ptr [rbp - 0x70], bx
00997CAF  66 89 4D 92                     mov word ptr [rbp - 0x6e], cx
00997CB3  48 8B C8                        mov rcx, rax
00997CB6  E8 85 EB D2 FF                  call 0x1406c6840
00997CBB  33 C9                           xor ecx, ecx
00997CBD  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00997CC2  8B C3                           mov eax, ebx
00997CC4  49 8B D7                        mov rdx, r15
00997CC7  48 D1 E8                        shr rax, 1
00997CCA  66 89 0C 47                     mov word ptr [rdi + rax*2], cx
00997CCE  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00997CD2  E8 0D 1C 00 00                  call 0x1409998e4
00997CD7  8B D8                           mov ebx, eax
00997CD9  85 C0                           test eax, eax
00997CDB  0F 88 6F 06 00 00               js 0x140998350
00997CE1  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00997CE6  BA 5C 00 00 00                  mov edx, 0x5c
00997CEB  E8 60 A1 B6 FF                  call 0x140501e50
00997CF0  48 85 C0                        test rax, rax
00997CF3  0F 84 C1 06 00 00               je 0x1409983ba
00997CF9  48 8D 50 02                     lea rdx, [rax + 2]
00997CFD  48 8D 4D B8                     lea rcx, [rbp - 0x48]
00997D01  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
00997D05  E8 76 2A A9 FF                  call 0x14042a780
00997D0A  48 8D 55 B8                     lea rdx, [rbp - 0x48]
00997D0E  B9 01 00 00 00                  mov ecx, 1
00997D13  E8 D4 00 B2 FF                  call 0x1404b7dec
00997D18  48 8D 55 90                     lea rdx, [rbp - 0x70]
00997D1C  48 8D 0D 3D B6 67 FF            lea rcx, [rip - 0x9849c3]
00997D23  E8 0C 6B 8D FF                  call 0x14026e834
00997D28  45 84 F6                        test r14b, r14b
00997D2B  0F 85 A9 05 00 00               jne 0x1409982da
00997D31  45 33 F6                        xor r14d, r14d
00997D34  48 8D 55 A8                     lea rdx, [rbp - 0x58]
00997D38  49 8B CF                        mov rcx, r15
00997D3B  E8 C8 0A 00 00                  call 0x140998808
00997D40  8B D8                           mov ebx, eax
00997D42  85 C0                           test eax, eax
00997D44  0F 88 06 06 00 00               js 0x140998350
00997D4A  8B 05 70 2C 47 00               mov eax, dword ptr [rip + 0x472c70]
00997D50  48 8D 3D 49 56 5F 00            lea rdi, [rip + 0x5f5649]
00997D57  F7 D8                           neg eax
00997D59  C7 45 E8 30 00 00 00            mov dword ptr [rbp - 0x18], 0x30
00997D60  48 8D 45 A8                     lea rax, [rbp - 0x58]
00997D64  4C 89 75 F0                     mov qword ptr [rbp - 0x10], r14
00997D68  1B C9                           sbb ecx, ecx
00997D6A  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00997D6E  83 E1 40                        and ecx, 0x40
00997D71  0F 57 C0                        xorps xmm0, xmm0
00997D74  81 C1 10 02 00 00               add ecx, 0x210
00997D7A  B2 01                           mov dl, 1
00997D7C  89 4D 00                        mov dword ptr [rbp], ecx
00997D7F  48 8B CF                        mov rcx, rdi
00997D82  F3 0F 7F 45 08                  movdqu xmmword ptr [rbp + 8], xmm0
00997D87  E8 94 D0 87 FF                  call 0x140214e20
00997D8C  48 8D 45 C8                     lea rax, [rbp - 0x38]
00997D90  45 33 C9                        xor r9d, r9d
00997D93  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00997D98  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00997D9D  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00997DA2  45 33 C0                        xor r8d, r8d
00997DA5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00997DAA  33 D2                           xor edx, edx
00997DAC  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00997DB1  E8 D6 1D 00 00                  call 0x140999b8c
00997DB6  8B D8                           mov ebx, eax
00997DB8  85 C0                           test eax, eax
00997DBA  0F 89 26 02 00 00               jns 0x140997fe6
00997DC0  3D 0E 01 00 C0                  cmp eax, 0xc000010e
00997DC5  0F 85 6F 06 00 00               jne 0x14099843a
00997DCB  48 8B 1D A6 EE 62 00            mov rbx, qword ptr [rip + 0x62eea6]
00997DD2  E8 C9 16 A7 FF                  call 0x1404094a0
00997DD7  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00997DDB  45 33 C9                        xor r9d, r9d
00997DDE  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00997DE3  45 33 C0                        xor r8d, r8d
00997DE6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00997DEB  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00997DEF  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00997DF4  48 8B D3                        mov rdx, rbx
00997DF7  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00997DFC  E8 9F 2A F0 FF                  call 0x14089a8a0
00997E01  8B D8                           mov ebx, eax
00997E03  85 C0                           test eax, eax
00997E05  0F 88 62 06 00 00               js 0x14099846d
00997E0B  4C 8B 05 66 EE 62 00            mov r8, qword ptr [rip + 0x62ee66]
00997E12  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00997E17  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
00997E1B  45 33 C9                        xor r9d, r9d
00997E1E  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00997E23  33 D2                           xor edx, edx
00997E25  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00997E2A  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
00997E2F  E8 7C 0F ED FF                  call 0x140868db0
00997E34  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
00997E38  8B D8                           mov ebx, eax
00997E3A  E8 71 54 D1 FF                  call 0x1406ad2b0
00997E3F  85 DB                           test ebx, ebx
00997E41  0F 88 F5 04 00 00               js 0x14099833c
00997E47  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00997E4C  E8 3B 95 B1 FF                  call 0x1404b138c
00997E51  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00997E56  8B D8                           mov ebx, eax
00997E58  E8 F3 14 96 FF                  call 0x1402f9350
00997E5D  48 8D 74 24 68                  lea rsi, [rsp + 0x68]
00997E62  48 8B CF                        mov rcx, rdi
00997E65  E8 A6 7B 8C FF                  call 0x14025fa10
00997E6A  41 8A D6                        mov dl, r14b
00997E6D  48 8B CE                        mov rcx, rsi
00997E70  E8 23 8B 0F 00                  call 0x140a90998
00997E75  BE 65 03 00 C0                  mov esi, 0xc0000365
00997E7A  85 DB                           test ebx, ebx
00997E7C  0F 88 42 04 00 00               js 0x1409982c4
00997E82  B9 02 00 00 00                  mov ecx, 2
00997E87  33 D2                           xor edx, edx
00997E89  E8 5E FF B1 FF                  call 0x1404b7dec
00997E8E  45 33 F6                        xor r14d, r14d
00997E91  85 DB                           test ebx, ebx
00997E93  0F 88 56 04 00 00               js 0x1409982ef
00997E99  4D 85 ED                        test r13, r13
00997E9C  74 0A                           je 0x140997ea8
00997E9E  33 D2                           xor edx, edx
00997EA0  49 8B CD                        mov rcx, r13
00997EA3  E8 C8 A9 1E 00                  call 0x140b82870
00997EA8  48 8B 75 98                     mov rsi, qword ptr [rbp - 0x68]
00997EAC  48 85 F6                        test rsi, rsi
00997EAF  0F 84 D9 00 00 00               je 0x140997f8e
00997EB5  0F B7 45 90                     movzx eax, word ptr [rbp - 0x70]
00997EB9  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
00997EBD  66 D1 E8                        shr ax, 1
00997EC0  66 89 44 24 50                  mov word ptr [rsp + 0x50], ax
00997EC5  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00997ECA  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00997ECE  0F B7 45 90                     movzx eax, word ptr [rbp - 0x70]
00997ED2  89 45 38                        mov dword ptr [rbp + 0x38], eax
00997ED5  48 8D 45 A0                     lea rax, [rbp - 0x60]
00997ED9  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00997EDD  44 89 65 80                     mov dword ptr [rbp - 0x80], r12d
00997EE1  89 5D A0                        mov dword ptr [rbp - 0x60], ebx
00997EE4  48 C7 45 28 02 00 00 00         mov qword ptr [rbp + 0x28], 2
00997EEC  48 89 75 30                     mov qword ptr [rbp + 0x30], rsi
00997EF0  44 89 75 3C                     mov dword ptr [rbp + 0x3c], r14d
00997EF4  48 C7 45 48 04 00 00 00         mov qword ptr [rbp + 0x48], 4
00997EFC  48 85 C9                        test rcx, rcx
00997EFF  0F 84 1B 06 00 00               je 0x140998520
00997F05  0F B7 45 A8                     movzx eax, word ptr [rbp - 0x58]
00997F09  66 D1 E8                        shr ax, 1
00997F0C  66 89 44 24 60                  mov word ptr [rsp + 0x60], ax
00997F11  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00997F16  0F B7 C0                        movzx eax, ax
00997F19  03 C0                           add eax, eax
00997F1B  48 89 4D 60                     mov qword ptr [rbp + 0x60], rcx
00997F1F  48 8B 0D B2 E3 4C 00            mov rcx, qword ptr [rip + 0x4ce3b2]
00997F26  89 45 68                        mov dword ptr [rbp + 0x68], eax
00997F29  48 8D 45 80                     lea rax, [rbp - 0x80]
00997F2D  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00997F31  4C 89 45 50                     mov qword ptr [rbp + 0x50], r8
00997F35  48 C7 45 58 02 00 00 00         mov qword ptr [rbp + 0x58], 2
00997F3D  44 89 75 6C                     mov dword ptr [rbp + 0x6c], r14d
00997F41  48 C7 45 78 04 00 00 00         mov qword ptr [rbp + 0x78], 4
00997F49  48 85 C9                        test rcx, rcx
00997F4C  74 35                           je 0x140997f83
00997F4E  48 8D 15 1B B4 67 FF            lea rdx, [rip - 0x984be5]
00997F55  E8 F6 A4 9F FF                  call 0x140392450
00997F5A  84 C0                           test al, al
00997F5C  74 25                           je 0x140997f83
00997F5E  48 8B 0D 73 E3 4C 00            mov rcx, qword ptr [rip + 0x4ce373]
00997F65  48 8D 45 20                     lea rax, [rbp + 0x20]
00997F69  41 B9 06 00 00 00               mov r9d, 6
00997F6F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00997F74  45 33 C0                        xor r8d, r8d
00997F77  48 8D 15 F2 B3 67 FF            lea rdx, [rip - 0x984c0e]
00997F7E  E8 9D 47 A8 FF                  call 0x14041c720
00997F83  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00997F87  33 D2                           xor edx, edx
00997F89  E8 E2 A8 1E 00                  call 0x140b82870
00997F8E  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
00997F92  48 85 C9                        test rcx, rcx
00997F95  74 07                           je 0x140997f9e
00997F97  33 D2                           xor edx, edx
00997F99  E8 D2 A8 1E 00                  call 0x140b82870
00997F9E  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00997FA3  48 85 C9                        test rcx, rcx
00997FA6  74 07                           je 0x140997faf
00997FA8  33 D2                           xor edx, edx
00997FAA  E8 C1 A8 1E 00                  call 0x140b82870
00997FAF  33 D2                           xor edx, edx
00997FB1  49 8B CF                        mov rcx, r15
00997FB4  E8 B7 98 F0 FF                  call 0x1408a1870
00997FB9  8B C3                           mov eax, ebx
00997FBB  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
00997FC2  48 33 CC                        xor rcx, rsp
00997FC5  E8 76 46 D1 FF                  call 0x1406ac640
00997FCA  48 8B 9C 24 D8 01 00 00         mov rbx, qword ptr [rsp + 0x1d8]
00997FD2  48 81 C4 90 01 00 00            add rsp, 0x190
00997FD9  41 5F                           pop r15
00997FDB  41 5E                           pop r14
00997FDD  41 5D                           pop r13
00997FDF  41 5C                           pop r12
00997FE1  5F                              pop rdi
00997FE2  5E                              pop rsi
00997FE3  5D                              pop rbp
00997FE4  C3                              ret
00997FE5  CC                              int3
00997FE6  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00997FEA  E8 71 BB AA FF                  call 0x140443b60
00997FEF  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
00997FF3  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00997FF7  44 8B CE                        mov r9d, esi
00997FFA  49 8B D7                        mov rdx, r15
00997FFD  44 0F B7 60 44                  movzx r12d, word ptr [rax + 0x44]
00998002  0F B7 40 46                     movzx eax, word ptr [rax + 0x46]
00998006  41 C1 E4 10                     shl r12d, 0x10
0099800A  44 0B E0                        or r12d, eax
0099800D  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00998012  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00998017  48 8D 45 80                     lea rax, [rbp - 0x80]
0099801B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00998020  E8 A3 EC FF FF                  call 0x140996cc8
00998025  8B D8                           mov ebx, eax
00998027  85 C0                           test eax, eax
00998029  0F 88 03 03 00 00               js 0x140998332
0099802F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00998038  4C 8D 45 E8                     lea r8, [rbp - 0x18]
0099803C  48 8B 15 35 EC 62 00            mov rdx, qword ptr [rip + 0x62ec35]
00998043  BE A8 01 00 00                  mov esi, 0x1a8
00998048  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
0099804D  45 33 C9                        xor r9d, r9d
00998050  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
00998056  48 8D 45 A0                     lea rax, [rbp - 0x60]
0099805A  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0099805F  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00998064  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00998069  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
0099806D  E8 6E 31 F0 FF                  call 0x14089b1e0
00998072  8B D8                           mov ebx, eax
00998074  85 C0                           test eax, eax
00998076  0F 88 B6 02 00 00               js 0x140998332
0099807C  48 8B 5D A0                     mov rbx, qword ptr [rbp - 0x60]
00998080  44 8B C6                        mov r8d, esi
00998083  48 8B CB                        mov rcx, rbx
00998086  33 D2                           xor edx, edx
00998088  E8 B3 EB D2 FF                  call 0x1406c6c40
0099808D  48 8D 83 50 01 00 00            lea rax, [rbx + 0x150]
00998094  41 8B CE                        mov ecx, r14d
00998097  48 89 43 30                     mov qword ptr [rbx + 0x30], rax
0099809B  48 8D 15 EE 34 90 FF            lea rdx, [rip - 0x6fcb12]
009980A2  48 89 18                        mov qword ptr [rax], rbx
009980A5  41 8B C6                        mov eax, r14d
009980A8  48 89 54 C3 70                  mov qword ptr [rbx + rax*8 + 0x70], rdx
009980AD  8D 41 01                        lea eax, [rcx + 1]
009980B0  8B C8                           mov ecx, eax
009980B2  83 F8 1B                        cmp eax, 0x1b
009980B5  76 F1                           jbe 0x1409980a8
009980B7  48 8B 75 C8                     mov rsi, qword ptr [rbp - 0x38]
009980BB  48 8B CE                        mov rcx, rsi
009980BE  89 45 A0                        mov dword ptr [rbp - 0x60], eax
009980C1  C7 03 04 00 50 01               mov dword ptr [rbx], 0x1500004
009980C7  E8 94 BA AA FF                  call 0x140443b60
009980CC  48 8B D0                        mov rdx, rax
009980CF  44 0F B7 60 44                  movzx r12d, word ptr [rax + 0x44]
009980D4  0F B7 48 46                     movzx ecx, word ptr [rax + 0x46]
009980D8  8B 40 28                        mov eax, dword ptr [rax + 0x28]
009980DB  41 C1 E4 10                     shl r12d, 0x10
009980DF  48 03 C6                        add rax, rsi
009980E2  44 0B E1                        or r12d, ecx
009980E5  66 0F BA 62 5E 0D               bt word ptr [rdx + 0x5e], 0xd
009980EB  72 08                           jb 0x1409980f5
009980ED  B9 02 00 00 00                  mov ecx, 2
009980F2  09 4B 10                        or dword ptr [rbx + 0x10], ecx
009980F5  48 89 43 58                     mov qword ptr [rbx + 0x58], rax
009980F9  45 33 C9                        xor r9d, r9d
009980FC  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00998101  48 8B CB                        mov rcx, rbx
00998104  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
00998108  48 89 73 18                     mov qword ptr [rbx + 0x18], rsi
0099810C  8B 42 50                        mov eax, dword ptr [rdx + 0x50]
0099810F  41 8D 71 01                     lea esi, [r9 + 1]
00998113  89 43 20                        mov dword ptr [rbx + 0x20], eax
00998116  44 8B C6                        mov r8d, esi
00998119  48 8D 45 88                     lea rax, [rbp - 0x78]
0099811D  33 D2                           xor edx, edx
0099811F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00998124  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00998129  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
0099812E  E8 6D 16 F2 FF                  call 0x1408b97a0
00998133  48 8B CF                        mov rcx, rdi
00998136  8B D8                           mov ebx, eax
00998138  E8 D3 78 8C FF                  call 0x14025fa10
0099813D  33 D2                           xor edx, edx
0099813F  85 DB                           test ebx, ebx
00998141  0F 88 FF 01 00 00               js 0x140998346
00998147  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00998150  4C 8B 05 21 EB 62 00            mov r8, qword ptr [rip + 0x62eb21]
00998157  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
0099815B  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00998160  44 8A 88 32 02 00 00            mov r9b, byte ptr [rax + 0x232]
00998167  48 8D 44 24 58                  lea rax, [rsp + 0x58]
0099816C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00998171  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
00998176  E8 35 0C ED FF                  call 0x140868db0
0099817B  85 C0                           test eax, eax
0099817D  0F 85 17 03 00 00               jne 0x14099849a
00998183  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
00998187  E8 24 51 D1 FF                  call 0x1406ad2b0
0099818C  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00998191  48 8D 05 50 1C 64 00            lea rax, [rip + 0x641c50]
00998198  8D 4E 3F                        lea ecx, [rsi + 0x3f]
0099819B  41 B8 49 6F 4E 31               mov r8d, 0x314e6f49
009981A1  48 89 47 48                     mov qword ptr [rdi + 0x48], rax
009981A5  0F B7 55 AA                     movzx edx, word ptr [rbp - 0x56]
009981A9  E8 42 9F 1E 00                  call 0x140b820f0
009981AE  48 89 47 40                     mov qword ptr [rdi + 0x40], rax
009981B2  48 85 C0                        test rax, rax
009981B5  0F 85 39 02 00 00               jne 0x1409983f4
009981BB  BB 00 10 00 00                  mov ebx, 0x1000
009981C0  41 B8 49 6F 20 20               mov r8d, 0x20206f49
009981C6  8B D3                           mov edx, ebx
009981C8  B9 40 00 00 00                  mov ecx, 0x40
009981CD  E8 1E 9F 1E 00                  call 0x140b820f0
009981D2  4C 8B F0                        mov r14, rax
009981D5  48 85 C0                        test rax, rax
009981D8  0F 84 3D 02 00 00               je 0x14099841b
009981DE  48 8D 45 A0                     lea rax, [rbp - 0x60]
009981E2  44 8B CB                        mov r9d, ebx
009981E5  4D 8B C6                        mov r8, r14
009981E8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009981ED  8B D6                           mov edx, esi
009981EF  49 8B CF                        mov rcx, r15
009981F2  E8 B9 EB F0 FF                  call 0x1408a6db0
009981F7  8B D8                           mov ebx, eax
009981F9  33 C0                           xor eax, eax
009981FB  85 DB                           test ebx, ebx
009981FD  0F 88 B3 02 00 00               js 0x1409984b6
00998203  48 8B 75 98                     mov rsi, qword ptr [rbp - 0x68]
00998207  48 85 F6                        test rsi, rsi
0099820A  0F 85 75 01 00 00               jne 0x140998385
00998210  F6 45 80 01                     test byte ptr [rbp - 0x80], 1
00998214  0F 85 E3 02 00 00               jne 0x1409984fd
0099821A  38 44 24 50                     cmp byte ptr [rsp + 0x50], al
0099821E  0F 85 E3 02 00 00               jne 0x140998507
00998224  49 8B D6                        mov rdx, r14
00998227  48 8D 0D 62 B1 67 FF            lea rcx, [rip - 0x984e9e]
0099822E  E8 01 66 8D FF                  call 0x14026e834
00998233  48 8B CF                        mov rcx, rdi
00998236  E8 BD 04 B1 FF                  call 0x1404a86f8
0099823B  49 8B D6                        mov rdx, r14
0099823E  48 8B CF                        mov rcx, rdi
00998241  E8 AE E8 FF FF                  call 0x140996af4
00998246  8B D8                           mov ebx, eax
00998248  85 C0                           test eax, eax
0099824A  0F 89 8A 01 00 00               jns 0x1409983da
00998250  44 8B C3                        mov r8d, ebx
00998253  48 8D 0D 26 B1 67 FF            lea rcx, [rip - 0x984eda]
0099825A  49 8B D6                        mov rdx, r14
0099825D  E8 F6 1C B1 FF                  call 0x1404a9f58
00998262  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00998266  4C 8D 15 23 33 90 FF            lea r10, [rip - 0x6fccdd]
0099826D  45 33 C9                        xor r9d, r9d
00998270  BE 65 03 00 C0                  mov esi, 0xc0000365
00998275  85 DB                           test ebx, ebx
00998277  41 8B D1                        mov edx, r9d
0099827A  45 8B C1                        mov r8d, r9d
0099827D  41 8B C9                        mov ecx, r9d
00998280  89 18                           mov dword ptr [rax], ebx
00998282  0F 48 DE                        cmovs ebx, esi
00998285  41 8B C1                        mov eax, r9d
00998288  4C 39 4C C7 70                  cmp qword ptr [rdi + rax*8 + 0x70], r9
0099828D  0F 84 7E 02 00 00               je 0x140998511
00998293  8D 42 01                        lea eax, [rdx + 1]
00998296  8B C8                           mov ecx, eax
00998298  8B D0                           mov edx, eax
0099829A  44 8B C0                        mov r8d, eax
0099829D  83 F8 1B                        cmp eax, 0x1b
009982A0  76 E6                           jbe 0x140998288
009982A2  33 D2                           xor edx, edx
009982A4  49 8B CE                        mov rcx, r14
009982A7  E8 C4 A5 1E 00                  call 0x140b82870
009982AC  85 DB                           test ebx, ebx
009982AE  0F 89 A6 00 00 00               jns 0x14099835a
009982B4  48 8B CF                        mov rcx, rdi
009982B7  E8 A4 75 0E 00                  call 0x140a7f860
009982BC  48 8B CF                        mov rcx, rdi
009982BF  E8 8C 10 96 FF                  call 0x1402f9350
009982C4  81 FB 0E 01 00 C0               cmp ebx, 0xc000010e
009982CA  0F 84 B2 FB FF FF               je 0x140997e82
009982D0  B9 03 00 00 00                  mov ecx, 3
009982D5  E9 AD FB FF FF                  jmp 0x140997e87
009982DA  45 33 F6                        xor r14d, r14d
009982DD  44 39 35 E0 BE 62 00            cmp dword ptr [rip + 0x62bee0], r14d
009982E4  0F 84 4A FA FF FF               je 0x140997d34
009982EA  E9 6D 48 19 00                  jmp 0x140b2cb5c
009982EF  81 FB 5E 02 00 C0               cmp ebx, 0xc000025e
009982F5  0F 84 9E FB FF FF               je 0x140997e99
009982FB  81 FB 6C 03 00 C0               cmp ebx, 0xc000036c
00998301  0F 84 92 FB FF FF               je 0x140997e99
00998307  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
0099830C  81 FB 0E 01 00 C0               cmp ebx, 0xc000010e
00998312  0F 84 81 FB FF FF               je 0x140997e99
00998318  E9 11 49 19 00                  jmp 0x140b2cc2e
0099831D  3D 23 00 00 C0                  cmp eax, 0xc0000023
00998322  0F 84 01 F9 FF FF               je 0x140997c29
00998328  BB 60 01 00 C0                  mov ebx, 0xc0000160
0099832D  E9 FE 00 00 00                  jmp 0x140998430
00998332  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00998337  E8 24 AC 10 00                  call 0x140aa2f60
0099833C  48 8B CF                        mov rcx, rdi
0099833F  E8 CC 76 8C FF                  call 0x14025fa10
00998344  33 D2                           xor edx, edx
00998346  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
0099834B  E8 48 86 0F 00                  call 0x140a90998
00998350  BE 65 03 00 C0                  mov esi, 0xc0000365
00998355  E9 6A FF FF FF                  jmp 0x1409982c4
0099835A  B2 01                           mov dl, 1
0099835C  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00998361  E8 32 86 0F 00                  call 0x140a90998
00998366  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
0099836A  E8 99 29 0B 00                  call 0x140a4ad08
0099836F  48 8B CF                        mov rcx, rdi
00998372  E8 2D E5 10 00                  call 0x140aa68a4
00998377  48 8D 4F 38                     lea rcx, [rdi + 0x38]
0099837B  E8 60 02 10 00                  call 0x140a985e0
00998380  E9 FD FA FF FF                  jmp 0x140997e82
00998385  0F B7 5D 92                     movzx ebx, word ptr [rbp - 0x6e]
00998389  41 B8 49 6F 4E 31               mov r8d, 0x314e6f49
0099838F  8B D3                           mov edx, ebx
00998391  B9 40 00 00 00                  mov ecx, 0x40
00998396  E8 55 9D 1E 00                  call 0x140b820f0
0099839B  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
0099839F  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
009983A3  33 C9                           xor ecx, ecx
009983A5  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
009983A9  48 39 48 20                     cmp qword ptr [rax + 0x20], rcx
009983AD  0F 85 22 01 00 00               jne 0x1409984d5
009983B3  33 C0                           xor eax, eax
009983B5  E9 56 FE FF FF                  jmp 0x140998210
009983BA  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
009983BF  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
009983C3  0F B7 44 24 68                  movzx eax, word ptr [rsp + 0x68]
009983C8  66 89 45 B8                     mov word ptr [rbp - 0x48], ax
009983CC  0F B7 44 24 6A                  movzx eax, word ptr [rsp + 0x6a]
009983D1  66 89 45 BA                     mov word ptr [rbp - 0x46], ax
009983D5  E9 30 F9 FF FF                  jmp 0x140997d0a
009983DA  48 8B CF                        mov rcx, rdi
009983DD  E8 B6 02 B1 FF                  call 0x1404a8698
009983E2  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
009983E7  48 8B CF                        mov rcx, rdi
009983EA  E8 0D 08 FC FF                  call 0x140958bfc
009983EF  E9 5C FE FF FF                  jmp 0x140998250
009983F4  0F B7 45 AA                     movzx eax, word ptr [rbp - 0x56]
009983F8  66 89 47 3A                     mov word ptr [rdi + 0x3a], ax
009983FC  0F B7 45 A8                     movzx eax, word ptr [rbp - 0x58]
00998400  66 89 47 38                     mov word ptr [rdi + 0x38], ax
00998404  44 0F B7 45 AA                  movzx r8d, word ptr [rbp - 0x56]
00998409  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
0099840D  48 8B 4F 40                     mov rcx, qword ptr [rdi + 0x40]
00998411  E8 2A E4 D2 FF                  call 0x1406c6840
00998416  E9 A0 FD FF FF                  jmp 0x1409981bb
0099841B  48 8B CF                        mov rcx, rdi
0099841E  E8 3D 74 0E 00                  call 0x140a7f860
00998423  48 8B CF                        mov rcx, rdi
00998426  E8 25 0F 96 FF                  call 0x1402f9350
0099842B  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00998430  BE 65 03 00 C0                  mov esi, 0xc0000365
00998435  E9 96 FE FF FF                  jmp 0x1409982d0
0099843A  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
0099843F  8B C8                           mov ecx, eax
00998441  E8 6E 2B D8 FF                  call 0x14071afb4
00998446  3C 01                           cmp al, 1
00998448  0F 85 0F FA FF FF               jne 0x140997e5d
0099844E  40 F6 DE                        neg sil
00998451  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00998456  1B DB                           sbb ebx, ebx
00998458  F7 DB                           neg ebx
0099845A  81 C3 6B 03 00 C0               add ebx, 0xc000036b
00998460  44 8B C3                        mov r8d, ebx
00998463  E8 94 37 D8 FF                  call 0x14071bbfc
00998468  E9 F0 F9 FF FF                  jmp 0x140997e5d
0099846D  48 8B CF                        mov rcx, rdi
00998470  E8 9B 75 8C FF                  call 0x14025fa10
00998475  33 D2                           xor edx, edx
00998477  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
0099847C  E8 17 85 0F 00                  call 0x140a90998
00998481  BE 65 03 00 C0                  mov esi, 0xc0000365
00998486  81 FB 34 00 00 C0               cmp ebx, 0xc0000034
0099848C  0F 85 32 FE FF FF               jne 0x1409982c4
00998492  8D 5E 29                        lea ebx, [rsi + 0x29]
00998495  E9 2A FE FF FF                  jmp 0x1409982c4
0099849A  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
0099849F  B9 1F 01 00 00                  mov ecx, 0x11f
009984A4  48 8B 55 88                     mov rdx, qword ptr [rbp - 0x78]
009984A8  4C 63 C0                        movsxd r8, eax
009984AB  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
009984B0  E8 AB 51 B6 FF                  call 0x1404fd660
009984B5  CC                              int3
009984B6  48 8B CF                        mov rcx, rdi
009984B9  E8 A2 73 0E 00                  call 0x140a7f860
009984BE  48 8B CF                        mov rcx, rdi
009984C1  E8 8A 0E 96 FF                  call 0x1402f9350
009984C6  33 D2                           xor edx, edx
009984C8  49 8B CE                        mov rcx, r14
009984CB  E8 A0 A3 1E 00                  call 0x140b82870
009984D0  E9 7B FE FF FF                  jmp 0x140998350
009984D5  66 89 58 1A                     mov word ptr [rax + 0x1a], bx
009984D9  4C 8B C3                        mov r8, rbx
009984DC  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
009984E0  48 8B D6                        mov rdx, rsi
009984E3  0F B7 45 90                     movzx eax, word ptr [rbp - 0x70]
009984E7  66 89 41 18                     mov word ptr [rcx + 0x18], ax
009984EB  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
009984EF  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
009984F3  E8 48 E3 D2 FF                  call 0x1406c6840
009984F8  E9 B6 FE FF FF                  jmp 0x1409983b3
009984FD  0F BA 6F 10 08                  bts dword ptr [rdi + 0x10], 8
00998502  E9 13 FD FF FF                  jmp 0x14099821a
00998507  0F BA 6F 10 0C                  bts dword ptr [rdi + 0x10], 0xc
0099850C  E9 13 FD FF FF                  jmp 0x140998224
00998511  8B C1                           mov eax, ecx
00998513  41 8B D0                        mov edx, r8d
00998516  4C 89 54 C7 70                  mov qword ptr [rdi + rax*8 + 0x70], r10
0099851B  E9 73 FD FF FF                  jmp 0x140998293
00998520  41 8B C6                        mov eax, r14d
00998523  E9 E4 F9 FF FF                  jmp 0x140997f0c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopLoadDriver(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int16 v_stack_m10E;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int16 v_stack_m11E;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int16 v_stack_m136;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int16 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int8 v_stack_m178;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int16 v_stack_p6A;
    unsigned __int64 v_stack_p70;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (400);
    result = (*(unsigned __int64 *)(v_rip + 4664262)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rdi = 0;
    v_stack_mE8 = a4;
    v_stack_m150 = 0;
    v_stack_mDC = 0;
    v_stack_mC4 = 0;
    v_stack_m170 = 0;
    a2 = 0;
    v_stack_m128 = 0;
    v_stack_m100 = 0;
    v_stack_m140 = 0;
    v_stack_m160 = v_xmm0;
    *(unsigned int *)(a4) = 0;
    v_stack_m138 = v_xmm1;
    v_stack_m148 = 0;
    v_stack_m110 = v_xmm0;
    v_stack_m178 = 0;
    v_stack_m120 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m160, a2, a3, a4);
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m138, a2, a3, a4);
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m110, a2, a3, a4);
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m120, a2, a3, a4);
    a4 = 0;
    a3 = 0;
    v_stack_m1A8 = v_stack_m150;
    a2 = 0;
    result = NtQueryKey(a1, a2, a3, a4);
    if (((unsigned int)(result)) != 0x80000005ULL) goto loc_0099831D;
loc_00997C29:
    result = ExAllocatePool2(64, (unsigned int)(v_stack_m150), (unsigned int)(0x654B6F49ULL), a4);
    if (result == 0) goto loc_0099842B;
    v_stack_m1A8 = v_stack_m150;
    a2 = 0;
    result = NtQueryKey(a1, a2, result, (unsigned int)(v_stack_m150));
    if (sign_flag) goto loc_00998350;
    a2 = ((unsigned int)(*(unsigned int *)(result + 12))) + (2);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x314E6F49ULL), (unsigned int)(v_stack_m150));
    v_stack_m130 = result;
    if (result == 0) goto loc_0099842B;
    a1 = (unsigned int)((2) + ((unsigned int)(*(unsigned __int16 *)(result + 12))));
    v_stack_m138 = (unsigned __int16)(*(unsigned __int16 *)(result + 12));
    v_stack_m136 = (unsigned __int16)(a1);
    result = memcpy(result, result + 16, (unsigned int)(*(unsigned int *)(result + 12)), (unsigned int)(v_stack_m150));
    a1 = 0;
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 12)))) >> (1);
    *(unsigned __int16 *)(result + result * 2) = 0;
    result = IopBuildFullDriverPath(v_stack_m138, 0, v_stack_m160, (unsigned int)(v_stack_m150));
    if (sign_flag) goto loc_00998350;
    result = wcsrchr(v_stack_m158, 92, v_stack_m160, (unsigned int)(v_stack_m150));
    if (result == 0) goto loc_009983BA;
    v_stack_m108 = result + 2;
    result = RtlInitUnicodeString(v_stack_m110, result + 2, v_stack_m160, (unsigned int)(v_stack_m150));
loc_00997D0A:
    result = HeadlessKernelAddLogEntry(1, v_stack_m110, v_stack_m160, (unsigned int)(v_stack_m150));
    result = PnpDiagnosticTraceObject(v_rip - 9980355, v_stack_m138, v_stack_m160, (unsigned int)(v_stack_m150));
    if ((unsigned __int8)((unsigned __int8)(a2)) != 0) goto loc_009982DA;
    v_r14 = 0;
loc_00997D34:
    result = IopGetDriverNameFromKeyNode(0, v_stack_m120, v_stack_m160, (unsigned int)(v_stack_m150));
    if (sign_flag) goto loc_00998350;
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rip + 4664432))));
    v_stack_mE0 = 48;
    v_stack_mD8 = 0;
    v_stack_mD0 = v_stack_m120;
    a1 = (unsigned int)((0) & (64));
    a1 = (unsigned int)((a1) + (528));
    v_stack_mC8 = (unsigned int)(a1);
    v_stack_mC0 = v_xmm0;
    result = ExAcquireResourceExclusiveLite(v_rip + 6248009, 1, v_stack_m160, (unsigned int)(v_stack_m150));
    a4 = 0;
    v_stack_m198 = v_stack_m100;
    a3 = 0;
    v_stack_m1A0 = v_stack_m170;
    a2 = 0;
    v_stack_m1A8 = 0;
    result = MmLoadSystemImageEx(v_stack_m160, a2, a3, a4);
    if (!sign_flag) goto loc_00997FE6;
    if (((unsigned int)(result)) != 0xC000010EULL) goto loc_0099843A;
    result = PsGetCurrentSilo(v_stack_m160, a2, a3, a4);
    a4 = 0;
    v_stack_m190 = v_stack_m140;
    a3 = 0;
    v_stack_m198 = result;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = 0;
    result = ObOpenObjectByNameEx(v_stack_mE0, *(unsigned __int64 *)(v_rip + 6483622), a3, a4);
    if (sign_flag) goto loc_0099846D;
    a4 = 0;
    v_stack_m1A0 = 0;
    a2 = 0;
    v_stack_m1A8 = v_stack_m170;
    v_stack_m170 = 0;
    result = ObReferenceObjectByHandle(v_stack_m140, a2, *(unsigned __int64 *)(v_rip + 6483558), a4);
    result = ZwClose(v_stack_m140, a2, *(unsigned __int64 *)(v_rip + 6483558), a4);
    if (sign_flag) goto loc_0099833C;
    result = IopResurrectDriver(v_stack_m170, a2, *(unsigned __int64 *)(v_rip + 6483558), a4);
    result = ObfDereferenceObject(v_stack_m170, a2, *(unsigned __int64 *)(v_rip + 6483558), a4);
loc_00997E5D:
    result = ExReleaseResourceLite(v_rip + 6248009, a2, *(unsigned __int64 *)(v_rip + 6483558), a4);
    result = IopBootLog(v_stack_m160, 0, *(unsigned __int64 *)(v_rip + 6483558), a4);
    if (sign_flag) goto loc_009982C4;
loc_00997E82:
loc_00997E87:
    a2 = 0;
    result = HeadlessKernelAddLogEntry(2, a2, *(unsigned __int64 *)(v_rip + 6483558), a4);
    v_r14 = 0;
    if (sign_flag) goto loc_009982EF;
loc_00997E99:
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, *(unsigned __int64 *)(v_rip + 6483558), a4);
    }
    if (v_stack_m130 == 0) goto loc_00997F8E;
    result = (unsigned __int16)((v_stack_m138) >> (1));
    v_stack_m178 = (unsigned __int16)(result);
    v_stack_mA8 = v_stack_m178;
    v_stack_m90 = (unsigned int)(v_stack_m138);
    v_stack_m88 = v_stack_m128;
    v_stack_m148 = 0;
    v_stack_m128 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_mA0 = 2;
    v_stack_m98 = v_stack_m130;
    v_stack_m8C = 0;
    v_stack_m80 = 4;
    if (v_stack_m118 == 0) goto loc_00998520;
    result = (unsigned __int16)((v_stack_m120) >> (1));
loc_00997F0C:
    v_stack_m168 = (unsigned __int16)(result);
    result = (unsigned int)(((unsigned __int16)(result)) + ((unsigned int)((unsigned __int16)(result))));
    v_stack_m68 = v_stack_m118;
    v_stack_m60 = (unsigned int)(result);
    v_stack_m58 = v_stack_m148;
    v_stack_m78 = v_stack_m168;
    v_stack_m70 = 2;
    v_stack_m5C = 0;
    v_stack_m50 = 4;
    if (*(unsigned __int64 *)(v_rip + 5039026) == 0) goto loc_00997F83;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 5039026), v_rip - 9980901, v_stack_m168, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 5038963);
        result = v_stack_mA8;
        a4 = 6;
        v_stack_m1A8 = result;
        a3 = 0;
        a2 = v_rip - 9980942;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m130, a2, a3, a4);
loc_00997F8E:
    if (v_stack_m118 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m118, a2, a3, a4);
    }
    if (v_stack_m158 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m158, a2, a3, a4);
    }
    a2 = 0;
    result = ObCloseHandle(a1, a2, a3, a4);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (400);
    return result;
loc_00997FE6:
    result = RtlImageNtHeader(v_stack_m100, a2, a3, a4);
    v_r12 = (unsigned int)((*(unsigned __int16 *)(result + 68)) << (16));
    v_r12 = (unsigned int)((v_r12) | ((unsigned int)(*(unsigned __int16 *)(result + 70))));
    v_stack_p28 = v_stack_p50;
    v_stack_p20 = v_stack_m148;
    result = PnpPrepareDriverLoading(v_stack_m138, a1, v_stack_m100, (unsigned int)((unsigned int)(v_stack_m130)));
    if (sign_flag) goto loc_00998332;
    v_stack_p48 = 0;
    a4 = 0;
    v_stack_p40 = v_stack_m128;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = 424;
    result = ObCreateObjectEx(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), *(unsigned __int64 *)(v_rip + 6482997), v_stack_mE0, a4);
    if (sign_flag) goto loc_00998332;
    a2 = 0;
    result = memset(v_stack_m128, a2, 424, a4);
    *(unsigned __int64 *)(v_stack_m128 + 48) = v_stack_m128 + 336;
    *(unsigned __int64 *)(v_stack_m128 + 336) = v_stack_m128;
loc_009980A8:
    *(unsigned __int64 *)(v_stack_m128 + 0 * 8 + 112) = v_rip - 7326482;
    if (((unsigned int)(0 + 1)) <= 27) goto loc_009980A8;
    v_stack_m128 = (unsigned int)(0 + 1);
    *(unsigned int *)(v_stack_m128) = 0x1500004ULL;
    result = RtlImageNtHeader(v_stack_m100, v_rip - 7326482, 424, a4);
    v_r12 = (unsigned int)((*(unsigned __int16 *)(result + 68)) << (16));
    result = ((unsigned int)(*(unsigned int *)(result + 40))) + (v_stack_m100);
    v_r12 = (unsigned int)((v_r12) | ((unsigned int)(*(unsigned __int16 *)(result + 70))));
    if (!(condition_is_below)) {
        a1 = 2;
    }
    *(unsigned __int64 *)(v_stack_m128 + 88) = result;
    a4 = 0;
    *(unsigned __int64 *)(v_stack_m128 + 40) = v_stack_p58;
    *(unsigned __int64 *)(v_stack_m128 + 24) = v_stack_m100;
    *(unsigned int *)(v_stack_m128 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 80)));
    a2 = 0;
    v_stack_p30 = v_stack_m140;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = ObInsertObjectEx(v_stack_m128, a2, (unsigned int)((unsigned int)(a4 + 1)), a4);
    result = ExReleaseResourceLite(v_rip + 6248009, a2, (unsigned int)((unsigned int)(a4 + 1)), a4);
    a2 = 0;
    if (sign_flag) goto loc_00998346;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p58;
    v_stack_p58 = 0;
    result = ObReferenceObjectByHandle(v_stack_m140, a2, *(unsigned __int64 *)(v_rip + 6482721), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned int)(result) != 0) goto loc_0099849A;
    result = ZwClose(v_stack_m140, a2, *(unsigned __int64 *)(v_rip + 6482721), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    *(unsigned __int64 *)(v_stack_p58 + 72) = v_rip + 6560848;
    result = ExAllocatePool2(a4 + 1 + 63, v_stack_m11E, (unsigned int)(0x314E6F49ULL), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    *(unsigned __int64 *)(v_stack_p58 + 64) = result;
    if (result != 0) goto loc_009983F4;
loc_009981BB:
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), (unsigned int)(0x20206F49ULL), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (result == 0) goto loc_0099841B;
    v_stack_p20 = v_stack_m128;
    result = NtQueryObject(a1, (unsigned int)((unsigned int)(a4 + 1)), result, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))));
    result = 0;
    if (sign_flag) goto loc_009984B6;
    if (v_stack_m130 != 0) goto loc_00998385;
loc_00998210:
    if (((v_stack_m148) & (1)) != 0) goto loc_009984FD;
loc_0099821A:
    if (v_stack_p50 != 0) goto loc_00998507;
loc_00998224:
    result = PnpDiagnosticTraceObject(v_rip - 9981598, 0, result, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))));
    result = VfDifCaptureDriverEntry(v_stack_p58, 0, result, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))));
    result = PnpCallDriverEntry(v_stack_p58, result, result, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))));
    if (!sign_flag) goto loc_009983DA;
loc_00998250:
    result = PnpDiagnosticTraceObjectWithStatus(v_rip - 9981658, result, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))));
    a4 = 0;
    *(unsigned int *)(v_stack_mE8) = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_rbx = (unsigned int)((unsigned int)(result));
    if (sign_flag) { v_rbx = (unsigned int)((unsigned int)(0xC0000365ULL)); }
loc_00998288:
    if ((*(unsigned __int64 *)(v_stack_p58 + 0 * 8 + 112)) == 0) goto loc_00998511;
loc_00998293:
    if (((unsigned int)(0 + 1)) <= 27) goto loc_00998288;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)((unsigned int)(0 + 1)), a4);
    if (!sign_flag) goto loc_0099835A;
    result = ObMakeTemporaryObject(v_stack_p58, a2, (unsigned int)((unsigned int)(0 + 1)), a4);
    result = ObfDereferenceObject(v_stack_p58, a2, (unsigned int)((unsigned int)(0 + 1)), a4);
loc_009982C4:
    if (((unsigned int)(v_rbx)) == 0xC000010EULL) goto loc_00997E82;
loc_009982D0:
    goto loc_00997E87;
loc_009982DA:
    v_r14 = 0;
    if ((*(unsigned int *)(v_rip + 6471392)) == 0) goto loc_00997D34;
loc_009982EF:
    if (((unsigned int)(v_rbx)) == 0xC000025EULL) goto loc_00997E99;
    if (((unsigned int)(v_rbx)) == 0xC000036CULL) goto loc_00997E99;
    v_stack_p58 = 0;
    if (((unsigned int)(v_rbx)) == 0xC000010EULL) goto loc_00997E99;
loc_0099831D:
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_00997C29;
    goto loc_00998430;
loc_00998332:
    result = MmUnloadSystemImage(v_stack_p58, a2, (unsigned int)((unsigned int)(0 + 1)), a4);
loc_0099833C:
    result = ExReleaseResourceLite(v_stack_p58, a2, (unsigned int)((unsigned int)(0 + 1)), a4);
    a2 = 0;
loc_00998346:
    result = IopBootLog(v_stack_p68, a2, (unsigned int)((unsigned int)(0 + 1)), a4);
loc_00998350:
    goto loc_009982C4;
loc_0099835A:
    result = IopBootLog(v_stack_p68, 1, (unsigned int)((unsigned int)(0 + 1)), a4);
    result = MmFreeDriverInitialization(*(unsigned __int64 *)(v_stack_p58 + 40), 1, (unsigned int)((unsigned int)(0 + 1)), a4);
    result = IopReadyDeviceObjects(v_stack_p58, 1, (unsigned int)((unsigned int)(0 + 1)), a4);
    result = EtwTiLogDriverObjectLoad(v_stack_p58 + 56, 1, (unsigned int)((unsigned int)(0 + 1)), a4);
    goto loc_00997E82;
loc_00998385:
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)(v_stack_m136)), (unsigned int)(0x314E6F49ULL), a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 48) + 32) = result;
    a1 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 48) + 32)) != 0) goto loc_009984D5;
loc_009983B3:
    result = 0;
    goto loc_00998210;
loc_009983BA:
    v_stack_m108 = v_stack_p70;
    v_stack_m110 = (unsigned __int16)(v_stack_p68);
    v_stack_m10E = (unsigned __int16)(v_stack_p6A);
    goto loc_00997D0A;
loc_009983DA:
    result = VfDifCaptureIoCallbacks(v_stack_p58, (unsigned int)((unsigned int)(v_stack_m136)), (unsigned int)(0x314E6F49ULL), a4);
    result = KseShimDriverIoCallbacks(v_stack_p58, (unsigned int)((unsigned int)(v_stack_m136)), v_stack_p68, a4);
    goto loc_00998250;
loc_009983F4:
    *(unsigned __int16 *)(v_stack_p58 + 58) = (unsigned __int16)(v_stack_m11E);
    *(unsigned __int16 *)(v_stack_p58 + 56) = (unsigned __int16)(v_stack_m120);
    result = memcpy(*(unsigned __int64 *)(v_stack_p58 + 64), v_stack_m118, v_stack_m11E, a4);
    goto loc_009981BB;
loc_0099841B:
    result = ObMakeTemporaryObject(v_stack_p58, v_stack_m118, v_stack_m11E, a4);
    result = ObfDereferenceObject(v_stack_p58, v_stack_m118, v_stack_m11E, a4);
loc_0099842B:
loc_00998430:
    goto loc_009982D0;
loc_0099843A:
    result = IopCheckIfNotNativeDriver((unsigned int)((unsigned int)(result)), v_stack_p68, v_stack_m11E, a4);
    if (((unsigned __int8)(result)) != 1) goto loc_00997E5D;
    v_rsi = (unsigned __int8)(-((unsigned int)(0xC0000365ULL)));
    v_rbx = (unsigned int)(-((unsigned int)(0xC000009AULL)));
    v_rbx = (unsigned int)((v_rbx) + (0xC000036BULL));
    result = IopLogBlockedDriverEvent(v_stack_p68, v_stack_p68, (unsigned int)((unsigned int)(v_rbx)), a4);
    goto loc_00997E5D;
loc_0099846D:
    result = ExReleaseResourceLite(v_stack_p58, v_stack_p68, (unsigned int)((unsigned int)(v_rbx)), a4);
    a2 = 0;
    result = IopBootLog(v_stack_p68, a2, (unsigned int)((unsigned int)(v_rbx)), a4);
    if (((unsigned int)(v_rbx)) != 0xC0000034ULL) goto loc_009982C4;
    goto loc_009982C4;
loc_0099849A:
    v_stack_p20 = 0;
    result = KeBugCheckEx(287, v_stack_m140, (int)((unsigned int)(result)), v_stack_p58);
loc_009984B6:
    result = ObMakeTemporaryObject(v_stack_p58, v_stack_m140, (int)((unsigned int)(result)), v_stack_p58);
    result = ObfDereferenceObject(v_stack_p58, v_stack_m140, (int)((unsigned int)(result)), v_stack_p58);
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, (int)((unsigned int)(result)), v_stack_p58);
    goto loc_00998350;
loc_009984D5:
    *(unsigned __int16 *)(result + 26) = (unsigned __int16)((unsigned int)(0xC0000365ULL) + 41);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p58 + 48) + 24) = (unsigned __int16)(v_stack_m138);
    result = memcpy(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 48) + 32), (unsigned int)(0xC0000365ULL), (unsigned int)(0xC0000365ULL) + 41, v_stack_p58);
    goto loc_009983B3;
loc_009984FD:
    goto loc_0099821A;
loc_00998507:
    goto loc_00998224;
loc_00998511:
    *(unsigned __int64 *)(v_stack_p58 + (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 48) + 32))) * 8 + 112) = v_rip - 7326941;
    goto loc_00998293;
loc_00998520:
    goto loc_00997F0C;
}
```

## 5. (Beta) C Style

```c
int64_t IopLoadDriver(int64_t Arg1, int32_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint16_t v_stack_m10E;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint16_t v_stack_m11E;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint16_t v_stack_m136;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint16_t v_stack_m168;
    uint64_t v_stack_m170;
    uint8_t v_stack_m178;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint16_t v_stack_p6A;
    uint64_t v_stack_p70;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (400);
    result = (*(uint64_t *)(v_rip + 0x472BC6)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rdi = 0;
    v_stack_mE8 = Arg4;
    v_stack_m150 = 0;
    v_stack_mDC = 0;
    v_stack_mC4 = 0;
    v_stack_m170 = 0;
    Arg2 = 0;
    v_stack_m128 = 0;
    v_stack_m100 = 0;
    v_stack_m140 = 0;
    v_stack_m160 = v_xmm0;
    *(uint32_t *)(arg4) = 0;
    v_stack_m138 = v_xmm1;
    v_stack_m148 = 0;
    v_stack_m110 = v_xmm0;
    v_stack_m178 = 0;
    v_stack_m120 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m160, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m138, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m110, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m120, Arg2, Arg3, Arg4);
    Arg4 = 0;
    Arg3 = 0;
    v_stack_m1A8 = v_stack_m150;
    Arg2 = 0;
    result = NtQueryKey(Arg1, Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) != 0x80000005ULL) goto loc_0099831D;
loc_00997C29:
    result = ExAllocatePool2(64, (uint32_t)(v_stack_m150), (uint32_t)(0x654B6F49ULL), Arg4);
    if (result == 0) goto loc_0099842B;
    v_stack_m1A8 = v_stack_m150;
    Arg2 = 0;
    result = NtQueryKey(Arg1, Arg2, result, (uint32_t)(v_stack_m150));
    if (sign_flag) goto loc_00998350;
    Arg2 = ((uint32_t)(*(uint32_t *)(result + 0xC))) + (2);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x314E6F49ULL), (uint32_t)(v_stack_m150));
    v_stack_m130 = result;
    if (result == 0) goto loc_0099842B;
    Arg1 = (uint32_t)((2) + ((uint32_t)(*(uint16_t *)(result + 0xC))));
    v_stack_m138 = (uint16_t)(*(uint16_t *)(result + 0xC));
    v_stack_m136 = (uint16_t)(Arg1);
    result = memcpy(result, result + 16, (uint32_t)(*(uint32_t *)(result + 0xC)), (uint32_t)(v_stack_m150));
    Arg1 = 0;
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(result + 0xC)))) >> (1);
    *(uint16_t *)(result + result * 2) = 0;
    result = IopBuildFullDriverPath(v_stack_m138, 0, v_stack_m160, (uint32_t)(v_stack_m150));
    if (sign_flag) goto loc_00998350;
    result = wcsrchr(v_stack_m158, 92, v_stack_m160, (uint32_t)(v_stack_m150));
    if (result == 0) goto loc_009983BA;
    v_stack_m108 = result + 2;
    result = RtlInitUnicodeString(v_stack_m110, result + 2, v_stack_m160, (uint32_t)(v_stack_m150));
loc_00997D0A:
    result = HeadlessKernelAddLogEntry(1, v_stack_m110, v_stack_m160, (uint32_t)(v_stack_m150));
    result = PnpDiagnosticTraceObject(v_rip - 9980355, v_stack_m138, v_stack_m160, (uint32_t)(v_stack_m150));
    if ((uint8_t)((uint8_t)(Arg2)) != 0) goto loc_009982DA;
    local_r14 = 0;
loc_00997D34:
    result = IopGetDriverNameFromKeyNode(0, v_stack_m120, v_stack_m160, (uint32_t)(v_stack_m150));
    if (sign_flag) goto loc_00998350;
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_rip + 0x472C70))));
    v_stack_mE0 = 48;
    v_stack_mD8 = 0;
    v_stack_mD0 = v_stack_m120;
    Arg1 = (uint32_t)((0) & (64));
    Arg1 = (uint32_t)((Arg1) + (528));
    v_stack_mC8 = (uint32_t)(Arg1);
    v_stack_mC0 = v_xmm0;
    result = ExAcquireResourceExclusiveLite(v_rip + 6248009, 1, v_stack_m160, (uint32_t)(v_stack_m150));
    Arg4 = 0;
    v_stack_m198 = v_stack_m100;
    Arg3 = 0;
    v_stack_m1A0 = v_stack_m170;
    Arg2 = 0;
    v_stack_m1A8 = 0;
    result = MmLoadSystemImageEx(v_stack_m160, Arg2, Arg3, Arg4);
    if (!sign_flag) goto loc_00997FE6;
    if (((uint32_t)(result)) != 0xC000010EULL) goto loc_0099843A;
    result = PsGetCurrentSilo(v_stack_m160, Arg2, Arg3, Arg4);
    Arg4 = 0;
    v_stack_m190 = v_stack_m140;
    Arg3 = 0;
    v_stack_m198 = result;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = 0;
    result = ObOpenObjectByNameEx(v_stack_mE0, *(uint64_t *)(v_rip + 0x62EEA6), Arg3, Arg4);
    if (sign_flag) goto loc_0099846D;
    Arg4 = 0;
    v_stack_m1A0 = 0;
    Arg2 = 0;
    v_stack_m1A8 = v_stack_m170;
    v_stack_m170 = 0;
    result = ObReferenceObjectByHandle(v_stack_m140, Arg2, *(uint64_t *)(v_rip + 0x62EE66), Arg4);
    result = ZwClose(v_stack_m140, Arg2, *(uint64_t *)(v_rip + 0x62EE66), Arg4);
    if (sign_flag) goto loc_0099833C;
    result = IopResurrectDriver(v_stack_m170, Arg2, *(uint64_t *)(v_rip + 0x62EE66), Arg4);
    result = ObfDereferenceObject(v_stack_m170, Arg2, *(uint64_t *)(v_rip + 0x62EE66), Arg4);
loc_00997E5D:
    result = ExReleaseResourceLite(v_rip + 6248009, Arg2, *(uint64_t *)(v_rip + 0x62EE66), Arg4);
    result = IopBootLog(v_stack_m160, 0, *(uint64_t *)(v_rip + 0x62EE66), Arg4);
    if (sign_flag) goto loc_009982C4;
loc_00997E82:
loc_00997E87:
    Arg2 = 0;
    result = HeadlessKernelAddLogEntry(2, Arg2, *(uint64_t *)(v_rip + 0x62EE66), Arg4);
    local_r14 = 0;
    if (sign_flag) goto loc_009982EF;
loc_00997E99:
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, *(uint64_t *)(v_rip + 0x62EE66), Arg4);
    }
    if (v_stack_m130 == 0) goto loc_00997F8E;
    result = (uint16_t)((v_stack_m138) >> (1));
    v_stack_m178 = (uint16_t)(result);
    v_stack_mA8 = v_stack_m178;
    v_stack_m90 = (uint32_t)(v_stack_m138);
    v_stack_m88 = v_stack_m128;
    v_stack_m148 = 0;
    v_stack_m128 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_mA0 = 2;
    v_stack_m98 = v_stack_m130;
    v_stack_m8C = 0;
    v_stack_m80 = 4;
    if (v_stack_m118 == 0) goto loc_00998520;
    result = (uint16_t)((v_stack_m120) >> (1));
loc_00997F0C:
    v_stack_m168 = (uint16_t)(result);
    result = (uint32_t)(((uint16_t)(result)) + ((uint32_t)((uint16_t)(result))));
    v_stack_m68 = v_stack_m118;
    v_stack_m60 = (uint32_t)(result);
    v_stack_m58 = v_stack_m148;
    v_stack_m78 = v_stack_m168;
    v_stack_m70 = 2;
    v_stack_m5C = 0;
    v_stack_m50 = 4;
    if (*(uint64_t *)(v_rip + 0x4CE3B2) == 0) goto loc_00997F83;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x4CE3B2), v_rip - 9980901, v_stack_m168, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x4CE373);
        result = v_stack_mA8;
        Arg4 = 6;
        v_stack_m1A8 = result;
        Arg3 = 0;
        Arg2 = v_rip - 9980942;
        result = EtwWrite(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m130, Arg2, Arg3, Arg4);
loc_00997F8E:
    if (v_stack_m118 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m118, Arg2, Arg3, Arg4);
    }
    if (v_stack_m158 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m158, Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    result = ObCloseHandle(Arg1, Arg2, Arg3, Arg4);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (400);
    return result;
loc_00997FE6:
    result = RtlImageNtHeader(v_stack_m100, Arg2, Arg3, Arg4);
    local_r12 = (uint32_t)((*(uint16_t *)(result + 0x44)) << (16));
    local_r12 = (uint32_t)((local_r12) | ((uint32_t)(*(uint16_t *)(result + 0x46))));
    v_stack_p28 = v_stack_p50;
    v_stack_p20 = v_stack_m148;
    result = PnpPrepareDriverLoading(v_stack_m138, Arg1, v_stack_m100, (uint32_t)((uint32_t)(v_stack_m130)));
    if (sign_flag) goto loc_00998332;
    v_stack_p48 = 0;
    Arg4 = 0;
    v_stack_p40 = v_stack_m128;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p28 = 424;
    result = ObCreateObjectEx(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), *(uint64_t *)(v_rip + 0x62EC35), v_stack_mE0, Arg4);
    if (sign_flag) goto loc_00998332;
    Arg2 = 0;
    result = memset(v_stack_m128, Arg2, 424, Arg4);
    *(uint64_t *)(v_stack_m128 + 0x30) = v_stack_m128 + 336;
    *(uint64_t *)(v_stack_m128 + 0x150) = v_stack_m128;
loc_009980A8:
    *(uint64_t *)(v_stack_m128 + 0x0 * 8 + 0x70) = v_rip - 7326482;
    if (((uint32_t)(0 + 1)) <= 27) goto loc_009980A8;
    v_stack_m128 = (uint32_t)(0 + 1);
    *(uint32_t *)(v_stack_m128) = 0x1500004ULL;
    result = RtlImageNtHeader(v_stack_m100, v_rip - 7326482, 424, Arg4);
    local_r12 = (uint32_t)((*(uint16_t *)(result + 0x44)) << (16));
    result = ((uint32_t)(*(uint32_t *)(result + 0x28))) + (v_stack_m100);
    local_r12 = (uint32_t)((local_r12) | ((uint32_t)(*(uint16_t *)(result + 0x46))));
    if (!(condition_is_below)) {
        Arg1 = 2;
    }
    *(uint64_t *)(v_stack_m128 + 0x58) = result;
    Arg4 = 0;
    *(uint64_t *)(v_stack_m128 + 0x28) = v_stack_p58;
    *(uint64_t *)(v_stack_m128 + 0x18) = v_stack_m100;
    *(uint32_t *)(v_stack_m128 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x50)));
    Arg2 = 0;
    v_stack_p30 = v_stack_m140;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = ObInsertObjectEx(v_stack_m128, Arg2, (uint32_t)((uint32_t)(Arg4 + 1)), Arg4);
    result = ExReleaseResourceLite(v_rip + 6248009, Arg2, (uint32_t)((uint32_t)(Arg4 + 1)), Arg4);
    Arg2 = 0;
    if (sign_flag) goto loc_00998346;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p58;
    v_stack_p58 = 0;
    result = ObReferenceObjectByHandle(v_stack_m140, Arg2, *(uint64_t *)(v_rip + 0x62EB21), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint32_t)(result) != 0) goto loc_0099849A;
    result = ZwClose(v_stack_m140, Arg2, *(uint64_t *)(v_rip + 0x62EB21), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    *(uint64_t *)(v_stack_p58 + 0x48) = v_rip + 6560848;
    result = ExAllocatePool2(Arg4 + 1 + 63, v_stack_m11E, (uint32_t)(0x314E6F49ULL), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    *(uint64_t *)(v_stack_p58 + 0x40) = result;
    if (result != 0) goto loc_009983F4;
loc_009981BB:
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), (uint32_t)(0x20206F49ULL), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (result == 0) goto loc_0099841B;
    v_stack_p20 = v_stack_m128;
    result = NtQueryObject(Arg1, (uint32_t)((uint32_t)(Arg4 + 1)), result, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))));
    result = 0;
    if (sign_flag) goto loc_009984B6;
    if (v_stack_m130 != 0) goto loc_00998385;
loc_00998210:
    if (((v_stack_m148) & (1)) != 0) goto loc_009984FD;
loc_0099821A:
    if (v_stack_p50 != 0) goto loc_00998507;
loc_00998224:
    result = PnpDiagnosticTraceObject(v_rip - 9981598, 0, result, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))));
    result = VfDifCaptureDriverEntry(v_stack_p58, 0, result, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))));
    result = PnpCallDriverEntry(v_stack_p58, result, result, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))));
    if (!sign_flag) goto loc_009983DA;
loc_00998250:
    result = PnpDiagnosticTraceObjectWithStatus(v_rip - 9981658, result, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))));
    Arg4 = 0;
    *(uint32_t *)(v_stack_mE8) = (uint32_t)((uint32_t)((uint32_t)(result)));
    local_rbx = (uint32_t)((uint32_t)(result));
    if (sign_flag) { local_rbx = (uint32_t)((uint32_t)(0xC0000365ULL)); }
loc_00998288:
    if ((*(uint64_t *)(v_stack_p58 + 0x0 * 8 + 0x70)) == 0) goto loc_00998511;
loc_00998293:
    if (((uint32_t)(0 + 1)) <= 27) goto loc_00998288;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)((uint32_t)(0 + 1)), Arg4);
    if (!sign_flag) goto loc_0099835A;
    result = ObMakeTemporaryObject(v_stack_p58, Arg2, (uint32_t)((uint32_t)(0 + 1)), Arg4);
    result = ObfDereferenceObject(v_stack_p58, Arg2, (uint32_t)((uint32_t)(0 + 1)), Arg4);
loc_009982C4:
    if (((uint32_t)(local_rbx)) == 0xC000010EULL) goto loc_00997E82;
loc_009982D0:
    goto loc_00997E87;
loc_009982DA:
    local_r14 = 0;
    if ((*(uint32_t *)(v_rip + 0x62BEE0)) == 0) goto loc_00997D34;
loc_009982EF:
    if (((uint32_t)(local_rbx)) == 0xC000025EULL) goto loc_00997E99;
    if (((uint32_t)(local_rbx)) == 0xC000036CULL) goto loc_00997E99;
    v_stack_p58 = 0;
    if (((uint32_t)(local_rbx)) == 0xC000010EULL) goto loc_00997E99;
loc_0099831D:
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_00997C29;
    goto loc_00998430;
loc_00998332:
    result = MmUnloadSystemImage(v_stack_p58, Arg2, (uint32_t)((uint32_t)(0 + 1)), Arg4);
loc_0099833C:
    result = ExReleaseResourceLite(v_stack_p58, Arg2, (uint32_t)((uint32_t)(0 + 1)), Arg4);
    Arg2 = 0;
loc_00998346:
    result = IopBootLog(v_stack_p68, Arg2, (uint32_t)((uint32_t)(0 + 1)), Arg4);
loc_00998350:
    goto loc_009982C4;
loc_0099835A:
    result = IopBootLog(v_stack_p68, 1, (uint32_t)((uint32_t)(0 + 1)), Arg4);
    result = MmFreeDriverInitialization(*(uint64_t *)(v_stack_p58 + 0x28), 1, (uint32_t)((uint32_t)(0 + 1)), Arg4);
    result = IopReadyDeviceObjects(v_stack_p58, 1, (uint32_t)((uint32_t)(0 + 1)), Arg4);
    result = EtwTiLogDriverObjectLoad(v_stack_p58 + 56, 1, (uint32_t)((uint32_t)(0 + 1)), Arg4);
    goto loc_00997E82;
loc_00998385:
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)(v_stack_m136)), (uint32_t)(0x314E6F49ULL), Arg4);
    *(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x30) + 0x20) = result;
    Arg1 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x30) + 0x20)) != 0) goto loc_009984D5;
loc_009983B3:
    result = 0;
    goto loc_00998210;
loc_009983BA:
    v_stack_m108 = v_stack_p70;
    v_stack_m110 = (uint16_t)(v_stack_p68);
    v_stack_m10E = (uint16_t)(v_stack_p6A);
    goto loc_00997D0A;
loc_009983DA:
    result = VfDifCaptureIoCallbacks(v_stack_p58, (uint32_t)((uint32_t)(v_stack_m136)), (uint32_t)(0x314E6F49ULL), Arg4);
    result = KseShimDriverIoCallbacks(v_stack_p58, (uint32_t)((uint32_t)(v_stack_m136)), v_stack_p68, Arg4);
    goto loc_00998250;
loc_009983F4:
    *(uint16_t *)(v_stack_p58 + 0x3A) = (uint16_t)(v_stack_m11E);
    *(uint16_t *)(v_stack_p58 + 0x38) = (uint16_t)(v_stack_m120);
    result = memcpy(*(uint64_t *)(v_stack_p58 + 0x40), v_stack_m118, v_stack_m11E, Arg4);
    goto loc_009981BB;
loc_0099841B:
    result = ObMakeTemporaryObject(v_stack_p58, v_stack_m118, v_stack_m11E, Arg4);
    result = ObfDereferenceObject(v_stack_p58, v_stack_m118, v_stack_m11E, Arg4);
loc_0099842B:
loc_00998430:
    goto loc_009982D0;
loc_0099843A:
    result = IopCheckIfNotNativeDriver((uint32_t)((uint32_t)(result)), v_stack_p68, v_stack_m11E, Arg4);
    if (((uint8_t)(result)) != 1) goto loc_00997E5D;
    local_rsi = (uint8_t)(-((uint32_t)(0xC0000365ULL)));
    local_rbx = (uint32_t)(-((uint32_t)(0xC000009AULL)));
    local_rbx = (uint32_t)((local_rbx) + (0xC000036BULL));
    result = IopLogBlockedDriverEvent(v_stack_p68, v_stack_p68, (uint32_t)((uint32_t)(local_rbx)), Arg4);
    goto loc_00997E5D;
loc_0099846D:
    result = ExReleaseResourceLite(v_stack_p58, v_stack_p68, (uint32_t)((uint32_t)(local_rbx)), Arg4);
    Arg2 = 0;
    result = IopBootLog(v_stack_p68, Arg2, (uint32_t)((uint32_t)(local_rbx)), Arg4);
    if (((uint32_t)(local_rbx)) != 0xC0000034ULL) goto loc_009982C4;
    goto loc_009982C4;
loc_0099849A:
    v_stack_p20 = 0;
    result = KeBugCheckEx(287, v_stack_m140, (int32_t)((uint32_t)(result)), v_stack_p58);
loc_009984B6:
    result = ObMakeTemporaryObject(v_stack_p58, v_stack_m140, (int32_t)((uint32_t)(result)), v_stack_p58);
    result = ObfDereferenceObject(v_stack_p58, v_stack_m140, (int32_t)((uint32_t)(result)), v_stack_p58);
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, (int32_t)((uint32_t)(result)), v_stack_p58);
    goto loc_00998350;
loc_009984D5:
    *(uint16_t *)(result + 0x1A) = (uint16_t)((uint32_t)(0xC0000365ULL) + 41);
    *(uint16_t *)(*(uint64_t *)(v_stack_p58 + 0x30) + 0x18) = (uint16_t)(v_stack_m138);
    result = memcpy(*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x30) + 0x20), (uint32_t)(0xC0000365ULL), (uint32_t)(0xC0000365ULL) + 41, v_stack_p58);
    goto loc_009983B3;
loc_009984FD:
    goto loc_0099821A;
loc_00998507:
    goto loc_00998224;
loc_00998511:
    *(uint64_t *)(v_stack_p58 + (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x30) + 0x20))) * 8 + 0x70) = v_rip - 7326941;
    goto loc_00998293;
loc_00998520:
    goto loc_00997F0C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00997B54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
