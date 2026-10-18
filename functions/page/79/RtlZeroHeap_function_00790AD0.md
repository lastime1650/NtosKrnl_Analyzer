# RtlZeroHeap

- RVA: `0x00790AD0`–`0x00790F80` (길이 `1,200` bytes)
- VA: `0x0000000140790AD0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CFC40`
- 디코드: `307`개 명령, `1,200/1,200` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00790B36` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00790BC0` → [RtlpAnalyzeHeapFailure](../../text/5F/RtlpAnalyzeHeapFailure_function_005F0F9C.md) (function, `0x005F0F9C`)
- `0x00790C80` → [RtlpHeapRemoveListEntry](../../text/5F/RtlpHeapRemoveListEntry_function_005F1B90.md) (function, `0x005F1B90`)
- `0x00790CC1` → [RtlpFindEntry](../../text/5F/RtlpFindEntry_function_005F17B4.md) (function, `0x005F17B4`)
- `0x00790D67` → [RtlpLogHeapFailure](../../text/35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x00790DBC` → [RtlpHeapAddListEntry](../../text/5F/RtlpHeapAddListEntry_function_005F18C8.md) (function, `0x005F18C8`)
- `0x00790E02` → [RtlpLogHeapFailure](../../text/35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x00790F74` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x00790B36` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00790BC0` → [RtlpAnalyzeHeapFailure](../../text/5F/RtlpAnalyzeHeapFailure_function_005F0F9C.md) (`PAGE` → `.text`)
  - `0x00790C80` → [RtlpHeapRemoveListEntry](../../text/5F/RtlpHeapRemoveListEntry_function_005F1B90.md) (`PAGE` → `.text`)
  - `0x00790CC1` → [RtlpFindEntry](../../text/5F/RtlpFindEntry_function_005F17B4.md) (`PAGE` → `.text`)
  - `0x00790D67` → [RtlpLogHeapFailure](../../text/35/RtlpLogHeapFailure_function_0035B7BC.md) (`PAGE` → `.text`)
  - `0x00790DBC` → [RtlpHeapAddListEntry](../../text/5F/RtlpHeapAddListEntry_function_005F18C8.md) (`PAGE` → `.text`)
  - `0x00790E02` → [RtlpLogHeapFailure](../../text/35/RtlpLogHeapFailure_function_0035B7BC.md) (`PAGE` → `.text`)
  - `0x00790F74` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00790AD0  40 53                           push rbx
00790AD2  56                              push rsi
00790AD3  57                              push rdi
00790AD4  41 54                           push r12
00790AD6  41 55                           push r13
00790AD8  41 56                           push r14
00790ADA  41 57                           push r15
00790ADC  48 81 EC B0 00 00 00            sub rsp, 0xb0
00790AE3  4C 8B F1                        mov r14, rcx
00790AE6  33 DB                           xor ebx, ebx
00790AE8  8B F3                           mov esi, ebx
00790AEA  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00790AEF  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00790AF4  88 5C 24 30                     mov byte ptr [rsp + 0x30], bl
00790AF8  81 79 10 EE DD EE DD            cmp dword ptr [rcx + 0x10], 0xddeeddee
00790AFF  75 16                           jne 0x140790b17
00790B01  33 C0                           xor eax, eax
00790B03  48 81 C4 B0 00 00 00            add rsp, 0xb0
00790B0A  41 5F                           pop r15
00790B0C  41 5E                           pop r14
00790B0E  41 5D                           pop r13
00790B10  41 5C                           pop r12
00790B12  5F                              pop rdi
00790B13  5E                              pop rsi
00790B14  5B                              pop rbx
00790B15  C3                              ret
00790B16  CC                              int3
00790B17  0B 51 74                        or edx, dword ptr [rcx + 0x74]
00790B1A  89 9C 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], ebx
00790B21  89 9C 24 00 01 00 00            mov dword ptr [rsp + 0x100], ebx
00790B28  F6 C2 01                        test dl, 1
00790B2B  75 13                           jne 0x140790b40
00790B2D  B2 01                           mov dl, 1
00790B2F  48 8B 89 60 01 00 00            mov rcx, qword ptr [rcx + 0x160]
00790B36  E8 E5 42 A8 FF                  call 0x140214e20
00790B3B  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
00790B40  49 8D 8E 20 01 00 00            lea rcx, [r14 + 0x120]
00790B47  48 8B 01                        mov rax, qword ptr [rcx]
00790B4A  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
00790B52  48 3B C1                        cmp rax, rcx
00790B55  0F 84 D4 03 00 00               je 0x140790f2f
00790B5B  4C 8B 78 28                     mov r15, qword ptr [rax + 0x28]
00790B5F  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
00790B64  4D 8D 66 7C                     lea r12, [r14 + 0x7c]
00790B68  4C 3B 78 30                     cmp r15, qword ptr [rax + 0x30]
00790B6C  0F 83 AE 03 00 00               jae 0x140790f20
00790B72  48 85 F6                        test rsi, rsi
00790B75  74 1C                           je 0x140790b93
00790B77  41 39 1C 24                     cmp dword ptr [r12], ebx
00790B7B  74 48                           je 0x140790bc5
00790B7D  8A 4E 0A                        mov cl, byte ptr [rsi + 0xa]
00790B80  32 4E 09                        xor cl, byte ptr [rsi + 9]
00790B83  32 4E 08                        xor cl, byte ptr [rsi + 8]
00790B86  88 4E 0B                        mov byte ptr [rsi + 0xb], cl
00790B89  41 8B 86 88 00 00 00            mov eax, dword ptr [r14 + 0x88]
00790B90  31 46 08                        xor dword ptr [rsi + 8], eax
00790B93  41 39 1C 24                     cmp dword ptr [r12], ebx
00790B97  74 2C                           je 0x140790bc5
00790B99  41 8B 8E 88 00 00 00            mov ecx, dword ptr [r14 + 0x88]
00790BA0  41 33 4F 08                     xor ecx, dword ptr [r15 + 8]
00790BA4  41 89 4F 08                     mov dword ptr [r15 + 8], ecx
00790BA8  41 8A 4F 0A                     mov cl, byte ptr [r15 + 0xa]
00790BAC  41 32 4F 09                     xor cl, byte ptr [r15 + 9]
00790BB0  41 32 4F 08                     xor cl, byte ptr [r15 + 8]
00790BB4  41 38 4F 0B                     cmp byte ptr [r15 + 0xb], cl
00790BB8  74 0B                           je 0x140790bc5
00790BBA  49 8B D7                        mov rdx, r15
00790BBD  49 8B CE                        mov rcx, r14
00790BC0  E8 D7 03 E6 FF                  call 0x1405f0f9c
00790BC5  49 8B F7                        mov rsi, r15
00790BC8  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
00790BCD  4D 8D 57 08                     lea r10, [r15 + 8]
00790BD1  4C 89 54 24 38                  mov qword ptr [rsp + 0x38], r10
00790BD6  41 0F B7 3A                     movzx edi, word ptr [r10]
00790BDA  8B D7                           mov edx, edi
00790BDC  48 C1 E2 04                     shl rdx, 4
00790BE0  41 8A 4F 0A                     mov cl, byte ptr [r15 + 0xa]
00790BE4  F6 C1 01                        test cl, 1
00790BE7  0F 85 08 03 00 00               jne 0x140790ef5
00790BED  4D 8B EF                        mov r13, r15
00790BF0  4C 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], r15
00790BF8  F6 C1 08                        test cl, 8
00790BFB  0F 84 1B 02 00 00               je 0x140790e1c
00790C01  49 8D 77 10                     lea rsi, [r15 + 0x10]
00790C05  48 8B 0E                        mov rcx, qword ptr [rsi]
00790C08  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00790C0D  4D 8B 47 18                     mov r8, qword ptr [r15 + 0x18]
00790C11  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
00790C16  49 8B 00                        mov rax, qword ptr [r8]
00790C19  4C 8B 49 08                     mov r9, qword ptr [rcx + 8]
00790C1D  49 3B C1                        cmp rax, r9
00790C20  0F 85 C7 01 00 00               jne 0x140790ded
00790C26  48 3B C6                        cmp rax, rsi
00790C29  0F 85 BE 01 00 00               jne 0x140790ded
00790C2F  49 8B 86 C0 00 00 00            mov rax, qword ptr [r14 + 0xc0]
00790C36  48 2B C7                        sub rax, rdi
00790C39  49 89 86 C0 00 00 00            mov qword ptr [r14 + 0xc0], rax
00790C40  49 8B 96 38 01 00 00            mov rdx, qword ptr [r14 + 0x138]
00790C47  48 85 D2                        test rdx, rdx
00790C4A  74 48                           je 0x140790c94
00790C4C  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00790C51  41 0F B7 0A                     movzx ecx, word ptr [r10]
00790C55  8B 7A 08                        mov edi, dword ptr [rdx + 8]
00790C58  48 3B CF                        cmp rcx, rdi
00790C5B  72 0B                           jb 0x140790c68
00790C5D  48 8B 02                        mov rax, qword ptr [rdx]
00790C60  48 85 C0                        test rax, rax
00790C63  75 6B                           jne 0x140790cd0
00790C65  8D 4F FF                        lea ecx, [rdi - 1]
00790C68  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
00790C6D  41 0F B7 02                     movzx eax, word ptr [r10]
00790C71  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00790C76  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00790C7A  4C 8B CE                        mov r9, rsi
00790C7D  49 8B CE                        mov rcx, r14
00790C80  E8 0B 0F E6 FF                  call 0x1405f1b90
00790C85  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00790C8A  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00790C8F  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
00790C94  49 89 08                        mov qword ptr [r8], rcx
00790C97  4C 89 41 08                     mov qword ptr [rcx + 8], r8
00790C9B  41 0F B7 0A                     movzx ecx, word ptr [r10]
00790C9F  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00790CA4  41 88 5F 0A                     mov byte ptr [r15 + 0xa], bl
00790CA8  41 88 5F 0F                     mov byte ptr [r15 + 0xf], bl
00790CAC  49 8D BE 50 01 00 00            lea rdi, [r14 + 0x150]
00790CB3  49 39 9E 38 01 00 00            cmp qword ptr [r14 + 0x138], rbx
00790CBA  74 19                           je 0x140790cd5
00790CBC  8B D1                           mov edx, ecx
00790CBE  49 8B CE                        mov rcx, r14
00790CC1  E8 EE 0A E6 FF                  call 0x1405f17b4
00790CC6  4C 8B C0                        mov r8, rax
00790CC9  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00790CCE  EB 08                           jmp 0x140790cd8
00790CD0  48 8B D0                        mov rdx, rax
00790CD3  EB 80                           jmp 0x140790c55
00790CD5  4C 8B 07                        mov r8, qword ptr [rdi]
00790CD8  49 3B F8                        cmp rdi, r8
00790CDB  74 5C                           je 0x140790d39
00790CDD  41 39 1C 24                     cmp dword ptr [r12], ebx
00790CE1  74 44                           je 0x140790d27
00790CE3  41 8B 40 F8                     mov eax, dword ptr [r8 - 8]
00790CE7  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
00790CEE  41 85 04 24                     test dword ptr [r12], eax
00790CF2  74 0E                           je 0x140790d02
00790CF4  41 33 86 88 00 00 00            xor eax, dword ptr [r14 + 0x88]
00790CFB  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
00790D02  0F B7 84 24 A0 00 00 00         movzx eax, word ptr [rsp + 0xa0]
00790D0A  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
00790D0F  4C 8B AC 24 80 00 00 00         mov r13, qword ptr [rsp + 0x80]
00790D17  8B 94 24 00 01 00 00            mov edx, dword ptr [rsp + 0x100]
00790D1E  89 94 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], edx
00790D25  EB 05                           jmp 0x140790d2c
00790D27  41 0F B7 40 F8                  movzx eax, word ptr [r8 - 8]
00790D2C  0F B7 C0                        movzx eax, ax
00790D2F  48 3B C8                        cmp rcx, rax
00790D32  76 05                           jbe 0x140790d39
00790D34  4D 8B 00                        mov r8, qword ptr [r8]
00790D37  EB 9F                           jmp 0x140790cd8
00790D39  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
00790D3D  48 8B 08                        mov rcx, qword ptr [rax]
00790D40  49 3B C8                        cmp rcx, r8
00790D43  75 10                           jne 0x140790d55
00790D45  4C 89 06                        mov qword ptr [rsi], r8
00790D48  48 89 46 08                     mov qword ptr [rsi + 8], rax
00790D4C  48 89 30                        mov qword ptr [rax], rsi
00790D4F  49 89 70 08                     mov qword ptr [r8 + 8], rsi
00790D53  EB 17                           jmp 0x140790d6c
00790D55  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00790D5A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00790D5F  45 33 C9                        xor r9d, r9d
00790D62  33 D2                           xor edx, edx
00790D64  8D 4A 0D                        lea ecx, [rdx + 0xd]
00790D67  E8 50 AA BC FF                  call 0x14035b7bc
00790D6C  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
00790D71  41 0F B7 00                     movzx eax, word ptr [r8]
00790D75  49 01 86 C0 00 00 00            add qword ptr [r14 + 0xc0], rax
00790D7C  49 8B 96 38 01 00 00            mov rdx, qword ptr [r14 + 0x138]
00790D83  48 85 D2                        test rdx, rdx
00790D86  74 39                           je 0x140790dc1
00790D88  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00790D8D  41 0F B7 08                     movzx ecx, word ptr [r8]
00790D91  8B 7A 08                        mov edi, dword ptr [rdx + 8]
00790D94  48 3B CF                        cmp rcx, rdi
00790D97  72 0B                           jb 0x140790da4
00790D99  48 8B 02                        mov rax, qword ptr [rdx]
00790D9C  48 85 C0                        test rax, rax
00790D9F  75 47                           jne 0x140790de8
00790DA1  8D 4F FF                        lea ecx, [rdi - 1]
00790DA4  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00790DA9  41 0F B7 00                     movzx eax, word ptr [r8]
00790DAD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00790DB2  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00790DB6  4C 8B CE                        mov r9, rsi
00790DB9  49 8B CE                        mov rcx, r14
00790DBC  E8 07 0B E6 FF                  call 0x1405f18c8
00790DC1  41 39 1C 24                     cmp dword ptr [r12], ebx
00790DC5  74 40                           je 0x140790e07
00790DC7  41 8A 4D 0A                     mov cl, byte ptr [r13 + 0xa]
00790DCB  41 32 4D 09                     xor cl, byte ptr [r13 + 9]
00790DCF  41 32 4D 08                     xor cl, byte ptr [r13 + 8]
00790DD3  41 88 4D 0B                     mov byte ptr [r13 + 0xb], cl
00790DD7  41 8B 8E 88 00 00 00            mov ecx, dword ptr [r14 + 0x88]
00790DDE  41 33 4D 08                     xor ecx, dword ptr [r13 + 8]
00790DE2  41 89 4D 08                     mov dword ptr [r13 + 8], ecx
00790DE6  EB 1F                           jmp 0x140790e07
00790DE8  48 8B D0                        mov rdx, rax
00790DEB  EB A4                           jmp 0x140790d91
00790DED  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00790DF2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00790DF7  4C 8B C6                        mov r8, rsi
00790DFA  49 8B D6                        mov rdx, r14
00790DFD  B9 0D 00 00 00                  mov ecx, 0xd
00790E02  E8 B5 A9 BC FF                  call 0x14035b7bc
00790E07  48 8B F3                        mov rsi, rbx
00790E0A  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00790E0F  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
00790E17  E9 4C FD FF FF                  jmp 0x140790b68
00790E1C  48 83 C2 E0                     add rdx, -0x20
00790E20  4D 8D 47 20                     lea r8, [r15 + 0x20]
00790E24  41 F6 46 70 40                  test byte ptr [r14 + 0x70], 0x40
00790E29  0F 95 C0                        setne al
00790E2C  C0 E9 02                        shr cl, 2
00790E2F  22 C1                           and al, cl
00790E31  A8 01                           test al, 1
00790E33  74 6D                           je 0x140790ea2
00790E35  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
00790E3A  4C 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], r8
00790E42  48 C1 EA 02                     shr rdx, 2
00790E46  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
00790E4B  48 85 D2                        test rdx, rdx
00790E4E  0F 84 A1 00 00 00               je 0x140790ef5
00790E54  41 F6 C0 04                     test r8b, 4
00790E58  74 22                           je 0x140790e7c
00790E5A  41 C7 00 EE FE EE FE            mov dword ptr [r8], 0xfeeefeee
00790E61  48 83 EA 01                     sub rdx, 1
00790E65  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
00790E6A  0F 84 85 00 00 00               je 0x140790ef5
00790E70  49 83 C0 04                     add r8, 4
00790E74  4C 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], r8
00790E7C  48 8B CA                        mov rcx, rdx
00790E7F  48 D1 E9                        shr rcx, 1
00790E82  48 B8 EE FE EE FE EE FE EE FE   movabs rax, 0xfeeefeeefeeefeee
00790E8C  49 8B F8                        mov rdi, r8
00790E8F  F3 48 AB                        rep stosq qword ptr [rdi], rax
00790E92  F6 C2 01                        test dl, 1
00790E95  74 5E                           je 0x140790ef5
00790E97  41 C7 44 90 FC EE FE EE FE      mov dword ptr [r8 + rdx*4 - 4], 0xfeeefeee
00790EA0  EB 53                           jmp 0x140790ef5
00790EA2  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
00790EA7  4C 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], r8
00790EAF  48 C1 EA 02                     shr rdx, 2
00790EB3  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
00790EB8  48 85 D2                        test rdx, rdx
00790EBB  74 38                           je 0x140790ef5
00790EBD  41 F6 C0 04                     test r8b, 4
00790EC1  74 1A                           je 0x140790edd
00790EC3  41 89 18                        mov dword ptr [r8], ebx
00790EC6  48 83 EA 01                     sub rdx, 1
00790ECA  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
00790ECF  74 24                           je 0x140790ef5
00790ED1  49 83 C0 04                     add r8, 4
00790ED5  4C 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], r8
00790EDD  48 8B CA                        mov rcx, rdx
00790EE0  48 D1 E9                        shr rcx, 1
00790EE3  49 8B F8                        mov rdi, r8
00790EE6  33 C0                           xor eax, eax
00790EE8  F3 48 AB                        rep stosq qword ptr [rdi], rax
00790EEB  F6 C2 01                        test dl, 1
00790EEE  74 05                           je 0x140790ef5
00790EF0  41 89 5C 90 FC                  mov dword ptr [r8 + rdx*4 - 4], ebx
00790EF5  41 80 7F 0F 03                  cmp byte ptr [r15 + 0xf], 3
00790EFA  75 16                           jne 0x140790f12
00790EFC  49 8D 4F 10                     lea rcx, [r15 + 0x10]
00790F00  4C 8D 79 30                     lea r15, [rcx + 0x30]
00790F04  4C 03 79 28                     add r15, qword ptr [rcx + 0x28]
00790F08  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
00790F0D  E9 FD FE FF FF                  jmp 0x140790e0f
00790F12  41 0F B7 47 08                  movzx eax, word ptr [r15 + 8]
00790F17  48 C1 E0 04                     shl rax, 4
00790F1B  4C 03 F8                        add r15, rax
00790F1E  EB E8                           jmp 0x140790f08
00790F20  48 8B 00                        mov rax, qword ptr [rax]
00790F23  49 8D 8E 20 01 00 00            lea rcx, [r14 + 0x120]
00790F2A  E9 1B FC FF FF                  jmp 0x140790b4a
00790F2F  8B BC 24 F0 00 00 00            mov edi, dword ptr [rsp + 0xf0]
00790F36  EB 0E                           jmp 0x140790f46
00790F38  8B F8                           mov edi, eax
00790F3A  33 DB                           xor ebx, ebx
00790F3C  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00790F41  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00790F46  48 85 F6                        test rsi, rsi
00790F49  74 1C                           je 0x140790f67
00790F4B  41 39 5E 7C                     cmp dword ptr [r14 + 0x7c], ebx
00790F4F  74 16                           je 0x140790f67
00790F51  8A 56 0A                        mov dl, byte ptr [rsi + 0xa]
00790F54  32 56 09                        xor dl, byte ptr [rsi + 9]
00790F57  32 56 08                        xor dl, byte ptr [rsi + 8]
00790F5A  88 56 0B                        mov byte ptr [rsi + 0xb], dl
00790F5D  41 8B 96 88 00 00 00            mov edx, dword ptr [r14 + 0x88]
00790F64  31 56 08                        xor dword ptr [rsi + 8], edx
00790F67  38 5C 24 30                     cmp byte ptr [rsp + 0x30], bl
00790F6B  74 0C                           je 0x140790f79
00790F6D  49 8B 8E 60 01 00 00            mov rcx, qword ptr [r14 + 0x160]
00790F74  E8 97 EA AC FF                  call 0x14025fa10
00790F79  8B C7                           mov eax, edi
00790F7B  E9 83 FB FF FF                  jmp 0x140790b03
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlZeroHeap(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int8 v_stack_mB8;
    unsigned int v_stack_p100;
    unsigned __int64 v_stack_p108;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned int v_stack_pA0;
    unsigned int v_stack_pF0;

    v_rsp = (v_rsp) - (176);
    v_rbx = 0;
    v_stack_mA8 = 0;
    v_stack_m98 = a1;
    v_stack_mB8 = 0;
    if ((*(unsigned int *)(a1 + 16)) != 0xDDEEDDEEULL) goto loc_00790B17;
    result = 0;
loc_00790B03:
    v_rsp = (v_rsp) + (176);
    return result;
loc_00790B17:
    a2 = (unsigned int)((a2) | (*(unsigned int *)(a1 + 116)));
    v_stack_pF0 = 0;
    v_stack_p100 = 0;
    if ((((unsigned __int8)(a2)) & (1)) == 0) {
        a2 = 1;
        a1 = *(unsigned __int64 *)(a1 + 352);
        result = ExAcquireResourceExclusiveLite(a1, a2, a3, a4);
        v_stack_p30 = 1;
    }
loc_00790B4A:
    v_stack_p108 = *(unsigned __int64 *)(a1 + 288);
    if ((*(unsigned __int64 *)(a1 + 288)) == (a1 + 288)) goto loc_00790F2F;
    v_stack_p48 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40);
loc_00790B68:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 48))) goto loc_00790F20;
    if (0 == 0) goto loc_00790B93;
    if ((*(unsigned int *)(a1 + 124)) == 0) goto loc_00790BC5;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(0 + 10)) ^ (*(unsigned __int8 *)(0 + 9)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(0 + 8)));
    *(unsigned __int8 *)(0 + 11) = (unsigned __int8)(a1);
loc_00790B93:
    if ((*(unsigned int *)(a1 + 124)) == 0) goto loc_00790BC5;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 136))) ^ (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 8)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 8) = (unsigned int)(a1);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 10)) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 9)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 8)));
    result = (unsigned int)(*(unsigned int *)(a1 + 136));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 11)) != ((unsigned __int8)(a1))) {
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40);
        a1 = a1;
        result = RtlpAnalyzeHeapFailure(a1, a2, a3, a4);
    }
    v_stack_p40 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40);
    v_stack_p38 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 8;
    a2 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 8)))) << (4);
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 10))) & (1)) != 0) goto loc_00790EF5;
    v_stack_p80 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40);
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 10))) & (8)) == 0) goto loc_00790E1C;
    v_stack_p78 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 16);
    v_stack_p58 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 24);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 24))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 16) + 8))) goto loc_00790DED;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 24))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 16)) goto loc_00790DED;
    result = (*(unsigned __int64 *)(a1 + 192)) - (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 8));
    *(unsigned __int64 *)(a1 + 192) = result;
    if (*(unsigned __int64 *)(a1 + 312) == 0) goto loc_00790C94;
    v_stack_p60 = 0;
loc_00790C55:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 8)) < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)))) goto loc_00790C68;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312)) != 0) goto loc_00790CD0;
loc_00790C68:
    v_stack_p60 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)) - 1;
    v_stack_p28 = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 8);
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)) - 1);
    result = RtlpHeapRemoveListEntry(a1, *(unsigned __int64 *)(a1 + 312), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 24), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 16);
loc_00790C94:
    *(unsigned __int64 *)(v_stack_p58) = v_stack_p78;
    *(unsigned __int64 *)(v_stack_p78 + 8) = v_stack_p58;
    v_stack_p58 = *(unsigned __int16 *)(v_stack_p38);
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 10) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 15) = 0;
    if ((*(unsigned __int64 *)(a1 + 312)) == 0) goto loc_00790CD5;
    result = RtlpFindEntry(a1, (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_p38))), v_stack_p58, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 16);
    goto loc_00790CD8;
loc_00790CD0:
    goto loc_00790C55;
loc_00790CD5:
loc_00790CD8:
    if ((a1 + 336) == (*(unsigned __int64 *)(a1 + 336))) goto loc_00790D39;
    if ((*(unsigned int *)(a1 + 124)) == 0) goto loc_00790D27;
    v_stack_pA0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8)));
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8));
    if (((*(unsigned int *)(a1 + 124)) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8))))) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 336) - 8))) ^ (*(unsigned int *)(a1 + 136)));
        v_stack_pA0 = (unsigned int)(result);
    }
    v_stack_pF0 = (unsigned int)((unsigned int)(v_stack_p100));
    goto loc_00790D2C;
loc_00790D27:
loc_00790D2C:
    if (v_stack_p58 <= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 336) - 8)))) goto loc_00790D39;
    goto loc_00790CD8;
loc_00790D39:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)))) goto loc_00790D55;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 16 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 16;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 16;
    goto loc_00790D6C;
loc_00790D55:
    v_stack_p28 = 0;
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)) + 8));
    a4 = 0;
    a2 = 0;
    result = RtlpLogHeapFailure(a2 + 13, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 336)), a4);
loc_00790D6C:
    if (*(unsigned __int64 *)(a1 + 312) == 0) goto loc_00790DC1;
    v_stack_p38 = 0;
loc_00790D91:
    if ((*(unsigned __int16 *)(v_stack_p38)) < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)))) goto loc_00790DA4;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312)) != 0) goto loc_00790DE8;
loc_00790DA4:
    v_stack_p38 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)) - 1;
    v_stack_p28 = *(unsigned __int16 *)(v_stack_p38);
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 312) + 8)) - 1);
    result = RtlpHeapAddListEntry(a1, *(unsigned __int64 *)(a1 + 312), v_stack_p38, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 16);
loc_00790DC1:
    if ((*(unsigned int *)(a1 + 124)) == 0) goto loc_00790E07;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p80 + 10)) ^ (*(unsigned __int8 *)(v_stack_p80 + 9)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(v_stack_p80 + 8)));
    *(unsigned __int8 *)(v_stack_p80 + 11) = (unsigned __int8)(a1);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 136))) ^ (*(unsigned int *)(v_stack_p80 + 8)));
    *(unsigned int *)(v_stack_p80 + 8) = (unsigned int)(a1);
    goto loc_00790E07;
loc_00790DE8:
    goto loc_00790D91;
loc_00790DED:
    v_stack_p28 = 0;
    v_stack_p20 = result;
    result = RtlpLogHeapFailure(13, a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 16, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 16);
loc_00790E07:
    v_stack_p40 = 0;
loc_00790E0F:
    goto loc_00790B68;
loc_00790E1C:
    a2 = (a1) + (-32);
    result = (((*(unsigned __int8 *)(a1 + 112)) & (64)) != 0) ? 1 : 0;
    a1 = (unsigned __int8)((13) >> (2));
    result = (unsigned __int8)((result) & ((unsigned __int8)(a1)));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00790EA2;
    v_stack_p68 = a2;
    v_stack_p88 = v_stack_p48 + 32;
    a2 = (a2) >> (2);
    v_stack_p68 = a2;
    if (a2 == 0) goto loc_00790EF5;
    if ((((unsigned __int8)(v_stack_p48 + 32)) & (4)) == 0) goto loc_00790E7C;
    *(unsigned int *)(v_stack_p48 + 32) = 0xFEEEFEEEULL;
    a2 = (a2) - (1);
    v_stack_p68 = a2;
    if (condition_is_equal) goto loc_00790EF5;
    a3 = (v_stack_p48 + 32) + (4);
    v_stack_p88 = a3;
loc_00790E7C:
    a1 = (a2) >> (1);
    if ((((unsigned __int8)(a2)) & (1)) == 0) goto loc_00790EF5;
    *(unsigned int *)(a3 + a2 * 4 - 4) = 0xFEEEFEEEULL;
    goto loc_00790EF5;
loc_00790EA2:
    v_stack_p70 = a2;
    v_stack_p90 = a3;
    a2 = (a2) >> (2);
    v_stack_p70 = a2;
    if (a2 == 0) goto loc_00790EF5;
    if ((((unsigned __int8)(a3)) & (4)) == 0) goto loc_00790EDD;
    *(unsigned int *)(a3) = 0;
    a2 = (a2) - (1);
    v_stack_p70 = a2;
    if (condition_is_equal) goto loc_00790EF5;
    a3 = (a3) + (4);
    v_stack_p90 = a3;
loc_00790EDD:
    a1 = (a2) >> (1);
    result = 0;
    if ((((unsigned __int8)(a2)) & (1)) != 0) {
        *(unsigned int *)(a3 + a2 * 4 - 4) = 0;
    }
    if ((*(unsigned __int8 *)(v_stack_p48 + 15)) != 3) goto loc_00790F12;
    v_r15 = (v_stack_p48 + 16 + 48) + (*(unsigned __int64 *)(v_stack_p48 + 16 + 40));
loc_00790F08:
    v_stack_p48 = v_r15;
    goto loc_00790E0F;
loc_00790F12:
    result = (*(unsigned __int16 *)(v_r15 + 8)) << (4);
    v_r15 = (v_r15) + (result);
    goto loc_00790F08;
loc_00790F20:
    goto loc_00790B4A;
loc_00790F2F:
    goto loc_00790F46;
loc_00790F46:
    if (0 == 0) goto loc_00790F67;
    if ((*(unsigned int *)(a1 + 124)) != 0) {
        a2 = *(unsigned __int8 *)(0 + 10);
        a2 = (unsigned __int8)((a2) ^ (*(unsigned __int8 *)(0 + 9)));
        a2 = (unsigned __int8)((a2) ^ (*(unsigned __int8 *)(0 + 8)));
        *(unsigned __int8 *)(0 + 11) = (unsigned __int8)(a2);
        a2 = *(unsigned int *)(a1 + 136);
    }
    result = *(unsigned __int64 *)(result);
    if (v_stack_p30 != 0) {
        a1 = *(unsigned __int64 *)(a1 + 352);
        result = ExReleaseResourceLite(a1, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 288) + 40) + 16);
    }
    goto loc_00790B03;
}
```

## 5. (Beta) C Style

```c
int64_t RtlZeroHeap(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint8_t v_stack_mB8;
    uint32_t v_stack_p100;
    uint64_t v_stack_p108;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint32_t v_stack_pA0;
    uint32_t v_stack_pF0;

    local_rsp = (local_rsp) - (176);
    local_rbx = 0;
    v_stack_mA8 = 0;
    v_stack_m98 = Arg1;
    v_stack_mB8 = 0;
    if ((*(uint32_t *)(arg1 + 0x10)) != 0xDDEEDDEEULL) goto loc_00790B17;
    result = 0;
loc_00790B03:
    local_rsp = (local_rsp) + (176);
    return result;
loc_00790B17:
    Arg2 = (uint32_t)((Arg2) | (*(uint32_t *)(arg1 + 0x74)));
    v_stack_pF0 = 0;
    v_stack_p100 = 0;
    if ((((uint8_t)(Arg2)) & (1)) == 0) {
        Arg2 = 1;
        Arg1 = *(uint64_t *)(arg1 + 0x160);
        result = ExAcquireResourceExclusiveLite(Arg1, Arg2, a3, a4);
        v_stack_p30 = 1;
    }
loc_00790B4A:
    v_stack_p108 = *(uint64_t *)(arg1 + 0x120);
    if ((*(uint64_t *)(arg1 + 0x120)) == (Arg1 + 288)) goto loc_00790F2F;
    v_stack_p48 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28);
loc_00790B68:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28)) >= (*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x30))) goto loc_00790F20;
    if (0 == 0) goto loc_00790B93;
    if ((*(uint32_t *)(arg1 + 0x7C)) == 0) goto loc_00790BC5;
    Arg1 = (uint8_t)((*(uint8_t *)(0 + 0xA)) ^ (*(uint8_t *)(0 + 0x9)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(0 + 0x8)));
    *(uint8_t *)(0 + 0xB) = (uint8_t)(Arg1);
loc_00790B93:
    if ((*(uint32_t *)(arg1 + 0x7C)) == 0) goto loc_00790BC5;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x88))) ^ (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x8)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x8) = (uint32_t)(Arg1);
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0xA)) ^ (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x9)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x8)));
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x88));
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0xB)) != ((uint8_t)(Arg1))) {
        Arg2 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28);
        Arg1 = Arg1;
        result = RtlpAnalyzeHeapFailure(Arg1, Arg2, a3, a4);
    }
    v_stack_p40 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28);
    v_stack_p38 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 8;
    Arg2 = ((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x8)))) << (4);
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0xA))) & (1)) != 0) goto loc_00790EF5;
    v_stack_p80 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28);
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0xA))) & (8)) == 0) goto loc_00790E1C;
    v_stack_p78 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x10);
    v_stack_p58 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x18);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x18))) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x10) + 0x8))) goto loc_00790DED;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x18))) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 16)) goto loc_00790DED;
    result = (*(uint64_t *)(arg1 + 0xC0)) - (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x8));
    *(uint64_t *)(arg1 + 0xC0) = result;
    if (*(uint64_t *)(arg1 + 0x138) == 0) goto loc_00790C94;
    v_stack_p60 = 0;
loc_00790C55:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x8)) < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)))) goto loc_00790C68;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x138)) != 0) goto loc_00790CD0;
loc_00790C68:
    v_stack_p60 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)) - 1;
    v_stack_p28 = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x8);
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)) - 1);
    result = RtlpHeapRemoveListEntry(Arg1, *(uint64_t *)(arg1 + 0x138), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x18), *(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 16);
loc_00790C94:
    *(uint64_t *)(v_stack_p58) = v_stack_p78;
    *(uint64_t *)(v_stack_p78 + 0x8) = v_stack_p58;
    v_stack_p58 = *(uint16_t *)(v_stack_p38);
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0xA) = 0;
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0xF) = 0;
    if ((*(uint64_t *)(arg1 + 0x138)) == 0) goto loc_00790CD5;
    result = RtlpFindEntry(Arg1, (uint32_t)((uint32_t)(*(uint16_t *)(v_stack_p38))), v_stack_p58, *(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 16);
    goto loc_00790CD8;
loc_00790CD0:
    goto loc_00790C55;
loc_00790CD5:
loc_00790CD8:
    if ((Arg1 + 336) == (*(uint64_t *)(arg1 + 0x150))) goto loc_00790D39;
    if ((*(uint32_t *)(arg1 + 0x7C)) == 0) goto loc_00790D27;
    v_stack_pA0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8)));
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8));
    if (((*(uint32_t *)(arg1 + 0x7C)) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8))))) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8))) ^ (*(uint32_t *)(arg1 + 0x88)));
        v_stack_pA0 = (uint32_t)(result);
    }
    v_stack_pF0 = (uint32_t)((uint32_t)(v_stack_p100));
    goto loc_00790D2C;
loc_00790D27:
loc_00790D2C:
    if (v_stack_p58 <= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x150) - 0x8)))) goto loc_00790D39;
    goto loc_00790CD8;
loc_00790D39:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)))) goto loc_00790D55;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x10) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x150));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 0x10 + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 16;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 16;
    goto loc_00790D6C;
loc_00790D55:
    v_stack_p28 = 0;
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x150)) + 0x8));
    a4 = 0;
    Arg2 = 0;
    result = RtlpLogHeapFailure(Arg2 + 13, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x150)), a4);
loc_00790D6C:
    if (*(uint64_t *)(arg1 + 0x138) == 0) goto loc_00790DC1;
    v_stack_p38 = 0;
loc_00790D91:
    if ((*(uint16_t *)(v_stack_p38)) < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)))) goto loc_00790DA4;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x138)) != 0) goto loc_00790DE8;
loc_00790DA4:
    v_stack_p38 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)) - 1;
    v_stack_p28 = *(uint16_t *)(v_stack_p38);
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x138) + 0x8)) - 1);
    result = RtlpHeapAddListEntry(Arg1, *(uint64_t *)(arg1 + 0x138), v_stack_p38, *(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 16);
loc_00790DC1:
    if ((*(uint32_t *)(arg1 + 0x7C)) == 0) goto loc_00790E07;
    Arg1 = (uint8_t)((*(uint8_t *)(v_stack_p80 + 0xA)) ^ (*(uint8_t *)(v_stack_p80 + 0x9)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(v_stack_p80 + 0x8)));
    *(uint8_t *)(v_stack_p80 + 0xB) = (uint8_t)(Arg1);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x88))) ^ (*(uint32_t *)(v_stack_p80 + 0x8)));
    *(uint32_t *)(v_stack_p80 + 0x8) = (uint32_t)(Arg1);
    goto loc_00790E07;
loc_00790DE8:
    goto loc_00790D91;
loc_00790DED:
    v_stack_p28 = 0;
    v_stack_p20 = result;
    result = RtlpLogHeapFailure(13, Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 16, *(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 16);
loc_00790E07:
    v_stack_p40 = 0;
loc_00790E0F:
    goto loc_00790B68;
loc_00790E1C:
    Arg2 = (Arg1) + (-32);
    result = (((*(uint8_t *)(arg1 + 0x70)) & (64)) != 0) ? 1 : 0;
    Arg1 = (uint8_t)((13) >> (2));
    result = (uint8_t)((result) & ((uint8_t)(Arg1)));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00790EA2;
    v_stack_p68 = Arg2;
    v_stack_p88 = v_stack_p48 + 32;
    Arg2 = (Arg2) >> (2);
    v_stack_p68 = Arg2;
    if (Arg2 == 0) goto loc_00790EF5;
    if ((((uint8_t)(v_stack_p48 + 32)) & (4)) == 0) goto loc_00790E7C;
    *(uint32_t *)(v_stack_p48 + 0x20) = 0xFEEEFEEEULL;
    Arg2 = (Arg2) - (1);
    v_stack_p68 = Arg2;
    if (condition_is_equal) goto loc_00790EF5;
    a3 = (v_stack_p48 + 32) + (4);
    v_stack_p88 = a3;
loc_00790E7C:
    Arg1 = (Arg2) >> (1);
    if ((((uint8_t)(Arg2)) & (1)) == 0) goto loc_00790EF5;
    *(uint32_t *)(a3 + Arg2 * 4 - 0x4) = 0xFEEEFEEEULL;
    goto loc_00790EF5;
loc_00790EA2:
    v_stack_p70 = Arg2;
    v_stack_p90 = a3;
    Arg2 = (Arg2) >> (2);
    v_stack_p70 = Arg2;
    if (Arg2 == 0) goto loc_00790EF5;
    if ((((uint8_t)(a3)) & (4)) == 0) goto loc_00790EDD;
    *(uint32_t *)(a3) = 0;
    Arg2 = (Arg2) - (1);
    v_stack_p70 = Arg2;
    if (condition_is_equal) goto loc_00790EF5;
    a3 = (a3) + (4);
    v_stack_p90 = a3;
loc_00790EDD:
    Arg1 = (Arg2) >> (1);
    result = 0;
    if ((((uint8_t)(Arg2)) & (1)) != 0) {
        *(uint32_t *)(a3 + Arg2 * 4 - 0x4) = 0;
    }
    if ((*(uint8_t *)(v_stack_p48 + 0xF)) != 3) goto loc_00790F12;
    local_r15 = (v_stack_p48 + 16 + 48) + (*(uint64_t *)(v_stack_p48 + 0x10 + 0x28));
loc_00790F08:
    v_stack_p48 = local_r15;
    goto loc_00790E0F;
loc_00790F12:
    result = (*(uint16_t *)(local_r15 + 0x8)) << (4);
    local_r15 = (local_r15) + (result);
    goto loc_00790F08;
loc_00790F20:
    goto loc_00790B4A;
loc_00790F2F:
    goto loc_00790F46;
loc_00790F46:
    if (0 == 0) goto loc_00790F67;
    if ((*(uint32_t *)(arg1 + 0x7C)) != 0) {
        Arg2 = *(uint8_t *)(0 + 0xA);
        Arg2 = (uint8_t)((Arg2) ^ (*(uint8_t *)(0 + 0x9)));
        Arg2 = (uint8_t)((Arg2) ^ (*(uint8_t *)(0 + 0x8)));
        *(uint8_t *)(0 + 0xB) = (uint8_t)(Arg2);
        Arg2 = *(uint32_t *)(arg1 + 0x88);
    }
    result = *(uint64_t *)(result);
    if (v_stack_p30 != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x160);
        result = ExReleaseResourceLite(Arg1, Arg2, a3, *(uint64_t *)(*(uint64_t *)(arg1 + 0x120) + 0x28) + 16);
    }
    goto loc_00790B03;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x70` | `8` | `R` |
| `Arg1` | `+ 0x74` | `32` | `R` |
| `Arg1` | `+ 0x7C` | `32` | `R` |
| `Arg1` | `+ 0x7C` | `64` | `R` |
| `Arg1` | `+ 0x88` | `32` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R/W` |
| `Arg1` | `+ 0xC0` | `64` | `W` |
| `Arg1` | `+ 0x120` | `64` | `R` |
| `Arg1` | `+ 0x138` | `64` | `R` |
| `Arg1` | `+ 0x150` | `64` | `R` |
| `Arg1` | `+ 0x160` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00790AD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
