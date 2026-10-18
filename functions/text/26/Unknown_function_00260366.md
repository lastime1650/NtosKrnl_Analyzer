# sub_00260366

- RVA: `0x00260366`–`0x00260D3F` (길이 `2,521` bytes)
- VA: `0x0000000140260366`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000643E0`
- 디코드: `595`개 명령, `2,521/2,521` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00260441` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x00260500` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0026051F` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x00260539` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x00260554` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002605C7` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x002605E1` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002606A4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x002606E1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00260817` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0026084D` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x00260860` → [KiHaltOnAddressWakeEntireList](../21/KiHaltOnAddressWakeEntireList_function_00217AF4.md) (function, `0x00217AF4`)
- `0x002608BF` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x0026090B` → [KiRemoveBoostThread](../21/KiRemoveBoostThread_function_00219128.md) (function, `0x00219128`)
- `0x00260936` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x00260989` → [KiRemoveSystemWorkPriorityKick](KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x002609D5` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x00260A38` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x00260A76` → [KiRemoveBoostThread](../21/KiRemoveBoostThread_function_00219128.md) (function, `0x00219128`)
- `0x00260AA3` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x00260AD2` → [KiRemoveSystemWorkPriorityKick](KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00260B05` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00260B23` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x00260B64` → [KiRemoveSystemWorkPriorityKick](KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00260BA7` → [RtlRemoveHeadCircularList](../43/RtlRemoveHeadCircularList_function_00432D70.md) (function, `0x00432D70`)
- `0x00260C5F` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x00260C70` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00260C8E` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002603D4` → RVA `0x00FC6F88` (`ALMOSTRO`; read)
- `0x0026042A` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x002604CA` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00260526` → RVA `0x00F0DE58` (`.data`; read)
- `0x0026053E` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0026058F` → RVA `0x00FC6B06` (`ALMOSTRO`; reference)
- `0x00260684` → RVA `0x00E68468` (`.data`; read)
- `0x002607C5` → RVA `0x00E0EB10` (`.data`; read)
- `0x00260842` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00260BE4` → RVA `0x00E0EB18` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x002606A4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x002606E1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **39**
  - `0x002603DD` → [sub_00260D5A + 0x1F1](Unknown_function_00260D5A.md) (`tail-transfer`)
  - `0x002603EA` → [sub_00261078 + 0x54](Unknown_function_00261078.md) (`tail-transfer`)
  - `0x002603FB` → [sub_0026118A + 0xC1](Unknown_function_0026118A.md) (`tail-transfer`)
  - `0x00260457` → [sub_00260D5A + 0x49](Unknown_function_00260D5A.md) (`tail-transfer`)
  - `0x00260482` → [sub_00260D5A + 0x15B](Unknown_function_00260D5A.md) (`tail-transfer`)
  - `0x002605F6` → [sub_0026029A + 0x4D](Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x00260651` → [sub_0026029A + 0x4D](Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x00260677` → [sub_0026029A + 0x4D](Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x002606AF` → [sub_0026029A + 0x4D](Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x00260753` → [sub_0026029A + 0x4D](Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x0026075C` → [sub_0026029A + 0x4A](Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x00260772` → [sub_0026118A + 0x1D3](Unknown_function_0026118A.md) (`tail-transfer`)
  - `0x00260791` → [sub_0026118A + 0x1DB](Unknown_function_0026118A.md) (`tail-transfer`)
  - `0x002607AF` → [sub_0026118A + 0x204](Unknown_function_0026118A.md) (`tail-transfer`)
  - `0x002607CD` → [sub_0026029A + 0x4A](Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x002608D5` → [sub_00260129 + 0x109](Unknown_function_00260129.md) (`tail-transfer`)
  - `0x002608DF` → [sub_00260129 + 0x109](Unknown_function_00260129.md) (`tail-transfer`)
  - `0x0026093B` → [sub_0025FB5C + 0x24B](../25/Unknown_function_0025FB5C.md) (`tail-transfer`)
  - `0x00260966` → [sub_0025FB5C + 0x110](../25/Unknown_function_0025FB5C.md) (`tail-transfer`)
  - `0x00260983` → [sub_0025FB5C + 0x5A6](../25/Unknown_function_0025FB5C.md) (`tail-transfer`)
  - `0x0026098E` → [sub_0025FB5C + 0x5A6](../25/Unknown_function_0025FB5C.md) (`tail-transfer`)
  - `0x00260A06` → [sub_00260129 + 0x130](Unknown_function_00260129.md) (`tail-transfer`)
  - `0x00260A0F` → [sub_00260129 + 0x130](Unknown_function_00260129.md) (`tail-transfer`)
  - `0x00260A83` → [sub_00260D5A + 0x11](Unknown_function_00260D5A.md) (`tail-transfer`)
  - `0x00260A8C` → [sub_00260D5A](Unknown_function_00260D5A.md) (`tail-transfer`)
  - `0x00260AAF` → [sub_0025FB5C + 0x278](../25/Unknown_function_0025FB5C.md) (`tail-transfer`)
  - `0x00260ACC` → [sub_0025FB5C + 0x1ED](../25/Unknown_function_0025FB5C.md) (`tail-transfer`)
  - `0x00260AD7` → [sub_0025FB5C + 0x1ED](../25/Unknown_function_0025FB5C.md) (`tail-transfer`)
  - `0x00260AE3` → [sub_0026029A + 0x4D](Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x00260AED` → [sub_0026029A + 0x4D](Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x00260B0A` → [sub_00260129 + 0xC3](Unknown_function_00260129.md) (`tail-transfer`)
  - `0x00260B12` → [sub_00260D5A + 0x76](Unknown_function_00260D5A.md) (`tail-transfer`)
  - `0x00260B41` → [sub_00260129 + 0x109](Unknown_function_00260129.md) (`tail-transfer`)
  - `0x00260B74` → [sub_00260129 + 0xD7](Unknown_function_00260129.md) (`tail-transfer`)
  - `0x00260B80` → [sub_00260129 + 0x9F](Unknown_function_00260129.md) (`tail-transfer`)
  - `0x00260B9E` → [sub_0025FB5C + 0x110](../25/Unknown_function_0025FB5C.md) (`tail-transfer`)
  - `0x00260BEC` → [sub_0026029A + 0x1B](Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x00260C64` → [sub_0026029A + 0x4A](Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x00260C7D` → [sub_00260D5A + 0xEA](Unknown_function_00260D5A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00260366  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0026036F  8B C7                           mov eax, edi
00260371  2B 43 10                        sub eax, dword ptr [rbx + 0x10]
00260374  48 C1 F8 04                     sar rax, 4
00260378  88 81 60 04 00 00               mov byte ptr [rcx + 0x460], al
0026037E  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00260381  41 BC 01 00 00 00               mov r12d, 1
00260387  8B C1                           mov eax, ecx
00260389  83 E1 07                        and ecx, 7
0026038C  C1 E8 03                        shr eax, 3
0026038F  8D 04 C5 F8 FF FF FF            lea eax, [rax*8 - 8]
00260396  0B C1                           or eax, ecx
00260398  44 8B F0                        mov r14d, eax
0026039B  89 47 08                        mov dword ptr [rdi + 8], eax
0026039E  41 C1 EE 03                     shr r14d, 3
002603A2  44 89 74 24 60                  mov dword ptr [rsp + 0x60], r14d
002603A7  45 85 F6                        test r14d, r14d
002603AA  0F 85 DF 01 00 00               jne 0x14026058f
002603B0  4C 8B 37                        mov r14, qword ptr [rdi]
002603B3  41 84 C7                        test r15b, al
002603B6  0F 84 D1 04 00 00               je 0x14026088d
002603BC  49 83 E6 FC                     and r14, 0xfffffffffffffffc
002603C0  4D 85 F6                        test r14, r14
002603C3  0F 84 98 00 00 00               je 0x140260461
002603C9  41 84 C4                        test r12b, al
002603CC  74 42                           je 0x140260410
002603CE  45 32 E4                        xor r12b, r12b
002603D1  45 32 ED                        xor r13b, r13b
002603D4  39 35 AE 6B D6 00               cmp dword ptr [rip + 0xd66bae], esi
002603DA  48 8B C6                        mov rax, rsi
002603DD  0F 85 68 0B 00 00               jne 0x140260f4b
002603E3  41 39 B6 E0 05 00 00            cmp dword ptr [r14 + 0x5e0], esi
002603EA  0F 84 DC 0C 00 00               je 0x1402610cc
002603F0  F0 41 FF 8E E0 05 00 00         lock dec dword ptr [r14 + 0x5e0]
002603F8  45 84 E4                        test r12b, r12b
002603FB  0F 85 4A 0E 00 00               jne 0x14026124b
00260401  8B 47 08                        mov eax, dword ptr [rdi + 8]
00260404  41 BC 01 00 00 00               mov r12d, 1
0026040A  83 E0 FE                        and eax, 0xfffffffe
0026040D  89 47 08                        mov dword ptr [rdi + 8], eax
00260410  A8 04                           test al, 4
00260412  74 11                           je 0x140260425
00260414  F0 41 FF 8E E4 05 00 00         lock dec dword ptr [r14 + 0x5e4]
0026041C  8B 47 08                        mov eax, dword ptr [rdi + 8]
0026041F  83 E0 FB                        and eax, 0xfffffffb
00260422  89 47 08                        mov dword ptr [rdi + 8], eax
00260425  41 84 C7                        test r15b, al
00260428  74 37                           je 0x140260461
0026042A  39 35 E0 4B D6 00               cmp dword ptr [rip + 0xd64be0], esi
00260430  74 14                           je 0x140260446
00260432  41 B9 44 66 6C 74               mov r9d, 0x746c6644
00260438  49 8D 4E D0                     lea rcx, [r14 - 0x30]
0026043C  45 8B C4                        mov r8d, r12d
0026043F  33 D2                           xor edx, edx
00260441  E8 9E 05 FB FF                  call 0x1402109e4
00260446  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0026044D  F0 49 0F C1 46 D0               lock xadd qword ptr [r14 - 0x30], rax
00260453  48 83 E8 01                     sub rax, 1
00260457  0F 8E 46 09 00 00               jle 0x140260da3
0026045D  83 67 08 FD                     and dword ptr [rdi + 8], 0xfffffffd
00260461  48 89 37                        mov qword ptr [rdi], rsi
00260464  48 8B FE                        mov rdi, rsi
00260467  83 7B 40 01                     cmp dword ptr [rbx + 0x40], 1
0026046B  8B 43 44                        mov eax, dword ptr [rbx + 0x44]
0026046E  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00260472  77 14                           ja 0x140260488
00260474  39 73 4C                        cmp dword ptr [rbx + 0x4c], esi
00260477  0F 85 26 07 00 00               jne 0x140260ba3
0026047D  8B 4B 48                        mov ecx, dword ptr [rbx + 0x48]
00260480  85 C9                           test ecx, ecx
00260482  0F 85 2D 0A 00 00               jne 0x140260eb5
00260488  8B CE                           mov ecx, esi
0026048A  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
0026048D  FF C8                           dec eax
0026048F  03 C8                           add ecx, eax
00260491  89 4B 40                        mov dword ptr [rbx + 0x40], ecx
00260494  75 04                           jne 0x14026049a
00260496  66 89 73 18                     mov word ptr [rbx + 0x18], si
0026049A  39 73 4C                        cmp dword ptr [rbx + 0x4c], esi
0026049D  75 0E                           jne 0x1402604ad
0026049F  39 73 48                        cmp dword ptr [rbx + 0x48], esi
002604A2  75 09                           jne 0x1402604ad
002604A4  B9 F9 00 00 00                  mov ecx, 0xf9
002604A9  66 21 4B 1A                     and word ptr [rbx + 0x1a], cx
002604AD  0F B6 43 1B                     movzx eax, byte ptr [rbx + 0x1b]
002604B1  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
002604B5  48 85 FF                        test rdi, rdi
002604B8  74 10                           je 0x1402604ca
002604BA  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
002604BD  83 E0 07                        and eax, 7
002604C0  48 89 7B 30                     mov qword ptr [rbx + 0x30], rdi
002604C4  83 C8 08                        or eax, 8
002604C7  89 43 38                        mov dword ptr [rbx + 0x38], eax
002604CA  F6 05 35 66 D6 00 01            test byte ptr [rip + 0xd66635], 1
002604D1  75 53                           jne 0x140260526
002604D3  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
002604D8  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002604DD  48 85 C0                        test rax, rax
002604E0  75 23                           jne 0x140260505
002604E2  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
002604E7  48 8D 44 24 48                  lea rax, [rsp + 0x48]
002604EC  F0 48 0F B1 31                  lock cmpxchg qword ptr [rcx], rsi
002604F1  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
002604F6  48 3B C1                        cmp rax, rcx
002604F9  74 43                           je 0x14026053e
002604FB  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00260500  E8 9B 75 FB FF                  call 0x140217aa0
00260505  48 8D 48 08                     lea rcx, [rax + 8]
00260509  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
0026050E  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00260513  48 8B C2                        mov rax, rdx
00260516  48 87 01                        xchg qword ptr [rcx], rax
00260519  32 C2                           xor al, dl
0026051B  A8 04                           test al, 4
0026051D  74 1F                           je 0x14026053e
0026051F  E8 FC 76 FB FF                  call 0x140217c20
00260524  EB 18                           jmp 0x14026053e
00260526  8B 05 2C D9 CA 00               mov eax, dword ptr [rip + 0xcad92c]
0026052C  85 C0                           test eax, eax
0026052E  75 A3                           jne 0x1402604d3
00260530  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
00260534  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00260539  E8 B2 74 FB FF                  call 0x1402179f0
0026053E  39 35 DC 67 D6 00               cmp dword ptr [rip + 0xd667dc], esi
00260544  44 0F B6 74 24 58               movzx r14d, byte ptr [rsp + 0x58]
0026054A  74 0D                           je 0x140260559
0026054C  44 0F 20 C1                     mov rcx, cr8
00260550  41 0F B6 D6                     movzx edx, r14b
00260554  E8 3F 51 29 00                  call 0x1404f5698
00260559  45 0F 22 C6                     mov cr8, r14
0026055D  48 85 FF                        test rdi, rdi
00260560  B8 01 00 00 00                  mov eax, 1
00260565  44 8B F0                        mov r14d, eax
00260568  41 BC 03 00 00 00               mov r12d, 3
0026056E  45 0F 45 F4                     cmovne r14d, r12d
00260572  8B F8                           mov edi, eax
00260574  48 39 75 A0                     cmp qword ptr [rbp - 0x60], rsi
00260578  0F 85 15 04 00 00               jne 0x140260993
0026057E  41 BE 42 00 01 00               mov r14d, 0x10042
00260584  89 74 24 60                     mov dword ptr [rsp + 0x60], esi
00260588  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
0026058D  EB 5B                           jmp 0x1402605ea
0026058F  44 84 25 70 65 D6 00            test byte ptr [rip + 0xd66570], r12b
00260596  41 BE 52 00 01 00               mov r14d, 0x10052
0026059C  44 8B 6B 44                     mov r13d, dword ptr [rbx + 0x44]
002605A0  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
002605A5  44 89 6C 24 40                  mov dword ptr [rsp + 0x40], r13d
002605AA  0F 84 36 02 00 00               je 0x1402607e6
002605B0  8B 05 A2 D8 CA 00               mov eax, dword ptr [rip + 0xcad8a2]
002605B6  85 C0                           test eax, eax
002605B8  0F 85 28 02 00 00               jne 0x1402607e6
002605BE  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
002605C2  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
002605C7  E8 24 74 FB FF                  call 0x1402179f0
002605CC  39 35 4E 67 D6 00               cmp dword ptr [rip + 0xd6674e], esi
002605D2  0F B6 7C 24 58                  movzx edi, byte ptr [rsp + 0x58]
002605D7  74 0D                           je 0x1402605e6
002605D9  44 0F 20 C1                     mov rcx, cr8
002605DD  40 0F B6 D7                     movzx edx, dil
002605E1  E8 B2 50 29 00                  call 0x1404f5698
002605E6  44 0F 22 C7                     mov cr8, rdi
002605EA  65 FF 04 25 70 90 00 00         inc dword ptr gs:[0x9070]
002605F2  39 74 24 70                     cmp dword ptr [rsp + 0x70], esi
002605F6  0F 84 EB FC FF FF               je 0x1402602e7
002605FC  0F 57 C0                        xorps xmm0, xmm0
002605FF  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00260603  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00260607  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
0026060B  0F 31                           rdtsc
0026060D  65 4C 8B 2C 25 20 00 00 00      mov r13, qword ptr gs:[0x20]
00260616  48 C1 E2 20                     shl rdx, 0x20
0026061A  48 0B C2                        or rax, rdx
0026061D  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00260621  41 FF 85 70 8F 00 00            inc dword ptr [r13 + 0x8f70]
00260628  41 0F B6 85 D0 00 00 00         movzx eax, byte ptr [r13 + 0xd0]
00260630  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00260639  66 89 44 24 70                  mov word ptr [rsp + 0x70], ax
0026063E  41 0F B6 85 D1 00 00 00         movzx eax, byte ptr [r13 + 0xd1]
00260646  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0026064A  48 39 B1 20 06 00 00            cmp qword ptr [rcx + 0x620], rsi
00260651  0F 84 90 FC FF FF               je 0x1402602e7
00260657  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00260660  45 8B E6                        mov r12d, r14d
00260663  41 81 E4 00 00 FF FF            and r12d, 0xffff0000
0026066A  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0026066F  8B 81 A0 05 00 00               mov eax, dword ptr [rcx + 0x5a0]
00260675  A8 01                           test al, 1
00260677  0F 85 6A FC FF FF               jne 0x1402602e7
0026067D  4C 8B B1 20 06 00 00            mov r14, qword ptr [rcx + 0x620]
00260684  44 8B 05 DD 7D C0 00            mov r8d, dword ptr [rip + 0xc07ddd]
0026068B  44 89 44 24 68                  mov dword ptr [rsp + 0x68], r8d
00260690  4D 85 F6                        test r14, r14
00260693  75 56                           jne 0x1402606eb
00260695  BA 00 02 00 00                  mov edx, 0x200
0026069A  41 8D 4E 48                     lea ecx, [r14 + 0x48]
0026069E  41 B8 52 65 54 72               mov r8d, 0x72546552
002606A4  E8 47 1A 92 00                  call 0x140b820f0
002606A9  48 8B F8                        mov rdi, rax
002606AC  48 85 C0                        test rax, rax
002606AF  0F 84 32 FC FF FF               je 0x1402602e7
002606B5  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
002606BA  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
002606BE  44 89 60 1C                     mov dword ptr [rax + 0x1c], r12d
002606C2  89 70 20                        mov dword ptr [rax + 0x20], esi
002606C5  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
002606C9  89 47 28                        mov dword ptr [rdi + 0x28], eax
002606CC  33 C0                           xor eax, eax
002606CE  F0 48 0F B1 B9 20 06 00 00      lock cmpxchg qword ptr [rcx + 0x620], rdi
002606D7  4C 8B F0                        mov r14, rax
002606DA  74 7D                           je 0x140260759
002606DC  33 D2                           xor edx, edx
002606DE  48 8B CF                        mov rcx, rdi
002606E1  E8 8A 21 92 00                  call 0x140b82870
002606E6  44 8B 44 24 68                  mov r8d, dword ptr [rsp + 0x68]
002606EB  48 8B C6                        mov rax, rsi
002606EE  8B D6                           mov edx, esi
002606F0  83 FA 08                        cmp edx, 8
002606F3  73 33                           jae 0x140260728
002606F5  41 8B 4E 1C                     mov ecx, dword ptr [r14 + 0x1c]
002606F9  41 3B CC                        cmp ecx, r12d
002606FC  75 0C                           jne 0x14026070a
002606FE  49 39 5E 10                     cmp qword ptr [r14 + 0x10], rbx
00260702  75 06                           jne 0x14026070a
00260704  45 39 46 28                     cmp dword ptr [r14 + 0x28], r8d
00260708  74 43                           je 0x14026074d
0026070A  48 85 C0                        test rax, rax
0026070D  0F 85 C8 00 00 00               jne 0x1402607db
00260713  85 C9                           test ecx, ecx
00260715  0F 84 BD 00 00 00               je 0x1402607d8
0026071B  45 39 46 28                     cmp dword ptr [r14 + 0x28], r8d
0026071F  0F 8D B6 00 00 00               jge 0x1402607db
00260725  49 8B C6                        mov rax, r14
00260728  4C 8B F0                        mov r14, rax
0026072B  48 85 C0                        test rax, rax
0026072E  74 1D                           je 0x14026074d
00260730  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00260734  44 89 60 1C                     mov dword ptr [rax + 0x1c], r12d
00260738  48 89 70 20                     mov qword ptr [rax + 0x20], rsi
0026073C  48 89 30                        mov qword ptr [rax], rsi
0026073F  48 89 70 08                     mov qword ptr [rax + 8], rsi
00260743  89 70 18                        mov dword ptr [rax + 0x18], esi
00260746  44 89 40 28                     mov dword ptr [rax + 0x28], r8d
0026074A  89 70 2C                        mov dword ptr [rax + 0x2c], esi
0026074D  49 8B FE                        mov rdi, r14
00260750  4D 85 F6                        test r14, r14
00260753  0F 84 8E FB FF FF               je 0x1402602e7
00260759  39 77 20                        cmp dword ptr [rdi + 0x20], esi
0026075C  0F 84 82 FB FF FF               je 0x1402602e4
00260762  41 FF 85 74 8F 00 00            inc dword ptr [r13 + 0x8f74]
00260769  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
0026076D  FF C0                           inc eax
0026076F  39 47 24                        cmp dword ptr [rdi + 0x24], eax
00260772  0F 82 E5 0B 00 00               jb 0x14026135d
00260778  44 8B 44 24 38                  mov r8d, dword ptr [rsp + 0x38]
0026077D  41 81 F8 42 00 01 00            cmp r8d, 0x10042
00260784  0F 85 52 03 00 00               jne 0x140260adc
0026078A  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0026078E  49 3B C7                        cmp rax, r15
00260791  0F 87 CE 0B 00 00               ja 0x140261365
00260797  4C 8B CE                        mov r9, rsi
0026079A  48 83 3F 01                     cmp qword ptr [rdi], 1
0026079E  0F 87 34 05 00 00               ja 0x140260cd8
002607A4  8B 4F 2C                        mov ecx, dword ptr [rdi + 0x2c]
002607A7  44 8B 54 24 40                  mov r10d, dword ptr [rsp + 0x40]
002607AC  44 3B D1                        cmp r10d, ecx
002607AF  0F 87 D9 0B 00 00               ja 0x14026138e
002607B5  41 8B 85 F0 8E 00 00            mov eax, dword ptr [r13 + 0x8ef0]
002607BC  33 D2                           xor edx, edx
002607BE  41 03 85 EC 8E 00 00            add eax, dword ptr [r13 + 0x8eec]
002607C5  F7 35 45 E3 BA 00               div dword ptr [rip + 0xbae345]
002607CB  85 D2                           test edx, edx
002607CD  0F 85 11 FB FF FF               jne 0x1402602e4
002607D3  E9 23 05 00 00                  jmp 0x140260cfb
002607D8  49 8B C6                        mov rax, r14
002607DB  49 83 C6 40                     add r14, 0x40
002607DF  FF C2                           inc edx
002607E1  E9 0A FF FF FF                  jmp 0x1402606f0
002607E6  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
002607EB  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002607F0  48 85 C0                        test rax, rax
002607F3  75 27                           jne 0x14026081c
002607F5  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
002607FA  48 8D 44 24 48                  lea rax, [rsp + 0x48]
002607FF  F0 48 0F B1 31                  lock cmpxchg qword ptr [rcx], rsi
00260804  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00260809  48 3B C1                        cmp rax, rcx
0026080C  0F 84 BA FD FF FF               je 0x1402605cc
00260812  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00260817  E8 84 72 FB FF                  call 0x140217aa0
0026081C  4C 8D 40 08                     lea r8, [rax + 8]
00260820  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
00260825  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0026082A  48 8B C1                        mov rax, rcx
0026082D  49 87 00                        xchg qword ptr [r8], rax
00260830  32 C1                           xor al, cl
00260832  A8 04                           test al, 4
00260834  0F 84 92 FD FF FF               je 0x1402605cc
0026083A  F0 09 34 24                     lock or dword ptr [rsp], esi
0026083E  49 C1 E8 05                     shr r8, 5
00260842  4C 8D 15 B7 F7 D9 FF            lea r10, [rip - 0x260849]
00260849  41 83 E0 7F                     and r8d, 0x7f
0026084D  E8 8E 73 FB FF                  call 0x140217be0
00260852  48 8B D6                        mov rdx, rsi
00260855  0F B6 F8                        movzx edi, al
00260858  4B 87 94 C2 20 1B F2 00         xchg qword ptr [r10 + r8*8 + 0xf21b20], rdx
00260860  E8 8F 72 FB FF                  call 0x140217af4
00260865  40 84 FF                        test dil, dil
00260868  0F 84 5E FD FF FF               je 0x1402605cc
0026086E  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00260877  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0026087E  4D 85 C0                        test r8, r8
00260881  0F 85 BF 02 00 00               jne 0x140260b46
00260887  FB                              sti
00260888  E9 3F FD FF FF                  jmp 0x1402605cc
0026088D  41 F6 C6 03                     test r14b, 3
00260891  0F 85 CA FB FF FF               jne 0x140260461
00260897  E9 24 FB FF FF                  jmp 0x1402603c0
0026089C  48 89 10                        mov qword ptr [rax], rdx
0026089F  48 89 42 08                     mov qword ptr [rdx + 8], rax
002608A3  0F B6 41 10                     movzx eax, byte ptr [rcx + 0x10]
002608A7  41 3A C6                        cmp al, r14b
002608AA  0F 85 5F 02 00 00               jne 0x140260b0f
002608B0  44 0F B7 41 12                  movzx r8d, word ptr [rcx + 0x12]
002608B5  48 8B D1                        mov rdx, rcx
002608B8  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
002608BC  45 33 C9                        xor r9d, r9d
002608BF  E8 0C FE 0E 00                  call 0x1403506d0
002608C4  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002608C9  84 C0                           test al, al
002608CB  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
002608D0  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
002608D5  0F 84 57 F9 FF FF               je 0x140260232
002608DB  45 29 71 04                     sub dword ptr [r9 + 4], r14d
002608DF  0F 85 4D F9 FF FF               jne 0x140260232
002608E5  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
002608E9  F0 81 60 18 7F FF FF FF         lock and dword ptr [rax + 0x18], 0xffffff7f
002608F1  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
002608F5  48 3B 4D 90                     cmp rcx, qword ptr [rbp - 0x70]
002608F9  0F 85 6F 02 00 00               jne 0x140260b6e
002608FF  4C 8B 65 80                     mov r12, qword ptr [rbp - 0x80]
00260903  49 8B CC                        mov rcx, r12
00260906  49 8B 54 24 08                  mov rdx, qword ptr [r12 + 8]
0026090B  E8 18 88 FB FF                  call 0x140219128
00260910  45 85 ED                        test r13d, r13d
00260913  0F 85 B0 03 00 00               jne 0x140260cc9
00260919  41 84 FF                        test r15b, dil
0026091C  0F 85 8A 03 00 00               jne 0x140260cac
00260922  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00260927  45 8B CD                        mov r9d, r13d
0026092A  45 8B C6                        mov r8d, r14d
0026092D  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00260931  33 D2                           xor edx, edx
00260933  49 8B CC                        mov rcx, r12
00260936  E8 B5 13 FF FF                  call 0x140251cf0
0026093B  E9 67 F4 FF FF                  jmp 0x14025fda7
00260940  48 89 73 28                     mov qword ptr [rbx + 0x28], rsi
00260944  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00260948  4C 8B 71 10                     mov r14, qword ptr [rcx + 0x10]
0026094C  48 85 C0                        test rax, rax
0026094F  0F 85 24 02 00 00               jne 0x140260b79
00260955  48 89 49 08                     mov qword ptr [rcx + 8], rcx
00260959  48 89 09                        mov qword ptr [rcx], rcx
0026095C  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
00260960  FF 4B 4C                        dec dword ptr [rbx + 0x4c]
00260963  41 8B CC                        mov ecx, r12d
00260966  E9 01 F3 FF FF                  jmp 0x14025fc6c
0026096B  41 0F 0D 08                     prefetchw byte ptr [r8]
0026096F  41 8B 00                        mov eax, dword ptr [r8]
00260972  8B D0                           mov edx, eax
00260974  0F BA F2 15                     btr edx, 0x15
00260978  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0026097D  75 F3                           jne 0x140260972
0026097F  0F BA E0 15                     bt eax, 0x15
00260983  0F 83 79 F7 FF FF               jae 0x140260102
00260989  E8 42 28 00 00                  call 0x1402631d0
0026098E  E9 6F F7 FF FF                  jmp 0x140260102
00260993  44 0F 20 C0                     mov rax, cr8
00260997  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0026099C  45 0F 22 C7                     mov cr8, r15
002609A0  39 35 7A 63 D6 00               cmp dword ptr [rip + 0xd6637a], esi
002609A6  0F 85 BD 02 00 00               jne 0x140260c69
002609AC  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002609B5  4C 8B 6D A0                     mov r13, qword ptr [rbp - 0x60]
002609B9  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
002609BD  49 8B 45 00                     mov rax, qword ptr [r13]
002609C1  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
002609C5  49 8D 45 18                     lea rax, [r13 + 0x18]
002609C9  48 8B C8                        mov rcx, rax
002609CC  4C 89 6D 88                     mov qword ptr [rbp - 0x78], r13
002609D0  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002609D5  E8 B6 12 FF FF                  call 0x140251c90
002609DA  4D 8D 4D 18                     lea r9, [r13 + 0x18]
002609DE  41 89 7D 1C                     mov dword ptr [r13 + 0x1c], edi
002609E2  4D 8B 69 08                     mov r13, qword ptr [r9 + 8]
002609E6  49 8D 41 08                     lea rax, [r9 + 8]
002609EA  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
002609EF  4C 3B E8                        cmp r13, rax
002609F2  74 5D                           je 0x140260a51
002609F4  49 8B 55 00                     mov rdx, qword ptr [r13]
002609F8  49 8B C5                        mov rax, r13
002609FB  4C 8B EA                        mov r13, rdx
002609FE  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00260A02  48 39 42 08                     cmp qword ptr [rdx + 8], rax
00260A06  0F 85 4D F8 FF FF               jne 0x140260259
00260A0C  48 39 01                        cmp qword ptr [rcx], rax
00260A0F  0F 85 44 F8 FF FF               jne 0x140260259
00260A15  48 89 11                        mov qword ptr [rcx], rdx
00260A18  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00260A1C  0F B6 48 10                     movzx ecx, byte ptr [rax + 0x10]
00260A20  40 3A CF                        cmp cl, dil
00260A23  0F 85 51 02 00 00               jne 0x140260c7a
00260A29  44 0F B7 40 12                  movzx r8d, word ptr [rax + 0x12]
00260A2E  45 33 C9                        xor r9d, r9d
00260A31  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00260A35  48 8B D0                        mov rdx, rax
00260A38  E8 93 FC 0E 00                  call 0x1403506d0
00260A3D  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
00260A42  84 C0                           test al, al
00260A44  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00260A49  74 A4                           je 0x1402609ef
00260A4B  41 29 79 04                     sub dword ptr [r9 + 4], edi
00260A4F  75 9E                           jne 0x1402609ef
00260A51  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00260A55  F0 81 60 18 7F FF FF FF         lock and dword ptr [rax + 0x18], 0xffffff7f
00260A5D  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
00260A61  48 3B 45 A0                     cmp rax, qword ptr [rbp - 0x60]
00260A65  0F 85 53 02 00 00               jne 0x140260cbe
00260A6B  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
00260A6F  49 8B CD                        mov rcx, r13
00260A72  49 8B 55 08                     mov rdx, qword ptr [r13 + 8]
00260A76  E8 AD 86 FB FF                  call 0x140219128
00260A7B  44 8B 4C 24 68                  mov r9d, dword ptr [rsp + 0x68]
00260A80  45 85 C9                        test r9d, r9d
00260A83  0F 85 E2 02 00 00               jne 0x140260d6b
00260A89  45 84 F7                        test r15b, r14b
00260A8C  0F 85 C8 02 00 00               jne 0x140260d5a
00260A92  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00260A97  44 8B C7                        mov r8d, edi
00260A9A  33 D2                           xor edx, edx
00260A9C  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00260AA0  49 8B CD                        mov rcx, r13
00260AA3  E8 48 12 FF FF                  call 0x140251cf0
00260AA8  E9 D1 FA FF FF                  jmp 0x14026057e
00260AAD  8B C6                           mov eax, esi
00260AAF  E9 20 F3 FF FF                  jmp 0x14025fdd4
00260AB4  41 0F 0D 08                     prefetchw byte ptr [r8]
00260AB8  41 8B 00                        mov eax, dword ptr [r8]
00260ABB  8B D0                           mov edx, eax
00260ABD  0F BA F2 15                     btr edx, 0x15
00260AC1  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00260AC6  75 F3                           jne 0x140260abb
00260AC8  0F BA E0 15                     bt eax, 0x15
00260ACC  0F 83 77 F2 FF FF               jae 0x14025fd49
00260AD2  E8 F9 26 00 00                  call 0x1402631d0
00260AD7  E9 6D F2 FF FF                  jmp 0x14025fd49
00260ADC  41 81 F8 52 00 01 00            cmp r8d, 0x10052
00260AE3  0F 85 FE F7 FF FF               jne 0x1402602e7
00260AE9  44 89 7F 20                     mov dword ptr [rdi + 0x20], r15d
00260AED  E9 F5 F7 FF FF                  jmp 0x1402602e7
00260AF2  48 89 10                        mov qword ptr [rax], rdx
00260AF5  48 89 42 08                     mov qword ptr [rdx + 8], rax
00260AF9  E9 46 FE FF FF                  jmp 0x140260944
00260AFE  41 0F B6 D7                     movzx edx, r15b
00260B02  0F B6 C8                        movzx ecx, al
00260B05  E8 F2 4B 29 00                  call 0x1404f56fc
00260B0A  E9 DD F6 FF FF                  jmp 0x1402601ec
00260B0F  41 3A C7                        cmp al, r15b
00260B12  0F 85 B8 02 00 00               jne 0x140260dd0
00260B18  C6 41 11 05                     mov byte ptr [rcx + 0x11], 5
00260B1C  48 8B D1                        mov rdx, rcx
00260B1F  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
00260B23  E8 08 90 FB FF                  call 0x140219b30
00260B28  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
00260B2D  45 29 71 04                     sub dword ptr [r9 + 4], r14d
00260B31  0F 84 AE FD FF FF               je 0x1402608e5
00260B37  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00260B3C  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00260B41  E9 EC F6 FF FF                  jmp 0x140260232
00260B46  41 0F 0D 08                     prefetchw byte ptr [r8]
00260B4A  41 8B 00                        mov eax, dword ptr [r8]
00260B4D  8B D0                           mov edx, eax
00260B4F  0F BA F2 15                     btr edx, 0x15
00260B53  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00260B58  75 F3                           jne 0x140260b4d
00260B5A  0F BA E0 15                     bt eax, 0x15
00260B5E  0F 83 23 FD FF FF               jae 0x140260887
00260B64  E8 67 26 00 00                  call 0x1402631d0
00260B69  E9 19 FD FF FF                  jmp 0x140260887
00260B6E  48 8B C1                        mov rax, rcx
00260B71  48 8B 09                        mov rcx, qword ptr [rcx]
00260B74  E9 87 F6 FF FF                  jmp 0x140260200
00260B79  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00260B7D  48 39 02                        cmp qword ptr [rdx], rax
00260B80  0F 85 42 F6 FF FF               jne 0x1402601c8
00260B86  48 89 01                        mov qword ptr [rcx], rax
00260B89  48 89 51 08                     mov qword ptr [rcx + 8], rdx
00260B8D  48 89 0A                        mov qword ptr [rdx], rcx
00260B90  48 89 48 08                     mov qword ptr [rax + 8], rcx
00260B94  FF 4B 4C                        dec dword ptr [rbx + 0x4c]
00260B97  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
00260B9B  41 8B CC                        mov ecx, r12d
00260B9E  E9 C9 F0 FF FF                  jmp 0x14025fc6c
00260BA3  48 8D 4B 28                     lea rcx, [rbx + 0x28]
00260BA7  E8 C4 21 1D 00                  call 0x140432d70
00260BAC  48 85 C0                        test rax, rax
00260BAF  74 0F                           je 0x140260bc0
00260BB1  48 8B 78 10                     mov rdi, qword ptr [rax + 0x10]
00260BB5  48 89 40 08                     mov qword ptr [rax + 8], rax
00260BB9  48 89 00                        mov qword ptr [rax], rax
00260BBC  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00260BC0  FF 4B 4C                        dec dword ptr [rbx + 0x4c]
00260BC3  B8 80 00 00 00                  mov eax, 0x80
00260BC8  66 09 43 1A                     or word ptr [rbx + 0x1a], ax
00260BCC  41 8B CC                        mov ecx, r12d
00260BCF  E9 B6 F8 FF FF                  jmp 0x14026048a
00260BD4  41 8B 87 F0 8E 00 00            mov eax, dword ptr [r15 + 0x8ef0]
00260BDB  33 D2                           xor edx, edx
00260BDD  41 03 87 EC 8E 00 00            add eax, dword ptr [r15 + 0x8eec]
00260BE4  F7 35 2E DF BA 00               div dword ptr [rip + 0xbadf2e]
00260BEA  85 D2                           test edx, edx
00260BEC  0F 85 C3 F6 FF FF               jne 0x1402602b5
00260BF2  44 8B 54 24 40                  mov r10d, dword ptr [rsp + 0x40]
00260BF7  44 89 45 D0                     mov dword ptr [rbp - 0x30], r8d
00260BFB  48 89 5D C8                     mov qword ptr [rbp - 0x38], rbx
00260BFF  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00260C03  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
00260C07  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00260C0A  89 45 C0                        mov dword ptr [rbp - 0x40], eax
00260C0D  4C 89 4D B0                     mov qword ptr [rbp - 0x50], r9
00260C11  48 8B 07                        mov rax, qword ptr [rdi]
00260C14  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00260C18  44 2B 57 2C                     sub r10d, dword ptr [rdi + 0x2c]
00260C1C  44 89 55 D4                     mov dword ptr [rbp - 0x2c], r10d
00260C20  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00260C29  8B 88 10 05 00 00               mov ecx, dword ptr [rax + 0x510]
00260C2F  48 8D 45 A8                     lea rax, [rbp - 0x58]
00260C33  89 4D C4                        mov dword ptr [rbp - 0x3c], ecx
00260C36  41 B9 2B 05 00 00               mov r9d, 0x52b
00260C3C  C7 44 24 20 02 18 60 01         mov dword ptr [rsp + 0x20], 0x1601802
00260C44  41 B8 00 00 02 20               mov r8d, 0x20020000
00260C4A  48 89 45 08                     mov qword ptr [rbp + 8], rax
00260C4E  BA 01 00 00 00                  mov edx, 1
00260C53  48 C7 45 10 30 00 00 00         mov qword ptr [rbp + 0x10], 0x30
00260C5B  48 8D 4D 08                     lea rcx, [rbp + 8]
00260C5F  E8 EC 46 FD FF                  call 0x140235350
00260C64  E9 7B F6 FF FF                  jmp 0x1402602e4
00260C69  41 0F B6 D7                     movzx edx, r15b
00260C6D  0F B6 C8                        movzx ecx, al
00260C70  E8 87 4A 29 00                  call 0x1404f56fc
00260C75  E9 32 FD FF FF                  jmp 0x1402609ac
00260C7A  41 3A CF                        cmp cl, r15b
00260C7D  0F 85 C1 01 00 00               jne 0x140260e44
00260C83  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
00260C87  48 8B D0                        mov rdx, rax
00260C8A  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00260C8E  E8 9D 8E FB FF                  call 0x140219b30
00260C93  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
00260C98  41 29 79 04                     sub dword ptr [r9 + 4], edi
00260C9C  0F 84 AF FD FF FF               je 0x140260a51
00260CA2  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00260CA7  E9 43 FD FF FF                  jmp 0x1402609ef
00260CAC  41 83 FE 01                     cmp r14d, 1
00260CB0  B8 01 00 00 00                  mov eax, 1
00260CB5  44 0F 44 E8                     cmove r13d, eax
00260CB9  E9 64 FC FF FF                  jmp 0x140260922
00260CBE  4C 8B E8                        mov r13, rax
00260CC1  48 8B 00                        mov rax, qword ptr [rax]
00260CC4  E9 F8 FC FF FF                  jmp 0x1402609c1
00260CC9  41 3B C5                        cmp eax, r13d
00260CCC  45 8B F7                        mov r14d, r15d
00260CCF  44 0F 4F E8                     cmovg r13d, eax
00260CD3  E9 41 FC FF FF                  jmp 0x140260919
00260CD8  41 8B 85 F0 8E 00 00            mov eax, dword ptr [r13 + 0x8ef0]
00260CDF  33 D2                           xor edx, edx
00260CE1  41 03 85 EC 8E 00 00            add eax, dword ptr [r13 + 0x8eec]
00260CE8  F7 35 2A DE BA 00               div dword ptr [rip + 0xbade2a]
00260CEE  85 D2                           test edx, edx
00260CF0  0F 85 AE FA FF FF               jne 0x1402607a4
00260CF6  44 8B 54 24 40                  mov r10d, dword ptr [rsp + 0x40]
00260CFB  44 89 45 00                     mov dword ptr [rbp], r8d
00260CFF  48 89 5D F8                     mov qword ptr [rbp - 8], rbx
00260D03  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00260D07  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00260D0B  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00260D0E  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00260D11  4C 89 4D E0                     mov qword ptr [rbp - 0x20], r9
00260D15  48 8B 07                        mov rax, qword ptr [rdi]
00260D18  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00260D1C  44 2B 57 2C                     sub r10d, dword ptr [rdi + 0x2c]
00260D20  44 89 55 04                     mov dword ptr [rbp + 4], r10d
00260D24  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00260D2D  8B 88 10 05 00 00               mov ecx, dword ptr [rax + 0x510]
00260D33  48 8D 45 D8                     lea rax, [rbp - 0x28]
00260D37  89 4D F4                        mov dword ptr [rbp - 0xc], ecx
00260D3A  E9 F7 FE FF FF                  jmp 0x140260c36
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00260366(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, unsigned int a8, unsigned __int8 a9, __int64 a10, unsigned __int8 a11, unsigned int a12, unsigned int a13, unsigned int a14, __int64 a15)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rdi;
    unsigned int v_stack_p0;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int16 v_stack_p70;
    unsigned __int64 v_stack_p78;

    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - (*(unsigned int *)(v_rbx + 16)));
    result = (result) >> (4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1120) = (unsigned __int8)(result);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 8))) & (7));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8))))) >> (3));
    result = (unsigned int)((result * 8 - 8) | ((unsigned int)(a1)));
    *(unsigned int *)(v_rdi + 8) = (unsigned int)(result);
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (3));
    v_stack_p60 = (unsigned int)(v_r14);
    if ((unsigned int)(v_r14) != 0) goto loc_0026058F;
    if ((((unsigned __int8)(v_r15)) & ((unsigned __int8)(result))) == 0) goto loc_0026088D;
    v_r14 = (*(unsigned __int64 *)(v_rdi)) & (-4);
loc_002603C0:
    if (v_r14 == 0) goto loc_00260461;
    if (((1) & ((unsigned __int8)(result))) == 0) goto loc_00260410;
    v_r12 = 0;
    v_r13 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 8))) & (0xFFFFFFFEULL));
    *(unsigned int *)(v_rdi + 8) = (unsigned int)(result);
loc_00260410:
    if ((((unsigned __int8)(result)) & (4)) != 0) {
        result = *(unsigned int *)(v_rdi + 8);
        result = (unsigned int)((result) & (0xFFFFFFFBULL));
        *(unsigned int *)(v_rdi + 8) = (unsigned int)(result);
    }
    if ((((unsigned __int8)(v_r15)) & ((unsigned __int8)(result))) == 0) goto loc_00260461;
    if ((*(unsigned int *)(v_rip + 14044128)) != ((unsigned int)(v_rsi))) {
        a4 = 0x746C6644ULL;
        a1 = v_r14 - 48;
        a3 = 1;
        a2 = 0;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    result = (-1) - (1);
loc_00260461:
    *(unsigned __int64 *)(v_rdi) = v_rsi;
    v_stack_p40 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 68)));
    if ((*(unsigned int *)(v_rbx + 64)) > 1) goto loc_00260488;
    if ((*(unsigned int *)(v_rbx + 76)) != ((unsigned int)(v_rsi))) goto loc_00260BA3;
loc_00260488:
loc_0026048A:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 64))) - 1);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) + ((unsigned int)(result)));
    *(unsigned int *)(v_rbx + 64) = (unsigned int)(a1);
    if (!(condition_is_not_equal)) {
        *(unsigned __int16 *)(v_rbx + 24) = (unsigned __int16)(v_rsi);
    }
    if ((*(unsigned int *)(v_rbx + 76)) != ((unsigned int)(v_rsi))) goto loc_002604AD;
    if ((*(unsigned int *)(v_rbx + 72)) == ((unsigned int)(v_rsi))) {
        a1 = 249;
    }
    v_stack_p68 = (unsigned int)(*(unsigned __int8 *)(v_rbx + 27));
    result = *(unsigned __int8 *)(v_rbx + 27);
    if (v_rsi != 0) {
        result = *(unsigned int *)(v_rbx + 56);
        result = (unsigned int)((result) & (7));
        *(unsigned __int64 *)(v_rbx + 48) = v_rsi;
        result = (unsigned int)((result) | (8));
        *(unsigned int *)(v_rbx + 56) = (unsigned int)(result);
    }
    if (((*(unsigned __int8 *)(v_rip + 14050869)) & (1)) != 0) goto loc_00260526;
loc_002604D3:
    if (a9 != 0) goto loc_00260505;
    if (a9 == a9) goto loc_0026053E;
    result = KxWaitForLockChainValid(a9, a2, a3, a4);
loc_00260505:
    v_stack_p48 = v_rsi;
    result = (unsigned __int8)((a10) ^ ((unsigned __int8)(a10)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0026053E;
    result = KeWakeAddressAll(result + 8, a10, a3, a4);
    goto loc_0026053E;
loc_00260526:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13293868))) != 0) goto loc_002604D3;
    result = KiReleaseQueuedSpinLockInstrumented(a9, *(unsigned __int64 *)(v_rbp + 72), a3, a4);
loc_0026053E:
    if ((*(unsigned int *)(v_rip + 14051292)) != ((unsigned int)(v_rsi))) {
        a1 = v_cr8;
        a2 = a11;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_r14 = 1;
    if (v_rsi != 0) { v_r14 = 3; }
    if ((*(unsigned __int64 *)(v_rbp - 96)) != v_rsi) goto loc_00260993;
loc_0026057E:
    v_stack_p60 = (unsigned int)(v_rsi);
    v_stack_p38 = (unsigned int)((unsigned int)(0x10042ULL));
    goto loc_002605EA;
loc_0026058F:
    v_stack_p38 = (unsigned int)((unsigned int)(0x10052ULL));
    v_stack_p40 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 68)));
    if (((*(unsigned __int8 *)(v_rip + 14050672)) & (3)) == 0) goto loc_002607E6;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13293730))) != 0) goto loc_002607E6;
    result = KiReleaseQueuedSpinLockInstrumented(a9, *(unsigned __int64 *)(v_rbp + 72), a3, a4);
loc_002605CC:
    if ((*(unsigned int *)(v_rip + 14051150)) != ((unsigned int)(v_rsi))) {
        a1 = a11;
        a2 = a11;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
loc_002605EA:
    *(unsigned __int64 *)(v_rbp - 40) = v_xmm0;
    *(unsigned __int64 *)(v_rbp - 24) = v_xmm0;
    *(unsigned __int64 *)(v_rbp - 8) = v_xmm0;
    a2 = (a2) << (32);
    result = (result) | (a2);
    *(unsigned __int64 *)(v_rbp - 120) = result;
    v_stack_p70 = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    v_stack_p30 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x10052ULL)))) & (0xFFFF0000ULL));
    v_stack_p78 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_p68 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12615133)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) != 0) goto loc_002606EB;
    result = ExAllocatePool2(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) + 72, 512, (unsigned int)(0x72546552ULL), a4);
    *(unsigned __int64 *)(result + 16) = v_rbx;
    *(unsigned int *)(result + 28) = (unsigned int)(v_r12);
    *(unsigned int *)(result + 32) = (unsigned int)(v_rsi);
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(a13));
    result = 0;
    if (condition_is_equal) goto loc_00260759;
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, (unsigned int)(0x72546552ULL), a4);
loc_002606EB:
loc_002606F0:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rsi)))) >= 8) goto loc_00260728;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28)))) != ((unsigned int)(v_r12))) goto loc_0026070A;
    if ((*(unsigned __int64 *)(0 + 16)) != v_rbx) goto loc_0026070A;
    if ((*(unsigned int *)(0 + 40)) == ((unsigned int)((unsigned int)(a13)))) goto loc_0026074D;
loc_0026070A:
    if (v_rsi != 0) goto loc_002607DB;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28))) == 0) goto loc_002607D8;
    if ((*(unsigned int *)(0 + 40)) >= ((unsigned int)((unsigned int)(a13)))) goto loc_002607DB;
loc_00260728:
    if (0 != 0) {
        *(unsigned __int64 *)(0 + 16) = v_rbx;
        *(unsigned int *)(0 + 28) = (unsigned int)(v_r12);
        *(unsigned __int64 *)(0 + 32) = v_rsi;
        *(unsigned __int64 *)(0) = v_rsi;
        *(unsigned __int64 *)(0 + 8) = v_rsi;
        *(unsigned int *)(0 + 24) = (unsigned int)(v_rsi);
        *(unsigned int *)(0 + 40) = (unsigned int)((unsigned int)(a13));
        *(unsigned int *)(0 + 44) = (unsigned int)(v_rsi);
    }
loc_00260759:
    result = (unsigned int)(((unsigned int)(a12)) + 1);
    if (((unsigned int)((unsigned int)(a7))) != 0x10042ULL) goto loc_00260ADC;
    if ((*(unsigned __int64 *)(0)) > 1) goto loc_00260CD8;
loc_002607A4:
    a2 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36592))) + (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36588)));
    goto loc_00260CFB;
loc_002607D8:
loc_002607DB:
    v_r14 = (0) + (64);
    a2 = (unsigned int)((a2) + 1);
    goto loc_002606F0;
loc_002607E6:
    if (a9 != 0) goto loc_0026081C;
    if (a9 == a9) goto loc_002605CC;
    result = KxWaitForLockChainValid(a9, a2, (unsigned int)(a7), v_rsi);
loc_0026081C:
    v_stack_p48 = v_rsi;
    result = (unsigned __int8)((a10) ^ ((unsigned __int8)(a10)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_002605CC;
    a3 = (result + 8) >> (5);
    a3 = (unsigned int)((a3) & (127));
    result = KeDisableInterrupts(a10, a2, a3, v_rsi);
    result = KiHaltOnAddressWakeEntireList(a10, v_rsi, a3, v_rsi);
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_002605CC;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00260B46;
loc_00260887:
    goto loc_002605CC;
loc_0026088D:
    if ((((unsigned __int8)(v_r14)) & (3)) != 0) goto loc_00260461;
    goto loc_002603C0;
loc_00260993:
    v_stack_p78 = a11;
    if ((*(unsigned int *)(v_rip + 14050170)) != ((unsigned int)(v_rsi))) goto loc_00260C69;
loc_002609AC:
    *(unsigned __int64 *)(v_rbp - 128) = *(unsigned __int64 *)(gs_base + (0 + 32));
loc_002609C1:
    *(unsigned __int64 *)(v_rbp - 104) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 96));
    *(unsigned __int64 *)(v_rbp - 120) = *(unsigned __int64 *)(v_rbp - 96);
    v_stack_p38 = *(unsigned __int64 *)(v_rbp - 96) + 24;
    result = KiAcquireKobjectLockSafe(*(unsigned __int64 *)(v_rbp - 96) + 24, v_rsi, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), v_rsi);
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp - 96) + 28) = (unsigned int)((unsigned __int8)(result));
    v_stack_p60 = *(unsigned __int64 *)(v_rbp - 96) + 24 + 8;
loc_002609EF:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 96) + 24 + 8)) == (*(unsigned __int64 *)(v_rbp - 96) + 24 + 8)) goto loc_00260A51;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 96) + 24 + 8) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 96) + 24 + 8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 96) + 24 + 8)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 96) + 24 + 8) + 8);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 96) + 24 + 8) + 16))) != ((unsigned __int8)((unsigned __int8)(result)))) goto loc_00260C7A;
    a4 = 0;
    result = KiTryUnwaitThread(*(unsigned __int64 *)(v_rbp - 128), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 96) + 24 + 8), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 96) + 24 + 8) + 18), a4);
    if ((unsigned __int8)(result) == 0) goto loc_002609EF;
    if ((unsigned __int8)(result) != 0) goto loc_002609EF;
loc_00260A51:
    if ((*(unsigned __int64 *)(v_rbp - 104)) != (*(unsigned __int64 *)(v_rbp - 96))) goto loc_00260CBE;
    result = KiRemoveBoostThread(*(unsigned __int64 *)(v_rbp - 128), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 128) + 8), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 96) + 24 + 8) + 18), a7);
    a2 = 0;
    v_stack_p20 = (unsigned __int8)(a15);
    result = KiExitDispatcher(*(unsigned __int64 *)(v_rbp - 128), a2, (unsigned int)((unsigned int)((unsigned __int8)(result))), (unsigned int)(a13));
    goto loc_0026057E;
loc_00260ADC:
    *(unsigned int *)((unsigned __int8)(result) + 32) = (unsigned int)(v_r15);
loc_00260B46:
loc_00260B4D:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned __int8)(result))))) != 0x10052ULL) goto loc_00260B4D;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned __int8)(result))))) >= 0x10052ULL) goto loc_00260887;
    result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(v_rbp - 128), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int8)(result))))))), (unsigned int)((unsigned int)((unsigned __int8)(result))), (unsigned int)(a13));
    goto loc_00260887;
loc_00260BA3:
    result = RtlRemoveHeadCircularList(v_rbx + 40, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int8)(result))))))), (unsigned int)((unsigned int)((unsigned __int8)(result))), (unsigned int)(a13));
    v_rdi = (unsigned __int8)(result);
    if (result != 0) {
        v_rdi = *(unsigned __int64 *)(result + 16);
        *(unsigned __int64 *)(result + 8) = result;
        *(unsigned __int64 *)(result) = result;
        *(unsigned __int64 *)(v_rbp - 96) = result;
    }
    goto loc_0026048A;
loc_00260C36:
    v_stack_p20 = 0x1601802ULL;
    *(unsigned __int64 *)(v_rbp + 8) = 128;
    *(unsigned __int64 *)(v_rbp + 16) = 48;
    result = EtwTraceKernelEvent(v_rbp + 8, 1, (unsigned int)(0x20020000ULL), (unsigned int)(0x52BULL));
loc_00260C69:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(result), (unsigned __int8)(v_r15), (unsigned int)(0x20020000ULL), (unsigned int)(0x52BULL));
    goto loc_002609AC;
loc_00260C7A:
    *(unsigned __int8 *)(result + 17) = 5;
    result = KiInsertQueueInternal(*(unsigned __int64 *)(result + 24), result, (unsigned int)(0x20020000ULL), (unsigned int)(0x52BULL));
    if (((unsigned __int8)((unsigned __int8)(result))) == ((unsigned __int8)(v_r15))) goto loc_00260A51;
    goto loc_002609EF;
loc_00260CBE:
    goto loc_002609C1;
loc_00260CD8:
    a2 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a12 + 36592))) + (*(unsigned int *)(a12 + 36588)));
    if (0 != 0) goto loc_002607A4;
loc_00260CFB:
    *(unsigned int *)(v_rbp) = (unsigned int)((unsigned int)(0x20020000ULL));
    *(unsigned __int64 *)(v_rbp - 8) = v_rbx;
    *(unsigned __int64 *)(v_rbp - 40) = *(unsigned __int64 *)(v_rdi + 8);
    *(unsigned int *)(v_rbp - 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 36)));
    *(unsigned __int64 *)(v_rbp - 32) = a7;
    *(unsigned __int64 *)(v_rbp - 24) = *(unsigned __int64 *)(v_rdi);
    v_r10 = (unsigned int)(((unsigned int)(a8)) - (*(unsigned int *)(v_rdi + 44)));
    *(unsigned int *)(v_rbp + 4) = (unsigned int)(v_r10);
    *(unsigned int *)(v_rbp - 12) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1296)));
    goto loc_00260C36;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00260366(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, void *Arg7, uint32_t Arg8, uint8_t Arg9, void *Arg10, uint8_t Arg11, uint32_t Arg12, uint32_t Arg13, uint32_t Arg14, void *Arg15)
{
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg10 = (uint8_t *)Arg10;
    uint8_t *arg15 = (uint8_t *)Arg15;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rdi;
    uint32_t v_stack_p0;
    uint8_t v_stack_p20;
    uint8_t v_stack_p30;
    uint32_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p60;
    uint32_t v_stack_p68;
    uint16_t v_stack_p70;
    uint64_t v_stack_p78;

    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - (*(uint32_t *)(local_rbx + 0x10)));
    result = (result) >> (4);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x460) = (uint8_t)(result);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) & (7));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8))))) >> (3));
    result = (uint32_t)((result * 8 - 8) | ((uint32_t)(Arg1)));
    *(uint32_t *)(local_rdi + 0x8) = (uint32_t)(result);
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (3));
    v_stack_p60 = (uint32_t)(local_r14);
    if ((uint32_t)(local_r14) != 0) goto loc_0026058F;
    if ((((uint8_t)(local_r15)) & ((uint8_t)(result))) == 0) goto loc_0026088D;
    local_r14 = (*(uint64_t *)(local_rdi)) & (-4);
loc_002603C0:
    if (local_r14 == 0) goto loc_00260461;
    if (((1) & ((uint8_t)(result))) == 0) goto loc_00260410;
    local_r12 = 0;
    local_r13 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) & (0xFFFFFFFEULL));
    *(uint32_t *)(local_rdi + 0x8) = (uint32_t)(result);
loc_00260410:
    if ((((uint8_t)(result)) & (4)) != 0) {
        result = *(uint32_t *)(local_rdi + 0x8);
        result = (uint32_t)((result) & (0xFFFFFFFBULL));
        *(uint32_t *)(local_rdi + 0x8) = (uint32_t)(result);
    }
    if ((((uint8_t)(local_r15)) & ((uint8_t)(result))) == 0) goto loc_00260461;
    if ((*(uint32_t *)(v_rip + 0xD64BE0)) != ((uint32_t)(local_rsi))) {
        Arg4 = 0x746C6644ULL;
        Arg1 = local_r14 - 48;
        Arg3 = 1;
        Arg2 = 0;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    result = (-1) - (1);
loc_00260461:
    *(uint64_t *)(local_rdi) = local_rsi;
    v_stack_p40 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x44)));
    if ((*(uint32_t *)(local_rbx + 0x40)) > 1) goto loc_00260488;
    if ((*(uint32_t *)(local_rbx + 0x4C)) != ((uint32_t)(local_rsi))) goto loc_00260BA3;
loc_00260488:
loc_0026048A:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x40))) - 1);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) + ((uint32_t)(result)));
    *(uint32_t *)(local_rbx + 0x40) = (uint32_t)(Arg1);
    if (!(condition_is_not_equal)) {
        *(uint16_t *)(local_rbx + 0x18) = (uint16_t)(local_rsi);
    }
    if ((*(uint32_t *)(local_rbx + 0x4C)) != ((uint32_t)(local_rsi))) goto loc_002604AD;
    if ((*(uint32_t *)(local_rbx + 0x48)) == ((uint32_t)(local_rsi))) {
        Arg1 = 249;
    }
    v_stack_p68 = (uint32_t)(*(uint8_t *)(local_rbx + 0x1B));
    result = *(uint8_t *)(local_rbx + 0x1B);
    if (local_rsi != 0) {
        result = *(uint32_t *)(local_rbx + 0x38);
        result = (uint32_t)((result) & (7));
        *(uint64_t *)(local_rbx + 0x30) = local_rsi;
        result = (uint32_t)((result) | (8));
        *(uint32_t *)(local_rbx + 0x38) = (uint32_t)(result);
    }
    if (((*(uint8_t *)(v_rip + 0xD66635)) & (1)) != 0) goto loc_00260526;
loc_002604D3:
    if (Arg9 != 0) goto loc_00260505;
    if (Arg9 == Arg9) goto loc_0026053E;
    result = KxWaitForLockChainValid(Arg9, Arg2, Arg3, Arg4);
loc_00260505:
    v_stack_p48 = local_rsi;
    result = (uint8_t)((Arg10) ^ ((uint8_t)(Arg10)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0026053E;
    result = KeWakeAddressAll(result + 8, Arg10, Arg3, Arg4);
    goto loc_0026053E;
loc_00260526:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAD92C))) != 0) goto loc_002604D3;
    result = KiReleaseQueuedSpinLockInstrumented(Arg9, *(uint64_t *)(local_rbp + 0x48), Arg3, Arg4);
loc_0026053E:
    if ((*(uint32_t *)(v_rip + 0xD667DC)) != ((uint32_t)(local_rsi))) {
        Arg1 = v_cr8;
        Arg2 = Arg11;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    local_r14 = 1;
    if (local_rsi != 0) { local_r14 = 3; }
    if ((*(uint64_t *)(local_rbp - 0x60)) != local_rsi) goto loc_00260993;
loc_0026057E:
    v_stack_p60 = (uint32_t)(local_rsi);
    v_stack_p38 = (uint32_t)((uint32_t)(0x10042ULL));
    goto loc_002605EA;
loc_0026058F:
    v_stack_p38 = (uint32_t)((uint32_t)(0x10052ULL));
    v_stack_p40 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x44)));
    if (((*(uint8_t *)(v_rip + 0xD66570)) & (3)) == 0) goto loc_002607E6;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAD8A2))) != 0) goto loc_002607E6;
    result = KiReleaseQueuedSpinLockInstrumented(Arg9, *(uint64_t *)(local_rbp + 0x48), Arg3, Arg4);
loc_002605CC:
    if ((*(uint32_t *)(v_rip + 0xD6674E)) != ((uint32_t)(local_rsi))) {
        Arg1 = Arg11;
        Arg2 = Arg11;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
loc_002605EA:
    *(uint64_t *)(local_rbp - 0x28) = v_xmm0;
    *(uint64_t *)(local_rbp - 0x18) = v_xmm0;
    *(uint64_t *)(local_rbp - 0x8) = v_xmm0;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    *(uint64_t *)(local_rbp - 0x78) = result;
    v_stack_p70 = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    v_stack_p30 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x10052ULL)))) & (0xFFFF0000ULL));
    v_stack_p78 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_p68 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC07DDD)));
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) != 0) goto loc_002606EB;
    result = ExAllocatePool2(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) + 72, 512, (uint32_t)(0x72546552ULL), Arg4);
    *(uint64_t *)(result + 0x10) = local_rbx;
    *(uint32_t *)(result + 0x1C) = (uint32_t)(local_r12);
    *(uint32_t *)(result + 0x20) = (uint32_t)(local_rsi);
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(Arg13));
    result = 0;
    if (condition_is_equal) goto loc_00260759;
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, (uint32_t)(0x72546552ULL), Arg4);
loc_002606EB:
loc_002606F0:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rsi)))) >= 8) goto loc_00260728;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C)))) != ((uint32_t)(local_r12))) goto loc_0026070A;
    if ((*(uint64_t *)(0 + 0x10)) != local_rbx) goto loc_0026070A;
    if ((*(uint32_t *)(0 + 0x28)) == ((uint32_t)((uint32_t)(Arg13)))) goto loc_0026074D;
loc_0026070A:
    if (local_rsi != 0) goto loc_002607DB;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C))) == 0) goto loc_002607D8;
    if ((*(uint32_t *)(0 + 0x28)) >= ((uint32_t)((uint32_t)(Arg13)))) goto loc_002607DB;
loc_00260728:
    if (0 != 0) {
        *(uint64_t *)(0 + 0x10) = local_rbx;
        *(uint32_t *)(0 + 0x1C) = (uint32_t)(local_r12);
        *(uint64_t *)(0 + 0x20) = local_rsi;
        *(uint64_t *)(0) = local_rsi;
        *(uint64_t *)(0 + 0x8) = local_rsi;
        *(uint32_t *)(0 + 0x18) = (uint32_t)(local_rsi);
        *(uint32_t *)(0 + 0x28) = (uint32_t)((uint32_t)(Arg13));
        *(uint32_t *)(0 + 0x2C) = (uint32_t)(local_rsi);
    }
loc_00260759:
    result = (uint32_t)(((uint32_t)(Arg12)) + 1);
    if (((uint32_t)((uint32_t)(Arg7))) != 0x10042ULL) goto loc_00260ADC;
    if ((*(uint64_t *)(0)) > 1) goto loc_00260CD8;
loc_002607A4:
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EF0))) + (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EEC)));
    goto loc_00260CFB;
loc_002607D8:
loc_002607DB:
    local_r14 = (0) + (64);
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_002606F0;
loc_002607E6:
    if (Arg9 != 0) goto loc_0026081C;
    if (Arg9 == Arg9) goto loc_002605CC;
    result = KxWaitForLockChainValid(Arg9, Arg2, (uint32_t)(Arg7), local_rsi);
loc_0026081C:
    v_stack_p48 = local_rsi;
    result = (uint8_t)((Arg10) ^ ((uint8_t)(Arg10)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_002605CC;
    Arg3 = (result + 8) >> (5);
    Arg3 = (uint32_t)((Arg3) & (127));
    result = KeDisableInterrupts(Arg10, Arg2, Arg3, local_rsi);
    result = KiHaltOnAddressWakeEntireList(Arg10, local_rsi, Arg3, local_rsi);
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_002605CC;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00260B46;
loc_00260887:
    goto loc_002605CC;
loc_0026088D:
    if ((((uint8_t)(local_r14)) & (3)) != 0) goto loc_00260461;
    goto loc_002603C0;
loc_00260993:
    v_stack_p78 = Arg11;
    if ((*(uint32_t *)(v_rip + 0xD6637A)) != ((uint32_t)(local_rsi))) goto loc_00260C69;
loc_002609AC:
    *(uint64_t *)(local_rbp - 0x80) = *(uint64_t *)(gs_base + (0 + 0x20));
loc_002609C1:
    *(uint64_t *)(local_rbp - 0x68) = *(uint64_t *)(*(uint64_t *)(local_rbp - 0x60));
    *(uint64_t *)(local_rbp - 0x78) = *(uint64_t *)(local_rbp - 0x60);
    v_stack_p38 = *(uint64_t *)(local_rbp - 0x60) + 24;
    result = KiAcquireKobjectLockSafe(*(uint64_t *)(local_rbp - 0x60) + 24, local_rsi, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), local_rsi);
    *(uint32_t *)(*(uint64_t *)(local_rbp - 0x60) + 0x1C) = (uint32_t)((uint8_t)(result));
    v_stack_p60 = *(uint64_t *)(local_rbp - 0x60) + 24 + 8;
loc_002609EF:
    if ((*(uint64_t *)(*(uint64_t *)(local_rbp - 0x60) + 0x18 + 0x8)) == (*(uint64_t *)(local_rbp - 0x60) + 24 + 8)) goto loc_00260A51;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x60) + 0x18 + 0x8) + 0x8)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x60) + 0x18 + 0x8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x60) + 0x18 + 0x8)) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x60) + 0x18 + 0x8) + 0x8);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x60) + 0x18 + 0x8) + 0x10))) != ((uint8_t)((uint8_t)(result)))) goto loc_00260C7A;
    Arg4 = 0;
    result = KiTryUnwaitThread(*(uint64_t *)(local_rbp - 0x80), *(uint64_t *)(*(uint64_t *)(local_rbp - 0x60) + 0x18 + 0x8), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x60) + 0x18 + 0x8) + 0x12), Arg4);
    if ((uint8_t)(result) == 0) goto loc_002609EF;
    if ((uint8_t)(result) != 0) goto loc_002609EF;
loc_00260A51:
    if ((*(uint64_t *)(local_rbp - 0x68)) != (*(uint64_t *)(local_rbp - 0x60))) goto loc_00260CBE;
    result = KiRemoveBoostThread(*(uint64_t *)(local_rbp - 0x80), *(uint64_t *)(*(uint64_t *)(local_rbp - 0x80) + 0x8), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x60) + 0x18 + 0x8) + 0x12), Arg7);
    Arg2 = 0;
    v_stack_p20 = (uint8_t)(Arg15);
    result = KiExitDispatcher(*(uint64_t *)(local_rbp - 0x80), Arg2, (uint32_t)((uint32_t)((uint8_t)(result))), (uint32_t)(Arg13));
    goto loc_0026057E;
loc_00260ADC:
    *(uint32_t *)((uint8_t)(result) + 0x20) = (uint32_t)(local_r15);
loc_00260B46:
loc_00260B4D:
    if (((uint32_t)((uint32_t)((uint32_t)((uint8_t)(result))))) != 0x10052ULL) goto loc_00260B4D;
    if (((uint32_t)((uint32_t)((uint32_t)((uint8_t)(result))))) >= 0x10052ULL) goto loc_00260887;
    result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(local_rbp - 0x80), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint8_t)(result))))))), (uint32_t)((uint32_t)((uint8_t)(result))), (uint32_t)(Arg13));
    goto loc_00260887;
loc_00260BA3:
    result = RtlRemoveHeadCircularList(local_rbx + 40, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint8_t)(result))))))), (uint32_t)((uint32_t)((uint8_t)(result))), (uint32_t)(Arg13));
    local_rdi = (uint8_t)(result);
    if (result != 0) {
        local_rdi = *(uint64_t *)(result + 0x10);
        *(uint64_t *)(result + 0x8) = result;
        *(uint64_t *)(result) = result;
        *(uint64_t *)(local_rbp - 0x60) = result;
    }
    goto loc_0026048A;
loc_00260C36:
    v_stack_p20 = 0x1601802ULL;
    *(uint64_t *)(local_rbp + 0x8) = 128;
    *(uint64_t *)(local_rbp + 0x10) = 48;
    result = EtwTraceKernelEvent(local_rbp + 8, 1, (uint32_t)(0x20020000ULL), (uint32_t)(0x52BULL));
loc_00260C69:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(result), (uint8_t)(local_r15), (uint32_t)(0x20020000ULL), (uint32_t)(0x52BULL));
    goto loc_002609AC;
loc_00260C7A:
    *(uint8_t *)(result + 0x11) = 5;
    result = KiInsertQueueInternal(*(uint64_t *)(result + 0x18), result, (uint32_t)(0x20020000ULL), (uint32_t)(0x52BULL));
    if (((uint8_t)((uint8_t)(result))) == ((uint8_t)(local_r15))) goto loc_00260A51;
    goto loc_002609EF;
loc_00260CBE:
    goto loc_002609C1;
loc_00260CD8:
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg12 + 0x8EF0))) + (*(uint32_t *)(Arg12 + 0x8EEC)));
    if (0 != 0) goto loc_002607A4;
loc_00260CFB:
    *(uint32_t *)(local_rbp) = (uint32_t)((uint32_t)(0x20020000ULL));
    *(uint64_t *)(local_rbp - 0x8) = local_rbx;
    *(uint64_t *)(local_rbp - 0x28) = *(uint64_t *)(local_rdi + 0x8);
    *(uint32_t *)(local_rbp - 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x24)));
    *(void **)(local_rbp - 0x20) = Arg7;
    *(uint64_t *)(local_rbp - 0x18) = *(uint64_t *)(local_rdi);
    local_r10 = (uint32_t)(((uint32_t)(Arg8)) - (*(uint32_t *)(local_rdi + 0x2C)));
    *(uint32_t *)(local_rbp + 0x4) = (uint32_t)(local_r10);
    *(uint32_t *)(local_rbp - 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x510)));
    goto loc_00260C36;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg7` | `+ 0x4` | `32` | `R/W` |
| `Arg10` | `+ 0x0` | `64` | `R` |
| `Arg15` | `+ 0x620` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00260366&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
