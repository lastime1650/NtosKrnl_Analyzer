# MiApplyImageHotPatchRequest

- RVA: `0x008025AC`–`0x00802F8F` (길이 `2,531` bytes)
- VA: `0x00000001408025AC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D8468`
- 디코드: `632`개 명령, `2,531/2,531` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **62**; 고유 호출 대상: **42**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008025E0` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008025EE` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008025FD` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00802637` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0080264A` → [MiInitializeImageHotPatchContext](../AD/MiInitializeImageHotPatchContext_function_00ADA2DC.md) (function, `0x00ADA2DC`)
- `0x00802658` → [MiInitializeImageHotPatchContext](../AD/MiInitializeImageHotPatchContext_function_00ADA2DC.md) (function, `0x00ADA2DC`)
- `0x008026CB` → [Feature_Servicing_HotpatchLoaderFixes__private_IsEnabledDeviceUsageNoInline](../../text/68/Feature_Servicing_HotpatchLoaderFixes__private_IsEnabledDeviceUsageNoInline_function_00682F3C.md) (function, `0x00682F3C`)
- `0x008026D7` → [PsWow64GetProcessNtdllType](../8C/PsWow64GetProcessNtdllType_function_008CE464.md) (function, `0x008CE464`)
- `0x008026F2` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00802718` → [MiGetVadForHotPatchInProgress](MiGetVadForHotPatchInProgress_function_008039C4.md) (function, `0x008039C4`)
- `0x00802761` → [MiLocateLockedVadEvent](../../text/2A/MiLocateLockedVadEvent_function_002A7A0C.md) (function, `0x002A7A0C`)
- `0x0080277B` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x008027A9` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x008027BC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008027D0` → [MiInsertVadEvent](../../text/43/MiInsertVadEvent_function_00430E74.md) (function, `0x00430E74`)
- `0x00802842` → [MiUnlockVad](../../text/2A/MiUnlockVad_function_002A59C8.md) (function, `0x002A59C8`)
- `0x00802859` → [MiGetVadForHotPatchInProgress](MiGetVadForHotPatchInProgress_function_008039C4.md) (function, `0x008039C4`)
- `0x0080289B` → [MiUnlockVad](../../text/2A/MiUnlockVad_function_002A59C8.md) (function, `0x002A59C8`)
- `0x008028CC` → [MiReferenceMappedControlArea](../../text/67/MiReferenceMappedControlArea_function_00678F50.md) (function, `0x00678F50`)
- `0x008028D8` → [MiUnlockVad](../../text/2A/MiUnlockVad_function_002A59C8.md) (function, `0x002A59C8`)
- `0x008028ED` → [SeCompareSigningLevels](../A1/SeCompareSigningLevels_function_00A13760.md) (function, `0x00A13760`)
- `0x00802912` → [MiGetAllRegisteredPatches](MiGetAllRegisteredPatches_function_0080367C.md) (function, `0x0080367C`)
- `0x0080295F` → [MiOpenHotPatchFile](../AB/MiOpenHotPatchFile_function_00AB5684.md) (function, `0x00AB5684`)
- `0x0080296F` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (function, `0x00294CB0`)
- `0x0080297D` → [MiUnmapImageInSystemSpace](../94/MiUnmapImageInSystemSpace_function_0094206C.md) (function, `0x0094206C`)
- `0x0080298F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0080299F` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x008029E7` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00802A02` → [MiLogHotPatchOperationStatus](MiLogHotPatchOperationStatus_function_00804E84.md) (function, `0x00804E84`)
- `0x00802A1B` → [MiLockVad](../../text/29/MiLockVad_function_00295810.md) (function, `0x00295810`)
- `0x00802A29` → [MiSetVadFlags](../../text/43/MiSetVadFlags_function_004311FC.md) (function, `0x004311FC`)
- `0x00802A4A` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x00802A5E` → [MiLockVad](../../text/29/MiLockVad_function_00295810.md) (function, `0x00295810`)
- `0x00802A6C` → [MiSetVadFlags](../../text/43/MiSetVadFlags_function_004311FC.md) (function, `0x004311FC`)
- `0x00802A74` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x00802A81` → [MiDeleteHotPatchEntry](MiDeleteHotPatchEntry_function_008033C0.md) (function, `0x008033C0`)
- `0x00802A8D` → [MiReleaseHotPatchResources](../AC/MiReleaseHotPatchResources_function_00ACCD60.md) (function, `0x00ACCD60`)
- `0x00802A96` → [MiReleaseHotPatchResources](../AC/MiReleaseHotPatchResources_function_00ACCD60.md) (function, `0x00ACCD60`)
- `0x00802AB0` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00802AC0` → [MiUnmapImageInSystemSpace](../94/MiUnmapImageInSystemSpace_function_0094206C.md) (function, `0x0094206C`)
- `0x00802AD3` → [MiDereferenceControlAreaBySection](../../text/45/MiDereferenceControlAreaBySection_function_00458348.md) (function, `0x00458348`)
- `0x00802AE9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00802AF9` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00802B0C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00802B27` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00802B31` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00802B3F` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00802B68` → [MiDereferenceControlAreaBySection](../../text/45/MiDereferenceControlAreaBySection_function_00458348.md) (function, `0x00458348`)
- `0x00802B80` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00802BD8` → [MiCaptureHotPatchInfo](MiCaptureHotPatchInfo_function_00802F98.md) (function, `0x00802F98`)
- `0x00802C91` → [MiGetProcessHotPatchContext](MiGetProcessHotPatchContext_function_00803948.md) (function, `0x00803948`)
- `0x00802CD7` → [MiPrepareToHotPatchVad](MiPrepareToHotPatchVad_function_00806E70.md) (function, `0x00806E70`)
- `0x00802D16` → [MiPrepareToHotPatchVad](MiPrepareToHotPatchVad_function_00806E70.md) (function, `0x00806E70`)
- `0x00802D3D` → [MiProcessPatchImageCfg](MiProcessPatchImageCfg_function_00806F9C.md) (function, `0x00806F9C`)
- `0x00802E16` → [RtlApplyHotPatch](../../pagelk/B7/RtlApplyHotPatch_function_00B7528C.md) (function, `0x00B7528C`)
- `0x00802E52` → [MiApplyImageHotPatch](MiApplyImageHotPatch_function_00802330.md) (function, `0x00802330`)
- `0x00802E79` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00802E96` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00802EEB` → [MiLogHotPatchOperation](MiLogHotPatchOperation_function_00804A04.md) (function, `0x00804A04`)
- `0x00802F4F` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00802F58` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00802F79` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)

### Direct callers
- [NtManageHotPatch](../AF/NtManageHotPatch_function_00AF8660.md) at `0x00AF8B5C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **37**
  - `0x008025E0` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008025EE` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008025FD` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00802637` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x008026CB` → [Feature_Servicing_HotpatchLoaderFixes__private_IsEnabledDeviceUsageNoInline](../../text/68/Feature_Servicing_HotpatchLoaderFixes__private_IsEnabledDeviceUsageNoInline_function_00682F3C.md) (`PAGE` → `.text`)
  - `0x008026F2` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00802761` → [MiLocateLockedVadEvent](../../text/2A/MiLocateLockedVadEvent_function_002A7A0C.md) (`PAGE` → `.text`)
  - `0x0080277B` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x008027A9` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x008027BC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008027D0` → [MiInsertVadEvent](../../text/43/MiInsertVadEvent_function_00430E74.md) (`PAGE` → `.text`)
  - `0x00802842` → [MiUnlockVad](../../text/2A/MiUnlockVad_function_002A59C8.md) (`PAGE` → `.text`)
  - `0x0080289B` → [MiUnlockVad](../../text/2A/MiUnlockVad_function_002A59C8.md) (`PAGE` → `.text`)
  - `0x008028CC` → [MiReferenceMappedControlArea](../../text/67/MiReferenceMappedControlArea_function_00678F50.md) (`PAGE` → `.text`)
  - `0x008028D8` → [MiUnlockVad](../../text/2A/MiUnlockVad_function_002A59C8.md) (`PAGE` → `.text`)
  - `0x0080296F` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (`PAGE` → `.text`)
  - `0x0080298F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008029E7` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00802A1B` → [MiLockVad](../../text/29/MiLockVad_function_00295810.md) (`PAGE` → `.text`)
  - `0x00802A29` → [MiSetVadFlags](../../text/43/MiSetVadFlags_function_004311FC.md) (`PAGE` → `.text`)
  - `0x00802A4A` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (`PAGE` → `.text`)
  - `0x00802A5E` → [MiLockVad](../../text/29/MiLockVad_function_00295810.md) (`PAGE` → `.text`)
  - `0x00802A6C` → [MiSetVadFlags](../../text/43/MiSetVadFlags_function_004311FC.md) (`PAGE` → `.text`)
  - `0x00802A74` → [MiUnlockAndDereferenceVad](../../text/31/MiUnlockAndDereferenceVad_function_00316E60.md) (`PAGE` → `.text`)
  - `0x00802AB0` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00802AD3` → [MiDereferenceControlAreaBySection](../../text/45/MiDereferenceControlAreaBySection_function_00458348.md) (`PAGE` → `.text`)
  - `0x00802AE9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00802B0C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00802B31` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00802B68` → [MiDereferenceControlAreaBySection](../../text/45/MiDereferenceControlAreaBySection_function_00458348.md) (`PAGE` → `.text`)
  - `0x00802B80` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00802E16` → [RtlApplyHotPatch](../../pagelk/B7/RtlApplyHotPatch_function_00B7528C.md) (`PAGE` → `PAGELK`)
  - `0x00802E79` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00802E96` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00802F4F` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00802F58` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00802F79` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008025AC  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
008025B1  55                              push rbp
008025B2  53                              push rbx
008025B3  56                              push rsi
008025B4  57                              push rdi
008025B5  41 54                           push r12
008025B7  41 55                           push r13
008025B9  41 56                           push r14
008025BB  41 57                           push r15
008025BD  48 8D AC 24 48 FE FF FF         lea rbp, [rsp - 0x1b8]
008025C5  48 81 EC 28 03 00 00            sub rsp, 0x328
008025CC  4C 8B E1                        mov r12, rcx
008025CF  BB A0 00 00 00                  mov ebx, 0xa0
008025D4  44 8B C3                        mov r8d, ebx
008025D7  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
008025DE  33 D2                           xor edx, edx
008025E0  E8 5B 46 EC FF                  call 0x1406c6c40
008025E5  44 8B C3                        mov r8d, ebx
008025E8  48 8D 4D 70                     lea rcx, [rbp + 0x70]
008025EC  33 D2                           xor edx, edx
008025EE  E8 4D 46 EC FF                  call 0x1406c6c40
008025F3  33 D2                           xor edx, edx
008025F5  44 8D 43 B0                     lea r8d, [rbx - 0x50]
008025F9  48 8D 4D 20                     lea rcx, [rbp + 0x20]
008025FD  E8 3E 46 EC FF                  call 0x1406c6c40
00802602  48 83 65 C8 00                  and qword ptr [rbp - 0x38], 0
00802607  48 8D 4D 00                     lea rcx, [rbp]
0080260B  48 83 65 90 00                  and qword ptr [rbp - 0x70], 0
00802610  45 33 F6                        xor r14d, r14d
00802613  48 83 65 B0 00                  and qword ptr [rbp - 0x50], 0
00802618  0F 57 C0                        xorps xmm0, xmm0
0080261B  48 83 65 B8 00                  and qword ptr [rbp - 0x48], 0
00802620  33 D2                           xor edx, edx
00802622  48 83 65 98 00                  and qword ptr [rbp - 0x68], 0
00802627  4C 21 75 D0                     and qword ptr [rbp - 0x30], r14
0080262B  4C 21 75 D8                     and qword ptr [rbp - 0x28], r14
0080262F  4C 21 75 C0                     and qword ptr [rbp - 0x40], r14
00802633  0F 11 45 00                     movups xmmword ptr [rbp], xmm0
00802637  E8 44 81 C2 FF                  call 0x14042a780
0080263C  33 D2                           xor edx, edx
0080263E  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00802645  45 33 C0                        xor r8d, r8d
00802648  33 FF                           xor edi, edi
0080264A  E8 8D 7C 2D 00                  call 0x140ada2dc
0080264F  33 D2                           xor edx, edx
00802651  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00802655  45 33 C0                        xor r8d, r8d
00802658  E8 7F 7C 2D 00                  call 0x140ada2dc
0080265D  65 4C 8B 2C 25 88 01 00 00      mov r13, qword ptr gs:[0x188]
00802666  45 8D 7E 01                     lea r15d, [r14 + 1]
0080266A  48 21 7D A8                     and qword ptr [rbp - 0x58], rdi
0080266E  21 7D A0                        and dword ptr [rbp - 0x60], edi
00802671  21 7D 88                        and dword ptr [rbp - 0x78], edi
00802674  41 83 3C 24 02                  cmp dword ptr [r12], 2
00802679  49 8B B5 B8 00 00 00            mov rsi, qword ptr [r13 + 0xb8]
00802680  4C 89 6D 80                     mov qword ptr [rbp - 0x80], r13
00802684  48 89 75 F0                     mov qword ptr [rbp - 0x10], rsi
00802688  0F B7 86 EC 06 00 00            movzx eax, word ptr [rsi + 0x6ec]
0080268F  66 89 85 10 02 00 00            mov word ptr [rbp + 0x210], ax
00802696  75 29                           jne 0x1408026c1
00802698  48 83 CB FF                     or rbx, 0xffffffffffffffff
0080269C  49 39 5C 24 08                  cmp qword ptr [r12 + 8], rbx
008026A1  75 1E                           jne 0x1408026c1
008026A3  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
008026A8  A9 FC FF FF 7F                  test eax, 0x7ffffffc
008026AD  75 12                           jne 0x1408026c1
008026AF  A8 03                           test al, 3
008026B1  74 0E                           je 0x1408026c1
008026B3  49 39 7C 24 18                  cmp qword ptr [r12 + 0x18], rdi
008026B8  74 07                           je 0x1408026c1
008026BA  49 39 7C 24 10                  cmp qword ptr [r12 + 0x10], rdi
008026BF  75 0A                           jne 0x1408026cb
008026C1  BE 0D 00 00 C0                  mov esi, 0xc000000d
008026C6  E9 25 03 00 00                  jmp 0x1408029f0
008026CB  E8 6C 08 E8 FF                  call 0x140682f3c
008026D0  85 C0                           test eax, eax
008026D2  74 17                           je 0x1408026eb
008026D4  48 8B CE                        mov rcx, rsi
008026D7  E8 88 BD 0C 00                  call 0x1408ce464
008026DC  83 F8 02                        cmp eax, 2
008026DF  75 0A                           jne 0x1408026eb
008026E1  BE BB 00 00 C0                  mov esi, 0xc00000bb
008026E6  E9 05 03 00 00                  jmp 0x1408029f0
008026EB  48 8D 8E E8 01 00 00            lea rcx, [rsi + 0x1e8]
008026F2  E8 29 3F A1 FF                  call 0x140216620
008026F7  40 8A F8                        mov dil, al
008026FA  41 23 FF                        and edi, r15d
008026FD  75 0A                           jne 0x140802709
008026FF  BE 0A 01 00 C0                  mov esi, 0xc000010a
00802704  E9 D8 02 00 00                  jmp 0x1408029e1
00802709  49 8B 4C 24 10                  mov rcx, qword ptr [r12 + 0x10]
0080270E  4C 8D 4D A0                     lea r9, [rbp - 0x60]
00802712  4C 8D 45 90                     lea r8, [rbp - 0x70]
00802716  33 D2                           xor edx, edx
00802718  E8 A7 12 00 00                  call 0x1408039c4
0080271D  8B F0                           mov esi, eax
0080271F  85 C0                           test eax, eax
00802721  0F 88 BA 02 00 00               js 0x1408029e1
00802727  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0080272B  BA 00 02 00 00                  mov edx, 0x200
00802730  49 8B 47 48                     mov rax, qword ptr [r15 + 0x48]
00802734  48 8B 08                        mov rcx, qword ptr [rax]
00802737  4C 8B 01                        mov r8, qword ptr [rcx]
0080273A  4C 89 85 18 02 00 00            mov qword ptr [rbp + 0x218], r8
00802741  49 8B 48 38                     mov rcx, qword ptr [r8 + 0x38]
00802745  8B 41 3C                        mov eax, dword ptr [rcx + 0x3c]
00802748  89 45 A8                        mov dword ptr [rbp - 0x58], eax
0080274B  8B 41 48                        mov eax, dword ptr [rcx + 0x48]
0080274E  89 45 AC                        mov dword ptr [rbp - 0x54], eax
00802751  41 8A 40 0F                     mov al, byte ptr [r8 + 0xf]
00802755  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00802759  24 0F                           and al, 0xf
0080275B  88 85 08 02 00 00               mov byte ptr [rbp + 0x208], al
00802761  E8 A6 52 AA FF                  call 0x1402a7a0c
00802766  48 85 C0                        test rax, rax
00802769  0F 85 82 00 00 00               jne 0x1408027f1
0080276F  8D 50 58                        lea edx, [rax + 0x58]
00802772  41 B8 4D 69 48 62               mov r8d, 0x6248694d
00802778  8D 48 40                        lea ecx, [rax + 0x40]
0080277B  E8 C0 8D B5 FF                  call 0x14035b540
00802780  48 8B F0                        mov rsi, rax
00802783  48 85 C0                        test rax, rax
00802786  75 0A                           jne 0x140802792
00802788  BE 9A 00 00 C0                  mov esi, 0xc000009a
0080278D  E9 FA 00 00 00                  jmp 0x14080288c
00802792  BA 48 00 00 00                  mov edx, 0x48
00802797  C7 40 50 00 02 00 00            mov dword ptr [rax + 0x50], 0x200
0080279E  B9 00 01 00 00                  mov ecx, 0x100
008027A3  41 B8 48 50 45 4E               mov r8d, 0x4e455048
008027A9  E8 92 8D B5 FF                  call 0x14035b540
008027AE  48 89 46 08                     mov qword ptr [rsi + 8], rax
008027B2  48 85 C0                        test rax, rax
008027B5  75 0C                           jne 0x1408027c3
008027B7  33 D2                           xor edx, edx
008027B9  48 8B CE                        mov rcx, rsi
008027BC  E8 AF 00 38 00                  call 0x140b82870
008027C1  EB C5                           jmp 0x140802788
008027C3  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
008027C7  41 B8 01 00 00 00               mov r8d, 1
008027CD  48 8B D6                        mov rdx, rsi
008027D0  E8 9F E6 C2 FF                  call 0x140430e74
008027D5  4C 8B 76 08                     mov r14, qword ptr [rsi + 8]
008027D9  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
008027DD  4C 8B 85 18 02 00 00            mov r8, qword ptr [rbp + 0x218]
008027E4  C7 45 A0 02 00 00 00            mov dword ptr [rbp - 0x60], 2
008027EB  49 89 46 20                     mov qword ptr [r14 + 0x20], rax
008027EF  EB 04                           jmp 0x1408027f5
008027F1  4C 8B 70 08                     mov r14, qword ptr [rax + 8]
008027F5  41 83 4E 44 01                  or dword ptr [r14 + 0x44], 1
008027FA  48 8B C3                        mov rax, rbx
008027FD  F0 49 0F B1 58 18               lock cmpxchg qword ptr [r8 + 0x18], rbx
00802803  49 8B 48 38                     mov rcx, qword ptr [r8 + 0x38]
00802807  BA 4C 01 00 00                  mov edx, 0x14c
0080280C  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00802810  0F B7 41 30                     movzx eax, word ptr [rcx + 0x30]
00802814  B9 64 86 00 00                  mov ecx, 0x8664
00802819  66 89 85 18 02 00 00            mov word ptr [rbp + 0x218], ax
00802820  66 3B C1                        cmp ax, cx
00802823  74 16                           je 0x14080283b
00802825  66 3B C2                        cmp ax, dx
00802828  74 11                           je 0x14080283b
0080282A  B9 64 AA 00 00                  mov ecx, 0xaa64
0080282F  66 3B C1                        cmp ax, cx
00802832  74 07                           je 0x14080283b
00802834  BE 7B 00 00 C0                  mov esi, 0xc000007b
00802839  EB 51                           jmp 0x14080288c
0080283B  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
0080283F  49 8B CD                        mov rcx, r13
00802842  E8 81 31 AA FF                  call 0x1402a59c8
00802847  49 8B 4C 24 18                  mov rcx, qword ptr [r12 + 0x18]
0080284C  4C 8D 4D 88                     lea r9, [rbp - 0x78]
00802850  4C 8D 45 B0                     lea r8, [rbp - 0x50]
00802854  BA 01 00 00 00                  mov edx, 1
00802859  E8 66 11 00 00                  call 0x1408039c4
0080285E  8B F0                           mov esi, eax
00802860  85 C0                           test eax, eax
00802862  0F 88 79 01 00 00               js 0x1408029e1
00802868  4C 8B 7D B0                     mov r15, qword ptr [rbp - 0x50]
0080286C  49 8B 47 48                     mov rax, qword ptr [r15 + 0x48]
00802870  48 8B 08                        mov rcx, qword ptr [rax]
00802873  0F B7 85 18 02 00 00            movzx eax, word ptr [rbp + 0x218]
0080287A  48 8B 11                        mov rdx, qword ptr [rcx]
0080287D  48 8B 4A 38                     mov rcx, qword ptr [rdx + 0x38]
00802881  66 3B 41 30                     cmp ax, word ptr [rcx + 0x30]
00802885  74 1E                           je 0x1408028a5
00802887  BE CB 00 00 C0                  mov esi, 0xc00000cb
0080288C  4D 85 FF                        test r15, r15
0080288F  0F 84 4C 01 00 00               je 0x1408029e1
00802895  49 8B D7                        mov rdx, r15
00802898  49 8B CD                        mov rcx, r13
0080289B  E8 28 31 AA FF                  call 0x1402a59c8
008028A0  E9 3C 01 00 00                  jmp 0x1408029e1
008028A5  8B 41 3C                        mov eax, dword ptr [rcx + 0x3c]
008028A8  89 45 E8                        mov dword ptr [rbp - 0x18], eax
008028AB  8B 41 48                        mov eax, dword ptr [rcx + 0x48]
008028AE  89 45 EC                        mov dword ptr [rbp - 0x14], eax
008028B1  48 8B C3                        mov rax, rbx
008028B4  F0 48 0F B1 5A 18               lock cmpxchg qword ptr [rdx + 0x18], rbx
008028BA  49 8B 4F 48                     mov rcx, qword ptr [r15 + 0x48]
008028BE  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
008028C2  48 8B 01                        mov rax, qword ptr [rcx]
008028C5  48 8B C8                        mov rcx, rax
008028C8  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
008028CC  E8 7F 66 E7 FF                  call 0x140678f50
008028D1  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
008028D5  49 8B CD                        mov rcx, r13
008028D8  E8 EB 30 AA FF                  call 0x1402a59c8
008028DD  0F B6 B5 08 02 00 00            movzx esi, byte ptr [rbp + 0x208]
008028E4  41 B7 08                        mov r15b, 8
008028E7  41 8A D7                        mov dl, r15b
008028EA  40 8A CE                        mov cl, sil
008028ED  E8 6E 0E 21 00                  call 0x140a13760
008028F2  44 8B 45 AC                     mov r8d, dword ptr [rbp - 0x54]
008028F6  4C 8D 4D C0                     lea r9, [rbp - 0x40]
008028FA  8B 55 A8                        mov edx, dword ptr [rbp - 0x58]
008028FD  85 C0                           test eax, eax
008028FF  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00802903  45 0F B6 FF                     movzx r15d, r15b
00802907  44 0F 45 FE                     cmovne r15d, esi
0080290B  44 89 BD 08 02 00 00            mov dword ptr [rbp + 0x208], r15d
00802912  E8 65 0D 00 00                  call 0x14080367c
00802917  8B F0                           mov esi, eax
00802919  85 C0                           test eax, eax
0080291B  0F 88 C0 00 00 00               js 0x1408029e1
00802921  4C 8B 6D C0                     mov r13, qword ptr [rbp - 0x40]
00802925  33 F6                           xor esi, esi
00802927  4D 85 ED                        test r13, r13
0080292A  0F 84 A8 00 00 00               je 0x1408029d8
00802930  4C 8B 65 B8                     mov r12, qword ptr [rbp - 0x48]
00802934  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
0080293A  48 8D 45 20                     lea rax, [rbp + 0x20]
0080293E  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00802944  49 8D 4D 28                     lea rcx, [r13 + 0x28]
00802948  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0080294D  4C 8D 4D D8                     lea r9, [rbp - 0x28]
00802951  48 8D 45 D0                     lea rax, [rbp - 0x30]
00802955  45 8A C7                        mov r8b, r15b
00802958  33 D2                           xor edx, edx
0080295A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0080295F  E8 20 2D 2B 00                  call 0x140ab5684
00802964  85 C0                           test eax, eax
00802966  78 4A                           js 0x1408029b2
00802968  4C 8B 7D D0                     mov r15, qword ptr [rbp - 0x30]
0080296C  49 8B CF                        mov rcx, r15
0080296F  E8 3C 23 A9 FF                  call 0x140294cb0
00802974  49 3B C4                        cmp rax, r12
00802977  74 4B                           je 0x1408029c4
00802979  48 8D 4D 20                     lea rcx, [rbp + 0x20]
0080297D  E8 EA F6 13 00                  call 0x14094206c
00802982  48 83 65 20 00                  and qword ptr [rbp + 0x20], 0
00802987  BA 4D 6D 48 70                  mov edx, 0x70486d4d
0080298C  49 8B CF                        mov rcx, r15
0080298F  E8 4C 4F AF FF                  call 0x1402f78e0
00802994  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00802998  33 D2                           xor edx, edx
0080299A  48 83 65 D0 00                  and qword ptr [rbp - 0x30], 0
0080299F  E8 CC EE 09 00                  call 0x1408a1870
008029A4  48 83 65 D8 00                  and qword ptr [rbp - 0x28], 0
008029A9  44 8B BD 08 02 00 00            mov r15d, dword ptr [rbp + 0x208]
008029B0  EB 05                           jmp 0x1408029b7
008029B2  85 F6                           test esi, esi
008029B4  0F 49 F0                        cmovns esi, eax
008029B7  4D 8B 6D 00                     mov r13, qword ptr [r13]
008029BB  4D 85 ED                        test r13, r13
008029BE  0F 85 70 FF FF FF               jne 0x140802934
008029C4  4C 8B A5 00 02 00 00            mov r12, qword ptr [rbp + 0x200]
008029CB  4D 85 ED                        test r13, r13
008029CE  0F 85 87 01 00 00               jne 0x140802b5b
008029D4  85 F6                           test esi, esi
008029D6  78 05                           js 0x1408029dd
008029D8  BE D4 04 00 C0                  mov esi, 0xc00004d4
008029DD  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
008029E1  40 F6 C7 02                     test dil, 2
008029E5  74 05                           je 0x1408029ec
008029E7  E8 C4 AE A5 FF                  call 0x14025d8b0
008029EC  85 F6                           test esi, esi
008029EE  79 17                           jns 0x140802a07
008029F0  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
008029F5  4C 8D 45 00                     lea r8, [rbp]
008029F9  8B 55 AC                        mov edx, dword ptr [rbp - 0x54]
008029FC  44 8B CE                        mov r9d, esi
008029FF  8B 4D A8                        mov ecx, dword ptr [rbp - 0x58]
00802A02  E8 7D 24 00 00                  call 0x140804e84
00802A07  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
00802A0B  BB 04 00 00 00                  mov ebx, 4
00802A10  4D 85 FF                        test r15, r15
00802A13  74 3A                           je 0x140802a4f
00802A15  49 8B D7                        mov rdx, r15
00802A18  49 8B CD                        mov rcx, r13
00802A1B  E8 F0 2D A9 FF                  call 0x140295810
00802A20  44 8B 45 A0                     mov r8d, dword ptr [rbp - 0x60]
00802A24  8B D3                           mov edx, ebx
00802A26  49 8B CF                        mov rcx, r15
00802A29  E8 CE E7 C2 FF                  call 0x1404311fc
00802A2E  4D 85 F6                        test r14, r14
00802A31  74 13                           je 0x140802a46
00802A33  41 83 66 44 FE                  and dword ptr [r14 + 0x44], 0xfffffffe
00802A38  41 8B 46 44                     mov eax, dword ptr [r14 + 0x44]
00802A3C  24 02                           and al, 2
00802A3E  F6 D8                           neg al
00802A40  48 1B C0                        sbb rax, rax
00802A43  4C 23 F0                        and r14, rax
00802A46  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00802A4A  E8 11 44 B1 FF                  call 0x140316e60
00802A4F  4C 8B 7D B0                     mov r15, qword ptr [rbp - 0x50]
00802A53  4D 85 FF                        test r15, r15
00802A56  74 21                           je 0x140802a79
00802A58  49 8B D7                        mov rdx, r15
00802A5B  49 8B CD                        mov rcx, r13
00802A5E  E8 AD 2D A9 FF                  call 0x140295810
00802A63  44 8B 45 88                     mov r8d, dword ptr [rbp - 0x78]
00802A67  8B D3                           mov edx, ebx
00802A69  49 8B CF                        mov rcx, r15
00802A6C  E8 8B E7 C2 FF                  call 0x1404311fc
00802A71  49 8B CF                        mov rcx, r15
00802A74  E8 E7 43 B1 FF                  call 0x140316e60
00802A79  4D 85 F6                        test r14, r14
00802A7C  74 08                           je 0x140802a86
00802A7E  49 8B CE                        mov rcx, r14
00802A81  E8 3A 09 00 00                  call 0x1408033c0
00802A86  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00802A8D  E8 CE A2 2C 00                  call 0x140accd60
00802A92  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00802A96  E8 C5 A2 2C 00                  call 0x140accd60
00802A9B  BB 01 00 00 00                  mov ebx, 1
00802AA0  40 84 FB                        test bl, dil
00802AA3  74 10                           je 0x140802ab5
00802AA5  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00802AA9  48 81 C1 E8 01 00 00            add rcx, 0x1e8
00802AB0  E8 CB 73 B4 FF                  call 0x140349e80
00802AB5  48 83 7D 20 00                  cmp qword ptr [rbp + 0x20], 0
00802ABA  74 09                           je 0x140802ac5
00802ABC  48 8D 4D 20                     lea rcx, [rbp + 0x20]
00802AC0  E8 A7 F5 13 00                  call 0x14094206c
00802AC5  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00802AC9  48 85 C0                        test rax, rax
00802ACC  74 0A                           je 0x140802ad8
00802ACE  8B D3                           mov edx, ebx
00802AD0  48 8B C8                        mov rcx, rax
00802AD3  E8 70 58 C5 FF                  call 0x140458348
00802AD8  4C 8B 7D D0                     mov r15, qword ptr [rbp - 0x30]
00802ADC  4D 85 FF                        test r15, r15
00802ADF  74 0D                           je 0x140802aee
00802AE1  BA 4D 6D 48 70                  mov edx, 0x70486d4d
00802AE6  49 8B CF                        mov rcx, r15
00802AE9  E8 F2 4D AF FF                  call 0x1402f78e0
00802AEE  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00802AF2  48 85 C9                        test rcx, rcx
00802AF5  74 07                           je 0x140802afe
00802AF7  33 D2                           xor edx, edx
00802AF9  E8 72 ED 09 00                  call 0x1408a1870
00802AFE  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
00802B02  48 85 C0                        test rax, rax
00802B05  74 0A                           je 0x140802b11
00802B07  33 D2                           xor edx, edx
00802B09  48 8B C8                        mov rcx, rax
00802B0C  E8 5F FD 37 00                  call 0x140b82870
00802B11  48 83 7D C0 00                  cmp qword ptr [rbp - 0x40], 0
00802B16  74 23                           je 0x140802b3b
00802B18  48 8B 5D C0                     mov rbx, qword ptr [rbp - 0x40]
00802B1C  48 8B 3B                        mov rdi, qword ptr [rbx]
00802B1F  48 8D 4B 28                     lea rcx, [rbx + 0x28]
00802B23  48 89 7D C0                     mov qword ptr [rbp - 0x40], rdi
00802B27  E8 D4 DC 1B 00                  call 0x1409c0800
00802B2C  33 D2                           xor edx, edx
00802B2E  48 8B CB                        mov rcx, rbx
00802B31  E8 3A FD 37 00                  call 0x140b82870
00802B36  48 85 FF                        test rdi, rdi
00802B39  75 DD                           jne 0x140802b18
00802B3B  48 8D 4D 00                     lea rcx, [rbp]
00802B3F  E8 BC DC 1B 00                  call 0x1409c0800
00802B44  8B C6                           mov eax, esi
00802B46  48 81 C4 28 03 00 00            add rsp, 0x328
00802B4D  41 5F                           pop r15
00802B4F  41 5E                           pop r14
00802B51  41 5D                           pop r13
00802B53  41 5C                           pop r12
00802B55  5F                              pop rdi
00802B56  5E                              pop rsi
00802B57  5B                              pop rbx
00802B58  5D                              pop rbp
00802B59  C3                              ret
00802B5A  CC                              int3
00802B5B  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
00802B5F  41 BF 01 00 00 00               mov r15d, 1
00802B65  41 8B D7                        mov edx, r15d
00802B68  E8 DB 57 C5 FF                  call 0x140458348
00802B6D  48 83 65 B8 00                  and qword ptr [rbp - 0x48], 0
00802B72  49 8D 4D 28                     lea rcx, [r13 + 0x28]
00802B76  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00802B79  33 D2                           xor edx, edx
00802B7B  F3 0F 7F 45 00                  movdqu xmmword ptr [rbp], xmm0
00802B80  E8 FB 7B C2 FF                  call 0x14042a780
00802B85  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
00802B8A  41 84 C7                        test r15b, al
00802B8D  75 10                           jne 0x140802b9f
00802B8F  83 7D 88 03                     cmp dword ptr [rbp - 0x78], 3
00802B93  74 10                           je 0x140802ba5
00802B95  BE 03 A0 00 C0                  mov esi, 0xc000a003
00802B9A  E9 3E FE FF FF                  jmp 0x1408029dd
00802B9F  83 7D 88 00                     cmp dword ptr [rbp - 0x78], 0
00802BA3  EB EE                           jmp 0x140802b93
00802BA5  4C 8B 6D 10                     mov r13, qword ptr [rbp + 0x10]
00802BA9  48 8D 45 C8                     lea rax, [rbp - 0x38]
00802BAD  44 0F B7 BD 10 02 00 00         movzx r15d, word ptr [rbp + 0x210]
00802BB5  48 8D 4D 20                     lea rcx, [rbp + 0x20]
00802BB9  45 8B 4E 24                     mov r9d, dword ptr [r14 + 0x24]
00802BBD  41 8B D5                        mov edx, r13d
00802BC0  45 8B 46 20                     mov r8d, dword ptr [r14 + 0x20]
00802BC4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00802BC9  48 8D 45 98                     lea rax, [rbp - 0x68]
00802BCD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00802BD2  66 44 89 7C 24 20               mov word ptr [rsp + 0x20], r15w
00802BD8  E8 BB 03 00 00                  call 0x140802f98
00802BDD  8B F0                           mov esi, eax
00802BDF  85 C0                           test eax, eax
00802BE1  0F 88 F6 FD FF FF               js 0x1408029dd
00802BE7  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
00802BEB  8B 40 08                        mov eax, dword ptr [rax + 8]
00802BEE  89 85 00 02 00 00               mov dword ptr [rbp + 0x200], eax
00802BF4  41 39 46 40                     cmp dword ptr [r14 + 0x40], eax
00802BF8  72 0A                           jb 0x140802c04
00802BFA  BE 2A 04 00 C0                  mov esi, 0xc000042a
00802BFF  E9 D9 FD FF FF                  jmp 0x1408029dd
00802C04  B8 4C 01 00 00                  mov eax, 0x14c
00802C09  66 39 85 18 02 00 00            cmp word ptr [rbp + 0x218], ax
00802C10  75 61                           jne 0x140802c73
00802C12  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
00802C16  BA FF 0F 00 00                  mov edx, 0xfff
00802C1B  49 B8 00 00 00 00 01 00 00 00   movabs r8, 0x100000000
00802C25  41 0F B6 4F 21                  movzx ecx, byte ptr [r15 + 0x21]
00802C2A  41 8B 47 1C                     mov eax, dword ptr [r15 + 0x1c]
00802C2E  48 C1 E1 20                     shl rcx, 0x20
00802C32  48 0B C8                        or rcx, rax
00802C35  48 C1 E1 0C                     shl rcx, 0xc
00802C39  48 0B CA                        or rcx, rdx
00802C3C  49 3B C8                        cmp rcx, r8
00802C3F  77 20                           ja 0x140802c61
00802C41  4C 8B 7D B0                     mov r15, qword ptr [rbp - 0x50]
00802C45  41 0F B6 4F 21                  movzx ecx, byte ptr [r15 + 0x21]
00802C4A  41 8B 47 1C                     mov eax, dword ptr [r15 + 0x1c]
00802C4E  48 C1 E1 20                     shl rcx, 0x20
00802C52  48 0B C8                        or rcx, rax
00802C55  48 C1 E1 0C                     shl rcx, 0xc
00802C59  48 0B CA                        or rcx, rdx
00802C5C  49 3B C8                        cmp rcx, r8
00802C5F  76 0A                           jbe 0x140802c6b
00802C61  BE 19 00 00 C0                  mov esi, 0xc0000019
00802C66  E9 72 FD FF FF                  jmp 0x1408029dd
00802C6B  44 0F B7 BD 10 02 00 00         movzx r15d, word ptr [rbp + 0x210]
00802C73  83 C8 FF                        or eax, 0xffffffff
00802C76  44 3B E8                        cmp r13d, eax
00802C79  0F 83 06 03 00 00               jae 0x140802f85
00802C7F  39 45 18                        cmp dword ptr [rbp + 0x18], eax
00802C82  0F 83 FD 02 00 00               jae 0x140802f85
00802C88  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00802C8C  BA 01 00 00 00                  mov edx, 1
00802C91  E8 B2 0C 00 00                  call 0x140803948
00802C96  4C 8B E8                        mov r13, rax
00802C99  48 85 C0                        test rax, rax
00802C9C  75 0A                           jne 0x140802ca8
00802C9E  BE 9A 00 00 C0                  mov esi, 0xc000009a
00802CA3  E9 35 FD FF FF                  jmp 0x1408029dd
00802CA8  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
00802CAD  4C 8D 45 70                     lea r8, [rbp + 0x70]
00802CB1  83 E0 01                        and eax, 1
00802CB4  49 8B CD                        mov rcx, r13
00802CB7  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00802CBB  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
00802CBF  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
00802CC5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00802CCA  66 44 89 7C 24 28               mov word ptr [rsp + 0x28], r15w
00802CD0  4C 8B 7D B0                     mov r15, qword ptr [rbp - 0x50]
00802CD4  49 8B D7                        mov rdx, r15
00802CD7  E8 94 41 00 00                  call 0x140806e70
00802CDC  8B F0                           mov esi, eax
00802CDE  85 C0                           test eax, eax
00802CE0  0F 88 F7 FC FF FF               js 0x1408029dd
00802CE6  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
00802CEA  4C 8D 85 10 01 00 00            lea r8, [rbp + 0x110]
00802CF1  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
00802CF5  49 8B CD                        mov rcx, r13
00802CF8  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
00802D00  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00802D05  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00802D0A  0F B7 85 10 02 00 00            movzx eax, word ptr [rbp + 0x210]
00802D11  66 89 44 24 28                  mov word ptr [rsp + 0x28], ax
00802D16  E8 55 41 00 00                  call 0x140806e70
00802D1B  8B F0                           mov esi, eax
00802D1D  85 C0                           test eax, eax
00802D1F  0F 88 B8 FC FF FF               js 0x1408029dd
00802D25  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
00802D2A  A8 01                           test al, 1
00802D2C  0F 84 FC 00 00 00               je 0x140802e2e
00802D32  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
00802D36  49 8B CF                        mov rcx, r15
00802D39  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
00802D3D  E8 5A 42 00 00                  call 0x140806f9c
00802D42  8B F0                           mov esi, eax
00802D44  85 C0                           test eax, eax
00802D46  0F 88 91 FC FF FF               js 0x1408029dd
00802D4C  48 83 A4 24 C0 00 00 00 00      and qword ptr [rsp + 0xc0], 0
00802D55  45 33 C9                        xor r9d, r9d
00802D58  48 83 A4 24 B8 00 00 00 00      and qword ptr [rsp + 0xb8], 0
00802D61  45 33 C0                        xor r8d, r8d
00802D64  48 83 A4 24 B0 00 00 00 00      and qword ptr [rsp + 0xb0], 0
00802D6D  0F B7 85 10 02 00 00            movzx eax, word ptr [rbp + 0x210]
00802D74  4C 8B 7D C8                     mov r15, qword ptr [rbp - 0x38]
00802D78  48 8B 95 18 01 00 00            mov rdx, qword ptr [rbp + 0x118]
00802D7F  48 8B 8D 58 01 00 00            mov rcx, qword ptr [rbp + 0x158]
00802D86  83 65 E0 00                     and dword ptr [rbp - 0x20], 0
00802D8A  66 89 84 24 A8 00 00 00         mov word ptr [rsp + 0xa8], ax
00802D92  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
00802D96  C7 84 24 A0 00 00 00 02 00 00 00  mov dword ptr [rsp + 0xa0], 2
00802DA1  4C 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], r15
00802DA9  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00802DB1  8B 85 08 01 00 00               mov eax, dword ptr [rbp + 0x108]
00802DB7  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
00802DBE  48 8B 85 00 01 00 00            mov rax, qword ptr [rbp + 0x100]
00802DC5  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00802DCD  48 8D 45 E0                     lea rax, [rbp - 0x20]
00802DD1  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00802DD6  8B 85 94 00 00 00               mov eax, dword ptr [rbp + 0x94]
00802DDC  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00802DE0  48 8B 85 C0 00 00 00            mov rax, qword ptr [rbp + 0xc0]
00802DE7  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00802DEC  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
00802DF0  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00802DF5  48 8B 85 B8 00 00 00            mov rax, qword ptr [rbp + 0xb8]
00802DFC  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00802E01  33 C0                           xor eax, eax
00802E03  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00802E08  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00802E0C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00802E11  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00802E16  E8 71 24 37 00                  call 0x140b7528c
00802E1B  8B F0                           mov esi, eax
00802E1D  85 C0                           test eax, eax
00802E1F  0F 88 B8 FB FF FF               js 0x1408029dd
00802E25  C7 45 88 03 00 00 00            mov dword ptr [rbp - 0x78], 3
00802E2C  EB 04                           jmp 0x140802e32
00802E2E  4C 8B 7D C8                     mov r15, qword ptr [rbp - 0x38]
00802E32  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
00802E37  A8 02                           test al, 2
00802E39  74 26                           je 0x140802e61
00802E3B  4C 8B 4D 98                     mov r9, qword ptr [rbp - 0x68]
00802E3F  48 8D 55 70                     lea rdx, [rbp + 0x70]
00802E43  4D 8B C6                        mov r8, r14
00802E46  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00802E4B  48 8D 8D 10 01 00 00            lea rcx, [rbp + 0x110]
00802E52  E8 D9 F4 FF FF                  call 0x140802330
00802E57  8B F0                           mov esi, eax
00802E59  85 C0                           test eax, eax
00802E5B  0F 88 7C FB FF FF               js 0x1408029dd
00802E61  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00802E65  4D 8D 7D 10                     lea r15, [r13 + 0x10]
00802E69  45 33 C0                        xor r8d, r8d
00802E6C  33 D2                           xor edx, edx
00802E6E  49 8B CF                        mov rcx, r15
00802E71  66 01 98 E6 01 00 00            add word ptr [rax + 0x1e6], bx
00802E78  90                              nop
00802E79  E8 B2 D3 A0 FF                  call 0x140210230
00802E7E  F0 49 0F BA 2F 00               lock bts qword ptr [r15], 0
00802E84  48 89 85 08 02 00 00            mov qword ptr [rbp + 0x208], rax
00802E8B  73 15                           jae 0x140802ea2
00802E8D  4D 8B C7                        mov r8, r15
00802E90  48 8B D0                        mov rdx, rax
00802E93  49 8B CF                        mov rcx, r15
00802E96  E8 F5 CD A0 FF                  call 0x14020fc90
00802E9B  48 8B 85 08 02 00 00            mov rax, qword ptr [rbp + 0x208]
00802EA2  41 BF 01 00 00 00               mov r15d, 1
00802EA8  48 85 C0                        test rax, rax
00802EAB  74 04                           je 0x140802eb1
00802EAD  44 88 78 0A                     mov byte ptr [rax + 0xa], r15b
00802EB1  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
00802EB6  49 8B CE                        mov rcx, r14
00802EB9  45 8B 46 24                     mov r8d, dword ptr [r14 + 0x24]
00802EBD  41 8B 56 20                     mov edx, dword ptr [r14 + 0x20]
00802EC1  D1 E8                           shr eax, 1
00802EC3  F7 D0                           not eax
00802EC5  41 23 C7                        and eax, r15d
00802EC8  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00802ECC  48 8D 45 00                     lea rax, [rbp]
00802ED0  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00802ED4  8B B5 00 02 00 00               mov esi, dword ptr [rbp + 0x200]
00802EDA  44 8B CE                        mov r9d, esi
00802EDD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00802EE2  48 8D 45 E8                     lea rax, [rbp - 0x18]
00802EE6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00802EEB  E8 14 1B 00 00                  call 0x140804a04
00802EF0  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
00802EF5  A8 02                           test al, 2
00802EF7  74 44                           je 0x140802f3d
00802EF9  41 0F 10 4E 28                  movups xmm1, xmmword ptr [r14 + 0x28]
00802EFE  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00802F02  49 89 46 38                     mov qword ptr [r14 + 0x38], rax
00802F06  41 89 76 40                     mov dword ptr [r14 + 0x40], esi
00802F0A  0F 28 45 00                     movaps xmm0, xmmword ptr [rbp]
00802F0E  F3 41 0F 7F 46 28               movdqu xmmword ptr [r14 + 0x28], xmm0
00802F14  66 0F 7F 4D 00                  movdqa xmmword ptr [rbp], xmm1
00802F19  49 83 3E 00                     cmp qword ptr [r14], 0
00802F1D  75 1E                           jne 0x140802f3d
00802F1F  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
00802F23  4C 39 28                        cmp qword ptr [rax], r13
00802F26  74 07                           je 0x140802f2f
00802F28  B9 03 00 00 00                  mov ecx, 3
00802F2D  CD 29                           int 0x29
00802F2F  4D 89 2E                        mov qword ptr [r14], r13
00802F32  49 89 46 08                     mov qword ptr [r14 + 8], rax
00802F36  4C 89 30                        mov qword ptr [rax], r14
00802F39  4D 89 75 08                     mov qword ptr [r13 + 8], r14
00802F3D  F0 49 0F C1 5D 10               lock xadd qword ptr [r13 + 0x10], rbx
00802F43  80 E3 06                        and bl, 6
00802F46  80 FB 02                        cmp bl, 2
00802F49  75 09                           jne 0x140802f54
00802F4B  49 8D 4D 10                     lea rcx, [r13 + 0x10]
00802F4F  E8 7C 2E A6 FF                  call 0x140265dd0
00802F54  49 8D 4D 10                     lea rcx, [r13 + 0x10]
00802F58  E8 A3 E6 AD FF                  call 0x1402e1600
00802F5D  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
00802F61  90                              nop
00802F62  66 45 01 BD E6 01 00 00         add word ptr [r13 + 0x1e6], r15w
00802F6A  75 12                           jne 0x140802f7e
00802F6C  49 8D 85 98 00 00 00            lea rax, [r13 + 0x98]
00802F73  90                              nop
00802F74  48 39 00                        cmp qword ptr [rax], rax
00802F77  74 05                           je 0x140802f7e
00802F79  E8 02 FD AD FF                  call 0x1402e2c80
00802F7E  33 F6                           xor esi, esi
00802F80  E9 5C FA FF FF                  jmp 0x1408029e1
00802F85  BE 04 09 00 C0                  mov esi, 0xc0000904
00802F8A  E9 4E FA FF FF                  jmp 0x1408029dd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiApplyImageHotPatchRequest(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m164;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m208;
    unsigned int v_stack_m20C;
    unsigned int v_stack_m210;
    unsigned int v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned int v_stack_m24C;
    unsigned __int64 v_stack_m250;
    unsigned int v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned int v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m330;
    unsigned __int64 v_stack_m338;
    unsigned __int64 v_stack_m340;
    unsigned __int64 v_stack_m348;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int8 v_stack_p10;
    unsigned __int16 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned int v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned int v_stack_pA0;
    unsigned __int16 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (808);
    a2 = 0;
    result = memset(v_stack_mE8, a2, 160, a4);
    a2 = 0;
    result = memset(v_stack_m188, a2, 160, a4);
    a2 = 0;
    result = memset(v_stack_m1D8, a2, 160 - 80, a4);
    v_r14 = 0;
    a2 = 0;
    v_stack_m1F8 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m1F8, a2, 160 - 80, a4);
    a2 = 0;
    a3 = 0;
    v_rdi = 0;
    result = MiInitializeImageHotPatchContext(v_stack_mE8, a2, a3, a4);
    a2 = 0;
    a3 = 0;
    result = MiInitializeImageHotPatchContext(v_stack_m188, a2, a3, a4);
    v_stack_m278 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m208 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_p18 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772));
    if ((*(unsigned int *)(a1)) != 2) goto loc_008026C1;
    v_rbx = (160) | (-1);
    if ((*(unsigned __int64 *)(a1 + 8)) != v_rbx) goto loc_008026C1;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (0x7FFFFFFCULL)) != 0) goto loc_008026C1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (3)) == 0) goto loc_008026C1;
    if ((*(unsigned __int64 *)(a1 + 24)) == 0) goto loc_008026C1;
    if ((*(unsigned __int64 *)(a1 + 16)) != 0) goto loc_008026CB;
loc_008026C1:
    goto loc_008029F0;
loc_008026CB:
    result = Feature_Servicing_HotpatchLoaderFixes__private_IsEnabledDeviceUsageNoInline(v_stack_m188, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_008026EB;
    result = PsWow64GetProcessNtdllType((unsigned int)(0xC000000DULL), a2, a3, a4);
    if (((unsigned int)(result)) != 2) goto loc_008026EB;
    goto loc_008029F0;
loc_008026EB:
    result = ExAcquireRundownProtection((unsigned int)(0xC00000BBULL) + 488, a2, a3, a4);
    v_rdi = (unsigned int)(((unsigned __int8)(result)) & ((unsigned int)(v_r14 + 1)));
    if (condition_is_not_equal) goto loc_00802709;
    goto loc_008029E1;
loc_00802709:
    a2 = 0;
    result = MiGetVadForHotPatchInProgress(*(unsigned __int64 *)(a1 + 16), a2, v_stack_m268, v_stack_m258);
    if (sign_flag) goto loc_008029E1;
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m268 + 72)));
    v_stack_m250 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m268 + 72))) + 56) + 60)));
    v_stack_m24C = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m268 + 72))) + 56) + 72)));
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m268 + 72))) + 15)) & (15));
    v_stack_p10 = (unsigned __int8)(result);
    result = MiLocateLockedVadEvent(v_stack_m268, 512, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m268 + 72))), v_stack_m258);
    if (result != 0) goto loc_008027F1;
    result = MiAllocatePool(result + 64, result + 88, (unsigned int)(0x6248694DULL), v_stack_m258);
    if (result != 0) goto loc_00802792;
loc_00802788:
    goto loc_0080288C;
loc_00802792:
    *(unsigned int *)(result + 80) = 512;
    result = MiAllocatePool(256, 72, (unsigned int)(0x4E455048ULL), v_stack_m258);
    *(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 8) = result;
    if (result != 0) goto loc_008027C3;
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)(0xC000009AULL), a2, (unsigned int)(0x4E455048ULL), v_stack_m258);
    goto loc_00802788;
loc_008027C3:
    result = MiInsertVadEvent(v_stack_m268, (unsigned int)(0xC000009AULL), 1, v_stack_m258);
    v_stack_m258 = 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 8) + 32) = v_stack_m250;
    goto loc_008027F5;
loc_008027F1:
loc_008027F5:
    v_stack_m1E8 = v_rbx;
    v_stack_p20 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p20 + 56) + 48));
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p20 + 56) + 48))) == ((unsigned __int16)((unsigned int)(0x8664ULL)))) goto loc_0080283B;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p20 + 56) + 48))) == 332) goto loc_0080283B;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p20 + 56) + 48))) == ((unsigned __int16)((unsigned int)(0xAA64ULL)))) goto loc_0080283B;
    goto loc_0080288C;
loc_0080283B:
    result = MiUnlockVad(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m268, v_stack_p20, v_stack_m258);
    result = MiGetVadForHotPatchInProgress(*(unsigned __int64 *)(a1 + 24), 1, v_stack_m248, v_stack_m270);
    if (sign_flag) goto loc_008029E1;
    if (((unsigned __int16)(v_stack_p20)) == (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m248 + 72))) + 56) + 48))) goto loc_008028A5;
loc_0080288C:
    if (v_stack_m248 == 0) goto loc_008029E1;
    result = MiUnlockVad(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m248, v_stack_m248, v_stack_m270);
    goto loc_008029E1;
loc_008028A5:
    v_stack_m210 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 60)));
    v_stack_m20C = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 72)));
    v_stack_m1E0 = v_rbx;
    v_stack_m240 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m248 + 72));
    result = MiReferenceMappedControlArea(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m248 + 72)), v_stack_m248, v_stack_m248, v_stack_m270);
    result = MiUnlockVad(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m248, v_stack_m248, v_stack_m270);
    result = SeCompareSigningLevels((unsigned __int8)(v_stack_p10), 8, v_stack_m248, v_stack_m270);
    v_r15 = 8;
    if ((unsigned int)(result) != 0) { v_r15 = (unsigned int)(v_stack_p10); }
    v_stack_p10 = (unsigned int)(v_r15);
    result = MiGetAllRegisteredPatches(v_stack_m208, (unsigned int)(v_stack_m250), (unsigned int)(v_stack_m24C), v_stack_m238);
    if (sign_flag) goto loc_008029E1;
    v_rsi = 0;
    if (v_stack_m238 == 0) goto loc_008029D8;
loc_00802934:
    v_stack_m340 = v_stack_m1D8;
    a2 = 0;
    v_stack_m348 = v_stack_m228;
    result = MiOpenHotPatchFile(v_stack_m238 + 40, a2, (unsigned __int8)(v_r15), v_stack_m220);
    if (sign_flag) goto loc_008029B2;
    result = MiSectionControlArea(v_stack_m228, a2, (unsigned __int8)(v_r15), v_stack_m220);
    if (result == v_stack_m240) goto loc_008029C4;
    result = MiUnmapImageInSystemSpace(v_stack_m1D8, a2, (unsigned __int8)(v_r15), v_stack_m220);
    result = ObfDereferenceObjectWithTag(v_stack_m228, (unsigned int)(0x70486D4DULL), (unsigned __int8)(v_r15), v_stack_m220);
    a2 = 0;
    result = ObCloseHandle(v_stack_m220, a2, (unsigned __int8)(v_r15), v_stack_m220);
    goto loc_008029B7;
loc_008029B2:
    if (!sign_flag) { v_rsi = (unsigned int)(result); }
loc_008029B7:
    if (*(unsigned __int64 *)(v_stack_m238) != 0) goto loc_00802934;
loc_008029C4:
    if (*(unsigned __int64 *)(v_stack_m238) != 0) goto loc_00802B5B;
    if (!(sign_flag)) {
        v_rsi = 0xC00004D4ULL;
    }
loc_008029E1:
    if ((((unsigned __int8)(v_rdi)) & (2)) != 0) {
        result = KeLeaveCriticalRegion(v_stack_m220, a2, (unsigned __int8)(v_r15), v_stack_m220);
    }
    if (sign_flag) {
        a3 = v_stack_m1F8;
        a2 = v_stack_m24C;
        a4 = (unsigned int)(v_rsi);
        a1 = v_stack_m250;
        result = MiLogHotPatchOperationStatus(a1, a2, a3, a4);
    }
    if (v_stack_m268 == 0) goto loc_00802A4F;
    result = MiLockVad(v_stack_m278, v_stack_m268, a3, a4);
    result = MiSetVadFlags(v_stack_m268, 4, (unsigned int)(v_stack_m258), a4);
    v_r14 = *(unsigned __int64 *)(v_stack_m250 + 8);
    if (*(unsigned __int64 *)(v_stack_m250 + 8) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(v_stack_m250 + 8) + 68);
        result = (unsigned __int8)((result) & (2));
        result = (unsigned __int8)(-(result));
        v_r14 = (*(unsigned __int64 *)(v_stack_m250 + 8)) & (result);
    }
    result = MiUnlockAndDereferenceVad(v_stack_m268, 4, (unsigned int)(v_stack_m258), a4);
loc_00802A4F:
    if (v_stack_m248 != 0) {
        a2 = v_stack_m248;
        a1 = v_stack_m278;
        result = MiLockVad(a1, a2, (unsigned int)(v_stack_m258), a4);
        a3 = v_stack_m270;
        a2 = 4;
        a1 = v_stack_m248;
        result = MiSetVadFlags(a1, a2, a3, a4);
        a1 = v_stack_m248;
        result = MiUnlockAndDereferenceVad(a1, a2, a3, a4);
    }
    if (v_r14 != 0) {
        a1 = v_r14;
        result = MiDeleteHotPatchEntry(a1, a2, a3, a4);
    }
    result = MiReleaseHotPatchResources(v_stack_mE8, a2, a3, a4);
    result = MiReleaseHotPatchResources(v_stack_m188, a2, a3, a4);
    if (((1) & ((unsigned __int8)(v_rdi))) != 0) {
        a1 = v_stack_m208;
        a1 = (a1) + (488);
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    if (v_stack_m1D8 != 0) {
        a1 = v_stack_m1D8;
        result = MiUnmapImageInSystemSpace(a1, a2, a3, a4);
    }
    result = v_stack_m240;
    if (v_stack_m240 != 0) {
        a2 = 1;
        a1 = v_stack_m240;
        result = MiDereferenceControlAreaBySection(a1, a2, a3, a4);
    }
    if (v_stack_m228 != 0) {
        a2 = 0x70486D4DULL;
        a1 = v_stack_m228;
        result = ObfDereferenceObjectWithTag(a1, a2, a3, a4);
    }
    if (v_stack_m220 != 0) {
        a2 = 0;
        result = ObCloseHandle(v_stack_m220, a2, a3, a4);
    }
    result = v_stack_m260;
    if (v_stack_m260 != 0) {
        a2 = 0;
        a1 = v_stack_m260;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (v_stack_m238 == 0) goto loc_00802B3B;
loc_00802B18:
    v_stack_m238 = *(unsigned __int64 *)(v_stack_m238);
    result = RtlFreeAnsiString(v_stack_m238 + 40, a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m238, a2, a3, a4);
    if (*(unsigned __int64 *)(v_stack_m238) != 0) goto loc_00802B18;
loc_00802B3B:
    result = RtlFreeAnsiString(v_stack_m1F8, a2, a3, a4);
    v_rsp = (v_rsp) + (808);
    return (unsigned int)((unsigned int)(v_rsi));
loc_00802B5B:
    result = MiDereferenceControlAreaBySection(v_stack_m240, 1, a3, a4);
    a2 = 0;
    v_stack_m1F8 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m278 + 40, a2, a3, a4);
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4))))) != 0) goto loc_00802B9F;
loc_00802B93:
    if (v_stack_m270 == 3) goto loc_00802BA5;
    goto loc_008029DD;
loc_00802B9F:
    goto loc_00802B93;
loc_00802BA5:
    v_stack_p30 = v_stack_m230;
    v_stack_p28 = v_stack_m260;
    v_stack_p20 = (unsigned __int16)(v_stack_p18);
    result = MiCaptureHotPatchInfo(v_stack_m1D8, (unsigned int)((unsigned int)(v_stack_m1E8)), (unsigned int)(*(unsigned int *)(v_r14 + 32)), (unsigned int)(*(unsigned int *)(v_r14 + 36)));
    if (sign_flag) goto loc_008029DD;
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m260 + 8)));
    if ((*(unsigned int *)(v_r14 + 64)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m260 + 8))))) goto loc_00802C04;
    goto loc_008029DD;
loc_00802C04:
    if (v_stack_p20 != 332) goto loc_00802C73;
    a1 = (*(unsigned __int8 *)(v_stack_m268 + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(v_stack_m268 + 28)));
    a1 = (a1) << (12);
    a1 = (a1) | ((unsigned int)(0xFFFULL));
    if (a1 > ((unsigned int)(*(unsigned int *)(v_r14 + 32)))) goto loc_00802C61;
    a1 = (*(unsigned __int8 *)(v_stack_m248 + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(v_stack_m248 + 28)));
    a1 = (a1) << (12);
    a1 = (a1) | ((unsigned int)(0xFFFULL));
    if (a1 <= ((unsigned int)(*(unsigned int *)(v_r14 + 32)))) goto loc_00802C6B;
loc_00802C61:
    goto loc_008029DD;
loc_00802C6B:
loc_00802C73:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m248 + 28))) | (0xFFFFFFFFULL));
    if (((unsigned int)(v_stack_m1E8)) >= ((unsigned int)(result))) goto loc_00802F85;
    if (v_stack_m1E0 >= ((unsigned int)(result))) goto loc_00802F85;
    result = MiGetProcessHotPatchContext(v_stack_m208, 1, (unsigned int)(*(unsigned int *)(v_r14 + 32)), (unsigned int)(*(unsigned int *)(v_r14 + 36)));
    if (result != 0) goto loc_00802CA8;
    goto loc_008029DD;
loc_00802CA8:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 4))) & (1));
    v_stack_p40 = (unsigned int)(result);
    v_stack_p30 = v_stack_m260;
    v_stack_p28 = (unsigned __int16)(v_stack_p18);
    result = MiPrepareToHotPatchVad(result, v_stack_m248, v_stack_m188, (unsigned int)(*(unsigned int *)(v_r14 + 36)));
    if (sign_flag) goto loc_008029DD;
    v_stack_p40 = 1;
    v_stack_p38 = v_r14;
    v_stack_p30 = v_stack_m260;
    v_stack_p28 = (unsigned __int16)(v_stack_p18);
    result = MiPrepareToHotPatchVad(result, v_stack_m268, v_stack_mE8, (unsigned int)(*(unsigned int *)(v_r14 + 36)));
    if (sign_flag) goto loc_008029DD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)))) & (1)) == 0) goto loc_00802E2E;
    result = MiProcessPatchImageCfg(v_stack_m248, v_stack_m260, v_stack_m230, (unsigned int)(*(unsigned int *)(v_r14 + 36)));
    if (sign_flag) goto loc_008029DD;
    a4 = 0;
    a3 = 0;
    v_stack_pA8 = (unsigned __int16)(v_stack_p18);
    v_stack_pA0 = 2;
    v_stack_p98 = v_stack_m230;
    v_stack_p90 = v_stack_m260;
    v_stack_p88 = (unsigned int)((unsigned int)(v_stack_mF0));
    v_stack_p80 = v_stack_mF8;
    v_stack_p70 = v_stack_m218;
    v_stack_p68 = (unsigned int)((unsigned int)(v_stack_m164));
    v_stack_p60 = v_stack_m138;
    v_stack_p58 = v_stack_m180;
    v_stack_p50 = v_stack_m140;
    result = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p20 = 0;
    result = RtlApplyHotPatch(v_stack_mA0, v_stack_mE0, a3, a4);
    if (sign_flag) goto loc_008029DD;
    v_stack_m270 = 3;
    goto loc_00802E32;
loc_00802E2E:
loc_00802E32:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)))) & (2)) == 0) goto loc_00802E61;
    v_stack_p20 = v_stack_m230;
    result = MiApplyImageHotPatch(v_stack_mE8, v_stack_m188, v_r14, v_stack_m260);
    if (sign_flag) goto loc_008029DD;
loc_00802E61:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 16, a2, a3, v_stack_m260);
    v_stack_p10 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = result + 16;
        a2 = result;
        a1 = result + 16;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_m260);
        result = v_stack_p10;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 4))) >> (1));
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (1));
    v_stack_p38 = (unsigned int)(result);
    v_stack_p30 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_p28 = v_stack_m1F8;
    v_stack_p20 = v_stack_m210;
    result = MiLogHotPatchOperation(v_r14, (unsigned int)(*(unsigned int *)(v_r14 + 32)), (unsigned int)(*(unsigned int *)(v_r14 + 36)), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)))) & (2)) == 0) goto loc_00802F3D;
    *(unsigned __int64 *)(v_r14 + 56) = v_stack_m210;
    *(unsigned int *)(v_r14 + 64) = (unsigned int)((unsigned int)(v_stack_p8));
    *(unsigned __int64 *)(v_r14 + 40) = v_xmm0;
    v_stack_m1F8 = v_xmm1;
    if ((*(unsigned __int64 *)(v_r14)) != 0) goto loc_00802F3D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) {
        a1 = 3;
    }
    *(unsigned __int64 *)(v_r14) = result;
    *(unsigned __int64 *)(v_r14 + 8) = *(unsigned __int64 *)(result + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = v_r14;
    *(unsigned __int64 *)(result + 8) = v_r14;
loc_00802F3D:
    v_rbx = (unsigned __int8)((v_stack_m238) & (6));
    result = *(unsigned __int64 *)(result + 8);
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = result + 16;
        result = ExfTryToWakePushLock(a1, (unsigned int)(*(unsigned int *)(v_r14 + 32)), (unsigned int)(*(unsigned int *)(v_r14 + 36)), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    }
    result = KeAbPostRelease(result + 16, (unsigned int)(*(unsigned int *)(v_r14 + 32)), (unsigned int)(*(unsigned int *)(v_r14 + 36)), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    if (((unsigned __int8)(v_rbx)) != 2) goto loc_00802F7E;
    result = v_stack_m278 + 152;
    if ((*(unsigned __int64 *)(v_stack_m278 + 152)) != (v_stack_m278 + 152)) {
        result = KiCheckForKernelApcDelivery(result + 16, (unsigned int)(*(unsigned int *)(v_r14 + 32)), (unsigned int)(*(unsigned int *)(v_r14 + 36)), (unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    }
    v_rsi = 0;
    goto loc_008029E1;
loc_00802F85:
    goto loc_008029DD;
}
```

## 5. (Beta) C Style

```c
int64_t MiApplyImageHotPatchRequest(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m164;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m208;
    uint32_t v_stack_m20C;
    uint32_t v_stack_m210;
    uint32_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint32_t v_stack_m24C;
    uint64_t v_stack_m250;
    uint32_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint32_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m330;
    uint64_t v_stack_m338;
    uint64_t v_stack_m340;
    uint64_t v_stack_m348;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint8_t v_stack_p10;
    uint16_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint32_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint32_t v_stack_pA0;
    uint16_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (808);
    Arg2 = 0;
    result = memset(v_stack_mE8, Arg2, 160, a4);
    Arg2 = 0;
    result = memset(v_stack_m188, Arg2, 160, a4);
    Arg2 = 0;
    result = memset(v_stack_m1D8, Arg2, 160 - 80, a4);
    local_r14 = 0;
    Arg2 = 0;
    v_stack_m1F8 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m1F8, Arg2, 160 - 80, a4);
    Arg2 = 0;
    a3 = 0;
    local_rdi = 0;
    result = MiInitializeImageHotPatchContext(v_stack_mE8, Arg2, a3, a4);
    Arg2 = 0;
    a3 = 0;
    result = MiInitializeImageHotPatchContext(v_stack_m188, Arg2, a3, a4);
    v_stack_m278 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m208 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_p18 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC));
    if ((*(uint32_t *)(arg1)) != 2) goto loc_008026C1;
    local_rbx = (160) | (-1);
    if ((*(uint64_t *)(arg1 + 0x8)) != local_rbx) goto loc_008026C1;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) & (0x7FFFFFFCULL)) != 0) goto loc_008026C1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) & (3)) == 0) goto loc_008026C1;
    if ((*(uint64_t *)(arg1 + 0x18)) == 0) goto loc_008026C1;
    if ((*(uint64_t *)(arg1 + 0x10)) != 0) goto loc_008026CB;
loc_008026C1:
    goto loc_008029F0;
loc_008026CB:
    result = Feature_Servicing_HotpatchLoaderFixes__private_IsEnabledDeviceUsageNoInline(v_stack_m188, Arg2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_008026EB;
    result = PsWow64GetProcessNtdllType((uint32_t)(0xC000000DULL), Arg2, a3, a4);
    if (((uint32_t)(result)) != 2) goto loc_008026EB;
    goto loc_008029F0;
loc_008026EB:
    result = ExAcquireRundownProtection((uint32_t)(0xC00000BBULL) + 488, Arg2, a3, a4);
    local_rdi = (uint32_t)(((uint8_t)(result)) & ((uint32_t)(local_r14 + 1)));
    if (condition_is_not_equal) goto loc_00802709;
    goto loc_008029E1;
loc_00802709:
    Arg2 = 0;
    result = MiGetVadForHotPatchInProgress(*(uint64_t *)(arg1 + 0x10), Arg2, v_stack_m268, v_stack_m258);
    if (sign_flag) goto loc_008029E1;
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m268 + 0x48)));
    v_stack_m250 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m268 + 0x48))) + 0x38) + 0x3C)));
    v_stack_m24C = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m268 + 0x48))) + 0x38) + 0x48)));
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m268 + 0x48))) + 0xF)) & (15));
    v_stack_p10 = (uint8_t)(result);
    result = MiLocateLockedVadEvent(v_stack_m268, 512, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m268 + 0x48))), v_stack_m258);
    if (result != 0) goto loc_008027F1;
    result = MiAllocatePool(result + 64, result + 88, (uint32_t)(0x6248694DULL), v_stack_m258);
    if (result != 0) goto loc_00802792;
loc_00802788:
    goto loc_0080288C;
loc_00802792:
    *(uint32_t *)(result + 0x50) = 512;
    result = MiAllocatePool(256, 72, (uint32_t)(0x4E455048ULL), v_stack_m258);
    *(uint64_t *)((uint32_t)(0xC000009AULL) + 0x8) = result;
    if (result != 0) goto loc_008027C3;
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)(0xC000009AULL), Arg2, (uint32_t)(0x4E455048ULL), v_stack_m258);
    goto loc_00802788;
loc_008027C3:
    result = MiInsertVadEvent(v_stack_m268, (uint32_t)(0xC000009AULL), 1, v_stack_m258);
    v_stack_m258 = 2;
    *(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL) + 0x8) + 0x20) = v_stack_m250;
    goto loc_008027F5;
loc_008027F1:
loc_008027F5:
    v_stack_m1E8 = local_rbx;
    v_stack_p20 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p20 + 0x38) + 0x30));
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p20 + 0x38) + 0x30))) == ((uint16_t)((uint32_t)(0x8664ULL)))) goto loc_0080283B;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p20 + 0x38) + 0x30))) == 332) goto loc_0080283B;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p20 + 0x38) + 0x30))) == ((uint16_t)((uint32_t)(0xAA64ULL)))) goto loc_0080283B;
    goto loc_0080288C;
loc_0080283B:
    result = MiUnlockVad(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m268, v_stack_p20, v_stack_m258);
    result = MiGetVadForHotPatchInProgress(*(uint64_t *)(arg1 + 0x18), 1, v_stack_m248, v_stack_m270);
    if (sign_flag) goto loc_008029E1;
    if (((uint16_t)(v_stack_p20)) == (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m248 + 0x48))) + 0x38) + 0x30))) goto loc_008028A5;
loc_0080288C:
    if (v_stack_m248 == 0) goto loc_008029E1;
    result = MiUnlockVad(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m248, v_stack_m248, v_stack_m270);
    goto loc_008029E1;
loc_008028A5:
    v_stack_m210 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x3C)));
    v_stack_m20C = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x48)));
    v_stack_m1E0 = local_rbx;
    v_stack_m240 = *(uint64_t *)(*(uint64_t *)(v_stack_m248 + 0x48));
    result = MiReferenceMappedControlArea(*(uint64_t *)(*(uint64_t *)(v_stack_m248 + 0x48)), v_stack_m248, v_stack_m248, v_stack_m270);
    result = MiUnlockVad(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m248, v_stack_m248, v_stack_m270);
    result = SeCompareSigningLevels((uint8_t)(v_stack_p10), 8, v_stack_m248, v_stack_m270);
    local_r15 = 8;
    if ((uint32_t)(result) != 0) { local_r15 = (uint32_t)(v_stack_p10); }
    v_stack_p10 = (uint32_t)(local_r15);
    result = MiGetAllRegisteredPatches(v_stack_m208, (uint32_t)(v_stack_m250), (uint32_t)(v_stack_m24C), v_stack_m238);
    if (sign_flag) goto loc_008029E1;
    local_rsi = 0;
    if (v_stack_m238 == 0) goto loc_008029D8;
loc_00802934:
    v_stack_m340 = v_stack_m1D8;
    Arg2 = 0;
    v_stack_m348 = v_stack_m228;
    result = MiOpenHotPatchFile(v_stack_m238 + 40, Arg2, (uint8_t)(local_r15), v_stack_m220);
    if (sign_flag) goto loc_008029B2;
    result = MiSectionControlArea(v_stack_m228, Arg2, (uint8_t)(local_r15), v_stack_m220);
    if (result == v_stack_m240) goto loc_008029C4;
    result = MiUnmapImageInSystemSpace(v_stack_m1D8, Arg2, (uint8_t)(local_r15), v_stack_m220);
    result = ObfDereferenceObjectWithTag(v_stack_m228, (uint32_t)(0x70486D4DULL), (uint8_t)(local_r15), v_stack_m220);
    Arg2 = 0;
    result = ObCloseHandle(v_stack_m220, Arg2, (uint8_t)(local_r15), v_stack_m220);
    goto loc_008029B7;
loc_008029B2:
    if (!sign_flag) { local_rsi = (uint32_t)(result); }
loc_008029B7:
    if (*(uint64_t *)(v_stack_m238) != 0) goto loc_00802934;
loc_008029C4:
    if (*(uint64_t *)(v_stack_m238) != 0) goto loc_00802B5B;
    if (!(sign_flag)) {
        local_rsi = 0xC00004D4ULL;
    }
loc_008029E1:
    if ((((uint8_t)(local_rdi)) & (2)) != 0) {
        result = KeLeaveCriticalRegion(v_stack_m220, Arg2, (uint8_t)(local_r15), v_stack_m220);
    }
    if (sign_flag) {
        a3 = v_stack_m1F8;
        Arg2 = v_stack_m24C;
        a4 = (uint32_t)(local_rsi);
        Arg1 = v_stack_m250;
        result = MiLogHotPatchOperationStatus(Arg1, Arg2, a3, a4);
    }
    if (v_stack_m268 == 0) goto loc_00802A4F;
    result = MiLockVad(v_stack_m278, v_stack_m268, a3, a4);
    result = MiSetVadFlags(v_stack_m268, 4, (uint32_t)(v_stack_m258), a4);
    local_r14 = *(uint64_t *)(v_stack_m250 + 0x8);
    if (*(uint64_t *)(v_stack_m250 + 0x8) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(v_stack_m250 + 0x8) + 0x44);
        result = (uint8_t)((result) & (2));
        result = (uint8_t)(-(result));
        local_r14 = (*(uint64_t *)(v_stack_m250 + 0x8)) & (result);
    }
    result = MiUnlockAndDereferenceVad(v_stack_m268, 4, (uint32_t)(v_stack_m258), a4);
loc_00802A4F:
    if (v_stack_m248 != 0) {
        Arg2 = v_stack_m248;
        Arg1 = v_stack_m278;
        result = MiLockVad(Arg1, Arg2, (uint32_t)(v_stack_m258), a4);
        a3 = v_stack_m270;
        Arg2 = 4;
        Arg1 = v_stack_m248;
        result = MiSetVadFlags(Arg1, Arg2, a3, a4);
        Arg1 = v_stack_m248;
        result = MiUnlockAndDereferenceVad(Arg1, Arg2, a3, a4);
    }
    if (local_r14 != 0) {
        Arg1 = local_r14;
        result = MiDeleteHotPatchEntry(Arg1, Arg2, a3, a4);
    }
    result = MiReleaseHotPatchResources(v_stack_mE8, Arg2, a3, a4);
    result = MiReleaseHotPatchResources(v_stack_m188, Arg2, a3, a4);
    if (((1) & ((uint8_t)(local_rdi))) != 0) {
        Arg1 = v_stack_m208;
        Arg1 = (Arg1) + (488);
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    if (v_stack_m1D8 != 0) {
        Arg1 = v_stack_m1D8;
        result = MiUnmapImageInSystemSpace(Arg1, Arg2, a3, a4);
    }
    result = v_stack_m240;
    if (v_stack_m240 != 0) {
        Arg2 = 1;
        Arg1 = v_stack_m240;
        result = MiDereferenceControlAreaBySection(Arg1, Arg2, a3, a4);
    }
    if (v_stack_m228 != 0) {
        Arg2 = 0x70486D4DULL;
        Arg1 = v_stack_m228;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, a3, a4);
    }
    if (v_stack_m220 != 0) {
        Arg2 = 0;
        result = ObCloseHandle(v_stack_m220, Arg2, a3, a4);
    }
    result = v_stack_m260;
    if (v_stack_m260 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m260;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    if (v_stack_m238 == 0) goto loc_00802B3B;
loc_00802B18:
    v_stack_m238 = *(uint64_t *)(v_stack_m238);
    result = RtlFreeAnsiString(v_stack_m238 + 40, Arg2, a3, a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m238, Arg2, a3, a4);
    if (*(uint64_t *)(v_stack_m238) != 0) goto loc_00802B18;
loc_00802B3B:
    result = RtlFreeAnsiString(v_stack_m1F8, Arg2, a3, a4);
    local_rsp = (local_rsp) + (808);
    return (uint32_t)((uint32_t)(local_rsi));
loc_00802B5B:
    result = MiDereferenceControlAreaBySection(v_stack_m240, 1, a3, a4);
    Arg2 = 0;
    v_stack_m1F8 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m278 + 40, Arg2, a3, a4);
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4))))) != 0) goto loc_00802B9F;
loc_00802B93:
    if (v_stack_m270 == 3) goto loc_00802BA5;
    goto loc_008029DD;
loc_00802B9F:
    goto loc_00802B93;
loc_00802BA5:
    v_stack_p30 = v_stack_m230;
    v_stack_p28 = v_stack_m260;
    v_stack_p20 = (uint16_t)(v_stack_p18);
    result = MiCaptureHotPatchInfo(v_stack_m1D8, (uint32_t)((uint32_t)(v_stack_m1E8)), (uint32_t)(*(uint32_t *)(local_r14 + 0x20)), (uint32_t)(*(uint32_t *)(local_r14 + 0x24)));
    if (sign_flag) goto loc_008029DD;
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m260 + 0x8)));
    if ((*(uint32_t *)(local_r14 + 0x40)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m260 + 0x8))))) goto loc_00802C04;
    goto loc_008029DD;
loc_00802C04:
    if (v_stack_p20 != 332) goto loc_00802C73;
    Arg1 = (*(uint8_t *)(v_stack_m268 + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(v_stack_m268 + 0x1C)));
    Arg1 = (Arg1) << (12);
    Arg1 = (Arg1) | ((uint32_t)(0xFFFULL));
    if (Arg1 > ((uint32_t)(*(uint32_t *)(local_r14 + 0x20)))) goto loc_00802C61;
    Arg1 = (*(uint8_t *)(v_stack_m248 + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(v_stack_m248 + 0x1C)));
    Arg1 = (Arg1) << (12);
    Arg1 = (Arg1) | ((uint32_t)(0xFFFULL));
    if (Arg1 <= ((uint32_t)(*(uint32_t *)(local_r14 + 0x20)))) goto loc_00802C6B;
loc_00802C61:
    goto loc_008029DD;
loc_00802C6B:
loc_00802C73:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m248 + 0x1C))) | (0xFFFFFFFFULL));
    if (((uint32_t)(v_stack_m1E8)) >= ((uint32_t)(result))) goto loc_00802F85;
    if (v_stack_m1E0 >= ((uint32_t)(result))) goto loc_00802F85;
    result = MiGetProcessHotPatchContext(v_stack_m208, 1, (uint32_t)(*(uint32_t *)(local_r14 + 0x20)), (uint32_t)(*(uint32_t *)(local_r14 + 0x24)));
    if (result != 0) goto loc_00802CA8;
    goto loc_008029DD;
loc_00802CA8:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4))) & (1));
    v_stack_p40 = (uint32_t)(result);
    v_stack_p30 = v_stack_m260;
    v_stack_p28 = (uint16_t)(v_stack_p18);
    result = MiPrepareToHotPatchVad(result, v_stack_m248, v_stack_m188, (uint32_t)(*(uint32_t *)(local_r14 + 0x24)));
    if (sign_flag) goto loc_008029DD;
    v_stack_p40 = 1;
    v_stack_p38 = local_r14;
    v_stack_p30 = v_stack_m260;
    v_stack_p28 = (uint16_t)(v_stack_p18);
    result = MiPrepareToHotPatchVad(result, v_stack_m268, v_stack_mE8, (uint32_t)(*(uint32_t *)(local_r14 + 0x24)));
    if (sign_flag) goto loc_008029DD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)))) & (1)) == 0) goto loc_00802E2E;
    result = MiProcessPatchImageCfg(v_stack_m248, v_stack_m260, v_stack_m230, (uint32_t)(*(uint32_t *)(local_r14 + 0x24)));
    if (sign_flag) goto loc_008029DD;
    a4 = 0;
    a3 = 0;
    v_stack_pA8 = (uint16_t)(v_stack_p18);
    v_stack_pA0 = 2;
    v_stack_p98 = v_stack_m230;
    v_stack_p90 = v_stack_m260;
    v_stack_p88 = (uint32_t)((uint32_t)(v_stack_mF0));
    v_stack_p80 = v_stack_mF8;
    v_stack_p70 = v_stack_m218;
    v_stack_p68 = (uint32_t)((uint32_t)(v_stack_m164));
    v_stack_p60 = v_stack_m138;
    v_stack_p58 = v_stack_m180;
    v_stack_p50 = v_stack_m140;
    result = 0;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = 0;
    v_stack_p20 = 0;
    result = RtlApplyHotPatch(v_stack_mA0, v_stack_mE0, a3, a4);
    if (sign_flag) goto loc_008029DD;
    v_stack_m270 = 3;
    goto loc_00802E32;
loc_00802E2E:
loc_00802E32:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)))) & (2)) == 0) goto loc_00802E61;
    v_stack_p20 = v_stack_m230;
    result = MiApplyImageHotPatch(v_stack_mE8, v_stack_m188, local_r14, v_stack_m260);
    if (sign_flag) goto loc_008029DD;
loc_00802E61:
    a3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 16, Arg2, a3, v_stack_m260);
    v_stack_p10 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = result + 16;
        Arg2 = result;
        Arg1 = result + 16;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, a3, v_stack_m260);
        result = v_stack_p10;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4))) >> (1));
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (1));
    v_stack_p38 = (uint32_t)(result);
    v_stack_p30 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_p28 = v_stack_m1F8;
    v_stack_p20 = v_stack_m210;
    result = MiLogHotPatchOperation(local_r14, (uint32_t)(*(uint32_t *)(local_r14 + 0x20)), (uint32_t)(*(uint32_t *)(local_r14 + 0x24)), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)))) & (2)) == 0) goto loc_00802F3D;
    *(uint64_t *)(local_r14 + 0x38) = v_stack_m210;
    *(uint32_t *)(local_r14 + 0x40) = (uint32_t)((uint32_t)(v_stack_p8));
    *(uint64_t *)(local_r14 + 0x28) = v_xmm0;
    v_stack_m1F8 = v_xmm1;
    if ((*(uint64_t *)(local_r14)) != 0) goto loc_00802F3D;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) {
        Arg1 = 3;
    }
    *(uint64_t *)(local_r14) = result;
    *(uint64_t *)(local_r14 + 0x8) = *(uint64_t *)(result + 0x8);
    *(uint64_t *)(*(uint64_t *)(result + 0x8)) = local_r14;
    *(uint64_t *)(result + 0x8) = local_r14;
loc_00802F3D:
    local_rbx = (uint8_t)((v_stack_m238) & (6));
    result = *(uint64_t *)(result + 0x8);
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = result + 16;
        result = ExfTryToWakePushLock(Arg1, (uint32_t)(*(uint32_t *)(local_r14 + 0x20)), (uint32_t)(*(uint32_t *)(local_r14 + 0x24)), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    }
    result = KeAbPostRelease(result + 16, (uint32_t)(*(uint32_t *)(local_r14 + 0x20)), (uint32_t)(*(uint32_t *)(local_r14 + 0x24)), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    if (((uint8_t)(local_rbx)) != 2) goto loc_00802F7E;
    result = v_stack_m278 + 152;
    if ((*(uint64_t *)(v_stack_m278 + 0x98)) != (v_stack_m278 + 152)) {
        result = KiCheckForKernelApcDelivery(result + 16, (uint32_t)(*(uint32_t *)(local_r14 + 0x20)), (uint32_t)(*(uint32_t *)(local_r14 + 0x24)), (uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    }
    local_rsi = 0;
    goto loc_008029E1;
loc_00802F85:
    goto loc_008029DD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008025AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
