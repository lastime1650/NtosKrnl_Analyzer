# NtEnumerateValueKey

- RVA: `0x008B3B50`–`0x008B46B0` (길이 `2,912` bytes)
- VA: `0x00000001408B3B50`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082784`
- 디코드: `584`개 명령, `2,912/2,912` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **53**; 고유 호출 대상: **39**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x008B3BE2` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008B3C1F` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (function, `0x0039FC50`)
- `0x008B3C3C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008B3C89` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x008B3C96` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (function, `0x00BC9400`)
- `0x008B3CE5` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (function, `0x00BC9350`)
- `0x008B3D1D` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008B3DA5` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x008B3E15` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x008B3E3D` → [CmKeyBodyRemapToVirtualForEnum](CmKeyBodyRemapToVirtualForEnum_function_008B46C0.md) (function, `0x008B46C0`)
- `0x008B3E9B` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008B3F11` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x008B3F1E` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x008B3F30` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x008B3F35` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x008B3F51` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x008B3F60` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (function, `0x00BC97D0`)
- `0x008B3FC9` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x008B3FEC` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x008B401D` → [CmpQueryKeyValueData](../85/CmpQueryKeyValueData_function_00856650.md) (function, `0x00856650`)
- `0x008B403F` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008B4062` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008B4071` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x008B4076` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x008B4083` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x008B40C6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008B4109` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B4126` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x008B41BD` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x008B41D9` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008B41EB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B4229` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x008B4236` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x008B4248` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008B4276` → [ExFreeToLookasideListEx](../../text/38/ExFreeToLookasideListEx_function_0038ACC0.md) (function, `0x0038ACC0`)
- `0x008B4291` → [ExAllocateFromLookasideListEx](../../text/3C/ExAllocateFromLookasideListEx_function_003CD390.md) (function, `0x003CD390`)
- `0x008B42AA` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008B42D9` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x008B42E3` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x008B43C0` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (function, `0x002F0F7C`)
- `0x008B43D3` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (function, `0x00461190`)
- `0x008B4416` → [CmEnumerateValueFromLayeredKey](CmEnumerateValueFromLayeredKey_function_008B31FC.md) (function, `0x008B31FC`)
- `0x008B44A6` → [EtwpTraceRegistry](../86/EtwpTraceRegistry_function_00862980.md) (function, `0x00862980`)
- `0x008B44F4` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008B44FE` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008B451D` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x008B4574` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x008B458D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B45C7` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x008B460D` → [CmEnumerateValueKeyFromMergedView](../A7/CmEnumerateValueKeyFromMergedView_function_00A7D650.md) (function, `0x00A7D650`)
- `0x008B4665` → [CmpTransSearchAddTransFromKeyBody](../87/CmpTransSearchAddTransFromKeyBody_function_008736B8.md) (function, `0x008736B8`)
- `0x008B4682` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (function, `0x00BC97D0`)
- `0x008B46A6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [RtlInitFunctionalityCache](../78/RtlInitFunctionalityCache_function_0078A5F8.md) at `0x0078A6A1`
- [AdtpObjsInitialize](../82/AdtpObjsInitialize_function_00822B30.md) at `0x00822E9E`
- [AdtpObjsInitialize](../82/AdtpObjsInitialize_function_00822B30.md) at `0x00822EF0`

### Static image references
- `0x008B3B63` → RVA `0x00E0A740` (`.data`; read)
- `0x008B3C09` → RVA `0x00FD8008` (`PAGEDATA`; read)
- `0x008B3D98` → RVA `0x00EEFB88` (`.data`; read)
- `0x008B3E60` → RVA `0x00EF7208` (`.data`; read)
- `0x008B3E77` → RVA `0x00E09F58` (`.data`; read)
- `0x008B426F` → RVA `0x00E2CA40` (`.data`; read)
- `0x008B42FA` → RVA `0x00E09F68` (`.data`; read)
- `0x008B43B2` → RVA `0x0005627C` (`.rdata`; read)
- `0x008B447C` → RVA `0x00862980` (`EtwpTraceRegistry`; read)
- `0x008B454E` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)
- `0x008B45A1` → RVA `0x00E09F70` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **33**
  - `0x008B3BE2` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008B3C1F` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (`PAGE` → `.text`)
  - `0x008B3C3C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008B3C89` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x008B3C96` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (`PAGE` → `PAGECMRC`)
  - `0x008B3CE5` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (`PAGE` → `PAGECMRC`)
  - `0x008B3DA5` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x008B3E9B` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008B3F30` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x008B3F35` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x008B3F51` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x008B3F60` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (`PAGE` → `PAGECMRC`)
  - `0x008B4071` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008B4076` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x008B4083` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`PAGE` → `PAGECMRC`)
  - `0x008B40C6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008B4109` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B4126` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x008B41D9` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008B41EB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B4229` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x008B4236` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x008B4248` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008B4276` → [ExFreeToLookasideListEx](../../text/38/ExFreeToLookasideListEx_function_0038ACC0.md) (`PAGE` → `.text`)
  - `0x008B4291` → [ExAllocateFromLookasideListEx](../../text/3C/ExAllocateFromLookasideListEx_function_003CD390.md) (`PAGE` → `.text`)
  - `0x008B42AA` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008B43C0` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (`PAGE` → `.text`)
  - `0x008B43D3` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (`PAGE` → `.text`)
  - `0x008B451D` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x008B458D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B45C7` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`PAGE` → `PAGECMRC`)
  - `0x008B4682` → [CmpPerformKeyBodyDeletionCheck](../../pagecmrc/BC/CmpPerformKeyBodyDeletionCheck_function_00BC97D0.md) (`PAGE` → `PAGECMRC`)
  - `0x008B46A6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008B3B50  40 53                           push rbx
008B3B52  56                              push rsi
008B3B53  57                              push rdi
008B3B54  41 54                           push r12
008B3B56  41 55                           push r13
008B3B58  41 56                           push r14
008B3B5A  41 57                           push r15
008B3B5C  48 81 EC B0 02 00 00            sub rsp, 0x2b0
008B3B63  48 8B 05 D6 6B 55 00            mov rax, qword ptr [rip + 0x556bd6]
008B3B6A  48 33 C4                        xor rax, rsp
008B3B6D  48 89 84 24 A0 02 00 00         mov qword ptr [rsp + 0x2a0], rax
008B3B75  4D 8B E1                        mov r12, r9
008B3B78  45 8B F8                        mov r15d, r8d
008B3B7B  44 89 44 24 68                  mov dword ptr [rsp + 0x68], r8d
008B3B80  44 8B EA                        mov r13d, edx
008B3B83  89 54 24 54                     mov dword ptr [rsp + 0x54], edx
008B3B87  48 8B D9                        mov rbx, rcx
008B3B8A  48 8B 84 24 18 03 00 00         mov rax, qword ptr [rsp + 0x318]
008B3B92  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
008B3B9A  89 94 24 88 00 00 00            mov dword ptr [rsp + 0x88], edx
008B3BA1  0F 57 C0                        xorps xmm0, xmm0
008B3BA4  33 C0                           xor eax, eax
008B3BA6  0F 11 84 24 10 01 00 00         movups xmmword ptr [rsp + 0x110], xmm0
008B3BAE  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
008B3BB6  33 F6                           xor esi, esi
008B3BB8  89 74 24 78                     mov dword ptr [rsp + 0x78], esi
008B3BBC  0F 11 84 24 20 02 00 00         movups xmmword ptr [rsp + 0x220], xmm0
008B3BC4  0F 11 84 24 30 02 00 00         movups xmmword ptr [rsp + 0x230], xmm0
008B3BCC  0F 11 84 24 40 02 00 00         movups xmmword ptr [rsp + 0x240], xmm0
008B3BD4  33 D2                           xor edx, edx
008B3BD6  44 8D 40 47                     lea r8d, [rax + 0x47]
008B3BDA  48 8D 8C 24 81 01 00 00         lea rcx, [rsp + 0x181]
008B3BE2  E8 59 30 E1 FF                  call 0x1406c6c40
008B3BE7  0F 57 C0                        xorps xmm0, xmm0
008B3BEA  0F 11 84 24 D0 01 00 00         movups xmmword ptr [rsp + 0x1d0], xmm0
008B3BF2  0F 11 84 24 E0 01 00 00         movups xmmword ptr [rsp + 0x1e0], xmm0
008B3BFA  8B C6                           mov eax, esi
008B3BFC  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008B3C01  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
008B3C09  48 39 35 F8 43 72 00            cmp qword ptr [rip + 0x7243f8], rsi
008B3C10  74 12                           je 0x1408b3c24
008B3C12  BA 00 00 02 00                  mov edx, 0x20000
008B3C17  48 8D 8C 24 D0 01 00 00         lea rcx, [rsp + 0x1d0]
008B3C1F  E8 2C C0 AE FF                  call 0x14039fc50
008B3C24  40 88 74 24 52                  mov byte ptr [rsp + 0x52], sil
008B3C29  40 88 74 24 53                  mov byte ptr [rsp + 0x53], sil
008B3C2E  33 D2                           xor edx, edx
008B3C30  44 8D 42 40                     lea r8d, [rdx + 0x40]
008B3C34  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
008B3C3C  E8 FF 2F E1 FF                  call 0x1406c6c40
008B3C41  48 8B FE                        mov rdi, rsi
008B3C44  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
008B3C49  89 74 24 6C                     mov dword ptr [rsp + 0x6c], esi
008B3C4D  0F 57 C0                        xorps xmm0, xmm0
008B3C50  33 C0                           xor eax, eax
008B3C52  0F 11 84 24 70 01 00 00         movups xmmword ptr [rsp + 0x170], xmm0
008B3C5A  88 84 24 80 01 00 00            mov byte ptr [rsp + 0x180], al
008B3C61  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
008B3C69  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
008B3C71  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
008B3C79  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
008B3C81  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
008B3C89  E8 E2 81 B4 FF                  call 0x1403fbe70
008B3C8E  48 89 B4 24 98 00 00 00         mov qword ptr [rsp + 0x98], rsi
008B3C96  E8 65 57 31 00                  call 0x140bc9400
008B3C9B  44 0F B6 F0                     movzx r14d, al
008B3C9F  88 44 24 50                     mov byte ptr [rsp + 0x50], al
008B3CA3  84 C0                           test al, al
008B3CA5  0F 84 42 06 00 00               je 0x1408b42ed
008B3CAB  41 83 FF 02                     cmp r15d, 2
008B3CAF  0F 87 72 08 00 00               ja 0x1408b4527
008B3CB5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B3CBE  44 0F B6 B0 32 02 00 00         movzx r14d, byte ptr [rax + 0x232]
008B3CC6  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008B3CCB  48 8D 44 24 60                  lea rax, [rsp + 0x60]
008B3CD0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B3CD5  45 0F B6 CE                     movzx r9d, r14b
008B3CD9  41 BF 01 00 00 00               mov r15d, 1
008B3CDF  41 8B D7                        mov edx, r15d
008B3CE2  48 8B CB                        mov rcx, rbx
008B3CE5  E8 66 56 31 00                  call 0x140bc9350
008B3CEA  8B D8                           mov ebx, eax
008B3CEC  85 C0                           test eax, eax
008B3CEE  0F 88 31 07 00 00               js 0x1408b4425
008B3CF4  48 39 35 0D 43 72 00            cmp qword ptr [rip + 0x72430d], rsi
008B3CFB  0F 85 CF 07 00 00               jne 0x1408b44d0
008B3D01  45 3A F7                        cmp r14b, r15b
008B3D04  0F 85 BA 05 00 00               jne 0x1408b42c4
008B3D0A  44 8B AC 24 10 03 00 00         mov r13d, dword ptr [rsp + 0x310]
008B3D12  45 85 ED                        test r13d, r13d
008B3D15  74 28                           je 0x1408b3d3f
008B3D17  41 F6 C4 03                     test r12b, 3
008B3D1B  74 05                           je 0x1408b3d22
008B3D1D  E8 AE 62 FE FF                  call 0x140899fd0
008B3D22  4B 8D 14 2C                     lea rdx, [r12 + r13]
008B3D26  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
008B3D30  48 3B D1                        cmp rdx, rcx
008B3D33  77 05                           ja 0x1408b3d3a
008B3D35  49 3B D4                        cmp rdx, r12
008B3D38  73 0F                           jae 0x1408b3d49
008B3D3A  0F B6 01                        movzx eax, byte ptr [rcx]
008B3D3D  EB 0A                           jmp 0x1408b3d49
008B3D3F  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
008B3D49  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
008B3D51  48 3B D9                        cmp rbx, rcx
008B3D54  48 0F 42 CB                     cmovb rcx, rbx
008B3D58  8B 01                           mov eax, dword ptr [rcx]
008B3D5A  89 01                           mov dword ptr [rcx], eax
008B3D5C  EB 24                           jmp 0x1408b3d82
008B3D5E  8B D8                           mov ebx, eax
008B3D60  33 F6                           xor esi, esi
008B3D62  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
008B3D67  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
008B3D6F  44 8B AC 24 88 00 00 00         mov r13d, dword ptr [rsp + 0x88]
008B3D77  44 0F B6 74 24 50               movzx r14d, byte ptr [rsp + 0x50]
008B3D7D  E9 7A 03 00 00                  jmp 0x1408b40fc
008B3D82  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B3D8B  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B3D92  90                              nop
008B3D93  C6 44 24 53 01                  mov byte ptr [rsp + 0x53], 1
008B3D98  83 3D E9 BD 63 00 00            cmp dword ptr [rip + 0x63bde9], 0
008B3D9F  0F 84 84 00 00 00               je 0x1408b3e29
008B3DA5  E8 D2 2C BA FF                  call 0x140456a7c
008B3DAA  85 C0                           test eax, eax
008B3DAC  75 7B                           jne 0x1408b3e29
008B3DAE  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
008B3DB3  48 89 BC 24 30 01 00 00         mov qword ptr [rsp + 0x130], rdi
008B3DBB  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
008B3DBF  89 84 24 38 01 00 00            mov dword ptr [rsp + 0x138], eax
008B3DC6  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
008B3DCA  89 84 24 3C 01 00 00            mov dword ptr [rsp + 0x13c], eax
008B3DD1  4C 89 A4 24 40 01 00 00         mov qword ptr [rsp + 0x140], r12
008B3DD9  44 89 AC 24 48 01 00 00         mov dword ptr [rsp + 0x148], r13d
008B3DE1  48 89 9C 24 50 01 00 00         mov qword ptr [rsp + 0x150], rbx
008B3DE9  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
008B3DF1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B3DF6  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
008B3DFB  C7 44 24 20 15 00 00 00         mov dword ptr [rsp + 0x20], 0x15
008B3E03  41 B1 01                        mov r9b, 1
008B3E06  45 33 C0                        xor r8d, r8d
008B3E09  48 8D 94 24 30 01 00 00         lea rdx, [rsp + 0x130]
008B3E11  41 8D 48 06                     lea ecx, [r8 + 6]
008B3E15  E8 26 21 FB FF                  call 0x140865f40
008B3E1A  8B D8                           mov ebx, eax
008B3E1C  85 C0                           test eax, eax
008B3E1E  0F 88 FD 07 00 00               js 0x1408b4621
008B3E24  C6 44 24 52 01                  mov byte ptr [rsp + 0x52], 1
008B3E29  4C 8D 8C 24 98 00 00 00         lea r9, [rsp + 0x98]
008B3E31  45 8B C7                        mov r8d, r15d
008B3E34  41 0F B6 D6                     movzx edx, r14b
008B3E38  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
008B3E3D  E8 7E 08 00 00                  call 0x1408b46c0
008B3E42  8B D8                           mov ebx, eax
008B3E44  85 C0                           test eax, eax
008B3E46  0F 88 16 06 00 00               js 0x1408b4462
008B3E4C  41 8B DD                        mov ebx, r13d
008B3E4F  4C 89 A4 24 70 01 00 00         mov qword ptr [rsp + 0x170], r12
008B3E57  45 85 ED                        test r13d, r13d
008B3E5A  0F 84 A8 06 00 00               je 0x1408b4508
008B3E60  48 83 3D A0 33 64 00 00         cmp qword ptr [rip + 0x6433a0], 0
008B3E68  0F 84 55 06 00 00               je 0x1408b44c3
008B3E6E  45 84 F6                        test r14b, r14b
008B3E71  0F 84 39 06 00 00               je 0x1408b44b0
008B3E77  83 3D DA 60 55 00 05            cmp dword ptr [rip + 0x5560da], 5
008B3E7E  0F 87 76 04 00 00               ja 0x1408b42fa
008B3E84  48 83 FB 40                     cmp rbx, 0x40
008B3E88  0F 87 EF 03 00 00               ja 0x1408b427d
008B3E8E  4C 8B C3                        mov r8, rbx
008B3E91  33 D2                           xor edx, edx
008B3E93  48 8D 8C 24 81 01 00 00         lea rcx, [rsp + 0x181]
008B3E9B  E8 A0 2D E1 FF                  call 0x1406c6c40
008B3EA0  48 8D 84 24 81 01 00 00         lea rax, [rsp + 0x181]
008B3EA8  48 89 84 24 78 01 00 00         mov qword ptr [rsp + 0x178], rax
008B3EB0  8B DE                           mov ebx, esi
008B3EB2  85 DB                           test ebx, ebx
008B3EB4  0F 88 A8 05 00 00               js 0x1408b4462
008B3EBA  48 83 BC 24 98 00 00 00 00      cmp qword ptr [rsp + 0x98], 0
008B3EC3  0F 85 F6 06 00 00               jne 0x1408b45bf
008B3EC9  48 8B 9C 24 78 01 00 00         mov rbx, qword ptr [rsp + 0x178]
008B3ED1  48 89 9C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rbx
008B3ED9  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
008B3EE1  0F 57 C0                        xorps xmm0, xmm0
008B3EE4  0F 11 84 24 F0 01 00 00         movups xmmword ptr [rsp + 0x1f0], xmm0
008B3EEC  0F 11 84 24 00 02 00 00         movups xmmword ptr [rsp + 0x200], xmm0
008B3EF4  0F 11 84 24 10 02 00 00         movups xmmword ptr [rsp + 0x210], xmm0
008B3EFC  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
008B3F01  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
008B3F09  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
008B3F11  E8 FA 1F FA FF                  call 0x140855f10
008B3F16  4C 8B E6                        mov r12, rsi
008B3F19  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
008B3F1E  E8 ED 1F FA FF                  call 0x140855f10
008B3F23  44 88 64 24 51                  mov byte ptr [rsp + 0x51], r12b
008B3F28  48 8D 8C 24 F0 01 00 00         lea rcx, [rsp + 0x1f0]
008B3F30  E8 AB 59 31 00                  call 0x140bc98e0
008B3F35  E8 FA 5B 31 00                  call 0x140bc9b34
008B3F3A  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
008B3F3F  4C 8B 77 08                     mov r14, qword ptr [rdi + 8]
008B3F43  66 41 39 76 42                  cmp word ptr [r14 + 0x42], si
008B3F48  0F 85 AA 04 00 00               jne 0x1408b43f8
008B3F4E  49 8B CE                        mov rcx, r14
008B3F51  E8 C6 5A 31 00                  call 0x140bc9a1c
008B3F56  C6 44 24 51 01                  mov byte ptr [rsp + 0x51], 1
008B3F5B  33 D2                           xor edx, edx
008B3F5D  48 8B CF                        mov rcx, rdi
008B3F60  E8 6B 58 31 00                  call 0x140bc97d0
008B3F65  8B D8                           mov ebx, eax
008B3F67  85 C0                           test eax, eax
008B3F69  0F 88 81 04 00 00               js 0x1408b43f0
008B3F6F  48 39 77 38                     cmp qword ptr [rdi + 0x38], rsi
008B3F73  75 09                           jne 0x1408b3f7e
008B3F75  48 39 77 40                     cmp qword ptr [rdi + 0x40], rsi
008B3F79  75 03                           jne 0x1408b3f7e
008B3F7B  44 8B FE                        mov r15d, esi
008B3F7E  45 85 FF                        test r15d, r15d
008B3F81  0F 85 D3 06 00 00               jne 0x1408b465a
008B3F87  4C 8B BC 24 A0 00 00 00         mov r15, qword ptr [rsp + 0xa0]
008B3F8F  4D 85 FF                        test r15, r15
008B3F92  0F 85 AB 06 00 00               jne 0x1408b4643
008B3F98  B8 60 00 00 00                  mov eax, 0x60
008B3F9D  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
008B3FA1  41 3B 1C 06                     cmp ebx, dword ptr [r14 + rax]
008B3FA5  0F 83 40 04 00 00               jae 0x1408b43eb
008B3FAB  41 8B 54 06 04                  mov edx, dword ptr [r14 + rax + 4]
008B3FB0  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
008B3FB4  4C 8D 84 24 90 00 00 00         lea r8, [rsp + 0x90]
008B3FBC  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008B3FC3  0F 84 10 03 00 00               je 0x1408b42d9
008B3FC9  E8 92 0C FA FF                  call 0x140854c60
008B3FCE  4C 8B F8                        mov r15, rax
008B3FD1  8B 1C 98                        mov ebx, dword ptr [rax + rbx*4]
008B3FD4  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
008B3FD8  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
008B3FDD  8B D3                           mov edx, ebx
008B3FDF  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008B3FE6  0F 84 F7 02 00 00               je 0x1408b42e3
008B3FEC  E8 6F 0C FA FF                  call 0x140854c60
008B3FF1  4C 8B E0                        mov r12, rax
008B3FF4  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
008B3FF9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B3FFE  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
008B4003  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
008B400B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B4010  44 8B 4C 24 68                  mov r9d, dword ptr [rsp + 0x68]
008B4015  4D 8B C4                        mov r8, r12
008B4018  8B D3                           mov edx, ebx
008B401A  49 8B CE                        mov rcx, r14
008B401D  E8 2E 26 FA FF                  call 0x140856650
008B4022  8B D8                           mov ebx, eax
008B4024  4D 85 E4                        test r12, r12
008B4027  74 1B                           je 0x1408b4044
008B4029  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
008B402D  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
008B4032  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008B4039  0F 85 BF 04 00 00               jne 0x1408b44fe
008B403F  E8 FC 1E FA FF                  call 0x140855f40
008B4044  4D 85 FF                        test r15, r15
008B4047  74 1E                           je 0x1408b4067
008B4049  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
008B404D  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
008B4055  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008B405C  0F 85 92 04 00 00               jne 0x1408b44f4
008B4062  E8 D9 1E FA FF                  call 0x140855f40
008B4067  80 7C 24 51 00                  cmp byte ptr [rsp + 0x51], 0
008B406C  74 08                           je 0x1408b4076
008B406E  49 8B CE                        mov rcx, r14
008B4071  E8 4A 52 31 00                  call 0x140bc92c0
008B4076  E8 09 5A 31 00                  call 0x140bc9a84
008B407B  48 8D 8C 24 F0 01 00 00         lea rcx, [rsp + 0x1f0]
008B4083  E8 98 58 31 00                  call 0x140bc9920
008B4088  85 DB                           test ebx, ebx
008B408A  0F 88 A5 03 00 00               js 0x1408b4435
008B4090  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
008B4094  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
008B409C  89 01                           mov dword ptr [rcx], eax
008B409E  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
008B40A4  74 25                           je 0x1408b40cb
008B40A6  44 3B E8                        cmp r13d, eax
008B40A9  72 03                           jb 0x1408b40ae
008B40AB  44 8B E8                        mov r13d, eax
008B40AE  48 8B 8C 24 70 01 00 00         mov rcx, qword ptr [rsp + 0x170]
008B40B6  48 8B 94 24 78 01 00 00         mov rdx, qword ptr [rsp + 0x178]
008B40BE  48 3B CA                        cmp rcx, rdx
008B40C1  74 08                           je 0x1408b40cb
008B40C3  45 8B C5                        mov r8d, r13d
008B40C6  E8 75 27 E1 FF                  call 0x1406c6840
008B40CB  44 0F B6 74 24 50               movzx r14d, byte ptr [rsp + 0x50]
008B40D1  44 8B 6C 24 54                  mov r13d, dword ptr [rsp + 0x54]
008B40D6  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
008B40DB  EB 1F                           jmp 0x1408b40fc
008B40DD  8B D8                           mov ebx, eax
008B40DF  33 F6                           xor esi, esi
008B40E1  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
008B40E6  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
008B40EE  44 8B AC 24 88 00 00 00         mov r13d, dword ptr [rsp + 0x88]
008B40F6  44 0F B6 74 24 50               movzx r14d, byte ptr [rsp + 0x50]
008B40FC  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
008B4104  48 85 C9                        test rcx, rcx
008B4107  74 05                           je 0x1408b410e
008B4109  E8 42 52 A4 FF                  call 0x1402f9350
008B410E  80 7C 24 52 00                  cmp byte ptr [rsp + 0x52], 0
008B4113  0F 84 B0 00 00 00               je 0x1408b41c9
008B4119  83 3D 68 BA 63 00 00            cmp dword ptr [rip + 0x63ba68], 0
008B4120  0F 84 A3 00 00 00               je 0x1408b41c9
008B4126  E8 51 29 BA FF                  call 0x140456a7c
008B412B  85 C0                           test eax, eax
008B412D  0F 85 96 00 00 00               jne 0x1408b41c9
008B4133  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
008B413B  48 39 84 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rax
008B4143  0F 84 80 00 00 00               je 0x1408b41c9
008B4149  89 B4 24 E4 00 00 00            mov dword ptr [rsp + 0xe4], esi
008B4150  0F 57 C0                        xorps xmm0, xmm0
008B4153  F3 0F 7F 84 24 F4 00 00 00      movdqu xmmword ptr [rsp + 0xf4], xmm0
008B415C  48 89 B4 24 04 01 00 00         mov qword ptr [rsp + 0x104], rsi
008B4164  89 B4 24 0C 01 00 00            mov dword ptr [rsp + 0x10c], esi
008B416B  48 89 BC 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rdi
008B4173  89 9C 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], ebx
008B417A  89 9C 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], ebx
008B4181  48 8D 84 24 30 01 00 00         lea rax, [rsp + 0x130]
008B4189  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
008B4191  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
008B4199  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B419E  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
008B41A3  C7 44 24 20 15 00 00 00         mov dword ptr [rsp + 0x20], 0x15
008B41AB  45 33 C9                        xor r9d, r9d
008B41AE  45 33 C0                        xor r8d, r8d
008B41B1  48 8D 94 24 D8 00 00 00         lea rdx, [rsp + 0xd8]
008B41B9  41 8D 49 15                     lea ecx, [r9 + 0x15]
008B41BD  E8 7E 1D FB FF                  call 0x140865f40
008B41C2  8B 9C 24 F0 00 00 00            mov ebx, dword ptr [rsp + 0xf0]
008B41C9  80 7C 24 53 00                  cmp byte ptr [rsp + 0x53], 0
008B41CE  74 13                           je 0x1408b41e3
008B41D0  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008B41D9  E8 12 AE 9A FF                  call 0x14025eff0
008B41DE  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
008B41E3  48 85 FF                        test rdi, rdi
008B41E6  74 08                           je 0x1408b41f0
008B41E8  48 8B CF                        mov rcx, rdi
008B41EB  E8 60 51 A4 FF                  call 0x1402f9350
008B41F0  48 8B 94 24 78 01 00 00         mov rdx, qword ptr [rsp + 0x178]
008B41F8  48 85 D2                        test rdx, rdx
008B41FB  74 17                           je 0x1408b4214
008B41FD  48 3B 94 24 70 01 00 00         cmp rdx, qword ptr [rsp + 0x170]
008B4205  74 0D                           je 0x1408b4214
008B4207  48 8D 84 24 81 01 00 00         lea rax, [rsp + 0x181]
008B420F  48 3B D0                        cmp rdx, rax
008B4212  75 4D                           jne 0x1408b4261
008B4214  48 8B 05 ED 3D 72 00            mov rax, qword ptr [rip + 0x723ded]
008B421B  48 85 C0                        test rax, rax
008B421E  0F 85 58 02 00 00               jne 0x1408b447c
008B4224  45 84 F6                        test r14b, r14b
008B4227  74 05                           je 0x1408b422e
008B4229  E8 52 56 31 00                  call 0x140bc9880
008B422E  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
008B4236  E8 15 BB B6 FF                  call 0x14041fd50
008B423B  8B C3                           mov eax, ebx
008B423D  48 8B 8C 24 A0 02 00 00         mov rcx, qword ptr [rsp + 0x2a0]
008B4245  48 33 CC                        xor rcx, rsp
008B4248  E8 F3 83 DF FF                  call 0x1406ac640
008B424D  48 81 C4 B0 02 00 00            add rsp, 0x2b0
008B4254  41 5F                           pop r15
008B4256  41 5E                           pop r14
008B4258  41 5D                           pop r13
008B425A  41 5C                           pop r12
008B425C  5F                              pop rdi
008B425D  5E                              pop rsi
008B425E  5B                              pop rbx
008B425F  C3                              ret
008B4260  CC                              int3
008B4261  F6 84 24 80 01 00 00 01         test byte ptr [rsp + 0x180], 1
008B4269  0F 84 A6 02 00 00               je 0x1408b4515
008B426F  48 8D 0D CA 87 57 00            lea rcx, [rip + 0x5787ca]
008B4276  E8 45 6A AD FF                  call 0x14038acc0
008B427B  EB 97                           jmp 0x1408b4214
008B427D  48 81 FB 00 10 00 00            cmp rbx, 0x1000
008B4284  0F 87 40 01 00 00               ja 0x1408b43ca
008B428A  48 8D 0D AF 87 57 00            lea rcx, [rip + 0x5787af]
008B4291  E8 FA 90 B1 FF                  call 0x1403cd390
008B4296  48 8B F8                        mov rdi, rax
008B4299  48 85 C0                        test rax, rax
008B429C  0F 84 28 01 00 00               je 0x1408b43ca
008B42A2  4C 8B C3                        mov r8, rbx
008B42A5  33 D2                           xor edx, edx
008B42A7  48 8B C8                        mov rcx, rax
008B42AA  E8 91 29 E1 FF                  call 0x1406c6c40
008B42AF  80 8C 24 80 01 00 00 01         or byte ptr [rsp + 0x180], 1
008B42B7  48 89 BC 24 78 01 00 00         mov qword ptr [rsp + 0x178], rdi
008B42BF  E9 EC FB FF FF                  jmp 0x1408b3eb0
008B42C4  44 8B AC 24 10 03 00 00         mov r13d, dword ptr [rsp + 0x310]
008B42CC  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
008B42D4  E9 A9 FA FF FF                  jmp 0x1408b3d82
008B42D9  E8 D2 09 FA FF                  call 0x140854cb0
008B42DE  E9 EB FC FF FF                  jmp 0x1408b3fce
008B42E3  E8 C8 09 FA FF                  call 0x140854cb0
008B42E8  E9 04 FD FF FF                  jmp 0x1408b3ff1
008B42ED  BB 89 01 00 C0                  mov ebx, 0xc0000189
008B42F2  4C 8B FE                        mov r15, rsi
008B42F5  E9 02 FE FF FF                  jmp 0x1408b40fc
008B42FA  F6 05 67 5C 55 00 04            test byte ptr [rip + 0x555c67], 4
008B4301  0F 85 9A 02 00 00               jne 0x1408b45a1
008B4307  32 C0                           xor al, al
008B4309  84 C0                           test al, al
008B430B  0F 84 73 FB FF FF               je 0x1408b3e84
008B4311  4C 89 BC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r15
008B4319  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
008B4321  48 89 84 24 70 02 00 00         mov qword ptr [rsp + 0x270], rax
008B4329  48 C7 84 24 78 02 00 00 08 00 00 00  mov qword ptr [rsp + 0x278], 8
008B4335  C6 44 24 58 01                  mov byte ptr [rsp + 0x58], 1
008B433A  48 8D 44 24 58                  lea rax, [rsp + 0x58]
008B433F  48 89 84 24 80 02 00 00         mov qword ptr [rsp + 0x280], rax
008B4347  48 C7 84 24 88 02 00 00 01 00 00 00  mov qword ptr [rsp + 0x288], 1
008B4353  41 8B D5                        mov edx, r13d
008B4356  41 8D 45 FF                     lea eax, [r13 - 1]
008B435A  41 85 C5                        test r13d, eax
008B435D  74 1A                           je 0x1408b4379
008B435F  41 8B C5                        mov eax, r13d
008B4362  B9 FF FF FF FF                  mov ecx, 0xffffffff
008B4367  45 85 ED                        test r13d, r13d
008B436A  74 06                           je 0x1408b4372
008B436C  FF C1                           inc ecx
008B436E  D1 E8                           shr eax, 1
008B4370  75 FA                           jne 0x1408b436c
008B4372  FF C1                           inc ecx
008B4374  41 8B D7                        mov edx, r15d
008B4377  D3 E2                           shl edx, cl
008B4379  8B C2                           mov eax, edx
008B437B  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
008B4383  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
008B438B  48 89 84 24 90 02 00 00         mov qword ptr [rsp + 0x290], rax
008B4393  48 C7 84 24 98 02 00 00 08 00 00 00  mov qword ptr [rsp + 0x298], 8
008B439F  48 8D 84 24 50 02 00 00         lea rax, [rsp + 0x250]
008B43A7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B43AC  41 B9 05 00 00 00               mov r9d, 5
008B43B2  48 8D 15 C3 1E 7A FF            lea rdx, [rip - 0x85e13d]
008B43B9  48 8D 0D 98 5B 55 00            lea rcx, [rip + 0x555b98]
008B43C0  E8 B7 CB A3 FF                  call 0x1402f0f7c
008B43C5  E9 BA FA FF FF                  jmp 0x1408b3e84
008B43CA  41 B8 43 4D 42 42               mov r8d, 0x42424d43
008B43D0  48 8B D3                        mov rdx, rbx
008B43D3  E8 B8 CD BA FF                  call 0x140461190
008B43D8  48 85 C0                        test rax, rax
008B43DB  0F 85 C7 FA FF FF               jne 0x1408b3ea8
008B43E1  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008B43E6  E9 C7 FA FF FF                  jmp 0x1408b3eb2
008B43EB  BB 1A 00 00 80                  mov ebx, 0x8000001a
008B43F0  4C 8B FE                        mov r15, rsi
008B43F3  E9 2C FC FF FF                  jmp 0x1408b4024
008B43F8  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
008B43FD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008B4402  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
008B4407  4C 8B CB                        mov r9, rbx
008B440A  44 8B 44 24 68                  mov r8d, dword ptr [rsp + 0x68]
008B440F  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
008B4413  48 8B CF                        mov rcx, rdi
008B4416  E8 E1 ED FF FF                  call 0x1408b31fc
008B441B  8B D8                           mov ebx, eax
008B441D  4C 8B FE                        mov r15, rsi
008B4420  E9 FF FB FF FF                  jmp 0x1408b4024
008B4425  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
008B442A  44 0F B6 74 24 50               movzx r14d, byte ptr [rsp + 0x50]
008B4430  E9 BD FE FF FF                  jmp 0x1408b42f2
008B4435  81 FB 05 00 00 80               cmp ebx, 0x80000005
008B443B  0F 84 4F FC FF FF               je 0x1408b4090
008B4441  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
008B4447  0F 84 43 FC FF FF               je 0x1408b4090
008B444D  44 0F B6 74 24 50               movzx r14d, byte ptr [rsp + 0x50]
008B4453  44 8B 6C 24 54                  mov r13d, dword ptr [rsp + 0x54]
008B4458  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
008B445D  E9 9A FC FF FF                  jmp 0x1408b40fc
008B4462  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
008B4467  44 0F B6 74 24 50               movzx r14d, byte ptr [rsp + 0x50]
008B446D  44 8B 6C 24 54                  mov r13d, dword ptr [rsp + 0x54]
008B4472  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
008B4477  E9 80 FC FF FF                  jmp 0x1408b40fc
008B447C  48 8D 0D FD E4 FA FF            lea rcx, [rip - 0x51b03]
008B4483  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008B4488  45 8B CD                        mov r9d, r13d
008B448B  44 8B C3                        mov r8d, ebx
008B448E  48 8D 94 24 D0 01 00 00         lea rdx, [rsp + 0x1d0]
008B4496  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
008B449B  48 3B C1                        cmp rax, rcx
008B449E  B1 12                           mov cl, 0x12
008B44A0  0F 85 00 02 00 00               jne 0x1408b46a6
008B44A6  E8 D5 E4 FA FF                  call 0x140862980
008B44AB  E9 74 FD FF FF                  jmp 0x1408b4224
008B44B0  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
008B44BA  4C 3B E0                        cmp r12, rax
008B44BD  0F 86 B4 F9 FF FF               jbe 0x1408b3e77
008B44C3  4C 89 A4 24 78 01 00 00         mov qword ptr [rsp + 0x178], r12
008B44CB  E9 E0 F9 FF FF                  jmp 0x1408b3eb0
008B44D0  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
008B44D5  48 85 C0                        test rax, rax
008B44D8  0F 84 23 F8 FF FF               je 0x1408b3d01
008B44DE  48 8B 40 08                     mov rax, qword ptr [rax + 8]
008B44E2  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008B44E7  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
008B44EF  E9 0D F8 FF FF                  jmp 0x1408b3d01
008B44F4  E8 27 87 FA FF                  call 0x14085cc20
008B44F9  E9 69 FB FF FF                  jmp 0x1408b4067
008B44FE  E8 1D 87 FA FF                  call 0x14085cc20
008B4503  E9 3C FB FF FF                  jmp 0x1408b4044
008B4508  48 89 B4 24 78 01 00 00         mov qword ptr [rsp + 0x178], rsi
008B4510  E9 9B F9 FF FF                  jmp 0x1408b3eb0
008B4515  48 8B 8C 24 78 01 00 00         mov rcx, qword ptr [rsp + 0x178]
008B451D  E8 5E 18 BC FF                  call 0x140475d80
008B4522  E9 ED FC FF FF                  jmp 0x1408b4214
008B4527  48 39 35 DA 3A 72 00            cmp qword ptr [rip + 0x723ada], rsi
008B452E  0F 84 6A 01 00 00               je 0x1408b469e
008B4534  48 85 DB                        test rbx, rbx
008B4537  0F 84 61 01 00 00               je 0x1408b469e
008B453D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B4546  44 0F B6 88 32 02 00 00         movzx r9d, byte ptr [rax + 0x232]
008B454E  4C 8B 05 6B 25 71 00            mov r8, qword ptr [rip + 0x71256b]
008B4555  48 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], rsi
008B455D  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008B4562  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
008B456A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B456F  33 D2                           xor edx, edx
008B4571  48 8B CB                        mov rcx, rbx
008B4574  E8 37 48 FB FF                  call 0x140868db0
008B4579  85 C0                           test eax, eax
008B457B  0F 88 18 01 00 00               js 0x1408b4699
008B4581  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
008B4589  4C 8B 79 08                     mov r15, qword ptr [rcx + 8]
008B458D  E8 BE 4D A4 FF                  call 0x1402f9350
008B4592  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
008B4597  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008B459C  E9 5B FB FF FF                  jmp 0x1408b40fc
008B45A1  48 8B 05 C8 59 55 00            mov rax, qword ptr [rip + 0x5559c8]
008B45A8  83 E0 04                        and eax, 4
008B45AB  48 3B 05 BE 59 55 00            cmp rax, qword ptr [rip + 0x5559be]
008B45B2  0F 85 4F FD FF FF               jne 0x1408b4307
008B45B8  B0 01                           mov al, 1
008B45BA  E9 4A FD FF FF                  jmp 0x1408b4309
008B45BF  48 8D 8C 24 20 02 00 00         lea rcx, [rsp + 0x220]
008B45C7  E8 14 53 31 00                  call 0x140bc98e0
008B45CC  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
008B45D1  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
008B45D6  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008B45DB  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
008B45E0  48 8B 84 24 78 01 00 00         mov rax, qword ptr [rsp + 0x178]
008B45E8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008B45ED  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
008B45F1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008B45F5  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
008B45FA  45 33 C0                        xor r8d, r8d
008B45FD  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
008B4605  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
008B460A  48 8B CF                        mov rcx, rdi
008B460D  E8 3E 90 1C 00                  call 0x140a7d650
008B4612  8B D8                           mov ebx, eax
008B4614  48 8D 8C 24 20 02 00 00         lea rcx, [rsp + 0x220]
008B461C  E9 62 FA FF FF                  jmp 0x1408b4083
008B4621  44 0F B6 74 24 50               movzx r14d, byte ptr [rsp + 0x50]
008B4627  44 8B 6C 24 54                  mov r13d, dword ptr [rsp + 0x54]
008B462C  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
008B4631  3D 03 05 00 C0                  cmp eax, 0xc0000503
008B4636  0F 85 C0 FA FF FF               jne 0x1408b40fc
008B463C  8B DE                           mov ebx, esi
008B463E  E9 B9 FA FF FF                  jmp 0x1408b40fc
008B4643  4D 3B BE 20 01 00 00            cmp r15, qword ptr [r14 + 0x120]
008B464A  0F 85 48 F9 FF FF               jne 0x1408b3f98
008B4650  B8 18 01 00 00                  mov eax, 0x118
008B4655  E9 43 F9 FF FF                  jmp 0x1408b3f9d
008B465A  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
008B4662  48 8B CF                        mov rcx, rdi
008B4665  E8 4E F0 FB FF                  call 0x1408736b8
008B466A  8B D8                           mov ebx, eax
008B466C  85 C0                           test eax, eax
008B466E  0F 88 7C FD FF FF               js 0x1408b43f0
008B4674  4C 8B BC 24 A0 00 00 00         mov r15, qword ptr [rsp + 0xa0]
008B467C  49 8B D7                        mov rdx, r15
008B467F  48 8B CF                        mov rcx, rdi
008B4682  E8 49 51 31 00                  call 0x140bc97d0
008B4687  8B D8                           mov ebx, eax
008B4689  85 C0                           test eax, eax
008B468B  0F 89 FE F8 FF FF               jns 0x1408b3f8f
008B4691  4C 8B FE                        mov r15, rsi
008B4694  E9 8B F9 FF FF                  jmp 0x1408b4024
008B4699  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
008B469E  4C 8B FE                        mov r15, rsi
008B46A1  E9 F1 FE FF FF                  jmp 0x1408b4597
008B46A6  E8 25 64 E0 FF                  call 0x1406baad0
008B46AB  E9 74 FB FF FF                  jmp 0x1408b4224
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtEnumerateValueKey(__int64 a1, int a2, int a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m167;
    unsigned __int8 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned int v_stack_m1AC;
    unsigned int v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D8;
    unsigned int v_stack_m1DC;
    unsigned __int64 v_stack_m1E4;
    unsigned __int64 v_stack_m1F4;
    unsigned int v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned int v_stack_m204;
    unsigned int v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned int v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned int v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned int v_stack_m27C;
    unsigned int v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned int v_stack_m294;
    unsigned __int8 v_stack_m295;
    unsigned __int8 v_stack_m296;
    unsigned __int8 v_stack_m297;
    unsigned __int8 v_stack_m298;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p178;
    unsigned __int8 v_stack_p180;
    unsigned __int64 v_stack_p1D0;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p220;
    unsigned __int64 v_stack_p250;
    unsigned __int64 v_stack_p270;
    unsigned __int64 v_stack_p278;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p280;
    unsigned __int64 v_stack_p288;
    unsigned __int64 v_stack_p290;
    unsigned __int64 v_stack_p298;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p50;
    unsigned int v_stack_p54;
    unsigned __int8 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p6C;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;

    v_rsp = (v_rsp) - (688);
    result = (*(unsigned __int64 *)(v_rip + 5598166)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m280 = a3;
    v_stack_m294 = a2;
    v_stack_m268 = a6;
    v_stack_m260 = a2;
    result = 0;
    v_stack_m1D8 = v_xmm0;
    v_stack_m1C8 = 0;
    v_rsi = 0;
    v_stack_m270 = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    a2 = 0;
    result = memset(v_stack_m167, a2, result + 71, a4);
    v_stack_m118 = v_xmm0;
    v_stack_m108 = v_xmm0;
    v_stack_m278 = 0;
    v_stack_m240 = 0;
    result = 0;
    if ((*(unsigned __int64 *)(v_rip + 7488504)) != 0) {
        a2 = 0x20000ULL;
        a1 = v_stack_m118;
        result = EtwGetKernelTraceTimestamp(a1, a2, result + 71, a4);
    }
    v_stack_m296 = 0;
    v_stack_m295 = 0;
    a2 = 0;
    result = memset(v_stack_m1B8, a2, a2 + 64, a4);
    v_stack_m288 = 0;
    v_stack_m27C = 0;
    result = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m168 = 0;
    v_stack_m230 = v_stack_m238;
    v_stack_m238 = v_stack_m238;
    result = CmpInitializeThreadInfo(v_stack_m1D8, a2, a2 + 64, a4);
    v_stack_m250 = 0;
    result = CmpAcquireShutdownRundown(v_stack_m1D8, a2, a2 + 64, a4);
    v_stack_m298 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_008B42ED;
    if (((unsigned int)((unsigned int)(a3))) > 2) goto loc_008B4527;
    v_stack_m2C0 = 0;
    v_stack_m2C8 = v_stack_m288;
    result = CmObReferenceObjectByHandle(a1, 1, a2 + 64, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_008B4425;
    if ((*(unsigned __int64 *)(v_rip + 7488269)) != 0) goto loc_008B44D0;
loc_008B3D01:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) != 1) goto loc_008B42C4;
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_008B3D3F;
    if ((((unsigned __int8)(a4)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, 1, a2 + 64, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    if ((a4 + (unsigned int)(a5) * 1) > a1) goto loc_008B3D3A;
    if ((a4 + (unsigned int)(a5) * 1) >= a4) goto loc_008B3D49;
loc_008B3D3A:
    goto loc_008B3D49;
loc_008B3D3F:
loc_008B3D49:
    if (v_stack_m268 < a1) { a1 = v_stack_m268; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    goto loc_008B3D82;
loc_008B3D82:
    v_stack_m295 = 1;
    if ((*(unsigned int *)(v_rip + 6536681)) == 0) goto loc_008B3E29;
    result = CmpIsRegistryLockAcquired(a1, a4 + (unsigned int)(a5) * 1, a2 + 64, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if ((unsigned int)(result) != 0) goto loc_008B3E29;
    v_stack_m1B8 = v_stack_m288;
    v_stack_m1B0 = (unsigned int)((unsigned int)(v_stack_m294));
    v_stack_m1AC = (unsigned int)((unsigned int)(v_stack_m280));
    v_stack_m1A8 = a4;
    v_stack_m1A0 = (unsigned int)((unsigned int)(a5));
    v_stack_m198 = v_stack_m268;
    v_stack_m2B8 = v_stack_m238;
    v_stack_m2C0 = v_stack_m288;
    v_stack_m2C8 = 21;
    a3 = 0;
    result = CmpCallCallBacksEx(a3 + 6, v_stack_m1B8, a3, 1);
    if (sign_flag) goto loc_008B4621;
    v_stack_m296 = 1;
loc_008B3E29:
    result = CmKeyBodyRemapToVirtualForEnum(v_stack_m288, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), 1, v_stack_m250);
    if (sign_flag) goto loc_008B4462;
    v_stack_m178 = a4;
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_008B4508;
    if ((*(unsigned __int64 *)(v_rip + 6566816)) == 0) goto loc_008B44C3;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008B44B0;
loc_008B3E77:
    if ((*(unsigned int *)(v_rip + 5595354)) > 5) goto loc_008B42FA;
loc_008B3E84:
    if (((unsigned int)((unsigned int)((unsigned int)(a5)))) > 64) goto loc_008B427D;
    a2 = 0;
    result = memset(v_stack_m167, a2, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m250);
loc_008B3EA8:
    v_stack_m170 = v_stack_m167;
loc_008B3EB0:
loc_008B3EB2:
    if (sign_flag) goto loc_008B4462;
    if (v_stack_m250 != 0) goto loc_008B45BF;
    v_stack_m218 = v_stack_m170;
    v_stack_m258 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm0;
    v_stack_mD8 = v_xmm0;
    v_stack_m270 = 0;
    v_stack_m248 = 0;
    result = HvpGetCellContextInitialize(v_stack_m258, a2, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m250);
    result = HvpGetCellContextInitialize(v_stack_m270, a2, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m250);
    v_stack_m297 = 0;
    result = CmpAttachToRegistryProcess(v_stack_mF8, a2, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m250);
    result = CmpLockRegistry(v_stack_mF8, a2, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m250);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m288 + 8) + 66)) != 0) goto loc_008B43F8;
    result = CmpLockKcbShared(*(unsigned __int64 *)(v_stack_m288 + 8), a2, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m250);
    v_stack_m297 = 1;
    a2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(v_stack_m288, a2, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m250);
    if (sign_flag) goto loc_008B43F0;
    if ((*(unsigned __int64 *)(v_stack_m288 + 56)) != 0) goto loc_008B3F7E;
    v_r15 = 1;
    if ((*(unsigned __int64 *)(v_stack_m288 + 64)) == 0) {
        v_r15 = 0;
    }
    if ((unsigned int)(v_r15) != 0) goto loc_008B465A;
loc_008B3F8F:
    if (v_stack_m248 != 0) goto loc_008B4643;
loc_008B3F98:
loc_008B3F9D:
    if (((unsigned int)((unsigned int)(v_stack_m294))) >= (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m288 + 8) + 96 * 1))) goto loc_008B43EB;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m288 + 8) + 32) + 140)) & (1)) == 0) goto loc_008B42D9;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m288 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m288 + 8) + 96 * 1 + 4)), v_stack_m258, v_stack_m250);
loc_008B3FCE:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m288 + 8) + 32) + 140)) & (1)) == 0) goto loc_008B42E3;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m288 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + (unsigned int)(v_stack_m294) * 4)))), v_stack_m270, v_stack_m250);
loc_008B3FF1:
    v_stack_m2B8 = v_stack_m27C;
    v_stack_m2C0 = (unsigned int)((unsigned int)(a5));
    v_stack_m2C8 = v_stack_m218;
    result = CmpQueryKeyValueData(*(unsigned __int64 *)(v_stack_m288 + 8), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + (unsigned int)(v_stack_m294) * 4)))), result, (unsigned int)(v_stack_m280));
loc_008B4024:
    if (result == 0) goto loc_008B4044;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m288 + 8) + 32) + 140)) & (1)) != 0) goto loc_008B44FE;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m288 + 8) + 32), v_stack_m270, result, (unsigned int)(v_stack_m280));
loc_008B4044:
    if (result == 0) goto loc_008B4067;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m288 + 8) + 32) + 140)) & (1)) != 0) goto loc_008B44F4;
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m288 + 8) + 32), v_stack_m258, result, (unsigned int)(v_stack_m280));
loc_008B4067:
    if (v_stack_m297 != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m288 + 8);
        result = CmpUnlockKcb(a1, v_stack_m258, result, (unsigned int)(v_stack_m280));
    }
    result = CmpUnlockRegistry(a1, v_stack_m258, result, (unsigned int)(v_stack_m280));
loc_008B4083:
    result = CmpDetachFromRegistryProcess(v_stack_mF8, v_stack_m258, result, (unsigned int)(v_stack_m280));
    if (sign_flag) goto loc_008B4435;
loc_008B4090:
    *(unsigned int *)(v_stack_m268) = (unsigned int)((unsigned int)(v_stack_m27C));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000023ULL) goto loc_008B40CB;
    v_r13 = (unsigned int)(a5);
    if (((unsigned int)((unsigned int)(a5))) >= ((unsigned int)((unsigned int)(v_stack_m27C)))) {
        v_r13 = (unsigned int)((unsigned int)(v_stack_m27C));
    }
    result = (unsigned int)(v_stack_m27C);
    if (v_stack_m178 != v_stack_m170) {
        a3 = (unsigned int)(v_r13);
        result = memcpy(v_stack_m178, v_stack_m170, a3, (unsigned int)(v_stack_m280));
    }
    goto loc_008B40FC;
loc_008B40FC:
    if (v_stack_m250 != 0) {
        result = ObfDereferenceObject(v_stack_m250, v_stack_m170, a3, (unsigned int)(v_stack_m280));
    }
    if (v_stack_m296 == 0) goto loc_008B41C9;
    if ((*(unsigned int *)(v_rip + 6535784)) == 0) goto loc_008B41C9;
    result = CmpIsRegistryLockAcquired(v_stack_m250, v_stack_m170, a3, (unsigned int)(v_stack_m280));
    if ((unsigned int)(result) != 0) goto loc_008B41C9;
    result = v_stack_m238;
    v_rbx = (unsigned int)((unsigned int)(result));
    if (v_stack_m238 != v_stack_m238) {
        v_stack_m204 = 0;
        v_stack_m1F4 = v_xmm0;
        v_stack_m1E4 = 0;
        v_stack_m1DC = 0;
        v_stack_m210 = v_stack_m288;
        v_stack_m208 = (unsigned int)((unsigned int)((unsigned int)(result)));
        v_stack_m1F8 = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = v_stack_m1B8;
        v_stack_m200 = result;
        result = v_stack_m238;
        v_stack_m2B8 = result;
        v_stack_m2C0 = v_stack_m288;
        v_stack_m2C8 = 21;
        a4 = 0;
        a3 = 0;
        a2 = v_stack_m210;
        a1 = a4 + 21;
        result = CmpCallCallBacksEx(a1, a2, a3, a4);
        v_rbx = v_stack_m1F8;
    }
    v_rdi = v_stack_m288;
    if (v_stack_m295 != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = KeLeaveCriticalRegionThread(a1, a2, a3, a4);
        v_rdi = v_stack_m288;
    }
    if (v_rdi != 0) {
        a1 = v_rdi;
        result = ObfDereferenceObject(a1, a2, a3, a4);
    }
    if (v_stack_m170 == 0) goto loc_008B4214;
    if (v_stack_m170 == v_stack_m178) goto loc_008B4214;
    if (v_stack_m170 != v_stack_m167) goto loc_008B4261;
loc_008B4214:
    if (*(unsigned __int64 *)(v_rip + 7486957) != 0) goto loc_008B447C;
loc_008B4224:
    result = *(unsigned __int64 *)(v_rip + 7486957);
    if ((unsigned __int8)(v_stack_m298) != 0) {
        result = CmpReleaseShutdownRundown(a1, v_stack_m170, a3, a4);
    }
    result = CmCleanupThreadInfo(v_stack_m1D8, v_stack_m170, a3, a4);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m170, a3, a4);
    v_rsp = (v_rsp) + (688);
    return result;
loc_008B4261:
    if (((v_stack_p180) & (1)) == 0) goto loc_008B4515;
    result = ExFreeToLookasideListEx(v_rip + 5736394, v_stack_m170, a3, a4);
    goto loc_008B4214;
loc_008B427D:
    if (v_rbx > 0x1000ULL) goto loc_008B43CA;
    result = ExAllocateFromLookasideListEx(v_rip + 5736367, v_stack_m170, a3, a4);
    if (result == 0) goto loc_008B43CA;
    a2 = 0;
    result = memset(result, a2, v_rbx, a4);
    v_stack_p178 = result;
    goto loc_008B3EB0;
loc_008B42C4:
    goto loc_008B3D82;
loc_008B42D9:
    result = HvpGetCellPaged(result, a2, v_rbx, a4);
    goto loc_008B3FCE;
loc_008B42E3:
    result = HvpGetCellPaged(result, a2, v_rbx, a4);
    goto loc_008B3FF1;
loc_008B42ED:
loc_008B42F2:
    goto loc_008B40FC;
loc_008B42FA:
    if (((*(unsigned __int8 *)(v_rip + 5594215)) & (4)) != 0) goto loc_008B45A1;
loc_008B4307:
    result = 0;
loc_008B4309:
    if (0 == 0) goto loc_008B3E84;
    v_stack_pC0 = 0;
    v_stack_p270 = v_stack_pC0;
    v_stack_p278 = 8;
    v_stack_p58 = 1;
    v_stack_p280 = v_stack_p58;
    v_stack_p288 = 1;
    if ((((unsigned int)((unsigned int)(a5))) & ((unsigned int)((unsigned int)(a5) - 1))) == 0) goto loc_008B4379;
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_008B4372;
loc_008B436C:
    a1 = (unsigned int)(((unsigned int)(0xFFFFFFFFULL)) + 1);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) >> (1));
    if (condition_is_not_equal) goto loc_008B436C;
loc_008B4372:
    a1 = (unsigned int)((a1) + 1);
    a2 = (unsigned int)((0) << ((unsigned __int8)(a1)));
loc_008B4379:
    v_stack_pC8 = (unsigned int)(a2);
    v_stack_p290 = v_stack_pC8;
    v_stack_p298 = 8;
    v_stack_p20 = v_stack_p250;
    result = tlgWriteAgg(v_rip + 5594008, v_rip - 8773949, v_rbx, 5);
    goto loc_008B3E84;
loc_008B43CA:
    result = CmpAllocateTransientPoolWithQuota(v_rip + 5594008, (unsigned int)(0xC0000189ULL), (unsigned int)(0x42424D43ULL), 5);
    if (result != 0) goto loc_008B3EA8;
    goto loc_008B3EB2;
loc_008B43EB:
loc_008B43F0:
    goto loc_008B4024;
loc_008B43F8:
    v_stack_p28 = v_stack_p6C;
    v_stack_p20 = (unsigned int)((unsigned int)(a5));
    result = CmEnumerateValueFromLayeredKey(result, (unsigned int)(v_stack_p54), (unsigned int)(v_stack_p68), (unsigned int)(0x8000001AULL));
    goto loc_008B4024;
loc_008B4425:
    goto loc_008B42F2;
loc_008B4435:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0x80000005ULL) goto loc_008B4090;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000023ULL) goto loc_008B4090;
    goto loc_008B40FC;
loc_008B4462:
    goto loc_008B40FC;
loc_008B447C:
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p70;
    if (result != (v_rip - 334595)) goto loc_008B46A6;
    result = EtwpTraceRegistry(18, v_stack_p1D0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(v_stack_p54))));
    goto loc_008B4224;
loc_008B44B0:
    if (result <= result) goto loc_008B3E77;
loc_008B44C3:
    v_stack_p178 = result;
    goto loc_008B3EB0;
loc_008B44D0:
    if (v_stack_p60 == 0) goto loc_008B3D01;
    v_stack_p70 = *(unsigned __int64 *)(v_stack_p60 + 8);
    v_stack_pA8 = *(unsigned __int64 *)(v_stack_p60 + 8);
    goto loc_008B3D01;
loc_008B44F4:
    result = HvpReleaseCellFlat(18, v_stack_p1D0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(v_stack_p54))));
    goto loc_008B4067;
loc_008B44FE:
    result = HvpReleaseCellFlat(18, v_stack_p1D0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(v_stack_p54))));
    goto loc_008B4044;
loc_008B4508:
    v_stack_p178 = 0;
    goto loc_008B3EB0;
loc_008B4515:
    result = CmSiFreeMemory(v_stack_p178, v_stack_p1D0, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(v_stack_p54))));
    goto loc_008B4214;
loc_008B4527:
    if ((*(unsigned __int64 *)(v_rip + 7486170)) == 0) goto loc_008B469E;
    if ((unsigned int)((unsigned int)(result)) == 0) goto loc_008B469E;
    v_stack_p80 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p80;
    a2 = 0;
    result = ObReferenceObjectByHandle((unsigned int)((unsigned int)(result)), a2, *(unsigned __int64 *)(v_rip + 7415147), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (sign_flag) goto loc_008B4699;
    result = ObfDereferenceObject(v_stack_p80, a2, *(unsigned __int64 *)(v_rip + 7415147), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
loc_008B4597:
    goto loc_008B40FC;
loc_008B45A1:
    result = (unsigned int)((*(unsigned __int64 *)(v_rip + 5593544)) & (4));
    if (result != (*(unsigned __int64 *)(v_rip + 5593534))) goto loc_008B4307;
    goto loc_008B4309;
loc_008B45BF:
    result = CmpAttachToRegistryProcess(v_stack_p220, a2, *(unsigned __int64 *)(v_rip + 7415147), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_p40 = 0;
    v_stack_p38 = v_stack_p6C;
    v_stack_p30 = (unsigned int)((unsigned int)(v_stack_p54));
    v_stack_p28 = v_stack_p178;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_p68));
    a3 = 0;
    result = CmEnumerateValueKeyFromMergedView(v_stack_p60, v_stack_p98, a3, (unsigned int)(v_stack_p54));
    goto loc_008B4083;
loc_008B4621:
    if (((unsigned int)(result)) != 0xC0000503ULL) goto loc_008B40FC;
    goto loc_008B40FC;
loc_008B4643:
    if (v_stack_p70 != (*(unsigned __int64 *)(v_stack_p50 + 288))) goto loc_008B3F98;
    goto loc_008B3F9D;
loc_008B465A:
    result = CmpTransSearchAddTransFromKeyBody(v_stack_p60, v_stack_pA0, a3, (unsigned int)(v_stack_p54));
    if (sign_flag) goto loc_008B43F0;
    result = CmpPerformKeyBodyDeletionCheck(v_stack_p60, v_stack_pA0, a3, (unsigned int)(v_stack_p54));
    if (!sign_flag) goto loc_008B3F8F;
    goto loc_008B4024;
loc_008B4699:
loc_008B469E:
    goto loc_008B4597;
loc_008B46A6:
    result = guard_dispatch_icall(v_stack_p60, v_stack_pA0, a3, (unsigned int)(v_stack_p54));
    goto loc_008B4224;
}
```

## 5. (Beta) C Style

```c
int64_t NtEnumerateValueKey(int64_t Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m167;
    uint8_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m198;
    uint32_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint32_t v_stack_m1AC;
    uint32_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D8;
    uint32_t v_stack_m1DC;
    uint64_t v_stack_m1E4;
    uint64_t v_stack_m1F4;
    uint32_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint32_t v_stack_m204;
    uint32_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint32_t v_stack_m260;
    uint64_t v_stack_m268;
    uint32_t v_stack_m270;
    uint64_t v_stack_m278;
    uint32_t v_stack_m27C;
    uint32_t v_stack_m280;
    uint64_t v_stack_m288;
    uint32_t v_stack_m294;
    uint8_t v_stack_m295;
    uint8_t v_stack_m296;
    uint8_t v_stack_m297;
    uint8_t v_stack_m298;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m48;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p178;
    uint8_t v_stack_p180;
    uint64_t v_stack_p1D0;
    uint64_t v_stack_p20;
    uint64_t v_stack_p220;
    uint64_t v_stack_p250;
    uint64_t v_stack_p270;
    uint64_t v_stack_p278;
    uint64_t v_stack_p28;
    uint64_t v_stack_p280;
    uint64_t v_stack_p288;
    uint64_t v_stack_p290;
    uint64_t v_stack_p298;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p50;
    uint32_t v_stack_p54;
    uint8_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p6C;
    uint64_t v_stack_p70;
    uint64_t v_stack_p80;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;

    local_rsp = (local_rsp) - (688);
    result = (*(uint64_t *)(v_rip + 0x556BD6)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m280 = Arg3;
    v_stack_m294 = Arg2;
    v_stack_m268 = Arg6;
    v_stack_m260 = Arg2;
    result = 0;
    v_stack_m1D8 = v_xmm0;
    v_stack_m1C8 = 0;
    local_rsi = 0;
    v_stack_m270 = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    Arg2 = 0;
    result = memset(v_stack_m167, Arg2, result + 71, Arg4);
    v_stack_m118 = v_xmm0;
    v_stack_m108 = v_xmm0;
    v_stack_m278 = 0;
    v_stack_m240 = 0;
    result = 0;
    if ((*(uint64_t *)(v_rip + 0x7243F8)) != 0) {
        Arg2 = 0x20000ULL;
        Arg1 = v_stack_m118;
        result = EtwGetKernelTraceTimestamp(Arg1, Arg2, result + 71, Arg4);
    }
    v_stack_m296 = 0;
    v_stack_m295 = 0;
    Arg2 = 0;
    result = memset(v_stack_m1B8, Arg2, Arg2 + 64, Arg4);
    v_stack_m288 = 0;
    v_stack_m27C = 0;
    result = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m168 = 0;
    v_stack_m230 = v_stack_m238;
    v_stack_m238 = v_stack_m238;
    result = CmpInitializeThreadInfo(v_stack_m1D8, Arg2, Arg2 + 64, Arg4);
    v_stack_m250 = 0;
    result = CmpAcquireShutdownRundown(v_stack_m1D8, Arg2, Arg2 + 64, Arg4);
    v_stack_m298 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_008B42ED;
    if (((uint32_t)((uint32_t)(Arg3))) > 2) goto loc_008B4527;
    v_stack_m2C0 = 0;
    v_stack_m2C8 = v_stack_m288;
    result = CmObReferenceObjectByHandle(Arg1, 1, Arg2 + 64, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_008B4425;
    if ((*(uint64_t *)(v_rip + 0x72430D)) != 0) goto loc_008B44D0;
loc_008B3D01:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) != 1) goto loc_008B42C4;
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_008B3D3F;
    if ((((uint8_t)(Arg4)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, 1, Arg2 + 64, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    if ((Arg4 + (uint32_t)(Arg5) * 1) > Arg1) goto loc_008B3D3A;
    if ((Arg4 + (uint32_t)(Arg5) * 1) >= Arg4) goto loc_008B3D49;
loc_008B3D3A:
    goto loc_008B3D49;
loc_008B3D3F:
loc_008B3D49:
    if (v_stack_m268 < Arg1) { Arg1 = v_stack_m268; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    goto loc_008B3D82;
loc_008B3D82:
    v_stack_m295 = 1;
    if ((*(uint32_t *)(v_rip + 0x63BDE9)) == 0) goto loc_008B3E29;
    result = CmpIsRegistryLockAcquired(Arg1, Arg4 + (uint32_t)(Arg5) * 1, Arg2 + 64, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if ((uint32_t)(result) != 0) goto loc_008B3E29;
    v_stack_m1B8 = v_stack_m288;
    v_stack_m1B0 = (uint32_t)((uint32_t)(v_stack_m294));
    v_stack_m1AC = (uint32_t)((uint32_t)(v_stack_m280));
    v_stack_m1A8 = Arg4;
    v_stack_m1A0 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m198 = v_stack_m268;
    v_stack_m2B8 = v_stack_m238;
    v_stack_m2C0 = v_stack_m288;
    v_stack_m2C8 = 21;
    Arg3 = 0;
    result = CmpCallCallBacksEx(Arg3 + 6, v_stack_m1B8, Arg3, 1);
    if (sign_flag) goto loc_008B4621;
    v_stack_m296 = 1;
loc_008B3E29:
    result = CmKeyBodyRemapToVirtualForEnum(v_stack_m288, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), 1, v_stack_m250);
    if (sign_flag) goto loc_008B4462;
    v_stack_m178 = Arg4;
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_008B4508;
    if ((*(uint64_t *)(v_rip + 0x6433A0)) == 0) goto loc_008B44C3;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008B44B0;
loc_008B3E77:
    if ((*(uint32_t *)(v_rip + 0x5560DA)) > 5) goto loc_008B42FA;
loc_008B3E84:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg5)))) > 64) goto loc_008B427D;
    Arg2 = 0;
    result = memset(v_stack_m167, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m250);
loc_008B3EA8:
    v_stack_m170 = v_stack_m167;
loc_008B3EB0:
loc_008B3EB2:
    if (sign_flag) goto loc_008B4462;
    if (v_stack_m250 != 0) goto loc_008B45BF;
    v_stack_m218 = v_stack_m170;
    v_stack_m258 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm0;
    v_stack_mD8 = v_xmm0;
    v_stack_m270 = 0;
    v_stack_m248 = 0;
    result = HvpGetCellContextInitialize(v_stack_m258, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m250);
    result = HvpGetCellContextInitialize(v_stack_m270, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m250);
    v_stack_m297 = 0;
    result = CmpAttachToRegistryProcess(v_stack_mF8, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m250);
    result = CmpLockRegistry(v_stack_mF8, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m250);
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m288 + 0x8) + 0x42)) != 0) goto loc_008B43F8;
    result = CmpLockKcbShared(*(uint64_t *)(v_stack_m288 + 0x8), Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m250);
    v_stack_m297 = 1;
    Arg2 = 0;
    result = CmpPerformKeyBodyDeletionCheck(v_stack_m288, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m250);
    if (sign_flag) goto loc_008B43F0;
    if ((*(uint64_t *)(v_stack_m288 + 0x38)) != 0) goto loc_008B3F7E;
    local_r15 = 1;
    if ((*(uint64_t *)(v_stack_m288 + 0x40)) == 0) {
        local_r15 = 0;
    }
    if ((uint32_t)(local_r15) != 0) goto loc_008B465A;
loc_008B3F8F:
    if (v_stack_m248 != 0) goto loc_008B4643;
loc_008B3F98:
loc_008B3F9D:
    if (((uint32_t)((uint32_t)(v_stack_m294))) >= (*(uint32_t *)(*(uint64_t *)(v_stack_m288 + 0x8) + 0x60 * 1))) goto loc_008B43EB;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m288 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_008B42D9;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(v_stack_m288 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m288 + 0x8) + 0x60 * 1 + 0x4)), v_stack_m258, v_stack_m250);
loc_008B3FCE:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m288 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_008B42E3;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(v_stack_m288 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + (uint32_t)(v_stack_m294) * 4)))), v_stack_m270, v_stack_m250);
loc_008B3FF1:
    v_stack_m2B8 = v_stack_m27C;
    v_stack_m2C0 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m2C8 = v_stack_m218;
    result = CmpQueryKeyValueData(*(uint64_t *)(v_stack_m288 + 0x8), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + (uint32_t)(v_stack_m294) * 4)))), result, (uint32_t)(v_stack_m280));
loc_008B4024:
    if (result == 0) goto loc_008B4044;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m288 + 0x8) + 0x20) + 0x8C)) & (1)) != 0) goto loc_008B44FE;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(v_stack_m288 + 0x8) + 0x20), v_stack_m270, result, (uint32_t)(v_stack_m280));
loc_008B4044:
    if (result == 0) goto loc_008B4067;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m288 + 0x8) + 0x20) + 0x8C)) & (1)) != 0) goto loc_008B44F4;
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(v_stack_m288 + 0x8) + 0x20), v_stack_m258, result, (uint32_t)(v_stack_m280));
loc_008B4067:
    if (v_stack_m297 != 0) {
        Arg1 = *(uint64_t *)(v_stack_m288 + 0x8);
        result = CmpUnlockKcb(Arg1, v_stack_m258, result, (uint32_t)(v_stack_m280));
    }
    result = CmpUnlockRegistry(Arg1, v_stack_m258, result, (uint32_t)(v_stack_m280));
loc_008B4083:
    result = CmpDetachFromRegistryProcess(v_stack_mF8, v_stack_m258, result, (uint32_t)(v_stack_m280));
    if (sign_flag) goto loc_008B4435;
loc_008B4090:
    *(uint32_t *)(v_stack_m268) = (uint32_t)((uint32_t)(v_stack_m27C));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000023ULL) goto loc_008B40CB;
    local_r13 = (uint32_t)(Arg5);
    if (((uint32_t)((uint32_t)(Arg5))) >= ((uint32_t)((uint32_t)(v_stack_m27C)))) {
        local_r13 = (uint32_t)((uint32_t)(v_stack_m27C));
    }
    result = (uint32_t)(v_stack_m27C);
    if (v_stack_m178 != v_stack_m170) {
        Arg3 = (uint32_t)(local_r13);
        result = memcpy(v_stack_m178, v_stack_m170, Arg3, (uint32_t)(v_stack_m280));
    }
    goto loc_008B40FC;
loc_008B40FC:
    if (v_stack_m250 != 0) {
        result = ObfDereferenceObject(v_stack_m250, v_stack_m170, Arg3, (uint32_t)(v_stack_m280));
    }
    if (v_stack_m296 == 0) goto loc_008B41C9;
    if ((*(uint32_t *)(v_rip + 0x63BA68)) == 0) goto loc_008B41C9;
    result = CmpIsRegistryLockAcquired(v_stack_m250, v_stack_m170, Arg3, (uint32_t)(v_stack_m280));
    if ((uint32_t)(result) != 0) goto loc_008B41C9;
    result = v_stack_m238;
    local_rbx = (uint32_t)((uint32_t)(result));
    if (v_stack_m238 != v_stack_m238) {
        v_stack_m204 = 0;
        v_stack_m1F4 = v_xmm0;
        v_stack_m1E4 = 0;
        v_stack_m1DC = 0;
        v_stack_m210 = v_stack_m288;
        v_stack_m208 = (uint32_t)((uint32_t)((uint32_t)(result)));
        v_stack_m1F8 = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = v_stack_m1B8;
        v_stack_m200 = result;
        result = v_stack_m238;
        v_stack_m2B8 = result;
        v_stack_m2C0 = v_stack_m288;
        v_stack_m2C8 = 21;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_stack_m210;
        Arg1 = Arg4 + 21;
        result = CmpCallCallBacksEx(Arg1, Arg2, Arg3, Arg4);
        local_rbx = v_stack_m1F8;
    }
    local_rdi = v_stack_m288;
    if (v_stack_m295 != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = KeLeaveCriticalRegionThread(Arg1, Arg2, Arg3, Arg4);
        local_rdi = v_stack_m288;
    }
    if (local_rdi != 0) {
        Arg1 = local_rdi;
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m170 == 0) goto loc_008B4214;
    if (v_stack_m170 == v_stack_m178) goto loc_008B4214;
    if (v_stack_m170 != v_stack_m167) goto loc_008B4261;
loc_008B4214:
    if (*(uint64_t *)(v_rip + 0x723DED) != 0) goto loc_008B447C;
loc_008B4224:
    result = *(uint64_t *)(v_rip + 0x723DED);
    if ((uint8_t)(v_stack_m298) != 0) {
        result = CmpReleaseShutdownRundown(Arg1, v_stack_m170, Arg3, Arg4);
    }
    result = CmCleanupThreadInfo(v_stack_m1D8, v_stack_m170, Arg3, Arg4);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m170, Arg3, Arg4);
    local_rsp = (local_rsp) + (688);
    return result;
loc_008B4261:
    if (((v_stack_p180) & (1)) == 0) goto loc_008B4515;
    result = ExFreeToLookasideListEx(v_rip + 5736394, v_stack_m170, Arg3, Arg4);
    goto loc_008B4214;
loc_008B427D:
    if (local_rbx > 0x1000ULL) goto loc_008B43CA;
    result = ExAllocateFromLookasideListEx(v_rip + 5736367, v_stack_m170, Arg3, Arg4);
    if (result == 0) goto loc_008B43CA;
    Arg2 = 0;
    result = memset(result, Arg2, local_rbx, Arg4);
    v_stack_p178 = result;
    goto loc_008B3EB0;
loc_008B42C4:
    goto loc_008B3D82;
loc_008B42D9:
    result = HvpGetCellPaged(result, Arg2, local_rbx, Arg4);
    goto loc_008B3FCE;
loc_008B42E3:
    result = HvpGetCellPaged(result, Arg2, local_rbx, Arg4);
    goto loc_008B3FF1;
loc_008B42ED:
loc_008B42F2:
    goto loc_008B40FC;
loc_008B42FA:
    if (((*(uint8_t *)(v_rip + 0x555C67)) & (4)) != 0) goto loc_008B45A1;
loc_008B4307:
    result = 0;
loc_008B4309:
    if (0 == 0) goto loc_008B3E84;
    v_stack_pC0 = 0;
    v_stack_p270 = v_stack_pC0;
    v_stack_p278 = 8;
    v_stack_p58 = 1;
    v_stack_p280 = v_stack_p58;
    v_stack_p288 = 1;
    if ((((uint32_t)((uint32_t)(Arg5))) & ((uint32_t)((uint32_t)(Arg5) - 1))) == 0) goto loc_008B4379;
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_008B4372;
loc_008B436C:
    Arg1 = (uint32_t)(((uint32_t)(0xFFFFFFFFULL)) + 1);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) >> (1));
    if (condition_is_not_equal) goto loc_008B436C;
loc_008B4372:
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = (uint32_t)((0) << ((uint8_t)(Arg1)));
loc_008B4379:
    v_stack_pC8 = (uint32_t)(Arg2);
    v_stack_p290 = v_stack_pC8;
    v_stack_p298 = 8;
    v_stack_p20 = v_stack_p250;
    result = tlgWriteAgg(v_rip + 5594008, v_rip - 8773949, local_rbx, 5);
    goto loc_008B3E84;
loc_008B43CA:
    result = CmpAllocateTransientPoolWithQuota(v_rip + 5594008, (uint32_t)(0xC0000189ULL), (uint32_t)(0x42424D43ULL), 5);
    if (result != 0) goto loc_008B3EA8;
    goto loc_008B3EB2;
loc_008B43EB:
loc_008B43F0:
    goto loc_008B4024;
loc_008B43F8:
    v_stack_p28 = v_stack_p6C;
    v_stack_p20 = (uint32_t)((uint32_t)(Arg5));
    result = CmEnumerateValueFromLayeredKey(result, (uint32_t)(v_stack_p54), (uint32_t)(v_stack_p68), (uint32_t)(0x8000001AULL));
    goto loc_008B4024;
loc_008B4425:
    goto loc_008B42F2;
loc_008B4435:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0x80000005ULL) goto loc_008B4090;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000023ULL) goto loc_008B4090;
    goto loc_008B40FC;
loc_008B4462:
    goto loc_008B40FC;
loc_008B447C:
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p70;
    if (result != (v_rip - 334595)) goto loc_008B46A6;
    result = EtwpTraceRegistry(18, v_stack_p1D0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(v_stack_p54))));
    goto loc_008B4224;
loc_008B44B0:
    if (result <= result) goto loc_008B3E77;
loc_008B44C3:
    v_stack_p178 = result;
    goto loc_008B3EB0;
loc_008B44D0:
    if (v_stack_p60 == 0) goto loc_008B3D01;
    v_stack_p70 = *(uint64_t *)(v_stack_p60 + 0x8);
    v_stack_pA8 = *(uint64_t *)(v_stack_p60 + 0x8);
    goto loc_008B3D01;
loc_008B44F4:
    result = HvpReleaseCellFlat(18, v_stack_p1D0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(v_stack_p54))));
    goto loc_008B4067;
loc_008B44FE:
    result = HvpReleaseCellFlat(18, v_stack_p1D0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(v_stack_p54))));
    goto loc_008B4044;
loc_008B4508:
    v_stack_p178 = 0;
    goto loc_008B3EB0;
loc_008B4515:
    result = CmSiFreeMemory(v_stack_p178, v_stack_p1D0, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(v_stack_p54))));
    goto loc_008B4214;
loc_008B4527:
    if ((*(uint64_t *)(v_rip + 0x723ADA)) == 0) goto loc_008B469E;
    if ((uint32_t)((uint32_t)(result)) == 0) goto loc_008B469E;
    v_stack_p80 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p80;
    Arg2 = 0;
    result = ObReferenceObjectByHandle((uint32_t)((uint32_t)(result)), Arg2, *(uint64_t *)(v_rip + 0x71256B), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (sign_flag) goto loc_008B4699;
    result = ObfDereferenceObject(v_stack_p80, Arg2, *(uint64_t *)(v_rip + 0x71256B), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
loc_008B4597:
    goto loc_008B40FC;
loc_008B45A1:
    result = (uint32_t)((*(uint64_t *)(v_rip + 0x5559C8)) & (4));
    if (result != (*(uint64_t *)(v_rip + 0x5559BE))) goto loc_008B4307;
    goto loc_008B4309;
loc_008B45BF:
    result = CmpAttachToRegistryProcess(v_stack_p220, Arg2, *(uint64_t *)(v_rip + 0x71256B), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_p40 = 0;
    v_stack_p38 = v_stack_p6C;
    v_stack_p30 = (uint32_t)((uint32_t)(v_stack_p54));
    v_stack_p28 = v_stack_p178;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_p68));
    Arg3 = 0;
    result = CmEnumerateValueKeyFromMergedView(v_stack_p60, v_stack_p98, Arg3, (uint32_t)(v_stack_p54));
    goto loc_008B4083;
loc_008B4621:
    if (((uint32_t)(result)) != 0xC0000503ULL) goto loc_008B40FC;
    goto loc_008B40FC;
loc_008B4643:
    if (v_stack_p70 != (*(uint64_t *)(v_stack_p50 + 0x120))) goto loc_008B3F98;
    goto loc_008B3F9D;
loc_008B465A:
    result = CmpTransSearchAddTransFromKeyBody(v_stack_p60, v_stack_pA0, Arg3, (uint32_t)(v_stack_p54));
    if (sign_flag) goto loc_008B43F0;
    result = CmpPerformKeyBodyDeletionCheck(v_stack_p60, v_stack_pA0, Arg3, (uint32_t)(v_stack_p54));
    if (!sign_flag) goto loc_008B3F8F;
    goto loc_008B4024;
loc_008B4699:
loc_008B469E:
    goto loc_008B4597;
loc_008B46A6:
    result = guard_dispatch_icall(v_stack_p60, v_stack_pA0, Arg3, (uint32_t)(v_stack_p54));
    goto loc_008B4224;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008B3B50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
