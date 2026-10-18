# RtlIpv6StringToAddressA

- RVA: `0x004A6BD0`–`0x004A7065` (길이 `1,173` bytes)
- VA: `0x00000001404A6BD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B6F74`
- 디코드: `286`개 명령, `1,173/1,173` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004A6C43` → [_isascii](../50/_isascii_function_00500660.md) (function, `0x00500660`)
- `0x004A6C52` → [isdigit](../50/isdigit_function_00500680.md) (function, `0x00500680`)
- `0x004A6D79` → [strtol](../4F/strtol_function_004FF358.md) (function, `0x004FF358`)
- `0x004A6DB5` → [_isascii](../50/_isascii_function_00500660.md) (function, `0x00500660`)
- `0x004A6DC6` → [isdigit](../50/isdigit_function_00500680.md) (function, `0x00500680`)
- `0x004A6DF8` → [_isascii](../50/_isascii_function_00500660.md) (function, `0x00500660`)
- `0x004A6E46` → [strtol](../4F/strtol_function_004FF358.md) (function, `0x004FF358`)
- `0x004A6E75` → [isxdigit](../50/isxdigit_function_00500770.md) (function, `0x00500770`)
- `0x004A6F8D` → [_isascii](../50/_isascii_function_00500660.md) (function, `0x00500660`)
- `0x004A6F9C` → [isxdigit](../50/isxdigit_function_00500770.md) (function, `0x00500770`)
- `0x004A6FFB` → [strtol](../4F/strtol_function_004FF358.md) (function, `0x004FF358`)
- `0x004A7049` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x004A705B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- [RtlIpv6StringToAddressExA](../5E/RtlIpv6StringToAddressExA_function_005EC150.md) at `0x005EC1C0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x004A6D60` → [sub_006F99DE + 0x58](../6F/Unknown_function_006F99DE.md) (`tail-transfer`)
  - `0x004A6D9A` → [sub_006F99DE + 0x46](../6F/Unknown_function_006F99DE.md) (`tail-transfer`)
  - `0x004A6F30` → [sub_006F99DE + 0x8](../6F/Unknown_function_006F99DE.md) (`tail-transfer`)
  - `0x004A6F5F` → [sub_006F99DE + 0x25](../6F/Unknown_function_006F99DE.md) (`tail-transfer`)
  - `0x004A6F6F` → [sub_006F99DE + 0x25](../6F/Unknown_function_006F99DE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
004A6BD0  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
004A6BD5  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
004A6BDA  53                              push rbx
004A6BDB  55                              push rbp
004A6BDC  56                              push rsi
004A6BDD  57                              push rdi
004A6BDE  41 54                           push r12
004A6BE0  41 55                           push r13
004A6BE2  41 56                           push r14
004A6BE4  41 57                           push r15
004A6BE6  48 83 EC 38                     sub rsp, 0x38
004A6BEA  33 C0                           xor eax, eax
004A6BEC  49 8B F0                        mov rsi, r8
004A6BEF  44 8A D8                        mov r11b, al
004A6BF2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004A6BF7  44 89 5C 24 20                  mov dword ptr [rsp + 0x20], r11d
004A6BFC  48 8B D9                        mov rbx, rcx
004A6BFF  44 8B E8                        mov r13d, eax
004A6C02  88 84 24 80 00 00 00            mov byte ptr [rsp + 0x80], al
004A6C09  44 8B C8                        mov r9d, eax
004A6C0C  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
004A6C13  44 8A C0                        mov r8b, al
004A6C16  8B F8                           mov edi, eax
004A6C18  44 8B F0                        mov r14d, eax
004A6C1B  44 8B E0                        mov r12d, eax
004A6C1E  44 8B F8                        mov r15d, eax
004A6C21  44 8B D0                        mov r10d, eax
004A6C24  0F BE 2B                        movsx ebp, byte ptr [rbx]
004A6C27  40 84 ED                        test bpl, bpl
004A6C2A  74 7E                           je 0x1404a6caa
004A6C2C  41 8B CD                        mov ecx, r13d
004A6C2F  45 85 ED                        test r13d, r13d
004A6C32  0F 84 C8 00 00 00               je 0x1404a6d00
004A6C38  83 E9 01                        sub ecx, 1
004A6C3B  0F 85 5E 01 00 00               jne 0x1404a6d9f
004A6C41  8B CD                           mov ecx, ebp
004A6C43  E8 18 9A 05 00                  call 0x140500660
004A6C48  85 C0                           test eax, eax
004A6C4A  0F 84 A6 01 00 00               je 0x1404a6df6
004A6C50  8B CD                           mov ecx, ebp
004A6C52  E8 29 9A 05 00                  call 0x140500680
004A6C57  85 C0                           test eax, eax
004A6C59  0F 84 97 01 00 00               je 0x1404a6df6
004A6C5F  44 8A 84 24 80 00 00 00         mov r8b, byte ptr [rsp + 0x80]
004A6C67  41 FF C4                        inc r12d
004A6C6A  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
004A6C6F  44 8B 94 24 98 00 00 00         mov r10d, dword ptr [rsp + 0x98]
004A6C77  48 8B B4 24 90 00 00 00         mov rsi, qword ptr [rsp + 0x90]
004A6C7F  48 FF C3                        inc rbx
004A6C82  44 8B 5C 24 20                  mov r11d, dword ptr [rsp + 0x20]
004A6C87  EB 9B                           jmp 0x1404a6c24
004A6C89  83 FF 06                        cmp edi, 6
004A6C8C  0F 87 4B 02 00 00               ja 0x1404a6edd
004A6C92  83 FF 07                        cmp edi, 7
004A6C95  77 13                           ja 0x1404a6caa
004A6C97  80 7B 01 3A                     cmp byte ptr [rbx + 1], 0x3a
004A6C9B  0F 85 7E 02 00 00               jne 0x1404a6f1f
004A6CA1  45 85 FF                        test r15d, r15d
004A6CA4  0F 84 42 02 00 00               je 0x1404a6eec
004A6CAA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
004A6CB2  48 89 18                        mov qword ptr [rax], rbx
004A6CB5  33 DB                           xor ebx, ebx
004A6CB7  45 85 F6                        test r14d, r14d
004A6CBA  0F 85 63 01 00 00               jne 0x1404a6e23
004A6CC0  44 8D 43 01                     lea r8d, [rbx + 1]
004A6CC4  45 85 FF                        test r15d, r15d
004A6CC7  0F 84 0B 03 00 00               je 0x1404a6fd8
004A6CCD  45 3B E8                        cmp r13d, r8d
004A6CD0  0F 85 E7 01 00 00               jne 0x1404a6ebd
004A6CD6  45 85 F6                        test r14d, r14d
004A6CD9  0F 85 07 03 00 00               jne 0x1404a6fe6
004A6CDF  41 83 FC 04                     cmp r12d, 4
004A6CE3  0F 86 52 01 00 00               jbe 0x1404a6e3b
004A6CE9  B8 0D 00 00 C0                  mov eax, 0xc000000d
004A6CEE  48 83 C4 38                     add rsp, 0x38
004A6CF2  41 5F                           pop r15
004A6CF4  41 5E                           pop r14
004A6CF6  41 5D                           pop r13
004A6CF8  41 5C                           pop r12
004A6CFA  5F                              pop rdi
004A6CFB  5E                              pop rsi
004A6CFC  5D                              pop rbp
004A6CFD  5B                              pop rbx
004A6CFE  C3                              ret
004A6CFF  CC                              int3
004A6D00  40 80 FD 3A                     cmp bpl, 0x3a
004A6D04  0F 85 9E 00 00 00               jne 0x1404a6da8
004A6D0A  45 85 F6                        test r14d, r14d
004A6D0D  0F 85 03 01 00 00               jne 0x1404a6e16
004A6D13  85 FF                           test edi, edi
004A6D15  75 93                           jne 0x1404a6caa
004A6D17  40 38 6B 01                     cmp byte ptr [rbx + 1], bpl
004A6D1B  75 8D                           jne 0x1404a6caa
004A6D1D  8D 6F 01                        lea ebp, [rdi + 1]
004A6D20  45 0F B6 DB                     movzx r11d, r11b
004A6D24  45 85 D2                        test r10d, r10d
004A6D27  41 8B C2                        mov eax, r10d
004A6D2A  44 8B FD                        mov r15d, ebp
004A6D2D  44 0F 44 DD                     cmove r11d, ebp
004A6D31  33 D2                           xor edx, edx
004A6D33  44 89 5C 24 20                  mov dword ptr [rsp + 0x20], r11d
004A6D38  44 03 D5                        add r10d, ebp
004A6D3B  45 8D 5E 02                     lea r11d, [r14 + 2]
004A6D3F  44 89 94 24 98 00 00 00         mov dword ptr [rsp + 0x98], r10d
004A6D47  41 8B FB                        mov edi, r11d
004A6D4A  66 89 14 46                     mov word ptr [rsi + rax*2], dx
004A6D4E  45 8B EB                        mov r13d, r11d
004A6D51  48 FF C3                        inc rbx
004A6D54  4D 85 C9                        test r9, r9
004A6D57  0F 84 1A FF FF FF               je 0x1404a6c77
004A6D5D  45 85 F6                        test r14d, r14d
004A6D60  0F 85 D0 2C 25 00               jne 0x1406f9a36
004A6D66  41 83 FC 04                     cmp r12d, 4
004A6D6A  0F 87 79 FF FF FF               ja 0x1404a6ce9
004A6D70  33 D2                           xor edx, edx
004A6D72  45 8D 46 10                     lea r8d, [r14 + 0x10]
004A6D76  49 8B C9                        mov rcx, r9
004A6D79  E8 DA 85 05 00                  call 0x1404ff358
004A6D7E  44 8B 94 24 98 00 00 00         mov r10d, dword ptr [rsp + 0x98]
004A6D86  66 C1 C8 08                     ror ax, 8
004A6D8A  66 42 89 04 56                  mov word ptr [rsi + r10*2], ax
004A6D8F  44 03 D5                        add r10d, ebp
004A6D92  44 89 94 24 98 00 00 00         mov dword ptr [rsp + 0x98], r10d
004A6D9A  E9 85 2C 25 00                  jmp 0x1406f9a24
004A6D9F  83 F9 01                        cmp ecx, 1
004A6DA2  0F 85 F5 00 00 00               jne 0x1404a6e9d
004A6DA8  83 FF 07                        cmp edi, 7
004A6DAB  0F 87 C3 01 00 00               ja 0x1404a6f74
004A6DB1  8B CD                           mov ecx, ebp
004A6DB3  8B F5                           mov esi, ebp
004A6DB5  E8 A6 98 05 00                  call 0x140500660
004A6DBA  33 ED                           xor ebp, ebp
004A6DBC  85 C0                           test eax, eax
004A6DBE  0F 84 C7 01 00 00               je 0x1404a6f8b
004A6DC4  8B CE                           mov ecx, esi
004A6DC6  E8 B5 98 05 00                  call 0x140500680
004A6DCB  85 C0                           test eax, eax
004A6DCD  0F 84 B8 01 00 00               je 0x1404a6f8b
004A6DD3  33 C0                           xor eax, eax
004A6DD5  44 8D 55 01                     lea r10d, [rbp + 1]
004A6DD9  44 8A C0                        mov r8b, al
004A6DDC  88 84 24 80 00 00 00            mov byte ptr [rsp + 0x80], al
004A6DE3  45 8B E2                        mov r12d, r10d
004A6DE6  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
004A6DEB  45 8B EA                        mov r13d, r10d
004A6DEE  4C 8B CB                        mov r9, rbx
004A6DF1  E9 79 FE FF FF                  jmp 0x1404a6c6f
004A6DF6  8B CD                           mov ecx, ebp
004A6DF8  E8 63 98 05 00                  call 0x140500660
004A6DFD  33 C9                           xor ecx, ecx
004A6DFF  85 C0                           test eax, eax
004A6E01  75 70                           jne 0x1404a6e73
004A6E03  40 80 FD 3A                     cmp bpl, 0x3a
004A6E07  0F 85 28 01 00 00               jne 0x1404a6f35
004A6E0D  45 85 F6                        test r14d, r14d
004A6E10  0F 84 73 FE FF FF               je 0x1404a6c89
004A6E16  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
004A6E1E  48 89 18                        mov qword ptr [rax], rbx
004A6E21  33 DB                           xor ebx, ebx
004A6E23  41 B8 01 00 00 00               mov r8d, 1
004A6E29  41 83 FE 03                     cmp r14d, 3
004A6E2D  0F 85 B6 FE FF FF               jne 0x1404a6ce9
004A6E33  41 03 F8                        add edi, r8d
004A6E36  E9 89 FE FF FF                  jmp 0x1404a6cc4
004A6E3B  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
004A6E40  33 D2                           xor edx, edx
004A6E42  44 8D 42 10                     lea r8d, [rdx + 0x10]
004A6E46  E8 0D 85 05 00                  call 0x1404ff358
004A6E4B  8B 8C 24 98 00 00 00            mov ecx, dword ptr [rsp + 0x98]
004A6E52  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
004A6E5A  66 C1 C8 08                     ror ax, 8
004A6E5E  66 41 89 04 49                  mov word ptr [r9 + rcx*2], ax
004A6E63  45 85 FF                        test r15d, r15d
004A6E66  0F 85 BB 01 00 00               jne 0x1404a7027
004A6E6C  33 C0                           xor eax, eax
004A6E6E  E9 7B FE FF FF                  jmp 0x1404a6cee
004A6E73  8B CD                           mov ecx, ebp
004A6E75  E8 F6 98 05 00                  call 0x140500770
004A6E7A  33 C9                           xor ecx, ecx
004A6E7C  85 C0                           test eax, eax
004A6E7E  74 83                           je 0x1404a6e03
004A6E80  44 8D 41 01                     lea r8d, [rcx + 1]
004A6E84  45 03 E0                        add r12d, r8d
004A6E87  45 85 F6                        test r14d, r14d
004A6E8A  0F 85 36 01 00 00               jne 0x1404a6fc6
004A6E90  44 88 84 24 80 00 00 00         mov byte ptr [rsp + 0x80], r8b
004A6E98  E9 CD FD FF FF                  jmp 0x1404a6c6a
004A6E9D  BD 01 00 00 00                  mov ebp, 1
004A6EA2  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
004A6EA7  44 88 84 24 80 00 00 00         mov byte ptr [rsp + 0x80], r8b
004A6EAF  44 3B ED                        cmp r13d, ebp
004A6EB2  0F 84 BF FD FF FF               je 0x1404a6c77
004A6EB8  E9 97 FE FF FF                  jmp 0x1404a6d54
004A6EBD  41 83 FD 02                     cmp r13d, 2
004A6EC1  0F 85 22 FE FF FF               jne 0x1404a6ce9
004A6EC7  8B 8C 24 98 00 00 00            mov ecx, dword ptr [rsp + 0x98]
004A6ECE  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
004A6ED6  66 41 89 1C 49                  mov word ptr [r9 + rcx*2], bx
004A6EDB  EB 86                           jmp 0x1404a6e63
004A6EDD  38 4C 24 20                     cmp byte ptr [rsp + 0x20], cl
004A6EE1  0F 84 C3 FD FF FF               je 0x1404a6caa
004A6EE7  E9 A6 FD FF FF                  jmp 0x1404a6c92
004A6EEC  44 8A 84 24 80 00 00 00         mov r8b, byte ptr [rsp + 0x80]
004A6EF4  44 8D 7F 01                     lea r15d, [rdi + 1]
004A6EF8  48 8B B4 24 90 00 00 00         mov rsi, qword ptr [rsp + 0x90]
004A6F00  41 BD 02 00 00 00               mov r13d, 2
004A6F06  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
004A6F0B  83 C7 02                        add edi, 2
004A6F0E  44 8B 94 24 98 00 00 00         mov r10d, dword ptr [rsp + 0x98]
004A6F16  41 8D 6D FF                     lea ebp, [r13 - 1]
004A6F1A  E9 32 FE FF FF                  jmp 0x1404a6d51
004A6F1F  44 8A 84 24 80 00 00 00         mov r8b, byte ptr [rsp + 0x80]
004A6F27  BD 01 00 00 00                  mov ebp, 1
004A6F2C  03 FD                           add edi, ebp
004A6F2E  33 C0                           xor eax, eax
004A6F30  E9 B1 2A 25 00                  jmp 0x1406f99e6
004A6F35  40 80 FD 2E                     cmp bpl, 0x2e
004A6F39  0F 85 6B FD FF FF               jne 0x1404a6caa
004A6F3F  44 8A 84 24 80 00 00 00         mov r8b, byte ptr [rsp + 0x80]
004A6F47  33 C0                           xor eax, eax
004A6F49  45 84 C0                        test r8b, r8b
004A6F4C  0F 85 58 FD FF FF               jne 0x1404a6caa
004A6F52  41 83 FE 02                     cmp r14d, 2
004A6F56  0F 87 BA FE FF FF               ja 0x1404a6e16
004A6F5C  83 FF 06                        cmp edi, 6
004A6F5F  0F 86 9E 2A 25 00               jbe 0x1406f9a03
004A6F65  38 44 24 20                     cmp byte ptr [rsp + 0x20], al
004A6F69  0F 84 3B FD FF FF               je 0x1404a6caa
004A6F6F  E9 8F 2A 25 00                  jmp 0x1406f9a03
004A6F74  83 FF 08                        cmp edi, 8
004A6F77  0F 87 2D FD FF FF               ja 0x1404a6caa
004A6F7D  45 84 DB                        test r11b, r11b
004A6F80  0F 84 24 FD FF FF               je 0x1404a6caa
004A6F86  E9 26 FE FF FF                  jmp 0x1404a6db1
004A6F8B  8B CE                           mov ecx, esi
004A6F8D  E8 CE 96 05 00                  call 0x140500660
004A6F92  85 C0                           test eax, eax
004A6F94  0F 84 10 FD FF FF               je 0x1404a6caa
004A6F9A  8B CE                           mov ecx, esi
004A6F9C  E8 CF 97 05 00                  call 0x140500770
004A6FA1  85 C0                           test eax, eax
004A6FA3  0F 84 01 FD FF FF               je 0x1404a6caa
004A6FA9  45 85 F6                        test r14d, r14d
004A6FAC  0F 85 64 FE FF FF               jne 0x1404a6e16
004A6FB2  45 8D 56 01                     lea r10d, [r14 + 1]
004A6FB6  45 8A C2                        mov r8b, r10b
004A6FB9  44 88 94 24 80 00 00 00         mov byte ptr [rsp + 0x80], r10b
004A6FC1  E9 1D FE FF FF                  jmp 0x1404a6de3
004A6FC6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
004A6FCE  48 89 18                        mov qword ptr [rax], rbx
004A6FD1  33 DB                           xor ebx, ebx
004A6FD3  E9 51 FE FF FF                  jmp 0x1404a6e29
004A6FD8  83 FF 07                        cmp edi, 7
004A6FDB  0F 85 08 FD FF FF               jne 0x1404a6ce9
004A6FE1  E9 E7 FC FF FF                  jmp 0x1404a6ccd
004A6FE6  41 83 FC 03                     cmp r12d, 3
004A6FEA  0F 87 F9 FC FF FF               ja 0x1404a6ce9
004A6FF0  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
004A6FF5  33 D2                           xor edx, edx
004A6FF7  44 8D 42 0A                     lea r8d, [rdx + 0xa]
004A6FFB  E8 58 83 05 00                  call 0x1404ff358
004A7000  3D FF 00 00 00                  cmp eax, 0xff
004A7005  0F 87 DE FC FF FF               ja 0x1404a6ce9
004A700B  8B 8C 24 98 00 00 00            mov ecx, dword ptr [rsp + 0x98]
004A7012  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
004A701A  41 8D 0C 4E                     lea ecx, [r14 + rcx*2]
004A701E  42 88 04 09                     mov byte ptr [rcx + r9], al
004A7022  E9 3C FE FF FF                  jmp 0x1404a6e63
004A7027  41 8B C7                        mov eax, r15d
004A702A  44 8B C7                        mov r8d, edi
004A702D  45 2B C7                        sub r8d, r15d
004A7030  BE 08 00 00 00                  mov esi, 8
004A7035  44 2B FF                        sub r15d, edi
004A7038  4D 03 C0                        add r8, r8
004A703B  44 03 FE                        add r15d, esi
004A703E  49 8D 1C 41                     lea rbx, [r9 + rax*2]
004A7042  48 8B D3                        mov rdx, rbx
004A7045  4B 8D 0C 79                     lea rcx, [r9 + r15*2]
004A7049  E8 F2 F7 21 00                  call 0x1406c6840
004A704E  2B F7                           sub esi, edi
004A7050  33 D2                           xor edx, edx
004A7052  44 8B C6                        mov r8d, esi
004A7055  48 8B CB                        mov rcx, rbx
004A7058  4D 03 C0                        add r8, r8
004A705B  E8 E0 FB 21 00                  call 0x1406c6c40
004A7060  E9 07 FE FF FF                  jmp 0x1404a6e6c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlIpv6StringToAddressA(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p8;
    unsigned __int8 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned int v_stack_p98;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (56);
    result = 0;
    v_stack_m50 = 0;
    v_stack_m58 = 0;
    v_stack_p8 = 0;
    v_stack_p20 = 0;
loc_004A6C24:
    if ((unsigned __int8)((__int8)(*(unsigned __int8 *)(a1))) == 0) goto loc_004A6CAA;
    if (0 == 0) goto loc_004A6D00;
    a1 = (unsigned int)((0) - (1));
    if (condition_is_not_equal) goto loc_004A6D9F;
    result = _isascii((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(a1)))), a2, 0, 0);
    if ((unsigned int)(result) == 0) goto loc_004A6DF6;
    result = isdigit((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(a1)))), a2, 0, 0);
    if ((unsigned int)(result) == 0) goto loc_004A6DF6;
    v_r12 = (unsigned int)((0) + 1);
loc_004A6C6A:
loc_004A6C6F:
loc_004A6C77:
    v_rbx = (a1) + 1;
    goto loc_004A6C24;
loc_004A6C89:
    if (0 > 6) goto loc_004A6EDD;
loc_004A6C92:
    if (0 > 7) goto loc_004A6CAA;
    if ((*(unsigned __int8 *)(v_rbx + 1)) != 58) goto loc_004A6F1F;
    if (0 == 0) goto loc_004A6EEC;
loc_004A6CAA:
    *(unsigned __int64 *)(v_stack_p10) = v_rbx;
    v_rbx = 0;
    if (0 != 0) goto loc_004A6E23;
loc_004A6CC4:
    if (0 == 0) goto loc_004A6FD8;
loc_004A6CCD:
    if (0 != ((unsigned int)(v_rbx + 1))) goto loc_004A6EBD;
    if (0 != 0) goto loc_004A6FE6;
    if (((unsigned int)(v_r12)) <= 4) goto loc_004A6E3B;
loc_004A6CE9:
loc_004A6CEE:
    v_rsp = (v_rsp) + (56);
    return (unsigned int)(0xC000000DULL);
loc_004A6D00:
    if (((unsigned __int8)((__int8)(*(unsigned __int8 *)(a1)))) != 58) goto loc_004A6DA8;
    if (0 != 0) goto loc_004A6E16;
    if (0 != 0) goto loc_004A6CAA;
    if ((*(unsigned __int8 *)(v_rbx + 1)) != ((unsigned __int8)((__int8)(*(unsigned __int8 *)(a1))))) goto loc_004A6CAA;
    v_r11 = (unsigned __int8)((unsigned int)(v_stack_m58));
    if ((unsigned int)((unsigned int)(v_stack_p20)) == 0) { v_r11 = (unsigned int)(0 + 1); }
    a2 = 0;
    v_stack_p20 = (unsigned int)(v_r11);
    v_r10 = (unsigned int)(((unsigned int)(v_stack_p20)) + ((unsigned int)(0 + 1)));
    v_stack_p98 = (unsigned int)(v_r10);
    *(unsigned __int16 *)(v_stack_p18 + (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))) * 2) = 0;
loc_004A6D51:
    v_rbx = (v_rbx) + 1;
loc_004A6D54:
    if (v_stack_m50 == 0) goto loc_004A6C77;
    if (((unsigned int)(v_r12)) > 4) goto loc_004A6CE9;
    a2 = 0;
    result = strtol(v_stack_m50, a2, 0 + 16, v_stack_m50);
    *(unsigned __int16 *)(v_stack_p18 + (unsigned int)(v_stack_p98) * 2) = (unsigned __int16)(result);
    v_r10 = (unsigned int)(((unsigned int)(v_stack_p98)) + ((unsigned int)(0 + 1)));
    v_stack_p98 = (unsigned int)(v_r10);
loc_004A6D9F:
    if (((unsigned int)(v_stack_m50)) != 1) goto loc_004A6E9D;
loc_004A6DA8:
    if (((unsigned int)((unsigned int)((unsigned int)(0 + 2)))) > 7) goto loc_004A6F74;
loc_004A6DB1:
    result = _isascii((unsigned int)((unsigned int)(0 + 1)), a2, 0 + 16, v_stack_m50);
    v_rbp = 0;
    if ((unsigned int)(result) == 0) goto loc_004A6F8B;
    result = isdigit((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0 + 1)))), a2, 0 + 16, v_stack_m50);
    if ((unsigned int)(result) == 0) goto loc_004A6F8B;
    result = 0;
    v_stack_p80 = 0;
loc_004A6DE3:
    v_stack_p28 = v_rbx;
    goto loc_004A6C6F;
loc_004A6DF6:
    result = _isascii(0, a2, 0, v_rbx);
    a1 = 0;
    if ((unsigned int)(result) != 0) goto loc_004A6E73;
loc_004A6E03:
    if (0 != 58) goto loc_004A6F35;
    if (0 == 0) goto loc_004A6C89;
loc_004A6E16:
    *(unsigned __int64 *)(v_stack_p88) = v_rbx;
    v_rbx = 0;
loc_004A6E23:
loc_004A6E29:
    if (0 != 3) goto loc_004A6CE9;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(0 + 2))) + (1));
    goto loc_004A6CC4;
loc_004A6E3B:
    a2 = 0;
    result = strtol(v_stack_p28, a2, a2 + 16, v_rbx);
    *(unsigned __int16 *)(v_stack_p90 + (unsigned int)(v_stack_p98) * 2) = (unsigned __int16)(result);
loc_004A6E63:
    if ((unsigned int)((unsigned int)((unsigned int)(0 + 1))) != 0) goto loc_004A7027;
loc_004A6E6C:
    result = 0;
    goto loc_004A6CEE;
loc_004A6E73:
    result = isxdigit(0, a2, a2 + 16, v_stack_p90);
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_004A6E03;
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_rbp + 1))) + ((unsigned int)(a1 + 1)));
    if (0 != 0) goto loc_004A6FC6;
    v_stack_p80 = (unsigned __int8)(a1 + 1);
    goto loc_004A6C6A;
loc_004A6E9D:
    v_stack_p28 = v_stack_p90;
    v_stack_p80 = (unsigned __int8)(a1 + 1);
    if (((unsigned int)((unsigned int)((unsigned int)(v_rbp + 1)))) == 1) goto loc_004A6C77;
    goto loc_004A6D54;
loc_004A6EBD:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rbp + 1)))) != 2) goto loc_004A6CE9;
    *(unsigned __int16 *)(v_stack_p90 + (unsigned int)(v_stack_p98) * 2) = 0;
    goto loc_004A6E63;
loc_004A6EDD:
    if (v_stack_p20 == ((unsigned __int8)((unsigned int)(v_stack_p98)))) goto loc_004A6CAA;
    goto loc_004A6C92;
loc_004A6EEC:
    v_rdi = (unsigned int)((v_rdi) + (2));
    goto loc_004A6D51;
loc_004A6F1F:
    v_rdi = (unsigned int)((v_rdi) + (1));
    result = 0;
loc_004A6F35:
    if (1 != 46) goto loc_004A6CAA;
    result = 0;
    if ((unsigned __int8)(v_stack_p80) != 0) goto loc_004A6CAA;
    if (0 > 2) goto loc_004A6E16;
    if (v_stack_p20 == 0) goto loc_004A6CAA;
loc_004A6F74:
    if (((unsigned int)(v_rdi)) > 8) goto loc_004A6CAA;
    if ((unsigned __int8)(0 + 2) == 0) goto loc_004A6CAA;
    goto loc_004A6DB1;
loc_004A6F8B:
    result = _isascii((unsigned int)((unsigned int)(v_stack_p90)), a2, v_stack_p80, v_stack_p28);
    if ((unsigned int)(result) == 0) goto loc_004A6CAA;
    result = isxdigit((unsigned int)((unsigned int)(v_stack_p90)), a2, v_stack_p80, v_stack_p28);
    if ((unsigned int)(result) == 0) goto loc_004A6CAA;
    if (0 != 0) goto loc_004A6E16;
    v_stack_p80 = (unsigned __int8)(0 + 1);
    goto loc_004A6DE3;
loc_004A6FC6:
    *(unsigned __int64 *)(v_stack_p88) = 0;
    v_rbx = 0;
    goto loc_004A6E29;
loc_004A6FD8:
    if (((unsigned int)(v_rdi)) != 7) goto loc_004A6CE9;
    goto loc_004A6CCD;
loc_004A6FE6:
    if (((unsigned int)(v_r12)) > 3) goto loc_004A6CE9;
    a2 = 0;
    result = strtol(v_stack_p28, a2, a2 + 10, v_stack_p28);
    if (((unsigned int)(result)) > 255) goto loc_004A6CE9;
    *(unsigned __int8 *)(0 + (unsigned int)(v_stack_p98) * 2 + v_stack_p90 * 1) = (unsigned __int8)(result);
    goto loc_004A6E63;
loc_004A7027:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - ((unsigned int)(v_rdi + 1)));
    v_r15 = (unsigned int)((v_rdi + 1) - ((unsigned int)(v_rdi)));
    a3 = (a3) + (a3);
    v_r15 = (unsigned int)((v_r15) + (8));
    result = memcpy(v_stack_p90 + v_r15 * 2, v_stack_p90 + (unsigned int)((unsigned int)(v_rdi + 1)) * 2, a3, v_stack_p90);
    v_rsi = (unsigned int)((8) - ((unsigned int)(v_rdi)));
    a2 = 0;
    a3 = ((unsigned int)((unsigned int)(v_rsi))) + ((unsigned int)((unsigned int)(v_rsi)));
    result = memset(v_stack_p90 + (unsigned int)((unsigned int)(v_rdi + 1)) * 2, a2, a3, v_stack_p90);
    goto loc_004A6E6C;
}
```

## 5. (Beta) C Style

```c
int64_t RtlIpv6StringToAddressA(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p8;
    uint8_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint32_t v_stack_p98;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (56);
    result = 0;
    v_stack_m50 = 0;
    v_stack_m58 = 0;
    v_stack_p8 = 0;
    v_stack_p20 = 0;
loc_004A6C24:
    if ((uint8_t)((int8_t)(*(uint8_t *)(Arg1))) == 0) goto loc_004A6CAA;
    if (0 == 0) goto loc_004A6D00;
    Arg1 = (uint32_t)((0) - (1));
    if (condition_is_not_equal) goto loc_004A6D9F;
    result = _isascii((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(Arg1)))), Arg2, 0, 0);
    if ((uint32_t)(result) == 0) goto loc_004A6DF6;
    result = isdigit((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(Arg1)))), Arg2, 0, 0);
    if ((uint32_t)(result) == 0) goto loc_004A6DF6;
    local_r12 = (uint32_t)((0) + 1);
loc_004A6C6A:
loc_004A6C6F:
loc_004A6C77:
    local_rbx = (Arg1) + 1;
    goto loc_004A6C24;
loc_004A6C89:
    if (0 > 6) goto loc_004A6EDD;
loc_004A6C92:
    if (0 > 7) goto loc_004A6CAA;
    if ((*(uint8_t *)(local_rbx + 0x1)) != 58) goto loc_004A6F1F;
    if (0 == 0) goto loc_004A6EEC;
loc_004A6CAA:
    *(uint64_t *)(v_stack_p10) = local_rbx;
    local_rbx = 0;
    if (0 != 0) goto loc_004A6E23;
loc_004A6CC4:
    if (0 == 0) goto loc_004A6FD8;
loc_004A6CCD:
    if (0 != ((uint32_t)(local_rbx + 1))) goto loc_004A6EBD;
    if (0 != 0) goto loc_004A6FE6;
    if (((uint32_t)(local_r12)) <= 4) goto loc_004A6E3B;
loc_004A6CE9:
loc_004A6CEE:
    local_rsp = (local_rsp) + (56);
    return (uint32_t)(0xC000000DULL);
loc_004A6D00:
    if (((uint8_t)((int8_t)(*(uint8_t *)(Arg1)))) != 58) goto loc_004A6DA8;
    if (0 != 0) goto loc_004A6E16;
    if (0 != 0) goto loc_004A6CAA;
    if ((*(uint8_t *)(local_rbx + 0x1)) != ((uint8_t)((int8_t)(*(uint8_t *)(Arg1))))) goto loc_004A6CAA;
    local_r11 = (uint8_t)((uint32_t)(v_stack_m58));
    if ((uint32_t)((uint32_t)(v_stack_p20)) == 0) { local_r11 = (uint32_t)(0 + 1); }
    Arg2 = 0;
    v_stack_p20 = (uint32_t)(local_r11);
    local_r10 = (uint32_t)(((uint32_t)(v_stack_p20)) + ((uint32_t)(0 + 1)));
    v_stack_p98 = (uint32_t)(local_r10);
    *(uint16_t *)(v_stack_p18 + (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))) * 2) = 0;
loc_004A6D51:
    local_rbx = (local_rbx) + 1;
loc_004A6D54:
    if (v_stack_m50 == 0) goto loc_004A6C77;
    if (((uint32_t)(local_r12)) > 4) goto loc_004A6CE9;
    Arg2 = 0;
    result = strtol(v_stack_m50, Arg2, 0 + 16, v_stack_m50);
    *(uint16_t *)(v_stack_p18 + (uint32_t)(v_stack_p98) * 2) = (uint16_t)(result);
    local_r10 = (uint32_t)(((uint32_t)(v_stack_p98)) + ((uint32_t)(0 + 1)));
    v_stack_p98 = (uint32_t)(local_r10);
loc_004A6D9F:
    if (((uint32_t)(v_stack_m50)) != 1) goto loc_004A6E9D;
loc_004A6DA8:
    if (((uint32_t)((uint32_t)((uint32_t)(0 + 2)))) > 7) goto loc_004A6F74;
loc_004A6DB1:
    result = _isascii((uint32_t)((uint32_t)(0 + 1)), Arg2, 0 + 16, v_stack_m50);
    local_rbp = 0;
    if ((uint32_t)(result) == 0) goto loc_004A6F8B;
    result = isdigit((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0 + 1)))), Arg2, 0 + 16, v_stack_m50);
    if ((uint32_t)(result) == 0) goto loc_004A6F8B;
    result = 0;
    v_stack_p80 = 0;
loc_004A6DE3:
    v_stack_p28 = local_rbx;
    goto loc_004A6C6F;
loc_004A6DF6:
    result = _isascii(0, Arg2, 0, local_rbx);
    Arg1 = 0;
    if ((uint32_t)(result) != 0) goto loc_004A6E73;
loc_004A6E03:
    if (0 != 58) goto loc_004A6F35;
    if (0 == 0) goto loc_004A6C89;
loc_004A6E16:
    *(uint64_t *)(v_stack_p88) = local_rbx;
    local_rbx = 0;
loc_004A6E23:
loc_004A6E29:
    if (0 != 3) goto loc_004A6CE9;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(0 + 2))) + (1));
    goto loc_004A6CC4;
loc_004A6E3B:
    Arg2 = 0;
    result = strtol(v_stack_p28, Arg2, Arg2 + 16, local_rbx);
    *(uint16_t *)(v_stack_p90 + (uint32_t)(v_stack_p98) * 2) = (uint16_t)(result);
loc_004A6E63:
    if ((uint32_t)((uint32_t)((uint32_t)(0 + 1))) != 0) goto loc_004A7027;
loc_004A6E6C:
    result = 0;
    goto loc_004A6CEE;
loc_004A6E73:
    result = isxdigit(0, Arg2, Arg2 + 16, v_stack_p90);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) goto loc_004A6E03;
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(local_rbp + 1))) + ((uint32_t)(Arg1 + 1)));
    if (0 != 0) goto loc_004A6FC6;
    v_stack_p80 = (uint8_t)(Arg1 + 1);
    goto loc_004A6C6A;
loc_004A6E9D:
    v_stack_p28 = v_stack_p90;
    v_stack_p80 = (uint8_t)(Arg1 + 1);
    if (((uint32_t)((uint32_t)((uint32_t)(local_rbp + 1)))) == 1) goto loc_004A6C77;
    goto loc_004A6D54;
loc_004A6EBD:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rbp + 1)))) != 2) goto loc_004A6CE9;
    *(uint16_t *)(v_stack_p90 + (uint32_t)(v_stack_p98) * 2) = 0;
    goto loc_004A6E63;
loc_004A6EDD:
    if (v_stack_p20 == ((uint8_t)((uint32_t)(v_stack_p98)))) goto loc_004A6CAA;
    goto loc_004A6C92;
loc_004A6EEC:
    local_rdi = (uint32_t)((local_rdi) + (2));
    goto loc_004A6D51;
loc_004A6F1F:
    local_rdi = (uint32_t)((local_rdi) + (1));
    result = 0;
loc_004A6F35:
    if (1 != 46) goto loc_004A6CAA;
    result = 0;
    if ((uint8_t)(v_stack_p80) != 0) goto loc_004A6CAA;
    if (0 > 2) goto loc_004A6E16;
    if (v_stack_p20 == 0) goto loc_004A6CAA;
loc_004A6F74:
    if (((uint32_t)(local_rdi)) > 8) goto loc_004A6CAA;
    if ((uint8_t)(0 + 2) == 0) goto loc_004A6CAA;
    goto loc_004A6DB1;
loc_004A6F8B:
    result = _isascii((uint32_t)((uint32_t)(v_stack_p90)), Arg2, v_stack_p80, v_stack_p28);
    if ((uint32_t)(result) == 0) goto loc_004A6CAA;
    result = isxdigit((uint32_t)((uint32_t)(v_stack_p90)), Arg2, v_stack_p80, v_stack_p28);
    if ((uint32_t)(result) == 0) goto loc_004A6CAA;
    if (0 != 0) goto loc_004A6E16;
    v_stack_p80 = (uint8_t)(0 + 1);
    goto loc_004A6DE3;
loc_004A6FC6:
    *(uint64_t *)(v_stack_p88) = 0;
    local_rbx = 0;
    goto loc_004A6E29;
loc_004A6FD8:
    if (((uint32_t)(local_rdi)) != 7) goto loc_004A6CE9;
    goto loc_004A6CCD;
loc_004A6FE6:
    if (((uint32_t)(local_r12)) > 3) goto loc_004A6CE9;
    Arg2 = 0;
    result = strtol(v_stack_p28, Arg2, Arg2 + 10, v_stack_p28);
    if (((uint32_t)(result)) > 255) goto loc_004A6CE9;
    *(uint8_t *)(0 + (uint32_t)(v_stack_p98) * 2 + v_stack_p90 * 1) = (uint8_t)(result);
    goto loc_004A6E63;
loc_004A7027:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - ((uint32_t)(local_rdi + 1)));
    local_r15 = (uint32_t)((local_rdi + 1) - ((uint32_t)(local_rdi)));
    Arg3 = (Arg3) + (Arg3);
    local_r15 = (uint32_t)((local_r15) + (8));
    result = memcpy(v_stack_p90 + local_r15 * 2, v_stack_p90 + (uint32_t)((uint32_t)(local_rdi + 1)) * 2, Arg3, v_stack_p90);
    local_rsi = (uint32_t)((8) - ((uint32_t)(local_rdi)));
    Arg2 = 0;
    Arg3 = ((uint32_t)((uint32_t)(local_rsi))) + ((uint32_t)((uint32_t)(local_rsi)));
    result = memset(v_stack_p90 + (uint32_t)((uint32_t)(local_rdi + 1)) * 2, Arg2, Arg3, v_stack_p90);
    goto loc_004A6E6C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A6BD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
