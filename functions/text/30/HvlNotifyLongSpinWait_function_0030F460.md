# HvlNotifyLongSpinWait

- RVA: `0x0030F460`–`0x0030F48A` (길이 `42` bytes)
- VA: `0x000000014030F460`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **494**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0030F47F` → [HvcallInitiateHypercall](../31/HvcallInitiateHypercall_function_00313630.md) (function, `0x00313630`)

### Direct callers
- [KiDeferGroupSchedulingPreemption](../20/KiDeferGroupSchedulingPreemption_function_0020076C.md) at `0x0020092F`
- [KiFlushReadyLists](../20/KiFlushReadyLists_function_002011E8.md) at `0x00201285`
- [sub_00201B22](../20/Unknown_function_00201B22.md) at `0x00201B55`
- [KiSchedulerApc](../20/KiSchedulerApc_function_00202BC0.md) at `0x00202E15`
- [KiResumeThread](../20/KiResumeThread_function_00203644.md) at `0x00203919`
- [KiResumeThread](../20/KiResumeThread_function_00203644.md) at `0x002039D5`
- [KeInsertQueueApc](../20/KeInsertQueueApc_function_00203F10.md) at `0x00204130`
- [KxWaitForSpinLockAndAcquire](../20/KxWaitForSpinLockAndAcquire_function_002085C0.md) at `0x0020860F`
- [sub_002092A9](../20/Unknown_function_002092A9.md) at `0x00209464`
- [sub_002098FF](../20/Unknown_function_002098FF.md) at `0x002099D7`
- [sub_002099FA](../20/Unknown_function_002099FA.md) at `0x00209AE5`
- [sub_002099FA](../20/Unknown_function_002099FA.md) at `0x00209C4E`
- [KeYieldExecution](../20/KeYieldExecution_function_00209FA0.md) at `0x0020A38C`
- [KeYieldExecution](../20/KeYieldExecution_function_00209FA0.md) at `0x0020A433`
- [sub_0020C2D4](../20/Unknown_function_0020C2D4.md) at `0x0020C334`
- [sub_0020C2D4](../20/Unknown_function_0020C2D4.md) at `0x0020C4AC`
- [sub_0020C2D4](../20/Unknown_function_0020C2D4.md) at `0x0020C9A9`
- [sub_0020C2D4](../20/Unknown_function_0020C2D4.md) at `0x0020C9D0`
- [sub_0020C2D4](../20/Unknown_function_0020C2D4.md) at `0x0020C9F7`
- [sub_0020C2D4](../20/Unknown_function_0020C2D4.md) at `0x0020CB2F`
- [KiActivateWaiterQueueWithNoLocks](../20/KiActivateWaiterQueueWithNoLocks_function_0020CEB0.md) at `0x0020D0FF`
- [sub_0020D1EC](../20/Unknown_function_0020D1EC.md) at `0x0020D56F`
- [sub_0020D8DF](../20/Unknown_function_0020D8DF.md) at `0x0020D994`
- [sub_0020D8DF](../20/Unknown_function_0020D8DF.md) at `0x0020DA66`
- [sub_0020D8DF](../20/Unknown_function_0020D8DF.md) at `0x0020DA8E`
- [sub_0020D8DF](../20/Unknown_function_0020D8DF.md) at `0x0020DAB6`
- [sub_0020D8DF](../20/Unknown_function_0020D8DF.md) at `0x0020DAFE`
- [KiCommitThreadWait](../20/KiCommitThreadWait_function_0020DFE0.md) at `0x0020E332`
- [KiCommitThreadWait](../20/KiCommitThreadWait_function_0020DFE0.md) at `0x0020E4A1`
- [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) at `0x0020ECEB`
- [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) at `0x0020EE23`
- [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) at `0x0020EE4A`
- [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) at `0x0020EF8A`
- [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) at `0x0020F0B7`
- [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) at `0x0020F4AA`
- [sub_00210E15](../21/Unknown_function_00210E15.md) at `0x00210EA4`
- [sub_002142F9](../21/Unknown_function_002142F9.md) at `0x0021494F`
- [sub_002142F9](../21/Unknown_function_002142F9.md) at `0x002149D2`
- [sub_00216B16](../21/Unknown_function_00216B16.md) at `0x00216B45`
- [sub_00216B4F](../21/Unknown_function_00216B4F.md) at `0x00216DC0`
- [sub_00216E70](../21/Unknown_function_00216E70.md) at `0x00216E85`
- [sub_002175E7](../21/Unknown_function_002175E7.md) at `0x00217615`
- [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) at `0x00217AE4`
- [sub_002180B5](../21/Unknown_function_002180B5.md) at `0x002180E3`
- [KiAttachProcess](../21/KiAttachProcess_function_002182D0.md) at `0x00218576`
- [sub_002188FB](../21/Unknown_function_002188FB.md) at `0x0021892A`
- [KiUpdateSoftParkElectionStatisticsOnInsertion](../21/KiUpdateSoftParkElectionStatisticsOnInsertion_function_00218F40.md) at `0x00219110`
- [KiRemoveBoostThread](../21/KiRemoveBoostThread_function_00219128.md) at `0x0021938F`
- [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) at `0x00219D80`
- [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) at `0x00219E1B`
- [KiRetireDpcList](../21/KiRetireDpcList_function_0021A0B0.md) at `0x0021AF44`
- [KiNormalPriorityReadyScan](../21/KiNormalPriorityReadyScan_function_0021B400.md) at `0x0021B6A2`
- [sub_0021B985](../21/Unknown_function_0021B985.md) at `0x0021B9A2`
- [sub_0021BDD6](../21/Unknown_function_0021BDD6.md) at `0x0021BFF0`
- [sub_0021C284](../21/Unknown_function_0021C284.md) at `0x0021C2A1`
- [sub_0021C284](../21/Unknown_function_0021C284.md) at `0x0021C46E`
- [KiQueueReadyThread](../21/KiQueueReadyThread_function_0021C7B0.md) at `0x0021D232`
- [KiQueueReadyThread](../21/KiQueueReadyThread_function_0021C7B0.md) at `0x0021D251`
- [sub_0021D7F8](../21/Unknown_function_0021D7F8.md) at `0x0021DC02`
- [sub_0021D7F8](../21/Unknown_function_0021D7F8.md) at `0x0021E369`
- [KiAbThreadInsertList](../21/KiAbThreadInsertList_function_0021F0E0.md) at `0x0021F182`
- [sub_0021F31C](../21/Unknown_function_0021F31C.md) at `0x0021F339`
- [sub_0021F36F](../21/Unknown_function_0021F36F.md) at `0x0021F60F`
- [KiWakePriQueueWaiter](../21/KiWakePriQueueWaiter_function_0021F720.md) at `0x0021F99E`
- [sub_0021FB57](../21/Unknown_function_0021FB57.md) at `0x0021FB74`
- [sub_0021FD23](../21/Unknown_function_0021FD23.md) at `0x0021FE8F`
- [sub_002203C4](../22/Unknown_function_002203C4.md) at `0x002203E1`
- [sub_00220639](../22/Unknown_function_00220639.md) at `0x00220657`
- [sub_002208AD](../22/Unknown_function_002208AD.md) at `0x002208CB`
- [KiFastExitThreadWait](../22/KiFastExitThreadWait_function_00220BB0.md) at `0x00220CDC`
- [KiFastExitThreadWait](../22/KiFastExitThreadWait_function_00220BB0.md) at `0x00220DF8`
- [KiSetPriorityThread](../22/KiSetPriorityThread_function_00220E78.md) at `0x00220FA0`
- [KiSwapDirectoryTableBaseTarget](../22/KiSwapDirectoryTableBaseTarget_function_00227FF0.md) at `0x002280A5`
- [KiSwapDirectoryTableBaseTarget](../22/KiSwapDirectoryTableBaseTarget_function_00227FF0.md) at `0x00228109`
- [MiTranslatePageForCopy](../22/MiTranslatePageForCopy_function_00228960.md) at `0x00228D60`
- [MiTranslatePageForCopy](../22/MiTranslatePageForCopy_function_00228960.md) at `0x00228D7D`
- [MiReplacePageTablePage](../22/MiReplacePageTablePage_function_00229184.md) at `0x0022983C`
- [MiReplacePageTablePage](../22/MiReplacePageTablePage_function_00229184.md) at `0x002299B9`
- [MiReplacePageTablePage](../22/MiReplacePageTablePage_function_00229184.md) at `0x002299E1`
- [MiReplacePageTablePage](../22/MiReplacePageTablePage_function_00229184.md) at `0x00229ACD`
- [MiReplacePageTablePage](../22/MiReplacePageTablePage_function_00229184.md) at `0x00229AF5`
- [MiReplacePageTablePage](../22/MiReplacePageTablePage_function_00229184.md) at `0x00229B1D`
- [MiDemoteCombinedPte](../22/MiDemoteCombinedPte_function_0022ABAC.md) at `0x0022AF09`
- [MiDemoteCombinedPte](../22/MiDemoteCombinedPte_function_0022ABAC.md) at `0x0022AF71`
- [MiCombineWithExisting](../22/MiCombineWithExisting_function_0022B4B8.md) at `0x0022B8AC`
- [MiCombineWithExisting](../22/MiCombineWithExisting_function_0022B4B8.md) at `0x0022B8C8`
- [MiCombineInitialInstance](../22/MiCombineInitialInstance_function_0022BC0C.md) at `0x0022C8E1`
- [MiCombineInitialInstance](../22/MiCombineInitialInstance_function_0022BC0C.md) at `0x0022C910`
- [MiCombineInitialInstance](../22/MiCombineInitialInstance_function_0022BC0C.md) at `0x0022C965`
- [MiCombineInitialInstance](../22/MiCombineInitialInstance_function_0022BC0C.md) at `0x0022C997`
- [MiResolveProtoCombine](../22/MiResolveProtoCombine_function_0022CD00.md) at `0x0022CF3B`
- [MiHandleForkTransitionPte](../22/MiHandleForkTransitionPte_function_0022D34C.md) at `0x0022DAD3`
- [MiHandleForkTransitionPte](../22/MiHandleForkTransitionPte_function_0022D34C.md) at `0x0022DAFA`
- [MiHandleForkTransitionPte](../22/MiHandleForkTransitionPte_function_0022D34C.md) at `0x0022DB24`
- [MiHandleForkTransitionPte](../22/MiHandleForkTransitionPte_function_0022D34C.md) at `0x0022DB59`
- [MiBuildForkPte](../22/MiBuildForkPte_function_0022E32C.md) at `0x0022EFDC`
- [MiBuildForkPte](../22/MiBuildForkPte_function_0022E32C.md) at `0x0022F007`
- [MiBuildForkPte](../22/MiBuildForkPte_function_0022E32C.md) at `0x0022F037`
- [MiBuildForkPte](../22/MiBuildForkPte_function_0022E32C.md) at `0x0022F08F`
- [MiBuildForkPte](../22/MiBuildForkPte_function_0022E32C.md) at `0x0022F0B6`
- [MiBuildForkPte](../22/MiBuildForkPte_function_0022E32C.md) at `0x0022F0DD`
- [MiBuildForkPte](../22/MiBuildForkPte_function_0022E32C.md) at `0x0022F104`
- [MiBuildForkPte](../22/MiBuildForkPte_function_0022E32C.md) at `0x0022F12B`
- [ExpSetTimerObject](../23/ExpSetTimerObject_function_00231730.md) at `0x002320A9`
- [ExpSetTimerObject](../23/ExpSetTimerObject_function_00231730.md) at `0x00232179`
- [ExpSetTimerObject](../23/ExpSetTimerObject_function_00231730.md) at `0x0023219F`
- [ExpSetTimerObject](../23/ExpSetTimerObject_function_00231730.md) at `0x002321CE`
- [ExpSetTimerObject](../23/ExpSetTimerObject_function_00231730.md) at `0x0023225F`
- [ExpSetTimerObject](../23/ExpSetTimerObject_function_00231730.md) at `0x00232288`
- [sub_002329B4](../23/Unknown_function_002329B4.md) at `0x00232B24`
- [sub_002329B4](../23/Unknown_function_002329B4.md) at `0x00232BAF`
- [sub_002329B4](../23/Unknown_function_002329B4.md) at `0x00232BD3`
- [sub_002329B4](../23/Unknown_function_002329B4.md) at `0x00232BFA`
- [sub_002329B4](../23/Unknown_function_002329B4.md) at `0x00232C21`
- [sub_002329B4](../23/Unknown_function_002329B4.md) at `0x00232C48`
- [KiSetTimerEx](../23/KiSetTimerEx_function_00232CB0.md) at `0x00233136`
- [KiSetTimerEx](../23/KiSetTimerEx_function_00232CB0.md) at `0x002331D3`
- [KiSetTimerEx](../23/KiSetTimerEx_function_00232CB0.md) at `0x002331F8`
- [KiSetTimerEx](../23/KiSetTimerEx_function_00232CB0.md) at `0x0023321F`
- [KiSetTimerEx](../23/KiSetTimerEx_function_00232CB0.md) at `0x00233246`
- [KiSetTimerEx](../23/KiSetTimerEx_function_00232CB0.md) at `0x0023326E`
- [KiInsertTimerTable](../23/KiInsertTimerTable_function_00233400.md) at `0x002335D9`
- [KeSetTimer](../23/KeSetTimer_function_00233BE0.md) at `0x00234046`
- [KeSetTimer](../23/KeSetTimer_function_00233BE0.md) at `0x002340E3`
- [KeSetTimer](../23/KeSetTimer_function_00233BE0.md) at `0x00234108`
- [KeSetTimer](../23/KeSetTimer_function_00233BE0.md) at `0x0023412F`
- [KeSetTimer](../23/KeSetTimer_function_00233BE0.md) at `0x00234156`
- [KeSetTimer](../23/KeSetTimer_function_00233BE0.md) at `0x0023417E`
- [KiProcessExpiredTimerList](../23/KiProcessExpiredTimerList_function_00234200.md) at `0x00234646`
- [sub_00234FE8](../23/Unknown_function_00234FE8.md) at `0x00235006`
- [sub_00234FE8](../23/Unknown_function_00234FE8.md) at `0x0023502D`
- [sub_00234FE8](../23/Unknown_function_00234FE8.md) at `0x0023523F`
- [sub_00234FE8](../23/Unknown_function_00234FE8.md) at `0x0023526C`
- [sub_00234FE8](../23/Unknown_function_00234FE8.md) at `0x00235294`
- [sub_00234FE8](../23/Unknown_function_00234FE8.md) at `0x002352BF`
- [sub_00234FE8](../23/Unknown_function_00234FE8.md) at `0x002352E2`
- [sub_00234FE8](../23/Unknown_function_00234FE8.md) at `0x0023530F`
- [MmSetAddressRangeModifiedEx](../23/MmSetAddressRangeModifiedEx_function_00236F20.md) at `0x00237461`
- [sub_00238C83](../23/Unknown_function_00238C83.md) at `0x00238CC7`
- [MiLockWorkingSetOptimal](../23/MiLockWorkingSetOptimal_function_00238FC0.md) at `0x002393E3`
- [MiLockWorkingSetOptimal](../23/MiLockWorkingSetOptimal_function_00238FC0.md) at `0x002394B6`
- [sub_0023C6BE](../23/Unknown_function_0023C6BE.md) at `0x0023C6DB`
- [sub_0023C6E5](../23/Unknown_function_0023C6E5.md) at `0x0023C794`
- [sub_0023E278](../23/Unknown_function_0023E278.md) at `0x0023E4D3`
- [sub_0023E278](../23/Unknown_function_0023E278.md) at `0x0023E509`
- [MmStoreProbeAndLockPages](../23/MmStoreProbeAndLockPages_function_0023E570.md) at `0x0023E7D0`
- [sub_0023EBEE](../23/Unknown_function_0023EBEE.md) at `0x0023EC0B`
- [sub_0023ECA0](../23/Unknown_function_0023ECA0.md) at `0x0023ECD3`
- [sub_0023F124](../23/Unknown_function_0023F124.md) at `0x0023F32F`
- [MiWsleFlush](../23/MiWsleFlush_function_0023FB30.md) at `0x0023FF32`
- [MiDecommitHandleTransitionPte](../24/MiDecommitHandleTransitionPte_function_0024037C.md) at `0x002406A4`
- [MiDecommitAddToList](../24/MiDecommitAddToList_function_00242264.md) at `0x00242964`
- [MiDecommitAddToList](../24/MiDecommitAddToList_function_00242264.md) at `0x00242992`
- [MiDecommitAddToList](../24/MiDecommitAddToList_function_00242264.md) at `0x002429BF`
- [sub_00243804](../24/Unknown_function_00243804.md) at `0x00243821`
- [MiProbeUnlockPage](../24/MiProbeUnlockPage_function_00243860.md) at `0x00243B3D`
- [MiWalkVaRange](../24/MiWalkVaRange_function_00243BF0.md) at `0x00244806`
- [MiWalkVaRange](../24/MiWalkVaRange_function_00243BF0.md) at `0x00244C0A`
- [MiActOnPte](../24/MiActOnPte_function_00244C90.md) at `0x002454A4`
- [MiActOnPte](../24/MiActOnPte_function_00244C90.md) at `0x00245910`
- [sub_002461C2](../24/Unknown_function_002461C2.md) at `0x002461DF`
- [sub_0024682F](../24/Unknown_function_0024682F.md) at `0x0024684C`
- [KeResetEvent](../24/KeResetEvent_function_00248350.md) at `0x00248401`
- [sub_00248760](../24/Unknown_function_00248760.md) at `0x00248775`
- [sub_00248F05](../24/Unknown_function_00248F05.md) at `0x00248F1A`
- [sub_00249649](../24/Unknown_function_00249649.md) at `0x00249666`
- [sub_00249B6A](../24/Unknown_function_00249B6A.md) at `0x00249C1A`
- [MiAddPageToInsertList](../24/MiAddPageToInsertList_function_0024A950.md) at `0x0024AD14`
- [PopPepProcessEvent](../24/PopPepProcessEvent_function_0024B930.md) at `0x0024CB2A`
- [PopPepProcessEvent](../24/PopPepProcessEvent_function_0024B930.md) at `0x0024CB52`
- [IoSetIoCompletionEx3](../24/IoSetIoCompletionEx3_function_0024EEE0.md) at `0x0024F28C`
- [IopCompleteIrpInFileObjectList](../24/IopCompleteIrpInFileObjectList_function_0024F330.md) at `0x0024F8C5`
- [IoSetIoCompletionEx](../24/IoSetIoCompletionEx_function_0024FA80.md) at `0x0024FDAA`
- [sub_00250195](../25/Unknown_function_00250195.md) at `0x002501C9`
- [sub_0025036E](../25/Unknown_function_0025036E.md) at `0x00250383`
- [IopReleaseFileObjectLock](../25/IopReleaseFileObjectLock_function_00250A90.md) at `0x00250E3D`
- [sub_002514A5](../25/Unknown_function_002514A5.md) at `0x002514C2`
- [sub_002514A5](../25/Unknown_function_002514A5.md) at `0x00251621`
- [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) at `0x00251CE2`
- [KiProcessThreadWaitList](../25/KiProcessThreadWaitList_function_00252CC0.md) at `0x00252F90`
- [sub_0025308F](../25/Unknown_function_0025308F.md) at `0x002538C2`
- [sub_0025308F](../25/Unknown_function_0025308F.md) at `0x00253D24`
- [sub_0025308F](../25/Unknown_function_0025308F.md) at `0x002542EA`
- [sub_002546C5](../25/Unknown_function_002546C5.md) at `0x002546E2`
- [KiHeteroSelectProcessorToPreempt](../25/KiHeteroSelectProcessorToPreempt_function_002560D0.md) at `0x00256418`
- [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) at `0x00257F5E`
- [KiAbEntryRemoveFromTree](../26/KiAbEntryRemoveFromTree_function_00262410.md) at `0x00262B1E`
- [sub_00264063](../26/Unknown_function_00264063.md) at `0x002641A0`
- [sub_00264063](../26/Unknown_function_00264063.md) at `0x002641BF`
- [sub_002647A9](../26/Unknown_function_002647A9.md) at `0x002648D0`
- [MmProtectPool](../26/MmProtectPool_function_002697AC.md) at `0x00269E8D`
- [sub_0026F901](../26/Unknown_function_0026F901.md) at `0x0026F92F`
- [sub_002760C1](../27/Unknown_function_002760C1.md) at `0x0027617C`
- [sub_002762D6](../27/Unknown_function_002762D6.md) at `0x0027631E`
- [MiFastLockLeafPageTable](../27/MiFastLockLeafPageTable_function_00276340.md) at `0x00276F64`
- [MiFastLockLeafPageTable](../27/MiFastLockLeafPageTable_function_00276340.md) at `0x00276FD8`
- [MiFastLockLeafPageTable](../27/MiFastLockLeafPageTable_function_00276340.md) at `0x002771B1`
- [MiFastLockLeafPageTable](../27/MiFastLockLeafPageTable_function_00276340.md) at `0x002771DA`
- [MiWalkPageTablesRecursively](../27/MiWalkPageTablesRecursively_function_002796C0.md) at `0x0027B4CB`
- [MiWalkPageTablesRecursively](../27/MiWalkPageTablesRecursively_function_002796C0.md) at `0x0027B79A`
- [sub_0027C37D](../27/Unknown_function_0027C37D.md) at `0x0027C39A`
- [sub_0027C3A4](../27/Unknown_function_0027C3A4.md) at `0x0027C3C1`
- [MiAcquirePageListLock](../27/MiAcquirePageListLock_function_0027C450.md) at `0x0027CB6E`
- [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) at `0x00280B16`
- [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) at `0x00280C9C`
- [MiLockLowestValidPageTableEx](../28/MiLockLowestValidPageTableEx_function_00280D10.md) at `0x002815E3`
- [MiLockLowestValidPageTableEx](../28/MiLockLowestValidPageTableEx_function_00280D10.md) at `0x0028175D`
- [sub_00282570](../28/Unknown_function_00282570.md) at `0x00282633`
- [sub_0028271E](../28/Unknown_function_0028271E.md) at `0x00282813`
- [MiResolveTransitionFault](../28/MiResolveTransitionFault_function_00282940.md) at `0x00283529`
- [MiResolveTransitionFault](../28/MiResolveTransitionFault_function_00282940.md) at `0x0028359B`
- [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) at `0x0028448C`
- [MiWsleFree](../28/MiWsleFree_function_00284600.md) at `0x002852B6`
- [MiWsleFree](../28/MiWsleFree_function_00284600.md) at `0x002852F1`
- [MiWsleFree](../28/MiWsleFree_function_00284600.md) at `0x0028532A`
- [MiLockPageAndSetDirty](../28/MiLockPageAndSetDirty_function_002857A0.md) at `0x002858F1`
- [sub_002860AF](../28/Unknown_function_002860AF.md) at `0x002860D8`
- [sub_00286720](../28/Unknown_function_00286720.md) at `0x00286784`
- [MiAddPageToFlushMdl](../28/MiAddPageToFlushMdl_function_00286930.md) at `0x00286BD7`
- [MiGetPage](../28/MiGetPage_function_002884C0.md) at `0x002896B6`
- [MiGetPerfectColorHeadPage](../28/MiGetPerfectColorHeadPage_function_00289CA8.md) at `0x0028A03A`
- [MiFindContiguousPagesEx](../28/MiFindContiguousPagesEx_function_0028BDE0.md) at `0x0028CA41`
- [MiMigratePfn](../28/MiMigratePfn_function_0028DBB0.md) at `0x0028E195`
- [MiMigratePfn](../28/MiMigratePfn_function_0028DBB0.md) at `0x0028E1BC`
- [MiMigratePfn](../28/MiMigratePfn_function_0028DBB0.md) at `0x0028E1E3`
- [MiMigratePfn](../28/MiMigratePfn_function_0028DBB0.md) at `0x0028E20A`
- [MiMigratePfn](../28/MiMigratePfn_function_0028DBB0.md) at `0x0028E231`
- [sub_0028F316](../28/Unknown_function_0028F316.md) at `0x0028F344`
- [sub_0028F553](../28/Unknown_function_0028F553.md) at `0x0028F570`
- [sub_002901B8](../29/Unknown_function_002901B8.md) at `0x0029050C`
- [MiClearPteAccessed](../29/MiClearPteAccessed_function_00290630.md) at `0x00290990`
- [MiRevertPfnActivePageTable](../29/MiRevertPfnActivePageTable_function_002938F4.md) at `0x002939CB`
- [sub_0029430C](../29/Unknown_function_0029430C.md) at `0x0029436D`
- [MiLockSetPfnPriority](../29/MiLockSetPfnPriority_function_00294E10.md) at `0x00294E9C`
- [MiLockVadCore](../29/MiLockVadCore_function_00297170.md) at `0x00297217`
- [sub_0029D673](../29/Unknown_function_0029D673.md) at `0x0029D6B9`
- [KiOutSwapKernelStacks](../29/KiOutSwapKernelStacks_function_0029F628.md) at `0x0029F85E`
- [MiSwapStackPage](../29/MiSwapStackPage_function_0029FDE0.md) at `0x002A01D4`
- [MiSwapStackPageNoDpc](../2A/MiSwapStackPageNoDpc_function_002A0270.md) at `0x002A0485`
- [MiChangePageAttributeBatch](../2A/MiChangePageAttributeBatch_function_002A06E0.md) at `0x002A0A52`
- [KiWaitForContextSwap](../2A/KiWaitForContextSwap_function_002A172C.md) at `0x002A1774`
- [MiOutPageSingleKernelStack](../2A/MiOutPageSingleKernelStack_function_002A1790.md) at `0x002A1B78`
- [MiOutPageSingleKernelStack](../2A/MiOutPageSingleKernelStack_function_002A1790.md) at `0x002A1B94`
- [MiAllocateKernelStackPages](../2A/MiAllocateKernelStackPages_function_002A1BEC.md) at `0x002A224E`
- [MiAddSystemPageTableToList](../2A/MiAddSystemPageTableToList_function_002A23A4.md) at `0x002A24DF`
- [MmFreeIndependentPages](../2A/MmFreeIndependentPages_function_002A2510.md) at `0x002A2785`
- [MiLockAndDecrementShareCount](../2A/MiLockAndDecrementShareCount_function_002A2854.md) at `0x002A293B`
- [MiUnlockCodePage](../2A/MiUnlockCodePage_function_002A2AB8.md) at `0x002A2C69`
- [MiMakeSystemCachePteValid](../2A/MiMakeSystemCachePteValid_function_002A35D8.md) at `0x002A3821`
- [MiReleaseInPageRefs](../2A/MiReleaseInPageRefs_function_002A4214.md) at `0x002A4343`
- [MiMarkMdlComplete](../2A/MiMarkMdlComplete_function_002A75D0.md) at `0x002A7789`
- [MiReplaceRotateWithDemandZeroNoCopy](../2A/MiReplaceRotateWithDemandZeroNoCopy_function_002AAB04.md) at `0x002AAEAB`
- [MiGetSystemPage](../2A/MiGetSystemPage_function_002AB7E8.md) at `0x002AB8F7`
- [MiInitializeNewImageSectionProtos](../2A/MiInitializeNewImageSectionProtos_function_002ABB80.md) at `0x002ABD83`
- [MiInitializeImageProtos](../2A/MiInitializeImageProtos_function_002ABDAC.md) at `0x002AC0E9`
- [MiGetPageForHeader](../2A/MiGetPageForHeader_function_002AC120.md) at `0x002AC2D9`
- [MiInitializeTransitionPfn](../2A/MiInitializeTransitionPfn_function_002AC2E8.md) at `0x002AC481`
- [MiFinishMdlForMappedFileFault](../2A/MiFinishMdlForMappedFileFault_function_002AC974.md) at `0x002ACC25`
- [sub_002ADE02](../2A/Unknown_function_002ADE02.md) at `0x002ADE20`
- [sub_002ADE82](../2A/Unknown_function_002ADE82.md) at `0x002ADF2A`
- [MiInsertPhysicalPteMapping](../2A/MiInsertPhysicalPteMapping_function_002AE26C.md) at `0x002AE4F2`
- [MiCopyDataPageToImagePage](../2A/MiCopyDataPageToImagePage_function_002AE818.md) at `0x002AEE07`
- [MiGetWorkingSetInfoList](../2A/MiGetWorkingSetInfoList_function_002AF770.md) at `0x002B0D08`
- [sub_002B0F0E](../2B/Unknown_function_002B0F0E.md) at `0x002B0F23`
- [MiReplaceTransitionPage](../2B/MiReplaceTransitionPage_function_002B1120.md) at `0x002B197E`
- [sub_002B1D4E](../2B/Unknown_function_002B1D4E.md) at `0x002B2024`
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B3826`
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B384D`
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B3915`
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B393C`
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B39BE`
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B3A7C`
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B3C3F`
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B3C66`
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B3C91`
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B3CB8`
- [MiGetTopLevelPfn](../2B/MiGetTopLevelPfn_function_002B44E0.md) at `0x002B463C`
- [MiStoreWriteModifiedPages](../2B/MiStoreWriteModifiedPages_function_002B46C4.md) at `0x002B52D2`
- [MiInitializeReadInProgressPfn](../2B/MiInitializeReadInProgressPfn_function_002B6990.md) at `0x002B6E2F`
- [MiInitializeReadInProgressPfn](../2B/MiInitializeReadInProgressPfn_function_002B6990.md) at `0x002B6E56`
- [MiFinishHardFault](../2B/MiFinishHardFault_function_002B6F10.md) at `0x002B76A2`
- [MiFinishHardFault](../2B/MiFinishHardFault_function_002B6F10.md) at `0x002B76CA`
- [MiFinishHardFault](../2B/MiFinishHardFault_function_002B6F10.md) at `0x002B7738`
- [MiMakePageAvoidRead](../2B/MiMakePageAvoidRead_function_002B7DE0.md) at `0x002B841E`
- [MiCreateDecayPfn](../2B/MiCreateDecayPfn_function_002B8764.md) at `0x002B8A84`
- [MiCreateDecayPfn](../2B/MiCreateDecayPfn_function_002B8764.md) at `0x002B8AA0`
- [MiLockProtoPoolPage](../2B/MiLockProtoPoolPage_function_002B8B80.md) at `0x002B90A2`
- [MiLockProtoPoolPage](../2B/MiLockProtoPoolPage_function_002B8B80.md) at `0x002B90C9`
- [MiLockProtoPoolPage](../2B/MiLockProtoPoolPage_function_002B8B80.md) at `0x002B91E9`
- [MiLockSectionControlArea](../2B/MiLockSectionControlArea_function_002BC930.md) at `0x002BCB38`
- [PopPepUpdateIdleStateRefCount](../2B/PopPepUpdateIdleStateRefCount_function_002BF930.md) at `0x002BFC09`
- [MiLockWorkingSetCoreExclusive](../2C/MiLockWorkingSetCoreExclusive_function_002C0CFC.md) at `0x002C0DAA`
- [sub_002C1E2F](../2C/Unknown_function_002C1E2F.md) at `0x002C1E4D`
- [MiDeleteNonPagedPoolTail](../2C/MiDeleteNonPagedPoolTail_function_002C20F0.md) at `0x002C21C7`
- [MiComputeAgingAmount](../2C/MiComputeAgingAmount_function_002C2520.md) at `0x002C26B8`
- [MiProtectPrivateMemory](../2C/MiProtectPrivateMemory_function_002C45B0.md) at `0x002C4F9D`
- [MiSetProtectionOnTransitionPte](../2C/MiSetProtectionOnTransitionPte_function_002C586C.md) at `0x002C5AAD`
- [MiUpdatePfnProtection](../2C/MiUpdatePfnProtection_function_002C5AD0.md) at `0x002C5C04`
- [MiCompleteRestrictedImageFault](../2C/MiCompleteRestrictedImageFault_function_002C60D4.md) at `0x002C6438`
- [KeSetPriorityThread](../2C/KeSetPriorityThread_function_002C76E0.md) at `0x002C78DC`
- [MiDeleteRotateVa](../2C/MiDeleteRotateVa_function_002C79D4.md) at `0x002C7AFB`
- [MmAllocateNonChargedSecurePages](../2C/MmAllocateNonChargedSecurePages_function_002C886C.md) at `0x002C8A50`
- [MiInitializeMdlLeafPfns](../2C/MiInitializeMdlLeafPfns_function_002C8FDC.md) at `0x002C90D6`
- [MiInitializeMdlBatchPages](../2C/MiInitializeMdlBatchPages_function_002C90E4.md) at `0x002C935E`
- [KiInitiateGenericCallDpc](../2C/KiInitiateGenericCallDpc_function_002C9C40.md) at `0x002C9D11`
- [KiBeginThreadWait](../2C/KiBeginThreadWait_function_002CA8E0.md) at `0x002CAA67`
- [KiSetAffinityThread](../2C/KiSetAffinityThread_function_002CE010.md) at `0x002CE311`
- [KiIpiStallOnPacketTargetsPrcb](../2C/KiIpiStallOnPacketTargetsPrcb_function_002CE670.md) at `0x002CE6C7`
- [MiFreePageFileHashPfns](../2D/MiFreePageFileHashPfns_function_002DBEF8.md) at `0x002DC020`
- [MiFreeSlabEntry](../2D/MiFreeSlabEntry_function_002DC650.md) at `0x002DC925`
- [sub_002E0B15](../2E/Unknown_function_002E0B15.md) at `0x002E1004`
- [ExTryConvertSharedSpinLockExclusive](../2E/ExTryConvertSharedSpinLockExclusive_function_002EF4C0.md) at `0x002EF557`
- [ExpAddTagForBigPages](../2E/ExpAddTagForBigPages_function_002EF570.md) at `0x002EF927`
- [ExpTryConvertSharedSpinLockExclusiveInstrumented](../2E/ExpTryConvertSharedSpinLockExclusiveInstrumented_function_002EF988.md) at `0x002EFA58`
- [sub_002F6E32](../2F/Unknown_function_002F6E32.md) at `0x002F75E8`
- [KiUpdateThreadCpuSetAffinitiesFromDpcLevel](KiUpdateThreadCpuSetAffinitiesFromDpcLevel_function_003030C4.md) at `0x00303103`
- [KeSetSelectedCpuSetsThread](KeSetSelectedCpuSetsThread_function_003033D0.md) at `0x0030346C`
- [KiUpdateVpBackingThreadPriorityDpcRoutine](KiUpdateVpBackingThreadPriorityDpcRoutine_function_00303790.md) at `0x003038CC`
- [KiUpdateGlobalCpuSetConfiguration](KiUpdateGlobalCpuSetConfiguration_function_00305AB8.md) at `0x00305DCE`
- [KiInsertDeferredPreemptionApc](KiInsertDeferredPreemptionApc_function_0030A8E8.md) at `0x0030A9A6`
- [KiSoftParkElectionUnparkProcessor](KiSoftParkElectionUnparkProcessor_function_0030B818.md) at `0x0030B8F8`
- [KiEnterLongDpcProcessing](KiEnterLongDpcProcessing_function_0030BE54.md) at `0x0030C194`
- [KiAcquireMultiplePrcbLockArrays](KiAcquireMultiplePrcbLockArrays_function_0030D4D0.md) at `0x0030D570`
- [sub_0030E8E0](Unknown_function_0030E8E0.md) at `0x0030E9CC`
- [sub_0030E8E0](Unknown_function_0030E8E0.md) at `0x0030EAED`
- [sub_0030ED05](Unknown_function_0030ED05.md) at `0x0030ED31`
- [sub_0030EDE0](Unknown_function_0030EDE0.md) at `0x0030EE0C`
- [sub_0030EE9F](Unknown_function_0030EE9F.md) at `0x0030EFC5`
- [sub_0030F19D](Unknown_function_0030F19D.md) at `0x0030F235`
- [sub_0030F244](Unknown_function_0030F244.md) at `0x0030F261`
- [KiSearchForNewThreadsOnTarget](KiSearchForNewThreadsOnTarget_function_0030F500.md) at `0x0030F8DD`
- [KiIpiSendRequestEx](../31/KiIpiSendRequestEx_function_003112D0.md) at `0x00311359`
- [KiIpiWaitForRequestBarrier](../31/KiIpiWaitForRequestBarrier_function_003133C0.md) at `0x00313417`
- [MiLinkPoolCommitChain](../31/MiLinkPoolCommitChain_function_00313D20.md) at `0x003140D4`
- [KxSetTimeStampBusy](../31/KxSetTimeStampBusy_function_00314CC0.md) at `0x00314D35`
- [MiFreeDeferredCrcPages](../31/MiFreeDeferredCrcPages_function_00315018.md) at `0x003150FB`
- [MiSharePages](../31/MiSharePages_function_00315110.md) at `0x00315FC8`
- [MiSharePages](../31/MiSharePages_function_00315110.md) at `0x00316003`
- [MiSharePages](../31/MiSharePages_function_00315110.md) at `0x003160A2`
- [MiCrcStillIntact](../31/MiCrcStillIntact_function_00317028.md) at `0x0031727A`
- [MiObtainProtoReference](../31/MiObtainProtoReference_function_00318178.md) at `0x00318243`
- [MiObtainProtoReference](../31/MiObtainProtoReference_function_00318178.md) at `0x0031825F`
- [MiRelockProtoPoolPage](../31/MiRelockProtoPoolPage_function_0031826C.md) at `0x00318314`
- [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) at `0x0031A3CA`
- [MiCompareTbFlushTimeStamp](../31/MiCompareTbFlushTimeStamp_function_0031ADE4.md) at `0x0031AE4C`
- [MiSafeLockPageAtDpc](../31/MiSafeLockPageAtDpc_function_0031C67C.md) at `0x0031C701`
- [MiGetBaseResidentPage](../31/MiGetBaseResidentPage_function_0031C750.md) at `0x0031C8AA`
- [sub_0031CA77](../31/Unknown_function_0031CA77.md) at `0x0031CA95`
- [MiConvertLargeActivePageToChain](../31/MiConvertLargeActivePageToChain_function_0031D980.md) at `0x0031DC3A`
- [MiGetLargePage](../31/MiGetLargePage_function_0031E210.md) at `0x0031E585`
- [MiLockProtoPoolPageForce](../32/MiLockProtoPoolPageForce_function_00320E10.md) at `0x00321162`
- [sub_0032171B](../32/Unknown_function_0032171B.md) at `0x00321738`
- [MiResolveProtoPteFault](../32/MiResolveProtoPteFault_function_00321750.md) at `0x003222B8`
- [MiResolveProtoPteFault](../32/MiResolveProtoPteFault_function_00321750.md) at `0x003222DF`
- [MiLockOwnedProtoPage](../32/MiLockOwnedProtoPage_function_00322560.md) at `0x003226B9`
- [MiGetUltraMapping](../32/MiGetUltraMapping_function_00323270.md) at `0x003236B1`
- [MiGetUltraMapping](../32/MiGetUltraMapping_function_00323270.md) at `0x003237AA`
- [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) at `0x00323987`
- [ExpWaitForSpinLockExclusiveAndAcquire](../32/ExpWaitForSpinLockExclusiveAndAcquire_function_003239A0.md) at `0x00323A60`
- [sub_00323B23](../32/Unknown_function_00323B23.md) at `0x00323B46`
- [sub_003247A5](../32/Unknown_function_003247A5.md) at `0x00324802`
- [sub_00324954](../32/Unknown_function_00324954.md) at `0x00324971`
- [MiAddViewsForSection](../32/MiAddViewsForSection_function_00324990.md) at `0x00324E15`
- [MiReferenceActiveSubsection](../32/MiReferenceActiveSubsection_function_00325060.md) at `0x003255B6`
- [MiDeleteSubsectionPages](../32/MiDeleteSubsectionPages_function_00326340.md) at `0x00326474`
- [MiReturnPhysicalPoolPages](../32/MiReturnPhysicalPoolPages_function_00328568.md) at `0x003287B0`
- [MiReducePteUseCount](../32/MiReducePteUseCount_function_0032A160.md) at `0x0032A33E`
- [sub_0032BD21](../32/Unknown_function_0032BD21.md) at `0x0032C1EE`
- [MiCheckVadSequential](../32/MiCheckVadSequential_function_0032EBE0.md) at `0x0032EF06`
- [MiResolveSharedZeroFault](../32/MiResolveSharedZeroFault_function_0032EF20.md) at `0x0032F67A`
- [MiResolveSharedZeroFault](../32/MiResolveSharedZeroFault_function_0032EF20.md) at `0x0032F70D`
- [MiCompletePrivateZeroFault](../33/MiCompletePrivateZeroFault_function_00330CC0.md) at `0x00331B88`
- [MiCompletePrivateZeroFault](../33/MiCompletePrivateZeroFault_function_00330CC0.md) at `0x00331BAF`
- [MiCompletePrivateZeroFault](../33/MiCompletePrivateZeroFault_function_00330CC0.md) at `0x00331CE1`
- [MiCompletePrivateZeroFault](../33/MiCompletePrivateZeroFault_function_00330CC0.md) at `0x00331DB3`
- [MiInitializePfn](../33/MiInitializePfn_function_00331E60.md) at `0x00332472`
- [MiInitializePfn](../33/MiInitializePfn_function_00331E60.md) at `0x003324BE`
- [MiChangePageAttribute](../33/MiChangePageAttribute_function_00332ECC.md) at `0x003332A0`
- [MiAllocateWsle](../33/MiAllocateWsle_function_003332C0.md) at `0x00333C48`
- [MiAllocateWsle](../33/MiAllocateWsle_function_003332C0.md) at `0x00333C70`
- [MiAllocateWsle](../33/MiAllocateWsle_function_003332C0.md) at `0x00333D54`
- [MiAllocateWsle](../33/MiAllocateWsle_function_003332C0.md) at `0x00333F45`
- [MiPurgePartitionStandby](../33/MiPurgePartitionStandby_function_00334460.md) at `0x003345A8`
- [MiReleaseFreshPageAtDpc](../33/MiReleaseFreshPageAtDpc_function_00334B50.md) at `0x00334BBC`
- [sub_003354FB](../33/Unknown_function_003354FB.md) at `0x00335E7F`
- [MiUnlinkFreeOrZeroedPage](../33/MiUnlinkFreeOrZeroedPage_function_00336C40.md) at `0x0033754C`
- [sub_0033827F](../33/Unknown_function_0033827F.md) at `0x00338604`
- [MiAddKernelStackToPrcbCache](../33/MiAddKernelStackToPrcbCache_function_00338710.md) at `0x00338BF2`
- [MiAddKernelStackToPrcbCache](../33/MiAddKernelStackToPrcbCache_function_00338710.md) at `0x00338C21`
- [sub_00338E63](../33/Unknown_function_00338E63.md) at `0x00339708`
- [MiRestoreTransitionPte](../33/MiRestoreTransitionPte_function_0033DD90.md) at `0x0033E130`
- [sub_0033F84B](../33/Unknown_function_0033F84B.md) at `0x0033F8D7`
- [sub_0033F84B](../33/Unknown_function_0033F84B.md) at `0x0033F924`
- [sub_0033F84B](../33/Unknown_function_0033F84B.md) at `0x0033F94B`
- [sub_0033F84B](../33/Unknown_function_0033F84B.md) at `0x0033F972`
- [sub_0033F97C](../33/Unknown_function_0033F97C.md) at `0x0033F999`
- [KiWakeQueueWaiter](../34/KiWakeQueueWaiter_function_00344C10.md) at `0x00344E60`
- [KiWakeQueueWaiter](../34/KiWakeQueueWaiter_function_00344C10.md) at `0x00344E90`
- [sub_0034569C](../34/Unknown_function_0034569C.md) at `0x003456BA`
- [sub_003456C4](../34/Unknown_function_003456C4.md) at `0x003456E1`
- [MiCompleteProtoPteFault](../34/MiCompleteProtoPteFault_function_00345710.md) at `0x00346530`
- [MiCompleteProtoPteFault](../34/MiCompleteProtoPteFault_function_00345710.md) at `0x0034678A`
- [KeReleaseSemaphoreEx](../34/KeReleaseSemaphoreEx_function_003468C0.md) at `0x00346B72`
- [MiDeleteClusterPage](../34/MiDeleteClusterPage_function_00346CB0.md) at `0x0034704A`
- [MiDeleteClusterPage](../34/MiDeleteClusterPage_function_00346CB0.md) at `0x00347073`
- [sub_003478B2](../34/Unknown_function_003478B2.md) at `0x003478C7`
- [sub_003478D0](../34/Unknown_function_003478D0.md) at `0x00347900`
- [MiConvertSmallPageRangeToLarge](../34/MiConvertSmallPageRangeToLarge_function_003484DC.md) at `0x003486BA`
- [MiConvertSmallPageRangeToLarge](../34/MiConvertSmallPageRangeToLarge_function_003484DC.md) at `0x003486D9`
- [MiReturnWsToExpansionList](../35/MiReturnWsToExpansionList_function_003504E0.md) at `0x00350684`
- [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) at `0x003508CD`
- [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) at `0x003508FD`
- [KeRundownQueueCommon](../35/KeRundownQueueCommon_function_003515F4.md) at `0x00351730`
- [KeDeleteMutant](../35/KeDeleteMutant_function_00351788.md) at `0x00351986`
- [KiForceIdleParkUnparkProcessor](../35/KiForceIdleParkUnparkProcessor_function_003523B8.md) at `0x00352490`
- [sub_00352D10](../35/Unknown_function_00352D10.md) at `0x00352E1E`
- [sub_00352D10](../35/Unknown_function_00352D10.md) at `0x00352E46`
- [sub_00353356](../35/Unknown_function_00353356.md) at `0x0035336B`
- [KiSendHeteroRescheduleIntRequestHelper](../35/KiSendHeteroRescheduleIntRequestHelper_function_0035420C.md) at `0x003543E1`
- [KiSendHeteroRescheduleIntRequestHelper](../35/KiSendHeteroRescheduleIntRequestHelper_function_0035420C.md) at `0x00354764`
- [KiIdleSchedule](../35/KiIdleSchedule_function_00355000.md) at `0x003550DA`
- [KeTerminateThread](../35/KeTerminateThread_function_00355138.md) at `0x0035541B`
- [KiInSwapSingleProcess](../35/KiInSwapSingleProcess_function_00355474.md) at `0x00355534`
- [KiSwapThread](../35/KiSwapThread_function_00355640.md) at `0x003557A0`
- [KiRemoveThreadFromSchedulingGroup](../35/KiRemoveThreadFromSchedulingGroup_function_00356514.md) at `0x00356725`
- [KiRemoveThreadFromSchedulingGroup](../35/KiRemoveThreadFromSchedulingGroup_function_00356514.md) at `0x00356744`
- [MiProcessWsInSwapFault](../36/MiProcessWsInSwapFault_function_00361EFC.md) at `0x00361FFF`
- [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) at `0x0036244A`
- [MiCopyOnWrite](../36/MiCopyOnWrite_function_00362A0C.md) at `0x00363434`
- [MiCopyOnWrite](../36/MiCopyOnWrite_function_00362A0C.md) at `0x0036345B`
- [MiInitializeHardFaultPfn](../36/MiInitializeHardFaultPfn_function_00363DD8.md) at `0x00363F59`
- [MiReturnPfnReferenceCountAtDpc](../36/MiReturnPfnReferenceCountAtDpc_function_00364010.md) at `0x00364077`
- [MiPfPutPagesInTransition](../36/MiPfPutPagesInTransition_function_003640EC.md) at `0x00364B6A`
- [MiReplacePageOfProtoPool](../36/MiReplacePageOfProtoPool_function_00364BB8.md) at `0x003652FA`
- [MiReplacePageOfProtoPool](../36/MiReplacePageOfProtoPool_function_00364BB8.md) at `0x00365321`
- [MiReplacePageOfProtoPool](../36/MiReplacePageOfProtoPool_function_00364BB8.md) at `0x00365348`
- [MiLockLeafPage](../36/MiLockLeafPage_function_003658C0.md) at `0x00365AA7`
- [MiLockLeafPage](../36/MiLockLeafPage_function_003658C0.md) at `0x00365AC7`
- [MiZeroCfgSystemWideBitmapWorker](../36/MiZeroCfgSystemWideBitmapWorker_function_00367060.md) at `0x0036773A`
- [MiFreeUnmappedPageTables](../36/MiFreeUnmappedPageTables_function_003678E0.md) at `0x003679A0`
- [MiInitializeEnclavePfn](../36/MiInitializeEnclavePfn_function_003682A8.md) at `0x0036832B`
- [MiUpdateAwePageTable](../36/MiUpdateAwePageTable_function_00368730.md) at `0x003687B9`
- [MiDeleteEnclavePage](../36/MiDeleteEnclavePage_function_00368CCC.md) at `0x00368D78`
- [MiPrivateFixup](../36/MiPrivateFixup_function_003693E8.md) at `0x0036998B`
- [MiHandleCollidedFault](../36/MiHandleCollidedFault_function_00369B48.md) at `0x00369CD8`
- [MiWaitForCollidedFaultComplete](../36/MiWaitForCollidedFaultComplete_function_00369EDC.md) at `0x0036A1A2`
- [MiWaitForCollidedFaultComplete](../36/MiWaitForCollidedFaultComplete_function_00369EDC.md) at `0x0036A1CB`
- [MiCopyFileOnlyGlobalSubsectionPage](../36/MiCopyFileOnlyGlobalSubsectionPage_function_0036A9EC.md) at `0x0036AA64`
- [MiCopyFileOnlyGlobalSubsectionPage](../36/MiCopyFileOnlyGlobalSubsectionPage_function_0036A9EC.md) at `0x0036ADCA`
- [MiDecommitPrivatePageTail](../36/MiDecommitPrivatePageTail_function_0036F564.md) at `0x0036F802`
- [MiLockCode](../36/MiLockCode_function_0036F91C.md) at `0x0036FDB6`
- [MiLockCode](../36/MiLockCode_function_0036F91C.md) at `0x0036FFF2`
- [MiDecommitSharedPageTail](../37/MiDecommitSharedPageTail_function_00370240.md) at `0x003706E1`
- [MiLockCloneBlockAtDpc](../37/MiLockCloneBlockAtDpc_function_00370FD8.md) at `0x00371031`
- [MiTryDeleteTransitionPte](../37/MiTryDeleteTransitionPte_function_003710DC.md) at `0x003712DC`
- [MiPurgeSubsection](../37/MiPurgeSubsection_function_003712F0.md) at `0x00371949`
- [sub_00371F2D](../37/Unknown_function_00371F2D.md) at `0x00371F4A`
- [MiOutSwapWorkingSetPte](../37/MiOutSwapWorkingSetPte_function_00372190.md) at `0x003727E3`
- [MiOutSwapWorkingSetPte](../37/MiOutSwapWorkingSetPte_function_00372190.md) at `0x0037280B`
- [MiUnlockStoreLockedPages](../37/MiUnlockStoreLockedPages_function_003735C0.md) at `0x00373783`
- [MiDeleteSectionCluster](../37/MiDeleteSectionCluster_function_00373DF0.md) at `0x0037434D`
- [MiTradeActivePage](../37/MiTradeActivePage_function_00374424.md) at `0x0037473D`
- [MiTradeActivePage](../37/MiTradeActivePage_function_00374424.md) at `0x00374764`
- [MiZeroAndReleasePages](../37/MiZeroAndReleasePages_function_003748D0.md) at `0x00374D48`
- [MiCreateSlabEntry](../37/MiCreateSlabEntry_function_00374DEC.md) at `0x0037537A`
- [MiLockPageListAndFirstPage](../37/MiLockPageListAndFirstPage_function_0037573C.md) at `0x003758AE`
- [MiFreeMdlPageRun](../37/MiFreeMdlPageRun_function_00375A4C.md) at `0x00375D3C`
- [MiFreeSmallPageFromMdl](../37/MiFreeSmallPageFromMdl_function_00375D58.md) at `0x00375FE1`
- [MiGetPageFromSlabAllocator](../37/MiGetPageFromSlabAllocator_function_00377294.md) at `0x0037768D`
- [MiFinishLargePageFree](../37/MiFinishLargePageFree_function_00377B94.md) at `0x00377D4D`
- [MiDecreaseUsedPtes](../37/MiDecreaseUsedPtes_function_00378080.md) at `0x00378251`
- [MiRewriteTrimPteAsDemandZero](../38/MiRewriteTrimPteAsDemandZero_function_003823F4.md) at `0x003825D3`
- [MiDuplicateCloneLeaf](../38/MiDuplicateCloneLeaf_function_003825F0.md) at `0x0038298E`
- [MiDuplicateCloneLeaf](../38/MiDuplicateCloneLeaf_function_003825F0.md) at `0x003829B1`
- [MiDuplicateCloneLeaf](../38/MiDuplicateCloneLeaf_function_003825F0.md) at `0x003829E0`
- [MiInitializePfnForOtherProcess](../38/MiInitializePfnForOtherProcess_function_00382A20.md) at `0x00382CCA`
- [MiInitializePfnForOtherProcess](../38/MiInitializePfnForOtherProcess_function_00382A20.md) at `0x00382CE9`
- [MiWriteUselessChildPte](../38/MiWriteUselessChildPte_function_00382CFC.md) at `0x00382D82`
- [MiMarkPfnVerified](../38/MiMarkPfnVerified_function_003833C4.md) at `0x003834B6`
- [MiReservePageFileSpaceForPage](../38/MiReservePageFileSpaceForPage_function_0038377C.md) at `0x00383D89`
- [MiReservePageFileSpaceForPage](../38/MiReservePageFileSpaceForPage_function_0038377C.md) at `0x00383E16`
- [MiSetSystemCodeProtection](../38/MiSetSystemCodeProtection_function_00384420.md) at `0x003848B3`
- [MiSetSystemCodeProtection](../38/MiSetSystemCodeProtection_function_00384420.md) at `0x00384B1D`
- [MiLockLowestPrioritySecondaryStandbyPage](../38/MiLockLowestPrioritySecondaryStandbyPage_function_00385A2C.md) at `0x00385C78`
- [MiSwapHardFaultPage](../38/MiSwapHardFaultPage_function_00385F34.md) at `0x003860C3`
- [ExpAcquireSpinLockDisabled](../38/ExpAcquireSpinLockDisabled_function_00386858.md) at `0x003868FA`
- [sub_0038BBFB](../38/Unknown_function_0038BBFB.md) at `0x0038BC87`
- [sub_00393045](../39/Unknown_function_00393045.md) at `0x00393074`
- [sub_003931B0](../39/Unknown_function_003931B0.md) at `0x003931DC`
- [KeAdjustWobPriority](../39/KeAdjustWobPriority_function_00393570.md) at `0x00393663`
- [KeApplyWobBamQos](../39/KeApplyWobBamQos_function_003937AC.md) at `0x003938DB`
- [sub_003954A1](../39/Unknown_function_003954A1.md) at `0x003954BE`
- [sub_003954C8](../39/Unknown_function_003954C8.md) at `0x003954F7`
- [AlpcpSignal](../39/AlpcpSignal_function_003955E0.md) at `0x00395C9E`
- [AlpcpSignal](../39/AlpcpSignal_function_003955E0.md) at `0x00395FC4`
- [AlpcpSignal](../39/AlpcpSignal_function_003955E0.md) at `0x0039606A`
- [KiAcquireThreadLockRaiseToDpc](../39/KiAcquireThreadLockRaiseToDpc_function_00396280.md) at `0x00396304`
- [KiClearPriorityFloor](../39/KiClearPriorityFloor_function_00396314.md) at `0x003964B5`
- [KiWakeOtherQueueWaiters](../39/KiWakeOtherQueueWaiters_function_003964D0.md) at `0x00396685`
- [KeReleaseMutantEx](../39/KeReleaseMutantEx_function_00396850.md) at `0x00396C51`
- [KeReleaseMutantEx](../39/KeReleaseMutantEx_function_00396850.md) at `0x00396C78`
- [KeReleaseMutantEx](../39/KeReleaseMutantEx_function_00396850.md) at `0x00396C9F`
- [KiReadyOutSwappedThreads](../39/KiReadyOutSwappedThreads_function_00396E30.md) at `0x00396FC1`
- [sub_00397301](../39/Unknown_function_00397301.md) at `0x0039731E`
- [sub_00397328](../39/Unknown_function_00397328.md) at `0x00397372`
- [AlpcpQueueIoCompletion](../39/AlpcpQueueIoCompletion_function_00397480.md) at `0x0039783D`
- [sub_00397C00](../39/Unknown_function_00397C00.md) at `0x00397C2C`
- [KiAlertSingleThreadByThreadId](../39/KiAlertSingleThreadByThreadId_function_00397D8C.md) at `0x00397F05`
- [KiRequestProcessInSwap](../39/KiRequestProcessInSwap_function_003981D4.md) at `0x00398271`
- [KiFastReadyThread](../39/KiFastReadyThread_function_00398548.md) at `0x00398629`
- [sub_00398A1B](../39/Unknown_function_00398A1B.md) at `0x00398A30`
- [KeRevertToUserGroupAffinityThread](../39/KeRevertToUserGroupAffinityThread_function_00398EC0.md) at `0x00399093`
- [sub_00399302](../39/Unknown_function_00399302.md) at `0x00399385`
- [KiSetSystemAffinityThread](../39/KiSetSystemAffinityThread_function_003993E0.md) at `0x0039960E`
- [KeClockInterruptNotify](../39/KeClockInterruptNotify_function_0039A970.md) at `0x0039AD62`
- [KiUpdateTime](../39/KiUpdateTime_function_0039B530.md) at `0x0039BA6E`
- [KiAcquireTimer2LockUnlessDisabled](../3A/KiAcquireTimer2LockUnlessDisabled_function_003A10D8.md) at `0x003A1138`
- [KiCheckAndRearmForceIdle](../3A/KiCheckAndRearmForceIdle_function_003A1C58.md) at `0x003A1D05`
- [KiIpiGenericCallTarget](../3A/KiIpiGenericCallTarget_function_003A4000.md) at `0x003A40B4`
- [MiGetLargePageDemoteAsNeeded](../3B/MiGetLargePageDemoteAsNeeded_function_003B8440.md) at `0x003B8720`
- [MiWaitForPageMoveComplete](../3B/MiWaitForPageMoveComplete_function_003B8C30.md) at `0x003B8CA3`
- [MiRebuildLargePage](../3B/MiRebuildLargePage_function_003BBAEC.md) at `0x003BBEE3`
- [MiAllocateEnclavePages](../3B/MiAllocateEnclavePages_function_003BC43C.md) at `0x003BC714`
- [MiUpdatePageThresholdsDpc](../3B/MiUpdatePageThresholdsDpc_function_003BD050.md) at `0x003BD16B`
- [MiUpdatePageThresholdsDpc](../3B/MiUpdatePageThresholdsDpc_function_003BD050.md) at `0x003BD258`
- [KiSetDisableBoostThread](../3C/KiSetDisableBoostThread_function_003C1A5C.md) at `0x003C1B33`
- [KeSetProcessPpmPolicy](../3C/KeSetProcessPpmPolicy_function_003C1CCC.md) at `0x003C1E78`
- [KeSetPriorityAndQuantumProcess](../3C/KeSetPriorityAndQuantumProcess_function_003C2EC0.md) at `0x003C3213`
- [KeSetPriorityAndQuantumProcess](../3C/KeSetPriorityAndQuantumProcess_function_003C2EC0.md) at `0x003C339E`
- [KeAdjustPriorityFloor](../3C/KeAdjustPriorityFloor_function_003C3574.md) at `0x003C3624`
- [KeSetActualBasePriorityThread](../3C/KeSetActualBasePriorityThread_function_003C4370.md) at `0x003C45BB`
- [KeWaitForAlertByThreadId](../3C/KeWaitForAlertByThreadId_function_003C4B14.md) at `0x003C4E52`
- [KeRemovePriQueue](../3C/KeRemovePriQueue_function_003C5090.md) at `0x003C53AE`
- [KeRemovePriQueue](../3C/KeRemovePriQueue_function_003C5090.md) at `0x003C53D5`
- [KeRemovePriQueue](../3C/KeRemovePriQueue_function_003C5090.md) at `0x003C5704`
- [KeRemovePriQueue](../3C/KeRemovePriQueue_function_003C5090.md) at `0x003C5753`
- [KiWaitForAllObjects](../3C/KiWaitForAllObjects_function_003C5800.md) at `0x003C5D48`
- [KiWaitForAllObjects](../3C/KiWaitForAllObjects_function_003C5800.md) at `0x003C5EDD`
- [KiSwitchPriQueue](../3C/KiSwitchPriQueue_function_003C6DC0.md) at `0x003C6E68`
- [KeSetBasePriorityThread](../3C/KeSetBasePriorityThread_function_003C6EB0.md) at `0x003C716F`
- [sub_003C763E](../3C/Unknown_function_003C763E.md) at `0x003C766C`
- [sub_003C7B1E](../3C/Unknown_function_003C7B1E.md) at `0x003C7B4C`
- [sub_003D36B4](../3D/Unknown_function_003D36B4.md) at `0x003D36D1`
- [KiCancelTimer](../3D/KiCancelTimer_function_003D3A80.md) at `0x003D3D76`
- [KiCancelTimer](../3D/KiCancelTimer_function_003D3A80.md) at `0x003D3E0F`
- [KiCancelTimer](../3D/KiCancelTimer_function_003D3A80.md) at `0x003D3E33`
- [KiCancelTimer](../3D/KiCancelTimer_function_003D3A80.md) at `0x003D3E5A`
- [KiCancelTimer](../3D/KiCancelTimer_function_003D3A80.md) at `0x003D3E81`
- [KiCancelTimer](../3D/KiCancelTimer_function_003D3A80.md) at `0x003D3EA8`
- [MiLockStandbyOldestPage](../3D/MiLockStandbyOldestPage_function_003D4EA4.md) at `0x003D50CC`
- [sub_003E67E6](../3E/Unknown_function_003E67E6.md) at `0x003E68FE`
- [MiFreeSecureKernelPage](../3E/MiFreeSecureKernelPage_function_003E9394.md) at `0x003E954F`
- [MiFreeSecureKernelPage](../3E/MiFreeSecureKernelPage_function_003E9394.md) at `0x003E956B`
- [MiAllocateContiguousMemory](../3E/MiAllocateContiguousMemory_function_003E9FDC.md) at `0x003EA5D3`
- [sub_003EC202](../3E/Unknown_function_003EC202.md) at `0x003EC272`
- [MiFreeContiguousPages](../3F/MiFreeContiguousPages_function_003F7178.md) at `0x003F73E6`
- [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) at `0x003FBD38`
- [AlpcpQueueIoCompletionPort](../3F/AlpcpQueueIoCompletionPort_function_003FF760.md) at `0x003FFD1D`
- [KiInsertPrcbWaitEntry](../40/KiInsertPrcbWaitEntry_function_004015D0.md) at `0x00401649`
- [sub_00401923](../40/Unknown_function_00401923.md) at `0x00401940`
- [sub_0040194A](../40/Unknown_function_0040194A.md) at `0x00401967`
- [sub_0040194A](../40/Unknown_function_0040194A.md) at `0x0040198A`
- [MiUpdatePrefetchPriority](../40/MiUpdatePrefetchPriority_function_00402CB0.md) at `0x00402FB1`
- [MiUpdatePrefetchPriority](../40/MiUpdatePrefetchPriority_function_00402CB0.md) at `0x00403047`
- [MiFlushSection](../40/MiFlushSection_function_004036B0.md) at `0x00403F71`
- [MiLockTransitionLeafPageEx](../40/MiLockTransitionLeafPageEx_function_00405884.md) at `0x00405B0C`
- [MiBuildMappedCluster](../40/MiBuildMappedCluster_function_00405F1C.md) at `0x0040670C`
- [MiBuildMappedCluster](../40/MiBuildMappedCluster_function_00405F1C.md) at `0x00406886`
- [sub_0040710D](../40/Unknown_function_0040710D.md) at `0x00407164`
- [MiBuildReservationCluster](../40/MiBuildReservationCluster_function_004071A0.md) at `0x00407906`
- [sub_004084AE](../40/Unknown_function_004084AE.md) at `0x004084CC`
- [NtLockVirtualMemory](../40/NtLockVirtualMemory_function_004088A0.md) at `0x004091A5`
- [MiLockNestedPageAtDpcInline](../40/MiLockNestedPageAtDpcInline_function_0040DCB0.md) at `0x0040DD00`
- [MiLockPageListAndLastPage](../41/MiLockPageListAndLastPage_function_00411BA0.md) at `0x00411DE9`
- [KxWaitForLockOwnerShipWithIrql](../41/KxWaitForLockOwnerShipWithIrql_function_00414E30.md) at `0x00414EEA`
- [KiAcquirePrcbLock](../41/KiAcquirePrcbLock_function_004168F0.md) at `0x00416941`
- [sub_0041881C](../41/Unknown_function_0041881C.md) at `0x00418839`
- [KeTestAlertThread](../41/KeTestAlertThread_function_0041C590.md) at `0x0041C692`
- [KeQueryBasePriorityThread](../41/KeQueryBasePriorityThread_function_0041E500.md) at `0x0041E667`
- [MiDecommitFreePagesTail](../41/MiDecommitFreePagesTail_function_0041ECE0.md) at `0x0041F04B`
- [MiDoubleUnlockMdlPage](../41/MiDoubleUnlockMdlPage_function_0041F43C.md) at `0x0041F4E6`
- [MiConvertLargeFreePageToActive](../42/MiConvertLargeFreePageToActive_function_00420974.md) at `0x00420AEA`
- [MiConvertActiveLargePageToSmall](../42/MiConvertActiveLargePageToSmall_function_00420AF8.md) at `0x00420C7D`
- [MiDeprioritizeVirtualAddresses](../42/MiDeprioritizeVirtualAddresses_function_0042AD1C.md) at `0x0042B013`
- [MiMakeOutswappedPageResident](../43/MiMakeOutswappedPageResident_function_00431AD0.md) at `0x00431EEE`
- [MiSpinForProtoPoolLock](../43/MiSpinForProtoPoolLock_function_00434540.md) at `0x004345D0`
- [sub_0043487C](../43/Unknown_function_0043487C.md) at `0x00434891`
- [MiInsertDemotedPages](../43/MiInsertDemotedPages_function_004354B8.md) at `0x004357E2`
- [sub_00435912](../43/Unknown_function_00435912.md) at `0x00435941`
- [sub_00439107](../43/Unknown_function_00439107.md) at `0x0043911C`
- [KeSignalCallDpcSynchronize](../43/KeSignalCallDpcSynchronize_function_0043DFA0.md) at `0x0043E03A`
- [ExpGetPoolTagInfoTarget](../44/ExpGetPoolTagInfoTarget_function_004407D0.md) at `0x0044087C`
- [ExpGetPoolTagInfoTarget](../44/ExpGetPoolTagInfoTarget_function_004407D0.md) at `0x004408DB`
- [MiLockNonPagedPoolPte](../44/MiLockNonPagedPoolPte_function_004450EC.md) at `0x004451A4`
- [sub_00445850](../44/Unknown_function_00445850.md) at `0x00445883`
- [MiDecayPfnFullyInitialized](../44/MiDecayPfnFullyInitialized_function_00447748.md) at `0x0044797D`
- [MiUpdateImportRelocationsOnDriverPrivatePages](../44/MiUpdateImportRelocationsOnDriverPrivatePages_function_00449BCC.md) at `0x00449E25`
- [MiDemoteSlabEntriesDpc](../44/MiDemoteSlabEntriesDpc_function_0044C3C0.md) at `0x0044C48D`
- [MiDemoteSlabEntriesDpc](../44/MiDemoteSlabEntriesDpc_function_0044C3C0.md) at `0x0044C4EE`
- [MiDemoteSlabEntry](../44/MiDemoteSlabEntry_function_0044CB0C.md) at `0x0044CD12`
- [MiUnlinkTransitionSlabPages](../44/MiUnlinkTransitionSlabPages_function_0044D140.md) at `0x0044D2BB`
- [MiUnlinkTransitionSlabPages](../44/MiUnlinkTransitionSlabPages_function_0044D140.md) at `0x0044D2F5`
- [MiDrainZeroLookasides](../44/MiDrainZeroLookasides_function_0044D818.md) at `0x0044DB6B`
- [KeInitializeMutantEx](../44/KeInitializeMutantEx_function_0044DBA4.md) at `0x0044DCAD`
- [KiSoftParkElectionDpcRoutine](../45/KiSoftParkElectionDpcRoutine_function_004508F0.md) at `0x00450A9E`
- [KiInitializeMutant](../45/KiInitializeMutant_function_00456E9C.md) at `0x00456FA5`
- [KiProcessScbTracingList](../45/KiProcessScbTracingList_function_0045A500.md) at `0x0045A5C5`
- [MiMirrorPerformBrownWrites](../45/MiMirrorPerformBrownWrites_function_0045C560.md) at `0x0045CD52`
- [MiMirrorPerformBrownWrites](../45/MiMirrorPerformBrownWrites_function_0045C560.md) at `0x0045CD7F`
- [MiCaptureProtectionFromLockedProto](../46/MiCaptureProtectionFromLockedProto_function_00460744.md) at `0x0046082D`
- [MiSetPfnOwnedAndActive](../46/MiSetPfnOwnedAndActive_function_004652AC.md) at `0x004653E3`
- [MiDeleteTopLevelPage](../46/MiDeleteTopLevelPage_function_00465E7C.md) at `0x00465F74`
- [MiCompleteSecureProcessFault](../46/MiCompleteSecureProcessFault_function_0046710C.md) at `0x0046736B`
- [MiCompleteSecureProcessFault](../46/MiCompleteSecureProcessFault_function_0046710C.md) at `0x0046739F`
- [KiAcquireReleaseThreadLock](../46/KiAcquireReleaseThreadLock_function_0046B658.md) at `0x0046B705`
- [KeInsertSchedulingGroup](../46/KeInsertSchedulingGroup_function_0046D324.md) at `0x0046D60E`
- [KiSetThreadSchedulingGroup](../46/KiSetThreadSchedulingGroup_function_0046E458.md) at `0x0046E577`
- [KiScanSharedReadyThreads](../46/KiScanSharedReadyThreads_function_0046F120.md) at `0x0046F4DD`
- [MiLockAndInsertPageInFreeList](../47/MiLockAndInsertPageInFreeList_function_00470FA8.md) at `0x00471074`
- [KeIpiGenericCall](../47/KeIpiGenericCall_function_00471720.md) at `0x004718AE`
- [IopLiveDumpProcessCorralStateChange](../47/IopLiveDumpProcessCorralStateChange_function_00471C7C.md) at `0x00471D16`
- [KeQuerySchedulingGroupReadyTime](../47/KeQuerySchedulingGroupReadyTime_function_0047A9E4.md) at `0x0047AADF`
- [MiLockPagedAddress](../48/MiLockPagedAddress_function_00484CDC.md) at `0x00484EC0`
- [KiSetSystemTimeDpc](../48/KiSetSystemTimeDpc_function_00486130.md) at `0x0048623D`
- [KiSetSystemTimeDpc](../48/KiSetSystemTimeDpc_function_00486130.md) at `0x0048631B`
- [KiSetSystemTimeDpc](../48/KiSetSystemTimeDpc_function_00486130.md) at `0x00486393`
- [KeAlertThread](../48/KeAlertThread_function_00489B40.md) at `0x00489C77`
- [MiRemoveSystemImagePage](../48/MiRemoveSystemImagePage_function_0048B398.md) at `0x0048B473`
- [MiJumpStackTarget](../48/MiJumpStackTarget_function_0048BC10.md) at `0x0048BCCB`
- [MiJumpStackTarget](../48/MiJumpStackTarget_function_0048BC10.md) at `0x0048BD20`
- [MiPurgeSlabEntry](../48/MiPurgeSlabEntry_function_0048D444.md) at `0x0048D599`
- [KeSetForceIdle](../48/KeSetForceIdle_function_0048D5A8.md) at `0x0048D62A`
- [KeClearForceIdle](../48/KeClearForceIdle_function_0048D69C.md) at `0x0048D70F`
- [KiForceIdleStopDpcRoutine](../48/KiForceIdleStopDpcRoutine_function_0048D7B0.md) at `0x0048D844`
- [MiMapPageFileHash](../49/MiMapPageFileHash_function_004921E0.md) at `0x00492698`
- [MmUpdateUserShadowStackValue](../49/MmUpdateUserShadowStackValue_function_004935D8.md) at `0x00493777`
- [MiDeleteShadowStackPtes](../49/MiDeleteShadowStackPtes_function_00493AE4.md) at `0x00493DAA`
- [KeQueryUserAffinityThread](../49/KeQueryUserAffinityThread_function_00496234.md) at `0x004962F3`
- [MiLockAndIncrementShareCount](../49/MiLockAndIncrementShareCount_function_0049BE04.md) at `0x0049BE97`
- [MiSetPagesModified](../49/MiSetPagesModified_function_0049DC2C.md) at `0x0049E05E`
- [MiSetPageTablePfnBuddy](../4A/MiSetPageTablePfnBuddy_function_004A3394.md) at `0x004A34B6`
- [MiWriteSharedDemandZeroPte](../4A/MiWriteSharedDemandZeroPte_function_004A8DDC.md) at `0x004A8EB4`
- [MiBuildForkPageTable](../4A/MiBuildForkPageTable_function_004ACF5C.md) at `0x004AD2EA`
- [MiBuildForkPageTable](../4A/MiBuildForkPageTable_function_004ACF5C.md) at `0x004AD307`
- [KeRemoveSchedulingGroup](../4A/KeRemoveSchedulingGroup_function_004AD328.md) at `0x004AD527`
- [KiAdaptThreadIdealProcessorForProcessIdealSetChange](../4A/KiAdaptThreadIdealProcessorForProcessIdealSetChange_function_004AF434.md) at `0x004AF5A8`
- [MiTrimSystemImagePages](../4B/MiTrimSystemImagePages_function_004B18FC.md) at `0x004B1B26`
- [MiTrimSystemImagePages](../4B/MiTrimSystemImagePages_function_004B18FC.md) at `0x004B1B3B`
- [KeTryToFreezeThreadStack](../4B/KeTryToFreezeThreadStack_function_004B5038.md) at `0x004B51FD`
- [MiInitializeLargeNonPagedPoolLeafFrames](../4B/MiInitializeLargeNonPagedPoolLeafFrames_function_004B7CE4.md) at `0x004B7DDE`
- [MiSwitchToTransition](../4C/MiSwitchToTransition_function_004C0F5C.md) at `0x004C1472`
- [MiWritePteHighLevelIsr](../4C/MiWritePteHighLevelIsr_function_004C2FC0.md) at `0x004C3220`
- [MiWritePteHighLevelIsr](../4C/MiWritePteHighLevelIsr_function_004C2FC0.md) at `0x004C32E1`
- [MiWritePteHighLevelIsr](../4C/MiWritePteHighLevelIsr_function_004C2FC0.md) at `0x004C33DA`
- [MiWritePteHighLevelIsr](../4C/MiWritePteHighLevelIsr_function_004C2FC0.md) at `0x004C3521`
- [MiWritePteHighLevelIsr](../4C/MiWritePteHighLevelIsr_function_004C2FC0.md) at `0x004C35E1`
- [MiWritePteHighLevelIsr](../4C/MiWritePteHighLevelIsr_function_004C2FC0.md) at `0x004C36C3`
- [KiForceIdleStartDpcRoutine](../4C/KiForceIdleStartDpcRoutine_function_004C3F40.md) at `0x004C3F7B`
- [KiProcessPendingForegroundBoosts](../4C/KiProcessPendingForegroundBoosts_function_004C5A80.md) at `0x004C5BAB`
- [MiZeroAndFlushGoodCitizen](../4D/MiZeroAndFlushGoodCitizen_function_004D0828.md) at `0x004D08A8`
- [KeSetSystemMultipleGroupAffinityThread](../4D/KeSetSystemMultipleGroupAffinityThread_function_004D0C88.md) at `0x004D0DD7`
- [KeBoostPriorityThread](../4D/KeBoostPriorityThread_function_004D37F8.md) at `0x004D3887`
- [MiFinishPageTableForLargePage](../4D/MiFinishPageTableForLargePage_function_004D3D4C.md) at `0x004D3DEE`
- [MiLockDownWorkingSet](../4D/MiLockDownWorkingSet_function_004D4950.md) at `0x004D4A00`
- [MiInitializeLargeUserBasePfn](../4F/MiInitializeLargeUserBasePfn_function_004F6268.md) at `0x004F62AF`
- [KiOptimizeSpecCtrlSettingsWorker](../5B/KiOptimizeSpecCtrlSettingsWorker_function_005BF5A0.md) at `0x005BF8D8`
- [KiOptimizeSpecCtrlSettingsWorker](../5B/KiOptimizeSpecCtrlSettingsWorker_function_005BF5A0.md) at `0x005BFD63`
- [KiOptimizeSpecCtrlSettingsWorker](../5B/KiOptimizeSpecCtrlSettingsWorker_function_005BF5A0.md) at `0x005C0307`
- [ExpLimitInsertDpc](../65/ExpLimitInsertDpc_function_00656BF0.md) at `0x00656D3D`
- [ExpLimitInsertDpc](../65/ExpLimitInsertDpc_function_00656BF0.md) at `0x00656E00`
- [ExpLimitInsertDpc](../65/ExpLimitInsertDpc_function_00656BF0.md) at `0x00656EDB`
- [ExpAeThresholdInitWorker](../65/ExpAeThresholdInitWorker_function_0065D680.md) at `0x0065D79B`
- [MiFreeUnusedPfnPagesDpc](../67/MiFreeUnusedPfnPagesDpc_function_00672150.md) at `0x0067224F`
- [MiFreeUnusedPfnPagesDpc](../67/MiFreeUnusedPfnPagesDpc_function_00672150.md) at `0x0067233C`
- [MiMakeIoRangePermanentDpc](../67/MiMakeIoRangePermanentDpc_function_0067C540.md) at `0x0067C648`
- [MiMakeIoRangePermanentDpc](../67/MiMakeIoRangePermanentDpc_function_0067C540.md) at `0x0067C735`
- [MiReapplyImportOptimizationWorker](../68/MiReapplyImportOptimizationWorker_function_00682720.md) at `0x006829CF`
- [MiDbgCopyMemoryTarget](../68/MiDbgCopyMemoryTarget_function_00684E70.md) at `0x0068506C`
- [MiDbgCopyMemoryTarget](../68/MiDbgCopyMemoryTarget_function_00684E70.md) at `0x00685159`
- [MiChangeSlabIdentitiesDpc](../68/MiChangeSlabIdentitiesDpc_function_0068CF10.md) at `0x0068D035`
- [MiChangeSlabIdentitiesDpc](../68/MiChangeSlabIdentitiesDpc_function_0068CF10.md) at `0x0068D122`
- [MiSpecialPurposeMemoryCacheUpdateDpc](../69/MiSpecialPurposeMemoryCacheUpdateDpc_function_00695240.md) at `0x0069539A`
- [MiSpecialPurposeMemoryCacheUpdateDpc](../69/MiSpecialPurposeMemoryCacheUpdateDpc_function_00695240.md) at `0x00695495`
- [MiDpcGangTarget](../69/MiDpcGangTarget_function_00697E60.md) at `0x00698032`
- [MiDpcGangTarget](../69/MiDpcGangTarget_function_00697E60.md) at `0x00698153`
- [SwapContext](../6B/SwapContext_function_006B9820.md) at `0x006B9EA1`
- [sub_006E2870](../6E/Unknown_function_006E2870.md) at `0x006E2932`
- [KiInitializeKernel](../../pagelk/B6/KiInitializeKernel_function_00B68D20.md) at `0x00B695CD`
- [PopIssueNextState](../../pagelk/B7/PopIssueNextState_function_00B772EC.md) at `0x00B77343`
- [PopHandleNextState](../../pagelk/B7/PopHandleNextState_function_00B77350.md) at `0x00B7740E`
- [MiInsertRegistryPageInModifiedList](../../init/C7/MiInsertRegistryPageInModifiedList_function_00C76010.md) at `0x00C7607F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0030F460  48 83 EC 28                     sub rsp, 0x28
0030F464  48 C7 44 24 38 08 00 00 00      mov qword ptr [rsp + 0x38], 8
0030F46D  45 33 C0                        xor r8d, r8d
0030F470  8B D1                           mov edx, ecx
0030F472  C7 44 24 38 08 00 01 00         mov dword ptr [rsp + 0x38], 0x10008
0030F47A  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0030F47F  E8 AC 41 00 00                  call 0x140313630
0030F484  48 83 C4 28                     add rsp, 0x28
0030F488  C3                              ret
0030F489  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlNotifyLongSpinWait(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_rsp = (v_rsp) - (40);
    v_stack_p10 = 8;
    a3 = 0;
    v_stack_p10 = 0x10008ULL;
    result = HvcallInitiateHypercall(v_stack_p10, (unsigned int)(a1), a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlNotifyLongSpinWait(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    local_rsp = (local_rsp) - (40);
    v_stack_p10 = 8;
    Arg3 = 0;
    v_stack_p10 = 0x10008ULL;
    result = HvcallInitiateHypercall(v_stack_p10, (uint32_t)(Arg1), Arg3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0030F460&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0030F460[BB_0030F460]
  bb_0030F489[BB_0030F489]
```
