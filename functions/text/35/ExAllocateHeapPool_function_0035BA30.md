# ExAllocateHeapPool

- RVA: `0x0035BA30`–`0x0035F4DB` (길이 `15,019` bytes)
- VA: `0x000000014035BA30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00079B68`
- 디코드: `3,546`개 명령, `15,019/15,019` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **152**; 고유 호출 대상: **62**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **44**

### Outgoing calls
- `0x0035BC01` → [RtlCSparseBitmapBitmaskRead](../36/RtlCSparseBitmapBitmaskRead_function_0036190C.md) (function, `0x0036190C`)
- `0x0035BE82` → [RtlpLogHeapFailure](RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x0035BF1A` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035BF83` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035BFDD` → [RtlpHpVsContextFree](../36/RtlpHpVsContextFree_function_00361630.md) (function, `0x00361630`)
- `0x0035C07A` → [RtlpHpLargeFree](../2E/RtlpHpLargeFree_function_002EC89C.md) (function, `0x002EC89C`)
- `0x0035C0BC` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035C0C8` → [RtlpHpSegPageRangeShrink](../2E/RtlpHpSegPageRangeShrink_function_002E2FA0.md) (function, `0x002E2FA0`)
- `0x0035C0EA` → [RtlpLogHeapFailure](RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x0035C123` → [RtlpHpAllocateHeapBackend](../32/RtlpHpAllocateHeapBackend_function_00326580.md) (function, `0x00326580`)
- `0x0035C158` → [ExpAddTagForBigPages](../2E/ExpAddTagForBigPages_function_002EF570.md) (function, `0x002EF570`)
- `0x0035C43D` → [RtlpHpLfhSubsegmentCommitBlock](../2E/RtlpHpLfhSubsegmentCommitBlock_function_002EA630.md) (function, `0x002EA630`)
- `0x0035C46A` → [RtlHeapZero](../6B/RtlHeapZero_function_006BBC10.md) (function, `0x006BBC10`)
- `0x0035C4A2` → [RtlpHpLfhBucketUpdateAffinityMapping](../4D/RtlpHpLfhBucketUpdateAffinityMapping_function_004D0008.md) (function, `0x004D0008`)
- `0x0035C4DA` → [RtlpHpEnvCompactionSchedule](../32/RtlpHpEnvCompactionSchedule_function_003264A0.md) (function, `0x003264A0`)
- `0x0035C75B` → [RtlpHpLfhSubsegmentCommitBlock](../2E/RtlpHpLfhSubsegmentCommitBlock_function_002EA630.md) (function, `0x002EA630`)
- `0x0035C782` → [RtlHeapZero](../6B/RtlHeapZero_function_006BBC10.md) (function, `0x006BBC10`)
- `0x0035C8F1` → [VfPtFreePoolNotification](../../pagevrfy/BB/VfPtFreePoolNotification_function_00BB96DC.md) (function, `0x00BB96DC`)
- `0x0035CA85` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0035CAA4` → [ViFreeTrackedPool](../../pagevrfy/BB/ViFreeTrackedPool_function_00BB8FC0.md) (function, `0x00BB8FC0`)
- `0x0035CAFF` → [RtlCSparseBitmapBitmaskRead](../36/RtlCSparseBitmapBitmaskRead_function_0036190C.md) (function, `0x0036190C`)
- `0x0035CB5E` → [RtlpLogHeapFailure](RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x0035CB73` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x0035CEC2` → [ExpAcquireSpinLockSharedAtDpcLevelInstrumented](../27/ExpAcquireSpinLockSharedAtDpcLevelInstrumented_function_0027CD20.md) (function, `0x0027CD20`)
- `0x0035CF33` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035D11A` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x0035D1DD` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0035D257` → [RtlpHpVsContextFree](../36/RtlpHpVsContextFree_function_00361630.md) (function, `0x00361630`)
- `0x0035D2ED` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x0035D33B` → [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x0035D34C` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0035D363` → [RtlpHpSegPageRangeShrink](../2E/RtlpHpSegPageRangeShrink_function_002E2FA0.md) (function, `0x002E2FA0`)
- `0x0035D385` → [RtlpLogHeapFailure](RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x0035D3E1` → [RtlpHpEnvCompactionIsScheduled](../48/RtlpHpEnvCompactionIsScheduled_function_0048E7E0.md) (function, `0x0048E7E0`)
- `0x0035D3F2` → [RtlpHpEnvCompactionSchedule](../32/RtlpHpEnvCompactionSchedule_function_003264A0.md) (function, `0x003264A0`)
- `0x0035D403` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0035D52C` → [ExpTrackTableGetMoreLimit](../2E/ExpTrackTableGetMoreLimit_function_002ECE40.md) (function, `0x002ECE40`)
- `0x0035D57F` → [RtlCSparseBitmapBitmaskRead](../36/RtlCSparseBitmapBitmaskRead_function_0036190C.md) (function, `0x0036190C`)
- `0x0035D5B6` → [RtlpHpVaMgrCtxQuery](../32/RtlpHpVaMgrCtxQuery_function_003273C0.md) (function, `0x003273C0`)
- `0x0035D629` → [PspReturnResourceQuota](../38/PspReturnResourceQuota_function_0038FFC4.md) (function, `0x0038FFC4`)
- `0x0035D657` → [ExpInsertPoolTrackerExpansion](../2E/ExpInsertPoolTrackerExpansion_function_002ECCC0.md) (function, `0x002ECCC0`)
- `0x0035D6C2` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035D6CC` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x0035D7D0` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x0035D80C` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035D888` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0035D8E8` → [RtlpHpLfhSlotAllocateSlow](../2E/RtlpHpLfhSlotAllocateSlow_function_002E8FBC.md) (function, `0x002E8FBC`)
- `0x0035D930` → [RtlpHpLfhBucketCheckAndUpdate](../4F/RtlpHpLfhBucketCheckAndUpdate_function_004FC894.md) (function, `0x004FC894`)
- `0x0035D964` → [RtlpHpVsContextAllocate](../2E/RtlpHpVsContextAllocate_function_002EA944.md) (function, `0x002EA944`)
- `0x0035D971` → [RtlpHpLfhBucketCheckAndUpdate](../4F/RtlpHpLfhBucketCheckAndUpdate_function_004FC894.md) (function, `0x004FC894`)
- `0x0035D99D` → [RtlpHpVsContextAllocate](../2E/RtlpHpVsContextAllocate_function_002EA944.md) (function, `0x002EA944`)
- `0x0035DA14` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035DA43` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035DA99` → [PspReturnResourceQuota](../38/PspReturnResourceQuota_function_0038FFC4.md) (function, `0x0038FFC4`)
- `0x0035DB29` → [ExpPlFindLimitEntry](../2E/ExpPlFindLimitEntry_function_002ECBF0.md) (function, `0x002ECBF0`)
- `0x0035DB4D` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0035DD61` → [RtlpHpLfhSlotAllocateSlow](../2E/RtlpHpLfhSlotAllocateSlow_function_002E8FBC.md) (function, `0x002E8FBC`)
- `0x0035DD83` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x0035DDF6` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x0035DE2F` → [RtlpHpLfhSubsegmentPrefetch](../2E/RtlpHpLfhSubsegmentPrefetch_function_002EBB18.md) (function, `0x002EBB18`)
- `0x0035DE58` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)
- `0x0035DE65` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0035DE96` → [RtlpHpLfhSubsegmentPrefetch](../2E/RtlpHpLfhSubsegmentPrefetch_function_002EBB18.md) (function, `0x002EBB18`)
- `0x0035DECA` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035DEEE` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035E0DD` → [ExpTrackTableGetMoreLimit](../2E/ExpTrackTableGetMoreLimit_function_002ECE40.md) (function, `0x002ECE40`)
- `0x0035E139` → [ExpInsertPoolTrackerExpansion](../2E/ExpInsertPoolTrackerExpansion_function_002ECCC0.md) (function, `0x002ECCC0`)
- `0x0035E234` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035E321` → [ExpPlFindLimitEntry](../2E/ExpPlFindLimitEntry_function_002ECBF0.md) (function, `0x002ECBF0`)
- `0x0035E350` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0035E3A1` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x0035E3AE` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0035E3E2` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035E3EF` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x0035E414` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035E41E` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x0035E4BD` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035E4DB` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (function, `0x00B84080`)
- `0x0035E510` → [EtwTracePool](../2E/EtwTracePool_function_002ECEEC.md) (function, `0x002ECEEC`)
- `0x0035E5A7` → [ExpInterlockedPopEntrySList](../6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x0035E5D1` → [RtlHeapZero](../6B/RtlHeapZero_function_006BBC10.md) (function, `0x006BBC10`)
- `0x0035E649` → [ExpCheckForLookaside](../4A/ExpCheckForLookaside_function_004A52DC.md) (function, `0x004A52DC`)
- `0x0035E65E` → [KeCheckForTimer](../4D/KeCheckForTimer_function_004D870C.md) (function, `0x004D870C`)
- `0x0035E669` → [FREE_CHECK_ERESOURCE](../49/FREE_CHECK_ERESOURCE_function_0049CA00.md) (function, `0x0049CA00`)
- `0x0035E682` → [ExpCheckForWorker](../4E/ExpCheckForWorker_function_004EC8FC.md) (function, `0x004EC8FC`)
- `0x0035E6A9` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035E6DD` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (function, `0x00B84080`)
- `0x0035E70A` → [EtwTracePool](../2E/EtwTracePool_function_002ECEEC.md) (function, `0x002ECEEC`)
- `0x0035E796` → [ExIsSpecialPoolAddress](../49/ExIsSpecialPoolAddress_function_0049C410.md) (function, `0x0049C410`)
- `0x0035E7AE` → [RtlpHpLargeFree](../2E/RtlpHpLargeFree_function_002EC89C.md) (function, `0x002EC89C`)
- `0x0035E7D4` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (function, `0x00B84080`)
- `0x0035E808` → [EtwTracePool](../2E/EtwTracePool_function_002ECEEC.md) (function, `0x002ECEEC`)
- `0x0035E820` → [ExCheckSingleFilter](../40/ExCheckSingleFilter_function_0040014C.md) (function, `0x0040014C`)
- `0x0035E8A9` → [ExpTrackTableReturnLimit](../4B/ExpTrackTableReturnLimit_function_004B055C.md) (function, `0x004B055C`)
- `0x0035E8B6` → [RtlpHpLfhThreadDataInitializeSet](../4F/RtlpHpLfhThreadDataInitializeSet_function_004F6334.md) (function, `0x004F6334`)
- `0x0035E8D4` → [ExpTrackTableReturnLimit](../4B/ExpTrackTableReturnLimit_function_004B055C.md) (function, `0x004B055C`)
- `0x0035E93E` → [RtlpHpAllocateHeapBackend](../32/RtlpHpAllocateHeapBackend_function_00326580.md) (function, `0x00326580`)
- `0x0035E94E` → [RtlpHpLfhThreadDataInitializeSet](../4F/RtlpHpLfhThreadDataInitializeSet_function_004F6334.md) (function, `0x004F6334`)
- `0x0035E96D` → [RtlpHpAllocateHeapBackend](../32/RtlpHpAllocateHeapBackend_function_00326580.md) (function, `0x00326580`)
- `0x0035E9B4` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035E9BA` → [RtlpHpLargeAlloc](../2E/RtlpHpLargeAlloc_function_002EBD5C.md) (function, `0x002EBD5C`)
- `0x0035E9C4` → [RtlpHpLargeAlloc](../2E/RtlpHpLargeAlloc_function_002EBD5C.md) (function, `0x002EBD5C`)
- `0x0035E9D1` → [RtlpHpLfhThreadDataInitializeSet](../4F/RtlpHpLfhThreadDataInitializeSet_function_004F6334.md) (function, `0x004F6334`)
- `0x0035E9E5` → [RtlpHpLfhThreadDataInitializeSet](../4F/RtlpHpLfhThreadDataInitializeSet_function_004F6334.md) (function, `0x004F6334`)
- `0x0035E9FA` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x0035EA0D` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x0035EA79` → [ViFreeTrackedPool](../../pagevrfy/BB/ViFreeTrackedPool_function_00BB8FC0.md) (function, `0x00BB8FC0`)
- `0x0035EB1C` → [ExpRemovePoolTrackerExpansion](../36/ExpRemovePoolTrackerExpansion_function_00361300.md) (function, `0x00361300`)
- `0x0035EB27` → [RtlpHpFreeHeap](RtlpHpFreeHeap_function_0035F600.md) (function, `0x0035F600`)
- `0x0035EB4E` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035EB71` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035EB88` → [ExpPoolTrackerReturnLimit](../36/ExpPoolTrackerReturnLimit_function_00361570.md) (function, `0x00361570`)
- `0x0035EBDD` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (function, `0x00B84080`)
- `0x0035EC0A` → [EtwTracePool](../2E/EtwTracePool_function_002ECEEC.md) (function, `0x002ECEEC`)
- `0x0035EC1E` → [MmDeterminePoolType](MmDeterminePoolType_function_0035F5B0.md) (function, `0x0035F5B0`)
- `0x0035EC63` → [ExpFreePoolChecks](ExpFreePoolChecks_function_0035F4F0.md) (function, `0x0035F4F0`)
- `0x0035EC92` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035ECC9` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035ECF8` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035ED0C` → [ExGetHeapFromType](ExGetHeapFromType_function_0035B8E0.md) (function, `0x0035B8E0`)
- `0x0035ED2E` → [RtlpHpSegAlloc](../32/RtlpHpSegAlloc_function_003265BC.md) (function, `0x003265BC`)
- `0x0035ED5F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0035EDBC` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0035EDCF` → [MmDeterminePoolType](MmDeterminePoolType_function_0035F5B0.md) (function, `0x0035F5B0`)
- `0x0035EEA6` → [ExpPoolTrackerChargeEntry](ExpPoolTrackerChargeEntry_function_0035B810.md) (function, `0x0035B810`)
- `0x0035EEC3` → [KasanPoolAllocate](../2E/KasanPoolAllocate_function_002EE3E0.md) (function, `0x002EE3E0`)
- `0x0035EF00` → [ExpFreeHeapSpecialPool](../2E/ExpFreeHeapSpecialPool_function_002EE600.md) (function, `0x002EE600`)
- `0x0035EF49` → [ExpInsertPoolTrackerExpansion](../2E/ExpInsertPoolTrackerExpansion_function_002ECCC0.md) (function, `0x002ECCC0`)
- `0x0035EF64` → [KasanPoolAllocate](../2E/KasanPoolAllocate_function_002EE3E0.md) (function, `0x002EE3E0`)
- `0x0035EFC4` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x0035EFE3` → [ExpPlFindLimitEntry](../2E/ExpPlFindLimitEntry_function_002ECBF0.md) (function, `0x002ECBF0`)
- `0x0035F01B` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0035F059` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (function, `0x00B84080`)
- `0x0035F08C` → [EtwTracePool](../2E/EtwTracePool_function_002ECEEC.md) (function, `0x002ECEEC`)
- `0x0035F103` → [RtlpHpVsContextMultiAlloc](../2E/RtlpHpVsContextMultiAlloc_function_002EB6B4.md) (function, `0x002EB6B4`)
- `0x0035F139` → [InterlockedPushListSList](../6B/InterlockedPushListSList_function_006BA620.md) (function, `0x006BA620`)
- `0x0035F16C` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035F191` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035F1FC` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035F222` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0035F290` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0035F2B5` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035F2F0` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0035F328` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035F352` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035F373` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035F39E` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035F3C0` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035F40D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0035F435` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0035F459` → [RtlpHpLfhBucketUpdateAffinityMapping](../4D/RtlpHpLfhBucketUpdateAffinityMapping_function_004D0008.md) (function, `0x004D0008`)
- `0x0035F4B0` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- [ExpAllocatePoolWithTagFromNode](ExpAllocatePoolWithTagFromNode_function_0035B970.md) at `0x0035B9BD`

### Static image references
- `0x0035BA7D` → RVA `0x00FC6BD0` (`ALMOSTRO`; read)
- `0x0035BADC` → RVA `0x00FC6C28` (`ALMOSTRO`; read)
- `0x0035BB3B` → RVA `0x00E6BF10` (`.data`; read)
- `0x0035BB51` → RVA `0x00E6BF40` (`.data`; read)
- `0x0035BBEC` → RVA `0x00E68610` (`.data`; read)
- `0x0035BBF3` → RVA `0x00E68608` (`.data`; read)
- `0x0035BC37` → RVA `0x00E28300` (`.data`; read)
- `0x0035BCA9` → RVA `0x00E28308` (`.data`; read)
- `0x0035BE87` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0035C090` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x0035C39B` → RVA `0x00E28328` (`.data`; read)
- `0x0035C4C8` → RVA `0x00EFA7BC` (`.data`; read)
- `0x0035C7D2` → RVA `0x00EFED20` (`.data`; read)
- `0x0035C8F6` → RVA `0x00FC514C` (`ALMOSTRO`; read)
- `0x0035C90F` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0035C925` → RVA `0x00EFED58` (`.data`; read)
- `0x0035C986` → RVA `0x00EFAD00` (`.data`; read)
- `0x0035C9AD` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0035C9BA` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0035C9CF` → RVA `0x00EFAD00` (`.data`; read/write)
- `0x0035C9DF` → RVA `0x00EFED48` (`.data`; read)
- `0x0035C9E9` → RVA `0x00EFED40` (`.data`; read)
- `0x0035CA28` → RVA `0x00EEEF40` (`.data`; read)
- `0x0035CA2F` → RVA `0x00EEEF60` (`.data`; read)
- `0x0035CAA9` → RVA `0x00FCEC68` (`ALMOSTRO`; read)
- `0x0035CEA9` → RVA `0x00F0DE58` (`.data`; read)
- `0x0035CEBB` → RVA `0x00EFACF8` (`.data`; read)
- `0x0035CEC7` → RVA `0x00EFED38` (`.data`; read)
- `0x0035CED1` → RVA `0x00EFED30` (`.data`; read)
- `0x0035CF5A` → RVA `0x00FC7228` (`ALMOSTRO`; read)
- `0x0035D035` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x0035D0AB` → RVA `0x00E27F80` (`.data`; read)
- `0x0035D104` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x0035D149` → RVA `0x00FCF100` (`CACHEALI`; read)
- `0x0035D19D` → RVA `0x00FCF100` (`CACHEALI`; read/write)
- `0x0035D1BA` → RVA `0x00EFACF8` (`.data`; read/write)
- `0x0035D3A2` → RVA `0x00EFED60` (`.data`; read)
- `0x0035D40D` → RVA `0x00EFA7C0` (`.data`; read)
- `0x0035D46B` → RVA `0x00EFED50` (`.data`; read)
- `0x0035D5A1` → RVA `0x00E68658` (`.data`; read)
- `0x0035D812` → RVA `0x00FC6C80` (`ALMOSTRO`; read)
- `0x0035E4A4` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x0035EC14` → RVA `0x00EFED20` (`.data`; read/write)
- `0x0035F1AF` → RVA `0x00FC6ED8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x0035C8F1` → [VfPtFreePoolNotification](../../pagevrfy/BB/VfPtFreePoolNotification_function_00BB96DC.md) (`.text` → `PAGEVRFY`)
  - `0x0035CAA4` → [ViFreeTrackedPool](../../pagevrfy/BB/ViFreeTrackedPool_function_00BB8FC0.md) (`.text` → `PAGEVRFY`)
  - `0x0035E4DB` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (`.text` → `POOLCODE`)
  - `0x0035E6DD` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (`.text` → `POOLCODE`)
  - `0x0035E7D4` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (`.text` → `POOLCODE`)
  - `0x0035EA79` → [ViFreeTrackedPool](../../pagevrfy/BB/ViFreeTrackedPool_function_00BB8FC0.md) (`.text` → `PAGEVRFY`)
  - `0x0035EBDD` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (`.text` → `POOLCODE`)
  - `0x0035F059` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0035C5BF` → [sub_006E2C7C](../6E/Unknown_function_006E2C7C.md) (`tail-transfer`)
  - `0x0035DC73` → [sub_006E2C7C + 0x364](../6E/Unknown_function_006E2C7C.md) (`tail-transfer`)
  - `0x0035DD0A` → [sub_006E2C7C + 0x120](../6E/Unknown_function_006E2C7C.md) (`tail-transfer`)
  - `0x0035F475` → [sub_006E2C7C + 0x235](../6E/Unknown_function_006E2C7C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0035BA30  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0035BA35  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0035BA3A  55                              push rbp
0035BA3B  56                              push rsi
0035BA3C  57                              push rdi
0035BA3D  41 54                           push r12
0035BA3F  41 55                           push r13
0035BA41  41 56                           push r14
0035BA43  41 57                           push r15
0035BA45  48 8D AC 24 D0 FE FF FF         lea rbp, [rsp - 0x130]
0035BA4D  48 81 EC 30 02 00 00            sub rsp, 0x230
0035BA54  48 8B C1                        mov rax, rcx
0035BA57  45 8B F9                        mov r15d, r9d
0035BA5A  45 33 C9                        xor r9d, r9d
0035BA5D  C7 44 24 6C 01 00 00 00         mov dword ptr [rsp + 0x6c], 1
0035BA65  4C 8B E1                        mov r12, rcx
0035BA68  4C 89 4C 24 70                  mov qword ptr [rsp + 0x70], r9
0035BA6D  41 83 E4 02                     and r12d, 2
0035BA71  4C 8B D9                        mov r11, rcx
0035BA74  41 BE 02 00 00 00               mov r14d, 2
0035BA7A  41 8B D8                        mov ebx, r8d
0035BA7D  44 8B 05 4C B1 C6 00            mov r8d, dword ptr [rip + 0xc6b14c]
0035BA84  45 0F 45 F1                     cmovne r14d, r9d
0035BA88  25 08 04 00 00                  and eax, 0x408
0035BA8D  49 83 E3 F7                     and r11, 0xfffffffffffffff7
0035BA91  48 3D 08 04 00 00               cmp rax, 0x408
0035BA97  48 8B F2                        mov rsi, rdx
0035BA9A  41 8B F9                        mov edi, r9d
0035BA9D  45 8B E9                        mov r13d, r9d
0035BAA0  4C 0F 45 D9                     cmovne r11, rcx
0035BAA4  49 F7 C3 40 01 00 00            test r11, 0x140
0035BAAB  4C 89 5C 24 78                  mov qword ptr [rsp + 0x78], r11
0035BAB0  0F 94 C1                        sete cl
0035BAB3  41 0F BA E0 0A                  bt r8d, 0xa
0035BAB8  0F 92 C0                        setb al
0035BABB  84 C8                           test al, cl
0035BABD  74 0E                           je 0x14035bacd
0035BABF  49 0F BA F3 07                  btr r11, 7
0035BAC4  49 83 CB 40                     or r11, 0x40
0035BAC8  4C 89 5C 24 78                  mov qword ptr [rsp + 0x78], r11
0035BACD  41 BA 00 10 00 00               mov r10d, 0x1000
0035BAD3  48 81 FE E0 0F 00 00            cmp rsi, 0xfe0
0035BADA  77 1E                           ja 0x14035bafa
0035BADC  44 8B 0D 45 B1 C6 00            mov r9d, dword ptr [rip + 0xc6b145]
0035BAE3  45 85 C9                        test r9d, r9d
0035BAE6  0F 85 26 2D 00 00               jne 0x14035e812
0035BAEC  49 0F BA E3 20                  bt r11, 0x20
0035BAF1  0F 82 29 04 00 00               jb 0x14035bf20
0035BAF7  45 33 C9                        xor r9d, r9d
0035BAFA  41 81 E3 FF 0F 00 00            and r11d, 0xfff
0035BB01  41 B8 01 00 00 00               mov r8d, 1
0035BB07  48 85 F6                        test rsi, rsi
0035BB0A  4C 89 5C 24 78                  mov qword ptr [rsp + 0x78], r11
0035BB0F  45 8B E8                        mov r13d, r8d
0035BB12  4C 0F 45 EE                     cmovne r13, rsi
0035BB16  41 81 FF 00 00 00 80            cmp r15d, 0x80000000
0035BB1D  0F 85 6D 05 00 00               jne 0x14035c090
0035BB23  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0035BB2C  48 8B 88 C0 00 00 00            mov rcx, qword ptr [rax + 0xc0]
0035BB33  44 0F B7 B9 8A 00 00 00         movzx r15d, word ptr [rcx + 0x8a]
0035BB3B  44 3B 3D CE 03 B1 00            cmp r15d, dword ptr [rip + 0xb103ce]
0035BB42  72 03                           jb 0x14035bb47
0035BB44  45 8B F9                        mov r15d, r9d
0035BB47  41 8B C7                        mov eax, r15d
0035BB4A  4C 69 F8 C0 20 00 00            imul r15, rax, 0x20c0
0035BB51  48 8D 05 E8 03 B1 00            lea rax, [rip + 0xb103e8]
0035BB58  4C 03 F8                        add r15, rax
0035BB5B  41 F6 C3 10                     test r11b, 0x10
0035BB5F  0F 85 22 05 00 00               jne 0x14035c087
0035BB65  49 0F BA E3 08                  bt r11, 8
0035BB6A  0F 83 F4 04 00 00               jae 0x14035c064
0035BB70  B8 02 00 00 00                  mov eax, 2
0035BB75  4D 8B 3C C7                     mov r15, qword ptr [r15 + rax*8]
0035BB79  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
0035BB7E  49 81 FD E0 0F 00 00            cmp r13, 0xfe0
0035BB85  0F 86 EE 05 00 00               jbe 0x14035c179
0035BB8B  49 8D 75 0F                     lea rsi, [r13 + 0xf]
0035BB8F  48 83 E6 F0                     and rsi, 0xfffffffffffffff0
0035BB93  8B C6                           mov eax, esi
0035BB95  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
0035BB9A  25 FF 0F 00 00                  and eax, 0xfff
0035BB9F  3D C0 0F 00 00                  cmp eax, 0xfc0
0035BBA4  0F 87 C2 1C 00 00               ja 0x14035d86c
0035BBAA  48 81 FE 00 00 01 00            cmp rsi, 0x10000
0035BBB1  0F 83 B5 1C 00 00               jae 0x14035d86c
0035BBB7  49 3B F5                        cmp rsi, r13
0035BBBA  0F 83 34 05 00 00               jae 0x14035c0f4
0035BBC0  4D 8B E1                        mov r12, r9
0035BBC3  4C 89 8D 78 01 00 00            mov qword ptr [rbp + 0x178], r9
0035BBCA  45 8B F8                        mov r15d, r8d
0035BBCD  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
0035BBD2  48 85 FF                        test rdi, rdi
0035BBD5  0F 84 A4 04 00 00               je 0x14035c07f
0035BBDB  66 85 FF                        test di, di
0035BBDE  74 09                           je 0x14035bbe9
0035BBE0  49 8D B5 40 01 00 00            lea rsi, [r13 + 0x140]
0035BBE7  EB 41                           jmp 0x14035bc2a
0035BBE9  48 8B D7                        mov rdx, rdi
0035BBEC  48 8D 0D 1D CA B0 00            lea rcx, [rip + 0xb0ca1d]
0035BBF3  48 2B 15 0E CA B0 00            sub rdx, qword ptr [rip + 0xb0ca0e]
0035BBFA  48 C1 EA 14                     shr rdx, 0x14
0035BBFE  48 03 D2                        add rdx, rdx
0035BC01  E8 06 5D 00 00                  call 0x14036190c
0035BC06  48 85 C0                        test rax, rax
0035BC09  0F 84 65 04 00 00               je 0x14035c074
0035BC0F  FF C8                           dec eax
0035BC11  83 F8 02                        cmp eax, 2
0035BC14  0F 84 5A 04 00 00               je 0x14035c074
0035BC1A  49 8D B5 40 01 00 00            lea rsi, [r13 + 0x140]
0035BC21  83 F8 01                        cmp eax, 1
0035BC24  0F 84 C1 1D 00 00               je 0x14035d9eb
0035BC2A  4C 8B 0E                        mov r9, qword ptr [rsi]
0035BC2D  49 8B D1                        mov rdx, r9
0035BC30  48 23 D7                        and rdx, rdi
0035BC33  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
0035BC37  48 33 05 C2 C6 AC 00            xor rax, qword ptr [rip + 0xacc6c2]
0035BC3E  48 33 C2                        xor rax, rdx
0035BC41  48 3B C6                        cmp rax, rsi
0035BC44  0F 85 1D 02 00 00               jne 0x14035be67
0035BC4A  44 0F B6 56 08                  movzx r10d, byte ptr [rsi + 8]
0035BC4F  44 8B C7                        mov r8d, edi
0035BC52  44 2B C2                        sub r8d, edx
0035BC55  41 8B CA                        mov ecx, r10d
0035BC58  41 D3 E8                        shr r8d, cl
0035BC5B  49 C1 E0 05                     shl r8, 5
0035BC5F  4C 03 C2                        add r8, rdx
0035BC62  41 0F B6 40 1A                  movzx eax, byte ptr [r8 + 0x1a]
0035BC67  48 F7 D8                        neg rax
0035BC6A  48 C1 E0 05                     shl rax, 5
0035BC6E  4C 03 C0                        add r8, rax
0035BC71  49 8B D8                        mov rbx, r8
0035BC74  48 2B DA                        sub rbx, rdx
0035BC77  48 C1 FB 05                     sar rbx, 5
0035BC7B  48 D3 E3                        shl rbx, cl
0035BC7E  48 03 DA                        add rbx, rdx
0035BC81  41 0F B6 50 18                  movzx edx, byte ptr [r8 + 0x18]
0035BC86  48 3B DF                        cmp rbx, rdi
0035BC89  0F 94 C0                        sete al
0035BC8C  8D 0C 10                        lea ecx, [rax + rdx]
0035BC8F  80 F9 0B                        cmp cl, 0xb
0035BC92  0F 85 F1 02 00 00               jne 0x14035bf89
0035BC98  4C 8B 76 18                     mov r14, qword ptr [rsi + 0x18]
0035BC9C  48 8B C3                        mov rax, rbx
0035BC9F  48 C1 E8 0C                     shr rax, 0xc
0035BCA3  44 8B C7                        mov r8d, edi
0035BCA6  33 43 28                        xor eax, dword ptr [rbx + 0x28]
0035BCA9  33 05 59 C6 AC 00               xor eax, dword ptr [rip + 0xacc659]
0035BCAF  8B C8                           mov ecx, eax
0035BCB1  48 C1 E8 10                     shr rax, 0x10
0035BCB5  48 03 C3                        add rax, rbx
0035BCB8  89 8D A0 00 00 00               mov dword ptr [rbp + 0xa0], ecx
0035BCBE  0F B7 53 2C                     movzx edx, word ptr [rbx + 0x2c]
0035BCC2  44 2B C0                        sub r8d, eax
0035BCC5  41 8B C0                        mov eax, r8d
0035BCC8  48 C1 E2 06                     shl rdx, 6
0035BCCC  0F B7 C9                        movzx ecx, cx
0035BCCF  42 8B 74 32 48                  mov esi, dword ptr [rdx + r14 + 0x48]
0035BCD4  48 0F AF F0                     imul rsi, rax
0035BCD8  48 C1 EE 20                     shr rsi, 0x20
0035BCDC  8B C6                           mov eax, esi
0035BCDE  0F AF C1                        imul eax, ecx
0035BCE1  44 2B C0                        sub r8d, eax
0035BCE4  44 89 85 9C 00 00 00            mov dword ptr [rbp + 0x9c], r8d
0035BCEB  0F 85 8E 03 00 00               jne 0x14035c07f
0035BCF1  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0035BCFA  41 B9 01 00 00 00               mov r9d, 1
0035BD00  45 8B 56 4C                     mov r10d, dword ptr [r14 + 0x4c]
0035BD04  45 33 ED                        xor r13d, r13d
0035BD07  41 8B D2                        mov edx, r10d
0035BD0A  49 C1 EA 04                     shr r10, 4
0035BD0E  C1 EA 0D                        shr edx, 0xd
0035BD11  41 81 E2 FF 01 00 00            and r10d, 0x1ff
0035BD18  4C 8B 80 B0 8B 00 00            mov r8, qword ptr [rax + 0x8bb0]
0035BD1F  81 E2 FF FF 03 00               and edx, 0x3ffff
0035BD25  0F BD CA                        bsr ecx, edx
0035BD28  41 D3 E1                        shl r9d, cl
0035BD2B  83 C1 FE                        add ecx, -2
0035BD2E  89 4D 1C                        mov dword ptr [rbp + 0x1c], ecx
0035BD31  44 33 CA                        xor r9d, edx
0035BD34  49 8B 0C C8                     mov rcx, qword ptr [r8 + rcx*8]
0035BD38  4A 8B 4C C9 08                  mov rcx, qword ptr [rcx + r9*8 + 8]
0035BD3D  4A 8B 04 D1                     mov rax, qword ptr [rcx + r10*8]
0035BD41  48 85 C0                        test rax, rax
0035BD44  0F 84 69 2B 00 00               je 0x14035e8b3
0035BD4A  66 3B 43 2E                     cmp ax, word ptr [rbx + 0x2e]
0035BD4E  0F 84 F8 2A 00 00               je 0x14035e84c
0035BD54  8B C6                           mov eax, esi
0035BD56  8B D6                           mov edx, esi
0035BD58  C1 E8 06                        shr eax, 6
0035BD5B  83 E2 3F                        and edx, 0x3f
0035BD5E  48 8B 4C C3 40                  mov rcx, qword ptr [rbx + rax*8 + 0x40]
0035BD63  8B C2                           mov eax, edx
0035BD65  48 0F A3 C1                     bt rcx, rax
0035BD69  0F 83 63 03 00 00               jae 0x14035c0d2
0035BD6F  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0035BD73  66 FF C6                        inc si
0035BD76  48 8B C8                        mov rcx, rax
0035BD79  48 89 45 08                     mov qword ptr [rbp + 8], rax
0035BD7D  48 C1 E9 30                     shr rcx, 0x30
0035BD81  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0035BD86  80 F9 01                        cmp cl, 1
0035BD89  75 05                           jne 0x14035bd90
0035BD8B  C6 44 24 4E 02                  mov byte ptr [rsp + 0x4e], 2
0035BD90  4D 8B 46 50                     mov r8, qword ptr [r14 + 0x50]
0035BD94  0F B7 4C 24 48                  movzx ecx, word ptr [rsp + 0x48]
0035BD99  49 8B D0                        mov rdx, r8
0035BD9C  66 FF 44 24 4A                  inc word ptr [rsp + 0x4a]
0035BDA1  66 89 0F                        mov word ptr [rdi], cx
0035BDA4  4C 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], r8
0035BDAB  44 33 07                        xor r8d, dword ptr [rdi]
0035BDAE  0F B6 0F                        movzx ecx, byte ptr [rdi]
0035BDB1  48 C1 EA 20                     shr rdx, 0x20
0035BDB5  33 D7                           xor edx, edi
0035BDB7  41 D3 C0                        rol r8d, cl
0035BDBA  44 33 C2                        xor r8d, edx
0035BDBD  66 89 74 24 48                  mov word ptr [rsp + 0x48], si
0035BDC2  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0035BDC7  44 89 47 08                     mov dword ptr [rdi + 8], r8d
0035BDCB  0F B7 53 2C                     movzx edx, word ptr [rbx + 0x2c]
0035BDCF  48 C1 E2 06                     shl rdx, 6
0035BDD3  F0 48 0F B1 4B 10               lock cmpxchg qword ptr [rbx + 0x10], rcx
0035BDD9  75 9B                           jne 0x14035bd76
0035BDDB  46 38 6C 32 5C                  cmp byte ptr [rdx + r14 + 0x5c], r13b
0035BDE0  0F 84 C6 06 00 00               je 0x14035c4ac
0035BDE6  80 7D 0E 01                     cmp byte ptr [rbp + 0xe], 1
0035BDEA  0F 85 97 00 00 00               jne 0x14035be87
0035BDF0  44 0F B7 4D 0C                  movzx r9d, word ptr [rbp + 0xc]
0035BDF5  41 C1 E1 06                     shl r9d, 6
0035BDF9  4D 03 CE                        add r9, r14
0035BDFC  41 0F 0D 49 08                  prefetchw byte ptr [r9 + 8]
0035BE01  4C 8B 53 18                     mov r10, qword ptr [rbx + 0x18]
0035BE05  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
0035BE09  49 8B CA                        mov rcx, r10
0035BE0C  48 33 C8                        xor rcx, rax
0035BE0F  48 8B D0                        mov rdx, rax
0035BE12  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
0035BE19  81 E2 FF 0F 00 00               and edx, 0xfff
0035BE1F  49 33 CA                        xor rcx, r10
0035BE22  48 89 4B 18                     mov qword ptr [rbx + 0x18], rcx
0035BE26  48 8B CB                        mov rcx, rbx
0035BE29  48 0B CA                        or rcx, rdx
0035BE2C  F0 49 0F B1 49 08               lock cmpxchg qword ptr [r9 + 8], rcx
0035BE32  74 53                           je 0x14035be87
0035BE34  48 8B D0                        mov rdx, rax
0035BE37  49 8B CA                        mov rcx, r10
0035BE3A  48 33 C8                        xor rcx, rax
0035BE3D  81 E2 FF 0F 00 00               and edx, 0xfff
0035BE43  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
0035BE4A  4C 8B C0                        mov r8, rax
0035BE4D  49 33 CA                        xor rcx, r10
0035BE50  48 89 4B 18                     mov qword ptr [rbx + 0x18], rcx
0035BE54  48 8B CB                        mov rcx, rbx
0035BE57  48 0B CA                        or rcx, rdx
0035BE5A  F0 49 0F B1 49 08               lock cmpxchg qword ptr [r9 + 8], rcx
0035BE60  49 3B C0                        cmp rax, r8
0035BE63  75 CF                           jne 0x14035be34
0035BE65  EB 20                           jmp 0x14035be87
0035BE67  45 33 ED                        xor r13d, r13d
0035BE6A  48 8B 56 38                     mov rdx, qword ptr [rsi + 0x38]
0035BE6E  45 33 C9                        xor r9d, r9d
0035BE71  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0035BE76  4C 8B C7                        mov r8, rdi
0035BE79  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0035BE7E  41 8D 49 09                     lea ecx, [r9 + 9]
0035BE82  E8 35 F9 FF FF                  call 0x14035b7bc
0035BE87  48 8D 3D 72 41 CA FF            lea rdi, [rip - 0x35be8e]
0035BE8E  45 85 FF                        test r15d, r15d
0035BE91  0F 85 29 09 00 00               jne 0x14035c7c0
0035BE97  0F 57 C0                        xorps xmm0, xmm0
0035BE9A  0F 11 45 58                     movups xmmword ptr [rbp + 0x58], xmm0
0035BE9E  66 C7 45 58 01 01               mov word ptr [rbp + 0x58], 0x101
0035BEA4  C6 45 58 03                     mov byte ptr [rbp + 0x58], 3
0035BEA8  C6 45 58 03                     mov byte ptr [rbp + 0x58], 3
0035BEAC  44 88 7D 5A                     mov byte ptr [rbp + 0x5a], r15b
0035BEB0  66 45 85 E4                     test r12w, r12w
0035BEB4  0F 84 AD 16 00 00               je 0x14035d567
0035BEBA  41 8B C5                        mov eax, r13d
0035BEBD  48 63 C8                        movsxd rcx, eax
0035BEC0  C7 45 48 00 00 10 00            mov dword ptr [rbp + 0x48], 0x100000
0035BEC7  C7 45 4C 00 00 00 01            mov dword ptr [rbp + 0x4c], 0x1000000
0035BECE  8B 44 8D 48                     mov eax, dword ptr [rbp + rcx*4 + 0x48]
0035BED2  48 FF C8                        dec rax
0035BED5  48 F7 D0                        not rax
0035BED8  49 23 C4                        and rax, r12
0035BEDB  4C 8B 78 10                     mov r15, qword ptr [rax + 0x10]
0035BEDF  4C 33 3D 1A C4 AC 00            xor r15, qword ptr [rip + 0xacc41a]
0035BEE6  4C 33 F8                        xor r15, rax
0035BEE9  48 8D 04 49                     lea rax, [rcx + rcx*2]
0035BEED  48 C1 E0 06                     shl rax, 6
0035BEF1  4C 2B F8                        sub r15, rax
0035BEF4  49 81 EF 40 01 00 00            sub r15, 0x140
0035BEFB  4C 89 7D 88                     mov qword ptr [rbp - 0x78], r15
0035BEFF  4D 85 FF                        test r15, r15
0035BF02  0F 85 CA 08 00 00               jne 0x14035c7d2
0035BF08  4D 8B CC                        mov r9, r12
0035BF0B  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0035BF10  45 33 C0                        xor r8d, r8d
0035BF13  33 D2                           xor edx, edx
0035BF15  B9 C2 00 00 00                  mov ecx, 0xc2
0035BF1A  E8 41 17 1A 00                  call 0x1404fd660
0035BF1F  CC                              int3
0035BF20  49 8B CB                        mov rcx, r11
0035BF23  4C 89 5D B8                     mov qword ptr [rbp - 0x48], r11
0035BF27  81 E1 C0 01 00 00               and ecx, 0x1c0
0035BF2D  49 8B FB                        mov rdi, r11
0035BF30  48 81 F9 00 01 00 00            cmp rcx, 0x100
0035BF37  75 11                           jne 0x14035bf4a
0035BF39  B2 01                           mov dl, 1
0035BF3B  44 0F 20 C0                     mov rax, cr8
0035BF3F  48 81 F9 00 01 00 00            cmp rcx, 0x100
0035BF46  75 1A                           jne 0x14035bf62
0035BF48  EB 1A                           jmp 0x14035bf64
0035BF4A  41 0F BA E0 0A                  bt r8d, 0xa
0035BF4F  73 E8                           jae 0x14035bf39
0035BF51  48 0F BA F7 07                  btr rdi, 7
0035BF56  48 83 CF 40                     or rdi, 0x40
0035BF5A  48 89 7D B8                     mov qword ptr [rbp - 0x48], rdi
0035BF5E  44 0F 20 C0                     mov rax, cr8
0035BF62  B2 02                           mov dl, 2
0035BF64  3A C2                           cmp al, dl
0035BF66  0F 86 92 2D 00 00               jbe 0x14035ecfe
0035BF6C  44 8B C7                        mov r8d, edi
0035BF6F  4C 8B CE                        mov r9, rsi
0035BF72  0F B6 D0                        movzx edx, al
0035BF75  B9 C1 00 00 00                  mov ecx, 0xc1
0035BF7A  48 C7 44 24 20 30 00 00 00      mov qword ptr [rsp + 0x20], 0x30
0035BF83  E8 D8 16 1A 00                  call 0x1404fd660
0035BF88  CC                              int3
0035BF89  4D 23 C8                        and r9, r8
0035BF8C  41 8B CA                        mov ecx, r10d
0035BF8F  45 33 ED                        xor r13d, r13d
0035BF92  49 8B C0                        mov rax, r8
0035BF95  49 2B C1                        sub rax, r9
0035BF98  44 89 6D D4                     mov dword ptr [rbp - 0x2c], r13d
0035BF9C  48 C1 F8 05                     sar rax, 5
0035BFA0  48 D3 E0                        shl rax, cl
0035BFA3  4A 8D 0C 08                     lea rcx, [rax + r9]
0035BFA7  0F B6 C2                        movzx eax, dl
0035BFAA  24 03                           and al, 3
0035BFAC  3C 03                           cmp al, 3
0035BFAE  0F 85 B6 FE FF FF               jne 0x14035be6a
0035BFB4  48 3B F9                        cmp rdi, rcx
0035BFB7  0F 84 05 01 00 00               je 0x14035c0c2
0035BFBD  80 FA 0F                        cmp dl, 0xf
0035BFC0  0F 85 A4 FE FF FF               jne 0x14035be6a
0035BFC6  48 3B F9                        cmp rdi, rcx
0035BFC9  0F 86 F3 00 00 00               jbe 0x14035c0c2
0035BFCF  48 8B D1                        mov rdx, rcx
0035BFD2  4C 8D 4D D4                     lea r9, [rbp - 0x2c]
0035BFD6  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
0035BFDA  4C 8B C7                        mov r8, rdi
0035BFDD  E8 4E 56 00 00                  call 0x140361630
0035BFE2  85 C0                           test eax, eax
0035BFE4  0F 84 9D FE FF FF               je 0x14035be87
0035BFEA  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
0035BFEE  48 8D 3D 0B 40 CA FF            lea rdi, [rip - 0x35bff5]
0035BFF5  8B 4D D4                        mov ecx, dword ptr [rbp - 0x2c]
0035BFF8  0F B7 42 44                     movzx eax, word ptr [rdx + 0x44]
0035BFFC  3B C8                           cmp ecx, eax
0035BFFE  0F 83 8A FE FF FF               jae 0x14035be8e
0035C004  8D 41 0F                        lea eax, [rcx + 0xf]
0035C007  C1 E8 04                        shr eax, 4
0035C00A  44 0F B6 94 38 80 0B 01 00      movzx r10d, byte ptr [rax + rdi + 0x10b80]
0035C013  41 FF CA                        dec r10d
0035C016  4E 8D 0C D2                     lea r9, [rdx + r10*8]
0035C01A  4D 8B 81 C0 01 00 00            mov r8, qword ptr [r9 + 0x1c0]
0035C021  49 8B C0                        mov rax, r8
0035C024  49 8B C8                        mov rcx, r8
0035C027  48 C1 E8 10                     shr rax, 0x10
0035C02B  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
0035C02F  41 F6 C0 01                     test r8b, 1
0035C033  74 22                           je 0x14035c057
0035C035  66 83 F8 01                     cmp ax, 1
0035C039  76 0B                           jbe 0x14035c046
0035C03B  66 FF C8                        dec ax
0035C03E  66 89 45 8A                     mov word ptr [rbp - 0x76], ax
0035C042  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
0035C046  49 8B C0                        mov rax, r8
0035C049  F0 49 0F B1 89 C0 01 00 00      lock cmpxchg qword ptr [r9 + 0x1c0], rcx
0035C052  49 3B C0                        cmp rax, r8
0035C055  75 C3                           jne 0x14035c01a
0035C057  4A 8B 8C D2 C0 01 00 00         mov rcx, qword ptr [rdx + r10*8 + 0x1c0]
0035C05F  E9 2A FE FF FF                  jmp 0x14035be8e
0035C064  41 F6 C3 80                     test r11b, 0x80
0035C068  49 8B C0                        mov rax, r8
0035C06B  49 0F 45 C1                     cmovne rax, r9
0035C06F  E9 01 FB FF FF                  jmp 0x14035bb75
0035C074  48 8B D7                        mov rdx, rdi
0035C077  49 8B CD                        mov rcx, r13
0035C07A  E8 1D 08 F9 FF                  call 0x1402ec89c
0035C07F  45 33 ED                        xor r13d, r13d
0035C082  E9 00 FE FF FF                  jmp 0x14035be87
0035C087  4D 8B 7F 18                     mov r15, qword ptr [r15 + 0x18]
0035C08B  E9 E9 FA FF FF                  jmp 0x14035bb79
0035C090  0F B7 05 69 8F C6 00            movzx eax, word ptr [rip + 0xc68f69]
0035C097  44 3B F8                        cmp r15d, eax
0035C09A  0F 82 A9 17 00 00               jb 0x14035d849
0035C0A0  49 0F BA F3 09                  btr r11, 9
0035C0A5  8B C3                           mov eax, ebx
0035C0A7  4D 8B CB                        mov r9, r11
0035C0AA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0035C0AF  4D 8B C7                        mov r8, r15
0035C0B2  BA 0E 00 00 00                  mov edx, 0xe
0035C0B7  B9 C2 00 00 00                  mov ecx, 0xc2
0035C0BC  E8 9F 15 1A 00                  call 0x1404fd660
0035C0C1  CC                              int3
0035C0C2  49 8B D0                        mov rdx, r8
0035C0C5  48 8B CE                        mov rcx, rsi
0035C0C8  E8 D3 6E F8 FF                  call 0x1402e2fa0
0035C0CD  E9 B5 FD FF FF                  jmp 0x14035be87
0035C0D2  49 8B 16                        mov rdx, qword ptr [r14]
0035C0D5  4C 8B CB                        mov r9, rbx
0035C0D8  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0035C0DD  4C 8B C7                        mov r8, rdi
0035C0E0  B9 11 00 00 00                  mov ecx, 0x11
0035C0E5  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0035C0EA  E8 CD F6 FF FF                  call 0x14035b7bc
0035C0EF  E9 93 FD FF FF                  jmp 0x14035be87
0035C0F4  F7 C6 FF 0F 00 00               test esi, 0xfff
0035C0FA  0F 85 E4 03 00 00               jne 0x14035c4e4
0035C100  41 8B 87 10 02 00 00            mov eax, dword ptr [r15 + 0x210]
0035C107  48 3B F0                        cmp rsi, rax
0035C10A  0F 87 D4 03 00 00               ja 0x14035c4e4
0035C110  45 8B CB                        mov r9d, r11d
0035C113  4C 8B C6                        mov r8, rsi
0035C116  41 F7 D1                        not r9d
0035C119  48 8B D6                        mov rdx, rsi
0035C11C  41 83 E1 02                     and r9d, 2
0035C120  49 8B CF                        mov rcx, r15
0035C123  E8 58 A4 FC FF                  call 0x140326580
0035C128  48 8B F8                        mov rdi, rax
0035C12B  48 85 FF                        test rdi, rdi
0035C12E  0F 84 EA 17 00 00               je 0x14035d91e
0035C134  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
0035C139  33 F6                           xor esi, esi
0035C13B  8B 9D 80 01 00 00               mov ebx, dword ptr [rbp + 0x180]
0035C141  4D 8B CE                        mov r9, r14
0035C144  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
0035C149  8B D3                           mov edx, ebx
0035C14B  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
0035C150  48 8B CF                        mov rcx, rdi
0035C153  66 89 74 24 20                  mov word ptr [rsp + 0x20], si
0035C158  E8 13 34 F9 FF                  call 0x1402ef570
0035C15D  85 C0                           test eax, eax
0035C15F  0F 85 B3 12 00 00               jne 0x14035d418
0035C165  44 8B E6                        mov r12d, esi
0035C168  48 89 B5 78 01 00 00            mov qword ptr [rbp + 0x178], rsi
0035C16F  44 8B 7C 24 6C                  mov r15d, dword ptr [rsp + 0x6c]
0035C174  E9 54 FA FF FF                  jmp 0x14035bbcd
0035C179  49 8D 75 10                     lea rsi, [r13 + 0x10]
0035C17D  41 F6 C3 08                     test r11b, 8
0035C181  0F 85 8B 16 00 00               jne 0x14035d812
0035C187  48 83 C6 0F                     add rsi, 0xf
0035C18B  4C 8D 15 6E 3E CA FF            lea r10, [rip - 0x35c192]
0035C192  48 83 E6 F0                     and rsi, 0xfffffffffffffff0
0035C196  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
0035C19B  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
0035C1A0  48 8D 86 FF FD FF FF            lea rax, [rsi - 0x201]
0035C1A7  48 3D 7F 0D 00 00               cmp rax, 0xd7f
0035C1AD  0F 86 A3 23 00 00               jbe 0x14035e556
0035C1B3  48 8B C6                        mov rax, rsi
0035C1B6  49 8B D0                        mov rdx, r8
0035C1B9  48 83 F8 01                     cmp rax, 1
0035C1BD  48 0F 47 D0                     cmova rdx, rax
0035C1C1  41 0F B7 87 84 03 00 00         movzx eax, word ptr [r15 + 0x384]
0035C1C9  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
0035C1CD  48 3B D0                        cmp rdx, rax
0035C1D0  0F 83 AD 32 00 00               jae 0x14035f483
0035C1D6  8D 42 0F                        lea eax, [rdx + 0xf]
0035C1D9  41 B9 01 00 00 00               mov r9d, 1
0035C1DF  C1 E8 04                        shr eax, 4
0035C1E2  4D 8D 9F 40 03 00 00            lea r11, [r15 + 0x340]
0035C1E9  42 0F B6 84 10 80 0B 01 00      movzx eax, byte ptr [rax + r10 + 0x10b80]
0035C1F2  45 8B 53 4C                     mov r10d, dword ptr [r11 + 0x4c]
0035C1F6  FF C8                           dec eax
0035C1F8  41 8B D2                        mov edx, r10d
0035C1FB  89 85 70 01 00 00               mov dword ptr [rbp + 0x170], eax
0035C201  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0035C20A  49 C1 EA 04                     shr r10, 4
0035C20E  C1 EA 0D                        shr edx, 0xd
0035C211  41 81 E2 FF 01 00 00            and r10d, 0x1ff
0035C218  81 E2 FF FF 03 00               and edx, 0x3ffff
0035C21E  4C 8B 80 B0 8B 00 00            mov r8, qword ptr [rax + 0x8bb0]
0035C225  0F BD CA                        bsr ecx, edx
0035C228  41 D3 E1                        shl r9d, cl
0035C22B  83 C1 FE                        add ecx, -2
0035C22E  89 4D 18                        mov dword ptr [rbp + 0x18], ecx
0035C231  44 33 CA                        xor r9d, edx
0035C234  49 8B 0C C8                     mov rcx, qword ptr [r8 + rcx*8]
0035C238  4A 8B 4C C9 08                  mov rcx, qword ptr [rcx + r9*8 + 8]
0035C23D  4A 8B 04 D1                     mov rax, qword ptr [rcx + r10*8]
0035C241  48 85 C0                        test rax, rax
0035C244  0F 84 84 27 00 00               je 0x14035e9ce
0035C24A  8B 95 70 01 00 00               mov edx, dword ptr [rbp + 0x170]
0035C250  0F B7 C8                        movzx ecx, ax
0035C253  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
0035C257  8B C2                           mov eax, edx
0035C259  48 03 C0                        add rax, rax
0035C25C  C1 E1 06                        shl ecx, 6
0035C25F  49 03 CB                        add rcx, r11
0035C262  48 89 85 70 01 00 00            mov qword ptr [rbp + 0x170], rax
0035C269  48 03 C1                        add rax, rcx
0035C26C  48 89 8D 78 01 00 00            mov qword ptr [rbp + 0x178], rcx
0035C273  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0035C278  0F B7 00                        movzx eax, word ptr [rax]
0035C27B  44 8B C0                        mov r8d, eax
0035C27E  85 C0                           test eax, eax
0035C280  0F 84 A7 16 00 00               je 0x14035d92d
0035C286  41 C1 E0 06                     shl r8d, 6
0035C28A  41 8B D0                        mov edx, r8d
0035C28D  49 03 D3                        add rdx, r11
0035C290  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
0035C295  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
0035C29A  66 83 7A 04 00                  cmp word ptr [rdx + 4], 0
0035C29F  0F 85 C6 31 00 00               jne 0x14035f46b
0035C2A5  C7 44 24 68 00 00 00 00         mov dword ptr [rsp + 0x68], 0
0035C2AD  0F 0D 4A 38                     prefetchw byte ptr [rdx + 0x38]
0035C2B1  4C 8B 5A 38                     mov r11, qword ptr [rdx + 0x38]
0035C2B5  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
0035C2BA  49 F7 C3 FF 0F 00 00            test r11, 0xfff
0035C2C1  0F 84 14 16 00 00               je 0x14035d8db
0035C2C7  49 8D 4B FF                     lea rcx, [r11 - 1]
0035C2CB  49 8B C3                        mov rax, r11
0035C2CE  F0 48 0F B1 4A 38               lock cmpxchg qword ptr [rdx + 0x38], rcx
0035C2D4  0F 85 5F 15 00 00               jne 0x14035d839
0035C2DA  65 4C 8B 0C 25 88 01 00 00      mov r9, qword ptr gs:[0x188]
0035C2E3  49 81 E3 00 F0 FF FF            and r11, 0xfffffffffffff000
0035C2EA  49 8B C3                        mov rax, r11
0035C2ED  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
0035C2F2  48 C1 E8 0C                     shr rax, 0xc
0035C2F6  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
0035C2FB  41 33 43 28                     xor eax, dword ptr [r11 + 0x28]
0035C2FF  33 05 03 C0 AC 00               xor eax, dword ptr [rip + 0xacc003]
0035C305  49 8B 89 60 07 00 00            mov rcx, qword ptr [r9 + 0x760]
0035C30C  49 8B 91 68 07 00 00            mov rdx, qword ptr [r9 + 0x768]
0035C313  45 0F B6 53 18                  movzx r10d, byte ptr [r11 + 0x18]
0035C318  89 45 A0                        mov dword ptr [rbp - 0x60], eax
0035C31B  41 83 EA 08                     sub r10d, 8
0035C31F  0F B7 C0                        movzx eax, ax
0035C322  4C 8D 04 0A                     lea r8, [rdx + rcx]
0035C326  89 45 80                        mov dword ptr [rbp - 0x80], eax
0035C329  48 33 D1                        xor rdx, rcx
0035C32C  49 C1 E8 20                     shr r8, 0x20
0035C330  48 C1 C1 18                     rol rcx, 0x18
0035C334  48 8B C2                        mov rax, rdx
0035C337  48 C1 E0 10                     shl rax, 0x10
0035C33B  48 33 C8                        xor rcx, rax
0035C33E  48 33 CA                        xor rcx, rdx
0035C341  48 C1 C2 25                     rol rdx, 0x25
0035C345  49 89 89 60 07 00 00            mov qword ptr [r9 + 0x760], rcx
0035C34C  49 FF CA                        dec r10
0035C34F  49 89 91 68 07 00 00            mov qword ptr [r9 + 0x768], rdx
0035C356  49 8D 4B 40                     lea rcx, [r11 + 0x40]
0035C35A  41 0F B6 43 32                  movzx eax, byte ptr [r11 + 0x32]
0035C35F  89 45 D0                        mov dword ptr [rbp - 0x30], eax
0035C362  41 0F B6 43 27                  movzx eax, byte ptr [r11 + 0x27]
0035C367  4E 8D 14 D1                     lea r10, [rcx + r10*8]
0035C36B  8B 75 D0                        mov esi, dword ptr [rbp - 0x30]
0035C36E  45 0F B6 C8                     movzx r9d, r8b
0035C372  88 85 70 01 00 00               mov byte ptr [rbp + 0x170], al
0035C378  41 0F B6 43 24                  movzx eax, byte ptr [r11 + 0x24]
0035C37D  44 89 8D 78 01 00 00            mov dword ptr [rbp + 0x178], r9d
0035C384  4C 89 55 B0                     mov qword ptr [rbp - 0x50], r10
0035C388  4C 8D 04 C1                     lea r8, [rcx + rax*8]
0035C38C  49 8B 10                        mov rdx, qword ptr [r8]
0035C38F  48 F7 D2                        not rdx
0035C392  48 85 D2                        test rdx, rdx
0035C395  0F 84 AD 19 00 00               je 0x14035dd48
0035C39B  8B 05 87 BF AC 00               mov eax, dword ptr [rip + 0xacbf87]
0035C3A1  A8 04                           test al, 4
0035C3A3  0F 85 EE 17 00 00               jne 0x14035db97
0035C3A9  4D 3B C2                        cmp r8, r10
0035C3AC  0F 84 94 20 00 00               je 0x14035e446
0035C3B2  83 FE 40                        cmp esi, 0x40
0035C3B5  0F 85 8B 20 00 00               jne 0x14035e446
0035C3BB  41 8B C9                        mov ecx, r9d
0035C3BE  48 D3 CA                        ror rdx, cl
0035C3C1  F3 4C 0F BC D2                  tzcnt r10, rdx
0035C3C6  45 03 D1                        add r10d, r9d
0035C3C9  41 83 E2 3F                     and r10d, 0x3f
0035C3CD  41 8B CA                        mov ecx, r10d
0035C3D0  41 B9 01 00 00 00               mov r9d, 1
0035C3D6  49 D3 E1                        shl r9, cl
0035C3D9  41 0F 0D 08                     prefetchw byte ptr [r8]
0035C3DD  49 8B 00                        mov rax, qword ptr [r8]
0035C3E0  48 8B C8                        mov rcx, rax
0035C3E3  49 0B C9                        or rcx, r9
0035C3E6  F0 49 0F B1 08                  lock cmpxchg qword ptr [r8], rcx
0035C3EB  75 F3                           jne 0x14035c3e0
0035C3ED  48 8B D0                        mov rdx, rax
0035C3F0  4C 85 C8                        test rax, r9
0035C3F3  0F 85 71 17 00 00               jne 0x14035db6a
0035C3F9  44 8B 4D 80                     mov r9d, dword ptr [rbp - 0x80]
0035C3FD  49 8D 43 40                     lea rax, [r11 + 0x40]
0035C401  44 2B C0                        sub r8d, eax
0035C404  43 8D 0C C2                     lea ecx, [r10 + r8*8]
0035C408  8B F1                           mov esi, ecx
0035C40A  89 8D 78 01 00 00               mov dword ptr [rbp + 0x178], ecx
0035C410  41 0F AF F1                     imul esi, r9d
0035C414  8B C1                           mov eax, ecx
0035C416  C1 E8 06                        shr eax, 6
0035C419  41 88 43 24                     mov byte ptr [r11 + 0x24], al
0035C41D  0F B7 45 A2                     movzx eax, word ptr [rbp - 0x5e]
0035C421  03 F0                           add esi, eax
0035C423  80 BD 70 01 00 00 01            cmp byte ptr [rbp + 0x170], 1
0035C42A  0F 86 E5 19 00 00               jbe 0x14035de15
0035C430  44 8B C6                        mov r8d, esi
0035C433  49 8D 8F 40 03 00 00            lea rcx, [r15 + 0x340]
0035C43A  49 8B D3                        mov rdx, r11
0035C43D  E8 EE E1 F8 FF                  call 0x1402ea630
0035C442  4C 8B 5C 24 30                  mov r11, qword ptr [rsp + 0x30]
0035C447  85 C0                           test eax, eax
0035C449  0F 88 CE 17 00 00               js 0x14035dc1d
0035C44F  49 03 F3                        add rsi, r11
0035C452  4D 85 E4                        test r12, r12
0035C455  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
0035C45A  75 18                           jne 0x14035c474
0035C45C  41 8B D4                        mov edx, r12d
0035C45F  48 8B CE                        mov rcx, rsi
0035C462  48 83 C2 0F                     add rdx, 0xf
0035C466  48 83 E2 F0                     and rdx, 0xfffffffffffffff0
0035C46A  E8 A1 F7 35 00                  call 0x1406bbc10
0035C46F  4C 8B 5C 24 30                  mov r11, qword ptr [rsp + 0x30]
0035C474  48 85 F6                        test rsi, rsi
0035C477  0F 84 E6 17 00 00               je 0x14035dc63
0035C47D  4D 8D 87 40 03 00 00            lea r8, [r15 + 0x340]
0035C484  83 7C 24 68 00                  cmp dword ptr [rsp + 0x68], 0
0035C489  0F 84 66 14 00 00               je 0x14035d8f5
0035C48F  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0035C494  49 8B C8                        mov rcx, r8
0035C497  0F B7 50 02                     movzx edx, word ptr [rax + 2]
0035C49B  48 C1 E2 06                     shl rdx, 6
0035C49F  49 03 D0                        add rdx, r8
0035C4A2  E8 61 3B 17 00                  call 0x1404d0008
0035C4A7  E9 49 14 00 00                  jmp 0x14035d8f5
0035C4AC  42 C6 44 32 5C 01               mov byte ptr [rdx + r14 + 0x5c], 1
0035C4B2  49 8B 0E                        mov rcx, qword ptr [r14]
0035C4B5  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
0035C4B9  48 8B 00                        mov rax, qword ptr [rax]
0035C4BC  48 C1 E8 08                     shr rax, 8
0035C4C0  3C 01                           cmp al, 1
0035C4C2  0F 85 45 0F 00 00               jne 0x14035d40d
0035C4C8  8B 05 EE E2 B9 00               mov eax, dword ptr [rip + 0xb9e2ee]
0035C4CE  85 C0                           test eax, eax
0035C4D0  0F 85 10 F9 FF FF               jne 0x14035bde6
0035C4D6  48 8B 49 38                     mov rcx, qword ptr [rcx + 0x38]
0035C4DA  E8 C1 9F FC FF                  call 0x1403264a0
0035C4DF  E9 02 F9 FF FF                  jmp 0x14035bde6
0035C4E4  41 0F B7 87 84 03 00 00         movzx eax, word ptr [r15 + 0x384]
0035C4EC  49 3B F0                        cmp rsi, r8
0035C4EF  49 8B F8                        mov rdi, r8
0035C4F2  48 0F 47 FE                     cmova rdi, rsi
0035C4F6  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
0035C4FA  48 3B F8                        cmp rdi, rax
0035C4FD  0F 83 7C 14 00 00               jae 0x14035d97f
0035C503  8D 4F 0F                        lea ecx, [rdi + 0xf]
0035C506  41 B9 01 00 00 00               mov r9d, 1
0035C50C  C1 E9 04                        shr ecx, 4
0035C50F  48 8D 05 EA 3A CA FF            lea rax, [rip - 0x35c516]
0035C516  4D 8D 9F 40 03 00 00            lea r11, [r15 + 0x340]
0035C51D  45 8B 53 4C                     mov r10d, dword ptr [r11 + 0x4c]
0035C521  41 8B D2                        mov edx, r10d
0035C524  49 C1 EA 04                     shr r10, 4
0035C528  0F B6 84 01 80 0B 01 00         movzx eax, byte ptr [rcx + rax + 0x10b80]
0035C530  41 81 E2 FF 01 00 00            and r10d, 0x1ff
0035C537  FF C8                           dec eax
0035C539  C1 EA 0D                        shr edx, 0xd
0035C53C  81 E2 FF FF 03 00               and edx, 0x3ffff
0035C542  89 85 70 01 00 00               mov dword ptr [rbp + 0x170], eax
0035C548  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0035C551  0F BD CA                        bsr ecx, edx
0035C554  4C 8B 80 B0 8B 00 00            mov r8, qword ptr [rax + 0x8bb0]
0035C55B  41 D3 E1                        shl r9d, cl
0035C55E  83 C1 FE                        add ecx, -2
0035C561  89 4D 10                        mov dword ptr [rbp + 0x10], ecx
0035C564  44 33 CA                        xor r9d, edx
0035C567  49 8B 0C C8                     mov rcx, qword ptr [r8 + rcx*8]
0035C56B  4A 8B 4C C9 08                  mov rcx, qword ptr [rcx + r9*8 + 8]
0035C570  4A 8B 04 D1                     mov rax, qword ptr [rcx + r10*8]
0035C574  48 85 C0                        test rax, rax
0035C577  0F 84 65 24 00 00               je 0x14035e9e2
0035C57D  8B 95 70 01 00 00               mov edx, dword ptr [rbp + 0x170]
0035C583  0F B7 D8                        movzx ebx, ax
0035C586  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0035C58A  8B C2                           mov eax, edx
0035C58C  48 03 C0                        add rax, rax
0035C58F  C1 E3 06                        shl ebx, 6
0035C592  49 03 DB                        add rbx, r11
0035C595  48 89 85 70 01 00 00            mov qword ptr [rbp + 0x170], rax
0035C59C  0F B7 04 18                     movzx eax, word ptr [rax + rbx]
0035C5A0  44 8B C0                        mov r8d, eax
0035C5A3  85 C0                           test eax, eax
0035C5A5  0F 84 C3 13 00 00               je 0x14035d96e
0035C5AB  41 C1 E0 06                     shl r8d, 6
0035C5AF  41 8B D0                        mov edx, r8d
0035C5B2  49 03 D3                        add rdx, r11
0035C5B5  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
0035C5BA  66 83 7A 04 00                  cmp word ptr [rdx + 4], 0
0035C5BF  0F 85 B7 66 38 00               jne 0x1406e2c7c
0035C5C5  C7 44 24 68 00 00 00 00         mov dword ptr [rsp + 0x68], 0
0035C5CD  0F 0D 4A 38                     prefetchw byte ptr [rdx + 0x38]
0035C5D1  48 8B 5A 38                     mov rbx, qword ptr [rdx + 0x38]
0035C5D5  41 BA 01 00 00 00               mov r10d, 1
0035C5DB  48 89 5D B8                     mov qword ptr [rbp - 0x48], rbx
0035C5DF  48 F7 C3 FF 0F 00 00            test rbx, 0xfff
0035C5E6  0F 84 6A 17 00 00               je 0x14035dd56
0035C5EC  48 8D 4B FF                     lea rcx, [rbx - 1]
0035C5F0  48 8B C3                        mov rax, rbx
0035C5F3  F0 48 0F B1 4A 38               lock cmpxchg qword ptr [rdx + 0x38], rcx
0035C5F9  0F 85 5C 12 00 00               jne 0x14035d85b
0035C5FF  65 4C 8B 0C 25 88 01 00 00      mov r9, qword ptr gs:[0x188]
0035C608  48 8B FB                        mov rdi, rbx
0035C60B  48 81 E7 00 F0 FF FF            and rdi, 0xfffffffffffff000
0035C612  48 8B C7                        mov rax, rdi
0035C615  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
0035C61A  48 C1 E8 0C                     shr rax, 0xc
0035C61E  49 8B 89 60 07 00 00            mov rcx, qword ptr [r9 + 0x760]
0035C625  33 47 28                        xor eax, dword ptr [rdi + 0x28]
0035C628  33 05 DA BC AC 00               xor eax, dword ptr [rip + 0xacbcda]
0035C62E  49 8B 91 68 07 00 00            mov rdx, qword ptr [r9 + 0x768]
0035C635  44 0F B6 57 18                  movzx r10d, byte ptr [rdi + 0x18]
0035C63A  89 45 D0                        mov dword ptr [rbp - 0x30], eax
0035C63D  41 83 EA 08                     sub r10d, 8
0035C641  0F B7 C0                        movzx eax, ax
0035C644  4C 8D 04 0A                     lea r8, [rdx + rcx]
0035C648  89 45 80                        mov dword ptr [rbp - 0x80], eax
0035C64B  48 33 D1                        xor rdx, rcx
0035C64E  49 C1 E8 20                     shr r8, 0x20
0035C652  48 C1 C1 18                     rol rcx, 0x18
0035C656  48 8B C2                        mov rax, rdx
0035C659  48 C1 E0 10                     shl rax, 0x10
0035C65D  48 33 C8                        xor rcx, rax
0035C660  48 33 CA                        xor rcx, rdx
0035C663  48 C1 C2 25                     rol rdx, 0x25
0035C667  49 89 89 60 07 00 00            mov qword ptr [r9 + 0x760], rcx
0035C66E  49 FF CA                        dec r10
0035C671  49 89 91 68 07 00 00            mov qword ptr [r9 + 0x768], rdx
0035C678  48 8D 4F 40                     lea rcx, [rdi + 0x40]
0035C67C  0F B6 47 32                     movzx eax, byte ptr [rdi + 0x32]
0035C680  89 45 A0                        mov dword ptr [rbp - 0x60], eax
0035C683  0F B6 47 27                     movzx eax, byte ptr [rdi + 0x27]
0035C687  4E 8D 14 D1                     lea r10, [rcx + r10*8]
0035C68B  45 0F B6 C8                     movzx r9d, r8b
0035C68F  88 85 70 01 00 00               mov byte ptr [rbp + 0x170], al
0035C695  0F B6 47 24                     movzx eax, byte ptr [rdi + 0x24]
0035C699  44 89 8D 78 01 00 00            mov dword ptr [rbp + 0x178], r9d
0035C6A0  4C 89 55 C0                     mov qword ptr [rbp - 0x40], r10
0035C6A4  4C 8D 04 C1                     lea r8, [rcx + rax*8]
0035C6A8  49 8B 10                        mov rdx, qword ptr [r8]
0035C6AB  48 F7 D2                        not rdx
0035C6AE  48 85 D2                        test rdx, rdx
0035C6B1  0F 84 D6 16 00 00               je 0x14035dd8d
0035C6B7  8B 05 6B BC AC 00               mov eax, dword ptr [rip + 0xacbc6b]
0035C6BD  A8 04                           test al, 4
0035C6BF  0F 85 24 15 00 00               jne 0x14035dbe9
0035C6C5  4D 3B C2                        cmp r8, r10
0035C6C8  44 8B 55 A0                     mov r10d, dword ptr [rbp - 0x60]
0035C6CC  0F 84 48 1E 00 00               je 0x14035e51a
0035C6D2  41 83 FA 40                     cmp r10d, 0x40
0035C6D6  0F 85 3E 1E 00 00               jne 0x14035e51a
0035C6DC  41 8B C9                        mov ecx, r9d
0035C6DF  48 D3 CA                        ror rdx, cl
0035C6E2  F3 4C 0F BC D2                  tzcnt r10, rdx
0035C6E7  45 03 D1                        add r10d, r9d
0035C6EA  41 83 E2 3F                     and r10d, 0x3f
0035C6EE  41 8B CA                        mov ecx, r10d
0035C6F1  41 B9 01 00 00 00               mov r9d, 1
0035C6F7  49 D3 E1                        shl r9, cl
0035C6FA  41 0F 0D 08                     prefetchw byte ptr [r8]
0035C6FE  49 8B 00                        mov rax, qword ptr [r8]
0035C701  48 8B C8                        mov rcx, rax
0035C704  49 0B C9                        or rcx, r9
0035C707  F0 49 0F B1 08                  lock cmpxchg qword ptr [r8], rcx
0035C70C  75 F3                           jne 0x14035c701
0035C70E  48 8B D0                        mov rdx, rax
0035C711  4C 85 C8                        test rax, r9
0035C714  0F 85 A2 14 00 00               jne 0x14035dbbc
0035C71A  44 8B 4D 80                     mov r9d, dword ptr [rbp - 0x80]
0035C71E  48 8D 47 40                     lea rax, [rdi + 0x40]
0035C722  44 2B C0                        sub r8d, eax
0035C725  43 8D 0C C2                     lea ecx, [r10 + r8*8]
0035C729  8B C1                           mov eax, ecx
0035C72B  89 8D 78 01 00 00               mov dword ptr [rbp + 0x178], ecx
0035C731  C1 E8 06                        shr eax, 6
0035C734  88 47 24                        mov byte ptr [rdi + 0x24], al
0035C737  8B F9                           mov edi, ecx
0035C739  0F B7 45 D2                     movzx eax, word ptr [rbp - 0x2e]
0035C73D  41 0F AF F9                     imul edi, r9d
0035C741  03 F8                           add edi, eax
0035C743  80 BD 70 01 00 00 01            cmp byte ptr [rbp + 0x170], 1
0035C74A  0F 86 2B 17 00 00               jbe 0x14035de7b
0035C750  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
0035C755  44 8B C7                        mov r8d, edi
0035C758  49 8B CB                        mov rcx, r11
0035C75B  E8 D0 DE F8 FF                  call 0x1402ea630
0035C760  4C 8B 54 24 30                  mov r10, qword ptr [rsp + 0x30]
0035C765  85 C0                           test eax, eax
0035C767  0F 88 4C 15 00 00               js 0x14035dcb9
0035C76D  49 03 FA                        add rdi, r10
0035C770  4D 85 E4                        test r12, r12
0035C773  75 17                           jne 0x14035c78c
0035C775  8B D6                           mov edx, esi
0035C777  48 8B CF                        mov rcx, rdi
0035C77A  48 83 C2 0F                     add rdx, 0xf
0035C77E  48 83 E2 F0                     and rdx, 0xfffffffffffffff0
0035C782  E8 89 F4 35 00                  call 0x1406bbc10
0035C787  4C 8B 54 24 30                  mov r10, qword ptr [rsp + 0x30]
0035C78C  48 85 FF                        test rdi, rdi
0035C78F  0F 84 65 15 00 00               je 0x14035dcfa
0035C795  4D 8D A7 40 03 00 00            lea r12, [r15 + 0x340]
0035C79C  83 7C 24 68 00                  cmp dword ptr [rsp + 0x68], 0
0035C7A1  0F 85 9F 2C 00 00               jne 0x14035f446
0035C7A7  8B DE                           mov ebx, esi
0035C7A9  44 8B 45 A8                     mov r8d, dword ptr [rbp - 0x58]
0035C7AD  48 83 FF FF                     cmp rdi, -1
0035C7B1  0F 85 74 F9 FF FF               jne 0x14035c12b
0035C7B7  48 8B 7D A8                     mov rdi, qword ptr [rbp - 0x58]
0035C7BB  E9 C4 11 00 00                  jmp 0x14035d984
0035C7C0  4D 8B EC                        mov r13, r12
0035C7C3  4D 85 E4                        test r12, r12
0035C7C6  0F 84 97 03 00 00               je 0x14035cb63
0035C7CC  E9 EC 2C 00 00                  jmp 0x14035f4bd
0035C7D1  CC                              int3
0035C7D2  8B 05 48 25 BA 00               mov eax, dword ptr [rip + 0xba2548]
0035C7D8  85 C0                           test eax, eax
0035C7DA  0F 85 48 02 00 00               jne 0x14035ca28
0035C7E0  49 F7 C4 FF 0F 00 00            test r12, 0xfff
0035C7E7  0F 84 4A 06 00 00               je 0x14035ce37
0035C7ED  41 0F B6 44 24 F3               movzx eax, byte ptr [r12 - 0xd]
0035C7F3  4D 8D 74 24 F0                  lea r14, [r12 - 0x10]
0035C7F8  A8 08                           test al, 8
0035C7FA  0F 85 39 07 00 00               jne 0x14035cf39
0035C800  41 F6 46 03 04                  test byte ptr [r14 + 3], 4
0035C805  74 1B                           je 0x14035c822
0035C807  41 0F B7 06                     movzx eax, word ptr [r14]
0035C80B  B9 FF 00 00 00                  mov ecx, 0xff
0035C810  66 23 C1                        and ax, cx
0035C813  0F B7 C0                        movzx eax, ax
0035C816  48 C1 E0 04                     shl rax, 4
0035C81A  4C 2B F0                        sub r14, rax
0035C81D  41 80 4E 03 04                  or byte ptr [r14 + 3], 4
0035C822  45 0F B6 46 03                  movzx r8d, byte ptr [r14 + 3]
0035C827  B9 00 01 00 00                  mov ecx, 0x100
0035C82C  41 8B 5E 04                     mov ebx, dword ptr [r14 + 4]
0035C830  41 F6 C0 01                     test r8b, 1
0035C834  B8 80 00 00 00                  mov eax, 0x80
0035C839  45 8B C8                        mov r9d, r8d
0035C83C  0F 44 C8                        cmove ecx, eax
0035C83F  8B D1                           mov edx, ecx
0035C841  48 83 CA 04                     or rdx, 4
0035C845  41 F6 C0 20                     test r8b, 0x20
0035C849  48 0F 44 D1                     cmove rdx, rcx
0035C84D  48 83 CA 02                     or rdx, 2
0035C851  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
0035C856  41 83 E1 08                     and r9d, 8
0035C85A  0F 85 B9 05 00 00               jne 0x14035ce19
0035C860  41 F6 C0 DE                     test r8b, 0xde
0035C864  74 4F                           je 0x14035c8b5
0035C866  48 8B CA                        mov rcx, rdx
0035C869  48 83 C9 08                     or rcx, 8
0035C86D  41 F6 C0 04                     test r8b, 4
0035C871  48 0F 44 CA                     cmove rcx, rdx
0035C875  48 8B D1                        mov rdx, rcx
0035C878  48 0F BA EA 09                  bts rdx, 9
0035C87D  44 84 C0                        test al, r8b
0035C880  48 0F 44 D1                     cmove rdx, rcx
0035C884  48 8B CA                        mov rcx, rdx
0035C887  48 0F BA E9 0A                  bts rcx, 0xa
0035C88C  41 F6 C0 40                     test r8b, 0x40
0035C890  48 0F 44 CA                     cmove rcx, rdx
0035C894  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0035C899  45 85 C9                        test r9d, r9d
0035C89C  75 17                           jne 0x14035c8b5
0035C89E  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0035C8A3  41 F6 C0 10                     test r8b, 0x10
0035C8A7  74 0C                           je 0x14035c8b5
0035C8A9  48 8B C1                        mov rax, rcx
0035C8AC  48 83 C8 20                     or rax, 0x20
0035C8B0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0035C8B5  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
0035C8BA  49 8D 7E 10                     lea rdi, [r14 + 0x10]
0035C8BE  44 0F B6 F8                     movzx r15d, al
0035C8C2  49 C1 E7 04                     shl r15, 4
0035C8C6  8B 05 04 A3 C6 00               mov eax, dword ptr [rip + 0xc6a304]
0035C8CC  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
0035C8D1  A9 07 02 00 00                  test eax, 0x207
0035C8D6  0F 85 55 1D 00 00               jne 0x14035e631
0035C8DC  8B 05 EE A2 C6 00               mov eax, dword ptr [rip + 0xc6a2ee]
0035C8E2  A8 10                           test al, 0x10
0035C8E4  74 10                           je 0x14035c8f6
0035C8E6  4D 8B CC                        mov r9, r12
0035C8E9  4D 8B C7                        mov r8, r15
0035C8EC  8B D3                           mov edx, ebx
0035C8EE  49 8B CE                        mov rcx, r14
0035C8F1  E8 E6 CD 85 00                  call 0x140bb96dc
0035C8F6  8B 05 50 88 C6 00               mov eax, dword ptr [rip + 0xc68850]
0035C8FC  44 89 6D A4                     mov dword ptr [rbp - 0x5c], r13d
0035C900  C6 44 24 3C 00                  mov byte ptr [rsp + 0x3c], 0
0035C905  C6 44 24 5C 00                  mov byte ptr [rsp + 0x5c], 0
0035C90A  3B D8                           cmp ebx, eax
0035C90C  75 01                           jne 0x14035c90f
0035C90E  CC                              int3
0035C90F  8B 05 EF A1 C6 00               mov eax, dword ptr [rip + 0xc6a1ef]
0035C915  A8 41                           test al, 0x41
0035C917  0F 85 A5 1D 00 00               jne 0x14035e6c2
0035C91D  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0035C925  4C 8B 05 2C 24 BA 00            mov r8, qword ptr [rip + 0xba242c]
0035C92C  8B C8                           mov ecx, eax
0035C92E  48 8D 05 CB 36 CA FF            lea rax, [rip - 0x35c935]
0035C935  4C 8B 9C C8 20 AD EF 00         mov r11, qword ptr [rax + rcx*8 + 0xefad20]
0035C93D  8B C3                           mov eax, ebx
0035C93F  48 69 C8 5F 9E 00 00            imul rcx, rax, 0x9e5f
0035C946  48 8B D1                        mov rdx, rcx
0035C949  48 C1 EA 20                     shr rdx, 0x20
0035C94D  33 D1                           xor edx, ecx
0035C94F  41 23 D0                        and edx, r8d
0035C952  44 8B D2                        mov r10d, edx
0035C955  8B C2                           mov eax, edx
0035C957  48 8D 0C 80                     lea rcx, [rax + rax*4]
0035C95B  48 03 C9                        add rcx, rcx
0035C95E  41 8B 04 CB                     mov eax, dword ptr [r11 + rcx*8]
0035C962  4D 8D 0C CB                     lea r9, [r11 + rcx*8]
0035C966  3B C3                           cmp eax, ebx
0035C968  0F 84 0B 02 00 00               je 0x14035cb79
0035C96E  85 C0                           test eax, eax
0035C970  0F 84 2C 0A 00 00               je 0x14035d3a2
0035C976  8D 42 01                        lea eax, [rdx + 1]
0035C979  41 23 C0                        and eax, r8d
0035C97C  8B D0                           mov edx, eax
0035C97E  41 3B C2                        cmp eax, r10d
0035C981  75 D2                           jne 0x14035c955
0035C983  0F 57 C0                        xorps xmm0, xmm0
0035C986  48 8D 0D 73 E3 B9 00            lea rcx, [rip + 0xb9e373]
0035C98D  0F 11 45 30                     movups xmmword ptr [rbp + 0x30], xmm0
0035C991  33 C0                           xor eax, eax
0035C993  48 89 4D 38                     mov qword ptr [rbp + 0x38], rcx
0035C997  4C 89 6D 30                     mov qword ptr [rbp + 0x30], r13
0035C99B  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
0035C99F  90                              nop
0035C9A0  44 0F 20 C7                     mov rdi, cr8
0035C9A4  B8 02 00 00 00                  mov eax, 2
0035C9A9  44 0F 22 C0                     mov cr8, rax
0035C9AD  83 3D 6C A3 C6 00 00            cmp dword ptr [rip + 0xc6a36c], 0
0035C9B4  0F 85 8B 09 00 00               jne 0x14035d345
0035C9BA  F6 05 45 A1 C6 00 21            test byte ptr [rip + 0xc6a145], 0x21
0035C9C1  40 88 7D 40                     mov byte ptr [rbp + 0x40], dil
0035C9C5  0F 85 0D 09 00 00               jne 0x14035d2d8
0035C9CB  48 8D 55 30                     lea rdx, [rbp + 0x30]
0035C9CF  48 87 15 2A E3 B9 00            xchg qword ptr [rip + 0xb9e32a], rdx
0035C9D6  48 85 D2                        test rdx, rdx
0035C9D9  0F 85 E9 0C 00 00               jne 0x14035d6c8
0035C9DF  4C 8B 05 62 23 BA 00            mov r8, qword ptr [rip + 0xba2362]
0035C9E6  41 8B D5                        mov edx, r13d
0035C9E9  4C 8B 0D 50 23 BA 00            mov r9, qword ptr [rip + 0xba2350]
0035C9F0  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0035C9F7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
0035CA00  8B C2                           mov eax, edx
0035CA02  49 3B C0                        cmp rax, r8
0035CA05  0F 83 79 0E 00 00               jae 0x14035d884
0035CA0B  48 8D 0C 80                     lea rcx, [rax + rax*4]
0035CA0F  48 C1 E1 04                     shl rcx, 4
0035CA13  49 03 C9                        add rcx, r9
0035CA16  8B 01                           mov eax, dword ptr [rcx]
0035CA18  3B C3                           cmp eax, ebx
0035CA1A  74 32                           je 0x14035ca4e
0035CA1C  85 C0                           test eax, eax
0035CA1E  0F 84 60 0E 00 00               je 0x14035d884
0035CA24  FF C2                           inc edx
0035CA26  EB D8                           jmp 0x14035ca00
0035CA28  48 8D 05 11 25 B9 00            lea rax, [rip + 0xb92511]
0035CA2F  48 8D 0D 2A 25 B9 00            lea rcx, [rip + 0xb9252a]
0035CA36  48 3B C1                        cmp rax, rcx
0035CA39  0F 8D A1 FD FF FF               jge 0x14035c7e0
0035CA3F  4C 3B 38                        cmp r15, qword ptr [rax]
0035CA42  0F 84 CC 21 00 00               je 0x14035ec14
0035CA48  48 83 C0 08                     add rax, 8
0035CA4C  EB E8                           jmp 0x14035ca36
0035CA4E  48 0F BA E6 08                  bt rsi, 8
0035CA53  0F 82 CE 03 00 00               jb 0x14035ce27
0035CA59  41 B9 01 00 00 00               mov r9d, 1
0035CA5F  4C 8D 41 08                     lea r8, [rcx + 8]
0035CA63  48 8D 41 18                     lea rax, [rcx + 0x18]
0035CA67  F0 48 FF 00                     lock inc qword ptr [rax]
0035CA6B  49 8B D7                        mov rdx, r15
0035CA6E  48 F7 DA                        neg rdx
0035CA71  F0 49 0F C1 10                  lock xadd qword ptr [r8], rdx
0035CA76  48 83 79 48 00                  cmp qword ptr [rcx + 0x48], 0
0035CA7B  0F 85 93 1C 00 00               jne 0x14035e714
0035CA81  48 8D 4D 30                     lea rcx, [rbp + 0x30]
0035CA85  E8 56 62 FE FF                  call 0x140342ce0
0035CA8A  48 0F BA E6 0A                  bt rsi, 0xa
0035CA8F  73 18                           jae 0x14035caa9
0035CA91  48 C1 EE 08                     shr rsi, 8
0035CA95  45 33 C9                        xor r9d, r9d
0035CA98  83 E6 01                        and esi, 1
0035CA9B  49 8B D7                        mov rdx, r15
0035CA9E  44 8B C6                        mov r8d, esi
0035CAA1  49 8B CC                        mov rcx, r12
0035CAA4  E8 17 C5 85 00                  call 0x140bb8fc0
0035CAA9  80 3D B8 21 C7 00 00            cmp byte ptr [rip + 0xc721b8], 0
0035CAB0  0F 85 64 0F 00 00               jne 0x14035da1a
0035CAB6  48 8B 5D 88                     mov rbx, qword ptr [rbp - 0x78]
0035CABA  49 8D 87 FF FD FF FF            lea rax, [r15 - 0x201]
0035CAC1  48 8D 35 38 35 CA FF            lea rsi, [rip - 0x35cac8]
0035CAC8  48 8B 53 38                     mov rdx, qword ptr [rbx + 0x38]
0035CACC  48 3D 7F 0D 00 00               cmp rax, 0xd7f
0035CAD2  0F 86 EA 12 00 00               jbe 0x14035ddc2
0035CAD8  66 45 85 F6                     test r14w, r14w
0035CADC  74 09                           je 0x14035cae7
0035CADE  48 81 C3 40 01 00 00            add rbx, 0x140
0035CAE5  EB 3F                           jmp 0x14035cb26
0035CAE7  49 8B D6                        mov rdx, r14
0035CAEA  48 8D 0D 1F BB B0 00            lea rcx, [rip + 0xb0bb1f]
0035CAF1  48 2B 15 10 BB B0 00            sub rdx, qword ptr [rip + 0xb0bb10]
0035CAF8  48 C1 EA 14                     shr rdx, 0x14
0035CAFC  48 03 D2                        add rdx, rdx
0035CAFF  E8 08 4E 00 00                  call 0x14036190c
0035CB04  48 85 C0                        test rax, rax
0035CB07  0F 84 9B 1C 00 00               je 0x14035e7a8
0035CB0D  83 F8 03                        cmp eax, 3
0035CB10  0F 84 92 1C 00 00               je 0x14035e7a8
0035CB16  48 81 C3 40 01 00 00            add rbx, 0x140
0035CB1D  83 F8 02                        cmp eax, 2
0035CB20  0F 84 7D 0F 00 00               je 0x14035daa3
0035CB26  4C 8B 0B                        mov r9, qword ptr [rbx]
0035CB29  49 8B D1                        mov rdx, r9
0035CB2C  49 23 D6                        and rdx, r14
0035CB2F  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
0035CB33  48 33 05 C6 B7 AC 00            xor rax, qword ptr [rip + 0xacb7c6]
0035CB3A  48 33 C2                        xor rax, rdx
0035CB3D  48 3B C3                        cmp rax, rbx
0035CB40  0F 84 BA 00 00 00               je 0x14035cc00
0035CB46  48 8B 53 38                     mov rdx, qword ptr [rbx + 0x38]
0035CB4A  45 33 C9                        xor r9d, r9d
0035CB4D  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0035CB52  4D 8B C6                        mov r8, r14
0035CB55  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0035CB5A  41 8D 49 09                     lea ecx, [r9 + 9]
0035CB5E  E8 59 EC FF FF                  call 0x14035b7bc
0035CB63  F6 44 24 78 20                  test byte ptr [rsp + 0x78], 0x20
0035CB68  0F 84 4F 29 00 00               je 0x14035f4bd
0035CB6E  B9 9A 00 00 C0                  mov ecx, 0xc000009a
0035CB73  E8 D8 9E F9 FF                  call 0x1402f6a50
0035CB78  CC                              int3
0035CB79  48 0F BA E6 08                  bt rsi, 8
0035CB7E  0F 83 73 07 00 00               jae 0x14035d2f7
0035CB84  45 8B C5                        mov r8d, r13d
0035CB87  49 8D 51 20                     lea rdx, [r9 + 0x20]
0035CB8B  49 8D 41 30                     lea rax, [r9 + 0x30]
0035CB8F  F0 48 FF 00                     lock inc qword ptr [rax]
0035CB93  49 8B CF                        mov rcx, r15
0035CB96  48 F7 D9                        neg rcx
0035CB99  F0 48 0F C1 0A                  lock xadd qword ptr [rdx], rcx
0035CB9E  49 83 79 48 00                  cmp qword ptr [r9 + 0x48], 0
0035CBA3  0F 84 E1 FE FF FF               je 0x14035ca8a
0035CBA9  41 8B C0                        mov eax, r8d
0035CBAC  41 F6 44 C1 38 01               test byte ptr [r9 + rax*8 + 0x38], 1
0035CBB2  4D 8D 1C C1                     lea r11, [r9 + rax*8]
0035CBB6  0F 85 CE FE FF FF               jne 0x14035ca8a
0035CBBC  49 8B 43 38                     mov rax, qword ptr [r11 + 0x38]
0035CBC0  4E 8D 14 BD 3F 00 00 00         lea r10, [r15*4 + 0x3f]
0035CBC8  49 83 E2 C0                     and r10, 0xffffffffffffffc0
0035CBCC  BB 80 00 00 00                  mov ebx, 0x80
0035CBD1  49 83 FA 40                     cmp r10, 0x40
0035CBD5  4C 0F 44 D3                     cmove r10, rbx
0035CBD9  49 8D 1C 0A                     lea rbx, [r10 + rcx]
0035CBDD  48 3B C8                        cmp rcx, rax
0035CBE0  0F 8D A4 FE FF FF               jge 0x14035ca8a
0035CBE6  48 3B D8                        cmp rbx, rax
0035CBE9  0F 8D 9B FE FF FF               jge 0x14035ca8a
0035CBEF  F0 49 0F B1 5B 38               lock cmpxchg qword ptr [r11 + 0x38], rbx
0035CBF5  0F 84 C5 1C 00 00               je 0x14035e8c0
0035CBFB  48 8B 0A                        mov rcx, qword ptr [rdx]
0035CBFE  EB D9                           jmp 0x14035cbd9
0035CC00  44 0F B6 53 08                  movzx r10d, byte ptr [rbx + 8]
0035CC05  45 8B C6                        mov r8d, r14d
0035CC08  44 2B C2                        sub r8d, edx
0035CC0B  41 8B CA                        mov ecx, r10d
0035CC0E  41 D3 E8                        shr r8d, cl
0035CC11  49 C1 E0 05                     shl r8, 5
0035CC15  4C 03 C2                        add r8, rdx
0035CC18  41 0F B6 40 1A                  movzx eax, byte ptr [r8 + 0x1a]
0035CC1D  48 F7 D8                        neg rax
0035CC20  48 C1 E0 05                     shl rax, 5
0035CC24  4C 03 C0                        add r8, rax
0035CC27  49 8B F8                        mov rdi, r8
0035CC2A  48 2B FA                        sub rdi, rdx
0035CC2D  48 C1 FF 05                     sar rdi, 5
0035CC31  45 0F B6 58 18                  movzx r11d, byte ptr [r8 + 0x18]
0035CC36  48 D3 E7                        shl rdi, cl
0035CC39  48 03 FA                        add rdi, rdx
0035CC3C  49 3B FE                        cmp rdi, r14
0035CC3F  0F 94 C0                        sete al
0035CC42  42 8D 0C 18                     lea ecx, [rax + r11]
0035CC46  80 F9 0B                        cmp cl, 0xb
0035CC49  0F 85 B9 05 00 00               jne 0x14035d208
0035CC4F  48 8B 73 18                     mov rsi, qword ptr [rbx + 0x18]
0035CC53  48 8B C7                        mov rax, rdi
0035CC56  0F B7 57 2C                     movzx edx, word ptr [rdi + 0x2c]
0035CC5A  45 8B C6                        mov r8d, r14d
0035CC5D  48 C1 E8 0C                     shr rax, 0xc
0035CC61  33 47 28                        xor eax, dword ptr [rdi + 0x28]
0035CC64  33 05 9E B6 AC 00               xor eax, dword ptr [rip + 0xacb69e]
0035CC6A  0F B7 C8                        movzx ecx, ax
0035CC6D  48 C1 E8 10                     shr rax, 0x10
0035CC71  48 03 C7                        add rax, rdi
0035CC74  48 C1 E2 06                     shl rdx, 6
0035CC78  44 2B C0                        sub r8d, eax
0035CC7B  41 8B C0                        mov eax, r8d
0035CC7E  8B 5C 32 48                     mov ebx, dword ptr [rdx + rsi + 0x48]
0035CC82  48 0F AF D8                     imul rbx, rax
0035CC86  48 C1 EB 20                     shr rbx, 0x20
0035CC8A  8B C3                           mov eax, ebx
0035CC8C  0F AF C1                        imul eax, ecx
0035CC8F  44 3B C0                        cmp r8d, eax
0035CC92  0F 85 CB FE FF FF               jne 0x14035cb63
0035CC98  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
0035CCA1  41 B9 01 00 00 00               mov r9d, 1
0035CCA7  44 8B 46 4C                     mov r8d, dword ptr [rsi + 0x4c]
0035CCAB  41 8B C0                        mov eax, r8d
0035CCAE  C1 E8 0D                        shr eax, 0xd
0035CCB1  25 FF FF 03 00                  and eax, 0x3ffff
0035CCB6  49 C1 E8 04                     shr r8, 4
0035CCBA  0F BD C8                        bsr ecx, eax
0035CCBD  41 81 E0 FF 01 00 00            and r8d, 0x1ff
0035CCC4  41 D3 E1                        shl r9d, cl
0035CCC7  83 C1 FE                        add ecx, -2
0035CCCA  44 33 C8                        xor r9d, eax
0035CCCD  89 4D 20                        mov dword ptr [rbp + 0x20], ecx
0035CCD0  48 8B 82 B0 8B 00 00            mov rax, qword ptr [rdx + 0x8bb0]
0035CCD7  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
0035CCDB  4A 8B 44 C8 08                  mov rax, qword ptr [rax + r9*8 + 8]
0035CCE0  4A 8B 04 C0                     mov rax, qword ptr [rax + r8*8]
0035CCE4  48 85 C0                        test rax, rax
0035CCE7  0F 84 5E 1C 00 00               je 0x14035e94b
0035CCED  66 3B 47 2E                     cmp ax, word ptr [rdi + 0x2e]
0035CCF1  0F 84 E7 1B 00 00               je 0x14035e8de
0035CCF7  8B C3                           mov eax, ebx
0035CCF9  4C 8B C3                        mov r8, rbx
0035CCFC  83 E0 3F                        and eax, 0x3f
0035CCFF  0F B6 D0                        movzx edx, al
0035CD02  48 8B C3                        mov rax, rbx
0035CD05  48 C1 E8 06                     shr rax, 6
0035CD09  48 8B 44 C7 40                  mov rax, qword ptr [rdi + rax*8 + 0x40]
0035CD0E  48 0F A3 D0                     bt rax, rdx
0035CD12  0F 83 55 06 00 00               jae 0x14035d36d
0035CD18  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0035CD1C  48 8B C8                        mov rcx, rax
0035CD1F  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
0035CD23  48 C1 E9 30                     shr rcx, 0x30
0035CD27  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0035CD2C  80 F9 01                        cmp cl, 1
0035CD2F  75 05                           jne 0x14035cd36
0035CD31  C6 44 24 36 02                  mov byte ptr [rsp + 0x36], 2
0035CD36  4D 85 F6                        test r14, r14
0035CD39  74 2E                           je 0x14035cd69
0035CD3B  4C 8B 46 50                     mov r8, qword ptr [rsi + 0x50]
0035CD3F  0F B7 4C 24 30                  movzx ecx, word ptr [rsp + 0x30]
0035CD44  41 8B D0                        mov edx, r8d
0035CD47  66 41 89 0E                     mov word ptr [r14], cx
0035CD4B  41 33 16                        xor edx, dword ptr [r14]
0035CD4E  0F B6 C9                        movzx ecx, cl
0035CD51  D3 C2                           rol edx, cl
0035CD53  8D 4B 01                        lea ecx, [rbx + 1]
0035CD56  49 C1 E8 20                     shr r8, 0x20
0035CD5A  41 33 D0                        xor edx, r8d
0035CD5D  66 89 4C 24 30                  mov word ptr [rsp + 0x30], cx
0035CD62  41 33 D6                        xor edx, r14d
0035CD65  41 89 56 08                     mov dword ptr [r14 + 8], edx
0035CD69  66 FF 44 24 32                  inc word ptr [rsp + 0x32]
0035CD6E  0F B7 57 2C                     movzx edx, word ptr [rdi + 0x2c]
0035CD72  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0035CD77  48 C1 E2 06                     shl rdx, 6
0035CD7B  F0 48 0F B1 4F 10               lock cmpxchg qword ptr [rdi + 0x10], rcx
0035CD81  75 99                           jne 0x14035cd1c
0035CD83  80 7C 32 5C 00                  cmp byte ptr [rdx + rsi + 0x5c], 0
0035CD88  0F 84 47 06 00 00               je 0x14035d3d5
0035CD8E  80 7D AE 01                     cmp byte ptr [rbp - 0x52], 1
0035CD92  0F 85 CB FD FF FF               jne 0x14035cb63
0035CD98  44 0F B7 4D AC                  movzx r9d, word ptr [rbp - 0x54]
0035CD9D  41 C1 E1 06                     shl r9d, 6
0035CDA1  4C 03 CE                        add r9, rsi
0035CDA4  41 0F 0D 49 08                  prefetchw byte ptr [r9 + 8]
0035CDA9  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
0035CDAD  4C 8B 57 18                     mov r10, qword ptr [rdi + 0x18]
0035CDB1  48 8B D0                        mov rdx, rax
0035CDB4  81 E2 FF 0F 00 00               and edx, 0xfff
0035CDBA  4D 8B C2                        mov r8, r10
0035CDBD  41 81 E0 FF 0F 00 00            and r8d, 0xfff
0035CDC4  48 8B C8                        mov rcx, rax
0035CDC7  48 2B CA                        sub rcx, rdx
0035CDCA  49 0B C8                        or rcx, r8
0035CDCD  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
0035CDD1  48 8B CF                        mov rcx, rdi
0035CDD4  48 0B CA                        or rcx, rdx
0035CDD7  F0 49 0F B1 49 08               lock cmpxchg qword ptr [r9 + 8], rcx
0035CDDD  0F 84 80 FD FF FF               je 0x14035cb63
0035CDE3  48 8B D0                        mov rdx, rax
0035CDE6  48 8B C8                        mov rcx, rax
0035CDE9  49 33 CA                        xor rcx, r10
0035CDEC  81 E2 FF 0F 00 00               and edx, 0xfff
0035CDF2  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
0035CDF9  4C 8B C0                        mov r8, rax
0035CDFC  49 33 CA                        xor rcx, r10
0035CDFF  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
0035CE03  48 8B CF                        mov rcx, rdi
0035CE06  48 0B CA                        or rcx, rdx
0035CE09  F0 49 0F B1 49 08               lock cmpxchg qword ptr [r9 + 8], rcx
0035CE0F  49 3B C0                        cmp rax, r8
0035CE12  75 CF                           jne 0x14035cde3
0035CE14  E9 4A FD FF FF                  jmp 0x14035cb63
0035CE19  48 83 CA 01                     or rdx, 1
0035CE1D  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
0035CE22  E9 39 FA FF FF                  jmp 0x14035c860
0035CE27  45 8B CD                        mov r9d, r13d
0035CE2A  4C 8D 41 20                     lea r8, [rcx + 0x20]
0035CE2E  48 8D 41 30                     lea rax, [rcx + 0x30]
0035CE32  E9 30 FC FF FF                  jmp 0x14035ca67
0035CE37  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
0035CE41  4C 3B E0                        cmp r12, rax
0035CE44  72 21                           jb 0x14035ce67
0035CE46  49 8B C4                        mov rax, r12
0035CE49  48 C1 E8 27                     shr rax, 0x27
0035CE4D  25 FF 01 00 00                  and eax, 0x1ff
0035CE52  05 00 FF FF FF                  add eax, 0xffffff00
0035CE57  0F B6 84 38 A8 8A E3 00         movzx eax, byte ptr [rax + rdi + 0xe38aa8]
0035CE5F  3C 05                           cmp al, 5
0035CE61  0F 84 54 22 00 00               je 0x14035f0bb
0035CE67  41 BE 40 00 00 00               mov r14d, 0x40
0035CE6D  4C 89 AD A8 00 00 00            mov qword ptr [rbp + 0xa8], r13
0035CE74  4C 89 AD B0 00 00 00            mov qword ptr [rbp + 0xb0], r13
0035CE7B  4C 89 AD B8 00 00 00            mov qword ptr [rbp + 0xb8], r13
0035CE82  45 0F 20 C7                     mov r15, cr8
0035CE86  B8 02 00 00 00                  mov eax, 2
0035CE8B  44 0F 22 C0                     mov cr8, rax
0035CE8F  83 3D 8A 9E C6 00 00            cmp dword ptr [rip + 0xc69e8a], 0
0035CE96  0F 85 60 05 00 00               jne 0x14035d3fc
0035CE9C  F6 05 63 9C C6 00 21            test byte ptr [rip + 0xc69c63], 0x21
0035CEA3  0F 84 61 04 00 00               je 0x14035d30a
0035CEA9  8B 05 A9 0F BB 00               mov eax, dword ptr [rip + 0xbb0fa9]
0035CEAF  85 C0                           test eax, eax
0035CEB1  0F 85 53 04 00 00               jne 0x14035d30a
0035CEB7  41 0F B6 D7                     movzx edx, r15b
0035CEBB  48 8D 0D 36 DE B9 00            lea rcx, [rip + 0xb9de36]
0035CEC2  E8 59 FE F1 FF                  call 0x14027cd20
0035CEC7  4C 8B 05 6A 1E BA 00            mov r8, qword ptr [rip + 0xba1e6a]
0035CECE  49 8B C4                        mov rax, r12
0035CED1  4C 8B 0D 58 1E BA 00            mov r9, qword ptr [rip + 0xba1e58]
0035CED8  41 BA 01 00 00 00               mov r10d, 1
0035CEDE  48 C1 E8 0C                     shr rax, 0xc
0035CEE2  48 69 C8 5F 9E 00 00            imul rcx, rax, 0x9e5f
0035CEE9  41 8D 50 FF                     lea edx, [r8 - 1]
0035CEED  48 8B C1                        mov rax, rcx
0035CEF0  48 C1 E8 20                     shr rax, 0x20
0035CEF4  48 33 C8                        xor rcx, rax
0035CEF7  23 D1                           and edx, ecx
0035CEF9  8B CA                           mov ecx, edx
0035CEFB  48 C1 E1 05                     shl rcx, 5
0035CEFF  49 03 C9                        add rcx, r9
0035CF02  48 8B 01                        mov rax, qword ptr [rcx]
0035CF05  49 3B C4                        cmp rax, r12
0035CF08  0F 84 32 02 00 00               je 0x14035d140
0035CF0E  FF C2                           inc edx
0035CF10  8B C2                           mov eax, edx
0035CF12  49 3B C0                        cmp rax, r8
0035CF15  72 E2                           jb 0x14035cef9
0035CF17  45 85 D2                        test r10d, r10d
0035CF1A  0F 85 4A 18 00 00               jne 0x14035e76a
0035CF20  BA 22 00 00 00                  mov edx, 0x22
0035CF25  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0035CF2A  4D 8B CE                        mov r9, r14
0035CF2D  4D 8B C4                        mov r8, r12
0035CF30  8D 4A F7                        lea ecx, [rdx - 9]
0035CF33  E8 28 07 1A 00                  call 0x1404fd660
0035CF38  CC                              int3
0035CF39  49 8B CE                        mov rcx, r14
0035CF3C  BB FF 00 00 00                  mov ebx, 0xff
0035CF41  A8 04                           test al, 4
0035CF43  74 11                           je 0x14035cf56
0035CF45  41 0F B7 06                     movzx eax, word ptr [r14]
0035CF49  66 23 C3                        and ax, bx
0035CF4C  0F B7 C0                        movzx eax, ax
0035CF4F  48 C1 E0 04                     shl rax, 4
0035CF53  48 2B C8                        sub rcx, rax
0035CF56  48 33 49 08                     xor rcx, qword ptr [rcx + 8]
0035CF5A  48 33 0D C7 A2 C6 00            xor rcx, qword ptr [rip + 0xc6a2c7]
0035CF61  0F 84 99 F8 FF FF               je 0x14035c800
0035CF67  48 83 F9 FF                     cmp rcx, -1
0035CF6B  0F 84 8F F8 FF FF               je 0x14035c800
0035CF71  8B 05 A9 1D BA 00               mov eax, dword ptr [rip + 0xba1da9]
0035CF77  85 C0                           test eax, eax
0035CF79  0F 85 14 18 00 00               jne 0x14035e793
0035CF7F  49 B8 00 00 00 00 00 80 FF FF   movabs r8, 0xffff800000000000
0035CF89  4D 3B E0                        cmp r12, r8
0035CF8C  72 21                           jb 0x14035cfaf
0035CF8E  49 8B C4                        mov rax, r12
0035CF91  48 C1 E8 27                     shr rax, 0x27
0035CF95  25 FF 01 00 00                  and eax, 0x1ff
0035CF9A  05 00 FF FF FF                  add eax, 0xffffff00
0035CF9F  0F B6 84 38 A8 8A E3 00         movzx eax, byte ptr [rax + rdi + 0xe38aa8]
0035CFA7  3C 05                           cmp al, 5
0035CFA9  0F 84 F9 20 00 00               je 0x14035f0a8
0035CFAF  41 BE 40 00 00 00               mov r14d, 0x40
0035CFB5  41 F6 44 24 F3 04               test byte ptr [r12 - 0xd], 4
0035CFBB  49 8D 54 24 F0                  lea rdx, [r12 - 0x10]
0035CFC0  74 10                           je 0x14035cfd2
0035CFC2  0F B7 02                        movzx eax, word ptr [rdx]
0035CFC5  66 23 C3                        and ax, bx
0035CFC8  0F B7 C0                        movzx eax, ax
0035CFCB  48 C1 E0 04                     shl rax, 4
0035CFCF  48 2B D0                        sub rdx, rax
0035CFD2  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
0035CFD6  8B 72 04                        mov esi, dword ptr [rdx + 4]
0035CFD9  0F B6 D8                        movzx ebx, al
0035CFDC  48 C1 E3 04                     shl rbx, 4
0035CFE0  66 C1 E8 08                     shr ax, 8
0035CFE4  A8 08                           test al, 8
0035CFE6  0F 84 4A 01 00 00               je 0x14035d136
0035CFEC  48 8B 3D 35 A2 C6 00            mov rdi, qword ptr [rip + 0xc6a235]
0035CFF3  48 8B C2                        mov rax, rdx
0035CFF6  48 33 7A 08                     xor rdi, qword ptr [rdx + 8]
0035CFFA  48 33 05 27 A2 C6 00            xor rax, qword ptr [rip + 0xc6a227]
0035D001  48 89 42 08                     mov qword ptr [rdx + 8], rax
0035D005  48 33 FA                        xor rdi, rdx
0035D008  0F 84 28 01 00 00               je 0x14035d136
0035D00E  48 83 FF FF                     cmp rdi, -1
0035D012  0F 84 1E 01 00 00               je 0x14035d136
0035D018  49 3B F8                        cmp rdi, r8
0035D01B  0F 82 6B 16 00 00               jb 0x14035e68c
0035D021  0F B6 07                        movzx eax, byte ptr [rdi]
0035D024  24 7F                           and al, 0x7f
0035D026  3C 03                           cmp al, 3
0035D028  0F 85 5E 16 00 00               jne 0x14035e68c
0035D02E  41 81 E6 00 01 00 00            and r14d, 0x100
0035D035  48 3B 3D 74 9A C6 00            cmp rdi, qword ptr [rip + 0xc69a74]
0035D03C  0F 84 C2 00 00 00               je 0x14035d104
0035D042  41 8B C5                        mov eax, r13d
0035D045  4C 8D 0D B4 2F CA FF            lea r9, [rip - 0x35d04c]
0035D04C  4D 85 F6                        test r14, r14
0035D04F  0F 95 C0                        setne al
0035D052  44 8B E0                        mov r12d, eax
0035D055  48 8B 87 F8 02 00 00            mov rax, qword ptr [rdi + 0x2f8]
0035D05C  45 8B FC                        mov r15d, r12d
0035D05F  49 C1 E7 07                     shl r15, 7
0035D063  4C 03 F8                        add r15, rax
0035D066  48 89 85 70 01 00 00            mov qword ptr [rbp + 0x170], rax
0035D06D  47 0F B6 AC E1 50 73 FC 00      movzx r13d, byte ptr [r9 + r12*8 + 0xfc7350]
0035D076  41 0F 0D 0F                     prefetchw byte ptr [r15]
0035D07A  4D 8B 37                        mov r14, qword ptr [r15]
0035D07D  49 8B 47 40                     mov rax, qword ptr [r15 + 0x40]
0035D081  49 83 7F 50 00                  cmp qword ptr [r15 + 0x50], 0
0035D086  74 20                           je 0x14035d0a8
0035D088  4D 6B C4 38                     imul r8, r12, 0x38
0035D08C  49 3B C6                        cmp rax, r14
0035D08F  76 17                           jbe 0x14035d0a8
0035D091  4B 8B 94 08 48 66 F0 00         mov rdx, qword ptr [r8 + r9 + 0xf06648]
0035D099  48 8B C8                        mov rcx, rax
0035D09C  49 2B CE                        sub rcx, r14
0035D09F  48 3B CA                        cmp rcx, rdx
0035D0A2  0F 87 35 05 00 00               ja 0x14035d5dd
0035D0A8  4D 8B D4                        mov r10, r12
0035D0AB  4C 8D 1D CE AE AC 00            lea r11, [rip + 0xacaece]
0035D0B2  49 C1 E2 07                     shl r10, 7
0035D0B6  4C 8B CB                        mov r9, rbx
0035D0B9  49 3B DE                        cmp rbx, r14
0035D0BC  4D 8B C6                        mov r8, r14
0035D0BF  49 8B CE                        mov rcx, r14
0035D0C2  49 8B C6                        mov rax, r14
0035D0C5  4C 0F 42 C3                     cmovb r8, rbx
0035D0C9  48 2B CB                        sub rcx, rbx
0035D0CC  33 D2                           xor edx, edx
0035D0CE  49 3B DE                        cmp rbx, r14
0035D0D1  48 0F 42 D1                     cmovb rdx, rcx
0035D0D5  F0 49 0F B1 17                  lock cmpxchg qword ptr [r15], rdx
0035D0DA  4C 8B F0                        mov r14, rax
0035D0DD  75 DA                           jne 0x14035d0b9
0035D0DF  49 2B D8                        sub rbx, r8
0035D0E2  0F 85 0F 09 00 00               jne 0x14035d9f7
0035D0E8  41 F6 C5 04                     test r13b, 4
0035D0EC  74 0C                           je 0x14035d0fa
0035D0EE  49 F7 D9                        neg r9
0035D0F1  F0 4E 01 8C E7 00 02 00 00      lock add qword ptr [rdi + r12*8 + 0x200], r9
0035D0FA  4C 8B A5 78 01 00 00            mov r12, qword ptr [rbp + 0x178]
0035D101  45 33 ED                        xor r13d, r13d
0035D104  83 3D 05 7F C6 00 00            cmp dword ptr [rip + 0xc67f05], 0
0035D10B  74 12                           je 0x14035d11f
0035D10D  33 D2                           xor edx, edx
0035D10F  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0035D113  44 8B CE                        mov r9d, esi
0035D116  44 8D 42 01                     lea r8d, [rdx + 1]
0035D11A  E8 C5 38 EB FF                  call 0x1402109e4
0035D11F  48 C7 C6 FF FF FF FF            mov rsi, 0xffffffffffffffff
0035D126  F0 48 0F C1 77 D0               lock xadd qword ptr [rdi - 0x30], rsi
0035D12C  48 83 EE 01                     sub rsi, 1
0035D130  0F 8E 6D 0D 00 00               jle 0x14035dea3
0035D136  4D 8D 74 24 F0                  lea r14, [r12 - 0x10]
0035D13B  E9 C0 F6 FF FF                  jmp 0x14035c800
0035D140  48 85 C9                        test rcx, rcx
0035D143  0F 84 D7 FD FF FF               je 0x14035cf20
0035D149  48 8D 05 B0 1F C7 00            lea rax, [rip + 0xc71fb0]
0035D150  4C 89 8D A8 00 00 00            mov qword ptr [rbp + 0xa8], r9
0035D157  48 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], rax
0035D15E  48 C7 C6 FF FF FF FF            mov rsi, 0xffffffffffffffff
0035D165  4C 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], r8
0035D16C  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
0035D16F  44 8B F0                        mov r14d, eax
0035D172  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
0035D176  8B 59 08                        mov ebx, dword ptr [rcx + 8]
0035D179  49 C1 EE 08                     shr r14, 8
0035D17D  41 81 E6 FF 0F 00 00            and r14d, 0xfff
0035D184  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
0035D189  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
0035D18E  0F BA E0 08                     bt eax, 8
0035D192  0F 82 F7 01 00 00               jb 0x14035d38f
0035D198  48 8B FE                        mov rdi, rsi
0035D19B  8B C6                           mov eax, esi
0035D19D  F0 0F C1 05 5B 1F C7 00         lock xadd dword ptr [rip + 0xc71f5b], eax
0035D1A5  4C 89 69 18                     mov qword ptr [rcx + 0x18], r13
0035D1A9  F0 48 FF 01                     lock inc qword ptr [rcx]
0035D1AD  F6 05 52 99 C6 00 01            test byte ptr [rip + 0xc69952], 1
0035D1B4  0F 85 82 0C 00 00               jne 0x14035de3c
0035D1BA  F0 81 25 33 DB B9 00 FF FF FF BF  lock and dword ptr [rip + 0xb9db33], 0xbfffffff
0035D1C5  F0 FF 0D 2C DB B9 00            lock dec dword ptr [rip + 0xb9db2c]
0035D1CC  83 3D 4D 9B C6 00 00            cmp dword ptr [rip + 0xc69b4d], 0
0035D1D3  74 0D                           je 0x14035d1e2
0035D1D5  44 0F 20 C1                     mov rcx, cr8
0035D1D9  41 0F B6 D7                     movzx edx, r15b
0035D1DD  E8 B6 84 19 00                  call 0x1404f5698
0035D1E2  41 0F B6 C7                     movzx eax, r15b
0035D1E6  44 0F 22 C0                     mov cr8, rax
0035D1EA  48 8D 47 FF                     lea rax, [rdi - 1]
0035D1EE  48 83 F8 FD                     cmp rax, -3
0035D1F2  0F 86 DE 04 00 00               jbe 0x14035d6d6
0035D1F8  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
0035D1FD  4D 8B F4                        mov r14, r12
0035D200  49 8B FC                        mov rdi, r12
0035D203  E9 BE F6 FF FF                  jmp 0x14035c8c6
0035D208  4D 23 C8                        and r9, r8
0035D20B  44 89 6D D8                     mov dword ptr [rbp - 0x28], r13d
0035D20F  49 8B D0                        mov rdx, r8
0035D212  41 8B CA                        mov ecx, r10d
0035D215  49 2B D1                        sub rdx, r9
0035D218  41 0F B6 C3                     movzx eax, r11b
0035D21C  48 C1 FA 05                     sar rdx, 5
0035D220  24 03                           and al, 3
0035D222  48 D3 E2                        shl rdx, cl
0035D225  49 03 D1                        add rdx, r9
0035D228  3C 03                           cmp al, 3
0035D22A  0F 85 16 F9 FF FF               jne 0x14035cb46
0035D230  4C 3B F2                        cmp r14, rdx
0035D233  0F 84 24 01 00 00               je 0x14035d35d
0035D239  41 80 FB 0F                     cmp r11b, 0xf
0035D23D  0F 85 03 F9 FF FF               jne 0x14035cb46
0035D243  4C 3B F2                        cmp r14, rdx
0035D246  0F 86 11 01 00 00               jbe 0x14035d35d
0035D24C  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
0035D250  4C 8D 4D D8                     lea r9, [rbp - 0x28]
0035D254  4D 8B C6                        mov r8, r14
0035D257  E8 D4 43 00 00                  call 0x140361630
0035D25C  85 C0                           test eax, eax
0035D25E  0F 84 FF F8 FF FF               je 0x14035cb63
0035D264  4C 8B 43 18                     mov r8, qword ptr [rbx + 0x18]
0035D268  8B 4D D8                        mov ecx, dword ptr [rbp - 0x28]
0035D26B  41 0F B7 40 44                  movzx eax, word ptr [r8 + 0x44]
0035D270  3B C8                           cmp ecx, eax
0035D272  0F 83 EB F8 FF FF               jae 0x14035cb63
0035D278  83 C1 0F                        add ecx, 0xf
0035D27B  48 C1 E9 04                     shr rcx, 4
0035D27F  44 0F B6 94 31 80 0B 01 00      movzx r10d, byte ptr [rcx + rsi + 0x10b80]
0035D288  41 FF CA                        dec r10d
0035D28B  4F 8D 0C D0                     lea r9, [r8 + r10*8]
0035D28F  49 8B 89 C0 01 00 00            mov rcx, qword ptr [r9 + 0x1c0]
0035D296  48 8B C1                        mov rax, rcx
0035D299  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
0035D29D  48 C1 E8 10                     shr rax, 0x10
0035D2A1  48 8B D1                        mov rdx, rcx
0035D2A4  F6 C1 01                        test cl, 1
0035D2A7  74 22                           je 0x14035d2cb
0035D2A9  66 83 F8 01                     cmp ax, 1
0035D2AD  76 0B                           jbe 0x14035d2ba
0035D2AF  66 FF C8                        dec ax
0035D2B2  66 89 45 CA                     mov word ptr [rbp - 0x36], ax
0035D2B6  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
0035D2BA  48 8B C1                        mov rax, rcx
0035D2BD  F0 49 0F B1 91 C0 01 00 00      lock cmpxchg qword ptr [r9 + 0x1c0], rdx
0035D2C6  48 3B C1                        cmp rax, rcx
0035D2C9  75 C4                           jne 0x14035d28f
0035D2CB  4B 8B 8C D0 C0 01 00 00         mov rcx, qword ptr [r8 + r10*8 + 0x1c0]
0035D2D3  E9 8B F8 FF FF                  jmp 0x14035cb63
0035D2D8  8B 05 7A 0B BB 00               mov eax, dword ptr [rip + 0xbb0b7a]
0035D2DE  85 C0                           test eax, eax
0035D2E0  0F 85 E5 F6 FF FF               jne 0x14035c9cb
0035D2E6  48 8B D1                        mov rdx, rcx
0035D2E9  48 8D 4D 30                     lea rcx, [rbp + 0x30]
0035D2ED  E8 5E 85 F1 FF                  call 0x140275850
0035D2F2  E9 E8 F6 FF FF                  jmp 0x14035c9df
0035D2F7  41 B8 01 00 00 00               mov r8d, 1
0035D2FD  49 8D 51 08                     lea rdx, [r9 + 8]
0035D301  49 8D 41 18                     lea rax, [r9 + 0x18]
0035D305  E9 85 F8 FF FF                  jmp 0x14035cb8f
0035D30A  0F 0D 0D E7 D9 B9 00            prefetchw byte ptr [rip + 0xb9d9e7]
0035D311  8B 05 E1 D9 B9 00               mov eax, dword ptr [rip + 0xb9d9e1]
0035D317  0F BA F0 1F                     btr eax, 0x1f
0035D31B  8D 48 01                        lea ecx, [rax + 1]
0035D31E  F0 0F B1 0D D2 D9 B9 00         lock cmpxchg dword ptr [rip + 0xb9d9d2], ecx
0035D326  0F 84 9B FB FF FF               je 0x14035cec7
0035D32C  85 C0                           test eax, eax
0035D32E  79 EB                           jns 0x14035d31b
0035D330  41 0F B6 D7                     movzx edx, r15b
0035D334  48 8D 0D BD D9 B9 00            lea rcx, [rip + 0xb9d9bd]
0035D33B  E8 40 50 00 00                  call 0x140362380
0035D340  E9 82 FB FF FF                  jmp 0x14035cec7
0035D345  0F B6 D0                        movzx edx, al
0035D348  40 0F B6 CF                     movzx ecx, dil
0035D34C  E8 AB 83 19 00                  call 0x1404f56fc
0035D351  48 8D 0D A8 D9 B9 00            lea rcx, [rip + 0xb9d9a8]
0035D358  E9 5D F6 FF FF                  jmp 0x14035c9ba
0035D35D  49 8B D0                        mov rdx, r8
0035D360  48 8B CB                        mov rcx, rbx
0035D363  E8 38 5C F8 FF                  call 0x1402e2fa0
0035D368  E9 F6 F7 FF FF                  jmp 0x14035cb63
0035D36D  48 8B 16                        mov rdx, qword ptr [rsi]
0035D370  4C 8B CF                        mov r9, rdi
0035D373  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0035D378  B9 11 00 00 00                  mov ecx, 0x11
0035D37D  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
0035D382  4D 8B C6                        mov r8, r14
0035D385  E8 32 E4 FF FF                  call 0x14035b7bc
0035D38A  E9 D4 F7 FF FF                  jmp 0x14035cb63
0035D38F  48 8B 79 18                     mov rdi, qword ptr [rcx + 0x18]
0035D393  48 33 3D 8E 9E C6 00            xor rdi, qword ptr [rip + 0xc69e8e]
0035D39A  49 33 FC                        xor rdi, r12
0035D39D  E9 F9 FD FF FF                  jmp 0x14035d19b
0035D3A2  48 8B 05 B7 19 BA 00            mov rax, qword ptr [rip + 0xba19b7]
0035D3A9  8B 04 C8                        mov eax, dword ptr [rax + rcx*8]
0035D3AC  85 C0                           test eax, eax
0035D3AE  0F 84 C2 F5 FF FF               je 0x14035c976
0035D3B4  41 89 01                        mov dword ptr [r9], eax
0035D3B7  48 8B 05 A2 19 BA 00            mov rax, qword ptr [rip + 0xba19a2]
0035D3BE  48 8B 44 C8 48                  mov rax, qword ptr [rax + rcx*8 + 0x48]
0035D3C3  48 85 C0                        test rax, rax
0035D3C6  0F 84 89 F5 FF FF               je 0x14035c955
0035D3CC  49 89 41 48                     mov qword ptr [r9 + 0x48], rax
0035D3D0  E9 80 F5 FF FF                  jmp 0x14035c955
0035D3D5  C6 44 32 5C 01                  mov byte ptr [rdx + rsi + 0x5c], 1
0035D3DA  48 8B 16                        mov rdx, qword ptr [rsi]
0035D3DD  48 8B 4A 38                     mov rcx, qword ptr [rdx + 0x38]
0035D3E1  E8 FA 13 13 00                  call 0x14048e7e0
0035D3E6  85 C0                           test eax, eax
0035D3E8  0F 85 A0 F9 FF FF               jne 0x14035cd8e
0035D3EE  48 8B 4A 38                     mov rcx, qword ptr [rdx + 0x38]
0035D3F2  E8 A9 90 FC FF                  call 0x1403264a0
0035D3F7  E9 92 F9 FF FF                  jmp 0x14035cd8e
0035D3FC  0F B6 D0                        movzx edx, al
0035D3FF  41 0F B6 CF                     movzx ecx, r15b
0035D403  E8 F4 82 19 00                  call 0x1404f56fc
0035D408  E9 8F FA FF FF                  jmp 0x14035ce9c
0035D40D  8B 05 AD D3 B9 00               mov eax, dword ptr [rip + 0xb9d3ad]
0035D413  E9 B6 F0 FF FF                  jmp 0x14035c4ce
0035D418  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
0035D41D  33 C0                           xor eax, eax
0035D41F  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
0035D423  0F 57 C0                        xorps xmm0, xmm0
0035D426  88 44 24 39                     mov byte ptr [rsp + 0x39], al
0035D42A  88 44 24 59                     mov byte ptr [rsp + 0x59], al
0035D42E  8B 05 18 7D C6 00               mov eax, dword ptr [rip + 0xc67d18]
0035D434  4C 89 8D 78 01 00 00            mov qword ptr [rbp + 0x178], r9
0035D43B  89 75 94                        mov dword ptr [rbp - 0x6c], esi
0035D43E  0F 11 45 68                     movups xmmword ptr [rbp + 0x68], xmm0
0035D442  3B D8                           cmp ebx, eax
0035D444  75 01                           jne 0x14035d447
0035D446  CC                              int3
0035D447  8B 05 B7 96 C6 00               mov eax, dword ptr [rip + 0xc696b7]
0035D44D  A8 41                           test al, 0x41
0035D44F  0F 85 63 13 00 00               jne 0x14035e7b8
0035D455  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0035D45D  4D 8B E6                        mov r12, r14
0035D460  48 8B 15 F1 18 BA 00            mov rdx, qword ptr [rip + 0xba18f1]
0035D467  49 83 E4 FB                     and r12, 0xfffffffffffffffb
0035D46B  4C 8B 1D DE 18 BA 00            mov r11, qword ptr [rip + 0xba18de]
0035D472  8B C8                           mov ecx, eax
0035D474  48 8D 05 85 2B CA FF            lea rax, [rip - 0x35d47b]
0035D47B  48 89 55 C8                     mov qword ptr [rbp - 0x38], rdx
0035D47F  4C 89 5D B0                     mov qword ptr [rbp - 0x50], r11
0035D483  4C 8B 8C C8 20 AD EF 00         mov r9, qword ptr [rax + rcx*8 + 0xefad20]
0035D48B  48 69 CB 5F 9E 00 00            imul rcx, rbx, 0x9e5f
0035D492  4C 89 4D 88                     mov qword ptr [rbp - 0x78], r9
0035D496  48 8B F1                        mov rsi, rcx
0035D499  48 C1 EE 20                     shr rsi, 0x20
0035D49D  33 F1                           xor esi, ecx
0035D49F  23 F2                           and esi, edx
0035D4A1  44 8B C6                        mov r8d, esi
0035D4A4  89 B5 70 01 00 00               mov dword ptr [rbp + 0x170], esi
0035D4AA  8B CE                           mov ecx, esi
0035D4AC  4C 8D 3C 89                     lea r15, [rcx + rcx*4]
0035D4B0  49 C1 E7 04                     shl r15, 4
0035D4B4  43 8B 04 39                     mov eax, dword ptr [r9 + r15]
0035D4B8  4F 8D 34 39                     lea r14, [r9 + r15]
0035D4BC  3B C3                           cmp eax, ebx
0035D4BE  0F 85 6F 01 00 00               jne 0x14035d633
0035D4C4  41 B8 01 00 00 00               mov r8d, 1
0035D4CA  49 0F BA E4 08                  bt r12, 8
0035D4CF  0F 82 39 07 00 00               jb 0x14035dc0e
0035D4D5  41 8B C8                        mov ecx, r8d
0035D4D8  49 8D 5E 08                     lea rbx, [r14 + 8]
0035D4DC  49 8D 46 10                     lea rax, [r14 + 0x10]
0035D4E0  89 8D 70 01 00 00               mov dword ptr [rbp + 0x170], ecx
0035D4E6  F0 48 FF 00                     lock inc qword ptr [rax]
0035D4EA  4C 8B 8D 78 01 00 00            mov r9, qword ptr [rbp + 0x178]
0035D4F1  49 8B F1                        mov rsi, r9
0035D4F4  F0 48 0F C1 33                  lock xadd qword ptr [rbx], rsi
0035D4F9  49 83 7E 48 00                  cmp qword ptr [r14 + 0x48], 0
0035D4FE  0F 84 5E 01 00 00               je 0x14035d662
0035D504  48 63 C1                        movsxd rax, ecx
0035D507  4D 8D 3C C6                     lea r15, [r14 + rax*8]
0035D50B  4D 8B 67 38                     mov r12, qword ptr [r15 + 0x38]
0035D50F  41 F6 C4 01                     test r12b, 1
0035D513  0F 85 49 01 00 00               jne 0x14035d662
0035D519  4C 3B E6                        cmp r12, rsi
0035D51C  0F 8D 40 01 00 00               jge 0x14035d662
0035D522  44 8B C1                        mov r8d, ecx
0035D525  49 8B D1                        mov rdx, r9
0035D528  49 8B 4E 48                     mov rcx, qword ptr [r14 + 0x48]
0035D52C  E8 0F F9 F8 FF                  call 0x1402ece40
0035D531  41 B8 01 00 00 00               mov r8d, 1
0035D537  48 85 C0                        test rax, rax
0035D53A  0F 84 23 1F 00 00               je 0x14035f463
0035D540  49 3B C0                        cmp rax, r8
0035D543  0F 85 2C 12 00 00               jne 0x14035e775
0035D549  49 8B C4                        mov rax, r12
0035D54C  F0 4D 0F B1 47 38               lock cmpxchg qword ptr [r15 + 0x38], r8
0035D552  0F 84 0A 01 00 00               je 0x14035d662
0035D558  8B 8D 70 01 00 00               mov ecx, dword ptr [rbp + 0x170]
0035D55E  4C 8B 8D 78 01 00 00            mov r9, qword ptr [rbp + 0x178]
0035D565  EB A4                           jmp 0x14035d50b
0035D567  49 8B D4                        mov rdx, r12
0035D56A  48 8D 0D 9F B0 B0 00            lea rcx, [rip + 0xb0b09f]
0035D571  48 2B 15 90 B0 B0 00            sub rdx, qword ptr [rip + 0xb0b090]
0035D578  48 C1 EA 14                     shr rdx, 0x14
0035D57C  48 03 D2                        add rdx, rdx
0035D57F  E8 88 43 00 00                  call 0x14036190c
0035D584  48 85 C0                        test rax, rax
0035D587  74 0B                           je 0x14035d594
0035D589  FF C8                           dec eax
0035D58B  83 F8 02                        cmp eax, 2
0035D58E  0F 85 29 E9 FF FF               jne 0x14035bebd
0035D594  0F 57 C0                        xorps xmm0, xmm0
0035D597  4C 8D 85 D8 00 00 00            lea r8, [rbp + 0xd8]
0035D59E  49 8B D4                        mov rdx, r12
0035D5A1  48 8D 0D B0 B0 B0 00            lea rcx, [rip + 0xb0b0b0]
0035D5A8  0F 11 85 D8 00 00 00            movups xmmword ptr [rbp + 0xd8], xmm0
0035D5AF  0F 11 85 E8 00 00 00            movups xmmword ptr [rbp + 0xe8], xmm0
0035D5B6  E8 05 9E FC FF                  call 0x1403273c0
0035D5BB  48 8B 8D E8 00 00 00            mov rcx, qword ptr [rbp + 0xe8]
0035D5C2  8B 85 F0 00 00 00               mov eax, dword ptr [rbp + 0xf0]
0035D5C8  48 89 8D 10 01 00 00            mov qword ptr [rbp + 0x110], rcx
0035D5CF  89 85 98 00 00 00               mov dword ptr [rbp + 0x98], eax
0035D5D5  4C 8B 39                        mov r15, qword ptr [rcx]
0035D5D8  E9 1E E9 FF FF                  jmp 0x14035befb
0035D5DD  48 3B D3                        cmp rdx, rbx
0035D5E0  48 8B C8                        mov rcx, rax
0035D5E3  48 0F 47 D3                     cmova rdx, rbx
0035D5E7  48 2B CA                        sub rcx, rdx
0035D5EA  F0 49 0F B1 4F 40               lock cmpxchg qword ptr [r15 + 0x40], rcx
0035D5F0  0F 85 B2 FA FF FF               jne 0x14035d0a8
0035D5F6  48 8B C2                        mov rax, rdx
0035D5F9  F0 49 0F C1 47 48               lock xadd qword ptr [r15 + 0x48], rax
0035D5FF  48 03 D0                        add rdx, rax
0035D602  4B 3B 94 08 48 66 F0 00         cmp rdx, qword ptr [r8 + r9 + 0xf06648]
0035D60A  0F 86 98 FA FF FF               jbe 0x14035d0a8
0035D610  45 33 C0                        xor r8d, r8d
0035D613  4D 87 47 48                     xchg qword ptr [r15 + 0x48], r8
0035D617  4D 85 C0                        test r8, r8
0035D61A  0F 84 88 FA FF FF               je 0x14035d0a8
0035D620  45 33 C9                        xor r9d, r9d
0035D623  49 8B D7                        mov rdx, r15
0035D626  41 8B CC                        mov ecx, r12d
0035D629  E8 96 29 03 00                  call 0x14038ffc4
0035D62E  E9 75 FA FF FF                  jmp 0x14035d0a8
0035D633  85 C0                           test eax, eax
0035D635  0F 84 7B 03 00 00               je 0x14035d9b6
0035D63B  8D 46 01                        lea eax, [rsi + 1]
0035D63E  23 C2                           and eax, edx
0035D640  8B F0                           mov esi, eax
0035D642  41 3B C0                        cmp eax, r8d
0035D645  0F 85 5F FE FF FF               jne 0x14035d4aa
0035D64B  48 8B 95 78 01 00 00            mov rdx, qword ptr [rbp + 0x178]
0035D652  4D 8B C4                        mov r8, r12
0035D655  8B CB                           mov ecx, ebx
0035D657  E8 64 F6 F8 FF                  call 0x1402eccc0
0035D65C  41 B8 01 00 00 00               mov r8d, 1
0035D662  45 8B F8                        mov r15d, r8d
0035D665  0F B6 05 FC 15 C7 00            movzx eax, byte ptr [rip + 0xc715fc]
0035D66C  4C 8B E7                        mov r12, rdi
0035D66F  48 89 BD 78 01 00 00            mov qword ptr [rbp + 0x178], rdi
0035D676  48 BA 00 00 00 00 00 80 FF FF   movabs rdx, 0xffff800000000000
0035D680  33 FF                           xor edi, edi
0035D682  84 C0                           test al, al
0035D684  0F 85 6F 0D 00 00               jne 0x14035e3f9
0035D68A  4D 8B CC                        mov r9, r12
0035D68D  49 8B CC                        mov rcx, r12
0035D690  49 83 E1 F8                     and r9, 0xfffffffffffffff8
0035D694  4D 2B E9                        sub r13, r9
0035D697  49 2B C9                        sub rcx, r9
0035D69A  48 03 4C 24 70                  add rcx, qword ptr [rsp + 0x70]
0035D69F  4D 03 EC                        add r13, r12
0035D6A2  84 C0                           test al, al
0035D6A4  0F 84 23 E5 FF FF               je 0x14035bbcd
0035D6AA  4C 3B CA                        cmp r9, rdx
0035D6AD  0F 83 67 1D 00 00               jae 0x14035f41a
0035D6B3  BA 02 00 00 00                  mov edx, 2
0035D6B8  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0035D6BD  B9 F1 01 00 00                  mov ecx, 0x1f1
0035D6C2  E8 99 FF 19 00                  call 0x1404fd660
0035D6C7  CC                              int3
0035D6C8  48 8D 4D 30                     lea rcx, [rbp + 0x30]
0035D6CC  E8 DF A7 EF FF                  call 0x140257eb0
0035D6D1  E9 09 F3 FF FF                  jmp 0x14035c9df
0035D6D6  49 8B CE                        mov rcx, r14
0035D6D9  81 E1 00 01 00 00               and ecx, 0x100
0035D6DF  48 3B 3D CA 93 C6 00            cmp rdi, qword ptr [rip + 0xc693ca]
0035D6E6  0F 84 CE 00 00 00               je 0x14035d7ba
0035D6EC  41 8B C5                        mov eax, r13d
0035D6EF  4C 8D 0D 0A 29 CA FF            lea r9, [rip - 0x35d6f6]
0035D6F6  4C 8B AF F8 02 00 00            mov r13, qword ptr [rdi + 0x2f8]
0035D6FD  48 85 C9                        test rcx, rcx
0035D700  0F 95 C0                        setne al
0035D703  44 8B E0                        mov r12d, eax
0035D706  45 8B F4                        mov r14d, r12d
0035D709  49 C1 E6 07                     shl r14, 7
0035D70D  4D 03 F5                        add r14, r13
0035D710  43 0F B6 84 E1 50 73 FC 00      movzx eax, byte ptr [r9 + r12*8 + 0xfc7350]
0035D719  88 85 70 01 00 00               mov byte ptr [rbp + 0x170], al
0035D71F  41 0F 0D 0E                     prefetchw byte ptr [r14]
0035D723  4D 8B 3E                        mov r15, qword ptr [r14]
0035D726  49 8B 46 40                     mov rax, qword ptr [r14 + 0x40]
0035D72A  49 83 7E 50 00                  cmp qword ptr [r14 + 0x50], 0
0035D72F  74 20                           je 0x14035d751
0035D731  4D 6B C4 38                     imul r8, r12, 0x38
0035D735  49 3B C7                        cmp rax, r15
0035D738  76 17                           jbe 0x14035d751
0035D73A  4B 8B 94 08 48 66 F0 00         mov rdx, qword ptr [r8 + r9 + 0xf06648]
0035D742  48 8B C8                        mov rcx, rax
0035D745  49 2B CF                        sub rcx, r15
0035D748  48 3B CA                        cmp rcx, rdx
0035D74B  0F 87 F8 02 00 00               ja 0x14035da49
0035D751  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
0035D756  4C 8D 1D 23 A8 AC 00            lea r11, [rip + 0xaca823]
0035D75D  4D 8B D4                        mov r10, r12
0035D760  49 C1 E2 07                     shl r10, 7
0035D764  4D 3B CF                        cmp r9, r15
0035D767  4D 8B C7                        mov r8, r15
0035D76A  49 8B CF                        mov rcx, r15
0035D76D  49 8B C7                        mov rax, r15
0035D770  4D 0F 42 C1                     cmovb r8, r9
0035D774  49 2B C9                        sub rcx, r9
0035D777  33 D2                           xor edx, edx
0035D779  4D 3B CF                        cmp r9, r15
0035D77C  48 0F 42 D1                     cmovb rdx, rcx
0035D780  F0 49 0F B1 16                  lock cmpxchg qword ptr [r14], rdx
0035D785  4C 8B F8                        mov r15, rax
0035D788  75 DA                           jne 0x14035d764
0035D78A  4D 2B C8                        sub r9, r8
0035D78D  0F 85 3D 07 00 00               jne 0x14035ded0
0035D793  F6 85 70 01 00 00 04            test byte ptr [rbp + 0x170], 4
0035D79A  74 14                           je 0x14035d7b0
0035D79C  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0035D7A1  4A 8D 0C E7                     lea rcx, [rdi + r12*8]
0035D7A5  48 F7 D8                        neg rax
0035D7A8  F0 48 01 81 00 02 00 00         lock add qword ptr [rcx + 0x200], rax
0035D7B0  4C 8B A5 78 01 00 00            mov r12, qword ptr [rbp + 0x178]
0035D7B7  45 33 ED                        xor r13d, r13d
0035D7BA  83 3D 4F 78 C6 00 00            cmp dword ptr [rip + 0xc6784f], 0
0035D7C1  74 12                           je 0x14035d7d5
0035D7C3  33 D2                           xor edx, edx
0035D7C5  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0035D7C9  44 8B CB                        mov r9d, ebx
0035D7CC  44 8D 42 01                     lea r8d, [rdx + 1]
0035D7D0  E8 0F 32 EB FF                  call 0x1402109e4
0035D7D5  F0 48 0F C1 77 D0               lock xadd qword ptr [rdi - 0x30], rsi
0035D7DB  48 83 EE 01                     sub rsi, 1
0035D7DF  0F 8F 13 FA FF FF               jg 0x14035d1f8
0035D7E5  48 8B 4F D8                     mov rcx, qword ptr [rdi - 0x28]
0035D7E9  48 85 C9                        test rcx, rcx
0035D7EC  0F 85 85 11 00 00               jne 0x14035e977
0035D7F2  48 85 F6                        test rsi, rsi
0035D7F5  0F 89 0E 12 00 00               jns 0x14035ea09
0035D7FB  33 D2                           xor edx, edx
0035D7FD  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0035D802  44 8D 49 04                     lea r9d, [rcx + 4]
0035D806  4C 8B C7                        mov r8, rdi
0035D809  8D 4A 18                        lea ecx, [rdx + 0x18]
0035D80C  E8 4F FE 19 00                  call 0x1404fd660
0035D811  CC                              int3
0035D812  8B 05 68 94 C6 00               mov eax, dword ptr [rip + 0xc69468]
0035D818  48 03 F0                        add rsi, rax
0035D81B  48 81 FE E0 0F 00 00            cmp rsi, 0xfe0
0035D822  0F 86 5F E9 FF FF               jbe 0x14035c187
0035D828  48 2B F0                        sub rsi, rax
0035D82B  49 83 E3 F7                     and r11, 0xfffffffffffffff7
0035D82F  4C 89 5C 24 78                  mov qword ptr [rsp + 0x78], r11
0035D834  E9 4E E9 FF FF                  jmp 0x14035c187
0035D839  C7 44 24 68 01 00 00 00         mov dword ptr [rsp + 0x68], 1
0035D841  4C 8B D8                        mov r11, rax
0035D844  E9 71 EA FF FF                  jmp 0x14035c2ba
0035D849  41 81 FF 00 00 00 80            cmp r15d, 0x80000000
0035D850  0F 84 CD E2 FF FF               je 0x14035bb23
0035D856  E9 E0 E2 FF FF                  jmp 0x14035bb3b
0035D85B  44 89 54 24 68                  mov dword ptr [rsp + 0x68], r10d
0035D860  48 8B D8                        mov rbx, rax
0035D863  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0035D867  E9 73 ED FF FF                  jmp 0x14035c5df
0035D86C  48 81 C6 FF 0F 00 00            add rsi, 0xfff
0035D873  48 81 E6 00 F0 FF FF            and rsi, 0xfffffffffffff000
0035D87A  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
0035D87F  E9 33 E3 FF FF                  jmp 0x14035bbb7
0035D884  48 8D 4D 30                     lea rcx, [rbp + 0x30]
0035D888  E8 53 54 FE FF                  call 0x140342ce0
0035D88D  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0035D895  44 8B 05 B4 14 BA 00            mov r8d, dword ptr [rip + 0xba14b4]
0035D89C  8B C8                           mov ecx, eax
0035D89E  41 FF C8                        dec r8d
0035D8A1  48 8D 05 58 27 CA FF            lea rax, [rip - 0x35d8a8]
0035D8A8  48 8B 94 C8 20 AD EF 00         mov rdx, qword ptr [rax + rcx*8 + 0xefad20]
0035D8B0  4B 8D 0C 80                     lea rcx, [r8 + r8*4]
0035D8B4  48 C1 E1 04                     shl rcx, 4
0035D8B8  49 8B C7                        mov rax, r15
0035D8BB  48 03 CA                        add rcx, rdx
0035D8BE  48 F7 D8                        neg rax
0035D8C1  48 0F BA E6 08                  bt rsi, 8
0035D8C6  0F 82 DB 00 00 00               jb 0x14035d9a7
0035D8CC  F0 48 FF 41 18                  lock inc qword ptr [rcx + 0x18]
0035D8D1  F0 48 01 41 08                  lock add qword ptr [rcx + 8], rax
0035D8D6  E9 AF F1 FF FF                  jmp 0x14035ca8a
0035D8DB  49 8D 8F 40 03 00 00            lea rcx, [r15 + 0x340]
0035D8E2  45 8B CE                        mov r9d, r14d
0035D8E5  44 8B C6                        mov r8d, esi
0035D8E8  E8 CF B6 F8 FF                  call 0x1402e8fbc
0035D8ED  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
0035D8F2  48 8B F0                        mov rsi, rax
0035D8F5  48 83 FE FF                     cmp rsi, -1
0035D8F9  74 48                           je 0x14035d943
0035D8FB  48 85 F6                        test rsi, rsi
0035D8FE  74 1E                           je 0x14035d91e
0035D900  4C 8B 5C 24 78                  mov r11, qword ptr [rsp + 0x78]
0035D905  41 F6 C3 10                     test r11b, 0x10
0035D909  48 8B FE                        mov rdi, rsi
0035D90C  0F 94 C1                        sete cl
0035D90F  41 F6 C3 10                     test r11b, 0x10
0035D913  0F 95 C0                        setne al
0035D916  84 C8                           test al, cl
0035D918  0F 84 D6 05 00 00               je 0x14035def4
0035D91E  45 33 E4                        xor r12d, r12d
0035D921  4C 89 A5 78 01 00 00            mov qword ptr [rbp + 0x178], r12
0035D928  E9 42 E8 FF FF                  jmp 0x14035c16f
0035D92D  49 8B CB                        mov rcx, r11
0035D930  E8 5F EF 19 00                  call 0x1404fc894
0035D935  48 85 C0                        test rax, rax
0035D938  0F 85 3A 03 00 00               jne 0x14035dc78
0035D93E  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
0035D943  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
0035D947  45 8B CE                        mov r9d, r14d
0035D94A  48 81 FA 00 00 02 00            cmp rdx, 0x20000
0035D951  0F 87 D2 0F 00 00               ja 0x14035e929
0035D957  44 8B C2                        mov r8d, edx
0035D95A  49 8D 8F C0 02 00 00            lea rcx, [r15 + 0x2c0]
0035D961  41 8B D4                        mov edx, r12d
0035D964  E8 DB CF F8 FF                  call 0x1402ea944
0035D969  48 8B F0                        mov rsi, rax
0035D96C  EB 8D                           jmp 0x14035d8fb
0035D96E  49 8B CB                        mov rcx, r11
0035D971  E8 1E EF 19 00                  call 0x1404fc894
0035D976  48 85 C0                        test rax, rax
0035D979  0F 85 90 03 00 00               jne 0x14035dd0f
0035D97F  44 8B C7                        mov r8d, edi
0035D982  8B DE                           mov ebx, esi
0035D984  45 8B CE                        mov r9d, r14d
0035D987  48 81 FF 00 00 02 00            cmp rdi, 0x20000
0035D98E  0F 87 C4 0F 00 00               ja 0x14035e958
0035D994  49 8D 8F C0 02 00 00            lea rcx, [r15 + 0x2c0]
0035D99B  8B D3                           mov edx, ebx
0035D99D  E8 A2 CF F8 FF                  call 0x1402ea944
0035D9A2  E9 81 E7 FF FF                  jmp 0x14035c128
0035D9A7  F0 48 FF 41 30                  lock inc qword ptr [rcx + 0x30]
0035D9AC  F0 48 01 41 20                  lock add qword ptr [rcx + 0x20], rax
0035D9B1  E9 D4 F0 FF FF                  jmp 0x14035ca8a
0035D9B6  48 8B 05 A3 13 BA 00            mov rax, qword ptr [rip + 0xba13a3]
0035D9BD  45 8B 14 07                     mov r10d, dword ptr [r15 + rax]
0035D9C1  45 85 D2                        test r10d, r10d
0035D9C4  0F 84 E5 00 00 00               je 0x14035daaf
0035D9CA  45 89 16                        mov dword ptr [r14], r10d
0035D9CD  48 8B 05 8C 13 BA 00            mov rax, qword ptr [rip + 0xba138c]
0035D9D4  49 8B 4C 07 48                  mov rcx, qword ptr [r15 + rax + 0x48]
0035D9D9  48 85 C9                        test rcx, rcx
0035D9DC  0F 84 C8 FA FF FF               je 0x14035d4aa
0035D9E2  49 89 4E 48                     mov qword ptr [r14 + 0x48], rcx
0035D9E6  E9 BF FA FF FF                  jmp 0x14035d4aa
0035D9EB  48 81 C6 C0 00 00 00            add rsi, 0xc0
0035D9F2  E9 33 E2 FF FF                  jmp 0x14035bc2a
0035D9F7  4C 39 9D 70 01 00 00            cmp qword ptr [rbp + 0x170], r11
0035D9FE  0F 85 9F 03 00 00               jne 0x14035dda3
0035DA04  4D 8B C4                        mov r8, r12
0035DA07  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0035DA0C  48 8B D7                        mov rdx, rdi
0035DA0F  B9 21 00 00 00                  mov ecx, 0x21
0035DA14  E8 47 FC 19 00                  call 0x1404fd660
0035DA19  CC                              int3
0035DA1A  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
0035DA24  4C 3B F0                        cmp r14, rax
0035DA27  0F 83 1E 17 00 00               jae 0x14035f14b
0035DA2D  BA 02 00 00 00                  mov edx, 2
0035DA32  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0035DA37  4D 8B CE                        mov r9, r14
0035DA3A  B9 F1 01 00 00                  mov ecx, 0x1f1
0035DA3F  44 8D 42 FF                     lea r8d, [rdx - 1]
0035DA43  E8 18 FC 19 00                  call 0x1404fd660
0035DA48  CC                              int3
0035DA49  48 3B 54 24 60                  cmp rdx, qword ptr [rsp + 0x60]
0035DA4E  48 8B C8                        mov rcx, rax
0035DA51  48 0F 47 54 24 60               cmova rdx, qword ptr [rsp + 0x60]
0035DA57  48 2B CA                        sub rcx, rdx
0035DA5A  F0 49 0F B1 4E 40               lock cmpxchg qword ptr [r14 + 0x40], rcx
0035DA60  0F 85 EB FC FF FF               jne 0x14035d751
0035DA66  48 8B C2                        mov rax, rdx
0035DA69  F0 49 0F C1 46 48               lock xadd qword ptr [r14 + 0x48], rax
0035DA6F  48 03 D0                        add rdx, rax
0035DA72  4B 3B 94 08 48 66 F0 00         cmp rdx, qword ptr [r8 + r9 + 0xf06648]
0035DA7A  0F 86 D1 FC FF FF               jbe 0x14035d751
0035DA80  45 33 C0                        xor r8d, r8d
0035DA83  4D 87 46 48                     xchg qword ptr [r14 + 0x48], r8
0035DA87  4D 85 C0                        test r8, r8
0035DA8A  0F 84 C1 FC FF FF               je 0x14035d751
0035DA90  45 33 C9                        xor r9d, r9d
0035DA93  49 8B D6                        mov rdx, r14
0035DA96  41 8B CC                        mov ecx, r12d
0035DA99  E8 26 25 03 00                  call 0x14038ffc4
0035DA9E  E9 AE FC FF FF                  jmp 0x14035d751
0035DAA3  48 81 C3 C0 00 00 00            add rbx, 0xc0
0035DAAA  E9 77 F0 FF FF                  jmp 0x14035cb26
0035DAAF  49 8D 43 FF                     lea rax, [r11 - 1]
0035DAB3  48 3B C8                        cmp rcx, rax
0035DAB6  0F 84 7F FB FF FF               je 0x14035d63b
0035DABC  48 8D 0D 3D D2 B9 00            lea rcx, [rip + 0xb9d23d]
0035DAC3  48 C7 45 68 00 00 00 00         mov qword ptr [rbp + 0x68], 0
0035DACB  48 89 4D 70                     mov qword ptr [rbp + 0x70], rcx
0035DACF  90                              nop
0035DAD0  44 0F 20 C0                     mov rax, cr8
0035DAD4  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0035DAD9  BA 02 00 00 00                  mov edx, 2
0035DADE  44 0F 22 C2                     mov cr8, rdx
0035DAE2  83 3D 37 92 C6 00 00            cmp dword ptr [rip + 0xc69237], 0
0035DAE9  0F 85 73 03 00 00               jne 0x14035de62
0035DAEF  F6 05 10 90 C6 00 21            test byte ptr [rip + 0xc69010], 0x21
0035DAF6  88 45 78                        mov byte ptr [rbp + 0x78], al
0035DAF9  0F 85 6F 02 00 00               jne 0x14035dd6e
0035DAFF  48 8D 55 68                     lea rdx, [rbp + 0x68]
0035DB03  48 87 15 F6 D1 B9 00            xchg qword ptr [rip + 0xb9d1f6], rdx
0035DB0A  48 85 D2                        test rdx, rdx
0035DB0D  0F 85 07 09 00 00               jne 0x14035e41a
0035DB13  48 8B 05 46 12 BA 00            mov rax, qword ptr [rip + 0xba1246]
0035DB1A  49 03 C7                        add rax, r15
0035DB1D  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0035DB22  83 38 00                        cmp dword ptr [rax], 0
0035DB25  75 22                           jne 0x14035db49
0035DB27  8B CB                           mov ecx, ebx
0035DB29  E8 C2 F0 F8 FF                  call 0x1402ecbf0
0035DB2E  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0035DB33  48 89 41 48                     mov qword ptr [rcx + 0x48], rax
0035DB37  49 89 46 48                     mov qword ptr [r14 + 0x48], rax
0035DB3B  48 8B 05 1E 12 BA 00            mov rax, qword ptr [rip + 0xba121e]
0035DB42  41 89 1C 07                     mov dword ptr [r15 + rax], ebx
0035DB46  41 89 1E                        mov dword ptr [r14], ebx
0035DB49  48 8D 4D 68                     lea rcx, [rbp + 0x68]
0035DB4D  E8 8E 51 FE FF                  call 0x140342ce0
0035DB52  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
0035DB56  44 8B 85 70 01 00 00            mov r8d, dword ptr [rbp + 0x170]
0035DB5D  4C 8B 4D 88                     mov r9, qword ptr [rbp - 0x78]
0035DB61  4C 8B 5D B0                     mov r11, qword ptr [rbp - 0x50]
0035DB65  E9 40 F9 FF FF                  jmp 0x14035d4aa
0035DB6A  44 8B 8D 78 01 00 00            mov r9d, dword ptr [rbp + 0x178]
0035DB71  48 F7 D2                        not rdx
0035DB74  4C 8B 55 B0                     mov r10, qword ptr [rbp - 0x50]
0035DB78  48 85 D2                        test rdx, rdx
0035DB7B  0F 85 1A E8 FF FF               jne 0x14035c39b
0035DB81  49 8D 4B 40                     lea rcx, [r11 + 0x40]
0035DB85  4D 3B C2                        cmp r8, r10
0035DB88  0F 84 0D 02 00 00               je 0x14035dd9b
0035DB8E  49 83 C0 08                     add r8, 8
0035DB92  E9 F5 E7 FF FF                  jmp 0x14035c38c
0035DB97  F3 48 0F B8 C2                  popcnt rax, rdx
0035DB9C  41 0F AF C1                     imul eax, r9d
0035DBA0  B9 01 00 00 00                  mov ecx, 1
0035DBA5  C1 E8 08                        shr eax, 8
0035DBA8  C4 E2 F9 F7 C1                  shlx rax, rcx, rax
0035DBAD  C4 62 FB F5 CA                  pdep r9, rax, rdx
0035DBB2  F3 4D 0F BC D1                  tzcnt r10, r9
0035DBB7  E9 1D E8 FF FF                  jmp 0x14035c3d9
0035DBBC  44 8B 8D 78 01 00 00            mov r9d, dword ptr [rbp + 0x178]
0035DBC3  48 F7 D2                        not rdx
0035DBC6  4C 8B 55 C0                     mov r10, qword ptr [rbp - 0x40]
0035DBCA  48 85 D2                        test rdx, rdx
0035DBCD  0F 85 E4 EA FF FF               jne 0x14035c6b7
0035DBD3  48 8D 4F 40                     lea rcx, [rdi + 0x40]
0035DBD7  4D 3B C2                        cmp r8, r10
0035DBDA  0F 84 DA 01 00 00               je 0x14035ddba
0035DBE0  49 83 C0 08                     add r8, 8
0035DBE4  E9 BF EA FF FF                  jmp 0x14035c6a8
0035DBE9  F3 48 0F B8 C2                  popcnt rax, rdx
0035DBEE  41 0F AF C1                     imul eax, r9d
0035DBF2  B9 01 00 00 00                  mov ecx, 1
0035DBF7  C1 E8 08                        shr eax, 8
0035DBFA  C4 E2 F9 F7 C1                  shlx rax, rcx, rax
0035DBFF  C4 62 FB F5 CA                  pdep r9, rax, rdx
0035DC04  F3 4D 0F BC D1                  tzcnt r10, r9
0035DC09  E9 EC EA FF FF                  jmp 0x14035c6fa
0035DC0E  33 C9                           xor ecx, ecx
0035DC10  49 8D 5E 20                     lea rbx, [r14 + 0x20]
0035DC14  49 8D 46 28                     lea rax, [r14 + 0x28]
0035DC18  E9 C3 F8 FF FF                  jmp 0x14035d4e0
0035DC1D  8B 8D 78 01 00 00               mov ecx, dword ptr [rbp + 0x178]
0035DC23  45 33 C9                        xor r9d, r9d
0035DC26  41 8B F1                        mov esi, r9d
0035DC29  83 F9 FF                        cmp ecx, -1
0035DC2C  0F 84 E5 0D 00 00               je 0x14035ea17
0035DC32  8B C1                           mov eax, ecx
0035DC34  49 C7 C0 FE FF FF FF            mov r8, 0xfffffffffffffffe
0035DC3B  C1 E8 06                        shr eax, 6
0035DC3E  83 E1 3F                        and ecx, 0x3f
0035DC41  49 D3 C0                        rol r8, cl
0035DC44  49 8D 14 C3                     lea rdx, [r11 + rax*8]
0035DC48  0F 0D 4A 40                     prefetchw byte ptr [rdx + 0x40]
0035DC4C  48 8B 42 40                     mov rax, qword ptr [rdx + 0x40]
0035DC50  48 8B C8                        mov rcx, rax
0035DC53  49 23 C8                        and rcx, r8
0035DC56  F0 48 0F B1 4A 40               lock cmpxchg qword ptr [rdx + 0x40], rcx
0035DC5C  75 F2                           jne 0x14035dc50
0035DC5E  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
0035DC63  49 8B 43 10                     mov rax, qword ptr [r11 + 0x10]
0035DC67  4D 8D 87 40 03 00 00            lea r8, [r15 + 0x340]
0035DC6E  BB 02 00 00 00                  mov ebx, 2
0035DC73  E9 68 53 38 00                  jmp 0x1406e2fe0
0035DC78  0F B6 4D B4                     movzx ecx, byte ptr [rbp - 0x4c]
0035DC7C  4D 8D 9F 40 03 00 00            lea r11, [r15 + 0x340]
0035DC83  48 8B 85 70 01 00 00            mov rax, qword ptr [rbp + 0x170]
0035DC8A  48 C1 E1 08                     shl rcx, 8
0035DC8E  48 81 C1 C0 05 00 00            add rcx, 0x5c0
0035DC95  49 03 CB                        add rcx, r11
0035DC98  0F B7 14 01                     movzx edx, word ptr [rcx + rax]
0035DC9C  44 8B C2                        mov r8d, edx
0035DC9F  48 39 8D 78 01 00 00            cmp qword ptr [rbp + 0x178], rcx
0035DCA6  0F 84 DA E5 FF FF               je 0x14035c286
0035DCAC  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0035DCB1  66 89 10                        mov word ptr [rax], dx
0035DCB4  E9 CD E5 FF FF                  jmp 0x14035c286
0035DCB9  8B 8D 78 01 00 00               mov ecx, dword ptr [rbp + 0x178]
0035DCBF  45 33 C9                        xor r9d, r9d
0035DCC2  41 8B F9                        mov edi, r9d
0035DCC5  83 F9 FF                        cmp ecx, -1
0035DCC8  0F 84 BE EA FF FF               je 0x14035c78c
0035DCCE  8B C1                           mov eax, ecx
0035DCD0  49 C7 C0 FE FF FF FF            mov r8, 0xfffffffffffffffe
0035DCD7  C1 E8 06                        shr eax, 6
0035DCDA  83 E1 3F                        and ecx, 0x3f
0035DCDD  49 D3 C0                        rol r8, cl
0035DCE0  49 8D 14 C2                     lea rdx, [r10 + rax*8]
0035DCE4  0F 0D 4A 40                     prefetchw byte ptr [rdx + 0x40]
0035DCE8  48 8B 42 40                     mov rax, qword ptr [rdx + 0x40]
0035DCEC  48 8B C8                        mov rcx, rax
0035DCEF  49 23 C8                        and rcx, r8
0035DCF2  F0 48 0F B1 4A 40               lock cmpxchg qword ptr [rdx + 0x40], rcx
0035DCF8  75 F2                           jne 0x14035dcec
0035DCFA  49 8B 42 10                     mov rax, qword ptr [r10 + 0x10]
0035DCFE  4D 8D A7 40 03 00 00            lea r12, [r15 + 0x340]
0035DD05  BB 02 00 00 00                  mov ebx, 2
0035DD0A  E9 8D 50 38 00                  jmp 0x1406e2d9c
0035DD0F  0F B6 4D C4                     movzx ecx, byte ptr [rbp - 0x3c]
0035DD13  4D 8D 9F 40 03 00 00            lea r11, [r15 + 0x340]
0035DD1A  48 8B 85 70 01 00 00            mov rax, qword ptr [rbp + 0x170]
0035DD21  48 C1 E1 08                     shl rcx, 8
0035DD25  48 81 C1 C0 05 00 00            add rcx, 0x5c0
0035DD2C  49 03 CB                        add rcx, r11
0035DD2F  0F B7 14 08                     movzx edx, word ptr [rax + rcx]
0035DD33  44 8B C2                        mov r8d, edx
0035DD36  48 3B D9                        cmp rbx, rcx
0035DD39  0F 84 6C E8 FF FF               je 0x14035c5ab
0035DD3F  66 89 14 18                     mov word ptr [rax + rbx], dx
0035DD43  E9 63 E8 FF FF                  jmp 0x14035c5ab
0035DD48  4D 3B C2                        cmp r8, r10
0035DD4B  74 4E                           je 0x14035dd9b
0035DD4D  49 83 C0 08                     add r8, 8
0035DD51  E9 36 E6 FF FF                  jmp 0x14035c38c
0035DD56  45 8B CE                        mov r9d, r14d
0035DD59  44 8B C6                        mov r8d, esi
0035DD5C  49 8B CB                        mov rcx, r11
0035DD5F  8B DE                           mov ebx, esi
0035DD61  E8 56 B2 F8 FF                  call 0x1402e8fbc
0035DD66  48 8B F8                        mov rdi, rax
0035DD69  E9 3B EA FF FF                  jmp 0x14035c7a9
0035DD6E  8B 05 E4 00 BB 00               mov eax, dword ptr [rip + 0xbb00e4]
0035DD74  85 C0                           test eax, eax
0035DD76  0F 85 83 FD FF FF               jne 0x14035daff
0035DD7C  48 8B D1                        mov rdx, rcx
0035DD7F  48 8D 4D 68                     lea rcx, [rbp + 0x68]
0035DD83  E8 C8 7A F1 FF                  call 0x140275850
0035DD88  E9 86 FD FF FF                  jmp 0x14035db13
0035DD8D  4D 3B C2                        cmp r8, r10
0035DD90  74 28                           je 0x14035ddba
0035DD92  49 83 C0 08                     add r8, 8
0035DD96  E9 0D E9 FF FF                  jmp 0x14035c6a8
0035DD9B  4C 8B C1                        mov r8, rcx
0035DD9E  E9 E9 E5 FF FF                  jmp 0x14035c38c
0035DDA3  4C 89 9D 70 01 00 00            mov qword ptr [rbp + 0x170], r11
0035DDAA  4F 8D 3C 1A                     lea r15, [r10 + r11]
0035DDAE  41 0F 0D 0F                     prefetchw byte ptr [r15]
0035DDB2  4D 8B 37                        mov r14, qword ptr [r15]
0035DDB5  E9 FF F2 FF FF                  jmp 0x14035d0b9
0035DDBA  4C 8B C1                        mov r8, rcx
0035DDBD  E9 E6 E8 FF FF                  jmp 0x14035c6a8
0035DDC2  48 85 D2                        test rdx, rdx
0035DDC5  0F 84 0D ED FF FF               je 0x14035cad8
0035DDCB  41 8D 47 0F                     lea eax, [r15 + 0xf]
0035DDCF  C1 E8 04                        shr eax, 4
0035DDD2  0F B6 8C 30 80 0B 01 00         movzx ecx, byte ptr [rax + rsi + 0x10b80]
0035DDDA  83 C1 DF                        add ecx, -0x21
0035DDDD  48 FF C1                        inc rcx
0035DDE0  48 C1 E1 06                     shl rcx, 6
0035DDE4  48 03 CA                        add rcx, rdx
0035DDE7  FF 41 1C                        inc dword ptr [rcx + 0x1c]
0035DDEA  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
0035DDEE  66 39 01                        cmp word ptr [rcx], ax
0035DDF1  73 1A                           jae 0x14035de0d
0035DDF3  49 8B D6                        mov rdx, r14
0035DDF6  E8 B5 C7 35 00                  call 0x1406ba5b0
0035DDFB  B8 01 00 00 00                  mov eax, 1
0035DE00  85 C0                           test eax, eax
0035DE02  0F 84 D0 EC FF FF               je 0x14035cad8
0035DE08  E9 56 ED FF FF                  jmp 0x14035cb63
0035DE0D  FF 41 20                        inc dword ptr [rcx + 0x20]
0035DE10  41 8B C5                        mov eax, r13d
0035DE13  EB EB                           jmp 0x14035de00
0035DE15  41 0F B7 43 30                  movzx eax, word ptr [r11 + 0x30]
0035DE1A  3B C8                           cmp ecx, eax
0035DE1C  0F 86 2D E6 FF FF               jbe 0x14035c44f
0035DE22  44 8B C6                        mov r8d, esi
0035DE25  49 8D 8F 40 03 00 00            lea rcx, [r15 + 0x340]
0035DE2C  49 8B D3                        mov rdx, r11
0035DE2F  E8 E4 DC F8 FF                  call 0x1402ebb18
0035DE34  4C 8B DA                        mov r11, rdx
0035DE37  E9 13 E6 FF FF                  jmp 0x14035c44f
0035DE3C  8B 05 16 00 BB 00               mov eax, dword ptr [rip + 0xbb0016]
0035DE42  85 C0                           test eax, eax
0035DE44  0F 85 70 F3 FF FF               jne 0x14035d1ba
0035DE4A  48 8B 95 68 01 00 00            mov rdx, qword ptr [rbp + 0x168]
0035DE51  48 8D 0D A0 CE B9 00            lea rcx, [rip + 0xb9cea0]
0035DE58  E8 EB 30 F9 FF                  call 0x1402f0f48
0035DE5D  E9 6A F3 FF FF                  jmp 0x14035d1cc
0035DE62  0F B6 C8                        movzx ecx, al
0035DE65  E8 92 78 19 00                  call 0x1404f56fc
0035DE6A  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0035DE6F  48 8D 0D 8A CE B9 00            lea rcx, [rip + 0xb9ce8a]
0035DE76  E9 74 FC FF FF                  jmp 0x14035daef
0035DE7B  4C 8B 54 24 30                  mov r10, qword ptr [rsp + 0x30]
0035DE80  41 0F B7 42 30                  movzx eax, word ptr [r10 + 0x30]
0035DE85  3B C8                           cmp ecx, eax
0035DE87  0F 86 E0 E8 FF FF               jbe 0x14035c76d
0035DE8D  44 8B C7                        mov r8d, edi
0035DE90  49 8B D2                        mov rdx, r10
0035DE93  49 8B CB                        mov rcx, r11
0035DE96  E8 7D DC F8 FF                  call 0x1402ebb18
0035DE9B  4C 8B D2                        mov r10, rdx
0035DE9E  E9 CA E8 FF FF                  jmp 0x14035c76d
0035DEA3  48 8B 4F D8                     mov rcx, qword ptr [rdi - 0x28]
0035DEA7  48 85 C9                        test rcx, rcx
0035DEAA  0F 85 D0 05 00 00               jne 0x14035e480
0035DEB0  48 85 F6                        test rsi, rsi
0035DEB3  0F 89 3D 0B 00 00               jns 0x14035e9f6
0035DEB9  33 D2                           xor edx, edx
0035DEBB  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0035DEC0  44 8D 49 04                     lea r9d, [rcx + 4]
0035DEC4  4C 8B C7                        mov r8, rdi
0035DEC7  8D 4A 18                        lea ecx, [rdx + 0x18]
0035DECA  E8 91 F7 19 00                  call 0x1404fd660
0035DECF  CC                              int3
0035DED0  4D 3B EB                        cmp r13, r11
0035DED3  0F 85 D6 07 00 00               jne 0x14035e6af
0035DED9  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0035DEDE  4D 8B C4                        mov r8, r12
0035DEE1  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
0035DEE6  48 8B D7                        mov rdx, rdi
0035DEE9  B9 21 00 00 00                  mov ecx, 0x21
0035DEEE  E8 6D F7 19 00                  call 0x1404fd660
0035DEF3  CC                              int3
0035DEF4  49 8B C3                        mov rax, r11
0035DEF7  25 C0 01 00 00                  and eax, 0x1c0
0035DEFC  48 3D 00 01 00 00               cmp rax, 0x100
0035DF02  0F 85 32 03 00 00               jne 0x14035e23a
0035DF08  41 F6 C3 10                     test r11b, 0x10
0035DF0C  BA 01 00 00 00                  mov edx, 1
0035DF11  B8 01 00 00 80                  mov eax, 0x80000001
0035DF16  0F 45 D0                        cmovne edx, eax
0035DF19  8B CA                           mov ecx, edx
0035DF1B  48 B8 29 06 00 00 01 00 00 00   movabs rax, 0x100000629
0035DF25  83 C9 20                        or ecx, 0x20
0035DF28  41 F6 C3 04                     test r11b, 4
0035DF2C  0F 44 CA                        cmove ecx, edx
0035DF2F  44 8B C1                        mov r8d, ecx
0035DF32  41 0F BA E8 0A                  bts r8d, 0xa
0035DF37  41 F6 C3 02                     test r11b, 2
0035DF3B  44 0F 45 C1                     cmovne r8d, ecx
0035DF3F  4C 85 D8                        test rax, r11
0035DF42  74 53                           je 0x14035df97
0035DF44  49 8B C3                        mov rax, r11
0035DF47  41 8B C8                        mov ecx, r8d
0035DF4A  83 C9 04                        or ecx, 4
0035DF4D  41 F6 C3 08                     test r11b, 8
0035DF51  41 0F 44 C8                     cmove ecx, r8d
0035DF55  25 00 02 00 00                  and eax, 0x200
0035DF5A  8B D1                           mov edx, ecx
0035DF5C  0F BA EA 07                     bts edx, 7
0035DF60  48 85 C0                        test rax, rax
0035DF63  49 8B C3                        mov rax, r11
0035DF66  0F 44 D1                        cmove edx, ecx
0035DF69  25 00 04 00 00                  and eax, 0x400
0035DF6E  8B CA                           mov ecx, edx
0035DF70  83 C9 40                        or ecx, 0x40
0035DF73  48 85 C0                        test rax, rax
0035DF76  49 8B C3                        mov rax, r11
0035DF79  0F 44 CA                        cmove ecx, edx
0035DF7C  83 E0 20                        and eax, 0x20
0035DF7F  44 8B C1                        mov r8d, ecx
0035DF82  41 F6 C3 01                     test r11b, 1
0035DF86  0F 84 C2 02 00 00               je 0x14035e24e
0035DF8C  41 83 C8 08                     or r8d, 8
0035DF90  48 85 C0                        test rax, rax
0035DF93  44 0F 45 C1                     cmovne r8d, ecx
0035DF97  89 5E 04                        mov dword ptr [rsi + 4], ebx
0035DF9A  4D 8B F3                        mov r14, r11
0035DF9D  C6 06 00                        mov byte ptr [rsi], 0
0035DFA0  0F 57 C0                        xorps xmm0, xmm0
0035DFA3  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0035DFA8  48 C1 E8 04                     shr rax, 4
0035DFAC  88 46 02                        mov byte ptr [rsi + 2], al
0035DFAF  41 0F B6 C0                     movzx eax, r8b
0035DFB3  0C 08                           or al, 8
0035DFB5  0F B6 D0                        movzx edx, al
0035DFB8  41 F6 C3 01                     test r11b, 1
0035DFBC  41 0F B6 C0                     movzx eax, r8b
0035DFC0  0F 44 D0                        cmove edx, eax
0035DFC3  33 C0                           xor eax, eax
0035DFC5  80 E2 6D                        and dl, 0x6d
0035DFC8  89 45 98                        mov dword ptr [rbp - 0x68], eax
0035DFCB  80 CA 02                        or dl, 2
0035DFCE  88 44 24 3A                     mov byte ptr [rsp + 0x3a], al
0035DFD2  88 56 03                        mov byte ptr [rsi + 3], dl
0035DFD5  41 81 E6 CD 03 00 00            and r14d, 0x3cd
0035DFDC  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
0035DFE1  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
0035DFE8  88 44 24 5A                     mov byte ptr [rsp + 0x5a], al
0035DFEC  8B 05 5A 71 C6 00               mov eax, dword ptr [rip + 0xc6715a]
0035DFF2  4C 89 8D 78 01 00 00            mov qword ptr [rbp + 0x178], r9
0035DFF9  0F 11 85 80 00 00 00            movups xmmword ptr [rbp + 0x80], xmm0
0035E000  3B D8                           cmp ebx, eax
0035E002  75 01                           jne 0x14035e005
0035E004  CC                              int3
0035E005  8B 05 F9 8A C6 00               mov eax, dword ptr [rip + 0xc68af9]
0035E00B  A8 41                           test al, 0x41
0035E00D  0F 85 B0 04 00 00               jne 0x14035e4c3
0035E013  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0035E01B  49 83 E6 FB                     and r14, 0xfffffffffffffffb
0035E01F  4C 8B 25 32 0D BA 00            mov r12, qword ptr [rip + 0xba0d32]
0035E026  4C 8B 15 23 0D BA 00            mov r10, qword ptr [rip + 0xba0d23]
0035E02D  8B C8                           mov ecx, eax
0035E02F  48 8D 05 CA 1F CA FF            lea rax, [rip - 0x35e036]
0035E036  4C 89 55 88                     mov qword ptr [rbp - 0x78], r10
0035E03A  4C 8B 84 C8 20 AD EF 00         mov r8, qword ptr [rax + rcx*8 + 0xefad20]
0035E042  8B C3                           mov eax, ebx
0035E044  48 69 C8 5F 9E 00 00            imul rcx, rax, 0x9e5f
0035E04B  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
0035E04F  48 8B F9                        mov rdi, rcx
0035E052  48 C1 EF 20                     shr rdi, 0x20
0035E056  33 F9                           xor edi, ecx
0035E058  41 23 FC                        and edi, r12d
0035E05B  44 8B CF                        mov r9d, edi
0035E05E  89 BD 70 01 00 00               mov dword ptr [rbp + 0x170], edi
0035E064  8B D7                           mov edx, edi
0035E066  48 8D 0C 92                     lea rcx, [rdx + rdx*4]
0035E06A  48 03 C9                        add rcx, rcx
0035E06D  41 8B 04 C8                     mov eax, dword ptr [r8 + rcx*8]
0035E071  4D 8D 3C C8                     lea r15, [r8 + rcx*8]
0035E075  3B C3                           cmp eax, ebx
0035E077  0F 85 97 00 00 00               jne 0x14035e114
0035E07D  41 BB 01 00 00 00               mov r11d, 1
0035E083  49 0F BA E6 08                  bt r14, 8
0035E088  0F 82 EC 02 00 00               jb 0x14035e37a
0035E08E  41 8B CB                        mov ecx, r11d
0035E091  49 8D 7F 08                     lea rdi, [r15 + 8]
0035E095  49 8D 47 10                     lea rax, [r15 + 0x10]
0035E099  89 8D 70 01 00 00               mov dword ptr [rbp + 0x170], ecx
0035E09F  F0 48 FF 00                     lock inc qword ptr [rax]
0035E0A3  4C 8B 8D 78 01 00 00            mov r9, qword ptr [rbp + 0x178]
0035E0AA  49 8B D9                        mov rbx, r9
0035E0AD  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
0035E0B2  49 83 7F 48 00                  cmp qword ptr [r15 + 0x48], 0
0035E0B7  0F 84 87 00 00 00               je 0x14035e144
0035E0BD  48 63 C1                        movsxd rax, ecx
0035E0C0  4D 8D 34 C7                     lea r14, [r15 + rax*8]
0035E0C4  4D 8B 66 38                     mov r12, qword ptr [r14 + 0x38]
0035E0C8  41 F6 C4 01                     test r12b, 1
0035E0CC  75 76                           jne 0x14035e144
0035E0CE  4C 3B E3                        cmp r12, rbx
0035E0D1  7D 71                           jge 0x14035e144
0035E0D3  44 8B C1                        mov r8d, ecx
0035E0D6  49 8B D1                        mov rdx, r9
0035E0D9  49 8B 4F 48                     mov rcx, qword ptr [r15 + 0x48]
0035E0DD  E8 5E ED F8 FF                  call 0x1402ece40
0035E0E2  41 BB 01 00 00 00               mov r11d, 1
0035E0E8  48 85 C0                        test rax, rax
0035E0EB  0F 84 9C 13 00 00               je 0x14035f48d
0035E0F1  49 3B C3                        cmp rax, r11
0035E0F4  0F 85 2E 03 00 00               jne 0x14035e428
0035E0FA  49 8B C4                        mov rax, r12
0035E0FD  F0 4D 0F B1 5E 38               lock cmpxchg qword ptr [r14 + 0x38], r11
0035E103  74 3F                           je 0x14035e144
0035E105  4C 8B 8D 78 01 00 00            mov r9, qword ptr [rbp + 0x178]
0035E10C  8B 8D 70 01 00 00               mov ecx, dword ptr [rbp + 0x170]
0035E112  EB B0                           jmp 0x14035e0c4
0035E114  85 C0                           test eax, eax
0035E116  0F 84 44 01 00 00               je 0x14035e260
0035E11C  8D 47 01                        lea eax, [rdi + 1]
0035E11F  41 23 C4                        and eax, r12d
0035E122  8B F8                           mov edi, eax
0035E124  41 3B C1                        cmp eax, r9d
0035E127  0F 85 37 FF FF FF               jne 0x14035e064
0035E12D  48 8B 95 78 01 00 00            mov rdx, qword ptr [rbp + 0x178]
0035E134  4D 8B C6                        mov r8, r14
0035E137  8B CB                           mov ecx, ebx
0035E139  E8 82 EB F8 FF                  call 0x1402eccc0
0035E13E  41 BB 01 00 00 00               mov r11d, 1
0035E144  45 33 D2                        xor r10d, r10d
0035E147  45 8B FB                        mov r15d, r11d
0035E14A  F6 44 24 78 08                  test byte ptr [rsp + 0x78], 8
0035E14F  48 8B DE                        mov rbx, rsi
0035E152  74 69                           je 0x14035e1bd
0035E154  80 66 03 FB                     and byte ptr [rsi + 3], 0xfb
0035E158  B9 F0 FF FF FF                  mov ecx, 0xfffffff0
0035E15D  8B 05 1D 8B C6 00               mov eax, dword ptr [rip + 0xc68b1d]
0035E163  2B CB                           sub ecx, ebx
0035E165  FF C8                           dec eax
0035E167  23 C8                           and ecx, eax
0035E169  74 52                           je 0x14035e1bd
0035E16B  8B D1                           mov edx, ecx
0035E16D  48 03 D3                        add rdx, rbx
0035E170  48 8B CA                        mov rcx, rdx
0035E173  48 2B CB                        sub rcx, rbx
0035E176  48 C1 F9 04                     sar rcx, 4
0035E17A  88 0A                           mov byte ptr [rdx], cl
0035E17C  0F B6 46 02                     movzx eax, byte ptr [rsi + 2]
0035E180  2A C1                           sub al, cl
0035E182  B9 FF 00 00 00                  mov ecx, 0xff
0035E187  88 42 02                        mov byte ptr [rdx + 2], al
0035E18A  0F B6 46 01                     movzx eax, byte ptr [rsi + 1]
0035E18E  88 42 01                        mov byte ptr [rdx + 1], al
0035E191  0F B6 46 03                     movzx eax, byte ptr [rsi + 3]
0035E195  0C 04                           or al, 4
0035E197  88 42 03                        mov byte ptr [rdx + 3], al
0035E19A  8B 46 04                        mov eax, dword ptr [rsi + 4]
0035E19D  89 42 04                        mov dword ptr [rdx + 4], eax
0035E1A0  0F B7 02                        movzx eax, word ptr [rdx]
0035E1A3  66 23 C1                        and ax, cx
0035E1A6  66 83 F8 01                     cmp ax, 1
0035E1AA  76 0E                           jbe 0x14035e1ba
0035E1AC  48 8B C2                        mov rax, rdx
0035E1AF  48 33 05 72 90 C6 00            xor rax, qword ptr [rip + 0xc69072]
0035E1B6  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
0035E1BA  48 8B F2                        mov rsi, rdx
0035E1BD  0F B6 15 A4 0A C7 00            movzx edx, byte ptr [rip + 0xc70aa4]
0035E1C4  4C 8D 66 10                     lea r12, [rsi + 0x10]
0035E1C8  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0035E1CD  49 8B C4                        mov rax, r12
0035E1D0  48 2B C3                        sub rax, rbx
0035E1D3  4C 89 A5 78 01 00 00            mov qword ptr [rbp + 0x178], r12
0035E1DA  83 E0 07                        and eax, 7
0035E1DD  49 8B CC                        mov rcx, r12
0035E1E0  48 2B C8                        sub rcx, rax
0035E1E3  49 8B FA                        mov rdi, r10
0035E1E6  4C 8B C1                        mov r8, rcx
0035E1E9  49 BE 00 00 00 00 00 80 FF FF   movabs r14, 0xffff800000000000
0035E1F3  4C 2B C3                        sub r8, rbx
0035E1F6  84 D2                           test dl, dl
0035E1F8  0F 85 C6 01 00 00               jne 0x14035e3c4
0035E1FE  4D 8B CC                        mov r9, r12
0035E201  49 83 E1 F8                     and r9, 0xfffffffffffffff8
0035E205  4D 2B E9                        sub r13, r9
0035E208  49 2B F1                        sub rsi, r9
0035E20B  4D 03 EC                        add r13, r12
0035E20E  48 03 F3                        add rsi, rbx
0035E211  84 D2                           test dl, dl
0035E213  0F 84 B4 D9 FF FF               je 0x14035bbcd
0035E219  4D 3B CE                        cmp r9, r14
0035E21C  0F 83 36 11 00 00               jae 0x14035f358
0035E222  4D 8B C3                        mov r8, r11
0035E225  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
0035E22A  BA 02 00 00 00                  mov edx, 2
0035E22F  B9 F1 01 00 00                  mov ecx, 0x1f1
0035E234  E8 27 F4 19 00                  call 0x1404fd660
0035E239  CC                              int3
0035E23A  48 83 E8 40                     sub rax, 0x40
0035E23E  0F 85 25 01 00 00               jne 0x14035e369
0035E244  BA 00 02 00 00                  mov edx, 0x200
0035E249  E9 CB FC FF FF                  jmp 0x14035df19
0035E24E  48 85 C0                        test rax, rax
0035E251  0F 84 40 FD FF FF               je 0x14035df97
0035E257  41 83 C8 10                     or r8d, 0x10
0035E25B  E9 37 FD FF FF                  jmp 0x14035df97
0035E260  48 8B 05 F9 0A BA 00            mov rax, qword ptr [rip + 0xba0af9]
0035E267  44 8B 1C C8                     mov r11d, dword ptr [rax + rcx*8]
0035E26B  45 85 DB                        test r11d, r11d
0035E26E  74 21                           je 0x14035e291
0035E270  45 89 1F                        mov dword ptr [r15], r11d
0035E273  48 8B 05 E6 0A BA 00            mov rax, qword ptr [rip + 0xba0ae6]
0035E27A  48 8B 54 C8 48                  mov rdx, qword ptr [rax + rcx*8 + 0x48]
0035E27F  48 85 D2                        test rdx, rdx
0035E282  0F 84 DC FD FF FF               je 0x14035e064
0035E288  49 89 57 48                     mov qword ptr [r15 + 0x48], rdx
0035E28C  E9 D3 FD FF FF                  jmp 0x14035e064
0035E291  49 8D 42 FF                     lea rax, [r10 - 1]
0035E295  48 3B D0                        cmp rdx, rax
0035E298  0F 84 7E FE FF FF               je 0x14035e11c
0035E29E  48 8D 0D 5B CA B9 00            lea rcx, [rip + 0xb9ca5b]
0035E2A5  48 C7 85 80 00 00 00 00 00 00 00  mov qword ptr [rbp + 0x80], 0
0035E2B0  48 89 8D 88 00 00 00            mov qword ptr [rbp + 0x88], rcx
0035E2B7  90                              nop
0035E2B8  44 0F 20 C0                     mov rax, cr8
0035E2BC  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0035E2C1  BA 02 00 00 00                  mov edx, 2
0035E2C6  44 0F 22 C2                     mov cr8, rdx
0035E2CA  83 3D 4F 8A C6 00 00            cmp dword ptr [rip + 0xc68a4f], 0
0035E2D1  0F 85 D4 00 00 00               jne 0x14035e3ab
0035E2D7  F6 05 28 88 C6 00 21            test byte ptr [rip + 0xc68828], 0x21
0035E2DE  88 85 90 00 00 00               mov byte ptr [rbp + 0x90], al
0035E2E4  0F 85 9F 00 00 00               jne 0x14035e389
0035E2EA  48 8D 95 80 00 00 00            lea rdx, [rbp + 0x80]
0035E2F1  48 87 15 08 CA B9 00            xchg qword ptr [rip + 0xb9ca08], rdx
0035E2F8  48 85 D2                        test rdx, rdx
0035E2FB  0F 85 E7 00 00 00               jne 0x14035e3e8
0035E301  8B C7                           mov eax, edi
0035E303  48 8D 0C 80                     lea rcx, [rax + rax*4]
0035E307  48 8B 05 52 0A BA 00            mov rax, qword ptr [rip + 0xba0a52]
0035E30E  48 C1 E1 04                     shl rcx, 4
0035E312  48 03 C1                        add rax, rcx
0035E315  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0035E31A  83 38 00                        cmp dword ptr [rax], 0
0035E31D  75 2A                           jne 0x14035e349
0035E31F  8B CB                           mov ecx, ebx
0035E321  E8 CA E8 F8 FF                  call 0x1402ecbf0
0035E326  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0035E32B  48 89 41 48                     mov qword ptr [rcx + 0x48], rax
0035E32F  49 89 47 48                     mov qword ptr [r15 + 0x48], rax
0035E333  8B C7                           mov eax, edi
0035E335  48 8D 0C 80                     lea rcx, [rax + rax*4]
0035E339  48 8B 05 20 0A BA 00            mov rax, qword ptr [rip + 0xba0a20]
0035E340  48 03 C9                        add rcx, rcx
0035E343  89 1C C8                        mov dword ptr [rax + rcx*8], ebx
0035E346  41 89 1F                        mov dword ptr [r15], ebx
0035E349  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
0035E350  E8 8B 49 FE FF                  call 0x140342ce0
0035E355  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
0035E359  44 8B 8D 70 01 00 00            mov r9d, dword ptr [rbp + 0x170]
0035E360  4C 8B 55 88                     mov r10, qword ptr [rbp - 0x78]
0035E364  E9 FB FC FF FF                  jmp 0x14035e064
0035E369  48 83 F8 40                     cmp rax, 0x40
0035E36D  0F 85 AB F5 FF FF               jne 0x14035d91e
0035E373  33 D2                           xor edx, edx
0035E375  E9 9F FB FF FF                  jmp 0x14035df19
0035E37A  33 C9                           xor ecx, ecx
0035E37C  49 8D 7F 20                     lea rdi, [r15 + 0x20]
0035E380  49 8D 47 28                     lea rax, [r15 + 0x28]
0035E384  E9 10 FD FF FF                  jmp 0x14035e099
0035E389  8B 05 C9 FA BA 00               mov eax, dword ptr [rip + 0xbafac9]
0035E38F  85 C0                           test eax, eax
0035E391  0F 85 53 FF FF FF               jne 0x14035e2ea
0035E397  48 8B D1                        mov rdx, rcx
0035E39A  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
0035E3A1  E8 AA 74 F1 FF                  call 0x140275850
0035E3A6  E9 56 FF FF FF                  jmp 0x14035e301
0035E3AB  0F B6 C8                        movzx ecx, al
0035E3AE  E8 49 73 19 00                  call 0x1404f56fc
0035E3B3  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0035E3B8  48 8D 0D 41 C9 B9 00            lea rcx, [rip + 0xb9c941]
0035E3BF  E9 13 FF FF FF                  jmp 0x14035e2d7
0035E3C4  49 3B DE                        cmp rbx, r14
0035E3C7  0F 83 61 0F 00 00               jae 0x14035f32e
0035E3CD  4C 8B CB                        mov r9, rbx
0035E3D0  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
0035E3D5  4D 8B C3                        mov r8, r11
0035E3D8  BA 02 00 00 00                  mov edx, 2
0035E3DD  B9 F1 01 00 00                  mov ecx, 0x1f1
0035E3E2  E8 79 F2 19 00                  call 0x1404fd660
0035E3E7  CC                              int3
0035E3E8  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
0035E3EF  E8 BC 9A EF FF                  call 0x140257eb0
0035E3F4  E9 08 FF FF FF                  jmp 0x14035e301
0035E3F9  4C 3B E2                        cmp r12, rdx
0035E3FC  0F 83 77 0F 00 00               jae 0x14035f379
0035E402  4D 8B CC                        mov r9, r12
0035E405  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0035E40A  BA 02 00 00 00                  mov edx, 2
0035E40F  B9 F1 01 00 00                  mov ecx, 0x1f1
0035E414  E8 47 F2 19 00                  call 0x1404fd660
0035E419  CC                              int3
0035E41A  48 8D 4D 68                     lea rcx, [rbp + 0x68]
0035E41E  E8 8D 9A EF FF                  call 0x140257eb0
0035E423  E9 EB F6 FF FF                  jmp 0x14035db13
0035E428  4C 8B E0                        mov r12, rax
0035E42B  F0 4D 0F C1 66 38               lock xadd qword ptr [r14 + 0x38], r12
0035E431  48 8B 1F                        mov rbx, qword ptr [rdi]
0035E434  4C 8B 8D 78 01 00 00            mov r9, qword ptr [rbp + 0x178]
0035E43B  8B 8D 70 01 00 00               mov ecx, dword ptr [rbp + 0x170]
0035E441  E9 82 FC FF FF                  jmp 0x14035e0c8
0035E446  F3 48 0F BC CA                  tzcnt rcx, rdx
0035E44B  48 0F BD C2                     bsr rax, rdx
0035E44F  89 45 24                        mov dword ptr [rbp + 0x24], eax
0035E452  2B C1                           sub eax, ecx
0035E454  FF C0                           inc eax
0035E456  3B F0                           cmp esi, eax
0035E458  0F 42 C6                        cmovb eax, esi
0035E45B  44 0F AF C8                     imul r9d, eax
0035E45F  41 C1 E9 08                     shr r9d, 8
0035E463  44 03 C9                        add r9d, ecx
0035E466  41 8B C9                        mov ecx, r9d
0035E469  44 89 8D 78 01 00 00            mov dword ptr [rbp + 0x178], r9d
0035E470  48 D3 CA                        ror rdx, cl
0035E473  F3 4C 0F BC D2                  tzcnt r10, rdx
0035E478  45 03 D1                        add r10d, r9d
0035E47B  E9 4D DF FF FF                  jmp 0x14035c3cd
0035E480  41 B9 03 00 00 00               mov r9d, 3
0035E486  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0035E48B  48 8D 47 D0                     lea rax, [rdi - 0x30]
0035E48F  4C 8B C7                        mov r8, rdi
0035E492  48 C1 E8 08                     shr rax, 8
0035E496  0F B6 D0                        movzx edx, al
0035E499  0F B6 47 E8                     movzx eax, byte ptr [rdi - 0x18]
0035E49D  41 8D 49 15                     lea ecx, [r9 + 0x15]
0035E4A1  48 33 D0                        xor rdx, rax
0035E4A4  0F B6 05 A1 89 C6 00            movzx eax, byte ptr [rip + 0xc689a1]
0035E4AB  48 33 D0                        xor rdx, rax
0035E4AE  48 8D 05 4B 1B CA FF            lea rax, [rip - 0x35e4b5]
0035E4B5  48 8B 94 D0 00 78 FC 00         mov rdx, qword ptr [rax + rdx*8 + 0xfc7800]
0035E4BD  E8 9E F1 19 00                  call 0x1404fd660
0035E4C2  CC                              int3
0035E4C3  48 8D 44 24 5A                  lea rax, [rsp + 0x5a]
0035E4C8  33 D2                           xor edx, edx
0035E4CA  4C 8D 4C 24 3A                  lea r9, [rsp + 0x3a]
0035E4CF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0035E4D4  4C 8D 45 98                     lea r8, [rbp - 0x68]
0035E4D8  49 8B CE                        mov rcx, r14
0035E4DB  E8 A0 5B 82 00                  call 0x140b84080
0035E4E0  85 C0                           test eax, eax
0035E4E2  0F 88 2B FB FF FF               js 0x14035e013
0035E4E8  80 7C 24 3A 00                  cmp byte ptr [rsp + 0x3a], 0
0035E4ED  8B 55 98                        mov edx, dword ptr [rbp - 0x68]
0035E4F0  74 06                           je 0x14035e4f8
0035E4F2  83 CA 08                        or edx, 8
0035E4F5  89 55 98                        mov dword ptr [rbp - 0x68], edx
0035E4F8  48 8B 85 78 01 00 00            mov rax, qword ptr [rbp + 0x178]
0035E4FF  4C 8D 4E 10                     lea r9, [rsi + 0x10]
0035E503  B9 20 0E 00 00                  mov ecx, 0xe20
0035E508  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0035E50D  44 8B C3                        mov r8d, ebx
0035E510  E8 D7 E9 F8 FF                  call 0x1402eceec
0035E515  E9 F9 FA FF FF                  jmp 0x14035e013
0035E51A  F3 48 0F BC CA                  tzcnt rcx, rdx
0035E51F  48 0F BD C2                     bsr rax, rdx
0035E523  89 45 14                        mov dword ptr [rbp + 0x14], eax
0035E526  2B C1                           sub eax, ecx
0035E528  FF C0                           inc eax
0035E52A  44 3B D0                        cmp r10d, eax
0035E52D  41 0F 42 C2                     cmovb eax, r10d
0035E531  44 0F AF C8                     imul r9d, eax
0035E535  41 C1 E9 08                     shr r9d, 8
0035E539  44 03 C9                        add r9d, ecx
0035E53C  41 8B C9                        mov ecx, r9d
0035E53F  44 89 8D 78 01 00 00            mov dword ptr [rbp + 0x178], r9d
0035E546  48 D3 CA                        ror rdx, cl
0035E549  F3 4C 0F BC D2                  tzcnt r10, rdx
0035E54E  45 03 D1                        add r10d, r9d
0035E551  E9 98 E1 FF FF                  jmp 0x14035c6ee
0035E556  8D 46 0F                        lea eax, [rsi + 0xf]
0035E559  C1 E8 04                        shr eax, 4
0035E55C  42 0F B6 94 10 80 0B 01 00      movzx edx, byte ptr [rax + r10 + 0x10b80]
0035E565  41 0F B7 84 52 C0 C3 01 00      movzx eax, word ptr [r10 + rdx*2 + 0x1c3c0]
0035E56E  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0035E573  8D 42 DF                        lea eax, [rdx - 0x21]
0035E576  49 8B 4F 38                     mov rcx, qword ptr [r15 + 0x38]
0035E57A  89 85 70 01 00 00               mov dword ptr [rbp + 0x170], eax
0035E580  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
0035E585  48 85 C9                        test rcx, rcx
0035E588  74 67                           je 0x14035e5f1
0035E58A  48 FF C0                        inc rax
0035E58D  48 C1 E0 06                     shl rax, 6
0035E591  48 03 C1                        add rax, rcx
0035E594  48 89 85 78 01 00 00            mov qword ptr [rbp + 0x178], rax
0035E59B  FF 40 14                        inc dword ptr [rax + 0x14]
0035E59E  66 83 38 00                     cmp word ptr [rax], 0
0035E5A2  76 66                           jbe 0x14035e60a
0035E5A4  48 8B C8                        mov rcx, rax
0035E5A7  E8 C4 BF 35 00                  call 0x1406ba570
0035E5AC  48 8B F0                        mov rsi, rax
0035E5AF  48 85 C0                        test rax, rax
0035E5B2  74 4C                           je 0x14035e600
0035E5B4  4C 8B 5C 24 78                  mov r11, qword ptr [rsp + 0x78]
0035E5B9  41 F6 C3 02                     test r11b, 2
0035E5BD  75 1C                           jne 0x14035e5db
0035E5BF  48 85 F6                        test rsi, rsi
0035E5C2  74 20                           je 0x14035e5e4
0035E5C4  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0035E5C9  48 8D 4E 10                     lea rcx, [rsi + 0x10]
0035E5CD  48 83 C2 F0                     add rdx, -0x10
0035E5D1  E8 3A D6 35 00                  call 0x1406bbc10
0035E5D6  4C 8B 5C 24 78                  mov r11, qword ptr [rsp + 0x78]
0035E5DB  48 85 F6                        test rsi, rsi
0035E5DE  0F 85 21 F3 FF FF               jne 0x14035d905
0035E5E4  4C 8D 15 15 1A CA FF            lea r10, [rip - 0x35e5eb]
0035E5EB  41 B8 01 00 00 00               mov r8d, 1
0035E5F1  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0035E5F6  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
0035E5FB  E9 B3 DB FF FF                  jmp 0x14035c1b3
0035E600  48 8B 85 78 01 00 00            mov rax, qword ptr [rbp + 0x178]
0035E607  45 33 C9                        xor r9d, r9d
0035E60A  FF 40 18                        inc dword ptr [rax + 0x18]
0035E60D  44 0F B7 40 10                  movzx r8d, word ptr [rax + 0x10]
0035E612  0F B7 08                        movzx ecx, word ptr [rax]
0035E615  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0035E61A  90                              nop
0035E61B  4C 89 4D F8                     mov qword ptr [rbp - 8], r9
0035E61F  4C 89 4D 50                     mov qword ptr [rbp + 0x50], r9
0035E623  41 3B C8                        cmp ecx, r8d
0035E626  0F 82 A2 0A 00 00               jb 0x14035f0ce
0035E62C  49 8B F1                        mov rsi, r9
0035E62F  EB 83                           jmp 0x14035e5b4
0035E631  40 F6 C6 C0                     test sil, 0xc0
0035E635  0F 95 C1                        setne cl
0035E638  0F BA E0 09                     bt eax, 9
0035E63C  0F 92 C0                        setb al
0035E63F  84 C8                           test al, cl
0035E641  74 0B                           je 0x14035e64e
0035E643  49 8B D7                        mov rdx, r15
0035E646  49 8B CE                        mov rcx, r14
0035E649  E8 8E 6C 14 00                  call 0x1404a52dc
0035E64E  8B 05 7C 85 C6 00               mov eax, dword ptr [rip + 0xc6857c]
0035E654  A8 01                           test al, 1
0035E656  74 0B                           je 0x14035e663
0035E658  49 8B D7                        mov rdx, r15
0035E65B  49 8B CE                        mov rcx, r14
0035E65E  E8 A9 A0 17 00                  call 0x1404d870c
0035E663  49 8B D7                        mov rdx, r15
0035E666  49 8B CE                        mov rcx, r14
0035E669  E8 92 E3 13 00                  call 0x14049ca00
0035E66E  8B 05 5C 85 C6 00               mov eax, dword ptr [rip + 0xc6855c]
0035E674  A8 02                           test al, 2
0035E676  0F 84 60 E2 FF FF               je 0x14035c8dc
0035E67C  49 8B D7                        mov rdx, r15
0035E67F  49 8B CE                        mov rcx, r14
0035E682  E8 75 E2 18 00                  call 0x1404ec8fc
0035E687  E9 50 E2 FF FF                  jmp 0x14035c8dc
0035E68C  48 85 D2                        test rdx, rdx
0035E68F  74 03                           je 0x14035e694
0035E691  44 8B EE                        mov r13d, esi
0035E694  45 8B CD                        mov r9d, r13d
0035E697  4D 8B C4                        mov r8, r12
0035E69A  BA 0D 00 00 00                  mov edx, 0xd
0035E69F  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0035E6A4  B9 C2 00 00 00                  mov ecx, 0xc2
0035E6A9  E8 B2 EF 19 00                  call 0x1404fd660
0035E6AE  CC                              int3
0035E6AF  4D 8B EB                        mov r13, r11
0035E6B2  4F 8D 34 1A                     lea r14, [r10 + r11]
0035E6B6  41 0F 0D 0E                     prefetchw byte ptr [r14]
0035E6BA  4D 8B 3E                        mov r15, qword ptr [r14]
0035E6BD  E9 A2 F0 FF FF                  jmp 0x14035d764
0035E6C2  8B D6                           mov edx, esi
0035E6C4  48 8D 44 24 5C                  lea rax, [rsp + 0x5c]
0035E6C9  83 E2 10                        and edx, 0x10
0035E6CC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0035E6D1  4C 8D 4C 24 3C                  lea r9, [rsp + 0x3c]
0035E6D6  48 8B CE                        mov rcx, rsi
0035E6D9  4C 8D 45 A4                     lea r8, [rbp - 0x5c]
0035E6DD  E8 9E 59 82 00                  call 0x140b84080
0035E6E2  85 C0                           test eax, eax
0035E6E4  0F 88 33 E2 FF FF               js 0x14035c91d
0035E6EA  80 7C 24 3C 00                  cmp byte ptr [rsp + 0x3c], 0
0035E6EF  8B 55 A4                        mov edx, dword ptr [rbp - 0x5c]
0035E6F2  74 06                           je 0x14035e6fa
0035E6F4  83 CA 08                        or edx, 8
0035E6F7  89 55 A4                        mov dword ptr [rbp - 0x5c], edx
0035E6FA  B9 22 0E 00 00                  mov ecx, 0xe22
0035E6FF  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0035E704  4C 8B CF                        mov r9, rdi
0035E707  44 8B C3                        mov r8d, ebx
0035E70A  E8 DD E7 F8 FF                  call 0x1402eceec
0035E70F  E9 09 E2 FF FF                  jmp 0x14035c91d
0035E714  49 63 C1                        movsxd rax, r9d
0035E717  F6 44 C1 38 01                  test byte ptr [rcx + rax*8 + 0x38], 1
0035E71C  4C 8D 1C C1                     lea r11, [rcx + rax*8]
0035E720  0F 85 5B E3 FF FF               jne 0x14035ca81
0035E726  49 8B 43 38                     mov rax, qword ptr [r11 + 0x38]
0035E72A  4E 8D 14 BD 3F 00 00 00         lea r10, [r15*4 + 0x3f]
0035E732  49 83 E2 C0                     and r10, 0xffffffffffffffc0
0035E736  BB 80 00 00 00                  mov ebx, 0x80
0035E73B  49 83 FA 40                     cmp r10, 0x40
0035E73F  4C 0F 44 D3                     cmove r10, rbx
0035E743  49 8D 1C 12                     lea rbx, [r10 + rdx]
0035E747  48 3B D0                        cmp rdx, rax
0035E74A  0F 8D 31 E3 FF FF               jge 0x14035ca81
0035E750  48 3B D8                        cmp rbx, rax
0035E753  0F 8D 28 E3 FF FF               jge 0x14035ca81
0035E759  F0 49 0F B1 5B 38               lock cmpxchg qword ptr [r11 + 0x38], rbx
0035E75F  0F 84 2D 01 00 00               je 0x14035e892
0035E765  49 8B 10                        mov rdx, qword ptr [r8]
0035E768  EB D9                           jmp 0x14035e743
0035E76A  41 8B D5                        mov edx, r13d
0035E76D  45 8B D5                        mov r10d, r13d
0035E770  E9 84 E7 FF FF                  jmp 0x14035cef9
0035E775  4C 8B E0                        mov r12, rax
0035E778  F0 4D 0F C1 67 38               lock xadd qword ptr [r15 + 0x38], r12
0035E77E  48 8B 33                        mov rsi, qword ptr [rbx]
0035E781  8B 8D 70 01 00 00               mov ecx, dword ptr [rbp + 0x170]
0035E787  4C 8B 8D 78 01 00 00            mov r9, qword ptr [rbp + 0x178]
0035E78E  E9 7C ED FF FF                  jmp 0x14035d50f
0035E793  49 8B CC                        mov rcx, r12
0035E796  E8 75 DC 13 00                  call 0x14049c410
0035E79B  85 C0                           test eax, eax
0035E79D  0F 84 DC E7 FF FF               je 0x14035cf7f
0035E7A3  E9 58 E0 FF FF                  jmp 0x14035c800
0035E7A8  49 8B D6                        mov rdx, r14
0035E7AB  48 8B CB                        mov rcx, rbx
0035E7AE  E8 E9 E0 F8 FF                  call 0x1402ec89c
0035E7B3  E9 AB E3 FF FF                  jmp 0x14035cb63
0035E7B8  41 8B D6                        mov edx, r14d
0035E7BB  48 8D 44 24 59                  lea rax, [rsp + 0x59]
0035E7C0  83 E2 10                        and edx, 0x10
0035E7C3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0035E7C8  4C 8D 4C 24 39                  lea r9, [rsp + 0x39]
0035E7CD  49 8B CE                        mov rcx, r14
0035E7D0  4C 8D 45 94                     lea r8, [rbp - 0x6c]
0035E7D4  E8 A7 58 82 00                  call 0x140b84080
0035E7D9  85 C0                           test eax, eax
0035E7DB  0F 88 74 EC FF FF               js 0x14035d455
0035E7E1  8B 55 94                        mov edx, dword ptr [rbp - 0x6c]
0035E7E4  40 38 74 24 39                  cmp byte ptr [rsp + 0x39], sil
0035E7E9  74 06                           je 0x14035e7f1
0035E7EB  83 CA 08                        or edx, 8
0035E7EE  89 55 94                        mov dword ptr [rbp - 0x6c], edx
0035E7F1  48 8B 85 78 01 00 00            mov rax, qword ptr [rbp + 0x178]
0035E7F8  B9 20 0E 00 00                  mov ecx, 0xe20
0035E7FD  4C 8B CF                        mov r9, rdi
0035E800  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0035E805  44 8B C3                        mov r8d, ebx
0035E808  E8 DF E6 F8 FF                  call 0x1402eceec
0035E80D  E9 43 EC FF FF                  jmp 0x14035d455
0035E812  48 85 F6                        test rsi, rsi
0035E815  0F 84 D1 D2 FF FF               je 0x14035baec
0035E81B  41 8B D1                        mov edx, r9d
0035E81E  8B CB                           mov ecx, ebx
0035E820  E8 27 19 0A 00                  call 0x14040014c
0035E825  85 C0                           test eax, eax
0035E827  0F 85 F3 D6 FF FF               jne 0x14035bf20
0035E82D  48 8D 46 10                     lea rax, [rsi + 0x10]
0035E831  4C 3B C8                        cmp r9, rax
0035E834  0F 82 B2 D2 FF FF               jb 0x14035baec
0035E83A  48 8D 46 20                     lea rax, [rsi + 0x20]
0035E83E  4C 3B C8                        cmp r9, rax
0035E841  0F 83 A5 D2 FF FF               jae 0x14035baec
0035E847  E9 D4 D6 FF FF                  jmp 0x14035bf20
0035E84C  80 7B 16 01                     cmp byte ptr [rbx + 0x16], 1
0035E850  0F 84 FE D4 FF FF               je 0x14035bd54
0035E856  8B C6                           mov eax, esi
0035E858  8B CE                           mov ecx, esi
0035E85A  C1 E8 06                        shr eax, 6
0035E85D  83 E1 3F                        and ecx, 0x3f
0035E860  48 8B 54 C3 40                  mov rdx, qword ptr [rbx + rax*8 + 0x40]
0035E865  49 C7 C0 FE FF FF FF            mov r8, 0xfffffffffffffffe
0035E86C  49 D3 C0                        rol r8, cl
0035E86F  48 8D 0C C3                     lea rcx, [rbx + rax*8]
0035E873  48 8B C2                        mov rax, rdx
0035E876  49 23 C0                        and rax, r8
0035E879  49 F7 D0                        not r8
0035E87C  48 89 41 40                     mov qword ptr [rcx + 0x40], rax
0035E880  4C 85 C2                        test rdx, r8
0035E883  0F 84 49 D8 FF FF               je 0x14035c0d2
0035E889  66 FF 43 20                     inc word ptr [rbx + 0x20]
0035E88D  E9 F5 D5 FF FF                  jmp 0x14035be87
0035E892  48 8B 49 48                     mov rcx, qword ptr [rcx + 0x48]
0035E896  48 2B C3                        sub rax, rbx
0035E899  48 8B D0                        mov rdx, rax
0035E89C  45 8B C1                        mov r8d, r9d
0035E89F  48 F7 DA                        neg rdx
0035E8A2  48 85 C0                        test rax, rax
0035E8A5  48 0F 49 D0                     cmovns rdx, rax
0035E8A9  E8 AE 1C 15 00                  call 0x1404b055c
0035E8AE  E9 CE E1 FF FF                  jmp 0x14035ca81
0035E8B3  49 8B CE                        mov rcx, r14
0035E8B6  E8 79 7A 19 00                  call 0x1404f6334
0035E8BB  E9 8A D4 FF FF                  jmp 0x14035bd4a
0035E8C0  49 8B 49 48                     mov rcx, qword ptr [r9 + 0x48]
0035E8C4  48 2B C3                        sub rax, rbx
0035E8C7  48 8B D0                        mov rdx, rax
0035E8CA  48 F7 DA                        neg rdx
0035E8CD  48 85 C0                        test rax, rax
0035E8D0  48 0F 49 D0                     cmovns rdx, rax
0035E8D4  E8 83 1C 15 00                  call 0x1404b055c
0035E8D9  E9 AC E1 FF FF                  jmp 0x14035ca8a
0035E8DE  80 7F 16 01                     cmp byte ptr [rdi + 0x16], 1
0035E8E2  0F 84 0F E4 FF FF               je 0x14035ccf7
0035E8E8  8B CB                           mov ecx, ebx
0035E8EA  48 8B C3                        mov rax, rbx
0035E8ED  48 C1 E8 06                     shr rax, 6
0035E8F1  83 E1 3F                        and ecx, 0x3f
0035E8F4  48 8B 54 C7 40                  mov rdx, qword ptr [rdi + rax*8 + 0x40]
0035E8F9  49 C7 C1 FE FF FF FF            mov r9, 0xfffffffffffffffe
0035E900  49 D3 C1                        rol r9, cl
0035E903  4C 8B C3                        mov r8, rbx
0035E906  48 8D 0C C7                     lea rcx, [rdi + rax*8]
0035E90A  48 8B C2                        mov rax, rdx
0035E90D  49 23 C1                        and rax, r9
0035E910  49 F7 D1                        not r9
0035E913  48 89 41 40                     mov qword ptr [rcx + 0x40], rax
0035E917  4C 85 CA                        test rdx, r9
0035E91A  0F 84 4D EA FF FF               je 0x14035d36d
0035E920  66 FF 47 20                     inc word ptr [rdi + 0x20]
0035E924  E9 3A E2 FF FF                  jmp 0x14035cb63
0035E929  41 8B 87 10 02 00 00            mov eax, dword ptr [r15 + 0x210]
0035E930  4C 8B C2                        mov r8, rdx
0035E933  48 3B D0                        cmp rdx, rax
0035E936  49 8B CF                        mov rcx, r15
0035E939  49 8B D4                        mov rdx, r12
0035E93C  77 7C                           ja 0x14035e9ba
0035E93E  E8 3D 7C FC FF                  call 0x140326580
0035E943  48 8B F0                        mov rsi, rax
0035E946  E9 B0 EF FF FF                  jmp 0x14035d8fb
0035E94B  48 8B CE                        mov rcx, rsi
0035E94E  E8 E1 79 19 00                  call 0x1404f6334
0035E953  E9 95 E3 FF FF                  jmp 0x14035cced
0035E958  41 8B 87 10 02 00 00            mov eax, dword ptr [r15 + 0x210]
0035E95F  4C 8B C7                        mov r8, rdi
0035E962  48 8B D6                        mov rdx, rsi
0035E965  49 8B CF                        mov rcx, r15
0035E968  48 3B F8                        cmp rdi, rax
0035E96B  77 57                           ja 0x14035e9c4
0035E96D  E8 0E 7C FC FF                  call 0x140326580
0035E972  E9 B1 D7 FF FF                  jmp 0x14035c128
0035E977  41 B9 03 00 00 00               mov r9d, 3
0035E97D  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0035E982  48 8D 47 D0                     lea rax, [rdi - 0x30]
0035E986  4C 8B C7                        mov r8, rdi
0035E989  48 C1 E8 08                     shr rax, 8
0035E98D  0F B6 D0                        movzx edx, al
0035E990  0F B6 47 E8                     movzx eax, byte ptr [rdi - 0x18]
0035E994  41 8D 49 15                     lea ecx, [r9 + 0x15]
0035E998  48 33 D0                        xor rdx, rax
0035E99B  0F B6 05 AA 84 C6 00            movzx eax, byte ptr [rip + 0xc684aa]
0035E9A2  48 33 D0                        xor rdx, rax
0035E9A5  48 8D 05 54 16 CA FF            lea rax, [rip - 0x35e9ac]
0035E9AC  48 8B 94 D0 00 78 FC 00         mov rdx, qword ptr [rax + rdx*8 + 0xfc7800]
0035E9B4  E8 A7 EC 19 00                  call 0x1404fd660
0035E9B9  CC                              int3
0035E9BA  E8 9D D3 F8 FF                  call 0x1402ebd5c
0035E9BF  E9 A5 EF FF FF                  jmp 0x14035d969
0035E9C4  E8 93 D3 F8 FF                  call 0x1402ebd5c
0035E9C9  E9 5A D7 FF FF                  jmp 0x14035c128
0035E9CE  49 8B CB                        mov rcx, r11
0035E9D1  E8 5E 79 19 00                  call 0x1404f6334
0035E9D6  4D 8D 9F 40 03 00 00            lea r11, [r15 + 0x340]
0035E9DD  E9 68 D8 FF FF                  jmp 0x14035c24a
0035E9E2  49 8B CB                        mov rcx, r11
0035E9E5  E8 4A 79 19 00                  call 0x1404f6334
0035E9EA  4D 8D 9F 40 03 00 00            lea r11, [r15 + 0x340]
0035E9F1  E9 87 DB FF FF                  jmp 0x14035c57d
0035E9F6  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0035E9FA  E8 95 39 04 00                  call 0x1403a2394
0035E9FF  4D 8D 74 24 F0                  lea r14, [r12 - 0x10]
0035EA04  E9 F7 DD FF FF                  jmp 0x14035c800
0035EA09  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0035EA0D  E8 82 39 04 00                  call 0x1403a2394
0035EA12  E9 E1 E7 FF FF                  jmp 0x14035d1f8
0035EA17  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
0035EA1C  E9 53 DA FF FF                  jmp 0x14035c474
0035EA21  8B 03                           mov eax, dword ptr [rbx]
0035EA23  4C 8D 43 10                     lea r8, [rbx + 0x10]
0035EA27  8B C8                           mov ecx, eax
0035EA29  C1 E9 10                        shr ecx, 0x10
0035EA2C  0F BA E0 0E                     bt eax, 0xe
0035EA30  73 04                           jae 0x14035ea36
0035EA32  4C 8D 43 18                     lea r8, [rbx + 0x18]
0035EA36  4D 3B C4                        cmp r8, r12
0035EA39  0F 82 F2 00 00 00               jb 0x14035eb31
0035EA3F  49 8D 84 24 FF 0F 00 00         lea rax, [r12 + 0xfff]
0035EA47  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
0035EA4D  4E 8D 04 27                     lea r8, [rdi + r12]
0035EA51  4C 3B C0                        cmp r8, rax
0035EA54  0F 82 FA 00 00 00               jb 0x14035eb54
0035EA5A  F7 03 00 40 00 00               test dword ptr [rbx], 0x4000
0035EA60  74 1C                           je 0x14035ea7e
0035EA62  4C 8B C6                        mov r8, rsi
0035EA65  41 B9 01 00 00 00               mov r9d, 1
0035EA6B  49 C1 E8 08                     shr r8, 8
0035EA6F  48 8B D7                        mov rdx, rdi
0035EA72  41 83 E0 01                     and r8d, 1
0035EA76  49 8B CC                        mov rcx, r12
0035EA79  E8 42 A5 85 00                  call 0x140bb8fc0
0035EA7E  8B 05 C8 66 C6 00               mov eax, dword ptr [rip + 0xc666c8]
0035EA84  4C 8D 77 0F                     lea r14, [rdi + 0xf]
0035EA88  8B 7B 04                        mov edi, dword ptr [rbx + 4]
0035EA8B  49 83 E6 F0                     and r14, 0xfffffffffffffff0
0035EA8F  44 89 6D 9C                     mov dword ptr [rbp - 0x64], r13d
0035EA93  C6 44 24 3B 00                  mov byte ptr [rsp + 0x3b], 0
0035EA98  C6 44 24 5B 00                  mov byte ptr [rsp + 0x5b], 0
0035EA9D  3B F8                           cmp edi, eax
0035EA9F  75 01                           jne 0x14035eaa2
0035EAA1  CC                              int3
0035EAA2  8B 05 5C 80 C6 00               mov eax, dword ptr [rip + 0xc6805c]
0035EAA8  A8 41                           test al, 0x41
0035EAAA  0F 85 12 01 00 00               jne 0x14035ebc2
0035EAB0  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0035EAB8  48 83 E6 FB                     and rsi, 0xfffffffffffffffb
0035EABC  4C 8B 05 95 02 BA 00            mov r8, qword ptr [rip + 0xba0295]
0035EAC3  8B C8                           mov ecx, eax
0035EAC5  48 8D 05 34 15 CA FF            lea rax, [rip - 0x35eacc]
0035EACC  4C 8B 9C C8 20 AD EF 00         mov r11, qword ptr [rax + rcx*8 + 0xefad20]
0035EAD4  48 69 CF 5F 9E 00 00            imul rcx, rdi, 0x9e5f
0035EADB  48 8B D1                        mov rdx, rcx
0035EADE  48 C1 EA 20                     shr rdx, 0x20
0035EAE2  33 D1                           xor edx, ecx
0035EAE4  41 23 D0                        and edx, r8d
0035EAE7  44 8B D2                        mov r10d, edx
0035EAEA  8B C2                           mov eax, edx
0035EAEC  48 8D 0C 80                     lea rcx, [rax + rax*4]
0035EAF0  48 03 C9                        add rcx, rcx
0035EAF3  41 8B 04 CB                     mov eax, dword ptr [r11 + rcx*8]
0035EAF7  4D 8D 0C CB                     lea r9, [r11 + rcx*8]
0035EAFB  3B C7                           cmp eax, edi
0035EAFD  74 78                           je 0x14035eb77
0035EAFF  85 C0                           test eax, eax
0035EB01  0F 84 88 00 00 00               je 0x14035eb8f
0035EB07  8D 42 01                        lea eax, [rdx + 1]
0035EB0A  41 23 C0                        and eax, r8d
0035EB0D  8B D0                           mov edx, eax
0035EB0F  41 3B C2                        cmp eax, r10d
0035EB12  75 D6                           jne 0x14035eaea
0035EB14  4C 8B C6                        mov r8, rsi
0035EB17  49 8B D6                        mov rdx, r14
0035EB1A  8B CF                           mov ecx, edi
0035EB1C  E8 DF 27 00 00                  call 0x140361300
0035EB21  48 8B D3                        mov rdx, rbx
0035EB24  49 8B CF                        mov rcx, r15
0035EB27  E8 D4 0A 00 00                  call 0x14035f600
0035EB2C  E9 32 E0 FF FF                  jmp 0x14035cb63
0035EB31  41 38 08                        cmp byte ptr [r8], cl
0035EB34  0F 84 5E 09 00 00               je 0x14035f498
0035EB3A  44 8B 0B                        mov r9d, dword ptr [rbx]
0035EB3D  49 8B D4                        mov rdx, r12
0035EB40  B9 C1 00 00 00                  mov ecx, 0xc1
0035EB45  48 C7 44 24 20 23 00 00 00      mov qword ptr [rsp + 0x20], 0x23
0035EB4E  E8 0D EB 19 00                  call 0x1404fd660
0035EB53  CC                              int3
0035EB54  41 38 08                        cmp byte ptr [r8], cl
0035EB57  0F 84 43 09 00 00               je 0x14035f4a0
0035EB5D  44 8B 0B                        mov r9d, dword ptr [rbx]
0035EB60  49 8B D4                        mov rdx, r12
0035EB63  B9 C1 00 00 00                  mov ecx, 0xc1
0035EB68  48 C7 44 24 20 24 00 00 00      mov qword ptr [rsp + 0x20], 0x24
0035EB71  E8 EA EA 19 00                  call 0x1404fd660
0035EB76  CC                              int3
0035EB77  48 C1 EE 08                     shr rsi, 8
0035EB7B  4D 8B C1                        mov r8, r9
0035EB7E  F7 D6                           not esi
0035EB80  49 8B D6                        mov rdx, r14
0035EB83  83 E6 01                        and esi, 1
0035EB86  8B CE                           mov ecx, esi
0035EB88  E8 E3 29 00 00                  call 0x140361570
0035EB8D  EB 92                           jmp 0x14035eb21
0035EB8F  48 8B 05 CA 01 BA 00            mov rax, qword ptr [rip + 0xba01ca]
0035EB96  8B 04 C8                        mov eax, dword ptr [rax + rcx*8]
0035EB99  85 C0                           test eax, eax
0035EB9B  0F 84 66 FF FF FF               je 0x14035eb07
0035EBA1  41 89 01                        mov dword ptr [r9], eax
0035EBA4  48 8B 05 B5 01 BA 00            mov rax, qword ptr [rip + 0xba01b5]
0035EBAB  48 8B 44 C8 48                  mov rax, qword ptr [rax + rcx*8 + 0x48]
0035EBB0  48 85 C0                        test rax, rax
0035EBB3  0F 84 31 FF FF FF               je 0x14035eaea
0035EBB9  49 89 41 48                     mov qword ptr [r9 + 0x48], rax
0035EBBD  E9 28 FF FF FF                  jmp 0x14035eaea
0035EBC2  8B D6                           mov edx, esi
0035EBC4  48 8D 44 24 5B                  lea rax, [rsp + 0x5b]
0035EBC9  83 E2 10                        and edx, 0x10
0035EBCC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0035EBD1  4C 8D 4C 24 3B                  lea r9, [rsp + 0x3b]
0035EBD6  48 8B CE                        mov rcx, rsi
0035EBD9  4C 8D 45 9C                     lea r8, [rbp - 0x64]
0035EBDD  E8 9E 54 82 00                  call 0x140b84080
0035EBE2  85 C0                           test eax, eax
0035EBE4  0F 88 C6 FE FF FF               js 0x14035eab0
0035EBEA  80 7C 24 3B 00                  cmp byte ptr [rsp + 0x3b], 0
0035EBEF  8B 55 9C                        mov edx, dword ptr [rbp - 0x64]
0035EBF2  74 06                           je 0x14035ebfa
0035EBF4  83 CA 08                        or edx, 8
0035EBF7  89 55 9C                        mov dword ptr [rbp - 0x64], edx
0035EBFA  B9 22 0E 00 00                  mov ecx, 0xe22
0035EBFF  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0035EC04  4D 8B CC                        mov r9, r12
0035EC07  44 8B C7                        mov r8d, edi
0035EC0A  E8 DD E2 F8 FF                  call 0x1402eceec
0035EC0F  E9 9C FE FF FF                  jmp 0x14035eab0
0035EC14  F0 FF 0D 05 01 BA 00            lock dec dword ptr [rip + 0xba0105]
0035EC1B  49 8B CC                        mov rcx, r12
0035EC1E  E8 8D 09 00 00                  call 0x14035f5b0
0035EC23  49 8B DC                        mov rbx, r12
0035EC26  48 8B F0                        mov rsi, rax
0035EC29  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
0035EC30  80 3D 31 00 C7 00 00            cmp byte ptr [rip + 0xc70031], 0
0035EC37  0F 85 92 00 00 00               jne 0x14035eccf
0035EC3D  8B 53 04                        mov edx, dword ptr [rbx + 4]
0035EC40  41 8B C4                        mov eax, r12d
0035EC43  25 FF 0F 00 00                  and eax, 0xfff
0035EC48  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0035EC4D  B9 00 10 00 00                  mov ecx, 0x1000
0035EC52  41 B9 80 00 00 00               mov r9d, 0x80
0035EC58  2B C8                           sub ecx, eax
0035EC5A  44 8B F1                        mov r14d, ecx
0035EC5D  44 8B C1                        mov r8d, ecx
0035EC60  49 8B CC                        mov rcx, r12
0035EC63  E8 88 08 00 00                  call 0x14035f4f0
0035EC68  44 0F 20 C1                     mov rcx, cr8
0035EC6C  48 0F BA E6 08                  bt rsi, 8
0035EC71  0F 93 C0                        setae al
0035EC74  FE C0                           inc al
0035EC76  3A C8                           cmp cl, al
0035EC78  76 1E                           jbe 0x14035ec98
0035EC7A  0F B6 D1                        movzx edx, cl
0035EC7D  4D 8B CC                        mov r9, r12
0035EC80  B9 C1 00 00 00                  mov ecx, 0xc1
0035EC85  48 C7 44 24 20 31 00 00 00      mov qword ptr [rsp + 0x20], 0x31
0035EC8E  44 8D 41 3F                     lea r8d, [rcx + 0x3f]
0035EC92  E8 C9 E9 19 00                  call 0x1404fd660
0035EC97  CC                              int3
0035EC98  0F B7 3B                        movzx edi, word ptr [rbx]
0035EC9B  81 E7 FF 1F 00 00               and edi, 0x1fff
0035ECA1  48 8D 47 0F                     lea rax, [rdi + 0xf]
0035ECA5  48 83 E0 F0                     and rax, 0xfffffffffffffff0
0035ECA9  49 3B C6                        cmp rax, r14
0035ECAC  0F 84 6F FD FF FF               je 0x14035ea21
0035ECB2  4D 8B CE                        mov r9, r14
0035ECB5  48 C7 44 24 20 21 00 00 00      mov qword ptr [rsp + 0x20], 0x21
0035ECBE  44 8B C7                        mov r8d, edi
0035ECC1  49 8B D4                        mov rdx, r12
0035ECC4  B9 C1 00 00 00                  mov ecx, 0xc1
0035ECC9  E8 92 E9 19 00                  call 0x1404fd660
0035ECCE  CC                              int3
0035ECCF  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
0035ECD9  48 3B D8                        cmp rbx, rax
0035ECDC  0F 83 F4 04 00 00               jae 0x14035f1d6
0035ECE2  BA 02 00 00 00                  mov edx, 2
0035ECE7  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0035ECEC  4C 8B CB                        mov r9, rbx
0035ECEF  B9 F1 01 00 00                  mov ecx, 0x1f1
0035ECF4  44 8D 42 FF                     lea r8d, [rdx - 1]
0035ECF8  E8 63 E9 19 00                  call 0x1404fd660
0035ECFD  CC                              int3
0035ECFE  BA 00 00 00 80                  mov edx, 0x80000000
0035ED03  41 B8 01 00 00 00               mov r8d, 1
0035ED09  48 8B CF                        mov rcx, rdi
0035ED0C  E8 CF CB FF FF                  call 0x14035b8e0
0035ED11  4D 8B CA                        mov r9, r10
0035ED14  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0035ED19  4D 8B C2                        mov r8, r10
0035ED1C  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
0035ED24  49 8B D2                        mov rdx, r10
0035ED27  48 8D 88 40 01 00 00            lea rcx, [rax + 0x140]
0035ED2E  E8 89 78 FC FF                  call 0x1403265bc
0035ED33  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
0035ED37  48 8B C8                        mov rcx, rax
0035ED3A  48 85 C0                        test rax, rax
0035ED3D  0F 84 F8 06 00 00               je 0x14035f43b
0035ED43  48 A1 20 03 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000320]
0035ED4D  48 83 C1 10                     add rcx, 0x10
0035ED51  0F B6 D8                        movzx ebx, al
0035ED54  41 B8 F0 0F 00 00               mov r8d, 0xff0
0035ED5A  8B D3                           mov edx, ebx
0035ED5C  83 CA 01                        or edx, 1
0035ED5F  E8 DC 7E 36 00                  call 0x1406c6c40
0035ED64  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0035ED68  4C 8D 46 F8                     lea r8, [rsi - 8]
0035ED6C  48 8B C7                        mov rax, rdi
0035ED6F  25 00 04 00 00                  and eax, 0x400
0035ED74  48 85 C0                        test rax, rax
0035ED77  4C 89 69 08                     mov qword ptr [rcx + 8], r13
0035ED7B  8B 95 80 01 00 00               mov edx, dword ptr [rbp + 0x180]
0035ED81  4C 0F 44 C6                     cmove r8, rsi
0035ED85  80 CB 01                        or bl, 1
0035ED88  44 89 01                        mov dword ptr [rcx], r8d
0035ED8B  88 59 02                        mov byte ptr [rcx + 2], bl
0035ED8E  89 51 04                        mov dword ptr [rcx + 4], edx
0035ED91  4C 89 45 E8                     mov qword ptr [rbp - 0x18], r8
0035ED95  48 85 C0                        test rax, rax
0035ED98  74 06                           je 0x14035eda0
0035ED9A  81 09 00 40 00 00               or dword ptr [rcx], 0x4000
0035EDA0  48 8B F9                        mov rdi, rcx
0035EDA3  49 2B F8                        sub rdi, r8
0035EDA6  48 81 C7 00 10 00 00            add rdi, 0x1000
0035EDAD  48 83 E7 F0                     and rdi, 0xfffffffffffffff0
0035EDB1  F6 45 B8 02                     test byte ptr [rbp - 0x48], 2
0035EDB5  75 18                           jne 0x14035edcf
0035EDB7  33 D2                           xor edx, edx
0035EDB9  48 8B CF                        mov rcx, rdi
0035EDBC  E8 7F 7E 36 00                  call 0x1406c6c40
0035EDC1  8B 95 80 01 00 00               mov edx, dword ptr [rbp + 0x180]
0035EDC7  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0035EDCB  4C 8B 45 E8                     mov r8, qword ptr [rbp - 0x18]
0035EDCF  E8 DC 07 00 00                  call 0x14035f5b0
0035EDD4  48 8B D8                        mov rbx, rax
0035EDD7  4D 8D 48 0F                     lea r9, [r8 + 0xf]
0035EDDB  33 C0                           xor eax, eax
0035EDDD  49 83 E1 F0                     and r9, 0xfffffffffffffff0
0035EDE1  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
0035EDE8  0F 57 C0                        xorps xmm0, xmm0
0035EDEB  89 45 90                        mov dword ptr [rbp - 0x70], eax
0035EDEE  88 44 24 38                     mov byte ptr [rsp + 0x38], al
0035EDF2  88 44 24 58                     mov byte ptr [rsp + 0x58], al
0035EDF6  8B 05 50 63 C6 00               mov eax, dword ptr [rip + 0xc66350]
0035EDFC  4C 89 4C 24 60                  mov qword ptr [rsp + 0x60], r9
0035EE01  0F 11 85 C0 00 00 00            movups xmmword ptr [rbp + 0xc0], xmm0
0035EE08  3B D0                           cmp edx, eax
0035EE0A  75 01                           jne 0x14035ee0d
0035EE0C  CC                              int3
0035EE0D  8B 05 F1 7C C6 00               mov eax, dword ptr [rip + 0xc67cf1]
0035EE13  A8 41                           test al, 0x41
0035EE15  0F 85 23 02 00 00               jne 0x14035f03e
0035EE1B  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0035EE23  4C 8D 1D D6 11 CA FF            lea r11, [rip - 0x35ee2a]
0035EE2A  4C 8B 05 27 FF B9 00            mov r8, qword ptr [rip + 0xb9ff27]
0035EE31  48 83 E3 FB                     and rbx, 0xfffffffffffffffb
0035EE35  4C 89 45 B0                     mov qword ptr [rbp - 0x50], r8
0035EE39  4D 8B 9C C3 20 AD EF 00         mov r11, qword ptr [r11 + rax*8 + 0xefad20]
0035EE41  48 8B 05 08 FF B9 00            mov rax, qword ptr [rip + 0xb9ff08]
0035EE48  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0035EE4C  8B C2                           mov eax, edx
0035EE4E  48 69 C8 5F 9E 00 00            imul rcx, rax, 0x9e5f
0035EE55  4C 89 9D 78 01 00 00            mov qword ptr [rbp + 0x178], r11
0035EE5C  4C 8B D1                        mov r10, rcx
0035EE5F  49 C1 EA 20                     shr r10, 0x20
0035EE63  44 33 D1                        xor r10d, ecx
0035EE66  45 23 D0                        and r10d, r8d
0035EE69  4C 89 55 A8                     mov qword ptr [rbp - 0x58], r10
0035EE6D  44 89 95 70 01 00 00            mov dword ptr [rbp + 0x170], r10d
0035EE74  45 8B CA                        mov r9d, r10d
0035EE77  4F 8D 04 89                     lea r8, [r9 + r9*4]
0035EE7B  49 C1 E0 04                     shl r8, 4
0035EE7F  43 8B 04 18                     mov eax, dword ptr [r8 + r11]
0035EE83  4B 8D 0C 18                     lea rcx, [r8 + r11]
0035EE87  4C 89 45 B8                     mov qword ptr [rbp - 0x48], r8
0035EE8B  3B C2                           cmp eax, edx
0035EE8D  0F 85 88 00 00 00               jne 0x14035ef1b
0035EE93  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
0035EE98  4C 8B C1                        mov r8, rcx
0035EE9B  48 C1 EB 08                     shr rbx, 8
0035EE9F  F7 D3                           not ebx
0035EEA1  83 E3 01                        and ebx, 1
0035EEA4  8B CB                           mov ecx, ebx
0035EEA6  E8 65 C9 FF FF                  call 0x14035b810
0035EEAB  8B D8                           mov ebx, eax
0035EEAD  4C 8B 4D E8                     mov r9, qword ptr [rbp - 0x18]
0035EEB1  48 8B CF                        mov rcx, rdi
0035EEB4  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
0035EEBB  4C 8B C7                        mov r8, rdi
0035EEBE  BA 00 10 00 00                  mov edx, 0x1000
0035EEC3  E8 18 F5 F8 FF                  call 0x1402ee3e0
0035EEC8  85 DB                           test ebx, ebx
0035EECA  74 2C                           je 0x14035eef8
0035EECC  8B 9D 80 01 00 00               mov ebx, dword ptr [rbp + 0x180]
0035EED2  48 85 FF                        test rdi, rdi
0035EED5  0F 84 5B 01 00 00               je 0x14035f036
0035EEDB  F0 FF 05 3E FE B9 00            lock inc dword ptr [rip + 0xb9fe3e]
0035EEE2  44 8B 7C 24 6C                  mov r15d, dword ptr [rsp + 0x6c]
0035EEE7  4C 8B E7                        mov r12, rdi
0035EEEA  48 89 BD 78 01 00 00            mov qword ptr [rbp + 0x178], rdi
0035EEF1  33 FF                           xor edi, edi
0035EEF3  E9 DA CC FF FF                  jmp 0x14035bbd2
0035EEF8  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0035EEFD  48 8B D7                        mov rdx, rdi
0035EF00  E8 FB F6 F8 FF                  call 0x1402ee600
0035EF05  8B 9D 80 01 00 00               mov ebx, dword ptr [rbp + 0x180]
0035EF0B  45 33 C9                        xor r9d, r9d
0035EF0E  41 8B F9                        mov edi, r9d
0035EF11  4C 8B 5C 24 78                  mov r11, qword ptr [rsp + 0x78]
0035EF16  E9 DF CB FF FF                  jmp 0x14035bafa
0035EF1B  85 C0                           test eax, eax
0035EF1D  74 4F                           je 0x14035ef6e
0035EF1F  41 8D 42 01                     lea eax, [r10 + 1]
0035EF23  23 45 B0                        and eax, dword ptr [rbp - 0x50]
0035EF26  44 8B D0                        mov r10d, eax
0035EF29  4C 89 55 A8                     mov qword ptr [rbp - 0x58], r10
0035EF2D  3B 85 70 01 00 00               cmp eax, dword ptr [rbp + 0x170]
0035EF33  0F 85 3B FF FF FF               jne 0x14035ee74
0035EF39  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
0035EF3E  4C 8B C3                        mov r8, rbx
0035EF41  8B 9D 80 01 00 00               mov ebx, dword ptr [rbp + 0x180]
0035EF47  8B CB                           mov ecx, ebx
0035EF49  E8 72 DD F8 FF                  call 0x1402eccc0
0035EF4E  4C 8B 4D E8                     mov r9, qword ptr [rbp - 0x18]
0035EF52  48 8B CF                        mov rcx, rdi
0035EF55  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
0035EF5C  4C 8B C7                        mov r8, rdi
0035EF5F  BA 00 10 00 00                  mov edx, 0x1000
0035EF64  E8 77 F4 F8 FF                  call 0x1402ee3e0
0035EF69  E9 64 FF FF FF                  jmp 0x14035eed2
0035EF6E  48 8B 05 EB FD B9 00            mov rax, qword ptr [rip + 0xb9fdeb]
0035EF75  45 8B 1C 00                     mov r11d, dword ptr [r8 + rax]
0035EF79  45 85 DB                        test r11d, r11d
0035EF7C  74 28                           je 0x14035efa6
0035EF7E  44 89 19                        mov dword ptr [rcx], r11d
0035EF81  48 8B 05 D8 FD B9 00            mov rax, qword ptr [rip + 0xb9fdd8]
0035EF88  4C 8B 9D 78 01 00 00            mov r11, qword ptr [rbp + 0x178]
0035EF8F  4D 8B 4C 00 48                  mov r9, qword ptr [r8 + rax + 0x48]
0035EF94  4D 85 C9                        test r9, r9
0035EF97  0F 84 D7 FE FF FF               je 0x14035ee74
0035EF9D  4C 89 49 48                     mov qword ptr [rcx + 0x48], r9
0035EFA1  E9 CE FE FF FF                  jmp 0x14035ee74
0035EFA6  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
0035EFAA  48 FF C8                        dec rax
0035EFAD  4C 3B C8                        cmp r9, rax
0035EFB0  0F 84 E6 00 00 00               je 0x14035f09c
0035EFB6  48 8D 95 C0 00 00 00            lea rdx, [rbp + 0xc0]
0035EFBD  48 8D 0D 3C BD B9 00            lea rcx, [rip + 0xb9bd3c]
0035EFC4  E8 D7 67 F1 FF                  call 0x1402757a0
0035EFC9  48 8B 05 90 FD B9 00            mov rax, qword ptr [rip + 0xb9fd90]
0035EFD0  48 03 45 B8                     add rax, qword ptr [rbp - 0x48]
0035EFD4  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0035EFD8  44 39 28                        cmp dword ptr [rax], r13d
0035EFDB  75 37                           jne 0x14035f014
0035EFDD  8B 8D 80 01 00 00               mov ecx, dword ptr [rbp + 0x180]
0035EFE3  E8 08 DC F8 FF                  call 0x1402ecbf0
0035EFE8  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
0035EFEC  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
0035EFF0  4C 8B 85 78 01 00 00            mov r8, qword ptr [rbp + 0x178]
0035EFF7  48 89 41 48                     mov qword ptr [rcx + 0x48], rax
0035EFFB  8B 8D 80 01 00 00               mov ecx, dword ptr [rbp + 0x180]
0035F001  4A 89 44 02 48                  mov qword ptr [rdx + r8 + 0x48], rax
0035F006  48 8B 05 53 FD B9 00            mov rax, qword ptr [rip + 0xb9fd53]
0035F00D  89 0C 02                        mov dword ptr [rdx + rax], ecx
0035F010  42 89 0C 02                     mov dword ptr [rdx + r8], ecx
0035F014  48 8D 8D C0 00 00 00            lea rcx, [rbp + 0xc0]
0035F01B  E8 C0 3C FE FF                  call 0x140342ce0
0035F020  8B 95 80 01 00 00               mov edx, dword ptr [rbp + 0x180]
0035F026  4C 8B 55 A8                     mov r10, qword ptr [rbp - 0x58]
0035F02A  4C 8B 9D 78 01 00 00            mov r11, qword ptr [rbp + 0x178]
0035F031  E9 3E FE FF FF                  jmp 0x14035ee74
0035F036  45 33 C9                        xor r9d, r9d
0035F039  E9 D3 FE FF FF                  jmp 0x14035ef11
0035F03E  8B D3                           mov edx, ebx
0035F040  48 8D 44 24 58                  lea rax, [rsp + 0x58]
0035F045  83 E2 10                        and edx, 0x10
0035F048  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0035F04D  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0035F052  48 8B CB                        mov rcx, rbx
0035F055  4C 8D 45 90                     lea r8, [rbp - 0x70]
0035F059  E8 22 50 82 00                  call 0x140b84080
0035F05E  85 C0                           test eax, eax
0035F060  78 2F                           js 0x14035f091
0035F062  8B 55 90                        mov edx, dword ptr [rbp - 0x70]
0035F065  44 38 6C 24 38                  cmp byte ptr [rsp + 0x38], r13b
0035F06A  74 06                           je 0x14035f072
0035F06C  83 CA 08                        or edx, 8
0035F06F  89 55 90                        mov dword ptr [rbp - 0x70], edx
0035F072  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0035F077  B9 20 0E 00 00                  mov ecx, 0xe20
0035F07C  4C 8B 4D 28                     mov r9, qword ptr [rbp + 0x28]
0035F080  44 8B 85 80 01 00 00            mov r8d, dword ptr [rbp + 0x180]
0035F087  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0035F08C  E8 5B DE F8 FF                  call 0x1402eceec
0035F091  8B 95 80 01 00 00               mov edx, dword ptr [rbp + 0x180]
0035F097  E9 7F FD FF FF                  jmp 0x14035ee1b
0035F09C  4C 8B 9D 78 01 00 00            mov r11, qword ptr [rbp + 0x178]
0035F0A3  E9 77 FE FF FF                  jmp 0x14035ef1f
0035F0A8  3C 04                           cmp al, 4
0035F0AA  0F 84 FF DE FF FF               je 0x14035cfaf
0035F0B0  41 BE 00 01 00 00               mov r14d, 0x100
0035F0B6  E9 FA DE FF FF                  jmp 0x14035cfb5
0035F0BB  3C 04                           cmp al, 4
0035F0BD  0F 84 A4 DD FF FF               je 0x14035ce67
0035F0C3  41 BE 00 01 00 00               mov r14d, 0x100
0035F0C9  E9 9F DD FF FF                  jmp 0x14035ce6d
0035F0CE  44 2B C1                        sub r8d, ecx
0035F0D1  41 D1 E8                        shr r8d, 1
0035F0D4  0F 84 52 F5 FF FF               je 0x14035e62c
0035F0DA  41 FF C0                        inc r8d
0035F0DD  48 81 FA 00 00 02 00            cmp rdx, 0x20000
0035F0E4  0F 87 42 F5 FF FF               ja 0x14035e62c
0035F0EA  48 8D 45 50                     lea rax, [rbp + 0x50]
0035F0EE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0035F0F3  49 8D 8F C0 02 00 00            lea rcx, [r15 + 0x2c0]
0035F0FA  48 8D 45 F8                     lea rax, [rbp - 8]
0035F0FE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0035F103  E8 AC C5 F8 FF                  call 0x1402eb6b4
0035F108  85 C0                           test eax, eax
0035F10A  74 37                           je 0x14035f143
0035F10C  48 8B 75 F8                     mov rsi, qword ptr [rbp - 8]
0035F110  48 8B 16                        mov rdx, qword ptr [rsi]
0035F113  48 89 55 F8                     mov qword ptr [rbp - 8], rdx
0035F117  83 C0 FF                        add eax, -1
0035F11A  0F 84 94 F4 FF FF               je 0x14035e5b4
0035F120  8B 8D 70 01 00 00               mov ecx, dword ptr [rbp + 0x170]
0035F126  44 8B C8                        mov r9d, eax
0035F129  4C 8B 45 50                     mov r8, qword ptr [rbp + 0x50]
0035F12D  48 FF C1                        inc rcx
0035F130  48 C1 E1 06                     shl rcx, 6
0035F134  48 03 4C 24 50                  add rcx, qword ptr [rsp + 0x50]
0035F139  E8 E2 B4 35 00                  call 0x1406ba620
0035F13E  E9 71 F4 FF FF                  jmp 0x14035e5b4
0035F143  45 33 C9                        xor r9d, r9d
0035F146  E9 E1 F4 FF FF                  jmp 0x14035e62c
0035F14B  41 F6 C6 07                     test r14b, 7
0035F14F  74 21                           je 0x14035f172
0035F151  B8 02 00 00 00                  mov eax, 2
0035F156  48 C7 44 24 20 08 00 00 00      mov qword ptr [rsp + 0x20], 8
0035F15F  44 8B C0                        mov r8d, eax
0035F162  8B D0                           mov edx, eax
0035F164  4D 8B CE                        mov r9, r14
0035F167  B9 F1 01 00 00                  mov ecx, 0x1f1
0035F16C  E8 EF E4 19 00                  call 0x1404fd660
0035F171  CC                              int3
0035F172  4B 8D 04 37                     lea rax, [r15 + r14]
0035F176  49 3B C6                        cmp rax, r14
0035F179  73 1C                           jae 0x14035f197
0035F17B  BA 02 00 00 00                  mov edx, 2
0035F180  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0035F185  4D 8B CE                        mov r9, r14
0035F188  B9 F1 01 00 00                  mov ecx, 0x1f1
0035F18D  44 8D 42 01                     lea r8d, [rdx + 1]
0035F191  E8 CA E4 19 00                  call 0x1404fd660
0035F196  CC                              int3
0035F197  48 BB 00 00 00 00 00 80 00 00   movabs rbx, 0x800000000000
0035F1A1  49 8B FF                        mov rdi, r15
0035F1A4  49 03 DE                        add rbx, r14
0035F1A7  48 C1 EF 03                     shr rdi, 3
0035F1AB  48 C1 EB 03                     shr rbx, 3
0035F1AF  48 03 1D 22 7D C6 00            add rbx, qword ptr [rip + 0xc67d22]
0035F1B6  48 85 FF                        test rdi, rdi
0035F1B9  0F 85 E9 02 00 00               jne 0x14035f4a8
0035F1BF  41 F6 C7 07                     test r15b, 7
0035F1C3  0F 84 ED D8 FF FF               je 0x14035cab6
0035F1C9  41 0F B6 C7                     movzx eax, r15b
0035F1CD  24 07                           and al, 7
0035F1CF  88 03                           mov byte ptr [rbx], al
0035F1D1  E9 E0 D8 FF FF                  jmp 0x14035cab6
0035F1D6  48 8D 83 00 10 00 00            lea rax, [rbx + 0x1000]
0035F1DD  48 3B C3                        cmp rax, rbx
0035F1E0  73 20                           jae 0x14035f202
0035F1E2  BA 02 00 00 00                  mov edx, 2
0035F1E7  48 C7 44 24 20 00 10 00 00      mov qword ptr [rsp + 0x20], 0x1000
0035F1F0  4C 8B CB                        mov r9, rbx
0035F1F3  B9 F1 01 00 00                  mov ecx, 0x1f1
0035F1F8  44 8D 42 01                     lea r8d, [rdx + 1]
0035F1FC  E8 5F E4 19 00                  call 0x1404fd660
0035F201  CC                              int3
0035F202  48 B9 00 00 00 00 00 80 00 00   movabs rcx, 0x800000000000
0035F20C  33 D2                           xor edx, edx
0035F20E  48 03 CB                        add rcx, rbx
0035F211  41 B8 00 02 00 00               mov r8d, 0x200
0035F217  48 C1 E9 03                     shr rcx, 3
0035F21B  48 03 0D B6 7C C6 00            add rcx, qword ptr [rip + 0xc67cb6]
0035F222  E8 19 7A 36 00                  call 0x1406c6c40
0035F227  E9 11 FA FF FF                  jmp 0x14035ec3d
0035F22C  48 8D 46 FF                     lea rax, [rsi - 1]
0035F230  4D 8B F5                        mov r14, r13
0035F233  49 8D 5D FF                     lea rbx, [r13 - 1]
0035F237  49 C1 EE 03                     shr r14, 3
0035F23B  83 E3 07                        and ebx, 7
0035F23E  83 E0 07                        and eax, 7
0035F241  48 2B D8                        sub rbx, rax
0035F244  49 2B DD                        sub rbx, r13
0035F247  48 03 DE                        add rbx, rsi
0035F24A  48 BE 00 00 00 00 00 80 00 00   movabs rsi, 0x800000000000
0035F254  49 03 F1                        add rsi, r9
0035F257  48 C1 EE 03                     shr rsi, 3
0035F25B  48 03 35 76 7C C6 00            add rsi, qword ptr [rip + 0xc67c76]
0035F262  4D 85 F6                        test r14, r14
0035F265  0F 85 9A 01 00 00               jne 0x14035f405
0035F26B  41 F6 C5 07                     test r13b, 7
0035F26F  74 0A                           je 0x14035f27b
0035F271  41 80 E5 07                     and r13b, 7
0035F275  44 88 2E                        mov byte ptr [rsi], r13b
0035F278  48 FF C6                        inc rsi
0035F27B  48 C1 EB 03                     shr rbx, 3
0035F27F  48 85 DB                        test rbx, rbx
0035F282  0F 84 45 C9 FF FF               je 0x14035bbcd
0035F288  4C 8B C3                        mov r8, rbx
0035F28B  B2 86                           mov dl, 0x86
0035F28D  48 8B CE                        mov rcx, rsi
0035F290  E8 AB 79 36 00                  call 0x1406c6c40
0035F295  E9 33 C9 FF FF                  jmp 0x14035bbcd
0035F29A  48 3B CB                        cmp rcx, rbx
0035F29D  73 1C                           jae 0x14035f2bb
0035F29F  BA 02 00 00 00                  mov edx, 2
0035F2A4  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
0035F2A9  4C 8B CB                        mov r9, rbx
0035F2AC  B9 F1 01 00 00                  mov ecx, 0x1f1
0035F2B1  44 8D 42 01                     lea r8d, [rdx + 1]
0035F2B5  E8 A6 E3 19 00                  call 0x1404fd660
0035F2BA  CC                              int3
0035F2BB  49 8D 40 FF                     lea rax, [r8 - 1]
0035F2BF  48 B9 00 00 00 00 00 80 00 00   movabs rcx, 0x800000000000
0035F2C9  48 03 CB                        add rcx, rbx
0035F2CC  83 E0 07                        and eax, 7
0035F2CF  4C 2B C0                        sub r8, rax
0035F2D2  48 C1 E9 03                     shr rcx, 3
0035F2D6  48 03 0D FB 7B C6 00            add rcx, qword ptr [rip + 0xc67bfb]
0035F2DD  49 83 C0 07                     add r8, 7
0035F2E1  49 C1 E8 03                     shr r8, 3
0035F2E5  4D 85 C0                        test r8, r8
0035F2E8  0F 84 10 EF FF FF               je 0x14035e1fe
0035F2EE  B2 8D                           mov dl, 0x8d
0035F2F0  E8 4B 79 36 00                  call 0x1406c6c40
0035F2F5  0F B6 15 6C F9 C6 00            movzx edx, byte ptr [rip + 0xc6f96c]
0035F2FC  45 33 D2                        xor r10d, r10d
0035F2FF  45 8D 5A 01                     lea r11d, [r10 + 1]
0035F303  E9 F6 EE FF FF                  jmp 0x14035e1fe
0035F308  4A 8D 04 0E                     lea rax, [rsi + r9]
0035F30C  49 3B C1                        cmp rax, r9
0035F30F  0F 83 17 FF FF FF               jae 0x14035f22c
0035F315  BA 02 00 00 00                  mov edx, 2
0035F31A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0035F31F  B9 F1 01 00 00                  mov ecx, 0x1f1
0035F324  44 8D 42 01                     lea r8d, [rdx + 1]
0035F328  E8 33 E3 19 00                  call 0x1404fd660
0035F32D  CC                              int3
0035F32E  F6 C3 07                        test bl, 7
0035F331  0F 84 63 FF FF FF               je 0x14035f29a
0035F337  B8 02 00 00 00                  mov eax, 2
0035F33C  48 C7 44 24 20 08 00 00 00      mov qword ptr [rsp + 0x20], 8
0035F345  44 8B C0                        mov r8d, eax
0035F348  8B D0                           mov edx, eax
0035F34A  4C 8B CB                        mov r9, rbx
0035F34D  B9 F1 01 00 00                  mov ecx, 0x1f1
0035F352  E8 09 E3 19 00                  call 0x1404fd660
0035F357  CC                              int3
0035F358  4C 3B EE                        cmp r13, rsi
0035F35B  76 AB                           jbe 0x14035f308
0035F35D  BA 02 00 00 00                  mov edx, 2
0035F362  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0035F367  4D 8B CD                        mov r9, r13
0035F36A  B9 F1 01 00 00                  mov ecx, 0x1f1
0035F36F  44 8D 42 01                     lea r8d, [rdx + 1]
0035F373  E8 E8 E2 19 00                  call 0x1404fd660
0035F378  CC                              int3
0035F379  41 F6 C4 07                     test r12b, 7
0035F37D  0F 84 07 E3 FF FF               je 0x14035d68a
0035F383  B8 02 00 00 00                  mov eax, 2
0035F388  48 C7 44 24 20 08 00 00 00      mov qword ptr [rsp + 0x20], 8
0035F391  44 8B C0                        mov r8d, eax
0035F394  8B D0                           mov edx, eax
0035F396  4D 8B CC                        mov r9, r12
0035F399  B9 F1 01 00 00                  mov ecx, 0x1f1
0035F39E  E8 BD E2 19 00                  call 0x1404fd660
0035F3A3  CC                              int3
0035F3A4  4A 8D 04 09                     lea rax, [rcx + r9]
0035F3A8  49 3B C1                        cmp rax, r9
0035F3AB  73 19                           jae 0x14035f3c6
0035F3AD  BA 02 00 00 00                  mov edx, 2
0035F3B2  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0035F3B7  B9 F1 01 00 00                  mov ecx, 0x1f1
0035F3BC  44 8D 42 01                     lea r8d, [rdx + 1]
0035F3C0  E8 9B E2 19 00                  call 0x1404fd660
0035F3C5  CC                              int3
0035F3C6  48 8D 41 FF                     lea rax, [rcx - 1]
0035F3CA  48 BE 00 00 00 00 00 80 00 00   movabs rsi, 0x800000000000
0035F3D4  49 03 F1                        add rsi, r9
0035F3D7  49 8D 5D FF                     lea rbx, [r13 - 1]
0035F3DB  83 E3 07                        and ebx, 7
0035F3DE  48 C1 EE 03                     shr rsi, 3
0035F3E2  48 03 35 EF 7A C6 00            add rsi, qword ptr [rip + 0xc67aef]
0035F3E9  83 E0 07                        and eax, 7
0035F3EC  48 2B D8                        sub rbx, rax
0035F3EF  4D 8B F5                        mov r14, r13
0035F3F2  49 2B DD                        sub rbx, r13
0035F3F5  49 C1 EE 03                     shr r14, 3
0035F3F9  48 03 D9                        add rbx, rcx
0035F3FC  4D 85 F6                        test r14, r14
0035F3FF  0F 84 66 FE FF FF               je 0x14035f26b
0035F405  4D 8B C6                        mov r8, r14
0035F408  33 D2                           xor edx, edx
0035F40A  48 8B CE                        mov rcx, rsi
0035F40D  E8 2E 78 36 00                  call 0x1406c6c40
0035F412  49 03 F6                        add rsi, r14
0035F415  E9 51 FE FF FF                  jmp 0x14035f26b
0035F41A  4C 3B E9                        cmp r13, rcx
0035F41D  76 85                           jbe 0x14035f3a4
0035F41F  BA 02 00 00 00                  mov edx, 2
0035F424  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0035F429  4D 8B CD                        mov r9, r13
0035F42C  B9 F1 01 00 00                  mov ecx, 0x1f1
0035F431  44 8D 42 01                     lea r8d, [rdx + 1]
0035F435  E8 26 E2 19 00                  call 0x1404fd660
0035F43A  CC                              int3
0035F43B  45 33 C9                        xor r9d, r9d
0035F43E  41 8B F9                        mov edi, r9d
0035F441  E9 CB FA FF FF                  jmp 0x14035ef11
0035F446  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0035F44B  49 8B CC                        mov rcx, r12
0035F44E  0F B7 50 02                     movzx edx, word ptr [rax + 2]
0035F452  48 C1 E2 06                     shl rdx, 6
0035F456  49 03 D4                        add rdx, r12
0035F459  E8 AA 0B 17 00                  call 0x1404d0008
0035F45E  E9 44 D3 FF FF                  jmp 0x14035c7a7
0035F463  45 33 FF                        xor r15d, r15d
0035F466  E9 FA E1 FF FF                  jmp 0x14035d665
0035F46B  48 8B 42 38                     mov rax, qword ptr [rdx + 0x38]
0035F46F  48 A9 FF 0F 00 00               test rax, 0xfff
0035F475  0F 85 36 3A 38 00               jne 0x1406e2eb1
0035F47B  49 8B CB                        mov rcx, r11
0035F47E  E9 5F E4 FF FF                  jmp 0x14035d8e2
0035F483  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
0035F488  E9 BA E4 FF FF                  jmp 0x14035d947
0035F48D  45 33 D2                        xor r10d, r10d
0035F490  45 8B FA                        mov r15d, r10d
0035F493  E9 B2 EC FF FF                  jmp 0x14035e14a
0035F498  49 FF C0                        inc r8
0035F49B  E9 96 F5 FF FF                  jmp 0x14035ea36
0035F4A0  49 FF C0                        inc r8
0035F4A3  E9 A9 F5 FF FF                  jmp 0x14035ea51
0035F4A8  4C 8B C7                        mov r8, rdi
0035F4AB  33 D2                           xor edx, edx
0035F4AD  48 8B CB                        mov rcx, rbx
0035F4B0  E8 8B 77 36 00                  call 0x1406c6c40
0035F4B5  48 03 DF                        add rbx, rdi
0035F4B8  E9 02 FD FF FF                  jmp 0x14035f1bf
0035F4BD  48 8B 9C 24 88 02 00 00         mov rbx, qword ptr [rsp + 0x288]
0035F4C5  49 8B C5                        mov rax, r13
0035F4C8  48 81 C4 30 02 00 00            add rsp, 0x230
0035F4CF  41 5F                           pop r15
0035F4D1  41 5E                           pop r14
0035F4D3  41 5D                           pop r13
0035F4D5  41 5C                           pop r12
0035F4D7  5F                              pop rdi
0035F4D8  5E                              pop rsi
0035F4D9  5D                              pop rbp
0035F4DA  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExAllocateHeapPool(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int8 v_stack_m10E;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m11C;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m144;
    unsigned int v_stack_m148;
    unsigned int v_stack_m14C;
    unsigned int v_stack_m150;
    unsigned int v_stack_m154;
    unsigned int v_stack_m158;
    unsigned __int8 v_stack_m15A;
    unsigned __int16 v_stack_m15C;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m190;
    unsigned int v_stack_m194;
    unsigned __int16 v_stack_m196;
    unsigned int v_stack_m198;
    unsigned __int16 v_stack_m19E;
    unsigned __int64 v_stack_m1A0;
    unsigned __int8 v_stack_m1A4;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int8 v_stack_m1B4;
    unsigned __int64 v_stack_m1B8;
    unsigned __int8 v_stack_m1BA;
    unsigned __int16 v_stack_m1BC;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1C4;
    unsigned __int16 v_stack_m1C6;
    unsigned int v_stack_m1C8;
    unsigned int v_stack_m1CC;
    unsigned int v_stack_m1D0;
    unsigned int v_stack_m1D4;
    unsigned int v_stack_m1D8;
    unsigned __int16 v_stack_m1DE;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned int v_stack_m1FC;
    unsigned int v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int8 v_stack_m20C;
    unsigned __int8 v_stack_m20D;
    unsigned __int8 v_stack_m20E;
    unsigned __int8 v_stack_m20F;
    unsigned __int8 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int8 v_stack_m21A;
    unsigned __int16 v_stack_m21E;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int8 v_stack_m22C;
    unsigned __int8 v_stack_m22D;
    unsigned __int8 v_stack_m22E;
    unsigned __int8 v_stack_m22F;
    unsigned __int8 v_stack_m230;
    unsigned __int8 v_stack_m232;
    unsigned __int16 v_stack_m236;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p20 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (560);
    a4 = 0;
    v_stack_m1FC = 1;
    v_stack_m1F8 = 0;
    v_r12 = (unsigned int)((a1) & (2));
    v_r14 = 2;
    if (condition_is_not_equal) { v_r14 = 0; }
    result = (unsigned int)((a1) & (0x408ULL));
    v_r11 = (a1) & (-9);
    if (result != 0x408ULL) { v_r11 = a1; }
    v_stack_m1F0 = v_r11;
    a1 = (((v_r11) & (320)) == 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) {
        v_r11 = (v_r11) | (64);
        v_stack_m1F0 = v_r11;
    }
    if (a2 > 0xFE0ULL) goto loc_0035BAFA;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13021509))) != 0) goto loc_0035E812;
loc_0035BAEC:
    if (condition_is_below) goto loc_0035BF20;
    a4 = 0;
loc_0035BAFA:
    v_r11 = (unsigned int)((v_r11) & (0xFFFULL));
    v_stack_m1F0 = v_r11;
    v_r13 = 1;
    if (a2 != 0) { v_r13 = a2; }
    if (((unsigned int)((unsigned int)(a4))) != 0x80000000ULL) goto loc_0035C090;
loc_0035BB23:
loc_0035BB3B:
    v_r15 = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 192) + 138);
    if (((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 192) + 138))) >= (*(unsigned int *)(v_rip + 11600846))) {
        v_r15 = 0;
    }
    v_r15 = (v_r15) * ((unsigned int)((unsigned int)(v_r15)));
    v_r15 = (v_r15) + (v_rip + 11600872);
    if ((((unsigned __int8)(v_r11)) & (16)) != 0) goto loc_0035C087;
    if (condition_is_above_or_equal) goto loc_0035C064;
loc_0035BB75:
loc_0035BB79:
    v_stack_m220 = *(unsigned __int64 *)(v_r15 + 2 * 8);
    if (v_r13 <= 0xFE0ULL) goto loc_0035C179;
    v_rsi = (v_r13 + 15) & (-16);
    v_stack_m1F8 = v_rsi;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (0xFFFULL));
    if (((unsigned int)(result)) > 0xFC0ULL) goto loc_0035D86C;
    if (v_rsi >= 0x10000ULL) goto loc_0035D86C;
loc_0035BBB7:
    if (v_rsi >= v_r13) goto loc_0035C0F4;
    v_stack_p10 = 0;
loc_0035BBCD:
loc_0035BBD2:
    if (0 == 0) goto loc_0035C07F;
    if (0 == 0) goto loc_0035BBE9;
    goto loc_0035BC2A;
loc_0035BBE9:
    a2 = (0) - (*(unsigned __int64 *)(v_rip + 11586062));
    a2 = (a2) >> (20);
    a2 = (a2) + (a2);
    result = RtlCSparseBitmapBitmaskRead(v_rip + 11586077, a2, 1, a4);
    if (result == 0) goto loc_0035C074;
    result = (unsigned int)((result) - 1);
    if (((unsigned int)(result)) == 2) goto loc_0035C074;
    if (((unsigned int)(result)) == 1) goto loc_0035D9EB;
loc_0035BC2A:
    a2 = (*(unsigned __int64 *)(v_stack_m220 + 320)) & (0);
    result = (*(unsigned __int64 *)(a2 + 16)) ^ (*(unsigned __int64 *)(v_rip + 11323074));
    result = (result) ^ (a2);
    if (result != (v_stack_m220 + 320)) goto loc_0035BE67;
    a3 = (unsigned int)((0) - ((unsigned int)(a2)));
    a3 = (unsigned int)((a3) >> ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_stack_m220 + 320 + 8))))));
    a3 = (a3) << (5);
    a3 = (a3) + (a2);
    result = -(*(unsigned __int8 *)(a3 + 26));
    result = (result) << (5);
    a3 = (a3) + (result);
    v_rbx = (a3) - (a2);
    v_rbx = (v_rbx) >> (5);
    v_rbx = (v_rbx) << ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_stack_m220 + 320 + 8)))));
    v_rbx = (v_rbx) + (a2);
    result = (v_rbx == 0) ? 1 : 0;
    if (((unsigned __int8)(result + *(unsigned __int8 *)(a3 + 24) * 1)) != 11) goto loc_0035BF89;
    result = (v_rbx) >> (12);
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rbx + 40)));
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rip + 11322969)));
    result = (result) >> (16);
    result = (result) + (v_rbx);
    v_stack_mC8 = (unsigned int)((unsigned int)((unsigned int)(result)));
    a3 = (unsigned int)((0) - ((unsigned int)(result)));
    a2 = (*(unsigned __int16 *)(v_rbx + 44)) << (6);
    v_rsi = ((unsigned int)(*(unsigned int *)(a2 + *(unsigned __int64 *)(v_stack_m220 + 320 + 24) * 1 + 72))) * ((unsigned int)(a3));
    v_rsi = (v_rsi) >> (32);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) * ((unsigned int)((unsigned __int16)((unsigned int)((unsigned int)(result))))));
    a3 = (unsigned int)((a3) - ((unsigned int)(result)));
    v_stack_mCC = a3;
    if (condition_is_not_equal) goto loc_0035C07F;
    v_r13 = 0;
    v_r10 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m220 + 320 + 24) + 76))) >> (4);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m220 + 320 + 24) + 76))))) >> (13));
    v_r10 = (unsigned int)((v_r10) & (511));
    a2 = (unsigned int)((a2) & (0x3FFFFULL));
    a4 = (unsigned int)((1) << ((unsigned __int8)((unsigned __int16)((unsigned int)((unsigned int)(result))))));
    a1 = (unsigned int)(((unsigned __int16)((unsigned int)((unsigned int)(result)))) + (-2));
    v_stack_m14C = (unsigned int)(a1);
    a4 = (unsigned int)((a4) ^ ((unsigned int)(a2)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35760) + a1 * 8) + a4 * 8 + 8) + v_r10 * 8) == 0) goto loc_0035E8B3;
loc_0035BD4A:
    if (((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35760) + a1 * 8) + a4 * 8 + 8) + v_r10 * 8))) == (*(unsigned __int16 *)(v_rbx + 46))) goto loc_0035E84C;
loc_0035BD54:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) >> (6));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (63));
    if (condition_is_above_or_equal) goto loc_0035C0D2;
    v_rsi = (unsigned __int16)((v_rsi) + 1);
loc_0035BD76:
    v_stack_m160 = *(unsigned __int64 *)(v_rbx + 16);
    a1 = (*(unsigned __int64 *)(v_rbx + 16)) >> (48);
    v_stack_m220 = *(unsigned __int64 *)(v_rbx + 16);
    if (((unsigned __int8)(a1)) == 1) {
        v_stack_m21A = 2;
    }
    *(unsigned __int16 *)(0) = (unsigned __int16)(v_stack_m220);
    v_stack_m68 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m220 + 320 + 24) + 80);
    a3 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m220 + 320 + 24) + 80)) ^ (*(unsigned int *)(0)));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m220 + 320 + 24) + 80)) >> (32);
    a2 = (unsigned int)((a2) ^ (0));
    a3 = (unsigned int)((a3) ^ ((unsigned int)(a2)));
    v_stack_m220 = (unsigned __int16)(v_rsi);
    *(unsigned int *)(0 + 8) = a3;
    a2 = (*(unsigned __int16 *)(v_rbx + 44)) << (6);
    if (condition_is_not_equal) goto loc_0035BD76;
    if ((*(unsigned __int8 *)(a2 + *(unsigned __int64 *)(v_stack_m220 + 320 + 24) * 1 + 92)) == 0) goto loc_0035C4AC;
loc_0035BDE6:
    if (v_stack_m15A != 1) goto loc_0035BE87;
    a4 = (unsigned int)((v_stack_m15C) << (6));
    a4 = (a4) + (*(unsigned __int64 *)(v_stack_m220 + 320 + 24));
    a1 = (*(unsigned __int64 *)(v_rbx + 24)) ^ (*(unsigned __int64 *)(a4 + 8));
    a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (unsigned int)((*(unsigned __int64 *)(a4 + 8)) & (0xFFFULL));
    a1 = (a1) ^ (*(unsigned __int64 *)(v_rbx + 24));
    *(unsigned __int64 *)(v_rbx + 24) = a1;
    a1 = (v_rbx) | (a2);
    if (condition_is_equal) goto loc_0035BE87;
loc_0035BE34:
    a1 = (*(unsigned __int64 *)(v_rbx + 24)) ^ (*(unsigned __int64 *)(a4 + 8));
    a2 = (unsigned int)((*(unsigned __int64 *)(a4 + 8)) & (0xFFFULL));
    a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (a1) ^ (*(unsigned __int64 *)(v_rbx + 24));
    *(unsigned __int64 *)(v_rbx + 24) = a1;
    a1 = (v_rbx) | (a2);
    if ((*(unsigned __int64 *)(a4 + 8)) != (*(unsigned __int64 *)(a4 + 8))) goto loc_0035BE34;
    goto loc_0035BE87;
loc_0035BE67:
    v_r13 = 0;
loc_0035BE6A:
    a4 = 0;
    v_stack_m240 = 0;
    v_stack_m248 = 0;
    result = RtlpLogHeapFailure(a4 + 9, *(unsigned __int64 *)(v_rsi + 56), 0, a4);
loc_0035BE87:
loc_0035BE8E:
    if (1 != 0) goto loc_0035C7C0;
    v_stack_m110 = v_xmm0;
    v_stack_m110 = 257;
    v_stack_m110 = 3;
    v_stack_m110 = 3;
    v_stack_m10E = 1;
    if (0 == 0) goto loc_0035D567;
loc_0035BEBD:
    v_stack_m120 = 0x100000ULL;
    v_stack_m11C = 0x1000000ULL;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m168 + (int)(0) * 4 + 72))) - 1;
    result = ~(result);
    result = (result) & (0);
    v_r15 = (*(unsigned __int64 *)(result + 16)) ^ (*(unsigned __int64 *)(v_rip + 11322394));
    v_r15 = (v_r15) ^ (result);
    result = ((int)(0) + (int)(0) * 2) << (6);
    v_r15 = (v_r15) - (result);
    v_r15 = (v_r15) - (320);
loc_0035BEFB:
    v_stack_m1E0 = v_r15;
    if (v_r15 != 0) goto loc_0035C7D2;
    v_stack_m248 = 0;
    a3 = 0;
    a2 = 0;
    result = KeBugCheckEx(194, a2, a3, 0);
loc_0035BF20:
    v_stack_m1B0 = v_r11;
    a1 = (unsigned int)((v_r11) & (448));
    if (a1 != 256) goto loc_0035BF4A;
loc_0035BF39:
    if (a1 != 256) goto loc_0035BF62;
    goto loc_0035BF64;
loc_0035BF4A:
    if (a1 >= 256) goto loc_0035BF39;
    v_rdi = (v_r11) | (64);
    v_stack_m1B0 = v_rdi;
loc_0035BF62:
loc_0035BF64:
    if (((unsigned __int8)(v_cr8)) <= 2) goto loc_0035ECFE;
    v_stack_m248 = 48;
    result = KeBugCheckEx(193, (unsigned __int8)(v_cr8), (unsigned int)((unsigned int)(v_rdi)), v_rsi);
loc_0035BF89:
    a4 = (v_rsi) & ((unsigned int)((unsigned int)(v_rdi)));
    v_r13 = 0;
    result = ((unsigned int)((unsigned int)(v_rdi))) - (a4);
    v_stack_m194 = 0;
    result = (result) >> (5);
    result = (result) << ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbx + 24)))));
    result = (unsigned __int8)(((unsigned __int8)((unsigned __int8)(v_cr8))) & (3));
    if (((unsigned __int8)(result)) != 3) goto loc_0035BE6A;
    if (v_rdi == (result + a4 * 1)) goto loc_0035C0C2;
    if (((unsigned __int8)((unsigned __int8)(v_cr8))) != 15) goto loc_0035BE6A;
    if (v_rdi <= (result + a4 * 1)) goto loc_0035C0C2;
    result = RtlpHpVsContextFree(*(unsigned __int64 *)(v_rsi + 32), result + a4 * 1, v_rdi, v_stack_m194);
    if ((unsigned int)(result) == 0) goto loc_0035BE87;
    if (((unsigned int)((unsigned int)(v_stack_m194))) >= ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsi + 24) + 68)))) goto loc_0035BE8E;
    result = (unsigned int)(((unsigned int)(v_stack_m194) + 15) >> (4));
    v_r10 = (unsigned int)((*(unsigned __int8 *)(result + v_rip - 3522549 * 1 + 68480)) - 1);
loc_0035C01A:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 24) + v_r10 * 8 + 448)) >> (16);
    v_stack_m1E0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 24) + v_r10 * 8 + 448);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 24) + v_r10 * 8 + 448))) & (1)) == 0) goto loc_0035C057;
    if (((unsigned __int16)(result)) >= = 1) {
        result = (unsigned __int16)((result) - 1);
        v_stack_m1DE = (unsigned __int16)(result);
        a1 = v_stack_m1E0;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 24) + v_r10 * 8 + 448)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 24) + v_r10 * 8 + 448))) goto loc_0035C01A;
loc_0035C057:
    goto loc_0035BE8E;
loc_0035C064:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 24) + v_r10 * 8 + 448);
    if ((((unsigned __int8)(v_r11)) & (128)) != 0) { result = *(unsigned __int64 *)(v_rsi + 24) + v_r10 * 8; }
    goto loc_0035BB75;
loc_0035C074:
    result = RtlpHpLargeFree(0, v_rip - 3522549, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 24) + v_r10 * 8 + 448), *(unsigned __int64 *)(v_rsi + 24) + v_r10 * 8);
loc_0035C07F:
    v_r13 = 0;
    goto loc_0035BE87;
loc_0035C087:
    goto loc_0035BB79;
loc_0035C090:
    if (((unsigned int)(*(unsigned __int64 *)(v_r15 + 24))) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 13012841)))) goto loc_0035D849;
    v_stack_m248 = (unsigned int)((unsigned int)(v_rbx));
    result = KeBugCheckEx(194, 14, *(unsigned __int64 *)(v_r15 + 24), v_r11);
loc_0035C0C2:
    result = RtlpHpSegPageRangeShrink(v_rsi, *(unsigned __int64 *)(v_r15 + 24), *(unsigned __int64 *)(v_r15 + 24), v_r11);
    goto loc_0035BE87;
loc_0035C0D2:
    v_stack_m240 = 0;
    v_stack_m248 = v_rsi;
    result = RtlpLogHeapFailure(17, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m220 + 320 + 24)), v_rip - 3522549, v_rbx);
    goto loc_0035BE87;
loc_0035C0F4:
    if ((((unsigned int)(v_rsi)) & (0xFFFULL)) != 0) goto loc_0035C4E4;
    if (v_rsi > ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r15 + 24) + 528)))) goto loc_0035C4E4;
    a4 = (unsigned int)(~((unsigned int)((unsigned int)(v_r11))));
    a4 = (unsigned int)((a4) & (2));
    result = RtlpHpAllocateHeapBackend(*(unsigned __int64 *)(v_r15 + 24), v_rsi, v_rsi, a4);
loc_0035C128:
loc_0035C12B:
    if (result == 0) goto loc_0035D91E;
    v_rsi = 0;
    v_stack_m240 = 0;
    v_stack_m248 = 0;
    result = ExpAddTagForBigPages(result, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), v_stack_m1F8, v_stack_m1F0);
    if ((unsigned int)(result) != 0) goto loc_0035D418;
    v_stack_p10 = 0;
loc_0035C16F:
    goto loc_0035BBCD;
loc_0035C179:
    if ((((unsigned __int8)(v_r11)) & (8)) != 0) goto loc_0035D812;
loc_0035C187:
    v_rsi = (v_r13 + 16) + (15);
    v_rsi = (v_rsi) & (-16);
    v_stack_m228 = v_rsi;
    v_stack_m1F8 = v_rsi;
    if ((v_rsi - 513) <= 0xD7FULL) goto loc_0035E556;
loc_0035C1B3:
    a2 = v_stack_m1F8;
    if (v_rsi > 1) { a2 = v_rsi; }
    v_stack_m1A8 = a2;
    if (a2 >= (*(unsigned __int16 *)((unsigned int)(v_stack_m1FC) + 900))) goto loc_0035F483;
    result = (unsigned int)((a2 + 15) >> (4));
    result = (unsigned int)((*(unsigned __int8 *)(result + v_rip - 3522962 * 1 + 68480)) - 1);
    v_stack_p8 = (unsigned int)(result);
    v_r10 = ((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m1FC) + 832 + 76))) >> (4);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m1FC) + 832 + 76))))) >> (13));
    v_r10 = (unsigned int)((v_r10) & (511));
    a2 = (unsigned int)((a2) & (0x3FFFFULL));
    a4 = (unsigned int)((1) << ((unsigned __int8)(result)));
    a1 = (unsigned int)((result) + (-2));
    v_stack_m150 = (unsigned int)(a1);
    a4 = (unsigned int)((a4) ^ ((unsigned int)(a2)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35760) + a1 * 8) + a4 * 8 + 8) + v_r10 * 8) == 0) goto loc_0035E9CE;
loc_0035C24A:
    v_stack_m1B8 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35760) + a1 * 8) + a4 * 8 + 8) + v_r10 * 8);
    result = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p8)))) + ((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    a1 = (unsigned int)(((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35760) + a1 * 8) + a4 * 8 + 8) + v_r10 * 8))) << (6));
    a1 = (a1) + ((unsigned int)(v_stack_m1FC) + 832);
    v_stack_p8 = result;
    result = (result) + (a1);
    v_stack_p10 = a1;
    v_stack_m218 = result;
    if ((unsigned int)(*(unsigned __int16 *)(result)) == 0) goto loc_0035D92D;
loc_0035C286:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(result)))) << (6));
    a2 = ((unsigned int)(a3)) + ((unsigned int)(v_stack_m1FC) + 832);
    v_stack_m228 = v_rsi;
    v_stack_m218 = a2;
    if ((*(unsigned __int16 *)(a2 + 4)) != 0) goto loc_0035F46B;
    v_stack_m200 = 0;
    v_stack_m228 = v_rsi;
loc_0035C2BA:
    if (((*(unsigned __int64 *)(a2 + 56)) & (0xFFFULL)) == 0) goto loc_0035D8DB;
    if (((*(unsigned __int64 *)(a2 + 56)) & (0xFFFULL)) != 0) goto loc_0035D839;
    v_r11 = (*(unsigned __int64 *)(a2 + 56)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m228 = v_rsi;
    result = (v_r11) >> (12);
    v_stack_m238 = v_r11;
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_r11 + 40)));
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rip + 11321347)));
    v_stack_m1C8 = (unsigned int)(result);
    v_r10 = (unsigned int)((*(unsigned __int8 *)(v_r11 + 24)) - (8));
    v_stack_m1E8 = (unsigned int)((unsigned __int16)(result));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1896)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888));
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1896) + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888) * 1) >> (32);
    result = (a2) << (16);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888)) ^ (result);
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888) = a1;
    v_r10 = (v_r10) - 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1896) = a2;
    v_stack_m198 = (unsigned int)(*(unsigned __int8 *)(v_r11 + 50));
    v_stack_p8 = (unsigned __int8)(*(unsigned __int8 *)(v_r11 + 39));
    v_stack_p10 = (unsigned int)((unsigned __int8)(a3));
    v_stack_m1B8 = v_r11 + 64 + v_r10 * 8;
loc_0035C38C:
    a2 = ~(*(unsigned __int64 *)(v_r11 + 64 + *(unsigned __int8 *)(v_r11 + 36) * 8));
    if (a2 == 0) goto loc_0035DD48;
loc_0035C39B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11321223)))) & (4)) != 0) goto loc_0035DB97;
    if ((v_r11 + 64 + *(unsigned __int8 *)(v_r11 + 36) * 8) == (v_r11 + 64 + v_r10 * 8)) goto loc_0035E446;
    if (((unsigned int)((unsigned int)(v_stack_m198))) != 64) goto loc_0035E446;
    v_r10 = (unsigned int)((v_r11 + 64 + v_r10 * 8) + ((unsigned int)((unsigned __int8)(a3))));
    v_r10 = (unsigned int)((v_r10) & (63));
loc_0035C3CD:
    a4 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r10))));
loc_0035C3D9:
loc_0035C3E0:
    a1 = (*(unsigned __int64 *)(v_r11 + 64 + *(unsigned __int8 *)(v_r11 + 36) * 8)) | (a4);
    if (condition_is_not_equal) goto loc_0035C3E0;
    if (((*(unsigned __int64 *)(v_r11 + 64 + *(unsigned __int8 *)(v_r11 + 36) * 8)) & (a4)) != 0) goto loc_0035DB6A;
    a3 = (unsigned int)((v_r11 + 64 + *(unsigned __int8 *)(v_r11 + 36) * 8) - ((unsigned int)(v_r11 + 64)));
    v_stack_p10 = (unsigned int)(v_r10 + a3 * 8);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r10 + a3 * 8))) * ((unsigned int)((unsigned int)(v_stack_m1E8))));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r10 + a3 * 8))) >> (6));
    *(unsigned __int8 *)(v_r11 + 36) = (unsigned __int8)(result);
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_stack_m1C6)));
    if (v_stack_p8 <= 1) goto loc_0035DE15;
    result = RtlpHpLfhSubsegmentCommitBlock((unsigned int)(v_stack_m1FC) + 832, v_r11, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(v_stack_m1E8));
    if (sign_flag) goto loc_0035DC1D;
loc_0035C44F:
    v_rsi = (v_rsi) + (v_stack_m238);
    v_r11 = v_stack_m238;
    if (0 == 0) {
        a2 = (unsigned int)(v_stack_m228);
        a1 = v_rsi;
        a2 = (a2) + (15);
        a2 = (a2) & (-16);
        result = RtlHeapZero(a1, a2, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(v_stack_m1E8));
        v_r11 = v_stack_m238;
    }
    if (v_rsi == 0) goto loc_0035DC63;
    if (v_stack_m200 == 0) goto loc_0035D8F5;
    a2 = (*(unsigned __int16 *)(v_stack_m218 + 2)) << (6);
    a2 = (a2) + ((unsigned int)(v_stack_m1FC) + 832);
    result = RtlpHpLfhBucketUpdateAffinityMapping((unsigned int)(v_stack_m1FC) + 832, a2, (unsigned int)(v_stack_m1FC) + 832, (unsigned int)(v_stack_m1E8));
    goto loc_0035D8F5;
loc_0035C4AC:
    *(unsigned __int8 *)(a2 + v_stack_m1F0 * 1 + 92) = 1;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1F0) + 56))) >> (8);
    if (((unsigned __int8)(result)) != 1) goto loc_0035D40D;
loc_0035C4CE:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12182254))) != 0) goto loc_0035BDE6;
    result = RtlpHpEnvCompactionSchedule(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1F0) + 56), a2, (unsigned int)(v_stack_m1FC) + 832, (unsigned int)(v_stack_m1E8));
    goto loc_0035BDE6;
loc_0035C4E4:
    v_rdi = (unsigned int)(v_stack_m1FC) + 832;
    if (v_rsi > ((unsigned int)(v_stack_m1FC) + 832)) { v_rdi = v_rsi; }
    v_stack_m1C0 = v_rdi;
    if (v_rdi >= (*(unsigned __int16 *)((unsigned int)(v_stack_m1FC) + 900))) goto loc_0035D97F;
    a1 = (unsigned int)((v_rdi + 15) >> (4));
    v_r10 = ((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m1FC) + 832 + 76))) >> (4);
    v_r10 = (unsigned int)((v_r10) & (511));
    result = (unsigned int)((*(unsigned __int8 *)(a1 + v_rip - 3523862 * 1 + 68480)) - 1);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m1FC) + 832 + 76))))) >> (13));
    a2 = (unsigned int)((a2) & (0x3FFFFULL));
    v_stack_p8 = (unsigned int)(result);
    a4 = (unsigned int)((1) << ((unsigned __int8)(a1)));
    a1 = (unsigned int)((a1) + (-2));
    v_stack_m158 = (unsigned int)(a1);
    a4 = (unsigned int)((a4) ^ ((unsigned int)(a2)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35760) + a1 * 8) + a4 * 8 + 8) + v_r10 * 8) == 0) goto loc_0035E9E2;
loc_0035C57D:
    v_stack_m1A8 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35760) + a1 * 8) + a4 * 8 + 8) + v_r10 * 8);
    result = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p8)))) + ((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))));
    v_rbx = (unsigned int)(((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35760) + a1 * 8) + a4 * 8 + 8) + v_r10 * 8))) << (6));
    v_rbx = (v_rbx) + ((unsigned int)(v_stack_m1FC) + 832);
    v_stack_p8 = result;
    if ((unsigned int)(*(unsigned __int16 *)(result + v_rbx * 1)) == 0) goto loc_0035D96E;
loc_0035C5AB:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(result + v_rbx * 1)))) << (6));
    a2 = ((unsigned int)(a3)) + ((unsigned int)(v_stack_m1FC) + 832);
    v_stack_m218 = a2;
    v_stack_m200 = 0;
    v_stack_m1B0 = *(unsigned __int64 *)(a2 + 56);
loc_0035C5DF:
    if (((*(unsigned __int64 *)(a2 + 56)) & (0xFFFULL)) == 0) goto loc_0035DD56;
    if (((*(unsigned __int64 *)(a2 + 56)) & (0xFFFULL)) != 0) goto loc_0035D85B;
    v_rdi = (*(unsigned __int64 *)(a2 + 56)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m238 = v_rdi;
    result = (v_rdi) >> (12);
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rdi + 40)));
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rip + 11320538)));
    v_stack_m198 = (unsigned int)(result);
    v_r10 = (unsigned int)((*(unsigned __int8 *)(v_rdi + 24)) - (8));
    v_stack_m1E8 = (unsigned int)((unsigned __int16)(result));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1896)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888));
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1896) + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888) * 1) >> (32);
    result = (a2) << (16);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888)) ^ (result);
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888) = a1;
    v_r10 = (v_r10) - 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1896) = a2;
    v_stack_m1C8 = (unsigned int)(*(unsigned __int8 *)(v_rdi + 50));
    v_stack_p8 = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 39));
    v_stack_p10 = (unsigned int)((unsigned __int8)(a3));
    v_stack_m1A8 = v_rdi + 64 + v_r10 * 8;
loc_0035C6A8:
    a2 = ~(*(unsigned __int64 *)(v_rdi + 64 + *(unsigned __int8 *)(v_rdi + 36) * 8));
    if (a2 == 0) goto loc_0035DD8D;
loc_0035C6B7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11320427)))) & (4)) != 0) goto loc_0035DBE9;
    if ((v_rdi + 64 + *(unsigned __int8 *)(v_rdi + 36) * 8) == (v_rdi + 64 + v_r10 * 8)) goto loc_0035E51A;
    if (((unsigned int)((unsigned int)(v_stack_m1C8))) != 64) goto loc_0035E51A;
    v_r10 = (unsigned int)(((unsigned int)(v_stack_m1C8)) + ((unsigned int)((unsigned __int8)(a3))));
    v_r10 = (unsigned int)((v_r10) & (63));
loc_0035C6EE:
    a4 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r10))));
loc_0035C6FA:
loc_0035C701:
    a1 = (*(unsigned __int64 *)(v_rdi + 64 + *(unsigned __int8 *)(v_rdi + 36) * 8)) | (a4);
    if (condition_is_not_equal) goto loc_0035C701;
    if (((*(unsigned __int64 *)(v_rdi + 64 + *(unsigned __int8 *)(v_rdi + 36) * 8)) & (a4)) != 0) goto loc_0035DBBC;
    a3 = (unsigned int)((v_rdi + 64 + *(unsigned __int8 *)(v_rdi + 36) * 8) - ((unsigned int)(v_rdi + 64)));
    v_stack_p10 = (unsigned int)(v_r10 + a3 * 8);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r10 + a3 * 8))) >> (6));
    *(unsigned __int8 *)(v_rdi + 36) = (unsigned __int8)(result);
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_r10 + a3 * 8))) * ((unsigned int)((unsigned int)(v_stack_m1E8))));
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_stack_m196)));
    if (v_stack_p8 <= 1) goto loc_0035DE7B;
    result = RtlpHpLfhSubsegmentCommitBlock((unsigned int)(v_stack_m1FC) + 832, v_stack_m238, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(v_stack_m1E8));
    if (sign_flag) goto loc_0035DCB9;
loc_0035C76D:
    v_rdi = (v_rdi) + (v_stack_m238);
    v_r10 = v_stack_m238;
    if (v_stack_m228 == 0) {
        a2 = (unsigned int)(v_rsi);
        a1 = v_rdi;
        a2 = (a2) + (15);
        a2 = (a2) & (-16);
        result = RtlHeapZero(a1, a2, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(v_stack_m1E8));
        v_r10 = v_stack_m238;
    }
    if (v_rdi == 0) goto loc_0035DCFA;
    if (v_stack_m200 != 0) goto loc_0035F446;
loc_0035C7A7:
loc_0035C7A9:
    if (v_rdi != -1) goto loc_0035C12B;
    goto loc_0035D984;
loc_0035C7C0:
    if ((unsigned int)(v_stack_m1FC) + 832 == 0) goto loc_0035CB63;
    goto loc_0035F4BD;
loc_0035C7D2:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12199240))) != 0) goto loc_0035CA28;
loc_0035C7E0:
    if ((((unsigned int)(v_stack_m1FC) + 832) & (0xFFFULL)) == 0) goto loc_0035CE37;
    if ((((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(v_stack_m1FC) + 832 - 13))) & (8)) != 0) goto loc_0035CF39;
loc_0035C800:
    result = *(unsigned __int8 *)((unsigned int)(v_stack_m1FC) + 832 - 13);
    v_r14 = (unsigned int)(v_stack_m1FC) + 832 - 16;
    if (((*(unsigned __int8 *)((unsigned int)(v_stack_m1FC) + 832 - 16 + 3)) & (4)) != 0) {
        result = *(unsigned __int16 *)((unsigned int)(v_stack_m1FC) + 832 - 16);
        a1 = 255;
        result = (unsigned __int16)((result) & ((unsigned __int16)(a1)));
        result = (unsigned __int16)(result);
        result = (result) << (4);
        v_r14 = ((unsigned int)(v_stack_m1FC) + 832 - 16) - (result);
    }
    a1 = 256;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r14 + 3))) & (1)) == 0) { a1 = 128; }
    a2 = ((unsigned int)((unsigned int)(a1))) | (4);
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r14 + 3))) & (32)) == 0) { a2 = a1; }
    a2 = (a2) | (2);
    v_stack_m238 = a2;
    a4 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_r14 + 3)))) & (8));
    if (condition_is_not_equal) goto loc_0035CE19;
loc_0035C860:
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r14 + 3))) & (222)) == 0) goto loc_0035C8B5;
    a1 = (a2) | (8);
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r14 + 3))) & (4)) == 0) { a1 = a2; }
    if (((128) & ((unsigned __int8)(*(unsigned __int8 *)(v_r14 + 3)))) == 0) { a1 = a1; }
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r14 + 3))) & (64)) == 0) { a1 = a1; }
    v_stack_m238 = a1;
    if (a4 != 0) goto loc_0035C8B5;
    v_stack_m238 = a1;
    result = 128;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r14 + 3))) & (16)) != 0) {
        result = a1;
        result = (result) | (32);
        v_stack_m238 = result;
    }
    v_r15 = ((unsigned __int8)(*(unsigned __int16 *)(v_r14 + 2))) << (4);
loc_0035C8C6:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13017860)))) & (519)) != 0) goto loc_0035E631;
loc_0035C8DC:
    result = (unsigned int)(*(unsigned int *)(v_rip + 13017838));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13017838)))) & (16)) != 0) {
        a4 = (unsigned int)(v_stack_m1FC) + 832;
        a3 = v_r15;
        a2 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 4)));
        a1 = v_r14;
        result = VfPtFreePoolNotification(a1, a2, a3, a4);
    }
    v_stack_m1C4 = (unsigned int)((unsigned int)(v_stack_m1FC) + 832);
    v_stack_m22C = 0;
    v_stack_m20C = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 4)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13011024))))) {
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13017583)))) & (65)) != 0) goto loc_0035E6C2;
loc_0035C91D:
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))))) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 4)))));
    a2 = (a1) >> (32);
    a2 = (unsigned int)((a2) ^ ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) & ((unsigned int)(*(unsigned __int64 *)(v_rip + 12198956))));
loc_0035C955:
    a1 = ((unsigned int)((unsigned int)(a2)) + (unsigned int)((unsigned int)(a2)) * 4) + ((unsigned int)((unsigned int)(a2)) + (unsigned int)((unsigned int)(a2)) * 4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 3524917 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 4))))) goto loc_0035CB79;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 3524917 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8))) == 0) goto loc_0035D3A2;
loc_0035C976:
    result = (unsigned int)((a2 + 1) & ((unsigned int)(*(unsigned __int64 *)(v_rip + 12198956))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_0035C955;
    v_stack_m138 = v_xmm0;
    result = 0;
    v_stack_m130 = v_rip + 12182387;
    v_stack_m138 = (unsigned int)(v_stack_m1FC) + 832;
    v_stack_m128 = 0;
    if ((*(unsigned int *)(v_rip + 13017964)) != 0) goto loc_0035D345;
loc_0035C9BA:
    v_stack_m128 = (unsigned __int8)(v_cr8);
    if (((*(unsigned __int8 *)(v_rip + 13017413)) & (33)) != 0) goto loc_0035D2D8;
loc_0035C9CB:
    if (v_stack_m138 != 0) goto loc_0035D6C8;
loc_0035C9DF:
loc_0035CA00:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1FC) + 832))))) >= (*(unsigned __int64 *)(v_rip + 12198754))) goto loc_0035D884;
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1FC) + 832)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1FC) + 832)))) * 4) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 12198736));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 4))))) goto loc_0035CA4E;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1))) == 0) goto loc_0035D884;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m1FC) + 832))) + 1);
    goto loc_0035CA00;
loc_0035CA28:
loc_0035CA36:
    if ((v_rip + 12133649) >= (v_rip + 12133674)) goto loc_0035C7E0;
    if (v_r15 == (*(unsigned __int64 *)(v_rip + 12133649))) goto loc_0035EC14;
    result = (v_rip + 12133649) + (8);
    goto loc_0035CA36;
loc_0035CA4E:
    if (condition_is_below) goto loc_0035CE27;
loc_0035CA67:
    a2 = -(v_r15);
    if ((*(unsigned __int64 *)(v_rip + 12133674 + 72)) != 0) goto loc_0035E714;
loc_0035CA81:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m138, a2, v_rip + 12133674 + 8, 1);
loc_0035CA8A:
    v_rsi = v_stack_m238;
    if ((*(unsigned __int64 *)(v_rip + 12133674 + 72)) < 0) {
        v_rsi = (v_stack_m238) >> (8);
        a4 = 0;
        v_rsi = (unsigned int)((v_rsi) & (1));
        a2 = v_r15;
        a3 = (unsigned int)(v_rsi);
        a1 = (unsigned int)(v_stack_m1FC) + 832;
        result = ViFreeTrackedPool(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 13050296)) != 0) goto loc_0035DA1A;
loc_0035CAB6:
    if ((v_r15 - 513) <= 0xD7FULL) goto loc_0035DDC2;
loc_0035CAD8:
    if ((unsigned __int16)(v_r14) == 0) goto loc_0035CAE7;
    v_rbx = (v_stack_m1E0) + (320);
    goto loc_0035CB26;
loc_0035CAE7:
    a2 = (v_r14) - (*(unsigned __int64 *)(v_rip + 11582224));
    a2 = (a2) >> (20);
    a2 = (a2) + (a2);
    result = RtlCSparseBitmapBitmaskRead(v_rip + 11582239, a2, a3, a4);
    if (result == 0) goto loc_0035E7A8;
    if (((unsigned int)(result)) == 3) goto loc_0035E7A8;
    v_rbx = (v_rbx) + (320);
    if (((unsigned int)(result)) == 2) goto loc_0035DAA3;
loc_0035CB26:
    a2 = (*(unsigned __int64 *)(v_rbx)) & (v_r14);
    result = (*(unsigned __int64 *)(a2 + 16)) ^ (*(unsigned __int64 *)(v_rip + 11319238));
    result = (result) ^ (a2);
    if (result == v_rbx) goto loc_0035CC00;
loc_0035CB46:
    a4 = 0;
    v_stack_m240 = (unsigned int)(v_stack_m1FC) + 832;
    v_stack_m248 = (unsigned int)(v_stack_m1FC) + 832;
    result = RtlpLogHeapFailure(a4 + 9, *(unsigned __int64 *)(v_rbx + 56), v_r14, a4);
loc_0035CB63:
    if (((v_stack_m1F0) & (32)) == 0) goto loc_0035F4BD;
    result = RtlRaiseStatus((unsigned int)(0xC000009AULL), *(unsigned __int64 *)(v_rbx + 56), v_r14, a4);
loc_0035CB79:
    if (condition_is_above_or_equal) goto loc_0035D2F7;
loc_0035CB8F:
    a1 = -(v_r15);
    if ((*(unsigned __int64 *)(a4 + 72)) == 0) goto loc_0035CA8A;
    if (((*(unsigned __int8 *)(a4 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1FC) + 832)))) * 8 + 56)) & (1)) != 0) goto loc_0035CA8A;
    v_r10 = (v_r15 * 4 + 63) & (-64);
    if (v_r10 == 64) { v_r10 = 128; }
loc_0035CBD9:
    if (a1 >= (*(unsigned __int64 *)(a4 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1FC) + 832)))) * 8 + 56))) goto loc_0035CA8A;
    if ((v_r10 + a1 * 1) >= (*(unsigned __int64 *)(a4 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1FC) + 832)))) * 8 + 56))) goto loc_0035CA8A;
    if ((v_r10 + a1 * 1) == (*(unsigned __int64 *)(a4 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1FC) + 832)))) * 8 + 56))) goto loc_0035E8C0;
    goto loc_0035CBD9;
loc_0035CC00:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)(a4 + 32)));
    a3 = (unsigned int)((a3) >> ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_r10 + a1 * 1 + 8))))));
    a3 = (a3) << (5);
    a3 = (a3) + (a4 + 32);
    result = -(*(unsigned __int8 *)(a3 + 26));
    result = (result) << (5);
    a3 = (a3) + (result);
    v_rdi = (a3) - (a4 + 32);
    v_rdi = (v_rdi) >> (5);
    v_rdi = (v_rdi) << ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_r10 + a1 * 1 + 8)))));
    v_rdi = (v_rdi) + (a4 + 32);
    result = (v_rdi == v_r14) ? 1 : 0;
    if (((unsigned __int8)(result + *(unsigned __int8 *)(a3 + 24) * 1)) != 11) goto loc_0035D208;
    result = (v_rdi) >> (12);
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rdi + 40)));
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rip + 11318942)));
    result = (result) >> (16);
    result = (result) + (v_rdi);
    a2 = (*(unsigned __int16 *)(v_rdi + 44)) << (6);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)(result)));
    v_rbx = ((unsigned int)(*(unsigned int *)(a2 + *(unsigned __int64 *)(v_r10 + a1 * 1 + 24) * 1 + 72))) * ((unsigned int)(a3));
    v_rbx = (v_rbx) >> (32);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) * ((unsigned int)((unsigned __int16)(result))));
    if (a3 != ((unsigned int)(result))) goto loc_0035CB63;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r10 + a1 * 1 + 24) + 76))))) >> (13));
    result = (unsigned int)((result) & (0x3FFFFULL));
    a3 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r10 + a1 * 1 + 24) + 76))) >> (4);
    a3 = (unsigned int)((a3) & (511));
    a4 = (unsigned int)((1) << ((unsigned __int8)((unsigned __int16)(result))));
    a1 = (unsigned int)(((unsigned __int16)(result)) + (-2));
    a4 = (unsigned int)((a4) ^ ((unsigned int)(result)));
    v_stack_m148 = (unsigned int)(a1);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35760) + a1 * 8) + a4 * 8 + 8) + a3 * 8) == 0) goto loc_0035E94B;
loc_0035CCED:
    if (((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35760) + a1 * 8) + a4 * 8 + 8) + a3 * 8))) == (*(unsigned __int16 *)(v_rdi + 46))) goto loc_0035E8DE;
loc_0035CCF7:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (63));
    result = (v_rbx) >> (6);
    if (condition_is_above_or_equal) goto loc_0035D36D;
loc_0035CD1C:
    v_stack_m1C0 = *(unsigned __int64 *)(v_rdi + 16);
    a1 = (*(unsigned __int64 *)(v_rdi + 16)) >> (48);
    v_stack_m238 = *(unsigned __int64 *)(v_rdi + 16);
    if (((unsigned __int8)(a1)) == 1) {
        v_stack_m232 = 2;
    }
    if (v_r14 != 0) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r10 + a1 * 1 + 24) + 80);
        a1 = v_stack_m238;
        a2 = a3;
        *(unsigned __int16 *)(v_r14) = (unsigned __int16)(a1);
        a2 = (unsigned int)((a2) ^ (*(unsigned int *)(v_r14)));
        a1 = (unsigned __int8)(a1);
        a1 = v_rbx + 1;
        a3 = (a3) >> (32);
        a2 = (unsigned int)((a2) ^ (a3));
        v_stack_m238 = (unsigned __int16)(a1);
        a2 = (unsigned int)((a2) ^ ((unsigned int)(v_r14)));
        *(unsigned int *)(v_r14 + 8) = (unsigned int)(a2);
    }
    a2 = (*(unsigned __int16 *)(v_rdi + 44)) << (6);
    if (condition_is_not_equal) goto loc_0035CD1C;
    if ((*(unsigned __int8 *)(a2 + *(unsigned __int64 *)(v_r10 + a1 * 1 + 24) * 1 + 92)) == 0) goto loc_0035D3D5;
loc_0035CD8E:
    if (v_stack_m1BA != 1) goto loc_0035CB63;
    a4 = (unsigned int)((v_stack_m1BC) << (6));
    a4 = (a4) + (*(unsigned __int64 *)(v_r10 + a1 * 1 + 24));
    a2 = (unsigned int)((*(unsigned __int64 *)(a4 + 8)) & (0xFFFULL));
    a3 = (unsigned int)((*(unsigned __int64 *)(v_rdi + 24)) & (0xFFFULL));
    a1 = (*(unsigned __int64 *)(a4 + 8)) - (a2);
    a1 = (a1) | (a3);
    *(unsigned __int64 *)(v_rdi + 24) = a1;
    a1 = (v_rdi) | (a2);
    if (condition_is_equal) goto loc_0035CB63;
loc_0035CDE3:
    a1 = (*(unsigned __int64 *)(a4 + 8)) ^ (*(unsigned __int64 *)(v_rdi + 24));
    a2 = (unsigned int)((*(unsigned __int64 *)(a4 + 8)) & (0xFFFULL));
    a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (a1) ^ (*(unsigned __int64 *)(v_rdi + 24));
    *(unsigned __int64 *)(v_rdi + 24) = a1;
    a1 = (v_rdi) | (a2);
    if ((*(unsigned __int64 *)(a4 + 8)) != (*(unsigned __int64 *)(a4 + 8))) goto loc_0035CDE3;
    goto loc_0035CB63;
loc_0035CE19:
    a2 = (a2) | (1);
    v_stack_m238 = a2;
    goto loc_0035C860;
loc_0035CE27:
    goto loc_0035CA67;
loc_0035CE37:
    if (((unsigned int)(v_stack_m1FC) + 832) < (a1 + 48)) goto loc_0035CE67;
    result = ((unsigned int)(v_stack_m1FC) + 832) >> (39);
    result = (unsigned int)((result) & (511));
    result = (unsigned int)((result) + (0xFFFFFF00ULL));
    if (((unsigned __int8)(*(unsigned __int8 *)(result + v_rdi * 1 + 14912168))) == 5) goto loc_0035F0BB;
loc_0035CE67:
loc_0035CE6D:
    v_stack_mC0 = (unsigned int)(v_stack_m1FC) + 832;
    v_stack_mB8 = (unsigned int)(v_stack_m1FC) + 832;
    v_stack_mB0 = (unsigned int)(v_stack_m1FC) + 832;
    if ((*(unsigned int *)(v_rip + 13016714)) != 0) goto loc_0035D3FC;
loc_0035CE9C:
    if (((*(unsigned __int8 *)(v_rip + 13016163)) & (33)) == 0) goto loc_0035D30A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12259241))) != 0) goto loc_0035D30A;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(v_rip + 12181046, 2, a1 + 32, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1FC) + 832)));
loc_0035CEC7:
    result = ((unsigned int)(v_stack_m1FC) + 832) >> (12);
    a1 = (v_rip + 12181046) * (result);
    result = (a1) >> (32);
    a1 = (a1) ^ (result);
    a2 = (unsigned int)((*(unsigned __int64 *)(v_rip + 12197482) - 1) & ((unsigned int)(a1)));
loc_0035CEF9:
    a1 = ((unsigned int)((unsigned int)(a2))) << (5);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 12197464));
    if ((*(unsigned __int64 *)(a1)) == ((unsigned int)(v_stack_m1FC) + 832)) goto loc_0035D140;
    a2 = (unsigned int)((a2) + 1);
    if (((unsigned int)((unsigned int)(a2))) < (*(unsigned __int64 *)(v_rip + 12197482))) goto loc_0035CEF9;
    if (1 != 0) goto loc_0035E76A;
loc_0035CF20:
    v_stack_m248 = (unsigned int)(v_stack_m1FC) + 832;
    result = KeBugCheckEx(34 - 9, 34, (unsigned int)(v_stack_m1FC) + 832, 64);
loc_0035CF39:
    if ((((unsigned __int8)(result)) & (4)) != 0) {
        result = *(unsigned __int16 *)(64);
        result = (unsigned __int16)((result) & (255));
        result = (unsigned __int16)(result);
        result = (result) << (4);
        a1 = (64) - (result);
    }
    a1 = (a1) ^ (*(unsigned __int64 *)(a1 + 8));
    a1 = (a1) ^ (*(unsigned __int64 *)(v_rip + 13017799));
    if (condition_is_equal) goto loc_0035C800;
    if (a1 == -1) goto loc_0035C800;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12197289))) != 0) goto loc_0035E793;
loc_0035CF7F:
    if (((unsigned int)(v_stack_m1FC) + 832) < ((unsigned int)(v_stack_m1FC) + 832)) goto loc_0035CFAF;
    result = ((unsigned int)(v_stack_m1FC) + 832) >> (39);
    result = (unsigned int)((result) & (511));
    result = (unsigned int)((result) + (0xFFFFFF00ULL));
    if (((unsigned __int8)(*(unsigned __int8 *)(result + v_rdi * 1 + 14912168))) == 5) goto loc_0035F0A8;
loc_0035CFAF:
loc_0035CFB5:
    result = *(unsigned __int8 *)(result + v_rdi * 1 + 14912168);
    if (((*(unsigned __int8 *)((unsigned int)(v_stack_m1FC) + 832 - 13)) & (4)) != 0) {
        result = *(unsigned __int16 *)((unsigned int)(v_stack_m1FC) + 832 - 16);
        result = (unsigned __int16)((result) & (255));
        result = (unsigned __int16)(result);
        result = (result) << (4);
        a2 = ((unsigned int)(v_stack_m1FC) + 832 - 16) - (result);
    }
    v_rbx = ((unsigned __int8)(*(unsigned __int16 *)(a2 + 2))) << (4);
    result = (unsigned __int16)((*(unsigned __int16 *)(a2 + 2)) >> (8));
    if ((((unsigned __int8)(result)) & (8)) == 0) goto loc_0035D136;
    v_rdi = (*(unsigned __int64 *)(v_rip + 13017653)) ^ (*(unsigned __int64 *)(a2 + 8));
    result = (a2) ^ (*(unsigned __int64 *)(v_rip + 13017639));
    *(unsigned __int64 *)(a2 + 8) = result;
    v_rdi = (v_rdi) ^ (a2);
    if (condition_is_equal) goto loc_0035D136;
    if (v_rdi == -1) goto loc_0035D136;
    if (v_rdi < ((unsigned int)(v_stack_m1FC) + 832)) goto loc_0035E68C;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rdi)) & (127));
    if (((unsigned __int8)(result)) != 3) goto loc_0035E68C;
    v_r14 = (unsigned int)((64) & (256));
    if (v_rdi == (*(unsigned __int64 *)(v_rip + 13015668))) goto loc_0035D104;
    result = (v_r14 != 0) ? 1 : 0;
    v_r15 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) << (7);
    v_r15 = (v_r15) + (*(unsigned __int64 *)(v_rdi + 760));
    v_stack_p8 = *(unsigned __int64 *)(v_rdi + 760);
    if ((*(unsigned __int64 *)(v_r15 + 80)) == 0) goto loc_0035D0A8;
    a3 = ((unsigned int)(v_stack_m1FC) + 832) * ((unsigned int)((unsigned int)(result)));
    if ((*(unsigned __int64 *)(v_r15 + 64)) <= (*(unsigned __int64 *)(v_r15))) goto loc_0035D0A8;
    a1 = (*(unsigned __int64 *)(v_r15 + 64)) - (*(unsigned __int64 *)(v_r15));
    if (a1 > (*(unsigned __int64 *)(a3 + v_rip - 3526732 * 1 + 15754824))) goto loc_0035D5DD;
loc_0035D0A8:
    v_r10 = ((unsigned int)((unsigned int)(result))) << (7);
loc_0035D0B9:
    a3 = *(unsigned __int64 *)(v_r15);
    if (v_rbx < (*(unsigned __int64 *)(v_r15))) { a3 = v_rbx; }
    a1 = (*(unsigned __int64 *)(v_r15)) - (v_rbx);
    a2 = 0;
    if (v_rbx < (*(unsigned __int64 *)(v_r15))) { a2 = a1; }
    if (v_rbx != (*(unsigned __int64 *)(v_r15))) goto loc_0035D0B9;
    v_rbx = (v_rbx) - (a3);
    if (condition_is_not_equal) goto loc_0035D9F7;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rip - 3526732 + (unsigned int)((unsigned int)(result)) * 8 + 16544592))) & (4)) != 0) {
        a4 = -(v_rbx);
    }
    v_r13 = 0;
loc_0035D104:
    result = *(unsigned __int64 *)(v_r15);
    if ((*(unsigned int *)(v_rip + 13008645)) != 0) {
        a2 = 0;
        a1 = v_rdi - 48;
        a4 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4)));
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    v_rsi = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_0035DEA3;
loc_0035D136:
    goto loc_0035C800;
loc_0035D140:
    if (a1 == 0) goto loc_0035CF20;
    v_stack_mC0 = a4;
    v_stack_mB0 = v_rip + 13049776;
    v_stack_mB8 = a3;
    v_r14 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12))))) >> (8);
    v_r14 = (unsigned int)((v_r14) & (0xFFFULL));
    v_stack_m208 = *(unsigned __int64 *)(a1 + 16);
    v_stack_m238 = v_r14;
    if (condition_is_below) goto loc_0035D38F;
loc_0035D19B:
    *(unsigned __int64 *)(a1 + 24) = 0;
    if (((*(unsigned __int8 *)(v_rip + 13015378)) & (1)) != 0) goto loc_0035DE3C;
loc_0035D1BA:
loc_0035D1CC:
    result = -1;
    if ((*(unsigned int *)(v_rip + 13015885)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_r15);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    if ((-1 - 1) <= -3) goto loc_0035D6D6;
loc_0035D1F8:
    goto loc_0035C8C6;
loc_0035D208:
    a4 = (a4) & (a3);
    v_stack_m190 = 0;
    a2 = (a3) - (a4);
    a2 = (a2) >> (5);
    result = (unsigned __int8)(((unsigned __int8)(v_rip + 11316942)) & (3));
    a2 = (a2) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r10))));
    a2 = (a2) + (a4);
    if (((unsigned __int8)(result)) != 3) goto loc_0035CB46;
    if (v_stack_p10 == a2) goto loc_0035D35D;
    if (((unsigned __int8)(v_rip + 11316942)) != 15) goto loc_0035CB46;
    if (v_stack_p10 <= a2) goto loc_0035D35D;
    result = RtlpHpVsContextFree(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 8)) + 32), a2, v_stack_p10, v_stack_m190);
    if ((unsigned int)(result) == 0) goto loc_0035CB63;
    if (((unsigned int)((unsigned int)(v_stack_m190))) >= ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 8)) + 24) + 68)))) goto loc_0035CB63;
    a1 = (unsigned int)(((unsigned int)(v_stack_m190)) + (15));
    a1 = (a1) >> (4);
    v_r10 = (unsigned int)((*(unsigned __int8 *)(a1 + -1 * 1 + 68480)) - 1);
loc_0035D28F:
    v_stack_m1A0 = *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 8)) + 24) + v_r10 * 8 + 448);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 8)) + 24) + v_r10 * 8 + 448)) >> (16);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 8)) + 24) + v_r10 * 8 + 448))) & (1)) == 0) goto loc_0035D2CB;
    if (((unsigned __int16)(result)) >= = 1) {
        result = (unsigned __int16)((result) - 1);
        v_stack_m19E = (unsigned __int16)(result);
        a2 = v_stack_m1A0;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 8)) + 24) + v_r10 * 8 + 448)) != (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 8)) + 24) + v_r10 * 8 + 448))) goto loc_0035D28F;
loc_0035D2CB:
    goto loc_0035CB63;
loc_0035D2D8:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12258170))) != 0) goto loc_0035C9CB;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m138, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 8)) + 24) + v_r10 * 8 + 448), *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 8)) + 24), *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 8)) + 24) + v_r10 * 8);
    goto loc_0035C9DF;
loc_0035D2F7:
    goto loc_0035CB8F;
loc_0035D30A:
loc_0035D31B:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12258170))) == 0) goto loc_0035CEC7;
    if (!sign_flag) goto loc_0035D31B;
    result = ExpWaitForSpinLockSharedAndAcquire(v_rip + 12179901, (unsigned __int8)(v_stack_m208), 1, *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 8)) + 24) + v_r10 * 8);
    goto loc_0035CEC7;
loc_0035D345:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p10), (unsigned __int8)(result), 1, *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 8)) + 24) + v_r10 * 8);
    goto loc_0035C9BA;
loc_0035D35D:
    result = RtlpHpSegPageRangeShrink((unsigned int)(*(unsigned int *)(a1 + 8)), 1, 1, *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 8)) + 24) + v_r10 * 8);
    goto loc_0035CB63;
loc_0035D36D:
    v_stack_m240 = 0;
    v_stack_m248 = 1;
    result = RtlpLogHeapFailure(17, *(unsigned __int64 *)(-1), v_stack_p10, v_stack_p10);
    goto loc_0035CB63;
loc_0035D38F:
    v_rdi = (*(unsigned __int64 *)(17 + 24)) ^ (*(unsigned __int64 *)(v_rip + 13016718));
    v_rdi = (v_rdi) ^ (v_stack_p10);
    goto loc_0035D19B;
loc_0035D3A2:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12196279) + 17 * 8))) == 0) goto loc_0035C976;
    *(unsigned int *)(v_stack_p10) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12196279) + 17 * 8)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12196258) + 17 * 8 + 72) == 0) goto loc_0035C955;
    *(unsigned __int64 *)(v_stack_p10 + 72) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12196258) + 17 * 8 + 72);
    goto loc_0035C955;
loc_0035D3D5:
    *(unsigned __int8 *)(*(unsigned __int64 *)(-1) + -1 * 1 + 92) = 1;
    result = RtlpHpEnvCompactionIsScheduled(*(unsigned __int64 *)(*(unsigned __int64 *)(-1) + 56), *(unsigned __int64 *)(-1), v_stack_p10, v_stack_p10);
    if ((unsigned int)(result) != 0) goto loc_0035CD8E;
    result = RtlpHpEnvCompactionSchedule(*(unsigned __int64 *)(*(unsigned __int64 *)(-1) + 56), *(unsigned __int64 *)(-1), v_stack_p10, v_stack_p10);
    goto loc_0035CD8E;
loc_0035D3FC:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_m208), (unsigned __int8)(result), v_stack_p10, v_stack_p10);
    goto loc_0035CE9C;
loc_0035D40D:
    goto loc_0035C4CE;
loc_0035D418:
    result = 0;
    v_stack_mF0 = 0;
    v_stack_m22F = 0;
    v_stack_m20F = 0;
    v_stack_p10 = v_stack_m1F8;
    v_stack_m1D4 = -1;
    v_stack_m100 = v_xmm0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13008152))))) {
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13014711)))) & (65)) != 0) goto loc_0035E7B8;
loc_0035D455:
    v_r12 = (v_stack_p10) & (-5);
    v_stack_m1A0 = *(unsigned __int64 *)(v_rip + 12196081);
    v_stack_m1B8 = *(unsigned __int64 *)(v_rip + 12196062);
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))))) * ((unsigned int)(*(unsigned int *)(a1 + 8)));
    v_stack_m1E0 = *(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424);
    v_rsi = (a1) >> (32);
    v_rsi = (unsigned int)((v_rsi) ^ ((unsigned int)(a1)));
    v_rsi = (unsigned int)((v_rsi) & ((unsigned int)(*(unsigned __int64 *)(v_rip + 12196081))));
    v_stack_p8 = (unsigned int)(v_rsi);
loc_0035D4AA:
    v_r15 = ((unsigned int)((unsigned int)(v_rsi)) + (unsigned int)((unsigned int)(v_rsi)) * 4) << (4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))))) goto loc_0035D633;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))))) goto loc_0035DC0E;
loc_0035D4E0:
    v_stack_p8 = 1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1 + 72)) == 0) goto loc_0035D662;
loc_0035D50B:
loc_0035D50F:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1 + (int)(1) * 8 + 56))) & (1)) != 0) goto loc_0035D662;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1 + (int)(1) * 8 + 56)) >= v_stack_p10) goto loc_0035D662;
    result = ExpTrackTableGetMoreLimit(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1 + 72), v_stack_p10, 1, v_stack_p10);
    if (result == 0) goto loc_0035F463;
    if (result != 1) goto loc_0035E775;
    if (result == 1) goto loc_0035D662;
    goto loc_0035D50B;
loc_0035D567:
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1 + (int)(1) * 8 + 56)) - (*(unsigned __int64 *)(v_rip + 11579536));
    a2 = (a2) >> (20);
    a2 = (a2) + (a2);
    result = RtlCSparseBitmapBitmaskRead(v_rip + 11579551, a2, 1, v_stack_p10);
    if (result == 0) goto loc_0035D594;
    result = (unsigned int)((result) - 1);
    if (((unsigned int)(result)) != 2) goto loc_0035BEBD;
loc_0035D594:
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    result = RtlpHpVaMgrCtxQuery(v_rip + 11579568, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1 + (int)(1) * 8 + 56), v_stack_m90, v_stack_p10);
    v_stack_m58 = v_stack_m80;
    v_stack_mD0 = (unsigned int)((unsigned int)(v_stack_m78));
    goto loc_0035BEFB;
loc_0035D5DD:
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1 + (int)(1) * 8 + 56);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1 + (int)(1) * 8 + 56)) > (*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1 + 8)) { a2 = *(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1 + 8; }
    a1 = ((unsigned int)(v_stack_m78)) - (a2);
    if (condition_is_not_equal) goto loc_0035D0A8;
    a2 = (a2) + (a2);
    if (a2 <= (*(unsigned __int64 *)(v_stack_m90 + v_stack_p10 * 1 + 15754824))) goto loc_0035D0A8;
    a3 = 0;
    if (0 == 0) goto loc_0035D0A8;
    a4 = 0;
    result = PspReturnResourceQuota((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1 + (int)(1) * 8 + 56))), *(unsigned __int64 *)(v_stack_m80), a3, a4);
    goto loc_0035D0A8;
loc_0035D633:
    if ((unsigned int)(result) == 0) goto loc_0035D9B6;
loc_0035D63B:
    result = (unsigned int)((v_stack_p10 + 1) & ((unsigned int)(*(unsigned __int64 *)(v_stack_m80))));
    if (((unsigned int)(result)) != 0) goto loc_0035D4AA;
    result = ExpInsertPoolTrackerExpansion((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1 + 8)), v_stack_p10, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1 + (int)(1) * 8 + 56), a4);
loc_0035D662:
loc_0035D665:
    v_stack_p10 = v_rdi;
    v_rdi = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 13047292)) != 0) goto loc_0035E3F9;
loc_0035D68A:
    a4 = (0) & (-8);
    v_r13 = (v_r13) - (a4);
    a1 = (0) - (a4);
    a1 = (a1) + (v_stack_m1F8);
    v_r13 = (v_r13) + (0);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 13047292)) == 0) goto loc_0035BBCD;
    if (a4 >= v_stack_p10) goto loc_0035F41A;
    v_stack_m248 = 0;
    result = KeBugCheckEx(497, 2, 1, a4);
loc_0035D6C8:
    result = KxWaitForLockOwnerShip(v_stack_m138, 2, 1, a4);
    goto loc_0035C9DF;
loc_0035D6D6:
    a1 = (unsigned int)((*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1) & (256));
    if (0 == (*(unsigned __int64 *)(v_rip + 13013962))) goto loc_0035D7BA;
    result = (a1 != 0) ? 1 : 0;
    v_r14 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) << (7);
    v_r14 = (v_r14) + (*(unsigned __int64 *)(v_rdi + 760));
    v_stack_p8 = (unsigned __int8)(*(unsigned __int8 *)(v_rip - 3528438 + (unsigned int)((unsigned int)(result)) * 8 + 16544592));
    if ((*(unsigned __int64 *)(v_r14 + 80)) == 0) goto loc_0035D751;
    a3 = (1) * ((unsigned int)((unsigned int)(result)));
    if ((*(unsigned __int64 *)(v_r14 + 64)) <= (*(unsigned __int64 *)(v_r14))) goto loc_0035D751;
    a1 = (*(unsigned __int64 *)(v_r14 + 64)) - (*(unsigned __int64 *)(v_r14));
    if (a1 > (*(unsigned __int64 *)(a3 + v_rip - 3528438 * 1 + 15754824))) goto loc_0035DA49;
loc_0035D751:
    v_r10 = ((unsigned int)((unsigned int)(result))) << (7);
loc_0035D764:
    a3 = *(unsigned __int64 *)(v_r14);
    if (v_stack_m208 < (*(unsigned __int64 *)(v_r14))) { a3 = v_stack_m208; }
    a1 = (*(unsigned __int64 *)(v_r14)) - (v_stack_m208);
    a2 = 0;
    if (v_stack_m208 < (*(unsigned __int64 *)(v_r14))) { a2 = a1; }
    if (v_stack_m208 != (*(unsigned __int64 *)(v_r14))) goto loc_0035D764;
    a4 = (v_stack_m208) - (a3);
    if (condition_is_not_equal) goto loc_0035DED0;
    result = *(unsigned __int64 *)(v_r14);
    if (((v_stack_p8) & (4)) != 0) {
        result = v_stack_m208;
        a1 = v_rdi + (unsigned int)((unsigned int)(result)) * 8;
        result = -(result);
    }
    v_r13 = 0;
loc_0035D7BA:
    if ((*(unsigned int *)(v_rip + 13006927)) != 0) {
        a2 = 0;
        a1 = v_rdi - 48;
        a4 = (unsigned int)(*(unsigned __int64 *)(v_rip - 3527803 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + v_r15 * 1 + 8);
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    v_rsi = ((unsigned int)((unsigned int)(result))) - (1);
    if (condition_is_greater) goto loc_0035D1F8;
    if (*(unsigned __int64 *)(v_rdi - 40) != 0) goto loc_0035E977;
    if (!sign_flag) goto loc_0035EA09;
    a2 = 0;
    v_stack_m248 = v_rsi;
    result = KeBugCheckEx(a2 + 24, a2, 0, *(unsigned __int64 *)(v_rdi - 40) + 4);
loc_0035D812:
    v_rsi = (v_rsi) + ((unsigned int)(*(unsigned int *)(v_rip + 13014120)));
    if (v_rsi <= 0xFE0ULL) goto loc_0035C187;
    v_rsi = (v_rsi) - ((unsigned int)(*(unsigned int *)(v_rip + 13014120)));
    v_r11 = (v_rip + 11315235) & (-9);
    v_stack_m1F0 = v_r11;
    goto loc_0035C187;
loc_0035D839:
    v_stack_m200 = 1;
    goto loc_0035C2BA;
loc_0035D849:
    if (((unsigned int)(*(unsigned __int64 *)(v_r14))) == 0x80000000ULL) goto loc_0035BB23;
    goto loc_0035BB3B;
loc_0035D85B:
    v_stack_m200 = (unsigned int)(v_r10);
    v_stack_m1B0 = (unsigned int)(*(unsigned int *)(v_rip + 13014120));
    goto loc_0035C5DF;
loc_0035D86C:
    v_rsi = (v_rsi) + (0xFFFULL);
    v_rsi = (v_rsi) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m1F8 = v_rsi;
    goto loc_0035BBB7;
loc_0035D884:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m138, a2, 0, *(unsigned __int64 *)(v_rdi - 40) + 4);
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12194996))) - 1);
    a1 = (a3 + a3 * 4) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip - 3528872 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424));
    result = -(*(unsigned __int64 *)(v_r14));
    if (condition_is_below) goto loc_0035D9A7;
    goto loc_0035CA8A;
loc_0035D8DB:
loc_0035D8E2:
    result = RtlpHpLfhSlotAllocateSlow(*(unsigned __int64 *)(v_r14) + 832, *(unsigned __int64 *)(v_rip - 3528872 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424), (unsigned int)((unsigned int)(v_rsi)), (unsigned int)((unsigned int)(v_r14)));
loc_0035D8F5:
    if (result == -1) goto loc_0035D943;
loc_0035D8FB:
    if (result == 0) goto loc_0035D91E;
loc_0035D905:
    a1 = ((((unsigned __int8)(v_stack_m1F0)) & (16)) == 0) ? 1 : 0;
    result = ((((unsigned __int8)(v_stack_m1F0)) & (16)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0035DEF4;
loc_0035D91E:
    v_r12 = 0;
    v_stack_p10 = 0;
    goto loc_0035C16F;
loc_0035D92D:
    result = RtlpHpLfhBucketCheckAndUpdate(v_stack_m1F0, *(unsigned __int64 *)(v_rip - 3528872 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424), (unsigned int)((unsigned int)(v_rsi)), (unsigned int)((unsigned int)(v_r14)));
    if (result != 0) goto loc_0035DC78;
loc_0035D943:
loc_0035D947:
    if (v_stack_m1A8 > 0x20000ULL) goto loc_0035E929;
    result = RtlpHpVsContextAllocate(*(unsigned __int64 *)(v_r14) + 704, (unsigned int)((unsigned int)(v_stack_m228)), (unsigned int)((unsigned int)(v_stack_m1A8)), (unsigned int)((unsigned int)(v_r14)));
loc_0035D969:
    goto loc_0035D8FB;
loc_0035D96E:
    result = RtlpHpLfhBucketCheckAndUpdate(v_stack_m1F0, (unsigned int)((unsigned int)(v_stack_m228)), (unsigned int)((unsigned int)(v_stack_m1A8)), (unsigned int)((unsigned int)(v_r14)));
    if (result != 0) goto loc_0035DD0F;
loc_0035D97F:
loc_0035D984:
    if (result > 0x20000ULL) goto loc_0035E958;
    result = RtlpHpVsContextAllocate(*(unsigned __int64 *)(v_r14) + 704, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r14)));
    goto loc_0035C128;
loc_0035D9A7:
    goto loc_0035CA8A;
loc_0035D9B6:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r14) + *(unsigned __int64 *)(v_rip + 12194723) * 1))) == 0) goto loc_0035DAAF;
    *(unsigned int *)(v_r14) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r14) + *(unsigned __int64 *)(v_rip + 12194723) * 1)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14) + *(unsigned __int64 *)(v_rip + 12194700) * 1 + 72) == 0) goto loc_0035D4AA;
    *(unsigned __int64 *)(v_r14 + 72) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r14) + *(unsigned __int64 *)(v_rip + 12194700) * 1 + 72);
    goto loc_0035D4AA;
loc_0035D9EB:
    v_rsi = (result) + (192);
    goto loc_0035BC2A;
loc_0035D9F7:
    if (v_stack_p8 != v_stack_m1F0) goto loc_0035DDA3;
    v_stack_m248 = (unsigned int)((unsigned int)(result));
    result = KeBugCheckEx(33, result, v_stack_m228, (unsigned int)((unsigned int)(v_r14)));
loc_0035DA1A:
    if (v_r14 >= result) goto loc_0035F14B;
    v_stack_m248 = 0;
    result = KeBugCheckEx(497, 2, 2 - 1, v_r14);
loc_0035DA49:
    a2 = 2;
    if (2 > v_stack_m208) { a2 = v_stack_m208; }
    a1 = (result) - (a2);
    if (condition_is_not_equal) goto loc_0035D751;
    a2 = (a2) + (a2);
    if (a2 <= (*(unsigned __int64 *)(2 - 1 + v_r14 * 1 + 15754824))) goto loc_0035D751;
    a3 = 0;
    if (0 == 0) goto loc_0035D751;
    a4 = 0;
    result = PspReturnResourceQuota((unsigned int)((unsigned int)(v_stack_m228)), v_r14, a3, a4);
    goto loc_0035D751;
loc_0035DAA3:
    v_rbx = ((unsigned int)((unsigned int)(result))) + (192);
    goto loc_0035CB26;
loc_0035DAAF:
    if (((unsigned int)((unsigned int)(v_stack_m228))) == (v_stack_m1F0 - 1)) goto loc_0035D63B;
    v_stack_m100 = 0;
    v_stack_mF8 = v_rip + 12177981;
    v_stack_m218 = (unsigned __int8)(v_r15);
    if ((*(unsigned int *)(v_rip + 13013559)) != 0) goto loc_0035DE62;
loc_0035DAEF:
    v_stack_mF0 = (unsigned __int8)((unsigned __int8)(v_r15));
    if (((*(unsigned __int8 *)(v_rip + 13013008)) & (33)) != 0) goto loc_0035DD6E;
loc_0035DAFF:
    if (v_stack_m100 != 0) goto loc_0035E41A;
loc_0035DB13:
    result = (*(unsigned __int64 *)(v_rip + 12194374)) + (*(unsigned __int64 *)(v_r14));
    v_stack_m218 = result;
    if ((*(unsigned int *)(result)) == 0) {
        a1 = (unsigned int)(v_rbx);
        result = ExpPlFindLimitEntry(a1, v_stack_m100, a3, a4);
        a1 = v_stack_m218;
        *(unsigned __int64 *)(a1 + 72) = result;
        *(unsigned __int64 *)(v_r14 + 72) = result;
        result = *(unsigned __int64 *)(v_rip + 12194334);
        *(unsigned int *)(*(unsigned __int64 *)(v_r14) + result * 1) = (unsigned int)(v_rbx);
        *(unsigned int *)(v_r14) = (unsigned int)(v_rbx);
    }
    result = KeReleaseInStackQueuedSpinLock(v_stack_m100, v_stack_m100, a3, a4);
    goto loc_0035D4AA;
loc_0035DB6A:
    a2 = ~(v_stack_m1A0);
    if (a2 != 0) goto loc_0035C39B;
    if (((unsigned int)(v_stack_p8)) == v_stack_m1B8) goto loc_0035DD9B;
    a3 = ((unsigned int)(v_stack_p8)) + (8);
    goto loc_0035C38C;
loc_0035DB97:
    result = (unsigned int)((result) * ((unsigned int)((unsigned int)(v_stack_p10))));
    result = (unsigned int)((result) >> (8));
    goto loc_0035C3D9;
loc_0035DBBC:
    a2 = ~(a2);
    if (a2 != 0) goto loc_0035C6B7;
    if (a3 == v_stack_m1A8) goto loc_0035DDBA;
    a3 = (a3) + (8);
    goto loc_0035C6A8;
loc_0035DBE9:
    result = (unsigned int)((result) * ((unsigned int)((unsigned int)(v_stack_p10))));
    result = (unsigned int)((result) >> (8));
    goto loc_0035C6FA;
loc_0035DC0E:
    a1 = 0;
    goto loc_0035D4E0;
loc_0035DC1D:
    a4 = 0;
    if (((unsigned int)((unsigned int)(v_stack_p10))) == -1) goto loc_0035EA17;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))) >> (6));
    a1 = (unsigned int)(((unsigned int)(v_stack_p10)) & (63));
loc_0035DC50:
    a1 = (*(unsigned __int64 *)(v_stack_m1B8 + result * 8 + 64)) & (-2);
    if (condition_is_not_equal) goto loc_0035DC50;
loc_0035DC63:
loc_0035DC78:
    a1 = (v_stack_m1B4) << (8);
    a1 = (a1) + (0x5C0ULL);
    a1 = (a1) + (*(unsigned __int64 *)(v_r14) + 832);
    if (v_stack_p10 == a1) goto loc_0035C286;
    *(unsigned __int16 *)(v_stack_m218) = (unsigned __int16)(*(unsigned __int16 *)(a1 + v_stack_p8 * 1));
    goto loc_0035C286;
loc_0035DCB9:
    a4 = 0;
    if (((unsigned int)((unsigned int)(v_stack_p10))) == -1) goto loc_0035C78C;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))) >> (6));
    a1 = (unsigned int)(((unsigned int)(v_stack_p10)) & (63));
loc_0035DCEC:
    a1 = (*(unsigned __int64 *)(v_stack_m1A8 + result * 8 + 64)) & (-2);
    if (condition_is_not_equal) goto loc_0035DCEC;
loc_0035DCFA:
loc_0035DD0F:
    a1 = (v_stack_m1A4) << (8);
    a1 = (a1) + (0x5C0ULL);
    a1 = (a1) + (*(unsigned __int64 *)(v_r14) + 832);
    if (2 == a1) goto loc_0035C5AB;
    *(unsigned __int16 *)(v_stack_p8 + 2 * 1) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_p8 + a1 * 1));
    goto loc_0035C5AB;
loc_0035DD48:
    if (((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_p8 + a1 * 1)))) == v_stack_m1A8) goto loc_0035DD9B;
    a3 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_p8 + a1 * 1)))) + (8);
    goto loc_0035C38C;
loc_0035DD56:
    result = RtlpHpLfhSlotAllocateSlow(*(unsigned __int64 *)(v_r14) + 832, *(unsigned __int16 *)(v_stack_p8 + a1 * 1), 0, (unsigned int)((unsigned int)(v_r14)));
    goto loc_0035C7A9;
loc_0035DD6E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12255460))) != 0) goto loc_0035DAFF;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m100, *(unsigned __int64 *)(v_r14) + 832, 0, (unsigned int)((unsigned int)(v_r14)));
    goto loc_0035DB13;
loc_0035DD8D:
    if (0 == v_stack_m1A8) goto loc_0035DDBA;
    a3 = (0) + (8);
    goto loc_0035C6A8;
loc_0035DD9B:
    goto loc_0035C38C;
loc_0035DDA3:
    v_stack_p8 = *(unsigned __int64 *)(v_r14) + 832;
    goto loc_0035D0B9;
loc_0035DDBA:
    goto loc_0035C6A8;
loc_0035DDC2:
    if (*(unsigned __int64 *)(v_r14) + 832 == 0) goto loc_0035CAD8;
    result = (unsigned int)((v_stack_m1A8 + *(unsigned __int64 *)(v_r14) + 832 * 1 + 15) >> (4));
    a1 = (unsigned int)((*(unsigned __int8 *)(result + 0 * 1 + 68480)) + (-33));
    a1 = (a1) + 1;
    a1 = (a1) << (6);
    a1 = (a1) + (*(unsigned __int64 *)(v_r14) + 832);
    if ((*(unsigned __int16 *)(a1)) >= ((unsigned __int16)(*(unsigned __int16 *)(a1 + 16)))) goto loc_0035DE0D;
    result = ExpInterlockedPushEntrySList(a1, *(unsigned __int64 *)(v_stack_m1A8 + *(unsigned __int64 *)(v_r14) + 832 * 1), v_stack_m100, (unsigned int)((unsigned int)(v_r14)));
loc_0035DE00:
    if (1 == 0) goto loc_0035CAD8;
    goto loc_0035CB63;
loc_0035DE0D:
    goto loc_0035DE00;
loc_0035DE15:
    if (((unsigned int)(a1)) <= ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14) + 832 + 48)))) goto loc_0035C44F;
    result = RtlpHpLfhSubsegmentPrefetch(v_stack_m1A8 + *(unsigned __int64 *)(v_r14) + 832 * 1 + 832, *(unsigned __int64 *)(v_r14) + 832, 0, (unsigned int)((unsigned int)(v_r14)));
    goto loc_0035C44F;
loc_0035DE3C:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12255254))) != 0) goto loc_0035D1BA;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(v_rip + 12177056, v_stack_p0, 0, (unsigned int)((unsigned int)(v_r14)));
    goto loc_0035D1CC;
loc_0035DE62:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(result), v_stack_p0, 0, (unsigned int)((unsigned int)(v_r14)));
    goto loc_0035DAEF;
loc_0035DE7B:
    if (((unsigned int)(v_rip + 12177034)) <= ((unsigned int)(*(unsigned __int16 *)(v_stack_m238 + 48)))) goto loc_0035C76D;
    result = RtlpHpLfhSubsegmentPrefetch(*(unsigned __int64 *)(v_r14) + 832, v_stack_m238, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r14)));
    goto loc_0035C76D;
loc_0035DEA3:
    if (*(unsigned __int64 *)(result - 40) != 0) goto loc_0035E480;
    if (!sign_flag) goto loc_0035E9F6;
    a2 = 0;
    v_stack_m248 = 0;
    result = KeBugCheckEx(a2 + 24, a2, result, *(unsigned __int64 *)(result - 40) + 4);
loc_0035DED0:
    if (0 != (*(unsigned __int64 *)(v_r14) + 832)) goto loc_0035E6AF;
    v_stack_m248 = *(unsigned __int64 *)(result - 40) + 4;
    result = KeBugCheckEx(33, result, *(unsigned __int64 *)(v_r14) + 832, v_stack_m208);
loc_0035DEF4:
    result = (unsigned int)((*(unsigned __int64 *)(v_r14) + 832) & (448));
    if (result != 256) goto loc_0035E23A;
    a2 = 1;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14) + 832)) & (16)) != 0) { a2 = (unsigned int)((unsigned int)(0x80000001ULL)); }
loc_0035DF19:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a2))) | (32));
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14) + 832)) & (4)) == 0) { a1 = (unsigned int)(a2); }
    a3 = (unsigned int)((unsigned int)(a1));
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14) + 832)) & (2)) != 0) { a3 = (unsigned int)(a1); }
    if ((((unsigned int)(0x80000001ULL)) & (*(unsigned __int64 *)(v_r14) + 832)) == 0) goto loc_0035DF97;
    a1 = (unsigned int)(((unsigned int)(a3)) | (4));
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14) + 832)) & (8)) == 0) { a1 = a3; }
    result = (unsigned int)((*(unsigned __int64 *)(v_r14) + 832) & (512));
    a2 = (unsigned int)((unsigned int)(a1));
    if (result == 0) { a2 = (unsigned int)(a1); }
    result = (unsigned int)((*(unsigned __int64 *)(v_r14) + 832) & (0x400ULL));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a2))) | (64));
    if (result == 0) { a1 = (unsigned int)(a2); }
    result = (unsigned int)((*(unsigned __int64 *)(v_r14) + 832) & (32));
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14) + 832)) & (1)) == 0) goto loc_0035E24E;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (8));
    if (result != 0) { a3 = (unsigned int)(a1); }
loc_0035DF97:
    *(unsigned int *)(0 + 4) = 0;
    *(unsigned __int8 *)(0) = 0;
    result = (v_stack_m1F8) >> (4);
    *(unsigned __int8 *)(0 + 2) = (unsigned __int8)(result);
    result = (unsigned __int8)(((unsigned __int8)(a3)) | (8));
    a2 = (unsigned __int8)(result);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r14) + 832)) & (1)) == 0) { a2 = (unsigned int)((unsigned __int8)(a3)); }
    result = 0;
    a2 = (unsigned __int8)((a2) & (109));
    v_stack_m1D0 = 0;
    a2 = (unsigned __int8)((a2) | (2));
    v_stack_m22E = 0;
    *(unsigned __int8 *)(0 + 3) = (unsigned __int8)(a2);
    v_r14 = (unsigned int)((*(unsigned __int64 *)(v_r14) + 832) & (973));
    v_stack_mD8 = 0;
    v_stack_m20E = 0;
    v_stack_p10 = v_stack_m1F8;
    v_stack_mE8 = v_xmm0;
    if (0 == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13005146))))) {
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13011705)))) & (65)) != 0) goto loc_0035E4C3;
loc_0035E013:
    v_r14 = (v_r14) & (-5);
    v_stack_m1E0 = *(unsigned __int64 *)(v_rip + 12193059);
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))))) * (0);
    v_stack_m1A0 = *(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424);
    v_rdi = (a1) >> (32);
    v_rdi = (unsigned int)((v_rdi) ^ ((unsigned int)(a1)));
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)(*(unsigned __int64 *)(v_rip + 12193074))));
    v_stack_p8 = (unsigned int)(v_rdi);
loc_0035E064:
    a1 = ((unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4) + ((unsigned int)((unsigned int)(v_rdi)) + (unsigned int)((unsigned int)(v_rdi)) * 4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8)))) != 0) goto loc_0035E114;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8)))) < 0) goto loc_0035E37A;
loc_0035E099:
    v_stack_p8 = 1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8 + 72)) == 0) goto loc_0035E144;
loc_0035E0C4:
loc_0035E0C8:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8 + (int)(1) * 8 + 56))) & (1)) != 0) goto loc_0035E144;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8 + (int)(1) * 8 + 56)) >= v_stack_p10) goto loc_0035E144;
    result = ExpTrackTableGetMoreLimit(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8 + 72), v_stack_p10, 1, v_stack_p10);
    if (result == 0) goto loc_0035F48D;
    if (result != 1) goto loc_0035E428;
    if (result == 1) goto loc_0035E144;
    goto loc_0035E0C4;
loc_0035E114:
    if ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8 + (int)(1) * 8 + 56)) == 0) goto loc_0035E260;
loc_0035E11C:
    result = (unsigned int)((*(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8 + 8 + 1) & ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8 + (int)(1) * 8 + 56))));
    if (((unsigned int)(result)) != ((unsigned int)(v_stack_p10))) goto loc_0035E064;
    result = ExpInsertPoolTrackerExpansion((unsigned int)((unsigned int)(v_stack_p10)), v_stack_p10, *(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8 + (int)(1) * 8, v_stack_p10);
loc_0035E144:
    v_r10 = 0;
loc_0035E14A:
    if (((v_stack_m1F0) & (8)) == 0) goto loc_0035E1BD;
    a1 = (unsigned int)(((unsigned int)(0xFFFFFFF0ULL)) - (0));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 13011741))) - 1);
    a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    if (condition_is_equal) goto loc_0035E1BD;
    a2 = ((unsigned int)((unsigned int)(a1))) + (0);
    a1 = (a2) - (0);
    a1 = (a1) >> (4);
    *(unsigned __int8 *)(a2) = (unsigned __int8)(a1);
    result = (unsigned __int8)((*(unsigned __int8 *)(0 + 2)) - ((unsigned __int8)(a1)));
    *(unsigned __int8 *)(a2 + 2) = (unsigned __int8)(result);
    *(unsigned __int8 *)(a2 + 1) = (unsigned __int8)(*(unsigned __int8 *)(0 + 1));
    result = (unsigned __int8)((*(unsigned __int8 *)(0 + 3)) | (4));
    *(unsigned __int8 *)(a2 + 3) = (unsigned __int8)(result);
    *(unsigned int *)(a2 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 4)));
    result = (unsigned __int16)((*(unsigned __int16 *)(a2)) & (255));
    if (((unsigned __int16)(result)) >= = 1) {
        result = a2;
        result = (result) ^ (*(unsigned __int64 *)(v_rip + 13013106));
        *(unsigned __int64 *)(0 + 16) = result;
    }
loc_0035E1BD:
    result = (a2 + 16) - (0);
    v_stack_p10 = a2 + 16;
    result = (unsigned int)((result) & (7));
    a1 = (a2 + 16) - (result);
    a3 = (a1) - (0);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 13044388)) != 0) goto loc_0035E3C4;
loc_0035E1FE:
    a4 = (a2 + 16) & (-8);
    v_r13 = (v_r13) - (a4);
    v_rsi = (v_stack_m1F8) - (a4);
    v_r13 = (v_r13) + (a2 + 16);
    v_rsi = (v_rsi) + (0);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 13044388)) == 0) goto loc_0035BBCD;
    if (a4 >= (*(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8 + (int)(1) * 8)) goto loc_0035F358;
    v_stack_m248 = 0;
    result = KeBugCheckEx(497, 2, 1, a4);
loc_0035E23A:
    result = (result) - (64);
    if (condition_is_not_equal) goto loc_0035E369;
    goto loc_0035DF19;
loc_0035E24E:
    if (result == 0) goto loc_0035DF97;
    a3 = (unsigned int)((1) | (16));
    goto loc_0035DF97;
loc_0035E260:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12192505) + 497 * 8))) == 0) goto loc_0035E291;
    *(unsigned int *)(1) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12192505) + 497 * 8)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12192486) + 497 * 8 + 72) == 0) goto loc_0035E064;
    *(unsigned __int64 *)(1 + 72) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12192486) + 497 * 8 + 72);
    goto loc_0035E064;
loc_0035E291:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12192486) + 497 * 8 + 72)) == (v_r10 - 1)) goto loc_0035E11C;
    v_stack_mE8 = 0;
    v_stack_mE0 = v_rip + 12175963;
    v_stack_m218 = 2;
    if ((*(unsigned int *)(v_rip + 13011535)) != 0) goto loc_0035E3AB;
loc_0035E2D7:
    v_stack_mD8 = 2;
    if (((*(unsigned __int8 *)(v_rip + 13010984)) & (33)) != 0) goto loc_0035E389;
loc_0035E2EA:
    if (v_stack_mE8 != 0) goto loc_0035E3E8;
loc_0035E301:
    a1 = (0 + 0 * 4) << (4);
    result = (*(unsigned __int64 *)(v_rip + 12192338)) + (a1);
    v_stack_m218 = result;
    if ((*(unsigned int *)(result)) == 0) {
        a1 = 0;
        result = ExpPlFindLimitEntry(a1, v_stack_mE8, a3, a4);
        a1 = v_stack_m218;
        *(unsigned __int64 *)(a1 + 72) = result;
        *(unsigned __int64 *)(1 + 72) = result;
        result = 0;
        a1 = result + result * 4;
        result = *(unsigned __int64 *)(v_rip + 12192288);
        a1 = (a1) + (a1);
        *(unsigned int *)(result + a1 * 8) = 0;
        *(unsigned int *)(1) = 0;
    }
    result = KeReleaseInStackQueuedSpinLock(v_stack_mE8, v_stack_mE8, a3, a4);
    goto loc_0035E064;
loc_0035E369:
    if (result != 64) goto loc_0035D91E;
    a2 = 0;
    goto loc_0035DF19;
loc_0035E37A:
    a1 = 0;
    goto loc_0035E099;
loc_0035E389:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12253897))) != 0) goto loc_0035E2EA;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_mE8, 0, v_stack_m1A0, (unsigned int)(v_stack_p8));
    goto loc_0035E301;
loc_0035E3AB:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(result), 0, v_stack_m1A0, (unsigned int)(v_stack_p8));
    goto loc_0035E2D7;
loc_0035E3C4:
    if (0 >= (*(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8 + (int)(1) * 8)) goto loc_0035F32E;
    v_stack_m248 = v_stack_m1E0;
    result = KeBugCheckEx(497, 2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12192505) + 497 * 8)), 0);
loc_0035E3E8:
    result = KxWaitForLockOwnerShip(v_stack_mE8, 2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12192505) + 497 * 8)), 0);
    goto loc_0035E301;
loc_0035E3F9:
    if ((a2 + 16) >= 2) goto loc_0035F379;
    v_stack_m248 = 1 + 32;
    result = KeBugCheckEx(497, 2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12192505) + 497 * 8)), a2 + 16);
loc_0035E41A:
    result = KxWaitForLockOwnerShip(v_stack_m100, 2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12192505) + 497 * 8)), a2 + 16);
    goto loc_0035DB13;
loc_0035E428:
    goto loc_0035E0C8;
loc_0035E446:
    v_stack_m144 = (unsigned int)(result);
    result = (unsigned int)((result) - ((unsigned int)((unsigned int)(v_stack_p8))));
    result = (unsigned int)((result) + 1);
    if (((unsigned int)(v_rsi)) < ((unsigned int)(result))) { result = (unsigned int)(v_rsi); }
    a4 = (unsigned int)((v_stack_p10) * ((unsigned int)(result)));
    a4 = (unsigned int)((a4) >> (8));
    a4 = (unsigned int)((a4) + ((unsigned int)((unsigned int)(v_stack_p8))));
    v_stack_p10 = a4;
    v_r10 = (unsigned int)((v_stack_m1E0) + (a4));
    goto loc_0035C3CD;
loc_0035E480:
    v_stack_m248 = (unsigned int)(a4);
    result = (1 + 32 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(1 + 32 - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 13011361));
    result = KeBugCheckEx(3 + 21, *(unsigned __int64 *)(v_rip - 3531957 + a2 * 8 + 16545792), 1 + 32, 3);
loc_0035E4C3:
    a2 = 0;
    v_stack_m248 = v_stack_m20E;
    result = ExpPoolFlagsToPoolType(*(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8 + (int)(1) * 8, a2, v_stack_m1D0, v_stack_m22E);
    if (sign_flag) goto loc_0035E013;
    if (v_stack_m22E != 0) {
        a2 = (unsigned int)(((unsigned int)(v_stack_m1D0)) | (8));
        v_stack_m1D0 = (unsigned int)(a2);
    }
    v_stack_m248 = v_stack_p10;
    result = EtwTracePool((unsigned int)(0xE20ULL), a2, (unsigned int)((unsigned int)(*(unsigned __int64 *)(1 + 32))), v_rsi + 16);
    goto loc_0035E013;
loc_0035E51A:
    v_stack_m154 = (unsigned int)(result);
    result = (unsigned int)((result) - ((unsigned int)((unsigned int)(0xE20ULL))));
    result = (unsigned int)((result) + 1);
    if (((unsigned int)(v_r10)) < ((unsigned int)(result))) { result = (unsigned int)(v_r10); }
    a4 = (unsigned int)((v_rsi + 16) * ((unsigned int)(result)));
    a4 = (unsigned int)((a4) >> (8));
    a4 = (unsigned int)((a4) + ((unsigned int)((unsigned int)(0xE20ULL))));
    v_stack_p10 = a4;
    v_r10 = (unsigned int)((v_r10) + (a4));
    goto loc_0035C6EE;
loc_0035E556:
    result = (unsigned int)((v_rsi + 15) >> (4));
    v_stack_m1F8 = *(unsigned __int16 *)(v_r10 + *(unsigned __int8 *)(result + v_r10 * 1 + 68480) * 2 + 115648);
    v_stack_p8 = (unsigned int)(*(unsigned __int8 *)(result + v_r10 * 1 + 68480) - 33);
    v_stack_m218 = *(unsigned __int64 *)(1 + 56);
    if (*(unsigned __int64 *)(1 + 56) == 0) goto loc_0035E5F1;
    result = (*(unsigned __int8 *)(result + v_r10 * 1 + 68480) - 33) + 1;
    result = (result) << (6);
    result = (result) + (*(unsigned __int64 *)(1 + 56));
    v_stack_p10 = result;
    if ((*(unsigned __int16 *)(result)) <= 0) goto loc_0035E60A;
    result = ExpInterlockedPopEntrySList(result, *(unsigned __int8 *)(result + v_r10 * 1 + 68480), (unsigned int)((unsigned int)(*(unsigned __int64 *)(1 + 32))), a4);
    if (result == 0) goto loc_0035E600;
loc_0035E5B4:
    if ((((unsigned __int8)(v_stack_m1F0)) & (2)) != 0) goto loc_0035E5DB;
    if (result == 0) goto loc_0035E5E4;
    a2 = (v_stack_m1F8) + (-16);
    result = RtlHeapZero(result + 16, a2, (unsigned int)((unsigned int)(*(unsigned __int64 *)(1 + 32))), a4);
loc_0035E5DB:
    if (result != 0) goto loc_0035D905;
loc_0035E5E4:
loc_0035E5F1:
    v_stack_m228 = v_stack_m1F8;
    goto loc_0035C1B3;
loc_0035E600:
    a4 = 0;
loc_0035E60A:
    v_stack_m170 = 0;
    v_stack_m118 = 0;
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_p10))) < ((unsigned int)(*(unsigned __int16 *)(v_stack_p10 + 16)))) goto loc_0035F0CE;
loc_0035E62C:
    goto loc_0035E5B4;
loc_0035E631:
    a1 = (((0) & (192)) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) {
        a2 = 1;
        a1 = *(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8 + (int)(1) * 8;
        result = ExpCheckForLookaside(a1, a2, *(unsigned __int16 *)(v_stack_p10 + 16), a4);
    }
    result = (unsigned int)(*(unsigned int *)(v_rip + 13010300));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13010300)))) & (1)) != 0) {
        a2 = 1;
        a1 = *(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8 + (int)(1) * 8;
        result = KeCheckForTimer(a1, a2, *(unsigned __int16 *)(v_stack_p10 + 16), a4);
    }
    result = FREE_CHECK_ERESOURCE(*(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8 + (int)(1) * 8, 1, *(unsigned __int16 *)(v_stack_p10 + 16), a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13010268)))) & (2)) == 0) goto loc_0035C8DC;
    result = ExpCheckForWorker(*(unsigned __int64 *)(v_rip - 3530806 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8 + (int)(1) * 8, 1, *(unsigned __int16 *)(v_stack_p10 + 16), a4);
    goto loc_0035C8DC;
loc_0035E68C:
    if (1 != 0) {
        v_r13 = 0;
    }
    v_stack_m248 = 1 + 32;
    result = KeBugCheckEx(194, 13, result, (unsigned int)((unsigned int)(v_r13)));
loc_0035E6AF:
    goto loc_0035D764;
loc_0035E6C2:
    a2 = (unsigned int)((0) & (16));
    v_stack_m248 = v_stack_m20C;
    result = ExpPoolFlagsToPoolType(0, a2, v_stack_m1C4, v_stack_m22C);
    if (sign_flag) goto loc_0035C91D;
    if (v_stack_m22C != 0) {
        a2 = (unsigned int)(((unsigned int)(v_stack_m1C4)) | (8));
        v_stack_m1C4 = (unsigned int)(a2);
    }
    v_stack_m248 = *(unsigned __int64 *)(v_rip - 3532267 + v_stack_m1F0 * 1);
    result = EtwTracePool((unsigned int)(0xE22ULL), a2, (unsigned int)((unsigned int)(*(unsigned __int64 *)(1 + 32))), 1 + 32);
    goto loc_0035C91D;
loc_0035E714:
    if (((*(unsigned __int8 *)((unsigned int)(0xE22ULL) + (int)((unsigned int)(1 + 32)) * 8 + 56)) & (1)) != 0) goto loc_0035CA81;
    v_r10 = (*(unsigned __int64 *)(v_rip - 3532267 + v_stack_m1F0 * 1) * 4 + 63) & (-64);
    if (v_r10 == 64) { v_r10 = 128; }
loc_0035E743:
    if (a2 >= (*(unsigned __int64 *)((unsigned int)(0xE22ULL) + (int)((unsigned int)(1 + 32)) * 8 + 56))) goto loc_0035CA81;
    if ((v_r10 + a2 * 1) >= (*(unsigned __int64 *)((unsigned int)(0xE22ULL) + (int)((unsigned int)(1 + 32)) * 8 + 56))) goto loc_0035CA81;
    if ((v_r10 + a2 * 1) == (*(unsigned __int64 *)((unsigned int)(0xE22ULL) + (int)((unsigned int)(1 + 32)) * 8 + 56))) goto loc_0035E892;
    goto loc_0035E743;
loc_0035E76A:
    goto loc_0035CEF9;
loc_0035E775:
    goto loc_0035D50F;
loc_0035E793:
    result = ExIsSpecialPoolAddress(*(unsigned __int64 *)((unsigned int)(0xE22ULL) + (int)((unsigned int)(1 + 32)) * 8 + 56), (unsigned int)((unsigned int)(v_stack_m1F0)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(1 + 32))), v_stack_p10);
    if ((unsigned int)(result) == 0) goto loc_0035CF7F;
    goto loc_0035C800;
loc_0035E7A8:
    result = RtlpHpLargeFree(v_r10 + a2 * 1, v_rip - 3532267 + v_stack_m1F0 * 1, (unsigned int)((unsigned int)(*(unsigned __int64 *)(1 + 32))), v_stack_p10);
    goto loc_0035CB63;
loc_0035E7B8:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rip - 3532267 + v_stack_m1F0 * 1))) & (16));
    v_stack_m248 = v_stack_m20F;
    result = ExpPoolFlagsToPoolType(v_rip - 3532267 + v_stack_m1F0 * 1, a2, v_stack_m1D4, v_stack_m22F);
    if (sign_flag) goto loc_0035D455;
    if (v_stack_m22F != ((unsigned __int8)(*(unsigned __int64 *)(v_r10 + a2 * 1)))) {
        a2 = (unsigned int)(((unsigned int)(v_stack_m1D4)) | (8));
        v_stack_m1D4 = (unsigned int)(a2);
    }
    v_stack_m248 = v_stack_p10;
    result = EtwTracePool((unsigned int)(0xE20ULL), a2, (unsigned int)((unsigned int)(v_r10 + a2 * 1)), 1 + 32);
    goto loc_0035D455;
loc_0035E812:
    if (*(unsigned __int64 *)(v_r10 + a2 * 1) == 0) goto loc_0035BAEC;
    result = ExCheckSingleFilter((unsigned int)((unsigned int)(v_r10 + a2 * 1)), (unsigned int)((unsigned int)(1 + 32)), (unsigned int)((unsigned int)(v_r10 + a2 * 1)), 1 + 32);
    if ((unsigned int)(result) != 0) goto loc_0035BF20;
    if ((1 + 32) < (*(unsigned __int64 *)(v_r10 + a2 * 1) + 16)) goto loc_0035BAEC;
    if ((1 + 32) >= (*(unsigned __int64 *)(v_r10 + a2 * 1) + 32)) goto loc_0035BAEC;
    goto loc_0035BF20;
loc_0035E84C:
    if ((*(unsigned __int8 *)(v_r10 + a2 * 1 + 22)) == 1) goto loc_0035BD54;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_r10 + a2 * 1)))) >> (6));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_r10 + a2 * 1)))) & (63));
    result = (*(unsigned __int64 *)(v_r10 + a2 * 1 + result * 8 + 64)) & (-2);
    a3 = ~(-2);
    *(unsigned __int64 *)(v_r10 + a2 * 1 + result * 8 + 64) = result;
    if (((*(unsigned __int64 *)(v_r10 + a2 * 1 + result * 8 + 64)) & (a3)) == 0) goto loc_0035C0D2;
    goto loc_0035BE87;
loc_0035E892:
    result = (result) - (v_r10 + a2 * 1);
    a2 = -(result);
    if (!sign_flag) { a2 = result; }
    result = ExpTrackTableReturnLimit(*(unsigned __int64 *)(v_r10 + a2 * 1 + result * 8 + 72), a2, (unsigned int)((unsigned int)(1 + 32)), 1 + 32);
    goto loc_0035CA81;
loc_0035E8B3:
    result = RtlpHpLfhThreadDataInitializeSet(v_rip - 3532267 + v_stack_m1F0 * 1, a2, (unsigned int)((unsigned int)(1 + 32)), 1 + 32);
    goto loc_0035BD4A;
loc_0035E8C0:
    result = (result) - (v_r10 + a2 * 1);
    a2 = -(result);
    if (!sign_flag) { a2 = result; }
    result = ExpTrackTableReturnLimit(*(unsigned __int64 *)(1 + 32 + 72), a2, (unsigned int)((unsigned int)(1 + 32)), 1 + 32);
    goto loc_0035CA8A;
loc_0035E8DE:
    if ((*(unsigned __int8 *)(1 + 32 + 22)) == 1) goto loc_0035CCF7;
    result = (v_r10 + a2 * 1) >> (6);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r10 + a2 * 1))) & (63));
    result = (*(unsigned __int64 *)(1 + 32 + result * 8 + 64)) & (-2);
    a4 = ~(-2);
    *(unsigned __int64 *)(1 + 32 + result * 8 + 64) = result;
    if (((*(unsigned __int64 *)(1 + 32 + result * 8 + 64)) & (a4)) == 0) goto loc_0035D36D;
    goto loc_0035CB63;
loc_0035E929:
    if ((*(unsigned __int64 *)(1 + 32 + result * 8 + 64)) > ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 3532267 + v_stack_m1F0 * 1) + 528)))) goto loc_0035E9BA;
    result = RtlpHpAllocateHeapBackend(*(unsigned __int64 *)(v_rip - 3532267 + v_stack_m1F0 * 1), *(unsigned __int64 *)((unsigned int)(0xE22ULL) + (int)((unsigned int)(1 + 32)) * 8 + 56), *(unsigned __int64 *)(1 + 32 + result * 8 + 64), a4);
    goto loc_0035D8FB;
loc_0035E94B:
    result = RtlpHpLfhThreadDataInitializeSet(result, *(unsigned __int64 *)((unsigned int)(0xE22ULL) + (int)((unsigned int)(1 + 32)) * 8 + 56), *(unsigned __int64 *)(1 + 32 + result * 8 + 64), a4);
    goto loc_0035CCED;
loc_0035E958:
    if ((1 + 32) > ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 3532267 + v_stack_m1F0 * 1) + 528)))) goto loc_0035E9C4;
    result = RtlpHpAllocateHeapBackend(*(unsigned __int64 *)(v_rip - 3532267 + v_stack_m1F0 * 1), result, 1 + 32, a4);
    goto loc_0035C128;
loc_0035E977:
    v_stack_m248 = *(unsigned __int64 *)(v_rip - 3532267 + v_stack_m1F0 * 1);
    result = (1 + 32 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(1 + 32 - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 13010090));
    result = KeBugCheckEx(3 + 21, *(unsigned __int64 *)(v_rip - 3533228 + a2 * 8 + 16545792), 1 + 32, 3);
loc_0035E9BA:
    result = RtlpHpLargeAlloc(3 + 21, *(unsigned __int64 *)(v_rip - 3533228 + a2 * 8 + 16545792), 1 + 32, 3);
    goto loc_0035D969;
loc_0035E9C4:
    result = RtlpHpLargeAlloc(3 + 21, *(unsigned __int64 *)(v_rip - 3533228 + a2 * 8 + 16545792), 1 + 32, 3);
    goto loc_0035C128;
loc_0035E9CE:
    result = RtlpHpLfhThreadDataInitializeSet((unsigned int)(0xE22ULL) + (int)((unsigned int)(1 + 32)) * 8, *(unsigned __int64 *)(v_rip - 3533228 + a2 * 8 + 16545792), 1 + 32, 3);
    goto loc_0035C24A;
loc_0035E9E2:
    result = RtlpHpLfhThreadDataInitializeSet(*(unsigned __int64 *)(v_rip - 3532267 + v_stack_m1F0 * 1) + 832, *(unsigned __int64 *)(v_rip - 3533228 + a2 * 8 + 16545792), 1 + 32, 3);
    goto loc_0035C57D;
loc_0035E9F6:
    result = ObpDeferObjectDeletion(1 + 32 - 48, *(unsigned __int64 *)(v_rip - 3533228 + a2 * 8 + 16545792), 1 + 32, 3);
    goto loc_0035C800;
loc_0035EA09:
    result = ObpDeferObjectDeletion(1 + 32 - 48, *(unsigned __int64 *)(v_rip - 3533228 + a2 * 8 + 16545792), 1 + 32, 3);
    goto loc_0035D1F8;
loc_0035EA17:
    goto loc_0035C474;
loc_0035EA21:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + a2 * 1))))) >> (16));
    if (!(condition_is_above_or_equal)) {
        a3 = v_r10 + a2 * 1 + 24;
    }
    if (a3 < v_stack_m228) goto loc_0035EB31;
    result = (v_stack_m228 + 4095) & (0xFFFFFFFFFFFFF000ULL);
loc_0035EA51:
    if ((1 + 32 + v_stack_m228 * 1) < result) goto loc_0035EB54;
    if (((*(unsigned int *)(v_r10 + a2 * 1)) & (0x4000ULL)) != 0) {
        a3 = result;
        a4 = 1;
        a3 = (a3) >> (8);
        a2 = 1 + 32;
        a3 = (unsigned int)((a3) & (1));
        a1 = v_stack_m228;
        result = ViFreeTrackedPool(a1, a2, a3, a4);
    }
    v_r14 = (1 + 32 + 15) & (-16);
    v_stack_m1CC = (unsigned int)(v_stack_m1F0);
    v_stack_m22D = 0;
    v_stack_m20D = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + a2 * 1 + 4)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13002440))))) {
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13008988)))) & (65)) != 0) goto loc_0035EBC2;
loc_0035EAB0:
    v_rsi = (result) & (-5);
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))))) * ((unsigned int)(*(unsigned int *)(v_r10 + a2 * 1 + 4)));
    a2 = (a1) >> (32);
    a2 = (unsigned int)((a2) ^ ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) & ((unsigned int)(*(unsigned __int64 *)(v_rip + 12190357))));
loc_0035EAEA:
    a1 = ((unsigned int)((unsigned int)(a2)) + (unsigned int)((unsigned int)(a2)) * 4) + ((unsigned int)((unsigned int)(a2)) + (unsigned int)((unsigned int)(a2)) * 4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 3533516 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + a2 * 1 + 4))))) goto loc_0035EB77;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 3533516 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8))) == 0) goto loc_0035EB8F;
loc_0035EB07:
    result = (unsigned int)((a2 + 1) & ((unsigned int)(*(unsigned __int64 *)(v_rip + 12190357))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_0035EAEA;
    result = ExpRemovePoolTrackerExpansion((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + a2 * 1 + 4)))), v_r14, v_rsi, *(unsigned __int64 *)(v_rip - 3533516 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8);
loc_0035EB21:
    result = RtlpHpFreeHeap(*(unsigned __int64 *)(v_rip - 3532267 + v_stack_m1F0 * 1), v_r10 + a2 * 1, v_rsi, *(unsigned __int64 *)(v_rip - 3533516 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))) * 8 + 15707424) + a1 * 8);
    goto loc_0035CB63;
loc_0035EB31:
    if ((*(unsigned __int8 *)(v_rsi)) == ((unsigned __int8)(*(unsigned __int64 *)(v_rip - 3532267 + v_stack_m1F0 * 1)))) goto loc_0035F498;
    v_stack_m248 = 35;
    result = KeBugCheckEx(193, v_stack_m228, v_rsi, (unsigned int)(*(unsigned int *)(v_r10 + a2 * 1)));
loc_0035EB54:
    if ((*(unsigned __int8 *)(v_rsi)) == 193) goto loc_0035F4A0;
    v_stack_m248 = 36;
    result = KeBugCheckEx(193, v_stack_m228, v_rsi, (unsigned int)(*(unsigned int *)(v_r10 + a2 * 1)));
loc_0035EB77:
    v_rsi = (v_rsi) >> (8);
    v_rsi = (unsigned int)(~(v_rsi));
    v_rsi = (unsigned int)((v_rsi) & (1));
    result = ExpPoolTrackerReturnLimit((unsigned int)((unsigned int)(v_rsi)), v_r14, (unsigned int)(*(unsigned int *)(v_r10 + a2 * 1)), (unsigned int)(*(unsigned int *)(v_r10 + a2 * 1)));
    goto loc_0035EB21;
loc_0035EB8F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12190154) + (unsigned int)((unsigned int)(v_rsi)) * 8))) == 0) goto loc_0035EB07;
    *(unsigned int *)((unsigned int)(*(unsigned int *)(v_r10 + a2 * 1))) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12190154) + (unsigned int)((unsigned int)(v_rsi)) * 8)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12190133) + (unsigned int)((unsigned int)(v_rsi)) * 8 + 72) == 0) goto loc_0035EAEA;
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_r10 + a2 * 1)) + 72) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12190133) + (unsigned int)((unsigned int)(v_rsi)) * 8 + 72);
    goto loc_0035EAEA;
loc_0035EBC2:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (16));
    v_stack_m248 = v_stack_m20D;
    result = ExpPoolFlagsToPoolType(v_rsi, a2, v_stack_m1CC, v_stack_m22D);
    if (sign_flag) goto loc_0035EAB0;
    if (v_stack_m22D != 0) {
        a2 = (unsigned int)(((unsigned int)(v_stack_m1CC)) | (8));
        v_stack_m1CC = (unsigned int)(a2);
    }
    v_stack_m248 = v_r14;
    result = EtwTracePool((unsigned int)(0xE22ULL), a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + a2 * 1 + 4)))), v_stack_m228);
    goto loc_0035EAB0;
loc_0035EC14:
    result = MmDeterminePoolType(v_stack_m228, a2, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + a2 * 1 + 4)))), v_stack_m228);
    v_rbx = (v_stack_m228) & (0xFFFFFFFFFFFFF000ULL);
    if ((*(unsigned __int8 *)(v_rip + 13041713)) != 0) goto loc_0035ECCF;
loc_0035EC3D:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m228))) & (0xFFFULL));
    v_stack_m248 = v_stack_m228;
    a1 = (unsigned int)(((unsigned int)(0x1000ULL)) - ((unsigned int)(result)));
    result = ExpFreePoolChecks(v_stack_m228, (unsigned int)(*(unsigned int *)(v_rbx + 4)), (unsigned int)((unsigned int)(a1)), 128);
    result = (condition_is_above_or_equal) ? 1 : 0;
    result = (unsigned __int8)((result) + 1);
    if (2 >= = ((unsigned __int8)(result))) {
        a2 = 2;
        a4 = v_stack_m228;
        a1 = 193;
        v_stack_m248 = 49;
        a3 = a1 + 63;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_rdi = (unsigned int)((*(unsigned __int16 *)(v_rbx)) & (0x1FFFULL));
    result = (v_rdi + 15) & (-16);
    if (result == ((unsigned int)((unsigned int)(a1)))) goto loc_0035EA21;
    v_stack_m248 = 33;
    result = KeBugCheckEx(193, v_stack_m228, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)(a1)));
loc_0035ECCF:
    if (v_rbx >= result) goto loc_0035F1D6;
    v_stack_m248 = v_stack_m1F0;
    result = KeBugCheckEx(497, 2, 2 - 1, v_rbx);
loc_0035ECFE:
    result = ExGetHeapFromType(v_rdi, (unsigned int)(0x80000000ULL), 1, v_rbx);
    v_stack_m218 = result;
    v_stack_m248 = 4;
    result = RtlpHpSegAlloc(result + 320, (unsigned int)((unsigned int)(a2)), (unsigned int)((unsigned int)(a2)), (unsigned int)((unsigned int)(a2)));
    v_stack_m140 = result;
    if (result == 0) goto loc_0035F43B;
    a1 = (result) + (16);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)(result)))) | (1));
    result = memset(a1, a2, (unsigned int)(0xFF0ULL), (unsigned int)((unsigned int)(a2)));
    result = (unsigned int)((v_rdi) & (0x400ULL));
    *(unsigned __int64 *)(v_stack_m140 + 8) = v_stack_m1F0;
    a3 = result - 8;
    if (result == 0) { a3 = result; }
    v_rbx = (unsigned __int8)(((unsigned __int8)(result)) | (1));
    *(unsigned int *)(v_stack_m140) = a3;
    *(unsigned __int8 *)(v_stack_m140 + 2) = (unsigned __int8)(v_rbx);
    *(unsigned int *)(v_stack_m140 + 4) = (unsigned int)((unsigned int)(v_stack_p18));
    v_stack_m180 = a3;
    if (result != 0) {
    }
    v_rdi = (v_stack_m140) - (a3);
    v_rdi = (v_rdi) + (0x1000ULL);
    v_rdi = (v_rdi) & (-16);
    if (((v_stack_m1B0) & (2)) == 0) {
        a2 = 0;
        a1 = v_rdi;
        result = memset(a1, a2, a3, (unsigned int)((unsigned int)(a2)));
        a2 = v_stack_p18;
        a1 = v_stack_m140;
        a3 = v_stack_m180;
    }
    result = MmDeterminePoolType(a1, a2, a3, (unsigned int)((unsigned int)(a2)));
    result = 0;
    a4 = (a3 + 15) & (-16);
    v_stack_m98 = 0;
    v_stack_m1D8 = 0;
    v_stack_m230 = 0;
    v_stack_m210 = 0;
    v_stack_m208 = a4;
    v_stack_mA8 = v_xmm0;
    if (((unsigned int)(a2)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13001552))))) {
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13008113)))) & (65)) != 0) goto loc_0035F03E;
loc_0035EE1B:
    v_rbx = (result) & (-5);
    v_stack_m1B8 = *(unsigned __int64 *)(v_rip + 12189479);
    v_stack_m1A0 = *(unsigned __int64 *)(v_rip + 12189448);
    a1 = (a1) * ((unsigned int)((unsigned int)(a2)));
    v_stack_p10 = *(unsigned __int64 *)(v_rip - 3534378 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 15707424);
    v_r10 = (a1) >> (32);
    v_r10 = (unsigned int)((v_r10) ^ ((unsigned int)(a1)));
    v_r10 = (unsigned int)((v_r10) & ((unsigned int)(*(unsigned __int64 *)(v_rip + 12189479))));
    v_stack_m1C0 = v_r10;
    v_stack_p8 = (unsigned int)(v_r10);
loc_0035EE74:
    a3 = ((unsigned int)((unsigned int)(v_r10)) + (unsigned int)((unsigned int)(v_r10)) * 4) << (4);
    v_stack_m1B0 = a3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + *(unsigned __int64 *)(v_rip - 3534378 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 15707424) * 1)))) != ((unsigned int)(a2))) goto loc_0035EF1B;
    v_rbx = (v_rbx) >> (8);
    v_rbx = (unsigned int)(~(v_rbx));
    v_rbx = (unsigned int)((v_rbx) & (1));
    result = ExpPoolTrackerChargeEntry((unsigned int)((unsigned int)(v_rbx)), v_stack_m208, a3 + *(unsigned __int64 *)(v_rip - 3534378 + (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))) * 8 + 15707424) * 1, (unsigned int)((unsigned int)(v_r10)));
    a1 = (v_rdi) & (0xFFFFFFFFFFFFF000ULL);
    result = KasanPoolAllocate(a1, (unsigned int)(0x1000ULL), v_rdi, v_stack_m180);
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_0035EEF8;
loc_0035EED2:
    if (v_rdi == 0) goto loc_0035F036;
    v_stack_p10 = v_rdi;
    v_rdi = 0;
    goto loc_0035BBD2;
loc_0035EEF8:
    result = ExpFreeHeapSpecialPool(v_stack_m218, 0, v_rdi, v_stack_m180);
    a4 = 0;
loc_0035EF11:
    goto loc_0035BAFA;
loc_0035EF1B:
    if ((unsigned int)(result) == 0) goto loc_0035EF6E;
loc_0035EF1F:
    result = (unsigned int)((v_r10 + 1) & (v_stack_m1B8));
    v_stack_m1C0 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) != v_stack_p8) goto loc_0035EE74;
    result = ExpInsertPoolTrackerExpansion((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), v_stack_m208, (unsigned int)(v_stack_p18), a4);
    a1 = (0) & (0xFFFFFFFFFFFFF000ULL);
    result = KasanPoolAllocate(a1, (unsigned int)(0x1000ULL), 0, v_stack_m180);
    goto loc_0035EED2;
loc_0035EF6E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + *(unsigned __int64 *)(v_rip + 12189163) * 1))) == 0) goto loc_0035EFA6;
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + *(unsigned __int64 *)(v_rip + 12189163) * 1)));
    if (*(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_rip + 12189144) * 1 + 72) == 0) goto loc_0035EE74;
    *(unsigned __int64 *)(a1 + 72) = *(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_rip + 12189144) * 1 + 72);
    goto loc_0035EE74;
loc_0035EFA6:
    result = (v_stack_m1A0) - 1;
    if ((*(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_rip + 12189144) * 1 + 72)) == result) goto loc_0035F09C;
    result = KeAcquireInStackQueuedSpinLock(v_rip + 12172604, v_stack_mA8, 0, *(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_rip + 12189144) * 1 + 72));
    result = (*(unsigned __int64 *)(v_rip + 12189072)) + (v_stack_m1B0);
    v_stack_m1E0 = result;
    if ((*(unsigned int *)(result)) == ((unsigned int)(v_stack_m1F0))) {
        a1 = v_stack_p18;
        result = ExpPlFindLimitEntry(a1, v_stack_mA8, 0, *(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_rip + 12189144) * 1 + 72));
        a2 = v_stack_m1B0;
        a1 = v_stack_m1E0;
        a3 = v_stack_p10;
        *(unsigned __int64 *)(a1 + 72) = result;
        a1 = v_stack_p18;
        *(unsigned __int64 *)(a2 + a3 * 1 + 72) = result;
        result = *(unsigned __int64 *)(v_rip + 12189011);
        *(unsigned int *)(a2 + result * 1) = (unsigned int)(a1);
        *(unsigned int *)(a2 + a3 * 1) = (unsigned int)(a1);
    }
    result = KeReleaseInStackQueuedSpinLock(v_stack_mA8, a2, a3, *(unsigned __int64 *)(0 + *(unsigned __int64 *)(v_rip + 12189144) * 1 + 72));
    goto loc_0035EE74;
loc_0035F036:
    a4 = 0;
    goto loc_0035EF11;
loc_0035F03E:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p18)))) & (16));
    v_stack_m248 = v_stack_m210;
    result = ExpPoolFlagsToPoolType((unsigned int)(v_stack_p18), a2, v_stack_m1D8, v_stack_m230);
    if (sign_flag) goto loc_0035F091;
    if (v_stack_m230 != ((unsigned __int8)(v_stack_m1F0))) {
        a2 = (unsigned int)(((unsigned int)(v_stack_m1D8)) | (8));
        v_stack_m1D8 = (unsigned int)(a2);
    }
    v_stack_m248 = v_stack_m208;
    result = EtwTracePool((unsigned int)(0xE20ULL), a2, (unsigned int)(v_stack_p18), v_stack_m140);
loc_0035F091:
    goto loc_0035EE1B;
loc_0035F09C:
    goto loc_0035EF1F;
loc_0035F0A8:
    if (((unsigned __int8)(result)) == 4) goto loc_0035CFAF;
    goto loc_0035CFB5;
loc_0035F0BB:
    if (((unsigned __int8)(result)) == 4) goto loc_0035CE67;
    goto loc_0035CE6D;
loc_0035F0CE:
    a3 = (unsigned int)(((unsigned int)(v_stack_p18)) - ((unsigned int)((unsigned int)(0xE20ULL))));
    a3 = (unsigned int)((a3) >> (1));
    if (condition_is_equal) goto loc_0035E62C;
    a3 = (unsigned int)((a3) + 1);
    if (((unsigned int)(v_stack_p18)) > 0x20000ULL) goto loc_0035E62C;
    v_stack_m240 = v_stack_m118;
    v_stack_m248 = v_stack_m170;
    result = RtlpHpVsContextMultiAlloc((unsigned int)(v_stack_m1FC) + 704, (unsigned int)(v_stack_p18), a3, v_stack_m140);
    if ((unsigned int)(result) == 0) goto loc_0035F143;
    v_stack_m170 = *(unsigned __int64 *)(v_stack_m170);
    result = (unsigned int)((result) + (-1));
    if (condition_is_equal) goto loc_0035E5B4;
    a1 = ((unsigned int)(v_stack_p8)) + 1;
    a1 = (a1) << (6);
    a1 = (a1) + (v_stack_m218);
    result = InterlockedPushListSList(a1, *(unsigned __int64 *)(v_stack_m170), v_stack_m118, (unsigned int)((unsigned int)(result)));
    goto loc_0035E5B4;
loc_0035F143:
    a4 = 0;
    goto loc_0035E62C;
loc_0035F14B:
    if (((256) & (7)) != 0) {
        result = 2;
        v_stack_m248 = 8;
        a3 = (unsigned int)(result);
        a2 = (unsigned int)(result);
        a4 = 256;
        a1 = 497;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = (unsigned int)(v_stack_m1FC) + 256 * 1;
    if (((unsigned int)(v_stack_m1FC) + 256 * 1) < 256) {
        a2 = 2;
        v_stack_m248 = (unsigned int)(v_stack_m1FC);
        a4 = 256;
        a1 = 497;
        a3 = a2 + 1;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_rbx = ((unsigned int)(v_stack_p18)) + (256);
    v_rdi = ((unsigned int)(v_stack_m1FC)) >> (3);
    v_rbx = (v_rbx) >> (3);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 13008162));
    if (v_rdi != 0) goto loc_0035F4A8;
loc_0035F1BF:
    if ((((unsigned __int8)((unsigned int)(v_stack_m1FC))) & (7)) == 0) goto loc_0035CAB6;
    result = (unsigned __int8)(((unsigned __int8)((unsigned int)(v_stack_m1FC))) & (7));
    *(unsigned __int8 *)(v_rbx) = (unsigned __int8)(result);
    goto loc_0035CAB6;
loc_0035F1D6:
    result = v_rbx + 4096;
    if ((v_rbx + 4096) < v_rbx) {
        a2 = 2;
        v_stack_m248 = 0x1000ULL;
        a4 = v_rbx;
        a1 = 497;
        a3 = a2 + 1;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a2 = 0;
    a1 = (a1) + (v_rbx);
    a1 = (a1) >> (3);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 13008054));
    result = memset(a1, a2, 512, a4);
    goto loc_0035EC3D;
loc_0035F22C:
    v_r14 = (v_stack_m1F0) >> (3);
    v_rbx = (unsigned int)((v_stack_m1F0 - 1) & (7));
    result = (unsigned int)((v_stack_m170 - 1) & (7));
    v_rbx = (v_rbx) - (result);
    v_rbx = (v_rbx) - (v_stack_m1F0);
    v_rbx = (v_rbx) + (v_stack_m170);
    v_rsi = (v_stack_m170) + (a4);
    v_rsi = (v_rsi) >> (3);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(v_rip + 13007990));
    if (v_r14 != 0) goto loc_0035F405;
loc_0035F26B:
    v_r13 = v_stack_m1F0;
    if ((((unsigned __int8)(v_stack_m1F0)) & (7)) != 0) {
        v_r13 = (unsigned __int8)((v_stack_m1F0) & (7));
        *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(v_r13);
        v_rsi = (v_rsi) + 1;
    }
    v_rbx = (v_rbx) >> (3);
    if (v_rbx == 0) goto loc_0035BBCD;
    result = memset(v_rsi, 134, v_rbx, a4);
    goto loc_0035BBCD;
loc_0035F29A:
    if (v_rsi < v_rbx) {
        a2 = 2;
        v_stack_m248 = v_rbx;
        a4 = v_rbx;
        a1 = 497;
        a3 = a2 + 1;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a1 = (a1) + (v_rbx);
    result = (unsigned int)((a3 - 1) & (7));
    a3 = (a3) - (result);
    a1 = (a1) >> (3);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 13007867));
    a3 = (a3) + (7);
    a3 = (a3) >> (3);
    if (a3 == 0) goto loc_0035E1FE;
    result = memset(a1, 141, a3, a4);
    v_r10 = 0;
    goto loc_0035E1FE;
loc_0035F308:
    if ((v_rsi + a4 * 1) >= a4) goto loc_0035F22C;
    v_stack_m248 = v_rsi;
    result = KeBugCheckEx(497, 2, 2 + 1, a4);
loc_0035F32E:
    if ((((unsigned __int8)(v_rbx)) & (7)) == 0) goto loc_0035F29A;
    v_stack_m248 = 8;
    result = KeBugCheckEx(497, 2, 2, v_rbx);
loc_0035F358:
    if (v_r13 <= v_rsi) goto loc_0035F308;
    v_stack_m248 = v_rsi;
    result = KeBugCheckEx(497, 2, 2 + 1, v_r13);
loc_0035F379:
    if ((((unsigned __int8)(v_rdi)) & (7)) == 0) goto loc_0035D68A;
    v_stack_m248 = 8;
    result = KeBugCheckEx(497, 2, 2, v_rdi);
loc_0035F3A4:
    result = 497 + v_rdi * 1;
    if ((497 + v_rdi * 1) < v_rdi) {
        a2 = 2;
        v_stack_m248 = 497;
        a1 = 497;
        a3 = a2 + 1;
        result = KeBugCheckEx(a1, a2, a3, v_rdi);
    }
    v_rsi = (v_rsi) + (v_rdi);
    v_rbx = (unsigned int)((v_r13 - 1) & (7));
    v_rsi = (v_rsi) >> (3);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(v_rip + 13007599));
    result = (unsigned int)((a1 - 1) & (7));
    v_rbx = (v_rbx) - (result);
    v_rbx = (v_rbx) - (v_r13);
    v_r14 = (v_r13) >> (3);
    v_rbx = (v_rbx) + (a1);
    if (v_r14 == 0) goto loc_0035F26B;
loc_0035F405:
    a2 = 0;
    result = memset(v_rsi, a2, v_r14, v_rdi);
    v_rsi = (v_rsi) + (v_r14);
    goto loc_0035F26B;
loc_0035F41A:
    if (v_r13 <= v_rsi) goto loc_0035F3A4;
    v_stack_m248 = v_rsi;
    result = KeBugCheckEx(497, 2, 2 + 1, v_r13);
loc_0035F43B:
    a4 = 0;
    goto loc_0035EF11;
loc_0035F446:
    a2 = (*(unsigned __int16 *)(v_stack_m218 + 2)) << (6);
    a2 = (a2) + (v_rdi);
    result = RtlpHpLfhBucketUpdateAffinityMapping(v_rdi, a2, 2 + 1, a4);
    goto loc_0035C7A7;
loc_0035F463:
    v_r15 = 0;
    goto loc_0035D665;
loc_0035F46B:
    goto loc_0035D8E2;
loc_0035F483:
    goto loc_0035D947;
loc_0035F48D:
    v_r10 = 0;
    goto loc_0035E14A;
loc_0035F498:
    a3 = (2 + 1) + 1;
    goto loc_0035EA36;
loc_0035F4A0:
    a3 = (a3) + 1;
    goto loc_0035EA51;
loc_0035F4A8:
    a2 = 0;
    result = memset(v_rbx, a2, 0, a4);
    v_rbx = (v_rbx) + (0);
    goto loc_0035F1BF;
loc_0035F4BD:
    v_rsp = (v_rsp) + (560);
    return v_r13;
}
```

## 5. (Beta) C Style

```c
int64_t ExAllocateHeapPool(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint8_t v_stack_m10E;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m11C;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m144;
    uint32_t v_stack_m148;
    uint32_t v_stack_m14C;
    uint32_t v_stack_m150;
    uint32_t v_stack_m154;
    uint32_t v_stack_m158;
    uint8_t v_stack_m15A;
    uint16_t v_stack_m15C;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m180;
    uint32_t v_stack_m190;
    uint32_t v_stack_m194;
    uint16_t v_stack_m196;
    uint32_t v_stack_m198;
    uint16_t v_stack_m19E;
    uint64_t v_stack_m1A0;
    uint8_t v_stack_m1A4;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint8_t v_stack_m1B4;
    uint64_t v_stack_m1B8;
    uint8_t v_stack_m1BA;
    uint16_t v_stack_m1BC;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1C4;
    uint16_t v_stack_m1C6;
    uint32_t v_stack_m1C8;
    uint32_t v_stack_m1CC;
    uint32_t v_stack_m1D0;
    uint32_t v_stack_m1D4;
    uint32_t v_stack_m1D8;
    uint16_t v_stack_m1DE;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint32_t v_stack_m1FC;
    uint32_t v_stack_m200;
    uint64_t v_stack_m208;
    uint8_t v_stack_m20C;
    uint8_t v_stack_m20D;
    uint8_t v_stack_m20E;
    uint8_t v_stack_m20F;
    uint8_t v_stack_m210;
    uint64_t v_stack_m218;
    uint8_t v_stack_m21A;
    uint16_t v_stack_m21E;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint8_t v_stack_m22C;
    uint8_t v_stack_m22D;
    uint8_t v_stack_m22E;
    uint8_t v_stack_m22F;
    uint8_t v_stack_m230;
    uint8_t v_stack_m232;
    uint16_t v_stack_m236;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p20 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (560);
    Arg4 = 0;
    v_stack_m1FC = 1;
    v_stack_m1F8 = 0;
    local_r12 = (uint32_t)((Arg1) & (2));
    local_r14 = 2;
    if (condition_is_not_equal) { local_r14 = 0; }
    result = (uint32_t)((Arg1) & (0x408ULL));
    local_r11 = (Arg1) & (-9);
    if (result != 0x408ULL) { local_r11 = Arg1; }
    v_stack_m1F0 = local_r11;
    Arg1 = (((local_r11) & (320)) == 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) {
        local_r11 = (local_r11) | (64);
        v_stack_m1F0 = local_r11;
    }
    if (Arg2 > 0xFE0ULL) goto loc_0035BAFA;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC6B145))) != 0) goto loc_0035E812;
loc_0035BAEC:
    if (condition_is_below) goto loc_0035BF20;
    Arg4 = 0;
loc_0035BAFA:
    local_r11 = (uint32_t)((local_r11) & (0xFFFULL));
    v_stack_m1F0 = local_r11;
    local_r13 = 1;
    if (Arg2 != 0) { local_r13 = Arg2; }
    if (((uint32_t)((uint32_t)(Arg4))) != 0x80000000ULL) goto loc_0035C090;
loc_0035BB23:
loc_0035BB3B:
    local_r15 = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xC0) + 0x8A);
    if (((uint32_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xC0) + 0x8A))) >= (*(uint32_t *)(v_rip + 0xB103CE))) {
        local_r15 = 0;
    }
    local_r15 = (local_r15) * ((uint32_t)((uint32_t)(local_r15)));
    local_r15 = (local_r15) + (v_rip + 11600872);
    if ((((uint8_t)(local_r11)) & (16)) != 0) goto loc_0035C087;
    if (condition_is_above_or_equal) goto loc_0035C064;
loc_0035BB75:
loc_0035BB79:
    v_stack_m220 = *(uint64_t *)(local_r15 + 0x2 * 8);
    if (local_r13 <= 0xFE0ULL) goto loc_0035C179;
    local_rsi = (local_r13 + 15) & (-16);
    v_stack_m1F8 = local_rsi;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (0xFFFULL));
    if (((uint32_t)(result)) > 0xFC0ULL) goto loc_0035D86C;
    if (local_rsi >= 0x10000ULL) goto loc_0035D86C;
loc_0035BBB7:
    if (local_rsi >= local_r13) goto loc_0035C0F4;
    v_stack_p10 = 0;
loc_0035BBCD:
loc_0035BBD2:
    if (0 == 0) goto loc_0035C07F;
    if (0 == 0) goto loc_0035BBE9;
    goto loc_0035BC2A;
loc_0035BBE9:
    Arg2 = (0) - (*(uint64_t *)(v_rip + 0xB0CA0E));
    Arg2 = (Arg2) >> (20);
    Arg2 = (Arg2) + (Arg2);
    result = RtlCSparseBitmapBitmaskRead(v_rip + 11586077, Arg2, 1, Arg4);
    if (result == 0) goto loc_0035C074;
    result = (uint32_t)((result) - 1);
    if (((uint32_t)(result)) == 2) goto loc_0035C074;
    if (((uint32_t)(result)) == 1) goto loc_0035D9EB;
loc_0035BC2A:
    Arg2 = (*(uint64_t *)(v_stack_m220 + 0x140)) & (0);
    result = (*(uint64_t *)(Arg2 + 0x10)) ^ (*(uint64_t *)(v_rip + 0xACC6C2));
    result = (result) ^ (Arg2);
    if (result != (v_stack_m220 + 320)) goto loc_0035BE67;
    Arg3 = (uint32_t)((0) - ((uint32_t)(Arg2)));
    Arg3 = (uint32_t)((Arg3) >> ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(v_stack_m220 + 0x140 + 0x8))))));
    Arg3 = (Arg3) << (5);
    Arg3 = (Arg3) + (Arg2);
    result = -(*(uint8_t *)(Arg3 + 0x1A));
    result = (result) << (5);
    Arg3 = (Arg3) + (result);
    local_rbx = (Arg3) - (Arg2);
    local_rbx = (local_rbx) >> (5);
    local_rbx = (local_rbx) << ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(v_stack_m220 + 0x140 + 0x8)))));
    local_rbx = (local_rbx) + (Arg2);
    result = (local_rbx == 0) ? 1 : 0;
    if (((uint8_t)(result + *(uint8_t *)(Arg3 + 0x18) * 1)) != 11) goto loc_0035BF89;
    result = (local_rbx) >> (12);
    result = (uint32_t)((result) ^ (*(uint32_t *)(local_rbx + 0x28)));
    result = (uint32_t)((result) ^ (*(uint32_t *)(v_rip + 0xACC659)));
    result = (result) >> (16);
    result = (result) + (local_rbx);
    v_stack_mC8 = (uint32_t)((uint32_t)((uint32_t)(result)));
    Arg3 = (uint32_t)((0) - ((uint32_t)(result)));
    Arg2 = (*(uint16_t *)(local_rbx + 0x2C)) << (6);
    local_rsi = ((uint32_t)(*(uint32_t *)(Arg2 + *(uint64_t *)(v_stack_m220 + 0x140 + 0x18) * 1 + 0x48))) * ((uint32_t)(Arg3));
    local_rsi = (local_rsi) >> (32);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) * ((uint32_t)((uint16_t)((uint32_t)((uint32_t)(result))))));
    Arg3 = (uint32_t)((Arg3) - ((uint32_t)(result)));
    v_stack_mCC = Arg3;
    if (condition_is_not_equal) goto loc_0035C07F;
    local_r13 = 0;
    local_r10 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m220 + 0x140 + 0x18) + 0x4C))) >> (4);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m220 + 0x140 + 0x18) + 0x4C))))) >> (13));
    local_r10 = (uint32_t)((local_r10) & (511));
    Arg2 = (uint32_t)((Arg2) & (0x3FFFFULL));
    Arg4 = (uint32_t)((1) << ((uint8_t)((uint16_t)((uint32_t)((uint32_t)(result))))));
    Arg1 = (uint32_t)(((uint16_t)((uint32_t)((uint32_t)(result)))) + (-2));
    v_stack_m14C = (uint32_t)(Arg1);
    Arg4 = (uint32_t)((Arg4) ^ ((uint32_t)(Arg2)));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8BB0) + Arg1 * 8) + Arg4 * 8 + 0x8) + local_r10 * 8) == 0) goto loc_0035E8B3;
loc_0035BD4A:
    if (((uint16_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8BB0) + Arg1 * 8) + Arg4 * 8 + 0x8) + local_r10 * 8))) == (*(uint16_t *)(local_rbx + 0x2E))) goto loc_0035E84C;
loc_0035BD54:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) >> (6));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (63));
    if (condition_is_above_or_equal) goto loc_0035C0D2;
    local_rsi = (uint16_t)((local_rsi) + 1);
loc_0035BD76:
    v_stack_m160 = *(uint64_t *)(local_rbx + 0x10);
    Arg1 = (*(uint64_t *)(local_rbx + 0x10)) >> (48);
    v_stack_m220 = *(uint64_t *)(local_rbx + 0x10);
    if (((uint8_t)(Arg1)) == 1) {
        v_stack_m21A = 2;
    }
    *(uint16_t *)(0) = (uint16_t)(v_stack_m220);
    v_stack_m68 = *(uint64_t *)(*(uint64_t *)(v_stack_m220 + 0x140 + 0x18) + 0x50);
    Arg3 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(v_stack_m220 + 0x140 + 0x18) + 0x50)) ^ (*(uint32_t *)(0)));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_m220 + 0x140 + 0x18) + 0x50)) >> (32);
    Arg2 = (uint32_t)((Arg2) ^ (0));
    Arg3 = (uint32_t)((Arg3) ^ ((uint32_t)(Arg2)));
    v_stack_m220 = (uint16_t)(local_rsi);
    *(uint32_t *)(0 + 0x8) = Arg3;
    Arg2 = (*(uint16_t *)(local_rbx + 0x2C)) << (6);
    if (condition_is_not_equal) goto loc_0035BD76;
    if ((*(uint8_t *)(Arg2 + *(uint64_t *)(v_stack_m220 + 0x140 + 0x18) * 1 + 0x5C)) == 0) goto loc_0035C4AC;
loc_0035BDE6:
    if (v_stack_m15A != 1) goto loc_0035BE87;
    Arg4 = (uint32_t)((v_stack_m15C) << (6));
    Arg4 = (Arg4) + (*(uint64_t *)(v_stack_m220 + 0x140 + 0x18));
    Arg1 = (*(uint64_t *)(local_rbx + 0x18)) ^ (*(uint64_t *)(Arg4 + 0x8));
    Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (uint32_t)((*(uint64_t *)(Arg4 + 0x8)) & (0xFFFULL));
    Arg1 = (Arg1) ^ (*(uint64_t *)(local_rbx + 0x18));
    *(uint64_t *)(local_rbx + 0x18) = Arg1;
    Arg1 = (local_rbx) | (Arg2);
    if (condition_is_equal) goto loc_0035BE87;
loc_0035BE34:
    Arg1 = (*(uint64_t *)(local_rbx + 0x18)) ^ (*(uint64_t *)(Arg4 + 0x8));
    Arg2 = (uint32_t)((*(uint64_t *)(Arg4 + 0x8)) & (0xFFFULL));
    Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (Arg1) ^ (*(uint64_t *)(local_rbx + 0x18));
    *(uint64_t *)(local_rbx + 0x18) = Arg1;
    Arg1 = (local_rbx) | (Arg2);
    if ((*(uint64_t *)(Arg4 + 0x8)) != (*(uint64_t *)(Arg4 + 0x8))) goto loc_0035BE34;
    goto loc_0035BE87;
loc_0035BE67:
    local_r13 = 0;
loc_0035BE6A:
    Arg4 = 0;
    v_stack_m240 = 0;
    v_stack_m248 = 0;
    result = RtlpLogHeapFailure(Arg4 + 9, *(uint64_t *)(local_rsi + 0x38), 0, Arg4);
loc_0035BE87:
loc_0035BE8E:
    if (1 != 0) goto loc_0035C7C0;
    v_stack_m110 = v_xmm0;
    v_stack_m110 = 257;
    v_stack_m110 = 3;
    v_stack_m110 = 3;
    v_stack_m10E = 1;
    if (0 == 0) goto loc_0035D567;
loc_0035BEBD:
    v_stack_m120 = 0x100000ULL;
    v_stack_m11C = 0x1000000ULL;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m168 + (int32_t)(0) * 4 + 0x48))) - 1;
    result = ~(result);
    result = (result) & (0);
    local_r15 = (*(uint64_t *)(result + 0x10)) ^ (*(uint64_t *)(v_rip + 0xACC41A));
    local_r15 = (local_r15) ^ (result);
    result = ((int32_t)(0) + (int32_t)(0) * 2) << (6);
    local_r15 = (local_r15) - (result);
    local_r15 = (local_r15) - (320);
loc_0035BEFB:
    v_stack_m1E0 = local_r15;
    if (local_r15 != 0) goto loc_0035C7D2;
    v_stack_m248 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeBugCheckEx(194, Arg2, Arg3, 0);
loc_0035BF20:
    v_stack_m1B0 = local_r11;
    Arg1 = (uint32_t)((local_r11) & (448));
    if (Arg1 != 256) goto loc_0035BF4A;
loc_0035BF39:
    if (Arg1 != 256) goto loc_0035BF62;
    goto loc_0035BF64;
loc_0035BF4A:
    if (Arg1 >= 256) goto loc_0035BF39;
    local_rdi = (local_r11) | (64);
    v_stack_m1B0 = local_rdi;
loc_0035BF62:
loc_0035BF64:
    if (((uint8_t)(v_cr8)) <= 2) goto loc_0035ECFE;
    v_stack_m248 = 48;
    result = KeBugCheckEx(193, (uint8_t)(v_cr8), (uint32_t)((uint32_t)(local_rdi)), local_rsi);
loc_0035BF89:
    Arg4 = (local_rsi) & ((uint32_t)((uint32_t)(local_rdi)));
    local_r13 = 0;
    result = ((uint32_t)((uint32_t)(local_rdi))) - (Arg4);
    v_stack_m194 = 0;
    result = (result) >> (5);
    result = (result) << ((uint8_t)((uint32_t)((uint32_t)(*(uint64_t *)(local_rbx + 0x18)))));
    result = (uint8_t)(((uint8_t)((uint8_t)(v_cr8))) & (3));
    if (((uint8_t)(result)) != 3) goto loc_0035BE6A;
    if (local_rdi == (result + Arg4 * 1)) goto loc_0035C0C2;
    if (((uint8_t)((uint8_t)(v_cr8))) != 15) goto loc_0035BE6A;
    if (local_rdi <= (result + Arg4 * 1)) goto loc_0035C0C2;
    result = RtlpHpVsContextFree(*(uint64_t *)(local_rsi + 0x20), result + Arg4 * 1, local_rdi, v_stack_m194);
    if ((uint32_t)(result) == 0) goto loc_0035BE87;
    if (((uint32_t)((uint32_t)(v_stack_m194))) >= ((uint32_t)(*(uint16_t *)(*(uint64_t *)(local_rsi + 0x18) + 0x44)))) goto loc_0035BE8E;
    result = (uint32_t)(((uint32_t)(v_stack_m194) + 15) >> (4));
    local_r10 = (uint32_t)((*(uint8_t *)(result + v_rip - 0x35BFF5 * 1 + 0x10B80)) - 1);
loc_0035C01A:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x18) + local_r10 * 8 + 0x1C0)) >> (16);
    v_stack_m1E0 = *(uint64_t *)(*(uint64_t *)(local_rsi + 0x18) + local_r10 * 8 + 0x1C0);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsi + 0x18) + local_r10 * 8 + 0x1C0))) & (1)) == 0) goto loc_0035C057;
    if (((uint16_t)(result)) >= = 1) {
        result = (uint16_t)((result) - 1);
        v_stack_m1DE = (uint16_t)(result);
        Arg1 = v_stack_m1E0;
    }
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0x18) + local_r10 * 8 + 0x1C0)) != (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x18) + local_r10 * 8 + 0x1C0))) goto loc_0035C01A;
loc_0035C057:
    goto loc_0035BE8E;
loc_0035C064:
    result = *(uint64_t *)(*(uint64_t *)(local_rsi + 0x18) + local_r10 * 8 + 0x1C0);
    if ((((uint8_t)(local_r11)) & (128)) != 0) { result = *(uint64_t *)(local_rsi + 0x18) + local_r10 * 8; }
    goto loc_0035BB75;
loc_0035C074:
    result = RtlpHpLargeFree(0, v_rip - 3522549, *(uint64_t *)(*(uint64_t *)(local_rsi + 0x18) + local_r10 * 8 + 0x1C0), *(uint64_t *)(local_rsi + 0x18) + local_r10 * 8);
loc_0035C07F:
    local_r13 = 0;
    goto loc_0035BE87;
loc_0035C087:
    goto loc_0035BB79;
loc_0035C090:
    if (((uint32_t)(*(uint64_t *)(local_r15 + 0x18))) < ((uint32_t)(*(uint16_t *)(v_rip + 0xC68F69)))) goto loc_0035D849;
    v_stack_m248 = (uint32_t)((uint32_t)(local_rbx));
    result = KeBugCheckEx(194, 14, *(uint64_t *)(local_r15 + 0x18), local_r11);
loc_0035C0C2:
    result = RtlpHpSegPageRangeShrink(local_rsi, *(uint64_t *)(local_r15 + 0x18), *(uint64_t *)(local_r15 + 0x18), local_r11);
    goto loc_0035BE87;
loc_0035C0D2:
    v_stack_m240 = 0;
    v_stack_m248 = local_rsi;
    result = RtlpLogHeapFailure(17, *(uint64_t *)(*(uint64_t *)(v_stack_m220 + 0x140 + 0x18)), v_rip - 3522549, local_rbx);
    goto loc_0035BE87;
loc_0035C0F4:
    if ((((uint32_t)(local_rsi)) & (0xFFFULL)) != 0) goto loc_0035C4E4;
    if (local_rsi > ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r15 + 0x18) + 0x210)))) goto loc_0035C4E4;
    Arg4 = (uint32_t)(~((uint32_t)((uint32_t)(local_r11))));
    Arg4 = (uint32_t)((Arg4) & (2));
    result = RtlpHpAllocateHeapBackend(*(uint64_t *)(local_r15 + 0x18), local_rsi, local_rsi, Arg4);
loc_0035C128:
loc_0035C12B:
    if (result == 0) goto loc_0035D91E;
    local_rsi = 0;
    v_stack_m240 = 0;
    v_stack_m248 = 0;
    result = ExpAddTagForBigPages(result, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), v_stack_m1F8, v_stack_m1F0);
    if ((uint32_t)(result) != 0) goto loc_0035D418;
    v_stack_p10 = 0;
loc_0035C16F:
    goto loc_0035BBCD;
loc_0035C179:
    if ((((uint8_t)(local_r11)) & (8)) != 0) goto loc_0035D812;
loc_0035C187:
    local_rsi = (local_r13 + 16) + (15);
    local_rsi = (local_rsi) & (-16);
    v_stack_m228 = local_rsi;
    v_stack_m1F8 = local_rsi;
    if ((local_rsi - 513) <= 0xD7FULL) goto loc_0035E556;
loc_0035C1B3:
    Arg2 = v_stack_m1F8;
    if (local_rsi > 1) { Arg2 = local_rsi; }
    v_stack_m1A8 = Arg2;
    if (Arg2 >= (*(uint16_t *)((uint32_t)(v_stack_m1FC) + 0x384))) goto loc_0035F483;
    result = (uint32_t)((Arg2 + 15) >> (4));
    result = (uint32_t)((*(uint8_t *)(result + v_rip - 0x35C192 * 1 + 0x10B80)) - 1);
    v_stack_p8 = (uint32_t)(result);
    local_r10 = ((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m1FC) + 0x340 + 0x4C))) >> (4);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m1FC) + 0x340 + 0x4C))))) >> (13));
    local_r10 = (uint32_t)((local_r10) & (511));
    Arg2 = (uint32_t)((Arg2) & (0x3FFFFULL));
    Arg4 = (uint32_t)((1) << ((uint8_t)(result)));
    Arg1 = (uint32_t)((result) + (-2));
    v_stack_m150 = (uint32_t)(Arg1);
    Arg4 = (uint32_t)((Arg4) ^ ((uint32_t)(Arg2)));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8BB0) + Arg1 * 8) + Arg4 * 8 + 0x8) + local_r10 * 8) == 0) goto loc_0035E9CE;
loc_0035C24A:
    v_stack_m1B8 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8BB0) + Arg1 * 8) + Arg4 * 8 + 0x8) + local_r10 * 8);
    result = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p8)))) + ((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    Arg1 = (uint32_t)(((uint16_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8BB0) + Arg1 * 8) + Arg4 * 8 + 0x8) + local_r10 * 8))) << (6));
    Arg1 = (Arg1) + ((uint32_t)(v_stack_m1FC) + 832);
    v_stack_p8 = result;
    result = (result) + (Arg1);
    v_stack_p10 = Arg1;
    v_stack_m218 = result;
    if ((uint32_t)(*(uint16_t *)(result)) == 0) goto loc_0035D92D;
loc_0035C286:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(result)))) << (6));
    Arg2 = ((uint32_t)(Arg3)) + ((uint32_t)(v_stack_m1FC) + 832);
    v_stack_m228 = local_rsi;
    v_stack_m218 = Arg2;
    if ((*(uint16_t *)(Arg2 + 0x4)) != 0) goto loc_0035F46B;
    v_stack_m200 = 0;
    v_stack_m228 = local_rsi;
loc_0035C2BA:
    if (((*(uint64_t *)(Arg2 + 0x38)) & (0xFFFULL)) == 0) goto loc_0035D8DB;
    if (((*(uint64_t *)(Arg2 + 0x38)) & (0xFFFULL)) != 0) goto loc_0035D839;
    local_r11 = (*(uint64_t *)(Arg2 + 0x38)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m228 = local_rsi;
    result = (local_r11) >> (12);
    v_stack_m238 = local_r11;
    result = (uint32_t)((result) ^ (*(uint32_t *)(local_r11 + 0x28)));
    result = (uint32_t)((result) ^ (*(uint32_t *)(v_rip + 0xACC003)));
    v_stack_m1C8 = (uint32_t)(result);
    local_r10 = (uint32_t)((*(uint8_t *)(local_r11 + 0x18)) - (8));
    v_stack_m1E8 = (uint32_t)((uint16_t)(result));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x768)) ^ (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760));
    Arg3 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x768) + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760) * 1) >> (32);
    result = (Arg2) << (16);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760)) ^ (result);
    Arg1 = (Arg1) ^ (Arg2);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760) = Arg1;
    local_r10 = (local_r10) - 1;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x768) = Arg2;
    v_stack_m198 = (uint32_t)(*(uint8_t *)(local_r11 + 0x32));
    v_stack_p8 = (uint8_t)(*(uint8_t *)(local_r11 + 0x27));
    v_stack_p10 = (uint32_t)((uint8_t)(Arg3));
    v_stack_m1B8 = local_r11 + 64 + local_r10 * 8;
loc_0035C38C:
    Arg2 = ~(*(uint64_t *)(local_r11 + 0x40 + *(uint8_t *)(local_r11 + 0x24) * 8));
    if (Arg2 == 0) goto loc_0035DD48;
loc_0035C39B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACBF87)))) & (4)) != 0) goto loc_0035DB97;
    if ((local_r11 + 64 + *(uint8_t *)(local_r11 + 0x24) * 8) == (local_r11 + 64 + local_r10 * 8)) goto loc_0035E446;
    if (((uint32_t)((uint32_t)(v_stack_m198))) != 64) goto loc_0035E446;
    local_r10 = (uint32_t)((local_r11 + 64 + local_r10 * 8) + ((uint32_t)((uint8_t)(Arg3))));
    local_r10 = (uint32_t)((local_r10) & (63));
loc_0035C3CD:
    Arg4 = (1) << ((uint8_t)((uint32_t)((uint32_t)(local_r10))));
loc_0035C3D9:
loc_0035C3E0:
    Arg1 = (*(uint64_t *)(local_r11 + 0x40 + *(uint8_t *)(local_r11 + 0x24) * 8)) | (Arg4);
    if (condition_is_not_equal) goto loc_0035C3E0;
    if (((*(uint64_t *)(local_r11 + 0x40 + *(uint8_t *)(local_r11 + 0x24) * 8)) & (Arg4)) != 0) goto loc_0035DB6A;
    Arg3 = (uint32_t)((local_r11 + 64 + *(uint8_t *)(local_r11 + 0x24) * 8) - ((uint32_t)(local_r11 + 64)));
    v_stack_p10 = (uint32_t)(local_r10 + Arg3 * 8);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r10 + Arg3 * 8))) * ((uint32_t)((uint32_t)(v_stack_m1E8))));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r10 + Arg3 * 8))) >> (6));
    *(uint8_t *)(local_r11 + 0x24) = (uint8_t)(result);
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(v_stack_m1C6)));
    if (v_stack_p8 <= 1) goto loc_0035DE15;
    result = RtlpHpLfhSubsegmentCommitBlock((uint32_t)(v_stack_m1FC) + 832, local_r11, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(v_stack_m1E8));
    if (sign_flag) goto loc_0035DC1D;
loc_0035C44F:
    local_rsi = (local_rsi) + (v_stack_m238);
    local_r11 = v_stack_m238;
    if (0 == 0) {
        Arg2 = (uint32_t)(v_stack_m228);
        Arg1 = local_rsi;
        Arg2 = (Arg2) + (15);
        Arg2 = (Arg2) & (-16);
        result = RtlHeapZero(Arg1, Arg2, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(v_stack_m1E8));
        local_r11 = v_stack_m238;
    }
    if (local_rsi == 0) goto loc_0035DC63;
    if (v_stack_m200 == 0) goto loc_0035D8F5;
    Arg2 = (*(uint16_t *)(v_stack_m218 + 0x2)) << (6);
    Arg2 = (Arg2) + ((uint32_t)(v_stack_m1FC) + 832);
    result = RtlpHpLfhBucketUpdateAffinityMapping((uint32_t)(v_stack_m1FC) + 832, Arg2, (uint32_t)(v_stack_m1FC) + 832, (uint32_t)(v_stack_m1E8));
    goto loc_0035D8F5;
loc_0035C4AC:
    *(uint8_t *)(Arg2 + v_stack_m1F0 * 1 + 0x5C) = 1;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m1F0) + 0x38))) >> (8);
    if (((uint8_t)(result)) != 1) goto loc_0035D40D;
loc_0035C4CE:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB9E2EE))) != 0) goto loc_0035BDE6;
    result = RtlpHpEnvCompactionSchedule(*(uint64_t *)(*(uint64_t *)(v_stack_m1F0) + 0x38), Arg2, (uint32_t)(v_stack_m1FC) + 832, (uint32_t)(v_stack_m1E8));
    goto loc_0035BDE6;
loc_0035C4E4:
    local_rdi = (uint32_t)(v_stack_m1FC) + 832;
    if (local_rsi > ((uint32_t)(v_stack_m1FC) + 832)) { local_rdi = local_rsi; }
    v_stack_m1C0 = local_rdi;
    if (local_rdi >= (*(uint16_t *)((uint32_t)(v_stack_m1FC) + 0x384))) goto loc_0035D97F;
    Arg1 = (uint32_t)((local_rdi + 15) >> (4));
    local_r10 = ((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m1FC) + 0x340 + 0x4C))) >> (4);
    local_r10 = (uint32_t)((local_r10) & (511));
    result = (uint32_t)((*(uint8_t *)(Arg1 + v_rip - 0x35C516 * 1 + 0x10B80)) - 1);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m1FC) + 0x340 + 0x4C))))) >> (13));
    Arg2 = (uint32_t)((Arg2) & (0x3FFFFULL));
    v_stack_p8 = (uint32_t)(result);
    Arg4 = (uint32_t)((1) << ((uint8_t)(Arg1)));
    Arg1 = (uint32_t)((Arg1) + (-2));
    v_stack_m158 = (uint32_t)(Arg1);
    Arg4 = (uint32_t)((Arg4) ^ ((uint32_t)(Arg2)));
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8BB0) + Arg1 * 8) + Arg4 * 8 + 0x8) + local_r10 * 8) == 0) goto loc_0035E9E2;
loc_0035C57D:
    v_stack_m1A8 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8BB0) + Arg1 * 8) + Arg4 * 8 + 0x8) + local_r10 * 8);
    result = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p8)))) + ((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))));
    local_rbx = (uint32_t)(((uint16_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8BB0) + Arg1 * 8) + Arg4 * 8 + 0x8) + local_r10 * 8))) << (6));
    local_rbx = (local_rbx) + ((uint32_t)(v_stack_m1FC) + 832);
    v_stack_p8 = result;
    if ((uint32_t)(*(uint16_t *)(result + local_rbx * 1)) == 0) goto loc_0035D96E;
loc_0035C5AB:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(result + local_rbx * 1)))) << (6));
    Arg2 = ((uint32_t)(Arg3)) + ((uint32_t)(v_stack_m1FC) + 832);
    v_stack_m218 = Arg2;
    v_stack_m200 = 0;
    v_stack_m1B0 = *(uint64_t *)(Arg2 + 0x38);
loc_0035C5DF:
    if (((*(uint64_t *)(Arg2 + 0x38)) & (0xFFFULL)) == 0) goto loc_0035DD56;
    if (((*(uint64_t *)(Arg2 + 0x38)) & (0xFFFULL)) != 0) goto loc_0035D85B;
    local_rdi = (*(uint64_t *)(Arg2 + 0x38)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m238 = local_rdi;
    result = (local_rdi) >> (12);
    result = (uint32_t)((result) ^ (*(uint32_t *)(local_rdi + 0x28)));
    result = (uint32_t)((result) ^ (*(uint32_t *)(v_rip + 0xACBCDA)));
    v_stack_m198 = (uint32_t)(result);
    local_r10 = (uint32_t)((*(uint8_t *)(local_rdi + 0x18)) - (8));
    v_stack_m1E8 = (uint32_t)((uint16_t)(result));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x768)) ^ (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760));
    Arg3 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x768) + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760) * 1) >> (32);
    result = (Arg2) << (16);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760)) ^ (result);
    Arg1 = (Arg1) ^ (Arg2);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760) = Arg1;
    local_r10 = (local_r10) - 1;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x768) = Arg2;
    v_stack_m1C8 = (uint32_t)(*(uint8_t *)(local_rdi + 0x32));
    v_stack_p8 = (uint8_t)(*(uint8_t *)(local_rdi + 0x27));
    v_stack_p10 = (uint32_t)((uint8_t)(Arg3));
    v_stack_m1A8 = local_rdi + 64 + local_r10 * 8;
loc_0035C6A8:
    Arg2 = ~(*(uint64_t *)(local_rdi + 0x40 + *(uint8_t *)(local_rdi + 0x24) * 8));
    if (Arg2 == 0) goto loc_0035DD8D;
loc_0035C6B7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACBC6B)))) & (4)) != 0) goto loc_0035DBE9;
    if ((local_rdi + 64 + *(uint8_t *)(local_rdi + 0x24) * 8) == (local_rdi + 64 + local_r10 * 8)) goto loc_0035E51A;
    if (((uint32_t)((uint32_t)(v_stack_m1C8))) != 64) goto loc_0035E51A;
    local_r10 = (uint32_t)(((uint32_t)(v_stack_m1C8)) + ((uint32_t)((uint8_t)(Arg3))));
    local_r10 = (uint32_t)((local_r10) & (63));
loc_0035C6EE:
    Arg4 = (1) << ((uint8_t)((uint32_t)((uint32_t)(local_r10))));
loc_0035C6FA:
loc_0035C701:
    Arg1 = (*(uint64_t *)(local_rdi + 0x40 + *(uint8_t *)(local_rdi + 0x24) * 8)) | (Arg4);
    if (condition_is_not_equal) goto loc_0035C701;
    if (((*(uint64_t *)(local_rdi + 0x40 + *(uint8_t *)(local_rdi + 0x24) * 8)) & (Arg4)) != 0) goto loc_0035DBBC;
    Arg3 = (uint32_t)((local_rdi + 64 + *(uint8_t *)(local_rdi + 0x24) * 8) - ((uint32_t)(local_rdi + 64)));
    v_stack_p10 = (uint32_t)(local_r10 + Arg3 * 8);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r10 + Arg3 * 8))) >> (6));
    *(uint8_t *)(local_rdi + 0x24) = (uint8_t)(result);
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(local_r10 + Arg3 * 8))) * ((uint32_t)((uint32_t)(v_stack_m1E8))));
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(v_stack_m196)));
    if (v_stack_p8 <= 1) goto loc_0035DE7B;
    result = RtlpHpLfhSubsegmentCommitBlock((uint32_t)(v_stack_m1FC) + 832, v_stack_m238, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(v_stack_m1E8));
    if (sign_flag) goto loc_0035DCB9;
loc_0035C76D:
    local_rdi = (local_rdi) + (v_stack_m238);
    local_r10 = v_stack_m238;
    if (v_stack_m228 == 0) {
        Arg2 = (uint32_t)(local_rsi);
        Arg1 = local_rdi;
        Arg2 = (Arg2) + (15);
        Arg2 = (Arg2) & (-16);
        result = RtlHeapZero(Arg1, Arg2, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(v_stack_m1E8));
        local_r10 = v_stack_m238;
    }
    if (local_rdi == 0) goto loc_0035DCFA;
    if (v_stack_m200 != 0) goto loc_0035F446;
loc_0035C7A7:
loc_0035C7A9:
    if (local_rdi != -1) goto loc_0035C12B;
    goto loc_0035D984;
loc_0035C7C0:
    if ((uint32_t)(v_stack_m1FC) + 832 == 0) goto loc_0035CB63;
    goto loc_0035F4BD;
loc_0035C7D2:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA2548))) != 0) goto loc_0035CA28;
loc_0035C7E0:
    if ((((uint32_t)(v_stack_m1FC) + 832) & (0xFFFULL)) == 0) goto loc_0035CE37;
    if ((((uint8_t)(*(uint8_t *)((uint32_t)(v_stack_m1FC) + 0x340 - 0xD))) & (8)) != 0) goto loc_0035CF39;
loc_0035C800:
    result = *(uint8_t *)((uint32_t)(v_stack_m1FC) + 0x340 - 0xD);
    local_r14 = (uint32_t)(v_stack_m1FC) + 832 - 16;
    if (((*(uint8_t *)((uint32_t)(v_stack_m1FC) + 0x340 - 0x10 + 0x3)) & (4)) != 0) {
        result = *(uint16_t *)((uint32_t)(v_stack_m1FC) + 0x340 - 0x10);
        Arg1 = 255;
        result = (uint16_t)((result) & ((uint16_t)(Arg1)));
        result = (uint16_t)(result);
        result = (result) << (4);
        local_r14 = ((uint32_t)(v_stack_m1FC) + 832 - 16) - (result);
    }
    Arg1 = 256;
    if ((((uint8_t)(*(uint8_t *)(local_r14 + 0x3))) & (1)) == 0) { Arg1 = 128; }
    Arg2 = ((uint32_t)((uint32_t)(Arg1))) | (4);
    if ((((uint8_t)(*(uint8_t *)(local_r14 + 0x3))) & (32)) == 0) { Arg2 = Arg1; }
    Arg2 = (Arg2) | (2);
    v_stack_m238 = Arg2;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(local_r14 + 0x3)))) & (8));
    if (condition_is_not_equal) goto loc_0035CE19;
loc_0035C860:
    if ((((uint8_t)(*(uint8_t *)(local_r14 + 0x3))) & (222)) == 0) goto loc_0035C8B5;
    Arg1 = (Arg2) | (8);
    if ((((uint8_t)(*(uint8_t *)(local_r14 + 0x3))) & (4)) == 0) { Arg1 = Arg2; }
    if (((128) & ((uint8_t)(*(uint8_t *)(local_r14 + 0x3)))) == 0) { Arg1 = Arg1; }
    if ((((uint8_t)(*(uint8_t *)(local_r14 + 0x3))) & (64)) == 0) { Arg1 = Arg1; }
    v_stack_m238 = Arg1;
    if (Arg4 != 0) goto loc_0035C8B5;
    v_stack_m238 = Arg1;
    result = 128;
    if ((((uint8_t)(*(uint8_t *)(local_r14 + 0x3))) & (16)) != 0) {
        result = Arg1;
        result = (result) | (32);
        v_stack_m238 = result;
    }
    local_r15 = ((uint8_t)(*(uint16_t *)(local_r14 + 0x2))) << (4);
loc_0035C8C6:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC6A304)))) & (519)) != 0) goto loc_0035E631;
loc_0035C8DC:
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xC6A2EE));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC6A2EE)))) & (16)) != 0) {
        Arg4 = (uint32_t)(v_stack_m1FC) + 832;
        Arg3 = local_r15;
        Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x4)));
        Arg1 = local_r14;
        result = VfPtFreePoolNotification(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m1C4 = (uint32_t)((uint32_t)(v_stack_m1FC) + 832);
    v_stack_m22C = 0;
    v_stack_m20C = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x4)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC68850))))) {
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC6A1EF)))) & (65)) != 0) goto loc_0035E6C2;
loc_0035C91D:
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))))) * ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x4)))));
    Arg2 = (Arg1) >> (32);
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)(*(uint64_t *)(v_rip + 0xBA242C))));
loc_0035C955:
    Arg1 = ((uint32_t)((uint32_t)(Arg2)) + (uint32_t)((uint32_t)(Arg2)) * 4) + ((uint32_t)((uint32_t)(Arg2)) + (uint32_t)((uint32_t)(Arg2)) * 4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x35C935 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x4))))) goto loc_0035CB79;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x35C935 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8))) == 0) goto loc_0035D3A2;
loc_0035C976:
    result = (uint32_t)((Arg2 + 1) & ((uint32_t)(*(uint64_t *)(v_rip + 0xBA242C))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_0035C955;
    v_stack_m138 = v_xmm0;
    result = 0;
    v_stack_m130 = v_rip + 12182387;
    v_stack_m138 = (uint32_t)(v_stack_m1FC) + 832;
    v_stack_m128 = 0;
    if ((*(uint32_t *)(v_rip + 0xC6A36C)) != 0) goto loc_0035D345;
loc_0035C9BA:
    v_stack_m128 = (uint8_t)(v_cr8);
    if (((*(uint8_t *)(v_rip + 0xC6A145)) & (33)) != 0) goto loc_0035D2D8;
loc_0035C9CB:
    if (v_stack_m138 != 0) goto loc_0035D6C8;
loc_0035C9DF:
loc_0035CA00:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1FC) + 832))))) >= (*(uint64_t *)(v_rip + 0xBA2362))) goto loc_0035D884;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1FC) + 832)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1FC) + 832)))) * 4) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xBA2350));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x4))))) goto loc_0035CA4E;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))) == 0) goto loc_0035D884;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m1FC) + 832))) + 1);
    goto loc_0035CA00;
loc_0035CA28:
loc_0035CA36:
    if ((v_rip + 12133649) >= (v_rip + 12133674)) goto loc_0035C7E0;
    if (local_r15 == (*(uint64_t *)(v_rip + 0xB92511))) goto loc_0035EC14;
    result = (v_rip + 12133649) + (8);
    goto loc_0035CA36;
loc_0035CA4E:
    if (condition_is_below) goto loc_0035CE27;
loc_0035CA67:
    Arg2 = -(local_r15);
    if ((*(uint64_t *)(v_rip + 0xB9252A + 0x48)) != 0) goto loc_0035E714;
loc_0035CA81:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m138, Arg2, v_rip + 12133674 + 8, 1);
loc_0035CA8A:
    local_rsi = v_stack_m238;
    if ((*(uint64_t *)(v_rip + 0xB9252A + 0x48)) < 0) {
        local_rsi = (v_stack_m238) >> (8);
        Arg4 = 0;
        local_rsi = (uint32_t)((local_rsi) & (1));
        Arg2 = local_r15;
        Arg3 = (uint32_t)(local_rsi);
        Arg1 = (uint32_t)(v_stack_m1FC) + 832;
        result = ViFreeTrackedPool(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint8_t *)(v_rip + 0xC721B8)) != 0) goto loc_0035DA1A;
loc_0035CAB6:
    if ((local_r15 - 513) <= 0xD7FULL) goto loc_0035DDC2;
loc_0035CAD8:
    if ((uint16_t)(local_r14) == 0) goto loc_0035CAE7;
    local_rbx = (v_stack_m1E0) + (320);
    goto loc_0035CB26;
loc_0035CAE7:
    Arg2 = (local_r14) - (*(uint64_t *)(v_rip + 0xB0BB10));
    Arg2 = (Arg2) >> (20);
    Arg2 = (Arg2) + (Arg2);
    result = RtlCSparseBitmapBitmaskRead(v_rip + 11582239, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0035E7A8;
    if (((uint32_t)(result)) == 3) goto loc_0035E7A8;
    local_rbx = (local_rbx) + (320);
    if (((uint32_t)(result)) == 2) goto loc_0035DAA3;
loc_0035CB26:
    Arg2 = (*(uint64_t *)(local_rbx)) & (local_r14);
    result = (*(uint64_t *)(Arg2 + 0x10)) ^ (*(uint64_t *)(v_rip + 0xACB7C6));
    result = (result) ^ (Arg2);
    if (result == local_rbx) goto loc_0035CC00;
loc_0035CB46:
    Arg4 = 0;
    v_stack_m240 = (uint32_t)(v_stack_m1FC) + 832;
    v_stack_m248 = (uint32_t)(v_stack_m1FC) + 832;
    result = RtlpLogHeapFailure(Arg4 + 9, *(uint64_t *)(local_rbx + 0x38), local_r14, Arg4);
loc_0035CB63:
    if (((v_stack_m1F0) & (32)) == 0) goto loc_0035F4BD;
    result = RtlRaiseStatus((uint32_t)(0xC000009AULL), *(uint64_t *)(local_rbx + 0x38), local_r14, Arg4);
loc_0035CB79:
    if (condition_is_above_or_equal) goto loc_0035D2F7;
loc_0035CB8F:
    Arg1 = -(local_r15);
    if ((*(uint64_t *)(Arg4 + 0x48)) == 0) goto loc_0035CA8A;
    if (((*(uint8_t *)(Arg4 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1FC) + 0x340)))) * 8 + 0x38)) & (1)) != 0) goto loc_0035CA8A;
    local_r10 = (local_r15 * 4 + 63) & (-64);
    if (local_r10 == 64) { local_r10 = 128; }
loc_0035CBD9:
    if (Arg1 >= (*(uint64_t *)(Arg4 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1FC) + 0x340)))) * 8 + 0x38))) goto loc_0035CA8A;
    if ((local_r10 + Arg1 * 1) >= (*(uint64_t *)(Arg4 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1FC) + 0x340)))) * 8 + 0x38))) goto loc_0035CA8A;
    if ((local_r10 + Arg1 * 1) == (*(uint64_t *)(Arg4 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1FC) + 0x340)))) * 8 + 0x38))) goto loc_0035E8C0;
    goto loc_0035CBD9;
loc_0035CC00:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)(Arg4 + 32)));
    Arg3 = (uint32_t)((Arg3) >> ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_r10 + Arg1 * 1 + 0x8))))));
    Arg3 = (Arg3) << (5);
    Arg3 = (Arg3) + (Arg4 + 32);
    result = -(*(uint8_t *)(Arg3 + 0x1A));
    result = (result) << (5);
    Arg3 = (Arg3) + (result);
    local_rdi = (Arg3) - (Arg4 + 32);
    local_rdi = (local_rdi) >> (5);
    local_rdi = (local_rdi) << ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_r10 + Arg1 * 1 + 0x8)))));
    local_rdi = (local_rdi) + (Arg4 + 32);
    result = (local_rdi == local_r14) ? 1 : 0;
    if (((uint8_t)(result + *(uint8_t *)(Arg3 + 0x18) * 1)) != 11) goto loc_0035D208;
    result = (local_rdi) >> (12);
    result = (uint32_t)((result) ^ (*(uint32_t *)(local_rdi + 0x28)));
    result = (uint32_t)((result) ^ (*(uint32_t *)(v_rip + 0xACB69E)));
    result = (result) >> (16);
    result = (result) + (local_rdi);
    Arg2 = (*(uint16_t *)(local_rdi + 0x2C)) << (6);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)(result)));
    local_rbx = ((uint32_t)(*(uint32_t *)(Arg2 + *(uint64_t *)(local_r10 + Arg1 * 1 + 0x18) * 1 + 0x48))) * ((uint32_t)(Arg3));
    local_rbx = (local_rbx) >> (32);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) * ((uint32_t)((uint16_t)(result))));
    if (Arg3 != ((uint32_t)(result))) goto loc_0035CB63;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r10 + Arg1 * 1 + 0x18) + 0x4C))))) >> (13));
    result = (uint32_t)((result) & (0x3FFFFULL));
    Arg3 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r10 + Arg1 * 1 + 0x18) + 0x4C))) >> (4);
    Arg3 = (uint32_t)((Arg3) & (511));
    Arg4 = (uint32_t)((1) << ((uint8_t)((uint16_t)(result))));
    Arg1 = (uint32_t)(((uint16_t)(result)) + (-2));
    Arg4 = (uint32_t)((Arg4) ^ ((uint32_t)(result)));
    v_stack_m148 = (uint32_t)(Arg1);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8BB0) + Arg1 * 8) + Arg4 * 8 + 0x8) + Arg3 * 8) == 0) goto loc_0035E94B;
loc_0035CCED:
    if (((uint16_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8BB0) + Arg1 * 8) + Arg4 * 8 + 0x8) + Arg3 * 8))) == (*(uint16_t *)(local_rdi + 0x2E))) goto loc_0035E8DE;
loc_0035CCF7:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (63));
    result = (local_rbx) >> (6);
    if (condition_is_above_or_equal) goto loc_0035D36D;
loc_0035CD1C:
    v_stack_m1C0 = *(uint64_t *)(local_rdi + 0x10);
    Arg1 = (*(uint64_t *)(local_rdi + 0x10)) >> (48);
    v_stack_m238 = *(uint64_t *)(local_rdi + 0x10);
    if (((uint8_t)(Arg1)) == 1) {
        v_stack_m232 = 2;
    }
    if (local_r14 != 0) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(local_r10 + Arg1 * 1 + 0x18) + 0x50);
        Arg1 = v_stack_m238;
        Arg2 = Arg3;
        *(uint16_t *)(local_r14) = (uint16_t)(Arg1);
        Arg2 = (uint32_t)((Arg2) ^ (*(uint32_t *)(local_r14)));
        Arg1 = (uint8_t)(Arg1);
        Arg1 = local_rbx + 1;
        Arg3 = (Arg3) >> (32);
        Arg2 = (uint32_t)((Arg2) ^ (Arg3));
        v_stack_m238 = (uint16_t)(Arg1);
        Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(local_r14)));
        *(uint32_t *)(local_r14 + 0x8) = (uint32_t)(Arg2);
    }
    Arg2 = (*(uint16_t *)(local_rdi + 0x2C)) << (6);
    if (condition_is_not_equal) goto loc_0035CD1C;
    if ((*(uint8_t *)(Arg2 + *(uint64_t *)(local_r10 + Arg1 * 1 + 0x18) * 1 + 0x5C)) == 0) goto loc_0035D3D5;
loc_0035CD8E:
    if (v_stack_m1BA != 1) goto loc_0035CB63;
    Arg4 = (uint32_t)((v_stack_m1BC) << (6));
    Arg4 = (Arg4) + (*(uint64_t *)(local_r10 + Arg1 * 1 + 0x18));
    Arg2 = (uint32_t)((*(uint64_t *)(Arg4 + 0x8)) & (0xFFFULL));
    Arg3 = (uint32_t)((*(uint64_t *)(local_rdi + 0x18)) & (0xFFFULL));
    Arg1 = (*(uint64_t *)(Arg4 + 0x8)) - (Arg2);
    Arg1 = (Arg1) | (Arg3);
    *(uint64_t *)(local_rdi + 0x18) = Arg1;
    Arg1 = (local_rdi) | (Arg2);
    if (condition_is_equal) goto loc_0035CB63;
loc_0035CDE3:
    Arg1 = (*(uint64_t *)(Arg4 + 0x8)) ^ (*(uint64_t *)(local_rdi + 0x18));
    Arg2 = (uint32_t)((*(uint64_t *)(Arg4 + 0x8)) & (0xFFFULL));
    Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (Arg1) ^ (*(uint64_t *)(local_rdi + 0x18));
    *(uint64_t *)(local_rdi + 0x18) = Arg1;
    Arg1 = (local_rdi) | (Arg2);
    if ((*(uint64_t *)(Arg4 + 0x8)) != (*(uint64_t *)(Arg4 + 0x8))) goto loc_0035CDE3;
    goto loc_0035CB63;
loc_0035CE19:
    Arg2 = (Arg2) | (1);
    v_stack_m238 = Arg2;
    goto loc_0035C860;
loc_0035CE27:
    goto loc_0035CA67;
loc_0035CE37:
    if (((uint32_t)(v_stack_m1FC) + 832) < (Arg1 + 48)) goto loc_0035CE67;
    result = ((uint32_t)(v_stack_m1FC) + 832) >> (39);
    result = (uint32_t)((result) & (511));
    result = (uint32_t)((result) + (0xFFFFFF00ULL));
    if (((uint8_t)(*(uint8_t *)(result + local_rdi * 1 + 0xE38AA8))) == 5) goto loc_0035F0BB;
loc_0035CE67:
loc_0035CE6D:
    v_stack_mC0 = (uint32_t)(v_stack_m1FC) + 832;
    v_stack_mB8 = (uint32_t)(v_stack_m1FC) + 832;
    v_stack_mB0 = (uint32_t)(v_stack_m1FC) + 832;
    if ((*(uint32_t *)(v_rip + 0xC69E8A)) != 0) goto loc_0035D3FC;
loc_0035CE9C:
    if (((*(uint8_t *)(v_rip + 0xC69C63)) & (33)) == 0) goto loc_0035D30A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB0FA9))) != 0) goto loc_0035D30A;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(v_rip + 12181046, 2, Arg1 + 32, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1FC) + 832)));
loc_0035CEC7:
    result = ((uint32_t)(v_stack_m1FC) + 832) >> (12);
    Arg1 = (v_rip + 12181046) * (result);
    result = (Arg1) >> (32);
    Arg1 = (Arg1) ^ (result);
    Arg2 = (uint32_t)((*(uint64_t *)(v_rip + 0xBA1E6A) - 1) & ((uint32_t)(Arg1)));
loc_0035CEF9:
    Arg1 = ((uint32_t)((uint32_t)(Arg2))) << (5);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xBA1E58));
    if ((*(uint64_t *)(Arg1)) == ((uint32_t)(v_stack_m1FC) + 832)) goto loc_0035D140;
    Arg2 = (uint32_t)((Arg2) + 1);
    if (((uint32_t)((uint32_t)(Arg2))) < (*(uint64_t *)(v_rip + 0xBA1E6A))) goto loc_0035CEF9;
    if (1 != 0) goto loc_0035E76A;
loc_0035CF20:
    v_stack_m248 = (uint32_t)(v_stack_m1FC) + 832;
    result = KeBugCheckEx(34 - 9, 34, (uint32_t)(v_stack_m1FC) + 832, 64);
loc_0035CF39:
    if ((((uint8_t)(result)) & (4)) != 0) {
        result = *(uint16_t *)(64);
        result = (uint16_t)((result) & (255));
        result = (uint16_t)(result);
        result = (result) << (4);
        Arg1 = (64) - (result);
    }
    Arg1 = (Arg1) ^ (*(uint64_t *)(Arg1 + 0x8));
    Arg1 = (Arg1) ^ (*(uint64_t *)(v_rip + 0xC6A2C7));
    if (condition_is_equal) goto loc_0035C800;
    if (Arg1 == -1) goto loc_0035C800;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBA1DA9))) != 0) goto loc_0035E793;
loc_0035CF7F:
    if (((uint32_t)(v_stack_m1FC) + 832) < ((uint32_t)(v_stack_m1FC) + 832)) goto loc_0035CFAF;
    result = ((uint32_t)(v_stack_m1FC) + 832) >> (39);
    result = (uint32_t)((result) & (511));
    result = (uint32_t)((result) + (0xFFFFFF00ULL));
    if (((uint8_t)(*(uint8_t *)(result + local_rdi * 1 + 0xE38AA8))) == 5) goto loc_0035F0A8;
loc_0035CFAF:
loc_0035CFB5:
    result = *(uint8_t *)(result + local_rdi * 1 + 0xE38AA8);
    if (((*(uint8_t *)((uint32_t)(v_stack_m1FC) + 0x340 - 0xD)) & (4)) != 0) {
        result = *(uint16_t *)((uint32_t)(v_stack_m1FC) + 0x340 - 0x10);
        result = (uint16_t)((result) & (255));
        result = (uint16_t)(result);
        result = (result) << (4);
        Arg2 = ((uint32_t)(v_stack_m1FC) + 832 - 16) - (result);
    }
    local_rbx = ((uint8_t)(*(uint16_t *)(Arg2 + 0x2))) << (4);
    result = (uint16_t)((*(uint16_t *)(Arg2 + 0x2)) >> (8));
    if ((((uint8_t)(result)) & (8)) == 0) goto loc_0035D136;
    local_rdi = (*(uint64_t *)(v_rip + 0xC6A235)) ^ (*(uint64_t *)(Arg2 + 0x8));
    result = (Arg2) ^ (*(uint64_t *)(v_rip + 0xC6A227));
    *(uint64_t *)(Arg2 + 0x8) = result;
    local_rdi = (local_rdi) ^ (Arg2);
    if (condition_is_equal) goto loc_0035D136;
    if (local_rdi == -1) goto loc_0035D136;
    if (local_rdi < ((uint32_t)(v_stack_m1FC) + 832)) goto loc_0035E68C;
    result = (uint8_t)((*(uint8_t *)(local_rdi)) & (127));
    if (((uint8_t)(result)) != 3) goto loc_0035E68C;
    local_r14 = (uint32_t)((64) & (256));
    if (local_rdi == (*(uint64_t *)(v_rip + 0xC69A74))) goto loc_0035D104;
    result = (local_r14 != 0) ? 1 : 0;
    local_r15 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) << (7);
    local_r15 = (local_r15) + (*(uint64_t *)(local_rdi + 0x2F8));
    v_stack_p8 = *(uint64_t *)(local_rdi + 0x2F8);
    if ((*(uint64_t *)(local_r15 + 0x50)) == 0) goto loc_0035D0A8;
    Arg3 = ((uint32_t)(v_stack_m1FC) + 832) * ((uint32_t)((uint32_t)(result)));
    if ((*(uint64_t *)(local_r15 + 0x40)) <= (*(uint64_t *)(local_r15))) goto loc_0035D0A8;
    Arg1 = (*(uint64_t *)(local_r15 + 0x40)) - (*(uint64_t *)(local_r15));
    if (Arg1 > (*(uint64_t *)(Arg3 + v_rip - 0x35D04C * 1 + 0xF06648))) goto loc_0035D5DD;
loc_0035D0A8:
    local_r10 = ((uint32_t)((uint32_t)(result))) << (7);
loc_0035D0B9:
    Arg3 = *(uint64_t *)(local_r15);
    if (local_rbx < (*(uint64_t *)(local_r15))) { Arg3 = local_rbx; }
    Arg1 = (*(uint64_t *)(local_r15)) - (local_rbx);
    Arg2 = 0;
    if (local_rbx < (*(uint64_t *)(local_r15))) { Arg2 = Arg1; }
    if (local_rbx != (*(uint64_t *)(local_r15))) goto loc_0035D0B9;
    local_rbx = (local_rbx) - (Arg3);
    if (condition_is_not_equal) goto loc_0035D9F7;
    if ((((uint8_t)(*(uint8_t *)(v_rip - 0x35D04C + (uint32_t)((uint32_t)(result)) * 8 + 0xFC7350))) & (4)) != 0) {
        Arg4 = -(local_rbx);
    }
    local_r13 = 0;
loc_0035D104:
    result = *(uint64_t *)(local_r15);
    if ((*(uint32_t *)(v_rip + 0xC67F05)) != 0) {
        Arg2 = 0;
        Arg1 = local_rdi - 48;
        Arg4 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x4)));
        Arg3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsi = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_0035DEA3;
loc_0035D136:
    goto loc_0035C800;
loc_0035D140:
    if (Arg1 == 0) goto loc_0035CF20;
    v_stack_mC0 = Arg4;
    v_stack_mB0 = v_rip + 13049776;
    v_stack_mB8 = Arg3;
    local_r14 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0xC))))) >> (8);
    local_r14 = (uint32_t)((local_r14) & (0xFFFULL));
    v_stack_m208 = *(uint64_t *)(Arg1 + 0x10);
    v_stack_m238 = local_r14;
    if (condition_is_below) goto loc_0035D38F;
loc_0035D19B:
    *(uint64_t *)(Arg1 + 0x18) = 0;
    if (((*(uint8_t *)(v_rip + 0xC69952)) & (1)) != 0) goto loc_0035DE3C;
loc_0035D1BA:
loc_0035D1CC:
    result = -1;
    if ((*(uint32_t *)(v_rip + 0xC69B4D)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(local_r15);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    if ((-1 - 1) <= -3) goto loc_0035D6D6;
loc_0035D1F8:
    goto loc_0035C8C6;
loc_0035D208:
    Arg4 = (Arg4) & (Arg3);
    v_stack_m190 = 0;
    Arg2 = (Arg3) - (Arg4);
    Arg2 = (Arg2) >> (5);
    result = (uint8_t)(((uint8_t)(v_rip + 11316942)) & (3));
    Arg2 = (Arg2) << ((uint8_t)((uint32_t)((uint32_t)(local_r10))));
    Arg2 = (Arg2) + (Arg4);
    if (((uint8_t)(result)) != 3) goto loc_0035CB46;
    if (v_stack_p10 == Arg2) goto loc_0035D35D;
    if (((uint8_t)(v_rip + 11316942)) != 15) goto loc_0035CB46;
    if (v_stack_p10 <= Arg2) goto loc_0035D35D;
    result = RtlpHpVsContextFree(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)) + 0x20), Arg2, v_stack_p10, v_stack_m190);
    if ((uint32_t)(result) == 0) goto loc_0035CB63;
    if (((uint32_t)((uint32_t)(v_stack_m190))) >= ((uint32_t)(*(uint16_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)) + 0x18) + 0x44)))) goto loc_0035CB63;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m190)) + (15));
    Arg1 = (Arg1) >> (4);
    local_r10 = (uint32_t)((*(uint8_t *)(Arg1 + - 0x1 * 1 + 0x10B80)) - 1);
loc_0035D28F:
    v_stack_m1A0 = *(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)) + 0x18) + local_r10 * 8 + 0x1C0);
    result = (*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)) + 0x18) + local_r10 * 8 + 0x1C0)) >> (16);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)) + 0x18) + local_r10 * 8 + 0x1C0))) & (1)) == 0) goto loc_0035D2CB;
    if (((uint16_t)(result)) >= = 1) {
        result = (uint16_t)((result) - 1);
        v_stack_m19E = (uint16_t)(result);
        Arg2 = v_stack_m1A0;
    }
    if ((*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)) + 0x18) + local_r10 * 8 + 0x1C0)) != (*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)) + 0x18) + local_r10 * 8 + 0x1C0))) goto loc_0035D28F;
loc_0035D2CB:
    goto loc_0035CB63;
loc_0035D2D8:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB0B7A))) != 0) goto loc_0035C9CB;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m138, *(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)) + 0x18) + local_r10 * 8 + 0x1C0), *(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)) + 0x18), *(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)) + 0x18) + local_r10 * 8);
    goto loc_0035C9DF;
loc_0035D2F7:
    goto loc_0035CB8F;
loc_0035D30A:
loc_0035D31B:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB0B7A))) == 0) goto loc_0035CEC7;
    if (!sign_flag) goto loc_0035D31B;
    result = ExpWaitForSpinLockSharedAndAcquire(v_rip + 12179901, (uint8_t)(v_stack_m208), 1, *(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)) + 0x18) + local_r10 * 8);
    goto loc_0035CEC7;
loc_0035D345:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p10), (uint8_t)(result), 1, *(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)) + 0x18) + local_r10 * 8);
    goto loc_0035C9BA;
loc_0035D35D:
    result = RtlpHpSegPageRangeShrink((uint32_t)(*(uint32_t *)(Arg1 + 0x8)), 1, 1, *(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)) + 0x18) + local_r10 * 8);
    goto loc_0035CB63;
loc_0035D36D:
    v_stack_m240 = 0;
    v_stack_m248 = 1;
    result = RtlpLogHeapFailure(17, *(uint64_t *)(- 0x1), v_stack_p10, v_stack_p10);
    goto loc_0035CB63;
loc_0035D38F:
    local_rdi = (*(uint64_t *)(17 + 0x18)) ^ (*(uint64_t *)(v_rip + 0xC69E8E));
    local_rdi = (local_rdi) ^ (v_stack_p10);
    goto loc_0035D19B;
loc_0035D3A2:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBA19B7) + 0x11 * 8))) == 0) goto loc_0035C976;
    *(uint32_t *)(v_stack_p10) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBA19B7) + 0x11 * 8)));
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA19A2) + 0x11 * 8 + 0x48) == 0) goto loc_0035C955;
    *(uint64_t *)(v_stack_p10 + 0x48) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBA19A2) + 0x11 * 8 + 0x48);
    goto loc_0035C955;
loc_0035D3D5:
    *(uint8_t *)(*(uint64_t *)(- 0x1) + - 0x1 * 1 + 0x5C) = 1;
    result = RtlpHpEnvCompactionIsScheduled(*(uint64_t *)(*(uint64_t *)(- 0x1) + 0x38), *(uint64_t *)(- 0x1), v_stack_p10, v_stack_p10);
    if ((uint32_t)(result) != 0) goto loc_0035CD8E;
    result = RtlpHpEnvCompactionSchedule(*(uint64_t *)(*(uint64_t *)(- 0x1) + 0x38), *(uint64_t *)(- 0x1), v_stack_p10, v_stack_p10);
    goto loc_0035CD8E;
loc_0035D3FC:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_m208), (uint8_t)(result), v_stack_p10, v_stack_p10);
    goto loc_0035CE9C;
loc_0035D40D:
    goto loc_0035C4CE;
loc_0035D418:
    result = 0;
    v_stack_mF0 = 0;
    v_stack_m22F = 0;
    v_stack_m20F = 0;
    v_stack_p10 = v_stack_m1F8;
    v_stack_m1D4 = -1;
    v_stack_m100 = v_xmm0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC67D18))))) {
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC696B7)))) & (65)) != 0) goto loc_0035E7B8;
loc_0035D455:
    local_r12 = (v_stack_p10) & (-5);
    v_stack_m1A0 = *(uint64_t *)(v_rip + 0xBA18F1);
    v_stack_m1B8 = *(uint64_t *)(v_rip + 0xBA18DE);
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))))) * ((uint32_t)(*(uint32_t *)(Arg1 + 0x8)));
    v_stack_m1E0 = *(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20);
    local_rsi = (Arg1) >> (32);
    local_rsi = (uint32_t)((local_rsi) ^ ((uint32_t)(Arg1)));
    local_rsi = (uint32_t)((local_rsi) & ((uint32_t)(*(uint64_t *)(v_rip + 0xBA18F1))));
    v_stack_p8 = (uint32_t)(local_rsi);
loc_0035D4AA:
    local_r15 = ((uint32_t)((uint32_t)(local_rsi)) + (uint32_t)((uint32_t)(local_rsi)) * 4) << (4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x8))))) goto loc_0035D633;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x8))))) goto loc_0035DC0E;
loc_0035D4E0:
    v_stack_p8 = 1;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1 + 0x48)) == 0) goto loc_0035D662;
loc_0035D50B:
loc_0035D50F:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1 + (int32_t)(1) * 8 + 0x38))) & (1)) != 0) goto loc_0035D662;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1 + (int32_t)(1) * 8 + 0x38)) >= v_stack_p10) goto loc_0035D662;
    result = ExpTrackTableGetMoreLimit(*(uint64_t *)(*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1 + 0x48), v_stack_p10, 1, v_stack_p10);
    if (result == 0) goto loc_0035F463;
    if (result != 1) goto loc_0035E775;
    if (result == 1) goto loc_0035D662;
    goto loc_0035D50B;
loc_0035D567:
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1 + (int32_t)(1) * 8 + 0x38)) - (*(uint64_t *)(v_rip + 0xB0B090));
    Arg2 = (Arg2) >> (20);
    Arg2 = (Arg2) + (Arg2);
    result = RtlCSparseBitmapBitmaskRead(v_rip + 11579551, Arg2, 1, v_stack_p10);
    if (result == 0) goto loc_0035D594;
    result = (uint32_t)((result) - 1);
    if (((uint32_t)(result)) != 2) goto loc_0035BEBD;
loc_0035D594:
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    result = RtlpHpVaMgrCtxQuery(v_rip + 11579568, *(uint64_t *)(*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1 + (int32_t)(1) * 8 + 0x38), v_stack_m90, v_stack_p10);
    v_stack_m58 = v_stack_m80;
    v_stack_mD0 = (uint32_t)((uint32_t)(v_stack_m78));
    goto loc_0035BEFB;
loc_0035D5DD:
    Arg2 = *(uint64_t *)(*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1 + (int32_t)(1) * 8 + 0x38);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1 + (int32_t)(1) * 8 + 0x38)) > (*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1 + 8)) { Arg2 = *(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1 + 8; }
    Arg1 = ((uint32_t)(v_stack_m78)) - (Arg2);
    if (condition_is_not_equal) goto loc_0035D0A8;
    Arg2 = (Arg2) + (Arg2);
    if (Arg2 <= (*(uint64_t *)(v_stack_m90 + v_stack_p10 * 1 + 0xF06648))) goto loc_0035D0A8;
    Arg3 = 0;
    if (0 == 0) goto loc_0035D0A8;
    Arg4 = 0;
    result = PspReturnResourceQuota((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1 + (int32_t)(1) * 8 + 0x38))), *(uint64_t *)(v_stack_m80), Arg3, Arg4);
    goto loc_0035D0A8;
loc_0035D633:
    if ((uint32_t)(result) == 0) goto loc_0035D9B6;
loc_0035D63B:
    result = (uint32_t)((v_stack_p10 + 1) & ((uint32_t)(*(uint64_t *)(v_stack_m80))));
    if (((uint32_t)(result)) != 0) goto loc_0035D4AA;
    result = ExpInsertPoolTrackerExpansion((uint32_t)((uint32_t)(*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1 + 8)), v_stack_p10, *(uint64_t *)(*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1 + (int32_t)(1) * 8 + 0x38), Arg4);
loc_0035D662:
loc_0035D665:
    v_stack_p10 = local_rdi;
    local_rdi = 0;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xC715FC)) != 0) goto loc_0035E3F9;
loc_0035D68A:
    Arg4 = (0) & (-8);
    local_r13 = (local_r13) - (Arg4);
    Arg1 = (0) - (Arg4);
    Arg1 = (Arg1) + (v_stack_m1F8);
    local_r13 = (local_r13) + (0);
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xC715FC)) == 0) goto loc_0035BBCD;
    if (Arg4 >= v_stack_p10) goto loc_0035F41A;
    v_stack_m248 = 0;
    result = KeBugCheckEx(497, 2, 1, Arg4);
loc_0035D6C8:
    result = KxWaitForLockOwnerShip(v_stack_m138, 2, 1, Arg4);
    goto loc_0035C9DF;
loc_0035D6D6:
    Arg1 = (uint32_t)((*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1) & (256));
    if (0 == (*(uint64_t *)(v_rip + 0xC693CA))) goto loc_0035D7BA;
    result = (Arg1 != 0) ? 1 : 0;
    local_r14 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) << (7);
    local_r14 = (local_r14) + (*(uint64_t *)(local_rdi + 0x2F8));
    v_stack_p8 = (uint8_t)(*(uint8_t *)(v_rip - 0x35D6F6 + (uint32_t)((uint32_t)(result)) * 8 + 0xFC7350));
    if ((*(uint64_t *)(local_r14 + 0x50)) == 0) goto loc_0035D751;
    Arg3 = (1) * ((uint32_t)((uint32_t)(result)));
    if ((*(uint64_t *)(local_r14 + 0x40)) <= (*(uint64_t *)(local_r14))) goto loc_0035D751;
    Arg1 = (*(uint64_t *)(local_r14 + 0x40)) - (*(uint64_t *)(local_r14));
    if (Arg1 > (*(uint64_t *)(Arg3 + v_rip - 0x35D6F6 * 1 + 0xF06648))) goto loc_0035DA49;
loc_0035D751:
    local_r10 = ((uint32_t)((uint32_t)(result))) << (7);
loc_0035D764:
    Arg3 = *(uint64_t *)(local_r14);
    if (v_stack_m208 < (*(uint64_t *)(local_r14))) { Arg3 = v_stack_m208; }
    Arg1 = (*(uint64_t *)(local_r14)) - (v_stack_m208);
    Arg2 = 0;
    if (v_stack_m208 < (*(uint64_t *)(local_r14))) { Arg2 = Arg1; }
    if (v_stack_m208 != (*(uint64_t *)(local_r14))) goto loc_0035D764;
    Arg4 = (v_stack_m208) - (Arg3);
    if (condition_is_not_equal) goto loc_0035DED0;
    result = *(uint64_t *)(local_r14);
    if (((v_stack_p8) & (4)) != 0) {
        result = v_stack_m208;
        Arg1 = local_rdi + (uint32_t)((uint32_t)(result)) * 8;
        result = -(result);
    }
    local_r13 = 0;
loc_0035D7BA:
    if ((*(uint32_t *)(v_rip + 0xC6784F)) != 0) {
        Arg2 = 0;
        Arg1 = local_rdi - 48;
        Arg4 = (uint32_t)(*(uint64_t *)(v_rip - 0x35D47B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + local_r15 * 1 + 8);
        Arg3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsi = ((uint32_t)((uint32_t)(result))) - (1);
    if (condition_is_greater) goto loc_0035D1F8;
    if (*(uint64_t *)(local_rdi - 0x28) != 0) goto loc_0035E977;
    if (!sign_flag) goto loc_0035EA09;
    Arg2 = 0;
    v_stack_m248 = local_rsi;
    result = KeBugCheckEx(Arg2 + 24, Arg2, 0, *(uint64_t *)(local_rdi - 0x28) + 4);
loc_0035D812:
    local_rsi = (local_rsi) + ((uint32_t)(*(uint32_t *)(v_rip + 0xC69468)));
    if (local_rsi <= 0xFE0ULL) goto loc_0035C187;
    local_rsi = (local_rsi) - ((uint32_t)(*(uint32_t *)(v_rip + 0xC69468)));
    local_r11 = (v_rip + 11315235) & (-9);
    v_stack_m1F0 = local_r11;
    goto loc_0035C187;
loc_0035D839:
    v_stack_m200 = 1;
    goto loc_0035C2BA;
loc_0035D849:
    if (((uint32_t)(*(uint64_t *)(local_r14))) == 0x80000000ULL) goto loc_0035BB23;
    goto loc_0035BB3B;
loc_0035D85B:
    v_stack_m200 = (uint32_t)(local_r10);
    v_stack_m1B0 = (uint32_t)(*(uint32_t *)(v_rip + 0xC69468));
    goto loc_0035C5DF;
loc_0035D86C:
    local_rsi = (local_rsi) + (0xFFFULL);
    local_rsi = (local_rsi) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m1F8 = local_rsi;
    goto loc_0035BBB7;
loc_0035D884:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m138, Arg2, 0, *(uint64_t *)(local_rdi - 0x28) + 4);
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xBA14B4))) - 1);
    Arg1 = (Arg3 + Arg3 * 4) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip - 0x35D8A8 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20));
    result = -(*(uint64_t *)(local_r14));
    if (condition_is_below) goto loc_0035D9A7;
    goto loc_0035CA8A;
loc_0035D8DB:
loc_0035D8E2:
    result = RtlpHpLfhSlotAllocateSlow(*(uint64_t *)(local_r14) + 832, *(uint64_t *)(v_rip - 0x35D8A8 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20), (uint32_t)((uint32_t)(local_rsi)), (uint32_t)((uint32_t)(local_r14)));
loc_0035D8F5:
    if (result == -1) goto loc_0035D943;
loc_0035D8FB:
    if (result == 0) goto loc_0035D91E;
loc_0035D905:
    Arg1 = ((((uint8_t)(v_stack_m1F0)) & (16)) == 0) ? 1 : 0;
    result = ((((uint8_t)(v_stack_m1F0)) & (16)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0035DEF4;
loc_0035D91E:
    local_r12 = 0;
    v_stack_p10 = 0;
    goto loc_0035C16F;
loc_0035D92D:
    result = RtlpHpLfhBucketCheckAndUpdate(v_stack_m1F0, *(uint64_t *)(v_rip - 0x35D8A8 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20), (uint32_t)((uint32_t)(local_rsi)), (uint32_t)((uint32_t)(local_r14)));
    if (result != 0) goto loc_0035DC78;
loc_0035D943:
loc_0035D947:
    if (v_stack_m1A8 > 0x20000ULL) goto loc_0035E929;
    result = RtlpHpVsContextAllocate(*(uint64_t *)(local_r14) + 704, (uint32_t)((uint32_t)(v_stack_m228)), (uint32_t)((uint32_t)(v_stack_m1A8)), (uint32_t)((uint32_t)(local_r14)));
loc_0035D969:
    goto loc_0035D8FB;
loc_0035D96E:
    result = RtlpHpLfhBucketCheckAndUpdate(v_stack_m1F0, (uint32_t)((uint32_t)(v_stack_m228)), (uint32_t)((uint32_t)(v_stack_m1A8)), (uint32_t)((uint32_t)(local_r14)));
    if (result != 0) goto loc_0035DD0F;
loc_0035D97F:
loc_0035D984:
    if (result > 0x20000ULL) goto loc_0035E958;
    result = RtlpHpVsContextAllocate(*(uint64_t *)(local_r14) + 704, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r14)));
    goto loc_0035C128;
loc_0035D9A7:
    goto loc_0035CA8A;
loc_0035D9B6:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r14) + *(uint64_t *)(v_rip + 0xBA13A3) * 1))) == 0) goto loc_0035DAAF;
    *(uint32_t *)(local_r14) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r14) + *(uint64_t *)(v_rip + 0xBA13A3) * 1)));
    if (*(uint64_t *)(*(uint64_t *)(local_r14) + *(uint64_t *)(v_rip + 0xBA138C) * 1 + 0x48) == 0) goto loc_0035D4AA;
    *(uint64_t *)(local_r14 + 0x48) = *(uint64_t *)(*(uint64_t *)(local_r14) + *(uint64_t *)(v_rip + 0xBA138C) * 1 + 0x48);
    goto loc_0035D4AA;
loc_0035D9EB:
    local_rsi = (result) + (192);
    goto loc_0035BC2A;
loc_0035D9F7:
    if (v_stack_p8 != v_stack_m1F0) goto loc_0035DDA3;
    v_stack_m248 = (uint32_t)((uint32_t)(result));
    result = KeBugCheckEx(33, result, v_stack_m228, (uint32_t)((uint32_t)(local_r14)));
loc_0035DA1A:
    if (local_r14 >= result) goto loc_0035F14B;
    v_stack_m248 = 0;
    result = KeBugCheckEx(497, 2, 2 - 1, local_r14);
loc_0035DA49:
    Arg2 = 2;
    if (2 > v_stack_m208) { Arg2 = v_stack_m208; }
    Arg1 = (result) - (Arg2);
    if (condition_is_not_equal) goto loc_0035D751;
    Arg2 = (Arg2) + (Arg2);
    if (Arg2 <= (*(uint64_t *)(2 - 0x1 + local_r14 * 1 + 0xF06648))) goto loc_0035D751;
    Arg3 = 0;
    if (0 == 0) goto loc_0035D751;
    Arg4 = 0;
    result = PspReturnResourceQuota((uint32_t)((uint32_t)(v_stack_m228)), local_r14, Arg3, Arg4);
    goto loc_0035D751;
loc_0035DAA3:
    local_rbx = ((uint32_t)((uint32_t)(result))) + (192);
    goto loc_0035CB26;
loc_0035DAAF:
    if (((uint32_t)((uint32_t)(v_stack_m228))) == (v_stack_m1F0 - 1)) goto loc_0035D63B;
    v_stack_m100 = 0;
    v_stack_mF8 = v_rip + 12177981;
    v_stack_m218 = (uint8_t)(local_r15);
    if ((*(uint32_t *)(v_rip + 0xC69237)) != 0) goto loc_0035DE62;
loc_0035DAEF:
    v_stack_mF0 = (uint8_t)((uint8_t)(local_r15));
    if (((*(uint8_t *)(v_rip + 0xC69010)) & (33)) != 0) goto loc_0035DD6E;
loc_0035DAFF:
    if (v_stack_m100 != 0) goto loc_0035E41A;
loc_0035DB13:
    result = (*(uint64_t *)(v_rip + 0xBA1246)) + (*(uint64_t *)(local_r14));
    v_stack_m218 = result;
    if ((*(uint32_t *)(result)) == 0) {
        Arg1 = (uint32_t)(local_rbx);
        result = ExpPlFindLimitEntry(Arg1, v_stack_m100, Arg3, Arg4);
        Arg1 = v_stack_m218;
        *(uint64_t *)(Arg1 + 0x48) = result;
        *(uint64_t *)(local_r14 + 0x48) = result;
        result = *(uint64_t *)(v_rip + 0xBA121E);
        *(uint32_t *)(*(uint64_t *)(local_r14) + result * 1) = (uint32_t)(local_rbx);
        *(uint32_t *)(local_r14) = (uint32_t)(local_rbx);
    }
    result = KeReleaseInStackQueuedSpinLock(v_stack_m100, v_stack_m100, Arg3, Arg4);
    goto loc_0035D4AA;
loc_0035DB6A:
    Arg2 = ~(v_stack_m1A0);
    if (Arg2 != 0) goto loc_0035C39B;
    if (((uint32_t)(v_stack_p8)) == v_stack_m1B8) goto loc_0035DD9B;
    Arg3 = ((uint32_t)(v_stack_p8)) + (8);
    goto loc_0035C38C;
loc_0035DB97:
    result = (uint32_t)((result) * ((uint32_t)((uint32_t)(v_stack_p10))));
    result = (uint32_t)((result) >> (8));
    goto loc_0035C3D9;
loc_0035DBBC:
    Arg2 = ~(Arg2);
    if (Arg2 != 0) goto loc_0035C6B7;
    if (Arg3 == v_stack_m1A8) goto loc_0035DDBA;
    Arg3 = (Arg3) + (8);
    goto loc_0035C6A8;
loc_0035DBE9:
    result = (uint32_t)((result) * ((uint32_t)((uint32_t)(v_stack_p10))));
    result = (uint32_t)((result) >> (8));
    goto loc_0035C6FA;
loc_0035DC0E:
    Arg1 = 0;
    goto loc_0035D4E0;
loc_0035DC1D:
    Arg4 = 0;
    if (((uint32_t)((uint32_t)(v_stack_p10))) == -1) goto loc_0035EA17;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))) >> (6));
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p10)) & (63));
loc_0035DC50:
    Arg1 = (*(uint64_t *)(v_stack_m1B8 + result * 8 + 0x40)) & (-2);
    if (condition_is_not_equal) goto loc_0035DC50;
loc_0035DC63:
loc_0035DC78:
    Arg1 = (v_stack_m1B4) << (8);
    Arg1 = (Arg1) + (0x5C0ULL);
    Arg1 = (Arg1) + (*(uint64_t *)(local_r14) + 832);
    if (v_stack_p10 == Arg1) goto loc_0035C286;
    *(uint16_t *)(v_stack_m218) = (uint16_t)(*(uint16_t *)(Arg1 + v_stack_p8 * 1));
    goto loc_0035C286;
loc_0035DCB9:
    Arg4 = 0;
    if (((uint32_t)((uint32_t)(v_stack_p10))) == -1) goto loc_0035C78C;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))) >> (6));
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p10)) & (63));
loc_0035DCEC:
    Arg1 = (*(uint64_t *)(v_stack_m1A8 + result * 8 + 0x40)) & (-2);
    if (condition_is_not_equal) goto loc_0035DCEC;
loc_0035DCFA:
loc_0035DD0F:
    Arg1 = (v_stack_m1A4) << (8);
    Arg1 = (Arg1) + (0x5C0ULL);
    Arg1 = (Arg1) + (*(uint64_t *)(local_r14) + 832);
    if (2 == Arg1) goto loc_0035C5AB;
    *(uint16_t *)(v_stack_p8 + 0x2 * 1) = (uint16_t)(*(uint16_t *)(v_stack_p8 + Arg1 * 1));
    goto loc_0035C5AB;
loc_0035DD48:
    if (((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_p8 + Arg1 * 1)))) == v_stack_m1A8) goto loc_0035DD9B;
    Arg3 = ((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_p8 + Arg1 * 1)))) + (8);
    goto loc_0035C38C;
loc_0035DD56:
    result = RtlpHpLfhSlotAllocateSlow(*(uint64_t *)(local_r14) + 832, *(uint16_t *)(v_stack_p8 + Arg1 * 1), 0, (uint32_t)((uint32_t)(local_r14)));
    goto loc_0035C7A9;
loc_0035DD6E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB00E4))) != 0) goto loc_0035DAFF;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m100, *(uint64_t *)(local_r14) + 832, 0, (uint32_t)((uint32_t)(local_r14)));
    goto loc_0035DB13;
loc_0035DD8D:
    if (0 == v_stack_m1A8) goto loc_0035DDBA;
    Arg3 = (0) + (8);
    goto loc_0035C6A8;
loc_0035DD9B:
    goto loc_0035C38C;
loc_0035DDA3:
    v_stack_p8 = *(uint64_t *)(local_r14) + 832;
    goto loc_0035D0B9;
loc_0035DDBA:
    goto loc_0035C6A8;
loc_0035DDC2:
    if (*(uint64_t *)(local_r14) + 832 == 0) goto loc_0035CAD8;
    result = (uint32_t)((v_stack_m1A8 + *(uint64_t *)(local_r14) + 832 * 1 + 15) >> (4));
    Arg1 = (uint32_t)((*(uint8_t *)(result + 0x0 * 1 + 0x10B80)) + (-33));
    Arg1 = (Arg1) + 1;
    Arg1 = (Arg1) << (6);
    Arg1 = (Arg1) + (*(uint64_t *)(local_r14) + 832);
    if ((*(uint16_t *)(Arg1)) >= ((uint16_t)(*(uint16_t *)(Arg1 + 0x10)))) goto loc_0035DE0D;
    result = ExpInterlockedPushEntrySList(Arg1, *(uint64_t *)(v_stack_m1A8 + *(uint64_t *)(local_r14) + 0x340 * 1), v_stack_m100, (uint32_t)((uint32_t)(local_r14)));
loc_0035DE00:
    if (1 == 0) goto loc_0035CAD8;
    goto loc_0035CB63;
loc_0035DE0D:
    goto loc_0035DE00;
loc_0035DE15:
    if (((uint32_t)(Arg1)) <= ((uint32_t)(*(uint16_t *)(*(uint64_t *)(local_r14) + 0x340 + 0x30)))) goto loc_0035C44F;
    result = RtlpHpLfhSubsegmentPrefetch(v_stack_m1A8 + *(uint64_t *)(local_r14) + 832 * 1 + 832, *(uint64_t *)(local_r14) + 832, 0, (uint32_t)((uint32_t)(local_r14)));
    goto loc_0035C44F;
loc_0035DE3C:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB0016))) != 0) goto loc_0035D1BA;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(v_rip + 12177056, v_stack_p0, 0, (uint32_t)((uint32_t)(local_r14)));
    goto loc_0035D1CC;
loc_0035DE62:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(result), v_stack_p0, 0, (uint32_t)((uint32_t)(local_r14)));
    goto loc_0035DAEF;
loc_0035DE7B:
    if (((uint32_t)(v_rip + 12177034)) <= ((uint32_t)(*(uint16_t *)(v_stack_m238 + 0x30)))) goto loc_0035C76D;
    result = RtlpHpLfhSubsegmentPrefetch(*(uint64_t *)(local_r14) + 832, v_stack_m238, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r14)));
    goto loc_0035C76D;
loc_0035DEA3:
    if (*(uint64_t *)(result - 0x28) != 0) goto loc_0035E480;
    if (!sign_flag) goto loc_0035E9F6;
    Arg2 = 0;
    v_stack_m248 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, result, *(uint64_t *)(result - 0x28) + 4);
loc_0035DED0:
    if (0 != (*(uint64_t *)(local_r14) + 832)) goto loc_0035E6AF;
    v_stack_m248 = *(uint64_t *)(result - 0x28) + 4;
    result = KeBugCheckEx(33, result, *(uint64_t *)(local_r14) + 832, v_stack_m208);
loc_0035DEF4:
    result = (uint32_t)((*(uint64_t *)(local_r14) + 832) & (448));
    if (result != 256) goto loc_0035E23A;
    Arg2 = 1;
    if ((((uint8_t)(*(uint64_t *)(local_r14) + 832)) & (16)) != 0) { Arg2 = (uint32_t)((uint32_t)(0x80000001ULL)); }
loc_0035DF19:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) | (32));
    if ((((uint8_t)(*(uint64_t *)(local_r14) + 832)) & (4)) == 0) { Arg1 = (uint32_t)(Arg2); }
    Arg3 = (uint32_t)((uint32_t)(Arg1));
    if ((((uint8_t)(*(uint64_t *)(local_r14) + 832)) & (2)) != 0) { Arg3 = (uint32_t)(Arg1); }
    if ((((uint32_t)(0x80000001ULL)) & (*(uint64_t *)(local_r14) + 832)) == 0) goto loc_0035DF97;
    Arg1 = (uint32_t)(((uint32_t)(Arg3)) | (4));
    if ((((uint8_t)(*(uint64_t *)(local_r14) + 832)) & (8)) == 0) { Arg1 = Arg3; }
    result = (uint32_t)((*(uint64_t *)(local_r14) + 832) & (512));
    Arg2 = (uint32_t)((uint32_t)(Arg1));
    if (result == 0) { Arg2 = (uint32_t)(Arg1); }
    result = (uint32_t)((*(uint64_t *)(local_r14) + 832) & (0x400ULL));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) | (64));
    if (result == 0) { Arg1 = (uint32_t)(Arg2); }
    result = (uint32_t)((*(uint64_t *)(local_r14) + 832) & (32));
    if ((((uint8_t)(*(uint64_t *)(local_r14) + 832)) & (1)) == 0) goto loc_0035E24E;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (8));
    if (result != 0) { Arg3 = (uint32_t)(Arg1); }
loc_0035DF97:
    *(uint32_t *)(0 + 0x4) = 0;
    *(uint8_t *)(0) = 0;
    result = (v_stack_m1F8) >> (4);
    *(uint8_t *)(0 + 0x2) = (uint8_t)(result);
    result = (uint8_t)(((uint8_t)(Arg3)) | (8));
    Arg2 = (uint8_t)(result);
    if ((((uint8_t)(*(uint64_t *)(local_r14) + 832)) & (1)) == 0) { Arg2 = (uint32_t)((uint8_t)(Arg3)); }
    result = 0;
    Arg2 = (uint8_t)((Arg2) & (109));
    v_stack_m1D0 = 0;
    Arg2 = (uint8_t)((Arg2) | (2));
    v_stack_m22E = 0;
    *(uint8_t *)(0 + 0x3) = (uint8_t)(Arg2);
    local_r14 = (uint32_t)((*(uint64_t *)(local_r14) + 832) & (973));
    v_stack_mD8 = 0;
    v_stack_m20E = 0;
    v_stack_p10 = v_stack_m1F8;
    v_stack_mE8 = v_xmm0;
    if (0 == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC6715A))))) {
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC68AF9)))) & (65)) != 0) goto loc_0035E4C3;
loc_0035E013:
    local_r14 = (local_r14) & (-5);
    v_stack_m1E0 = *(uint64_t *)(v_rip + 0xBA0D23);
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))))) * (0);
    v_stack_m1A0 = *(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20);
    local_rdi = (Arg1) >> (32);
    local_rdi = (uint32_t)((local_rdi) ^ ((uint32_t)(Arg1)));
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)(*(uint64_t *)(v_rip + 0xBA0D32))));
    v_stack_p8 = (uint32_t)(local_rdi);
loc_0035E064:
    Arg1 = ((uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4) + ((uint32_t)((uint32_t)(local_rdi)) + (uint32_t)((uint32_t)(local_rdi)) * 4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8)))) != 0) goto loc_0035E114;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8)))) < 0) goto loc_0035E37A;
loc_0035E099:
    v_stack_p8 = 1;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8 + 0x48)) == 0) goto loc_0035E144;
loc_0035E0C4:
loc_0035E0C8:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8 + (int32_t)(1) * 8 + 0x38))) & (1)) != 0) goto loc_0035E144;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8 + (int32_t)(1) * 8 + 0x38)) >= v_stack_p10) goto loc_0035E144;
    result = ExpTrackTableGetMoreLimit(*(uint64_t *)(*(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8 + 0x48), v_stack_p10, 1, v_stack_p10);
    if (result == 0) goto loc_0035F48D;
    if (result != 1) goto loc_0035E428;
    if (result == 1) goto loc_0035E144;
    goto loc_0035E0C4;
loc_0035E114:
    if ((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8 + (int32_t)(1) * 8 + 0x38)) == 0) goto loc_0035E260;
loc_0035E11C:
    result = (uint32_t)((*(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8 + 8 + 1) & ((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8 + (int32_t)(1) * 8 + 0x38))));
    if (((uint32_t)(result)) != ((uint32_t)(v_stack_p10))) goto loc_0035E064;
    result = ExpInsertPoolTrackerExpansion((uint32_t)((uint32_t)(v_stack_p10)), v_stack_p10, *(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8 + (int32_t)(1) * 8, v_stack_p10);
loc_0035E144:
    local_r10 = 0;
loc_0035E14A:
    if (((v_stack_m1F0) & (8)) == 0) goto loc_0035E1BD;
    Arg1 = (uint32_t)(((uint32_t)(0xFFFFFFF0ULL)) - (0));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xC68B1D))) - 1);
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    if (condition_is_equal) goto loc_0035E1BD;
    Arg2 = ((uint32_t)((uint32_t)(Arg1))) + (0);
    Arg1 = (Arg2) - (0);
    Arg1 = (Arg1) >> (4);
    *(uint8_t *)(Arg2) = (uint8_t)(Arg1);
    result = (uint8_t)((*(uint8_t *)(0 + 0x2)) - ((uint8_t)(Arg1)));
    *(uint8_t *)(Arg2 + 0x2) = (uint8_t)(result);
    *(uint8_t *)(Arg2 + 0x1) = (uint8_t)(*(uint8_t *)(0 + 0x1));
    result = (uint8_t)((*(uint8_t *)(0 + 0x3)) | (4));
    *(uint8_t *)(Arg2 + 0x3) = (uint8_t)(result);
    *(uint32_t *)(Arg2 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x4)));
    result = (uint16_t)((*(uint16_t *)(Arg2)) & (255));
    if (((uint16_t)(result)) >= = 1) {
        result = Arg2;
        result = (result) ^ (*(uint64_t *)(v_rip + 0xC69072));
        *(uint64_t *)(0 + 0x10) = result;
    }
loc_0035E1BD:
    result = (Arg2 + 16) - (0);
    v_stack_p10 = Arg2 + 16;
    result = (uint32_t)((result) & (7));
    Arg1 = (Arg2 + 16) - (result);
    Arg3 = (Arg1) - (0);
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xC70AA4)) != 0) goto loc_0035E3C4;
loc_0035E1FE:
    Arg4 = (Arg2 + 16) & (-8);
    local_r13 = (local_r13) - (Arg4);
    local_rsi = (v_stack_m1F8) - (Arg4);
    local_r13 = (local_r13) + (Arg2 + 16);
    local_rsi = (local_rsi) + (0);
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xC70AA4)) == 0) goto loc_0035BBCD;
    if (Arg4 >= (*(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8 + (int32_t)(1) * 8)) goto loc_0035F358;
    v_stack_m248 = 0;
    result = KeBugCheckEx(497, 2, 1, Arg4);
loc_0035E23A:
    result = (result) - (64);
    if (condition_is_not_equal) goto loc_0035E369;
    goto loc_0035DF19;
loc_0035E24E:
    if (result == 0) goto loc_0035DF97;
    Arg3 = (uint32_t)((1) | (16));
    goto loc_0035DF97;
loc_0035E260:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBA0AF9) + 0x1F1 * 8))) == 0) goto loc_0035E291;
    *(uint32_t *)(1) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBA0AF9) + 0x1F1 * 8)));
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA0AE6) + 0x1F1 * 8 + 0x48) == 0) goto loc_0035E064;
    *(uint64_t *)(1 + 0x48) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBA0AE6) + 0x1F1 * 8 + 0x48);
    goto loc_0035E064;
loc_0035E291:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA0AE6) + 0x1F1 * 8 + 0x48)) == (local_r10 - 1)) goto loc_0035E11C;
    v_stack_mE8 = 0;
    v_stack_mE0 = v_rip + 12175963;
    v_stack_m218 = 2;
    if ((*(uint32_t *)(v_rip + 0xC68A4F)) != 0) goto loc_0035E3AB;
loc_0035E2D7:
    v_stack_mD8 = 2;
    if (((*(uint8_t *)(v_rip + 0xC68828)) & (33)) != 0) goto loc_0035E389;
loc_0035E2EA:
    if (v_stack_mE8 != 0) goto loc_0035E3E8;
loc_0035E301:
    Arg1 = (0 + 0 * 4) << (4);
    result = (*(uint64_t *)(v_rip + 0xBA0A52)) + (Arg1);
    v_stack_m218 = result;
    if ((*(uint32_t *)(result)) == 0) {
        Arg1 = 0;
        result = ExpPlFindLimitEntry(Arg1, v_stack_mE8, Arg3, Arg4);
        Arg1 = v_stack_m218;
        *(uint64_t *)(Arg1 + 0x48) = result;
        *(uint64_t *)(1 + 0x48) = result;
        result = 0;
        Arg1 = result + result * 4;
        result = *(uint64_t *)(v_rip + 0xBA0A20);
        Arg1 = (Arg1) + (Arg1);
        *(uint32_t *)(result + Arg1 * 8) = 0;
        *(uint32_t *)(1) = 0;
    }
    result = KeReleaseInStackQueuedSpinLock(v_stack_mE8, v_stack_mE8, Arg3, Arg4);
    goto loc_0035E064;
loc_0035E369:
    if (result != 64) goto loc_0035D91E;
    Arg2 = 0;
    goto loc_0035DF19;
loc_0035E37A:
    Arg1 = 0;
    goto loc_0035E099;
loc_0035E389:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBAFAC9))) != 0) goto loc_0035E2EA;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_mE8, 0, v_stack_m1A0, (uint32_t)(v_stack_p8));
    goto loc_0035E301;
loc_0035E3AB:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(result), 0, v_stack_m1A0, (uint32_t)(v_stack_p8));
    goto loc_0035E2D7;
loc_0035E3C4:
    if (0 >= (*(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8 + (int32_t)(1) * 8)) goto loc_0035F32E;
    v_stack_m248 = v_stack_m1E0;
    result = KeBugCheckEx(497, 2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBA0AF9) + 0x1F1 * 8)), 0);
loc_0035E3E8:
    result = KxWaitForLockOwnerShip(v_stack_mE8, 2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBA0AF9) + 0x1F1 * 8)), 0);
    goto loc_0035E301;
loc_0035E3F9:
    if ((Arg2 + 16) >= 2) goto loc_0035F379;
    v_stack_m248 = 1 + 32;
    result = KeBugCheckEx(497, 2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBA0AF9) + 0x1F1 * 8)), Arg2 + 16);
loc_0035E41A:
    result = KxWaitForLockOwnerShip(v_stack_m100, 2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBA0AF9) + 0x1F1 * 8)), Arg2 + 16);
    goto loc_0035DB13;
loc_0035E428:
    goto loc_0035E0C8;
loc_0035E446:
    v_stack_m144 = (uint32_t)(result);
    result = (uint32_t)((result) - ((uint32_t)((uint32_t)(v_stack_p8))));
    result = (uint32_t)((result) + 1);
    if (((uint32_t)(local_rsi)) < ((uint32_t)(result))) { result = (uint32_t)(local_rsi); }
    Arg4 = (uint32_t)((v_stack_p10) * ((uint32_t)(result)));
    Arg4 = (uint32_t)((Arg4) >> (8));
    Arg4 = (uint32_t)((Arg4) + ((uint32_t)((uint32_t)(v_stack_p8))));
    v_stack_p10 = Arg4;
    local_r10 = (uint32_t)((v_stack_m1E0) + (Arg4));
    goto loc_0035C3CD;
loc_0035E480:
    v_stack_m248 = (uint32_t)(Arg4);
    result = (1 + 32 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(1 + 0x20 - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xC689A1));
    result = KeBugCheckEx(3 + 21, *(uint64_t *)(v_rip - 0x35E4B5 + Arg2 * 8 + 0xFC7800), 1 + 32, 3);
loc_0035E4C3:
    Arg2 = 0;
    v_stack_m248 = v_stack_m20E;
    result = ExpPoolFlagsToPoolType(*(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8 + (int32_t)(1) * 8, Arg2, v_stack_m1D0, v_stack_m22E);
    if (sign_flag) goto loc_0035E013;
    if (v_stack_m22E != 0) {
        Arg2 = (uint32_t)(((uint32_t)(v_stack_m1D0)) | (8));
        v_stack_m1D0 = (uint32_t)(Arg2);
    }
    v_stack_m248 = v_stack_p10;
    result = EtwTracePool((uint32_t)(0xE20ULL), Arg2, (uint32_t)((uint32_t)(*(uint64_t *)(1 + 0x20))), local_rsi + 16);
    goto loc_0035E013;
loc_0035E51A:
    v_stack_m154 = (uint32_t)(result);
    result = (uint32_t)((result) - ((uint32_t)((uint32_t)(0xE20ULL))));
    result = (uint32_t)((result) + 1);
    if (((uint32_t)(local_r10)) < ((uint32_t)(result))) { result = (uint32_t)(local_r10); }
    Arg4 = (uint32_t)((local_rsi + 16) * ((uint32_t)(result)));
    Arg4 = (uint32_t)((Arg4) >> (8));
    Arg4 = (uint32_t)((Arg4) + ((uint32_t)((uint32_t)(0xE20ULL))));
    v_stack_p10 = Arg4;
    local_r10 = (uint32_t)((local_r10) + (Arg4));
    goto loc_0035C6EE;
loc_0035E556:
    result = (uint32_t)((local_rsi + 15) >> (4));
    v_stack_m1F8 = *(uint16_t *)(local_r10 + *(uint8_t *)(result + local_r10 * 1 + 0x10B80) * 2 + 0x1C3C0);
    v_stack_p8 = (uint32_t)(*(uint8_t *)(result + local_r10 * 1 + 0x10B80) - 33);
    v_stack_m218 = *(uint64_t *)(1 + 0x38);
    if (*(uint64_t *)(1 + 0x38) == 0) goto loc_0035E5F1;
    result = (*(uint8_t *)(result + local_r10 * 1 + 0x10B80) - 33) + 1;
    result = (result) << (6);
    result = (result) + (*(uint64_t *)(1 + 0x38));
    v_stack_p10 = result;
    if ((*(uint16_t *)(result)) <= 0) goto loc_0035E60A;
    result = ExpInterlockedPopEntrySList(result, *(uint8_t *)(result + local_r10 * 1 + 0x10B80), (uint32_t)((uint32_t)(*(uint64_t *)(1 + 0x20))), Arg4);
    if (result == 0) goto loc_0035E600;
loc_0035E5B4:
    if ((((uint8_t)(v_stack_m1F0)) & (2)) != 0) goto loc_0035E5DB;
    if (result == 0) goto loc_0035E5E4;
    Arg2 = (v_stack_m1F8) + (-16);
    result = RtlHeapZero(result + 16, Arg2, (uint32_t)((uint32_t)(*(uint64_t *)(1 + 0x20))), Arg4);
loc_0035E5DB:
    if (result != 0) goto loc_0035D905;
loc_0035E5E4:
loc_0035E5F1:
    v_stack_m228 = v_stack_m1F8;
    goto loc_0035C1B3;
loc_0035E600:
    Arg4 = 0;
loc_0035E60A:
    v_stack_m170 = 0;
    v_stack_m118 = 0;
    if (((uint32_t)(*(uint16_t *)(v_stack_p10))) < ((uint32_t)(*(uint16_t *)(v_stack_p10 + 0x10)))) goto loc_0035F0CE;
loc_0035E62C:
    goto loc_0035E5B4;
loc_0035E631:
    Arg1 = (((0) & (192)) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) {
        Arg2 = 1;
        Arg1 = *(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8 + (int32_t)(1) * 8;
        result = ExpCheckForLookaside(Arg1, Arg2, *(uint16_t *)(v_stack_p10 + 0x10), Arg4);
    }
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xC6857C));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC6857C)))) & (1)) != 0) {
        Arg2 = 1;
        Arg1 = *(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8 + (int32_t)(1) * 8;
        result = KeCheckForTimer(Arg1, Arg2, *(uint16_t *)(v_stack_p10 + 0x10), Arg4);
    }
    result = FREE_CHECK_ERESOURCE(*(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8 + (int32_t)(1) * 8, 1, *(uint16_t *)(v_stack_p10 + 0x10), Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC6855C)))) & (2)) == 0) goto loc_0035C8DC;
    result = ExpCheckForWorker(*(uint64_t *)(v_rip - 0x35E036 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8 + (int32_t)(1) * 8, 1, *(uint16_t *)(v_stack_p10 + 0x10), Arg4);
    goto loc_0035C8DC;
loc_0035E68C:
    if (1 != 0) {
        local_r13 = 0;
    }
    v_stack_m248 = 1 + 32;
    result = KeBugCheckEx(194, 13, result, (uint32_t)((uint32_t)(local_r13)));
loc_0035E6AF:
    goto loc_0035D764;
loc_0035E6C2:
    Arg2 = (uint32_t)((0) & (16));
    v_stack_m248 = v_stack_m20C;
    result = ExpPoolFlagsToPoolType(0, Arg2, v_stack_m1C4, v_stack_m22C);
    if (sign_flag) goto loc_0035C91D;
    if (v_stack_m22C != 0) {
        Arg2 = (uint32_t)(((uint32_t)(v_stack_m1C4)) | (8));
        v_stack_m1C4 = (uint32_t)(Arg2);
    }
    v_stack_m248 = *(uint64_t *)(v_rip - 0x35E5EB + v_stack_m1F0 * 1);
    result = EtwTracePool((uint32_t)(0xE22ULL), Arg2, (uint32_t)((uint32_t)(*(uint64_t *)(1 + 0x20))), 1 + 32);
    goto loc_0035C91D;
loc_0035E714:
    if (((*(uint8_t *)((uint32_t)(0xE22ULL) + (int32_t)((uint32_t)(1 + 0x20)) * 8 + 0x38)) & (1)) != 0) goto loc_0035CA81;
    local_r10 = (*(uint64_t *)(v_rip - 0x35E5EB + v_stack_m1F0 * 1) * 4 + 63) & (-64);
    if (local_r10 == 64) { local_r10 = 128; }
loc_0035E743:
    if (Arg2 >= (*(uint64_t *)((uint32_t)(0xE22ULL) + (int32_t)((uint32_t)(1 + 0x20)) * 8 + 0x38))) goto loc_0035CA81;
    if ((local_r10 + Arg2 * 1) >= (*(uint64_t *)((uint32_t)(0xE22ULL) + (int32_t)((uint32_t)(1 + 0x20)) * 8 + 0x38))) goto loc_0035CA81;
    if ((local_r10 + Arg2 * 1) == (*(uint64_t *)((uint32_t)(0xE22ULL) + (int32_t)((uint32_t)(1 + 0x20)) * 8 + 0x38))) goto loc_0035E892;
    goto loc_0035E743;
loc_0035E76A:
    goto loc_0035CEF9;
loc_0035E775:
    goto loc_0035D50F;
loc_0035E793:
    result = ExIsSpecialPoolAddress(*(uint64_t *)((uint32_t)(0xE22ULL) + (int32_t)((uint32_t)(1 + 0x20)) * 8 + 0x38), (uint32_t)((uint32_t)(v_stack_m1F0)), (uint32_t)((uint32_t)(*(uint64_t *)(1 + 0x20))), v_stack_p10);
    if ((uint32_t)(result) == 0) goto loc_0035CF7F;
    goto loc_0035C800;
loc_0035E7A8:
    result = RtlpHpLargeFree(local_r10 + Arg2 * 1, v_rip - 3532267 + v_stack_m1F0 * 1, (uint32_t)((uint32_t)(*(uint64_t *)(1 + 0x20))), v_stack_p10);
    goto loc_0035CB63;
loc_0035E7B8:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(v_rip - 3532267 + v_stack_m1F0 * 1))) & (16));
    v_stack_m248 = v_stack_m20F;
    result = ExpPoolFlagsToPoolType(v_rip - 3532267 + v_stack_m1F0 * 1, Arg2, v_stack_m1D4, v_stack_m22F);
    if (sign_flag) goto loc_0035D455;
    if (v_stack_m22F != ((uint8_t)(*(uint64_t *)(local_r10 + Arg2 * 1)))) {
        Arg2 = (uint32_t)(((uint32_t)(v_stack_m1D4)) | (8));
        v_stack_m1D4 = (uint32_t)(Arg2);
    }
    v_stack_m248 = v_stack_p10;
    result = EtwTracePool((uint32_t)(0xE20ULL), Arg2, (uint32_t)((uint32_t)(local_r10 + Arg2 * 1)), 1 + 32);
    goto loc_0035D455;
loc_0035E812:
    if (*(uint64_t *)(local_r10 + Arg2 * 1) == 0) goto loc_0035BAEC;
    result = ExCheckSingleFilter((uint32_t)((uint32_t)(local_r10 + Arg2 * 1)), (uint32_t)((uint32_t)(1 + 32)), (uint32_t)((uint32_t)(local_r10 + Arg2 * 1)), 1 + 32);
    if ((uint32_t)(result) != 0) goto loc_0035BF20;
    if ((1 + 32) < (*(uint64_t *)(local_r10 + Arg2 * 1) + 16)) goto loc_0035BAEC;
    if ((1 + 32) >= (*(uint64_t *)(local_r10 + Arg2 * 1) + 32)) goto loc_0035BAEC;
    goto loc_0035BF20;
loc_0035E84C:
    if ((*(uint8_t *)(local_r10 + Arg2 * 1 + 0x16)) == 1) goto loc_0035BD54;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(local_r10 + Arg2 * 1)))) >> (6));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(local_r10 + Arg2 * 1)))) & (63));
    result = (*(uint64_t *)(local_r10 + Arg2 * 1 + result * 8 + 0x40)) & (-2);
    Arg3 = ~(-2);
    *(uint64_t *)(local_r10 + Arg2 * 1 + result * 8 + 0x40) = result;
    if (((*(uint64_t *)(local_r10 + Arg2 * 1 + result * 8 + 0x40)) & (Arg3)) == 0) goto loc_0035C0D2;
    goto loc_0035BE87;
loc_0035E892:
    result = (result) - (local_r10 + Arg2 * 1);
    Arg2 = -(result);
    if (!sign_flag) { Arg2 = result; }
    result = ExpTrackTableReturnLimit(*(uint64_t *)(local_r10 + Arg2 * 1 + result * 8 + 0x48), Arg2, (uint32_t)((uint32_t)(1 + 32)), 1 + 32);
    goto loc_0035CA81;
loc_0035E8B3:
    result = RtlpHpLfhThreadDataInitializeSet(v_rip - 3532267 + v_stack_m1F0 * 1, Arg2, (uint32_t)((uint32_t)(1 + 32)), 1 + 32);
    goto loc_0035BD4A;
loc_0035E8C0:
    result = (result) - (local_r10 + Arg2 * 1);
    Arg2 = -(result);
    if (!sign_flag) { Arg2 = result; }
    result = ExpTrackTableReturnLimit(*(uint64_t *)(1 + 0x20 + 0x48), Arg2, (uint32_t)((uint32_t)(1 + 32)), 1 + 32);
    goto loc_0035CA8A;
loc_0035E8DE:
    if ((*(uint8_t *)(1 + 0x20 + 0x16)) == 1) goto loc_0035CCF7;
    result = (local_r10 + Arg2 * 1) >> (6);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r10 + Arg2 * 1))) & (63));
    result = (*(uint64_t *)(1 + 0x20 + result * 8 + 0x40)) & (-2);
    Arg4 = ~(-2);
    *(uint64_t *)(1 + 0x20 + result * 8 + 0x40) = result;
    if (((*(uint64_t *)(1 + 0x20 + result * 8 + 0x40)) & (Arg4)) == 0) goto loc_0035D36D;
    goto loc_0035CB63;
loc_0035E929:
    if ((*(uint64_t *)(1 + 0x20 + result * 8 + 0x40)) > ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x35E5EB + v_stack_m1F0 * 1) + 0x210)))) goto loc_0035E9BA;
    result = RtlpHpAllocateHeapBackend(*(uint64_t *)(v_rip - 0x35E5EB + v_stack_m1F0 * 1), *(uint64_t *)((uint32_t)(0xE22ULL) + (int32_t)((uint32_t)(1 + 0x20)) * 8 + 0x38), *(uint64_t *)(1 + 0x20 + result * 8 + 0x40), Arg4);
    goto loc_0035D8FB;
loc_0035E94B:
    result = RtlpHpLfhThreadDataInitializeSet(result, *(uint64_t *)((uint32_t)(0xE22ULL) + (int32_t)((uint32_t)(1 + 0x20)) * 8 + 0x38), *(uint64_t *)(1 + 0x20 + result * 8 + 0x40), Arg4);
    goto loc_0035CCED;
loc_0035E958:
    if ((1 + 32) > ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x35E5EB + v_stack_m1F0 * 1) + 0x210)))) goto loc_0035E9C4;
    result = RtlpHpAllocateHeapBackend(*(uint64_t *)(v_rip - 0x35E5EB + v_stack_m1F0 * 1), result, 1 + 32, Arg4);
    goto loc_0035C128;
loc_0035E977:
    v_stack_m248 = *(uint64_t *)(v_rip - 0x35E5EB + v_stack_m1F0 * 1);
    result = (1 + 32 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(1 + 0x20 - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xC684AA));
    result = KeBugCheckEx(3 + 21, *(uint64_t *)(v_rip - 0x35E9AC + Arg2 * 8 + 0xFC7800), 1 + 32, 3);
loc_0035E9BA:
    result = RtlpHpLargeAlloc(3 + 21, *(uint64_t *)(v_rip - 0x35E9AC + Arg2 * 8 + 0xFC7800), 1 + 32, 3);
    goto loc_0035D969;
loc_0035E9C4:
    result = RtlpHpLargeAlloc(3 + 21, *(uint64_t *)(v_rip - 0x35E9AC + Arg2 * 8 + 0xFC7800), 1 + 32, 3);
    goto loc_0035C128;
loc_0035E9CE:
    result = RtlpHpLfhThreadDataInitializeSet((uint32_t)(0xE22ULL) + (int32_t)((uint32_t)(1 + 32)) * 8, *(uint64_t *)(v_rip - 0x35E9AC + Arg2 * 8 + 0xFC7800), 1 + 32, 3);
    goto loc_0035C24A;
loc_0035E9E2:
    result = RtlpHpLfhThreadDataInitializeSet(*(uint64_t *)(v_rip - 0x35E5EB + v_stack_m1F0 * 1) + 832, *(uint64_t *)(v_rip - 0x35E9AC + Arg2 * 8 + 0xFC7800), 1 + 32, 3);
    goto loc_0035C57D;
loc_0035E9F6:
    result = ObpDeferObjectDeletion(1 + 32 - 48, *(uint64_t *)(v_rip - 0x35E9AC + Arg2 * 8 + 0xFC7800), 1 + 32, 3);
    goto loc_0035C800;
loc_0035EA09:
    result = ObpDeferObjectDeletion(1 + 32 - 48, *(uint64_t *)(v_rip - 0x35E9AC + Arg2 * 8 + 0xFC7800), 1 + 32, 3);
    goto loc_0035D1F8;
loc_0035EA17:
    goto loc_0035C474;
loc_0035EA21:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + Arg2 * 1))))) >> (16));
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_r10 + Arg2 * 1 + 24;
    }
    if (Arg3 < v_stack_m228) goto loc_0035EB31;
    result = (v_stack_m228 + 4095) & (0xFFFFFFFFFFFFF000ULL);
loc_0035EA51:
    if ((1 + 32 + v_stack_m228 * 1) < result) goto loc_0035EB54;
    if (((*(uint32_t *)(local_r10 + Arg2 * 1)) & (0x4000ULL)) != 0) {
        Arg3 = result;
        Arg4 = 1;
        Arg3 = (Arg3) >> (8);
        Arg2 = 1 + 32;
        Arg3 = (uint32_t)((Arg3) & (1));
        Arg1 = v_stack_m228;
        result = ViFreeTrackedPool(Arg1, Arg2, Arg3, Arg4);
    }
    local_r14 = (1 + 32 + 15) & (-16);
    v_stack_m1CC = (uint32_t)(v_stack_m1F0);
    v_stack_m22D = 0;
    v_stack_m20D = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + Arg2 * 1 + 0x4)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC666C8))))) {
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC6805C)))) & (65)) != 0) goto loc_0035EBC2;
loc_0035EAB0:
    local_rsi = (result) & (-5);
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))))) * ((uint32_t)(*(uint32_t *)(local_r10 + Arg2 * 1 + 0x4)));
    Arg2 = (Arg1) >> (32);
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)(*(uint64_t *)(v_rip + 0xBA0295))));
loc_0035EAEA:
    Arg1 = ((uint32_t)((uint32_t)(Arg2)) + (uint32_t)((uint32_t)(Arg2)) * 4) + ((uint32_t)((uint32_t)(Arg2)) + (uint32_t)((uint32_t)(Arg2)) * 4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x35EACC + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + Arg2 * 1 + 0x4))))) goto loc_0035EB77;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x35EACC + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8))) == 0) goto loc_0035EB8F;
loc_0035EB07:
    result = (uint32_t)((Arg2 + 1) & ((uint32_t)(*(uint64_t *)(v_rip + 0xBA0295))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_0035EAEA;
    result = ExpRemovePoolTrackerExpansion((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + Arg2 * 1 + 0x4)))), local_r14, local_rsi, *(uint64_t *)(v_rip - 0x35EACC + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8);
loc_0035EB21:
    result = RtlpHpFreeHeap(*(uint64_t *)(v_rip - 0x35E5EB + v_stack_m1F0 * 1), local_r10 + Arg2 * 1, local_rsi, *(uint64_t *)(v_rip - 0x35EACC + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))) * 8 + 0xEFAD20) + Arg1 * 8);
    goto loc_0035CB63;
loc_0035EB31:
    if ((*(uint8_t *)(local_rsi)) == ((uint8_t)(*(uint64_t *)(v_rip - 0x35E5EB + v_stack_m1F0 * 1)))) goto loc_0035F498;
    v_stack_m248 = 35;
    result = KeBugCheckEx(193, v_stack_m228, local_rsi, (uint32_t)(*(uint32_t *)(local_r10 + Arg2 * 1)));
loc_0035EB54:
    if ((*(uint8_t *)(local_rsi)) == 193) goto loc_0035F4A0;
    v_stack_m248 = 36;
    result = KeBugCheckEx(193, v_stack_m228, local_rsi, (uint32_t)(*(uint32_t *)(local_r10 + Arg2 * 1)));
loc_0035EB77:
    local_rsi = (local_rsi) >> (8);
    local_rsi = (uint32_t)(~(local_rsi));
    local_rsi = (uint32_t)((local_rsi) & (1));
    result = ExpPoolTrackerReturnLimit((uint32_t)((uint32_t)(local_rsi)), local_r14, (uint32_t)(*(uint32_t *)(local_r10 + Arg2 * 1)), (uint32_t)(*(uint32_t *)(local_r10 + Arg2 * 1)));
    goto loc_0035EB21;
loc_0035EB8F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBA01CA) + (uint32_t)((uint32_t)(local_rsi)) * 8))) == 0) goto loc_0035EB07;
    *(uint32_t *)((uint32_t)(*(uint32_t *)(local_r10 + Arg2 * 1))) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBA01CA) + (uint32_t)((uint32_t)(local_rsi)) * 8)));
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA01B5) + (uint32_t)((uint32_t)(local_rsi)) * 8 + 0x48) == 0) goto loc_0035EAEA;
    *(uint64_t *)((uint32_t)(*(uint32_t *)(local_r10 + Arg2 * 1)) + 0x48) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBA01B5) + (uint32_t)((uint32_t)(local_rsi)) * 8 + 0x48);
    goto loc_0035EAEA;
loc_0035EBC2:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (16));
    v_stack_m248 = v_stack_m20D;
    result = ExpPoolFlagsToPoolType(local_rsi, Arg2, v_stack_m1CC, v_stack_m22D);
    if (sign_flag) goto loc_0035EAB0;
    if (v_stack_m22D != 0) {
        Arg2 = (uint32_t)(((uint32_t)(v_stack_m1CC)) | (8));
        v_stack_m1CC = (uint32_t)(Arg2);
    }
    v_stack_m248 = local_r14;
    result = EtwTracePool((uint32_t)(0xE22ULL), Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + Arg2 * 1 + 0x4)))), v_stack_m228);
    goto loc_0035EAB0;
loc_0035EC14:
    result = MmDeterminePoolType(v_stack_m228, Arg2, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + Arg2 * 1 + 0x4)))), v_stack_m228);
    local_rbx = (v_stack_m228) & (0xFFFFFFFFFFFFF000ULL);
    if ((*(uint8_t *)(v_rip + 0xC70031)) != 0) goto loc_0035ECCF;
loc_0035EC3D:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m228))) & (0xFFFULL));
    v_stack_m248 = v_stack_m228;
    Arg1 = (uint32_t)(((uint32_t)(0x1000ULL)) - ((uint32_t)(result)));
    result = ExpFreePoolChecks(v_stack_m228, (uint32_t)(*(uint32_t *)(local_rbx + 0x4)), (uint32_t)((uint32_t)(Arg1)), 128);
    result = (condition_is_above_or_equal) ? 1 : 0;
    result = (uint8_t)((result) + 1);
    if (2 >= = ((uint8_t)(result))) {
        Arg2 = 2;
        Arg4 = v_stack_m228;
        Arg1 = 193;
        v_stack_m248 = 49;
        Arg3 = Arg1 + 63;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    local_rdi = (uint32_t)((*(uint16_t *)(local_rbx)) & (0x1FFFULL));
    result = (local_rdi + 15) & (-16);
    if (result == ((uint32_t)((uint32_t)(Arg1)))) goto loc_0035EA21;
    v_stack_m248 = 33;
    result = KeBugCheckEx(193, v_stack_m228, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)(Arg1)));
loc_0035ECCF:
    if (local_rbx >= result) goto loc_0035F1D6;
    v_stack_m248 = v_stack_m1F0;
    result = KeBugCheckEx(497, 2, 2 - 1, local_rbx);
loc_0035ECFE:
    result = ExGetHeapFromType(local_rdi, (uint32_t)(0x80000000ULL), 1, local_rbx);
    v_stack_m218 = result;
    v_stack_m248 = 4;
    result = RtlpHpSegAlloc(result + 320, (uint32_t)((uint32_t)(Arg2)), (uint32_t)((uint32_t)(Arg2)), (uint32_t)((uint32_t)(Arg2)));
    v_stack_m140 = result;
    if (result == 0) goto loc_0035F43B;
    Arg1 = (result) + (16);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)(result)))) | (1));
    result = memset(Arg1, Arg2, (uint32_t)(0xFF0ULL), (uint32_t)((uint32_t)(Arg2)));
    result = (uint32_t)((local_rdi) & (0x400ULL));
    *(uint64_t *)(v_stack_m140 + 0x8) = v_stack_m1F0;
    Arg3 = result - 8;
    if (result == 0) { Arg3 = result; }
    local_rbx = (uint8_t)(((uint8_t)(result)) | (1));
    *(uint32_t *)(v_stack_m140) = Arg3;
    *(uint8_t *)(v_stack_m140 + 0x2) = (uint8_t)(local_rbx);
    *(uint32_t *)(v_stack_m140 + 0x4) = (uint32_t)((uint32_t)(v_stack_p18));
    v_stack_m180 = Arg3;
    if (result != 0) {
    }
    local_rdi = (v_stack_m140) - (Arg3);
    local_rdi = (local_rdi) + (0x1000ULL);
    local_rdi = (local_rdi) & (-16);
    if (((v_stack_m1B0) & (2)) == 0) {
        Arg2 = 0;
        Arg1 = local_rdi;
        result = memset(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(Arg2)));
        Arg2 = v_stack_p18;
        Arg1 = v_stack_m140;
        Arg3 = v_stack_m180;
    }
    result = MmDeterminePoolType(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(Arg2)));
    result = 0;
    Arg4 = (Arg3 + 15) & (-16);
    v_stack_m98 = 0;
    v_stack_m1D8 = 0;
    v_stack_m230 = 0;
    v_stack_m210 = 0;
    v_stack_m208 = Arg4;
    v_stack_mA8 = v_xmm0;
    if (((uint32_t)(Arg2)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC66350))))) {
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC67CF1)))) & (65)) != 0) goto loc_0035F03E;
loc_0035EE1B:
    local_rbx = (result) & (-5);
    v_stack_m1B8 = *(uint64_t *)(v_rip + 0xB9FF27);
    v_stack_m1A0 = *(uint64_t *)(v_rip + 0xB9FF08);
    Arg1 = (Arg1) * ((uint32_t)((uint32_t)(Arg2)));
    v_stack_p10 = *(uint64_t *)(v_rip - 0x35EE2A + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xEFAD20);
    local_r10 = (Arg1) >> (32);
    local_r10 = (uint32_t)((local_r10) ^ ((uint32_t)(Arg1)));
    local_r10 = (uint32_t)((local_r10) & ((uint32_t)(*(uint64_t *)(v_rip + 0xB9FF27))));
    v_stack_m1C0 = local_r10;
    v_stack_p8 = (uint32_t)(local_r10);
loc_0035EE74:
    Arg3 = ((uint32_t)((uint32_t)(local_r10)) + (uint32_t)((uint32_t)(local_r10)) * 4) << (4);
    v_stack_m1B0 = Arg3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + *(uint64_t *)(v_rip - 0x35EE2A + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xEFAD20) * 1)))) != ((uint32_t)(Arg2))) goto loc_0035EF1B;
    local_rbx = (local_rbx) >> (8);
    local_rbx = (uint32_t)(~(local_rbx));
    local_rbx = (uint32_t)((local_rbx) & (1));
    result = ExpPoolTrackerChargeEntry((uint32_t)((uint32_t)(local_rbx)), v_stack_m208, Arg3 + *(uint64_t *)(v_rip - 0x35EE2A + (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))) * 8 + 0xEFAD20) * 1, (uint32_t)((uint32_t)(local_r10)));
    Arg1 = (local_rdi) & (0xFFFFFFFFFFFFF000ULL);
    result = KasanPoolAllocate(Arg1, (uint32_t)(0x1000ULL), local_rdi, v_stack_m180);
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_0035EEF8;
loc_0035EED2:
    if (local_rdi == 0) goto loc_0035F036;
    v_stack_p10 = local_rdi;
    local_rdi = 0;
    goto loc_0035BBD2;
loc_0035EEF8:
    result = ExpFreeHeapSpecialPool(v_stack_m218, 0, local_rdi, v_stack_m180);
    Arg4 = 0;
loc_0035EF11:
    goto loc_0035BAFA;
loc_0035EF1B:
    if ((uint32_t)(result) == 0) goto loc_0035EF6E;
loc_0035EF1F:
    result = (uint32_t)((local_r10 + 1) & (v_stack_m1B8));
    v_stack_m1C0 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) != v_stack_p8) goto loc_0035EE74;
    result = ExpInsertPoolTrackerExpansion((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), v_stack_m208, (uint32_t)(v_stack_p18), Arg4);
    Arg1 = (0) & (0xFFFFFFFFFFFFF000ULL);
    result = KasanPoolAllocate(Arg1, (uint32_t)(0x1000ULL), 0, v_stack_m180);
    goto loc_0035EED2;
loc_0035EF6E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + *(uint64_t *)(v_rip + 0xB9FDEB) * 1))) == 0) goto loc_0035EFA6;
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + *(uint64_t *)(v_rip + 0xB9FDEB) * 1)));
    if (*(uint64_t *)(0 + *(uint64_t *)(v_rip + 0xB9FDD8) * 1 + 0x48) == 0) goto loc_0035EE74;
    *(uint64_t *)(Arg1 + 0x48) = *(uint64_t *)(0 + *(uint64_t *)(v_rip + 0xB9FDD8) * 1 + 0x48);
    goto loc_0035EE74;
loc_0035EFA6:
    result = (v_stack_m1A0) - 1;
    if ((*(uint64_t *)(0 + *(uint64_t *)(v_rip + 0xB9FDD8) * 1 + 0x48)) == result) goto loc_0035F09C;
    result = KeAcquireInStackQueuedSpinLock(v_rip + 12172604, v_stack_mA8, 0, *(uint64_t *)(0 + *(uint64_t *)(v_rip + 0xB9FDD8) * 1 + 0x48));
    result = (*(uint64_t *)(v_rip + 0xB9FD90)) + (v_stack_m1B0);
    v_stack_m1E0 = result;
    if ((*(uint32_t *)(result)) == ((uint32_t)(v_stack_m1F0))) {
        Arg1 = v_stack_p18;
        result = ExpPlFindLimitEntry(Arg1, v_stack_mA8, 0, *(uint64_t *)(0 + *(uint64_t *)(v_rip + 0xB9FDD8) * 1 + 0x48));
        Arg2 = v_stack_m1B0;
        Arg1 = v_stack_m1E0;
        Arg3 = v_stack_p10;
        *(uint64_t *)(Arg1 + 0x48) = result;
        Arg1 = v_stack_p18;
        *(uint64_t *)(Arg2 + Arg3 * 1 + 0x48) = result;
        result = *(uint64_t *)(v_rip + 0xB9FD53);
        *(uint32_t *)(Arg2 + result * 1) = (uint32_t)(Arg1);
        *(uint32_t *)(Arg2 + Arg3 * 1) = (uint32_t)(Arg1);
    }
    result = KeReleaseInStackQueuedSpinLock(v_stack_mA8, Arg2, Arg3, *(uint64_t *)(0 + *(uint64_t *)(v_rip + 0xB9FDD8) * 1 + 0x48));
    goto loc_0035EE74;
loc_0035F036:
    Arg4 = 0;
    goto loc_0035EF11;
loc_0035F03E:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p18)))) & (16));
    v_stack_m248 = v_stack_m210;
    result = ExpPoolFlagsToPoolType((uint32_t)(v_stack_p18), Arg2, v_stack_m1D8, v_stack_m230);
    if (sign_flag) goto loc_0035F091;
    if (v_stack_m230 != ((uint8_t)(v_stack_m1F0))) {
        Arg2 = (uint32_t)(((uint32_t)(v_stack_m1D8)) | (8));
        v_stack_m1D8 = (uint32_t)(Arg2);
    }
    v_stack_m248 = v_stack_m208;
    result = EtwTracePool((uint32_t)(0xE20ULL), Arg2, (uint32_t)(v_stack_p18), v_stack_m140);
loc_0035F091:
    goto loc_0035EE1B;
loc_0035F09C:
    goto loc_0035EF1F;
loc_0035F0A8:
    if (((uint8_t)(result)) == 4) goto loc_0035CFAF;
    goto loc_0035CFB5;
loc_0035F0BB:
    if (((uint8_t)(result)) == 4) goto loc_0035CE67;
    goto loc_0035CE6D;
loc_0035F0CE:
    Arg3 = (uint32_t)(((uint32_t)(v_stack_p18)) - ((uint32_t)((uint32_t)(0xE20ULL))));
    Arg3 = (uint32_t)((Arg3) >> (1));
    if (condition_is_equal) goto loc_0035E62C;
    Arg3 = (uint32_t)((Arg3) + 1);
    if (((uint32_t)(v_stack_p18)) > 0x20000ULL) goto loc_0035E62C;
    v_stack_m240 = v_stack_m118;
    v_stack_m248 = v_stack_m170;
    result = RtlpHpVsContextMultiAlloc((uint32_t)(v_stack_m1FC) + 704, (uint32_t)(v_stack_p18), Arg3, v_stack_m140);
    if ((uint32_t)(result) == 0) goto loc_0035F143;
    v_stack_m170 = *(uint64_t *)(v_stack_m170);
    result = (uint32_t)((result) + (-1));
    if (condition_is_equal) goto loc_0035E5B4;
    Arg1 = ((uint32_t)(v_stack_p8)) + 1;
    Arg1 = (Arg1) << (6);
    Arg1 = (Arg1) + (v_stack_m218);
    result = InterlockedPushListSList(Arg1, *(uint64_t *)(v_stack_m170), v_stack_m118, (uint32_t)((uint32_t)(result)));
    goto loc_0035E5B4;
loc_0035F143:
    Arg4 = 0;
    goto loc_0035E62C;
loc_0035F14B:
    if (((256) & (7)) != 0) {
        result = 2;
        v_stack_m248 = 8;
        Arg3 = (uint32_t)(result);
        Arg2 = (uint32_t)(result);
        Arg4 = 256;
        Arg1 = 497;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint32_t)(v_stack_m1FC) + 256 * 1;
    if (((uint32_t)(v_stack_m1FC) + 256 * 1) < 256) {
        Arg2 = 2;
        v_stack_m248 = (uint32_t)(v_stack_m1FC);
        Arg4 = 256;
        Arg1 = 497;
        Arg3 = Arg2 + 1;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    local_rbx = ((uint32_t)(v_stack_p18)) + (256);
    local_rdi = ((uint32_t)(v_stack_m1FC)) >> (3);
    local_rbx = (local_rbx) >> (3);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0xC67D22));
    if (local_rdi != 0) goto loc_0035F4A8;
loc_0035F1BF:
    if ((((uint8_t)((uint32_t)(v_stack_m1FC))) & (7)) == 0) goto loc_0035CAB6;
    result = (uint8_t)(((uint8_t)((uint32_t)(v_stack_m1FC))) & (7));
    *(uint8_t *)(local_rbx) = (uint8_t)(result);
    goto loc_0035CAB6;
loc_0035F1D6:
    result = local_rbx + 4096;
    if ((local_rbx + 4096) < local_rbx) {
        Arg2 = 2;
        v_stack_m248 = 0x1000ULL;
        Arg4 = local_rbx;
        Arg1 = 497;
        Arg3 = Arg2 + 1;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    Arg1 = (Arg1) + (local_rbx);
    Arg1 = (Arg1) >> (3);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xC67CB6));
    result = memset(Arg1, Arg2, 512, Arg4);
    goto loc_0035EC3D;
loc_0035F22C:
    local_r14 = (v_stack_m1F0) >> (3);
    local_rbx = (uint32_t)((v_stack_m1F0 - 1) & (7));
    result = (uint32_t)((v_stack_m170 - 1) & (7));
    local_rbx = (local_rbx) - (result);
    local_rbx = (local_rbx) - (v_stack_m1F0);
    local_rbx = (local_rbx) + (v_stack_m170);
    local_rsi = (v_stack_m170) + (Arg4);
    local_rsi = (local_rsi) >> (3);
    local_rsi = (local_rsi) + (*(uint64_t *)(v_rip + 0xC67C76));
    if (local_r14 != 0) goto loc_0035F405;
loc_0035F26B:
    local_r13 = v_stack_m1F0;
    if ((((uint8_t)(v_stack_m1F0)) & (7)) != 0) {
        local_r13 = (uint8_t)((v_stack_m1F0) & (7));
        *(uint8_t *)(local_rsi) = (uint8_t)(local_r13);
        local_rsi = (local_rsi) + 1;
    }
    local_rbx = (local_rbx) >> (3);
    if (local_rbx == 0) goto loc_0035BBCD;
    result = memset(local_rsi, 134, local_rbx, Arg4);
    goto loc_0035BBCD;
loc_0035F29A:
    if (local_rsi < local_rbx) {
        Arg2 = 2;
        v_stack_m248 = local_rbx;
        Arg4 = local_rbx;
        Arg1 = 497;
        Arg3 = Arg2 + 1;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (Arg1) + (local_rbx);
    result = (uint32_t)((Arg3 - 1) & (7));
    Arg3 = (Arg3) - (result);
    Arg1 = (Arg1) >> (3);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xC67BFB));
    Arg3 = (Arg3) + (7);
    Arg3 = (Arg3) >> (3);
    if (Arg3 == 0) goto loc_0035E1FE;
    result = memset(Arg1, 141, Arg3, Arg4);
    local_r10 = 0;
    goto loc_0035E1FE;
loc_0035F308:
    if ((local_rsi + Arg4 * 1) >= Arg4) goto loc_0035F22C;
    v_stack_m248 = local_rsi;
    result = KeBugCheckEx(497, 2, 2 + 1, Arg4);
loc_0035F32E:
    if ((((uint8_t)(local_rbx)) & (7)) == 0) goto loc_0035F29A;
    v_stack_m248 = 8;
    result = KeBugCheckEx(497, 2, 2, local_rbx);
loc_0035F358:
    if (local_r13 <= local_rsi) goto loc_0035F308;
    v_stack_m248 = local_rsi;
    result = KeBugCheckEx(497, 2, 2 + 1, local_r13);
loc_0035F379:
    if ((((uint8_t)(local_rdi)) & (7)) == 0) goto loc_0035D68A;
    v_stack_m248 = 8;
    result = KeBugCheckEx(497, 2, 2, local_rdi);
loc_0035F3A4:
    result = 497 + local_rdi * 1;
    if ((497 + local_rdi * 1) < local_rdi) {
        Arg2 = 2;
        v_stack_m248 = 497;
        Arg1 = 497;
        Arg3 = Arg2 + 1;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, local_rdi);
    }
    local_rsi = (local_rsi) + (local_rdi);
    local_rbx = (uint32_t)((local_r13 - 1) & (7));
    local_rsi = (local_rsi) >> (3);
    local_rsi = (local_rsi) + (*(uint64_t *)(v_rip + 0xC67AEF));
    result = (uint32_t)((Arg1 - 1) & (7));
    local_rbx = (local_rbx) - (result);
    local_rbx = (local_rbx) - (local_r13);
    local_r14 = (local_r13) >> (3);
    local_rbx = (local_rbx) + (Arg1);
    if (local_r14 == 0) goto loc_0035F26B;
loc_0035F405:
    Arg2 = 0;
    result = memset(local_rsi, Arg2, local_r14, local_rdi);
    local_rsi = (local_rsi) + (local_r14);
    goto loc_0035F26B;
loc_0035F41A:
    if (local_r13 <= local_rsi) goto loc_0035F3A4;
    v_stack_m248 = local_rsi;
    result = KeBugCheckEx(497, 2, 2 + 1, local_r13);
loc_0035F43B:
    Arg4 = 0;
    goto loc_0035EF11;
loc_0035F446:
    Arg2 = (*(uint16_t *)(v_stack_m218 + 0x2)) << (6);
    Arg2 = (Arg2) + (local_rdi);
    result = RtlpHpLfhBucketUpdateAffinityMapping(local_rdi, Arg2, 2 + 1, Arg4);
    goto loc_0035C7A7;
loc_0035F463:
    local_r15 = 0;
    goto loc_0035D665;
loc_0035F46B:
    goto loc_0035D8E2;
loc_0035F483:
    goto loc_0035D947;
loc_0035F48D:
    local_r10 = 0;
    goto loc_0035E14A;
loc_0035F498:
    Arg3 = (2 + 1) + 1;
    goto loc_0035EA36;
loc_0035F4A0:
    Arg3 = (Arg3) + 1;
    goto loc_0035EA51;
loc_0035F4A8:
    Arg2 = 0;
    result = memset(local_rbx, Arg2, 0, Arg4);
    local_rbx = (local_rbx) + (0);
    goto loc_0035F1BF;
loc_0035F4BD:
    local_rsp = (local_rsp) + (560);
    return local_r13;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0035BA30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
