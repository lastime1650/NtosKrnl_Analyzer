# AdtpBuildAccessesString

- RVA: `0x00A8898C`–`0x00A88E9F` (길이 `1,299` bytes)
- VA: `0x0000000140A8898C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B8144`
- 디코드: `322`개 명령, `1,299/1,299` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x00A88A57` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A88AED` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A88B53` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00A88B82` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x00A88BCA` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A88BCF` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A88C4C` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x00A88C5F` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x00A88C6C` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x00A88C83` → [RtlIntegerToUnicodeString](../91/RtlIntegerToUnicodeString_function_0091D3E0.md) (function, `0x0091D3E0`)
- `0x00A88CA1` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x00A88CAF` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x00A88CBC` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x00A88D0B` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A88D1B` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x00A88D36` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A88D61` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x00A88D9B` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00A88DDB` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x00A88DEE` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x00A88DFB` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x00A88E60` → [RtlEqualUnicodeString](../93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)

### Direct callers
- [AdtpBuildAccessReasonAuditStringInternal](../../text/40/AdtpBuildAccessReasonAuditStringInternal_function_0040F344.md) at `0x0040F5BC`
- [AdtpPackageParameters](../../text/45/AdtpPackageParameters_function_00459964.md) at `0x0045A114`
- [AdtpBuildStagingReasonAuditStringInternal](../../text/69/AdtpBuildStagingReasonAuditStringInternal_function_0069DA44.md) at `0x0069DB1B`
- [AdtpBuildObjectTypeStrings](../AD/AdtpBuildObjectTypeStrings_function_00AD0B38.md) at `0x00AD0C25`

### Static image references
- `0x00A889A8` → RVA `0x00E0A740` (`.data`; read)
- `0x00A88A28` → RVA `0x0001BEC8` (`.rdata`; read)
- `0x00A88A92` → RVA `0x0001BEEC` (`.rdata`; read)
- `0x00A88A99` → RVA `0x00EF0780` (`.data`; read)
- `0x00A88B42` → RVA `0x00EF0600` (`.data`; read)
- `0x00A88B5B` → RVA `0x00EF07F0` (`.data`; read)
- `0x00A88BA8` → RVA `0x00EF07F0` (`.data`; write)
- `0x00A88C1A` → RVA `0x0001BED8` (`.rdata`; read)
- `0x00A88C40` → RVA `0x000134F8` (`.rdata`; read)
- `0x00A88CDD` → RVA `0x0001E0B0` (`.rdata`; read)
- `0x00A88CFD` → RVA `0x0001BF2C` (`.rdata`; read)
- `0x00A88D2B` → RVA `0x0001BEF8` (`.rdata`; read)
- `0x00A88D91` → RVA `0x0001A748` (`.rdata`; read)
- `0x00A88DB9` → RVA `0x00041AAC` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00A88A57` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A88AED` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A88B53` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00A88BCA` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A88BCF` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A88C4C` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x00A88C5F` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`PAGE` → `.text`)
  - `0x00A88C6C` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x00A88CA1` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x00A88CAF` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`PAGE` → `.text`)
  - `0x00A88CBC` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x00A88D0B` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A88D36` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A88D9B` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00A88DDB` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x00A88DEE` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`PAGE` → `.text`)
  - `0x00A88DFB` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00A88DA9` → [sub_00B45196](../B4/Unknown_function_00B45196.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A8898C  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00A88991  55                              push rbp
00A88992  56                              push rsi
00A88993  57                              push rdi
00A88994  41 54                           push r12
00A88996  41 55                           push r13
00A88998  41 56                           push r14
00A8899A  41 57                           push r15
00A8899C  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
00A889A1  48 81 EC B0 00 00 00            sub rsp, 0xb0
00A889A8  48 8B 05 91 1D 38 00            mov rax, qword ptr [rip + 0x381d91]
00A889AF  48 33 C4                        xor rax, rsp
00A889B2  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00A889B6  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
00A889BA  45 8B E0                        mov r12d, r8d
00A889BD  48 8B 7D 6F                     mov rdi, qword ptr [rbp + 0x6f]
00A889C1  0F 57 C0                        xorps xmm0, xmm0
00A889C4  4C 8B 5D 77                     mov r11, qword ptr [rbp + 0x77]
00A889C8  0F 57 C9                        xorps xmm1, xmm1
00A889CB  4C 8B 55 7F                     mov r10, qword ptr [rbp + 0x7f]
00A889CF  48 8B B5 87 00 00 00            mov rsi, qword ptr [rbp + 0x87]
00A889D6  48 89 55 B7                     mov qword ptr [rbp - 0x49], rdx
00A889DA  33 D2                           xor edx, edx
00A889DC  44 89 45 87                     mov dword ptr [rbp - 0x79], r8d
00A889E0  44 8B EA                        mov r13d, edx
00A889E3  48 89 4D AF                     mov qword ptr [rbp - 0x51], rcx
00A889E7  44 8B C2                        mov r8d, edx
00A889EA  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00A889EE  44 8B F2                        mov r14d, edx
00A889F1  48 89 7D 97                     mov qword ptr [rbp - 0x69], rdi
00A889F5  48 89 55 9F                     mov qword ptr [rbp - 0x61], rdx
00A889F9  48 89 55 BF                     mov qword ptr [rbp - 0x41], rdx
00A889FD  89 54 24 24                     mov dword ptr [rsp + 0x24], edx
00A88A01  0F 11 45 D7                     movups xmmword ptr [rbp - 0x29], xmm0
00A88A05  0F 11 4D E7                     movups xmmword ptr [rbp - 0x19], xmm1
00A88A09  45 85 E4                        test r12d, r12d
00A88A0C  0F 84 C2 02 00 00               je 0x140a88cd4
00A88A12  41 8B CC                        mov ecx, r12d
00A88A15  8D 41 FF                        lea eax, [rcx - 1]
00A88A18  41 FF C0                        inc r8d
00A88A1B  23 C8                           and ecx, eax
00A88A1D  75 F6                           jne 0x140a88a15
00A88A1F  45 85 C9                        test r9d, r9d
00A88A22  0F 85 7D 03 00 00               jne 0x140a88da5
00A88A28  4C 8D 3D 99 34 59 FF            lea r15, [rip - 0xa6cb67]
00A88A2F  4C 89 7D 8F                     mov qword ptr [rbp - 0x71], r15
00A88A33  43 8D 04 40                     lea eax, [r8 + r8*2]
00A88A37  8D 1C C5 01 00 00 00            lea ebx, [rax*8 + 1]
00A88A3E  4D 85 DB                        test r11, r11
00A88A41  0F 85 C7 00 00 00               jne 0x140a88b0e
00A88A47  8B D3                           mov edx, ebx
00A88A49  B9 00 01 00 00                  mov ecx, 0x100
00A88A4E  48 03 D2                        add rdx, rdx
00A88A51  41 B8 53 65 41 6B               mov r8d, 0x6b416553
00A88A57  E8 94 96 0F 00                  call 0x140b820f0
00A88A5C  33 D2                           xor edx, edx
00A88A5E  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
00A88A62  48 85 C0                        test rax, rax
00A88A65  0F 84 5A 03 00 00               je 0x140a88dc5
00A88A6B  C6 06 01                        mov byte ptr [rsi], 1
00A88A6E  66 03 DB                        add bx, bx
00A88A71  66 89 54 24 20                  mov word ptr [rsp + 0x20], dx
00A88A76  66 89 5C 24 22                  mov word ptr [rsp + 0x22], bx
00A88A7B  BB 05 00 00 00                  mov ebx, 5
00A88A80  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A88A85  41 F7 C4 00 00 1F 00            test r12d, 0x1f0000
00A88A8C  0F 85 86 01 00 00               jne 0x140a88c18
00A88A92  48 8D 35 53 34 59 FF            lea rsi, [rip - 0xa6cbad]
00A88A99  48 8D 3D E0 7C 46 00            lea rdi, [rip + 0x467ce0]
00A88AA0  44 85 26                        test dword ptr [rsi], r12d
00A88AA3  0F 85 26 03 00 00               jne 0x140a88dcf
00A88AA9  FF C3                           inc ebx
00A88AAB  48 83 C6 04                     add rsi, 4
00A88AAF  83 FB 07                        cmp ebx, 7
00A88AB2  72 EC                           jb 0x140a88aa0
00A88AB4  48 8B 7D 97                     mov rdi, qword ptr [rbp - 0x69]
00A88AB8  33 C9                           xor ecx, ecx
00A88ABA  66 45 85 E4                     test r12w, r12w
00A88ABE  75 79                           jne 0x140a88b39
00A88AC0  45 85 ED                        test r13d, r13d
00A88AC3  78 1E                           js 0x140a88ae3
00A88AC5  48 85 FF                        test rdi, rdi
00A88AC8  0F 84 BF 03 00 00               je 0x140a88e8d
00A88ACE  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
00A88AD2  48 89 07                        mov qword ptr [rdi], rax
00A88AD5  0F B7 44 24 20                  movzx eax, word ptr [rsp + 0x20]
00A88ADA  83 C0 02                        add eax, 2
00A88ADD  89 4F 0C                        mov dword ptr [rdi + 0xc], ecx
00A88AE0  89 47 08                        mov dword ptr [rdi + 8], eax
00A88AE3  41 8B C5                        mov eax, r13d
00A88AE6  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
00A88AEA  48 33 CC                        xor rcx, rsp
00A88AED  E8 4E 3B C2 FF                  call 0x1406ac640
00A88AF2  48 8B 9C 24 00 01 00 00         mov rbx, qword ptr [rsp + 0x100]
00A88AFA  48 81 C4 B0 00 00 00            add rsp, 0xb0
00A88B01  41 5F                           pop r15
00A88B03  41 5E                           pop r14
00A88B05  41 5D                           pop r13
00A88B07  41 5C                           pop r12
00A88B09  5F                              pop rdi
00A88B0A  5E                              pop rsi
00A88B0B  5D                              pop rbp
00A88B0C  C3                              ret
00A88B0D  CC                              int3
00A88B0E  4D 85 D2                        test r10, r10
00A88B11  0F 84 30 FF FF FF               je 0x140a88a47
00A88B17  41 8B 02                        mov eax, dword ptr [r10]
00A88B1A  8D 0C 18                        lea ecx, [rax + rbx]
00A88B1D  81 F9 00 04 00 00               cmp ecx, 0x400
00A88B23  0F 83 1E FF FF FF               jae 0x140a88a47
00A88B29  49 8D 04 43                     lea rax, [r11 + rax*2]
00A88B2D  41 89 0A                        mov dword ptr [r10], ecx
00A88B30  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
00A88B34  E9 35 FF FF FF                  jmp 0x140a88a6e
00A88B39  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A88B42  48 8D 0D B7 7A 46 00            lea rcx, [rip + 0x467ab7]
00A88B49  B2 01                           mov dl, 1
00A88B4B  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00A88B52  90                              nop
00A88B53  E8 C8 C2 78 FF                  call 0x140214e20
00A88B58  40 32 F6                        xor sil, sil
00A88B5B  48 8D 1D 8E 7C 46 00            lea rbx, [rip + 0x467c8e]
00A88B62  48 83 3D 86 7C 46 00 00         cmp qword ptr [rip + 0x467c86], 0
00A88B6A  74 57                           je 0x140a88bc3
00A88B6C  48 8B 7D AF                     mov rdi, qword ptr [rbp - 0x51]
00A88B70  40 84 F6                        test sil, sil
00A88B73  75 40                           jne 0x140a88bb5
00A88B75  48 8B 0B                        mov rcx, qword ptr [rbx]
00A88B78  41 B0 01                        mov r8b, 1
00A88B7B  48 83 C1 08                     add rcx, 8
00A88B7F  48 8B D7                        mov rdx, rdi
00A88B82  E8 99 9E EA FF                  call 0x140932a20
00A88B87  48 8B 0B                        mov rcx, qword ptr [rbx]
00A88B8A  84 C0                           test al, al
00A88B8C  0F 84 81 00 00 00               je 0x140a88c13
00A88B92  48 8B 01                        mov rax, qword ptr [rcx]
00A88B95  40 B6 01                        mov sil, 1
00A88B98  48 89 03                        mov qword ptr [rbx], rax
00A88B9B  4C 8B F1                        mov r14, rcx
00A88B9E  48 8B 05 4B 7C 46 00            mov rax, qword ptr [rip + 0x467c4b]
00A88BA5  48 89 01                        mov qword ptr [rcx], rax
00A88BA8  48 89 0D 41 7C 46 00            mov qword ptr [rip + 0x467c41], rcx
00A88BAF  48 83 3B 00                     cmp qword ptr [rbx], 0
00A88BB3  75 BB                           jne 0x140a88b70
00A88BB5  48 8B 7D 97                     mov rdi, qword ptr [rbp - 0x69]
00A88BB9  40 80 FE 01                     cmp sil, 1
00A88BBD  0F 84 33 01 00 00               je 0x140a88cf6
00A88BC3  48 8D 0D 36 7A 46 00            lea rcx, [rip + 0x467a36]
00A88BCA  E8 41 6E 7D FF                  call 0x14025fa10
00A88BCF  E8 DC 4C 7D FF                  call 0x14025d8b0
00A88BD4  33 C9                           xor ecx, ecx
00A88BD6  40 84 F6                        test sil, sil
00A88BD9  0F 84 EA 00 00 00               je 0x140a88cc9
00A88BDF  4C 8B 75 BF                     mov r14, qword ptr [rbp - 0x41]
00A88BE3  45 8B 76 18                     mov r14d, dword ptr [r14 + 0x18]
00A88BE7  48 8D 45 E7                     lea rax, [rbp - 0x19]
00A88BEB  48 C7 45 9F 00 00 14 00         mov qword ptr [rbp - 0x61], 0x140000
00A88BF3  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
00A88BF7  BE 01 00 00 00                  mov esi, 1
00A88BFC  8B D9                           mov ebx, ecx
00A88BFE  41 85 F4                        test r12d, esi
00A88C01  75 73                           jne 0x140a88c76
00A88C03  33 C9                           xor ecx, ecx
00A88C05  FF C3                           inc ebx
00A88C07  03 F6                           add esi, esi
00A88C09  83 FB 10                        cmp ebx, 0x10
00A88C0C  72 F0                           jb 0x140a88bfe
00A88C0E  E9 AD FE FF FF                  jmp 0x140a88ac0
00A88C13  48 8B D9                        mov rbx, rcx
00A88C16  EB 97                           jmp 0x140a88baf
00A88C18  8B F2                           mov esi, edx
00A88C1A  4C 8D 35 B7 32 59 FF            lea r14, [rip - 0xa6cd49]
00A88C21  48 8D 3D 58 7B 46 00            lea rdi, [rip + 0x467b58]
00A88C28  45 85 26                        test dword ptr [r14], r12d
00A88C2B  75 13                           jne 0x140a88c40
00A88C2D  FF C6                           inc esi
00A88C2F  49 83 C6 04                     add r14, 4
00A88C33  3B F3                           cmp esi, ebx
00A88C35  72 F1                           jb 0x140a88c28
00A88C37  4C 8B 75 9F                     mov r14, qword ptr [rbp - 0x61]
00A88C3B  E9 52 FE FF FF                  jmp 0x140a88a92
00A88C40  48 8D 15 B1 A8 58 FF            lea rdx, [rip - 0xa7574f]
00A88C47  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A88C4C  E8 3F 6D 98 FF                  call 0x14040f990
00A88C51  8B D6                           mov edx, esi
00A88C53  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A88C58  48 C1 E2 04                     shl rdx, 4
00A88C5C  48 03 D7                        add rdx, rdi
00A88C5F  E8 EC 6D 98 FF                  call 0x14040fa50
00A88C64  49 8B D7                        mov rdx, r15
00A88C67  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A88C6C  E8 1F 6D 98 FF                  call 0x14040f990
00A88C71  44 8B E8                        mov r13d, eax
00A88C74  EB B7                           jmp 0x140a88c2d
00A88C76  42 8D 0C 33                     lea ecx, [rbx + r14]
00A88C7A  BA 0A 00 00 00                  mov edx, 0xa
00A88C7F  4C 8D 45 9F                     lea r8, [rbp - 0x61]
00A88C83  E8 58 47 E9 FF                  call 0x14091d3e0
00A88C88  33 C9                           xor ecx, ecx
00A88C8A  44 8B E8                        mov r13d, eax
00A88C8D  85 C0                           test eax, eax
00A88C8F  0F 88 70 FF FF FF               js 0x140a88c05
00A88C95  48 8D 15 5C A8 58 FF            lea rdx, [rip - 0xa757a4]
00A88C9C  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A88CA1  E8 EA 6C 98 FF                  call 0x14040f990
00A88CA6  48 8D 55 9F                     lea rdx, [rbp - 0x61]
00A88CAA  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A88CAF  E8 9C 6D 98 FF                  call 0x14040fa50
00A88CB4  49 8B D7                        mov rdx, r15
00A88CB7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A88CBC  E8 CF 6C 98 FF                  call 0x14040f990
00A88CC1  44 8B E8                        mov r13d, eax
00A88CC4  E9 3A FF FF FF                  jmp 0x140a88c03
00A88CC9  41 BE 10 06 00 00               mov r14d, 0x610
00A88CCF  E9 13 FF FF FF                  jmp 0x140a88be7
00A88CD4  48 85 FF                        test rdi, rdi
00A88CD7  0F 84 AB 00 00 00               je 0x140a88d88
00A88CDD  48 8D 05 CC 53 59 FF            lea rax, [rip - 0xa6ac34]
00A88CE4  48 C7 47 08 04 00 00 00         mov qword ptr [rdi + 8], 4
00A88CEC  48 89 07                        mov qword ptr [rdi], rax
00A88CEF  33 C0                           xor eax, eax
00A88CF1  E9 F0 FD FF FF                  jmp 0x140a88ae6
00A88CF6  4D 8D 66 18                     lea r12, [r14 + 0x18]
00A88CFA  40 32 F6                        xor sil, sil
00A88CFD  48 8D 15 28 32 59 FF            lea rdx, [rip - 0xa6cdd8]
00A88D04  49 8B DC                        mov rbx, r12
00A88D07  48 8D 4D D7                     lea rcx, [rbp - 0x29]
00A88D0B  E8 70 1A 9A FF                  call 0x14042a780
00A88D10  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
00A88D14  48 8D 55 D7                     lea rdx, [rbp - 0x29]
00A88D18  41 B0 01                        mov r8b, 1
00A88D1B  E8 00 9D EA FF                  call 0x140932a20
00A88D20  84 C0                           test al, al
00A88D22  0F 85 E0 00 00 00               jne 0x140a88e08
00A88D28  45 32 F6                        xor r14b, r14b
00A88D2B  48 8D 15 C6 31 59 FF            lea rdx, [rip - 0xa6ce3a]
00A88D32  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00A88D36  E8 45 1A 9A FF                  call 0x14042a780
00A88D3B  49 83 3C 24 00                  cmp qword ptr [r12], 0
00A88D40  74 3D                           je 0x140a88d7f
00A88D42  4C 8B 7D B7                     mov r15, qword ptr [rbp - 0x49]
00A88D46  40 84 F6                        test sil, sil
00A88D49  75 2C                           jne 0x140a88d77
00A88D4B  45 84 F6                        test r14b, r14b
00A88D4E  0F 85 FE 00 00 00               jne 0x140a88e52
00A88D54  48 8B 0B                        mov rcx, qword ptr [rbx]
00A88D57  41 B0 01                        mov r8b, 1
00A88D5A  48 83 C1 08                     add rcx, 8
00A88D5E  49 8B D7                        mov rdx, r15
00A88D61  E8 BA 9C EA FF                  call 0x140932a20
00A88D66  84 C0                           test al, al
00A88D68  0F 85 FF 00 00 00               jne 0x140a88e6d
00A88D6E  48 8B 1B                        mov rbx, qword ptr [rbx]
00A88D71  48 83 3B 00                     cmp qword ptr [rbx], 0
00A88D75  75 CF                           jne 0x140a88d46
00A88D77  48 8B 7D 97                     mov rdi, qword ptr [rbp - 0x69]
00A88D7B  4C 8B 7D 8F                     mov r15, qword ptr [rbp - 0x71]
00A88D7F  44 8B 65 87                     mov r12d, dword ptr [rbp - 0x79]
00A88D83  E9 3B FE FF FF                  jmp 0x140a88bc3
00A88D88  48 85 C0                        test rax, rax
00A88D8B  0F 84 5E FF FF FF               je 0x140a88cef
00A88D91  48 8D 15 B0 19 59 FF            lea rdx, [rip - 0xa6e650]
00A88D98  48 8B C8                        mov rcx, rax
00A88D9B  E8 E0 19 9A FF                  call 0x14042a780
00A88DA0  E9 4A FF FF FF                  jmp 0x140a88cef
00A88DA5  41 83 E9 01                     sub r9d, 1
00A88DA9  0F 84 E7 C3 0B 00               je 0x140b45196
00A88DAF  41 83 F9 01                     cmp r9d, 1
00A88DB3  0F 85 6F FC FF FF               jne 0x140a88a28
00A88DB9  4C 8D 3D EC 8C 5B FF            lea r15, [rip - 0xa47314]
00A88DC0  E9 6A FC FF FF                  jmp 0x140a88a2f
00A88DC5  B8 17 00 00 C0                  mov eax, 0xc0000017
00A88DCA  E9 17 FD FF FF                  jmp 0x140a88ae6
00A88DCF  48 8D 15 22 A7 58 FF            lea rdx, [rip - 0xa758de]
00A88DD6  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A88DDB  E8 B0 6B 98 FF                  call 0x14040f990
00A88DE0  8B D3                           mov edx, ebx
00A88DE2  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A88DE7  48 C1 E2 04                     shl rdx, 4
00A88DEB  48 03 D7                        add rdx, rdi
00A88DEE  E8 5D 6C 98 FF                  call 0x14040fa50
00A88DF3  49 8B D7                        mov rdx, r15
00A88DF6  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A88DFB  E8 90 6B 98 FF                  call 0x14040f990
00A88E00  44 8B E8                        mov r13d, eax
00A88E03  E9 A1 FC FF FF                  jmp 0x140a88aa9
00A88E08  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
00A88E0C  B9 4E 00 00 00                  mov ecx, 0x4e
00A88E11  66 3B 08                        cmp cx, word ptr [rax]
00A88E14  0F 85 0E FF FF FF               jne 0x140a88d28
00A88E1A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00A88E1E  B9 25 00 00 00                  mov ecx, 0x25
00A88E23  66 3B 08                        cmp cx, word ptr [rax]
00A88E26  0F 85 FC FE FF FF               jne 0x140a88d28
00A88E2C  B9 7B 00 00 00                  mov ecx, 0x7b
00A88E31  66 3B 48 02                     cmp cx, word ptr [rax + 2]
00A88E35  0F 85 ED FE FF FF               jne 0x140a88d28
00A88E3B  B9 7D 00 00 00                  mov ecx, 0x7d
00A88E40  66 3B 48 4C                     cmp cx, word ptr [rax + 0x4c]
00A88E44  0F 85 DE FE FF FF               jne 0x140a88d28
00A88E4A  41 B6 01                        mov r14b, 1
00A88E4D  E9 D9 FE FF FF                  jmp 0x140a88d2b
00A88E52  48 8B 0B                        mov rcx, qword ptr [rbx]
00A88E55  48 8D 55 E7                     lea rdx, [rbp - 0x19]
00A88E59  48 83 C1 08                     add rcx, 8
00A88E5D  41 B0 01                        mov r8b, 1
00A88E60  E8 BB 9B EA FF                  call 0x140932a20
00A88E65  84 C0                           test al, al
00A88E67  0F 84 E7 FE FF FF               je 0x140a88d54
00A88E6D  48 8B 3B                        mov rdi, qword ptr [rbx]
00A88E70  40 B6 01                        mov sil, 1
00A88E73  48 89 7D BF                     mov qword ptr [rbp - 0x41], rdi
00A88E77  48 8B 07                        mov rax, qword ptr [rdi]
00A88E7A  48 89 03                        mov qword ptr [rbx], rax
00A88E7D  49 8B 04 24                     mov rax, qword ptr [r12]
00A88E81  48 89 07                        mov qword ptr [rdi], rax
00A88E84  49 89 3C 24                     mov qword ptr [r12], rdi
00A88E88  E9 E4 FE FF FF                  jmp 0x140a88d71
00A88E8D  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
00A88E91  0F 10 44 24 20                  movups xmm0, xmmword ptr [rsp + 0x20]
00A88E96  F3 0F 7F 00                     movdqu xmmword ptr [rax], xmm0
00A88E9A  E9 44 FC FF FF                  jmp 0x140a88ae3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AdtpBuildAccessesString(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m3F;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned __int16 v_stack_mC6;
    unsigned __int16 v_stack_mC8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 3677585)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m88 = a2;
    a2 = 0;
    v_stack_mB8 = a3;
    v_stack_m90 = a1;
    v_stack_m70 = a5;
    v_stack_mA8 = a6;
    v_stack_mA0 = 0;
    v_stack_m80 = 0;
    v_stack_mC4 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm1;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_00A88CD4;
loc_00A88A15:
    a3 = (unsigned int)((0) + 1);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a3))) - 1)));
    if (condition_is_not_equal) goto loc_00A88A15;
    if (a4 != 0) goto loc_00A88DA5;
loc_00A88A28:
loc_00A88A2F:
    v_stack_mB0 = v_rip - 10931047;
    if (a7 != 0) goto loc_00A88B0E;
loc_00A88A47:
    a2 = ((unsigned int)((unsigned int)(a3 + a3 * 2 * 8 + 1))) + ((unsigned int)((unsigned int)(a3 + a3 * 2 * 8 + 1)));
    result = ExAllocatePool2(256, a2, (unsigned int)(0x6B416553ULL), a4);
    a2 = 0;
    v_stack_m78 = result;
    if (result == 0) goto loc_00A88DC5;
    *(unsigned __int8 *)(a9) = 1;
loc_00A88A6E:
    v_rbx = (unsigned __int16)((a3 + a3 * 2 * 8 + 1) + ((unsigned __int16)(a3 + a3 * 2 * 8 + 1)));
    v_stack_mC8 = 0;
    v_stack_mC6 = (unsigned __int16)(v_rbx);
    v_stack_mC0 = result;
    if ((((unsigned int)((unsigned int)(a3))) & (0x1F0000ULL)) != 0) goto loc_00A88C18;
loc_00A88A92:
loc_00A88AA0:
    if (((*(unsigned int *)(v_rip - 10931117)) & ((unsigned int)((unsigned int)(a3)))) != 0) goto loc_00A88DCF;
loc_00A88AA9:
    v_rbx = (unsigned int)((5) + 1);
    v_rsi = (v_rip - 10931117) + (4);
    if (((unsigned int)(v_rbx)) < 7) goto loc_00A88AA0;
    a1 = 0;
    if ((unsigned __int16)((unsigned int)(a3)) != 0) goto loc_00A88B39;
loc_00A88AC0:
    if (sign_flag) goto loc_00A88AE3;
    if (v_stack_mA8 == 0) goto loc_00A88E8D;
    *(unsigned __int64 *)(v_stack_mA8) = v_stack_m78;
    result = (unsigned int)((v_stack_mC8) + (2));
    *(unsigned int *)(v_stack_mA8 + 12) = 0;
    *(unsigned int *)(v_stack_mA8 + 8) = (unsigned int)(result);
loc_00A88AE3:
loc_00A88AE6:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(0x6B416553ULL), a4);
    v_rsp = (v_rsp) + (176);
    return result;
loc_00A88B0E:
    if (a8 == 0) goto loc_00A88A47;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a8)) + v_stack_p18 * 1)) >= 0x400ULL) goto loc_00A88A47;
    *(unsigned int *)(a8) = (unsigned int)((unsigned int)(*(unsigned int *)(a8)) + v_stack_p18 * 1);
    v_stack_m78 = a7 + (unsigned int)(*(unsigned int *)(a8)) * 2;
    goto loc_00A88A6E;
loc_00A88B39:
    result = ExAcquireResourceExclusiveLite(v_rip + 4618935, 1, (unsigned int)(0x6B416553ULL), a4);
    v_rsi = 0;
    if ((*(unsigned __int64 *)(v_rip + 4619398)) == 0) goto loc_00A88BC3;
loc_00A88B70:
    if (0 != 0) goto loc_00A88BB5;
    a1 = (*(unsigned __int64 *)(v_rip + 4619406)) + (8);
    result = RtlEqualUnicodeString(a1, v_stack_m90, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A88C13;
    *(unsigned __int64 *)(v_rip + 4619406) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4619406));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4619406)) = *(unsigned __int64 *)(v_rip + 4619339);
    *(unsigned __int64 *)(v_rip + 4619329) = *(unsigned __int64 *)(v_rip + 4619406);
loc_00A88BAF:
    if ((*(unsigned __int64 *)(v_rip + 4619406)) != 0) goto loc_00A88B70;
loc_00A88BB5:
    if (1 == 1) goto loc_00A88CF6;
loc_00A88BC3:
    result = ExReleaseResourceLite(v_rip + 4618806, v_stack_m90, 1, a4);
    result = KeLeaveCriticalRegion(v_rip + 4618806, v_stack_m90, 1, a4);
    a1 = 0;
    if (1 == 0) goto loc_00A88CC9;
loc_00A88BE7:
    v_stack_mA0 = 0x140000ULL;
    v_stack_m98 = v_stack_m58;
loc_00A88BFE:
    if ((((unsigned int)((unsigned int)(a3))) & (1)) != 0) goto loc_00A88C76;
loc_00A88C03:
    a1 = 0;
loc_00A88C05:
    v_rbx = (unsigned int)((0) + 1);
    v_rsi = (unsigned int)((1) + (1));
    if (((unsigned int)(v_rbx)) < 16) goto loc_00A88BFE;
    goto loc_00A88AC0;
loc_00A88C13:
    goto loc_00A88BAF;
loc_00A88C18:
loc_00A88C28:
    if (((*(unsigned int *)(v_rip - 10931529)) & ((unsigned int)((unsigned int)(a3)))) != 0) goto loc_00A88C40;
loc_00A88C2D:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m90))) + 1);
    v_r14 = (v_rip - 10931529) + (4);
    if (((unsigned int)(v_rsi)) < 0) goto loc_00A88C28;
    goto loc_00A88A92;
loc_00A88C40:
    result = RtlAppendUnicodeToString(v_stack_p20, v_rip - 10966863, 1, a4);
    a2 = ((unsigned int)((unsigned int)(v_rsi))) << (4);
    a2 = (a2) + (v_rip + 4619096);
    result = RtlAppendUnicodeStringToString(v_stack_p20, a2, 1, a4);
    result = RtlAppendUnicodeToString(v_stack_p20, v_rip - 10931047, 1, a4);
    goto loc_00A88C2D;
loc_00A88C76:
    result = RtlIntegerToUnicodeString(0 + v_stack_mA0 * 1, 10, v_stack_mA0, a4);
    a1 = 0;
    if (sign_flag) goto loc_00A88C05;
    result = RtlAppendUnicodeToString(v_stack_p20, v_rip - 10966948, v_stack_mA0, a4);
    result = RtlAppendUnicodeStringToString(v_stack_p20, v_stack_mA0, v_stack_mA0, a4);
    result = RtlAppendUnicodeToString(v_stack_p20, v_rip - 10931047, v_stack_mA0, a4);
    goto loc_00A88C03;
loc_00A88CC9:
    goto loc_00A88BE7;
loc_00A88CD4:
    if (v_rip + 4619096 == 0) goto loc_00A88D88;
    *(unsigned __int64 *)(v_rip + 4619096 + 8) = 4;
    *(unsigned __int64 *)(v_rip + 4619096) = v_rip - 10923060;
loc_00A88CEF:
    result = 0;
    goto loc_00A88AE6;
loc_00A88CF6:
    v_rsi = 0;
    result = RtlInitUnicodeString(v_stack_m68, v_rip - 10931672, v_stack_mA0, a4);
    result = RtlEqualUnicodeString(v_stack_m90, v_stack_m68, 1, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A88E08;
loc_00A88D28:
    v_r14 = 0;
loc_00A88D2B:
    result = RtlInitUnicodeString(v_stack_m58, v_rip - 10931770, 1, a4);
    if ((*(unsigned __int64 *)((unsigned int)(0x610ULL) + 24)) == 0) goto loc_00A88D7F;
loc_00A88D46:
    if (0 != 0) goto loc_00A88D77;
    if (0 != 0) goto loc_00A88E52;
loc_00A88D54:
    a1 = (*(unsigned __int64 *)((unsigned int)(0x610ULL) + 24)) + (8);
    result = RtlEqualUnicodeString(a1, v_stack_m88, 1, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A88E6D;
loc_00A88D71:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0x610ULL) + 24))) != 0) goto loc_00A88D46;
loc_00A88D77:
loc_00A88D7F:
    goto loc_00A88BC3;
loc_00A88D88:
    if (result == 0) goto loc_00A88CEF;
    result = RtlInitUnicodeString(result, v_rip - 10937936, 1, a4);
    goto loc_00A88CEF;
loc_00A88DA5:
    a4 = (unsigned int)((a4) - (1));
    if (a4 != 1) goto loc_00A88A28;
    goto loc_00A88A2F;
loc_00A88DC5:
    goto loc_00A88AE6;
loc_00A88DCF:
    result = RtlAppendUnicodeToString(v_stack_p20, v_rip - 10967262, 1, a4);
    a2 = ((unsigned int)((unsigned int)(*(unsigned __int64 *)((unsigned int)(0x610ULL) + 24)))) << (4);
    a2 = (a2) + (v_stack_mA8);
    result = RtlAppendUnicodeStringToString(v_stack_p20, a2, 1, a4);
    result = RtlAppendUnicodeToString(v_stack_p20, v_rip - 10777364, 1, a4);
    goto loc_00A88AA9;
loc_00A88E08:
    if (78 != (*(unsigned __int16 *)(v_stack_m88))) goto loc_00A88D28;
    if (37 != (*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m88 + 8)))) goto loc_00A88D28;
    if (123 != (*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m88 + 8) + 2))) goto loc_00A88D28;
    if (125 != (*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m88 + 8) + 76))) goto loc_00A88D28;
    goto loc_00A88D2B;
loc_00A88E52:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0x610ULL) + 24))) + (8);
    result = RtlEqualUnicodeString(a1, v_stack_m58, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A88D54;
loc_00A88E6D:
    v_stack_m80 = *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0x610ULL) + 24));
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0x610ULL) + 24)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0x610ULL) + 24)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0x610ULL) + 24))) = *(unsigned __int64 *)((unsigned int)(v_stack_mB8));
    *(unsigned __int64 *)((unsigned int)(v_stack_mB8)) = *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0x610ULL) + 24));
    goto loc_00A88D71;
loc_00A88E8D:
    *(unsigned __int64 *)(v_stack_m70) = v_xmm0;
    goto loc_00A88AE3;
}
```

## 5. (Beta) C Style

```c
int64_t AdtpBuildAccessesString(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, void *Arg9)
{
    uint8_t *arg9 = (uint8_t *)Arg9;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m3F;
    uint64_t v_stack_m40;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint16_t v_stack_mC6;
    uint16_t v_stack_mC8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x381D91)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m88 = Arg2;
    Arg2 = 0;
    v_stack_mB8 = Arg3;
    v_stack_m90 = Arg1;
    v_stack_m70 = Arg5;
    v_stack_mA8 = Arg6;
    v_stack_mA0 = 0;
    v_stack_m80 = 0;
    v_stack_mC4 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm1;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_00A88CD4;
loc_00A88A15:
    Arg3 = (uint32_t)((0) + 1);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg3))) - 1)));
    if (condition_is_not_equal) goto loc_00A88A15;
    if (Arg4 != 0) goto loc_00A88DA5;
loc_00A88A28:
loc_00A88A2F:
    v_stack_mB0 = v_rip - 10931047;
    if (Arg7 != 0) goto loc_00A88B0E;
loc_00A88A47:
    Arg2 = ((uint32_t)((uint32_t)(Arg3 + Arg3 * 2 * 8 + 1))) + ((uint32_t)((uint32_t)(Arg3 + Arg3 * 2 * 8 + 1)));
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x6B416553ULL), Arg4);
    Arg2 = 0;
    v_stack_m78 = result;
    if (result == 0) goto loc_00A88DC5;
    *(uint8_t *)(arg9) = 1;
loc_00A88A6E:
    local_rbx = (uint16_t)((Arg3 + Arg3 * 2 * 8 + 1) + ((uint16_t)(Arg3 + Arg3 * 2 * 8 + 1)));
    v_stack_mC8 = 0;
    v_stack_mC6 = (uint16_t)(local_rbx);
    v_stack_mC0 = result;
    if ((((uint32_t)((uint32_t)(Arg3))) & (0x1F0000ULL)) != 0) goto loc_00A88C18;
loc_00A88A92:
loc_00A88AA0:
    if (((*(uint32_t *)(v_rip - 0xA6CBAD)) & ((uint32_t)((uint32_t)(Arg3)))) != 0) goto loc_00A88DCF;
loc_00A88AA9:
    local_rbx = (uint32_t)((5) + 1);
    local_rsi = (v_rip - 10931117) + (4);
    if (((uint32_t)(local_rbx)) < 7) goto loc_00A88AA0;
    Arg1 = 0;
    if ((uint16_t)((uint32_t)(Arg3)) != 0) goto loc_00A88B39;
loc_00A88AC0:
    if (sign_flag) goto loc_00A88AE3;
    if (v_stack_mA8 == 0) goto loc_00A88E8D;
    *(uint64_t *)(v_stack_mA8) = v_stack_m78;
    result = (uint32_t)((v_stack_mC8) + (2));
    *(uint32_t *)(v_stack_mA8 + 0xC) = 0;
    *(uint32_t *)(v_stack_mA8 + 0x8) = (uint32_t)(result);
loc_00A88AE3:
loc_00A88AE6:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(0x6B416553ULL), Arg4);
    local_rsp = (local_rsp) + (176);
    return result;
loc_00A88B0E:
    if (Arg8 == 0) goto loc_00A88A47;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg8)) + v_stack_p18 * 1)) >= 0x400ULL) goto loc_00A88A47;
    *(uint32_t *)(Arg8) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg8)) + v_stack_p18 * 1);
    v_stack_m78 = Arg7 + (uint32_t)(*(uint32_t *)(Arg8)) * 2;
    goto loc_00A88A6E;
loc_00A88B39:
    result = ExAcquireResourceExclusiveLite(v_rip + 4618935, 1, (uint32_t)(0x6B416553ULL), Arg4);
    local_rsi = 0;
    if ((*(uint64_t *)(v_rip + 0x467C86)) == 0) goto loc_00A88BC3;
loc_00A88B70:
    if (0 != 0) goto loc_00A88BB5;
    Arg1 = (*(uint64_t *)(v_rip + 0x467C8E)) + (8);
    result = RtlEqualUnicodeString(Arg1, v_stack_m90, 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A88C13;
    *(uint64_t *)(v_rip + 0x467C8E) = *(uint64_t *)(*(uint64_t *)(v_rip + 0x467C8E));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x467C8E)) = *(uint64_t *)(v_rip + 0x467C4B);
    *(uint64_t *)(v_rip + 0x467C41) = *(uint64_t *)(v_rip + 0x467C8E);
loc_00A88BAF:
    if ((*(uint64_t *)(v_rip + 0x467C8E)) != 0) goto loc_00A88B70;
loc_00A88BB5:
    if (1 == 1) goto loc_00A88CF6;
loc_00A88BC3:
    result = ExReleaseResourceLite(v_rip + 4618806, v_stack_m90, 1, Arg4);
    result = KeLeaveCriticalRegion(v_rip + 4618806, v_stack_m90, 1, Arg4);
    Arg1 = 0;
    if (1 == 0) goto loc_00A88CC9;
loc_00A88BE7:
    v_stack_mA0 = 0x140000ULL;
    v_stack_m98 = v_stack_m58;
loc_00A88BFE:
    if ((((uint32_t)((uint32_t)(Arg3))) & (1)) != 0) goto loc_00A88C76;
loc_00A88C03:
    Arg1 = 0;
loc_00A88C05:
    local_rbx = (uint32_t)((0) + 1);
    local_rsi = (uint32_t)((1) + (1));
    if (((uint32_t)(local_rbx)) < 16) goto loc_00A88BFE;
    goto loc_00A88AC0;
loc_00A88C13:
    goto loc_00A88BAF;
loc_00A88C18:
loc_00A88C28:
    if (((*(uint32_t *)(v_rip - 0xA6CD49)) & ((uint32_t)((uint32_t)(Arg3)))) != 0) goto loc_00A88C40;
loc_00A88C2D:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m90))) + 1);
    local_r14 = (v_rip - 10931529) + (4);
    if (((uint32_t)(local_rsi)) < 0) goto loc_00A88C28;
    goto loc_00A88A92;
loc_00A88C40:
    result = RtlAppendUnicodeToString(v_stack_p20, v_rip - 10966863, 1, Arg4);
    Arg2 = ((uint32_t)((uint32_t)(local_rsi))) << (4);
    Arg2 = (Arg2) + (v_rip + 4619096);
    result = RtlAppendUnicodeStringToString(v_stack_p20, Arg2, 1, Arg4);
    result = RtlAppendUnicodeToString(v_stack_p20, v_rip - 10931047, 1, Arg4);
    goto loc_00A88C2D;
loc_00A88C76:
    result = RtlIntegerToUnicodeString(0 + v_stack_mA0 * 1, 10, v_stack_mA0, Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_00A88C05;
    result = RtlAppendUnicodeToString(v_stack_p20, v_rip - 10966948, v_stack_mA0, Arg4);
    result = RtlAppendUnicodeStringToString(v_stack_p20, v_stack_mA0, v_stack_mA0, Arg4);
    result = RtlAppendUnicodeToString(v_stack_p20, v_rip - 10931047, v_stack_mA0, Arg4);
    goto loc_00A88C03;
loc_00A88CC9:
    goto loc_00A88BE7;
loc_00A88CD4:
    if (v_rip + 4619096 == 0) goto loc_00A88D88;
    *(uint64_t *)(v_rip + 0x467B58 + 0x8) = 4;
    *(uint64_t *)(v_rip + 0x467B58) = v_rip - 10923060;
loc_00A88CEF:
    result = 0;
    goto loc_00A88AE6;
loc_00A88CF6:
    local_rsi = 0;
    result = RtlInitUnicodeString(v_stack_m68, v_rip - 10931672, v_stack_mA0, Arg4);
    result = RtlEqualUnicodeString(v_stack_m90, v_stack_m68, 1, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00A88E08;
loc_00A88D28:
    local_r14 = 0;
loc_00A88D2B:
    result = RtlInitUnicodeString(v_stack_m58, v_rip - 10931770, 1, Arg4);
    if ((*(uint64_t *)((uint32_t)(0x610ULL) + 0x18)) == 0) goto loc_00A88D7F;
loc_00A88D46:
    if (0 != 0) goto loc_00A88D77;
    if (0 != 0) goto loc_00A88E52;
loc_00A88D54:
    Arg1 = (*(uint64_t *)((uint32_t)(0x610ULL) + 0x18)) + (8);
    result = RtlEqualUnicodeString(Arg1, v_stack_m88, 1, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00A88E6D;
loc_00A88D71:
    if ((*(uint64_t *)(*(uint64_t *)((uint32_t)(0x610ULL) + 0x18))) != 0) goto loc_00A88D46;
loc_00A88D77:
loc_00A88D7F:
    goto loc_00A88BC3;
loc_00A88D88:
    if (result == 0) goto loc_00A88CEF;
    result = RtlInitUnicodeString(result, v_rip - 10937936, 1, Arg4);
    goto loc_00A88CEF;
loc_00A88DA5:
    Arg4 = (uint32_t)((Arg4) - (1));
    if (Arg4 != 1) goto loc_00A88A28;
    goto loc_00A88A2F;
loc_00A88DC5:
    goto loc_00A88AE6;
loc_00A88DCF:
    result = RtlAppendUnicodeToString(v_stack_p20, v_rip - 10967262, 1, Arg4);
    Arg2 = ((uint32_t)((uint32_t)(*(uint64_t *)((uint32_t)(0x610ULL) + 0x18)))) << (4);
    Arg2 = (Arg2) + (v_stack_mA8);
    result = RtlAppendUnicodeStringToString(v_stack_p20, Arg2, 1, Arg4);
    result = RtlAppendUnicodeToString(v_stack_p20, v_rip - 10777364, 1, Arg4);
    goto loc_00A88AA9;
loc_00A88E08:
    if (78 != (*(uint16_t *)(v_stack_m88))) goto loc_00A88D28;
    if (37 != (*(uint16_t *)(*(uint64_t *)(v_stack_m88 + 0x8)))) goto loc_00A88D28;
    if (123 != (*(uint16_t *)(*(uint64_t *)(v_stack_m88 + 0x8) + 0x2))) goto loc_00A88D28;
    if (125 != (*(uint16_t *)(*(uint64_t *)(v_stack_m88 + 0x8) + 0x4C))) goto loc_00A88D28;
    goto loc_00A88D2B;
loc_00A88E52:
    Arg1 = (*(uint64_t *)(*(uint64_t *)((uint32_t)(0x610ULL) + 0x18))) + (8);
    result = RtlEqualUnicodeString(Arg1, v_stack_m58, 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A88D54;
loc_00A88E6D:
    v_stack_m80 = *(uint64_t *)(*(uint64_t *)((uint32_t)(0x610ULL) + 0x18));
    *(uint64_t *)(*(uint64_t *)((uint32_t)(0x610ULL) + 0x18)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0x610ULL) + 0x18)));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)(0x610ULL) + 0x18))) = *(uint64_t *)((uint32_t)(v_stack_mB8));
    *(uint64_t *)((uint32_t)(v_stack_mB8)) = *(uint64_t *)(*(uint64_t *)((uint32_t)(0x610ULL) + 0x18));
    goto loc_00A88D71;
loc_00A88E8D:
    *(uint64_t *)(v_stack_m70) = v_xmm0;
    goto loc_00A88AE3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg9` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8898C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
