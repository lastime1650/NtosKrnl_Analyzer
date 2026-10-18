# ExpressionConvertToString

- RVA: `0x00AD83F8`–`0x00AD87F2` (길이 `1,018` bytes)
- VA: `0x0000000140AD83F8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AEAB0`
- 디코드: `275`개 명령, `1,018/1,018` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **22**

### Outgoing calls
- `0x00AD84CD` → [RtlStringCbCopyW](../../text/43/RtlStringCbCopyW_function_0043B910.md) (function, `0x0043B910`)
- `0x00AD8510` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (function, `0x0045488C`)
- `0x00AD856A` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (function, `0x0045488C`)
- `0x00AD85B8` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (function, `0x0045488C`)
- `0x00AD8603` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (function, `0x0045488C`)
- `0x00AD8734` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (function, `0x0045488C`)
- `0x00AD8758` → [ConvertDevpropertyToString](../AF/ConvertDevpropertyToString_function_00AFA7B8.md) (function, `0x00AFA7B8`)
- `0x00AD87BA` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (function, `0x0045488C`)

### Direct callers
- [FilterConvertToString](../83/FilterConvertToString_function_00835CAC.md) at `0x00835D15`

### Static image references
- `0x00AD8483` → RVA `0x00B01BB0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD848C` → RVA `0x00B0DFC0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD8495` → RVA `0x00B0DFB0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD849E` → RVA `0x00B0DFA0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD8509` → RVA `0x00B0DFD0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD855D` → RVA `0x00B0DFE0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD85AB` → RVA `0x00B0DFF0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD85F6` → RVA `0x00B0E010` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD865D` → RVA `0x00B0DDD0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD8669` → RVA `0x00B0DDC0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD8675` → RVA `0x00B0DDB0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD8681` → RVA `0x00B0E040` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD868A` → RVA `0x00B0E020` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD8693` → RVA `0x00B0DDE0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD86B9` → RVA `0x00B0DE50` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD86C2` → RVA `0x00B0DE30` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD86CB` → RVA `0x00B0DE10` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD86D4` → RVA `0x00B0DE00` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD86DD` → RVA `0x00B0DDF0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD86E6` → RVA `0x00B0DE70` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD86FB` → RVA `0x00B0DE90` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AD87AD` → RVA `0x00B01B90` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00AD84CD` → [RtlStringCbCopyW](../../text/43/RtlStringCbCopyW_function_0043B910.md) (`PAGE` → `.text`)
  - `0x00AD8510` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (`PAGE` → `.text`)
  - `0x00AD856A` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (`PAGE` → `.text`)
  - `0x00AD85B8` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (`PAGE` → `.text`)
  - `0x00AD8603` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (`PAGE` → `.text`)
  - `0x00AD8734` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (`PAGE` → `.text`)
  - `0x00AD87BA` → [RtlStringCbCopyExW](../../text/45/RtlStringCbCopyExW_function_0045488C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AD83F8  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00AD83FD  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00AD8402  55                              push rbp
00AD8403  56                              push rsi
00AD8404  57                              push rdi
00AD8405  41 54                           push r12
00AD8407  41 55                           push r13
00AD8409  41 56                           push r14
00AD840B  41 57                           push r15
00AD840D  48 8B EC                        mov rbp, rsp
00AD8410  48 83 EC 40                     sub rsp, 0x40
00AD8414  44 8B F2                        mov r14d, edx
00AD8417  4D 8B D0                        mov r10, r8
00AD841A  33 D2                           xor edx, edx
00AD841C  4C 8B E9                        mov r13, rcx
00AD841F  48 89 55 F0                     mov qword ptr [rbp - 0x10], rdx
00AD8423  8B FA                           mov edi, edx
00AD8425  48 89 55 F8                     mov qword ptr [rbp - 8], rdx
00AD8429  8B F2                           mov esi, edx
00AD842B  89 55 40                        mov dword ptr [rbp + 0x40], edx
00AD842E  48 85 C9                        test rcx, rcx
00AD8431  75 0A                           jne 0x140ad843d
00AD8433  B9 0D 00 00 C0                  mov ecx, 0xc000000d
00AD8438  E9 9A 03 00 00                  jmp 0x140ad87d7
00AD843D  41 BC 02 00 00 00               mov r12d, 2
00AD8443  45 3B F4                        cmp r14d, r12d
00AD8446  72 04                           jb 0x140ad844c
00AD8448  66 41 89 10                     mov word ptr [r8], dx
00AD844C  8B 01                           mov eax, dword ptr [rcx]
00AD844E  25 00 00 F0 0F                  and eax, 0xff00000
00AD8453  0F 84 8A 00 00 00               je 0x140ad84e3
00AD8459  3D 00 00 10 00                  cmp eax, 0x100000
00AD845E  74 3E                           je 0x140ad849e
00AD8460  3D 00 00 20 00                  cmp eax, 0x200000
00AD8465  74 1C                           je 0x140ad8483
00AD8467  3D 00 00 30 00                  cmp eax, 0x300000
00AD846C  74 27                           je 0x140ad8495
00AD846E  3D 00 00 40 00                  cmp eax, 0x400000
00AD8473  74 0E                           je 0x140ad8483
00AD8475  3D 00 00 50 00                  cmp eax, 0x500000
00AD847A  74 10                           je 0x140ad848c
00AD847C  3D 00 00 60 00                  cmp eax, 0x600000
00AD8481  75 B0                           jne 0x140ad8433
00AD8483  4C 8D 05 26 97 02 00            lea r8, [rip + 0x29726]
00AD848A  EB 19                           jmp 0x140ad84a5
00AD848C  4C 8D 05 2D 5B 03 00            lea r8, [rip + 0x35b2d]
00AD8493  EB 10                           jmp 0x140ad84a5
00AD8495  4C 8D 05 14 5B 03 00            lea r8, [rip + 0x35b14]
00AD849C  EB 07                           jmp 0x140ad84a5
00AD849E  4C 8D 05 FB 5A 03 00            lea r8, [rip + 0x35afb]
00AD84A5  48 83 C8 FF                     or rax, 0xffffffffffffffff
00AD84A9  48 FF C0                        inc rax
00AD84AC  66 41 39 14 40                  cmp word ptr [r8 + rax*2], dx
00AD84B1  75 F6                           jne 0x140ad84a9
00AD84B3  8D 04 45 02 00 00 00            lea eax, [rax*2 + 2]
00AD84BA  4D 85 C9                        test r9, r9
00AD84BD  74 03                           je 0x140ad84c2
00AD84BF  41 89 01                        mov dword ptr [r9], eax
00AD84C2  41 3B C6                        cmp eax, r14d
00AD84C5  77 12                           ja 0x140ad84d9
00AD84C7  49 8B D6                        mov rdx, r14
00AD84CA  49 8B CA                        mov rcx, r10
00AD84CD  E8 3E 34 96 FF                  call 0x14043b910
00AD84D2  8B C8                           mov ecx, eax
00AD84D4  E9 FE 02 00 00                  jmp 0x140ad87d7
00AD84D9  B9 23 00 00 C0                  mov ecx, 0xc0000023
00AD84DE  E9 F4 02 00 00                  jmp 0x140ad87d7
00AD84E3  41 BF 06 00 00 00               mov r15d, 6
00AD84E9  45 3B F7                        cmp r14d, r15d
00AD84EC  72 3B                           jb 0x140ad8529
00AD84EE  48 8D 45 F0                     lea rax, [rbp - 0x10]
00AD84F2  C7 44 24 28 00 04 00 00         mov dword ptr [rsp + 0x28], 0x400
00AD84FA  49 8B D6                        mov rdx, r14
00AD84FD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AD8502  4C 8D 4D F8                     lea r9, [rbp - 8]
00AD8506  49 8B CA                        mov rcx, r10
00AD8509  4C 8D 05 C0 5A 03 00            lea r8, [rip + 0x35ac0]
00AD8510  E8 77 C3 97 FF                  call 0x14045488c
00AD8515  33 D2                           xor edx, edx
00AD8517  8B C8                           mov ecx, eax
00AD8519  85 C0                           test eax, eax
00AD851B  0F 88 B6 02 00 00               js 0x140ad87d7
00AD8521  48 8B 7D F0                     mov rdi, qword ptr [rbp - 0x10]
00AD8525  48 8B 75 F8                     mov rsi, qword ptr [rbp - 8]
00AD8529  41 8B 5D 00                     mov ebx, dword ptr [r13]
00AD852D  81 E3 00 00 0F 00               and ebx, 0xf0000
00AD8533  0F BA E3 10                     bt ebx, 0x10
00AD8537  73 4A                           jae 0x140ad8583
00AD8539  0F BA F3 10                     btr ebx, 0x10
00AD853D  41 BF 10 00 00 00               mov r15d, 0x10
00AD8543  45 3B F7                        cmp r14d, r15d
00AD8546  72 3B                           jb 0x140ad8583
00AD8548  48 8D 45 F0                     lea rax, [rbp - 0x10]
00AD854C  C7 44 24 28 00 04 00 00         mov dword ptr [rsp + 0x28], 0x400
00AD8554  4C 8D 4D F8                     lea r9, [rbp - 8]
00AD8558  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AD855D  4C 8D 05 7C 5A 03 00            lea r8, [rip + 0x35a7c]
00AD8564  48 8B D7                        mov rdx, rdi
00AD8567  48 8B CE                        mov rcx, rsi
00AD856A  E8 1D C3 97 FF                  call 0x14045488c
00AD856F  33 D2                           xor edx, edx
00AD8571  8B C8                           mov ecx, eax
00AD8573  85 C0                           test eax, eax
00AD8575  0F 88 5C 02 00 00               js 0x140ad87d7
00AD857B  48 8B 7D F0                     mov rdi, qword ptr [rbp - 0x10]
00AD857F  48 8B 75 F8                     mov rsi, qword ptr [rbp - 8]
00AD8583  0F BA E3 11                     bt ebx, 0x11
00AD8587  73 48                           jae 0x140ad85d1
00AD8589  0F BA F3 11                     btr ebx, 0x11
00AD858D  41 83 C7 1A                     add r15d, 0x1a
00AD8591  45 3B FE                        cmp r15d, r14d
00AD8594  77 3B                           ja 0x140ad85d1
00AD8596  48 8D 45 F0                     lea rax, [rbp - 0x10]
00AD859A  C7 44 24 28 00 04 00 00         mov dword ptr [rsp + 0x28], 0x400
00AD85A2  4C 8D 4D F8                     lea r9, [rbp - 8]
00AD85A6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AD85AB  4C 8D 05 3E 5A 03 00            lea r8, [rip + 0x35a3e]
00AD85B2  48 8B D7                        mov rdx, rdi
00AD85B5  48 8B CE                        mov rcx, rsi
00AD85B8  E8 CF C2 97 FF                  call 0x14045488c
00AD85BD  33 D2                           xor edx, edx
00AD85BF  8B C8                           mov ecx, eax
00AD85C1  85 C0                           test eax, eax
00AD85C3  0F 88 0E 02 00 00               js 0x140ad87d7
00AD85C9  48 8B 7D F0                     mov rdi, qword ptr [rbp - 0x10]
00AD85CD  48 8B 75 F8                     mov rsi, qword ptr [rbp - 8]
00AD85D1  85 DB                           test ebx, ebx
00AD85D3  0F 85 5A FE FF FF               jne 0x140ad8433
00AD85D9  45 03 FC                        add r15d, r12d
00AD85DC  45 3B FE                        cmp r15d, r14d
00AD85DF  77 3B                           ja 0x140ad861c
00AD85E1  48 8D 45 F0                     lea rax, [rbp - 0x10]
00AD85E5  C7 44 24 28 00 04 00 00         mov dword ptr [rsp + 0x28], 0x400
00AD85ED  4C 8D 4D F8                     lea r9, [rbp - 8]
00AD85F1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AD85F6  4C 8D 05 13 5A 03 00            lea r8, [rip + 0x35a13]
00AD85FD  48 8B D7                        mov rdx, rdi
00AD8600  48 8B CE                        mov rcx, rsi
00AD8603  E8 84 C2 97 FF                  call 0x14045488c
00AD8608  33 D2                           xor edx, edx
00AD860A  8B C8                           mov ecx, eax
00AD860C  85 C0                           test eax, eax
00AD860E  0F 88 C3 01 00 00               js 0x140ad87d7
00AD8614  48 8B 7D F0                     mov rdi, qword ptr [rbp - 0x10]
00AD8618  48 8B 75 F8                     mov rsi, qword ptr [rbp - 8]
00AD861C  41 8B 4D 00                     mov ecx, dword ptr [r13]
00AD8620  B8 00 10 00 00                  mov eax, 0x1000
00AD8625  81 E1 FF FF 00 F0               and ecx, 0xf000ffff
00AD862B  3B C8                           cmp ecx, eax
00AD862D  0F 8F BC 00 00 00               jg 0x140ad86ef
00AD8633  0F 84 AD 00 00 00               je 0x140ad86e6
00AD8639  83 F9 06                        cmp ecx, 6
00AD863C  7F 5E                           jg 0x140ad869c
00AD863E  74 53                           je 0x140ad8693
00AD8640  83 E9 01                        sub ecx, 1
00AD8643  74 45                           je 0x140ad868a
00AD8645  83 E9 01                        sub ecx, 1
00AD8648  74 37                           je 0x140ad8681
00AD864A  83 E9 01                        sub ecx, 1
00AD864D  74 26                           je 0x140ad8675
00AD864F  83 E9 01                        sub ecx, 1
00AD8652  74 15                           je 0x140ad8669
00AD8654  83 F9 01                        cmp ecx, 1
00AD8657  0F 85 D6 FD FF FF               jne 0x140ad8433
00AD865D  4C 8D 05 6C 57 03 00            lea r8, [rip + 0x3576c]
00AD8664  E9 99 00 00 00                  jmp 0x140ad8702
00AD8669  4C 8D 05 50 57 03 00            lea r8, [rip + 0x35750]
00AD8670  E9 8D 00 00 00                  jmp 0x140ad8702
00AD8675  4C 8D 05 34 57 03 00            lea r8, [rip + 0x35734]
00AD867C  E9 81 00 00 00                  jmp 0x140ad8702
00AD8681  4C 8D 05 B8 59 03 00            lea r8, [rip + 0x359b8]
00AD8688  EB 78                           jmp 0x140ad8702
00AD868A  4C 8D 05 8F 59 03 00            lea r8, [rip + 0x3598f]
00AD8691  EB 6F                           jmp 0x140ad8702
00AD8693  4C 8D 05 46 57 03 00            lea r8, [rip + 0x35746]
00AD869A  EB 66                           jmp 0x140ad8702
00AD869C  83 E9 07                        sub ecx, 7
00AD869F  74 3C                           je 0x140ad86dd
00AD86A1  83 E9 01                        sub ecx, 1
00AD86A4  74 2E                           je 0x140ad86d4
00AD86A6  83 E9 01                        sub ecx, 1
00AD86A9  74 20                           je 0x140ad86cb
00AD86AB  83 E9 01                        sub ecx, 1
00AD86AE  74 12                           je 0x140ad86c2
00AD86B0  83 F9 01                        cmp ecx, 1
00AD86B3  0F 85 7A FD FF FF               jne 0x140ad8433
00AD86B9  4C 8D 05 90 57 03 00            lea r8, [rip + 0x35790]
00AD86C0  EB 40                           jmp 0x140ad8702
00AD86C2  4C 8D 05 67 57 03 00            lea r8, [rip + 0x35767]
00AD86C9  EB 37                           jmp 0x140ad8702
00AD86CB  4C 8D 05 3E 57 03 00            lea r8, [rip + 0x3573e]
00AD86D2  EB 2E                           jmp 0x140ad8702
00AD86D4  4C 8D 05 25 57 03 00            lea r8, [rip + 0x35725]
00AD86DB  EB 25                           jmp 0x140ad8702
00AD86DD  4C 8D 05 0C 57 03 00            lea r8, [rip + 0x3570c]
00AD86E4  EB 1C                           jmp 0x140ad8702
00AD86E6  4C 8D 05 83 57 03 00            lea r8, [rip + 0x35783]
00AD86ED  EB 13                           jmp 0x140ad8702
00AD86EF  81 F9 00 00 00 10               cmp ecx, 0x10000000
00AD86F5  0F 85 38 FD FF FF               jne 0x140ad8433
00AD86FB  4C 8D 05 8E 57 03 00            lea r8, [rip + 0x3578e]
00AD8702  48 83 C8 FF                     or rax, 0xffffffffffffffff
00AD8706  48 FF C0                        inc rax
00AD8709  66 41 39 14 40                  cmp word ptr [r8 + rax*2], dx
00AD870E  75 F6                           jne 0x140ad8706
00AD8710  45 8D 3C 47                     lea r15d, [r15 + rax*2]
00AD8714  45 3B FE                        cmp r15d, r14d
00AD8717  77 32                           ja 0x140ad874b
00AD8719  48 8D 45 F0                     lea rax, [rbp - 0x10]
00AD871D  C7 44 24 28 00 04 00 00         mov dword ptr [rsp + 0x28], 0x400
00AD8725  4C 8D 4D F8                     lea r9, [rbp - 8]
00AD8729  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AD872E  48 8B D7                        mov rdx, rdi
00AD8731  48 8B CE                        mov rcx, rsi
00AD8734  E8 53 C1 97 FF                  call 0x14045488c
00AD8739  8B C8                           mov ecx, eax
00AD873B  85 C0                           test eax, eax
00AD873D  0F 88 94 00 00 00               js 0x140ad87d7
00AD8743  48 8B 7D F0                     mov rdi, qword ptr [rbp - 0x10]
00AD8747  48 8B 75 F8                     mov rsi, qword ptr [rbp - 8]
00AD874B  49 8D 4D 08                     lea rcx, [r13 + 8]
00AD874F  4C 8B C6                        mov r8, rsi
00AD8752  4C 8D 4D 40                     lea r9, [rbp + 0x40]
00AD8756  8B D7                           mov edx, edi
00AD8758  E8 5B 20 02 00                  call 0x140afa7b8
00AD875D  BA 00 00 00 80                  mov edx, 0x80000000
00AD8762  8B C8                           mov ecx, eax
00AD8764  03 C2                           add eax, edx
00AD8766  BB 23 00 00 C0                  mov ebx, 0xc0000023
00AD876B  85 C2                           test edx, eax
00AD876D  75 04                           jne 0x140ad8773
00AD876F  3B CB                           cmp ecx, ebx
00AD8771  75 64                           jne 0x140ad87d7
00AD8773  8B 45 40                        mov eax, dword ptr [rbp + 0x40]
00AD8776  33 C9                           xor ecx, ecx
00AD8778  44 03 F8                        add r15d, eax
00AD877B  8B D0                           mov edx, eax
00AD877D  48 83 C0 FE                     add rax, -2
00AD8781  48 3B F8                        cmp rdi, rax
00AD8784  72 0D                           jb 0x140ad8793
00AD8786  4C 2B E2                        sub r12, rdx
00AD8789  49 03 FC                        add rdi, r12
00AD878C  48 D1 E8                        shr rax, 1
00AD878F  48 8D 34 46                     lea rsi, [rsi + rax*2]
00AD8793  45 3B FE                        cmp r15d, r14d
00AD8796  77 2D                           ja 0x140ad87c5
00AD8798  48 8D 45 F0                     lea rax, [rbp - 0x10]
00AD879C  C7 44 24 28 00 04 00 00         mov dword ptr [rsp + 0x28], 0x400
00AD87A4  4C 8D 4D F8                     lea r9, [rbp - 8]
00AD87A8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AD87AD  4C 8D 05 DC 93 02 00            lea r8, [rip + 0x293dc]
00AD87B4  48 8B D7                        mov rdx, rdi
00AD87B7  48 8B CE                        mov rcx, rsi
00AD87BA  E8 CD C0 97 FF                  call 0x14045488c
00AD87BF  8B C8                           mov ecx, eax
00AD87C1  85 C0                           test eax, eax
00AD87C3  78 12                           js 0x140ad87d7
00AD87C5  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00AD87C9  48 85 C0                        test rax, rax
00AD87CC  74 03                           je 0x140ad87d1
00AD87CE  44 89 38                        mov dword ptr [rax], r15d
00AD87D1  45 3B FE                        cmp r15d, r14d
00AD87D4  0F 47 CB                        cmova ecx, ebx
00AD87D7  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
00AD87DF  8B C1                           mov eax, ecx
00AD87E1  48 83 C4 40                     add rsp, 0x40
00AD87E5  41 5F                           pop r15
00AD87E7  41 5E                           pop r14
00AD87E9  41 5D                           pop r13
00AD87EB  41 5C                           pop r12
00AD87ED  5F                              pop rdi
00AD87EE  5E                              pop rsi
00AD87EF  5D                              pop rbp
00AD87F0  C3                              ret
00AD87F1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpressionConvertToString(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (64);
    a2 = 0;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
    v_stack_p8 = 0;
    if (a1 != 0) goto loc_00AD843D;
loc_00AD8433:
    goto loc_00AD87D7;
loc_00AD843D:
    if (((unsigned int)((unsigned int)(a2))) >= 2) {
        *(unsigned __int16 *)(a3) = 0;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(0xC000000DULL)))) & (0xFF00000ULL));
    if (condition_is_equal) goto loc_00AD84E3;
    if (((unsigned int)(result)) == 0x100000ULL) goto loc_00AD849E;
    if (((unsigned int)(result)) == 0x200000ULL) goto loc_00AD8483;
    if (((unsigned int)(result)) == 0x300000ULL) goto loc_00AD8495;
    if (((unsigned int)(result)) == 0x400000ULL) goto loc_00AD8483;
    if (((unsigned int)(result)) == 0x500000ULL) goto loc_00AD848C;
    if (((unsigned int)(result)) != 0x600000ULL) goto loc_00AD8433;
loc_00AD8483:
    goto loc_00AD84A5;
loc_00AD848C:
    goto loc_00AD84A5;
loc_00AD8495:
    goto loc_00AD84A5;
loc_00AD849E:
loc_00AD84A5:
    result = (result) | (-1);
loc_00AD84A9:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_rip + 219899 + result * 2)) != 0) goto loc_00AD84A9;
    if (a4 != 0) {
        *(unsigned int *)(a4) = (unsigned int)(result * 2 + 2);
    }
    if (((unsigned int)(result * 2 + 2)) > ((unsigned int)((unsigned int)(a2)))) goto loc_00AD84D9;
    result = RtlStringCbCopyW(a3, (unsigned int)(a2), v_rip + 219899, a4);
    goto loc_00AD87D7;
loc_00AD84D9:
    goto loc_00AD87D7;
loc_00AD84E3:
    if (((unsigned int)((unsigned int)(a2))) < 6) goto loc_00AD8529;
    v_stack_m50 = 0x400ULL;
    v_stack_m58 = v_stack_m48;
    result = RtlStringCbCopyExW(a3, (unsigned int)(a2), v_rip + 219840, v_stack_m40);
    a2 = 0;
    if (sign_flag) goto loc_00AD87D7;
loc_00AD8529:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) & (0xF0000ULL));
    if (condition_is_above_or_equal) goto loc_00AD8583;
    if (((unsigned int)((unsigned int)(a2))) < 16) goto loc_00AD8583;
    v_stack_m50 = 0x400ULL;
    v_stack_m58 = v_stack_m48;
    result = RtlStringCbCopyExW(v_stack_m40, v_stack_m48, v_rip + 219772, v_stack_m40);
    a2 = 0;
    if (sign_flag) goto loc_00AD87D7;
loc_00AD8583:
    if (condition_is_above_or_equal) goto loc_00AD85D1;
    v_r15 = (unsigned int)((16) + (26));
    if (((unsigned int)(v_r15)) > ((unsigned int)((unsigned int)(a2)))) goto loc_00AD85D1;
    v_stack_m50 = 0x400ULL;
    v_stack_m58 = v_stack_m48;
    result = RtlStringCbCopyExW(v_stack_m40, v_stack_m48, v_rip + 219710, v_stack_m40);
    a2 = 0;
    if (sign_flag) goto loc_00AD87D7;
loc_00AD85D1:
    if ((unsigned int)(v_rbx) != 0) goto loc_00AD8433;
    v_r15 = (unsigned int)((v_r15) + (2));
    if (((unsigned int)(v_r15)) > ((unsigned int)((unsigned int)(a2)))) goto loc_00AD861C;
    v_stack_m50 = 0x400ULL;
    v_stack_m58 = v_stack_m48;
    result = RtlStringCbCopyExW(v_stack_m40, v_stack_m48, v_rip + 219667, v_stack_m40);
    a2 = 0;
    if (sign_flag) goto loc_00AD87D7;
loc_00AD861C:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) & (0xF000FFFFULL));
    if (((unsigned int)(a1)) > ((unsigned int)((unsigned int)(0x1000ULL)))) goto loc_00AD86EF;
    if (((unsigned int)(a1)) == ((unsigned int)((unsigned int)(0x1000ULL)))) goto loc_00AD86E6;
    if (((unsigned int)(a1)) > 6) goto loc_00AD869C;
    if (((unsigned int)(a1)) == 6) goto loc_00AD8693;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AD868A;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AD8681;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AD8675;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AD8669;
    if (((unsigned int)(a1)) != 1) goto loc_00AD8433;
    goto loc_00AD8702;
loc_00AD8669:
    goto loc_00AD8702;
loc_00AD8675:
    goto loc_00AD8702;
loc_00AD8681:
    goto loc_00AD8702;
loc_00AD868A:
    goto loc_00AD8702;
loc_00AD8693:
    goto loc_00AD8702;
loc_00AD869C:
    a1 = (unsigned int)((a1) - (7));
    if (condition_is_equal) goto loc_00AD86DD;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AD86D4;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AD86CB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AD86C2;
    if (((unsigned int)(a1)) != 1) goto loc_00AD8433;
    goto loc_00AD8702;
loc_00AD86C2:
    goto loc_00AD8702;
loc_00AD86CB:
    goto loc_00AD8702;
loc_00AD86D4:
    goto loc_00AD8702;
loc_00AD86DD:
    goto loc_00AD8702;
loc_00AD86E6:
    goto loc_00AD8702;
loc_00AD86EF:
    if (((unsigned int)(a1)) != 0x10000000ULL) goto loc_00AD8433;
loc_00AD8702:
    result = ((unsigned int)(0x1000ULL)) | (-1);
loc_00AD8706:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_rip + 219022 + result * 2)) != 0) goto loc_00AD8706;
    if (((unsigned int)(v_r15 + result * 2)) > ((unsigned int)((unsigned int)(a2)))) goto loc_00AD874B;
    v_stack_m50 = 0x400ULL;
    v_stack_m58 = v_stack_m48;
    result = RtlStringCbCopyExW(v_stack_m40, v_stack_m48, v_rip + 219022, v_stack_m40);
    if (sign_flag) goto loc_00AD87D7;
loc_00AD874B:
    result = ConvertDevpropertyToString(a1 + 8, (unsigned int)((unsigned int)(v_stack_m48)), v_stack_m40, v_stack_p8);
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) != 0) goto loc_00AD8773;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)((unsigned int)(0xC0000023ULL)))) goto loc_00AD87D7;
loc_00AD8773:
    a1 = 0;
    v_r15 = (unsigned int)((v_r15 + result * 2) + ((unsigned int)((unsigned int)(v_stack_p8))));
    result = ((unsigned int)(v_stack_p8)) + (-2);
    v_rsi = v_stack_m40;
    v_rdi = v_stack_m48;
    v_r12 = 2;
    if (v_stack_m48 >= result) {
        v_r12 = (2) - ((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
        v_rdi = (v_stack_m48) + (v_r12);
        result = (result) >> (1);
        v_rsi = v_stack_m40 + result * 2;
    }
    if (((unsigned int)(v_r15)) > ((unsigned int)((unsigned int)(a2)))) goto loc_00AD87C5;
    v_stack_m50 = 0x400ULL;
    v_stack_m58 = v_stack_m48;
    result = RtlStringCbCopyExW(v_rsi, v_rdi, v_rip + 168924, v_stack_m40);
    if (sign_flag) goto loc_00AD87D7;
loc_00AD87C5:
    if (v_stack_p20 != 0) {
        *(unsigned int *)(v_stack_p20) = (unsigned int)(v_r15);
    }
    a1 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(v_r15)) > ((unsigned int)((unsigned int)(a2)))) { a1 = (unsigned int)((unsigned int)(0xC0000023ULL)); }
loc_00AD87D7:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)(a1));
}
```

## 5. (Beta) C Style

```c
int64_t ExpressionConvertToString(void *Arg1, int32_t Arg2, void *Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (64);
    Arg2 = 0;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
    v_stack_p8 = 0;
    if (Arg1 != NULL) goto loc_00AD843D;
loc_00AD8433:
    goto loc_00AD87D7;
loc_00AD843D:
    if (((uint32_t)((uint32_t)(Arg2))) >= 2) {
        *(uint16_t *)(arg3) = 0;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(0xC000000DULL)))) & (0xFF00000ULL));
    if (condition_is_equal) goto loc_00AD84E3;
    if (((uint32_t)(result)) == 0x100000ULL) goto loc_00AD849E;
    if (((uint32_t)(result)) == 0x200000ULL) goto loc_00AD8483;
    if (((uint32_t)(result)) == 0x300000ULL) goto loc_00AD8495;
    if (((uint32_t)(result)) == 0x400000ULL) goto loc_00AD8483;
    if (((uint32_t)(result)) == 0x500000ULL) goto loc_00AD848C;
    if (((uint32_t)(result)) != 0x600000ULL) goto loc_00AD8433;
loc_00AD8483:
    goto loc_00AD84A5;
loc_00AD848C:
    goto loc_00AD84A5;
loc_00AD8495:
    goto loc_00AD84A5;
loc_00AD849E:
loc_00AD84A5:
    result = (result) | (-1);
loc_00AD84A9:
    result = (result) + 1;
    if ((*(uint16_t *)(v_rip + 0x35AFB + result * 2)) != 0) goto loc_00AD84A9;
    if (Arg4 != 0) {
        *(uint32_t *)(Arg4) = (uint32_t)(result * 2 + 2);
    }
    if (((uint32_t)(result * 2 + 2)) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_00AD84D9;
    result = RtlStringCbCopyW(Arg3, (uint32_t)(Arg2), v_rip + 219899, Arg4);
    goto loc_00AD87D7;
loc_00AD84D9:
    goto loc_00AD87D7;
loc_00AD84E3:
    if (((uint32_t)((uint32_t)(Arg2))) < 6) goto loc_00AD8529;
    v_stack_m50 = 0x400ULL;
    v_stack_m58 = v_stack_m48;
    result = RtlStringCbCopyExW(Arg3, (uint32_t)(Arg2), v_rip + 219840, v_stack_m40);
    Arg2 = 0;
    if (sign_flag) goto loc_00AD87D7;
loc_00AD8529:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) & (0xF0000ULL));
    if (condition_is_above_or_equal) goto loc_00AD8583;
    if (((uint32_t)((uint32_t)(Arg2))) < 16) goto loc_00AD8583;
    v_stack_m50 = 0x400ULL;
    v_stack_m58 = v_stack_m48;
    result = RtlStringCbCopyExW(v_stack_m40, v_stack_m48, v_rip + 219772, v_stack_m40);
    Arg2 = 0;
    if (sign_flag) goto loc_00AD87D7;
loc_00AD8583:
    if (condition_is_above_or_equal) goto loc_00AD85D1;
    local_r15 = (uint32_t)((16) + (26));
    if (((uint32_t)(local_r15)) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_00AD85D1;
    v_stack_m50 = 0x400ULL;
    v_stack_m58 = v_stack_m48;
    result = RtlStringCbCopyExW(v_stack_m40, v_stack_m48, v_rip + 219710, v_stack_m40);
    Arg2 = 0;
    if (sign_flag) goto loc_00AD87D7;
loc_00AD85D1:
    if ((uint32_t)(local_rbx) != 0) goto loc_00AD8433;
    local_r15 = (uint32_t)((local_r15) + (2));
    if (((uint32_t)(local_r15)) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_00AD861C;
    v_stack_m50 = 0x400ULL;
    v_stack_m58 = v_stack_m48;
    result = RtlStringCbCopyExW(v_stack_m40, v_stack_m48, v_rip + 219667, v_stack_m40);
    Arg2 = 0;
    if (sign_flag) goto loc_00AD87D7;
loc_00AD861C:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) & (0xF000FFFFULL));
    if (((uint32_t)(Arg1)) > ((uint32_t)((uint32_t)(0x1000ULL)))) goto loc_00AD86EF;
    if (((uint32_t)(Arg1)) == ((uint32_t)((uint32_t)(0x1000ULL)))) goto loc_00AD86E6;
    if (((uint32_t)(Arg1)) > 6) goto loc_00AD869C;
    if (((uint32_t)(Arg1)) == 6) goto loc_00AD8693;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AD868A;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AD8681;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AD8675;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AD8669;
    if (((uint32_t)(Arg1)) != 1) goto loc_00AD8433;
    goto loc_00AD8702;
loc_00AD8669:
    goto loc_00AD8702;
loc_00AD8675:
    goto loc_00AD8702;
loc_00AD8681:
    goto loc_00AD8702;
loc_00AD868A:
    goto loc_00AD8702;
loc_00AD8693:
    goto loc_00AD8702;
loc_00AD869C:
    Arg1 = (uint32_t)((Arg1) - (7));
    if (condition_is_equal) goto loc_00AD86DD;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AD86D4;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AD86CB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AD86C2;
    if (((uint32_t)(Arg1)) != 1) goto loc_00AD8433;
    goto loc_00AD8702;
loc_00AD86C2:
    goto loc_00AD8702;
loc_00AD86CB:
    goto loc_00AD8702;
loc_00AD86D4:
    goto loc_00AD8702;
loc_00AD86DD:
    goto loc_00AD8702;
loc_00AD86E6:
    goto loc_00AD8702;
loc_00AD86EF:
    if (((uint32_t)(Arg1)) != 0x10000000ULL) goto loc_00AD8433;
loc_00AD8702:
    result = ((uint32_t)(0x1000ULL)) | (-1);
loc_00AD8706:
    result = (result) + 1;
    if ((*(uint16_t *)(v_rip + 0x3578E + result * 2)) != 0) goto loc_00AD8706;
    if (((uint32_t)(local_r15 + result * 2)) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_00AD874B;
    v_stack_m50 = 0x400ULL;
    v_stack_m58 = v_stack_m48;
    result = RtlStringCbCopyExW(v_stack_m40, v_stack_m48, v_rip + 219022, v_stack_m40);
    if (sign_flag) goto loc_00AD87D7;
loc_00AD874B:
    result = ConvertDevpropertyToString(Arg1 + 8, (uint32_t)((uint32_t)(v_stack_m48)), v_stack_m40, v_stack_p8);
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) != 0) goto loc_00AD8773;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)((uint32_t)(0xC0000023ULL)))) goto loc_00AD87D7;
loc_00AD8773:
    Arg1 = 0;
    local_r15 = (uint32_t)((local_r15 + result * 2) + ((uint32_t)((uint32_t)(v_stack_p8))));
    result = ((uint32_t)(v_stack_p8)) + (-2);
    local_rsi = v_stack_m40;
    local_rdi = v_stack_m48;
    local_r12 = 2;
    if (v_stack_m48 >= result) {
        local_r12 = (2) - ((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
        local_rdi = (v_stack_m48) + (local_r12);
        result = (result) >> (1);
        local_rsi = v_stack_m40 + result * 2;
    }
    if (((uint32_t)(local_r15)) > ((uint32_t)((uint32_t)(Arg2)))) goto loc_00AD87C5;
    v_stack_m50 = 0x400ULL;
    v_stack_m58 = v_stack_m48;
    result = RtlStringCbCopyExW(local_rsi, local_rdi, v_rip + 168924, v_stack_m40);
    if (sign_flag) goto loc_00AD87D7;
loc_00AD87C5:
    if (v_stack_p20 != 0) {
        *(uint32_t *)(v_stack_p20) = (uint32_t)(local_r15);
    }
    Arg1 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(local_r15)) > ((uint32_t)((uint32_t)(Arg2)))) { Arg1 = (uint32_t)((uint32_t)(0xC0000023ULL)); }
loc_00AD87D7:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)(Arg1));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x0` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AD83F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
