# sub_00AD1D78

- RVA: `0x00AD1D78`–`0x00AD2439` (길이 `1,729` bytes)
- VA: `0x0000000140AD1D78`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BEA34`
- 디코드: `507`개 명령, `1,729/1,729` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AD1EC4` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (function, `0x00458B60`)
- `0x00AD1F03` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD1F23` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AD204A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD206E` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AD20CB` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AD2195` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD21ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AD2200` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AD237F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x0096A44A`

### Static image references
- `0x00AD2086` → RVA `0x00FD8390` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x00AD1EC4` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (`PAGE` → `.text`)
  - `0x00AD1F03` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD1F23` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AD204A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD206E` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AD20CB` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AD2195` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD21ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AD2200` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AD237F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AD1D78  48 8B C4                        mov rax, rsp
00AD1D7B  48 89 58 08                     mov qword ptr [rax + 8], rbx
00AD1D7F  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00AD1D83  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00AD1D87  55                              push rbp
00AD1D88  56                              push rsi
00AD1D89  57                              push rdi
00AD1D8A  41 54                           push r12
00AD1D8C  41 55                           push r13
00AD1D8E  41 56                           push r14
00AD1D90  41 57                           push r15
00AD1D92  48 83 EC 70                     sub rsp, 0x70
00AD1D96  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
00AD1D9A  33 FF                           xor edi, edi
00AD1D9C  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
00AD1DA1  49 8B F1                        mov rsi, r9
00AD1DA4  89 78 18                        mov dword ptr [rax + 0x18], edi
00AD1DA7  48 8B D9                        mov rbx, rcx
00AD1DAA  44 8B EF                        mov r13d, edi
00AD1DAD  4D 85 C0                        test r8, r8
00AD1DB0  74 51                           je 0x140ad1e03
00AD1DB2  83 39 03                        cmp dword ptr [rcx], 3
00AD1DB5  76 4C                           jbe 0x140ad1e03
00AD1DB7  49 8B C0                        mov rax, r8
00AD1DBA  8B D7                           mov edx, edi
00AD1DBC  44 8B 08                        mov r9d, dword ptr [rax]
00AD1DBF  48 8D 48 04                     lea rcx, [rax + 4]
00AD1DC3  83 FA 03                        cmp edx, 3
00AD1DC6  73 1A                           jae 0x140ad1de2
00AD1DC8  48 3B C8                        cmp rcx, rax
00AD1DCB  0F 82 48 06 00 00               jb 0x140ad2419
00AD1DD1  4A 8D 04 09                     lea rax, [rcx + r9]
00AD1DD5  48 3B C1                        cmp rax, rcx
00AD1DD8  0F 82 3B 06 00 00               jb 0x140ad2419
00AD1DDE  FF C2                           inc edx
00AD1DE0  EB DA                           jmp 0x140ad1dbc
00AD1DE2  48 3B C8                        cmp rcx, rax
00AD1DE5  0F 82 2E 06 00 00               jb 0x140ad2419
00AD1DEB  45 85 C9                        test r9d, r9d
00AD1DEE  4C 8B F7                        mov r14, rdi
00AD1DF1  4C 0F 45 F1                     cmovne r14, rcx
00AD1DF5  41 83 F9 08                     cmp r9d, 8
00AD1DF9  75 56                           jne 0x140ad1e51
00AD1DFB  83 3B 04                        cmp dword ptr [rbx], 4
00AD1DFE  4D 8B 36                        mov r14, qword ptr [r14]
00AD1E01  77 0A                           ja 0x140ad1e0d
00AD1E03  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD1E08  E9 11 06 00 00                  jmp 0x140ad241e
00AD1E0D  49 8B C0                        mov rax, r8
00AD1E10  8B D7                           mov edx, edi
00AD1E12  44 8B 08                        mov r9d, dword ptr [rax]
00AD1E15  48 8D 48 04                     lea rcx, [rax + 4]
00AD1E19  83 FA 04                        cmp edx, 4
00AD1E1C  73 1A                           jae 0x140ad1e38
00AD1E1E  48 3B C8                        cmp rcx, rax
00AD1E21  0F 82 F2 05 00 00               jb 0x140ad2419
00AD1E27  4A 8D 04 09                     lea rax, [rcx + r9]
00AD1E2B  48 3B C1                        cmp rax, rcx
00AD1E2E  0F 82 E5 05 00 00               jb 0x140ad2419
00AD1E34  FF C2                           inc edx
00AD1E36  EB DA                           jmp 0x140ad1e12
00AD1E38  48 3B C8                        cmp rcx, rax
00AD1E3B  0F 82 D8 05 00 00               jb 0x140ad2419
00AD1E41  45 85 C9                        test r9d, r9d
00AD1E44  4C 8B FF                        mov r15, rdi
00AD1E47  4C 0F 45 F9                     cmovne r15, rcx
00AD1E4B  41 83 F9 04                     cmp r9d, 4
00AD1E4F  74 0A                           je 0x140ad1e5b
00AD1E51  BB 23 00 00 C0                  mov ebx, 0xc0000023
00AD1E56  E9 C3 05 00 00                  jmp 0x140ad241e
00AD1E5B  83 3B 05                        cmp dword ptr [rbx], 5
00AD1E5E  45 8B 3F                        mov r15d, dword ptr [r15]
00AD1E61  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00AD1E66  76 9B                           jbe 0x140ad1e03
00AD1E68  44 8B CF                        mov r9d, edi
00AD1E6B  41 8B 10                        mov edx, dword ptr [r8]
00AD1E6E  49 8D 48 04                     lea rcx, [r8 + 4]
00AD1E72  41 83 F9 05                     cmp r9d, 5
00AD1E76  73 1B                           jae 0x140ad1e93
00AD1E78  49 3B C8                        cmp rcx, r8
00AD1E7B  0F 82 98 05 00 00               jb 0x140ad2419
00AD1E81  4C 8D 04 11                     lea r8, [rcx + rdx]
00AD1E85  4C 3B C1                        cmp r8, rcx
00AD1E88  0F 82 8B 05 00 00               jb 0x140ad2419
00AD1E8E  41 FF C1                        inc r9d
00AD1E91  EB D8                           jmp 0x140ad1e6b
00AD1E93  49 3B C8                        cmp rcx, r8
00AD1E96  0F 82 7D 05 00 00               jb 0x140ad2419
00AD1E9C  85 D2                           test edx, edx
00AD1E9E  48 8B EF                        mov rbp, rdi
00AD1EA1  48 0F 45 E9                     cmovne rbp, rcx
00AD1EA5  74 34                           je 0x140ad1edb
00AD1EA7  F6 C2 01                        test dl, 1
00AD1EAA  75 2F                           jne 0x140ad1edb
00AD1EAC  48 8B C2                        mov rax, rdx
00AD1EAF  4C 8B DA                        mov r11, rdx
00AD1EB2  48 D1 E8                        shr rax, 1
00AD1EB5  66 3B 7C 45 FE                  cmp di, word ptr [rbp + rax*2 - 2]
00AD1EBA  75 1F                           jne 0x140ad1edb
00AD1EBC  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00AD1EC1  48 8B CD                        mov rcx, rbp
00AD1EC4  E8 97 6C 98 FF                  call 0x140458b60
00AD1EC9  85 C0                           test eax, eax
00AD1ECB  78 0E                           js 0x140ad1edb
00AD1ECD  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00AD1ED2  48 8D 41 02                     lea rax, [rcx + 2]
00AD1ED6  49 3B C3                        cmp rax, r11
00AD1ED9  74 0A                           je 0x140ad1ee5
00AD1EDB  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00AD1EE0  E9 39 05 00 00                  jmp 0x140ad241e
00AD1EE5  48 D1 E9                        shr rcx, 1
00AD1EE8  8D 0C 4D 02 00 00 00            lea ecx, [rcx*2 + 2]
00AD1EEF  85 C9                           test ecx, ecx
00AD1EF1  74 E8                           je 0x140ad1edb
00AD1EF3  44 8B E1                        mov r12d, ecx
00AD1EF6  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD1EFC  8B D1                           mov edx, ecx
00AD1EFE  B9 00 01 00 00                  mov ecx, 0x100
00AD1F03  E8 E8 01 0B 00                  call 0x140b820f0
00AD1F08  48 8B F8                        mov rdi, rax
00AD1F0B  48 85 C0                        test rax, rax
00AD1F0E  75 0A                           jne 0x140ad1f1a
00AD1F10  BB 17 00 00 C0                  mov ebx, 0xc0000017
00AD1F15  E9 04 05 00 00                  jmp 0x140ad241e
00AD1F1A  4D 8B C4                        mov r8, r12
00AD1F1D  48 8B D5                        mov rdx, rbp
00AD1F20  48 8B C8                        mov rcx, rax
00AD1F23  E8 18 49 BF FF                  call 0x1406c6840
00AD1F28  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00AD1F2C  48 85 D2                        test rdx, rdx
00AD1F2F  75 0A                           jne 0x140ad1f3b
00AD1F31  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD1F36  E9 A8 02 00 00                  jmp 0x140ad21e3
00AD1F3B  83 3B 06                        cmp dword ptr [rbx], 6
00AD1F3E  76 F1                           jbe 0x140ad1f31
00AD1F40  48 8B C2                        mov rax, rdx
00AD1F43  45 33 C0                        xor r8d, r8d
00AD1F46  44 8B 28                        mov r13d, dword ptr [rax]
00AD1F49  48 8D 48 04                     lea rcx, [rax + 4]
00AD1F4D  41 83 F8 06                     cmp r8d, 6
00AD1F51  73 1B                           jae 0x140ad1f6e
00AD1F53  48 3B C8                        cmp rcx, rax
00AD1F56  0F 82 7D 02 00 00               jb 0x140ad21d9
00AD1F5C  4A 8D 04 29                     lea rax, [rcx + r13]
00AD1F60  48 3B C1                        cmp rax, rcx
00AD1F63  0F 82 70 02 00 00               jb 0x140ad21d9
00AD1F69  41 FF C0                        inc r8d
00AD1F6C  EB D8                           jmp 0x140ad1f46
00AD1F6E  48 3B C8                        cmp rcx, rax
00AD1F71  0F 82 62 02 00 00               jb 0x140ad21d9
00AD1F77  45 33 E4                        xor r12d, r12d
00AD1F7A  45 85 ED                        test r13d, r13d
00AD1F7D  4C 0F 45 E1                     cmovne r12, rcx
00AD1F81  83 3B 07                        cmp dword ptr [rbx], 7
00AD1F84  77 0A                           ja 0x140ad1f90
00AD1F86  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD1F8B  E9 4E 02 00 00                  jmp 0x140ad21de
00AD1F90  48 8B C2                        mov rax, rdx
00AD1F93  45 33 C9                        xor r9d, r9d
00AD1F96  44 8B 00                        mov r8d, dword ptr [rax]
00AD1F99  48 8D 48 04                     lea rcx, [rax + 4]
00AD1F9D  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
00AD1FA2  41 83 F9 07                     cmp r9d, 7
00AD1FA6  73 1B                           jae 0x140ad1fc3
00AD1FA8  48 3B C8                        cmp rcx, rax
00AD1FAB  0F 82 28 02 00 00               jb 0x140ad21d9
00AD1FB1  4A 8D 04 01                     lea rax, [rcx + r8]
00AD1FB5  48 3B C1                        cmp rax, rcx
00AD1FB8  0F 82 1B 02 00 00               jb 0x140ad21d9
00AD1FBE  41 FF C1                        inc r9d
00AD1FC1  EB D3                           jmp 0x140ad1f96
00AD1FC3  48 3B C8                        cmp rcx, rax
00AD1FC6  0F 82 0D 02 00 00               jb 0x140ad21d9
00AD1FCC  33 C0                           xor eax, eax
00AD1FCE  45 85 C0                        test r8d, r8d
00AD1FD1  48 0F 45 C1                     cmovne rax, rcx
00AD1FD5  83 3B 08                        cmp dword ptr [rbx], 8
00AD1FD8  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00AD1FDD  76 A7                           jbe 0x140ad1f86
00AD1FDF  45 33 D2                        xor r10d, r10d
00AD1FE2  44 8B 1A                        mov r11d, dword ptr [rdx]
00AD1FE5  48 8D 4A 04                     lea rcx, [rdx + 4]
00AD1FE9  41 83 FA 08                     cmp r10d, 8
00AD1FED  73 25                           jae 0x140ad2014
00AD1FEF  48 3B CA                        cmp rcx, rdx
00AD1FF2  0F 82 E1 01 00 00               jb 0x140ad21d9
00AD1FF8  4A 8D 14 19                     lea rdx, [rcx + r11]
00AD1FFC  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
00AD2001  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00AD2006  48 3B D1                        cmp rdx, rcx
00AD2009  0F 82 CA 01 00 00               jb 0x140ad21d9
00AD200F  41 FF C2                        inc r10d
00AD2012  EB CE                           jmp 0x140ad1fe2
00AD2014  48 3B CA                        cmp rcx, rdx
00AD2017  0F 82 BC 01 00 00               jb 0x140ad21d9
00AD201D  33 ED                           xor ebp, ebp
00AD201F  45 85 DB                        test r11d, r11d
00AD2022  48 0F 45 E9                     cmovne rbp, rcx
00AD2026  41 83 FB 04                     cmp r11d, 4
00AD202A  74 0A                           je 0x140ad2036
00AD202C  BB 23 00 00 C0                  mov ebx, 0xc0000023
00AD2031  E9 A8 01 00 00                  jmp 0x140ad21de
00AD2036  8B 6D 00                        mov ebp, dword ptr [rbp]
00AD2039  85 ED                           test ebp, ebp
00AD203B  74 44                           je 0x140ad2081
00AD203D  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD2043  8B D5                           mov edx, ebp
00AD2045  B9 00 01 00 00                  mov ecx, 0x100
00AD204A  E8 A1 00 0B 00                  call 0x140b820f0
00AD204F  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00AD2054  48 85 C0                        test rax, rax
00AD2057  75 0D                           jne 0x140ad2066
00AD2059  BB 17 00 00 C0                  mov ebx, 0xc0000017
00AD205E  4C 8B E8                        mov r13, rax
00AD2061  E9 7D 01 00 00                  jmp 0x140ad21e3
00AD2066  4C 8B C5                        mov r8, rbp
00AD2069  33 D2                           xor edx, edx
00AD206B  48 8B C8                        mov rcx, rax
00AD206E  E8 CD 4B BF FF                  call 0x1406c6c40
00AD2073  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00AD2078  33 C9                           xor ecx, ecx
00AD207A  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
00AD207F  EB 05                           jmp 0x140ad2086
00AD2081  B9 01 00 00 00                  mov ecx, 1
00AD2086  4C 8B 15 03 63 50 00            mov r10, qword ptr [rip + 0x506303]
00AD208D  4D 85 D2                        test r10, r10
00AD2090  74 43                           je 0x140ad20d5
00AD2092  33 D2                           xor edx, edx
00AD2094  45 8B CD                        mov r9d, r13d
00AD2097  85 C9                           test ecx, ecx
00AD2099  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
00AD20A1  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00AD20A6  41 8B CF                        mov ecx, r15d
00AD20A9  48 0F 44 54 24 58               cmove rdx, qword ptr [rsp + 0x58]
00AD20AF  89 6C 24 38                     mov dword ptr [rsp + 0x38], ebp
00AD20B3  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00AD20B8  48 8B D7                        mov rdx, rdi
00AD20BB  44 89 44 24 28                  mov dword ptr [rsp + 0x28], r8d
00AD20C0  4D 8B C4                        mov r8, r12
00AD20C3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AD20C8  49 8B C2                        mov rax, r10
00AD20CB  E8 00 8A BE FF                  call 0x1406baad0
00AD20D0  44 8B F8                        mov r15d, eax
00AD20D3  EB 06                           jmp 0x140ad20db
00AD20D5  41 BF BB 00 00 C0               mov r15d, 0xc00000bb
00AD20DB  8D 45 04                        lea eax, [rbp + 4]
00AD20DE  83 F8 04                        cmp eax, 4
00AD20E1  0F 82 F2 00 00 00               jb 0x140ad21d9
00AD20E7  83 C0 14                        add eax, 0x14
00AD20EA  83 F8 14                        cmp eax, 0x14
00AD20ED  0F 82 E6 00 00 00               jb 0x140ad21d9
00AD20F3  8D 48 08                        lea ecx, [rax + 8]
00AD20F6  3B C8                           cmp ecx, eax
00AD20F8  0F 82 DB 00 00 00               jb 0x140ad21d9
00AD20FE  8D 41 08                        lea eax, [rcx + 8]
00AD2101  83 F8 08                        cmp eax, 8
00AD2104  0F 82 CF 00 00 00               jb 0x140ad21d9
00AD210A  48 8D 50 07                     lea rdx, [rax + 7]
00AD210E  83 E2 F8                        and edx, 0xfffffff8
00AD2111  3B D0                           cmp edx, eax
00AD2113  0F 82 C0 00 00 00               jb 0x140ad21d9
00AD2119  8D 42 08                        lea eax, [rdx + 8]
00AD211C  3B C2                           cmp eax, edx
00AD211E  0F 82 B5 00 00 00               jb 0x140ad21d9
00AD2124  4C 8B 84 24 B8 00 00 00         mov r8, qword ptr [rsp + 0xb8]
00AD212C  83 C0 04                        add eax, 4
00AD212F  45 8B 48 20                     mov r9d, dword ptr [r8 + 0x20]
00AD2133  45 8B 40 10                     mov r8d, dword ptr [r8 + 0x10]
00AD2137  83 F8 04                        cmp eax, 4
00AD213A  72 26                           jb 0x140ad2162
00AD213C  8D 50 04                        lea edx, [rax + 4]
00AD213F  3B D0                           cmp edx, eax
00AD2141  72 1F                           jb 0x140ad2162
00AD2143  41 8D 04 10                     lea eax, [r8 + rdx]
00AD2147  3B C2                           cmp eax, edx
00AD2149  72 17                           jb 0x140ad2162
00AD214B  8D 50 04                        lea edx, [rax + 4]
00AD214E  3B D0                           cmp edx, eax
00AD2150  72 10                           jb 0x140ad2162
00AD2152  41 8D 04 11                     lea eax, [r9 + rdx]
00AD2156  3B C2                           cmp eax, edx
00AD2158  1B DB                           sbb ebx, ebx
00AD215A  81 E3 95 00 00 C0               and ebx, 0xc0000095
00AD2160  EB 05                           jmp 0x140ad2167
00AD2162  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD2167  45 33 ED                        xor r13d, r13d
00AD216A  85 DB                           test ebx, ebx
00AD216C  78 70                           js 0x140ad21de
00AD216E  48 85 F6                        test rsi, rsi
00AD2171  0F 84 0F FE FF FF               je 0x140ad1f86
00AD2177  89 4E 04                        mov dword ptr [rsi + 4], ecx
00AD217A  41 8B DD                        mov ebx, r13d
00AD217D  85 C9                           test ecx, ecx
00AD217F  75 07                           jne 0x140ad2188
00AD2181  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00AD2186  EB 25                           jmp 0x140ad21ad
00AD2188  8B D1                           mov edx, ecx
00AD218A  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD2190  B9 00 01 00 00                  mov ecx, 0x100
00AD2195  E8 56 FF 0A 00                  call 0x140b820f0
00AD219A  48 85 C0                        test rax, rax
00AD219D  75 07                           jne 0x140ad21a6
00AD219F  BB 17 00 00 C0                  mov ebx, 0xc0000017
00AD21A4  EB 07                           jmp 0x140ad21ad
00AD21A6  48 89 46 08                     mov qword ptr [rsi + 8], rax
00AD21AA  44 89 2E                        mov dword ptr [rsi], r13d
00AD21AD  85 DB                           test ebx, ebx
00AD21AF  78 2D                           js 0x140ad21de
00AD21B1  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00AD21B5  41 0F BA EF 1C                  bts r15d, 0x1c
00AD21BA  48 85 D2                        test rdx, rdx
00AD21BD  75 4B                           jne 0x140ad220a
00AD21BF  8B 46 04                        mov eax, dword ptr [rsi + 4]
00AD21C2  8D 48 08                        lea ecx, [rax + 8]
00AD21C5  3B C8                           cmp ecx, eax
00AD21C7  72 0C                           jb 0x140ad21d5
00AD21C9  89 4E 04                        mov dword ptr [rsi + 4], ecx
00AD21CC  44 8D 62 01                     lea r12d, [rdx + 1]
00AD21D0  E9 89 00 00 00                  jmp 0x140ad225e
00AD21D5  83 4E 04 FF                     or dword ptr [rsi + 4], 0xffffffff
00AD21D9  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD21DE  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00AD21E3  48 85 FF                        test rdi, rdi
00AD21E6  74 0A                           je 0x140ad21f2
00AD21E8  33 D2                           xor edx, edx
00AD21EA  48 8B CF                        mov rcx, rdi
00AD21ED  E8 7E 06 0B 00                  call 0x140b82870
00AD21F2  4D 85 ED                        test r13, r13
00AD21F5  0F 84 23 02 00 00               je 0x140ad241e
00AD21FB  33 D2                           xor edx, edx
00AD21FD  49 8B CD                        mov rcx, r13
00AD2200  E8 6B 06 0B 00                  call 0x140b82870
00AD2205  E9 14 02 00 00                  jmp 0x140ad241e
00AD220A  44 8B 0E                        mov r9d, dword ptr [rsi]
00AD220D  41 8B CD                        mov ecx, r13d
00AD2210  41 BC 01 00 00 00               mov r12d, 1
00AD2216  41 3B C9                        cmp ecx, r9d
00AD2219  73 1D                           jae 0x140ad2238
00AD221B  8B 02                           mov eax, dword ptr [rdx]
00AD221D  83 C0 04                        add eax, 4
00AD2220  83 F8 04                        cmp eax, 4
00AD2223  72 B4                           jb 0x140ad21d9
00AD2225  44 8B C0                        mov r8d, eax
00AD2228  4C 03 C2                        add r8, rdx
00AD222B  4C 3B C2                        cmp r8, rdx
00AD222E  72 A9                           jb 0x140ad21d9
00AD2230  49 8B D0                        mov rdx, r8
00AD2233  41 03 CC                        add ecx, r12d
00AD2236  EB DE                           jmp 0x140ad2216
00AD2238  4C 8D 42 04                     lea r8, [rdx + 4]
00AD223C  4C 3B C2                        cmp r8, rdx
00AD223F  72 98                           jb 0x140ad21d9
00AD2241  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
00AD2244  48 8D 42 08                     lea rax, [rdx + 8]
00AD2248  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
00AD224C  48 3B C1                        cmp rax, rcx
00AD224F  0F 87 D7 FD FF FF               ja 0x140ad202c
00AD2255  C7 02 04 00 00 00               mov dword ptr [rdx], 4
00AD225B  45 89 38                        mov dword ptr [r8], r15d
00AD225E  44 01 26                        add dword ptr [rsi], r12d
00AD2261  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00AD2265  48 85 D2                        test rdx, rdx
00AD2268  75 13                           jne 0x140ad227d
00AD226A  8B 46 04                        mov eax, dword ptr [rsi + 4]
00AD226D  8D 48 0C                        lea ecx, [rax + 0xc]
00AD2270  3B C8                           cmp ecx, eax
00AD2272  0F 82 5D FF FF FF               jb 0x140ad21d5
00AD2278  89 4E 04                        mov dword ptr [rsi + 4], ecx
00AD227B  EB 5A                           jmp 0x140ad22d7
00AD227D  44 8B 0E                        mov r9d, dword ptr [rsi]
00AD2280  41 8B CD                        mov ecx, r13d
00AD2283  41 3B C9                        cmp ecx, r9d
00AD2286  73 25                           jae 0x140ad22ad
00AD2288  8B 02                           mov eax, dword ptr [rdx]
00AD228A  83 C0 04                        add eax, 4
00AD228D  83 F8 04                        cmp eax, 4
00AD2290  0F 82 43 FF FF FF               jb 0x140ad21d9
00AD2296  44 8B C0                        mov r8d, eax
00AD2299  4C 03 C2                        add r8, rdx
00AD229C  4C 3B C2                        cmp r8, rdx
00AD229F  0F 82 34 FF FF FF               jb 0x140ad21d9
00AD22A5  49 8B D0                        mov rdx, r8
00AD22A8  41 03 CC                        add ecx, r12d
00AD22AB  EB D6                           jmp 0x140ad2283
00AD22AD  4C 8D 42 04                     lea r8, [rdx + 4]
00AD22B1  4C 3B C2                        cmp r8, rdx
00AD22B4  0F 82 1F FF FF FF               jb 0x140ad21d9
00AD22BA  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
00AD22BD  48 8D 42 0C                     lea rax, [rdx + 0xc]
00AD22C1  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
00AD22C5  48 3B C1                        cmp rax, rcx
00AD22C8  0F 87 5E FD FF FF               ja 0x140ad202c
00AD22CE  C7 02 08 00 00 00               mov dword ptr [rdx], 8
00AD22D4  4D 89 30                        mov qword ptr [r8], r14
00AD22D7  44 01 26                        add dword ptr [rsi], r12d
00AD22DA  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
00AD22DF  4D 85 D2                        test r10, r10
00AD22E2  75 0B                           jne 0x140ad22ef
00AD22E4  85 ED                           test ebp, ebp
00AD22E6  74 0B                           je 0x140ad22f3
00AD22E8  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD22ED  EB 2D                           jmp 0x140ad231c
00AD22EF  85 ED                           test ebp, ebp
00AD22F1  74 F5                           je 0x140ad22e8
00AD22F3  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00AD22F7  48 85 D2                        test rdx, rdx
00AD22FA  75 28                           jne 0x140ad2324
00AD22FC  83 C5 04                        add ebp, 4
00AD22FF  83 FD 04                        cmp ebp, 4
00AD2302  72 13                           jb 0x140ad2317
00AD2304  8B 46 04                        mov eax, dword ptr [rsi + 4]
00AD2307  8D 0C 28                        lea ecx, [rax + rbp]
00AD230A  3B C8                           cmp ecx, eax
00AD230C  72 05                           jb 0x140ad2313
00AD230E  89 4E 04                        mov dword ptr [rsi + 4], ecx
00AD2311  EB 71                           jmp 0x140ad2384
00AD2313  83 4E 04 FF                     or dword ptr [rsi + 4], 0xffffffff
00AD2317  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD231C  4D 8B EA                        mov r13, r10
00AD231F  E9 BF FE FF FF                  jmp 0x140ad21e3
00AD2324  44 8B 0E                        mov r9d, dword ptr [rsi]
00AD2327  41 8B CD                        mov ecx, r13d
00AD232A  41 3B C9                        cmp ecx, r9d
00AD232D  73 1D                           jae 0x140ad234c
00AD232F  8B 02                           mov eax, dword ptr [rdx]
00AD2331  83 C0 04                        add eax, 4
00AD2334  83 F8 04                        cmp eax, 4
00AD2337  72 DE                           jb 0x140ad2317
00AD2339  44 8B C0                        mov r8d, eax
00AD233C  4C 03 C2                        add r8, rdx
00AD233F  4C 3B C2                        cmp r8, rdx
00AD2342  72 D3                           jb 0x140ad2317
00AD2344  49 8B D0                        mov rdx, r8
00AD2347  41 03 CC                        add ecx, r12d
00AD234A  EB DE                           jmp 0x140ad232a
00AD234C  4C 8D 4A 04                     lea r9, [rdx + 4]
00AD2350  4C 3B CA                        cmp r9, rdx
00AD2353  72 C2                           jb 0x140ad2317
00AD2355  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
00AD2358  48 8D 45 04                     lea rax, [rbp + 4]
00AD235C  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
00AD2360  48 03 C2                        add rax, rdx
00AD2363  44 8B C5                        mov r8d, ebp
00AD2366  48 3B C1                        cmp rax, rcx
00AD2369  76 07                           jbe 0x140ad2372
00AD236B  BB 23 00 00 C0                  mov ebx, 0xc0000023
00AD2370  EB AA                           jmp 0x140ad231c
00AD2372  89 2A                           mov dword ptr [rdx], ebp
00AD2374  4D 85 D2                        test r10, r10
00AD2377  74 0B                           je 0x140ad2384
00AD2379  49 8B D2                        mov rdx, r10
00AD237C  49 8B C9                        mov rcx, r9
00AD237F  E8 BC 44 BF FF                  call 0x1406c6840
00AD2384  44 01 26                        add dword ptr [rsi], r12d
00AD2387  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00AD238B  44 8B 84 24 C0 00 00 00         mov r8d, dword ptr [rsp + 0xc0]
00AD2393  48 85 D2                        test rdx, rdx
00AD2396  75 1C                           jne 0x140ad23b4
00AD2398  8B 46 04                        mov eax, dword ptr [rsi + 4]
00AD239B  8D 48 08                        lea ecx, [rax + 8]
00AD239E  3B C8                           cmp ecx, eax
00AD23A0  0F 82 2F FE FF FF               jb 0x140ad21d5
00AD23A6  44 01 26                        add dword ptr [rsi], r12d
00AD23A9  41 8B DD                        mov ebx, r13d
00AD23AC  89 4E 04                        mov dword ptr [rsi + 4], ecx
00AD23AF  E9 2A FE FF FF                  jmp 0x140ad21de
00AD23B4  44 8B 16                        mov r10d, dword ptr [rsi]
00AD23B7  41 8B CD                        mov ecx, r13d
00AD23BA  41 3B CA                        cmp ecx, r10d
00AD23BD  73 25                           jae 0x140ad23e4
00AD23BF  8B 02                           mov eax, dword ptr [rdx]
00AD23C1  83 C0 04                        add eax, 4
00AD23C4  83 F8 04                        cmp eax, 4
00AD23C7  0F 82 0C FE FF FF               jb 0x140ad21d9
00AD23CD  44 8B C8                        mov r9d, eax
00AD23D0  4C 03 CA                        add r9, rdx
00AD23D3  4C 3B CA                        cmp r9, rdx
00AD23D6  0F 82 FD FD FF FF               jb 0x140ad21d9
00AD23DC  49 8B D1                        mov rdx, r9
00AD23DF  41 03 CC                        add ecx, r12d
00AD23E2  EB D6                           jmp 0x140ad23ba
00AD23E4  4C 8D 4A 04                     lea r9, [rdx + 4]
00AD23E8  4C 3B CA                        cmp r9, rdx
00AD23EB  0F 82 E8 FD FF FF               jb 0x140ad21d9
00AD23F1  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
00AD23F4  48 8D 42 08                     lea rax, [rdx + 8]
00AD23F8  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
00AD23FC  41 8B DD                        mov ebx, r13d
00AD23FF  48 3B C1                        cmp rax, rcx
00AD2402  0F 87 24 FC FF FF               ja 0x140ad202c
00AD2408  C7 02 04 00 00 00               mov dword ptr [rdx], 4
00AD240E  45 89 01                        mov dword ptr [r9], r8d
00AD2411  44 01 26                        add dword ptr [rsi], r12d
00AD2414  E9 C5 FD FF FF                  jmp 0x140ad21de
00AD2419  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD241E  8B C3                           mov eax, ebx
00AD2420  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
00AD2428  48 83 C4 70                     add rsp, 0x70
00AD242C  41 5F                           pop r15
00AD242E  41 5E                           pop r14
00AD2430  41 5D                           pop r13
00AD2432  41 5C                           pop r12
00AD2434  5F                              pop rdi
00AD2435  5E                              pop rsi
00AD2436  5D                              pop rbp
00AD2437  C3                              ret
00AD2438  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00AD1D78(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (112);
    v_rdi = 0;
    v_stack_m50 = 0;
    *(unsigned int *)(v_rsp + 24) = 0;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00AD1E03;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_00AD1E03;
loc_00AD1DBC:
    if (0 >= 3) goto loc_00AD1DE2;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD2419;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD2419;
    a2 = (unsigned int)((0) + 1);
    goto loc_00AD1DBC;
loc_00AD1DE2:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD2419;
    v_r14 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r14 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_00AD1E51;
    if ((*(unsigned int *)(a1)) > 4) goto loc_00AD1E0D;
loc_00AD1E03:
    goto loc_00AD241E;
loc_00AD1E0D:
loc_00AD1E12:
    if (0 >= 4) goto loc_00AD1E38;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD2419;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD2419;
    a2 = (unsigned int)((0) + 1);
    goto loc_00AD1E12;
loc_00AD1E38:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD2419;
    v_r15 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r15 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) == 4) goto loc_00AD1E5B;
loc_00AD1E51:
    goto loc_00AD241E;
loc_00AD1E5B:
    v_stack_m48 = 0;
    if ((*(unsigned int *)((unsigned int)(0xC0000023ULL))) <= 5) goto loc_00AD1E03;
loc_00AD1E6B:
    if (0 >= 5) goto loc_00AD1E93;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD2419;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD2419;
    a4 = (unsigned int)((0) + 1);
    goto loc_00AD1E6B;
loc_00AD1E93:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD2419;
    v_rbp = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rbp = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) == 0) goto loc_00AD1EDB;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) & (1)) != 0) goto loc_00AD1EDB;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) >> (1);
    if (0 != (*(unsigned __int16 *)(v_rbp + result * 2 - 2))) goto loc_00AD1EDB;
    result = StringCbLengthW(v_rbp, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))), v_stack_m48, a4);
    if (sign_flag) goto loc_00AD1EDB;
    if ((v_stack_m48 + 2) == ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) goto loc_00AD1EE5;
loc_00AD1EDB:
    goto loc_00AD241E;
loc_00AD1EE5:
    a1 = (v_stack_m48) >> (1);
    if ((unsigned int)(a1 * 2 + 2) == 0) goto loc_00AD1EDB;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(a1 * 2 + 2)), (unsigned int)(0x20534C53ULL), a4);
    if (result != 0) goto loc_00AD1F1A;
    goto loc_00AD241E;
loc_00AD1F1A:
    result = memcpy(result, v_rbp, (unsigned int)((unsigned int)(a1 * 2 + 2)), a4);
    if (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) != 0) goto loc_00AD1F3B;
loc_00AD1F31:
    goto loc_00AD21E3;
loc_00AD1F3B:
    if ((*(unsigned int *)((unsigned int)(0xC000000DULL))) <= 6) goto loc_00AD1F31;
    a3 = 0;
loc_00AD1F46:
    if (0 >= 6) goto loc_00AD1F6E;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) goto loc_00AD21D9;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4)) goto loc_00AD21D9;
    a3 = (unsigned int)((a3) + 1);
    goto loc_00AD1F46;
loc_00AD1F6E:
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1)) goto loc_00AD21D9;
    v_r12 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8)))) != 0) { v_r12 = *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4; }
    if ((*(unsigned int *)((unsigned int)(0xC000000DULL))) > 7) goto loc_00AD1F90;
loc_00AD1F86:
    goto loc_00AD21DE;
loc_00AD1F90:
    a4 = 0;
loc_00AD1F96:
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))));
    if (0 >= 7) goto loc_00AD1FC3;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) goto loc_00AD21D9;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4)) goto loc_00AD21D9;
    a4 = (unsigned int)((a4) + 1);
    goto loc_00AD1F96;
loc_00AD1FC3:
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1)) goto loc_00AD21D9;
    result = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8)))) != 0) { result = *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4; }
    v_stack_m48 = result;
    if ((*(unsigned int *)((unsigned int)(0xC000000DULL))) <= 8) goto loc_00AD1F86;
    v_r10 = 0;
loc_00AD1FE2:
    if (0 >= 8) goto loc_00AD2014;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) goto loc_00AD21D9;
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))));
    v_stack_m48 = result;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4)) goto loc_00AD21D9;
    v_r10 = (unsigned int)((v_r10) + 1);
    goto loc_00AD1FE2;
loc_00AD2014:
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1)) goto loc_00AD21D9;
    v_rbp = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8)))) != 0) { v_rbp = *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))))) == 4) goto loc_00AD2036;
loc_00AD202C:
    goto loc_00AD21DE;
loc_00AD2036:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp))) == 0) goto loc_00AD2081;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp)))), (unsigned int)(0x20534C53ULL), a4);
    v_stack_m50 = result;
    if (result != 0) goto loc_00AD2066;
    goto loc_00AD21E3;
loc_00AD2066:
    a2 = 0;
    result = memset(result, a2, (unsigned int)(*(unsigned int *)(v_rbp)), a4);
    a1 = 0;
    goto loc_00AD2086;
loc_00AD2081:
loc_00AD2086:
    if (*(unsigned __int64 *)(v_rip + 5268227) == 0) goto loc_00AD20D5;
    a2 = 0;
    v_stack_m68 = v_stack_p18;
    if (1 == 0) { a2 = v_stack_m50; }
    v_stack_m70 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp)));
    v_stack_m78 = a2;
    v_stack_m80 = (unsigned int)((unsigned int)(v_stack_m58));
    v_stack_m88 = v_stack_m48;
    result = guard_dispatch_icall((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r15)))), result, v_r12, (unsigned int)((unsigned int)(result)));
    goto loc_00AD20DB;
loc_00AD20D5:
loc_00AD20DB:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp)) + 4)) < 4) goto loc_00AD21D9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp)) + 4) + (20));
    if (((unsigned int)(result)) < 20) goto loc_00AD21D9;
    if (((unsigned int)(result + 8)) < ((unsigned int)(result))) goto loc_00AD21D9;
    if (((unsigned int)(result + 8 + 8)) < 8) goto loc_00AD21D9;
    a2 = (unsigned int)((result + 8 + 8 + 7) & (0xFFFFFFF8ULL));
    if (((unsigned int)(a2)) < ((unsigned int)(result + 8 + 8))) goto loc_00AD21D9;
    if (((unsigned int)(a2 + 8)) < ((unsigned int)(a2))) goto loc_00AD21D9;
    result = (unsigned int)((a2 + 8) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD2162;
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_00AD2162;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 16)) + result + 4 * 1)) < ((unsigned int)(result + 4))) goto loc_00AD2162;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 16)) + result + 4 * 1 + 4)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 16)) + result + 4 * 1))) goto loc_00AD2162;
    v_rbx = (unsigned int)(((unsigned int)(0xC0000017ULL)) & (0xC0000095ULL));
    goto loc_00AD2167;
loc_00AD2162:
loc_00AD2167:
    v_r13 = 0;
    if (sign_flag) goto loc_00AD21DE;
    if (a4 == 0) goto loc_00AD1F86;
    *(unsigned int *)(a4 + 4) = (unsigned int)(result + 8);
    if ((unsigned int)(result + 8) != 0) goto loc_00AD2188;
    goto loc_00AD21AD;
loc_00AD2188:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result + 8)), (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(v_stack_p10 + 32)));
    if (result != 0) goto loc_00AD21A6;
    goto loc_00AD21AD;
loc_00AD21A6:
    *(unsigned __int64 *)(a4 + 8) = result;
    *(unsigned int *)(a4) = 0;
loc_00AD21AD:
    if (sign_flag) goto loc_00AD21DE;
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD220A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD21D5;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00AD225E;
loc_00AD21D5:
loc_00AD21D9:
loc_00AD21DE:
loc_00AD21E3:
    result = (unsigned int)(*(unsigned int *)(a4 + 4));
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(v_stack_p10 + 32)));
    }
    if (v_stack_m50 == 0) goto loc_00AD241E;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m50, a2, (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(v_stack_p10 + 32)));
    goto loc_00AD241E;
loc_00AD220A:
loc_00AD2216:
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_m50)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD2238;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD21D9;
    a3 = ((unsigned int)((unsigned int)(result))) + (0);
    if (a3 < 0) goto loc_00AD21D9;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m50))) + (1));
    goto loc_00AD2216;
loc_00AD2238:
    if ((a3 + 4) < a3) goto loc_00AD21D9;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_00AD202C;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)(0xC00000BBULL));
loc_00AD225E:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD227D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD21D5;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12);
    goto loc_00AD22D7;
loc_00AD227D:
loc_00AD2283:
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_m50)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD22AD;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD21D9;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00AD21D9;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m50))) + (1));
    goto loc_00AD2283;
loc_00AD22AD:
    if ((a3 + 4) < a3) goto loc_00AD21D9;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) > a1) goto loc_00AD202C;
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)(a3 + 4) = *(unsigned __int64 *)(v_r14);
loc_00AD22D7:
    if (v_stack_m50 != 0) goto loc_00AD22EF;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp))) == 0) goto loc_00AD22F3;
loc_00AD22E8:
    goto loc_00AD231C;
loc_00AD22EF:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp))) == 0) goto loc_00AD22E8;
loc_00AD22F3:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD2324;
    v_rbp = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp))) + (4));
    if (((unsigned int)(v_rbp)) < 4) goto loc_00AD2317;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + v_rbp * 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD2313;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + v_rbp * 1);
    goto loc_00AD2384;
loc_00AD2313:
loc_00AD2317:
loc_00AD231C:
    goto loc_00AD21E3;
loc_00AD2324:
loc_00AD232A:
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_m50)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD234C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD2317;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00AD2317;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m50))) + (1));
    goto loc_00AD232A;
loc_00AD234C:
    if ((a3 + 4) < a3) goto loc_00AD2317;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    result = (v_rbp + 4) + (a3);
    if (result <= a1) goto loc_00AD2372;
    goto loc_00AD231C;
loc_00AD2372:
    *(unsigned int *)(a3) = (unsigned int)(v_rbp);
    if (v_stack_m50 != 0) {
        a2 = v_stack_m50;
        a1 = a3 + 4;
        result = memcpy(a1, a2, (unsigned int)((unsigned int)(v_rbp)), a3 + 4);
    }
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD23B4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD21D5;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00AD21DE;
loc_00AD23B4:
loc_00AD23BA:
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_m50)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD23E4;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD21D9;
    a4 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a4 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00AD21D9;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m50))) + (1));
    goto loc_00AD23BA;
loc_00AD23E4:
    if ((a4 + 4) < a4) goto loc_00AD21D9;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a4 + 8) > a1) goto loc_00AD202C;
    *(unsigned int *)(a4) = 4;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(v_stack_p18));
    goto loc_00AD21DE;
loc_00AD2419:
loc_00AD241E:
    v_rsp = (v_rsp) + (112);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_00AD1D78(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (112);
    local_rdi = 0;
    v_stack_m50 = 0;
    *(uint32_t *)(local_rsp + 0x18) = 0;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00AD1E03;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_00AD1E03;
loc_00AD1DBC:
    if (0 >= 3) goto loc_00AD1DE2;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD2419;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD2419;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00AD1DBC;
loc_00AD1DE2:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD2419;
    local_r14 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r14 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_00AD1E51;
    if ((*(uint32_t *)(arg1)) > 4) goto loc_00AD1E0D;
loc_00AD1E03:
    goto loc_00AD241E;
loc_00AD1E0D:
loc_00AD1E12:
    if (0 >= 4) goto loc_00AD1E38;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD2419;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD2419;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00AD1E12;
loc_00AD1E38:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD2419;
    local_r15 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r15 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) == 4) goto loc_00AD1E5B;
loc_00AD1E51:
    goto loc_00AD241E;
loc_00AD1E5B:
    v_stack_m48 = 0;
    if ((*(uint32_t *)((uint32_t)(0xC0000023ULL))) <= 5) goto loc_00AD1E03;
loc_00AD1E6B:
    if (0 >= 5) goto loc_00AD1E93;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD2419;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD2419;
    Arg4 = (uint32_t)((0) + 1);
    goto loc_00AD1E6B;
loc_00AD1E93:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD2419;
    local_rbp = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rbp = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) == 0) goto loc_00AD1EDB;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) & (1)) != 0) goto loc_00AD1EDB;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) >> (1);
    if (0 != (*(uint16_t *)(local_rbp + result * 2 - 0x2))) goto loc_00AD1EDB;
    result = StringCbLengthW(local_rbp, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))), v_stack_m48, Arg4);
    if (sign_flag) goto loc_00AD1EDB;
    if ((v_stack_m48 + 2) == ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) goto loc_00AD1EE5;
loc_00AD1EDB:
    goto loc_00AD241E;
loc_00AD1EE5:
    Arg1 = (v_stack_m48) >> (1);
    if ((uint32_t)(Arg1 * 2 + 2) == 0) goto loc_00AD1EDB;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(Arg1 * 2 + 2)), (uint32_t)(0x20534C53ULL), Arg4);
    if (result != 0) goto loc_00AD1F1A;
    goto loc_00AD241E;
loc_00AD1F1A:
    result = memcpy(result, local_rbp, (uint32_t)((uint32_t)(Arg1 * 2 + 2)), Arg4);
    if (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) != 0) goto loc_00AD1F3B;
loc_00AD1F31:
    goto loc_00AD21E3;
loc_00AD1F3B:
    if ((*(uint32_t *)((uint32_t)(0xC000000DULL))) <= 6) goto loc_00AD1F31;
    Arg3 = 0;
loc_00AD1F46:
    if (0 >= 6) goto loc_00AD1F6E;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) goto loc_00AD21D9;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4)) goto loc_00AD21D9;
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_00AD1F46;
loc_00AD1F6E:
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1)) goto loc_00AD21D9;
    local_r12 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8)))) != 0) { local_r12 = *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4; }
    if ((*(uint32_t *)((uint32_t)(0xC000000DULL))) > 7) goto loc_00AD1F90;
loc_00AD1F86:
    goto loc_00AD21DE;
loc_00AD1F90:
    Arg4 = 0;
loc_00AD1F96:
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))));
    if (0 >= 7) goto loc_00AD1FC3;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) goto loc_00AD21D9;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4)) goto loc_00AD21D9;
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_00AD1F96;
loc_00AD1FC3:
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1)) goto loc_00AD21D9;
    result = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8)))) != 0) { result = *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4; }
    v_stack_m48 = result;
    if ((*(uint32_t *)((uint32_t)(0xC000000DULL))) <= 8) goto loc_00AD1F86;
    local_r10 = 0;
loc_00AD1FE2:
    if (0 >= 8) goto loc_00AD2014;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) goto loc_00AD21D9;
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))));
    v_stack_m48 = result;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4)) goto loc_00AD21D9;
    local_r10 = (uint32_t)((local_r10) + 1);
    goto loc_00AD1FE2;
loc_00AD2014:
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1)) goto loc_00AD21D9;
    local_rbp = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8)))) != 0) { local_rbp = *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))))) == 4) goto loc_00AD2036;
loc_00AD202C:
    goto loc_00AD21DE;
loc_00AD2036:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp))) == 0) goto loc_00AD2081;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp)))), (uint32_t)(0x20534C53ULL), Arg4);
    v_stack_m50 = result;
    if (result != 0) goto loc_00AD2066;
    goto loc_00AD21E3;
loc_00AD2066:
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(*(uint32_t *)(local_rbp)), Arg4);
    Arg1 = 0;
    goto loc_00AD2086;
loc_00AD2081:
loc_00AD2086:
    if (*(uint64_t *)(v_rip + 0x506303) == 0) goto loc_00AD20D5;
    Arg2 = 0;
    v_stack_m68 = v_stack_p18;
    if (1 == 0) { Arg2 = v_stack_m50; }
    v_stack_m70 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp)));
    v_stack_m78 = Arg2;
    v_stack_m80 = (uint32_t)((uint32_t)(v_stack_m58));
    v_stack_m88 = v_stack_m48;
    result = guard_dispatch_icall((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r15)))), result, local_r12, (uint32_t)((uint32_t)(result)));
    goto loc_00AD20DB;
loc_00AD20D5:
loc_00AD20DB:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp)) + 4)) < 4) goto loc_00AD21D9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp)) + 4) + (20));
    if (((uint32_t)(result)) < 20) goto loc_00AD21D9;
    if (((uint32_t)(result + 8)) < ((uint32_t)(result))) goto loc_00AD21D9;
    if (((uint32_t)(result + 8 + 8)) < 8) goto loc_00AD21D9;
    Arg2 = (uint32_t)((result + 8 + 8 + 7) & (0xFFFFFFF8ULL));
    if (((uint32_t)(Arg2)) < ((uint32_t)(result + 8 + 8))) goto loc_00AD21D9;
    if (((uint32_t)(Arg2 + 8)) < ((uint32_t)(Arg2))) goto loc_00AD21D9;
    result = (uint32_t)((Arg2 + 8) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD2162;
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_00AD2162;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x10)) + result + 4 * 1)) < ((uint32_t)(result + 4))) goto loc_00AD2162;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x10)) + result + 4 * 1 + 4)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x10)) + result + 4 * 1))) goto loc_00AD2162;
    local_rbx = (uint32_t)(((uint32_t)(0xC0000017ULL)) & (0xC0000095ULL));
    goto loc_00AD2167;
loc_00AD2162:
loc_00AD2167:
    local_r13 = 0;
    if (sign_flag) goto loc_00AD21DE;
    if (Arg4 == 0) goto loc_00AD1F86;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(result + 8);
    if ((uint32_t)(result + 8) != 0) goto loc_00AD2188;
    goto loc_00AD21AD;
loc_00AD2188:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result + 8)), (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20)));
    if (result != 0) goto loc_00AD21A6;
    goto loc_00AD21AD;
loc_00AD21A6:
    *(uint64_t *)(Arg4 + 0x8) = result;
    *(uint32_t *)(Arg4) = 0;
loc_00AD21AD:
    if (sign_flag) goto loc_00AD21DE;
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD220A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD21D5;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_00AD225E;
loc_00AD21D5:
loc_00AD21D9:
loc_00AD21DE:
loc_00AD21E3:
    result = (uint32_t)(*(uint32_t *)(Arg4 + 0x4));
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20)));
    }
    if (v_stack_m50 == 0) goto loc_00AD241E;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m50, Arg2, (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20)));
    goto loc_00AD241E;
loc_00AD220A:
loc_00AD2216:
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_m50)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD2238;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD21D9;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (0);
    if (Arg3 < 0) goto loc_00AD21D9;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m50))) + (1));
    goto loc_00AD2216;
loc_00AD2238:
    if ((Arg3 + 4) < Arg3) goto loc_00AD21D9;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_00AD202C;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)(0xC00000BBULL));
loc_00AD225E:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD227D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD21D5;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12);
    goto loc_00AD22D7;
loc_00AD227D:
loc_00AD2283:
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_m50)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD22AD;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD21D9;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00AD21D9;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m50))) + (1));
    goto loc_00AD2283;
loc_00AD22AD:
    if ((Arg3 + 4) < Arg3) goto loc_00AD21D9;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 12) > Arg1) goto loc_00AD202C;
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)(Arg3 + 0x4) = *(uint64_t *)(local_r14);
loc_00AD22D7:
    if (v_stack_m50 != 0) goto loc_00AD22EF;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp))) == 0) goto loc_00AD22F3;
loc_00AD22E8:
    goto loc_00AD231C;
loc_00AD22EF:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp))) == 0) goto loc_00AD22E8;
loc_00AD22F3:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD2324;
    local_rbp = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp))) + (4));
    if (((uint32_t)(local_rbp)) < 4) goto loc_00AD2317;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + local_rbp * 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD2313;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + local_rbp * 1);
    goto loc_00AD2384;
loc_00AD2313:
loc_00AD2317:
loc_00AD231C:
    goto loc_00AD21E3;
loc_00AD2324:
loc_00AD232A:
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_m50)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD234C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD2317;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00AD2317;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m50))) + (1));
    goto loc_00AD232A;
loc_00AD234C:
    if ((Arg3 + 4) < Arg3) goto loc_00AD2317;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    result = (local_rbp + 4) + (Arg3);
    if (result <= Arg1) goto loc_00AD2372;
    goto loc_00AD231C;
loc_00AD2372:
    *(uint32_t *)(Arg3) = (uint32_t)(local_rbp);
    if (v_stack_m50 != 0) {
        Arg2 = v_stack_m50;
        Arg1 = Arg3 + 4;
        result = memcpy(Arg1, Arg2, (uint32_t)((uint32_t)(local_rbp)), Arg3 + 4);
    }
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD23B4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD21D5;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_00AD21DE;
loc_00AD23B4:
loc_00AD23BA:
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_m50)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD23E4;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD21D9;
    Arg4 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg4 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00AD21D9;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m50))) + (1));
    goto loc_00AD23BA;
loc_00AD23E4:
    if ((Arg4 + 4) < Arg4) goto loc_00AD21D9;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg4 + 8) > Arg1) goto loc_00AD202C;
    *(uint32_t *)(Arg4) = 4;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(v_stack_p18));
    goto loc_00AD21DE;
loc_00AD2419:
loc_00AD241E:
    local_rsp = (local_rsp) + (112);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AD1D78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
