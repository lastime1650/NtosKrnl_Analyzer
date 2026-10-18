# PiDevCfgResolveVariableFormatString

- RVA: `0x00735AB0`–`0x00735FC0` (길이 `1,296` bytes)
- VA: `0x0000000140735AB0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C8AC8`
- 디코드: `367`개 명령, `1,296/1,296` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00735B07` → [IopGetRegistryValue](../99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00735B1D` → [PnpValidateRegistryString](../../text/4B/PnpValidateRegistryString_function_004B763C.md) (function, `0x004B763C`)
- `0x00735B4C` → [IopGetRegistryValue](../99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00735BCB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00735BEC` → [PnpValidateRegistryMultiSz](../../text/4D/PnpValidateRegistryMultiSz_function_004DC170.md) (function, `0x004DC170`)
- `0x00735C1F` → [PiDevCfgResolveVariable](../A8/PiDevCfgResolveVariable_function_00A81AB8.md) (function, `0x00A81AB8`)
- `0x00735D3B` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (function, `0x00482D5C`)
- `0x00735D92` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00735E99` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (function, `0x00482D5C`)
- `0x00735EF6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00735F3C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00735F73` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00735F82` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00735F91` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00735F9F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00735ACA` → RVA `0x00E0A740` (`.data`; read)
- `0x00735AFD` → RVA `0x00AFF610` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00735B3B` → RVA `0x00AFF150` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00735D28` → RVA `0x00AFDAA0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x00735B1D` → [PnpValidateRegistryString](../../text/4B/PnpValidateRegistryString_function_004B763C.md) (`PAGE` → `.text`)
  - `0x00735BCB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00735BEC` → [PnpValidateRegistryMultiSz](../../text/4D/PnpValidateRegistryMultiSz_function_004DC170.md) (`PAGE` → `.text`)
  - `0x00735D3B` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (`PAGE` → `.text`)
  - `0x00735D92` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00735E99` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (`PAGE` → `.text`)
  - `0x00735EF6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00735F3C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00735F73` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00735F82` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00735F91` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00735F9F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00735AB0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00735AB5  55                              push rbp
00735AB6  56                              push rsi
00735AB7  57                              push rdi
00735AB8  41 54                           push r12
00735ABA  41 55                           push r13
00735ABC  41 56                           push r14
00735ABE  41 57                           push r15
00735AC0  48 8B EC                        mov rbp, rsp
00735AC3  48 81 EC 80 00 00 00            sub rsp, 0x80
00735ACA  48 8B 05 6F 4C 6D 00            mov rax, qword ptr [rip + 0x6d4c6f]
00735AD1  48 33 C4                        xor rax, rsp
00735AD4  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00735AD8  33 C0                           xor eax, eax
00735ADA  4C 89 45 D0                     mov qword ptr [rbp - 0x30], r8
00735ADE  48 8B F2                        mov rsi, rdx
00735AE1  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00735AE5  4C 8B E1                        mov r12, rcx
00735AE8  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00735AEC  48 8B CE                        mov rcx, rsi
00735AEF  89 45 A0                        mov dword ptr [rbp - 0x60], eax
00735AF2  4C 8D 4D B8                     lea r9, [rbp - 0x48]
00735AF6  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
00735AFA  45 33 C0                        xor r8d, r8d
00735AFD  48 8D 15 0C 9B 3C 00            lea rdx, [rip + 0x3c9b0c]
00735B04  44 8B F8                        mov r15d, eax
00735B07  E8 E0 35 26 00                  call 0x1409990ec
00735B0C  48 8B 5D B8                     mov rbx, qword ptr [rbp - 0x48]
00735B10  8B F8                           mov edi, eax
00735B12  85 C0                           test eax, eax
00735B14  0F 88 6D 04 00 00               js 0x140735f87
00735B1A  48 8B CB                        mov rcx, rbx
00735B1D  E8 1A 1B D8 FF                  call 0x1404b763c
00735B22  84 C0                           test al, al
00735B24  75 0A                           jne 0x140735b30
00735B26  BF 01 00 00 C0                  mov edi, 0xc0000001
00735B2B  E9 57 04 00 00                  jmp 0x140735f87
00735B30  44 8B 6B 08                     mov r13d, dword ptr [rbx + 8]
00735B34  4C 8D 4D C0                     lea r9, [rbp - 0x40]
00735B38  4C 03 EB                        add r13, rbx
00735B3B  48 8D 15 0E 96 3C 00            lea rdx, [rip + 0x3c960e]
00735B42  45 33 C0                        xor r8d, r8d
00735B45  4C 89 6D B0                     mov qword ptr [rbp - 0x50], r13
00735B49  48 8B CE                        mov rcx, rsi
00735B4C  E8 9B 35 26 00                  call 0x1409990ec
00735B51  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00735B55  45 33 D2                        xor r10d, r10d
00735B58  8B F8                           mov edi, eax
00735B5A  85 C0                           test eax, eax
00735B5C  0F 89 87 00 00 00               jns 0x140735be9
00735B62  3D 34 00 00 C0                  cmp eax, 0xc0000034
00735B67  0F 85 0B 04 00 00               jne 0x140735f78
00735B6D  41 8B FA                        mov edi, r10d
00735B70  48 85 F6                        test rsi, rsi
00735B73  0F 84 F6 00 00 00               je 0x140735c6f
00735B79  44 8B 76 08                     mov r14d, dword ptr [rsi + 8]
00735B7D  4C 03 F6                        add r14, rsi
00735B80  49 8B CE                        mov rcx, r14
00735B83  66 45 39 16                     cmp word ptr [r14], r10w
00735B87  0F 84 E2 00 00 00               je 0x140735c6f
00735B8D  41 FF C7                        inc r15d
00735B90  48 83 C8 FF                     or rax, 0xffffffffffffffff
00735B94  48 FF C0                        inc rax
00735B97  66 44 39 14 41                  cmp word ptr [rcx + rax*2], r10w
00735B9C  75 F6                           jne 0x140735b94
00735B9E  48 8D 0C 41                     lea rcx, [rcx + rax*2]
00735BA2  48 83 C1 02                     add rcx, 2
00735BA6  66 44 39 11                     cmp word ptr [rcx], r10w
00735BAA  75 E1                           jne 0x140735b8d
00735BAC  44 89 7D A0                     mov dword ptr [rbp - 0x60], r15d
00735BB0  45 85 FF                        test r15d, r15d
00735BB3  0F 84 B6 00 00 00               je 0x140735c6f
00735BB9  41 8B D7                        mov edx, r15d
00735BBC  B9 00 01 00 00                  mov ecx, 0x100
00735BC1  48 C1 E2 03                     shl rdx, 3
00735BC5  41 B8 50 70 64 63               mov r8d, 0x63647050
00735BCB  E8 20 C5 44 00                  call 0x140b820f0
00735BD0  45 33 D2                        xor r10d, r10d
00735BD3  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
00735BD7  48 8B D0                        mov rdx, rax
00735BDA  48 85 C0                        test rax, rax
00735BDD  75 24                           jne 0x140735c03
00735BDF  BF 9A 00 00 C0                  mov edi, 0xc000009a
00735BE4  E9 8F 03 00 00                  jmp 0x140735f78
00735BE9  48 8B CE                        mov rcx, rsi
00735BEC  E8 7F 65 DA FF                  call 0x1404dc170
00735BF1  84 C0                           test al, al
00735BF3  0F 85 77 FF FF FF               jne 0x140735b70
00735BF9  BF 01 00 00 C0                  mov edi, 0xc0000001
00735BFE  E9 75 03 00 00                  jmp 0x140735f78
00735C03  45 8B FA                        mov r15d, r10d
00735C06  66 45 39 16                     cmp word ptr [r14], r10w
00735C0A  74 57                           je 0x140735c63
00735C0C  44 3B 7D A0                     cmp r15d, dword ptr [rbp - 0x60]
00735C10  73 51                           jae 0x140735c63
00735C12  41 8B C7                        mov eax, r15d
00735C15  49 8B CC                        mov rcx, r12
00735C18  4C 8D 04 C2                     lea r8, [rdx + rax*8]
00735C1C  49 8B D6                        mov rdx, r14
00735C1F  E8 94 BE 34 00                  call 0x140a81ab8
00735C24  45 33 D2                        xor r10d, r10d
00735C27  8B F8                           mov edi, eax
00735C29  85 C0                           test eax, eax
00735C2B  78 1F                           js 0x140735c4c
00735C2D  48 83 C8 FF                     or rax, 0xffffffffffffffff
00735C31  48 FF C0                        inc rax
00735C34  66 45 39 14 46                  cmp word ptr [r14 + rax*2], r10w
00735C39  75 F6                           jne 0x140735c31
00735C3B  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
00735C3F  4D 8D 34 46                     lea r14, [r14 + rax*2]
00735C43  49 83 C6 02                     add r14, 2
00735C47  41 FF C7                        inc r15d
00735C4A  EB BA                           jmp 0x140735c06
00735C4C  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00735C50  3D 34 00 00 C0                  cmp eax, 0xc0000034
00735C55  0F 85 16 03 00 00               jne 0x140735f71
00735C5B  8D 78 CD                        lea edi, [rax - 0x33]
00735C5E  E9 0E 03 00 00                  jmp 0x140735f71
00735C63  85 FF                           test edi, edi
00735C65  0F 88 02 03 00 00               js 0x140735f6d
00735C6B  44 8B 7D A0                     mov r15d, dword ptr [rbp - 0x60]
00735C6F  41 0F B7 45 00                  movzx eax, word ptr [r13]
00735C74  45 8B E2                        mov r12d, r10d
00735C77  89 7D C8                        mov dword ptr [rbp - 0x38], edi
00735C7A  4D 8B F5                        mov r14, r13
00735C7D  B9 25 00 00 00                  mov ecx, 0x25
00735C82  66 85 C0                        test ax, ax
00735C85  0F 84 F5 00 00 00               je 0x140735d80
00735C8B  48 8B 7D A8                     mov rdi, qword ptr [rbp - 0x58]
00735C8F  49 83 C6 02                     add r14, 2
00735C93  66 3B C1                        cmp ax, cx
00735C96  75 0D                           jne 0x140735ca5
00735C98  41 0F B7 16                     movzx edx, word ptr [r14]
00735C9C  66 3B D1                        cmp dx, cx
00735C9F  75 0D                           jne 0x140735cae
00735CA1  49 83 C6 02                     add r14, 2
00735CA5  41 83 C4 02                     add r12d, 2
00735CA9  E9 BA 00 00 00                  jmp 0x140735d68
00735CAE  8D 42 D0                        lea eax, [rdx - 0x30]
00735CB1  66 83 F8 09                     cmp ax, 9
00735CB5  0F 87 AD 00 00 00               ja 0x140735d68
00735CBB  41 8B CA                        mov ecx, r10d
00735CBE  EB 1D                           jmp 0x140735cdd
00735CC0  8D 42 D0                        lea eax, [rdx - 0x30]
00735CC3  66 83 F8 09                     cmp ax, 9
00735CC7  77 19                           ja 0x140735ce2
00735CC9  0F B7 C2                        movzx eax, dx
00735CCC  8D 0C 89                        lea ecx, [rcx + rcx*4]
00735CCF  49 83 C6 02                     add r14, 2
00735CD3  8D 49 E8                        lea ecx, [rcx - 0x18]
00735CD6  8D 0C 48                        lea ecx, [rax + rcx*2]
00735CD9  41 0F B7 16                     movzx edx, word ptr [r14]
00735CDD  66 85 D2                        test dx, dx
00735CE0  75 DE                           jne 0x140735cc0
00735CE2  41 3B CF                        cmp ecx, r15d
00735CE5  73 7C                           jae 0x140735d63
00735CE7  0F AE E8                        lfence
00735CEA  8B C1                           mov eax, ecx
00735CEC  48 8B 14 C7                     mov rdx, qword ptr [rdi + rax*8]
00735CF0  48 85 D2                        test rdx, rdx
00735CF3  74 6E                           je 0x140735d63
00735CF5  8B 4A 20                        mov ecx, dword ptr [rdx + 0x20]
00735CF8  83 E9 01                        sub ecx, 1
00735CFB  74 5E                           je 0x140735d5b
00735CFD  83 E9 01                        sub ecx, 1
00735D00  74 59                           je 0x140735d5b
00735D02  83 E9 02                        sub ecx, 2
00735D05  74 1D                           je 0x140735d24
00735D07  83 F9 03                        cmp ecx, 3
00735D0A  75 57                           jne 0x140735d63
00735D0C  48 8B 4A 28                     mov rcx, qword ptr [rdx + 0x28]
00735D10  48 83 C8 FF                     or rax, 0xffffffffffffffff
00735D14  48 FF C0                        inc rax
00735D17  66 44 39 14 41                  cmp word ptr [rcx + rax*2], r10w
00735D1C  75 F6                           jne 0x140735d14
00735D1E  45 8D 24 44                     lea r12d, [r12 + rax*2]
00735D22  EB 3F                           jmp 0x140735d63
00735D24  4C 8B 4A 28                     mov r9, qword ptr [rdx + 0x28]
00735D28  4C 8D 05 71 7D 3C 00            lea r8, [rip + 0x3c7d71]
00735D2F  BA 0B 00 00 00                  mov edx, 0xb
00735D34  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00735D38  45 8B 09                        mov r9d, dword ptr [r9]
00735D3B  E8 1C D0 D4 FF                  call 0x140482d5c
00735D40  45 33 D2                        xor r10d, r10d
00735D43  85 C0                           test eax, eax
00735D45  78 1C                           js 0x140735d63
00735D47  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00735D4B  48 83 C8 FF                     or rax, 0xffffffffffffffff
00735D4F  48 FF C0                        inc rax
00735D52  66 44 39 14 41                  cmp word ptr [rcx + rax*2], r10w
00735D57  75 F6                           jne 0x140735d4f
00735D59  EB C3                           jmp 0x140735d1e
00735D5B  41 83 C4 FE                     add r12d, -2
00735D5F  44 03 62 24                     add r12d, dword ptr [rdx + 0x24]
00735D63  B9 25 00 00 00                  mov ecx, 0x25
00735D68  41 0F B7 06                     movzx eax, word ptr [r14]
00735D6C  66 85 C0                        test ax, ax
00735D6F  0F 85 1A FF FF FF               jne 0x140735c8f
00735D75  48 8B 5D B8                     mov rbx, qword ptr [rbp - 0x48]
00735D79  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00735D7D  8B 7D C8                        mov edi, dword ptr [rbp - 0x38]
00735D80  41 83 C4 02                     add r12d, 2
00735D84  B9 00 01 00 00                  mov ecx, 0x100
00735D89  41 8B D4                        mov edx, r12d
00735D8C  41 B8 50 70 64 63               mov r8d, 0x63647050
00735D92  E8 59 C3 44 00                  call 0x140b820f0
00735D97  45 33 D2                        xor r10d, r10d
00735D9A  4C 8B E8                        mov r13, rax
00735D9D  48 85 C0                        test rax, rax
00735DA0  75 0A                           jne 0x140735dac
00735DA2  BF 9A 00 00 C0                  mov edi, 0xc000009a
00735DA7  E9 9D 01 00 00                  jmp 0x140735f49
00735DAC  4D 8B FD                        mov r15, r13
00735DAF  45 8B F4                        mov r14d, r12d
00735DB2  4C 8B 45 B0                     mov r8, qword ptr [rbp - 0x50]
00735DB6  B9 25 00 00 00                  mov ecx, 0x25
00735DBB  41 0F B7 00                     movzx eax, word ptr [r8]
00735DBF  66 85 C0                        test ax, ax
00735DC2  0F 84 60 01 00 00               je 0x140735f28
00735DC8  66 3B C1                        cmp ax, cx
00735DCB  0F 85 3C 01 00 00               jne 0x140735f0d
00735DD1  49 83 C0 02                     add r8, 2
00735DD5  4C 89 45 B0                     mov qword ptr [rbp - 0x50], r8
00735DD9  41 0F B7 10                     movzx edx, word ptr [r8]
00735DDD  66 3B D1                        cmp dx, cx
00735DE0  75 13                           jne 0x140735df5
00735DE2  41 83 FE 02                     cmp r14d, 2
00735DE6  0F 86 46 01 00 00               jbe 0x140735f32
00735DEC  66 41 89 0F                     mov word ptr [r15], cx
00735DF0  E9 22 01 00 00                  jmp 0x140735f17
00735DF5  8D 42 D0                        lea eax, [rdx - 0x30]
00735DF8  66 83 F8 09                     cmp ax, 9
00735DFC  77 BD                           ja 0x140735dbb
00735DFE  41 8B CA                        mov ecx, r10d
00735E01  66 85 D2                        test dx, dx
00735E04  74 26                           je 0x140735e2c
00735E06  8D 42 D0                        lea eax, [rdx - 0x30]
00735E09  66 83 F8 09                     cmp ax, 9
00735E0D  77 19                           ja 0x140735e28
00735E0F  49 83 C0 02                     add r8, 2
00735E13  0F B7 C2                        movzx eax, dx
00735E16  8D 0C 89                        lea ecx, [rcx + rcx*4]
00735E19  8D 49 E8                        lea ecx, [rcx - 0x18]
00735E1C  41 0F B7 10                     movzx edx, word ptr [r8]
00735E20  8D 0C 48                        lea ecx, [rax + rcx*2]
00735E23  66 85 D2                        test dx, dx
00735E26  75 DE                           jne 0x140735e06
00735E28  4C 89 45 B0                     mov qword ptr [rbp - 0x50], r8
00735E2C  3B 4D A0                        cmp ecx, dword ptr [rbp - 0x60]
00735E2F  73 85                           jae 0x140735db6
00735E31  0F AE E8                        lfence
00735E34  8B C1                           mov eax, ecx
00735E36  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00735E3A  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
00735E3E  B9 25 00 00 00                  mov ecx, 0x25
00735E43  48 85 D2                        test rdx, rdx
00735E46  0F 84 6F FF FF FF               je 0x140735dbb
00735E4C  8B 4A 20                        mov ecx, dword ptr [rdx + 0x20]
00735E4F  83 E9 01                        sub ecx, 1
00735E52  74 77                           je 0x140735ecb
00735E54  83 E9 01                        sub ecx, 1
00735E57  74 72                           je 0x140735ecb
00735E59  83 E9 02                        sub ecx, 2
00735E5C  74 24                           je 0x140735e82
00735E5E  83 F9 03                        cmp ecx, 3
00735E61  B9 25 00 00 00                  mov ecx, 0x25
00735E66  0F 85 4F FF FF FF               jne 0x140735dbb
00735E6C  48 8B 4A 28                     mov rcx, qword ptr [rdx + 0x28]
00735E70  48 83 CE FF                     or rsi, 0xffffffffffffffff
00735E74  48 FF C6                        inc rsi
00735E77  66 44 39 14 71                  cmp word ptr [rcx + rsi*2], r10w
00735E7C  75 F6                           jne 0x140735e74
00735E7E  03 F6                           add esi, esi
00735E80  EB 53                           jmp 0x140735ed5
00735E82  4C 8B 4A 28                     mov r9, qword ptr [rdx + 0x28]
00735E86  4C 8D 05 13 7C 3C 00            lea r8, [rip + 0x3c7c13]
00735E8D  BA 0B 00 00 00                  mov edx, 0xb
00735E92  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00735E96  45 8B 09                        mov r9d, dword ptr [r9]
00735E99  E8 BE CE D4 FF                  call 0x140482d5c
00735E9E  4C 8B 45 B0                     mov r8, qword ptr [rbp - 0x50]
00735EA2  45 33 D2                        xor r10d, r10d
00735EA5  41 8D 4A 25                     lea ecx, [r10 + 0x25]
00735EA9  85 C0                           test eax, eax
00735EAB  0F 88 0A FF FF FF               js 0x140735dbb
00735EB1  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00735EB5  48 83 CE FF                     or rsi, 0xffffffffffffffff
00735EB9  48 8D 45 D8                     lea rax, [rbp - 0x28]
00735EBD  48 FF C6                        inc rsi
00735EC0  66 44 39 14 70                  cmp word ptr [rax + rsi*2], r10w
00735EC5  75 F6                           jne 0x140735ebd
00735EC7  03 F6                           add esi, esi
00735EC9  EB 13                           jmp 0x140735ede
00735ECB  8B 72 24                        mov esi, dword ptr [rdx + 0x24]
00735ECE  48 8B 4A 28                     mov rcx, qword ptr [rdx + 0x28]
00735ED2  83 EE 02                        sub esi, 2
00735ED5  48 85 C9                        test rcx, rcx
00735ED8  0F 84 D8 FE FF FF               je 0x140735db6
00735EDE  85 F6                           test esi, esi
00735EE0  0F 84 D0 FE FF FF               je 0x140735db6
00735EE6  44 3B F6                        cmp r14d, esi
00735EE9  76 47                           jbe 0x140735f32
00735EEB  48 8B D1                        mov rdx, rcx
00735EEE  44 8B C6                        mov r8d, esi
00735EF1  49 8B CF                        mov rcx, r15
00735EF4  8B DE                           mov ebx, esi
00735EF6  E8 45 09 F9 FF                  call 0x1406c6840
00735EFB  48 D1 EB                        shr rbx, 1
00735EFE  44 2B F6                        sub r14d, esi
00735F01  45 33 D2                        xor r10d, r10d
00735F04  4D 8D 3C 5F                     lea r15, [r15 + rbx*2]
00735F08  E9 A5 FE FF FF                  jmp 0x140735db2
00735F0D  41 83 FE 02                     cmp r14d, 2
00735F11  76 1F                           jbe 0x140735f32
00735F13  66 41 89 07                     mov word ptr [r15], ax
00735F17  49 83 C7 02                     add r15, 2
00735F1B  49 83 C0 02                     add r8, 2
00735F1F  41 83 C6 FE                     add r14d, -2
00735F23  E9 93 FE FF FF                  jmp 0x140735dbb
00735F28  85 FF                           test edi, edi
00735F2A  78 0B                           js 0x140735f37
00735F2C  41 83 FE 02                     cmp r14d, 2
00735F30  74 22                           je 0x140735f54
00735F32  BF 01 00 00 C0                  mov edi, 0xc0000001
00735F37  33 D2                           xor edx, edx
00735F39  49 8B CD                        mov rcx, r13
00735F3C  E8 2F C9 44 00                  call 0x140b82870
00735F41  48 8B 75 C0                     mov rsi, qword ptr [rbp - 0x40]
00735F45  48 8B 5D B8                     mov rbx, qword ptr [rbp - 0x48]
00735F49  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00735F4D  48 85 C9                        test rcx, rcx
00735F50  74 26                           je 0x140735f78
00735F52  EB 1D                           jmp 0x140735f71
00735F54  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00735F58  66 45 89 17                     mov word ptr [r15], r10w
00735F5C  C7 40 20 01 00 00 00            mov dword ptr [rax + 0x20], 1
00735F63  44 89 60 24                     mov dword ptr [rax + 0x24], r12d
00735F67  4C 89 68 28                     mov qword ptr [rax + 0x28], r13
00735F6B  EB D4                           jmp 0x140735f41
00735F6D  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00735F71  33 D2                           xor edx, edx
00735F73  E8 F8 C8 44 00                  call 0x140b82870
00735F78  48 85 F6                        test rsi, rsi
00735F7B  74 0A                           je 0x140735f87
00735F7D  33 D2                           xor edx, edx
00735F7F  48 8B CE                        mov rcx, rsi
00735F82  E8 E9 C8 44 00                  call 0x140b82870
00735F87  48 85 DB                        test rbx, rbx
00735F8A  74 0A                           je 0x140735f96
00735F8C  33 D2                           xor edx, edx
00735F8E  48 8B CB                        mov rcx, rbx
00735F91  E8 DA C8 44 00                  call 0x140b82870
00735F96  8B C7                           mov eax, edi
00735F98  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00735F9C  48 33 CC                        xor rcx, rsp
00735F9F  E8 9C 66 F7 FF                  call 0x1406ac640
00735FA4  48 8B 9C 24 D8 00 00 00         mov rbx, qword ptr [rsp + 0xd8]
00735FAC  48 81 C4 80 00 00 00            add rsp, 0x80
00735FB3  41 5F                           pop r15
00735FB5  41 5E                           pop r14
00735FB7  41 5D                           pop r13
00735FB9  41 5C                           pop r12
00735FBB  5F                              pop rdi
00735FBC  5E                              pop rsi
00735FBD  5D                              pop rbp
00735FBE  C3                              ret
00735FBF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgResolveVariableFormatString(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 7162991)) ^ (v_rsp);
    v_stack_m48 = result;
    result = 0;
    v_stack_m68 = a3;
    v_stack_m80 = 0;
    v_stack_m78 = 0;
    v_stack_m98 = 0;
    v_stack_m90 = 0;
    a3 = 0;
    result = IopGetRegistryValue(a2, v_rip + 3971852, a3, v_stack_m80);
    if (sign_flag) goto loc_00735F87;
    result = PnpValidateRegistryString(v_stack_m80, v_rip + 3971852, a3, v_stack_m80);
    if ((unsigned __int8)(result) != 0) goto loc_00735B30;
    goto loc_00735F87;
loc_00735B30:
    v_r13 = ((unsigned int)(*(unsigned int *)(v_stack_m80 + 8))) + (v_stack_m80);
    a3 = 0;
    v_stack_m88 = v_r13;
    result = IopGetRegistryValue(a2, v_rip + 3970574, a3, v_stack_m78);
    v_r10 = 0;
    if (!sign_flag) goto loc_00735BE9;
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00735F78;
loc_00735B70:
    if (v_stack_m78 == 0) goto loc_00735C6F;
    v_r14 = ((unsigned int)(*(unsigned int *)(v_stack_m78 + 8))) + (v_stack_m78);
    if ((*(unsigned __int16 *)(v_r14)) == 0) goto loc_00735C6F;
loc_00735B8D:
    v_r15 = (unsigned int)((0) + 1);
    result = (result) | (-1);
loc_00735B94:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_r14 + result * 2)) != 0) goto loc_00735B94;
    a1 = (v_r14 + result * 2) + (2);
    if ((*(unsigned __int16 *)(a1)) != 0) goto loc_00735B8D;
    v_stack_m98 = (unsigned int)(v_r15);
    if ((unsigned int)(v_r15) == 0) goto loc_00735C6F;
    a2 = ((unsigned int)((unsigned int)(v_r15))) << (3);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x63647050ULL), v_stack_m78);
    v_r10 = 0;
    v_stack_m90 = result;
    if (result != 0) goto loc_00735C03;
    goto loc_00735F78;
loc_00735BE9:
    result = PnpValidateRegistryMultiSz(v_stack_m78, result, (unsigned int)(0x63647050ULL), v_stack_m78);
    if ((unsigned __int8)(result) != 0) goto loc_00735B70;
    goto loc_00735F78;
loc_00735C03:
loc_00735C06:
    if ((*(unsigned __int16 *)(v_r14)) == 0) goto loc_00735C63;
    if (0 >= v_stack_m98) goto loc_00735C63;
    result = PiDevCfgResolveVariable(a1, v_r14, result + 0 * 8, v_stack_m78);
    v_r10 = 0;
    if (sign_flag) goto loc_00735C4C;
    result = (result) | (-1);
loc_00735C31:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_r14 + result * 2)) != 0) goto loc_00735C31;
    v_r14 = (v_r14 + result * 2) + (2);
    v_r15 = (unsigned int)((0) + 1);
    goto loc_00735C06;
loc_00735C4C:
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00735F71;
    goto loc_00735F71;
loc_00735C63:
    if (sign_flag) goto loc_00735F6D;
loc_00735C6F:
    v_stack_m70 = (unsigned int)(result - 51);
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r13)) == 0) goto loc_00735D80;
loc_00735C8F:
    v_r14 = (v_r13) + (2);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r13))) != 37) goto loc_00735CA5;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14))) != 37) goto loc_00735CAE;
    v_r14 = (v_r14) + (2);
loc_00735CA5:
    v_r12 = (unsigned int)((0) + (2));
    goto loc_00735D68;
loc_00735CAE:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14) - 48)) > 9) goto loc_00735D68;
    goto loc_00735CDD;
loc_00735CC0:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14) - 48)) > 9) goto loc_00735CE2;
    v_r14 = (v_r14) + (2);
loc_00735CDD:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r14)) != 0) goto loc_00735CC0;
loc_00735CE2:
    if (((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_r14)) + 0 + 0 * 4 - 24 * 2)) >= ((unsigned int)((unsigned int)(v_stack_m98)))) goto loc_00735D63;
    if (*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_r14)) + 0 + 0 * 4 - 24 * 2)) * 8) == 0) goto loc_00735D63;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_r14)) + 0 + 0 * 4 - 24 * 2)) * 8) + 32))) - (1));
    if (condition_is_equal) goto loc_00735D5B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00735D5B;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00735D24;
    if (((unsigned int)(a1)) != 3) goto loc_00735D63;
    result = ((unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_r14)) + 0 + 0 * 4 - 24 * 2))) | (-1);
loc_00735D14:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_r14)) + 0 + 0 * 4 - 24 * 2)) * 8) + 40) + result * 2)) != 0) goto loc_00735D14;
loc_00735D1E:
    goto loc_00735D63;
loc_00735D24:
    result = RtlStringCchPrintfW(v_stack_m60, 11, v_rip + 3964273, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_r14)) + 0 + 0 * 4 - 24 * 2)) * 8) + 40))));
    v_r10 = 0;
    if (sign_flag) goto loc_00735D63;
    result = (result) | (-1);
loc_00735D4F:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_stack_m60 + result * 2)) != 0) goto loc_00735D4F;
    goto loc_00735D1E;
loc_00735D5B:
    v_r12 = (unsigned int)((v_r12 + result * 2) + (-2));
    v_r12 = (unsigned int)((v_r12) + (*(unsigned int *)(11 + 36)));
loc_00735D63:
loc_00735D68:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r14)) != 0) goto loc_00735C8F;
loc_00735D80:
    v_r12 = (unsigned int)((v_r12) + (2));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_r12)), (unsigned int)(0x63647050ULL), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(v_r14)) + 0 + 0 * 4 - 24 * 2)) * 8) + 40))));
    v_r10 = 0;
    if (result != 0) goto loc_00735DAC;
    goto loc_00735F49;
loc_00735DAC:
loc_00735DB2:
loc_00735DB6:
loc_00735DBB:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m88)) == 0) goto loc_00735F28;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m88))) != 37) goto loc_00735F0D;
    a3 = (v_stack_m88) + (2);
    v_stack_m88 = a3;
    if (((unsigned __int16)(*(unsigned __int16 *)(a3))) != 37) goto loc_00735DF5;
    if (((unsigned int)((unsigned int)((unsigned int)(v_r12)))) <= 2) goto loc_00735F32;
    *(unsigned __int16 *)(result) = 37;
    goto loc_00735F17;
loc_00735DF5:
    if (((unsigned __int16)(*(unsigned __int16 *)(a3) - 48)) > 9) goto loc_00735DBB;
    if ((unsigned __int16)(*(unsigned __int16 *)(a3)) == 0) goto loc_00735E2C;
loc_00735E06:
    if (((unsigned __int16)(*(unsigned __int16 *)(a3) - 48)) > 9) goto loc_00735E28;
    a3 = (a3) + (2);
    if ((unsigned __int16)(*(unsigned __int16 *)(a3)) != 0) goto loc_00735E06;
loc_00735E28:
    v_stack_m88 = a3;
loc_00735E2C:
    if (((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a3)) + 0 + 0 * 4 - 24 * 2)) >= v_stack_m98) goto loc_00735DB6;
    if (*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a3)) + 0 + 0 * 4 - 24 * 2)) * 8) == 0) goto loc_00735DBB;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a3)) + 0 + 0 * 4 - 24 * 2)) * 8) + 32))) - (1));
    if (condition_is_equal) goto loc_00735ECB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00735ECB;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00735E82;
    if (((unsigned int)(a1)) != 3) goto loc_00735DBB;
    v_rsi = (v_stack_m78) | (-1);
loc_00735E74:
    v_rsi = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a3)) + 0 + 0 * 4 - 24 * 2)) * 8) + 40) + v_rsi * 2)) != 0) goto loc_00735E74;
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_rsi)));
    goto loc_00735ED5;
loc_00735E82:
    result = RtlStringCchPrintfW(v_stack_m60, 11, v_rip + 3963923, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a3)) + 0 + 0 * 4 - 24 * 2)) * 8) + 40))));
    v_r10 = 0;
    if (sign_flag) goto loc_00735DBB;
    v_rsi = (v_rsi) | (-1);
loc_00735EBD:
    v_rsi = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(v_stack_m60 + v_rsi * 2)) != 0) goto loc_00735EBD;
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_rsi)));
    goto loc_00735EDE;
loc_00735ECB:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(11 + 36))) - (2));
loc_00735ED5:
    if (*(unsigned __int64 *)(11 + 40) == 0) goto loc_00735DB6;
loc_00735EDE:
    if ((unsigned int)(v_rsi) == 0) goto loc_00735DB6;
    if (((unsigned int)((unsigned int)((unsigned int)(v_r12)))) <= ((unsigned int)(v_rsi))) goto loc_00735F32;
    result = memcpy(result, *(unsigned __int64 *)(11 + 40), (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a3)) + 0 + 0 * 4 - 24 * 2)) * 8) + 40))));
    v_rbx = ((unsigned int)((unsigned int)(v_rsi))) >> (1);
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - ((unsigned int)(v_rsi)));
    v_r10 = 0;
    goto loc_00735DB2;
loc_00735F0D:
    if (((unsigned int)(v_r14)) <= 2) goto loc_00735F32;
    *(unsigned __int16 *)(result + v_rbx * 2) = (unsigned __int16)(result);
loc_00735F17:
    v_r15 = (result + v_rbx * 2) + (2);
    a3 = ((unsigned int)((unsigned int)(v_rsi))) + (2);
    v_r14 = (unsigned int)((v_r14) + (-2));
    goto loc_00735DBB;
loc_00735F28:
    if (sign_flag) goto loc_00735F37;
    if (((unsigned int)(v_r14)) == 2) goto loc_00735F54;
loc_00735F32:
loc_00735F37:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a3)) + 0 + 0 * 4 - 24 * 2)) * 8) + 40))));
loc_00735F41:
loc_00735F49:
    if (v_stack_m90 == 0) goto loc_00735F78;
    goto loc_00735F71;
loc_00735F54:
    *(unsigned __int16 *)(v_r15) = 0;
    *(unsigned int *)(v_stack_m68 + 32) = 1;
    *(unsigned int *)(v_stack_m68 + 36) = (unsigned int)(v_r12);
    *(unsigned __int64 *)(v_stack_m68 + 40) = result;
    goto loc_00735F41;
loc_00735F6D:
loc_00735F71:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a3)) + 0 + 0 * 4 - 24 * 2)) * 8) + 40))));
loc_00735F78:
    if (v_stack_m78 != 0) {
        a2 = 0;
        a1 = v_stack_m78;
        result = ExFreePoolWithTag(a1, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a3)) + 0 + 0 * 4 - 24 * 2)) * 8) + 40))));
    }
    if (v_stack_m80 != 0) {
        a2 = 0;
        a1 = v_stack_m80;
        result = ExFreePoolWithTag(a1, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a3)) + 0 + 0 * 4 - 24 * 2)) * 8) + 40))));
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a3)) + 0 + 0 * 4 - 24 * 2)) * 8) + 40))));
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgResolveVariableFormatString(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x6D4C6F)) ^ (local_rsp);
    v_stack_m48 = result;
    result = 0;
    v_stack_m68 = Arg3;
    v_stack_m80 = 0;
    v_stack_m78 = 0;
    v_stack_m98 = 0;
    v_stack_m90 = 0;
    Arg3 = 0;
    result = IopGetRegistryValue(Arg2, v_rip + 3971852, Arg3, v_stack_m80);
    if (sign_flag) goto loc_00735F87;
    result = PnpValidateRegistryString(v_stack_m80, v_rip + 3971852, Arg3, v_stack_m80);
    if ((uint8_t)(result) != 0) goto loc_00735B30;
    goto loc_00735F87;
loc_00735B30:
    local_r13 = ((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x8))) + (v_stack_m80);
    Arg3 = 0;
    v_stack_m88 = local_r13;
    result = IopGetRegistryValue(Arg2, v_rip + 3970574, Arg3, v_stack_m78);
    local_r10 = 0;
    if (!sign_flag) goto loc_00735BE9;
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00735F78;
loc_00735B70:
    if (v_stack_m78 == 0) goto loc_00735C6F;
    local_r14 = ((uint32_t)(*(uint32_t *)(v_stack_m78 + 0x8))) + (v_stack_m78);
    if ((*(uint16_t *)(local_r14)) == 0) goto loc_00735C6F;
loc_00735B8D:
    local_r15 = (uint32_t)((0) + 1);
    result = (result) | (-1);
loc_00735B94:
    result = (result) + 1;
    if ((*(uint16_t *)(local_r14 + result * 2)) != 0) goto loc_00735B94;
    Arg1 = (local_r14 + result * 2) + (2);
    if ((*(uint16_t *)(Arg1)) != 0) goto loc_00735B8D;
    v_stack_m98 = (uint32_t)(local_r15);
    if ((uint32_t)(local_r15) == 0) goto loc_00735C6F;
    Arg2 = ((uint32_t)((uint32_t)(local_r15))) << (3);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x63647050ULL), v_stack_m78);
    local_r10 = 0;
    v_stack_m90 = result;
    if (result != 0) goto loc_00735C03;
    goto loc_00735F78;
loc_00735BE9:
    result = PnpValidateRegistryMultiSz(v_stack_m78, result, (uint32_t)(0x63647050ULL), v_stack_m78);
    if ((uint8_t)(result) != 0) goto loc_00735B70;
    goto loc_00735F78;
loc_00735C03:
loc_00735C06:
    if ((*(uint16_t *)(local_r14)) == 0) goto loc_00735C63;
    if (0 >= v_stack_m98) goto loc_00735C63;
    result = PiDevCfgResolveVariable(Arg1, local_r14, result + 0 * 8, v_stack_m78);
    local_r10 = 0;
    if (sign_flag) goto loc_00735C4C;
    result = (result) | (-1);
loc_00735C31:
    result = (result) + 1;
    if ((*(uint16_t *)(local_r14 + result * 2)) != 0) goto loc_00735C31;
    local_r14 = (local_r14 + result * 2) + (2);
    local_r15 = (uint32_t)((0) + 1);
    goto loc_00735C06;
loc_00735C4C:
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00735F71;
    goto loc_00735F71;
loc_00735C63:
    if (sign_flag) goto loc_00735F6D;
loc_00735C6F:
    v_stack_m70 = (uint32_t)(result - 51);
    if ((uint16_t)(*(uint16_t *)(local_r13)) == 0) goto loc_00735D80;
loc_00735C8F:
    local_r14 = (local_r13) + (2);
    if (((uint16_t)(*(uint16_t *)(local_r13))) != 37) goto loc_00735CA5;
    if (((uint16_t)(*(uint16_t *)(local_r14))) != 37) goto loc_00735CAE;
    local_r14 = (local_r14) + (2);
loc_00735CA5:
    local_r12 = (uint32_t)((0) + (2));
    goto loc_00735D68;
loc_00735CAE:
    if (((uint16_t)(*(uint16_t *)(local_r14) - 48)) > 9) goto loc_00735D68;
    goto loc_00735CDD;
loc_00735CC0:
    if (((uint16_t)(*(uint16_t *)(local_r14) - 48)) > 9) goto loc_00735CE2;
    local_r14 = (local_r14) + (2);
loc_00735CDD:
    if ((uint16_t)(*(uint16_t *)(local_r14)) != 0) goto loc_00735CC0;
loc_00735CE2:
    if (((uint32_t)((uint16_t)(*(uint16_t *)(local_r14)) + 0 + 0 * 4 - 24 * 2)) >= ((uint32_t)((uint32_t)(v_stack_m98)))) goto loc_00735D63;
    if (*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(local_r14)) + 0x0 + 0x0 * 4 - 0x18 * 2)) * 8) == 0) goto loc_00735D63;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(local_r14)) + 0x0 + 0x0 * 4 - 0x18 * 2)) * 8) + 0x20))) - (1));
    if (condition_is_equal) goto loc_00735D5B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00735D5B;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00735D24;
    if (((uint32_t)(Arg1)) != 3) goto loc_00735D63;
    result = ((uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(local_r14)) + 0 + 0 * 4 - 24 * 2))) | (-1);
loc_00735D14:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(local_r14)) + 0x0 + 0x0 * 4 - 0x18 * 2)) * 8) + 0x28) + result * 2)) != 0) goto loc_00735D14;
loc_00735D1E:
    goto loc_00735D63;
loc_00735D24:
    result = RtlStringCchPrintfW(v_stack_m60, 11, v_rip + 3964273, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(local_r14)) + 0x0 + 0x0 * 4 - 0x18 * 2)) * 8) + 0x28))));
    local_r10 = 0;
    if (sign_flag) goto loc_00735D63;
    result = (result) | (-1);
loc_00735D4F:
    result = (result) + 1;
    if ((*(uint16_t *)(v_stack_m60 + result * 2)) != 0) goto loc_00735D4F;
    goto loc_00735D1E;
loc_00735D5B:
    local_r12 = (uint32_t)((local_r12 + result * 2) + (-2));
    local_r12 = (uint32_t)((local_r12) + (*(uint32_t *)(11 + 0x24)));
loc_00735D63:
loc_00735D68:
    if ((uint16_t)(*(uint16_t *)(local_r14)) != 0) goto loc_00735C8F;
loc_00735D80:
    local_r12 = (uint32_t)((local_r12) + (2));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_r12)), (uint32_t)(0x63647050ULL), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(local_r14)) + 0x0 + 0x0 * 4 - 0x18 * 2)) * 8) + 0x28))));
    local_r10 = 0;
    if (result != 0) goto loc_00735DAC;
    goto loc_00735F49;
loc_00735DAC:
loc_00735DB2:
loc_00735DB6:
loc_00735DBB:
    if ((uint16_t)(*(uint16_t *)(v_stack_m88)) == 0) goto loc_00735F28;
    if (((uint16_t)(*(uint16_t *)(v_stack_m88))) != 37) goto loc_00735F0D;
    Arg3 = (v_stack_m88) + (2);
    v_stack_m88 = Arg3;
    if (((uint16_t)(*(uint16_t *)(Arg3))) != 37) goto loc_00735DF5;
    if (((uint32_t)((uint32_t)((uint32_t)(local_r12)))) <= 2) goto loc_00735F32;
    *(uint16_t *)(result) = 37;
    goto loc_00735F17;
loc_00735DF5:
    if (((uint16_t)(*(uint16_t *)(Arg3) - 48)) > 9) goto loc_00735DBB;
    if ((uint16_t)(*(uint16_t *)(Arg3)) == 0) goto loc_00735E2C;
loc_00735E06:
    if (((uint16_t)(*(uint16_t *)(Arg3) - 48)) > 9) goto loc_00735E28;
    Arg3 = (Arg3) + (2);
    if ((uint16_t)(*(uint16_t *)(Arg3)) != 0) goto loc_00735E06;
loc_00735E28:
    v_stack_m88 = Arg3;
loc_00735E2C:
    if (((uint32_t)((uint16_t)(*(uint16_t *)(Arg3)) + 0 + 0 * 4 - 24 * 2)) >= v_stack_m98) goto loc_00735DB6;
    if (*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(Arg3)) + 0x0 + 0x0 * 4 - 0x18 * 2)) * 8) == 0) goto loc_00735DBB;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(Arg3)) + 0x0 + 0x0 * 4 - 0x18 * 2)) * 8) + 0x20))) - (1));
    if (condition_is_equal) goto loc_00735ECB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00735ECB;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00735E82;
    if (((uint32_t)(Arg1)) != 3) goto loc_00735DBB;
    local_rsi = (v_stack_m78) | (-1);
loc_00735E74:
    local_rsi = (local_rsi) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(Arg3)) + 0x0 + 0x0 * 4 - 0x18 * 2)) * 8) + 0x28) + local_rsi * 2)) != 0) goto loc_00735E74;
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(local_rsi)));
    goto loc_00735ED5;
loc_00735E82:
    result = RtlStringCchPrintfW(v_stack_m60, 11, v_rip + 3963923, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(Arg3)) + 0x0 + 0x0 * 4 - 0x18 * 2)) * 8) + 0x28))));
    local_r10 = 0;
    if (sign_flag) goto loc_00735DBB;
    local_rsi = (local_rsi) | (-1);
loc_00735EBD:
    local_rsi = (local_rsi) + 1;
    if ((*(uint16_t *)(v_stack_m60 + local_rsi * 2)) != 0) goto loc_00735EBD;
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(local_rsi)));
    goto loc_00735EDE;
loc_00735ECB:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(11 + 0x24))) - (2));
loc_00735ED5:
    if (*(uint64_t *)(11 + 0x28) == 0) goto loc_00735DB6;
loc_00735EDE:
    if ((uint32_t)(local_rsi) == 0) goto loc_00735DB6;
    if (((uint32_t)((uint32_t)((uint32_t)(local_r12)))) <= ((uint32_t)(local_rsi))) goto loc_00735F32;
    result = memcpy(result, *(uint64_t *)(11 + 0x28), (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(Arg3)) + 0x0 + 0x0 * 4 - 0x18 * 2)) * 8) + 0x28))));
    local_rbx = ((uint32_t)((uint32_t)(local_rsi))) >> (1);
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - ((uint32_t)(local_rsi)));
    local_r10 = 0;
    goto loc_00735DB2;
loc_00735F0D:
    if (((uint32_t)(local_r14)) <= 2) goto loc_00735F32;
    *(uint16_t *)(result + local_rbx * 2) = (uint16_t)(result);
loc_00735F17:
    local_r15 = (result + local_rbx * 2) + (2);
    Arg3 = ((uint32_t)((uint32_t)(local_rsi))) + (2);
    local_r14 = (uint32_t)((local_r14) + (-2));
    goto loc_00735DBB;
loc_00735F28:
    if (sign_flag) goto loc_00735F37;
    if (((uint32_t)(local_r14)) == 2) goto loc_00735F54;
loc_00735F32:
loc_00735F37:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(Arg3)) + 0x0 + 0x0 * 4 - 0x18 * 2)) * 8) + 0x28))));
loc_00735F41:
loc_00735F49:
    if (v_stack_m90 == 0) goto loc_00735F78;
    goto loc_00735F71;
loc_00735F54:
    *(uint16_t *)(local_r15) = 0;
    *(uint32_t *)(v_stack_m68 + 0x20) = 1;
    *(uint32_t *)(v_stack_m68 + 0x24) = (uint32_t)(local_r12);
    *(uint64_t *)(v_stack_m68 + 0x28) = result;
    goto loc_00735F41;
loc_00735F6D:
loc_00735F71:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, Arg2, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(Arg3)) + 0x0 + 0x0 * 4 - 0x18 * 2)) * 8) + 0x28))));
loc_00735F78:
    if (v_stack_m78 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m78;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(Arg3)) + 0x0 + 0x0 * 4 - 0x18 * 2)) * 8) + 0x28))));
    }
    if (v_stack_m80 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m80;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(Arg3)) + 0x0 + 0x0 * 4 - 0x18 * 2)) * 8) + 0x28))));
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)((uint16_t)(*(uint16_t *)(Arg3)) + 0x0 + 0x0 * 4 - 0x18 * 2)) * 8) + 0x28))));
    local_rsp = (local_rsp) + (128);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00735AB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
