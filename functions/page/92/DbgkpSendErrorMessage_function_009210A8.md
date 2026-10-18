# DbgkpSendErrorMessage

- RVA: `0x009210A8`–`0x00921581` (길이 `1,241` bytes)
- VA: `0x00000001409210A8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008CFC4`
- 디코드: `305`개 명령, `1,241/1,241` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **27**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x009210EB` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0092111B` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (function, `0x0044BEE0`)
- `0x00921126` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (function, `0x002250A0`)
- `0x0092113C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00921165` → [MmGetSectionInformation](MmGetSectionInformation_function_00921910.md) (function, `0x00921910`)
- `0x0092116D` → [PsGetServerSiloServiceSessionId](../../text/45/PsGetServerSiloServiceSessionId_function_0045ED00.md) (function, `0x0045ED00`)
- `0x00921177` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x0092118F` → [DbgkpSuspendProcess](../8A/DbgkpSuspendProcess_function_008A34D4.md) (function, `0x008A34D4`)
- `0x00921198` → [DbgkpStartSystemErrorHandler](DbgkpStartSystemErrorHandler_function_00920F78.md) (function, `0x00920F78`)
- `0x009211DA` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00921227` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00921248` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00921282` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x009212A6` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x009212AE` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009212B6` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00921305` → [KeCopyExceptionRecord](../../text/43/KeCopyExceptionRecord_function_00439750.md) (function, `0x00439750`)
- `0x009213BC` → [PsTestProtectedProcessIncompatibility](../A1/PsTestProtectedProcessIncompatibility_function_00A1003C.md) (function, `0x00A1003C`)
- `0x009213DB` → [AlpcInitializeMessageAttribute](../../text/45/AlpcInitializeMessageAttribute_function_00450050.md) (function, `0x00450050`)
- `0x009213EB` → [AlpcGetMessageAttribute](../../text/45/AlpcGetMessageAttribute_function_00450010.md) (function, `0x00450010`)
- `0x00921421` → [KeTestAlertThread](../../text/41/KeTestAlertThread_function_0041C590.md) (function, `0x0041C590`)
- `0x0092144A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00921452` → [DbgkpDereferenceErrorPort](../../text/57/DbgkpDereferenceErrorPort_function_0057FD58.md) (function, `0x0057FD58`)
- `0x00921485` → [ZwAlpcSendWaitReceivePort](../../text/6A/ZwAlpcSendWaitReceivePort_function_006AE290.md) (function, `0x006AE290`)
- `0x009214A0` → [DbgkpRemoveErrorPort](../71/DbgkpRemoveErrorPort_function_00711038.md) (function, `0x00711038`)
- `0x009214DD` → [ZwAlpcSendWaitReceivePort](../../text/6A/ZwAlpcSendWaitReceivePort_function_006AE290.md) (function, `0x006AE290`)
- `0x00921510` → [DbgkpResumeProcess](../A7/DbgkpResumeProcess_function_00A7954C.md) (function, `0x00A7954C`)
- `0x00921523` → [DbgkForwardException](../8A/DbgkForwardException_function_008A2D60.md) (function, `0x008A2D60`)
- `0x00921552` → [DbgkpResumeProcess](../A7/DbgkpResumeProcess_function_00A7954C.md) (function, `0x00A7954C`)
- `0x00921560` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_006F88AE](../../text/6F/Unknown_function_006F88AE.md) at `0x006F8ABD`
- [DbgkForwardException](../8A/DbgkForwardException_function_008A2D60.md) at `0x008A30FC`

### Static image references
- `0x009210C4` → RVA `0x00E0A740` (`.data`; read)
- `0x009211A7` → RVA `0x00FC51DC` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **22**
  - `0x009210EB` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0092111B` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (`PAGE` → `.text`)
  - `0x00921126` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (`PAGE` → `.text`)
  - `0x0092113C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0092116D` → [PsGetServerSiloServiceSessionId](../../text/45/PsGetServerSiloServiceSessionId_function_0045ED00.md) (`PAGE` → `.text`)
  - `0x00921177` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x009211DA` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00921227` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00921248` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00921282` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x009212A6` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x009212AE` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009212B6` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00921305` → [KeCopyExceptionRecord](../../text/43/KeCopyExceptionRecord_function_00439750.md) (`PAGE` → `.text`)
  - `0x009213DB` → [AlpcInitializeMessageAttribute](../../text/45/AlpcInitializeMessageAttribute_function_00450050.md) (`PAGE` → `.text`)
  - `0x009213EB` → [AlpcGetMessageAttribute](../../text/45/AlpcGetMessageAttribute_function_00450010.md) (`PAGE` → `.text`)
  - `0x00921421` → [KeTestAlertThread](../../text/41/KeTestAlertThread_function_0041C590.md) (`PAGE` → `.text`)
  - `0x0092144A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00921452` → [DbgkpDereferenceErrorPort](../../text/57/DbgkpDereferenceErrorPort_function_0057FD58.md) (`PAGE` → `.text`)
  - `0x00921485` → [ZwAlpcSendWaitReceivePort](../../text/6A/ZwAlpcSendWaitReceivePort_function_006AE290.md) (`PAGE` → `.text`)
  - `0x009214DD` → [ZwAlpcSendWaitReceivePort](../../text/6A/ZwAlpcSendWaitReceivePort_function_006AE290.md) (`PAGE` → `.text`)
  - `0x00921560` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009210A8  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
009210AD  55                              push rbp
009210AE  56                              push rsi
009210AF  57                              push rdi
009210B0  41 54                           push r12
009210B2  41 55                           push r13
009210B4  41 56                           push r14
009210B6  41 57                           push r15
009210B8  48 8D 6C 24 D0                  lea rbp, [rsp - 0x30]
009210BD  48 81 EC 30 01 00 00            sub rsp, 0x130
009210C4  48 8B 05 75 96 4E 00            mov rax, qword ptr [rip + 0x4e9675]
009210CB  48 33 C4                        xor rax, rsp
009210CE  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
009210D2  44 8B F2                        mov r14d, edx
009210D5  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
009210D9  33 D2                           xor edx, edx
009210DB  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
009210E0  4D 8B F8                        mov r15, r8
009210E3  48 8D 4D C0                     lea rcx, [rbp - 0x40]
009210E7  44 8D 42 60                     lea r8d, [rdx + 0x60]
009210EB  E8 50 5B DA FF                  call 0x1406c6c40
009210F0  45 33 ED                        xor r13d, r13d
009210F3  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
009210F8  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
009210FD  65 4C 8B 24 25 88 01 00 00      mov r12, qword ptr gs:[0x188]
00921106  44 88 6C 24 40                  mov byte ptr [rsp + 0x40], r13b
0092110B  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
00921110  49 8B B4 24 20 02 00 00         mov rsi, qword ptr [r12 + 0x220]
00921118  48 8B CE                        mov rcx, rsi
0092111B  E8 C0 AD B2 FF                  call 0x14044bee0
00921120  48 8B C8                        mov rcx, rax
00921123  48 8B D8                        mov rbx, rax
00921126  E8 75 3F 90 FF                  call 0x1402250a0
0092112B  33 D2                           xor edx, edx
0092112D  45 8D 45 40                     lea r8d, [r13 + 0x40]
00921131  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00921135  48 8D B8 A8 03 00 00            lea rdi, [rax + 0x3a8]
0092113C  E8 FF 5A DA FF                  call 0x1406c6c40
00921141  8B 86 FC 05 00 00               mov eax, dword ptr [rsi + 0x5fc]
00921147  A8 01                           test al, 1
00921149  74 0A                           je 0x140921155
0092114B  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00921150  E9 02 04 00 00                  jmp 0x140921557
00921155  48 8B 8E A8 02 00 00            mov rcx, qword ptr [rsi + 0x2a8]
0092115C  4C 8D 45 80                     lea r8, [rbp - 0x80]
00921160  BA 01 00 00 00                  mov edx, 1
00921165  E8 A6 07 00 00                  call 0x140921910
0092116A  48 8B CB                        mov rcx, rbx
0092116D  E8 8E DB B3 FF                  call 0x14045ed00
00921172  48 8B CE                        mov rcx, rsi
00921175  8B D8                           mov ebx, eax
00921177  E8 74 E7 90 FF                  call 0x14022f8f0
0092117C  3B C3                           cmp eax, ebx
0092117E  74 18                           je 0x140921198
00921180  83 7D A0 01                     cmp dword ptr [rbp - 0x60], 1
00921184  74 12                           je 0x140921198
00921186  41 F6 C6 02                     test r14b, 2
0092118A  74 0C                           je 0x140921198
0092118C  48 8B CE                        mov rcx, rsi
0092118F  E8 40 23 F8 FF                  call 0x1408a34d4
00921194  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00921198  E8 DB FD FF FF                  call 0x140920f78
0092119D  8B D8                           mov ebx, eax
0092119F  85 C0                           test eax, eax
009211A1  0F 88 9E 03 00 00               js 0x140921545
009211A7  48 63 0D 2E 40 6A 00            movsxd rcx, dword ptr [rip + 0x6a402e]
009211AE  83 F9 FF                        cmp ecx, -1
009211B1  74 13                           je 0x1409211c6
009211B3  48 69 D1 F0 D8 FF FF            imul rdx, rcx, -0x2710
009211BA  48 8D 44 24 60                  lea rax, [rsp + 0x60]
009211BF  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
009211C4  EB 03                           jmp 0x1409211c9
009211C6  49 8B C5                        mov rax, r13
009211C9  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
009211CD  45 33 C9                        xor r9d, r9d
009211D0  41 B0 01                        mov r8b, 1
009211D3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009211D8  33 D2                           xor edx, edx
009211DA  E8 D1 D4 8E FF                  call 0x14020e6b0
009211DF  3D 02 01 00 00                  cmp eax, 0x102
009211E4  0F 84 56 03 00 00               je 0x140921540
009211EA  4C 39 6F 08                     cmp qword ptr [rdi + 8], r13
009211EE  0F 84 4C 03 00 00               je 0x140921540
009211F4  3D 01 01 00 00                  cmp eax, 0x101
009211F9  0F 84 3A 03 00 00               je 0x140921539
009211FF  3D C0 00 00 00                  cmp eax, 0xc0
00921204  0F 84 2F 03 00 00               je 0x140921539
0092120A  66 41 FF 8C 24 E4 01 00 00      dec word ptr [r12 + 0x1e4]
00921213  45 33 C0                        xor r8d, r8d
00921216  33 D2                           xor edx, edx
00921218  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
0092121D  48 8B CF                        mov rcx, rdi
00921220  90                              nop
00921221  41 8B DD                        mov ebx, r13d
00921224  4D 8B F5                        mov r14, r13
00921227  E8 04 F0 8E FF                  call 0x140210230
0092122C  4C 8B E8                        mov r13, rax
0092122F  B9 11 00 00 00                  mov ecx, 0x11
00921234  33 C0                           xor eax, eax
00921236  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
0092123B  74 10                           je 0x14092124d
0092123D  4C 8B CF                        mov r9, rdi
00921240  4D 8B C5                        mov r8, r13
00921243  33 D2                           xor edx, edx
00921245  48 8B CF                        mov rcx, rdi
00921248  E8 FF F1 8E FF                  call 0x14021044c
0092124D  33 C9                           xor ecx, ecx
0092124F  4D 85 ED                        test r13, r13
00921252  74 05                           je 0x140921259
00921254  41 C6 45 0A 01                  mov byte ptr [r13 + 0xa], 1
00921259  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0092125D  48 3B F0                        cmp rsi, rax
00921260  75 07                           jne 0x140921269
00921262  BB 94 01 00 C0                  mov ebx, 0xc0000194
00921267  EB 2B                           jmp 0x140921294
00921269  4C 8B 77 08                     mov r14, qword ptr [rdi + 8]
0092126D  4D 85 F6                        test r14, r14
00921270  74 1D                           je 0x14092128f
00921272  BA 44 62 67 50                  mov edx, 0x50676244
00921277  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0092127C  48 8B C8                        mov rcx, rax
0092127F  4C 8B E8                        mov r13, rax
00921282  E8 89 F4 8E FF                  call 0x140210710
00921287  F0 41 FF 06                     lock inc dword ptr [r14]
0092128B  33 C9                           xor ecx, ecx
0092128D  EB 08                           jmp 0x140921297
0092128F  BB 53 03 00 C0                  mov ebx, 0xc0000353
00921294  4C 8B E9                        mov r13, rcx
00921297  B8 11 00 00 00                  mov eax, 0x11
0092129C  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
009212A1  74 08                           je 0x1409212ab
009212A3  48 8B CF                        mov rcx, rdi
009212A6  E8 95 21 94 FF                  call 0x140263440
009212AB  48 8B CF                        mov rcx, rdi
009212AE  E8 4D 03 9C FF                  call 0x1402e1600
009212B3  49 8B CC                        mov rcx, r12
009212B6  E8 35 DD 93 FF                  call 0x14025eff0
009212BB  45 33 E4                        xor r12d, r12d
009212BE  85 DB                           test ebx, ebx
009212C0  0F 88 7F 02 00 00               js 0x140921545
009212C6  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
009212CB  49 8D 4F 30                     lea rcx, [r15 + 0x30]
009212CF  4D 89 67 08                     mov qword ptr [r15 + 8], r12
009212D3  4D 89 67 10                     mov qword ptr [r15 + 0x10], r12
009212D7  4D 89 67 18                     mov qword ptr [r15 + 0x18], r12
009212DB  4D 89 67 20                     mov qword ptr [r15 + 0x20], r12
009212DF  41 C7 47 04 08 00 00 00         mov dword ptr [r15 + 4], 8
009212E7  66 41 C7 47 04 07 80            mov word ptr [r15 + 4], 0x8007
009212EE  41 C7 07 E8 00 10 01            mov dword ptr [r15], 0x11000e8
009212F5  41 C7 47 28 07 00 00 00         mov dword ptr [r15 + 0x28], 7
009212FD  41 C7 47 2C 01 00 01 80         mov dword ptr [r15 + 0x2c], 0x80010001
00921305  E8 46 84 B1 FF                  call 0x140439750
0092130A  0F 28 45 80                     movaps xmm0, xmmword ptr [rbp - 0x80]
0092130E  0F 28 4D 90                     movaps xmm1, xmmword ptr [rbp - 0x70]
00921312  41 0F 11 87 C8 00 00 00         movups xmmword ptr [r15 + 0xc8], xmm0
0092131A  45 89 A7 08 01 00 00            mov dword ptr [r15 + 0x108], r12d
00921321  0F 28 45 A0                     movaps xmm0, xmmword ptr [rbp - 0x60]
00921325  41 0F 11 8F D8 00 00 00         movups xmmword ptr [r15 + 0xd8], xmm1
0092132D  0F 28 4D B0                     movaps xmm1, xmmword ptr [rbp - 0x50]
00921331  41 0F 11 87 E8 00 00 00         movups xmmword ptr [r15 + 0xe8], xmm0
00921339  41 0F 11 8F F8 00 00 00         movups xmmword ptr [r15 + 0xf8], xmm1
00921341  F6 86 FA 05 00 00 07            test byte ptr [rsi + 0x5fa], 7
00921348  77 05                           ja 0x14092134f
0092134A  41 8B CC                        mov ecx, r12d
0092134D  EB 10                           jmp 0x14092135f
0092134F  41 C7 87 08 01 00 00 01 00 00 00  mov dword ptr [r15 + 0x108], 1
0092135A  B9 01 00 00 00                  mov ecx, 1
0092135F  F6 86 70 01 00 00 01            test byte ptr [rsi + 0x170], 1
00921366  74 0A                           je 0x140921372
00921368  83 C9 08                        or ecx, 8
0092136B  41 89 8F 08 01 00 00            mov dword ptr [r15 + 0x108], ecx
00921372  4C 39 A6 10 03 00 00            cmp qword ptr [rsi + 0x310], r12
00921379  74 25                           je 0x1409213a0
0092137B  0F B7 86 EC 06 00 00            movzx eax, word ptr [rsi + 0x6ec]
00921382  BA 4C 01 00 00                  mov edx, 0x14c
00921387  66 3B C2                        cmp ax, dx
0092138A  74 0A                           je 0x140921396
0092138C  BA C4 01 00 00                  mov edx, 0x1c4
00921391  66 3B C2                        cmp ax, dx
00921394  75 0A                           jne 0x1409213a0
00921396  83 C9 02                        or ecx, 2
00921399  41 89 8F 08 01 00 00            mov dword ptr [r15 + 0x108], ecx
009213A0  F6 44 24 50 01                  test byte ptr [rsp + 0x50], 1
009213A5  74 0D                           je 0x1409213b4
009213A7  83 C9 04                        or ecx, 4
009213AA  41 B4 01                        mov r12b, 1
009213AD  41 89 8F 08 01 00 00            mov dword ptr [r15 + 0x108], ecx
009213B4  4C 8B C6                        mov r8, rsi
009213B7  49 8B D5                        mov rdx, r13
009213BA  B1 01                           mov cl, 1
009213BC  E8 7B EC 0E 00                  call 0x140a1003c
009213C1  41 BD 00 00 00 10               mov r13d, 0x10000000
009213C7  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
009213CC  41 8B CD                        mov ecx, r13d
009213CF  48 8D 55 80                     lea rdx, [rbp - 0x80]
009213D3  41 B8 A0 00 00 00               mov r8d, 0xa0
009213D9  8A D8                           mov bl, al
009213DB  E8 70 EC B2 FF                  call 0x140450050
009213E0  41 8B D5                        mov edx, r13d
009213E3  44 89 6D 84                     mov dword ptr [rbp - 0x7c], r13d
009213E7  48 8D 4D 80                     lea rcx, [rbp - 0x80]
009213EB  E8 20 EC B2 FF                  call 0x140450010
009213F0  F6 DB                           neg bl
009213F2  1B C9                           sbb ecx, ecx
009213F4  33 DB                           xor ebx, ebx
009213F6  81 E1 01 1C F0 FF               and ecx, 0xfff01c01
009213FC  C7 40 10 04 00 00 00            mov dword ptr [rax + 0x10], 4
00921403  81 C1 FF FF 1F 00               add ecx, 0x1fffff
00921409  48 C7 40 08 FE FF FF FF         mov qword ptr [rax + 8], 0xfffffffffffffffe
00921411  89 48 14                        mov dword ptr [rax + 0x14], ecx
00921414  33 C9                           xor ecx, ecx
00921416  89 18                           mov dword ptr [rax], ebx
00921418  48 C7 44 24 58 10 01 00 00      mov qword ptr [rsp + 0x58], 0x110
00921421  E8 6A B1 AF FF                  call 0x14041c590
00921426  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
0092142B  41 8B 85 A0 05 00 00            mov eax, dword ptr [r13 + 0x5a0]
00921432  A8 01                           test al, 1
00921434  74 26                           je 0x14092145c
00921436  BB 4B 00 00 C0                  mov ebx, 0xc000004b
0092143B  40 8A 7C 24 40                  mov dil, byte ptr [rsp + 0x40]
00921440  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00921445  BA 44 62 67 50                  mov edx, 0x50676244
0092144A  E8 91 64 9D FF                  call 0x1402f78e0
0092144F  49 8B CE                        mov rcx, r14
00921452  E8 01 E9 C5 FF                  call 0x14057fd58
00921457  E9 EE 00 00 00                  jmp 0x14092154a
0092145C  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
00921460  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00921465  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
0092146A  4C 8D 4D 80                     lea r9, [rbp - 0x80]
0092146E  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
00921473  4D 8B C7                        mov r8, r15
00921476  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0092147B  BA 00 00 22 00                  mov edx, 0x220000
00921480  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00921485  E8 06 CE D8 FF                  call 0x1406ae290
0092148A  8B D8                           mov ebx, eax
0092148C  85 C0                           test eax, eax
0092148E  79 17                           jns 0x1409214a7
00921490  3D 37 00 00 C0                  cmp eax, 0xc0000037
00921495  75 A4                           jne 0x14092143b
00921497  4D 8B C6                        mov r8, r14
0092149A  48 8B D7                        mov rdx, rdi
0092149D  49 8B CD                        mov rcx, r13
009214A0  E8 93 FB DE FF                  call 0x140711038
009214A5  EB 94                           jmp 0x14092143b
009214A7  3D 01 01 00 00                  cmp eax, 0x101
009214AC  74 88                           je 0x140921436
009214AE  45 33 ED                        xor r13d, r13d
009214B1  66 41 0F BA 67 04 0D            bt word ptr [r15 + 4], 0xd
009214B8  73 28                           jae 0x1409214e2
009214BA  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
009214BE  45 33 C9                        xor r9d, r9d
009214C1  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
009214C6  4D 8B C7                        mov r8, r15
009214C9  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
009214CE  BA 00 00 01 00                  mov edx, 0x10000
009214D3  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
009214D8  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
009214DD  E8 AE CD D8 FF                  call 0x1406ae290
009214E2  41 8B 5F 2C                     mov ebx, dword ptr [r15 + 0x2c]
009214E6  85 DB                           test ebx, ebx
009214E8  0F 88 4D FF FF FF               js 0x14092143b
009214EE  45 84 E4                        test r12b, r12b
009214F1  0F 85 44 FF FF FF               jne 0x14092143b
009214F7  81 FB 02 00 01 00               cmp ebx, 0x10002
009214FD  0F 85 38 FF FF FF               jne 0x14092143b
00921503  40 8A 7C 24 40                  mov dil, byte ptr [rsp + 0x40]
00921508  40 84 FF                        test dil, dil
0092150B  74 0B                           je 0x140921518
0092150D  48 8B CE                        mov rcx, rsi
00921510  E8 37 80 15 00                  call 0x140a7954c
00921515  41 8A FD                        mov dil, r13b
00921518  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0092151D  41 B0 01                        mov r8b, 1
00921520  41 8A D0                        mov dl, r8b
00921523  E8 38 18 F8 FF                  call 0x1408a2d60
00921528  F6 D8                           neg al
0092152A  1B DB                           sbb ebx, ebx
0092152C  F7 D3                           not ebx
0092152E  81 E3 44 01 00 C0               and ebx, 0xc0000144
00921534  E9 07 FF FF FF                  jmp 0x140921440
00921539  BB 4B 00 00 C0                  mov ebx, 0xc000004b
0092153E  EB 05                           jmp 0x140921545
00921540  BB 53 03 00 C0                  mov ebx, 0xc0000353
00921545  40 8A 7C 24 40                  mov dil, byte ptr [rsp + 0x40]
0092154A  40 84 FF                        test dil, dil
0092154D  74 08                           je 0x140921557
0092154F  48 8B CE                        mov rcx, rsi
00921552  E8 F5 7F 15 00                  call 0x140a7954c
00921557  8B C3                           mov eax, ebx
00921559  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
0092155D  48 33 CC                        xor rcx, rsp
00921560  E8 DB B0 D8 FF                  call 0x1406ac640
00921565  48 8B 9C 24 78 01 00 00         mov rbx, qword ptr [rsp + 0x178]
0092156D  48 81 C4 30 01 00 00            add rsp, 0x130
00921574  41 5F                           pop r15
00921576  41 5E                           pop r14
00921578  41 5D                           pop r13
0092157A  41 5C                           pop r12
0092157C  5F                              pop rdi
0092157D  5E                              pop rsi
0092157E  5D                              pop rbp
0092157F  C3                              ret
00921580  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DbgkpSendErrorMessage(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int8 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE4;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 5150325)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m118 = a2;
    a2 = 0;
    v_stack_m100 = a1;
    result = memset(v_stack_mA8, a2, a2 + 96, a4);
    v_r13 = 0;
    v_stack_m110 = 0;
    v_stack_m108 = 0;
    v_stack_m128 = 0;
    v_stack_mF8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = PsGetProcessServerSilo(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), a2, a2 + 96, a4);
    result = PsGetServerSiloGlobals(result, a2, a2 + 96, a4);
    a2 = 0;
    result = memset(v_stack_mE8, a2, v_r13 + 64, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 1532)))) & (1)) == 0) goto loc_00921155;
    goto loc_00921557;
loc_00921155:
    result = MmGetSectionInformation(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 680), 1, v_stack_mE8, a4);
    result = PsGetServerSiloServiceSessionId((unsigned int)(0xC00000BBULL), 1, v_stack_mE8, a4);
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), 1, v_stack_mE8, a4);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_00921198;
    if (v_stack_mC8 == 1) goto loc_00921198;
    if ((((unsigned __int8)((unsigned int)(a2))) & (2)) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544);
        result = DbgkpSuspendProcess(a1, 1, v_stack_mE8, a4);
        v_stack_m128 = (unsigned __int8)(result);
    }
    result = DbgkpStartSystemErrorHandler(a1, 1, v_stack_mE8, a4);
    if (sign_flag) goto loc_00921545;
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 6963246)))) == -1) goto loc_009211C6;
    a2 = (1) * ((int)(*(unsigned int *)(v_rip + 6963246)));
    v_stack_m108 = a2;
    goto loc_009211C9;
loc_009211C6:
loc_009211C9:
    a4 = 0;
    v_stack_m148 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(*(unsigned __int64 *)(result + 936 + 24), a2, 1, a4);
    if (((unsigned int)(result)) == 258) goto loc_00921540;
    if ((*(unsigned __int64 *)(result + 936 + 8)) == 0) goto loc_00921540;
    if (((unsigned int)(result)) == 257) goto loc_00921539;
    if (((unsigned int)(result)) == 192) goto loc_00921539;
    a3 = 0;
    a2 = 0;
    v_stack_m120 = 0;
    result = KeAbPreAcquire(result + 936, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = result + 936;
        a3 = 0;
        a2 = 0;
        a1 = result + 936;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    a1 = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544)) != (*(unsigned __int64 *)(result + 936 + 16))) goto loc_00921269;
    goto loc_00921294;
loc_00921269:
    if (*(unsigned __int64 *)(result + 936 + 8) == 0) goto loc_0092128F;
    v_stack_m120 = *(unsigned __int64 *)(result + 936 + 16);
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(result + 936 + 16), (unsigned int)(0x50676244ULL), a3, a4);
    a1 = 0;
    goto loc_00921297;
loc_0092128F:
loc_00921294:
loc_00921297:
    result = 17;
    if (!(condition_is_equal)) {
        a1 = result + 936;
        result = ExfReleasePushLockShared(a1, (unsigned int)(0x50676244ULL), a3, a4);
    }
    result = KeAbPostRelease(result + 936, (unsigned int)(0x50676244ULL), a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x50676244ULL), a3, a4);
    v_r12 = 0;
    if (sign_flag) goto loc_00921545;
    *(unsigned __int64 *)(a3 + 8) = 0;
    *(unsigned __int64 *)(a3 + 16) = 0;
    *(unsigned __int64 *)(a3 + 24) = 0;
    *(unsigned __int64 *)(a3 + 32) = 0;
    *(unsigned int *)(a3 + 4) = 8;
    *(unsigned __int16 *)(a3 + 4) = 0x8007ULL;
    *(unsigned int *)(a3) = 0x11000E8ULL;
    *(unsigned int *)(a3 + 40) = 7;
    *(unsigned int *)(a3 + 44) = 0x80010001ULL;
    result = KeCopyExceptionRecord(a3 + 48, v_stack_m100, a3, a4);
    *(unsigned __int64 *)(a3 + 200) = v_xmm0;
    *(unsigned int *)(a3 + 264) = 0;
    *(unsigned __int64 *)(a3 + 216) = v_xmm1;
    *(unsigned __int64 *)(a3 + 232) = v_xmm0;
    *(unsigned __int64 *)(a3 + 248) = v_xmm1;
    if (condition_is_above) goto loc_0092134F;
    goto loc_0092135F;
loc_0092134F:
    *(unsigned int *)(a3 + 264) = 1;
loc_0092135F:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 368)) & (1)) != 0) {
        a1 = (unsigned int)((1) | (8));
        *(unsigned int *)(a3 + 264) = (unsigned int)(a1);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 784)) == 0) goto loc_009213A0;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 1772))) == 332) goto loc_00921396;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 1772))) == 452) {
        a1 = (unsigned int)((a1) | (2));
        *(unsigned int *)(a3 + 264) = (unsigned int)(a1);
    }
    if (((v_stack_m118) & (1)) != 0) {
        a1 = (unsigned int)((a1) | (4));
        v_r12 = 1;
        *(unsigned int *)(a3 + 264) = (unsigned int)(a1);
    }
    result = PsTestProtectedProcessIncompatibility(1, 0, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), a4);
    result = AlpcInitializeMessageAttribute((unsigned int)((unsigned int)((unsigned int)(0x10000000ULL))), v_stack_mE8, 160, v_stack_m110);
    v_stack_mE4 = (unsigned int)((unsigned int)(0x10000000ULL));
    result = AlpcGetMessageAttribute(v_stack_mE8, (unsigned int)((unsigned int)((unsigned int)(0x10000000ULL))), 160, v_stack_m110);
    v_rbx = (unsigned __int8)(-((unsigned __int8)(result)));
    v_rbx = 0;
    a1 = (unsigned int)((v_stack_mE8) & (0xFFF01C01ULL));
    *(unsigned int *)(result + 16) = 4;
    a1 = (unsigned int)((a1) + (0x1FFFFFULL));
    *(unsigned __int64 *)(result + 8) = -2;
    *(unsigned int *)(result + 20) = (unsigned int)(a1);
    a1 = 0;
    *(unsigned int *)(result) = 0;
    v_stack_m110 = 272;
    result = KeTestAlertThread(a1, (unsigned int)((unsigned int)((unsigned int)(0x10000000ULL))), 160, v_stack_m110);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mF8 + 1440)))) & (1)) == 0) goto loc_0092145C;
loc_00921436:
loc_0092143B:
loc_00921440:
    result = ObfDereferenceObjectWithTag(v_stack_m120, (unsigned int)(0x50676244ULL), 160, v_stack_m110);
    result = DbgkpDereferenceErrorPort(*(unsigned __int64 *)(result + 936 + 8), (unsigned int)(0x50676244ULL), 160, v_stack_m110);
    goto loc_0092154A;
loc_0092145C:
    v_stack_m130 = (unsigned int)(0xC000004BULL);
    v_stack_m138 = (unsigned int)(0xC000004BULL);
    v_stack_m140 = v_stack_m110;
    v_stack_m148 = a3;
    result = ZwAlpcSendWaitReceivePort(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 936 + 8) + 8), (unsigned int)(0x220000ULL), a3, v_stack_mE8);
    if (!sign_flag) goto loc_009214A7;
    if (((unsigned int)(result)) != 0xC0000037ULL) goto loc_0092143B;
    result = DbgkpRemoveErrorPort(v_stack_mF8, v_stack_m128, *(unsigned __int64 *)(result + 936 + 8), v_stack_mE8);
    goto loc_0092143B;
loc_009214A7:
    if (((unsigned int)(result)) == 257) goto loc_00921436;
    v_r13 = 0;
    if (!(condition_is_above_or_equal)) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 936 + 8) + 8);
        a4 = 0;
        v_stack_m130 = 0;
        a3 = a3;
        v_stack_m138 = 0;
        a2 = 0x10000ULL;
        v_stack_m140 = 0;
        v_stack_m148 = 0;
        result = ZwAlpcSendWaitReceivePort(a1, a2, a3, a4);
    }
    if (sign_flag) goto loc_0092143B;
    if ((unsigned __int8)(v_r12) != 0) goto loc_0092143B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 44)))) != 0x10002ULL) goto loc_0092143B;
    v_rdi = v_stack_m128;
    if ((unsigned __int8)(v_stack_m128) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544);
        result = DbgkpResumeProcess(a1, a2, a3, a4);
        v_rdi = 0;
    }
    result = DbgkForwardException(v_stack_m100, 1, 1, a4);
    result = (unsigned __int8)(-(result));
    v_rbx = (unsigned int)(~((unsigned int)(*(unsigned int *)(a3 + 44))));
    v_rbx = (unsigned int)((v_rbx) & (0xC0000144ULL));
    goto loc_00921440;
loc_00921539:
    goto loc_00921545;
loc_00921540:
loc_00921545:
loc_0092154A:
    if ((unsigned __int8)(v_stack_m128) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544);
        result = DbgkpResumeProcess(a1, 1, 1, a4);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, 1, a4);
    v_rsp = (v_rsp) + (304);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DbgkpSendErrorMessage(int64_t Arg1, int32_t Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m120;
    uint8_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m48;
    uint64_t v_stack_m68;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE4;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x4E9675)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m118 = Arg2;
    Arg2 = 0;
    v_stack_m100 = Arg1;
    result = memset(v_stack_mA8, Arg2, Arg2 + 96, Arg4);
    local_r13 = 0;
    v_stack_m110 = 0;
    v_stack_m108 = 0;
    v_stack_m128 = 0;
    v_stack_mF8 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = PsGetProcessServerSilo(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), Arg2, Arg2 + 96, Arg4);
    result = PsGetServerSiloGlobals(result, Arg2, Arg2 + 96, Arg4);
    Arg2 = 0;
    result = memset(v_stack_mE8, Arg2, local_r13 + 64, Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x5FC)))) & (1)) == 0) goto loc_00921155;
    goto loc_00921557;
loc_00921155:
    result = MmGetSectionInformation(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A8), 1, v_stack_mE8, Arg4);
    result = PsGetServerSiloServiceSessionId((uint32_t)(0xC00000BBULL), 1, v_stack_mE8, Arg4);
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), 1, v_stack_mE8, Arg4);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_00921198;
    if (v_stack_mC8 == 1) goto loc_00921198;
    if ((((uint8_t)((uint32_t)(Arg2))) & (2)) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220);
        result = DbgkpSuspendProcess(Arg1, 1, v_stack_mE8, Arg4);
        v_stack_m128 = (uint8_t)(result);
    }
    result = DbgkpStartSystemErrorHandler(Arg1, 1, v_stack_mE8, Arg4);
    if (sign_flag) goto loc_00921545;
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0x6A402E)))) == -1) goto loc_009211C6;
    Arg2 = (1) * ((int32_t)(*(uint32_t *)(v_rip + 0x6A402E)));
    v_stack_m108 = Arg2;
    goto loc_009211C9;
loc_009211C6:
loc_009211C9:
    Arg4 = 0;
    v_stack_m148 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(*(uint64_t *)(result + 0x3A8 + 0x18), Arg2, 1, Arg4);
    if (((uint32_t)(result)) == 258) goto loc_00921540;
    if ((*(uint64_t *)(result + 0x3A8 + 0x8)) == 0) goto loc_00921540;
    if (((uint32_t)(result)) == 257) goto loc_00921539;
    if (((uint32_t)(result)) == 192) goto loc_00921539;
    Arg3 = 0;
    Arg2 = 0;
    v_stack_m120 = 0;
    result = KeAbPreAcquire(result + 936, Arg2, Arg3, Arg4);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = result + 936;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = result + 936;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220)) != (*(uint64_t *)(result + 0x3A8 + 0x10))) goto loc_00921269;
    goto loc_00921294;
loc_00921269:
    if (*(uint64_t *)(result + 0x3A8 + 0x8) == 0) goto loc_0092128F;
    v_stack_m120 = *(uint64_t *)(result + 0x3A8 + 0x10);
    result = ObfReferenceObjectWithTag(*(uint64_t *)(result + 0x3A8 + 0x10), (uint32_t)(0x50676244ULL), Arg3, Arg4);
    Arg1 = 0;
    goto loc_00921297;
loc_0092128F:
loc_00921294:
loc_00921297:
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = result + 936;
        result = ExfReleasePushLockShared(Arg1, (uint32_t)(0x50676244ULL), Arg3, Arg4);
    }
    result = KeAbPostRelease(result + 936, (uint32_t)(0x50676244ULL), Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x50676244ULL), Arg3, Arg4);
    local_r12 = 0;
    if (sign_flag) goto loc_00921545;
    *(uint64_t *)(arg3 + 0x8) = 0;
    *(uint64_t *)(arg3 + 0x10) = 0;
    *(uint64_t *)(arg3 + 0x18) = 0;
    *(uint64_t *)(arg3 + 0x20) = 0;
    *(uint32_t *)(arg3 + 0x4) = 8;
    *(uint16_t *)(arg3 + 0x4) = 0x8007ULL;
    *(uint32_t *)(arg3) = 0x11000E8ULL;
    *(uint32_t *)(arg3 + 0x28) = 7;
    *(uint32_t *)(arg3 + 0x2C) = 0x80010001ULL;
    result = KeCopyExceptionRecord(Arg3 + 48, v_stack_m100, Arg3, Arg4);
    *(uint64_t *)(arg3 + 0xC8) = v_xmm0;
    *(uint32_t *)(arg3 + 0x108) = 0;
    *(uint64_t *)(arg3 + 0xD8) = v_xmm1;
    *(uint64_t *)(arg3 + 0xE8) = v_xmm0;
    *(uint64_t *)(arg3 + 0xF8) = v_xmm1;
    if (condition_is_above) goto loc_0092134F;
    goto loc_0092135F;
loc_0092134F:
    *(uint32_t *)(arg3 + 0x108) = 1;
loc_0092135F:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x170)) & (1)) != 0) {
        Arg1 = (uint32_t)((1) | (8));
        *(uint32_t *)(arg3 + 0x108) = (uint32_t)(Arg1);
    }
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x310)) == 0) goto loc_009213A0;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x6EC))) == 332) goto loc_00921396;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x6EC))) == 452) {
        Arg1 = (uint32_t)((Arg1) | (2));
        *(uint32_t *)(arg3 + 0x108) = (uint32_t)(Arg1);
    }
    if (((v_stack_m118) & (1)) != 0) {
        Arg1 = (uint32_t)((Arg1) | (4));
        local_r12 = 1;
        *(uint32_t *)(arg3 + 0x108) = (uint32_t)(Arg1);
    }
    result = PsTestProtectedProcessIncompatibility(1, 0, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), Arg4);
    result = AlpcInitializeMessageAttribute((uint32_t)((uint32_t)((uint32_t)(0x10000000ULL))), v_stack_mE8, 160, v_stack_m110);
    v_stack_mE4 = (uint32_t)((uint32_t)(0x10000000ULL));
    result = AlpcGetMessageAttribute(v_stack_mE8, (uint32_t)((uint32_t)((uint32_t)(0x10000000ULL))), 160, v_stack_m110);
    local_rbx = (uint8_t)(-((uint8_t)(result)));
    local_rbx = 0;
    Arg1 = (uint32_t)((v_stack_mE8) & (0xFFF01C01ULL));
    *(uint32_t *)(result + 0x10) = 4;
    Arg1 = (uint32_t)((Arg1) + (0x1FFFFFULL));
    *(uint64_t *)(result + 0x8) = -2;
    *(uint32_t *)(result + 0x14) = (uint32_t)(Arg1);
    Arg1 = 0;
    *(uint32_t *)(result) = 0;
    v_stack_m110 = 272;
    result = KeTestAlertThread(Arg1, (uint32_t)((uint32_t)((uint32_t)(0x10000000ULL))), 160, v_stack_m110);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mF8 + 0x5A0)))) & (1)) == 0) goto loc_0092145C;
loc_00921436:
loc_0092143B:
loc_00921440:
    result = ObfDereferenceObjectWithTag(v_stack_m120, (uint32_t)(0x50676244ULL), 160, v_stack_m110);
    result = DbgkpDereferenceErrorPort(*(uint64_t *)(result + 0x3A8 + 0x8), (uint32_t)(0x50676244ULL), 160, v_stack_m110);
    goto loc_0092154A;
loc_0092145C:
    v_stack_m130 = (uint32_t)(0xC000004BULL);
    v_stack_m138 = (uint32_t)(0xC000004BULL);
    v_stack_m140 = v_stack_m110;
    v_stack_m148 = Arg3;
    result = ZwAlpcSendWaitReceivePort(*(uint64_t *)(*(uint64_t *)(result + 0x3A8 + 0x8) + 0x8), (uint32_t)(0x220000ULL), Arg3, v_stack_mE8);
    if (!sign_flag) goto loc_009214A7;
    if (((uint32_t)(result)) != 0xC0000037ULL) goto loc_0092143B;
    result = DbgkpRemoveErrorPort(v_stack_mF8, v_stack_m128, *(uint64_t *)(result + 0x3A8 + 0x8), v_stack_mE8);
    goto loc_0092143B;
loc_009214A7:
    if (((uint32_t)(result)) == 257) goto loc_00921436;
    local_r13 = 0;
    if (!(condition_is_above_or_equal)) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(result + 0x3A8 + 0x8) + 0x8);
        Arg4 = 0;
        v_stack_m130 = 0;
        Arg3 = Arg3;
        v_stack_m138 = 0;
        Arg2 = 0x10000ULL;
        v_stack_m140 = 0;
        v_stack_m148 = 0;
        result = ZwAlpcSendWaitReceivePort(Arg1, Arg2, Arg3, Arg4);
    }
    if (sign_flag) goto loc_0092143B;
    if ((uint8_t)(local_r12) != 0) goto loc_0092143B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x2C)))) != 0x10002ULL) goto loc_0092143B;
    local_rdi = v_stack_m128;
    if ((uint8_t)(v_stack_m128) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220);
        result = DbgkpResumeProcess(Arg1, Arg2, Arg3, Arg4);
        local_rdi = 0;
    }
    result = DbgkForwardException(v_stack_m100, 1, 1, Arg4);
    result = (uint8_t)(-(result));
    local_rbx = (uint32_t)(~((uint32_t)(*(uint32_t *)(arg3 + 0x2C))));
    local_rbx = (uint32_t)((local_rbx) & (0xC0000144ULL));
    goto loc_00921440;
loc_00921539:
    goto loc_00921545;
loc_00921540:
loc_00921545:
loc_0092154A:
    if ((uint8_t)(v_stack_m128) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220);
        result = DbgkpResumeProcess(Arg1, 1, 1, Arg4);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, 1, Arg4);
    local_rsp = (local_rsp) + (304);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `W` |
| `Arg3` | `+ 0x4` | `16` | `R` |
| `Arg3` | `+ 0x4` | `16` | `W` |
| `Arg3` | `+ 0x4` | `32` | `W` |
| `Arg3` | `+ 0x8` | `64` | `W` |
| `Arg3` | `+ 0x10` | `64` | `W` |
| `Arg3` | `+ 0x18` | `64` | `W` |
| `Arg3` | `+ 0x20` | `64` | `W` |
| `Arg3` | `+ 0x28` | `32` | `W` |
| `Arg3` | `+ 0x2C` | `32` | `R` |
| `Arg3` | `+ 0x2C` | `32` | `W` |
| `Arg3` | `+ 0x30` | `64` | `R` |
| `Arg3` | `+ 0xC8` | `128` | `R` |
| `Arg3` | `+ 0xD8` | `128` | `R` |
| `Arg3` | `+ 0xE8` | `128` | `R` |
| `Arg3` | `+ 0xF8` | `128` | `R` |
| `Arg3` | `+ 0x108` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009210A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
