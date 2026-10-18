# ExpSystemErrorHandler2

- RVA: `0x00B72C30`–`0x00B732DE` (길이 `1,710` bytes)
- VA: `0x0000000140B72C30`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D55C0`
- 디코드: `377`개 명령, `1,710/1,710` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x00B72CAC` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00B72D01` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B72D37` → [strcat_s](../../text/50/strcat_s_function_00505F20.md) (function, `0x00505F20`)
- `0x00B72D4C` → [RtlUnicodeStringToAnsiString](../../page/90/RtlUnicodeStringToAnsiString_function_0090D1F0.md) (function, `0x0090D1F0`)
- `0x00B72DB6` → [strcat_s](../../text/50/strcat_s_function_00505F20.md) (function, `0x00505F20`)
- `0x00B72DD6` → [strcat_s](../../text/50/strcat_s_function_00505F20.md) (function, `0x00505F20`)
- `0x00B72DF9` → [PsQuerySystemDllInfo](../../page/8D/PsQuerySystemDllInfo_function_008D20F8.md) (function, `0x008D20F8`)
- `0x00B72E4D` → [RtlFindMessage](../../page/99/RtlFindMessage_function_0099B220.md) (function, `0x0099B220`)
- `0x00B72E86` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00B72E90` → [RtlxUnicodeStringToAnsiSize](../../page/90/RtlxUnicodeStringToAnsiSize_function_0090CE80.md) (function, `0x0090CE80`)
- `0x00B72EB0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B72EE2` → [RtlUnicodeStringToAnsiString](../../page/90/RtlUnicodeStringToAnsiString_function_0090D1F0.md) (function, `0x0090D1F0`)
- `0x00B72EF0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B72F39` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B72F54` → [strcpy_s](../../text/50/strcpy_s_function_00505FB0.md) (function, `0x00505FB0`)
- `0x00B73030` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (function, `0x0053BC0C`)
- `0x00B73073` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (function, `0x0053BC0C`)
- `0x00B7307F` → [MmLockPagableSectionByHandle](../../page/A4/MmLockPagableSectionByHandle_function_00A4D1E0.md) (function, `0x00A4D1E0`)
- `0x00B730A4` → [RtlInitAnsiString](../../text/47/RtlInitAnsiString_function_00470F40.md) (function, `0x00470F40`)
- `0x00B730B9` → [RtlAnsiStringToUnicodeString](../../page/90/RtlAnsiStringToUnicodeString_function_0090BEA0.md) (function, `0x0090BEA0`)
- `0x00B730C7` → [RtlxUnicodeStringToAnsiSize](../../page/90/RtlxUnicodeStringToAnsiSize_function_0090CE80.md) (function, `0x0090CE80`)
- `0x00B730EA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B73114` → [RtlUnicodeStringToOemString](../../page/AC/RtlUnicodeStringToOemString_function_00AC1C10.md) (function, `0x00AC1C10`)
- `0x00B7315C` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (function, `0x0053BC0C`)
- `0x00B731D4` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (function, `0x0053BC0C`)
- `0x00B731E9` → [RtlInitAnsiString](../../text/47/RtlInitAnsiString_function_00470F40.md) (function, `0x00470F40`)
- `0x00B731FE` → [RtlAnsiStringToUnicodeString](../../page/90/RtlAnsiStringToUnicodeString_function_0090BEA0.md) (function, `0x0090BEA0`)
- `0x00B7320C` → [RtlxUnicodeStringToAnsiSize](../../page/90/RtlxUnicodeStringToAnsiSize_function_0090CE80.md) (function, `0x0090CE80`)
- `0x00B7322F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B73254` → [RtlUnicodeStringToOemString](../../page/AC/RtlUnicodeStringToOemString_function_00AC1C10.md) (function, `0x00AC1C10`)
- `0x00B73259` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (function, `0x00225710`)
- `0x00B73269` → [PsTerminateServerSilo](../../page/77/PsTerminateServerSilo_function_0077F620.md) (function, `0x0077F620`)
- `0x00B73279` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00B732BD` → [PoShutdownBugCheck](../../page/75/PoShutdownBugCheck_function_0075E580.md) (function, `0x0075E580`)
- `0x00B732D8` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [ExpSystemErrorHandler](../../text/4F/ExpSystemErrorHandler_function_004FEDF0.md) at `0x004FEEC3`

### Static image references
- `0x00B72C45` → RVA `0x00E0A740` (`.data`; read)
- `0x00B72D23` → RVA `0x00B802B0` (` ?? ::OKHAJAOM::`string'`; read)
- `0x00B72D86` → RVA `0x00B80280` (` ?? ::OKHAJAOM::`string'`; read)
- `0x00B72DA2` → RVA `0x00B80270` (` ?? ::OKHAJAOM::`string'`; read)
- `0x00B72DC2` → RVA `0x00B802A0` (` ?? ::OKHAJAOM::`string'`; read)
- `0x00B72DE8` → RVA `0x00B802C0` (` ?? ::OKHAJAOM::`string'`; read)
- `0x00B72E1B` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x00B72FDA` → RVA `0x00B80290` (` ?? ::OKHAJAOM::`string'`; read)
- `0x00B7301A` → RVA `0x00B80220` (` ?? ::OKHAJAOM::`string'`; read)
- `0x00B73061` → RVA `0x00B80210` (` ?? ::OKHAJAOM::`string'`; read)
- `0x00B73078` → RVA `0x00FC6C00` (`ALMOSTRO`; read)
- `0x00B731C2` → RVA `0x00B80230` (` ?? ::OKHAJAOM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **35**
  - `0x00B72CAC` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGELK` → `.text`)
  - `0x00B72D01` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGELK` → `.text`)
  - `0x00B72D37` → [strcat_s](../../text/50/strcat_s_function_00505F20.md) (`PAGELK` → `.text`)
  - `0x00B72D4C` → [RtlUnicodeStringToAnsiString](../../page/90/RtlUnicodeStringToAnsiString_function_0090D1F0.md) (`PAGELK` → `PAGE`)
  - `0x00B72DB6` → [strcat_s](../../text/50/strcat_s_function_00505F20.md) (`PAGELK` → `.text`)
  - `0x00B72DD6` → [strcat_s](../../text/50/strcat_s_function_00505F20.md) (`PAGELK` → `.text`)
  - `0x00B72DF9` → [PsQuerySystemDllInfo](../../page/8D/PsQuerySystemDllInfo_function_008D20F8.md) (`PAGELK` → `PAGE`)
  - `0x00B72E4D` → [RtlFindMessage](../../page/99/RtlFindMessage_function_0099B220.md) (`PAGELK` → `PAGE`)
  - `0x00B72E86` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGELK` → `.text`)
  - `0x00B72E90` → [RtlxUnicodeStringToAnsiSize](../../page/90/RtlxUnicodeStringToAnsiSize_function_0090CE80.md) (`PAGELK` → `PAGE`)
  - `0x00B72EB0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGELK` → `POOLCODE`)
  - `0x00B72EE2` → [RtlUnicodeStringToAnsiString](../../page/90/RtlUnicodeStringToAnsiString_function_0090D1F0.md) (`PAGELK` → `PAGE`)
  - `0x00B72EF0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGELK` → `POOLCODE`)
  - `0x00B72F39` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGELK` → `POOLCODE`)
  - `0x00B72F54` → [strcpy_s](../../text/50/strcpy_s_function_00505FB0.md) (`PAGELK` → `.text`)
  - `0x00B73030` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (`PAGELK` → `.text`)
  - `0x00B73073` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (`PAGELK` → `.text`)
  - `0x00B7307F` → [MmLockPagableSectionByHandle](../../page/A4/MmLockPagableSectionByHandle_function_00A4D1E0.md) (`PAGELK` → `PAGE`)
  - `0x00B730A4` → [RtlInitAnsiString](../../text/47/RtlInitAnsiString_function_00470F40.md) (`PAGELK` → `.text`)
  - `0x00B730B9` → [RtlAnsiStringToUnicodeString](../../page/90/RtlAnsiStringToUnicodeString_function_0090BEA0.md) (`PAGELK` → `PAGE`)
  - `0x00B730C7` → [RtlxUnicodeStringToAnsiSize](../../page/90/RtlxUnicodeStringToAnsiSize_function_0090CE80.md) (`PAGELK` → `PAGE`)
  - `0x00B730EA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGELK` → `POOLCODE`)
  - `0x00B73114` → [RtlUnicodeStringToOemString](../../page/AC/RtlUnicodeStringToOemString_function_00AC1C10.md) (`PAGELK` → `PAGE`)
  - `0x00B7315C` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (`PAGELK` → `.text`)
  - `0x00B731D4` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (`PAGELK` → `.text`)
  - `0x00B731E9` → [RtlInitAnsiString](../../text/47/RtlInitAnsiString_function_00470F40.md) (`PAGELK` → `.text`)
  - `0x00B731FE` → [RtlAnsiStringToUnicodeString](../../page/90/RtlAnsiStringToUnicodeString_function_0090BEA0.md) (`PAGELK` → `PAGE`)
  - `0x00B7320C` → [RtlxUnicodeStringToAnsiSize](../../page/90/RtlxUnicodeStringToAnsiSize_function_0090CE80.md) (`PAGELK` → `PAGE`)
  - `0x00B7322F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGELK` → `POOLCODE`)
  - `0x00B73254` → [RtlUnicodeStringToOemString](../../page/AC/RtlUnicodeStringToOemString_function_00AC1C10.md) (`PAGELK` → `PAGE`)
  - `0x00B73259` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (`PAGELK` → `.text`)
  - `0x00B73269` → [PsTerminateServerSilo](../../page/77/PsTerminateServerSilo_function_0077F620.md) (`PAGELK` → `PAGE`)
  - `0x00B73279` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
  - `0x00B732BD` → [PoShutdownBugCheck](../../page/75/PoShutdownBugCheck_function_0075E580.md) (`PAGELK` → `PAGE`)
  - `0x00B732D8` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B72C30  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00B72C35  53                              push rbx
00B72C36  56                              push rsi
00B72C37  57                              push rdi
00B72C38  41 55                           push r13
00B72C3A  41 56                           push r14
00B72C3C  41 57                           push r15
00B72C3E  48 81 EC 38 02 00 00            sub rsp, 0x238
00B72C45  48 8B 05 F4 7A 29 00            mov rax, qword ptr [rip + 0x297af4]
00B72C4C  48 33 C4                        xor rax, rsp
00B72C4F  48 89 84 24 20 02 00 00         mov qword ptr [rsp + 0x220], rax
00B72C57  4D 8B E9                        mov r13, r9
00B72C5A  45 8B F0                        mov r14d, r8d
00B72C5D  44 8B F9                        mov r15d, ecx
00B72C60  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
00B72C64  89 8C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ecx
00B72C6B  4C 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r9
00B72C73  48 83 A4 24 C0 00 00 00 00      and qword ptr [rsp + 0xc0], 0
00B72C7C  48 83 A4 24 B8 00 00 00 00      and qword ptr [rsp + 0xb8], 0
00B72C85  48 83 64 24 60 00               and qword ptr [rsp + 0x60], 0
00B72C8B  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
00B72C91  0F 57 C0                        xorps xmm0, xmm0
00B72C94  0F 11 84 24 88 00 00 00         movups xmmword ptr [rsp + 0x88], xmm0
00B72C9C  0F 57 C9                        xorps xmm1, xmm1
00B72C9F  0F 11 4C 24 78                  movups xmmword ptr [rsp + 0x78], xmm1
00B72CA4  0F 11 84 24 98 00 00 00         movups xmmword ptr [rsp + 0x98], xmm0
00B72CAC  E8 3F B5 78 FF                  call 0x1402fe1f0
00B72CB1  0F B7 B8 14 04 00 00            movzx edi, word ptr [rax + 0x414]
00B72CB8  66 89 7C 24 68                  mov word ptr [rsp + 0x68], di
00B72CBD  B8 05 00 00 00                  mov eax, 5
00B72CC2  3B D0                           cmp edx, eax
00B72CC4  0F 46 C2                        cmovbe eax, edx
00B72CC7  8B F0                           mov esi, eax
00B72CC9  89 74 24 70                     mov dword ptr [rsp + 0x70], esi
00B72CCD  C6 84 24 F8 00 00 00 00         mov byte ptr [rsp + 0xf8], 0
00B72CD5  33 C0                           xor eax, eax
00B72CD7  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
00B72CDF  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
00B72CE7  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
00B72CEF  44 8B C6                        mov r8d, esi
00B72CF2  49 C1 E0 03                     shl r8, 3
00B72CF6  49 8B D1                        mov rdx, r9
00B72CF9  48 8D 8C 24 D0 00 00 00         lea rcx, [rsp + 0xd0]
00B72D01  E8 3A 3B B5 FF                  call 0x1406c6840
00B72D06  48 83 A4 24 C8 00 00 00 00      and qword ptr [rsp + 0xc8], 0
00B72D0F  33 DB                           xor ebx, ebx
00B72D11  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00B72D15  3B DE                           cmp ebx, esi
00B72D17  0F 83 A5 00 00 00               jae 0x140b72dc2
00B72D1D  41 0F A3 DE                     bt r14d, ebx
00B72D21  73 7F                           jae 0x140b72da2
00B72D23  4C 8D 05 86 D5 00 00            lea r8, [rip + 0xd586]
00B72D2A  BA 20 00 00 00                  mov edx, 0x20
00B72D2F  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
00B72D37  E8 E4 31 99 FF                  call 0x140505f20
00B72D3C  41 B0 01                        mov r8b, 1
00B72D3F  49 8B 54 DD 00                  mov rdx, qword ptr [r13 + rbx*8]
00B72D44  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
00B72D4C  E8 9F A4 D9 FF                  call 0x14090d1f0
00B72D51  8B D0                           mov edx, eax
00B72D53  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00B72D57  EB 2B                           jmp 0x140b72d84
00B72D59  BA 01 00 00 C0                  mov edx, 0xc0000001
00B72D5E  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00B72D62  44 8B B4 24 80 02 00 00         mov r14d, dword ptr [rsp + 0x280]
00B72D6A  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
00B72D6E  44 8B 7C 24 58                  mov r15d, dword ptr [rsp + 0x58]
00B72D73  4C 8B AC 24 B0 00 00 00         mov r13, qword ptr [rsp + 0xb0]
00B72D7B  0F B7 7C 24 68                  movzx edi, word ptr [rsp + 0x68]
00B72D80  8B 74 24 70                     mov esi, dword ptr [rsp + 0x70]
00B72D84  8B CB                           mov ecx, ebx
00B72D86  48 8D 05 F3 D4 00 00            lea rax, [rip + 0xd4f3]
00B72D8D  85 D2                           test edx, edx
00B72D8F  48 0F 49 84 24 C8 00 00 00      cmovns rax, qword ptr [rsp + 0xc8]
00B72D98  48 89 84 CC D0 00 00 00         mov qword ptr [rsp + rcx*8 + 0xd0], rax
00B72DA0  EB 19                           jmp 0x140b72dbb
00B72DA2  4C 8D 05 C7 D4 00 00            lea r8, [rip + 0xd4c7]
00B72DA9  BA 20 00 00 00                  mov edx, 0x20
00B72DAE  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
00B72DB6  E8 65 31 99 FF                  call 0x140505f20
00B72DBB  FF C3                           inc ebx
00B72DBD  E9 4F FF FF FF                  jmp 0x140b72d11
00B72DC2  4C 8D 05 D7 D4 00 00            lea r8, [rip + 0xd4d7]
00B72DC9  BA 20 00 00 00                  mov edx, 0x20
00B72DCE  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
00B72DD6  E8 45 31 99 FF                  call 0x140505f20
00B72DDB  4C 8D B4 24 F8 00 00 00         lea r14, [rsp + 0xf8]
00B72DE3  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
00B72DE8  48 8D 35 D1 D4 00 00            lea rsi, [rip + 0xd4d1]
00B72DEF  48 8B DE                        mov rbx, rsi
00B72DF2  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00B72DF7  33 C9                           xor ecx, ecx
00B72DF9  E8 FA F2 D5 FF                  call 0x1408d20f8
00B72DFE  48 85 C0                        test rax, rax
00B72E01  0F 84 0B 02 00 00               je 0x140b73012
00B72E07  4C 8B 50 18                     mov r10, qword ptr [rax + 0x18]
00B72E0B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00B72E14  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
00B72E1B  48 3B 15 8E 3C 45 00            cmp rdx, qword ptr [rip + 0x453c8e]
00B72E22  75 04                           jne 0x140b72e28
00B72E24  4C 8B 50 20                     mov r10, qword ptr [rax + 0x20]
00B72E28  66 F7 DF                        neg di
00B72E2B  45 1B C0                        sbb r8d, r8d
00B72E2E  41 81 E0 09 04 00 00            and r8d, 0x409
00B72E35  48 8D 84 24 B8 00 00 00         lea rax, [rsp + 0xb8]
00B72E3D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B72E42  45 8B CF                        mov r9d, r15d
00B72E45  BA 0B 00 00 00                  mov edx, 0xb
00B72E4A  49 8B CA                        mov rcx, r10
00B72E4D  E8 CE 83 E2 FF                  call 0x14099b220
00B72E52  85 C0                           test eax, eax
00B72E54  79 15                           jns 0x140b72e6b
00B72E56  48 8B DE                        mov rbx, rsi
00B72E59  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00B72E5E  4C 8B F6                        mov r14, rsi
00B72E61  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
00B72E66  E9 81 01 00 00                  jmp 0x140b72fec
00B72E6B  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00B72E73  F6 41 02 01                     test byte ptr [rcx + 2], 1
00B72E77  0F 84 94 00 00 00               je 0x140b72f11
00B72E7D  48 8D 51 04                     lea rdx, [rcx + 4]
00B72E81  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00B72E86  E8 F5 78 8B FF                  call 0x14042a780
00B72E8B  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00B72E90  E8 EB 9F D9 FF                  call 0x14090ce80
00B72E95  66 89 84 24 88 00 00 00         mov word ptr [rsp + 0x88], ax
00B72E9D  0F B7 F8                        movzx edi, ax
00B72EA0  83 C7 10                        add edi, 0x10
00B72EA3  8B D7                           mov edx, edi
00B72EA5  B9 40 00 00 00                  mov ecx, 0x40
00B72EAA  41 B8 45 72 72 20               mov r8d, 0x20727245
00B72EB0  E8 3B F2 00 00                  call 0x140b820f0
00B72EB5  48 8B D8                        mov rbx, rax
00B72EB8  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00B72EBD  48 85 C0                        test rax, rax
00B72EC0  74 33                           je 0x140b72ef5
00B72EC2  66 89 BC 24 8A 00 00 00         mov word ptr [rsp + 0x8a], di
00B72ECA  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00B72ED2  45 33 C0                        xor r8d, r8d
00B72ED5  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00B72EDA  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
00B72EE2  E8 09 A3 D9 FF                  call 0x14090d1f0
00B72EE7  85 C0                           test eax, eax
00B72EE9  79 20                           jns 0x140b72f0b
00B72EEB  33 D2                           xor edx, edx
00B72EED  48 8B CB                        mov rcx, rbx
00B72EF0  E8 7B F9 00 00                  call 0x140b82870
00B72EF5  48 8B DE                        mov rbx, rsi
00B72EF8  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00B72EFD  48 8B C6                        mov rax, rsi
00B72F00  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B72F05  48 83 CF FF                     or rdi, 0xffffffffffffffff
00B72F09  EB 65                           jmp 0x140b72f70
00B72F0B  48 83 CF FF                     or rdi, 0xffffffffffffffff
00B72F0F  EB 48                           jmp 0x140b72f59
00B72F11  4C 8D 71 04                     lea r14, [rcx + 4]
00B72F15  48 83 CF FF                     or rdi, 0xffffffffffffffff
00B72F19  48 8B C7                        mov rax, rdi
00B72F1C  48 FF C0                        inc rax
00B72F1F  41 80 3C 06 00                  cmp byte ptr [r14 + rax], 0
00B72F24  75 F6                           jne 0x140b72f1c
00B72F26  83 C0 10                        add eax, 0x10
00B72F29  44 8B E8                        mov r13d, eax
00B72F2C  41 B8 45 72 72 20               mov r8d, 0x20727245
00B72F32  8B D0                           mov edx, eax
00B72F34  B9 40 00 00 00                  mov ecx, 0x40
00B72F39  E8 B2 F1 00 00                  call 0x140b820f0
00B72F3E  48 8B D8                        mov rbx, rax
00B72F41  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00B72F46  48 85 C0                        test rax, rax
00B72F49  74 15                           je 0x140b72f60
00B72F4B  4D 8B C6                        mov r8, r14
00B72F4E  41 8B D5                        mov edx, r13d
00B72F51  48 8B C8                        mov rcx, rax
00B72F54  E8 57 30 99 FF                  call 0x140505fb0
00B72F59  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00B72F5E  EB 10                           jmp 0x140b72f70
00B72F60  48 8B C6                        mov rax, rsi
00B72F63  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B72F68  48 8B DE                        mov rbx, rsi
00B72F6B  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00B72F70  48 3B DE                        cmp rbx, rsi
00B72F73  74 61                           je 0x140b72fd6
00B72F75  48 8B C3                        mov rax, rbx
00B72F78  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00B72F7D  48 FF C7                        inc rdi
00B72F80  80 3C 3B 00                     cmp byte ptr [rbx + rdi], 0
00B72F84  75 F7                           jne 0x140b72f7d
00B72F86  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
00B72F8A  83 CA FF                        or edx, 0xffffffff
00B72F8D  85 FF                           test edi, edi
00B72F8F  74 15                           je 0x140b72fa6
00B72F91  80 38 20                        cmp byte ptr [rax], 0x20
00B72F94  7C 10                           jl 0x140b72fa6
00B72F96  48 FF C0                        inc rax
00B72F99  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B72F9E  03 FA                           add edi, edx
00B72FA0  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
00B72FA4  EB E7                           jmp 0x140b72f8d
00B72FA6  C6 00 00                        mov byte ptr [rax], 0
00B72FA9  48 FF C0                        inc rax
00B72FAC  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B72FB1  03 FA                           add edi, edx
00B72FB3  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
00B72FB7  85 FF                           test edi, edi
00B72FB9  74 1F                           je 0x140b72fda
00B72FBB  8A 08                           mov cl, byte ptr [rax]
00B72FBD  84 C9                           test cl, cl
00B72FBF  74 19                           je 0x140b72fda
00B72FC1  80 F9 20                        cmp cl, 0x20
00B72FC4  7F 14                           jg 0x140b72fda
00B72FC6  48 FF C0                        inc rax
00B72FC9  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B72FCE  03 FA                           add edi, edx
00B72FD0  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
00B72FD4  EB E1                           jmp 0x140b72fb7
00B72FD6  8B 7C 24 40                     mov edi, dword ptr [rsp + 0x40]
00B72FDA  4C 8D 35 AF D2 00 00            lea r14, [rip + 0xd2af]
00B72FE1  85 FF                           test edi, edi
00B72FE3  4C 0F 45 F0                     cmovne r14, rax
00B72FE7  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
00B72FEC  EB 24                           jmp 0x140b73012
00B72FEE  4C 8D 35 CB D2 00 00            lea r14, [rip + 0xd2cb]
00B72FF5  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
00B72FFA  48 8D 1D BF D2 00 00            lea rbx, [rip + 0xd2bf]
00B73001  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00B73006  48 8D 35 B3 D2 00 00            lea rsi, [rip + 0xd2b3]
00B7300D  44 8B 7C 24 58                  mov r15d, dword ptr [rsp + 0x58]
00B73012  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00B73017  45 8B CF                        mov r9d, r15d
00B7301A  4C 8D 05 FF D1 00 00            lea r8, [rip + 0xd1ff]
00B73021  BF 00 01 00 00                  mov edi, 0x100
00B73026  8B D7                           mov edx, edi
00B73028  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
00B73030  E8 D7 8B 9C FF                  call 0x14053bc0c
00B73035  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00B73039  EB 1F                           jmp 0x140b7305a
00B7303B  B8 01 00 00 C0                  mov eax, 0xc0000001
00B73040  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00B73044  48 8D 35 75 D2 00 00            lea rsi, [rip + 0xd275]
00B7304B  BF 00 01 00 00                  mov edi, 0x100
00B73050  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00B73055  44 8B 7C 24 58                  mov r15d, dword ptr [rsp + 0x58]
00B7305A  85 C0                           test eax, eax
00B7305C  79 1A                           jns 0x140b73078
00B7305E  45 8B CF                        mov r9d, r15d
00B73061  4C 8D 05 A8 D1 00 00            lea r8, [rip + 0xd1a8]
00B73068  48 8B D7                        mov rdx, rdi
00B7306B  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
00B73073  E8 94 8B 9C FF                  call 0x14053bc0c
00B73078  48 8B 0D 81 3B 45 00            mov rcx, qword ptr [rip + 0x453b81]
00B7307F  E8 5C A1 ED FF                  call 0x140a4d1e0
00B73084  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
00B73089  48 8B DE                        mov rbx, rsi
00B7308C  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
00B73094  48 8D 94 24 20 01 00 00         lea rdx, [rsp + 0x120]
00B7309C  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
00B730A4  E8 97 DE 8F FF                  call 0x140470f40
00B730A9  41 B0 01                        mov r8b, 1
00B730AC  48 8D 94 24 88 00 00 00         lea rdx, [rsp + 0x88]
00B730B4  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00B730B9  E8 E2 8D D9 FF                  call 0x14090bea0
00B730BE  85 C0                           test eax, eax
00B730C0  78 5C                           js 0x140b7311e
00B730C2  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00B730C7  E8 B4 9D D9 FF                  call 0x14090ce80
00B730CC  66 89 84 24 98 00 00 00         mov word ptr [rsp + 0x98], ax
00B730D4  66 89 84 24 9A 00 00 00         mov word ptr [rsp + 0x9a], ax
00B730DC  0F B7 D0                        movzx edx, ax
00B730DF  B9 40 00 00 00                  mov ecx, 0x40
00B730E4  41 B8 45 72 72 20               mov r8d, 0x20727245
00B730EA  E8 01 F0 00 00                  call 0x140b820f0
00B730EF  48 8B F0                        mov rsi, rax
00B730F2  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00B730FA  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00B730FF  48 85 C0                        test rax, rax
00B73102  74 1A                           je 0x140b7311e
00B73104  45 33 C0                        xor r8d, r8d
00B73107  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00B7310C  48 8D 8C 24 98 00 00 00         lea rcx, [rsp + 0x98]
00B73114  E8 F7 EA F4 FF                  call 0x140ac1c10
00B73119  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
00B7311E  90                              nop
00B7311F  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
00B73127  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B7312C  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00B73134  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B73139  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00B73141  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B73146  4C 8B 8C 24 D0 00 00 00         mov r9, qword ptr [rsp + 0xd0]
00B7314E  4D 8B C6                        mov r8, r14
00B73151  48 8B D7                        mov rdx, rdi
00B73154  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
00B7315C  E8 AB 8A 9C FF                  call 0x14053bc0c
00B73161  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00B73165  EB 20                           jmp 0x140b73187
00B73167  B8 01 00 00 C0                  mov eax, 0xc0000001
00B7316C  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00B73170  BF 00 01 00 00                  mov edi, 0x100
00B73175  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00B7317A  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
00B73182  44 8B 7C 24 58                  mov r15d, dword ptr [rsp + 0x58]
00B73187  85 C0                           test eax, eax
00B73189  79 4E                           jns 0x140b731d9
00B7318B  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
00B73193  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B73198  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00B731A0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B731A5  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00B731AD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B731B2  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00B731BA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B731BF  45 8B CF                        mov r9d, r15d
00B731C2  4C 8D 05 67 D0 00 00            lea r8, [rip + 0xd067]
00B731C9  48 8B D7                        mov rdx, rdi
00B731CC  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
00B731D4  E8 33 8A 9C FF                  call 0x14053bc0c
00B731D9  48 8D 94 24 20 01 00 00         lea rdx, [rsp + 0x120]
00B731E1  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
00B731E9  E8 52 DD 8F FF                  call 0x140470f40
00B731EE  41 B0 01                        mov r8b, 1
00B731F1  48 8D 94 24 88 00 00 00         lea rdx, [rsp + 0x88]
00B731F9  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00B731FE  E8 9D 8C D9 FF                  call 0x14090bea0
00B73203  85 C0                           test eax, eax
00B73205  78 52                           js 0x140b73259
00B73207  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00B7320C  E8 6F 9C D9 FF                  call 0x14090ce80
00B73211  66 89 84 24 98 00 00 00         mov word ptr [rsp + 0x98], ax
00B73219  66 89 84 24 9A 00 00 00         mov word ptr [rsp + 0x9a], ax
00B73221  0F B7 D0                        movzx edx, ax
00B73224  B9 40 00 00 00                  mov ecx, 0x40
00B73229  41 B8 45 72 72 20               mov r8d, 0x20727245
00B7322F  E8 BC EE 00 00                  call 0x140b820f0
00B73234  48 8B D8                        mov rbx, rax
00B73237  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00B7323F  48 85 C0                        test rax, rax
00B73242  74 15                           je 0x140b73259
00B73244  45 33 C0                        xor r8d, r8d
00B73247  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00B7324C  48 8D 8C 24 98 00 00 00         lea rcx, [rsp + 0x98]
00B73254  E8 B7 E9 F4 FF                  call 0x140ac1c10
00B73259  E8 B2 24 6B FF                  call 0x140225710
00B7325E  48 85 C0                        test rax, rax
00B73261  74 2D                           je 0x140b73290
00B73263  41 8B D7                        mov edx, r15d
00B73266  48 8B C8                        mov rcx, rax
00B73269  E8 B2 C3 C0 FF                  call 0x14077f620
00B7326E  48 8B 8C 24 20 02 00 00         mov rcx, qword ptr [rsp + 0x220]
00B73276  48 33 CC                        xor rcx, rsp
00B73279  E8 C2 93 B3 FF                  call 0x1406ac640
00B7327E  48 81 C4 38 02 00 00            add rsp, 0x238
00B73285  41 5F                           pop r15
00B73287  41 5E                           pop r14
00B73289  41 5D                           pop r13
00B7328B  5F                              pop rdi
00B7328C  5E                              pop rsi
00B7328D  5B                              pop rbx
00B7328E  C3                              ret
00B7328F  CC                              int3
00B73290  8B 94 24 A8 00 00 00            mov edx, dword ptr [rsp + 0xa8]
00B73297  80 BC 24 90 02 00 00 00         cmp byte ptr [rsp + 0x290], 0
00B7329F  74 22                           je 0x140b732c3
00B732A1  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00B732A6  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00B732AB  4C 8D 8C 24 D0 00 00 00         lea r9, [rsp + 0xd0]
00B732B3  44 8B C2                        mov r8d, edx
00B732B6  BA 4C 00 00 00                  mov edx, 0x4c
00B732BB  B1 01                           mov cl, 1
00B732BD  E8 BE B2 BE FF                  call 0x14075e580
00B732C2  CC                              int3
00B732C3  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00B732C8  4C 8B CE                        mov r9, rsi
00B732CB  4C 8D 84 24 D0 00 00 00         lea r8, [rsp + 0xd0]
00B732D3  B9 4C 00 00 00                  mov ecx, 0x4c
00B732D8  E8 83 A3 98 FF                  call 0x1404fd660
00B732DD  90                              nop
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpSystemErrorHandler2(int a1, int a2, int a3, __int64 a4, unsigned __int8 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m148;
    unsigned __int8 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int16 v_stack_m1CE;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int16 v_stack_m1DE;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1F0;
    unsigned int v_stack_m1F8;
    unsigned __int16 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned int v_stack_m210;
    unsigned int v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned int v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_pA8;
    unsigned __int64 v_stack_pD0;

    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (568);
    result = (*(unsigned __int64 *)(v_rip + 2718452)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m210 = a1;
    v_stack_m1C0 = a1;
    v_stack_m1B8 = a4;
    v_stack_m1E0 = v_xmm0;
    v_stack_m1F0 = v_xmm1;
    v_stack_m1D0 = v_xmm0;
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    v_stack_m200 = (unsigned __int16)(*(unsigned __int16 *)(result + 1044));
    result = 5;
    if (a2 <= 5) { result = a2; }
    v_stack_m1F8 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_m170 = 0;
    result = 0;
    v_stack_m198 = v_xmm0;
    v_stack_m188 = v_xmm0;
    v_stack_m178 = 0;
    a3 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) << (3);
    result = memcpy(v_stack_m198, a4, a3, a4);
    v_rbx = 0;
loc_00B72D11:
    v_stack_m228 = 0;
    if (0 >= ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_00B72DC2;
    if (0 >= ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_00B72DA2;
    result = strcat_s(v_stack_m170, 32, v_rip + 54662, a4);
    result = RtlUnicodeStringToAnsiString(v_stack_m1A8, *(unsigned __int64 *)(a4 + v_rbx * 8), 1, a4);
    v_stack_m218 = (unsigned int)(result);
    goto loc_00B72D84;
loc_00B72D84:
    result = v_rip + 54515;
    if (!sign_flag) { result = v_stack_m1A0; }
    *(unsigned __int64 *)(v_rsp + 0 * 8 + 208) = result;
    goto loc_00B72DBB;
loc_00B72DA2:
    result = strcat_s(v_stack_m170, 32, v_rip + 54471, a4);
loc_00B72DBB:
    v_rbx = (unsigned int)((v_rbx) + 1);
    goto loc_00B72D11;
loc_00B72DC2:
    result = strcat_s(v_stack_m170, 32, v_rip + 54487, a4);
    v_stack_m220 = v_stack_m170;
    v_stack_m208 = v_rip + 54481;
    a1 = 0;
    result = PsQuerySystemDllInfo(a1, 32, v_rip + 54487, a4);
    if (result == 0) goto loc_00B73012;
    v_r10 = *(unsigned __int64 *)(result + 24);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) == (*(unsigned __int64 *)(v_rip + 4537486))) {
        v_r10 = *(unsigned __int64 *)(result + 32);
    }
    v_rdi = (unsigned __int16)(-(*(unsigned __int16 *)(result + 1044)));
    a3 = (unsigned int)((v_rip + 54487) & (0x409ULL));
    v_stack_m248 = v_stack_m1B0;
    result = RtlFindMessage(v_r10, 11, a3, (unsigned int)((unsigned int)((unsigned int)(a1))));
    if (!sign_flag) goto loc_00B72E6B;
    v_stack_m208 = v_rip + 54481;
    v_stack_m220 = v_rip + 54481;
    goto loc_00B72FEC;
loc_00B72E6B:
    if (((*(unsigned __int8 *)(v_stack_m1B0 + 2)) & (1)) == 0) goto loc_00B72F11;
    result = RtlInitUnicodeString(v_stack_m1F0, v_stack_m1B0 + 4, a3, (unsigned int)((unsigned int)((unsigned int)(a1))));
    result = RtlxUnicodeStringToAnsiSize(v_stack_m1F0, v_stack_m1B0 + 4, a3, (unsigned int)((unsigned int)((unsigned int)(a1))));
    v_stack_m1E0 = (unsigned __int16)(result);
    v_rdi = (unsigned int)(((unsigned __int16)(result)) + (16));
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x20727245ULL), (unsigned int)((unsigned int)((unsigned int)(a1))));
    v_stack_m208 = result;
    if (result == 0) goto loc_00B72EF5;
    v_stack_m1DE = (unsigned __int16)(v_rdi);
    v_stack_m1D8 = result;
    a3 = 0;
    result = RtlUnicodeStringToAnsiString(v_stack_m1E0, v_stack_m1F0, a3, (unsigned int)((unsigned int)((unsigned int)(a1))));
    if (!sign_flag) goto loc_00B72F0B;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a1))));
loc_00B72EF5:
    v_stack_m208 = v_rip + 54481;
    v_stack_m220 = v_rip + 54481;
    v_rdi = (v_rdi) | (-1);
    goto loc_00B72F70;
loc_00B72F0B:
    v_rdi = (v_rdi) | (-1);
    goto loc_00B72F59;
loc_00B72F11:
    v_rdi = (v_rdi) | (-1);
loc_00B72F1C:
    result = (v_rdi) + 1;
    if ((*(unsigned __int8 *)(result + 4 + result * 1)) != 0) goto loc_00B72F1C;
    result = (unsigned int)((result) + (16));
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)(result)), (unsigned int)(0x20727245ULL), (unsigned int)((unsigned int)((unsigned int)(a1))));
    v_stack_m208 = result;
    if (result == 0) goto loc_00B72F60;
    result = strcpy_s(result, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result + 4, (unsigned int)((unsigned int)((unsigned int)(a1))));
loc_00B72F59:
    goto loc_00B72F70;
loc_00B72F60:
    v_stack_m220 = v_rip + 54481;
    v_stack_m208 = v_rip + 54481;
loc_00B72F70:
    if ((v_rip + 54481) == (v_rip + 54481)) goto loc_00B72FD6;
    v_stack_m220 = v_rip + 54481;
loc_00B72F7D:
    v_rdi = (v_rdi) + 1;
    if ((*(unsigned __int8 *)(v_rip + 54481 + v_rdi * 1)) != 0) goto loc_00B72F7D;
    v_stack_m228 = (unsigned int)(v_rdi);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) | (0xFFFFFFFFULL));
loc_00B72F8D:
    if ((unsigned int)(v_rdi) == 0) goto loc_00B72FA6;
    if ((*(unsigned __int8 *)(v_rip + 54481)) < 32) goto loc_00B72FA6;
    result = (v_rip + 54481) + 1;
    v_stack_m220 = result;
    v_rdi = (unsigned int)((v_rdi) + (a2));
    v_stack_m228 = (unsigned int)(v_rdi);
    goto loc_00B72F8D;
loc_00B72FA6:
    *(unsigned __int8 *)(result) = 0;
    result = (result) + 1;
    v_stack_m220 = result;
    v_rdi = (unsigned int)((v_rdi) + (a2));
    v_stack_m228 = (unsigned int)(v_rdi);
loc_00B72FB7:
    if ((unsigned int)(v_rdi) == 0) goto loc_00B72FDA;
    if ((unsigned __int8)(*(unsigned __int8 *)(result)) == 0) goto loc_00B72FDA;
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) > 32) goto loc_00B72FDA;
    result = (result) + 1;
    v_stack_m220 = result;
    v_rdi = (unsigned int)((v_rdi) + (a2));
    v_stack_m228 = (unsigned int)(v_rdi);
    goto loc_00B72FB7;
loc_00B72FD6:
loc_00B72FDA:
    v_r14 = v_rip + 53935;
    if ((unsigned int)((unsigned int)(v_stack_m228)) != 0) { v_r14 = result; }
    v_stack_m220 = v_r14;
loc_00B72FEC:
    goto loc_00B73012;
loc_00B73012:
    v_stack_m248 = v_rip + 54481;
    result = RtlStringCbPrintfA(v_stack_m148, 256, v_rip + 53759, (unsigned int)((unsigned int)((unsigned int)(a1))));
    v_stack_m218 = (unsigned int)(result);
    goto loc_00B7305A;
loc_00B7305A:
    if (sign_flag) {
        a4 = (unsigned int)((unsigned int)(a1));
        a3 = v_rip + 53672;
        a2 = 256;
        a1 = v_stack_m148;
        result = RtlStringCbPrintfA(a1, a2, a3, a4);
    }
    result = MmLockPagableSectionByHandle(*(unsigned __int64 *)(v_rip + 4537217), a2, a3, a4);
    v_stack_m1F8 = v_rip + 54481;
    v_stack_m1B8 = v_rip + 54481;
    result = RtlInitAnsiString(v_stack_m1E0, v_stack_m148, a3, a4);
    result = RtlAnsiStringToUnicodeString(v_stack_m1F0, v_stack_m1E0, 1, a4);
    if (sign_flag) goto loc_00B7311E;
    result = RtlxUnicodeStringToAnsiSize(v_stack_m1F0, v_stack_m1E0, 1, a4);
    v_stack_m1D0 = (unsigned __int16)(result);
    v_stack_m1CE = (unsigned __int16)(result);
    result = ExAllocatePool2(64, (unsigned __int16)(result), (unsigned int)(0x20727245ULL), a4);
    v_stack_m1C8 = result;
    v_stack_m1F8 = result;
    if (result != 0) {
        a3 = 0;
        a2 = v_stack_m1F0;
        a1 = v_stack_m1D0;
        result = RtlUnicodeStringToOemString(a1, a2, a3, a4);
        v_stack_m1F8 = result;
    }
    v_stack_m238 = v_stack_m180;
    v_stack_m240 = v_stack_m188;
    v_stack_m248 = v_stack_m190;
    result = RtlStringCbPrintfA(v_stack_m148, 256, v_r14, v_stack_m198);
    v_stack_m218 = (unsigned int)(result);
    goto loc_00B73187;
loc_00B73187:
    if (sign_flag) {
        result = v_stack_m180;
        v_stack_m230 = result;
        result = v_stack_m188;
        v_stack_m238 = result;
        result = v_stack_m190;
        v_stack_m240 = result;
        result = v_stack_m198;
        v_stack_m248 = result;
        a4 = (unsigned int)((unsigned int)(a1));
        a3 = v_rip + 53351;
        a2 = 256;
        a1 = v_stack_m148;
        result = RtlStringCbPrintfA(a1, a2, a3, a4);
    }
    result = RtlInitAnsiString(v_stack_m1E0, v_stack_m148, a3, a4);
    result = RtlAnsiStringToUnicodeString(v_stack_m1F0, v_stack_m1E0, 1, a4);
    if (sign_flag) goto loc_00B73259;
    result = RtlxUnicodeStringToAnsiSize(v_stack_m1F0, v_stack_m1E0, 1, a4);
    v_stack_m1D0 = (unsigned __int16)(result);
    v_stack_m1CE = (unsigned __int16)(result);
    result = ExAllocatePool2(64, (unsigned __int16)(result), (unsigned int)(0x20727245ULL), a4);
    v_stack_m1C8 = result;
    if (result != 0) {
        a3 = 0;
        a2 = v_stack_m1F0;
        a1 = v_stack_m1D0;
        result = RtlUnicodeStringToOemString(a1, a2, a3, a4);
    }
    result = PsGetCurrentServerSilo(a1, a2, a3, a4);
    if (result == 0) goto loc_00B73290;
    result = PsTerminateServerSilo(result, (unsigned int)((unsigned int)((unsigned int)(a1))), a3, a4);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)((unsigned int)((unsigned int)(a1))), a3, a4);
    v_rsp = (v_rsp) + (568);
    return result;
loc_00B73290:
    if (a5 != 0) {
        v_stack_p28 = result;
        v_stack_p20 = result;
        a4 = v_stack_pD0;
        a3 = (unsigned int)((unsigned int)(v_stack_pA8));
        a2 = 76;
        a1 = 1;
        result = PoShutdownBugCheck(a1, a2, a3, a4);
    }
    v_stack_p20 = result;
    result = KeBugCheckEx(76, a2, v_stack_pD0, result);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpSystemErrorHandler2(int32_t Arg1, int32_t Arg2, int32_t Arg3, void *Arg4, uint8_t Arg5)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m148;
    uint8_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint16_t v_stack_m1CE;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint16_t v_stack_m1DE;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1F0;
    uint32_t v_stack_m1F8;
    uint16_t v_stack_m200;
    uint64_t v_stack_m208;
    uint32_t v_stack_m210;
    uint32_t v_stack_m218;
    uint64_t v_stack_m220;
    uint32_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m48;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_pA8;
    uint64_t v_stack_pD0;

    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (568);
    result = (*(uint64_t *)(v_rip + 0x297AF4)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m210 = Arg1;
    v_stack_m1C0 = Arg1;
    v_stack_m1B8 = Arg4;
    v_stack_m1E0 = v_xmm0;
    v_stack_m1F0 = v_xmm1;
    v_stack_m1D0 = v_xmm0;
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, Arg3, Arg4);
    v_stack_m200 = (uint16_t)(*(uint16_t *)(result + 0x414));
    result = 5;
    if (Arg2 <= 5) { result = Arg2; }
    v_stack_m1F8 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_m170 = 0;
    result = 0;
    v_stack_m198 = v_xmm0;
    v_stack_m188 = v_xmm0;
    v_stack_m178 = 0;
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) << (3);
    result = memcpy(v_stack_m198, Arg4, Arg3, Arg4);
    local_rbx = 0;
loc_00B72D11:
    v_stack_m228 = 0;
    if (0 >= ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_00B72DC2;
    if (0 >= ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_00B72DA2;
    result = strcat_s(v_stack_m170, 32, v_rip + 54662, Arg4);
    result = RtlUnicodeStringToAnsiString(v_stack_m1A8, *(uint64_t *)(arg4 + local_rbx * 8), 1, Arg4);
    v_stack_m218 = (uint32_t)(result);
    goto loc_00B72D84;
loc_00B72D84:
    result = v_rip + 54515;
    if (!sign_flag) { result = v_stack_m1A0; }
    *(uint64_t *)(local_rsp + 0x0 * 8 + 0xD0) = result;
    goto loc_00B72DBB;
loc_00B72DA2:
    result = strcat_s(v_stack_m170, 32, v_rip + 54471, Arg4);
loc_00B72DBB:
    local_rbx = (uint32_t)((local_rbx) + 1);
    goto loc_00B72D11;
loc_00B72DC2:
    result = strcat_s(v_stack_m170, 32, v_rip + 54487, Arg4);
    v_stack_m220 = v_stack_m170;
    v_stack_m208 = v_rip + 54481;
    Arg1 = 0;
    result = PsQuerySystemDllInfo(Arg1, 32, v_rip + 54487, Arg4);
    if (result == 0) goto loc_00B73012;
    local_r10 = *(uint64_t *)(result + 0x18);
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) == (*(uint64_t *)(v_rip + 0x453C8E))) {
        local_r10 = *(uint64_t *)(result + 0x20);
    }
    local_rdi = (uint16_t)(-(*(uint16_t *)(result + 0x414)));
    Arg3 = (uint32_t)((v_rip + 54487) & (0x409ULL));
    v_stack_m248 = v_stack_m1B0;
    result = RtlFindMessage(local_r10, 11, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg1))));
    if (!sign_flag) goto loc_00B72E6B;
    v_stack_m208 = v_rip + 54481;
    v_stack_m220 = v_rip + 54481;
    goto loc_00B72FEC;
loc_00B72E6B:
    if (((*(uint8_t *)(v_stack_m1B0 + 0x2)) & (1)) == 0) goto loc_00B72F11;
    result = RtlInitUnicodeString(v_stack_m1F0, v_stack_m1B0 + 4, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg1))));
    result = RtlxUnicodeStringToAnsiSize(v_stack_m1F0, v_stack_m1B0 + 4, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg1))));
    v_stack_m1E0 = (uint16_t)(result);
    local_rdi = (uint32_t)(((uint16_t)(result)) + (16));
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x20727245ULL), (uint32_t)((uint32_t)((uint32_t)(Arg1))));
    v_stack_m208 = result;
    if (result == 0) goto loc_00B72EF5;
    v_stack_m1DE = (uint16_t)(local_rdi);
    v_stack_m1D8 = result;
    Arg3 = 0;
    result = RtlUnicodeStringToAnsiString(v_stack_m1E0, v_stack_m1F0, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg1))));
    if (!sign_flag) goto loc_00B72F0B;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg1))));
loc_00B72EF5:
    v_stack_m208 = v_rip + 54481;
    v_stack_m220 = v_rip + 54481;
    local_rdi = (local_rdi) | (-1);
    goto loc_00B72F70;
loc_00B72F0B:
    local_rdi = (local_rdi) | (-1);
    goto loc_00B72F59;
loc_00B72F11:
    local_rdi = (local_rdi) | (-1);
loc_00B72F1C:
    result = (local_rdi) + 1;
    if ((*(uint8_t *)(result + 0x4 + result * 1)) != 0) goto loc_00B72F1C;
    result = (uint32_t)((result) + (16));
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)(result)), (uint32_t)(0x20727245ULL), (uint32_t)((uint32_t)((uint32_t)(Arg1))));
    v_stack_m208 = result;
    if (result == 0) goto loc_00B72F60;
    result = strcpy_s(result, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result + 4, (uint32_t)((uint32_t)((uint32_t)(Arg1))));
loc_00B72F59:
    goto loc_00B72F70;
loc_00B72F60:
    v_stack_m220 = v_rip + 54481;
    v_stack_m208 = v_rip + 54481;
loc_00B72F70:
    if ((v_rip + 54481) == (v_rip + 54481)) goto loc_00B72FD6;
    v_stack_m220 = v_rip + 54481;
loc_00B72F7D:
    local_rdi = (local_rdi) + 1;
    if ((*(uint8_t *)(v_rip + 0xD4D1 + local_rdi * 1)) != 0) goto loc_00B72F7D;
    v_stack_m228 = (uint32_t)(local_rdi);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) | (0xFFFFFFFFULL));
loc_00B72F8D:
    if ((uint32_t)(local_rdi) == 0) goto loc_00B72FA6;
    if ((*(uint8_t *)(v_rip + 0xD4D1)) < 32) goto loc_00B72FA6;
    result = (v_rip + 54481) + 1;
    v_stack_m220 = result;
    local_rdi = (uint32_t)((local_rdi) + (Arg2));
    v_stack_m228 = (uint32_t)(local_rdi);
    goto loc_00B72F8D;
loc_00B72FA6:
    *(uint8_t *)(result) = 0;
    result = (result) + 1;
    v_stack_m220 = result;
    local_rdi = (uint32_t)((local_rdi) + (Arg2));
    v_stack_m228 = (uint32_t)(local_rdi);
loc_00B72FB7:
    if ((uint32_t)(local_rdi) == 0) goto loc_00B72FDA;
    if ((uint8_t)(*(uint8_t *)(result)) == 0) goto loc_00B72FDA;
    if (((uint8_t)(*(uint8_t *)(result))) > 32) goto loc_00B72FDA;
    result = (result) + 1;
    v_stack_m220 = result;
    local_rdi = (uint32_t)((local_rdi) + (Arg2));
    v_stack_m228 = (uint32_t)(local_rdi);
    goto loc_00B72FB7;
loc_00B72FD6:
loc_00B72FDA:
    local_r14 = v_rip + 53935;
    if ((uint32_t)((uint32_t)(v_stack_m228)) != 0) { local_r14 = result; }
    v_stack_m220 = local_r14;
loc_00B72FEC:
    goto loc_00B73012;
loc_00B73012:
    v_stack_m248 = v_rip + 54481;
    result = RtlStringCbPrintfA(v_stack_m148, 256, v_rip + 53759, (uint32_t)((uint32_t)((uint32_t)(Arg1))));
    v_stack_m218 = (uint32_t)(result);
    goto loc_00B7305A;
loc_00B7305A:
    if (sign_flag) {
        Arg4 = (uint32_t)((uint32_t)(Arg1));
        Arg3 = v_rip + 53672;
        Arg2 = 256;
        Arg1 = v_stack_m148;
        result = RtlStringCbPrintfA(Arg1, Arg2, Arg3, Arg4);
    }
    result = MmLockPagableSectionByHandle(*(uint64_t *)(v_rip + 0x453B81), Arg2, Arg3, Arg4);
    v_stack_m1F8 = v_rip + 54481;
    v_stack_m1B8 = v_rip + 54481;
    result = RtlInitAnsiString(v_stack_m1E0, v_stack_m148, Arg3, Arg4);
    result = RtlAnsiStringToUnicodeString(v_stack_m1F0, v_stack_m1E0, 1, Arg4);
    if (sign_flag) goto loc_00B7311E;
    result = RtlxUnicodeStringToAnsiSize(v_stack_m1F0, v_stack_m1E0, 1, Arg4);
    v_stack_m1D0 = (uint16_t)(result);
    v_stack_m1CE = (uint16_t)(result);
    result = ExAllocatePool2(64, (uint16_t)(result), (uint32_t)(0x20727245ULL), Arg4);
    v_stack_m1C8 = result;
    v_stack_m1F8 = result;
    if (result != 0) {
        Arg3 = 0;
        Arg2 = v_stack_m1F0;
        Arg1 = v_stack_m1D0;
        result = RtlUnicodeStringToOemString(Arg1, Arg2, Arg3, Arg4);
        v_stack_m1F8 = result;
    }
    v_stack_m238 = v_stack_m180;
    v_stack_m240 = v_stack_m188;
    v_stack_m248 = v_stack_m190;
    result = RtlStringCbPrintfA(v_stack_m148, 256, local_r14, v_stack_m198);
    v_stack_m218 = (uint32_t)(result);
    goto loc_00B73187;
loc_00B73187:
    if (sign_flag) {
        result = v_stack_m180;
        v_stack_m230 = result;
        result = v_stack_m188;
        v_stack_m238 = result;
        result = v_stack_m190;
        v_stack_m240 = result;
        result = v_stack_m198;
        v_stack_m248 = result;
        Arg4 = (uint32_t)((uint32_t)(Arg1));
        Arg3 = v_rip + 53351;
        Arg2 = 256;
        Arg1 = v_stack_m148;
        result = RtlStringCbPrintfA(Arg1, Arg2, Arg3, Arg4);
    }
    result = RtlInitAnsiString(v_stack_m1E0, v_stack_m148, Arg3, Arg4);
    result = RtlAnsiStringToUnicodeString(v_stack_m1F0, v_stack_m1E0, 1, Arg4);
    if (sign_flag) goto loc_00B73259;
    result = RtlxUnicodeStringToAnsiSize(v_stack_m1F0, v_stack_m1E0, 1, Arg4);
    v_stack_m1D0 = (uint16_t)(result);
    v_stack_m1CE = (uint16_t)(result);
    result = ExAllocatePool2(64, (uint16_t)(result), (uint32_t)(0x20727245ULL), Arg4);
    v_stack_m1C8 = result;
    if (result != 0) {
        Arg3 = 0;
        Arg2 = v_stack_m1F0;
        Arg1 = v_stack_m1D0;
        result = RtlUnicodeStringToOemString(Arg1, Arg2, Arg3, Arg4);
    }
    result = PsGetCurrentServerSilo(Arg1, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00B73290;
    result = PsTerminateServerSilo(result, (uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg3, Arg4);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg3, Arg4);
    local_rsp = (local_rsp) + (568);
    return result;
loc_00B73290:
    if (Arg5 != 0) {
        v_stack_p28 = result;
        v_stack_p20 = result;
        Arg4 = v_stack_pD0;
        Arg3 = (uint32_t)((uint32_t)(v_stack_pA8));
        Arg2 = 76;
        Arg1 = 1;
        result = PoShutdownBugCheck(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_p20 = result;
    result = KeBugCheckEx(76, Arg2, v_stack_pD0, result);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0 + rbx*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B72C30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
