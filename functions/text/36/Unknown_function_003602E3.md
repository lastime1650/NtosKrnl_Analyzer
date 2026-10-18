# sub_003602E3

- RVA: `0x003602E3`–`0x00360911` (길이 `1,582` bytes)
- VA: `0x00000001403602E3`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00079C74`
- 디코드: `367`개 명령, `1,582/1,582` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **17**

### Outgoing calls
- `0x00360378` → [ExpAcquireSpinLockSharedAtDpcLevelInstrumented](../27/ExpAcquireSpinLockSharedAtDpcLevelInstrumented_function_0027CD20.md) (function, `0x0027CD20`)
- `0x003603EC` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003605CC` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x00360678` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003606B7` → [ExpPoolTrackerReturnLimit](ExpPoolTrackerReturnLimit_function_00361570.md) (function, `0x00361570`)
- `0x00360710` → [RtlpHpVsContextFree](RtlpHpVsContextFree_function_00361630.md) (function, `0x00361630`)
- `0x003607A9` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x003607FB` → [ExpWaitForSpinLockSharedAndAcquire](ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x0036080C` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00360823` → [RtlpHpSegPageRangeShrink](../2E/RtlpHpSegPageRangeShrink_function_002E2FA0.md) (function, `0x002E2FA0`)
- `0x00360845` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x003608C2` → [RtlpHpEnvCompactionSchedule](../32/RtlpHpEnvCompactionSchedule_function_003264A0.md) (function, `0x003264A0`)
- `0x003608D4` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0036030A` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00360345` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00360352` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0036035F` → RVA `0x00F0DE58` (`.data`; read)
- `0x00360371` → RVA `0x00EFACF8` (`.data`; read)
- `0x0036037D` → RVA `0x00EFED38` (`.data`; read)
- `0x00360387` → RVA `0x00EFED30` (`.data`; read)
- `0x0036040D` → RVA `0x00FC7228` (`ALMOSTRO`; read)
- `0x00360424` → RVA `0x00EFED20` (`.data`; read)
- `0x003604E8` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x00360562` → RVA `0x00E27F80` (`.data`; read)
- `0x003605B6` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x00360639` → RVA `0x00FCF100` (`CACHEALI`; read/write)
- `0x00360655` → RVA `0x00EFACF8` (`.data`; read/write)
- `0x00360811` → RVA `0x00EFAD00` (`.data`; read)
- `0x00360862` → RVA `0x00EFED60` (`.data`; read)
- `0x003608B0` → RVA `0x00EFA7BC` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **38**
  - `0x003602EB` → [sub_0035FB85 + 0xBF](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x003602FB` → [sub_0035FB85 + 0x2C3](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360331` → [sub_00360968 + 0x863](Unknown_function_00360968.md) (`tail-transfer`)
  - `0x003603D3` → [sub_00360968 + 0x528](Unknown_function_00360968.md) (`tail-transfer`)
  - `0x00360414` → [sub_0035FB85 + 0x69](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x0036041E` → [sub_0035FB85 + 0x69](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x0036042C` → [sub_00360968 + 0x582](Unknown_function_00360968.md) (`tail-transfer`)
  - `0x00360453` → [sub_00360968 + 0x850](Unknown_function_00360968.md) (`tail-transfer`)
  - `0x003604CE` → [sub_00360968 + 0x447](Unknown_function_00360968.md) (`tail-transfer`)
  - `0x003604DB` → [sub_00360968 + 0x447](Unknown_function_00360968.md) (`tail-transfer`)
  - `0x00360558` → [sub_00360968](Unknown_function_00360968.md) (`tail-transfer`)
  - `0x00360596` → [sub_00360968 + 0x209](Unknown_function_00360968.md) (`tail-transfer`)
  - `0x003605E2` → [sub_00360968 + 0x353](Unknown_function_00360968.md) (`tail-transfer`)
  - `0x003605F7` → [sub_0035FB85 + 0x69](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x0036064F` → [sub_00360968 + 0x330](Unknown_function_00360968.md) (`tail-transfer`)
  - `0x0036068D` → [sub_00360968 + 0x6D](Unknown_function_00360968.md) (`tail-transfer`)
  - `0x003606A1` → [sub_0035FB85 + 0x12A](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x003606BC` → [sub_0035FB85 + 0x72D](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x003606E3` → [sub_0035FB85 + 0x650](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x003606F6` → [sub_0035FB85 + 0x650](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360717` → [sub_0035FB85 + 0x738](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x0036072B` → [sub_0035FB85 + 0x738](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x0036078F` → [sub_0035FB85 + 0x738](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x0036079C` → [sub_0035FB85 + 0x22D](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x003607AE` → [sub_0035FB85 + 0x241](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x003607C5` → [sub_0035FB85 + 0x5DC](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360818` → [sub_0035FB85 + 0x21C](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360828` → [sub_0035FB85 + 0x738](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x0036084A` → [sub_0035FB85 + 0x738](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x0036086E` → [sub_0035FB85 + 0x1D8](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360886` → [sub_0035FB85 + 0x1B7](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360890` → [sub_0035FB85 + 0x1B7](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x003608AA` → [sub_00360968 + 0x54](Unknown_function_00360968.md) (`tail-transfer`)
  - `0x003608B8` → [sub_0035FB85 + 0x53B](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x003608C7` → [sub_0035FB85 + 0x53B](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x003608EA` → [sub_0035FB85 + 0x713](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360902` → [sub_0035FB85 + 0x6F2](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x0036090C` → [sub_0035FB85 + 0x6F2](../35/Unknown_function_0035FB85.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003602E3  48 83 CA 01                     or rdx, 1
003602E7  48 89 55 97                     mov qword ptr [rbp - 0x69], rdx
003602EB  E9 54 F9 FF FF                  jmp 0x14035fc44
003602F0  45 8B CE                        mov r9d, r14d
003602F3  49 8D 50 20                     lea rdx, [r8 + 0x20]
003602F7  49 8D 40 30                     lea rax, [r8 + 0x30]
003602FB  E9 48 FB FF FF                  jmp 0x14035fe48
00360300  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
0036030A  48 8D 15 EF FC C9 FF            lea rdx, [rip - 0x360311]
00360311  4C 3B E0                        cmp r12, rax
00360314  72 21                           jb 0x140360337
00360316  49 8B C4                        mov rax, r12
00360319  48 C1 E8 27                     shr rax, 0x27
0036031D  25 FF 01 00 00                  and eax, 0x1ff
00360322  05 00 FF FF FF                  add eax, 0xffffff00
00360327  0F B6 84 10 A8 8A E3 00         movzx eax, byte ptr [rax + rdx + 0xe38aa8]
0036032F  3C 05                           cmp al, 5
00360331  0F 84 94 0E 00 00               je 0x1403611cb
00360337  41 BE 40 00 00 00               mov r14d, 0x40
0036033D  45 0F 20 C7                     mov r15, cr8
00360341  45 0F 22 C0                     mov cr8, r8
00360345  83 3D D4 69 C6 00 00            cmp dword ptr [rip + 0xc669d4], 0
0036034C  0F 85 7A 05 00 00               jne 0x1403608cc
00360352  F6 05 AD 67 C6 00 21            test byte ptr [rip + 0xc667ad], 0x21
00360359  0F 84 6B 04 00 00               je 0x1403607ca
0036035F  8B 05 F3 DA BA 00               mov eax, dword ptr [rip + 0xbadaf3]
00360365  85 C0                           test eax, eax
00360367  0F 85 5D 04 00 00               jne 0x1403607ca
0036036D  41 0F B6 D7                     movzx edx, r15b
00360371  48 8D 0D 80 A9 B9 00            lea rcx, [rip + 0xb9a980]
00360378  E8 A3 C9 F1 FF                  call 0x14027cd20
0036037D  4C 8B 05 B4 E9 B9 00            mov r8, qword ptr [rip + 0xb9e9b4]
00360384  49 8B C4                        mov rax, r12
00360387  4C 8B 0D A2 E9 B9 00            mov r9, qword ptr [rip + 0xb9e9a2]
0036038E  41 BA 01 00 00 00               mov r10d, 1
00360394  48 C1 E8 0C                     shr rax, 0xc
00360398  48 69 C8 5F 9E 00 00            imul rcx, rax, 0x9e5f
0036039F  41 8D 50 FF                     lea edx, [r8 - 1]
003603A3  48 8B C1                        mov rax, rcx
003603A6  48 C1 E8 20                     shr rax, 0x20
003603AA  48 33 C8                        xor rcx, rax
003603AD  23 D1                           and edx, ecx
003603AF  45 33 DB                        xor r11d, r11d
003603B2  8B CA                           mov ecx, edx
003603B4  48 C1 E1 05                     shl rcx, 5
003603B8  49 03 C9                        add rcx, r9
003603BB  48 8B 01                        mov rax, qword ptr [rcx]
003603BE  49 3B C4                        cmp rax, r12
003603C1  0F 84 35 02 00 00               je 0x1403605fc
003603C7  FF C2                           inc edx
003603C9  8B C2                           mov eax, edx
003603CB  49 3B C0                        cmp rax, r8
003603CE  72 E2                           jb 0x1403603b2
003603D0  45 85 D2                        test r10d, r10d
003603D3  0F 85 B7 0A 00 00               jne 0x140360e90
003603D9  BA 22 00 00 00                  mov edx, 0x22
003603DE  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
003603E3  4D 8B CE                        mov r9, r14
003603E6  4D 8B C4                        mov r8, r12
003603E9  8D 4A F7                        lea ecx, [rdx - 9]
003603EC  E8 6F D2 19 00                  call 0x1404fd660
003603F1  CC                              int3
003603F2  48 8B CE                        mov rcx, rsi
003603F5  A8 04                           test al, 4
003603F7  74 10                           je 0x140360409
003603F9  0F B7 06                        movzx eax, word ptr [rsi]
003603FC  66 23 C7                        and ax, di
003603FF  0F B7 C0                        movzx eax, ax
00360402  48 C1 E0 04                     shl rax, 4
00360406  48 2B C8                        sub rcx, rax
00360409  48 33 49 08                     xor rcx, qword ptr [rcx + 8]
0036040D  48 33 0D 14 6E C6 00            xor rcx, qword ptr [rip + 0xc66e14]
00360414  0F 84 D4 F7 FF FF               je 0x14035fbee
0036041A  48 83 F9 FF                     cmp rcx, -1
0036041E  0F 84 CA F7 FF FF               je 0x14035fbee
00360424  8B 05 F6 E8 B9 00               mov eax, dword ptr [rip + 0xb9e8f6]
0036042A  85 C0                           test eax, eax
0036042C  0F 85 B8 0A 00 00               jne 0x140360eea
00360432  4C 3B E3                        cmp r12, rbx
00360435  72 22                           jb 0x140360459
00360437  49 8B C4                        mov rax, r12
0036043A  48 C1 E8 27                     shr rax, 0x27
0036043E  25 FF 01 00 00                  and eax, 0x1ff
00360443  05 00 FF FF FF                  add eax, 0xffffff00
00360448  42 0F B6 84 00 A8 8A E3 00      movzx eax, byte ptr [rax + r8 + 0xe38aa8]
00360451  3C 05                           cmp al, 5
00360453  0F 84 5F 0D 00 00               je 0x1403611b8
00360459  41 BE 40 00 00 00               mov r14d, 0x40
0036045F  F6 46 03 04                     test byte ptr [rsi + 3], 4
00360463  48 8B D6                        mov rdx, rsi
00360466  74 13                           je 0x14036047b
00360468  0F B7 06                        movzx eax, word ptr [rsi]
0036046B  66 23 C7                        and ax, di
0036046E  0F B7 C8                        movzx ecx, ax
00360471  48 F7 D9                        neg rcx
00360474  48 C1 E1 04                     shl rcx, 4
00360478  48 03 D1                        add rdx, rcx
0036047B  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
0036047F  8B 72 04                        mov esi, dword ptr [rdx + 4]
00360482  0F B6 D8                        movzx ebx, al
00360485  48 C1 E3 04                     shl rbx, 4
00360489  66 C1 E8 08                     shr ax, 8
0036048D  A8 08                           test al, 8
0036048F  0F 84 58 01 00 00               je 0x1403605ed
00360495  48 8B FA                        mov rdi, rdx
00360498  48 8B C2                        mov rax, rdx
0036049B  48 33 7A 08                     xor rdi, qword ptr [rdx + 8]
0036049F  48 33 05 82 6D C6 00            xor rax, qword ptr [rip + 0xc66d82]
003604A6  48 89 42 08                     mov qword ptr [rdx + 8], rax
003604AA  48 33 3D 77 6D C6 00            xor rdi, qword ptr [rip + 0xc66d77]
003604B1  0F 84 31 01 00 00               je 0x1403605e8
003604B7  48 83 FF FF                     cmp rdi, -1
003604BB  0F 84 27 01 00 00               je 0x1403605e8
003604C1  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
003604CB  48 3B F8                        cmp rdi, rax
003604CE  0F 82 DB 08 00 00               jb 0x140360daf
003604D4  0F B6 07                        movzx eax, byte ptr [rdi]
003604D7  24 7F                           and al, 0x7f
003604D9  3C 03                           cmp al, 3
003604DB  0F 85 CE 08 00 00               jne 0x140360daf
003604E1  41 81 E6 00 01 00 00            and r14d, 0x100
003604E8  48 3B 3D C1 65 C6 00            cmp rdi, qword ptr [rip + 0xc665c1]
003604EF  0F 84 C1 00 00 00               je 0x1403605b6
003604F5  48 8B 8F F8 02 00 00            mov rcx, qword ptr [rdi + 0x2f8]
003604FC  41 8B C7                        mov eax, r15d
003604FF  4D 85 F6                        test r14, r14
00360502  48 89 4D 7F                     mov qword ptr [rbp + 0x7f], rcx
00360506  0F 95 C0                        setne al
00360509  44 8B F8                        mov r15d, eax
0036050C  8B C0                           mov eax, eax
0036050E  48 C1 E0 07                     shl rax, 7
00360512  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00360516  47 0F B6 AC F8 50 73 FC 00      movzx r13d, byte ptr [r8 + r15*8 + 0xfc7350]
0036051F  4C 8D 24 01                     lea r12, [rcx + rax]
00360523  41 0F 0D 0C 24                  prefetchw byte ptr [r12]
00360528  4D 8B 34 24                     mov r14, qword ptr [r12]
0036052C  49 8B 44 24 40                  mov rax, qword ptr [r12 + 0x40]
00360531  49 83 7C 24 50 00               cmp qword ptr [r12 + 0x50], 0
00360537  74 25                           je 0x14036055e
00360539  49 6B CF 38                     imul rcx, r15, 0x38
0036053D  49 3B C6                        cmp rax, r14
00360540  76 1C                           jbe 0x14036055e
00360542  4D 8D 80 48 66 F0 00            lea r8, [r8 + 0xf06648]
00360549  4C 03 C1                        add r8, rcx
0036054C  48 8B C8                        mov rcx, rax
0036054F  49 2B CE                        sub rcx, r14
00360552  49 8B 10                        mov rdx, qword ptr [r8]
00360555  48 3B CA                        cmp rcx, rdx
00360558  0F 87 0A 04 00 00               ja 0x140360968
0036055E  4C 8B 5D AF                     mov r11, qword ptr [rbp - 0x51]
00360562  4C 8D 15 17 7A AC 00            lea r10, [rip + 0xac7a17]
00360569  4C 8B C3                        mov r8, rbx
0036056C  49 3B DE                        cmp rbx, r14
0036056F  4D 8B CE                        mov r9, r14
00360572  49 8B CE                        mov rcx, r14
00360575  49 8B C6                        mov rax, r14
00360578  4C 0F 42 CB                     cmovb r9, rbx
0036057C  48 2B CB                        sub rcx, rbx
0036057F  33 D2                           xor edx, edx
00360581  49 3B DE                        cmp rbx, r14
00360584  48 0F 42 D1                     cmovb rdx, rcx
00360588  F0 49 0F B1 14 24               lock cmpxchg qword ptr [r12], rdx
0036058E  4C 8B F0                        mov r14, rax
00360591  75 D9                           jne 0x14036056c
00360593  49 2B D9                        sub rbx, r9
00360596  0F 85 D5 05 00 00               jne 0x140360b71
0036059C  41 F6 C5 04                     test r13b, 4
003605A0  74 0C                           je 0x1403605ae
003605A2  49 F7 D8                        neg r8
003605A5  F0 4E 01 84 FF 00 02 00 00      lock add qword ptr [rdi + r15*8 + 0x200], r8
003605AE  4C 8B 65 67                     mov r12, qword ptr [rbp + 0x67]
003605B2  4C 8B 6D 6F                     mov r13, qword ptr [rbp + 0x6f]
003605B6  83 3D 53 4A C6 00 00            cmp dword ptr [rip + 0xc64a53], 0
003605BD  74 12                           je 0x1403605d1
003605BF  33 D2                           xor edx, edx
003605C1  48 8D 4F D0                     lea rcx, [rdi - 0x30]
003605C5  44 8B CE                        mov r9d, esi
003605C8  44 8D 42 01                     lea r8d, [rdx + 1]
003605CC  E8 13 04 EB FF                  call 0x1402109e4
003605D1  48 C7 C6 FF FF FF FF            mov rsi, 0xffffffffffffffff
003605D8  F0 48 0F C1 77 D0               lock xadd qword ptr [rdi - 0x30], rsi
003605DE  48 83 EE 01                     sub rsi, 1
003605E2  0F 8E D3 06 00 00               jle 0x140360cbb
003605E8  BF FF 00 00 00                  mov edi, 0xff
003605ED  49 8D 74 24 F0                  lea rsi, [r12 - 0x10]
003605F2  BA 80 00 00 00                  mov edx, 0x80
003605F7  E9 F2 F5 FF FF                  jmp 0x14035fbee
003605FC  48 85 C9                        test rcx, rcx
003605FF  0F 84 D4 FD FF FF               je 0x1403603d9
00360605  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
00360608  48 C7 C6 FF FF FF FF            mov rsi, 0xffffffffffffffff
0036060F  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
00360613  44 8B F0                        mov r14d, eax
00360616  8B 59 08                        mov ebx, dword ptr [rcx + 8]
00360619  49 C1 EE 08                     shr r14, 8
0036061D  41 81 E6 FF 0F 00 00            and r14d, 0xfff
00360624  48 89 55 8F                     mov qword ptr [rbp - 0x71], rdx
00360628  4C 89 75 97                     mov qword ptr [rbp - 0x69], r14
0036062C  0F BA E0 08                     bt eax, 8
00360630  0F 82 19 02 00 00               jb 0x14036084f
00360636  48 8B FE                        mov rdi, rsi
00360639  F0 FF 0D C0 EA C6 00            lock dec dword ptr [rip + 0xc6eac0]
00360640  4C 89 59 18                     mov qword ptr [rcx + 0x18], r11
00360644  F0 48 FF 01                     lock inc qword ptr [rcx]
00360648  F6 05 B7 64 C6 00 01            test byte ptr [rip + 0xc664b7], 1
0036064F  0F 85 43 06 00 00               jne 0x140360c98
00360655  F0 81 25 98 A6 B9 00 FF FF FF BF  lock and dword ptr [rip + 0xb9a698], 0xbfffffff
00360660  F0 FF 0D 91 A6 B9 00            lock dec dword ptr [rip + 0xb9a691]
00360667  83 3D B2 66 C6 00 00            cmp dword ptr [rip + 0xc666b2], 0
0036066E  74 0D                           je 0x14036067d
00360670  44 0F 20 C1                     mov rcx, cr8
00360674  41 0F B6 D7                     movzx edx, r15b
00360678  E8 1B 50 19 00                  call 0x1404f5698
0036067D  41 0F B6 C7                     movzx eax, r15b
00360681  44 0F 22 C0                     mov cr8, rax
00360685  48 8D 47 FF                     lea rax, [rdi - 1]
00360689  48 83 F8 FD                     cmp rax, -3
0036068D  0F 86 42 03 00 00               jbe 0x1403609d5
00360693  4C 8B 75 8F                     mov r14, qword ptr [rbp - 0x71]
00360697  49 8B F4                        mov rsi, r12
0036069A  4C 89 65 7F                     mov qword ptr [rbp + 0x7f], r12
0036069E  49 8B FC                        mov rdi, r12
003606A1  E9 09 F6 FF FF                  jmp 0x14035fcaf
003606A6  48 C1 EF 08                     shr rdi, 8
003606AA  4D 8B C1                        mov r8, r9
003606AD  F7 D7                           not edi
003606AF  49 8B D6                        mov rdx, r14
003606B2  83 E7 01                        and edi, 1
003606B5  8B CF                           mov ecx, edi
003606B7  E8 B4 0E 00 00                  call 0x140361570
003606BC  E9 F1 FB FF FF                  jmp 0x1403602b2
003606C1  4D 23 C8                        and r9, r8
003606C4  44 89 75 A7                     mov dword ptr [rbp - 0x59], r14d
003606C8  49 8B D0                        mov rdx, r8
003606CB  41 8B CA                        mov ecx, r10d
003606CE  49 2B D1                        sub rdx, r9
003606D1  41 0F B6 C3                     movzx eax, r11b
003606D5  48 C1 FA 05                     sar rdx, 5
003606D9  24 03                           and al, 3
003606DB  48 D3 E2                        shl rdx, cl
003606DE  49 03 D1                        add rdx, r9
003606E1  3C 03                           cmp al, 3
003606E3  0F 85 EC FA FF FF               jne 0x1403601d5
003606E9  48 3B F2                        cmp rsi, rdx
003606EC  0F 84 2B 01 00 00               je 0x14036081d
003606F2  41 80 FB 0F                     cmp r11b, 0xf
003606F6  0F 85 D9 FA FF FF               jne 0x1403601d5
003606FC  48 3B F2                        cmp rsi, rdx
003606FF  0F 86 18 01 00 00               jbe 0x14036081d
00360705  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
00360709  4C 8D 4D A7                     lea r9, [rbp - 0x59]
0036070D  4C 8B C6                        mov r8, rsi
00360710  E8 1B 0F 00 00                  call 0x140361630
00360715  85 C0                           test eax, eax
00360717  0F 84 A0 FB FF FF               je 0x1403602bd
0036071D  4C 8B 43 18                     mov r8, qword ptr [rbx + 0x18]
00360721  8B 4D A7                        mov ecx, dword ptr [rbp - 0x59]
00360724  41 0F B7 40 44                  movzx eax, word ptr [r8 + 0x44]
00360729  3B C8                           cmp ecx, eax
0036072B  0F 83 8C FB FF FF               jae 0x1403602bd
00360731  83 C1 0F                        add ecx, 0xf
00360734  48 C1 E9 04                     shr rcx, 4
00360738  46 0F B6 94 39 80 0B 01 00      movzx r10d, byte ptr [rcx + r15 + 0x10b80]
00360741  41 FF CA                        dec r10d
00360744  4F 8D 0C D0                     lea r9, [r8 + r10*8]
00360748  49 8B 89 C0 01 00 00            mov rcx, qword ptr [r9 + 0x1c0]
0036074F  48 8B C1                        mov rax, rcx
00360752  48 89 4D 7F                     mov qword ptr [rbp + 0x7f], rcx
00360756  48 C1 E8 10                     shr rax, 0x10
0036075A  48 8B D1                        mov rdx, rcx
0036075D  F6 C1 01                        test cl, 1
00360760  74 25                           je 0x140360787
00360762  66 83 F8 01                     cmp ax, 1
00360766  76 0E                           jbe 0x140360776
00360768  66 FF C8                        dec ax
0036076B  66 89 85 81 00 00 00            mov word ptr [rbp + 0x81], ax
00360772  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
00360776  48 8B C1                        mov rax, rcx
00360779  F0 49 0F B1 91 C0 01 00 00      lock cmpxchg qword ptr [r9 + 0x1c0], rdx
00360782  48 3B C1                        cmp rax, rcx
00360785  75 C1                           jne 0x140360748
00360787  4B 8B 8C D0 C0 01 00 00         mov rcx, qword ptr [r8 + r10*8 + 0x1c0]
0036078F  E9 29 FB FF FF                  jmp 0x1403602bd
00360794  8B 05 BE D6 BA 00               mov eax, dword ptr [rip + 0xbad6be]
0036079A  85 C0                           test eax, eax
0036079C  0F 85 10 F6 FF FF               jne 0x14035fdb2
003607A2  48 8B D1                        mov rdx, rcx
003607A5  48 8D 4D B7                     lea rcx, [rbp - 0x49]
003607A9  E8 A2 50 F1 FF                  call 0x140275850
003607AE  E9 13 F6 FF FF                  jmp 0x14035fdc6
003607B3  41 B9 01 00 00 00               mov r9d, 1
003607B9  49 8D 50 08                     lea rdx, [r8 + 8]
003607BD  49 8D 40 18                     lea rax, [r8 + 0x18]
003607C1  45 8D 51 17                     lea r10d, [r9 + 0x17]
003607C5  E9 97 F9 FF FF                  jmp 0x140360161
003607CA  0F 0D 0D 27 A5 B9 00            prefetchw byte ptr [rip + 0xb9a527]
003607D1  8B 05 21 A5 B9 00               mov eax, dword ptr [rip + 0xb9a521]
003607D7  0F BA F0 1F                     btr eax, 0x1f
003607DB  8D 48 01                        lea ecx, [rax + 1]
003607DE  F0 0F B1 0D 12 A5 B9 00         lock cmpxchg dword ptr [rip + 0xb9a512], ecx
003607E6  0F 84 91 FB FF FF               je 0x14036037d
003607EC  85 C0                           test eax, eax
003607EE  79 EB                           jns 0x1403607db
003607F0  41 0F B6 D7                     movzx edx, r15b
003607F4  48 8D 0D FD A4 B9 00            lea rcx, [rip + 0xb9a4fd]
003607FB  E8 80 1B 00 00                  call 0x140362380
00360800  E9 78 FB FF FF                  jmp 0x14036037d
00360805  0F B6 D0                        movzx edx, al
00360808  40 0F B6 CF                     movzx ecx, dil
0036080C  E8 EB 4E 19 00                  call 0x1404f56fc
00360811  48 8D 0D E8 A4 B9 00            lea rcx, [rip + 0xb9a4e8]
00360818  E9 84 F5 FF FF                  jmp 0x14035fda1
0036081D  49 8B D0                        mov rdx, r8
00360820  48 8B CB                        mov rcx, rbx
00360823  E8 78 27 F8 FF                  call 0x1402e2fa0
00360828  E9 90 FA FF FF                  jmp 0x1403602bd
0036082D  48 8B 16                        mov rdx, qword ptr [rsi]
00360830  4D 8B C7                        mov r8, r15
00360833  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00360838  B9 11 00 00 00                  mov ecx, 0x11
0036083D  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00360842  4C 8B CF                        mov r9, rdi
00360845  E8 72 AF FF FF                  call 0x14035b7bc
0036084A  E9 6E FA FF FF                  jmp 0x1403602bd
0036084F  48 8B 79 18                     mov rdi, qword ptr [rcx + 0x18]
00360853  48 33 3D CE 69 C6 00            xor rdi, qword ptr [rip + 0xc669ce]
0036085A  49 33 FC                        xor rdi, r12
0036085D  E9 D7 FD FF FF                  jmp 0x140360639
00360862  48 8B 05 F7 E4 B9 00            mov rax, qword ptr [rip + 0xb9e4f7]
00360869  8B 04 C8                        mov eax, dword ptr [rax + rcx*8]
0036086C  85 C0                           test eax, eax
0036086E  0F 84 E9 F4 FF FF               je 0x14035fd5d
00360874  41 89 00                        mov dword ptr [r8], eax
00360877  48 8B 05 E2 E4 B9 00            mov rax, qword ptr [rip + 0xb9e4e2]
0036087E  48 8B 44 C8 48                  mov rax, qword ptr [rax + rcx*8 + 0x48]
00360883  48 85 C0                        test rax, rax
00360886  0F 84 B0 F4 FF FF               je 0x14035fd3c
0036088C  49 89 40 48                     mov qword ptr [r8 + 0x48], rax
00360890  E9 A7 F4 FF FF                  jmp 0x14035fd3c
00360895  C6 44 32 5C 01                  mov byte ptr [rdx + rsi + 0x5c], 1
0036089A  48 8B 0E                        mov rcx, qword ptr [rsi]
0036089D  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
003608A1  48 8B 00                        mov rax, qword ptr [rax]
003608A4  48 C1 E8 08                     shr rax, 8
003608A8  3C 01                           cmp al, 1
003608AA  0F 85 0C 01 00 00               jne 0x1403609bc
003608B0  8B 05 06 9F B9 00               mov eax, dword ptr [rip + 0xb99f06]
003608B6  85 C0                           test eax, eax
003608B8  0F 85 02 F8 FF FF               jne 0x1403600c0
003608BE  48 8B 49 38                     mov rcx, qword ptr [rcx + 0x38]
003608C2  E8 D9 5B FC FF                  call 0x1403264a0
003608C7  E9 F4 F7 FF FF                  jmp 0x1403600c0
003608CC  41 0F B6 D0                     movzx edx, r8b
003608D0  41 0F B6 CF                     movzx ecx, r15b
003608D4  E8 23 4E 19 00                  call 0x1404f56fc
003608D9  E9 74 FA FF FF                  jmp 0x140360352
003608DE  48 8B 05 7B E4 B9 00            mov rax, qword ptr [rip + 0xb9e47b]
003608E5  8B 04 C8                        mov eax, dword ptr [rax + rcx*8]
003608E8  85 C0                           test eax, eax
003608EA  0F 84 A8 F9 FF FF               je 0x140360298
003608F0  41 89 01                        mov dword ptr [r9], eax
003608F3  48 8B 05 66 E4 B9 00            mov rax, qword ptr [rip + 0xb9e466]
003608FA  48 8B 44 C8 48                  mov rax, qword ptr [rax + rcx*8 + 0x48]
003608FF  48 85 C0                        test rax, rax
00360902  0F 84 6F F9 FF FF               je 0x140360277
00360908  49 89 41 48                     mov qword ptr [r9 + 0x48], rax
0036090C  E9 66 F9 FF FF                  jmp 0x140360277
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003602E3(__int64 a1, __int64 a2, __int64 a3)
{
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;

    a2 = (a2) | (1);
    *(unsigned __int64 *)(v_rbp - 105) = a2;
}
```

## 5. (Beta) C Style

```c
int64_t sub_003602E3(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;

    Arg2 = (Arg2) | (1);
    *(uint64_t *)(local_rbp - 0x69) = Arg2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003602E3&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
