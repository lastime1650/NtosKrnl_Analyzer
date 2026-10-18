# sub_00AD7D60

- RVA: `0x00AD7D60`–`0x00AD81A9` (길이 `1,097` bytes)
- VA: `0x0000000140AD7D60`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BF128`
- 디코드: `320`개 명령, `1,097/1,097` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00AD7E8C` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (function, `0x00458B60`)
- `0x00AD7EC1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD7EE1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AD7F51` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AD7FA8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD816F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AD8185` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x0096A70C`

### Static image references
- `0x00AD7D7C` → RVA `0x00E0A740` (`.data`; read)
- `0x00AD7F30` → RVA `0x00FD83A0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00AD7E8C` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (`PAGE` → `.text`)
  - `0x00AD7EC1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD7EE1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AD7F51` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AD7FA8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD816F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AD8185` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AD7D60  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00AD7D65  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00AD7D6A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00AD7D6F  57                              push rdi
00AD7D70  41 54                           push r12
00AD7D72  41 55                           push r13
00AD7D74  41 56                           push r14
00AD7D76  41 57                           push r15
00AD7D78  48 83 EC 50                     sub rsp, 0x50
00AD7D7C  48 8B 05 BD 29 33 00            mov rax, qword ptr [rip + 0x3329bd]
00AD7D83  48 33 C4                        xor rax, rsp
00AD7D86  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AD7D8B  45 33 E4                        xor r12d, r12d
00AD7D8E  0F 57 C0                        xorps xmm0, xmm0
00AD7D91  4D 8B F1                        mov r14, r9
00AD7D94  4C 8B EA                        mov r13, rdx
00AD7D97  48 8B D9                        mov rbx, rcx
00AD7D9A  0F 11 44 24 38                  movups xmmword ptr [rsp + 0x38], xmm0
00AD7D9F  48 85 D2                        test rdx, rdx
00AD7DA2  75 0A                           jne 0x140ad7dae
00AD7DA4  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD7DA9  E9 CD 03 00 00                  jmp 0x140ad817b
00AD7DAE  4D 85 F6                        test r14, r14
00AD7DB1  74 F1                           je 0x140ad7da4
00AD7DB3  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00AD7DB7  48 85 C9                        test rcx, rcx
00AD7DBA  74 E8                           je 0x140ad7da4
00AD7DBC  83 3B 03                        cmp dword ptr [rbx], 3
00AD7DBF  76 E3                           jbe 0x140ad7da4
00AD7DC1  48 8B C1                        mov rax, rcx
00AD7DC4  45 8B C4                        mov r8d, r12d
00AD7DC7  44 8B 08                        mov r9d, dword ptr [rax]
00AD7DCA  48 8D 50 04                     lea rdx, [rax + 4]
00AD7DCE  41 83 F8 03                     cmp r8d, 3
00AD7DD2  73 1B                           jae 0x140ad7def
00AD7DD4  48 3B D0                        cmp rdx, rax
00AD7DD7  0F 82 99 03 00 00               jb 0x140ad8176
00AD7DDD  4A 8D 04 0A                     lea rax, [rdx + r9]
00AD7DE1  48 3B C2                        cmp rax, rdx
00AD7DE4  0F 82 8C 03 00 00               jb 0x140ad8176
00AD7DEA  41 FF C0                        inc r8d
00AD7DED  EB D8                           jmp 0x140ad7dc7
00AD7DEF  48 3B D0                        cmp rdx, rax
00AD7DF2  0F 82 7E 03 00 00               jb 0x140ad8176
00AD7DF8  45 85 C9                        test r9d, r9d
00AD7DFB  49 8B EC                        mov rbp, r12
00AD7DFE  48 0F 45 EA                     cmovne rbp, rdx
00AD7E02  41 83 F9 08                     cmp r9d, 8
00AD7E06  74 0A                           je 0x140ad7e12
00AD7E08  BB 23 00 00 C0                  mov ebx, 0xc0000023
00AD7E0D  E9 69 03 00 00                  jmp 0x140ad817b
00AD7E12  83 3B 04                        cmp dword ptr [rbx], 4
00AD7E15  48 8B 6D 00                     mov rbp, qword ptr [rbp]
00AD7E19  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
00AD7E1E  76 84                           jbe 0x140ad7da4
00AD7E20  45 8B CC                        mov r9d, r12d
00AD7E23  44 8B 01                        mov r8d, dword ptr [rcx]
00AD7E26  48 8D 51 04                     lea rdx, [rcx + 4]
00AD7E2A  41 83 F9 04                     cmp r9d, 4
00AD7E2E  73 1B                           jae 0x140ad7e4b
00AD7E30  48 3B D1                        cmp rdx, rcx
00AD7E33  0F 82 3D 03 00 00               jb 0x140ad8176
00AD7E39  4A 8D 0C 02                     lea rcx, [rdx + r8]
00AD7E3D  48 3B CA                        cmp rcx, rdx
00AD7E40  0F 82 30 03 00 00               jb 0x140ad8176
00AD7E46  41 FF C1                        inc r9d
00AD7E49  EB D8                           jmp 0x140ad7e23
00AD7E4B  48 3B D1                        cmp rdx, rcx
00AD7E4E  0F 82 22 03 00 00               jb 0x140ad8176
00AD7E54  45 85 C0                        test r8d, r8d
00AD7E57  49 8B F4                        mov rsi, r12
00AD7E5A  48 0F 45 F2                     cmovne rsi, rdx
00AD7E5E  75 0A                           jne 0x140ad7e6a
00AD7E60  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00AD7E65  E9 11 03 00 00                  jmp 0x140ad817b
00AD7E6A  41 F6 C0 01                     test r8b, 1
00AD7E6E  75 F0                           jne 0x140ad7e60
00AD7E70  49 8B C0                        mov rax, r8
00AD7E73  4D 8B D8                        mov r11, r8
00AD7E76  48 D1 E8                        shr rax, 1
00AD7E79  66 44 3B 64 46 FE               cmp r12w, word ptr [rsi + rax*2 - 2]
00AD7E7F  75 DF                           jne 0x140ad7e60
00AD7E81  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
00AD7E86  49 8B D3                        mov rdx, r11
00AD7E89  48 8B CE                        mov rcx, rsi
00AD7E8C  E8 CF 0C 98 FF                  call 0x140458b60
00AD7E91  85 C0                           test eax, eax
00AD7E93  78 CB                           js 0x140ad7e60
00AD7E95  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00AD7E9A  48 8D 41 02                     lea rax, [rcx + 2]
00AD7E9E  49 3B C3                        cmp rax, r11
00AD7EA1  75 BD                           jne 0x140ad7e60
00AD7EA3  48 D1 E9                        shr rcx, 1
00AD7EA6  8D 0C 4D 02 00 00 00            lea ecx, [rcx*2 + 2]
00AD7EAD  85 C9                           test ecx, ecx
00AD7EAF  74 AF                           je 0x140ad7e60
00AD7EB1  44 8B F9                        mov r15d, ecx
00AD7EB4  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD7EBA  8B D1                           mov edx, ecx
00AD7EBC  B9 00 01 00 00                  mov ecx, 0x100
00AD7EC1  E8 2A A2 0A 00                  call 0x140b820f0
00AD7EC6  48 8B F8                        mov rdi, rax
00AD7EC9  48 85 C0                        test rax, rax
00AD7ECC  75 0A                           jne 0x140ad7ed8
00AD7ECE  BB 17 00 00 C0                  mov ebx, 0xc0000017
00AD7ED3  E9 A3 02 00 00                  jmp 0x140ad817b
00AD7ED8  4D 8B C7                        mov r8, r15
00AD7EDB  48 8B D6                        mov rdx, rsi
00AD7EDE  48 8B C8                        mov rcx, rax
00AD7EE1  E8 5A E9 BE FF                  call 0x1406c6840
00AD7EE6  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00AD7EEA  48 85 C0                        test rax, rax
00AD7EED  75 0A                           jne 0x140ad7ef9
00AD7EEF  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD7EF4  E9 6C 02 00 00                  jmp 0x140ad8165
00AD7EF9  83 3B 05                        cmp dword ptr [rbx], 5
00AD7EFC  76 F1                           jbe 0x140ad7eef
00AD7EFE  41 8B D4                        mov edx, r12d
00AD7F01  44 8B 10                        mov r10d, dword ptr [rax]
00AD7F04  48 8D 48 04                     lea rcx, [rax + 4]
00AD7F08  83 FA 05                        cmp edx, 5
00AD7F0B  73 1A                           jae 0x140ad7f27
00AD7F0D  48 3B C8                        cmp rcx, rax
00AD7F10  0F 82 4A 02 00 00               jb 0x140ad8160
00AD7F16  4A 8D 04 11                     lea rax, [rcx + r10]
00AD7F1A  48 3B C1                        cmp rax, rcx
00AD7F1D  0F 82 3D 02 00 00               jb 0x140ad8160
00AD7F23  FF C2                           inc edx
00AD7F25  EB DA                           jmp 0x140ad7f01
00AD7F27  48 3B C8                        cmp rcx, rax
00AD7F2A  0F 82 30 02 00 00               jb 0x140ad8160
00AD7F30  48 8B 05 69 04 50 00            mov rax, qword ptr [rip + 0x500469]
00AD7F37  45 85 D2                        test r10d, r10d
00AD7F3A  49 8B D4                        mov rdx, r12
00AD7F3D  48 0F 45 D1                     cmovne rdx, rcx
00AD7F41  48 85 C0                        test rax, rax
00AD7F44  74 15                           je 0x140ad7f5b
00AD7F46  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
00AD7F4B  45 8B C2                        mov r8d, r10d
00AD7F4E  48 8B CF                        mov rcx, rdi
00AD7F51  E8 7A 2B BE FF                  call 0x1406baad0
00AD7F56  44 8B F8                        mov r15d, eax
00AD7F59  EB 06                           jmp 0x140ad7f61
00AD7F5B  41 BF 81 A2 00 C0               mov r15d, 0xc000a281
00AD7F61  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
00AD7F65  41 8B 55 20                     mov edx, dword ptr [r13 + 0x20]
00AD7F69  83 C0 40                        add eax, 0x40
00AD7F6C  83 F8 40                        cmp eax, 0x40
00AD7F6F  0F 82 EB 01 00 00               jb 0x140ad8160
00AD7F75  8D 48 04                        lea ecx, [rax + 4]
00AD7F78  3B C8                           cmp ecx, eax
00AD7F7A  0F 82 E0 01 00 00               jb 0x140ad8160
00AD7F80  8D 04 11                        lea eax, [rcx + rdx]
00AD7F83  BE 95 00 00 C0                  mov esi, 0xc0000095
00AD7F88  3B C1                           cmp eax, ecx
00AD7F8A  1B DB                           sbb ebx, ebx
00AD7F8C  23 DE                           and ebx, esi
00AD7F8E  0F 88 D1 01 00 00               js 0x140ad8165
00AD7F94  BA 28 00 00 00                  mov edx, 0x28
00AD7F99  B9 00 01 00 00                  mov ecx, 0x100
00AD7F9E  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD7FA4  41 89 56 04                     mov dword ptr [r14 + 4], edx
00AD7FA8  E8 43 A1 0A 00                  call 0x140b820f0
00AD7FAD  48 85 C0                        test rax, rax
00AD7FB0  75 08                           jne 0x140ad7fba
00AD7FB2  8D 5E 82                        lea ebx, [rsi - 0x7e]
00AD7FB5  E9 AB 01 00 00                  jmp 0x140ad8165
00AD7FBA  49 89 46 08                     mov qword ptr [r14 + 8], rax
00AD7FBE  41 0F BA EF 1C                  bts r15d, 0x1c
00AD7FC3  45 89 26                        mov dword ptr [r14], r12d
00AD7FC6  48 8B D0                        mov rdx, rax
00AD7FC9  48 85 C0                        test rax, rax
00AD7FCC  75 1D                           jne 0x140ad7feb
00AD7FCE  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00AD7FD2  8D 48 08                        lea ecx, [rax + 8]
00AD7FD5  3B C8                           cmp ecx, eax
00AD7FD7  72 06                           jb 0x140ad7fdf
00AD7FD9  41 89 4E 04                     mov dword ptr [r14 + 4], ecx
00AD7FDD  EB 57                           jmp 0x140ad8036
00AD7FDF  41 83 4E 04 FF                  or dword ptr [r14 + 4], 0xffffffff
00AD7FE4  8B DE                           mov ebx, esi
00AD7FE6  E9 7A 01 00 00                  jmp 0x140ad8165
00AD7FEB  41 8B CC                        mov ecx, r12d
00AD7FEE  41 3B CC                        cmp ecx, r12d
00AD7FF1  73 1C                           jae 0x140ad800f
00AD7FF3  8B 02                           mov eax, dword ptr [rdx]
00AD7FF5  83 C0 04                        add eax, 4
00AD7FF8  83 F8 04                        cmp eax, 4
00AD7FFB  72 E7                           jb 0x140ad7fe4
00AD7FFD  44 8B C0                        mov r8d, eax
00AD8000  4C 03 C2                        add r8, rdx
00AD8003  4C 3B C2                        cmp r8, rdx
00AD8006  72 DC                           jb 0x140ad7fe4
00AD8008  49 8B D0                        mov rdx, r8
00AD800B  FF C1                           inc ecx
00AD800D  EB DF                           jmp 0x140ad7fee
00AD800F  4C 8D 42 04                     lea r8, [rdx + 4]
00AD8013  4C 3B C2                        cmp r8, rdx
00AD8016  72 CC                           jb 0x140ad7fe4
00AD8018  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00AD801C  48 8D 42 08                     lea rax, [rdx + 8]
00AD8020  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
00AD8024  48 3B C1                        cmp rax, rcx
00AD8027  0F 87 8A 00 00 00               ja 0x140ad80b7
00AD802D  C7 02 04 00 00 00               mov dword ptr [rdx], 4
00AD8033  45 89 38                        mov dword ptr [r8], r15d
00AD8036  41 FF 06                        inc dword ptr [r14]
00AD8039  41 83 C8 FF                     or r8d, 0xffffffff
00AD803D  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00AD8041  48 85 D2                        test rdx, rdx
00AD8044  75 24                           jne 0x140ad806a
00AD8046  41 8B 56 04                     mov edx, dword ptr [r14 + 4]
00AD804A  41 8B C0                        mov eax, r8d
00AD804D  8D 4A 0C                        lea ecx, [rdx + 0xc]
00AD8050  3B CA                           cmp ecx, edx
00AD8052  0F 43 C1                        cmovae eax, ecx
00AD8055  1B DB                           sbb ebx, ebx
00AD8057  23 DE                           and ebx, esi
00AD8059  41 89 46 04                     mov dword ptr [r14 + 4], eax
00AD805D  3B CA                           cmp ecx, edx
00AD805F  73 69                           jae 0x140ad80ca
00AD8061  85 DB                           test ebx, ebx
00AD8063  79 68                           jns 0x140ad80cd
00AD8065  E9 FB 00 00 00                  jmp 0x140ad8165
00AD806A  45 8B 16                        mov r10d, dword ptr [r14]
00AD806D  41 8B CC                        mov ecx, r12d
00AD8070  41 3B CA                        cmp ecx, r10d
00AD8073  73 24                           jae 0x140ad8099
00AD8075  8B 02                           mov eax, dword ptr [rdx]
00AD8077  83 C0 04                        add eax, 4
00AD807A  83 F8 04                        cmp eax, 4
00AD807D  0F 82 61 FF FF FF               jb 0x140ad7fe4
00AD8083  44 8B C8                        mov r9d, eax
00AD8086  4C 03 CA                        add r9, rdx
00AD8089  4C 3B CA                        cmp r9, rdx
00AD808C  0F 82 52 FF FF FF               jb 0x140ad7fe4
00AD8092  49 8B D1                        mov rdx, r9
00AD8095  FF C1                           inc ecx
00AD8097  EB D7                           jmp 0x140ad8070
00AD8099  4C 8D 4A 04                     lea r9, [rdx + 4]
00AD809D  4C 3B CA                        cmp r9, rdx
00AD80A0  0F 82 3E FF FF FF               jb 0x140ad7fe4
00AD80A6  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00AD80AA  48 8D 42 0C                     lea rax, [rdx + 0xc]
00AD80AE  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
00AD80B2  48 3B C1                        cmp rax, rcx
00AD80B5  76 0A                           jbe 0x140ad80c1
00AD80B7  BB 23 00 00 C0                  mov ebx, 0xc0000023
00AD80BC  E9 A4 00 00 00                  jmp 0x140ad8165
00AD80C1  C7 02 08 00 00 00               mov dword ptr [rdx], 8
00AD80C7  49 89 29                        mov qword ptr [r9], rbp
00AD80CA  41 FF 06                        inc dword ptr [r14]
00AD80CD  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00AD80D1  48 85 D2                        test rdx, rdx
00AD80D4  75 21                           jne 0x140ad80f7
00AD80D6  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00AD80DA  8D 41 14                        lea eax, [rcx + 0x14]
00AD80DD  3B C1                           cmp eax, ecx
00AD80DF  44 0F 43 C0                     cmovae r8d, eax
00AD80E3  1B DB                           sbb ebx, ebx
00AD80E5  23 DE                           and ebx, esi
00AD80E7  45 89 46 04                     mov dword ptr [r14 + 4], r8d
00AD80EB  3B C1                           cmp eax, ecx
00AD80ED  72 76                           jb 0x140ad8165
00AD80EF  41 FF 06                        inc dword ptr [r14]
00AD80F2  41 8B DC                        mov ebx, r12d
00AD80F5  EB 6E                           jmp 0x140ad8165
00AD80F7  45 8B 0E                        mov r9d, dword ptr [r14]
00AD80FA  41 8B CC                        mov ecx, r12d
00AD80FD  41 3B C9                        cmp ecx, r9d
00AD8100  73 24                           jae 0x140ad8126
00AD8102  8B 02                           mov eax, dword ptr [rdx]
00AD8104  83 C0 04                        add eax, 4
00AD8107  83 F8 04                        cmp eax, 4
00AD810A  0F 82 D4 FE FF FF               jb 0x140ad7fe4
00AD8110  44 8B C0                        mov r8d, eax
00AD8113  4C 03 C2                        add r8, rdx
00AD8116  4C 3B C2                        cmp r8, rdx
00AD8119  0F 82 C5 FE FF FF               jb 0x140ad7fe4
00AD811F  49 8B D0                        mov rdx, r8
00AD8122  FF C1                           inc ecx
00AD8124  EB D7                           jmp 0x140ad80fd
00AD8126  4C 8D 42 04                     lea r8, [rdx + 4]
00AD812A  4C 3B C2                        cmp r8, rdx
00AD812D  0F 82 B1 FE FF FF               jb 0x140ad7fe4
00AD8133  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00AD8137  48 8D 42 14                     lea rax, [rdx + 0x14]
00AD813B  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
00AD813F  41 8B DC                        mov ebx, r12d
00AD8142  48 3B C1                        cmp rax, rcx
00AD8145  0F 87 6C FF FF FF               ja 0x140ad80b7
00AD814B  C7 02 10 00 00 00               mov dword ptr [rdx], 0x10
00AD8151  0F 10 44 24 38                  movups xmm0, xmmword ptr [rsp + 0x38]
00AD8156  F3 41 0F 7F 00                  movdqu xmmword ptr [r8], xmm0
00AD815B  41 FF 06                        inc dword ptr [r14]
00AD815E  EB 05                           jmp 0x140ad8165
00AD8160  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD8165  48 85 FF                        test rdi, rdi
00AD8168  74 11                           je 0x140ad817b
00AD816A  33 D2                           xor edx, edx
00AD816C  48 8B CF                        mov rcx, rdi
00AD816F  E8 FC A6 0A 00                  call 0x140b82870
00AD8174  EB 05                           jmp 0x140ad817b
00AD8176  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD817B  8B C3                           mov eax, ebx
00AD817D  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AD8182  48 33 CC                        xor rcx, rsp
00AD8185  E8 B6 44 BD FF                  call 0x1406ac640
00AD818A  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
00AD818F  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00AD8193  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
00AD8197  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00AD819B  49 8B E3                        mov rsp, r11
00AD819E  41 5F                           pop r15
00AD81A0  41 5E                           pop r14
00AD81A2  41 5D                           pop r13
00AD81A4  41 5C                           pop r12
00AD81A6  5F                              pop rdi
00AD81A7  C3                              ret
00AD81A8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00AD7D60(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (80);
    result = (*(unsigned __int64 *)(v_rip + 3353021)) ^ (v_rsp);
    v_stack_m30 = result;
    v_r12 = 0;
    v_stack_m40 = v_xmm0;
    if (a2 != 0) goto loc_00AD7DAE;
loc_00AD7DA4:
    goto loc_00AD817B;
loc_00AD7DAE:
    if (a4 == 0) goto loc_00AD7DA4;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00AD7DA4;
    if ((*(unsigned int *)((unsigned int)(0xC000000DULL))) <= 3) goto loc_00AD7DA4;
loc_00AD7DC7:
    if (0 >= 3) goto loc_00AD7DEF;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD8176;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD8176;
    a3 = (unsigned int)((0) + 1);
    goto loc_00AD7DC7;
loc_00AD7DEF:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD8176;
    v_rbp = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rbp = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) == 8) goto loc_00AD7E12;
    goto loc_00AD817B;
loc_00AD7E12:
    v_stack_m48 = 0;
    if ((*(unsigned int *)((unsigned int)(0xC0000023ULL))) <= 4) goto loc_00AD7DA4;
loc_00AD7E23:
    if (0 >= 4) goto loc_00AD7E4B;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD8176;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD8176;
    a4 = (unsigned int)((0) + 1);
    goto loc_00AD7E23;
loc_00AD7E4B:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD8176;
    v_rsi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rsi = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) goto loc_00AD7E6A;
loc_00AD7E60:
    goto loc_00AD817B;
loc_00AD7E6A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) & (1)) != 0) goto loc_00AD7E60;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) >> (1);
    if (0 != (*(unsigned __int16 *)(v_rsi + result * 2 - 2))) goto loc_00AD7E60;
    result = StringCbLengthW(v_rsi, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))), v_stack_m48, a4);
    if (sign_flag) goto loc_00AD7E60;
    if ((v_stack_m48 + 2) != ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) goto loc_00AD7E60;
    a1 = (v_stack_m48) >> (1);
    if ((unsigned int)(a1 * 2 + 2) == 0) goto loc_00AD7E60;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(a1 * 2 + 2)), (unsigned int)(0x20534C53ULL), a4);
    if (result != 0) goto loc_00AD7ED8;
    goto loc_00AD817B;
loc_00AD7ED8:
    result = memcpy(result, v_rsi, (unsigned int)((unsigned int)(a1 * 2 + 2)), a4);
    if (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) != 0) goto loc_00AD7EF9;
loc_00AD7EEF:
    goto loc_00AD8165;
loc_00AD7EF9:
    if ((*(unsigned int *)((unsigned int)(0xC000000DULL))) <= 5) goto loc_00AD7EEF;
loc_00AD7F01:
    if (0 >= 5) goto loc_00AD7F27;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) goto loc_00AD8160;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4)) goto loc_00AD8160;
    a2 = (unsigned int)((0) + 1);
    goto loc_00AD7F01;
loc_00AD7F27:
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1)) goto loc_00AD8160;
    a2 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8)))) != 0) { a2 = *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4; }
    if (*(unsigned __int64 *)(v_rip + 5244009) == 0) goto loc_00AD7F5B;
    result = guard_dispatch_icall(result, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))))), v_stack_m40);
    goto loc_00AD7F61;
loc_00AD7F5B:
loc_00AD7F61:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) + (64));
    if (((unsigned int)(result)) < 64) goto loc_00AD8160;
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_00AD8160;
    v_rbx = (unsigned int)(((unsigned int)(0xC000000DULL)) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (sign_flag) goto loc_00AD8165;
    *(unsigned int *)(a4 + 4) = 40;
    result = ExAllocatePool2(256, 40, (unsigned int)(0x20534C53ULL), v_stack_m40);
    if (result != 0) goto loc_00AD7FBA;
    goto loc_00AD8165;
loc_00AD7FBA:
    *(unsigned __int64 *)(a4 + 8) = result;
    *(unsigned int *)(a4) = 0;
    if (result != 0) goto loc_00AD7FEB;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD7FDF;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00AD8036;
loc_00AD7FDF:
loc_00AD7FE4:
    goto loc_00AD8165;
loc_00AD7FEB:
loc_00AD7FEE:
    if (0 >= 0) goto loc_00AD800F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD7FE4;
    a3 = ((unsigned int)((unsigned int)(result))) + (result);
    if (a3 < result) goto loc_00AD7FE4;
    a1 = (unsigned int)((0) + 1);
    goto loc_00AD7FEE;
loc_00AD800F:
    if ((a3 + 4) < a3) goto loc_00AD7FE4;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_00AD80B7;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)(0xC000A281ULL));
loc_00AD8036:
    a3 = (unsigned int)((a3 + 4) | (0xFFFFFFFFULL));
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD806A;
    result = (unsigned int)((unsigned int)(a3));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12); }
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)))) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    *(unsigned int *)(a4 + 4) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD80CA;
    if (!sign_flag) goto loc_00AD80CD;
    goto loc_00AD8165;
loc_00AD806A:
loc_00AD8070:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD8099;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a4 + 4))))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD7FE4;
    a4 = ((unsigned int)((unsigned int)(result))) + ((unsigned int)(*(unsigned int *)(a4 + 4)));
    if (a4 < ((unsigned int)(*(unsigned int *)(a4 + 4)))) goto loc_00AD7FE4;
    a1 = (unsigned int)((0) + 1);
    goto loc_00AD8070;
loc_00AD8099:
    if ((a4 + 4) < a4) goto loc_00AD7FE4;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a4 + 12) <= a1) goto loc_00AD80C1;
loc_00AD80B7:
    goto loc_00AD8165;
loc_00AD80C1:
    *(unsigned int *)(a4) = 8;
    *(unsigned __int64 *)(a4 + 4) = *(unsigned __int64 *)(v_rbp);
loc_00AD80CA:
loc_00AD80CD:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD80F7;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 20)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { a3 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 20); }
    v_rbx = (unsigned int)(((unsigned int)(0xC0000023ULL)) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    *(unsigned int *)(a4 + 4) = (unsigned int)(a3);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 20)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD8165;
    goto loc_00AD8165;
loc_00AD80F7:
loc_00AD80FD:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD8126;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD7FE4;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00AD7FE4;
    a1 = (unsigned int)((0) + 1);
    goto loc_00AD80FD;
loc_00AD8126:
    if ((a3 + 4) < a3) goto loc_00AD7FE4;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 20) > a1) goto loc_00AD80B7;
    *(unsigned int *)(a3) = 16;
    *(unsigned __int64 *)(a3 + 4) = v_xmm0;
    goto loc_00AD8165;
loc_00AD8160:
loc_00AD8165:
    if (result == 0) goto loc_00AD817B;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3 + 4, (unsigned int)(*(unsigned int *)(a4)));
    goto loc_00AD817B;
loc_00AD8176:
loc_00AD817B:
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3 + 4, (unsigned int)(*(unsigned int *)(a4)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00AD7D60(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (80);
    result = (*(uint64_t *)(v_rip + 0x3329BD)) ^ (local_rsp);
    v_stack_m30 = result;
    local_r12 = 0;
    v_stack_m40 = v_xmm0;
    if (Arg2 != NULL) goto loc_00AD7DAE;
loc_00AD7DA4:
    goto loc_00AD817B;
loc_00AD7DAE:
    if (Arg4 == 0) goto loc_00AD7DA4;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00AD7DA4;
    if ((*(uint32_t *)((uint32_t)(0xC000000DULL))) <= 3) goto loc_00AD7DA4;
loc_00AD7DC7:
    if (0 >= 3) goto loc_00AD7DEF;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD8176;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD8176;
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00AD7DC7;
loc_00AD7DEF:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD8176;
    local_rbp = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rbp = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) == 8) goto loc_00AD7E12;
    goto loc_00AD817B;
loc_00AD7E12:
    v_stack_m48 = 0;
    if ((*(uint32_t *)((uint32_t)(0xC0000023ULL))) <= 4) goto loc_00AD7DA4;
loc_00AD7E23:
    if (0 >= 4) goto loc_00AD7E4B;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD8176;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD8176;
    Arg4 = (uint32_t)((0) + 1);
    goto loc_00AD7E23;
loc_00AD7E4B:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD8176;
    local_rsi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rsi = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) goto loc_00AD7E6A;
loc_00AD7E60:
    goto loc_00AD817B;
loc_00AD7E6A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) & (1)) != 0) goto loc_00AD7E60;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) >> (1);
    if (0 != (*(uint16_t *)(local_rsi + result * 2 - 0x2))) goto loc_00AD7E60;
    result = StringCbLengthW(local_rsi, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))), v_stack_m48, Arg4);
    if (sign_flag) goto loc_00AD7E60;
    if ((v_stack_m48 + 2) != ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) goto loc_00AD7E60;
    Arg1 = (v_stack_m48) >> (1);
    if ((uint32_t)(Arg1 * 2 + 2) == 0) goto loc_00AD7E60;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(Arg1 * 2 + 2)), (uint32_t)(0x20534C53ULL), Arg4);
    if (result != 0) goto loc_00AD7ED8;
    goto loc_00AD817B;
loc_00AD7ED8:
    result = memcpy(result, local_rsi, (uint32_t)((uint32_t)(Arg1 * 2 + 2)), Arg4);
    if (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) != 0) goto loc_00AD7EF9;
loc_00AD7EEF:
    goto loc_00AD8165;
loc_00AD7EF9:
    if ((*(uint32_t *)((uint32_t)(0xC000000DULL))) <= 5) goto loc_00AD7EEF;
loc_00AD7F01:
    if (0 >= 5) goto loc_00AD7F27;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) goto loc_00AD8160;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4)) goto loc_00AD8160;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00AD7F01;
loc_00AD7F27:
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1)) goto loc_00AD8160;
    Arg2 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8)))) != 0) { Arg2 = *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4; }
    if (*(uint64_t *)(v_rip + 0x500469) == 0) goto loc_00AD7F5B;
    result = guard_dispatch_icall(result, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))))), v_stack_m40);
    goto loc_00AD7F61;
loc_00AD7F5B:
loc_00AD7F61:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10))) + (64));
    if (((uint32_t)(result)) < 64) goto loc_00AD8160;
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_00AD8160;
    local_rbx = (uint32_t)(((uint32_t)(0xC000000DULL)) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (sign_flag) goto loc_00AD8165;
    *(uint32_t *)(Arg4 + 0x4) = 40;
    result = ExAllocatePool2(256, 40, (uint32_t)(0x20534C53ULL), v_stack_m40);
    if (result != 0) goto loc_00AD7FBA;
    goto loc_00AD8165;
loc_00AD7FBA:
    *(uint64_t *)(Arg4 + 0x8) = result;
    *(uint32_t *)(Arg4) = 0;
    if (result != 0) goto loc_00AD7FEB;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD7FDF;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_00AD8036;
loc_00AD7FDF:
loc_00AD7FE4:
    goto loc_00AD8165;
loc_00AD7FEB:
loc_00AD7FEE:
    if (0 >= 0) goto loc_00AD800F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD7FE4;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (result);
    if (Arg3 < result) goto loc_00AD7FE4;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00AD7FEE;
loc_00AD800F:
    if ((Arg3 + 4) < Arg3) goto loc_00AD7FE4;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_00AD80B7;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)(0xC000A281ULL));
loc_00AD8036:
    Arg3 = (uint32_t)((Arg3 + 4) | (0xFFFFFFFFULL));
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD806A;
    result = (uint32_t)((uint32_t)(Arg3));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12); }
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)))) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD80CA;
    if (!sign_flag) goto loc_00AD80CD;
    goto loc_00AD8165;
loc_00AD806A:
loc_00AD8070:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD8099;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD7FE4;
    Arg4 = ((uint32_t)((uint32_t)(result))) + ((uint32_t)(*(uint32_t *)(Arg4 + 0x4)));
    if (Arg4 < ((uint32_t)(*(uint32_t *)(Arg4 + 0x4)))) goto loc_00AD7FE4;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00AD8070;
loc_00AD8099:
    if ((Arg4 + 4) < Arg4) goto loc_00AD7FE4;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg4 + 12) <= Arg1) goto loc_00AD80C1;
loc_00AD80B7:
    goto loc_00AD8165;
loc_00AD80C1:
    *(uint32_t *)(Arg4) = 8;
    *(uint64_t *)(Arg4 + 0x4) = *(uint64_t *)(local_rbp);
loc_00AD80CA:
loc_00AD80CD:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD80F7;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 20)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) { Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 20); }
    local_rbx = (uint32_t)(((uint32_t)(0xC0000023ULL)) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(Arg3);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 20)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD8165;
    goto loc_00AD8165;
loc_00AD80F7:
loc_00AD80FD:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD8126;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD7FE4;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00AD7FE4;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00AD80FD;
loc_00AD8126:
    if ((Arg3 + 4) < Arg3) goto loc_00AD7FE4;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 20) > Arg1) goto loc_00AD80B7;
    *(uint32_t *)(Arg3) = 16;
    *(uint64_t *)(Arg3 + 0x4) = v_xmm0;
    goto loc_00AD8165;
loc_00AD8160:
loc_00AD8165:
    if (result == 0) goto loc_00AD817B;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3 + 4, (uint32_t)(*(uint32_t *)(Arg4)));
    goto loc_00AD817B;
loc_00AD8176:
loc_00AD817B:
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3 + 4, (uint32_t)(*(uint32_t *)(Arg4)));
    return result;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AD7D60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
