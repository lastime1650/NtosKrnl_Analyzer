# KiTransitionSchedulingGroupGeneration

- RVA: `0x003094C8`–`0x003099A6` (길이 `1,246` bytes)
- VA: `0x00000001403094C8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00073B74`
- 디코드: `298`개 명령, `1,246/1,246` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x0030967D` → [KiMoveScbThreadsToNewReadylist](KiMoveScbThreadsToNewReadylist_function_003099AC.md) (function, `0x003099AC`)
- `0x00309717` → [KeInterlockedClearProcessorAffinityEx](../35/KeInterlockedClearProcessorAffinityEx_function_003524F0.md) (function, `0x003524F0`)
- `0x003097E0` → [RtlGetInterruptTimePrecise](../20/RtlGetInterruptTimePrecise_function_0020A4C0.md) (function, `0x0020A4C0`)
- `0x0030980A` → [KiSetClockTimer](../39/KiSetClockTimer_function_0039DB2C.md) (function, `0x0039DB2C`)
- `0x00309821` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00309864` → [KiInsertNonMaxOverQuotaScb](../20/KiInsertNonMaxOverQuotaScb_function_00201374.md) (function, `0x00201374`)
- `0x003098F6` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00309909` → [KiQueryEffectivePriorityThread](../25/KiQueryEffectivePriorityThread_function_00257BA0.md) (function, `0x00257BA0`)
- `0x00309921` → [KiSetSchedulerAssistPriority](../46/KiSetSchedulerAssistPriority_function_0046E740.md) (function, `0x0046E740`)
- `0x0030995A` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)

### Direct callers
- [KiGroupSchedulingGenerationEnd](KiGroupSchedulingGenerationEnd_function_0030A9B4.md) at `0x0030AA18`
- [KiParkCurrentProcessor](../35/KiParkCurrentProcessor_function_003533A4.md) at `0x00353544`

### Static image references
- `0x00309507` → RVA `0x00F23150` (`.data`; read)
- `0x0030950E` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x00309518` → RVA `0x00FC6A85` (`ALMOSTRO`; read)
- `0x00309694` → RVA `0x00FC6B14` (`ALMOSTRO`; read)
- `0x00309709` → RVA `0x00E0AFD0` (`.data`; read)
- `0x0030971E` → RVA `0x00FC6DB8` (`ALMOSTRO`; read)
- `0x00309747` → RVA `0x00FC529C` (`ALMOSTRO`; read)
- `0x003097C5` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003097D2` → RVA `0x00FC6AA5` (`ALMOSTRO`; read)
- `0x00309918` → RVA `0x00FC504C` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00309979` → [sub_006E0BC0](../6E/Unknown_function_006E0BC0.md) (`tail-transfer`)
  - `0x003099A1` → [sub_006E0BC0](../6E/Unknown_function_006E0BC0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003094C8  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
003094CD  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
003094D2  53                              push rbx
003094D3  55                              push rbp
003094D4  56                              push rsi
003094D5  57                              push rdi
003094D6  41 54                           push r12
003094D8  41 55                           push r13
003094DA  41 56                           push r14
003094DC  41 57                           push r15
003094DE  48 83 EC 58                     sub rsp, 0x58
003094E2  45 33 DB                        xor r11d, r11d
003094E5  48 8B F1                        mov rsi, rcx
003094E8  48 8B 89 D8 8B 00 00            mov rcx, qword ptr [rcx + 0x8bd8]
003094EF  4D 8B D0                        mov r10, r8
003094F2  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
003094F7  41 8D 5B 01                     lea ebx, [r11 + 1]
003094FB  44 8B EB                        mov r13d, ebx
003094FE  4C 3B C1                        cmp r8, rcx
00309501  0F 87 17 02 00 00               ja 0x14030971e
00309507  48 8B 0D 42 9C C1 00            mov rcx, qword ptr [rip + 0xc19c42]
0030950E  8B 3D 8C D5 CB 00               mov edi, dword ptr [rip + 0xcbd58c]
00309514  48 0F AF F9                     imul rdi, rcx
00309518  44 38 1D 66 D5 CB 00            cmp byte ptr [rip + 0xcbd566], r11b
0030951F  48 89 8E D8 8B 00 00            mov qword ptr [rsi + 0x8bd8], rcx
00309526  0F 85 8C 02 00 00               jne 0x1403097b8
0030952C  4C 39 9E 30 84 00 00            cmp qword ptr [rsi + 0x8430], r11
00309533  0F 85 82 03 00 00               jne 0x1403098bb
00309539  48 8B 6E 10                     mov rbp, qword ptr [rsi + 0x10]
0030953D  44 88 9C 24 A8 00 00 00         mov byte ptr [rsp + 0xa8], r11b
00309545  48 85 ED                        test rbp, rbp
00309548  0F 84 A6 01 00 00               je 0x1403096f4
0030954E  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
00309552  48 85 C0                        test rax, rax
00309555  0F 84 E4 01 00 00               je 0x14030973f
0030955B  44 8B A6 D8 00 00 00            mov r12d, dword ptr [rsi + 0xd8]
00309562  4C 03 E0                        add r12, rax
00309565  4C 8D BE 88 8A 00 00            lea r15, [rsi + 0x8a88]
0030956C  4D 8B 37                        mov r14, qword ptr [r15]
0030956F  4D 3B F7                        cmp r14, r15
00309572  0F 84 85 01 00 00               je 0x1403096fd
00309578  41 8B CD                        mov ecx, r13d
0030957B  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00309580  49 8D 7E B8                     lea rdi, [r14 - 0x48]
00309584  8B 47 7C                        mov eax, dword ptr [rdi + 0x7c]
00309587  89 84 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], eax
0030958E  0F B7 47 70                     movzx eax, word ptr [rdi + 0x70]
00309592  66 83 E0 02                     and ax, 2
00309596  66 89 84 24 A0 00 00 00         mov word ptr [rsp + 0xa0], ax
0030959E  41 83 FD 40                     cmp r13d, 0x40
003095A2  0F 83 CE 01 00 00               jae 0x140309776
003095A8  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
003095AC  48 D3 E2                        shl rdx, cl
003095AF  48 8B CA                        mov rcx, rdx
003095B2  48 0B CB                        or rcx, rbx
003095B5  48 8B DF                        mov rbx, rdi
003095B8  F6 47 70 04                     test byte ptr [rdi + 0x70], 4
003095BC  48 0F 44 CA                     cmove rcx, rdx
003095C0  48 89 4F 30                     mov qword ptr [rdi + 0x30], rcx
003095C4  8B 86 D8 00 00 00               mov eax, dword ptr [rsi + 0xd8]
003095CA  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
003095CE  48 2B D8                        sub rbx, rax
003095D1  48 8B 07                        mov rax, qword ptr [rdi]
003095D4  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
003095D8  48 2B C8                        sub rcx, rax
003095DB  F0 48 01 4B 30                  lock add qword ptr [rbx + 0x30], rcx
003095E0  4C 39 5B 20                     cmp qword ptr [rbx + 0x20], r11
003095E4  0F 8F 46 03 00 00               jg 0x140309930
003095EA  45 84 C9                        test r9b, r9b
003095ED  0F 84 8B 01 00 00               je 0x14030977e
003095F3  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003095F7  48 39 47 08                     cmp qword ptr [rdi + 8], rax
003095FB  0F 85 46 01 00 00               jne 0x140309747
00309601  48 8B 97 80 00 00 00            mov rdx, qword ptr [rdi + 0x80]
00309608  BB 01 00 00 00                  mov ebx, 1
0030960D  4C 89 1F                        mov qword ptr [rdi], r11
00309610  4C 89 5F 28                     mov qword ptr [rdi + 0x28], r11
00309614  48 85 D2                        test rdx, rdx
00309617  0F 85 AE 00 00 00               jne 0x1403096cb
0030961D  0F B7 4F 70                     movzx ecx, word ptr [rdi + 0x70]
00309621  0F 57 C0                        xorps xmm0, xmm0
00309624  4C 89 5F 18                     mov qword ptr [rdi + 0x18], r11
00309628  8B C1                           mov eax, ecx
0030962A  C1 E8 03                        shr eax, 3
0030962D  23 C3                           and eax, ebx
0030962F  89 47 7C                        mov dword ptr [rdi + 0x7c], eax
00309632  B8 FC FF 00 00                  mov eax, 0xfffc
00309637  66 23 C8                        and cx, ax
0030963A  33 C0                           xor eax, eax
0030963C  66 89 4F 70                     mov word ptr [rdi + 0x70], cx
00309640  0F 11 47 58                     movups xmmword ptr [rdi + 0x58], xmm0
00309644  48 89 47 68                     mov qword ptr [rdi + 0x68], rax
00309648  4C 89 9F 90 01 00 00            mov qword ptr [rdi + 0x190], r11
0030964F  4C 89 9F 98 01 00 00            mov qword ptr [rdi + 0x198], r11
00309656  44 39 5F 7C                     cmp dword ptr [rdi + 0x7c], r11d
0030965A  0F 85 E7 01 00 00               jne 0x140309847
00309660  B8 FB FF 00 00                  mov eax, 0xfffb
00309665  66 21 47 70                     and word ptr [rdi + 0x70], ax
00309669  49 3B FC                        cmp rdi, r12
0030966C  0F 84 10 02 00 00               je 0x140309882
00309672  45 33 C9                        xor r9d, r9d
00309675  4C 8B C6                        mov r8, rsi
00309678  33 D2                           xor edx, edx
0030967A  48 8B CF                        mov rcx, rdi
0030967D  E8 2A 03 00 00                  call 0x1403099ac
00309682  44 8A 8C 24 B8 00 00 00         mov r9b, byte ptr [rsp + 0xb8]
0030968A  45 33 DB                        xor r11d, r11d
0030968D  8A 94 24 A8 00 00 00            mov dl, byte ptr [rsp + 0xa8]
00309694  F7 05 76 D4 CB 00 00 40 00 00   test dword ptr [rip + 0xcbd476], 0x4000
0030969E  0F 85 CB 02 00 00               jne 0x14030996f
003096A4  4D 8B 36                        mov r14, qword ptr [r14]
003096A7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
003096AC  4D 3B F7                        cmp r14, r15
003096AF  0F 85 CB FE FF FF               jne 0x140309580
003096B5  84 D2                           test dl, dl
003096B7  74 44                           je 0x1403096fd
003096B9  48 83 C4 58                     add rsp, 0x58
003096BD  41 5F                           pop r15
003096BF  41 5E                           pop r14
003096C1  41 5D                           pop r13
003096C3  41 5C                           pop r12
003096C5  5F                              pop rdi
003096C6  5E                              pop rsi
003096C7  5D                              pop rbp
003096C8  5B                              pop rbx
003096C9  C3                              ret
003096CA  CC                              int3
003096CB  0F B7 4F 70                     movzx ecx, word ptr [rdi + 0x70]
003096CF  C1 E9 03                        shr ecx, 3
003096D2  23 CB                           and ecx, ebx
003096D4  2B 4F 7C                        sub ecx, dword ptr [rdi + 0x7c]
003096D7  8B C1                           mov eax, ecx
003096D9  F0 0F C1 02                     lock xadd dword ptr [rdx], eax
003096DD  03 C1                           add eax, ecx
003096DF  0F 89 38 FF FF FF               jns 0x14030961d
003096E5  48 8B 87 80 00 00 00            mov rax, qword ptr [rdi + 0x80]
003096EC  44 89 18                        mov dword ptr [rax], r11d
003096EF  E9 29 FF FF FF                  jmp 0x14030961d
003096F4  48 8B 6E 08                     mov rbp, qword ptr [rsi + 8]
003096F8  E9 51 FE FF FF                  jmp 0x14030954e
003096FD  44 38 9E 59 86 00 00            cmp byte ptr [rsi + 0x8659], r11b
00309704  74 B3                           je 0x1403096b9
00309706  8B 56 24                        mov edx, dword ptr [rsi + 0x24]
00309709  48 8D 0D C0 18 B0 00            lea rcx, [rip + 0xb018c0]
00309710  44 88 9E 59 86 00 00            mov byte ptr [rsi + 0x8659], r11b
00309717  E8 D4 8D 04 00                  call 0x1403524f0
0030971C  EB 9B                           jmp 0x1403096b9
0030971E  44 8B 05 93 D6 CB 00            mov r8d, dword ptr [rip + 0xcbd693]
00309725  33 D2                           xor edx, edx
00309727  41 8B C0                        mov eax, r8d
0030972A  48 2B C1                        sub rax, rcx
0030972D  48 FF C8                        dec rax
00309730  49 03 C2                        add rax, r10
00309733  49 F7 F0                        div r8
00309736  44 8D 2C 03                     lea r13d, [rbx + rax]
0030973A  E9 C8 FD FF FF                  jmp 0x140309507
0030973F  4D 8B E3                        mov r12, r11
00309742  E9 1E FE FF FF                  jmp 0x140309565
00309747  8B 15 4F BB CB 00               mov edx, dword ptr [rip + 0xcbbb4f]
0030974D  41 B8 00 04 00 00               mov r8d, 0x400
00309753  48 8B 0F                        mov rcx, qword ptr [rdi]
00309756  44 2B C2                        sub r8d, edx
00309759  4C 0F AF 47 20                  imul r8, qword ptr [rdi + 0x20]
0030975E  48 C1 E9 0A                     shr rcx, 0xa
00309762  48 0F AF CA                     imul rcx, rdx
00309766  49 C1 E8 0A                     shr r8, 0xa
0030976A  4C 03 C1                        add r8, rcx
0030976D  4C 89 47 20                     mov qword ptr [rdi + 0x20], r8
00309771  E9 8B FE FF FF                  jmp 0x140309601
00309776  49 8B D3                        mov rdx, r11
00309779  E9 31 FE FF FF                  jmp 0x1403095af
0030977E  44 38 5E 21                     cmp byte ptr [rsi + 0x21], r11b
00309782  0F 84 6B FE FF FF               je 0x1403095f3
00309788  F6 47 70 10                     test byte ptr [rdi + 0x70], 0x10
0030978C  0F 85 61 FE FF FF               jne 0x1403095f3
00309792  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
00309796  48 8B C1                        mov rax, rcx
00309799  F0 48 0F C1 43 30               lock xadd qword ptr [rbx + 0x30], rax
0030979F  48 03 C8                        add rcx, rax
003097A2  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
003097A6  48 3B C8                        cmp rcx, rax
003097A9  0F 8E 44 FE FF FF               jle 0x1403095f3
003097AF  48 87 43 30                     xchg qword ptr [rbx + 0x30], rax
003097B3  E9 3B FE FF FF                  jmp 0x1403095f3
003097B8  44 0F 20 C3                     mov rbx, cr8
003097BC  BA 0F 00 00 00                  mov edx, 0xf
003097C1  44 0F 22 C2                     mov cr8, rdx
003097C5  44 39 1D 54 D5 CB 00            cmp dword ptr [rip + 0xcbd554], r11d
003097CC  0F 85 22 01 00 00               jne 0x1403098f4
003097D2  44 38 1D CC D2 CB 00            cmp byte ptr [rip + 0xcbd2cc], r11b
003097D9  74 67                           je 0x140309842
003097DB  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
003097E0  E8 DB 0C F0 FF                  call 0x14020a4c0
003097E5  45 33 DB                        xor r11d, r11d
003097E8  44 8B 0D B1 D2 CB 00            mov r9d, dword ptr [rip + 0xcbd2b1]
003097EF  4C 8B C7                        mov r8, rdi
003097F2  44 88 5C 24 30                  mov byte ptr [rsp + 0x30], r11b
003097F7  48 8B D0                        mov rdx, rax
003097FA  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
003097FF  48 8B CE                        mov rcx, rsi
00309802  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
0030980A  E8 1D 43 09 00                  call 0x14039db2c
0030980F  45 33 DB                        xor r11d, r11d
00309812  44 39 1D 07 D5 CB 00            cmp dword ptr [rip + 0xcbd507], r11d
00309819  74 0E                           je 0x140309829
0030981B  44 0F 20 C1                     mov rcx, cr8
0030981F  8A D3                           mov dl, bl
00309821  E8 72 BE 1E 00                  call 0x1404f5698
00309826  45 33 DB                        xor r11d, r11d
00309829  0F B6 C3                        movzx eax, bl
0030982C  44 0F 22 C0                     mov cr8, rax
00309830  44 8A 8C 24 B8 00 00 00         mov r9b, byte ptr [rsp + 0xb8]
00309838  BB 01 00 00 00                  mov ebx, 1
0030983D  E9 EA FC FF FF                  jmp 0x14030952c
00309842  49 8B C3                        mov rax, r11
00309845  EB A1                           jmp 0x1403097e8
00309847  45 84 C9                        test r9b, r9b
0030984A  0F 85 22 FE FF FF               jne 0x140309672
00309850  66 44 39 5F 78                  cmp word ptr [rdi + 0x78], r11w
00309855  0F 84 32 FE FF FF               je 0x14030968d
0030985B  45 33 C0                        xor r8d, r8d
0030985E  48 8B D6                        mov rdx, rsi
00309861  48 8B CF                        mov rcx, rdi
00309864  E8 0B 7B EF FF                  call 0x140201374
00309869  44 8A 8C 24 B8 00 00 00         mov r9b, byte ptr [rsp + 0xb8]
00309871  8A D3                           mov dl, bl
00309873  45 33 DB                        xor r11d, r11d
00309876  88 9C 24 A8 00 00 00            mov byte ptr [rsp + 0xa8], bl
0030987D  E9 12 FE FF FF                  jmp 0x140309694
00309882  F6 45 02 04                     test byte ptr [rbp + 2], 4
00309886  4C 8B 7E 38                     mov r15, qword ptr [rsi + 0x38]
0030988A  41 8A 1F                        mov bl, byte ptr [r15]
0030988D  75 74                           jne 0x140309903
0030988F  8A C3                           mov al, bl
00309891  32 85 C3 00 00 00               xor al, byte ptr [rbp + 0xc3]
00309897  24 7F                           and al, 0x7f
00309899  32 C3                           xor al, bl
0030989B  41 88 07                        mov byte ptr [r15], al
0030989E  48 8B 8E B8 8E 00 00            mov rcx, qword ptr [rsi + 0x8eb8]
003098A5  48 85 C9                        test rcx, rcx
003098A8  75 68                           jne 0x140309912
003098AA  BB 01 00 00 00                  mov ebx, 1
003098AF  4C 8D BE 88 8A 00 00            lea r15, [rsi + 0x8a88]
003098B6  E9 B7 FD FF FF                  jmp 0x140309672
003098BB  4C 89 9E 30 84 00 00            mov qword ptr [rsi + 0x8430], r11
003098C2  4C 89 9E 38 84 00 00            mov qword ptr [rsi + 0x8438], r11
003098C9  44 39 9E 74 86 00 00            cmp dword ptr [rsi + 0x8674], r11d
003098D0  0F 85 63 FC FF FF               jne 0x140309539
003098D6  48 8B 8E C8 00 00 00            mov rcx, qword ptr [rsi + 0xc8]
003098DD  48 8B 86 C0 00 00 00            mov rax, qword ptr [rsi + 0xc0]
003098E4  48 F7 D1                        not rcx
003098E7  F0 48 21 88 80 01 00 00         lock and qword ptr [rax + 0x180], rcx
003098EF  E9 45 FC FF FF                  jmp 0x140309539
003098F4  8A CB                           mov cl, bl
003098F6  E8 01 BE 1E 00                  call 0x1404f56fc
003098FB  45 33 DB                        xor r11d, r11d
003098FE  E9 CF FE FF FF                  jmp 0x1403097d2
00309903  48 8B D6                        mov rdx, rsi
00309906  48 8B CD                        mov rcx, rbp
00309909  E8 92 E2 F4 FF                  call 0x140257ba0
0030990E  32 C3                           xor al, bl
00309910  EB 85                           jmp 0x140309897
00309912  48 3B 6E 18                     cmp rbp, qword ptr [rsi + 0x18]
00309916  75 10                           jne 0x140309928
00309918  8B 15 2E B7 CB 00               mov edx, dword ptr [rip + 0xcbb72e]
0030991E  45 33 C0                        xor r8d, r8d
00309921  E8 1A 4E 16 00                  call 0x14046e740
00309926  EB 82                           jmp 0x1403098aa
00309928  0F B6 D0                        movzx edx, al
0030992B  83 E2 7F                        and edx, 0x7f
0030992E  EB EE                           jmp 0x14030991e
00309930  48 8B C1                        mov rax, rcx
00309933  F0 48 0F C1 43 20               lock xadd qword ptr [rbx + 0x20], rax
00309939  48 03 C1                        add rax, rcx
0030993C  48 85 C0                        test rax, rax
0030993F  0F 8F A5 FC FF FF               jg 0x1403095ea
00309945  49 8B CB                        mov rcx, r11
00309948  48 87 4B 48                     xchg qword ptr [rbx + 0x48], rcx
0030994C  48 85 C9                        test rcx, rcx
0030994F  0F 84 95 FC FF FF               je 0x1403095ea
00309955  45 33 C0                        xor r8d, r8d
00309958  33 D2                           xor edx, edx
0030995A  E8 F1 E2 EF FF                  call 0x140207c50
0030995F  44 8A 8C 24 B8 00 00 00         mov r9b, byte ptr [rsp + 0xb8]
00309967  45 33 DB                        xor r11d, r11d
0030996A  E9 7B FC FF FF                  jmp 0x1403095ea
0030996F  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00309976  3B 47 7C                        cmp eax, dword ptr [rdi + 0x7c]
00309979  0F 85 41 72 3D 00               jne 0x1406e0bc0
0030997F  66 44 39 9C 24 A0 00 00 00      cmp word ptr [rsp + 0xa0], r11w
00309988  41 8B CB                        mov ecx, r11d
0030998B  0F B7 47 70                     movzx eax, word ptr [rdi + 0x70]
0030998F  0F 95 C1                        setne cl
00309992  66 D1 E8                        shr ax, 1
00309995  66 23 C3                        and ax, bx
00309998  66 3B C8                        cmp cx, ax
0030999B  0F 84 03 FD FF FF               je 0x1403096a4
003099A1  E9 1A 72 3D 00                  jmp 0x1406e0bc0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiTransitionSchedulingGroupGeneration(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int16 v_stack_p8;
    unsigned __int16 v_stack_pA0;
    unsigned __int8 v_stack_pA8;
    unsigned int v_stack_pB0;
    unsigned __int8 v_stack_pB8;

    v_stack_p20 = (unsigned __int8)(a4);
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (88);
    v_r11 = 0;
    v_stack_m58 = 0;
    if (a3 > (*(unsigned __int64 *)(a1 + 35800))) goto loc_0030971E;
loc_00309507:
    v_rdi = ((unsigned int)(*(unsigned int *)(v_rip + 13358476))) * (*(unsigned __int64 *)(v_rip + 12688450));
    *(unsigned __int64 *)(a1 + 35800) = *(unsigned __int64 *)(v_rip + 12688450);
    if ((*(unsigned __int8 *)(v_rip + 13358438)) != 0) goto loc_003097B8;
loc_0030952C:
    if ((*(unsigned __int64 *)(a1 + 33840)) != 0) goto loc_003098BB;
loc_00309539:
    v_stack_p10 = 0;
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_003096F4;
loc_0030954E:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 104) == 0) goto loc_0030973F;
    v_r12 = ((unsigned int)(*(unsigned int *)(a1 + 216))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 104));
loc_00309565:
    if ((*(unsigned __int64 *)(a1 + 35464)) == (a1 + 35464)) goto loc_003096FD;
    v_stack_m50 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r11 + 1))));
loc_00309580:
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 124)));
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 112)) & (2));
    v_stack_p8 = (unsigned __int16)(result);
    if (((unsigned int)((unsigned int)((unsigned int)(v_r11 + 1)))) >= 64) goto loc_00309776;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 48)) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r11 + 1))))));
loc_003095AF:
    a1 = (a2) | (v_r11 + 1);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 112)) & (4)) == 0) { a1 = a2; }
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 48) = a1;
    v_rbx = (*(unsigned __int64 *)(a1 + 35464) - 72) - ((unsigned int)(*(unsigned int *)(a1 + 216)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 40)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72));
    if ((*(unsigned __int64 *)(v_rbx + 32)) > 0) goto loc_00309930;
loc_003095EA:
    if ((unsigned __int8)(a4) == 0) goto loc_0030977E;
loc_003095F3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 16))) goto loc_00309747;
loc_00309601:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 40) = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 128) != 0) goto loc_003096CB;
loc_0030961D:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 24) = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 112)))) >> (3));
    result = (unsigned int)((result) & (1));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 124) = (unsigned int)(result);
    a1 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 112)) & ((unsigned __int16)((unsigned int)(0xFFFCULL))));
    result = 0;
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 112) = (unsigned __int16)(a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 88) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 104) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 400) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 408) = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 124)) != 0) goto loc_00309847;
    if ((*(unsigned __int64 *)(a1 + 35464) - 72) == v_r12) goto loc_00309882;
loc_00309672:
    a4 = 0;
    a2 = 0;
    result = KiMoveScbThreadsToNewReadylist(*(unsigned __int64 *)(a1 + 35464) - 72, a2, a1, a4);
    v_r11 = 0;
loc_0030968D:
loc_00309694:
    if (((*(unsigned int *)(v_rip + 13358198)) & (0x4000ULL)) != 0) goto loc_0030996F;
loc_003096A4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464))) != (a1 + 35464)) goto loc_00309580;
    if ((unsigned __int8)(v_stack_p10) == 0) goto loc_003096FD;
loc_003096B9:
    v_rsp = (v_rsp) + (88);
    return result;
loc_003096CB:
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 112)) >> (3));
    a1 = (unsigned int)((a1) & (1));
    a1 = (unsigned int)((a1) - (*(unsigned int *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 124)));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) + ((unsigned int)(a1)));
    if (!sign_flag) goto loc_0030961D;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 128)) = 0;
    goto loc_0030961D;
loc_003096F4:
    goto loc_0030954E;
loc_003096FD:
    if ((*(unsigned __int8 *)(a1 + 34393)) == 0) goto loc_003096B9;
    *(unsigned __int8 *)(a1 + 34393) = 0;
    result = KeInterlockedClearProcessorAffinityEx(v_rip + 11540672, (unsigned int)(*(unsigned int *)(a1 + 36)), a1, v_stack_p20);
    goto loc_003096B9;
loc_0030971E:
    a2 = 0;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13358739))))) - (v_rip + 11540672);
    result = (result) - 1;
    result = (result) + (a3);
    goto loc_00309507;
loc_0030973F:
    goto loc_00309565;
loc_00309747:
    a3 = (unsigned int)(((unsigned int)(0x400ULL)) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13351759)))));
    a3 = (a3) * (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 32));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72)) >> (10);
    a1 = (a1) * ((unsigned int)(*(unsigned int *)(v_rip + 13351759)));
    a3 = (a3) >> (10);
    a3 = (a3) + (a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 32) = a3;
    goto loc_00309601;
loc_00309776:
    goto loc_003095AF;
loc_0030977E:
    if ((*(unsigned __int8 *)(a1 + 33)) == 0) goto loc_003095F3;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 112)) & (16)) != 0) goto loc_003095F3;
    a1 = (*(unsigned __int64 *)(1 + 40)) + (*(unsigned __int64 *)(1 + 40));
    if (a1 <= (*(unsigned __int64 *)(1 + 40))) goto loc_003095F3;
    goto loc_003095F3;
loc_003097B8:
    if ((*(unsigned int *)(v_rip + 13358420)) != 0) goto loc_003098F4;
loc_003097D2:
    if ((*(unsigned __int8 *)(v_rip + 13357772)) == 0) goto loc_00309842;
    result = RtlGetInterruptTimePrecise(v_stack_p40, 15, a3, v_stack_p20);
    v_r11 = 0;
loc_003097E8:
    v_stack_p30 = 0;
    v_stack_p28 = 1;
    v_stack_p20 = 4;
    result = KiSetClockTimer(a1, result, *(unsigned __int64 *)(a1 + 35464) - 72, (unsigned int)(*(unsigned int *)(v_rip + 13357745)));
    v_r11 = 0;
    if ((*(unsigned int *)(v_rip + 13358343)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(a1 + 35464) - 72, (unsigned int)(*(unsigned int *)(v_rip + 13357745)));
        v_r11 = 0;
    }
    goto loc_0030952C;
loc_00309842:
    goto loc_003097E8;
loc_00309847:
    if ((unsigned __int8)(v_stack_pB8) != 0) goto loc_00309672;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 120)) == 0) goto loc_0030968D;
    a3 = 0;
    result = KiInsertNonMaxOverQuotaScb(*(unsigned __int64 *)(a1 + 35464) - 72, a1, a3, v_stack_pB8);
    v_r11 = 0;
    v_stack_pA8 = 1;
    goto loc_00309694;
loc_00309882:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 2)) & (4)) != 0) goto loc_00309903;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 56)))) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 195)));
loc_00309897:
    result = (unsigned __int8)((result) & (127));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 56)))));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 56)) = (unsigned __int8)(result);
    if (*(unsigned __int64 *)(a1 + 36536) != 0) goto loc_00309912;
loc_003098AA:
    goto loc_00309672;
loc_003098BB:
    *(unsigned __int64 *)(a1 + 33840) = 0;
    *(unsigned __int64 *)(a1 + 33848) = 0;
    if ((*(unsigned int *)(a1 + 34420)) != 0) goto loc_00309539;
    a1 = ~(*(unsigned __int64 *)(a1 + 200));
    goto loc_00309539;
loc_003098F4:
    result = KiRaiseIrqlProcessIrqlFlags(1, 1, a3, v_stack_pB8);
    v_r11 = 0;
    goto loc_003097D2;
loc_00309903:
    result = KiQueryEffectivePriorityThread(*(unsigned __int64 *)(a1 + 8), a1, a3, v_stack_pB8);
    result = (unsigned __int8)((result) ^ (1));
    goto loc_00309897;
loc_00309912:
    if ((*(unsigned __int64 *)(a1 + 8)) != (*(unsigned __int64 *)(a1 + 24))) goto loc_00309928;
loc_0030991E:
    a3 = 0;
    result = KiSetSchedulerAssistPriority(*(unsigned __int64 *)(a1 + 8), (unsigned int)(*(unsigned int *)(v_rip + 13350702)), a3, v_stack_pB8);
    goto loc_003098AA;
loc_00309928:
    a2 = (unsigned int)(((unsigned __int8)(result)) & (127));
    goto loc_0030991E;
loc_00309930:
    result = (*(unsigned __int64 *)(a1 + 8)) + (*(unsigned __int64 *)(a1 + 8));
    if (condition_is_greater) goto loc_003095EA;
    if (0 == 0) goto loc_003095EA;
    a3 = 0;
    a2 = 0;
    result = KeInsertQueueDpc(0, a2, a3, v_stack_pB8);
    v_r11 = 0;
    goto loc_003095EA;
loc_0030996F:
    a1 = (v_stack_pA0 != 0) ? 1 : 0;
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 35464) - 72 + 112)) >> (1));
    result = (unsigned __int16)((result) & (1));
    if (((unsigned __int16)(a1)) == ((unsigned __int16)(result))) goto loc_003096A4;
}
```

## 5. (Beta) C Style

```c
int64_t KiTransitionSchedulingGroupGeneration(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint8_t v_stack_p20;
    uint8_t v_stack_p28;
    uint8_t v_stack_p30;
    uint64_t v_stack_p40;
    uint16_t v_stack_p8;
    uint16_t v_stack_pA0;
    uint8_t v_stack_pA8;
    uint32_t v_stack_pB0;
    uint8_t v_stack_pB8;

    v_stack_p20 = (uint8_t)(Arg4);
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (88);
    local_r11 = 0;
    v_stack_m58 = 0;
    if (Arg3 > (*(uint64_t *)(arg1 + 0x8BD8))) goto loc_0030971E;
loc_00309507:
    local_rdi = ((uint32_t)(*(uint32_t *)(v_rip + 0xCBD58C))) * (*(uint64_t *)(v_rip + 0xC19C42));
    *(uint64_t *)(arg1 + 0x8BD8) = *(uint64_t *)(v_rip + 0xC19C42);
    if ((*(uint8_t *)(v_rip + 0xCBD566)) != 0) goto loc_003097B8;
loc_0030952C:
    if ((*(uint64_t *)(arg1 + 0x8430)) != 0) goto loc_003098BB;
loc_00309539:
    v_stack_p10 = 0;
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_003096F4;
loc_0030954E:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x68) == 0) goto loc_0030973F;
    local_r12 = ((uint32_t)(*(uint32_t *)(arg1 + 0xD8))) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x68));
loc_00309565:
    if ((*(uint64_t *)(arg1 + 0x8A88)) == (Arg1 + 35464)) goto loc_003096FD;
    v_stack_m50 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r11 + 1))));
loc_00309580:
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x7C)));
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x70)) & (2));
    v_stack_p8 = (uint16_t)(result);
    if (((uint32_t)((uint32_t)((uint32_t)(local_r11 + 1)))) >= 64) goto loc_00309776;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x30)) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r11 + 1))))));
loc_003095AF:
    Arg1 = (Arg2) | (local_r11 + 1);
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x70)) & (4)) == 0) { Arg1 = Arg2; }
    *(void **)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x30) = Arg1;
    local_rbx = (*(uint64_t *)(arg1 + 0x8A88) - 72) - ((uint32_t)(*(uint32_t *)(arg1 + 0xD8)));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x28) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x28)) - (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48));
    if ((*(uint64_t *)(local_rbx + 0x20)) > 0) goto loc_00309930;
loc_003095EA:
    if ((uint8_t)(Arg4) == 0) goto loc_0030977E;
loc_003095F3:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x8)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x10))) goto loc_00309747;
loc_00309601:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48) = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x28) = 0;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x80) != 0) goto loc_003096CB;
loc_0030961D:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x18) = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x70)))) >> (3));
    result = (uint32_t)((result) & (1));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x7C) = (uint32_t)(result);
    Arg1 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x70)) & ((uint16_t)((uint32_t)(0xFFFCULL))));
    result = 0;
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x70) = (uint16_t)(Arg1);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x58) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x68) = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x190) = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x198) = 0;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x7C)) != 0) goto loc_00309847;
    if ((*(uint64_t *)(arg1 + 0x8A88) - 72) == local_r12) goto loc_00309882;
loc_00309672:
    Arg4 = 0;
    Arg2 = 0;
    result = KiMoveScbThreadsToNewReadylist(*(uint64_t *)(arg1 + 0x8A88) - 72, Arg2, Arg1, Arg4);
    local_r11 = 0;
loc_0030968D:
loc_00309694:
    if (((*(uint32_t *)(v_rip + 0xCBD476)) & (0x4000ULL)) != 0) goto loc_0030996F;
loc_003096A4:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88))) != (Arg1 + 35464)) goto loc_00309580;
    if ((uint8_t)(v_stack_p10) == 0) goto loc_003096FD;
loc_003096B9:
    local_rsp = (local_rsp) + (88);
    return result;
loc_003096CB:
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x70)) >> (3));
    Arg1 = (uint32_t)((Arg1) & (1));
    Arg1 = (uint32_t)((Arg1) - (*(uint32_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x7C)));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) + ((uint32_t)(Arg1)));
    if (!sign_flag) goto loc_0030961D;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x80)) = 0;
    goto loc_0030961D;
loc_003096F4:
    goto loc_0030954E;
loc_003096FD:
    if ((*(uint8_t *)(arg1 + 0x8659)) == 0) goto loc_003096B9;
    *(uint8_t *)(arg1 + 0x8659) = 0;
    result = KeInterlockedClearProcessorAffinityEx(v_rip + 11540672, (uint32_t)(*(uint32_t *)(arg1 + 0x24)), Arg1, v_stack_p20);
    goto loc_003096B9;
loc_0030971E:
    Arg2 = 0;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCBD693))))) - (v_rip + 11540672);
    result = (result) - 1;
    result = (result) + (Arg3);
    goto loc_00309507;
loc_0030973F:
    goto loc_00309565;
loc_00309747:
    Arg3 = (uint32_t)(((uint32_t)(0x400ULL)) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCBBB4F)))));
    Arg3 = (Arg3) * (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x20));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48)) >> (10);
    Arg1 = (Arg1) * ((uint32_t)(*(uint32_t *)(v_rip + 0xCBBB4F)));
    Arg3 = (Arg3) >> (10);
    Arg3 = (Arg3) + (Arg1);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x20) = Arg3;
    goto loc_00309601;
loc_00309776:
    goto loc_003095AF;
loc_0030977E:
    if ((*(uint8_t *)(arg1 + 0x21)) == 0) goto loc_003095F3;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x70)) & (16)) != 0) goto loc_003095F3;
    Arg1 = (*(uint64_t *)(1 + 0x28)) + (*(uint64_t *)(1 + 0x28));
    if (Arg1 <= (*(uint64_t *)(1 + 0x28))) goto loc_003095F3;
    goto loc_003095F3;
loc_003097B8:
    if ((*(uint32_t *)(v_rip + 0xCBD554)) != 0) goto loc_003098F4;
loc_003097D2:
    if ((*(uint8_t *)(v_rip + 0xCBD2CC)) == 0) goto loc_00309842;
    result = RtlGetInterruptTimePrecise(v_stack_p40, 15, Arg3, v_stack_p20);
    local_r11 = 0;
loc_003097E8:
    v_stack_p30 = 0;
    v_stack_p28 = 1;
    v_stack_p20 = 4;
    result = KiSetClockTimer(Arg1, result, *(uint64_t *)(arg1 + 0x8A88) - 72, (uint32_t)(*(uint32_t *)(v_rip + 0xCBD2B1)));
    local_r11 = 0;
    if ((*(uint32_t *)(v_rip + 0xCBD507)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(arg1 + 0x8A88) - 72, (uint32_t)(*(uint32_t *)(v_rip + 0xCBD2B1)));
        local_r11 = 0;
    }
    goto loc_0030952C;
loc_00309842:
    goto loc_003097E8;
loc_00309847:
    if ((uint8_t)(v_stack_pB8) != 0) goto loc_00309672;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x78)) == 0) goto loc_0030968D;
    Arg3 = 0;
    result = KiInsertNonMaxOverQuotaScb(*(uint64_t *)(arg1 + 0x8A88) - 72, Arg1, Arg3, v_stack_pB8);
    local_r11 = 0;
    v_stack_pA8 = 1;
    goto loc_00309694;
loc_00309882:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x2)) & (4)) != 0) goto loc_00309903;
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x38)))) ^ (*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0xC3)));
loc_00309897:
    result = (uint8_t)((result) & (127));
    result = (uint8_t)((result) ^ ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x38)))));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x38)) = (uint8_t)(result);
    if (*(uint64_t *)(arg1 + 0x8EB8) != 0) goto loc_00309912;
loc_003098AA:
    goto loc_00309672;
loc_003098BB:
    *(uint64_t *)(arg1 + 0x8430) = 0;
    *(uint64_t *)(arg1 + 0x8438) = 0;
    if ((*(uint32_t *)(arg1 + 0x8674)) != 0) goto loc_00309539;
    Arg1 = ~(*(uint64_t *)(arg1 + 0xC8));
    goto loc_00309539;
loc_003098F4:
    result = KiRaiseIrqlProcessIrqlFlags(1, 1, Arg3, v_stack_pB8);
    local_r11 = 0;
    goto loc_003097D2;
loc_00309903:
    result = KiQueryEffectivePriorityThread(*(uint64_t *)(arg1 + 0x8), Arg1, Arg3, v_stack_pB8);
    result = (uint8_t)((result) ^ (1));
    goto loc_00309897;
loc_00309912:
    if ((*(uint64_t *)(arg1 + 0x8)) != (*(uint64_t *)(arg1 + 0x18))) goto loc_00309928;
loc_0030991E:
    Arg3 = 0;
    result = KiSetSchedulerAssistPriority(*(uint64_t *)(arg1 + 0x8), (uint32_t)(*(uint32_t *)(v_rip + 0xCBB72E)), Arg3, v_stack_pB8);
    goto loc_003098AA;
loc_00309928:
    Arg2 = (uint32_t)(((uint8_t)(result)) & (127));
    goto loc_0030991E;
loc_00309930:
    result = (*(uint64_t *)(arg1 + 0x8)) + (*(uint64_t *)(arg1 + 0x8));
    if (condition_is_greater) goto loc_003095EA;
    if (0 == 0) goto loc_003095EA;
    Arg3 = 0;
    Arg2 = 0;
    result = KeInsertQueueDpc(0, Arg2, Arg3, v_stack_pB8);
    local_r11 = 0;
    goto loc_003095EA;
loc_0030996F:
    Arg1 = (v_stack_pA0 != 0) ? 1 : 0;
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8A88) - 0x48 + 0x70)) >> (1));
    result = (uint16_t)((result) & (1));
    if (((uint16_t)(Arg1)) == ((uint16_t)(result))) goto loc_003096A4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x21` | `8` | `R` |
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0xC8` | `64` | `R` |
| `Arg1` | `+ 0xD8` | `32` | `R` |
| `Arg1` | `+ 0x8430` | `64` | `R` |
| `Arg1` | `+ 0x8430` | `64` | `W` |
| `Arg1` | `+ 0x8438` | `64` | `W` |
| `Arg1` | `+ 0x8659` | `8` | `R` |
| `Arg1` | `+ 0x8659` | `8` | `W` |
| `Arg1` | `+ 0x8674` | `32` | `R` |
| `Arg1` | `+ 0x8A88` | `64` | `R` |
| `Arg1` | `+ 0x8BD8` | `64` | `R` |
| `Arg1` | `+ 0x8BD8` | `64` | `W` |
| `Arg1` | `+ 0x8EB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003094C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
