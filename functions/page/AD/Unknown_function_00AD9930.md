# sub_00AD9930

- RVA: `0x00AD9930`–`0x00AD9D64` (길이 `1,076` bytes)
- VA: `0x0000000140AD9930`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008C2BC`
- 디코드: `308`개 명령, `1,076/1,076` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00AD9A42` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (function, `0x00458B60`)
- `0x00AD9A82` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD9AA2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AD9B23` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (function, `0x00458B60`)
- `0x00AD9B63` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD9B83` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AD9BA5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AD9BC2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AD9BEE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AD9C34` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AD9C47` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x0096A886`

### Static image references
- `0x00AD9B88` → RVA `0x00FD8450` (`PAGEDATA`; read)
- `0x00AD9BB3` → RVA `0x00FD83F0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x00AD9A42` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (`PAGE` → `.text`)
  - `0x00AD9A82` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD9AA2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AD9B23` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (`PAGE` → `.text`)
  - `0x00AD9B63` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD9B83` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AD9BA5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AD9BC2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AD9BEE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AD9C34` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AD9C47` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AD9930  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00AD9935  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00AD993A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00AD993F  57                              push rdi
00AD9940  41 54                           push r12
00AD9942  41 55                           push r13
00AD9944  41 56                           push r14
00AD9946  41 57                           push r15
00AD9948  48 83 EC 30                     sub rsp, 0x30
00AD994C  33 FF                           xor edi, edi
00AD994E  4D 8B F1                        mov r14, r9
00AD9951  48 8B D9                        mov rbx, rcx
00AD9954  8B F7                           mov esi, edi
00AD9956  48 85 C9                        test rcx, rcx
00AD9959  75 0A                           jne 0x140ad9965
00AD995B  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD9960  E9 DF 03 00 00                  jmp 0x140ad9d44
00AD9965  48 85 D2                        test rdx, rdx
00AD9968  74 F1                           je 0x140ad995b
00AD996A  4D 85 F6                        test r14, r14
00AD996D  74 EC                           je 0x140ad995b
00AD996F  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00AD9973  48 85 C9                        test rcx, rcx
00AD9976  74 E3                           je 0x140ad995b
00AD9978  83 3B 03                        cmp dword ptr [rbx], 3
00AD997B  76 DE                           jbe 0x140ad995b
00AD997D  48 8B C1                        mov rax, rcx
00AD9980  44 8B C7                        mov r8d, edi
00AD9983  44 8B 08                        mov r9d, dword ptr [rax]
00AD9986  48 8D 50 04                     lea rdx, [rax + 4]
00AD998A  41 83 F8 03                     cmp r8d, 3
00AD998E  73 1B                           jae 0x140ad99ab
00AD9990  48 3B D0                        cmp rdx, rax
00AD9993  0F 82 A6 03 00 00               jb 0x140ad9d3f
00AD9999  4A 8D 04 0A                     lea rax, [rdx + r9]
00AD999D  48 3B C2                        cmp rax, rdx
00AD99A0  0F 82 99 03 00 00               jb 0x140ad9d3f
00AD99A6  41 FF C0                        inc r8d
00AD99A9  EB D8                           jmp 0x140ad9983
00AD99AB  48 3B D0                        cmp rdx, rax
00AD99AE  0F 82 8B 03 00 00               jb 0x140ad9d3f
00AD99B4  45 85 C9                        test r9d, r9d
00AD99B7  48 8B EF                        mov rbp, rdi
00AD99BA  48 0F 45 EA                     cmovne rbp, rdx
00AD99BE  41 83 F9 08                     cmp r9d, 8
00AD99C2  74 0A                           je 0x140ad99ce
00AD99C4  BB 23 00 00 C0                  mov ebx, 0xc0000023
00AD99C9  E9 76 03 00 00                  jmp 0x140ad9d44
00AD99CE  83 3B 04                        cmp dword ptr [rbx], 4
00AD99D1  48 8B 6D 00                     mov rbp, qword ptr [rbp]
00AD99D5  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00AD99DA  0F 86 7B FF FF FF               jbe 0x140ad995b
00AD99E0  44 8B CF                        mov r9d, edi
00AD99E3  44 8B 01                        mov r8d, dword ptr [rcx]
00AD99E6  48 8D 51 04                     lea rdx, [rcx + 4]
00AD99EA  41 83 F9 04                     cmp r9d, 4
00AD99EE  73 1B                           jae 0x140ad9a0b
00AD99F0  48 3B D1                        cmp rdx, rcx
00AD99F3  0F 82 46 03 00 00               jb 0x140ad9d3f
00AD99F9  4A 8D 0C 02                     lea rcx, [rdx + r8]
00AD99FD  48 3B CA                        cmp rcx, rdx
00AD9A00  0F 82 39 03 00 00               jb 0x140ad9d3f
00AD9A06  41 FF C1                        inc r9d
00AD9A09  EB D8                           jmp 0x140ad99e3
00AD9A0B  48 3B D1                        cmp rdx, rcx
00AD9A0E  0F 82 2B 03 00 00               jb 0x140ad9d3f
00AD9A14  45 85 C0                        test r8d, r8d
00AD9A17  4C 8B E7                        mov r12, rdi
00AD9A1A  4C 0F 45 E2                     cmovne r12, rdx
00AD9A1E  74 39                           je 0x140ad9a59
00AD9A20  41 F6 C0 01                     test r8b, 1
00AD9A24  75 33                           jne 0x140ad9a59
00AD9A26  49 8B C0                        mov rax, r8
00AD9A29  4D 8B D8                        mov r11, r8
00AD9A2C  48 D1 E8                        shr rax, 1
00AD9A2F  66 41 3B 7C 44 FE               cmp di, word ptr [r12 + rax*2 - 2]
00AD9A35  75 22                           jne 0x140ad9a59
00AD9A37  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00AD9A3C  49 8B D3                        mov rdx, r11
00AD9A3F  49 8B CC                        mov rcx, r12
00AD9A42  E8 19 F1 97 FF                  call 0x140458b60
00AD9A47  85 C0                           test eax, eax
00AD9A49  78 0E                           js 0x140ad9a59
00AD9A4B  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00AD9A50  49 8D 47 02                     lea rax, [r15 + 2]
00AD9A54  49 3B C3                        cmp rax, r11
00AD9A57  74 0A                           je 0x140ad9a63
00AD9A59  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00AD9A5E  E9 E1 02 00 00                  jmp 0x140ad9d44
00AD9A63  49 D1 EF                        shr r15, 1
00AD9A66  42 8D 04 7D 02 00 00 00         lea eax, [r15*2 + 2]
00AD9A6E  85 C0                           test eax, eax
00AD9A70  74 E7                           je 0x140ad9a59
00AD9A72  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD9A78  8B D0                           mov edx, eax
00AD9A7A  B9 00 01 00 00                  mov ecx, 0x100
00AD9A7F  44 8B E8                        mov r13d, eax
00AD9A82  E8 69 86 0A 00                  call 0x140b820f0
00AD9A87  48 8B F8                        mov rdi, rax
00AD9A8A  48 85 C0                        test rax, rax
00AD9A8D  75 0A                           jne 0x140ad9a99
00AD9A8F  BB 17 00 00 C0                  mov ebx, 0xc0000017
00AD9A94  E9 AB 02 00 00                  jmp 0x140ad9d44
00AD9A99  4D 8B C5                        mov r8, r13
00AD9A9C  49 8B D4                        mov rdx, r12
00AD9A9F  48 8B C8                        mov rcx, rax
00AD9AA2  E8 99 CD BE FF                  call 0x1406c6840
00AD9AA7  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00AD9AAB  45 33 E4                        xor r12d, r12d
00AD9AAE  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
00AD9AB3  48 85 C0                        test rax, rax
00AD9AB6  75 0A                           jne 0x140ad9ac2
00AD9AB8  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD9ABD  E9 68 01 00 00                  jmp 0x140ad9c2a
00AD9AC2  83 3B 05                        cmp dword ptr [rbx], 5
00AD9AC5  76 F1                           jbe 0x140ad9ab8
00AD9AC7  45 8B C4                        mov r8d, r12d
00AD9ACA  8B 10                           mov edx, dword ptr [rax]
00AD9ACC  48 8D 48 04                     lea rcx, [rax + 4]
00AD9AD0  41 83 F8 05                     cmp r8d, 5
00AD9AD4  73 1B                           jae 0x140ad9af1
00AD9AD6  48 3B C8                        cmp rcx, rax
00AD9AD9  0F 82 46 01 00 00               jb 0x140ad9c25
00AD9ADF  48 8D 04 11                     lea rax, [rcx + rdx]
00AD9AE3  48 3B C1                        cmp rax, rcx
00AD9AE6  0F 82 39 01 00 00               jb 0x140ad9c25
00AD9AEC  41 FF C0                        inc r8d
00AD9AEF  EB D9                           jmp 0x140ad9aca
00AD9AF1  48 3B C8                        cmp rcx, rax
00AD9AF4  0F 82 2B 01 00 00               jb 0x140ad9c25
00AD9AFA  85 D2                           test edx, edx
00AD9AFC  49 8B DC                        mov rbx, r12
00AD9AFF  48 0F 45 D9                     cmovne rbx, rcx
00AD9B03  74 35                           je 0x140ad9b3a
00AD9B05  F6 C2 01                        test dl, 1
00AD9B08  75 30                           jne 0x140ad9b3a
00AD9B0A  48 8B C2                        mov rax, rdx
00AD9B0D  4C 8B DA                        mov r11, rdx
00AD9B10  48 D1 E8                        shr rax, 1
00AD9B13  66 44 3B 64 43 FE               cmp r12w, word ptr [rbx + rax*2 - 2]
00AD9B19  75 1F                           jne 0x140ad9b3a
00AD9B1B  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00AD9B20  48 8B CB                        mov rcx, rbx
00AD9B23  E8 38 F0 97 FF                  call 0x140458b60
00AD9B28  85 C0                           test eax, eax
00AD9B2A  78 0E                           js 0x140ad9b3a
00AD9B2C  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00AD9B31  49 8D 45 02                     lea rax, [r13 + 2]
00AD9B35  49 3B C3                        cmp rax, r11
00AD9B38  74 0A                           je 0x140ad9b44
00AD9B3A  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00AD9B3F  E9 E6 00 00 00                  jmp 0x140ad9c2a
00AD9B44  49 D1 ED                        shr r13, 1
00AD9B47  42 8D 04 6D 02 00 00 00         lea eax, [r13*2 + 2]
00AD9B4F  85 C0                           test eax, eax
00AD9B51  74 E7                           je 0x140ad9b3a
00AD9B53  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD9B59  8B D0                           mov edx, eax
00AD9B5B  B9 00 01 00 00                  mov ecx, 0x100
00AD9B60  44 8B E0                        mov r12d, eax
00AD9B63  E8 88 85 0A 00                  call 0x140b820f0
00AD9B68  48 85 C0                        test rax, rax
00AD9B6B  75 0A                           jne 0x140ad9b77
00AD9B6D  BB 17 00 00 C0                  mov ebx, 0xc0000017
00AD9B72  E9 B3 00 00 00                  jmp 0x140ad9c2a
00AD9B77  4D 8B C4                        mov r8, r12
00AD9B7A  48 8B D3                        mov rdx, rbx
00AD9B7D  48 8B C8                        mov rcx, rax
00AD9B80  48 8B F0                        mov rsi, rax
00AD9B83  E8 B8 CC BE FF                  call 0x1406c6840
00AD9B88  48 8B 05 C1 E8 4F 00            mov rax, qword ptr [rip + 0x4fe8c1]
00AD9B8F  46 8D 04 6D 02 00 00 00         lea r8d, [r13*2 + 2]
00AD9B97  42 8D 0C 7D 02 00 00 00         lea ecx, [r15*2 + 2]
00AD9B9F  4C 8B CE                        mov r9, rsi
00AD9BA2  48 8B D7                        mov rdx, rdi
00AD9BA5  E8 26 0F BE FF                  call 0x1406baad0
00AD9BAA  45 33 E4                        xor r12d, r12d
00AD9BAD  8B D8                           mov ebx, eax
00AD9BAF  85 C0                           test eax, eax
00AD9BB1  78 27                           js 0x140ad9bda
00AD9BB3  48 8B 05 36 E8 4F 00            mov rax, qword ptr [rip + 0x4fe836]
00AD9BBA  48 85 C0                        test rax, rax
00AD9BBD  74 16                           je 0x140ad9bd5
00AD9BBF  48 8B CF                        mov rcx, rdi
00AD9BC2  E8 09 0F BE FF                  call 0x1406baad0
00AD9BC7  8B D8                           mov ebx, eax
00AD9BC9  3D 72 02 00 C0                  cmp eax, 0xc0000272
00AD9BCE  75 0A                           jne 0x140ad9bda
00AD9BD0  41 8B DC                        mov ebx, r12d
00AD9BD3  EB 05                           jmp 0x140ad9bda
00AD9BD5  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00AD9BDA  BA 14 00 00 00                  mov edx, 0x14
00AD9BDF  B9 00 01 00 00                  mov ecx, 0x100
00AD9BE4  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00AD9BEA  41 89 56 04                     mov dword ptr [r14 + 4], edx
00AD9BEE  E8 FD 84 0A 00                  call 0x140b820f0
00AD9BF3  48 85 C0                        test rax, rax
00AD9BF6  0F 84 71 FF FF FF               je 0x140ad9b6d
00AD9BFC  49 89 46 08                     mov qword ptr [r14 + 8], rax
00AD9C00  0F BA EB 1C                     bts ebx, 0x1c
00AD9C04  45 89 26                        mov dword ptr [r14], r12d
00AD9C07  48 8B D0                        mov rdx, rax
00AD9C0A  48 85 C0                        test rax, rax
00AD9C0D  75 42                           jne 0x140ad9c51
00AD9C0F  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00AD9C13  8D 48 08                        lea ecx, [rax + 8]
00AD9C16  3B C8                           cmp ecx, eax
00AD9C18  72 06                           jb 0x140ad9c20
00AD9C1A  41 89 4E 04                     mov dword ptr [r14 + 4], ecx
00AD9C1E  EB 7F                           jmp 0x140ad9c9f
00AD9C20  41 83 4E 04 FF                  or dword ptr [r14 + 4], 0xffffffff
00AD9C25  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD9C2A  48 85 FF                        test rdi, rdi
00AD9C2D  74 0A                           je 0x140ad9c39
00AD9C2F  33 D2                           xor edx, edx
00AD9C31  48 8B CF                        mov rcx, rdi
00AD9C34  E8 37 8C 0A 00                  call 0x140b82870
00AD9C39  48 85 F6                        test rsi, rsi
00AD9C3C  0F 84 02 01 00 00               je 0x140ad9d44
00AD9C42  33 D2                           xor edx, edx
00AD9C44  48 8B CE                        mov rcx, rsi
00AD9C47  E8 24 8C 0A 00                  call 0x140b82870
00AD9C4C  E9 F3 00 00 00                  jmp 0x140ad9d44
00AD9C51  41 8B CC                        mov ecx, r12d
00AD9C54  41 3B CC                        cmp ecx, r12d
00AD9C57  73 1C                           jae 0x140ad9c75
00AD9C59  8B 02                           mov eax, dword ptr [rdx]
00AD9C5B  83 C0 04                        add eax, 4
00AD9C5E  83 F8 04                        cmp eax, 4
00AD9C61  72 C2                           jb 0x140ad9c25
00AD9C63  44 8B C0                        mov r8d, eax
00AD9C66  4C 03 C2                        add r8, rdx
00AD9C69  4C 3B C2                        cmp r8, rdx
00AD9C6C  72 B7                           jb 0x140ad9c25
00AD9C6E  49 8B D0                        mov rdx, r8
00AD9C71  FF C1                           inc ecx
00AD9C73  EB DF                           jmp 0x140ad9c54
00AD9C75  4C 8D 42 04                     lea r8, [rdx + 4]
00AD9C79  4C 3B C2                        cmp r8, rdx
00AD9C7C  72 A7                           jb 0x140ad9c25
00AD9C7E  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00AD9C82  48 8D 42 08                     lea rax, [rdx + 8]
00AD9C86  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
00AD9C8A  48 3B C1                        cmp rax, rcx
00AD9C8D  76 07                           jbe 0x140ad9c96
00AD9C8F  BB 23 00 00 C0                  mov ebx, 0xc0000023
00AD9C94  EB 94                           jmp 0x140ad9c2a
00AD9C96  C7 02 04 00 00 00               mov dword ptr [rdx], 4
00AD9C9C  41 89 18                        mov dword ptr [r8], ebx
00AD9C9F  41 FF 06                        inc dword ptr [r14]
00AD9CA2  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00AD9CA6  48 85 D2                        test rdx, rdx
00AD9CA9  75 2F                           jne 0x140ad9cda
00AD9CAB  41 8B 56 04                     mov edx, dword ptr [r14 + 4]
00AD9CAF  83 C8 FF                        or eax, 0xffffffff
00AD9CB2  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD9CB7  8D 4A 0C                        lea ecx, [rdx + 0xc]
00AD9CBA  3B CA                           cmp ecx, edx
00AD9CBC  0F 43 C1                        cmovae eax, ecx
00AD9CBF  41 89 46 04                     mov dword ptr [r14 + 4], eax
00AD9CC3  1B C0                           sbb eax, eax
00AD9CC5  23 D8                           and ebx, eax
00AD9CC7  3B CA                           cmp ecx, edx
00AD9CC9  0F 82 5B FF FF FF               jb 0x140ad9c2a
00AD9CCF  41 FF 06                        inc dword ptr [r14]
00AD9CD2  41 8B DC                        mov ebx, r12d
00AD9CD5  E9 50 FF FF FF                  jmp 0x140ad9c2a
00AD9CDA  45 8B 0E                        mov r9d, dword ptr [r14]
00AD9CDD  41 8B CC                        mov ecx, r12d
00AD9CE0  41 3B C9                        cmp ecx, r9d
00AD9CE3  73 24                           jae 0x140ad9d09
00AD9CE5  8B 02                           mov eax, dword ptr [rdx]
00AD9CE7  83 C0 04                        add eax, 4
00AD9CEA  83 F8 04                        cmp eax, 4
00AD9CED  0F 82 32 FF FF FF               jb 0x140ad9c25
00AD9CF3  44 8B C0                        mov r8d, eax
00AD9CF6  4C 03 C2                        add r8, rdx
00AD9CF9  4C 3B C2                        cmp r8, rdx
00AD9CFC  0F 82 23 FF FF FF               jb 0x140ad9c25
00AD9D02  49 8B D0                        mov rdx, r8
00AD9D05  FF C1                           inc ecx
00AD9D07  EB D7                           jmp 0x140ad9ce0
00AD9D09  4C 8D 42 04                     lea r8, [rdx + 4]
00AD9D0D  4C 3B C2                        cmp r8, rdx
00AD9D10  0F 82 0F FF FF FF               jb 0x140ad9c25
00AD9D16  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00AD9D1A  48 8D 42 0C                     lea rax, [rdx + 0xc]
00AD9D1E  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
00AD9D22  41 8B DC                        mov ebx, r12d
00AD9D25  48 3B C1                        cmp rax, rcx
00AD9D28  0F 87 61 FF FF FF               ja 0x140ad9c8f
00AD9D2E  C7 02 08 00 00 00               mov dword ptr [rdx], 8
00AD9D34  49 89 28                        mov qword ptr [r8], rbp
00AD9D37  41 FF 06                        inc dword ptr [r14]
00AD9D3A  E9 EB FE FF FF                  jmp 0x140ad9c2a
00AD9D3F  BB 95 00 00 C0                  mov ebx, 0xc0000095
00AD9D44  48 8B 6C 24 70                  mov rbp, qword ptr [rsp + 0x70]
00AD9D49  8B C3                           mov eax, ebx
00AD9D4B  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
00AD9D50  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00AD9D55  48 83 C4 30                     add rsp, 0x30
00AD9D59  41 5F                           pop r15
00AD9D5B  41 5E                           pop r14
00AD9D5D  41 5D                           pop r13
00AD9D5F  41 5C                           pop r12
00AD9D61  5F                              pop rdi
00AD9D62  C3                              ret
00AD9D63  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00AD9930(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (48);
    v_rdi = 0;
    if (a1 != 0) goto loc_00AD9965;
loc_00AD995B:
    goto loc_00AD9D44;
loc_00AD9965:
    if (a2 == 0) goto loc_00AD995B;
    if (a4 == 0) goto loc_00AD995B;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00AD995B;
    if ((*(unsigned int *)((unsigned int)(0xC000000DULL))) <= 3) goto loc_00AD995B;
loc_00AD9983:
    if (0 >= 3) goto loc_00AD99AB;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD9D3F;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD9D3F;
    a3 = (unsigned int)((0) + 1);
    goto loc_00AD9983;
loc_00AD99AB:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD9D3F;
    v_rbp = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rbp = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) == 8) goto loc_00AD99CE;
    goto loc_00AD9D44;
loc_00AD99CE:
    v_stack_p8 = 0;
    if ((*(unsigned int *)((unsigned int)(0xC0000023ULL))) <= 4) goto loc_00AD995B;
loc_00AD99E3:
    if (0 >= 4) goto loc_00AD9A0B;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00AD9D3F;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00AD9D3F;
    a4 = (unsigned int)((0) + 1);
    goto loc_00AD99E3;
loc_00AD9A0B:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00AD9D3F;
    v_r12 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r12 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) == 0) goto loc_00AD9A59;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) & (1)) != 0) goto loc_00AD9A59;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) >> (1);
    if (0 != (*(unsigned __int16 *)(v_r12 + result * 2 - 2))) goto loc_00AD9A59;
    result = StringCbLengthW(v_r12, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))), v_stack_p8, a4);
    if (sign_flag) goto loc_00AD9A59;
    if ((v_stack_p8 + 2) == ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) goto loc_00AD9A63;
loc_00AD9A59:
    goto loc_00AD9D44;
loc_00AD9A63:
    v_r15 = (v_stack_p8) >> (1);
    if ((unsigned int)(v_r15 * 2 + 2) == 0) goto loc_00AD9A59;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_r15 * 2 + 2)), (unsigned int)(0x20534C53ULL), a4);
    if (result != 0) goto loc_00AD9A99;
    goto loc_00AD9D44;
loc_00AD9A99:
    result = memcpy(result, v_r12, (unsigned int)((unsigned int)(v_r15 * 2 + 2)), a4);
    v_r12 = 0;
    v_stack_p8 = 0;
    if (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) != 0) goto loc_00AD9AC2;
loc_00AD9AB8:
    goto loc_00AD9C2A;
loc_00AD9AC2:
    if ((*(unsigned int *)((unsigned int)(0xC000000DULL))) <= 5) goto loc_00AD9AB8;
loc_00AD9ACA:
    if (0 >= 5) goto loc_00AD9AF1;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) goto loc_00AD9C25;
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4)) goto loc_00AD9C25;
    a3 = (unsigned int)((0) + 1);
    goto loc_00AD9ACA;
loc_00AD9AF1:
    if ((*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4) < (*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))) * 1)) goto loc_00AD9C25;
    v_rbx = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8)))) != 0) { v_rbx = *(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8) + 4; }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8)))) == 0) goto loc_00AD9B3A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))))) & (1)) != 0) goto loc_00AD9B3A;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8)))) >> (1);
    if (0 != (*(unsigned __int16 *)(v_rbx + result * 2 - 2))) goto loc_00AD9B3A;
    result = StringCbLengthW(v_rbx, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))), v_stack_p8, a4);
    if (sign_flag) goto loc_00AD9B3A;
    if ((v_stack_p8 + 2) == ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC0000017ULL) + 8))))) goto loc_00AD9B44;
loc_00AD9B3A:
    goto loc_00AD9C2A;
loc_00AD9B44:
    v_r13 = (v_stack_p8) >> (1);
    if ((unsigned int)(v_r13 * 2 + 2) == 0) goto loc_00AD9B3A;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_r13 * 2 + 2)), (unsigned int)(0x20534C53ULL), a4);
    if (result != 0) goto loc_00AD9B77;
loc_00AD9B6D:
    goto loc_00AD9C2A;
loc_00AD9B77:
    result = memcpy(result, (unsigned int)(0xC0000017ULL), (unsigned int)((unsigned int)(v_r13 * 2 + 2)), a4);
    result = guard_dispatch_icall(v_r15 * 2 + 2, result, v_r13 * 2 + 2, result);
    v_r12 = 0;
    if (sign_flag) goto loc_00AD9BDA;
    if (*(unsigned __int64 *)(v_rip + 5236790) == 0) goto loc_00AD9BD5;
    result = guard_dispatch_icall(result, result, v_r13 * 2 + 2, result);
    if (((unsigned int)(result)) != 0xC0000272ULL) goto loc_00AD9BDA;
    goto loc_00AD9BDA;
loc_00AD9BD5:
loc_00AD9BDA:
    *(unsigned int *)(a4 + 4) = 20;
    result = ExAllocatePool2(256, 20, (unsigned int)(0x20534C53ULL), result);
    if (result == 0) goto loc_00AD9B6D;
    *(unsigned __int64 *)(a4 + 8) = result;
    *(unsigned int *)(a4) = 0;
    if (result != 0) goto loc_00AD9C51;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD9C20;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00AD9C9F;
loc_00AD9C20:
loc_00AD9C25:
loc_00AD9C2A:
    result = (unsigned int)(*(unsigned int *)(a4 + 4));
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x20534C53ULL), result);
    }
    if (result == 0) goto loc_00AD9D44;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x20534C53ULL), result);
    goto loc_00AD9D44;
loc_00AD9C51:
loc_00AD9C54:
    if (0 >= 0) goto loc_00AD9C75;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD9C25;
    a3 = ((unsigned int)((unsigned int)(result))) + (0);
    if (a3 < 0) goto loc_00AD9C25;
    a1 = (unsigned int)((0) + 1);
    goto loc_00AD9C54;
loc_00AD9C75:
    if ((a3 + 4) < a3) goto loc_00AD9C25;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) <= a1) goto loc_00AD9C96;
loc_00AD9C8F:
    goto loc_00AD9C2A;
loc_00AD9C96:
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)(0xC0000023ULL));
loc_00AD9C9F:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00AD9CDA;
    result = (unsigned int)((a3 + 8) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12); }
    *(unsigned int *)(a4 + 4) = (unsigned int)(result);
    v_rbx = (unsigned int)(((unsigned int)(0xC0000095ULL)) & ((unsigned int)(result)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00AD9C2A;
    goto loc_00AD9C2A;
loc_00AD9CDA:
loc_00AD9CE0:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00AD9D09;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a4 + 4))))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00AD9C25;
    a3 = ((unsigned int)((unsigned int)(result))) + ((unsigned int)(*(unsigned int *)(a4 + 4)));
    if (a3 < ((unsigned int)(*(unsigned int *)(a4 + 4)))) goto loc_00AD9C25;
    a1 = (unsigned int)((0) + 1);
    goto loc_00AD9CE0;
loc_00AD9D09:
    if ((a3 + 4) < a3) goto loc_00AD9C25;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) > a1) goto loc_00AD9C8F;
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)(a3 + 4) = *(unsigned __int64 *)(v_rbp);
    goto loc_00AD9C2A;
loc_00AD9D3F:
loc_00AD9D44:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_00AD9930(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (48);
    local_rdi = 0;
    if (Arg1 != NULL) goto loc_00AD9965;
loc_00AD995B:
    goto loc_00AD9D44;
loc_00AD9965:
    if (Arg2 == 0) goto loc_00AD995B;
    if (Arg4 == 0) goto loc_00AD995B;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00AD995B;
    if ((*(uint32_t *)((uint32_t)(0xC000000DULL))) <= 3) goto loc_00AD995B;
loc_00AD9983:
    if (0 >= 3) goto loc_00AD99AB;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD9D3F;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD9D3F;
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00AD9983;
loc_00AD99AB:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD9D3F;
    local_rbp = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rbp = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) == 8) goto loc_00AD99CE;
    goto loc_00AD9D44;
loc_00AD99CE:
    v_stack_p8 = 0;
    if ((*(uint32_t *)((uint32_t)(0xC0000023ULL))) <= 4) goto loc_00AD995B;
loc_00AD99E3:
    if (0 >= 4) goto loc_00AD9A0B;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00AD9D3F;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00AD9D3F;
    Arg4 = (uint32_t)((0) + 1);
    goto loc_00AD99E3;
loc_00AD9A0B:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00AD9D3F;
    local_r12 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r12 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) == 0) goto loc_00AD9A59;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) & (1)) != 0) goto loc_00AD9A59;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) >> (1);
    if (0 != (*(uint16_t *)(local_r12 + result * 2 - 0x2))) goto loc_00AD9A59;
    result = StringCbLengthW(local_r12, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))), v_stack_p8, Arg4);
    if (sign_flag) goto loc_00AD9A59;
    if ((v_stack_p8 + 2) == ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) goto loc_00AD9A63;
loc_00AD9A59:
    goto loc_00AD9D44;
loc_00AD9A63:
    local_r15 = (v_stack_p8) >> (1);
    if ((uint32_t)(local_r15 * 2 + 2) == 0) goto loc_00AD9A59;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_r15 * 2 + 2)), (uint32_t)(0x20534C53ULL), Arg4);
    if (result != 0) goto loc_00AD9A99;
    goto loc_00AD9D44;
loc_00AD9A99:
    result = memcpy(result, local_r12, (uint32_t)((uint32_t)(local_r15 * 2 + 2)), Arg4);
    local_r12 = 0;
    v_stack_p8 = 0;
    if (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) != 0) goto loc_00AD9AC2;
loc_00AD9AB8:
    goto loc_00AD9C2A;
loc_00AD9AC2:
    if ((*(uint32_t *)((uint32_t)(0xC000000DULL))) <= 5) goto loc_00AD9AB8;
loc_00AD9ACA:
    if (0 >= 5) goto loc_00AD9AF1;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) goto loc_00AD9C25;
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4)) goto loc_00AD9C25;
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00AD9ACA;
loc_00AD9AF1:
    if ((*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4) < (*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))) * 1)) goto loc_00AD9C25;
    local_rbx = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8)))) != 0) { local_rbx = *(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8) + 4; }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8)))) == 0) goto loc_00AD9B3A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))))) & (1)) != 0) goto loc_00AD9B3A;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8)))) >> (1);
    if (0 != (*(uint16_t *)(local_rbx + result * 2 - 0x2))) goto loc_00AD9B3A;
    result = StringCbLengthW(local_rbx, (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))), v_stack_p8, Arg4);
    if (sign_flag) goto loc_00AD9B3A;
    if ((v_stack_p8 + 2) == ((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC0000017ULL) + 0x8))))) goto loc_00AD9B44;
loc_00AD9B3A:
    goto loc_00AD9C2A;
loc_00AD9B44:
    local_r13 = (v_stack_p8) >> (1);
    if ((uint32_t)(local_r13 * 2 + 2) == 0) goto loc_00AD9B3A;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_r13 * 2 + 2)), (uint32_t)(0x20534C53ULL), Arg4);
    if (result != 0) goto loc_00AD9B77;
loc_00AD9B6D:
    goto loc_00AD9C2A;
loc_00AD9B77:
    result = memcpy(result, (uint32_t)(0xC0000017ULL), (uint32_t)((uint32_t)(local_r13 * 2 + 2)), Arg4);
    result = guard_dispatch_icall(local_r15 * 2 + 2, result, local_r13 * 2 + 2, result);
    local_r12 = 0;
    if (sign_flag) goto loc_00AD9BDA;
    if (*(uint64_t *)(v_rip + 0x4FE836) == 0) goto loc_00AD9BD5;
    result = guard_dispatch_icall(result, result, local_r13 * 2 + 2, result);
    if (((uint32_t)(result)) != 0xC0000272ULL) goto loc_00AD9BDA;
    goto loc_00AD9BDA;
loc_00AD9BD5:
loc_00AD9BDA:
    *(uint32_t *)(Arg4 + 0x4) = 20;
    result = ExAllocatePool2(256, 20, (uint32_t)(0x20534C53ULL), result);
    if (result == 0) goto loc_00AD9B6D;
    *(uint64_t *)(Arg4 + 0x8) = result;
    *(uint32_t *)(Arg4) = 0;
    if (result != 0) goto loc_00AD9C51;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD9C20;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_00AD9C9F;
loc_00AD9C20:
loc_00AD9C25:
loc_00AD9C2A:
    result = (uint32_t)(*(uint32_t *)(Arg4 + 0x4));
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x20534C53ULL), result);
    }
    if (result == 0) goto loc_00AD9D44;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x20534C53ULL), result);
    goto loc_00AD9D44;
loc_00AD9C51:
loc_00AD9C54:
    if (0 >= 0) goto loc_00AD9C75;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD9C25;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (0);
    if (Arg3 < 0) goto loc_00AD9C25;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00AD9C54;
loc_00AD9C75:
    if ((Arg3 + 4) < Arg3) goto loc_00AD9C25;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 8) <= Arg1) goto loc_00AD9C96;
loc_00AD9C8F:
    goto loc_00AD9C2A;
loc_00AD9C96:
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)(0xC0000023ULL));
loc_00AD9C9F:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00AD9CDA;
    result = (uint32_t)((Arg3 + 8) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12); }
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(result);
    local_rbx = (uint32_t)(((uint32_t)(0xC0000095ULL)) & ((uint32_t)(result)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00AD9C2A;
    goto loc_00AD9C2A;
loc_00AD9CDA:
loc_00AD9CE0:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00AD9D09;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00AD9C25;
    Arg3 = ((uint32_t)((uint32_t)(result))) + ((uint32_t)(*(uint32_t *)(Arg4 + 0x4)));
    if (Arg3 < ((uint32_t)(*(uint32_t *)(Arg4 + 0x4)))) goto loc_00AD9C25;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00AD9CE0;
loc_00AD9D09:
    if ((Arg3 + 4) < Arg3) goto loc_00AD9C25;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 12) > Arg1) goto loc_00AD9C8F;
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)(Arg3 + 0x4) = *(uint64_t *)(local_rbp);
    goto loc_00AD9C2A;
loc_00AD9D3F:
loc_00AD9D44:
    local_rsp = (local_rsp) + (48);
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AD9930&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
