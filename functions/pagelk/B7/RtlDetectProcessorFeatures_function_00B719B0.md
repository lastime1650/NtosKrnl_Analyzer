# RtlDetectProcessorFeatures

- RVA: `0x00B719B0`–`0x00B720B4` (길이 `1,796` bytes)
- VA: `0x0000000140B719B0`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CFFD4`
- 디코드: `430`개 명령, `1,796/1,796` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00B71A48` → [RtlGetProcessorSignature](RtlGetProcessorSignature_function_00B7225C.md) (function, `0x00B7225C`)
- `0x00B71BEC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B71C9A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B71D51` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B71D7E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B71EF1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B71F77` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B72017` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B72039` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B72074` → [RtlpGetSpecificProcessorFlags](RtlpGetSpecificProcessorFlags_function_00B72430.md) (function, `0x00B72430`)
- `0x00B7209B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KiSetProcessorSignature](../../text/5C/KiSetProcessorSignature_function_005C48C0.md) at `0x005C48EE`

### Static image references
- `0x00B719C3` → RVA `0x00E0A740` (`.data`; read)
- `0x00B71AB8` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00B71C40` → RVA `0x00F05BE8` (`.data`; read)
- `0x00B71C5F` → RVA `0x00F05BE0` (`.data`; read)
- `0x00B72082` → RVA `0x00F05BE8` (`.data`; write)
- `0x00B72089` → RVA `0x00F05BE0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x00B71BEC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B71C9A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
  - `0x00B71D51` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
  - `0x00B71D7E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
  - `0x00B71EF1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B71F77` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
  - `0x00B72017` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
  - `0x00B72039` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGELK` → `.text`)
  - `0x00B7209B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B719B0  40 53                           push rbx
00B719B2  56                              push rsi
00B719B3  57                              push rdi
00B719B4  41 54                           push r12
00B719B6  41 55                           push r13
00B719B8  41 56                           push r14
00B719BA  41 57                           push r15
00B719BC  48 81 EC 00 01 00 00            sub rsp, 0x100
00B719C3  48 8B 05 76 8D 29 00            mov rax, qword ptr [rip + 0x298d76]
00B719CA  48 33 C4                        xor rax, rsp
00B719CD  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
00B719D5  4C 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r9
00B719DD  49 8B D8                        mov rbx, r8
00B719E0  48 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbx
00B719E8  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
00B719F0  8B C1                           mov eax, ecx
00B719F2  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
00B719F6  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
00B719FA  48 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdx
00B71A02  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
00B71A0A  4C 89 8C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r9
00B71A12  0F 57 C0                        xorps xmm0, xmm0
00B71A15  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
00B71A1D  0F 57 C9                        xorps xmm1, xmm1
00B71A20  33 C9                           xor ecx, ecx
00B71A22  0F 11 4C 24 40                  movups xmmword ptr [rsp + 0x40], xmm1
00B71A27  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00B71A2C  21 4C 24 38                     and dword ptr [rsp + 0x38], ecx
00B71A30  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B71A34  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
00B71A39  4C 8D 44 24 4C                  lea r8, [rsp + 0x4c]
00B71A3E  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00B71A43  48 8D 4C 24 44                  lea rcx, [rsp + 0x44]
00B71A48  E8 0F 08 00 00                  call 0x140b7225c
00B71A4D  8B F8                           mov edi, eax
00B71A4F  89 44 24 6C                     mov dword ptr [rsp + 0x6c], eax
00B71A53  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00B71A57  B8 00 00 00 80                  mov eax, 0x80000000
00B71A5C  33 C9                           xor ecx, ecx
00B71A5E  0F A2                           cpuid
00B71A60  44 8B D0                        mov r10d, eax
00B71A63  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00B71A67  33 C0                           xor eax, eax
00B71A69  33 C9                           xor ecx, ecx
00B71A6B  0F A2                           cpuid
00B71A6D  44 8B C8                        mov r9d, eax
00B71A70  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00B71A74  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
00B71A7B  89 9C 24 E4 00 00 00            mov dword ptr [rsp + 0xe4], ebx
00B71A82  89 8C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ecx
00B71A89  89 94 24 EC 00 00 00            mov dword ptr [rsp + 0xec], edx
00B71A90  45 33 ED                        xor r13d, r13d
00B71A93  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
00B71A98  45 33 E4                        xor r12d, r12d
00B71A9B  4C 89 A4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r12
00B71AA3  45 33 FF                        xor r15d, r15d
00B71AA6  33 DB                           xor ebx, ebx
00B71AA8  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00B71AAC  45 33 C0                        xor r8d, r8d
00B71AAF  0F B6 4C 24 44                  movzx ecx, byte ptr [rsp + 0x44]
00B71AB4  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
00B71AB8  4C 8D 35 41 E5 48 FF            lea r14, [rip - 0xb71abf]
00B71ABF  44 89 44 24 3C                  mov dword ptr [rsp + 0x3c], r8d
00B71AC4  41 83 F8 3C                     cmp r8d, 0x3c
00B71AC8  0F 83 B6 02 00 00               jae 0x140b71d84
00B71ACE  4B 8D 34 80                     lea rsi, [r8 + r8*4]
00B71AD2  41 8B 84 F6 20 8A 00 00         mov eax, dword ptr [r14 + rsi*8 + 0x8a20]
00B71ADA  A8 02                           test al, 2
00B71ADC  0F 85 40 02 00 00               jne 0x140b71d22
00B71AE2  C1 E8 18                        shr eax, 0x18
00B71AE5  85 C0                           test eax, eax
00B71AE7  74 09                           je 0x140b71af2
00B71AE9  0F A3 C8                        bt eax, ecx
00B71AEC  0F 83 30 02 00 00               jae 0x140b71d22
00B71AF2  41 8B 84 F6 10 8A 00 00         mov eax, dword ptr [r14 + rsi*8 + 0x8a10]
00B71AFA  41 3B C7                        cmp eax, r15d
00B71AFD  75 0A                           jne 0x140b71b09
00B71AFF  41 39 9C F6 14 8A 00 00         cmp dword ptr [r14 + rsi*8 + 0x8a14], ebx
00B71B07  74 4D                           je 0x140b71b56
00B71B09  44 8B F8                        mov r15d, eax
00B71B0C  41 8B 9C F6 14 8A 00 00         mov ebx, dword ptr [r14 + rsi*8 + 0x8a14]
00B71B14  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00B71B18  3D 00 00 00 80                  cmp eax, 0x80000000
00B71B1D  72 05                           jb 0x140b71b24
00B71B1F  41 3B C2                        cmp eax, r10d
00B71B22  76 05                           jbe 0x140b71b29
00B71B24  41 3B C1                        cmp eax, r9d
00B71B27  77 22                           ja 0x140b71b4b
00B71B29  8B CB                           mov ecx, ebx
00B71B2B  0F A2                           cpuid
00B71B2D  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
00B71B34  89 9C 24 E4 00 00 00            mov dword ptr [rsp + 0xe4], ebx
00B71B3B  89 8C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ecx
00B71B42  89 94 24 EC 00 00 00            mov dword ptr [rsp + 0xec], edx
00B71B49  EB 0B                           jmp 0x140b71b56
00B71B4B  0F 57 C0                        xorps xmm0, xmm0
00B71B4E  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
00B71B56  33 D2                           xor edx, edx
00B71B58  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
00B71B5C  49 63 84 F6 1C 8A 00 00         movsxd rax, dword ptr [r14 + rsi*8 + 0x8a1c]
00B71B64  8B 8C 84 E0 00 00 00            mov ecx, dword ptr [rsp + rax*4 + 0xe0]
00B71B6B  41 85 8C F6 18 8A 00 00         test dword ptr [r14 + rsi*8 + 0x8a18], ecx
00B71B73  75 38                           jne 0x140b71bad
00B71B75  41 8B 9C F6 20 8A 00 00         mov ebx, dword ptr [r14 + rsi*8 + 0x8a20]
00B71B7D  F6 C3 08                        test bl, 8
00B71B80  74 13                           je 0x140b71b95
00B71B82  49 8B 8C F6 28 8A 00 00         mov rcx, qword ptr [r14 + rsi*8 + 0x8a28]
00B71B8A  48 8B C1                        mov rax, rcx
00B71B8D  49 23 C5                        and rax, r13
00B71B90  48 3B C1                        cmp rax, rcx
00B71B93  74 18                           je 0x140b71bad
00B71B95  F6 C3 10                        test bl, 0x10
00B71B98  74 1C                           je 0x140b71bb6
00B71B9A  49 8B 8C F6 28 8A 00 00         mov rcx, qword ptr [r14 + rsi*8 + 0x8a28]
00B71BA2  48 8B C1                        mov rax, rcx
00B71BA5  49 23 C4                        and rax, r12
00B71BA8  48 3B C1                        cmp rax, rcx
00B71BAB  75 09                           jne 0x140b71bb6
00B71BAD  BA 01 00 00 00                  mov edx, 1
00B71BB2  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
00B71BB6  49 8B 84 F6 30 8A 00 00         mov rax, qword ptr [r14 + rsi*8 + 0x8a30]
00B71BBE  48 85 C0                        test rax, rax
00B71BC1  74 41                           je 0x140b71c04
00B71BC3  0F 10 44 24 40                  movups xmm0, xmmword ptr [rsp + 0x40]
00B71BC8  0F 29 84 24 C0 00 00 00         movaps xmmword ptr [rsp + 0xc0], xmm0
00B71BD0  F2 0F 10 44 24 50               movsd xmm0, qword ptr [rsp + 0x50]
00B71BD6  F2 0F 11 84 24 D0 00 00 00      movsd qword ptr [rsp + 0xd0], xmm0
00B71BDF  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
00B71BE4  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
00B71BEC  E8 DF 8E B4 FF                  call 0x1406baad0
00B71BF1  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
00B71BF5  44 8B 44 24 3C                  mov r8d, dword ptr [rsp + 0x3c]
00B71BFA  44 8B 4C 24 68                  mov r9d, dword ptr [rsp + 0x68]
00B71BFF  44 8B 54 24 60                  mov r10d, dword ptr [rsp + 0x60]
00B71C04  41 8B 8C F6 20 8A 00 00         mov ecx, dword ptr [r14 + rsi*8 + 0x8a20]
00B71C0C  85 D2                           test edx, edx
00B71C0E  0F 85 8C 00 00 00               jne 0x140b71ca0
00B71C14  F6 C1 01                        test cl, 1
00B71C17  0F 85 0D 01 00 00               jne 0x140b71d2a
00B71C1D  F6 C1 04                        test cl, 4
00B71C20  0F 84 F4 00 00 00               je 0x140b71d1a
00B71C26  39 54 24 40                     cmp dword ptr [rsp + 0x40], edx
00B71C2A  0F 84 EA 00 00 00               je 0x140b71d1a
00B71C30  F6 C1 08                        test cl, 8
00B71C33  74 1A                           je 0x140b71c4f
00B71C35  49 8B 8C F6 28 8A 00 00         mov rcx, qword ptr [r14 + rsi*8 + 0x8a28]
00B71C3D  48 8B C1                        mov rax, rcx
00B71C40  48 23 05 A1 3F 39 00            and rax, qword ptr [rip + 0x393fa1]
00B71C47  48 3B C1                        cmp rax, rcx
00B71C4A  0F 94 C2                        sete dl
00B71C4D  EB 1C                           jmp 0x140b71c6b
00B71C4F  F6 C1 10                        test cl, 0x10
00B71C52  74 17                           je 0x140b71c6b
00B71C54  49 8B 8C F6 28 8A 00 00         mov rcx, qword ptr [r14 + rsi*8 + 0x8a28]
00B71C5C  48 8B C1                        mov rax, rcx
00B71C5F  48 23 05 7A 3F 39 00            and rax, qword ptr [rip + 0x393f7a]
00B71C66  48 3B C1                        cmp rax, rcx
00B71C69  74 08                           je 0x140b71c73
00B71C6B  85 D2                           test edx, edx
00B71C6D  0F 84 A7 00 00 00               je 0x140b71d1a
00B71C73  49 63 84 F6 1C 8A 00 00         movsxd rax, dword ptr [r14 + rsi*8 + 0x8a1c]
00B71C7B  45 8B 8C F6 18 8A 00 00         mov r9d, dword ptr [r14 + rsi*8 + 0x8a18]
00B71C83  45 8B 84 F6 10 8A 00 00         mov r8d, dword ptr [r14 + rsi*8 + 0x8a10]
00B71C8B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B71C90  BA FE FF FF FF                  mov edx, 0xfffffffe
00B71C95  B9 5D 00 00 00                  mov ecx, 0x5d
00B71C9A  E8 C1 B9 98 FF                  call 0x1404fd660
00B71C9F  CC                              int3
00B71CA0  8B D9                           mov ebx, ecx
00B71CA2  83 E3 08                        and ebx, 8
00B71CA5  74 0F                           je 0x140b71cb6
00B71CA7  4D 0B AC F6 28 8A 00 00         or r13, qword ptr [r14 + rsi*8 + 0x8a28]
00B71CAF  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
00B71CB4  EB 15                           jmp 0x140b71ccb
00B71CB6  F6 C1 10                        test cl, 0x10
00B71CB9  74 10                           je 0x140b71ccb
00B71CBB  4D 0B A4 F6 28 8A 00 00         or r12, qword ptr [r14 + rsi*8 + 0x8a28]
00B71CC3  4C 89 A4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r12
00B71CCB  8B C1                           mov eax, ecx
00B71CCD  24 24                           and al, 0x24
00B71CCF  3C 04                           cmp al, 4
00B71CD1  75 47                           jne 0x140b71d1a
00B71CD3  83 7C 24 40 00                  cmp dword ptr [rsp + 0x40], 0
00B71CD8  74 40                           je 0x140b71d1a
00B71CDA  33 D2                           xor edx, edx
00B71CDC  85 DB                           test ebx, ebx
00B71CDE  74 1A                           je 0x140b71cfa
00B71CE0  49 8B 8C F6 28 8A 00 00         mov rcx, qword ptr [r14 + rsi*8 + 0x8a28]
00B71CE8  48 8B C1                        mov rax, rcx
00B71CEB  48 23 05 F6 3E 39 00            and rax, qword ptr [rip + 0x393ef6]
00B71CF2  48 3B C1                        cmp rax, rcx
00B71CF5  0F 94 C2                        sete dl
00B71CF8  EB 1C                           jmp 0x140b71d16
00B71CFA  F6 C1 10                        test cl, 0x10
00B71CFD  74 17                           je 0x140b71d16
00B71CFF  49 8B 8C F6 28 8A 00 00         mov rcx, qword ptr [r14 + rsi*8 + 0x8a28]
00B71D07  48 8B C1                        mov rax, rcx
00B71D0A  48 23 05 CF 3E 39 00            and rax, qword ptr [rip + 0x393ecf]
00B71D11  48 3B C1                        cmp rax, rcx
00B71D14  74 04                           je 0x140b71d1a
00B71D16  85 D2                           test edx, edx
00B71D18  74 3D                           je 0x140b71d57
00B71D1A  8B 5C 24 30                     mov ebx, dword ptr [rsp + 0x30]
00B71D1E  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
00B71D22  41 FF C0                        inc r8d
00B71D25  E9 95 FD FF FF                  jmp 0x140b71abf
00B71D2A  49 63 84 F6 1C 8A 00 00         movsxd rax, dword ptr [r14 + rsi*8 + 0x8a1c]
00B71D32  45 8B 8C F6 18 8A 00 00         mov r9d, dword ptr [r14 + rsi*8 + 0x8a18]
00B71D3A  45 8B 84 F6 10 8A 00 00         mov r8d, dword ptr [r14 + rsi*8 + 0x8a10]
00B71D42  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B71D47  BA FF FF FF FF                  mov edx, 0xffffffff
00B71D4C  B9 5D 00 00 00                  mov ecx, 0x5d
00B71D51  E8 0A B9 98 FF                  call 0x1404fd660
00B71D56  CC                              int3
00B71D57  49 63 84 F6 1C 8A 00 00         movsxd rax, dword ptr [r14 + rsi*8 + 0x8a1c]
00B71D5F  45 8B 8C F6 18 8A 00 00         mov r9d, dword ptr [r14 + rsi*8 + 0x8a18]
00B71D67  45 8B 84 F6 10 8A 00 00         mov r8d, dword ptr [r14 + rsi*8 + 0x8a10]
00B71D6F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B71D74  BA FD FF FF FF                  mov edx, 0xfffffffd
00B71D79  B9 5D 00 00 00                  mov ecx, 0x5d
00B71D7E  E8 DD B8 98 FF                  call 0x1404fd660
00B71D83  CC                              int3
00B71D84  45 33 FF                        xor r15d, r15d
00B71D87  44 8A 5C 24 44                  mov r11b, byte ptr [rsp + 0x44]
00B71D8C  44 89 7C 24 3C                  mov dword ptr [rsp + 0x3c], r15d
00B71D91  41 83 FF 02                     cmp r15d, 2
00B71D95  0F 83 B1 02 00 00               jae 0x140b7204c
00B71D9B  4B 8D 0C 7F                     lea rcx, [r15 + r15*2]
00B71D9F  48 8D 34 CD D0 B6 00 00         lea rsi, [rcx*8 + 0xb6d0]
00B71DA7  49 03 F6                        add rsi, r14
00B71DAA  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
00B71DAF  8B 56 04                        mov edx, dword ptr [rsi + 4]
00B71DB2  F6 C2 02                        test dl, 2
00B71DB5  0F 85 89 02 00 00               jne 0x140b72044
00B71DBB  8B CA                           mov ecx, edx
00B71DBD  C1 E9 18                        shr ecx, 0x18
00B71DC0  85 C9                           test ecx, ecx
00B71DC2  74 0D                           je 0x140b71dd1
00B71DC4  41 0F B6 C3                     movzx eax, r11b
00B71DC8  0F A3 C1                        bt ecx, eax
00B71DCB  0F 83 73 02 00 00               jae 0x140b72044
00B71DD1  F6 C2 08                        test dl, 8
00B71DD4  74 05                           je 0x140b71ddb
00B71DD6  49 8B D5                        mov rdx, r13
00B71DD9  EB 0C                           jmp 0x140b71de7
00B71DDB  F6 C2 10                        test dl, 0x10
00B71DDE  0F 84 60 02 00 00               je 0x140b72044
00B71DE4  49 8B D4                        mov rdx, r12
00B71DE7  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
00B71DEB  48 8B C1                        mov rax, rcx
00B71DEE  48 23 C2                        and rax, rdx
00B71DF1  48 3B C1                        cmp rax, rcx
00B71DF4  0F 85 4A 02 00 00               jne 0x140b72044
00B71DFA  8B 0E                           mov ecx, dword ptr [rsi]
00B71DFC  0F 32                           rdmsr
00B71DFE  48 C1 E2 20                     shl rdx, 0x20
00B71E02  48 0B C2                        or rax, rdx
00B71E05  48 8B D0                        mov rdx, rax
00B71E08  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00B71E10  EB 69                           jmp 0x140b71e7b
00B71E12  33 D2                           xor edx, edx
00B71E14  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
00B71E1C  4C 8D 35 DD E1 48 FF            lea r14, [rip - 0xb71e23]
00B71E23  8B 7C 24 6C                     mov edi, dword ptr [rsp + 0x6c]
00B71E27  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
00B71E2C  4C 8B A4 24 80 00 00 00         mov r12, qword ptr [rsp + 0x80]
00B71E34  44 8B 7C 24 3C                  mov r15d, dword ptr [rsp + 0x3c]
00B71E39  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00B71E3E  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00B71E42  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00B71E46  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00B71E4E  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00B71E56  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00B71E5E  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00B71E66  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00B71E6E  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00B71E76  44 8A 5C 24 44                  mov r11b, byte ptr [rsp + 0x44]
00B71E7B  48 8B 5E 08                     mov rbx, qword ptr [rsi + 8]
00B71E7F  45 0F B6 C3                     movzx r8d, r11b
00B71E83  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
00B71E88  48 8B 0B                        mov rcx, qword ptr [rbx]
00B71E8B  48 85 C9                        test rcx, rcx
00B71E8E  0F 84 AB 01 00 00               je 0x140b7203f
00B71E94  8B 43 08                        mov eax, dword ptr [rbx + 8]
00B71E97  A8 02                           test al, 2
00B71E99  0F 85 4B 01 00 00               jne 0x140b71fea
00B71E9F  C1 E8 18                        shr eax, 0x18
00B71EA2  85 C0                           test eax, eax
00B71EA4  74 0A                           je 0x140b71eb0
00B71EA6  44 0F A3 C0                     bt eax, r8d
00B71EAA  0F 83 3A 01 00 00               jae 0x140b71fea
00B71EB0  48 85 CA                        test rdx, rcx
00B71EB3  B9 00 00 00 00                  mov ecx, 0
00B71EB8  0F 95 C1                        setne cl
00B71EBB  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
00B71EBF  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00B71EC3  48 85 C0                        test rax, rax
00B71EC6  74 37                           je 0x140b71eff
00B71EC8  0F 10 44 24 40                  movups xmm0, xmmword ptr [rsp + 0x40]
00B71ECD  0F 29 84 24 C0 00 00 00         movaps xmmword ptr [rsp + 0xc0], xmm0
00B71ED5  F2 0F 10 44 24 50               movsd xmm0, qword ptr [rsp + 0x50]
00B71EDB  F2 0F 11 84 24 D0 00 00 00      movsd qword ptr [rsp + 0xd0], xmm0
00B71EE4  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
00B71EE9  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
00B71EF1  E8 DA 8B B4 FF                  call 0x1406baad0
00B71EF6  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
00B71EFA  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
00B71EFF  85 C9                           test ecx, ecx
00B71F01  75 7A                           jne 0x140b71f7d
00B71F03  8B 43 08                        mov eax, dword ptr [rbx + 8]
00B71F06  A8 01                           test al, 1
00B71F08  0F 85 ED 00 00 00               jne 0x140b71ffb
00B71F0E  A8 04                           test al, 4
00B71F10  0F 84 D4 00 00 00               je 0x140b71fea
00B71F16  39 4C 24 40                     cmp dword ptr [rsp + 0x40], ecx
00B71F1A  0F 84 CA 00 00 00               je 0x140b71fea
00B71F20  33 D2                           xor edx, edx
00B71F22  A8 08                           test al, 8
00B71F24  74 16                           je 0x140b71f3c
00B71F26  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00B71F2A  48 8B C1                        mov rax, rcx
00B71F2D  48 23 05 B4 3C 39 00            and rax, qword ptr [rip + 0x393cb4]
00B71F34  48 3B C1                        cmp rax, rcx
00B71F37  0F 94 C2                        sete dl
00B71F3A  EB 17                           jmp 0x140b71f53
00B71F3C  A8 10                           test al, 0x10
00B71F3E  74 13                           je 0x140b71f53
00B71F40  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00B71F44  48 8B C1                        mov rax, rcx
00B71F47  48 23 05 92 3C 39 00            and rax, qword ptr [rip + 0x393c92]
00B71F4E  48 3B C1                        cmp rax, rcx
00B71F51  74 08                           je 0x140b71f5b
00B71F53  85 D2                           test edx, edx
00B71F55  0F 84 8F 00 00 00               je 0x140b71fea
00B71F5B  4C 8B 0B                        mov r9, qword ptr [rbx]
00B71F5E  49 8B C1                        mov rax, r9
00B71F61  48 C1 E8 20                     shr rax, 0x20
00B71F65  44 8B 06                        mov r8d, dword ptr [rsi]
00B71F68  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B71F6D  BA FB FF FF FF                  mov edx, 0xfffffffb
00B71F72  B9 5D 00 00 00                  mov ecx, 0x5d
00B71F77  E8 E4 B6 98 FF                  call 0x1404fd660
00B71F7C  CC                              int3
00B71F7D  8B 53 08                        mov edx, dword ptr [rbx + 8]
00B71F80  8B CA                           mov ecx, edx
00B71F82  8B C2                           mov eax, edx
00B71F84  83 E0 10                        and eax, 0x10
00B71F87  83 E1 08                        and ecx, 8
00B71F8A  74 0B                           je 0x140b71f97
00B71F8C  4C 0B 6B 10                     or r13, qword ptr [rbx + 0x10]
00B71F90  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
00B71F95  EB 10                           jmp 0x140b71fa7
00B71F97  85 C0                           test eax, eax
00B71F99  74 0C                           je 0x140b71fa7
00B71F9B  4C 0B 63 10                     or r12, qword ptr [rbx + 0x10]
00B71F9F  4C 89 A4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r12
00B71FA7  F6 C2 04                        test dl, 4
00B71FAA  74 3E                           je 0x140b71fea
00B71FAC  83 7C 24 40 00                  cmp dword ptr [rsp + 0x40], 0
00B71FB1  74 37                           je 0x140b71fea
00B71FB3  33 D2                           xor edx, edx
00B71FB5  85 C9                           test ecx, ecx
00B71FB7  74 16                           je 0x140b71fcf
00B71FB9  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00B71FBD  48 8B C1                        mov rax, rcx
00B71FC0  48 23 05 21 3C 39 00            and rax, qword ptr [rip + 0x393c21]
00B71FC7  48 3B C1                        cmp rax, rcx
00B71FCA  0F 94 C2                        sete dl
00B71FCD  EB 17                           jmp 0x140b71fe6
00B71FCF  85 C0                           test eax, eax
00B71FD1  74 13                           je 0x140b71fe6
00B71FD3  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00B71FD7  48 8B C1                        mov rax, rcx
00B71FDA  48 23 05 FF 3B 39 00            and rax, qword ptr [rip + 0x393bff]
00B71FE1  48 3B C1                        cmp rax, rcx
00B71FE4  74 04                           je 0x140b71fea
00B71FE6  85 D2                           test edx, edx
00B71FE8  74 33                           je 0x140b7201d
00B71FEA  48 83 C3 20                     add rbx, 0x20
00B71FEE  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
00B71FF6  E9 8D FE FF FF                  jmp 0x140b71e88
00B71FFB  4C 8B 0B                        mov r9, qword ptr [rbx]
00B71FFE  49 8B C1                        mov rax, r9
00B72001  48 C1 E8 20                     shr rax, 0x20
00B72005  44 8B 06                        mov r8d, dword ptr [rsi]
00B72008  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B7200D  BA FC FF FF FF                  mov edx, 0xfffffffc
00B72012  B9 5D 00 00 00                  mov ecx, 0x5d
00B72017  E8 44 B6 98 FF                  call 0x1404fd660
00B7201C  CC                              int3
00B7201D  4C 8B 0B                        mov r9, qword ptr [rbx]
00B72020  49 8B C1                        mov rax, r9
00B72023  48 C1 E8 20                     shr rax, 0x20
00B72027  44 8B 06                        mov r8d, dword ptr [rsi]
00B7202A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B7202F  BA FA FF FF FF                  mov edx, 0xfffffffa
00B72034  B9 5D 00 00 00                  mov ecx, 0x5d
00B72039  E8 22 B6 98 FF                  call 0x1404fd660
00B7203E  CC                              int3
00B7203F  44 8A 5C 24 44                  mov r11b, byte ptr [rsp + 0x44]
00B72044  41 FF C7                        inc r15d
00B72047  E9 40 FD FF FF                  jmp 0x140b71d8c
00B7204C  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
00B72054  4C 89 28                        mov qword ptr [rax], r13
00B72057  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00B7205F  4C 89 20                        mov qword ptr [rax], r12
00B72062  48 8B B4 24 A0 00 00 00         mov rsi, qword ptr [rsp + 0xa0]
00B7206A  48 85 F6                        test rsi, rsi
00B7206D  74 0C                           je 0x140b7207b
00B7206F  8B D7                           mov edx, edi
00B72071  41 8A CB                        mov cl, r11b
00B72074  E8 B7 03 00 00                  call 0x140b72430
00B72079  89 06                           mov dword ptr [rsi], eax
00B7207B  83 7C 24 58 00                  cmp dword ptr [rsp + 0x58], 0
00B72080  75 0E                           jne 0x140b72090
00B72082  4C 89 2D 5F 3B 39 00            mov qword ptr [rip + 0x393b5f], r13
00B72089  4C 89 25 50 3B 39 00            mov qword ptr [rip + 0x393b50], r12
00B72090  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00B72098  48 33 CC                        xor rcx, rsp
00B7209B  E8 A0 A5 B3 FF                  call 0x1406ac640
00B720A0  48 81 C4 00 01 00 00            add rsp, 0x100
00B720A7  41 5F                           pop r15
00B720A9  41 5E                           pop r14
00B720AB  41 5D                           pop r13
00B720AD  41 5C                           pop r12
00B720AF  5F                              pop rdi
00B720B0  5E                              pop rsi
00B720B1  5B                              pop rbx
00B720B2  C3                              ret
00B720B3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlDetectProcessorFeatures(int a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mEC;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF4;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_mFC;

    v_rsp = (v_rsp) - (256);
    result = (*(unsigned __int64 *)(v_rip + 2723190)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m98 = a4;
    v_stack_mA0 = a3;
    v_stack_mA8 = a2;
    v_stack_mE0 = a1;
    v_stack_mC8 = a1;
    v_stack_m90 = a2;
    v_stack_m88 = a3;
    v_stack_m80 = a4;
    v_stack_m58 = v_xmm0;
    a1 = 0;
    v_stack_mF8 = v_xmm1;
    v_stack_mE8 = 0;
    v_stack_mF8 = (unsigned int)((unsigned int)(a1));
    result = RtlGetProcessorSignature(v_stack_mF4, v_stack_mF0, v_stack_mEC, v_stack_mE8);
    v_stack_mCC = (unsigned int)(result);
    v_stack_mE4 = (unsigned int)(result);
    a1 = 0;
    v_stack_mD8 = (unsigned int)((unsigned int)(0x80000000ULL));
    result = 0;
    a1 = 0;
    v_stack_mD0 = 0;
    v_stack_m58 = 0;
    v_stack_m54 = (unsigned int)(a3);
    v_stack_m50 = 0;
    v_stack_m4C = (unsigned int)(v_stack_mF0);
    v_r13 = 0;
    v_stack_mC0 = 0;
    v_r12 = 0;
    v_stack_mB8 = 0;
    v_r15 = 0;
    v_rbx = 0;
    v_stack_m108 = 0;
    a3 = 0;
    v_stack_m104 = (unsigned int)(v_stack_mF4);
loc_00B71ABF:
    v_stack_mFC = 0;
    if (0 >= 60) goto loc_00B71D84;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35360)))) & (2)) != 0) goto loc_00B71D22;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35360))) >> (24));
    if ((unsigned int)(result) == 0) goto loc_00B71AF2;
    if (condition_is_above_or_equal) goto loc_00B71D22;
loc_00B71AF2:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35344)))) != 0) goto loc_00B71B09;
    if ((*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35348)) == 0) goto loc_00B71B56;
loc_00B71B09:
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35348)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35344)))) < 0x80000000ULL) goto loc_00B71B24;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35344)))) <= ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0x80000000ULL)))))) goto loc_00B71B29;
loc_00B71B24:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35344)))) > 0) goto loc_00B71B4B;
loc_00B71B29:
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35344)));
    v_stack_m54 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35348)));
    v_stack_m50 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35348)))));
    v_stack_m4C = (unsigned int)(v_stack_mF0);
    goto loc_00B71B56;
loc_00B71B4B:
    v_stack_m58 = v_xmm0;
loc_00B71B56:
    a2 = 0;
    v_stack_m100 = 0;
    if (((*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35352)) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + (int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35356)) * 4 + 224))))) != 0) goto loc_00B71BAD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35360)))) & (8)) == 0) goto loc_00B71B95;
    result = (*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368)) & (0);
    if (result == (*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368))) goto loc_00B71BAD;
loc_00B71B95:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35360)))) & (16)) == 0) goto loc_00B71BB6;
    result = (*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368)) & (0);
    if (result == (*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368))) {
        a2 = 1;
        v_stack_m100 = (unsigned int)(a2);
    }
    result = *(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35376);
    v_r10 = (unsigned int)((unsigned int)((unsigned int)(0x80000000ULL)));
    if (*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35376) != 0) {
        v_stack_m78 = v_xmm0;
        v_stack_m68 = v_xmm0;
        a2 = v_stack_m100;
        a1 = v_stack_m78;
        result = guard_dispatch_icall(a1, a2, a3, 0);
        a2 = v_stack_m100;
        a3 = v_stack_mFC;
        a4 = v_stack_mD0;
        v_r10 = v_stack_mD8;
    }
    if ((unsigned int)(a2) != 0) goto loc_00B71CA0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35360)))) & (1)) != 0) goto loc_00B71D2A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35360)))) & (4)) == 0) goto loc_00B71D1A;
    if (v_stack_mF8 == ((unsigned int)(a2))) goto loc_00B71D1A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35360)))) & (8)) == 0) goto loc_00B71C4F;
    result = (*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368)) & (*(unsigned __int64 *)(v_rip + 3751841));
    a2 = (result == (*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368))) ? 1 : 0;
    goto loc_00B71C6B;
loc_00B71C4F:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368))) & (16)) == 0) goto loc_00B71C6B;
    result = (*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368)) & (*(unsigned __int64 *)(v_rip + 3751802));
    if (result == (*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368))) goto loc_00B71C73;
loc_00B71C6B:
    if ((unsigned int)(a2) == 0) goto loc_00B71D1A;
loc_00B71C73:
    v_stack_m118 = (int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35356));
    result = KeBugCheckEx(93, (unsigned int)(0xFFFFFFFEULL), (unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35344)), (unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35352)));
loc_00B71CA0:
    v_rbx = (unsigned int)((93) & (8));
    if (condition_is_equal) goto loc_00B71CB6;
    v_r13 = (v_r13) | (*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368));
    v_stack_mC0 = v_r13;
    goto loc_00B71CCB;
loc_00B71CB6:
    if (((93) & (16)) != 0) {
        v_r12 = (v_r12) | (*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368));
        v_stack_mB8 = v_r12;
    }
    result = (unsigned __int8)((93) & (36));
    if (((unsigned __int8)(result)) != 4) goto loc_00B71D1A;
    if (v_stack_mF8 == 0) goto loc_00B71D1A;
    a2 = 0;
    if ((unsigned int)(v_rbx) == 0) goto loc_00B71CFA;
    result = (*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368)) & (*(unsigned __int64 *)(v_rip + 3751670));
    a2 = (result == (*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368))) ? 1 : 0;
    goto loc_00B71D16;
loc_00B71CFA:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368))) & (16)) == 0) goto loc_00B71D16;
    result = (*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368)) & (*(unsigned __int64 *)(v_rip + 3751631));
    if (result == (*(unsigned __int64 *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35368))) goto loc_00B71D1A;
loc_00B71D16:
    if ((unsigned int)(a2) == 0) goto loc_00B71D57;
loc_00B71D1A:
loc_00B71D22:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35344))) + 1);
    goto loc_00B71ABF;
loc_00B71D2A:
    v_stack_m118 = (int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35356));
    result = KeBugCheckEx(93, (unsigned int)(0xFFFFFFFFULL), (unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35344)), (unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35352)));
loc_00B71D57:
    v_stack_m118 = (int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35356));
    result = KeBugCheckEx(93, (unsigned int)(0xFFFFFFFDULL), (unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35344)), (unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35352)));
loc_00B71D84:
    v_r15 = 0;
loc_00B71D8C:
    v_stack_mFC = 0;
    if (0 >= 2) goto loc_00B7204C;
    v_rsi = (v_r15 + v_r15 * 2 * 8 + 46800) + (v_rip - 11999935);
    v_stack_mD8 = v_rsi;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsi + 4)))) & (2)) != 0) goto loc_00B72044;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 4))))) >> (24));
    if (a1 == 0) goto loc_00B71DD1;
    if (condition_is_above_or_equal) goto loc_00B72044;
loc_00B71DD1:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsi + 4)))) & (8)) == 0) goto loc_00B71DDB;
    goto loc_00B71DE7;
loc_00B71DDB:
    if ((((unsigned __int8)(v_r13)) & (16)) == 0) goto loc_00B72044;
loc_00B71DE7:
    result = (*(unsigned __int64 *)(v_rsi + 16)) & (v_r12);
    if (result != (*(unsigned __int64 *)(v_rsi + 16))) goto loc_00B72044;
    a2 = (v_r12) << (32);
    result = (result) | (a2);
    v_stack_mB0 = result;
    goto loc_00B71E7B;
loc_00B71E7B:
    v_stack_mD8 = (unsigned int)((unsigned __int8)(v_stack_mF4));
loc_00B71E88:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8)) == 0) goto loc_00B7203F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 8)))) & (2)) != 0) goto loc_00B71FEA;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 8))) >> (24));
    if ((unsigned int)(result) == 0) goto loc_00B71EB0;
    if (condition_is_above_or_equal) goto loc_00B71FEA;
loc_00B71EB0:
    a1 = (((result) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8)))) != 0) ? 1 : 0;
    v_stack_m100 = a1;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + 24);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + 24) != 0) {
        v_stack_m78 = v_xmm0;
        v_stack_m68 = v_xmm0;
        a2 = v_stack_m100;
        a1 = v_stack_m78;
        result = guard_dispatch_icall(a1, a2, (unsigned __int8)(v_stack_mF4), (unsigned int)(*(unsigned int *)(v_rip - 11999935 + a3 + a3 * 4 * 8 + 35352)));
        a1 = v_stack_m100;
        a3 = v_stack_mD8;
    }
    if (a1 != 0) goto loc_00B71F7D;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 8)))) & (1)) != 0) goto loc_00B71FFB;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 8)))) & (4)) == 0) goto loc_00B71FEA;
    if (v_stack_mF8 == a1) goto loc_00B71FEA;
    a2 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 8)))) & (8)) == 0) goto loc_00B71F3C;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + 16)) & (*(unsigned __int64 *)(v_rip + 3751092));
    a2 = (result == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + 16))) ? 1 : 0;
    goto loc_00B71F53;
loc_00B71F3C:
    if ((((unsigned __int8)(result)) & (16)) == 0) goto loc_00B71F53;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + 16)) & (*(unsigned __int64 *)(v_rip + 3751058));
    if (result == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + 16))) goto loc_00B71F5B;
loc_00B71F53:
    if ((unsigned int)(a2) == 0) goto loc_00B71FEA;
loc_00B71F5B:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8))) >> (32);
    v_stack_m118 = result;
    result = KeBugCheckEx(93, (unsigned int)(0xFFFFFFFBULL), (unsigned int)(*(unsigned int *)(v_rsi)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8)));
loc_00B71F7D:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 8))))) & (16));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 8))))) & (8));
    if (condition_is_equal) goto loc_00B71F97;
    v_r13 = (v_r13) | (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + 16));
    v_stack_mC0 = v_r13;
    goto loc_00B71FA7;
loc_00B71F97:
    if ((unsigned int)(result) != 0) {
        v_r12 = (v_r12) | (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + 16));
        v_stack_mB8 = v_r12;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 8) + 8)))) & (4)) == 0) goto loc_00B71FEA;
    if (v_stack_mF8 == 0) goto loc_00B71FEA;
    a2 = 0;
    if (a1 == 0) goto loc_00B71FCF;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + 16)) & (*(unsigned __int64 *)(v_rip + 3750945));
    a2 = (result == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + 16))) ? 1 : 0;
    goto loc_00B71FE6;
loc_00B71FCF:
    if ((unsigned int)(result) == 0) goto loc_00B71FE6;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + 16)) & (*(unsigned __int64 *)(v_rip + 3750911));
    if (result == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 8) + 16))) goto loc_00B71FEA;
loc_00B71FE6:
    if ((unsigned int)(a2) == 0) goto loc_00B7201D;
loc_00B71FEA:
    v_rbx = (*(unsigned __int64 *)(v_rsi + 8)) + (32);
    goto loc_00B71E88;
loc_00B71FFB:
    result = (*(unsigned __int64 *)(v_rbx)) >> (32);
    v_stack_m118 = result;
    result = KeBugCheckEx(93, (unsigned int)(0xFFFFFFFCULL), (unsigned int)(*(unsigned int *)(v_rsi)), *(unsigned __int64 *)(v_rbx));
loc_00B7201D:
    result = (*(unsigned __int64 *)(v_rbx)) >> (32);
    v_stack_m118 = result;
    result = KeBugCheckEx(93, (unsigned int)(0xFFFFFFFAULL), (unsigned int)(*(unsigned int *)(v_rsi)), *(unsigned __int64 *)(v_rbx));
loc_00B7203F:
loc_00B72044:
    v_r15 = (unsigned int)((v_r15) + 1);
    goto loc_00B71D8C;
loc_00B7204C:
    *(unsigned __int64 *)(v_stack_mA8) = v_r13;
    *(unsigned __int64 *)(v_stack_mA0) = v_r12;
    result = v_stack_mA0;
    if (v_stack_m98 != 0) {
        a2 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = (unsigned __int8)(v_stack_mF4);
        result = RtlpGetSpecificProcessorFlags(a1, a2, (unsigned int)(*(unsigned int *)(v_rsi)), *(unsigned __int64 *)(v_rbx));
        *(unsigned int *)(v_stack_m98) = (unsigned int)(result);
    }
    if (v_stack_mE0 == 0) {
        *(unsigned __int64 *)(v_rip + 3750751) = v_r13;
        *(unsigned __int64 *)(v_rip + 3750736) = v_r12;
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(*(unsigned int *)(v_rsi)), *(unsigned __int64 *)(v_rbx));
    v_rsp = (v_rsp) + (256);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlDetectProcessorFeatures(int32_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mEC;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF4;
    uint64_t v_stack_mF8;
    uint32_t v_stack_mFC;

    local_rsp = (local_rsp) - (256);
    result = (*(uint64_t *)(v_rip + 0x298D76)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m98 = Arg4;
    v_stack_mA0 = Arg3;
    v_stack_mA8 = Arg2;
    v_stack_mE0 = Arg1;
    v_stack_mC8 = Arg1;
    v_stack_m90 = Arg2;
    v_stack_m88 = Arg3;
    v_stack_m80 = Arg4;
    v_stack_m58 = v_xmm0;
    Arg1 = 0;
    v_stack_mF8 = v_xmm1;
    v_stack_mE8 = 0;
    v_stack_mF8 = (uint32_t)((uint32_t)(Arg1));
    result = RtlGetProcessorSignature(v_stack_mF4, v_stack_mF0, v_stack_mEC, v_stack_mE8);
    v_stack_mCC = (uint32_t)(result);
    v_stack_mE4 = (uint32_t)(result);
    Arg1 = 0;
    v_stack_mD8 = (uint32_t)((uint32_t)(0x80000000ULL));
    result = 0;
    Arg1 = 0;
    v_stack_mD0 = 0;
    v_stack_m58 = 0;
    v_stack_m54 = (uint32_t)(Arg3);
    v_stack_m50 = 0;
    v_stack_m4C = (uint32_t)(v_stack_mF0);
    local_r13 = 0;
    v_stack_mC0 = 0;
    local_r12 = 0;
    v_stack_mB8 = 0;
    local_r15 = 0;
    local_rbx = 0;
    v_stack_m108 = 0;
    Arg3 = 0;
    v_stack_m104 = (uint32_t)(v_stack_mF4);
loc_00B71ABF:
    v_stack_mFC = 0;
    if (0 >= 60) goto loc_00B71D84;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A20)))) & (2)) != 0) goto loc_00B71D22;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A20))) >> (24));
    if ((uint32_t)(result) == 0) goto loc_00B71AF2;
    if (condition_is_above_or_equal) goto loc_00B71D22;
loc_00B71AF2:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A10)))) != 0) goto loc_00B71B09;
    if ((*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A14)) == 0) goto loc_00B71B56;
loc_00B71B09:
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A14)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A10)))) < 0x80000000ULL) goto loc_00B71B24;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A10)))) <= ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0x80000000ULL)))))) goto loc_00B71B29;
loc_00B71B24:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A10)))) > 0) goto loc_00B71B4B;
loc_00B71B29:
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A10)));
    v_stack_m54 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A14)));
    v_stack_m50 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A14)))));
    v_stack_m4C = (uint32_t)(v_stack_mF0);
    goto loc_00B71B56;
loc_00B71B4B:
    v_stack_m58 = v_xmm0;
loc_00B71B56:
    Arg2 = 0;
    v_stack_m100 = 0;
    if (((*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A18)) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + (int32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A1C)) * 4 + 0xE0))))) != 0) goto loc_00B71BAD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A20)))) & (8)) == 0) goto loc_00B71B95;
    result = (*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28)) & (0);
    if (result == (*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28))) goto loc_00B71BAD;
loc_00B71B95:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A20)))) & (16)) == 0) goto loc_00B71BB6;
    result = (*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28)) & (0);
    if (result == (*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28))) {
        Arg2 = 1;
        v_stack_m100 = (uint32_t)(Arg2);
    }
    result = *(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A30);
    local_r10 = (uint32_t)((uint32_t)((uint32_t)(0x80000000ULL)));
    if (*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A30) != 0) {
        v_stack_m78 = v_xmm0;
        v_stack_m68 = v_xmm0;
        Arg2 = v_stack_m100;
        Arg1 = v_stack_m78;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, 0);
        Arg2 = v_stack_m100;
        Arg3 = v_stack_mFC;
        Arg4 = v_stack_mD0;
        local_r10 = v_stack_mD8;
    }
    if ((uint32_t)(Arg2) != 0) goto loc_00B71CA0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A20)))) & (1)) != 0) goto loc_00B71D2A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A20)))) & (4)) == 0) goto loc_00B71D1A;
    if (v_stack_mF8 == ((uint32_t)(Arg2))) goto loc_00B71D1A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A20)))) & (8)) == 0) goto loc_00B71C4F;
    result = (*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28)) & (*(uint64_t *)(v_rip + 0x393FA1));
    Arg2 = (result == (*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28))) ? 1 : 0;
    goto loc_00B71C6B;
loc_00B71C4F:
    if ((((uint8_t)(*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28))) & (16)) == 0) goto loc_00B71C6B;
    result = (*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28)) & (*(uint64_t *)(v_rip + 0x393F7A));
    if (result == (*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28))) goto loc_00B71C73;
loc_00B71C6B:
    if ((uint32_t)(Arg2) == 0) goto loc_00B71D1A;
loc_00B71C73:
    v_stack_m118 = (int32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A1C));
    result = KeBugCheckEx(93, (uint32_t)(0xFFFFFFFEULL), (uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A10)), (uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A18)));
loc_00B71CA0:
    local_rbx = (uint32_t)((93) & (8));
    if (condition_is_equal) goto loc_00B71CB6;
    local_r13 = (local_r13) | (*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28));
    v_stack_mC0 = local_r13;
    goto loc_00B71CCB;
loc_00B71CB6:
    if (((93) & (16)) != 0) {
        local_r12 = (local_r12) | (*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28));
        v_stack_mB8 = local_r12;
    }
    result = (uint8_t)((93) & (36));
    if (((uint8_t)(result)) != 4) goto loc_00B71D1A;
    if (v_stack_mF8 == 0) goto loc_00B71D1A;
    Arg2 = 0;
    if ((uint32_t)(local_rbx) == 0) goto loc_00B71CFA;
    result = (*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28)) & (*(uint64_t *)(v_rip + 0x393EF6));
    Arg2 = (result == (*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28))) ? 1 : 0;
    goto loc_00B71D16;
loc_00B71CFA:
    if ((((uint8_t)(*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28))) & (16)) == 0) goto loc_00B71D16;
    result = (*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28)) & (*(uint64_t *)(v_rip + 0x393ECF));
    if (result == (*(uint64_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A28))) goto loc_00B71D1A;
loc_00B71D16:
    if ((uint32_t)(Arg2) == 0) goto loc_00B71D57;
loc_00B71D1A:
loc_00B71D22:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A10))) + 1);
    goto loc_00B71ABF;
loc_00B71D2A:
    v_stack_m118 = (int32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A1C));
    result = KeBugCheckEx(93, (uint32_t)(0xFFFFFFFFULL), (uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A10)), (uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A18)));
loc_00B71D57:
    v_stack_m118 = (int32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A1C));
    result = KeBugCheckEx(93, (uint32_t)(0xFFFFFFFDULL), (uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A10)), (uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A18)));
loc_00B71D84:
    local_r15 = 0;
loc_00B71D8C:
    v_stack_mFC = 0;
    if (0 >= 2) goto loc_00B7204C;
    local_rsi = (local_r15 + local_r15 * 2 * 8 + 46800) + (v_rip - 11999935);
    v_stack_mD8 = local_rsi;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x4)))) & (2)) != 0) goto loc_00B72044;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x4))))) >> (24));
    if (Arg1 == 0) goto loc_00B71DD1;
    if (condition_is_above_or_equal) goto loc_00B72044;
loc_00B71DD1:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x4)))) & (8)) == 0) goto loc_00B71DDB;
    goto loc_00B71DE7;
loc_00B71DDB:
    if ((((uint8_t)(local_r13)) & (16)) == 0) goto loc_00B72044;
loc_00B71DE7:
    result = (*(uint64_t *)(local_rsi + 0x10)) & (local_r12);
    if (result != (*(uint64_t *)(local_rsi + 0x10))) goto loc_00B72044;
    Arg2 = (local_r12) << (32);
    result = (result) | (Arg2);
    v_stack_mB0 = result;
    goto loc_00B71E7B;
loc_00B71E7B:
    v_stack_mD8 = (uint32_t)((uint8_t)(v_stack_mF4));
loc_00B71E88:
    if (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8)) == 0) goto loc_00B7203F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x8)))) & (2)) != 0) goto loc_00B71FEA;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x8))) >> (24));
    if ((uint32_t)(result) == 0) goto loc_00B71EB0;
    if (condition_is_above_or_equal) goto loc_00B71FEA;
loc_00B71EB0:
    Arg1 = (((result) & (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8)))) != 0) ? 1 : 0;
    v_stack_m100 = Arg1;
    result = *(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x18);
    if (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x18) != 0) {
        v_stack_m78 = v_xmm0;
        v_stack_m68 = v_xmm0;
        Arg2 = v_stack_m100;
        Arg1 = v_stack_m78;
        result = guard_dispatch_icall(Arg1, Arg2, (uint8_t)(v_stack_mF4), (uint32_t)(*(uint32_t *)(v_rip - 0xB71ABF + Arg3 + Arg3 * 4 * 8 + 0x8A18)));
        Arg1 = v_stack_m100;
        Arg3 = v_stack_mD8;
    }
    if (Arg1 != 0) goto loc_00B71F7D;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x8)))) & (1)) != 0) goto loc_00B71FFB;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x8)))) & (4)) == 0) goto loc_00B71FEA;
    if (v_stack_mF8 == Arg1) goto loc_00B71FEA;
    Arg2 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x8)))) & (8)) == 0) goto loc_00B71F3C;
    result = (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x10)) & (*(uint64_t *)(v_rip + 0x393CB4));
    Arg2 = (result == (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x10))) ? 1 : 0;
    goto loc_00B71F53;
loc_00B71F3C:
    if ((((uint8_t)(result)) & (16)) == 0) goto loc_00B71F53;
    result = (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x10)) & (*(uint64_t *)(v_rip + 0x393C92));
    if (result == (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x10))) goto loc_00B71F5B;
loc_00B71F53:
    if ((uint32_t)(Arg2) == 0) goto loc_00B71FEA;
loc_00B71F5B:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8))) >> (32);
    v_stack_m118 = result;
    result = KeBugCheckEx(93, (uint32_t)(0xFFFFFFFBULL), (uint32_t)(*(uint32_t *)(local_rsi)), *(uint64_t *)(*(uint64_t *)(local_rsi + 0x8)));
loc_00B71F7D:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x8))))) & (16));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x8))))) & (8));
    if (condition_is_equal) goto loc_00B71F97;
    local_r13 = (local_r13) | (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x10));
    v_stack_mC0 = local_r13;
    goto loc_00B71FA7;
loc_00B71F97:
    if ((uint32_t)(result) != 0) {
        local_r12 = (local_r12) | (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x10));
        v_stack_mB8 = local_r12;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x8)))) & (4)) == 0) goto loc_00B71FEA;
    if (v_stack_mF8 == 0) goto loc_00B71FEA;
    Arg2 = 0;
    if (Arg1 == 0) goto loc_00B71FCF;
    result = (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x10)) & (*(uint64_t *)(v_rip + 0x393C21));
    Arg2 = (result == (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x10))) ? 1 : 0;
    goto loc_00B71FE6;
loc_00B71FCF:
    if ((uint32_t)(result) == 0) goto loc_00B71FE6;
    result = (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x10)) & (*(uint64_t *)(v_rip + 0x393BFF));
    if (result == (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x8) + 0x10))) goto loc_00B71FEA;
loc_00B71FE6:
    if ((uint32_t)(Arg2) == 0) goto loc_00B7201D;
loc_00B71FEA:
    local_rbx = (*(uint64_t *)(local_rsi + 0x8)) + (32);
    goto loc_00B71E88;
loc_00B71FFB:
    result = (*(uint64_t *)(local_rbx)) >> (32);
    v_stack_m118 = result;
    result = KeBugCheckEx(93, (uint32_t)(0xFFFFFFFCULL), (uint32_t)(*(uint32_t *)(local_rsi)), *(uint64_t *)(local_rbx));
loc_00B7201D:
    result = (*(uint64_t *)(local_rbx)) >> (32);
    v_stack_m118 = result;
    result = KeBugCheckEx(93, (uint32_t)(0xFFFFFFFAULL), (uint32_t)(*(uint32_t *)(local_rsi)), *(uint64_t *)(local_rbx));
loc_00B7203F:
loc_00B72044:
    local_r15 = (uint32_t)((local_r15) + 1);
    goto loc_00B71D8C;
loc_00B7204C:
    *(uint64_t *)(v_stack_mA8) = local_r13;
    *(uint64_t *)(v_stack_mA0) = local_r12;
    result = v_stack_mA0;
    if (v_stack_m98 != 0) {
        Arg2 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = (uint8_t)(v_stack_mF4);
        result = RtlpGetSpecificProcessorFlags(Arg1, Arg2, (uint32_t)(*(uint32_t *)(local_rsi)), *(uint64_t *)(local_rbx));
        *(uint32_t *)(v_stack_m98) = (uint32_t)(result);
    }
    if (v_stack_mE0 == 0) {
        *(uint64_t *)(v_rip + 0x393B5F) = local_r13;
        *(uint64_t *)(v_rip + 0x393B50) = local_r12;
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(*(uint32_t *)(local_rsi)), *(uint64_t *)(local_rbx));
    local_rsp = (local_rsp) + (256);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B719B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
