# sub_004C4874

- RVA: `0x004C4874`–`0x004C4CE7` (길이 `1,139` bytes)
- VA: `0x00000001404C4874`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCDB8`
- 디코드: `350`개 명령, `1,139/1,139` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004C496C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004C498B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004C49B2` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004C4A77` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004C4C1E` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x004C4CBB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [sub_00968AF6](../../page/96/Unknown_function_00968AF6.md) at `0x0096A6E7`

### Static image references
- `0x004C4997` → RVA `0x00FD8408` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x004C496C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004C4A77` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004C4CBB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C4874  48 8B C4                        mov rax, rsp
004C4877  48 89 58 08                     mov qword ptr [rax + 8], rbx
004C487B  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
004C487F  48 89 70 20                     mov qword ptr [rax + 0x20], rsi
004C4883  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
004C4887  57                              push rdi
004C4888  41 54                           push r12
004C488A  41 55                           push r13
004C488C  41 56                           push r14
004C488E  41 57                           push r15
004C4890  48 83 EC 20                     sub rsp, 0x20
004C4894  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
004C4898  45 33 E4                        xor r12d, r12d
004C489B  44 21 60 18                     and dword ptr [rax + 0x18], r12d
004C489F  49 8B F1                        mov rsi, r9
004C48A2  48 8B FA                        mov rdi, rdx
004C48A5  4C 8B C9                        mov r9, rcx
004C48A8  4D 85 C0                        test r8, r8
004C48AB  74 58                           je 0x1404c4905
004C48AD  83 39 03                        cmp dword ptr [rcx], 3
004C48B0  76 53                           jbe 0x1404c4905
004C48B2  49 8B C0                        mov rax, r8
004C48B5  45 8D 6C 24 01                  lea r13d, [r12 + 1]
004C48BA  33 D2                           xor edx, edx
004C48BC  44 8B 10                        mov r10d, dword ptr [rax]
004C48BF  48 8D 48 04                     lea rcx, [rax + 4]
004C48C3  83 FA 03                        cmp edx, 3
004C48C6  73 1B                           jae 0x1404c48e3
004C48C8  48 3B C8                        cmp rcx, rax
004C48CB  0F 82 F1 03 00 00               jb 0x1404c4cc2
004C48D1  4A 8D 04 11                     lea rax, [rcx + r10]
004C48D5  48 3B C1                        cmp rax, rcx
004C48D8  0F 82 E4 03 00 00               jb 0x1404c4cc2
004C48DE  41 03 D5                        add edx, r13d
004C48E1  EB D9                           jmp 0x1404c48bc
004C48E3  48 3B C8                        cmp rcx, rax
004C48E6  0F 82 D6 03 00 00               jb 0x1404c4cc2
004C48EC  45 33 F6                        xor r14d, r14d
004C48EF  45 85 D2                        test r10d, r10d
004C48F2  4C 0F 45 F1                     cmovne r14, rcx
004C48F6  41 83 FA 08                     cmp r10d, 8
004C48FA  75 52                           jne 0x1404c494e
004C48FC  41 83 39 04                     cmp dword ptr [r9], 4
004C4900  4D 8B 36                        mov r14, qword ptr [r14]
004C4903  77 0A                           ja 0x1404c490f
004C4905  BB 0D 00 00 C0                  mov ebx, 0xc000000d
004C490A  E9 B8 03 00 00                  jmp 0x1404c4cc7
004C490F  33 D2                           xor edx, edx
004C4911  41 8B 00                        mov eax, dword ptr [r8]
004C4914  49 8D 48 04                     lea rcx, [r8 + 4]
004C4918  83 FA 04                        cmp edx, 4
004C491B  73 1B                           jae 0x1404c4938
004C491D  49 3B C8                        cmp rcx, r8
004C4920  0F 82 9C 03 00 00               jb 0x1404c4cc2
004C4926  4C 8D 04 01                     lea r8, [rcx + rax]
004C492A  4C 3B C1                        cmp r8, rcx
004C492D  0F 82 8F 03 00 00               jb 0x1404c4cc2
004C4933  41 03 D5                        add edx, r13d
004C4936  EB D9                           jmp 0x1404c4911
004C4938  49 3B C8                        cmp rcx, r8
004C493B  0F 82 81 03 00 00               jb 0x1404c4cc2
004C4941  33 ED                           xor ebp, ebp
004C4943  85 C0                           test eax, eax
004C4945  48 0F 45 E9                     cmovne rbp, rcx
004C4949  83 F8 04                        cmp eax, 4
004C494C  74 0A                           je 0x1404c4958
004C494E  BB 23 00 00 C0                  mov ebx, 0xc0000023
004C4953  E9 6F 03 00 00                  jmp 0x1404c4cc7
004C4958  8B 6D 00                        mov ebp, dword ptr [rbp]
004C495B  85 ED                           test ebp, ebp
004C495D  74 35                           je 0x1404c4994
004C495F  41 B8 53 4C 53 20               mov r8d, 0x20534c53
004C4965  8B D5                           mov edx, ebp
004C4967  B9 00 01 00 00                  mov ecx, 0x100
004C496C  E8 7F D7 6B 00                  call 0x140b820f0
004C4971  4C 8B E0                        mov r12, rax
004C4974  48 85 C0                        test rax, rax
004C4977  75 0A                           jne 0x1404c4983
004C4979  BB 17 00 00 C0                  mov ebx, 0xc0000017
004C497E  E9 44 03 00 00                  jmp 0x1404c4cc7
004C4983  4C 8B C5                        mov r8, rbp
004C4986  33 D2                           xor edx, edx
004C4988  48 8B C8                        mov rcx, rax
004C498B  E8 B0 22 20 00                  call 0x1406c6c40
004C4990  33 D2                           xor edx, edx
004C4992  EB 03                           jmp 0x1404c4997
004C4994  41 8B D5                        mov edx, r13d
004C4997  48 8B 05 6A 3A B1 00            mov rax, qword ptr [rip + 0xb13a6a]
004C499E  48 85 C0                        test rax, rax
004C49A1  74 19                           je 0x1404c49bc
004C49A3  33 C9                           xor ecx, ecx
004C49A5  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
004C49AA  85 D2                           test edx, edx
004C49AC  8B D5                           mov edx, ebp
004C49AE  49 0F 44 CC                     cmove rcx, r12
004C49B2  E8 19 61 1F 00                  call 0x1406baad0
004C49B7  44 8B F8                        mov r15d, eax
004C49BA  EB 06                           jmp 0x1404c49c2
004C49BC  41 BF BB 00 00 C0               mov r15d, 0xc00000bb
004C49C2  8D 45 04                        lea eax, [rbp + 4]
004C49C5  83 F8 04                        cmp eax, 4
004C49C8  0F 82 DE 02 00 00               jb 0x1404c4cac
004C49CE  83 C0 14                        add eax, 0x14
004C49D1  83 F8 14                        cmp eax, 0x14
004C49D4  0F 82 D2 02 00 00               jb 0x1404c4cac
004C49DA  8D 48 08                        lea ecx, [rax + 8]
004C49DD  3B C8                           cmp ecx, eax
004C49DF  0F 82 C7 02 00 00               jb 0x1404c4cac
004C49E5  8D 41 08                        lea eax, [rcx + 8]
004C49E8  83 F8 08                        cmp eax, 8
004C49EB  0F 82 BB 02 00 00               jb 0x1404c4cac
004C49F1  48 8D 50 07                     lea rdx, [rax + 7]
004C49F5  83 E2 F8                        and edx, 0xfffffff8
004C49F8  3B D0                           cmp edx, eax
004C49FA  0F 82 AC 02 00 00               jb 0x1404c4cac
004C4A00  8D 42 08                        lea eax, [rdx + 8]
004C4A03  3B C2                           cmp eax, edx
004C4A05  0F 82 A1 02 00 00               jb 0x1404c4cac
004C4A0B  44 8B 4F 20                     mov r9d, dword ptr [rdi + 0x20]
004C4A0F  83 C0 04                        add eax, 4
004C4A12  44 8B 47 10                     mov r8d, dword ptr [rdi + 0x10]
004C4A16  83 F8 04                        cmp eax, 4
004C4A19  72 27                           jb 0x1404c4a42
004C4A1B  8D 50 04                        lea edx, [rax + 4]
004C4A1E  3B D0                           cmp edx, eax
004C4A20  72 20                           jb 0x1404c4a42
004C4A22  42 8D 04 02                     lea eax, [rdx + r8]
004C4A26  3B C2                           cmp eax, edx
004C4A28  72 18                           jb 0x1404c4a42
004C4A2A  8D 50 04                        lea edx, [rax + 4]
004C4A2D  BF 95 00 00 C0                  mov edi, 0xc0000095
004C4A32  3B D0                           cmp edx, eax
004C4A34  72 11                           jb 0x1404c4a47
004C4A36  42 8D 04 0A                     lea eax, [rdx + r9]
004C4A3A  3B C2                           cmp eax, edx
004C4A3C  1B DB                           sbb ebx, ebx
004C4A3E  23 DF                           and ebx, edi
004C4A40  EB 07                           jmp 0x1404c4a49
004C4A42  BF 95 00 00 C0                  mov edi, 0xc0000095
004C4A47  8B DF                           mov ebx, edi
004C4A49  85 DB                           test ebx, ebx
004C4A4B  0F 88 60 02 00 00               js 0x1404c4cb1
004C4A51  48 85 F6                        test rsi, rsi
004C4A54  0F 84 2E 01 00 00               je 0x1404c4b88
004C4A5A  33 DB                           xor ebx, ebx
004C4A5C  89 4E 04                        mov dword ptr [rsi + 4], ecx
004C4A5F  85 C9                           test ecx, ecx
004C4A61  75 07                           jne 0x1404c4a6a
004C4A63  BB 3E 00 00 C0                  mov ebx, 0xc000003e
004C4A68  EB 24                           jmp 0x1404c4a8e
004C4A6A  8B D1                           mov edx, ecx
004C4A6C  41 B8 53 4C 53 20               mov r8d, 0x20534c53
004C4A72  B9 00 01 00 00                  mov ecx, 0x100
004C4A77  E8 74 D6 6B 00                  call 0x140b820f0
004C4A7C  48 85 C0                        test rax, rax
004C4A7F  75 07                           jne 0x1404c4a88
004C4A81  BB 17 00 00 C0                  mov ebx, 0xc0000017
004C4A86  EB 06                           jmp 0x1404c4a8e
004C4A88  48 89 46 08                     mov qword ptr [rsi + 8], rax
004C4A8C  21 1E                           and dword ptr [rsi], ebx
004C4A8E  85 DB                           test ebx, ebx
004C4A90  0F 88 1B 02 00 00               js 0x1404c4cb1
004C4A96  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
004C4A9A  41 0F BA EF 1C                  bts r15d, 0x1c
004C4A9F  48 85 D2                        test rdx, rdx
004C4AA2  75 13                           jne 0x1404c4ab7
004C4AA4  8B 46 04                        mov eax, dword ptr [rsi + 4]
004C4AA7  8D 48 08                        lea ecx, [rax + 8]
004C4AAA  3B C8                           cmp ecx, eax
004C4AAC  0F 82 04 01 00 00               jb 0x1404c4bb6
004C4AB2  89 4E 04                        mov dword ptr [rsi + 4], ecx
004C4AB5  EB 59                           jmp 0x1404c4b10
004C4AB7  44 8B 16                        mov r10d, dword ptr [rsi]
004C4ABA  33 C9                           xor ecx, ecx
004C4ABC  41 3B CA                        cmp ecx, r10d
004C4ABF  73 25                           jae 0x1404c4ae6
004C4AC1  8B 02                           mov eax, dword ptr [rdx]
004C4AC3  83 C0 04                        add eax, 4
004C4AC6  83 F8 04                        cmp eax, 4
004C4AC9  0F 82 EB 00 00 00               jb 0x1404c4bba
004C4ACF  44 8B C0                        mov r8d, eax
004C4AD2  4C 03 C2                        add r8, rdx
004C4AD5  4C 3B C2                        cmp r8, rdx
004C4AD8  0F 82 DC 00 00 00               jb 0x1404c4bba
004C4ADE  49 8B D0                        mov rdx, r8
004C4AE1  41 03 CD                        add ecx, r13d
004C4AE4  EB D6                           jmp 0x1404c4abc
004C4AE6  4C 8D 42 04                     lea r8, [rdx + 4]
004C4AEA  4C 3B C2                        cmp r8, rdx
004C4AED  0F 82 C7 00 00 00               jb 0x1404c4bba
004C4AF3  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
004C4AF6  48 8D 42 08                     lea rax, [rdx + 8]
004C4AFA  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
004C4AFE  48 3B C1                        cmp rax, rcx
004C4B01  0F 87 00 01 00 00               ja 0x1404c4c07
004C4B07  C7 02 04 00 00 00               mov dword ptr [rdx], 4
004C4B0D  45 89 38                        mov dword ptr [r8], r15d
004C4B10  44 01 2E                        add dword ptr [rsi], r13d
004C4B13  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
004C4B17  48 85 D2                        test rdx, rdx
004C4B1A  75 13                           jne 0x1404c4b2f
004C4B1C  8B 46 04                        mov eax, dword ptr [rsi + 4]
004C4B1F  8D 48 0C                        lea ecx, [rax + 0xc]
004C4B22  3B C8                           cmp ecx, eax
004C4B24  0F 82 8C 00 00 00               jb 0x1404c4bb6
004C4B2A  89 4E 04                        mov dword ptr [rsi + 4], ecx
004C4B2D  EB 4D                           jmp 0x1404c4b7c
004C4B2F  44 8B 0E                        mov r9d, dword ptr [rsi]
004C4B32  33 C9                           xor ecx, ecx
004C4B34  41 3B C9                        cmp ecx, r9d
004C4B37  73 1D                           jae 0x1404c4b56
004C4B39  8B 02                           mov eax, dword ptr [rdx]
004C4B3B  83 C0 04                        add eax, 4
004C4B3E  83 F8 04                        cmp eax, 4
004C4B41  72 77                           jb 0x1404c4bba
004C4B43  44 8B C0                        mov r8d, eax
004C4B46  4C 03 C2                        add r8, rdx
004C4B49  4C 3B C2                        cmp r8, rdx
004C4B4C  72 6C                           jb 0x1404c4bba
004C4B4E  49 8B D0                        mov rdx, r8
004C4B51  41 03 CD                        add ecx, r13d
004C4B54  EB DE                           jmp 0x1404c4b34
004C4B56  4C 8D 42 04                     lea r8, [rdx + 4]
004C4B5A  4C 3B C2                        cmp r8, rdx
004C4B5D  72 5B                           jb 0x1404c4bba
004C4B5F  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
004C4B62  48 8D 42 0C                     lea rax, [rdx + 0xc]
004C4B66  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
004C4B6A  48 3B C1                        cmp rax, rcx
004C4B6D  0F 87 94 00 00 00               ja 0x1404c4c07
004C4B73  C7 02 08 00 00 00               mov dword ptr [rdx], 8
004C4B79  4D 89 30                        mov qword ptr [r8], r14
004C4B7C  44 01 2E                        add dword ptr [rsi], r13d
004C4B7F  4D 85 E4                        test r12, r12
004C4B82  75 0E                           jne 0x1404c4b92
004C4B84  85 ED                           test ebp, ebp
004C4B86  74 0E                           je 0x1404c4b96
004C4B88  BB 0D 00 00 C0                  mov ebx, 0xc000000d
004C4B8D  E9 1F 01 00 00                  jmp 0x1404c4cb1
004C4B92  85 ED                           test ebp, ebp
004C4B94  74 F2                           je 0x1404c4b88
004C4B96  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
004C4B9A  48 85 D2                        test rdx, rdx
004C4B9D  75 22                           jne 0x1404c4bc1
004C4B9F  83 C5 04                        add ebp, 4
004C4BA2  83 FD 04                        cmp ebp, 4
004C4BA5  72 13                           jb 0x1404c4bba
004C4BA7  8B 46 04                        mov eax, dword ptr [rsi + 4]
004C4BAA  8D 0C 28                        lea ecx, [rax + rbp]
004C4BAD  3B C8                           cmp ecx, eax
004C4BAF  72 05                           jb 0x1404c4bb6
004C4BB1  89 4E 04                        mov dword ptr [rsi + 4], ecx
004C4BB4  EB 6D                           jmp 0x1404c4c23
004C4BB6  83 4E 04 FF                     or dword ptr [rsi + 4], 0xffffffff
004C4BBA  8B DF                           mov ebx, edi
004C4BBC  E9 F0 00 00 00                  jmp 0x1404c4cb1
004C4BC1  44 8B 0E                        mov r9d, dword ptr [rsi]
004C4BC4  33 C9                           xor ecx, ecx
004C4BC6  41 3B C9                        cmp ecx, r9d
004C4BC9  73 1D                           jae 0x1404c4be8
004C4BCB  8B 02                           mov eax, dword ptr [rdx]
004C4BCD  83 C0 04                        add eax, 4
004C4BD0  83 F8 04                        cmp eax, 4
004C4BD3  72 E5                           jb 0x1404c4bba
004C4BD5  44 8B C0                        mov r8d, eax
004C4BD8  4C 03 C2                        add r8, rdx
004C4BDB  4C 3B C2                        cmp r8, rdx
004C4BDE  72 DA                           jb 0x1404c4bba
004C4BE0  49 8B D0                        mov rdx, r8
004C4BE3  41 03 CD                        add ecx, r13d
004C4BE6  EB DE                           jmp 0x1404c4bc6
004C4BE8  4C 8D 4A 04                     lea r9, [rdx + 4]
004C4BEC  4C 3B CA                        cmp r9, rdx
004C4BEF  72 C9                           jb 0x1404c4bba
004C4BF1  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
004C4BF4  48 8D 45 04                     lea rax, [rbp + 4]
004C4BF8  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
004C4BFC  48 03 C2                        add rax, rdx
004C4BFF  44 8B C5                        mov r8d, ebp
004C4C02  48 3B C1                        cmp rax, rcx
004C4C05  76 0A                           jbe 0x1404c4c11
004C4C07  BB 23 00 00 C0                  mov ebx, 0xc0000023
004C4C0C  E9 A0 00 00 00                  jmp 0x1404c4cb1
004C4C11  89 2A                           mov dword ptr [rdx], ebp
004C4C13  4D 85 E4                        test r12, r12
004C4C16  74 0B                           je 0x1404c4c23
004C4C18  49 8B D4                        mov rdx, r12
004C4C1B  49 8B C9                        mov rcx, r9
004C4C1E  E8 1D 1C 20 00                  call 0x1406c6840
004C4C23  44 01 2E                        add dword ptr [rsi], r13d
004C4C26  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
004C4C2A  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
004C4C2F  48 85 D2                        test rdx, rdx
004C4C32  75 18                           jne 0x1404c4c4c
004C4C34  8B 46 04                        mov eax, dword ptr [rsi + 4]
004C4C37  8D 48 08                        lea ecx, [rax + 8]
004C4C3A  3B C8                           cmp ecx, eax
004C4C3C  0F 82 74 FF FF FF               jb 0x1404c4bb6
004C4C42  44 01 2E                        add dword ptr [rsi], r13d
004C4C45  33 DB                           xor ebx, ebx
004C4C47  89 4E 04                        mov dword ptr [rsi + 4], ecx
004C4C4A  EB 65                           jmp 0x1404c4cb1
004C4C4C  44 8B 16                        mov r10d, dword ptr [rsi]
004C4C4F  33 C9                           xor ecx, ecx
004C4C51  41 3B CA                        cmp ecx, r10d
004C4C54  73 25                           jae 0x1404c4c7b
004C4C56  8B 02                           mov eax, dword ptr [rdx]
004C4C58  83 C0 04                        add eax, 4
004C4C5B  83 F8 04                        cmp eax, 4
004C4C5E  0F 82 56 FF FF FF               jb 0x1404c4bba
004C4C64  44 8B C8                        mov r9d, eax
004C4C67  4C 03 CA                        add r9, rdx
004C4C6A  4C 3B CA                        cmp r9, rdx
004C4C6D  0F 82 47 FF FF FF               jb 0x1404c4bba
004C4C73  49 8B D1                        mov rdx, r9
004C4C76  41 03 CD                        add ecx, r13d
004C4C79  EB D6                           jmp 0x1404c4c51
004C4C7B  4C 8D 4A 04                     lea r9, [rdx + 4]
004C4C7F  4C 3B CA                        cmp r9, rdx
004C4C82  0F 82 32 FF FF FF               jb 0x1404c4bba
004C4C88  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
004C4C8B  48 8D 42 08                     lea rax, [rdx + 8]
004C4C8F  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
004C4C93  33 DB                           xor ebx, ebx
004C4C95  48 3B C1                        cmp rax, rcx
004C4C98  0F 87 69 FF FF FF               ja 0x1404c4c07
004C4C9E  C7 02 04 00 00 00               mov dword ptr [rdx], 4
004C4CA4  45 89 01                        mov dword ptr [r9], r8d
004C4CA7  44 01 2E                        add dword ptr [rsi], r13d
004C4CAA  EB 05                           jmp 0x1404c4cb1
004C4CAC  BB 95 00 00 C0                  mov ebx, 0xc0000095
004C4CB1  4D 85 E4                        test r12, r12
004C4CB4  74 11                           je 0x1404c4cc7
004C4CB6  33 D2                           xor edx, edx
004C4CB8  49 8B CC                        mov rcx, r12
004C4CBB  E8 B0 DB 6B 00                  call 0x140b82870
004C4CC0  EB 05                           jmp 0x1404c4cc7
004C4CC2  BB 95 00 00 C0                  mov ebx, 0xc0000095
004C4CC7  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
004C4CCC  8B C3                           mov eax, ebx
004C4CCE  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
004C4CD3  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
004C4CD8  48 83 C4 20                     add rsp, 0x20
004C4CDC  41 5F                           pop r15
004C4CDE  41 5E                           pop r14
004C4CE0  41 5D                           pop r13
004C4CE2  41 5C                           pop r12
004C4CE4  5F                              pop rdi
004C4CE5  C3                              ret
004C4CE6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_004C4874(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    *(unsigned int *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (32);
    v_r12 = 0;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_004C4905;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_004C4905;
    a2 = 0;
loc_004C48BC:
    if (0 >= 3) goto loc_004C48E3;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_004C4CC2;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_004C4CC2;
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
    goto loc_004C48BC;
loc_004C48E3:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_004C4CC2;
    v_r14 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r14 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_004C494E;
    if ((*(unsigned int *)(a1)) > 4) goto loc_004C490F;
loc_004C4905:
    goto loc_004C4CC7;
loc_004C490F:
    a2 = 0;
loc_004C4911:
    if (0 >= 4) goto loc_004C4938;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_004C4CC2;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_004C4CC2;
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
    goto loc_004C4911;
loc_004C4938:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_004C4CC2;
    v_rbp = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rbp = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) == 4) goto loc_004C4958;
loc_004C494E:
    goto loc_004C4CC7;
loc_004C4958:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp))) == 0) goto loc_004C4994;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp)))), (unsigned int)(0x20534C53ULL), a1);
    if (result != 0) goto loc_004C4983;
    goto loc_004C4CC7;
loc_004C4983:
    a2 = 0;
    result = memset(result, a2, (unsigned int)(*(unsigned int *)(v_rbp)), a1);
    a2 = 0;
    goto loc_004C4997;
loc_004C4994:
loc_004C4997:
    if (*(unsigned __int64 *)(v_rip + 11614826) == 0) goto loc_004C49BC;
    a1 = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(v_r12 + 1))) == 0) { a1 = result; }
    result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp)))), v_stack_p18, a1);
    goto loc_004C49C2;
loc_004C49BC:
loc_004C49C2:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp)) + 4)) < 4) goto loc_004C4CAC;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp)) + 4) + (20));
    if (((unsigned int)(result)) < 20) goto loc_004C4CAC;
    if (((unsigned int)(result + 8)) < ((unsigned int)(result))) goto loc_004C4CAC;
    if (((unsigned int)(result + 8 + 8)) < 8) goto loc_004C4CAC;
    a2 = (unsigned int)((result + 8 + 8 + 7) & (0xFFFFFFF8ULL));
    if (((unsigned int)(a2)) < ((unsigned int)(result + 8 + 8))) goto loc_004C4CAC;
    if (((unsigned int)(a2 + 8)) < ((unsigned int)(a2))) goto loc_004C4CAC;
    result = (unsigned int)((a2 + 8) + (4));
    if (((unsigned int)(result)) < 4) goto loc_004C4A42;
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_004C4A42;
    if (((unsigned int)(result + 4 + (unsigned int)(*(unsigned int *)(a2 + 16)) * 1)) < ((unsigned int)(result + 4))) goto loc_004C4A42;
    if (((unsigned int)(result + 4 + (unsigned int)(*(unsigned int *)(a2 + 16)) * 1 + 4)) < ((unsigned int)(result + 4 + (unsigned int)(*(unsigned int *)(a2 + 16)) * 1))) goto loc_004C4A47;
    v_rbx = (unsigned int)(((unsigned int)(0xC0000017ULL)) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    goto loc_004C4A49;
loc_004C4A42:
loc_004C4A47:
loc_004C4A49:
    if (sign_flag) goto loc_004C4CB1;
    if (a4 == 0) goto loc_004C4B88;
    v_rbx = 0;
    *(unsigned int *)(a4 + 4) = (unsigned int)(result + 8);
    if ((unsigned int)(result + 8) != 0) goto loc_004C4A6A;
    goto loc_004C4A8E;
loc_004C4A6A:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result + 8)), (unsigned int)(0x20534C53ULL), (unsigned int)(*(unsigned int *)(a2 + 32)));
    if (result != 0) goto loc_004C4A88;
    goto loc_004C4A8E;
loc_004C4A88:
    *(unsigned __int64 *)(a4 + 8) = result;
loc_004C4A8E:
    if (sign_flag) goto loc_004C4CB1;
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_004C4AB7;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_004C4BB6;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_004C4B10;
loc_004C4AB7:
    a1 = 0;
loc_004C4ABC:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_004C4AE6;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_004C4BBA;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_004C4BBA;
    a1 = (unsigned int)((a1) + ((unsigned int)(v_r12 + 1)));
    goto loc_004C4ABC;
loc_004C4AE6:
    if ((a3 + 4) < a3) goto loc_004C4BBA;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_004C4C07;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)(0xC00000BBULL));
loc_004C4B10:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_004C4B2F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_004C4BB6;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12);
    goto loc_004C4B7C;
loc_004C4B2F:
    a1 = 0;
loc_004C4B34:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_004C4B56;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_004C4BBA;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_004C4BBA;
    a1 = (unsigned int)((a1) + ((unsigned int)(v_r12 + 1)));
    goto loc_004C4B34;
loc_004C4B56:
    if ((a3 + 4) < a3) goto loc_004C4BBA;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) > a1) goto loc_004C4C07;
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)(a3 + 4) = *(unsigned __int64 *)(v_r14);
loc_004C4B7C:
    if (result != 0) goto loc_004C4B92;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp))) == 0) goto loc_004C4B96;
loc_004C4B88:
    goto loc_004C4CB1;
loc_004C4B92:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp))) == 0) goto loc_004C4B88;
loc_004C4B96:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_004C4BC1;
    v_rbp = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp))) + (4));
    if (((unsigned int)(v_rbp)) < 4) goto loc_004C4BBA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + v_rbp * 1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_004C4BB6;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + v_rbp * 1);
    goto loc_004C4C23;
loc_004C4BB6:
loc_004C4BBA:
    goto loc_004C4CB1;
loc_004C4BC1:
    a1 = 0;
loc_004C4BC6:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_004C4BE8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_004C4BBA;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_004C4BBA;
    a1 = (unsigned int)((a1) + ((unsigned int)(v_r12 + 1)));
    goto loc_004C4BC6;
loc_004C4BE8:
    if ((a3 + 4) < a3) goto loc_004C4BBA;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    result = (v_rbp + 4) + (a3);
    if (result <= a1) goto loc_004C4C11;
loc_004C4C07:
    goto loc_004C4CB1;
loc_004C4C11:
    *(unsigned int *)(a3) = (unsigned int)(v_rbp);
    if (result != 0) {
        a2 = result;
        a1 = a3 + 4;
        result = memcpy(a1, a2, (unsigned int)((unsigned int)(v_rbp)), a3 + 4);
    }
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_004C4C4C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_004C4BB6;
    v_rbx = 0;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_004C4CB1;
loc_004C4C4C:
    a1 = 0;
loc_004C4C51:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_004C4C7B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_004C4BBA;
    a4 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a4 < (*(unsigned __int64 *)(a4 + 8))) goto loc_004C4BBA;
    a1 = (unsigned int)((a1) + ((unsigned int)(v_r12 + 1)));
    goto loc_004C4C51;
loc_004C4C7B:
    if ((a4 + 4) < a4) goto loc_004C4BBA;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    v_rbx = 0;
    if ((a4 + 8) > a1) goto loc_004C4C07;
    *(unsigned int *)(a4) = 4;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(v_stack_p18));
    goto loc_004C4CB1;
loc_004C4CAC:
loc_004C4CB1:
    if (result == 0) goto loc_004C4CC7;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(v_stack_p18), a4 + 4);
    goto loc_004C4CC7;
loc_004C4CC2:
loc_004C4CC7:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_004C4874(void *Arg1, void *Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (32);
    local_r12 = 0;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_004C4905;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_004C4905;
    Arg2 = 0;
loc_004C48BC:
    if (0 >= 3) goto loc_004C48E3;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_004C4CC2;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_004C4CC2;
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
    goto loc_004C48BC;
loc_004C48E3:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_004C4CC2;
    local_r14 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r14 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_004C494E;
    if ((*(uint32_t *)(arg1)) > 4) goto loc_004C490F;
loc_004C4905:
    goto loc_004C4CC7;
loc_004C490F:
    Arg2 = 0;
loc_004C4911:
    if (0 >= 4) goto loc_004C4938;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_004C4CC2;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_004C4CC2;
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
    goto loc_004C4911;
loc_004C4938:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_004C4CC2;
    local_rbp = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rbp = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) == 4) goto loc_004C4958;
loc_004C494E:
    goto loc_004C4CC7;
loc_004C4958:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp))) == 0) goto loc_004C4994;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp)))), (uint32_t)(0x20534C53ULL), Arg1);
    if (result != 0) goto loc_004C4983;
    goto loc_004C4CC7;
loc_004C4983:
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(*(uint32_t *)(local_rbp)), Arg1);
    Arg2 = 0;
    goto loc_004C4997;
loc_004C4994:
loc_004C4997:
    if (*(uint64_t *)(v_rip + 0xB13A6A) == 0) goto loc_004C49BC;
    Arg1 = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(local_r12 + 1))) == 0) { Arg1 = result; }
    result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp)))), v_stack_p18, Arg1);
    goto loc_004C49C2;
loc_004C49BC:
loc_004C49C2:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp)) + 4)) < 4) goto loc_004C4CAC;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp)) + 4) + (20));
    if (((uint32_t)(result)) < 20) goto loc_004C4CAC;
    if (((uint32_t)(result + 8)) < ((uint32_t)(result))) goto loc_004C4CAC;
    if (((uint32_t)(result + 8 + 8)) < 8) goto loc_004C4CAC;
    Arg2 = (uint32_t)((result + 8 + 8 + 7) & (0xFFFFFFF8ULL));
    if (((uint32_t)(Arg2)) < ((uint32_t)(result + 8 + 8))) goto loc_004C4CAC;
    if (((uint32_t)(Arg2 + 8)) < ((uint32_t)(Arg2))) goto loc_004C4CAC;
    result = (uint32_t)((Arg2 + 8) + (4));
    if (((uint32_t)(result)) < 4) goto loc_004C4A42;
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_004C4A42;
    if (((uint32_t)(result + 4 + (uint32_t)(*(uint32_t *)(arg2 + 0x10)) * 1)) < ((uint32_t)(result + 4))) goto loc_004C4A42;
    if (((uint32_t)(result + 4 + (uint32_t)(*(uint32_t *)(arg2 + 0x10)) * 1 + 4)) < ((uint32_t)(result + 4 + (uint32_t)(*(uint32_t *)(arg2 + 0x10)) * 1))) goto loc_004C4A47;
    local_rbx = (uint32_t)(((uint32_t)(0xC0000017ULL)) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    goto loc_004C4A49;
loc_004C4A42:
loc_004C4A47:
loc_004C4A49:
    if (sign_flag) goto loc_004C4CB1;
    if (Arg4 == 0) goto loc_004C4B88;
    local_rbx = 0;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(result + 8);
    if ((uint32_t)(result + 8) != 0) goto loc_004C4A6A;
    goto loc_004C4A8E;
loc_004C4A6A:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result + 8)), (uint32_t)(0x20534C53ULL), (uint32_t)(*(uint32_t *)(arg2 + 0x20)));
    if (result != 0) goto loc_004C4A88;
    goto loc_004C4A8E;
loc_004C4A88:
    *(uint64_t *)(Arg4 + 0x8) = result;
loc_004C4A8E:
    if (sign_flag) goto loc_004C4CB1;
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_004C4AB7;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_004C4BB6;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_004C4B10;
loc_004C4AB7:
    Arg1 = 0;
loc_004C4ABC:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_004C4AE6;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_004C4BBA;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_004C4BBA;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r12 + 1)));
    goto loc_004C4ABC;
loc_004C4AE6:
    if ((Arg3 + 4) < Arg3) goto loc_004C4BBA;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_004C4C07;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)(0xC00000BBULL));
loc_004C4B10:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_004C4B2F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_004C4BB6;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12);
    goto loc_004C4B7C;
loc_004C4B2F:
    Arg1 = 0;
loc_004C4B34:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_004C4B56;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_004C4BBA;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_004C4BBA;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r12 + 1)));
    goto loc_004C4B34;
loc_004C4B56:
    if ((Arg3 + 4) < Arg3) goto loc_004C4BBA;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 12) > Arg1) goto loc_004C4C07;
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)(Arg3 + 0x4) = *(uint64_t *)(local_r14);
loc_004C4B7C:
    if (result != 0) goto loc_004C4B92;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp))) == 0) goto loc_004C4B96;
loc_004C4B88:
    goto loc_004C4CB1;
loc_004C4B92:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp))) == 0) goto loc_004C4B88;
loc_004C4B96:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_004C4BC1;
    local_rbp = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp))) + (4));
    if (((uint32_t)(local_rbp)) < 4) goto loc_004C4BBA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + local_rbp * 1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_004C4BB6;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + local_rbp * 1);
    goto loc_004C4C23;
loc_004C4BB6:
loc_004C4BBA:
    goto loc_004C4CB1;
loc_004C4BC1:
    Arg1 = 0;
loc_004C4BC6:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_004C4BE8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_004C4BBA;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_004C4BBA;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r12 + 1)));
    goto loc_004C4BC6;
loc_004C4BE8:
    if ((Arg3 + 4) < Arg3) goto loc_004C4BBA;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    result = (local_rbp + 4) + (Arg3);
    if (result <= Arg1) goto loc_004C4C11;
loc_004C4C07:
    goto loc_004C4CB1;
loc_004C4C11:
    *(uint32_t *)(Arg3) = (uint32_t)(local_rbp);
    if (result != 0) {
        Arg2 = result;
        Arg1 = Arg3 + 4;
        result = memcpy(Arg1, Arg2, (uint32_t)((uint32_t)(local_rbp)), Arg3 + 4);
    }
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_004C4C4C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_004C4BB6;
    local_rbx = 0;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_004C4CB1;
loc_004C4C4C:
    Arg1 = 0;
loc_004C4C51:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_004C4C7B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_004C4BBA;
    Arg4 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg4 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_004C4BBA;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r12 + 1)));
    goto loc_004C4C51;
loc_004C4C7B:
    if ((Arg4 + 4) < Arg4) goto loc_004C4BBA;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    local_rbx = 0;
    if ((Arg4 + 8) > Arg1) goto loc_004C4C07;
    *(uint32_t *)(Arg4) = 4;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(v_stack_p18));
    goto loc_004C4CB1;
loc_004C4CAC:
loc_004C4CB1:
    if (result == 0) goto loc_004C4CC7;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(v_stack_p18), Arg4 + 4);
    goto loc_004C4CC7;
loc_004C4CC2:
loc_004C4CC7:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x20` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C4874&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
