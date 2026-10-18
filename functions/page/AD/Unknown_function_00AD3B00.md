# sub_00AD3B00

- RVA: `0x00AD3B00`–`0x00AD409E` (길이 `1,438` bytes)
- VA: `0x0000000140AD3B00`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BEBC0`
- 디코드: `423`개 명령, `1,438/1,438` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AD3CD7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD3CF8` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AD3D47` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AD3E16` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD3E6B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AD3FEA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x0096A7FF`

### Static image references
- `0x00AD3D0B` → RVA `0x00FD83E0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00AD3CD7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD3CF8` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AD3D47` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AD3E16` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD3E6B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AD3FEA` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AD3B00  48 8B C4                        mov rax, rsp
00AD3B03  48 89 58 08                     mov qword ptr [rax + 8], rbx
00AD3B07  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00AD3B0B  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00AD3B0F  55                              push rbp
00AD3B10  56                              push rsi
00AD3B11  57                              push rdi
00AD3B12  41 54                           push r12
00AD3B14  41 55                           push r13
00AD3B16  41 56                           push r14
00AD3B18  41 57                           push r15
00AD3B1A  48 83 EC 60                     sub rsp, 0x60
00AD3B1E  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
00AD3B22  45 33 DB                        xor r11d, r11d
00AD3B25  44 21 58 18                     and dword ptr [rax + 0x18], r11d
00AD3B29  49 8B F9                        mov rdi, r9
00AD3B2C  4C 89 5C 24 50                  mov qword ptr [rsp + 0x50], r11
00AD3B31  4C 8B C9                        mov r9, rcx
00AD3B34  4D 85 C0                        test r8, r8
00AD3B37  0F 84 F1 00 00 00               je 0x140ad3c2e
00AD3B3D  83 39 03                        cmp dword ptr [rcx], 3
00AD3B40  0F 86 E8 00 00 00               jbe 0x140ad3c2e
00AD3B46  49 8B C0                        mov rax, r8
00AD3B49  33 D2                           xor edx, edx
00AD3B4B  44 8B 10                        mov r10d, dword ptr [rax]
00AD3B4E  48 8D 48 04                     lea rcx, [rax + 4]
00AD3B52  83 FA 03                        cmp edx, 3
00AD3B55  73 1A                           jae 0x140ad3b71
00AD3B57  48 3B C8                        cmp rcx, rax
00AD3B5A  0F 82 1E 05 00 00               jb 0x140ad407e
00AD3B60  4A 8D 04 11                     lea rax, [rcx + r10]
00AD3B64  48 3B C1                        cmp rax, rcx
00AD3B67  0F 82 11 05 00 00               jb 0x140ad407e
00AD3B6D  FF C2                           inc edx
00AD3B6F  EB DA                           jmp 0x140ad3b4b
00AD3B71  48 3B C8                        cmp rcx, rax
00AD3B74  0F 82 04 05 00 00               jb 0x140ad407e
00AD3B7A  33 ED                           xor ebp, ebp
00AD3B7C  45 85 D2                        test r10d, r10d
00AD3B7F  48 0F 45 E9                     cmovne rbp, rcx
00AD3B83  41 83 FA 08                     cmp r10d, 8
00AD3B87  0F 85 2D 01 00 00               jne 0x140ad3cba
00AD3B8D  41 83 39 04                     cmp dword ptr [r9], 4
00AD3B91  48 8B 6D 00                     mov rbp, qword ptr [rbp]
00AD3B95  0F 86 93 00 00 00               jbe 0x140ad3c2e
00AD3B9B  49 8B C0                        mov rax, r8
00AD3B9E  33 D2                           xor edx, edx
00AD3BA0  44 8B 10                        mov r10d, dword ptr [rax]
00AD3BA3  48 8D 48 04                     lea rcx, [rax + 4]
00AD3BA7  83 FA 04                        cmp edx, 4
00AD3BAA  73 1A                           jae 0x140ad3bc6
00AD3BAC  48 3B C8                        cmp rcx, rax
00AD3BAF  0F 82 C9 04 00 00               jb 0x140ad407e
00AD3BB5  4A 8D 04 11                     lea rax, [rcx + r10]
00AD3BB9  48 3B C1                        cmp rax, rcx
00AD3BBC  0F 82 BC 04 00 00               jb 0x140ad407e
00AD3BC2  FF C2                           inc edx
00AD3BC4  EB DA                           jmp 0x140ad3ba0
00AD3BC6  48 3B C8                        cmp rcx, rax
00AD3BC9  0F 82 AF 04 00 00               jb 0x140ad407e
00AD3BCF  45 33 FF                        xor r15d, r15d
00AD3BD2  45 85 D2                        test r10d, r10d
00AD3BD5  4C 0F 45 F9                     cmovne r15, rcx
00AD3BD9  41 83 FA 04                     cmp r10d, 4
00AD3BDD  0F 85 D7 00 00 00               jne 0x140ad3cba
00AD3BE3  41 83 39 05                     cmp dword ptr [r9], 5
00AD3BE7  45 8B 3F                        mov r15d, dword ptr [r15]
00AD3BEA  76 42                           jbe 0x140ad3c2e
00AD3BEC  49 8B C0                        mov rax, r8
00AD3BEF  33 D2                           xor edx, edx
00AD3BF1  8B 18                           mov ebx, dword ptr [rax]
00AD3BF3  48 8D 48 04                     lea rcx, [rax + 4]
00AD3BF7  83 FA 05                        cmp edx, 5
00AD3BFA  73 1A                           jae 0x140ad3c16
00AD3BFC  48 3B C8                        cmp rcx, rax
00AD3BFF  0F 82 79 04 00 00               jb 0x140ad407e
00AD3C05  48 8D 04 19                     lea rax, [rcx + rbx]
00AD3C09  48 3B C1                        cmp rax, rcx
00AD3C0C  0F 82 6C 04 00 00               jb 0x140ad407e
00AD3C12  FF C2                           inc edx
00AD3C14  EB DB                           jmp 0x140ad3bf1
00AD3C16  48 3B C8                        cmp rcx, rax
00AD3C19  0F 82 5F 04 00 00               jb 0x140ad407e
00AD3C1F  45 33 F6                        xor r14d, r14d
00AD3C22  85 DB                           test ebx, ebx
00AD3C24  4C 0F 45 F1                     cmovne r14, rcx
00AD3C28  41 83 39 06                     cmp dword ptr [r9], 6
00AD3C2C  77 0A                           ja 0x140ad3c38
00AD3C2E  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD3C33  E9 4B 04 00 00                  jmp 0x140ad4083
00AD3C38  49 8B C0                        mov rax, r8
00AD3C3B  33 D2                           xor edx, edx
00AD3C3D  44 8B 28                        mov r13d, dword ptr [rax]
00AD3C40  48 8D 48 04                     lea rcx, [rax + 4]
00AD3C44  83 FA 06                        cmp edx, 6
00AD3C47  73 1A                           jae 0x140ad3c63
00AD3C49  48 3B C8                        cmp rcx, rax
00AD3C4C  0F 82 2C 04 00 00               jb 0x140ad407e
00AD3C52  4A 8D 04 29                     lea rax, [rcx + r13]
00AD3C56  48 3B C1                        cmp rax, rcx
00AD3C59  0F 82 1F 04 00 00               jb 0x140ad407e
00AD3C5F  FF C2                           inc edx
00AD3C61  EB DA                           jmp 0x140ad3c3d
00AD3C63  48 3B C8                        cmp rcx, rax
00AD3C66  0F 82 12 04 00 00               jb 0x140ad407e
00AD3C6C  45 33 E4                        xor r12d, r12d
00AD3C6F  45 85 ED                        test r13d, r13d
00AD3C72  4C 0F 45 E1                     cmovne r12, rcx
00AD3C76  41 83 39 07                     cmp dword ptr [r9], 7
00AD3C7A  76 B2                           jbe 0x140ad3c2e
00AD3C7C  33 D2                           xor edx, edx
00AD3C7E  41 8B 00                        mov eax, dword ptr [r8]
00AD3C81  49 8D 48 04                     lea rcx, [r8 + 4]
00AD3C85  83 FA 07                        cmp edx, 7
00AD3C88  73 1A                           jae 0x140ad3ca4
00AD3C8A  49 3B C8                        cmp rcx, r8
00AD3C8D  0F 82 EB 03 00 00               jb 0x140ad407e
00AD3C93  4C 8D 04 01                     lea r8, [rcx + rax]
00AD3C97  4C 3B C1                        cmp r8, rcx
00AD3C9A  0F 82 DE 03 00 00               jb 0x140ad407e
00AD3CA0  FF C2                           inc edx
00AD3CA2  EB DA                           jmp 0x140ad3c7e
00AD3CA4  49 3B C8                        cmp rcx, r8
00AD3CA7  0F 82 D1 03 00 00               jb 0x140ad407e
00AD3CAD  33 F6                           xor esi, esi
00AD3CAF  85 C0                           test eax, eax
00AD3CB1  48 0F 45 F1                     cmovne rsi, rcx
00AD3CB5  83 F8 04                        cmp eax, 4
00AD3CB8  74 0A                           je 0x140ad3cc4
00AD3CBA  BB 23 00 00 C0                  mov ebx, 0xc0000023
00AD3CBF  E9 BF 03 00 00                  jmp 0x140ad4083
00AD3CC4  8B 36                           mov esi, dword ptr [rsi]
00AD3CC6  85 F6                           test esi, esi
00AD3CC8  74 3C                           je 0x140ad3d06
00AD3CCA  8B D6                           mov edx, esi
00AD3CCC  B9 00 01 00 00                  mov ecx, 0x100
00AD3CD1  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD3CD7  E8 14 E4 0A 00                  call 0x140b820f0
00AD3CDC  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AD3CE1  48 85 C0                        test rax, rax
00AD3CE4  75 0A                           jne 0x140ad3cf0
00AD3CE6  BB 17 00 00 C0                  mov ebx, 0xc0000017
00AD3CEB  E9 93 03 00 00                  jmp 0x140ad4083
00AD3CF0  4C 8B C6                        mov r8, rsi
00AD3CF3  33 D2                           xor edx, edx
00AD3CF5  48 8B C8                        mov rcx, rax
00AD3CF8  E8 43 2F BF FF                  call 0x1406c6c40
00AD3CFD  4C 8B 5C 24 50                  mov r11, qword ptr [rsp + 0x50]
00AD3D02  33 C9                           xor ecx, ecx
00AD3D04  EB 05                           jmp 0x140ad3d0b
00AD3D06  B9 01 00 00 00                  mov ecx, 1
00AD3D0B  48 8B 05 CE 46 50 00            mov rax, qword ptr [rip + 0x5046ce]
00AD3D12  48 85 C0                        test rax, rax
00AD3D15  74 3A                           je 0x140ad3d51
00AD3D17  45 33 C0                        xor r8d, r8d
00AD3D1A  4D 8B CC                        mov r9, r12
00AD3D1D  85 C9                           test ecx, ecx
00AD3D1F  49 8B D6                        mov rdx, r14
00AD3D22  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
00AD3D2A  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00AD3D2F  4D 0F 44 C3                     cmove r8, r11
00AD3D33  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00AD3D37  41 8B CF                        mov ecx, r15d
00AD3D3A  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
00AD3D3F  44 8B C3                        mov r8d, ebx
00AD3D42  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
00AD3D47  E8 84 6D BE FF                  call 0x1406baad0
00AD3D4C  44 8B F0                        mov r14d, eax
00AD3D4F  EB 06                           jmp 0x140ad3d57
00AD3D51  41 BE BB 00 00 C0               mov r14d, 0xc00000bb
00AD3D57  8D 46 04                        lea eax, [rsi + 4]
00AD3D5A  41 BC 04 00 00 00               mov r12d, 4
00AD3D60  41 3B C4                        cmp eax, r12d
00AD3D63  0F 82 ED 00 00 00               jb 0x140ad3e56
00AD3D69  83 C0 14                        add eax, 0x14
00AD3D6C  83 F8 14                        cmp eax, 0x14
00AD3D6F  0F 82 E1 00 00 00               jb 0x140ad3e56
00AD3D75  8D 48 08                        lea ecx, [rax + 8]
00AD3D78  3B C8                           cmp ecx, eax
00AD3D7A  0F 82 D6 00 00 00               jb 0x140ad3e56
00AD3D80  8D 41 08                        lea eax, [rcx + 8]
00AD3D83  83 F8 08                        cmp eax, 8
00AD3D86  0F 82 CA 00 00 00               jb 0x140ad3e56
00AD3D8C  48 8D 50 07                     lea rdx, [rax + 7]
00AD3D90  83 E2 F8                        and edx, 0xfffffff8
00AD3D93  3B D0                           cmp edx, eax
00AD3D95  0F 82 BB 00 00 00               jb 0x140ad3e56
00AD3D9B  8D 42 08                        lea eax, [rdx + 8]
00AD3D9E  3B C2                           cmp eax, edx
00AD3DA0  0F 82 B0 00 00 00               jb 0x140ad3e56
00AD3DA6  4C 8B 84 24 A8 00 00 00         mov r8, qword ptr [rsp + 0xa8]
00AD3DAE  41 03 C4                        add eax, r12d
00AD3DB1  45 8B 48 20                     mov r9d, dword ptr [r8 + 0x20]
00AD3DB5  45 8B 40 10                     mov r8d, dword ptr [r8 + 0x10]
00AD3DB9  41 3B C4                        cmp eax, r12d
00AD3DBC  72 26                           jb 0x140ad3de4
00AD3DBE  8D 50 04                        lea edx, [rax + 4]
00AD3DC1  3B D0                           cmp edx, eax
00AD3DC3  72 1F                           jb 0x140ad3de4
00AD3DC5  42 8D 04 02                     lea eax, [rdx + r8]
00AD3DC9  3B C2                           cmp eax, edx
00AD3DCB  72 17                           jb 0x140ad3de4
00AD3DCD  8D 50 04                        lea edx, [rax + 4]
00AD3DD0  3B D0                           cmp edx, eax
00AD3DD2  72 10                           jb 0x140ad3de4
00AD3DD4  42 8D 04 0A                     lea eax, [rdx + r9]
00AD3DD8  3B C2                           cmp eax, edx
00AD3DDA  1B DB                           sbb ebx, ebx
00AD3DDC  81 E3 95 00 00 C0               and ebx, 0xc0000095
00AD3DE2  EB 05                           jmp 0x140ad3de9
00AD3DE4  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD3DE9  85 DB                           test ebx, ebx
00AD3DEB  78 6E                           js 0x140ad3e5b
00AD3DED  48 85 FF                        test rdi, rdi
00AD3DF0  75 07                           jne 0x140ad3df9
00AD3DF2  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD3DF7  EB 62                           jmp 0x140ad3e5b
00AD3DF9  33 DB                           xor ebx, ebx
00AD3DFB  89 4F 04                        mov dword ptr [rdi + 4], ecx
00AD3DFE  85 C9                           test ecx, ecx
00AD3E00  75 07                           jne 0x140ad3e09
00AD3E02  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00AD3E07  EB 24                           jmp 0x140ad3e2d
00AD3E09  8B D1                           mov edx, ecx
00AD3E0B  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD3E11  B9 00 01 00 00                  mov ecx, 0x100
00AD3E16  E8 D5 E2 0A 00                  call 0x140b820f0
00AD3E1B  48 85 C0                        test rax, rax
00AD3E1E  75 07                           jne 0x140ad3e27
00AD3E20  BB 17 00 00 C0                  mov ebx, 0xc0000017
00AD3E25  EB 06                           jmp 0x140ad3e2d
00AD3E27  48 89 47 08                     mov qword ptr [rdi + 8], rax
00AD3E2B  21 1F                           and dword ptr [rdi], ebx
00AD3E2D  85 DB                           test ebx, ebx
00AD3E2F  78 2A                           js 0x140ad3e5b
00AD3E31  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00AD3E35  41 0F BA EE 1C                  bts r14d, 0x1c
00AD3E3A  48 85 D2                        test rdx, rdx
00AD3E3D  75 36                           jne 0x140ad3e75
00AD3E3F  8B 47 04                        mov eax, dword ptr [rdi + 4]
00AD3E42  8D 48 08                        lea ecx, [rax + 8]
00AD3E45  3B C8                           cmp ecx, eax
00AD3E47  72 09                           jb 0x140ad3e52
00AD3E49  89 4F 04                        mov dword ptr [rdi + 4], ecx
00AD3E4C  44 8D 7A 01                     lea r15d, [rdx + 1]
00AD3E50  EB 71                           jmp 0x140ad3ec3
00AD3E52  83 4F 04 FF                     or dword ptr [rdi + 4], 0xffffffff
00AD3E56  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD3E5B  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AD3E60  48 85 C9                        test rcx, rcx
00AD3E63  0F 84 1A 02 00 00               je 0x140ad4083
00AD3E69  33 D2                           xor edx, edx
00AD3E6B  E8 00 EA 0A 00                  call 0x140b82870
00AD3E70  E9 0E 02 00 00                  jmp 0x140ad4083
00AD3E75  44 8B 17                        mov r10d, dword ptr [rdi]
00AD3E78  33 C9                           xor ecx, ecx
00AD3E7A  44 8D 79 01                     lea r15d, [rcx + 1]
00AD3E7E  41 3B CA                        cmp ecx, r10d
00AD3E81  73 1D                           jae 0x140ad3ea0
00AD3E83  8B 02                           mov eax, dword ptr [rdx]
00AD3E85  41 03 C4                        add eax, r12d
00AD3E88  41 3B C4                        cmp eax, r12d
00AD3E8B  72 C9                           jb 0x140ad3e56
00AD3E8D  44 8B C0                        mov r8d, eax
00AD3E90  4C 03 C2                        add r8, rdx
00AD3E93  4C 3B C2                        cmp r8, rdx
00AD3E96  72 BE                           jb 0x140ad3e56
00AD3E98  49 8B D0                        mov rdx, r8
00AD3E9B  41 03 CF                        add ecx, r15d
00AD3E9E  EB DE                           jmp 0x140ad3e7e
00AD3EA0  4C 8D 42 04                     lea r8, [rdx + 4]
00AD3EA4  4C 3B C2                        cmp r8, rdx
00AD3EA7  72 AD                           jb 0x140ad3e56
00AD3EA9  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00AD3EAC  48 8D 42 08                     lea rax, [rdx + 8]
00AD3EB0  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00AD3EB4  48 3B C1                        cmp rax, rcx
00AD3EB7  0F 87 16 01 00 00               ja 0x140ad3fd3
00AD3EBD  44 89 22                        mov dword ptr [rdx], r12d
00AD3EC0  45 89 30                        mov dword ptr [r8], r14d
00AD3EC3  44 01 3F                        add dword ptr [rdi], r15d
00AD3EC6  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00AD3ECA  48 85 D2                        test rdx, rdx
00AD3ECD  75 13                           jne 0x140ad3ee2
00AD3ECF  8B 47 04                        mov eax, dword ptr [rdi + 4]
00AD3ED2  8D 48 0C                        lea ecx, [rax + 0xc]
00AD3ED5  3B C8                           cmp ecx, eax
00AD3ED7  0F 82 75 FF FF FF               jb 0x140ad3e52
00AD3EDD  89 4F 04                        mov dword ptr [rdi + 4], ecx
00AD3EE0  EB 59                           jmp 0x140ad3f3b
00AD3EE2  44 8B 0F                        mov r9d, dword ptr [rdi]
00AD3EE5  33 C9                           xor ecx, ecx
00AD3EE7  41 3B C9                        cmp ecx, r9d
00AD3EEA  73 25                           jae 0x140ad3f11
00AD3EEC  8B 02                           mov eax, dword ptr [rdx]
00AD3EEE  41 03 C4                        add eax, r12d
00AD3EF1  41 3B C4                        cmp eax, r12d
00AD3EF4  0F 82 5C FF FF FF               jb 0x140ad3e56
00AD3EFA  44 8B C0                        mov r8d, eax
00AD3EFD  4C 03 C2                        add r8, rdx
00AD3F00  4C 3B C2                        cmp r8, rdx
00AD3F03  0F 82 4D FF FF FF               jb 0x140ad3e56
00AD3F09  49 8B D0                        mov rdx, r8
00AD3F0C  41 03 CF                        add ecx, r15d
00AD3F0F  EB D6                           jmp 0x140ad3ee7
00AD3F11  4C 8D 42 04                     lea r8, [rdx + 4]
00AD3F15  4C 3B C2                        cmp r8, rdx
00AD3F18  0F 82 38 FF FF FF               jb 0x140ad3e56
00AD3F1E  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00AD3F21  48 8D 42 0C                     lea rax, [rdx + 0xc]
00AD3F25  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00AD3F29  48 3B C1                        cmp rax, rcx
00AD3F2C  0F 87 A1 00 00 00               ja 0x140ad3fd3
00AD3F32  C7 02 08 00 00 00               mov dword ptr [rdx], 8
00AD3F38  49 89 28                        mov qword ptr [r8], rbp
00AD3F3B  44 01 3F                        add dword ptr [rdi], r15d
00AD3F3E  4C 8B 5C 24 50                  mov r11, qword ptr [rsp + 0x50]
00AD3F43  4D 85 DB                        test r11, r11
00AD3F46  75 09                           jne 0x140ad3f51
00AD3F48  85 F6                           test esi, esi
00AD3F4A  74 0D                           je 0x140ad3f59
00AD3F4C  E9 A1 FE FF FF                  jmp 0x140ad3df2
00AD3F51  85 F6                           test esi, esi
00AD3F53  0F 84 99 FE FF FF               je 0x140ad3df2
00AD3F59  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00AD3F5D  48 85 D2                        test rdx, rdx
00AD3F60  75 1F                           jne 0x140ad3f81
00AD3F62  41 03 F4                        add esi, r12d
00AD3F65  41 3B F4                        cmp esi, r12d
00AD3F68  0F 82 E8 FE FF FF               jb 0x140ad3e56
00AD3F6E  8B 47 04                        mov eax, dword ptr [rdi + 4]
00AD3F71  8D 0C 30                        lea ecx, [rax + rsi]
00AD3F74  3B C8                           cmp ecx, eax
00AD3F76  0F 82 D6 FE FF FF               jb 0x140ad3e52
00AD3F7C  89 4F 04                        mov dword ptr [rdi + 4], ecx
00AD3F7F  EB 6E                           jmp 0x140ad3fef
00AD3F81  44 8B 0F                        mov r9d, dword ptr [rdi]
00AD3F84  33 C9                           xor ecx, ecx
00AD3F86  41 3B C9                        cmp ecx, r9d
00AD3F89  73 25                           jae 0x140ad3fb0
00AD3F8B  8B 02                           mov eax, dword ptr [rdx]
00AD3F8D  41 03 C4                        add eax, r12d
00AD3F90  41 3B C4                        cmp eax, r12d
00AD3F93  0F 82 BD FE FF FF               jb 0x140ad3e56
00AD3F99  44 8B C0                        mov r8d, eax
00AD3F9C  4C 03 C2                        add r8, rdx
00AD3F9F  4C 3B C2                        cmp r8, rdx
00AD3FA2  0F 82 AE FE FF FF               jb 0x140ad3e56
00AD3FA8  49 8B D0                        mov rdx, r8
00AD3FAB  41 03 CF                        add ecx, r15d
00AD3FAE  EB D6                           jmp 0x140ad3f86
00AD3FB0  4C 8D 4A 04                     lea r9, [rdx + 4]
00AD3FB4  4C 3B CA                        cmp r9, rdx
00AD3FB7  0F 82 99 FE FF FF               jb 0x140ad3e56
00AD3FBD  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00AD3FC0  48 8D 46 04                     lea rax, [rsi + 4]
00AD3FC4  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00AD3FC8  48 03 C2                        add rax, rdx
00AD3FCB  44 8B C6                        mov r8d, esi
00AD3FCE  48 3B C1                        cmp rax, rcx
00AD3FD1  76 0A                           jbe 0x140ad3fdd
00AD3FD3  BB 23 00 00 C0                  mov ebx, 0xc0000023
00AD3FD8  E9 7E FE FF FF                  jmp 0x140ad3e5b
00AD3FDD  89 32                           mov dword ptr [rdx], esi
00AD3FDF  4D 85 DB                        test r11, r11
00AD3FE2  74 0B                           je 0x140ad3fef
00AD3FE4  49 8B D3                        mov rdx, r11
00AD3FE7  49 8B C9                        mov rcx, r9
00AD3FEA  E8 51 28 BF FF                  call 0x1406c6840
00AD3FEF  44 01 3F                        add dword ptr [rdi], r15d
00AD3FF2  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00AD3FF6  44 8B 84 24 B0 00 00 00         mov r8d, dword ptr [rsp + 0xb0]
00AD3FFE  48 85 D2                        test rdx, rdx
00AD4001  75 1B                           jne 0x140ad401e
00AD4003  8B 47 04                        mov eax, dword ptr [rdi + 4]
00AD4006  8D 48 08                        lea ecx, [rax + 8]
00AD4009  3B C8                           cmp ecx, eax
00AD400B  0F 82 41 FE FF FF               jb 0x140ad3e52
00AD4011  44 01 3F                        add dword ptr [rdi], r15d
00AD4014  33 DB                           xor ebx, ebx
00AD4016  89 4F 04                        mov dword ptr [rdi + 4], ecx
00AD4019  E9 3D FE FF FF                  jmp 0x140ad3e5b
00AD401E  44 8B 17                        mov r10d, dword ptr [rdi]
00AD4021  33 C9                           xor ecx, ecx
00AD4023  41 3B CA                        cmp ecx, r10d
00AD4026  73 25                           jae 0x140ad404d
00AD4028  8B 02                           mov eax, dword ptr [rdx]
00AD402A  41 03 C4                        add eax, r12d
00AD402D  41 3B C4                        cmp eax, r12d
00AD4030  0F 82 20 FE FF FF               jb 0x140ad3e56
00AD4036  44 8B C8                        mov r9d, eax
00AD4039  4C 03 CA                        add r9, rdx
00AD403C  4C 3B CA                        cmp r9, rdx
00AD403F  0F 82 11 FE FF FF               jb 0x140ad3e56
00AD4045  49 8B D1                        mov rdx, r9
00AD4048  41 03 CF                        add ecx, r15d
00AD404B  EB D6                           jmp 0x140ad4023
00AD404D  4C 8D 4A 04                     lea r9, [rdx + 4]
00AD4051  4C 3B CA                        cmp r9, rdx
00AD4054  0F 82 FC FD FF FF               jb 0x140ad3e56
00AD405A  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00AD405D  48 8D 42 08                     lea rax, [rdx + 8]
00AD4061  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00AD4065  33 DB                           xor ebx, ebx
00AD4067  48 3B C1                        cmp rax, rcx
00AD406A  0F 87 63 FF FF FF               ja 0x140ad3fd3
00AD4070  44 89 22                        mov dword ptr [rdx], r12d
00AD4073  45 89 01                        mov dword ptr [r9], r8d
00AD4076  44 01 3F                        add dword ptr [rdi], r15d
00AD4079  E9 DD FD FF FF                  jmp 0x140ad3e5b
00AD407E  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD4083  8B C3                           mov eax, ebx
00AD4085  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
00AD408D  48 83 C4 60                     add rsp, 0x60
00AD4091  41 5F                           pop r15
00AD4093  41 5E                           pop r14
00AD4095  41 5D                           pop r13
00AD4097  41 5C                           pop r12
00AD4099  5F                              pop rdi
00AD409A  5E                              pop rsi
00AD409B  5D                              pop rbp
00AD409C  C3                              ret
00AD409D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00AD3B00(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (96);
    v_r11 = 0;
    v_stack_m48 = 0;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00AD3C2E;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_00AD3C2E;
    a2 = 0;
loc_00AD3B4B:
    if (0 >= 3) goto loc_00AD3B71;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD407E;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD407E;
    a2 = (unsigned int)((a2) + 1);
    goto loc_00AD3B4B;
loc_00AD3B71:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD407E;
    v_rbp = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rbp = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_00AD3CBA;
    if ((*(unsigned int *)(a1)) <= 4) goto loc_00AD3C2E;
    a2 = 0;
loc_00AD3BA0:
    if (0 >= 4) goto loc_00AD3BC6;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD407E;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD407E;
    a2 = (unsigned int)((a2) + 1);
    goto loc_00AD3BA0;
loc_00AD3BC6:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD407E;
    v_r15 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r15 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 4) goto loc_00AD3CBA;
    if ((*(unsigned int *)(a1)) <= 5) goto loc_00AD3C2E;
    a2 = 0;
loc_00AD3BF1:
    if (0 >= 5) goto loc_00AD3C16;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD407E;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD407E;
    a2 = (unsigned int)((a2) + 1);
    goto loc_00AD3BF1;
loc_00AD3C16:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD407E;
    v_r14 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r14 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((*(unsigned int *)(a1)) > 6) goto loc_00AD3C38;
loc_00AD3C2E:
    goto loc_00AD4083;
loc_00AD3C38:
    a2 = 0;
loc_00AD3C3D:
    if (0 >= 6) goto loc_00AD3C63;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD407E;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD407E;
    a2 = (unsigned int)((a2) + 1);
    goto loc_00AD3C3D;
loc_00AD3C63:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD407E;
    v_r12 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r12 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((*(unsigned int *)(a1)) <= 7) goto loc_00AD3C2E;
    a2 = 0;
loc_00AD3C7E:
    if (0 >= 7) goto loc_00AD3CA4;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD407E;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD407E;
    a2 = (unsigned int)((a2) + 1);
    goto loc_00AD3C7E;
loc_00AD3CA4:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD407E;
    v_rsi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rsi = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) == 4) goto loc_00AD3CC4;
loc_00AD3CBA:
    goto loc_00AD4083;
loc_00AD3CC4:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))) == 0) goto loc_00AD3D06;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)))), (unsigned int)(0x20534C53ULL), a1);
    v_stack_m48 = result;
    if (result != 0) goto loc_00AD3CF0;
    goto loc_00AD4083;
loc_00AD3CF0:
    a2 = 0;
    result = memset(result, a2, (unsigned int)(*(unsigned int *)(v_rsi)), a1);
    a1 = 0;
    goto loc_00AD3D0B;
loc_00AD3D06:
loc_00AD3D0B:
    if (*(unsigned __int64 *)(v_rip + 5261006) == 0) goto loc_00AD3D51;
    a3 = 0;
    v_stack_m60 = v_stack_p18;
    if (1 == 0) { a3 = v_stack_m48; }
    v_stack_m68 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)));
    v_stack_m70 = a3;
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    result = guard_dispatch_icall((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r15)))), v_r14, (unsigned int)((unsigned int)((unsigned int)(0xC0000017ULL))), v_r12);
    goto loc_00AD3D57;
loc_00AD3D51:
loc_00AD3D57:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)) + 4)) < 4) goto loc_00AD3E56;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi)) + 4) + (20));
    if (((unsigned int)(result)) < 20) goto loc_00AD3E56;
    if (((unsigned int)(result + 8)) < ((unsigned int)(result))) goto loc_00AD3E56;
    if (((unsigned int)(result + 8 + 8)) < 8) goto loc_00AD3E56;
    a2 = (unsigned int)((result + 8 + 8 + 7) & (0xFFFFFFF8ULL));
    if (((unsigned int)(a2)) < ((unsigned int)(result + 8 + 8))) goto loc_00AD3E56;
    if (((unsigned int)(a2 + 8)) < ((unsigned int)(a2))) goto loc_00AD3E56;
    result = (unsigned int)((a2 + 8) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD3DE4;
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_00AD3DE4;
    if (((unsigned int)(result + 4 + (unsigned int)(*(unsigned int *)(v_stack_p10 + 16)) * 1)) < ((unsigned int)(result + 4))) goto loc_00AD3DE4;
    if (((unsigned int)(result + 4 + (unsigned int)(*(unsigned int *)(v_stack_p10 + 16)) * 1 + 4)) < ((unsigned int)(result + 4 + (unsigned int)(*(unsigned int *)(v_stack_p10 + 16)) * 1))) goto loc_00AD3DE4;
    v_rbx = (unsigned int)(((unsigned int)(0xC0000017ULL)) & (0xC0000095ULL));
    goto loc_00AD3DE9;
loc_00AD3DE4:
loc_00AD3DE9:
    if (sign_flag) goto loc_00AD3E5B;
    if (a4 != 0) goto loc_00AD3DF9;
loc_00AD3DF2:
    goto loc_00AD3E5B;
loc_00AD3DF9:
    v_rbx = 0;
    *(unsigned int *)(a4 + 4) = (unsigned int)(result + 8);
    if ((unsigned int)(result + 8) != 0) goto loc_00AD3E09;
    goto loc_00AD3E2D;
loc_00AD3E09:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result + 8)), (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(v_stack_p10 + 32)));
    if (result != 0) goto loc_00AD3E27;
    goto loc_00AD3E2D;
loc_00AD3E27:
    *(unsigned __int64 *)(a4 + 8) = result;
loc_00AD3E2D:
    if (sign_flag) goto loc_00AD3E5B;
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD3E75;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD3E52;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00AD3EC3;
loc_00AD3E52:
loc_00AD3E56:
loc_00AD3E5B:
    if (v_stack_m48 == 0) goto loc_00AD4083;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m48, a2, (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(v_stack_p10 + 32)));
    goto loc_00AD4083;
loc_00AD3E75:
    a1 = 0;
loc_00AD3E7E:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD3EA0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD3E56;
    a3 = ((unsigned int)((unsigned int)(result))) + (0);
    if (a3 < 0) goto loc_00AD3E56;
    a1 = (unsigned int)((a1) + ((unsigned int)(a1 + 1)));
    goto loc_00AD3E7E;
loc_00AD3EA0:
    if ((a3 + 4) < a3) goto loc_00AD3E56;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_00AD3FD3;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)(0xC00000BBULL));
loc_00AD3EC3:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD3EE2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD3E52;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12);
    goto loc_00AD3F3B;
loc_00AD3EE2:
    a1 = 0;
loc_00AD3EE7:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD3F11;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD3E56;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00AD3E56;
    a1 = (unsigned int)((a1) + ((unsigned int)(a1 + 1)));
    goto loc_00AD3EE7;
loc_00AD3F11:
    if ((a3 + 4) < a3) goto loc_00AD3E56;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) > a1) goto loc_00AD3FD3;
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)(a3 + 4) = *(unsigned __int64 *)(v_rbp);
loc_00AD3F3B:
    if (v_stack_m48 != 0) goto loc_00AD3F51;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))) == 0) goto loc_00AD3F59;
    goto loc_00AD3DF2;
loc_00AD3F51:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi))) == 0) goto loc_00AD3DF2;
loc_00AD3F59:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD3F81;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) + (4));
    if (((unsigned int)(v_rsi)) < 4) goto loc_00AD3E56;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + v_rsi * 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD3E52;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + v_rsi * 1);
    goto loc_00AD3FEF;
loc_00AD3F81:
    a1 = 0;
loc_00AD3F86:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD3FB0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD3E56;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00AD3E56;
    a1 = (unsigned int)((a1) + ((unsigned int)(a1 + 1)));
    goto loc_00AD3F86;
loc_00AD3FB0:
    if ((a3 + 4) < a3) goto loc_00AD3E56;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    result = (v_rsi + 4) + (a3);
    if (result <= a1) goto loc_00AD3FDD;
loc_00AD3FD3:
    goto loc_00AD3E5B;
loc_00AD3FDD:
    *(unsigned int *)(a3) = (unsigned int)(v_rsi);
    if (v_stack_m48 != 0) {
        a2 = v_stack_m48;
        a1 = a3 + 4;
        result = memcpy(a1, a2, (unsigned int)((unsigned int)(v_rsi)), a3 + 4);
    }
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD401E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD3E52;
    v_rbx = 0;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00AD3E5B;
loc_00AD401E:
    a1 = 0;
loc_00AD4023:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD404D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD3E56;
    a4 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a4 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00AD3E56;
    a1 = (unsigned int)((a1) + ((unsigned int)(a1 + 1)));
    goto loc_00AD4023;
loc_00AD404D:
    if ((a4 + 4) < a4) goto loc_00AD3E56;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    v_rbx = 0;
    if ((a4 + 8) > a1) goto loc_00AD3FD3;
    *(unsigned int *)(a4) = 4;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(v_stack_p18));
    goto loc_00AD3E5B;
loc_00AD407E:
loc_00AD4083:
    v_rsp = (v_rsp) + (96);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_00AD3B00(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (96);
    local_r11 = 0;
    v_stack_m48 = 0;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00AD3C2E;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_00AD3C2E;
    Arg2 = 0;
loc_00AD3B4B:
    if (0 >= 3) goto loc_00AD3B71;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD407E;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD407E;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_00AD3B4B;
loc_00AD3B71:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD407E;
    local_rbp = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rbp = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_00AD3CBA;
    if ((*(uint32_t *)(arg1)) <= 4) goto loc_00AD3C2E;
    Arg2 = 0;
loc_00AD3BA0:
    if (0 >= 4) goto loc_00AD3BC6;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD407E;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD407E;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_00AD3BA0;
loc_00AD3BC6:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD407E;
    local_r15 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r15 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 4) goto loc_00AD3CBA;
    if ((*(uint32_t *)(arg1)) <= 5) goto loc_00AD3C2E;
    Arg2 = 0;
loc_00AD3BF1:
    if (0 >= 5) goto loc_00AD3C16;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD407E;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD407E;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_00AD3BF1;
loc_00AD3C16:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD407E;
    local_r14 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r14 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((*(uint32_t *)(arg1)) > 6) goto loc_00AD3C38;
loc_00AD3C2E:
    goto loc_00AD4083;
loc_00AD3C38:
    Arg2 = 0;
loc_00AD3C3D:
    if (0 >= 6) goto loc_00AD3C63;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD407E;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD407E;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_00AD3C3D;
loc_00AD3C63:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD407E;
    local_r12 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r12 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((*(uint32_t *)(arg1)) <= 7) goto loc_00AD3C2E;
    Arg2 = 0;
loc_00AD3C7E:
    if (0 >= 7) goto loc_00AD3CA4;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD407E;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD407E;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_00AD3C7E;
loc_00AD3CA4:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD407E;
    local_rsi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rsi = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) == 4) goto loc_00AD3CC4;
loc_00AD3CBA:
    goto loc_00AD4083;
loc_00AD3CC4:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))) == 0) goto loc_00AD3D06;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)))), (uint32_t)(0x20534C53ULL), Arg1);
    v_stack_m48 = result;
    if (result != 0) goto loc_00AD3CF0;
    goto loc_00AD4083;
loc_00AD3CF0:
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(*(uint32_t *)(local_rsi)), Arg1);
    Arg1 = 0;
    goto loc_00AD3D0B;
loc_00AD3D06:
loc_00AD3D0B:
    if (*(uint64_t *)(v_rip + 0x5046CE) == 0) goto loc_00AD3D51;
    Arg3 = 0;
    v_stack_m60 = v_stack_p18;
    if (1 == 0) { Arg3 = v_stack_m48; }
    v_stack_m68 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)));
    v_stack_m70 = Arg3;
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    result = guard_dispatch_icall((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r15)))), local_r14, (uint32_t)((uint32_t)((uint32_t)(0xC0000017ULL))), local_r12);
    goto loc_00AD3D57;
loc_00AD3D51:
loc_00AD3D57:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)) + 4)) < 4) goto loc_00AD3E56;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi)) + 4) + (20));
    if (((uint32_t)(result)) < 20) goto loc_00AD3E56;
    if (((uint32_t)(result + 8)) < ((uint32_t)(result))) goto loc_00AD3E56;
    if (((uint32_t)(result + 8 + 8)) < 8) goto loc_00AD3E56;
    Arg2 = (uint32_t)((result + 8 + 8 + 7) & (0xFFFFFFF8ULL));
    if (((uint32_t)(Arg2)) < ((uint32_t)(result + 8 + 8))) goto loc_00AD3E56;
    if (((uint32_t)(Arg2 + 8)) < ((uint32_t)(Arg2))) goto loc_00AD3E56;
    result = (uint32_t)((Arg2 + 8) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD3DE4;
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_00AD3DE4;
    if (((uint32_t)(result + 4 + (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x10)) * 1)) < ((uint32_t)(result + 4))) goto loc_00AD3DE4;
    if (((uint32_t)(result + 4 + (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x10)) * 1 + 4)) < ((uint32_t)(result + 4 + (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x10)) * 1))) goto loc_00AD3DE4;
    local_rbx = (uint32_t)(((uint32_t)(0xC0000017ULL)) & (0xC0000095ULL));
    goto loc_00AD3DE9;
loc_00AD3DE4:
loc_00AD3DE9:
    if (sign_flag) goto loc_00AD3E5B;
    if (Arg4 != 0) goto loc_00AD3DF9;
loc_00AD3DF2:
    goto loc_00AD3E5B;
loc_00AD3DF9:
    local_rbx = 0;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(result + 8);
    if ((uint32_t)(result + 8) != 0) goto loc_00AD3E09;
    goto loc_00AD3E2D;
loc_00AD3E09:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result + 8)), (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20)));
    if (result != 0) goto loc_00AD3E27;
    goto loc_00AD3E2D;
loc_00AD3E27:
    *(uint64_t *)(Arg4 + 0x8) = result;
loc_00AD3E2D:
    if (sign_flag) goto loc_00AD3E5B;
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD3E75;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD3E52;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_00AD3EC3;
loc_00AD3E52:
loc_00AD3E56:
loc_00AD3E5B:
    if (v_stack_m48 == 0) goto loc_00AD4083;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m48, Arg2, (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x20)));
    goto loc_00AD4083;
loc_00AD3E75:
    Arg1 = 0;
loc_00AD3E7E:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD3EA0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD3E56;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (0);
    if (Arg3 < 0) goto loc_00AD3E56;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1 + 1)));
    goto loc_00AD3E7E;
loc_00AD3EA0:
    if ((Arg3 + 4) < Arg3) goto loc_00AD3E56;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_00AD3FD3;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)(0xC00000BBULL));
loc_00AD3EC3:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD3EE2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD3E52;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12);
    goto loc_00AD3F3B;
loc_00AD3EE2:
    Arg1 = 0;
loc_00AD3EE7:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD3F11;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD3E56;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00AD3E56;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1 + 1)));
    goto loc_00AD3EE7;
loc_00AD3F11:
    if ((Arg3 + 4) < Arg3) goto loc_00AD3E56;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 12) > Arg1) goto loc_00AD3FD3;
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)(Arg3 + 0x4) = *(uint64_t *)(local_rbp);
loc_00AD3F3B:
    if (v_stack_m48 != 0) goto loc_00AD3F51;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))) == 0) goto loc_00AD3F59;
    goto loc_00AD3DF2;
loc_00AD3F51:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi))) == 0) goto loc_00AD3DF2;
loc_00AD3F59:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD3F81;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) + (4));
    if (((uint32_t)(local_rsi)) < 4) goto loc_00AD3E56;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + local_rsi * 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD3E52;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + local_rsi * 1);
    goto loc_00AD3FEF;
loc_00AD3F81:
    Arg1 = 0;
loc_00AD3F86:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD3FB0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD3E56;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00AD3E56;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1 + 1)));
    goto loc_00AD3F86;
loc_00AD3FB0:
    if ((Arg3 + 4) < Arg3) goto loc_00AD3E56;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    result = (local_rsi + 4) + (Arg3);
    if (result <= Arg1) goto loc_00AD3FDD;
loc_00AD3FD3:
    goto loc_00AD3E5B;
loc_00AD3FDD:
    *(uint32_t *)(Arg3) = (uint32_t)(local_rsi);
    if (v_stack_m48 != 0) {
        Arg2 = v_stack_m48;
        Arg1 = Arg3 + 4;
        result = memcpy(Arg1, Arg2, (uint32_t)((uint32_t)(local_rsi)), Arg3 + 4);
    }
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD401E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD3E52;
    local_rbx = 0;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_00AD3E5B;
loc_00AD401E:
    Arg1 = 0;
loc_00AD4023:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD404D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD3E56;
    Arg4 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg4 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00AD3E56;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg1 + 1)));
    goto loc_00AD4023;
loc_00AD404D:
    if ((Arg4 + 4) < Arg4) goto loc_00AD3E56;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    local_rbx = 0;
    if ((Arg4 + 8) > Arg1) goto loc_00AD3FD3;
    *(uint32_t *)(Arg4) = 4;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(v_stack_p18));
    goto loc_00AD3E5B;
loc_00AD407E:
loc_00AD4083:
    local_rsp = (local_rsp) + (96);
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AD3B00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
