# KiDeferGroupSchedulingPreemption

- RVA: `0x0020076C`–`0x002010D5` (길이 `2,409` bytes)
- VA: `0x000000014020076C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C6F0`
- 디코드: `628`개 명령, `2,409/2,409` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x002008A6` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x00200924` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020092F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00200957` → [KiIsThreadConstrainedBySchedulingGroup](../30/KiIsThreadConstrainedBySchedulingGroup_function_0030B200.md) (function, `0x0030B200`)
- `0x00200960` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x0020096C` → [KiCheckForMaxOverQuotaScb](KiCheckForMaxOverQuotaScb_function_002027A0.md) (function, `0x002027A0`)
- `0x002009C3` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002009D2` → [KiStartRescheduleContext](../30/KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x00200A05` → [KiFindRescheduleContextEntryForPrcb](../35/KiFindRescheduleContextEntryForPrcb_function_00353060.md) (function, `0x00353060`)
- `0x00200B17` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x00200BA5` → [KiAddThreadToPrcbQueue](../21/KiAddThreadToPrcbQueue_function_00218B00.md) (function, `0x00218B00`)
- `0x00200BC5` → [KiSearchForNewThreadsForRescheduleContext](../25/KiSearchForNewThreadsForRescheduleContext_function_00258620.md) (function, `0x00258620`)
- `0x00200BD7` → [KiCommitRescheduleContext](../30/KiCommitRescheduleContext_function_0030CF20.md) (function, `0x0030CF20`)
- `0x00200BF5` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x00200CB3` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x00200CD5` → [KiInsertDeferredPreemptionApc](../30/KiInsertDeferredPreemptionApc_function_0030A8E8.md) (function, `0x0030A8E8`)
- `0x00200D03` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x00200D19` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x00200DA5` → [EtwTraceXSchedulerPriorityKickSend](../4F/EtwTraceXSchedulerPriorityKickSend_function_004FB2C0.md) (function, `0x004FB2C0`)
- `0x00200DCB` → [EtwTraceScheduleThread](../30/EtwTraceScheduleThread_function_0030B74C.md) (function, `0x0030B74C`)
- `0x00200DE8` → [KiIsThreadConstrainedBySchedulingGroup](../30/KiIsThreadConstrainedBySchedulingGroup_function_0030B200.md) (function, `0x0030B200`)
- `0x00200DF1` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x00200DFD` → [KiCheckForMaxOverQuotaScb](KiCheckForMaxOverQuotaScb_function_002027A0.md) (function, `0x002027A0`)
- `0x00200E41` → [KiReadyDeferredReadyList](../30/KiReadyDeferredReadyList_function_0030DD80.md) (function, `0x0030DD80`)
- `0x00200E6C` → [KiAddThreadToScbQueue](KiAddThreadToScbQueue_function_002010DC.md) (function, `0x002010DC`)
- `0x00200E92` → [KiFindRescheduleContextEntryForPrcb](../35/KiFindRescheduleContextEntryForPrcb_function_00353060.md) (function, `0x00353060`)
- `0x00200F09` → [KiAdjustRescheduleContextEntryForThreadRemoval](../35/KiAdjustRescheduleContextEntryForThreadRemoval_function_00352340.md) (function, `0x00352340`)
- `0x00200F53` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x00200F79` → [KiInsertDeferredReadyList](KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x00200F86` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x00200FA8` → [KiInsertDeferredReadyList](KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x00200FD7` → [KiFindRescheduleContextEntryForPrcb](../35/KiFindRescheduleContextEntryForPrcb_function_00353060.md) (function, `0x00353060`)
- `0x00201051` → [KiAdjustRescheduleContextEntryForThreadRemoval](../35/KiAdjustRescheduleContextEntryForThreadRemoval_function_00352340.md) (function, `0x00352340`)
- `0x00201099` → [KiDoesThreadDominateRescheduleContextEntry](../25/KiDoesThreadDominateRescheduleContextEntry_function_002581D0.md) (function, `0x002581D0`)
- `0x002010CB` → [EtwTraceReadyQueueInsertion](../22/EtwTraceReadyQueueInsertion_function_00223444.md) (function, `0x00223444`)

### Direct callers
- [sub_0021B9AC](../21/Unknown_function_0021B9AC.md) at `0x0021BA02`

### Static image references
- `0x002008F6` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0020091A` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00200BAE` → RVA `0x00FC6B14` (`ALMOSTRO`; read)
- `0x00200C0E` → RVA `0x00FCD260` (`ALMOSTRO`; read)
- `0x00200D66` → RVA `0x00FC5007` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0020076C  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00200771  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00200776  55                              push rbp
00200777  56                              push rsi
00200778  57                              push rdi
00200779  41 54                           push r12
0020077B  41 55                           push r13
0020077D  41 56                           push r14
0020077F  41 57                           push r15
00200781  48 8B EC                        mov rbp, rsp
00200784  48 83 EC 60                     sub rsp, 0x60
00200788  45 33 E4                        xor r12d, r12d
0020078B  48 8B FA                        mov rdi, rdx
0020078E  48 8B 51 68                     mov rdx, qword ptr [rcx + 0x68]
00200792  4C 8B D1                        mov r10, rcx
00200795  44 89 65 D0                     mov dword ptr [rbp - 0x30], r12d
00200799  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0020079D  48 85 D2                        test rdx, rdx
002007A0  74 0F                           je 0x1402007b1
002007A2  8B 87 D8 00 00 00               mov eax, dword ptr [rdi + 0xd8]
002007A8  48 03 C2                        add rax, rdx
002007AB  0F 85 F5 00 00 00               jne 0x1402008a6
002007B1  45 8A F4                        mov r14b, r12b
002007B4  E9 D1 00 00 00                  jmp 0x14020088a
002007B9  4C 8B 55 40                     mov r10, qword ptr [rbp + 0x40]
002007BD  45 33 E4                        xor r12d, r12d
002007C0  49 8B 4A 68                     mov rcx, qword ptr [r10 + 0x68]
002007C4  4C 8B 6F 10                     mov r13, qword ptr [rdi + 0x10]
002007C8  48 85 C9                        test rcx, rcx
002007CB  74 67                           je 0x140200834
002007CD  8B 87 D8 00 00 00               mov eax, dword ptr [rdi + 0xd8]
002007D3  48 03 C1                        add rax, rcx
002007D6  74 5C                           je 0x140200834
002007D8  4C 3B 6F 18                     cmp r13, qword ptr [rdi + 0x18]
002007DC  74 56                           je 0x140200834
002007DE  49 8B 92 40 02 00 00            mov rdx, qword ptr [r10 + 0x240]
002007E5  0F B6 87 D0 00 00 00            movzx eax, byte ptr [rdi + 0xd0]
002007EC  66 3B 02                        cmp ax, word ptr [rdx]
002007EF  73 43                           jae 0x140200834
002007F1  8A 8F D1 00 00 00               mov cl, byte ptr [rdi + 0xd1]
002007F7  48 8B 54 C2 08                  mov rdx, qword ptr [rdx + rax*8 + 8]
002007FC  48 D3 EA                        shr rdx, cl
002007FF  F6 C2 01                        test dl, 1
00200802  74 30                           je 0x140200834
00200804  49 8B 45 68                     mov rax, qword ptr [r13 + 0x68]
00200808  48 85 C0                        test rax, rax
0020080B  0F 84 3B 03 00 00               je 0x140200b4c
00200811  8B 9F D8 00 00 00               mov ebx, dword ptr [rdi + 0xd8]
00200817  48 03 D8                        add rbx, rax
0020081A  0F 85 24 01 00 00               jne 0x140200944
00200820  41 8A 82 C3 00 00 00            mov al, byte ptr [r10 + 0xc3]
00200827  41 38 85 C3 00 00 00            cmp byte ptr [r13 + 0xc3], al
0020082E  0F 8E 79 01 00 00               jle 0x1402009ad
00200834  45 8A F4                        mov r14b, r12b
00200837  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
0020083B  48 85 C0                        test rax, rax
0020083E  74 4A                           je 0x14020088a
00200840  4C 8B C8                        mov r9, rax
00200843  4D 8B C4                        mov r8, r12
00200846  49 83 E1 FE                     and r9, 0xfffffffffffffffe
0020084A  41 8B D4                        mov edx, r12d
0020084D  4C 89 4D F8                     mov qword ptr [rbp - 8], r9
00200851  83 E0 01                        and eax, 1
00200854  0F 84 DC 00 00 00               je 0x140200936
0020085A  83 F8 01                        cmp eax, 1
0020085D  75 15                           jne 0x140200874
0020085F  49 8B 81 58 8E 00 00            mov rax, qword ptr [r9 + 0x8e58]
00200866  4D 8B 81 58 8E 00 00            mov r8, qword ptr [r9 + 0x8e58]
0020086D  49 83 C0 08                     add r8, 8
00200871  0F B6 10                        movzx edx, byte ptr [rax]
00200874  85 D2                           test edx, edx
00200876  74 12                           je 0x14020088a
00200878  8D 42 FF                        lea eax, [rdx - 1]
0020087B  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
0020087F  8B D0                           mov edx, eax
00200881  F0 4C 21 61 30                  lock and qword ptr [rcx + 0x30], r12
00200886  85 C0                           test eax, eax
00200888  75 EE                           jne 0x140200878
0020088A  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
00200892  41 8A C6                        mov al, r14b
00200895  48 83 C4 60                     add rsp, 0x60
00200899  41 5F                           pop r15
0020089B  41 5E                           pop r14
0020089D  41 5D                           pop r13
0020089F  41 5C                           pop r12
002008A1  5F                              pop rdi
002008A2  5E                              pop rsi
002008A3  5D                              pop rbp
002008A4  C3                              ret
002008A5  CC                              int3
002008A6  E8 65 5A 15 00                  call 0x140356310
002008AB  84 C0                           test al, al
002008AD  0F 84 FE FE FF FF               je 0x1402007b1
002008B3  48 8B C7                        mov rax, rdi
002008B6  48 83 E0 FE                     and rax, 0xfffffffffffffffe
002008BA  48 83 C8 01                     or rax, 1
002008BE  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
002008C2  45 8B F4                        mov r14d, r12d
002008C5  44 88 65 50                     mov byte ptr [rbp + 0x50], r12b
002008C9  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
002008CD  48 8B 87 58 8E 00 00            mov rax, qword ptr [rdi + 0x8e58]
002008D4  0F B6 08                        movzx ecx, byte ptr [rax]
002008D7  4C 8D 78 08                     lea r15, [rax + 8]
002008DB  84 C9                           test cl, cl
002008DD  0F 84 DD FE FF FF               je 0x1402007c0
002008E3  44 8B E1                        mov r12d, ecx
002008E6  49 8B 37                        mov rsi, qword ptr [r15]
002008E9  33 DB                           xor ebx, ebx
002008EB  F0 48 0F BA 6E 30 00            lock bts qword ptr [rsi + 0x30], 0
002008F2  73 17                           jae 0x14020090b
002008F4  FF C3                           inc ebx
002008F6  85 1D B0 49 DC 00               test dword ptr [rip + 0xdc49b0], ebx
002008FC  74 1C                           je 0x14020091a
002008FE  F3 90                           pause
00200900  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
00200904  48 85 C0                        test rax, rax
00200907  74 E2                           je 0x1402008eb
00200909  EB E9                           jmp 0x1402008f4
0020090B  49 83 C7 08                     add r15, 8
0020090F  49 83 EC 01                     sub r12, 1
00200913  75 D1                           jne 0x1402008e6
00200915  E9 9F FE FF FF                  jmp 0x1402007b9
0020091A  8B 05 98 61 DC 00               mov eax, dword ptr [rip + 0xdc6198]
00200920  A8 40                           test al, 0x40
00200922  74 DA                           je 0x1402008fe
00200924  E8 67 EB 10 00                  call 0x14030f490
00200929  84 C0                           test al, al
0020092B  74 D1                           je 0x1402008fe
0020092D  8B CB                           mov ecx, ebx
0020092F  E8 2C EB 10 00                  call 0x14030f460
00200934  EB CA                           jmp 0x140200900
00200936  4C 8D 45 F8                     lea r8, [rbp - 8]
0020093A  BA 01 00 00 00                  mov edx, 1
0020093F  E9 34 FF FF FF                  jmp 0x140200878
00200944  4C 8B 8B 80 00 00 00            mov r9, qword ptr [rbx + 0x80]
0020094B  49 8B CD                        mov rcx, r13
0020094E  48 8B D3                        mov rdx, rbx
00200951  45 8B F4                        mov r14d, r12d
00200954  45 8B C4                        mov r8d, r12d
00200957  E8 A4 A8 10 00                  call 0x14030b200
0020095C  84 C0                           test al, al
0020095E  74 40                           je 0x1402009a0
00200960  E8 AB 59 15 00                  call 0x140356310
00200965  84 C0                           test al, al
00200967  75 37                           jne 0x1402009a0
00200969  48 8B CB                        mov rcx, rbx
0020096C  E8 2F 1E 00 00                  call 0x1402027a0
00200971  84 C0                           test al, al
00200973  0F 85 32 07 00 00               jne 0x1402010ab
00200979  44 03 72 7C                     add r14d, dword ptr [rdx + 0x7c]
0020097D  4D 85 C9                        test r9, r9
00200980  0F 85 CE 01 00 00               jne 0x140200b54
00200986  45 85 F6                        test r14d, r14d
00200989  75 0C                           jne 0x140200997
0020098B  48 8B 92 A0 01 00 00            mov rdx, qword ptr [rdx + 0x1a0]
00200992  48 85 D2                        test rdx, rdx
00200995  75 E2                           jne 0x140200979
00200997  C6 45 50 01                     mov byte ptr [rbp + 0x50], 1
0020099B  45 85 C0                        test r8d, r8d
0020099E  75 04                           jne 0x1402009a4
002009A0  44 88 65 50                     mov byte ptr [rbp + 0x50], r12b
002009A4  45 85 F6                        test r14d, r14d
002009A7  0F 84 73 FE FF FF               je 0x140200820
002009AD  48 8B B7 E8 37 00 00            mov rsi, qword ptr [rdi + 0x37e8]
002009B4  33 D2                           xor edx, edx
002009B6  48 8B CE                        mov rcx, rsi
002009B9  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
002009BD  41 B8 F0 00 00 00               mov r8d, 0xf0
002009C3  E8 78 62 4C 00                  call 0x1406c6c40
002009C8  45 33 C0                        xor r8d, r8d
002009CB  48 8D 55 E0                     lea rdx, [rbp - 0x20]
002009CF  48 8B CE                        mov rcx, rsi
002009D2  E8 D9 BC 10 00                  call 0x14030c6b0
002009D7  4C 8B 7F 08                     mov r15, qword ptr [rdi + 8]
002009DB  4C 89 65 E8                     mov qword ptr [rbp - 0x18], r12
002009DF  4C 89 7D 58                     mov qword ptr [rbp + 0x58], r15
002009E3  45 8B 47 78                     mov r8d, dword ptr [r15 + 0x78]
002009E7  41 0F BA E0 0C                  bt r8d, 0xc
002009EC  0F 82 9A 04 00 00               jb 0x140200e8c
002009F2  4C 3B BF 80 8E 00 00            cmp r15, qword ptr [rdi + 0x8e80]
002009F9  0F 84 8D 04 00 00               je 0x140200e8c
002009FF  48 8B D7                        mov rdx, rdi
00200A02  48 8B CE                        mov rcx, rsi
00200A05  E8 56 26 15 00                  call 0x140353060
00200A0A  41 8B 4D 78                     mov ecx, dword ptr [r13 + 0x78]
00200A0E  41 83 E0 02                     and r8d, 2
00200A12  83 E1 02                        and ecx, 2
00200A15  4C 8B E0                        mov r12, rax
00200A18  44 3A C1                        cmp r8b, cl
00200A1B  0F 87 93 06 00 00               ja 0x1402010b4
00200A21  49 8B 04 24                     mov rax, qword ptr [r12]
00200A25  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00200A29  49 89 4C 24 10                  mov qword ptr [r12 + 0x10], rcx
00200A2E  48 3B 48 18                     cmp rcx, qword ptr [rax + 0x18]
00200A32  41 8A 44 24 20                  mov al, byte ptr [r12 + 0x20]
00200A37  0F 94 C2                        sete dl
00200A3A  24 FE                           and al, 0xfe
00200A3C  0A D0                           or dl, al
00200A3E  41 88 54 24 20                  mov byte ptr [r12 + 0x20], dl
00200A43  80 E2 FD                        and dl, 0xfd
00200A46  8B 41 78                        mov eax, dword ptr [rcx + 0x78]
00200A49  49 83 64 24 18 00               and qword ptr [r12 + 0x18], 0
00200A4F  41 80 64 24 21 FE               and byte ptr [r12 + 0x21], 0xfe
00200A55  41 80 4C 24 22 01               or byte ptr [r12 + 0x22], 1
00200A5B  D1 E8                           shr eax, 1
00200A5D  24 01                           and al, 1
00200A5F  02 C0                           add al, al
00200A61  32 C2                           xor al, dl
00200A63  24 C7                           and al, 0xc7
00200A65  0C 04                           or al, 4
00200A67  41 88 44 24 20                  mov byte ptr [r12 + 0x20], al
00200A6C  41 8B 4F 78                     mov ecx, dword ptr [r15 + 0x78]
00200A70  41 0B 4D 78                     or ecx, dword ptr [r13 + 0x78]
00200A74  F6 C1 02                        test cl, 2
00200A77  0F 84 BE 00 00 00               je 0x140200b3b
00200A7D  33 D2                           xor edx, edx
00200A7F  89 55 58                        mov dword ptr [rbp + 0x58], edx
00200A82  38 16                           cmp byte ptr [rsi], dl
00200A84  0F 86 B1 00 00 00               jbe 0x140200b3b
00200A8A  8B C2                           mov eax, edx
00200A8C  4C 8D 0C 95 02 00 00 00         lea r9, [rdx*4 + 2]
00200A94  4C 03 C8                        add r9, rax
00200A97  4E 8D 0C CE                     lea r9, [rsi + r9*8]
00200A9B  4D 3B E1                        cmp r12, r9
00200A9E  0F 84 87 00 00 00               je 0x140200b2b
00200AA4  41 8B 47 78                     mov eax, dword ptr [r15 + 0x78]
00200AA8  49 8B 49 18                     mov rcx, qword ptr [r9 + 0x18]
00200AAC  48 83 65 E8 00                  and qword ptr [rbp - 0x18], 0
00200AB1  4D 8B 11                        mov r10, qword ptr [r9]
00200AB4  A8 02                           test al, 2
00200AB6  48 8D 41 FF                     lea rax, [rcx - 1]
00200ABA  0F 84 5E 04 00 00               je 0x140200f1e
00200AC0  4D 8B 9A 80 8E 00 00            mov r11, qword ptr [r10 + 0x8e80]
00200AC7  48 83 F8 FC                     cmp rax, -4
00200ACB  0F 86 82 04 00 00               jbe 0x140200f53
00200AD1  41 8A 41 20                     mov al, byte ptr [r9 + 0x20]
00200AD5  24 FE                           and al, 0xfe
00200AD7  4D 89 79 10                     mov qword ptr [r9 + 0x10], r15
00200ADB  41 88 41 20                     mov byte ptr [r9 + 0x20], al
00200ADF  24 FD                           and al, 0xfd
00200AE1  41 8B 4F 78                     mov ecx, dword ptr [r15 + 0x78]
00200AE5  D1 E9                           shr ecx, 1
00200AE7  80 E1 01                        and cl, 1
00200AEA  02 C9                           add cl, cl
00200AEC  32 C8                           xor cl, al
00200AEE  80 E1 E7                        and cl, 0xe7
00200AF1  80 C9 04                        or cl, 4
00200AF4  8A C1                           mov al, cl
00200AF6  80 C9 20                        or cl, 0x20
00200AF9  24 DF                           and al, 0xdf
00200AFB  0F B6 C9                        movzx ecx, cl
00200AFE  4D 3B FB                        cmp r15, r11
00200B01  0F B6 C0                        movzx eax, al
00200B04  0F 44 C8                        cmove ecx, eax
00200B07  41 88 49 20                     mov byte ptr [r9 + 0x20], cl
00200B0B  49 8B CB                        mov rcx, r11
00200B0E  41 80 61 21 FE                  and byte ptr [r9 + 0x21], 0xfe
00200B13  4D 89 59 18                     mov qword ptr [r9 + 0x18], r11
00200B17  E8 14 27 15 00                  call 0x140353230
00200B1C  84 C0                           test al, al
00200B1E  75 0B                           jne 0x140200b2b
00200B20  41 8B 42 24                     mov eax, dword ptr [r10 + 0x24]
00200B24  41 89 83 18 02 00 00            mov dword ptr [r11 + 0x218], eax
00200B2B  0F B6 06                        movzx eax, byte ptr [rsi]
00200B2E  FF C2                           inc edx
00200B30  89 55 58                        mov dword ptr [rbp + 0x58], edx
00200B33  3B D0                           cmp edx, eax
00200B35  0F 82 4F FF FF FF               jb 0x140200a8a
00200B3B  41 8B 47 78                     mov eax, dword ptr [r15 + 0x78]
00200B3F  D1 E8                           shr eax, 1
00200B41  83 E0 01                        and eax, 1
00200B44  89 46 04                        mov dword ptr [rsi + 4], eax
00200B47  45 33 E4                        xor r12d, r12d
00200B4A  EB 1B                           jmp 0x140200b67
00200B4C  49 8B DC                        mov rbx, r12
00200B4F  E9 CC FC FF FF                  jmp 0x140200820
00200B54  48 8B 82 80 00 00 00            mov rax, qword ptr [rdx + 0x80]
00200B5B  44 03 00                        add r8d, dword ptr [rax]
00200B5E  E9 28 FE FF FF                  jmp 0x14020098b
00200B63  44 89 66 04                     mov dword ptr [rsi + 4], r12d
00200B67  41 C6 85 84 01 00 00 01         mov byte ptr [r13 + 0x184], 1
00200B6F  48 85 DB                        test rbx, rbx
00200B72  0F 85 5D 02 00 00               jne 0x140200dd5
00200B78  41 B9 01 00 00 00               mov r9d, 1
00200B7E  48 8B CF                        mov rcx, rdi
00200B81  45 85 F6                        test r14d, r14d
00200B84  0F 85 DC 02 00 00               jne 0x140200e66
00200B8A  45 0F BE 85 C3 00 00 00         movsx r8d, byte ptr [r13 + 0xc3]
00200B92  48 8D 45 D0                     lea rax, [rbp - 0x30]
00200B96  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00200B9B  49 8B D5                        mov rdx, r13
00200B9E  8A 45 50                        mov al, byte ptr [rbp + 0x50]
00200BA1  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00200BA5  E8 56 7F 01 00                  call 0x140218b00
00200BAA  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
00200BAE  F7 05 5C 5F DC 00 00 08 00 00   test dword ptr [rip + 0xdc5f5c], 0x800
00200BB8  0F 85 04 05 00 00               jne 0x1402010c2
00200BBE  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00200BC2  48 8B CE                        mov rcx, rsi
00200BC5  E8 56 7A 05 00                  call 0x140258620
00200BCA  4C 8D 4D D8                     lea r9, [rbp - 0x28]
00200BCE  45 33 C0                        xor r8d, r8d
00200BD1  48 8B D7                        mov rdx, rdi
00200BD4  48 8B CE                        mov rcx, rsi
00200BD7  E8 44 C3 10 00                  call 0x14030cf20
00200BDC  4C 8B 7F 10                     mov r15, qword ptr [rdi + 0x10]
00200BE0  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00200BE4  4D 85 FF                        test r15, r15
00200BE7  4C 89 7D 58                     mov qword ptr [rbp + 0x58], r15
00200BEB  8A D8                           mov bl, al
00200BED  41 0F 94 C6                     sete r14b
00200BF1  44 88 75 50                     mov byte ptr [rbp + 0x50], r14b
00200BF5  E8 56 90 19 00                  call 0x140399c50
00200BFA  84 DB                           test bl, bl
00200BFC  0F 84 B6 00 00 00               je 0x140200cb8
00200C02  45 8B EC                        mov r13d, r12d
00200C05  44 38 26                        cmp byte ptr [rsi], r12b
00200C08  0F 86 9E 00 00 00               jbe 0x140200cac
00200C0E  4C 8D 35 4B C6 DC 00            lea r14, [rip + 0xdcc64b]
00200C15  41 8B C5                        mov eax, r13d
00200C18  4C 8D 24 80                     lea r12, [rax + rax*4]
00200C1C  42 8A 44 E6 33                  mov al, byte ptr [rsi + r12*8 + 0x33]
00200C21  4A 8B 5C E6 10                  mov rbx, qword ptr [rsi + r12*8 + 0x10]
00200C26  A8 10                           test al, 0x10
00200C28  75 0B                           jne 0x140200c35
00200C2A  A8 08                           test al, 8
00200C2C  74 25                           je 0x140200c53
00200C2E  90                              nop
00200C2F  80 7B 07 00                     cmp byte ptr [rbx + 7], 0
00200C33  74 1E                           je 0x140200c53
00200C35  8A 87 D9 35 00 00               mov al, byte ptr [rdi + 0x35d9]
00200C3B  84 C0                           test al, al
00200C3D  0F 85 9C 00 00 00               jne 0x140200cdf
00200C43  C6 87 D9 35 00 00 01            mov byte ptr [rdi + 0x35d9], 1
00200C4A  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
00200C4D  89 87 DC 35 00 00               mov dword ptr [rdi + 0x35dc], eax
00200C53  42 F6 44 E6 33 02               test byte ptr [rsi + r12*8 + 0x33], 2
00200C59  0F 85 61 01 00 00               jne 0x140200dc0
00200C5F  42 F6 44 E6 33 04               test byte ptr [rsi + r12*8 + 0x33], 4
00200C65  74 16                           je 0x140200c7d
00200C67  48 8B 83 B8 8E 00 00            mov rax, qword ptr [rbx + 0x8eb8]
00200C6E  46 0F BE 4C E6 34               movsx r9d, byte ptr [rsi + r12*8 + 0x34]
00200C74  48 85 C0                        test rax, rax
00200C77  0F 85 AF 00 00 00               jne 0x140200d2c
00200C7D  42 F6 44 E6 33 01               test byte ptr [rsi + r12*8 + 0x33], 1
00200C83  74 0D                           je 0x140200c92
00200C85  4A 8B 44 E6 28                  mov rax, qword ptr [rsi + r12*8 + 0x28]
00200C8A  66 F0 FF 88 64 03 00 00         lock dec word ptr [rax + 0x364]
00200C92  0F B6 06                        movzx eax, byte ptr [rsi]
00200C95  41 FF C5                        inc r13d
00200C98  44 3B E8                        cmp r13d, eax
00200C9B  0F 82 74 FF FF FF               jb 0x140200c15
00200CA1  44 8A 75 50                     mov r14b, byte ptr [rbp + 0x50]
00200CA5  45 33 E4                        xor r12d, r12d
00200CA8  4C 8B 7D 58                     mov r15, qword ptr [rbp + 0x58]
00200CAC  48 8D 8F D8 35 00 00            lea rcx, [rdi + 0x35d8]
00200CB3  E8 48 15 05 00                  call 0x140252200
00200CB8  4C 39 65 D8                     cmp qword ptr [rbp - 0x28], r12
00200CBC  0F 85 78 01 00 00               jne 0x140200e3a
00200CC2  4D 85 FF                        test r15, r15
00200CC5  0F 85 6C FB FF FF               jne 0x140200837
00200CCB  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
00200CCF  45 33 C0                        xor r8d, r8d
00200CD2  48 8B CF                        mov rcx, rdi
00200CD5  E8 0E 9C 10 00                  call 0x14030a8e8
00200CDA  E9 58 FB FF FF                  jmp 0x140200837
00200CDF  3C 01                           cmp al, 1
00200CE1  75 40                           jne 0x140200d23
00200CE3  8B 97 DC 35 00 00               mov edx, dword ptr [rdi + 0x35dc]
00200CE9  3B 53 24                        cmp edx, dword ptr [rbx + 0x24]
00200CEC  0F 84 61 FF FF FF               je 0x140200c53
00200CF2  4C 8D BF E0 35 00 00            lea r15, [rdi + 0x35e0]
00200CF9  C6 87 D9 35 00 00 02            mov byte ptr [rdi + 0x35d9], 2
00200D00  49 8B CF                        mov rcx, r15
00200D03  E8 E8 A9 05 00                  call 0x14025b6f0
00200D08  4C 8B 83 C8 00 00 00            mov r8, qword ptr [rbx + 0xc8]
00200D0F  49 8B CF                        mov rcx, r15
00200D12  0F B6 93 D0 00 00 00            movzx edx, byte ptr [rbx + 0xd0]
00200D19  E8 A2 A9 05 00                  call 0x14025b6c0
00200D1E  E9 30 FF FF FF                  jmp 0x140200c53
00200D23  4C 8D BF E0 35 00 00            lea r15, [rdi + 0x35e0]
00200D2A  EB DC                           jmp 0x140200d08
00200D2C  48 8D 8F B8 8E 00 00            lea rcx, [rdi + 0x8eb8]
00200D33  48 83 39 00                     cmp qword ptr [rcx], 0
00200D37  0F 84 40 FF FF FF               je 0x140200c7d
00200D3D  48 3B FB                        cmp rdi, rbx
00200D40  0F 84 37 FF FF FF               je 0x140200c7d
00200D46  8B 00                           mov eax, dword ptr [rax]
00200D48  4C 8B C1                        mov r8, rcx
00200D4B  8B D0                           mov edx, eax
00200D4D  81 E2 00 00 04 00               and edx, 0x40000
00200D53  74 07                           je 0x140200d5c
00200D55  4C 8D 87 B8 8E 00 00            lea r8, [rdi + 0x8eb8]
00200D5C  0F BA E0 14                     bt eax, 0x14
00200D60  0F 83 4F 02 00 00               jae 0x140200fb5
00200D66  80 3D 9A 42 DC 00 00            cmp byte ptr [rip + 0xdc429a], 0
00200D6D  48 8B 11                        mov rdx, qword ptr [rcx]
00200D70  C7 42 0C 02 00 00 00            mov dword ptr [rdx + 0xc], 2
00200D77  44 8B 7B 24                     mov r15d, dword ptr [rbx + 0x24]
00200D7B  75 12                           jne 0x140200d8f
00200D7D  43 0F B6 44 7E 01               movzx eax, byte ptr [r14 + r15*2 + 1]
00200D83  47 0F B6 3C 7E                  movzx r15d, byte ptr [r14 + r15*2]
00200D88  41 C1 E7 06                     shl r15d, 6
00200D8C  44 0B F8                        or r15d, eax
00200D8F  44 89 7A 08                     mov dword ptr [rdx + 8], r15d
00200D93  8B 05 7B 5D DC 00               mov eax, dword ptr [rip + 0xdc5d7b]
00200D99  A8 20                           test al, 0x20
00200D9B  74 0D                           je 0x140200daa
00200D9D  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
00200DA0  BA 02 00 00 00                  mov edx, 2
00200DA5  E8 16 A5 2F 00                  call 0x1404fb2c0
00200DAA  41 8B D7                        mov edx, r15d
00200DAD  B9 C2 00 00 40                  mov ecx, 0x400000c2
00200DB2  48 C1 EA 20                     shr rdx, 0x20
00200DB6  41 8B C7                        mov eax, r15d
00200DB9  0F 30                           wrmsr
00200DBB  E9 BD FE FF FF                  jmp 0x140200c7d
00200DC0  4A 8B 4C E6 28                  mov rcx, qword ptr [rsi + r12*8 + 0x28]
00200DC5  45 33 C0                        xor r8d, r8d
00200DC8  48 8B D3                        mov rdx, rbx
00200DCB  E8 7C A9 10 00                  call 0x14030b74c
00200DD0  E9 8A FE FF FF                  jmp 0x140200c5f
00200DD5  4C 8B 8B 80 00 00 00            mov r9, qword ptr [rbx + 0x80]
00200DDC  49 8B CD                        mov rcx, r13
00200DDF  48 8B D3                        mov rdx, rbx
00200DE2  45 8B F4                        mov r14d, r12d
00200DE5  45 8B C4                        mov r8d, r12d
00200DE8  E8 13 A4 10 00                  call 0x14030b200
00200DED  84 C0                           test al, al
00200DEF  74 40                           je 0x140200e31
00200DF1  E8 1A 55 15 00                  call 0x140356310
00200DF6  84 C0                           test al, al
00200DF8  75 37                           jne 0x140200e31
00200DFA  48 8B CB                        mov rcx, rbx
00200DFD  E8 9E 19 00 00                  call 0x1402027a0
00200E02  84 C0                           test al, al
00200E04  0F 85 AF 02 00 00               jne 0x1402010b9
00200E0A  44 03 72 7C                     add r14d, dword ptr [rdx + 0x7c]
00200E0E  4D 85 C9                        test r9, r9
00200E11  75 6D                           jne 0x140200e80
00200E13  45 85 F6                        test r14d, r14d
00200E16  75 0C                           jne 0x140200e24
00200E18  48 8B 92 A0 01 00 00            mov rdx, qword ptr [rdx + 0x1a0]
00200E1F  48 85 D2                        test rdx, rdx
00200E22  75 E6                           jne 0x140200e0a
00200E24  C6 45 50 01                     mov byte ptr [rbp + 0x50], 1
00200E28  45 85 C0                        test r8d, r8d
00200E2B  0F 85 47 FD FF FF               jne 0x140200b78
00200E31  44 88 65 50                     mov byte ptr [rbp + 0x50], r12b
00200E35  E9 3E FD FF FF                  jmp 0x140200b78
00200E3A  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00200E3E  48 8B CF                        mov rcx, rdi
00200E41  E8 3A CF 10 00                  call 0x14030dd80
00200E46  4D 85 FF                        test r15, r15
00200E49  0F 85 E8 F9 FF FF               jne 0x140200837
00200E4F  4C 39 67 10                     cmp qword ptr [rdi + 0x10], r12
00200E53  0F 84 72 FE FF FF               je 0x140200ccb
00200E59  4C 8B 55 40                     mov r10, qword ptr [rbp + 0x40]
00200E5D  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00200E61  E9 5C FA FF FF                  jmp 0x1402008c2
00200E66  4D 8B C5                        mov r8, r13
00200E69  48 8B D3                        mov rdx, rbx
00200E6C  E8 6B 02 00 00                  call 0x1402010dc
00200E71  41 B8 02 00 00 00               mov r8d, 2
00200E77  44 89 45 D0                     mov dword ptr [rbp - 0x30], r8d
00200E7B  E9 2E FD FF FF                  jmp 0x140200bae
00200E80  48 8B 82 80 00 00 00            mov rax, qword ptr [rdx + 0x80]
00200E87  44 03 00                        add r8d, dword ptr [rax]
00200E8A  EB 8C                           jmp 0x140200e18
00200E8C  48 8B D7                        mov rdx, rdi
00200E8F  48 8B CE                        mov rcx, rsi
00200E92  E8 C9 21 15 00                  call 0x140353060
00200E97  4C 8B D0                        mov r10, rax
00200E9A  0F B6 50 20                     movzx edx, byte ptr [rax + 0x20]
00200E9E  4C 8B 08                        mov r9, qword ptr [rax]
00200EA1  44 8B C2                        mov r8d, edx
00200EA4  41 D1 E8                        shr r8d, 1
00200EA7  41 83 E0 01                     and r8d, 1
00200EAB  F6 C2 20                        test dl, 0x20
00200EAE  75 04                           jne 0x140200eb4
00200EB0  80 48 22 01                     or byte ptr [rax + 0x22], 1
00200EB4  80 60 22 FD                     and byte ptr [rax + 0x22], 0xfd
00200EB8  80 E2 C5                        and dl, 0xc5
00200EBB  49 8B 41 18                     mov rax, qword ptr [r9 + 0x18]
00200EBF  80 CA 05                        or dl, 5
00200EC2  41 88 52 20                     mov byte ptr [r10 + 0x20], dl
00200EC6  49 89 42 10                     mov qword ptr [r10 + 0x10], rax
00200ECA  49 8B 41 18                     mov rax, qword ptr [r9 + 0x18]
00200ECE  41 80 62 21 FE                  and byte ptr [r10 + 0x21], 0xfe
00200ED3  49 89 42 18                     mov qword ptr [r10 + 0x18], rax
00200ED7  45 85 C0                        test r8d, r8d
00200EDA  0F 84 87 FC FF FF               je 0x140200b67
00200EE0  45 8B DC                        mov r11d, r12d
00200EE3  44 38 26                        cmp byte ptr [rsi], r12b
00200EE6  0F 86 77 FC FF FF               jbe 0x140200b63
00200EEC  41 8B C3                        mov eax, r11d
00200EEF  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
00200EF7  48 03 C8                        add rcx, rax
00200EFA  48 8D 0C CE                     lea rcx, [rsi + rcx*8]
00200EFE  49 3B CA                        cmp rcx, r10
00200F01  74 0B                           je 0x140200f0e
00200F03  45 33 C9                        xor r9d, r9d
00200F06  41 B0 01                        mov r8b, 1
00200F09  E8 32 14 15 00                  call 0x140352340
00200F0E  0F B6 06                        movzx eax, byte ptr [rsi]
00200F11  41 FF C3                        inc r11d
00200F14  44 3B D8                        cmp r11d, eax
00200F17  72 D3                           jb 0x140200eec
00200F19  E9 45 FC FF FF                  jmp 0x140200b63
00200F1E  4D 8B 5A 18                     mov r11, qword ptr [r10 + 0x18]
00200F22  48 83 F8 FC                     cmp rax, -4
00200F26  76 5E                           jbe 0x140200f86
00200F28  41 8A 41 20                     mov al, byte ptr [r9 + 0x20]
00200F2C  0C 01                           or al, 1
00200F2E  4D 89 59 10                     mov qword ptr [r9 + 0x10], r11
00200F32  41 88 41 20                     mov byte ptr [r9 + 0x20], al
00200F36  24 FD                           and al, 0xfd
00200F38  41 8B 4B 78                     mov ecx, dword ptr [r11 + 0x78]
00200F3C  D1 E9                           shr ecx, 1
00200F3E  80 E1 01                        and cl, 1
00200F41  02 C9                           add cl, cl
00200F43  32 C8                           xor cl, al
00200F45  80 E1 E7                        and cl, 0xe7
00200F48  80 C9 04                        or cl, 4
00200F4B  80 E1 DF                        and cl, 0xdf
00200F4E  E9 B4 FB FF FF                  jmp 0x140200b07
00200F53  E8 D8 22 15 00                  call 0x140353230
00200F58  84 C0                           test al, al
00200F5A  0F 85 71 FB FF FF               jne 0x140200ad1
00200F60  41 F6 41 21 01                  test byte ptr [r9 + 0x21], 1
00200F65  74 04                           je 0x140200f6b
00200F67  83 49 74 02                     or dword ptr [rcx + 0x74], 2
00200F6B  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
00200F72  48 8B D1                        mov rdx, rcx
00200F75  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00200F79  E8 92 03 00 00                  call 0x140201310
00200F7E  8B 55 58                        mov edx, dword ptr [rbp + 0x58]
00200F81  E9 4B FB FF FF                  jmp 0x140200ad1
00200F86  E8 A5 22 15 00                  call 0x140353230
00200F8B  84 C0                           test al, al
00200F8D  75 99                           jne 0x140200f28
00200F8F  41 F6 41 21 01                  test byte ptr [r9 + 0x21], 1
00200F94  74 04                           je 0x140200f9a
00200F96  83 49 74 02                     or dword ptr [rcx + 0x74], 2
00200F9A  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
00200FA1  48 8B D1                        mov rdx, rcx
00200FA4  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00200FA8  E8 63 03 00 00                  call 0x140201310
00200FAD  8B 55 58                        mov edx, dword ptr [rbp + 0x58]
00200FB0  E9 73 FF FF FF                  jmp 0x140200f28
00200FB5  85 D2                           test edx, edx
00200FB7  0F 84 C0 FC FF FF               je 0x140200c7d
00200FBD  0F B6 C0                        movzx eax, al
00200FC0  49 8B C8                        mov rcx, r8
00200FC3  41 3B C1                        cmp eax, r9d
00200FC6  0F 8D B1 FC FF FF               jge 0x140200c7d
00200FCC  E9 95 FD FF FF                  jmp 0x140200d66
00200FD1  48 8B D7                        mov rdx, rdi
00200FD4  48 8B CE                        mov rcx, rsi
00200FD7  E8 84 20 15 00                  call 0x140353060
00200FDC  4C 8B D0                        mov r10, rax
00200FDF  0F B6 50 20                     movzx edx, byte ptr [rax + 0x20]
00200FE3  4C 8B 08                        mov r9, qword ptr [rax]
00200FE6  44 8B C2                        mov r8d, edx
00200FE9  41 D1 E8                        shr r8d, 1
00200FEC  41 83 E0 01                     and r8d, 1
00200FF0  F6 C2 20                        test dl, 0x20
00200FF3  75 04                           jne 0x140200ff9
00200FF5  80 48 22 01                     or byte ptr [rax + 0x22], 1
00200FF9  80 60 22 FD                     and byte ptr [rax + 0x22], 0xfd
00200FFD  80 E2 C5                        and dl, 0xc5
00201000  49 8B 41 18                     mov rax, qword ptr [r9 + 0x18]
00201004  80 CA 05                        or dl, 5
00201007  41 88 52 20                     mov byte ptr [r10 + 0x20], dl
0020100B  45 33 E4                        xor r12d, r12d
0020100E  49 89 42 10                     mov qword ptr [r10 + 0x10], rax
00201012  49 8B 41 18                     mov rax, qword ptr [r9 + 0x18]
00201016  41 80 62 21 FE                  and byte ptr [r10 + 0x21], 0xfe
0020101B  49 89 42 18                     mov qword ptr [r10 + 0x18], rax
0020101F  45 85 C0                        test r8d, r8d
00201022  0F 84 3F FB FF FF               je 0x140200b67
00201028  45 8B DC                        mov r11d, r12d
0020102B  44 38 26                        cmp byte ptr [rsi], r12b
0020102E  0F 86 2F FB FF FF               jbe 0x140200b63
00201034  41 8B C3                        mov eax, r11d
00201037  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
0020103F  48 03 C8                        add rcx, rax
00201042  48 8D 0C CE                     lea rcx, [rsi + rcx*8]
00201046  49 3B CA                        cmp rcx, r10
00201049  74 0B                           je 0x140201056
0020104B  45 33 C9                        xor r9d, r9d
0020104E  41 B0 01                        mov r8b, 1
00201051  E8 EA 12 15 00                  call 0x140352340
00201056  0F B6 06                        movzx eax, byte ptr [rsi]
00201059  41 FF C3                        inc r11d
0020105C  44 3B D8                        cmp r11d, eax
0020105F  72 D3                           jb 0x140201034
00201061  E9 FD FA FF FF                  jmp 0x140200b63
00201066  0F B6 0E                        movzx ecx, byte ptr [rsi]
00201069  44 3B F9                        cmp r15d, ecx
0020106C  72 09                           jb 0x140201077
0020106E  4C 8B 7D 58                     mov r15, qword ptr [rbp + 0x58]
00201072  E9 AA F9 FF FF                  jmp 0x140200a21
00201077  41 8B C7                        mov eax, r15d
0020107A  4A 8D 0C BD 02 00 00 00         lea rcx, [r15*4 + 2]
00201082  48 03 C8                        add rcx, rax
00201085  48 8D 0C CE                     lea rcx, [rsi + rcx*8]
00201089  4C 3B E1                        cmp r12, rcx
0020108C  74 18                           je 0x1402010a6
0020108E  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
00201092  45 33 C9                        xor r9d, r9d
00201095  45 8D 41 02                     lea r8d, [r9 + 2]
00201099  E8 32 71 05 00                  call 0x1402581d0
0020109E  84 C0                           test al, al
002010A0  0F 84 2B FF FF FF               je 0x140200fd1
002010A6  41 FF C7                        inc r15d
002010A9  EB BB                           jmp 0x140201066
002010AB  41 83 CE FF                     or r14d, 0xffffffff
002010AF  E9 EC F8 FF FF                  jmp 0x1402009a0
002010B4  45 33 FF                        xor r15d, r15d
002010B7  EB AD                           jmp 0x140201066
002010B9  41 83 CE FF                     or r14d, 0xffffffff
002010BD  E9 6F FD FF FF                  jmp 0x140200e31
002010C2  8B 57 24                        mov edx, dword ptr [rdi + 0x24]
002010C5  45 33 C9                        xor r9d, r9d
002010C8  49 8B CD                        mov rcx, r13
002010CB  E8 74 23 02 00                  call 0x140223444
002010D0  E9 E9 FA FF FF                  jmp 0x140200bbe
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiDeferGroupSchedulingPreemption(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (96);
    v_r12 = 0;
    v_stack_m68 = 0;
    v_stack_m58 = 0;
    if (*(unsigned __int64 *)(a1 + 104) == 0) goto loc_002007B1;
    result = ((unsigned int)(*(unsigned int *)(a2 + 216))) + (*(unsigned __int64 *)(a1 + 104));
    if (condition_is_not_equal) goto loc_002008A6;
loc_002007B1:
    goto loc_0020088A;
loc_002007B9:
    v_r12 = 0;
loc_002007C0:
    if (*(unsigned __int64 *)(v_stack_p8 + 104) == 0) goto loc_00200834;
    result = ((unsigned int)(*(unsigned int *)(a2 + 216))) + (*(unsigned __int64 *)(v_stack_p8 + 104));
    if (condition_is_equal) goto loc_00200834;
    if ((*(unsigned __int64 *)(a2 + 16)) == (*(unsigned __int64 *)(a2 + 24))) goto loc_00200834;
    if (((unsigned __int16)(*(unsigned __int8 *)(a2 + 208))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 576)))) goto loc_00200834;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 576) + *(unsigned __int8 *)(a2 + 208) * 8 + 8)) >> ((unsigned __int8)(*(unsigned __int8 *)(a2 + 209)));
    if ((((unsigned __int8)(a2)) & (1)) == 0) goto loc_00200834;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 104) == 0) goto loc_00200B4C;
    v_rbx = ((unsigned int)(*(unsigned int *)(a2 + 216))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 16) + 104));
    if (condition_is_not_equal) goto loc_00200944;
loc_00200820:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 16) + 195)) <= ((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 195)))) goto loc_002009AD;
loc_00200834:
loc_00200837:
    if (v_stack_m58 == 0) goto loc_0020088A;
    a4 = (v_stack_m58) & (-2);
    v_stack_m40 = a4;
    result = (unsigned int)((v_stack_m58) & (1));
    if (condition_is_equal) goto loc_00200936;
    if (((unsigned int)(result)) == 1) {
        result = *(unsigned __int64 *)(a4 + 36440);
        a3 = *(unsigned __int64 *)(a4 + 36440);
        a3 = (a3) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_0020088A;
loc_00200878:
    if ((unsigned int)(a2 - 1) != 0) goto loc_00200878;
loc_0020088A:
    v_rsp = (v_rsp) + (96);
    return 0;
loc_002008A6:
    result = KiShouldPreemptionBeDeferred(*(unsigned __int64 *)(a3 + a2 - 1 * 8), (unsigned int)((unsigned int)(a2 - 1)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002007B1;
    result = (a2) & (-2);
    result = (result) | (1);
    v_stack_m48 = result;
loc_002008C2:
    v_stack_p18 = 0;
    v_stack_m58 = result;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36440))) == 0) goto loc_002007C0;
loc_002008E6:
    v_rbx = 0;
loc_002008EB:
    if (condition_is_above_or_equal) goto loc_0020090B;
loc_002008F4:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 14436784)) & ((unsigned int)(v_rbx))) == 0) goto loc_0020091A;
loc_002008FE:
loc_00200900:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 36440) + 8) + 48) == 0) goto loc_002008EB;
    goto loc_002008F4;
loc_0020090B:
    v_r15 = (*(unsigned __int64 *)(a2 + 36440) + 8) + (8);
    v_r12 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36440))))) - (1);
    if (condition_is_not_equal) goto loc_002008E6;
    goto loc_002007B9;
loc_0020091A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14442904)))) & (64)) == 0) goto loc_002008FE;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 36440)), (unsigned int)((unsigned int)(a2 - 1)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002008FE;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(a2 - 1)), a3, a4);
    goto loc_00200900;
loc_00200936:
    goto loc_00200878;
loc_00200944:
    result = KiIsThreadConstrainedBySchedulingGroup(*(unsigned __int64 *)(a2 + 16), v_rbx, (unsigned int)((unsigned int)(v_r12)), *(unsigned __int64 *)(v_rbx + 128));
    if ((unsigned __int8)(result) == 0) goto loc_002009A0;
    result = KiShouldPreemptionBeDeferred(*(unsigned __int64 *)(a2 + 16), v_rbx, (unsigned int)((unsigned int)(v_r12)), *(unsigned __int64 *)(v_rbx + 128));
    if ((unsigned __int8)(result) != 0) goto loc_002009A0;
    result = KiCheckForMaxOverQuotaScb(v_rbx, v_rbx, (unsigned int)((unsigned int)(v_r12)), *(unsigned __int64 *)(v_rbx + 128));
    if ((unsigned __int8)(result) != 0) goto loc_002010AB;
loc_00200979:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) + (*(unsigned int *)(v_rbx + 124)));
    if (*(unsigned __int64 *)(v_rbx + 128) != 0) goto loc_00200B54;
    if ((unsigned int)(v_r14) != 0) goto loc_00200997;
loc_0020098B:
    if (*(unsigned __int64 *)(v_rbx + 416) != 0) goto loc_00200979;
loc_00200997:
    v_stack_p18 = 1;
    if ((unsigned int)((unsigned int)((unsigned int)(v_r12))) == 0) {
        v_stack_p18 = (unsigned __int8)(v_r12);
    }
    if ((unsigned int)(v_r14) == 0) goto loc_00200820;
loc_002009AD:
    a2 = 0;
    v_stack_m60 = v_r12;
    result = memset(*(unsigned __int64 *)(a2 + 14312), a2, 240, *(unsigned __int64 *)(v_rbx + 128));
    a3 = 0;
    result = KiStartRescheduleContext(*(unsigned __int64 *)(a2 + 14312), v_stack_m58, a3, *(unsigned __int64 *)(v_rbx + 128));
    v_stack_m50 = v_r12;
    v_stack_p20 = *(unsigned __int64 *)(a2 + 8);
    if (condition_is_below) goto loc_00200E8C;
    if ((*(unsigned __int64 *)(a2 + 8)) == (*(unsigned __int64 *)(a2 + 36480))) goto loc_00200E8C;
    result = KiFindRescheduleContextEntryForPrcb(*(unsigned __int64 *)(a2 + 14312), 0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 120)), *(unsigned __int64 *)(v_rbx + 128));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 120))) & (2));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 16) + 120))) & (2));
    if (((unsigned __int8)(a3)) > ((unsigned __int8)(a1))) goto loc_002010B4;
loc_00200A21:
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8);
    a2 = ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24))) ? 1 : 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(result + 32)) & (254));
    a2 = (unsigned __int8)((a2) | ((unsigned __int8)(result)));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(a2);
    a2 = (unsigned __int8)((a2) & (253));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) + 120))) >> (1));
    result = (unsigned __int8)((result) & (1));
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a2)));
    result = (unsigned __int8)((result) & (199));
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(result);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 120))) | (*(unsigned int *)(*(unsigned __int64 *)(a2 + 16) + 120)));
    if ((((unsigned __int8)(a1)) & (2)) == 0) goto loc_00200B3B;
    a2 = 0;
    v_stack_p20 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312))) <= 0) goto loc_00200B3B;
loc_00200A8A:
    a4 = (a2 * 4 + 2) + (0);
    if (result == (*(unsigned __int64 *)(a2 + 14312) + a4 * 8)) goto loc_00200B2B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 120)))) & (2)) == 0) goto loc_00200F1E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + a4 * 8 + 24) - 1) <= -4) goto loc_00200F53;
loc_00200AD1:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312) + a4 * 8 + 32)) & (254));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + a4 * 8 + 16) = *(unsigned __int64 *)(a2 + 8);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312) + a4 * 8 + 32) = (unsigned __int8)(result);
    result = (unsigned __int8)((result) & (253));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 120))) >> (1));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a1)));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) & (231));
    a1 = (unsigned __int8)((a1) | (4));
    a1 = (unsigned __int8)((a1) | (32));
    result = (unsigned __int8)(((unsigned __int8)(a1)) & (223));
    a1 = (unsigned __int8)(a1);
    if ((*(unsigned __int64 *)(a2 + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + a4 * 8) + 36480))) { a1 = (unsigned int)((unsigned __int8)(result)); }
loc_00200B07:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312) + a4 * 8 + 32) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + a4 * 8 + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + a4 * 8) + 36480);
    result = KiIsPrcbThread(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + a4 * 8) + 36480), a2, a3, *(unsigned __int64 *)(a2 + 14312) + a4 * 8);
    if ((unsigned __int8)(result) == 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + a4 * 8) + 36);
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + a4 * 8) + 36480) + 536) = (unsigned int)(result);
    }
    a2 = (unsigned int)((a2) + 1);
    v_stack_p20 = (unsigned int)(a2);
    if (((unsigned int)(a2)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312))))) goto loc_00200A8A;
loc_00200B3B:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 120))) >> (1));
    result = (unsigned int)((result) & (1));
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 14312) + 4) = (unsigned int)(result);
    v_r12 = 0;
    goto loc_00200B67;
loc_00200B4C:
    goto loc_00200820;
loc_00200B54:
    a3 = (unsigned int)((a3) + (*(unsigned int *)(*(unsigned __int64 *)(a2 + 128))));
    goto loc_0020098B;
loc_00200B63:
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 14312) + 4) = 0;
loc_00200B67:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 16) + 388) = 1;
    if (0 != 0) goto loc_00200DD5;
loc_00200B78:
    if ((unsigned int)(v_r14) != 0) goto loc_00200E66;
    v_stack_p28 = v_stack_m68;
    v_stack_p20 = (unsigned __int8)(v_stack_p18);
    result = KiAddThreadToPrcbQueue(a2, *(unsigned __int64 *)(a2 + 16), (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 16) + 195)), 1);
loc_00200BAE:
    if (((*(unsigned int *)(v_rip + 14442332)) & (0x800ULL)) != 0) goto loc_002010C2;
loc_00200BBE:
    result = KiSearchForNewThreadsForRescheduleContext(*(unsigned __int64 *)(a2 + 14312), v_stack_m60, (unsigned int)(v_stack_m68), 1);
    a3 = 0;
    result = KiCommitRescheduleContext(*(unsigned __int64 *)(a2 + 14312), a2, a3, v_stack_m60);
    v_stack_p20 = *(unsigned __int64 *)(a2 + 16);
    v_r14 = (*(unsigned __int64 *)(a2 + 16) == 0) ? 1 : 0;
    v_stack_p18 = (unsigned __int8)(v_r14);
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_m58, a2, a3, v_stack_m60);
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_00200CB8;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312))) <= 0) goto loc_00200CAC;
loc_00200C15:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 51))) & (16)) != 0) goto loc_00200C35;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 51))) & (8)) == 0) goto loc_00200C53;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 7)) == 0) goto loc_00200C53;
loc_00200C35:
    if ((unsigned __int8)(*(unsigned __int8 *)(a2 + 13785)) != 0) goto loc_00200CDF;
    *(unsigned __int8 *)(a2 + 13785) = 1;
    *(unsigned int *)(a2 + 13788) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 36)));
loc_00200C53:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 51)) & (2)) != 0) goto loc_00200DC0;
loc_00200C5F:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 51)) & (4)) == 0) goto loc_00200C7D;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 36536) != 0) goto loc_00200D2C;
loc_00200C7D:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 36536);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 51)) & (1)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 40);
    }
    v_r13 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r13)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312))))) goto loc_00200C15;
    v_r12 = 0;
loc_00200CAC:
    result = KiFlushSoftwareInterruptBatch(a2 + 13784, a2, a3, (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 52)));
loc_00200CB8:
    if (v_stack_m60 != 0) goto loc_00200E3A;
    if (v_stack_p20 != 0) goto loc_00200837;
loc_00200CCB:
    a3 = 0;
    result = KiInsertDeferredPreemptionApc(a2, v_stack_p8, a3, (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 52)));
    goto loc_00200837;
loc_00200CDF:
    if (((unsigned __int8)(result)) != 1) goto loc_00200D23;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 13788)))) == (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 36))) goto loc_00200C53;
    *(unsigned __int8 *)(a2 + 13785) = 2;
    result = KeAddProcessorAffinityEx(a2 + 13792, (unsigned int)(*(unsigned int *)(a2 + 13788)), a3, (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 52)));
loc_00200D08:
    result = KeAddGroupAffinityEx(a2 + 13792, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 208), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 200), (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 52)));
    goto loc_00200C53;
loc_00200D23:
    goto loc_00200D08;
loc_00200D2C:
    if ((*(unsigned __int64 *)(a2 + 36536)) == 0) goto loc_00200C7D;
    if (a2 == (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16))) goto loc_00200C7D;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result))))) & (0x40000ULL));
    if (!(condition_is_equal)) {
        a3 = a2 + 36536;
    }
    if (condition_is_above_or_equal) goto loc_00200FB5;
loc_00200D66:
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 36536) + 12) = 2;
    result = (unsigned int)(*(unsigned int *)(result));
    v_r15 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 36));
    if ((*(unsigned __int8 *)(v_rip + 14434970)) == 0) {
        result = *(unsigned __int8 *)(v_stack_p18 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 36)) * 2 + 1);
        v_r15 = *(unsigned __int8 *)(v_stack_p18 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 36)) * 2);
        v_r15 = (unsigned int)((v_r15) << (6));
        v_r15 = (unsigned int)((v_r15) | ((unsigned int)(result)));
    }
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 36536) + 8) = (unsigned int)(v_r15);
    result = (unsigned int)(*(unsigned int *)(v_rip + 14441851));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14441851)))) & (32)) != 0) {
        a1 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 36);
        a2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(a1, a2, a3, (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 52)));
    }
    a2 = ((unsigned int)((unsigned int)(v_r15))) >> (32);
    goto loc_00200C7D;
loc_00200DC0:
    a3 = 0;
    result = EtwTraceScheduleThread(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + v_r12 * 8 + 40), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16), a3, (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 52)));
    goto loc_00200C5F;
loc_00200DD5:
    result = KiIsThreadConstrainedBySchedulingGroup(v_r13, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16), 0, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 128));
    if ((unsigned __int8)(result) == 0) goto loc_00200E31;
    result = KiShouldPreemptionBeDeferred(v_r13, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16), 0, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 128));
    if ((unsigned __int8)(result) != 0) goto loc_00200E31;
    result = KiCheckForMaxOverQuotaScb(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16), 0, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 128));
    if ((unsigned __int8)(result) != 0) goto loc_002010B9;
loc_00200E0A:
    v_r14 = (unsigned int)((0) + (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 124)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 128) != 0) goto loc_00200E80;
    if ((unsigned int)(v_r14) != 0) goto loc_00200E24;
loc_00200E18:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 416) != 0) goto loc_00200E0A;
loc_00200E24:
    v_stack_p18 = 1;
    if (0 != 0) goto loc_00200B78;
loc_00200E31:
    v_stack_p18 = 0;
    goto loc_00200B78;
loc_00200E3A:
    result = KiReadyDeferredReadyList(a2, v_stack_m60, 0, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 128));
    if (v_r15 != 0) goto loc_00200837;
    if ((*(unsigned __int64 *)(a2 + 16)) == 0) goto loc_00200CCB;
    goto loc_002008C2;
loc_00200E66:
    result = KiAddThreadToScbQueue(a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16), v_r13, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 128));
    v_stack_m68 = 2;
    goto loc_00200BAE;
loc_00200E80:
    a3 = (unsigned int)((2) + (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 128))));
    goto loc_00200E18;
loc_00200E8C:
    result = KiFindRescheduleContextEntryForPrcb(*(unsigned __int64 *)(a2 + 14312), a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 14312) + 0 + 0 * 4 * 8 + 16) + 128));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(result + 32)))) >> (1));
    a3 = (unsigned int)((a3) & (1));
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (32)) == 0) {
    }
    a2 = (unsigned __int8)((*(unsigned __int8 *)(result + 32)) & (197));
    a2 = (unsigned __int8)((a2) | (5));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(a2);
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    if ((unsigned int)(a3) == 0) goto loc_00200B67;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312))) <= 0) goto loc_00200B63;
loc_00200EEC:
    a1 = (0 * 4 + 2) + (0);
    result = 0;
    if ((*(unsigned __int64 *)(a2 + 14312) + a1 * 8) != result) {
        a4 = 0;
        a3 = 1;
        result = KiAdjustRescheduleContextEntryForThreadRemoval(*(unsigned __int64 *)(a2 + 14312) + a1 * 8, a2, a3, a4);
    }
    v_r11 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r11)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312))))) goto loc_00200EEC;
    goto loc_00200B63;
loc_00200F1E:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312))) <= -4) goto loc_00200F86;
loc_00200F28:
    result = (unsigned __int8)((*(unsigned __int8 *)(a4 + 32)) | (1));
    *(unsigned __int64 *)(a4 + 16) = *(unsigned __int64 *)(result + 24);
    *(unsigned __int8 *)(a4 + 32) = (unsigned __int8)(result);
    result = (unsigned __int8)((result) & (253));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 120))) >> (1));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a1)));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) & (231));
    a1 = (unsigned __int8)((a1) | (4));
    a1 = (unsigned __int8)((a1) & (223));
    goto loc_00200B07;
loc_00200F53:
    result = KiIsPrcbThread(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00200AD1;
    if (((*(unsigned __int8 *)(a4 + 33)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(a1 + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_m50, a1, a3, a4);
    goto loc_00200AD1;
loc_00200F86:
    result = KiIsPrcbThread(v_stack_m50, (unsigned int)(v_stack_p20), a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00200F28;
    if (((*(unsigned __int8 *)(a4 + 33)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(v_stack_m50 + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_m50, v_stack_m50, a3, a4);
    goto loc_00200F28;
loc_00200FB5:
    if ((unsigned int)((unsigned int)(v_stack_p20)) == 0) goto loc_00200C7D;
    if (((unsigned int)((unsigned __int8)(result))) >= 0) goto loc_00200C7D;
    goto loc_00200D66;
loc_00200FD1:
    result = KiFindRescheduleContextEntryForPrcb(*(unsigned __int64 *)(a2 + 14312), a2, a3, a4);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(result + 32)))) >> (1));
    a3 = (unsigned int)((a3) & (1));
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (32)) == 0) {
    }
    a2 = (unsigned __int8)((*(unsigned __int8 *)(result + 32)) & (197));
    a2 = (unsigned __int8)((a2) | (5));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(a2);
    v_r12 = 0;
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    if ((unsigned int)(a3) == 0) goto loc_00200B67;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312))) <= 0) goto loc_00200B63;
loc_00201034:
    a1 = (0 * 4 + 2) + (0);
    result = 0;
    if ((*(unsigned __int64 *)(a2 + 14312) + a1 * 8) != result) {
        a4 = 0;
        a3 = 1;
        result = KiAdjustRescheduleContextEntryForThreadRemoval(*(unsigned __int64 *)(a2 + 14312) + a1 * 8, a2, a3, a4);
    }
    v_r11 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r11)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312))))) goto loc_00201034;
    goto loc_00200B63;
loc_00201066:
    if (((unsigned int)(v_r15)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 14312))))) goto loc_00201077;
    goto loc_00200A21;
loc_00201077:
    a1 = (v_stack_p20 * 4 + 2) + ((unsigned int)((unsigned int)(v_stack_p20)));
    if (0 == (*(unsigned __int64 *)(a2 + 14312) + a1 * 8)) goto loc_002010A6;
    a4 = 0;
    result = KiDoesThreadDominateRescheduleContextEntry(*(unsigned __int64 *)(a2 + 14312) + a1 * 8, v_stack_p20, a4 + 2, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00200FD1;
loc_002010A6:
    v_r15 = (unsigned int)((v_stack_p20) + 1);
    goto loc_00201066;
loc_002010AB:
    v_r14 = (unsigned int)((v_r14) | (0xFFFFFFFFULL));
    goto loc_002009A0;
loc_002010B4:
    v_r15 = 0;
    goto loc_00201066;
loc_002010B9:
    v_r14 = (unsigned int)((v_r14) | (0xFFFFFFFFULL));
    goto loc_00200E31;
loc_002010C2:
    a4 = 0;
    result = EtwTraceReadyQueueInsertion(v_r13, (unsigned int)(*(unsigned int *)(a2 + 36)), a4 + 2, a4);
    goto loc_00200BBE;
}
```

## 5. (Beta) C Style

```c
int64_t KiDeferGroupSchedulingPreemption(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (96);
    local_r12 = 0;
    v_stack_m68 = 0;
    v_stack_m58 = 0;
    if (*(uint64_t *)(arg1 + 0x68) == 0) goto loc_002007B1;
    result = ((uint32_t)(*(uint32_t *)(arg2 + 0xD8))) + (*(uint64_t *)(arg1 + 0x68));
    if (condition_is_not_equal) goto loc_002008A6;
loc_002007B1:
    goto loc_0020088A;
loc_002007B9:
    local_r12 = 0;
loc_002007C0:
    if (*(uint64_t *)(v_stack_p8 + 0x68) == 0) goto loc_00200834;
    result = ((uint32_t)(*(uint32_t *)(arg2 + 0xD8))) + (*(uint64_t *)(v_stack_p8 + 0x68));
    if (condition_is_equal) goto loc_00200834;
    if ((*(uint64_t *)(arg2 + 0x10)) == (*(uint64_t *)(arg2 + 0x18))) goto loc_00200834;
    if (((uint16_t)(*(uint8_t *)(arg2 + 0xD0))) >= (*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x240)))) goto loc_00200834;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x240) + *(uint8_t *)(arg2 + 0xD0) * 8 + 0x8)) >> ((uint8_t)(*(uint8_t *)(arg2 + 0xD1)));
    if ((((uint8_t)(Arg2)) & (1)) == 0) goto loc_00200834;
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x68) == 0) goto loc_00200B4C;
    local_rbx = ((uint32_t)(*(uint32_t *)(arg2 + 0xD8))) + (*(uint64_t *)(*(uint64_t *)(arg2 + 0x10) + 0x68));
    if (condition_is_not_equal) goto loc_00200944;
loc_00200820:
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x10) + 0xC3)) <= ((uint8_t)(*(uint8_t *)(v_stack_p8 + 0xC3)))) goto loc_002009AD;
loc_00200834:
loc_00200837:
    if (v_stack_m58 == 0) goto loc_0020088A;
    a4 = (v_stack_m58) & (-2);
    v_stack_m40 = a4;
    result = (uint32_t)((v_stack_m58) & (1));
    if (condition_is_equal) goto loc_00200936;
    if (((uint32_t)(result)) == 1) {
        result = *(uint64_t *)(a4 + 0x8E58);
        a3 = *(uint64_t *)(a4 + 0x8E58);
        a3 = (a3) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0020088A;
loc_00200878:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_00200878;
loc_0020088A:
    local_rsp = (local_rsp) + (96);
    return 0;
loc_002008A6:
    result = KiShouldPreemptionBeDeferred(*(uint64_t *)(a3 + arg2 - 0x1 * 8), (uint32_t)((uint32_t)(Arg2 - 1)), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_002007B1;
    result = (Arg2) & (-2);
    result = (result) | (1);
    v_stack_m48 = result;
loc_002008C2:
    v_stack_p18 = 0;
    v_stack_m58 = result;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E58))) == 0) goto loc_002007C0;
loc_002008E6:
    local_rbx = 0;
loc_002008EB:
    if (condition_is_above_or_equal) goto loc_0020090B;
loc_002008F4:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xDC49B0)) & ((uint32_t)(local_rbx))) == 0) goto loc_0020091A;
loc_002008FE:
loc_00200900:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8E58) + 0x8) + 0x30) == 0) goto loc_002008EB;
    goto loc_002008F4;
loc_0020090B:
    local_r15 = (*(uint64_t *)(arg2 + 0x8E58) + 8) + (8);
    local_r12 = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E58))))) - (1);
    if (condition_is_not_equal) goto loc_002008E6;
    goto loc_002007B9;
loc_0020091A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDC6198)))) & (64)) == 0) goto loc_002008FE;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8E58)), (uint32_t)((uint32_t)(Arg2 - 1)), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_002008FE;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(Arg2 - 1)), a3, a4);
    goto loc_00200900;
loc_00200936:
    goto loc_00200878;
loc_00200944:
    result = KiIsThreadConstrainedBySchedulingGroup(*(uint64_t *)(arg2 + 0x10), local_rbx, (uint32_t)((uint32_t)(local_r12)), *(uint64_t *)(local_rbx + 0x80));
    if ((uint8_t)(result) == 0) goto loc_002009A0;
    result = KiShouldPreemptionBeDeferred(*(uint64_t *)(arg2 + 0x10), local_rbx, (uint32_t)((uint32_t)(local_r12)), *(uint64_t *)(local_rbx + 0x80));
    if ((uint8_t)(result) != 0) goto loc_002009A0;
    result = KiCheckForMaxOverQuotaScb(local_rbx, local_rbx, (uint32_t)((uint32_t)(local_r12)), *(uint64_t *)(local_rbx + 0x80));
    if ((uint8_t)(result) != 0) goto loc_002010AB;
loc_00200979:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) + (*(uint32_t *)(local_rbx + 0x7C)));
    if (*(uint64_t *)(local_rbx + 0x80) != 0) goto loc_00200B54;
    if ((uint32_t)(local_r14) != 0) goto loc_00200997;
loc_0020098B:
    if (*(uint64_t *)(local_rbx + 0x1A0) != 0) goto loc_00200979;
loc_00200997:
    v_stack_p18 = 1;
    if ((uint32_t)((uint32_t)((uint32_t)(local_r12))) == 0) {
        v_stack_p18 = (uint8_t)(local_r12);
    }
    if ((uint32_t)(local_r14) == 0) goto loc_00200820;
loc_002009AD:
    Arg2 = 0;
    v_stack_m60 = local_r12;
    result = memset(*(uint64_t *)(arg2 + 0x37E8), Arg2, 240, *(uint64_t *)(local_rbx + 0x80));
    a3 = 0;
    result = KiStartRescheduleContext(*(uint64_t *)(arg2 + 0x37E8), v_stack_m58, a3, *(uint64_t *)(local_rbx + 0x80));
    v_stack_m50 = local_r12;
    v_stack_p20 = *(uint64_t *)(arg2 + 0x8);
    if (condition_is_below) goto loc_00200E8C;
    if ((*(uint64_t *)(arg2 + 0x8)) == (*(uint64_t *)(arg2 + 0x8E80))) goto loc_00200E8C;
    result = KiFindRescheduleContextEntryForPrcb(*(uint64_t *)(arg2 + 0x37E8), 0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x78)), *(uint64_t *)(local_rbx + 0x80));
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x78))) & (2));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x10) + 0x78))) & (2));
    if (((uint8_t)(a3)) > ((uint8_t)(Arg1))) goto loc_002010B4;
loc_00200A21:
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(*(uint64_t *)(result) + 0x8);
    Arg2 = ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(result) + 0x18))) ? 1 : 0;
    result = (uint8_t)((*(uint8_t *)(result + 0x20)) & (254));
    Arg2 = (uint8_t)((Arg2) | ((uint8_t)(result)));
    *(uint8_t *)(result + 0x20) = (uint8_t)(Arg2);
    Arg2 = (uint8_t)((Arg2) & (253));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result) + 0x8) + 0x78))) >> (1));
    result = (uint8_t)((result) & (1));
    result = (uint8_t)((result) + ((uint8_t)(result)));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg2)));
    result = (uint8_t)((result) & (199));
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(result + 0x20) = (uint8_t)(result);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x78))) | (*(uint32_t *)(*(uint64_t *)(arg2 + 0x10) + 0x78)));
    if ((((uint8_t)(Arg1)) & (2)) == 0) goto loc_00200B3B;
    Arg2 = 0;
    v_stack_p20 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8))) <= 0) goto loc_00200B3B;
loc_00200A8A:
    a4 = (Arg2 * 4 + 2) + (0);
    if (result == (*(uint64_t *)(arg2 + 0x37E8) + a4 * 8)) goto loc_00200B2B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x78)))) & (2)) == 0) goto loc_00200F1E;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + a4 * 8 + 0x18) - 1) <= -4) goto loc_00200F53;
loc_00200AD1:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8) + a4 * 8 + 0x20)) & (254));
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + a4 * 8 + 0x10) = *(uint64_t *)(arg2 + 0x8);
    *(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8) + a4 * 8 + 0x20) = (uint8_t)(result);
    result = (uint8_t)((result) & (253));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x78))) >> (1));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg1)));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) & (231));
    Arg1 = (uint8_t)((Arg1) | (4));
    Arg1 = (uint8_t)((Arg1) | (32));
    result = (uint8_t)(((uint8_t)(Arg1)) & (223));
    Arg1 = (uint8_t)(Arg1);
    if ((*(uint64_t *)(arg2 + 0x8)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + a4 * 8) + 0x8E80))) { Arg1 = (uint32_t)((uint8_t)(result)); }
loc_00200B07:
    *(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8) + a4 * 8 + 0x20) = (uint8_t)(Arg1);
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + a4 * 8 + 0x18) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + a4 * 8) + 0x8E80);
    result = KiIsPrcbThread(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + a4 * 8) + 0x8E80), Arg2, a3, *(uint64_t *)(arg2 + 0x37E8) + a4 * 8);
    if ((uint8_t)(result) == 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + a4 * 8) + 0x24);
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + a4 * 8) + 0x8E80) + 0x218) = (uint32_t)(result);
    }
    Arg2 = (uint32_t)((Arg2) + 1);
    v_stack_p20 = (uint32_t)(Arg2);
    if (((uint32_t)(Arg2)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8))))) goto loc_00200A8A;
loc_00200B3B:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x78))) >> (1));
    result = (uint32_t)((result) & (1));
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x4) = (uint32_t)(result);
    local_r12 = 0;
    goto loc_00200B67;
loc_00200B4C:
    goto loc_00200820;
loc_00200B54:
    a3 = (uint32_t)((a3) + (*(uint32_t *)(*(uint64_t *)(arg2 + 0x80))));
    goto loc_0020098B;
loc_00200B63:
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x4) = 0;
loc_00200B67:
    *(uint8_t *)(*(uint64_t *)(arg2 + 0x10) + 0x184) = 1;
    if (0 != 0) goto loc_00200DD5;
loc_00200B78:
    if ((uint32_t)(local_r14) != 0) goto loc_00200E66;
    v_stack_p28 = v_stack_m68;
    v_stack_p20 = (uint8_t)(v_stack_p18);
    result = KiAddThreadToPrcbQueue(Arg2, *(uint64_t *)(arg2 + 0x10), (int8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x10) + 0xC3)), 1);
loc_00200BAE:
    if (((*(uint32_t *)(v_rip + 0xDC5F5C)) & (0x800ULL)) != 0) goto loc_002010C2;
loc_00200BBE:
    result = KiSearchForNewThreadsForRescheduleContext(*(uint64_t *)(arg2 + 0x37E8), v_stack_m60, (uint32_t)(v_stack_m68), 1);
    a3 = 0;
    result = KiCommitRescheduleContext(*(uint64_t *)(arg2 + 0x37E8), Arg2, a3, v_stack_m60);
    v_stack_p20 = *(uint64_t *)(arg2 + 0x10);
    local_r14 = (*(uint64_t *)(arg2 + 0x10) == 0) ? 1 : 0;
    v_stack_p18 = (uint8_t)(local_r14);
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_m58, Arg2, a3, v_stack_m60);
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_00200CB8;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8))) <= 0) goto loc_00200CAC;
loc_00200C15:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x33))) & (16)) != 0) goto loc_00200C35;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x33))) & (8)) == 0) goto loc_00200C53;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x7)) == 0) goto loc_00200C53;
loc_00200C35:
    if ((uint8_t)(*(uint8_t *)(arg2 + 0x35D9)) != 0) goto loc_00200CDF;
    *(uint8_t *)(arg2 + 0x35D9) = 1;
    *(uint32_t *)(arg2 + 0x35DC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24)));
loc_00200C53:
    if (((*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x33)) & (2)) != 0) goto loc_00200DC0;
loc_00200C5F:
    if (((*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x33)) & (4)) == 0) goto loc_00200C7D;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8EB8) != 0) goto loc_00200D2C;
loc_00200C7D:
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8EB8);
    if (((*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x33)) & (1)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28);
    }
    local_r13 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r13)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8))))) goto loc_00200C15;
    local_r12 = 0;
loc_00200CAC:
    result = KiFlushSoftwareInterruptBatch(Arg2 + 13784, Arg2, a3, (int8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x34)));
loc_00200CB8:
    if (v_stack_m60 != 0) goto loc_00200E3A;
    if (v_stack_p20 != 0) goto loc_00200837;
loc_00200CCB:
    a3 = 0;
    result = KiInsertDeferredPreemptionApc(Arg2, v_stack_p8, a3, (int8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x34)));
    goto loc_00200837;
loc_00200CDF:
    if (((uint8_t)(result)) != 1) goto loc_00200D23;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x35DC)))) == (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24))) goto loc_00200C53;
    *(uint8_t *)(arg2 + 0x35D9) = 2;
    result = KeAddProcessorAffinityEx(Arg2 + 13792, (uint32_t)(*(uint32_t *)(arg2 + 0x35DC)), a3, (int8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x34)));
loc_00200D08:
    result = KeAddGroupAffinityEx(Arg2 + 13792, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0xD0), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0xC8), (int8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x34)));
    goto loc_00200C53;
loc_00200D23:
    goto loc_00200D08;
loc_00200D2C:
    if ((*(uint64_t *)(arg2 + 0x8EB8)) == 0) goto loc_00200C7D;
    if (Arg2 == (*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10))) goto loc_00200C7D;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result))))) & (0x40000ULL));
    if (!(condition_is_equal)) {
        a3 = Arg2 + 36536;
    }
    if (condition_is_above_or_equal) goto loc_00200FB5;
loc_00200D66:
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x8EB8) + 0xC) = 2;
    result = (uint32_t)(*(uint32_t *)(result));
    local_r15 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24));
    if ((*(uint8_t *)(v_rip + 0xDC429A)) == 0) {
        result = *(uint8_t *)(v_stack_p18 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24)) * 2 + 0x1);
        local_r15 = *(uint8_t *)(v_stack_p18 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24)) * 2);
        local_r15 = (uint32_t)((local_r15) << (6));
        local_r15 = (uint32_t)((local_r15) | ((uint32_t)(result)));
    }
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x8EB8) + 0x8) = (uint32_t)(local_r15);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xDC5D7B));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDC5D7B)))) & (32)) != 0) {
        Arg1 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24);
        Arg2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(Arg1, Arg2, a3, (int8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x34)));
    }
    Arg2 = ((uint32_t)((uint32_t)(local_r15))) >> (32);
    goto loc_00200C7D;
loc_00200DC0:
    a3 = 0;
    result = EtwTraceScheduleThread(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + local_r12 * 8 + 0x28), *(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10), a3, (int8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x34)));
    goto loc_00200C5F;
loc_00200DD5:
    result = KiIsThreadConstrainedBySchedulingGroup(local_r13, *(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10), 0, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x80));
    if ((uint8_t)(result) == 0) goto loc_00200E31;
    result = KiShouldPreemptionBeDeferred(local_r13, *(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10), 0, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x80));
    if ((uint8_t)(result) != 0) goto loc_00200E31;
    result = KiCheckForMaxOverQuotaScb(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10), *(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10), 0, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x80));
    if ((uint8_t)(result) != 0) goto loc_002010B9;
loc_00200E0A:
    local_r14 = (uint32_t)((0) + (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x7C)));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x80) != 0) goto loc_00200E80;
    if ((uint32_t)(local_r14) != 0) goto loc_00200E24;
loc_00200E18:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x1A0) != 0) goto loc_00200E0A;
loc_00200E24:
    v_stack_p18 = 1;
    if (0 != 0) goto loc_00200B78;
loc_00200E31:
    v_stack_p18 = 0;
    goto loc_00200B78;
loc_00200E3A:
    result = KiReadyDeferredReadyList(Arg2, v_stack_m60, 0, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x80));
    if (local_r15 != 0) goto loc_00200837;
    if ((*(uint64_t *)(arg2 + 0x10)) == 0) goto loc_00200CCB;
    goto loc_002008C2;
loc_00200E66:
    result = KiAddThreadToScbQueue(Arg2, *(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10), local_r13, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x80));
    v_stack_m68 = 2;
    goto loc_00200BAE;
loc_00200E80:
    a3 = (uint32_t)((2) + (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x80))));
    goto loc_00200E18;
loc_00200E8C:
    result = KiFindRescheduleContextEntryForPrcb(*(uint64_t *)(arg2 + 0x37E8), Arg2, a3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x80));
    a3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(result + 0x20)))) >> (1));
    a3 = (uint32_t)((a3) & (1));
    if ((((uint8_t)(*(uint8_t *)(result + 0x20))) & (32)) == 0) {
    }
    Arg2 = (uint8_t)((*(uint8_t *)(result + 0x20)) & (197));
    Arg2 = (uint8_t)((Arg2) | (5));
    *(uint8_t *)(result + 0x20) = (uint8_t)(Arg2);
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    if ((uint32_t)(a3) == 0) goto loc_00200B67;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8))) <= 0) goto loc_00200B63;
loc_00200EEC:
    Arg1 = (0 * 4 + 2) + (0);
    result = 0;
    if ((*(uint64_t *)(arg2 + 0x37E8) + Arg1 * 8) != result) {
        a4 = 0;
        a3 = 1;
        result = KiAdjustRescheduleContextEntryForThreadRemoval(*(uint64_t *)(arg2 + 0x37E8) + Arg1 * 8, Arg2, a3, a4);
    }
    local_r11 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r11)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8))))) goto loc_00200EEC;
    goto loc_00200B63;
loc_00200F1E:
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8))) <= -4) goto loc_00200F86;
loc_00200F28:
    result = (uint8_t)((*(uint8_t *)(a4 + 0x20)) | (1));
    *(uint64_t *)(a4 + 0x10) = *(uint64_t *)(result + 0x18);
    *(uint8_t *)(a4 + 0x20) = (uint8_t)(result);
    result = (uint8_t)((result) & (253));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x78))) >> (1));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg1)));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) & (231));
    Arg1 = (uint8_t)((Arg1) | (4));
    Arg1 = (uint8_t)((Arg1) & (223));
    goto loc_00200B07;
loc_00200F53:
    result = KiIsPrcbThread(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_00200AD1;
    if (((*(uint8_t *)(a4 + 0x21)) & (1)) != 0) {
    }
    *(uint8_t *)(arg1 + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_m50, Arg1, a3, a4);
    goto loc_00200AD1;
loc_00200F86:
    result = KiIsPrcbThread(v_stack_m50, (uint32_t)(v_stack_p20), a3, a4);
    if ((uint8_t)(result) != 0) goto loc_00200F28;
    if (((*(uint8_t *)(a4 + 0x21)) & (1)) != 0) {
    }
    *(uint8_t *)(v_stack_m50 + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_m50, v_stack_m50, a3, a4);
    goto loc_00200F28;
loc_00200FB5:
    if ((uint32_t)((uint32_t)(v_stack_p20)) == 0) goto loc_00200C7D;
    if (((uint32_t)((uint8_t)(result))) >= 0) goto loc_00200C7D;
    goto loc_00200D66;
loc_00200FD1:
    result = KiFindRescheduleContextEntryForPrcb(*(uint64_t *)(arg2 + 0x37E8), Arg2, a3, a4);
    a3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(result + 0x20)))) >> (1));
    a3 = (uint32_t)((a3) & (1));
    if ((((uint8_t)(*(uint8_t *)(result + 0x20))) & (32)) == 0) {
    }
    Arg2 = (uint8_t)((*(uint8_t *)(result + 0x20)) & (197));
    Arg2 = (uint8_t)((Arg2) | (5));
    *(uint8_t *)(result + 0x20) = (uint8_t)(Arg2);
    local_r12 = 0;
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    if ((uint32_t)(a3) == 0) goto loc_00200B67;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8))) <= 0) goto loc_00200B63;
loc_00201034:
    Arg1 = (0 * 4 + 2) + (0);
    result = 0;
    if ((*(uint64_t *)(arg2 + 0x37E8) + Arg1 * 8) != result) {
        a4 = 0;
        a3 = 1;
        result = KiAdjustRescheduleContextEntryForThreadRemoval(*(uint64_t *)(arg2 + 0x37E8) + Arg1 * 8, Arg2, a3, a4);
    }
    local_r11 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r11)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8))))) goto loc_00201034;
    goto loc_00200B63;
loc_00201066:
    if (((uint32_t)(local_r15)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x37E8))))) goto loc_00201077;
    goto loc_00200A21;
loc_00201077:
    Arg1 = (v_stack_p20 * 4 + 2) + ((uint32_t)((uint32_t)(v_stack_p20)));
    if (0 == (*(uint64_t *)(arg2 + 0x37E8) + Arg1 * 8)) goto loc_002010A6;
    a4 = 0;
    result = KiDoesThreadDominateRescheduleContextEntry(*(uint64_t *)(arg2 + 0x37E8) + Arg1 * 8, v_stack_p20, a4 + 2, a4);
    if ((uint8_t)(result) == 0) goto loc_00200FD1;
loc_002010A6:
    local_r15 = (uint32_t)((v_stack_p20) + 1);
    goto loc_00201066;
loc_002010AB:
    local_r14 = (uint32_t)((local_r14) | (0xFFFFFFFFULL));
    goto loc_002009A0;
loc_002010B4:
    local_r15 = 0;
    goto loc_00201066;
loc_002010B9:
    local_r14 = (uint32_t)((local_r14) | (0xFFFFFFFFULL));
    goto loc_00200E31;
loc_002010C2:
    a4 = 0;
    result = EtwTraceReadyQueueInsertion(local_r13, (uint32_t)(*(uint32_t *)(arg2 + 0x24)), a4 + 2, a4);
    goto loc_00200BBE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg2` | `+ 0xD8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0020076C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
