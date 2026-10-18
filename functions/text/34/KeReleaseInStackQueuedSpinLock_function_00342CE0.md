# KeReleaseInStackQueuedSpinLock

- RVA: `0x00342CE0`–`0x00342CED` (길이 `13` bytes)
- VA: `0x0000000140342CE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000779C4`
- 디코드: `3`개 명령, `13/13` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **241**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ExpAcquireResourceSharedLite](../21/ExpAcquireResourceSharedLite_function_00212040.md) at `0x00212AC8`
- [ExpAcquireResourceSharedLite](../21/ExpAcquireResourceSharedLite_function_00212040.md) at `0x00212EBF`
- [ExpAcquireResourceSharedLite](../21/ExpAcquireResourceSharedLite_function_00212040.md) at `0x002132B9`
- [ExpAcquireResourceSharedLite](../21/ExpAcquireResourceSharedLite_function_00212040.md) at `0x002133D3`
- [sub_002142F9](../21/Unknown_function_002142F9.md) at `0x00214655`
- [sub_00215166](../21/Unknown_function_00215166.md) at `0x002151E0`
- [sub_00215166](../21/Unknown_function_00215166.md) at `0x00215559`
- [sub_00215166](../21/Unknown_function_00215166.md) at `0x00215640`
- [SepRmCallLsa](../22/SepRmCallLsa_function_00223630.md) at `0x00223764`
- [SepQueueWorkItem](../22/SepQueueWorkItem_function_00225844.md) at `0x0022597A`
- [CcFlushCacheOneRange](../23/CcFlushCacheOneRange_function_00236A30.md) at `0x00236E97`
- [CcSetFileSizesEx](../26/CcSetFileSizesEx_function_0026D070.md) at `0x0026D123`
- [CcSetFileSizesEx](../26/CcSetFileSizesEx_function_0026D070.md) at `0x0026D12C`
- [CcSetFileSizesEx](../26/CcSetFileSizesEx_function_0026D070.md) at `0x0026D174`
- [CcSetFileSizesEx](../26/CcSetFileSizesEx_function_0026D070.md) at `0x0026D198`
- [CcSetFileSizesEx](../26/CcSetFileSizesEx_function_0026D070.md) at `0x0026D210`
- [CcSetFileSizesEx](../26/CcSetFileSizesEx_function_0026D070.md) at `0x0026D273`
- [CcSetFileSizesEx](../26/CcSetFileSizesEx_function_0026D070.md) at `0x0026D27C`
- [CcSetFileSizesEx](../26/CcSetFileSizesEx_function_0026D070.md) at `0x0026D2F3`
- [CcSetFileSizesEx](../26/CcSetFileSizesEx_function_0026D070.md) at `0x0026D321`
- [PopIrpWorker](../26/PopIrpWorker_function_0026D410.md) at `0x0026D54E`
- [PopDequeueQuerySetIrp](../26/PopDequeueQuerySetIrp_function_0026EC34.md) at `0x0026ED0B`
- [PopFreeIrp](../26/PopFreeIrp_function_0026FAA0.md) at `0x0026FB37`
- [PopAllocateIrp](../27/PopAllocateIrp_function_0027116C.md) at `0x00271553`
- [CcUnmapInactiveViewsInternal](../27/CcUnmapInactiveViewsInternal_function_0027174C.md) at `0x00271AE0`
- [CcUnmapInactiveViewsInternal](../27/CcUnmapInactiveViewsInternal_function_0027174C.md) at `0x00271CF6`
- [CcUnmapInactiveViewsInternal](../27/CcUnmapInactiveViewsInternal_function_0027174C.md) at `0x00271D2B`
- [NtShutdownWorkerFactory](../2A/NtShutdownWorkerFactory_function_002A4E60.md) at `0x002A4F40`
- [ExpShutdownWorkerFactory](../2A/ExpShutdownWorkerFactory_function_002A4F70.md) at `0x002A5050`
- [PopQueueQuerySetIrp](../2B/PopQueueQuerySetIrp_function_002BEF18.md) at `0x002BF07E`
- [ExpInsertPoolTrackerExpansion](../2E/ExpInsertPoolTrackerExpansion_function_002ECCC0.md) at `0x002ECDC6`
- [ExAllocateContiguousHeapPool](../2E/ExAllocateContiguousHeapPool_function_002EE960.md) at `0x002EEBE8`
- [ExpInsertPoolTracker](../2E/ExpInsertPoolTracker_function_002EEFAC.md) at `0x002EF136`
- [AlpcpSignalAndWait](../2F/AlpcpSignalAndWait_function_002F9620.md) at `0x002F9703`
- [AlpcpSignalAndWait](../2F/AlpcpSignalAndWait_function_002F9620.md) at `0x002F9A3E`
- [ExpAcquireSharedStarveExclusive](ExpAcquireSharedStarveExclusive_function_003411C0.md) at `0x00341295`
- [ExpAcquireSharedStarveExclusive](ExpAcquireSharedStarveExclusive_function_003411C0.md) at `0x003415AC`
- [ExpAcquireSharedStarveExclusive](ExpAcquireSharedStarveExclusive_function_003411C0.md) at `0x0034166A`
- [ExpAcquireSharedStarveExclusive](ExpAcquireSharedStarveExclusive_function_003411C0.md) at `0x00341712`
- [ExpAcquireSharedStarveExclusive](ExpAcquireSharedStarveExclusive_function_003411C0.md) at `0x00341752`
- [ExpAcquireSharedStarveExclusive](ExpAcquireSharedStarveExclusive_function_003411C0.md) at `0x003417AD`
- [sub_00341BF0](Unknown_function_00341BF0.md) at `0x00341C10`
- [sub_003422B4](Unknown_function_003422B4.md) at `0x00342353`
- [sub_003422B4](Unknown_function_003422B4.md) at `0x0034236E`
- [sub_003439EB](Unknown_function_003439EB.md) at `0x00343AB9`
- [sub_00343D34](Unknown_function_00343D34.md) at `0x00343DEE`
- [ExpSetResourceOwnerPointerEx](ExpSetResourceOwnerPointerEx_function_00343E20.md) at `0x0034408D`
- [ExpSetResourceOwnerPointerEx](ExpSetResourceOwnerPointerEx_function_00343E20.md) at `0x00344334`
- [sub_003444DD](Unknown_function_003444DD.md) at `0x00344519`
- [sub_00344568](Unknown_function_00344568.md) at `0x003445F3`
- [sub_0034466C](Unknown_function_0034466C.md) at `0x003446C3`
- [sub_0034466C](Unknown_function_0034466C.md) at `0x003446F0`
- [ExpWorkerFactoryCompletionPacketRoutine](ExpWorkerFactoryCompletionPacketRoutine_function_00344810.md) at `0x00344890`
- [ExpWorkerFactoryCompletionPacketRoutine](ExpWorkerFactoryCompletionPacketRoutine_function_00344810.md) at `0x003448F2`
- [IopRecordIoAttribution](IopRecordIoAttribution_function_00349758.md) at `0x00349832`
- [ExpWorkerFactoryCreateThread](ExpWorkerFactoryCreateThread_function_0034B620.md) at `0x0034B6BE`
- [ExpWorkerFactoryCreateThread](ExpWorkerFactoryCreateThread_function_0034B620.md) at `0x0034B73B`
- [ExpWorkerFactoryCreateThread](ExpWorkerFactoryCreateThread_function_0034B620.md) at `0x0034B7C9`
- [ExpConvertExclusiveToSharedLite](ExpConvertExclusiveToSharedLite_function_0034F7A8.md) at `0x0034F836`
- [NtSetInformationWorkerFactory](../35/NtSetInformationWorkerFactory_function_00350A30.md) at `0x00350D25`
- [NtSetInformationWorkerFactory](../35/NtSetInformationWorkerFactory_function_00350A30.md) at `0x00350F39`
- [NtSetInformationWorkerFactory](../35/NtSetInformationWorkerFactory_function_00350A30.md) at `0x00351078`
- [NtSetInformationWorkerFactory](../35/NtSetInformationWorkerFactory_function_00350A30.md) at `0x00351177`
- [IopDeleteIoCompletionInternal](../35/IopDeleteIoCompletionInternal_function_00351438.md) at `0x003514B5`
- [CcRepostToSynchronousLazywriter](../35/CcRepostToSynchronousLazywriter_function_0035492C.md) at `0x003549AF`
- [CcAsyncLazywriteWorker](../35/CcAsyncLazywriteWorker_function_00354C28.md) at `0x00354D4D`
- [CcAsyncLazywriteWorker](../35/CcAsyncLazywriteWorker_function_00354C28.md) at `0x00354EB0`
- [CcPostWorkQueueRegular](../35/CcPostWorkQueueRegular_function_00356834.md) at `0x00356953`
- [CcCachemapUninitWorkerThread](../35/CcCachemapUninitWorkerThread_function_003569D0.md) at `0x00356AB4`
- [CcCachemapUninitWorkerThread](../35/CcCachemapUninitWorkerThread_function_003569D0.md) at `0x00356BAD`
- [CcPostWorkQueueCachemapUninit](../35/CcPostWorkQueueCachemapUninit_function_00356C94.md) at `0x00356DDB`
- [CcWriteBehindPreProcess](../35/CcWriteBehindPreProcess_function_00357784.md) at `0x00357815`
- [CcWriteBehindPreProcess](../35/CcWriteBehindPreProcess_function_00357784.md) at `0x00357845`
- [CcWriteBehindPreProcess](../35/CcWriteBehindPreProcess_function_00357784.md) at `0x003578CE`
- [CcWriteBehindPreProcess](../35/CcWriteBehindPreProcess_function_00357784.md) at `0x003579B3`
- [CcWriteBehindPostProcess](../35/CcWriteBehindPostProcess_function_00357BB4.md) at `0x00357CBC`
- [CcWriteBehindPostProcess](../35/CcWriteBehindPostProcess_function_00357BB4.md) at `0x00357D99`
- [CcWriteBehindPostProcess](../35/CcWriteBehindPostProcess_function_00357BB4.md) at `0x00357F19`
- [CcAsyncCopyRead](../35/CcAsyncCopyRead_function_00358880.md) at `0x003589EE`
- [CcGetDirtyPagesHelper](../35/CcGetDirtyPagesHelper_function_00358D40.md) at `0x00358E55`
- [CcGetDirtyPagesHelper](../35/CcGetDirtyPagesHelper_function_00358D40.md) at `0x003590D7`
- [CcFlushCachePostProcessOneRange](../35/CcFlushCachePostProcessOneRange_function_00359710.md) at `0x00359806`
- [CcFlushCachePostProcessOneRange](../35/CcFlushCachePostProcessOneRange_function_00359710.md) at `0x00359BF8`
- [CcUnpinFileDataEx](../35/CcUnpinFileDataEx_function_00359DEC.md) at `0x00359F48`
- [CcSetDirtyPinnedData](../35/CcSetDirtyPinnedData_function_0035A120.md) at `0x0035A2C9`
- [sub_0035A582](../35/Unknown_function_0035A582.md) at `0x0035A7B4`
- [CcFlushCachePreProcess](../35/CcFlushCachePreProcess_function_0035A9B0.md) at `0x0035AB3B`
- [CcFlushCachePreProcess](../35/CcFlushCachePreProcess_function_0035A9B0.md) at `0x0035ABDD`
- [ExAllocateHeapPool](../35/ExAllocateHeapPool_function_0035BA30.md) at `0x0035CA85`
- [ExAllocateHeapPool](../35/ExAllocateHeapPool_function_0035BA30.md) at `0x0035D888`
- [ExAllocateHeapPool](../35/ExAllocateHeapPool_function_0035BA30.md) at `0x0035DB4D`
- [ExAllocateHeapPool](../35/ExAllocateHeapPool_function_0035BA30.md) at `0x0035E350`
- [ExAllocateHeapPool](../35/ExAllocateHeapPool_function_0035BA30.md) at `0x0035F01B`
- [sub_0035FB85](../35/Unknown_function_0035FB85.md) at `0x0035FE69`
- [sub_00360968](../36/Unknown_function_00360968.md) at `0x00360B12`
- [ExpRemovePoolTrackerExpansion](../36/ExpRemovePoolTrackerExpansion_function_00361300.md) at `0x00361403`
- [ExpRemovePoolTrackerExpansion](../36/ExpRemovePoolTrackerExpansion_function_00361300.md) at `0x00361467`
- [IoDiskIoAttributionQuery](../37/IoDiskIoAttributionQuery_function_00379D38.md) at `0x00379DD8`
- [CcCanIWrite](../38/CcCanIWrite_function_00388250.md) at `0x00388627`
- [CcScheduleReadAheadNuma](../38/CcScheduleReadAheadNuma_function_0038883C.md) at `0x00388B41`
- [CcLazyWriteScanVolume](../38/CcLazyWriteScanVolume_function_00388DC0.md) at `0x0038908C`
- [CcLazyWriteScanVolume](../38/CcLazyWriteScanVolume_function_00388DC0.md) at `0x003891D5`
- [CcLazyWriteScanVolume](../38/CcLazyWriteScanVolume_function_00388DC0.md) at `0x0038920D`
- [CcLazyWriteScanVolume](../38/CcLazyWriteScanVolume_function_00388DC0.md) at `0x0038936A`
- [CcLazyWriteScanVolume](../38/CcLazyWriteScanVolume_function_00388DC0.md) at `0x0038943F`
- [CcForEachPrivateVolumeCacheMap](../38/CcForEachPrivateVolumeCacheMap_function_0038967C.md) at `0x003896E4`
- [CcForEachPrivateVolumeCacheMap](../38/CcForEachPrivateVolumeCacheMap_function_0038967C.md) at `0x00389731`
- [CcCanIWriteStreamEx](../38/CcCanIWriteStreamEx_function_0038993C.md) at `0x00389A6D`
- [CcCanIWriteStreamEx](../38/CcCanIWriteStreamEx_function_0038993C.md) at `0x00389B43`
- [CcDeleteBcbs](../38/CcDeleteBcbs_function_00389BF0.md) at `0x00389D01`
- [CcForceWriteThrough](../38/CcForceWriteThrough_function_00389E50.md) at `0x00389F8B`
- [CcScanLogHandleList](../38/CcScanLogHandleList_function_0038A26C.md) at `0x0038A32B`
- [CcDeleteSharedCacheMap](../38/CcDeleteSharedCacheMap_function_0038A804.md) at `0x0038A969`
- [CcDeleteSharedCacheMap](../38/CcDeleteSharedCacheMap_function_0038A804.md) at `0x0038A976`
- [CcDeleteSharedCacheMap](../38/CcDeleteSharedCacheMap_function_0038A804.md) at `0x0038AA5A`
- [CcPurgeCacheSection](../38/CcPurgeCacheSection_function_0038B130.md) at `0x0038B211`
- [CcPurgeCacheSection](../38/CcPurgeCacheSection_function_0038B130.md) at `0x0038B21A`
- [CcPurgeCacheSection](../38/CcPurgeCacheSection_function_0038B130.md) at `0x0038B340`
- [CcPurgeCacheSection](../38/CcPurgeCacheSection_function_0038B130.md) at `0x0038B3BE`
- [CcDeleteMbcb](../38/CcDeleteMbcb_function_0038C088.md) at `0x0038C108`
- [NtWaitForWorkViaWorkerFactory](../39/NtWaitForWorkViaWorkerFactory_function_00394270.md) at `0x00394E31`
- [AlpcpSignal](../39/AlpcpSignal_function_003955E0.md) at `0x003956AF`
- [AlpcpSignal](../39/AlpcpSignal_function_003955E0.md) at `0x00395FEF`
- [CcLazyWriteScan](../3C/CcLazyWriteScan_function_003C9394.md) at `0x003C94DA`
- [CcLazyWriteScan](../3C/CcLazyWriteScan_function_003C9394.md) at `0x003C94F2`
- [CcLazyWriteScan](../3C/CcLazyWriteScan_function_003C9394.md) at `0x003C9837`
- [CcLazyWriteScan](../3C/CcLazyWriteScan_function_003C9394.md) at `0x003C990F`
- [CcLazyWriteScan](../3C/CcLazyWriteScan_function_003C9394.md) at `0x003C9A7F`
- [CcQueueLazyWriteScanThreadForVolume](../3C/CcQueueLazyWriteScanThreadForVolume_function_003C9AF0.md) at `0x003C9C79`
- [CcQueueLazyWriteScanThreadForVolume](../3C/CcQueueLazyWriteScanThreadForVolume_function_003C9AF0.md) at `0x003C9CF9`
- [CcCoalescingCallBackHelper](../3C/CcCoalescingCallBackHelper_function_003CA200.md) at `0x003CA2B1`
- [CcMdlWriteComplete2](../3C/CcMdlWriteComplete2_function_003CA36C.md) at `0x003CA436`
- [CcMapAndCopyInToCache](../3C/CcMapAndCopyInToCache_function_003CA7F0.md) at `0x003CB21C`
- [CcMapAndCopyInToCache](../3C/CcMapAndCopyInToCache_function_003CA7F0.md) at `0x003CB2BC`
- [CcMapAndCopyInToCache](../3C/CcMapAndCopyInToCache_function_003CA7F0.md) at `0x003CB36A`
- [CcSetDirtyInMask](../3C/CcSetDirtyInMask_function_003CB688.md) at `0x003CB894`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CCBA9`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CCBB2`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CCBDD`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CCCA8`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CCCB1`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CCDAB`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CCDB4`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CCECE`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CCFE9`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CD0E9`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CD19F`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CD1F5`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CD1FE`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CD229`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CD296`
- [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CD2CE`
- [CcUninitializeCacheMap](../3C/CcUninitializeCacheMap_function_003CD520.md) at `0x003CD743`
- [CcUninitializeCacheMap](../3C/CcUninitializeCacheMap_function_003CD520.md) at `0x003CD7CE`
- [CcUninitializeCacheMap](../3C/CcUninitializeCacheMap_function_003CD520.md) at `0x003CD7D7`
- [CcUninitializeCacheMap](../3C/CcUninitializeCacheMap_function_003CD520.md) at `0x003CD814`
- [CcUninitializeCacheMap](../3C/CcUninitializeCacheMap_function_003CD520.md) at `0x003CD882`
- [CcUninitializeCacheMap](../3C/CcUninitializeCacheMap_function_003CD520.md) at `0x003CD88B`
- [CcCreatePrivateVolumeCacheMap](../3C/CcCreatePrivateVolumeCacheMap_function_003CDB20.md) at `0x003CDC5B`
- [CcFindPrivateVolumeCacheMap](../3C/CcFindPrivateVolumeCacheMap_function_003CDC80.md) at `0x003CDD30`
- [CcFindPrivateVolumeCacheMap](../3C/CcFindPrivateVolumeCacheMap_function_003CDC80.md) at `0x003CDDFE`
- [CcInsertPrivateVolumeCacheMap](../3C/CcInsertPrivateVolumeCacheMap_function_003CE714.md) at `0x003CE92D`
- [CcDeletePrivateVolumeCacheMap](../3C/CcDeletePrivateVolumeCacheMap_function_003CE950.md) at `0x003CEB84`
- [CcReapPrivateVolumeCachemapWorkerThread](../3C/CcReapPrivateVolumeCachemapWorkerThread_function_003CF320.md) at `0x003CF389`
- [CcReapPrivateVolumeCachemapWorkerThread](../3C/CcReapPrivateVolumeCachemapWorkerThread_function_003CF320.md) at `0x003CF3C3`
- [ExAcquireSharedWaitForExclusive](../3D/ExAcquireSharedWaitForExclusive_function_003D43F0.md) at `0x003D44AE`
- [ExAcquireSharedWaitForExclusive](../3D/ExAcquireSharedWaitForExclusive_function_003D43F0.md) at `0x003D4585`
- [ExAcquireSharedWaitForExclusive](../3D/ExAcquireSharedWaitForExclusive_function_003D43F0.md) at `0x003D45D0`
- [ExAcquireSharedWaitForExclusive](../3D/ExAcquireSharedWaitForExclusive_function_003D43F0.md) at `0x003D4615`
- [ExpExpandResourceOwnerTable](../3D/ExpExpandResourceOwnerTable_function_003D489C.md) at `0x003D48D7`
- [ExpExpandResourceOwnerTable](../3D/ExpExpandResourceOwnerTable_function_003D489C.md) at `0x003D4936`
- [ExpExpandResourceOwnerTable](../3D/ExpExpandResourceOwnerTable_function_003D489C.md) at `0x003D49CC`
- [HalpDmaAllocateScatterPagesFromScatterPool](../3D/HalpDmaAllocateScatterPagesFromScatterPool_function_003DC3EC.md) at `0x003DC4D5`
- [HalpDmaAllocateScatterPagesFromScatterPoolV3](../3D/HalpDmaAllocateScatterPagesFromScatterPoolV3_function_003DC5D8.md) at `0x003DC660`
- [HalpDmaAllocateScatterPagesFromScatterPoolV3](../3D/HalpDmaAllocateScatterPagesFromScatterPoolV3_function_003DC5D8.md) at `0x003DC69D`
- [KeInsertDeviceQueue](../3D/KeInsertDeviceQueue_function_003DD900.md) at `0x003DD9FC`
- [HalpDmaAllocateMapRegisters](../3D/HalpDmaAllocateMapRegisters_function_003DDA0C.md) at `0x003DDB53`
- [HalpDmaAllocateMapRegisters](../3D/HalpDmaAllocateMapRegisters_function_003DDA0C.md) at `0x003DDBCF`
- [HalpDmaFreeMapRegisters](../3D/HalpDmaFreeMapRegisters_function_003DF5F4.md) at `0x003DF6FE`
- [KeRemoveDeviceQueue](../3D/KeRemoveDeviceQueue_function_003DF890.md) at `0x003DF9AF`
- [HalpDmaDequeueAdapter](../3D/HalpDmaDequeueAdapter_function_003DF9C0.md) at `0x003DFA49`
- [HalpDmaReturnPageToOwner](../3D/HalpDmaReturnPageToOwner_function_003DFB94.md) at `0x003DFC59`
- [HalpDmaReturnToScatterPool](../3D/HalpDmaReturnToScatterPool_function_003DFD00.md) at `0x003DFD96`
- [HalpDmaAllocateContiguousPagesFromContiguousPoolV2](../3E/HalpDmaAllocateContiguousPagesFromContiguousPoolV2_function_003E02A0.md) at `0x003E0313`
- [HalpDmaAllocateContiguousPagesFromContiguousPoolV2](../3E/HalpDmaAllocateContiguousPagesFromContiguousPoolV2_function_003E02A0.md) at `0x003E0380`
- [HalpDmaReturnToContiguousPool](../3E/HalpDmaReturnToContiguousPool_function_003E1758.md) at `0x003E1804`
- [HalpDmaAllocateScatterPagesFromContiguousPoolV2](../3E/HalpDmaAllocateScatterPagesFromContiguousPoolV2_function_003E1DC4.md) at `0x003E1F96`
- [HalpDmaAllocateScatterPagesFromContiguousPoolV2](../3E/HalpDmaAllocateScatterPagesFromContiguousPoolV2_function_003E1DC4.md) at `0x003E1FB3`
- [AlpcpQueueIoCompletionPort](../3F/AlpcpQueueIoCompletionPort_function_003FF760.md) at `0x003FFA4F`
- [CcAcquireByteRangeForWrite](../40/CcAcquireByteRangeForWrite_function_00401E74.md) at `0x004020FA`
- [CcGetFlushedValidData](../40/CcGetFlushedValidData_function_00402920.md) at `0x00402A13`
- [CcGetFlushedValidData](../40/CcGetFlushedValidData_function_00402920.md) at `0x00402A67`
- [CcGetFlushedValidData](../40/CcGetFlushedValidData_function_00402920.md) at `0x00402A71`
- [CcGetFlushedValidData](../40/CcGetFlushedValidData_function_00402920.md) at `0x00402AC2`
- [CcNotifyOfMappedWrite](../40/CcNotifyOfMappedWrite_function_0040338C.md) at `0x0040340B`
- [CcNotifyOfMappedWrite](../40/CcNotifyOfMappedWrite_function_0040338C.md) at `0x00403456`
- [CcNotifyOfMappedWrite](../40/CcNotifyOfMappedWrite_function_0040338C.md) at `0x004034CF`
- [CcNotifyOfMappedWrite](../40/CcNotifyOfMappedWrite_function_0040338C.md) at `0x004034D8`
- [CcNotifyOfMappedWrite](../40/CcNotifyOfMappedWrite_function_0040338C.md) at `0x004035BF`
- [CcNotifyOfMappedWrite](../40/CcNotifyOfMappedWrite_function_0040338C.md) at `0x00403650`
- [CcNotifyOfMappedWriteComplete](../40/CcNotifyOfMappedWriteComplete_function_0040873C.md) at `0x00408818`
- [ExDisableResourceBoostLite](../41/ExDisableResourceBoostLite_function_0041F840.md) at `0x0041F88F`
- [NtCancelWaitCompletionPacket](../42/NtCancelWaitCompletionPacket_function_0042F100.md) at `0x0042F1E8`
- [IopCloseWaitCompletionPacket](../42/IopCloseWaitCompletionPacket_function_0042F520.md) at `0x0042F5EC`
- [PopWakeDeviceList](../43/PopWakeDeviceList_function_00430238.md) at `0x004303BC`
- [PopSleepDeviceList](../43/PopSleepDeviceList_function_00430460.md) at `0x00430687`
- [PoQueryWatchdogTime](../44/PoQueryWatchdogTime_function_004479B0.md) at `0x00447A81`
- [CcSetParallelFlushFile](../44/CcSetParallelFlushFile_function_0044B900.md) at `0x0044B997`
- [CcSetLogHandleForFileEx](../44/CcSetLogHandleForFileEx_function_0044EA30.md) at `0x0044EC5D`
- [CcChangeBackingFileObject](../45/CcChangeBackingFileObject_function_00457E5C.md) at `0x00457EFD`
- [CcChangeBackingFileObject](../45/CcChangeBackingFileObject_function_00457E5C.md) at `0x00457F65`
- [CcChangeBackingFileObject](../45/CcChangeBackingFileObject_function_00457E5C.md) at `0x00457FB9`
- [CcChangeBackingFileObject](../45/CcChangeBackingFileObject_function_00457E5C.md) at `0x00457FE0`
- [CcIsThereDirtyLoggedPages](../45/CcIsThereDirtyLoggedPages_function_0045BBF0.md) at `0x0045BCF3`
- [CcCompleteAsyncRead](../45/CcCompleteAsyncRead_function_0045E7DC.md) at `0x0045EA44`
- [CcUpdateSharedCacheMapFlag](../45/CcUpdateSharedCacheMapFlag_function_0045EC14.md) at `0x0045ECA2`
- [KeRemoveByKeyDeviceQueue](../45/KeRemoveByKeyDeviceQueue_function_0045FB30.md) at `0x0045FBFA`
- [KeInsertByKeyDeviceQueue](../45/KeInsertByKeyDeviceQueue_function_0045FD80.md) at `0x0045FE32`
- [CcWaitForUninitializeCacheMap](../46/CcWaitForUninitializeCacheMap_function_004633F0.md) at `0x0046350B`
- [CcMapDataForOverwrite](../46/CcMapDataForOverwrite_function_00466160.md) at `0x00466325`
- [KeReleaseInStackQueuedSpinLockForDpc](../46/KeReleaseInStackQueuedSpinLockForDpc_function_0046A3E0.md) at `0x0046A404`
- [KeSetSchedulingGroupWeights](../46/KeSetSchedulingGroupWeights_function_0046D024.md) at `0x0046D210`
- [KeInsertSchedulingGroup](../46/KeInsertSchedulingGroup_function_0046D324.md) at `0x0046D5B5`
- [KeSetSchedulingGroupCpuRates](../46/KeSetSchedulingGroupCpuRates_function_0046DE5C.md) at `0x0046DFB3`
- [PoHandleIrp](../47/PoHandleIrp_function_004709D0.md) at `0x00470AD8`
- [PoHandleIrp](../47/PoHandleIrp_function_004709D0.md) at `0x00470B9B`
- [NtWorkerFactoryWorkerReady](../47/NtWorkerFactoryWorkerReady_function_00474CF0.md) at `0x00474D8B`
- [PopApplyLegacyPowerRequestFlags](../47/PopApplyLegacyPowerRequestFlags_function_00477364.md) at `0x00477409`
- [PopPowerRequestReferenceRelease](../47/PopPowerRequestReferenceRelease_function_004775B0.md) at `0x00477662`
- [PopPowerRequestReferenceAcquire](../47/PopPowerRequestReferenceAcquire_function_004776C0.md) at `0x0047776E`
- [PopPowerRequestHandleRequestOverrideQueryResponse](../47/PopPowerRequestHandleRequestOverrideQueryResponse_function_004777FC.md) at `0x00477854`
- [PopPowerRequestHandleClose](../47/PopPowerRequestHandleClose_function_00477894.md) at `0x004778F0`
- [PopPowerRequestCallbackWorker](../47/PopPowerRequestCallbackWorker_function_00477AD0.md) at `0x00477B30`
- [PopPowerRequestCallbackWorker](../47/PopPowerRequestCallbackWorker_function_00477AD0.md) at `0x00477B89`
- [AlpcpFreeCompletionPacketLookaside](../47/AlpcpFreeCompletionPacketLookaside_function_0047BBB0.md) at `0x0047BBE6`
- [PopCompleteNotifyTransitionCommon](../48/PopCompleteNotifyTransitionCommon_function_00483B4C.md) at `0x00483D2A`
- [ExpDeleteWorkerFactory](../48/ExpDeleteWorkerFactory_function_00486880.md) at `0x004868C7`
- [KeQuerySchedulingGroupHistory](../48/KeQuerySchedulingGroupHistory_function_0048B8B4.md) at `0x0048B963`
- [CcIsThereDirtyDataHelper](../48/CcIsThereDirtyDataHelper_function_0048BF30.md) at `0x0048BFDC`
- [CcIsThereDirtyDataHelper](../48/CcIsThereDirtyDataHelper_function_0048BF30.md) at `0x0048C01D`
- [CcIsThereDirtyDataHelper](../48/CcIsThereDirtyDataHelper_function_0048BF30.md) at `0x0048C030`
- [CcWorkerThread](../48/CcWorkerThread_function_0048F0F0.md) at `0x0048F28E`
- [CcWorkerThread](../48/CcWorkerThread_function_0048F0F0.md) at `0x0048F4E1`
- [CcWorkerThread](../48/CcWorkerThread_function_0048F0F0.md) at `0x0048F588`
- [CcPerformReadAhead](../48/CcPerformReadAhead_function_0048F738.md) at `0x0048F899`
- [CcPerformReadAhead](../48/CcPerformReadAhead_function_0048F738.md) at `0x0048FC3F`
- [CcPerformReadAhead](../48/CcPerformReadAhead_function_0048F738.md) at `0x0048FC97`
- [WmipWriteWnodeToObject](../49/WmipWriteWnodeToObject_function_00491C0C.md) at `0x00491C64`
- [WmipCompleteGuidIrpWithError](../49/WmipCompleteGuidIrpWithError_function_004955BC.md) at `0x004955F3`
- [CcPrepareMdlWrite](../49/CcPrepareMdlWrite_function_004996D0.md) at `0x00499A23`
- [HalpDmaCommitScatterMapBuffers](../49/HalpDmaCommitScatterMapBuffers_function_0049A9D0.md) at `0x0049AB0D`
- [HalpDmaGetTranslationEntries](../49/HalpDmaGetTranslationEntries_function_0049AB3C.md) at `0x0049AC2C`
- [HalpDmaGetTranslationEntries](../49/HalpDmaGetTranslationEntries_function_0049AB3C.md) at `0x0049AC6E`
- [CcSetAdditionalCacheAttributesEx](../4A/CcSetAdditionalCacheAttributesEx_function_004A5000.md) at `0x004A50C0`
- [CcDeductDirtyPagesFromExternalCache](../4A/CcDeductDirtyPagesFromExternalCache_function_004A65D0.md) at `0x004A668B`
- [PopUpdateWakeSource](../4A/PopUpdateWakeSource_function_004AA70C.md) at `0x004AA767`
- [KeRemoveSchedulingGroup](../4A/KeRemoveSchedulingGroup_function_004AD328.md) at `0x004AD4D4`
- [CcGetFileObjectFromSectionPtrs](../4B/CcGetFileObjectFromSectionPtrs_function_004B0E60.md) at `0x004B0EAD`
- [CcAsyncLazywriteWorkerThread](../4B/CcAsyncLazywriteWorkerThread_function_004B2130.md) at `0x004B21F7`
- [CcAsyncLazywriteWorkerThread](../4B/CcAsyncLazywriteWorkerThread_function_004B2130.md) at `0x004B228C`
- [CcPostWorkQueueAsyncLazywrite](../4B/CcPostWorkQueueAsyncLazywrite_function_004BA17C.md) at `0x004BA264`
- [PopGetMostRecentWakeInfo](../4B/PopGetMostRecentWakeInfo_function_004BE4F8.md) at `0x004BE538`
- [PopPowerRequestUnrevokeRequests](../4B/PopPowerRequestUnrevokeRequests_function_004BF3D0.md) at `0x004BF40B`
- [CcQuickLazyWriteScanForVolume](../4B/CcQuickLazyWriteScanForVolume_function_004BFEE0.md) at `0x004BFF72`
- [PopPowerRequestRevokeRequests](../4C/PopPowerRequestRevokeRequests_function_004C0158.md) at `0x004C01A9`
- [CcPostWorkQueueSpecial](../4C/CcPostWorkQueueSpecial_function_004C046C.md) at `0x004C0539`
- [CcPostPVCMForDeleteToPartition](../4C/CcPostPVCMForDeleteToPartition_function_004C2DBC.md) at `0x004C2EAB`
- [CcPostPVCMDelayedDelete](../4C/CcPostPVCMDelayedDelete_function_004C2EE4.md) at `0x004C2F9C`
- [PopGetCurrentWakeInfos](../4C/PopGetCurrentWakeInfos_function_004C8840.md) at `0x004C88D1`
- [CcSetLoggedDataThreshold](../4C/CcSetLoggedDataThreshold_function_004C8D50.md) at `0x004C8DDE`
- [PopRecordPoIrpBlackboxInformation](../4C/PopRecordPoIrpBlackboxInformation_function_004CE14C.md) at `0x004CE381`
- [CcAsyncLazywriteWorkerMulti](../4D/CcAsyncLazywriteWorkerMulti_function_004D1574.md) at `0x004D1875`
- [CcAsyncLazywriteWorkerMulti](../4D/CcAsyncLazywriteWorkerMulti_function_004D1574.md) at `0x004D1967`
- [PopReleaseWakeSourceSpinLock](../4D/PopReleaseWakeSourceSpinLock_function_004D4464.md) at `0x004D4468`
- [NtQueryInformationWorkerFactory](../4D/NtQueryInformationWorkerFactory_function_004D4480.md) at `0x004D4683`
- [CcLogExtraWBThreadAction](../4D/CcLogExtraWBThreadAction_function_004D737C.md) at `0x004D73D5`
- [HalpDmaFlushBufferWithEmergencyResources](../4D/HalpDmaFlushBufferWithEmergencyResources_function_004D8024.md) at `0x004D817D`
- [IoPerfInit](../4D/IoPerfInit_function_004DC338.md) at `0x004DC3AC`
- [HalpDmaSyncMapBuffersWithEmergencyResources](../4D/HalpDmaSyncMapBuffersWithEmergencyResources_function_004DE714.md) at `0x004DE9F6`
- [HalpDmaQueueAdapter](../4E/HalpDmaQueueAdapter_function_004E2B3C.md) at `0x004E2BFC`
- [HalpDmaAllocateScatterPagesFromContiguousPoolV3](../4E/HalpDmaAllocateScatterPagesFromContiguousPoolV3_function_004E380C.md) at `0x004E388F`
- [HalpDmaAllocateScatterPagesFromContiguousPoolV3](../4E/HalpDmaAllocateScatterPagesFromContiguousPoolV3_function_004E380C.md) at `0x004E3911`
- [WmipReceiveNotifications](../4E/WmipReceiveNotifications_function_004EC280.md) at `0x004EC6C8`
- [HalpDmaAllocateContiguousPagesFromContiguousPoolV3](../53/HalpDmaAllocateContiguousPagesFromContiguousPoolV3_function_0053DE24.md) at `0x0053DE85`
- [HalpDmaAllocateContiguousPagesFromContiguousPoolV3](../53/HalpDmaAllocateContiguousPagesFromContiguousPoolV3_function_0053DE24.md) at `0x0053DED9`
- [HalpDmaRemoveAdapterFromMasterQueue](../53/HalpDmaRemoveAdapterFromMasterQueue_function_0053E2FC.md) at `0x0053E395`
- [HalReadDmaCounterV2](../53/HalReadDmaCounterV2_function_0053FB70.md) at `0x0053FBBB`
- [HalpDmaCommitContiguousMapBuffers](../55/HalpDmaCommitContiguousMapBuffers_function_00550A84.md) at `0x00550CC4`
- [CcGetFileObjectFromSectionPtrsRef](../57/CcGetFileObjectFromSectionPtrsRef_function_0057B180.md) at `0x0057B1D2`
- [CcQueueLazyWriteScanThread](../57/CcQueueLazyWriteScanThread_function_0057BBD0.md) at `0x0057BD95`
- [CcQueueLazyWriteScanThread](../57/CcQueueLazyWriteScanThread_function_0057BBD0.md) at `0x0057BDAE`
- [CcQueueLazyWriteScanThread](../57/CcQueueLazyWriteScanThread_function_0057BBD0.md) at `0x0057BDF8`
- [CcRegisterExternalCacheEx](../57/CcRegisterExternalCacheEx_function_0057C0B0.md) at `0x0057C1E4`
- [CcUpdateExternalCacheInfoEx](../57/CcUpdateExternalCacheInfoEx_function_0057C420.md) at `0x0057C535`
- [CcUpdateExternalCacheInfoEx](../57/CcUpdateExternalCacheInfoEx_function_0057C420.md) at `0x0057C598`
- [CcWaitForCurrentLazyWriterActivityOnNode](../57/CcWaitForCurrentLazyWriterActivityOnNode_function_0057C618.md) at `0x0057C750`
- [CcWaitForCurrentLazyWriterActivityOnNode](../57/CcWaitForCurrentLazyWriterActivityOnNode_function_0057C618.md) at `0x0057C770`
- [CcWaitForCurrentLazyWriterActivityOnNode](../57/CcWaitForCurrentLazyWriterActivityOnNode_function_0057C618.md) at `0x0057C7A3`
- [CcDeferWrite](../57/CcDeferWrite_function_0057C860.md) at `0x0057C99A`
- [CcErrorCallbackRoutine](../57/CcErrorCallbackRoutine_function_0057C9D0.md) at `0x0057CA36`
- [CcIsThereDirtyDataEx](../57/CcIsThereDirtyDataEx_function_0057D7B0.md) at `0x0057D86D`
- [CcSetLogHandleForFile](../57/CcSetLogHandleForFile_function_0057D890.md) at `0x0057D9D1`
- [CcMdlWriteAbort](../57/CcMdlWriteAbort_function_0057DA70.md) at `0x0057DAF4`
- [CcDrainDelayDeleteForPartitionExit](../57/CcDrainDelayDeleteForPartitionExit_function_0057DBB0.md) at `0x0057DC31`
- [CcDrainDelayDeleteForPartitionExit](../57/CcDrainDelayDeleteForPartitionExit_function_0057DBB0.md) at `0x0057DC55`
- [CcProcessDelayedDeletePVCM](../57/CcProcessDelayedDeletePVCM_function_0057DCD0.md) at `0x0057DDE2`
- [CcDeletePartition](../57/CcDeletePartition_function_0057DE9C.md) at `0x0057DFBA`
- [CcDeleteSectionsForPartition](../57/CcDeleteSectionsForPartition_function_0057E0F8.md) at `0x0057E14F`
- [CcDeleteSectionsForPartition](../57/CcDeleteSectionsForPartition_function_0057E0F8.md) at `0x0057E1E7`
- [CcDeleteSectionsForPartition](../57/CcDeleteSectionsForPartition_function_0057E0F8.md) at `0x0057E22F`
- [CcDeleteSectionsForPartition](../57/CcDeleteSectionsForPartition_function_0057E0F8.md) at `0x0057E2BE`
- [CcDeleteSectionsForPartition](../57/CcDeleteSectionsForPartition_function_0057E0F8.md) at `0x0057E307`
- [CcDeleteSectionsForPartition](../57/CcDeleteSectionsForPartition_function_0057E0F8.md) at `0x0057E310`
- [CcExitPartition](../57/CcExitPartition_function_0057E340.md) at `0x0057E3EC`
- [CcExitPartition](../57/CcExitPartition_function_0057E340.md) at `0x0057E46D`
- [CcGetDeviceGuidAsync](../57/CcGetDeviceGuidAsync_function_0057ED70.md) at `0x0057EE28`
- [CcCompleteAsyncLazywriteWorker](../57/CcCompleteAsyncLazywriteWorker_function_0057F6AC.md) at `0x0057F71D`
- [CcCompleteAsyncLazywriteWorker](../57/CcCompleteAsyncLazywriteWorker_function_0057F6AC.md) at `0x0057F745`
- [CcCompleteAsyncLazywriteWorkerThread](../57/CcCompleteAsyncLazywriteWorkerThread_function_0057F770.md) at `0x0057F7F2`
- [CcCompleteAsyncWriteBehind](../57/CcCompleteAsyncWriteBehind_function_0057F824.md) at `0x0057F929`
- [CcCompleteAsyncWriteBehind](../57/CcCompleteAsyncWriteBehind_function_0057F824.md) at `0x0057F99F`
- [IopIrpExtensionControl](../59/IopIrpExtensionControl_function_00597558.md) at `0x00597614`
- [IopUpdateFunctionPointers](../59/IopUpdateFunctionPointers_function_0059762C.md) at `0x005976FE`
- [IoCancelMiniCompletionPacket](../59/IoCancelMiniCompletionPacket_function_00598150.md) at `0x0059818F`
- [IoPerfReset](../59/IoPerfReset_function_0059863C.md) at `0x005986AB`
- [KeRemoveEntryDeviceQueue](../5B/KeRemoveEntryDeviceQueue_function_005BE410.md) at `0x005BE484`
- [KiEnableGroupScheduling](../5C/KiEnableGroupScheduling_function_005C8914.md) at `0x005C89D7`
- [KeTraceSchedulingGroupRundown](../5C/KeTraceSchedulingGroupRundown_function_005C8D20.md) at `0x005C8D92`
- [KeTraceSchedulingGroupRundown](../5C/KeTraceSchedulingGroupRundown_function_005C8D20.md) at `0x005C8DF3`
- [KeUpdateGroupSchedulingConstants](../5C/KeUpdateGroupSchedulingConstants_function_005C8E14.md) at `0x005C8F12`
- [PfpPartitionInsertToGlobals](../5C/PfpPartitionInsertToGlobals_function_005CE040.md) at `0x005CE0C6`
- [PfpPartitionRemoveFromGlobals](../5C/PfpPartitionRemoveFromGlobals_function_005CE11C.md) at `0x005CE16B`
- [PopDereferenceWakeInfos](../5D/PopDereferenceWakeInfos_function_005D498C.md) at `0x005D49DD`
- [SepAdtInitLsaDeadEventForNonPagedList](../60/SepAdtInitLsaDeadEventForNonPagedList_function_0060647C.md) at `0x006064C2`
- [DifKeReleaseInStackQueuedSpinLockWrapper](../63/DifKeReleaseInStackQueuedSpinLockWrapper_function_00631670.md) at `0x00631736`
- [ExPoolQueryLimits](../65/ExPoolQueryLimits_function_006562A0.md) at `0x0065643B`
- [ExpPlGrowTableIfNeeded](../65/ExpPlGrowTableIfNeeded_function_00656F14.md) at `0x00656F76`
- [ExpPlGrowTableIfNeeded](../65/ExpPlGrowTableIfNeeded_function_00656F14.md) at `0x00656FE1`
- [ExpPlGrowTableIfNeeded](../65/ExpPlGrowTableIfNeeded_function_00656F14.md) at `0x00657137`
- [ExpTrackTableInsertLimit](../65/ExpTrackTableInsertLimit_function_006572D0.md) at `0x00657505`
- [ExpTryConvertSharedToExclusiveLite](../65/ExpTryConvertSharedToExclusiveLite_function_00658F30.md) at `0x00658FCA`
- [ExpTryToAcquireResourceExclusiveLite](../65/ExpTryToAcquireResourceExclusiveLite_function_00658FEC.md) at `0x006590C3`
- [ExpWorkerFactoryManagerThread](../65/ExpWorkerFactoryManagerThread_function_0065CCC0.md) at `0x0065CD92`
- [ExpWorkerFactoryManagerThread](../65/ExpWorkerFactoryManagerThread_function_0065CCC0.md) at `0x0065CE03`
- [CcMapAndCopyInToCache$fin$1](../6D/CcMapAndCopyInToCache_fin_1_function_006D2AF9.md) at `0x006D2C84`
- [CcCompleteAsyncRead$fin$1](../6D/CcCompleteAsyncRead_fin_1_function_006D3387.md) at `0x006D34BC`
- [CcPerformReadAhead$fin$1](../6D/CcPerformReadAhead_fin_1_function_006D3929.md) at `0x006D39F1`
- [CcPerformReadAhead$fin$1](../6D/CcPerformReadAhead_fin_1_function_006D3929.md) at `0x006D3A45`
- [CcPrepareMdlWrite$fin$0](../6D/CcPrepareMdlWrite_fin_0_function_006D3DF5.md) at `0x006D3F1F`
- [sub_006DEB9E](../6D/Unknown_function_006DEB9E.md) at `0x006DEBBB`
- [sub_006DEB9E](../6D/Unknown_function_006DEB9E.md) at `0x006DEC91`
- [sub_006DEB9E](../6D/Unknown_function_006DEB9E.md) at `0x006DECE1`
- [sub_006DF3C2](../6D/Unknown_function_006DF3C2.md) at `0x006DF3CB`
- [sub_006E2AF2](../6E/Unknown_function_006E2AF2.md) at `0x006E2AFE`
- [sub_006E2B2A](../6E/Unknown_function_006E2B2A.md) at `0x006E2B42`
- [sub_006E2B2A](../6E/Unknown_function_006E2B2A.md) at `0x006E2B4B`
- [sub_006E2C34](../6E/Unknown_function_006E2C34.md) at `0x006E2C55`
- [sub_006E4CFE](../6E/Unknown_function_006E4CFE.md) at `0x006E4D5B`
- [sub_006E4F4E](../6E/Unknown_function_006E4F4E.md) at `0x006E4F81`
- [sub_006E5110](../6E/Unknown_function_006E5110.md) at `0x006E51D7`
- [sub_006E5110](../6E/Unknown_function_006E5110.md) at `0x006E5274`
- [sub_006E53AC](../6E/Unknown_function_006E53AC.md) at `0x006E53B8`
- [sub_006E59DC](../6E/Unknown_function_006E59DC.md) at `0x006E59E4`
- [sub_006E85B0](../6E/Unknown_function_006E85B0.md) at `0x006E85CD`
- [sub_006E85B0](../6E/Unknown_function_006E85B0.md) at `0x006E85FF`
- [sub_006E86B0](../6E/Unknown_function_006E86B0.md) at `0x006E86BF`
- [sub_006E86B0](../6E/Unknown_function_006E86B0.md) at `0x006E86C8`
- [sub_006E86B0](../6E/Unknown_function_006E86B0.md) at `0x006E8773`
- [sub_006E86B0](../6E/Unknown_function_006E86B0.md) at `0x006E877C`
- [sub_006E8790](../6E/Unknown_function_006E8790.md) at `0x006E8815`
- [sub_006E8986](../6E/Unknown_function_006E8986.md) at `0x006E89CF`
- [sub_006E96C4](../6E/Unknown_function_006E96C4.md) at `0x006E971B`
- [sub_006E96C4](../6E/Unknown_function_006E96C4.md) at `0x006E979C`
- [sub_006EA0C0](../6E/Unknown_function_006EA0C0.md) at `0x006EA104`
- [sub_006EA110](../6E/Unknown_function_006EA110.md) at `0x006EA154`
- [sub_006EA22C](../6E/Unknown_function_006EA22C.md) at `0x006EA377`
- [sub_006EA3B0](../6E/Unknown_function_006EA3B0.md) at `0x006EA403`
- [sub_006EA780](../6E/Unknown_function_006EA780.md) at `0x006EA78C`
- [sub_006EC0B0](../6E/Unknown_function_006EC0B0.md) at `0x006EC0B8`
- [sub_006EC29A](../6E/Unknown_function_006EC29A.md) at `0x006EC2CF`
- [sub_006F2A56](../6F/Unknown_function_006F2A56.md) at `0x006F2AFD`
- [sub_006F2A56](../6F/Unknown_function_006F2A56.md) at `0x006F2B0D`
- [sub_006F94DC](../6F/Unknown_function_006F94DC.md) at `0x006F9524`
- [sub_006FCB7E](../6F/Unknown_function_006FCB7E.md) at `0x006FCBD8`
- [PnprMarkOrMirrorPages](../../pagelk/B6/PnprMarkOrMirrorPages_function_00B646A8.md) at `0x00B647C5`
- [KiAddProcessorToGroupSchedulingDatabase](../../pagelk/B6/KiAddProcessorToGroupSchedulingDatabase_function_00B6B1D8.md) at `0x00B6B256`
- [PopBroadcastBlameBugcheckCallback](../../pagelk/B7/PopBroadcastBlameBugcheckCallback_function_00B70B40.md) at `0x00B70C52`
- [PopBroadcastBlameBugcheckCallback](../../pagelk/B7/PopBroadcastBlameBugcheckCallback_function_00B70B40.md) at `0x00B70C5C`
- [sub_00B82950](../../poolcode/B8/Unknown_function_00B82950.md) at `0x00B82C2A`
- [sub_00B8371E](../../poolcode/B8/Unknown_function_00B8371E.md) at `0x00B838CD`

### Static image references
- `0x00342CE6` → RVA `0x00FC6B06` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00342CE0  40 53                           push rbx
00342CE2  48 83 EC 20                     sub rsp, 0x20
00342CE6  F6 05 19 3E C8 00 01            test byte ptr [rip + 0xc83e19], 1
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall KeReleaseInStackQueuedSpinLock(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    return;
}
```

## 5. (Beta) C Style

```c
void KeReleaseInStackQueuedSpinLock(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00342CE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00342CE0[BB_00342CE0]
```
