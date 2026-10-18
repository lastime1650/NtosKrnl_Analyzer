# MiReservePageFileSpace

- RVA: `0x00383ED8`–`0x0038439C` (길이 `1,220` bytes)
- VA: `0x0000000140383ED8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007BC00`
- 디코드: `330`개 명령, `1,220/1,220` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00383F5A` → [MiGetPageFileSectionForReservation](MiGetPageFileSectionForReservation_function_00385E2C.md) (function, `0x00385E2C`)
- `0x00383FA5` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x00383FAD` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x00383FBA` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x003840F2` → [MiReservePageFileSpaceForPage](MiReservePageFileSpaceForPage_function_0038377C.md) (function, `0x0038377C`)
- `0x00384137` → [MiReservePageFileSpaceForPage](MiReservePageFileSpaceForPage_function_0038377C.md) (function, `0x0038377C`)
- `0x00384193` → [MiUpdatePageFileHighInPte](../36/MiUpdatePageFileHighInPte_function_0036D840.md) (function, `0x0036D840`)
- `0x003841A7` → [MI_IS_PTE_IN_WS_SWAP_SET](MI_IS_PTE_IN_WS_SWAP_SET_function_00385DD8.md) (function, `0x00385DD8`)
- `0x003841CF` → [MiFindFreePageFileSpace](../3E/MiFindFreePageFileSpace_function_003E2CAC.md) (function, `0x003E2CAC`)
- `0x00384209` → [MiReservePageFileSpaceForPage](MiReservePageFileSpaceForPage_function_0038377C.md) (function, `0x0038377C`)
- `0x00384243` → [MiUpdatePageFileHighInPte](../36/MiUpdatePageFileHighInPte_function_0036D840.md) (function, `0x0036D840`)
- `0x00384275` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00384280` → [MiDecrementModifiedWriteCount](../29/MiDecrementModifiedWriteCount_function_00298184.md) (function, `0x00298184`)
- `0x00384291` → [MiReleaseControlAreaWaiters](../28/MiReleaseControlAreaWaiters_function_002865F0.md) (function, `0x002865F0`)
- `0x00384392` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)

### Direct callers
- [sub_0023FFC8](../23/Unknown_function_0023FFC8.md) at `0x00240099`
- [MiFillNoReservationCluster](../40/MiFillNoReservationCluster_function_00405B40.md) at `0x00405CE6`

### Static image references
- `0x0038416A` → RVA `0x00E2DC80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x003842F5` → [sub_006E4988 + 0x50](../6E/Unknown_function_006E4988.md) (`tail-transfer`)
  - `0x0038432F` → [sub_006E4988](../6E/Unknown_function_006E4988.md) (`tail-transfer`)
  - `0x00384338` → [sub_006E4988 + 0x8](../6E/Unknown_function_006E4988.md) (`tail-transfer`)
  - `0x0038434D` → [sub_006E4988 + 0x24](../6E/Unknown_function_006E4988.md) (`tail-transfer`)
  - `0x00384356` → [sub_006E4988 + 0x24](../6E/Unknown_function_006E4988.md) (`tail-transfer`)
  - `0x00384365` → [sub_006E4988 + 0x24](../6E/Unknown_function_006E4988.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00383ED8  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00383EDD  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00383EE2  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00383EE7  55                              push rbp
00383EE8  56                              push rsi
00383EE9  57                              push rdi
00383EEA  41 54                           push r12
00383EEC  41 55                           push r13
00383EEE  41 56                           push r14
00383EF0  41 57                           push r15
00383EF2  48 8B EC                        mov rbp, rsp
00383EF5  48 83 EC 70                     sub rsp, 0x70
00383EF9  48 8B C1                        mov rax, rcx
00383EFC  0F 57 C0                        xorps xmm0, xmm0
00383EFF  33 C9                           xor ecx, ecx
00383F01  4D 8B E0                        mov r12, r8
00383F04  4C 8B EA                        mov r13, rdx
00383F07  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
00383F0B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00383F0F  8B B0 98 03 00 00               mov esi, dword ptr [rax + 0x398]
00383F15  8B FE                           mov edi, esi
00383F17  81 E7 FF 03 00 00               and edi, 0x3ff
00383F1D  89 75 B8                        mov dword ptr [rbp - 0x48], esi
00383F20  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00383F24  83 FF 10                        cmp edi, 0x10
00383F27  73 19                           jae 0x140383f42
00383F29  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
00383F31  48 83 C4 70                     add rsp, 0x70
00383F35  41 5F                           pop r15
00383F37  41 5E                           pop r14
00383F39  41 5D                           pop r13
00383F3B  41 5C                           pop r12
00383F3D  5F                              pop rdi
00383F3E  5E                              pop rsi
00383F3F  5D                              pop rbp
00383F40  C3                              ret
00383F41  CC                              int3
00383F42  21 4D B0                        and dword ptr [rbp - 0x50], ecx
00383F45  33 DB                           xor ebx, ebx
00383F47  44 8D 7B 01                     lea r15d, [rbx + 1]
00383F4B  4D 85 E4                        test r12, r12
00383F4E  75 24                           jne 0x140383f74
00383F50  45 8B C7                        mov r8d, r15d
00383F53  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00383F57  49 8B CD                        mov rcx, r13
00383F5A  E8 CD 1E 00 00                  call 0x140385e2c
00383F5F  85 C0                           test eax, eax
00383F61  74 C6                           je 0x140383f29
00383F63  4C 8B 75 E8                     mov r14, qword ptr [rbp - 0x18]
00383F67  44 89 7D B0                     mov dword ptr [rbp - 0x50], r15d
00383F6B  4C 8B 7D E0                     mov r15, qword ptr [rbp - 0x20]
00383F6F  E9 1C 01 00 00                  jmp 0x140384090
00383F74  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
00383F7B  A8 0F                           test al, 0xf
00383F7D  0F 85 80 03 00 00               jne 0x140384303
00383F83  4D 8B F5                        mov r14, r13
00383F86  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00383F90  49 C1 E6 19                     shl r14, 0x19
00383F94  48 8B C0                        mov rax, rax
00383F97  48 C1 E0 19                     shl rax, 0x19
00383F9B  41 8B CF                        mov ecx, r15d
00383F9E  4C 2B F0                        sub r14, rax
00383FA1  49 C1 FE 10                     sar r14, 0x10
00383FA5  E8 46 81 EF FF                  call 0x14027c0f0
00383FAA  49 8B CE                        mov rcx, r14
00383FAD  E8 1E 29 F9 FF                  call 0x1403168d0
00383FB2  B2 11                           mov dl, 0x11
00383FB4  41 8B CF                        mov ecx, r15d
00383FB7  48 8B D8                        mov rbx, rax
00383FBA  E8 61 30 F1 FF                  call 0x140297020
00383FBF  48 85 DB                        test rbx, rbx
00383FC2  0F 84 61 FF FF FF               je 0x140383f29
00383FC8  8B 53 30                        mov edx, dword ptr [rbx + 0x30]
00383FCB  41 B8 00 00 20 00               mov r8d, 0x200000
00383FD1  F6 C2 70                        test dl, 0x70
00383FD4  8B C2                           mov eax, edx
00383FD6  0F 94 C1                        sete cl
00383FD9  25 04 00 20 00                  and eax, 0x200004
00383FDE  41 3B C0                        cmp eax, r8d
00383FE1  0F 94 C0                        sete al
00383FE4  84 C8                           test al, cl
00383FE6  0F 84 3D FF FF FF               je 0x140383f29
00383FEC  41 85 D0                        test r8d, edx
00383FEF  74 1C                           je 0x14038400d
00383FF1  0F BA E2 17                     bt edx, 0x17
00383FF5  0F 82 2E FF FF FF               jb 0x140383f29
00383FFB  81 E2 00 00 18 00               and edx, 0x180000
00384001  81 FA 00 00 10 00               cmp edx, 0x100000
00384007  0F 83 1C FF FF FF               jae 0x140383f29
0038400D  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
00384010  49 81 E6 00 00 E0 FF            and r14, 0xffffffffffe00000
00384017  0F B6 4B 20                     movzx ecx, byte ptr [rbx + 0x20]
0038401B  48 BA FF FF FF FF 0F 00 00 00   movabs rdx, 0xfffffffff
00384025  48 C1 E1 20                     shl rcx, 0x20
00384029  49 B8 F8 FF FF FF 7F 00 00 00   movabs r8, 0x7ffffffff8
00384033  48 0B C8                        or rcx, rax
00384036  48 8B C1                        mov rax, rcx
00384039  48 C1 E0 0C                     shl rax, 0xc
0038403D  4C 3B F0                        cmp r14, rax
00384040  0F 83 6D 02 00 00               jae 0x1403842b3
00384046  48 23 CA                        and rcx, rdx
00384049  48 C1 E1 03                     shl rcx, 3
0038404D  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
00384057  49 8B C1                        mov rax, r9
0038405A  4C 8D 3C 01                     lea r15, [rcx + rax]
0038405E  49 81 C6 00 F0 1F 00            add r14, 0x1ff000
00384065  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
00384068  0F B6 4B 21                     movzx ecx, byte ptr [rbx + 0x21]
0038406C  48 C1 E1 20                     shl rcx, 0x20
00384070  48 0B C8                        or rcx, rax
00384073  48 8B C1                        mov rax, rcx
00384076  48 C1 E0 0C                     shl rax, 0xc
0038407A  4C 3B F0                        cmp r14, rax
0038407D  0F 87 3F 02 00 00               ja 0x1403842c2
00384083  49 C1 EE 09                     shr r14, 9
00384087  4D 23 F0                        and r14, r8
0038408A  49 8B C1                        mov rax, r9
0038408D  4C 03 F0                        add r14, rax
00384090  49 8B C6                        mov rax, r14
00384093  49 2B C7                        sub rax, r15
00384096  48 C1 F8 03                     sar rax, 3
0038409A  FF C0                           inc eax
0038409C  3B C7                           cmp eax, edi
0038409E  0F 87 75 02 00 00               ja 0x140384319
003840A4  49 F7 DC                        neg r12
003840A7  1B FF                           sbb edi, edi
003840A9  81 E7 80 00 00 00               and edi, 0x80
003840AF  FF C7                           inc edi
003840B1  48 85 DB                        test rbx, rbx
003840B4  74 16                           je 0x1403840cc
003840B6  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
003840B9  0F BA E0 19                     bt eax, 0x19
003840BD  73 0D                           jae 0x1403840cc
003840BF  25 80 0F 00 00                  and eax, 0xf80
003840C4  83 C8 40                        or eax, 0x40
003840C7  C1 E8 05                        shr eax, 5
003840CA  0B F8                           or edi, eax
003840CC  33 DB                           xor ebx, ebx
003840CE  4D 8D 65 F8                     lea r12, [r13 - 8]
003840D2  21 5D 58                        and dword ptr [rbp + 0x58], ebx
003840D5  48 89 5D C0                     mov qword ptr [rbp - 0x40], rbx
003840D9  4D 3B E7                        cmp r12, r15
003840DC  72 36                           jb 0x140384114
003840DE  8B 75 58                        mov esi, dword ptr [rbp + 0x58]
003840E1  4C 8B 6D 40                     mov r13, qword ptr [rbp + 0x40]
003840E5  4C 8D 4D C0                     lea r9, [rbp - 0x40]
003840E9  44 8B C7                        mov r8d, edi
003840EC  49 8B D4                        mov rdx, r12
003840EF  49 8B CD                        mov rcx, r13
003840F2  E8 85 F6 FF FF                  call 0x14038377c
003840F7  85 C0                           test eax, eax
003840F9  74 0B                           je 0x140384106
003840FB  FF C6                           inc esi
003840FD  49 83 EC 08                     sub r12, 8
00384101  4D 3B E7                        cmp r12, r15
00384104  73 DF                           jae 0x1403840e5
00384106  48 8B 5D C0                     mov rbx, qword ptr [rbp - 0x40]
0038410A  4C 8B 6D 48                     mov r13, qword ptr [rbp + 0x48]
0038410E  89 75 58                        mov dword ptr [rbp + 0x58], esi
00384111  8B 75 B8                        mov esi, dword ptr [rbp - 0x48]
00384114  33 C9                           xor ecx, ecx
00384116  4D 8D 65 08                     lea r12, [r13 + 8]
0038411A  45 33 FF                        xor r15d, r15d
0038411D  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
00384121  4D 3B E6                        cmp r12, r14
00384124  77 2E                           ja 0x140384154
00384126  4C 8B 6D 40                     mov r13, qword ptr [rbp + 0x40]
0038412A  4C 8D 4D C8                     lea r9, [rbp - 0x38]
0038412E  44 8B C7                        mov r8d, edi
00384131  49 8B D4                        mov rdx, r12
00384134  49 8B CD                        mov rcx, r13
00384137  E8 40 F6 FF FF                  call 0x14038377c
0038413C  85 C0                           test eax, eax
0038413E  74 0C                           je 0x14038414c
00384140  41 FF C7                        inc r15d
00384143  49 83 C4 08                     add r12, 8
00384147  4D 3B E6                        cmp r12, r14
0038414A  76 DE                           jbe 0x14038412a
0038414C  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00384150  4C 8B 6D 48                     mov r13, qword ptr [rbp + 0x48]
00384154  44 8B 75 58                     mov r14d, dword ptr [rbp + 0x58]
00384158  45 33 E4                        xor r12d, r12d
0038415B  41 FF C6                        inc r14d
0038415E  45 03 F7                        add r14d, r15d
00384161  48 85 DB                        test rbx, rbx
00384164  0F 84 31 01 00 00               je 0x14038429b
0038416A  48 8B 0D 0F 9B AA 00            mov rcx, qword ptr [rip + 0xaa9b0f]
00384171  48 8B D3                        mov rdx, rbx
00384174  48 8B C3                        mov rax, rbx
00384177  48 85 C9                        test rcx, rcx
0038417A  74 0D                           je 0x140384189
0038417C  A8 10                           test al, 0x10
0038417E  75 09                           jne 0x140384189
00384180  48 8B D1                        mov rdx, rcx
00384183  48 F7 D2                        not rdx
00384186  48 23 D0                        and rdx, rax
00384189  48 C1 EA 20                     shr rdx, 0x20
0038418D  48 8B CB                        mov rcx, rbx
00384190  48 FF C2                        inc rdx
00384193  E8 A8 96 FE FF                  call 0x14036d840
00384198  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0038419C  48 8B 5D 40                     mov rbx, qword ptr [rbp + 0x40]
003841A0  48 8D 55 B8                     lea rdx, [rbp - 0x48]
003841A4  48 8B CB                        mov rcx, rbx
003841A7  E8 2C 1C 00 00                  call 0x140385dd8
003841AC  85 C0                           test eax, eax
003841AE  0F 85 B6 01 00 00               jne 0x14038436a
003841B4  41 83 FE 01                     cmp r14d, 1
003841B8  0F 84 98 00 00 00               je 0x140384256
003841BE  41 83 CC 01                     or r12d, 1
003841C2  45 8B C6                        mov r8d, r14d
003841C5  45 8B CC                        mov r9d, r12d
003841C8  48 8D 55 B8                     lea rdx, [rbp - 0x48]
003841CC  48 8B CB                        mov rcx, rbx
003841CF  E8 D8 EA 05 00                  call 0x1403e2cac
003841D4  8B D0                           mov edx, eax
003841D6  41 3B C6                        cmp eax, r14d
003841D9  0F 85 F2 00 00 00               jne 0x1403842d1
003841DF  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
003841E2  4A 8D 34 FD 00 00 00 00         lea rsi, [r15*8]
003841EA  49 03 F5                        add rsi, r13
003841ED  48 C1 E0 03                     shl rax, 3
003841F1  83 E7 FE                        and edi, 0xfffffffe
003841F4  4C 2B E8                        sub r13, rax
003841F7  4C 3B EE                        cmp r13, rsi
003841FA  77 63                           ja 0x14038425f
003841FC  4C 8D 4D B8                     lea r9, [rbp - 0x48]
00384200  44 8B C7                        mov r8d, edi
00384203  49 8B D5                        mov rdx, r13
00384206  48 8B CB                        mov rcx, rbx
00384209  E8 6E F5 FF FF                  call 0x14038377c
0038420E  48 8B 5D B8                     mov rbx, qword ptr [rbp - 0x48]
00384212  85 C0                           test eax, eax
00384214  0F 84 6B 01 00 00               je 0x140384385
0038421A  48 8B 0D 5F 9A AA 00            mov rcx, qword ptr [rip + 0xaa9a5f]
00384221  48 8B D3                        mov rdx, rbx
00384224  48 8B C3                        mov rax, rbx
00384227  48 85 C9                        test rcx, rcx
0038422A  74 0D                           je 0x140384239
0038422C  A8 10                           test al, 0x10
0038422E  75 09                           jne 0x140384239
00384230  48 8B D1                        mov rdx, rcx
00384233  48 F7 D2                        not rdx
00384236  48 23 D0                        and rdx, rax
00384239  48 C1 EA 20                     shr rdx, 0x20
0038423D  48 8B CB                        mov rcx, rbx
00384240  48 FF C2                        inc rdx
00384243  E8 F8 95 FE FF                  call 0x14036d840
00384248  48 8B 5D 40                     mov rbx, qword ptr [rbp + 0x40]
0038424C  49 83 C5 08                     add r13, 8
00384250  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00384254  EB A1                           jmp 0x1403841f7
00384256  45 85 E4                        test r12d, r12d
00384259  0F 84 1B 01 00 00               je 0x14038437a
0038425F  83 7D B0 00                     cmp dword ptr [rbp - 0x50], 0
00384263  0F 84 C0 FC FF FF               je 0x140383f29
00384269  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
0038426D  48 85 C9                        test rcx, rcx
00384270  74 08                           je 0x14038427a
00384272  8A 55 F0                        mov dl, byte ptr [rbp - 0x10]
00384275  E8 16 1E EC FF                  call 0x140246090
0038427A  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
0038427E  33 D2                           xor edx, edx
00384280  E8 FF 3E F1 FF                  call 0x140298184
00384285  48 85 C0                        test rax, rax
00384288  0F 84 9B FC FF FF               je 0x140383f29
0038428E  48 8B C8                        mov rcx, rax
00384291  E8 5A 23 F0 FF                  call 0x1402865f0
00384296  E9 8E FC FF FF                  jmp 0x140383f29
0038429B  48 85 C9                        test rcx, rcx
0038429E  0F 85 99 00 00 00               jne 0x14038433d
003842A4  4C 21 65 B8                     and qword ptr [rbp - 0x48], r12
003842A8  41 BC 10 00 00 00               mov r12d, 0x10
003842AE  E9 E9 FE FF FF                  jmp 0x14038419c
003842B3  49 8B CE                        mov rcx, r14
003842B6  48 C1 E9 09                     shr rcx, 9
003842BA  49 23 C8                        and rcx, r8
003842BD  E9 8B FD FF FF                  jmp 0x14038404d
003842C2  48 23 CA                        and rcx, rdx
003842C5  49 8B C1                        mov rax, r9
003842C8  4C 8D 34 C8                     lea r14, [rax + rcx*8]
003842CC  E9 BF FD FF FF                  jmp 0x140384090
003842D1  8B CE                           mov ecx, esi
003842D3  8B C6                           mov eax, esi
003842D5  33 CA                           xor ecx, edx
003842D7  81 E1 00 FC FF FF               and ecx, 0xfffffc00
003842DD  33 CA                           xor ecx, edx
003842DF  F0 0F B1 8B 98 03 00 00         lock cmpxchg dword ptr [rbx + 0x398], ecx
003842E7  85 D2                           test edx, edx
003842E9  0F 84 70 FF FF FF               je 0x14038425f
003842EF  44 2B F2                        sub r14d, edx
003842F2  45 3B FE                        cmp r15d, r14d
003842F5  0F 82 DD 06 36 00               jb 0x1406e49d8
003842FB  45 2B FE                        sub r15d, r14d
003842FE  E9 DC FE FF FF                  jmp 0x1403841df
00384303  4D 8B FD                        mov r15, r13
00384306  49 81 E7 00 F0 FF FF            and r15, 0xfffffffffffff000
0038430D  4D 8D B7 F8 0F 00 00            lea r14, [r15 + 0xff8]
00384314  E9 77 FD FF FF                  jmp 0x140384090
00384319  4D 2B F5                        sub r14, r13
0038431C  49 8B CD                        mov rcx, r13
0038431F  49 2B CF                        sub rcx, r15
00384322  49 C1 FE 03                     sar r14, 3
00384326  48 C1 F9 03                     sar rcx, 3
0038432A  2B C7                           sub eax, edi
0038432C  44 3B F0                        cmp r14d, eax
0038432F  0F 82 53 06 36 00               jb 0x1406e4988
00384335  44 2B F0                        sub r14d, eax
00384338  E9 53 06 36 00                  jmp 0x1406e4990
0038433D  4C 8B 05 3C 99 AA 00            mov r8, qword ptr [rip + 0xaa993c]
00384344  48 8B C1                        mov rax, rcx
00384347  48 8B D1                        mov rdx, rcx
0038434A  4D 85 C0                        test r8, r8
0038434D  0F 84 59 06 36 00               je 0x1406e49ac
00384353  F6 C1 10                        test cl, 0x10
00384356  0F 85 50 06 36 00               jne 0x1406e49ac
0038435C  49 8B C0                        mov rax, r8
0038435F  48 F7 D0                        not rax
00384362  48 23 C1                        and rax, rcx
00384365  E9 42 06 36 00                  jmp 0x1406e49ac
0038436A  48 83 65 B8 00                  and qword ptr [rbp - 0x48], 0
0038436F  41 BC 10 00 00 00               mov r12d, 0x10
00384375  E9 3A FE FF FF                  jmp 0x1403841b4
0038437A  41 BC 40 00 00 00               mov r12d, 0x40
00384380  E9 39 FE FF FF                  jmp 0x1403841be
00384385  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00384389  41 B8 01 00 00 00               mov r8d, 1
0038438F  48 8B D3                        mov rdx, rbx
00384392  E8 39 FC EF FF                  call 0x140283fd0
00384397  E9 7E FE FF FF                  jmp 0x14038421a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReservePageFileSpace(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (112);
    a1 = 0;
    v_stack_m48 = 0;
    v_stack_m68 = v_xmm0;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 920))))) & (0x3FFULL));
    v_stack_m80 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 920)));
    v_stack_m58 = v_xmm0;
    if (((unsigned int)(v_rdi)) >= 16) goto loc_00383F42;
loc_00383F29:
    v_rsp = (v_rsp) + (112);
    return a1;
loc_00383F42:
    v_rbx = 0;
    if (a3 != 0) goto loc_00383F74;
    result = MiGetPageFileSectionForReservation(a2, v_stack_m68, (unsigned int)((unsigned int)(v_rbx + 1)), a4);
    if ((unsigned int)(result) == 0) goto loc_00383F29;
    v_stack_m88 = (unsigned int)(v_rbx + 1);
    goto loc_00384090;
loc_00383F74:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_rbx + 1)) + 184)))) & (15)) != 0) goto loc_00384303;
    v_r14 = (a2) << (25);
    result = ((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_rbx + 1)) + 184))) << (25);
    v_r14 = (v_r14) - (result);
    v_r14 = (v_r14) >> (16);
    result = MiLockVadTree((unsigned int)((unsigned int)(v_stack_m58)), v_stack_m68, (unsigned int)((unsigned int)(v_rbx + 1)), a4);
    result = MiLocateAddress(v_r14, v_stack_m68, (unsigned int)((unsigned int)(v_rbx + 1)), a4);
    result = MiUnlockVadTree((unsigned int)((unsigned int)(v_stack_m58)), 17, (unsigned int)((unsigned int)(v_rbx + 1)), a4);
    if (result == 0) goto loc_00383F29;
    a1 = ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 48)))) & (112)) == 0) ? 1 : 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 48))))) & (0x200004ULL));
    result = (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x200000ULL)))) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00383F29;
    if ((((unsigned int)((unsigned int)(0x200000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 48))))) == 0) goto loc_0038400D;
    if (condition_is_below) goto loc_00383F29;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0x180000ULL));
    if (((unsigned int)(a2)) >= 0x100000ULL) goto loc_00383F29;
loc_0038400D:
    v_r14 = (v_r14) & (0xFFFFFFFFFFE00000ULL);
    a1 = (*(unsigned __int8 *)(result + 32)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(result + 24)));
    result = (a1) << (12);
    if (v_r14 >= result) goto loc_003842B3;
    a1 = (a1) & (a2);
    a1 = (a1) << (3);
loc_0038404D:
    v_r14 = (v_r14) + (0x1FF000ULL);
    a1 = (*(unsigned __int8 *)(result + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(result + 28)));
    result = (a1) << (12);
    if (v_r14 > result) goto loc_003842C2;
    v_r14 = (v_r14) >> (9);
    v_r14 = (v_r14) & ((unsigned int)(0x200000ULL));
    v_r14 = (v_r14) + (a4);
loc_00384090:
    result = (v_r14) - (a1 + a4 * 1);
    result = (result) >> (3);
    result = (unsigned int)((result) + 1);
    if (((unsigned int)(result)) > ((unsigned int)(v_rdi))) goto loc_00384319;
    v_r12 = -(a3);
    v_rdi = (unsigned int)((v_rdi) & (128));
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (result == 0) goto loc_003840CC;
    result = (unsigned int)(*(unsigned int *)(result + 48));
    if (!(condition_is_above_or_equal)) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0xF80ULL));
        result = (unsigned int)((result) | (64));
        result = (unsigned int)((result) >> (5));
        v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(result)));
    }
    v_rbx = 0;
    v_stack_m78 = 0;
    if ((a2 - 8) < (a1 + a4 * 1)) goto loc_00384114;
loc_003840E5:
    result = MiReservePageFileSpaceForPage(v_stack_p8, a2 - 8, (unsigned int)((unsigned int)(v_rdi)), v_stack_m78);
    if ((unsigned int)(result) == 0) goto loc_00384106;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_p20)) + 1);
    v_r12 = (a2 - 8) - (8);
    if (v_r12 >= (a1 + a4 * 1)) goto loc_003840E5;
loc_00384106:
    v_stack_p20 = (unsigned int)(v_rsi);
loc_00384114:
    a1 = 0;
    v_r15 = 0;
    v_stack_m70 = 0;
    if ((v_stack_p10 + 8) > v_r14) goto loc_00384154;
loc_0038412A:
    result = MiReservePageFileSpaceForPage(v_stack_p8, v_stack_p10 + 8, (unsigned int)((unsigned int)(v_rdi)), v_stack_m70);
    if ((unsigned int)(result) == 0) goto loc_0038414C;
    v_r15 = (unsigned int)((v_r15) + 1);
    v_r12 = (v_stack_p10 + 8) + (8);
    if (v_r12 <= v_r14) goto loc_0038412A;
loc_0038414C:
loc_00384154:
    v_r12 = 0;
    v_r14 = (unsigned int)(((unsigned int)(v_stack_p20)) + 1);
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r15)));
    if (v_stack_m78 == 0) goto loc_0038429B;
    if (*(unsigned __int64 *)(v_rip + 11180815) == 0) goto loc_00384189;
    if ((((unsigned __int8)(v_stack_m78)) & (16)) == 0) {
        a2 = *(unsigned __int64 *)(v_rip + 11180815);
        a2 = ~(a2);
        a2 = (a2) & (v_stack_m78);
    }
    a2 = (a2) >> (32);
    a2 = (a2) + 1;
    result = MiUpdatePageFileHighInPte(v_stack_m78, a2, (unsigned int)((unsigned int)(v_rdi)), v_stack_m70);
    v_stack_m80 = result;
loc_0038419C:
    result = MI_IS_PTE_IN_WS_SWAP_SET(v_stack_p8, v_stack_m80, (unsigned int)((unsigned int)(v_rdi)), v_stack_m70);
    if ((unsigned int)(result) != 0) goto loc_0038436A;
loc_003841B4:
    if (((unsigned int)(v_r14)) == 1) goto loc_00384256;
loc_003841BE:
    v_r12 = (unsigned int)((v_r12) | (1));
    result = MiFindFreePageFileSpace(v_stack_p8, v_stack_m80, (unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)(v_r12)));
    if (((unsigned int)(result)) != ((unsigned int)(v_r14))) goto loc_003842D1;
loc_003841DF:
    v_rsi = (v_r15 * 8) + (v_stack_p10);
    result = ((unsigned int)(v_stack_p20)) << (3);
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFFEULL));
    v_r13 = (v_stack_p10) - (result);
loc_003841F7:
    if (v_r13 > v_rsi) goto loc_0038425F;
    result = MiReservePageFileSpaceForPage(v_stack_p8, v_r13, (unsigned int)((unsigned int)(v_rdi)), v_stack_m80);
    if ((unsigned int)(result) == 0) goto loc_00384385;
loc_0038421A:
    if (*(unsigned __int64 *)(v_rip + 11180639) == 0) goto loc_00384239;
    if ((((unsigned __int8)(v_stack_m80)) & (16)) == 0) {
        a2 = *(unsigned __int64 *)(v_rip + 11180639);
        a2 = ~(a2);
        a2 = (a2) & (v_stack_m80);
    }
    a2 = (a2) >> (32);
    a2 = (a2) + 1;
    result = MiUpdatePageFileHighInPte(v_stack_m80, a2, (unsigned int)((unsigned int)(v_rdi)), v_stack_m80);
    v_r13 = (v_r13) + (8);
    v_stack_m80 = result;
    goto loc_003841F7;
loc_00384256:
    if ((unsigned int)(v_r12) == 0) goto loc_0038437A;
loc_0038425F:
    if (v_stack_m88 == 0) goto loc_00383F29;
    if (v_stack_m60 != 0) {
        a2 = v_stack_m48;
        result = MiUnlockProtoPoolPage(v_stack_m60, a2, (unsigned int)((unsigned int)(v_rdi)), v_stack_m80);
    }
    a2 = 0;
    result = MiDecrementModifiedWriteCount(v_stack_m68, a2, (unsigned int)((unsigned int)(v_rdi)), v_stack_m80);
    if (result == 0) goto loc_00383F29;
    result = MiReleaseControlAreaWaiters(result, a2, (unsigned int)((unsigned int)(v_rdi)), v_stack_m80);
    goto loc_00383F29;
loc_0038429B:
    if (result != 0) goto loc_0038433D;
    goto loc_0038419C;
loc_003842B3:
    a1 = (v_r14) >> (9);
    a1 = (a1) & ((unsigned int)((unsigned int)(v_rdi)));
    goto loc_0038404D;
loc_003842C2:
    a1 = (a1) & (0);
    goto loc_00384090;
loc_003842D1:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) ^ (0));
    a1 = (unsigned int)((a1) & (0xFFFFFC00ULL));
    a1 = (unsigned int)((a1) ^ (0));
    if (0 == 0) goto loc_0038425F;
    v_r14 = (unsigned int)((v_stack_m80 + a1 * 8) - (0));
    v_r15 = (unsigned int)((v_r15) - ((unsigned int)(v_r14)));
    goto loc_003841DF;
loc_00384303:
    v_r15 = (v_r13) & (0xFFFFFFFFFFFFF000ULL);
    goto loc_00384090;
loc_00384319:
    v_r14 = (v_r15 + 4088) - (v_r13);
    a1 = (v_r13) - (v_r15);
    v_r14 = (v_r14) >> (3);
    a1 = (a1) >> (3);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) - ((unsigned int)(v_rdi)));
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)(result)));
loc_0038433D:
    result = ~(*(unsigned __int64 *)(v_rip + 11180348));
    result = (result) & (a1);
loc_0038436A:
    goto loc_003841B4;
loc_0038437A:
    goto loc_003841BE;
loc_00384385:
    result = MiReleasePageFileInfo(v_stack_p8, v_stack_p8, 1, v_stack_m80);
    goto loc_0038421A;
}
```

## 5. (Beta) C Style

```c
void *MiReservePageFileSpace(void *Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p18 = local_rbx;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (112);
    Arg1 = 0;
    v_stack_m48 = 0;
    v_stack_m68 = v_xmm0;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x398))))) & (0x3FFULL));
    v_stack_m80 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x398)));
    v_stack_m58 = v_xmm0;
    if (((uint32_t)(local_rdi)) >= 16) goto loc_00383F42;
loc_00383F29:
    local_rsp = (local_rsp) + (112);
    return Arg1;
loc_00383F42:
    local_rbx = 0;
    if (Arg3 != NULL) goto loc_00383F74;
    result = MiGetPageFileSectionForReservation(Arg2, v_stack_m68, (uint32_t)((uint32_t)(local_rbx + 1)), a4);
    if ((uint32_t)(result) == 0) goto loc_00383F29;
    v_stack_m88 = (uint32_t)(local_rbx + 1);
    goto loc_00384090;
loc_00383F74:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_rbx + 0x1)) + 0xB8)))) & (15)) != 0) goto loc_00384303;
    local_r14 = (Arg2) << (25);
    result = ((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_rbx + 0x1)) + 0xB8))) << (25);
    local_r14 = (local_r14) - (result);
    local_r14 = (local_r14) >> (16);
    result = MiLockVadTree((uint32_t)((uint32_t)(v_stack_m58)), v_stack_m68, (uint32_t)((uint32_t)(local_rbx + 1)), a4);
    result = MiLocateAddress(local_r14, v_stack_m68, (uint32_t)((uint32_t)(local_rbx + 1)), a4);
    result = MiUnlockVadTree((uint32_t)((uint32_t)(v_stack_m58)), 17, (uint32_t)((uint32_t)(local_rbx + 1)), a4);
    if (result == 0) goto loc_00383F29;
    Arg1 = ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x30)))) & (112)) == 0) ? 1 : 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30))))) & (0x200004ULL));
    result = (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x200000ULL)))) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00383F29;
    if ((((uint32_t)((uint32_t)(0x200000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30))))) == 0) goto loc_0038400D;
    if (condition_is_below) goto loc_00383F29;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0x180000ULL));
    if (((uint32_t)(Arg2)) >= 0x100000ULL) goto loc_00383F29;
loc_0038400D:
    local_r14 = (local_r14) & (0xFFFFFFFFFFE00000ULL);
    Arg1 = (*(uint8_t *)(result + 0x20)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(result + 0x18)));
    result = (Arg1) << (12);
    if (local_r14 >= result) goto loc_003842B3;
    Arg1 = (Arg1) & (Arg2);
    Arg1 = (Arg1) << (3);
loc_0038404D:
    local_r14 = (local_r14) + (0x1FF000ULL);
    Arg1 = (*(uint8_t *)(result + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    result = (Arg1) << (12);
    if (local_r14 > result) goto loc_003842C2;
    local_r14 = (local_r14) >> (9);
    local_r14 = (local_r14) & ((uint32_t)(0x200000ULL));
    local_r14 = (local_r14) + (a4);
loc_00384090:
    result = (local_r14) - (Arg1 + a4 * 1);
    result = (result) >> (3);
    result = (uint32_t)((result) + 1);
    if (((uint32_t)(result)) > ((uint32_t)(local_rdi))) goto loc_00384319;
    local_r12 = -(Arg3);
    local_rdi = (uint32_t)((local_rdi) & (128));
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (result == 0) goto loc_003840CC;
    result = (uint32_t)(*(uint32_t *)(result + 0x30));
    if (!(condition_is_above_or_equal)) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0xF80ULL));
        result = (uint32_t)((result) | (64));
        result = (uint32_t)((result) >> (5));
        local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(result)));
    }
    local_rbx = 0;
    v_stack_m78 = 0;
    if ((Arg2 - 8) < (Arg1 + a4 * 1)) goto loc_00384114;
loc_003840E5:
    result = MiReservePageFileSpaceForPage(v_stack_p8, Arg2 - 8, (uint32_t)((uint32_t)(local_rdi)), v_stack_m78);
    if ((uint32_t)(result) == 0) goto loc_00384106;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_p20)) + 1);
    local_r12 = (Arg2 - 8) - (8);
    if (local_r12 >= (Arg1 + a4 * 1)) goto loc_003840E5;
loc_00384106:
    v_stack_p20 = (uint32_t)(local_rsi);
loc_00384114:
    Arg1 = 0;
    local_r15 = 0;
    v_stack_m70 = 0;
    if ((v_stack_p10 + 8) > local_r14) goto loc_00384154;
loc_0038412A:
    result = MiReservePageFileSpaceForPage(v_stack_p8, v_stack_p10 + 8, (uint32_t)((uint32_t)(local_rdi)), v_stack_m70);
    if ((uint32_t)(result) == 0) goto loc_0038414C;
    local_r15 = (uint32_t)((local_r15) + 1);
    local_r12 = (v_stack_p10 + 8) + (8);
    if (local_r12 <= local_r14) goto loc_0038412A;
loc_0038414C:
loc_00384154:
    local_r12 = 0;
    local_r14 = (uint32_t)(((uint32_t)(v_stack_p20)) + 1);
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r15)));
    if (v_stack_m78 == 0) goto loc_0038429B;
    if (*(uint64_t *)(v_rip + 0xAA9B0F) == 0) goto loc_00384189;
    if ((((uint8_t)(v_stack_m78)) & (16)) == 0) {
        Arg2 = *(uint64_t *)(v_rip + 0xAA9B0F);
        Arg2 = ~(Arg2);
        Arg2 = (Arg2) & (v_stack_m78);
    }
    Arg2 = (Arg2) >> (32);
    Arg2 = (Arg2) + 1;
    result = MiUpdatePageFileHighInPte(v_stack_m78, Arg2, (uint32_t)((uint32_t)(local_rdi)), v_stack_m70);
    v_stack_m80 = result;
loc_0038419C:
    result = MI_IS_PTE_IN_WS_SWAP_SET(v_stack_p8, v_stack_m80, (uint32_t)((uint32_t)(local_rdi)), v_stack_m70);
    if ((uint32_t)(result) != 0) goto loc_0038436A;
loc_003841B4:
    if (((uint32_t)(local_r14)) == 1) goto loc_00384256;
loc_003841BE:
    local_r12 = (uint32_t)((local_r12) | (1));
    result = MiFindFreePageFileSpace(v_stack_p8, v_stack_m80, (uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)(local_r12)));
    if (((uint32_t)(result)) != ((uint32_t)(local_r14))) goto loc_003842D1;
loc_003841DF:
    local_rsi = (local_r15 * 8) + (v_stack_p10);
    result = ((uint32_t)(v_stack_p20)) << (3);
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFFEULL));
    local_r13 = (v_stack_p10) - (result);
loc_003841F7:
    if (local_r13 > local_rsi) goto loc_0038425F;
    result = MiReservePageFileSpaceForPage(v_stack_p8, local_r13, (uint32_t)((uint32_t)(local_rdi)), v_stack_m80);
    if ((uint32_t)(result) == 0) goto loc_00384385;
loc_0038421A:
    if (*(uint64_t *)(v_rip + 0xAA9A5F) == 0) goto loc_00384239;
    if ((((uint8_t)(v_stack_m80)) & (16)) == 0) {
        Arg2 = *(uint64_t *)(v_rip + 0xAA9A5F);
        Arg2 = ~(Arg2);
        Arg2 = (Arg2) & (v_stack_m80);
    }
    Arg2 = (Arg2) >> (32);
    Arg2 = (Arg2) + 1;
    result = MiUpdatePageFileHighInPte(v_stack_m80, Arg2, (uint32_t)((uint32_t)(local_rdi)), v_stack_m80);
    local_r13 = (local_r13) + (8);
    v_stack_m80 = result;
    goto loc_003841F7;
loc_00384256:
    if ((uint32_t)(local_r12) == 0) goto loc_0038437A;
loc_0038425F:
    if (v_stack_m88 == 0) goto loc_00383F29;
    if (v_stack_m60 != 0) {
        Arg2 = v_stack_m48;
        result = MiUnlockProtoPoolPage(v_stack_m60, Arg2, (uint32_t)((uint32_t)(local_rdi)), v_stack_m80);
    }
    Arg2 = 0;
    result = MiDecrementModifiedWriteCount(v_stack_m68, Arg2, (uint32_t)((uint32_t)(local_rdi)), v_stack_m80);
    if (result == 0) goto loc_00383F29;
    result = MiReleaseControlAreaWaiters(result, Arg2, (uint32_t)((uint32_t)(local_rdi)), v_stack_m80);
    goto loc_00383F29;
loc_0038429B:
    if (result != 0) goto loc_0038433D;
    goto loc_0038419C;
loc_003842B3:
    Arg1 = (local_r14) >> (9);
    Arg1 = (Arg1) & ((uint32_t)((uint32_t)(local_rdi)));
    goto loc_0038404D;
loc_003842C2:
    Arg1 = (Arg1) & (0);
    goto loc_00384090;
loc_003842D1:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) ^ (0));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFC00ULL));
    Arg1 = (uint32_t)((Arg1) ^ (0));
    if (0 == 0) goto loc_0038425F;
    local_r14 = (uint32_t)((v_stack_m80 + Arg1 * 8) - (0));
    local_r15 = (uint32_t)((local_r15) - ((uint32_t)(local_r14)));
    goto loc_003841DF;
loc_00384303:
    local_r15 = (local_r13) & (0xFFFFFFFFFFFFF000ULL);
    goto loc_00384090;
loc_00384319:
    local_r14 = (local_r15 + 4088) - (local_r13);
    Arg1 = (local_r13) - (local_r15);
    local_r14 = (local_r14) >> (3);
    Arg1 = (Arg1) >> (3);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) - ((uint32_t)(local_rdi)));
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)(result)));
loc_0038433D:
    result = ~(*(uint64_t *)(v_rip + 0xAA993C));
    result = (result) & (Arg1);
loc_0038436A:
    goto loc_003841B4;
loc_0038437A:
    goto loc_003841BE;
loc_00384385:
    result = MiReleasePageFileInfo(v_stack_p8, v_stack_p8, 1, v_stack_m80);
    goto loc_0038421A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x398` | `32` | `R` |
| `Arg2` | `- 0x8` | `64` | `R` |
| `Arg2` | `+ 0xFF8` | `64` | `R` |
| `Arg3` | `+ 0xB8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00383ED8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
