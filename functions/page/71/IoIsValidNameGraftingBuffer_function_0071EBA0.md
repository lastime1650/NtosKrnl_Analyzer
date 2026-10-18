# IoIsValidNameGraftingBuffer

- RVA: `0x0071EBA0`–`0x0071EF65` (길이 `965` bytes)
- VA: `0x000000014071EBA0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C7694`
- 디코드: `234`개 명령, `965/965` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0071EC7F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0071ED04` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x0071ED44` → [ZwOpenSymbolicLinkObject](../../text/6A/ZwOpenSymbolicLinkObject_function_006AF7F0.md) (function, `0x006AF7F0`)
- `0x0071ED61` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0071ED72` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0071ED8E` → [ZwQuerySymbolicLinkObject](../../text/6A/ZwQuerySymbolicLinkObject_function_006AFE50.md) (function, `0x006AFE50`)
- `0x0071ED99` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0071EE41` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0071EE50` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0071EBBF` → RVA `0x00E0A740` (`.data`; read)
- `0x0071ECE3` → RVA `0x00AFCF60` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x0071EC7F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0071ED04` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x0071ED44` → [ZwOpenSymbolicLinkObject](../../text/6A/ZwOpenSymbolicLinkObject_function_006AF7F0.md) (`PAGE` → `.text`)
  - `0x0071ED61` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0071ED72` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0071ED8E` → [ZwQuerySymbolicLinkObject](../../text/6A/ZwQuerySymbolicLinkObject_function_006AFE50.md) (`PAGE` → `.text`)
  - `0x0071ED99` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0071EE41` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0071EE50` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0071EBA0  48 8B C4                        mov rax, rsp
0071EBA3  48 89 58 08                     mov qword ptr [rax + 8], rbx
0071EBA7  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0071EBAB  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
0071EBAF  55                              push rbp
0071EBB0  41 56                           push r14
0071EBB2  41 57                           push r15
0071EBB4  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0071EBB8  48 81 EC A0 00 00 00            sub rsp, 0xa0
0071EBBF  48 8B 05 7A BB 6E 00            mov rax, qword ptr [rip + 0x6ebb7a]
0071EBC6  48 33 C4                        xor rax, rsp
0071EBC9  48 89 45 3F                     mov qword ptr [rbp + 0x3f], rax
0071EBCD  48 8B 81 B8 00 00 00            mov rax, qword ptr [rcx + 0xb8]
0071EBD4  0F 57 C0                        xorps xmm0, xmm0
0071EBD7  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
0071EBDB  33 F6                           xor esi, esi
0071EBDD  48 8B FA                        mov rdi, rdx
0071EBE0  44 8B 40 08                     mov r8d, dword ptr [rax + 8]
0071EBE4  45 85 C0                        test r8d, r8d
0071EBE7  74 12                           je 0x14071ebfb
0071EBE9  0F B7 4A 0E                     movzx ecx, word ptr [rdx + 0xe]
0071EBED  0F B7 42 0A                     movzx eax, word ptr [rdx + 0xa]
0071EBF1  83 C1 14                        add ecx, 0x14
0071EBF4  03 C8                           add ecx, eax
0071EBF6  44 3B C1                        cmp r8d, ecx
0071EBF9  72 7B                           jb 0x14071ec76
0071EBFB  0F B7 42 0A                     movzx eax, word ptr [rdx + 0xa]
0071EBFF  66 41 BF 5C 00                  mov r15w, 0x5c
0071EC04  66 83 F8 06                     cmp ax, 6
0071EC08  76 1E                           jbe 0x14071ec28
0071EC0A  66 44 39 7A 10                  cmp word ptr [rdx + 0x10], r15w
0071EC0F  75 17                           jne 0x14071ec28
0071EC11  66 44 39 7A 12                  cmp word ptr [rdx + 0x12], r15w
0071EC16  75 10                           jne 0x14071ec28
0071EC18  0F B7 4A 14                     movzx ecx, word ptr [rdx + 0x14]
0071EC1C  66 83 F9 2E                     cmp cx, 0x2e
0071EC20  74 06                           je 0x14071ec28
0071EC22  66 83 F9 3F                     cmp cx, 0x3f
0071EC26  75 4E                           jne 0x14071ec76
0071EC28  66 83 F8 10                     cmp ax, 0x10
0071EC2C  76 74                           jbe 0x14071eca2
0071EC2E  66 44 39 7A 10                  cmp word ptr [rdx + 0x10], r15w
0071EC33  0F 85 1C 02 00 00               jne 0x14071ee55
0071EC39  66 83 7A 12 3F                  cmp word ptr [rdx + 0x12], 0x3f
0071EC3E  0F 85 11 02 00 00               jne 0x14071ee55
0071EC44  66 83 7A 14 3F                  cmp word ptr [rdx + 0x14], 0x3f
0071EC49  0F 85 06 02 00 00               jne 0x14071ee55
0071EC4F  66 44 39 7A 16                  cmp word ptr [rdx + 0x16], r15w
0071EC54  0F 85 FB 01 00 00               jne 0x14071ee55
0071EC5A  66 83 7A 18 55                  cmp word ptr [rdx + 0x18], 0x55
0071EC5F  75 77                           jne 0x14071ecd8
0071EC61  66 83 7A 1A 4E                  cmp word ptr [rdx + 0x1a], 0x4e
0071EC66  75 70                           jne 0x14071ecd8
0071EC68  66 83 7A 1C 43                  cmp word ptr [rdx + 0x1c], 0x43
0071EC6D  75 69                           jne 0x14071ecd8
0071EC6F  66 44 39 7A 1E                  cmp word ptr [rdx + 0x1e], r15w
0071EC74  75 62                           jne 0x14071ecd8
0071EC76  32 C0                           xor al, al
0071EC78  48 8B 4D 3F                     mov rcx, qword ptr [rbp + 0x3f]
0071EC7C  48 33 CC                        xor rcx, rsp
0071EC7F  E8 BC D9 F8 FF                  call 0x1406ac640
0071EC84  4C 8D 9C 24 A0 00 00 00         lea r11, [rsp + 0xa0]
0071EC8C  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
0071EC90  49 8B 73 28                     mov rsi, qword ptr [r11 + 0x28]
0071EC94  49 8B 7B 30                     mov rdi, qword ptr [r11 + 0x30]
0071EC98  49 8B E3                        mov rsp, r11
0071EC9B  41 5F                           pop r15
0071EC9D  41 5E                           pop r14
0071EC9F  5D                              pop rbp
0071ECA0  C3                              ret
0071ECA1  CC                              int3
0071ECA2  66 83 F8 0C                     cmp ax, 0xc
0071ECA6  0F 86 A9 01 00 00               jbe 0x14071ee55
0071ECAC  66 44 39 7A 10                  cmp word ptr [rdx + 0x10], r15w
0071ECB1  0F 85 9E 01 00 00               jne 0x14071ee55
0071ECB7  66 83 7A 12 3F                  cmp word ptr [rdx + 0x12], 0x3f
0071ECBC  0F 85 93 01 00 00               jne 0x14071ee55
0071ECC2  66 83 7A 14 3F                  cmp word ptr [rdx + 0x14], 0x3f
0071ECC7  0F 85 88 01 00 00               jne 0x14071ee55
0071ECCD  66 44 39 7A 16                  cmp word ptr [rdx + 0x16], r15w
0071ECD2  0F 85 7D 01 00 00               jne 0x14071ee55
0071ECD8  66 83 7A 1A 3A                  cmp word ptr [rdx + 0x1a], 0x3a
0071ECDD  0F 85 72 01 00 00               jne 0x14071ee55
0071ECE3  0F 10 05 76 E2 3D 00            movups xmm0, xmmword ptr [rip + 0x3de276]
0071ECEA  48 8D 55 1F                     lea rdx, [rbp + 0x1f]
0071ECEE  89 75 D3                        mov dword ptr [rbp - 0x2d], esi
0071ECF1  48 8D 4D DF                     lea rcx, [rbp - 0x21]
0071ECF5  89 75 F3                        mov dword ptr [rbp - 0xd], esi
0071ECF8  F3 0F 7F 45 1F                  movdqu xmmword ptr [rbp + 0x1f], xmm0
0071ECFD  89 75 0B                        mov dword ptr [rbp + 0xb], esi
0071ED00  48 89 75 C7                     mov qword ptr [rbp - 0x39], rsi
0071ED04  E8 77 BA D0 FF                  call 0x14042a780
0071ED09  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
0071ED0D  4C 8D 45 EF                     lea r8, [rbp - 0x11]
0071ED11  0F B7 4F 18                     movzx ecx, word ptr [rdi + 0x18]
0071ED15  0F 57 C0                        xorps xmm0, xmm0
0071ED18  BA 01 00 00 00                  mov edx, 1
0071ED1D  66 89 48 08                     mov word ptr [rax + 8], cx
0071ED21  48 8D 45 DF                     lea rax, [rbp - 0x21]
0071ED25  48 8D 4D C7                     lea rcx, [rbp - 0x39]
0071ED29  48 89 45 FF                     mov qword ptr [rbp - 1], rax
0071ED2D  C7 45 EF 30 00 00 00            mov dword ptr [rbp - 0x11], 0x30
0071ED34  48 89 75 F7                     mov qword ptr [rbp - 9], rsi
0071ED38  C7 45 07 40 02 00 00            mov dword ptr [rbp + 7], 0x240
0071ED3F  F3 0F 7F 45 0F                  movdqu xmmword ptr [rbp + 0xf], xmm0
0071ED44  E8 A7 0A F9 FF                  call 0x1406af7f0
0071ED49  85 C0                           test eax, eax
0071ED4B  0F 88 04 01 00 00               js 0x14071ee55
0071ED51  BA 08 02 00 00                  mov edx, 0x208
0071ED56  B9 40 00 00 00                  mov ecx, 0x40
0071ED5B  41 B8 49 6F 20 20               mov r8d, 0x20206f49
0071ED61  E8 8A 33 46 00                  call 0x140b820f0
0071ED66  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
0071ED6A  4C 8B F0                        mov r14, rax
0071ED6D  48 85 C0                        test rax, rax
0071ED70  75 0A                           jne 0x14071ed7c
0071ED72  E8 39 E5 F8 FF                  call 0x1406ad2b0
0071ED77  E9 FA FE FF FF                  jmp 0x14071ec76
0071ED7C  45 33 C0                        xor r8d, r8d
0071ED7F  4C 89 75 D7                     mov qword ptr [rbp - 0x29], r14
0071ED83  48 8D 55 CF                     lea rdx, [rbp - 0x31]
0071ED87  C7 45 CF 00 00 08 02            mov dword ptr [rbp - 0x31], 0x2080000
0071ED8E  E8 BD 10 F9 FF                  call 0x1406afe50
0071ED93  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
0071ED97  8B D8                           mov ebx, eax
0071ED99  E8 12 E5 F8 FF                  call 0x1406ad2b0
0071ED9E  85 DB                           test ebx, ebx
0071EDA0  0F 88 A5 00 00 00               js 0x14071ee4b
0071EDA6  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
0071EDAA  66 44 39 39                     cmp word ptr [rcx], r15w
0071EDAE  0F 85 97 00 00 00               jne 0x14071ee4b
0071EDB4  66 83 79 02 44                  cmp word ptr [rcx + 2], 0x44
0071EDB9  0F 85 8C 00 00 00               jne 0x14071ee4b
0071EDBF  66 83 79 04 65                  cmp word ptr [rcx + 4], 0x65
0071EDC4  0F 85 81 00 00 00               jne 0x14071ee4b
0071EDCA  66 83 79 06 76                  cmp word ptr [rcx + 6], 0x76
0071EDCF  75 7A                           jne 0x14071ee4b
0071EDD1  66 83 79 08 69                  cmp word ptr [rcx + 8], 0x69
0071EDD6  75 73                           jne 0x14071ee4b
0071EDD8  66 83 79 0A 63                  cmp word ptr [rcx + 0xa], 0x63
0071EDDD  75 6C                           jne 0x14071ee4b
0071EDDF  66 83 79 0C 65                  cmp word ptr [rcx + 0xc], 0x65
0071EDE4  75 65                           jne 0x14071ee4b
0071EDE6  66 44 39 79 0E                  cmp word ptr [rcx + 0xe], r15w
0071EDEB  75 5E                           jne 0x14071ee4b
0071EDED  66 83 79 10 4C                  cmp word ptr [rcx + 0x10], 0x4c
0071EDF2  75 57                           jne 0x14071ee4b
0071EDF4  66 83 79 12 61                  cmp word ptr [rcx + 0x12], 0x61
0071EDF9  75 50                           jne 0x14071ee4b
0071EDFB  66 83 79 14 6E                  cmp word ptr [rcx + 0x14], 0x6e
0071EE00  75 49                           jne 0x14071ee4b
0071EE02  66 83 79 1C 52                  cmp word ptr [rcx + 0x1c], 0x52
0071EE07  75 42                           jne 0x14071ee4b
0071EE09  66 83 79 1E 65                  cmp word ptr [rcx + 0x1e], 0x65
0071EE0E  75 3B                           jne 0x14071ee4b
0071EE10  66 83 79 20 64                  cmp word ptr [rcx + 0x20], 0x64
0071EE15  75 34                           jne 0x14071ee4b
0071EE17  66 83 79 22 69                  cmp word ptr [rcx + 0x22], 0x69
0071EE1C  75 2D                           jne 0x14071ee4b
0071EE1E  66 83 79 24 72                  cmp word ptr [rcx + 0x24], 0x72
0071EE23  75 26                           jne 0x14071ee4b
0071EE25  66 83 79 2E 72                  cmp word ptr [rcx + 0x2e], 0x72
0071EE2A  8B C6                           mov eax, esi
0071EE2C  0F 94 C0                        sete al
0071EE2F  66 44 39 79 30                  cmp word ptr [rcx + 0x30], r15w
0071EE34  40 0F 94 C6                     sete sil
0071EE38  85 C6                           test esi, eax
0071EE3A  74 0F                           je 0x14071ee4b
0071EE3C  33 D2                           xor edx, edx
0071EE3E  49 8B CE                        mov rcx, r14
0071EE41  E8 2A 3A 46 00                  call 0x140b82870
0071EE46  E9 2B FE FF FF                  jmp 0x14071ec76
0071EE4B  33 D2                           xor edx, edx
0071EE4D  49 8B CE                        mov rcx, r14
0071EE50  E8 1B 3A 46 00                  call 0x140b82870
0071EE55  0F B7 4F 0A                     movzx ecx, word ptr [rdi + 0xa]
0071EE59  66 83 F9 0C                     cmp cx, 0xc
0071EE5D  0F 82 13 FE FF FF               jb 0x14071ec76
0071EE63  0F B7 57 10                     movzx edx, word ptr [rdi + 0x10]
0071EE67  66 41 3B D7                     cmp dx, r15w
0071EE6B  75 23                           jne 0x14071ee90
0071EE6D  66 83 7F 12 3F                  cmp word ptr [rdi + 0x12], 0x3f
0071EE72  75 1C                           jne 0x14071ee90
0071EE74  66 83 7F 14 3F                  cmp word ptr [rdi + 0x14], 0x3f
0071EE79  75 15                           jne 0x14071ee90
0071EE7B  66 44 39 7F 16                  cmp word ptr [rdi + 0x16], r15w
0071EE80  75 0E                           jne 0x14071ee90
0071EE82  66 83 7F 1A 3A                  cmp word ptr [rdi + 0x1a], 0x3a
0071EE87  75 07                           jne 0x14071ee90
0071EE89  B0 01                           mov al, 1
0071EE8B  E9 E8 FD FF FF                  jmp 0x14071ec78
0071EE90  66 83 F9 60                     cmp cx, 0x60
0071EE94  74 15                           je 0x14071eeab
0071EE96  66 83 F9 62                     cmp cx, 0x62
0071EE9A  0F 85 D6 FD FF FF               jne 0x14071ec76
0071EEA0  66 44 39 7F 70                  cmp word ptr [rdi + 0x70], r15w
0071EEA5  0F 85 CB FD FF FF               jne 0x14071ec76
0071EEAB  66 41 3B D7                     cmp dx, r15w
0071EEAF  0F 85 C1 FD FF FF               jne 0x14071ec76
0071EEB5  0F B7 47 12                     movzx eax, word ptr [rdi + 0x12]
0071EEB9  66 83 F8 3F                     cmp ax, 0x3f
0071EEBD  74 0A                           je 0x14071eec9
0071EEBF  66 41 3B C7                     cmp ax, r15w
0071EEC3  0F 85 AD FD FF FF               jne 0x14071ec76
0071EEC9  66 83 7F 14 3F                  cmp word ptr [rdi + 0x14], 0x3f
0071EECE  0F 85 A2 FD FF FF               jne 0x14071ec76
0071EED4  66 44 39 7F 16                  cmp word ptr [rdi + 0x16], r15w
0071EED9  0F 85 97 FD FF FF               jne 0x14071ec76
0071EEDF  66 83 7F 18 56                  cmp word ptr [rdi + 0x18], 0x56
0071EEE4  0F 85 8C FD FF FF               jne 0x14071ec76
0071EEEA  66 83 7F 1A 6F                  cmp word ptr [rdi + 0x1a], 0x6f
0071EEEF  0F 85 81 FD FF FF               jne 0x14071ec76
0071EEF5  66 83 7F 1C 6C                  cmp word ptr [rdi + 0x1c], 0x6c
0071EEFA  0F 85 76 FD FF FF               jne 0x14071ec76
0071EF00  66 83 7F 1E 75                  cmp word ptr [rdi + 0x1e], 0x75
0071EF05  0F 85 6B FD FF FF               jne 0x14071ec76
0071EF0B  66 83 7F 20 6D                  cmp word ptr [rdi + 0x20], 0x6d
0071EF10  0F 85 60 FD FF FF               jne 0x14071ec76
0071EF16  66 83 7F 22 65                  cmp word ptr [rdi + 0x22], 0x65
0071EF1B  0F 85 55 FD FF FF               jne 0x14071ec76
0071EF21  66 83 7F 24 7B                  cmp word ptr [rdi + 0x24], 0x7b
0071EF26  0F 85 4A FD FF FF               jne 0x14071ec76
0071EF2C  66 B8 2D 00                     mov ax, 0x2d
0071EF30  66 39 47 36                     cmp word ptr [rdi + 0x36], ax
0071EF34  0F 85 3C FD FF FF               jne 0x14071ec76
0071EF3A  66 39 47 40                     cmp word ptr [rdi + 0x40], ax
0071EF3E  0F 85 32 FD FF FF               jne 0x14071ec76
0071EF44  66 39 47 4A                     cmp word ptr [rdi + 0x4a], ax
0071EF48  0F 85 28 FD FF FF               jne 0x14071ec76
0071EF4E  66 39 47 54                     cmp word ptr [rdi + 0x54], ax
0071EF52  0F 85 1E FD FF FF               jne 0x14071ec76
0071EF58  66 83 7F 6E 7D                  cmp word ptr [rdi + 0x6e], 0x7d
0071EF5D  0F 94 C0                        sete al
0071EF60  E9 13 FD FF FF                  jmp 0x14071ec78
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoIsValidNameGraftingBuffer(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 7256954)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 63) = result;
    *(unsigned __int64 *)(v_rsp - 95 - 33) = v_xmm0;
    v_rsi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 184) + 8))) == 0) goto loc_0071EBFB;
    a1 = (unsigned int)((*(unsigned __int16 *)(a2 + 14)) + (20));
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int16 *)(a2 + 10))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 184) + 8)))) < ((unsigned int)(a1))) goto loc_0071EC76;
loc_0071EBFB:
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 10))) <= 6) goto loc_0071EC28;
    if ((*(unsigned __int16 *)(a2 + 16)) != 92) goto loc_0071EC28;
    if ((*(unsigned __int16 *)(a2 + 18)) != 92) goto loc_0071EC28;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 20))) == 46) goto loc_0071EC28;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 20))) != 63) goto loc_0071EC76;
loc_0071EC28:
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 10))) <= 16) goto loc_0071ECA2;
    if ((*(unsigned __int16 *)(a2 + 16)) != 92) goto loc_0071EE55;
    if ((*(unsigned __int16 *)(a2 + 18)) != 63) goto loc_0071EE55;
    if ((*(unsigned __int16 *)(a2 + 20)) != 63) goto loc_0071EE55;
    if ((*(unsigned __int16 *)(a2 + 22)) != 92) goto loc_0071EE55;
    if ((*(unsigned __int16 *)(a2 + 24)) != 85) goto loc_0071ECD8;
    if ((*(unsigned __int16 *)(a2 + 26)) != 78) goto loc_0071ECD8;
    if ((*(unsigned __int16 *)(a2 + 28)) != 67) goto loc_0071ECD8;
    if ((*(unsigned __int16 *)(a2 + 30)) != 92) goto loc_0071ECD8;
loc_0071EC76:
    result = 0;
loc_0071EC78:
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 63)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 184) + 8)), a4);
    return result;
loc_0071ECA2:
    if (((unsigned __int16)(result)) <= 12) goto loc_0071EE55;
    if ((*(unsigned __int16 *)(a2 + 16)) != 92) goto loc_0071EE55;
    if ((*(unsigned __int16 *)(a2 + 18)) != 63) goto loc_0071EE55;
    if ((*(unsigned __int16 *)(a2 + 20)) != 63) goto loc_0071EE55;
    if ((*(unsigned __int16 *)(a2 + 22)) != 92) goto loc_0071EE55;
loc_0071ECD8:
    if ((*(unsigned __int16 *)(a2 + 26)) != 58) goto loc_0071EE55;
    *(unsigned int *)(v_rsp - 95 - 45) = (unsigned int)(*(unsigned __int64 *)(v_stack_m18 + 40));
    *(unsigned int *)(v_rsp - 95 - 13) = (unsigned int)(*(unsigned __int64 *)(v_stack_m18 + 40));
    *(unsigned __int64 *)(v_rsp - 95 + 31) = v_xmm0;
    *(unsigned int *)(v_rsp - 95 + 11) = (unsigned int)(*(unsigned __int64 *)(v_stack_m18 + 40));
    *(unsigned __int64 *)(v_rsp - 95 - 57) = *(unsigned __int64 *)(v_stack_m18 + 40);
    result = RtlInitUnicodeString(v_rsp - 95 - 33, v_rsp - 95 + 31, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 184) + 8)), a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 25) + 8) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 24));
    *(unsigned __int64 *)(v_rsp - 95 - 1) = v_rsp - 95 - 33;
    *(unsigned int *)(v_rsp - 95 - 17) = 48;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = *(unsigned __int64 *)(v_stack_m18 + 40);
    *(unsigned int *)(v_rsp - 95 + 7) = 576;
    *(unsigned __int64 *)(v_rsp - 95 + 15) = v_xmm0;
    result = ZwOpenSymbolicLinkObject(v_rsp - 95 - 57, 1, v_rsp - 95 - 17, a4);
    if (sign_flag) goto loc_0071EE55;
    result = ExAllocatePool2(64, 520, (unsigned int)(0x20206F49ULL), a4);
    if (result != 0) goto loc_0071ED7C;
    result = ZwClose(*(unsigned __int64 *)(v_rsp - 95 - 57), 520, (unsigned int)(0x20206F49ULL), a4);
    goto loc_0071EC76;
loc_0071ED7C:
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 41) = result;
    *(unsigned int *)(v_rsp - 95 - 49) = 0x2080000ULL;
    result = ZwQuerySymbolicLinkObject(*(unsigned __int64 *)(v_rsp - 95 - 57), v_rsp - 95 - 49, a3, a4);
    result = ZwClose(*(unsigned __int64 *)(v_rsp - 95 - 57), v_rsp - 95 - 49, a3, a4);
    if (sign_flag) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41))) != 92) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 2)) != 68) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 4)) != 101) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 6)) != 118) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 8)) != 105) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 10)) != 99) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 12)) != 101) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 14)) != 92) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 16)) != 76) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 18)) != 97) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 20)) != 110) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 28)) != 82) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 30)) != 101) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 32)) != 100) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 34)) != 105) goto loc_0071EE4B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 36)) != 114) goto loc_0071EE4B;
    result = ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 46)) == 114) ? 1 : 0;
    v_rsi = ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 95 - 41) + 48)) == 92) ? 1 : 0;
    if ((((unsigned int)(v_rsi)) & ((unsigned int)(result))) == 0) goto loc_0071EE4B;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    goto loc_0071EC76;
loc_0071EE4B:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
loc_0071EE55:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 10))) < 12) goto loc_0071EC76;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 16))) != 92) goto loc_0071EE90;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 18)) != 63) goto loc_0071EE90;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 20)) != 63) goto loc_0071EE90;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 22)) != 92) goto loc_0071EE90;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 26)) != 58) goto loc_0071EE90;
    goto loc_0071EC78;
loc_0071EE90:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 10))) == 96) goto loc_0071EEAB;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 10))) != 98) goto loc_0071EC76;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 112)) != 92) goto loc_0071EC76;
loc_0071EEAB:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 16))) != 92) goto loc_0071EC76;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 18))) == 63) goto loc_0071EEC9;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 18))) != 92) goto loc_0071EC76;
loc_0071EEC9:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 20)) != 63) goto loc_0071EC76;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 22)) != 92) goto loc_0071EC76;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 24)) != 86) goto loc_0071EC76;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 26)) != 111) goto loc_0071EC76;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 28)) != 108) goto loc_0071EC76;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 30)) != 117) goto loc_0071EC76;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 32)) != 109) goto loc_0071EC76;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 34)) != 101) goto loc_0071EC76;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 36)) != 123) goto loc_0071EC76;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 54)) != 45) goto loc_0071EC76;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 64)) != 45) goto loc_0071EC76;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 74)) != 45) goto loc_0071EC76;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 84)) != 45) goto loc_0071EC76;
    result = ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m18 + 48) + 110)) == 125) ? 1 : 0;
    goto loc_0071EC78;
}
```

## 5. (Beta) C Style

```c
int64_t IoIsValidNameGraftingBuffer(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x6EBB7A)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x3F) = result;
    *(uint64_t *)(local_rsp - 0x5F - 0x21) = v_xmm0;
    local_rsi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8))) == 0) goto loc_0071EBFB;
    Arg1 = (uint32_t)((*(uint16_t *)(arg2 + 0xE)) + (20));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint16_t *)(arg2 + 0xA))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8)))) < ((uint32_t)(Arg1))) goto loc_0071EC76;
loc_0071EBFB:
    if (((uint16_t)(*(uint16_t *)(arg2 + 0xA))) <= 6) goto loc_0071EC28;
    if ((*(uint16_t *)(arg2 + 0x10)) != 92) goto loc_0071EC28;
    if ((*(uint16_t *)(arg2 + 0x12)) != 92) goto loc_0071EC28;
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x14))) == 46) goto loc_0071EC28;
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x14))) != 63) goto loc_0071EC76;
loc_0071EC28:
    if (((uint16_t)(*(uint16_t *)(arg2 + 0xA))) <= 16) goto loc_0071ECA2;
    if ((*(uint16_t *)(arg2 + 0x10)) != 92) goto loc_0071EE55;
    if ((*(uint16_t *)(arg2 + 0x12)) != 63) goto loc_0071EE55;
    if ((*(uint16_t *)(arg2 + 0x14)) != 63) goto loc_0071EE55;
    if ((*(uint16_t *)(arg2 + 0x16)) != 92) goto loc_0071EE55;
    if ((*(uint16_t *)(arg2 + 0x18)) != 85) goto loc_0071ECD8;
    if ((*(uint16_t *)(arg2 + 0x1A)) != 78) goto loc_0071ECD8;
    if ((*(uint16_t *)(arg2 + 0x1C)) != 67) goto loc_0071ECD8;
    if ((*(uint16_t *)(arg2 + 0x1E)) != 92) goto loc_0071ECD8;
loc_0071EC76:
    result = 0;
loc_0071EC78:
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x3F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8)), a4);
    return result;
loc_0071ECA2:
    if (((uint16_t)(result)) <= 12) goto loc_0071EE55;
    if ((*(uint16_t *)(arg2 + 0x10)) != 92) goto loc_0071EE55;
    if ((*(uint16_t *)(arg2 + 0x12)) != 63) goto loc_0071EE55;
    if ((*(uint16_t *)(arg2 + 0x14)) != 63) goto loc_0071EE55;
    if ((*(uint16_t *)(arg2 + 0x16)) != 92) goto loc_0071EE55;
loc_0071ECD8:
    if ((*(uint16_t *)(arg2 + 0x1A)) != 58) goto loc_0071EE55;
    *(uint32_t *)(local_rsp - 0x5F - 0x2D) = (uint32_t)(*(uint64_t *)(v_stack_m18 + 0x28));
    *(uint32_t *)(local_rsp - 0x5F - 0xD) = (uint32_t)(*(uint64_t *)(v_stack_m18 + 0x28));
    *(uint64_t *)(local_rsp - 0x5F + 0x1F) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x5F + 0xB) = (uint32_t)(*(uint64_t *)(v_stack_m18 + 0x28));
    *(uint64_t *)(local_rsp - 0x5F - 0x39) = *(uint64_t *)(v_stack_m18 + 0x28);
    result = RtlInitUnicodeString(local_rsp - 95 - 33, local_rsp - 95 + 31, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8)), a4);
    *(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x19) + 0x8) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x18));
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = local_rsp - 95 - 33;
    *(uint32_t *)(local_rsp - 0x5F - 0x11) = 48;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = *(uint64_t *)(v_stack_m18 + 0x28);
    *(uint32_t *)(local_rsp - 0x5F + 0x7) = 576;
    *(uint64_t *)(local_rsp - 0x5F + 0xF) = v_xmm0;
    result = ZwOpenSymbolicLinkObject(local_rsp - 95 - 57, 1, local_rsp - 95 - 17, a4);
    if (sign_flag) goto loc_0071EE55;
    result = ExAllocatePool2(64, 520, (uint32_t)(0x20206F49ULL), a4);
    if (result != 0) goto loc_0071ED7C;
    result = ZwClose(*(uint64_t *)(local_rsp - 0x5F - 0x39), 520, (uint32_t)(0x20206F49ULL), a4);
    goto loc_0071EC76;
loc_0071ED7C:
    a3 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x29) = result;
    *(uint32_t *)(local_rsp - 0x5F - 0x31) = 0x2080000ULL;
    result = ZwQuerySymbolicLinkObject(*(uint64_t *)(local_rsp - 0x5F - 0x39), local_rsp - 95 - 49, a3, a4);
    result = ZwClose(*(uint64_t *)(local_rsp - 0x5F - 0x39), local_rsp - 95 - 49, a3, a4);
    if (sign_flag) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29))) != 92) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0x2)) != 68) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0x4)) != 101) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0x6)) != 118) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0x8)) != 105) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0xA)) != 99) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0xC)) != 101) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0xE)) != 92) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0x10)) != 76) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0x12)) != 97) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0x14)) != 110) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0x1C)) != 82) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0x1E)) != 101) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0x20)) != 100) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0x22)) != 105) goto loc_0071EE4B;
    if ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0x24)) != 114) goto loc_0071EE4B;
    result = ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0x2E)) == 114) ? 1 : 0;
    local_rsi = ((*(uint16_t *)(*(uint64_t *)(local_rsp - 0x5F - 0x29) + 0x30)) == 92) ? 1 : 0;
    if ((((uint32_t)(local_rsi)) & ((uint32_t)(result))) == 0) goto loc_0071EE4B;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, a3, a4);
    goto loc_0071EC76;
loc_0071EE4B:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, a3, a4);
loc_0071EE55:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0xA))) < 12) goto loc_0071EC76;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x10))) != 92) goto loc_0071EE90;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x12)) != 63) goto loc_0071EE90;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x14)) != 63) goto loc_0071EE90;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x16)) != 92) goto loc_0071EE90;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x1A)) != 58) goto loc_0071EE90;
    goto loc_0071EC78;
loc_0071EE90:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0xA))) == 96) goto loc_0071EEAB;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0xA))) != 98) goto loc_0071EC76;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x70)) != 92) goto loc_0071EC76;
loc_0071EEAB:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x10))) != 92) goto loc_0071EC76;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x12))) == 63) goto loc_0071EEC9;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x12))) != 92) goto loc_0071EC76;
loc_0071EEC9:
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x14)) != 63) goto loc_0071EC76;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x16)) != 92) goto loc_0071EC76;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x18)) != 86) goto loc_0071EC76;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x1A)) != 111) goto loc_0071EC76;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x1C)) != 108) goto loc_0071EC76;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x1E)) != 117) goto loc_0071EC76;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x20)) != 109) goto loc_0071EC76;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x22)) != 101) goto loc_0071EC76;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x24)) != 123) goto loc_0071EC76;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x36)) != 45) goto loc_0071EC76;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x40)) != 45) goto loc_0071EC76;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x4A)) != 45) goto loc_0071EC76;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x54)) != 45) goto loc_0071EC76;
    result = ((*(uint16_t *)(*(uint64_t *)(v_stack_m18 + 0x30) + 0x6E)) == 125) ? 1 : 0;
    goto loc_0071EC78;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg2` | `+ 0xA` | `16` | `R` |
| `Arg2` | `+ 0xE` | `16` | `R` |
| `Arg2` | `+ 0x10` | `16` | `R` |
| `Arg2` | `+ 0x12` | `16` | `R` |
| `Arg2` | `+ 0x14` | `16` | `R` |
| `Arg2` | `+ 0x16` | `16` | `R` |
| `Arg2` | `+ 0x18` | `16` | `R` |
| `Arg2` | `+ 0x1A` | `16` | `R` |
| `Arg2` | `+ 0x1C` | `16` | `R` |
| `Arg2` | `+ 0x1E` | `16` | `R` |
| `Arg2` | `+ 0x20` | `16` | `R` |
| `Arg2` | `+ 0x22` | `16` | `R` |
| `Arg2` | `+ 0x24` | `16` | `R` |
| `Arg2` | `+ 0x36` | `16` | `R` |
| `Arg2` | `+ 0x40` | `16` | `R` |
| `Arg2` | `+ 0x4A` | `16` | `R` |
| `Arg2` | `+ 0x54` | `16` | `R` |
| `Arg2` | `+ 0x6E` | `16` | `R` |
| `Arg2` | `+ 0x70` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0071EBA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
