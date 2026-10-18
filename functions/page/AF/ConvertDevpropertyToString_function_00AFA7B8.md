# ConvertDevpropertyToString

- RVA: `0x00AFA7B8`–`0x00AFAEFD` (길이 `1,861` bytes)
- VA: `0x0000000140AFA7B8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DAC50`
- 디코드: `478`개 명령, `1,861/1,861` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **39**

### Outgoing calls
- `0x00AFA808` → [ConvertDevpropcompkeyToString](ConvertDevpropcompkeyToString_function_00AFA604.md) (function, `0x00AFA604`)
- `0x00AFAA9E` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (function, `0x0045488C`)
- `0x00AFAB86` → [RtlStringCbPrintfExW](../../text/46/RtlStringCbPrintfExW_function_00461AD4.md) (function, `0x00461AD4`)
- `0x00AFAC99` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (function, `0x0045488C`)
- `0x00AFACC0` → [Feature_KernelPnP_DevfilterLogging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_DevfilterLogging__private_IsEnabledDeviceUsageNoInline_function_006A3150.md) (function, `0x006A3150`)
- `0x00AFAD84` → [RtlStringCbPrintfExW](../../text/46/RtlStringCbPrintfExW_function_00461AD4.md) (function, `0x00461AD4`)
- `0x00AFAEA0` → [RtlStringCbPrintfExW](../../text/46/RtlStringCbPrintfExW_function_00461AD4.md) (function, `0x00461AD4`)

### Direct callers
- [ExpressionConvertToString](../AD/ExpressionConvertToString_function_00AD83F8.md) at `0x00AD8758`

### Static image references
- `0x00AFA8A7` → RVA `0x00B0DCE0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA8B3` → RVA `0x00B0DCD0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA8BF` → RVA `0x00B0DCC0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA8CB` → RVA `0x00B0DCB0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA8D7` → RVA `0x00B0A170` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA8E3` → RVA `0x00B0DCA0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA8EF` → RVA `0x00B0DCF0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA91D` → RVA `0x00B0DD50` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA929` → RVA `0x00B0DD40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA935` → RVA `0x00B0DD30` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA941` → RVA `0x00B0DD20` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA94D` → RVA `0x00B0DD10` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA959` → RVA `0x00B0DD00` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA965` → RVA `0x00B0DD60` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA99A` → RVA `0x00B0DB00` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA9A6` → RVA `0x00B0DAD0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA9B2` → RVA `0x00B0DAC0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA9BE` → RVA `0x00B0DAA0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA9CA` → RVA `0x00B0DA90` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA9D6` → RVA `0x00B0DD90` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFA9E2` → RVA `0x00B0DB30` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAA04` → RVA `0x00B0DBF0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAA0D` → RVA `0x00B0DBD0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAA16` → RVA `0x00B0DBC0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAA1F` → RVA `0x00B0DB90` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAA28` → RVA `0x00B0DB70` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAA31` → RVA `0x00B0DBB0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAA52` → RVA `0x00B0DAE0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAA5B` → RVA `0x00B0DD70` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAB4A` → RVA `0x00B0DC30` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAB67` → RVA `0x00B0DC10` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFABE6` → RVA `0x00B0DEE0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAC07` → RVA `0x00B0DEC0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAC58` → RVA `0x00B0DF70` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAC5F` → RVA `0x00B0DF60` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFACF2` → RVA `0x00B0DF80` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAD1E` → RVA `0x00B0DC50` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAD60` → RVA `0x00B0DF90` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AFAE40` → RVA `0x00B0DEF0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00AFAA9E` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (`PAGE` → `.text`)
  - `0x00AFAB86` → [RtlStringCbPrintfExW](../../text/46/RtlStringCbPrintfExW_function_00461AD4.md) (`PAGE` → `.text`)
  - `0x00AFAC99` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (`PAGE` → `.text`)
  - `0x00AFACC0` → [Feature_KernelPnP_DevfilterLogging__private_IsEnabledDeviceUsageNoInline](../../text/6A/Feature_KernelPnP_DevfilterLogging__private_IsEnabledDeviceUsageNoInline_function_006A3150.md) (`PAGE` → `.text`)
  - `0x00AFAD84` → [RtlStringCbPrintfExW](../../text/46/RtlStringCbPrintfExW_function_00461AD4.md) (`PAGE` → `.text`)
  - `0x00AFAEA0` → [RtlStringCbPrintfExW](../../text/46/RtlStringCbPrintfExW_function_00461AD4.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AFA7B8  48 8B C4                        mov rax, rsp
00AFA7BB  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00AFA7BF  89 50 10                        mov dword ptr [rax + 0x10], edx
00AFA7C2  48 89 48 08                     mov qword ptr [rax + 8], rcx
00AFA7C6  55                              push rbp
00AFA7C7  53                              push rbx
00AFA7C8  56                              push rsi
00AFA7C9  57                              push rdi
00AFA7CA  41 54                           push r12
00AFA7CC  41 55                           push r13
00AFA7CE  41 56                           push r14
00AFA7D0  41 57                           push r15
00AFA7D2  48 8D 68 A1                     lea rbp, [rax - 0x5f]
00AFA7D6  48 81 EC B8 00 00 00            sub rsp, 0xb8
00AFA7DD  33 C0                           xor eax, eax
00AFA7DF  44 8B FA                        mov r15d, edx
00AFA7E2  4D 8B E8                        mov r13, r8
00AFA7E5  89 45 77                        mov dword ptr [rbp + 0x77], eax
00AFA7E8  8D 78 02                        lea edi, [rax + 2]
00AFA7EB  3B D7                           cmp edx, edi
00AFA7ED  72 04                           jb 0x140afa7f3
00AFA7EF  66 41 89 00                     mov word ptr [r8], ax
00AFA7F3  4C 8D 4D 77                     lea r9, [rbp + 0x77]
00AFA7F7  4C 89 6D FF                     mov qword ptr [rbp - 1], r13
00AFA7FB  45 8B C7                        mov r8d, r15d
00AFA7FE  4C 89 7D F7                     mov qword ptr [rbp - 9], r15
00AFA802  49 8B D5                        mov rdx, r13
00AFA805  4D 8B F7                        mov r14, r15
00AFA808  E8 F7 FD FF FF                  call 0x140afa604
00AFA80D  8B D8                           mov ebx, eax
00AFA80F  BA 23 00 00 C0                  mov edx, 0xc0000023
00AFA814  B8 00 00 00 80                  mov eax, 0x80000000
00AFA819  8D 0C 03                        lea ecx, [rbx + rax]
00AFA81C  85 C8                           test eax, ecx
00AFA81E  75 08                           jne 0x140afa828
00AFA820  3B DA                           cmp ebx, edx
00AFA822  0F 85 BE 06 00 00               jne 0x140afaee6
00AFA828  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00AFA82B  45 33 D2                        xor r10d, r10d
00AFA82E  8B C8                           mov ecx, eax
00AFA830  41 8B DA                        mov ebx, r10d
00AFA833  44 8D 48 02                     lea r9d, [rax + 2]
00AFA837  48 83 C0 FE                     add rax, -2
00AFA83B  4C 3B F0                        cmp r14, rax
00AFA83E  72 16                           jb 0x140afa856
00AFA840  48 2B F9                        sub rdi, rcx
00AFA843  4C 03 F7                        add r14, rdi
00AFA846  48 D1 E8                        shr rax, 1
00AFA849  4C 89 75 F7                     mov qword ptr [rbp - 9], r14
00AFA84D  4D 8D 6C 45 00                  lea r13, [r13 + rax*2]
00AFA852  4C 89 6D FF                     mov qword ptr [rbp - 1], r13
00AFA856  48 8B 55 67                     mov rdx, qword ptr [rbp + 0x67]
00AFA85A  B9 03 10 00 00                  mov ecx, 0x1003
00AFA85F  8B 42 20                        mov eax, dword ptr [rdx + 0x20]
00AFA862  3B C1                           cmp eax, ecx
00AFA864  0F 87 D0 01 00 00               ja 0x140afaa3a
00AFA86A  0F 84 C1 01 00 00               je 0x140afaa31
00AFA870  83 F8 0D                        cmp eax, 0xd
00AFA873  0F 87 F8 00 00 00               ja 0x140afa971
00AFA879  0F 84 E6 00 00 00               je 0x140afa965
00AFA87F  83 F8 06                        cmp eax, 6
00AFA882  77 77                           ja 0x140afa8fb
00AFA884  74 69                           je 0x140afa8ef
00AFA886  85 C0                           test eax, eax
00AFA888  74 59                           je 0x140afa8e3
00AFA88A  83 E8 01                        sub eax, 1
00AFA88D  74 48                           je 0x140afa8d7
00AFA88F  83 E8 01                        sub eax, 1
00AFA892  74 37                           je 0x140afa8cb
00AFA894  83 E8 01                        sub eax, 1
00AFA897  74 26                           je 0x140afa8bf
00AFA899  83 E8 01                        sub eax, 1
00AFA89C  74 15                           je 0x140afa8b3
00AFA89E  83 F8 01                        cmp eax, 1
00AFA8A1  0F 85 A1 01 00 00               jne 0x140afaa48
00AFA8A7  4C 8D 05 32 34 01 00            lea r8, [rip + 0x13432]
00AFA8AE  E9 AF 01 00 00                  jmp 0x140afaa62
00AFA8B3  4C 8D 05 16 34 01 00            lea r8, [rip + 0x13416]
00AFA8BA  E9 A3 01 00 00                  jmp 0x140afaa62
00AFA8BF  4C 8D 05 FA 33 01 00            lea r8, [rip + 0x133fa]
00AFA8C6  E9 97 01 00 00                  jmp 0x140afaa62
00AFA8CB  4C 8D 05 DE 33 01 00            lea r8, [rip + 0x133de]
00AFA8D2  E9 8B 01 00 00                  jmp 0x140afaa62
00AFA8D7  4C 8D 05 92 F8 00 00            lea r8, [rip + 0xf892]
00AFA8DE  E9 7F 01 00 00                  jmp 0x140afaa62
00AFA8E3  4C 8D 05 B6 33 01 00            lea r8, [rip + 0x133b6]
00AFA8EA  E9 73 01 00 00                  jmp 0x140afaa62
00AFA8EF  4C 8D 05 FA 33 01 00            lea r8, [rip + 0x133fa]
00AFA8F6  E9 67 01 00 00                  jmp 0x140afaa62
00AFA8FB  83 E8 07                        sub eax, 7
00AFA8FE  74 59                           je 0x140afa959
00AFA900  83 E8 01                        sub eax, 1
00AFA903  74 48                           je 0x140afa94d
00AFA905  83 E8 01                        sub eax, 1
00AFA908  74 37                           je 0x140afa941
00AFA90A  83 E8 01                        sub eax, 1
00AFA90D  74 26                           je 0x140afa935
00AFA90F  83 E8 01                        sub eax, 1
00AFA912  74 15                           je 0x140afa929
00AFA914  83 F8 01                        cmp eax, 1
00AFA917  0F 85 2B 01 00 00               jne 0x140afaa48
00AFA91D  4C 8D 05 2C 34 01 00            lea r8, [rip + 0x1342c]
00AFA924  E9 39 01 00 00                  jmp 0x140afaa62
00AFA929  4C 8D 05 10 34 01 00            lea r8, [rip + 0x13410]
00AFA930  E9 2D 01 00 00                  jmp 0x140afaa62
00AFA935  4C 8D 05 F4 33 01 00            lea r8, [rip + 0x133f4]
00AFA93C  E9 21 01 00 00                  jmp 0x140afaa62
00AFA941  4C 8D 05 D8 33 01 00            lea r8, [rip + 0x133d8]
00AFA948  E9 15 01 00 00                  jmp 0x140afaa62
00AFA94D  4C 8D 05 BC 33 01 00            lea r8, [rip + 0x133bc]
00AFA954  E9 09 01 00 00                  jmp 0x140afaa62
00AFA959  4C 8D 05 A0 33 01 00            lea r8, [rip + 0x133a0]
00AFA960  E9 FD 00 00 00                  jmp 0x140afaa62
00AFA965  4C 8D 05 F4 33 01 00            lea r8, [rip + 0x133f4]
00AFA96C  E9 F1 00 00 00                  jmp 0x140afaa62
00AFA971  83 F8 14                        cmp eax, 0x14
00AFA974  77 75                           ja 0x140afa9eb
00AFA976  74 6A                           je 0x140afa9e2
00AFA978  83 E8 0E                        sub eax, 0xe
00AFA97B  74 59                           je 0x140afa9d6
00AFA97D  83 E8 01                        sub eax, 1
00AFA980  74 48                           je 0x140afa9ca
00AFA982  83 E8 01                        sub eax, 1
00AFA985  74 37                           je 0x140afa9be
00AFA987  83 E8 01                        sub eax, 1
00AFA98A  74 26                           je 0x140afa9b2
00AFA98C  83 E8 01                        sub eax, 1
00AFA98F  74 15                           je 0x140afa9a6
00AFA991  83 F8 01                        cmp eax, 1
00AFA994  0F 85 AE 00 00 00               jne 0x140afaa48
00AFA99A  4C 8D 05 5F 31 01 00            lea r8, [rip + 0x1315f]
00AFA9A1  E9 BC 00 00 00                  jmp 0x140afaa62
00AFA9A6  4C 8D 05 23 31 01 00            lea r8, [rip + 0x13123]
00AFA9AD  E9 B0 00 00 00                  jmp 0x140afaa62
00AFA9B2  4C 8D 05 07 31 01 00            lea r8, [rip + 0x13107]
00AFA9B9  E9 A4 00 00 00                  jmp 0x140afaa62
00AFA9BE  4C 8D 05 DB 30 01 00            lea r8, [rip + 0x130db]
00AFA9C5  E9 98 00 00 00                  jmp 0x140afaa62
00AFA9CA  4C 8D 05 BF 30 01 00            lea r8, [rip + 0x130bf]
00AFA9D1  E9 8C 00 00 00                  jmp 0x140afaa62
00AFA9D6  4C 8D 05 B3 33 01 00            lea r8, [rip + 0x133b3]
00AFA9DD  E9 80 00 00 00                  jmp 0x140afaa62
00AFA9E2  4C 8D 05 47 31 01 00            lea r8, [rip + 0x13147]
00AFA9E9  EB 77                           jmp 0x140afaa62
00AFA9EB  83 E8 15                        sub eax, 0x15
00AFA9EE  74 38                           je 0x140afaa28
00AFA9F0  83 E8 01                        sub eax, 1
00AFA9F3  74 2A                           je 0x140afaa1f
00AFA9F5  83 E8 01                        sub eax, 1
00AFA9F8  74 1C                           je 0x140afaa16
00AFA9FA  83 E8 01                        sub eax, 1
00AFA9FD  74 0E                           je 0x140afaa0d
00AFA9FF  83 F8 01                        cmp eax, 1
00AFAA02  75 44                           jne 0x140afaa48
00AFAA04  4C 8D 05 E5 31 01 00            lea r8, [rip + 0x131e5]
00AFAA0B  EB 55                           jmp 0x140afaa62
00AFAA0D  4C 8D 05 BC 31 01 00            lea r8, [rip + 0x131bc]
00AFAA14  EB 4C                           jmp 0x140afaa62
00AFAA16  4C 8D 05 A3 31 01 00            lea r8, [rip + 0x131a3]
00AFAA1D  EB 43                           jmp 0x140afaa62
00AFAA1F  4C 8D 05 6A 31 01 00            lea r8, [rip + 0x1316a]
00AFAA26  EB 3A                           jmp 0x140afaa62
00AFAA28  4C 8D 05 41 31 01 00            lea r8, [rip + 0x13141]
00AFAA2F  EB 31                           jmp 0x140afaa62
00AFAA31  4C 8D 05 78 31 01 00            lea r8, [rip + 0x13178]
00AFAA38  EB 28                           jmp 0x140afaa62
00AFAA3A  3D 0D 10 00 00                  cmp eax, 0x100d
00AFAA3F  74 1A                           je 0x140afaa5b
00AFAA41  3D 12 20 00 00                  cmp eax, 0x2012
00AFAA46  74 0A                           je 0x140afaa52
00AFAA48  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AFAA4D  E9 94 04 00 00                  jmp 0x140afaee6
00AFAA52  4C 8D 05 87 30 01 00            lea r8, [rip + 0x13087]
00AFAA59  EB 07                           jmp 0x140afaa62
00AFAA5B  4C 8D 05 0E 33 01 00            lea r8, [rip + 0x1330e]
00AFAA62  48 83 CE FF                     or rsi, 0xffffffffffffffff
00AFAA66  48 8B C6                        mov rax, rsi
00AFAA69  48 FF C0                        inc rax
00AFAA6C  66 45 39 14 40                  cmp word ptr [r8 + rax*2], r10w
00AFAA71  75 F6                           jne 0x140afaa69
00AFAA73  45 8D 61 FE                     lea r12d, [r9 - 2]
00AFAA77  41 B9 00 04 00 00               mov r9d, 0x400
00AFAA7D  45 8D 24 44                     lea r12d, [r12 + rax*2]
00AFAA81  45 3B E7                        cmp r12d, r15d
00AFAA84  77 41                           ja 0x140afaac7
00AFAA86  44 89 4C 24 28                  mov dword ptr [rsp + 0x28], r9d
00AFAA8B  48 8D 45 F7                     lea rax, [rbp - 9]
00AFAA8F  4C 8D 4D FF                     lea r9, [rbp - 1]
00AFAA93  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AFAA98  49 8B D6                        mov rdx, r14
00AFAA9B  49 8B CD                        mov rcx, r13
00AFAA9E  E8 E9 9D 95 FF                  call 0x14045488c
00AFAAA3  45 33 D2                        xor r10d, r10d
00AFAAA6  8B D8                           mov ebx, eax
00AFAAA8  85 C0                           test eax, eax
00AFAAAA  0F 88 36 04 00 00               js 0x140afaee6
00AFAAB0  4C 8B 6D FF                     mov r13, qword ptr [rbp - 1]
00AFAAB4  B9 03 10 00 00                  mov ecx, 0x1003
00AFAAB9  4C 8B 75 F7                     mov r14, qword ptr [rbp - 9]
00AFAABD  41 B9 00 04 00 00               mov r9d, 0x400
00AFAAC3  48 8B 55 67                     mov rdx, qword ptr [rbp + 0x67]
00AFAAC7  44 39 52 24                     cmp dword ptr [rdx + 0x24], r10d
00AFAACB  0F 86 FE 03 00 00               jbe 0x140afaecf
00AFAAD1  48 8B 7A 28                     mov rdi, qword ptr [rdx + 0x28]
00AFAAD5  48 85 FF                        test rdi, rdi
00AFAAD8  0F 84 F1 03 00 00               je 0x140afaecf
00AFAADE  8B 42 20                        mov eax, dword ptr [rdx + 0x20]
00AFAAE1  3B C1                           cmp eax, ecx
00AFAAE3  0F 87 41 02 00 00               ja 0x140afad2a
00AFAAE9  0F 84 E0 03 00 00               je 0x140afaecf
00AFAAEF  83 F8 0D                        cmp eax, 0xd
00AFAAF2  0F 87 1B 01 00 00               ja 0x140afac13
00AFAAF8  0F 84 C6 02 00 00               je 0x140afadc4
00AFAAFE  83 F8 06                        cmp eax, 6
00AFAB01  0F 87 93 00 00 00               ja 0x140afab9a
00AFAB07  0F 84 FE 01 00 00               je 0x140afad0b
00AFAB0D  85 C0                           test eax, eax
00AFAB0F  0F 84 33 FF FF FF               je 0x140afaa48
00AFAB15  83 E8 01                        sub eax, 1
00AFAB18  0F 84 2A FF FF FF               je 0x140afaa48
00AFAB1E  83 E8 01                        sub eax, 1
00AFAB21  74 30                           je 0x140afab53
00AFAB23  83 E8 01                        sub eax, 1
00AFAB26  74 2B                           je 0x140afab53
00AFAB28  83 E8 01                        sub eax, 1
00AFAB2B  74 09                           je 0x140afab36
00AFAB2D  83 F8 01                        cmp eax, 1
00AFAB30  0F 85 06 02 00 00               jne 0x140afad3c
00AFAB36  41 83 C4 10                     add r12d, 0x10
00AFAB3A  45 3B E7                        cmp r12d, r15d
00AFAB3D  0F 87 8C 03 00 00               ja 0x140afaecf
00AFAB43  0F BF 07                        movsx eax, word ptr [rdi]
00AFAB46  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00AFAB4A  48 8D 05 DF 30 01 00            lea rax, [rip + 0x130df]
00AFAB51  EB 1B                           jmp 0x140afab6e
00AFAB53  41 83 C4 0C                     add r12d, 0xc
00AFAB57  45 3B E7                        cmp r12d, r15d
00AFAB5A  0F 87 6F 03 00 00               ja 0x140afaecf
00AFAB60  0F B6 07                        movzx eax, byte ptr [rdi]
00AFAB63  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00AFAB67  48 8D 05 A2 30 01 00            lea rax, [rip + 0x130a2]
00AFAB6E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AFAB73  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00AFAB78  4C 8D 4D F7                     lea r9, [rbp - 9]
00AFAB7C  49 8B D6                        mov rdx, r14
00AFAB7F  4C 8D 45 FF                     lea r8, [rbp - 1]
00AFAB83  49 8B CD                        mov rcx, r13
00AFAB86  E8 49 6F 96 FF                  call 0x140461ad4
00AFAB8B  8B D8                           mov ebx, eax
00AFAB8D  85 C0                           test eax, eax
00AFAB8F  0F 88 51 03 00 00               js 0x140afaee6
00AFAB95  E9 35 03 00 00                  jmp 0x140afaecf
00AFAB9A  8B C8                           mov ecx, eax
00AFAB9C  83 E9 07                        sub ecx, 7
00AFAB9F  0F 84 66 01 00 00               je 0x140afad0b
00AFABA5  83 E9 01                        sub ecx, 1
00AFABA8  74 48                           je 0x140afabf2
00AFABAA  83 E9 01                        sub ecx, 1
00AFABAD  74 43                           je 0x140afabf2
00AFABAF  83 E9 01                        sub ecx, 1
00AFABB2  74 0D                           je 0x140afabc1
00AFABB4  83 E9 01                        sub ecx, 1
00AFABB7  74 08                           je 0x140afabc1
00AFABB9  83 F9 01                        cmp ecx, 1
00AFABBC  E9 89 00 00 00                  jmp 0x140afac4a
00AFABC1  41 83 C4 20                     add r12d, 0x20
00AFABC5  45 3B E7                        cmp r12d, r15d
00AFABC8  0F 87 01 03 00 00               ja 0x140afaecf
00AFABCE  83 F8 0A                        cmp eax, 0xa
00AFABD1  75 09                           jne 0x140afabdc
00AFABD3  F3 0F 10 07                     movss xmm0, dword ptr [rdi]
00AFABD7  0F 5A C0                        cvtps2pd xmm0, xmm0
00AFABDA  EB 04                           jmp 0x140afabe0
00AFABDC  F2 0F 10 07                     movsd xmm0, qword ptr [rdi]
00AFABE0  F2 0F 11 44 24 30               movsd qword ptr [rsp + 0x30], xmm0
00AFABE6  48 8D 05 F3 32 01 00            lea rax, [rip + 0x132f3]
00AFABED  E9 7C FF FF FF                  jmp 0x140afab6e
00AFABF2  41 83 C4 28                     add r12d, 0x28
00AFABF6  45 3B E7                        cmp r12d, r15d
00AFABF9  0F 87 D0 02 00 00               ja 0x140afaecf
00AFABFF  48 8B 07                        mov rax, qword ptr [rdi]
00AFAC02  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AFAC07  48 8D 05 B2 32 01 00            lea rax, [rip + 0x132b2]
00AFAC0E  E9 5B FF FF FF                  jmp 0x140afab6e
00AFAC13  83 F8 14                        cmp eax, 0x14
00AFAC16  0F 87 87 00 00 00               ja 0x140afaca3
00AFAC1C  0F 84 9E 00 00 00               je 0x140afacc0
00AFAC22  83 E8 0E                        sub eax, 0xe
00AFAC25  0F 84 A4 02 00 00               je 0x140afaecf
00AFAC2B  83 E8 01                        sub eax, 1
00AFAC2E  0F 84 9B 02 00 00               je 0x140afaecf
00AFAC34  83 E8 01                        sub eax, 1
00AFAC37  0F 84 92 02 00 00               je 0x140afaecf
00AFAC3D  83 E8 01                        sub eax, 1
00AFAC40  74 13                           je 0x140afac55
00AFAC42  83 E8 01                        sub eax, 1
00AFAC45  74 79                           je 0x140afacc0
00AFAC47  83 F8 01                        cmp eax, 1
00AFAC4A  0F 84 7F 02 00 00               je 0x140afaecf
00AFAC50  E9 E7 00 00 00                  jmp 0x140afad3c
00AFAC55  40 38 37                        cmp byte ptr [rdi], sil
00AFAC58  48 8D 0D 11 33 01 00            lea rcx, [rip + 0x13311]
00AFAC5F  4C 8D 05 FA 32 01 00            lea r8, [rip + 0x132fa]
00AFAC66  4C 0F 45 C1                     cmovne r8, rcx
00AFAC6A  48 FF C6                        inc rsi
00AFAC6D  66 45 39 14 70                  cmp word ptr [r8 + rsi*2], r10w
00AFAC72  75 F6                           jne 0x140afac6a
00AFAC74  45 8D 24 74                     lea r12d, [r12 + rsi*2]
00AFAC78  45 3B E7                        cmp r12d, r15d
00AFAC7B  0F 87 4E 02 00 00               ja 0x140afaecf
00AFAC81  44 89 4C 24 28                  mov dword ptr [rsp + 0x28], r9d
00AFAC86  48 8D 45 F7                     lea rax, [rbp - 9]
00AFAC8A  4C 8D 4D FF                     lea r9, [rbp - 1]
00AFAC8E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AFAC93  49 8B D6                        mov rdx, r14
00AFAC96  49 8B CD                        mov rcx, r13
00AFAC99  E8 EE 9B 95 FF                  call 0x14045488c
00AFAC9E  E9 E8 FE FF FF                  jmp 0x140afab8b
00AFACA3  83 E8 15                        sub eax, 0x15
00AFACA6  0F 84 23 02 00 00               je 0x140afaecf
00AFACAC  83 E8 01                        sub eax, 1
00AFACAF  74 5A                           je 0x140afad0b
00AFACB1  83 E8 01                        sub eax, 1
00AFACB4  74 55                           je 0x140afad0b
00AFACB6  83 E8 01                        sub eax, 1
00AFACB9  74 50                           je 0x140afad0b
00AFACBB  83 F8 01                        cmp eax, 1
00AFACBE  75 7C                           jne 0x140afad3c
00AFACC0  E8 8B 84 BA FF                  call 0x1406a3150
00AFACC5  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
00AFACC9  33 FF                           xor edi, edi
00AFACCB  48 8B 49 28                     mov rcx, qword ptr [rcx + 0x28]
00AFACCF  48 FF C6                        inc rsi
00AFACD2  66 39 3C 71                     cmp word ptr [rcx + rsi*2], di
00AFACD6  75 F7                           jne 0x140afaccf
00AFACD8  45 8D 24 74                     lea r12d, [r12 + rsi*2]
00AFACDC  85 C0                           test eax, eax
00AFACDE  74 04                           je 0x140aface4
00AFACE0  41 83 C4 04                     add r12d, 4
00AFACE4  45 3B E7                        cmp r12d, r15d
00AFACE7  0F 87 E2 01 00 00               ja 0x140afaecf
00AFACED  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00AFACF2  48 8D 05 87 32 01 00            lea rax, [rip + 0x13287]
00AFACF9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AFACFE  C7 44 24 20 00 04 00 00         mov dword ptr [rsp + 0x20], 0x400
00AFAD06  E9 6D FE FF FF                  jmp 0x140afab78
00AFAD0B  41 83 C4 18                     add r12d, 0x18
00AFAD0F  45 3B E7                        cmp r12d, r15d
00AFAD12  0F 87 B7 01 00 00               ja 0x140afaecf
00AFAD18  8B 07                           mov eax, dword ptr [rdi]
00AFAD1A  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00AFAD1E  48 8D 05 2B 2F 01 00            lea rax, [rip + 0x12f2b]
00AFAD25  E9 44 FE FF FF                  jmp 0x140afab6e
00AFAD2A  3D 0D 10 00 00                  cmp eax, 0x100d
00AFAD2F  0F 84 8F 00 00 00               je 0x140afadc4
00AFAD35  3D 12 20 00 00                  cmp eax, 0x2012
00AFAD3A  74 7D                           je 0x140afadb9
00AFAD3C  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AFAD41  E9 89 01 00 00                  jmp 0x140afaecf
00AFAD46  48 8B C6                        mov rax, rsi
00AFAD49  48 FF C0                        inc rax
00AFAD4C  66 44 39 14 47                  cmp word ptr [rdi + rax*2], r10w
00AFAD51  75 F6                           jne 0x140afad49
00AFAD53  45 8D 24 44                     lea r12d, [r12 + rax*2]
00AFAD57  41 83 C4 04                     add r12d, 4
00AFAD5B  45 3B E7                        cmp r12d, r15d
00AFAD5E  77 3A                           ja 0x140afad9a
00AFAD60  48 8D 05 29 32 01 00            lea rax, [rip + 0x13229]
00AFAD67  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AFAD6C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AFAD71  4C 8D 45 FF                     lea r8, [rbp - 1]
00AFAD75  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00AFAD7A  49 8B D6                        mov rdx, r14
00AFAD7D  4C 8D 4D F7                     lea r9, [rbp - 9]
00AFAD81  49 8B CD                        mov rcx, r13
00AFAD84  E8 4B 6D 96 FF                  call 0x140461ad4
00AFAD89  45 33 D2                        xor r10d, r10d
00AFAD8C  8B D8                           mov ebx, eax
00AFAD8E  85 C0                           test eax, eax
00AFAD90  0F 88 50 01 00 00               js 0x140afaee6
00AFAD96  4C 8B 6D FF                     mov r13, qword ptr [rbp - 1]
00AFAD9A  48 8B C6                        mov rax, rsi
00AFAD9D  48 FF C0                        inc rax
00AFADA0  66 44 39 14 47                  cmp word ptr [rdi + rax*2], r10w
00AFADA5  75 F6                           jne 0x140afad9d
00AFADA7  4C 8B 75 F7                     mov r14, qword ptr [rbp - 9]
00AFADAB  48 8D 3C 47                     lea rdi, [rdi + rax*2]
00AFADAF  48 83 C7 02                     add rdi, 2
00AFADB3  41 B9 00 04 00 00               mov r9d, 0x400
00AFADB9  66 44 39 17                     cmp word ptr [rdi], r10w
00AFADBD  75 87                           jne 0x140afad46
00AFADBF  E9 0B 01 00 00                  jmp 0x140afaecf
00AFADC4  49 8B CA                        mov rcx, r10
00AFADC7  48 89 4D 77                     mov qword ptr [rbp + 0x77], rcx
00AFADCB  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
00AFADCF  41 83 C4 50                     add r12d, 0x50
00AFADD3  0F 10 04 08                     movups xmm0, xmmword ptr [rax + rcx]
00AFADD7  F3 0F 7F 45 07                  movdqu xmmword ptr [rbp + 7], xmm0
00AFADDC  45 3B E7                        cmp r12d, r15d
00AFADDF  0F 87 D6 00 00 00               ja 0x140afaebb
00AFADE5  48 8B 4D 0F                     mov rcx, qword ptr [rbp + 0xf]
00AFADE9  4C 8B 5D 07                     mov r11, qword ptr [rbp + 7]
00AFADED  48 8B C1                        mov rax, rcx
00AFADF0  48 C1 E8 30                     shr rax, 0x30
00AFADF4  4C 8B F9                        mov r15, rcx
00AFADF7  44 0F B6 F0                     movzx r14d, al
00AFADFB  49 8B D3                        mov rdx, r11
00AFADFE  44 0F B6 C9                     movzx r9d, cl
00AFAE02  48 8B C1                        mov rax, rcx
00AFAE05  48 C1 E8 28                     shr rax, 0x28
00AFAE09  0F B6 F0                        movzx esi, al
00AFAE0C  48 8B C1                        mov rax, rcx
00AFAE0F  48 C1 E8 20                     shr rax, 0x20
00AFAE13  0F B6 F8                        movzx edi, al
00AFAE16  48 8B C1                        mov rax, rcx
00AFAE19  48 C1 E8 18                     shr rax, 0x18
00AFAE1D  0F B6 D8                        movzx ebx, al
00AFAE20  48 8B C1                        mov rax, rcx
00AFAE23  48 C1 E8 10                     shr rax, 0x10
00AFAE27  44 0F B6 D0                     movzx r10d, al
00AFAE2B  48 8B C1                        mov rax, rcx
00AFAE2E  48 C1 E8 08                     shr rax, 8
00AFAE32  44 0F B6 C0                     movzx r8d, al
00AFAE36  49 8B C3                        mov rax, r11
00AFAE39  48 C1 E8 20                     shr rax, 0x20
00AFAE3D  0F B7 C8                        movzx ecx, ax
00AFAE40  48 8D 05 A9 30 01 00            lea rax, [rip + 0x130a9]
00AFAE47  48 C1 EA 30                     shr rdx, 0x30
00AFAE4B  49 C1 EF 38                     shr r15, 0x38
00AFAE4F  44 89 BC 24 80 00 00 00         mov dword ptr [rsp + 0x80], r15d
00AFAE57  44 89 74 24 78                  mov dword ptr [rsp + 0x78], r14d
00AFAE5C  89 74 24 70                     mov dword ptr [rsp + 0x70], esi
00AFAE60  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
00AFAE64  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
00AFAE68  44 89 54 24 58                  mov dword ptr [rsp + 0x58], r10d
00AFAE6D  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
00AFAE72  4C 8D 45 FF                     lea r8, [rbp - 1]
00AFAE76  44 89 4C 24 48                  mov dword ptr [rsp + 0x48], r9d
00AFAE7B  4C 8D 4D F7                     lea r9, [rbp - 9]
00AFAE7F  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00AFAE83  48 8B 55 F7                     mov rdx, qword ptr [rbp - 9]
00AFAE87  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
00AFAE8B  49 8B CD                        mov rcx, r13
00AFAE8E  44 89 5C 24 30                  mov dword ptr [rsp + 0x30], r11d
00AFAE93  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AFAE98  C7 44 24 20 00 04 00 00         mov dword ptr [rsp + 0x20], 0x400
00AFAEA0  E8 2F 6C 96 FF                  call 0x140461ad4
00AFAEA5  8B D8                           mov ebx, eax
00AFAEA7  85 C0                           test eax, eax
00AFAEA9  78 3B                           js 0x140afaee6
00AFAEAB  4C 8B 6D FF                     mov r13, qword ptr [rbp - 1]
00AFAEAF  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
00AFAEB3  44 8B 7D 6F                     mov r15d, dword ptr [rbp + 0x6f]
00AFAEB7  48 8B 55 67                     mov rdx, qword ptr [rbp + 0x67]
00AFAEBB  8B 42 24                        mov eax, dword ptr [rdx + 0x24]
00AFAEBE  48 83 C1 10                     add rcx, 0x10
00AFAEC2  48 89 4D 77                     mov qword ptr [rbp + 0x77], rcx
00AFAEC6  48 3B C8                        cmp rcx, rax
00AFAEC9  0F 82 FC FE FF FF               jb 0x140afadcb
00AFAECF  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00AFAED3  48 85 C0                        test rax, rax
00AFAED6  74 03                           je 0x140afaedb
00AFAED8  44 89 20                        mov dword ptr [rax], r12d
00AFAEDB  45 3B E7                        cmp r12d, r15d
00AFAEDE  B8 23 00 00 C0                  mov eax, 0xc0000023
00AFAEE3  0F 47 D8                        cmova ebx, eax
00AFAEE6  8B C3                           mov eax, ebx
00AFAEE8  48 81 C4 B8 00 00 00            add rsp, 0xb8
00AFAEEF  41 5F                           pop r15
00AFAEF1  41 5E                           pop r14
00AFAEF3  41 5D                           pop r13
00AFAEF5  41 5C                           pop r12
00AFAEF7  5F                              pop rdi
00AFAEF8  5E                              pop rsi
00AFAEF9  5B                              pop rbx
00AFAEFA  5D                              pop rbp
00AFAEFB  C3                              ret
00AFAEFC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ConvertDevpropertyToString(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m88;
    unsigned int v_stack_m90;
    unsigned int v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (184);
    result = 0;
    *(unsigned int *)(v_rsp - 95 + 119) = 0;
    if (a2 >= ((unsigned int)(result + 2))) {
        *(unsigned __int16 *)(a3) = 0;
    }
    *(unsigned __int64 *)(v_rsp - 95 - 1) = a3;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = (unsigned int)(a2);
    result = ConvertDevpropcompkeyToString(a1, a3, (unsigned int)((unsigned int)((unsigned int)(a2))), v_rsp - 95 + 119);
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)((unsigned int)((unsigned int)(result)) + (unsigned int)(0x80000000ULL) * 1))) != 0) goto loc_00AFA828;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)((unsigned int)(0xC0000023ULL)))) goto loc_00AFAEE6;
loc_00AFA828:
    v_r10 = 0;
    result = ((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119))) + (-2);
    v_rdi = result + 2;
    v_r13 = a3;
    v_r14 = (unsigned int)(a2);
    if (((unsigned int)(a2)) >= result) {
        v_rdi = (result + 2) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)))));
        v_r14 = ((unsigned int)(a2)) + (v_rdi);
        result = (result) >> (1);
        *(unsigned __int64 *)(v_rsp - 95 - 9) = v_r14;
        v_r13 = a3 + result * 2;
        *(unsigned __int64 *)(v_rsp - 95 - 1) = v_r13;
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32)))) > ((unsigned int)((unsigned int)(0x1003ULL)))) goto loc_00AFAA3A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32)))) == ((unsigned int)((unsigned int)(0x1003ULL)))) goto loc_00AFAA31;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32)))) > 13) goto loc_00AFA971;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32)))) == 13) goto loc_00AFA965;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32)))) > 6) goto loc_00AFA8FB;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32)))) == 6) goto loc_00AFA8EF;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32))) == 0) goto loc_00AFA8E3;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32))) - (1));
    if (condition_is_equal) goto loc_00AFA8D7;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFA8CB;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFA8BF;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFA8B3;
    if (((unsigned int)(result)) != 1) goto loc_00AFAA48;
    goto loc_00AFAA62;
loc_00AFA8B3:
    goto loc_00AFAA62;
loc_00AFA8BF:
    goto loc_00AFAA62;
loc_00AFA8CB:
    goto loc_00AFAA62;
loc_00AFA8D7:
    goto loc_00AFAA62;
loc_00AFA8E3:
    goto loc_00AFAA62;
loc_00AFA8EF:
    goto loc_00AFAA62;
loc_00AFA8FB:
    result = (unsigned int)((result) - (7));
    if (condition_is_equal) goto loc_00AFA959;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFA94D;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFA941;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFA935;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFA929;
    if (((unsigned int)(result)) != 1) goto loc_00AFAA48;
    goto loc_00AFAA62;
loc_00AFA929:
    goto loc_00AFAA62;
loc_00AFA935:
    goto loc_00AFAA62;
loc_00AFA941:
    goto loc_00AFAA62;
loc_00AFA94D:
    goto loc_00AFAA62;
loc_00AFA959:
    goto loc_00AFAA62;
loc_00AFA965:
    goto loc_00AFAA62;
loc_00AFA971:
    if (((unsigned int)(result)) > 20) goto loc_00AFA9EB;
    if (((unsigned int)(result)) == 20) goto loc_00AFA9E2;
    result = (unsigned int)((result) - (14));
    if (condition_is_equal) goto loc_00AFA9D6;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFA9CA;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFA9BE;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFA9B2;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFA9A6;
    if (((unsigned int)(result)) != 1) goto loc_00AFAA48;
    goto loc_00AFAA62;
loc_00AFA9A6:
    goto loc_00AFAA62;
loc_00AFA9B2:
    goto loc_00AFAA62;
loc_00AFA9BE:
    goto loc_00AFAA62;
loc_00AFA9CA:
    goto loc_00AFAA62;
loc_00AFA9D6:
    goto loc_00AFAA62;
loc_00AFA9E2:
    goto loc_00AFAA62;
loc_00AFA9EB:
    result = (unsigned int)((result) - (21));
    if (condition_is_equal) goto loc_00AFAA28;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFAA1F;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFAA16;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFAA0D;
    if (((unsigned int)(result)) != 1) goto loc_00AFAA48;
    goto loc_00AFAA62;
loc_00AFAA0D:
    goto loc_00AFAA62;
loc_00AFAA16:
    goto loc_00AFAA62;
loc_00AFAA1F:
    goto loc_00AFAA62;
loc_00AFAA28:
    goto loc_00AFAA62;
loc_00AFAA31:
    goto loc_00AFAA62;
loc_00AFAA3A:
    if (((unsigned int)(result)) == 0x100DULL) goto loc_00AFAA5B;
    if (((unsigned int)(result)) == 0x2012ULL) goto loc_00AFAA52;
loc_00AFAA48:
    goto loc_00AFAEE6;
loc_00AFAA52:
    goto loc_00AFAA62;
loc_00AFAA5B:
loc_00AFAA62:
    v_rsi = (v_rsi) | (-1);
loc_00AFAA69:
    result = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(v_rip + 78606 + result * 2)) != 0) goto loc_00AFAA69;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)) + 2 - 2 + result * 2)) > ((unsigned int)((unsigned int)(a2)))) goto loc_00AFAAC7;
    v_stack_mD0 = (unsigned int)((unsigned int)(0x400ULL));
    v_stack_mD8 = v_rsp - 95 - 9;
    result = RtlStringCbCopyExW(v_r13, v_r14, v_rip + 78606, v_rsp - 95 - 1);
    v_r10 = 0;
    if (sign_flag) goto loc_00AFAEE6;
loc_00AFAAC7:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 36)) <= 0) goto loc_00AFAECF;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 40) == 0) goto loc_00AFAECF;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32)))) > ((unsigned int)((unsigned int)(0x1003ULL)))) goto loc_00AFAD2A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32)))) == ((unsigned int)((unsigned int)(0x1003ULL)))) goto loc_00AFAECF;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32)))) > 13) goto loc_00AFAC13;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32)))) == 13) goto loc_00AFADC4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32)))) > 6) goto loc_00AFAB9A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32)))) == 6) goto loc_00AFAD0B;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32))) == 0) goto loc_00AFAA48;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 32))) - (1));
    if (condition_is_equal) goto loc_00AFAA48;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFAB53;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFAB53;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFAB36;
    if (((unsigned int)(result)) != 1) goto loc_00AFAD3C;
loc_00AFAB36:
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 95 + 119)) + 2 - 2 + result * 2) + (16));
    if (((unsigned int)(v_r12)) > ((unsigned int)((unsigned int)(a2)))) goto loc_00AFAECF;
    v_stack_mC8 = (unsigned int)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 40))));
    goto loc_00AFAB6E;
loc_00AFAB53:
    v_r12 = (unsigned int)((v_r12) + (12));
    if (((unsigned int)(v_r12)) > ((unsigned int)((unsigned int)(a2)))) goto loc_00AFAECF;
    v_stack_mC8 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 40)));
loc_00AFAB6E:
    v_stack_mD0 = v_rip + 77986;
    v_stack_mD8 = (unsigned int)((unsigned int)(0x400ULL));
loc_00AFAB78:
    result = RtlStringCbPrintfExW(*(unsigned __int64 *)(v_rsp - 95 - 1), *(unsigned __int64 *)(v_rsp - 95 - 9), v_rsp - 95 - 1, v_rsp - 95 - 9);
loc_00AFAB8B:
    if (sign_flag) goto loc_00AFAEE6;
    goto loc_00AFAECF;
loc_00AFAB9A:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) - (7));
    if (condition_is_equal) goto loc_00AFAD0B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AFABF2;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AFABF2;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AFABC1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AFABC1;
    goto loc_00AFAC4A;
loc_00AFABC1:
    v_r12 = (unsigned int)((v_r12) + (32));
    if (((unsigned int)(v_r12)) > ((unsigned int)((unsigned int)(a2)))) goto loc_00AFAECF;
    if (((unsigned int)(result)) != 10) goto loc_00AFABDC;
    goto loc_00AFABE0;
loc_00AFABDC:
loc_00AFABE0:
    v_stack_mC8 = v_xmm0;
    goto loc_00AFAB6E;
loc_00AFABF2:
    v_r12 = (unsigned int)((v_r12) + (40));
    if (((unsigned int)(v_r12)) > ((unsigned int)((unsigned int)(a2)))) goto loc_00AFAECF;
    v_stack_mC8 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 40));
    goto loc_00AFAB6E;
loc_00AFAC13:
    if (((unsigned int)(v_rip + 78514)) > 20) goto loc_00AFACA3;
    if (((unsigned int)(v_rip + 78514)) == 20) goto loc_00AFACC0;
    result = (unsigned int)((v_rip + 78514) - (14));
    if (condition_is_equal) goto loc_00AFAECF;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFAECF;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFAECF;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFAC55;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFACC0;
loc_00AFAC4A:
    if (((unsigned int)(result)) == 1) goto loc_00AFAECF;
    goto loc_00AFAD3C;
loc_00AFAC55:
    a3 = v_rip + 78586;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 40))) != ((unsigned __int8)(v_rsi))) { a3 = v_rip + 78609; }
loc_00AFAC6A:
    v_rsi = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(a3 + v_rsi * 2)) != 0) goto loc_00AFAC6A;
    if (((unsigned int)(v_r12 + v_rsi * 2)) > ((unsigned int)((unsigned int)(a2)))) goto loc_00AFAECF;
    v_stack_mD0 = (unsigned int)(v_rsp - 95 - 9);
    v_stack_mD8 = v_rsp - 95 - 9;
    result = RtlStringCbCopyExW(*(unsigned __int64 *)(v_rsp - 95 - 1), *(unsigned __int64 *)(v_rsp - 95 - 9), a3, v_rsp - 95 - 1);
    goto loc_00AFAB8B;
loc_00AFACA3:
    result = (unsigned int)((result) - (21));
    if (condition_is_equal) goto loc_00AFAECF;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFAD0B;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFAD0B;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00AFAD0B;
    if (((unsigned int)(result)) != 1) goto loc_00AFAD3C;
loc_00AFACC0:
    result = Feature_KernelPnP_DevfilterLogging__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(v_rsp - 95 - 1), *(unsigned __int64 *)(v_rsp - 95 - 9), a3, v_rsp - 95 - 1);
    v_rdi = 0;
loc_00AFACCF:
    v_rsi = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 40) + v_rsi * 2)) != 0) goto loc_00AFACCF;
    v_r12 = v_r12 + v_rsi * 2 + v_rsi * 2;
    if ((unsigned int)(result) != 0) {
        v_r12 = (unsigned int)((v_r12 + v_rsi * 2 + v_rsi * 2) + (4));
    }
    if (((unsigned int)(v_r12)) > ((unsigned int)((unsigned int)(a2)))) goto loc_00AFAECF;
    v_stack_mC8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 40);
    v_stack_mD0 = v_rip + 78471;
    v_stack_mD8 = 0x400ULL;
    goto loc_00AFAB78;
loc_00AFAD0B:
    v_r12 = (unsigned int)((v_r12) + (24));
    if (((unsigned int)(v_r12)) > ((unsigned int)((unsigned int)(a2)))) goto loc_00AFAECF;
    v_stack_mC8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)));
    goto loc_00AFAB6E;
loc_00AFAD2A:
    if (((unsigned int)(v_rip + 77611)) == 0x100DULL) goto loc_00AFADC4;
    if (((unsigned int)(v_rip + 77611)) == 0x2012ULL) goto loc_00AFADB9;
loc_00AFAD3C:
    goto loc_00AFAECF;
loc_00AFAD46:
loc_00AFAD49:
    result = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(v_rdi + result * 2)) != 0) goto loc_00AFAD49;
    v_r12 = (unsigned int)((v_r12 + result * 2) + (4));
    if (((unsigned int)(v_r12)) > ((unsigned int)((unsigned int)(a2)))) goto loc_00AFAD9A;
    v_stack_mC8 = 0;
    v_stack_mD0 = v_rip + 78377;
    v_stack_mD8 = (unsigned int)(v_rsp - 95 - 1);
    result = RtlStringCbPrintfExW(*(unsigned __int64 *)(v_rsp - 95 - 1), *(unsigned __int64 *)(v_rsp - 95 - 9), v_rsp - 95 - 1, v_rsp - 95 - 9);
    v_r10 = 0;
    if (sign_flag) goto loc_00AFAEE6;
loc_00AFAD9A:
loc_00AFAD9D:
    result = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(v_rdi + result * 2)) != 0) goto loc_00AFAD9D;
    v_rdi = (v_rdi + result * 2) + (2);
loc_00AFADB9:
    if ((*(unsigned __int16 *)(v_rdi)) != 0) goto loc_00AFAD46;
    goto loc_00AFAECF;
loc_00AFADC4:
    *(unsigned __int64 *)(v_rsp - 95 + 119) = 0;
loc_00AFADCB:
    v_r12 = (unsigned int)((v_r12) + (80));
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_xmm0;
    if (((unsigned int)(v_r12)) > ((unsigned int)((unsigned int)(a2)))) goto loc_00AFAEBB;
    result = (*(unsigned __int64 *)(v_rsp - 95 + 15)) >> (48);
    result = (*(unsigned __int64 *)(v_rsp - 95 + 15)) >> (40);
    result = (*(unsigned __int64 *)(v_rsp - 95 + 15)) >> (32);
    result = (*(unsigned __int64 *)(v_rsp - 95 + 15)) >> (24);
    result = (*(unsigned __int64 *)(v_rsp - 95 + 15)) >> (16);
    result = (*(unsigned __int64 *)(v_rsp - 95 + 15)) >> (8);
    result = (*(unsigned __int64 *)(v_rsp - 95 + 7)) >> (32);
    a2 = (*(unsigned __int64 *)(v_rsp - 95 + 7)) >> (48);
    v_r15 = (*(unsigned __int64 *)(v_rsp - 95 + 15)) >> (56);
    v_stack_m78 = (unsigned int)(v_r15);
    v_stack_m80 = (unsigned int)((unsigned __int8)(result));
    v_stack_m88 = (unsigned int)((unsigned __int8)(result));
    v_stack_m90 = (unsigned int)((unsigned __int8)(result));
    v_stack_m98 = (unsigned int)((unsigned __int8)(result));
    v_stack_mA0 = (unsigned int)((unsigned __int8)(result));
    v_stack_mA8 = (unsigned int)((unsigned __int8)(result));
    v_stack_mB0 = (unsigned int)((unsigned __int8)(*(unsigned __int64 *)(v_rsp - 95 + 15)));
    v_stack_mB8 = a2;
    v_stack_mC0 = (unsigned int)((unsigned __int16)(result));
    v_stack_mC8 = (unsigned int)(*(unsigned __int64 *)(v_rsp - 95 + 7));
    v_stack_mD0 = v_rip + 77993;
    v_stack_mD8 = 0x400ULL;
    result = RtlStringCbPrintfExW(*(unsigned __int64 *)(v_rsp - 95 - 1), *(unsigned __int64 *)(v_rsp - 95 - 9), v_rsp - 95 - 1, v_rsp - 95 - 9);
    if (sign_flag) goto loc_00AFAEE6;
loc_00AFAEBB:
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 119)) + (16);
    *(unsigned __int64 *)(v_rsp - 95 + 119) = a1;
    if (a1 < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 103) + 36)))) goto loc_00AFADCB;
loc_00AFAECF:
    if (*(unsigned __int64 *)(v_rsp - 95 + 127) != 0) {
        *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 95 + 127)) = (unsigned int)(v_r12);
    }
    v_rbx = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(v_r12)) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 95 + 111))))) { v_rbx = (unsigned int)((unsigned int)(0xC0000023ULL)); }
loc_00AFAEE6:
    v_rsp = (v_rsp) + (184);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t ConvertDevpropertyToString(int64_t Arg1, int32_t Arg2, void *Arg3, int64_t Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m88;
    uint32_t v_stack_m90;
    uint32_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (184);
    result = 0;
    *(uint32_t *)(local_rsp - 0x5F + 0x77) = 0;
    if (Arg2 >= ((uint32_t)(result + 2))) {
        *(uint16_t *)(arg3) = 0;
    }
    *(void **)(local_rsp - 0x5F - 0x1) = Arg3;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = (uint32_t)(Arg2);
    result = ConvertDevpropcompkeyToString(Arg1, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg2))), local_rsp - 95 + 119);
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)((uint32_t)((uint32_t)(result)) + (uint32_t)(0x80000000ULL) * 1))) != 0) goto loc_00AFA828;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)((uint32_t)(0xC0000023ULL)))) goto loc_00AFAEE6;
loc_00AFA828:
    local_r10 = 0;
    result = ((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77))) + (-2);
    local_rdi = result + 2;
    local_r13 = Arg3;
    local_r14 = (uint32_t)(Arg2);
    if (((uint32_t)(Arg2)) >= result) {
        local_rdi = (result + 2) - ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)))));
        local_r14 = ((uint32_t)(Arg2)) + (local_rdi);
        result = (result) >> (1);
        *(uint64_t *)(local_rsp - 0x5F - 0x9) = local_r14;
        local_r13 = Arg3 + result * 2;
        *(uint64_t *)(local_rsp - 0x5F - 0x1) = local_r13;
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20)))) > ((uint32_t)((uint32_t)(0x1003ULL)))) goto loc_00AFAA3A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20)))) == ((uint32_t)((uint32_t)(0x1003ULL)))) goto loc_00AFAA31;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20)))) > 13) goto loc_00AFA971;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20)))) == 13) goto loc_00AFA965;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20)))) > 6) goto loc_00AFA8FB;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20)))) == 6) goto loc_00AFA8EF;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20))) == 0) goto loc_00AFA8E3;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20))) - (1));
    if (condition_is_equal) goto loc_00AFA8D7;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFA8CB;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFA8BF;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFA8B3;
    if (((uint32_t)(result)) != 1) goto loc_00AFAA48;
    goto loc_00AFAA62;
loc_00AFA8B3:
    goto loc_00AFAA62;
loc_00AFA8BF:
    goto loc_00AFAA62;
loc_00AFA8CB:
    goto loc_00AFAA62;
loc_00AFA8D7:
    goto loc_00AFAA62;
loc_00AFA8E3:
    goto loc_00AFAA62;
loc_00AFA8EF:
    goto loc_00AFAA62;
loc_00AFA8FB:
    result = (uint32_t)((result) - (7));
    if (condition_is_equal) goto loc_00AFA959;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFA94D;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFA941;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFA935;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFA929;
    if (((uint32_t)(result)) != 1) goto loc_00AFAA48;
    goto loc_00AFAA62;
loc_00AFA929:
    goto loc_00AFAA62;
loc_00AFA935:
    goto loc_00AFAA62;
loc_00AFA941:
    goto loc_00AFAA62;
loc_00AFA94D:
    goto loc_00AFAA62;
loc_00AFA959:
    goto loc_00AFAA62;
loc_00AFA965:
    goto loc_00AFAA62;
loc_00AFA971:
    if (((uint32_t)(result)) > 20) goto loc_00AFA9EB;
    if (((uint32_t)(result)) == 20) goto loc_00AFA9E2;
    result = (uint32_t)((result) - (14));
    if (condition_is_equal) goto loc_00AFA9D6;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFA9CA;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFA9BE;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFA9B2;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFA9A6;
    if (((uint32_t)(result)) != 1) goto loc_00AFAA48;
    goto loc_00AFAA62;
loc_00AFA9A6:
    goto loc_00AFAA62;
loc_00AFA9B2:
    goto loc_00AFAA62;
loc_00AFA9BE:
    goto loc_00AFAA62;
loc_00AFA9CA:
    goto loc_00AFAA62;
loc_00AFA9D6:
    goto loc_00AFAA62;
loc_00AFA9E2:
    goto loc_00AFAA62;
loc_00AFA9EB:
    result = (uint32_t)((result) - (21));
    if (condition_is_equal) goto loc_00AFAA28;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFAA1F;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFAA16;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFAA0D;
    if (((uint32_t)(result)) != 1) goto loc_00AFAA48;
    goto loc_00AFAA62;
loc_00AFAA0D:
    goto loc_00AFAA62;
loc_00AFAA16:
    goto loc_00AFAA62;
loc_00AFAA1F:
    goto loc_00AFAA62;
loc_00AFAA28:
    goto loc_00AFAA62;
loc_00AFAA31:
    goto loc_00AFAA62;
loc_00AFAA3A:
    if (((uint32_t)(result)) == 0x100DULL) goto loc_00AFAA5B;
    if (((uint32_t)(result)) == 0x2012ULL) goto loc_00AFAA52;
loc_00AFAA48:
    goto loc_00AFAEE6;
loc_00AFAA52:
    goto loc_00AFAA62;
loc_00AFAA5B:
loc_00AFAA62:
    local_rsi = (local_rsi) | (-1);
loc_00AFAA69:
    result = (local_rsi) + 1;
    if ((*(uint16_t *)(v_rip + 0x1330E + result * 2)) != 0) goto loc_00AFAA69;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)) + 2 - 2 + result * 2)) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_00AFAAC7;
    v_stack_mD0 = (uint32_t)((uint32_t)(0x400ULL));
    v_stack_mD8 = local_rsp - 95 - 9;
    result = RtlStringCbCopyExW(local_r13, local_r14, v_rip + 78606, local_rsp - 95 - 1);
    local_r10 = 0;
    if (sign_flag) goto loc_00AFAEE6;
loc_00AFAAC7:
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x24)) <= 0) goto loc_00AFAECF;
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x28) == 0) goto loc_00AFAECF;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20)))) > ((uint32_t)((uint32_t)(0x1003ULL)))) goto loc_00AFAD2A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20)))) == ((uint32_t)((uint32_t)(0x1003ULL)))) goto loc_00AFAECF;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20)))) > 13) goto loc_00AFAC13;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20)))) == 13) goto loc_00AFADC4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20)))) > 6) goto loc_00AFAB9A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20)))) == 6) goto loc_00AFAD0B;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20))) == 0) goto loc_00AFAA48;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x20))) - (1));
    if (condition_is_equal) goto loc_00AFAA48;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFAB53;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFAB53;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFAB36;
    if (((uint32_t)(result)) != 1) goto loc_00AFAD3C;
loc_00AFAB36:
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x77)) + 2 - 2 + result * 2) + (16));
    if (((uint32_t)(local_r12)) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_00AFAECF;
    v_stack_mC8 = (uint32_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x28))));
    goto loc_00AFAB6E;
loc_00AFAB53:
    local_r12 = (uint32_t)((local_r12) + (12));
    if (((uint32_t)(local_r12)) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_00AFAECF;
    v_stack_mC8 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x28)));
loc_00AFAB6E:
    v_stack_mD0 = v_rip + 77986;
    v_stack_mD8 = (uint32_t)((uint32_t)(0x400ULL));
loc_00AFAB78:
    result = RtlStringCbPrintfExW(*(uint64_t *)(local_rsp - 0x5F - 0x1), *(uint64_t *)(local_rsp - 0x5F - 0x9), local_rsp - 95 - 1, local_rsp - 95 - 9);
loc_00AFAB8B:
    if (sign_flag) goto loc_00AFAEE6;
    goto loc_00AFAECF;
loc_00AFAB9A:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) - (7));
    if (condition_is_equal) goto loc_00AFAD0B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AFABF2;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AFABF2;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AFABC1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AFABC1;
    goto loc_00AFAC4A;
loc_00AFABC1:
    local_r12 = (uint32_t)((local_r12) + (32));
    if (((uint32_t)(local_r12)) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_00AFAECF;
    if (((uint32_t)(result)) != 10) goto loc_00AFABDC;
    goto loc_00AFABE0;
loc_00AFABDC:
loc_00AFABE0:
    v_stack_mC8 = v_xmm0;
    goto loc_00AFAB6E;
loc_00AFABF2:
    local_r12 = (uint32_t)((local_r12) + (40));
    if (((uint32_t)(local_r12)) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_00AFAECF;
    v_stack_mC8 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x28));
    goto loc_00AFAB6E;
loc_00AFAC13:
    if (((uint32_t)(v_rip + 78514)) > 20) goto loc_00AFACA3;
    if (((uint32_t)(v_rip + 78514)) == 20) goto loc_00AFACC0;
    result = (uint32_t)((v_rip + 78514) - (14));
    if (condition_is_equal) goto loc_00AFAECF;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFAECF;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFAECF;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFAC55;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFACC0;
loc_00AFAC4A:
    if (((uint32_t)(result)) == 1) goto loc_00AFAECF;
    goto loc_00AFAD3C;
loc_00AFAC55:
    Arg3 = v_rip + 78586;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x28))) != ((uint8_t)(local_rsi))) { Arg3 = v_rip + 78609; }
loc_00AFAC6A:
    local_rsi = (local_rsi) + 1;
    if ((*(uint16_t *)(arg3 + local_rsi * 2)) != 0) goto loc_00AFAC6A;
    if (((uint32_t)(local_r12 + local_rsi * 2)) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_00AFAECF;
    v_stack_mD0 = (uint32_t)(local_rsp - 95 - 9);
    v_stack_mD8 = local_rsp - 95 - 9;
    result = RtlStringCbCopyExW(*(uint64_t *)(local_rsp - 0x5F - 0x1), *(uint64_t *)(local_rsp - 0x5F - 0x9), Arg3, local_rsp - 95 - 1);
    goto loc_00AFAB8B;
loc_00AFACA3:
    result = (uint32_t)((result) - (21));
    if (condition_is_equal) goto loc_00AFAECF;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFAD0B;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFAD0B;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00AFAD0B;
    if (((uint32_t)(result)) != 1) goto loc_00AFAD3C;
loc_00AFACC0:
    result = Feature_KernelPnP_DevfilterLogging__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(local_rsp - 0x5F - 0x1), *(uint64_t *)(local_rsp - 0x5F - 0x9), Arg3, local_rsp - 95 - 1);
    local_rdi = 0;
loc_00AFACCF:
    local_rsi = (local_rsi) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x28) + local_rsi * 2)) != 0) goto loc_00AFACCF;
    local_r12 = local_r12 + local_rsi * 2 + local_rsi * 2;
    if ((uint32_t)(result) != 0) {
        local_r12 = (uint32_t)((local_r12 + local_rsi * 2 + local_rsi * 2) + (4));
    }
    if (((uint32_t)(local_r12)) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_00AFAECF;
    v_stack_mC8 = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x28);
    v_stack_mD0 = v_rip + 78471;
    v_stack_mD8 = 0x400ULL;
    goto loc_00AFAB78;
loc_00AFAD0B:
    local_r12 = (uint32_t)((local_r12) + (24));
    if (((uint32_t)(local_r12)) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_00AFAECF;
    v_stack_mC8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)));
    goto loc_00AFAB6E;
loc_00AFAD2A:
    if (((uint32_t)(v_rip + 77611)) == 0x100DULL) goto loc_00AFADC4;
    if (((uint32_t)(v_rip + 77611)) == 0x2012ULL) goto loc_00AFADB9;
loc_00AFAD3C:
    goto loc_00AFAECF;
loc_00AFAD46:
loc_00AFAD49:
    result = (local_rsi) + 1;
    if ((*(uint16_t *)(local_rdi + result * 2)) != 0) goto loc_00AFAD49;
    local_r12 = (uint32_t)((local_r12 + result * 2) + (4));
    if (((uint32_t)(local_r12)) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_00AFAD9A;
    v_stack_mC8 = 0;
    v_stack_mD0 = v_rip + 78377;
    v_stack_mD8 = (uint32_t)(local_rsp - 95 - 1);
    result = RtlStringCbPrintfExW(*(uint64_t *)(local_rsp - 0x5F - 0x1), *(uint64_t *)(local_rsp - 0x5F - 0x9), local_rsp - 95 - 1, local_rsp - 95 - 9);
    local_r10 = 0;
    if (sign_flag) goto loc_00AFAEE6;
loc_00AFAD9A:
loc_00AFAD9D:
    result = (local_rsi) + 1;
    if ((*(uint16_t *)(local_rdi + result * 2)) != 0) goto loc_00AFAD9D;
    local_rdi = (local_rdi + result * 2) + (2);
loc_00AFADB9:
    if ((*(uint16_t *)(local_rdi)) != 0) goto loc_00AFAD46;
    goto loc_00AFAECF;
loc_00AFADC4:
    *(uint64_t *)(local_rsp - 0x5F + 0x77) = 0;
loc_00AFADCB:
    local_r12 = (uint32_t)((local_r12) + (80));
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = v_xmm0;
    if (((uint32_t)(local_r12)) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_00AFAEBB;
    result = (*(uint64_t *)(local_rsp - 0x5F + 0xF)) >> (48);
    result = (*(uint64_t *)(local_rsp - 0x5F + 0xF)) >> (40);
    result = (*(uint64_t *)(local_rsp - 0x5F + 0xF)) >> (32);
    result = (*(uint64_t *)(local_rsp - 0x5F + 0xF)) >> (24);
    result = (*(uint64_t *)(local_rsp - 0x5F + 0xF)) >> (16);
    result = (*(uint64_t *)(local_rsp - 0x5F + 0xF)) >> (8);
    result = (*(uint64_t *)(local_rsp - 0x5F + 0x7)) >> (32);
    Arg2 = (*(uint64_t *)(local_rsp - 0x5F + 0x7)) >> (48);
    local_r15 = (*(uint64_t *)(local_rsp - 0x5F + 0xF)) >> (56);
    v_stack_m78 = (uint32_t)(local_r15);
    v_stack_m80 = (uint32_t)((uint8_t)(result));
    v_stack_m88 = (uint32_t)((uint8_t)(result));
    v_stack_m90 = (uint32_t)((uint8_t)(result));
    v_stack_m98 = (uint32_t)((uint8_t)(result));
    v_stack_mA0 = (uint32_t)((uint8_t)(result));
    v_stack_mA8 = (uint32_t)((uint8_t)(result));
    v_stack_mB0 = (uint32_t)((uint8_t)(*(uint64_t *)(local_rsp - 0x5F + 0xF)));
    v_stack_mB8 = Arg2;
    v_stack_mC0 = (uint32_t)((uint16_t)(result));
    v_stack_mC8 = (uint32_t)(*(uint64_t *)(local_rsp - 0x5F + 0x7));
    v_stack_mD0 = v_rip + 77993;
    v_stack_mD8 = 0x400ULL;
    result = RtlStringCbPrintfExW(*(uint64_t *)(local_rsp - 0x5F - 0x1), *(uint64_t *)(local_rsp - 0x5F - 0x9), local_rsp - 95 - 1, local_rsp - 95 - 9);
    if (sign_flag) goto loc_00AFAEE6;
loc_00AFAEBB:
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x77)) + (16);
    *(uint64_t *)(local_rsp - 0x5F + 0x77) = Arg1;
    if (Arg1 < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x67) + 0x24)))) goto loc_00AFADCB;
loc_00AFAECF:
    if (*(uint64_t *)(local_rsp - 0x5F + 0x7F) != 0) {
        *(uint32_t *)(*(uint64_t *)(local_rsp - 0x5F + 0x7F)) = (uint32_t)(local_r12);
    }
    local_rbx = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(local_r12)) > ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F + 0x6F))))) { local_rbx = (uint32_t)((uint32_t)(0xC0000023ULL)); }
loc_00AFAEE6:
    local_rsp = (local_rsp) + (184);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `16` | `W` |
| `Arg3` | `+ 0x0 + rax*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AFA7B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
