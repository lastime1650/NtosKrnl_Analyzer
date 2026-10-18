# RtlpGetTokenNamedObjectPath

- RVA: `0x0078ED40`–`0x0078F376` (길이 `1,590` bytes)
- VA: `0x000000014078ED40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CF99C`
- 디코드: `410`개 명령, `1,590/1,590` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **42**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x0078ED94` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0078EDB3` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0078EDC4` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0078EDD3` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0078EE74` → [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) (function, `0x00AECDD0`)
- `0x0078EEA5` → [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) (function, `0x00AECDD0`)
- `0x0078EEE6` → [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) (function, `0x00AECDD0`)
- `0x0078EF16` → [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) (function, `0x00AECDD0`)
- `0x0078EF30` → [RtlConvertSidToUnicodeString](../92/RtlConvertSidToUnicodeString_function_00927B30.md) (function, `0x00927B30`)
- `0x0078EF5B` → [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) (function, `0x00AECDD0`)
- `0x0078EF79` → [RtlGetAppContainerSidType](../A7/RtlGetAppContainerSidType_function_00A72160.md) (function, `0x00A72160`)
- `0x0078EF9A` → [RtlConvertSidToUnicodeString](../92/RtlConvertSidToUnicodeString_function_00927B30.md) (function, `0x00927B30`)
- `0x0078EFCB` → [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) (function, `0x00AECDD0`)
- `0x0078EFF0` → [RtlGetCurrentServiceSessionId](../../text/22/RtlGetCurrentServiceSessionId_function_00225070.md) (function, `0x00225070`)
- `0x0078F010` → [RtlGetAppContainerParent](RtlGetAppContainerParent_function_0078E4A0.md) (function, `0x0078E4A0`)
- `0x0078F02F` → [RtlConvertSidToUnicodeString](../92/RtlConvertSidToUnicodeString_function_00927B30.md) (function, `0x00927B30`)
- `0x0078F046` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x0078F056` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x0078F066` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x0078F076` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x0078F0AF` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (function, `0x00482D5C`)
- `0x0078F0C3` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0078F0D4` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0078F136` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (function, `0x00482D5C`)
- `0x0078F173` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (function, `0x00482D5C`)
- `0x0078F188` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (function, `0x0026E9A4`)
- `0x0078F1AE` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (function, `0x004575EC`)
- `0x0078F212` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0078F235` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0078F254` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0078F273` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x0078F294` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x0078F2A6` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x0078F2BF` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x0078F2D2` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x0078F2EF` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x0078F301` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x0078F311` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0078F31D` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0078F32E` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0078F33D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0078F355` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [RtlGetAppContainerNamedObjectPath](../../text/5E/RtlGetAppContainerNamedObjectPath_function_005E6F70.md) at `0x005E7164`
- [RtlGetTokenNamedObjectPath](RtlGetTokenNamedObjectPath_function_0078E690.md) at `0x0078E6A2`

### Static image references
- `0x0078ED5F` → RVA `0x00E0A740` (`.data`; read)
- `0x0078EDE3` → RVA `0x00AFC990` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0078F07D` → RVA `0x00B055B0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0078F10C` → RVA `0x00B05680` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0078F113` → RVA `0x00B05570` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0078F123` → RVA `0x00B05660` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0078F12F` → RVA `0x00AFCB30` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0078F13D` → RVA `0x00B05630` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0078F14E` → RVA `0x00AFCAD0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0078F155` → RVA `0x00B055F0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0078F160` → RVA `0x00B05830` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **27**
  - `0x0078ED94` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0078EDB3` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0078EDC4` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0078EDD3` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0078EFF0` → [RtlGetCurrentServiceSessionId](../../text/22/RtlGetCurrentServiceSessionId_function_00225070.md) (`PAGE` → `.text`)
  - `0x0078F046` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x0078F056` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x0078F066` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x0078F076` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x0078F0AF` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (`PAGE` → `.text`)
  - `0x0078F0D4` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0078F136` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (`PAGE` → `.text`)
  - `0x0078F173` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (`PAGE` → `.text`)
  - `0x0078F188` → [RtlStringCchCopyW](../../text/26/RtlStringCchCopyW_function_0026E9A4.md) (`PAGE` → `.text`)
  - `0x0078F1AE` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (`PAGE` → `.text`)
  - `0x0078F212` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0078F235` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0078F254` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0078F273` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x0078F294` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`PAGE` → `.text`)
  - `0x0078F2A6` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`PAGE` → `.text`)
  - `0x0078F2BF` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`PAGE` → `.text`)
  - `0x0078F2D2` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`PAGE` → `.text`)
  - `0x0078F2EF` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`PAGE` → `.text`)
  - `0x0078F301` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`PAGE` → `.text`)
  - `0x0078F33D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0078F355` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0078ED40  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
0078ED45  55                              push rbp
0078ED46  56                              push rsi
0078ED47  57                              push rdi
0078ED48  41 54                           push r12
0078ED4A  41 55                           push r13
0078ED4C  41 56                           push r14
0078ED4E  41 57                           push r15
0078ED50  48 8D AC 24 40 FA FF FF         lea rbp, [rsp - 0x5c0]
0078ED58  48 81 EC C0 06 00 00            sub rsp, 0x6c0
0078ED5F  48 8B 05 DA B9 67 00            mov rax, qword ptr [rip + 0x67b9da]
0078ED66  48 33 C4                        xor rax, rsp
0078ED69  48 89 85 B0 05 00 00            mov qword ptr [rbp + 0x5b0], rax
0078ED70  33 F6                           xor esi, esi
0078ED72  41 8B F8                        mov edi, r8d
0078ED75  48 8B DA                        mov rbx, rdx
0078ED78  89 74 24 5C                     mov dword ptr [rsp + 0x5c], esi
0078ED7C  4C 8B E9                        mov r13, rcx
0078ED7F  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
0078ED84  33 D2                           xor edx, edx
0078ED86  48 8D 4D 20                     lea rcx, [rbp + 0x20]
0078ED8A  44 8D 46 50                     lea r8d, [rsi + 0x50]
0078ED8E  4D 8B F1                        mov r14, r9
0078ED91  44 8B E6                        mov r12d, esi
0078ED94  E8 A7 7E F3 FF                  call 0x1406c6c40
0078ED99  41 BF 08 02 00 00               mov r15d, 0x208
0078ED9F  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
0078EDA3  45 8B C7                        mov r8d, r15d
0078EDA6  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
0078EDAA  33 D2                           xor edx, edx
0078EDAC  48 8D 8D 90 01 00 00            lea rcx, [rbp + 0x190]
0078EDB3  E8 88 7E F3 FF                  call 0x1406c6c40
0078EDB8  45 8B C7                        mov r8d, r15d
0078EDBB  48 8D 8D A0 03 00 00            lea rcx, [rbp + 0x3a0]
0078EDC2  33 D2                           xor edx, edx
0078EDC4  E8 77 7E F3 FF                  call 0x1406c6c40
0078EDC9  33 D2                           xor edx, edx
0078EDCB  44 8D 46 58                     lea r8d, [rsi + 0x58]
0078EDCF  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0078EDD3  E8 68 7E F3 FF                  call 0x1406c6c40
0078EDD8  48 C7 45 88 02 00 04 00         mov qword ptr [rbp - 0x78], 0x40002
0078EDE0  0F 57 C0                        xorps xmm0, xmm0
0078EDE3  48 8D 05 A6 DB 36 00            lea rax, [rip + 0x36dba6]
0078EDEA  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0078EDEE  8D 4E 02                        lea ecx, [rsi + 2]
0078EDF1  8D 56 04                        lea edx, [rsi + 4]
0078EDF4  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
0078EDF8  4D 85 F6                        test r14, r14
0078EDFB  0F 84 45 05 00 00               je 0x14078f346
0078EE01  4D 85 ED                        test r13, r13
0078EE04  0F 84 3C 05 00 00               je 0x14078f346
0078EE0A  44 21 64 24 4C                  and dword ptr [rsp + 0x4c], r12d
0078EE0F  44 8D 7E 01                     lea r15d, [rsi + 1]
0078EE13  44 21 64 24 54                  and dword ptr [rsp + 0x54], r12d
0078EE18  8B C7                           mov eax, edi
0078EE1A  41 23 C7                        and eax, r15d
0078EE1D  44 88 7C 24 48                  mov byte ptr [rsp + 0x48], r15b
0078EE22  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
0078EE26  8B F7                           mov esi, edi
0078EE28  8B C7                           mov eax, edi
0078EE2A  23 F1                           and esi, ecx
0078EE2C  83 E0 08                        and eax, 8
0078EE2F  89 75 84                        mov dword ptr [rbp - 0x7c], esi
0078EE32  23 FA                           and edi, edx
0078EE34  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0078EE38  89 7D 80                        mov dword ptr [rbp - 0x80], edi
0078EE3B  0F 57 C9                        xorps xmm1, xmm1
0078EE3E  41 0F 11 06                     movups xmmword ptr [r14], xmm0
0078EE42  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
0078EE47  0F 11 4D 98                     movups xmmword ptr [rbp - 0x68], xmm1
0078EE4B  48 85 DB                        test rbx, rbx
0078EE4E  74 0A                           je 0x14078ee5a
0078EE50  4C 8B E3                        mov r12, rbx
0078EE53  44 89 7C 24 4C                  mov dword ptr [rsp + 0x4c], r15d
0078EE58  EB 72                           jmp 0x14078eecc
0078EE5A  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0078EE5F  44 8B CA                        mov r9d, edx
0078EE62  BA 1D 00 00 00                  mov edx, 0x1d
0078EE67  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0078EE6C  4C 8D 44 24 4C                  lea r8, [rsp + 0x4c]
0078EE71  49 8B CD                        mov rcx, r13
0078EE74  E8 57 DF 35 00                  call 0x140aecdd0
0078EE79  8B D8                           mov ebx, eax
0078EE7B  85 C0                           test eax, eax
0078EE7D  0F 88 85 04 00 00               js 0x14078f308
0078EE83  44 39 64 24 4C                  cmp dword ptr [rsp + 0x4c], r12d
0078EE88  74 3D                           je 0x14078eec7
0078EE8A  41 B9 50 00 00 00               mov r9d, 0x50
0078EE90  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0078EE95  4C 8D 45 20                     lea r8, [rbp + 0x20]
0078EE99  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0078EE9E  49 8B CD                        mov rcx, r13
0078EEA1  41 8D 51 CF                     lea edx, [r9 - 0x31]
0078EEA5  E8 26 DF 35 00                  call 0x140aecdd0
0078EEAA  8B D8                           mov ebx, eax
0078EEAC  85 C0                           test eax, eax
0078EEAE  0F 88 54 04 00 00               js 0x14078f308
0078EEB4  4C 8B 65 20                     mov r12, qword ptr [rbp + 0x20]
0078EEB8  4D 85 E4                        test r12, r12
0078EEBB  75 0A                           jne 0x14078eec7
0078EEBD  BB 01 00 00 C0                  mov ebx, 0xc0000001
0078EEC2  E9 41 04 00 00                  jmp 0x14078f308
0078EEC7  BA 04 00 00 00                  mov edx, 4
0078EECC  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0078EED1  44 8B CA                        mov r9d, edx
0078EED4  BA 2A 00 00 00                  mov edx, 0x2a
0078EED9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0078EEDE  4C 8D 44 24 54                  lea r8, [rsp + 0x54]
0078EEE3  49 8B CD                        mov rcx, r13
0078EEE6  E8 E5 DE 35 00                  call 0x140aecdd0
0078EEEB  8B D8                           mov ebx, eax
0078EEED  85 C0                           test eax, eax
0078EEEF  0F 88 13 04 00 00               js 0x14078f308
0078EEF5  83 7C 24 54 00                  cmp dword ptr [rsp + 0x54], 0
0078EEFA  74 43                           je 0x14078ef3f
0078EEFC  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0078EF01  41 B9 58 00 00 00               mov r9d, 0x58
0078EF07  4C 8D 45 C0                     lea r8, [rbp - 0x40]
0078EF0B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0078EF10  41 8B D7                        mov edx, r15d
0078EF13  49 8B CD                        mov rcx, r13
0078EF16  E8 B5 DE 35 00                  call 0x140aecdd0
0078EF1B  8B D8                           mov ebx, eax
0078EF1D  85 C0                           test eax, eax
0078EF1F  0F 88 E3 03 00 00               js 0x14078f308
0078EF25  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
0078EF29  48 8D 4D 98                     lea rcx, [rbp - 0x68]
0078EF2D  45 8A C7                        mov r8b, r15b
0078EF30  E8 FB 8B 19 00                  call 0x140927b30
0078EF35  8B D8                           mov ebx, eax
0078EF37  85 C0                           test eax, eax
0078EF39  0F 88 C9 03 00 00               js 0x14078f308
0078EF3F  41 B9 04 00 00 00               mov r9d, 4
0078EF45  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0078EF4A  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
0078EF4F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0078EF54  49 8B CD                        mov rcx, r13
0078EF57  41 8D 51 08                     lea edx, [r9 + 8]
0078EF5B  E8 70 DE 35 00                  call 0x140aecdd0
0078EF60  8B D8                           mov ebx, eax
0078EF62  85 C0                           test eax, eax
0078EF64  0F 88 9E 03 00 00               js 0x14078f308
0078EF6A  83 7C 24 4C 00                  cmp dword ptr [rsp + 0x4c], 0
0078EF6F  74 38                           je 0x14078efa9
0078EF71  48 8D 54 24 5C                  lea rdx, [rsp + 0x5c]
0078EF76  49 8B CC                        mov rcx, r12
0078EF79  E8 E2 31 2E 00                  call 0x140a72160
0078EF7E  8B D8                           mov ebx, eax
0078EF80  85 C0                           test eax, eax
0078EF82  0F 88 80 03 00 00               js 0x14078f308
0078EF88  83 7C 24 5C 02                  cmp dword ptr [rsp + 0x5c], 2
0078EF8D  75 79                           jne 0x14078f008
0078EF8F  45 8A C7                        mov r8b, r15b
0078EF92  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0078EF97  49 8B D4                        mov rdx, r12
0078EF9A  E8 91 8B 19 00                  call 0x140927b30
0078EF9F  8B D8                           mov ebx, eax
0078EFA1  85 C0                           test eax, eax
0078EFA3  0F 88 5F 03 00 00               js 0x14078f308
0078EFA9  41 BC 04 01 00 00               mov r12d, 0x104
0078EFAF  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0078EFB4  41 B9 20 01 00 00               mov r9d, 0x120
0078EFBA  4C 8D 45 70                     lea r8, [rbp + 0x70]
0078EFBE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0078EFC3  BA 2C 00 00 00                  mov edx, 0x2c
0078EFC8  49 8B CD                        mov rcx, r13
0078EFCB  E8 00 DE 35 00                  call 0x140aecdd0
0078EFD0  8B D8                           mov ebx, eax
0078EFD2  85 C0                           test eax, eax
0078EFD4  0F 88 2E 03 00 00               js 0x14078f308
0078EFDA  83 7C 24 54 00                  cmp dword ptr [rsp + 0x54], 0
0078EFDF  0F 85 04 01 00 00               jne 0x14078f0e9
0078EFE5  83 7C 24 4C 00                  cmp dword ptr [rsp + 0x4c], 0
0078EFEA  0F 85 F9 00 00 00               jne 0x14078f0e9
0078EFF0  E8 7B 60 A9 FF                  call 0x140225070
0078EFF5  44 8B 4C 24 58                  mov r9d, dword ptr [rsp + 0x58]
0078EFFA  44 3B C8                        cmp r9d, eax
0078EFFD  0F 84 EE 00 00 00               je 0x14078f0f1
0078F003  E9 E6 00 00 00                  jmp 0x14078f0ee
0078F008  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
0078F00D  49 8B CC                        mov rcx, r12
0078F010  E8 8B F4 FF FF                  call 0x14078e4a0
0078F015  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
0078F01A  8B D8                           mov ebx, eax
0078F01C  85 C0                           test eax, eax
0078F01E  0F 88 E9 02 00 00               js 0x14078f30d
0078F024  45 8A C7                        mov r8b, r15b
0078F027  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0078F02C  48 8B D7                        mov rdx, rdi
0078F02F  E8 FC 8A 19 00                  call 0x140927b30
0078F034  8B D8                           mov ebx, eax
0078F036  85 C0                           test eax, eax
0078F038  0F 88 CF 02 00 00               js 0x14078f30d
0078F03E  BA 0B 00 00 00                  mov edx, 0xb
0078F043  49 8B CC                        mov rcx, r12
0078F046  E8 C5 7C CC FF                  call 0x140456d10
0078F04B  BA 0A 00 00 00                  mov edx, 0xa
0078F050  49 8B CC                        mov rcx, r12
0078F053  48 8B F0                        mov rsi, rax
0078F056  E8 B5 7C CC FF                  call 0x140456d10
0078F05B  BA 09 00 00 00                  mov edx, 9
0078F060  49 8B CC                        mov rcx, r12
0078F063  48 8B F8                        mov rdi, rax
0078F066  E8 A5 7C CC FF                  call 0x140456d10
0078F06B  BA 08 00 00 00                  mov edx, 8
0078F070  49 8B CC                        mov rcx, r12
0078F073  48 8B D8                        mov rbx, rax
0078F076  E8 95 7C CC FF                  call 0x140456d10
0078F07B  8B 0E                           mov ecx, dword ptr [rsi]
0078F07D  4C 8D 05 2C 65 37 00            lea r8, [rip + 0x37652c]
0078F084  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
0078F089  41 BC 04 01 00 00               mov r12d, 0x104
0078F08F  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0078F093  41 8B D4                        mov edx, r12d
0078F096  8B 0F                           mov ecx, dword ptr [rdi]
0078F098  8B 00                           mov eax, dword ptr [rax]
0078F09A  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0078F09E  8B 0B                           mov ecx, dword ptr [rbx]
0078F0A0  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
0078F0A4  48 8D 8D A0 03 00 00            lea rcx, [rbp + 0x3a0]
0078F0AB  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0078F0AF  E8 A8 3C CF FF                  call 0x140482d5c
0078F0B4  8B D8                           mov ebx, eax
0078F0B6  85 C0                           test eax, eax
0078F0B8  0F 88 4A 02 00 00               js 0x14078f308
0078F0BE  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0078F0C3  E8 38 17 23 00                  call 0x1409c0800
0078F0C8  48 8D 95 A0 03 00 00            lea rdx, [rbp + 0x3a0]
0078F0CF  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0078F0D4  E8 A7 B6 C9 FF                  call 0x14042a780
0078F0D9  8B 7D 80                        mov edi, dword ptr [rbp - 0x80]
0078F0DC  8B 75 84                        mov esi, dword ptr [rbp - 0x7c]
0078F0DF  C6 44 24 48 00                  mov byte ptr [rsp + 0x48], 0
0078F0E4  E9 C6 FE FF FF                  jmp 0x14078efaf
0078F0E9  44 8B 4C 24 58                  mov r9d, dword ptr [rsp + 0x58]
0078F0EE  45 32 FF                        xor r15b, r15b
0078F0F1  80 7C 24 68 00                  cmp byte ptr [rsp + 0x68], 0
0078F0F6  49 8B D4                        mov rdx, r12
0078F0F9  75 4B                           jne 0x14078f146
0078F0FB  48 8D 8D 90 01 00 00            lea rcx, [rbp + 0x190]
0078F102  45 84 FF                        test r15b, r15b
0078F105  75 36                           jne 0x14078f13d
0078F107  83 7C 24 4C 00                  cmp dword ptr [rsp + 0x4c], 0
0078F10C  48 8D 05 6D 65 37 00            lea rax, [rip + 0x37656d]
0078F113  4C 8D 05 56 64 37 00            lea r8, [rip + 0x376456]
0078F11A  4C 0F 44 C0                     cmove r8, rax
0078F11E  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
0078F123  4C 8D 05 36 65 37 00            lea r8, [rip + 0x376536]
0078F12A  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
0078F12F  4C 8D 0D FA D9 36 00            lea r9, [rip + 0x36d9fa]
0078F136  E8 21 3C CF FF                  call 0x140482d5c
0078F13B  EB 50                           jmp 0x14078f18d
0078F13D  4C 8D 05 EC 64 37 00            lea r8, [rip + 0x3764ec]
0078F144  EB 42                           jmp 0x14078f188
0078F146  85 FF                           test edi, edi
0078F148  75 30                           jne 0x14078f17a
0078F14A  39 7C 24 4C                     cmp dword ptr [rsp + 0x4c], edi
0078F14E  48 8D 0D 7B D9 36 00            lea rcx, [rip + 0x36d97b]
0078F155  48 8D 05 94 64 37 00            lea rax, [rip + 0x376494]
0078F15C  48 0F 44 C1                     cmove rax, rcx
0078F160  4C 8D 05 C9 66 37 00            lea r8, [rip + 0x3766c9]
0078F167  48 8D 8D 90 01 00 00            lea rcx, [rbp + 0x190]
0078F16E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0078F173  E8 E4 3B CF FF                  call 0x140482d5c
0078F178  EB 13                           jmp 0x14078f18d
0078F17A  4C 8D 05 EF 63 37 00            lea r8, [rip + 0x3763ef]
0078F181  48 8D 8D 90 01 00 00            lea rcx, [rbp + 0x190]
0078F188  E8 17 F8 AD FF                  call 0x14026e9a4
0078F18D  8B D8                           mov ebx, eax
0078F18F  85 C0                           test eax, eax
0078F191  0F 88 71 01 00 00               js 0x14078f308
0078F197  48 83 64 24 68 00               and qword ptr [rsp + 0x68], 0
0078F19D  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
0078F1A2  BA 08 02 00 00                  mov edx, 0x208
0078F1A7  48 8D 8D 90 01 00 00            lea rcx, [rbp + 0x190]
0078F1AE  E8 39 84 CC FF                  call 0x1404575ec
0078F1B3  8B D8                           mov ebx, eax
0078F1B5  85 C0                           test eax, eax
0078F1B7  0F 88 4B 01 00 00               js 0x14078f308
0078F1BD  83 7C 24 54 00                  cmp dword ptr [rsp + 0x54], 0
0078F1C2  74 17                           je 0x14078f1db
0078F1C4  85 F6                           test esi, esi
0078F1C6  75 13                           jne 0x14078f1db
0078F1C8  0F B7 4D 98                     movzx ecx, word ptr [rbp - 0x68]
0078F1CC  8D 7E 02                        lea edi, [rsi + 2]
0078F1CF  8B DF                           mov ebx, edi
0078F1D1  48 03 5C 24 68                  add rbx, qword ptr [rsp + 0x68]
0078F1D6  48 03 D9                        add rbx, rcx
0078F1D9  EB 0A                           jmp 0x14078f1e5
0078F1DB  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
0078F1E0  BF 02 00 00 00                  mov edi, 2
0078F1E5  83 7C 24 4C 00                  cmp dword ptr [rsp + 0x4c], 0
0078F1EA  74 0E                           je 0x14078f1fa
0078F1EC  0F B7 4C 24 70                  movzx ecx, word ptr [rsp + 0x70]
0078F1F1  0F B7 C7                        movzx eax, di
0078F1F4  48 03 D8                        add rbx, rax
0078F1F7  48 03 D9                        add rbx, rcx
0078F1FA  80 7D 78 00                     cmp byte ptr [rbp + 0x78], 0
0078F1FE  44 8B 7C 24 60                  mov r15d, dword ptr [rsp + 0x60]
0078F203  74 1F                           je 0x14078f224
0078F205  45 85 FF                        test r15d, r15d
0078F208  75 1A                           jne 0x14078f224
0078F20A  48 8B 55 70                     mov rdx, qword ptr [rbp + 0x70]
0078F20E  48 8D 4D A8                     lea rcx, [rbp - 0x58]
0078F212  E8 69 B5 C9 FF                  call 0x14042a780
0078F217  0F B7 4D A8                     movzx ecx, word ptr [rbp - 0x58]
0078F21B  0F B7 C7                        movzx eax, di
0078F21E  48 03 D8                        add rbx, rax
0078F221  48 03 D9                        add rbx, rcx
0078F224  48 03 DF                        add rbx, rdi
0078F227  41 B8 53 74 72 67               mov r8d, 0x67727453
0078F22D  48 8B D3                        mov rdx, rbx
0078F230  B9 00 01 00 00                  mov ecx, 0x100
0078F235  E8 B6 2E 3F 00                  call 0x140b820f0
0078F23A  48 8B F8                        mov rdi, rax
0078F23D  48 85 C0                        test rax, rax
0078F240  75 0A                           jne 0x14078f24c
0078F242  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0078F247  E9 BC 00 00 00                  jmp 0x14078f308
0078F24C  4C 8B C3                        mov r8, rbx
0078F24F  33 D2                           xor edx, edx
0078F251  48 8B CF                        mov rcx, rdi
0078F254  E8 E7 79 F3 FF                  call 0x1406c6c40
0078F259  0F 57 C0                        xorps xmm0, xmm0
0078F25C  48 8D 95 90 01 00 00            lea rdx, [rbp + 0x190]
0078F263  41 0F 11 06                     movups xmmword ptr [r14], xmm0
0078F267  49 8B CE                        mov rcx, r14
0078F26A  66 41 89 5E 02                  mov word ptr [r14 + 2], bx
0078F26F  49 89 7E 08                     mov qword ptr [r14 + 8], rdi
0078F273  E8 18 07 C8 FF                  call 0x14040f990
0078F278  8B D8                           mov ebx, eax
0078F27A  85 C0                           test eax, eax
0078F27C  0F 88 86 00 00 00               js 0x14078f308
0078F282  83 7C 24 54 00                  cmp dword ptr [rsp + 0x54], 0
0078F287  74 28                           je 0x14078f2b1
0078F289  85 F6                           test esi, esi
0078F28B  75 24                           jne 0x14078f2b1
0078F28D  48 8D 55 88                     lea rdx, [rbp - 0x78]
0078F291  49 8B CE                        mov rcx, r14
0078F294  E8 B7 07 C8 FF                  call 0x14040fa50
0078F299  8B D8                           mov ebx, eax
0078F29B  85 C0                           test eax, eax
0078F29D  78 69                           js 0x14078f308
0078F29F  48 8D 55 98                     lea rdx, [rbp - 0x68]
0078F2A3  49 8B CE                        mov rcx, r14
0078F2A6  E8 A5 07 C8 FF                  call 0x14040fa50
0078F2AB  8B D8                           mov ebx, eax
0078F2AD  85 C0                           test eax, eax
0078F2AF  78 57                           js 0x14078f308
0078F2B1  83 7C 24 4C 00                  cmp dword ptr [rsp + 0x4c], 0
0078F2B6  74 25                           je 0x14078f2dd
0078F2B8  48 8D 55 88                     lea rdx, [rbp - 0x78]
0078F2BC  49 8B CE                        mov rcx, r14
0078F2BF  E8 8C 07 C8 FF                  call 0x14040fa50
0078F2C4  8B D8                           mov ebx, eax
0078F2C6  85 C0                           test eax, eax
0078F2C8  78 3E                           js 0x14078f308
0078F2CA  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
0078F2CF  49 8B CE                        mov rcx, r14
0078F2D2  E8 79 07 C8 FF                  call 0x14040fa50
0078F2D7  8B D8                           mov ebx, eax
0078F2D9  85 C0                           test eax, eax
0078F2DB  78 2B                           js 0x14078f308
0078F2DD  80 7D 78 00                     cmp byte ptr [rbp + 0x78], 0
0078F2E1  74 25                           je 0x14078f308
0078F2E3  45 85 FF                        test r15d, r15d
0078F2E6  75 20                           jne 0x14078f308
0078F2E8  48 8D 55 88                     lea rdx, [rbp - 0x78]
0078F2EC  49 8B CE                        mov rcx, r14
0078F2EF  E8 5C 07 C8 FF                  call 0x14040fa50
0078F2F4  8B D8                           mov ebx, eax
0078F2F6  85 C0                           test eax, eax
0078F2F8  78 0E                           js 0x14078f308
0078F2FA  48 8D 55 A8                     lea rdx, [rbp - 0x58]
0078F2FE  49 8B CE                        mov rcx, r14
0078F301  E8 4A 07 C8 FF                  call 0x14040fa50
0078F306  8B D8                           mov ebx, eax
0078F308  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
0078F30D  48 8D 4D 98                     lea rcx, [rbp - 0x68]
0078F311  E8 EA 14 23 00                  call 0x1409c0800
0078F316  85 DB                           test ebx, ebx
0078F318  79 08                           jns 0x14078f322
0078F31A  49 8B CE                        mov rcx, r14
0078F31D  E8 DE 14 23 00                  call 0x1409c0800
0078F322  80 7C 24 48 00                  cmp byte ptr [rsp + 0x48], 0
0078F327  74 0A                           je 0x14078f333
0078F329  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0078F32E  E8 CD 14 23 00                  call 0x1409c0800
0078F333  48 85 FF                        test rdi, rdi
0078F336  74 0A                           je 0x14078f342
0078F338  33 D2                           xor edx, edx
0078F33A  48 8B CF                        mov rcx, rdi
0078F33D  E8 2E 35 3F 00                  call 0x140b82870
0078F342  8B C3                           mov eax, ebx
0078F344  EB 05                           jmp 0x14078f34b
0078F346  B8 0D 00 00 C0                  mov eax, 0xc000000d
0078F34B  48 8B 8D B0 05 00 00            mov rcx, qword ptr [rbp + 0x5b0]
0078F352  48 33 CC                        xor rcx, rsp
0078F355  E8 E6 D2 F1 FF                  call 0x1406ac640
0078F35A  48 8B 9C 24 10 07 00 00         mov rbx, qword ptr [rsp + 0x710]
0078F362  48 81 C4 C0 06 00 00            add rsp, 0x6c0
0078F369  41 5F                           pop r15
0078F36B  41 5E                           pop r14
0078F36D  41 5D                           pop r13
0078F36F  41 5C                           pop r12
0078F371  5F                              pop rdi
0078F372  5E                              pop rsi
0078F373  5D                              pop rbp
0078F374  C3                              ret
0078F375  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpGetTokenNamedObjectPath(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m468;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m580;
    unsigned __int64 v_stack_m588;
    unsigned __int64 v_stack_m5D8;
    unsigned __int64 v_stack_m5F8;
    unsigned __int64 v_stack_m638;
    unsigned __int64 v_stack_m650;
    unsigned __int64 v_stack_m660;
    unsigned __int64 v_stack_m668;
    unsigned __int64 v_stack_m670;
    unsigned int v_stack_m674;
    unsigned int v_stack_m678;
    unsigned __int64 v_stack_m680;
    unsigned __int64 v_stack_m688;
    unsigned int v_stack_m690;
    unsigned int v_stack_m698;
    unsigned int v_stack_m69C;
    unsigned int v_stack_m6A0;
    unsigned int v_stack_m6A4;
    unsigned int v_stack_m6A8;
    unsigned int v_stack_m6AC;
    unsigned __int8 v_stack_m6B0;
    unsigned __int64 v_stack_m6B8;
    unsigned int v_stack_m6C0;
    unsigned int v_stack_m6C8;
    unsigned int v_stack_m6D0;
    unsigned __int64 v_stack_m6D8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (0x6C0ULL);
    result = (*(unsigned __int64 *)(v_rip + 6797786)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rsi = 0;
    v_stack_m69C = 0;
    v_stack_m6B8 = 0;
    a2 = 0;
    result = memset(v_stack_m5D8, a2, v_rsi + 80, a4);
    v_stack_m6A8 = 0;
    v_stack_m6A0 = 0;
    a2 = 0;
    result = memset(v_stack_m468, a2, 520, a4);
    a2 = 0;
    result = memset(v_stack_m258, a2, 520, a4);
    a2 = 0;
    result = memset(v_stack_m638, a2, v_rsi + 88, a4);
    v_stack_m670 = 0x40002ULL;
    v_stack_m668 = v_rip + 3595174;
    v_stack_m650 = v_xmm0;
    if (a4 == 0) goto loc_0078F346;
    if (a1 == 0) goto loc_0078F346;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & ((unsigned int)(v_rsi + 1)));
    v_stack_m6B0 = (unsigned __int8)(v_rsi + 1);
    v_stack_m690 = (unsigned int)(result);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & ((unsigned int)(v_rsi + 2)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (8));
    v_stack_m674 = (unsigned int)(v_rsi);
    v_rdi = (unsigned int)(((unsigned int)(a3)) & ((unsigned int)(v_rsi + 4)));
    v_stack_m698 = (unsigned int)(result);
    v_stack_m678 = (unsigned int)(v_rdi);
    *(unsigned __int64 *)(a4) = v_xmm0;
    v_stack_m688 = v_xmm0;
    v_stack_m660 = v_xmm1;
    if (0 == 0) goto loc_0078EE5A;
    v_stack_m6AC = (unsigned int)(v_rsi + 1);
    goto loc_0078EECC;
loc_0078EE5A:
    v_stack_m6D8 = v_stack_m6A8;
    result = NtQueryInformationToken(a1, 29, v_stack_m6AC, (unsigned int)((unsigned int)(v_rsi + 4)));
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m6AC == 0) goto loc_0078EEC7;
    v_stack_m6D8 = v_stack_m6A8;
    result = NtQueryInformationToken(a1, 80 - 49, v_stack_m5D8, 80);
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m5D8 != 0) goto loc_0078EEC7;
    goto loc_0078F308;
loc_0078EEC7:
loc_0078EECC:
    v_stack_m6D8 = v_stack_m6A8;
    result = NtQueryInformationToken(a1, 42, v_stack_m6A4, 4);
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m6A4 == 0) goto loc_0078EF3F;
    v_stack_m6D8 = v_stack_m6A8;
    result = NtQueryInformationToken(a1, (unsigned int)((unsigned int)(v_rsi + 1)), v_stack_m638, 88);
    if (sign_flag) goto loc_0078F308;
    result = RtlConvertSidToUnicodeString(v_stack_m660, v_stack_m638, (unsigned __int8)(v_rsi + 1), 88);
    if (sign_flag) goto loc_0078F308;
loc_0078EF3F:
    v_stack_m6D8 = v_stack_m6A8;
    result = NtQueryInformationToken(a1, 4 + 8, v_stack_m6A0, 4);
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m6AC == 0) goto loc_0078EFA9;
    result = RtlGetAppContainerSidType(v_stack_m5D8, v_stack_m69C, v_stack_m6A0, 4);
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m69C != 2) goto loc_0078F008;
    result = RtlConvertSidToUnicodeString(v_stack_m688, v_stack_m5D8, (unsigned __int8)(v_rsi + 1), 4);
    if (sign_flag) goto loc_0078F308;
loc_0078EFA9:
loc_0078EFAF:
    v_stack_m6D8 = v_stack_m6A8;
    result = NtQueryInformationToken(a1, 44, v_stack_m588, 288);
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m6A4 != 0) goto loc_0078F0E9;
    if (v_stack_m6AC != 0) goto loc_0078F0E9;
    result = RtlGetCurrentServiceSessionId(a1, 44, v_stack_m588, 288);
    if (((unsigned int)((unsigned int)(v_stack_m6A0))) == ((unsigned int)(result))) goto loc_0078F0F1;
    goto loc_0078F0EE;
loc_0078F008:
    result = RtlGetAppContainerParent(260, v_stack_m6B8, v_stack_m588, (unsigned int)(v_stack_m6A0));
    if (sign_flag) goto loc_0078F30D;
    result = RtlConvertSidToUnicodeString(v_stack_m688, v_stack_m6B8, (unsigned __int8)(v_rsi + 1), (unsigned int)(v_stack_m6A0));
    if (sign_flag) goto loc_0078F30D;
    result = RtlSubAuthoritySid(260, 11, (unsigned __int8)(v_rsi + 1), (unsigned int)(v_stack_m6A0));
    result = RtlSubAuthoritySid(260, 10, (unsigned __int8)(v_rsi + 1), (unsigned int)(v_stack_m6A0));
    result = RtlSubAuthoritySid(260, 9, (unsigned __int8)(v_rsi + 1), (unsigned int)(v_stack_m6A0));
    result = RtlSubAuthoritySid(260, 8, (unsigned __int8)(v_rsi + 1), (unsigned int)(v_stack_m6A0));
    v_stack_m6C0 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    v_stack_m6C8 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    v_stack_m6D0 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    v_stack_m6D8 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    result = RtlStringCchPrintfW(v_stack_m258, 260, v_rip + 3630380, v_stack_m680);
    if (sign_flag) goto loc_0078F308;
    result = RtlFreeAnsiString(v_stack_m688, 260, v_rip + 3630380, v_stack_m680);
    result = RtlInitUnicodeString(v_stack_m688, v_stack_m258, v_rip + 3630380, v_stack_m680);
    v_stack_m6B0 = 0;
    goto loc_0078EFAF;
loc_0078F0E9:
loc_0078F0EE:
    v_r15 = 0;
loc_0078F0F1:
    if (v_stack_m690 != 0) goto loc_0078F146;
    if (0 != 0) goto loc_0078F13D;
    a3 = v_rip + 3630166;
    if (v_stack_m6AC == 0) { a3 = v_rip + 3630445; }
    v_stack_m6D0 = a3;
    v_stack_m6D8 = (unsigned int)((unsigned int)(v_stack_m6A0));
    result = RtlStringCchPrintfW(v_stack_m468, 260, v_rip + 3630390, v_rip + 3594746);
    goto loc_0078F18D;
loc_0078F13D:
    goto loc_0078F188;
loc_0078F146:
    if ((unsigned int)((unsigned int)(v_stack_m678)) != 0) goto loc_0078F17A;
    result = v_rip + 3630228;
    if (v_stack_m6AC == ((unsigned int)((unsigned int)(v_stack_m678)))) { result = v_rip + 3594619; }
    v_stack_m6D8 = result;
    result = RtlStringCchPrintfW(v_stack_m468, 260, v_rip + 3630793, v_rip + 3594746);
    goto loc_0078F18D;
loc_0078F17A:
loc_0078F188:
    result = RtlStringCchCopyW(v_stack_m468, 260, v_rip + 3630063, v_rip + 3594746);
loc_0078F18D:
    if (sign_flag) goto loc_0078F308;
    result = RtlStringCbLengthW(v_stack_m468, 520, v_stack_m690, v_rip + 3594746);
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m6A4 == 0) goto loc_0078F1DB;
    if ((unsigned int)((unsigned int)(v_stack_m674)) != 0) goto loc_0078F1DB;
    v_rbx = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m674) + 2))) + (v_stack_m690);
    v_rbx = (v_rbx) + (v_stack_m660);
    goto loc_0078F1E5;
loc_0078F1DB:
loc_0078F1E5:
    v_rbx = v_stack_m690;
    if (v_stack_m6AC != 0) {
        a1 = v_stack_m688;
        result = 2;
        v_rbx = (v_stack_m690) + (result);
        v_rbx = (v_rbx) + (a1);
    }
    if (v_stack_m580 == 0) goto loc_0078F224;
    if ((unsigned int)((unsigned int)(v_stack_m698)) == 0) {
        a2 = v_stack_m588;
        a1 = v_stack_m650;
        result = RtlInitUnicodeString(a1, a2, v_stack_m690, v_rip + 3594746);
        a1 = v_stack_m650;
        result = 2;
        v_rbx = (v_rbx) + (result);
        v_rbx = (v_rbx) + (a1);
    }
    v_rbx = (v_rbx) + (2);
    result = ExAllocatePool2(256, v_rbx, (unsigned int)(0x67727453ULL), v_rip + 3594746);
    if (result != 0) goto loc_0078F24C;
    goto loc_0078F308;
loc_0078F24C:
    a2 = 0;
    result = memset(result, a2, (unsigned int)(0xC000009AULL), v_rip + 3594746);
    *(unsigned __int64 *)(a4) = v_xmm0;
    *(unsigned __int16 *)(a4 + 2) = (unsigned __int16)((unsigned int)(0xC000009AULL));
    *(unsigned __int64 *)(a4 + 8) = result;
    result = RtlAppendUnicodeToString(a4, v_stack_m468, (unsigned int)(0xC000009AULL), v_rip + 3594746);
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m6A4 == 0) goto loc_0078F2B1;
    if ((unsigned int)((unsigned int)(v_stack_m674)) != 0) goto loc_0078F2B1;
    result = RtlAppendUnicodeStringToString(a4, v_stack_m670, (unsigned int)(0xC000009AULL), v_rip + 3594746);
    if (sign_flag) goto loc_0078F308;
    result = RtlAppendUnicodeStringToString(a4, v_stack_m660, (unsigned int)(0xC000009AULL), v_rip + 3594746);
    if (sign_flag) goto loc_0078F308;
loc_0078F2B1:
    if (v_stack_m6AC == 0) goto loc_0078F2DD;
    result = RtlAppendUnicodeStringToString(a4, v_stack_m670, (unsigned int)(0xC000009AULL), v_rip + 3594746);
    if (sign_flag) goto loc_0078F308;
    result = RtlAppendUnicodeStringToString(a4, v_stack_m688, (unsigned int)(0xC000009AULL), v_rip + 3594746);
    if (sign_flag) goto loc_0078F308;
loc_0078F2DD:
    if (v_stack_m580 == 0) goto loc_0078F308;
    if ((unsigned int)((unsigned int)(v_stack_m698)) != 0) goto loc_0078F308;
    result = RtlAppendUnicodeStringToString(a4, v_stack_m670, (unsigned int)(0xC000009AULL), v_rip + 3594746);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        a2 = v_stack_m650;
        a1 = a4;
        result = RtlAppendUnicodeStringToString(a1, a2, (unsigned int)(0xC000009AULL), v_rip + 3594746);
        v_rbx = (unsigned int)(result);
    }
loc_0078F30D:
    result = RtlFreeAnsiString(v_stack_m660, a2, (unsigned int)(0xC000009AULL), v_rip + 3594746);
    if (sign_flag) {
        a1 = a4;
        result = RtlFreeAnsiString(a1, a2, (unsigned int)(0xC000009AULL), v_rip + 3594746);
    }
    if (v_stack_m6B0 != 0) {
        a1 = v_stack_m688;
        result = RtlFreeAnsiString(a1, a2, (unsigned int)(0xC000009AULL), v_rip + 3594746);
    }
    if (v_stack_m6B8 != 0) {
        a2 = 0;
        a1 = v_stack_m6B8;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0xC000009AULL), v_rip + 3594746);
    }
    goto loc_0078F34B;
loc_0078F346:
loc_0078F34B:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(0xC000009AULL), v_rip + 3594746);
    v_rsp = (v_rsp) + (0x6C0ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpGetTokenNamedObjectPath(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m258;
    uint64_t v_stack_m468;
    uint64_t v_stack_m48;
    uint8_t v_stack_m580;
    uint64_t v_stack_m588;
    uint64_t v_stack_m5D8;
    uint64_t v_stack_m5F8;
    uint64_t v_stack_m638;
    uint64_t v_stack_m650;
    uint64_t v_stack_m660;
    uint64_t v_stack_m668;
    uint64_t v_stack_m670;
    uint32_t v_stack_m674;
    uint32_t v_stack_m678;
    uint64_t v_stack_m680;
    uint64_t v_stack_m688;
    uint32_t v_stack_m690;
    uint32_t v_stack_m698;
    uint32_t v_stack_m69C;
    uint32_t v_stack_m6A0;
    uint32_t v_stack_m6A4;
    uint32_t v_stack_m6A8;
    uint32_t v_stack_m6AC;
    uint8_t v_stack_m6B0;
    uint64_t v_stack_m6B8;
    uint32_t v_stack_m6C0;
    uint32_t v_stack_m6C8;
    uint32_t v_stack_m6D0;
    uint64_t v_stack_m6D8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (0x6C0ULL);
    result = (*(uint64_t *)(v_rip + 0x67B9DA)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rsi = 0;
    v_stack_m69C = 0;
    v_stack_m6B8 = 0;
    Arg2 = 0;
    result = memset(v_stack_m5D8, Arg2, local_rsi + 80, Arg4);
    v_stack_m6A8 = 0;
    v_stack_m6A0 = 0;
    Arg2 = 0;
    result = memset(v_stack_m468, Arg2, 520, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m258, Arg2, 520, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m638, Arg2, local_rsi + 88, Arg4);
    v_stack_m670 = 0x40002ULL;
    v_stack_m668 = v_rip + 3595174;
    v_stack_m650 = v_xmm0;
    if (Arg4 == 0) goto loc_0078F346;
    if (Arg1 == 0) goto loc_0078F346;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & ((uint32_t)(local_rsi + 1)));
    v_stack_m6B0 = (uint8_t)(local_rsi + 1);
    v_stack_m690 = (uint32_t)(result);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & ((uint32_t)(local_rsi + 2)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (8));
    v_stack_m674 = (uint32_t)(local_rsi);
    local_rdi = (uint32_t)(((uint32_t)(Arg3)) & ((uint32_t)(local_rsi + 4)));
    v_stack_m698 = (uint32_t)(result);
    v_stack_m678 = (uint32_t)(local_rdi);
    *(uint64_t *)(Arg4) = v_xmm0;
    v_stack_m688 = v_xmm0;
    v_stack_m660 = v_xmm1;
    if (0 == 0) goto loc_0078EE5A;
    v_stack_m6AC = (uint32_t)(local_rsi + 1);
    goto loc_0078EECC;
loc_0078EE5A:
    v_stack_m6D8 = v_stack_m6A8;
    result = NtQueryInformationToken(Arg1, 29, v_stack_m6AC, (uint32_t)((uint32_t)(local_rsi + 4)));
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m6AC == 0) goto loc_0078EEC7;
    v_stack_m6D8 = v_stack_m6A8;
    result = NtQueryInformationToken(Arg1, 80 - 49, v_stack_m5D8, 80);
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m5D8 != 0) goto loc_0078EEC7;
    goto loc_0078F308;
loc_0078EEC7:
loc_0078EECC:
    v_stack_m6D8 = v_stack_m6A8;
    result = NtQueryInformationToken(Arg1, 42, v_stack_m6A4, 4);
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m6A4 == 0) goto loc_0078EF3F;
    v_stack_m6D8 = v_stack_m6A8;
    result = NtQueryInformationToken(Arg1, (uint32_t)((uint32_t)(local_rsi + 1)), v_stack_m638, 88);
    if (sign_flag) goto loc_0078F308;
    result = RtlConvertSidToUnicodeString(v_stack_m660, v_stack_m638, (uint8_t)(local_rsi + 1), 88);
    if (sign_flag) goto loc_0078F308;
loc_0078EF3F:
    v_stack_m6D8 = v_stack_m6A8;
    result = NtQueryInformationToken(Arg1, 4 + 8, v_stack_m6A0, 4);
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m6AC == 0) goto loc_0078EFA9;
    result = RtlGetAppContainerSidType(v_stack_m5D8, v_stack_m69C, v_stack_m6A0, 4);
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m69C != 2) goto loc_0078F008;
    result = RtlConvertSidToUnicodeString(v_stack_m688, v_stack_m5D8, (uint8_t)(local_rsi + 1), 4);
    if (sign_flag) goto loc_0078F308;
loc_0078EFA9:
loc_0078EFAF:
    v_stack_m6D8 = v_stack_m6A8;
    result = NtQueryInformationToken(Arg1, 44, v_stack_m588, 288);
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m6A4 != 0) goto loc_0078F0E9;
    if (v_stack_m6AC != 0) goto loc_0078F0E9;
    result = RtlGetCurrentServiceSessionId(Arg1, 44, v_stack_m588, 288);
    if (((uint32_t)((uint32_t)(v_stack_m6A0))) == ((uint32_t)(result))) goto loc_0078F0F1;
    goto loc_0078F0EE;
loc_0078F008:
    result = RtlGetAppContainerParent(260, v_stack_m6B8, v_stack_m588, (uint32_t)(v_stack_m6A0));
    if (sign_flag) goto loc_0078F30D;
    result = RtlConvertSidToUnicodeString(v_stack_m688, v_stack_m6B8, (uint8_t)(local_rsi + 1), (uint32_t)(v_stack_m6A0));
    if (sign_flag) goto loc_0078F30D;
    result = RtlSubAuthoritySid(260, 11, (uint8_t)(local_rsi + 1), (uint32_t)(v_stack_m6A0));
    result = RtlSubAuthoritySid(260, 10, (uint8_t)(local_rsi + 1), (uint32_t)(v_stack_m6A0));
    result = RtlSubAuthoritySid(260, 9, (uint8_t)(local_rsi + 1), (uint32_t)(v_stack_m6A0));
    result = RtlSubAuthoritySid(260, 8, (uint8_t)(local_rsi + 1), (uint32_t)(v_stack_m6A0));
    v_stack_m6C0 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    v_stack_m6C8 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    v_stack_m6D0 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    v_stack_m6D8 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    result = RtlStringCchPrintfW(v_stack_m258, 260, v_rip + 3630380, v_stack_m680);
    if (sign_flag) goto loc_0078F308;
    result = RtlFreeAnsiString(v_stack_m688, 260, v_rip + 3630380, v_stack_m680);
    result = RtlInitUnicodeString(v_stack_m688, v_stack_m258, v_rip + 3630380, v_stack_m680);
    v_stack_m6B0 = 0;
    goto loc_0078EFAF;
loc_0078F0E9:
loc_0078F0EE:
    local_r15 = 0;
loc_0078F0F1:
    if (v_stack_m690 != 0) goto loc_0078F146;
    if (0 != 0) goto loc_0078F13D;
    Arg3 = v_rip + 3630166;
    if (v_stack_m6AC == 0) { Arg3 = v_rip + 3630445; }
    v_stack_m6D0 = Arg3;
    v_stack_m6D8 = (uint32_t)((uint32_t)(v_stack_m6A0));
    result = RtlStringCchPrintfW(v_stack_m468, 260, v_rip + 3630390, v_rip + 3594746);
    goto loc_0078F18D;
loc_0078F13D:
    goto loc_0078F188;
loc_0078F146:
    if ((uint32_t)((uint32_t)(v_stack_m678)) != 0) goto loc_0078F17A;
    result = v_rip + 3630228;
    if (v_stack_m6AC == ((uint32_t)((uint32_t)(v_stack_m678)))) { result = v_rip + 3594619; }
    v_stack_m6D8 = result;
    result = RtlStringCchPrintfW(v_stack_m468, 260, v_rip + 3630793, v_rip + 3594746);
    goto loc_0078F18D;
loc_0078F17A:
loc_0078F188:
    result = RtlStringCchCopyW(v_stack_m468, 260, v_rip + 3630063, v_rip + 3594746);
loc_0078F18D:
    if (sign_flag) goto loc_0078F308;
    result = RtlStringCbLengthW(v_stack_m468, 520, v_stack_m690, v_rip + 3594746);
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m6A4 == 0) goto loc_0078F1DB;
    if ((uint32_t)((uint32_t)(v_stack_m674)) != 0) goto loc_0078F1DB;
    local_rbx = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m674) + 2))) + (v_stack_m690);
    local_rbx = (local_rbx) + (v_stack_m660);
    goto loc_0078F1E5;
loc_0078F1DB:
loc_0078F1E5:
    local_rbx = v_stack_m690;
    if (v_stack_m6AC != 0) {
        Arg1 = v_stack_m688;
        result = 2;
        local_rbx = (v_stack_m690) + (result);
        local_rbx = (local_rbx) + (Arg1);
    }
    if (v_stack_m580 == 0) goto loc_0078F224;
    if ((uint32_t)((uint32_t)(v_stack_m698)) == 0) {
        Arg2 = v_stack_m588;
        Arg1 = v_stack_m650;
        result = RtlInitUnicodeString(Arg1, Arg2, v_stack_m690, v_rip + 3594746);
        Arg1 = v_stack_m650;
        result = 2;
        local_rbx = (local_rbx) + (result);
        local_rbx = (local_rbx) + (Arg1);
    }
    local_rbx = (local_rbx) + (2);
    result = ExAllocatePool2(256, local_rbx, (uint32_t)(0x67727453ULL), v_rip + 3594746);
    if (result != 0) goto loc_0078F24C;
    goto loc_0078F308;
loc_0078F24C:
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(0xC000009AULL), v_rip + 3594746);
    *(uint64_t *)(Arg4) = v_xmm0;
    *(uint16_t *)(Arg4 + 0x2) = (uint16_t)((uint32_t)(0xC000009AULL));
    *(uint64_t *)(Arg4 + 0x8) = result;
    result = RtlAppendUnicodeToString(Arg4, v_stack_m468, (uint32_t)(0xC000009AULL), v_rip + 3594746);
    if (sign_flag) goto loc_0078F308;
    if (v_stack_m6A4 == 0) goto loc_0078F2B1;
    if ((uint32_t)((uint32_t)(v_stack_m674)) != 0) goto loc_0078F2B1;
    result = RtlAppendUnicodeStringToString(Arg4, v_stack_m670, (uint32_t)(0xC000009AULL), v_rip + 3594746);
    if (sign_flag) goto loc_0078F308;
    result = RtlAppendUnicodeStringToString(Arg4, v_stack_m660, (uint32_t)(0xC000009AULL), v_rip + 3594746);
    if (sign_flag) goto loc_0078F308;
loc_0078F2B1:
    if (v_stack_m6AC == 0) goto loc_0078F2DD;
    result = RtlAppendUnicodeStringToString(Arg4, v_stack_m670, (uint32_t)(0xC000009AULL), v_rip + 3594746);
    if (sign_flag) goto loc_0078F308;
    result = RtlAppendUnicodeStringToString(Arg4, v_stack_m688, (uint32_t)(0xC000009AULL), v_rip + 3594746);
    if (sign_flag) goto loc_0078F308;
loc_0078F2DD:
    if (v_stack_m580 == 0) goto loc_0078F308;
    if ((uint32_t)((uint32_t)(v_stack_m698)) != 0) goto loc_0078F308;
    result = RtlAppendUnicodeStringToString(Arg4, v_stack_m670, (uint32_t)(0xC000009AULL), v_rip + 3594746);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        Arg2 = v_stack_m650;
        Arg1 = Arg4;
        result = RtlAppendUnicodeStringToString(Arg1, Arg2, (uint32_t)(0xC000009AULL), v_rip + 3594746);
        local_rbx = (uint32_t)(result);
    }
loc_0078F30D:
    result = RtlFreeAnsiString(v_stack_m660, Arg2, (uint32_t)(0xC000009AULL), v_rip + 3594746);
    if (sign_flag) {
        Arg1 = Arg4;
        result = RtlFreeAnsiString(Arg1, Arg2, (uint32_t)(0xC000009AULL), v_rip + 3594746);
    }
    if (v_stack_m6B0 != 0) {
        Arg1 = v_stack_m688;
        result = RtlFreeAnsiString(Arg1, Arg2, (uint32_t)(0xC000009AULL), v_rip + 3594746);
    }
    if (v_stack_m6B8 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m6B8;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0xC000009AULL), v_rip + 3594746);
    }
    goto loc_0078F34B;
loc_0078F346:
loc_0078F34B:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(0xC000009AULL), v_rip + 3594746);
    local_rsp = (local_rsp) + (0x6C0ULL);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0078ED40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
