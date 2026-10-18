# KiSearchForNewThreadsForRescheduleContext

- RVA: `0x00258620`–`0x0025980B` (길이 `4,587` bytes)
- VA: `0x0000000140258620`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00063F3C`
- 디코드: `1,140`개 명령, `4,587/4,587` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **39**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **22**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x002586EC` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002586F8` → [KiStartReadyQueueEnumeratorForRescheduleContext](KiStartReadyQueueEnumeratorForRescheduleContext_function_00259820.md) (function, `0x00259820`)
- `0x00258BAC` → [KiComputeThreadQos](KiComputeThreadQos_function_00258010.md) (function, `0x00258010`)
- `0x00258C67` → [KiEvaluateGroupSchedulingPreemption](KiEvaluateGroupSchedulingPreemption_function_00258270.md) (function, `0x00258270`)
- `0x00258CA9` → [KxWaitForLockOwnerShip](KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00258CBC` → [KiAdvanceReadyQueueEnumeratorToNextList](../20/KiAdvanceReadyQueueEnumeratorToNextList_function_00201C50.md) (function, `0x00201C50`)
- `0x00258D14` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00258DFA` → [KiUpdateSoftParkElectionStatisticsOnRemoval](../20/KiUpdateSoftParkElectionStatisticsOnRemoval_function_00201A50.md) (function, `0x00201A50`)
- `0x00258EC6` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x00258F75` → [KiIsThreadConstrainedBySchedulingGroup](../30/KiIsThreadConstrainedBySchedulingGroup_function_0030B200.md) (function, `0x0030B200`)
- `0x00258F85` → [KiCheckForMaxOverQuotaScb](../20/KiCheckForMaxOverQuotaScb_function_002027A0.md) (function, `0x002027A0`)
- `0x00258F95` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x002590B2` → [KiIsThreadExemptFromForcePark](../4D/KiIsThreadExemptFromForcePark_function_004D7B80.md) (function, `0x004D7B80`)
- `0x00259184` → [KiUpdateSoftParkElectionStatisticsOnRemoval](../20/KiUpdateSoftParkElectionStatisticsOnRemoval_function_00201A50.md) (function, `0x00201A50`)
- `0x0025924D` → [KiAdvanceReadyQueueEnumeratorToNextScb](../20/KiAdvanceReadyQueueEnumeratorToNextScb_function_0020227C.md) (function, `0x0020227C`)
- `0x002592B0` → [KiAdvanceReadyQueueEnumeratorToNextList](../20/KiAdvanceReadyQueueEnumeratorToNextList_function_00201C50.md) (function, `0x00201C50`)
- `0x002592C1` → [KiRemoveThreadFromScbQueue](../20/KiRemoveThreadFromScbQueue_function_00201B64.md) (function, `0x00201B64`)
- `0x0025931C` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x00259338` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0025936A` → [KiRemoveThreadFromReadyQueue](../20/KiRemoveThreadFromReadyQueue_function_002016C8.md) (function, `0x002016C8`)
- `0x0025940F` → [KiAdvanceReadyQueueEnumeratorToNextList](../20/KiAdvanceReadyQueueEnumeratorToNextList_function_00201C50.md) (function, `0x00201C50`)
- `0x00259420` → [KiRemoveThreadFromScbQueue](../20/KiRemoveThreadFromScbQueue_function_00201B64.md) (function, `0x00201B64`)
- `0x002594C4` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x00259522` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x002595AB` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x00259627` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x002596A1` → [KiCanLocalReadyThreadBeScheduledToRescheduleContextEntry](KiCanLocalReadyThreadBeScheduledToRescheduleContextEntry_function_00257D10.md) (function, `0x00257D10`)
- `0x002596D1` → [KiDoesThreadDominateRescheduleContextEntry](KiDoesThreadDominateRescheduleContextEntry_function_002581D0.md) (function, `0x002581D0`)
- `0x002596E3` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x00259708` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0025971C` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x00259741` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0025974B` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x00259770` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0025977A` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025979F` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x002597B0` → [KiRemoveCurrentlyEnumeratedThreadFromReadyQueue](../20/KiRemoveCurrentlyEnumeratedThreadFromReadyQueue_function_00201790.md) (function, `0x00201790`)
- `0x002597CA` → [KiAddThreadToScbQueue](../20/KiAddThreadToScbQueue_function_002010DC.md) (function, `0x002010DC`)
- `0x002597F2` → [EtwTraceReadyQueueInsertion](../22/EtwTraceReadyQueueInsertion_function_00223444.md) (function, `0x00223444`)

### Direct callers
- [KiDeferGroupSchedulingPreemption](../20/KiDeferGroupSchedulingPreemption_function_0020076C.md) at `0x00200BC5`
- [KiHandleDeferredPreemption](../20/KiHandleDeferredPreemption_function_00202ECC.md) at `0x00203033`
- [KeYieldExecution](../20/KeYieldExecution_function_00209FA0.md) at `0x0020A2AB`
- [KiRemoveBoostThread](../21/KiRemoveBoostThread_function_00219128.md) at `0x00219278`
- [sub_0021C00A](../21/Unknown_function_0021C00A.md) at `0x0021C0A1`
- [sub_0021D7F8](../21/Unknown_function_0021D7F8.md) at `0x0021E4AA`
- [KiSetPriorityThread](../22/KiSetPriorityThread_function_00220E78.md) at `0x00221055`
- [KiExecuteAllDpcs](KiExecuteAllDpcs_function_0025B740.md) at `0x0025C865`
- [KiUpdateGlobalCpuSetConfiguration](../30/KiUpdateGlobalCpuSetConfiguration_function_00305AB8.md) at `0x00305D8E`
- [KiGroupSchedulingGenerationEnd](../30/KiGroupSchedulingGenerationEnd_function_0030A9B4.md) at `0x0030AA5B`
- [KiGroupSchedulingQuantumEnd](../30/KiGroupSchedulingQuantumEnd_function_0030B220.md) at `0x0030B5CE`
- [KiSoftParkElectionUnparkProcessor](../30/KiSoftParkElectionUnparkProcessor_function_0030B818.md) at `0x0030B95A`
- [KiEnterLongDpcProcessing](../30/KiEnterLongDpcProcessing_function_0030BE54.md) at `0x0030C238`
- [KiRescheduleThreadAfterAffinityChange](../30/KiRescheduleThreadAfterAffinityChange_function_0030C9E8.md) at `0x0030CB32`
- [KiAttemptToStealStandbyThread](../30/KiAttemptToStealStandbyThread_function_0030D790.md) at `0x0030D9FF`
- [KiAttemptToStealStandbyThread](../30/KiAttemptToStealStandbyThread_function_0030D790.md) at `0x0030DB14`
- [KiExitThreadWaitReschedule](../35/KiExitThreadWaitReschedule_function_00352EC8.md) at `0x00352F81`
- [KiParkCurrentProcessor](../35/KiParkCurrentProcessor_function_003533A4.md) at `0x003534A1`
- [KiSearchForNewThread](../35/KiSearchForNewThread_function_00355C98.md) at `0x00355D01`
- [KiSetSystemAffinityThread](../39/KiSetSystemAffinityThread_function_003993E0.md) at `0x003997A6`
- [KiApplyForegroundBoostThread](../4F/KiApplyForegroundBoostThread_function_004F7DC0.md) at `0x004F7F6B`
- [KiAdjustCoreIsolationReasonThread](../5C/KiAdjustCoreIsolationReasonThread_function_005C3818.md) at `0x005C39FD`
- [KiForceParkDutyCycleDpcCallback](../5C/KiForceParkDutyCycleDpcCallback_function_005C97D0.md) at `0x005C98C0`

### Static image references
- `0x0025863F` → RVA `0x00E0A740` (`.data`; read)
- `0x002586AC` → RVA `0x00FC6B38` (`ALMOSTRO`; read)
- `0x0025893D` → RVA `0x00FC6BF8` (`ALMOSTRO`; read)
- `0x00258B6B` → RVA `0x00FC52E0` (`ALMOSTRO`; read)
- `0x00258BC8` → RVA `0x00FC537C` (`ALMOSTRO`; read)
- `0x00258C42` → RVA `0x00FC6ABC` (`ALMOSTRO`; read)
- `0x00259478` → RVA `0x00FCFF00` (`CACHEALI`; read)
- `0x002597CF` → RVA `0x00FC6B14` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002589BF` → [sub_006D8D62](../6D/Unknown_function_006D8D62.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00258620  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00258625  55                              push rbp
00258626  56                              push rsi
00258627  57                              push rdi
00258628  41 54                           push r12
0025862A  41 55                           push r13
0025862C  41 56                           push r14
0025862E  41 57                           push r15
00258630  48 8D AC 24 60 FF FF FF         lea rbp, [rsp - 0xa0]
00258638  48 81 EC A0 01 00 00            sub rsp, 0x1a0
0025863F  48 8B 05 FA 20 BB 00            mov rax, qword ptr [rip + 0xbb20fa]
00258646  48 33 C4                        xor rax, rsp
00258649  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
00258650  45 33 F6                        xor r14d, r14d
00258653  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00258658  45 8B C6                        mov r8d, r14d
0025865B  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00258660  41 8B FE                        mov edi, r14d
00258663  4C 8B FA                        mov r15, rdx
00258666  4C 8B E9                        mov r13, rcx
00258669  41 0F B6 45 00                  movzx eax, byte ptr [r13]
0025866E  49 8B DE                        mov rbx, r14
00258671  84 C0                           test al, al
00258673  74 6B                           je 0x1402586e0
00258675  49 8D 4D 18                     lea rcx, [r13 + 0x18]
00258679  8B D0                           mov edx, eax
0025867B  48 8B 01                        mov rax, qword ptr [rcx]
0025867E  49 3B C0                        cmp rax, r8
00258681  76 0D                           jbe 0x140258690
00258683  48 85 DB                        test rbx, rbx
00258686  74 05                           je 0x14025868d
00258688  48 3B C3                        cmp rax, rbx
0025868B  73 03                           jae 0x140258690
0025868D  48 8B D8                        mov rbx, rax
00258690  48 83 C1 28                     add rcx, 0x28
00258694  48 83 EA 01                     sub rdx, 1
00258698  75 E1                           jne 0x14025867b
0025869A  48 85 DB                        test rbx, rbx
0025869D  74 41                           je 0x1402586e0
0025869F  8B CF                           mov ecx, edi
002586A1  48 83 C1 0B                     add rcx, 0xb
002586A5  48 C1 E1 04                     shl rcx, 4
002586A9  49 03 CD                        add rcx, r13
002586AC  F7 05 82 E4 D6 00 00 00 20 00   test dword ptr [rip + 0xd6e482], 0x200000
002586B6  0F 84 F2 02 00 00               je 0x1402589ae
002586BC  48 89 59 08                     mov qword ptr [rcx + 8], rbx
002586C0  48 8B D1                        mov rdx, rcx
002586C3  4C 89 31                        mov qword ptr [rcx], r14
002586C6  90                              nop
002586C7  48 87 13                        xchg qword ptr [rbx], rdx
002586CA  48 85 D2                        test rdx, rdx
002586CD  0F 85 D6 05 00 00               jne 0x140258ca9
002586D3  FF C7                           inc edi
002586D5  4C 8B C3                        mov r8, rbx
002586D8  EB 8F                           jmp 0x140258669
002586DA  66 0F 1F 44 00 00               nop word ptr [rax + rax]
002586E0  33 D2                           xor edx, edx
002586E2  48 8D 4D A0                     lea rcx, [rbp - 0x60]
002586E6  41 B8 F0 00 00 00               mov r8d, 0xf0
002586EC  E8 4F E5 46 00                  call 0x1406c6c40
002586F1  49 8B D5                        mov rdx, r13
002586F4  48 8D 4D A0                     lea rcx, [rbp - 0x60]
002586F8  E8 23 11 00 00                  call 0x140259820
002586FD  0F B6 45 AD                     movzx eax, byte ptr [rbp - 0x53]
00258701  3C 04                           cmp al, 4
00258703  0F 84 C0 05 00 00               je 0x140258cc9
00258709  84 C0                           test al, al
0025870B  0F 85 DF 01 00 00               jne 0x1402588f0
00258711  44 0F B6 55 A9                  movzx r10d, byte ptr [rbp - 0x57]
00258716  40 B7 01                        mov dil, 1
00258719  44 8B 45 A0                     mov r8d, dword ptr [rbp - 0x60]
0025871D  0F 1F 00                        nop dword ptr [rax]
00258720  40 0F B6 CF                     movzx ecx, dil
00258724  83 F9 02                        cmp ecx, 2
00258727  0F 84 09 01 00 00               je 0x140258836
0025872D  83 E9 01                        sub ecx, 1
00258730  0F 85 8E 02 00 00               jne 0x1402589c4
00258736  41 8B C6                        mov eax, r14d
00258739  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
0025873C  45 85 C0                        test r8d, r8d
0025873F  0F 85 5A 03 00 00               jne 0x140258a9f
00258745  83 E0 FE                        and eax, 0xfffffffe
00258748  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
0025874B  0F 84 84 01 00 00               je 0x1402588d5
00258751  44 0F BD D8                     bsr r11d, eax
00258755  44 88 55 AA                     mov byte ptr [rbp - 0x56], r10b
00258759  41 B9 01 00 00 00               mov r9d, 1
0025875F  44 88 5D A8                     mov byte ptr [rbp - 0x58], r11b
00258763  41 0F B6 C2                     movzx eax, r10b
00258767  41 0F B6 DB                     movzx ebx, r11b
0025876B  44 89 5C 24 44                  mov dword ptr [rsp + 0x44], r11d
00258770  48 8D 0C 40                     lea rcx, [rax + rax*2]
00258774  48 03 C9                        add rcx, rcx
00258777  8B 54 CD F8                     mov edx, dword ptr [rbp + rcx*8 - 8]
0025877B  0B 54 CD FC                     or edx, dword ptr [rbp + rcx*8 - 4]
0025877F  8B CB                           mov ecx, ebx
00258781  41 D3 E1                        shl r9d, cl
00258784  44 85 CA                        test edx, r9d
00258787  75 2F                           jne 0x1402587b8
00258789  41 FE C2                        inc r10b
0025878C  41 0F B6 C2                     movzx eax, r10b
00258790  44 88 55 AA                     mov byte ptr [rbp - 0x56], r10b
00258794  41 3B C0                        cmp eax, r8d
00258797  72 07                           jb 0x1402587a0
00258799  45 32 D2                        xor r10b, r10b
0025879C  44 88 55 AA                     mov byte ptr [rbp - 0x56], r10b
002587A0  41 0F B6 C2                     movzx eax, r10b
002587A4  48 8D 0C 40                     lea rcx, [rax + rax*2]
002587A8  48 03 C9                        add rcx, rcx
002587AB  8B 54 CD F8                     mov edx, dword ptr [rbp + rcx*8 - 8]
002587AF  0B 54 CD FC                     or edx, dword ptr [rbp + rcx*8 - 4]
002587B3  44 85 CA                        test edx, r9d
002587B6  74 D1                           je 0x140258789
002587B8  41 0F B6 C2                     movzx eax, r10b
002587BC  48 8D 55 D0                     lea rdx, [rbp - 0x30]
002587C0  48 8D 0C 40                     lea rcx, [rax + rax*2]
002587C4  48 C1 E1 04                     shl rcx, 4
002587C8  48 03 D1                        add rdx, rcx
002587CB  32 C9                           xor cl, cl
002587CD  4C 8B 12                        mov r10, qword ptr [rdx]
002587D0  4C 8B 42 08                     mov r8, qword ptr [rdx + 8]
002587D4  88 4D AB                        mov byte ptr [rbp - 0x55], cl
002587D7  44 85 4A 28                     test dword ptr [rdx + 0x28], r9d
002587DB  74 05                           je 0x1402587e2
002587DD  B1 01                           mov cl, 1
002587DF  88 4D AB                        mov byte ptr [rbp - 0x55], cl
002587E2  44 85 4A 2C                     test dword ptr [rdx + 0x2c], r9d
002587E6  74 06                           je 0x1402587ee
002587E8  80 C9 02                        or cl, 2
002587EB  88 4D AB                        mov byte ptr [rbp - 0x55], cl
002587EE  0F B6 D1                        movzx edx, cl
002587F1  8D 42 FF                        lea eax, [rdx - 1]
002587F4  85 C2                           test edx, eax
002587F6  0F 85 85 0A 00 00               jne 0x140259281
002587FC  0F BC C2                        bsf eax, edx
002587FF  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00258803  88 45 AC                        mov byte ptr [rbp - 0x54], al
00258806  0F B6 C8                        movzx ecx, al
00258809  84 C0                           test al, al
0025880B  0F 84 34 07 00 00               je 0x140258f45
00258811  83 F9 01                        cmp ecx, 1
00258814  75 13                           jne 0x140258829
00258816  41 0F B6 C3                     movzx eax, r11b
0025881A  48 83 C0 04                     add rax, 4
0025881E  48 C1 E0 04                     shl rax, 4
00258822  49 03 C0                        add rax, r8
00258825  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00258829  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
0025882D  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00258831  E9 AC 00 00 00                  jmp 0x1402588e2
00258836  32 D2                           xor dl, dl
00258838  45 85 C0                        test r8d, r8d
0025883B  74 57                           je 0x140258894
0025883D  0F 1F 00                        nop dword ptr [rax]
00258840  0F B6 C2                        movzx eax, dl
00258843  48 8D 0C 40                     lea rcx, [rax + rax*2]
00258847  48 03 C9                        add rcx, rcx
0025884A  44 8B 4C CD F0                  mov r9d, dword ptr [rbp + rcx*8 - 0x10]
0025884F  45 85 C9                        test r9d, r9d
00258852  74 31                           je 0x140258885
00258854  48 8B 44 CD D0                  mov rax, qword ptr [rbp + rcx*8 - 0x30]
00258859  48 05 30 84 00 00               add rax, 0x8430
0025885F  4C 8B 40 08                     mov r8, qword ptr [rax + 8]
00258863  41 F6 C0 01                     test r8b, 1
00258867  0F 85 2B 01 00 00               jne 0x140258998
0025886D  49 8B C0                        mov rax, r8
00258870  48 85 C0                        test rax, rax
00258873  0F 85 B0 07 00 00               jne 0x140259029
00258879  49 8B C6                        mov rax, r14
0025887C  48 89 44 CD E0                  mov qword ptr [rbp + rcx*8 - 0x20], rax
00258881  44 8B 45 A0                     mov r8d, dword ptr [rbp - 0x60]
00258885  FE C2                           inc dl
00258887  0F B6 C2                        movzx eax, dl
0025888A  41 3B C0                        cmp eax, r8d
0025888D  72 B1                           jb 0x140258840
0025888F  44 0F B6 55 A9                  movzx r10d, byte ptr [rbp - 0x57]
00258894  32 DB                           xor bl, bl
00258896  4D 8B DE                        mov r11, r14
00258899  41 0F B6 D2                     movzx edx, r10b
0025889D  0F 1F 00                        nop dword ptr [rax]
002588A0  0F B6 C2                        movzx eax, dl
002588A3  48 8D 0C 40                     lea rcx, [rax + rax*2]
002588A7  48 03 C9                        add rcx, rcx
002588AA  4C 8B 4C CD E0                  mov r9, qword ptr [rbp + rcx*8 - 0x20]
002588AF  4D 85 C9                        test r9, r9
002588B2  0F 85 84 07 00 00               jne 0x14025903c
002588B8  FE C2                           inc dl
002588BA  0F B6 C2                        movzx eax, dl
002588BD  41 3B C0                        cmp eax, r8d
002588C0  0F B6 D2                        movzx edx, dl
002588C3  41 0F 43 D6                     cmovae edx, r14d
002588C7  41 3A D2                        cmp dl, r10b
002588CA  75 D4                           jne 0x1402588a0
002588CC  4D 85 DB                        test r11, r11
002588CF  0F 85 7B 07 00 00               jne 0x140259050
002588D5  40 FE C7                        inc dil
002588D8  40 80 FF 04                     cmp dil, 4
002588DC  0F 82 3E FE FF FF               jb 0x140258720
002588E2  40 88 7D AD                     mov byte ptr [rbp - 0x53], dil
002588E6  40 80 FF 04                     cmp dil, 4
002588EA  0F 84 D9 03 00 00               je 0x140258cc9
002588F0  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
002588F4  48 8B 38                        mov rdi, qword ptr [rax]
002588F7  48 89 7D C8                     mov qword ptr [rbp - 0x38], rdi
002588FB  48 3B 7D C0                     cmp rdi, qword ptr [rbp - 0x40]
002588FF  0F 84 B3 03 00 00               je 0x140258cb8
00258905  0F B6 45 AA                     movzx eax, byte ptr [rbp - 0x56]
00258909  48 8D B7 28 FF FF FF            lea rsi, [rdi - 0xd8]
00258910  48 8D 0C 40                     lea rcx, [rax + rax*2]
00258914  48 03 C9                        add rcx, rcx
00258917  80 7D AD 02                     cmp byte ptr [rbp - 0x53], 2
0025891B  48 8B 5C CD D0                  mov rbx, qword ptr [rbp + rcx*8 - 0x30]
00258920  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00258925  0F 84 C8 08 00 00               je 0x1402591f3
0025892B  80 7D AC 01                     cmp byte ptr [rbp - 0x54], 1
0025892F  0F 85 08 06 00 00               jne 0x140258f3d
00258935  4C 8B 64 CD D8                  mov r12, qword ptr [rbp + rcx*8 - 0x28]
0025893A  49 8B D6                        mov rdx, r14
0025893D  48 8B 05 B4 E2 D6 00            mov rax, qword ptr [rip + 0xd6e2b4]
00258944  48 39 86 38 02 00 00            cmp qword ptr [rsi + 0x238], rax
0025894B  0F 85 81 07 00 00               jne 0x1402590d2
00258951  48 85 D2                        test rdx, rdx
00258954  0F 84 68 01 00 00               je 0x140258ac2
0025895A  8B 4E 78                        mov ecx, dword ptr [rsi + 0x78]
0025895D  D1 E9                           shr ecx, 1
0025895F  83 E1 01                        and ecx, 1
00258962  41 3B 4D 08                     cmp ecx, dword ptr [r13 + 8]
00258966  0F 8F 91 FD FF FF               jg 0x1402586fd
0025896C  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
00258970  3B C8                           cmp ecx, eax
00258972  0F 4C C8                        cmovl ecx, eax
00258975  85 C9                           test ecx, ecx
00258977  0F 85 E8 0C 00 00               jne 0x140259665
0025897D  41 0F B6 45 00                  movzx eax, byte ptr [r13]
00258982  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
00258987  44 3B F0                        cmp r14d, eax
0025898A  0F 82 C9 01 00 00               jb 0x140258b59
00258990  45 33 F6                        xor r14d, r14d
00258993  E9 65 FD FF FF                  jmp 0x1402586fd
00258998  49 83 F8 01                     cmp r8, 1
0025899C  0F 84 D7 FE FF FF               je 0x140258879
002589A2  48 83 C8 01                     or rax, 1
002589A6  49 33 C0                        xor rax, r8
002589A9  E9 C2 FE FF FF                  jmp 0x140258870
002589AE  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
002589B3  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
002589B9  0F 83 14 FD FF FF               jae 0x1402586d3
002589BF  E9 9E 03 48 00                  jmp 0x1406d8d62
002589C4  83 F9 02                        cmp ecx, 2
002589C7  0F 85 08 FF FF FF               jne 0x1402588d5
002589CD  41 8B C6                        mov eax, r14d
002589D0  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
002589D3  45 85 C0                        test r8d, r8d
002589D6  0F 85 AA 02 00 00               jne 0x140258c86
002589DC  83 E0 01                        and eax, 1
002589DF  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
002589E2  0F 84 ED FE FF FF               je 0x1402588d5
002589E8  44 0F BD D8                     bsr r11d, eax
002589EC  44 88 55 AA                     mov byte ptr [rbp - 0x56], r10b
002589F0  41 B9 01 00 00 00               mov r9d, 1
002589F6  44 88 5D A8                     mov byte ptr [rbp - 0x58], r11b
002589FA  41 0F B6 C2                     movzx eax, r10b
002589FE  41 0F B6 DB                     movzx ebx, r11b
00258A02  44 89 5C 24 3C                  mov dword ptr [rsp + 0x3c], r11d
00258A07  48 8D 0C 40                     lea rcx, [rax + rax*2]
00258A0B  48 03 C9                        add rcx, rcx
00258A0E  8B 54 CD F8                     mov edx, dword ptr [rbp + rcx*8 - 8]
00258A12  0B 54 CD FC                     or edx, dword ptr [rbp + rcx*8 - 4]
00258A16  8B CB                           mov ecx, ebx
00258A18  41 D3 E1                        shl r9d, cl
00258A1B  44 85 CA                        test edx, r9d
00258A1E  75 2F                           jne 0x140258a4f
00258A20  41 FE C2                        inc r10b
00258A23  41 0F B6 C2                     movzx eax, r10b
00258A27  44 88 55 AA                     mov byte ptr [rbp - 0x56], r10b
00258A2B  41 3B C0                        cmp eax, r8d
00258A2E  72 07                           jb 0x140258a37
00258A30  45 32 D2                        xor r10b, r10b
00258A33  44 88 55 AA                     mov byte ptr [rbp - 0x56], r10b
00258A37  41 0F B6 C2                     movzx eax, r10b
00258A3B  48 8D 0C 40                     lea rcx, [rax + rax*2]
00258A3F  48 03 C9                        add rcx, rcx
00258A42  8B 54 CD F8                     mov edx, dword ptr [rbp + rcx*8 - 8]
00258A46  0B 54 CD FC                     or edx, dword ptr [rbp + rcx*8 - 4]
00258A4A  44 85 CA                        test edx, r9d
00258A4D  74 D1                           je 0x140258a20
00258A4F  41 0F B6 C2                     movzx eax, r10b
00258A53  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00258A57  48 8D 0C 40                     lea rcx, [rax + rax*2]
00258A5B  48 C1 E1 04                     shl rcx, 4
00258A5F  48 03 D1                        add rdx, rcx
00258A62  32 C9                           xor cl, cl
00258A64  4C 8B 12                        mov r10, qword ptr [rdx]
00258A67  4C 8B 42 08                     mov r8, qword ptr [rdx + 8]
00258A6B  88 4D AB                        mov byte ptr [rbp - 0x55], cl
00258A6E  44 85 4A 28                     test dword ptr [rdx + 0x28], r9d
00258A72  74 05                           je 0x140258a79
00258A74  B1 01                           mov cl, 1
00258A76  88 4D AB                        mov byte ptr [rbp - 0x55], cl
00258A79  44 85 4A 2C                     test dword ptr [rdx + 0x2c], r9d
00258A7D  74 06                           je 0x140258a85
00258A7F  80 C9 02                        or cl, 2
00258A82  88 4D AB                        mov byte ptr [rbp - 0x55], cl
00258A85  0F B6 D1                        movzx edx, cl
00258A88  8D 42 FF                        lea eax, [rdx - 1]
00258A8B  85 C2                           test edx, eax
00258A8D  0F 85 E1 08 00 00               jne 0x140259374
00258A93  0F BC C2                        bsf eax, edx
00258A96  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00258A9A  E9 64 FD FF FF                  jmp 0x140258803
00258A9F  48 8D 4D FC                     lea rcx, [rbp - 4]
00258AA3  41 8B D0                        mov edx, r8d
00258AA6  0B 41 FC                        or eax, dword ptr [rcx - 4]
00258AA9  48 8D 49 30                     lea rcx, [rcx + 0x30]
00258AAD  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
00258AB0  0B 41 D0                        or eax, dword ptr [rcx - 0x30]
00258AB3  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
00258AB6  48 83 EA 01                     sub rdx, 1
00258ABA  0F 84 85 FC FF FF               je 0x140258745
00258AC0  EB E4                           jmp 0x140258aa6
00258AC2  48 8B 46 68                     mov rax, qword ptr [rsi + 0x68]
00258AC6  48 85 C0                        test rax, rax
00258AC9  0F 84 8B FE FF FF               je 0x14025895a
00258ACF  8B 8B D8 00 00 00               mov ecx, dword ptr [rbx + 0xd8]
00258AD5  48 03 C8                        add rcx, rax
00258AD8  0F 84 7C FE FF FF               je 0x14025895a
00258ADE  80 BE C3 00 00 00 10            cmp byte ptr [rsi + 0xc3], 0x10
00258AE5  45 8B C6                        mov r8d, r14d
00258AE8  0F 8D 6C FE FF FF               jge 0x14025895a
00258AEE  F7 46 78 00 02 00 00            test dword ptr [rsi + 0x78], 0x200
00258AF5  0F 85 5F FE FF FF               jne 0x14025895a
00258AFB  83 BE E4 01 00 00 00            cmp dword ptr [rsi + 0x1e4], 0
00258B02  0F 85 52 FE FF FF               jne 0x14025895a
00258B08  80 BE 86 01 00 00 01            cmp byte ptr [rsi + 0x186], 1
00258B0F  0F 84 45 FE FF FF               je 0x14025895a
00258B15  48 8B D1                        mov rdx, rcx
00258B18  4C 8B F1                        mov r14, rcx
00258B1B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00258B20  F6 42 70 02                     test byte ptr [rdx + 0x70], 2
00258B24  0F 85 7F 0C 00 00               jne 0x1402597a9
00258B2A  48 8B 92 A0 01 00 00            mov rdx, qword ptr [rdx + 0x1a0]
00258B31  48 85 D2                        test rdx, rdx
00258B34  75 EA                           jne 0x140258b20
00258B36  44 03 41 7C                     add r8d, dword ptr [rcx + 0x7c]
00258B3A  75 0C                           jne 0x140258b48
00258B3C  48 8B 89 A0 01 00 00            mov rcx, qword ptr [rcx + 0x1a0]
00258B43  48 85 C9                        test rcx, rcx
00258B46  75 EE                           jne 0x140258b36
00258B48  45 85 C0                        test r8d, r8d
00258B4B  0F 85 58 0C 00 00               jne 0x1402597a9
00258B51  45 33 F6                        xor r14d, r14d
00258B54  E9 01 FE FF FF                  jmp 0x14025895a
00258B59  41 8B C6                        mov eax, r14d
00258B5C  48 8D 0C 80                     lea rcx, [rax + rax*4]
00258B60  4C 8D 3C CD 00 00 00 00         lea r15, [rcx*8]
00258B68  4D 03 FD                        add r15, r13
00258B6B  83 3D 6E C7 D6 00 00            cmp dword ptr [rip + 0xd6c76e], 0
00258B72  4D 8B 6F 10                     mov r13, qword ptr [r15 + 0x10]
00258B76  74 0B                           je 0x140258b83
00258B78  41 F6 45 23 20                  test byte ptr [r13 + 0x23], 0x20
00258B7D  0F 85 2C 05 00 00               jne 0x1402590af
00258B83  4D 85 E4                        test r12, r12
00258B86  0F 84 38 05 00 00               je 0x1402590c4
00258B8C  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
00258B90  48 85 C0                        test rax, rax
00258B93  0F 84 DB 00 00 00               je 0x140258c74
00258B99  49 3B C4                        cmp rax, r12
00258B9C  0F 85 D2 00 00 00               jne 0x140258c74
00258BA2  49 8B 9D C0 00 00 00            mov rbx, qword ptr [r13 + 0xc0]
00258BA9  48 8B CE                        mov rcx, rsi
00258BAC  E8 5F F4 FF FF                  call 0x140258010
00258BB1  44 8B 46 50                     mov r8d, dword ptr [rsi + 0x50]
00258BB5  8B 4E 54                        mov ecx, dword ptr [rsi + 0x54]
00258BB8  44 3B C1                        cmp r8d, ecx
00258BBB  44 0F 46 C1                     cmovbe r8d, ecx
00258BBF  0F B6 8E 05 02 00 00            movzx ecx, byte ptr [rsi + 0x205]
00258BC6  33 D2                           xor edx, edx
00258BC8  44 3B 05 AD C7 D6 00            cmp r8d, dword ptr [rip + 0xd6c7ad]
00258BCF  0F 93 C2                        setae dl
00258BD2  44 8D 04 42                     lea r8d, [rdx + rax*2]
00258BD6  0F B6 83 B9 00 00 00            movzx eax, byte ptr [rbx + 0xb9]
00258BDD  44 0F AF C0                     imul r8d, eax
00258BE1  48 8B 83 C0 00 00 00            mov rax, qword ptr [rbx + 0xc0]
00258BE8  44 03 C1                        add r8d, ecx
00258BEB  4B 8D 0C 40                     lea rcx, [r8 + r8*2]
00258BEF  4C 8B 44 C8 10                  mov r8, qword ptr [rax + rcx*8 + 0x10]
00258BF4  48 8B 54 C8 08                  mov rdx, qword ptr [rax + rcx*8 + 8]
00258BF9  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00258BFD  49 23 D0                        and rdx, r8
00258C00  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
00258C04  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
00258C09  48 23 D0                        and rdx, rax
00258C0C  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
00258C11  0F 10 44 24 60                  movups xmm0, xmmword ptr [rsp + 0x60]
00258C16  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
00258C1B  F2 0F 10 4C 24 70               movsd xmm1, qword ptr [rsp + 0x70]
00258C21  0F 11 45 80                     movups xmmword ptr [rbp - 0x80], xmm0
00258C25  F2 0F 11 4D 90                  movsd qword ptr [rbp - 0x70], xmm1
00258C2A  4D 85 85 C8 00 00 00            test qword ptr [r13 + 0xc8], r8
00258C31  0F 84 31 06 00 00               je 0x140259268
00258C37  4C 3B 6C 24 50                  cmp r13, qword ptr [rsp + 0x50]
00258C3C  0F 85 19 03 00 00               jne 0x140258f5b
00258C42  80 3D 73 DE D6 00 00            cmp byte ptr [rip + 0xd6de73], 0
00258C49  48 C7 44 24 78 00 00 00 00      mov qword ptr [rsp + 0x78], 0
00258C52  0F 84 49 07 00 00               je 0x1402593a1
00258C58  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
00258C5D  45 33 C0                        xor r8d, r8d
00258C60  48 8B D6                        mov rdx, rsi
00258C63  49 8D 4F 10                     lea rcx, [r15 + 0x10]
00258C67  E8 04 F6 FF FF                  call 0x140258270
00258C6C  84 C0                           test al, al
00258C6E  0F 85 D1 00 00 00               jne 0x140258d45
00258C74  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00258C79  41 FF C6                        inc r14d
00258C7C  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00258C81  E9 F7 FC FF FF                  jmp 0x14025897d
00258C86  48 8D 4D FC                     lea rcx, [rbp - 4]
00258C8A  41 8B D0                        mov edx, r8d
00258C8D  0B 41 FC                        or eax, dword ptr [rcx - 4]
00258C90  48 8D 49 30                     lea rcx, [rcx + 0x30]
00258C94  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
00258C97  0B 41 D0                        or eax, dword ptr [rcx - 0x30]
00258C9A  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
00258C9D  48 83 EA 01                     sub rdx, 1
00258CA1  0F 84 35 FD FF FF               je 0x1402589dc
00258CA7  EB E4                           jmp 0x140258c8d
00258CA9  E8 02 F2 FF FF                  call 0x140257eb0
00258CAE  FF C7                           inc edi
00258CB0  4C 8B C3                        mov r8, rbx
00258CB3  E9 B1 F9 FF FF                  jmp 0x140258669
00258CB8  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00258CBC  E8 8F 8F FA FF                  call 0x140201c50
00258CC1  85 C0                           test eax, eax
00258CC3  0F 89 27 FC FF FF               jns 0x1402588f0
00258CC9  4D 8B C6                        mov r8, r14
00258CCC  41 8B F6                        mov esi, r14d
00258CCF  90                              nop
00258CD0  41 0F B6 45 00                  movzx eax, byte ptr [r13]
00258CD5  49 8B DE                        mov rbx, r14
00258CD8  84 C0                           test al, al
00258CDA  74 2E                           je 0x140258d0a
00258CDC  49 8D 4D 18                     lea rcx, [r13 + 0x18]
00258CE0  8B D0                           mov edx, eax
00258CE2  48 8B 01                        mov rax, qword ptr [rcx]
00258CE5  49 3B C0                        cmp rax, r8
00258CE8  76 0D                           jbe 0x140258cf7
00258CEA  48 85 DB                        test rbx, rbx
00258CED  74 05                           je 0x140258cf4
00258CEF  48 3B C3                        cmp rax, rbx
00258CF2  73 03                           jae 0x140258cf7
00258CF4  48 8B D8                        mov rbx, rax
00258CF7  48 83 C1 28                     add rcx, 0x28
00258CFB  48 83 EA 01                     sub rdx, 1
00258CFF  75 E1                           jne 0x140258ce2
00258D01  48 85 DB                        test rbx, rbx
00258D04  0F 85 DD 05 00 00               jne 0x1402592e7
00258D0A  48 8B 8D 90 00 00 00            mov rcx, qword ptr [rbp + 0x90]
00258D11  48 33 CC                        xor rcx, rsp
00258D14  E8 27 39 45 00                  call 0x1406ac640
00258D19  48 8B 9C 24 F0 01 00 00         mov rbx, qword ptr [rsp + 0x1f0]
00258D21  48 81 C4 A0 01 00 00            add rsp, 0x1a0
00258D28  41 5F                           pop r15
00258D2A  41 5E                           pop r14
00258D2C  41 5D                           pop r13
00258D2E  41 5C                           pop r12
00258D30  5F                              pop rdi
00258D31  5E                              pop rsi
00258D32  5D                              pop rbp
00258D33  C3                              ret
00258D34  CC                              int3
00258D35  A8 10                           test al, 0x10
00258D37  0F 84 37 FF FF FF               je 0x140258c74
00258D3D  84 C9                           test cl, cl
00258D3F  0F 84 2F FF FF FF               je 0x140258c74
00258D45  49 8B 5F 10                     mov rbx, qword ptr [r15 + 0x10]
00258D49  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00258D4E  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
00258D53  48 85 DB                        test rbx, rbx
00258D56  0F 84 34 FC FF FF               je 0x140258990
00258D5C  0F B6 45 AA                     movzx eax, byte ptr [rbp - 0x56]
00258D60  44 0F B6 7D A8                  movzx r15d, byte ptr [rbp - 0x58]
00258D65  48 8D 0C 40                     lea rcx, [rax + rax*2]
00258D69  48 03 C9                        add rcx, rcx
00258D6C  80 7D AD 02                     cmp byte ptr [rbp - 0x53], 2
00258D70  4C 8B 74 CD D0                  mov r14, qword ptr [rbp + rcx*8 - 0x30]
00258D75  0F 84 16 05 00 00               je 0x140259291
00258D7B  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00258D7F  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00258D83  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
00258D87  0F B6 4D AC                     movzx ecx, byte ptr [rbp - 0x54]
00258D8B  85 C9                           test ecx, ecx
00258D8D  0F 84 14 02 00 00               je 0x140258fa7
00258D93  83 F9 01                        cmp ecx, 1
00258D96  75 67                           jne 0x140258dff
00258D98  0F B6 4D AB                     movzx ecx, byte ptr [rbp - 0x55]
00258D9C  8D 41 FF                        lea eax, [rcx - 1]
00258D9F  85 C1                           test ecx, eax
00258DA1  74 08                           je 0x140258dab
00258DA3  45 0F AB BE DC 83 00 00         bts dword ptr [r14 + 0x83dc], r15d
00258DAB  F7 46 78 00 00 40 00            test dword ptr [rsi + 0x78], 0x400000
00258DB2  4D 8B 8E 48 8E 00 00            mov r9, qword ptr [r14 + 0x8e48]
00258DB9  0F 85 19 06 00 00               jne 0x1402593d8
00258DBF  48 8B 0F                        mov rcx, qword ptr [rdi]
00258DC2  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00258DC6  48 39 79 08                     cmp qword ptr [rcx + 8], rdi
00258DCA  75 09                           jne 0x140258dd5
00258DCC  48 39 38                        cmp qword ptr [rax], rdi
00258DCF  0F 84 44 01 00 00               je 0x140258f19
00258DD5  B9 03 00 00 00                  mov ecx, 3
00258DDA  CD 29                           int 0x29
00258DDC  41 83 41 0C FF                  add dword ptr [r9 + 0xc], -1
00258DE1  0F 84 14 01 00 00               je 0x140258efb
00258DE7  8B 86 F8 06 00 00               mov eax, dword ptr [rsi + 0x6f8]
00258DED  49 8B C9                        mov rcx, r9
00258DF0  49 29 41 10                     sub qword ptr [r9 + 0x10], rax
00258DF4  45 33 C0                        xor r8d, r8d
00258DF7  48 8B D6                        mov rdx, rsi
00258DFA  E8 51 8C FA FF                  call 0x140201a50
00258DFF  45 0F B6 45 00                  movzx r8d, byte ptr [r13]
00258E04  45 33 C9                        xor r9d, r9d
00258E07  33 D2                           xor edx, edx
00258E09  0F 1F 80 00 00 00 00            nop dword ptr [rax]
00258E10  41 3B D0                        cmp edx, r8d
00258E13  73 1E                           jae 0x140258e33
00258E15  48 8D 0C 92                     lea rcx, [rdx + rdx*4]
00258E19  48 8D 04 CD 00 00 00 00         lea rax, [rcx*8]
00258E21  4A 39 5C 28 10                  cmp qword ptr [rax + r13 + 0x10], rbx
00258E26  74 04                           je 0x140258e2c
00258E28  FF C2                           inc edx
00258E2A  EB E4                           jmp 0x140258e10
00258E2C  4D 8D 4D 10                     lea r9, [r13 + 0x10]
00258E30  4C 03 C8                        add r9, rax
00258E33  44 8B 56 78                     mov r10d, dword ptr [rsi + 0x78]
00258E37  41 0F B6 41 20                  movzx eax, byte ptr [r9 + 0x20]
00258E3C  41 D1 EA                        shr r10d, 1
00258E3F  D1 E8                           shr eax, 1
00258E41  41 83 E2 01                     and r10d, 1
00258E45  83 E0 01                        and eax, 1
00258E48  44 3B D0                        cmp r10d, eax
00258E4B  0F 83 DE 05 00 00               jae 0x14025942f
00258E51  45 33 DB                        xor r11d, r11d
00258E54  45 84 C0                        test r8b, r8b
00258E57  0F 84 2F 06 00 00               je 0x14025948c
00258E5D  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
00258E62  4B 8D 0C 9B                     lea rcx, [r11 + r11*4]
00258E66  4C 8D 0C CD 00 00 00 00         lea r9, [rcx*8]
00258E6E  4D 03 CD                        add r9, r13
00258E71  49 8B 49 28                     mov rcx, qword ptr [r9 + 0x28]
00258E75  4D 8B 71 10                     mov r14, qword ptr [r9 + 0x10]
00258E79  48 8D 41 FF                     lea rax, [rcx - 1]
00258E7D  4C 3B F3                        cmp r14, rbx
00258E80  0F 84 60 06 00 00               je 0x1402594e6
00258E86  49 8B 7E 18                     mov rdi, qword ptr [r14 + 0x18]
00258E8A  48 83 F8 FC                     cmp rax, -4
00258E8E  0F 86 4F 08 00 00               jbe 0x1402596e3
00258E94  41 0F B6 49 30                  movzx ecx, byte ptr [r9 + 0x30]
00258E99  80 C9 01                        or cl, 1
00258E9C  49 89 79 20                     mov qword ptr [r9 + 0x20], rdi
00258EA0  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
00258EA4  80 E1 FD                        and cl, 0xfd
00258EA7  8B 47 78                        mov eax, dword ptr [rdi + 0x78]
00258EAA  D1 E8                           shr eax, 1
00258EAC  24 01                           and al, 1
00258EAE  02 C0                           add al, al
00258EB0  32 C1                           xor al, cl
00258EB2  48 8B CF                        mov rcx, rdi
00258EB5  24 C7                           and al, 0xc7
00258EB7  0C 04                           or al, 4
00258EB9  41 88 41 30                     mov byte ptr [r9 + 0x30], al
00258EBD  41 80 61 31 FE                  and byte ptr [r9 + 0x31], 0xfe
00258EC2  49 89 79 28                     mov qword ptr [r9 + 0x28], rdi
00258EC6  E8 65 A3 0F 00                  call 0x140353230
00258ECB  84 C0                           test al, al
00258ECD  75 0A                           jne 0x140258ed9
00258ECF  41 8B 46 24                     mov eax, dword ptr [r14 + 0x24]
00258ED3  89 87 18 02 00 00               mov dword ptr [rdi + 0x218], eax
00258ED9  41 0F B6 45 00                  movzx eax, byte ptr [r13]
00258EDE  41 FF C3                        inc r11d
00258EE1  44 3B D8                        cmp r11d, eax
00258EE4  0F 82 78 FF FF FF               jb 0x140258e62
00258EEA  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
00258EEF  45 33 F6                        xor r14d, r14d
00258EF2  45 89 55 04                     mov dword ptr [r13 + 4], r10d
00258EF6  E9 E5 F7 FF FF                  jmp 0x1402586e0
00258EFB  49 8B 91 C8 02 00 00            mov rdx, qword ptr [r9 + 0x2c8]
00258F02  49 8B 81 D0 02 00 00            mov rax, qword ptr [r9 + 0x2d0]
00258F09  48 F7 D2                        not rdx
00258F0C  F0 48 21 90 88 01 00 00         lock and qword ptr [rax + 0x188], rdx
00258F14  E9 CE FE FF FF                  jmp 0x140258de7
00258F19  48 89 08                        mov qword ptr [rax], rcx
00258F1C  48 89 41 08                     mov qword ptr [rcx + 8], rax
00258F20  48 3B C1                        cmp rax, rcx
00258F23  0F 85 B3 FE FF FF               jne 0x140258ddc
00258F29  41 8B 49 08                     mov ecx, dword ptr [r9 + 8]
00258F2D  41 0F B6 C7                     movzx eax, r15b
00258F31  0F BB C1                        btc ecx, eax
00258F34  41 89 49 08                     mov dword ptr [r9 + 8], ecx
00258F38  E9 9F FE FF FF                  jmp 0x140258ddc
00258F3D  4D 8B E6                        mov r12, r14
00258F40  E9 F5 F9 FF FF                  jmp 0x14025893a
00258F45  41 0F B6 C3                     movzx eax, r11b
00258F49  48 05 44 08 00 00               add rax, 0x844
00258F4F  48 C1 E0 04                     shl rax, 4
00258F53  49 03 C2                        add rax, r10
00258F56  E9 CA F8 FF FF                  jmp 0x140258825
00258F5B  48 8B 46 68                     mov rax, qword ptr [rsi + 0x68]
00258F5F  48 85 C0                        test rax, rax
00258F62  0F 84 DA FC FF FF               je 0x140258c42
00258F68  41 8B 95 D8 00 00 00            mov edx, dword ptr [r13 + 0xd8]
00258F6F  48 8B CE                        mov rcx, rsi
00258F72  48 03 D0                        add rdx, rax
00258F75  E8 86 22 0B 00                  call 0x14030b200
00258F7A  84 C0                           test al, al
00258F7C  0F 84 C0 FC FF FF               je 0x140258c42
00258F82  48 8B CA                        mov rcx, rdx
00258F85  E8 16 98 FA FF                  call 0x1402027a0
00258F8A  84 C0                           test al, al
00258F8C  0F 84 B0 FC FF FF               je 0x140258c42
00258F92  48 8B CE                        mov rcx, rsi
00258F95  E8 76 D3 0F 00                  call 0x140356310
00258F9A  84 C0                           test al, al
00258F9C  0F 85 A0 FC FF FF               jne 0x140258c42
00258FA2  E9 CD FC FF FF                  jmp 0x140258c74
00258FA7  0F B6 4D AB                     movzx ecx, byte ptr [rbp - 0x55]
00258FAB  8D 41 FF                        lea eax, [rcx - 1]
00258FAE  85 C1                           test ecx, eax
00258FB0  74 08                           je 0x140258fba
00258FB2  45 0F B3 BE DC 83 00 00         btr dword ptr [r14 + 0x83dc], r15d
00258FBA  F7 46 78 00 00 40 00            test dword ptr [rsi + 0x78], 0x400000
00258FC1  0F 85 07 05 00 00               jne 0x1402594ce
00258FC7  48 8B 0F                        mov rcx, qword ptr [rdi]
00258FCA  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00258FCE  48 39 79 08                     cmp qword ptr [rcx + 8], rdi
00258FD2  0F 85 FD FD FF FF               jne 0x140258dd5
00258FD8  48 39 38                        cmp qword ptr [rax], rdi
00258FDB  0F 85 F4 FD FF FF               jne 0x140258dd5
00258FE1  48 89 08                        mov qword ptr [rax], rcx
00258FE4  48 89 41 08                     mov qword ptr [rcx + 8], rax
00258FE8  48 3B C1                        cmp rax, rcx
00258FEB  75 15                           jne 0x140259002
00258FED  41 8B 8E D8 83 00 00            mov ecx, dword ptr [r14 + 0x83d8]
00258FF4  41 0F B6 C7                     movzx eax, r15b
00258FF8  0F BB C1                        btc ecx, eax
00258FFB  41 89 8E D8 83 00 00            mov dword ptr [r14 + 0x83d8], ecx
00259002  41 83 86 74 86 00 00 FF         add dword ptr [r14 + 0x8674], -1
0025900A  0F 84 0D 02 00 00               je 0x14025921d
00259010  8B 86 F8 06 00 00               mov eax, dword ptr [rsi + 0x6f8]
00259016  49 29 86 78 86 00 00            sub qword ptr [r14 + 0x8678], rax
0025901D  49 8B 8E 48 8E 00 00            mov rcx, qword ptr [r14 + 0x8e48]
00259024  E9 CB FD FF FF                  jmp 0x140258df4
00259029  48 83 C0 A8                     add rax, -0x58
0025902D  44 39 48 7C                     cmp dword ptr [rax + 0x7c], r9d
00259031  0F 87 42 F8 FF FF               ja 0x140258879
00259037  E9 40 F8 FF FF                  jmp 0x14025887c
0025903C  4D 85 DB                        test r11, r11
0025903F  0F 85 86 02 00 00               jne 0x1402592cb
00259045  0F B6 DA                        movzx ebx, dl
00259048  4D 8B D9                        mov r11, r9
0025904B  E9 68 F8 FF FF                  jmp 0x1402588b8
00259050  41 0F B7 4B 78                  movzx ecx, word ptr [r11 + 0x78]
00259055  0F B6 C3                        movzx eax, bl
00259058  88 5D AA                        mov byte ptr [rbp - 0x56], bl
0025905B  4C 89 5D B8                     mov qword ptr [rbp - 0x48], r11
0025905F  4C 89 5D B0                     mov qword ptr [rbp - 0x50], r11
00259063  48 8D 14 40                     lea rdx, [rax + rax*2]
00259067  89 4D A4                        mov dword ptr [rbp - 0x5c], ecx
0025906A  48 03 D2                        add rdx, rdx
0025906D  8B 44 D5 F0                     mov eax, dword ptr [rbp + rdx*8 - 0x10]
00259071  41 39 43 7C                     cmp dword ptr [r11 + 0x7c], eax
00259075  75 0B                           jne 0x140259082
00259077  8B 44 D5 F4                     mov eax, dword ptr [rbp + rdx*8 - 0xc]
0025907B  23 C1                           and eax, ecx
0025907D  8B C8                           mov ecx, eax
0025907F  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
00259082  85 C9                           test ecx, ecx
00259084  0F 84 BF 01 00 00               je 0x140259249
0025908A  0F BD C1                        bsr eax, ecx
0025908D  0F B6 C8                        movzx ecx, al
00259090  48 83 C1 09                     add rcx, 9
00259094  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
00259098  48 C1 E1 04                     shl rcx, 4
0025909C  49 03 CB                        add rcx, r11
0025909F  88 45 A8                        mov byte ptr [rbp - 0x58], al
002590A2  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
002590A6  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
002590AA  E9 33 F8 FF FF                  jmp 0x1402588e2
002590AF  48 8B CE                        mov rcx, rsi
002590B2  E8 C9 EA 27 00                  call 0x1404d7b80
002590B7  84 C0                           test al, al
002590B9  0F 85 C4 FA FF FF               jne 0x140258b83
002590BF  E9 B0 FB FF FF                  jmp 0x140258c74
002590C4  4C 3B EB                        cmp r13, rbx
002590C7  0F 85 BF FA FF FF               jne 0x140258b8c
002590CD  E9 70 FB FF FF                  jmp 0x140258c42
002590D2  8B 46 74                        mov eax, dword ptr [rsi + 0x74]
002590D5  A8 08                           test al, 8
002590D7  0F 85 74 F8 FF FF               jne 0x140258951
002590DD  0F B6 45 AA                     movzx eax, byte ptr [rbp - 0x56]
002590E1  44 0F B6 75 A8                  movzx r14d, byte ptr [rbp - 0x58]
002590E6  48 8D 0C 40                     lea rcx, [rax + rax*2]
002590EA  48 03 C9                        add rcx, rcx
002590ED  80 7D AD 02                     cmp byte ptr [rbp - 0x53], 2
002590F1  48 8B 5C CD D0                  mov rbx, qword ptr [rbp + rcx*8 - 0x30]
002590F6  0F 84 F4 02 00 00               je 0x1402593f0
002590FC  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00259100  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00259104  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
00259108  0F B6 4D AC                     movzx ecx, byte ptr [rbp - 0x54]
0025910C  85 C9                           test ecx, ecx
0025910E  0F 84 3A 02 00 00               je 0x14025934e
00259114  83 F9 01                        cmp ecx, 1
00259117  75 70                           jne 0x140259189
00259119  0F B6 4D AB                     movzx ecx, byte ptr [rbp - 0x55]
0025911D  8D 41 FF                        lea eax, [rcx - 1]
00259120  85 C1                           test ecx, eax
00259122  74 08                           je 0x14025912c
00259124  44 0F AB B3 DC 83 00 00         bts dword ptr [rbx + 0x83dc], r14d
0025912C  F7 46 78 00 00 40 00            test dword ptr [rsi + 0x78], 0x400000
00259133  4C 8B 8B 48 8E 00 00            mov r9, qword ptr [rbx + 0x8e48]
0025913A  0F 85 0D 05 00 00               jne 0x14025964d
00259140  48 8B 0F                        mov rcx, qword ptr [rdi]
00259143  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00259147  48 39 79 08                     cmp qword ptr [rcx + 8], rdi
0025914B  0F 85 84 FC FF FF               jne 0x140258dd5
00259151  48 39 38                        cmp qword ptr [rax], rdi
00259154  0F 85 7B FC FF FF               jne 0x140258dd5
0025915A  48 89 08                        mov qword ptr [rax], rcx
0025915D  48 89 41 08                     mov qword ptr [rcx + 8], rax
00259161  48 3B C1                        cmp rax, rcx
00259164  74 79                           je 0x1402591df
00259166  41 83 41 0C FF                  add dword ptr [r9 + 0xc], -1
0025916B  0F 84 8E 00 00 00               je 0x1402591ff
00259171  8B 86 F8 06 00 00               mov eax, dword ptr [rsi + 0x6f8]
00259177  45 33 C0                        xor r8d, r8d
0025917A  49 29 41 10                     sub qword ptr [r9 + 0x10], rax
0025917E  48 8B D6                        mov rdx, rsi
00259181  49 8B C9                        mov rcx, r9
00259184  E8 C7 88 FA FF                  call 0x140201a50
00259189  0F B6 86 84 01 00 00            movzx eax, byte ptr [rsi + 0x184]
00259190  3C 01                           cmp al, 1
00259192  0F 84 46 01 00 00               je 0x1402592de
00259198  3C 05                           cmp al, 5
0025919A  75 22                           jne 0x1402591be
0025919C  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
002591A6  8B 08                           mov ecx, dword ptr [rax]
002591A8  2B 8E B4 01 00 00               sub ecx, dword ptr [rsi + 0x1b4]
002591AE  80 BE 87 01 00 00 00            cmp byte ptr [rsi + 0x187], 0
002591B5  74 1F                           je 0x1402591d6
002591B7  48 01 8E E8 03 00 00            add qword ptr [rsi + 0x3e8], rcx
002591BE  C6 86 84 01 00 00 07            mov byte ptr [rsi + 0x184], 7
002591C5  45 33 F6                        xor r14d, r14d
002591C8  49 8B 07                        mov rax, qword ptr [r15]
002591CB  48 89 07                        mov qword ptr [rdi], rax
002591CE  49 89 3F                        mov qword ptr [r15], rdi
002591D1  E9 27 F5 FF FF                  jmp 0x1402586fd
002591D6  48 01 8E E0 03 00 00            add qword ptr [rsi + 0x3e0], rcx
002591DD  EB DF                           jmp 0x1402591be
002591DF  41 8B 49 08                     mov ecx, dword ptr [r9 + 8]
002591E3  41 0F B6 C6                     movzx eax, r14b
002591E7  0F BB C1                        btc ecx, eax
002591EA  41 89 49 08                     mov dword ptr [r9 + 8], ecx
002591EE  E9 73 FF FF FF                  jmp 0x140259166
002591F3  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
002591F7  4D 8B E6                        mov r12, r14
002591FA  E9 3E F7 FF FF                  jmp 0x14025893d
002591FF  49 8B 91 C8 02 00 00            mov rdx, qword ptr [r9 + 0x2c8]
00259206  49 8B 81 D0 02 00 00            mov rax, qword ptr [r9 + 0x2d0]
0025920D  48 F7 D2                        not rdx
00259210  F0 48 21 90 88 01 00 00         lock and qword ptr [rax + 0x188], rdx
00259218  E9 54 FF FF FF                  jmp 0x140259171
0025921D  49 83 BE 30 84 00 00 00         cmp qword ptr [r14 + 0x8430], 0
00259225  0F 85 E5 FD FF FF               jne 0x140259010
0025922B  49 8B 8E C8 00 00 00            mov rcx, qword ptr [r14 + 0xc8]
00259232  49 8B 86 C0 00 00 00            mov rax, qword ptr [r14 + 0xc0]
00259239  48 F7 D1                        not rcx
0025923C  F0 48 21 88 80 01 00 00         lock and qword ptr [rax + 0x180], rcx
00259244  E9 C7 FD FF FF                  jmp 0x140259010
00259249  48 8D 4D A0                     lea rcx, [rbp - 0x60]
0025924D  E8 2A 90 FA FF                  call 0x14020227c
00259252  85 C0                           test eax, eax
00259254  0F 89 2A 01 00 00               jns 0x140259384
0025925A  44 0F B6 55 A9                  movzx r10d, byte ptr [rbp - 0x57]
0025925F  44 8B 45 A0                     mov r8d, dword ptr [rbp - 0x60]
00259263  E9 6D F6 FF FF                  jmp 0x1402588d5
00259268  49 8B 84 24 C8 02 00 00         mov rax, qword ptr [r12 + 0x2c8]
00259270  49 23 C0                        and rax, r8
00259273  48 85 C1                        test rcx, rax
00259276  0F 85 F8 F9 FF FF               jne 0x140258c74
0025927C  E9 B6 F9 FF FF                  jmp 0x140258c37
00259281  41 0F A3 9A DC 83 00 00         bt dword ptr [r10 + 0x83dc], ebx
00259289  0F 93 C0                        setae al
0025928C  E9 72 F5 FF FF                  jmp 0x140258803
00259291  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00259295  4C 8B 65 B0                     mov r12, qword ptr [rbp - 0x50]
00259299  48 39 07                        cmp qword ptr [rdi], rax
0025929C  0F 85 EE 00 00 00               jne 0x140259390
002592A2  48 39 47 08                     cmp qword ptr [rdi + 8], rax
002592A6  0F 85 E4 00 00 00               jne 0x140259390
002592AC  48 8D 4D A0                     lea rcx, [rbp - 0x60]
002592B0  E8 9B 89 FA FF                  call 0x140201c50
002592B5  45 8B CF                        mov r9d, r15d
002592B8  4C 8B C6                        mov r8, rsi
002592BB  49 8B D4                        mov rdx, r12
002592BE  49 8B CE                        mov rcx, r14
002592C1  E8 9E 88 FA FF                  call 0x140201b64
002592C6  E9 34 FB FF FF                  jmp 0x140258dff
002592CB  41 8B 41 7C                     mov eax, dword ptr [r9 + 0x7c]
002592CF  41 39 43 7C                     cmp dword ptr [r11 + 0x7c], eax
002592D3  0F 83 DF F5 FF FF               jae 0x1402588b8
002592D9  E9 67 FD FF FF                  jmp 0x140259045
002592DE  83 4E 74 02                     or dword ptr [rsi + 0x74], 2
002592E2  E9 D7 FE FF FF                  jmp 0x1402591be
002592E7  8B FE                           mov edi, esi
002592E9  48 83 C7 0B                     add rdi, 0xb
002592ED  48 C1 E7 04                     shl rdi, 4
002592F1  49 03 FD                        add rdi, r13
002592F4  F7 05 3A D8 D6 00 00 00 20 00   test dword ptr [rip + 0xd6d83a], 0x200000
002592FE  74 47                           je 0x140259347
00259300  0F 0D 0F                        prefetchw byte ptr [rdi]
00259303  48 8B 07                        mov rax, qword ptr [rdi]
00259306  48 85 C0                        test rax, rax
00259309  75 16                           jne 0x140259321
0025930B  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0025930F  48 8B C7                        mov rax, rdi
00259312  F0 4C 0F B1 31                  lock cmpxchg qword ptr [rcx], r14
00259317  74 24                           je 0x14025933d
00259319  48 8B CF                        mov rcx, rdi
0025931C  E8 7F E7 FB FF                  call 0x140217aa0
00259321  48 8D 48 08                     lea rcx, [rax + 8]
00259325  4C 89 37                        mov qword ptr [rdi], r14
00259328  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
0025932C  48 8B C2                        mov rax, rdx
0025932F  48 87 01                        xchg qword ptr [rcx], rax
00259332  32 C2                           xor al, dl
00259334  A8 04                           test al, 4
00259336  74 05                           je 0x14025933d
00259338  E8 E3 E8 FB FF                  call 0x140217c20
0025933D  FF C6                           inc esi
0025933F  4C 8B C3                        mov r8, rbx
00259342  E9 89 F9 FF FF                  jmp 0x140258cd0
00259347  F0 48 83 23 00                  lock and qword ptr [rbx], 0
0025934C  EB EF                           jmp 0x14025933d
0025934E  0F B6 4D AB                     movzx ecx, byte ptr [rbp - 0x55]
00259352  8D 41 FF                        lea eax, [rcx - 1]
00259355  85 C1                           test ecx, eax
00259357  74 08                           je 0x140259361
00259359  44 0F B3 B3 DC 83 00 00         btr dword ptr [rbx + 0x83dc], r14d
00259361  45 8B C6                        mov r8d, r14d
00259364  48 8B D7                        mov rdx, rdi
00259367  48 8B CB                        mov rcx, rbx
0025936A  E8 59 83 FA FF                  call 0x1402016c8
0025936F  E9 15 FE FF FF                  jmp 0x140259189
00259374  41 0F A3 9A DC 83 00 00         bt dword ptr [r10 + 0x83dc], ebx
0025937C  0F 93 C0                        setae al
0025937F  E9 7F F4 FF FF                  jmp 0x140258803
00259384  4C 8B 5D B0                     mov r11, qword ptr [rbp - 0x50]
00259388  8B 4D A4                        mov ecx, dword ptr [rbp - 0x5c]
0025938B  E9 FA FC FF FF                  jmp 0x14025908a
00259390  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00259394  4C 8B 40 08                     mov r8, qword ptr [rax + 8]
00259398  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
0025939C  E9 14 FF FF FF                  jmp 0x1402592b5
002593A1  41 0F B6 47 30                  movzx eax, byte ptr [r15 + 0x30]
002593A6  49 8B 57 20                     mov rdx, qword ptr [r15 + 0x20]
002593AA  A8 01                           test al, 1
002593AC  0F 85 93 F9 FF FF               jne 0x140258d45
002593B2  0F B6 8E C3 00 00 00            movzx ecx, byte ptr [rsi + 0xc3]
002593B9  3A 8A C3 00 00 00               cmp cl, byte ptr [rdx + 0xc3]
002593BF  0F 8F 80 F9 FF FF               jg 0x140258d45
002593C5  0F 85 6A F9 FF FF               jne 0x140258d35
002593CB  A8 18                           test al, 0x18
002593CD  0F 85 72 F9 FF FF               jne 0x140258d45
002593D3  E9 5D F9 FF FF                  jmp 0x140258d35
002593D8  48 8B 86 C8 03 00 00            mov rax, qword ptr [rsi + 0x3c8]
002593DF  F0 81 20 FF FF FB FF            lock and dword ptr [rax], 0xfffbffff
002593E6  44 0F B6 7D A8                  movzx r15d, byte ptr [rbp - 0x58]
002593EB  E9 CF F9 FF FF                  jmp 0x140258dbf
002593F0  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
002593F4  4C 8B 7D B0                     mov r15, qword ptr [rbp - 0x50]
002593F8  48 39 07                        cmp qword ptr [rdi], rax
002593FB  0F 85 3B 02 00 00               jne 0x14025963c
00259401  48 39 47 08                     cmp qword ptr [rdi + 8], rax
00259405  0F 85 31 02 00 00               jne 0x14025963c
0025940B  48 8D 4D A0                     lea rcx, [rbp - 0x60]
0025940F  E8 3C 88 FA FF                  call 0x140201c50
00259414  45 8B CE                        mov r9d, r14d
00259417  4C 8B C6                        mov r8, rsi
0025941A  49 8B D7                        mov rdx, r15
0025941D  48 8B CB                        mov rcx, rbx
00259420  E8 3F 87 FA FF                  call 0x140201b64
00259425  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
0025942A  E9 5A FD FF FF                  jmp 0x140259189
0025942F  45 85 D2                        test r10d, r10d
00259432  0F 85 06 01 00 00               jne 0x14025953e
00259438  49 8B 51 18                     mov rdx, qword ptr [r9 + 0x18]
0025943C  4D 8B 19                        mov r11, qword ptr [r9]
0025943F  48 8D 42 FF                     lea rax, [rdx - 1]
00259443  48 83 F8 FC                     cmp rax, -4
00259447  76 54                           jbe 0x14025949d
00259449  41 0F B6 49 20                  movzx ecx, byte ptr [r9 + 0x20]
0025944E  80 E1 FE                        and cl, 0xfe
00259451  49 89 71 10                     mov qword ptr [r9 + 0x10], rsi
00259455  41 88 49 20                     mov byte ptr [r9 + 0x20], cl
00259459  80 E1 FD                        and cl, 0xfd
0025945C  8B 46 78                        mov eax, dword ptr [rsi + 0x78]
0025945F  41 80 61 21 FE                  and byte ptr [r9 + 0x21], 0xfe
00259464  D1 E8                           shr eax, 1
00259466  24 01                           and al, 1
00259468  49 89 71 18                     mov qword ptr [r9 + 0x18], rsi
0025946C  02 C0                           add al, al
0025946E  32 C1                           xor al, cl
00259470  24 C7                           and al, 0xc7
00259472  0C 04                           or al, 4
00259474  41 88 41 20                     mov byte ptr [r9 + 0x20], al
00259478  48 8D 05 81 6A D7 00            lea rax, [rip + 0xd76a81]
0025947F  48 39 86 20 02 00 00            cmp qword ptr [rsi + 0x220], rax
00259486  0F 85 70 03 00 00               jne 0x1402597fc
0025948C  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
00259491  45 33 F6                        xor r14d, r14d
00259494  45 89 55 04                     mov dword ptr [r13 + 4], r10d
00259498  E9 43 F2 FF FF                  jmp 0x1402586e0
0025949D  48 8D 05 5C 6A D7 00            lea rax, [rip + 0xd76a5c]
002594A4  48 39 82 20 02 00 00            cmp qword ptr [rdx + 0x220], rax
002594AB  74 9C                           je 0x140259449
002594AD  41 F6 41 21 01                  test byte ptr [r9 + 0x21], 1
002594B2  74 04                           je 0x1402594b8
002594B4  83 4A 74 02                     or dword ptr [rdx + 0x74], 2
002594B8  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
002594BD  C6 82 35 02 00 00 01            mov byte ptr [rdx + 0x235], 1
002594C4  E8 47 7E FA FF                  call 0x140201310
002594C9  E9 7B FF FF FF                  jmp 0x140259449
002594CE  48 8B 86 C8 03 00 00            mov rax, qword ptr [rsi + 0x3c8]
002594D5  F0 81 20 FF FF FB FF            lock and dword ptr [rax], 0xfffbffff
002594DC  44 0F B6 7D A8                  movzx r15d, byte ptr [rbp - 0x58]
002594E1  E9 E1 FA FF FF                  jmp 0x140258fc7
002594E6  48 83 F8 FC                     cmp rax, -4
002594EA  0F 86 2C 02 00 00               jbe 0x14025971c
002594F0  41 0F B6 49 30                  movzx ecx, byte ptr [r9 + 0x30]
002594F5  80 E1 FE                        and cl, 0xfe
002594F8  49 89 71 20                     mov qword ptr [r9 + 0x20], rsi
002594FC  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
00259500  80 E1 FD                        and cl, 0xfd
00259503  8B 46 78                        mov eax, dword ptr [rsi + 0x78]
00259506  41 80 61 31 FE                  and byte ptr [r9 + 0x31], 0xfe
0025950B  D1 E8                           shr eax, 1
0025950D  24 01                           and al, 1
0025950F  49 89 71 28                     mov qword ptr [r9 + 0x28], rsi
00259513  02 C0                           add al, al
00259515  32 C1                           xor al, cl
00259517  48 8B CE                        mov rcx, rsi
0025951A  24 C7                           and al, 0xc7
0025951C  0C 04                           or al, 4
0025951E  41 88 41 30                     mov byte ptr [r9 + 0x30], al
00259522  E8 09 9D 0F 00                  call 0x140353230
00259527  84 C0                           test al, al
00259529  0F 85 AA F9 FF FF               jne 0x140258ed9
0025952F  41 8B 46 24                     mov eax, dword ptr [r14 + 0x24]
00259533  89 86 18 02 00 00               mov dword ptr [rsi + 0x218], eax
00259539  E9 9B F9 FF FF                  jmp 0x140258ed9
0025953E  45 33 DB                        xor r11d, r11d
00259541  45 84 C0                        test r8b, r8b
00259544  0F 84 42 FF FF FF               je 0x14025948c
0025954A  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
0025954F  4B 8D 0C 9B                     lea rcx, [r11 + r11*4]
00259553  4C 8D 0C CD 00 00 00 00         lea r9, [rcx*8]
0025955B  4D 03 CD                        add r9, r13
0025955E  49 8B 49 28                     mov rcx, qword ptr [r9 + 0x28]
00259562  49 8B 79 10                     mov rdi, qword ptr [r9 + 0x10]
00259566  48 8D 41 FF                     lea rax, [rcx - 1]
0025956A  48 3B FB                        cmp rdi, rbx
0025956D  75 60                           jne 0x1402595cf
0025956F  48 83 F8 FC                     cmp rax, -4
00259573  0F 86 D2 01 00 00               jbe 0x14025974b
00259579  41 0F B6 49 30                  movzx ecx, byte ptr [r9 + 0x30]
0025957E  80 E1 FE                        and cl, 0xfe
00259581  49 89 71 20                     mov qword ptr [r9 + 0x20], rsi
00259585  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
00259589  80 E1 FD                        and cl, 0xfd
0025958C  8B 46 78                        mov eax, dword ptr [rsi + 0x78]
0025958F  41 80 61 31 FE                  and byte ptr [r9 + 0x31], 0xfe
00259594  D1 E8                           shr eax, 1
00259596  24 01                           and al, 1
00259598  49 89 71 28                     mov qword ptr [r9 + 0x28], rsi
0025959C  02 C0                           add al, al
0025959E  32 C1                           xor al, cl
002595A0  48 8B CE                        mov rcx, rsi
002595A3  24 C7                           and al, 0xc7
002595A5  0C 04                           or al, 4
002595A7  41 88 41 30                     mov byte ptr [r9 + 0x30], al
002595AB  E8 80 9C 0F 00                  call 0x140353230
002595B0  84 C0                           test al, al
002595B2  75 09                           jne 0x1402595bd
002595B4  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
002595B7  89 86 18 02 00 00               mov dword ptr [rsi + 0x218], eax
002595BD  41 0F B6 45 00                  movzx eax, byte ptr [r13]
002595C2  41 FF C3                        inc r11d
002595C5  44 3B D8                        cmp r11d, eax
002595C8  72 85                           jb 0x14025954f
002595CA  E9 BD FE FF FF                  jmp 0x14025948c
002595CF  4C 8B B7 80 8E 00 00            mov r14, qword ptr [rdi + 0x8e80]
002595D6  48 83 F8 FC                     cmp rax, -4
002595DA  0F 86 9A 01 00 00               jbe 0x14025977a
002595E0  41 0F B6 41 30                  movzx eax, byte ptr [r9 + 0x30]
002595E5  24 FE                           and al, 0xfe
002595E7  49 89 71 20                     mov qword ptr [r9 + 0x20], rsi
002595EB  41 88 41 30                     mov byte ptr [r9 + 0x30], al
002595EF  24 FD                           and al, 0xfd
002595F1  8B 4E 78                        mov ecx, dword ptr [rsi + 0x78]
002595F4  D1 E9                           shr ecx, 1
002595F6  80 E1 01                        and cl, 1
002595F9  02 C9                           add cl, cl
002595FB  32 C8                           xor cl, al
002595FD  80 E1 E7                        and cl, 0xe7
00259600  80 C9 04                        or cl, 4
00259603  0F B6 C1                        movzx eax, cl
00259606  80 C9 20                        or cl, 0x20
00259609  24 DF                           and al, 0xdf
0025960B  0F B6 C9                        movzx ecx, cl
0025960E  0F B6 C0                        movzx eax, al
00259611  49 3B F6                        cmp rsi, r14
00259614  0F 44 C8                        cmove ecx, eax
00259617  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
0025961B  49 8B CE                        mov rcx, r14
0025961E  41 80 61 31 FE                  and byte ptr [r9 + 0x31], 0xfe
00259623  4D 89 71 28                     mov qword ptr [r9 + 0x28], r14
00259627  E8 04 9C 0F 00                  call 0x140353230
0025962C  84 C0                           test al, al
0025962E  75 8D                           jne 0x1402595bd
00259630  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00259633  41 89 86 18 02 00 00            mov dword ptr [r14 + 0x218], eax
0025963A  EB 81                           jmp 0x1402595bd
0025963C  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00259640  4C 8B 40 08                     mov r8, qword ptr [rax + 8]
00259644  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
00259648  E9 C7 FD FF FF                  jmp 0x140259414
0025964D  48 8B 86 C8 03 00 00            mov rax, qword ptr [rsi + 0x3c8]
00259654  F0 81 20 FF FF FB FF            lock and dword ptr [rax], 0xfffbffff
0025965B  44 0F B6 75 A8                  movzx r14d, byte ptr [rbp - 0x58]
00259660  E9 DB FA FF FF                  jmp 0x140259140
00259665  41 0F B6 45 00                  movzx eax, byte ptr [r13]
0025966A  44 3B F0                        cmp r14d, eax
0025966D  72 40                           jb 0x1402596af
0025966F  45 33 F6                        xor r14d, r14d
00259672  41 0F B6 45 00                  movzx eax, byte ptr [r13]
00259677  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
0025967C  44 3B F0                        cmp r14d, eax
0025967F  0F 83 0B F3 FF FF               jae 0x140258990
00259685  4B 8D 0C B6                     lea rcx, [r14 + r14*4]
00259689  4D 8B CC                        mov r9, r12
0025968C  4C 8D 3C CD 00 00 00 00         lea r15, [rcx*8]
00259694  4C 8B C3                        mov r8, rbx
00259697  49 8D 4F 10                     lea rcx, [r15 + 0x10]
0025969B  48 8B D6                        mov rdx, rsi
0025969E  49 03 CD                        add rcx, r13
002596A1  E8 6A E6 FF FF                  call 0x140257d10
002596A6  84 C0                           test al, al
002596A8  75 68                           jne 0x140259712
002596AA  41 FF C6                        inc r14d
002596AD  EB C3                           jmp 0x140259672
002596AF  41 8B C6                        mov eax, r14d
002596B2  45 33 C9                        xor r9d, r9d
002596B5  45 33 C0                        xor r8d, r8d
002596B8  48 8B D6                        mov rdx, rsi
002596BB  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
002596C3  48 03 C8                        add rcx, rax
002596C6  48 8D 0C CD 00 00 00 00         lea rcx, [rcx*8]
002596CE  49 03 CD                        add rcx, r13
002596D1  E8 FA EA FF FF                  call 0x1402581d0
002596D6  84 C0                           test al, al
002596D8  0F 84 B2 F2 FF FF               je 0x140258990
002596DE  41 FF C6                        inc r14d
002596E1  EB 82                           jmp 0x140259665
002596E3  E8 48 9B 0F 00                  call 0x140353230
002596E8  84 C0                           test al, al
002596EA  0F 85 A4 F7 FF FF               jne 0x140258e94
002596F0  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
002596F5  74 04                           je 0x1402596fb
002596F7  83 49 74 02                     or dword ptr [rcx + 0x74], 2
002596FB  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
00259702  48 8B D1                        mov rdx, rcx
00259705  49 8B CF                        mov rcx, r15
00259708  E8 03 7C FA FF                  call 0x140201310
0025970D  E9 82 F7 FF FF                  jmp 0x140258e94
00259712  4B 8B 5C 2F 10                  mov rbx, qword ptr [r15 + r13 + 0x10]
00259717  E9 32 F6 FF FF                  jmp 0x140258d4e
0025971C  E8 0F 9B 0F 00                  call 0x140353230
00259721  84 C0                           test al, al
00259723  0F 85 C7 FD FF FF               jne 0x1402594f0
00259729  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
0025972E  74 04                           je 0x140259734
00259730  83 49 74 02                     or dword ptr [rcx + 0x74], 2
00259734  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
0025973B  48 8B D1                        mov rdx, rcx
0025973E  49 8B CF                        mov rcx, r15
00259741  E8 CA 7B FA FF                  call 0x140201310
00259746  E9 A5 FD FF FF                  jmp 0x1402594f0
0025974B  E8 E0 9A 0F 00                  call 0x140353230
00259750  84 C0                           test al, al
00259752  0F 85 21 FE FF FF               jne 0x140259579
00259758  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
0025975D  74 04                           je 0x140259763
0025975F  83 49 74 02                     or dword ptr [rcx + 0x74], 2
00259763  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
0025976A  48 8B D1                        mov rdx, rcx
0025976D  49 8B CF                        mov rcx, r15
00259770  E8 9B 7B FA FF                  call 0x140201310
00259775  E9 FF FD FF FF                  jmp 0x140259579
0025977A  E8 B1 9A 0F 00                  call 0x140353230
0025977F  84 C0                           test al, al
00259781  0F 85 59 FE FF FF               jne 0x1402595e0
00259787  41 F6 41 31 01                  test byte ptr [r9 + 0x31], 1
0025978C  74 04                           je 0x140259792
0025978E  83 49 74 02                     or dword ptr [rcx + 0x74], 2
00259792  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
00259799  48 8B D1                        mov rdx, rcx
0025979C  49 8B CF                        mov rcx, r15
0025979F  E8 6C 7B FA FF                  call 0x140201310
002597A4  E9 37 FE FF FF                  jmp 0x1402595e0
002597A9  48 8B D6                        mov rdx, rsi
002597AC  48 8D 4D A0                     lea rcx, [rbp - 0x60]
002597B0  E8 DB 7F FA FF                  call 0x140201790
002597B5  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
002597B8  45 33 C9                        xor r9d, r9d
002597BB  4C 8B C6                        mov r8, rsi
002597BE  89 86 18 02 00 00               mov dword ptr [rsi + 0x218], eax
002597C4  49 8B D6                        mov rdx, r14
002597C7  48 8B CB                        mov rcx, rbx
002597CA  E8 0D 79 FA FF                  call 0x1402010dc
002597CF  F7 05 3B D3 D6 00 00 08 00 00   test dword ptr [rip + 0xd6d33b], 0x800
002597D9  41 BE 00 00 00 00               mov r14d, 0
002597DF  0F 84 18 EF FF FF               je 0x1402586fd
002597E5  8B 53 24                        mov edx, dword ptr [rbx + 0x24]
002597E8  45 8D 46 02                     lea r8d, [r14 + 2]
002597EC  45 33 C9                        xor r9d, r9d
002597EF  48 8B CE                        mov rcx, rsi
002597F2  E8 4D 9C FC FF                  call 0x140223444
002597F7  E9 01 EF FF FF                  jmp 0x1402586fd
002597FC  41 8B 43 24                     mov eax, dword ptr [r11 + 0x24]
00259800  89 86 18 02 00 00               mov dword ptr [rsi + 0x218], eax
00259806  E9 81 FC FF FF                  jmp 0x14025948c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSearchForNewThreadsForRescheduleContext(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int8 v_stack_m12B;
    unsigned __int8 v_stack_m12C;
    unsigned __int8 v_stack_m12D;
    unsigned __int8 v_stack_m12E;
    unsigned __int8 v_stack_m12F;
    unsigned __int8 v_stack_m130;
    unsigned int v_stack_m134;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m190;
    unsigned int v_stack_m194;
    unsigned int v_stack_m198;
    unsigned int v_stack_m19C;
    unsigned int v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mDC;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p4C;
    unsigned __int64 v_stack_p58;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (416);
    result = (*(unsigned __int64 *)(v_rip + 12263674)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r14 = 0;
    v_stack_m1A8 = a2;
    v_stack_m180 = a1;
loc_00258669:
    if ((unsigned __int8)(*(unsigned __int8 *)(a1)) == 0) goto loc_002586E0;
loc_0025867B:
    if ((*(unsigned __int64 *)(a1 + 24)) <= 0) goto loc_00258690;
    if (0 == 0) goto loc_0025868D;
    v_rbx = 0;
    if ((*(unsigned __int64 *)(a1 + 24)) < 0) {
        v_rbx = *(unsigned __int64 *)(a1 + 24);
    }
    a1 = (a1 + 24) + (40);
    a2 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1)))) - (1);
    if (condition_is_not_equal) goto loc_0025867B;
    if (v_rbx == 0) goto loc_002586E0;
    a1 = (0) + (11);
    a1 = (a1) << (4);
    a1 = (a1) + (a1);
    if (((*(unsigned int *)(v_rip + 14083202)) & (0x200000ULL)) == 0) goto loc_002589AE;
    *(unsigned __int64 *)(a1 + 8) = v_rbx;
    *(unsigned __int64 *)(a1) = 0;
    if (a1 != 0) goto loc_00258CA9;
loc_002586D3:
    v_rdi = (unsigned int)((0) + 1);
    goto loc_00258669;
loc_002586E0:
    a2 = 0;
    result = memset(v_stack_m138, a2, 240, a4);
    result = KiStartReadyQueueEnumeratorForRescheduleContext(v_stack_m138, a1, 240, a4);
loc_002586FD:
    if (((unsigned __int8)(v_stack_m12B)) == 4) goto loc_00258CC9;
    if ((unsigned __int8)(v_stack_m12B) != 0) goto loc_002588F0;
loc_00258720:
    if (1 == 2) goto loc_00258836;
    a1 = (unsigned int)((1) - (1));
    if (condition_is_not_equal) goto loc_002589C4;
    v_stack_m134 = 0;
    if ((unsigned int)((unsigned int)(v_stack_m138)) != 0) goto loc_00258A9F;
loc_00258745:
    result = (unsigned int)((0) & (0xFFFFFFFEULL));
    v_stack_m134 = (unsigned int)(result);
    if (condition_is_equal) goto loc_002588D5;
    v_stack_m12E = (unsigned __int8)(v_stack_m12F);
    v_stack_m130 = (unsigned __int8)(v_r11);
    v_stack_m194 = (unsigned int)(v_r11);
    a1 = ((unsigned __int8)(v_stack_m12F) + (unsigned __int8)(v_stack_m12F) * 2) + ((unsigned __int8)(v_stack_m12F) + (unsigned __int8)(v_stack_m12F) * 2);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mD8 + a1 * 8 - 8))) | (*(unsigned int *)(v_stack_mD8 + a1 * 8 - 4)));
    a4 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned __int8)(v_r11))))));
    if ((((unsigned int)(a2)) & ((unsigned int)(a4))) != 0) goto loc_002587B8;
loc_00258789:
    v_r10 = (unsigned __int8)((v_stack_m12F) + 1);
    v_stack_m12E = (unsigned __int8)(v_r10);
    if (((unsigned int)((unsigned __int8)(v_r10))) >= ((unsigned int)((unsigned int)(v_stack_m138)))) {
        v_r10 = 0;
        v_stack_m12E = 0;
    }
    a1 = (0 + 0 * 2) + (0 + 0 * 2);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mD8 + a1 * 8 - 8))) | (*(unsigned int *)(v_stack_mD8 + a1 * 8 - 4)));
    if ((((unsigned int)(a2)) & ((unsigned int)(a4))) == 0) goto loc_00258789;
loc_002587B8:
    a1 = (0 + 0 * 2) << (4);
    a2 = (v_stack_m108) + (a1);
    a1 = 0;
    v_stack_m12D = 0;
    if (((*(unsigned int *)(a2 + 40)) & ((unsigned int)(a4))) != 0) {
        a1 = 1;
        v_stack_m12D = (unsigned __int8)(a1);
    }
    if (((*(unsigned int *)(a2 + 44)) & ((unsigned int)(a4))) != 0) {
        a1 = (unsigned __int8)((a1) | (2));
        v_stack_m12D = (unsigned __int8)(a1);
    }
    if ((((unsigned int)((unsigned __int8)(a1))) & ((unsigned int)((unsigned __int8)(a1) - 1))) != 0) goto loc_00259281;
    v_stack_m190 = (unsigned int)((unsigned __int8)(a1) - 1);
loc_00258803:
    v_stack_m12C = (unsigned __int8)((unsigned __int8)(a1) - 1);
    if ((unsigned __int8)((unsigned __int8)(a1) - 1) == 0) goto loc_00258F45;
    if (((unsigned int)((unsigned __int8)((unsigned __int8)(a1) - 1))) != 1) goto loc_00258829;
    result = ((unsigned __int8)(v_r11)) + (4);
    result = (result) << (4);
    result = (result) + (*(unsigned __int64 *)(a2 + 8));
loc_00258825:
    v_stack_m118 = result;
loc_00258829:
    v_stack_m110 = v_stack_m118;
    goto loc_002588E2;
loc_00258836:
    a2 = 0;
    if ((unsigned int)(*(unsigned __int64 *)(a2 + 8)) == 0) goto loc_00258894;
loc_00258840:
    a1 = (0 + 0 * 2) + (0 + 0 * 2);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mD8 + a1 * 8 - 16))) == 0) goto loc_00258885;
    result = (*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 48)) + (0x8430ULL);
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 8))) & (1)) != 0) goto loc_00258998;
loc_00258870:
    if (*(unsigned __int64 *)(result + 8) != 0) goto loc_00259029;
loc_00258879:
loc_0025887C:
    *(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 32) = 0;
loc_00258885:
    a2 = (unsigned __int8)((a2) + 1);
    if (((unsigned int)((unsigned __int8)(a2))) < ((unsigned int)((unsigned int)(v_stack_m138)))) goto loc_00258840;
loc_00258894:
    v_rbx = 0;
loc_002588A0:
    a1 = ((unsigned __int8)((unsigned __int8)(v_stack_m12F)) + (unsigned __int8)((unsigned __int8)(v_stack_m12F)) * 2) + ((unsigned __int8)((unsigned __int8)(v_stack_m12F)) + (unsigned __int8)((unsigned __int8)(v_stack_m12F)) * 2);
    if (*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 32) != 0) goto loc_0025903C;
loc_002588B8:
    a2 = (unsigned __int8)(((unsigned __int8)(v_stack_m12F)) + 1);
    a2 = (unsigned __int8)(a2);
    if (((unsigned int)((unsigned __int8)(a2))) >= ((unsigned int)((unsigned int)(v_stack_m138)))) { a2 = 0; }
    if (((unsigned __int8)(a2)) != ((unsigned __int8)(v_stack_m12F))) goto loc_002588A0;
    if (0 != 0) goto loc_00259050;
loc_002588D5:
    v_rdi = (unsigned __int8)((1) + 1);
    if (((unsigned __int8)(v_rdi)) < 4) goto loc_00258720;
loc_002588E2:
    v_stack_m12B = (unsigned __int8)(v_rdi);
    if (((unsigned __int8)(v_rdi)) == 4) goto loc_00258CC9;
loc_002588F0:
    v_stack_m110 = *(unsigned __int64 *)(v_stack_m110);
    if ((*(unsigned __int64 *)(v_stack_m110)) == v_stack_m118) goto loc_00258CB8;
    a1 = (v_stack_m12E + v_stack_m12E * 2) + (v_stack_m12E + v_stack_m12E * 2);
    v_stack_m188 = *(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 48);
    if (v_stack_m12B == 2) goto loc_002591F3;
    if (v_stack_m12C != 1) goto loc_00258F3D;
loc_0025893A:
loc_0025893D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m110) - 216 + 568)) != (*(unsigned __int64 *)(v_rip + 14082740))) goto loc_002590D2;
loc_00258951:
    if (0 == 0) goto loc_00258AC2;
loc_0025895A:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m110) - 216 + 120))) >> (1));
    a1 = (unsigned int)((a1) & (1));
    if (((unsigned int)(a1)) > (*(unsigned int *)(a1 + 8))) goto loc_002586FD;
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))); }
    if ((unsigned int)(a1) != 0) goto loc_00259665;
loc_0025897D:
    if (0 < ((unsigned int)(*(unsigned __int8 *)(a1)))) goto loc_00258B59;
loc_00258990:
    v_r14 = 0;
    goto loc_002586FD;
loc_00258998:
    if (((unsigned int)(v_stack_m138)) == 1) goto loc_00258879;
    result = (*(unsigned __int8 *)(a1)) | (1);
    result = (result) ^ ((unsigned int)(v_stack_m138));
    goto loc_00258870;
loc_002589AE:
    v_stack_m1A0 = 0;
    if (condition_is_above_or_equal) goto loc_002586D3;
loc_002589C4:
    if (((unsigned int)(a1)) != 2) goto loc_002588D5;
    v_stack_m134 = 0;
    if ((unsigned int)((unsigned int)(v_stack_m138)) != 0) goto loc_00258C86;
loc_002589DC:
    result = (unsigned int)((0) & (1));
    v_stack_m134 = (unsigned int)(result);
    if (condition_is_equal) goto loc_002588D5;
    v_stack_m12E = (unsigned __int8)(v_stack_m12F);
    v_stack_m130 = 0;
    v_stack_m19C = 0;
    a1 = ((unsigned __int8)(v_stack_m12F) + (unsigned __int8)(v_stack_m12F) * 2) + ((unsigned __int8)(v_stack_m12F) + (unsigned __int8)(v_stack_m12F) * 2);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mD8 + a1 * 8 - 8))) | (*(unsigned int *)(v_stack_mD8 + a1 * 8 - 4)));
    a4 = (unsigned int)((1) << (0));
    if ((((unsigned int)(a2)) & ((unsigned int)(a4))) != 0) goto loc_00258A4F;
loc_00258A20:
    v_r10 = (unsigned __int8)((v_stack_m12F) + 1);
    v_stack_m12E = (unsigned __int8)(v_r10);
    if (((unsigned int)((unsigned __int8)(v_r10))) >= ((unsigned int)((unsigned int)(v_stack_m138)))) {
        v_r10 = 0;
        v_stack_m12E = 0;
    }
    a1 = (0 + 0 * 2) + (0 + 0 * 2);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mD8 + a1 * 8 - 8))) | (*(unsigned int *)(v_stack_mD8 + a1 * 8 - 4)));
    if ((((unsigned int)(a2)) & ((unsigned int)(a4))) == 0) goto loc_00258A20;
loc_00258A4F:
    a1 = (0 + 0 * 2) << (4);
    a2 = (v_stack_m108) + (a1);
    a1 = 0;
    v_stack_m12D = 0;
    if (((*(unsigned int *)(a2 + 40)) & ((unsigned int)(a4))) != 0) {
        a1 = 1;
        v_stack_m12D = (unsigned __int8)(a1);
    }
    if (((*(unsigned int *)(a2 + 44)) & ((unsigned int)(a4))) != 0) {
        a1 = (unsigned __int8)((a1) | (2));
        v_stack_m12D = (unsigned __int8)(a1);
    }
    if ((((unsigned int)((unsigned __int8)(a1))) & ((unsigned int)((unsigned __int8)(a1) - 1))) != 0) goto loc_00259374;
    v_stack_m198 = (unsigned int)((unsigned __int8)(a1) - 1);
    goto loc_00258803;
loc_00258A9F:
loc_00258AA6:
    result = (unsigned int)(((unsigned __int8)(a1) - 1) | (*(unsigned int *)(v_stack_mDC - 4)));
    v_stack_m134 = (unsigned int)(result);
    result = (unsigned int)((result) | (*(unsigned int *)(v_stack_mDC + 48 - 48)));
    v_stack_m134 = (unsigned int)(result);
    a2 = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(a2 + 8)))) - (1);
    if (condition_is_equal) goto loc_00258745;
    goto loc_00258AA6;
loc_00258AC2:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m110) - 216 + 104) == 0) goto loc_0025895A;
    a1 = ((unsigned int)(*(unsigned int *)(0 + 216))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m110) - 216 + 104));
    if (condition_is_equal) goto loc_0025895A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m110) - 216 + 195)) >= 16) goto loc_0025895A;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m110) - 216 + 120)) & (512)) != 0) goto loc_0025895A;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m110) - 216 + 484)) != 0) goto loc_0025895A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m110) - 216 + 390)) == 1) goto loc_0025895A;
loc_00258B20:
    if (((*(unsigned __int8 *)(a1 + 112)) & (2)) != 0) goto loc_002597A9;
    if (*(unsigned __int64 *)(a1 + 416) != 0) goto loc_00258B20;
loc_00258B36:
    a3 = (unsigned int)((0) + (*(unsigned int *)(a1 + 124)));
    if (condition_is_not_equal) goto loc_00258B48;
    if (*(unsigned __int64 *)(a1 + 416) != 0) goto loc_00258B36;
loc_00258B48:
    if ((unsigned int)(a3) != 0) goto loc_002597A9;
    v_r14 = 0;
    goto loc_0025895A;
loc_00258B59:
    v_r15 = (0 + 0 * 4 * 8) + (a1);
    if ((*(unsigned int *)(v_rip + 14075758)) == 0) goto loc_00258B83;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 + 16) + 35)) & (32)) != 0) goto loc_002590AF;
loc_00258B83:
    if (*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 40) == 0) goto loc_002590C4;
loc_00258B8C:
    if (*(unsigned __int64 *)(v_r15 + 24) == 0) goto loc_00258C74;
    if ((*(unsigned __int64 *)(v_r15 + 24)) != (*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 40))) goto loc_00258C74;
    result = KiComputeThreadQos(*(unsigned __int64 *)(v_stack_m110) - 216, *(unsigned __int64 *)(a1 + 416), a3, a4);
    a3 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m110) - 216 + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m110) - 216 + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m110) - 216 + 84))))) { a3 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m110) - 216 + 84))); }
    a2 = 0;
    a2 = (((unsigned int)(a3)) >= (*(unsigned int *)(v_rip + 14075821))) ? 1 : 0;
    a3 = (unsigned int)((a2 + result * 2) * ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 16) + 192) + 185))));
    a3 = (unsigned int)((a3) + ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m110) - 216 + 517))));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 16) + 192) + 192) + a3 + a3 * 2 * 8 + 8)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 16) + 192) + 192) + a3 + a3 * 2 * 8 + 16));
    v_stack_m170 = a2;
    a2 = (a2) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 16) + 192) + 192) + a3 + a3 * 2 * 8));
    v_stack_m178 = a2;
    v_stack_m168 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 16) + 192) + 192) + a3 + a3 * 2 * 8 + 16);
    v_stack_m158 = v_xmm0;
    v_stack_m148 = v_xmm1;
    if (((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 16) + 200)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 16) + 192) + 192) + a3 + a3 * 2 * 8 + 16))) == 0) goto loc_00259268;
loc_00258C37:
    if ((*(unsigned __int64 *)(v_r15 + 16)) != v_stack_m188) goto loc_00258F5B;
loc_00258C42:
    v_stack_m160 = 0;
    if ((*(unsigned __int8 *)(v_rip + 14081651)) == 0) goto loc_002593A1;
    a3 = 0;
    result = KiEvaluateGroupSchedulingPreemption(v_r15 + 16, *(unsigned __int64 *)(v_stack_m110) - 216, a3, v_stack_m160);
    if ((unsigned __int8)(result) != 0) goto loc_00258D45;
loc_00258C74:
    v_r14 = (unsigned int)((v_r14) + 1);
    goto loc_0025897D;
loc_00258C86:
loc_00258C8D:
    result = (unsigned int)((result) | (*(unsigned int *)(v_stack_mDC - 4)));
    v_stack_m134 = (unsigned int)(result);
    result = (unsigned int)((result) | (*(unsigned int *)(v_stack_mDC + 48 - 48)));
    v_stack_m134 = (unsigned int)(result);
    a2 = (0) - (1);
    if (condition_is_equal) goto loc_002589DC;
    goto loc_00258C8D;
loc_00258CA9:
    result = KxWaitForLockOwnerShip(v_stack_mDC + 48, a2, a3, v_stack_m160);
    v_rdi = (unsigned int)((*(unsigned __int64 *)(v_stack_m110)) + 1);
    goto loc_00258669;
loc_00258CB8:
    result = KiAdvanceReadyQueueEnumeratorToNextList(v_stack_m138, a2, v_stack_m188, v_stack_m160);
    if (!sign_flag) goto loc_002588F0;
loc_00258CC9:
loc_00258CD0:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m180)) == 0) goto loc_00258D0A;
loc_00258CE2:
    if ((*(unsigned __int64 *)(v_stack_m180 + 24)) <= v_r14) goto loc_00258CF7;
    if (v_r14 == 0) goto loc_00258CF4;
    v_rbx = v_r14;
    if ((*(unsigned __int64 *)(v_stack_m180 + 24)) < v_r14) {
        v_rbx = *(unsigned __int64 *)(v_stack_m180 + 24);
    }
    a1 = (v_stack_m180 + 24) + (40);
    a2 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_stack_m180)))) - (1);
    if (condition_is_not_equal) goto loc_00258CE2;
    if (v_rbx != 0) goto loc_002592E7;
loc_00258D0A:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_r14, v_stack_m160);
    v_rsp = (v_rsp) + (416);
    return result;
loc_00258D35:
    if ((((unsigned __int8)(result)) & (16)) == 0) goto loc_00258C74;
    if ((unsigned __int8)(a1) == 0) goto loc_00258C74;
loc_00258D45:
loc_00258D4E:
    if (*(unsigned __int64 *)(v_r15 + 16) == 0) goto loc_00258990;
    a1 = (v_stack_m12E + v_stack_m12E * 2) + (v_stack_m12E + v_stack_m12E * 2);
    if (v_stack_m12B == 2) goto loc_00259291;
    v_stack_m110 = *(unsigned __int64 *)(v_stack_m110 + 8);
    if ((unsigned int)(v_stack_m12C) == 0) goto loc_00258FA7;
    if (((unsigned int)(v_stack_m12C)) != 1) goto loc_00258DFF;
    if ((((unsigned int)(v_stack_m12D)) & ((unsigned int)(v_stack_m12D - 1))) != 0) {
    }
    if (((*(unsigned int *)((unsigned int)((unsigned int)(v_r14)) + 120)) & (0x400000ULL)) != 0) goto loc_002593D8;
loc_00258DBF:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 8)) != v_rdi) goto loc_00258DD5;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8))) == v_rdi) goto loc_00258F19;
loc_00258DD5:
loc_00258DDC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8))) == v_rdi) goto loc_00258EFB;
loc_00258DE7:
loc_00258DF4:
    a3 = 0;
    result = KiUpdateSoftParkElectionStatisticsOnRemoval(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 48) + 36424), (unsigned int)((unsigned int)(v_r14)), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 48) + 36424));
loc_00258DFF:
    a4 = 0;
    a2 = 0;
loc_00258E10:
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(v_stack_p58)))) goto loc_00258E33;
    if ((*(unsigned __int64 *)(a2 + a2 * 4 * 8 + v_stack_p58 * 1 + 16)) == (*(unsigned __int64 *)(v_r15 + 16))) goto loc_00258E2C;
    a2 = (unsigned int)((a2) + 1);
    goto loc_00258E10;
loc_00258E2C:
    a4 = (v_stack_p58 + 16) + (a2 + a2 * 4 * 8);
loc_00258E33:
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_r14)) + 120))) >> (1));
    result = (unsigned int)((*(unsigned __int8 *)(a4 + 32)) >> (1));
    v_r10 = (unsigned int)((v_r10) & (1));
    result = (unsigned int)((result) & (1));
    if (((unsigned int)(v_r10)) >= ((unsigned int)(result))) goto loc_0025942F;
    v_r11 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_p58)) == 0) goto loc_0025948C;
loc_00258E62:
    a4 = (v_r11 + v_r11 * 4 * 8) + (v_stack_p58);
    if ((*(unsigned __int64 *)(a4 + 16)) == (*(unsigned __int64 *)(v_r15 + 16))) goto loc_002594E6;
    if ((*(unsigned __int64 *)(a4 + 40) - 1) <= -4) goto loc_002596E3;
loc_00258E94:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a4 + 48)) | (1));
    *(unsigned __int64 *)(a4 + 32) = *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24);
    *(unsigned __int8 *)(a4 + 48) = (unsigned __int8)(a1);
    a1 = (unsigned __int8)((a1) & (253));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24) + 120))) >> (1));
    result = (unsigned __int8)((result) & (1));
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (199));
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(a4 + 48) = (unsigned __int8)(result);
    *(unsigned __int64 *)(a4 + 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24);
    result = KiIsPrcbThread(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24), a2, *(unsigned __int8 *)(v_stack_p58), a4);
    if ((unsigned __int8)(result) == 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(a4 + 16) + 36);
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24) + 536) = (unsigned int)(result);
    }
    v_r11 = (unsigned int)((v_r11) + 1);
    if (((unsigned int)(v_r11)) < ((unsigned int)(*(unsigned __int8 *)(v_stack_p58)))) goto loc_00258E62;
    v_r14 = 0;
    *(unsigned int *)(v_stack_p58 + 4) = (unsigned int)(v_r10);
    goto loc_002586E0;
loc_00258EFB:
    a2 = ~(*(unsigned __int64 *)(a4 + 712));
    goto loc_00258DE7;
loc_00258F19:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 720)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24) + 8) = *(unsigned __int64 *)(a4 + 720);
    if ((*(unsigned __int64 *)(a4 + 720)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24))) goto loc_00258DDC;
    *(unsigned int *)(a4 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)));
    goto loc_00258DDC;
loc_00258F3D:
    goto loc_0025893A;
loc_00258F45:
    result = ((unsigned __int8)(v_r11)) + (0x844ULL);
    result = (result) << (4);
    result = (result) + (v_r10);
    goto loc_00258825;
loc_00258F5B:
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)(v_r14)) + 104) == 0) goto loc_00258C42;
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_p58 + 216))) + (*(unsigned __int64 *)((unsigned int)((unsigned int)(v_r14)) + 104));
    result = KiIsThreadConstrainedBySchedulingGroup((unsigned int)((unsigned int)(v_r14)), a2, *(unsigned __int8 *)(v_stack_p58), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00258C42;
    result = KiCheckForMaxOverQuotaScb(a2, a2, *(unsigned __int8 *)(v_stack_p58), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00258C42;
    result = KiShouldPreemptionBeDeferred((unsigned int)((unsigned int)(v_r14)), a2, *(unsigned __int8 *)(v_stack_p58), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00258C42;
    goto loc_00258C74;
loc_00258FA7:
    if ((((unsigned int)(v_stack_m12D)) & ((unsigned int)(v_stack_m12D - 1))) != 0) {
    }
    if (((*(unsigned int *)((unsigned int)((unsigned int)(v_r14)) + 120)) & (0x400000ULL)) != 0) goto loc_002594CE;
loc_00258FC7:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24))) goto loc_00258DD5;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24))) goto loc_00258DD5;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24) + 8);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24) + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24)))) {
        a1 = *(unsigned int *)(v_r14 + 33752);
        result = (unsigned __int8)(v_stack_p30);
        *(unsigned int *)(v_r14 + 33752) = (unsigned int)(a1);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24)))) goto loc_0025921D;
loc_00259010:
    goto loc_00258DF4;
loc_00259029:
    result = ((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_r14)) + 1784))) + (-88);
    if ((*(unsigned int *)(result + 124)) > ((unsigned int)(a4))) goto loc_00258879;
    goto loc_0025887C;
loc_0025903C:
    if (v_r11 != 0) goto loc_002592CB;
loc_00259045:
    goto loc_002588B8;
loc_00259050:
    v_stack_m12E = (unsigned __int8)((unsigned __int8)(a2));
    v_stack_m120 = a4;
    v_stack_m128 = a4;
    v_stack_m134 = (unsigned int)(*(unsigned __int16 *)(a4 + 120));
    a2 = ((unsigned __int8)((unsigned __int8)(a2)) + (unsigned __int8)((unsigned __int8)(a2)) * 2) + ((unsigned __int8)((unsigned __int8)(a2)) + (unsigned __int8)((unsigned __int8)(a2)) * 2);
    result = (unsigned int)(*(unsigned int *)(v_stack_mD8 + a2 * 8 - 16));
    if ((*(unsigned int *)(a4 + 124)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mD8 + a2 * 8 - 16))))) {
        result = *(unsigned int *)(v_stack_mD8 + a2 * 8 - 12);
        result = (unsigned int)((result) & ((unsigned int)(*(unsigned __int16 *)(a4 + 120))));
        a1 = (unsigned int)(result);
        v_stack_m134 = (unsigned int)(result);
    }
    if ((unsigned int)(a1) == 0) goto loc_00259249;
loc_0025908A:
    a1 = ((unsigned __int8)(result)) + (9);
    v_stack_p4C = (unsigned int)(result);
    a1 = (a1) << (4);
    a1 = (a1) + (a4);
    v_stack_m130 = (unsigned __int8)(result);
    v_stack_m118 = a1;
    v_stack_m110 = a1;
    goto loc_002588E2;
loc_002590AF:
    result = KiIsThreadExemptFromForcePark((unsigned int)((unsigned int)(v_r14)), a2, *(unsigned __int8 *)(v_stack_p58), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00258B83;
    goto loc_00258C74;
loc_002590C4:
    if (v_stack_p58 != ((unsigned __int8)(a2))) goto loc_00258B8C;
    goto loc_00258C42;
loc_002590D2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_r14)) + 116)))) & (8)) != 0) goto loc_00258951;
    a1 = (v_stack_m12E + v_stack_m12E * 2) + (v_stack_m12E + v_stack_m12E * 2);
    if (v_stack_m12B == 2) goto loc_002593F0;
    v_stack_m110 = *(unsigned __int64 *)(v_stack_m110 + 8);
    if ((unsigned int)(v_stack_m12C) == 0) goto loc_0025934E;
    if (((unsigned int)(v_stack_m12C)) != 1) goto loc_00259189;
    if ((((unsigned int)(v_stack_m12D)) & ((unsigned int)(v_stack_m12D - 1))) != 0) {
    }
    if (((*(unsigned int *)((unsigned int)((unsigned int)(v_r14)) + 120)) & (0x400000ULL)) != 0) goto loc_0025964D;
loc_00259140:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24))) goto loc_00258DD5;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24))) goto loc_00258DD5;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24) + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24)))) goto loc_002591DF;
loc_00259166:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24)))) goto loc_002591FF;
loc_00259171:
    a3 = 0;
    result = KiUpdateSoftParkElectionStatisticsOnRemoval(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 48) + 36424), (unsigned int)((unsigned int)(v_r14)), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 48) + 36424));
loc_00259189:
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_r14)) + 388))) == 1) goto loc_002592DE;
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_r14)) + 388))) != 5) goto loc_002591BE;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)((unsigned int)((unsigned int)(v_r14)) + 388)))) - (*(unsigned int *)((unsigned int)((unsigned int)(v_r14)) + 436)));
    if ((*(unsigned __int8 *)((unsigned int)((unsigned int)(v_r14)) + 391)) == 0) goto loc_002591D6;
loc_002591BE:
    *(unsigned __int8 *)((unsigned int)((unsigned int)(v_r14)) + 388) = 7;
    v_r14 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24)) = *(unsigned __int64 *)(v_stack_p30);
    *(unsigned __int64 *)(v_stack_p30) = *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24);
    goto loc_002586FD;
loc_002591D6:
    goto loc_002591BE;
loc_002591DF:
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 48) + 36424) + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 48) + 36424) + 8)));
    goto loc_00259166;
loc_002591F3:
    goto loc_0025893D;
loc_002591FF:
    a2 = ~(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 48) + 36424) + 712));
    goto loc_00259171;
loc_0025921D:
    if ((*(unsigned __int64 *)(v_r14 + 33840)) != 0) goto loc_00259010;
    a1 = ~(*(unsigned __int64 *)(v_r14 + 200));
    goto loc_00259010;
loc_00259249:
    result = KiAdvanceReadyQueueEnumeratorToNextScb(v_stack_m138, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 48) + 36424));
    if (!sign_flag) goto loc_00259384;
    goto loc_002588D5;
loc_00259268:
    result = (*(unsigned __int64 *)(0 + 712)) & ((unsigned int)(v_stack_m138));
    if (((v_stack_m138) & (result)) != 0) goto loc_00258C74;
    goto loc_00258C37;
loc_00259281:
    result = (condition_is_above_or_equal) ? 1 : 0;
    goto loc_00258803;
loc_00259291:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24))) != v_stack_m118) goto loc_00259390;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 24) + 8)) != v_stack_m118) goto loc_00259390;
    result = KiAdvanceReadyQueueEnumeratorToNextList(v_stack_m138, a2, (unsigned int)(v_stack_m138), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 48) + 36424));
loc_002592B5:
    result = KiRemoveThreadFromScbQueue(0, v_stack_m128, (unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)(v_stack_p30)));
    goto loc_00258DFF;
loc_002592CB:
    if ((*(unsigned int *)(a4 + 124)) >= ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_stack_p30)) + 124))))) goto loc_002588B8;
    goto loc_00259045;
loc_002592DE:
    goto loc_002591BE;
loc_002592E7:
    v_rdi = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14))))) + (11);
    v_rdi = (v_rdi) << (4);
    v_rdi = (v_rdi) + (v_stack_p58);
    if (((*(unsigned int *)(v_rip + 14080058)) & (0x200000ULL)) == 0) goto loc_00259347;
    if (*(unsigned __int64 *)(v_rdi) != 0) goto loc_00259321;
    if (*(unsigned __int64 *)(v_rdi) == 0) goto loc_0025933D;
    result = KxWaitForLockChainValid(v_rdi, v_stack_m128, (unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)(v_stack_p30)));
loc_00259321:
    *(unsigned __int64 *)(v_rdi) = 0;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_rdi + 8)) ^ ((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 8))));
    if ((((unsigned __int8)(result)) & (4)) != 0) {
        result = KeWakeAddressAll(result + 8, *(unsigned __int64 *)(v_rdi + 8), (unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)(v_stack_p30)));
    }
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) + 1);
    goto loc_00258CD0;
loc_00259347:
    goto loc_0025933D;
loc_0025934E:
    if ((((unsigned int)(v_stack_m12D)) & ((unsigned int)(v_stack_m12D - 1))) != 0) {
    }
    result = KiRemoveThreadFromReadyQueue(*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 48), v_rdi, 0, (unsigned int)((unsigned int)(v_stack_p30)));
    goto loc_00259189;
loc_00259374:
    result = (condition_is_above_or_equal) ? 1 : 0;
    goto loc_00258803;
loc_00259384:
    goto loc_0025908A;
loc_00259390:
    v_stack_m110 = *(unsigned __int64 *)(v_stack_m110 + 8);
    goto loc_002592B5;
loc_002593A1:
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p30 + 48))) & (1)) != 0) goto loc_00258D45;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 195))) > (*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p30 + 32) + 195))) goto loc_00258D45;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 195))) != (*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p30 + 32) + 195))) goto loc_00258D35;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p30 + 48))) & (24)) != 0) goto loc_00258D45;
    goto loc_00258D35;
loc_002593D8:
    goto loc_00258DBF;
loc_002593F0:
    if ((*(unsigned __int64 *)(v_rdi)) != v_stack_m118) goto loc_0025963C;
    if ((*(unsigned __int64 *)(v_rdi + 8)) != v_stack_m118) goto loc_0025963C;
    result = KiAdvanceReadyQueueEnumeratorToNextList(v_stack_m138, *(unsigned __int64 *)(v_stack_p30 + 32), *(unsigned __int64 *)(v_stack_m110 + 8), (unsigned int)((unsigned int)(v_stack_p30)));
loc_00259414:
    result = KiRemoveThreadFromScbQueue(*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 48), v_stack_m128, v_rsi, 0);
    goto loc_00259189;
loc_0025942F:
    if ((unsigned int)(v_stack_m12F) != 0) goto loc_0025953E;
    if ((*(unsigned __int64 *)(0 + 24) - 1) <= -4) goto loc_0025949D;
loc_00259449:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(0 + 32)) & (254));
    *(unsigned __int64 *)(0 + 16) = v_rsi;
    *(unsigned __int8 *)(0 + 32) = (unsigned __int8)(a1);
    a1 = (unsigned __int8)((a1) & (253));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 120))) >> (1));
    result = (unsigned __int8)((result) & (1));
    *(unsigned __int64 *)(0 + 24) = v_rsi;
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (199));
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(0 + 32) = (unsigned __int8)(result);
    if ((*(unsigned __int64 *)(v_rsi + 544)) != (v_rip + 14117505)) goto loc_002597FC;
loc_0025948C:
    v_r14 = 0;
    *(unsigned int *)(v_stack_p58 + 4) = (unsigned int)(v_stack_m12F);
    goto loc_002586E0;
loc_0025949D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 24) + 544)) == (v_rip + 14117468)) goto loc_00259449;
    if (((*(unsigned __int8 *)(0 + 33)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(*(unsigned __int64 *)(0 + 24) + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_p30, *(unsigned __int64 *)(0 + 24), v_rsi, 0);
    goto loc_00259449;
loc_002594CE:
    goto loc_00258FC7;
loc_002594E6:
    if ((*(unsigned __int64 *)(v_rsi + 968)) <= -4) goto loc_0025971C;
loc_002594F0:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(0 + 48)) & (254));
    *(unsigned __int64 *)(0 + 32) = v_rsi;
    *(unsigned __int8 *)(0 + 48) = (unsigned __int8)(a1);
    a1 = (unsigned __int8)((a1) & (253));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 120))) >> (1));
    result = (unsigned __int8)((result) & (1));
    *(unsigned __int64 *)(0 + 40) = v_rsi;
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (199));
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(0 + 48) = (unsigned __int8)(result);
    result = KiIsPrcbThread(v_rsi, *(unsigned __int64 *)(0 + 24), v_rsi, 0);
    if ((unsigned __int8)(result) != 0) goto loc_00258ED9;
    *(unsigned int *)(v_rsi + 536) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 36)));
    goto loc_00258ED9;
loc_0025953E:
    v_r11 = 0;
    if ((unsigned __int8)(v_rsi) == 0) goto loc_0025948C;
loc_0025954F:
    a4 = (v_r11 + v_r11 * 4 * 8) + (v_stack_p58);
    if ((*(unsigned __int64 *)(a4 + 16)) != (*(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 48))) goto loc_002595CF;
    if ((*(unsigned __int64 *)(a4 + 40) - 1) <= -4) goto loc_0025974B;
loc_00259579:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a4 + 48)) & (254));
    *(unsigned __int64 *)(a4 + 32) = v_rsi;
    *(unsigned __int8 *)(a4 + 48) = (unsigned __int8)(a1);
    a1 = (unsigned __int8)((a1) & (253));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 120))) >> (1));
    result = (unsigned __int8)((result) & (1));
    *(unsigned __int64 *)(a4 + 40) = v_rsi;
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (199));
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(a4 + 48) = (unsigned __int8)(result);
    result = KiIsPrcbThread(v_rsi, *(unsigned __int64 *)(0 + 24), v_rsi, a4);
    if ((unsigned __int8)(result) == 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(a4 + 16) + 36);
        *(unsigned int *)(v_rsi + 536) = (unsigned int)(result);
    }
    v_r11 = (unsigned int)((v_r11) + 1);
    if (((unsigned int)(v_r11)) < ((unsigned int)(*(unsigned __int8 *)(v_stack_p58)))) goto loc_0025954F;
    goto loc_0025948C;
loc_002595CF:
    if ((*(unsigned __int8 *)(v_stack_p58)) <= -4) goto loc_0025977A;
loc_002595E0:
    result = (unsigned __int8)((*(unsigned __int8 *)(a4 + 48)) & (254));
    *(unsigned __int64 *)(a4 + 32) = v_rsi;
    *(unsigned __int8 *)(a4 + 48) = (unsigned __int8)(result);
    result = (unsigned __int8)((result) & (253));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 120))) >> (1));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a1)));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) & (231));
    a1 = (unsigned __int8)((a1) | (4));
    a1 = (unsigned __int8)((a1) | (32));
    result = (unsigned __int8)(((unsigned __int8)(a1)) & (223));
    a1 = (unsigned __int8)(a1);
    if (v_rsi == (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 36480))) { a1 = (unsigned int)((unsigned __int8)(result)); }
    *(unsigned __int8 *)(a4 + 48) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(a4 + 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 36480);
    result = KiIsPrcbThread(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 36480), *(unsigned __int64 *)(0 + 24), v_rsi, a4);
    if ((unsigned __int8)(result) != 0) goto loc_002595BD;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 16) + 36480) + 536) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 16) + 36)));
    goto loc_002595BD;
loc_0025963C:
    v_stack_m110 = *(unsigned __int64 *)(v_stack_m110 + 8);
    goto loc_00259414;
loc_0025964D:
    goto loc_00259140;
loc_00259665:
    if (((unsigned int)(v_stack_m130)) < ((unsigned int)(*(unsigned __int8 *)(v_stack_p58)))) goto loc_002596AF;
    v_r14 = 0;
loc_00259672:
    if (0 >= ((unsigned int)(*(unsigned __int8 *)(v_stack_p58)))) goto loc_00258990;
    a1 = (v_r14 + v_r14 * 4 * 8 + 16) + (v_stack_p58);
    result = KiCanLocalReadyThreadBeScheduledToRescheduleContextEntry(a1, v_rsi, *(unsigned __int64 *)(v_stack_mD8 + a1 * 8 - 48), v_stack_m128);
    if ((unsigned __int8)(result) != 0) goto loc_00259712;
    v_r14 = (unsigned int)((v_r14) + 1);
    goto loc_00259672;
loc_002596AF:
    a4 = 0;
    a3 = 0;
    a1 = ((unsigned int)((unsigned int)(v_r14)) * 4 + 2) + ((unsigned int)((unsigned int)(v_r14)));
    a1 = (a1 * 8) + (v_stack_p58);
    result = KiDoesThreadDominateRescheduleContextEntry(a1, v_rsi, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00258990;
    v_r14 = (unsigned int)((v_r14) + 1);
    goto loc_00259665;
loc_002596E3:
    result = KiIsPrcbThread(a1, v_rsi, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00258E94;
    if (((*(unsigned __int8 *)(a4 + 49)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(a1 + 565) = 1;
    result = KiInsertDeferredReadyList(v_r14 + v_r14 * 4 * 8, a1, a3, a4);
    goto loc_00258E94;
loc_00259712:
    goto loc_00258D4E;
loc_0025971C:
    result = KiIsPrcbThread(v_r14 + v_r14 * 4 * 8, a1, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_002594F0;
    if (((*(unsigned __int8 *)(a4 + 49)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(v_r14 + v_r14 * 4 * 8 + 565) = 1;
    result = KiInsertDeferredReadyList(v_r14 + v_r14 * 4 * 8, v_r14 + v_r14 * 4 * 8, a3, a4);
    goto loc_002594F0;
loc_0025974B:
    result = KiIsPrcbThread(v_r14 + v_r14 * 4 * 8, v_r14 + v_r14 * 4 * 8, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00259579;
    if (((*(unsigned __int8 *)(a4 + 49)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(v_r14 + v_r14 * 4 * 8 + 565) = 1;
    result = KiInsertDeferredReadyList(v_r14 + v_r14 * 4 * 8, v_r14 + v_r14 * 4 * 8, a3, a4);
    goto loc_00259579;
loc_0025977A:
    result = KiIsPrcbThread(v_r14 + v_r14 * 4 * 8, v_r14 + v_r14 * 4 * 8, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_002595E0;
    if (((*(unsigned __int8 *)(a4 + 49)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(v_r14 + v_r14 * 4 * 8 + 565) = 1;
    result = KiInsertDeferredReadyList(v_r14 + v_r14 * 4 * 8, v_r14 + v_r14 * 4 * 8, a3, a4);
    goto loc_002595E0;
loc_002597A9:
    result = KiRemoveCurrentlyEnumeratedThreadFromReadyQueue(v_stack_m138, v_rsi, a3, a4);
    a4 = 0;
    *(unsigned int *)(v_rsi + 536) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r14 + v_r14 * 4 * 8 + v_stack_p58 * 1 + 16) + 36)));
    result = KiAddThreadToScbQueue(*(unsigned __int64 *)(v_r14 + v_r14 * 4 * 8 + v_stack_p58 * 1 + 16), v_r14, v_rsi, a4);
    if (((*(unsigned int *)(v_rip + 14078779)) & (0x800ULL)) == 0) goto loc_002586FD;
    a4 = 0;
    result = EtwTraceReadyQueueInsertion(v_rsi, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r14 + v_r14 * 4 * 8 + v_stack_p58 * 1 + 16) + 36)), 0 + 2, a4);
    goto loc_002586FD;
loc_002597FC:
    *(unsigned int *)(v_rsi + 536) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 36)));
    goto loc_0025948C;
}
```

## 5. (Beta) C Style

```c
int64_t KiSearchForNewThreadsForRescheduleContext(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint8_t v_stack_m12B;
    uint8_t v_stack_m12C;
    uint8_t v_stack_m12D;
    uint8_t v_stack_m12E;
    uint8_t v_stack_m12F;
    uint8_t v_stack_m130;
    uint32_t v_stack_m134;
    uint64_t v_stack_m138;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint32_t v_stack_m190;
    uint32_t v_stack_m194;
    uint32_t v_stack_m198;
    uint32_t v_stack_m19C;
    uint32_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m48;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mDC;
    uint64_t v_stack_p18;
    uint64_t v_stack_p30;
    uint32_t v_stack_p4C;
    uint64_t v_stack_p58;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (416);
    result = (*(uint64_t *)(v_rip + 0xBB20FA)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r14 = 0;
    v_stack_m1A8 = Arg2;
    v_stack_m180 = Arg1;
loc_00258669:
    if ((uint8_t)(*(uint8_t *)(arg1)) == 0) goto loc_002586E0;
loc_0025867B:
    if ((*(uint64_t *)(arg1 + 0x18)) <= 0) goto loc_00258690;
    if (0 == 0) goto loc_0025868D;
    local_rbx = 0;
    if ((*(uint64_t *)(arg1 + 0x18)) < 0) {
        local_rbx = *(uint64_t *)(arg1 + 0x18);
    }
    Arg1 = (Arg1 + 24) + (40);
    Arg2 = ((uint32_t)((uint32_t)(*(uint8_t *)(arg1)))) - (1);
    if (condition_is_not_equal) goto loc_0025867B;
    if (local_rbx == 0) goto loc_002586E0;
    Arg1 = (0) + (11);
    Arg1 = (Arg1) << (4);
    Arg1 = (Arg1) + (Arg1);
    if (((*(uint32_t *)(v_rip + 0xD6E482)) & (0x200000ULL)) == 0) goto loc_002589AE;
    *(uint64_t *)(arg1 + 0x8) = local_rbx;
    *(uint64_t *)(arg1) = 0;
    if (Arg1 != NULL) goto loc_00258CA9;
loc_002586D3:
    local_rdi = (uint32_t)((0) + 1);
    goto loc_00258669;
loc_002586E0:
    Arg2 = 0;
    result = memset(v_stack_m138, Arg2, 240, a4);
    result = KiStartReadyQueueEnumeratorForRescheduleContext(v_stack_m138, Arg1, 240, a4);
loc_002586FD:
    if (((uint8_t)(v_stack_m12B)) == 4) goto loc_00258CC9;
    if ((uint8_t)(v_stack_m12B) != 0) goto loc_002588F0;
loc_00258720:
    if (1 == 2) goto loc_00258836;
    Arg1 = (uint32_t)((1) - (1));
    if (condition_is_not_equal) goto loc_002589C4;
    v_stack_m134 = 0;
    if ((uint32_t)((uint32_t)(v_stack_m138)) != 0) goto loc_00258A9F;
loc_00258745:
    result = (uint32_t)((0) & (0xFFFFFFFEULL));
    v_stack_m134 = (uint32_t)(result);
    if (condition_is_equal) goto loc_002588D5;
    v_stack_m12E = (uint8_t)(v_stack_m12F);
    v_stack_m130 = (uint8_t)(local_r11);
    v_stack_m194 = (uint32_t)(local_r11);
    Arg1 = ((uint8_t)(v_stack_m12F) + (uint8_t)(v_stack_m12F) * 2) + ((uint8_t)(v_stack_m12F) + (uint8_t)(v_stack_m12F) * 2);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mD8 + arg1 * 8 - 0x8))) | (*(uint32_t *)(v_stack_mD8 + arg1 * 8 - 0x4)));
    a4 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)((uint8_t)(local_r11))))));
    if ((((uint32_t)(Arg2)) & ((uint32_t)(a4))) != 0) goto loc_002587B8;
loc_00258789:
    local_r10 = (uint8_t)((v_stack_m12F) + 1);
    v_stack_m12E = (uint8_t)(local_r10);
    if (((uint32_t)((uint8_t)(local_r10))) >= ((uint32_t)((uint32_t)(v_stack_m138)))) {
        local_r10 = 0;
        v_stack_m12E = 0;
    }
    Arg1 = (0 + 0 * 2) + (0 + 0 * 2);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mD8 + arg1 * 8 - 0x8))) | (*(uint32_t *)(v_stack_mD8 + arg1 * 8 - 0x4)));
    if ((((uint32_t)(Arg2)) & ((uint32_t)(a4))) == 0) goto loc_00258789;
loc_002587B8:
    Arg1 = (0 + 0 * 2) << (4);
    Arg2 = (v_stack_m108) + (Arg1);
    Arg1 = 0;
    v_stack_m12D = 0;
    if (((*(uint32_t *)(Arg2 + 0x28)) & ((uint32_t)(a4))) != 0) {
        Arg1 = 1;
        v_stack_m12D = (uint8_t)(Arg1);
    }
    if (((*(uint32_t *)(Arg2 + 0x2C)) & ((uint32_t)(a4))) != 0) {
        Arg1 = (uint8_t)((Arg1) | (2));
        v_stack_m12D = (uint8_t)(Arg1);
    }
    if ((((uint32_t)((uint8_t)(Arg1))) & ((uint32_t)((uint8_t)(Arg1) - 1))) != 0) goto loc_00259281;
    v_stack_m190 = (uint32_t)((uint8_t)(Arg1) - 1);
loc_00258803:
    v_stack_m12C = (uint8_t)((uint8_t)(Arg1) - 1);
    if ((uint8_t)((uint8_t)(Arg1) - 1) == 0) goto loc_00258F45;
    if (((uint32_t)((uint8_t)((uint8_t)(Arg1) - 1))) != 1) goto loc_00258829;
    result = ((uint8_t)(local_r11)) + (4);
    result = (result) << (4);
    result = (result) + (*(uint64_t *)(Arg2 + 0x8));
loc_00258825:
    v_stack_m118 = result;
loc_00258829:
    v_stack_m110 = v_stack_m118;
    goto loc_002588E2;
loc_00258836:
    Arg2 = 0;
    if ((uint32_t)(*(uint64_t *)(Arg2 + 0x8)) == 0) goto loc_00258894;
loc_00258840:
    Arg1 = (0 + 0 * 2) + (0 + 0 * 2);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mD8 + arg1 * 8 - 0x10))) == 0) goto loc_00258885;
    result = (*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x30)) + (0x8430ULL);
    if ((((uint8_t)(*(uint64_t *)(result + 0x8))) & (1)) != 0) goto loc_00258998;
loc_00258870:
    if (*(uint64_t *)(result + 0x8) != 0) goto loc_00259029;
loc_00258879:
loc_0025887C:
    *(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x20) = 0;
loc_00258885:
    Arg2 = (uint8_t)((Arg2) + 1);
    if (((uint32_t)((uint8_t)(Arg2))) < ((uint32_t)((uint32_t)(v_stack_m138)))) goto loc_00258840;
loc_00258894:
    local_rbx = 0;
loc_002588A0:
    Arg1 = ((uint8_t)((uint8_t)(v_stack_m12F)) + (uint8_t)((uint8_t)(v_stack_m12F)) * 2) + ((uint8_t)((uint8_t)(v_stack_m12F)) + (uint8_t)((uint8_t)(v_stack_m12F)) * 2);
    if (*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x20) != 0) goto loc_0025903C;
loc_002588B8:
    Arg2 = (uint8_t)(((uint8_t)(v_stack_m12F)) + 1);
    Arg2 = (uint8_t)(Arg2);
    if (((uint32_t)((uint8_t)(Arg2))) >= ((uint32_t)((uint32_t)(v_stack_m138)))) { Arg2 = 0; }
    if (((uint8_t)(Arg2)) != ((uint8_t)(v_stack_m12F))) goto loc_002588A0;
    if (0 != 0) goto loc_00259050;
loc_002588D5:
    local_rdi = (uint8_t)((1) + 1);
    if (((uint8_t)(local_rdi)) < 4) goto loc_00258720;
loc_002588E2:
    v_stack_m12B = (uint8_t)(local_rdi);
    if (((uint8_t)(local_rdi)) == 4) goto loc_00258CC9;
loc_002588F0:
    v_stack_m110 = *(uint64_t *)(v_stack_m110);
    if ((*(uint64_t *)(v_stack_m110)) == v_stack_m118) goto loc_00258CB8;
    Arg1 = (v_stack_m12E + v_stack_m12E * 2) + (v_stack_m12E + v_stack_m12E * 2);
    v_stack_m188 = *(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x30);
    if (v_stack_m12B == 2) goto loc_002591F3;
    if (v_stack_m12C != 1) goto loc_00258F3D;
loc_0025893A:
loc_0025893D:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m110) - 0xD8 + 0x238)) != (*(uint64_t *)(v_rip + 0xD6E2B4))) goto loc_002590D2;
loc_00258951:
    if (0 == 0) goto loc_00258AC2;
loc_0025895A:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m110) - 0xD8 + 0x78))) >> (1));
    Arg1 = (uint32_t)((Arg1) & (1));
    if (((uint32_t)(Arg1)) > (*(uint32_t *)(arg1 + 0x8))) goto loc_002586FD;
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))); }
    if ((uint32_t)(Arg1) != 0) goto loc_00259665;
loc_0025897D:
    if (0 < ((uint32_t)(*(uint8_t *)(arg1)))) goto loc_00258B59;
loc_00258990:
    local_r14 = 0;
    goto loc_002586FD;
loc_00258998:
    if (((uint32_t)(v_stack_m138)) == 1) goto loc_00258879;
    result = (*(uint8_t *)(arg1)) | (1);
    result = (result) ^ ((uint32_t)(v_stack_m138));
    goto loc_00258870;
loc_002589AE:
    v_stack_m1A0 = 0;
    if (condition_is_above_or_equal) goto loc_002586D3;
loc_002589C4:
    if (((uint32_t)(Arg1)) != 2) goto loc_002588D5;
    v_stack_m134 = 0;
    if ((uint32_t)((uint32_t)(v_stack_m138)) != 0) goto loc_00258C86;
loc_002589DC:
    result = (uint32_t)((0) & (1));
    v_stack_m134 = (uint32_t)(result);
    if (condition_is_equal) goto loc_002588D5;
    v_stack_m12E = (uint8_t)(v_stack_m12F);
    v_stack_m130 = 0;
    v_stack_m19C = 0;
    Arg1 = ((uint8_t)(v_stack_m12F) + (uint8_t)(v_stack_m12F) * 2) + ((uint8_t)(v_stack_m12F) + (uint8_t)(v_stack_m12F) * 2);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mD8 + arg1 * 8 - 0x8))) | (*(uint32_t *)(v_stack_mD8 + arg1 * 8 - 0x4)));
    a4 = (uint32_t)((1) << (0));
    if ((((uint32_t)(Arg2)) & ((uint32_t)(a4))) != 0) goto loc_00258A4F;
loc_00258A20:
    local_r10 = (uint8_t)((v_stack_m12F) + 1);
    v_stack_m12E = (uint8_t)(local_r10);
    if (((uint32_t)((uint8_t)(local_r10))) >= ((uint32_t)((uint32_t)(v_stack_m138)))) {
        local_r10 = 0;
        v_stack_m12E = 0;
    }
    Arg1 = (0 + 0 * 2) + (0 + 0 * 2);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mD8 + arg1 * 8 - 0x8))) | (*(uint32_t *)(v_stack_mD8 + arg1 * 8 - 0x4)));
    if ((((uint32_t)(Arg2)) & ((uint32_t)(a4))) == 0) goto loc_00258A20;
loc_00258A4F:
    Arg1 = (0 + 0 * 2) << (4);
    Arg2 = (v_stack_m108) + (Arg1);
    Arg1 = 0;
    v_stack_m12D = 0;
    if (((*(uint32_t *)(Arg2 + 0x28)) & ((uint32_t)(a4))) != 0) {
        Arg1 = 1;
        v_stack_m12D = (uint8_t)(Arg1);
    }
    if (((*(uint32_t *)(Arg2 + 0x2C)) & ((uint32_t)(a4))) != 0) {
        Arg1 = (uint8_t)((Arg1) | (2));
        v_stack_m12D = (uint8_t)(Arg1);
    }
    if ((((uint32_t)((uint8_t)(Arg1))) & ((uint32_t)((uint8_t)(Arg1) - 1))) != 0) goto loc_00259374;
    v_stack_m198 = (uint32_t)((uint8_t)(Arg1) - 1);
    goto loc_00258803;
loc_00258A9F:
loc_00258AA6:
    result = (uint32_t)(((uint8_t)(Arg1) - 1) | (*(uint32_t *)(v_stack_mDC - 0x4)));
    v_stack_m134 = (uint32_t)(result);
    result = (uint32_t)((result) | (*(uint32_t *)(v_stack_mDC + 0x30 - 0x30)));
    v_stack_m134 = (uint32_t)(result);
    Arg2 = ((uint32_t)((uint32_t)(*(uint64_t *)(Arg2 + 0x8)))) - (1);
    if (condition_is_equal) goto loc_00258745;
    goto loc_00258AA6;
loc_00258AC2:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m110) - 0xD8 + 0x68) == 0) goto loc_0025895A;
    Arg1 = ((uint32_t)(*(uint32_t *)(0 + 0xD8))) + (*(uint64_t *)(*(uint64_t *)(v_stack_m110) - 0xD8 + 0x68));
    if (condition_is_equal) goto loc_0025895A;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m110) - 0xD8 + 0xC3)) >= 16) goto loc_0025895A;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m110) - 0xD8 + 0x78)) & (512)) != 0) goto loc_0025895A;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m110) - 0xD8 + 0x1E4)) != 0) goto loc_0025895A;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m110) - 0xD8 + 0x186)) == 1) goto loc_0025895A;
loc_00258B20:
    if (((*(uint8_t *)(arg1 + 0x70)) & (2)) != 0) goto loc_002597A9;
    if (*(uint64_t *)(arg1 + 0x1A0) != 0) goto loc_00258B20;
loc_00258B36:
    a3 = (uint32_t)((0) + (*(uint32_t *)(arg1 + 0x7C)));
    if (condition_is_not_equal) goto loc_00258B48;
    if (*(uint64_t *)(arg1 + 0x1A0) != 0) goto loc_00258B36;
loc_00258B48:
    if ((uint32_t)(a3) != 0) goto loc_002597A9;
    local_r14 = 0;
    goto loc_0025895A;
loc_00258B59:
    local_r15 = (0 + 0 * 4 * 8) + (Arg1);
    if ((*(uint32_t *)(v_rip + 0xD6C76E)) == 0) goto loc_00258B83;
    if (((*(uint8_t *)(*(uint64_t *)(local_r15 + 0x10) + 0x23)) & (32)) != 0) goto loc_002590AF;
loc_00258B83:
    if (*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x28) == 0) goto loc_002590C4;
loc_00258B8C:
    if (*(uint64_t *)(local_r15 + 0x18) == 0) goto loc_00258C74;
    if ((*(uint64_t *)(local_r15 + 0x18)) != (*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x28))) goto loc_00258C74;
    result = KiComputeThreadQos(*(uint64_t *)(v_stack_m110) - 216, *(uint64_t *)(arg1 + 0x1A0), a3, a4);
    a3 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m110) - 0xD8 + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m110) - 0xD8 + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m110) - 0xD8 + 0x54))))) { a3 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m110) - 0xD8 + 0x54))); }
    Arg2 = 0;
    Arg2 = (((uint32_t)(a3)) >= (*(uint32_t *)(v_rip + 0xD6C7AD))) ? 1 : 0;
    a3 = (uint32_t)((Arg2 + result * 2) * ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x10) + 0xC0) + 0xB9))));
    a3 = (uint32_t)((a3) + ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m110) - 0xD8 + 0x205))));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x10) + 0xC0) + 0xC0) + a3 + a3 * 2 * 8 + 0x8)) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x10) + 0xC0) + 0xC0) + a3 + a3 * 2 * 8 + 0x10));
    v_stack_m170 = Arg2;
    Arg2 = (Arg2) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x10) + 0xC0) + 0xC0) + a3 + a3 * 2 * 8));
    v_stack_m178 = Arg2;
    v_stack_m168 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x10) + 0xC0) + 0xC0) + a3 + a3 * 2 * 8 + 0x10);
    v_stack_m158 = v_xmm0;
    v_stack_m148 = v_xmm1;
    if (((*(uint64_t *)(*(uint64_t *)(local_r15 + 0x10) + 0xC8)) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x10) + 0xC0) + 0xC0) + a3 + a3 * 2 * 8 + 0x10))) == 0) goto loc_00259268;
loc_00258C37:
    if ((*(uint64_t *)(local_r15 + 0x10)) != v_stack_m188) goto loc_00258F5B;
loc_00258C42:
    v_stack_m160 = 0;
    if ((*(uint8_t *)(v_rip + 0xD6DE73)) == 0) goto loc_002593A1;
    a3 = 0;
    result = KiEvaluateGroupSchedulingPreemption(local_r15 + 16, *(uint64_t *)(v_stack_m110) - 216, a3, v_stack_m160);
    if ((uint8_t)(result) != 0) goto loc_00258D45;
loc_00258C74:
    local_r14 = (uint32_t)((local_r14) + 1);
    goto loc_0025897D;
loc_00258C86:
loc_00258C8D:
    result = (uint32_t)((result) | (*(uint32_t *)(v_stack_mDC - 0x4)));
    v_stack_m134 = (uint32_t)(result);
    result = (uint32_t)((result) | (*(uint32_t *)(v_stack_mDC + 0x30 - 0x30)));
    v_stack_m134 = (uint32_t)(result);
    Arg2 = (0) - (1);
    if (condition_is_equal) goto loc_002589DC;
    goto loc_00258C8D;
loc_00258CA9:
    result = KxWaitForLockOwnerShip(v_stack_mDC + 48, Arg2, a3, v_stack_m160);
    local_rdi = (uint32_t)((*(uint64_t *)(v_stack_m110)) + 1);
    goto loc_00258669;
loc_00258CB8:
    result = KiAdvanceReadyQueueEnumeratorToNextList(v_stack_m138, Arg2, v_stack_m188, v_stack_m160);
    if (!sign_flag) goto loc_002588F0;
loc_00258CC9:
loc_00258CD0:
    if ((uint8_t)(*(uint8_t *)(v_stack_m180)) == 0) goto loc_00258D0A;
loc_00258CE2:
    if ((*(uint64_t *)(v_stack_m180 + 0x18)) <= local_r14) goto loc_00258CF7;
    if (local_r14 == 0) goto loc_00258CF4;
    local_rbx = local_r14;
    if ((*(uint64_t *)(v_stack_m180 + 0x18)) < local_r14) {
        local_rbx = *(uint64_t *)(v_stack_m180 + 0x18);
    }
    Arg1 = (v_stack_m180 + 24) + (40);
    Arg2 = ((uint32_t)((uint32_t)(*(uint8_t *)(v_stack_m180)))) - (1);
    if (condition_is_not_equal) goto loc_00258CE2;
    if (local_rbx != 0) goto loc_002592E7;
loc_00258D0A:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, local_r14, v_stack_m160);
    local_rsp = (local_rsp) + (416);
    return result;
loc_00258D35:
    if ((((uint8_t)(result)) & (16)) == 0) goto loc_00258C74;
    if ((uint8_t)(Arg1) == 0) goto loc_00258C74;
loc_00258D45:
loc_00258D4E:
    if (*(uint64_t *)(local_r15 + 0x10) == 0) goto loc_00258990;
    Arg1 = (v_stack_m12E + v_stack_m12E * 2) + (v_stack_m12E + v_stack_m12E * 2);
    if (v_stack_m12B == 2) goto loc_00259291;
    v_stack_m110 = *(uint64_t *)(v_stack_m110 + 0x8);
    if ((uint32_t)(v_stack_m12C) == 0) goto loc_00258FA7;
    if (((uint32_t)(v_stack_m12C)) != 1) goto loc_00258DFF;
    if ((((uint32_t)(v_stack_m12D)) & ((uint32_t)(v_stack_m12D - 1))) != 0) {
    }
    if (((*(uint32_t *)((uint32_t)((uint32_t)(local_r14)) + 0x78)) & (0x400000ULL)) != 0) goto loc_002593D8;
loc_00258DBF:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi) + 0x8)) != local_rdi) goto loc_00258DD5;
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x8))) == local_rdi) goto loc_00258F19;
loc_00258DD5:
loc_00258DDC:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x8))) == local_rdi) goto loc_00258EFB;
loc_00258DE7:
loc_00258DF4:
    a3 = 0;
    result = KiUpdateSoftParkElectionStatisticsOnRemoval(*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x30) + 0x8E48), (uint32_t)((uint32_t)(local_r14)), a3, *(uint64_t *)(*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x30) + 0x8E48));
loc_00258DFF:
    a4 = 0;
    Arg2 = 0;
loc_00258E10:
    if (0 >= ((uint32_t)(*(uint8_t *)(v_stack_p58)))) goto loc_00258E33;
    if ((*(uint64_t *)(Arg2 + Arg2 * 4 * 8 + v_stack_p58 * 1 + 0x10)) == (*(uint64_t *)(local_r15 + 0x10))) goto loc_00258E2C;
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_00258E10;
loc_00258E2C:
    a4 = (v_stack_p58 + 16) + (Arg2 + Arg2 * 4 * 8);
loc_00258E33:
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_r14)) + 0x78))) >> (1));
    result = (uint32_t)((*(uint8_t *)(a4 + 0x20)) >> (1));
    local_r10 = (uint32_t)((local_r10) & (1));
    result = (uint32_t)((result) & (1));
    if (((uint32_t)(local_r10)) >= ((uint32_t)(result))) goto loc_0025942F;
    local_r11 = 0;
    if ((uint8_t)(*(uint8_t *)(v_stack_p58)) == 0) goto loc_0025948C;
loc_00258E62:
    a4 = (local_r11 + local_r11 * 4 * 8) + (v_stack_p58);
    if ((*(uint64_t *)(a4 + 0x10)) == (*(uint64_t *)(local_r15 + 0x10))) goto loc_002594E6;
    if ((*(uint64_t *)(a4 + 0x28) - 1) <= -4) goto loc_002596E3;
loc_00258E94:
    Arg1 = (uint8_t)((*(uint8_t *)(a4 + 0x30)) | (1));
    *(uint64_t *)(a4 + 0x20) = *(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18);
    *(uint8_t *)(a4 + 0x30) = (uint8_t)(Arg1);
    Arg1 = (uint8_t)((Arg1) & (253));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18) + 0x78))) >> (1));
    result = (uint8_t)((result) & (1));
    result = (uint8_t)((result) + ((uint8_t)(result)));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (199));
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(a4 + 0x30) = (uint8_t)(result);
    *(uint64_t *)(a4 + 0x28) = *(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18);
    result = KiIsPrcbThread(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18), Arg2, *(uint8_t *)(v_stack_p58), a4);
    if ((uint8_t)(result) == 0) {
        result = *(uint32_t *)(*(uint64_t *)(a4 + 0x10) + 0x24);
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18) + 0x218) = (uint32_t)(result);
    }
    local_r11 = (uint32_t)((local_r11) + 1);
    if (((uint32_t)(local_r11)) < ((uint32_t)(*(uint8_t *)(v_stack_p58)))) goto loc_00258E62;
    local_r14 = 0;
    *(uint32_t *)(v_stack_p58 + 0x4) = (uint32_t)(local_r10);
    goto loc_002586E0;
loc_00258EFB:
    Arg2 = ~(*(uint64_t *)(a4 + 0x2C8));
    goto loc_00258DE7;
loc_00258F19:
    *(uint64_t *)(*(uint64_t *)(a4 + 0x2D0)) = *(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18) + 0x8) = *(uint64_t *)(a4 + 0x2D0);
    if ((*(uint64_t *)(a4 + 0x2D0)) != (*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18))) goto loc_00258DDC;
    *(uint32_t *)(a4 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(a4 + 0x8)));
    goto loc_00258DDC;
loc_00258F3D:
    goto loc_0025893A;
loc_00258F45:
    result = ((uint8_t)(local_r11)) + (0x844ULL);
    result = (result) << (4);
    result = (result) + (local_r10);
    goto loc_00258825;
loc_00258F5B:
    if (*(uint64_t *)((uint32_t)((uint32_t)(local_r14)) + 0x68) == 0) goto loc_00258C42;
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_p58 + 0xD8))) + (*(uint64_t *)((uint32_t)((uint32_t)(local_r14)) + 0x68));
    result = KiIsThreadConstrainedBySchedulingGroup((uint32_t)((uint32_t)(local_r14)), Arg2, *(uint8_t *)(v_stack_p58), a4);
    if ((uint8_t)(result) == 0) goto loc_00258C42;
    result = KiCheckForMaxOverQuotaScb(Arg2, Arg2, *(uint8_t *)(v_stack_p58), a4);
    if ((uint8_t)(result) == 0) goto loc_00258C42;
    result = KiShouldPreemptionBeDeferred((uint32_t)((uint32_t)(local_r14)), Arg2, *(uint8_t *)(v_stack_p58), a4);
    if ((uint8_t)(result) != 0) goto loc_00258C42;
    goto loc_00258C74;
loc_00258FA7:
    if ((((uint32_t)(v_stack_m12D)) & ((uint32_t)(v_stack_m12D - 1))) != 0) {
    }
    if (((*(uint32_t *)((uint32_t)((uint32_t)(local_r14)) + 0x78)) & (0x400000ULL)) != 0) goto loc_002594CE;
loc_00258FC7:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18))) goto loc_00258DD5;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18))) goto loc_00258DD5;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18) + 0x8)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18)) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18) + 0x8);
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18) + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18)))) {
        Arg1 = *(uint32_t *)(local_r14 + 0x83D8);
        result = (uint8_t)(v_stack_p30);
        *(uint32_t *)(local_r14 + 0x83D8) = (uint32_t)(Arg1);
    }
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18)))) goto loc_0025921D;
loc_00259010:
    goto loc_00258DF4;
loc_00259029:
    result = ((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_r14)) + 0x6F8))) + (-88);
    if ((*(uint32_t *)(result + 0x7C)) > ((uint32_t)(a4))) goto loc_00258879;
    goto loc_0025887C;
loc_0025903C:
    if (local_r11 != 0) goto loc_002592CB;
loc_00259045:
    goto loc_002588B8;
loc_00259050:
    v_stack_m12E = (uint8_t)((uint8_t)(Arg2));
    v_stack_m120 = a4;
    v_stack_m128 = a4;
    v_stack_m134 = (uint32_t)(*(uint16_t *)(a4 + 0x78));
    Arg2 = ((uint8_t)((uint8_t)(Arg2)) + (uint8_t)((uint8_t)(Arg2)) * 2) + ((uint8_t)((uint8_t)(Arg2)) + (uint8_t)((uint8_t)(Arg2)) * 2);
    result = (uint32_t)(*(uint32_t *)(v_stack_mD8 + Arg2 * 8 - 0x10));
    if ((*(uint32_t *)(a4 + 0x7C)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mD8 + Arg2 * 8 - 0x10))))) {
        result = *(uint32_t *)(v_stack_mD8 + Arg2 * 8 - 0xC);
        result = (uint32_t)((result) & ((uint32_t)(*(uint16_t *)(a4 + 0x78))));
        Arg1 = (uint32_t)(result);
        v_stack_m134 = (uint32_t)(result);
    }
    if ((uint32_t)(Arg1) == 0) goto loc_00259249;
loc_0025908A:
    Arg1 = ((uint8_t)(result)) + (9);
    v_stack_p4C = (uint32_t)(result);
    Arg1 = (Arg1) << (4);
    Arg1 = (Arg1) + (a4);
    v_stack_m130 = (uint8_t)(result);
    v_stack_m118 = Arg1;
    v_stack_m110 = Arg1;
    goto loc_002588E2;
loc_002590AF:
    result = KiIsThreadExemptFromForcePark((uint32_t)((uint32_t)(local_r14)), Arg2, *(uint8_t *)(v_stack_p58), a4);
    if ((uint8_t)(result) != 0) goto loc_00258B83;
    goto loc_00258C74;
loc_002590C4:
    if (v_stack_p58 != ((uint8_t)(Arg2))) goto loc_00258B8C;
    goto loc_00258C42;
loc_002590D2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_r14)) + 0x74)))) & (8)) != 0) goto loc_00258951;
    Arg1 = (v_stack_m12E + v_stack_m12E * 2) + (v_stack_m12E + v_stack_m12E * 2);
    if (v_stack_m12B == 2) goto loc_002593F0;
    v_stack_m110 = *(uint64_t *)(v_stack_m110 + 0x8);
    if ((uint32_t)(v_stack_m12C) == 0) goto loc_0025934E;
    if (((uint32_t)(v_stack_m12C)) != 1) goto loc_00259189;
    if ((((uint32_t)(v_stack_m12D)) & ((uint32_t)(v_stack_m12D - 1))) != 0) {
    }
    if (((*(uint32_t *)((uint32_t)((uint32_t)(local_r14)) + 0x78)) & (0x400000ULL)) != 0) goto loc_0025964D;
loc_00259140:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18))) goto loc_00258DD5;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18))) goto loc_00258DD5;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18) + 0x8)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18)) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18) + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18)))) goto loc_002591DF;
loc_00259166:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18)))) goto loc_002591FF;
loc_00259171:
    a3 = 0;
    result = KiUpdateSoftParkElectionStatisticsOnRemoval(*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x30) + 0x8E48), (uint32_t)((uint32_t)(local_r14)), a3, *(uint64_t *)(*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x30) + 0x8E48));
loc_00259189:
    if (((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_r14)) + 0x184))) == 1) goto loc_002592DE;
    if (((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(local_r14)) + 0x184))) != 5) goto loc_002591BE;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint8_t *)((uint32_t)((uint32_t)(local_r14)) + 0x184)))) - (*(uint32_t *)((uint32_t)((uint32_t)(local_r14)) + 0x1B4)));
    if ((*(uint8_t *)((uint32_t)((uint32_t)(local_r14)) + 0x187)) == 0) goto loc_002591D6;
loc_002591BE:
    *(uint8_t *)((uint32_t)((uint32_t)(local_r14)) + 0x184) = 7;
    local_r14 = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18)) = *(uint64_t *)(v_stack_p30);
    *(uint64_t *)(v_stack_p30) = *(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18);
    goto loc_002586FD;
loc_002591D6:
    goto loc_002591BE;
loc_002591DF:
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x30) + 0x8E48) + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x30) + 0x8E48) + 0x8)));
    goto loc_00259166;
loc_002591F3:
    goto loc_0025893D;
loc_002591FF:
    Arg2 = ~(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x30) + 0x8E48) + 0x2C8));
    goto loc_00259171;
loc_0025921D:
    if ((*(uint64_t *)(local_r14 + 0x8430)) != 0) goto loc_00259010;
    Arg1 = ~(*(uint64_t *)(local_r14 + 0xC8));
    goto loc_00259010;
loc_00259249:
    result = KiAdvanceReadyQueueEnumeratorToNextScb(v_stack_m138, Arg2, a3, *(uint64_t *)(*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x30) + 0x8E48));
    if (!sign_flag) goto loc_00259384;
    goto loc_002588D5;
loc_00259268:
    result = (*(uint64_t *)(0 + 0x2C8)) & ((uint32_t)(v_stack_m138));
    if (((v_stack_m138) & (result)) != 0) goto loc_00258C74;
    goto loc_00258C37;
loc_00259281:
    result = (condition_is_above_or_equal) ? 1 : 0;
    goto loc_00258803;
loc_00259291:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18))) != v_stack_m118) goto loc_00259390;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x18) + 0x8)) != v_stack_m118) goto loc_00259390;
    result = KiAdvanceReadyQueueEnumeratorToNextList(v_stack_m138, Arg2, (uint32_t)(v_stack_m138), *(uint64_t *)(*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x30) + 0x8E48));
loc_002592B5:
    result = KiRemoveThreadFromScbQueue(0, v_stack_m128, (uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)(v_stack_p30)));
    goto loc_00258DFF;
loc_002592CB:
    if ((*(uint32_t *)(a4 + 0x7C)) >= ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(v_stack_p30)) + 0x7C))))) goto loc_002588B8;
    goto loc_00259045;
loc_002592DE:
    goto loc_002591BE;
loc_002592E7:
    local_rdi = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14))))) + (11);
    local_rdi = (local_rdi) << (4);
    local_rdi = (local_rdi) + (v_stack_p58);
    if (((*(uint32_t *)(v_rip + 0xD6D83A)) & (0x200000ULL)) == 0) goto loc_00259347;
    if (*(uint64_t *)(local_rdi) != 0) goto loc_00259321;
    if (*(uint64_t *)(local_rdi) == 0) goto loc_0025933D;
    result = KxWaitForLockChainValid(local_rdi, v_stack_m128, (uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)(v_stack_p30)));
loc_00259321:
    *(uint64_t *)(local_rdi) = 0;
    result = (uint8_t)((*(uint64_t *)(local_rdi + 0x8)) ^ ((uint8_t)(*(uint64_t *)(local_rdi + 0x8))));
    if ((((uint8_t)(result)) & (4)) != 0) {
        result = KeWakeAddressAll(result + 8, *(uint64_t *)(local_rdi + 0x8), (uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)(v_stack_p30)));
    }
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) + 1);
    goto loc_00258CD0;
loc_00259347:
    goto loc_0025933D;
loc_0025934E:
    if ((((uint32_t)(v_stack_m12D)) & ((uint32_t)(v_stack_m12D - 1))) != 0) {
    }
    result = KiRemoveThreadFromReadyQueue(*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x30), local_rdi, 0, (uint32_t)((uint32_t)(v_stack_p30)));
    goto loc_00259189;
loc_00259374:
    result = (condition_is_above_or_equal) ? 1 : 0;
    goto loc_00258803;
loc_00259384:
    goto loc_0025908A;
loc_00259390:
    v_stack_m110 = *(uint64_t *)(v_stack_m110 + 0x8);
    goto loc_002592B5;
loc_002593A1:
    if ((((uint8_t)(*(uint8_t *)(v_stack_p30 + 0x30))) & (1)) != 0) goto loc_00258D45;
    if (((uint8_t)(*(uint8_t *)(local_rsi + 0xC3))) > (*(uint8_t *)(*(uint64_t *)(v_stack_p30 + 0x20) + 0xC3))) goto loc_00258D45;
    if (((uint8_t)(*(uint8_t *)(local_rsi + 0xC3))) != (*(uint8_t *)(*(uint64_t *)(v_stack_p30 + 0x20) + 0xC3))) goto loc_00258D35;
    if ((((uint8_t)(*(uint8_t *)(v_stack_p30 + 0x30))) & (24)) != 0) goto loc_00258D45;
    goto loc_00258D35;
loc_002593D8:
    goto loc_00258DBF;
loc_002593F0:
    if ((*(uint64_t *)(local_rdi)) != v_stack_m118) goto loc_0025963C;
    if ((*(uint64_t *)(local_rdi + 0x8)) != v_stack_m118) goto loc_0025963C;
    result = KiAdvanceReadyQueueEnumeratorToNextList(v_stack_m138, *(uint64_t *)(v_stack_p30 + 0x20), *(uint64_t *)(v_stack_m110 + 0x8), (uint32_t)((uint32_t)(v_stack_p30)));
loc_00259414:
    result = KiRemoveThreadFromScbQueue(*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x30), v_stack_m128, local_rsi, 0);
    goto loc_00259189;
loc_0025942F:
    if ((uint32_t)(v_stack_m12F) != 0) goto loc_0025953E;
    if ((*(uint64_t *)(0 + 0x18) - 1) <= -4) goto loc_0025949D;
loc_00259449:
    Arg1 = (uint8_t)((*(uint8_t *)(0 + 0x20)) & (254));
    *(uint64_t *)(0 + 0x10) = local_rsi;
    *(uint8_t *)(0 + 0x20) = (uint8_t)(Arg1);
    Arg1 = (uint8_t)((Arg1) & (253));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x78))) >> (1));
    result = (uint8_t)((result) & (1));
    *(uint64_t *)(0 + 0x18) = local_rsi;
    result = (uint8_t)((result) + ((uint8_t)(result)));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (199));
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(0 + 0x20) = (uint8_t)(result);
    if ((*(uint64_t *)(local_rsi + 0x220)) != (v_rip + 14117505)) goto loc_002597FC;
loc_0025948C:
    local_r14 = 0;
    *(uint32_t *)(v_stack_p58 + 0x4) = (uint32_t)(v_stack_m12F);
    goto loc_002586E0;
loc_0025949D:
    if ((*(uint64_t *)(*(uint64_t *)(0 + 0x18) + 0x220)) == (v_rip + 14117468)) goto loc_00259449;
    if (((*(uint8_t *)(0 + 0x21)) & (1)) != 0) {
    }
    *(uint8_t *)(*(uint64_t *)(0 + 0x18) + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_p30, *(uint64_t *)(0 + 0x18), local_rsi, 0);
    goto loc_00259449;
loc_002594CE:
    goto loc_00258FC7;
loc_002594E6:
    if ((*(uint64_t *)(local_rsi + 0x3C8)) <= -4) goto loc_0025971C;
loc_002594F0:
    Arg1 = (uint8_t)((*(uint8_t *)(0 + 0x30)) & (254));
    *(uint64_t *)(0 + 0x20) = local_rsi;
    *(uint8_t *)(0 + 0x30) = (uint8_t)(Arg1);
    Arg1 = (uint8_t)((Arg1) & (253));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x78))) >> (1));
    result = (uint8_t)((result) & (1));
    *(uint64_t *)(0 + 0x28) = local_rsi;
    result = (uint8_t)((result) + ((uint8_t)(result)));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (199));
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(0 + 0x30) = (uint8_t)(result);
    result = KiIsPrcbThread(local_rsi, *(uint64_t *)(0 + 0x18), local_rsi, 0);
    if ((uint8_t)(result) != 0) goto loc_00258ED9;
    *(uint32_t *)(local_rsi + 0x218) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x24)));
    goto loc_00258ED9;
loc_0025953E:
    local_r11 = 0;
    if ((uint8_t)(local_rsi) == 0) goto loc_0025948C;
loc_0025954F:
    a4 = (local_r11 + local_r11 * 4 * 8) + (v_stack_p58);
    if ((*(uint64_t *)(a4 + 0x10)) != (*(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x30))) goto loc_002595CF;
    if ((*(uint64_t *)(a4 + 0x28) - 1) <= -4) goto loc_0025974B;
loc_00259579:
    Arg1 = (uint8_t)((*(uint8_t *)(a4 + 0x30)) & (254));
    *(uint64_t *)(a4 + 0x20) = local_rsi;
    *(uint8_t *)(a4 + 0x30) = (uint8_t)(Arg1);
    Arg1 = (uint8_t)((Arg1) & (253));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x78))) >> (1));
    result = (uint8_t)((result) & (1));
    *(uint64_t *)(a4 + 0x28) = local_rsi;
    result = (uint8_t)((result) + ((uint8_t)(result)));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (199));
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(a4 + 0x30) = (uint8_t)(result);
    result = KiIsPrcbThread(local_rsi, *(uint64_t *)(0 + 0x18), local_rsi, a4);
    if ((uint8_t)(result) == 0) {
        result = *(uint32_t *)(*(uint64_t *)(a4 + 0x10) + 0x24);
        *(uint32_t *)(local_rsi + 0x218) = (uint32_t)(result);
    }
    local_r11 = (uint32_t)((local_r11) + 1);
    if (((uint32_t)(local_r11)) < ((uint32_t)(*(uint8_t *)(v_stack_p58)))) goto loc_0025954F;
    goto loc_0025948C;
loc_002595CF:
    if ((*(uint8_t *)(v_stack_p58)) <= -4) goto loc_0025977A;
loc_002595E0:
    result = (uint8_t)((*(uint8_t *)(a4 + 0x30)) & (254));
    *(uint64_t *)(a4 + 0x20) = local_rsi;
    *(uint8_t *)(a4 + 0x30) = (uint8_t)(result);
    result = (uint8_t)((result) & (253));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x78))) >> (1));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg1)));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) & (231));
    Arg1 = (uint8_t)((Arg1) | (4));
    Arg1 = (uint8_t)((Arg1) | (32));
    result = (uint8_t)(((uint8_t)(Arg1)) & (223));
    Arg1 = (uint8_t)(Arg1);
    if (local_rsi == (*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x8E80))) { Arg1 = (uint32_t)((uint8_t)(result)); }
    *(uint8_t *)(a4 + 0x30) = (uint8_t)(Arg1);
    *(uint64_t *)(a4 + 0x28) = *(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x8E80);
    result = KiIsPrcbThread(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x8E80), *(uint64_t *)(0 + 0x18), local_rsi, a4);
    if ((uint8_t)(result) != 0) goto loc_002595BD;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(a4 + 0x10) + 0x8E80) + 0x218) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(a4 + 0x10) + 0x24)));
    goto loc_002595BD;
loc_0025963C:
    v_stack_m110 = *(uint64_t *)(v_stack_m110 + 0x8);
    goto loc_00259414;
loc_0025964D:
    goto loc_00259140;
loc_00259665:
    if (((uint32_t)(v_stack_m130)) < ((uint32_t)(*(uint8_t *)(v_stack_p58)))) goto loc_002596AF;
    local_r14 = 0;
loc_00259672:
    if (0 >= ((uint32_t)(*(uint8_t *)(v_stack_p58)))) goto loc_00258990;
    Arg1 = (local_r14 + local_r14 * 4 * 8 + 16) + (v_stack_p58);
    result = KiCanLocalReadyThreadBeScheduledToRescheduleContextEntry(Arg1, local_rsi, *(uint64_t *)(v_stack_mD8 + arg1 * 8 - 0x30), v_stack_m128);
    if ((uint8_t)(result) != 0) goto loc_00259712;
    local_r14 = (uint32_t)((local_r14) + 1);
    goto loc_00259672;
loc_002596AF:
    a4 = 0;
    a3 = 0;
    Arg1 = ((uint32_t)((uint32_t)(local_r14)) * 4 + 2) + ((uint32_t)((uint32_t)(local_r14)));
    Arg1 = (Arg1 * 8) + (v_stack_p58);
    result = KiDoesThreadDominateRescheduleContextEntry(Arg1, local_rsi, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00258990;
    local_r14 = (uint32_t)((local_r14) + 1);
    goto loc_00259665;
loc_002596E3:
    result = KiIsPrcbThread(Arg1, local_rsi, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_00258E94;
    if (((*(uint8_t *)(a4 + 0x31)) & (1)) != 0) {
    }
    *(uint8_t *)(arg1 + 0x235) = 1;
    result = KiInsertDeferredReadyList(local_r14 + local_r14 * 4 * 8, Arg1, a3, a4);
    goto loc_00258E94;
loc_00259712:
    goto loc_00258D4E;
loc_0025971C:
    result = KiIsPrcbThread(local_r14 + local_r14 * 4 * 8, Arg1, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_002594F0;
    if (((*(uint8_t *)(a4 + 0x31)) & (1)) != 0) {
    }
    *(uint8_t *)(local_r14 + local_r14 * 4 * 8 + 0x235) = 1;
    result = KiInsertDeferredReadyList(local_r14 + local_r14 * 4 * 8, local_r14 + local_r14 * 4 * 8, a3, a4);
    goto loc_002594F0;
loc_0025974B:
    result = KiIsPrcbThread(local_r14 + local_r14 * 4 * 8, local_r14 + local_r14 * 4 * 8, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_00259579;
    if (((*(uint8_t *)(a4 + 0x31)) & (1)) != 0) {
    }
    *(uint8_t *)(local_r14 + local_r14 * 4 * 8 + 0x235) = 1;
    result = KiInsertDeferredReadyList(local_r14 + local_r14 * 4 * 8, local_r14 + local_r14 * 4 * 8, a3, a4);
    goto loc_00259579;
loc_0025977A:
    result = KiIsPrcbThread(local_r14 + local_r14 * 4 * 8, local_r14 + local_r14 * 4 * 8, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_002595E0;
    if (((*(uint8_t *)(a4 + 0x31)) & (1)) != 0) {
    }
    *(uint8_t *)(local_r14 + local_r14 * 4 * 8 + 0x235) = 1;
    result = KiInsertDeferredReadyList(local_r14 + local_r14 * 4 * 8, local_r14 + local_r14 * 4 * 8, a3, a4);
    goto loc_002595E0;
loc_002597A9:
    result = KiRemoveCurrentlyEnumeratedThreadFromReadyQueue(v_stack_m138, local_rsi, a3, a4);
    a4 = 0;
    *(uint32_t *)(local_rsi + 0x218) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r14 + local_r14 * 4 * 8 + v_stack_p58 * 1 + 0x10) + 0x24)));
    result = KiAddThreadToScbQueue(*(uint64_t *)(local_r14 + local_r14 * 4 * 8 + v_stack_p58 * 1 + 0x10), local_r14, local_rsi, a4);
    if (((*(uint32_t *)(v_rip + 0xD6D33B)) & (0x800ULL)) == 0) goto loc_002586FD;
    a4 = 0;
    result = EtwTraceReadyQueueInsertion(local_rsi, (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r14 + local_r14 * 4 * 8 + v_stack_p58 * 1 + 0x10) + 0x24)), 0 + 2, a4);
    goto loc_002586FD;
loc_002597FC:
    *(uint32_t *)(local_rsi + 0x218) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x24)));
    goto loc_0025948C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00258620&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
