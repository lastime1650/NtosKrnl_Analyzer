# KiSearchForNewThreadsOnTarget

- RVA: `0x0030F500`–`0x003112C6` (길이 `7,622` bytes)
- VA: `0x000000014030F500`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00074118`
- 디코드: `1,737`개 명령, `7,622/7,622` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **105**; 고유 호출 대상: **39**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x0030F55D` → [KiMayStealStandbyThread](KiMayStealStandbyThread_function_0030D704.md) (function, `0x0030D704`)
- `0x0030F6A8` → [KiSendSoftwareInterruptAffinity](KiSendSoftwareInterruptAffinity_function_0030E834.md) (function, `0x0030E834`)
- `0x0030F745` → [KiSendSoftwareInterruptAffinity](KiSendSoftwareInterruptAffinity_function_0030E834.md) (function, `0x0030E834`)
- `0x0030F78F` → [KiDeferredReadySingleThread](../25/KiDeferredReadySingleThread_function_00252FE0.md) (function, `0x00252FE0`)
- `0x0030F7B2` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x0030F7E6` → [KiSendSoftwareInterruptAffinity](KiSendSoftwareInterruptAffinity_function_0030E834.md) (function, `0x0030E834`)
- `0x0030F8CE` → [KiCheckVpBackingLongSpinWaitHypercall](KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0030F8DD` → [HvlNotifyLongSpinWait](HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0030F93A` → [HalpInterruptSendIpi](../25/HalpInterruptSendIpi_function_00252310.md) (function, `0x00252310`)
- `0x0030F98A` → [HalpInterruptSendIpi](../25/HalpInterruptSendIpi_function_00252310.md) (function, `0x00252310`)
- `0x0030F9D3` → [HalpInterruptSendIpi](../25/HalpInterruptSendIpi_function_00252310.md) (function, `0x00252310`)
- `0x0030FA30` → [KiMayStealStandbyThread](KiMayStealStandbyThread_function_0030D704.md) (function, `0x0030D704`)
- `0x0030FA4D` → [KiAttemptToStealStandbyThread](KiAttemptToStealStandbyThread_function_0030D790.md) (function, `0x0030D790`)
- `0x0030FB90` → [KiComputeThreadQos](../25/KiComputeThreadQos_function_00258010.md) (function, `0x00258010`)
- `0x0030FC8C` → [KiComputeThreadQos](../25/KiComputeThreadQos_function_00258010.md) (function, `0x00258010`)
- `0x0030FD79` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0030FD86` → [KiCheckThreadAffinity](../25/KiCheckThreadAffinity_function_00256DD0.md) (function, `0x00256DD0`)
- `0x0030FE17` → [KiRemoveThreadFromReadyQueue](../20/KiRemoveThreadFromReadyQueue_function_002016C8.md) (function, `0x002016C8`)
- `0x0030FE24` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0030FE31` → [KiCheckThreadAffinity](../25/KiCheckThreadAffinity_function_00256DD0.md) (function, `0x00256DD0`)
- `0x0030FE9F` → [KiRemoveCurrentThreadScbReadyQueueEnumerator](../20/KiRemoveCurrentThreadScbReadyQueueEnumerator_function_00201538.md) (function, `0x00201538`)
- `0x0030FEAC` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0030FED1` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0030FF08` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0030FFBC` → [KiTryAcquirePrcbLocksForIsolationUnit](KiTryAcquirePrcbLocksForIsolationUnit_function_0030D598.md) (function, `0x0030D598`)
- `0x0030FFCD` → [KiIsIsolationUnitIdleByHandle](../25/KiIsIsolationUnitIdleByHandle_function_00256C70.md) (function, `0x00256C70`)
- `0x0030FFF5` → [KiIsThreadConstrainedBySchedulingGroup](KiIsThreadConstrainedBySchedulingGroup_function_0030B200.md) (function, `0x0030B200`)
- `0x0030FFFE` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x0031000A` → [KiCheckForMaxOverQuotaScb](../20/KiCheckForMaxOverQuotaScb_function_002027A0.md) (function, `0x002027A0`)
- `0x0031002E` → [KiRemoveThreadFromReadyQueue](../20/KiRemoveThreadFromReadyQueue_function_002016C8.md) (function, `0x002016C8`)
- `0x00310046` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00310055` → [KiStartRescheduleContext](KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x00310072` → [KiScheduleThreadToRescheduleContext](KiScheduleThreadToRescheduleContext_function_0030C2A0.md) (function, `0x0030C2A0`)
- `0x003100C5` → [KiCommitRescheduleContextEntry](KiCommitRescheduleContextEntry_function_0030CFD0.md) (function, `0x0030CFD0`)
- `0x003102A1` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x003102BD` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x0031034C` → [EtwTraceXSchedulerPriorityKickSend](../4F/EtwTraceXSchedulerPriorityKickSend_function_004FB2C0.md) (function, `0x004FB2C0`)
- `0x003103AC` → [KiTryAcquirePrcbLocksForIsolationUnit](KiTryAcquirePrcbLocksForIsolationUnit_function_0030D598.md) (function, `0x0030D598`)
- `0x003103BD` → [KiIsIsolationUnitIdleByHandle](../25/KiIsIsolationUnitIdleByHandle_function_00256C70.md) (function, `0x00256C70`)
- `0x003103E0` → [KiIsThreadConstrainedBySchedulingGroup](KiIsThreadConstrainedBySchedulingGroup_function_0030B200.md) (function, `0x0030B200`)
- `0x003103E9` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x003103F5` → [KiCheckForMaxOverQuotaScb](../20/KiCheckForMaxOverQuotaScb_function_002027A0.md) (function, `0x002027A0`)
- `0x0031040A` → [KiRemoveCurrentThreadScbReadyQueueEnumerator](../20/KiRemoveCurrentThreadScbReadyQueueEnumerator_function_00201538.md) (function, `0x00201538`)
- `0x00310422` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00310431` → [KiStartRescheduleContext](KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x0031044C` → [KiScheduleThreadToRescheduleContext](KiScheduleThreadToRescheduleContext_function_0030C2A0.md) (function, `0x0030C2A0`)
- `0x0031048E` → [KiCommitRescheduleContextEntry](KiCommitRescheduleContextEntry_function_0030CFD0.md) (function, `0x0030CFD0`)
- `0x00310603` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x00310619` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x003106B7` → [EtwTraceXSchedulerPriorityKickSend](../4F/EtwTraceXSchedulerPriorityKickSend_function_004FB2C0.md) (function, `0x004FB2C0`)
- `0x003106D5` → [KiIsThreadConstrainedBySchedulingGroup](KiIsThreadConstrainedBySchedulingGroup_function_0030B200.md) (function, `0x0030B200`)
- `0x003106E2` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x003106FA` → [KiReduceToUnderMaxQuotaSet](../20/KiReduceToUnderMaxQuotaSet_function_00202730.md) (function, `0x00202730`)
- `0x00310719` → [KiIsThreadRankBiased](../4F/KiIsThreadRankBiased_function_004F81BC.md) (function, `0x004F81BC`)
- `0x0031072D` → [KiFindRankBiasedIdleSmtSet](../3F/KiFindRankBiasedIdleSmtSet_function_003FE40C.md) (function, `0x003FE40C`)
- `0x0031073E` → [KiIsThreadConstrainedBySchedulingGroup](KiIsThreadConstrainedBySchedulingGroup_function_0030B200.md) (function, `0x0030B200`)
- `0x0031074B` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x00310763` → [KiReduceToUnderMaxQuotaSet](../20/KiReduceToUnderMaxQuotaSet_function_00202730.md) (function, `0x00202730`)
- `0x0031079D` → [KiDetermineNextScbForScbReadyQueueEnumerator](../25/KiDetermineNextScbForScbReadyQueueEnumerator_function_00256CE8.md) (function, `0x00256CE8`)
- `0x003107F6` → [EtwTraceScheduleThread](EtwTraceScheduleThread_function_0030B74C.md) (function, `0x0030B74C`)
- `0x0031080A` → [EtwTraceScheduleThread](EtwTraceScheduleThread_function_0030B74C.md) (function, `0x0030B74C`)
- `0x00310868` → [KiReadyDeferredReadyList](KiReadyDeferredReadyList_function_0030DD80.md) (function, `0x0030DD80`)
- `0x00310890` → [KiRemoveThreadFromReadyQueue](../20/KiRemoveThreadFromReadyQueue_function_002016C8.md) (function, `0x002016C8`)
- `0x0031089D` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x003108BA` → [KiRemoveCurrentThreadScbReadyQueueEnumerator](../20/KiRemoveCurrentThreadScbReadyQueueEnumerator_function_00201538.md) (function, `0x00201538`)
- `0x003108C7` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x003109FD` → [KiRemoveCurrentThreadScbReadyQueueEnumerator](../20/KiRemoveCurrentThreadScbReadyQueueEnumerator_function_00201538.md) (function, `0x00201538`)
- `0x00310A0A` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x00310A61` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x00310B38` → [KiTryAcquirePrcbLocksForIsolationUnit](KiTryAcquirePrcbLocksForIsolationUnit_function_0030D598.md) (function, `0x0030D598`)
- `0x00310B49` → [KiIsIsolationUnitIdleByHandle](../25/KiIsIsolationUnitIdleByHandle_function_00256C70.md) (function, `0x00256C70`)
- `0x00310B6F` → [KiIsThreadConstrainedBySchedulingGroup](KiIsThreadConstrainedBySchedulingGroup_function_0030B200.md) (function, `0x0030B200`)
- `0x00310B78` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x00310B84` → [KiCheckForMaxOverQuotaScb](../20/KiCheckForMaxOverQuotaScb_function_002027A0.md) (function, `0x002027A0`)
- `0x00310BA9` → [KiRemoveThreadFromSharedReadyQueue](../20/KiRemoveThreadFromSharedReadyQueue_function_002019B0.md) (function, `0x002019B0`)
- `0x00310BC1` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00310BD0` → [KiStartRescheduleContext](KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x00310BEB` → [KiScheduleThreadToRescheduleContext](KiScheduleThreadToRescheduleContext_function_0030C2A0.md) (function, `0x0030C2A0`)
- `0x00310BFE` → [KiCommitRescheduleContext](KiCommitRescheduleContext_function_0030CF20.md) (function, `0x0030CF20`)
- `0x00310C0A` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x00310C9A` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x00310CB0` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x00310D50` → [EtwTraceXSchedulerPriorityKickSend](../4F/EtwTraceXSchedulerPriorityKickSend_function_004FB2C0.md) (function, `0x004FB2C0`)
- `0x00310DE9` → [KiAdvanceReadyListEnumerator](../43/KiAdvanceReadyListEnumerator_function_004366D0.md) (function, `0x004366D0`)
- `0x00310E3D` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x00310E5E` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x00310EA8` → [KiComputeThreadQos](../25/KiComputeThreadQos_function_00258010.md) (function, `0x00258010`)
- `0x00310F37` → [KiCheckThreadAffinity](../25/KiCheckThreadAffinity_function_00256DD0.md) (function, `0x00256DD0`)
- `0x00310FE2` → [KiRemoveCurrentThreadSharedReadyQueueEnumerator](../20/KiRemoveCurrentThreadSharedReadyQueueEnumerator_function_002015B8.md) (function, `0x002015B8`)
- `0x00310FEF` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0031100D` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x0031101A` → [KiIsThreadConstrainedBySchedulingGroup](KiIsThreadConstrainedBySchedulingGroup_function_0030B200.md) (function, `0x0030B200`)
- `0x00311027` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x0031103E` → [KiReduceToUnderMaxQuotaSet](../20/KiReduceToUnderMaxQuotaSet_function_00202730.md) (function, `0x00202730`)
- `0x0031105D` → [KiIsThreadRankBiased](../4F/KiIsThreadRankBiased_function_004F81BC.md) (function, `0x004F81BC`)
- `0x00311071` → [KiFindRankBiasedIdleSmtSet](../3F/KiFindRankBiasedIdleSmtSet_function_003FE40C.md) (function, `0x003FE40C`)
- `0x00311089` → [EtwTraceScheduleThread](EtwTraceScheduleThread_function_0030B74C.md) (function, `0x0030B74C`)
- `0x003110DB` → [KiRemoveThreadFromSharedReadyQueue](../20/KiRemoveThreadFromSharedReadyQueue_function_002019B0.md) (function, `0x002019B0`)
- `0x003110E8` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x00311155` → [KiRemoveThreadFromSharedReadyQueue](../20/KiRemoveThreadFromSharedReadyQueue_function_002019B0.md) (function, `0x002019B0`)
- `0x00311162` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x00311193` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x00311258` → [KiIsThreadRankBiased](../4F/KiIsThreadRankBiased_function_004F81BC.md) (function, `0x004F81BC`)
- `0x00311270` → [KiFindRankBiasedIdleSmtSet](../3F/KiFindRankBiasedIdleSmtSet_function_003FE40C.md) (function, `0x003FE40C`)
- `0x0031129A` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)

### Direct callers
- [KiSearchForNewThreadsWithinSearchContext](../35/KiSearchForNewThreadsWithinSearchContext_function_00353B30.md) at `0x00353C18`

### Static image references
- `0x0030F565` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0030F5EF` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0030F8C0` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0030FA0C` → RVA `0x00F231B8` (`.data`; read)
- `0x0030FBAE` → RVA `0x00FC537C` (`ALMOSTRO`; read)
- `0x0030FC23` → RVA `0x00FC6BF8` (`ALMOSTRO`; read)
- `0x0031007F` → RVA `0x00FC6B14` (`ALMOSTRO`; read)
- `0x00310309` → RVA `0x00FC5007` (`ALMOSTRO`; read)
- `0x003106FF` → RVA `0x00FC6D18` (`ALMOSTRO`; read)
- `0x00310DFF` → RVA `0x00FC6B38` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0031121B` → [sub_006E0EDA](../6E/Unknown_function_006E0EDA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0030F500  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0030F505  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0030F50A  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0030F50F  55                              push rbp
0030F510  56                              push rsi
0030F511  57                              push rdi
0030F512  41 54                           push r12
0030F514  41 55                           push r13
0030F516  41 56                           push r14
0030F518  41 57                           push r15
0030F51A  48 8D AC 24 70 FF FF FF         lea rbp, [rsp - 0x90]
0030F522  48 81 EC 90 01 00 00            sub rsp, 0x190
0030F529  48 8B BD F0 00 00 00            mov rdi, qword ptr [rbp + 0xf0]
0030F530  49 8B F1                        mov rsi, r9
0030F533  4C 8B B5 F8 00 00 00            mov r14, qword ptr [rbp + 0xf8]
0030F53A  49 8B D8                        mov rbx, r8
0030F53D  4C 8B EA                        mov r13, rdx
0030F540  4C 8B E1                        mov r12, rcx
0030F543  48 85 FF                        test rdi, rdi
0030F546  0F 84 97 01 00 00               je 0x14030f6e3
0030F54C  48 3B CF                        cmp rcx, rdi
0030F54F  0F 84 56 1D 00 00               je 0x1403112ab
0030F555  45 33 C0                        xor r8d, r8d
0030F558  33 D2                           xor edx, edx
0030F55A  48 8B CF                        mov rcx, rdi
0030F55D  E8 A2 E1 FF FF                  call 0x14030d704
0030F562  45 33 FF                        xor r15d, r15d
0030F565  4C 8D 05 94 0A CF FF            lea r8, [rip - 0x30f56c]
0030F56C  84 C0                           test al, al
0030F56E  74 10                           je 0x14030f580
0030F570  49 8B 5D 08                     mov rbx, qword ptr [r13 + 8]
0030F574  48 23 DE                        and rbx, rsi
0030F577  48 85 DB                        test rbx, rbx
0030F57A  0F 85 5D 04 00 00               jne 0x14030f9dd
0030F580  0F 57 C0                        xorps xmm0, xmm0
0030F583  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
0030F588  33 C0                           xor eax, eax
0030F58A  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
0030F58F  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
0030F593  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
0030F597  0F 57 C9                        xorps xmm1, xmm1
0030F59A  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0030F59E  8B 87 D8 83 00 00               mov eax, dword ptr [rdi + 0x83d8]
0030F5A4  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
0030F5A8  0F 11 4D 98                     movups xmmword ptr [rbp - 0x68], xmm1
0030F5AC  C6 45 9C 20                     mov byte ptr [rbp - 0x64], 0x20
0030F5B0  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
0030F5B5  C6 44 24 74 20                  mov byte ptr [rsp + 0x74], 0x20
0030F5BA  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
0030F5BF  85 C0                           test eax, eax
0030F5C1  0F 84 20 03 00 00               je 0x14030f8e7
0030F5C7  48 8B DF                        mov rbx, rdi
0030F5CA  41 8B F7                        mov esi, r15d
0030F5CD  48 83 E3 FE                     and rbx, 0xfffffffffffffffe
0030F5D1  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
0030F5D6  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
0030F5E0  F0 48 0F BA 6F 30 00            lock bts qword ptr [rdi + 0x30], 0
0030F5E7  0F 83 27 02 00 00               jae 0x14030f814
0030F5ED  FF C6                           inc esi
0030F5EF  85 35 B7 5C CB 00               test dword ptr [rip + 0xcb5cb7], esi
0030F5F5  0F 84 C5 02 00 00               je 0x14030f8c0
0030F5FB  F3 90                           pause
0030F5FD  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
0030F601  48 85 C0                        test rax, rax
0030F604  74 DA                           je 0x14030f5e0
0030F606  EB E5                           jmp 0x14030f5ed
0030F608  48 8B 95 D8 00 00 00            mov rdx, qword ptr [rbp + 0xd8]
0030F60F  48 81 C7 28 FF FF FF            add rdi, -0xd8
0030F616  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
0030F61A  48 23 CE                        and rcx, rsi
0030F61D  0F 85 37 06 00 00               jne 0x14030fc5a
0030F623  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
0030F628  45 33 FF                        xor r15d, r15d
0030F62B  48 85 DB                        test rbx, rbx
0030F62E  74 52                           je 0x14030f682
0030F630  48 8B CB                        mov rcx, rbx
0030F633  45 8B C7                        mov r8d, r15d
0030F636  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0030F63A  41 8B D7                        mov edx, r15d
0030F63D  48 89 8D 80 00 00 00            mov qword ptr [rbp + 0x80], rcx
0030F644  83 E3 01                        and ebx, 1
0030F647  0F 84 F7 02 00 00               je 0x14030f944
0030F64D  83 FB 01                        cmp ebx, 1
0030F650  75 15                           jne 0x14030f667
0030F652  48 8B 81 58 8E 00 00            mov rax, qword ptr [rcx + 0x8e58]
0030F659  4C 8B 81 58 8E 00 00            mov r8, qword ptr [rcx + 0x8e58]
0030F660  49 83 C0 08                     add r8, 8
0030F664  0F B6 10                        movzx edx, byte ptr [rax]
0030F667  85 D2                           test edx, edx
0030F669  74 17                           je 0x14030f682
0030F66B  BB 01 00 00 00                  mov ebx, 1
0030F670  8D 42 FF                        lea eax, [rdx - 1]
0030F673  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
0030F677  8B D0                           mov edx, eax
0030F679  F0 4C 21 79 30                  lock and qword ptr [rcx + 0x30], r15
0030F67E  85 C0                           test eax, eax
0030F680  75 EE                           jne 0x14030f670
0030F682  41 0F B6 84 24 D9 35 00 00      movzx eax, byte ptr [r12 + 0x35d9]
0030F68B  84 C0                           test al, al
0030F68D  74 42                           je 0x14030f6d1
0030F68F  41 0F B6 94 24 D8 35 00 00      movzx edx, byte ptr [r12 + 0x35d8]
0030F698  3C 01                           cmp al, 1
0030F69A  0F 84 5C 02 00 00               je 0x14030f8fc
0030F6A0  49 8D 8C 24 E0 35 00 00         lea rcx, [r12 + 0x35e0]
0030F6A8  E8 87 F1 FF FF                  call 0x14030e834
0030F6AD  41 80 BC 24 D9 35 00 00 02      cmp byte ptr [r12 + 0x35d9], 2
0030F6B6  0F 84 A1 06 00 00               je 0x14030fd5d
0030F6BC  41 C6 84 24 D9 35 00 00 00      mov byte ptr [r12 + 0x35d9], 0
0030F6C5  41 C7 84 24 DC 35 00 00 FF FF 00 00  mov dword ptr [r12 + 0x35dc], 0xffff
0030F6D1  48 83 7C 24 48 00               cmp qword ptr [rsp + 0x48], 0
0030F6D7  0F 85 83 11 00 00               jne 0x140310860
0030F6DD  E9 C9 1B 00 00                  jmp 0x1403112ab
0030F6E2  CC                              int3
0030F6E3  33 C0                           xor eax, eax
0030F6E5  0F 57 C9                        xorps xmm1, xmm1
0030F6E8  0F 11 4D 00                     movups xmmword ptr [rbp], xmm1
0030F6EC  48 89 45 08                     mov qword ptr [rbp + 8], rax
0030F6F0  45 33 FF                        xor r15d, r15d
0030F6F3  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
0030F6F7  0F 57 C0                        xorps xmm0, xmm0
0030F6FA  BF FE FF FF FF                  mov edi, 0xfffffffe
0030F6FF  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
0030F704  0F 11 4D F0                     movups xmmword ptr [rbp - 0x10], xmm1
0030F708  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
0030F70C  C6 45 FC 20                     mov byte ptr [rbp - 4], 0x20
0030F710  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0030F714  48 85 C7                        test rdi, rax
0030F717  0F 85 DE 1A 00 00               jne 0x1403111fb
0030F71D  49 8D 9C 24 D8 35 00 00         lea rbx, [r12 + 0x35d8]
0030F725  BF 1F 00 00 00                  mov edi, 0x1f
0030F72A  0F B6 43 01                     movzx eax, byte ptr [rbx + 1]
0030F72E  44 8D 77 10                     lea r14d, [rdi + 0x10]
0030F732  84 C0                           test al, al
0030F734  74 31                           je 0x14030f767
0030F736  3C 01                           cmp al, 1
0030F738  0F 84 19 02 00 00               je 0x14030f957
0030F73E  0F B6 13                        movzx edx, byte ptr [rbx]
0030F741  48 8D 4B 08                     lea rcx, [rbx + 8]
0030F745  E8 EA F0 FF FF                  call 0x14030e834
0030F74A  80 7B 01 02                     cmp byte ptr [rbx + 1], 2
0030F74E  0F 84 69 07 00 00               je 0x14030febd
0030F754  C6 43 01 00                     mov byte ptr [rbx + 1], 0
0030F758  C7 43 04 FF FF 00 00            mov dword ptr [rbx + 4], 0xffff
0030F75F  49 8D 9C 24 D8 35 00 00         lea rbx, [r12 + 0x35d8]
0030F767  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0030F76C  48 85 F6                        test rsi, rsi
0030F76F  0F 84 36 1B 00 00               je 0x1403112ab
0030F775  48 8B 06                        mov rax, qword ptr [rsi]
0030F778  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0030F77D  48 8D 96 28 FF FF FF            lea rdx, [rsi - 0xd8]
0030F784  45 33 C9                        xor r9d, r9d
0030F787  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
0030F78C  49 8B CC                        mov rcx, r12
0030F78F  E8 4C 38 F4 FF                  call 0x140252fe0
0030F794  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0030F799  41 FF C7                        inc r15d
0030F79C  48 85 F6                        test rsi, rsi
0030F79F  74 08                           je 0x14030f7a9
0030F7A1  48 8B 06                        mov rax, qword ptr [rsi]
0030F7A4  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0030F7A9  41 F6 C7 0F                     test r15b, 0xf
0030F7AD  75 08                           jne 0x14030f7b7
0030F7AF  48 8B CB                        mov rcx, rbx
0030F7B2  E8 49 2A F4 FF                  call 0x140252200
0030F7B7  48 85 F6                        test rsi, rsi
0030F7BA  75 C1                           jne 0x14030f77d
0030F7BC  41 0F B6 84 24 D9 35 00 00      movzx eax, byte ptr [r12 + 0x35d9]
0030F7C5  84 C0                           test al, al
0030F7C7  0F 84 DE 1A 00 00               je 0x1403112ab
0030F7CD  3C 01                           cmp al, 1
0030F7CF  0F 84 BF 01 00 00               je 0x14030f994
0030F7D5  41 0F B6 94 24 D8 35 00 00      movzx edx, byte ptr [r12 + 0x35d8]
0030F7DE  49 8D 8C 24 E0 35 00 00         lea rcx, [r12 + 0x35e0]
0030F7E6  E8 49 F0 FF FF                  call 0x14030e834
0030F7EB  41 80 BC 24 D9 35 00 00 02      cmp byte ptr [r12 + 0x35d9], 2
0030F7F4  0F 84 F2 06 00 00               je 0x14030feec
0030F7FA  41 C6 84 24 D9 35 00 00 00      mov byte ptr [r12 + 0x35d9], 0
0030F803  41 C7 84 24 DC 35 00 00 FF FF 00 00  mov dword ptr [r12 + 0x35dc], 0xffff
0030F80F  E9 97 1A 00 00                  jmp 0x1403112ab
0030F814  8B 87 D8 83 00 00               mov eax, dword ptr [rdi + 0x83d8]
0030F81A  48 8D 97 40 84 00 00            lea rdx, [rdi + 0x8440]
0030F821  48 89 55 A8                     mov qword ptr [rbp - 0x58], rdx
0030F825  48 89 7D 90                     mov qword ptr [rbp - 0x70], rdi
0030F829  89 45 98                        mov dword ptr [rbp - 0x68], eax
0030F82C  85 C0                           test eax, eax
0030F82E  0F 84 A7 06 00 00               je 0x14030fedb
0030F834  44 0F BD F0                     bsr r14d, eax
0030F838  41 8B F6                        mov esi, r14d
0030F83B  48 C1 E6 04                     shl rsi, 4
0030F83F  48 03 F2                        add rsi, rdx
0030F842  44 89 75 2C                     mov dword ptr [rbp + 0x2c], r14d
0030F846  48 89 75 A0                     mov qword ptr [rbp - 0x60], rsi
0030F84A  44 88 75 9C                     mov byte ptr [rbp - 0x64], r14b
0030F84E  4C 89 7D C0                     mov qword ptr [rbp - 0x40], r15
0030F852  41 8B C7                        mov eax, r15d
0030F855  4D 8B C7                        mov r8, r15
0030F858  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0030F85D  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
0030F861  83 F8 40                        cmp eax, 0x40
0030F864  0F 83 04 02 00 00               jae 0x14030fa6e
0030F86A  4C 89 7D 88                     mov qword ptr [rbp - 0x78], r15
0030F86E  48 85 F6                        test rsi, rsi
0030F871  0F 84 F7 01 00 00               je 0x14030fa6e
0030F877  4C 8B 2E                        mov r13, qword ptr [rsi]
0030F87A  41 0F B6 C6                     movzx eax, r14b
0030F87E  48 C1 E0 04                     shl rax, 4
0030F882  48 03 C2                        add rax, rdx
0030F885  4C 89 6D A0                     mov qword ptr [rbp - 0x60], r13
0030F889  4C 3B E8                        cmp r13, rax
0030F88C  0F 85 E5 01 00 00               jne 0x14030fa77
0030F892  8B 4D 98                        mov ecx, dword ptr [rbp - 0x68]
0030F895  41 0F B6 C6                     movzx eax, r14b
0030F899  0F B3 C1                        btr ecx, eax
0030F89C  89 4D 98                        mov dword ptr [rbp - 0x68], ecx
0030F89F  85 C9                           test ecx, ecx
0030F8A1  0F 84 BF 01 00 00               je 0x14030fa66
0030F8A7  0F BD C1                        bsr eax, ecx
0030F8AA  0F B6 F0                        movzx esi, al
0030F8AD  44 0F B6 F0                     movzx r14d, al
0030F8B1  48 C1 E6 04                     shl rsi, 4
0030F8B5  48 03 F2                        add rsi, rdx
0030F8B8  89 45 30                        mov dword ptr [rbp + 0x30], eax
0030F8BB  88 45 9C                        mov byte ptr [rbp - 0x64], al
0030F8BE  EB B7                           jmp 0x14030f877
0030F8C0  8B 05 F2 71 CB 00               mov eax, dword ptr [rip + 0xcb71f2]
0030F8C6  A8 40                           test al, 0x40
0030F8C8  0F 84 2D FD FF FF               je 0x14030f5fb
0030F8CE  E8 BD FB FF FF                  call 0x14030f490
0030F8D3  84 C0                           test al, al
0030F8D5  0F 84 20 FD FF FF               je 0x14030f5fb
0030F8DB  8B CE                           mov ecx, esi
0030F8DD  E8 7E FB FF FF                  call 0x14030f460
0030F8E2  E9 16 FD FF FF                  jmp 0x14030f5fd
0030F8E7  48 8B 87 30 84 00 00            mov rax, qword ptr [rdi + 0x8430]
0030F8EE  48 85 C0                        test rax, rax
0030F8F1  0F 84 8B FD FF FF               je 0x14030f682
0030F8F7  E9 CB FC FF FF                  jmp 0x14030f5c7
0030F8FC  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0030F905  BF 1F 00 00 00                  mov edi, 0x1f
0030F90A  41 8B 8C 24 DC 35 00 00         mov ecx, dword ptr [r12 + 0x35dc]
0030F912  41 BE 2F 00 00 00               mov r14d, 0x2f
0030F918  89 4D 18                        mov dword ptr [rbp + 0x18], ecx
0030F91B  48 8D 4D 10                     lea rcx, [rbp + 0x10]
0030F91F  48 C7 45 10 06 00 00 00         mov qword ptr [rbp + 0x10], 6
0030F927  FF 80 D4 8E 00 00               inc dword ptr [rax + 0x8ed4]
0030F92D  80 FA 01                        cmp dl, 1
0030F930  4C 89 7D 1C                     mov qword ptr [rbp + 0x1c], r15
0030F934  41 0F 45 FE                     cmovne edi, r14d
0030F938  8B D7                           mov edx, edi
0030F93A  E8 D1 29 F4 FF                  call 0x140252310
0030F93F  E9 69 FD FF FF                  jmp 0x14030f6ad
0030F944  BB 01 00 00 00                  mov ebx, 1
0030F949  4C 8D 85 80 00 00 00            lea r8, [rbp + 0x80]
0030F950  8B D3                           mov edx, ebx
0030F952  E9 19 FD FF FF                  jmp 0x14030f670
0030F957  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0030F960  8B D7                           mov edx, edi
0030F962  8B 4B 04                        mov ecx, dword ptr [rbx + 4]
0030F965  44 0F B6 03                     movzx r8d, byte ptr [rbx]
0030F969  89 4D 18                        mov dword ptr [rbp + 0x18], ecx
0030F96C  48 8D 4D 10                     lea rcx, [rbp + 0x10]
0030F970  FF 80 D4 8E 00 00               inc dword ptr [rax + 0x8ed4]
0030F976  41 80 F8 01                     cmp r8b, 1
0030F97A  48 C7 45 10 06 00 00 00         mov qword ptr [rbp + 0x10], 6
0030F982  4C 89 7D 1C                     mov qword ptr [rbp + 0x1c], r15
0030F986  41 0F 45 D6                     cmovne edx, r14d
0030F98A  E8 81 29 F4 FF                  call 0x140252310
0030F98F  E9 B6 FD FF FF                  jmp 0x14030f74a
0030F994  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0030F99D  41 8B 8C 24 DC 35 00 00         mov ecx, dword ptr [r12 + 0x35dc]
0030F9A5  45 0F B6 84 24 D8 35 00 00      movzx r8d, byte ptr [r12 + 0x35d8]
0030F9AE  89 4D 18                        mov dword ptr [rbp + 0x18], ecx
0030F9B1  48 8D 4D 10                     lea rcx, [rbp + 0x10]
0030F9B5  FF 80 D4 8E 00 00               inc dword ptr [rax + 0x8ed4]
0030F9BB  33 C0                           xor eax, eax
0030F9BD  41 80 F8 01                     cmp r8b, 1
0030F9C1  48 C7 45 10 06 00 00 00         mov qword ptr [rbp + 0x10], 6
0030F9C9  48 89 45 1C                     mov qword ptr [rbp + 0x1c], rax
0030F9CD  41 0F 45 FE                     cmovne edi, r14d
0030F9D1  8B D7                           mov edx, edi
0030F9D3  E8 38 29 F4 FF                  call 0x140252310
0030F9D8  E9 0E FE FF FF                  jmp 0x14030f7eb
0030F9DD  41 0F B6 8C 24 D1 00 00 00      movzx ecx, byte ptr [r12 + 0xd1]
0030F9E6  48 8B C3                        mov rax, rbx
0030F9E9  48 D3 C8                        ror rax, cl
0030F9EC  48 0F BC C0                     bsf rax, rax
0030F9F0  89 45 28                        mov dword ptr [rbp + 0x28], eax
0030F9F3  8D 14 01                        lea edx, [rcx + rax]
0030F9F6  41 0F B7 8D 88 00 00 00         movzx ecx, word ptr [r13 + 0x88]
0030F9FE  83 E2 3F                        and edx, 0x3f
0030FA01  C1 E1 06                        shl ecx, 6
0030FA04  8B C2                           mov eax, edx
0030FA06  03 CA                           add ecx, edx
0030FA08  48 0F B3 C3                     btr rbx, rax
0030FA0C  48 8B 05 A5 37 C1 00            mov rax, qword ptr [rip + 0xc137a5]
0030FA13  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
0030FA16  49 8B B4 C8 40 8C FC 00         mov rsi, qword ptr [r8 + rcx*8 + 0xfc8c40]
0030FA1E  48 3B FE                        cmp rdi, rsi
0030FA21  0F 84 50 FB FF FF               je 0x14030f577
0030FA27  45 33 C0                        xor r8d, r8d
0030FA2A  48 8B D6                        mov rdx, rsi
0030FA2D  48 8B CF                        mov rcx, rdi
0030FA30  E8 CF DC FF FF                  call 0x14030d704
0030FA35  4C 8D 05 C4 05 CF FF            lea r8, [rip - 0x30fa3c]
0030FA3C  84 C0                           test al, al
0030FA3E  0F 84 33 FB FF FF               je 0x14030f577
0030FA44  4C 8B C6                        mov r8, rsi
0030FA47  48 8B D7                        mov rdx, rdi
0030FA4A  49 8B CC                        mov rcx, r12
0030FA4D  E8 3E DD FF FF                  call 0x14030d790
0030FA52  4C 8D 05 A7 05 CF FF            lea r8, [rip - 0x30fa59]
0030FA59  84 C0                           test al, al
0030FA5B  0F 85 1F FB FF FF               jne 0x14030f580
0030FA61  E9 11 FB FF FF                  jmp 0x14030f577
0030FA66  C6 45 9C 00                     mov byte ptr [rbp - 0x64], 0
0030FA6A  4C 89 7D A0                     mov qword ptr [rbp - 0x60], r15
0030FA6E  48 8B B5 E0 00 00 00            mov rsi, qword ptr [rbp + 0xe0]
0030FA75  EB 25                           jmp 0x14030fa9c
0030FA77  4C 8B B5 D8 00 00 00            mov r14, qword ptr [rbp + 0xd8]
0030FA7E  4D 8D BD 28 FF FF FF            lea r15, [r13 - 0xd8]
0030FA85  48 8B B5 E0 00 00 00            mov rsi, qword ptr [rbp + 0xe0]
0030FA8C  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
0030FA90  48 23 CE                        and rcx, rsi
0030FA93  0F 85 C4 00 00 00               jne 0x14030fb5d
0030FA99  45 33 FF                        xor r15d, r15d
0030FA9C  48 8D 87 30 84 00 00            lea rax, [rdi + 0x8430]
0030FAA3  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
0030FAA8  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0030FAAC  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
0030FAB1  F6 C1 01                        test cl, 1
0030FAB4  0F 85 58 04 00 00               jne 0x14030ff12
0030FABA  48 8B C1                        mov rax, rcx
0030FABD  48 85 C0                        test rax, rax
0030FAC0  0F 85 62 04 00 00               jne 0x14030ff28
0030FAC6  4C 8B 5D 80                     mov r11, qword ptr [rbp - 0x80]
0030FACA  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
0030FACF  44 0F B6 54 24 74               movzx r10d, byte ptr [rsp + 0x74]
0030FAD5  4C 89 7D C8                     mov qword ptr [rbp - 0x38], r15
0030FAD9  45 8B EF                        mov r13d, r15d
0030FADC  44 89 BD F0 00 00 00            mov dword ptr [rbp + 0xf0], r15d
0030FAE3  BB 02 00 00 00                  mov ebx, 2
0030FAE8  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0030FAED  45 33 F6                        xor r14d, r14d
0030FAF0  41 83 FD 40                     cmp r13d, 0x40
0030FAF4  0F 83 29 FB FF FF               jae 0x14030f623
0030FAFA  48 83 7C 24 68 00               cmp qword ptr [rsp + 0x68], 0
0030FB00  0F 84 1D FB FF FF               je 0x14030f623
0030FB06  4D 85 C9                        test r9, r9
0030FB09  0F 84 89 0C 00 00               je 0x140310798
0030FB0F  49 8B 39                        mov rdi, qword ptr [r9]
0030FB12  41 0F B6 C2                     movzx eax, r10b
0030FB16  48 C1 E0 04                     shl rax, 4
0030FB1A  49 03 C3                        add rax, r11
0030FB1D  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
0030FB22  48 3B F8                        cmp rdi, rax
0030FB25  0F 85 DD FA FF FF               jne 0x14030f608
0030FB2B  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
0030FB2F  41 0F B6 C2                     movzx eax, r10b
0030FB33  0F B3 C1                        btr ecx, eax
0030FB36  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
0030FB3A  85 C9                           test ecx, ecx
0030FB3C  0F 84 46 0C 00 00               je 0x140310788
0030FB42  0F BD C1                        bsr eax, ecx
0030FB45  44 0F B6 C8                     movzx r9d, al
0030FB49  44 0F B6 D0                     movzx r10d, al
0030FB4D  49 C1 E1 04                     shl r9, 4
0030FB51  4D 03 CB                        add r9, r11
0030FB54  89 45 44                        mov dword ptr [rbp + 0x44], eax
0030FB57  88 44 24 74                     mov byte ptr [rsp + 0x74], al
0030FB5B  EB B2                           jmp 0x14030fb0f
0030FB5D  49 8B C0                        mov rax, r8
0030FB60  48 F7 D0                        not rax
0030FB63  48 23 C1                        and rax, rcx
0030FB66  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0030FB6A  0F 84 29 FF FF FF               je 0x14030fa99
0030FB70  49 8B 8F 40 02 00 00            mov rcx, qword ptr [r15 + 0x240]
0030FB77  41 0F B7 86 88 00 00 00         movzx eax, word ptr [r14 + 0x88]
0030FB7F  66 3B 01                        cmp ax, word ptr [rcx]
0030FB82  0F 83 CA 0D 00 00               jae 0x140310952
0030FB88  48 8B 74 C1 08                  mov rsi, qword ptr [rcx + rax*8 + 8]
0030FB8D  49 8B CF                        mov rcx, r15
0030FB90  E8 7B 84 F4 FF                  call 0x140258010
0030FB95  45 8B 47 50                     mov r8d, dword ptr [r15 + 0x50]
0030FB99  41 8B 4F 54                     mov ecx, dword ptr [r15 + 0x54]
0030FB9D  44 3B C1                        cmp r8d, ecx
0030FBA0  44 0F 46 C1                     cmovbe r8d, ecx
0030FBA4  41 0F B6 8F 05 02 00 00         movzx ecx, byte ptr [r15 + 0x205]
0030FBAC  33 D2                           xor edx, edx
0030FBAE  44 3B 05 C7 57 CB 00            cmp r8d, dword ptr [rip + 0xcb57c7]
0030FBB5  0F 93 C2                        setae dl
0030FBB8  44 8D 04 42                     lea r8d, [rdx + rax*2]
0030FBBC  41 0F B6 86 B9 00 00 00         movzx eax, byte ptr [r14 + 0xb9]
0030FBC4  44 0F AF C0                     imul r8d, eax
0030FBC8  49 8B 86 C0 00 00 00            mov rax, qword ptr [r14 + 0xc0]
0030FBCF  44 03 C1                        add r8d, ecx
0030FBD2  4B 8D 0C 40                     lea rcx, [r8 + r8*2]
0030FBD6  48 8D 14 C8                     lea rdx, [rax + rcx*8]
0030FBDA  48 8B 4C C8 10                  mov rcx, qword ptr [rax + rcx*8 + 0x10]
0030FBDF  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0030FBE3  48 8B 02                        mov rax, qword ptr [rdx]
0030FBE6  48 8B C6                        mov rax, rsi
0030FBE9  48 23 C1                        and rax, rcx
0030FBEC  48 0F 45 F0                     cmovne rsi, rax
0030FBF0  41 8B 47 78                     mov eax, dword ptr [r15 + 0x78]
0030FBF4  48 D1 E8                        shr rax, 1
0030FBF7  83 E0 01                        and eax, 1
0030FBFA  49 8B 4C C6 10                  mov rcx, qword ptr [r14 + rax*8 + 0x10]
0030FBFF  4D 8B 47 68                     mov r8, qword ptr [r15 + 0x68]
0030FC03  48 23 CE                        and rcx, rsi
0030FC06  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0030FC0A  48 23 F1                        and rsi, rcx
0030FC0D  48 89 75 88                     mov qword ptr [rbp - 0x78], rsi
0030FC11  4D 85 C0                        test r8, r8
0030FC14  0F 85 B8 0A 00 00               jne 0x1403106d2
0030FC1A  48 85 F6                        test rsi, rsi
0030FC1D  0F 85 60 01 00 00               jne 0x14030fd83
0030FC23  48 8B 05 CE 6F CB 00            mov rax, qword ptr [rip + 0xcb6fce]
0030FC2A  44 0F B6 75 9C                  movzx r14d, byte ptr [rbp - 0x64]
0030FC2F  49 39 87 38 02 00 00            cmp qword ptr [r15 + 0x238], rax
0030FC36  0F 85 36 0C 00 00               jne 0x140310872
0030FC3C  48 8B 75 A0                     mov rsi, qword ptr [rbp - 0x60]
0030FC40  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
0030FC44  48 8D 97 40 84 00 00            lea rdx, [rdi + 0x8440]
0030FC4B  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
0030FC50  FF C0                           inc eax
0030FC52  45 33 FF                        xor r15d, r15d
0030FC55  E9 03 FC FF FF                  jmp 0x14030f85d
0030FC5A  49 8B C7                        mov rax, r15
0030FC5D  48 F7 D0                        not rax
0030FC60  48 23 C1                        and rax, rcx
0030FC63  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
0030FC67  0F 84 B6 F9 FF FF               je 0x14030f623
0030FC6D  48 8B 8F 40 02 00 00            mov rcx, qword ptr [rdi + 0x240]
0030FC74  0F B7 82 88 00 00 00            movzx eax, word ptr [rdx + 0x88]
0030FC7B  66 3B 01                        cmp ax, word ptr [rcx]
0030FC7E  0F 83 D5 0C 00 00               jae 0x140310959
0030FC84  48 8B 74 C1 08                  mov rsi, qword ptr [rcx + rax*8 + 8]
0030FC89  48 8B CF                        mov rcx, rdi
0030FC8C  E8 7F 83 F4 FF                  call 0x140258010
0030FC91  44 8B 47 50                     mov r8d, dword ptr [rdi + 0x50]
0030FC95  41 8B D6                        mov edx, r14d
0030FC98  8B 4F 54                        mov ecx, dword ptr [rdi + 0x54]
0030FC9B  44 3B C1                        cmp r8d, ecx
0030FC9E  4C 8B 8D D8 00 00 00            mov r9, qword ptr [rbp + 0xd8]
0030FCA5  44 0F 46 C1                     cmovbe r8d, ecx
0030FCA9  0F B6 8F 05 02 00 00            movzx ecx, byte ptr [rdi + 0x205]
0030FCB0  44 3B 05 C5 56 CB 00            cmp r8d, dword ptr [rip + 0xcb56c5]
0030FCB7  0F 93 C2                        setae dl
0030FCBA  44 8D 04 42                     lea r8d, [rdx + rax*2]
0030FCBE  41 0F B6 81 B9 00 00 00         movzx eax, byte ptr [r9 + 0xb9]
0030FCC6  44 0F AF C0                     imul r8d, eax
0030FCCA  49 8B 81 C0 00 00 00            mov rax, qword ptr [r9 + 0xc0]
0030FCD1  44 03 C1                        add r8d, ecx
0030FCD4  4B 8D 0C 40                     lea rcx, [r8 + r8*2]
0030FCD8  48 8D 14 C8                     lea rdx, [rax + rcx*8]
0030FCDC  48 8B 4C C8 10                  mov rcx, qword ptr [rax + rcx*8 + 0x10]
0030FCE1  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0030FCE5  48 8B 02                        mov rax, qword ptr [rdx]
0030FCE8  48 8B C6                        mov rax, rsi
0030FCEB  48 23 C1                        and rax, rcx
0030FCEE  48 0F 45 F0                     cmovne rsi, rax
0030FCF2  8B 47 78                        mov eax, dword ptr [rdi + 0x78]
0030FCF5  48 D1 E8                        shr rax, 1
0030FCF8  83 E0 01                        and eax, 1
0030FCFB  49 8B 4C C1 10                  mov rcx, qword ptr [r9 + rax*8 + 0x10]
0030FD00  4C 8B 47 68                     mov r8, qword ptr [rdi + 0x68]
0030FD04  48 23 CE                        and rcx, rsi
0030FD07  48 8B 75 B0                     mov rsi, qword ptr [rbp - 0x50]
0030FD0B  48 23 F1                        and rsi, rcx
0030FD0E  48 89 75 B0                     mov qword ptr [rbp - 0x50], rsi
0030FD12  4D 85 C0                        test r8, r8
0030FD15  0F 85 20 0A 00 00               jne 0x14031073b
0030FD1B  48 85 F6                        test rsi, rsi
0030FD1E  0F 85 0A 01 00 00               jne 0x14030fe2e
0030FD24  48 8B 05 CD 6E CB 00            mov rax, qword ptr [rip + 0xcb6ecd]
0030FD2B  48 39 87 38 02 00 00            cmp qword ptr [rdi + 0x238], rax
0030FD32  0F 85 6F 0B 00 00               jne 0x1403108a7
0030FD38  41 FF C5                        inc r13d
0030FD3B  44 89 AD F0 00 00 00            mov dword ptr [rbp + 0xf0], r13d
0030FD42  44 0F B6 54 24 74               movzx r10d, byte ptr [rsp + 0x74]
0030FD48  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
0030FD4D  4C 8B 5D 80                     mov r11, qword ptr [rbp - 0x80]
0030FD51  48 8B B5 E0 00 00 00            mov rsi, qword ptr [rbp + 0xe0]
0030FD58  E9 93 FD FF FF                  jmp 0x14030faf0
0030FD5D  49 8D 8C 24 E8 35 00 00         lea rcx, [r12 + 0x35e8]
0030FD65  49 C7 84 24 E0 35 00 00 01 00 20 00  mov qword ptr [r12 + 0x35e0], 0x200001
0030FD71  33 D2                           xor edx, edx
0030FD73  41 B8 00 01 00 00               mov r8d, 0x100
0030FD79  E8 C2 6E 3B 00                  call 0x1406c6c40
0030FD7E  E9 39 F9 FF FF                  jmp 0x14030f6bc
0030FD83  49 8B CF                        mov rcx, r15
0030FD86  E8 45 70 F4 FF                  call 0x140256dd0
0030FD8B  85 C0                           test eax, eax
0030FD8D  0F 84 CE 0B 00 00               je 0x140310961
0030FD93  4C 8B F6                        mov r14, rsi
0030FD96  4D 85 F6                        test r14, r14
0030FD99  0F 85 CE 01 00 00               jne 0x14030ff6d
0030FD9F  48 85 F6                        test rsi, rsi
0030FDA2  0F 84 29 0B 00 00               je 0x1403108d1
0030FDA8  48 8B 85 D8 00 00 00            mov rax, qword ptr [rbp + 0xd8]
0030FDAF  48 0F BD D6                     bsr rdx, rsi
0030FDB3  0F B7 88 88 00 00 00            movzx ecx, word ptr [rax + 0x88]
0030FDBA  48 8B 05 F7 33 C1 00            mov rax, qword ptr [rip + 0xc133f7]
0030FDC1  C1 E1 06                        shl ecx, 6
0030FDC4  03 CA                           add ecx, edx
0030FDC6  44 89 75 3C                     mov dword ptr [rbp + 0x3c], r14d
0030FDCA  89 55 3C                        mov dword ptr [rbp + 0x3c], edx
0030FDCD  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
0030FDD0  48 8D 0D 29 02 CF FF            lea rcx, [rip - 0x30fdd7]
0030FDD7  48 8B 8C C1 40 8C FC 00         mov rcx, qword ptr [rcx + rax*8 + 0xfc8c40]
0030FDDF  41 8B 47 78                     mov eax, dword ptr [r15 + 0x78]
0030FDE3  A8 02                           test al, 2
0030FDE5  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0030FDEA  0F 84 24 0C 00 00               je 0x140310a14
0030FDF0  48 0B 81 60 8E 00 00            or rax, qword ptr [rcx + 0x8e60]
0030FDF7  49 8D 97 D8 00 00 00            lea rdx, [r15 + 0xd8]
0030FDFE  49 8B 75 08                     mov rsi, qword ptr [r13 + 8]
0030FE02  44 0F B6 75 9C                  movzx r14d, byte ptr [rbp - 0x64]
0030FE07  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0030FE0B  45 8B C6                        mov r8d, r14d
0030FE0E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0030FE13  48 89 75 A0                     mov qword ptr [rbp - 0x60], rsi
0030FE17  E8 AC 18 EF FF                  call 0x1402016c8
0030FE1C  49 8B D7                        mov rdx, r15
0030FE1F  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0030FE24  E8 E7 14 EF FF                  call 0x140201310
0030FE29  E9 0C 04 00 00                  jmp 0x14031023a
0030FE2E  48 8B CF                        mov rcx, rdi
0030FE31  E8 9A 6F F4 FF                  call 0x140256dd0
0030FE36  85 C0                           test eax, eax
0030FE38  0F 84 77 0B 00 00               je 0x1403109b5
0030FE3E  4C 8B F6                        mov r14, rsi
0030FE41  4D 85 F6                        test r14, r14
0030FE44  0F 85 1F 05 00 00               jne 0x140310369
0030FE4A  48 85 F6                        test rsi, rsi
0030FE4D  0F 84 A5 0A 00 00               je 0x1403108f8
0030FE53  41 0F B7 89 88 00 00 00         movzx ecx, word ptr [r9 + 0x88]
0030FE5B  48 8B 05 56 33 C1 00            mov rax, qword ptr [rip + 0xc13356]
0030FE62  C1 E1 06                        shl ecx, 6
0030FE65  48 0F BD D6                     bsr rdx, rsi
0030FE69  03 CA                           add ecx, edx
0030FE6B  89 55 54                        mov dword ptr [rbp + 0x54], edx
0030FE6E  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
0030FE71  48 8D 0D 88 01 CF FF            lea rcx, [rip - 0x30fe78]
0030FE78  48 8B 8C C1 40 8C FC 00         mov rcx, qword ptr [rcx + rax*8 + 0xfc8c40]
0030FE80  8B 47 78                        mov eax, dword ptr [rdi + 0x78]
0030FE83  84 C3                           test bl, al
0030FE85  0F 84 95 0B 00 00               je 0x140310a20
0030FE8B  4C 0B B9 60 8E 00 00            or r15, qword ptr [rcx + 0x8e60]
0030FE92  48 8B D7                        mov rdx, rdi
0030FE95  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0030FE9A  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0030FE9F  E8 94 16 EF FF                  call 0x140201538
0030FEA4  48 8B D7                        mov rdx, rdi
0030FEA7  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0030FEAC  E8 5F 14 EF FF                  call 0x140201310
0030FEB1  44 8B AD F0 00 00 00            mov r13d, dword ptr [rbp + 0xf0]
0030FEB8  E9 85 FE FF FF                  jmp 0x14030fd42
0030FEBD  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0030FEC1  48 C7 43 08 01 00 20 00         mov qword ptr [rbx + 8], 0x200001
0030FEC9  33 D2                           xor edx, edx
0030FECB  41 B8 00 01 00 00               mov r8d, 0x100
0030FED1  E8 6A 6D 3B 00                  call 0x1406c6c40
0030FED6  E9 79 F8 FF FF                  jmp 0x14030f754
0030FEDB  44 0F B6 75 9C                  movzx r14d, byte ptr [rbp - 0x64]
0030FEE0  49 8B F7                        mov rsi, r15
0030FEE3  4C 89 7D A0                     mov qword ptr [rbp - 0x60], r15
0030FEE7  E9 62 F9 FF FF                  jmp 0x14030f84e
0030FEEC  49 8D 8C 24 E8 35 00 00         lea rcx, [r12 + 0x35e8]
0030FEF4  49 C7 84 24 E0 35 00 00 01 00 20 00  mov qword ptr [r12 + 0x35e0], 0x200001
0030FF00  33 D2                           xor edx, edx
0030FF02  41 B8 00 01 00 00               mov r8d, 0x100
0030FF08  E8 33 6D 3B 00                  call 0x1406c6c40
0030FF0D  E9 E8 F8 FF FF                  jmp 0x14030f7fa
0030FF12  48 83 F9 01                     cmp rcx, 1
0030FF16  0F 84 AA FB FF FF               je 0x14030fac6
0030FF1C  48 83 C8 01                     or rax, 1
0030FF20  48 33 C1                        xor rax, rcx
0030FF23  E9 95 FB FF FF                  jmp 0x14030fabd
0030FF28  0F B7 48 20                     movzx ecx, word ptr [rax + 0x20]
0030FF2C  48 83 C0 A8                     add rax, -0x58
0030FF30  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0030FF35  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
0030FF39  4C 8D 98 90 00 00 00            lea r11, [rax + 0x90]
0030FF40  4C 89 5D 80                     mov qword ptr [rbp - 0x80], r11
0030FF44  85 C9                           test ecx, ecx
0030FF46  0F 84 F9 09 00 00               je 0x140310945
0030FF4C  44 0F BD D1                     bsr r10d, ecx
0030FF50  45 8B CA                        mov r9d, r10d
0030FF53  49 C1 E1 04                     shl r9, 4
0030FF57  4D 03 CB                        add r9, r11
0030FF5A  44 89 55 40                     mov dword ptr [rbp + 0x40], r10d
0030FF5E  4C 89 4C 24 78                  mov qword ptr [rsp + 0x78], r9
0030FF63  44 88 54 24 74                  mov byte ptr [rsp + 0x74], r10b
0030FF68  E9 68 FB FF FF                  jmp 0x14030fad5
0030FF6D  48 8B 85 D8 00 00 00            mov rax, qword ptr [rbp + 0xd8]
0030FF74  4C 8D 45 C0                     lea r8, [rbp - 0x40]
0030FF78  49 0F BD D6                     bsr rdx, r14
0030FF7C  0F B7 88 88 00 00 00            movzx ecx, word ptr [rax + 0x88]
0030FF83  48 8B 05 2E 32 C1 00            mov rax, qword ptr [rip + 0xc1322e]
0030FF8A  C1 E1 06                        shl ecx, 6
0030FF8D  03 CA                           add ecx, edx
0030FF8F  C7 45 38 00 00 00 00            mov dword ptr [rbp + 0x38], 0
0030FF96  89 55 38                        mov dword ptr [rbp + 0x38], edx
0030FF99  41 8B 57 78                     mov edx, dword ptr [r15 + 0x78]
0030FF9D  D1 EA                           shr edx, 1
0030FF9F  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
0030FFA2  83 E2 01                        and edx, 1
0030FFA5  48 8D 0D 54 00 CF FF            lea rcx, [rip - 0x30ffac]
0030FFAC  48 8B 84 C1 40 8C FC 00         mov rax, qword ptr [rcx + rax*8 + 0xfc8c40]
0030FFB4  48 8B C8                        mov rcx, rax
0030FFB7  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0030FFBC  E8 D7 D5 FF FF                  call 0x14030d598
0030FFC1  84 C0                           test al, al
0030FFC3  0F 84 67 08 00 00               je 0x140310830
0030FFC9  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0030FFCD  E8 9E 6C F4 FF                  call 0x140256c70
0030FFD2  85 C0                           test eax, eax
0030FFD4  0F 84 6A 0A 00 00               je 0x140310a44
0030FFDA  49 8B 47 68                     mov rax, qword ptr [r15 + 0x68]
0030FFDE  48 85 C0                        test rax, rax
0030FFE1  74 34                           je 0x140310017
0030FFE3  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
0030FFE8  49 8B CF                        mov rcx, r15
0030FFEB  44 8B 82 D8 00 00 00            mov r8d, dword ptr [rdx + 0xd8]
0030FFF2  4C 03 C0                        add r8, rax
0030FFF5  E8 06 B2 FF FF                  call 0x14030b200
0030FFFA  84 C0                           test al, al
0030FFFC  74 19                           je 0x140310017
0030FFFE  E8 0D 63 04 00                  call 0x140356310
00310003  84 C0                           test al, al
00310005  75 10                           jne 0x140310017
00310007  49 8B C8                        mov rcx, r8
0031000A  E8 91 27 EF FF                  call 0x1402027a0
0031000F  84 C0                           test al, al
00310011  0F 85 2B 12 00 00               jne 0x140311242
00310017  49 8B 75 08                     mov rsi, qword ptr [r13 + 8]
0031001B  49 8B D5                        mov rdx, r13
0031001E  44 0F B6 75 9C                  movzx r14d, byte ptr [rbp - 0x64]
00310023  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00310027  45 8B C6                        mov r8d, r14d
0031002A  48 89 75 A0                     mov qword ptr [rbp - 0x60], rsi
0031002E  E8 95 16 EF FF                  call 0x1402016c8
00310033  4D 8B AC 24 E8 37 00 00         mov r13, qword ptr [r12 + 0x37e8]
0031003B  33 D2                           xor edx, edx
0031003D  49 8B CD                        mov rcx, r13
00310040  41 B8 F0 00 00 00               mov r8d, 0xf0
00310046  E8 F5 6B 3B 00                  call 0x1406c6c40
0031004B  45 33 C0                        xor r8d, r8d
0031004E  48 8D 55 C0                     lea rdx, [rbp - 0x40]
00310052  49 8B CD                        mov rcx, r13
00310055  E8 56 C6 FF FF                  call 0x14030c6b0
0031005A  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
0031005F  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00310064  45 33 C9                        xor r9d, r9d
00310067  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0031006C  49 8B D7                        mov rdx, r15
0031006F  49 8B CD                        mov rcx, r13
00310072  E8 29 C2 FF FF                  call 0x14030c2a0
00310077  BA 00 00 00 00                  mov edx, 0
0031007C  45 32 D2                        xor r10b, r10b
0031007F  F7 05 8B 6A CB 00 00 04 00 00   test dword ptr [rip + 0xcb6a8b], 0x400
00310089  8B C2                           mov eax, edx
0031008B  B9 02 00 00 00                  mov ecx, 2
00310090  44 8B FA                        mov r15d, edx
00310093  0F 45 C1                        cmovne eax, ecx
00310096  41 38 55 00                     cmp byte ptr [r13], dl
0031009A  76 48                           jbe 0x1403100e4
0031009C  8B F8                           mov edi, eax
0031009E  0F B6 DA                        movzx ebx, dl
003100A1  41 8B C7                        mov eax, r15d
003100A4  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
003100A9  44 8B C7                        mov r8d, edi
003100AC  49 8B D4                        mov rdx, r12
003100AF  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
003100B7  48 03 C8                        add rcx, rax
003100BA  48 8D 0C CD 00 00 00 00         lea rcx, [rcx*8]
003100C2  49 03 CD                        add rcx, r13
003100C5  E8 06 CF FF FF                  call 0x14030cfd0
003100CA  0A D8                           or bl, al
003100CC  41 FF C7                        inc r15d
003100CF  41 0F B6 45 00                  movzx eax, byte ptr [r13]
003100D4  44 3B F8                        cmp r15d, eax
003100D7  72 C8                           jb 0x1403100a1
003100D9  48 8B BD F0 00 00 00            mov rdi, qword ptr [rbp + 0xf0]
003100E0  44 0F B6 D3                     movzx r10d, bl
003100E4  41 83 7D 08 01                  cmp dword ptr [r13 + 8], 1
003100E9  75 1C                           jne 0x140310107
003100EB  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
003100EF  48 8B 88 58 8E 00 00            mov rcx, qword ptr [rax + 0x8e58]
003100F6  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
003100FA  FE C0                           inc al
003100FC  88 41 01                        mov byte ptr [rcx + 1], al
003100FF  3A 01                           cmp al, byte ptr [rcx]
00310101  72 04                           jb 0x140310107
00310103  C6 41 01 00                     mov byte ptr [rcx + 1], 0
00310107  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
0031010B  45 33 FF                        xor r15d, r15d
0031010E  4C 8B C8                        mov r9, rax
00310111  45 8B C7                        mov r8d, r15d
00310114  49 83 E1 FE                     and r9, 0xfffffffffffffffe
00310118  41 8B D7                        mov edx, r15d
0031011B  4C 89 4D 70                     mov qword ptr [rbp + 0x70], r9
0031011F  83 E0 01                        and eax, 1
00310122  0F 84 EC 06 00 00               je 0x140310814
00310128  83 F8 01                        cmp eax, 1
0031012B  75 15                           jne 0x140310142
0031012D  49 8B 81 58 8E 00 00            mov rax, qword ptr [r9 + 0x8e58]
00310134  4D 8B 81 58 8E 00 00            mov r8, qword ptr [r9 + 0x8e58]
0031013B  49 83 C0 08                     add r8, 8
0031013F  0F B6 10                        movzx edx, byte ptr [rax]
00310142  85 D2                           test edx, edx
00310144  74 25                           je 0x14031016b
00310146  0F 1F 40 00                     nop dword ptr [rax]
0031014A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
00310150  8D 42 FF                        lea eax, [rdx - 1]
00310153  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
00310157  8B D0                           mov edx, eax
00310159  F0 4C 21 79 30                  lock and qword ptr [rcx + 0x30], r15
0031015E  85 C0                           test eax, eax
00310160  75 EE                           jne 0x140310150
00310162  48 8B 75 A0                     mov rsi, qword ptr [rbp - 0x60]
00310166  44 0F B6 75 9C                  movzx r14d, byte ptr [rbp - 0x64]
0031016B  4C 89 7D C0                     mov qword ptr [rbp - 0x40], r15
0031016F  45 84 D2                        test r10b, r10b
00310172  0F 84 B8 07 00 00               je 0x140310930
00310178  45 38 7D 00                     cmp byte ptr [r13], r15b
0031017C  0F 86 AE 07 00 00               jbe 0x140310930
00310182  BB 02 00 00 00                  mov ebx, 2
00310187  48 8D 3D 72 FE CE FF            lea rdi, [rip - 0x31018e]
0031018E  66 90                           nop
00310190  41 8B C7                        mov eax, r15d
00310193  48 8D 0C 80                     lea rcx, [rax + rax*4]
00310197  48 8D 34 CD 00 00 00 00         lea rsi, [rcx*8]
0031019F  49 03 F5                        add rsi, r13
003101A2  0F B6 46 33                     movzx eax, byte ptr [rsi + 0x33]
003101A6  4C 8B 76 10                     mov r14, qword ptr [rsi + 0x10]
003101AA  A8 10                           test al, 0x10
003101AC  0F 85 A0 00 00 00               jne 0x140310252
003101B2  A8 08                           test al, 8
003101B4  74 2E                           je 0x1403101e4
003101B6  90                              nop
003101B7  41 80 7E 07 00                  cmp byte ptr [r14 + 7], 0
003101BC  74 26                           je 0x1403101e4
003101BE  41 0F B6 84 24 D9 35 00 00      movzx eax, byte ptr [r12 + 0x35d9]
003101C7  84 C0                           test al, al
003101C9  0F 85 AC 00 00 00               jne 0x14031027b
003101CF  41 C6 84 24 D9 35 00 00 01      mov byte ptr [r12 + 0x35d9], 1
003101D8  41 8B 46 24                     mov eax, dword ptr [r14 + 0x24]
003101DC  41 89 84 24 DC 35 00 00         mov dword ptr [r12 + 0x35dc], eax
003101E4  84 5E 33                        test byte ptr [rsi + 0x33], bl
003101E7  0F 85 FF 05 00 00               jne 0x1403107ec
003101ED  F6 46 33 04                     test byte ptr [rsi + 0x33], 4
003101F1  74 14                           je 0x140310207
003101F3  49 8B 86 B8 8E 00 00            mov rax, qword ptr [r14 + 0x8eb8]
003101FA  0F BE 4E 34                     movsx ecx, byte ptr [rsi + 0x34]
003101FE  48 85 C0                        test rax, rax
00310201  0F 85 C0 00 00 00               jne 0x1403102c7
00310207  F6 46 33 01                     test byte ptr [rsi + 0x33], 1
0031020B  74 0C                           je 0x140310219
0031020D  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00310211  66 F0 FF 88 64 03 00 00         lock dec word ptr [rax + 0x364]
00310219  41 0F B6 45 00                  movzx eax, byte ptr [r13]
0031021E  41 FF C7                        inc r15d
00310221  44 3B F8                        cmp r15d, eax
00310224  0F 82 66 FF FF FF               jb 0x140310190
0031022A  48 8B BD F0 00 00 00            mov rdi, qword ptr [rbp + 0xf0]
00310231  48 8B 75 A0                     mov rsi, qword ptr [rbp - 0x60]
00310235  44 0F B6 75 9C                  movzx r14d, byte ptr [rbp - 0x64]
0031023A  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
0031023E  48 8D 97 40 84 00 00            lea rdx, [rdi + 0x8440]
00310245  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
0031024A  45 33 FF                        xor r15d, r15d
0031024D  E9 0F F6 FF FF                  jmp 0x14030f861
00310252  41 0F B6 84 24 D9 35 00 00      movzx eax, byte ptr [r12 + 0x35d9]
0031025B  84 C0                           test al, al
0031025D  0F 84 6C FF FF FF               je 0x1403101cf
00310263  3C 01                           cmp al, 1
00310265  75 3F                           jne 0x1403102a6
00310267  41 8B 94 24 DC 35 00 00         mov edx, dword ptr [r12 + 0x35dc]
0031026F  41 3B 56 24                     cmp edx, dword ptr [r14 + 0x24]
00310273  0F 84 6B FF FF FF               je 0x1403101e4
00310279  EB 16                           jmp 0x140310291
0031027B  3C 01                           cmp al, 1
0031027D  75 27                           jne 0x1403102a6
0031027F  41 8B 94 24 DC 35 00 00         mov edx, dword ptr [r12 + 0x35dc]
00310287  41 3B 56 24                     cmp edx, dword ptr [r14 + 0x24]
0031028B  0F 84 53 FF FF FF               je 0x1403101e4
00310291  49 8D 8C 24 E0 35 00 00         lea rcx, [r12 + 0x35e0]
00310299  41 88 9C 24 D9 35 00 00         mov byte ptr [r12 + 0x35d9], bl
003102A1  E8 4A B4 F4 FF                  call 0x14025b6f0
003102A6  4D 8B 86 C8 00 00 00            mov r8, qword ptr [r14 + 0xc8]
003102AD  49 8D 8C 24 E0 35 00 00         lea rcx, [r12 + 0x35e0]
003102B5  41 0F B6 96 D0 00 00 00         movzx edx, byte ptr [r14 + 0xd0]
003102BD  E8 FE B3 F4 FF                  call 0x14025b6c0
003102C2  E9 1D FF FF FF                  jmp 0x1403101e4
003102C7  49 83 BC 24 B8 8E 00 00 00      cmp qword ptr [r12 + 0x8eb8], 0
003102D0  0F 84 31 FF FF FF               je 0x140310207
003102D6  4D 3B E6                        cmp r12, r14
003102D9  0F 84 28 FF FF FF               je 0x140310207
003102DF  44 8B 00                        mov r8d, dword ptr [rax]
003102E2  45 8B C8                        mov r9d, r8d
003102E5  49 8D 84 24 B8 8E 00 00         lea rax, [r12 + 0x8eb8]
003102ED  41 81 E1 00 00 04 00            and r9d, 0x40000
003102F4  74 08                           je 0x1403102fe
003102F6  49 8D 84 24 B8 8E 00 00         lea rax, [r12 + 0x8eb8]
003102FE  41 0F BA E0 14                  bt r8d, 0x14
00310303  0F 83 AE 0E 00 00               jae 0x1403111b7
00310309  80 3D F7 4C CB 00 00            cmp byte ptr [rip + 0xcb4cf7], 0
00310310  48 8B 10                        mov rdx, qword ptr [rax]
00310313  89 5A 0C                        mov dword ptr [rdx + 0xc], ebx
00310316  41 8B 4E 24                     mov ecx, dword ptr [r14 + 0x24]
0031031A  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
0031031E  75 19                           jne 0x140310339
00310320  0F B6 84 4F 61 D2 FC 00         movzx eax, byte ptr [rdi + rcx*2 + 0xfcd261]
00310328  0F B6 8C 4F 60 D2 FC 00         movzx ecx, byte ptr [rdi + rcx*2 + 0xfcd260]
00310330  C1 E1 06                        shl ecx, 6
00310333  0B C8                           or ecx, eax
00310335  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00310339  89 4A 08                        mov dword ptr [rdx + 8], ecx
0031033C  8B 05 D2 67 CB 00               mov eax, dword ptr [rip + 0xcb67d2]
00310342  A8 20                           test al, 0x20
00310344  74 0F                           je 0x140310355
00310346  41 8B 4E 24                     mov ecx, dword ptr [r14 + 0x24]
0031034A  8B D3                           mov edx, ebx
0031034C  E8 6F AF 1E 00                  call 0x1404fb2c0
00310351  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
00310355  8B D1                           mov edx, ecx
00310357  8B C1                           mov eax, ecx
00310359  B9 C2 00 00 40                  mov ecx, 0x400000c2
0031035E  48 C1 EA 20                     shr rdx, 0x20
00310362  0F 30                           wrmsr
00310364  E9 9E FE FF FF                  jmp 0x140310207
00310369  41 0F B7 89 88 00 00 00         movzx ecx, word ptr [r9 + 0x88]
00310371  4C 8D 45 C8                     lea r8, [rbp - 0x38]
00310375  48 8B 05 3C 2E C1 00            mov rax, qword ptr [rip + 0xc12e3c]
0031037C  C1 E1 06                        shl ecx, 6
0031037F  49 0F BD D6                     bsr rdx, r14
00310383  C7 45 50 00 00 00 00            mov dword ptr [rbp + 0x50], 0
0031038A  03 CA                           add ecx, edx
0031038C  89 55 50                        mov dword ptr [rbp + 0x50], edx
0031038F  8B 57 78                        mov edx, dword ptr [rdi + 0x78]
00310392  D1 EA                           shr edx, 1
00310394  83 E2 01                        and edx, 1
00310397  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
0031039A  48 8D 0D 5F FC CE FF            lea rcx, [rip - 0x3103a1]
003103A1  4C 8B AC C1 40 8C FC 00         mov r13, qword ptr [rcx + rax*8 + 0xfc8c40]
003103A9  49 8B CD                        mov rcx, r13
003103AC  E8 E7 D1 FF FF                  call 0x14030d598
003103B1  84 C0                           test al, al
003103B3  0F 84 8E 04 00 00               je 0x140310847
003103B9  48 8D 4D C8                     lea rcx, [rbp - 0x38]
003103BD  E8 AE 68 F4 FF                  call 0x140256c70
003103C2  85 C0                           test eax, eax
003103C4  0F 84 B8 0E 00 00               je 0x140311282
003103CA  48 8B 47 68                     mov rax, qword ptr [rdi + 0x68]
003103CE  48 85 C0                        test rax, rax
003103D1  74 2F                           je 0x140310402
003103D3  41 8B 95 D8 00 00 00            mov edx, dword ptr [r13 + 0xd8]
003103DA  48 8B CF                        mov rcx, rdi
003103DD  48 03 D0                        add rdx, rax
003103E0  E8 1B AE FF FF                  call 0x14030b200
003103E5  84 C0                           test al, al
003103E7  74 19                           je 0x140310402
003103E9  E8 22 5F 04 00                  call 0x140356310
003103EE  84 C0                           test al, al
003103F0  75 10                           jne 0x140310402
003103F2  48 8B CA                        mov rcx, rdx
003103F5  E8 A6 23 EF FF                  call 0x1402027a0
003103FA  84 C0                           test al, al
003103FC  0F 85 7C 0E 00 00               jne 0x14031127e
00310402  48 8B D7                        mov rdx, rdi
00310405  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0031040A  E8 29 11 EF FF                  call 0x140201538
0031040F  4D 8B BC 24 E8 37 00 00         mov r15, qword ptr [r12 + 0x37e8]
00310417  33 D2                           xor edx, edx
00310419  49 8B CF                        mov rcx, r15
0031041C  41 B8 F0 00 00 00               mov r8d, 0xf0
00310422  E8 19 68 3B 00                  call 0x1406c6c40
00310427  45 33 C0                        xor r8d, r8d
0031042A  48 8D 55 C8                     lea rdx, [rbp - 0x38]
0031042E  49 8B CF                        mov rcx, r15
00310431  E8 7A C2 FF FF                  call 0x14030c6b0
00310436  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0031043B  45 33 C9                        xor r9d, r9d
0031043E  4D 8B C5                        mov r8, r13
00310441  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00310446  48 8B D7                        mov rdx, rdi
00310449  49 8B CF                        mov rcx, r15
0031044C  E8 4F BE FF FF                  call 0x14030c2a0
00310451  41 BA 00 00 00 00               mov r10d, 0
00310457  45 32 F6                        xor r14b, r14b
0031045A  F7 05 B0 66 CB 00 00 04 00 00   test dword ptr [rip + 0xcb66b0], 0x400
00310464  41 8B F2                        mov esi, r10d
00310467  41 8B FA                        mov edi, r10d
0031046A  0F 45 F3                        cmovne esi, ebx
0031046D  45 38 17                        cmp byte ptr [r15], r10b
00310470  76 31                           jbe 0x1403104a3
00310472  8B C7                           mov eax, edi
00310474  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
00310479  44 8B C6                        mov r8d, esi
0031047C  49 8B D4                        mov rdx, r12
0031047F  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
00310487  48 03 C8                        add rcx, rax
0031048A  49 8D 0C CF                     lea rcx, [r15 + rcx*8]
0031048E  E8 3D CB FF FF                  call 0x14030cfd0
00310493  44 0A F0                        or r14b, al
00310496  FF C7                           inc edi
00310498  41 0F B6 07                     movzx eax, byte ptr [r15]
0031049C  3B F8                           cmp edi, eax
0031049E  72 D2                           jb 0x140310472
003104A0  45 33 D2                        xor r10d, r10d
003104A3  41 83 7F 08 01                  cmp dword ptr [r15 + 8], 1
003104A8  75 1C                           jne 0x1403104c6
003104AA  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
003104AE  48 8B 88 58 8E 00 00            mov rcx, qword ptr [rax + 0x8e58]
003104B5  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
003104B9  FE C0                           inc al
003104BB  88 41 01                        mov byte ptr [rcx + 1], al
003104BE  3A 01                           cmp al, byte ptr [rcx]
003104C0  72 04                           jb 0x1403104c6
003104C2  C6 41 01 00                     mov byte ptr [rcx + 1], 0
003104C6  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
003104CA  4D 8B C2                        mov r8, r10
003104CD  4C 8B C8                        mov r9, rax
003104D0  41 8B D2                        mov edx, r10d
003104D3  49 83 E1 FE                     and r9, 0xfffffffffffffffe
003104D7  4C 89 4D 78                     mov qword ptr [rbp + 0x78], r9
003104DB  83 E0 01                        and eax, 1
003104DE  0F 84 3E 03 00 00               je 0x140310822
003104E4  83 F8 01                        cmp eax, 1
003104E7  75 15                           jne 0x1403104fe
003104E9  49 8B 81 58 8E 00 00            mov rax, qword ptr [r9 + 0x8e58]
003104F0  4D 8B 81 58 8E 00 00            mov r8, qword ptr [r9 + 0x8e58]
003104F7  49 83 C0 08                     add r8, 8
003104FB  0F B6 10                        movzx edx, byte ptr [rax]
003104FE  85 D2                           test edx, edx
00310500  74 21                           je 0x140310523
00310502  0F 1F 40 00                     nop dword ptr [rax]
00310506  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
00310510  8D 42 FF                        lea eax, [rdx - 1]
00310513  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
00310517  8B D0                           mov edx, eax
00310519  F0 48 83 61 30 00               lock and qword ptr [rcx + 0x30], 0
0031051F  85 C0                           test eax, eax
00310521  75 ED                           jne 0x140310510
00310523  4C 89 55 C8                     mov qword ptr [rbp - 0x38], r10
00310527  45 84 F6                        test r14b, r14b
0031052A  0F 84 9B 00 00 00               je 0x1403105cb
00310530  41 80 3F 00                     cmp byte ptr [r15], 0
00310534  45 8B F2                        mov r14d, r10d
00310537  0F 86 8E 00 00 00               jbe 0x1403105cb
0031053D  0F 1F 00                        nop dword ptr [rax]
00310540  41 8B C6                        mov eax, r14d
00310543  48 8D 0C 80                     lea rcx, [rax + rax*4]
00310547  41 0F B6 44 CF 33               movzx eax, byte ptr [r15 + rcx*8 + 0x33]
0031054D  49 8B 74 CF 10                  mov rsi, qword ptr [r15 + rcx*8 + 0x10]
00310552  49 8D 3C CF                     lea rdi, [r15 + rcx*8]
00310556  A8 10                           test al, 0x10
00310558  75 0B                           jne 0x140310565
0031055A  A8 08                           test al, 8
0031055C  74 28                           je 0x140310586
0031055E  90                              nop
0031055F  80 7E 07 00                     cmp byte ptr [rsi + 7], 0
00310563  74 21                           je 0x140310586
00310565  41 0F B6 84 24 D9 35 00 00      movzx eax, byte ptr [r12 + 0x35d9]
0031056E  84 C0                           test al, al
00310570  75 6D                           jne 0x1403105df
00310572  41 C6 84 24 D9 35 00 00 01      mov byte ptr [r12 + 0x35d9], 1
0031057B  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
0031057E  41 89 84 24 DC 35 00 00         mov dword ptr [r12 + 0x35dc], eax
00310586  84 5F 33                        test byte ptr [rdi + 0x33], bl
00310589  0F 85 71 02 00 00               jne 0x140310800
0031058F  F6 47 33 04                     test byte ptr [rdi + 0x33], 4
00310593  74 14                           je 0x1403105a9
00310595  48 8B 86 B8 8E 00 00            mov rax, qword ptr [rsi + 0x8eb8]
0031059C  0F BE 4F 34                     movsx ecx, byte ptr [rdi + 0x34]
003105A0  48 85 C0                        test rax, rax
003105A3  0F 85 84 00 00 00               jne 0x14031062d
003105A9  F6 47 33 01                     test byte ptr [rdi + 0x33], 1
003105AD  74 0C                           je 0x1403105bb
003105AF  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
003105B3  66 F0 FF 88 64 03 00 00         lock dec word ptr [rax + 0x364]
003105BB  41 0F B6 07                     movzx eax, byte ptr [r15]
003105BF  41 FF C6                        inc r14d
003105C2  44 3B F0                        cmp r14d, eax
003105C5  0F 82 75 FF FF FF               jb 0x140310540
003105CB  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
003105D0  45 33 F6                        xor r14d, r14d
003105D3  44 8B AD F0 00 00 00            mov r13d, dword ptr [rbp + 0xf0]
003105DA  E9 63 F7 FF FF                  jmp 0x14030fd42
003105DF  3C 01                           cmp al, 1
003105E1  75 40                           jne 0x140310623
003105E3  41 8B 94 24 DC 35 00 00         mov edx, dword ptr [r12 + 0x35dc]
003105EB  3B 56 24                        cmp edx, dword ptr [rsi + 0x24]
003105EE  74 96                           je 0x140310586
003105F0  4D 8D AC 24 E0 35 00 00         lea r13, [r12 + 0x35e0]
003105F8  41 88 9C 24 D9 35 00 00         mov byte ptr [r12 + 0x35d9], bl
00310600  49 8B CD                        mov rcx, r13
00310603  E8 E8 B0 F4 FF                  call 0x14025b6f0
00310608  4C 8B 86 C8 00 00 00            mov r8, qword ptr [rsi + 0xc8]
0031060F  49 8B CD                        mov rcx, r13
00310612  0F B6 96 D0 00 00 00            movzx edx, byte ptr [rsi + 0xd0]
00310619  E8 A2 B0 F4 FF                  call 0x14025b6c0
0031061E  E9 63 FF FF FF                  jmp 0x140310586
00310623  4D 8D AC 24 E0 35 00 00         lea r13, [r12 + 0x35e0]
0031062B  EB DB                           jmp 0x140310608
0031062D  49 83 BC 24 B8 8E 00 00 00      cmp qword ptr [r12 + 0x8eb8], 0
00310636  0F 84 6D FF FF FF               je 0x1403105a9
0031063C  4C 3B E6                        cmp r12, rsi
0031063F  0F 84 64 FF FF FF               je 0x1403105a9
00310645  44 8B 00                        mov r8d, dword ptr [rax]
00310648  45 8B C8                        mov r9d, r8d
0031064B  49 8D 84 24 B8 8E 00 00         lea rax, [r12 + 0x8eb8]
00310653  41 81 E1 00 00 04 00            and r9d, 0x40000
0031065A  74 08                           je 0x140310664
0031065C  49 8D 84 24 B8 8E 00 00         lea rax, [r12 + 0x8eb8]
00310664  41 0F BA E0 14                  bt r8d, 0x14
00310669  0F 83 6A 0B 00 00               jae 0x1403111d9
0031066F  80 3D 91 49 CB 00 00            cmp byte ptr [rip + 0xcb4991], 0
00310676  48 8B 08                        mov rcx, qword ptr [rax]
00310679  89 59 0C                        mov dword ptr [rcx + 0xc], ebx
0031067C  44 8B 6E 24                     mov r13d, dword ptr [rsi + 0x24]
00310680  75 22                           jne 0x1403106a4
00310682  41 8B C5                        mov eax, r13d
00310685  48 8D 15 74 F9 CE FF            lea rdx, [rip - 0x31068c]
0031068C  46 0F B6 AC 6A 60 D2 FC 00      movzx r13d, byte ptr [rdx + r13*2 + 0xfcd260]
00310695  41 C1 E5 06                     shl r13d, 6
00310699  0F B6 84 42 61 D2 FC 00         movzx eax, byte ptr [rdx + rax*2 + 0xfcd261]
003106A1  44 0B E8                        or r13d, eax
003106A4  44 89 69 08                     mov dword ptr [rcx + 8], r13d
003106A8  8B 05 66 64 CB 00               mov eax, dword ptr [rip + 0xcb6466]
003106AE  A8 20                           test al, 0x20
003106B0  74 0A                           je 0x1403106bc
003106B2  8B 4E 24                        mov ecx, dword ptr [rsi + 0x24]
003106B5  8B D3                           mov edx, ebx
003106B7  E8 04 AC 1E 00                  call 0x1404fb2c0
003106BC  41 8B D5                        mov edx, r13d
003106BF  B9 C2 00 00 40                  mov ecx, 0x400000c2
003106C4  48 C1 EA 20                     shr rdx, 0x20
003106C8  41 8B C5                        mov eax, r13d
003106CB  0F 30                           wrmsr
003106CD  E9 D7 FE FF FF                  jmp 0x1403105a9
003106D2  49 8B CF                        mov rcx, r15
003106D5  E8 26 AB FF FF                  call 0x14030b200
003106DA  84 C0                           test al, al
003106DC  0F 84 38 F5 FF FF               je 0x14030fc1a
003106E2  E8 29 5C 04 00                  call 0x140356310
003106E7  84 C0                           test al, al
003106E9  0F 85 2B F5 FF FF               jne 0x14030fc1a
003106EF  41 0F B7 8E 88 00 00 00         movzx ecx, word ptr [r14 + 0x88]
003106F7  48 8B D6                        mov rdx, rsi
003106FA  E8 31 20 EF FF                  call 0x140202730
003106FF  83 3D 12 66 CB 00 00            cmp dword ptr [rip + 0xcb6612], 0
00310706  48 8B F0                        mov rsi, rax
00310709  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0031070D  0F 84 07 F5 FF FF               je 0x14030fc1a
00310713  49 8B D4                        mov rdx, r12
00310716  49 8B CF                        mov rcx, r15
00310719  E8 9E 7A 1E 00                  call 0x1404f81bc
0031071E  84 C0                           test al, al
00310720  0F 84 F4 F4 FF FF               je 0x14030fc1a
00310726  48 8D 55 88                     lea rdx, [rbp - 0x78]
0031072A  49 8B CE                        mov rcx, r14
0031072D  E8 DA DC 0E 00                  call 0x1403fe40c
00310732  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
00310736  E9 DF F4 FF FF                  jmp 0x14030fc1a
0031073B  48 8B CF                        mov rcx, rdi
0031073E  E8 BD AA FF FF                  call 0x14030b200
00310743  84 C0                           test al, al
00310745  0F 84 D0 F5 FF FF               je 0x14030fd1b
0031074B  E8 C0 5B 04 00                  call 0x140356310
00310750  84 C0                           test al, al
00310752  0F 85 C3 F5 FF FF               jne 0x14030fd1b
00310758  41 0F B7 89 88 00 00 00         movzx ecx, word ptr [r9 + 0x88]
00310760  48 8B D6                        mov rdx, rsi
00310763  E8 C8 1F EF FF                  call 0x140202730
00310768  83 3D A9 65 CB 00 00            cmp dword ptr [rip + 0xcb65a9], 0
0031076F  48 8B F0                        mov rsi, rax
00310772  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00310776  0F 85 D6 0A 00 00               jne 0x140311252
0031077C  4C 8B 8D D8 00 00 00            mov r9, qword ptr [rbp + 0xd8]
00310783  E9 93 F5 FF FF                  jmp 0x14030fd1b
00310788  45 32 D2                        xor r10b, r10b
0031078B  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
00310790  44 88 54 24 74                  mov byte ptr [rsp + 0x74], r10b
00310795  4D 8B CE                        mov r9, r14
00310798  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0031079D  E8 46 65 F4 FF                  call 0x140256ce8
003107A2  48 8B C8                        mov rcx, rax
003107A5  48 85 C0                        test rax, rax
003107A8  74 38                           je 0x1403107e2
003107AA  4C 8D 98 90 00 00 00            lea r11, [rax + 0x90]
003107B1  0F B7 40 78                     movzx eax, word ptr [rax + 0x78]
003107B5  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
003107B9  4C 89 5D 80                     mov qword ptr [rbp - 0x80], r11
003107BD  85 C0                           test eax, eax
003107BF  0F 84 45 01 00 00               je 0x14031090a
003107C5  0F BD C0                        bsr eax, eax
003107C8  44 8B C8                        mov r9d, eax
003107CB  44 0F B6 D0                     movzx r10d, al
003107CF  49 C1 E1 04                     shl r9, 4
003107D3  4D 03 CB                        add r9, r11
003107D6  89 45 48                        mov dword ptr [rbp + 0x48], eax
003107D9  4C 89 4C 24 78                  mov qword ptr [rsp + 0x78], r9
003107DE  88 44 24 74                     mov byte ptr [rsp + 0x74], al
003107E2  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
003107E7  E9 0E F3 FF FF                  jmp 0x14030fafa
003107EC  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
003107F0  45 33 C0                        xor r8d, r8d
003107F3  49 8B D6                        mov rdx, r14
003107F6  E8 51 AF FF FF                  call 0x14030b74c
003107FB  E9 ED F9 FF FF                  jmp 0x1403101ed
00310800  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
00310804  45 33 C0                        xor r8d, r8d
00310807  48 8B D6                        mov rdx, rsi
0031080A  E8 3D AF FF FF                  call 0x14030b74c
0031080F  E9 7B FD FF FF                  jmp 0x14031058f
00310814  4C 8D 45 70                     lea r8, [rbp + 0x70]
00310818  BA 01 00 00 00                  mov edx, 1
0031081D  E9 2E F9 FF FF                  jmp 0x140310150
00310822  4C 8D 45 78                     lea r8, [rbp + 0x78]
00310826  BA 01 00 00 00                  mov edx, 1
0031082B  E9 E0 FC FF FF                  jmp 0x140310510
00310830  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00310835  49 8B 80 C8 00 00 00            mov rax, qword ptr [r8 + 0xc8]
0031083C  48 F7 D0                        not rax
0031083F  4C 23 F0                        and r14, rax
00310842  E9 4F F5 FF FF                  jmp 0x14030fd96
00310847  49 8B 85 C8 00 00 00            mov rax, qword ptr [r13 + 0xc8]
0031084E  4C 8B 8D D8 00 00 00            mov r9, qword ptr [rbp + 0xd8]
00310855  48 F7 D0                        not rax
00310858  4C 23 F0                        and r14, rax
0031085B  E9 E1 F5 FF FF                  jmp 0x14030fe41
00310860  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00310865  49 8B CC                        mov rcx, r12
00310868  E8 13 D5 FF FF                  call 0x14030dd80
0031086D  E9 39 0A 00 00                  jmp 0x1403112ab
00310872  41 8B 47 74                     mov eax, dword ptr [r15 + 0x74]
00310876  A8 08                           test al, 8
00310878  0F 85 BE F3 FF FF               jne 0x14030fc3c
0031087E  49 8B 75 08                     mov rsi, qword ptr [r13 + 8]
00310882  45 8B C6                        mov r8d, r14d
00310885  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00310889  49 8B D5                        mov rdx, r13
0031088C  48 89 75 A0                     mov qword ptr [rbp - 0x60], rsi
00310890  E8 33 0E EF FF                  call 0x1402016c8
00310895  49 8B D7                        mov rdx, r15
00310898  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0031089D  E8 6E 0A EF FF                  call 0x140201310
003108A2  E9 99 F3 FF FF                  jmp 0x14030fc40
003108A7  8B 47 74                        mov eax, dword ptr [rdi + 0x74]
003108AA  A8 08                           test al, 8
003108AC  0F 85 86 F4 FF FF               jne 0x14030fd38
003108B2  48 8B D7                        mov rdx, rdi
003108B5  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
003108BA  E8 79 0C EF FF                  call 0x140201538
003108BF  48 8B D7                        mov rdx, rdi
003108C2  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
003108C7  E8 44 0A EF FF                  call 0x140201310
003108CC  E9 67 F4 FF FF                  jmp 0x14030fd38
003108D1  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
003108D5  48 8D 97 40 84 00 00            lea rdx, [rdi + 0x8440]
003108DC  48 8B 75 A0                     mov rsi, qword ptr [rbp - 0x60]
003108E0  FF C0                           inc eax
003108E2  44 0F B6 75 9C                  movzx r14d, byte ptr [rbp - 0x64]
003108E7  45 33 FF                        xor r15d, r15d
003108EA  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
003108EF  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
003108F3  E9 69 EF FF FF                  jmp 0x14030f861
003108F8  44 8B AD F0 00 00 00            mov r13d, dword ptr [rbp + 0xf0]
003108FF  41 FF C5                        inc r13d
00310902  45 33 F6                        xor r14d, r14d
00310905  E9 31 F4 FF FF                  jmp 0x14030fd3b
0031090A  41 B2 20                        mov r10b, 0x20
0031090D  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
00310912  44 88 54 24 74                  mov byte ptr [rsp + 0x74], r10b
00310917  4D 8B CE                        mov r9, r14
0031091A  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
0031091F  E9 D6 F1 FF FF                  jmp 0x14030fafa
00310924  0F 1F 40 00                     nop dword ptr [rax]
00310928  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00310930  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
00310935  48 8D 97 40 84 00 00            lea rdx, [rdi + 0x8440]
0031093C  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
00310940  E9 1C EF FF FF                  jmp 0x14030f861
00310945  4D 8B CF                        mov r9, r15
00310948  4C 89 7C 24 78                  mov qword ptr [rsp + 0x78], r15
0031094D  E9 7D F1 FF FF                  jmp 0x14030facf
00310952  33 F6                           xor esi, esi
00310954  E9 34 F2 FF FF                  jmp 0x14030fb8d
00310959  49 8B F6                        mov rsi, r14
0031095C  E9 28 F3 FF FF                  jmp 0x14030fc89
00310961  41 0F B7 8E 88 00 00 00         movzx ecx, word ptr [r14 + 0x88]
00310969  48 8B 05 48 28 C1 00            mov rax, qword ptr [rip + 0xc12848]
00310970  C1 E1 06                        shl ecx, 6
00310973  48 0F BD D6                     bsr rdx, rsi
00310977  C7 45 34 00 00 00 00            mov dword ptr [rbp + 0x34], 0
0031097E  03 CA                           add ecx, edx
00310980  89 55 34                        mov dword ptr [rbp + 0x34], edx
00310983  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
00310986  48 8D 0D 73 F6 CE FF            lea rcx, [rip - 0x31098d]
0031098D  48 8B 8C C1 40 8C FC 00         mov rcx, qword ptr [rcx + rax*8 + 0xfc8c40]
00310995  41 8B 47 78                     mov eax, dword ptr [r15 + 0x78]
00310999  A8 02                           test al, 2
0031099B  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
003109A0  0F 84 86 00 00 00               je 0x140310a2c
003109A6  48 0B 81 60 8E 00 00            or rax, qword ptr [rcx + 0x8e60]
003109AD  49 8B D5                        mov rdx, r13
003109B0  E9 49 F4 FF FF                  jmp 0x14030fdfe
003109B5  41 0F B7 89 88 00 00 00         movzx ecx, word ptr [r9 + 0x88]
003109BD  48 8B 05 F4 27 C1 00            mov rax, qword ptr [rip + 0xc127f4]
003109C4  C1 E1 06                        shl ecx, 6
003109C7  48 0F BD D6                     bsr rdx, rsi
003109CB  03 CA                           add ecx, edx
003109CD  89 55 4C                        mov dword ptr [rbp + 0x4c], edx
003109D0  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
003109D3  48 8D 0D 26 F6 CE FF            lea rcx, [rip - 0x3109da]
003109DA  48 8B 8C C1 40 8C FC 00         mov rcx, qword ptr [rcx + rax*8 + 0xfc8c40]
003109E2  8B 47 78                        mov eax, dword ptr [rdi + 0x78]
003109E5  84 C3                           test bl, al
003109E7  74 52                           je 0x140310a3b
003109E9  4C 0B B9 60 8E 00 00            or r15, qword ptr [rcx + 0x8e60]
003109F0  48 8B D7                        mov rdx, rdi
003109F3  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
003109F8  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
003109FD  E8 36 0B EF FF                  call 0x140201538
00310A02  48 8B D7                        mov rdx, rdi
00310A05  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00310A0A  E8 01 09 EF FF                  call 0x140201310
00310A0F  E9 2E F3 FF FF                  jmp 0x14030fd42
00310A14  48 0B 81 C8 00 00 00            or rax, qword ptr [rcx + 0xc8]
00310A1B  E9 D7 F3 FF FF                  jmp 0x14030fdf7
00310A20  4C 0B B9 C8 00 00 00            or r15, qword ptr [rcx + 0xc8]
00310A27  E9 66 F4 FF FF                  jmp 0x14030fe92
00310A2C  48 0B 81 C8 00 00 00            or rax, qword ptr [rcx + 0xc8]
00310A33  49 8B D5                        mov rdx, r13
00310A36  E9 C3 F3 FF FF                  jmp 0x14030fdfe
00310A3B  4C 0B B9 C8 00 00 00            or r15, qword ptr [rcx + 0xc8]
00310A42  EB AC                           jmp 0x1403109f0
00310A44  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00310A49  49 8B 80 C8 00 00 00            mov rax, qword ptr [r8 + 0xc8]
00310A50  48 F7 D0                        not rax
00310A53  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00310A57  48 23 F0                        and rsi, rax
00310A5A  4C 23 F0                        and r14, rax
00310A5D  48 89 75 88                     mov qword ptr [rbp - 0x78], rsi
00310A61  E8 EA 91 08 00                  call 0x140399c50
00310A66  E9 2B F3 FF FF                  jmp 0x14030fd96
00310A6B  41 0F B6 84 24 D9 35 00 00      movzx eax, byte ptr [r12 + 0x35d9]
00310A74  84 C0                           test al, al
00310A76  0F 85 F6 01 00 00               jne 0x140310c72
00310A7C  41 C6 84 24 D9 35 00 00 01      mov byte ptr [r12 + 0x35d9], 1
00310A85  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00310A88  41 89 84 24 DC 35 00 00         mov dword ptr [r12 + 0x35dc], eax
00310A90  44 84 73 33                     test byte ptr [rbx + 0x33], r14b
00310A94  0F 85 E5 05 00 00               jne 0x14031107f
00310A9A  F6 43 33 04                     test byte ptr [rbx + 0x33], 4
00310A9E  74 14                           je 0x140310ab4
00310AA0  48 8B 87 B8 8E 00 00            mov rax, qword ptr [rdi + 0x8eb8]
00310AA7  0F BE 4B 34                     movsx ecx, byte ptr [rbx + 0x34]
00310AAB  48 85 C0                        test rax, rax
00310AAE  0F 85 10 02 00 00               jne 0x140310cc4
00310AB4  F6 43 33 01                     test byte ptr [rbx + 0x33], 1
00310AB8  74 0C                           je 0x140310ac6
00310ABA  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00310ABE  66 F0 FF 88 64 03 00 00         lock dec word ptr [rax + 0x364]
00310AC6  41 0F B6 07                     movzx eax, byte ptr [r15]
00310ACA  FF C6                           inc esi
00310ACC  3B F0                           cmp esi, eax
00310ACE  0F 82 6C 01 00 00               jb 0x140310c40
00310AD4  44 8B B5 F0 00 00 00            mov r14d, dword ptr [rbp + 0xf0]
00310ADB  4C 8B 6C 24 30                  mov r13, qword ptr [rsp + 0x30]
00310AE0  48 8B 9D E0 00 00 00            mov rbx, qword ptr [rbp + 0xe0]
00310AE7  45 33 FF                        xor r15d, r15d
00310AEA  E9 DC 02 00 00                  jmp 0x140310dcb
00310AEF  48 8B 85 D8 00 00 00            mov rax, qword ptr [rbp + 0xd8]
00310AF6  48 0F BD D6                     bsr rdx, rsi
00310AFA  0F B7 88 88 00 00 00            movzx ecx, word ptr [rax + 0x88]
00310B01  48 8B 05 B0 26 C1 00            mov rax, qword ptr [rip + 0xc126b0]
00310B08  C1 E1 06                        shl ecx, 6
00310B0B  03 CA                           add ecx, edx
00310B0D  C7 45 60 00 00 00 00            mov dword ptr [rbp + 0x60], 0
00310B14  89 55 60                        mov dword ptr [rbp + 0x60], edx
00310B17  41 8B 10                        mov edx, dword ptr [r8]
00310B1A  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00310B1E  D1 EA                           shr edx, 1
00310B20  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
00310B23  83 E2 01                        and edx, 1
00310B26  48 8D 0D D3 F4 CE FF            lea rcx, [rip - 0x310b2d]
00310B2D  4C 8B AC C1 40 8C FC 00         mov r13, qword ptr [rcx + rax*8 + 0xfc8c40]
00310B35  49 8B CD                        mov rcx, r13
00310B38  E8 5B CA FF FF                  call 0x14030d598
00310B3D  84 C0                           test al, al
00310B3F  0F 84 4E 05 00 00               je 0x140311093
00310B45  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00310B49  E8 22 61 F4 FF                  call 0x140256c70
00310B4E  85 C0                           test eax, eax
00310B50  0F 84 25 06 00 00               je 0x14031117b
00310B56  49 8B 07                        mov rax, qword ptr [r15]
00310B59  48 8B 5D D0                     mov rbx, qword ptr [rbp - 0x30]
00310B5D  48 85 C0                        test rax, rax
00310B60  74 2F                           je 0x140310b91
00310B62  41 8B 95 D8 00 00 00            mov edx, dword ptr [r13 + 0xd8]
00310B69  48 8B CB                        mov rcx, rbx
00310B6C  48 03 D0                        add rdx, rax
00310B6F  E8 8C A6 FF FF                  call 0x14030b200
00310B74  84 C0                           test al, al
00310B76  74 19                           je 0x140310b91
00310B78  E8 93 57 04 00                  call 0x140356310
00310B7D  84 C0                           test al, al
00310B7F  75 10                           jne 0x140310b91
00310B81  48 8B CA                        mov rcx, rdx
00310B84  E8 17 1C EF FF                  call 0x1402027a0
00310B89  84 C0                           test al, al
00310B8B  0F 85 E6 05 00 00               jne 0x140311177
00310B91  48 8B 45 00                     mov rax, qword ptr [rbp]
00310B95  48 8B D3                        mov rdx, rbx
00310B98  44 0F B6 45 FC                  movzx r8d, byte ptr [rbp - 4]
00310B9D  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00310BA1  48 89 4D 00                     mov qword ptr [rbp], rcx
00310BA5  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00310BA9  E8 02 0E EF FF                  call 0x1402019b0
00310BAE  4D 8B BC 24 E8 37 00 00         mov r15, qword ptr [r12 + 0x37e8]
00310BB6  33 D2                           xor edx, edx
00310BB8  49 8B CF                        mov rcx, r15
00310BBB  41 B8 F0 00 00 00               mov r8d, 0xf0
00310BC1  E8 7A 60 3B 00                  call 0x1406c6c40
00310BC6  45 33 C0                        xor r8d, r8d
00310BC9  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00310BCD  49 8B CF                        mov rcx, r15
00310BD0  E8 DB BA FF FF                  call 0x14030c6b0
00310BD5  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00310BDA  45 33 C9                        xor r9d, r9d
00310BDD  4D 8B C5                        mov r8, r13
00310BE0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00310BE5  48 8B D3                        mov rdx, rbx
00310BE8  49 8B CF                        mov rcx, r15
00310BEB  E8 B0 B6 FF FF                  call 0x14030c2a0
00310BF0  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
00310BF5  45 33 C0                        xor r8d, r8d
00310BF8  49 8B D4                        mov rdx, r12
00310BFB  49 8B CF                        mov rcx, r15
00310BFE  E8 1D C3 FF FF                  call 0x14030cf20
00310C03  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00310C07  0F B6 D8                        movzx ebx, al
00310C0A  E8 41 90 08 00                  call 0x140399c50
00310C0F  4C 8B 6C 24 30                  mov r13, qword ptr [rsp + 0x30]
00310C14  84 DB                           test bl, bl
00310C16  48 8B 9D E0 00 00 00            mov rbx, qword ptr [rbp + 0xe0]
00310C1D  48 8B B5 D8 00 00 00            mov rsi, qword ptr [rbp + 0xd8]
00310C24  0F 84 AA 01 00 00               je 0x140310dd4
00310C2A  33 F6                           xor esi, esi
00310C2C  41 38 37                        cmp byte ptr [r15], sil
00310C2F  0F 86 B2 FE FF FF               jbe 0x140310ae7
00310C35  44 8D 76 02                     lea r14d, [rsi + 2]
00310C39  0F 1F 80 00 00 00 00            nop dword ptr [rax]
00310C40  48 8D 0C B6                     lea rcx, [rsi + rsi*4]
00310C44  41 0F B6 44 CF 33               movzx eax, byte ptr [r15 + rcx*8 + 0x33]
00310C4A  49 8D 1C CF                     lea rbx, [r15 + rcx*8]
00310C4E  48 8B 7B 10                     mov rdi, qword ptr [rbx + 0x10]
00310C52  A8 10                           test al, 0x10
00310C54  0F 85 11 FE FF FF               jne 0x140310a6b
00310C5A  A8 08                           test al, 8
00310C5C  0F 84 2E FE FF FF               je 0x140310a90
00310C62  90                              nop
00310C63  80 7F 07 00                     cmp byte ptr [rdi + 7], 0
00310C67  0F 84 23 FE FF FF               je 0x140310a90
00310C6D  E9 F9 FD FF FF                  jmp 0x140310a6b
00310C72  3C 01                           cmp al, 1
00310C74  75 44                           jne 0x140310cba
00310C76  41 8B 94 24 DC 35 00 00         mov edx, dword ptr [r12 + 0x35dc]
00310C7E  3B 57 24                        cmp edx, dword ptr [rdi + 0x24]
00310C81  0F 84 09 FE FF FF               je 0x140310a90
00310C87  4D 8D AC 24 E0 35 00 00         lea r13, [r12 + 0x35e0]
00310C8F  45 88 B4 24 D9 35 00 00         mov byte ptr [r12 + 0x35d9], r14b
00310C97  49 8B CD                        mov rcx, r13
00310C9A  E8 51 AA F4 FF                  call 0x14025b6f0
00310C9F  4C 8B 87 C8 00 00 00            mov r8, qword ptr [rdi + 0xc8]
00310CA6  49 8B CD                        mov rcx, r13
00310CA9  0F B6 97 D0 00 00 00            movzx edx, byte ptr [rdi + 0xd0]
00310CB0  E8 0B AA F4 FF                  call 0x14025b6c0
00310CB5  E9 D6 FD FF FF                  jmp 0x140310a90
00310CBA  4D 8D AC 24 E0 35 00 00         lea r13, [r12 + 0x35e0]
00310CC2  EB DB                           jmp 0x140310c9f
00310CC4  49 83 BC 24 B8 8E 00 00 00      cmp qword ptr [r12 + 0x8eb8], 0
00310CCD  0F 84 E1 FD FF FF               je 0x140310ab4
00310CD3  4C 3B E7                        cmp r12, rdi
00310CD6  0F 84 D8 FD FF FF               je 0x140310ab4
00310CDC  44 8B 00                        mov r8d, dword ptr [rax]
00310CDF  45 8B C8                        mov r9d, r8d
00310CE2  49 8D 84 24 B8 8E 00 00         lea rax, [r12 + 0x8eb8]
00310CEA  41 81 E1 00 00 04 00            and r9d, 0x40000
00310CF1  74 08                           je 0x140310cfb
00310CF3  49 8D 84 24 B8 8E 00 00         lea rax, [r12 + 0x8eb8]
00310CFB  41 0F BA E0 14                  bt r8d, 0x14
00310D00  0F 83 1A 05 00 00               jae 0x140311220
00310D06  80 3D FA 42 CB 00 00            cmp byte ptr [rip + 0xcb42fa], 0
00310D0D  48 8B 08                        mov rcx, qword ptr [rax]
00310D10  44 89 71 0C                     mov dword ptr [rcx + 0xc], r14d
00310D14  44 8B 6F 24                     mov r13d, dword ptr [rdi + 0x24]
00310D18  75 22                           jne 0x140310d3c
00310D1A  41 8B C5                        mov eax, r13d
00310D1D  48 8D 15 DC F2 CE FF            lea rdx, [rip - 0x310d24]
00310D24  46 0F B6 AC 6A 60 D2 FC 00      movzx r13d, byte ptr [rdx + r13*2 + 0xfcd260]
00310D2D  41 C1 E5 06                     shl r13d, 6
00310D31  0F B6 84 42 61 D2 FC 00         movzx eax, byte ptr [rdx + rax*2 + 0xfcd261]
00310D39  44 0B E8                        or r13d, eax
00310D3C  44 89 69 08                     mov dword ptr [rcx + 8], r13d
00310D40  8B 05 CE 5D CB 00               mov eax, dword ptr [rip + 0xcb5dce]
00310D46  A8 20                           test al, 0x20
00310D48  74 0B                           je 0x140310d55
00310D4A  8B 4F 24                        mov ecx, dword ptr [rdi + 0x24]
00310D4D  41 8B D6                        mov edx, r14d
00310D50  E8 6B A5 1E 00                  call 0x1404fb2c0
00310D55  41 8B D5                        mov edx, r13d
00310D58  B9 C2 00 00 40                  mov ecx, 0x400000c2
00310D5D  48 C1 EA 20                     shr rdx, 0x20
00310D61  41 8B C5                        mov eax, r13d
00310D64  0F 30                           wrmsr
00310D66  E9 49 FD FF FF                  jmp 0x140310ab4
00310D6B  4C 89 75 E8                     mov qword ptr [rbp - 0x18], r14
00310D6F  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00310D73  4C 89 7D E0                     mov qword ptr [rbp - 0x20], r15
00310D77  90                              nop
00310D78  49 87 16                        xchg qword ptr [r14], rdx
00310D7B  48 85 D2                        test rdx, rdx
00310D7E  0F 85 85 02 00 00               jne 0x140311009
00310D84  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
00310D88  49 8D 56 40                     lea rdx, [r14 + 0x40]
00310D8C  23 C7                           and eax, edi
00310D8E  4C 89 75 F0                     mov qword ptr [rbp - 0x10], r14
00310D92  89 45 F8                        mov dword ptr [rbp - 8], eax
00310D95  48 89 55 08                     mov qword ptr [rbp + 8], rdx
00310D99  0F 84 61 02 00 00               je 0x140311000
00310D9F  0F BD C0                        bsr eax, eax
00310DA2  8B C8                           mov ecx, eax
00310DA4  48 C1 E1 04                     shl rcx, 4
00310DA8  48 03 CA                        add rcx, rdx
00310DAB  89 45 5C                        mov dword ptr [rbp + 0x5c], eax
00310DAE  48 89 4D 00                     mov qword ptr [rbp], rcx
00310DB2  88 45 FC                        mov byte ptr [rbp - 4], al
00310DB5  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00310DB9  45 8B F7                        mov r14d, r15d
00310DBC  44 89 BD F0 00 00 00            mov dword ptr [rbp + 0xf0], r15d
00310DC3  4D 8B EF                        mov r13, r15
00310DC6  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00310DCB  48 8B B5 D8 00 00 00            mov rsi, qword ptr [rbp + 0xd8]
00310DD2  EB 03                           jmp 0x140310dd7
00310DD4  45 33 FF                        xor r15d, r15d
00310DD7  41 83 FE 40                     cmp r14d, 0x40
00310DDB  73 22                           jae 0x140310dff
00310DDD  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00310DE1  4C 89 7D D0                     mov qword ptr [rbp - 0x30], r15
00310DE5  48 8D 4D F8                     lea rcx, [rbp - 8]
00310DE9  E8 E2 58 12 00                  call 0x1404366d0
00310DEE  85 C0                           test eax, eax
00310DF0  78 0D                           js 0x140310dff
00310DF2  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00310DF6  48 23 CB                        and rcx, rbx
00310DF9  0F 85 73 00 00 00               jne 0x140310e72
00310DFF  F7 05 2F 5D CB 00 00 00 20 00   test dword ptr [rip + 0xcb5d2f], 0x200000
00310E09  4C 8B B5 F8 00 00 00            mov r14, qword ptr [rbp + 0xf8]
00310E10  74 56                           je 0x140310e68
00310E12  0F 0D 4D E0                     prefetchw byte ptr [rbp - 0x20]
00310E16  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00310E1A  48 85 C0                        test rax, rax
00310E1D  75 23                           jne 0x140310e42
00310E1F  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00310E23  48 8D 45 E0                     lea rax, [rbp - 0x20]
00310E27  F0 4C 0F B1 39                  lock cmpxchg qword ptr [rcx], r15
00310E2C  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00310E30  48 3B C1                        cmp rax, rcx
00310E33  0F 84 E4 E8 FF FF               je 0x14030f71d
00310E39  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00310E3D  E8 5E 6C F0 FF                  call 0x140217aa0
00310E42  48 8D 48 08                     lea rcx, [rax + 8]
00310E46  4C 89 7D E0                     mov qword ptr [rbp - 0x20], r15
00310E4A  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
00310E4E  48 8B C2                        mov rax, rdx
00310E51  48 87 01                        xchg qword ptr [rcx], rax
00310E54  32 C2                           xor al, dl
00310E56  A8 04                           test al, 4
00310E58  0F 84 BF E8 FF FF               je 0x14030f71d
00310E5E  E8 BD 6D F0 FF                  call 0x140217c20
00310E63  E9 B5 E8 FF FF                  jmp 0x14030f71d
00310E68  F0 49 83 26 00                  lock and qword ptr [r14], 0
00310E6D  E9 AB E8 FF FF                  jmp 0x14030f71d
00310E72  49 8B C5                        mov rax, r13
00310E75  48 F7 D0                        not rax
00310E78  48 23 C1                        and rax, rcx
00310E7B  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00310E7F  0F 84 7A FF FF FF               je 0x140310dff
00310E85  48 8B 7D D0                     mov rdi, qword ptr [rbp - 0x30]
00310E89  0F B7 86 88 00 00 00            movzx eax, word ptr [rsi + 0x88]
00310E90  48 8B 8F 40 02 00 00            mov rcx, qword ptr [rdi + 0x240]
00310E97  66 3B 01                        cmp ax, word ptr [rcx]
00310E9A  0F 83 52 02 00 00               jae 0x1403110f2
00310EA0  48 8B 5C C1 08                  mov rbx, qword ptr [rcx + rax*8 + 8]
00310EA5  48 8B CF                        mov rcx, rdi
00310EA8  E8 63 71 F4 FF                  call 0x140258010
00310EAD  44 8B 47 50                     mov r8d, dword ptr [rdi + 0x50]
00310EB1  41 8B D7                        mov edx, r15d
00310EB4  8B 4F 54                        mov ecx, dword ptr [rdi + 0x54]
00310EB7  44 3B C1                        cmp r8d, ecx
00310EBA  44 0F 46 C1                     cmovbe r8d, ecx
00310EBE  0F B6 8F 05 02 00 00            movzx ecx, byte ptr [rdi + 0x205]
00310EC5  44 3B 05 B0 44 CB 00            cmp r8d, dword ptr [rip + 0xcb44b0]
00310ECC  0F 93 C2                        setae dl
00310ECF  44 8D 04 42                     lea r8d, [rdx + rax*2]
00310ED3  0F B6 86 B9 00 00 00            movzx eax, byte ptr [rsi + 0xb9]
00310EDA  44 0F AF C0                     imul r8d, eax
00310EDE  48 8B 86 C0 00 00 00            mov rax, qword ptr [rsi + 0xc0]
00310EE5  44 03 C1                        add r8d, ecx
00310EE8  4B 8D 0C 40                     lea rcx, [r8 + r8*2]
00310EEC  48 8D 14 C8                     lea rdx, [rax + rcx*8]
00310EF0  48 8B 4C C8 10                  mov rcx, qword ptr [rax + rcx*8 + 0x10]
00310EF5  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00310EF9  48 23 CB                        and rcx, rbx
00310EFC  48 8B 02                        mov rax, qword ptr [rdx]
00310EFF  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00310F03  48 0F 45 D9                     cmovne rbx, rcx
00310F07  8B 48 78                        mov ecx, dword ptr [rax + 0x78]
00310F0A  48 D1 E9                        shr rcx, 1
00310F0D  83 E1 01                        and ecx, 1
00310F10  48 8B 44 CE 10                  mov rax, qword ptr [rsi + rcx*8 + 0x10]
00310F15  48 8B 7D B8                     mov rdi, qword ptr [rbp - 0x48]
00310F19  48 23 C3                        and rax, rbx
00310F1C  48 8B 5D D0                     mov rbx, qword ptr [rbp - 0x30]
00310F20  48 23 F8                        and rdi, rax
00310F23  48 89 7D B8                     mov qword ptr [rbp - 0x48], rdi
00310F27  4C 8B 43 68                     mov r8, qword ptr [rbx + 0x68]
00310F2B  4D 85 C0                        test r8, r8
00310F2E  0F 85 E3 00 00 00               jne 0x140311017
00310F34  48 8B CB                        mov rcx, rbx
00310F37  E8 94 5E F4 FF                  call 0x140256dd0
00310F3C  48 85 FF                        test rdi, rdi
00310F3F  75 1E                           jne 0x140310f5f
00310F41  85 C0                           test eax, eax
00310F43  0F 84 7A 01 00 00               je 0x1403110c3
00310F49  48 8B 9D E0 00 00 00            mov rbx, qword ptr [rbp + 0xe0]
00310F50  41 FF C6                        inc r14d
00310F53  44 89 B5 F0 00 00 00            mov dword ptr [rbp + 0xf0], r14d
00310F5A  E9 78 FE FF FF                  jmp 0x140310dd7
00310F5F  85 C0                           test eax, eax
00310F61  0F 84 93 01 00 00               je 0x1403110fa
00310F67  4C 8D 43 78                     lea r8, [rbx + 0x78]
00310F6B  48 8B F7                        mov rsi, rdi
00310F6E  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
00310F73  4C 8D 7B 68                     lea r15, [rbx + 0x68]
00310F77  48 85 F6                        test rsi, rsi
00310F7A  0F 85 6F FB FF FF               jne 0x140310aef
00310F80  48 8B B5 D8 00 00 00            mov rsi, qword ptr [rbp + 0xd8]
00310F87  4C 8B 6C 24 30                  mov r13, qword ptr [rsp + 0x30]
00310F8C  48 85 FF                        test rdi, rdi
00310F8F  0F 84 15 01 00 00               je 0x1403110aa
00310F95  0F B7 8E 88 00 00 00            movzx ecx, word ptr [rsi + 0x88]
00310F9C  45 33 FF                        xor r15d, r15d
00310F9F  48 8B 05 12 22 C1 00            mov rax, qword ptr [rip + 0xc12212]
00310FA6  C1 E1 06                        shl ecx, 6
00310FA9  48 0F BD D7                     bsr rdx, rdi
00310FAD  03 CA                           add ecx, edx
00310FAF  89 55 68                        mov dword ptr [rbp + 0x68], edx
00310FB2  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
00310FB5  48 8D 0D 44 F0 CE FF            lea rcx, [rip - 0x310fbc]
00310FBC  48 8B 8C C1 40 8C FC 00         mov rcx, qword ptr [rcx + rax*8 + 0xfc8c40]
00310FC4  8B 43 78                        mov eax, dword ptr [rbx + 0x78]
00310FC7  A8 02                           test al, 2
00310FC9  0F 85 DC 01 00 00               jne 0x1403111ab
00310FCF  4C 0B A9 C8 00 00 00            or r13, qword ptr [rcx + 0xc8]
00310FD6  48 8B D3                        mov rdx, rbx
00310FD9  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
00310FDE  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00310FE2  E8 D1 05 EF FF                  call 0x1402015b8
00310FE7  48 8B D3                        mov rdx, rbx
00310FEA  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00310FEF  E8 1C 03 EF FF                  call 0x140201310
00310FF4  48 8B 9D E0 00 00 00            mov rbx, qword ptr [rbp + 0xe0]
00310FFB  E9 D7 FD FF FF                  jmp 0x140310dd7
00311000  4C 89 7D 00                     mov qword ptr [rbp], r15
00311004  E9 AC FD FF FF                  jmp 0x140310db5
00311009  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0031100D  E8 9E 6E F4 FF                  call 0x140257eb0
00311012  E9 6D FD FF FF                  jmp 0x140310d84
00311017  48 8B CB                        mov rcx, rbx
0031101A  E8 E1 A1 FF FF                  call 0x14030b200
0031101F  84 C0                           test al, al
00311021  0F 84 0D FF FF FF               je 0x140310f34
00311027  E8 E4 52 04 00                  call 0x140356310
0031102C  84 C0                           test al, al
0031102E  0F 85 00 FF FF FF               jne 0x140310f34
00311034  0F B7 8E 88 00 00 00            movzx ecx, word ptr [rsi + 0x88]
0031103B  48 8B D7                        mov rdx, rdi
0031103E  E8 ED 16 EF FF                  call 0x140202730
00311043  83 3D CE 5C CB 00 00            cmp dword ptr [rip + 0xcb5cce], 0
0031104A  48 8B F8                        mov rdi, rax
0031104D  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00311051  0F 84 DD FE FF FF               je 0x140310f34
00311057  49 8B D4                        mov rdx, r12
0031105A  48 8B CB                        mov rcx, rbx
0031105D  E8 5A 71 1E 00                  call 0x1404f81bc
00311062  84 C0                           test al, al
00311064  0F 84 CA FE FF FF               je 0x140310f34
0031106A  48 8D 55 B8                     lea rdx, [rbp - 0x48]
0031106E  48 8B CE                        mov rcx, rsi
00311071  E8 96 D3 0E 00                  call 0x1403fe40c
00311076  48 8B 7D B8                     mov rdi, qword ptr [rbp - 0x48]
0031107A  E9 B5 FE FF FF                  jmp 0x140310f34
0031107F  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
00311083  45 33 C0                        xor r8d, r8d
00311086  48 8B D7                        mov rdx, rdi
00311089  E8 BE A6 FF FF                  call 0x14030b74c
0031108E  E9 07 FA FF FF                  jmp 0x140310a9a
00311093  49 8B 85 C8 00 00 00            mov rax, qword ptr [r13 + 0xc8]
0031109A  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0031109F  48 F7 D0                        not rax
003110A2  48 23 F0                        and rsi, rax
003110A5  E9 CD FE FF FF                  jmp 0x140310f77
003110AA  48 8B 9D E0 00 00 00            mov rbx, qword ptr [rbp + 0xe0]
003110B1  41 FF C6                        inc r14d
003110B4  44 89 B5 F0 00 00 00            mov dword ptr [rbp + 0xf0], r14d
003110BB  45 33 FF                        xor r15d, r15d
003110BE  E9 14 FD FF FF                  jmp 0x140310dd7
003110C3  48 8B 45 00                     mov rax, qword ptr [rbp]
003110C7  48 8B D3                        mov rdx, rbx
003110CA  44 0F B6 45 FC                  movzx r8d, byte ptr [rbp - 4]
003110CF  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
003110D3  48 89 4D 00                     mov qword ptr [rbp], rcx
003110D7  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
003110DB  E8 D0 08 EF FF                  call 0x1402019b0
003110E0  48 8B D3                        mov rdx, rbx
003110E3  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
003110E8  E8 23 02 EF FF                  call 0x140201310
003110ED  E9 57 FE FF FF                  jmp 0x140310f49
003110F2  49 8B DF                        mov rbx, r15
003110F5  E9 AB FD FF FF                  jmp 0x140310ea5
003110FA  0F B7 8E 88 00 00 00            movzx ecx, word ptr [rsi + 0x88]
00311101  48 8B 05 B0 20 C1 00            mov rax, qword ptr [rip + 0xc120b0]
00311108  C1 E1 06                        shl ecx, 6
0031110B  48 0F BD D7                     bsr rdx, rdi
0031110F  03 CA                           add ecx, edx
00311111  89 55 64                        mov dword ptr [rbp + 0x64], edx
00311114  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
00311117  48 8D 0D E2 EE CE FF            lea rcx, [rip - 0x31111e]
0031111E  48 8B 8C C1 40 8C FC 00         mov rcx, qword ptr [rcx + rax*8 + 0xfc8c40]
00311126  8B 43 78                        mov eax, dword ptr [rbx + 0x78]
00311129  A8 02                           test al, 2
0031112B  0F 85 71 00 00 00               jne 0x1403111a2
00311131  4C 0B A9 C8 00 00 00            or r13, qword ptr [rcx + 0xc8]
00311138  48 8B 45 00                     mov rax, qword ptr [rbp]
0031113C  48 8B D3                        mov rdx, rbx
0031113F  44 0F B6 45 FC                  movzx r8d, byte ptr [rbp - 4]
00311144  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
00311149  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0031114D  48 89 4D 00                     mov qword ptr [rbp], rcx
00311151  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00311155  E8 56 08 EF FF                  call 0x1402019b0
0031115A  48 8B D3                        mov rdx, rbx
0031115D  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00311162  E8 A9 01 EF FF                  call 0x140201310
00311167  48 8B 9D E0 00 00 00            mov rbx, qword ptr [rbp + 0xe0]
0031116E  4C 89 7D D0                     mov qword ptr [rbp - 0x30], r15
00311172  E9 60 FC FF FF                  jmp 0x140310dd7
00311177  48 8B 7D B8                     mov rdi, qword ptr [rbp - 0x48]
0031117B  49 8B 85 C8 00 00 00            mov rax, qword ptr [r13 + 0xc8]
00311182  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00311186  48 F7 D0                        not rax
00311189  48 23 F8                        and rdi, rax
0031118C  48 23 F0                        and rsi, rax
0031118F  48 89 7D B8                     mov qword ptr [rbp - 0x48], rdi
00311193  E8 B8 8A 08 00                  call 0x140399c50
00311198  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0031119D  E9 D5 FD FF FF                  jmp 0x140310f77
003111A2  4C 0B A9 60 8E 00 00            or r13, qword ptr [rcx + 0x8e60]
003111A9  EB 8D                           jmp 0x140311138
003111AB  4C 0B A9 60 8E 00 00            or r13, qword ptr [rcx + 0x8e60]
003111B2  E9 1F FE FF FF                  jmp 0x140310fd6
003111B7  41 0F B6 D0                     movzx edx, r8b
003111BB  49 8D 84 24 B8 8E 00 00         lea rax, [r12 + 0x8eb8]
003111C3  45 85 C9                        test r9d, r9d
003111C6  0F 84 3B F0 FF FF               je 0x140310207
003111CC  3B D1                           cmp edx, ecx
003111CE  0F 8D 33 F0 FF FF               jge 0x140310207
003111D4  E9 30 F1 FF FF                  jmp 0x140310309
003111D9  41 0F B6 D0                     movzx edx, r8b
003111DD  49 8D 84 24 B8 8E 00 00         lea rax, [r12 + 0x8eb8]
003111E5  45 85 C9                        test r9d, r9d
003111E8  0F 84 BB F3 FF FF               je 0x1403105a9
003111EE  3B D1                           cmp edx, ecx
003111F0  0F 8D B3 F3 FF FF               jge 0x1403105a9
003111F6  E9 74 F4 FF FF                  jmp 0x14031066f
003111FB  F7 05 33 59 CB 00 00 00 20 00   test dword ptr [rip + 0xcb5933], 0x200000
00311205  0F 85 60 FB FF FF               jne 0x140310d6b
0031120B  44 89 7D 58                     mov dword ptr [rbp + 0x58], r15d
0031120F  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
00311215  0F 83 69 FB FF FF               jae 0x140310d84
0031121B  E9 BA FC 3C 00                  jmp 0x1406e0eda
00311220  41 0F B6 D0                     movzx edx, r8b
00311224  49 8D 84 24 B8 8E 00 00         lea rax, [r12 + 0x8eb8]
0031122C  45 85 C9                        test r9d, r9d
0031122F  0F 84 7F F8 FF FF               je 0x140310ab4
00311235  3B D1                           cmp edx, ecx
00311237  0F 8D 77 F8 FF FF               jge 0x140310ab4
0031123D  E9 C4 FA FF FF                  jmp 0x140310d06
00311242  48 8B 82 C8 00 00 00            mov rax, qword ptr [rdx + 0xc8]
00311249  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0031124D  E9 FE F7 FF FF                  jmp 0x140310a50
00311252  49 8B D4                        mov rdx, r12
00311255  48 8B CF                        mov rcx, rdi
00311258  E8 5F 6F 1E 00                  call 0x1404f81bc
0031125D  84 C0                           test al, al
0031125F  0F 84 17 F5 FF FF               je 0x14031077c
00311265  48 8B 8D D8 00 00 00            mov rcx, qword ptr [rbp + 0xd8]
0031126C  48 8D 55 B0                     lea rdx, [rbp - 0x50]
00311270  E8 97 D1 0E 00                  call 0x1403fe40c
00311275  48 8B 75 B0                     mov rsi, qword ptr [rbp - 0x50]
00311279  E9 FE F4 FF FF                  jmp 0x14031077c
0031127E  48 8B 75 B0                     mov rsi, qword ptr [rbp - 0x50]
00311282  49 8B 85 C8 00 00 00            mov rax, qword ptr [r13 + 0xc8]
00311289  48 8D 4D C8                     lea rcx, [rbp - 0x38]
0031128D  48 F7 D0                        not rax
00311290  48 23 F0                        and rsi, rax
00311293  4C 23 F0                        and r14, rax
00311296  48 89 75 B0                     mov qword ptr [rbp - 0x50], rsi
0031129A  E8 B1 89 08 00                  call 0x140399c50
0031129F  4C 8B 8D D8 00 00 00            mov r9, qword ptr [rbp + 0xd8]
003112A6  E9 96 EB FF FF                  jmp 0x14030fe41
003112AB  48 8B 9C 24 D0 01 00 00         mov rbx, qword ptr [rsp + 0x1d0]
003112B3  48 81 C4 90 01 00 00            add rsp, 0x190
003112BA  41 5F                           pop r15
003112BC  41 5E                           pop r14
003112BE  41 5D                           pop r13
003112C0  41 5C                           pop r12
003112C2  5F                              pop rdi
003112C3  5E                              pop rsi
003112C4  5D                              pop rbp
003112C5  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSearchForNewThreadsOnTarget(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int8 v_stack_m12C;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int8 v_stack_m154;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m18C;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int8 v_stack_mCC;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (400);
    if (a5 == 0) goto loc_0030F6E3;
    if (a1 == a5) goto loc_003112AB;
    a3 = 0;
    a2 = 0;
    result = KiMayStealStandbyThread(a5, a2, a3, a4);
    v_r15 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_0030F580;
    v_rbx = (*(unsigned __int64 *)(a2 + 8)) & (a4);
loc_0030F577:
    if (v_rbx != 0) goto loc_0030F9DD;
loc_0030F580:
    v_stack_m170 = 0;
    result = 0;
    v_stack_m180 = 0;
    v_stack_m128 = v_xmm0;
    v_stack_m120 = 0;
    v_stack_m148 = 0;
    v_stack_m138 = v_xmm0;
    v_stack_m130 = v_xmm1;
    v_stack_m12C = 32;
    v_stack_m158 = v_xmm0;
    v_stack_m154 = 32;
    v_stack_m168 = v_xmm0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 33752))) == 0) goto loc_0030F8E7;
loc_0030F5C7:
    v_rbx = (a5) & (-2);
    v_stack_m170 = v_rbx;
loc_0030F5E0:
    if (condition_is_above_or_equal) goto loc_0030F814;
loc_0030F5ED:
    v_rsi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 13327543)) & ((unsigned int)(v_rsi))) == 0) goto loc_0030F8C0;
loc_0030F5FB:
loc_0030F5FD:
    if (*(unsigned __int64 *)(a5 + 48) == 0) goto loc_0030F5E0;
    goto loc_0030F5ED;
loc_0030F608:
    v_rdi = (a5) + (-216);
    a1 = (*(unsigned __int64 *)(v_stack_p10 + 8)) & (v_rsi);
    if (condition_is_not_equal) goto loc_0030FC5A;
loc_0030F623:
    v_r15 = 0;
    if (v_stack_m170 == 0) goto loc_0030F682;
    a1 = (v_stack_m170) & (-2);
    v_stack_m48 = a1;
    v_rbx = (unsigned int)((v_stack_m170) & (1));
    if (condition_is_equal) goto loc_0030F944;
    result = *(unsigned __int64 *)(a5 + 48);
    if (((unsigned int)(v_rbx)) == 1) {
        result = *(unsigned __int64 *)(a1 + 36440);
        a3 = *(unsigned __int64 *)(a1 + 36440);
        a3 = (a3) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_0030F682;
loc_0030F670:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0030F670;
loc_0030F682:
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 13785)) == 0) goto loc_0030F6D1;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 13785))) == 1) goto loc_0030F8FC;
    result = KiSendSoftwareInterruptAffinity(a1 + 13792, *(unsigned __int8 *)(a1 + 13784), a3, a4);
loc_0030F6AD:
    if ((*(unsigned __int8 *)(a1 + 13785)) == 2) goto loc_0030FD5D;
loc_0030F6BC:
    *(unsigned __int8 *)(a1 + 13785) = 0;
    *(unsigned int *)(a1 + 13788) = 0xFFFFULL;
loc_0030F6D1:
    if (v_stack_m180 != 0) goto loc_00310860;
    goto loc_003112AB;
loc_0030F6E3:
    result = 0;
    v_stack_mC8 = v_xmm1;
    v_stack_mC0 = 0;
    v_r15 = 0;
    v_stack_m178 = 0;
    v_stack_mD8 = v_xmm1;
    v_stack_mD0 = v_xmm0;
    v_stack_mCC = 32;
    v_stack_mE8 = v_xmm0;
    if ((((unsigned int)(0xFFFFFFFEULL)) & ((unsigned int)(*(unsigned int *)(a6 + 8)))) != 0) goto loc_003111FB;
loc_0030F71D:
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 13784 + 1)) == 0) goto loc_0030F767;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 13784 + 1))) == 1) goto loc_0030F957;
    result = KiSendSoftwareInterruptAffinity(a1 + 13784 + 8, *(unsigned __int8 *)(a1 + 13784), a3, a4);
loc_0030F74A:
    if ((*(unsigned __int8 *)(a1 + 13784 + 1)) == 2) goto loc_0030FEBD;
loc_0030F754:
    *(unsigned __int8 *)(a1 + 13784 + 1) = 0;
    *(unsigned int *)(a1 + 13784 + 4) = 0xFFFFULL;
loc_0030F767:
    if (v_stack_m178 == 0) goto loc_003112AB;
    v_stack_m178 = *(unsigned __int64 *)(v_stack_m178);
loc_0030F77D:
    a4 = 0;
    result = KiDeferredReadySingleThread(a1, v_stack_m178 - 216, v_stack_m178, a4);
    v_r15 = (unsigned int)((v_r15) + 1);
    if (v_stack_m178 != 0) {
        result = *(unsigned __int64 *)(v_stack_m178);
        v_stack_m178 = result;
    }
    if ((((unsigned __int8)(v_r15)) & (15)) == 0) {
        a1 = a1 + 13784;
        result = KiFlushSoftwareInterruptBatch(a1, v_stack_m178 - 216, v_stack_m178, a4);
    }
    if (v_stack_m178 != 0) goto loc_0030F77D;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 13785)) == 0) goto loc_003112AB;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 13785))) == 1) goto loc_0030F994;
    result = KiSendSoftwareInterruptAffinity(a1 + 13792, *(unsigned __int8 *)(a1 + 13784), v_stack_m178, a4);
loc_0030F7EB:
    if ((*(unsigned __int8 *)(a1 + 13785)) == 2) goto loc_0030FEEC;
loc_0030F7FA:
    *(unsigned __int8 *)(a1 + 13785) = 0;
    *(unsigned int *)(a1 + 13788) = 0xFFFFULL;
    goto loc_003112AB;
loc_0030F814:
    v_stack_m120 = 31 + 33856;
    v_stack_m138 = 31;
    v_stack_m130 = (unsigned int)((unsigned int)(*(unsigned int *)(31 + 33752)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(31 + 33752))) == 0) goto loc_0030FEDB;
    v_rsi = ((unsigned int)((unsigned int)(31 + 16))) << (4);
    v_rsi = (v_rsi) + (31 + 33856);
    v_stack_m9C = (unsigned int)(31 + 16);
    v_stack_m128 = v_rsi;
    v_stack_m12C = (unsigned __int8)(31 + 16);
loc_0030F84E:
    v_stack_m108 = v_r15;
    v_stack_m198 = v_r15;
loc_0030F85D:
    v_stack_m18C = (unsigned int)((unsigned int)((unsigned int)(v_r15)));
loc_0030F861:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r15)))) >= 64) goto loc_0030FA6E;
    v_stack_m140 = v_r15;
    if (v_rsi == 0) goto loc_0030FA6E;
loc_0030F877:
    result = ((unsigned __int8)(31 + 16)) << (4);
    result = (result) + (31 + 33856);
    v_stack_m128 = *(unsigned __int64 *)(v_rsi);
    if ((*(unsigned __int64 *)(v_rsi)) != result) goto loc_0030FA77;
    v_stack_m130 = (unsigned int)((unsigned int)(v_stack_m130));
    if ((unsigned int)((unsigned int)(v_stack_m130)) == 0) goto loc_0030FA66;
    v_rsi = ((unsigned __int8)((unsigned __int8)(31 + 16))) << (4);
    v_rsi = (v_rsi) + (31 + 33856);
    v_stack_m98 = (unsigned int)((unsigned __int8)(31 + 16));
    v_stack_m12C = (unsigned __int8)((unsigned __int8)(31 + 16));
    goto loc_0030F877;
loc_0030F8C0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13332978)))) & (64)) == 0) goto loc_0030F5FB;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)(v_stack_m130), 31 + 33856, v_r15, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0030F5FB;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), 31 + 33856, v_r15, a4);
    goto loc_0030F5FD;
loc_0030F8E7:
    if (*(unsigned __int64 *)(31 + 33840) == 0) goto loc_0030F682;
    goto loc_0030F5C7;
loc_0030F8FC:
    v_stack_mB0 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 13788)));
    v_stack_mB8 = 6;
    v_stack_mAC = v_r15;
    v_rdi = 31;
    if (((unsigned __int8)(31 + 33856)) != 1) { v_rdi = 47; }
    result = HalpInterruptSendIpi(v_stack_mB8, (unsigned int)((unsigned int)(v_rdi)), v_r15, a4);
    goto loc_0030F6AD;
loc_0030F944:
    goto loc_0030F670;
loc_0030F957:
    v_stack_mB0 = (unsigned int)((unsigned int)(*(unsigned int *)(1 + 4)));
    v_stack_mB8 = 6;
    v_stack_mAC = v_r15;
    a2 = (unsigned int)((unsigned int)(v_rdi));
    if (((unsigned __int8)(*(unsigned __int8 *)(1))) != 1) { a2 = 47; }
    result = HalpInterruptSendIpi(v_stack_mB8, a2, *(unsigned __int8 *)(1), a4);
    goto loc_0030F74A;
loc_0030F994:
    v_stack_mB0 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 13788)));
    result = 0;
    v_stack_mB8 = 6;
    v_stack_mAC = 0;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 13784))) != 1) { v_rdi = 47; }
    result = HalpInterruptSendIpi(v_stack_mB8, (unsigned int)((unsigned int)(v_rdi)), *(unsigned __int8 *)(a1 + 13784), a4);
    goto loc_0030F7EB;
loc_0030F9DD:
    v_stack_mA0 = 1;
    a2 = (unsigned int)((*(unsigned __int8 *)(a1 + 209) + 1 * 1) & (63));
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsi) + 136)) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)(a2)));
    if (v_rdi == (*(unsigned __int64 *)(*(unsigned __int8 *)(a1 + 13784) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12662693) + a1 * 4)) * 8 + 16550976))) goto loc_0030F577;
    a3 = 0;
    result = KiMayStealStandbyThread(v_rdi, *(unsigned __int64 *)(*(unsigned __int8 *)(a1 + 13784) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12662693) + a1 * 4)) * 8 + 16550976), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0030F577;
    result = KiAttemptToStealStandbyThread(a1, v_rdi, *(unsigned __int64 *)(*(unsigned __int8 *)(a1 + 13784) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12662693) + a1 * 4)) * 8 + 16550976), a4);
    if ((unsigned __int8)(result) != 0) goto loc_0030F580;
    goto loc_0030F577;
loc_0030FA66:
    v_stack_m12C = 0;
    v_stack_m128 = v_r15;
loc_0030FA6E:
    goto loc_0030FA9C;
loc_0030FA77:
    a1 = (*(unsigned __int64 *)(v_stack_p10 + 8)) & (v_stack_p18);
    if (condition_is_not_equal) goto loc_0030FB5D;
loc_0030FA99:
    v_r15 = 0;
loc_0030FA9C:
    v_stack_m168 = v_rdi;
    v_stack_m160 = 0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 33840 + 8))) & (1)) != 0) goto loc_0030FF12;
loc_0030FABD:
    if (*(unsigned __int64 *)(v_rdi + 33840 + 8) != 0) goto loc_0030FF28;
loc_0030FAC6:
loc_0030FACF:
loc_0030FAD5:
    v_stack_m100 = 0;
    v_stack_p28 = 0;
    v_stack_m198 = 0;
    v_r14 = 0;
loc_0030FAF0:
    if (0 >= 64) goto loc_0030F623;
loc_0030FAFA:
    if (v_stack_m160 == 0) goto loc_0030F623;
    if (v_stack_m150 == 0) goto loc_00310798;
loc_0030FB0F:
    result = ((unsigned __int8)(v_stack_m154)) << (4);
    result = (result) + (v_stack_m148);
    v_stack_m150 = *(unsigned __int64 *)(v_stack_m150);
    if ((*(unsigned __int64 *)(v_stack_m150)) != result) goto loc_0030F608;
    v_stack_m158 = (unsigned int)((unsigned int)(v_stack_m158));
    if ((unsigned int)((unsigned int)(v_stack_m158)) == 0) goto loc_00310788;
    a4 = ((unsigned __int8)((unsigned __int8)(v_stack_m154))) << (4);
    a4 = (a4) + (v_stack_m148);
    v_stack_m84 = (unsigned int)((unsigned __int8)(v_stack_m154));
    v_stack_m154 = (unsigned __int8)((unsigned __int8)(v_stack_m154));
    goto loc_0030FB0F;
loc_0030FB5D:
    result = ~(v_rip - 3209817);
    result = (result) & ((unsigned int)(v_stack_m158));
    v_stack_m140 = result;
    if (condition_is_equal) goto loc_0030FA99;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14 + 136))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_r15 + 576)))) goto loc_00310952;
loc_0030FB8D:
    result = KiComputeThreadQos(0, v_rdi, v_rip - 3209817, a4);
    a3 = (unsigned int)(*(unsigned int *)(v_r15 + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 84))))) { a3 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 84))); }
    a2 = 0;
    a2 = (((unsigned int)(a3)) >= (*(unsigned int *)(v_rip + 13326279))) ? 1 : 0;
    a3 = (unsigned int)((a2 + result * 2) * ((unsigned int)(*(unsigned __int8 *)(v_r14 + 185))));
    a3 = (unsigned int)((a3) + ((unsigned int)(*(unsigned __int8 *)(v_r15 + 517))));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 576) + *(unsigned __int16 *)(v_r14 + 136) * 8 + 8)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 192) + a3 + a3 * 2 * 8 + 16));
    v_rsi = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 576) + *(unsigned __int16 *)(v_r14 + 136) * 8 + 8);
    if (condition_is_not_equal) { v_rsi = result; }
    result = ((unsigned int)(*(unsigned int *)(v_r15 + 120))) >> (1);
    result = (unsigned int)((result) & (1));
    a1 = (*(unsigned __int64 *)(v_r14 + result * 8 + 16)) & (v_rsi);
    v_rsi = (v_stack_m140) & (a1);
    v_stack_m140 = v_rsi;
    if (*(unsigned __int64 *)(v_r15 + 104) != 0) goto loc_003106D2;
loc_0030FC1A:
    if (v_rsi != 0) goto loc_0030FD83;
    if ((*(unsigned __int64 *)(v_r15 + 568)) != (*(unsigned __int64 *)(v_rip + 13332430))) goto loc_00310872;
loc_0030FC3C:
loc_0030FC40:
    result = (unsigned int)(((unsigned int)(v_stack_m18C)) + 1);
    v_r15 = 0;
    goto loc_0030F85D;
loc_0030FC5A:
    result = ~(0);
    result = (result) & (a1);
    v_stack_m118 = result;
    if (condition_is_equal) goto loc_0030F623;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m150) + 33856 + 136))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m150) + 576)))) goto loc_00310959;
loc_0030FC89:
    result = KiComputeThreadQos(*(unsigned __int64 *)(v_stack_m150), *(unsigned __int64 *)(v_stack_m150) + 33856, v_stack_m198, a4);
    a3 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m150) + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m150) + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m150) + 84))))) { a3 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m150) + 84))); }
    a2 = (((unsigned int)(a3)) >= (*(unsigned int *)(v_rip + 13326021))) ? 1 : 0;
    a3 = (unsigned int)((a2 + result * 2) * ((unsigned int)(*(unsigned __int8 *)(v_stack_p10 + 185))));
    a3 = (unsigned int)((a3) + ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m150) + 517))));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m150) + 576) + *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m150) + 33856 + 136) * 8 + 8)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 192) + a3 + a3 * 2 * 8 + 16));
    v_rsi = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m150) + 576) + *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m150) + 33856 + 136) * 8 + 8);
    if (condition_is_not_equal) { v_rsi = result; }
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m150) + 120))) >> (1);
    result = (unsigned int)((result) & (1));
    a1 = (*(unsigned __int64 *)(v_stack_p10 + result * 8 + 16)) & (v_rsi);
    v_rsi = (v_stack_m118) & (a1);
    v_stack_m118 = v_rsi;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m150) + 104) != 0) goto loc_0031073B;
loc_0030FD1B:
    if (v_rsi != 0) goto loc_0030FE2E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m150) + 568)) != (*(unsigned __int64 *)(v_rip + 13332173))) goto loc_003108A7;
loc_0030FD38:
    v_r13 = (unsigned int)((0) + 1);
loc_0030FD3B:
    v_stack_p28 = (unsigned int)(v_r13);
loc_0030FD42:
    goto loc_0030FAF0;
loc_0030FD5D:
    *(unsigned __int64 *)(a1 + 13792) = 0x200001ULL;
    a2 = 0;
    result = memset(a1 + 13800, a2, 256, v_stack_m150);
    goto loc_0030F6BC;
loc_0030FD83:
    result = KiCheckThreadAffinity(0, a2, 256, v_stack_m150);
    if ((unsigned int)(result) == 0) goto loc_00310961;
loc_0030FD96:
    if (v_stack_p18 != 0) goto loc_0030FF6D;
    if (v_stack_p18 == 0) goto loc_003108D1;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p10 + 136)) << (6));
    a1 = (unsigned int)((a1) + (0));
    v_stack_m8C = (unsigned int)(v_stack_p18);
    v_stack_m8C = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r15 + 120)))) & (2)) == 0) goto loc_00310A14;
    result = (v_stack_m198) | (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3210711 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12661751) + a1 * 4)) * 8 + 16550976) + 36448));
loc_0030FDF7:
loc_0030FDFE:
    v_stack_m198 = result;
    v_stack_m128 = *(unsigned __int64 *)(v_r13 + 8);
    result = KiRemoveThreadFromReadyQueue(v_stack_m138, v_r15 + 216, (unsigned int)((unsigned int)(v_stack_m12C)), v_stack_m150);
    result = KiInsertDeferredReadyList(v_stack_m180, 0, (unsigned int)((unsigned int)(v_stack_m12C)), v_stack_m150);
    goto loc_0031023A;
loc_0030FE2E:
    result = KiCheckThreadAffinity(*(unsigned __int64 *)(v_stack_m150), 0, (unsigned int)((unsigned int)(v_stack_m12C)), v_stack_m150);
    if ((unsigned int)(result) == 0) goto loc_003109B5;
loc_0030FE41:
    if (*(unsigned __int64 *)(v_r13 + 8) != 0) goto loc_00310369;
    if (*(unsigned __int64 *)(v_r13 + 8) == 0) goto loc_003108F8;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_m150 + 136)) << (6));
    a1 = (unsigned int)((a1) + (0));
    v_stack_m74 = 0;
    if (((2) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m150) + 120))))) == 0) goto loc_00310A20;
    v_r15 = (v_r15) | (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3210872 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12661590) + a1 * 4)) * 8 + 16550976) + 36448));
loc_0030FE92:
    v_stack_m198 = v_r15;
    result = KiRemoveCurrentThreadScbReadyQueueEnumerator(v_stack_m168, *(unsigned __int64 *)(v_stack_m150), (unsigned int)((unsigned int)(v_stack_m12C)), v_stack_m150);
    result = KiInsertDeferredReadyList(v_stack_m180, *(unsigned __int64 *)(v_stack_m150), (unsigned int)((unsigned int)(v_stack_m12C)), v_stack_m150);
    goto loc_0030FD42;
loc_0030FEBD:
    *(unsigned __int64 *)(2 + 8) = 0x200001ULL;
    a2 = 0;
    result = memset(2 + 16, a2, 256, v_stack_m150);
    goto loc_0030F754;
loc_0030FEDB:
    v_stack_m128 = v_r15;
    goto loc_0030F84E;
loc_0030FEEC:
    *(unsigned __int64 *)(a1 + 13792) = 0x200001ULL;
    a2 = 0;
    result = memset(a1 + 13800, a2, 256, v_stack_m150);
    goto loc_0030F7FA;
loc_0030FF12:
    if ((a1 + 13800) == 1) goto loc_0030FAC6;
    result = (result) | (1);
    result = (result) ^ (a1 + 13800);
    goto loc_0030FABD;
loc_0030FF28:
    result = (result) + (-88);
    v_stack_m160 = result;
    v_stack_m158 = (unsigned int)(*(unsigned __int16 *)(result + 32));
    v_stack_m148 = result + 144;
    if ((unsigned int)(*(unsigned __int16 *)(result + 32)) == 0) goto loc_00310945;
    a4 = ((unsigned int)((unsigned int)(v_stack_m154))) << (4);
    a4 = (a4) + (result + 144);
    v_stack_m88 = (unsigned int)(v_stack_m154);
    v_stack_m150 = a4;
    v_stack_m154 = (unsigned __int8)(v_stack_m154);
    goto loc_0030FAD5;
loc_0030FF6D:
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p10 + 136)) << (6));
    a1 = (unsigned int)((a1) + (0));
    v_stack_m90 = 0;
    v_stack_m90 = 0;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 120))) >> (1));
    a2 = (unsigned int)((a2) & (1));
    v_stack_m188 = *(unsigned __int64 *)(v_rip - 3211180 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12661294) + a1 * 4)) * 8 + 16550976);
    result = KiTryAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(v_rip - 3211180 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12661294) + a1 * 4)) * 8 + 16550976), a2, v_stack_m108, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00310830;
    result = KiIsIsolationUnitIdleByHandle(v_stack_m108, a2, v_stack_m108, a4);
    if ((unsigned int)(result) == 0) goto loc_00310A44;
    if (*(unsigned __int64 *)(v_r15 + 104) == 0) goto loc_00310017;
    a3 = ((unsigned int)(*(unsigned int *)(v_stack_m188 + 216))) + (*(unsigned __int64 *)(v_r15 + 104));
    result = KiIsThreadConstrainedBySchedulingGroup(v_r15, v_stack_m188, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00310017;
    result = KiShouldPreemptionBeDeferred(v_r15, v_stack_m188, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00310017;
    result = KiCheckForMaxOverQuotaScb(a3, v_stack_m188, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00311242;
loc_00310017:
    v_stack_m128 = *(unsigned __int64 *)((unsigned int)(a5) + 8);
    result = KiRemoveThreadFromReadyQueue(v_stack_m138, (unsigned int)(a5), (unsigned int)((unsigned int)(v_stack_m12C)), a4);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(a1 + 14312), a2, 240, a4);
    a3 = 0;
    result = KiStartRescheduleContext(*(unsigned __int64 *)(a1 + 14312), v_stack_m108, a3, a4);
    a4 = 0;
    v_stack_m1A8 = v_stack_m180;
    result = KiScheduleThreadToRescheduleContext(*(unsigned __int64 *)(a1 + 14312), v_r15, v_stack_m188, a4);
    v_r10 = 0;
    result = 0;
    if (((*(unsigned int *)(v_rip + 13331083)) & (0x400ULL)) != 0) { result = 2; }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_003100E4;
loc_003100A1:
    a1 = (0 * 4 + 2) + (0);
    a1 = (a1 * 8) + (*(unsigned __int64 *)(a1 + 14312));
    result = KiCommitRescheduleContextEntry(a1, a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m180);
    v_rbx = (unsigned __int8)((0) | ((unsigned __int8)(result)));
    v_r15 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r15)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_003100A1;
loc_003100E4:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 8)) != 1) goto loc_00310107;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1)) + 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1) = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) >= (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440)))) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1) = 0;
    }
    v_r15 = 0;
    a4 = (v_stack_m108) & (-2);
    v_stack_m58 = a4;
    result = (unsigned int)((v_stack_m108) & (1));
    if (condition_is_equal) goto loc_00310814;
    if (((unsigned int)(result)) == 1) {
        result = *(unsigned __int64 *)(a4 + 36440);
        a3 = *(unsigned __int64 *)(a4 + 36440);
        a3 = (a3) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_0031016B;
loc_00310150:
    if ((unsigned int)(a2 - 1) != 0) goto loc_00310150;
loc_0031016B:
    v_stack_m108 = 0;
    if ((unsigned __int8)((unsigned __int8)(v_rbx)) == 0) goto loc_00310930;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_00310930;
loc_00310190:
    v_rsi = (0 + 0 * 4 * 8) + (*(unsigned __int64 *)(a1 + 14312));
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 51))) & (16)) != 0) goto loc_00310252;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi + 51))) & (8)) == 0) goto loc_003101E4;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsi + 16) + 7)) == 0) goto loc_003101E4;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 13785)) != 0) goto loc_0031027B;
loc_003101CF:
    *(unsigned __int8 *)(a1 + 13785) = 1;
    *(unsigned int *)(a1 + 13788) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 16) + 36)));
loc_003101E4:
    if (((*(unsigned __int8 *)(v_rsi + 51)) & (2)) != 0) goto loc_003107EC;
loc_003101ED:
    if (((*(unsigned __int8 *)(v_rsi + 51)) & (4)) == 0) goto loc_00310207;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 16) + 36536) != 0) goto loc_003102C7;
loc_00310207:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 16) + 36536);
    if (((*(unsigned __int8 *)(v_rsi + 51)) & (1)) != 0) {
        result = *(unsigned __int64 *)(v_rsi + 40);
    }
    v_r15 = (unsigned int)((v_r15) + 1);
    if (((unsigned int)(v_r15)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_00310190;
loc_0031023A:
    v_r15 = 0;
    goto loc_0030F861;
loc_00310252:
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 13785)) == 0) goto loc_003101CF;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 13785))) != 1) goto loc_003102A6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 13788)))) == (*(unsigned int *)(v_stack_m12C + 36))) goto loc_003101E4;
    goto loc_00310291;
loc_0031027B:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 13785))) != 1) goto loc_003102A6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 13788)))) == (*(unsigned int *)(v_stack_m12C + 36))) goto loc_003101E4;
loc_00310291:
    *(unsigned __int8 *)(a1 + 13785) = 2;
    result = KeAddProcessorAffinityEx(a1 + 13792, (unsigned int)(*(unsigned int *)(a1 + 13788)), v_stack_m198, a4);
loc_003102A6:
    result = KeAddGroupAffinityEx(a1 + 13792, *(unsigned __int8 *)(v_stack_m12C + 208), *(unsigned __int64 *)(v_stack_m12C + 200), a4);
    goto loc_003101E4;
loc_003102C7:
    if ((*(unsigned __int64 *)(a1 + 36536)) == 0) goto loc_00310207;
    if (a1 == v_stack_m12C) goto loc_00310207;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result))))) & (0x40000ULL));
    result = a1 + 36536;
    if (!(condition_is_equal)) {
        result = a1 + 36536;
    }
    if (condition_is_above_or_equal) goto loc_003111B7;
loc_00310309:
    *(unsigned int *)(*(unsigned __int64 *)(result) + 12) = 2;
    v_stack_m188 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m12C + 36)));
    if ((*(unsigned __int8 *)(v_rip + 13323511)) == 0) {
        result = *(unsigned __int8 *)(a5 + (unsigned int)(*(unsigned int *)(v_stack_m12C + 36)) * 2 + 16568929);
        a1 = *(unsigned __int8 *)(a5 + (unsigned int)(*(unsigned int *)(v_stack_m12C + 36)) * 2 + 16568928);
        a1 = (unsigned int)((a1) << (6));
        a1 = (unsigned int)((a1) | ((unsigned int)(result)));
        v_stack_m188 = (unsigned int)(a1);
    }
    *(unsigned int *)(*(unsigned __int64 *)(result) + 8) = (unsigned int)(a1);
    result = (unsigned int)(*(unsigned int *)(v_rip + 13330386));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13330386)))) & (32)) != 0) {
        a1 = *(unsigned int *)(v_stack_m12C + 36);
        a2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(a1, a2, (unsigned int)(*(unsigned int *)(result)), a4);
        a1 = v_stack_m188;
    }
    a2 = ((unsigned int)((unsigned int)(a1))) >> (32);
    goto loc_00310207;
loc_00310369:
    a1 = (unsigned int)((*(unsigned __int16 *)(a4 + 136)) << (6));
    v_stack_m78 = 0;
    a1 = (unsigned int)((a1) + ((unsigned int)(a2)));
    v_stack_m78 = (unsigned int)(a2);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a5 + 120))) >> (1));
    a2 = (unsigned int)((a2) & (1));
    result = KiTryAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(v_rip - 3212193 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12660284) + a1 * 4)) * 8 + 16550976), a2, v_stack_m100, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00310847;
    result = KiIsIsolationUnitIdleByHandle(v_stack_m100, a2, v_stack_m100, a4);
    if ((unsigned int)(result) == 0) goto loc_00311282;
    if (*(unsigned __int64 *)(a5 + 104) == 0) goto loc_00310402;
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 3212193 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12660284) + a1 * 4)) * 8 + 16550976) + 216))) + (*(unsigned __int64 *)(a5 + 104));
    result = KiIsThreadConstrainedBySchedulingGroup(a5, a2, v_stack_m100, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00310402;
    result = KiShouldPreemptionBeDeferred(a5, a2, v_stack_m100, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00310402;
    result = KiCheckForMaxOverQuotaScb(a2, a2, v_stack_m100, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0031127E;
loc_00310402:
    result = KiRemoveCurrentThreadScbReadyQueueEnumerator(v_stack_m168, a5, v_stack_m100, a4);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(a1 + 14312), a2, 240, a4);
    a3 = 0;
    result = KiStartRescheduleContext(*(unsigned __int64 *)(a1 + 14312), v_stack_m100, a3, a4);
    a4 = 0;
    v_stack_m1A8 = v_stack_m180;
    result = KiScheduleThreadToRescheduleContext(*(unsigned __int64 *)(a1 + 14312), a5, *(unsigned __int64 *)(v_rip - 3212193 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12660284) + a1 * 4)) * 8 + 16550976), a4);
    v_r14 = 0;
    v_rsi = 0;
    if (((*(unsigned int *)(v_rip + 13330096)) & (0x400ULL)) != 0) { v_rsi = 2; }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_003104A3;
loc_00310472:
    a1 = (0 * 4 + 2) + (0);
    result = KiCommitRescheduleContextEntry(*(unsigned __int64 *)(a1 + 14312) + a1 * 8, a1, (unsigned int)((unsigned int)(v_rsi)), v_stack_m180);
    v_r14 = (unsigned __int8)((v_r14) | ((unsigned __int8)(result)));
    v_rdi = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rdi)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_00310472;
    v_r10 = 0;
loc_003104A3:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 8)) != 1) goto loc_003104C6;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1)) + 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1) = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) >= (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440)))) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 16) + 36440) + 1) = 0;
    }
    a4 = (v_stack_m100) & (-2);
    v_stack_m50 = a4;
    result = (unsigned int)((v_stack_m100) & (1));
    if (condition_is_equal) goto loc_00310822;
    if (((unsigned int)(result)) == 1) {
        result = *(unsigned __int64 *)(a4 + 36440);
        a3 = *(unsigned __int64 *)(a4 + 36440);
        a3 = (a3) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_00310523;
loc_00310510:
    if ((unsigned int)(a2 - 1) != 0) goto loc_00310510;
loc_00310523:
    v_stack_m100 = 0;
    if ((unsigned __int8)(v_r14) == 0) goto loc_003105CB;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_003105CB;
loc_00310540:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 51))) & (16)) != 0) goto loc_00310565;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 51))) & (8)) == 0) goto loc_00310586;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 7)) == 0) goto loc_00310586;
loc_00310565:
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 13785)) != 0) goto loc_003105DF;
    *(unsigned __int8 *)(a1 + 13785) = 1;
    *(unsigned int *)(a1 + 13788) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36)));
loc_00310586:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 51)) & (2)) != 0) goto loc_00310800;
loc_0031058F:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 51)) & (4)) == 0) goto loc_003105A9;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36536) != 0) goto loc_0031062D;
loc_003105A9:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36536);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 51)) & (1)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 40);
    }
    v_r14 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r14)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))))) goto loc_00310540;
loc_003105CB:
    v_r14 = 0;
    goto loc_0030FD42;
loc_003105DF:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312)))) != 1) goto loc_00310623;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 13788)))) == (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36))) goto loc_00310586;
    *(unsigned __int8 *)(a1 + 13785) = 2;
    result = KeAddProcessorAffinityEx(a1 + 13792, (unsigned int)(*(unsigned int *)(a1 + 13788)), a3, a4);
loc_00310608:
    result = KeAddGroupAffinityEx(a1 + 13792, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 208), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 200), a4);
    goto loc_00310586;
loc_00310623:
    goto loc_00310608;
loc_0031062D:
    if ((*(unsigned __int64 *)(a1 + 36536)) == 0) goto loc_003105A9;
    if (a1 == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16))) goto loc_003105A9;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result))))) & (0x40000ULL));
    result = a1 + 36536;
    if (!(condition_is_equal)) {
        result = a1 + 36536;
    }
    if (condition_is_above_or_equal) goto loc_003111D9;
loc_0031066F:
    *(unsigned int *)(*(unsigned __int64 *)(result) + 12) = 2;
    v_r13 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36));
    if ((*(unsigned __int8 *)(v_rip + 13322641)) == 0) {
        result = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36)));
        a2 = v_rip - 3212940;
        v_r13 = *(unsigned __int8 *)(a2 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36)) * 2 + 16568928);
        v_r13 = (unsigned int)((v_r13) << (6));
        result = *(unsigned __int8 *)(a2 + result * 2 + 16568929);
        v_r13 = (unsigned int)((v_r13) | ((unsigned int)(result)));
    }
    *(unsigned int *)(*(unsigned __int64 *)(result) + 8) = (unsigned int)(v_r13);
    result = (unsigned int)(*(unsigned int *)(v_rip + 13329510));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13329510)))) & (32)) != 0) {
        a1 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16) + 36);
        a2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(a1, a2, (unsigned int)(*(unsigned int *)(result)), a4);
    }
    a2 = ((unsigned int)((unsigned int)(v_r13))) >> (32);
    goto loc_003105A9;
loc_003106D2:
    result = KiIsThreadConstrainedBySchedulingGroup(v_stack_m198, a2, (unsigned int)(*(unsigned int *)(result)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0030FC1A;
    result = KiShouldPreemptionBeDeferred(v_stack_m198, a2, (unsigned int)(*(unsigned int *)(result)), a4);
    if ((unsigned __int8)(result) != 0) goto loc_0030FC1A;
    result = KiReduceToUnderMaxQuotaSet(*(unsigned __int16 *)(v_r14 + 136), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 16), (unsigned int)(*(unsigned int *)(result)), a4);
    v_stack_m140 = result;
    if ((*(unsigned int *)(v_rip + 13329938)) == 0) goto loc_0030FC1A;
    result = KiIsThreadRankBiased(v_stack_m198, a1, (unsigned int)(*(unsigned int *)(result)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0030FC1A;
    result = KiFindRankBiasedIdleSmtSet(0, v_stack_m140, (unsigned int)(*(unsigned int *)(result)), a4);
    goto loc_0030FC1A;
loc_0031073B:
    result = KiIsThreadConstrainedBySchedulingGroup(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8, v_stack_m140, (unsigned int)(*(unsigned int *)(result)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0030FD1B;
    result = KiShouldPreemptionBeDeferred(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8, v_stack_m140, (unsigned int)(*(unsigned int *)(result)), a4);
    if ((unsigned __int8)(result) != 0) goto loc_0030FD1B;
    result = KiReduceToUnderMaxQuotaSet(*(unsigned __int16 *)(a4 + 136), v_stack_m140, (unsigned int)(*(unsigned int *)(result)), a4);
    v_stack_m118 = result;
    if ((*(unsigned int *)(v_rip + 13329833)) != 0) goto loc_00311252;
loc_0031077C:
    goto loc_0030FD1B;
loc_00310788:
    v_r10 = 0;
    v_stack_m150 = 0;
    v_stack_m154 = 0;
loc_00310798:
    result = KiDetermineNextScbForScbReadyQueueEnumerator(v_stack_m160, v_stack_m140, (unsigned int)(*(unsigned int *)(result)), 0);
    if (result == 0) goto loc_003107E2;
    v_stack_m158 = (unsigned int)(*(unsigned __int16 *)(result + 120));
    v_stack_m148 = result + 144;
    if ((unsigned int)(*(unsigned __int16 *)(result + 120)) == 0) goto loc_0031090A;
    a4 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 120)))) << (4);
    a4 = (a4) + (result + 144);
    v_stack_m80 = (unsigned int)(*(unsigned __int16 *)(result + 120));
    v_stack_m150 = a4;
    v_stack_m154 = (unsigned __int8)(*(unsigned __int16 *)(result + 120));
loc_003107E2:
    v_stack_m160 = result;
    goto loc_0030FAFA;
loc_003107EC:
    a3 = 0;
    result = EtwTraceScheduleThread(*(unsigned __int64 *)(result + 40), 0, a3, a4);
    goto loc_003101ED;
loc_00310800:
    a3 = 0;
    result = EtwTraceScheduleThread(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 40), result, a3, a4);
    goto loc_0031058F;
loc_00310814:
    goto loc_00310150;
loc_00310822:
    goto loc_00310510;
loc_00310830:
    result = ~(*(unsigned __int64 *)(v_stack_m188 + 200));
    v_r14 = (v_r14) & (result);
    goto loc_0030FD96;
loc_00310847:
    result = ~(*(unsigned __int64 *)(v_r13 + 200));
    v_r14 = (v_r14) & (result);
    goto loc_0030FE41;
loc_00310860:
    result = KiReadyDeferredReadyList(a1, v_stack_m180, v_stack_m188, v_stack_p10);
    goto loc_003112AB;
loc_00310872:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m198 + 116)))) & (8)) != 0) goto loc_0030FC3C;
    v_stack_m128 = *(unsigned __int64 *)(v_r13 + 8);
    result = KiRemoveThreadFromReadyQueue(v_stack_m138, v_r13, (unsigned int)((unsigned int)(v_r14)), v_stack_p10);
    result = KiInsertDeferredReadyList(v_stack_m180, v_stack_m198, (unsigned int)((unsigned int)(v_r14)), v_stack_p10);
    goto loc_0030FC40;
loc_003108A7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 116)))) & (8)) != 0) goto loc_0030FD38;
    result = KiRemoveCurrentThreadScbReadyQueueEnumerator(v_stack_m168, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8, (unsigned int)((unsigned int)(v_r14)), v_stack_p10);
    result = KiInsertDeferredReadyList(v_stack_m180, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8, (unsigned int)((unsigned int)(v_r14)), v_stack_p10);
    goto loc_0030FD38;
loc_003108D1:
    result = (unsigned int)(((unsigned int)(v_stack_m18C)) + 1);
    v_r15 = 0;
    v_stack_m18C = (unsigned int)(result);
    goto loc_0030F861;
loc_003108F8:
    v_r13 = (unsigned int)(((unsigned int)(a5)) + 1);
    v_r14 = 0;
    goto loc_0030FD3B;
loc_0031090A:
    v_stack_m150 = 0;
    v_stack_m154 = 32;
    v_stack_m160 = v_stack_m180;
    goto loc_0030FAFA;
loc_00310930:
    goto loc_0030F861;
loc_00310945:
    v_stack_m150 = 0;
    goto loc_0030FACF;
loc_00310952:
    v_rsi = 0;
    goto loc_0030FB8D;
loc_00310959:
    goto loc_0030FC89;
loc_00310961:
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r14 + 136)) << (6));
    v_stack_m94 = 0;
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 33856)));
    v_stack_m94 = (unsigned int)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 33856);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r15 + 120)))) & (2)) == 0) goto loc_00310A2C;
    result = (v_stack_m198) | (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3213709 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12658760) + a1 * 4)) * 8 + 16550976) + 36448));
    goto loc_0030FDFE;
loc_003109B5:
    a1 = (unsigned int)((*(unsigned __int16 *)(0 + 136)) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)(v_r13)));
    v_stack_m7C = (unsigned int)(v_r13);
    if (((2) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 120))))) == 0) goto loc_00310A3B;
    v_r15 = (v_r15) | (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3213786 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12658676) + a1 * 4)) * 8 + 16550976) + 36448));
loc_003109F0:
    v_stack_m198 = v_r15;
    result = KiRemoveCurrentThreadScbReadyQueueEnumerator(v_stack_m168, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8, v_stack_m198, 0);
    result = KiInsertDeferredReadyList(v_stack_m180, *(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8, v_stack_m198, 0);
    goto loc_0030FD42;
loc_00310A14:
    result = (result) | (*(unsigned __int64 *)(v_stack_m180 + 200));
    goto loc_0030FDF7;
loc_00310A20:
    v_r15 = (v_r15) | (*(unsigned __int64 *)(v_stack_m180 + 200));
    goto loc_0030FE92;
loc_00310A2C:
    result = (result) | (*(unsigned __int64 *)(v_stack_m180 + 200));
    goto loc_0030FDFE;
loc_00310A3B:
    v_r15 = (v_r15) | (*(unsigned __int64 *)(v_stack_m180 + 200));
    goto loc_003109F0;
loc_00310A44:
loc_00310A50:
    result = ~(*(unsigned __int64 *)(v_stack_m188 + 200));
    v_rsi = (0) & (result);
    v_r14 = (v_r14) & (result);
    v_stack_m140 = v_rsi;
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_m108, v_r13, v_stack_m188, 0);
    goto loc_0030FD96;
loc_00310A6B:
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 13785)) != 0) goto loc_00310C72;
    *(unsigned __int8 *)(a1 + 13785) = 1;
    *(unsigned int *)(a1 + 13788) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 36)));
loc_00310A90:
    if (((*(unsigned __int8 *)(2 + 51)) & ((unsigned __int8)(v_r14))) != 0) goto loc_0031107F;
loc_00310A9A:
    if (((*(unsigned __int8 *)(2 + 51)) & (4)) == 0) goto loc_00310AB4;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 36536) != 0) goto loc_00310CC4;
loc_00310AB4:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + 0 + 0 * 4 * 8 + 36536);
    if (((*(unsigned __int8 *)(2 + 51)) & (1)) != 0) {
        result = *(unsigned __int64 *)(2 + 40);
    }
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((unsigned int)(v_rsi)) < ((unsigned int)(*(unsigned __int8 *)(v_r15)))) goto loc_00310C40;
loc_00310AE7:
    v_r15 = 0;
    goto loc_00310DCB;
loc_00310AEF:
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p10 + 136)) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)(v_r13)));
    v_stack_m68 = 0;
    v_stack_m68 = (unsigned int)(v_r13);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m188))) >> (1));
    a2 = (unsigned int)((a2) & (1));
    result = KiTryAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(v_rip - 3214125 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12658352) + a1 * 4)) * 8 + 16550976), a2, v_stack_mF0, 0);
    if ((unsigned __int8)(result) == 0) goto loc_00311093;
    result = KiIsIsolationUnitIdleByHandle(v_stack_mF0, a2, v_stack_mF0, 0);
    if ((unsigned int)(result) == 0) goto loc_0031117B;
    if (*(unsigned __int64 *)(v_r15) == 0) goto loc_00310B91;
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 3214125 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12658352) + a1 * 4)) * 8 + 16550976) + 216))) + (*(unsigned __int64 *)(v_r15));
    result = KiIsThreadConstrainedBySchedulingGroup(v_stack_mF8, a2, v_stack_mF0, 0);
    if ((unsigned __int8)(result) == 0) goto loc_00310B91;
    result = KiShouldPreemptionBeDeferred(v_stack_mF8, a2, v_stack_mF0, 0);
    if ((unsigned __int8)(result) != 0) goto loc_00310B91;
    result = KiCheckForMaxOverQuotaScb(a2, a2, v_stack_mF0, 0);
    if ((unsigned __int8)(result) != 0) goto loc_00311177;
loc_00310B91:
    v_stack_mC8 = *(unsigned __int64 *)(v_stack_mC8 + 8);
    result = KiRemoveThreadFromSharedReadyQueue(v_stack_mD8, v_stack_mF8, v_stack_mCC, 0);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(a1 + 14312), a2, 240, 0);
    a3 = 0;
    result = KiStartRescheduleContext(*(unsigned __int64 *)(a1 + 14312), v_stack_mF0, a3, 0);
    a4 = 0;
    v_stack_m1A8 = v_stack_m178;
    result = KiScheduleThreadToRescheduleContext(*(unsigned __int64 *)(a1 + 14312), v_stack_mF8, *(unsigned __int64 *)(v_rip - 3214125 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12658352) + a1 * 4)) * 8 + 16550976), a4);
    a3 = 0;
    result = KiCommitRescheduleContext(*(unsigned __int64 *)(a1 + 14312), a1, a3, v_stack_m178);
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_mF0, a1, a3, v_stack_m178);
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_00310DD4;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312))) <= 0) goto loc_00310AE7;
loc_00310C40:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_rsi + v_rsi * 4 * 8 + 51))) & (16)) != 0) goto loc_00310A6B;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_rsi + v_rsi * 4 * 8 + 51))) & (8)) == 0) goto loc_00310A90;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_rsi + v_rsi * 4 * 8 + 16) + 7)) == 0) goto loc_00310A90;
    goto loc_00310A6B;
loc_00310C72:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14312) + v_rsi + v_rsi * 4 * 8 + 51))) != 1) goto loc_00310CBA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 13788)))) == (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_rsi + v_rsi * 4 * 8 + 16) + 36))) goto loc_00310A90;
    *(unsigned __int8 *)(a1 + 13785) = (unsigned __int8)(v_rsi + 2);
    result = KeAddProcessorAffinityEx(a1 + 13792, (unsigned int)(*(unsigned int *)(a1 + 13788)), a3, v_stack_m178);
loc_00310C9F:
    result = KeAddGroupAffinityEx(a1 + 13792, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_rsi + v_rsi * 4 * 8 + 16) + 208), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_rsi + v_rsi * 4 * 8 + 16) + 200), v_stack_m178);
    goto loc_00310A90;
loc_00310CBA:
    goto loc_00310C9F;
loc_00310CC4:
    if ((*(unsigned __int64 *)(a1 + 36536)) == 0) goto loc_00310AB4;
    if (a1 == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_rsi + v_rsi * 4 * 8 + 16))) goto loc_00310AB4;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result))))) & (0x40000ULL));
    result = a1 + 36536;
    if (!(condition_is_equal)) {
        result = a1 + 36536;
    }
    if (condition_is_above_or_equal) goto loc_00311220;
loc_00310D06:
    *(unsigned int *)(*(unsigned __int64 *)(result) + 12) = (unsigned int)(v_rsi + 2);
    v_r13 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_rsi + v_rsi * 4 * 8 + 16) + 36));
    if ((*(unsigned __int8 *)(v_rip + 13320954)) == 0) {
        result = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_rsi + v_rsi * 4 * 8 + 16) + 36)));
        a2 = v_rip - 3214628;
        v_r13 = *(unsigned __int8 *)(a2 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_rsi + v_rsi * 4 * 8 + 16) + 36)) * 2 + 16568928);
        v_r13 = (unsigned int)((v_r13) << (6));
        result = *(unsigned __int8 *)(a2 + result * 2 + 16568929);
        v_r13 = (unsigned int)((v_r13) | ((unsigned int)(result)));
    }
    *(unsigned int *)(*(unsigned __int64 *)(result) + 8) = (unsigned int)(v_r13);
    result = (unsigned int)(*(unsigned int *)(v_rip + 13327822));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13327822)))) & (32)) != 0) {
        a1 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_rsi + v_rsi * 4 * 8 + 16) + 36);
        a2 = (unsigned int)(v_rsi + 2);
        result = EtwTraceXSchedulerPriorityKickSend(a1, a2, (unsigned int)(*(unsigned int *)(result)), a4);
    }
    a2 = ((unsigned int)((unsigned int)(v_r13))) >> (32);
    goto loc_00310AB4;
loc_00310D6B:
    v_stack_mE0 = v_rsi + 2;
    v_stack_mE8 = *(unsigned __int64 *)(a1 + 14312);
    if (v_stack_mE8 != 0) goto loc_00311009;
loc_00310D84:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 2 + 8))) & ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14312) + v_rsi + v_rsi * 4 * 8 + 16))));
    v_stack_mD8 = v_rsi + 2;
    v_stack_mD0 = (unsigned int)(result);
    v_stack_mC0 = v_rsi + 2 + 64;
    if (condition_is_equal) goto loc_00311000;
    a1 = ((unsigned int)((unsigned int)(result))) << (4);
    a1 = (a1) + (v_rsi + 2 + 64);
    v_stack_m6C = (unsigned int)(result);
    v_stack_mC8 = a1;
    v_stack_mCC = (unsigned __int8)(result);
loc_00310DB5:
    v_stack_mF0 = *(unsigned __int64 *)(a1 + 14312);
    v_stack_p28 = (unsigned int)(*(unsigned __int64 *)(a1 + 14312));
    v_stack_m198 = *(unsigned __int64 *)(a1 + 14312);
loc_00310DCB:
    goto loc_00310DD7;
loc_00310DD4:
    v_r15 = 0;
loc_00310DD7:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 14312))))) >= 64) goto loc_00310DFF;
    v_stack_mF8 = 0;
    result = KiAdvanceReadyListEnumerator(v_stack_mD0, v_stack_mF8, (unsigned int)(*(unsigned int *)(result)), a4);
    if (sign_flag) goto loc_00310DFF;
    a1 = (*(unsigned __int64 *)(v_stack_p10 + 8)) & (*(unsigned __int64 *)(a1 + 14312) + v_rsi + v_rsi * 4 * 8);
    if (condition_is_not_equal) goto loc_00310E72;
loc_00310DFF:
    if (((*(unsigned int *)(v_rip + 13327663)) & (0x200000ULL)) == 0) goto loc_00310E68;
    if (v_stack_mE8 != 0) goto loc_00310E42;
    if (v_stack_mE8 == v_stack_mE8) goto loc_0030F71D;
    result = KxWaitForLockChainValid(v_stack_mE8, v_stack_mF8, (unsigned int)(*(unsigned int *)(result)), a4);
loc_00310E42:
    v_stack_mE8 = 0;
    result = (unsigned __int8)((v_stack_mE0) ^ ((unsigned __int8)(v_stack_mE0)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0030F71D;
    result = KeWakeAddressAll(result + 8, v_stack_mE0, (unsigned int)(*(unsigned int *)(result)), a4);
    goto loc_0030F71D;
loc_00310E68:
    goto loc_0030F71D;
loc_00310E72:
    result = ~(*(unsigned __int64 *)(a1 + 14312));
    result = (result) & (result + 8);
    v_stack_m110 = result;
    if (condition_is_equal) goto loc_00310DFF;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_p10 + 136))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_mF8 + 576)))) goto loc_003110F2;
loc_00310EA5:
    result = KiComputeThreadQos(v_stack_mF8, v_stack_mE0, (unsigned int)(*(unsigned int *)(result)), a4);
    a3 = (unsigned int)(*(unsigned int *)(v_stack_mF8 + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mF8 + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mF8 + 84))))) { a3 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mF8 + 84))); }
    a2 = (((unsigned int)(a3)) >= (*(unsigned int *)(v_rip + 13321392))) ? 1 : 0;
    a3 = (unsigned int)((a2 + result * 2) * ((unsigned int)(*(unsigned __int8 *)(v_stack_p10 + 185))));
    a3 = (unsigned int)((a3) + ((unsigned int)(*(unsigned __int8 *)(v_stack_mF8 + 517))));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 192) + a3 + a3 * 2 * 8 + 16)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF8 + 576) + *(unsigned __int16 *)(v_stack_p10 + 136) * 8 + 8));
    v_rbx = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF8 + 576) + *(unsigned __int16 *)(v_stack_p10 + 136) * 8 + 8);
    if (condition_is_not_equal) { v_rbx = a1; }
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_mF8 + 120))) >> (1);
    a1 = (unsigned int)((a1) & (1));
    result = (*(unsigned __int64 *)(v_stack_p10 + a1 * 8 + 16)) & (v_rbx);
    v_rdi = (v_stack_m110) & (result);
    v_stack_m110 = v_rdi;
    if (*(unsigned __int64 *)(v_stack_mF8 + 104) != 0) goto loc_00311017;
loc_00310F34:
    result = KiCheckThreadAffinity(v_stack_mF8, *(unsigned __int64 *)(v_stack_p10 + 192) + a3 + a3 * 2 * 8, *(unsigned __int64 *)(v_stack_mF8 + 104), a4);
    if (v_rdi != 0) goto loc_00310F5F;
    if ((unsigned int)(result) == 0) goto loc_003110C3;
loc_00310F49:
    v_r14 = (unsigned int)((a6) + 1);
    v_stack_p28 = (unsigned int)(v_r14);
    goto loc_00310DD7;
loc_00310F5F:
    if ((unsigned int)(result) == 0) goto loc_003110FA;
    v_stack_m170 = v_stack_p18 + 120;
loc_00310F77:
    if (v_rdi != 0) goto loc_00310AEF;
    if (v_rdi == 0) goto loc_003110AA;
    v_r15 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_p10 + 136)) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int64 *)(v_stack_p10 + 192) + a3 + a3 * 2 * 8)));
    v_stack_m60 = (unsigned int)(*(unsigned __int64 *)(v_stack_p10 + 192) + a3 + a3 * 2 * 8);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p18 + 120)))) & (2)) != 0) goto loc_003111AB;
    v_r13 = (v_stack_m198) | (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3215292 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12657170) + a1 * 4)) * 8 + 16550976) + 200));
loc_00310FD6:
    v_stack_m198 = v_r13;
    result = KiRemoveCurrentThreadSharedReadyQueueEnumerator(v_stack_mD8, v_stack_p18, v_stack_p18 + 120, a4);
    result = KiInsertDeferredReadyList(v_stack_m178, v_stack_p18, v_stack_p18 + 120, a4);
    goto loc_00310DD7;
loc_00311000:
    v_stack_mC8 = 0;
    goto loc_00310DB5;
loc_00311009:
    result = KxWaitForLockOwnerShip(v_stack_mE8, v_stack_p18, v_stack_p18 + 120, a4);
    goto loc_00310D84;
loc_00311017:
    result = KiIsThreadConstrainedBySchedulingGroup(v_stack_p18, v_stack_p18, v_stack_p18 + 120, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00310F34;
    result = KiShouldPreemptionBeDeferred(v_stack_p18, v_stack_p18, v_stack_p18 + 120, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00310F34;
    result = KiReduceToUnderMaxQuotaSet(*(unsigned __int16 *)(v_stack_p10 + 136), v_rdi, v_stack_p18 + 120, a4);
    v_stack_m110 = result;
    if ((*(unsigned int *)(v_rip + 13327566)) == 0) goto loc_00310F34;
    result = KiIsThreadRankBiased(v_stack_p18, a1, v_stack_p18 + 120, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00310F34;
    result = KiFindRankBiasedIdleSmtSet(v_stack_p10, v_stack_m110, v_stack_p18 + 120, a4);
    goto loc_00310F34;
loc_0031107F:
    a3 = 0;
    result = EtwTraceScheduleThread(*(unsigned __int64 *)(v_stack_p18 + 40), v_stack_m110, a3, a4);
    goto loc_00310A9A;
loc_00311093:
    result = ~(*(unsigned __int64 *)(v_r13 + 200));
    v_rsi = (v_stack_p10) & (result);
    goto loc_00310F77;
loc_003110AA:
    v_r14 = (unsigned int)((v_r14) + 1);
    v_stack_p28 = (unsigned int)(v_r14);
    v_r15 = 0;
    goto loc_00310DD7;
loc_003110C3:
    v_stack_mC8 = *(unsigned __int64 *)(v_stack_mC8 + 8);
    result = KiRemoveThreadFromSharedReadyQueue(v_stack_mD8, v_stack_p18, v_stack_mCC, a4);
    result = KiInsertDeferredReadyList(v_stack_m178, v_stack_p18, v_stack_mCC, a4);
    goto loc_00310F49;
loc_003110F2:
    goto loc_00310EA5;
loc_003110FA:
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 136)) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)(v_stack_p18)));
    v_stack_m64 = (unsigned int)(v_stack_p18);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(0 + 120)))) & (2)) != 0) goto loc_003111A2;
    v_r13 = (v_r13) | (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3215646 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12656816) + a1 * 4)) * 8 + 16550976) + 200));
loc_00311138:
    v_stack_m198 = v_r13;
    v_stack_mC8 = *(unsigned __int64 *)(v_stack_mC8 + 8);
    result = KiRemoveThreadFromSharedReadyQueue(v_stack_mD8, 0, v_stack_mCC, a4);
    result = KiInsertDeferredReadyList(v_stack_m178, 0, v_stack_mCC, a4);
    v_stack_mF8 = 0;
    goto loc_00310DD7;
loc_00311177:
loc_0031117B:
    result = ~(*(unsigned __int64 *)(v_r13 + 200));
    v_rdi = (v_stack_m110) & (result);
    v_rsi = (v_rsi) & (result);
    v_stack_m110 = v_rdi;
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_mF0, 0, v_stack_mCC, a4);
    goto loc_00310F77;
loc_003111A2:
    v_r13 = (v_r13) | (*(unsigned __int64 *)(v_stack_mF0 + 36448));
    goto loc_00311138;
loc_003111AB:
    v_r13 = (v_r13) | (*(unsigned __int64 *)(v_stack_mF0 + 36448));
    goto loc_00310FD6;
loc_003111B7:
    if ((unsigned int)(a4) == 0) goto loc_00310207;
    if (((unsigned int)((unsigned __int8)(v_stack_m170))) >= ((unsigned int)(v_stack_mF0))) goto loc_00310207;
    goto loc_00310309;
loc_003111D9:
    if ((unsigned int)(a4) == 0) goto loc_003105A9;
    if (((unsigned int)((unsigned __int8)(v_stack_m170))) >= ((unsigned int)(v_stack_mF0))) goto loc_003105A9;
    goto loc_0031066F;
loc_003111FB:
    if (((*(unsigned int *)(v_rip + 13326643)) & (0x200000ULL)) != 0) goto loc_00310D6B;
    v_stack_m70 = 0;
    if (condition_is_above_or_equal) goto loc_00310D84;
loc_00311220:
    if ((unsigned int)(a4) == 0) goto loc_00310AB4;
    if (((unsigned int)((unsigned __int8)(v_stack_m170))) >= ((unsigned int)(v_stack_mF0))) goto loc_00310AB4;
    goto loc_00310D06;
loc_00311242:
    goto loc_00310A50;
loc_00311252:
    result = KiIsThreadRankBiased(v_rdi, a1, v_stack_m170, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0031077C;
    result = KiFindRankBiasedIdleSmtSet(v_stack_p10, v_stack_m118, v_stack_m170, a4);
    goto loc_0031077C;
loc_0031127E:
loc_00311282:
    result = ~(*(unsigned __int64 *)(v_r13 + 200));
    v_rsi = (v_stack_m118) & (result);
    v_r14 = (v_r14) & (result);
    v_stack_m118 = v_rsi;
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_m100, v_stack_m118, v_stack_m170, a4);
    goto loc_0030FE41;
loc_003112AB:
    v_rsp = (v_rsp) + (400);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiSearchForNewThreadsOnTarget(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, void *Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint8_t v_stack_m12C;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint8_t v_stack_m154;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint32_t v_stack_m18C;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint8_t v_stack_mCC;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (400);
    if (Arg5 == 0) goto loc_0030F6E3;
    if (Arg1 == Arg5) goto loc_003112AB;
    Arg3 = 0;
    Arg2 = 0;
    result = KiMayStealStandbyThread(Arg5, Arg2, Arg3, Arg4);
    local_r15 = 0;
    if ((uint8_t)(result) == 0) goto loc_0030F580;
    local_rbx = (*(uint64_t *)(arg2 + 0x8)) & (Arg4);
loc_0030F577:
    if (local_rbx != 0) goto loc_0030F9DD;
loc_0030F580:
    v_stack_m170 = 0;
    result = 0;
    v_stack_m180 = 0;
    v_stack_m128 = v_xmm0;
    v_stack_m120 = 0;
    v_stack_m148 = 0;
    v_stack_m138 = v_xmm0;
    v_stack_m130 = v_xmm1;
    v_stack_m12C = 32;
    v_stack_m158 = v_xmm0;
    v_stack_m154 = 32;
    v_stack_m168 = v_xmm0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg5 + 0x83D8))) == 0) goto loc_0030F8E7;
loc_0030F5C7:
    local_rbx = (Arg5) & (-2);
    v_stack_m170 = local_rbx;
loc_0030F5E0:
    if (condition_is_above_or_equal) goto loc_0030F814;
loc_0030F5ED:
    local_rsi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xCB5CB7)) & ((uint32_t)(local_rsi))) == 0) goto loc_0030F8C0;
loc_0030F5FB:
loc_0030F5FD:
    if (*(uint64_t *)(Arg5 + 0x30) == 0) goto loc_0030F5E0;
    goto loc_0030F5ED;
loc_0030F608:
    local_rdi = (Arg5) + (-216);
    Arg1 = (*(uint64_t *)(v_stack_p10 + 0x8)) & (local_rsi);
    if (condition_is_not_equal) goto loc_0030FC5A;
loc_0030F623:
    local_r15 = 0;
    if (v_stack_m170 == 0) goto loc_0030F682;
    Arg1 = (v_stack_m170) & (-2);
    v_stack_m48 = Arg1;
    local_rbx = (uint32_t)((v_stack_m170) & (1));
    if (condition_is_equal) goto loc_0030F944;
    result = *(uint64_t *)(Arg5 + 0x30);
    if (((uint32_t)(local_rbx)) == 1) {
        result = *(uint64_t *)(arg1 + 0x8E58);
        Arg3 = *(uint64_t *)(arg1 + 0x8E58);
        Arg3 = (Arg3) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0030F682;
loc_0030F670:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0030F670;
loc_0030F682:
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x35D9)) == 0) goto loc_0030F6D1;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x35D9))) == 1) goto loc_0030F8FC;
    result = KiSendSoftwareInterruptAffinity(Arg1 + 13792, *(uint8_t *)(arg1 + 0x35D8), Arg3, Arg4);
loc_0030F6AD:
    if ((*(uint8_t *)(arg1 + 0x35D9)) == 2) goto loc_0030FD5D;
loc_0030F6BC:
    *(uint8_t *)(arg1 + 0x35D9) = 0;
    *(uint32_t *)(arg1 + 0x35DC) = 0xFFFFULL;
loc_0030F6D1:
    if (v_stack_m180 != 0) goto loc_00310860;
    goto loc_003112AB;
loc_0030F6E3:
    result = 0;
    v_stack_mC8 = v_xmm1;
    v_stack_mC0 = 0;
    local_r15 = 0;
    v_stack_m178 = 0;
    v_stack_mD8 = v_xmm1;
    v_stack_mD0 = v_xmm0;
    v_stack_mCC = 32;
    v_stack_mE8 = v_xmm0;
    if ((((uint32_t)(0xFFFFFFFEULL)) & ((uint32_t)(*(uint32_t *)(arg6 + 0x8)))) != 0) goto loc_003111FB;
loc_0030F71D:
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x35D8 + 0x1)) == 0) goto loc_0030F767;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x35D8 + 0x1))) == 1) goto loc_0030F957;
    result = KiSendSoftwareInterruptAffinity(Arg1 + 13784 + 8, *(uint8_t *)(arg1 + 0x35D8), Arg3, Arg4);
loc_0030F74A:
    if ((*(uint8_t *)(arg1 + 0x35D8 + 0x1)) == 2) goto loc_0030FEBD;
loc_0030F754:
    *(uint8_t *)(arg1 + 0x35D8 + 0x1) = 0;
    *(uint32_t *)(arg1 + 0x35D8 + 0x4) = 0xFFFFULL;
loc_0030F767:
    if (v_stack_m178 == 0) goto loc_003112AB;
    v_stack_m178 = *(uint64_t *)(v_stack_m178);
loc_0030F77D:
    Arg4 = 0;
    result = KiDeferredReadySingleThread(Arg1, v_stack_m178 - 216, v_stack_m178, Arg4);
    local_r15 = (uint32_t)((local_r15) + 1);
    if (v_stack_m178 != 0) {
        result = *(uint64_t *)(v_stack_m178);
        v_stack_m178 = result;
    }
    if ((((uint8_t)(local_r15)) & (15)) == 0) {
        Arg1 = Arg1 + 13784;
        result = KiFlushSoftwareInterruptBatch(Arg1, v_stack_m178 - 216, v_stack_m178, Arg4);
    }
    if (v_stack_m178 != 0) goto loc_0030F77D;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x35D9)) == 0) goto loc_003112AB;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x35D9))) == 1) goto loc_0030F994;
    result = KiSendSoftwareInterruptAffinity(Arg1 + 13792, *(uint8_t *)(arg1 + 0x35D8), v_stack_m178, Arg4);
loc_0030F7EB:
    if ((*(uint8_t *)(arg1 + 0x35D9)) == 2) goto loc_0030FEEC;
loc_0030F7FA:
    *(uint8_t *)(arg1 + 0x35D9) = 0;
    *(uint32_t *)(arg1 + 0x35DC) = 0xFFFFULL;
    goto loc_003112AB;
loc_0030F814:
    v_stack_m120 = 31 + 33856;
    v_stack_m138 = 31;
    v_stack_m130 = (uint32_t)((uint32_t)(*(uint32_t *)(31 + 0x83D8)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(31 + 0x83D8))) == 0) goto loc_0030FEDB;
    local_rsi = ((uint32_t)((uint32_t)(31 + 16))) << (4);
    local_rsi = (local_rsi) + (31 + 33856);
    v_stack_m9C = (uint32_t)(31 + 16);
    v_stack_m128 = local_rsi;
    v_stack_m12C = (uint8_t)(31 + 16);
loc_0030F84E:
    v_stack_m108 = local_r15;
    v_stack_m198 = local_r15;
loc_0030F85D:
    v_stack_m18C = (uint32_t)((uint32_t)((uint32_t)(local_r15)));
loc_0030F861:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r15)))) >= 64) goto loc_0030FA6E;
    v_stack_m140 = local_r15;
    if (local_rsi == 0) goto loc_0030FA6E;
loc_0030F877:
    result = ((uint8_t)(31 + 16)) << (4);
    result = (result) + (31 + 33856);
    v_stack_m128 = *(uint64_t *)(local_rsi);
    if ((*(uint64_t *)(local_rsi)) != result) goto loc_0030FA77;
    v_stack_m130 = (uint32_t)((uint32_t)(v_stack_m130));
    if ((uint32_t)((uint32_t)(v_stack_m130)) == 0) goto loc_0030FA66;
    local_rsi = ((uint8_t)((uint8_t)(31 + 16))) << (4);
    local_rsi = (local_rsi) + (31 + 33856);
    v_stack_m98 = (uint32_t)((uint8_t)(31 + 16));
    v_stack_m12C = (uint8_t)((uint8_t)(31 + 16));
    goto loc_0030F877;
loc_0030F8C0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCB71F2)))) & (64)) == 0) goto loc_0030F5FB;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)(v_stack_m130), 31 + 33856, local_r15, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0030F5FB;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), 31 + 33856, local_r15, Arg4);
    goto loc_0030F5FD;
loc_0030F8E7:
    if (*(uint64_t *)(31 + 0x8430) == 0) goto loc_0030F682;
    goto loc_0030F5C7;
loc_0030F8FC:
    v_stack_mB0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x35DC)));
    v_stack_mB8 = 6;
    v_stack_mAC = local_r15;
    local_rdi = 31;
    if (((uint8_t)(31 + 33856)) != 1) { local_rdi = 47; }
    result = HalpInterruptSendIpi(v_stack_mB8, (uint32_t)((uint32_t)(local_rdi)), local_r15, Arg4);
    goto loc_0030F6AD;
loc_0030F944:
    goto loc_0030F670;
loc_0030F957:
    v_stack_mB0 = (uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x4)));
    v_stack_mB8 = 6;
    v_stack_mAC = local_r15;
    Arg2 = (uint32_t)((uint32_t)(local_rdi));
    if (((uint8_t)(*(uint8_t *)(1))) != 1) { Arg2 = 47; }
    result = HalpInterruptSendIpi(v_stack_mB8, Arg2, *(uint8_t *)(1), Arg4);
    goto loc_0030F74A;
loc_0030F994:
    v_stack_mB0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x35DC)));
    result = 0;
    v_stack_mB8 = 6;
    v_stack_mAC = 0;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x35D8))) != 1) { local_rdi = 47; }
    result = HalpInterruptSendIpi(v_stack_mB8, (uint32_t)((uint32_t)(local_rdi)), *(uint8_t *)(arg1 + 0x35D8), Arg4);
    goto loc_0030F7EB;
loc_0030F9DD:
    v_stack_mA0 = 1;
    Arg2 = (uint32_t)((*(uint8_t *)(arg1 + 0xD1) + 1 * 1) & (63));
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(local_rsi) + 0x88)) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg2)));
    if (local_rdi == (*(uint64_t *)(*(uint8_t *)(arg1 + 0x35D8) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC137A5) + arg1 * 4)) * 8 + 0xFC8C40))) goto loc_0030F577;
    Arg3 = 0;
    result = KiMayStealStandbyThread(local_rdi, *(uint64_t *)(*(uint8_t *)(arg1 + 0x35D8) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC137A5) + arg1 * 4)) * 8 + 0xFC8C40), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0030F577;
    result = KiAttemptToStealStandbyThread(Arg1, local_rdi, *(uint64_t *)(*(uint8_t *)(arg1 + 0x35D8) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC137A5) + arg1 * 4)) * 8 + 0xFC8C40), Arg4);
    if ((uint8_t)(result) != 0) goto loc_0030F580;
    goto loc_0030F577;
loc_0030FA66:
    v_stack_m12C = 0;
    v_stack_m128 = local_r15;
loc_0030FA6E:
    goto loc_0030FA9C;
loc_0030FA77:
    Arg1 = (*(uint64_t *)(v_stack_p10 + 0x8)) & (v_stack_p18);
    if (condition_is_not_equal) goto loc_0030FB5D;
loc_0030FA99:
    local_r15 = 0;
loc_0030FA9C:
    v_stack_m168 = local_rdi;
    v_stack_m160 = 0;
    if ((((uint8_t)(*(uint64_t *)(local_rdi + 0x8430 + 0x8))) & (1)) != 0) goto loc_0030FF12;
loc_0030FABD:
    if (*(uint64_t *)(local_rdi + 0x8430 + 0x8) != 0) goto loc_0030FF28;
loc_0030FAC6:
loc_0030FACF:
loc_0030FAD5:
    v_stack_m100 = 0;
    v_stack_p28 = 0;
    v_stack_m198 = 0;
    local_r14 = 0;
loc_0030FAF0:
    if (0 >= 64) goto loc_0030F623;
loc_0030FAFA:
    if (v_stack_m160 == 0) goto loc_0030F623;
    if (v_stack_m150 == 0) goto loc_00310798;
loc_0030FB0F:
    result = ((uint8_t)(v_stack_m154)) << (4);
    result = (result) + (v_stack_m148);
    v_stack_m150 = *(uint64_t *)(v_stack_m150);
    if ((*(uint64_t *)(v_stack_m150)) != result) goto loc_0030F608;
    v_stack_m158 = (uint32_t)((uint32_t)(v_stack_m158));
    if ((uint32_t)((uint32_t)(v_stack_m158)) == 0) goto loc_00310788;
    Arg4 = ((uint8_t)((uint8_t)(v_stack_m154))) << (4);
    Arg4 = (Arg4) + (v_stack_m148);
    v_stack_m84 = (uint32_t)((uint8_t)(v_stack_m154));
    v_stack_m154 = (uint8_t)((uint8_t)(v_stack_m154));
    goto loc_0030FB0F;
loc_0030FB5D:
    result = ~(v_rip - 3209817);
    result = (result) & ((uint32_t)(v_stack_m158));
    v_stack_m140 = result;
    if (condition_is_equal) goto loc_0030FA99;
    if (((uint16_t)(*(uint16_t *)(local_r14 + 0x88))) >= (*(uint16_t *)(*(uint64_t *)(local_r15 + 0x240)))) goto loc_00310952;
loc_0030FB8D:
    result = KiComputeThreadQos(0, local_rdi, v_rip - 3209817, Arg4);
    Arg3 = (uint32_t)(*(uint32_t *)(local_r15 + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x54))))) { Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x54))); }
    Arg2 = 0;
    Arg2 = (((uint32_t)(Arg3)) >= (*(uint32_t *)(v_rip + 0xCB57C7))) ? 1 : 0;
    Arg3 = (uint32_t)((Arg2 + result * 2) * ((uint32_t)(*(uint8_t *)(local_r14 + 0xB9))));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(*(uint8_t *)(local_r15 + 0x205))));
    result = (*(uint64_t *)(*(uint64_t *)(local_r15 + 0x240) + *(uint16_t *)(local_r14 + 0x88) * 8 + 0x8)) & (*(uint64_t *)(*(uint64_t *)(local_r14 + 0xC0) + Arg3 + Arg3 * 2 * 8 + 0x10));
    local_rsi = *(uint64_t *)(*(uint64_t *)(local_r15 + 0x240) + *(uint16_t *)(local_r14 + 0x88) * 8 + 0x8);
    if (condition_is_not_equal) { local_rsi = result; }
    result = ((uint32_t)(*(uint32_t *)(local_r15 + 0x78))) >> (1);
    result = (uint32_t)((result) & (1));
    Arg1 = (*(uint64_t *)(local_r14 + result * 8 + 0x10)) & (local_rsi);
    local_rsi = (v_stack_m140) & (Arg1);
    v_stack_m140 = local_rsi;
    if (*(uint64_t *)(local_r15 + 0x68) != 0) goto loc_003106D2;
loc_0030FC1A:
    if (local_rsi != 0) goto loc_0030FD83;
    if ((*(uint64_t *)(local_r15 + 0x238)) != (*(uint64_t *)(v_rip + 0xCB6FCE))) goto loc_00310872;
loc_0030FC3C:
loc_0030FC40:
    result = (uint32_t)(((uint32_t)(v_stack_m18C)) + 1);
    local_r15 = 0;
    goto loc_0030F85D;
loc_0030FC5A:
    result = ~(0);
    result = (result) & (Arg1);
    v_stack_m118 = result;
    if (condition_is_equal) goto loc_0030F623;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m150) + 0x8440 + 0x88))) >= (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m150) + 0x240)))) goto loc_00310959;
loc_0030FC89:
    result = KiComputeThreadQos(*(uint64_t *)(v_stack_m150), *(uint64_t *)(v_stack_m150) + 33856, v_stack_m198, Arg4);
    Arg3 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m150) + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m150) + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m150) + 0x54))))) { Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m150) + 0x54))); }
    Arg2 = (((uint32_t)(Arg3)) >= (*(uint32_t *)(v_rip + 0xCB56C5))) ? 1 : 0;
    Arg3 = (uint32_t)((Arg2 + result * 2) * ((uint32_t)(*(uint8_t *)(v_stack_p10 + 0xB9))));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m150) + 0x205))));
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m150) + 0x240) + *(uint16_t *)(*(uint64_t *)(v_stack_m150) + 0x8440 + 0x88) * 8 + 0x8)) & (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0xC0) + Arg3 + Arg3 * 2 * 8 + 0x10));
    local_rsi = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m150) + 0x240) + *(uint16_t *)(*(uint64_t *)(v_stack_m150) + 0x8440 + 0x88) * 8 + 0x8);
    if (condition_is_not_equal) { local_rsi = result; }
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m150) + 0x78))) >> (1);
    result = (uint32_t)((result) & (1));
    Arg1 = (*(uint64_t *)(v_stack_p10 + result * 8 + 0x10)) & (local_rsi);
    local_rsi = (v_stack_m118) & (Arg1);
    v_stack_m118 = local_rsi;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m150) + 0x68) != 0) goto loc_0031073B;
loc_0030FD1B:
    if (local_rsi != 0) goto loc_0030FE2E;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m150) + 0x238)) != (*(uint64_t *)(v_rip + 0xCB6ECD))) goto loc_003108A7;
loc_0030FD38:
    local_r13 = (uint32_t)((0) + 1);
loc_0030FD3B:
    v_stack_p28 = (uint32_t)(local_r13);
loc_0030FD42:
    goto loc_0030FAF0;
loc_0030FD5D:
    *(uint64_t *)(arg1 + 0x35E0) = 0x200001ULL;
    Arg2 = 0;
    result = memset(Arg1 + 13800, Arg2, 256, v_stack_m150);
    goto loc_0030F6BC;
loc_0030FD83:
    result = KiCheckThreadAffinity(0, Arg2, 256, v_stack_m150);
    if ((uint32_t)(result) == 0) goto loc_00310961;
loc_0030FD96:
    if (v_stack_p18 != 0) goto loc_0030FF6D;
    if (v_stack_p18 == 0) goto loc_003108D1;
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p10 + 0x88)) << (6));
    Arg1 = (uint32_t)((Arg1) + (0));
    v_stack_m8C = (uint32_t)(v_stack_p18);
    v_stack_m8C = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x78)))) & (2)) == 0) goto loc_00310A14;
    result = (v_stack_m198) | (*(uint64_t *)(*(uint64_t *)(v_rip - 0x30FDD7 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC133F7) + arg1 * 4)) * 8 + 0xFC8C40) + 0x8E60));
loc_0030FDF7:
loc_0030FDFE:
    v_stack_m198 = result;
    v_stack_m128 = *(uint64_t *)(local_r13 + 0x8);
    result = KiRemoveThreadFromReadyQueue(v_stack_m138, local_r15 + 216, (uint32_t)((uint32_t)(v_stack_m12C)), v_stack_m150);
    result = KiInsertDeferredReadyList(v_stack_m180, 0, (uint32_t)((uint32_t)(v_stack_m12C)), v_stack_m150);
    goto loc_0031023A;
loc_0030FE2E:
    result = KiCheckThreadAffinity(*(uint64_t *)(v_stack_m150), 0, (uint32_t)((uint32_t)(v_stack_m12C)), v_stack_m150);
    if ((uint32_t)(result) == 0) goto loc_003109B5;
loc_0030FE41:
    if (*(uint64_t *)(local_r13 + 0x8) != 0) goto loc_00310369;
    if (*(uint64_t *)(local_r13 + 0x8) == 0) goto loc_003108F8;
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_m150 + 0x88)) << (6));
    Arg1 = (uint32_t)((Arg1) + (0));
    v_stack_m74 = 0;
    if (((2) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m150) + 0x78))))) == 0) goto loc_00310A20;
    local_r15 = (local_r15) | (*(uint64_t *)(*(uint64_t *)(v_rip - 0x30FE78 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC13356) + arg1 * 4)) * 8 + 0xFC8C40) + 0x8E60));
loc_0030FE92:
    v_stack_m198 = local_r15;
    result = KiRemoveCurrentThreadScbReadyQueueEnumerator(v_stack_m168, *(uint64_t *)(v_stack_m150), (uint32_t)((uint32_t)(v_stack_m12C)), v_stack_m150);
    result = KiInsertDeferredReadyList(v_stack_m180, *(uint64_t *)(v_stack_m150), (uint32_t)((uint32_t)(v_stack_m12C)), v_stack_m150);
    goto loc_0030FD42;
loc_0030FEBD:
    *(uint64_t *)(2 + 0x8) = 0x200001ULL;
    Arg2 = 0;
    result = memset(2 + 16, Arg2, 256, v_stack_m150);
    goto loc_0030F754;
loc_0030FEDB:
    v_stack_m128 = local_r15;
    goto loc_0030F84E;
loc_0030FEEC:
    *(uint64_t *)(arg1 + 0x35E0) = 0x200001ULL;
    Arg2 = 0;
    result = memset(Arg1 + 13800, Arg2, 256, v_stack_m150);
    goto loc_0030F7FA;
loc_0030FF12:
    if ((Arg1 + 13800) == 1) goto loc_0030FAC6;
    result = (result) | (1);
    result = (result) ^ (Arg1 + 13800);
    goto loc_0030FABD;
loc_0030FF28:
    result = (result) + (-88);
    v_stack_m160 = result;
    v_stack_m158 = (uint32_t)(*(uint16_t *)(result + 0x20));
    v_stack_m148 = result + 144;
    if ((uint32_t)(*(uint16_t *)(result + 0x20)) == 0) goto loc_00310945;
    Arg4 = ((uint32_t)((uint32_t)(v_stack_m154))) << (4);
    Arg4 = (Arg4) + (result + 144);
    v_stack_m88 = (uint32_t)(v_stack_m154);
    v_stack_m150 = Arg4;
    v_stack_m154 = (uint8_t)(v_stack_m154);
    goto loc_0030FAD5;
loc_0030FF6D:
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p10 + 0x88)) << (6));
    Arg1 = (uint32_t)((Arg1) + (0));
    v_stack_m90 = 0;
    v_stack_m90 = 0;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x78))) >> (1));
    Arg2 = (uint32_t)((Arg2) & (1));
    v_stack_m188 = *(uint64_t *)(v_rip - 0x30FFAC + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC1322E) + arg1 * 4)) * 8 + 0xFC8C40);
    result = KiTryAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(v_rip - 0x30FFAC + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC1322E) + arg1 * 4)) * 8 + 0xFC8C40), Arg2, v_stack_m108, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00310830;
    result = KiIsIsolationUnitIdleByHandle(v_stack_m108, Arg2, v_stack_m108, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00310A44;
    if (*(uint64_t *)(local_r15 + 0x68) == 0) goto loc_00310017;
    Arg3 = ((uint32_t)(*(uint32_t *)(v_stack_m188 + 0xD8))) + (*(uint64_t *)(local_r15 + 0x68));
    result = KiIsThreadConstrainedBySchedulingGroup(local_r15, v_stack_m188, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00310017;
    result = KiShouldPreemptionBeDeferred(local_r15, v_stack_m188, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00310017;
    result = KiCheckForMaxOverQuotaScb(Arg3, v_stack_m188, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00311242;
loc_00310017:
    v_stack_m128 = *(uint64_t *)((uint32_t)(Arg5) + 0x8);
    result = KiRemoveThreadFromReadyQueue(v_stack_m138, (uint32_t)(Arg5), (uint32_t)((uint32_t)(v_stack_m12C)), Arg4);
    Arg2 = 0;
    result = memset(*(uint64_t *)(arg1 + 0x37E8), Arg2, 240, Arg4);
    Arg3 = 0;
    result = KiStartRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), v_stack_m108, Arg3, Arg4);
    Arg4 = 0;
    v_stack_m1A8 = v_stack_m180;
    result = KiScheduleThreadToRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), local_r15, v_stack_m188, Arg4);
    local_r10 = 0;
    result = 0;
    if (((*(uint32_t *)(v_rip + 0xCB6A8B)) & (0x400ULL)) != 0) { result = 2; }
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_003100E4;
loc_003100A1:
    Arg1 = (0 * 4 + 2) + (0);
    Arg1 = (Arg1 * 8) + (*(uint64_t *)(arg1 + 0x37E8));
    result = KiCommitRescheduleContextEntry(Arg1, Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m180);
    local_rbx = (uint8_t)((0) | ((uint8_t)(result)));
    local_r15 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r15)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_003100A1;
loc_003100E4:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x8)) != 1) goto loc_00310107;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1)) + 1);
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1) = (uint8_t)(result);
    if (((uint8_t)(result)) >= (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58)))) {
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1) = 0;
    }
    local_r15 = 0;
    Arg4 = (v_stack_m108) & (-2);
    v_stack_m58 = Arg4;
    result = (uint32_t)((v_stack_m108) & (1));
    if (condition_is_equal) goto loc_00310814;
    if (((uint32_t)(result)) == 1) {
        result = *(uint64_t *)(Arg4 + 0x8E58);
        Arg3 = *(uint64_t *)(Arg4 + 0x8E58);
        Arg3 = (Arg3) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0031016B;
loc_00310150:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_00310150;
loc_0031016B:
    v_stack_m108 = 0;
    if ((uint8_t)((uint8_t)(local_rbx)) == 0) goto loc_00310930;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_00310930;
loc_00310190:
    local_rsi = (0 + 0 * 4 * 8) + (*(uint64_t *)(arg1 + 0x37E8));
    if ((((uint8_t)(*(uint8_t *)(local_rsi + 0x33))) & (16)) != 0) goto loc_00310252;
    if ((((uint8_t)(*(uint8_t *)(local_rsi + 0x33))) & (8)) == 0) goto loc_003101E4;
    if ((*(uint8_t *)(*(uint64_t *)(local_rsi + 0x10) + 0x7)) == 0) goto loc_003101E4;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x35D9)) != 0) goto loc_0031027B;
loc_003101CF:
    *(uint8_t *)(arg1 + 0x35D9) = 1;
    *(uint32_t *)(arg1 + 0x35DC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsi + 0x10) + 0x24)));
loc_003101E4:
    if (((*(uint8_t *)(local_rsi + 0x33)) & (2)) != 0) goto loc_003107EC;
loc_003101ED:
    if (((*(uint8_t *)(local_rsi + 0x33)) & (4)) == 0) goto loc_00310207;
    if (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x10) + 0x8EB8) != 0) goto loc_003102C7;
loc_00310207:
    result = *(uint64_t *)(*(uint64_t *)(local_rsi + 0x10) + 0x8EB8);
    if (((*(uint8_t *)(local_rsi + 0x33)) & (1)) != 0) {
        result = *(uint64_t *)(local_rsi + 0x28);
    }
    local_r15 = (uint32_t)((local_r15) + 1);
    if (((uint32_t)(local_r15)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_00310190;
loc_0031023A:
    local_r15 = 0;
    goto loc_0030F861;
loc_00310252:
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x35D9)) == 0) goto loc_003101CF;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x35D9))) != 1) goto loc_003102A6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x35DC)))) == (*(uint32_t *)(v_stack_m12C + 0x24))) goto loc_003101E4;
    goto loc_00310291;
loc_0031027B:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x35D9))) != 1) goto loc_003102A6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x35DC)))) == (*(uint32_t *)(v_stack_m12C + 0x24))) goto loc_003101E4;
loc_00310291:
    *(uint8_t *)(arg1 + 0x35D9) = 2;
    result = KeAddProcessorAffinityEx(Arg1 + 13792, (uint32_t)(*(uint32_t *)(arg1 + 0x35DC)), v_stack_m198, Arg4);
loc_003102A6:
    result = KeAddGroupAffinityEx(Arg1 + 13792, *(uint8_t *)(v_stack_m12C + 0xD0), *(uint64_t *)(v_stack_m12C + 0xC8), Arg4);
    goto loc_003101E4;
loc_003102C7:
    if ((*(uint64_t *)(arg1 + 0x8EB8)) == 0) goto loc_00310207;
    if (Arg1 == v_stack_m12C) goto loc_00310207;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result))))) & (0x40000ULL));
    result = Arg1 + 36536;
    if (!(condition_is_equal)) {
        result = Arg1 + 36536;
    }
    if (condition_is_above_or_equal) goto loc_003111B7;
loc_00310309:
    *(uint32_t *)(*(uint64_t *)(result) + 0xC) = 2;
    v_stack_m188 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m12C + 0x24)));
    if ((*(uint8_t *)(v_rip + 0xCB4CF7)) == 0) {
        result = *(uint8_t *)(Arg5 + (uint32_t)(*(uint32_t *)(v_stack_m12C + 0x24)) * 2 + 0xFCD261);
        Arg1 = *(uint8_t *)(Arg5 + (uint32_t)(*(uint32_t *)(v_stack_m12C + 0x24)) * 2 + 0xFCD260);
        Arg1 = (uint32_t)((Arg1) << (6));
        Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
        v_stack_m188 = (uint32_t)(Arg1);
    }
    *(uint32_t *)(*(uint64_t *)(result) + 0x8) = (uint32_t)(Arg1);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xCB67D2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCB67D2)))) & (32)) != 0) {
        Arg1 = *(uint32_t *)(v_stack_m12C + 0x24);
        Arg2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(Arg1, Arg2, (uint32_t)(*(uint32_t *)(result)), Arg4);
        Arg1 = v_stack_m188;
    }
    Arg2 = ((uint32_t)((uint32_t)(Arg1))) >> (32);
    goto loc_00310207;
loc_00310369:
    Arg1 = (uint32_t)((*(uint16_t *)(Arg4 + 0x88)) << (6));
    v_stack_m78 = 0;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg2)));
    v_stack_m78 = (uint32_t)(Arg2);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg5 + 0x78))) >> (1));
    Arg2 = (uint32_t)((Arg2) & (1));
    result = KiTryAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(v_rip - 0x3103A1 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC12E3C) + arg1 * 4)) * 8 + 0xFC8C40), Arg2, v_stack_m100, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00310847;
    result = KiIsIsolationUnitIdleByHandle(v_stack_m100, Arg2, v_stack_m100, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00311282;
    if (*(uint64_t *)(Arg5 + 0x68) == 0) goto loc_00310402;
    Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x3103A1 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC12E3C) + arg1 * 4)) * 8 + 0xFC8C40) + 0xD8))) + (*(uint64_t *)(Arg5 + 0x68));
    result = KiIsThreadConstrainedBySchedulingGroup(Arg5, Arg2, v_stack_m100, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00310402;
    result = KiShouldPreemptionBeDeferred(Arg5, Arg2, v_stack_m100, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00310402;
    result = KiCheckForMaxOverQuotaScb(Arg2, Arg2, v_stack_m100, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0031127E;
loc_00310402:
    result = KiRemoveCurrentThreadScbReadyQueueEnumerator(v_stack_m168, Arg5, v_stack_m100, Arg4);
    Arg2 = 0;
    result = memset(*(uint64_t *)(arg1 + 0x37E8), Arg2, 240, Arg4);
    Arg3 = 0;
    result = KiStartRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), v_stack_m100, Arg3, Arg4);
    Arg4 = 0;
    v_stack_m1A8 = v_stack_m180;
    result = KiScheduleThreadToRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), Arg5, *(uint64_t *)(v_rip - 0x3103A1 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC12E3C) + arg1 * 4)) * 8 + 0xFC8C40), Arg4);
    local_r14 = 0;
    local_rsi = 0;
    if (((*(uint32_t *)(v_rip + 0xCB66B0)) & (0x400ULL)) != 0) { local_rsi = 2; }
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_003104A3;
loc_00310472:
    Arg1 = (0 * 4 + 2) + (0);
    result = KiCommitRescheduleContextEntry(*(uint64_t *)(arg1 + 0x37E8) + Arg1 * 8, Arg1, (uint32_t)((uint32_t)(local_rsi)), v_stack_m180);
    local_r14 = (uint8_t)((local_r14) | ((uint8_t)(result)));
    local_rdi = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rdi)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_00310472;
    local_r10 = 0;
loc_003104A3:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x8)) != 1) goto loc_003104C6;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1)) + 1);
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1) = (uint8_t)(result);
    if (((uint8_t)(result)) >= (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58)))) {
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x10) + 0x8E58) + 0x1) = 0;
    }
    Arg4 = (v_stack_m100) & (-2);
    v_stack_m50 = Arg4;
    result = (uint32_t)((v_stack_m100) & (1));
    if (condition_is_equal) goto loc_00310822;
    if (((uint32_t)(result)) == 1) {
        result = *(uint64_t *)(Arg4 + 0x8E58);
        Arg3 = *(uint64_t *)(Arg4 + 0x8E58);
        Arg3 = (Arg3) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_00310523;
loc_00310510:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_00310510;
loc_00310523:
    v_stack_m100 = 0;
    if ((uint8_t)(local_r14) == 0) goto loc_003105CB;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_003105CB;
loc_00310540:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x33))) & (16)) != 0) goto loc_00310565;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x33))) & (8)) == 0) goto loc_00310586;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x7)) == 0) goto loc_00310586;
loc_00310565:
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x35D9)) != 0) goto loc_003105DF;
    *(uint8_t *)(arg1 + 0x35D9) = 1;
    *(uint32_t *)(arg1 + 0x35DC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24)));
loc_00310586:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x33)) & (2)) != 0) goto loc_00310800;
loc_0031058F:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x33)) & (4)) == 0) goto loc_003105A9;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8EB8) != 0) goto loc_0031062D;
loc_003105A9:
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x8EB8);
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x33)) & (1)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28);
    }
    local_r14 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r14)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))))) goto loc_00310540;
loc_003105CB:
    local_r14 = 0;
    goto loc_0030FD42;
loc_003105DF:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8)))) != 1) goto loc_00310623;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x35DC)))) == (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24))) goto loc_00310586;
    *(uint8_t *)(arg1 + 0x35D9) = 2;
    result = KeAddProcessorAffinityEx(Arg1 + 13792, (uint32_t)(*(uint32_t *)(arg1 + 0x35DC)), Arg3, Arg4);
loc_00310608:
    result = KeAddGroupAffinityEx(Arg1 + 13792, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0xD0), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0xC8), Arg4);
    goto loc_00310586;
loc_00310623:
    goto loc_00310608;
loc_0031062D:
    if ((*(uint64_t *)(arg1 + 0x8EB8)) == 0) goto loc_003105A9;
    if (Arg1 == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10))) goto loc_003105A9;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result))))) & (0x40000ULL));
    result = Arg1 + 36536;
    if (!(condition_is_equal)) {
        result = Arg1 + 36536;
    }
    if (condition_is_above_or_equal) goto loc_003111D9;
loc_0031066F:
    *(uint32_t *)(*(uint64_t *)(result) + 0xC) = 2;
    local_r13 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24));
    if ((*(uint8_t *)(v_rip + 0xCB4991)) == 0) {
        result = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24)));
        Arg2 = v_rip - 3212940;
        local_r13 = *(uint8_t *)(arg2 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24)) * 2 + 0xFCD260);
        local_r13 = (uint32_t)((local_r13) << (6));
        result = *(uint8_t *)(arg2 + result * 2 + 0xFCD261);
        local_r13 = (uint32_t)((local_r13) | ((uint32_t)(result)));
    }
    *(uint32_t *)(*(uint64_t *)(result) + 0x8) = (uint32_t)(local_r13);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xCB6466));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCB6466)))) & (32)) != 0) {
        Arg1 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10) + 0x24);
        Arg2 = 2;
        result = EtwTraceXSchedulerPriorityKickSend(Arg1, Arg2, (uint32_t)(*(uint32_t *)(result)), Arg4);
    }
    Arg2 = ((uint32_t)((uint32_t)(local_r13))) >> (32);
    goto loc_003105A9;
loc_003106D2:
    result = KiIsThreadConstrainedBySchedulingGroup(v_stack_m198, Arg2, (uint32_t)(*(uint32_t *)(result)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0030FC1A;
    result = KiShouldPreemptionBeDeferred(v_stack_m198, Arg2, (uint32_t)(*(uint32_t *)(result)), Arg4);
    if ((uint8_t)(result) != 0) goto loc_0030FC1A;
    result = KiReduceToUnderMaxQuotaSet(*(uint16_t *)(local_r14 + 0x88), *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x10), (uint32_t)(*(uint32_t *)(result)), Arg4);
    v_stack_m140 = result;
    if ((*(uint32_t *)(v_rip + 0xCB6612)) == 0) goto loc_0030FC1A;
    result = KiIsThreadRankBiased(v_stack_m198, Arg1, (uint32_t)(*(uint32_t *)(result)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0030FC1A;
    result = KiFindRankBiasedIdleSmtSet(0, v_stack_m140, (uint32_t)(*(uint32_t *)(result)), Arg4);
    goto loc_0030FC1A;
loc_0031073B:
    result = KiIsThreadConstrainedBySchedulingGroup(*(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8, v_stack_m140, (uint32_t)(*(uint32_t *)(result)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0030FD1B;
    result = KiShouldPreemptionBeDeferred(*(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8, v_stack_m140, (uint32_t)(*(uint32_t *)(result)), Arg4);
    if ((uint8_t)(result) != 0) goto loc_0030FD1B;
    result = KiReduceToUnderMaxQuotaSet(*(uint16_t *)(Arg4 + 0x88), v_stack_m140, (uint32_t)(*(uint32_t *)(result)), Arg4);
    v_stack_m118 = result;
    if ((*(uint32_t *)(v_rip + 0xCB65A9)) != 0) goto loc_00311252;
loc_0031077C:
    goto loc_0030FD1B;
loc_00310788:
    local_r10 = 0;
    v_stack_m150 = 0;
    v_stack_m154 = 0;
loc_00310798:
    result = KiDetermineNextScbForScbReadyQueueEnumerator(v_stack_m160, v_stack_m140, (uint32_t)(*(uint32_t *)(result)), 0);
    if (result == 0) goto loc_003107E2;
    v_stack_m158 = (uint32_t)(*(uint16_t *)(result + 0x78));
    v_stack_m148 = result + 144;
    if ((uint32_t)(*(uint16_t *)(result + 0x78)) == 0) goto loc_0031090A;
    Arg4 = ((uint32_t)((uint32_t)(*(uint16_t *)(result + 0x78)))) << (4);
    Arg4 = (Arg4) + (result + 144);
    v_stack_m80 = (uint32_t)(*(uint16_t *)(result + 0x78));
    v_stack_m150 = Arg4;
    v_stack_m154 = (uint8_t)(*(uint16_t *)(result + 0x78));
loc_003107E2:
    v_stack_m160 = result;
    goto loc_0030FAFA;
loc_003107EC:
    Arg3 = 0;
    result = EtwTraceScheduleThread(*(uint64_t *)(result + 0x28), 0, Arg3, Arg4);
    goto loc_003101ED;
loc_00310800:
    Arg3 = 0;
    result = EtwTraceScheduleThread(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x28), result, Arg3, Arg4);
    goto loc_0031058F;
loc_00310814:
    goto loc_00310150;
loc_00310822:
    goto loc_00310510;
loc_00310830:
    result = ~(*(uint64_t *)(v_stack_m188 + 0xC8));
    local_r14 = (local_r14) & (result);
    goto loc_0030FD96;
loc_00310847:
    result = ~(*(uint64_t *)(local_r13 + 0xC8));
    local_r14 = (local_r14) & (result);
    goto loc_0030FE41;
loc_00310860:
    result = KiReadyDeferredReadyList(Arg1, v_stack_m180, v_stack_m188, v_stack_p10);
    goto loc_003112AB;
loc_00310872:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m198 + 0x74)))) & (8)) != 0) goto loc_0030FC3C;
    v_stack_m128 = *(uint64_t *)(local_r13 + 0x8);
    result = KiRemoveThreadFromReadyQueue(v_stack_m138, local_r13, (uint32_t)((uint32_t)(local_r14)), v_stack_p10);
    result = KiInsertDeferredReadyList(v_stack_m180, v_stack_m198, (uint32_t)((uint32_t)(local_r14)), v_stack_p10);
    goto loc_0030FC40;
loc_003108A7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x74)))) & (8)) != 0) goto loc_0030FD38;
    result = KiRemoveCurrentThreadScbReadyQueueEnumerator(v_stack_m168, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8, (uint32_t)((uint32_t)(local_r14)), v_stack_p10);
    result = KiInsertDeferredReadyList(v_stack_m180, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8, (uint32_t)((uint32_t)(local_r14)), v_stack_p10);
    goto loc_0030FD38;
loc_003108D1:
    result = (uint32_t)(((uint32_t)(v_stack_m18C)) + 1);
    local_r15 = 0;
    v_stack_m18C = (uint32_t)(result);
    goto loc_0030F861;
loc_003108F8:
    local_r13 = (uint32_t)(((uint32_t)(Arg5)) + 1);
    local_r14 = 0;
    goto loc_0030FD3B;
loc_0031090A:
    v_stack_m150 = 0;
    v_stack_m154 = 32;
    v_stack_m160 = v_stack_m180;
    goto loc_0030FAFA;
loc_00310930:
    goto loc_0030F861;
loc_00310945:
    v_stack_m150 = 0;
    goto loc_0030FACF;
loc_00310952:
    local_rsi = 0;
    goto loc_0030FB8D;
loc_00310959:
    goto loc_0030FC89;
loc_00310961:
    Arg1 = (uint32_t)((*(uint16_t *)(local_r14 + 0x88)) << (6));
    v_stack_m94 = 0;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8 + 33856)));
    v_stack_m94 = (uint32_t)(*(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8 + 33856);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x78)))) & (2)) == 0) goto loc_00310A2C;
    result = (v_stack_m198) | (*(uint64_t *)(*(uint64_t *)(v_rip - 0x31098D + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC12848) + arg1 * 4)) * 8 + 0xFC8C40) + 0x8E60));
    goto loc_0030FDFE;
loc_003109B5:
    Arg1 = (uint32_t)((*(uint16_t *)(0 + 0x88)) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r13)));
    v_stack_m7C = (uint32_t)(local_r13);
    if (((2) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x78))))) == 0) goto loc_00310A3B;
    local_r15 = (local_r15) | (*(uint64_t *)(*(uint64_t *)(v_rip - 0x3109DA + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC127F4) + arg1 * 4)) * 8 + 0xFC8C40) + 0x8E60));
loc_003109F0:
    v_stack_m198 = local_r15;
    result = KiRemoveCurrentThreadScbReadyQueueEnumerator(v_stack_m168, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8, v_stack_m198, 0);
    result = KiInsertDeferredReadyList(v_stack_m180, *(uint64_t *)(arg1 + 0x37E8) + 0 + 0 * 4 * 8, v_stack_m198, 0);
    goto loc_0030FD42;
loc_00310A14:
    result = (result) | (*(uint64_t *)(v_stack_m180 + 0xC8));
    goto loc_0030FDF7;
loc_00310A20:
    local_r15 = (local_r15) | (*(uint64_t *)(v_stack_m180 + 0xC8));
    goto loc_0030FE92;
loc_00310A2C:
    result = (result) | (*(uint64_t *)(v_stack_m180 + 0xC8));
    goto loc_0030FDFE;
loc_00310A3B:
    local_r15 = (local_r15) | (*(uint64_t *)(v_stack_m180 + 0xC8));
    goto loc_003109F0;
loc_00310A44:
loc_00310A50:
    result = ~(*(uint64_t *)(v_stack_m188 + 0xC8));
    local_rsi = (0) & (result);
    local_r14 = (local_r14) & (result);
    v_stack_m140 = local_rsi;
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_m108, local_r13, v_stack_m188, 0);
    goto loc_0030FD96;
loc_00310A6B:
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x35D9)) != 0) goto loc_00310C72;
    *(uint8_t *)(arg1 + 0x35D9) = 1;
    *(uint32_t *)(arg1 + 0x35DC) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x24)));
loc_00310A90:
    if (((*(uint8_t *)(2 + 0x33)) & ((uint8_t)(local_r14))) != 0) goto loc_0031107F;
loc_00310A9A:
    if (((*(uint8_t *)(2 + 0x33)) & (4)) == 0) goto loc_00310AB4;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x8EB8) != 0) goto loc_00310CC4;
loc_00310AB4:
    result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + 0x0 + 0x0 * 4 * 8 + 0x8EB8);
    if (((*(uint8_t *)(2 + 0x33)) & (1)) != 0) {
        result = *(uint64_t *)(2 + 0x28);
    }
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((uint32_t)(local_rsi)) < ((uint32_t)(*(uint8_t *)(local_r15)))) goto loc_00310C40;
loc_00310AE7:
    local_r15 = 0;
    goto loc_00310DCB;
loc_00310AEF:
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p10 + 0x88)) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(local_r13)));
    v_stack_m68 = 0;
    v_stack_m68 = (uint32_t)(local_r13);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m188))) >> (1));
    Arg2 = (uint32_t)((Arg2) & (1));
    result = KiTryAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(v_rip - 0x310B2D + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC126B0) + arg1 * 4)) * 8 + 0xFC8C40), Arg2, v_stack_mF0, 0);
    if ((uint8_t)(result) == 0) goto loc_00311093;
    result = KiIsIsolationUnitIdleByHandle(v_stack_mF0, Arg2, v_stack_mF0, 0);
    if ((uint32_t)(result) == 0) goto loc_0031117B;
    if (*(uint64_t *)(local_r15) == 0) goto loc_00310B91;
    Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x310B2D + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC126B0) + arg1 * 4)) * 8 + 0xFC8C40) + 0xD8))) + (*(uint64_t *)(local_r15));
    result = KiIsThreadConstrainedBySchedulingGroup(v_stack_mF8, Arg2, v_stack_mF0, 0);
    if ((uint8_t)(result) == 0) goto loc_00310B91;
    result = KiShouldPreemptionBeDeferred(v_stack_mF8, Arg2, v_stack_mF0, 0);
    if ((uint8_t)(result) != 0) goto loc_00310B91;
    result = KiCheckForMaxOverQuotaScb(Arg2, Arg2, v_stack_mF0, 0);
    if ((uint8_t)(result) != 0) goto loc_00311177;
loc_00310B91:
    v_stack_mC8 = *(uint64_t *)(v_stack_mC8 + 0x8);
    result = KiRemoveThreadFromSharedReadyQueue(v_stack_mD8, v_stack_mF8, v_stack_mCC, 0);
    Arg2 = 0;
    result = memset(*(uint64_t *)(arg1 + 0x37E8), Arg2, 240, 0);
    Arg3 = 0;
    result = KiStartRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), v_stack_mF0, Arg3, 0);
    Arg4 = 0;
    v_stack_m1A8 = v_stack_m178;
    result = KiScheduleThreadToRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), v_stack_mF8, *(uint64_t *)(v_rip - 0x310B2D + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC126B0) + arg1 * 4)) * 8 + 0xFC8C40), Arg4);
    Arg3 = 0;
    result = KiCommitRescheduleContext(*(uint64_t *)(arg1 + 0x37E8), Arg1, Arg3, v_stack_m178);
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_mF0, Arg1, Arg3, v_stack_m178);
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_00310DD4;
    local_rsi = 0;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8))) <= 0) goto loc_00310AE7;
loc_00310C40:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rsi + local_rsi * 4 * 8 + 0x33))) & (16)) != 0) goto loc_00310A6B;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rsi + local_rsi * 4 * 8 + 0x33))) & (8)) == 0) goto loc_00310A90;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rsi + local_rsi * 4 * 8 + 0x10) + 0x7)) == 0) goto loc_00310A90;
    goto loc_00310A6B;
loc_00310C72:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rsi + local_rsi * 4 * 8 + 0x33))) != 1) goto loc_00310CBA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x35DC)))) == (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rsi + local_rsi * 4 * 8 + 0x10) + 0x24))) goto loc_00310A90;
    *(uint8_t *)(arg1 + 0x35D9) = (uint8_t)(local_rsi + 2);
    result = KeAddProcessorAffinityEx(Arg1 + 13792, (uint32_t)(*(uint32_t *)(arg1 + 0x35DC)), Arg3, v_stack_m178);
loc_00310C9F:
    result = KeAddGroupAffinityEx(Arg1 + 13792, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rsi + local_rsi * 4 * 8 + 0x10) + 0xD0), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rsi + local_rsi * 4 * 8 + 0x10) + 0xC8), v_stack_m178);
    goto loc_00310A90;
loc_00310CBA:
    goto loc_00310C9F;
loc_00310CC4:
    if ((*(uint64_t *)(arg1 + 0x8EB8)) == 0) goto loc_00310AB4;
    if (Arg1 == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rsi + local_rsi * 4 * 8 + 0x10))) goto loc_00310AB4;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result))))) & (0x40000ULL));
    result = Arg1 + 36536;
    if (!(condition_is_equal)) {
        result = Arg1 + 36536;
    }
    if (condition_is_above_or_equal) goto loc_00311220;
loc_00310D06:
    *(uint32_t *)(*(uint64_t *)(result) + 0xC) = (uint32_t)(local_rsi + 2);
    local_r13 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rsi + local_rsi * 4 * 8 + 0x10) + 0x24));
    if ((*(uint8_t *)(v_rip + 0xCB42FA)) == 0) {
        result = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rsi + local_rsi * 4 * 8 + 0x10) + 0x24)));
        Arg2 = v_rip - 3214628;
        local_r13 = *(uint8_t *)(arg2 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rsi + local_rsi * 4 * 8 + 0x10) + 0x24)) * 2 + 0xFCD260);
        local_r13 = (uint32_t)((local_r13) << (6));
        result = *(uint8_t *)(arg2 + result * 2 + 0xFCD261);
        local_r13 = (uint32_t)((local_r13) | ((uint32_t)(result)));
    }
    *(uint32_t *)(*(uint64_t *)(result) + 0x8) = (uint32_t)(local_r13);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xCB5DCE));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCB5DCE)))) & (32)) != 0) {
        Arg1 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rsi + local_rsi * 4 * 8 + 0x10) + 0x24);
        Arg2 = (uint32_t)(local_rsi + 2);
        result = EtwTraceXSchedulerPriorityKickSend(Arg1, Arg2, (uint32_t)(*(uint32_t *)(result)), Arg4);
    }
    Arg2 = ((uint32_t)((uint32_t)(local_r13))) >> (32);
    goto loc_00310AB4;
loc_00310D6B:
    v_stack_mE0 = local_rsi + 2;
    v_stack_mE8 = *(uint64_t *)(arg1 + 0x37E8);
    if (v_stack_mE8 != 0) goto loc_00311009;
loc_00310D84:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x2 + 0x8))) & ((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x37E8) + local_rsi + local_rsi * 4 * 8 + 0x10))));
    v_stack_mD8 = local_rsi + 2;
    v_stack_mD0 = (uint32_t)(result);
    v_stack_mC0 = local_rsi + 2 + 64;
    if (condition_is_equal) goto loc_00311000;
    Arg1 = ((uint32_t)((uint32_t)(result))) << (4);
    Arg1 = (Arg1) + (local_rsi + 2 + 64);
    v_stack_m6C = (uint32_t)(result);
    v_stack_mC8 = Arg1;
    v_stack_mCC = (uint8_t)(result);
loc_00310DB5:
    v_stack_mF0 = *(uint64_t *)(arg1 + 0x37E8);
    v_stack_p28 = (uint32_t)(*(uint64_t *)(arg1 + 0x37E8));
    v_stack_m198 = *(uint64_t *)(arg1 + 0x37E8);
loc_00310DCB:
    goto loc_00310DD7;
loc_00310DD4:
    local_r15 = 0;
loc_00310DD7:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x37E8))))) >= 64) goto loc_00310DFF;
    v_stack_mF8 = 0;
    result = KiAdvanceReadyListEnumerator(v_stack_mD0, v_stack_mF8, (uint32_t)(*(uint32_t *)(result)), Arg4);
    if (sign_flag) goto loc_00310DFF;
    Arg1 = (*(uint64_t *)(v_stack_p10 + 0x8)) & (*(uint64_t *)(arg1 + 0x37E8) + local_rsi + local_rsi * 4 * 8);
    if (condition_is_not_equal) goto loc_00310E72;
loc_00310DFF:
    if (((*(uint32_t *)(v_rip + 0xCB5D2F)) & (0x200000ULL)) == 0) goto loc_00310E68;
    if (v_stack_mE8 != 0) goto loc_00310E42;
    if (v_stack_mE8 == v_stack_mE8) goto loc_0030F71D;
    result = KxWaitForLockChainValid(v_stack_mE8, v_stack_mF8, (uint32_t)(*(uint32_t *)(result)), Arg4);
loc_00310E42:
    v_stack_mE8 = 0;
    result = (uint8_t)((v_stack_mE0) ^ ((uint8_t)(v_stack_mE0)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0030F71D;
    result = KeWakeAddressAll(result + 8, v_stack_mE0, (uint32_t)(*(uint32_t *)(result)), Arg4);
    goto loc_0030F71D;
loc_00310E68:
    goto loc_0030F71D;
loc_00310E72:
    result = ~(*(uint64_t *)(arg1 + 0x37E8));
    result = (result) & (result + 8);
    v_stack_m110 = result;
    if (condition_is_equal) goto loc_00310DFF;
    if (((uint16_t)(*(uint16_t *)(v_stack_p10 + 0x88))) >= (*(uint16_t *)(*(uint64_t *)(v_stack_mF8 + 0x240)))) goto loc_003110F2;
loc_00310EA5:
    result = KiComputeThreadQos(v_stack_mF8, v_stack_mE0, (uint32_t)(*(uint32_t *)(result)), Arg4);
    Arg3 = (uint32_t)(*(uint32_t *)(v_stack_mF8 + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mF8 + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mF8 + 0x54))))) { Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mF8 + 0x54))); }
    Arg2 = (((uint32_t)(Arg3)) >= (*(uint32_t *)(v_rip + 0xCB44B0))) ? 1 : 0;
    Arg3 = (uint32_t)((Arg2 + result * 2) * ((uint32_t)(*(uint8_t *)(v_stack_p10 + 0xB9))));
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(*(uint8_t *)(v_stack_mF8 + 0x205))));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0xC0) + Arg3 + Arg3 * 2 * 8 + 0x10)) & (*(uint64_t *)(*(uint64_t *)(v_stack_mF8 + 0x240) + *(uint16_t *)(v_stack_p10 + 0x88) * 8 + 0x8));
    local_rbx = *(uint64_t *)(*(uint64_t *)(v_stack_mF8 + 0x240) + *(uint16_t *)(v_stack_p10 + 0x88) * 8 + 0x8);
    if (condition_is_not_equal) { local_rbx = Arg1; }
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_mF8 + 0x78))) >> (1);
    Arg1 = (uint32_t)((Arg1) & (1));
    result = (*(uint64_t *)(v_stack_p10 + arg1 * 8 + 0x10)) & (local_rbx);
    local_rdi = (v_stack_m110) & (result);
    v_stack_m110 = local_rdi;
    if (*(uint64_t *)(v_stack_mF8 + 0x68) != 0) goto loc_00311017;
loc_00310F34:
    result = KiCheckThreadAffinity(v_stack_mF8, *(uint64_t *)(v_stack_p10 + 0xC0) + Arg3 + Arg3 * 2 * 8, *(uint64_t *)(v_stack_mF8 + 0x68), Arg4);
    if (local_rdi != 0) goto loc_00310F5F;
    if ((uint32_t)(result) == 0) goto loc_003110C3;
loc_00310F49:
    local_r14 = (uint32_t)((Arg6) + 1);
    v_stack_p28 = (uint32_t)(local_r14);
    goto loc_00310DD7;
loc_00310F5F:
    if ((uint32_t)(result) == 0) goto loc_003110FA;
    v_stack_m170 = v_stack_p18 + 120;
loc_00310F77:
    if (local_rdi != 0) goto loc_00310AEF;
    if (local_rdi == 0) goto loc_003110AA;
    local_r15 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_p10 + 0x88)) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint64_t *)(v_stack_p10 + 0xC0) + Arg3 + Arg3 * 2 * 8)));
    v_stack_m60 = (uint32_t)(*(uint64_t *)(v_stack_p10 + 0xC0) + Arg3 + Arg3 * 2 * 8);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x78)))) & (2)) != 0) goto loc_003111AB;
    local_r13 = (v_stack_m198) | (*(uint64_t *)(*(uint64_t *)(v_rip - 0x310FBC + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC12212) + arg1 * 4)) * 8 + 0xFC8C40) + 0xC8));
loc_00310FD6:
    v_stack_m198 = local_r13;
    result = KiRemoveCurrentThreadSharedReadyQueueEnumerator(v_stack_mD8, v_stack_p18, v_stack_p18 + 120, Arg4);
    result = KiInsertDeferredReadyList(v_stack_m178, v_stack_p18, v_stack_p18 + 120, Arg4);
    goto loc_00310DD7;
loc_00311000:
    v_stack_mC8 = 0;
    goto loc_00310DB5;
loc_00311009:
    result = KxWaitForLockOwnerShip(v_stack_mE8, v_stack_p18, v_stack_p18 + 120, Arg4);
    goto loc_00310D84;
loc_00311017:
    result = KiIsThreadConstrainedBySchedulingGroup(v_stack_p18, v_stack_p18, v_stack_p18 + 120, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00310F34;
    result = KiShouldPreemptionBeDeferred(v_stack_p18, v_stack_p18, v_stack_p18 + 120, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00310F34;
    result = KiReduceToUnderMaxQuotaSet(*(uint16_t *)(v_stack_p10 + 0x88), local_rdi, v_stack_p18 + 120, Arg4);
    v_stack_m110 = result;
    if ((*(uint32_t *)(v_rip + 0xCB5CCE)) == 0) goto loc_00310F34;
    result = KiIsThreadRankBiased(v_stack_p18, Arg1, v_stack_p18 + 120, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00310F34;
    result = KiFindRankBiasedIdleSmtSet(v_stack_p10, v_stack_m110, v_stack_p18 + 120, Arg4);
    goto loc_00310F34;
loc_0031107F:
    Arg3 = 0;
    result = EtwTraceScheduleThread(*(uint64_t *)(v_stack_p18 + 0x28), v_stack_m110, Arg3, Arg4);
    goto loc_00310A9A;
loc_00311093:
    result = ~(*(uint64_t *)(local_r13 + 0xC8));
    local_rsi = (v_stack_p10) & (result);
    goto loc_00310F77;
loc_003110AA:
    local_r14 = (uint32_t)((local_r14) + 1);
    v_stack_p28 = (uint32_t)(local_r14);
    local_r15 = 0;
    goto loc_00310DD7;
loc_003110C3:
    v_stack_mC8 = *(uint64_t *)(v_stack_mC8 + 0x8);
    result = KiRemoveThreadFromSharedReadyQueue(v_stack_mD8, v_stack_p18, v_stack_mCC, Arg4);
    result = KiInsertDeferredReadyList(v_stack_m178, v_stack_p18, v_stack_mCC, Arg4);
    goto loc_00310F49;
loc_003110F2:
    goto loc_00310EA5;
loc_003110FA:
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x88)) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(v_stack_p18)));
    v_stack_m64 = (uint32_t)(v_stack_p18);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(0 + 0x78)))) & (2)) != 0) goto loc_003111A2;
    local_r13 = (local_r13) | (*(uint64_t *)(*(uint64_t *)(v_rip - 0x31111E + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xC120B0) + arg1 * 4)) * 8 + 0xFC8C40) + 0xC8));
loc_00311138:
    v_stack_m198 = local_r13;
    v_stack_mC8 = *(uint64_t *)(v_stack_mC8 + 0x8);
    result = KiRemoveThreadFromSharedReadyQueue(v_stack_mD8, 0, v_stack_mCC, Arg4);
    result = KiInsertDeferredReadyList(v_stack_m178, 0, v_stack_mCC, Arg4);
    v_stack_mF8 = 0;
    goto loc_00310DD7;
loc_00311177:
loc_0031117B:
    result = ~(*(uint64_t *)(local_r13 + 0xC8));
    local_rdi = (v_stack_m110) & (result);
    local_rsi = (local_rsi) & (result);
    v_stack_m110 = local_rdi;
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_mF0, 0, v_stack_mCC, Arg4);
    goto loc_00310F77;
loc_003111A2:
    local_r13 = (local_r13) | (*(uint64_t *)(v_stack_mF0 + 0x8E60));
    goto loc_00311138;
loc_003111AB:
    local_r13 = (local_r13) | (*(uint64_t *)(v_stack_mF0 + 0x8E60));
    goto loc_00310FD6;
loc_003111B7:
    if ((uint32_t)(Arg4) == 0) goto loc_00310207;
    if (((uint32_t)((uint8_t)(v_stack_m170))) >= ((uint32_t)(v_stack_mF0))) goto loc_00310207;
    goto loc_00310309;
loc_003111D9:
    if ((uint32_t)(Arg4) == 0) goto loc_003105A9;
    if (((uint32_t)((uint8_t)(v_stack_m170))) >= ((uint32_t)(v_stack_mF0))) goto loc_003105A9;
    goto loc_0031066F;
loc_003111FB:
    if (((*(uint32_t *)(v_rip + 0xCB5933)) & (0x200000ULL)) != 0) goto loc_00310D6B;
    v_stack_m70 = 0;
    if (condition_is_above_or_equal) goto loc_00310D84;
loc_00311220:
    if ((uint32_t)(Arg4) == 0) goto loc_00310AB4;
    if (((uint32_t)((uint8_t)(v_stack_m170))) >= ((uint32_t)(v_stack_mF0))) goto loc_00310AB4;
    goto loc_00310D06;
loc_00311242:
    goto loc_00310A50;
loc_00311252:
    result = KiIsThreadRankBiased(local_rdi, Arg1, v_stack_m170, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0031077C;
    result = KiFindRankBiasedIdleSmtSet(v_stack_p10, v_stack_m118, v_stack_m170, Arg4);
    goto loc_0031077C;
loc_0031127E:
loc_00311282:
    result = ~(*(uint64_t *)(local_r13 + 0xC8));
    local_rsi = (v_stack_m118) & (result);
    local_r14 = (local_r14) & (result);
    v_stack_m118 = local_rsi;
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_m100, v_stack_m118, v_stack_m170, Arg4);
    goto loc_0030FE41;
loc_003112AB:
    local_rsp = (local_rsp) + (400);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xD1` | `8` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x88` | `16` | `R` |
| `Arg6` | `+ 0x0` | `64` | `R/W` |
| `Arg6` | `+ 0x8` | `32` | `R` |
| `Arg6` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0030F500&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
