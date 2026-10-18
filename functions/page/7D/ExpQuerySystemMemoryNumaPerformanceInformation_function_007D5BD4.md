# ExpQuerySystemMemoryNumaPerformanceInformation

- RVA: `0x007D5BD4`–`0x007D5F91` (길이 `957` bytes)
- VA: `0x00000001407D5BD4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D5CF0`
- 디코드: `264`개 명령, `957/957` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x007D5CF4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x007D5D37` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x007D5DB6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007D5E0E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x007D5E2C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007D5F14` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007D5F5A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D5F6C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [ExpQuerySystemInformation](../A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A5B659`

### Static image references
- `0x007D5C5C` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x007D5CD5` → RVA `0x00E00638` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x007D5CF4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x007D5D37` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x007D5DB6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007D5E0E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x007D5E2C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007D5F14` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007D5F5A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D5F6C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007D5BD4  4C 8B DC                        mov r11, rsp
007D5BD7  49 89 5B 10                     mov qword ptr [r11 + 0x10], rbx
007D5BDB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
007D5BDF  57                              push rdi
007D5BE0  41 54                           push r12
007D5BE2  41 55                           push r13
007D5BE4  41 56                           push r14
007D5BE6  41 57                           push r15
007D5BE8  48 81 EC A0 00 00 00            sub rsp, 0xa0
007D5BEF  45 8B E1                        mov r12d, r9d
007D5BF2  4D 8B E8                        mov r13, r8
007D5BF5  41 83 63 08 00                  and dword ptr [r11 + 8], 0
007D5BFA  0F 57 C0                        xorps xmm0, xmm0
007D5BFD  33 C0                           xor eax, eax
007D5BFF  41 0F 11 43 C0                  movups xmmword ptr [r11 - 0x40], xmm0
007D5C04  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
007D5C08  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
007D5C0D  33 FF                           xor edi, edi
007D5C0F  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
007D5C14  33 F6                           xor esi, esi
007D5C16  48 85 C9                        test rcx, rcx
007D5C19  75 0A                           jne 0x1407d5c25
007D5C1B  BB 0D 00 00 C0                  mov ebx, 0xc000000d
007D5C20  E9 28 03 00 00                  jmp 0x1407d5f4d
007D5C25  83 FA 10                        cmp edx, 0x10
007D5C28  72 F1                           jb 0x1407d5c1b
007D5C2A  4D 85 ED                        test r13, r13
007D5C2D  75 05                           jne 0x1407d5c34
007D5C2F  45 85 E4                        test r12d, r12d
007D5C32  75 E7                           jne 0x1407d5c1b
007D5C34  0F 10 01                        movups xmm0, xmmword ptr [rcx]
007D5C37  F3 0F 7F 44 24 68               movdqu xmmword ptr [rsp + 0x68], xmm0
007D5C3D  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
007D5C42  41 83 F8 01                     cmp r8d, 1
007D5C46  75 D3                           jne 0x1407d5c1b
007D5C48  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
007D5C4D  48 8B C2                        mov rax, rdx
007D5C50  48 C1 E8 20                     shr rax, 0x20
007D5C54  85 C0                           test eax, eax
007D5C56  75 C3                           jne 0x1407d5c1b
007D5C58  49 C1 E8 20                     shr r8, 0x20
007D5C5C  0F B7 05 9D F3 7E 00            movzx eax, word ptr [rip + 0x7ef39d]
007D5C63  44 3B C0                        cmp r8d, eax
007D5C66  72 06                           jb 0x1407d5c6e
007D5C68  41 83 F8 FF                     cmp r8d, -1
007D5C6C  75 AD                           jne 0x1407d5c1b
007D5C6E  85 D2                           test edx, edx
007D5C70  74 56                           je 0x1407d5cc8
007D5C72  83 EA 01                        sub edx, 1
007D5C75  74 49                           je 0x1407d5cc0
007D5C77  83 EA 01                        sub edx, 1
007D5C7A  74 3C                           je 0x1407d5cb8
007D5C7C  83 EA 01                        sub edx, 1
007D5C7F  74 2F                           je 0x1407d5cb0
007D5C81  83 EA 01                        sub edx, 1
007D5C84  74 22                           je 0x1407d5ca8
007D5C86  83 EA 01                        sub edx, 1
007D5C89  74 15                           je 0x1407d5ca0
007D5C8B  83 FA 01                        cmp edx, 1
007D5C8E  74 08                           je 0x1407d5c98
007D5C90  41 BE 07 00 00 00               mov r14d, 7
007D5C96  EB 33                           jmp 0x1407d5ccb
007D5C98  41 BE 06 00 00 00               mov r14d, 6
007D5C9E  EB 2B                           jmp 0x1407d5ccb
007D5CA0  41 BE 05 00 00 00               mov r14d, 5
007D5CA6  EB 23                           jmp 0x1407d5ccb
007D5CA8  41 BE 04 00 00 00               mov r14d, 4
007D5CAE  EB 1B                           jmp 0x1407d5ccb
007D5CB0  41 BE 03 00 00 00               mov r14d, 3
007D5CB6  EB 13                           jmp 0x1407d5ccb
007D5CB8  41 BE 02 00 00 00               mov r14d, 2
007D5CBE  EB 0B                           jmp 0x1407d5ccb
007D5CC0  41 BE 01 00 00 00               mov r14d, 1
007D5CC6  EB 03                           jmp 0x1407d5ccb
007D5CC8  45 33 F6                        xor r14d, r14d
007D5CCB  41 83 FE 07                     cmp r14d, 7
007D5CCF  0F 84 46 FF FF FF               je 0x1407d5c1b
007D5CD5  48 8B 05 5C A9 62 00            mov rax, qword ptr [rip + 0x62a95c]
007D5CDC  4C 8D 8C 24 D0 00 00 00         lea r9, [rsp + 0xd0]
007D5CE4  4C 8D 84 24 88 00 00 00         lea r8, [rsp + 0x88]
007D5CEC  BA 18 00 00 00                  mov edx, 0x18
007D5CF1  8D 4A 1A                        lea ecx, [rdx + 0x1a]
007D5CF4  E8 D7 4D EE FF                  call 0x1406baad0
007D5CF9  8B D8                           mov ebx, eax
007D5CFB  85 C0                           test eax, eax
007D5CFD  0F 88 4A 02 00 00               js 0x1407d5f4d
007D5D03  48 8D 84 24 D0 00 00 00         lea rax, [rsp + 0xd0]
007D5D0B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007D5D10  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
007D5D15  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
007D5D1B  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
007D5D20  45 33 C9                        xor r9d, r9d
007D5D23  44 8B 44 24 6C                  mov r8d, dword ptr [rsp + 0x6c]
007D5D28  83 CA FF                        or edx, 0xffffffff
007D5D2B  41 8D 49 01                     lea ecx, [r9 + 1]
007D5D2F  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
007D5D37  E8 94 4D EE FF                  call 0x1406baad0
007D5D3C  33 DB                           xor ebx, ebx
007D5D3E  B9 23 00 00 C0                  mov ecx, 0xc0000023
007D5D43  3B C1                           cmp eax, ecx
007D5D45  0F 45 D8                        cmovne ebx, eax
007D5D48  85 DB                           test ebx, ebx
007D5D4A  0F 88 FD 01 00 00               js 0x1407d5f4d
007D5D50  8B 84 24 D0 00 00 00            mov eax, dword ptr [rsp + 0xd0]
007D5D57  85 C0                           test eax, eax
007D5D59  75 0A                           jne 0x1407d5d65
007D5D5B  BB 25 02 00 C0                  mov ebx, 0xc0000225
007D5D60  E9 E8 01 00 00                  jmp 0x1407d5f4d
007D5D65  83 F8 08                        cmp eax, 8
007D5D68  0F 82 CE 01 00 00               jb 0x1407d5f3c
007D5D6E  44 8D 78 F8                     lea r15d, [rax - 8]
007D5D72  41 F6 C7 1F                     test r15b, 0x1f
007D5D76  0F 85 C0 01 00 00               jne 0x1407d5f3c
007D5D7C  41 83 E7 E0                     and r15d, 0xffffffe0
007D5D80  41 83 C7 10                     add r15d, 0x10
007D5D84  45 3B E7                        cmp r12d, r15d
007D5D87  73 1B                           jae 0x1407d5da4
007D5D89  8B D9                           mov ebx, ecx
007D5D8B  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
007D5D93  48 85 C0                        test rax, rax
007D5D96  0F 84 B1 01 00 00               je 0x1407d5f4d
007D5D9C  44 89 38                        mov dword ptr [rax], r15d
007D5D9F  E9 A9 01 00 00                  jmp 0x1407d5f4d
007D5DA4  48 8B D0                        mov rdx, rax
007D5DA7  41 B8 4D 6E 48 6C               mov r8d, 0x6c486e4d
007D5DAD  41 BC 00 01 00 00               mov r12d, 0x100
007D5DB3  41 8B CC                        mov ecx, r12d
007D5DB6  E8 35 C3 3A 00                  call 0x140b820f0
007D5DBB  48 8B F8                        mov rdi, rax
007D5DBE  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
007D5DC3  48 85 C0                        test rax, rax
007D5DC6  75 0A                           jne 0x1407d5dd2
007D5DC8  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007D5DCD  E9 7B 01 00 00                  jmp 0x1407d5f4d
007D5DD2  48 8D 84 24 D0 00 00 00         lea rax, [rsp + 0xd0]
007D5DDA  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007D5DDF  8B 8C 24 D0 00 00 00            mov ecx, dword ptr [rsp + 0xd0]
007D5DE6  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
007D5DEA  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
007D5DEF  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
007D5DF4  45 33 C9                        xor r9d, r9d
007D5DF7  44 8B 44 24 6C                  mov r8d, dword ptr [rsp + 0x6c]
007D5DFC  83 CA FF                        or edx, 0xffffffff
007D5DFF  45 8D 71 01                     lea r14d, [r9 + 1]
007D5E03  41 8B CE                        mov ecx, r14d
007D5E06  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
007D5E0E  E8 BD 4C EE FF                  call 0x1406baad0
007D5E13  8B D8                           mov ebx, eax
007D5E15  85 C0                           test eax, eax
007D5E17  0F 88 30 01 00 00               js 0x1407d5f4d
007D5E1D  41 8B DF                        mov ebx, r15d
007D5E20  41 B8 4D 6E 48 6C               mov r8d, 0x6c486e4d
007D5E26  41 8B D7                        mov edx, r15d
007D5E29  49 8B CC                        mov rcx, r12
007D5E2C  E8 BF C2 3A 00                  call 0x140b820f0
007D5E31  48 8B F0                        mov rsi, rax
007D5E34  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
007D5E39  48 85 C0                        test rax, rax
007D5E3C  74 8A                           je 0x1407d5dc8
007D5E3E  44 89 30                        mov dword ptr [rax], r14d
007D5E41  44 89 78 04                     mov dword ptr [rax + 4], r15d
007D5E45  8B 07                           mov eax, dword ptr [rdi]
007D5E47  89 46 08                        mov dword ptr [rsi + 8], eax
007D5E4A  45 33 D2                        xor r10d, r10d
007D5E4D  44 3B 17                        cmp r10d, dword ptr [rdi]
007D5E50  0F 83 B5 00 00 00               jae 0x1407d5f0b
007D5E56  41 8B D2                        mov edx, r10d
007D5E59  48 C1 E2 05                     shl rdx, 5
007D5E5D  8B 4C 3A 14                     mov ecx, dword ptr [rdx + rdi + 0x14]
007D5E61  85 C9                           test ecx, ecx
007D5E63  74 2C                           je 0x1407d5e91
007D5E65  41 2B CE                        sub ecx, r14d
007D5E68  74 22                           je 0x1407d5e8c
007D5E6A  41 2B CE                        sub ecx, r14d
007D5E6D  74 15                           je 0x1407d5e84
007D5E6F  41 3B CE                        cmp ecx, r14d
007D5E72  74 08                           je 0x1407d5e7c
007D5E74  41 B8 04 00 00 00               mov r8d, 4
007D5E7A  EB 18                           jmp 0x1407d5e94
007D5E7C  41 B8 03 00 00 00               mov r8d, 3
007D5E82  EB 10                           jmp 0x1407d5e94
007D5E84  41 B8 02 00 00 00               mov r8d, 2
007D5E8A  EB 08                           jmp 0x1407d5e94
007D5E8C  45 8B C6                        mov r8d, r14d
007D5E8F  EB 03                           jmp 0x1407d5e94
007D5E91  45 33 C0                        xor r8d, r8d
007D5E94  41 83 F8 04                     cmp r8d, 4
007D5E98  74 6A                           je 0x1407d5f04
007D5E9A  0F B6 44 3A 19                  movzx eax, byte ptr [rdx + rdi + 0x19]
007D5E9F  84 C0                           test al, al
007D5EA1  75 05                           jne 0x1407d5ea8
007D5EA3  45 33 C9                        xor r9d, r9d
007D5EA6  EB 0D                           jmp 0x1407d5eb5
007D5EA8  3C 3B                           cmp al, 0x3b
007D5EAA  73 58                           jae 0x1407d5f04
007D5EAC  8D 48 05                        lea ecx, [rax + 5]
007D5EAF  4D 8B CE                        mov r9, r14
007D5EB2  49 D3 E1                        shl r9, cl
007D5EB5  8B 44 3A 08                     mov eax, dword ptr [rdx + rdi + 8]
007D5EB9  89 44 32 10                     mov dword ptr [rdx + rsi + 0x10], eax
007D5EBD  8B 44 3A 0C                     mov eax, dword ptr [rdx + rdi + 0xc]
007D5EC1  89 44 32 14                     mov dword ptr [rdx + rsi + 0x14], eax
007D5EC5  44 89 44 32 18                  mov dword ptr [rdx + rsi + 0x18], r8d
007D5ECA  8A 44 32 1C                     mov al, byte ptr [rdx + rsi + 0x1c]
007D5ECE  8A C8                           mov cl, al
007D5ED0  32 4C 3A 18                     xor cl, byte ptr [rdx + rdi + 0x18]
007D5ED4  41 22 CE                        and cl, r14b
007D5ED7  32 C8                           xor cl, al
007D5ED9  88 4C 32 1C                     mov byte ptr [rdx + rsi + 0x1c], cl
007D5EDD  8A 44 3A 18                     mov al, byte ptr [rdx + rdi + 0x18]
007D5EE1  02 C0                           add al, al
007D5EE3  32 C1                           xor al, cl
007D5EE5  24 02                           and al, 2
007D5EE7  32 C1                           xor al, cl
007D5EE9  88 44 32 1C                     mov byte ptr [rdx + rsi + 0x1c], al
007D5EED  4C 89 4C 32 20                  mov qword ptr [rdx + rsi + 0x20], r9
007D5EF2  48 8B 44 3A 20                  mov rax, qword ptr [rdx + rdi + 0x20]
007D5EF7  48 89 44 32 28                  mov qword ptr [rdx + rsi + 0x28], rax
007D5EFC  45 03 D6                        add r10d, r14d
007D5EFF  E9 49 FF FF FF                  jmp 0x1407d5e4d
007D5F04  BB 0F 00 14 C0                  mov ebx, 0xc014000f
007D5F09  EB 42                           jmp 0x1407d5f4d
007D5F0B  4C 8B C3                        mov r8, rbx
007D5F0E  48 8B D6                        mov rdx, rsi
007D5F11  49 8B CD                        mov rcx, r13
007D5F14  E8 27 09 EF FF                  call 0x1406c6840
007D5F19  90                              nop
007D5F1A  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
007D5F22  48 85 C0                        test rax, rax
007D5F25  74 03                           je 0x1407d5f2a
007D5F27  44 89 38                        mov dword ptr [rax], r15d
007D5F2A  33 DB                           xor ebx, ebx
007D5F2C  EB 1F                           jmp 0x1407d5f4d
007D5F2E  8B D8                           mov ebx, eax
007D5F30  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
007D5F35  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
007D5F3A  EB 11                           jmp 0x1407d5f4d
007D5F3C  BB E5 00 00 C0                  mov ebx, 0xc00000e5
007D5F41  EB 0A                           jmp 0x1407d5f4d
007D5F43  8B D8                           mov ebx, eax
007D5F45  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
007D5F4A  48 8B F7                        mov rsi, rdi
007D5F4D  48 85 FF                        test rdi, rdi
007D5F50  74 0D                           je 0x1407d5f5f
007D5F52  BA 4D 6E 48 6C                  mov edx, 0x6c486e4d
007D5F57  48 8B CF                        mov rcx, rdi
007D5F5A  E8 11 C9 3A 00                  call 0x140b82870
007D5F5F  48 85 F6                        test rsi, rsi
007D5F62  74 0D                           je 0x1407d5f71
007D5F64  BA 4D 6E 48 6C                  mov edx, 0x6c486e4d
007D5F69  48 8B CE                        mov rcx, rsi
007D5F6C  E8 FF C8 3A 00                  call 0x140b82870
007D5F71  8B C3                           mov eax, ebx
007D5F73  4C 8D 9C 24 A0 00 00 00         lea r11, [rsp + 0xa0]
007D5F7B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
007D5F7F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
007D5F83  49 8B E3                        mov rsp, r11
007D5F86  41 5F                           pop r15
007D5F88  41 5E                           pop r14
007D5F8A  41 5D                           pop r13
007D5F8C  41 5C                           pop r12
007D5F8E  5F                              pop rdi
007D5F8F  C3                              ret
007D5F90  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpQuerySystemMemoryNumaPerformanceInformation(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (160);
    result = 0;
    *(unsigned __int64 *)(v_rsp - 64) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 48) = 0;
    v_stack_m60 = v_xmm0;
    v_rdi = 0;
    v_stack_m70 = 0;
    v_rsi = 0;
    if (a1 != 0) goto loc_007D5C25;
loc_007D5C1B:
    goto loc_007D5F4D;
loc_007D5C25:
    if (a2 < 16) goto loc_007D5C1B;
    if (a3 != 0) goto loc_007D5C34;
    if ((unsigned int)((unsigned int)(a4)) != 0) goto loc_007D5C1B;
loc_007D5C34:
    v_stack_m60 = v_xmm0;
    if (((unsigned int)(v_stack_m60)) != 1) goto loc_007D5C1B;
    result = (v_stack_m58) >> (32);
    if ((unsigned int)(result) != 0) goto loc_007D5C1B;
    a3 = (v_stack_m60) >> (32);
    if (((unsigned int)(a3)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 8319901)))) goto loc_007D5C6E;
    if (((unsigned int)(a3)) != -1) goto loc_007D5C1B;
loc_007D5C6E:
    if ((unsigned int)(v_stack_m58) == 0) goto loc_007D5CC8;
    a2 = (unsigned int)((v_stack_m58) - (1));
    if (condition_is_equal) goto loc_007D5CC0;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_007D5CB8;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_007D5CB0;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_007D5CA8;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_007D5CA0;
    if (a2 == 1) goto loc_007D5C98;
    goto loc_007D5CCB;
loc_007D5C98:
    goto loc_007D5CCB;
loc_007D5CA0:
    goto loc_007D5CCB;
loc_007D5CA8:
    goto loc_007D5CCB;
loc_007D5CB0:
    goto loc_007D5CCB;
loc_007D5CB8:
    goto loc_007D5CCB;
loc_007D5CC0:
    goto loc_007D5CCB;
loc_007D5CC8:
    v_r14 = 0;
loc_007D5CCB:
    if (0 == 7) goto loc_007D5C1B;
    result = guard_dispatch_icall(24 + 26, 24, v_stack_m40, v_stack_p8);
    if (sign_flag) goto loc_007D5F4D;
    v_stack_m90 = v_stack_p8;
    v_stack_mA8 = 0;
    a4 = 0;
    a2 = (unsigned int)((24) | (0xFFFFFFFFULL));
    result = guard_dispatch_icall(a4 + 1, a2, (unsigned int)(v_stack_m5C), a4);
    v_rbx = 0;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000023ULL)))) { v_rbx = (unsigned int)(result); }
    if (sign_flag) goto loc_007D5F4D;
    if ((unsigned int)((unsigned int)(v_stack_p8)) != 0) goto loc_007D5D65;
    goto loc_007D5F4D;
loc_007D5D65:
    if (((unsigned int)((unsigned int)(v_stack_p8))) < 8) goto loc_007D5F3C;
    if ((((unsigned __int8)((unsigned int)(v_stack_p8) - 8)) & (31)) != 0) goto loc_007D5F3C;
    v_r15 = (unsigned int)(((unsigned int)(v_stack_p8) - 8) & (0xFFFFFFE0ULL));
    v_r15 = (unsigned int)((v_r15) + (16));
    if (((unsigned int)((unsigned int)(a4))) >= ((unsigned int)(v_r15))) goto loc_007D5DA4;
    if (a5 == 0) goto loc_007D5F4D;
    *(unsigned int *)(a5) = (unsigned int)(v_r15);
    goto loc_007D5F4D;
loc_007D5DA4:
    result = ExAllocatePool2(256, a5, (unsigned int)(0x6C486E4DULL), a4);
    v_stack_m70 = result;
    if (result != 0) goto loc_007D5DD2;
loc_007D5DC8:
    goto loc_007D5F4D;
loc_007D5DD2:
    v_stack_m90 = v_stack_p8;
    v_stack_m98 = (unsigned int)((unsigned int)(v_stack_p8));
    v_stack_mA0 = result;
    v_stack_mA8 = 0;
    a4 = 0;
    a2 = (unsigned int)((a5) | (0xFFFFFFFFULL));
    result = guard_dispatch_icall((unsigned int)((unsigned int)(a4 + 1)), a2, (unsigned int)(v_stack_m5C), a4);
    if (sign_flag) goto loc_007D5F4D;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_r15)), (unsigned int)(0x6C486E4DULL), a4);
    v_stack_m68 = result;
    if (result == 0) goto loc_007D5DC8;
    *(unsigned int *)(result) = (unsigned int)(a4 + 1);
    *(unsigned int *)(result + 4) = (unsigned int)(v_r15);
    *(unsigned int *)(result + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    v_r10 = 0;
loc_007D5E4D:
    if (0 >= (*(unsigned int *)(result))) goto loc_007D5F0B;
    a2 = (0) << (5);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + result * 1 + 20))) == 0) goto loc_007D5E91;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + result * 1 + 20))) - ((unsigned int)(a4 + 1)));
    if (condition_is_equal) goto loc_007D5E8C;
    a1 = (unsigned int)((a1) - ((unsigned int)(a4 + 1)));
    if (condition_is_equal) goto loc_007D5E84;
    if (((unsigned int)(a1)) == ((unsigned int)(a4 + 1))) goto loc_007D5E7C;
    goto loc_007D5E94;
loc_007D5E7C:
    goto loc_007D5E94;
loc_007D5E84:
    goto loc_007D5E94;
loc_007D5E8C:
    goto loc_007D5E94;
loc_007D5E91:
    a3 = 0;
loc_007D5E94:
    if (0 == 4) goto loc_007D5F04;
    if ((unsigned __int8)(*(unsigned __int8 *)(a2 + result * 1 + 25)) != 0) goto loc_007D5EA8;
    a4 = 0;
    goto loc_007D5EB5;
loc_007D5EA8:
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 + result * 1 + 25))) >= 59) goto loc_007D5F04;
    a4 = (a4 + 1) << ((unsigned __int8)(*(unsigned __int8 *)(a2 + result * 1 + 25) + 5));
loc_007D5EB5:
    *(unsigned int *)(a2 + result * 1 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + result * 1 + 8)));
    *(unsigned int *)(a2 + result * 1 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + result * 1 + 12)));
    *(unsigned int *)(a2 + result * 1 + 24) = 0;
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a2 + result * 1 + 28))) ^ (*(unsigned __int8 *)(a2 + result * 1 + 24)));
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(a4 + 1)));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(a2 + result * 1 + 28))));
    *(unsigned __int8 *)(a2 + result * 1 + 28) = (unsigned __int8)(a1);
    result = (unsigned __int8)((*(unsigned __int8 *)(a2 + result * 1 + 24)) + ((unsigned __int8)(*(unsigned __int8 *)(a2 + result * 1 + 24))));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (2));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    *(unsigned __int8 *)(a2 + result * 1 + 28) = (unsigned __int8)(result);
    *(unsigned __int64 *)(a2 + result * 1 + 32) = a4;
    *(unsigned __int64 *)(a2 + result * 1 + 40) = *(unsigned __int64 *)(a2 + result * 1 + 32);
    v_r10 = (unsigned int)((v_r10) + ((unsigned int)(a4 + 1)));
    goto loc_007D5E4D;
loc_007D5F04:
    goto loc_007D5F4D;
loc_007D5F0B:
    result = memcpy(0, result, (unsigned int)(0xC014000FULL), a4);
    if (a5 != 0) {
        *(unsigned int *)(a5) = (unsigned int)(v_r15);
    }
    v_rbx = 0;
    goto loc_007D5F4D;
loc_007D5F3C:
    goto loc_007D5F4D;
loc_007D5F4D:
    result = a5;
    if (result != 0) {
        a2 = 0x6C486E4DULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0xC014000FULL), a4);
    }
    if (result != 0) {
        a2 = 0x6C486E4DULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0xC014000FULL), a4);
    }
    return (unsigned int)((unsigned int)((unsigned int)(0xC00000E5ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t ExpQuerySystemMemoryNumaPerformanceInformation(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (160);
    result = 0;
    *(uint64_t *)(local_rsp - 0x40) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x30) = 0;
    v_stack_m60 = v_xmm0;
    local_rdi = 0;
    v_stack_m70 = 0;
    local_rsi = 0;
    if (Arg1 != 0) goto loc_007D5C25;
loc_007D5C1B:
    goto loc_007D5F4D;
loc_007D5C25:
    if (Arg2 < 16) goto loc_007D5C1B;
    if (Arg3 != 0) goto loc_007D5C34;
    if ((uint32_t)((uint32_t)(Arg4)) != 0) goto loc_007D5C1B;
loc_007D5C34:
    v_stack_m60 = v_xmm0;
    if (((uint32_t)(v_stack_m60)) != 1) goto loc_007D5C1B;
    result = (v_stack_m58) >> (32);
    if ((uint32_t)(result) != 0) goto loc_007D5C1B;
    Arg3 = (v_stack_m60) >> (32);
    if (((uint32_t)(Arg3)) < ((uint32_t)(*(uint16_t *)(v_rip + 0x7EF39D)))) goto loc_007D5C6E;
    if (((uint32_t)(Arg3)) != -1) goto loc_007D5C1B;
loc_007D5C6E:
    if ((uint32_t)(v_stack_m58) == 0) goto loc_007D5CC8;
    Arg2 = (uint32_t)((v_stack_m58) - (1));
    if (condition_is_equal) goto loc_007D5CC0;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_007D5CB8;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_007D5CB0;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_007D5CA8;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_007D5CA0;
    if (Arg2 == 1) goto loc_007D5C98;
    goto loc_007D5CCB;
loc_007D5C98:
    goto loc_007D5CCB;
loc_007D5CA0:
    goto loc_007D5CCB;
loc_007D5CA8:
    goto loc_007D5CCB;
loc_007D5CB0:
    goto loc_007D5CCB;
loc_007D5CB8:
    goto loc_007D5CCB;
loc_007D5CC0:
    goto loc_007D5CCB;
loc_007D5CC8:
    local_r14 = 0;
loc_007D5CCB:
    if (0 == 7) goto loc_007D5C1B;
    result = guard_dispatch_icall(24 + 26, 24, v_stack_m40, v_stack_p8);
    if (sign_flag) goto loc_007D5F4D;
    v_stack_m90 = v_stack_p8;
    v_stack_mA8 = 0;
    Arg4 = 0;
    Arg2 = (uint32_t)((24) | (0xFFFFFFFFULL));
    result = guard_dispatch_icall(Arg4 + 1, Arg2, (uint32_t)(v_stack_m5C), Arg4);
    local_rbx = 0;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000023ULL)))) { local_rbx = (uint32_t)(result); }
    if (sign_flag) goto loc_007D5F4D;
    if ((uint32_t)((uint32_t)(v_stack_p8)) != 0) goto loc_007D5D65;
    goto loc_007D5F4D;
loc_007D5D65:
    if (((uint32_t)((uint32_t)(v_stack_p8))) < 8) goto loc_007D5F3C;
    if ((((uint8_t)((uint32_t)(v_stack_p8) - 8)) & (31)) != 0) goto loc_007D5F3C;
    local_r15 = (uint32_t)(((uint32_t)(v_stack_p8) - 8) & (0xFFFFFFE0ULL));
    local_r15 = (uint32_t)((local_r15) + (16));
    if (((uint32_t)((uint32_t)(Arg4))) >= ((uint32_t)(local_r15))) goto loc_007D5DA4;
    if (Arg5 == 0) goto loc_007D5F4D;
    *(uint32_t *)(Arg5) = (uint32_t)(local_r15);
    goto loc_007D5F4D;
loc_007D5DA4:
    result = ExAllocatePool2(256, Arg5, (uint32_t)(0x6C486E4DULL), Arg4);
    v_stack_m70 = result;
    if (result != 0) goto loc_007D5DD2;
loc_007D5DC8:
    goto loc_007D5F4D;
loc_007D5DD2:
    v_stack_m90 = v_stack_p8;
    v_stack_m98 = (uint32_t)((uint32_t)(v_stack_p8));
    v_stack_mA0 = result;
    v_stack_mA8 = 0;
    Arg4 = 0;
    Arg2 = (uint32_t)((Arg5) | (0xFFFFFFFFULL));
    result = guard_dispatch_icall((uint32_t)((uint32_t)(Arg4 + 1)), Arg2, (uint32_t)(v_stack_m5C), Arg4);
    if (sign_flag) goto loc_007D5F4D;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_r15)), (uint32_t)(0x6C486E4DULL), Arg4);
    v_stack_m68 = result;
    if (result == 0) goto loc_007D5DC8;
    *(uint32_t *)(result) = (uint32_t)(Arg4 + 1);
    *(uint32_t *)(result + 0x4) = (uint32_t)(local_r15);
    *(uint32_t *)(result + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    local_r10 = 0;
loc_007D5E4D:
    if (0 >= (*(uint32_t *)(result))) goto loc_007D5F0B;
    Arg2 = (0) << (5);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + result * 1 + 0x14))) == 0) goto loc_007D5E91;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + result * 1 + 0x14))) - ((uint32_t)(Arg4 + 1)));
    if (condition_is_equal) goto loc_007D5E8C;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(Arg4 + 1)));
    if (condition_is_equal) goto loc_007D5E84;
    if (((uint32_t)(Arg1)) == ((uint32_t)(Arg4 + 1))) goto loc_007D5E7C;
    goto loc_007D5E94;
loc_007D5E7C:
    goto loc_007D5E94;
loc_007D5E84:
    goto loc_007D5E94;
loc_007D5E8C:
    goto loc_007D5E94;
loc_007D5E91:
    Arg3 = 0;
loc_007D5E94:
    if (0 == 4) goto loc_007D5F04;
    if ((uint8_t)(*(uint8_t *)(Arg2 + result * 1 + 0x19)) != 0) goto loc_007D5EA8;
    Arg4 = 0;
    goto loc_007D5EB5;
loc_007D5EA8:
    if (((uint8_t)(*(uint8_t *)(Arg2 + result * 1 + 0x19))) >= 59) goto loc_007D5F04;
    Arg4 = (Arg4 + 1) << ((uint8_t)(*(uint8_t *)(Arg2 + result * 1 + 0x19) + 5));
loc_007D5EB5:
    *(uint32_t *)(Arg2 + result * 1 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + result * 1 + 0x8)));
    *(uint32_t *)(Arg2 + result * 1 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + result * 1 + 0xC)));
    *(uint32_t *)(Arg2 + result * 1 + 0x18) = 0;
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(Arg2 + result * 1 + 0x1C))) ^ (*(uint8_t *)(Arg2 + result * 1 + 0x18)));
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(Arg4 + 1)));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(Arg2 + result * 1 + 0x1C))));
    *(uint8_t *)(Arg2 + result * 1 + 0x1C) = (uint8_t)(Arg1);
    result = (uint8_t)((*(uint8_t *)(Arg2 + result * 1 + 0x18)) + ((uint8_t)(*(uint8_t *)(Arg2 + result * 1 + 0x18))));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (2));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    *(uint8_t *)(Arg2 + result * 1 + 0x1C) = (uint8_t)(result);
    *(uint64_t *)(Arg2 + result * 1 + 0x20) = Arg4;
    *(uint64_t *)(Arg2 + result * 1 + 0x28) = *(uint64_t *)(Arg2 + result * 1 + 0x20);
    local_r10 = (uint32_t)((local_r10) + ((uint32_t)(Arg4 + 1)));
    goto loc_007D5E4D;
loc_007D5F04:
    goto loc_007D5F4D;
loc_007D5F0B:
    result = memcpy(0, result, (uint32_t)(0xC014000FULL), Arg4);
    if (Arg5 != 0) {
        *(uint32_t *)(Arg5) = (uint32_t)(local_r15);
    }
    local_rbx = 0;
    goto loc_007D5F4D;
loc_007D5F3C:
    goto loc_007D5F4D;
loc_007D5F4D:
    result = Arg5;
    if (result != 0) {
        Arg2 = 0x6C486E4DULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0xC014000FULL), Arg4);
    }
    if (result != 0) {
        Arg2 = 0x6C486E4DULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0xC014000FULL), Arg4);
    }
    return (uint32_t)((uint32_t)((uint32_t)(0xC00000E5ULL)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007D5BD4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
