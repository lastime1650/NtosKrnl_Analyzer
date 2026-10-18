# output_l

- RVA: `0x00503368`–`0x00503BD7` (길이 `2,159` bytes)
- VA: `0x0000000140503368`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C27F8`
- 디코드: `579`개 명령, `2,159/2,159` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x005033D4` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00503628` → [wctomb_s](wctomb_s_function_005025D4.md) (function, `0x005025D4`)
- `0x0050387A` → [write_multi_char](write_multi_char_function_00503C30.md) (function, `0x00503C30`)
- `0x00503891` → [write_string](write_string_function_00503C88.md) (function, `0x00503C88`)
- `0x005038AC` → [write_multi_char](write_multi_char_function_00503C30.md) (function, `0x00503C30`)
- `0x005038E4` → [wctomb_s](wctomb_s_function_005025D4.md) (function, `0x005025D4`)
- `0x00503909` → [write_string](write_string_function_00503C88.md) (function, `0x00503C88`)
- `0x0050392F` → [write_string](write_string_function_00503C88.md) (function, `0x00503C88`)
- `0x00503955` → [write_multi_char](write_multi_char_function_00503C30.md) (function, `0x00503C30`)
- `0x00503978` → [get_printf_count_output](get_printf_count_output_function_00504494.md) (function, `0x00504494`)
- `0x00503A74` → [write_char](write_char_function_00503BE0.md) (function, `0x00503BE0`)
- `0x00503BA4` → [EmpCheckErrataList](../49/EmpCheckErrataList_function_0049E550.md) (function, `0x0049E550`)
- `0x00503BB6` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [vsnprintf_l](../4F/vsnprintf_l_function_004FF070.md) at `0x004FF0D7`
- [snprintf](../4F/snprintf_function_004FFB80.md) at `0x004FFBE4`
- [sprintf](sprintf_function_00501230.md) at `0x00501283`
- [vsprintf_l](vsprintf_l_function_00501928.md) at `0x00501969`

### Static image references
- `0x00503387` → RVA `0x00E0A740` (`.data`; read)
- `0x00503410` → RVA `0x0001EFA0` (`.rdata`; read)
- `0x0050357B` → RVA `0x0001EF98` (`.rdata`; read)
- `0x005035D9` → RVA `0x0002AEF8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00503368  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
0050336D  55                              push rbp
0050336E  56                              push rsi
0050336F  57                              push rdi
00503370  41 54                           push r12
00503372  41 55                           push r13
00503374  41 56                           push r14
00503376  41 57                           push r15
00503378  48 8D AC 24 80 FE FF FF         lea rbp, [rsp - 0x180]
00503380  48 81 EC 80 02 00 00            sub rsp, 0x280
00503387  48 8B 05 B2 73 90 00            mov rax, qword ptr [rip + 0x9073b2]
0050338E  48 33 C4                        xor rax, rsp
00503391  48 89 85 78 01 00 00            mov qword ptr [rbp + 0x178], rax
00503398  4C 8B F1                        mov r14, rcx
0050339B  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
005033A0  33 C9                           xor ecx, ecx
005033A2  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
005033A7  89 4C 24 5C                     mov dword ptr [rsp + 0x5c], ecx
005033AB  44 8B F9                        mov r15d, ecx
005033AE  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
005033B2  44 8B E9                        mov r13d, ecx
005033B5  8B F1                           mov esi, ecx
005033B7  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
005033BB  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
005033BF  8B D9                           mov ebx, ecx
005033C1  4C 8B E2                        mov r12, rdx
005033C4  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
005033C9  33 D2                           xor edx, edx
005033CB  41 B8 00 02 00 00               mov r8d, 0x200
005033D1  49 8B F9                        mov rdi, r9
005033D4  E8 67 38 1C 00                  call 0x1406c6c40
005033D9  45 33 DB                        xor r11d, r11d
005033DC  44 89 5C 24 40                  mov dword ptr [rsp + 0x40], r11d
005033E1  4D 85 F6                        test r14, r14
005033E4  0F 84 AB 07 00 00               je 0x140503b95
005033EA  4D 85 E4                        test r12, r12
005033ED  0F 84 A2 07 00 00               je 0x140503b95
005033F3  45 8A 0C 24                     mov r9b, byte ptr [r12]
005033F7  45 8B F3                        mov r14d, r11d
005033FA  44 89 5C 24 34                  mov dword ptr [rsp + 0x34], r11d
005033FF  45 8B D3                        mov r10d, r11d
00503402  44 89 5C 24 3C                  mov dword ptr [rsp + 0x3c], r11d
00503407  45 84 C9                        test r9b, r9b
0050340A  0F 84 8F 06 00 00               je 0x140503a9f
00503410  48 8D 0D 89 BB B1 FF            lea rcx, [rip - 0x4e4477]
00503417  49 FF C4                        inc r12
0050341A  4C 8B C7                        mov r8, rdi
0050341D  45 85 F6                        test r14d, r14d
00503420  0F 88 79 06 00 00               js 0x140503a9f
00503426  41 8D 41 E0                     lea eax, [r9 - 0x20]
0050342A  3C 5A                           cmp al, 0x5a
0050342C  77 0E                           ja 0x14050343c
0050342E  49 0F BE C1                     movsx rax, r9b
00503432  0F BE 4C 08 E0                  movsx ecx, byte ptr [rax + rcx - 0x20]
00503437  83 E1 0F                        and ecx, 0xf
0050343A  EB 03                           jmp 0x14050343f
0050343C  41 8B CB                        mov ecx, r11d
0050343F  41 8D 04 CA                     lea eax, [r10 + rcx*8]
00503443  41 0F BE D1                     movsx edx, r9b
00503447  48 63 C8                        movsxd rcx, eax
0050344A  48 8D 05 4F BB B1 FF            lea rax, [rip - 0x4e44b1]
00503451  44 0F BE 14 01                  movsx r10d, byte ptr [rcx + rax]
00503456  41 C1 FA 04                     sar r10d, 4
0050345A  44 89 54 24 44                  mov dword ptr [rsp + 0x44], r10d
0050345F  41 8B CA                        mov ecx, r10d
00503462  45 85 D2                        test r10d, r10d
00503465  0F 84 F7 05 00 00               je 0x140503a62
0050346B  83 E9 01                        sub ecx, 1
0050346E  0F 84 FE 06 00 00               je 0x140503b72
00503474  83 E9 01                        sub ecx, 1
00503477  0F 84 A5 06 00 00               je 0x140503b22
0050347D  83 E9 01                        sub ecx, 1
00503480  0F 84 52 06 00 00               je 0x140503ad8
00503486  83 E9 01                        sub ecx, 1
00503489  0F 84 44 06 00 00               je 0x140503ad3
0050348F  83 E9 01                        sub ecx, 1
00503492  0F 84 0F 06 00 00               je 0x140503aa7
00503498  83 E9 01                        sub ecx, 1
0050349B  0F 84 03 05 00 00               je 0x1405039a4
005034A1  83 F9 01                        cmp ecx, 1
005034A4  0F 85 DC 05 00 00               jne 0x140503a86
005034AA  83 FA 69                        cmp edx, 0x69
005034AD  0F 8F A4 01 00 00               jg 0x140503657
005034B3  74 31                           je 0x1405034e6
005034B5  83 EA 43                        sub edx, 0x43
005034B8  0F 84 36 01 00 00               je 0x1405035f4
005034BE  83 EA 10                        sub edx, 0x10
005034C1  0F 84 D4 00 00 00               je 0x14050359b
005034C7  83 EA 05                        sub edx, 5
005034CA  0F 84 0D 02 00 00               je 0x1405036dd
005034D0  83 EA 02                        sub edx, 2
005034D3  74 4D                           je 0x140503522
005034D5  83 EA 09                        sub edx, 9
005034D8  0F 84 24 01 00 00               je 0x140503602
005034DE  3B D1                           cmp edx, ecx
005034E0  0F 85 2A 03 00 00               jne 0x140503810
005034E6  41 83 CF 40                     or r15d, 0x40
005034EA  41 BA 0A 00 00 00               mov r10d, 0xa
005034F0  B9 00 02 00 00                  mov ecx, 0x200
005034F5  48 83 C7 08                     add rdi, 8
005034F9  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
005034FE  41 0F BA E7 0F                  bt r15d, 0xf
00503503  72 0B                           jb 0x140503510
00503505  41 0F BA E7 0C                  bt r15d, 0xc
0050350A  0F 83 14 02 00 00               jae 0x140503724
00503510  49 8B 00                        mov rax, qword ptr [r8]
00503513  41 F6 C7 40                     test r15b, 0x40
00503517  0F 84 3C 02 00 00               je 0x140503759
0050351D  E9 25 02 00 00                  jmp 0x140503747
00503522  49 8B 10                        mov rdx, qword ptr [r8]
00503525  48 83 C7 08                     add rdi, 8
00503529  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
0050352E  48 85 D2                        test rdx, rdx
00503531  74 48                           je 0x14050357b
00503533  48 8B 5A 08                     mov rbx, qword ptr [rdx + 8]
00503537  48 85 DB                        test rbx, rbx
0050353A  74 3F                           je 0x14050357b
0050353C  0F B7 02                        movzx eax, word ptr [rdx]
0050353F  66 39 42 02                     cmp word ptr [rdx + 2], ax
00503543  0F 82 4C 06 00 00               jb 0x140503b95
00503549  8B C8                           mov ecx, eax
0050354B  41 0F BA E7 0B                  bt r15d, 0xb
00503550  73 22                           jae 0x140503574
00503552  F7 D0                           not eax
00503554  A8 01                           test al, 1
00503556  0F 84 39 06 00 00               je 0x140503b95
0050355C  8B C3                           mov eax, ebx
0050355E  F7 D0                           not eax
00503560  A8 01                           test al, 1
00503562  0F 84 2D 06 00 00               je 0x140503b95
00503568  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
00503570  D1 E9                           shr ecx, 1
00503572  EB 1E                           jmp 0x140503592
00503574  44 89 5C 24 40                  mov dword ptr [rsp + 0x40], r11d
00503579  EB 17                           jmp 0x140503592
0050357B  48 8D 05 16 BA B1 FF            lea rax, [rip - 0x4e45ea]
00503582  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00503586  48 8B D8                        mov rbx, rax
00503589  48 FF C1                        inc rcx
0050358C  44 38 1C 08                     cmp byte ptr [rax + rcx], r11b
00503590  75 F7                           jne 0x140503589
00503592  89 4C 24 3C                     mov dword ptr [rsp + 0x3c], ecx
00503596  E9 75 02 00 00                  jmp 0x140503810
0050359B  41 F7 C7 30 08 00 00            test r15d, 0x830
005035A2  75 05                           jne 0x1405035a9
005035A4  41 0F BA EF 0B                  bts r15d, 0xb
005035A9  49 8B 18                        mov rbx, qword ptr [r8]
005035AC  41 83 FD FF                     cmp r13d, -1
005035B0  41 8B CD                        mov ecx, r13d
005035B3  B8 FF FF FF 7F                  mov eax, 0x7fffffff
005035B8  0F 44 C8                        cmove ecx, eax
005035BB  48 83 C7 08                     add rdi, 8
005035BF  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
005035C4  41 F7 C7 10 08 00 00            test r15d, 0x810
005035CB  0F 84 D5 00 00 00               je 0x1405036a6
005035D1  48 8B C3                        mov rax, rbx
005035D4  48 85 DB                        test rbx, rbx
005035D7  75 0E                           jne 0x1405035e7
005035D9  48 8D 1D 18 79 B2 FF            lea rbx, [rip - 0x4d86e8]
005035E0  48 8D 05 11 79 B2 FF            lea rax, [rip - 0x4d86ef]
005035E7  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
005035EF  E9 A6 00 00 00                  jmp 0x14050369a
005035F4  41 F7 C7 30 08 00 00            test r15d, 0x830
005035FB  75 05                           jne 0x140503602
005035FD  41 0F BA EF 0B                  bts r15d, 0xb
00503602  48 83 C7 08                     add rdi, 8
00503606  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
0050360B  41 F7 C7 10 08 00 00            test r15d, 0x810
00503612  74 2A                           je 0x14050363e
00503614  45 0F B7 08                     movzx r9d, word ptr [r8]
00503618  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
0050361D  41 B8 00 02 00 00               mov r8d, 0x200
00503623  48 8D 4C 24 3C                  lea rcx, [rsp + 0x3c]
00503628  E8 A7 EF FF FF                  call 0x1405025d4
0050362D  45 33 DB                        xor r11d, r11d
00503630  85 C0                           test eax, eax
00503632  74 19                           je 0x14050364d
00503634  C7 44 24 58 01 00 00 00         mov dword ptr [rsp + 0x58], 1
0050363C  EB 0F                           jmp 0x14050364d
0050363E  41 8A 00                        mov al, byte ptr [r8]
00503641  88 44 24 70                     mov byte ptr [rsp + 0x70], al
00503645  C7 44 24 3C 01 00 00 00         mov dword ptr [rsp + 0x3c], 1
0050364D  48 8D 5C 24 70                  lea rbx, [rsp + 0x70]
00503652  E9 B9 01 00 00                  jmp 0x140503810
00503657  83 EA 6E                        sub edx, 0x6e
0050365A  0F 84 0C 03 00 00               je 0x14050396c
00503660  83 EA 01                        sub edx, 1
00503663  0F 84 9D 00 00 00               je 0x140503706
00503669  83 EA 01                        sub edx, 1
0050366C  74 64                           je 0x1405036d2
0050366E  83 EA 03                        sub edx, 3
00503671  0F 84 32 FF FF FF               je 0x1405035a9
00503677  83 EA 02                        sub edx, 2
0050367A  0F 84 6A FE FF FF               je 0x1405034ea
00503680  83 FA 03                        cmp edx, 3
00503683  0F 85 87 01 00 00               jne 0x140503810
00503689  8D 42 24                        lea eax, [rdx + 0x24]
0050368C  EB 54                           jmp 0x1405036e2
0050368E  FF C9                           dec ecx
00503690  66 44 39 18                     cmp word ptr [rax], r11w
00503694  74 08                           je 0x14050369e
00503696  48 83 C0 02                     add rax, 2
0050369A  85 C9                           test ecx, ecx
0050369C  75 F0                           jne 0x14050368e
0050369E  48 2B C3                        sub rax, rbx
005036A1  48 D1 F8                        sar rax, 1
005036A4  EB 23                           jmp 0x1405036c9
005036A6  48 85 DB                        test rbx, rbx
005036A9  48 8D 05 E8 B8 B1 FF            lea rax, [rip - 0x4e4718]
005036B0  48 0F 45 C3                     cmovne rax, rbx
005036B4  48 8B D8                        mov rbx, rax
005036B7  EB 0A                           jmp 0x1405036c3
005036B9  FF C9                           dec ecx
005036BB  44 38 18                        cmp byte ptr [rax], r11b
005036BE  74 07                           je 0x1405036c7
005036C0  48 FF C0                        inc rax
005036C3  85 C9                           test ecx, ecx
005036C5  75 F2                           jne 0x1405036b9
005036C7  2B C3                           sub eax, ebx
005036C9  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
005036CD  E9 3E 01 00 00                  jmp 0x140503810
005036D2  41 BD 10 00 00 00               mov r13d, 0x10
005036D8  41 0F BA EF 0F                  bts r15d, 0xf
005036DD  B8 07 00 00 00                  mov eax, 7
005036E2  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
005036E6  45 84 FF                        test r15b, r15b
005036E9  79 10                           jns 0x1405036fb
005036EB  04 51                           add al, 0x51
005036ED  C6 44 24 38 30                  mov byte ptr [rsp + 0x38], 0x30
005036F2  88 44 24 39                     mov byte ptr [rsp + 0x39], al
005036F6  BE 02 00 00 00                  mov esi, 2
005036FB  41 BA 10 00 00 00               mov r10d, 0x10
00503701  E9 EA FD FF FF                  jmp 0x1405034f0
00503706  B8 08 00 00 00                  mov eax, 8
0050370B  44 8B D0                        mov r10d, eax
0050370E  45 84 FF                        test r15b, r15b
00503711  0F 89 D9 FD FF FF               jns 0x1405034f0
00503717  B9 00 02 00 00                  mov ecx, 0x200
0050371C  44 0B F9                        or r15d, ecx
0050371F  E9 D1 FD FF FF                  jmp 0x1405034f5
00503724  41 8B C7                        mov eax, r15d
00503727  83 E0 40                        and eax, 0x40
0050372A  41 F6 C7 20                     test r15b, 0x20
0050372E  74 10                           je 0x140503740
00503730  85 C0                           test eax, eax
00503732  74 06                           je 0x14050373a
00503734  49 0F BF 00                     movsx rax, word ptr [r8]
00503738  EB 0D                           jmp 0x140503747
0050373A  41 0F B7 00                     movzx eax, word ptr [r8]
0050373E  EB 19                           jmp 0x140503759
00503740  85 C0                           test eax, eax
00503742  74 12                           je 0x140503756
00503744  49 63 00                        movsxd rax, dword ptr [r8]
00503747  48 85 C0                        test rax, rax
0050374A  79 0D                           jns 0x140503759
0050374C  48 F7 D8                        neg rax
0050374F  41 0F BA EF 08                  bts r15d, 8
00503754  EB 03                           jmp 0x140503759
00503756  41 8B 00                        mov eax, dword ptr [r8]
00503759  41 F7 C7 00 90 00 00            test r15d, 0x9000
00503760  44 8B C0                        mov r8d, eax
00503763  4C 0F 45 C0                     cmovne r8, rax
00503767  45 85 ED                        test r13d, r13d
0050376A  79 08                           jns 0x140503774
0050376C  41 BD 01 00 00 00               mov r13d, 1
00503772  EB 0B                           jmp 0x14050377f
00503774  41 83 E7 F7                     and r15d, 0xfffffff7
00503778  44 3B E9                        cmp r13d, ecx
0050377B  44 0F 4F E9                     cmovg r13d, ecx
0050377F  49 8B C0                        mov rax, r8
00503782  48 F7 D8                        neg rax
00503785  1B C9                           sbb ecx, ecx
00503787  23 CE                           and ecx, esi
00503789  8B 74 24 5C                     mov esi, dword ptr [rsp + 0x5c]
0050378D  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00503791  44 8B C9                        mov r9d, ecx
00503794  48 8D 8D 6F 01 00 00            lea rcx, [rbp + 0x16f]
0050379B  41 8B C5                        mov eax, r13d
0050379E  41 FF CD                        dec r13d
005037A1  85 C0                           test eax, eax
005037A3  7F 05                           jg 0x1405037aa
005037A5  4D 85 C0                        test r8, r8
005037A8  74 1C                           je 0x1405037c6
005037AA  33 D2                           xor edx, edx
005037AC  49 8B C0                        mov rax, r8
005037AF  49 F7 F2                        div r10
005037B2  83 C2 30                        add edx, 0x30
005037B5  4C 8B C0                        mov r8, rax
005037B8  83 FA 39                        cmp edx, 0x39
005037BB  7E 02                           jle 0x1405037bf
005037BD  03 D6                           add edx, esi
005037BF  88 11                           mov byte ptr [rcx], dl
005037C1  48 FF C9                        dec rcx
005037C4  EB D5                           jmp 0x14050379b
005037C6  48 8D 85 6F 01 00 00            lea rax, [rbp + 0x16f]
005037CD  41 8B F1                        mov esi, r9d
005037D0  2B C1                           sub eax, ecx
005037D2  48 8D 59 01                     lea rbx, [rcx + 1]
005037D6  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
005037DA  41 0F BA E7 09                  bt r15d, 9
005037DF  73 2C                           jae 0x14050380d
005037E1  85 C0                           test eax, eax
005037E3  74 0F                           je 0x1405037f4
005037E5  80 3B 30                        cmp byte ptr [rbx], 0x30
005037E8  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
005037ED  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
005037F2  74 19                           je 0x14050380d
005037F4  48 FF CB                        dec rbx
005037F7  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
005037FC  FF C0                           inc eax
005037FE  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
00503803  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
00503807  41 8B F1                        mov esi, r9d
0050380A  C6 03 30                        mov byte ptr [rbx], 0x30
0050380D  45 33 DB                        xor r11d, r11d
00503810  44 39 5C 24 58                  cmp dword ptr [rsp + 0x58], r11d
00503815  0F 85 66 02 00 00               jne 0x140503a81
0050381B  41 F6 C7 40                     test r15b, 0x40
0050381F  74 33                           je 0x140503854
00503821  41 0F BA E7 08                  bt r15d, 8
00503826  73 07                           jae 0x14050382f
00503828  C6 44 24 38 2D                  mov byte ptr [rsp + 0x38], 0x2d
0050382D  EB 0B                           jmp 0x14050383a
0050382F  41 F6 C7 01                     test r15b, 1
00503833  74 12                           je 0x140503847
00503835  C6 44 24 38 2B                  mov byte ptr [rsp + 0x38], 0x2b
0050383A  41 BE 01 00 00 00               mov r14d, 1
00503840  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00503845  EB 12                           jmp 0x140503859
00503847  41 F6 C7 02                     test r15b, 2
0050384B  74 07                           je 0x140503854
0050384D  C6 44 24 38 20                  mov byte ptr [rsp + 0x38], 0x20
00503852  EB E6                           jmp 0x14050383a
00503854  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
00503859  8B 74 24 48                     mov esi, dword ptr [rsp + 0x48]
0050385D  41 8B FF                        mov edi, r15d
00503860  2B 74 24 3C                     sub esi, dword ptr [rsp + 0x3c]
00503864  41 2B F6                        sub esi, r14d
00503867  83 E7 0C                        and edi, 0xc
0050386A  75 13                           jne 0x14050387f
0050386C  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00503871  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00503876  8B D6                           mov edx, esi
00503878  B1 20                           mov cl, 0x20
0050387A  E8 B1 03 00 00                  call 0x140503c30
0050387F  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00503884  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00503889  41 8B D6                        mov edx, r14d
0050388C  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
00503891  E8 F2 03 00 00                  call 0x140503c88
00503896  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
0050389B  83 FF 08                        cmp edi, 8
0050389E  75 11                           jne 0x1405038b1
005038A0  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
005038A5  4D 8B C6                        mov r8, r14
005038A8  8B D6                           mov edx, esi
005038AA  B1 30                           mov cl, 0x30
005038AC  E8 7F 03 00 00                  call 0x140503c30
005038B1  83 7C 24 40 00                  cmp dword ptr [rsp + 0x40], 0
005038B6  8B 7C 24 3C                     mov edi, dword ptr [rsp + 0x3c]
005038BA  74 66                           je 0x140503922
005038BC  85 FF                           test edi, edi
005038BE  7E 62                           jle 0x140503922
005038C0  83 64 24 68 00                  and dword ptr [rsp + 0x68], 0
005038C5  4C 8B F3                        mov r14, rbx
005038C8  45 0F B7 0E                     movzx r9d, word ptr [r14]
005038CC  48 8D 95 70 01 00 00            lea rdx, [rbp + 0x170]
005038D3  41 B8 06 00 00 00               mov r8d, 6
005038D9  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
005038DE  4D 8D 76 02                     lea r14, [r14 + 2]
005038E2  FF CF                           dec edi
005038E4  E8 EB EC FF FF                  call 0x1405025d4
005038E9  45 33 DB                        xor r11d, r11d
005038EC  85 C0                           test eax, eax
005038EE  75 27                           jne 0x140503917
005038F0  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
005038F4  85 D2                           test edx, edx
005038F6  74 1F                           je 0x140503917
005038F8  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
005038FD  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00503902  48 8D 8D 70 01 00 00            lea rcx, [rbp + 0x170]
00503909  E8 7A 03 00 00                  call 0x140503c88
0050390E  45 33 DB                        xor r11d, r11d
00503911  85 FF                           test edi, edi
00503913  75 B3                           jne 0x1405038c8
00503915  EB 20                           jmp 0x140503937
00503917  41 83 CE FF                     or r14d, 0xffffffff
0050391B  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
00503920  EB 1A                           jmp 0x14050393c
00503922  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00503927  4D 8B C6                        mov r8, r14
0050392A  8B D7                           mov edx, edi
0050392C  48 8B CB                        mov rcx, rbx
0050392F  E8 54 03 00 00                  call 0x140503c88
00503934  45 33 DB                        xor r11d, r11d
00503937  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
0050393C  45 85 F6                        test r14d, r14d
0050393F  78 22                           js 0x140503963
00503941  41 F6 C7 04                     test r15b, 4
00503945  74 1C                           je 0x140503963
00503947  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
0050394C  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00503951  8B D6                           mov edx, esi
00503953  B1 20                           mov cl, 0x20
00503955  E8 D6 02 00 00                  call 0x140503c30
0050395A  8B 74 24 30                     mov esi, dword ptr [rsp + 0x30]
0050395E  E9 16 01 00 00                  jmp 0x140503a79
00503963  8B 74 24 30                     mov esi, dword ptr [rsp + 0x30]
00503967  E9 15 01 00 00                  jmp 0x140503a81
0050396C  48 83 C7 08                     add rdi, 8
00503970  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00503975  49 8B 38                        mov rdi, qword ptr [r8]
00503978  E8 17 0B 00 00                  call 0x140504494
0050397D  45 33 DB                        xor r11d, r11d
00503980  85 C0                           test eax, eax
00503982  0F 84 0D 02 00 00               je 0x140503b95
00503988  41 F6 C7 20                     test r15b, 0x20
0050398C  74 06                           je 0x140503994
0050398E  66 44 89 37                     mov word ptr [rdi], r14w
00503992  EB 03                           jmp 0x140503997
00503994  44 89 37                        mov dword ptr [rdi], r14d
00503997  C7 44 24 58 01 00 00 00         mov dword ptr [rsp + 0x58], 1
0050399F  E9 DD 00 00 00                  jmp 0x140503a81
005039A4  41 80 F9 49                     cmp r9b, 0x49
005039A8  74 29                           je 0x1405039d3
005039AA  41 80 F9 68                     cmp r9b, 0x68
005039AE  74 70                           je 0x140503a20
005039B0  41 80 F9 6A                     cmp r9b, 0x6a
005039B4  74 1D                           je 0x1405039d3
005039B6  B2 6C                           mov dl, 0x6c
005039B8  44 3A CA                        cmp r9b, dl
005039BB  74 44                           je 0x140503a01
005039BD  41 80 F9 74                     cmp r9b, 0x74
005039C1  74 10                           je 0x1405039d3
005039C3  41 80 F9 77                     cmp r9b, 0x77
005039C7  74 2E                           je 0x1405039f7
005039C9  41 80 F9 7A                     cmp r9b, 0x7a
005039CD  0F 85 B3 00 00 00               jne 0x140503a86
005039D3  41 0F BA EF 0F                  bts r15d, 0xf
005039D8  41 80 F9 49                     cmp r9b, 0x49
005039DC  75 5F                           jne 0x140503a3d
005039DE  41 8A 04 24                     mov al, byte ptr [r12]
005039E2  3C 36                           cmp al, 0x36
005039E4  75 40                           jne 0x140503a26
005039E6  41 80 7C 24 01 34               cmp byte ptr [r12 + 1], 0x34
005039EC  75 55                           jne 0x140503a43
005039EE  49 83 C4 02                     add r12, 2
005039F2  E9 8F 00 00 00                  jmp 0x140503a86
005039F7  41 0F BA EF 0B                  bts r15d, 0xb
005039FC  E9 85 00 00 00                  jmp 0x140503a86
00503A01  41 8A 0C 24                     mov cl, byte ptr [r12]
00503A05  3A CA                           cmp cl, dl
00503A07  75 03                           jne 0x140503a0c
00503A09  49 FF C4                        inc r12
00503A0C  3A CA                           cmp cl, dl
00503A0E  B8 00 10 00 00                  mov eax, 0x1000
00503A13  B9 10 00 00 00                  mov ecx, 0x10
00503A18  0F 45 C1                        cmovne eax, ecx
00503A1B  44 0B F8                        or r15d, eax
00503A1E  EB 66                           jmp 0x140503a86
00503A20  41 83 CF 20                     or r15d, 0x20
00503A24  EB 60                           jmp 0x140503a86
00503A26  3C 33                           cmp al, 0x33
00503A28  75 19                           jne 0x140503a43
00503A2A  41 80 7C 24 01 32               cmp byte ptr [r12 + 1], 0x32
00503A30  75 11                           jne 0x140503a43
00503A32  49 83 C4 02                     add r12, 2
00503A36  41 0F BA F7 0F                  btr r15d, 0xf
00503A3B  EB 49                           jmp 0x140503a86
00503A3D  41 80 F9 6A                     cmp r9b, 0x6a
00503A41  74 43                           je 0x140503a86
00503A43  41 8A 04 24                     mov al, byte ptr [r12]
00503A47  2C 58                           sub al, 0x58
00503A49  3C 20                           cmp al, 0x20
00503A4B  77 10                           ja 0x140503a5d
00503A4D  48 B9 01 10 82 20 01 00 00 00   movabs rcx, 0x120821001
00503A57  48 0F A3 C1                     bt rcx, rax
00503A5B  72 29                           jb 0x140503a86
00503A5D  44 89 5C 24 44                  mov dword ptr [rsp + 0x44], r11d
00503A62  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00503A67  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00503A6C  41 8A C9                        mov cl, r9b
00503A6F  44 89 5C 24 40                  mov dword ptr [rsp + 0x40], r11d
00503A74  E8 67 01 00 00                  call 0x140503be0
00503A79  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
00503A7E  45 33 DB                        xor r11d, r11d
00503A81  44 8B 54 24 44                  mov r10d, dword ptr [rsp + 0x44]
00503A86  45 8A 0C 24                     mov r9b, byte ptr [r12]
00503A8A  48 8D 0D 0F B5 B1 FF            lea rcx, [rip - 0x4e4af1]
00503A91  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
00503A96  45 84 C9                        test r9b, r9b
00503A99  0F 85 78 F9 FF FF               jne 0x140503417
00503A9F  41 8B C6                        mov eax, r14d
00503AA2  E9 05 01 00 00                  jmp 0x140503bac
00503AA7  41 80 F9 2A                     cmp r9b, 0x2a
00503AAB  75 17                           jne 0x140503ac4
00503AAD  45 8B 28                        mov r13d, dword ptr [r8]
00503AB0  48 83 C7 08                     add rdi, 8
00503AB4  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00503AB9  45 85 ED                        test r13d, r13d
00503ABC  79 C8                           jns 0x140503a86
00503ABE  41 83 CD FF                     or r13d, 0xffffffff
00503AC2  EB C2                           jmp 0x140503a86
00503AC4  47 8D 6C AD 00                  lea r13d, [r13 + r13*4]
00503AC9  45 8D 6D E8                     lea r13d, [r13 - 0x18]
00503ACD  46 8D 2C 6A                     lea r13d, [rdx + r13*2]
00503AD1  EB B3                           jmp 0x140503a86
00503AD3  45 8B EB                        mov r13d, r11d
00503AD6  EB AE                           jmp 0x140503a86
00503AD8  41 80 F9 2A                     cmp r9b, 0x2a
00503ADC  75 2E                           jne 0x140503b0c
00503ADE  45 8B 00                        mov r8d, dword ptr [r8]
00503AE1  48 83 C7 08                     add rdi, 8
00503AE5  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00503AEA  41 8B C8                        mov ecx, r8d
00503AED  45 85 C0                        test r8d, r8d
00503AF0  79 04                           jns 0x140503af6
00503AF2  41 83 CF 04                     or r15d, 4
00503AF6  41 8B C0                        mov eax, r8d
00503AF9  41 F7 D8                        neg r8d
00503AFC  85 C0                           test eax, eax
00503AFE  44 0F 49 C1                     cmovns r8d, ecx
00503B02  44 89 44 24 48                  mov dword ptr [rsp + 0x48], r8d
00503B07  E9 7A FF FF FF                  jmp 0x140503a86
00503B0C  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
00503B10  8D 0C 89                        lea ecx, [rcx + rcx*4]
00503B13  8D 49 E8                        lea ecx, [rcx - 0x18]
00503B16  8D 0C 4A                        lea ecx, [rdx + rcx*2]
00503B19  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00503B1D  E9 64 FF FF FF                  jmp 0x140503a86
00503B22  41 80 F9 20                     cmp r9b, 0x20
00503B26  74 41                           je 0x140503b69
00503B28  41 80 F9 23                     cmp r9b, 0x23
00503B2C  74 31                           je 0x140503b5f
00503B2E  41 80 F9 2B                     cmp r9b, 0x2b
00503B32  74 22                           je 0x140503b56
00503B34  41 80 F9 2D                     cmp r9b, 0x2d
00503B38  74 13                           je 0x140503b4d
00503B3A  41 80 F9 30                     cmp r9b, 0x30
00503B3E  0F 85 42 FF FF FF               jne 0x140503a86
00503B44  41 83 CF 08                     or r15d, 8
00503B48  E9 39 FF FF FF                  jmp 0x140503a86
00503B4D  41 83 CF 04                     or r15d, 4
00503B51  E9 30 FF FF FF                  jmp 0x140503a86
00503B56  41 83 CF 01                     or r15d, 1
00503B5A  E9 27 FF FF FF                  jmp 0x140503a86
00503B5F  41 0F BA EF 07                  bts r15d, 7
00503B64  E9 1D FF FF FF                  jmp 0x140503a86
00503B69  41 83 CF 02                     or r15d, 2
00503B6D  E9 14 FF FF FF                  jmp 0x140503a86
00503B72  44 89 5C 24 58                  mov dword ptr [rsp + 0x58], r11d
00503B77  41 8B F3                        mov esi, r11d
00503B7A  44 89 5C 24 48                  mov dword ptr [rsp + 0x48], r11d
00503B7F  45 8B FB                        mov r15d, r11d
00503B82  44 89 5C 24 30                  mov dword ptr [rsp + 0x30], r11d
00503B87  41 83 CD FF                     or r13d, 0xffffffff
00503B8B  44 89 5C 24 40                  mov dword ptr [rsp + 0x40], r11d
00503B90  E9 F1 FE FF FF                  jmp 0x140503a86
00503B95  45 33 C9                        xor r9d, r9d
00503B98  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00503B9D  45 33 C0                        xor r8d, r8d
00503BA0  33 D2                           xor edx, edx
00503BA2  33 C9                           xor ecx, ecx
00503BA4  E8 A7 A9 F9 FF                  call 0x14049e550
00503BA9  83 C8 FF                        or eax, 0xffffffff
00503BAC  48 8B 8D 78 01 00 00            mov rcx, qword ptr [rbp + 0x178]
00503BB3  48 33 CC                        xor rcx, rsp
00503BB6  E8 85 8A 1A 00                  call 0x1406ac640
00503BBB  48 8B 9C 24 D0 02 00 00         mov rbx, qword ptr [rsp + 0x2d0]
00503BC3  48 81 C4 80 02 00 00            add rsp, 0x280
00503BCA  41 5F                           pop r15
00503BCC  41 5E                           pop r14
00503BCE  41 5D                           pop r13
00503BD0  41 5C                           pop r12
00503BD2  5F                              pop rdi
00503BD3  5E                              pop rsi
00503BD4  5D                              pop rbp
00503BD5  C3                              ret
00503BD6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall output_l(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m248;
    unsigned int v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned int v_stack_m25C;
    unsigned int v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned int v_stack_m270;
    unsigned int v_stack_m274;
    unsigned int v_stack_m278;
    unsigned int v_stack_m27C;
    unsigned __int8 v_stack_m27F;
    unsigned __int8 v_stack_m280;
    unsigned int v_stack_m284;
    unsigned int v_stack_m288;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m49;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (640);
    result = (*(unsigned __int64 *)(v_rip + 9466802)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m258 = a1;
    a1 = 0;
    v_stack_m268 = a4;
    v_stack_m25C = 0;
    v_stack_m270 = 0;
    v_stack_m288 = 0;
    v_stack_m260 = 0;
    a2 = 0;
    result = memset(v_stack_m248, a2, 512, a4);
    v_r11 = 0;
    v_stack_m278 = 0;
    if (0 == 0) goto loc_00503B95;
    if (0 == 0) goto loc_00503B95;
    v_stack_m284 = 0;
    v_stack_m27C = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(a2)) == 0) goto loc_00503A9F;
loc_00503417:
    v_r12 = (a2) + 1;
    if (sign_flag) goto loc_00503A9F;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2) - 32)) > 90) goto loc_0050343C;
    a1 = (unsigned int)(((__int8)(*(unsigned __int8 *)((__int8)((unsigned __int8)(*(unsigned __int8 *)(a2))) + v_rip - 5129335 * 1 - 32))) & (15));
    goto loc_0050343F;
loc_0050343C:
loc_0050343F:
    v_r10 = (unsigned int)(((__int8)(*(unsigned __int8 *)((int)((unsigned int)(0 + 0 * 8)) + v_rip - 5129393 * 1))) >> (4));
    v_stack_m274 = (unsigned int)(v_r10);
    if ((unsigned int)(v_r10) == 0) goto loc_00503A62;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - (1));
    if (condition_is_equal) goto loc_00503B72;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00503B22;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00503AD8;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00503AD3;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00503AA7;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005039A4;
    if (((unsigned int)(a1)) != 1) goto loc_00503A86;
    if (((unsigned int)((__int8)((unsigned __int8)(*(unsigned __int8 *)(a2))))) > 105) goto loc_00503657;
    if (((unsigned int)((__int8)((unsigned __int8)(*(unsigned __int8 *)(a2))))) == 105) goto loc_005034E6;
    a2 = (unsigned int)(((__int8)((unsigned __int8)(*(unsigned __int8 *)(a2)))) - (67));
    if (condition_is_equal) goto loc_005035F4;
    a2 = (unsigned int)((a2) - (16));
    if (condition_is_equal) goto loc_0050359B;
    a2 = (unsigned int)((a2) - (5));
    if (condition_is_equal) goto loc_005036DD;
    a2 = (unsigned int)((a2) - (2));
    if (condition_is_equal) goto loc_00503522;
    a2 = (unsigned int)((a2) - (9));
    if (condition_is_equal) goto loc_00503602;
    if (((unsigned int)(a2)) != ((unsigned int)(a1))) goto loc_00503810;
loc_005034E6:
    v_r15 = (unsigned int)((0) | (64));
loc_005034EA:
loc_005034F0:
loc_005034F5:
    v_rdi = (a4) + (8);
    v_stack_m268 = v_rdi;
    if (condition_is_below) goto loc_00503510;
    if (condition_is_above_or_equal) goto loc_00503724;
loc_00503510:
    if ((((unsigned __int8)(v_r15)) & (64)) == 0) goto loc_00503759;
    goto loc_00503747;
loc_00503522:
    v_rdi = (v_rdi) + (8);
    v_stack_m268 = v_rdi;
    if (*(unsigned __int64 *)(a4) == 0) goto loc_0050357B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 8) == 0) goto loc_0050357B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a4) + 2)) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4))))) goto loc_00503B95;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a4) + 2)) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4))))) goto loc_00503574;
    result = (unsigned int)(~(*(unsigned __int16 *)(*(unsigned __int64 *)(a4))));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00503B95;
    result = (unsigned int)(~((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 8)))));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00503B95;
    v_stack_m278 = 1;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4))))) >> (1));
    goto loc_00503592;
loc_00503574:
    v_stack_m278 = 0;
    goto loc_00503592;
loc_0050357B:
    a1 = (a1) | (-1);
loc_00503589:
    a1 = (a1) + 1;
    if ((*(unsigned __int8 *)(v_rip - 5129706 + a1 * 1)) != 0) goto loc_00503589;
loc_00503592:
    v_stack_m27C = (unsigned int)(a1);
    goto loc_00503810;
loc_0050359B:
    if ((((unsigned int)(v_r15)) & (0x830ULL)) == 0) {
    }
    a1 = 0;
    if (0 == -1) { a1 = (unsigned int)((unsigned int)(0x7FFFFFFFULL)); }
    v_rdi = (v_rdi) + (8);
    v_stack_m268 = v_rdi;
    if ((((unsigned int)(v_r15)) & (0x810ULL)) == 0) goto loc_005036A6;
    result = *(unsigned __int64 *)(a4);
    v_rbx = *(unsigned __int64 *)(a4);
    if (*(unsigned __int64 *)(a4) == 0) {
        v_rbx = v_rip - 5080808;
        result = v_rip - 5080815;
    }
    v_stack_m278 = 1;
    goto loc_0050369A;
loc_005035F4:
    if ((((unsigned int)(v_r15)) & (0x830ULL)) == 0) {
    }
    v_rdi = (v_rdi) + (8);
    v_stack_m268 = v_rdi;
    if ((((unsigned int)(v_r15)) & (0x810ULL)) == 0) goto loc_0050363E;
    result = wctomb_s(v_stack_m27C, v_stack_m248, 512, *(unsigned __int16 *)(a4));
    v_r11 = 0;
    if ((unsigned int)(result) == 0) goto loc_0050364D;
    v_stack_m260 = 1;
    goto loc_0050364D;
loc_0050363E:
    v_stack_m248 = (unsigned __int8)(*(unsigned __int8 *)(512));
    v_stack_m27C = 1;
loc_0050364D:
    goto loc_00503810;
loc_00503657:
    a2 = (unsigned int)((v_stack_m248) - (110));
    if (condition_is_equal) goto loc_0050396C;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00503706;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_005036D2;
    a2 = (unsigned int)((a2) - (3));
    if (condition_is_equal) goto loc_005035A9;
    a2 = (unsigned int)((a2) - (2));
    if (condition_is_equal) goto loc_005034EA;
    if (((unsigned int)(a2)) != 3) goto loc_00503810;
    goto loc_005036E2;
loc_0050368E:
    a1 = (unsigned int)((v_stack_m27C) - 1);
    if ((*(unsigned __int16 *)(a2 + 36)) == 0) goto loc_0050369E;
    result = (a2 + 36) + (2);
loc_0050369A:
    if ((unsigned int)(a1) != 0) goto loc_0050368E;
loc_0050369E:
    result = (result) - (v_stack_m248);
    result = (result) >> (1);
    goto loc_005036C9;
loc_005036A6:
    result = v_rip - 5130008;
    if (v_stack_m248 != 0) { result = v_stack_m248; }
    goto loc_005036C3;
loc_005036B9:
    a1 = (unsigned int)((a1) - 1);
    if ((*(unsigned __int8 *)(result)) == 0) goto loc_005036C7;
    result = (result) + 1;
loc_005036C3:
    if ((unsigned int)(a1) != 0) goto loc_005036B9;
loc_005036C7:
    result = (unsigned int)((result) - ((unsigned int)(result)));
loc_005036C9:
    v_stack_m27C = (unsigned int)(result);
    goto loc_00503810;
loc_005036D2:
loc_005036DD:
loc_005036E2:
    v_stack_m25C = 7;
    result = 7;
    v_rsi = 0;
    if (sign_flag) {
        result = (unsigned __int8)((7) + (81));
        v_stack_m280 = 48;
        v_stack_m27F = (unsigned __int8)(result);
        v_rsi = 2;
    }
    goto loc_005034F0;
loc_00503706:
    if (!sign_flag) goto loc_005034F0;
    v_r15 = (unsigned int)((v_r15) | (512));
    goto loc_005034F5;
loc_00503724:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (64));
    if ((((unsigned __int8)(v_r15)) & (32)) == 0) goto loc_00503740;
    if ((unsigned int)(result) == 0) goto loc_0050373A;
    goto loc_00503747;
loc_0050373A:
    goto loc_00503759;
loc_00503740:
    if ((unsigned int)(*(unsigned __int16 *)(512)) == 0) goto loc_00503756;
loc_00503747:
    if (!sign_flag) goto loc_00503759;
    result = -((int)(*(unsigned int *)(512)));
    goto loc_00503759;
loc_00503756:
loc_00503759:
    a3 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(512))));
    if ((((unsigned int)(v_r15)) & (0x9000ULL)) != 0) { a3 = (unsigned int)(*(unsigned int *)(512)); }
    if (!sign_flag) goto loc_00503774;
    goto loc_0050377F;
loc_00503774:
    v_r15 = (unsigned int)((v_r15) & (0xFFFFFFF7ULL));
    v_r13 = 1;
    if (1 > 512) { v_r13 = 512; }
loc_0050377F:
    result = -(a3);
    a1 = (unsigned int)((512) & ((unsigned int)(v_rsi)));
    v_stack_m288 = (unsigned int)(a1);
loc_0050379B:
    v_r13 = (unsigned int)((v_r13) - 1);
    if (condition_is_greater) goto loc_005037AA;
    if (a3 == 0) goto loc_005037C6;
loc_005037AA:
    a2 = 0;
    a2 = (unsigned int)((a2) + (48));
    if (((unsigned int)(a2)) >= = 57) {
        a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)(v_stack_m25C))));
    }
    *(unsigned __int8 *)(v_stack_m49) = (unsigned __int8)(a2);
    a1 = (v_stack_m49) - 1;
    goto loc_0050379B;
loc_005037C6:
    result = (unsigned int)((v_stack_m49) - ((unsigned int)(a1)));
    v_stack_m27C = (unsigned int)(result);
    if (condition_is_above_or_equal) goto loc_0050380D;
    if ((unsigned int)(result) == 0) goto loc_005037F4;
    v_stack_m268 = v_rdi;
    v_stack_m288 = (unsigned int)((unsigned int)((unsigned int)(a1)));
    v_rbx = a1 + 1;
    v_rsi = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1))));
    if ((*(unsigned __int8 *)(a1 + 1)) != 48) {
        v_rbx = (a1 + 1) - 1;
        v_stack_m268 = v_rdi;
        result = (unsigned int)((result) + 1);
        v_stack_m288 = (unsigned int)((unsigned int)((unsigned int)(a1)));
        v_stack_m27C = (unsigned int)(result);
        v_rsi = (unsigned int)((unsigned int)((unsigned int)(a1)));
        *(unsigned __int8 *)(v_rbx) = 48;
    }
    v_r11 = 0;
loc_00503810:
    if (v_stack_m260 != 0) goto loc_00503A81;
    if ((((unsigned __int8)(v_r15)) & (64)) == 0) goto loc_00503854;
    if (condition_is_above_or_equal) goto loc_0050382F;
    v_stack_m280 = 45;
    goto loc_0050383A;
loc_0050382F:
    if ((((unsigned __int8)(v_r15)) & (1)) == 0) goto loc_00503847;
    v_stack_m280 = 43;
loc_0050383A:
    v_stack_m288 = 1;
    goto loc_00503859;
loc_00503847:
    if ((((unsigned __int8)(v_r15)) & (2)) == 0) goto loc_00503854;
    v_stack_m280 = 32;
    goto loc_0050383A;
loc_00503854:
loc_00503859:
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m270)) - (v_stack_m27C));
    v_rsi = (unsigned int)((v_rsi) - ((unsigned int)((unsigned int)(v_stack_m288))));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (12));
    if (!(condition_is_not_equal)) {
        a3 = v_stack_m258;
        a4 = v_stack_m284;
        a2 = (unsigned int)(v_rsi);
        a1 = 32;
        result = write_multi_char(a1, a2, a3, a4);
    }
    result = write_string(v_stack_m280, (unsigned int)((unsigned int)((unsigned int)(v_stack_m288))), v_stack_m258, v_stack_m284);
    if (((unsigned int)(v_rdi)) == 8) {
        a4 = v_stack_m284;
        a3 = v_stack_m258;
        a2 = (unsigned int)(v_rsi);
        a1 = 48;
        result = write_multi_char(a1, a2, a3, a4);
    }
    if (v_stack_m278 == 0) goto loc_00503922;
    if (condition_is_less_or_equal) goto loc_00503922;
loc_005038C8:
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m27C)) - 1);
    result = wctomb_s(v_stack_m250, v_stack_m48, 6, *(unsigned __int16 *)(v_rbx));
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_00503917;
    if ((unsigned int)((unsigned int)(v_stack_m250)) == 0) goto loc_00503917;
    result = write_string(v_stack_m48, (unsigned int)(v_stack_m250), v_stack_m258, v_stack_m284);
    v_r11 = 0;
    if ((unsigned int)(v_rdi) != 0) goto loc_005038C8;
    goto loc_00503937;
loc_00503917:
    v_r14 = (unsigned int)((v_rbx + 2) | (0xFFFFFFFFULL));
    v_stack_m284 = (unsigned int)(v_r14);
    goto loc_0050393C;
loc_00503922:
    result = write_string(v_rbx, (unsigned int)((unsigned int)(v_rdi)), v_r14, v_stack_m284);
    v_r11 = 0;
loc_00503937:
loc_0050393C:
    if (sign_flag) goto loc_00503963;
    if ((((unsigned __int8)(v_r15)) & (4)) == 0) goto loc_00503963;
    result = write_multi_char(32, (unsigned int)((unsigned int)(v_rsi)), v_stack_m258, v_stack_m284);
    goto loc_00503A79;
loc_00503963:
    goto loc_00503A81;
loc_0050396C:
    v_rdi = (v_rdi) + (8);
    v_stack_m268 = v_rdi;
    result = get_printf_count_output(32, (unsigned int)((unsigned int)(v_rsi)), v_stack_m258, v_stack_m284);
    v_r11 = 0;
    if ((unsigned int)(result) == 0) goto loc_00503B95;
    if ((((unsigned __int8)(v_r15)) & (32)) == 0) goto loc_00503994;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m258)) = (unsigned __int16)((unsigned int)(v_stack_m284));
    goto loc_00503997;
loc_00503994:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m258)) = (unsigned int)((unsigned int)(v_stack_m284));
loc_00503997:
    v_stack_m260 = 1;
    goto loc_00503A81;
loc_005039A4:
    if (((unsigned __int8)(v_stack_m284)) == 73) goto loc_005039D3;
    if (((unsigned __int8)(v_stack_m284)) == 104) goto loc_00503A20;
    if (((unsigned __int8)(v_stack_m284)) == 106) goto loc_005039D3;
    if (((unsigned __int8)(v_stack_m284)) == 108) goto loc_00503A01;
    if (((unsigned __int8)(v_stack_m284)) == 116) goto loc_005039D3;
    if (((unsigned __int8)(v_stack_m284)) == 119) goto loc_005039F7;
    if (((unsigned __int8)(v_stack_m284)) != 122) goto loc_00503A86;
loc_005039D3:
    if (((unsigned __int8)(v_stack_m284)) != 73) goto loc_00503A3D;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r12))) != 54) goto loc_00503A26;
    if ((*(unsigned __int8 *)(v_r12 + 1)) != 52) goto loc_00503A43;
    v_r12 = (v_r12) + (2);
    goto loc_00503A86;
loc_005039F7:
    goto loc_00503A86;
loc_00503A01:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r12))) == 108) {
        v_r12 = (v_r12) + 1;
    }
    result = (unsigned int)(0x1000ULL);
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r12))) != 108) { result = 16; }
    v_r15 = (unsigned int)((v_r15) | ((unsigned int)(result)));
    goto loc_00503A86;
loc_00503A20:
    v_r15 = (unsigned int)((v_r15) | (32));
    goto loc_00503A86;
loc_00503A26:
    if (((unsigned __int8)(result)) != 51) goto loc_00503A43;
    if ((*(unsigned __int8 *)(v_r12 + 1)) != 50) goto loc_00503A43;
    v_r12 = (v_r12) + (2);
    goto loc_00503A86;
loc_00503A3D:
    if (((unsigned __int8)(v_stack_m284)) == 106) goto loc_00503A86;
loc_00503A43:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r12)) - (88));
    if (((unsigned __int8)(result)) > 32) goto loc_00503A5D;
    if (((unsigned __int8)(result)) < 32) goto loc_00503A86;
loc_00503A5D:
    v_stack_m274 = 0;
loc_00503A62:
    v_stack_m278 = 0;
    result = write_char((unsigned __int8)(v_stack_m284), v_stack_m258, v_stack_m284, v_stack_m284);
loc_00503A79:
    v_r11 = 0;
loc_00503A81:
loc_00503A86:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_r12)) != 0) goto loc_00503417;
loc_00503A9F:
    goto loc_00503BAC;
loc_00503AA7:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r12))) != 42) goto loc_00503AC4;
    v_rdi = (v_stack_m268) + (8);
    v_stack_m268 = v_rdi;
    if (!sign_flag) goto loc_00503A86;
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m284))) | (0xFFFFFFFFULL));
    goto loc_00503A86;
loc_00503AC4:
    goto loc_00503A86;
loc_00503AD3:
    goto loc_00503A86;
loc_00503AD8:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r12))) != 42) goto loc_00503B0C;
    v_rdi = (v_rdi) + (8);
    v_stack_m268 = v_rdi;
    if (sign_flag) {
        v_r15 = (unsigned int)((v_r15) | (4));
    }
    a3 = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_stack_m284))));
    if (!sign_flag) { a3 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m284))))); }
    v_stack_m270 = (unsigned int)(a3);
    goto loc_00503A86;
loc_00503B0C:
    v_stack_m270 = (unsigned int)(v_stack_m258 + (unsigned int)(v_stack_m270) + (unsigned int)(v_stack_m270) * 4 - 24 * 2);
    goto loc_00503A86;
loc_00503B22:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r12))) == 32) goto loc_00503B69;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r12))) == 35) goto loc_00503B5F;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r12))) == 43) goto loc_00503B56;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r12))) == 45) goto loc_00503B4D;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r12))) != 48) goto loc_00503A86;
    v_r15 = (unsigned int)((v_r15) | (8));
    goto loc_00503A86;
loc_00503B4D:
    v_r15 = (unsigned int)((v_r15) | (4));
    goto loc_00503A86;
loc_00503B56:
    v_r15 = (unsigned int)((v_r15) | (1));
    goto loc_00503A86;
loc_00503B5F:
    goto loc_00503A86;
loc_00503B69:
    v_r15 = (unsigned int)((v_r15) | (2));
    goto loc_00503A86;
loc_00503B72:
    v_stack_m260 = 0;
    v_stack_m270 = 0;
    v_stack_m288 = 0;
    v_r13 = (unsigned int)((0) | (0xFFFFFFFFULL));
    v_stack_m278 = 0;
    goto loc_00503A86;
loc_00503B95:
    a4 = 0;
    v_stack_m298 = 0;
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = EmpCheckErrataList(a1, a2, a3, a4);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
loc_00503BAC:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (640);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t output_l(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m248;
    uint32_t v_stack_m250;
    uint64_t v_stack_m258;
    uint32_t v_stack_m25C;
    uint32_t v_stack_m260;
    uint64_t v_stack_m268;
    uint32_t v_stack_m270;
    uint32_t v_stack_m274;
    uint32_t v_stack_m278;
    uint32_t v_stack_m27C;
    uint8_t v_stack_m27F;
    uint8_t v_stack_m280;
    uint32_t v_stack_m284;
    uint32_t v_stack_m288;
    uint64_t v_stack_m298;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m49;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (640);
    result = (*(uint64_t *)(v_rip + 0x9073B2)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m258 = Arg1;
    Arg1 = 0;
    v_stack_m268 = Arg4;
    v_stack_m25C = 0;
    v_stack_m270 = 0;
    v_stack_m288 = 0;
    v_stack_m260 = 0;
    Arg2 = 0;
    result = memset(v_stack_m248, Arg2, 512, Arg4);
    local_r11 = 0;
    v_stack_m278 = 0;
    if (0 == 0) goto loc_00503B95;
    if (0 == 0) goto loc_00503B95;
    v_stack_m284 = 0;
    v_stack_m27C = 0;
    if ((uint8_t)(*(uint8_t *)(Arg2)) == 0) goto loc_00503A9F;
loc_00503417:
    local_r12 = (Arg2) + 1;
    if (sign_flag) goto loc_00503A9F;
    if (((uint8_t)(*(uint8_t *)(Arg2) - 32)) > 90) goto loc_0050343C;
    Arg1 = (uint32_t)(((int8_t)(*(uint8_t *)((int8_t)((uint8_t)(*(uint8_t *)(Arg2))) + v_rip - 0x4E4477 * 1 - 0x20))) & (15));
    goto loc_0050343F;
loc_0050343C:
loc_0050343F:
    local_r10 = (uint32_t)(((int8_t)(*(uint8_t *)((int32_t)((uint32_t)(0 + 0x0 * 8)) + v_rip - 0x4E44B1 * 1))) >> (4));
    v_stack_m274 = (uint32_t)(local_r10);
    if ((uint32_t)(local_r10) == 0) goto loc_00503A62;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - (1));
    if (condition_is_equal) goto loc_00503B72;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00503B22;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00503AD8;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00503AD3;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00503AA7;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005039A4;
    if (((uint32_t)(Arg1)) != 1) goto loc_00503A86;
    if (((uint32_t)((int8_t)((uint8_t)(*(uint8_t *)(Arg2))))) > 105) goto loc_00503657;
    if (((uint32_t)((int8_t)((uint8_t)(*(uint8_t *)(Arg2))))) == 105) goto loc_005034E6;
    Arg2 = (uint32_t)(((int8_t)((uint8_t)(*(uint8_t *)(Arg2)))) - (67));
    if (condition_is_equal) goto loc_005035F4;
    Arg2 = (uint32_t)((Arg2) - (16));
    if (condition_is_equal) goto loc_0050359B;
    Arg2 = (uint32_t)((Arg2) - (5));
    if (condition_is_equal) goto loc_005036DD;
    Arg2 = (uint32_t)((Arg2) - (2));
    if (condition_is_equal) goto loc_00503522;
    Arg2 = (uint32_t)((Arg2) - (9));
    if (condition_is_equal) goto loc_00503602;
    if (((uint32_t)(Arg2)) != ((uint32_t)(Arg1))) goto loc_00503810;
loc_005034E6:
    local_r15 = (uint32_t)((0) | (64));
loc_005034EA:
loc_005034F0:
loc_005034F5:
    local_rdi = (Arg4) + (8);
    v_stack_m268 = local_rdi;
    if (condition_is_below) goto loc_00503510;
    if (condition_is_above_or_equal) goto loc_00503724;
loc_00503510:
    if ((((uint8_t)(local_r15)) & (64)) == 0) goto loc_00503759;
    goto loc_00503747;
loc_00503522:
    local_rdi = (local_rdi) + (8);
    v_stack_m268 = local_rdi;
    if (*(uint64_t *)(Arg4) == 0) goto loc_0050357B;
    if (*(uint64_t *)(*(uint64_t *)(Arg4) + 0x8) == 0) goto loc_0050357B;
    if ((*(uint16_t *)(*(uint64_t *)(Arg4) + 0x2)) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg4))))) goto loc_00503B95;
    if ((*(uint16_t *)(*(uint64_t *)(Arg4) + 0x2)) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg4))))) goto loc_00503574;
    result = (uint32_t)(~(*(uint16_t *)(*(uint64_t *)(Arg4))));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00503B95;
    result = (uint32_t)(~((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(Arg4) + 0x8)))));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00503B95;
    v_stack_m278 = 1;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(Arg4))))) >> (1));
    goto loc_00503592;
loc_00503574:
    v_stack_m278 = 0;
    goto loc_00503592;
loc_0050357B:
    Arg1 = (Arg1) | (-1);
loc_00503589:
    Arg1 = (Arg1) + 1;
    if ((*(uint8_t *)(v_rip - 0x4E45EA + Arg1 * 1)) != 0) goto loc_00503589;
loc_00503592:
    v_stack_m27C = (uint32_t)(Arg1);
    goto loc_00503810;
loc_0050359B:
    if ((((uint32_t)(local_r15)) & (0x830ULL)) == 0) {
    }
    Arg1 = 0;
    if (0 == -1) { Arg1 = (uint32_t)((uint32_t)(0x7FFFFFFFULL)); }
    local_rdi = (local_rdi) + (8);
    v_stack_m268 = local_rdi;
    if ((((uint32_t)(local_r15)) & (0x810ULL)) == 0) goto loc_005036A6;
    result = *(uint64_t *)(Arg4);
    local_rbx = *(uint64_t *)(Arg4);
    if (*(uint64_t *)(Arg4) == 0) {
        local_rbx = v_rip - 5080808;
        result = v_rip - 5080815;
    }
    v_stack_m278 = 1;
    goto loc_0050369A;
loc_005035F4:
    if ((((uint32_t)(local_r15)) & (0x830ULL)) == 0) {
    }
    local_rdi = (local_rdi) + (8);
    v_stack_m268 = local_rdi;
    if ((((uint32_t)(local_r15)) & (0x810ULL)) == 0) goto loc_0050363E;
    result = wctomb_s(v_stack_m27C, v_stack_m248, 512, *(uint16_t *)(Arg4));
    local_r11 = 0;
    if ((uint32_t)(result) == 0) goto loc_0050364D;
    v_stack_m260 = 1;
    goto loc_0050364D;
loc_0050363E:
    v_stack_m248 = (uint8_t)(*(uint8_t *)(512));
    v_stack_m27C = 1;
loc_0050364D:
    goto loc_00503810;
loc_00503657:
    Arg2 = (uint32_t)((v_stack_m248) - (110));
    if (condition_is_equal) goto loc_0050396C;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00503706;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_005036D2;
    Arg2 = (uint32_t)((Arg2) - (3));
    if (condition_is_equal) goto loc_005035A9;
    Arg2 = (uint32_t)((Arg2) - (2));
    if (condition_is_equal) goto loc_005034EA;
    if (((uint32_t)(Arg2)) != 3) goto loc_00503810;
    goto loc_005036E2;
loc_0050368E:
    Arg1 = (uint32_t)((v_stack_m27C) - 1);
    if ((*(uint16_t *)(Arg2 + 0x24)) == 0) goto loc_0050369E;
    result = (Arg2 + 36) + (2);
loc_0050369A:
    if ((uint32_t)(Arg1) != 0) goto loc_0050368E;
loc_0050369E:
    result = (result) - (v_stack_m248);
    result = (result) >> (1);
    goto loc_005036C9;
loc_005036A6:
    result = v_rip - 5130008;
    if (v_stack_m248 != 0) { result = v_stack_m248; }
    goto loc_005036C3;
loc_005036B9:
    Arg1 = (uint32_t)((Arg1) - 1);
    if ((*(uint8_t *)(result)) == 0) goto loc_005036C7;
    result = (result) + 1;
loc_005036C3:
    if ((uint32_t)(Arg1) != 0) goto loc_005036B9;
loc_005036C7:
    result = (uint32_t)((result) - ((uint32_t)(result)));
loc_005036C9:
    v_stack_m27C = (uint32_t)(result);
    goto loc_00503810;
loc_005036D2:
loc_005036DD:
loc_005036E2:
    v_stack_m25C = 7;
    result = 7;
    local_rsi = 0;
    if (sign_flag) {
        result = (uint8_t)((7) + (81));
        v_stack_m280 = 48;
        v_stack_m27F = (uint8_t)(result);
        local_rsi = 2;
    }
    goto loc_005034F0;
loc_00503706:
    if (!sign_flag) goto loc_005034F0;
    local_r15 = (uint32_t)((local_r15) | (512));
    goto loc_005034F5;
loc_00503724:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (64));
    if ((((uint8_t)(local_r15)) & (32)) == 0) goto loc_00503740;
    if ((uint32_t)(result) == 0) goto loc_0050373A;
    goto loc_00503747;
loc_0050373A:
    goto loc_00503759;
loc_00503740:
    if ((uint32_t)(*(uint16_t *)(512)) == 0) goto loc_00503756;
loc_00503747:
    if (!sign_flag) goto loc_00503759;
    result = -((int32_t)(*(uint32_t *)(512)));
    goto loc_00503759;
loc_00503756:
loc_00503759:
    Arg3 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(512))));
    if ((((uint32_t)(local_r15)) & (0x9000ULL)) != 0) { Arg3 = (uint32_t)(*(uint32_t *)(512)); }
    if (!sign_flag) goto loc_00503774;
    goto loc_0050377F;
loc_00503774:
    local_r15 = (uint32_t)((local_r15) & (0xFFFFFFF7ULL));
    local_r13 = 1;
    if (1 > 512) { local_r13 = 512; }
loc_0050377F:
    result = -(Arg3);
    Arg1 = (uint32_t)((512) & ((uint32_t)(local_rsi)));
    v_stack_m288 = (uint32_t)(Arg1);
loc_0050379B:
    local_r13 = (uint32_t)((local_r13) - 1);
    if (condition_is_greater) goto loc_005037AA;
    if (Arg3 == 0) goto loc_005037C6;
loc_005037AA:
    Arg2 = 0;
    Arg2 = (uint32_t)((Arg2) + (48));
    if (((uint32_t)(Arg2)) >= = 57) {
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)(v_stack_m25C))));
    }
    *(uint8_t *)(v_stack_m49) = (uint8_t)(Arg2);
    Arg1 = (v_stack_m49) - 1;
    goto loc_0050379B;
loc_005037C6:
    result = (uint32_t)((v_stack_m49) - ((uint32_t)(Arg1)));
    v_stack_m27C = (uint32_t)(result);
    if (condition_is_above_or_equal) goto loc_0050380D;
    if ((uint32_t)(result) == 0) goto loc_005037F4;
    v_stack_m268 = local_rdi;
    v_stack_m288 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
    local_rbx = Arg1 + 1;
    local_rsi = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1))));
    if ((*(uint8_t *)(Arg1 + 0x1)) != 48) {
        local_rbx = (Arg1 + 1) - 1;
        v_stack_m268 = local_rdi;
        result = (uint32_t)((result) + 1);
        v_stack_m288 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
        v_stack_m27C = (uint32_t)(result);
        local_rsi = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
        *(uint8_t *)(local_rbx) = 48;
    }
    local_r11 = 0;
loc_00503810:
    if (v_stack_m260 != 0) goto loc_00503A81;
    if ((((uint8_t)(local_r15)) & (64)) == 0) goto loc_00503854;
    if (condition_is_above_or_equal) goto loc_0050382F;
    v_stack_m280 = 45;
    goto loc_0050383A;
loc_0050382F:
    if ((((uint8_t)(local_r15)) & (1)) == 0) goto loc_00503847;
    v_stack_m280 = 43;
loc_0050383A:
    v_stack_m288 = 1;
    goto loc_00503859;
loc_00503847:
    if ((((uint8_t)(local_r15)) & (2)) == 0) goto loc_00503854;
    v_stack_m280 = 32;
    goto loc_0050383A;
loc_00503854:
loc_00503859:
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m270)) - (v_stack_m27C));
    local_rsi = (uint32_t)((local_rsi) - ((uint32_t)((uint32_t)(v_stack_m288))));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (12));
    if (!(condition_is_not_equal)) {
        Arg3 = v_stack_m258;
        Arg4 = v_stack_m284;
        Arg2 = (uint32_t)(local_rsi);
        Arg1 = 32;
        result = write_multi_char(Arg1, Arg2, Arg3, Arg4);
    }
    result = write_string(v_stack_m280, (uint32_t)((uint32_t)((uint32_t)(v_stack_m288))), v_stack_m258, v_stack_m284);
    if (((uint32_t)(local_rdi)) == 8) {
        Arg4 = v_stack_m284;
        Arg3 = v_stack_m258;
        Arg2 = (uint32_t)(local_rsi);
        Arg1 = 48;
        result = write_multi_char(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m278 == 0) goto loc_00503922;
    if (condition_is_less_or_equal) goto loc_00503922;
loc_005038C8:
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m27C)) - 1);
    result = wctomb_s(v_stack_m250, v_stack_m48, 6, *(uint16_t *)(local_rbx));
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_00503917;
    if ((uint32_t)((uint32_t)(v_stack_m250)) == 0) goto loc_00503917;
    result = write_string(v_stack_m48, (uint32_t)(v_stack_m250), v_stack_m258, v_stack_m284);
    local_r11 = 0;
    if ((uint32_t)(local_rdi) != 0) goto loc_005038C8;
    goto loc_00503937;
loc_00503917:
    local_r14 = (uint32_t)((local_rbx + 2) | (0xFFFFFFFFULL));
    v_stack_m284 = (uint32_t)(local_r14);
    goto loc_0050393C;
loc_00503922:
    result = write_string(local_rbx, (uint32_t)((uint32_t)(local_rdi)), local_r14, v_stack_m284);
    local_r11 = 0;
loc_00503937:
loc_0050393C:
    if (sign_flag) goto loc_00503963;
    if ((((uint8_t)(local_r15)) & (4)) == 0) goto loc_00503963;
    result = write_multi_char(32, (uint32_t)((uint32_t)(local_rsi)), v_stack_m258, v_stack_m284);
    goto loc_00503A79;
loc_00503963:
    goto loc_00503A81;
loc_0050396C:
    local_rdi = (local_rdi) + (8);
    v_stack_m268 = local_rdi;
    result = get_printf_count_output(32, (uint32_t)((uint32_t)(local_rsi)), v_stack_m258, v_stack_m284);
    local_r11 = 0;
    if ((uint32_t)(result) == 0) goto loc_00503B95;
    if ((((uint8_t)(local_r15)) & (32)) == 0) goto loc_00503994;
    *(uint16_t *)(*(uint64_t *)(v_stack_m258)) = (uint16_t)((uint32_t)(v_stack_m284));
    goto loc_00503997;
loc_00503994:
    *(uint32_t *)(*(uint64_t *)(v_stack_m258)) = (uint32_t)((uint32_t)(v_stack_m284));
loc_00503997:
    v_stack_m260 = 1;
    goto loc_00503A81;
loc_005039A4:
    if (((uint8_t)(v_stack_m284)) == 73) goto loc_005039D3;
    if (((uint8_t)(v_stack_m284)) == 104) goto loc_00503A20;
    if (((uint8_t)(v_stack_m284)) == 106) goto loc_005039D3;
    if (((uint8_t)(v_stack_m284)) == 108) goto loc_00503A01;
    if (((uint8_t)(v_stack_m284)) == 116) goto loc_005039D3;
    if (((uint8_t)(v_stack_m284)) == 119) goto loc_005039F7;
    if (((uint8_t)(v_stack_m284)) != 122) goto loc_00503A86;
loc_005039D3:
    if (((uint8_t)(v_stack_m284)) != 73) goto loc_00503A3D;
    if (((uint8_t)(*(uint8_t *)(local_r12))) != 54) goto loc_00503A26;
    if ((*(uint8_t *)(local_r12 + 0x1)) != 52) goto loc_00503A43;
    local_r12 = (local_r12) + (2);
    goto loc_00503A86;
loc_005039F7:
    goto loc_00503A86;
loc_00503A01:
    if (((uint8_t)(*(uint8_t *)(local_r12))) == 108) {
        local_r12 = (local_r12) + 1;
    }
    result = (uint32_t)(0x1000ULL);
    if (((uint8_t)(*(uint8_t *)(local_r12))) != 108) { result = 16; }
    local_r15 = (uint32_t)((local_r15) | ((uint32_t)(result)));
    goto loc_00503A86;
loc_00503A20:
    local_r15 = (uint32_t)((local_r15) | (32));
    goto loc_00503A86;
loc_00503A26:
    if (((uint8_t)(result)) != 51) goto loc_00503A43;
    if ((*(uint8_t *)(local_r12 + 0x1)) != 50) goto loc_00503A43;
    local_r12 = (local_r12) + (2);
    goto loc_00503A86;
loc_00503A3D:
    if (((uint8_t)(v_stack_m284)) == 106) goto loc_00503A86;
loc_00503A43:
    result = (uint8_t)((*(uint8_t *)(local_r12)) - (88));
    if (((uint8_t)(result)) > 32) goto loc_00503A5D;
    if (((uint8_t)(result)) < 32) goto loc_00503A86;
loc_00503A5D:
    v_stack_m274 = 0;
loc_00503A62:
    v_stack_m278 = 0;
    result = write_char((uint8_t)(v_stack_m284), v_stack_m258, v_stack_m284, v_stack_m284);
loc_00503A79:
    local_r11 = 0;
loc_00503A81:
loc_00503A86:
    if ((uint8_t)(*(uint8_t *)(local_r12)) != 0) goto loc_00503417;
loc_00503A9F:
    goto loc_00503BAC;
loc_00503AA7:
    if (((uint8_t)(*(uint8_t *)(local_r12))) != 42) goto loc_00503AC4;
    local_rdi = (v_stack_m268) + (8);
    v_stack_m268 = local_rdi;
    if (!sign_flag) goto loc_00503A86;
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m284))) | (0xFFFFFFFFULL));
    goto loc_00503A86;
loc_00503AC4:
    goto loc_00503A86;
loc_00503AD3:
    goto loc_00503A86;
loc_00503AD8:
    if (((uint8_t)(*(uint8_t *)(local_r12))) != 42) goto loc_00503B0C;
    local_rdi = (local_rdi) + (8);
    v_stack_m268 = local_rdi;
    if (sign_flag) {
        local_r15 = (uint32_t)((local_r15) | (4));
    }
    Arg3 = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_stack_m284))));
    if (!sign_flag) { Arg3 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m284))))); }
    v_stack_m270 = (uint32_t)(Arg3);
    goto loc_00503A86;
loc_00503B0C:
    v_stack_m270 = (uint32_t)(v_stack_m258 + (uint32_t)(v_stack_m270) + (uint32_t)(v_stack_m270) * 4 - 24 * 2);
    goto loc_00503A86;
loc_00503B22:
    if (((uint8_t)(*(uint8_t *)(local_r12))) == 32) goto loc_00503B69;
    if (((uint8_t)(*(uint8_t *)(local_r12))) == 35) goto loc_00503B5F;
    if (((uint8_t)(*(uint8_t *)(local_r12))) == 43) goto loc_00503B56;
    if (((uint8_t)(*(uint8_t *)(local_r12))) == 45) goto loc_00503B4D;
    if (((uint8_t)(*(uint8_t *)(local_r12))) != 48) goto loc_00503A86;
    local_r15 = (uint32_t)((local_r15) | (8));
    goto loc_00503A86;
loc_00503B4D:
    local_r15 = (uint32_t)((local_r15) | (4));
    goto loc_00503A86;
loc_00503B56:
    local_r15 = (uint32_t)((local_r15) | (1));
    goto loc_00503A86;
loc_00503B5F:
    goto loc_00503A86;
loc_00503B69:
    local_r15 = (uint32_t)((local_r15) | (2));
    goto loc_00503A86;
loc_00503B72:
    v_stack_m260 = 0;
    v_stack_m270 = 0;
    v_stack_m288 = 0;
    local_r13 = (uint32_t)((0) | (0xFFFFFFFFULL));
    v_stack_m278 = 0;
    goto loc_00503A86;
loc_00503B95:
    Arg4 = 0;
    v_stack_m298 = 0;
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = EmpCheckErrataList(Arg1, Arg2, Arg3, Arg4);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
loc_00503BAC:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (640);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00503368&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
