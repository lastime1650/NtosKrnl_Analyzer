# sub_00A42ACC

- RVA: `0x00A42ACC`–`0x00A431AA` (길이 `1,758` bytes)
- VA: `0x0000000140A42ACC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AEEE0`
- 디코드: `464`개 명령, `1,758/1,758` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A42B5F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A42CDA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A42CF4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A42D37` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A42D4A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A42E00` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A42E1A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A42F04` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A42F55` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x00969CCF`

### Static image references
- `0x00A42AE8` → RVA `0x00E0A740` (`.data`; read)
- `0x00A42ED5` → RVA `0x00FD8388` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x00A42B5F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A42CDA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A42CF4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A42D37` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A42D4A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A42E00` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A42E1A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A42F04` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A42F55` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A42ACC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A42AD1  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00A42AD6  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00A42ADB  57                              push rdi
00A42ADC  41 54                           push r12
00A42ADE  41 55                           push r13
00A42AE0  41 56                           push r14
00A42AE2  41 57                           push r15
00A42AE4  48 83 EC 60                     sub rsp, 0x60
00A42AE8  48 8B 05 51 7C 3C 00            mov rax, qword ptr [rip + 0x3c7c51]
00A42AEF  48 33 C4                        xor rax, rsp
00A42AF2  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00A42AF7  33 DB                           xor ebx, ebx
00A42AF9  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00A42AFE  0F 57 C0                        xorps xmm0, xmm0
00A42B01  4D 8B F1                        mov r14, r9
00A42B04  4C 8B E9                        mov r13, rcx
00A42B07  8B F3                           mov esi, ebx
00A42B09  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
00A42B0E  48 85 D2                        test rdx, rdx
00A42B11  0F 84 36 06 00 00               je 0x140a4314d
00A42B17  4D 85 C9                        test r9, r9
00A42B1A  0F 84 2D 06 00 00               je 0x140a4314d
00A42B20  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00A42B24  48 85 C9                        test rcx, rcx
00A42B27  0F 84 20 06 00 00               je 0x140a4314d
00A42B2D  41 83 7D 00 03                  cmp dword ptr [r13], 3
00A42B32  0F 86 15 06 00 00               jbe 0x140a4314d
00A42B38  48 8B C1                        mov rax, rcx
00A42B3B  44 8B C3                        mov r8d, ebx
00A42B3E  44 8B 08                        mov r9d, dword ptr [rax]
00A42B41  48 8D 50 04                     lea rdx, [rax + 4]
00A42B45  41 83 F8 03                     cmp r8d, 3
00A42B49  73 46                           jae 0x140a42b91
00A42B4B  48 3B D0                        cmp rdx, rax
00A42B4E  73 33                           jae 0x140a42b83
00A42B50  BB 95 00 00 C0                  mov ebx, 0xc0000095
00A42B55  8B C3                           mov eax, ebx
00A42B57  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00A42B5C  48 33 CC                        xor rcx, rsp
00A42B5F  E8 DC 9A C6 FF                  call 0x1406ac640
00A42B64  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00A42B69  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00A42B6D  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
00A42B71  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00A42B75  49 8B E3                        mov rsp, r11
00A42B78  41 5F                           pop r15
00A42B7A  41 5E                           pop r14
00A42B7C  41 5D                           pop r13
00A42B7E  41 5C                           pop r12
00A42B80  5F                              pop rdi
00A42B81  C3                              ret
00A42B82  CC                              int3
00A42B83  4A 8D 04 0A                     lea rax, [rdx + r9]
00A42B87  48 3B C2                        cmp rax, rdx
00A42B8A  72 C4                           jb 0x140a42b50
00A42B8C  41 FF C0                        inc r8d
00A42B8F  EB AD                           jmp 0x140a42b3e
00A42B91  48 3B D0                        cmp rdx, rax
00A42B94  72 BA                           jb 0x140a42b50
00A42B96  45 85 C9                        test r9d, r9d
00A42B99  48 8B C3                        mov rax, rbx
00A42B9C  48 0F 45 C2                     cmovne rax, rdx
00A42BA0  41 83 F9 08                     cmp r9d, 8
00A42BA4  0F 85 DE 05 00 00               jne 0x140a43188
00A42BAA  41 83 7D 00 04                  cmp dword ptr [r13], 4
00A42BAF  48 8B 28                        mov rbp, qword ptr [rax]
00A42BB2  0F 86 95 05 00 00               jbe 0x140a4314d
00A42BB8  48 8B C1                        mov rax, rcx
00A42BBB  44 8B C3                        mov r8d, ebx
00A42BBE  44 8B 08                        mov r9d, dword ptr [rax]
00A42BC1  48 8D 50 04                     lea rdx, [rax + 4]
00A42BC5  41 83 F8 04                     cmp r8d, 4
00A42BC9  73 17                           jae 0x140a42be2
00A42BCB  48 3B D0                        cmp rdx, rax
00A42BCE  72 80                           jb 0x140a42b50
00A42BD0  4A 8D 04 0A                     lea rax, [rdx + r9]
00A42BD4  48 3B C2                        cmp rax, rdx
00A42BD7  0F 82 73 FF FF FF               jb 0x140a42b50
00A42BDD  41 FF C0                        inc r8d
00A42BE0  EB DC                           jmp 0x140a42bbe
00A42BE2  48 3B D0                        cmp rdx, rax
00A42BE5  0F 82 65 FF FF FF               jb 0x140a42b50
00A42BEB  45 85 C9                        test r9d, r9d
00A42BEE  48 8B C3                        mov rax, rbx
00A42BF1  48 0F 45 C2                     cmovne rax, rdx
00A42BF5  41 83 F9 04                     cmp r9d, 4
00A42BF9  0F 85 89 05 00 00               jne 0x140a43188
00A42BFF  41 83 7D 00 05                  cmp dword ptr [r13], 5
00A42C04  44 8B 20                        mov r12d, dword ptr [rax]
00A42C07  0F 86 40 05 00 00               jbe 0x140a4314d
00A42C0D  44 8B CB                        mov r9d, ebx
00A42C10  8B 11                           mov edx, dword ptr [rcx]
00A42C12  4C 8D 41 04                     lea r8, [rcx + 4]
00A42C16  41 83 F9 05                     cmp r9d, 5
00A42C1A  73 1B                           jae 0x140a42c37
00A42C1C  4C 3B C1                        cmp r8, rcx
00A42C1F  0F 82 2B FF FF FF               jb 0x140a42b50
00A42C25  49 8D 0C 10                     lea rcx, [r8 + rdx]
00A42C29  49 3B C8                        cmp rcx, r8
00A42C2C  0F 82 1E FF FF FF               jb 0x140a42b50
00A42C32  41 FF C1                        inc r9d
00A42C35  EB D9                           jmp 0x140a42c10
00A42C37  4C 3B C1                        cmp r8, rcx
00A42C3A  0F 82 10 FF FF FF               jb 0x140a42b50
00A42C40  85 D2                           test edx, edx
00A42C42  48 8B CB                        mov rcx, rbx
00A42C45  49 0F 45 C8                     cmovne rcx, r8
00A42C49  0F 84 1C 05 00 00               je 0x140a4316b
00A42C4F  F6 C2 01                        test dl, 1
00A42C52  0F 85 13 05 00 00               jne 0x140a4316b
00A42C58  48 8B C2                        mov rax, rdx
00A42C5B  4C 8B C2                        mov r8, rdx
00A42C5E  48 D1 E8                        shr rax, 1
00A42C61  66 3B 5C 41 FE                  cmp bx, word ptr [rcx + rax*2 - 2]
00A42C66  0F 85 FF 04 00 00               jne 0x140a4316b
00A42C6C  48 85 C9                        test rcx, rcx
00A42C6F  0F 84 F6 04 00 00               je 0x140a4316b
00A42C75  48 8B D0                        mov rdx, rax
00A42C78  4C 8B F9                        mov r15, rcx
00A42C7B  48 85 C0                        test rax, rax
00A42C7E  0F 84 0E 05 00 00               je 0x140a43192
00A42C84  66 39 19                        cmp word ptr [rcx], bx
00A42C87  74 0A                           je 0x140a42c93
00A42C89  48 83 C1 02                     add rcx, 2
00A42C8D  48 83 E8 01                     sub rax, 1
00A42C91  75 F1                           jne 0x140a42c84
00A42C93  48 85 C0                        test rax, rax
00A42C96  0F 84 F6 04 00 00               je 0x140a43192
00A42C9C  48 2B D0                        sub rdx, rax
00A42C9F  48 85 C0                        test rax, rax
00A42CA2  0F 84 C3 04 00 00               je 0x140a4316b
00A42CA8  48 8D 0C 12                     lea rcx, [rdx + rdx]
00A42CAC  48 8D 41 02                     lea rax, [rcx + 2]
00A42CB0  49 3B C0                        cmp rax, r8
00A42CB3  0F 85 B2 04 00 00               jne 0x140a4316b
00A42CB9  48 D1 E9                        shr rcx, 1
00A42CBC  8D 0C 4D 02 00 00 00            lea ecx, [rcx*2 + 2]
00A42CC3  85 C9                           test ecx, ecx
00A42CC5  0F 84 A0 04 00 00               je 0x140a4316b
00A42CCB  8B D9                           mov ebx, ecx
00A42CCD  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A42CD3  8B D1                           mov edx, ecx
00A42CD5  B9 00 01 00 00                  mov ecx, 0x100
00A42CDA  E8 11 F4 13 00                  call 0x140b820f0
00A42CDF  48 8B F8                        mov rdi, rax
00A42CE2  48 85 C0                        test rax, rax
00A42CE5  0F 84 CF 03 00 00               je 0x140a430ba
00A42CEB  44 8B C3                        mov r8d, ebx
00A42CEE  49 8B D7                        mov rdx, r15
00A42CF1  48 8B C8                        mov rcx, rax
00A42CF4  E8 47 3B C8 FF                  call 0x1406c6840
00A42CF9  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
00A42CFD  33 DB                           xor ebx, ebx
00A42CFF  48 85 C0                        test rax, rax
00A42D02  0F 84 4F 04 00 00               je 0x140a43157
00A42D08  41 83 7D 00 06                  cmp dword ptr [r13], 6
00A42D0D  0F 86 44 04 00 00               jbe 0x140a43157
00A42D13  44 8B CB                        mov r9d, ebx
00A42D16  44 8B 00                        mov r8d, dword ptr [rax]
00A42D19  48 8D 50 04                     lea rdx, [rax + 4]
00A42D1D  41 83 F9 06                     cmp r9d, 6
00A42D21  73 3F                           jae 0x140a42d62
00A42D23  48 3B D0                        cmp rdx, rax
00A42D26  73 2C                           jae 0x140a42d54
00A42D28  BB 95 00 00 C0                  mov ebx, 0xc0000095
00A42D2D  48 85 FF                        test rdi, rdi
00A42D30  74 0A                           je 0x140a42d3c
00A42D32  33 D2                           xor edx, edx
00A42D34  48 8B CF                        mov rcx, rdi
00A42D37  E8 34 FB 13 00                  call 0x140b82870
00A42D3C  48 85 F6                        test rsi, rsi
00A42D3F  0F 84 10 FE FF FF               je 0x140a42b55
00A42D45  33 D2                           xor edx, edx
00A42D47  48 8B CE                        mov rcx, rsi
00A42D4A  E8 21 FB 13 00                  call 0x140b82870
00A42D4F  E9 01 FE FF FF                  jmp 0x140a42b55
00A42D54  4A 8D 04 02                     lea rax, [rdx + r8]
00A42D58  48 3B C2                        cmp rax, rdx
00A42D5B  72 CB                           jb 0x140a42d28
00A42D5D  41 FF C1                        inc r9d
00A42D60  EB B4                           jmp 0x140a42d16
00A42D62  48 3B D0                        cmp rdx, rax
00A42D65  72 C1                           jb 0x140a42d28
00A42D67  45 85 C0                        test r8d, r8d
00A42D6A  48 8B CB                        mov rcx, rbx
00A42D6D  48 0F 45 CA                     cmovne rcx, rdx
00A42D71  0F 84 FE 03 00 00               je 0x140a43175
00A42D77  41 F6 C0 01                     test r8b, 1
00A42D7B  0F 85 F4 03 00 00               jne 0x140a43175
00A42D81  49 8B C0                        mov rax, r8
00A42D84  48 D1 E8                        shr rax, 1
00A42D87  66 3B 5C 41 FE                  cmp bx, word ptr [rcx + rax*2 - 2]
00A42D8C  0F 85 E3 03 00 00               jne 0x140a43175
00A42D92  48 85 C9                        test rcx, rcx
00A42D95  0F 84 DA 03 00 00               je 0x140a43175
00A42D9B  48 8B D0                        mov rdx, rax
00A42D9E  4C 8B F9                        mov r15, rcx
00A42DA1  48 85 C0                        test rax, rax
00A42DA4  0F 84 F0 03 00 00               je 0x140a4319a
00A42DAA  66 39 19                        cmp word ptr [rcx], bx
00A42DAD  74 0A                           je 0x140a42db9
00A42DAF  48 83 C1 02                     add rcx, 2
00A42DB3  48 83 E8 01                     sub rax, 1
00A42DB7  75 F1                           jne 0x140a42daa
00A42DB9  48 85 C0                        test rax, rax
00A42DBC  0F 84 D8 03 00 00               je 0x140a4319a
00A42DC2  48 2B D0                        sub rdx, rax
00A42DC5  48 85 C0                        test rax, rax
00A42DC8  0F 84 A7 03 00 00               je 0x140a43175
00A42DCE  48 8D 0C 12                     lea rcx, [rdx + rdx]
00A42DD2  48 8D 41 02                     lea rax, [rcx + 2]
00A42DD6  49 3B C0                        cmp rax, r8
00A42DD9  0F 85 96 03 00 00               jne 0x140a43175
00A42DDF  48 D1 E9                        shr rcx, 1
00A42DE2  8D 0C 4D 02 00 00 00            lea ecx, [rcx*2 + 2]
00A42DE9  85 C9                           test ecx, ecx
00A42DEB  0F 84 84 03 00 00               je 0x140a43175
00A42DF1  8B D9                           mov ebx, ecx
00A42DF3  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A42DF9  8B D1                           mov edx, ecx
00A42DFB  B9 00 01 00 00                  mov ecx, 0x100
00A42E00  E8 EB F2 13 00                  call 0x140b820f0
00A42E05  48 85 C0                        test rax, rax
00A42E08  0F 84 B6 02 00 00               je 0x140a430c4
00A42E0E  44 8B C3                        mov r8d, ebx
00A42E11  49 8B D7                        mov rdx, r15
00A42E14  48 8B C8                        mov rcx, rax
00A42E17  48 8B F0                        mov rsi, rax
00A42E1A  E8 21 3A C8 FF                  call 0x1406c6840
00A42E1F  49 8B 55 08                     mov rdx, qword ptr [r13 + 8]
00A42E23  33 DB                           xor ebx, ebx
00A42E25  48 85 D2                        test rdx, rdx
00A42E28  0F 84 29 03 00 00               je 0x140a43157
00A42E2E  41 83 7D 00 07                  cmp dword ptr [r13], 7
00A42E33  0F 86 1E 03 00 00               jbe 0x140a43157
00A42E39  48 8B C2                        mov rax, rdx
00A42E3C  44 8B D3                        mov r10d, ebx
00A42E3F  44 8B 38                        mov r15d, dword ptr [rax]
00A42E42  48 8D 48 04                     lea rcx, [rax + 4]
00A42E46  41 83 FA 07                     cmp r10d, 7
00A42E4A  73 1B                           jae 0x140a42e67
00A42E4C  48 3B C8                        cmp rcx, rax
00A42E4F  0F 82 D3 FE FF FF               jb 0x140a42d28
00A42E55  4A 8D 04 39                     lea rax, [rcx + r15]
00A42E59  48 3B C1                        cmp rax, rcx
00A42E5C  0F 82 C6 FE FF FF               jb 0x140a42d28
00A42E62  41 FF C2                        inc r10d
00A42E65  EB D8                           jmp 0x140a42e3f
00A42E67  48 3B C8                        cmp rcx, rax
00A42E6A  0F 82 B8 FE FF FF               jb 0x140a42d28
00A42E70  45 85 FF                        test r15d, r15d
00A42E73  4C 8B DB                        mov r11, rbx
00A42E76  4C 0F 45 D9                     cmovne r11, rcx
00A42E7A  41 83 7D 00 08                  cmp dword ptr [r13], 8
00A42E7F  0F 86 D2 02 00 00               jbe 0x140a43157
00A42E85  44 8B D3                        mov r10d, ebx
00A42E88  41 BD 01 00 00 00               mov r13d, 1
00A42E8E  8B 1A                           mov ebx, dword ptr [rdx]
00A42E90  48 8D 4A 04                     lea rcx, [rdx + 4]
00A42E94  41 83 FA 08                     cmp r10d, 8
00A42E98  73 1B                           jae 0x140a42eb5
00A42E9A  48 3B CA                        cmp rcx, rdx
00A42E9D  0F 82 85 FE FF FF               jb 0x140a42d28
00A42EA3  48 8D 14 19                     lea rdx, [rcx + rbx]
00A42EA7  48 3B D1                        cmp rdx, rcx
00A42EAA  0F 82 78 FE FF FF               jb 0x140a42d28
00A42EB0  45 03 D5                        add r10d, r13d
00A42EB3  EB D9                           jmp 0x140a42e8e
00A42EB5  48 3B CA                        cmp rcx, rdx
00A42EB8  0F 82 6A FE FF FF               jb 0x140a42d28
00A42EBE  45 33 C0                        xor r8d, r8d
00A42EC1  85 DB                           test ebx, ebx
00A42EC3  41 8B C0                        mov eax, r8d
00A42EC6  48 0F 45 C1                     cmovne rax, rcx
00A42ECA  83 FB 04                        cmp ebx, 4
00A42ECD  0F 85 8E 02 00 00               jne 0x140a43161
00A42ED3  8B 10                           mov edx, dword ptr [rax]
00A42ED5  48 8B 05 AC 54 59 00            mov rax, qword ptr [rip + 0x5954ac]
00A42EDC  48 85 C0                        test rax, rax
00A42EDF  0F 84 E9 01 00 00               je 0x140a430ce
00A42EE5  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00A42EEA  4D 8B CB                        mov r9, r11
00A42EED  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00A42EF2  4C 8B C6                        mov r8, rsi
00A42EF5  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00A42EF9  41 8B CC                        mov ecx, r12d
00A42EFC  48 8B D7                        mov rdx, rdi
00A42EFF  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
00A42F04  E8 C7 7B C7 FF                  call 0x1406baad0
00A42F09  44 8B F8                        mov r15d, eax
00A42F0C  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00A42F11  8B 50 20                        mov edx, dword ptr [rax + 0x20]
00A42F14  8B 40 10                        mov eax, dword ptr [rax + 0x10]
00A42F17  83 C0 40                        add eax, 0x40
00A42F1A  83 F8 40                        cmp eax, 0x40
00A42F1D  0F 82 05 FE FF FF               jb 0x140a42d28
00A42F23  8D 48 04                        lea ecx, [rax + 4]
00A42F26  3B C8                           cmp ecx, eax
00A42F28  0F 82 FA FD FF FF               jb 0x140a42d28
00A42F2E  8D 04 11                        lea eax, [rcx + rdx]
00A42F31  3B C1                           cmp eax, ecx
00A42F33  1B DB                           sbb ebx, ebx
00A42F35  81 E3 95 00 00 C0               and ebx, 0xc0000095
00A42F3B  0F 88 EC FD FF FF               js 0x140a42d2d
00A42F41  BA 28 00 00 00                  mov edx, 0x28
00A42F46  B9 00 01 00 00                  mov ecx, 0x100
00A42F4B  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A42F51  41 89 56 04                     mov dword ptr [r14 + 4], edx
00A42F55  E8 96 F1 13 00                  call 0x140b820f0
00A42F5A  33 DB                           xor ebx, ebx
00A42F5C  48 85 C0                        test rax, rax
00A42F5F  0F 84 5F 01 00 00               je 0x140a430c4
00A42F65  49 89 46 08                     mov qword ptr [r14 + 8], rax
00A42F69  41 0F BA EF 1C                  bts r15d, 0x1c
00A42F6E  41 89 1E                        mov dword ptr [r14], ebx
00A42F71  48 8B D0                        mov rdx, rax
00A42F74  48 85 C0                        test rax, rax
00A42F77  0F 84 8E 01 00 00               je 0x140a4310b
00A42F7D  8B CB                           mov ecx, ebx
00A42F7F  3B CB                           cmp ecx, ebx
00A42F81  73 25                           jae 0x140a42fa8
00A42F83  8B 02                           mov eax, dword ptr [rdx]
00A42F85  83 C0 04                        add eax, 4
00A42F88  83 F8 04                        cmp eax, 4
00A42F8B  0F 82 97 FD FF FF               jb 0x140a42d28
00A42F91  44 8B C0                        mov r8d, eax
00A42F94  4C 03 C2                        add r8, rdx
00A42F97  4C 3B C2                        cmp r8, rdx
00A42F9A  0F 82 88 FD FF FF               jb 0x140a42d28
00A42FA0  49 8B D0                        mov rdx, r8
00A42FA3  41 03 CD                        add ecx, r13d
00A42FA6  EB D7                           jmp 0x140a42f7f
00A42FA8  4C 8D 42 04                     lea r8, [rdx + 4]
00A42FAC  4C 3B C2                        cmp r8, rdx
00A42FAF  0F 82 73 FD FF FF               jb 0x140a42d28
00A42FB5  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00A42FB9  48 8D 42 08                     lea rax, [rdx + 8]
00A42FBD  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
00A42FC1  48 3B C1                        cmp rax, rcx
00A42FC4  0F 87 97 01 00 00               ja 0x140a43161
00A42FCA  C7 02 04 00 00 00               mov dword ptr [rdx], 4
00A42FD0  45 89 38                        mov dword ptr [r8], r15d
00A42FD3  45 01 2E                        add dword ptr [r14], r13d
00A42FD6  41 83 C8 FF                     or r8d, 0xffffffff
00A42FDA  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00A42FDE  48 85 D2                        test rdx, rdx
00A42FE1  0F 84 F2 00 00 00               je 0x140a430d9
00A42FE7  45 8B 16                        mov r10d, dword ptr [r14]
00A42FEA  8B CB                           mov ecx, ebx
00A42FEC  41 3B CA                        cmp ecx, r10d
00A42FEF  73 25                           jae 0x140a43016
00A42FF1  8B 02                           mov eax, dword ptr [rdx]
00A42FF3  83 C0 04                        add eax, 4
00A42FF6  83 F8 04                        cmp eax, 4
00A42FF9  0F 82 29 FD FF FF               jb 0x140a42d28
00A42FFF  44 8B C8                        mov r9d, eax
00A43002  4C 03 CA                        add r9, rdx
00A43005  4C 3B CA                        cmp r9, rdx
00A43008  0F 82 1A FD FF FF               jb 0x140a42d28
00A4300E  49 8B D1                        mov rdx, r9
00A43011  41 03 CD                        add ecx, r13d
00A43014  EB D6                           jmp 0x140a42fec
00A43016  4C 8D 4A 04                     lea r9, [rdx + 4]
00A4301A  4C 3B CA                        cmp r9, rdx
00A4301D  0F 82 05 FD FF FF               jb 0x140a42d28
00A43023  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00A43027  48 8D 42 0C                     lea rax, [rdx + 0xc]
00A4302B  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
00A4302F  48 3B C1                        cmp rax, rcx
00A43032  0F 87 29 01 00 00               ja 0x140a43161
00A43038  C7 02 08 00 00 00               mov dword ptr [rdx], 8
00A4303E  49 89 29                        mov qword ptr [r9], rbp
00A43041  45 01 2E                        add dword ptr [r14], r13d
00A43044  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00A43048  48 85 D2                        test rdx, rdx
00A4304B  0F 84 CF 00 00 00               je 0x140a43120
00A43051  45 8B 0E                        mov r9d, dword ptr [r14]
00A43054  8B CB                           mov ecx, ebx
00A43056  41 3B C9                        cmp ecx, r9d
00A43059  73 25                           jae 0x140a43080
00A4305B  8B 02                           mov eax, dword ptr [rdx]
00A4305D  83 C0 04                        add eax, 4
00A43060  83 F8 04                        cmp eax, 4
00A43063  0F 82 BF FC FF FF               jb 0x140a42d28
00A43069  44 8B C0                        mov r8d, eax
00A4306C  4C 03 C2                        add r8, rdx
00A4306F  4C 3B C2                        cmp r8, rdx
00A43072  0F 82 B0 FC FF FF               jb 0x140a42d28
00A43078  49 8B D0                        mov rdx, r8
00A4307B  41 03 CD                        add ecx, r13d
00A4307E  EB D6                           jmp 0x140a43056
00A43080  4C 8D 42 04                     lea r8, [rdx + 4]
00A43084  4C 3B C2                        cmp r8, rdx
00A43087  0F 82 9B FC FF FF               jb 0x140a42d28
00A4308D  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00A43091  48 8D 42 14                     lea rax, [rdx + 0x14]
00A43095  49 03 4E 08                     add rcx, qword ptr [r14 + 8]
00A43099  48 3B C1                        cmp rax, rcx
00A4309C  0F 87 BF 00 00 00               ja 0x140a43161
00A430A2  C7 02 10 00 00 00               mov dword ptr [rdx], 0x10
00A430A8  0F 10 44 24 48                  movups xmm0, xmmword ptr [rsp + 0x48]
00A430AD  F3 41 0F 7F 00                  movdqu xmmword ptr [r8], xmm0
00A430B2  45 01 2E                        add dword ptr [r14], r13d
00A430B5  E9 73 FC FF FF                  jmp 0x140a42d2d
00A430BA  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A430BF  E9 91 FA FF FF                  jmp 0x140a42b55
00A430C4  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A430C9  E9 5F FC FF FF                  jmp 0x140a42d2d
00A430CE  41 BF 81 A2 00 C0               mov r15d, 0xc000a281
00A430D4  E9 33 FE FF FF                  jmp 0x140a42f0c
00A430D9  41 8B 56 04                     mov edx, dword ptr [r14 + 4]
00A430DD  41 8B C0                        mov eax, r8d
00A430E0  8D 4A 0C                        lea ecx, [rdx + 0xc]
00A430E3  3B CA                           cmp ecx, edx
00A430E5  0F 43 C1                        cmovae eax, ecx
00A430E8  1B DB                           sbb ebx, ebx
00A430EA  81 E3 95 00 00 C0               and ebx, 0xc0000095
00A430F0  41 89 46 04                     mov dword ptr [r14 + 4], eax
00A430F4  3B CA                           cmp ecx, edx
00A430F6  0F 83 A6 00 00 00               jae 0x140a431a2
00A430FC  85 DB                           test ebx, ebx
00A430FE  0F 88 29 FC FF FF               js 0x140a42d2d
00A43104  33 DB                           xor ebx, ebx
00A43106  E9 39 FF FF FF                  jmp 0x140a43044
00A4310B  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00A4310F  8D 48 08                        lea ecx, [rax + 8]
00A43112  3B C8                           cmp ecx, eax
00A43114  73 69                           jae 0x140a4317f
00A43116  41 83 4E 04 FF                  or dword ptr [r14 + 4], 0xffffffff
00A4311B  E9 08 FC FF FF                  jmp 0x140a42d28
00A43120  41 8B 4E 04                     mov ecx, dword ptr [r14 + 4]
00A43124  8D 41 14                        lea eax, [rcx + 0x14]
00A43127  3B C1                           cmp eax, ecx
00A43129  44 0F 43 C0                     cmovae r8d, eax
00A4312D  1B DB                           sbb ebx, ebx
00A4312F  81 E3 95 00 00 C0               and ebx, 0xc0000095
00A43135  45 89 46 04                     mov dword ptr [r14 + 4], r8d
00A43139  3B C1                           cmp eax, ecx
00A4313B  0F 82 EC FB FF FF               jb 0x140a42d2d
00A43141  45 01 2E                        add dword ptr [r14], r13d
00A43144  33 C9                           xor ecx, ecx
00A43146  8B D9                           mov ebx, ecx
00A43148  E9 E0 FB FF FF                  jmp 0x140a42d2d
00A4314D  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A43152  E9 FE F9 FF FF                  jmp 0x140a42b55
00A43157  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A4315C  E9 CC FB FF FF                  jmp 0x140a42d2d
00A43161  BB 23 00 00 C0                  mov ebx, 0xc0000023
00A43166  E9 C2 FB FF FF                  jmp 0x140a42d2d
00A4316B  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00A43170  E9 E0 F9 FF FF                  jmp 0x140a42b55
00A43175  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00A4317A  E9 AE FB FF FF                  jmp 0x140a42d2d
00A4317F  41 89 4E 04                     mov dword ptr [r14 + 4], ecx
00A43183  E9 4B FE FF FF                  jmp 0x140a42fd3
00A43188  BB 23 00 00 C0                  mov ebx, 0xc0000023
00A4318D  E9 C3 F9 FF FF                  jmp 0x140a42b55
00A43192  48 8B D3                        mov rdx, rbx
00A43195  E9 05 FB FF FF                  jmp 0x140a42c9f
00A4319A  48 8B D3                        mov rdx, rbx
00A4319D  E9 23 FC FF FF                  jmp 0x140a42dc5
00A431A2  45 01 2E                        add dword ptr [r14], r13d
00A431A5  E9 5A FF FF FF                  jmp 0x140a43104
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00A42ACC(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 3963985)) ^ (v_rsp);
    v_stack_m30 = result;
    v_rbx = 0;
    v_stack_m48 = a2;
    v_stack_m40 = v_xmm0;
    if (a2 == 0) goto loc_00A4314D;
    if (a4 == 0) goto loc_00A4314D;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00A4314D;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_00A4314D;
loc_00A42B3E:
    if (0 >= 3) goto loc_00A42B91;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) >= (*(unsigned __int64 *)(a1 + 8))) goto loc_00A42B83;
loc_00A42B50:
loc_00A42B55:
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(a1 + 8) + 4, 0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    return result;
loc_00A42B83:
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A42B50;
    a3 = (unsigned int)((0) + 1);
    goto loc_00A42B3E;
loc_00A42B91:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A42B50;
    result = *(unsigned __int64 *)(v_stack_m28 + 48);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { result = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_00A43188;
    if ((*(unsigned int *)(a1)) <= 4) goto loc_00A4314D;
loc_00A42BBE:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))))) >= 4) goto loc_00A42BE2;
    if ((a1 + 4) < a1) goto loc_00A42B50;
    if ((a1 + 4 + (unsigned int)(*(unsigned int *)(a1)) * 1) < (a1 + 4)) goto loc_00A42B50;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48)))) + 1);
    goto loc_00A42BBE;
loc_00A42BE2:
    if ((a1 + 4) < (a1 + 4 + (unsigned int)(*(unsigned int *)(a1)) * 1)) goto loc_00A42B50;
    result = *(unsigned __int64 *)(v_stack_m28 + 48);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1))) != 0) { result = a1 + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) != 4) goto loc_00A43188;
    if ((*(unsigned int *)(a1)) <= 5) goto loc_00A4314D;
loc_00A42C10:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))))) >= 5) goto loc_00A42C37;
    if ((a1 + 4) < a1) goto loc_00A42B50;
    if ((a1 + 4 + (unsigned int)(*(unsigned int *)(a1)) * 1) < (a1 + 4)) goto loc_00A42B50;
    a4 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48)))) + 1);
    goto loc_00A42C10;
loc_00A42C37:
    if ((a1 + 4) < (a1 + 4 + (unsigned int)(*(unsigned int *)(a1)) * 1)) goto loc_00A42B50;
    a1 = *(unsigned __int64 *)(v_stack_m28 + 48);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1))) != 0) { a1 = a1 + 4; }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1))) == 0) goto loc_00A4316B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (1)) != 0) goto loc_00A4316B;
    result = ((unsigned int)(*(unsigned int *)(a1))) >> (1);
    if (((unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 48))) != (*(unsigned __int16 *)(a1 + result * 2 - 2))) goto loc_00A4316B;
    if (a1 == 0) goto loc_00A4316B;
    if (result == 0) goto loc_00A43192;
loc_00A42C84:
    if ((*(unsigned __int16 *)(a1)) == ((unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 48)))) goto loc_00A42C93;
    a1 = (a1) + (2);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00A42C84;
loc_00A42C93:
    if (result == 0) goto loc_00A43192;
    a2 = (result) - (result);
loc_00A42C9F:
    if (result == 0) goto loc_00A4316B;
    if ((a2 + a2 * 1 + 2) != ((unsigned int)(*(unsigned int *)(a1)))) goto loc_00A4316B;
    a1 = (a2 + a2 * 1) >> (1);
    if ((unsigned int)(a1 * 2 + 2) == 0) goto loc_00A4316B;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(a1 * 2 + 2)), (unsigned int)(0x20534C53ULL), a4);
    if (result == 0) goto loc_00A430BA;
    result = memcpy(result, a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1 * 2 + 2)))), a4);
    v_rbx = 0;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00A43157;
    if ((*(unsigned int *)(a1)) <= 6) goto loc_00A43157;
loc_00A42D16:
    if (0 >= 6) goto loc_00A42D62;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) >= (*(unsigned __int64 *)(a1 + 8))) goto loc_00A42D54;
loc_00A42D28:
loc_00A42D2D:
    result = *(unsigned __int64 *)(a1 + 8);
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))), 0);
    }
    if (*(unsigned __int64 *)(v_stack_m28 + 64) == 0) goto loc_00A42B55;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m28 + 64), a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))), 0);
    goto loc_00A42B55;
loc_00A42D54:
    if ((a2 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < 0) goto loc_00A42D28;
    a4 = (unsigned int)((0) + 1);
    goto loc_00A42D16;
loc_00A42D62:
    if (0 < (a2 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A42D28;
    a1 = (unsigned int)(0xC0000095ULL);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { a1 = 0; }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) == 0) goto loc_00A43175;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) & (1)) != 0) goto loc_00A43175;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) >> (1);
    if (((unsigned __int16)((unsigned int)(0xC0000095ULL))) != (*(unsigned __int16 *)(a1 + result * 2 - 2))) goto loc_00A43175;
    if (a1 == 0) goto loc_00A43175;
    if (result == 0) goto loc_00A4319A;
loc_00A42DAA:
    if ((*(unsigned __int16 *)(a1)) == ((unsigned __int16)((unsigned int)(0xC0000095ULL)))) goto loc_00A42DB9;
    a1 = (a1) + (2);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00A42DAA;
loc_00A42DB9:
    if (result == 0) goto loc_00A4319A;
    a2 = (result) - (result);
loc_00A42DC5:
    if (result == 0) goto loc_00A43175;
    if ((a2 + a2 * 1 + 2) != ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) goto loc_00A43175;
    a1 = (a2 + a2 * 1) >> (1);
    if ((unsigned int)(a1 * 2 + 2) == 0) goto loc_00A43175;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(a1 * 2 + 2)), (unsigned int)(0x20534C53ULL), a4);
    if (result == 0) goto loc_00A430C4;
    result = memcpy(result, a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1 * 2 + 2)))), a4);
    v_rbx = 0;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00A43157;
    if ((*(unsigned int *)(a1)) <= 7) goto loc_00A43157;
loc_00A42E3F:
    if (0 >= 7) goto loc_00A42E67;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00A42D28;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A42D28;
    v_r10 = (unsigned int)((0) + 1);
    goto loc_00A42E3F;
loc_00A42E67:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A42D28;
    v_r11 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r11 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((*(unsigned int *)(a1)) <= 8) goto loc_00A43157;
loc_00A42E8E:
    if (0 >= 8) goto loc_00A42EB5;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00A42D28;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A42D28;
    v_r10 = (unsigned int)((0) + (1));
    goto loc_00A42E8E;
loc_00A42EB5:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A42D28;
    a3 = 0;
    result = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { result = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 4) goto loc_00A43161;
    if (*(unsigned __int64 *)(v_rip + 5854380) == 0) goto loc_00A430CE;
    v_stack_m30 = v_stack_m18;
    v_stack_m38 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    v_stack_m40 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    result = guard_dispatch_icall((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result)))), result, result, v_r11);
loc_00A42F0C:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m20 + 16))) + (64));
    if (((unsigned int)(result)) < 64) goto loc_00A42D28;
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_00A42D28;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) & (0xC0000095ULL));
    if (sign_flag) goto loc_00A42D2D;
    *(unsigned int *)(a4 + 4) = 40;
    result = ExAllocatePool2(256, 40, (unsigned int)(0x20534C53ULL), v_r11);
    v_rbx = 0;
    if (result == 0) goto loc_00A430C4;
    *(unsigned __int64 *)(a4 + 8) = result;
    *(unsigned int *)(a4) = 0;
    if (result == 0) goto loc_00A4310B;
loc_00A42F7F:
    if (0 >= 0) goto loc_00A42FA8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00A42D28;
    a3 = ((unsigned int)((unsigned int)(result))) + (result);
    if (a3 < result) goto loc_00A42D28;
    a1 = (unsigned int)((0) + (1));
    goto loc_00A42F7F;
loc_00A42FA8:
    if ((a3 + 4) < a3) goto loc_00A42D28;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_00A43161;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)((unsigned int)(result)));
loc_00A42FD3:
    a3 = (unsigned int)((a3 + 4) | (0xFFFFFFFFULL));
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_00A430D9;
loc_00A42FEC:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00A43016;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00A42D28;
    a4 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a4 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00A42D28;
    a1 = (unsigned int)((0) + (1));
    goto loc_00A42FEC;
loc_00A43016:
    if ((a4 + 4) < a4) goto loc_00A42D28;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a4 + 12) > a1) goto loc_00A43161;
    *(unsigned int *)(a4) = 8;
    *(unsigned __int64 *)(a4 + 4) = *(unsigned __int64 *)(result);
loc_00A43044:
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_00A43120;
loc_00A43056:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00A43080;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00A42D28;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00A42D28;
    a1 = (unsigned int)((0) + (1));
    goto loc_00A43056;
loc_00A43080:
    if ((a3 + 4) < a3) goto loc_00A42D28;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 20) > a1) goto loc_00A43161;
    *(unsigned int *)(a3) = 16;
    *(unsigned __int64 *)(a3 + 4) = v_xmm0;
    goto loc_00A42D2D;
loc_00A430BA:
    goto loc_00A42B55;
loc_00A430C4:
    goto loc_00A42D2D;
loc_00A430CE:
    goto loc_00A42F0C;
loc_00A430D9:
    result = (unsigned int)((unsigned int)(a3 + 4));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12); }
    v_rbx = (unsigned int)(((unsigned int)(0xC0000017ULL)) & (0xC0000095ULL));
    *(unsigned int *)(a4 + 4) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A431A2;
    if (sign_flag) goto loc_00A42D2D;
loc_00A43104:
    v_rbx = 0;
    goto loc_00A43044;
loc_00A4310B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A4317F;
    goto loc_00A42D28;
loc_00A43120:
    a3 = a3 + 4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 20)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { a3 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 20); }
    v_rbx = (unsigned int)((v_rbx) & (0xC0000095ULL));
    *(unsigned int *)(a4 + 4) = (unsigned int)(a3);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 20)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A42D2D;
    a1 = 0;
    goto loc_00A42D2D;
loc_00A4314D:
    goto loc_00A42B55;
loc_00A43157:
    goto loc_00A42D2D;
loc_00A43161:
    goto loc_00A42D2D;
loc_00A4316B:
    goto loc_00A42B55;
loc_00A43175:
    goto loc_00A42D2D;
loc_00A4317F:
    *(unsigned int *)(a4 + 4) = 0;
    goto loc_00A42FD3;
loc_00A43188:
    goto loc_00A42B55;
loc_00A43192:
    goto loc_00A42C9F;
loc_00A4319A:
    goto loc_00A42DC5;
loc_00A431A2:
    goto loc_00A43104;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00A42ACC(void *Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x3C7C51)) ^ (local_rsp);
    v_stack_m30 = result;
    local_rbx = 0;
    v_stack_m48 = Arg2;
    v_stack_m40 = v_xmm0;
    if (Arg2 == 0) goto loc_00A4314D;
    if (Arg4 == NULL) goto loc_00A4314D;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00A4314D;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_00A4314D;
loc_00A42B3E:
    if (0 >= 3) goto loc_00A42B91;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) >= (*(uint64_t *)(arg1 + 0x8))) goto loc_00A42B83;
loc_00A42B50:
loc_00A42B55:
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(arg1 + 0x8) + 4, 0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    return result;
loc_00A42B83:
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A42B50;
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00A42B3E;
loc_00A42B91:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A42B50;
    result = *(uint64_t *)(v_stack_m28 + 0x30);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { result = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_00A43188;
    if ((*(uint32_t *)(arg1)) <= 4) goto loc_00A4314D;
loc_00A42BBE:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))))) >= 4) goto loc_00A42BE2;
    if ((Arg1 + 4) < Arg1) goto loc_00A42B50;
    if ((Arg1 + 4 + (uint32_t)(*(uint32_t *)(arg1)) * 1) < (Arg1 + 4)) goto loc_00A42B50;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30)))) + 1);
    goto loc_00A42BBE;
loc_00A42BE2:
    if ((Arg1 + 4) < (Arg1 + 4 + (uint32_t)(*(uint32_t *)(arg1)) * 1)) goto loc_00A42B50;
    result = *(uint64_t *)(v_stack_m28 + 0x30);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))) != 0) { result = Arg1 + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) != 4) goto loc_00A43188;
    if ((*(uint32_t *)(arg1)) <= 5) goto loc_00A4314D;
loc_00A42C10:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))))) >= 5) goto loc_00A42C37;
    if ((Arg1 + 4) < Arg1) goto loc_00A42B50;
    if ((Arg1 + 4 + (uint32_t)(*(uint32_t *)(arg1)) * 1) < (Arg1 + 4)) goto loc_00A42B50;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30)))) + 1);
    goto loc_00A42C10;
loc_00A42C37:
    if ((Arg1 + 4) < (Arg1 + 4 + (uint32_t)(*(uint32_t *)(arg1)) * 1)) goto loc_00A42B50;
    Arg1 = *(uint64_t *)(v_stack_m28 + 0x30);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))) != 0) { Arg1 = Arg1 + 4; }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))) == 0) goto loc_00A4316B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (1)) != 0) goto loc_00A4316B;
    result = ((uint32_t)(*(uint32_t *)(arg1))) >> (1);
    if (((uint16_t)(*(uint64_t *)(v_stack_m28 + 0x30))) != (*(uint16_t *)(arg1 + result * 2 - 0x2))) goto loc_00A4316B;
    if (Arg1 == NULL) goto loc_00A4316B;
    if (result == 0) goto loc_00A43192;
loc_00A42C84:
    if ((*(uint16_t *)(arg1)) == ((uint16_t)(*(uint64_t *)(v_stack_m28 + 0x30)))) goto loc_00A42C93;
    Arg1 = (Arg1) + (2);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00A42C84;
loc_00A42C93:
    if (result == 0) goto loc_00A43192;
    Arg2 = (result) - (result);
loc_00A42C9F:
    if (result == 0) goto loc_00A4316B;
    if ((Arg2 + Arg2 * 1 + 2) != ((uint32_t)(*(uint32_t *)(arg1)))) goto loc_00A4316B;
    Arg1 = (Arg2 + Arg2 * 1) >> (1);
    if ((uint32_t)(Arg1 * 2 + 2) == 0) goto loc_00A4316B;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(Arg1 * 2 + 2)), (uint32_t)(0x20534C53ULL), Arg4);
    if (result == 0) goto loc_00A430BA;
    result = memcpy(result, Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1 * 2 + 2)))), Arg4);
    local_rbx = 0;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00A43157;
    if ((*(uint32_t *)(arg1)) <= 6) goto loc_00A43157;
loc_00A42D16:
    if (0 >= 6) goto loc_00A42D62;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) >= (*(uint64_t *)(arg1 + 0x8))) goto loc_00A42D54;
loc_00A42D28:
loc_00A42D2D:
    result = *(uint64_t *)(arg1 + 0x8);
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))), 0);
    }
    if (*(uint64_t *)(v_stack_m28 + 0x40) == 0) goto loc_00A42B55;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m28 + 0x40), Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))), 0);
    goto loc_00A42B55;
loc_00A42D54:
    if ((Arg2 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < 0) goto loc_00A42D28;
    Arg4 = (uint32_t)((0) + 1);
    goto loc_00A42D16;
loc_00A42D62:
    if (0 < (Arg2 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A42D28;
    Arg1 = (uint32_t)(0xC0000095ULL);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { Arg1 = 0; }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) == 0) goto loc_00A43175;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) & (1)) != 0) goto loc_00A43175;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) >> (1);
    if (((uint16_t)((uint32_t)(0xC0000095ULL))) != (*(uint16_t *)(arg1 + result * 2 - 0x2))) goto loc_00A43175;
    if (Arg1 == NULL) goto loc_00A43175;
    if (result == 0) goto loc_00A4319A;
loc_00A42DAA:
    if ((*(uint16_t *)(arg1)) == ((uint16_t)((uint32_t)(0xC0000095ULL)))) goto loc_00A42DB9;
    Arg1 = (Arg1) + (2);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00A42DAA;
loc_00A42DB9:
    if (result == 0) goto loc_00A4319A;
    Arg2 = (result) - (result);
loc_00A42DC5:
    if (result == 0) goto loc_00A43175;
    if ((Arg2 + Arg2 * 1 + 2) != ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) goto loc_00A43175;
    Arg1 = (Arg2 + Arg2 * 1) >> (1);
    if ((uint32_t)(Arg1 * 2 + 2) == 0) goto loc_00A43175;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(Arg1 * 2 + 2)), (uint32_t)(0x20534C53ULL), Arg4);
    if (result == 0) goto loc_00A430C4;
    result = memcpy(result, Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1 * 2 + 2)))), Arg4);
    local_rbx = 0;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00A43157;
    if ((*(uint32_t *)(arg1)) <= 7) goto loc_00A43157;
loc_00A42E3F:
    if (0 >= 7) goto loc_00A42E67;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00A42D28;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A42D28;
    local_r10 = (uint32_t)((0) + 1);
    goto loc_00A42E3F;
loc_00A42E67:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A42D28;
    local_r11 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r11 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((*(uint32_t *)(arg1)) <= 8) goto loc_00A43157;
loc_00A42E8E:
    if (0 >= 8) goto loc_00A42EB5;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00A42D28;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A42D28;
    local_r10 = (uint32_t)((0) + (1));
    goto loc_00A42E8E;
loc_00A42EB5:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A42D28;
    Arg3 = 0;
    result = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { result = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 4) goto loc_00A43161;
    if (*(uint64_t *)(v_rip + 0x5954AC) == 0) goto loc_00A430CE;
    v_stack_m30 = v_stack_m18;
    v_stack_m38 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    v_stack_m40 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    result = guard_dispatch_icall((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result)))), result, result, local_r11);
loc_00A42F0C:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m20 + 0x10))) + (64));
    if (((uint32_t)(result)) < 64) goto loc_00A42D28;
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_00A42D28;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) & (0xC0000095ULL));
    if (sign_flag) goto loc_00A42D2D;
    *(uint32_t *)(arg4 + 0x4) = 40;
    result = ExAllocatePool2(256, 40, (uint32_t)(0x20534C53ULL), local_r11);
    local_rbx = 0;
    if (result == 0) goto loc_00A430C4;
    *(uint64_t *)(arg4 + 0x8) = result;
    *(uint32_t *)(arg4) = 0;
    if (result == 0) goto loc_00A4310B;
loc_00A42F7F:
    if (0 >= 0) goto loc_00A42FA8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00A42D28;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (result);
    if (Arg3 < result) goto loc_00A42D28;
    Arg1 = (uint32_t)((0) + (1));
    goto loc_00A42F7F;
loc_00A42FA8:
    if ((Arg3 + 4) < Arg3) goto loc_00A42D28;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_00A43161;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)((uint32_t)(result)));
loc_00A42FD3:
    Arg3 = (uint32_t)((Arg3 + 4) | (0xFFFFFFFFULL));
    if (*(uint64_t *)(arg4 + 0x8) == 0) goto loc_00A430D9;
loc_00A42FEC:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_00A43016;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00A42D28;
    Arg4 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg4 + 0x8));
    if (Arg4 < (*(uint64_t *)(arg4 + 0x8))) goto loc_00A42D28;
    Arg1 = (uint32_t)((0) + (1));
    goto loc_00A42FEC;
loc_00A43016:
    if ((Arg4 + 4) < Arg4) goto loc_00A42D28;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    if ((Arg4 + 12) > Arg1) goto loc_00A43161;
    *(uint32_t *)(arg4) = 8;
    *(uint64_t *)(arg4 + 0x4) = *(uint64_t *)(result);
loc_00A43044:
    if (*(uint64_t *)(arg4 + 0x8) == 0) goto loc_00A43120;
loc_00A43056:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_00A43080;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00A42D28;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(arg4 + 0x8))) goto loc_00A42D28;
    Arg1 = (uint32_t)((0) + (1));
    goto loc_00A43056;
loc_00A43080:
    if ((Arg3 + 4) < Arg3) goto loc_00A42D28;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    if ((Arg3 + 20) > Arg1) goto loc_00A43161;
    *(uint32_t *)(Arg3) = 16;
    *(uint64_t *)(Arg3 + 0x4) = v_xmm0;
    goto loc_00A42D2D;
loc_00A430BA:
    goto loc_00A42B55;
loc_00A430C4:
    goto loc_00A42D2D;
loc_00A430CE:
    goto loc_00A42F0C;
loc_00A430D9:
    result = (uint32_t)((uint32_t)(Arg3 + 4));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 12); }
    local_rbx = (uint32_t)(((uint32_t)(0xC0000017ULL)) & (0xC0000095ULL));
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_00A431A2;
    if (sign_flag) goto loc_00A42D2D;
loc_00A43104:
    local_rbx = 0;
    goto loc_00A43044;
loc_00A4310B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_00A4317F;
    goto loc_00A42D28;
loc_00A43120:
    Arg3 = Arg3 + 4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 20)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) { Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 20); }
    local_rbx = (uint32_t)((local_rbx) & (0xC0000095ULL));
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)(Arg3);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 20)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_00A42D2D;
    Arg1 = 0;
    goto loc_00A42D2D;
loc_00A4314D:
    goto loc_00A42B55;
loc_00A43157:
    goto loc_00A42D2D;
loc_00A43161:
    goto loc_00A42D2D;
loc_00A4316B:
    goto loc_00A42B55;
loc_00A43175:
    goto loc_00A42D2D;
loc_00A4317F:
    *(uint32_t *)(arg4 + 0x4) = 0;
    goto loc_00A42FD3;
loc_00A43188:
    goto loc_00A42B55;
loc_00A43192:
    goto loc_00A42C9F;
loc_00A4319A:
    goto loc_00A42DC5;
loc_00A431A2:
    goto loc_00A43104;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R/W` |
| `Arg4` | `+ 0x0` | `32` | `W` |
| `Arg4` | `+ 0x4` | `32` | `R` |
| `Arg4` | `+ 0x4` | `32` | `R/W` |
| `Arg4` | `+ 0x4` | `32` | `W` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A42ACC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
