# VrpPreOpenOrCreate

- RVA: `0x00932B84`–`0x009330AF` (길이 `1,323` bytes)
- VA: `0x0000000140932B84`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008EF1C`
- 디코드: `341`개 명령, `1,323/1,323` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00932BF3` → [EtwActivityIdControl](../../text/41/EtwActivityIdControl_function_0041E720.md) (function, `0x0041E720`)
- `0x00932C29` → [VrpBuildKeyPath](VrpBuildKeyPath_function_00934650.md) (function, `0x00934650`)
- `0x00932CB9` → [RtlEqualUnicodeString](RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x00932D24` → [RtlEqualUnicodeString](RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x00932D79` → [VrpTranslatePath](VrpTranslatePath_function_009330C0.md) (function, `0x009330C0`)
- `0x00932DBD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00932DFD` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00932E39` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00932E7B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00932EC6` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00932ED5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00932EE0` → [CmpFreeExtraParameter](../87/CmpFreeExtraParameter_function_00876894.md) (function, `0x00876894`)
- `0x00932EEC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00932EFD` → [CmAllocateExtraParameter](CmAllocateExtraParameter_function_009370D8.md) (function, `0x009370D8`)
- `0x00932F18` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00932F39` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00933009` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0093308E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [VrpRegistryCallback](../86/VrpRegistryCallback_function_00867450.md) at `0x00867519`

### Static image references
- `0x00932BA0` → RVA `0x00E0A740` (`.data`; read)
- `0x00932CAD` → RVA `0x000021F0` (`.rdata`; read)
- `0x00932D18` → RVA `0x00002200` (`.rdata`; read)
- `0x00932F6D` → RVA `0x00E0A630` (`.data`; read)
- `0x00932F7D` → RVA `0x00002F28` (`.rdata`; read)
- `0x00932F9B` → RVA `0x0005A940` (`.rdata`; read)
- `0x0093304D` → RVA `0x0005AC58` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x00932BF3` → [EtwActivityIdControl](../../text/41/EtwActivityIdControl_function_0041E720.md) (`PAGE` → `.text`)
  - `0x00932DBD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00932DFD` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00932E39` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00932E7B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00932EC6` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00932ED5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00932EEC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00932F18` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x00932F39` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00933009` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0093308E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00932FAA` → [sub_00B244E6](../B2/Unknown_function_00B244E6.md) (`tail-transfer`)
  - `0x00933064` → [sub_00B244E6](../B2/Unknown_function_00B244E6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00932B84  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00932B89  55                              push rbp
00932B8A  56                              push rsi
00932B8B  57                              push rdi
00932B8C  41 54                           push r12
00932B8E  41 55                           push r13
00932B90  41 56                           push r14
00932B92  41 57                           push r15
00932B94  48 8D 6C 24 D0                  lea rbp, [rsp - 0x30]
00932B99  48 81 EC 30 01 00 00            sub rsp, 0x130
00932BA0  48 8B 05 99 7B 4D 00            mov rax, qword ptr [rip + 0x4d7b99]
00932BA7  48 33 C4                        xor rax, rsp
00932BAA  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00932BAE  4C 8B 39                        mov r15, qword ptr [rcx]
00932BB1  33 F6                           xor esi, esi
00932BB3  0F 57 C0                        xorps xmm0, xmm0
00932BB6  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
00932BBA  4C 8B E2                        mov r12, rdx
00932BBD  89 74 24 68                     mov dword ptr [rsp + 0x68], esi
00932BC1  0F 57 C9                        xorps xmm1, xmm1
00932BC4  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
00932BC9  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00932BCD  48 8D 55 B8                     lea rdx, [rbp - 0x48]
00932BD1  49 8B 1F                        mov rbx, qword ptr [r15]
00932BD4  8D 4E 03                        lea ecx, [rsi + 3]
00932BD7  4D 8B 6F 58                     mov r13, qword ptr [r15 + 0x58]
00932BDB  44 8B F6                        mov r14d, esi
00932BDE  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00932BE2  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
00932BE7  0F 11 4D 88                     movups xmmword ptr [rbp - 0x78], xmm1
00932BEB  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
00932BEF  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
00932BF3  E8 28 BB AE FF                  call 0x14041e720
00932BF8  49 8B C5                        mov rax, r13
00932BFB  49 8D 4D 10                     lea rcx, [r13 + 0x10]
00932BFF  48 F7 D8                        neg rax
00932C02  4D 1B C9                        sbb r9, r9
00932C05  4C 23 C9                        and r9, rcx
00932C08  66 39 33                        cmp word ptr [rbx], si
00932C0B  0F 84 8B 02 00 00               je 0x140932e9c
00932C11  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00932C15  66 83 38 5C                     cmp word ptr [rax], 0x5c
00932C19  0F 85 7D 02 00 00               jne 0x140932e9c
00932C1F  33 C9                           xor ecx, ecx
00932C21  49 8B 17                        mov rdx, qword ptr [r15]
00932C24  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00932C29  E8 22 1A 00 00                  call 0x140934650
00932C2E  8B D8                           mov ebx, eax
00932C30  85 C0                           test eax, eax
00932C32  0F 88 70 04 00 00               js 0x1409330a8
00932C38  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00932C3D  0F B7 D6                        movzx edx, si
00932C40  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
00932C45  48 8B DE                        mov rbx, rsi
00932C48  0F B7 74 24 58                  movzx esi, word ptr [rsp + 0x58]
00932C4D  33 C0                           xor eax, eax
00932C4F  66 89 54 24 78                  mov word ptr [rsp + 0x78], dx
00932C54  48 85 F6                        test rsi, rsi
00932C57  74 0B                           je 0x140932c64
00932C59  66 83 3C 38 5C                  cmp word ptr [rax + rdi], 0x5c
00932C5E  0F 84 45 02 00 00               je 0x140932ea9
00932C64  48 8D 0C 1B                     lea rcx, [rbx + rbx]
00932C68  48 8D 04 39                     lea rax, [rcx + rdi]
00932C6C  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00932C70  48 3B CE                        cmp rcx, rsi
00932C73  73 20                           jae 0x140932c95
00932C75  B8 02 00 00 00                  mov eax, 2
00932C7A  66 83 3C 39 5C                  cmp word ptr [rcx + rdi], 0x5c
00932C7F  74 0F                           je 0x140932c90
00932C81  48 FF C3                        inc rbx
00932C84  66 03 D0                        add dx, ax
00932C87  48 8D 0C 1B                     lea rcx, [rbx + rbx]
00932C8B  48 3B CE                        cmp rcx, rsi
00932C8E  72 EA                           jb 0x140932c7a
00932C90  66 89 54 24 78                  mov word ptr [rsp + 0x78], dx
00932C95  48 8D 04 1B                     lea rax, [rbx + rbx]
00932C99  48 3B C6                        cmp rax, rsi
00932C9C  73 0C                           jae 0x140932caa
00932C9E  66 83 3C 38 5C                  cmp word ptr [rax + rdi], 0x5c
00932CA3  75 05                           jne 0x140932caa
00932CA5  48 FF C3                        inc rbx
00932CA8  EB EB                           jmp 0x140932c95
00932CAA  41 B0 01                        mov r8b, 1
00932CAD  48 8D 15 3C F5 6C FF            lea rdx, [rip - 0x930ac4]
00932CB4  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00932CB9  E8 62 FD FF FF                  call 0x140932a20
00932CBE  33 C9                           xor ecx, ecx
00932CC0  84 C0                           test al, al
00932CC2  0F 84 2E 02 00 00               je 0x140932ef6
00932CC8  0F B7 D1                        movzx edx, cx
00932CCB  66 89 4C 24 78                  mov word ptr [rsp + 0x78], cx
00932CD0  48 8D 04 1B                     lea rax, [rbx + rbx]
00932CD4  48 3B C6                        cmp rax, rsi
00932CD7  73 0B                           jae 0x140932ce4
00932CD9  66 83 3C 38 5C                  cmp word ptr [rax + rdi], 0x5c
00932CDE  0F 84 DA 01 00 00               je 0x140932ebe
00932CE4  48 8D 0C 1B                     lea rcx, [rbx + rbx]
00932CE8  48 8D 04 39                     lea rax, [rcx + rdi]
00932CEC  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00932CF0  48 3B CE                        cmp rcx, rsi
00932CF3  73 20                           jae 0x140932d15
00932CF5  B8 02 00 00 00                  mov eax, 2
00932CFA  66 83 3C 39 5C                  cmp word ptr [rcx + rdi], 0x5c
00932CFF  74 0F                           je 0x140932d10
00932D01  48 FF C3                        inc rbx
00932D04  66 03 D0                        add dx, ax
00932D07  48 8D 0C 1B                     lea rcx, [rbx + rbx]
00932D0B  48 3B CE                        cmp rcx, rsi
00932D0E  72 EA                           jb 0x140932cfa
00932D10  66 89 54 24 78                  mov word ptr [rsp + 0x78], dx
00932D15  41 B0 01                        mov r8b, 1
00932D18  48 8D 15 E1 F4 6C FF            lea rdx, [rip - 0x930b1f]
00932D1F  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00932D24  E8 F7 FC FF FF                  call 0x140932a20
00932D29  33 F6                           xor esi, esi
00932D2B  84 C0                           test al, al
00932D2D  0F 85 2F 02 00 00               jne 0x140932f62
00932D33  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00932D38  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
00932D3C  48 8B 75 A0                     mov rsi, qword ptr [rbp - 0x60]
00932D40  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
00932D45  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00932D4A  4D 8B C5                        mov r8, r13
00932D4D  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00932D52  48 8B D6                        mov rdx, rsi
00932D55  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00932D5A  49 8B CC                        mov rcx, r12
00932D5D  48 8D 45 A8                     lea rax, [rbp - 0x58]
00932D61  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00932D66  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00932D6B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00932D70  48 8D 45 88                     lea rax, [rbp - 0x78]
00932D74  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00932D79  E8 42 03 00 00                  call 0x1409330c0
00932D7E  8B D8                           mov ebx, eax
00932D80  3D 34 00 00 C0                  cmp eax, 0xc0000034
00932D85  0F 84 EB 02 00 00               je 0x140933076
00932D8B  85 C0                           test eax, eax
00932D8D  0F 88 11 03 00 00               js 0x1409330a4
00932D93  8B 5C 24 68                     mov ebx, dword ptr [rsp + 0x68]
00932D97  F6 C3 04                        test bl, 4
00932D9A  0F 85 5D 01 00 00               jne 0x140932efd
00932DA0  0F B7 4E 32                     movzx ecx, word ptr [rsi + 0x32]
00932DA4  BA 48 00 00 00                  mov edx, 0x48
00932DA9  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00932DAE  41 B8 56 52 65 67               mov r8d, 0x67655256
00932DB4  66 89 48 32                     mov word ptr [rax + 0x32], cx
00932DB8  B9 00 01 00 00                  mov ecx, 0x100
00932DBD  E8 2E F3 24 00                  call 0x140b820f0
00932DC2  48 8B F0                        mov rsi, rax
00932DC5  48 85 C0                        test rax, rax
00932DC8  0F 84 CA 02 00 00               je 0x140933098
00932DCE  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00932DD2  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00932DD7  0F 10 4C 24 58                  movups xmm1, xmmword ptr [rsp + 0x58]
00932DDC  48 89 06                        mov qword ptr [rsi], rax
00932DDF  33 D2                           xor edx, edx
00932DE1  49 8B 07                        mov rax, qword ptr [r15]
00932DE4  0F 10 00                        movups xmm0, xmmword ptr [rax]
00932DE7  F3 0F 7F 46 10                  movdqu xmmword ptr [rsi + 0x10], xmm0
00932DEC  49 8B 47 70                     mov rax, qword ptr [r15 + 0x70]
00932DF0  0F 10 00                        movups xmm0, xmmword ptr [rax]
00932DF3  F3 0F 7F 4E 30                  movdqu xmmword ptr [rsi + 0x30], xmm1
00932DF8  F3 0F 7F 46 20                  movdqu xmmword ptr [rsi + 0x20], xmm0
00932DFD  E8 7E 79 AF FF                  call 0x14042a780
00932E02  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00932E06  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00932E0A  0F 10 45 88                     movups xmm0, xmmword ptr [rbp - 0x78]
00932E0E  89 5E 40                        mov dword ptr [rsi + 0x40], ebx
00932E11  33 D2                           xor edx, edx
00932E13  48 8B 5D 98                     mov rbx, qword ptr [rbp - 0x68]
00932E17  89 43 08                        mov dword ptr [rbx + 8], eax
00932E1A  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00932E1F  4C 89 66 08                     mov qword ptr [rsi + 8], r12
00932E23  49 89 47 08                     mov qword ptr [r15 + 8], rax
00932E27  49 8B 07                        mov rax, qword ptr [r15]
00932E2A  49 89 77 50                     mov qword ptr [r15 + 0x50], rsi
00932E2E  33 F6                           xor esi, esi
00932E30  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
00932E35  F3 0F 7F 00                     movdqu xmmword ptr [rax], xmm0
00932E39  E8 42 79 AF FF                  call 0x14042a780
00932E3E  49 8B 47 70                     mov rax, qword ptr [r15 + 0x70]
00932E42  0F 10 45 A8                     movups xmm0, xmmword ptr [rbp - 0x58]
00932E46  F3 0F 7F 00                     movdqu xmmword ptr [rax], xmm0
00932E4A  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00932E4F  8B DE                           mov ebx, esi
00932E51  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00932E55  48 85 C9                        test rcx, rcx
00932E58  0F 85 89 00 00 00               jne 0x140932ee7
00932E5E  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00932E63  48 85 C9                        test rcx, rcx
00932E66  75 5E                           jne 0x140932ec6
00932E68  48 85 FF                        test rdi, rdi
00932E6B  75 60                           jne 0x140932ecd
00932E6D  4D 85 F6                        test r14, r14
00932E70  75 6A                           jne 0x140932edc
00932E72  8B C3                           mov eax, ebx
00932E74  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
00932E78  48 33 CC                        xor rcx, rsp
00932E7B  E8 C0 97 D7 FF                  call 0x1406ac640
00932E80  48 8B 9C 24 80 01 00 00         mov rbx, qword ptr [rsp + 0x180]
00932E88  48 81 C4 30 01 00 00            add rsp, 0x130
00932E8F  41 5F                           pop r15
00932E91  41 5E                           pop r14
00932E93  41 5D                           pop r13
00932E95  41 5C                           pop r12
00932E97  5F                              pop rdi
00932E98  5E                              pop rsi
00932E99  5D                              pop rbp
00932E9A  C3                              ret
00932E9B  CC                              int3
00932E9C  4D 85 ED                        test r13, r13
00932E9F  74 A9                           je 0x140932e4a
00932EA1  49 8B C9                        mov rcx, r9
00932EA4  E9 78 FD FF FF                  jmp 0x140932c21
00932EA9  48 FF C3                        inc rbx
00932EAC  48 8D 04 1B                     lea rax, [rbx + rbx]
00932EB0  48 3B C6                        cmp rax, rsi
00932EB3  0F 82 A0 FD FF FF               jb 0x140932c59
00932EB9  E9 A6 FD FF FF                  jmp 0x140932c64
00932EBE  48 FF C3                        inc rbx
00932EC1  E9 0A FE FF FF                  jmp 0x140932cd0
00932EC6  E8 85 64 9C FF                  call 0x1402f9350
00932ECB  EB 9B                           jmp 0x140932e68
00932ECD  BA 56 52 65 67                  mov edx, 0x67655256
00932ED2  48 8B CF                        mov rcx, rdi
00932ED5  E8 96 F9 24 00                  call 0x140b82870
00932EDA  EB 91                           jmp 0x140932e6d
00932EDC  49 8D 4E D0                     lea rcx, [r14 - 0x30]
00932EE0  E8 AF 39 F4 FF                  call 0x140876894
00932EE5  EB 8B                           jmp 0x140932e72
00932EE7  BA 56 52 65 67                  mov edx, 0x67655256
00932EEC  E8 7F F9 24 00                  call 0x140b82870
00932EF1  E9 68 FF FF FF                  jmp 0x140932e5e
00932EF6  33 F6                           xor esi, esi
00932EF8  E9 36 FE FF FF                  jmp 0x140932d33
00932EFD  E8 D6 41 00 00                  call 0x1409370d8
00932F02  33 F6                           xor esi, esi
00932F04  4C 8B F0                        mov r14, rax
00932F07  48 85 C0                        test rax, rax
00932F0A  0F 84 6F 01 00 00               je 0x14093307f
00932F10  BA 56 52 65 67                  mov edx, 0x67655256
00932F15  49 8B CC                        mov rcx, r12
00932F18  E8 F3 D7 8D FF                  call 0x140210710
00932F1D  0F 10 44 24 58                  movups xmm0, xmmword ptr [rsp + 0x58]
00932F22  83 E3 FB                        and ebx, 0xfffffffb
00932F25  4D 89 26                        mov qword ptr [r14], r12
00932F28  33 D2                           xor edx, edx
00932F2A  41 89 5E 08                     mov dword ptr [r14 + 8], ebx
00932F2E  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00932F33  F3 41 0F 7F 46 10               movdqu xmmword ptr [r14 + 0x10], xmm0
00932F39  E8 42 78 AF FF                  call 0x14042a780
00932F3E  48 8B 5D 98                     mov rbx, qword ptr [rbp - 0x68]
00932F42  4D 8D 46 D0                     lea r8, [r14 - 0x30]
00932F46  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
00932F4A  4C 8B 0A                        mov r9, qword ptr [rdx]
00932F4D  4C 3B CA                        cmp r9, rdx
00932F50  75 5D                           jne 0x140932faf
00932F52  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00932F56  48 39 10                        cmp qword ptr [rax], rdx
00932F59  74 7C                           je 0x140932fd7
00932F5B  B9 03 00 00 00                  mov ecx, 3
00932F60  CD 29                           int 0x29
00932F62  BB 22 00 00 C0                  mov ebx, 0xc0000022
00932F67  41 B8 02 00 00 00               mov r8d, 2
00932F6D  44 39 05 BC 76 4D 00            cmp dword ptr [rip + 0x4d76bc], r8d
00932F74  0F 86 D7 FE FF FF               jbe 0x140932e51
00932F7A  49 8B 07                        mov rax, qword ptr [r15]
00932F7D  48 8D 15 A4 FF 6C FF            lea rdx, [rip - 0x93005c]
00932F84  48 39 70 08                     cmp qword ptr [rax + 8], rsi
00932F88  48 0F 45 D0                     cmovne rdx, rax
00932F8C  0F B7 0A                        movzx ecx, word ptr [rdx]
00932F8F  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00932F93  48 8D 55 08                     lea rdx, [rbp + 8]
00932F97  48 89 55 F0                     mov qword ptr [rbp - 0x10], rdx
00932F9B  48 8D 15 9E 79 72 FF            lea rdx, [rip - 0x8d8662]
00932FA2  4C 89 45 F8                     mov qword ptr [rbp - 8], r8
00932FA6  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00932FAA  E9 37 15 1F 00                  jmp 0x140b244e6
00932FAF  49 8B 49 10                     mov rcx, qword ptr [r9 + 0x10]
00932FB3  49 2B 48 10                     sub rcx, qword ptr [r8 + 0x10]
00932FB7  75 08                           jne 0x140932fc1
00932FB9  49 8B 49 18                     mov rcx, qword ptr [r9 + 0x18]
00932FBD  49 2B 48 18                     sub rcx, qword ptr [r8 + 0x18]
00932FC1  48 85 C9                        test rcx, rcx
00932FC4  74 05                           je 0x140932fcb
00932FC6  4D 8B 09                        mov r9, qword ptr [r9]
00932FC9  EB 82                           jmp 0x140932f4d
00932FCB  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00932FD0  BB 35 00 00 C0                  mov ebx, 0xc0000035
00932FD5  EB 90                           jmp 0x140932f67
00932FD7  49 89 10                        mov qword ptr [r8], rdx
00932FDA  4C 8B F6                        mov r14, rsi
00932FDD  49 89 40 08                     mov qword ptr [r8 + 8], rax
00932FE1  4C 89 00                        mov qword ptr [rax], r8
00932FE4  4C 89 42 08                     mov qword ptr [rdx + 8], r8
00932FE8  49 8B 07                        mov rax, qword ptr [r15]
00932FEB  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00932FEF  48 85 C9                        test rcx, rcx
00932FF2  0F 85 91 00 00 00               jne 0x140933089
00932FF8  49 8B 07                        mov rax, qword ptr [r15]
00932FFB  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00932FFF  0F 10 45 88                     movups xmm0, xmmword ptr [rbp - 0x78]
00933003  33 D2                           xor edx, edx
00933005  F3 0F 7F 00                     movdqu xmmword ptr [rax], xmm0
00933009  E8 72 77 AF FF                  call 0x14042a780
0093300E  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00933013  C7 43 0C 68 03 00 00            mov dword ptr [rbx + 0xc], 0x368
0093301A  BB 03 05 00 C0                  mov ebx, 0xc0000503
0093301F  83 3D 0A 76 4D 00 05            cmp dword ptr [rip + 0x4d760a], 5
00933026  0F 86 25 FE FF FF               jbe 0x140932e51
0093302C  49 8B 07                        mov rax, qword ptr [r15]
0093302F  48 8D 15 F2 FE 6C FF            lea rdx, [rip - 0x93010e]
00933036  48 39 70 08                     cmp qword ptr [rax + 8], rsi
0093303A  48 0F 45 D0                     cmovne rdx, rax
0093303E  0F B7 0A                        movzx ecx, word ptr [rdx]
00933041  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00933045  48 8D 55 08                     lea rdx, [rbp + 8]
00933049  48 89 55 F0                     mov qword ptr [rbp - 0x10], rdx
0093304D  48 8D 15 04 7C 72 FF            lea rdx, [rip - 0x8d83fc]
00933054  48 C7 45 F8 02 00 00 00         mov qword ptr [rbp - 8], 2
0093305C  C7 44 24 50 03 05 00 C0         mov dword ptr [rsp + 0x50], 0xc0000503
00933064  E9 7D 14 1F 00                  jmp 0x140b244e6
00933069  81 FB 03 05 00 C0               cmp ebx, 0xc0000503
0093306F  74 AE                           je 0x14093301f
00933071  E9 F1 FE FF FF                  jmp 0x140932f67
00933076  33 F6                           xor esi, esi
00933078  8B DE                           mov ebx, esi
0093307A  E9 D2 FD FF FF                  jmp 0x140932e51
0093307F  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00933084  E9 DE FE FF FF                  jmp 0x140932f67
00933089  BA 56 52 65 67                  mov edx, 0x67655256
0093308E  E8 DD F7 24 00                  call 0x140b82870
00933093  E9 60 FF FF FF                  jmp 0x140932ff8
00933098  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0093309D  33 F6                           xor esi, esi
0093309F  E9 C3 FE FF FF                  jmp 0x140932f67
009330A4  33 F6                           xor esi, esi
009330A6  EB C1                           jmp 0x140933069
009330A8  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
009330AD  EB BA                           jmp 0x140933069
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VrpPreOpenOrCreate(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 5077913)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rsi = 0;
    v_stack_mD0 = a1;
    v_stack_m100 = 0;
    v_stack_mF8 = 0;
    v_stack_mC8 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8);
    v_stack_m110 = v_xmm0;
    v_stack_mE0 = v_xmm1;
    v_stack_mC0 = v_xmm0;
    v_stack_mB0 = v_xmm0;
    result = EtwActivityIdControl(v_rsi + 3, v_stack_mB0, a3, a4);
    result = -(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 88));
    a4 = (a4) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 88) + 16);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)))) == 0) goto loc_00932E9C;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 8))) != 92) goto loc_00932E9C;
    a1 = 0;
loc_00932C21:
    result = VrpBuildKeyPath(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1)), v_stack_m110, a4);
    if (sign_flag) goto loc_009330A8;
    v_stack_mF0 = 0;
    result = 0;
    v_stack_mF0 = 0;
    if (v_stack_m110 == 0) goto loc_00932C64;
loc_00932C59:
    if ((*(unsigned __int16 *)(result + v_stack_m108 * 1)) == 92) goto loc_00932EA9;
loc_00932C64:
    v_stack_mE8 = 0 + 0 * 1 + v_stack_m108 * 1;
    if ((0 + 0 * 1) >= v_stack_m110) goto loc_00932C95;
loc_00932C7A:
    if ((*(unsigned __int16 *)(0 + 0 * 1 + v_stack_m108 * 1)) == 92) goto loc_00932C90;
    v_rbx = (0) + 1;
    a2 = (unsigned __int16)((0) + (2));
    if ((v_rbx + v_rbx * 1) < v_stack_m110) goto loc_00932C7A;
loc_00932C90:
    v_stack_mF0 = (unsigned __int16)(a2);
loc_00932C95:
    if ((v_rbx + v_rbx * 1) >= v_stack_m110) goto loc_00932CAA;
    if ((*(unsigned __int16 *)(v_rbx + v_rbx * 1 + v_stack_m108 * 1)) != 92) goto loc_00932CAA;
    v_rbx = (v_rbx) + 1;
    goto loc_00932C95;
loc_00932CAA:
    result = RtlEqualUnicodeString(v_stack_mF0, v_rip - 9636548, 1, a4);
    a1 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00932EF6;
    v_stack_mF0 = 0;
loc_00932CD0:
    if ((v_rbx + v_rbx * 1) >= v_stack_m110) goto loc_00932CE4;
    if ((*(unsigned __int16 *)(v_rbx + v_rbx * 1 + v_stack_m108 * 1)) == 92) goto loc_00932EBE;
loc_00932CE4:
    v_stack_mE8 = v_rbx + v_rbx * 1 + v_stack_m108 * 1;
    if ((v_rbx + v_rbx * 1) >= v_stack_m110) goto loc_00932D15;
loc_00932CFA:
    if ((*(unsigned __int16 *)(v_rbx + v_rbx * 1 + v_stack_m108 * 1)) == 92) goto loc_00932D10;
    v_rbx = (v_rbx) + 1;
    a2 = (unsigned __int16)((0) + (2));
    if ((v_rbx + v_rbx * 1) < v_stack_m110) goto loc_00932CFA;
loc_00932D10:
    v_stack_mF0 = (unsigned __int16)(a2);
loc_00932D15:
    result = RtlEqualUnicodeString(v_stack_mF0, v_rip - 9636639, 1, a4);
    v_rsi = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00932F62;
loc_00932D33:
    v_stack_m118 = 0;
    v_stack_m128 = v_stack_m118;
    v_stack_m130 = v_stack_m100;
    v_stack_m138 = v_stack_mC0;
    v_stack_m140 = v_stack_mF8;
    v_stack_m148 = v_stack_mE0;
    result = VrpTranslatePath(a2, v_stack_mC8, *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 88), v_stack_m110);
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_00933076;
    if (sign_flag) goto loc_009330A4;
    if ((((unsigned __int8)((unsigned int)(v_stack_m100))) & (4)) != 0) goto loc_00932EFD;
    *(unsigned __int16 *)(v_stack_mF8 + 50) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_mC8 + 50));
    result = ExAllocatePool2(256, 72, (unsigned int)(0x67655256ULL), v_stack_m110);
    if (result == 0) goto loc_00933098;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8);
    a2 = 0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m110, a2, (unsigned int)(0x67655256ULL), v_stack_m110);
    *(unsigned int *)(result + 64) = (unsigned int)((unsigned int)(v_stack_m100));
    a2 = 0;
    *(unsigned int *)(v_stack_mD0 + 8) = (unsigned int)((unsigned int)(v_stack_m118));
    *(unsigned __int64 *)(result + 8) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) = v_stack_mF8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 80) = result;
    v_rsi = 0;
    v_stack_mF8 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1))) = v_xmm0;
    result = RtlInitUnicodeString(v_stack_mE0, a2, (unsigned int)(0x67655256ULL), v_stack_m110);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 112)) = v_xmm0;
loc_00932E4A:
loc_00932E51:
    if (v_stack_mD8 != 0) goto loc_00932EE7;
loc_00932E5E:
    if (v_stack_mF8 != 0) goto loc_00932EC6;
loc_00932E68:
    if (v_stack_m108 != 0) goto loc_00932ECD;
loc_00932E6D:
    if (0 != 0) goto loc_00932EDC;
loc_00932E72:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(0x67655256ULL), v_stack_m110);
    v_rsp = (v_rsp) + (304);
    return result;
loc_00932E9C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 88) == 0) goto loc_00932E4A;
    goto loc_00932C21;
loc_00932EA9:
    v_rbx = (v_stack_p18) + 1;
    if ((v_rbx + v_rbx * 1) < 0) goto loc_00932C59;
    goto loc_00932C64;
loc_00932EBE:
    v_rbx = (v_rbx) + 1;
    goto loc_00932CD0;
loc_00932EC6:
    result = ObfDereferenceObject(v_stack_m110, a2, (unsigned int)(0x67655256ULL), v_stack_m110);
    goto loc_00932E68;
loc_00932ECD:
    result = ExFreePoolWithTag(v_stack_m108, (unsigned int)(0x67655256ULL), (unsigned int)(0x67655256ULL), v_stack_m110);
    goto loc_00932E6D;
loc_00932EDC:
    result = CmpFreeExtraParameter(0 - 48, (unsigned int)(0x67655256ULL), (unsigned int)(0x67655256ULL), v_stack_m110);
    goto loc_00932E72;
loc_00932EE7:
    result = ExFreePoolWithTag(0 - 48, (unsigned int)(0x67655256ULL), (unsigned int)(0x67655256ULL), v_stack_m110);
    goto loc_00932E5E;
loc_00932EF6:
    v_rsi = 0;
    goto loc_00932D33;
loc_00932EFD:
    result = CmAllocateExtraParameter(0 - 48, (unsigned int)(0x67655256ULL), (unsigned int)(0x67655256ULL), v_stack_m110);
    v_rsi = 0;
    if (result == 0) goto loc_0093307F;
    result = ObfReferenceObjectWithTag(0, (unsigned int)(0x67655256ULL), (unsigned int)(0x67655256ULL), v_stack_m110);
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFBULL));
    *(unsigned __int64 *)(result) = 0;
    a2 = 0;
    *(unsigned int *)(result + 8) = (unsigned int)(v_rbx);
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    result = RtlInitUnicodeString(v_stack_p58, a2, (unsigned int)(0x67655256ULL), v_stack_m110);
loc_00932F4D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 16))) != (*(unsigned __int64 *)(v_stack_mD0 + 16))) goto loc_00932FAF;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 16) + 8))) == (*(unsigned __int64 *)(v_stack_mD0 + 16))) goto loc_00932FD7;
loc_00932F62:
loc_00932F67:
    if ((*(unsigned int *)(v_rip + 5076668)) <= 2) goto loc_00932E51;
    a2 = v_rip - 9633884;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 8)) != 0) { a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1)); }
    v_stack_m78 = v_stack_m60;
    v_stack_m70 = 2;
    v_stack_p50 = (unsigned int)((unsigned int)(0xC0000022ULL));
loc_00932FAF:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 16)) + 16)) - (*(unsigned __int64 *)(2 + 16));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 16)) + 24);
        a1 = (a1) - (*(unsigned __int64 *)(2 + 24));
    }
    if (a1 == 0) goto loc_00932FCB;
    goto loc_00932F4D;
loc_00932FCB:
    goto loc_00932F67;
loc_00932FD7:
    *(unsigned __int64 *)(2) = v_rip - 9274978;
    *(unsigned __int64 *)(2 + 8) = *(unsigned __int64 *)(a2 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)) = 2;
    *(unsigned __int64 *)(v_rip - 9274978 + 8) = 2;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 8) != 0) goto loc_00933089;
loc_00932FF8:
    a2 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1))) = v_xmm0;
    result = RtlInitUnicodeString(v_stack_mE0, a2, 2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 16))));
    *(unsigned int *)((unsigned int)(0xC0000035ULL) + 12) = 872;
loc_0093301F:
    if ((*(unsigned int *)(v_rip + 5076490)) <= 5) goto loc_00932E51;
    a2 = v_rip - 9634062;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 8)) != 0) { a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1)); }
    v_stack_m78 = v_stack_m60;
    v_stack_m70 = 2;
    v_stack_p50 = 0xC0000503ULL;
loc_00933069:
    if (((unsigned int)((unsigned int)(0xC0000503ULL))) == 0xC0000503ULL) goto loc_0093301F;
    goto loc_00932F67;
loc_00933076:
    v_rsi = 0;
    goto loc_00932E51;
loc_0093307F:
    goto loc_00932F67;
loc_00933089:
    result = ExFreePoolWithTag(*(unsigned __int16 *)(a2), (unsigned int)(0x67655256ULL), 2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 16))));
    goto loc_00932FF8;
loc_00933098:
    v_rsi = 0;
    goto loc_00932F67;
loc_009330A4:
    v_rsi = 0;
    goto loc_00933069;
loc_009330A8:
    goto loc_00933069;
}
```

## 5. (Beta) C Style

```c
int64_t VrpPreOpenOrCreate(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m48;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x4D7B99)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rsi = 0;
    v_stack_mD0 = Arg1;
    v_stack_m100 = 0;
    v_stack_mF8 = 0;
    v_stack_mC8 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x8);
    v_stack_m110 = v_xmm0;
    v_stack_mE0 = v_xmm1;
    v_stack_mC0 = v_xmm0;
    v_stack_mB0 = v_xmm0;
    result = EtwActivityIdControl(local_rsi + 3, v_stack_mB0, Arg3, Arg4);
    result = -(*(uint64_t *)(*(uint64_t *)(arg1) + 0x58));
    Arg4 = (Arg4) & (*(uint64_t *)(*(uint64_t *)(arg1) + 0x58) + 16);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1)))) == 0) goto loc_00932E9C;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1)) + 0x8))) != 92) goto loc_00932E9C;
    Arg1 = 0;
loc_00932C21:
    result = VrpBuildKeyPath(Arg1, *(uint64_t *)(*(uint64_t *)(arg1)), v_stack_m110, Arg4);
    if (sign_flag) goto loc_009330A8;
    v_stack_mF0 = 0;
    result = 0;
    v_stack_mF0 = 0;
    if (v_stack_m110 == 0) goto loc_00932C64;
loc_00932C59:
    if ((*(uint16_t *)(result + v_stack_m108 * 1)) == 92) goto loc_00932EA9;
loc_00932C64:
    v_stack_mE8 = 0 + 0 * 1 + v_stack_m108 * 1;
    if ((0 + 0 * 1) >= v_stack_m110) goto loc_00932C95;
loc_00932C7A:
    if ((*(uint16_t *)(0 + 0x0 * 1 + v_stack_m108 * 1)) == 92) goto loc_00932C90;
    local_rbx = (0) + 1;
    Arg2 = (uint16_t)((0) + (2));
    if ((local_rbx + local_rbx * 1) < v_stack_m110) goto loc_00932C7A;
loc_00932C90:
    v_stack_mF0 = (uint16_t)(Arg2);
loc_00932C95:
    if ((local_rbx + local_rbx * 1) >= v_stack_m110) goto loc_00932CAA;
    if ((*(uint16_t *)(local_rbx + local_rbx * 1 + v_stack_m108 * 1)) != 92) goto loc_00932CAA;
    local_rbx = (local_rbx) + 1;
    goto loc_00932C95;
loc_00932CAA:
    result = RtlEqualUnicodeString(v_stack_mF0, v_rip - 9636548, 1, Arg4);
    Arg1 = 0;
    if ((uint8_t)(result) == 0) goto loc_00932EF6;
    v_stack_mF0 = 0;
loc_00932CD0:
    if ((local_rbx + local_rbx * 1) >= v_stack_m110) goto loc_00932CE4;
    if ((*(uint16_t *)(local_rbx + local_rbx * 1 + v_stack_m108 * 1)) == 92) goto loc_00932EBE;
loc_00932CE4:
    v_stack_mE8 = local_rbx + local_rbx * 1 + v_stack_m108 * 1;
    if ((local_rbx + local_rbx * 1) >= v_stack_m110) goto loc_00932D15;
loc_00932CFA:
    if ((*(uint16_t *)(local_rbx + local_rbx * 1 + v_stack_m108 * 1)) == 92) goto loc_00932D10;
    local_rbx = (local_rbx) + 1;
    Arg2 = (uint16_t)((0) + (2));
    if ((local_rbx + local_rbx * 1) < v_stack_m110) goto loc_00932CFA;
loc_00932D10:
    v_stack_mF0 = (uint16_t)(Arg2);
loc_00932D15:
    result = RtlEqualUnicodeString(v_stack_mF0, v_rip - 9636639, 1, Arg4);
    local_rsi = 0;
    if ((uint8_t)(result) != 0) goto loc_00932F62;
loc_00932D33:
    v_stack_m118 = 0;
    v_stack_m128 = v_stack_m118;
    v_stack_m130 = v_stack_m100;
    v_stack_m138 = v_stack_mC0;
    v_stack_m140 = v_stack_mF8;
    v_stack_m148 = v_stack_mE0;
    result = VrpTranslatePath(Arg2, v_stack_mC8, *(uint64_t *)(*(uint64_t *)(arg1) + 0x58), v_stack_m110);
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_00933076;
    if (sign_flag) goto loc_009330A4;
    if ((((uint8_t)((uint32_t)(v_stack_m100))) & (4)) != 0) goto loc_00932EFD;
    *(uint16_t *)(v_stack_mF8 + 0x32) = (uint16_t)(*(uint16_t *)(v_stack_mC8 + 0x32));
    result = ExAllocatePool2(256, 72, (uint32_t)(0x67655256ULL), v_stack_m110);
    if (result == 0) goto loc_00933098;
    *(uint64_t *)(result) = *(uint64_t *)(*(uint64_t *)(arg1) + 0x8);
    Arg2 = 0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x30) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    result = RtlInitUnicodeString(v_stack_m110, Arg2, (uint32_t)(0x67655256ULL), v_stack_m110);
    *(uint32_t *)(result + 0x40) = (uint32_t)((uint32_t)(v_stack_m100));
    Arg2 = 0;
    *(uint32_t *)(v_stack_mD0 + 0x8) = (uint32_t)((uint32_t)(v_stack_m118));
    *(uint64_t *)(result + 0x8) = 0;
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x8) = v_stack_mF8;
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x50) = result;
    local_rsi = 0;
    v_stack_mF8 = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1))) = v_xmm0;
    result = RtlInitUnicodeString(v_stack_mE0, Arg2, (uint32_t)(0x67655256ULL), v_stack_m110);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x70)) = v_xmm0;
loc_00932E4A:
loc_00932E51:
    if (v_stack_mD8 != 0) goto loc_00932EE7;
loc_00932E5E:
    if (v_stack_mF8 != 0) goto loc_00932EC6;
loc_00932E68:
    if (v_stack_m108 != 0) goto loc_00932ECD;
loc_00932E6D:
    if (0 != 0) goto loc_00932EDC;
loc_00932E72:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(0x67655256ULL), v_stack_m110);
    local_rsp = (local_rsp) + (304);
    return result;
loc_00932E9C:
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0x58) == 0) goto loc_00932E4A;
    goto loc_00932C21;
loc_00932EA9:
    local_rbx = (v_stack_p18) + 1;
    if ((local_rbx + local_rbx * 1) < 0) goto loc_00932C59;
    goto loc_00932C64;
loc_00932EBE:
    local_rbx = (local_rbx) + 1;
    goto loc_00932CD0;
loc_00932EC6:
    result = ObfDereferenceObject(v_stack_m110, Arg2, (uint32_t)(0x67655256ULL), v_stack_m110);
    goto loc_00932E68;
loc_00932ECD:
    result = ExFreePoolWithTag(v_stack_m108, (uint32_t)(0x67655256ULL), (uint32_t)(0x67655256ULL), v_stack_m110);
    goto loc_00932E6D;
loc_00932EDC:
    result = CmpFreeExtraParameter(0 - 48, (uint32_t)(0x67655256ULL), (uint32_t)(0x67655256ULL), v_stack_m110);
    goto loc_00932E72;
loc_00932EE7:
    result = ExFreePoolWithTag(0 - 48, (uint32_t)(0x67655256ULL), (uint32_t)(0x67655256ULL), v_stack_m110);
    goto loc_00932E5E;
loc_00932EF6:
    local_rsi = 0;
    goto loc_00932D33;
loc_00932EFD:
    result = CmAllocateExtraParameter(0 - 48, (uint32_t)(0x67655256ULL), (uint32_t)(0x67655256ULL), v_stack_m110);
    local_rsi = 0;
    if (result == 0) goto loc_0093307F;
    result = ObfReferenceObjectWithTag(0, (uint32_t)(0x67655256ULL), (uint32_t)(0x67655256ULL), v_stack_m110);
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFBULL));
    *(uint64_t *)(result) = 0;
    Arg2 = 0;
    *(uint32_t *)(result + 0x8) = (uint32_t)(local_rbx);
    *(uint64_t *)(result + 0x10) = v_xmm0;
    result = RtlInitUnicodeString(v_stack_p58, Arg2, (uint32_t)(0x67655256ULL), v_stack_m110);
loc_00932F4D:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x10))) != (*(uint64_t *)(v_stack_mD0 + 0x10))) goto loc_00932FAF;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x10) + 0x8))) == (*(uint64_t *)(v_stack_mD0 + 0x10))) goto loc_00932FD7;
loc_00932F62:
loc_00932F67:
    if ((*(uint32_t *)(v_rip + 0x4D76BC)) <= 2) goto loc_00932E51;
    Arg2 = v_rip - 9633884;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1)) + 0x8)) != 0) { Arg2 = *(uint64_t *)(*(uint64_t *)(arg1)); }
    v_stack_m78 = v_stack_m60;
    v_stack_m70 = 2;
    v_stack_p50 = (uint32_t)((uint32_t)(0xC0000022ULL));
loc_00932FAF:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x10)) + 0x10)) - (*(uint64_t *)(2 + 0x10));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x10)) + 0x18);
        Arg1 = (Arg1) - (*(uint64_t *)(2 + 0x18));
    }
    if (Arg1 == NULL) goto loc_00932FCB;
    goto loc_00932F4D;
loc_00932FCB:
    goto loc_00932F67;
loc_00932FD7:
    *(uint64_t *)(2) = v_rip - 9274978;
    *(uint64_t *)(2 + 0x8) = *(uint64_t *)(Arg2 + 0x8);
    *(uint64_t *)(*(uint64_t *)(Arg2 + 0x8)) = 2;
    *(uint64_t *)(v_rip - 0x8D8662 + 0x8) = 2;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1)) + 0x8) != 0) goto loc_00933089;
loc_00932FF8:
    Arg2 = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1))) = v_xmm0;
    result = RtlInitUnicodeString(v_stack_mE0, Arg2, 2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x10))));
    *(uint32_t *)((uint32_t)(0xC0000035ULL) + 0xC) = 872;
loc_0093301F:
    if ((*(uint32_t *)(v_rip + 0x4D760A)) <= 5) goto loc_00932E51;
    Arg2 = v_rip - 9634062;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1)) + 0x8)) != 0) { Arg2 = *(uint64_t *)(*(uint64_t *)(arg1)); }
    v_stack_m78 = v_stack_m60;
    v_stack_m70 = 2;
    v_stack_p50 = 0xC0000503ULL;
loc_00933069:
    if (((uint32_t)((uint32_t)(0xC0000503ULL))) == 0xC0000503ULL) goto loc_0093301F;
    goto loc_00932F67;
loc_00933076:
    local_rsi = 0;
    goto loc_00932E51;
loc_0093307F:
    goto loc_00932F67;
loc_00933089:
    result = ExFreePoolWithTag(*(uint16_t *)(Arg2), (uint32_t)(0x67655256ULL), 2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x10))));
    goto loc_00932FF8;
loc_00933098:
    local_rsi = 0;
    goto loc_00932F67;
loc_009330A4:
    local_rsi = 0;
    goto loc_00933069;
loc_009330A8:
    goto loc_00933069;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00932B84&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
