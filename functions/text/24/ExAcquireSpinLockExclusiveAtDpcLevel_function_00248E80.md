# ExAcquireSpinLockExclusiveAtDpcLevel

- RVA: `0x00248E80`–`0x00248E92` (길이 `18` bytes)
- VA: `0x0000000140248E80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006261C`
- 디코드: `5`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **244**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KeThawMultiProcess](../20/KeThawMultiProcess_function_00202A04.md) at `0x00202A57`
- [sub_002219E9](../22/Unknown_function_002219E9.md) at `0x00221AAA`
- [sub_00221B4E](../22/Unknown_function_00221B4E.md) at `0x00221C31`
- [MiReplaceActivePageTableLinks](../22/MiReplaceActivePageTableLinks_function_00229B54.md) at `0x00229BC2`
- [MiLockWorkingSetOptimal](../23/MiLockWorkingSetOptimal_function_00238FC0.md) at `0x00239474`
- [MiLockWorkingSetExclusiveAtDpc](../23/MiLockWorkingSetExclusiveAtDpc_function_002395EC.md) at `0x0023960F`
- [MiLockWorkingSetExclusiveAtDpc](../23/MiLockWorkingSetExclusiveAtDpc_function_002395EC.md) at `0x00239620`
- [MiReferenceIoPages](../23/MiReferenceIoPages_function_0023C804.md) at `0x0023CB13`
- [sub_0023EC7F](../23/Unknown_function_0023EC7F.md) at `0x0023EC8D`
- [MiUnlockNestedPageTableWritePte](../23/MiUnlockNestedPageTableWritePte_function_0023F4E4.md) at `0x0023F717`
- [sub_00245F7B](Unknown_function_00245F7B.md) at `0x00245F7E`
- [sub_00245F85](Unknown_function_00245F85.md) at `0x00245F96`
- [sub_0024680E](Unknown_function_0024680E.md) at `0x00246813`
- [sub_00246856](Unknown_function_00246856.md) at `0x00246859`
- [sub_00246CF7](Unknown_function_00246CF7.md) at `0x00246CFA`
- [sub_00246D01](Unknown_function_00246D01.md) at `0x00246D12`
- [sub_00246F4D](Unknown_function_00246F4D.md) at `0x002470B1`
- [sub_002484B4](Unknown_function_002484B4.md) at `0x0024855B`
- [sub_002484B4](Unknown_function_002484B4.md) at `0x00248644`
- [sub_00248B10](Unknown_function_00248B10.md) at `0x00248B10`
- [sub_00248F71](Unknown_function_00248F71.md) at `0x00248FB1`
- [sub_002490EA](Unknown_function_002490EA.md) at `0x002490ED`
- [sub_0024926A](Unknown_function_0024926A.md) at `0x0024928B`
- [sub_00249C6B](Unknown_function_00249C6B.md) at `0x00249DE3`
- [MiAddPageToInsertList](MiAddPageToInsertList_function_0024A950.md) at `0x0024ADAE`
- [PopPepProcessEvent](PopPepProcessEvent_function_0024B930.md) at `0x0024C537`
- [MiActivateCombineBlock](../26/MiActivateCombineBlock_function_00266094.md) at `0x002660E6`
- [sub_0026F8B2](../26/Unknown_function_0026F8B2.md) at `0x0026F8EB`
- [sub_002760C1](../27/Unknown_function_002760C1.md) at `0x00276241`
- [MiFastLockLeafPageTable](../27/MiFastLockLeafPageTable_function_00276340.md) at `0x0027704B`
- [MiWalkPageTablesRecursively](../27/MiWalkPageTablesRecursively_function_002796C0.md) at `0x0027B6AC`
- [MiAddWorkingSetEntries](../27/MiAddWorkingSetEntries_function_0027DC00.md) at `0x0027E157`
- [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) at `0x00280BD0`
- [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) at `0x00280CB2`
- [MiLockLowestValidPageTableEx](../28/MiLockLowestValidPageTableEx_function_00280D10.md) at `0x002816C3`
- [MiLockLowestValidPageTableEx](../28/MiLockLowestValidPageTableEx_function_00280D10.md) at `0x00281781`
- [sub_002826A2](../28/Unknown_function_002826A2.md) at `0x002826ED`
- [sub_0028271E](../28/Unknown_function_0028271E.md) at `0x0028282A`
- [sub_00285DC9](../28/Unknown_function_00285DC9.md) at `0x00285E0F`
- [MiReturnCrossPartitionCharges](../28/MiReturnCrossPartitionCharges_function_002867D0.md) at `0x00286810`
- [MiChargeCommit](../28/MiChargeCommit_function_00286EB0.md) at `0x0028746E`
- [MiRemoveDecayClusterTimer](../28/MiRemoveDecayClusterTimer_function_00288178.md) at `0x0028818F`
- [MiGetPerfectColorHeadPage](../28/MiGetPerfectColorHeadPage_function_00289CA8.md) at `0x00289E8B`
- [MiCheckZeroFreeRebalance](../28/MiCheckZeroFreeRebalance_function_0028B1FC.md) at `0x0028B326`
- [MiClearPteAccessed](../29/MiClearPteAccessed_function_00290630.md) at `0x002909E0`
- [MiSetVaAgeList](../29/MiSetVaAgeList_function_00290A20.md) at `0x0029120A`
- [MiSetVaAgeList](../29/MiSetVaAgeList_function_00290A20.md) at `0x0029131D`
- [MiSetVaAgeList](../29/MiSetVaAgeList_function_00290A20.md) at `0x002915E6`
- [sub_00291C9C](../29/Unknown_function_00291C9C.md) at `0x00291CCB`
- [MiInsertActivePageTableLinksTail](../29/MiInsertActivePageTableLinksTail_function_00291D98.md) at `0x00291E8D`
- [MiRemoveActivePageTableLinks](../29/MiRemoveActivePageTableLinks_function_00291FA8.md) at `0x00291FEE`
- [sub_0029273F](../29/Unknown_function_0029273F.md) at `0x00292801`
- [MiUpdateSystemProtoPtesTree](../29/MiUpdateSystemProtoPtesTree_function_00295F0C.md) at `0x00295F5B`
- [MiFreePageToSlabEntry](../2A/MiFreePageToSlabEntry_function_002A0D94.md) at `0x002A0EE4`
- [MiOutPageSingleKernelStack](../2A/MiOutPageSingleKernelStack_function_002A1790.md) at `0x002A1909`
- [MiDereferenceControlAreaPfnList](../2A/MiDereferenceControlAreaPfnList_function_002A45E8.md) at `0x002A4645`
- [MiRemoveUnusedSubsection](../2A/MiRemoveUnusedSubsection_function_002A6194.md) at `0x002A61C0`
- [NtGetWriteWatch](../2A/NtGetWriteWatch_function_002A7CE0.md) at `0x002A8148`
- [MiMoveDirtyBitsToPfns](../2A/MiMoveDirtyBitsToPfns_function_002A8624.md) at `0x002A88D3`
- [MiDereferenceIoPages](../2A/MiDereferenceIoPages_function_002AB1B0.md) at `0x002AB3F7`
- [MiSectionCreated](../2A/MiSectionCreated_function_002ABA18.md) at `0x002ABA7E`
- [MiSectionCreated](../2A/MiSectionCreated_function_002ABA18.md) at `0x002ABA96`
- [MiSectionCreated](../2A/MiSectionCreated_function_002ABA18.md) at `0x002ABB2A`
- [MiLockIoPfnTree](../2A/MiLockIoPfnTree_function_002AC8A4.md) at `0x002AC951`
- [MiLockActivePageTableInList](../2A/MiLockActivePageTableInList_function_002AD86C.md) at `0x002AD899`
- [sub_002ADE82](../2A/Unknown_function_002ADE82.md) at `0x002ADE9C`
- [MiCopyDataPageToImagePage](../2A/MiCopyDataPageToImagePage_function_002AE818.md) at `0x002AE8BC`
- [MiCopyDataPageToImagePage](../2A/MiCopyDataPageToImagePage_function_002AE818.md) at `0x002AE8D0`
- [MiGetSlabRepurposedStandbyListWorker](../2A/MiGetSlabRepurposedStandbyListWorker_function_002AF534.md) at `0x002AF6A0`
- [MiReplaceTransitionPage](../2B/MiReplaceTransitionPage_function_002B1120.md) at `0x002B1A28`
- [MiCreateDecayPfn](../2B/MiCreateDecayPfn_function_002B8764.md) at `0x002B887F`
- [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) at `0x002BA6A8`
- [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) at `0x002BA6B1`
- [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) at `0x002BA9FF`
- [MiInsertDecayClusterTimer](../2B/MiInsertDecayClusterTimer_function_002BADF4.md) at `0x002BAE20`
- [MiSynchronizeFastPageInsert](../2B/MiSynchronizeFastPageInsert_function_002BAE80.md) at `0x002BB55E`
- [MiSynchronizeFastPageInsert](../2B/MiSynchronizeFastPageInsert_function_002BAE80.md) at `0x002BB5D0`
- [MiSynchronizeFastPageInsert](../2B/MiSynchronizeFastPageInsert_function_002BAE80.md) at `0x002BB611`
- [sub_002BBD57](../2B/Unknown_function_002BBD57.md) at `0x002BBD68`
- [MiRemoveUnusedSegment](../2B/MiRemoveUnusedSegment_function_002BBE74.md) at `0x002BBEA6`
- [MiLockSectionControlArea](../2B/MiLockSectionControlArea_function_002BC930.md) at `0x002BCAF3`
- [PopPepWork](../2B/PopPepWork_function_002BCBC0.md) at `0x002BD09A`
- [PopPepComponentSetLatency](../2B/PopPepComponentSetLatency_function_002BF3D8.md) at `0x002BF557`
- [MiWaitForPageWriteCompletion](../2C/MiWaitForPageWriteCompletion_function_002C9EBC.md) at `0x002C9F0D`
- [MiDeleteAcceleratorDescriptor](../2C/MiDeleteAcceleratorDescriptor_function_002CA560.md) at `0x002CA589`
- [MiReplenishUltraPageTables](../2C/MiReplenishUltraPageTables_function_002CB4EC.md) at `0x002CB62E`
- [MiReplenishUltraPageTables](../2C/MiReplenishUltraPageTables_function_002CB4EC.md) at `0x002CB638`
- [sub_002CBDF6](../2C/Unknown_function_002CBDF6.md) at `0x002CBE42`
- [KeSetUserAffinityThread](../2C/KeSetUserAffinityThread_function_002CFA2C.md) at `0x002CFA79`
- [KeUpdateSoftParkRankList](../2D/KeUpdateSoftParkRankList_function_002D5998.md) at `0x002D5B1C`
- [MiEmptyDecayClusterTimers](../2D/MiEmptyDecayClusterTimers_function_002DAB50.md) at `0x002DAC01`
- [MiEmptyDecayClusterTimers](../2D/MiEmptyDecayClusterTimers_function_002DAB50.md) at `0x002DACAE`
- [MiEmptyDecayClusterTimers](../2D/MiEmptyDecayClusterTimers_function_002DAB50.md) at `0x002DAE19`
- [MiSignalLargePageRebuild](../2D/MiSignalLargePageRebuild_function_002DB4C8.md) at `0x002DB542`
- [MiManageUltraSpacePageTable](../2D/MiManageUltraSpacePageTable_function_002DCAF0.md) at `0x002DCC48`
- [MmReportParkedProcessors](../30/MmReportParkedProcessors_function_00305600.md) at `0x0030560D`
- [MiMoveBackgroundZeroThreads](../30/MiMoveBackgroundZeroThreads_function_00305810.md) at `0x003058B4`
- [KiSoftParkElectionUnparkProcessor](../30/KiSoftParkElectionUnparkProcessor_function_0030B818.md) at `0x0030BD1F`
- [VmpProcessContextLockExclusive](../31/VmpProcessContextLockExclusive_function_003147A4.md) at `0x003147CA`
- [MiReplenishCombineResources](../31/MiReplenishCombineResources_function_00316140.md) at `0x00316241`
- [sub_0031CD16](../31/Unknown_function_0031CD16.md) at `0x0031CD7E`
- [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) at `0x00322B5B`
- [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) at `0x00322C3B`
- [MiRewritePteWithLockBit](../32/MiRewritePteWithLockBit_function_00322FEC.md) at `0x00323160`
- [MiRewritePteWithLockBit](../32/MiRewritePteWithLockBit_function_00322FEC.md) at `0x003231E5`
- [MiReferenceActiveSubsection](../32/MiReferenceActiveSubsection_function_00325060.md) at `0x0032511E`
- [MiGetCrossPartitionCharges](../32/MiGetCrossPartitionCharges_function_00325BFC.md) at `0x00325C40`
- [MiReturnPhysicalPoolPages](../32/MiReturnPhysicalPoolPages_function_00328568.md) at `0x00328828`
- [MiAllocateWsle](../33/MiAllocateWsle_function_003332C0.md) at `0x00333CC1`
- [sub_003354FB](../33/Unknown_function_003354FB.md) at `0x00335C0A`
- [sub_00336094](../33/Unknown_function_00336094.md) at `0x003360D9`
- [sub_00336094](../33/Unknown_function_00336094.md) at `0x003361BF`
- [sub_0033C441](../33/Unknown_function_0033C441.md) at `0x0033C65E`
- [MiDecayNodeNowEmpty](../33/MiDecayNodeNowEmpty_function_0033C938.md) at `0x0033C9A8`
- [sub_0033E839](../33/Unknown_function_0033E839.md) at `0x0033E8D5`
- [sub_0033EABD](../33/Unknown_function_0033EABD.md) at `0x0033ED60`
- [sub_0033EABD](../33/Unknown_function_0033EABD.md) at `0x0033EDCC`
- [sub_0033EABD](../33/Unknown_function_0033EABD.md) at `0x0033EE06`
- [sub_0033EABD](../33/Unknown_function_0033EABD.md) at `0x0033EEF6`
- [KiAcquireReleaseObjectRundownLockExclusive](../35/KiAcquireReleaseObjectRundownLockExclusive_function_00351A0C.md) at `0x00351A2D`
- [KeTransitionProcessorParkState](../35/KeTransitionProcessorParkState_function_003527EC.md) at `0x00352840`
- [sub_003532A7](../35/Unknown_function_003532A7.md) at `0x003532B1`
- [KeTerminateThread](../35/KeTerminateThread_function_00355138.md) at `0x003551A4`
- [MiReferenceControlAreaPfn](../36/MiReferenceControlAreaPfn_function_00364084.md) at `0x003640B5`
- [MiCopyFileOnlyGlobalSubsectionPage](../36/MiCopyFileOnlyGlobalSubsectionPage_function_0036A9EC.md) at `0x0036AB57`
- [sub_00371C01](../37/Unknown_function_00371C01.md) at `0x00371C88`
- [sub_00371E3A](../37/Unknown_function_00371E3A.md) at `0x00371E7F`
- [MiFreeCombineBlock](../37/MiFreeCombineBlock_function_00372000.md) at `0x0037207A`
- [MiFreeCombineBlock](../37/MiFreeCombineBlock_function_00372000.md) at `0x0037209E`
- [MiLockPageListAndFirstPage](../37/MiLockPageListAndFirstPage_function_0037573C.md) at `0x0037583E`
- [MiUpdateLargePageBitMap](../37/MiUpdateLargePageBitMap_function_0037619C.md) at `0x00376336`
- [MiInsertSlabEntry](../37/MiInsertSlabEntry_function_00378AF4.md) at `0x00378C78`
- [MiUpdateSlabTypeAvailablePages](../37/MiUpdateSlabTypeAvailablePages_function_00378DC0.md) at `0x00378E4B`
- [MiReferencePageRuns](../37/MiReferencePageRuns_function_00379540.md) at `0x003795F9`
- [MiReferencePageRuns](../37/MiReferencePageRuns_function_00379540.md) at `0x0037960A`
- [MiWritePageFileHash](../38/MiWritePageFileHash_function_00381DC8.md) at `0x00382007`
- [MiSwapNumaStandbyPage](../38/MiSwapNumaStandbyPage_function_00385144.md) at `0x00385753`
- [MiLockLowestPrioritySecondaryStandbyPage](../38/MiLockLowestPrioritySecondaryStandbyPage_function_00385A2C.md) at `0x00385B0C`
- [MiLockLowestPrioritySecondaryStandbyPage](../38/MiLockLowestPrioritySecondaryStandbyPage_function_00385A2C.md) at `0x00385B6C`
- [MmGetControlAreaPartition](../38/MmGetControlAreaPartition_function_0038B80C.md) at `0x0038B872`
- [MiMarkSystemVaAllocated](../3B/MiMarkSystemVaAllocated_function_003B3878.md) at `0x003B3909`
- [MiExpandSystemCache](../3B/MiExpandSystemCache_function_003B3DC8.md) at `0x003B3EAD`
- [MiExpandPtes](../3B/MiExpandPtes_function_003B4B78.md) at `0x003B4E76`
- [MiExpandPtes](../3B/MiExpandPtes_function_003B4B78.md) at `0x003B4F32`
- [MiObtainDynamicVa](../3B/MiObtainDynamicVa_function_003B501C.md) at `0x003B5466`
- [MiWalkPagesOnLists](../3B/MiWalkPagesOnLists_function_003B6AA4.md) at `0x003B6B24`
- [MiWalkPagesOnLists](../3B/MiWalkPagesOnLists_function_003B6AA4.md) at `0x003B6C37`
- [MiWalkPagesOnLists](../3B/MiWalkPagesOnLists_function_003B6AA4.md) at `0x003B6D89`
- [MiWakeLargePageRebuild](../3B/MiWakeLargePageRebuild_function_003BA2C8.md) at `0x003BA33F`
- [MiRebuildLargePages](../3B/MiRebuildLargePages_function_003BA700.md) at `0x003BA770`
- [MiRebuildLargePages](../3B/MiRebuildLargePages_function_003BA700.md) at `0x003BAA0F`
- [MiSlabDemotionLowMemoryConditionUpdate](../3B/MiSlabDemotionLowMemoryConditionUpdate_function_003BB7E0.md) at `0x003BB802`
- [MiAllocateEnclavePages](../3B/MiAllocateEnclavePages_function_003BC43C.md) at `0x003BC525`
- [MiAllocateEnclavePages](../3B/MiAllocateEnclavePages_function_003BC43C.md) at `0x003BC576`
- [MiUpdateAvailableEventsAtDpc](../3B/MiUpdateAvailableEventsAtDpc_function_003BC804.md) at `0x003BC820`
- [sub_003BCD6B](../3B/Unknown_function_003BCD6B.md) at `0x003BCD7C`
- [sub_003BCDBD](../3B/Unknown_function_003BCDBD.md) at `0x003BCDC2`
- [MiDereferencePageRuns](../3B/MiDereferencePageRuns_function_003BD388.md) at `0x003BD417`
- [MiFreeListPageContentsChanged](../3B/MiFreeListPageContentsChanged_function_003BD4BC.md) at `0x003BD53A`
- [KeSetAffinityProcess](../3C/KeSetAffinityProcess_function_003C0A60.md) at `0x003C0B48`
- [KeSetDisableBoostProcess](../3C/KeSetDisableBoostProcess_function_003C18B4.md) at `0x003C18F8`
- [KeForceResumeProcess](../3C/KeForceResumeProcess_function_003C1BE4.md) at `0x003C1C2A`
- [KiAcquireProcessLockExclusive](../3C/KiAcquireProcessLockExclusive_function_003C26B8.md) at `0x003C26E9`
- [KeSetPriorityAndQuantumProcess](../3C/KeSetPriorityAndQuantumProcess_function_003C2EC0.md) at `0x003C2F6F`
- [MiCheckAndUpdateIoAttribution](../3C/MiCheckAndUpdateIoAttribution_function_003CB3C4.md) at `0x003CB455`
- [MiLockStandbyOldestPage](../3D/MiLockStandbyOldestPage_function_003D4EA4.md) at `0x003D4F69`
- [MiRepurposeDecayNode](../3D/MiRepurposeDecayNode_function_003D5774.md) at `0x003D57EA`
- [MiFindFreePageFileSpace](../3E/MiFindFreePageFileSpace_function_003E2CAC.md) at `0x003E2F7B`
- [MiUnmapMdlCommon](../3E/MiUnmapMdlCommon_function_003E7DF0.md) at `0x003E8238`
- [ViAvlAcquireTableLockAtDpcLevel](../3E/ViAvlAcquireTableLockAtDpcLevel_function_003EF7D4.md) at `0x003EF829`
- [MiGatherMappedPages](../40/MiGatherMappedPages_function_00404E80.md) at `0x00404F79`
- [MiReleaseWriteInProgressCharges](../40/MiReleaseWriteInProgressCharges_function_00407B4C.md) at `0x00407CFD`
- [sub_004084EC](../40/Unknown_function_004084EC.md) at `0x00408532`
- [VmpFaultEntryInsert](../42/VmpFaultEntryInsert_function_00429558.md) at `0x004295A5`
- [VmpFaultEntryRemove](../42/VmpFaultEntryRemove_function_0042969C.md) at `0x004296E3`
- [MmLockLoadedModuleListExclusive](../43/MmLockLoadedModuleListExclusive_function_0043229C.md) at `0x004322CC`
- [MiInsertHugeRangeInList](../43/MiInsertHugeRangeInList_function_004371E8.md) at `0x00437313`
- [MiUpdateCommitCounts](../43/MiUpdateCommitCounts_function_0043D9CC.md) at `0x0043DA95`
- [MiInsertUnusedSegment](../44/MiInsertUnusedSegment_function_004443DC.md) at `0x00444423`
- [MiDemoteSlabEntry](../44/MiDemoteSlabEntry_function_0044CB0C.md) at `0x0044CB49`
- [KiSoftParkElectionDpcRoutine](../45/KiSoftParkElectionDpcRoutine_function_004508F0.md) at `0x00450951`
- [MiInitializeSystemPageTable](../45/MiInitializeSystemPageTable_function_00451C88.md) at `0x00452082`
- [MmUpdateMdlTracker](../45/MmUpdateMdlTracker_function_00456468.md) at `0x004564C1`
- [MiClearFilePointer](../46/MiClearFilePointer_function_00463044.md) at `0x0046306C`
- [MiDeleteProcessShadow](../46/MiDeleteProcessShadow_function_00465BF8.md) at `0x00465CA1`
- [KeFreezeProcess](../46/KeFreezeProcess_function_0046B774.md) at `0x0046B7C1`
- [MiLogStandbyRepurpose](../46/MiLogStandbyRepurpose_function_0046BD14.md) at `0x0046BD6D`
- [KeSetProcessSchedulingGroup](../46/KeSetProcessSchedulingGroup_function_0046E378.md) at `0x0046E3B9`
- [MiFaultGetFileExtents](../47/MiFaultGetFileExtents_function_00479758.md) at `0x004797D2`
- [MiRetainSubsection](../47/MiRetainSubsection_function_00479864.md) at `0x0047987D`
- [MiSyncCommitSignals](../47/MiSyncCommitSignals_function_0047CA00.md) at `0x0047CAC3`
- [MmAdjustWorkingSetSizeEx](../47/MmAdjustWorkingSetSizeEx_function_0047D8D4.md) at `0x0047DC4B`
- [MiLockAllMemoryLists](../47/MiLockAllMemoryLists_function_0047FBD8.md) at `0x0047FBF4`
- [MiLockAllMemoryLists](../47/MiLockAllMemoryLists_function_0047FBD8.md) at `0x0047FC00`
- [MiQueuePageFileExtension](../48/MiQueuePageFileExtension_function_0048187C.md) at `0x0048193F`
- [MmEnforceWorkingSetLimit](../48/MmEnforceWorkingSetLimit_function_004881E0.md) at `0x00488276`
- [MiAllocatePfnRepurposeLogDispatch](../48/MiAllocatePfnRepurposeLogDispatch_function_00488BD0.md) at `0x00488C47`
- [MiMapPageFileHash](../49/MiMapPageFileHash_function_004921E0.md) at `0x004923C0`
- [MiMapPageFileHash](../49/MiMapPageFileHash_function_004921E0.md) at `0x00492436`
- [MiMapPageFileHash](../49/MiMapPageFileHash_function_004921E0.md) at `0x004925AC`
- [MiPerformSafePdeWrite](../49/MiPerformSafePdeWrite_function_00494300.md) at `0x004943DA`
- [MiFreeMdlTracker](../49/MiFreeMdlTracker_function_00494838.md) at `0x0049488C`
- [MiAddMdlTracker](../49/MiAddMdlTracker_function_0049A240.md) at `0x0049A399`
- [VslIumEfiRuntimeService](../49/VslIumEfiRuntimeService_function_0049C0C0.md) at `0x0049C153`
- [MiGetCachedPoolPages](../4A/MiGetCachedPoolPages_function_004A9324.md) at `0x004A9362`
- [MiZeroSectionObjectPointer](../4A/MiZeroSectionObjectPointer_function_004A9B90.md) at `0x004A9BE0`
- [MiAsyncSlabReplenish](../4A/MiAsyncSlabReplenish_function_004AA54C.md) at `0x004AA5CE`
- [MiAsyncSlabReplenish](../4A/MiAsyncSlabReplenish_function_004AA54C.md) at `0x004AA6B3`
- [MiConsumeOverCommit](../4B/MiConsumeOverCommit_function_004B3E0C.md) at `0x004B3E44`
- [MiFlowThroughInsertNode](../4B/MiFlowThroughInsertNode_function_004B560C.md) at `0x004B56AD`
- [MiFreeHardwareDescriptor](../4B/MiFreeHardwareDescriptor_function_004B6078.md) at `0x004B6125`
- [MiAllocateHardwareDescriptor](../4B/MiAllocateHardwareDescriptor_function_004B8738.md) at `0x004B87EE`
- [MiLockMemoryLists](../4B/MiLockMemoryLists_function_004BB470.md) at `0x004BB4A1`
- [MiLockMemoryLists](../4B/MiLockMemoryLists_function_004BB470.md) at `0x004BB4D3`
- [MiLockMemoryLists](../4B/MiLockMemoryLists_function_004BB470.md) at `0x004BB4F5`
- [MiLockMemoryLists](../4B/MiLockMemoryLists_function_004BB470.md) at `0x004BB501`
- [MiLockMemoryLists](../4B/MiLockMemoryLists_function_004BB470.md) at `0x004BB530`
- [MiLockMemoryLists](../4B/MiLockMemoryLists_function_004BB470.md) at `0x004BB555`
- [MiLockMemoryLists](../4B/MiLockMemoryLists_function_004BB470.md) at `0x004BB623`
- [MiLockMemoryLists](../4B/MiLockMemoryLists_function_004BB470.md) at `0x004BB655`
- [MiLockSlabAllocator](../4B/MiLockSlabAllocator_function_004BB6A0.md) at `0x004BB6AD`
- [MiLockMemoryListsCallback](../4B/MiLockMemoryListsCallback_function_004BE790.md) at `0x004BE7B6`
- [MiMapMdlWithLargePages](../4D/MiMapMdlWithLargePages_function_004D10B8.md) at `0x004D14E3`
- [MiQueueExtentPfnDeletion](../4D/MiQueueExtentPfnDeletion_function_004D1C80.md) at `0x004D1C95`
- [MiLateWritePageHash](../4D/MiLateWritePageHash_function_004D4148.md) at `0x004D417E`
- [MiRemovePteTracker](../4D/MiRemovePteTracker_function_004D8200.md) at `0x004D8254`
- [MiBadPageInserted](../4D/MiBadPageInserted_function_004DD9A0.md) at `0x004DD9BC`
- [MiPulseCommitSignal](../4D/MiPulseCommitSignal_function_004DEFF4.md) at `0x004DF01B`
- [MiMakeSystemRangeAvailable](../4E/MiMakeSystemRangeAvailable_function_004EE174.md) at `0x004EE216`
- [MiReplicatePteChange](../4F/MiReplicatePteChange_function_004F8A24.md) at `0x004F8A67`
- [MiFreeModifiedReservations](../4F/MiFreeModifiedReservations_function_004FA318.md) at `0x004FA3B9`
- [MiFreeUltraMapping](../4F/MiFreeUltraMapping_function_004FAFD4.md) at `0x004FAFFE`
- [MiRemoveFaultNode](../4F/MiRemoveFaultNode_function_004FC440.md) at `0x004FC4A8`
- [HalpIommuCreateDevice](../54/HalpIommuCreateDevice_function_0054ED60.md) at `0x0054EE27`
- [HalpIommuCreateDevice](../54/HalpIommuCreateDevice_function_0054ED60.md) at `0x0054F26C`
- [HalpIommuDeleteDevice](../54/HalpIommuDeleteDevice_function_0054F368.md) at `0x0054F3E3`
- [DbgpInsertDebugPrintCallback](../5E/DbgpInsertDebugPrintCallback_function_005E5908.md) at `0x005E596B`
- [DbgpRemoveDebugPrintCallback](../5E/DbgpRemoveDebugPrintCallback_function_005E59E4.md) at `0x005E5A7B`
- [RtlpAcquirePropStoreLockExclusive](../5E/RtlpAcquirePropStoreLockExclusive_function_005E84C4.md) at `0x005E84F1`
- [ViPtAcquireTreeLockAtDpcLevelSafe](../61/ViPtAcquireTreeLockAtDpcLevelSafe_function_0061388C.md) at `0x006138CB`
- [CarAcquireDbLockAtDpcLevelSafe](../61/CarAcquireDbLockAtDpcLevelSafe_function_0061B00C.md) at `0x0061B051`
- [DifAcquireSpinLockAtDpcLevelSafe](../61/DifAcquireSpinLockAtDpcLevelSafe_function_0061BDF4.md) at `0x0061BE73`
- [MiFreedUnusedPfnPagesDpc](../67/MiFreedUnusedPfnPagesDpc_function_00672378.md) at `0x006723AB`
- [MiPerformMemoryChange](../67/MiPerformMemoryChange_function_006733A8.md) at `0x00673432`
- [MmUpdateMdlTrackerForMdlSwitch](../67/MmUpdateMdlTrackerForMdlSwitch_function_00674298.md) at `0x00674300`
- [MiGetHugeBadRangeFromNode](../67/MiGetHugeBadRangeFromNode_function_00675818.md) at `0x00675904`
- [MiMakeEntireHugePfnGood](../67/MiMakeEntireHugePfnGood_function_00676644.md) at `0x0067669A`
- [MiMarkHugePfnBad](../67/MiMarkHugePfnBad_function_00676744.md) at `0x00676927`
- [MiMarkHugePfnBad](../67/MiMarkHugePfnBad_function_00676744.md) at `0x0067698E`
- [MiMarkHugePfnGood](../67/MiMarkHugePfnGood_function_00676BB0.md) at `0x00676C4E`
- [MiMoveBadHugeRangeCrossPartition](../67/MiMoveBadHugeRangeCrossPartition_function_00676DD0.md) at `0x00676E53`
- [MiInsertUnusedSubsectionInternal](../67/MiInsertUnusedSubsectionInternal_function_00677EDC.md) at `0x00677F75`
- [MiAddPendingBadPageNode](../67/MiAddPendingBadPageNode_function_006793B4.md) at `0x006793DB`
- [MiRemovePendingBadPageNode](../67/MiRemovePendingBadPageNode_function_0067A0DC.md) at `0x0067A0F0`
- [MiFreezeIoPfnNode](../67/MiFreezeIoPfnNode_function_0067BDAC.md) at `0x0067BE6C`
- [MiMarkHugeRangeIoPfnDeleted](../67/MiMarkHugeRangeIoPfnDeleted_function_0067C770.md) at `0x0067C7F7`
- [MiInitializeNonPagedPoolThresholds](../67/MiInitializeNonPagedPoolThresholds_function_0067CA64.md) at `0x0067CA77`
- [MiChangePagingFileMaximum](../67/MiChangePagingFileMaximum_function_0067FEFC.md) at `0x006801FA`
- [MiUpdatePageFileList](../68/MiUpdatePageFileList_function_006803AC.md) at `0x006803ED`
- [MiMarkFileOnlyPfnGood](../68/MiMarkFileOnlyPfnGood_function_0068178C.md) at `0x006817D5`
- [MiPurgeBadFileOnlyPages](../68/MiPurgeBadFileOnlyPages_function_00681ADC.md) at `0x00681B17`
- [MiResolveAwePageConflict](../68/MiResolveAwePageConflict_function_00689758.md) at `0x006897B8`
- [MiWakeWaitersForAweCacheAttributeChange](../68/MiWakeWaitersForAweCacheAttributeChange_function_00689A58.md) at `0x00689AA2`
- [MiNoPagesLastChance](../68/MiNoPagesLastChance_function_0068B22C.md) at `0x0068B482`
- [MiNoPagesLastChance](../68/MiNoPagesLastChance_function_0068B22C.md) at `0x0068B515`
- [MiNoPagesLastChance](../68/MiNoPagesLastChance_function_0068B22C.md) at `0x0068B69F`
- [MiDeleteSlabEntriesForIdentity](../68/MiDeleteSlabEntriesForIdentity_function_0068DE10.md) at `0x0068DE70`
- [MiDeleteSlabEntriesForIdentity](../68/MiDeleteSlabEntriesForIdentity_function_0068DE10.md) at `0x0068DF5D`
- [MiLockSlabRepurposedStandbyList](../68/MiLockSlabRepurposedStandbyList_function_0068ED78.md) at `0x0068ED89`
- [MiDrainCrossPartitionUsage](../69/MiDrainCrossPartitionUsage_function_00690984.md) at `0x006909D5`
- [MiTransferPartitionPageRun](../69/MiTransferPartitionPageRun_function_00691DCC.md) at `0x00691E36`
- [MiTransferPartitionPageRun](../69/MiTransferPartitionPageRun_function_00691DCC.md) at `0x00691E86`
- [MiAllocateAcceleratorDescriptor](../69/MiAllocateAcceleratorDescriptor_function_00697124.md) at `0x0069716B`
- [MiAllocateAcceleratorDescriptor](../69/MiAllocateAcceleratorDescriptor_function_00697124.md) at `0x006971CF`
- [MiSignalNewAcceleratorsAvailable](../69/MiSignalNewAcceleratorsAvailable_function_006974E4.md) at `0x006975B3`
- [MiUnlinkAccelerator](../69/MiUnlinkAccelerator_function_00697860.md) at `0x006978BF`
- [MiInsertPteTracker](../69/MiInsertPteTracker_function_00697BE4.md) at `0x00697DB8`
- [MiCreateProcessLargePageCacheAnchor](../69/MiCreateProcessLargePageCacheAnchor_function_00698A44.md) at `0x00698AE6`
- [MiFreeProcessLargePageCache](../69/MiFreeProcessLargePageCache_function_00699204.md) at `0x006992C0`
- [sub_006D7254](../6D/Unknown_function_006D7254.md) at `0x006D7262`
- [sub_006DB2D0](../6D/Unknown_function_006DB2D0.md) at `0x006DB2E4`
- [sub_006DB59E](../6D/Unknown_function_006DB59E.md) at `0x006DB5BA`
- [sub_006DBBC0](../6D/Unknown_function_006DBBC0.md) at `0x006DBC94`
- [sub_006DBBC0](../6D/Unknown_function_006DBBC0.md) at `0x006DBCBF`
- [sub_006DBBC0](../6D/Unknown_function_006DBBC0.md) at `0x006DBD14`
- [sub_006DC9A8](../6D/Unknown_function_006DC9A8.md) at `0x006DC9BA`
- [sub_006E362E](../6E/Unknown_function_006E362E.md) at `0x006E3929`
- [sub_006EF650](../6E/Unknown_function_006EF650.md) at `0x006EF653`
- [sub_006F28BE](../6F/Unknown_function_006F28BE.md) at `0x006F29CC`
- [sub_006F2D78](../6F/Unknown_function_006F2D78.md) at `0x006F2DB7`
- [sub_006F3CFE](../6F/Unknown_function_006F3CFE.md) at `0x006F3D01`
- [sub_006F9120](../6F/Unknown_function_006F9120.md) at `0x006F919C`
- [sub_006FBD3C](../6F/Unknown_function_006FBD3C.md) at `0x006FBD43`
- [ViDeadlockDetectionLock](../../pagevrfy/BA/ViDeadlockDetectionLock_function_00BA91C4.md) at `0x00BA91DA`

### Static image references
- `0x00248E86` → RVA `0x00FC6B06` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00248E90` → [sub_00248EEC + 0x1](Unknown_function_00248EEC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00248E80  40 53                           push rbx
00248E82  48 83 EC 20                     sub rsp, 0x20
00248E86  F6 05 79 DC D7 00 21            test byte ptr [rip + 0xd7dc79], 0x21
00248E8D  48 8B D9                        mov rbx, rcx
00248E90  75 5B                           jne 0x140248eed
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall ExAcquireSpinLockExclusiveAtDpcLevel(__int64 a1)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
}
```

## 5. (Beta) C Style

```c
void ExAcquireSpinLockExclusiveAtDpcLevel(int64_t Arg1)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00248E80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00248E80[BB_00248E80]
```
