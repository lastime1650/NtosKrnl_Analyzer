# MiCoalesceFreeSmallPages

- RVA: `0x00336340`–`0x00336C2F` (길이 `2,287` bytes)
- VA: `0x0000000140336340`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00076990`
- 디코드: `551`개 명령, `2,287/2,287` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x0033658B` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003365C0` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00336616` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0033663A` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00336793` → [MiUnlinkFreeOrZeroedPage](MiUnlinkFreeOrZeroedPage_function_00336C40.md) (function, `0x00336C40`)
- `0x003367DC` → [MiSetOriginalPtePfnFromFreeList](../28/MiSetOriginalPtePfnFromFreeList_function_0028A99C.md) (function, `0x0028A99C`)
- `0x00336824` → [MiMakeDemandZeroPte](MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x003368A9` → [MiColdPageSizeSupported](../45/MiColdPageSizeSupported_function_00454588.md) (function, `0x00454588`)
- `0x0033690E` → [MiInitializeAllResidentPageBasePfns](../46/MiInitializeAllResidentPageBasePfns_function_00462AF8.md) (function, `0x00462AF8`)
- `0x00336932` → [MiCreateInitialLargeLeafPfns](../44/MiCreateInitialLargeLeafPfns_function_004428E0.md) (function, `0x004428E0`)
- `0x00336974` → [MiInsertPageInFreeOrZeroedList](MiInsertPageInFreeOrZeroedList_function_00334D20.md) (function, `0x00334D20`)
- `0x00336A2A` → [MiReturnFreeZeroPage](MiReturnFreeZeroPage_function_00334BD0.md) (function, `0x00334BD0`)
- `0x00336AE4` → [MiChangePageAttribute](MiChangePageAttribute_function_00332ECC.md) (function, `0x00332ECC`)
- `0x00336B29` → [MiPfnZeroingNeeded](../29/MiPfnZeroingNeeded_function_0029FA80.md) (function, `0x0029FA80`)
- `0x00336BAF` → [MiSearchChannelTable](MiSearchChannelTable_function_0033BE24.md) (function, `0x0033BE24`)
- `0x00336BFF` → [MiChangePageHeatImmediate](../44/MiChangePageHeatImmediate_function_00445F5C.md) (function, `0x00445F5C`)

### Direct callers
- [sub_00334D90](Unknown_function_00334D90.md) at `0x00335189`
- [MiProcessLargeCoalesceBitmapCandidates](../37/MiProcessLargeCoalesceBitmapCandidates_function_0037A3F0.md) at `0x0037A4FC`

### Static image references
- `0x00336357` → RVA `0x00E0A740` (`.data`; read)
- `0x0033636F` → RVA `0x00FC6B88` (`ALMOSTRO`; read)
- `0x003363A2` → RVA `0x00E3CBE6` (`.data`; read)
- `0x003363AF` → RVA `0x00E3CCF8` (`.data`; read)
- `0x003363ED` → RVA `0x00E30088` (`.data`; read)
- `0x0033641E` → RVA `0x00E2DBC0` (`.data`; read)
- `0x00336425` → RVA `0x00E2DBC4` (`.data`; read)
- `0x00336447` → RVA `0x00E2DC20` (`.data`; read)
- `0x00336490` → RVA `0x00E2DBC0` (`.data`; write)
- `0x00336520` → RVA `0x00E2DC28` (`.data`; read)
- `0x00336640` → RVA `0x00010880` (`.rdata`; read)
- `0x003366A1` → RVA `0x00E2DCE0` (`.data`; read)
- `0x00336860` → RVA `0x00E2DC80` (`.data`; read)
- `0x003368BB` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00336C15` → [sub_006E1F9E](../6E/Unknown_function_006E1F9E.md) (`tail-transfer`)
  - `0x00336C2A` → [sub_006E1F9E](../6E/Unknown_function_006E1F9E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00336340  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00336345  55                              push rbp
00336346  56                              push rsi
00336347  57                              push rdi
00336348  41 54                           push r12
0033634A  41 55                           push r13
0033634C  41 56                           push r14
0033634E  41 57                           push r15
00336350  48 81 EC A0 00 00 00            sub rsp, 0xa0
00336357  48 8B 05 E2 43 AD 00            mov rax, qword ptr [rip + 0xad43e2]
0033635E  48 33 C4                        xor rax, rsp
00336361  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00336369  45 33 F6                        xor r14d, r14d
0033636C  48 8B F9                        mov rdi, rcx
0033636F  4C 39 35 12 08 C9 00            cmp qword ptr [rip + 0xc90812], r14
00336376  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
0033637B  0F 84 FD 01 00 00               je 0x14033657e
00336381  48 8D 34 49                     lea rsi, [rcx + rcx*2]
00336385  49 BA 00 00 00 00 00 DE FF FF   movabs r10, 0xffffde0000000000
0033638F  48 C1 E6 04                     shl rsi, 4
00336393  49 8B C2                        mov rax, r10
00336396  48 03 F0                        add rsi, rax
00336399  F6 C2 01                        test dl, 1
0033639C  0F 84 4F 02 00 00               je 0x1403365f1
003363A2  80 3D 3D 68 B0 00 02            cmp byte ptr [rip + 0xb0683d], 2
003363A9  0F 82 CF 01 00 00               jb 0x14033657e
003363AF  48 8B 05 42 69 B0 00            mov rax, qword ptr [rip + 0xb06942]
003363B6  48 C1 E9 04                     shr rcx, 4
003363BA  0F B6 0C 48                     movzx ecx, byte ptr [rax + rcx*2]
003363BE  80 E1 1F                        and cl, 0x1f
003363C1  80 F9 0F                        cmp cl, 0xf
003363C4  0F 82 B4 01 00 00               jb 0x14033657e
003363CA  4C 8B EE                        mov r13, rsi
003363CD  48 83 E7 F0                     and rdi, 0xfffffffffffffff0
003363D1  44 8B 46 20                     mov r8d, dword ptr [rsi + 0x20]
003363D5  4C 8D 24 7F                     lea r12, [rdi + rdi*2]
003363D9  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
003363DD  B9 FF 03 00 00                  mov ecx, 0x3ff
003363E2  48 C1 E8 2B                     shr rax, 0x2b
003363E6  48 23 C1                        and rax, rcx
003363E9  41 C1 E8 10                     shr r8d, 0x10
003363ED  48 8B 0D 94 9C AF 00            mov rcx, qword ptr [rip + 0xaf9c94]
003363F4  41 83 E0 07                     and r8d, 7
003363F8  44 89 44 24 48                  mov dword ptr [rsp + 0x48], r8d
003363FD  49 C1 E4 04                     shl r12, 4
00336401  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00336405  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0033640D  44 0F B7 08                     movzx r9d, word ptr [rax]
00336411  66 44 89 4C 24 44               mov word ptr [rsp + 0x44], r9w
00336417  49 8B C2                        mov rax, r10
0033641A  4D 8D 04 04                     lea r8, [r12 + rax]
0033641E  48 63 05 9B 77 AF 00            movsxd rax, dword ptr [rip + 0xaf779b]
00336425  8B 0D 99 77 AF 00               mov ecx, dword ptr [rip + 0xaf7799]
0033642B  4D 8D 98 00 03 00 00            lea r11, [r8 + 0x300]
00336432  4C 89 5C 24 68                  mov qword ptr [rsp + 0x68], r11
00336437  4C 89 44 24 50                  mov qword ptr [rsp + 0x50], r8
0033643C  3B C1                           cmp eax, ecx
0033643E  77 1D                           ja 0x14033645d
00336440  48 8B D8                        mov rbx, rax
00336443  48 C1 E3 04                     shl rbx, 4
00336447  48 03 1D D2 77 AF 00            add rbx, qword ptr [rip + 0xaf77d2]
0033644E  48 3B 3B                        cmp rdi, qword ptr [rbx]
00336451  72 0A                           jb 0x14033645d
00336453  3B C1                           cmp eax, ecx
00336455  74 3F                           je 0x140336496
00336457  48 3B 7B 10                     cmp rdi, qword ptr [rbx + 0x10]
0033645B  72 39                           jb 0x140336496
0033645D  41 8B C6                        mov eax, r14d
00336460  3B C8                           cmp ecx, eax
00336462  0F 8C 44 01 00 00               jl 0x1403365ac
00336468  8D 14 08                        lea edx, [rax + rcx]
0033646B  D1 FA                           sar edx, 1
0033646D  48 63 DA                        movsxd rbx, edx
00336470  48 C1 E3 04                     shl rbx, 4
00336474  48 03 1D A5 77 AF 00            add rbx, qword ptr [rip + 0xaf77a5]
0033647B  48 3B 3B                        cmp rdi, qword ptr [rbx]
0033647E  0F 82 75 01 00 00               jb 0x1403365f9
00336484  3B 15 3A 77 AF 00               cmp edx, dword ptr [rip + 0xaf773a]
0033648A  0F 85 4F 01 00 00               jne 0x1403365df
00336490  89 15 2A 77 AF 00               mov dword ptr [rip + 0xaf772a], edx
00336496  48 63 0D 23 77 AF 00            movsxd rcx, dword ptr [rip + 0xaf7723]
0033649D  41 BF 10 00 00 00               mov r15d, 0x10
003364A3  8B 15 1B 77 AF 00               mov edx, dword ptr [rip + 0xaf771b]
003364A9  8B 5B 08                        mov ebx, dword ptr [rbx + 8]
003364AC  3B CA                           cmp ecx, edx
003364AE  77 1D                           ja 0x1403364cd
003364B0  48 8B C1                        mov rax, rcx
003364B3  48 C1 E0 04                     shl rax, 4
003364B7  48 03 05 62 77 AF 00            add rax, qword ptr [rip + 0xaf7762]
003364BE  48 3B 38                        cmp rdi, qword ptr [rax]
003364C1  72 0A                           jb 0x1403364cd
003364C3  3B CA                           cmp ecx, edx
003364C5  74 48                           je 0x14033650f
003364C7  48 3B 78 10                     cmp rdi, qword ptr [rax + 0x10]
003364CB  72 42                           jb 0x14033650f
003364CD  41 8B CE                        mov ecx, r14d
003364D0  3B D1                           cmp edx, ecx
003364D2  0F 8C D4 00 00 00               jl 0x1403365ac
003364D8  44 8D 04 11                     lea r8d, [rcx + rdx]
003364DC  41 D1 F8                        sar r8d, 1
003364DF  49 63 C0                        movsxd rax, r8d
003364E2  48 C1 E0 04                     shl rax, 4
003364E6  48 03 05 33 77 AF 00            add rax, qword ptr [rip + 0xaf7733]
003364ED  48 3B 38                        cmp rdi, qword ptr [rax]
003364F0  0F 82 26 01 00 00               jb 0x14033661c
003364F6  44 3B 05 C7 76 AF 00            cmp r8d, dword ptr [rip + 0xaf76c7]
003364FD  0F 85 C9 00 00 00               jne 0x1403365cc
00336503  44 89 05 B6 76 AF 00            mov dword ptr [rip + 0xaf76b6], r8d
0033650A  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
0033650F  48 8B 48 10                     mov rcx, qword ptr [rax + 0x10]
00336513  48 8D 47 10                     lea rax, [rdi + 0x10]
00336517  48 3B C1                        cmp rax, rcx
0033651A  0F 87 81 06 00 00               ja 0x140336ba1
00336520  4C 39 35 01 77 AF 00            cmp qword ptr [rip + 0xaf7701], r14
00336527  49 8B EF                        mov rbp, r15
0033652A  0F 85 7C 06 00 00               jne 0x140336bac
00336530  49 83 FF 10                     cmp r15, 0x10
00336534  75 48                           jne 0x14033657e
00336536  41 8B 40 20                     mov eax, dword ptr [r8 + 0x20]
0033653A  49 8D 48 20                     lea rcx, [r8 + 0x20]
0033653E  C1 E8 10                        shr eax, 0x10
00336541  BA FF 03 00 00                  mov edx, 0x3ff
00336546  0F B6 E8                        movzx ebp, al
00336549  C1 ED 06                        shr ebp, 6
0033654C  48 8D 41 E0                     lea rax, [rcx - 0x20]
00336550  49 3B C3                        cmp rax, r11
00336553  0F 84 E7 00 00 00               je 0x140336640
00336559  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0033655D  48 C1 E8 2B                     shr rax, 0x2b
00336561  66 23 C2                        and ax, dx
00336564  66 41 3B C1                     cmp ax, r9w
00336568  75 14                           jne 0x14033657e
0033656A  4D 85 ED                        test r13, r13
0033656D  74 57                           je 0x1403365c6
0033656F  8B 01                           mov eax, dword ptr [rcx]
00336571  C1 E8 10                        shr eax, 0x10
00336574  0F B6 C0                        movzx eax, al
00336577  C1 E8 06                        shr eax, 6
0033657A  3B C5                           cmp eax, ebp
0033657C  74 48                           je 0x1403365c6
0033657E  33 C0                           xor eax, eax
00336580  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00336588  48 33 CC                        xor rcx, rsp
0033658B  E8 B0 60 37 00                  call 0x1406ac640
00336590  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
00336598  48 81 C4 A0 00 00 00            add rsp, 0xa0
0033659F  41 5F                           pop r15
003365A1  41 5E                           pop r14
003365A3  41 5D                           pop r13
003365A5  41 5C                           pop r12
003365A7  5F                              pop rdi
003365A8  5E                              pop rsi
003365A9  5D                              pop rbp
003365AA  C3                              ret
003365AB  CC                              int3
003365AC  45 33 C9                        xor r9d, r9d
003365AF  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
003365B4  4C 8B C7                        mov r8, rdi
003365B7  BA 80 51 00 00                  mov edx, 0x5180
003365BC  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
003365C0  E8 9B 70 1C 00                  call 0x1404fd660
003365C5  CC                              int3
003365C6  48 83 C1 30                     add rcx, 0x30
003365CA  EB 80                           jmp 0x14033654c
003365CC  48 3B 78 10                     cmp rdi, qword ptr [rax + 0x10]
003365D0  0F 82 2D FF FF FF               jb 0x140336503
003365D6  41 8D 48 01                     lea ecx, [r8 + 1]
003365DA  E9 F1 FE FF FF                  jmp 0x1403364d0
003365DF  48 3B 7B 10                     cmp rdi, qword ptr [rbx + 0x10]
003365E3  0F 82 A7 FE FF FF               jb 0x140336490
003365E9  8D 42 01                        lea eax, [rdx + 1]
003365EC  E9 6F FE FF FF                  jmp 0x140336460
003365F1  4D 8B EE                        mov r13, r14
003365F4  E9 D8 FD FF FF                  jmp 0x1403363d1
003365F9  85 D2                           test edx, edx
003365FB  0F 85 8F 05 00 00               jne 0x140336b90
00336601  4C 8B CB                        mov r9, rbx
00336604  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00336609  4C 8B C7                        mov r8, rdi
0033660C  BA 80 51 00 00                  mov edx, 0x5180
00336611  B9 1A 00 00 00                  mov ecx, 0x1a
00336616  E8 45 70 1C 00                  call 0x1404fd660
0033661B  CC                              int3
0033661C  45 85 C0                        test r8d, r8d
0033661F  0F 85 73 05 00 00               jne 0x140336b98
00336625  4C 8B C8                        mov r9, rax
00336628  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0033662D  4C 8B C7                        mov r8, rdi
00336630  BA 80 51 00 00                  mov edx, 0x5180
00336635  B9 1A 00 00 00                  mov ecx, 0x1a
0033663A  E8 21 70 1C 00                  call 0x1404fd660
0033663F  CC                              int3
00336640  48 8B 05 39 A2 CD FF            mov rax, qword ptr [rip - 0x325dc7]
00336647  4C 8B FF                        mov r15, rdi
0033664A  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0033664F  4D 85 ED                        test r13, r13
00336652  0F 84 53 04 00 00               je 0x140336aab
00336658  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00336660  41 8B D6                        mov edx, r14d
00336663  4C 69 D3 80 DF 00 00            imul r10, rbx, 0xdf80
0033666A  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
0033666E  49 8B D8                        mov rbx, r8
00336671  4C 03 50 10                     add r10, qword ptr [rax + 0x10]
00336675  4C 89 54 24 58                  mov qword ptr [rsp + 0x58], r10
0033667A  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00336684  4C 03 E0                        add r12, rax
00336687  49 3B DB                        cmp rbx, r11
0033668A  0F 84 65 01 00 00               je 0x1403367f5
00336690  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00336693  8B C8                           mov ecx, eax
00336695  C1 E9 10                        shr ecx, 0x10
00336698  49 3B DD                        cmp rbx, r13
0033669B  0F 84 2C 01 00 00               je 0x1403367cd
003366A1  4C 3B 3D 38 76 AF 00            cmp r15, qword ptr [rip + 0xaf7638]
003366A8  0F 87 2C 03 00 00               ja 0x1403369da
003366AE  49 8B 04 24                     mov rax, qword ptr [r12]
003366B2  48 C1 E8 36                     shr rax, 0x36
003366B6  0F BA E0 00                     bt eax, 0
003366BA  0F 83 1A 03 00 00               jae 0x1403369da
003366C0  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
003366C4  41 B8 FF 03 00 00               mov r8d, 0x3ff
003366CA  48 C1 E8 2B                     shr rax, 0x2b
003366CE  66 41 23 C0                     and ax, r8w
003366D2  66 41 3B C1                     cmp ax, r9w
003366D6  0F 85 FE 02 00 00               jne 0x1403369da
003366DC  80 E1 07                        and cl, 7
003366DF  80 F9 01                        cmp cl, 1
003366E2  0F 87 F2 02 00 00               ja 0x1403369da
003366E8  48 3B DE                        cmp rbx, rsi
003366EB  74 0D                           je 0x1403366fa
003366ED  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
003366F4  0F 82 D5 02 00 00               jb 0x1403369cf
003366FA  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
003366FD  C1 E8 10                        shr eax, 0x10
00336700  24 07                           and al, 7
00336702  3C 01                           cmp al, 1
00336704  0F 87 EE 03 00 00               ja 0x140336af8
0033670A  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0033670E  48 C1 E8 2B                     shr rax, 0x2b
00336712  66 41 23 C0                     and ax, r8w
00336716  66 41 3B C1                     cmp ax, r9w
0033671A  0F 85 D8 03 00 00               jne 0x140336af8
00336720  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00336723  C1 E8 18                        shr eax, 0x18
00336726  A8 40                           test al, 0x40
00336728  0F 85 CA 03 00 00               jne 0x140336af8
0033672E  4D 85 ED                        test r13, r13
00336731  74 14                           je 0x140336747
00336733  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00336736  C1 E8 10                        shr eax, 0x10
00336739  0F B6 C0                        movzx eax, al
0033673C  C1 E8 06                        shr eax, 6
0033673F  3B C5                           cmp eax, ebp
00336741  0F 85 B1 03 00 00               jne 0x140336af8
00336747  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0033674B  48 0F BA E0 28                  bt rax, 0x28
00336750  0F 82 A2 03 00 00               jb 0x140336af8
00336756  85 D2                           test edx, edx
00336758  75 2E                           jne 0x140336788
0033675A  49 8B 82 58 3B 00 00            mov rax, qword ptr [r10 + 0x3b58]
00336761  48 8D 50 01                     lea rdx, [rax + 1]
00336765  48 8B C8                        mov rcx, rax
00336768  48 33 CA                        xor rcx, rdx
0033676B  48 81 E1 00 00 FF FF            and rcx, 0xffffffffffff0000
00336772  48 33 CA                        xor rcx, rdx
00336775  F0 49 0F B1 8A 58 3B 00 00      lock cmpxchg qword ptr [r10 + 0x3b58], rcx
0033677E  75 E1                           jne 0x140336761
00336780  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
00336788  33 D2                           xor edx, edx
0033678A  41 B8 00 01 00 00               mov r8d, 0x100
00336790  49 8B CF                        mov rcx, r15
00336793  E8 A8 04 00 00                  call 0x140336c40
00336798  85 C0                           test eax, eax
0033679A  0F 84 58 03 00 00               je 0x140336af8
003367A0  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
003367A5  44 0F B7 4C 24 44               movzx r9d, word ptr [rsp + 0x44]
003367AB  4C 8B 5C 24 68                  mov r11, qword ptr [rsp + 0x68]
003367B0  4D 85 ED                        test r13, r13
003367B3  0F 84 D9 02 00 00               je 0x140336a92
003367B9  8B 54 24 40                     mov edx, dword ptr [rsp + 0x40]
003367BD  48 83 C3 30                     add rbx, 0x30
003367C1  49 FF C7                        inc r15
003367C4  49 83 C4 30                     add r12, 0x30
003367C8  E9 BA FE FF FF                  jmp 0x140336687
003367CD  C1 E8 10                        shr eax, 0x10
003367D0  A8 07                           test al, 7
003367D2  0F 84 22 02 00 00               je 0x1403369fa
003367D8  48 8D 4B 10                     lea rcx, [rbx + 0x10]
003367DC  E8 BB 41 F5 FF                  call 0x14028a99c
003367E1  8B 54 24 40                     mov edx, dword ptr [rsp + 0x40]
003367E5  48 83 C3 30                     add rbx, 0x30
003367E9  49 FF C7                        inc r15
003367EC  49 83 C4 30                     add r12, 0x30
003367F0  E9 92 FE FF FF                  jmp 0x140336687
003367F5  41 B9 02 00 00 00               mov r9d, 2
003367FB  45 8D 79 FF                     lea r15d, [r9 - 1]
003367FF  4D 85 ED                        test r13, r13
00336802  0F 84 3E 03 00 00               je 0x140336b46
00336808  83 7C 24 48 01                  cmp dword ptr [rsp + 0x48], 1
0033680D  0F 85 02 03 00 00               jne 0x140336b15
00336813  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00336818  48 85 C0                        test rax, rax
0033681B  0F 85 9A 02 00 00               jne 0x140336abb
00336821  8D 48 04                        lea ecx, [rax + 4]
00336824  E8 D7 11 00 00                  call 0x140337a00
00336829  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0033682E  45 8B C6                        mov r8d, r14d
00336831  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
00336836  49 8D 5B D0                     lea rbx, [r11 - 0x30]
0033683A  45 8B FE                        mov r15d, r14d
0033683D  BA FD FF FF FF                  mov edx, 0xfffffffd
00336842  41 BC 01 00 00 00               mov r12d, 1
00336848  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00336850  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00336853  4D 85 ED                        test r13, r13
00336856  0F 84 6F 02 00 00               je 0x140336acb
0033685C  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00336860  48 8B 0D 19 74 AF 00            mov rcx, qword ptr [rip + 0xaf7419]
00336867  48 85 C9                        test rcx, rcx
0033686A  74 0A                           je 0x140336876
0033686C  A8 10                           test al, 0x10
0033686E  75 68                           jne 0x1403368d8
00336870  48 F7 D1                        not rcx
00336873  48 23 C1                        and rax, rcx
00336876  48 C1 E8 20                     shr rax, 0x20
0033687A  48 3B C2                        cmp rax, rdx
0033687D  75 53                           jne 0x1403368d2
0033687F  45 0B C4                        or r8d, r12d
00336882  4C 89 73 10                     mov qword ptr [rbx + 0x10], r14
00336886  41 FF C7                        inc r15d
00336889  48 83 EB 30                     sub rbx, 0x30
0033688D  44 89 44 24 40                  mov dword ptr [rsp + 0x40], r8d
00336892  41 83 FF 10                     cmp r15d, 0x10
00336896  72 B8                           jb 0x140336850
00336898  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
0033689D  41 B9 02 00 00 00               mov r9d, 2
003368A3  49 8B D2                        mov rdx, r10
003368A6  41 8B C9                        mov ecx, r9d
003368A9  E8 DA DC 11 00                  call 0x140454588
003368AE  44 8B 64 24 48                  mov r12d, dword ptr [rsp + 0x48]
003368B3  85 C0                           test eax, eax
003368B5  0F 85 23 03 00 00               jne 0x140336bde
003368BB  F7 05 F3 01 C9 00 00 00 20 00   test dword ptr [rip + 0xc901f3], 0x200000
003368C5  0F 85 47 03 00 00               jne 0x140336c12
003368CB  B8 01 00 00 00                  mov eax, 1
003368D0  EB 18                           jmp 0x1403368ea
003368D2  41 83 C8 02                     or r8d, 2
003368D6  EB AA                           jmp 0x140336882
003368D8  48 83 E0 EF                     and rax, 0xffffffffffffffef
003368DC  EB 98                           jmp 0x140336876
003368DE  41 8B C6                        mov eax, r14d
003368E1  44 84 C1                        test cl, r8b
003368E4  0F 85 0C 03 00 00               jne 0x140336bf6
003368EA  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
003368F2  41 B8 10 00 00 00               mov r8d, 0x10
003368F8  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
00336900  48 8B CB                        mov rcx, rbx
00336903  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00336907  48 8B D7                        mov rdx, rdi
0033690A  89 6C 24 20                     mov dword ptr [rsp + 0x20], ebp
0033690E  E8 E5 C1 12 00                  call 0x140462af8
00336913  0F B7 03                        movzx eax, word ptr [rbx]
00336916  BA 10 00 00 00                  mov edx, 0x10
0033691B  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
00336923  44 8B CD                        mov r9d, ebp
00336926  48 8B CF                        mov rcx, rdi
00336929  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
0033692E  44 8D 42 F2                     lea r8d, [rdx - 0xe]
00336932  E8 A9 BF 10 00                  call 0x1404428e0
00336937  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
0033693C  BB 01 00 00 00                  mov ebx, 1
00336941  8B CB                           mov ecx, ebx
00336943  48 BD FF FF FF FF FF FF FF 7F   movabs rbp, 0x7fffffffffffffff
0033694D  49 8D 47 30                     lea rax, [r15 + 0x30]
00336951  48 3B C6                        cmp rax, rsi
00336954  74 05                           je 0x14033695b
00336956  F0 48 21 68 18                  lock and qword ptr [rax + 0x18], rbp
0033695B  FF C1                           inc ecx
0033695D  48 83 C0 30                     add rax, 0x30
00336961  83 F9 10                        cmp ecx, 0x10
00336964  72 EB                           jb 0x140336951
00336966  45 85 E4                        test r12d, r12d
00336969  48 8B CF                        mov rcx, rdi
0033696C  41 0F 95 C6                     setne r14b
00336970  41 8D 56 01                     lea edx, [r14 + 1]
00336974  E8 A7 E3 FF FF                  call 0x140334d20
00336979  4C 3B FE                        cmp r15, rsi
0033697C  74 05                           je 0x140336983
0033697E  F0 49 21 6F 18                  lock and qword ptr [r15 + 0x18], rbp
00336983  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00336988  49 8B 80 58 3B 00 00            mov rax, qword ptr [r8 + 0x3b58]
0033698F  90                              nop
00336990  48 8D 50 FF                     lea rdx, [rax - 1]
00336994  48 8B CA                        mov rcx, rdx
00336997  48 33 C8                        xor rcx, rax
0033699A  48 81 E1 00 00 FF FF            and rcx, 0xffffffffffff0000
003369A1  48 33 CA                        xor rcx, rdx
003369A4  66 85 C9                        test cx, cx
003369A7  75 14                           jne 0x1403369bd
003369A9  48 8D 91 00 00 01 00            lea rdx, [rcx + 0x10000]
003369B0  48 33 D1                        xor rdx, rcx
003369B3  48 81 E2 00 00 FF FF            and rdx, 0xffffffffffff0000
003369BA  48 33 CA                        xor rcx, rdx
003369BD  F0 49 0F B1 88 58 3B 00 00      lock cmpxchg qword ptr [r8 + 0x3b58], rcx
003369C6  75 C8                           jne 0x140336990
003369C8  8B C3                           mov eax, ebx
003369CA  E9 B1 FB FF FF                  jmp 0x140336580
003369CF  41 BE 02 00 00 00               mov r14d, 2
003369D5  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
003369DA  48 BD FF FF FF FF FF FF FF 7F   movabs rbp, 0x7fffffffffffffff
003369E4  48 39 5C 24 50                  cmp qword ptr [rsp + 0x50], rbx
003369E9  72 2D                           jb 0x140336a18
003369EB  83 7C 24 40 00                  cmp dword ptr [rsp + 0x40], 0
003369F0  75 57                           jne 0x140336a49
003369F2  41 8B C6                        mov eax, r14d
003369F5  E9 86 FB FF FF                  jmp 0x140336580
003369FA  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
003369FE  49 FF C7                        inc r15
00336A01  48 25 1F FC FF FF               and rax, 0xfffffffffffffc1f
00336A07  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00336A0B  48 83 C3 30                     add rbx, 0x30
00336A0F  49 83 C4 30                     add r12, 0x30
00336A13  E9 6F FC FF FF                  jmp 0x140336687
00336A18  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00336A1D  4D 3B F5                        cmp r14, r13
00336A20  74 0D                           je 0x140336a2f
00336A22  BA 00 02 00 00                  mov edx, 0x200
00336A27  49 8B CE                        mov rcx, r14
00336A2A  E8 A1 E1 FF FF                  call 0x140334bd0
00336A2F  4C 3B F6                        cmp r14, rsi
00336A32  74 05                           je 0x140336a39
00336A34  F0 49 21 6E 18                  lock and qword ptr [r14 + 0x18], rbp
00336A39  49 83 C6 30                     add r14, 0x30
00336A3D  4C 3B F3                        cmp r14, rbx
00336A40  72 DB                           jb 0x140336a1d
00336A42  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
00336A47  EB A2                           jmp 0x1403369eb
00336A49  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00336A4E  49 8B 80 58 3B 00 00            mov rax, qword ptr [r8 + 0x3b58]
00336A55  48 8D 50 FF                     lea rdx, [rax - 1]
00336A59  48 8B CA                        mov rcx, rdx
00336A5C  48 33 C8                        xor rcx, rax
00336A5F  48 81 E1 00 00 FF FF            and rcx, 0xffffffffffff0000
00336A66  48 33 CA                        xor rcx, rdx
00336A69  66 85 C9                        test cx, cx
00336A6C  75 14                           jne 0x140336a82
00336A6E  48 8D 91 00 00 01 00            lea rdx, [rcx + 0x10000]
00336A75  48 33 D1                        xor rdx, rcx
00336A78  48 81 E2 00 00 FF FF            and rdx, 0xffffffffffff0000
00336A7F  48 33 CA                        xor rcx, rdx
00336A82  F0 49 0F B1 88 58 3B 00 00      lock cmpxchg qword ptr [r8 + 0x3b58], rcx
00336A8B  75 C8                           jne 0x140336a55
00336A8D  E9 60 FF FF FF                  jmp 0x1403369f2
00336A92  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00336A95  C1 E8 10                        shr eax, 0x10
00336A98  0F B6 C0                        movzx eax, al
00336A9B  48 C1 E8 06                     shr rax, 6
00336A9F  FF 84 84 88 00 00 00            inc dword ptr [rsp + rax*4 + 0x88]
00336AA6  E9 0E FD FF FF                  jmp 0x1403367b9
00336AAB  0F 57 C0                        xorps xmm0, xmm0
00336AAE  0F 11 84 24 88 00 00 00         movups xmmword ptr [rsp + 0x88], xmm0
00336AB6  E9 9D FB FF FF                  jmp 0x140336658
00336ABB  48 25 9F FC FF FF               and rax, 0xfffffffffffffc9f
00336AC1  48 0F BA E8 07                  bts rax, 7
00336AC6  E9 5E FD FF FF                  jmp 0x140336829
00336ACB  C1 E8 10                        shr eax, 0x10
00336ACE  0F B6 C0                        movzx eax, al
00336AD1  C1 E8 06                        shr eax, 6
00336AD4  3B C5                           cmp eax, ebp
00336AD6  0F 84 80 FD FF FF               je 0x14033685c
00336ADC  45 8B C4                        mov r8d, r12d
00336ADF  8B D5                           mov edx, ebp
00336AE1  48 8B CB                        mov rcx, rbx
00336AE4  E8 E3 C3 FF FF                  call 0x140332ecc
00336AE9  44 8B 44 24 40                  mov r8d, dword ptr [rsp + 0x40]
00336AEE  BA FD FF FF FF                  mov edx, 0xfffffffd
00336AF3  E9 64 FD FF FF                  jmp 0x14033685c
00336AF8  48 3B DE                        cmp rbx, rsi
00336AFB  0F 84 D9 FE FF FF               je 0x1403369da
00336B01  48 BD FF FF FF FF FF FF FF 7F   movabs rbp, 0x7fffffffffffffff
00336B0B  F0 48 21 6B 18                  lock and qword ptr [rbx + 0x18], rbp
00336B10  E9 CF FE FF FF                  jmp 0x1403369e4
00336B15  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
00336B1A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
00336B20  48 83 EB 30                     sub rbx, 0x30
00336B24  8B D5                           mov edx, ebp
00336B26  48 8B CB                        mov rcx, rbx
00336B29  E8 52 8F F6 FF                  call 0x14029fa80
00336B2E  85 C0                           test eax, eax
00336B30  75 0A                           jne 0x140336b3c
00336B32  49 3B D8                        cmp rbx, r8
00336B35  75 E9                           jne 0x140336b20
00336B37  E9 F2 FC FF FF                  jmp 0x14033682e
00336B3C  44 89 7C 24 48                  mov dword ptr [rsp + 0x48], r15d
00336B41  E9 CD FC FF FF                  jmp 0x140336813
00336B46  8B 84 24 88 00 00 00            mov eax, dword ptr [rsp + 0x88]
00336B4D  41 8B EE                        mov ebp, r14d
00336B50  8B 94 24 8C 00 00 00            mov edx, dword ptr [rsp + 0x8c]
00336B57  85 C0                           test eax, eax
00336B59  8B C8                           mov ecx, eax
00336B5B  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
00336B62  41 0F 44 CE                     cmove ecx, r14d
00336B66  40 0F 94 C5                     sete bpl
00336B6A  3B CA                           cmp ecx, edx
00336B6C  0F 43 D1                        cmovae edx, ecx
00336B6F  41 0F 42 EF                     cmovb ebp, r15d
00336B73  3B D0                           cmp edx, eax
00336B75  B9 03 00 00 00                  mov ecx, 3
00336B7A  41 0F 42 E9                     cmovb ebp, r9d
00336B7E  0F 43 C2                        cmovae eax, edx
00336B81  3B 84 24 94 00 00 00            cmp eax, dword ptr [rsp + 0x94]
00336B88  0F 42 E9                        cmovb ebp, ecx
00336B8B  E9 78 FC FF FF                  jmp 0x140336808
00336B90  8D 4A FF                        lea ecx, [rdx - 1]
00336B93  E9 C8 F8 FF FF                  jmp 0x140336460
00336B98  41 8D 50 FF                     lea edx, [r8 - 1]
00336B9C  E9 2F F9 FF FF                  jmp 0x1403364d0
00336BA1  4C 8B F9                        mov r15, rcx
00336BA4  4C 2B FF                        sub r15, rdi
00336BA7  E9 74 F9 FF FF                  jmp 0x140336520
00336BAC  48 8B CF                        mov rcx, rdi
00336BAF  E8 70 52 00 00                  call 0x14033be24
00336BB4  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
00336BB9  44 0F B7 4C 24 44               movzx r9d, word ptr [rsp + 0x44]
00336BBF  4C 8B 5C 24 68                  mov r11, qword ptr [rsp + 0x68]
00336BC4  48 8B 48 10                     mov rcx, qword ptr [rax + 0x10]
00336BC8  49 8D 04 3F                     lea rax, [r15 + rdi]
00336BCC  4C 8B F9                        mov r15, rcx
00336BCF  4C 2B FF                        sub r15, rdi
00336BD2  48 3B C1                        cmp rax, rcx
00336BD5  4C 0F 46 FD                     cmovbe r15, rbp
00336BD9  E9 52 F9 FF FF                  jmp 0x140336530
00336BDE  41 83 FC 01                     cmp r12d, 1
00336BE2  0F 85 F6 FC FF FF               jne 0x1403368de
00336BE8  41 F7 D0                        not r8d
00336BEB  45 23 C4                        and r8d, r12d
00336BEE  41 8B C0                        mov eax, r8d
00336BF1  E9 F4 FC FF FF                  jmp 0x1403368ea
00336BF6  45 33 C0                        xor r8d, r8d
00336BF9  41 8B D1                        mov edx, r9d
00336BFC  48 8B CF                        mov rcx, rdi
00336BFF  E8 58 F3 10 00                  call 0x140445f5c
00336C04  41 8B C6                        mov eax, r14d
00336C07  41 B9 02 00 00 00               mov r9d, 2
00336C0D  E9 D8 FC FF FF                  jmp 0x1403368ea
00336C12  4D 85 D2                        test r10, r10
00336C15  0F 84 83 B3 3A 00               je 0x1406e1f9e
00336C1B  41 8B 82 50 3B 00 00            mov eax, dword ptr [r10 + 0x3b50]
00336C22  84 C1                           test cl, al
00336C24  0F 85 A1 FC FF FF               jne 0x1403368cb
00336C2A  E9 6F B3 3A 00                  jmp 0x1406e1f9e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCoalesceFreeSmallPages(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int16 v_stack_m94;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p40;
    unsigned __int16 v_stack_p44;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned int v_stack_p8C;
    unsigned int v_stack_p90;
    unsigned int v_stack_p94;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 11355106)) ^ (v_rsp);
    v_stack_m40 = result;
    v_r14 = 0;
    v_stack_m68 = 0;
    if ((*(unsigned __int64 *)(v_rip + 13174802)) == 0) goto loc_0033657E;
    v_rsi = (a1 + a1 * 2) << (4);
    v_rsi = (v_rsi) + (v_r10);
    if (((a2) & (1)) == 0) goto loc_003365F1;
    if ((*(unsigned __int8 *)(v_rip + 11561021)) < 2) goto loc_0033657E;
    a1 = (a1) >> (4);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11561282) + a1 * 2)) & (31));
    if (((unsigned __int8)(a1)) < 15) goto loc_0033657E;
    v_rdi = (a1) & (-16);
loc_003363D1:
    result = (*(unsigned __int64 *)(v_rsi + 40)) >> (43);
    result = (result) & ((unsigned int)(0x3FFULL));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 32))) >> (16));
    a3 = (unsigned int)((a3) & (7));
    v_stack_m90 = (unsigned int)(a3);
    v_r12 = (v_rdi + v_rdi * 2) << (4);
    v_stack_m58 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11508884) + result * 8);
    v_stack_m94 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11508884) + result * 8)));
    v_stack_m70 = v_r12 + v_r10 * 1 + 768;
    v_stack_m88 = v_r12 + v_r10 * 1;
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 11499419)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11499417))))) goto loc_0033645D;
    v_rbx = ((int)(*(unsigned int *)(v_rip + 11499419))) << (4);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 11499474));
    if (v_rdi < (*(unsigned __int64 *)(v_rbx))) goto loc_0033645D;
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 11499419)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11499417))))) goto loc_00336496;
    if (v_rdi < (*(unsigned __int64 *)(v_rbx + 16))) goto loc_00336496;
loc_0033645D:
loc_00336460:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11499417)))) < 0) goto loc_003365AC;
    a2 = (unsigned int)((0 + (unsigned int)(*(unsigned int *)(v_rip + 11499417)) * 1) >> (1));
    v_rbx = ((int)(a2)) << (4);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 11499429));
    if (v_rdi < (*(unsigned __int64 *)(v_rbx))) goto loc_003365F9;
    if (a2 != (*(unsigned int *)(v_rip + 11499322))) goto loc_003365DF;
loc_00336490:
    *(unsigned int *)(v_rip + 11499306) = a2;
loc_00336496:
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 11499299)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11499291))))) goto loc_003364CD;
    result = ((int)(*(unsigned int *)(v_rip + 11499299))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 11499362));
    if (v_rdi < (*(unsigned __int64 *)(result))) goto loc_003364CD;
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 11499299)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11499291))))) goto loc_0033650F;
    if (v_rdi < (*(unsigned __int64 *)(result + 16))) goto loc_0033650F;
loc_003364CD:
loc_003364D0:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11499291)))) < 0) goto loc_003365AC;
    a3 = (unsigned int)((0 + (unsigned int)(*(unsigned int *)(v_rip + 11499291)) * 1) >> (1));
    result = ((int)((unsigned int)(a3))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 11499315));
    if (v_rdi < (*(unsigned __int64 *)(result))) goto loc_0033661C;
    if (((unsigned int)(a3)) != (*(unsigned int *)(v_rip + 11499207))) goto loc_003365CC;
loc_00336503:
    *(unsigned int *)(v_rip + 11499190) = (unsigned int)(a3);
loc_0033650F:
    if ((v_rdi + 16) > (*(unsigned __int64 *)(result + 16))) goto loc_00336BA1;
loc_00336520:
    if ((*(unsigned __int64 *)(v_rip + 11499265)) != 0) goto loc_00336BAC;
loc_00336530:
    if (16 != 16) goto loc_0033657E;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m88 + 32))) >> (16));
    v_rbp = (unsigned int)(((unsigned __int8)(result)) >> (6));
loc_0033654C:
    if ((v_stack_m88 + 32 - 32) == (v_r12 + v_r10 * 1 + 768)) goto loc_00336640;
    result = (*(unsigned __int64 *)(v_stack_m88 + 32 + 8)) >> (43);
    result = (unsigned __int16)((result) & ((unsigned __int16)((unsigned int)(0x3FFULL))));
    if (((unsigned __int16)(result)) != ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11508884) + result * 8))))) goto loc_0033657E;
    if (v_rsi == 0) goto loc_003365C6;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m88 + 32))) >> (16));
    result = (unsigned int)(((unsigned __int8)(result)) >> (6));
    if (((unsigned int)(result)) == ((unsigned int)(v_rbp))) goto loc_003365C6;
loc_0033657E:
    result = 0;
loc_00336580:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0x3FFULL), v_stack_m88, *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11508884) + result * 8)));
    v_rsp = (v_rsp) + (160);
    return result;
loc_003365AC:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 26, (unsigned int)(0x5180ULL), v_rdi, a4);
loc_003365C6:
    a1 = (a4 + 26) + (48);
    goto loc_0033654C;
loc_003365CC:
    if (v_rdi < (*(unsigned __int64 *)(result + 16))) goto loc_00336503;
    goto loc_003364D0;
loc_003365DF:
    if (v_rdi < (*(unsigned __int64 *)(v_stack_p18 + 16))) goto loc_00336490;
    goto loc_00336460;
loc_003365F1:
    goto loc_003363D1;
loc_003365F9:
    if ((unsigned int)((unsigned int)(0x5180ULL)) != 0) goto loc_00336B90;
    v_stack_p20 = 0;
    result = KeBugCheckEx(26, (unsigned int)(0x5180ULL), v_rdi, v_stack_p18);
loc_0033661C:
    if ((unsigned int)(v_rdi) != 0) goto loc_00336B98;
    v_stack_p20 = 0;
    result = KeBugCheckEx(26, (unsigned int)(0x5180ULL), v_rdi, result);
loc_00336640:
    v_stack_p78 = *(unsigned __int64 *)(v_rip - 3300807);
    if (0 == 0) goto loc_00336AAB;
loc_00336658:
    v_r10 = (v_r10) * (v_stack_p18);
    v_stack_p40 = 0;
    v_r10 = (v_r10) + (*(unsigned __int64 *)(v_stack_p80 + 16));
    v_stack_p58 = v_r10;
    v_r12 = (v_r12) + (v_stack_p80);
loc_00336687:
    if (v_rdi == (v_r12 + v_r10 * 1 + 768)) goto loc_003367F5;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 32))))) >> (16));
    if (v_rdi == 0) goto loc_003367CD;
    if (v_rdi > (*(unsigned __int64 *)(v_rip + 11499064))) goto loc_003369DA;
    result = (*(unsigned __int64 *)(v_r12)) >> (54);
    if (condition_is_above_or_equal) goto loc_003369DA;
    result = (*(unsigned __int64 *)(v_rdi + 40)) >> (43);
    result = (unsigned __int16)((result) & ((unsigned __int16)((unsigned int)(0x3FFULL))));
    if (((unsigned __int16)(result)) != ((unsigned __int16)(result))) goto loc_003369DA;
    a1 = (unsigned __int8)((a1) & (7));
    if (((unsigned __int8)(a1)) > 1) goto loc_003369DA;
    if (v_rdi == v_rsi) goto loc_003366FA;
    if (v_rdi < v_rsi) goto loc_003369CF;
loc_003366FA:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (16));
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) > 1) goto loc_00336AF8;
    result = (*(unsigned __int64 *)(v_rdi + 40)) >> (43);
    result = (unsigned __int16)((result) & ((unsigned __int16)((unsigned int)(0x3FFULL))));
    if (((unsigned __int16)(result)) != ((unsigned __int16)(result))) goto loc_00336AF8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) != 0) goto loc_00336AF8;
    if (0 == 0) goto loc_00336747;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (16));
    result = (unsigned int)(((unsigned __int8)(result)) >> (6));
    if (((unsigned int)(result)) != ((unsigned int)(v_rbp))) goto loc_00336AF8;
loc_00336747:
    if (((unsigned int)(result)) < ((unsigned int)(v_rbp))) goto loc_00336AF8;
    if (0 != 0) goto loc_00336788;
loc_00336761:
    a1 = (*(unsigned __int64 *)(v_r10 + 15192)) ^ (*(unsigned __int64 *)(v_r10 + 15192) + 1);
    a1 = (a1) & (0xFFFFFFFFFFFF0000ULL);
    a1 = (a1) ^ (*(unsigned __int64 *)(v_r10 + 15192) + 1);
    if (condition_is_not_equal) goto loc_00336761;
    v_stack_p40 = 1;
loc_00336788:
    a2 = 0;
    result = MiUnlinkFreeOrZeroedPage(v_rdi, a2, 256, result);
    if ((unsigned int)(result) == 0) goto loc_00336AF8;
    if (0 == 0) goto loc_00336A92;
loc_003367B9:
    v_rbx = (v_rdi) + (48);
    v_r15 = (v_rdi) + 1;
    v_r12 = (v_r12) + (48);
    goto loc_00336687;
loc_003367CD:
    result = (unsigned int)((result) >> (16));
    if ((((unsigned __int8)(result)) & (7)) == 0) goto loc_003369FA;
    result = MiSetOriginalPtePfnFromFreeList(v_rbx + 16, (unsigned int)(v_stack_p40), 256, v_stack_p44);
    v_rbx = (v_rbx) + (48);
    v_r15 = (v_r15) + 1;
    v_r12 = (v_r12) + (48);
    goto loc_00336687;
loc_003367F5:
    if (0 == 0) goto loc_00336B46;
loc_00336808:
    if (v_stack_p48 != 1) goto loc_00336B15;
loc_00336813:
    if (v_stack_p78 != 0) goto loc_00336ABB;
    result = MiMakeDemandZeroPte(v_stack_p78 + 4, (unsigned int)(v_stack_p40), 256, 2);
loc_00336829:
    v_stack_p78 = result;
loc_0033682E:
    v_stack_p40 = 0;
loc_00336850:
    if (0 == 0) goto loc_00336ACB;
loc_0033685C:
    if (*(unsigned __int64 *)(v_rip + 11498521) == 0) goto loc_00336876;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p68 - 48 + 16))) & (16)) != 0) goto loc_003368D8;
    a1 = ~(*(unsigned __int64 *)(v_rip + 11498521));
    result = (*(unsigned __int64 *)(v_stack_p68 - 48 + 16)) & (a1);
loc_00336876:
    result = (result) >> (32);
    if (result != ((unsigned int)(0xFFFFFFFDULL))) goto loc_003368D2;
    a3 = (unsigned int)((0) | (1));
loc_00336882:
    *(unsigned __int64 *)(v_stack_p68 - 48 + 16) = 0;
    v_r15 = (unsigned int)((0) + 1);
    v_rbx = (v_stack_p68 - 48) - (48);
    v_stack_p40 = (unsigned int)(a3);
    if (((unsigned int)(v_r15)) < 16) goto loc_00336850;
    result = MiColdPageSizeSupported(2, v_stack_p58, a3, 2);
    if ((unsigned int)(result) != 0) goto loc_00336BDE;
    if (((*(unsigned int *)(v_rip + 13173235)) & (0x200000ULL)) != 0) goto loc_00336C12;
loc_003368CB:
    goto loc_003368EA;
loc_003368D2:
    a3 = (unsigned int)((a3) | (2));
    goto loc_00336882;
loc_003368D8:
    result = (1) & (-17);
    goto loc_00336876;
loc_003368DE:
    if (((2) & ((unsigned __int8)(a3))) != 0) goto loc_00336BF6;
loc_003368EA:
    v_stack_p30 = 1;
    v_stack_p28 = 0;
    v_stack_p20 = (unsigned int)(v_rbp);
    result = MiInitializeAllResidentPageBasePfns(v_stack_p80, v_rdi, 16, 2);
    v_stack_p28 = 1;
    v_stack_p20 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_p80));
    result = MiCreateInitialLargeLeafPfns(v_rdi, 16, 16 - 14, (unsigned int)((unsigned int)(v_rbp)));
loc_00336951:
    if ((v_stack_p50 + 48) != v_rsi) {
    }
    a1 = (unsigned int)((1) + 1);
    result = (v_stack_p50 + 48) + (48);
    if (((unsigned int)(a1)) < 16) goto loc_00336951;
    v_r14 = ((unsigned int)((unsigned int)(v_stack_p48)) != 0) ? 1 : 0;
    result = MiInsertPageInFreeOrZeroedList(v_rdi, v_r14 + 1, 16 - 14, (unsigned int)((unsigned int)(v_rbp)));
    if (v_stack_p50 != v_rsi) {
    }
loc_00336990:
    a1 = (*(unsigned __int64 *)(v_stack_p58 + 15192) - 1) ^ (*(unsigned __int64 *)(v_stack_p58 + 15192));
    a1 = (a1) & (0xFFFFFFFFFFFF0000ULL);
    a1 = (a1) ^ (*(unsigned __int64 *)(v_stack_p58 + 15192) - 1);
    if ((unsigned __int16)(a1) == 0) {
        a2 = a1 + 65536;
        a2 = (a2) ^ (a1);
        a2 = (a2) & (0xFFFFFFFFFFFF0000ULL);
        a1 = (a1) ^ (a2);
    }
    if (condition_is_not_equal) goto loc_00336990;
    goto loc_00336580;
loc_003369CF:
    v_stack_p70 = 2;
loc_003369DA:
loc_003369E4:
    if (v_stack_p50 < 1) goto loc_00336A18;
loc_003369EB:
    if (v_stack_p40 != 0) goto loc_00336A49;
loc_003369F2:
    goto loc_00336580;
loc_003369FA:
    v_r15 = (v_stack_p50) + 1;
    result = (*(unsigned __int64 *)(1 + 16)) & (-993);
    *(unsigned __int64 *)(1 + 16) = result;
    v_rbx = (1) + (48);
    v_r12 = ((unsigned int)(v_stack_p48)) + (48);
    goto loc_00336687;
loc_00336A18:
loc_00336A1D:
    if (v_stack_p50 != 0) {
        a2 = 512;
        a1 = v_stack_p50;
        result = MiReturnFreeZeroPage(a1, a2, v_stack_p58, (unsigned int)((unsigned int)(v_rbp)));
    }
    if (v_stack_p50 != v_rsi) {
    }
    v_r14 = (v_stack_p50) + (48);
    if (v_r14 < v_rbx) goto loc_00336A1D;
    goto loc_003369EB;
loc_00336A49:
loc_00336A55:
    a1 = (*(unsigned __int64 *)(v_stack_p58 + 15192) - 1) ^ (*(unsigned __int64 *)(v_stack_p58 + 15192));
    a1 = (a1) & (0xFFFFFFFFFFFF0000ULL);
    a1 = (a1) ^ (*(unsigned __int64 *)(v_stack_p58 + 15192) - 1);
    if ((unsigned __int16)(a1) == 0) {
        a2 = a1 + 65536;
        a2 = (a2) ^ (a1);
        a2 = (a2) & (0xFFFFFFFFFFFF0000ULL);
        a1 = (a1) ^ (a2);
    }
    if (condition_is_not_equal) goto loc_00336A55;
    goto loc_003369F2;
loc_00336A92:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 32))) >> (16));
    result = ((unsigned __int8)(result)) >> (6);
    goto loc_003367B9;
loc_00336AAB:
    v_stack_p88 = v_xmm0;
    goto loc_00336658;
loc_00336ABB:
    result = (result) & (-865);
    goto loc_00336829;
loc_00336ACB:
    result = (unsigned int)((result) >> (16));
    result = (unsigned int)(((unsigned __int8)(result)) >> (6));
    if (((unsigned int)(result)) == ((unsigned int)(v_rbp))) goto loc_0033685C;
    result = MiChangePageAttribute(v_rbx, (unsigned int)((unsigned int)(v_rbp)), (unsigned int)((unsigned int)(v_r12)), (unsigned int)((unsigned int)(v_rbp)));
    goto loc_0033685C;
loc_00336AF8:
    if (v_rbx == v_rsi) goto loc_003369DA;
    goto loc_003369E4;
loc_00336B15:
loc_00336B20:
    v_rbx = (v_rbx) - (48);
    result = MiPfnZeroingNeeded(v_rbx, (unsigned int)((unsigned int)(v_rbp)), v_stack_p50, (unsigned int)((unsigned int)(v_rbp)));
    if ((unsigned int)(result) != 0) goto loc_00336B3C;
    if (v_rbx != v_stack_p50) goto loc_00336B20;
    goto loc_0033682E;
loc_00336B3C:
    v_stack_p48 = (unsigned int)(v_r15);
    goto loc_00336813;
loc_00336B46:
    a1 = (unsigned int)((unsigned int)((unsigned int)(v_stack_p88)));
    if ((unsigned int)((unsigned int)(v_stack_p88)) == 0) { a1 = (unsigned int)(v_stack_p70); }
    v_rbp = ((unsigned int)((unsigned int)(v_stack_p88)) == 0) ? 1 : 0;
    a2 = (unsigned int)(v_stack_p8C);
    if (((unsigned int)(a1)) >= ((unsigned int)((unsigned int)(v_stack_p8C)))) { a2 = (unsigned int)(a1); }
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)(v_stack_p8C)))) { v_rbp = (unsigned int)(v_r15); }
    if (a2 < ((unsigned int)((unsigned int)(v_stack_p90)))) { v_rbp = (unsigned int)((unsigned int)((unsigned int)(v_rbp))); }
    result = (unsigned int)(v_stack_p90);
    if (a2 >= ((unsigned int)((unsigned int)(v_stack_p90)))) { result = a2; }
    if (((unsigned int)(result)) < v_stack_p94) { v_rbp = 3; }
    goto loc_00336808;
loc_00336B90:
    goto loc_00336460;
loc_00336B98:
    goto loc_003364D0;
loc_00336BA1:
    v_r15 = (a2 - 1) - (v_rdi);
    goto loc_00336520;
loc_00336BAC:
    result = MiSearchChannelTable(v_rdi, v_stack_p50 - 1, v_stack_p50, (unsigned int)((unsigned int)(v_rbp)));
    v_r15 = (*(unsigned __int64 *)(result + 16)) - (v_rdi);
    if ((v_r15 + v_rdi * 1) <= (*(unsigned __int64 *)(result + 16))) { v_r15 = v_rbp; }
    goto loc_00336530;
loc_00336BDE:
    if (((unsigned int)(v_r12)) != 1) goto loc_003368DE;
    a3 = (unsigned int)(~(v_stack_p50));
    a3 = (unsigned int)((a3) & ((unsigned int)(v_r12)));
    goto loc_003368EA;
loc_00336BF6:
    a3 = 0;
    result = MiChangePageHeatImmediate(v_rdi, (unsigned int)((unsigned int)(v_stack_p44)), a3, v_stack_p44);
    goto loc_003368EA;
loc_00336C12:
    if ((((unsigned __int8)(v_rdi)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p58 + 15184))))) != 0) goto loc_003368CB;
}
```

## 5. (Beta) C Style

```c
int64_t MiCoalesceFreeSmallPages(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint16_t v_stack_m94;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p40;
    uint16_t v_stack_p44;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint32_t v_stack_p8C;
    uint32_t v_stack_p90;
    uint32_t v_stack_p94;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0xAD43E2)) ^ (local_rsp);
    v_stack_m40 = result;
    local_r14 = 0;
    v_stack_m68 = 0;
    if ((*(uint64_t *)(v_rip + 0xC90812)) == 0) goto loc_0033657E;
    local_rsi = (Arg1 + Arg1 * 2) << (4);
    local_rsi = (local_rsi) + (local_r10);
    if (((Arg2) & (1)) == 0) goto loc_003365F1;
    if ((*(uint8_t *)(v_rip + 0xB0683D)) < 2) goto loc_0033657E;
    Arg1 = (Arg1) >> (4);
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0xB06942) + arg1 * 2)) & (31));
    if (((uint8_t)(Arg1)) < 15) goto loc_0033657E;
    local_rdi = (Arg1) & (-16);
loc_003363D1:
    result = (*(uint64_t *)(local_rsi + 0x28)) >> (43);
    result = (result) & ((uint32_t)(0x3FFULL));
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x20))) >> (16));
    a3 = (uint32_t)((a3) & (7));
    v_stack_m90 = (uint32_t)(a3);
    local_r12 = (local_rdi + local_rdi * 2) << (4);
    v_stack_m58 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAF9C94) + result * 8);
    v_stack_m94 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF9C94) + result * 8)));
    v_stack_m70 = local_r12 + local_r10 * 1 + 768;
    v_stack_m88 = local_r12 + local_r10 * 1;
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xAF779B)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF7799))))) goto loc_0033645D;
    local_rbx = ((int32_t)(*(uint32_t *)(v_rip + 0xAF779B))) << (4);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0xAF77D2));
    if (local_rdi < (*(uint64_t *)(local_rbx))) goto loc_0033645D;
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xAF779B)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF7799))))) goto loc_00336496;
    if (local_rdi < (*(uint64_t *)(local_rbx + 0x10))) goto loc_00336496;
loc_0033645D:
loc_00336460:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF7799)))) < 0) goto loc_003365AC;
    Arg2 = (uint32_t)((0 + (uint32_t)(*(uint32_t *)(v_rip + 0xAF7799)) * 1) >> (1));
    local_rbx = ((int32_t)(Arg2)) << (4);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0xAF77A5));
    if (local_rdi < (*(uint64_t *)(local_rbx))) goto loc_003365F9;
    if (Arg2 != (*(uint32_t *)(v_rip + 0xAF773A))) goto loc_003365DF;
loc_00336490:
    *(uint32_t *)(v_rip + 0xAF772A) = Arg2;
loc_00336496:
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xAF7723)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF771B))))) goto loc_003364CD;
    result = ((int32_t)(*(uint32_t *)(v_rip + 0xAF7723))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xAF7762));
    if (local_rdi < (*(uint64_t *)(result))) goto loc_003364CD;
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xAF7723)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF771B))))) goto loc_0033650F;
    if (local_rdi < (*(uint64_t *)(result + 0x10))) goto loc_0033650F;
loc_003364CD:
loc_003364D0:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF771B)))) < 0) goto loc_003365AC;
    a3 = (uint32_t)((0 + (uint32_t)(*(uint32_t *)(v_rip + 0xAF771B)) * 1) >> (1));
    result = ((int32_t)((uint32_t)(a3))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xAF7733));
    if (local_rdi < (*(uint64_t *)(result))) goto loc_0033661C;
    if (((uint32_t)(a3)) != (*(uint32_t *)(v_rip + 0xAF76C7))) goto loc_003365CC;
loc_00336503:
    *(uint32_t *)(v_rip + 0xAF76B6) = (uint32_t)(a3);
loc_0033650F:
    if ((local_rdi + 16) > (*(uint64_t *)(result + 0x10))) goto loc_00336BA1;
loc_00336520:
    if ((*(uint64_t *)(v_rip + 0xAF7701)) != 0) goto loc_00336BAC;
loc_00336530:
    if (16 != 16) goto loc_0033657E;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x20))) >> (16));
    local_rbp = (uint32_t)(((uint8_t)(result)) >> (6));
loc_0033654C:
    if ((v_stack_m88 + 32 - 32) == (local_r12 + local_r10 * 1 + 768)) goto loc_00336640;
    result = (*(uint64_t *)(v_stack_m88 + 0x20 + 0x8)) >> (43);
    result = (uint16_t)((result) & ((uint16_t)((uint32_t)(0x3FFULL))));
    if (((uint16_t)(result)) != ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF9C94) + result * 8))))) goto loc_0033657E;
    if (local_rsi == 0) goto loc_003365C6;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x20))) >> (16));
    result = (uint32_t)(((uint8_t)(result)) >> (6));
    if (((uint32_t)(result)) == ((uint32_t)(local_rbp))) goto loc_003365C6;
loc_0033657E:
    result = 0;
loc_00336580:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0x3FFULL), v_stack_m88, *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF9C94) + result * 8)));
    local_rsp = (local_rsp) + (160);
    return result;
loc_003365AC:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 26, (uint32_t)(0x5180ULL), local_rdi, a4);
loc_003365C6:
    Arg1 = (a4 + 26) + (48);
    goto loc_0033654C;
loc_003365CC:
    if (local_rdi < (*(uint64_t *)(result + 0x10))) goto loc_00336503;
    goto loc_003364D0;
loc_003365DF:
    if (local_rdi < (*(uint64_t *)(v_stack_p18 + 0x10))) goto loc_00336490;
    goto loc_00336460;
loc_003365F1:
    goto loc_003363D1;
loc_003365F9:
    if ((uint32_t)((uint32_t)(0x5180ULL)) != 0) goto loc_00336B90;
    v_stack_p20 = 0;
    result = KeBugCheckEx(26, (uint32_t)(0x5180ULL), local_rdi, v_stack_p18);
loc_0033661C:
    if ((uint32_t)(local_rdi) != 0) goto loc_00336B98;
    v_stack_p20 = 0;
    result = KeBugCheckEx(26, (uint32_t)(0x5180ULL), local_rdi, result);
loc_00336640:
    v_stack_p78 = *(uint64_t *)(v_rip - 0x325DC7);
    if (0 == 0) goto loc_00336AAB;
loc_00336658:
    local_r10 = (local_r10) * (v_stack_p18);
    v_stack_p40 = 0;
    local_r10 = (local_r10) + (*(uint64_t *)(v_stack_p80 + 0x10));
    v_stack_p58 = local_r10;
    local_r12 = (local_r12) + (v_stack_p80);
loc_00336687:
    if (local_rdi == (local_r12 + local_r10 * 1 + 768)) goto loc_003367F5;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x20))))) >> (16));
    if (local_rdi == 0) goto loc_003367CD;
    if (local_rdi > (*(uint64_t *)(v_rip + 0xAF7638))) goto loc_003369DA;
    result = (*(uint64_t *)(local_r12)) >> (54);
    if (condition_is_above_or_equal) goto loc_003369DA;
    result = (*(uint64_t *)(local_rdi + 0x28)) >> (43);
    result = (uint16_t)((result) & ((uint16_t)((uint32_t)(0x3FFULL))));
    if (((uint16_t)(result)) != ((uint16_t)(result))) goto loc_003369DA;
    Arg1 = (uint8_t)((Arg1) & (7));
    if (((uint8_t)(Arg1)) > 1) goto loc_003369DA;
    if (local_rdi == local_rsi) goto loc_003366FA;
    if (local_rdi < local_rsi) goto loc_003369CF;
loc_003366FA:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (16));
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) > 1) goto loc_00336AF8;
    result = (*(uint64_t *)(local_rdi + 0x28)) >> (43);
    result = (uint16_t)((result) & ((uint16_t)((uint32_t)(0x3FFULL))));
    if (((uint16_t)(result)) != ((uint16_t)(result))) goto loc_00336AF8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (64)) != 0) goto loc_00336AF8;
    if (0 == 0) goto loc_00336747;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (16));
    result = (uint32_t)(((uint8_t)(result)) >> (6));
    if (((uint32_t)(result)) != ((uint32_t)(local_rbp))) goto loc_00336AF8;
loc_00336747:
    if (((uint32_t)(result)) < ((uint32_t)(local_rbp))) goto loc_00336AF8;
    if (0 != 0) goto loc_00336788;
loc_00336761:
    Arg1 = (*(uint64_t *)(local_r10 + 0x3B58)) ^ (*(uint64_t *)(local_r10 + 0x3B58) + 1);
    Arg1 = (Arg1) & (0xFFFFFFFFFFFF0000ULL);
    Arg1 = (Arg1) ^ (*(uint64_t *)(local_r10 + 0x3B58) + 1);
    if (condition_is_not_equal) goto loc_00336761;
    v_stack_p40 = 1;
loc_00336788:
    Arg2 = 0;
    result = MiUnlinkFreeOrZeroedPage(local_rdi, Arg2, 256, result);
    if ((uint32_t)(result) == 0) goto loc_00336AF8;
    if (0 == 0) goto loc_00336A92;
loc_003367B9:
    local_rbx = (local_rdi) + (48);
    local_r15 = (local_rdi) + 1;
    local_r12 = (local_r12) + (48);
    goto loc_00336687;
loc_003367CD:
    result = (uint32_t)((result) >> (16));
    if ((((uint8_t)(result)) & (7)) == 0) goto loc_003369FA;
    result = MiSetOriginalPtePfnFromFreeList(local_rbx + 16, (uint32_t)(v_stack_p40), 256, v_stack_p44);
    local_rbx = (local_rbx) + (48);
    local_r15 = (local_r15) + 1;
    local_r12 = (local_r12) + (48);
    goto loc_00336687;
loc_003367F5:
    if (0 == 0) goto loc_00336B46;
loc_00336808:
    if (v_stack_p48 != 1) goto loc_00336B15;
loc_00336813:
    if (v_stack_p78 != 0) goto loc_00336ABB;
    result = MiMakeDemandZeroPte(v_stack_p78 + 4, (uint32_t)(v_stack_p40), 256, 2);
loc_00336829:
    v_stack_p78 = result;
loc_0033682E:
    v_stack_p40 = 0;
loc_00336850:
    if (0 == 0) goto loc_00336ACB;
loc_0033685C:
    if (*(uint64_t *)(v_rip + 0xAF7419) == 0) goto loc_00336876;
    if ((((uint8_t)(*(uint64_t *)(v_stack_p68 - 0x30 + 0x10))) & (16)) != 0) goto loc_003368D8;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xAF7419));
    result = (*(uint64_t *)(v_stack_p68 - 0x30 + 0x10)) & (Arg1);
loc_00336876:
    result = (result) >> (32);
    if (result != ((uint32_t)(0xFFFFFFFDULL))) goto loc_003368D2;
    a3 = (uint32_t)((0) | (1));
loc_00336882:
    *(uint64_t *)(v_stack_p68 - 0x30 + 0x10) = 0;
    local_r15 = (uint32_t)((0) + 1);
    local_rbx = (v_stack_p68 - 48) - (48);
    v_stack_p40 = (uint32_t)(a3);
    if (((uint32_t)(local_r15)) < 16) goto loc_00336850;
    result = MiColdPageSizeSupported(2, v_stack_p58, a3, 2);
    if ((uint32_t)(result) != 0) goto loc_00336BDE;
    if (((*(uint32_t *)(v_rip + 0xC901F3)) & (0x200000ULL)) != 0) goto loc_00336C12;
loc_003368CB:
    goto loc_003368EA;
loc_003368D2:
    a3 = (uint32_t)((a3) | (2));
    goto loc_00336882;
loc_003368D8:
    result = (1) & (-17);
    goto loc_00336876;
loc_003368DE:
    if (((2) & ((uint8_t)(a3))) != 0) goto loc_00336BF6;
loc_003368EA:
    v_stack_p30 = 1;
    v_stack_p28 = 0;
    v_stack_p20 = (uint32_t)(local_rbp);
    result = MiInitializeAllResidentPageBasePfns(v_stack_p80, local_rdi, 16, 2);
    v_stack_p28 = 1;
    v_stack_p20 = (uint16_t)(*(uint16_t *)(v_stack_p80));
    result = MiCreateInitialLargeLeafPfns(local_rdi, 16, 16 - 14, (uint32_t)((uint32_t)(local_rbp)));
loc_00336951:
    if ((v_stack_p50 + 48) != local_rsi) {
    }
    Arg1 = (uint32_t)((1) + 1);
    result = (v_stack_p50 + 48) + (48);
    if (((uint32_t)(Arg1)) < 16) goto loc_00336951;
    local_r14 = ((uint32_t)((uint32_t)(v_stack_p48)) != 0) ? 1 : 0;
    result = MiInsertPageInFreeOrZeroedList(local_rdi, local_r14 + 1, 16 - 14, (uint32_t)((uint32_t)(local_rbp)));
    if (v_stack_p50 != local_rsi) {
    }
loc_00336990:
    Arg1 = (*(uint64_t *)(v_stack_p58 + 0x3B58) - 1) ^ (*(uint64_t *)(v_stack_p58 + 0x3B58));
    Arg1 = (Arg1) & (0xFFFFFFFFFFFF0000ULL);
    Arg1 = (Arg1) ^ (*(uint64_t *)(v_stack_p58 + 0x3B58) - 1);
    if ((uint16_t)(Arg1) == 0) {
        Arg2 = Arg1 + 65536;
        Arg2 = (Arg2) ^ (Arg1);
        Arg2 = (Arg2) & (0xFFFFFFFFFFFF0000ULL);
        Arg1 = (Arg1) ^ (Arg2);
    }
    if (condition_is_not_equal) goto loc_00336990;
    goto loc_00336580;
loc_003369CF:
    v_stack_p70 = 2;
loc_003369DA:
loc_003369E4:
    if (v_stack_p50 < 1) goto loc_00336A18;
loc_003369EB:
    if (v_stack_p40 != 0) goto loc_00336A49;
loc_003369F2:
    goto loc_00336580;
loc_003369FA:
    local_r15 = (v_stack_p50) + 1;
    result = (*(uint64_t *)(1 + 0x10)) & (-993);
    *(uint64_t *)(1 + 0x10) = result;
    local_rbx = (1) + (48);
    local_r12 = ((uint32_t)(v_stack_p48)) + (48);
    goto loc_00336687;
loc_00336A18:
loc_00336A1D:
    if (v_stack_p50 != 0) {
        Arg2 = 512;
        Arg1 = v_stack_p50;
        result = MiReturnFreeZeroPage(Arg1, Arg2, v_stack_p58, (uint32_t)((uint32_t)(local_rbp)));
    }
    if (v_stack_p50 != local_rsi) {
    }
    local_r14 = (v_stack_p50) + (48);
    if (local_r14 < local_rbx) goto loc_00336A1D;
    goto loc_003369EB;
loc_00336A49:
loc_00336A55:
    Arg1 = (*(uint64_t *)(v_stack_p58 + 0x3B58) - 1) ^ (*(uint64_t *)(v_stack_p58 + 0x3B58));
    Arg1 = (Arg1) & (0xFFFFFFFFFFFF0000ULL);
    Arg1 = (Arg1) ^ (*(uint64_t *)(v_stack_p58 + 0x3B58) - 1);
    if ((uint16_t)(Arg1) == 0) {
        Arg2 = Arg1 + 65536;
        Arg2 = (Arg2) ^ (Arg1);
        Arg2 = (Arg2) & (0xFFFFFFFFFFFF0000ULL);
        Arg1 = (Arg1) ^ (Arg2);
    }
    if (condition_is_not_equal) goto loc_00336A55;
    goto loc_003369F2;
loc_00336A92:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x20))) >> (16));
    result = ((uint8_t)(result)) >> (6);
    goto loc_003367B9;
loc_00336AAB:
    v_stack_p88 = v_xmm0;
    goto loc_00336658;
loc_00336ABB:
    result = (result) & (-865);
    goto loc_00336829;
loc_00336ACB:
    result = (uint32_t)((result) >> (16));
    result = (uint32_t)(((uint8_t)(result)) >> (6));
    if (((uint32_t)(result)) == ((uint32_t)(local_rbp))) goto loc_0033685C;
    result = MiChangePageAttribute(local_rbx, (uint32_t)((uint32_t)(local_rbp)), (uint32_t)((uint32_t)(local_r12)), (uint32_t)((uint32_t)(local_rbp)));
    goto loc_0033685C;
loc_00336AF8:
    if (local_rbx == local_rsi) goto loc_003369DA;
    goto loc_003369E4;
loc_00336B15:
loc_00336B20:
    local_rbx = (local_rbx) - (48);
    result = MiPfnZeroingNeeded(local_rbx, (uint32_t)((uint32_t)(local_rbp)), v_stack_p50, (uint32_t)((uint32_t)(local_rbp)));
    if ((uint32_t)(result) != 0) goto loc_00336B3C;
    if (local_rbx != v_stack_p50) goto loc_00336B20;
    goto loc_0033682E;
loc_00336B3C:
    v_stack_p48 = (uint32_t)(local_r15);
    goto loc_00336813;
loc_00336B46:
    Arg1 = (uint32_t)((uint32_t)((uint32_t)(v_stack_p88)));
    if ((uint32_t)((uint32_t)(v_stack_p88)) == 0) { Arg1 = (uint32_t)(v_stack_p70); }
    local_rbp = ((uint32_t)((uint32_t)(v_stack_p88)) == 0) ? 1 : 0;
    Arg2 = (uint32_t)(v_stack_p8C);
    if (((uint32_t)(Arg1)) >= ((uint32_t)((uint32_t)(v_stack_p8C)))) { Arg2 = (uint32_t)(Arg1); }
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)(v_stack_p8C)))) { local_rbp = (uint32_t)(local_r15); }
    if (Arg2 < ((uint32_t)((uint32_t)(v_stack_p90)))) { local_rbp = (uint32_t)((uint32_t)((uint32_t)(local_rbp))); }
    result = (uint32_t)(v_stack_p90);
    if (Arg2 >= ((uint32_t)((uint32_t)(v_stack_p90)))) { result = Arg2; }
    if (((uint32_t)(result)) < v_stack_p94) { local_rbp = 3; }
    goto loc_00336808;
loc_00336B90:
    goto loc_00336460;
loc_00336B98:
    goto loc_003364D0;
loc_00336BA1:
    local_r15 = (Arg2 - 1) - (local_rdi);
    goto loc_00336520;
loc_00336BAC:
    result = MiSearchChannelTable(local_rdi, v_stack_p50 - 1, v_stack_p50, (uint32_t)((uint32_t)(local_rbp)));
    local_r15 = (*(uint64_t *)(result + 0x10)) - (local_rdi);
    if ((local_r15 + local_rdi * 1) <= (*(uint64_t *)(result + 0x10))) { local_r15 = local_rbp; }
    goto loc_00336530;
loc_00336BDE:
    if (((uint32_t)(local_r12)) != 1) goto loc_003368DE;
    a3 = (uint32_t)(~(v_stack_p50));
    a3 = (uint32_t)((a3) & ((uint32_t)(local_r12)));
    goto loc_003368EA;
loc_00336BF6:
    a3 = 0;
    result = MiChangePageHeatImmediate(local_rdi, (uint32_t)((uint32_t)(v_stack_p44)), a3, v_stack_p44);
    goto loc_003368EA;
loc_00336C12:
    if ((((uint8_t)(local_rdi)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x3B50))))) != 0) goto loc_003368CB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rcx*2` | `64` | `R` |
| `Arg1` | `+ 0x0 + rdi*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00336340&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
