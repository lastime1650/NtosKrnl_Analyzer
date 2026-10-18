# NtSetValueKey

- RVA: `0x00844EA0`–`0x008457B9` (길이 `2,329` bytes)
- VA: `0x0000000140844EA0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000691D8`
- 디코드: `483`개 명령, `2,329/2,329` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00844F41` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (function, `0x0039FC50`)
- `0x00844F4E` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x00844F94` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00844FA0` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00844FE9` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (function, `0x00BC9400`)
- `0x00845026` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (function, `0x00BC9350`)
- `0x008450C9` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00845194` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008451B7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008451F9` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (function, `0x00461190`)
- `0x008453F7` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x00845478` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x008454C7` → [CmSetValueKey](CmSetValueKey_function_008457C0.md) (function, `0x008457C0`)
- `0x008454E9` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00845504` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x008455A0` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x008455BE` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008455D1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008455F2` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x008455FC` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x00845609` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x0084561B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00845687` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008456B8` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x008456E5` → [CmpIsSystemEntity](../8B/CmpIsSystemEntity_function_008B4E90.md) (function, `0x008B4E90`)
- `0x0084572C` → [CmKeyBodyReplicateToVirtual](CmKeyBodyReplicateToVirtual_function_00843FE4.md) (function, `0x00843FE4`)
- `0x00845772` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (function, `0x00BC9350`)
- `0x0084578A` → [CmKeyBodyNeedsVirtualImage](CmKeyBodyNeedsVirtualImage_function_00849864.md) (function, `0x00849864`)

### Direct callers
- [ExpWatchProductTypeWork](../6F/ExpWatchProductTypeWork_function_006FFCA0.md) at `0x00700049`
- [ExpWatchProductTypeWork](../6F/ExpWatchProductTypeWork_function_006FFCA0.md) at `0x00700094`
- [ExpWatchProductTypeWork](../6F/ExpWatchProductTypeWork_function_006FFCA0.md) at `0x00700106`
- [ExpWatchProductTypeWork](../6F/ExpWatchProductTypeWork_function_006FFCA0.md) at `0x00700151`
- [ExpWatchLicenseInfoWork](../7C/ExpWatchLicenseInfoWork_function_007C6DB0.md) at `0x007C6FCC`
- [ExpWatchLicenseInfoWork](../7C/ExpWatchLicenseInfoWork_function_007C6DB0.md) at `0x007C70DF`
- [InitSafeBoot](../../init/C1/InitSafeBoot_function_00C1BFE0.md) at `0x00C1C157`
- [InitSafeBoot](../../init/C1/InitSafeBoot_function_00C1BFE0.md) at `0x00C1C194`
- [IopStoreSystemPartitionInformation](../../init/C2/IopStoreSystemPartitionInformation_function_00C2D780.md) at `0x00C2D953`
- [IopStoreSystemPartitionInformation](../../init/C2/IopStoreSystemPartitionInformation_function_00C2D780.md) at `0x00C2D9B0`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C51CC9`
- [ExpUpdateProductSuiteTypeInRegistry](../../init/C5/ExpUpdateProductSuiteTypeInRegistry_function_00C51BC0.md) at `0x00C52112`
- [CmpAddDockingInfo](../../init/C5/CmpAddDockingInfo_function_00C567B4.md) at `0x00C567F0`
- [CmpAddDockingInfo](../../init/C5/CmpAddDockingInfo_function_00C567B4.md) at `0x00C56823`
- [CmpAddDockingInfo](../../init/C5/CmpAddDockingInfo_function_00C567B4.md) at `0x00C56851`
- [CmpAddDockingInfo](../../init/C5/CmpAddDockingInfo_function_00C567B4.md) at `0x00C5687F`

### Static image references
- `0x00844EB3` → RVA `0x00E0A740` (`.data`; read)
- `0x00844F2B` → RVA `0x00FD8008` (`PAGEDATA`; read)
- `0x0084523B` → RVA `0x00EF7208` (`.data`; read)
- `0x008453EA` → RVA `0x00EEFB88` (`.data`; read)
- `0x008456C0` → RVA `0x00E0ECA0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **19**
  - `0x00844F41` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (`PAGE` → `.text`)
  - `0x00844F4E` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x00844F94` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00844FA0` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00844FE9` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (`PAGE` → `PAGECMRC`)
  - `0x00845026` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (`PAGE` → `PAGECMRC`)
  - `0x00845194` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008451B7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008451F9` → [CmpAllocateTransientPoolWithQuota](../../text/46/CmpAllocateTransientPoolWithQuota_function_00461190.md) (`PAGE` → `.text`)
  - `0x008453F7` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x00845504` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x008455BE` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008455D1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008455F2` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x008455FC` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x00845609` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x0084561B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00845687` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00845772` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (`PAGE` → `PAGECMRC`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00844EA0  40 53                           push rbx
00844EA2  56                              push rsi
00844EA3  57                              push rdi
00844EA4  41 54                           push r12
00844EA6  41 55                           push r13
00844EA8  41 56                           push r14
00844EAA  41 57                           push r15
00844EAC  48 81 EC 00 02 00 00            sub rsp, 0x200
00844EB3  48 8B 05 86 58 5C 00            mov rax, qword ptr [rip + 0x5c5886]
00844EBA  48 33 C4                        xor rax, rsp
00844EBD  48 89 84 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rax
00844EC5  44 89 4C 24 7C                  mov dword ptr [rsp + 0x7c], r9d
00844ECA  44 89 84 24 88 00 00 00         mov dword ptr [rsp + 0x88], r8d
00844ED2  48 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdx
00844EDA  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
00844EE2  48 8B 84 24 60 02 00 00         mov rax, qword ptr [rsp + 0x260]
00844EEA  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00844EEF  0F 57 C0                        xorps xmm0, xmm0
00844EF2  33 C0                           xor eax, eax
00844EF4  0F 11 84 24 38 01 00 00         movups xmmword ptr [rsp + 0x138], xmm0
00844EFC  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
00844F04  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
00844F09  33 DB                           xor ebx, ebx
00844F0B  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
00844F13  0F 11 84 24 90 01 00 00         movups xmmword ptr [rsp + 0x190], xmm0
00844F1B  0F 11 84 24 A0 01 00 00         movups xmmword ptr [rsp + 0x1a0], xmm0
00844F23  48 89 9C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rbx
00844F2B  48 39 05 D6 30 79 00            cmp qword ptr [rip + 0x7930d6], rax
00844F32  74 12                           je 0x140844f46
00844F34  BA 00 00 02 00                  mov edx, 0x20000
00844F39  48 8D 8C 24 90 01 00 00         lea rcx, [rsp + 0x190]
00844F41  E8 0A AD B5 FF                  call 0x14039fc50
00844F46  48 8D 8C 24 38 01 00 00         lea rcx, [rsp + 0x138]
00844F4E  E8 1D 6F BB FF                  call 0x1403fbe70
00844F53  45 32 ED                        xor r13b, r13b
00844F56  45 32 F6                        xor r14b, r14b
00844F59  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00844F5E  45 32 FF                        xor r15b, r15b
00844F61  44 88 7C 24 41                  mov byte ptr [rsp + 0x41], r15b
00844F66  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00844F6E  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00844F76  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00844F7E  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00844F86  33 D2                           xor edx, edx
00844F88  44 8D 42 40                     lea r8d, [rdx + 0x40]
00844F8C  48 8D 8C 24 50 01 00 00         lea rcx, [rsp + 0x150]
00844F94  E8 A7 1C E8 FF                  call 0x1406c6c40
00844F99  33 D2                           xor edx, edx
00844F9B  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00844FA0  E8 DB 57 BE FF                  call 0x14042a780
00844FA5  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00844FAA  48 89 9C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rbx
00844FB2  89 5C 24 78                     mov dword ptr [rsp + 0x78], ebx
00844FB6  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
00844FBE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00844FC7  0F B6 B8 32 02 00 00            movzx edi, byte ptr [rax + 0x232]
00844FCE  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
00844FD3  40 32 F6                        xor sil, sil
00844FD6  0F 57 C0                        xorps xmm0, xmm0
00844FD9  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
00844FE1  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
00844FE9  E8 12 44 38 00                  call 0x140bc9400
00844FEE  44 0F B6 E0                     movzx r12d, al
00844FF2  88 44 24 48                     mov byte ptr [rsp + 0x48], al
00844FF6  84 C0                           test al, al
00844FF8  0F 84 FE 06 00 00               je 0x1408456fc
00844FFE  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00845006  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0084500B  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00845010  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00845015  44 0F B6 CF                     movzx r9d, dil
00845019  BA 02 00 00 00                  mov edx, 2
0084501E  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00845026  E8 25 43 38 00                  call 0x140bc9350
0084502B  8B F8                           mov edi, eax
0084502D  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00845031  3D 22 00 00 C0                  cmp eax, 0xc0000022
00845036  0F 84 74 06 00 00               je 0x1408456b0
0084503C  41 0F B6 F7                     movzx esi, r15b
00845040  85 FF                           test edi, edi
00845042  0F 88 94 04 00 00               js 0x1408454dc
00845048  48 39 1D B9 2F 79 00            cmp qword ptr [rip + 0x792fb9], rbx
0084504F  0F 85 3C 06 00 00               jne 0x140845691
00845055  0F B6 4C 24 40                  movzx ecx, byte ptr [rsp + 0x40]
0084505A  80 F9 01                        cmp cl, 1
0084505D  0F 85 BC 02 00 00               jne 0x14084531f
00845063  0F 57 C0                        xorps xmm0, xmm0
00845066  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
0084506E  49 BA 00 00 FF FF FF 7F 00 00   movabs r10, 0x7fffffff0000
00845078  49 8B CA                        mov rcx, r10
0084507B  4C 39 94 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], r10
00845083  48 0F 42 8C 24 B0 00 00 00      cmovb rcx, qword ptr [rsp + 0xb0]
0084508C  90                              nop
0084508D  8B 01                           mov eax, dword ptr [rcx]
0084508F  89 84 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], eax
00845096  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
0084509A  4C 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r8
008450A2  0F 28 84 24 D0 00 00 00         movaps xmm0, xmmword ptr [rsp + 0xd0]
008450AA  66 0F 7F 44 24 50               movdqa xmmword ptr [rsp + 0x50], xmm0
008450B0  66 0F 7E C0                     movd eax, xmm0
008450B4  66 89 44 24 52                  mov word ptr [rsp + 0x52], ax
008450B9  0F B7 54 24 50                  movzx edx, word ptr [rsp + 0x50]
008450BE  66 85 D2                        test dx, dx
008450C1  74 25                           je 0x1408450e8
008450C3  41 F6 C0 01                     test r8b, 1
008450C7  74 05                           je 0x1408450ce
008450C9  E8 02 4F 05 00                  call 0x140899fd0
008450CE  4E 8D 0C 02                     lea r9, [rdx + r8]
008450D2  4A 8D 0C 02                     lea rcx, [rdx + r8]
008450D6  49 3B CA                        cmp rcx, r10
008450D9  0F 87 24 02 00 00               ja 0x140845303
008450DF  4D 3B C8                        cmp r9, r8
008450E2  0F 82 1B 02 00 00               jb 0x140845303
008450E8  44 8B B4 24 68 02 00 00         mov r14d, dword ptr [rsp + 0x268]
008450F0  45 85 F6                        test r14d, r14d
008450F3  74 1B                           je 0x140845110
008450F5  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008450FA  4E 8D 04 31                     lea r8, [rcx + r14]
008450FE  4D 3B C2                        cmp r8, r10
00845101  0F 87 0A 02 00 00               ja 0x140845311
00845107  4C 3B C1                        cmp r8, rcx
0084510A  0F 82 01 02 00 00               jb 0x140845311
00845110  0F B6 4C 24 40                  movzx ecx, byte ptr [rsp + 0x40]
00845115  B8 FF 7F 00 00                  mov eax, 0x7fff
0084511A  66 3B D0                        cmp dx, ax
0084511D  0F 87 3A 02 00 00               ja 0x14084535d
00845123  F6 C2 01                        test dl, 1
00845126  0F 85 31 02 00 00               jne 0x14084535d
0084512C  41 81 FE 00 F0 FF 7F            cmp r14d, 0x7ffff000
00845133  0F 87 24 02 00 00               ja 0x14084535d
00845139  0F B7 F2                        movzx esi, dx
0084513C  8D 7E 07                        lea edi, [rsi + 7]
0084513F  83 E7 F8                        and edi, 0xfffffff8
00845142  42 8D 04 37                     lea eax, [rdi + r14]
00845146  41 3B C6                        cmp eax, r14d
00845149  0F 82 9F 01 00 00               jb 0x1408452ee
0084514F  84 C9                           test cl, cl
00845151  0F 84 E4 00 00 00               je 0x14084523b
00845157  85 C0                           test eax, eax
00845159  74 70                           je 0x1408451cb
0084515B  83 F8 40                        cmp eax, 0x40
0084515E  77 75                           ja 0x1408451d5
00845160  48 8D 84 24 B0 01 00 00         lea rax, [rsp + 0x1b0]
00845168  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0084516D  8B C7                           mov eax, edi
0084516F  48 8D B4 24 B0 01 00 00         lea rsi, [rsp + 0x1b0]
00845177  48 03 F0                        add rsi, rax
0084517A  66 85 D2                        test dx, dx
0084517D  0F 84 2C 01 00 00               je 0x1408452af
00845183  44 0F B7 C2                     movzx r8d, dx
00845187  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0084518C  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
00845191  48 8B CF                        mov rcx, rdi
00845194  E8 A7 16 E8 FF                  call 0x1406c6840
00845199  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0084519E  0F B7 54 24 50                  movzx edx, word ptr [rsp + 0x50]
008451A3  45 85 F6                        test r14d, r14d
008451A6  0F 84 19 01 00 00               je 0x1408452c5
008451AC  45 8B C6                        mov r8d, r14d
008451AF  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
008451B4  48 8B CE                        mov rcx, rsi
008451B7  E8 84 16 E8 FF                  call 0x1406c6840
008451BC  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
008451C1  0F B7 54 24 50                  movzx edx, word ptr [rsp + 0x50]
008451C6  E9 D3 01 00 00                  jmp 0x14084539e
008451CB  48 8B B4 24 C0 00 00 00         mov rsi, qword ptr [rsp + 0xc0]
008451D3  EB A5                           jmp 0x14084517a
008451D5  41 83 FE 40                     cmp r14d, 0x40
008451D9  0F 86 9A 00 00 00               jbe 0x140845279
008451DF  8B F0                           mov esi, eax
008451E1  66 83 FA 40                     cmp dx, 0x40
008451E5  41 0F 46 F6                     cmovbe esi, r14d
008451E9  85 F6                           test esi, esi
008451EB  0F 84 6F FF FF FF               je 0x140845160
008451F1  8B D6                           mov edx, esi
008451F3  41 B8 43 6D 56 6E               mov r8d, 0x6e566d43
008451F9  E8 92 BF C1 FF                  call 0x140461190
008451FE  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00845206  48 85 C0                        test rax, rax
00845209  0F 84 CA 00 00 00               je 0x1408452d9
0084520F  0F B7 54 24 50                  movzx edx, word ptr [rsp + 0x50]
00845214  85 F6                           test esi, esi
00845216  0F 84 44 FF FF FF               je 0x140845160
0084521C  41 3B F6                        cmp esi, r14d
0084521F  75 6D                           jne 0x14084528e
00845221  48 8D 84 24 B0 01 00 00         lea rax, [rsp + 0x1b0]
00845229  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0084522E  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
00845236  E9 3F FF FF FF                  jmp 0x14084517a
0084523B  48 8B 0D C6 1F 6B 00            mov rcx, qword ptr [rip + 0x6b1fc6]
00845242  49 B8 FF FF FE FF FF 7F 00 00   movabs r8, 0x7ffffffeffff
0084524C  48 85 C9                        test rcx, rcx
0084524F  0F 84 71 FF FF FF               je 0x1408451c6
00845255  4C 39 44 24 58                  cmp qword ptr [rsp + 0x58], r8
0084525A  0F 86 F7 FE FF FF               jbe 0x140845157
00845260  48 85 C9                        test rcx, rcx
00845263  0F 84 5D FF FF FF               je 0x1408451c6
00845269  4C 39 44 24 68                  cmp qword ptr [rsp + 0x68], r8
0084526E  0F 86 E3 FE FF FF               jbe 0x140845157
00845274  E9 4D FF FF FF                  jmp 0x1408451c6
00845279  66 83 FA 40                     cmp dx, 0x40
0084527D  76 3A                           jbe 0x1408452b9
0084527F  41 83 FE 40                     cmp r14d, 0x40
00845283  0F 87 56 FF FF FF               ja 0x1408451df
00845289  E9 5B FF FF FF                  jmp 0x1408451e9
0084528E  0F B7 C2                        movzx eax, dx
00845291  3B F0                           cmp esi, eax
00845293  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0084529B  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008452A0  75 2D                           jne 0x1408452cf
008452A2  48 8D B4 24 B0 01 00 00         lea rsi, [rsp + 0x1b0]
008452AA  E9 CB FE FF FF                  jmp 0x14084517a
008452AF  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
008452B4  E9 EA FE FF FF                  jmp 0x1408451a3
008452B9  44 3B F6                        cmp r14d, esi
008452BC  41 0F 42 F6                     cmovb esi, r14d
008452C0  E9 24 FF FF FF                  jmp 0x1408451e9
008452C5  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
008452CA  E9 F7 FE FF FF                  jmp 0x1408451c6
008452CF  8B F7                           mov esi, edi
008452D1  48 03 F0                        add rsi, rax
008452D4  E9 A1 FE FF FF                  jmp 0x14084517a
008452D9  BF 9A 00 00 C0                  mov edi, 0xc000009a
008452DE  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
008452E2  41 0F B6 F7                     movzx esi, r15b
008452E6  45 32 F6                        xor r14b, r14b
008452E9  E9 EE 01 00 00                  jmp 0x1408454dc
008452EE  BF 0D 00 00 C0                  mov edi, 0xc000000d
008452F3  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
008452F7  41 0F B6 F7                     movzx esi, r15b
008452FB  45 32 F6                        xor r14b, r14b
008452FE  E9 D9 01 00 00                  jmp 0x1408454dc
00845303  41 0F B6 02                     movzx eax, byte ptr [r10]
00845307  0F B7 54 24 50                  movzx edx, word ptr [rsp + 0x50]
0084530C  E9 D7 FD FF FF                  jmp 0x1408450e8
00845311  41 0F B6 02                     movzx eax, byte ptr [r10]
00845315  0F B7 54 24 50                  movzx edx, word ptr [rsp + 0x50]
0084531A  E9 F1 FD FF FF                  jmp 0x140845110
0084531F  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00845327  0F 10 00                        movups xmm0, xmmword ptr [rax]
0084532A  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
0084532F  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00845334  44 8B B4 24 68 02 00 00         mov r14d, dword ptr [rsp + 0x268]
0084533C  45 85 F6                        test r14d, r14d
0084533F  74 12                           je 0x140845353
00845341  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00845346  0F B6 08                        movzx ecx, byte ptr [rax]
00845349  0F B7 54 24 50                  movzx edx, word ptr [rsp + 0x50]
0084534E  E9 BD FD FF FF                  jmp 0x140845110
00845353  0F B7 54 24 50                  movzx edx, word ptr [rsp + 0x50]
00845358  E9 B8 FD FF FF                  jmp 0x140845115
0084535D  BF 0D 00 00 C0                  mov edi, 0xc000000d
00845362  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
00845366  41 0F B6 F7                     movzx esi, r15b
0084536A  45 32 F6                        xor r14b, r14b
0084536D  E9 6A 01 00 00                  jmp 0x1408454dc
00845372  8B F8                           mov edi, eax
00845374  33 C0                           xor eax, eax
00845376  66 89 44 24 50                  mov word ptr [rsp + 0x50], ax
0084537B  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00845380  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
00845384  0F B6 74 24 41                  movzx esi, byte ptr [rsp + 0x41]
00845389  33 DB                           xor ebx, ebx
0084538B  44 0F B6 64 24 48               movzx r12d, byte ptr [rsp + 0x48]
00845391  44 0F B6 E8                     movzx r13d, al
00845395  44 0F B6 F0                     movzx r14d, al
00845399  E9 3E 01 00 00                  jmp 0x1408454dc
0084539E  66 85 D2                        test dx, dx
008453A1  74 1D                           je 0x1408453c0
008453A3  41 B8 FE FF 00 00               mov r8d, 0xfffe
008453A9  0F B7 CA                        movzx ecx, dx
008453AC  48 D1 E9                        shr rcx, 1
008453AF  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
008453B4  66 83 7C 48 FE 00               cmp word ptr [rax + rcx*2 - 2], 0
008453BA  0F 84 E5 03 00 00               je 0x1408457a5
008453C0  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
008453C5  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
008453C9  8B 41 08                        mov eax, dword ptr [rcx + 8]
008453CC  84 C0                           test al, al
008453CE  0F 88 60 02 00 00               js 0x140845634
008453D4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008453DD  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008453E4  90                              nop
008453E5  C6 44 24 41 01                  mov byte ptr [rsp + 0x41], 1
008453EA  83 3D 97 A7 6A 00 00            cmp dword ptr [rip + 0x6aa797], 0
008453F1  0F 84 91 00 00 00               je 0x140845488
008453F7  E8 80 16 C1 FF                  call 0x140456a7c
008453FC  85 C0                           test eax, eax
008453FE  0F 85 84 00 00 00               jne 0x140845488
00845404  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00845409  48 89 8C 24 50 01 00 00         mov qword ptr [rsp + 0x150], rcx
00845411  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00845416  48 89 84 24 58 01 00 00         mov qword ptr [rsp + 0x158], rax
0084541E  8B 84 24 88 00 00 00            mov eax, dword ptr [rsp + 0x88]
00845425  89 84 24 60 01 00 00            mov dword ptr [rsp + 0x160], eax
0084542C  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
00845430  89 84 24 64 01 00 00            mov dword ptr [rsp + 0x164], eax
00845437  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0084543C  48 89 84 24 68 01 00 00         mov qword ptr [rsp + 0x168], rax
00845444  44 89 B4 24 70 01 00 00         mov dword ptr [rsp + 0x170], r14d
0084544C  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00845454  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00845459  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0084545E  C7 44 24 20 10 00 00 00         mov dword ptr [rsp + 0x20], 0x10
00845466  41 B1 01                        mov r9b, 1
00845469  45 33 C0                        xor r8d, r8d
0084546C  48 8D 94 24 50 01 00 00         lea rdx, [rsp + 0x150]
00845474  41 8D 48 01                     lea ecx, [r8 + 1]
00845478  E8 C3 0A 02 00                  call 0x140865f40
0084547D  85 C0                           test eax, eax
0084547F  0F 88 C4 01 00 00               js 0x140845649
00845485  41 B5 01                        mov r13b, 1
00845488  45 84 FF                        test r15b, r15b
0084548B  0F 85 79 02 00 00               jne 0x14084570a
00845491  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
00845498  C1 E8 02                        shr eax, 2
0084549B  24 01                           and al, 1
0084549D  88 44 24 30                     mov byte ptr [rsp + 0x30], al
008454A1  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
008454A9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008454AE  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
008454B3  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
008454B8  44 8B 44 24 7C                  mov r8d, dword ptr [rsp + 0x7c]
008454BD  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
008454C2  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008454C7  E8 F4 02 00 00                  call 0x1408457c0
008454CC  8B F8                           mov edi, eax
008454CE  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
008454D2  41 0F B6 F7                     movzx esi, r15b
008454D6  44 0F B6 74 24 41               movzx r14d, byte ptr [rsp + 0x41]
008454DC  40 84 F6                        test sil, sil
008454DF  74 0D                           je 0x1408454ee
008454E1  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
008454E9  E8 22 62 02 00                  call 0x14086b710
008454EE  45 84 ED                        test r13b, r13b
008454F1  0F 84 B9 00 00 00               je 0x1408455b0
008454F7  83 3D 8A A6 6A 00 00            cmp dword ptr [rip + 0x6aa68a], 0
008454FE  0F 84 A8 00 00 00               je 0x1408455ac
00845504  E8 73 15 C1 FF                  call 0x140456a7c
00845509  85 C0                           test eax, eax
0084550B  0F 85 9B 00 00 00               jne 0x1408455ac
00845511  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00845519  48 39 84 24 A0 00 00 00         cmp qword ptr [rsp + 0xa0], rax
00845521  0F 84 85 00 00 00               je 0x1408455ac
00845527  89 9C 24 0C 01 00 00            mov dword ptr [rsp + 0x10c], ebx
0084552E  0F 57 C0                        xorps xmm0, xmm0
00845531  F3 0F 7F 84 24 1C 01 00 00      movdqu xmmword ptr [rsp + 0x11c], xmm0
0084553A  48 89 9C 24 2C 01 00 00         mov qword ptr [rsp + 0x12c], rbx
00845542  89 9C 24 34 01 00 00            mov dword ptr [rsp + 0x134], ebx
00845549  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0084554E  48 89 8C 24 00 01 00 00         mov qword ptr [rsp + 0x100], rcx
00845556  89 BC 24 08 01 00 00            mov dword ptr [rsp + 0x108], edi
0084555D  89 BC 24 18 01 00 00            mov dword ptr [rsp + 0x118], edi
00845564  48 8D 84 24 50 01 00 00         lea rax, [rsp + 0x150]
0084556C  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
00845574  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
0084557C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00845581  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00845586  C7 44 24 20 10 00 00 00         mov dword ptr [rsp + 0x20], 0x10
0084558E  45 33 C9                        xor r9d, r9d
00845591  45 33 C0                        xor r8d, r8d
00845594  48 8D 94 24 00 01 00 00         lea rdx, [rsp + 0x100]
0084559C  41 8D 49 10                     lea ecx, [r9 + 0x10]
008455A0  E8 9B 09 02 00                  call 0x140865f40
008455A5  8B BC 24 18 01 00 00            mov edi, dword ptr [rsp + 0x118]
008455AC  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
008455B0  45 84 F6                        test r14b, r14b
008455B3  74 12                           je 0x1408455c7
008455B5  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008455BE  E8 2D 9A A1 FF                  call 0x14025eff0
008455C3  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
008455C7  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008455CC  48 85 C9                        test rcx, rcx
008455CF  74 05                           je 0x1408455d6
008455D1  E8 7A 3D AB FF                  call 0x1402f9350
008455D6  48 8B 05 2B 2A 79 00            mov rax, qword ptr [rip + 0x792a2b]
008455DD  48 85 C0                        test rax, rax
008455E0  75 7E                           jne 0x140845660
008455E2  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
008455EA  48 85 C0                        test rax, rax
008455ED  74 08                           je 0x1408455f7
008455EF  48 8B C8                        mov rcx, rax
008455F2  E8 89 07 C3 FF                  call 0x140475d80
008455F7  45 84 E4                        test r12b, r12b
008455FA  74 05                           je 0x140845601
008455FC  E8 7F 42 38 00                  call 0x140bc9880
00845601  48 8D 8C 24 38 01 00 00         lea rcx, [rsp + 0x138]
00845609  E8 42 A7 BD FF                  call 0x14041fd50
0084560E  8B C7                           mov eax, edi
00845610  48 8B 8C 24 F0 01 00 00         mov rcx, qword ptr [rsp + 0x1f0]
00845618  48 33 CC                        xor rcx, rsp
0084561B  E8 20 70 E6 FF                  call 0x1406ac640
00845620  48 81 C4 00 02 00 00            add rsp, 0x200
00845627  41 5F                           pop r15
00845629  41 5E                           pop r14
0084562B  41 5D                           pop r13
0084562D  41 5C                           pop r12
0084562F  5F                              pop rdi
00845630  5E                              pop rsi
00845631  5B                              pop rbx
00845632  C3                              ret
00845633  CC                              int3
00845634  BF 22 00 00 C0                  mov edi, 0xc0000022
00845639  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
0084563D  41 0F B6 F7                     movzx esi, r15b
00845641  45 32 F6                        xor r14b, r14b
00845644  E9 93 FE FF FF                  jmp 0x1408454dc
00845649  41 0F B6 F7                     movzx esi, r15b
0084564D  8B FB                           mov edi, ebx
0084564F  3D 03 05 00 C0                  cmp eax, 0xc0000503
00845654  0F 45 F8                        cmovne edi, eax
00845657  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
0084565B  E9 76 FE FF FF                  jmp 0x1408454d6
00845660  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00845665  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0084566A  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00845672  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00845677  45 33 C9                        xor r9d, r9d
0084567A  44 8B C7                        mov r8d, edi
0084567D  48 8D 94 24 90 01 00 00         lea rdx, [rsp + 0x190]
00845685  B1 0E                           mov cl, 0xe
00845687  E8 44 54 E7 FF                  call 0x1406baad0
0084568C  E9 51 FF FF FF                  jmp 0x1408455e2
00845691  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00845696  48 85 C9                        test rcx, rcx
00845699  0F 84 B6 F9 FF FF               je 0x140845055
0084569F  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
008456A3  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
008456AB  E9 A5 F9 FF FF                  jmp 0x140845055
008456B0  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
008456B8  E8 63 61 02 00                  call 0x14086b820
008456BD  40 B6 01                        mov sil, 1
008456C0  38 1D DA 95 5C 00               cmp byte ptr [rip + 0x5c95da], bl
008456C6  74 26                           je 0x1408456ee
008456C8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008456D1  0F B6 88 32 02 00 00            movzx ecx, byte ptr [rax + 0x232]
008456D8  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
008456DD  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
008456E5  E8 A6 F7 06 00                  call 0x1408b4e90
008456EA  84 C0                           test al, al
008456EC  74 5A                           je 0x140845748
008456EE  BF 22 00 00 C0                  mov edi, 0xc0000022
008456F3  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
008456F7  E9 E0 FD FF FF                  jmp 0x1408454dc
008456FC  BF 89 01 00 C0                  mov edi, 0xc0000189
00845701  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
00845705  E9 D2 FD FF FF                  jmp 0x1408454dc
0084570A  48 8D 44 24 78                  lea rax, [rsp + 0x78]
0084570F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00845714  4C 8D 8C 24 E0 00 00 00         lea r9, [rsp + 0xe0]
0084571C  41 B8 02 00 00 00               mov r8d, 2
00845722  0F B6 54 24 40                  movzx edx, byte ptr [rsp + 0x40]
00845727  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0084572C  E8 B3 E8 FF FF                  call 0x140843fe4
00845731  8B F8                           mov edi, eax
00845733  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00845737  41 0F B6 F7                     movzx esi, r15b
0084573B  85 C0                           test eax, eax
0084573D  0F 89 4E FD FF FF               jns 0x140845491
00845743  E9 8E FD FF FF                  jmp 0x1408454d6
00845748  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00845750  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00845755  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0084575A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0084575F  44 0F B6 4C 24 40               movzx r9d, byte ptr [rsp + 0x40]
00845765  BA 19 00 02 00                  mov edx, 0x20019
0084576A  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00845772  E8 D9 3B 38 00                  call 0x140bc9350
00845777  8B F8                           mov edi, eax
00845779  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0084577D  85 C0                           test eax, eax
0084577F  0F 88 57 FD FF FF               js 0x1408454dc
00845785  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0084578A  E8 D5 40 00 00                  call 0x140849864
0084578F  84 C0                           test al, al
00845791  0F 84 57 FF FF FF               je 0x1408456ee
00845797  44 0F B6 FE                     movzx r15d, sil
0084579B  40 88 74 24 41                  mov byte ptr [rsp + 0x41], sil
008457A0  E9 97 F8 FF FF                  jmp 0x14084503c
008457A5  66 41 03 D0                     add dx, r8w
008457A9  66 89 54 24 50                  mov word ptr [rsp + 0x50], dx
008457AE  0F 85 F5 FB FF FF               jne 0x1408453a9
008457B4  E9 07 FC FF FF                  jmp 0x1408453c0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSetValueKey(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m104;
    unsigned __int64 v_stack_m10C;
    unsigned __int64 v_stack_m11C;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m12C;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned int v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m1BC;
    unsigned int v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int16 v_stack_m1E6;
    unsigned __int64 v_stack_m1E8;
    unsigned __int8 v_stack_m1F0;
    unsigned int v_stack_m1F4;
    unsigned __int8 v_stack_m1F7;
    unsigned __int8 v_stack_m1F8;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_p190;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p41;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pE0;

    v_rsp = (v_rsp) - (512);
    result = (*(unsigned __int64 *)(v_rip + 6051974)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m1BC = a4;
    v_stack_m1B0 = a3;
    v_stack_m188 = a2;
    v_stack_m1A0 = a1;
    v_stack_m1D0 = a5;
    result = 0;
    v_stack_m100 = v_xmm0;
    v_stack_mF0 = 0;
    v_stack_m1E8 = v_xmm0;
    v_rbx = 0;
    v_stack_m1A8 = 0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m180 = 0;
    if ((*(unsigned __int64 *)(v_rip + 7942358)) != 0) {
        a2 = 0x20000ULL;
        a1 = v_stack_mA8;
        result = EtwGetKernelTraceTimestamp(a1, a2, a3, a4);
    }
    result = CmpInitializeThreadInfo(v_stack_m100, a2, a3, a4);
    v_r13 = 0;
    v_r14 = 0;
    v_stack_m1D8 = 0;
    v_r15 = 0;
    v_stack_m1F7 = 0;
    v_stack_m190 = v_stack_m198;
    v_stack_m198 = v_stack_m198;
    a2 = 0;
    result = memset(v_stack_mE8, a2, a2 + 64, a4);
    a2 = 0;
    result = RtlInitUnicodeString(v_stack_m1E8, a2, a2 + 64, a4);
    v_stack_m1C8 = 0;
    v_stack_m178 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1F8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_rsi = 0;
    v_stack_m158 = v_xmm0;
    v_stack_m148 = v_xmm0;
    result = CmpAcquireShutdownRundown(v_stack_m1E8, a2, a2 + 64, a4);
    v_stack_m1F0 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_008456FC;
    v_stack_m210 = v_stack_m1A8;
    v_stack_m218 = v_stack_m1D8;
    result = CmObReferenceObjectByHandle(v_stack_m1A0, 2, a2 + 64, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_m1F4 = (unsigned int)(result);
    if (((unsigned int)(result)) == 0xC0000022ULL) goto loc_008456B0;
loc_0084503C:
    if (sign_flag) goto loc_008454DC;
    if ((*(unsigned __int64 *)(v_rip + 7942073)) != 0) goto loc_00845691;
loc_00845055:
    if (((unsigned __int8)(v_stack_m1F8)) != 1) goto loc_0084531F;
    v_stack_m168 = v_xmm0;
    a1 = v_r10;
    if (v_stack_m188 < v_r10) { a1 = v_stack_m188; }
    v_stack_m168 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_m160 = *(unsigned __int64 *)(a1 + 8);
    v_stack_m1E8 = v_xmm0;
    v_stack_m1E6 = (unsigned __int16)((unsigned int)(*(unsigned int *)(a1)));
    if ((unsigned __int16)(v_stack_m1E8) == 0) goto loc_008450E8;
    result = (unsigned int)(*(unsigned int *)(a1));
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 8))) & (1)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, v_stack_m1E8, *(unsigned __int64 *)(a1 + 8), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    if ((v_stack_m1E8 + *(unsigned __int64 *)(a1 + 8) * 1) > v_r10) goto loc_00845303;
    if ((v_stack_m1E8 + *(unsigned __int64 *)(a1 + 8) * 1) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00845303;
loc_008450E8:
    if ((unsigned int)((unsigned int)(a6)) == 0) goto loc_00845110;
    if ((v_stack_m1D0 + (unsigned int)(a6) * 1) > v_r10) goto loc_00845311;
    if ((v_stack_m1D0 + (unsigned int)(a6) * 1) < v_stack_m1D0) goto loc_00845311;
loc_00845110:
loc_00845115:
    if (((unsigned __int16)(v_stack_m1E8)) > ((unsigned __int16)((unsigned int)(0x7FFFULL)))) goto loc_0084535D;
    if ((((unsigned __int8)(v_stack_m1E8)) & (1)) != 0) goto loc_0084535D;
    if (((unsigned int)((unsigned int)(a6))) > 0x7FFFF000ULL) goto loc_0084535D;
    v_rdi = (unsigned int)(((unsigned __int16)(v_stack_m1E8) + 7) & (0xFFFFFFF8ULL));
    if (((unsigned int)(v_rdi + (unsigned int)(a6) * 1)) < ((unsigned int)((unsigned int)(a6)))) goto loc_008452EE;
    if ((unsigned __int8)(v_stack_m1F8) == 0) goto loc_0084523B;
loc_00845157:
    if ((unsigned int)(v_rdi + (unsigned int)(a6) * 1) == 0) goto loc_008451CB;
    if (((unsigned int)(v_rdi + (unsigned int)(a6) * 1)) > 64) goto loc_008451D5;
loc_00845160:
    v_stack_m1C8 = v_stack_m88;
    v_rsi = (v_stack_m88) + ((unsigned int)((unsigned int)(v_rdi)));
loc_0084517A:
    if ((unsigned __int16)(v_stack_m1E8) == 0) goto loc_008452AF;
    result = memcpy(v_stack_m1C8, v_stack_m1E0, (unsigned __int16)(v_stack_m1E8), v_stack_m1E8 + *(unsigned __int64 *)(a1 + 8) * 1);
    v_stack_m1E0 = v_stack_m1C8;
loc_008451A3:
    if ((unsigned int)((unsigned int)(a6)) == 0) goto loc_008452C5;
    result = memcpy(v_rsi, v_stack_m1D0, (unsigned int)((unsigned int)((unsigned int)(a6))), v_stack_m1E8 + *(unsigned __int64 *)(a1 + 8) * 1);
    v_stack_m1D0 = v_rsi;
loc_008451C6:
    goto loc_0084539E;
loc_008451CB:
    goto loc_0084517A;
loc_008451D5:
    if (((unsigned int)((unsigned int)(a6))) <= 64) goto loc_00845279;
loc_008451DF:
    v_rsi = (unsigned int)((unsigned int)(result));
    if (((unsigned __int16)(v_stack_m1E8)) <= 64) { v_rsi = (unsigned int)((unsigned int)(a6)); }
loc_008451E9:
    if ((unsigned int)(v_rsi) == 0) goto loc_00845160;
    result = CmpAllocateTransientPoolWithQuota(v_rsi, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0x6E566D43ULL), v_stack_m1E8 + *(unsigned __int64 *)(a1 + 8) * 1);
    v_stack_m1B8 = result;
    if (result == 0) goto loc_008452D9;
    if ((unsigned int)(v_rsi) == 0) goto loc_00845160;
    if (((unsigned int)(v_rsi)) != ((unsigned int)((unsigned int)(a6)))) goto loc_0084528E;
    v_stack_m1C8 = v_stack_m88;
    goto loc_0084517A;
loc_0084523B:
    if (*(unsigned __int64 *)(v_rip + 7020486) == 0) goto loc_008451C6;
    if (v_stack_m1E0 <= ((unsigned int)(0x6E566D43ULL))) goto loc_00845157;
    if (*(unsigned __int64 *)(v_rip + 7020486) == 0) goto loc_008451C6;
    if (v_stack_m1D0 <= ((unsigned int)(0x6E566D43ULL))) goto loc_00845157;
    goto loc_008451C6;
loc_00845279:
    if (((unsigned __int16)(v_stack_m1E8)) <= 64) goto loc_008452B9;
    if (((unsigned int)((unsigned int)(a6))) > 64) goto loc_008451DF;
    goto loc_008451E9;
loc_0084528E:
    v_stack_m1C8 = v_stack_m1B8;
    if (((unsigned int)(v_stack_m1B8)) != ((unsigned int)((unsigned __int16)(v_stack_m1E8)))) goto loc_008452CF;
    goto loc_0084517A;
loc_008452AF:
    v_stack_m1E0 = 0;
    goto loc_008451A3;
loc_008452B9:
    v_rsi = v_stack_m88;
    if (((unsigned int)((unsigned int)(a6))) < ((unsigned int)(v_stack_m88))) { v_rsi = (unsigned int)((unsigned int)(a6)); }
    goto loc_008451E9;
loc_008452C5:
    v_stack_m1D0 = 0;
    goto loc_008451C6;
loc_008452CF:
    v_rsi = ((unsigned int)((unsigned int)(v_stack_m1C8))) + (v_stack_m1B8);
    goto loc_0084517A;
loc_008452D9:
    v_stack_m1F4 = (unsigned int)((unsigned int)(0xC000009AULL));
    v_r14 = 0;
    goto loc_008454DC;
loc_008452EE:
    v_stack_m1F4 = (unsigned int)((unsigned int)(0xC000000DULL));
    v_r14 = 0;
    goto loc_008454DC;
loc_00845303:
    goto loc_008450E8;
loc_00845311:
    goto loc_00845110;
loc_0084531F:
    v_stack_m1E8 = v_xmm0;
    v_stack_m1C8 = 0;
    if ((unsigned int)((unsigned int)(a6)) == 0) goto loc_00845353;
    goto loc_00845110;
loc_00845353:
    goto loc_00845115;
loc_0084535D:
    v_stack_m1F4 = (unsigned int)((unsigned int)(0xC000000DULL));
    v_r14 = 0;
    goto loc_008454DC;
loc_0084539E:
    if ((unsigned __int16)(v_stack_m1E8) == 0) goto loc_008453C0;
loc_008453A9:
    a1 = ((unsigned __int16)(v_stack_m1E8)) >> (1);
    if ((*(unsigned __int16 *)(v_stack_m1E0 + a1 * 2 - 2)) == 0) goto loc_008457A5;
loc_008453C0:
    if (sign_flag) goto loc_00845634;
    v_stack_m1F7 = 1;
    if ((*(unsigned int *)(v_rip + 6989719)) == 0) goto loc_00845488;
    result = CmpIsRegistryLockAcquired(*(unsigned __int64 *)(v_stack_m1D8 + 8), v_stack_m1E8, (unsigned int)(0xFFFEULL), v_stack_m1E8 + *(unsigned __int64 *)(a1 + 8) * 1);
    if ((unsigned int)(result) != 0) goto loc_00845488;
    v_stack_mE8 = v_stack_m1D8;
    v_stack_mE0 = v_stack_m1E8;
    v_stack_mD8 = (unsigned int)((unsigned int)(v_stack_m1B0));
    v_stack_mD4 = (unsigned int)((unsigned int)(v_stack_m1BC));
    v_stack_mD0 = v_stack_m1D0;
    v_stack_mC8 = 0;
    v_stack_m208 = v_stack_m198;
    v_stack_m210 = v_stack_m1D8;
    v_stack_m218 = 16;
    a3 = 0;
    result = CmpCallCallBacksEx(a3 + 1, v_stack_mE8, a3, 1);
    if (sign_flag) goto loc_00845649;
loc_00845488:
    if (0 != 0) goto loc_0084570A;
loc_00845491:
    result = (unsigned int)(((unsigned int)(v_stack_m1A8)) >> (2));
    result = (unsigned __int8)((result) & (1));
    v_stack_m208 = (unsigned __int8)(result);
    v_stack_m210 = v_stack_m1A0;
    v_stack_m218 = 0;
    result = CmSetValueKey(v_stack_m1D8, v_stack_m1E8, (unsigned int)(v_stack_m1BC), v_stack_m1D0);
    v_stack_m1F4 = (unsigned int)(result);
loc_008454D6:
loc_008454DC:
    if (0 != 0) {
        a1 = v_stack_m158;
        result = SeReleaseSubjectContext(a1, v_stack_m1E8, (unsigned int)(v_stack_m1BC), v_stack_m1D0);
    }
    if (1 == 0) goto loc_008455B0;
    if ((*(unsigned int *)(v_rip + 6989450)) == 0) goto loc_008455AC;
    result = CmpIsRegistryLockAcquired(a1, v_stack_m1E8, (unsigned int)(v_stack_m1BC), v_stack_m1D0);
    if ((unsigned int)(result) != 0) goto loc_008455AC;
    result = v_stack_m198;
    v_rdi = (unsigned int)((unsigned int)(result));
    if (v_stack_m198 != v_stack_m198) {
        v_stack_m12C = 0;
        v_stack_m11C = v_xmm0;
        v_stack_m10C = 0;
        v_stack_m104 = 0;
        a1 = v_stack_m1D8;
        v_stack_m138 = a1;
        v_stack_m130 = (unsigned int)((unsigned int)((unsigned int)(result)));
        v_stack_m120 = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = v_stack_mE8;
        v_stack_m128 = result;
        result = v_stack_m198;
        v_stack_m208 = result;
        v_stack_m210 = a1;
        v_stack_m218 = 16;
        a4 = 0;
        a3 = 0;
        a2 = v_stack_m138;
        a1 = a4 + 16;
        result = CmpCallCallBacksEx(a1, a2, a3, a4);
        v_rdi = v_stack_m120;
    }
    v_stack_m1F4 = (unsigned int)(v_rdi);
loc_008455B0:
    if ((unsigned __int8)(v_stack_m1F7) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = KeLeaveCriticalRegionThread(a1, a2, a3, a4);
        v_rdi = v_stack_m1F4;
    }
    if (v_stack_m1D8 != 0) {
        result = ObfDereferenceObject(v_stack_m1D8, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rip + 7940651) != 0) goto loc_00845660;
loc_008455E2:
    result = v_stack_m1B8;
    if (v_stack_m1B8 != 0) {
        a1 = v_stack_m1B8;
        result = CmSiFreeMemory(a1, a2, a3, a4);
    }
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        result = CmpReleaseShutdownRundown(a1, a2, a3, a4);
    }
    result = CmCleanupThreadInfo(v_stack_m100, a2, a3, a4);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (512);
    return result;
loc_00845634:
    v_stack_p44 = (unsigned int)((unsigned int)(0xC0000022ULL));
    v_r14 = 0;
    goto loc_008454DC;
loc_00845649:
    v_rdi = 0;
    if (((unsigned int)(result)) != 0xC0000503ULL) { v_rdi = (unsigned int)(result); }
    v_stack_p44 = (unsigned int)(v_rdi);
    goto loc_008454D6;
loc_00845660:
    v_stack_p28 = v_stack_p50;
    v_stack_p20 = v_stack_pB8;
    a4 = 0;
    result = guard_dispatch_icall(14, v_stack_p190, (unsigned int)((unsigned int)(v_rdi)), a4);
    goto loc_008455E2;
loc_00845691:
    if (v_stack_p60 == 0) goto loc_00845055;
    v_stack_pB8 = *(unsigned __int64 *)(v_stack_p60 + 8);
    goto loc_00845055;
loc_008456B0:
    result = SeCaptureSubjectContext(v_stack_pE0, v_stack_p190, (unsigned int)((unsigned int)(v_rdi)), a4);
    if ((*(unsigned __int8 *)(v_rip + 6067674)) == 0) goto loc_008456EE;
    result = CmpIsSystemEntity(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), v_stack_pE0, v_stack_p78, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00845748;
loc_008456EE:
    v_stack_p44 = (unsigned int)((unsigned int)(0xC0000022ULL));
    goto loc_008454DC;
loc_008456FC:
    v_stack_p44 = (unsigned int)((unsigned int)(0xC0000189ULL));
    goto loc_008454DC;
loc_0084570A:
    v_stack_p20 = v_stack_p78;
    result = CmKeyBodyReplicateToVirtual(v_stack_p60, v_stack_p40, 2, v_stack_pE0);
    v_stack_p44 = (unsigned int)(result);
    if (!sign_flag) goto loc_00845491;
    goto loc_008454D6;
loc_00845748:
    v_stack_p28 = v_stack_p90;
    v_stack_p20 = v_stack_p60;
    result = CmObReferenceObjectByHandle(v_stack_p98, (unsigned int)(0x20019ULL), 2, v_stack_p40);
    v_stack_p44 = (unsigned int)(result);
    if (sign_flag) goto loc_008454DC;
    result = CmKeyBodyNeedsVirtualImage(v_stack_p60, (unsigned int)(0x20019ULL), 2, v_stack_p40);
    if ((unsigned __int8)(result) == 0) goto loc_008456EE;
    v_stack_p41 = 0;
    goto loc_0084503C;
loc_008457A5:
    a2 = (unsigned __int16)(((unsigned int)(0x20019ULL)) + (2));
    v_stack_p50 = (unsigned __int16)(a2);
    if (condition_is_not_equal) goto loc_008453A9;
    goto loc_008453C0;
}
```

## 5. (Beta) C Style

```c
int64_t NtSetValueKey(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m104;
    uint64_t v_stack_m10C;
    uint64_t v_stack_m11C;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m12C;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint32_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m1BC;
    uint32_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint16_t v_stack_m1E6;
    uint64_t v_stack_m1E8;
    uint8_t v_stack_m1F0;
    uint32_t v_stack_m1F4;
    uint8_t v_stack_m1F7;
    uint8_t v_stack_m1F8;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m48;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_p190;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p40;
    uint8_t v_stack_p41;
    uint32_t v_stack_p44;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;
    uint64_t v_stack_p78;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pE0;

    local_rsp = (local_rsp) - (512);
    result = (*(uint64_t *)(v_rip + 0x5C5886)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m1BC = Arg4;
    v_stack_m1B0 = Arg3;
    v_stack_m188 = Arg2;
    v_stack_m1A0 = Arg1;
    v_stack_m1D0 = Arg5;
    result = 0;
    v_stack_m100 = v_xmm0;
    v_stack_mF0 = 0;
    v_stack_m1E8 = v_xmm0;
    local_rbx = 0;
    v_stack_m1A8 = 0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    v_stack_m180 = 0;
    if ((*(uint64_t *)(v_rip + 0x7930D6)) != 0) {
        Arg2 = 0x20000ULL;
        Arg1 = v_stack_mA8;
        result = EtwGetKernelTraceTimestamp(Arg1, Arg2, Arg3, Arg4);
    }
    result = CmpInitializeThreadInfo(v_stack_m100, Arg2, Arg3, Arg4);
    local_r13 = 0;
    local_r14 = 0;
    v_stack_m1D8 = 0;
    local_r15 = 0;
    v_stack_m1F7 = 0;
    v_stack_m190 = v_stack_m198;
    v_stack_m198 = v_stack_m198;
    Arg2 = 0;
    result = memset(v_stack_mE8, Arg2, Arg2 + 64, Arg4);
    Arg2 = 0;
    result = RtlInitUnicodeString(v_stack_m1E8, Arg2, Arg2 + 64, Arg4);
    v_stack_m1C8 = 0;
    v_stack_m178 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1F8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    local_rsi = 0;
    v_stack_m158 = v_xmm0;
    v_stack_m148 = v_xmm0;
    result = CmpAcquireShutdownRundown(v_stack_m1E8, Arg2, Arg2 + 64, Arg4);
    v_stack_m1F0 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_008456FC;
    v_stack_m210 = v_stack_m1A8;
    v_stack_m218 = v_stack_m1D8;
    result = CmObReferenceObjectByHandle(v_stack_m1A0, 2, Arg2 + 64, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_m1F4 = (uint32_t)(result);
    if (((uint32_t)(result)) == 0xC0000022ULL) goto loc_008456B0;
loc_0084503C:
    if (sign_flag) goto loc_008454DC;
    if ((*(uint64_t *)(v_rip + 0x792FB9)) != 0) goto loc_00845691;
loc_00845055:
    if (((uint8_t)(v_stack_m1F8)) != 1) goto loc_0084531F;
    v_stack_m168 = v_xmm0;
    Arg1 = local_r10;
    if (v_stack_m188 < local_r10) { Arg1 = v_stack_m188; }
    v_stack_m168 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    v_stack_m160 = *(uint64_t *)(Arg1 + 0x8);
    v_stack_m1E8 = v_xmm0;
    v_stack_m1E6 = (uint16_t)((uint32_t)(*(uint32_t *)(Arg1)));
    if ((uint16_t)(v_stack_m1E8) == 0) goto loc_008450E8;
    result = (uint32_t)(*(uint32_t *)(Arg1));
    if ((((uint8_t)(*(uint64_t *)(Arg1 + 0x8))) & (1)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, v_stack_m1E8, *(uint64_t *)(Arg1 + 0x8), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    if ((v_stack_m1E8 + *(uint64_t *)(Arg1 + 0x8) * 1) > local_r10) goto loc_00845303;
    if ((v_stack_m1E8 + *(uint64_t *)(Arg1 + 0x8) * 1) < (*(uint64_t *)(Arg1 + 0x8))) goto loc_00845303;
loc_008450E8:
    if ((uint32_t)((uint32_t)(Arg6)) == 0) goto loc_00845110;
    if ((v_stack_m1D0 + (uint32_t)(Arg6) * 1) > local_r10) goto loc_00845311;
    if ((v_stack_m1D0 + (uint32_t)(Arg6) * 1) < v_stack_m1D0) goto loc_00845311;
loc_00845110:
loc_00845115:
    if (((uint16_t)(v_stack_m1E8)) > ((uint16_t)((uint32_t)(0x7FFFULL)))) goto loc_0084535D;
    if ((((uint8_t)(v_stack_m1E8)) & (1)) != 0) goto loc_0084535D;
    if (((uint32_t)((uint32_t)(Arg6))) > 0x7FFFF000ULL) goto loc_0084535D;
    local_rdi = (uint32_t)(((uint16_t)(v_stack_m1E8) + 7) & (0xFFFFFFF8ULL));
    if (((uint32_t)(local_rdi + (uint32_t)(Arg6) * 1)) < ((uint32_t)((uint32_t)(Arg6)))) goto loc_008452EE;
    if ((uint8_t)(v_stack_m1F8) == 0) goto loc_0084523B;
loc_00845157:
    if ((uint32_t)(local_rdi + (uint32_t)(Arg6) * 1) == 0) goto loc_008451CB;
    if (((uint32_t)(local_rdi + (uint32_t)(Arg6) * 1)) > 64) goto loc_008451D5;
loc_00845160:
    v_stack_m1C8 = v_stack_m88;
    local_rsi = (v_stack_m88) + ((uint32_t)((uint32_t)(local_rdi)));
loc_0084517A:
    if ((uint16_t)(v_stack_m1E8) == 0) goto loc_008452AF;
    result = memcpy(v_stack_m1C8, v_stack_m1E0, (uint16_t)(v_stack_m1E8), v_stack_m1E8 + *(uint64_t *)(Arg1 + 0x8) * 1);
    v_stack_m1E0 = v_stack_m1C8;
loc_008451A3:
    if ((uint32_t)((uint32_t)(Arg6)) == 0) goto loc_008452C5;
    result = memcpy(local_rsi, v_stack_m1D0, (uint32_t)((uint32_t)((uint32_t)(Arg6))), v_stack_m1E8 + *(uint64_t *)(Arg1 + 0x8) * 1);
    v_stack_m1D0 = local_rsi;
loc_008451C6:
    goto loc_0084539E;
loc_008451CB:
    goto loc_0084517A;
loc_008451D5:
    if (((uint32_t)((uint32_t)(Arg6))) <= 64) goto loc_00845279;
loc_008451DF:
    local_rsi = (uint32_t)((uint32_t)(result));
    if (((uint16_t)(v_stack_m1E8)) <= 64) { local_rsi = (uint32_t)((uint32_t)(Arg6)); }
loc_008451E9:
    if ((uint32_t)(local_rsi) == 0) goto loc_00845160;
    result = CmpAllocateTransientPoolWithQuota(local_rsi, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0x6E566D43ULL), v_stack_m1E8 + *(uint64_t *)(Arg1 + 0x8) * 1);
    v_stack_m1B8 = result;
    if (result == 0) goto loc_008452D9;
    if ((uint32_t)(local_rsi) == 0) goto loc_00845160;
    if (((uint32_t)(local_rsi)) != ((uint32_t)((uint32_t)(Arg6)))) goto loc_0084528E;
    v_stack_m1C8 = v_stack_m88;
    goto loc_0084517A;
loc_0084523B:
    if (*(uint64_t *)(v_rip + 0x6B1FC6) == 0) goto loc_008451C6;
    if (v_stack_m1E0 <= ((uint32_t)(0x6E566D43ULL))) goto loc_00845157;
    if (*(uint64_t *)(v_rip + 0x6B1FC6) == 0) goto loc_008451C6;
    if (v_stack_m1D0 <= ((uint32_t)(0x6E566D43ULL))) goto loc_00845157;
    goto loc_008451C6;
loc_00845279:
    if (((uint16_t)(v_stack_m1E8)) <= 64) goto loc_008452B9;
    if (((uint32_t)((uint32_t)(Arg6))) > 64) goto loc_008451DF;
    goto loc_008451E9;
loc_0084528E:
    v_stack_m1C8 = v_stack_m1B8;
    if (((uint32_t)(v_stack_m1B8)) != ((uint32_t)((uint16_t)(v_stack_m1E8)))) goto loc_008452CF;
    goto loc_0084517A;
loc_008452AF:
    v_stack_m1E0 = 0;
    goto loc_008451A3;
loc_008452B9:
    local_rsi = v_stack_m88;
    if (((uint32_t)((uint32_t)(Arg6))) < ((uint32_t)(v_stack_m88))) { local_rsi = (uint32_t)((uint32_t)(Arg6)); }
    goto loc_008451E9;
loc_008452C5:
    v_stack_m1D0 = 0;
    goto loc_008451C6;
loc_008452CF:
    local_rsi = ((uint32_t)((uint32_t)(v_stack_m1C8))) + (v_stack_m1B8);
    goto loc_0084517A;
loc_008452D9:
    v_stack_m1F4 = (uint32_t)((uint32_t)(0xC000009AULL));
    local_r14 = 0;
    goto loc_008454DC;
loc_008452EE:
    v_stack_m1F4 = (uint32_t)((uint32_t)(0xC000000DULL));
    local_r14 = 0;
    goto loc_008454DC;
loc_00845303:
    goto loc_008450E8;
loc_00845311:
    goto loc_00845110;
loc_0084531F:
    v_stack_m1E8 = v_xmm0;
    v_stack_m1C8 = 0;
    if ((uint32_t)((uint32_t)(Arg6)) == 0) goto loc_00845353;
    goto loc_00845110;
loc_00845353:
    goto loc_00845115;
loc_0084535D:
    v_stack_m1F4 = (uint32_t)((uint32_t)(0xC000000DULL));
    local_r14 = 0;
    goto loc_008454DC;
loc_0084539E:
    if ((uint16_t)(v_stack_m1E8) == 0) goto loc_008453C0;
loc_008453A9:
    Arg1 = ((uint16_t)(v_stack_m1E8)) >> (1);
    if ((*(uint16_t *)(v_stack_m1E0 + Arg1 * 2 - 0x2)) == 0) goto loc_008457A5;
loc_008453C0:
    if (sign_flag) goto loc_00845634;
    v_stack_m1F7 = 1;
    if ((*(uint32_t *)(v_rip + 0x6AA797)) == 0) goto loc_00845488;
    result = CmpIsRegistryLockAcquired(*(uint64_t *)(v_stack_m1D8 + 0x8), v_stack_m1E8, (uint32_t)(0xFFFEULL), v_stack_m1E8 + *(uint64_t *)(Arg1 + 0x8) * 1);
    if ((uint32_t)(result) != 0) goto loc_00845488;
    v_stack_mE8 = v_stack_m1D8;
    v_stack_mE0 = v_stack_m1E8;
    v_stack_mD8 = (uint32_t)((uint32_t)(v_stack_m1B0));
    v_stack_mD4 = (uint32_t)((uint32_t)(v_stack_m1BC));
    v_stack_mD0 = v_stack_m1D0;
    v_stack_mC8 = 0;
    v_stack_m208 = v_stack_m198;
    v_stack_m210 = v_stack_m1D8;
    v_stack_m218 = 16;
    Arg3 = 0;
    result = CmpCallCallBacksEx(Arg3 + 1, v_stack_mE8, Arg3, 1);
    if (sign_flag) goto loc_00845649;
loc_00845488:
    if (0 != 0) goto loc_0084570A;
loc_00845491:
    result = (uint32_t)(((uint32_t)(v_stack_m1A8)) >> (2));
    result = (uint8_t)((result) & (1));
    v_stack_m208 = (uint8_t)(result);
    v_stack_m210 = v_stack_m1A0;
    v_stack_m218 = 0;
    result = CmSetValueKey(v_stack_m1D8, v_stack_m1E8, (uint32_t)(v_stack_m1BC), v_stack_m1D0);
    v_stack_m1F4 = (uint32_t)(result);
loc_008454D6:
loc_008454DC:
    if (0 != 0) {
        Arg1 = v_stack_m158;
        result = SeReleaseSubjectContext(Arg1, v_stack_m1E8, (uint32_t)(v_stack_m1BC), v_stack_m1D0);
    }
    if (1 == 0) goto loc_008455B0;
    if ((*(uint32_t *)(v_rip + 0x6AA68A)) == 0) goto loc_008455AC;
    result = CmpIsRegistryLockAcquired(Arg1, v_stack_m1E8, (uint32_t)(v_stack_m1BC), v_stack_m1D0);
    if ((uint32_t)(result) != 0) goto loc_008455AC;
    result = v_stack_m198;
    local_rdi = (uint32_t)((uint32_t)(result));
    if (v_stack_m198 != v_stack_m198) {
        v_stack_m12C = 0;
        v_stack_m11C = v_xmm0;
        v_stack_m10C = 0;
        v_stack_m104 = 0;
        Arg1 = v_stack_m1D8;
        v_stack_m138 = Arg1;
        v_stack_m130 = (uint32_t)((uint32_t)((uint32_t)(result)));
        v_stack_m120 = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = v_stack_mE8;
        v_stack_m128 = result;
        result = v_stack_m198;
        v_stack_m208 = result;
        v_stack_m210 = Arg1;
        v_stack_m218 = 16;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_stack_m138;
        Arg1 = Arg4 + 16;
        result = CmpCallCallBacksEx(Arg1, Arg2, Arg3, Arg4);
        local_rdi = v_stack_m120;
    }
    v_stack_m1F4 = (uint32_t)(local_rdi);
loc_008455B0:
    if ((uint8_t)(v_stack_m1F7) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = KeLeaveCriticalRegionThread(Arg1, Arg2, Arg3, Arg4);
        local_rdi = v_stack_m1F4;
    }
    if (v_stack_m1D8 != 0) {
        result = ObfDereferenceObject(v_stack_m1D8, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(v_rip + 0x792A2B) != 0) goto loc_00845660;
loc_008455E2:
    result = v_stack_m1B8;
    if (v_stack_m1B8 != 0) {
        Arg1 = v_stack_m1B8;
        result = CmSiFreeMemory(Arg1, Arg2, Arg3, Arg4);
    }
    if ((uint8_t)((uint8_t)(result)) != 0) {
        result = CmpReleaseShutdownRundown(Arg1, Arg2, Arg3, Arg4);
    }
    result = CmCleanupThreadInfo(v_stack_m100, Arg2, Arg3, Arg4);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (512);
    return result;
loc_00845634:
    v_stack_p44 = (uint32_t)((uint32_t)(0xC0000022ULL));
    local_r14 = 0;
    goto loc_008454DC;
loc_00845649:
    local_rdi = 0;
    if (((uint32_t)(result)) != 0xC0000503ULL) { local_rdi = (uint32_t)(result); }
    v_stack_p44 = (uint32_t)(local_rdi);
    goto loc_008454D6;
loc_00845660:
    v_stack_p28 = v_stack_p50;
    v_stack_p20 = v_stack_pB8;
    Arg4 = 0;
    result = guard_dispatch_icall(14, v_stack_p190, (uint32_t)((uint32_t)(local_rdi)), Arg4);
    goto loc_008455E2;
loc_00845691:
    if (v_stack_p60 == 0) goto loc_00845055;
    v_stack_pB8 = *(uint64_t *)(v_stack_p60 + 0x8);
    goto loc_00845055;
loc_008456B0:
    result = SeCaptureSubjectContext(v_stack_pE0, v_stack_p190, (uint32_t)((uint32_t)(local_rdi)), Arg4);
    if ((*(uint8_t *)(v_rip + 0x5C95DA)) == 0) goto loc_008456EE;
    result = CmpIsSystemEntity(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), v_stack_pE0, v_stack_p78, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00845748;
loc_008456EE:
    v_stack_p44 = (uint32_t)((uint32_t)(0xC0000022ULL));
    goto loc_008454DC;
loc_008456FC:
    v_stack_p44 = (uint32_t)((uint32_t)(0xC0000189ULL));
    goto loc_008454DC;
loc_0084570A:
    v_stack_p20 = v_stack_p78;
    result = CmKeyBodyReplicateToVirtual(v_stack_p60, v_stack_p40, 2, v_stack_pE0);
    v_stack_p44 = (uint32_t)(result);
    if (!sign_flag) goto loc_00845491;
    goto loc_008454D6;
loc_00845748:
    v_stack_p28 = v_stack_p90;
    v_stack_p20 = v_stack_p60;
    result = CmObReferenceObjectByHandle(v_stack_p98, (uint32_t)(0x20019ULL), 2, v_stack_p40);
    v_stack_p44 = (uint32_t)(result);
    if (sign_flag) goto loc_008454DC;
    result = CmKeyBodyNeedsVirtualImage(v_stack_p60, (uint32_t)(0x20019ULL), 2, v_stack_p40);
    if ((uint8_t)(result) == 0) goto loc_008456EE;
    v_stack_p41 = 0;
    goto loc_0084503C;
loc_008457A5:
    Arg2 = (uint16_t)(((uint32_t)(0x20019ULL)) + (2));
    v_stack_p50 = (uint16_t)(Arg2);
    if (condition_is_not_equal) goto loc_008453A9;
    goto loc_008453C0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00844EA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
