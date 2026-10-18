# MiDeleteVaDirect

- RVA: `0x00277560`–`0x002789CD` (길이 `5,229` bytes)
- VA: `0x0000000140277560`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065F70`
- 디코드: `1,169`개 명령, `5,229/5,229` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00277701` → [MiFastLockLeafPageTable](MiFastLockLeafPageTable_function_00276340.md) (function, `0x00276340`)
- `0x0027780C` → [MiDeleteVa](MiDeleteVa_function_002789E0.md) (function, `0x002789E0`)
- `0x00277B77` → [EtwTraceShouldYieldProcessor](EtwTraceShouldYieldProcessor_function_00279088.md) (function, `0x00279088`)
- `0x00277C0F` → [MiDecommitPagesTail](MiDecommitPagesTail_function_002790FC.md) (function, `0x002790FC`)
- `0x00277CB7` → [MiReleaseWalkLocks](../23/MiReleaseWalkLocks_function_00239FD0.md) (function, `0x00239FD0`)
- `0x00277CE2` → [MiLockWorkingSetShared](MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002780E4` → [KxTryToAcquireQueuedSpinLock](KxTryToAcquireQueuedSpinLock_function_00277388.md) (function, `0x00277388`)
- `0x00278395` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x002783C2` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x002783DC` → [KiHaltOnAddressWakeEntireList](../21/KiHaltOnAddressWakeEntireList_function_00217AF4.md) (function, `0x00217AF4`)
- `0x00278550` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x002785B0` → [MiLockWorkingSetShared](MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00278624` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0027868F` → [ExReleaseSpinLockRegardlessFromDpcLevel](../23/ExReleaseSpinLockRegardlessFromDpcLevel_function_0023A330.md) (function, `0x0023A330`)
- `0x002786C3` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x002787BD` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x002787D7` → [MiDeleteEmptyPageTable](../47/MiDeleteEmptyPageTable_function_0047FE00.md) (function, `0x0047FE00`)
- `0x002787ED` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x0027880A` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00278856` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0027886E` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00278894` → [MiDeleteEmptyPageTableTail](../48/MiDeleteEmptyPageTableTail_function_00483280.md) (function, `0x00483280`)
- `0x002788B6` → [MiGetLeafVa](MiGetLeafVa_function_0027C0A0.md) (function, `0x0027C0A0`)
- `0x002788DA` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002788F2` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0027890B` → [ExTryAcquireSpinLockExclusiveAtDpcLevel](../2B/ExTryAcquireSpinLockExclusiveAtDpcLevel_function_002BB800.md) (function, `0x002BB800`)
- `0x0027894F` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x0027896F` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)
- `0x002789B6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002789C3` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [MiDeleteEmptyPageTables](../2A/MiDeleteEmptyPageTables_function_002A5220.md) at `0x002A547F`
- [MiDeletePagablePteRange](../2A/MiDeletePagablePteRange_function_002A96B4.md) at `0x002A9865`

### Static image references
- `0x0027757D` → RVA `0x002789E0` (`MiDeleteVa`; read)
- `0x00277854` → RVA `0x00E38840` (`.data`; read)
- `0x00277ACF` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00277B64` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x00277BF5` → RVA `0x00473EF0` (`MiDeleteVaTail`; read)
- `0x00277DDF` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0027832C` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00278537` → RVA `0x00F0DE58` (`.data`; read)
- `0x002787C7` → RVA `0x0047FE00` (`MiDeleteEmptyPageTable`; read)
- `0x00278881` → RVA `0x00483280` (`MiDeleteEmptyPageTableTail`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00277560  4C 8B DC                        mov r11, rsp
00277563  53                              push rbx
00277564  55                              push rbp
00277565  56                              push rsi
00277566  57                              push rdi
00277567  41 54                           push r12
00277569  41 55                           push r13
0027756B  41 56                           push r14
0027756D  41 57                           push r15
0027756F  48 81 EC D8 00 00 00            sub rsp, 0xd8
00277576  48 8B 81 B0 00 00 00            mov rax, qword ptr [rcx + 0xb0]
0027757D  48 8D 15 5C 14 00 00            lea rdx, [rip + 0x145c]
00277584  4C 8B 71 20                     mov r14, qword ptr [rcx + 0x20]
00277588  48 8B D9                        mov rbx, rcx
0027758B  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00277593  45 33 FF                        xor r15d, r15d
00277596  48 39 91 A8 00 00 00            cmp qword ptr [rcx + 0xa8], rdx
0027759D  B8 08 00 00 00                  mov eax, 8
002775A2  45 8B C7                        mov r8d, r15d
002775A5  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
002775AA  44 0F 45 C0                     cmovne r8d, eax
002775AE  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
002775B8  41 8B C7                        mov eax, r15d
002775BB  44 89 84 24 28 01 00 00         mov dword ptr [rsp + 0x128], r8d
002775C3  0F 95 C0                        setne al
002775C6  49 BA F8 FF FF FF 7F 00 00 00   movabs r10, 0x7ffffffff8
002775D0  44 8D 68 01                     lea r13d, [rax + 1]
002775D4  48 8B 81 B8 00 00 00            mov rax, qword ptr [rcx + 0xb8]
002775DB  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
002775E0  48 8B 08                        mov rcx, qword ptr [rax]
002775E3  8B 81 A0 00 00 00               mov eax, dword ptr [rcx + 0xa0]
002775E9  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
002775ED  48 C1 E9 09                     shr rcx, 9
002775F1  49 23 CA                        and rcx, r10
002775F4  89 84 24 30 01 00 00            mov dword ptr [rsp + 0x130], eax
002775FB  49 8B C1                        mov rax, r9
002775FE  48 03 C8                        add rcx, rax
00277601  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00277606  48 C1 E9 09                     shr rcx, 9
0027760A  49 23 CA                        and rcx, r10
0027760D  49 8B C1                        mov rax, r9
00277610  48 03 C8                        add rcx, rax
00277613  49 89 8B 68 FF FF FF            mov qword ptr [r11 - 0x98], rcx
0027761A  48 C1 E9 09                     shr rcx, 9
0027761E  49 23 CA                        and rcx, r10
00277621  49 8B C1                        mov rax, r9
00277624  48 03 C8                        add rcx, rax
00277627  49 89 8B 70 FF FF FF            mov qword ptr [r11 - 0x90], rcx
0027762E  48 C1 E9 09                     shr rcx, 9
00277632  49 23 CA                        and rcx, r10
00277635  49 8B C1                        mov rax, r9
00277638  48 03 C8                        add rcx, rax
0027763B  49 89 8B 78 FF FF FF            mov qword ptr [r11 - 0x88], rcx
00277642  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00277646  48 C1 E9 09                     shr rcx, 9
0027764A  49 23 CA                        and rcx, r10
0027764D  49 8B C1                        mov rax, r9
00277650  48 03 C8                        add rcx, rax
00277653  49 89 4B 90                     mov qword ptr [r11 - 0x70], rcx
00277657  48 C1 E9 09                     shr rcx, 9
0027765B  49 23 CA                        and rcx, r10
0027765E  49 8B C1                        mov rax, r9
00277661  48 03 C8                        add rcx, rax
00277664  49 89 4B 98                     mov qword ptr [r11 - 0x68], rcx
00277668  48 C1 E9 09                     shr rcx, 9
0027766C  49 23 CA                        and rcx, r10
0027766F  49 8B C1                        mov rax, r9
00277672  48 03 C8                        add rcx, rax
00277675  49 89 4B A0                     mov qword ptr [r11 - 0x60], rcx
00277679  48 C1 E9 09                     shr rcx, 9
0027767D  49 23 CA                        and rcx, r10
00277680  49 8B C1                        mov rax, r9
00277683  4A 8B 6C EC 78                  mov rbp, qword ptr [rsp + r13*8 + 0x78]
00277688  48 03 C8                        add rcx, rax
0027768B  49 89 4B A8                     mov qword ptr [r11 - 0x58], rcx
0027768F  4A 8B 84 EC A8 00 00 00         mov rax, qword ptr [rsp + r13*8 + 0xa8]
00277697  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0027769C  48 C7 84 24 38 01 00 00 FF FF FF FF  mov qword ptr [rsp + 0x138], 0xffffffffffffffff
002776A8  48 89 6C 24 58                  mov qword ptr [rsp + 0x58], rbp
002776AD  4D 8B F9                        mov r15, r9
002776B0  49 C1 E7 19                     shl r15, 0x19
002776B4  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
002776B9  49 8B CF                        mov rcx, r15
002776BC  49 BA FF FF FF FF FF F6 FF FF   movabs r10, 0xfffff6ffffffffff
002776C6  48 3B E8                        cmp rbp, rax
002776C9  0F 87 AF 06 00 00               ja 0x140277d7e
002776CF  48 8B D5                        mov rdx, rbp
002776D2  49 8B C1                        mov rax, r9
002776D5  48 3B E8                        cmp rbp, rax
002776D8  72 24                           jb 0x1402776fe
002776DA  66 0F 1F 44 00 00               nop word ptr [rax + rax]
002776E0  49 8B C2                        mov rax, r10
002776E3  48 3B D0                        cmp rdx, rax
002776E6  77 16                           ja 0x1402776fe
002776E8  48 C1 E2 19                     shl rdx, 0x19
002776EC  48 2B D1                        sub rdx, rcx
002776EF  49 8B CF                        mov rcx, r15
002776F2  48 C1 FA 10                     sar rdx, 0x10
002776F6  49 8B C1                        mov rax, r9
002776F9  48 3B D0                        cmp rdx, rax
002776FC  73 E2                           jae 0x1402776e0
002776FE  49 8B CE                        mov rcx, r14
00277701  E8 3A EC FF FF                  call 0x140276340
00277706  44 8B E0                        mov r12d, eax
00277709  85 C0                           test eax, eax
0027770B  0F 84 69 11 00 00               je 0x14027887a
00277711  48 8B FD                        mov rdi, rbp
00277714  48 89 6C 24 40                  mov qword ptr [rsp + 0x40], rbp
00277719  48 C1 E7 19                     shl rdi, 0x19
0027771D  48 8B F5                        mov rsi, rbp
00277720  49 2B FF                        sub rdi, r15
00277723  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
00277728  48 C1 FF 10                     sar rdi, 0x10
0027772C  49 BE 00 00 00 00 80 F6 FF FF   movabs r14, 0xfffff68000000000
00277736  44 3B E8                        cmp r13d, eax
00277739  0F 8C 3A 12 00 00               jl 0x140278979
0027773F  41 83 EC 01                     sub r12d, 1
00277743  0F 85 55 11 00 00               jne 0x14027889e
00277749  48 8D 4E 08                     lea rcx, [rsi + 8]
0027774D  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00277752  49 8B C6                        mov rax, r14
00277755  48 3B C8                        cmp rcx, rax
00277758  72 2A                           jb 0x140277784
0027775A  48 BA FF FF FF FF FF F6 FF FF   movabs rdx, 0xfffff6ffffffffff
00277764  48 8B C2                        mov rax, rdx
00277767  48 3B C8                        cmp rcx, rax
0027776A  77 13                           ja 0x14027777f
0027776C  48 C1 E1 19                     shl rcx, 0x19
00277770  49 2B CF                        sub rcx, r15
00277773  48 C1 F9 10                     sar rcx, 0x10
00277777  49 8B C6                        mov rax, r14
0027777A  48 3B C8                        cmp rcx, rax
0027777D  73 E5                           jae 0x140277764
0027777F  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00277784  49 63 EC                        movsxd rbp, r12d
00277787  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
0027778C  48 89 73 38                     mov qword ptr [rbx + 0x38], rsi
00277790  48 8B 44 EC 78                  mov rax, qword ptr [rsp + rbp*8 + 0x78]
00277795  48 8B 8B B8 00 00 00            mov rcx, qword ptr [rbx + 0xb8]
0027779C  48 3B F8                        cmp rdi, rax
0027779F  4C 8B 8B A8 00 00 00            mov r9, qword ptr [rbx + 0xa8]
002777A6  48 0F 42 F8                     cmovb rdi, rax
002777AA  4C 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], r9
002777B2  4C 8B EF                        mov r13, rdi
002777B5  4C 8B 39                        mov r15, qword ptr [rcx]
002777B8  45 85 E4                        test r12d, r12d
002777BB  75 1B                           jne 0x1402777d8
002777BD  48 8B 84 EC A8 00 00 00         mov rax, qword ptr [rsp + rbp*8 + 0xa8]
002777C5  49 83 E5 F8                     and r13, 0xfffffffffffffff8
002777C9  49 81 CD F8 0F 00 00            or r13, 0xff8
002777D0  4C 3B E8                        cmp r13, rax
002777D3  76 03                           jbe 0x1402777d8
002777D5  4C 8B E8                        mov r13, rax
002777D8  33 F6                           xor esi, esi
002777DA  89 B4 24 20 01 00 00            mov dword ptr [rsp + 0x120], esi
002777E1  49 3B FD                        cmp rdi, r13
002777E4  0F 87 0B 0E 00 00               ja 0x1402785f5
002777EA  45 85 E4                        test r12d, r12d
002777ED  0F 85 98 03 00 00               jne 0x140277b8b
002777F3  48 8D 05 E6 11 00 00            lea rax, [rip + 0x11e6]
002777FA  45 8B C4                        mov r8d, r12d
002777FD  48 8B D7                        mov rdx, rdi
00277800  48 8B CB                        mov rcx, rbx
00277803  4C 3B C8                        cmp r9, rax
00277806  0F 85 BB 0F 00 00               jne 0x1402787c7
0027780C  E8 CF 11 00 00                  call 0x1402789e0
00277811  48 FF 83 A0 00 00 00            inc qword ptr [rbx + 0xa0]
00277818  8B 0B                           mov ecx, dword ptr [rbx]
0027781A  48 8B 93 A0 00 00 00            mov rdx, qword ptr [rbx + 0xa0]
00277821  F6 C1 02                        test cl, 2
00277824  74 7B                           je 0x1402778a1
00277826  84 53 08                        test byte ptr [rbx + 8], dl
00277829  75 76                           jne 0x1402778a1
0027782B  4C 8B 4B 20                     mov r9, qword ptr [rbx + 0x20]
0027782F  83 E1 04                        and ecx, 4
00277832  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00277839  24 0F                           and al, 0xf
0027783B  3C 05                           cmp al, 5
0027783D  0F 87 D0 00 00 00               ja 0x140277913
00277843  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
0027784A  24 0F                           and al, 0xf
0027784C  3C 01                           cmp al, 1
0027784E  0F 85 8D 0F 00 00               jne 0x1402787e1
00277854  48 8D 15 E5 0F BC 00            lea rdx, [rip + 0xbc0fe5]
0027785B  48 8B 12                        mov rdx, qword ptr [rdx]
0027785E  85 C9                           test ecx, ecx
00277860  0F 84 8F 00 00 00               je 0x1402778f5
00277866  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0027786F  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
00277876  48 85 C9                        test rcx, rcx
00277879  74 76                           je 0x1402778f1
0027787B  8B 81 44 01 00 00               mov eax, dword ptr [rcx + 0x144]
00277881  48 C1 E0 06                     shl rax, 6
00277885  8B 04 02                        mov eax, dword ptr [rdx + rax]
00277888  0F BA E0 1E                     bt eax, 0x1e
0027788C  0F 83 81 00 00 00               jae 0x140277913
00277892  C7 84 24 20 01 00 00 02 00 00 00  mov dword ptr [rsp + 0x120], 2
0027789D  EB 02                           jmp 0x1402778a1
0027789F  33 F6                           xor esi, esi
002778A1  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
002778A4  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
002778A9  FF C0                           inc eax
002778AB  89 73 0C                        mov dword ptr [rbx + 0xc], esi
002778AE  48 8D 3C C7                     lea rdi, [rdi + rax*8]
002778B2  48 8B C7                        mov rax, rdi
002778B5  49 89 7F 48                     mov qword ptr [r15 + 0x48], rdi
002778B9  48 C1 E0 19                     shl rax, 0x19
002778BD  48 2B C1                        sub rax, rcx
002778C0  49 89 7F 58                     mov qword ptr [r15 + 0x58], rdi
002778C4  48 C1 F8 10                     sar rax, 0x10
002778C8  83 BC 24 20 01 00 00 02         cmp dword ptr [rsp + 0x120], 2
002778D0  49 89 47 38                     mov qword ptr [r15 + 0x38], rax
002778D4  0F 84 37 06 00 00               je 0x140277f11
002778DA  4C 8B 8C 24 98 00 00 00         mov r9, qword ptr [rsp + 0x98]
002778E2  49 BE 00 00 00 00 80 F6 FF FF   movabs r14, 0xfffff68000000000
002778EC  E9 F0 FE FF FF                  jmp 0x1402777e1
002778F1  8B C6                           mov eax, esi
002778F3  EB 8C                           jmp 0x140277881
002778F5  44 8B C6                        mov r8d, esi
002778F8  41 83 F8 04                     cmp r8d, 4
002778FC  73 15                           jae 0x140277913
002778FE  41 8B C0                        mov eax, r8d
00277901  48 C1 E0 06                     shl rax, 6
00277905  8B 0C 10                        mov ecx, dword ptr [rax + rdx]
00277908  0F BA E1 1E                     bt ecx, 0x1e
0027790C  72 84                           jb 0x140277892
0027790E  41 FF C0                        inc r8d
00277911  EB E5                           jmp 0x1402778f8
00277913  8B 03                           mov eax, dword ptr [rbx]
00277915  A8 04                           test al, 4
00277917  0F 84 B4 00 00 00               je 0x1402779d1
0027791D  4C 8B C7                        mov r8, rdi
00277920  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0027792A  49 C1 E8 09                     shr r8, 9
0027792E  4C 23 C0                        and r8, rax
00277931  49 8B C6                        mov rax, r14
00277934  4C 03 C0                        add r8, rax
00277937  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
00277941  48 8B C0                        mov rax, rax
00277944  4C 3B C0                        cmp r8, rax
00277947  0F 84 48 04 00 00               je 0x140277d95
0027794D  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00277954  A8 0F                           test al, 0xf
00277956  0F 84 FE 00 00 00               je 0x140277a5a
0027795C  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00277963  48 B9 00 D0 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed000
0027796D  A8 0F                           test al, 0xf
0027796F  74 1E                           je 0x14027798f
00277971  48 8B C1                        mov rax, rcx
00277974  4C 3B C0                        cmp r8, rax
00277977  72 16                           jb 0x14027798f
00277979  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
00277983  48 8B C0                        mov rax, rax
00277986  4C 3B C0                        cmp r8, rax
00277989  0F 86 33 04 00 00               jbe 0x140277dc2
0027798F  49 8B 00                        mov rax, qword ptr [r8]
00277992  48 8B C9                        mov rcx, rcx
00277995  4C 3B C1                        cmp r8, rcx
00277998  72 28                           jb 0x1402779c2
0027799A  48 B9 F8 D7 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed7f8
002779A4  48 8B C9                        mov rcx, rcx
002779A7  4C 3B C1                        cmp r8, rcx
002779AA  77 16                           ja 0x1402779c2
002779AC  A8 01                           test al, 1
002779AE  74 12                           je 0x1402779c2
002779B0  A8 42                           test al, 0x42
002779B2  0F 95 C2                        setne dl
002779B5  A8 20                           test al, 0x20
002779B7  0F 95 C1                        setne cl
002779BA  84 D1                           test cl, dl
002779BC  0F 84 0D 01 00 00               je 0x140277acf
002779C2  48 C1 E8 3C                     shr rax, 0x3c
002779C6  83 E0 02                        and eax, 2
002779C9  85 C0                           test eax, eax
002779CB  0F 85 C1 FE FF FF               jne 0x140277892
002779D1  80 7B 09 02                     cmp byte ptr [rbx + 9], 2
002779D5  0F 83 C6 FE FF FF               jae 0x1402778a1
002779DB  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
002779E4  44 8B C6                        mov r8d, esi
002779E7  44 8B CE                        mov r9d, esi
002779EA  8B 91 BC 38 00 00               mov edx, dword ptr [rcx + 0x38bc]
002779F0  8B A9 AC 83 00 00               mov ebp, dword ptr [rcx + 0x83ac]
002779F6  44 8B B1 5C 86 00 00            mov r14d, dword ptr [rcx + 0x865c]
002779FD  F6 C2 01                        test dl, 1
00277A00  0F 85 32 01 00 00               jne 0x140277b38
00277A06  80 79 20 00                     cmp byte ptr [rcx + 0x20], 0
00277A0A  0F 85 04 04 00 00               jne 0x140277e14
00277A10  F6 C2 1E                        test dl, 0x1e
00277A13  0F 85 46 01 00 00               jne 0x140277b5f
00277A19  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
00277A20  84 C0                           test al, al
00277A22  0F 85 13 04 00 00               jne 0x140277e3b
00277A28  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00277A2C  48 85 C0                        test rax, rax
00277A2F  0F 85 CB 03 00 00               jne 0x140277e00
00277A35  83 FD 07                        cmp ebp, 7
00277A38  0F 86 63 FE FF FF               jbe 0x1402778a1
00277A3E  45 85 C0                        test r8d, r8d
00277A41  0F 84 FE 03 00 00               je 0x140277e45
00277A47  F6 C2 1E                        test dl, 0x1e
00277A4A  0F 84 2A 04 00 00               je 0x140277e7a
00277A50  BE 05 00 00 00                  mov esi, 5
00277A55  E9 0A 01 00 00                  jmp 0x140277b64
00277A5A  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
00277A64  48 8B C0                        mov rax, rax
00277A67  4C 3B C0                        cmp r8, rax
00277A6A  0F 82 EC FE FF FF               jb 0x14027795c
00277A70  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
00277A7A  48 8B C0                        mov rax, rax
00277A7D  4C 3B C0                        cmp r8, rax
00277A80  0F 87 D6 FE FF FF               ja 0x14027795c
00277A86  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00277A8F  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00277A96  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
00277A9D  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
00277AA4  48 85 C9                        test rcx, rcx
00277AA7  0F 84 AF FE FF FF               je 0x14027795c
00277AAD  41 C1 E8 03                     shr r8d, 3
00277AB1  8B C6                           mov eax, esi
00277AB3  41 81 E0 FF 01 00 00            and r8d, 0x1ff
00277ABA  42 8B 0C 81                     mov ecx, dword ptr [rcx + r8*4]
00277ABE  0F BA E1 1E                     bt ecx, 0x1e
00277AC2  B9 01 00 00 00                  mov ecx, 1
00277AC7  0F 42 C1                        cmovb eax, ecx
00277ACA  E9 FA FE FF FF                  jmp 0x1402779c9
00277ACF  48 F7 05 AE EF D4 00 00 00 60 00  test qword ptr [rip + 0xd4efae], 0x600000
00277ADA  0F 84 E2 FE FF FF               je 0x1402779c2
00277AE0  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00277AE9  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
00277AF0  80 BA 60 01 00 00 01            cmp byte ptr [rdx + 0x160], 1
00277AF7  0F 84 C5 FE FF FF               je 0x1402779c2
00277AFD  48 8B 8A 08 05 00 00            mov rcx, qword ptr [rdx + 0x508]
00277B04  48 85 C9                        test rcx, rcx
00277B07  0F 84 B5 FE FF FF               je 0x1402779c2
00277B0D  49 C1 E8 03                     shr r8, 3
00277B11  41 81 E0 FF 01 00 00            and r8d, 0x1ff
00277B18  4A 8B 0C C1                     mov rcx, qword ptr [rcx + r8*8]
00277B1C  F6 C1 20                        test cl, 0x20
00277B1F  74 04                           je 0x140277b25
00277B21  48 83 C8 20                     or rax, 0x20
00277B25  48 8B D0                        mov rdx, rax
00277B28  48 83 C8 42                     or rax, 0x42
00277B2C  F6 C1 42                        test cl, 0x42
00277B2F  48 0F 44 C2                     cmove rax, rdx
00277B33  E9 8A FE FF FF                  jmp 0x1402779c2
00277B38  41 BA 01 00 00 00               mov r10d, 1
00277B3E  45 8B C2                        mov r8d, r10d
00277B41  41 83 FE 07                     cmp r14d, 7
00277B45  0F 86 EA FE FF FF               jbe 0x140277a35
00277B4B  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
00277B52  84 C0                           test al, al
00277B54  0F 84 ED FE FF FF               je 0x140277a47
00277B5A  41 8B F2                        mov esi, r10d
00277B5D  EB 05                           jmp 0x140277b64
00277B5F  BE 02 00 00 00                  mov esi, 2
00277B64  F7 05 96 EF D4 00 00 00 00 04   test dword ptr [rip + 0xd4ef96], 0x4000000
00277B6E  74 0C                           je 0x140277b7c
00277B70  45 8B C6                        mov r8d, r14d
00277B73  8B D5                           mov edx, ebp
00277B75  8B CE                           mov ecx, esi
00277B77  E8 0C 15 00 00                  call 0x140279088
00277B7C  85 F6                           test esi, esi
00277B7E  0F 84 1B FD FF FF               je 0x14027789f
00277B84  33 F6                           xor esi, esi
00277B86  E9 07 FD FF FF                  jmp 0x140277892
00277B8B  48 8B 07                        mov rax, qword ptr [rdi]
00277B8E  48 B9 00 D0 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed000
00277B98  48 8B C9                        mov rcx, rcx
00277B9B  48 3B F9                        cmp rdi, rcx
00277B9E  72 28                           jb 0x140277bc8
00277BA0  48 B9 F8 D7 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed7f8
00277BAA  48 8B C9                        mov rcx, rcx
00277BAD  48 3B F9                        cmp rdi, rcx
00277BB0  77 16                           ja 0x140277bc8
00277BB2  A8 01                           test al, 1
00277BB4  74 12                           je 0x140277bc8
00277BB6  A8 42                           test al, 0x42
00277BB8  0F 95 C2                        setne dl
00277BBB  A8 20                           test al, 0x20
00277BBD  0F 95 C1                        setne cl
00277BC0  84 D1                           test cl, dl
00277BC2  0F 84 C6 02 00 00               je 0x140277e8e
00277BC8  48 85 C0                        test rax, rax
00277BCB  0F 84 22 FC FF FF               je 0x1402777f3
00277BD1  A8 01                           test al, 1
00277BD3  0F 85 1A FC FF FF               jne 0x1402777f3
00277BD9  48 8B 6C 24 30                  mov rbp, qword ptr [rsp + 0x30]
00277BDE  BF 05 00 00 00                  mov edi, 5
00277BE3  49 BE 00 00 00 00 80 F6 FF FF   movabs r14, 0xfffff68000000000
00277BED  48 8B B4 24 A0 00 00 00         mov rsi, qword ptr [rsp + 0xa0]
00277BF5  48 8D 05 F4 C2 1F 00            lea rax, [rip + 0x1fc2f4]
00277BFC  48 3B F0                        cmp rsi, rax
00277BFF  0F 85 7C 0C 00 00               jne 0x140278881
00277C05  48 8B 83 B8 00 00 00            mov rax, qword ptr [rbx + 0xb8]
00277C0C  48 8B 08                        mov rcx, qword ptr [rax]
00277C0F  E8 E8 14 00 00                  call 0x1402790fc
00277C14  83 FF 05                        cmp edi, 5
00277C17  0F 84 43 0C 00 00               je 0x140278860
00277C1D  8B 43 04                        mov eax, dword ptr [rbx + 4]
00277C20  8B 0B                           mov ecx, dword ptr [rbx]
00277C22  A8 01                           test al, 1
00277C24  0F 85 64 09 00 00               jne 0x14027858e
00277C2A  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00277C2F  0F BA E1 0B                     bt ecx, 0xb
00277C33  49 BD 00 D0 BE 7D FB F6 FF FF   movabs r13, 0xfffff6fb7dbed000
00277C3D  0F 93 C1                        setae cl
00277C40  F6 84 24 30 01 00 00 80         test byte ptr [rsp + 0x130], 0x80
00277C48  0F 94 C0                        sete al
00277C4B  84 C8                           test al, cl
00277C4D  0F 84 41 03 00 00               je 0x140277f94
00277C53  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
00277C5D  48 8B C0                        mov rax, rax
00277C60  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
00277C65  48 3B F0                        cmp rsi, rax
00277C68  0F 84 2B 0A 00 00               je 0x140278699
00277C6E  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
00277C75  A8 0F                           test al, 0xf
00277C77  0F 84 BB 09 00 00               je 0x140278638
00277C7D  48 B9 FF DF BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbedfff
00277C87  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
00277C8E  A8 0F                           test al, 0xf
00277C90  0F 85 37 0A 00 00               jne 0x1402786cd
00277C96  48 B8 FF FF FF FF FF FF FF CF   movabs rax, 0xcfffffffffffffff
00277CA0  F0 48 21 06                     lock and qword ptr [rsi], rax
00277CA4  45 33 FF                        xor r15d, r15d
00277CA7  4C 89 7B 38                     mov qword ptr [rbx + 0x38], r15
00277CAB  83 FF 02                        cmp edi, 2
00277CAE  0F 85 7A 09 00 00               jne 0x14027862e
00277CB4  48 8B CB                        mov rcx, rbx
00277CB7  E8 14 23 FC FF                  call 0x140239fd0
00277CBC  83 63 04 FE                     and dword ptr [rbx + 4], 0xfffffffe
00277CC0  8B 03                           mov eax, dword ptr [rbx]
00277CC2  48 8B BC 24 38 01 00 00         mov rdi, qword ptr [rsp + 0x138]
00277CCA  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
00277CCE  48 C7 84 24 38 01 00 00 FF FF FF FF  mov qword ptr [rsp + 0x138], 0xffffffffffffffff
00277CDA  A8 04                           test al, 4
00277CDC  0F 84 0B 0B 00 00               je 0x1402787ed
00277CE2  E8 09 4F 00 00                  call 0x14027cbf0
00277CE7  48 8B EF                        mov rbp, rdi
00277CEA  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
00277CF4  48 C1 ED 12                     shr rbp, 0x12
00277CF8  81 E5 F8 FF FF 3F               and ebp, 0x3ffffff8
00277CFE  48 8B C0                        mov rax, rax
00277D01  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00277D06  48 03 E8                        add rbp, rax
00277D09  48 89 6C 24 58                  mov qword ptr [rsp + 0x58], rbp
00277D0E  49 BA F8 FF FF FF 7F 00 00 00   movabs r10, 0x7ffffffff8
00277D18  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
00277D22  41 83 FD 01                     cmp r13d, 1
00277D26  0F 87 EC 0B 00 00               ja 0x140278918
00277D2C  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00277D34  49 8B C1                        mov rax, r9
00277D37  48 3B C8                        cmp rcx, rax
00277D3A  72 39                           jb 0x140277d75
00277D3C  49 8B D1                        mov rdx, r9
00277D3F  48 C1 E2 19                     shl rdx, 0x19
00277D43  49 BA FF FF FF FF FF F6 FF FF   movabs r10, 0xfffff6ffffffffff
00277D4D  0F 1F 00                        nop dword ptr [rax]
00277D50  49 8B C2                        mov rax, r10
00277D53  48 3B C8                        cmp rcx, rax
00277D56  77 13                           ja 0x140277d6b
00277D58  48 C1 E1 19                     shl rcx, 0x19
00277D5C  48 2B CA                        sub rcx, rdx
00277D5F  48 C1 F9 10                     sar rcx, 0x10
00277D63  49 8B C1                        mov rax, r9
00277D66  48 3B C8                        cmp rcx, rax
00277D69  73 E5                           jae 0x140277d50
00277D6B  49 BA F8 FF FF FF 7F 00 00 00   movabs r10, 0x7ffffffff8
00277D75  48 3B F9                        cmp rdi, rcx
00277D78  0F 86 CB 09 00 00               jbe 0x140278749
00277D7E  B0 01                           mov al, 1
00277D80  48 81 C4 D8 00 00 00            add rsp, 0xd8
00277D87  41 5F                           pop r15
00277D89  41 5E                           pop r14
00277D8B  41 5D                           pop r13
00277D8D  41 5C                           pop r12
00277D8F  5F                              pop rdi
00277D90  5E                              pop rsi
00277D91  5D                              pop rbp
00277D92  5B                              pop rbx
00277D93  C3                              ret
00277D94  CC                              int3
00277D95  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00277D9E  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00277DA5  24 0F                           and al, 0xf
00277DA7  0F 85 4C 01 00 00               jne 0x140277ef9
00277DAD  B9 30 00 00 00                  mov ecx, 0x30
00277DB2  48 8B 84 11 40 9C 00 00         mov rax, qword ptr [rcx + rdx + 0x9c40]
00277DBA  48 85 C0                        test rax, rax
00277DBD  E9 09 FC FF FF                  jmp 0x1402779cb
00277DC2  48 8B C1                        mov rax, rcx
00277DC5  4C 2B C0                        sub r8, rax
00277DC8  41 8B 81 B8 00 00 00            mov eax, dword ptr [r9 + 0xb8]
00277DCF  49 C1 F8 03                     sar r8, 3
00277DD3  43 8D 14 00                     lea edx, [r8 + r8]
00277DD7  8B C2                           mov eax, edx
00277DD9  8B CA                           mov ecx, edx
00277DDB  48 C1 E8 05                     shr rax, 5
00277DDF  48 8D 15 1A 82 D8 FF            lea rdx, [rip - 0x277de6]
00277DE6  83 E1 1F                        and ecx, 0x1f
00277DE9  8B 94 82 AC F1 E2 00            mov edx, dword ptr [rdx + rax*4 + 0xe2f1ac]
00277DF0  D3 EA                           shr edx, cl
00277DF2  F6 C2 02                        test dl, 2
00277DF5  0F 84 D6 FB FF FF               je 0x1402779d1
00277DFB  E9 92 FA FF FF                  jmp 0x140277892
00277E00  48 3B 41 08                     cmp rax, qword ptr [rcx + 8]
00277E04  0F 84 2B FC FF FF               je 0x140277a35
00277E0A  BE 04 00 00 00                  mov esi, 4
00277E0F  E9 50 FD FF FF                  jmp 0x140277b64
00277E14  41 B9 01 00 00 00               mov r9d, 1
00277E1A  83 FD 07                        cmp ebp, 7
00277E1D  0F 86 7E FA FF FF               jbe 0x1402778a1
00277E23  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
00277E2A  84 C0                           test al, al
00277E2C  0F 84 15 FC FF FF               je 0x140277a47
00277E32  41 8D 71 06                     lea esi, [r9 + 6]
00277E36  E9 29 FD FF FF                  jmp 0x140277b64
00277E3B  BE 03 00 00 00                  mov esi, 3
00277E40  E9 1F FD FF FF                  jmp 0x140277b64
00277E45  45 85 C9                        test r9d, r9d
00277E48  0F 85 F9 FB FF FF               jne 0x140277a47
00277E4E  FA                              cli
00277E4F  89 B1 AC 83 00 00               mov dword ptr [rcx + 0x83ac], esi
00277E55  89 B1 5C 86 00 00               mov dword ptr [rcx + 0x865c], esi
00277E5B  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00277E64  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00277E6B  4D 85 C0                        test r8, r8
00277E6E  0F 85 92 07 00 00               jne 0x140278606
00277E74  FB                              sti
00277E75  E9 EA FC FF FF                  jmp 0x140277b64
00277E7A  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00277E7E  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00277E82  74 CA                           je 0x140277e4e
00277E84  BE 06 00 00 00                  mov esi, 6
00277E89  E9 D6 FC FF FF                  jmp 0x140277b64
00277E8E  48 F7 05 EF EB D4 00 00 00 60 00  test qword ptr [rip + 0xd4ebef], 0x600000
00277E99  0F 84 29 FD FF FF               je 0x140277bc8
00277E9F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00277EA8  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
00277EAF  80 BA 60 01 00 00 01            cmp byte ptr [rdx + 0x160], 1
00277EB6  0F 84 0C FD FF FF               je 0x140277bc8
00277EBC  4C 8B 82 08 05 00 00            mov r8, qword ptr [rdx + 0x508]
00277EC3  4D 85 C0                        test r8, r8
00277EC6  0F 84 FC FC FF FF               je 0x140277bc8
00277ECC  48 8B CF                        mov rcx, rdi
00277ECF  48 C1 E9 03                     shr rcx, 3
00277ED3  81 E1 FF 01 00 00               and ecx, 0x1ff
00277ED9  49 8B 0C C8                     mov rcx, qword ptr [r8 + rcx*8]
00277EDD  F6 C1 20                        test cl, 0x20
00277EE0  74 04                           je 0x140277ee6
00277EE2  48 83 C8 20                     or rax, 0x20
00277EE6  48 8B D0                        mov rdx, rax
00277EE9  48 83 C8 42                     or rax, 0x42
00277EED  F6 C1 42                        test cl, 0x42
00277EF0  48 0F 44 C2                     cmove rax, rdx
00277EF4  E9 CF FC FF FF                  jmp 0x140277bc8
00277EF9  3C 07                           cmp al, 7
00277EFB  0F 84 26 08 00 00               je 0x140278727
00277F01  3C 05                           cmp al, 5
00277F03  B9 48 00 00 00                  mov ecx, 0x48
00277F08  48 0F 44 CE                     cmove rcx, rsi
00277F0C  E9 A1 FE FF FF                  jmp 0x140277db2
00277F11  48 8B 6C 24 30                  mov rbp, qword ptr [rsp + 0x30]
00277F16  48 3B BC EC A8 00 00 00         cmp rdi, qword ptr [rsp + rbp*8 + 0xa8]
00277F1E  0F 87 92 08 00 00               ja 0x1402787b6
00277F24  48 83 BC 24 38 01 00 00 FF      cmp qword ptr [rsp + 0x138], -1
00277F2D  0F 85 C7 06 00 00               jne 0x1402785fa
00277F33  48 8B D7                        mov rdx, rdi
00277F36  49 BE 00 00 00 00 80 F6 FF FF   movabs r14, 0xfffff68000000000
00277F40  48 89 94 24 38 01 00 00         mov qword ptr [rsp + 0x138], rdx
00277F48  49 8B C6                        mov rax, r14
00277F4B  48 3B F8                        cmp rdi, rax
00277F4E  72 38                           jb 0x140277f88
00277F50  48 BD FF FF FF FF FF F6 FF FF   movabs rbp, 0xfffff6ffffffffff
00277F5A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
00277F60  48 8B C5                        mov rax, rbp
00277F63  48 3B D0                        cmp rdx, rax
00277F66  77 13                           ja 0x140277f7b
00277F68  48 C1 E2 19                     shl rdx, 0x19
00277F6C  48 2B D1                        sub rdx, rcx
00277F6F  48 C1 FA 10                     sar rdx, 0x10
00277F73  49 8B C6                        mov rax, r14
00277F76  48 3B D0                        cmp rdx, rax
00277F79  73 E5                           jae 0x140277f60
00277F7B  48 8B 6C 24 30                  mov rbp, qword ptr [rsp + 0x30]
00277F80  48 89 94 24 38 01 00 00         mov qword ptr [rsp + 0x138], rdx
00277F88  8B BC 24 20 01 00 00            mov edi, dword ptr [rsp + 0x120]
00277F8F  E9 59 FC FF FF                  jmp 0x140277bed
00277F94  41 83 FC 03                     cmp r12d, 3
00277F98  0F 84 B5 FC FF FF               je 0x140277c53
00277F9E  48 8B 16                        mov rdx, qword ptr [rsi]
00277FA1  49 8B C5                        mov rax, r13
00277FA4  48 3B F0                        cmp rsi, rax
00277FA7  72 7E                           jb 0x140278027
00277FA9  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
00277FB3  48 8B C0                        mov rax, rax
00277FB6  48 3B F0                        cmp rsi, rax
00277FB9  77 6C                           ja 0x140278027
00277FBB  F6 C2 01                        test dl, 1
00277FBE  74 67                           je 0x140278027
00277FC0  F6 C2 42                        test dl, 0x42
00277FC3  0F 95 C1                        setne cl
00277FC6  F6 C2 20                        test dl, 0x20
00277FC9  0F 95 C0                        setne al
00277FCC  84 C8                           test al, cl
00277FCE  75 57                           jne 0x140278027
00277FD0  48 F7 05 AD EA D4 00 00 00 60 00  test qword ptr [rip + 0xd4eaad], 0x600000
00277FDB  74 4A                           je 0x140278027
00277FDD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00277FE6  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00277FED  80 B9 60 01 00 00 01            cmp byte ptr [rcx + 0x160], 1
00277FF4  74 31                           je 0x140278027
00277FF6  4C 8B 81 08 05 00 00            mov r8, qword ptr [rcx + 0x508]
00277FFD  4D 85 C0                        test r8, r8
00278000  74 25                           je 0x140278027
00278002  48 8B C6                        mov rax, rsi
00278005  48 C1 E8 03                     shr rax, 3
00278009  25 FF 01 00 00                  and eax, 0x1ff
0027800E  49 8B 04 C0                     mov rax, qword ptr [r8 + rax*8]
00278012  A8 20                           test al, 0x20
00278014  74 04                           je 0x14027801a
00278016  48 83 CA 20                     or rdx, 0x20
0027801A  48 8B CA                        mov rcx, rdx
0027801D  48 83 CA 42                     or rdx, 0x42
00278021  A8 42                           test al, 0x42
00278023  48 0F 44 D1                     cmove rdx, rcx
00278027  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00278031  48 C1 EA 0C                     shr rdx, 0xc
00278035  48 23 D0                        and rdx, rax
00278038  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00278042  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00278046  48 C1 E1 04                     shl rcx, 4
0027804A  48 8B C0                        mov rax, rax
0027804D  48 03 C8                        add rcx, rax
00278050  8B 41 24                        mov eax, dword ptr [rcx + 0x24]
00278053  0F BA E0 1A                     bt eax, 0x1a
00278057  0F 83 91 00 00 00               jae 0x1402780ee
0027805D  48 8B 01                        mov rax, qword ptr [rcx]
00278060  48 C1 E8 20                     shr rax, 0x20
00278064  A9 FF 03 00 00                  test eax, 0x3ff
00278069  0F 85 E4 FB FF FF               jne 0x140277c53
0027806F  4C 8B C6                        mov r8, rsi
00278072  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0027807C  49 C1 E8 09                     shr r8, 9
00278080  4C 23 C0                        and r8, rax
00278083  49 8B C6                        mov rax, r14
00278086  4C 03 C0                        add r8, rax
00278089  48 BF 68 DF BE 7D FB F6 FF FF   movabs rdi, 0xfffff6fb7dbedf68
00278093  48 8B C7                        mov rax, rdi
00278096  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
0027809B  4C 3B C0                        cmp r8, rax
0027809E  0F 85 7B 01 00 00               jne 0x14027821f
002780A4  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
002780AD  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
002780B4  24 0F                           and al, 0xf
002780B6  0F 85 B4 03 00 00               jne 0x140278470
002780BC  B9 02 00 00 00                  mov ecx, 2
002780C1  49 8D 96 B0 00 00 00            lea rdx, [r14 + 0xb0]
002780C8  45 33 FF                        xor r15d, r15d
002780CB  8B C1                           mov eax, ecx
002780CD  48 8D 88 C4 09 00 00            lea rcx, [rax + 0x9c4]
002780D4  48 8D 0C 48                     lea rcx, [rax + rcx*2]
002780D8  49 8D 0C C8                     lea rcx, [r8 + rcx*8]
002780DC  48 89 51 08                     mov qword ptr [rcx + 8], rdx
002780E0  4C 89 39                        mov qword ptr [rcx], r15
002780E3  90                              nop
002780E4  E8 9F F2 FF FF                  call 0x140277388
002780E9  E9 B8 00 00 00                  jmp 0x1402781a6
002780EE  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
002780F2  48 C1 E8 10                     shr rax, 0x10
002780F6  E9 69 FF FF FF                  jmp 0x140278064
002780FB  48 F7 05 82 E9 D4 00 00 00 60 00  test qword ptr [rip + 0xd4e982], 0x600000
00278106  74 4D                           je 0x140278155
00278108  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00278111  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
00278118  80 BA 60 01 00 00 01            cmp byte ptr [rdx + 0x160], 1
0027811F  74 34                           je 0x140278155
00278121  4C 8B 8A 08 05 00 00            mov r9, qword ptr [rdx + 0x508]
00278128  4D 85 C9                        test r9, r9
0027812B  74 28                           je 0x140278155
0027812D  49 8B C8                        mov rcx, r8
00278130  48 C1 E9 03                     shr rcx, 3
00278134  81 E1 FF 01 00 00               and ecx, 0x1ff
0027813A  49 8B 0C C9                     mov rcx, qword ptr [r9 + rcx*8]
0027813E  F6 C1 20                        test cl, 0x20
00278141  74 04                           je 0x140278147
00278143  48 83 C8 20                     or rax, 0x20
00278147  48 8B D0                        mov rdx, rax
0027814A  48 83 C8 42                     or rax, 0x42
0027814E  F6 C1 42                        test cl, 0x42
00278151  48 0F 44 C2                     cmove rax, rdx
00278155  A8 01                           test al, 1
00278157  0F 84 8D 04 00 00               je 0x1402785ea
0027815D  48 0F BA E0 3C                  bt rax, 0x3c
00278162  0F 82 82 04 00 00               jb 0x1402785ea
00278168  48 BA FF FF FF FF FF FF FF DF   movabs rdx, 0xdfffffffffffffff
00278172  48 8B C8                        mov rcx, rax
00278175  48 23 CA                        and rcx, rdx
00278178  48 BA 20 00 00 00 00 00 00 10   movabs rdx, 0x1000000000000020
00278182  48 0B CA                        or rcx, rdx
00278185  48 F7 05 F8 E8 D4 00 00 00 00 02  test qword ptr [rip + 0xd4e8f8], 0x2000000
00278190  74 03                           je 0x140278195
00278192  0F AE E8                        lfence
00278195  F0 49 0F B1 08                  lock cmpxchg qword ptr [r8], rcx
0027819A  41 BF 00 00 00 00               mov r15d, 0
002781A0  41 8B C7                        mov eax, r15d
002781A3  0F 94 C0                        sete al
002781A6  85 C0                           test eax, eax
002781A8  0F 84 56 06 00 00               je 0x140278804
002781AE  48 8B C7                        mov rax, rdi
002781B1  48 3B F0                        cmp rsi, rax
002781B4  0F 84 87 01 00 00               je 0x140278341
002781BA  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
002781C1  A8 0F                           test al, 0xf
002781C3  0F 84 F5 00 00 00               je 0x1402782be
002781C9  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
002781D0  A8 0F                           test al, 0xf
002781D2  0F 85 31 02 00 00               jne 0x140278409
002781D8  48 B8 FF FF FF FF FF FF FF CF   movabs rax, 0xcfffffffffffffff
002781E2  F0 48 21 06                     lock and qword ptr [rsi], rax
002781E6  48 8B FE                        mov rdi, rsi
002781E9  49 BE 00 00 00 00 80 F6 FF FF   movabs r14, 0xfffff68000000000
002781F3  48 C1 EE 09                     shr rsi, 9
002781F7  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00278201  48 23 F0                        and rsi, rax
00278204  49 8B C6                        mov rax, r14
00278207  48 03 F0                        add rsi, rax
0027820A  41 FF C4                        inc r12d
0027820D  48 FF C5                        inc rbp
00278210  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
00278215  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
0027821A  E9 6D F5 FF FF                  jmp 0x14027778c
0027821F  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
00278226  A8 0F                           test al, 0xf
00278228  75 41                           jne 0x14027826b
0027822A  49 8B C5                        mov rax, r13
0027822D  4C 3B C0                        cmp r8, rax
00278230  72 39                           jb 0x14027826b
00278232  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0027823C  48 8B C0                        mov rax, rax
0027823F  4C 3B C0                        cmp r8, rax
00278242  77 27                           ja 0x14027826b
00278244  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0027824D  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00278254  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
0027825B  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
00278262  48 85 C9                        test rcx, rcx
00278265  0F 85 91 06 00 00               jne 0x1402788fc
0027826B  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
00278272  A8 0F                           test al, 0xf
00278274  0F 85 28 02 00 00               jne 0x1402784a2
0027827A  49 8B 00                        mov rax, qword ptr [r8]
0027827D  49 8B CD                        mov rcx, r13
00278280  4C 3B C1                        cmp r8, rcx
00278283  0F 82 CC FE FF FF               jb 0x140278155
00278289  48 B9 F8 D7 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed7f8
00278293  48 8B C9                        mov rcx, rcx
00278296  4C 3B C1                        cmp r8, rcx
00278299  0F 87 B6 FE FF FF               ja 0x140278155
0027829F  A8 01                           test al, 1
002782A1  0F 84 43 03 00 00               je 0x1402785ea
002782A7  A8 42                           test al, 0x42
002782A9  0F 95 C2                        setne dl
002782AC  A8 20                           test al, 0x20
002782AE  0F 95 C1                        setne cl
002782B1  84 D1                           test cl, dl
002782B3  0F 85 9C FE FF FF               jne 0x140278155
002782B9  E9 3D FE FF FF                  jmp 0x1402780fb
002782BE  49 8B C5                        mov rax, r13
002782C1  48 3B F0                        cmp rsi, rax
002782C4  0F 82 FF FE FF FF               jb 0x1402781c9
002782CA  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
002782D4  48 8B C0                        mov rax, rax
002782D7  48 3B F0                        cmp rsi, rax
002782DA  0F 87 E9 FE FF FF               ja 0x1402781c9
002782E0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002782E9  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
002782F0  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
002782F7  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
002782FE  48 85 C9                        test rcx, rcx
00278301  0F 84 C2 FE FF FF               je 0x1402781c9
00278307  48 8B C6                        mov rax, rsi
0027830A  48 C1 E8 03                     shr rax, 3
0027830E  25 FF 01 00 00                  and eax, 0x1ff
00278313  48 8D 0C 81                     lea rcx, [rcx + rax*4]
00278317  8B 01                           mov eax, dword ptr [rcx]
00278319  A9 FF FF FF 3F                  test eax, 0x3fffffff
0027831E  0F 85 36 02 00 00               jne 0x14027855a
00278324  85 C0                           test eax, eax
00278326  0F 89 99 05 00 00               jns 0x1402788c5
0027832C  F6 05 D3 E7 D4 00 01            test byte ptr [rip + 0xd4e7d3], 1
00278333  0F 85 00 06 00 00               jne 0x140278939
00278339  44 89 39                        mov dword ptr [rcx], r15d
0027833C  E9 A5 FE FF FF                  jmp 0x1402781e6
00278341  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
0027834A  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
00278351  24 0F                           and al, 0xf
00278353  0F 85 1D 02 00 00               jne 0x140278576
00278359  B9 30 00 00 00                  mov ecx, 0x30
0027835E  48 8D BA 40 9C 00 00            lea rdi, [rdx + 0x9c40]
00278365  48 03 F9                        add rdi, rcx
00278368  F6 05 97 E7 D4 00 01            test byte ptr [rip + 0xd4e797], 1
0027836F  0F 85 C2 01 00 00               jne 0x140278537
00278375  0F 0D 0F                        prefetchw byte ptr [rdi]
00278378  48 8B 07                        mov rax, qword ptr [rdi]
0027837B  48 85 C0                        test rax, rax
0027837E  75 1A                           jne 0x14027839a
00278380  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00278384  48 8B C7                        mov rax, rdi
00278387  F0 4C 0F B1 39                  lock cmpxchg qword ptr [rcx], r15
0027838C  0F 84 54 FE FF FF               je 0x1402781e6
00278392  48 8B CF                        mov rcx, rdi
00278395  E8 06 F7 F9 FF                  call 0x140217aa0
0027839A  4C 8D 40 08                     lea r8, [rax + 8]
0027839E  4C 89 3F                        mov qword ptr [rdi], r15
002783A1  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
002783A5  48 8B C1                        mov rax, rcx
002783A8  49 87 00                        xchg qword ptr [r8], rax
002783AB  32 C1                           xor al, cl
002783AD  A8 04                           test al, 4
002783AF  0F 84 31 FE FF FF               je 0x1402781e6
002783B5  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
002783BA  49 C1 E8 05                     shr r8, 5
002783BE  41 83 E0 7F                     and r8d, 0x7f
002783C2  E8 19 F8 F9 FF                  call 0x140217be0
002783C7  0F B6 F8                        movzx edi, al
002783CA  49 8B D7                        mov rdx, r15
002783CD  48 8D 05 2C 7C D8 FF            lea rax, [rip - 0x2783d4]
002783D4  4A 87 94 C0 20 1B F2 00         xchg qword ptr [rax + r8*8 + 0xf21b20], rdx
002783DC  E8 13 F7 F9 FF                  call 0x140217af4
002783E1  40 84 FF                        test dil, dil
002783E4  0F 84 FC FD FF FF               je 0x1402781e6
002783EA  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
002783F3  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
002783FA  4D 85 C0                        test r8, r8
002783FD  0F 85 35 04 00 00               jne 0x140278838
00278403  FB                              sti
00278404  E9 DD FD FF FF                  jmp 0x1402781e6
00278409  49 8B C5                        mov rax, r13
0027840C  48 3B F0                        cmp rsi, rax
0027840F  0F 82 C3 FD FF FF               jb 0x1402781d8
00278415  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0027841F  48 8B C0                        mov rax, rax
00278422  48 3B F0                        cmp rsi, rax
00278425  0F 87 AD FD FF FF               ja 0x1402781d8
0027842B  49 8B C5                        mov rax, r13
0027842E  48 8B CE                        mov rcx, rsi
00278431  BA 02 00 00 00                  mov edx, 2
00278436  48 2B C8                        sub rcx, rax
00278439  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
00278440  48 C1 F9 03                     sar rcx, 3
00278444  44 8D 04 09                     lea r8d, [rcx + rcx]
00278448  41 8B C8                        mov ecx, r8d
0027844B  41 8B C0                        mov eax, r8d
0027844E  83 E1 1F                        and ecx, 0x1f
00278451  D3 E2                           shl edx, cl
00278453  F7 D2                           not edx
00278455  0F B3 CA                        btr edx, ecx
00278458  48 C1 E8 05                     shr rax, 5
0027845C  48 8D 0D 9D 7B D8 FF            lea rcx, [rip - 0x278463]
00278463  F0 21 94 81 AC F1 E2 00         lock and dword ptr [rcx + rax*4 + 0xe2f1ac], edx
0027846B  E9 76 FD FF FF                  jmp 0x1402781e6
00278470  3C 07                           cmp al, 7
00278472  0F 84 C4 02 00 00               je 0x14027873c
00278478  3C 05                           cmp al, 5
0027847A  B9 03 00 00 00                  mov ecx, 3
0027847F  41 BF 00 00 00 00               mov r15d, 0
00278485  41 0F 44 CF                     cmove ecx, r15d
00278489  8B C1                           mov eax, ecx
0027848B  48 8D 15 6E 7B D8 FF            lea rdx, [rip - 0x278492]
00278492  48 8D 14 C2                     lea rdx, [rdx + rax*8]
00278496  48 8D 92 C0 FD E2 00            lea rdx, [rdx + 0xe2fdc0]
0027849D  E9 29 FC FF FF                  jmp 0x1402780cb
002784A2  49 8B C5                        mov rax, r13
002784A5  4C 3B C0                        cmp r8, rax
002784A8  0F 82 CC FD FF FF               jb 0x14027827a
002784AE  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
002784B8  48 8B C0                        mov rax, rax
002784BB  4C 3B C0                        cmp r8, rax
002784BE  0F 87 B6 FD FF FF               ja 0x14027827a
002784C4  49 8B C5                        mov rax, r13
002784C7  4C 2B C0                        sub r8, rax
002784CA  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
002784D1  49 C1 F8 03                     sar r8, 3
002784D5  43 8D 0C 00                     lea ecx, [r8 + r8]
002784D9  8B C1                           mov eax, ecx
002784DB  8B D1                           mov edx, ecx
002784DD  48 C1 E8 05                     shr rax, 5
002784E1  48 8D 0D 18 7B D8 FF            lea rcx, [rip - 0x2784e8]
002784E8  4C 8D 89 AC F1 E2 00            lea r9, [rcx + 0xe2f1ac]
002784EF  83 E2 1F                        and edx, 0x1f
002784F2  45 8B 14 81                     mov r10d, dword ptr [r9 + rax*4]
002784F6  4D 8D 0C 81                     lea r9, [r9 + rax*4]
002784FA  41 8B C2                        mov eax, r10d
002784FD  8B CA                           mov ecx, edx
002784FF  D3 E8                           shr eax, cl
00278501  A8 01                           test al, 1
00278503  0F 85 F8 02 00 00               jne 0x140278801
00278509  41 B8 01 00 00 00               mov r8d, 1
0027850F  BA 02 00 00 00                  mov edx, 2
00278514  41 D3 E0                        shl r8d, cl
00278517  41 8B C2                        mov eax, r10d
0027851A  D3 E2                           shl edx, cl
0027851C  45 0B C2                        or r8d, r10d
0027851F  F7 D2                           not edx
00278521  44 23 C2                        and r8d, edx
00278524  F0 45 0F B1 01                  lock cmpxchg dword ptr [r9], r8d
00278529  0F 85 D2 02 00 00               jne 0x140278801
0027852F  45 33 FF                        xor r15d, r15d
00278532  E9 77 FC FF FF                  jmp 0x1402781ae
00278537  8B 05 1B 59 C9 00               mov eax, dword ptr [rip + 0xc9591b]
0027853D  85 C0                           test eax, eax
0027853F  0F 85 30 FE FF FF               jne 0x140278375
00278545  48 8B 94 24 18 01 00 00         mov rdx, qword ptr [rsp + 0x118]
0027854D  48 8B CF                        mov rcx, rdi
00278550  E8 9B F4 F9 FF                  call 0x1402179f0
00278555  E9 8C FC FF FF                  jmp 0x1402781e6
0027855A  F6 05 A5 E5 D4 00 01            test byte ptr [rip + 0xd4e5a5], 1
00278561  0F 85 F2 03 00 00               jne 0x140278959
00278567  F0 81 21 FF FF FF BF            lock and dword ptr [rcx], 0xbfffffff
0027856E  F0 FF 09                        lock dec dword ptr [rcx]
00278571  E9 70 FC FF FF                  jmp 0x1402781e6
00278576  3C 07                           cmp al, 7
00278578  0F 84 79 02 00 00               je 0x1402787f7
0027857E  3C 05                           cmp al, 5
00278580  B9 48 00 00 00                  mov ecx, 0x48
00278585  49 0F 44 CF                     cmove rcx, r15
00278589  E9 D0 FD FF FF                  jmp 0x14027835e
0027858E  83 E0 FE                        and eax, 0xfffffffe
00278591  48 C7 84 24 38 01 00 00 FF FF FF FF  mov qword ptr [rsp + 0x138], 0xffffffffffffffff
0027859D  89 43 04                        mov dword ptr [rbx + 4], eax
002785A0  F6 C1 04                        test cl, 4
002785A3  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
002785A7  48 8B C8                        mov rcx, rax
002785AA  0F 84 0D 02 00 00               je 0x1402787bd
002785B0  E8 3B 46 00 00                  call 0x14027cbf0
002785B5  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
002785BA  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
002785BF  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
002785C4  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
002785C9  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
002785CE  44 8B 84 24 28 01 00 00         mov r8d, dword ptr [rsp + 0x128]
002785D6  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
002785DB  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
002785E5  E9 D2 F0 FF FF                  jmp 0x1402776bc
002785EA  45 33 FF                        xor r15d, r15d
002785ED  41 8B C7                        mov eax, r15d
002785F0  E9 B1 FB FF FF                  jmp 0x1402781a6
002785F5  48 8B 6C 24 30                  mov rbp, qword ptr [rsp + 0x30]
002785FA  8B BC 24 20 01 00 00            mov edi, dword ptr [rsp + 0x120]
00278601  E9 DD F5 FF FF                  jmp 0x140277be3
00278606  41 0F 0D 08                     prefetchw byte ptr [r8]
0027860A  41 8B 00                        mov eax, dword ptr [r8]
0027860D  8B D0                           mov edx, eax
0027860F  0F BA F2 15                     btr edx, 0x15
00278613  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00278618  75 F3                           jne 0x14027860d
0027861A  0F BA E0 15                     bt eax, 0x15
0027861E  0F 83 50 F8 FF FF               jae 0x140277e74
00278624  E8 A7 AB FE FF                  call 0x1402631d0
00278629  E9 46 F8 FF FF                  jmp 0x140277e74
0027862E  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00278633  E9 AF F6 FF FF                  jmp 0x140277ce7
00278638  49 8B C5                        mov rax, r13
0027863B  48 B9 FF DF BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbedfff
00278645  48 3B F0                        cmp rsi, rax
00278648  0F 82 39 F6 FF FF               jb 0x140277c87
0027864E  48 8B C1                        mov rax, rcx
00278651  48 3B F0                        cmp rsi, rax
00278654  0F 87 2D F6 FF FF               ja 0x140277c87
0027865A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00278663  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0027866A  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
00278671  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
00278678  48 85 C9                        test rcx, rcx
0027867B  0F 84 FC F5 FF FF               je 0x140277c7d
00278681  48 C1 EE 03                     shr rsi, 3
00278685  81 E6 FF 01 00 00               and esi, 0x1ff
0027868B  48 8D 0C B1                     lea rcx, [rcx + rsi*4]
0027868F  E8 9C 1C FC FF                  call 0x14023a330
00278694  E9 0B F6 FF FF                  jmp 0x140277ca4
00278699  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
002786A2  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
002786A9  24 0F                           and al, 0xf
002786AB  0F 85 69 01 00 00               jne 0x14027881a
002786B1  B9 30 00 00 00                  mov ecx, 0x30
002786B6  45 33 FF                        xor r15d, r15d
002786B9  48 81 C2 40 9C 00 00            add rdx, 0x9c40
002786C0  48 03 CA                        add rcx, rdx
002786C3  E8 E8 EA F9 FF                  call 0x1402171b0
002786C8  E9 DA F5 FF FF                  jmp 0x140277ca7
002786CD  49 8B C5                        mov rax, r13
002786D0  48 3B F0                        cmp rsi, rax
002786D3  0F 82 BD F5 FF FF               jb 0x140277c96
002786D9  48 8B C1                        mov rax, rcx
002786DC  48 3B F0                        cmp rsi, rax
002786DF  0F 87 B1 F5 FF FF               ja 0x140277c96
002786E5  49 8B C5                        mov rax, r13
002786E8  48 2B F0                        sub rsi, rax
002786EB  BA 02 00 00 00                  mov edx, 2
002786F0  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
002786F7  48 C1 FE 03                     sar rsi, 3
002786FB  44 8D 04 36                     lea r8d, [rsi + rsi]
002786FF  41 8B C8                        mov ecx, r8d
00278702  41 8B C0                        mov eax, r8d
00278705  83 E1 1F                        and ecx, 0x1f
00278708  D3 E2                           shl edx, cl
0027870A  F7 D2                           not edx
0027870C  0F B3 CA                        btr edx, ecx
0027870F  48 C1 E8 05                     shr rax, 5
00278713  48 8D 0D E6 78 D8 FF            lea rcx, [rip - 0x27871a]
0027871A  F0 21 94 81 AC F1 E2 00         lock and dword ptr [rcx + rax*4 + 0xe2f1ac], edx
00278722  E9 7D F5 FF FF                  jmp 0x140277ca4
00278727  B9 18 00 00 00                  mov ecx, 0x18
0027872C  48 8B 84 11 40 9C 00 00         mov rax, qword ptr [rcx + rdx + 0x9c40]
00278734  48 85 C0                        test rax, rax
00278737  E9 8F F2 FF FF                  jmp 0x1402779cb
0027873C  B9 01 00 00 00                  mov ecx, 1
00278741  45 33 FF                        xor r15d, r15d
00278744  E9 40 FD FF FF                  jmp 0x140278489
00278749  48 C1 EF 09                     shr rdi, 9
0027874D  49 23 FA                        and rdi, r10
00278750  49 8B C1                        mov rax, r9
00278753  48 03 F8                        add rdi, rax
00278756  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
0027875B  48 C1 EF 09                     shr rdi, 9
0027875F  49 23 FA                        and rdi, r10
00278762  49 8B C1                        mov rax, r9
00278765  48 03 F8                        add rdi, rax
00278768  48 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdi
00278770  48 C1 EF 09                     shr rdi, 9
00278774  49 23 FA                        and rdi, r10
00278777  49 8B C1                        mov rax, r9
0027877A  48 03 F8                        add rdi, rax
0027877D  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
00278785  48 C1 EF 09                     shr rdi, 9
00278789  49 23 FA                        and rdi, r10
0027878C  49 8B C1                        mov rax, r9
0027878F  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00278794  48 03 F8                        add rdi, rax
00278797  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0027879C  44 8B 84 24 28 01 00 00         mov r8d, dword ptr [rsp + 0x128]
002787A4  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
002787A9  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
002787B1  E9 06 EF FF FF                  jmp 0x1402776bc
002787B6  8B FE                           mov edi, esi
002787B8  E9 26 F4 FF FF                  jmp 0x140277be3
002787BD  E8 DE B0 0A 00                  call 0x1403238a0
002787C2  E9 EE FD FF FF                  jmp 0x1402785b5
002787C7  48 8D 05 32 76 20 00            lea rax, [rip + 0x207632]
002787CE  4C 3B C8                        cmp r9, rax
002787D1  0F 85 DC 01 00 00               jne 0x1402789b3
002787D7  E8 24 76 20 00                  call 0x14047fe00
002787DC  E9 30 F0 FF FF                  jmp 0x140277811
002787E1  49 8D 91 C0 00 00 00            lea rdx, [r9 + 0xc0]
002787E8  E9 6E F0 FF FF                  jmp 0x14027785b
002787ED  E8 AE B0 0A 00                  call 0x1403238a0
002787F2  E9 F0 F4 FF FF                  jmp 0x140277ce7
002787F7  B9 18 00 00 00                  mov ecx, 0x18
002787FC  E9 5D FB FF FF                  jmp 0x14027835e
00278801  45 33 FF                        xor r15d, r15d
00278804  48 8B D6                        mov rdx, rsi
00278807  49 8B CE                        mov rcx, r14
0027880A  E8 B1 E6 F9 FF                  call 0x140216ec0
0027880F  32 C0                           xor al, al
00278811  4C 89 7B 38                     mov qword ptr [rbx + 0x38], r15
00278815  E9 66 F5 FF FF                  jmp 0x140277d80
0027881A  3C 07                           cmp al, 7
0027881C  0F 84 BE 00 00 00               je 0x1402788e0
00278822  3C 05                           cmp al, 5
00278824  B9 48 00 00 00                  mov ecx, 0x48
00278829  41 BF 00 00 00 00               mov r15d, 0
0027882F  41 0F 44 CF                     cmove ecx, r15d
00278833  E9 81 FE FF FF                  jmp 0x1402786b9
00278838  41 0F 0D 08                     prefetchw byte ptr [r8]
0027883C  41 8B 00                        mov eax, dword ptr [r8]
0027883F  8B D0                           mov edx, eax
00278841  0F BA F2 15                     btr edx, 0x15
00278845  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0027884A  75 F3                           jne 0x14027883f
0027884C  0F BA E0 15                     bt eax, 0x15
00278850  0F 83 AD FB FF FF               jae 0x140278403
00278856  E8 75 A9 FE FF                  call 0x1402631d0
0027885B  E9 A3 FB FF FF                  jmp 0x140278403
00278860  48 8B 53 38                     mov rdx, qword ptr [rbx + 0x38]
00278864  48 85 D2                        test rdx, rdx
00278867  74 11                           je 0x14027887a
00278869  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0027886E  E8 4D E6 F9 FF                  call 0x140216ec0
00278873  45 33 FF                        xor r15d, r15d
00278876  4C 89 7B 38                     mov qword ptr [rbx + 0x38], r15
0027887A  32 C0                           xor al, al
0027887C  E9 FF F4 FF FF                  jmp 0x140277d80
00278881  48 8D 05 F8 A9 20 00            lea rax, [rip + 0x20a9f8]
00278888  48 8B CB                        mov rcx, rbx
0027888B  48 3B F0                        cmp rsi, rax
0027888E  0F 85 2C 01 00 00               jne 0x1402789c0
00278894  E8 E7 A9 20 00                  call 0x140483280
00278899  E9 76 F3 FF FF                  jmp 0x140277c14
0027889E  49 63 EC                        movsxd rbp, r12d
002788A1  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
002788A6  48 8B 44 EC 78                  mov rax, qword ptr [rsp + rbp*8 + 0x78]
002788AB  48 3B F8                        cmp rdi, rax
002788AE  48 0F 42 F8                     cmovb rdi, rax
002788B2  48 8D 4F 08                     lea rcx, [rdi + 8]
002788B6  E8 E5 37 00 00                  call 0x14027c0a0
002788BB  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
002788C0  E9 C7 EE FF FF                  jmp 0x14027778c
002788C5  45 33 C9                        xor r9d, r9d
002788C8  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
002788CD  48 8B D1                        mov rdx, rcx
002788D0  41 B8 00 01 00 00               mov r8d, 0x100
002788D6  41 8D 49 10                     lea ecx, [r9 + 0x10]
002788DA  E8 81 4D 28 00                  call 0x1404fd660
002788DF  CC                              int3
002788E0  48 81 C2 40 9C 00 00            add rdx, 0x9c40
002788E7  B9 18 00 00 00                  mov ecx, 0x18
002788EC  48 03 CA                        add rcx, rdx
002788EF  45 33 FF                        xor r15d, r15d
002788F2  E8 B9 E8 F9 FF                  call 0x1402171b0
002788F7  E9 AB F3 FF FF                  jmp 0x140277ca7
002788FC  41 C1 E8 03                     shr r8d, 3
00278900  41 81 E0 FF 01 00 00            and r8d, 0x1ff
00278907  4A 8D 0C 81                     lea rcx, [rcx + r8*4]
0027890B  E8 F0 2E 04 00                  call 0x1402bb800
00278910  45 33 FF                        xor r15d, r15d
00278913  E9 8E F8 FF FF                  jmp 0x1402781a6
00278918  41 8D 4D FF                     lea ecx, [r13 - 1]
0027891C  48 C1 ED 09                     shr rbp, 9
00278920  49 23 EA                        and rbp, r10
00278923  49 8B C1                        mov rax, r9
00278926  48 03 E8                        add rbp, rax
00278929  48 83 E9 01                     sub rcx, 1
0027892D  75 ED                           jne 0x14027891c
0027892F  48 89 6C 24 58                  mov qword ptr [rsp + 0x58], rbp
00278934  E9 F3 F3 FF FF                  jmp 0x140277d2c
00278939  8B 05 19 55 C9 00               mov eax, dword ptr [rip + 0xc95519]
0027893F  85 C0                           test eax, eax
00278941  0F 85 F2 F9 FF FF               jne 0x140278339
00278947  48 8B 94 24 18 01 00 00         mov rdx, qword ptr [rsp + 0x118]
0027894F  E8 F0 85 04 00                  call 0x1402c0f44
00278954  E9 8D F8 FF FF                  jmp 0x1402781e6
00278959  8B 05 F9 54 C9 00               mov eax, dword ptr [rip + 0xc954f9]
0027895F  85 C0                           test eax, eax
00278961  0F 85 00 FC FF FF               jne 0x140278567
00278967  48 8B 94 24 18 01 00 00         mov rdx, qword ptr [rsp + 0x118]
0027896F  E8 D4 85 07 00                  call 0x1402f0f48
00278974  E9 6D F8 FF FF                  jmp 0x1402781e6
00278979  41 8B CC                        mov ecx, r12d
0027897C  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
00278986  41 2B CD                        sub ecx, r13d
00278989  48 C1 EE 09                     shr rsi, 9
0027898D  48 23 F2                        and rsi, rdx
00278990  49 8B C6                        mov rax, r14
00278993  48 C1 EF 09                     shr rdi, 9
00278997  48 03 F0                        add rsi, rax
0027899A  48 23 FA                        and rdi, rdx
0027899D  49 8B C6                        mov rax, r14
002789A0  48 03 F8                        add rdi, rax
002789A3  48 83 E9 01                     sub rcx, 1
002789A7  75 E0                           jne 0x140278989
002789A9  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
002789AE  E9 8C ED FF FF                  jmp 0x14027773f
002789B3  49 8B C1                        mov rax, r9
002789B6  E8 15 21 44 00                  call 0x1406baad0
002789BB  E9 51 EE FF FF                  jmp 0x140277811
002789C0  48 8B C6                        mov rax, rsi
002789C3  E8 08 21 44 00                  call 0x1406baad0
002789C8  E9 47 F2 FF FF                  jmp 0x140277c14
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDeleteVaDirect(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_p0;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p118;
    unsigned int v_stack_p120;
    unsigned int v_stack_p128;
    unsigned __int64 v_stack_p138;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned int v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;

    v_rsp = (v_rsp) - (216);
    v_stack_m78 = *(unsigned __int64 *)(a1 + 176);
    v_r15 = 0;
    v_stack_mE0 = *(unsigned __int64 *)(a1 + 32);
    a3 = 0;
    if ((*(unsigned __int64 *)(a1 + 168)) != (v_rip + 5212)) { a3 = 8; }
    v_stack_p10 = (unsigned int)(a3);
    result = ((*(unsigned __int64 *)(a1 + 168)) != (v_rip + 5212)) ? 1 : 0;
    v_stack_mB0 = result + 1;
    a1 = (*(unsigned __int64 *)(a1 + 40)) >> (9);
    a1 = (a1) & (v_r10);
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 160)));
    a1 = (a1) + (a4);
    v_stack_mA0 = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (v_r10);
    a1 = (a1) + (a4);
    *(unsigned __int64 *)(v_rsp - 152) = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (v_r10);
    a1 = (a1) + (a4);
    *(unsigned __int64 *)(v_rsp - 144) = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (v_r10);
    a1 = (a1) + (a4);
    *(unsigned __int64 *)(v_rsp - 136) = a1;
    a1 = (*(unsigned __int64 *)(a1 + 48)) >> (9);
    a1 = (a1) & (v_r10);
    a1 = (a1) + (a4);
    *(unsigned __int64 *)(v_rsp - 112) = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (v_r10);
    a1 = (a1) + (a4);
    *(unsigned __int64 *)(v_rsp - 104) = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (v_r10);
    a1 = (a1) + (a4);
    *(unsigned __int64 *)(v_rsp - 96) = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (v_r10);
    a1 = (a1) + (a4);
    *(unsigned __int64 *)(v_rsp - 88) = a1;
    v_stack_mA8 = *(unsigned __int64 *)(v_rsp + result + 1 * 8 + 168);
    v_stack_p20 = -1;
    v_stack_mC0 = *(unsigned __int64 *)(v_rsp + result + 1 * 8 + 120);
    v_r15 = (a4) << (25);
    v_stack_mC8 = v_r15;
loc_002776BC:
    if ((*(unsigned __int64 *)(v_rsp + result + 1 * 8 + 120)) > (*(unsigned __int64 *)(v_rsp + result + 1 * 8 + 168))) goto loc_00277D7E;
    if ((*(unsigned __int64 *)(v_rsp + result + 1 * 8 + 120)) < a4) goto loc_002776FE;
loc_002776E0:
    if ((*(unsigned __int64 *)(v_rsp + result + 1 * 8 + 120)) > v_r10) goto loc_002776FE;
    a2 = (*(unsigned __int64 *)(v_rsp + result + 1 * 8 + 120)) << (25);
    a2 = (a2) - (v_r15);
    a2 = (a2) >> (16);
    if (a2 >= a4) goto loc_002776E0;
loc_002776FE:
    result = MiFastLockLeafPageTable(*(unsigned __int64 *)(a1 + 32), a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0027887A;
    v_stack_mD8 = *(unsigned __int64 *)(v_rsp + result + 1 * 8 + 120);
    v_rdi = (*(unsigned __int64 *)(v_rsp + result + 1 * 8 + 120)) << (25);
    v_rdi = (v_rdi) - (v_r15);
    v_stack_mB8 = v_r15;
    v_rdi = (v_rdi) >> (16);
    if (((unsigned int)(result + 1)) < ((unsigned int)(result))) goto loc_00278979;
loc_0027773F:
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(result))) - (1));
    if (condition_is_not_equal) goto loc_0027889E;
    v_stack_mD0 = *(unsigned __int64 *)(v_rsp + result + 1 * 8 + 120) + 8;
    if ((*(unsigned __int64 *)(v_rsp + result + 1 * 8 + 120) + 8) < (*(unsigned __int64 *)(a1 + 32))) goto loc_00277784;
loc_00277764:
    if ((*(unsigned __int64 *)(v_rsp + result + 1 * 8 + 120) + 8) > a2) goto loc_0027777F;
    a1 = (*(unsigned __int64 *)(v_rsp + result + 1 * 8 + 120) + 8) << (25);
    a1 = (a1) - (v_r15);
    a1 = (a1) >> (16);
    if (a1 >= (*(unsigned __int64 *)(a1 + 32))) goto loc_00277764;
loc_0027777F:
    v_stack_mD0 = a1;
loc_00277784:
    v_stack_mE8 = (int)((unsigned int)(v_r12));
loc_0027778C:
    *(unsigned __int64 *)(a1 + 56) = *(unsigned __int64 *)(v_rsp + result + 1 * 8 + 120);
    if (v_rdi < (*(unsigned __int64 *)(v_rsp + (int)((unsigned int)(v_r12)) * 8 + 120))) { v_rdi = *(unsigned __int64 *)(v_rsp + (int)((unsigned int)(v_r12)) * 8 + 120); }
    v_stack_m80 = *(unsigned __int64 *)(a1 + 168);
    if ((unsigned int)(v_r12) != 0) goto loc_002777D8;
    v_r13 = (v_rdi) & (-8);
    v_r13 = (v_r13) | (0xFF8ULL);
    if (v_r13 >= = (*(unsigned __int64 *)(v_rsp + (int)((unsigned int)(v_r12)) * 8 + 168))) {
        v_r13 = *(unsigned __int64 *)(v_rsp + (int)((unsigned int)(v_r12)) * 8 + 168);
    }
    v_rsi = 0;
    v_stack_p8 = 0;
loc_002777E1:
    if (v_rdi > v_r13) goto loc_002785F5;
    if ((unsigned int)(v_r12) != 0) goto loc_00277B8B;
loc_002777F3:
    if ((*(unsigned __int64 *)(a1 + 168)) != (v_rip + 4582)) goto loc_002787C7;
    result = MiDeleteVa(a1, v_rdi, (unsigned int)((unsigned int)(v_r12)), *(unsigned __int64 *)(a1 + 168));
loc_00277811:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (2)) == 0) goto loc_002778A1;
    if (((*(unsigned __int8 *)(a1 + 8)) & ((unsigned __int8)(*(unsigned __int64 *)(a1 + 160)))) != 0) goto loc_002778A1;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) & (4));
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184))) & (15));
    if (((unsigned __int8)(result)) > 5) goto loc_00277913;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 184))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_002787E1;
loc_0027785B:
    if ((unsigned int)(a1) == 0) goto loc_002778F5;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) == 0) goto loc_002778F1;
loc_00277881:
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 324))) << (6);
    if (condition_is_above_or_equal) goto loc_00277913;
loc_00277892:
    v_stack_p8 = 2;
    goto loc_002778A1;
loc_0027789F:
    v_rsi = 0;
loc_002778A1:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 12))) + 1);
    *(unsigned int *)(a1 + 12) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 72) = v_rdi + result * 8;
    result = (v_rdi + result * 8) << (25);
    result = (result) - (v_stack_mC8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 88) = v_rdi + result * 8;
    result = (result) >> (16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)) + 56) = result;
    if (v_stack_p8 == 2) goto loc_00277F11;
    goto loc_002777E1;
loc_002778F1:
    goto loc_00277881;
loc_002778F5:
loc_002778F8:
    if (0 >= 4) goto loc_00277913;
    result = (0) << (6);
    if (condition_is_below) goto loc_00277892;
    a3 = (unsigned int)((0) + 1);
    goto loc_002778F8;
loc_00277913:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (4)) == 0) goto loc_002779D1;
    a3 = (v_rdi + result * 8) >> (9);
    a3 = (a3) & ((unsigned int)(*(unsigned int *)(a1)));
    a3 = (a3) + (*(unsigned __int64 *)(a1 + 32));
    if (a3 == (*(unsigned __int64 *)(a1 + 32))) goto loc_00277D95;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m80 + 184)))) & (15)) == 0) goto loc_00277A5A;
loc_0027795C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m80 + 184)))) & (15)) == 0) goto loc_0027798F;
    if (a3 < ((unsigned int)(*(unsigned int *)(result + *(unsigned __int64 *)(v_rip + 12324837) * 1)))) goto loc_0027798F;
    if (a3 <= ((unsigned int)(*(unsigned int *)(result + *(unsigned __int64 *)(v_rip + 12324837) * 1)))) goto loc_00277DC2;
loc_0027798F:
    if (a3 < ((unsigned int)(*(unsigned int *)(result + *(unsigned __int64 *)(v_rip + 12324837) * 1)))) goto loc_002779C2;
    if (a3 > ((unsigned int)(*(unsigned int *)(result + *(unsigned __int64 *)(v_rip + 12324837) * 1)))) goto loc_002779C2;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (1)) == 0) goto loc_002779C2;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a2))) == 0) goto loc_00277ACF;
loc_002779C2:
    result = (*(unsigned __int64 *)(a3)) >> (60);
    result = (unsigned int)((result) & (2));
loc_002779C9:
loc_002779CB:
    if ((unsigned int)(result) != 0) goto loc_00277892;
loc_002779D1:
    if ((*(unsigned __int8 *)(a1 + 9)) >= 2) goto loc_002778A1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)))) & (1)) != 0) goto loc_00277B38;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32)) != 0) goto loc_00277E14;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)))) & (30)) != 0) goto loc_00277B5F;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14521)) != 0) goto loc_00277E3B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16) != 0) goto loc_00277E00;
loc_00277A35:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33708)))) <= 7) goto loc_002778A1;
    if (0 == 0) goto loc_00277E45;
loc_00277A47:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14524)))) & (30)) == 0) goto loc_00277E7A;
    goto loc_00277B64;
loc_00277A5A:
    if (0 < (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16))) goto loc_0027795C;
    if (0 > (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 16))) goto loc_0027795C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) == 0) goto loc_0027795C;
    a3 = (unsigned int)((0) >> (3));
    a3 = (unsigned int)((a3) & (511));
    result = 5;
    if (condition_is_below) { result = 1; }
    goto loc_002779C9;
loc_00277ACF:
    if (((*(unsigned __int64 *)(v_rip + 13954990)) & (0x600000ULL)) == 0) goto loc_002779C2;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_002779C2;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_002779C2;
    a3 = (a3) >> (3);
    a3 = (unsigned int)((a3) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a3 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    result = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a3 * 8))) & (66)) == 0) { result = result; }
    goto loc_002779C2;
loc_00277B38:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34396)))) <= 7) goto loc_00277A35;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a3 * 8) + 14521)) == 0) goto loc_00277A47;
    goto loc_00277B64;
loc_00277B5F:
loc_00277B64:
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a3 * 8) + 14521);
    if (((*(unsigned int *)(v_rip + 13954966)) & (0x4000000ULL)) != 0) {
        a3 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34396)));
        a2 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 33708)));
        a1 = 2;
        result = EtwTraceShouldYieldProcessor(a1, a2, a3, 0);
    }
    if (2 == 0) goto loc_0027789F;
    v_rsi = 0;
    goto loc_00277892;
loc_00277B8B:
    if ((v_rdi + result * 8) < a1) goto loc_00277BC8;
    if ((v_rdi + result * 8) > a1) goto loc_00277BC8;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi + result * 8))) & (1)) == 0) goto loc_00277BC8;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi + result * 8))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi + result * 8))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a2))) == 0) goto loc_00277E8E;
loc_00277BC8:
    if (*(unsigned __int64 *)(v_rdi + result * 8) == 0) goto loc_002777F3;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi + result * 8))) & (1)) != 0) goto loc_002777F3;
loc_00277BE3:
loc_00277BED:
    if (v_stack_m78 != (v_rip + 2081524)) goto loc_00278881;
    result = MiDecommitPagesTail(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184)), a2, a3, 0);
loc_00277C14:
    if (5 == 5) goto loc_00278860;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (1)) != 0) goto loc_0027858E;
    a1 = (condition_is_above_or_equal) ? 1 : 0;
    result = (((v_stack_p18) & (128)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00277F94;
loc_00277C53:
    if (v_stack_mD8 == result) goto loc_00278699;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mE0 + 184)))) & (15)) == 0) goto loc_00278638;
loc_00277C7D:
loc_00277C87:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mE0 + 184)))) & (15)) != 0) goto loc_002786CD;
loc_00277C96:
loc_00277CA4:
    v_r15 = 0;
loc_00277CA7:
    *(unsigned __int64 *)(a1 + 56) = 0;
    if (5 != 2) goto loc_0027862E;
    result = MiReleaseWalkLocks(a1, a2, a3, 0);
    v_stack_p20 = -1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (4)) == 0) goto loc_002787ED;
    result = MiLockWorkingSetShared(*(unsigned __int64 *)(a1 + 32), a2, a3, 0);
loc_00277CE7:
    v_rbp = (v_stack_p20) >> (18);
    v_rbp = (unsigned int)((v_rbp) & (0x3FFFFFF8ULL));
    v_rbp = (v_rbp) + (result);
    v_stack_mC0 = v_rbp;
    if (((unsigned int)(v_stack_mB0)) > 1) goto loc_00278918;
loc_00277D2C:
    if (v_stack_m70 < 0) goto loc_00277D75;
    a2 = (0) << (25);
loc_00277D50:
    if (v_stack_m70 > 1) goto loc_00277D6B;
    a1 = (v_stack_m70) << (25);
    a1 = (a1) - (a2);
    a1 = (a1) >> (16);
    if (a1 >= 0) goto loc_00277D50;
loc_00277D6B:
loc_00277D75:
    if (v_stack_p20 <= a1) goto loc_00278749;
loc_00277D7E:
loc_00277D80:
    v_rsp = (v_rsp) + (216);
    return 1;
loc_00277D95:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(0 + 184))) & (15));
    if (condition_is_not_equal) goto loc_00277EF9;
loc_00277DB2:
    goto loc_002779CB;
loc_00277DC2:
    a3 = (a3) - (48);
    a3 = (a3) >> (3);
    result = ((unsigned int)((unsigned int)(a3 + a3 * 1))) >> (5);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a3 + a3 * 1))) & (31));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip - 2588134 + result * 4 + 14873004))) >> ((unsigned __int8)(a1)));
    if ((((unsigned __int8)(a2)) & (2)) == 0) goto loc_002779D1;
    goto loc_00277892;
loc_00277E00:
    if (result == (*(unsigned __int64 *)(a1 + 8))) goto loc_00277A35;
    goto loc_00277B64;
loc_00277E14:
    if (((unsigned int)(v_rbp)) <= 7) goto loc_002778A1;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 14521)) == 0) goto loc_00277A47;
    goto loc_00277B64;
loc_00277E3B:
    goto loc_00277B64;
loc_00277E45:
    if (1 != 0) goto loc_00277A47;
loc_00277E4E:
    *(unsigned int *)(a1 + 33708) = 3;
    *(unsigned int *)(a1 + 34396) = 3;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00278606;
loc_00277E74:
    goto loc_00277B64;
loc_00277E7A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24))) goto loc_00277E4E;
    goto loc_00277B64;
loc_00277E8E:
    if (((*(unsigned __int64 *)(v_rip + 13954031)) & (0x600000ULL)) == 0) goto loc_00277BC8;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_00277BC8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_00277BC8;
    a1 = (v_stack_p20) >> (3);
    a1 = (unsigned int)((a1) & (511));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (32)) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24)) | (32);
    }
    result = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (66)) == 0) { result = result; }
    goto loc_00277BC8;
loc_00277EF9:
    if (((unsigned __int8)(result)) == 7) goto loc_00278727;
    a1 = 72;
    if (((unsigned __int8)(result)) == 5) { a1 = 6; }
    goto loc_00277DB2;
loc_00277F11:
    if (v_stack_p20 > (*(unsigned __int64 *)(v_rsp + v_stack_p30 * 8 + 168))) goto loc_002787B6;
    if (v_stack_p138 != -1) goto loc_002785FA;
    v_stack_p138 = v_stack_p20;
    if (v_stack_p20 < v_stack_mE0) goto loc_00277F88;
loc_00277F60:
    if (v_stack_p20 > v_stack_p30) goto loc_00277F7B;
    a2 = (v_stack_p20) << (25);
    a2 = (a2) - (a1);
    a2 = (a2) >> (16);
    if (a2 >= v_stack_mE0) goto loc_00277F60;
loc_00277F7B:
    v_stack_p138 = a2;
loc_00277F88:
    goto loc_00277BED;
loc_00277F94:
    if (((unsigned int)(v_r12)) == 3) goto loc_00277C53;
    if (6 < v_stack_mB0) goto loc_00278027;
    if (6 > v_stack_mB0) goto loc_00278027;
    if ((((unsigned __int8)(*(unsigned __int64 *)(6))) & (1)) == 0) goto loc_00278027;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(6))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(6))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_00278027;
    if (((*(unsigned __int64 *)(v_rip + 13953709)) & (0x600000ULL)) == 0) goto loc_00278027;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_00278027;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_00278027;
    result = (6) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (32)) != 0) {
        a2 = (*(unsigned __int64 *)(6)) | (32);
    }
    a2 = (a2) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (66)) == 0) { a2 = a2; }
loc_00278027:
    a2 = (a2) >> (12);
    a2 = (a2) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8));
    a1 = (a2 + a2 * 2) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8));
    if (condition_is_above_or_equal) goto loc_002780EE;
    result = (*(unsigned __int64 *)(a1)) >> (32);
loc_00278064:
    if ((((unsigned int)(result)) & (0x3FFULL)) != 0) goto loc_00277C53;
    a3 = (6) >> (9);
    a3 = (a3) & (result);
    a3 = (a3) + (v_stack_mE0);
    if (a3 != ((unsigned int)(v_stack_p120))) goto loc_0027821F;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p38 + 184))) & (15));
    if (condition_is_not_equal) goto loc_00278470;
    v_r15 = 0;
loc_002780CB:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8 + 8) = v_stack_p38 + 176;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8) = 0;
    result = KxTryToAcquireQueuedSpinLock(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8, v_stack_p38 + 176, *(unsigned __int64 *)(gs_base + (0 + 32)), 1);
    goto loc_002781A6;
loc_002780EE:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2 + 2 + 2500 * 2 * 8 + 16)) >> (16);
    goto loc_00278064;
loc_002780FB:
    if (((*(unsigned __int64 *)(v_rip + 13953410)) & (0x600000ULL)) == 0) goto loc_00278155;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_00278155;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_00278155;
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 32))) >> (3);
    a1 = (unsigned int)((a1) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    result = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (66)) == 0) { result = result; }
loc_00278155:
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_002785EA;
    if (condition_is_below) goto loc_002785EA;
    a1 = (result) & (result);
    a1 = (a1) | (result);
    if (((*(unsigned __int64 *)(v_rip + 13953272)) & (0x2000000ULL)) != 0) {
    }
    result = (((*(unsigned __int64 *)(v_rip + 13953272)) & (0x2000000ULL)) == 0) ? 1 : 0;
loc_002781A6:
    if ((unsigned int)(result) == 0) goto loc_00278804;
loc_002781AE:
    if (6 == ((unsigned int)(v_stack_p120))) goto loc_00278341;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p38 + 184)))) & (15)) == 0) goto loc_002782BE;
loc_002781C9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p38 + 184)))) & (15)) != 0) goto loc_00278409;
loc_002781D8:
loc_002781E6:
    v_rsi = (6) >> (9);
    v_rsi = (v_rsi) & ((unsigned int)(*(unsigned int *)(v_stack_p38 + 184)));
    v_rsi = (v_rsi) + (v_stack_p38);
    v_r12 = (unsigned int)((v_r12) + 1);
    v_rbp = (v_stack_p30) + 1;
    v_stack_p40 = v_rsi;
    v_stack_p30 = v_rbp;
    goto loc_0027778C;
loc_0027821F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p38 + 184)))) & (15)) != 0) goto loc_0027826B;
    if ((*(unsigned __int64 *)(gs_base + (0 + 32))) < v_stack_mB0) goto loc_0027826B;
    if ((*(unsigned __int64 *)(gs_base + (0 + 32))) > v_stack_mB0) goto loc_0027826B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) != 0) goto loc_002788FC;
loc_0027826B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p38 + 184)))) & (15)) != 0) goto loc_002784A2;
loc_0027827A:
    if ((*(unsigned __int64 *)(gs_base + (0 + 32))) < v_stack_mB0) goto loc_00278155;
    if ((*(unsigned __int64 *)(gs_base + (0 + 32))) > v_stack_mB0) goto loc_00278155;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32))))) & (1)) == 0) goto loc_002785EA;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32))))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32))))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a2))) != 0) goto loc_00278155;
    goto loc_002780FB;
loc_002782BE:
    if (v_rsi < v_stack_mB0) goto loc_002781C9;
    if (v_rsi > v_stack_mB0) goto loc_002781C9;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) == 0) goto loc_002781C9;
    result = (v_rsi) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + result * 4)))) & (0x3FFFFFFFULL)) != 0) goto loc_0027855A;
    if (!sign_flag) goto loc_002788C5;
    if (((*(unsigned __int8 *)(v_rip + 13952979)) & (1)) != 0) goto loc_00278939;
loc_00278339:
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + result * 4) = 0;
    goto loc_002781E6;
loc_00278341:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p38 + 184))) & (15));
    if (condition_is_not_equal) goto loc_00278576;
loc_0027835E:
    v_rdi = (*(unsigned __int64 *)(gs_base + (0 + 32)) + 40000) + (48);
    if (((*(unsigned __int8 *)(v_rip + 13952919)) & (1)) != 0) goto loc_00278537;
loc_00278375:
    if (*(unsigned __int64 *)(v_rdi) != 0) goto loc_0027839A;
    if (*(unsigned __int64 *)(v_rdi) == 0) goto loc_002781E6;
    result = KxWaitForLockChainValid(v_rdi, *(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288));
loc_0027839A:
    *(unsigned __int64 *)(v_rdi) = 0;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_rdi + 8)) ^ ((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 8))));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_002781E6;
    a3 = (result + 8) >> (5);
    a3 = (unsigned int)((a3) & (127));
    result = KeDisableInterrupts(*(unsigned __int64 *)(v_rdi + 8), *(unsigned __int64 *)(gs_base + (0 + 32)), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288));
    result = KiHaltOnAddressWakeEntireList(*(unsigned __int64 *)(v_rdi + 8), 0, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288));
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_002781E6;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00278838;
loc_00278403:
    goto loc_002781E6;
loc_00278409:
    if (v_rsi < v_stack_mB0) goto loc_002781D8;
    if (v_rsi > v_stack_mB0) goto loc_002781D8;
    a1 = (v_rsi) - (v_stack_mB0);
    a1 = (a1) >> (3);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a1 + a1 * 1))) & (31));
    a2 = (unsigned int)((2) << ((unsigned __int8)(a1)));
    a2 = (unsigned int)(~(a2));
    result = ((unsigned int)((unsigned int)(a1 + a1 * 1))) >> (5);
    goto loc_002781E6;
loc_00278470:
    if (((unsigned __int8)(result)) == 7) goto loc_0027873C;
    a1 = 3;
    if (((unsigned __int8)(result)) == 5) { a1 = 0; }
loc_00278489:
    goto loc_002780CB;
loc_002784A2:
    if ((a1 + a1 * 1) < v_stack_mB0) goto loc_0027827A;
    if ((a1 + a1 * 1) > v_stack_mB0) goto loc_0027827A;
    a3 = (a1 + a1 * 1) - (v_stack_mB0);
    a3 = (a3) >> (3);
    result = ((unsigned int)((unsigned int)(a3 + a3 * 1))) >> (5);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a3 + a3 * 1))) & (31));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2589928 + 14873004 + result * 4))))) >> ((unsigned __int8)((unsigned int)((unsigned int)(a2)))));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00278801;
    a3 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(a2)))));
    a2 = (unsigned int)((2) << ((unsigned __int8)((unsigned int)((unsigned int)(a2)))));
    a3 = (unsigned int)((a3) | ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2589928 + 14873004 + result * 4)))));
    a2 = (unsigned int)(~(a2));
    a3 = (unsigned int)((a3) & ((unsigned int)(a2)));
    if (condition_is_not_equal) goto loc_00278801;
    v_r15 = 0;
    goto loc_002781AE;
loc_00278537:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13195547))) != 0) goto loc_00278375;
    result = KiReleaseQueuedSpinLockInstrumented((unsigned __int8)(result), v_stack_p118, a3, v_rip - 2589928 + 14873004 + result * 4);
    goto loc_002781E6;
loc_0027855A:
    if (((*(unsigned __int8 *)(v_rip + 13952421)) & (1)) != 0) goto loc_00278959;
loc_00278567:
    goto loc_002781E6;
loc_00278576:
    if (((unsigned __int8)(result)) == 7) goto loc_002787F7;
    a1 = 72;
    if (((unsigned __int8)(result)) == 5) { a1 = 0; }
    goto loc_0027835E;
loc_0027858E:
    result = (unsigned int)((result) & (0xFFFFFFFEULL));
    v_stack_p138 = -1;
    *(unsigned int *)(a1 + 4) = (unsigned int)(result);
    if ((((unsigned __int8)(a1)) & (4)) == 0) goto loc_002787BD;
    result = MiLockWorkingSetShared(*(unsigned __int64 *)(a1 + 32), v_stack_p118, a3, v_rip - 2589928 + 14873004 + result * 4);
loc_002785B5:
    goto loc_002776BC;
loc_002785EA:
    v_r15 = 0;
    goto loc_002781A6;
loc_002785F5:
loc_002785FA:
    goto loc_00277BE3;
loc_00278606:
loc_0027860D:
    if (condition_is_not_equal) goto loc_0027860D;
    if (condition_is_above_or_equal) goto loc_00277E74;
    result = KiRemoveSystemWorkPriorityKick(v_stack_p60, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p128))))), (unsigned int)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_00277E74;
loc_0027862E:
    goto loc_00277CE7;
loc_00278638:
    if (v_rsi < v_stack_p68) goto loc_00277C87;
    if (v_rsi > v_stack_p60) goto loc_00277C87;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) == 0) goto loc_00277C7D;
    v_rsi = (v_rsi) >> (3);
    v_rsi = (unsigned int)((v_rsi) & (511));
    result = ExReleaseSpinLockRegardlessFromDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + v_rsi * 4, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p128))))), (unsigned int)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_00277CA4;
loc_00278699:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p38 + 184))) & (15));
    if (condition_is_not_equal) goto loc_0027881A;
    v_r15 = 0;
loc_002786B9:
    a2 = (*(unsigned __int64 *)(gs_base + (0 + 32))) + (0x9C40ULL);
    a1 = (48) + (a2);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(a1, a2, (unsigned int)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_00277CA7;
loc_002786CD:
    if (v_rsi < v_stack_p68) goto loc_00277C96;
    if (v_rsi > a1) goto loc_00277C96;
    v_rsi = (v_rsi) - (v_stack_p68);
    v_rsi = (v_rsi) >> (3);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi + v_rsi * 1))) & (31));
    a2 = (unsigned int)((2) << ((unsigned __int8)(a1)));
    a2 = (unsigned int)(~(a2));
    result = ((unsigned int)((unsigned int)(v_rsi + v_rsi * 1))) >> (5);
    goto loc_00277CA4;
loc_00278727:
    goto loc_002779CB;
loc_0027873C:
    v_r15 = 0;
    goto loc_00278489;
loc_00278749:
    v_rdi = (v_stack_p48) >> (9);
    v_rdi = (v_rdi) & ((unsigned int)(*(unsigned int *)(v_rip - 2589928 + 14873004 + result * 4)));
    v_rdi = (v_rdi) + (v_rip - 2589928 + 14873004 + result * 4);
    v_stack_p78 = v_rdi;
    v_rdi = (v_rdi) >> (9);
    v_rdi = (v_rdi) & ((unsigned int)(*(unsigned int *)(v_rip - 2589928 + 14873004 + result * 4)));
    v_rdi = (v_rdi) + (v_rip - 2589928 + 14873004 + result * 4);
    v_stack_p80 = v_rdi;
    v_rdi = (v_rdi) >> (9);
    v_rdi = (v_rdi) & ((unsigned int)(*(unsigned int *)(v_rip - 2589928 + 14873004 + result * 4)));
    v_rdi = (v_rdi) + (v_rip - 2589928 + 14873004 + result * 4);
    v_stack_p88 = v_rdi;
    v_rdi = (v_rdi) >> (9);
    v_rdi = (v_rdi) & ((unsigned int)(*(unsigned int *)(v_rip - 2589928 + 14873004 + result * 4)));
    v_rdi = (v_rdi) + (v_rip - 2589928 + 14873004 + result * 4);
    v_stack_p90 = v_rdi;
    goto loc_002776BC;
loc_002787B6:
    goto loc_00277BE3;
loc_002787BD:
    result = MiLockWorkingSetExclusive(v_stack_p60, a2, (unsigned int)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_002785B5;
loc_002787C7:
    if ((v_rip - 2589928 + 14873004 + result * 4) != (v_rip + 2127410)) goto loc_002789B3;
    result = MiDeleteEmptyPageTable(v_stack_p60, a2, (unsigned int)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_00277811;
loc_002787E1:
    goto loc_0027785B;
loc_002787ED:
    result = MiLockWorkingSetExclusive(v_stack_p60, v_rip - 2589928 + 14873004 + result * 4 + 192, (unsigned int)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_00277CE7;
loc_002787F7:
    goto loc_0027835E;
loc_00278801:
    v_r15 = 0;
loc_00278804:
    result = MiUnlockPageTable(v_stack_p38, v_rsi, (unsigned int)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    result = 0;
    *(unsigned __int64 *)(a1 + 56) = 0;
    goto loc_00277D80;
loc_0027881A:
    if (0 == 7) goto loc_002788E0;
    a1 = 72;
    if (0 == 5) { a1 = 0; }
    goto loc_002786B9;
loc_00278838:
loc_0027883F:
    if (0 != 5) goto loc_0027883F;
    if (0 >= 5) goto loc_00278403;
    result = KiRemoveSystemWorkPriorityKick(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p128))))), (unsigned int)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_00278403;
loc_00278860:
    v_r15 = 0;
    if (*(unsigned __int64 *)(a1 + 56) != 0) {
        a1 = v_stack_p38;
        result = MiUnlockPageTable(a1, *(unsigned __int64 *)(a1 + 56), (unsigned int)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
        v_r15 = 0;
        *(unsigned __int64 *)(a1 + 56) = 0;
    }
    result = 0;
    goto loc_00277D80;
loc_00278881:
    if (v_rsi != (v_rip + 2140664)) goto loc_002789C0;
    result = MiDeleteEmptyPageTableTail(a1, *(unsigned __int64 *)(a1 + 56), (unsigned int)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_00277C14;
loc_0027889E:
    v_stack_p30 = (int)((unsigned int)(v_r12));
    v_rdi = (unsigned int)((unsigned int)(v_rsi));
    if (((unsigned int)((unsigned int)(v_rsi))) < (*(unsigned __int64 *)(v_rsp + (int)((unsigned int)(v_r12)) * 8 + 120))) { v_rdi = *(unsigned __int64 *)(v_rsp + (int)((unsigned int)(v_r12)) * 8 + 120); }
    result = MiGetLeafVa(v_rdi + 8, *(unsigned __int64 *)(a1 + 56), (unsigned int)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    v_stack_p48 = result;
    goto loc_0027778C;
loc_002788C5:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 16, v_rdi + 8, 256, a4);
loc_002788E0:
    a2 = (v_rdi + 8) + (0x9C40ULL);
    a1 = (24) + (a2);
    v_r15 = 0;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(a1, a2, 256, a4);
    goto loc_00277CA7;
loc_002788FC:
    a3 = (unsigned int)((256) >> (3));
    a3 = (unsigned int)((a3) & (511));
    result = ExTryAcquireSpinLockExclusiveAtDpcLevel(a1 + a3 * 4, a2, a3, a4);
    v_r15 = 0;
    goto loc_002781A6;
loc_00278918:
loc_0027891C:
    v_rbp = ((int)((unsigned int)(v_r12))) >> (9);
    v_rbp = (v_rbp) & ((unsigned int)(*(unsigned int *)(v_rip - 2589928 + 14873004 + result * 4)));
    v_rbp = (v_rbp) + (0);
    a1 = (v_stack_p68 - 1) - (1);
    if (condition_is_not_equal) goto loc_0027891C;
    v_stack_p58 = v_rbp;
    goto loc_00277D2C;
loc_00278939:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13194521))) != 0) goto loc_00278339;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(a1, v_stack_p118, a3, a4);
    goto loc_002781E6;
loc_00278959:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13194489))) != 0) goto loc_00278567;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(a1, v_stack_p118, a3, a4);
    goto loc_002781E6;
loc_00278979:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - ((unsigned int)(v_stack_p68)));
loc_00278989:
    v_rsi = (v_rsi) >> (9);
    v_rsi = (v_rsi) & (v_stack_p118);
    v_rdi = (v_rdi) >> (9);
    v_rsi = (v_rsi) + (v_stack_p38);
    v_rdi = (v_rdi) & (v_stack_p118);
    v_rdi = (v_rdi) + (v_stack_p38);
    a1 = (a1) - (1);
    if (condition_is_not_equal) goto loc_00278989;
    v_stack_p40 = v_rsi;
    goto loc_0027773F;
loc_002789B3:
    result = guard_dispatch_icall(a1, v_stack_p118, a3, a4);
    goto loc_00277811;
loc_002789C0:
    result = guard_dispatch_icall(a1, v_stack_p118, a3, a4);
    goto loc_00277C14;
}
```

## 5. (Beta) C Style

```c
int64_t MiDeleteVaDirect(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_p0;
    uint32_t v_stack_p10;
    uint64_t v_stack_p118;
    uint32_t v_stack_p120;
    uint32_t v_stack_p128;
    uint64_t v_stack_p138;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint32_t v_stack_p8;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;

    local_rsp = (local_rsp) - (216);
    v_stack_m78 = *(uint64_t *)(arg1 + 0xB0);
    local_r15 = 0;
    v_stack_mE0 = *(uint64_t *)(arg1 + 0x20);
    a3 = 0;
    if ((*(uint64_t *)(arg1 + 0xA8)) != (v_rip + 5212)) { a3 = 8; }
    v_stack_p10 = (uint32_t)(a3);
    result = ((*(uint64_t *)(arg1 + 0xA8)) != (v_rip + 5212)) ? 1 : 0;
    v_stack_mB0 = result + 1;
    Arg1 = (*(uint64_t *)(arg1 + 0x28)) >> (9);
    Arg1 = (Arg1) & (local_r10);
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0xA0)));
    Arg1 = (Arg1) + (a4);
    v_stack_mA0 = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (local_r10);
    Arg1 = (Arg1) + (a4);
    *(void **)(local_rsp - 0x98) = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (local_r10);
    Arg1 = (Arg1) + (a4);
    *(void **)(local_rsp - 0x90) = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (local_r10);
    Arg1 = (Arg1) + (a4);
    *(void **)(local_rsp - 0x88) = Arg1;
    Arg1 = (*(uint64_t *)(arg1 + 0x30)) >> (9);
    Arg1 = (Arg1) & (local_r10);
    Arg1 = (Arg1) + (a4);
    *(void **)(local_rsp - 0x70) = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (local_r10);
    Arg1 = (Arg1) + (a4);
    *(void **)(local_rsp - 0x68) = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (local_r10);
    Arg1 = (Arg1) + (a4);
    *(void **)(local_rsp - 0x60) = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (local_r10);
    Arg1 = (Arg1) + (a4);
    *(void **)(local_rsp - 0x58) = Arg1;
    v_stack_mA8 = *(uint64_t *)(local_rsp + result + 0x1 * 8 + 0xA8);
    v_stack_p20 = -1;
    v_stack_mC0 = *(uint64_t *)(local_rsp + result + 0x1 * 8 + 0x78);
    local_r15 = (a4) << (25);
    v_stack_mC8 = local_r15;
loc_002776BC:
    if ((*(uint64_t *)(local_rsp + result + 0x1 * 8 + 0x78)) > (*(uint64_t *)(local_rsp + result + 0x1 * 8 + 0xA8))) goto loc_00277D7E;
    if ((*(uint64_t *)(local_rsp + result + 0x1 * 8 + 0x78)) < a4) goto loc_002776FE;
loc_002776E0:
    if ((*(uint64_t *)(local_rsp + result + 0x1 * 8 + 0x78)) > local_r10) goto loc_002776FE;
    a2 = (*(uint64_t *)(local_rsp + result + 0x1 * 8 + 0x78)) << (25);
    a2 = (a2) - (local_r15);
    a2 = (a2) >> (16);
    if (a2 >= a4) goto loc_002776E0;
loc_002776FE:
    result = MiFastLockLeafPageTable(*(uint64_t *)(arg1 + 0x20), a2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_0027887A;
    v_stack_mD8 = *(uint64_t *)(local_rsp + result + 0x1 * 8 + 0x78);
    local_rdi = (*(uint64_t *)(local_rsp + result + 0x1 * 8 + 0x78)) << (25);
    local_rdi = (local_rdi) - (local_r15);
    v_stack_mB8 = local_r15;
    local_rdi = (local_rdi) >> (16);
    if (((uint32_t)(result + 1)) < ((uint32_t)(result))) goto loc_00278979;
loc_0027773F:
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(result))) - (1));
    if (condition_is_not_equal) goto loc_0027889E;
    v_stack_mD0 = *(uint64_t *)(local_rsp + result + 0x1 * 8 + 0x78) + 8;
    if ((*(uint64_t *)(local_rsp + result + 0x1 * 8 + 0x78) + 8) < (*(uint64_t *)(arg1 + 0x20))) goto loc_00277784;
loc_00277764:
    if ((*(uint64_t *)(local_rsp + result + 0x1 * 8 + 0x78) + 8) > a2) goto loc_0027777F;
    Arg1 = (*(uint64_t *)(local_rsp + result + 0x1 * 8 + 0x78) + 8) << (25);
    Arg1 = (Arg1) - (local_r15);
    Arg1 = (Arg1) >> (16);
    if (Arg1 >= (*(uint64_t *)(arg1 + 0x20))) goto loc_00277764;
loc_0027777F:
    v_stack_mD0 = Arg1;
loc_00277784:
    v_stack_mE8 = (int32_t)((uint32_t)(local_r12));
loc_0027778C:
    *(uint64_t *)(arg1 + 0x38) = *(uint64_t *)(local_rsp + result + 0x1 * 8 + 0x78);
    if (local_rdi < (*(uint64_t *)(local_rsp + (int32_t)((uint32_t)(local_r12)) * 8 + 0x78))) { local_rdi = *(uint64_t *)(local_rsp + (int32_t)((uint32_t)(local_r12)) * 8 + 0x78); }
    v_stack_m80 = *(uint64_t *)(arg1 + 0xA8);
    if ((uint32_t)(local_r12) != 0) goto loc_002777D8;
    local_r13 = (local_rdi) & (-8);
    local_r13 = (local_r13) | (0xFF8ULL);
    if (local_r13 >= = (*(uint64_t *)(local_rsp + (int32_t)((uint32_t)(local_r12)) * 8 + 0xA8))) {
        local_r13 = *(uint64_t *)(local_rsp + (int32_t)((uint32_t)(local_r12)) * 8 + 0xA8);
    }
    local_rsi = 0;
    v_stack_p8 = 0;
loc_002777E1:
    if (local_rdi > local_r13) goto loc_002785F5;
    if ((uint32_t)(local_r12) != 0) goto loc_00277B8B;
loc_002777F3:
    if ((*(uint64_t *)(arg1 + 0xA8)) != (v_rip + 4582)) goto loc_002787C7;
    result = MiDeleteVa(Arg1, local_rdi, (uint32_t)((uint32_t)(local_r12)), *(uint64_t *)(arg1 + 0xA8));
loc_00277811:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (2)) == 0) goto loc_002778A1;
    if (((*(uint8_t *)(arg1 + 0x8)) & ((uint8_t)(*(uint64_t *)(arg1 + 0xA0)))) != 0) goto loc_002778A1;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) & (4));
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8))) & (15));
    if (((uint8_t)(result)) > 5) goto loc_00277913;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0xB8))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_002787E1;
loc_0027785B:
    if ((uint32_t)(Arg1) == 0) goto loc_002778F5;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) == 0) goto loc_002778F1;
loc_00277881:
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x144))) << (6);
    if (condition_is_above_or_equal) goto loc_00277913;
loc_00277892:
    v_stack_p8 = 2;
    goto loc_002778A1;
loc_0027789F:
    local_rsi = 0;
loc_002778A1:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC))) + 1);
    *(uint32_t *)(arg1 + 0xC) = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x48) = local_rdi + result * 8;
    result = (local_rdi + result * 8) << (25);
    result = (result) - (v_stack_mC8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x58) = local_rdi + result * 8;
    result = (result) >> (16);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)) + 0x38) = result;
    if (v_stack_p8 == 2) goto loc_00277F11;
    goto loc_002777E1;
loc_002778F1:
    goto loc_00277881;
loc_002778F5:
loc_002778F8:
    if (0 >= 4) goto loc_00277913;
    result = (0) << (6);
    if (condition_is_below) goto loc_00277892;
    a3 = (uint32_t)((0) + 1);
    goto loc_002778F8;
loc_00277913:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (4)) == 0) goto loc_002779D1;
    a3 = (local_rdi + result * 8) >> (9);
    a3 = (a3) & ((uint32_t)(*(uint32_t *)(arg1)));
    a3 = (a3) + (*(uint64_t *)(arg1 + 0x20));
    if (a3 == (*(uint64_t *)(arg1 + 0x20))) goto loc_00277D95;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m80 + 0xB8)))) & (15)) == 0) goto loc_00277A5A;
loc_0027795C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m80 + 0xB8)))) & (15)) == 0) goto loc_0027798F;
    if (a3 < ((uint32_t)(*(uint32_t *)(result + *(uint64_t *)(v_rip + 0xBC0FE5) * 1)))) goto loc_0027798F;
    if (a3 <= ((uint32_t)(*(uint32_t *)(result + *(uint64_t *)(v_rip + 0xBC0FE5) * 1)))) goto loc_00277DC2;
loc_0027798F:
    if (a3 < ((uint32_t)(*(uint32_t *)(result + *(uint64_t *)(v_rip + 0xBC0FE5) * 1)))) goto loc_002779C2;
    if (a3 > ((uint32_t)(*(uint32_t *)(result + *(uint64_t *)(v_rip + 0xBC0FE5) * 1)))) goto loc_002779C2;
    if ((((uint8_t)(*(uint64_t *)(a3))) & (1)) == 0) goto loc_002779C2;
    a2 = ((((uint8_t)(*(uint64_t *)(a3))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(a3))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(a2))) == 0) goto loc_00277ACF;
loc_002779C2:
    result = (*(uint64_t *)(a3)) >> (60);
    result = (uint32_t)((result) & (2));
loc_002779C9:
loc_002779CB:
    if ((uint32_t)(result) != 0) goto loc_00277892;
loc_002779D1:
    if ((*(uint8_t *)(arg1 + 0x9)) >= 2) goto loc_002778A1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)))) & (1)) != 0) goto loc_00277B38;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20)) != 0) goto loc_00277E14;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)))) & (30)) != 0) goto loc_00277B5F;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38B9)) != 0) goto loc_00277E3B;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10) != 0) goto loc_00277E00;
loc_00277A35:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x83AC)))) <= 7) goto loc_002778A1;
    if (0 == 0) goto loc_00277E45;
loc_00277A47:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BC)))) & (30)) == 0) goto loc_00277E7A;
    goto loc_00277B64;
loc_00277A5A:
    if (0 < (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10))) goto loc_0027795C;
    if (0 > (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x10))) goto loc_0027795C;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) == 0) goto loc_0027795C;
    a3 = (uint32_t)((0) >> (3));
    a3 = (uint32_t)((a3) & (511));
    result = 5;
    if (condition_is_below) { result = 1; }
    goto loc_002779C9;
loc_00277ACF:
    if (((*(uint64_t *)(v_rip + 0xD4EFAE)) & (0x600000ULL)) == 0) goto loc_002779C2;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_002779C2;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_002779C2;
    a3 = (a3) >> (3);
    a3 = (uint32_t)((a3) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + a3 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    result = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + a3 * 8))) & (66)) == 0) { result = result; }
    goto loc_002779C2;
loc_00277B38:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x865C)))) <= 7) goto loc_00277A35;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + a3 * 8) + 0x38B9)) == 0) goto loc_00277A47;
    goto loc_00277B64;
loc_00277B5F:
loc_00277B64:
    result = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + a3 * 8) + 0x38B9);
    if (((*(uint32_t *)(v_rip + 0xD4EF96)) & (0x4000000ULL)) != 0) {
        a3 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x865C)));
        a2 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x83AC)));
        Arg1 = 2;
        result = EtwTraceShouldYieldProcessor(Arg1, a2, a3, 0);
    }
    if (2 == 0) goto loc_0027789F;
    local_rsi = 0;
    goto loc_00277892;
loc_00277B8B:
    if ((local_rdi + result * 8) < Arg1) goto loc_00277BC8;
    if ((local_rdi + result * 8) > Arg1) goto loc_00277BC8;
    if ((((uint8_t)(*(uint64_t *)(local_rdi + result * 8))) & (1)) == 0) goto loc_00277BC8;
    a2 = ((((uint8_t)(*(uint64_t *)(local_rdi + result * 8))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(local_rdi + result * 8))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(a2))) == 0) goto loc_00277E8E;
loc_00277BC8:
    if (*(uint64_t *)(local_rdi + result * 8) == 0) goto loc_002777F3;
    if ((((uint8_t)(*(uint64_t *)(local_rdi + result * 8))) & (1)) != 0) goto loc_002777F3;
loc_00277BE3:
loc_00277BED:
    if (v_stack_m78 != (v_rip + 2081524)) goto loc_00278881;
    result = MiDecommitPagesTail(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8)), a2, a3, 0);
loc_00277C14:
    if (5 == 5) goto loc_00278860;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) & (1)) != 0) goto loc_0027858E;
    Arg1 = (condition_is_above_or_equal) ? 1 : 0;
    result = (((v_stack_p18) & (128)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00277F94;
loc_00277C53:
    if (v_stack_mD8 == result) goto loc_00278699;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + 0xB8)))) & (15)) == 0) goto loc_00278638;
loc_00277C7D:
loc_00277C87:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + 0xB8)))) & (15)) != 0) goto loc_002786CD;
loc_00277C96:
loc_00277CA4:
    local_r15 = 0;
loc_00277CA7:
    *(uint64_t *)(arg1 + 0x38) = 0;
    if (5 != 2) goto loc_0027862E;
    result = MiReleaseWalkLocks(Arg1, a2, a3, 0);
    v_stack_p20 = -1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (4)) == 0) goto loc_002787ED;
    result = MiLockWorkingSetShared(*(uint64_t *)(arg1 + 0x20), a2, a3, 0);
loc_00277CE7:
    local_rbp = (v_stack_p20) >> (18);
    local_rbp = (uint32_t)((local_rbp) & (0x3FFFFFF8ULL));
    local_rbp = (local_rbp) + (result);
    v_stack_mC0 = local_rbp;
    if (((uint32_t)(v_stack_mB0)) > 1) goto loc_00278918;
loc_00277D2C:
    if (v_stack_m70 < 0) goto loc_00277D75;
    a2 = (0) << (25);
loc_00277D50:
    if (v_stack_m70 > 1) goto loc_00277D6B;
    Arg1 = (v_stack_m70) << (25);
    Arg1 = (Arg1) - (a2);
    Arg1 = (Arg1) >> (16);
    if (Arg1 >= 0) goto loc_00277D50;
loc_00277D6B:
loc_00277D75:
    if (v_stack_p20 <= Arg1) goto loc_00278749;
loc_00277D7E:
loc_00277D80:
    local_rsp = (local_rsp) + (216);
    return 1;
loc_00277D95:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(0 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_00277EF9;
loc_00277DB2:
    goto loc_002779CB;
loc_00277DC2:
    a3 = (a3) - (48);
    a3 = (a3) >> (3);
    result = ((uint32_t)((uint32_t)(a3 + a3 * 1))) >> (5);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(a3 + a3 * 1))) & (31));
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip - 0x277DE6 + result * 4 + 0xE2F1AC))) >> ((uint8_t)(Arg1)));
    if ((((uint8_t)(a2)) & (2)) == 0) goto loc_002779D1;
    goto loc_00277892;
loc_00277E00:
    if (result == (*(uint64_t *)(arg1 + 0x8))) goto loc_00277A35;
    goto loc_00277B64;
loc_00277E14:
    if (((uint32_t)(local_rbp)) <= 7) goto loc_002778A1;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x38B9)) == 0) goto loc_00277A47;
    goto loc_00277B64;
loc_00277E3B:
    goto loc_00277B64;
loc_00277E45:
    if (1 != 0) goto loc_00277A47;
loc_00277E4E:
    *(uint32_t *)(arg1 + 0x83AC) = 3;
    *(uint32_t *)(arg1 + 0x865C) = 3;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00278606;
loc_00277E74:
    goto loc_00277B64;
loc_00277E7A:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18))) goto loc_00277E4E;
    goto loc_00277B64;
loc_00277E8E:
    if (((*(uint64_t *)(v_rip + 0xD4EBEF)) & (0x600000ULL)) == 0) goto loc_00277BC8;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_00277BC8;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_00277BC8;
    Arg1 = (v_stack_p20) >> (3);
    Arg1 = (uint32_t)((Arg1) & (511));
    result = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (32)) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18)) | (32);
    }
    result = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (66)) == 0) { result = result; }
    goto loc_00277BC8;
loc_00277EF9:
    if (((uint8_t)(result)) == 7) goto loc_00278727;
    Arg1 = 72;
    if (((uint8_t)(result)) == 5) { Arg1 = 6; }
    goto loc_00277DB2;
loc_00277F11:
    if (v_stack_p20 > (*(uint64_t *)(local_rsp + v_stack_p30 * 8 + 0xA8))) goto loc_002787B6;
    if (v_stack_p138 != -1) goto loc_002785FA;
    v_stack_p138 = v_stack_p20;
    if (v_stack_p20 < v_stack_mE0) goto loc_00277F88;
loc_00277F60:
    if (v_stack_p20 > v_stack_p30) goto loc_00277F7B;
    a2 = (v_stack_p20) << (25);
    a2 = (a2) - (Arg1);
    a2 = (a2) >> (16);
    if (a2 >= v_stack_mE0) goto loc_00277F60;
loc_00277F7B:
    v_stack_p138 = a2;
loc_00277F88:
    goto loc_00277BED;
loc_00277F94:
    if (((uint32_t)(local_r12)) == 3) goto loc_00277C53;
    if (6 < v_stack_mB0) goto loc_00278027;
    if (6 > v_stack_mB0) goto loc_00278027;
    if ((((uint8_t)(*(uint64_t *)(6))) & (1)) == 0) goto loc_00278027;
    Arg1 = ((((uint8_t)(*(uint64_t *)(6))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(6))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_00278027;
    if (((*(uint64_t *)(v_rip + 0xD4EAAD)) & (0x600000ULL)) == 0) goto loc_00278027;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_00278027;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_00278027;
    result = (6) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (32)) != 0) {
        a2 = (*(uint64_t *)(6)) | (32);
    }
    a2 = (a2) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (66)) == 0) { a2 = a2; }
loc_00278027:
    a2 = (a2) >> (12);
    a2 = (a2) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8));
    Arg1 = (a2 + a2 * 2) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8));
    if (condition_is_above_or_equal) goto loc_002780EE;
    result = (*(uint64_t *)(arg1)) >> (32);
loc_00278064:
    if ((((uint32_t)(result)) & (0x3FFULL)) != 0) goto loc_00277C53;
    a3 = (6) >> (9);
    a3 = (a3) & (result);
    a3 = (a3) + (v_stack_mE0);
    if (a3 != ((uint32_t)(v_stack_p120))) goto loc_0027821F;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p38 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_00278470;
    local_r15 = 0;
loc_002780CB:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 + 0x9C4 * 2 * 8 + 0x8) = v_stack_p38 + 176;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 + 0x9C4 * 2 * 8) = 0;
    result = KxTryToAcquireQueuedSpinLock(*(uint64_t *)(gs_base + (0 + 0x20)) + 2 + 2 + 2500 * 2 * 8, v_stack_p38 + 176, *(uint64_t *)(gs_base + (0 + 0x20)), 1);
    goto loc_002781A6;
loc_002780EE:
    result = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x2 + 0x2 + 0x9C4 * 2 * 8 + 0x10)) >> (16);
    goto loc_00278064;
loc_002780FB:
    if (((*(uint64_t *)(v_rip + 0xD4E982)) & (0x600000ULL)) == 0) goto loc_00278155;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_00278155;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_00278155;
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x20))) >> (3);
    Arg1 = (uint32_t)((Arg1) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    result = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (66)) == 0) { result = result; }
loc_00278155:
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_002785EA;
    if (condition_is_below) goto loc_002785EA;
    Arg1 = (result) & (result);
    Arg1 = (Arg1) | (result);
    if (((*(uint64_t *)(v_rip + 0xD4E8F8)) & (0x2000000ULL)) != 0) {
    }
    result = (((*(uint64_t *)(v_rip + 0xD4E8F8)) & (0x2000000ULL)) == 0) ? 1 : 0;
loc_002781A6:
    if ((uint32_t)(result) == 0) goto loc_00278804;
loc_002781AE:
    if (6 == ((uint32_t)(v_stack_p120))) goto loc_00278341;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p38 + 0xB8)))) & (15)) == 0) goto loc_002782BE;
loc_002781C9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p38 + 0xB8)))) & (15)) != 0) goto loc_00278409;
loc_002781D8:
loc_002781E6:
    local_rsi = (6) >> (9);
    local_rsi = (local_rsi) & ((uint32_t)(*(uint32_t *)(v_stack_p38 + 0xB8)));
    local_rsi = (local_rsi) + (v_stack_p38);
    local_r12 = (uint32_t)((local_r12) + 1);
    local_rbp = (v_stack_p30) + 1;
    v_stack_p40 = local_rsi;
    v_stack_p30 = local_rbp;
    goto loc_0027778C;
loc_0027821F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p38 + 0xB8)))) & (15)) != 0) goto loc_0027826B;
    if ((*(uint64_t *)(gs_base + (0 + 0x20))) < v_stack_mB0) goto loc_0027826B;
    if ((*(uint64_t *)(gs_base + (0 + 0x20))) > v_stack_mB0) goto loc_0027826B;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) != 0) goto loc_002788FC;
loc_0027826B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p38 + 0xB8)))) & (15)) != 0) goto loc_002784A2;
loc_0027827A:
    if ((*(uint64_t *)(gs_base + (0 + 0x20))) < v_stack_mB0) goto loc_00278155;
    if ((*(uint64_t *)(gs_base + (0 + 0x20))) > v_stack_mB0) goto loc_00278155;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20))))) & (1)) == 0) goto loc_002785EA;
    a2 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20))))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20))))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(a2))) != 0) goto loc_00278155;
    goto loc_002780FB;
loc_002782BE:
    if (local_rsi < v_stack_mB0) goto loc_002781C9;
    if (local_rsi > v_stack_mB0) goto loc_002781C9;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) == 0) goto loc_002781C9;
    result = (local_rsi) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + result * 4)))) & (0x3FFFFFFFULL)) != 0) goto loc_0027855A;
    if (!sign_flag) goto loc_002788C5;
    if (((*(uint8_t *)(v_rip + 0xD4E7D3)) & (1)) != 0) goto loc_00278939;
loc_00278339:
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + result * 4) = 0;
    goto loc_002781E6;
loc_00278341:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p38 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_00278576;
loc_0027835E:
    local_rdi = (*(uint64_t *)(gs_base + (0 + 0x20)) + 40000) + (48);
    if (((*(uint8_t *)(v_rip + 0xD4E797)) & (1)) != 0) goto loc_00278537;
loc_00278375:
    if (*(uint64_t *)(local_rdi) != 0) goto loc_0027839A;
    if (*(uint64_t *)(local_rdi) == 0) goto loc_002781E6;
    result = KxWaitForLockChainValid(local_rdi, *(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508));
loc_0027839A:
    *(uint64_t *)(local_rdi) = 0;
    result = (uint8_t)((*(uint64_t *)(local_rdi + 0x8)) ^ ((uint8_t)(*(uint64_t *)(local_rdi + 0x8))));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_002781E6;
    a3 = (result + 8) >> (5);
    a3 = (uint32_t)((a3) & (127));
    result = KeDisableInterrupts(*(uint64_t *)(local_rdi + 0x8), *(uint64_t *)(gs_base + (0 + 0x20)), a3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508));
    result = KiHaltOnAddressWakeEntireList(*(uint64_t *)(local_rdi + 0x8), 0, a3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508));
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_002781E6;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00278838;
loc_00278403:
    goto loc_002781E6;
loc_00278409:
    if (local_rsi < v_stack_mB0) goto loc_002781D8;
    if (local_rsi > v_stack_mB0) goto loc_002781D8;
    Arg1 = (local_rsi) - (v_stack_mB0);
    Arg1 = (Arg1) >> (3);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg1 + Arg1 * 1))) & (31));
    a2 = (uint32_t)((2) << ((uint8_t)(Arg1)));
    a2 = (uint32_t)(~(a2));
    result = ((uint32_t)((uint32_t)(Arg1 + Arg1 * 1))) >> (5);
    goto loc_002781E6;
loc_00278470:
    if (((uint8_t)(result)) == 7) goto loc_0027873C;
    Arg1 = 3;
    if (((uint8_t)(result)) == 5) { Arg1 = 0; }
loc_00278489:
    goto loc_002780CB;
loc_002784A2:
    if ((Arg1 + Arg1 * 1) < v_stack_mB0) goto loc_0027827A;
    if ((Arg1 + Arg1 * 1) > v_stack_mB0) goto loc_0027827A;
    a3 = (Arg1 + Arg1 * 1) - (v_stack_mB0);
    a3 = (a3) >> (3);
    result = ((uint32_t)((uint32_t)(a3 + a3 * 1))) >> (5);
    a2 = (uint32_t)(((uint32_t)((uint32_t)(a3 + a3 * 1))) & (31));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x2784E8 + 0xE2F1AC + result * 4))))) >> ((uint8_t)((uint32_t)((uint32_t)(a2)))));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00278801;
    a3 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(a2)))));
    a2 = (uint32_t)((2) << ((uint8_t)((uint32_t)((uint32_t)(a2)))));
    a3 = (uint32_t)((a3) | ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x2784E8 + 0xE2F1AC + result * 4)))));
    a2 = (uint32_t)(~(a2));
    a3 = (uint32_t)((a3) & ((uint32_t)(a2)));
    if (condition_is_not_equal) goto loc_00278801;
    local_r15 = 0;
    goto loc_002781AE;
loc_00278537:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC9591B))) != 0) goto loc_00278375;
    result = KiReleaseQueuedSpinLockInstrumented((uint8_t)(result), v_stack_p118, a3, v_rip - 2589928 + 14873004 + result * 4);
    goto loc_002781E6;
loc_0027855A:
    if (((*(uint8_t *)(v_rip + 0xD4E5A5)) & (1)) != 0) goto loc_00278959;
loc_00278567:
    goto loc_002781E6;
loc_00278576:
    if (((uint8_t)(result)) == 7) goto loc_002787F7;
    Arg1 = 72;
    if (((uint8_t)(result)) == 5) { Arg1 = 0; }
    goto loc_0027835E;
loc_0027858E:
    result = (uint32_t)((result) & (0xFFFFFFFEULL));
    v_stack_p138 = -1;
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)(result);
    if ((((uint8_t)(Arg1)) & (4)) == 0) goto loc_002787BD;
    result = MiLockWorkingSetShared(*(uint64_t *)(arg1 + 0x20), v_stack_p118, a3, v_rip - 2589928 + 14873004 + result * 4);
loc_002785B5:
    goto loc_002776BC;
loc_002785EA:
    local_r15 = 0;
    goto loc_002781A6;
loc_002785F5:
loc_002785FA:
    goto loc_00277BE3;
loc_00278606:
loc_0027860D:
    if (condition_is_not_equal) goto loc_0027860D;
    if (condition_is_above_or_equal) goto loc_00277E74;
    result = KiRemoveSystemWorkPriorityKick(v_stack_p60, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p128))))), (uint32_t)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_00277E74;
loc_0027862E:
    goto loc_00277CE7;
loc_00278638:
    if (local_rsi < v_stack_p68) goto loc_00277C87;
    if (local_rsi > v_stack_p60) goto loc_00277C87;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) == 0) goto loc_00277C7D;
    local_rsi = (local_rsi) >> (3);
    local_rsi = (uint32_t)((local_rsi) & (511));
    result = ExReleaseSpinLockRegardlessFromDpcLevel(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + local_rsi * 4, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p128))))), (uint32_t)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_00277CA4;
loc_00278699:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p38 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_0027881A;
    local_r15 = 0;
loc_002786B9:
    a2 = (*(uint64_t *)(gs_base + (0 + 0x20))) + (0x9C40ULL);
    Arg1 = (48) + (a2);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(Arg1, a2, (uint32_t)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_00277CA7;
loc_002786CD:
    if (local_rsi < v_stack_p68) goto loc_00277C96;
    if (local_rsi > Arg1) goto loc_00277C96;
    local_rsi = (local_rsi) - (v_stack_p68);
    local_rsi = (local_rsi) >> (3);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi + local_rsi * 1))) & (31));
    a2 = (uint32_t)((2) << ((uint8_t)(Arg1)));
    a2 = (uint32_t)(~(a2));
    result = ((uint32_t)((uint32_t)(local_rsi + local_rsi * 1))) >> (5);
    goto loc_00277CA4;
loc_00278727:
    goto loc_002779CB;
loc_0027873C:
    local_r15 = 0;
    goto loc_00278489;
loc_00278749:
    local_rdi = (v_stack_p48) >> (9);
    local_rdi = (local_rdi) & ((uint32_t)(*(uint32_t *)(v_rip - 0x2784E8 + 0xE2F1AC + result * 4)));
    local_rdi = (local_rdi) + (v_rip - 2589928 + 14873004 + result * 4);
    v_stack_p78 = local_rdi;
    local_rdi = (local_rdi) >> (9);
    local_rdi = (local_rdi) & ((uint32_t)(*(uint32_t *)(v_rip - 0x2784E8 + 0xE2F1AC + result * 4)));
    local_rdi = (local_rdi) + (v_rip - 2589928 + 14873004 + result * 4);
    v_stack_p80 = local_rdi;
    local_rdi = (local_rdi) >> (9);
    local_rdi = (local_rdi) & ((uint32_t)(*(uint32_t *)(v_rip - 0x2784E8 + 0xE2F1AC + result * 4)));
    local_rdi = (local_rdi) + (v_rip - 2589928 + 14873004 + result * 4);
    v_stack_p88 = local_rdi;
    local_rdi = (local_rdi) >> (9);
    local_rdi = (local_rdi) & ((uint32_t)(*(uint32_t *)(v_rip - 0x2784E8 + 0xE2F1AC + result * 4)));
    local_rdi = (local_rdi) + (v_rip - 2589928 + 14873004 + result * 4);
    v_stack_p90 = local_rdi;
    goto loc_002776BC;
loc_002787B6:
    goto loc_00277BE3;
loc_002787BD:
    result = MiLockWorkingSetExclusive(v_stack_p60, a2, (uint32_t)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_002785B5;
loc_002787C7:
    if ((v_rip - 2589928 + 14873004 + result * 4) != (v_rip + 2127410)) goto loc_002789B3;
    result = MiDeleteEmptyPageTable(v_stack_p60, a2, (uint32_t)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_00277811;
loc_002787E1:
    goto loc_0027785B;
loc_002787ED:
    result = MiLockWorkingSetExclusive(v_stack_p60, v_rip - 2589928 + 14873004 + result * 4 + 192, (uint32_t)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_00277CE7;
loc_002787F7:
    goto loc_0027835E;
loc_00278801:
    local_r15 = 0;
loc_00278804:
    result = MiUnlockPageTable(v_stack_p38, local_rsi, (uint32_t)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    result = 0;
    *(uint64_t *)(arg1 + 0x38) = 0;
    goto loc_00277D80;
loc_0027881A:
    if (0 == 7) goto loc_002788E0;
    Arg1 = 72;
    if (0 == 5) { Arg1 = 0; }
    goto loc_002786B9;
loc_00278838:
loc_0027883F:
    if (0 != 5) goto loc_0027883F;
    if (0 >= 5) goto loc_00278403;
    result = KiRemoveSystemWorkPriorityKick(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p128))))), (uint32_t)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_00278403;
loc_00278860:
    local_r15 = 0;
    if (*(uint64_t *)(arg1 + 0x38) != 0) {
        Arg1 = v_stack_p38;
        result = MiUnlockPageTable(Arg1, *(uint64_t *)(arg1 + 0x38), (uint32_t)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
        local_r15 = 0;
        *(uint64_t *)(arg1 + 0x38) = 0;
    }
    result = 0;
    goto loc_00277D80;
loc_00278881:
    if (local_rsi != (v_rip + 2140664)) goto loc_002789C0;
    result = MiDeleteEmptyPageTableTail(Arg1, *(uint64_t *)(arg1 + 0x38), (uint32_t)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    goto loc_00277C14;
loc_0027889E:
    v_stack_p30 = (int32_t)((uint32_t)(local_r12));
    local_rdi = (uint32_t)((uint32_t)(local_rsi));
    if (((uint32_t)((uint32_t)(local_rsi))) < (*(uint64_t *)(local_rsp + (int32_t)((uint32_t)(local_r12)) * 8 + 0x78))) { local_rdi = *(uint64_t *)(local_rsp + (int32_t)((uint32_t)(local_r12)) * 8 + 0x78); }
    result = MiGetLeafVa(local_rdi + 8, *(uint64_t *)(arg1 + 0x38), (uint32_t)(v_stack_p128), v_rip - 2589928 + 14873004 + result * 4);
    v_stack_p48 = result;
    goto loc_0027778C;
loc_002788C5:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 16, local_rdi + 8, 256, a4);
loc_002788E0:
    a2 = (local_rdi + 8) + (0x9C40ULL);
    Arg1 = (24) + (a2);
    local_r15 = 0;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(Arg1, a2, 256, a4);
    goto loc_00277CA7;
loc_002788FC:
    a3 = (uint32_t)((256) >> (3));
    a3 = (uint32_t)((a3) & (511));
    result = ExTryAcquireSpinLockExclusiveAtDpcLevel(Arg1 + a3 * 4, a2, a3, a4);
    local_r15 = 0;
    goto loc_002781A6;
loc_00278918:
loc_0027891C:
    local_rbp = ((int32_t)((uint32_t)(local_r12))) >> (9);
    local_rbp = (local_rbp) & ((uint32_t)(*(uint32_t *)(v_rip - 0x2784E8 + 0xE2F1AC + result * 4)));
    local_rbp = (local_rbp) + (0);
    Arg1 = (v_stack_p68 - 1) - (1);
    if (condition_is_not_equal) goto loc_0027891C;
    v_stack_p58 = local_rbp;
    goto loc_00277D2C;
loc_00278939:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC95519))) != 0) goto loc_00278339;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(Arg1, v_stack_p118, a3, a4);
    goto loc_002781E6;
loc_00278959:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC954F9))) != 0) goto loc_00278567;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(Arg1, v_stack_p118, a3, a4);
    goto loc_002781E6;
loc_00278979:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - ((uint32_t)(v_stack_p68)));
loc_00278989:
    local_rsi = (local_rsi) >> (9);
    local_rsi = (local_rsi) & (v_stack_p118);
    local_rdi = (local_rdi) >> (9);
    local_rsi = (local_rsi) + (v_stack_p38);
    local_rdi = (local_rdi) & (v_stack_p118);
    local_rdi = (local_rdi) + (v_stack_p38);
    Arg1 = (Arg1) - (1);
    if (condition_is_not_equal) goto loc_00278989;
    v_stack_p40 = local_rsi;
    goto loc_0027773F;
loc_002789B3:
    result = guard_dispatch_icall(Arg1, v_stack_p118, a3, a4);
    goto loc_00277811;
loc_002789C0:
    result = guard_dispatch_icall(Arg1, v_stack_p118, a3, a4);
    goto loc_00277C14;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R/W` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x9` | `8` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `W` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R/W` |
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00277560&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
