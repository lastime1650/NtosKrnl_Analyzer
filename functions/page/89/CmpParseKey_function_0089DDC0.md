# CmpParseKey

- RVA: `0x0089DDC0`–`0x0089E501` (길이 `1,857` bytes)
- VA: `0x000000014089DDC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007E818`
- 디코드: `424`개 명령, `1,857/1,857` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0089DE1B` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x0089DE51` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0089DEAF` → [CmpGetRegistryNamespaceRootForSilo](../9D/CmpGetRegistryNamespaceRootForSilo_function_009D0470.md) (function, `0x009D0470`)
- `0x0089DF5F` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x0089E027` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x0089E0A4` → [CmpDoParseKey](../85/CmpDoParseKey_function_0085F750.md) (function, `0x0085F750`)
- `0x0089E118` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x0089E189` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x0089E1D7` → [PsGetCurrentSilo](../../text/40/PsGetCurrentSilo_function_004094A0.md) (function, `0x004094A0`)
- `0x0089E1E9` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0089E1FE` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x0089E338` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x0089E3A9` → [CmpCallCallBacksEx](../86/CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x0089E43B` → [CmpAllocateParseContext](../87/CmpAllocateParseContext_function_008767B4.md) (function, `0x008767B4`)
- `0x0089E479` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0089E49C` → [CmpRollbackTransactionArray](../94/CmpRollbackTransactionArray_function_0094B3AC.md) (function, `0x0094B3AC`)
- `0x0089E4EF` → [CmpCleanupParseContext](../87/CmpCleanupParseContext_function_00876910.md) (function, `0x00876910`)
- `0x0089E4F7` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)

### Direct callers
- [ObpLookupObjectName](ObpLookupObjectName_function_0089BE90.md) at `0x0089C75E`

### Static image references
- `0x0089DE80` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)
- `0x0089DEA2` → RVA `0x00FD9B68` (`PAGEDATA`; read)
- `0x0089DF52` → RVA `0x00EEFB88` (`.data`; read)
- `0x0089E461` → RVA `0x00E09910` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x0089DE1B` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x0089DE51` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0089DF5F` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x0089E118` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x0089E1D7` → [PsGetCurrentSilo](../../text/40/PsGetCurrentSilo_function_004094A0.md) (`PAGE` → `.text`)
  - `0x0089E1E9` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0089E1FE` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x0089E338` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x0089E479` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x0089E4F7` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0089DDC0  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
0089DDC5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0089DDCA  55                              push rbp
0089DDCB  53                              push rbx
0089DDCC  56                              push rsi
0089DDCD  57                              push rdi
0089DDCE  41 54                           push r12
0089DDD0  41 55                           push r13
0089DDD2  41 56                           push r14
0089DDD4  41 57                           push r15
0089DDD6  48 8D AC 24 48 FF FF FF         lea rbp, [rsp - 0xb8]
0089DDDE  48 81 EC B8 01 00 00            sub rsp, 0x1b8
0089DDE5  4C 8B AD 48 01 00 00            mov r13, qword ptr [rbp + 0x148]
0089DDEC  0F 57 C0                        xorps xmm0, xmm0
0089DDEF  33 C0                           xor eax, eax
0089DDF1  0F 57 C9                        xorps xmm1, xmm1
0089DDF4  48 8B F1                        mov rsi, rcx
0089DDF7  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
0089DDFE  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
0089DE05  48 8B DA                        mov rbx, rdx
0089DE08  0F 11 85 90 00 00 00            movups xmmword ptr [rbp + 0x90], xmm0
0089DE0F  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
0089DE14  0F 11 8D 80 00 00 00            movups xmmword ptr [rbp + 0x80], xmm1
0089DE1B  E8 50 E0 B5 FF                  call 0x1403fbe70
0089DE20  48 8B 85 30 01 00 00            mov rax, qword ptr [rbp + 0x130]
0089DE27  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0089DE2B  33 FF                           xor edi, edi
0089DE2D  C6 85 00 01 00 00 00            mov byte ptr [rbp + 0x100], 0
0089DE34  33 D2                           xor edx, edx
0089DE36  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
0089DE3B  41 B8 88 00 00 00               mov r8d, 0x88
0089DE41  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
0089DE46  0F 10 10                        movups xmm2, xmmword ptr [rax]
0089DE49  44 8B FF                        mov r15d, edi
0089DE4C  0F 29 54 24 50                  movaps xmmword ptr [rsp + 0x50], xmm2
0089DE51  E8 EA 8D E2 FF                  call 0x1406c6c40
0089DE56  4C 8B A5 50 01 00 00            mov r12, qword ptr [rbp + 0x150]
0089DE5D  33 C0                           xor eax, eax
0089DE5F  4C 8B B5 38 01 00 00            mov r14, qword ptr [rbp + 0x138]
0089DE66  0F 57 C0                        xorps xmm0, xmm0
0089DE69  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0089DE6D  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0089DE72  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0089DE77  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0089DE7C  49 89 3C 24                     mov qword ptr [r12], rdi
0089DE80  48 3B 1D 39 8C 72 00            cmp rbx, qword ptr [rip + 0x728c39]
0089DE87  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0089DE8C  0F 11 45 80                     movups xmmword ptr [rbp - 0x80], xmm0
0089DE90  89 BD 30 01 00 00               mov dword ptr [rbp + 0x130], edi
0089DE96  89 BD 08 01 00 00               mov dword ptr [rbp + 0x108], edi
0089DE9C  0F 85 8F 05 00 00               jne 0x14089e431
0089DEA2  48 3B 35 BF BC 73 00            cmp rsi, qword ptr [rip + 0x73bcbf]
0089DEA9  75 0C                           jne 0x14089deb7
0089DEAB  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
0089DEAF  E8 BC 25 13 00                  call 0x1409d0470
0089DEB4  48 8B F0                        mov rsi, rax
0089DEB7  0F B7 4C 24 50                  movzx ecx, word ptr [rsp + 0x50]
0089DEBC  66 85 C9                        test cx, cx
0089DEBF  74 31                           je 0x14089def2
0089DEC1  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0089DEC6  41 B8 FE FF 00 00               mov r8d, 0xfffe
0089DECC  0F B7 C1                        movzx eax, cx
0089DECF  48 D1 E8                        shr rax, 1
0089DED2  66 83 7C 42 FE 5C               cmp word ptr [rdx + rax*2 - 2], 0x5c
0089DED8  0F 84 DC 04 00 00               je 0x14089e3ba
0089DEDE  66 85 C9                        test cx, cx
0089DEE1  74 0F                           je 0x14089def2
0089DEE3  0F B7 44 24 52                  movzx eax, word ptr [rsp + 0x52]
0089DEE8  66 83 3A 5C                     cmp word ptr [rdx], 0x5c
0089DEEC  0F 84 6A 03 00 00               je 0x14089e25c
0089DEF2  4D 85 F6                        test r14, r14
0089DEF5  0F 84 40 05 00 00               je 0x14089e43b
0089DEFB  8B 7E 60                        mov edi, dword ptr [rsi + 0x60]
0089DEFE  41 B9 DF FF 00 00               mov r9d, 0xffdf
0089DF04  41 23 7D 04                     and edi, dword ptr [r13 + 4]
0089DF08  41 89 7E 60                     mov dword ptr [r14 + 0x60], edi
0089DF0C  48 8B 0D 55 BC 73 00            mov rcx, qword ptr [rip + 0x73bc55]
0089DF13  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
0089DF17  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
0089DF1B  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0089DF20  49 3B D0                        cmp rdx, r8
0089DF23  0F 84 F1 02 00 00               je 0x14089e21a
0089DF29  41 F7 06 00 08 00 00            test dword ptr [r14], 0x800
0089DF30  0F 85 C0 04 00 00               jne 0x14089e3f6
0089DF36  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
0089DF39  A8 10                           test al, 0x10
0089DF3B  0F 85 44 03 00 00               jne 0x14089e285
0089DF41  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0089DF4A  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0089DF51  90                              nop
0089DF52  83 3D 2F 1C 65 00 00            cmp dword ptr [rip + 0x651c2f], 0
0089DF59  0F 84 E9 00 00 00               je 0x14089e048
0089DF5F  E8 18 8B BB FF                  call 0x140456a7c
0089DF64  85 C0                           test eax, eax
0089DF66  0F 85 DC 00 00 00               jne 0x14089e048
0089DF6C  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
0089DF73  4C 8D 45 80                     lea r8, [rbp - 0x80]
0089DF77  48 C7 45 58 01 00 00 00         mov qword ptr [rbp + 0x58], 1
0089DF7F  BA 00 00 00 00                  mov edx, 0
0089DF84  41 8B 46 1C                     mov eax, dword ptr [r14 + 0x1c]
0089DF88  41 B1 01                        mov r9b, 1
0089DF8B  89 45 68                        mov dword ptr [rbp + 0x68], eax
0089DF8E  8B 85 20 01 00 00               mov eax, dword ptr [rbp + 0x120]
0089DF94  89 45 6C                        mov dword ptr [rbp + 0x6c], eax
0089DF97  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0089DF9C  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
0089DFA0  0F B6 85 18 01 00 00            movzx eax, byte ptr [rbp + 0x118]
0089DFA7  88 45 70                        mov byte ptr [rbp + 0x70], al
0089DFAA  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
0089DFAE  89 45 08                        mov dword ptr [rbp + 8], eax
0089DFB1  48 8B 85 28 01 00 00            mov rax, qword ptr [rbp + 0x128]
0089DFB8  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0089DFBC  48 8B 05 FD 8A 72 00            mov rax, qword ptr [rip + 0x728afd]
0089DFC3  48 89 45 00                     mov qword ptr [rbp], rax
0089DFC7  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
0089DFCA  89 45 28                        mov dword ptr [rbp + 0x28], eax
0089DFCD  48 89 75 F8                     mov qword ptr [rbp - 8], rsi
0089DFD1  4C 89 65 38                     mov qword ptr [rbp + 0x38], r12
0089DFD5  49 8B 46 48                     mov rax, qword ptr [r14 + 0x48]
0089DFD9  A8 01                           test al, 1
0089DFDB  48 0F 45 C2                     cmovne rax, rdx
0089DFDF  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
0089DFE3  48 8D 45 F0                     lea rax, [rbp - 0x10]
0089DFE7  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0089DFEB  41 8B 46 60                     mov eax, dword ptr [r14 + 0x60]
0089DFEF  89 45 88                        mov dword ptr [rbp - 0x78], eax
0089DFF2  49 8D 86 90 00 00 00            lea rax, [r14 + 0x90]
0089DFF9  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0089DFFD  41 8B 06                        mov eax, dword ptr [r14]
0089E000  41 84 C1                        test r9b, al
0089E003  0F 85 CA 02 00 00               jne 0x14089e2d3
0089E009  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0089E00E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089E013  8D 4A 1C                        lea ecx, [rdx + 0x1c]
0089E016  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0089E01B  C7 44 24 20 1D 00 00 00         mov dword ptr [rsp + 0x20], 0x1d
0089E023  48 8D 55 F0                     lea rdx, [rbp - 0x10]
0089E027  E8 14 7F FC FF                  call 0x140865f40
0089E02C  8B D8                           mov ebx, eax
0089E02E  85 C0                           test eax, eax
0089E030  0F 88 59 02 00 00               js 0x14089e28f
0089E036  48 8B 75 F8                     mov rsi, qword ptr [rbp - 8]
0089E03A  8B 45 88                        mov eax, dword ptr [rbp - 0x78]
0089E03D  41 89 46 60                     mov dword ptr [r14 + 0x60], eax
0089E041  C6 85 00 01 00 00 01            mov byte ptr [rbp + 0x100], 1
0089E048  48 8B BD 10 01 00 00            mov rdi, qword ptr [rbp + 0x110]
0089E04F  0F 28 44 24 50                  movaps xmm0, xmmword ptr [rsp + 0x50]
0089E054  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0089E059  44 8B 8D 20 01 00 00            mov r9d, dword ptr [rbp + 0x120]
0089E060  48 8B D7                        mov rdx, rdi
0089E063  44 0F B6 85 18 01 00 00         movzx r8d, byte ptr [rbp + 0x118]
0089E06B  48 8B CE                        mov rcx, rsi
0089E06E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0089E073  48 8B 85 40 01 00 00            mov rax, qword ptr [rbp + 0x140]
0089E07A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0089E07F  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
0089E086  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
0089E08B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0089E090  48 8B 85 28 01 00 00            mov rax, qword ptr [rbp + 0x128]
0089E097  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0089E09C  66 0F 7F 85 80 00 00 00         movdqa xmmword ptr [rbp + 0x80], xmm0
0089E0A4  E8 A7 16 FC FF                  call 0x14085f750
0089E0A9  8B D8                           mov ebx, eax
0089E0AB  3D 03 01 00 00                  cmp eax, 0x103
0089E0B0  0F 84 9A 03 00 00               je 0x14089e450
0089E0B6  3D 2D 02 00 C0                  cmp eax, 0xc000022d
0089E0BB  0F 84 0D 03 00 00               je 0x14089e3ce
0089E0C1  8B 7E 60                        mov edi, dword ptr [rsi + 0x60]
0089E0C4  41 23 7D 04                     and edi, dword ptr [r13 + 4]
0089E0C8  85 C0                           test eax, eax
0089E0CA  78 12                           js 0x14089e0de
0089E0CC  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0089E0D1  49 89 04 24                     mov qword ptr [r12], rax
0089E0D5  48 C7 44 24 70 00 00 00 00      mov qword ptr [rsp + 0x70], 0
0089E0DE  80 BD 00 01 00 00 00            cmp byte ptr [rbp + 0x100], 0
0089E0E5  0F 84 D0 00 00 00               je 0x14089e1bb
0089E0EB  4C 8B BD 10 01 00 00            mov r15, qword ptr [rbp + 0x110]
0089E0F2  41 8B 47 14                     mov eax, dword ptr [r15 + 0x14]
0089E0F6  49 8D 77 14                     lea rsi, [r15 + 0x14]
0089E0FA  4D 8B 24 24                     mov r12, qword ptr [r12]
0089E0FE  89 45 2C                        mov dword ptr [rbp + 0x2c], eax
0089E101  41 8B 06                        mov eax, dword ptr [r14]
0089E104  A8 01                           test al, 1
0089E106  0F 85 23 02 00 00               jne 0x14089e32f
0089E10C  83 3D 75 1A 65 00 00            cmp dword ptr [rip + 0x651a75], 0
0089E113  4C 8B FE                        mov r15, rsi
0089E116  74 79                           je 0x14089e191
0089E118  E8 5F 89 BB FF                  call 0x140456a7c
0089E11D  85 C0                           test eax, eax
0089E11F  75 70                           jne 0x14089e191
0089E121  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0089E126  48 39 44 24 60                  cmp qword ptr [rsp + 0x60], rax
0089E12B  74 64                           je 0x14089e191
0089E12D  33 C0                           xor eax, eax
0089E12F  4C 89 65 98                     mov qword ptr [rbp - 0x68], r12
0089E133  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
0089E136  4C 8D 45 D0                     lea r8, [rbp - 0x30]
0089E13A  48 89 45 C4                     mov qword ptr [rbp - 0x3c], rax
0089E13E  48 8D 55 98                     lea rdx, [rbp - 0x68]
0089E142  89 45 CC                        mov dword ptr [rbp - 0x34], eax
0089E145  45 33 C9                        xor r9d, r9d
0089E148  48 8D 45 F0                     lea rax, [rbp - 0x10]
0089E14C  89 5D A0                        mov dword ptr [rbp - 0x60], ebx
0089E14F  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
0089E153  0F 57 C0                        xorps xmm0, xmm0
0089E156  48 8D 45 98                     lea rax, [rbp - 0x68]
0089E15A  89 5D B0                        mov dword ptr [rbp - 0x50], ebx
0089E15D  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0089E161  41 8D 49 1D                     lea ecx, [r9 + 0x1d]
0089E165  48 8D 45 80                     lea rax, [rbp - 0x80]
0089E169  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0089E16D  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0089E172  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089E177  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
0089E17C  C7 44 24 20 1D 00 00 00         mov dword ptr [rsp + 0x20], 0x1d
0089E184  F3 0F 7F 45 B4                  movdqu xmmword ptr [rbp - 0x4c], xmm0
0089E189  E8 B2 7D FC FF                  call 0x140865f40
0089E18E  8B 5D B0                        mov ebx, dword ptr [rbp - 0x50]
0089E191  85 DB                           test ebx, ebx
0089E193  78 0C                           js 0x14089e1a1
0089E195  8B 45 2C                        mov eax, dword ptr [rbp + 0x2c]
0089E198  41 3B 07                        cmp eax, dword ptr [r15]
0089E19B  0F 85 2E 03 00 00               jne 0x14089e4cf
0089E1A1  48 8B 8D 50 01 00 00            mov rcx, qword ptr [rbp + 0x150]
0089E1A8  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
0089E1AD  48 8B 09                        mov rcx, qword ptr [rcx]
0089E1B0  48 85 C9                        test rcx, rcx
0089E1B3  74 06                           je 0x14089e1bb
0089E1B5  8B 45 88                        mov eax, dword ptr [rbp - 0x78]
0089E1B8  89 41 60                        mov dword ptr [rcx + 0x60], eax
0089E1BB  81 FB 68 03 00 00               cmp ebx, 0x368
0089E1C1  75 08                           jne 0x14089e1cb
0089E1C3  33 C0                           xor eax, eax
0089E1C5  49 89 46 40                     mov qword ptr [r14 + 0x40], rax
0089E1C9  EB 11                           jmp 0x14089e1dc
0089E1CB  81 FB 04 01 00 00               cmp ebx, 0x104
0089E1D1  75 0D                           jne 0x14089e1e0
0089E1D3  41 89 7E 60                     mov dword ptr [r14 + 0x60], edi
0089E1D7  E8 C4 B2 B6 FF                  call 0x1404094a0
0089E1DC  49 89 45 08                     mov qword ptr [r13 + 8], rax
0089E1E0  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0089E1E9  E8 02 0E 9C FF                  call 0x14025eff0
0089E1EE  4D 85 FF                        test r15, r15
0089E1F1  0F 85 F3 02 00 00               jne 0x14089e4ea
0089E1F7  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
0089E1FE  E8 4D 1B B8 FF                  call 0x14041fd50
0089E203  8B C3                           mov eax, ebx
0089E205  48 81 C4 B8 01 00 00            add rsp, 0x1b8
0089E20C  41 5F                           pop r15
0089E20E  41 5E                           pop r14
0089E210  41 5D                           pop r13
0089E212  41 5C                           pop r12
0089E214  5F                              pop rdi
0089E215  5E                              pop rsi
0089E216  5B                              pop rbx
0089E217  5D                              pop rbp
0089E218  C3                              ret
0089E219  CC                              int3
0089E21A  66 83 7C 24 50 00               cmp word ptr [rsp + 0x50], 0
0089E220  0F 84 03 FD FF FF               je 0x14089df29
0089E226  0F B7 01                        movzx eax, word ptr [rcx]
0089E229  66 83 E8 41                     sub ax, 0x41
0089E22D  66 41 85 C1                     test r9w, ax
0089E231  0F 85 F2 FC FF FF               jne 0x14089df29
0089E237  66 83 7C 24 50 02               cmp word ptr [rsp + 0x50], 2
0089E23D  76 0B                           jbe 0x14089e24a
0089E23F  66 83 79 02 5C                  cmp word ptr [rcx + 2], 0x5c
0089E244  0F 85 DF FC FF FF               jne 0x14089df29
0089E24A  41 8B 06                        mov eax, dword ptr [r14]
0089E24D  A8 40                           test al, 0x40
0089E24F  0F 85 D4 FC FF FF               jne 0x14089df29
0089E255  BB 22 00 00 C0                  mov ebx, 0xc0000022
0089E25A  EB 92                           jmp 0x14089e1ee
0089E25C  48 83 C2 02                     add rdx, 2
0089E260  66 41 03 C8                     add cx, r8w
0089E264  66 41 03 C0                     add ax, r8w
0089E268  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
0089E26D  66 89 4C 24 50                  mov word ptr [rsp + 0x50], cx
0089E272  66 89 44 24 52                  mov word ptr [rsp + 0x52], ax
0089E277  66 85 C9                        test cx, cx
0089E27A  0F 85 68 FC FF FF               jne 0x14089dee8
0089E280  E9 6D FC FF FF                  jmp 0x14089def2
0089E285  41 83 4E 18 10                  or dword ptr [r14 + 0x18], 0x10
0089E28A  E9 B2 FC FF FF                  jmp 0x14089df41
0089E28F  81 FB 03 05 00 C0               cmp ebx, 0xc0000503
0089E295  0F 85 45 FF FF FF               jne 0x14089e1e0
0089E29B  8B 5D 8C                        mov ebx, dword ptr [rbp - 0x74]
0089E29E  81 FB 68 03 00 00               cmp ebx, 0x368
0089E2A4  0F 84 19 FF FF FF               je 0x14089e1c3
0089E2AA  81 FB 04 01 00 00               cmp ebx, 0x104
0089E2B0  0F 84 05 FF FF FF               je 0x14089e1bb
0089E2B6  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
0089E2BD  8B 45 2C                        mov eax, dword ptr [rbp + 0x2c]
0089E2C0  09 41 14                        or dword ptr [rcx + 0x14], eax
0089E2C3  0F BA E8 19                     bts eax, 0x19
0089E2C7  F7 D0                           not eax
0089E2C9  21 41 10                        and dword ptr [rcx + 0x10], eax
0089E2CC  33 DB                           xor ebx, ebx
0089E2CE  E9 0D FF FF FF                  jmp 0x14089e1e0
0089E2D3  41 0F B7 46 04                  movzx eax, word ptr [r14 + 4]
0089E2D8  66 89 45 E0                     mov word ptr [rbp - 0x20], ax
0089E2DC  66 89 45 E2                     mov word ptr [rbp - 0x1e], ax
0089E2E0  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0089E2E4  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0089E2E8  49 8D 46 20                     lea rax, [r14 + 0x20]
0089E2EC  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
0089E2F0  48 8D 45 E0                     lea rax, [rbp - 0x20]
0089E2F4  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0089E2F8  48 8B 41 40                     mov rax, qword ptr [rcx + 0x40]
0089E2FC  B9 1A 00 00 00                  mov ecx, 0x1a
0089E301  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
0089E305  48 8B 85 40 01 00 00            mov rax, qword ptr [rbp + 0x140]
0089E30C  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
0089E310  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0089E315  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089E31A  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0089E31F  C7 44 24 20 1B 00 00 00         mov dword ptr [rsp + 0x20], 0x1b
0089E327  89 55 E4                        mov dword ptr [rbp - 0x1c], edx
0089E32A  E9 F4 FC FF FF                  jmp 0x14089e023
0089E32F  83 3D 52 18 65 00 00            cmp dword ptr [rip + 0x651852], 0
0089E336  74 79                           je 0x14089e3b1
0089E338  E8 3F 87 BB FF                  call 0x140456a7c
0089E33D  85 C0                           test eax, eax
0089E33F  75 70                           jne 0x14089e3b1
0089E341  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0089E346  48 39 44 24 60                  cmp qword ptr [rsp + 0x60], rax
0089E34B  74 64                           je 0x14089e3b1
0089E34D  33 C0                           xor eax, eax
0089E34F  4C 89 65 98                     mov qword ptr [rbp - 0x68], r12
0089E353  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
0089E356  4C 8D 45 D0                     lea r8, [rbp - 0x30]
0089E35A  48 89 45 C4                     mov qword ptr [rbp - 0x3c], rax
0089E35E  48 8D 55 98                     lea rdx, [rbp - 0x68]
0089E362  89 45 CC                        mov dword ptr [rbp - 0x34], eax
0089E365  45 33 C9                        xor r9d, r9d
0089E368  48 8D 45 F0                     lea rax, [rbp - 0x10]
0089E36C  89 5D A0                        mov dword ptr [rbp - 0x60], ebx
0089E36F  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
0089E373  0F 57 C0                        xorps xmm0, xmm0
0089E376  48 8D 45 98                     lea rax, [rbp - 0x68]
0089E37A  89 5D B0                        mov dword ptr [rbp - 0x50], ebx
0089E37D  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0089E381  41 8D 49 1B                     lea ecx, [r9 + 0x1b]
0089E385  48 8D 45 80                     lea rax, [rbp - 0x80]
0089E389  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0089E38D  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0089E392  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089E397  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
0089E39C  C7 44 24 20 1B 00 00 00         mov dword ptr [rsp + 0x20], 0x1b
0089E3A4  F3 0F 7F 45 B4                  movdqu xmmword ptr [rbp - 0x4c], xmm0
0089E3A9  E8 92 7B FC FF                  call 0x140865f40
0089E3AE  8B 5D B0                        mov ebx, dword ptr [rbp - 0x50]
0089E3B1  49 83 C7 14                     add r15, 0x14
0089E3B5  E9 D7 FD FF FF                  jmp 0x14089e191
0089E3BA  66 41 03 C8                     add cx, r8w
0089E3BE  66 89 4C 24 50                  mov word ptr [rsp + 0x50], cx
0089E3C3  0F 85 03 FB FF FF               jne 0x14089decc
0089E3C9  E9 24 FB FF FF                  jmp 0x14089def2
0089E3CE  8B 9D 30 01 00 00               mov ebx, dword ptr [rbp + 0x130]
0089E3D4  83 FB 40                        cmp ebx, 0x40
0089E3D7  0F 83 E1 00 00 00               jae 0x14089e4be
0089E3DD  41 8B 46 64                     mov eax, dword ptr [r14 + 0x64]
0089E3E1  A8 04                           test al, 4
0089E3E3  0F 85 A1 00 00 00               jne 0x14089e48a
0089E3E9  FF C3                           inc ebx
0089E3EB  89 9D 30 01 00 00               mov dword ptr [rbp + 0x130], ebx
0089E3F1  E9 59 FC FF FF                  jmp 0x14089e04f
0089E3F6  49 3B D0                        cmp rdx, r8
0089E3F9  75 2C                           jne 0x14089e427
0089E3FB  66 83 7C 24 50 00               cmp word ptr [rsp + 0x50], 0
0089E401  74 24                           je 0x14089e427
0089E403  0F B7 01                        movzx eax, word ptr [rcx]
0089E406  66 83 E8 41                     sub ax, 0x41
0089E40A  66 41 85 C1                     test r9w, ax
0089E40E  75 17                           jne 0x14089e427
0089E410  66 83 7C 24 50 02               cmp word ptr [rsp + 0x50], 2
0089E416  0F 86 1A FB FF FF               jbe 0x14089df36
0089E41C  66 83 79 02 5C                  cmp word ptr [rcx + 2], 0x5c
0089E421  0F 84 0F FB FF FF               je 0x14089df36
0089E427  BB 22 00 00 C0                  mov ebx, 0xc0000022
0089E42C  E9 BD FD FF FF                  jmp 0x14089e1ee
0089E431  BB 24 00 00 C0                  mov ebx, 0xc0000024
0089E436  E9 BC FD FF FF                  jmp 0x14089e1f7
0089E43B  E8 74 83 FD FF                  call 0x1408767b4
0089E440  4C 8B F8                        mov r15, rax
0089E443  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0089E448  4C 8B F0                        mov r14, rax
0089E44B  E9 AB FA FF FF                  jmp 0x14089defb
0089E450  41 8B 86 88 00 00 00            mov eax, dword ptr [r14 + 0x88]
0089E457  45 33 C9                        xor r9d, r9d
0089E45A  48 69 C8 B8 00 00 00            imul rcx, rax, 0xb8
0089E461  48 8D 05 A8 B4 56 00            lea rax, [rip + 0x56b4a8]
0089E468  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
0089E471  48 03 C8                        add rcx, rax
0089E474  45 33 C0                        xor r8d, r8d
0089E477  33 D2                           xor edx, edx
0089E479  E8 32 02 97 FF                  call 0x14020e6b0
0089E47E  41 81 26 FF FE FF FF            and dword ptr [r14], 0xfffffeff
0089E485  E9 C5 FB FF FF                  jmp 0x14089e04f
0089E48A  49 8B 96 80 00 00 00            mov rdx, qword ptr [r14 + 0x80]
0089E491  4C 8D 8D 08 01 00 00            lea r9, [rbp + 0x108]
0089E498  41 8B 4E 78                     mov ecx, dword ptr [r14 + 0x78]
0089E49C  E8 0B CF 0A 00                  call 0x14094b3ac
0089E4A1  41 83 66 64 FB                  and dword ptr [r14 + 0x64], 0xfffffffb
0089E4A6  41 C7 46 78 00 00 00 00         mov dword ptr [r14 + 0x78], 0
0089E4AE  49 C7 86 80 00 00 00 00 00 00 00  mov qword ptr [r14 + 0x80], 0
0089E4B9  E9 2B FF FF FF                  jmp 0x14089e3e9
0089E4BE  8B 7E 60                        mov edi, dword ptr [rsi + 0x60]
0089E4C1  BB 34 00 00 C0                  mov ebx, 0xc0000034
0089E4C6  41 23 7D 04                     and edi, dword ptr [r13 + 4]
0089E4CA  E9 0F FC FF FF                  jmp 0x14089e0de
0089E4CF  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
0089E4D6  41 89 07                        mov dword ptr [r15], eax
0089E4D9  0F BA E8 19                     bts eax, 0x19
0089E4DD  F7 D0                           not eax
0089E4DF  23 41 18                        and eax, dword ptr [rcx + 0x18]
0089E4E2  89 41 10                        mov dword ptr [rcx + 0x10], eax
0089E4E5  E9 B7 FC FF FF                  jmp 0x14089e1a1
0089E4EA  33 D2                           xor edx, edx
0089E4EC  49 8B CF                        mov rcx, r15
0089E4EF  E8 1C 84 FD FF                  call 0x140876910
0089E4F4  49 8B CF                        mov rcx, r15
0089E4F7  E8 84 78 BD FF                  call 0x140475d80
0089E4FC  E9 F6 FC FF FF                  jmp 0x14089e1f7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpParseKey(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4, unsigned int a5, __int64 a6, unsigned int a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m114;
    unsigned __int16 v_stack_m116;
    unsigned __int16 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m12C;
    unsigned __int64 v_stack_m134;
    unsigned __int64 v_stack_m144;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m154;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m16C;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int16 v_stack_m1A6;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned int v_stack_m1D8;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int8 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int16 v_stack_p50;
    unsigned __int16 v_stack_p52;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p78;
    unsigned __int8 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (440);
    result = 0;
    v_stack_m58 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m1A8 = v_xmm0;
    v_stack_m78 = v_xmm1;
    result = CmpInitializeThreadInfo(v_stack_m68, a2, a3, a4);
    v_rdi = 0;
    v_stack_p8 = 0;
    a2 = 0;
    v_stack_m188 = 0;
    v_stack_m180 = 0;
    v_stack_m1A8 = v_xmm2;
    result = memset(v_stack_m108, a2, 136, a4);
    result = 0;
    v_stack_m168 = 0;
    v_stack_m190 = v_stack_m198;
    *(unsigned __int64 *)(a11) = 0;
    v_stack_m198 = v_stack_m198;
    v_stack_m178 = v_xmm0;
    v_stack_p38 = 0;
    v_stack_p10 = 0;
    if (0 != (*(unsigned __int64 *)(v_rip + 7507001))) goto loc_0089E431;
    result = v_stack_m198;
    v_rsi = a1;
    if (a1 == (*(unsigned __int64 *)(v_rip + 7584959))) {
        a1 = *(unsigned __int64 *)(a10 + 8);
        result = CmpGetRegistryNamespaceRootForSilo(a1, a2, 136, a4);
        v_rsi = result;
    }
    if ((unsigned __int16)(v_stack_m1A8) == 0) goto loc_0089DEF2;
loc_0089DECC:
    result = ((unsigned __int16)(v_stack_m1A8)) >> (1);
    if ((*(unsigned __int16 *)(v_stack_m1A0 + result * 2 - 2)) == 92) goto loc_0089E3BA;
    if ((unsigned __int16)(v_stack_m1A8) == 0) goto loc_0089DEF2;
loc_0089DEE8:
    if ((*(unsigned __int16 *)(v_stack_m1A0)) == 92) goto loc_0089E25C;
loc_0089DEF2:
    if (a8 == 0) goto loc_0089E43B;
loc_0089DEFB:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 96))) & (*(unsigned int *)(a10 + 4)));
    *(unsigned int *)(a8 + 96) = (unsigned int)(v_rdi);
    if ((*(unsigned __int64 *)(v_rsi + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7584853) + 8))) goto loc_0089E21A;
loc_0089DF29:
    if (((*(unsigned int *)(a8)) & (0x800ULL)) != 0) goto loc_0089E3F6;
loc_0089DF36:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsi + 48)))) & (16)) != 0) goto loc_0089E285;
loc_0089DF41:
    if ((*(unsigned int *)(v_rip + 6626351)) == 0) goto loc_0089E048;
    result = CmpIsRegistryLockAcquired(v_stack_m1A0, *(unsigned __int64 *)(v_rsi + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7584853) + 8), (unsigned int)(0xFFDFULL));
    if ((unsigned int)(result) != 0) goto loc_0089E048;
    v_stack_mA0 = 1;
    v_stack_m90 = (unsigned int)((unsigned int)(*(unsigned int *)(a8 + 28)));
    v_stack_m8C = (unsigned int)((unsigned int)(a5));
    v_stack_m98 = v_stack_m1A8;
    v_stack_m88 = (unsigned __int8)(v_stack_p20);
    v_stack_mF0 = (unsigned int)((unsigned int)(*(unsigned int *)(a8 + 24)));
    v_stack_m108 = a6;
    v_stack_mF8 = *(unsigned __int64 *)(v_rip + 7506685);
    v_stack_mD0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18 + 16)));
    v_stack_m100 = v_rsi;
    v_stack_mC0 = a11;
    result = *(unsigned __int64 *)(a8 + 72);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a8 + 72))) & (1)) != 0) { result = 0; }
    v_stack_mA8 = result;
    v_stack_m178 = v_stack_m108;
    v_stack_m170 = (unsigned int)((unsigned int)(*(unsigned int *)(a8 + 96)));
    v_stack_m168 = a8 + 144;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a8))))) != 0) goto loc_0089E2D3;
    v_stack_m1C8 = v_stack_m198;
    v_stack_m1D0 = v_rsi;
    v_stack_m1D8 = 29;
loc_0089E023:
    result = CmpCallCallBacksEx(0 + 28, v_stack_m108, v_stack_m178, 1);
    if (sign_flag) goto loc_0089E28F;
    *(unsigned int *)(a8 + 96) = (unsigned int)((unsigned int)(v_stack_m170));
    v_stack_p8 = 1;
loc_0089E048:
loc_0089E04F:
    v_stack_m1B8 = v_stack_m188;
    v_stack_m1C0 = a9;
    v_stack_m1C8 = a8;
    v_stack_m1D0 = v_stack_m78;
    v_stack_m1D8 = a6;
    v_stack_m78 = v_xmm0;
    result = CmpDoParseKey(v_stack_m100, v_stack_p18, v_stack_p20, (unsigned int)(a5));
    if (((unsigned int)(result)) == 259) goto loc_0089E450;
    if (((unsigned int)(result)) == 0xC000022DULL) goto loc_0089E3CE;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m100 + 96))) & (*(unsigned int *)(a10 + 4)));
    if (!(sign_flag)) {
        result = v_stack_m188;
        *(unsigned __int64 *)(a11) = result;
        v_stack_m188 = 0;
    }
    if (v_stack_p8 == 0) goto loc_0089E1BB;
    v_stack_mCC = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18 + 20)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a8)))) & (1)) != 0) goto loc_0089E32F;
    if ((*(unsigned int *)(v_rip + 6625909)) == 0) goto loc_0089E191;
    result = CmpIsRegistryLockAcquired(v_stack_m100, v_stack_p18, v_stack_p20, (unsigned int)(a5));
    if ((unsigned int)(result) != 0) goto loc_0089E191;
    result = v_stack_m198;
    v_rbx = (unsigned int)((unsigned int)(result));
    if (v_stack_m198 != v_stack_m198) {
        result = 0;
        v_stack_m160 = *(unsigned __int64 *)(a11);
        v_stack_m154 = 0;
        a3 = v_stack_m128;
        v_stack_m134 = 0;
        a2 = v_stack_m160;
        v_stack_m12C = 0;
        a4 = 0;
        result = v_stack_m108;
        v_stack_m158 = (unsigned int)((unsigned int)((unsigned int)(result)));
        v_stack_m150 = result;
        result = v_stack_m160;
        v_stack_m148 = (unsigned int)((unsigned int)((unsigned int)(result)));
        v_stack_m128 = result;
        a1 = a4 + 29;
        result = v_stack_m178;
        v_stack_m120 = result;
        result = v_stack_m198;
        v_stack_m1C8 = result;
        v_stack_m1D0 = *(unsigned __int64 *)(a11);
        v_stack_m1D8 = 29;
        v_stack_m144 = v_xmm0;
        result = CmpCallCallBacksEx(a1, a2, a3, a4);
        v_rbx = v_stack_m148;
    }
    if (sign_flag) goto loc_0089E1A1;
    if (((unsigned int)((unsigned int)(v_stack_mCC))) != (*(unsigned int *)(v_stack_p18 + 20))) goto loc_0089E4CF;
loc_0089E1A1:
    result = (unsigned int)(v_stack_mCC);
    if (*(unsigned __int64 *)(a11) != 0) {
        result = v_stack_m170;
        *(unsigned int *)(*(unsigned __int64 *)(a11) + 96) = (unsigned int)(result);
    }
    if (((unsigned int)(v_rbx)) != 872) goto loc_0089E1CB;
loc_0089E1C3:
    result = 0;
    *(unsigned __int64 *)(a8 + 64) = 0;
    goto loc_0089E1DC;
loc_0089E1CB:
    if (((unsigned int)(v_rbx)) != 260) goto loc_0089E1E0;
    *(unsigned int *)(a8 + 96) = (unsigned int)(v_rdi);
    result = PsGetCurrentSilo(*(unsigned __int64 *)(a11), a2, a3, a4);
loc_0089E1DC:
    *(unsigned __int64 *)(a10 + 8) = result;
loc_0089E1E0:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
loc_0089E1EE:
    if (v_stack_m180 != 0) goto loc_0089E4EA;
loc_0089E1F7:
    result = CmCleanupThreadInfo(v_stack_m68, a2, a3, a4);
    v_rsp = (v_rsp) + (440);
    return (unsigned int)((unsigned int)(v_rbx));
loc_0089E21A:
    if (v_stack_p50 == 0) goto loc_0089DF29;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m68)) - (65));
    if (((0) & ((unsigned __int16)(result))) != 0) goto loc_0089DF29;
    if (v_stack_p50 <= 2) goto loc_0089E24A;
    if ((*(unsigned __int16 *)(v_stack_m68 + 2)) != 92) goto loc_0089DF29;
loc_0089E24A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a8)))) & (64)) != 0) goto loc_0089DF29;
    goto loc_0089E1EE;
loc_0089E25C:
    a2 = (a2) + (2);
    a1 = (unsigned __int16)((v_stack_m68) + ((unsigned __int16)(a3)));
    result = (unsigned __int16)(((unsigned int)(*(unsigned int *)(a8))) + ((unsigned __int16)(a3)));
    v_stack_p58 = a2;
    v_stack_p50 = (unsigned __int16)(a1);
    v_stack_p52 = (unsigned __int16)(result);
    if ((unsigned __int16)(a1) != 0) goto loc_0089DEE8;
    goto loc_0089DEF2;
loc_0089E285:
    goto loc_0089DF41;
loc_0089E28F:
    if (((unsigned int)((unsigned int)(0xC0000022ULL))) != 0xC0000503ULL) goto loc_0089E1E0;
    if (((unsigned int)((unsigned int)(v_stack_m16C))) == 872) goto loc_0089E1C3;
    if (((unsigned int)((unsigned int)(v_stack_m16C))) == 260) goto loc_0089E1BB;
    result = (unsigned int)(~((unsigned int)(v_stack_mCC)));
    v_rbx = 0;
    goto loc_0089E1E0;
loc_0089E2D3:
    v_stack_m118 = (unsigned __int16)(*(unsigned __int16 *)(a8 + 4));
    v_stack_m116 = (unsigned __int16)(*(unsigned __int16 *)(a8 + 4));
    v_stack_m110 = *(unsigned __int64 *)(a8 + 8);
    v_stack_mC8 = a8 + 32;
    v_stack_mE8 = v_stack_m118;
    v_stack_mE0 = *(unsigned __int64 *)(v_stack_p18 + 64);
    v_stack_mD8 = a9;
    v_stack_p30 = v_stack_p60;
    v_stack_p28 = v_stack_p18 + 20;
    v_stack_p20 = 27;
    v_stack_m114 = (unsigned int)(a2);
    goto loc_0089E023;
loc_0089E32F:
    if ((*(unsigned int *)(v_rip + 6625362)) == 0) goto loc_0089E3B1;
    result = CmpIsRegistryLockAcquired(26, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0089E3B1;
    result = v_stack_p60;
    if (v_stack_p60 != v_stack_p60) {
        result = 0;
        v_stack_m160 = *(unsigned __int64 *)(a11);
        v_stack_m154 = 0;
        a3 = v_stack_m128;
        v_stack_m134 = 0;
        a2 = v_stack_m160;
        v_stack_m12C = 0;
        a4 = 0;
        result = v_stack_m108;
        v_stack_m158 = 0;
        v_stack_m150 = result;
        result = v_stack_m160;
        v_stack_m148 = 0;
        v_stack_m128 = result;
        a1 = a4 + 27;
        result = v_stack_m178;
        v_stack_m120 = result;
        result = v_stack_p60;
        v_stack_p30 = result;
        v_stack_p28 = *(unsigned __int64 *)(a11);
        v_stack_p20 = 27;
        v_stack_m144 = v_xmm0;
        result = CmpCallCallBacksEx(a1, a2, a3, a4);
        v_rbx = v_stack_m148;
    }
    v_r15 = (v_stack_m180) + (20);
    goto loc_0089E191;
loc_0089E3BA:
    a1 = (unsigned __int16)((a1) + ((unsigned __int16)(a3)));
    v_stack_p50 = (unsigned __int16)(a1);
    if (condition_is_not_equal) goto loc_0089DECC;
    goto loc_0089DEF2;
loc_0089E3CE:
    if (((unsigned int)((unsigned int)(a7))) >= 64) goto loc_0089E4BE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a8 + 100)))) & (4)) != 0) goto loc_0089E48A;
loc_0089E3E9:
    v_rbx = (unsigned int)(((unsigned int)(a7)) + 1);
    v_stack_p38 = (unsigned int)(v_rbx);
    goto loc_0089E04F;
loc_0089E3F6:
    if (a2 != a3) goto loc_0089E427;
    if (v_stack_p50 == 0) goto loc_0089E427;
    result = (unsigned __int16)((*(unsigned __int16 *)(a1)) - (65));
    if (((0) & ((unsigned __int16)(result))) != 0) goto loc_0089E427;
    if (v_stack_p50 <= 2) goto loc_0089DF36;
    if ((*(unsigned __int16 *)(a1 + 2)) == 92) goto loc_0089DF36;
loc_0089E427:
    goto loc_0089E1EE;
loc_0089E431:
    goto loc_0089E1F7;
loc_0089E43B:
    result = CmpAllocateParseContext(a1, a2, a3, a4);
    v_stack_p78 = result;
    goto loc_0089DEFB;
loc_0089E450:
    a4 = 0;
    a1 = (a1) * ((unsigned int)(*(unsigned int *)(result + 136)));
    v_stack_p20 = 0;
    a1 = (a1) + (v_rip + 5682344);
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(a1, a2, a3, a4);
    goto loc_0089E04F;
loc_0089E48A:
    result = CmpRollbackTransactionArray((unsigned int)(*(unsigned int *)(result + 120)), *(unsigned __int64 *)(result + 128), a3, v_stack_p10);
    *(unsigned int *)(result + 120) = 0;
    *(unsigned __int64 *)(result + 128) = 0;
    goto loc_0089E3E9;
loc_0089E4BE:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p18 + 20 + 96))) & (*(unsigned int *)(a10 + 4)));
    goto loc_0089E0DE;
loc_0089E4CF:
    *(unsigned int *)(result) = (unsigned int)(result);
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (*(unsigned int *)(v_stack_p18 + 24)));
    *(unsigned int *)(v_stack_p18 + 16) = (unsigned int)(result);
    goto loc_0089E1A1;
loc_0089E4EA:
    a2 = 0;
    result = CmpCleanupParseContext(result, a2, a3, v_stack_p10);
    result = CmSiFreeMemory(result, a2, a3, v_stack_p10);
    goto loc_0089E1F7;
}
```

## 5. (Beta) C Style

```c
int64_t CmpParseKey(int64_t Arg1, int64_t Arg2, int64_t Arg3, uint8_t Arg4, uint32_t Arg5, int64_t Arg6, void *Arg7, int64_t Arg8, int64_t Arg9, void *Arg10, void *Arg11)
{
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg10 = (uint8_t *)Arg10;
    uint8_t *arg11 = (uint8_t *)Arg11;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m114;
    uint16_t v_stack_m116;
    uint16_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m12C;
    uint64_t v_stack_m134;
    uint64_t v_stack_m144;
    uint32_t v_stack_m148;
    uint64_t v_stack_m150;
    uint32_t v_stack_m154;
    uint32_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m16C;
    uint32_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint16_t v_stack_m1A6;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint32_t v_stack_m1D8;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint8_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint16_t v_stack_p50;
    uint16_t v_stack_p52;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p78;
    uint8_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (440);
    result = 0;
    v_stack_m58 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m1A8 = v_xmm0;
    v_stack_m78 = v_xmm1;
    result = CmpInitializeThreadInfo(v_stack_m68, Arg2, Arg3, Arg4);
    local_rdi = 0;
    v_stack_p8 = 0;
    Arg2 = 0;
    v_stack_m188 = 0;
    v_stack_m180 = 0;
    v_stack_m1A8 = v_xmm2;
    result = memset(v_stack_m108, Arg2, 136, Arg4);
    result = 0;
    v_stack_m168 = 0;
    v_stack_m190 = v_stack_m198;
    *(uint64_t *)(arg11) = 0;
    v_stack_m198 = v_stack_m198;
    v_stack_m178 = v_xmm0;
    v_stack_p38 = 0;
    v_stack_p10 = 0;
    if (0 != (*(uint64_t *)(v_rip + 0x728C39))) goto loc_0089E431;
    result = v_stack_m198;
    local_rsi = Arg1;
    if (Arg1 == (*(uint64_t *)(v_rip + 0x73BCBF))) {
        Arg1 = *(uint64_t *)(arg10 + 0x8);
        result = CmpGetRegistryNamespaceRootForSilo(Arg1, Arg2, 136, Arg4);
        local_rsi = result;
    }
    if ((uint16_t)(v_stack_m1A8) == 0) goto loc_0089DEF2;
loc_0089DECC:
    result = ((uint16_t)(v_stack_m1A8)) >> (1);
    if ((*(uint16_t *)(v_stack_m1A0 + result * 2 - 0x2)) == 92) goto loc_0089E3BA;
    if ((uint16_t)(v_stack_m1A8) == 0) goto loc_0089DEF2;
loc_0089DEE8:
    if ((*(uint16_t *)(v_stack_m1A0)) == 92) goto loc_0089E25C;
loc_0089DEF2:
    if (Arg8 == 0) goto loc_0089E43B;
loc_0089DEFB:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x60))) & (*(uint32_t *)(arg10 + 0x4)));
    *(uint32_t *)(Arg8 + 0x60) = (uint32_t)(local_rdi);
    if ((*(uint64_t *)(local_rsi + 0x8)) == (*(uint64_t *)(*(uint64_t *)(v_rip + 0x73BC55) + 0x8))) goto loc_0089E21A;
loc_0089DF29:
    if (((*(uint32_t *)(Arg8)) & (0x800ULL)) != 0) goto loc_0089E3F6;
loc_0089DF36:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x30)))) & (16)) != 0) goto loc_0089E285;
loc_0089DF41:
    if ((*(uint32_t *)(v_rip + 0x651C2F)) == 0) goto loc_0089E048;
    result = CmpIsRegistryLockAcquired(v_stack_m1A0, *(uint64_t *)(local_rsi + 0x8), *(uint64_t *)(*(uint64_t *)(v_rip + 0x73BC55) + 0x8), (uint32_t)(0xFFDFULL));
    if ((uint32_t)(result) != 0) goto loc_0089E048;
    v_stack_mA0 = 1;
    v_stack_m90 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x1C)));
    v_stack_m8C = (uint32_t)((uint32_t)(Arg5));
    v_stack_m98 = v_stack_m1A8;
    v_stack_m88 = (uint8_t)(v_stack_p20);
    v_stack_mF0 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x18)));
    v_stack_m108 = Arg6;
    v_stack_mF8 = *(uint64_t *)(v_rip + 0x728AFD);
    v_stack_mD0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x10)));
    v_stack_m100 = local_rsi;
    v_stack_mC0 = Arg11;
    result = *(uint64_t *)(Arg8 + 0x48);
    if ((((uint8_t)(*(uint64_t *)(Arg8 + 0x48))) & (1)) != 0) { result = 0; }
    v_stack_mA8 = result;
    v_stack_m178 = v_stack_m108;
    v_stack_m170 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x60)));
    v_stack_m168 = Arg8 + 144;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(Arg8))))) != 0) goto loc_0089E2D3;
    v_stack_m1C8 = v_stack_m198;
    v_stack_m1D0 = local_rsi;
    v_stack_m1D8 = 29;
loc_0089E023:
    result = CmpCallCallBacksEx(0 + 28, v_stack_m108, v_stack_m178, 1);
    if (sign_flag) goto loc_0089E28F;
    *(uint32_t *)(Arg8 + 0x60) = (uint32_t)((uint32_t)(v_stack_m170));
    v_stack_p8 = 1;
loc_0089E048:
loc_0089E04F:
    v_stack_m1B8 = v_stack_m188;
    v_stack_m1C0 = Arg9;
    v_stack_m1C8 = Arg8;
    v_stack_m1D0 = v_stack_m78;
    v_stack_m1D8 = Arg6;
    v_stack_m78 = v_xmm0;
    result = CmpDoParseKey(v_stack_m100, v_stack_p18, v_stack_p20, (uint32_t)(Arg5));
    if (((uint32_t)(result)) == 259) goto loc_0089E450;
    if (((uint32_t)(result)) == 0xC000022DULL) goto loc_0089E3CE;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m100 + 0x60))) & (*(uint32_t *)(arg10 + 0x4)));
    if (!(sign_flag)) {
        result = v_stack_m188;
        *(uint64_t *)(arg11) = result;
        v_stack_m188 = 0;
    }
    if (v_stack_p8 == 0) goto loc_0089E1BB;
    v_stack_mCC = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x14)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg8)))) & (1)) != 0) goto loc_0089E32F;
    if ((*(uint32_t *)(v_rip + 0x651A75)) == 0) goto loc_0089E191;
    result = CmpIsRegistryLockAcquired(v_stack_m100, v_stack_p18, v_stack_p20, (uint32_t)(Arg5));
    if ((uint32_t)(result) != 0) goto loc_0089E191;
    result = v_stack_m198;
    local_rbx = (uint32_t)((uint32_t)(result));
    if (v_stack_m198 != v_stack_m198) {
        result = 0;
        v_stack_m160 = *(uint64_t *)(arg11);
        v_stack_m154 = 0;
        Arg3 = v_stack_m128;
        v_stack_m134 = 0;
        Arg2 = v_stack_m160;
        v_stack_m12C = 0;
        Arg4 = 0;
        result = v_stack_m108;
        v_stack_m158 = (uint32_t)((uint32_t)((uint32_t)(result)));
        v_stack_m150 = result;
        result = v_stack_m160;
        v_stack_m148 = (uint32_t)((uint32_t)((uint32_t)(result)));
        v_stack_m128 = result;
        Arg1 = Arg4 + 29;
        result = v_stack_m178;
        v_stack_m120 = result;
        result = v_stack_m198;
        v_stack_m1C8 = result;
        v_stack_m1D0 = *(uint64_t *)(arg11);
        v_stack_m1D8 = 29;
        v_stack_m144 = v_xmm0;
        result = CmpCallCallBacksEx(Arg1, Arg2, Arg3, Arg4);
        local_rbx = v_stack_m148;
    }
    if (sign_flag) goto loc_0089E1A1;
    if (((uint32_t)((uint32_t)(v_stack_mCC))) != (*(uint32_t *)(v_stack_p18 + 0x14))) goto loc_0089E4CF;
loc_0089E1A1:
    result = (uint32_t)(v_stack_mCC);
    if (*(uint64_t *)(arg11) != 0) {
        result = v_stack_m170;
        *(uint32_t *)(*(uint64_t *)(arg11) + 0x60) = (uint32_t)(result);
    }
    if (((uint32_t)(local_rbx)) != 872) goto loc_0089E1CB;
loc_0089E1C3:
    result = 0;
    *(uint64_t *)(Arg8 + 0x40) = 0;
    goto loc_0089E1DC;
loc_0089E1CB:
    if (((uint32_t)(local_rbx)) != 260) goto loc_0089E1E0;
    *(uint32_t *)(Arg8 + 0x60) = (uint32_t)(local_rdi);
    result = PsGetCurrentSilo(*(uint64_t *)(arg11), Arg2, Arg3, Arg4);
loc_0089E1DC:
    *(uint64_t *)(arg10 + 0x8) = result;
loc_0089E1E0:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
loc_0089E1EE:
    if (v_stack_m180 != 0) goto loc_0089E4EA;
loc_0089E1F7:
    result = CmCleanupThreadInfo(v_stack_m68, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (440);
    return (uint32_t)((uint32_t)(local_rbx));
loc_0089E21A:
    if (v_stack_p50 == 0) goto loc_0089DF29;
    result = (uint16_t)((*(uint16_t *)(v_stack_m68)) - (65));
    if (((0) & ((uint16_t)(result))) != 0) goto loc_0089DF29;
    if (v_stack_p50 <= 2) goto loc_0089E24A;
    if ((*(uint16_t *)(v_stack_m68 + 0x2)) != 92) goto loc_0089DF29;
loc_0089E24A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg8)))) & (64)) != 0) goto loc_0089DF29;
    goto loc_0089E1EE;
loc_0089E25C:
    Arg2 = (Arg2) + (2);
    Arg1 = (uint16_t)((v_stack_m68) + ((uint16_t)(Arg3)));
    result = (uint16_t)(((uint32_t)(*(uint32_t *)(Arg8))) + ((uint16_t)(Arg3)));
    v_stack_p58 = Arg2;
    v_stack_p50 = (uint16_t)(Arg1);
    v_stack_p52 = (uint16_t)(result);
    if ((uint16_t)(Arg1) != 0) goto loc_0089DEE8;
    goto loc_0089DEF2;
loc_0089E285:
    goto loc_0089DF41;
loc_0089E28F:
    if (((uint32_t)((uint32_t)(0xC0000022ULL))) != 0xC0000503ULL) goto loc_0089E1E0;
    if (((uint32_t)((uint32_t)(v_stack_m16C))) == 872) goto loc_0089E1C3;
    if (((uint32_t)((uint32_t)(v_stack_m16C))) == 260) goto loc_0089E1BB;
    result = (uint32_t)(~((uint32_t)(v_stack_mCC)));
    local_rbx = 0;
    goto loc_0089E1E0;
loc_0089E2D3:
    v_stack_m118 = (uint16_t)(*(uint16_t *)(Arg8 + 0x4));
    v_stack_m116 = (uint16_t)(*(uint16_t *)(Arg8 + 0x4));
    v_stack_m110 = *(uint64_t *)(Arg8 + 0x8);
    v_stack_mC8 = Arg8 + 32;
    v_stack_mE8 = v_stack_m118;
    v_stack_mE0 = *(uint64_t *)(v_stack_p18 + 0x40);
    v_stack_mD8 = Arg9;
    v_stack_p30 = v_stack_p60;
    v_stack_p28 = v_stack_p18 + 20;
    v_stack_p20 = 27;
    v_stack_m114 = (uint32_t)(Arg2);
    goto loc_0089E023;
loc_0089E32F:
    if ((*(uint32_t *)(v_rip + 0x651852)) == 0) goto loc_0089E3B1;
    result = CmpIsRegistryLockAcquired(26, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_0089E3B1;
    result = v_stack_p60;
    if (v_stack_p60 != v_stack_p60) {
        result = 0;
        v_stack_m160 = *(uint64_t *)(arg11);
        v_stack_m154 = 0;
        Arg3 = v_stack_m128;
        v_stack_m134 = 0;
        Arg2 = v_stack_m160;
        v_stack_m12C = 0;
        Arg4 = 0;
        result = v_stack_m108;
        v_stack_m158 = 0;
        v_stack_m150 = result;
        result = v_stack_m160;
        v_stack_m148 = 0;
        v_stack_m128 = result;
        Arg1 = Arg4 + 27;
        result = v_stack_m178;
        v_stack_m120 = result;
        result = v_stack_p60;
        v_stack_p30 = result;
        v_stack_p28 = *(uint64_t *)(arg11);
        v_stack_p20 = 27;
        v_stack_m144 = v_xmm0;
        result = CmpCallCallBacksEx(Arg1, Arg2, Arg3, Arg4);
        local_rbx = v_stack_m148;
    }
    local_r15 = (v_stack_m180) + (20);
    goto loc_0089E191;
loc_0089E3BA:
    Arg1 = (uint16_t)((Arg1) + ((uint16_t)(Arg3)));
    v_stack_p50 = (uint16_t)(Arg1);
    if (condition_is_not_equal) goto loc_0089DECC;
    goto loc_0089DEF2;
loc_0089E3CE:
    if (((uint32_t)((uint32_t)(Arg7))) >= 64) goto loc_0089E4BE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg8 + 0x64)))) & (4)) != 0) goto loc_0089E48A;
loc_0089E3E9:
    local_rbx = (uint32_t)(((uint32_t)(Arg7)) + 1);
    v_stack_p38 = (uint32_t)(local_rbx);
    goto loc_0089E04F;
loc_0089E3F6:
    if (Arg2 != Arg3) goto loc_0089E427;
    if (v_stack_p50 == 0) goto loc_0089E427;
    result = (uint16_t)((*(uint16_t *)(Arg1)) - (65));
    if (((0) & ((uint16_t)(result))) != 0) goto loc_0089E427;
    if (v_stack_p50 <= 2) goto loc_0089DF36;
    if ((*(uint16_t *)(Arg1 + 0x2)) == 92) goto loc_0089DF36;
loc_0089E427:
    goto loc_0089E1EE;
loc_0089E431:
    goto loc_0089E1F7;
loc_0089E43B:
    result = CmpAllocateParseContext(Arg1, Arg2, Arg3, Arg4);
    v_stack_p78 = result;
    goto loc_0089DEFB;
loc_0089E450:
    Arg4 = 0;
    Arg1 = (Arg1) * ((uint32_t)(*(uint32_t *)(result + 0x88)));
    v_stack_p20 = 0;
    Arg1 = (Arg1) + (v_rip + 5682344);
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(Arg1, Arg2, Arg3, Arg4);
    goto loc_0089E04F;
loc_0089E48A:
    result = CmpRollbackTransactionArray((uint32_t)(*(uint32_t *)(result + 0x78)), *(uint64_t *)(result + 0x80), Arg3, v_stack_p10);
    *(uint32_t *)(result + 0x78) = 0;
    *(uint64_t *)(result + 0x80) = 0;
    goto loc_0089E3E9;
loc_0089E4BE:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x14 + 0x60))) & (*(uint32_t *)(arg10 + 0x4)));
    goto loc_0089E0DE;
loc_0089E4CF:
    *(uint32_t *)(result) = (uint32_t)(result);
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (*(uint32_t *)(v_stack_p18 + 0x18)));
    *(uint32_t *)(v_stack_p18 + 0x10) = (uint32_t)(result);
    goto loc_0089E1A1;
loc_0089E4EA:
    Arg2 = 0;
    result = CmpCleanupParseContext(result, Arg2, Arg3, v_stack_p10);
    result = CmSiFreeMemory(result, Arg2, Arg3, v_stack_p10);
    goto loc_0089E1F7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg7` | `+ 0x0` | `128` | `R` |
| `Arg10` | `+ 0x4` | `32` | `R` |
| `Arg10` | `+ 0x8` | `64` | `R` |
| `Arg10` | `+ 0x8` | `64` | `W` |
| `Arg11` | `+ 0x0` | `64` | `R` |
| `Arg11` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0089DDC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
