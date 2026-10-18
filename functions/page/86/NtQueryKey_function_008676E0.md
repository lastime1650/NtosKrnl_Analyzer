# NtQueryKey

- RVA: `0x008676E0`–`0x0086802B` (길이 `2,379` bytes)
- VA: `0x00000001408676E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006BC7C`
- 디코드: `487`개 명령, `2,379/2,379` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x008677AA` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (function, `0x0039FC50`)
- `0x0086781A` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x00867827` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (function, `0x00BC9400`)
- `0x008678B8` → [ExRaiseAccessViolation](../8E/ExRaiseAccessViolation_function_008E9240.md) (function, `0x008E9240`)
- `0x008678BE` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00867934` → [ObReferenceObjectByHandle](ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x008679A7` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x00867A12` → [CmpCallCallBacksEx](CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x00867A7B` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00867A98` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x00867B34` → [CmpCallCallBacksEx](CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x00867B54` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00867B67` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00867BA7` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x00867BB4` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x00867BC6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00867BF4` → [ExFreeToLookasideListEx](../../text/38/ExFreeToLookasideListEx_function_0038ACC0.md) (function, `0x0038ACC0`)
- `0x00867C15` → [CmKeyBodyRemapToVirtualForEnum](../8B/CmKeyBodyRemapToVirtualForEnum_function_008B46C0.md) (function, `0x008B46C0`)
- `0x00867C77` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00867CC1` → [CmQueryKey](../85/CmQueryKey_function_00858240.md) (function, `0x00858240`)
- `0x00867D07` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00867D41` → [ExAllocateFromLookasideListEx](../../text/3C/ExAllocateFromLookasideListEx_function_003CD390.md) (function, `0x003CD390`)
- `0x00867D5A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00867DAE` → [EtwpTraceRegistry](EtwpTraceRegistry_function_00862980.md) (function, `0x00862980`)
- `0x00867E8F` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (function, `0x002F0F7C`)
- `0x00867EA2` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (function, `0x00461190`)
- `0x00867F07` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00867FB3` → [ObReferenceObjectByHandle](ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00867FCA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00868021` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PiDevCfgFindDeviceMigrationNode](../73/PiDevCfgFindDeviceMigrationNode_function_00732920.md) at `0x00732A12`
- [PiDevCfgQueryPolicyStringList](../73/PiDevCfgQueryPolicyStringList_function_00735358.md) at `0x0073543C`
- [ExpWatchLicenseInfoWork](../7C/ExpWatchLicenseInfoWork_function_007C6DB0.md) at `0x007C6EA5`
- [IopLoadDriver](../99/IopLoadDriver_function_00997B54.md) at `0x00997C19`
- [IopLoadDriver](../99/IopLoadDriver_function_00997B54.md) at `0x00997C60`
- [PiDevCfgConfigureDeviceLocation](../AA/PiDevCfgConfigureDeviceLocation_function_00AA88C0.md) at `0x00AA89CB`
- [ExpWatchProductTypeInitialization](../../init/C5/ExpWatchProductTypeInitialization_function_00C52170.md) at `0x00C527BB`

### Static image references
- `0x008676F3` → RVA `0x00E0A740` (`.data`; read)
- `0x00867794` → RVA `0x00FD8008` (`PAGEDATA`; read)
- `0x00867907` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)
- `0x0086799A` → RVA `0x00EEFB88` (`.data`; read)
- `0x00867BED` → RVA `0x00E2CA40` (`.data`; read)
- `0x00867C3C` → RVA `0x00EF7208` (`.data`; read)
- `0x00867C53` → RVA `0x00E09F58` (`.data`; read)
- `0x00867D7F` → RVA `0x00862980` (`EtwpTraceRegistry`; read)
- `0x00867DC6` → RVA `0x00E09F68` (`.data`; read)
- `0x00867E81` → RVA `0x0005627C` (`.rdata`; read)
- `0x00867FED` → RVA `0x00E09F70` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x008677AA` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (`PAGE` → `.text`)
  - `0x0086781A` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x00867827` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (`PAGE` → `PAGECMRC`)
  - `0x008679A7` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x00867A7B` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00867A98` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x00867B54` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00867B67` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00867BA7` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x00867BB4` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x00867BC6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00867BF4` → [ExFreeToLookasideListEx](../../text/38/ExFreeToLookasideListEx_function_0038ACC0.md) (`PAGE` → `.text`)
  - `0x00867C77` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00867D07` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00867D41` → [ExAllocateFromLookasideListEx](../../text/3C/ExAllocateFromLookasideListEx_function_003CD390.md) (`PAGE` → `.text`)
  - `0x00867D5A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00867E8F` → [tlgWriteAgg](../../text/2F/tlgWriteAgg_function_002F0F7C.md) (`PAGE` → `.text`)
  - `0x00867EA2` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (`PAGE` → `.text`)
  - `0x00867F07` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00867FCA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00868021` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008676E0  40 53                           push rbx
008676E2  56                              push rsi
008676E3  57                              push rdi
008676E4  41 54                           push r12
008676E6  41 55                           push r13
008676E8  41 56                           push r14
008676EA  41 57                           push r15
008676EC  48 81 EC 30 02 00 00            sub rsp, 0x230
008676F3  48 8B 05 46 30 5A 00            mov rax, qword ptr [rip + 0x5a3046]
008676FA  48 33 C4                        xor rax, rsp
008676FD  48 89 84 24 20 02 00 00         mov qword ptr [rsp + 0x220], rax
00867705  45 8B E1                        mov r12d, r9d
00867708  49 8B F0                        mov rsi, r8
0086770B  44 8B FA                        mov r15d, edx
0086770E  48 8B D9                        mov rbx, rcx
00867711  4C 8B B4 24 90 02 00 00         mov r14, qword ptr [rsp + 0x290]
00867719  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
0086771E  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00867722  0F 57 C0                        xorps xmm0, xmm0
00867725  33 C0                           xor eax, eax
00867727  0F 11 84 24 30 01 00 00         movups xmmword ptr [rsp + 0x130], xmm0
0086772F  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
00867737  33 FF                           xor edi, edi
00867739  48 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdi
00867741  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
00867745  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
00867749  0F 11 84 24 61 01 00 00         movups xmmword ptr [rsp + 0x161], xmm0
00867751  0F 11 84 24 71 01 00 00         movups xmmword ptr [rsp + 0x171], xmm0
00867759  0F 11 84 24 81 01 00 00         movups xmmword ptr [rsp + 0x181], xmm0
00867761  0F 11 84 24 91 01 00 00         movups xmmword ptr [rsp + 0x191], xmm0
00867769  89 84 24 A1 01 00 00            mov dword ptr [rsp + 0x1a1], eax
00867770  66 89 84 24 A5 01 00 00         mov word ptr [rsp + 0x1a5], ax
00867778  88 84 24 A7 01 00 00            mov byte ptr [rsp + 0x1a7], al
0086777F  0F 11 84 24 B0 01 00 00         movups xmmword ptr [rsp + 0x1b0], xmm0
00867787  0F 11 84 24 C0 01 00 00         movups xmmword ptr [rsp + 0x1c0], xmm0
0086778F  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00867794  48 39 05 6D 08 77 00            cmp qword ptr [rip + 0x77086d], rax
0086779B  74 12                           je 0x1408677af
0086779D  BA 00 00 02 00                  mov edx, 0x20000
008677A2  48 8D 8C 24 B0 01 00 00         lea rcx, [rsp + 0x1b0]
008677AA  E8 A1 84 B3 FF                  call 0x14039fc50
008677AF  40 88 7C 24 45                  mov byte ptr [rsp + 0x45], dil
008677B4  40 88 7C 24 46                  mov byte ptr [rsp + 0x46], dil
008677B9  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
008677BE  0F 57 C0                        xorps xmm0, xmm0
008677C1  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
008677C9  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
008677D1  0F 11 84 24 10 01 00 00         movups xmmword ptr [rsp + 0x110], xmm0
008677D9  0F 11 84 24 20 01 00 00         movups xmmword ptr [rsp + 0x120], xmm0
008677E1  33 C0                           xor eax, eax
008677E3  0F 11 84 24 50 01 00 00         movups xmmword ptr [rsp + 0x150], xmm0
008677EB  88 84 24 60 01 00 00            mov byte ptr [rsp + 0x160], al
008677F2  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
008677FA  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00867802  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
0086780A  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00867812  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
0086781A  E8 51 46 B9 FF                  call 0x1403fbe70
0086781F  48 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdi
00867827  E8 D4 1B 36 00                  call 0x140bc9400
0086782C  88 44 24 48                     mov byte ptr [rsp + 0x48], al
00867830  84 C0                           test al, al
00867832  0F 84 EB 04 00 00               je 0x140867d23
00867838  41 83 FF 08                     cmp r15d, 8
0086783C  0F 87 32 07 00 00               ja 0x140867f74
00867842  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086784B  0F B6 88 32 02 00 00            movzx ecx, byte ptr [rax + 0x232]
00867852  88 4C 24 44                     mov byte ptr [rsp + 0x44], cl
00867856  80 F9 01                        cmp cl, 1
00867859  0F 85 96 00 00 00               jne 0x1408678f5
0086785F  45 85 E4                        test r12d, r12d
00867862  74 60                           je 0x1408678c4
00867864  48 8B C6                        mov rax, rsi
00867867  40 F6 C6 03                     test sil, 3
0086786B  75 51                           jne 0x1408678be
0086786D  48 8D 56 FF                     lea rdx, [rsi - 1]
00867871  49 03 D4                        add rdx, r12
00867874  48 3B F2                        cmp rsi, rdx
00867877  77 3F                           ja 0x1408678b8
00867879  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
00867883  49 3B D0                        cmp rdx, r8
00867886  73 30                           jae 0x1408678b8
00867888  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
0086788F  48 81 C2 00 10 00 00            add rdx, 0x1000
00867896  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
008678A0  0F B6 08                        movzx ecx, byte ptr [rax]
008678A3  88 08                           mov byte ptr [rax], cl
008678A5  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
008678AB  48 05 00 10 00 00               add rax, 0x1000
008678B1  48 3B C2                        cmp rax, rdx
008678B4  75 EA                           jne 0x1408678a0
008678B6  EB 17                           jmp 0x1408678cf
008678B8  E8 83 19 08 00                  call 0x1408e9240
008678BD  CC                              int3
008678BE  E8 0D 27 03 00                  call 0x140899fd0
008678C3  CC                              int3
008678C4  90                              nop
008678C5  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
008678CF  4D 3B F0                        cmp r14, r8
008678D2  4D 0F 42 C6                     cmovb r8, r14
008678D6  41 8B 00                        mov eax, dword ptr [r8]
008678D9  41 89 00                        mov dword ptr [r8], eax
008678DC  0F B6 4C 24 44                  movzx ecx, byte ptr [rsp + 0x44]
008678E1  EB 12                           jmp 0x1408678f5
008678E3  8B D8                           mov ebx, eax
008678E5  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008678E9  33 FF                           xor edi, edi
008678EB  44 8B 7C 24 50                  mov r15d, dword ptr [rsp + 0x50]
008678F0  E9 79 01 00 00                  jmp 0x140867a6e
008678F5  41 8D 47 FD                     lea eax, [r15 - 3]
008678F9  A9 FB FF FF FF                  test eax, 0xfffffffb
008678FE  0F 85 70 04 00 00               jne 0x140867d74
00867904  44 8B EF                        mov r13d, edi
00867907  4C 8B 05 B2 F1 75 00            mov r8, qword ptr [rip + 0x75f1b2]
0086790E  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
00867913  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
0086791B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00867920  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00867925  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0086792A  44 0F B6 C9                     movzx r9d, cl
0086792E  41 8B D5                        mov edx, r13d
00867931  48 8B CB                        mov rcx, rbx
00867934  E8 77 14 00 00                  call 0x140868db0
00867939  8B D8                           mov ebx, eax
0086793B  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00867940  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00867945  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00867949  85 DB                           test ebx, ebx
0086794B  0F 88 1D 01 00 00               js 0x140867a6e
00867951  81 38 32 30 79 6B               cmp dword ptr [rax], 0x6b793032
00867957  0F 85 B4 05 00 00               jne 0x140867f11
0086795D  48 83 3D A3 06 77 00 00         cmp qword ptr [rip + 0x7706a3], 0
00867965  0F 85 4D 04 00 00               jne 0x140867db8
0086796B  41 8D 47 FD                     lea eax, [r15 - 3]
0086796F  A9 FB FF FF FF                  test eax, 0xfffffffb
00867974  75 0E                           jne 0x140867984
00867976  83 BC 24 9C 00 00 00 00         cmp dword ptr [rsp + 0x9c], 0
0086797E  0F 84 55 06 00 00               je 0x140867fd9
00867984  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086798D  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00867994  90                              nop
00867995  C6 44 24 46 01                  mov byte ptr [rsp + 0x46], 1
0086799A  83 3D E7 81 68 00 00            cmp dword ptr [rip + 0x6881e7], 0
008679A1  0F 84 64 06 00 00               je 0x14086800b
008679A7  E8 D0 F0 BE FF                  call 0x140456a7c
008679AC  85 C0                           test eax, eax
008679AE  0F 85 57 06 00 00               jne 0x14086800b
008679B4  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
008679B9  4C 89 B4 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], r14
008679C1  44 89 BC 24 F8 00 00 00         mov dword ptr [rsp + 0xf8], r15d
008679C9  48 89 B4 24 00 01 00 00         mov qword ptr [rsp + 0x100], rsi
008679D1  44 89 A4 24 08 01 00 00         mov dword ptr [rsp + 0x108], r12d
008679D9  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
008679DE  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
008679E6  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
008679EE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008679F3  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
008679F8  C7 44 24 20 16 00 00 00         mov dword ptr [rsp + 0x20], 0x16
00867A00  41 B1 01                        mov r9b, 1
00867A03  45 33 C0                        xor r8d, r8d
00867A06  48 8D 94 24 F0 00 00 00         lea rdx, [rsp + 0xf0]
00867A0E  41 8D 48 07                     lea ecx, [r8 + 7]
00867A12  E8 29 E5 FF FF                  call 0x140865f40
00867A17  8B D8                           mov ebx, eax
00867A19  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00867A1D  85 C0                           test eax, eax
00867A1F  0F 88 95 04 00 00               js 0x140867eba
00867A25  C6 44 24 45 01                  mov byte ptr [rsp + 0x45], 1
00867A2A  41 83 FF 07                     cmp r15d, 7
00867A2E  0F 85 C7 01 00 00               jne 0x140867bfb
00867A34  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00867A39  C7 00 04 00 00 00               mov dword ptr [rax], 4
00867A3F  41 83 FC 04                     cmp r12d, 4
00867A43  73 0B                           jae 0x140867a50
00867A45  BB 23 00 00 C0                  mov ebx, 0xc0000023
00867A4A  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00867A4E  EB 1E                           jmp 0x140867a6e
00867A50  41 0F B7 46 32                  movzx eax, word ptr [r14 + 0x32]
00867A55  89 06                           mov dword ptr [rsi], eax
00867A57  EB 0F                           jmp 0x140867a68
00867A59  8B D8                           mov ebx, eax
00867A5B  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00867A5F  33 FF                           xor edi, edi
00867A61  44 8B 7C 24 50                  mov r15d, dword ptr [rsp + 0x50]
00867A66  EB 06                           jmp 0x140867a6e
00867A68  8B DF                           mov ebx, edi
00867A6A  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00867A6E  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00867A76  48 85 C9                        test rcx, rcx
00867A79  74 05                           je 0x140867a80
00867A7B  E8 D0 18 A9 FF                  call 0x1402f9350
00867A80  80 7C 24 45 00                  cmp byte ptr [rsp + 0x45], 0
00867A85  0F 84 B9 00 00 00               je 0x140867b44
00867A8B  83 3D F6 80 68 00 00            cmp dword ptr [rip + 0x6880f6], 0
00867A92  0F 84 A8 00 00 00               je 0x140867b40
00867A98  E8 DF EF BE FF                  call 0x140456a7c
00867A9D  85 C0                           test eax, eax
00867A9F  0F 85 9B 00 00 00               jne 0x140867b40
00867AA5  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00867AAD  48 39 84 24 88 00 00 00         cmp qword ptr [rsp + 0x88], rax
00867AB5  0F 84 85 00 00 00               je 0x140867b40
00867ABB  89 BC 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], edi
00867AC2  0F 57 C0                        xorps xmm0, xmm0
00867AC5  F3 0F 7F 84 24 CC 00 00 00      movdqu xmmword ptr [rsp + 0xcc], xmm0
00867ACE  48 89 BC 24 DC 00 00 00         mov qword ptr [rsp + 0xdc], rdi
00867AD6  89 BC 24 E4 00 00 00            mov dword ptr [rsp + 0xe4], edi
00867ADD  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00867AE2  48 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rcx
00867AEA  89 9C 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], ebx
00867AF1  89 9C 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], ebx
00867AF8  48 8D 84 24 F0 00 00 00         lea rax, [rsp + 0xf0]
00867B00  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
00867B08  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00867B10  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00867B15  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00867B1A  C7 44 24 20 16 00 00 00         mov dword ptr [rsp + 0x20], 0x16
00867B22  45 33 C9                        xor r9d, r9d
00867B25  45 33 C0                        xor r8d, r8d
00867B28  48 8D 94 24 B0 00 00 00         lea rdx, [rsp + 0xb0]
00867B30  41 8D 49 16                     lea ecx, [r9 + 0x16]
00867B34  E8 07 E4 FF FF                  call 0x140865f40
00867B39  8B 9C 24 C8 00 00 00            mov ebx, dword ptr [rsp + 0xc8]
00867B40  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00867B44  80 7C 24 46 00                  cmp byte ptr [rsp + 0x46], 0
00867B49  74 12                           je 0x140867b5d
00867B4B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00867B54  E8 97 74 9F FF                  call 0x14025eff0
00867B59  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
00867B5D  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00867B62  48 85 C9                        test rcx, rcx
00867B65  74 05                           je 0x140867b6c
00867B67  E8 E4 17 A9 FF                  call 0x1402f9350
00867B6C  48 8B 94 24 58 01 00 00         mov rdx, qword ptr [rsp + 0x158]
00867B74  48 85 D2                        test rdx, rdx
00867B77  74 17                           je 0x140867b90
00867B79  48 3B 94 24 50 01 00 00         cmp rdx, qword ptr [rsp + 0x150]
00867B81  74 0D                           je 0x140867b90
00867B83  48 8D 84 24 61 01 00 00         lea rax, [rsp + 0x161]
00867B8B  48 3B D0                        cmp rdx, rax
00867B8E  75 4F                           jne 0x140867bdf
00867B90  48 8B 05 71 04 77 00            mov rax, qword ptr [rip + 0x770471]
00867B97  48 85 C0                        test rax, rax
00867B9A  0F 85 DF 01 00 00               jne 0x140867d7f
00867BA0  80 7C 24 48 00                  cmp byte ptr [rsp + 0x48], 0
00867BA5  74 05                           je 0x140867bac
00867BA7  E8 D4 1C 36 00                  call 0x140bc9880
00867BAC  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
00867BB4  E8 97 81 BB FF                  call 0x14041fd50
00867BB9  8B C3                           mov eax, ebx
00867BBB  48 8B 8C 24 20 02 00 00         mov rcx, qword ptr [rsp + 0x220]
00867BC3  48 33 CC                        xor rcx, rsp
00867BC6  E8 75 4A E4 FF                  call 0x1406ac640
00867BCB  48 81 C4 30 02 00 00            add rsp, 0x230
00867BD2  41 5F                           pop r15
00867BD4  41 5E                           pop r14
00867BD6  41 5D                           pop r13
00867BD8  41 5C                           pop r12
00867BDA  5F                              pop rdi
00867BDB  5E                              pop rsi
00867BDC  5B                              pop rbx
00867BDD  C3                              ret
00867BDE  CC                              int3
00867BDF  F6 84 24 60 01 00 00 01         test byte ptr [rsp + 0x160], 1
00867BE7  0F 84 12 03 00 00               je 0x140867eff
00867BED  48 8D 0D 4C 4E 5C 00            lea rcx, [rip + 0x5c4e4c]
00867BF4  E8 C7 30 B2 FF                  call 0x14038acc0
00867BF9  EB 95                           jmp 0x140867b90
00867BFB  4C 8D 8C 24 80 00 00 00         lea r9, [rsp + 0x80]
00867C03  45 8B C5                        mov r8d, r13d
00867C06  44 0F B6 74 24 44               movzx r14d, byte ptr [rsp + 0x44]
00867C0C  41 0F B6 D6                     movzx edx, r14b
00867C10  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00867C15  E8 A6 CA 04 00                  call 0x1408b46c0
00867C1A  8B D8                           mov ebx, eax
00867C1C  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00867C20  85 C0                           test eax, eax
00867C22  0F 88 46 FE FF FF               js 0x140867a6e
00867C28  49 8B DC                        mov rbx, r12
00867C2B  48 89 B4 24 50 01 00 00         mov qword ptr [rsp + 0x150], rsi
00867C33  45 85 E4                        test r12d, r12d
00867C36  0F 84 2B 03 00 00               je 0x140867f67
00867C3C  48 83 3D C4 F5 68 00 00         cmp qword ptr [rip + 0x68f5c4], 0
00867C44  0F 84 1D 01 00 00               je 0x140867d67
00867C4A  45 84 F6                        test r14b, r14b
00867C4D  0F 84 94 02 00 00               je 0x140867ee7
00867C53  83 3D FE 22 5A 00 05            cmp dword ptr [rip + 0x5a22fe], 5
00867C5A  0F 87 66 01 00 00               ja 0x140867dc6
00867C60  48 83 FB 40                     cmp rbx, 0x40
00867C64  0F 87 C3 00 00 00               ja 0x140867d2d
00867C6A  4C 8B C3                        mov r8, rbx
00867C6D  33 D2                           xor edx, edx
00867C6F  48 8D 8C 24 61 01 00 00         lea rcx, [rsp + 0x161]
00867C77  E8 C4 EF E5 FF                  call 0x1406c6c40
00867C7C  48 8D 84 24 61 01 00 00         lea rax, [rsp + 0x161]
00867C84  48 89 84 24 58 01 00 00         mov qword ptr [rsp + 0x158], rax
00867C8C  8B DF                           mov ebx, edi
00867C8E  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00867C92  85 DB                           test ebx, ebx
00867C94  0F 88 D4 FD FF FF               js 0x140867a6e
00867C9A  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00867C9F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00867CA4  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00867CA9  4C 8B 8C 24 58 01 00 00         mov r9, qword ptr [rsp + 0x158]
00867CB1  45 8B C7                        mov r8d, r15d
00867CB4  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
00867CBC  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00867CC1  E8 7A 05 FF FF                  call 0x140858240
00867CC6  8B D8                           mov ebx, eax
00867CC8  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00867CCC  85 C0                           test eax, eax
00867CCE  0F 88 F6 01 00 00               js 0x140867eca
00867CD4  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00867CD8  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00867CDD  89 01                           mov dword ptr [rcx], eax
00867CDF  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
00867CE5  74 25                           je 0x140867d0c
00867CE7  44 3B E0                        cmp r12d, eax
00867CEA  72 03                           jb 0x140867cef
00867CEC  44 8B E0                        mov r12d, eax
00867CEF  48 8B 8C 24 50 01 00 00         mov rcx, qword ptr [rsp + 0x150]
00867CF7  48 8B 94 24 58 01 00 00         mov rdx, qword ptr [rsp + 0x158]
00867CFF  48 3B CA                        cmp rcx, rdx
00867D02  74 08                           je 0x140867d0c
00867D04  45 8B C4                        mov r8d, r12d
00867D07  E8 34 EB E5 FF                  call 0x1406c6840
00867D0C  E9 5D FD FF FF                  jmp 0x140867a6e
00867D11  8B D8                           mov ebx, eax
00867D13  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00867D17  33 FF                           xor edi, edi
00867D19  44 8B 7C 24 50                  mov r15d, dword ptr [rsp + 0x50]
00867D1E  E9 4B FD FF FF                  jmp 0x140867a6e
00867D23  BB 89 01 00 C0                  mov ebx, 0xc0000189
00867D28  E9 3D FD FF FF                  jmp 0x140867a6a
00867D2D  48 81 FB 00 10 00 00            cmp rbx, 0x1000
00867D34  0F 87 5F 01 00 00               ja 0x140867e99
00867D3A  48 8D 0D FF 4C 5C 00            lea rcx, [rip + 0x5c4cff]
00867D41  E8 4A 56 B6 FF                  call 0x1403cd390
00867D46  48 8B F0                        mov rsi, rax
00867D49  48 85 C0                        test rax, rax
00867D4C  0F 84 47 01 00 00               je 0x140867e99
00867D52  4C 8B C3                        mov r8, rbx
00867D55  33 D2                           xor edx, edx
00867D57  48 8B C8                        mov rcx, rax
00867D5A  E8 E1 EE E5 FF                  call 0x1406c6c40
00867D5F  80 8C 24 60 01 00 00 01         or byte ptr [rsp + 0x160], 1
00867D67  48 89 B4 24 58 01 00 00         mov qword ptr [rsp + 0x158], rsi
00867D6F  E9 18 FF FF FF                  jmp 0x140867c8c
00867D74  41 BD 01 00 00 00               mov r13d, 1
00867D7A  E9 88 FB FF FF                  jmp 0x140867907
00867D7F  48 8D 0D FA AB FF FF            lea rcx, [rip - 0x5406]
00867D86  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00867D8B  45 8B CF                        mov r9d, r15d
00867D8E  44 8B C3                        mov r8d, ebx
00867D91  48 8D 94 24 B0 01 00 00         lea rdx, [rsp + 0x1b0]
00867D99  48 3B C1                        cmp rax, rcx
00867D9C  0F 85 73 02 00 00               jne 0x140868015
00867DA2  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00867DA7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00867DAC  B1 0D                           mov cl, 0xd
00867DAE  E8 CD AB FF FF                  call 0x140862980
00867DB3  E9 E8 FD FF FF                  jmp 0x140867ba0
00867DB8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00867DBC  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00867DC1  E9 A5 FB FF FF                  jmp 0x14086796b
00867DC6  F6 05 9B 21 5A 00 04            test byte ptr [rip + 0x5a219b], 4
00867DCD  0F 85 1A 02 00 00               jne 0x140867fed
00867DD3  32 C0                           xor al, al
00867DD5  84 C0                           test al, al
00867DD7  0F 84 83 FE FF FF               je 0x140867c60
00867DDD  48 C7 84 24 A0 00 00 00 01 00 00 00  mov qword ptr [rsp + 0xa0], 1
00867DE9  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00867DF1  48 89 84 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rax
00867DF9  48 C7 84 24 F8 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x1f8], 8
00867E05  C6 44 24 47 02                  mov byte ptr [rsp + 0x47], 2
00867E0A  48 8D 44 24 47                  lea rax, [rsp + 0x47]
00867E0F  48 89 84 24 00 02 00 00         mov qword ptr [rsp + 0x200], rax
00867E17  48 C7 84 24 08 02 00 00 01 00 00 00  mov qword ptr [rsp + 0x208], 1
00867E23  41 8B D4                        mov edx, r12d
00867E26  41 8D 44 24 FF                  lea eax, [r12 - 1]
00867E2B  41 85 C4                        test r12d, eax
00867E2E  74 18                           je 0x140867e48
00867E30  B9 FF FF FF FF                  mov ecx, 0xffffffff
00867E35  85 D2                           test edx, edx
00867E37  74 06                           je 0x140867e3f
00867E39  FF C1                           inc ecx
00867E3B  D1 EA                           shr edx, 1
00867E3D  75 FA                           jne 0x140867e39
00867E3F  FF C1                           inc ecx
00867E41  BA 01 00 00 00                  mov edx, 1
00867E46  D3 E2                           shl edx, cl
00867E48  8B C2                           mov eax, edx
00867E4A  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00867E52  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
00867E5A  48 89 84 24 10 02 00 00         mov qword ptr [rsp + 0x210], rax
00867E62  48 C7 84 24 18 02 00 00 08 00 00 00  mov qword ptr [rsp + 0x218], 8
00867E6E  48 8D 84 24 D0 01 00 00         lea rax, [rsp + 0x1d0]
00867E76  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00867E7B  41 B9 05 00 00 00               mov r9d, 5
00867E81  48 8D 15 F4 E3 7E FF            lea rdx, [rip - 0x811c0c]
00867E88  48 8D 0D C9 20 5A 00            lea rcx, [rip + 0x5a20c9]
00867E8F  E8 E8 90 A8 FF                  call 0x1402f0f7c
00867E94  E9 C7 FD FF FF                  jmp 0x140867c60
00867E99  41 B8 43 4D 42 42               mov r8d, 0x42424d43
00867E9F  48 8B D3                        mov rdx, rbx
00867EA2  E8 E9 92 BF FF                  call 0x140461190
00867EA7  48 85 C0                        test rax, rax
00867EAA  0F 85 D4 FD FF FF               jne 0x140867c84
00867EB0  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00867EB5  E9 D4 FD FF FF                  jmp 0x140867c8e
00867EBA  3D 03 05 00 C0                  cmp eax, 0xc0000503
00867EBF  0F 84 A3 FB FF FF               je 0x140867a68
00867EC5  E9 A4 FB FF FF                  jmp 0x140867a6e
00867ECA  81 FB 05 00 00 80               cmp ebx, 0x80000005
00867ED0  0F 84 FE FD FF FF               je 0x140867cd4
00867ED6  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
00867EDC  0F 85 8C FB FF FF               jne 0x140867a6e
00867EE2  E9 ED FD FF FF                  jmp 0x140867cd4
00867EE7  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
00867EF1  48 3B F0                        cmp rsi, rax
00867EF4  0F 86 59 FD FF FF               jbe 0x140867c53
00867EFA  E9 68 FE FF FF                  jmp 0x140867d67
00867EFF  48 8B 8C 24 58 01 00 00         mov rcx, qword ptr [rsp + 0x158]
00867F07  E8 74 DE C0 FF                  call 0x140475d80
00867F0C  E9 7F FC FF FF                  jmp 0x140867b90
00867F11  41 83 FF 04                     cmp r15d, 4
00867F15  0F 85 C8 00 00 00               jne 0x140867fe3
00867F1B  41 C7 06 28 00 00 00            mov dword ptr [r14], 0x28
00867F22  41 83 FC 28                     cmp r12d, 0x28
00867F26  73 0E                           jae 0x140867f36
00867F28  BB 23 00 00 C0                  mov ebx, 0xc0000023
00867F2D  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00867F31  E9 38 FB FF FF                  jmp 0x140867a6e
00867F36  0F 57 C0                        xorps xmm0, xmm0
00867F39  33 C9                           xor ecx, ecx
00867F3B  0F 11 06                        movups xmmword ptr [rsi], xmm0
00867F3E  0F 11 46 10                     movups xmmword ptr [rsi + 0x10], xmm0
00867F42  48 89 4E 20                     mov qword ptr [rsi + 0x20], rcx
00867F46  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00867F4A  8B 48 60                        mov ecx, dword ptr [rax + 0x60]
00867F4D  89 4E 14                        mov dword ptr [rsi + 0x14], ecx
00867F50  E9 13 FB FF FF                  jmp 0x140867a68
00867F55  8B D8                           mov ebx, eax
00867F57  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00867F5B  33 FF                           xor edi, edi
00867F5D  44 8B 7C 24 50                  mov r15d, dword ptr [rsp + 0x50]
00867F62  E9 07 FB FF FF                  jmp 0x140867a6e
00867F67  48 89 BC 24 58 01 00 00         mov qword ptr [rsp + 0x158], rdi
00867F6F  E9 18 FD FF FF                  jmp 0x140867c8c
00867F74  48 39 3D 8D 00 77 00            cmp qword ptr [rip + 0x77008d], rdi
00867F7B  74 52                           je 0x140867fcf
00867F7D  48 85 DB                        test rbx, rbx
00867F80  74 4D                           je 0x140867fcf
00867F82  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00867F8B  44 0F B6 88 32 02 00 00         movzx r9d, byte ptr [rax + 0x232]
00867F93  4C 8B 05 26 EB 75 00            mov r8, qword ptr [rip + 0x75eb26]
00867F9A  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
00867F9F  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00867FA4  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00867FA9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00867FAE  33 D2                           xor edx, edx
00867FB0  48 8B CB                        mov rcx, rbx
00867FB3  E8 F8 0D 00 00                  call 0x140868db0
00867FB8  85 C0                           test eax, eax
00867FBA  78 13                           js 0x140867fcf
00867FBC  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00867FC1  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00867FC5  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00867FCA  E8 81 13 A9 FF                  call 0x1402f9350
00867FCF  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00867FD4  E9 91 FA FF FF                  jmp 0x140867a6a
00867FD9  BB 22 00 00 C0                  mov ebx, 0xc0000022
00867FDE  E9 87 FA FF FF                  jmp 0x140867a6a
00867FE3  BB 08 00 00 C0                  mov ebx, 0xc0000008
00867FE8  E9 7D FA FF FF                  jmp 0x140867a6a
00867FED  48 8B 05 7C 1F 5A 00            mov rax, qword ptr [rip + 0x5a1f7c]
00867FF4  83 E0 04                        and eax, 4
00867FF7  48 3B 05 72 1F 5A 00            cmp rax, qword ptr [rip + 0x5a1f72]
00867FFE  0F 85 CF FD FF FF               jne 0x140867dd3
00868004  B0 01                           mov al, 1
00868006  E9 CA FD FF FF                  jmp 0x140867dd5
0086800B  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
00868010  E9 15 FA FF FF                  jmp 0x140867a2a
00868015  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0086801A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0086801F  B1 0D                           mov cl, 0xd
00868021  E8 AA 2A E5 FF                  call 0x1406baad0
00868026  E9 75 FB FF FF                  jmp 0x140867ba0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtQueryKey(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m107;
    unsigned __int8 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m184;
    unsigned __int64 v_stack_m18C;
    unsigned __int64 v_stack_m19C;
    unsigned int v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned int v_stack_m1AC;
    unsigned int v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m1CC;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned int v_stack_m200;
    unsigned int v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned int v_stack_m218;
    unsigned __int8 v_stack_m220;
    unsigned __int8 v_stack_m222;
    unsigned __int8 v_stack_m223;
    unsigned __int8 v_stack_m224;
    unsigned int v_stack_m228;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int8 v_stack_mC1;
    unsigned __int16 v_stack_mC3;
    unsigned int v_stack_mC7;
    unsigned __int64 v_stack_mD7;
    unsigned __int64 v_stack_mE7;
    unsigned __int64 v_stack_mF7;
    unsigned __int64 v_stack_p150;
    unsigned __int64 v_stack_p158;
    unsigned __int8 v_stack_p160;
    unsigned __int64 v_stack_p161;
    unsigned __int64 v_stack_p1B0;
    unsigned __int64 v_stack_p1D0;
    unsigned __int64 v_stack_p1F0;
    unsigned __int64 v_stack_p1F8;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p200;
    unsigned __int64 v_stack_p208;
    unsigned __int64 v_stack_p210;
    unsigned __int64 v_stack_p218;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p40;
    unsigned __int8 v_stack_p44;
    unsigned __int8 v_stack_p47;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;

    v_rsp = (v_rsp) - (560);
    result = (*(unsigned __int64 *)(v_rip + 5910598)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m210 = a5;
    v_stack_m218 = a2;
    result = 0;
    v_stack_m138 = v_xmm0;
    v_stack_m128 = 0;
    v_rdi = 0;
    v_stack_m1D0 = 0;
    v_stack_m200 = 0;
    v_stack_m208 = 0;
    v_stack_m107 = v_xmm0;
    v_stack_mF7 = v_xmm0;
    v_stack_mE7 = v_xmm0;
    v_stack_mD7 = v_xmm0;
    v_stack_mC7 = 0;
    v_stack_mC3 = 0;
    v_stack_mC1 = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    v_stack_m1F0 = 0;
    if ((*(unsigned __int64 *)(v_rip + 7800941)) != 0) {
        a2 = 0x20000ULL;
        a1 = v_stack_mB8;
        result = EtwGetKernelTraceTimestamp(a1, a2, a3, a4);
    }
    v_stack_m223 = 0;
    v_stack_m222 = 0;
    v_stack_m1F8 = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m168 = v_xmm0;
    v_stack_m158 = v_xmm0;
    v_stack_m148 = v_xmm0;
    result = 0;
    v_stack_m118 = v_xmm0;
    v_stack_m108 = 0;
    v_stack_m1D8 = v_stack_m1E0;
    v_stack_m1E0 = v_stack_m1E0;
    result = CmpInitializeThreadInfo(v_stack_m138, a2, a3, a4);
    v_stack_m1E8 = 0;
    result = CmpAcquireShutdownRundown(v_stack_m138, a2, a3, a4);
    v_stack_m220 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_00867D23;
    if (((unsigned int)((unsigned int)(a2))) > 8) goto loc_00867F74;
    v_stack_m224 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) != 1) goto loc_008678F5;
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_008678C4;
    if ((((unsigned __int8)(a3)) & (3)) != 0) goto loc_008678BE;
    a2 = (a3 - 1) + ((unsigned int)(a4));
    if (a3 > a2) goto loc_008678B8;
    if (a2 >= a3) goto loc_008678B8;
    a2 = (a2) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a2) + (0x1000ULL);
loc_008678A0:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(*(unsigned __int8 *)(a3));
    result = (a3) & (0xFFFFFFFFFFFFF000ULL);
    result = (result) + (0x1000ULL);
    if (result != a2) goto loc_008678A0;
    goto loc_008678CF;
loc_008678B8:
    result = ExRaiseAccessViolation(*(unsigned __int8 *)(a3), a2, a3, a4);
loc_008678BE:
    result = ExRaiseDatatypeMisalignment(*(unsigned __int8 *)(a3), a2, a3, a4);
loc_008678C4:
loc_008678CF:
    if (a5 < a3) { a3 = a5; }
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
    goto loc_008678F5;
loc_008678F5:
    if ((((unsigned int)((unsigned int)(a2) - 3)) & (0xFFFFFFFBULL)) != 0) goto loc_00867D74;
loc_00867907:
    v_stack_m200 = 0;
    v_stack_m240 = v_stack_m1D0;
    v_stack_m248 = v_stack_m200;
    result = ObReferenceObjectByHandle(a1, 0, *(unsigned __int64 *)(v_rip + 7729586), (unsigned __int8)(v_stack_m224));
    v_stack_m1F8 = v_stack_m200;
    v_stack_m228 = (unsigned int)((unsigned int)((unsigned int)(result)));
    if (sign_flag) goto loc_00867A6E;
    if ((*(unsigned int *)(v_stack_m200)) != 0x6B793032ULL) goto loc_00867F11;
    if ((*(unsigned __int64 *)(v_rip + 7800483)) != 0) goto loc_00867DB8;
loc_0086796B:
    if ((((unsigned int)((unsigned int)(a2) - 3)) & (0xFFFFFFFBULL)) != 0) goto loc_00867984;
    if (v_stack_m1CC == 0) goto loc_00867FD9;
loc_00867984:
    v_stack_m222 = 1;
    if ((*(unsigned int *)(v_rip + 6848999)) == 0) goto loc_0086800B;
    result = CmpIsRegistryLockAcquired(a1, 0, *(unsigned __int64 *)(v_rip + 7729586), (unsigned __int8)(v_stack_m224));
    if ((unsigned int)(result) != 0) goto loc_0086800B;
    v_stack_m178 = v_stack_m200;
    v_stack_m170 = (unsigned int)((unsigned int)(a2));
    v_stack_m168 = a3;
    v_stack_m160 = (unsigned int)((unsigned int)(a4));
    v_stack_m158 = v_stack_m210;
    v_stack_m238 = v_stack_m1E0;
    v_stack_m240 = v_stack_m200;
    v_stack_m248 = 22;
    a3 = 0;
    result = CmpCallCallBacksEx(a3 + 7, v_stack_m178, a3, 1);
    v_stack_m228 = (unsigned int)(result);
    if (sign_flag) goto loc_00867EBA;
    v_stack_m223 = 1;
loc_00867A2A:
    if (((unsigned int)((unsigned int)(a2))) != 7) goto loc_00867BFB;
    *(unsigned int *)(v_stack_m210) = 4;
    if (((unsigned int)((unsigned int)(a4))) >= 4) goto loc_00867A50;
    v_stack_m228 = (unsigned int)((unsigned int)(0xC0000023ULL));
    goto loc_00867A6E;
loc_00867A50:
    *(unsigned int *)(a3) = (unsigned int)(*(unsigned __int16 *)(v_stack_m200 + 50));
    goto loc_00867A68;
loc_00867A68:
loc_00867A6A:
    v_stack_m228 = 0;
loc_00867A6E:
    result = *(unsigned __int16 *)(v_stack_m200 + 50);
    if (v_stack_m1E8 != 0) {
        result = ObfDereferenceObject(v_stack_m1E8, v_stack_m178, a3, 1);
    }
    if (v_stack_m223 == 0) goto loc_00867B44;
    if ((*(unsigned int *)(v_rip + 6848758)) == 0) goto loc_00867B40;
    result = CmpIsRegistryLockAcquired(v_stack_m1E8, v_stack_m178, a3, 1);
    if ((unsigned int)(result) != 0) goto loc_00867B40;
    result = v_stack_m1E0;
    v_rbx = 0;
    if (v_stack_m1E0 != v_stack_m1E0) {
        v_stack_m1AC = 0;
        v_stack_m19C = v_xmm0;
        v_stack_m18C = 0;
        v_stack_m184 = 0;
        a1 = v_stack_m1F8;
        v_stack_m1B8 = a1;
        v_stack_m1B0 = 0;
        v_stack_m1A0 = 0;
        result = v_stack_m178;
        v_stack_m1A8 = result;
        result = v_stack_m1E0;
        v_stack_m238 = result;
        v_stack_m240 = a1;
        v_stack_m248 = 22;
        a4 = 0;
        a3 = 0;
        a2 = v_stack_m1B8;
        a1 = a4 + 22;
        result = CmpCallCallBacksEx(a1, a2, a3, a4);
        v_rbx = v_stack_m1A0;
    }
    v_stack_m228 = (unsigned int)(v_rbx);
loc_00867B44:
    if (v_stack_m222 != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = KeLeaveCriticalRegionThread(a1, a2, a3, a4);
        v_rbx = v_stack_m228;
    }
    if (v_stack_m1F8 != 0) {
        result = ObfDereferenceObject(v_stack_m1F8, a2, a3, a4);
    }
    if (v_stack_m110 == 0) goto loc_00867B90;
    if (v_stack_m110 == v_stack_m118) goto loc_00867B90;
    if (v_stack_m110 != v_stack_m107) goto loc_00867BDF;
loc_00867B90:
    if (*(unsigned __int64 *)(v_rip + 7799921) != 0) goto loc_00867D7F;
loc_00867BA0:
    result = *(unsigned __int64 *)(v_rip + 7799921);
    if (v_stack_m220 != 0) {
        result = CmpReleaseShutdownRundown(v_stack_m1F8, v_stack_m110, a3, a4);
    }
    result = CmCleanupThreadInfo(v_stack_m138, v_stack_m110, a3, a4);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m110, a3, a4);
    v_rsp = (v_rsp) + (560);
    return result;
loc_00867BDF:
    if (((v_stack_p160) & (1)) == 0) goto loc_00867EFF;
    result = ExFreeToLookasideListEx(v_rip + 6049356, v_stack_m110, a3, a4);
    goto loc_00867B90;
loc_00867BFB:
    result = CmKeyBodyRemapToVirtualForEnum(v_stack_p70, (unsigned __int8)(v_stack_p44), 0, v_stack_p80);
    v_stack_p40 = (unsigned int)(result);
    if (sign_flag) goto loc_00867A6E;
    v_stack_p150 = 0;
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_00867F67;
    if ((*(unsigned __int64 *)(v_rip + 6878660)) == 0) goto loc_00867D67;
    if ((unsigned __int8)(v_stack_p44) == 0) goto loc_00867EE7;
loc_00867C53:
    if ((*(unsigned int *)(v_rip + 5907198)) > 5) goto loc_00867DC6;
loc_00867C60:
    if (((unsigned int)(a4)) > 64) goto loc_00867D2D;
    a2 = 0;
    result = memset(v_stack_p161, a2, (unsigned int)(a4), v_stack_p80);
loc_00867C84:
    v_stack_p158 = v_stack_p161;
loc_00867C8C:
loc_00867C8E:
    v_stack_p40 = 0;
    if (sign_flag) goto loc_00867A6E;
    v_stack_p28 = v_stack_p60;
    v_stack_p20 = (unsigned int)((unsigned int)(a4));
    result = CmQueryKey(v_stack_p70, v_stack_p80, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_p158);
    v_stack_p40 = (unsigned int)(result);
    if (sign_flag) goto loc_00867ECA;
loc_00867CD4:
    *(unsigned int *)(v_stack_p58) = (unsigned int)((unsigned int)(v_stack_p60));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000023ULL) goto loc_00867D0C;
    v_r12 = (unsigned int)(a4);
    if (((unsigned int)((unsigned int)(a4))) >= ((unsigned int)((unsigned int)(v_stack_p60)))) {
        v_r12 = (unsigned int)((unsigned int)(v_stack_p60));
    }
    result = (unsigned int)(v_stack_p60);
    if (v_stack_p150 != v_stack_p158) {
        a3 = (unsigned int)(v_r12);
        result = memcpy(v_stack_p150, v_stack_p158, a3, v_stack_p158);
    }
    goto loc_00867A6E;
loc_00867D23:
    goto loc_00867A6A;
loc_00867D2D:
    if (((unsigned int)(0xC0000189ULL)) > 0x1000ULL) goto loc_00867E99;
    result = ExAllocateFromLookasideListEx(v_rip + 6049023, v_stack_p158, a3, v_stack_p158);
    if (result == 0) goto loc_00867E99;
    a2 = 0;
    result = memset(result, a2, (unsigned int)(0xC0000189ULL), v_stack_p158);
loc_00867D67:
    v_stack_p158 = result;
    goto loc_00867C8C;
loc_00867D74:
    goto loc_00867907;
loc_00867D7F:
    v_stack_p28 = 0;
    if (result != (v_rip - 21510)) goto loc_00868015;
    v_stack_p20 = v_stack_p78;
    result = EtwpTraceRegistry(13, v_stack_p1B0, (unsigned int)((unsigned int)((unsigned int)(0xC0000189ULL))), (unsigned int)((unsigned int)((unsigned int)(a2))));
    goto loc_00867BA0;
loc_00867DB8:
    v_stack_p78 = *(unsigned __int64 *)(result + 8);
    goto loc_0086796B;
loc_00867DC6:
    if (((*(unsigned __int8 *)(v_rip + 5906843)) & (4)) != 0) goto loc_00867FED;
loc_00867DD3:
    result = 0;
loc_00867DD5:
    if (0 == 0) goto loc_00867C60;
    v_stack_pA0 = 1;
    v_stack_p1F0 = v_stack_pA0;
    v_stack_p1F8 = 8;
    v_stack_p47 = 2;
    v_stack_p200 = v_stack_p47;
    v_stack_p208 = 1;
    if ((((unsigned int)(v_r12)) & ((unsigned int)(v_r12 - 1))) == 0) goto loc_00867E48;
    if ((unsigned int)((unsigned int)((unsigned int)(v_r12))) == 0) goto loc_00867E3F;
loc_00867E39:
    a1 = (unsigned int)(((unsigned int)(0xFFFFFFFFULL)) + 1);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) >> (1));
    if (condition_is_not_equal) goto loc_00867E39;
loc_00867E3F:
    a1 = (unsigned int)((a1) + 1);
    a2 = (unsigned int)((1) << ((unsigned __int8)(a1)));
loc_00867E48:
    v_stack_pA8 = (unsigned int)(a2);
    v_stack_p210 = v_stack_pA8;
    v_stack_p218 = 8;
    v_stack_p20 = v_stack_p1D0;
    result = tlgWriteAgg(v_rip + 5906633, v_rip - 8461324, (unsigned int)((unsigned int)((unsigned int)(0xC0000189ULL))), 5);
    goto loc_00867C60;
loc_00867E99:
    result = CmpAllocateTransientPoolWithQuota(v_rip + 5906633, (unsigned int)(0xC0000189ULL), (unsigned int)(0x42424D43ULL), 5);
    if (result != 0) goto loc_00867C84;
    goto loc_00867C8E;
loc_00867EBA:
    if (((unsigned int)(result)) == 0xC0000503ULL) goto loc_00867A68;
    goto loc_00867A6E;
loc_00867ECA:
    if (((unsigned int)((unsigned int)(0xC000009AULL))) == 0x80000005ULL) goto loc_00867CD4;
    if (((unsigned int)((unsigned int)(0xC000009AULL))) != 0xC0000023ULL) goto loc_00867A6E;
    goto loc_00867CD4;
loc_00867EE7:
    if (result <= result) goto loc_00867C53;
    goto loc_00867D67;
loc_00867EFF:
    result = CmSiFreeMemory(v_stack_p158, (unsigned int)(0xC0000189ULL), (unsigned int)(0x42424D43ULL), 5);
    goto loc_00867B90;
loc_00867F11:
    if (((unsigned int)((unsigned int)(a2))) != 4) goto loc_00867FE3;
    *(unsigned int *)(v_stack_p44) = 40;
    if (((unsigned int)(v_r12)) >= 40) goto loc_00867F36;
    v_stack_p40 = (unsigned int)((unsigned int)(0xC0000023ULL));
    goto loc_00867A6E;
loc_00867F36:
    a1 = 0;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = 0;
    *(unsigned int *)(result + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 8) + 96)));
    goto loc_00867A68;
loc_00867F67:
    v_stack_p158 = 0;
    goto loc_00867C8C;
loc_00867F74:
    if ((*(unsigned __int64 *)(v_rip + 7798925)) == 0) goto loc_00867FCF;
    if ((unsigned int)(0xC0000023ULL) == 0) goto loc_00867FCF;
    v_stack_p58 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p58;
    a2 = 0;
    result = ObReferenceObjectByHandle((unsigned int)(0xC0000023ULL), a2, *(unsigned __int64 *)(v_rip + 7727910), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (!(sign_flag)) {
        a1 = v_stack_p58;
        result = *(unsigned __int64 *)(a1 + 8);
        v_stack_p78 = result;
        result = ObfDereferenceObject(a1, a2, *(unsigned __int64 *)(v_rip + 7727910), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    }
    goto loc_00867A6A;
loc_00867FD9:
    goto loc_00867A6A;
loc_00867FE3:
    goto loc_00867A6A;
loc_00867FED:
    result = (unsigned int)((*(unsigned __int64 *)(v_rip + 5906300)) & (4));
    if (result != (*(unsigned __int64 *)(v_rip + 5906290))) goto loc_00867DD3;
    goto loc_00867DD5;
loc_0086800B:
    goto loc_00867A2A;
loc_00868015:
    v_stack_p20 = v_stack_p78;
    result = guard_dispatch_icall(13, a2, *(unsigned __int64 *)(v_rip + 7727910), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    goto loc_00867BA0;
}
```

## 5. (Beta) C Style

```c
int64_t NtQueryKey(int64_t Arg1, int32_t Arg2, void *Arg3, int32_t Arg4, int64_t Arg5)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m107;
    uint8_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m128;
    uint64_t v_stack_m138;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint32_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m184;
    uint64_t v_stack_m18C;
    uint64_t v_stack_m19C;
    uint32_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint32_t v_stack_m1AC;
    uint32_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m1CC;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint32_t v_stack_m200;
    uint32_t v_stack_m208;
    uint64_t v_stack_m210;
    uint32_t v_stack_m218;
    uint8_t v_stack_m220;
    uint8_t v_stack_m222;
    uint8_t v_stack_m223;
    uint8_t v_stack_m224;
    uint32_t v_stack_m228;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m48;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint8_t v_stack_mC1;
    uint16_t v_stack_mC3;
    uint32_t v_stack_mC7;
    uint64_t v_stack_mD7;
    uint64_t v_stack_mE7;
    uint64_t v_stack_mF7;
    uint64_t v_stack_p150;
    uint64_t v_stack_p158;
    uint8_t v_stack_p160;
    uint64_t v_stack_p161;
    uint64_t v_stack_p1B0;
    uint64_t v_stack_p1D0;
    uint64_t v_stack_p1F0;
    uint64_t v_stack_p1F8;
    uint32_t v_stack_p20;
    uint64_t v_stack_p200;
    uint64_t v_stack_p208;
    uint64_t v_stack_p210;
    uint64_t v_stack_p218;
    uint64_t v_stack_p28;
    uint32_t v_stack_p40;
    uint8_t v_stack_p44;
    uint8_t v_stack_p47;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;

    local_rsp = (local_rsp) - (560);
    result = (*(uint64_t *)(v_rip + 0x5A3046)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m210 = Arg5;
    v_stack_m218 = Arg2;
    result = 0;
    v_stack_m138 = v_xmm0;
    v_stack_m128 = 0;
    local_rdi = 0;
    v_stack_m1D0 = 0;
    v_stack_m200 = 0;
    v_stack_m208 = 0;
    v_stack_m107 = v_xmm0;
    v_stack_mF7 = v_xmm0;
    v_stack_mE7 = v_xmm0;
    v_stack_mD7 = v_xmm0;
    v_stack_mC7 = 0;
    v_stack_mC3 = 0;
    v_stack_mC1 = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    v_stack_m1F0 = 0;
    if ((*(uint64_t *)(v_rip + 0x77086D)) != 0) {
        Arg2 = 0x20000ULL;
        Arg1 = v_stack_mB8;
        result = EtwGetKernelTraceTimestamp(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m223 = 0;
    v_stack_m222 = 0;
    v_stack_m1F8 = 0;
    v_stack_m178 = v_xmm0;
    v_stack_m168 = v_xmm0;
    v_stack_m158 = v_xmm0;
    v_stack_m148 = v_xmm0;
    result = 0;
    v_stack_m118 = v_xmm0;
    v_stack_m108 = 0;
    v_stack_m1D8 = v_stack_m1E0;
    v_stack_m1E0 = v_stack_m1E0;
    result = CmpInitializeThreadInfo(v_stack_m138, Arg2, Arg3, Arg4);
    v_stack_m1E8 = 0;
    result = CmpAcquireShutdownRundown(v_stack_m138, Arg2, Arg3, Arg4);
    v_stack_m220 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_00867D23;
    if (((uint32_t)((uint32_t)(Arg2))) > 8) goto loc_00867F74;
    v_stack_m224 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) != 1) goto loc_008678F5;
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_008678C4;
    if ((((uint8_t)(Arg3)) & (3)) != 0) goto loc_008678BE;
    Arg2 = (Arg3 - 1) + ((uint32_t)(Arg4));
    if (Arg3 > Arg2) goto loc_008678B8;
    if (Arg2 >= Arg3) goto loc_008678B8;
    Arg2 = (Arg2) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (Arg2) + (0x1000ULL);
loc_008678A0:
    *(uint8_t *)(arg3) = (uint8_t)(*(uint8_t *)(arg3));
    result = (Arg3) & (0xFFFFFFFFFFFFF000ULL);
    result = (result) + (0x1000ULL);
    if (result != Arg2) goto loc_008678A0;
    goto loc_008678CF;
loc_008678B8:
    result = ExRaiseAccessViolation(*(uint8_t *)(arg3), Arg2, Arg3, Arg4);
loc_008678BE:
    result = ExRaiseDatatypeMisalignment(*(uint8_t *)(arg3), Arg2, Arg3, Arg4);
loc_008678C4:
loc_008678CF:
    if (Arg5 < Arg3) { Arg3 = Arg5; }
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(arg3)));
    goto loc_008678F5;
loc_008678F5:
    if ((((uint32_t)((uint32_t)(Arg2) - 3)) & (0xFFFFFFFBULL)) != 0) goto loc_00867D74;
loc_00867907:
    v_stack_m200 = 0;
    v_stack_m240 = v_stack_m1D0;
    v_stack_m248 = v_stack_m200;
    result = ObReferenceObjectByHandle(Arg1, 0, *(uint64_t *)(v_rip + 0x75F1B2), (uint8_t)(v_stack_m224));
    v_stack_m1F8 = v_stack_m200;
    v_stack_m228 = (uint32_t)((uint32_t)((uint32_t)(result)));
    if (sign_flag) goto loc_00867A6E;
    if ((*(uint32_t *)(v_stack_m200)) != 0x6B793032ULL) goto loc_00867F11;
    if ((*(uint64_t *)(v_rip + 0x7706A3)) != 0) goto loc_00867DB8;
loc_0086796B:
    if ((((uint32_t)((uint32_t)(Arg2) - 3)) & (0xFFFFFFFBULL)) != 0) goto loc_00867984;
    if (v_stack_m1CC == 0) goto loc_00867FD9;
loc_00867984:
    v_stack_m222 = 1;
    if ((*(uint32_t *)(v_rip + 0x6881E7)) == 0) goto loc_0086800B;
    result = CmpIsRegistryLockAcquired(Arg1, 0, *(uint64_t *)(v_rip + 0x75F1B2), (uint8_t)(v_stack_m224));
    if ((uint32_t)(result) != 0) goto loc_0086800B;
    v_stack_m178 = v_stack_m200;
    v_stack_m170 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m168 = Arg3;
    v_stack_m160 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m158 = v_stack_m210;
    v_stack_m238 = v_stack_m1E0;
    v_stack_m240 = v_stack_m200;
    v_stack_m248 = 22;
    Arg3 = 0;
    result = CmpCallCallBacksEx(Arg3 + 7, v_stack_m178, Arg3, 1);
    v_stack_m228 = (uint32_t)(result);
    if (sign_flag) goto loc_00867EBA;
    v_stack_m223 = 1;
loc_00867A2A:
    if (((uint32_t)((uint32_t)(Arg2))) != 7) goto loc_00867BFB;
    *(uint32_t *)(v_stack_m210) = 4;
    if (((uint32_t)((uint32_t)(Arg4))) >= 4) goto loc_00867A50;
    v_stack_m228 = (uint32_t)((uint32_t)(0xC0000023ULL));
    goto loc_00867A6E;
loc_00867A50:
    *(uint32_t *)(arg3) = (uint32_t)(*(uint16_t *)(v_stack_m200 + 0x32));
    goto loc_00867A68;
loc_00867A68:
loc_00867A6A:
    v_stack_m228 = 0;
loc_00867A6E:
    result = *(uint16_t *)(v_stack_m200 + 0x32);
    if (v_stack_m1E8 != 0) {
        result = ObfDereferenceObject(v_stack_m1E8, v_stack_m178, Arg3, 1);
    }
    if (v_stack_m223 == 0) goto loc_00867B44;
    if ((*(uint32_t *)(v_rip + 0x6880F6)) == 0) goto loc_00867B40;
    result = CmpIsRegistryLockAcquired(v_stack_m1E8, v_stack_m178, Arg3, 1);
    if ((uint32_t)(result) != 0) goto loc_00867B40;
    result = v_stack_m1E0;
    local_rbx = 0;
    if (v_stack_m1E0 != v_stack_m1E0) {
        v_stack_m1AC = 0;
        v_stack_m19C = v_xmm0;
        v_stack_m18C = 0;
        v_stack_m184 = 0;
        Arg1 = v_stack_m1F8;
        v_stack_m1B8 = Arg1;
        v_stack_m1B0 = 0;
        v_stack_m1A0 = 0;
        result = v_stack_m178;
        v_stack_m1A8 = result;
        result = v_stack_m1E0;
        v_stack_m238 = result;
        v_stack_m240 = Arg1;
        v_stack_m248 = 22;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_stack_m1B8;
        Arg1 = Arg4 + 22;
        result = CmpCallCallBacksEx(Arg1, Arg2, Arg3, Arg4);
        local_rbx = v_stack_m1A0;
    }
    v_stack_m228 = (uint32_t)(local_rbx);
loc_00867B44:
    if (v_stack_m222 != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = KeLeaveCriticalRegionThread(Arg1, Arg2, Arg3, Arg4);
        local_rbx = v_stack_m228;
    }
    if (v_stack_m1F8 != 0) {
        result = ObfDereferenceObject(v_stack_m1F8, Arg2, Arg3, Arg4);
    }
    if (v_stack_m110 == 0) goto loc_00867B90;
    if (v_stack_m110 == v_stack_m118) goto loc_00867B90;
    if (v_stack_m110 != v_stack_m107) goto loc_00867BDF;
loc_00867B90:
    if (*(uint64_t *)(v_rip + 0x770471) != 0) goto loc_00867D7F;
loc_00867BA0:
    result = *(uint64_t *)(v_rip + 0x770471);
    if (v_stack_m220 != 0) {
        result = CmpReleaseShutdownRundown(v_stack_m1F8, v_stack_m110, Arg3, Arg4);
    }
    result = CmCleanupThreadInfo(v_stack_m138, v_stack_m110, Arg3, Arg4);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m110, Arg3, Arg4);
    local_rsp = (local_rsp) + (560);
    return result;
loc_00867BDF:
    if (((v_stack_p160) & (1)) == 0) goto loc_00867EFF;
    result = ExFreeToLookasideListEx(v_rip + 6049356, v_stack_m110, Arg3, Arg4);
    goto loc_00867B90;
loc_00867BFB:
    result = CmKeyBodyRemapToVirtualForEnum(v_stack_p70, (uint8_t)(v_stack_p44), 0, v_stack_p80);
    v_stack_p40 = (uint32_t)(result);
    if (sign_flag) goto loc_00867A6E;
    v_stack_p150 = 0;
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_00867F67;
    if ((*(uint64_t *)(v_rip + 0x68F5C4)) == 0) goto loc_00867D67;
    if ((uint8_t)(v_stack_p44) == 0) goto loc_00867EE7;
loc_00867C53:
    if ((*(uint32_t *)(v_rip + 0x5A22FE)) > 5) goto loc_00867DC6;
loc_00867C60:
    if (((uint32_t)(Arg4)) > 64) goto loc_00867D2D;
    Arg2 = 0;
    result = memset(v_stack_p161, Arg2, (uint32_t)(Arg4), v_stack_p80);
loc_00867C84:
    v_stack_p158 = v_stack_p161;
loc_00867C8C:
loc_00867C8E:
    v_stack_p40 = 0;
    if (sign_flag) goto loc_00867A6E;
    v_stack_p28 = v_stack_p60;
    v_stack_p20 = (uint32_t)((uint32_t)(Arg4));
    result = CmQueryKey(v_stack_p70, v_stack_p80, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_p158);
    v_stack_p40 = (uint32_t)(result);
    if (sign_flag) goto loc_00867ECA;
loc_00867CD4:
    *(uint32_t *)(v_stack_p58) = (uint32_t)((uint32_t)(v_stack_p60));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000023ULL) goto loc_00867D0C;
    local_r12 = (uint32_t)(Arg4);
    if (((uint32_t)((uint32_t)(Arg4))) >= ((uint32_t)((uint32_t)(v_stack_p60)))) {
        local_r12 = (uint32_t)((uint32_t)(v_stack_p60));
    }
    result = (uint32_t)(v_stack_p60);
    if (v_stack_p150 != v_stack_p158) {
        Arg3 = (uint32_t)(local_r12);
        result = memcpy(v_stack_p150, v_stack_p158, Arg3, v_stack_p158);
    }
    goto loc_00867A6E;
loc_00867D23:
    goto loc_00867A6A;
loc_00867D2D:
    if (((uint32_t)(0xC0000189ULL)) > 0x1000ULL) goto loc_00867E99;
    result = ExAllocateFromLookasideListEx(v_rip + 6049023, v_stack_p158, Arg3, v_stack_p158);
    if (result == 0) goto loc_00867E99;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(0xC0000189ULL), v_stack_p158);
loc_00867D67:
    v_stack_p158 = result;
    goto loc_00867C8C;
loc_00867D74:
    goto loc_00867907;
loc_00867D7F:
    v_stack_p28 = 0;
    if (result != (v_rip - 21510)) goto loc_00868015;
    v_stack_p20 = v_stack_p78;
    result = EtwpTraceRegistry(13, v_stack_p1B0, (uint32_t)((uint32_t)((uint32_t)(0xC0000189ULL))), (uint32_t)((uint32_t)((uint32_t)(Arg2))));
    goto loc_00867BA0;
loc_00867DB8:
    v_stack_p78 = *(uint64_t *)(result + 0x8);
    goto loc_0086796B;
loc_00867DC6:
    if (((*(uint8_t *)(v_rip + 0x5A219B)) & (4)) != 0) goto loc_00867FED;
loc_00867DD3:
    result = 0;
loc_00867DD5:
    if (0 == 0) goto loc_00867C60;
    v_stack_pA0 = 1;
    v_stack_p1F0 = v_stack_pA0;
    v_stack_p1F8 = 8;
    v_stack_p47 = 2;
    v_stack_p200 = v_stack_p47;
    v_stack_p208 = 1;
    if ((((uint32_t)(local_r12)) & ((uint32_t)(local_r12 - 1))) == 0) goto loc_00867E48;
    if ((uint32_t)((uint32_t)((uint32_t)(local_r12))) == 0) goto loc_00867E3F;
loc_00867E39:
    Arg1 = (uint32_t)(((uint32_t)(0xFFFFFFFFULL)) + 1);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) >> (1));
    if (condition_is_not_equal) goto loc_00867E39;
loc_00867E3F:
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = (uint32_t)((1) << ((uint8_t)(Arg1)));
loc_00867E48:
    v_stack_pA8 = (uint32_t)(Arg2);
    v_stack_p210 = v_stack_pA8;
    v_stack_p218 = 8;
    v_stack_p20 = v_stack_p1D0;
    result = tlgWriteAgg(v_rip + 5906633, v_rip - 8461324, (uint32_t)((uint32_t)((uint32_t)(0xC0000189ULL))), 5);
    goto loc_00867C60;
loc_00867E99:
    result = CmpAllocateTransientPoolWithQuota(v_rip + 5906633, (uint32_t)(0xC0000189ULL), (uint32_t)(0x42424D43ULL), 5);
    if (result != 0) goto loc_00867C84;
    goto loc_00867C8E;
loc_00867EBA:
    if (((uint32_t)(result)) == 0xC0000503ULL) goto loc_00867A68;
    goto loc_00867A6E;
loc_00867ECA:
    if (((uint32_t)((uint32_t)(0xC000009AULL))) == 0x80000005ULL) goto loc_00867CD4;
    if (((uint32_t)((uint32_t)(0xC000009AULL))) != 0xC0000023ULL) goto loc_00867A6E;
    goto loc_00867CD4;
loc_00867EE7:
    if (result <= result) goto loc_00867C53;
    goto loc_00867D67;
loc_00867EFF:
    result = CmSiFreeMemory(v_stack_p158, (uint32_t)(0xC0000189ULL), (uint32_t)(0x42424D43ULL), 5);
    goto loc_00867B90;
loc_00867F11:
    if (((uint32_t)((uint32_t)(Arg2))) != 4) goto loc_00867FE3;
    *(uint32_t *)(v_stack_p44) = 40;
    if (((uint32_t)(local_r12)) >= 40) goto loc_00867F36;
    v_stack_p40 = (uint32_t)((uint32_t)(0xC0000023ULL));
    goto loc_00867A6E;
loc_00867F36:
    Arg1 = 0;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = 0;
    *(uint32_t *)(result + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x8) + 0x60)));
    goto loc_00867A68;
loc_00867F67:
    v_stack_p158 = 0;
    goto loc_00867C8C;
loc_00867F74:
    if ((*(uint64_t *)(v_rip + 0x77008D)) == 0) goto loc_00867FCF;
    if ((uint32_t)(0xC0000023ULL) == 0) goto loc_00867FCF;
    v_stack_p58 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p58;
    Arg2 = 0;
    result = ObReferenceObjectByHandle((uint32_t)(0xC0000023ULL), Arg2, *(uint64_t *)(v_rip + 0x75EB26), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (!(sign_flag)) {
        Arg1 = v_stack_p58;
        result = *(uint64_t *)(Arg1 + 0x8);
        v_stack_p78 = result;
        result = ObfDereferenceObject(Arg1, Arg2, *(uint64_t *)(v_rip + 0x75EB26), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    }
    goto loc_00867A6A;
loc_00867FD9:
    goto loc_00867A6A;
loc_00867FE3:
    goto loc_00867A6A;
loc_00867FED:
    result = (uint32_t)((*(uint64_t *)(v_rip + 0x5A1F7C)) & (4));
    if (result != (*(uint64_t *)(v_rip + 0x5A1F72))) goto loc_00867DD3;
    goto loc_00867DD5;
loc_0086800B:
    goto loc_00867A2A;
loc_00868015:
    v_stack_p20 = v_stack_p78;
    result = guard_dispatch_icall(13, Arg2, *(uint64_t *)(v_rip + 0x75EB26), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    goto loc_00867BA0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0 + rax*1` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008676E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
