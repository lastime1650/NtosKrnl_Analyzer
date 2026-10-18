# KeWaitForSingleObject

- RVA: `0x0020E6B0`–`0x0020F6B4` (길이 `4,100` bytes)
- VA: `0x000000014020E6B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005DB44`
- 디코드: `970`개 명령, `4,100/4,100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **58**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **478**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x0020E96B` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0020EC05` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0020EC37` → [KiRcuReportQuiescentState](KiRcuReportQuiescentState_function_0020AB8C.md) (function, `0x0020AB8C`)
- `0x0020EC4B` → [KiRcuFlushCompleted](KiRcuFlushCompleted_function_0020AD38.md) (function, `0x0020AD38`)
- `0x0020EC5D` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0020ECDC` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020ECEB` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020ED57` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0020EDA8` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0020EDB8` → [KiDeliverApc](../25/KiDeliverApc_function_00250F20.md) (function, `0x00250F20`)
- `0x0020EE14` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020EE23` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020EE3B` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020EE4A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020EE97` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0020EEF1` → [KiCommitThreadWait](KiCommitThreadWait_function_0020DFE0.md) (function, `0x0020DFE0`)
- `0x0020EF4D` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0020EF63` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0020EF7B` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020EF8A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020EF97` → [KiAbEntryRemoveFromTree](../26/KiAbEntryRemoveFromTree_function_00262410.md) (function, `0x00262410`)
- `0x0020EFDF` → [Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline](../4E/Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline_function_004EF7C0.md) (function, `0x004EF7C0`)
- `0x0020F065` → [KiSetPriorityThread](../22/KiSetPriorityThread_function_00220E78.md) (function, `0x00220E78`)
- `0x0020F081` → [KiComputeThreadPriorityNonStacking](../5C/KiComputeThreadPriorityNonStacking_function_005CA81C.md) (function, `0x005CA81C`)
- `0x0020F0A8` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020F0B7` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020F0CC` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x0020F0F1` → [KiPerformWaitDeferredWork](../22/KiPerformWaitDeferredWork_function_00220480.md) (function, `0x00220480`)
- `0x0020F114` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0020F135` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0020F1A9` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0020F1C0` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x0020F1D8` → [KiExitThreadWaitReschedule](../35/KiExitThreadWaitReschedule_function_00352EC8.md) (function, `0x00352EC8`)
- `0x0020F1FA` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0020F20E` → [KeAbPostReleaseEx](../26/KeAbPostReleaseEx_function_00262210.md) (function, `0x00262210`)
- `0x0020F226` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x0020F232` → [KiDeliverApc](../25/KiDeliverApc_function_00250F20.md) (function, `0x00250F20`)
- `0x0020F246` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0020F274` → [KiFastExitThreadWait](../22/KiFastExitThreadWait_function_00220BB0.md) (function, `0x00220BB0`)
- `0x0020F27E` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x0020F294` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0020F302` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0020F3D1` → [Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline](../4E/Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline_function_004EF7C0.md) (function, `0x004EF7C0`)
- `0x0020F457` → [KiSetPriorityThread](../22/KiSetPriorityThread_function_00220E78.md) (function, `0x00220E78`)
- `0x0020F473` → [KiComputeThreadPriorityNonStacking](../5C/KiComputeThreadPriorityNonStacking_function_005CA81C.md) (function, `0x005CA81C`)
- `0x0020F49A` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0020F4AA` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0020F4BF` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x0020F4D8` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0020F534` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0020F54C` → [KiExitThreadWaitReschedule](../35/KiExitThreadWaitReschedule_function_00352EC8.md) (function, `0x00352EC8`)
- `0x0020F592` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0020F5A0` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x0020F5AC` → [KiDeliverApc](../25/KiDeliverApc_function_00250F20.md) (function, `0x00250F20`)
- `0x0020F5C0` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0020F5F0` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0020F657` → [KiSrcuReportQuiescent](../5C/KiSrcuReportQuiescent_function_005C2C08.md) (function, `0x005C2C08`)
- `0x0020F668` → [KiSrcuFlushCompleted](../5C/KiSrcuFlushCompleted_function_005C22B4.md) (function, `0x005C22B4`)

### Direct callers
- [KiSchedulerApc](KiSchedulerApc_function_00202BC0.md) at `0x00202CB2`
- [sub_0020D18E](Unknown_function_0020D18E.md) at `0x0020D1AC`
- [sub_0020DEED](Unknown_function_0020DEED.md) at `0x0020DF34`
- [sub_0020E5E6](Unknown_function_0020E5E6.md) at `0x0020E62D`
- [ExfAcquirePushLockExclusiveEx](ExfAcquirePushLockExclusiveEx_function_0020FC90.md) at `0x0020FE20`
- [ExfAcquirePushLockSharedEx](../21/ExfAcquirePushLockSharedEx_function_0021044C.md) at `0x00210638`
- [ExpWaitForResource](../21/ExpWaitForResource_function_002166F0.md) at `0x0021675D`
- [sub_002360DC](../23/Unknown_function_002360DC.md) at `0x00236129`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmFeEvictComplete](../26/SMKM_STORE_MGR_SM_TRAITS_SmFeEvictComplete_function_00266854.md) at `0x00266B1D`
- [PopIrpWorker](../26/PopIrpWorker_function_0026D410.md) at `0x0026D4EA`
- [PopPepUpdateConstraints](../26/PopPepUpdateConstraints_function_0026F5C8.md) at `0x0026F78D`
- [IopCompleteUnloadOrDelete](../27/IopCompleteUnloadOrDelete_function_00270BC8.md) at `0x00270E94`
- [CcSetValidData](../29/CcSetValidData_function_00299420.md) at `0x00299523`
- [MiIssueSynchronousFlush](../29/MiIssueSynchronousFlush_function_0029A588.md) at `0x0029A722`
- [IopAllocateReserveIrp](../29/IopAllocateReserveIrp_function_0029C218.md) at `0x0029C28F`
- [IopAllocateReserveIrp](../29/IopAllocateReserveIrp_function_0029C218.md) at `0x0029C2C3`
- [IopAllocateReserveIrp](../29/IopAllocateReserveIrp_function_0029C218.md) at `0x0029C362`
- [NtSetInformationFile](../29/NtSetInformationFile_function_0029C5E0.md) at `0x0029D06E`
- [IopWaitForSynchronousIo](../29/IopWaitForSynchronousIo_function_0029D6D0.md) at `0x0029D74A`
- [MiZeroPageWrite](../29/MiZeroPageWrite_function_0029F280.md) at `0x0029F41F`
- [ExpUnblockPushLock](../2A/ExpUnblockPushLock_function_002A40FC.md) at `0x002A4205`
- [ExTimedWaitForUnblockPushLock](../2A/ExTimedWaitForUnblockPushLock_function_002A44B0.md) at `0x002A4574`
- [ExfWaitForRundownProtectionRelease](../2A/ExfWaitForRundownProtectionRelease_function_002A4CDC.md) at `0x002A4DC8`
- [MiTrimUnusedPageFileRegionsWorker](../2A/MiTrimUnusedPageFileRegionsWorker_function_002AA320.md) at `0x002AA574`
- [MiTrimUnusedPageFileRegionsWorker](../2A/MiTrimUnusedPageFileRegionsWorker_function_002AA320.md) at `0x002AA6CE`
- [PpmAcquireLock](../2D/PpmAcquireLock_function_002D9AA4.md) at `0x002D9AE3`
- [PopFxActivateComponent](../2D/PopFxActivateComponent_function_002D9DBC.md) at `0x002D9F20`
- [PopExecuteOnTargetProcessors](../2D/PopExecuteOnTargetProcessors_function_002DD834.md) at `0x002DD8CF`
- [PoGetIdleTimes](../2D/PoGetIdleTimes_function_002DF570.md) at `0x002DF866`
- [sub_002F8BF2](../2F/Unknown_function_002F8BF2.md) at `0x002F8C3D`
- [AlpcpSignalAndWait](../2F/AlpcpSignalAndWait_function_002F9620.md) at `0x002F9879`
- [MiBackgroundZeroLocalPages](../31/MiBackgroundZeroLocalPages_function_0031EF30.md) at `0x0031F5EB`
- [CcPinFileData](../33/CcPinFileData_function_0033FB40.md) at `0x0033FC7F`
- [sub_0034D7E9](../34/Unknown_function_0034D7E9.md) at `0x0034D851`
- [sub_0034FCFA](../34/Unknown_function_0034FCFA.md) at `0x0034FD4D`
- [CcWriteBehindAsync](../35/CcWriteBehindAsync_function_003549E8.md) at `0x00354ADD`
- [MiWaitForCollidedFaultComplete](../36/MiWaitForCollidedFaultComplete_function_00369EDC.md) at `0x00369FFA`
- [MiPfCompleteCoalescedIo](../36/MiPfCompleteCoalescedIo_function_0036C344.md) at `0x0036C37A`
- [MiWaitForInPageComplete](../38/MiWaitForInPageComplete_function_00380AB8.md) at `0x00380B7D`
- [WmipFindRegEntryByProviderId](../38/WmipFindRegEntryByProviderId_function_00386908.md) at `0x00386929`
- [CcCanIWrite](../38/CcCanIWrite_function_00388250.md) at `0x00388650`
- [KiInvokeInterruptServiceRoutine](../39/KiInvokeInterruptServiceRoutine_function_0039F8E0.md) at `0x0039F98C`
- [KiInvokeInterruptServiceRoutine](../39/KiInvokeInterruptServiceRoutine_function_0039F8E0.md) at `0x0039FAC2`
- [NtSignalAndWaitForSingleObject](../3A/NtSignalAndWaitForSingleObject_function_003A11D0.md) at `0x003A136D`
- [MiStoreEvictThread](../3A/MiStoreEvictThread_function_003A42D0.md) at `0x003A4332`
- [MiStoreAttemptContractPageFile](../3A/MiStoreAttemptContractPageFile_function_003A4584.md) at `0x003A4674`
- [SmKmStoreHelperCleanup](../3A/SmKmStoreHelperCleanup_function_003AFFE8.md) at `0x003B0018`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStCleanup](../3B/SMKM_STORE_SM_TRAITS_SmStCleanup_function_003B00E0.md) at `0x003B0150`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStCleanup](../3B/SMKM_STORE_SM_TRAITS_SmStCleanup_function_003B00E0.md) at `0x003B01BA`
- [SmKmStoreHelperCheckWaitCommand](../3B/SmKmStoreHelperCheckWaitCommand_function_003B06E0.md) at `0x003B072E`
- [SmKmStoreHelperWaitForCommand](../3B/SmKmStoreHelperWaitForCommand_function_003B075C.md) at `0x003B0792`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStWorkerThreadStartThread](../3B/SMKM_STORE_SM_TRAITS_SmStWorkerThreadStartThread_function_003B200C.md) at `0x003B2104`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmCompressCtxCreateThread](../3B/SMKM_STORE_MGR_SM_TRAITS_SmCompressCtxCreateThread_function_003B2400.md) at `0x003B2545`
- [ExpWaitForFastResource](../3B/ExpWaitForFastResource_function_003BE760.md) at `0x003BE7ED`
- [PpmTryAcquireLock](../3B/PpmTryAcquireLock_function_003BEB9C.md) at `0x003BEBE8`
- [PpmCheckPeriodicStart](../3B/PpmCheckPeriodicStart_function_003BED70.md) at `0x003BED98`
- [SmKmStoreHelperWorker](../3C/SmKmStoreHelperWorker_function_003C2BC0.md) at `0x003C2C69`
- [MiCheckHoldFaultForHotPatch](../3D/MiCheckHoldFaultForHotPatch_function_003D4BA8.md) at `0x003D4C9E`
- [sub_003F374F](../3F/Unknown_function_003F374F.md) at `0x003F379F`
- [sub_00415140](../41/Unknown_function_00415140.md) at `0x0041518F`
- [FsRtlpWaitForIoAtEof](../41/FsRtlpWaitForIoAtEof_function_00415298.md) at `0x00415404`
- [sub_004201AA](../42/Unknown_function_004201AA.md) at `0x00420492`
- [PopWakeDeviceList](../43/PopWakeDeviceList_function_00430238.md) at `0x00430356`
- [PopWakeDeviceList](../43/PopWakeDeviceList_function_00430238.md) at `0x00430405`
- [PopSleepDeviceList](../43/PopSleepDeviceList_function_00430460.md) at `0x0043062A`
- [EtwpCovSampCaptureContextStop](../43/EtwpCovSampCaptureContextStop_function_0043BE5C.md) at `0x0043BF1B`
- [EtwpCovSampCaptureContextStop](../43/EtwpCovSampCaptureContextStop_function_0043BE5C.md) at `0x0043BF68`
- [IopWaitForSynchronousIoEvent](../43/IopWaitForSynchronousIoEvent_function_0043F0F0.md) at `0x0043F162`
- [AlpcpWaitForSingleObject](../43/AlpcpWaitForSingleObject_function_0043F680.md) at `0x0043F6C6`
- [ExpAcquireFastMutexContended](../45/ExpAcquireFastMutexContended_function_00450288.md) at `0x004502DD`
- [SmKmStoreDeleteWhenEmpty](../45/SmKmStoreDeleteWhenEmpty_function_00450D50.md) at `0x00450E81`
- [LdrUnloadAlternateResourceModuleEx](../45/LdrUnloadAlternateResourceModuleEx_function_00454AE4.md) at `0x00454B1F`
- [LdrpGetAlternateResourceModuleHandleEx](../45/LdrpGetAlternateResourceModuleHandleEx_function_00455334.md) at `0x00455375`
- [LdrpGetFromMUIMemCache](../45/LdrpGetFromMUIMemCache_function_00455948.md) at `0x00455A20`
- [LdrpSetAlternateResourceModuleHandle](../45/LdrpSetAlternateResourceModuleHandle_function_00455EBC.md) at `0x00455F36`
- [PopSetWatchdog](../46/PopSetWatchdog_function_00460CAC.md) at `0x0046104B`
- [CcWaitForUninitializeCacheMap](../46/CcWaitForUninitializeCacheMap_function_004633F0.md) at `0x0046355C`
- [ExWaitForRundownProtectionReleaseCacheAware](../46/ExWaitForRundownProtectionReleaseCacheAware_function_004643A0.md) at `0x00464450`
- [WmipFindRegEntryByDevice](../46/WmipFindRegEntryByDevice_function_0046C22C.md) at `0x0046C24A`
- [IopWaitForLockAlertable](../47/IopWaitForLockAlertable_function_0047A684.md) at `0x0047A6C8`
- [WmipDeregisterRegEntry](../47/WmipDeregisterRegEntry_function_0047B568.md) at `0x0047B5AD`
- [WmipDeregisterRegEntry](../47/WmipDeregisterRegEntry_function_0047B568.md) at `0x0047B61F`
- [WmipDeregisterRegEntry](../47/WmipDeregisterRegEntry_function_0047B568.md) at `0x0047B639`
- [MiAttemptPageFileReduction](../48/MiAttemptPageFileReduction_function_004813E4.md) at `0x0048150D`
- [IoSynchronousCallDriver](../48/IoSynchronousCallDriver_function_00484050.md) at `0x004840BA`
- [WheapProcessWorkQueueItem](../48/WheapProcessWorkQueueItem_function_00484820.md) at `0x00484887`
- [CmpDoFileRead](../48/CmpDoFileRead_function_00485658.md) at `0x00485743`
- [PpmCapturePerformanceDistribution](../48/PpmCapturePerformanceDistribution_function_00489C88.md) at `0x00489E8B`
- [WmipBuildTraceDeviceList](../49/WmipBuildTraceDeviceList_function_00494050.md) at `0x0049408A`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmPerformStoreMaintenance](../49/SMKM_STORE_MGR_SM_TRAITS_SmPerformStoreMaintenance_function_00496FD8.md) at `0x004970A9`
- [PnpDeviceCompletionQueueRemoveCompletedRequest](../49/PnpDeviceCompletionQueueRemoveCompletedRequest_function_0049D73C.md) at `0x0049D75A`
- [CmSiWaitForSingleEvent](../49/CmSiWaitForSingleEvent_function_0049E4BC.md) at `0x0049E4D2`
- [PopFxProcessWorkPool](../49/PopFxProcessWorkPool_function_0049E8A0.md) at `0x0049E93B`
- [PopFxActivateDevice](../4A/PopFxActivateDevice_function_004A0DC8.md) at `0x004A0EF1`
- [PopFxActivateDevice](../4A/PopFxActivateDevice_function_004A0DC8.md) at `0x004A0F6A`
- [PopRunMaximumIrpWorkers](../4A/PopRunMaximumIrpWorkers_function_004A1688.md) at `0x004A1748`
- [WmiQueryTraceProviderCount](../4A/WmiQueryTraceProviderCount_function_004A24C8.md) at `0x004A24E4`
- [PnpLockDeviceActionQueue](../4A/PnpLockDeviceActionQueue_function_004A4388.md) at `0x004A4404`
- [FsRtlGetVirtualDiskNestingLevel](../4A/FsRtlGetVirtualDiskNestingLevel_function_004A4530.md) at `0x004A46F2`
- [MiAsyncSlabReplenish](../4A/MiAsyncSlabReplenish_function_004AA54C.md) at `0x004AA695`
- [EtwpTraceThreadRundownWithStack](../4A/EtwpTraceThreadRundownWithStack_function_004AB5A0.md) at `0x004AB6E1`
- [EtwpTraceThreadRundownWithStack](../4A/EtwpTraceThreadRundownWithStack_function_004AB5A0.md) at `0x004AB74C`
- [IoReleaseRemoveLockAndWaitEx](../4B/IoReleaseRemoveLockAndWaitEx_function_004B17B0.md) at `0x004B1811`
- [EtwpStartLoggerThread](../4B/EtwpStartLoggerThread_function_004B25C4.md) at `0x004B2670`
- [WmipAllocRegEntry](../4B/WmipAllocRegEntry_function_004B6D24.md) at `0x004B6D9B`
- [MiQueueSyncModifiedWriterApc](../4B/MiQueueSyncModifiedWriterApc_function_004B70B8.md) at `0x004B7123`
- [MmStoreFlushOutstandingEvictions](../4B/MmStoreFlushOutstandingEvictions_function_004B769C.md) at `0x004B7712`
- [ExUnregisterCallback](../4B/ExUnregisterCallback_function_004B7F80.md) at `0x004B7FD1`
- [PnpDeviceCompletionQueueGetCompletedRequest](../4B/PnpDeviceCompletionQueueGetCompletedRequest_function_004BE224.md) at `0x004BE23F`
- [KiAcquireSecondaryPassiveConnectLock](../4C/KiAcquireSecondaryPassiveConnectLock_function_004C0290.md) at `0x004C02B7`
- [PopFxIssueComponentPerfStateChanges](../4C/PopFxIssueComponentPerfStateChanges_function_004C1940.md) at `0x004C1B28`
- [PnpLockMountableDevice](../4C/PnpLockMountableDevice_function_004CFFAC.md) at `0x004CFFD5`
- [KiSynchronizePassiveInterruptExecution](../4D/KiSynchronizePassiveInterruptExecution_function_004D2444.md) at `0x004D2482`
- [PopCheckPowerSourceAfterRtcWakeCancel](../4D/PopCheckPowerSourceAfterRtcWakeCancel_function_004D7150.md) at `0x004D7173`
- [PopCheckPowerSourceAfterRtcWakeCancel](../4D/PopCheckPowerSourceAfterRtcWakeCancel_function_004D7150.md) at `0x004D71A2`
- [PopHaltDeviceIdle](../4D/PopHaltDeviceIdle_function_004DFFAC.md) at `0x004E0034`
- [PopIgnoreBatteryStatusChange](../4E/PopIgnoreBatteryStatusChange_function_004E347C.md) at `0x004E34B1`
- [FsRtlpWaitOnIrp](../4E/FsRtlpWaitOnIrp_function_004E7998.md) at `0x004E7DC4`
- [WmipReceiveNotifications](../4E/WmipReceiveNotifications_function_004EC280.md) at `0x004EC325`
- [MiQueueWorkingSetRequest](../4F/MiQueueWorkingSetRequest_function_004F7168.md) at `0x004F71FD`
- [IopLoadDriverImage](../4F/IopLoadDriverImage_function_004FA0FC.md) at `0x004FA2DF`
- [HalpAcquireSecondaryIcEntryExclusive](../55/HalpAcquireSecondaryIcEntryExclusive_function_00556C28.md) at `0x00556C58`
- [HalpAcquireSecondaryIcEntryExclusive](../55/HalpAcquireSecondaryIcEntryExclusive_function_00556C28.md) at `0x00556C91`
- [CcQueueLazyWriteScanThread](../57/CcQueueLazyWriteScanThread_function_0057BBD0.md) at `0x0057BE72`
- [CcWaitForCurrentLazyWriterActivityOnNode](../57/CcWaitForCurrentLazyWriterActivityOnNode_function_0057C618.md) at `0x0057C767`
- [CcDeletePartition](../57/CcDeletePartition_function_0057DE9C.md) at `0x0057DF9F`
- [CcDeleteSectionsForPartition](../57/CcDeleteSectionsForPartition_function_0057E0F8.md) at `0x0057E2D5`
- [FsRtlpPostStackOverflow](../58/FsRtlpPostStackOverflow_function_0058351C.md) at `0x00583580`
- [IoWriteCapturedPristineTriageDumpToDedicatedDumpFile](../59/IoWriteCapturedPristineTriageDumpToDedicatedDumpFile_function_005934C0.md) at `0x00593643`
- [IoWriteCapturedPristineTriageDumpToDedicatedDumpFile](../59/IoWriteCapturedPristineTriageDumpToDedicatedDumpFile_function_005934C0.md) at `0x0059368A`
- [IopAllocateBackpocketIrp](../59/IopAllocateBackpocketIrp_function_00596CE0.md) at `0x00596D4E`
- [IopAllocateBackpocketIrp](../59/IopAllocateBackpocketIrp_function_00596CE0.md) at `0x00596E7B`
- [IopIoRingWaitForCompletionEvent](../59/IopIoRingWaitForCompletionEvent_function_0059890C.md) at `0x00598941`
- [IopIoRingWaitForCompletionEvent](../59/IopIoRingWaitForCompletionEvent_function_0059890C.md) at `0x00598990`
- [IopMcWaitAndCleanupBufferEntry](../5A/IopMcWaitAndCleanupBufferEntry_function_005A3F44.md) at `0x005A3F99`
- [PnpSerializeBoot](../5A/PnpSerializeBoot_function_005A4F1C.md) at `0x005A4F61`
- [PnprQuiesce](../5A/PnprQuiesce_function_005A8DE8.md) at `0x005A8E31`
- [PnpProcessRebalance](../5A/PnpProcessRebalance_function_005AA7C8.md) at `0x005AA859`
- [KiSignalWaitDisconnectLock](../5C/KiSignalWaitDisconnectLock_function_005C34DC.md) at `0x005C34F1`
- [KeAbCrossThreadDelete](../5C/KeAbCrossThreadDelete_function_005C517C.md) at `0x005C5546`
- [KeSwapProcessOrStack](../5C/KeSwapProcessOrStack_function_005C5E00.md) at `0x005C5E48`
- [KiStallBugcheckThread](../5C/KiStallBugcheckThread_function_005C7C78.md) at `0x005C7D5A`
- [KiFlushScbReferences](../5C/KiFlushScbReferences_function_005C89E8.md) at `0x005C8ACB`
- [PopIrpWorkerControl](../5D/PopIrpWorkerControl_function_005D93E0.md) at `0x005D93FD`
- [PspIumFreePartitionState](../5E/PspIumFreePartitionState_function_005E48C4.md) at `0x005E4929`
- [SmTerminateStoreProcess](../60/SmTerminateStoreProcess_function_0060EB18.md) at `0x0060EB5D`
- [SmTerminateStoreProcess](../60/SmTerminateStoreProcess_function_0060EB18.md) at `0x0060EBB0`
- [SmpFpWaitForResource](../61/SmpFpWaitForResource_function_006102A4.md) at `0x00610300`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmStoreContentsRundown](../61/SMKM_STORE_MGR_SM_TRAITS_SmStoreContentsRundown_function_00610ADC.md) at `0x00610B8A`
- [SmWaitForSyncIo](../61/SmWaitForSyncIo_function_00611478.md) at `0x00611493`
- [DifKeWaitForSingleObjectWrapper](../63/DifKeWaitForSingleObjectWrapper_function_006336D0.md) at `0x006337D8`
- [ExRegisterBootDevice](../65/ExRegisterBootDevice_function_00657B90.md) at `0x00657BCF`
- [ExpWaitForBootDevices](../65/ExpWaitForBootDevices_function_00657D90.md) at `0x00657DBC`
- [WheapAddErrorSource](../65/WheapAddErrorSource_function_0065E178.md) at `0x0065E196`
- [WheaLogInternalEvent](../66/WheaLogInternalEvent_function_006605B0.md) at `0x00660668`
- [CmpLazyWriteWorker](../66/CmpLazyWriteWorker_function_0066ADF0.md) at `0x0066AE3D`
- [MiReadPagefilePage](../66/MiReadPagefilePage_function_0066F78C.md) at `0x0066F9B3`
- [MmReleaseCommitForMemResetPages](../66/MmReleaseCommitForMemResetPages_function_0066FDCC.md) at `0x0066FF4E`
- [MiContractWsSwapPageFileWorker](../68/MiContractWsSwapPageFileWorker_function_0068B860.md) at `0x0068B906`
- [MiDrainCrossPartitionUsage](../69/MiDrainCrossPartitionUsage_function_00690984.md) at `0x00690A4A`
- [MiDrainCrossPartitionUsage](../69/MiDrainCrossPartitionUsage_function_00690984.md) at `0x00690AA8`
- [MiDrainCrossPartitionUsage](../69/MiDrainCrossPartitionUsage_function_00690984.md) at `0x00690ADB`
- [MiStoreDeletePartition](../69/MiStoreDeletePartition_function_006926F4.md) at `0x0069279C`
- [MiStoreDeletePartition](../69/MiStoreDeletePartition_function_006926F4.md) at `0x006927EF`
- [sub_0069B640](../69/Unknown_function_0069B640.md) at `0x0069B6F9`
- [sub_0069B640](../69/Unknown_function_0069B640.md) at `0x0069B9D8`
- [sub_0069B640](../69/Unknown_function_0069B640.md) at `0x0069BA1E`
- [sub_006D969C](../6D/Unknown_function_006D969C.md) at `0x006D9894`
- [sub_006D969C](../6D/Unknown_function_006D969C.md) at `0x006D98BB`
- [sub_006DA254](../6D/Unknown_function_006DA254.md) at `0x006DA2FA`
- [sub_006DA772](../6D/Unknown_function_006DA772.md) at `0x006DA79E`
- [sub_006E299E](../6E/Unknown_function_006E299E.md) at `0x006E2A66`
- [sub_006E4F4E](../6E/Unknown_function_006E4F4E.md) at `0x006E4FA3`
- [sub_006E532A](../6E/Unknown_function_006E532A.md) at `0x006E5363`
- [sub_006E86B0](../6E/Unknown_function_006E86B0.md) at `0x006E86E1`
- [sub_006EE828](../6E/Unknown_function_006EE828.md) at `0x006EE839`
- [sub_006EE846](../6E/Unknown_function_006EE846.md) at `0x006EE857`
- [sub_006EEFB0](../6E/Unknown_function_006EEFB0.md) at `0x006EF004`
- [sub_006EF0FC](../6E/Unknown_function_006EF0FC.md) at `0x006EF248`
- [sub_006F2A56](../6F/Unknown_function_006F2A56.md) at `0x006F2B25`
- [sub_006F421A](../6F/Unknown_function_006F421A.md) at `0x006F4316`
- [sub_006F4C8C](../6F/Unknown_function_006F4C8C.md) at `0x006F4D50`
- [sub_006F639E](../6F/Unknown_function_006F639E.md) at `0x006F6429`
- [PopPowerAggregatorDozeTimerDisarm](../../page/6F/PopPowerAggregatorDozeTimerDisarm_function_006FE548.md) at `0x006FE5A7`
- [IoCancelFileOpen](../../page/70/IoCancelFileOpen_function_007034A0.md) at `0x0070357F`
- [sub_00703B14](../../page/70/Unknown_function_00703B14.md) at `0x00703BC1`
- [sub_00703ECC](../../page/70/Unknown_function_00703ECC.md) at `0x00703FA4`
- [PnpWaitForEmptyDeviceEventQueue](../../page/70/PnpWaitForEmptyDeviceEventQueue_function_00704350.md) at `0x00704369`
- [HalpSetAcpiRealTimeClock](../../page/70/HalpSetAcpiRealTimeClock_function_00705BFC.md) at `0x00705CC5`
- [HalpDynamicDeviceInterfaceNotification](../../page/70/HalpDynamicDeviceInterfaceNotification_function_00708410.md) at `0x0070845B`
- [HalpDynamicDeviceInterfaceNotification](../../page/70/HalpDynamicDeviceInterfaceNotification_function_00708410.md) at `0x007084C3`
- [HalGetAdapterV3](../../page/70/HalGetAdapterV3_function_00709838.md) at `0x00709B04`
- [HalGetAdapterV2](../../page/70/HalGetAdapterV2_function_00709DD8.md) at `0x00709FFA`
- [HalpQueryAcpiWakeAlarmSystemPowerState](../../page/70/HalpQueryAcpiWakeAlarmSystemPowerState_function_0070B634.md) at `0x0070B6F5`
- [HalpPutAcpiHacksInRegistry](../../page/70/HalpPutAcpiHacksInRegistry_function_0070BC04.md) at `0x0070BCB3`
- [HalpQueryPccInterface](../../page/70/HalpQueryPccInterface_function_0070D79C.md) at `0x0070D896`
- [ArbBuildAssignmentOrdering](../../page/70/ArbBuildAssignmentOrdering_function_0070E43C.md) at `0x0070E4C8`
- [DbgkpLkmdLaunchSnapApc](../../page/71/DbgkpLkmdLaunchSnapApc_function_00711844.md) at `0x0071192D`
- [FsRtlWaitForSmssEvent](../../page/71/FsRtlWaitForSmssEvent_function_007138A0.md) at `0x007138B7`
- [FsRtlBalanceReads](../../page/71/FsRtlBalanceReads_function_00714110.md) at `0x007141A7`
- [FsRtlDeregisterUncProvider](../../page/71/FsRtlDeregisterUncProvider_function_007141C0.md) at `0x007141EC`
- [FsRtlpRegisterUncProvider](../../page/71/FsRtlpRegisterUncProvider_function_007144D0.md) at `0x0071454F`
- [FsRtlIssueFileNotificationFsctl](../../page/71/FsRtlIssueFileNotificationFsctl_function_007161D8.md) at `0x007162CF`
- [NT_DISK::Control](../../page/71/NT_DISK_Control_function_00716FC0.md) at `0x00717085`
- [IopHardErrorThread](../../page/71/IopHardErrorThread_function_0071B690.md) at `0x0071B6B4`
- [IopLoadFileSystemDriver](../../page/71/IopLoadFileSystemDriver_function_0071BB1C.md) at `0x0071BBD1`
- [IopSetRemoteLink](../../page/71/IopSetRemoteLink_function_0071C690.md) at `0x0071C7CB`
- [IoRegisterFsRegistrationChangeMountAware](../../page/71/IoRegisterFsRegistrationChangeMountAware_function_0071D890.md) at `0x0071DA12`
- [IoSetInformation](../../page/71/IoSetInformation_function_0071DBF0.md) at `0x0071DF18`
- [IoSetInformation](../../page/71/IoSetInformation_function_0071DBF0.md) at `0x0071DF55`
- [IopIssueSystemEnvironmentRequest](../../page/72/IopIssueSystemEnvironmentRequest_function_00722878.md) at `0x00722969`
- [PnpShutdownDevices](../../page/72/PnpShutdownDevices_function_00723F20.md) at `0x00723FB9`
- [PnpShutdownDevices](../../page/72/PnpShutdownDevices_function_00723F20.md) at `0x00723FD2`
- [IoReplacePartitionUnit](../../page/72/IoReplacePartitionUnit_function_00727FD0.md) at `0x0072807E`
- [PnpRequestHwProfileChangeNotification](../../page/72/PnpRequestHwProfileChangeNotification_function_00729E78.md) at `0x00729F84`
- [PiPagePathSetState](../../page/72/PiPagePathSetState_function_0072BDE0.md) at `0x0072BE90`
- [IopAllocateBootResources](../../page/72/IopAllocateBootResources_function_0072E680.md) at `0x0072E6BF`
- [PnpWaitForEmptyDeviceActionQueue](../../page/73/PnpWaitForEmptyDeviceActionQueue_function_007375AC.md) at `0x007375C5`
- [PpProfileBeginHardwareProfileTransition](../../page/73/PpProfileBeginHardwareProfileTransition_function_007378E8.md) at `0x00737905`
- [PnpReplacePartitionUnit](../../page/73/PnpReplacePartitionUnit_function_00738550.md) at `0x007385E4`
- [PiIrpQueryRemoveDevice](../../page/73/PiIrpQueryRemoveDevice_function_0073E088.md) at `0x0073E165`
- [PnpReallocateResources](../../page/73/PnpReallocateResources_function_0073E924.md) at `0x0073E983`
- [PipSendGuestAssignedNotification](../../page/74/PipSendGuestAssignedNotification_function_007404B4.md) at `0x00740537`
- [IopWarmEjectDevice](../../page/74/IopWarmEjectDevice_function_007405EC.md) at `0x00740610`
- [PfTCleanup](../../page/75/PfTCleanup_function_00751208.md) at `0x007513D7`
- [PopDisablePowerLimitExtension](../../page/75/PopDisablePowerLimitExtension_function_00756148.md) at `0x007561D8`
- [PopFreePowerLimitRequest](../../page/75/PopFreePowerLimitRequest_function_00756494.md) at `0x00756630`
- [PopDisableCoolingExtension](../../page/75/PopDisableCoolingExtension_function_00757208.md) at `0x007572C4`
- [PopDirectedDripsWorkerRoutine](../../page/75/PopDirectedDripsWorkerRoutine_function_00757DF0.md) at `0x00757E14`
- [PopFxNotifySxTransitionState](../../page/75/PopFxNotifySxTransitionState_function_007593B0.md) at `0x00759433`
- [PopClearHiberFileSignature](../../page/75/PopClearHiberFileSignature_function_0075CD90.md) at `0x0075CE4D`
- [PopCreateHiberFile](../../page/75/PopCreateHiberFile_function_0075CE70.md) at `0x0075D16B`
- [PopCreateHiberFile](../../page/75/PopCreateHiberFile_function_0075CE70.md) at `0x0075D1C1`
- [PopCreateHiberFile](../../page/75/PopCreateHiberFile_function_0075CE70.md) at `0x0075D2B9`
- [PopCreateHiberFile](../../page/75/PopCreateHiberFile_function_0075CE70.md) at `0x0075D2EE`
- [PopSetSystemAwayMode](../../page/75/PopSetSystemAwayMode_function_0075EF00.md) at `0x0075EF7B`
- [PopThermalZoneRemove](../../page/75/PopThermalZoneRemove_function_0075FAD0.md) at `0x0075FAFF`
- [NtInitiatePowerAction](../../page/75/NtInitiatePowerAction_function_0075FCB0.md) at `0x0075FEDB`
- [NtInitiatePowerAction](../../page/75/NtInitiatePowerAction_function_0075FCB0.md) at `0x0075FF03`
- [PopPowerAggregatorSystemTransitionExitStateHandler](../../page/76/PopPowerAggregatorSystemTransitionExitStateHandler_function_00765180.md) at `0x00765209`
- [PopPolicyDeviceHandleWakeAlarmNotification](../../page/76/PopPolicyDeviceHandleWakeAlarmNotification_function_007660A4.md) at `0x007661EB`
- [PopBatteryRemove](../../page/76/PopBatteryRemove_function_00766D40.md) at `0x00766D64`
- [PopBatteryUpdateTestExempt](../../page/76/PopBatteryUpdateTestExempt_function_00766F54.md) at `0x00766FFA`
- [PopBatteryUpdateTestExempt](../../page/76/PopBatteryUpdateTestExempt_function_00766F54.md) at `0x00767106`
- [PopPowerAdapterRemove](../../page/76/PopPowerAdapterRemove_function_00768180.md) at `0x007681D4`
- [PopFanRemove](../../page/76/PopFanRemove_function_007691D0.md) at `0x007691FE`
- [PopEtDeferredInitDxgContext](../../page/76/PopEtDeferredInitDxgContext_function_00769B40.md) at `0x00769C52`
- [SshSessionManagerFlushBuffers](../../page/77/SshSessionManagerFlushBuffers_function_007736D8.md) at `0x00773816`
- [PspQueueDeferredWorkAndWait](../../page/78/PspQueueDeferredWorkAndWait_function_00780148.md) at `0x007801F4`
- [PspShutdownCsrProcess](../../page/78/PspShutdownCsrProcess_function_00780214.md) at `0x007803F6`
- [PsSetVmProcessorHostProcess](../../page/78/PsSetVmProcessorHostProcess_function_00783CEC.md) at `0x00783DCE`
- [PsWaitForAllProcesses](../../page/78/PsWaitForAllProcesses_function_00786318.md) at `0x007863B3`
- [PspWaitForUsermodeExit](../../page/78/PspWaitForUsermodeExit_function_0078661C.md) at `0x0078667A`
- [PspTeardownPartition](../../page/78/PspTeardownPartition_function_00788480.md) at `0x0078859D`
- [PsTerminateVsmEnclave](../../page/78/PsTerminateVsmEnclave_function_00788A64.md) at `0x00788C56`
- [RawPerformDevIoCtrl](../../page/78/RawPerformDevIoCtrl_function_0078A154.md) at `0x0078A208`
- [RawQueryFileSystemInformation](../../page/78/RawQueryFileSystemInformation_function_0078A350.md) at `0x0078A4F2`
- [RtlpRtlpCtWaitForWnfQuiescentWorker](../../page/79/RtlpRtlpCtWaitForWnfQuiescentWorker_function_00794AB0.md) at `0x00794AD0`
- [PdcWaitForEvent](../../page/79/PdcWaitForEvent_function_0079B7B4.md) at `0x0079B7C6`
- [SmProcessResizeRequest](../../page/7A/SmProcessResizeRequest_function_007A6D50.md) at `0x007A6E3E`
- [SmProcessStatsRequest](../../page/7A/SmProcessStatsRequest_function_007A6E68.md) at `0x007A710C`
- [SmStorePhysicalRequestIssue](../../page/7A/SmStorePhysicalRequestIssue_function_007A732C.md) at `0x007A744C`
- [SmKmIsVolumeIoPossible](../../page/7A/SmKmIsVolumeIoPossible_function_007A84BC.md) at `0x007A8535`
- [SmKmSendDeviceControl](../../page/7A/SmKmSendDeviceControl_function_007A8D84.md) at `0x007A8E28`
- [SmKmSendUsageNotification](../../page/7A/SmKmSendUsageNotification_function_007A8E44.md) at `0x007A8EF0`
- [SmKmStoreFileCreate](../../page/7A/SmKmStoreFileCreate_function_007A8F14.md) at `0x007A90D3`
- [SmKmStoreFileCreate](../../page/7A/SmKmStoreFileCreate_function_007A8F14.md) at `0x007A9131`
- [SmKmStoreFileCreate](../../page/7A/SmKmStoreFileCreate_function_007A8F14.md) at `0x007A9189`
- [SmKmStoreFileCreate](../../page/7A/SmKmStoreFileCreate_function_007A8F14.md) at `0x007A9200`
- [SmKmStoreFileDelete](../../page/7A/SmKmStoreFileDelete_function_007A9680.md) at `0x007A96EA`
- [SmKmStoreFileGetExtents](../../page/7A/SmKmStoreFileGetExtents_function_007A971C.md) at `0x007A981A`
- [SmKmStoreFileWriteHeader](../../page/7A/SmKmStoreFileWriteHeader_function_007A9DB4.md) at `0x007A9EE5`
- [SmKmStoreFileWriteHeader](../../page/7A/SmKmStoreFileWriteHeader_function_007A9DB4.md) at `0x007A9F77`
- [IoWMIAllocateInstanceIds](../../page/7B/IoWMIAllocateInstanceIds_function_007B1F70.md) at `0x007B1FBA`
- [WmipGetSysIds](../../page/7B/WmipGetSysIds_function_007B2DB0.md) at `0x007B2DFA`
- [WmipEnumerateGuids](../../page/7B/WmipEnumerateGuids_function_007B3560.md) at `0x007B35AF`
- [WmipProcessLegacyEtwRegister](../../page/7B/WmipProcessLegacyEtwRegister_function_007B3F64.md) at `0x007B3F92`
- [WmipProcessLegacyEtwRegister](../../page/7B/WmipProcessLegacyEtwRegister_function_007B3F64.md) at `0x007B4009`
- [WmipProcessLegacyEtwUnregister](../../page/7B/WmipProcessLegacyEtwUnregister_function_007B404C.md) at `0x007B406E`
- [WmipAddMofResource](../../page/7B/WmipAddMofResource_function_007B4188.md) at `0x007B4289`
- [WmipAddMofResource](../../page/7B/WmipAddMofResource_function_007B4188.md) at `0x007B42F1`
- [WmipWaitForCollectionEnabled](../../page/7B/WmipWaitForCollectionEnabled_function_007B49C0.md) at `0x007B4A06`
- [WmipWaitForCollectionEnabled](../../page/7B/WmipWaitForCollectionEnabled_function_007B49C0.md) at `0x007B4A20`
- [EtwpSetPmcProfileSource](../../page/7B/EtwpSetPmcProfileSource_function_007B8900.md) at `0x007B8942`
- [EtwDereferenceSpinLockCounters](../../page/7B/EtwDereferenceSpinLockCounters_function_007BC2E8.md) at `0x007BC301`
- [EtwReferenceSpinLockCounters](../../page/7B/EtwReferenceSpinLockCounters_function_007BC344.md) at `0x007BC35D`
- [EtwpKsrCallback](../../page/7B/EtwpKsrCallback_function_007BEE10.md) at `0x007BEEB9`
- [ExpQueryPrmInterface](../../page/7C/ExpQueryPrmInterface_function_007CF018.md) at `0x007CF106`
- [ExpWorkQueueDestroy](../../page/7C/ExpWorkQueueDestroy_function_007CFE70.md) at `0x007CFEEB`
- [NtStartProfile](../../page/7D/NtStartProfile_function_007D22C0.md) at `0x007D2335`
- [NtStopProfile](../../page/7D/NtStopProfile_function_007D25C0.md) at `0x007D2620`
- [NtMapCMFModule](../../page/7D/NtMapCMFModule_function_007D4310.md) at `0x007D4A4B`
- [WheaAttemptClearPoison](../../page/7D/WheaAttemptClearPoison_function_007D72A0.md) at `0x007D7340`
- [WheaAttemptPhysicalPageOffline](../../page/7D/WheaAttemptPhysicalPageOffline_function_007D7380.md) at `0x007D7438`
- [WheapProcessWaitingETWEvents](../../page/7D/WheapProcessWaitingETWEvents_function_007D8680.md) at `0x007D86A6`
- [WheapProcessWaitingETWEvents](../../page/7D/WheapProcessWaitingETWEvents_function_007D8680.md) at `0x007D8719`
- [WheaRegChangeNotifyCallback](../../page/7D/WheaRegChangeNotifyCallback_function_007D8A50.md) at `0x007D8B02`
- [CmpFinishSystemHivesLoad](../../page/7D/CmpFinishSystemHivesLoad_function_007DA210.md) at `0x007DA3A2`
- [CmpFinishSystemHivesLoad](../../page/7D/CmpFinishSystemHivesLoad_function_007DA210.md) at `0x007DA993`
- [CmpLoadHiveThread](../../page/7D/CmpLoadHiveThread_function_007DB040.md) at `0x007DB102`
- [CmpLoadHiveThread](../../page/7D/CmpLoadHiveThread_function_007DB040.md) at `0x007DB126`
- [CmCompleteRegistryInitialization](../../page/7D/CmCompleteRegistryInitialization_function_007DF1EC.md) at `0x007DF30A`
- [CmpDummyThreadRoutine](../../page/7E/CmpDummyThreadRoutine_function_007E8140.md) at `0x007E8159`
- [MiInsertPageFileInList](../../page/7F/MiInsertPageFileInList_function_007FFF80.md) at `0x008001AD`
- [MiZeroPageFileFirstPage](../../page/80/MiZeroPageFileFirstPage_function_00800678.md) at `0x0080072C`
- [MiInjectThreadForHotPatch](../../page/80/MiInjectThreadForHotPatch_function_00803FD8.md) at `0x0080413C`
- [CancelTimerCallbacksAndDeleteTimer](../../page/83/CancelTimerCallbacksAndDeleteTimer_function_00835ED4.md) at `0x00835F16`
- [VhdVerifyBootDisk](../../page/83/VhdVerifyBootDisk_function_0083BB84.md) at `0x0083BC74`
- [VhdiMountVhdFile](../../page/83/VhdiMountVhdFile_function_0083BED0.md) at `0x0083C102`
- [VhdiMountVhdFile](../../page/83/VhdiMountVhdFile_function_0083BED0.md) at `0x0083C38B`
- [VhdiMountVhdFile](../../page/83/VhdiMountVhdFile_function_0083BED0.md) at `0x0083C458`
- [sub_00863F57](../../page/86/Unknown_function_00863F57.md) at `0x00863F69`
- [IopCloseFile](../../page/86/IopCloseFile_function_008640C0.md) at `0x00864218`
- [ObWaitForSingleObject](../../page/86/ObWaitForSingleObject_function_00868C50.md) at `0x00868D0A`
- [IopGetSetSecurityObject](../../page/87/IopGetSetSecurityObject_function_00873A80.md) at `0x00873C49`
- [IopGetSetSecurityObject](../../page/87/IopGetSetSecurityObject_function_00873A80.md) at `0x00873D4C`
- [CmLoadAppKey](../../page/87/CmLoadAppKey_function_00876FFC.md) at `0x00877308`
- [CmpGetVolumeClusterSize](../../page/87/CmpGetVolumeClusterSize_function_0087B3D4.md) at `0x0087B52D`
- [AlpcpReceiveMessagePort](../../page/89/AlpcpReceiveMessagePort_function_00896B40.md) at `0x00896E7F`
- [AlpcpReceiveMessagePort](../../page/89/AlpcpReceiveMessagePort_function_00896B40.md) at `0x00896F56`
- [AlpcpReceiveMessagePort](../../page/89/AlpcpReceiveMessagePort_function_00896B40.md) at `0x00897113`
- [CmpParseKey](../../page/89/CmpParseKey_function_0089DDC0.md) at `0x0089E479`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x0089FA90`
- [DbgkpQueueMessage](../../page/8A/DbgkpQueueMessage_function_008A31C0.md) at `0x008A33B0`
- [IoVolumeDeviceToDosName](../../page/8A/IoVolumeDeviceToDosName_function_008A63F0.md) at `0x008A66FF`
- [IoVolumeDeviceToDosName](../../page/8A/IoVolumeDeviceToDosName_function_008A63F0.md) at `0x008A671D`
- [IoVolumeDeviceToDosName](../../page/8A/IoVolumeDeviceToDosName_function_008A63F0.md) at `0x008A6745`
- [IopQueryNameInternal](../../page/8A/IopQueryNameInternal_function_008A6770.md) at `0x008A69FD`
- [sub_008A8A27](../../page/8A/Unknown_function_008A8A27.md) at `0x008A8B37`
- [IopSynchronousApiServiceTail](../../page/8A/IopSynchronousApiServiceTail_function_008ACE3C.md) at `0x008ACEAB`
- [sub_008AD582](../../page/8A/Unknown_function_008AD582.md) at `0x008AD5D4`
- [NtQueryInformationFile](../../page/8A/NtQueryInformationFile_function_008AD630.md) at `0x008ADDC2`
- [NtQueryInformationFile](../../page/8A/NtQueryInformationFile_function_008AD630.md) at `0x008ADF45`
- [IopCancelIrpsInThreadList](../../page/8C/IopCancelIrpsInThreadList_function_008C9E18.md) at `0x008C9EC1`
- [IopCancelIrpsInThreadList](../../page/8C/IopCancelIrpsInThreadList_function_008C9E18.md) at `0x008C9F38`
- [PspSetContextThreadInternal](../../page/8D/PspSetContextThreadInternal_function_008D4420.md) at `0x008D46FD`
- [PspGetContextThreadInternal](../../page/8D/PspGetContextThreadInternal_function_008D4770.md) at `0x008D4976`
- [PspUserThreadStartup](../../page/8D/PspUserThreadStartup_function_008D5B10.md) at `0x008D5BEE`
- [IopSynchronousCall](../../page/8F/IopSynchronousCall_function_008FB018.md) at `0x008FB12C`
- [IopUncacheInterfaceInformation](../../page/8F/IopUncacheInterfaceInformation_function_008FCC28.md) at `0x008FCC77`
- [PnpStartDeviceNode](../../page/8F/PnpStartDeviceNode_function_008FE38C.md) at `0x008FE5B5`
- [IoDisconnectInterrupt](../../page/90/IoDisconnectInterrupt_function_00900890.md) at `0x00900912`
- [IopConnectInterrupt](../../page/90/IopConnectInterrupt_function_00900B40.md) at `0x00900C6E`
- [IopDestroyActiveConnectBlock](../../page/90/IopDestroyActiveConnectBlock_function_00900FE8.md) at `0x0090107A`
- [IopDestroyActiveConnectBlock](../../page/90/IopDestroyActiveConnectBlock_function_00900FE8.md) at `0x009010FF`
- [IopInitializeActiveConnectBlock](../../page/90/IopInitializeActiveConnectBlock_function_00901138.md) at `0x009011D0`
- [PspExitLastThread](../../page/90/PspExitLastThread_function_00904184.md) at `0x009043CC`
- [DbgkpSendErrorMessage](../../page/92/DbgkpSendErrorMessage_function_009210A8.md) at `0x009211DA`
- [PiDrvDbLoadNode](../../page/93/PiDrvDbLoadNode_function_00931AB0.md) at `0x00931BFF`
- [EtwpAcquireLoggerContext](../../page/93/EtwpAcquireLoggerContext_function_009326AC.md) at `0x009327F0`
- [EtwpAcquireLoggerContextByLoggerName](../../page/93/EtwpAcquireLoggerContextByLoggerName_function_0093283C.md) at `0x009328DA`
- [sub_0093299F](../../page/93/Unknown_function_0093299F.md) at `0x009329EC`
- [VrpWaitForDiffHiveEntryTransitionOwnerToLeave](../../page/93/VrpWaitForDiffHiveEntryTransitionOwnerToLeave_function_00937128.md) at `0x009371BF`
- [PnpQueueQueryAndRemoveEvent](../../page/94/PnpQueueQueryAndRemoveEvent_function_0094FD2C.md) at `0x0094FF1C`
- [IoVolumeDeviceToGuidPath](../../page/95/IoVolumeDeviceToGuidPath_function_00952B20.md) at `0x00952C9D`
- [IoVolumeDeviceNameToGuidPath](../../page/95/IoVolumeDeviceNameToGuidPath_function_00952CC0.md) at `0x00953012`
- [IoVolumeDeviceNameToGuidPath](../../page/95/IoVolumeDeviceNameToGuidPath_function_00952CC0.md) at `0x00953030`
- [Pdcv2ActivationClientActivate](../../page/95/Pdcv2ActivationClientActivate_function_00953C70.md) at `0x00953D5E`
- [Pdcv2ActivationClientDeactivate](../../page/95/Pdcv2ActivationClientDeactivate_function_009552E0.md) at `0x0095536D`
- [PnpDeviceEventWorker](../../page/95/PnpDeviceEventWorker_function_009556B0.md) at `0x0095570F`
- [PnpWatchdogTimerPause](../../page/95/PnpWatchdogTimerPause_function_00955B6C.md) at `0x00955C18`
- [WdtpCancelTimer](../../page/95/WdtpCancelTimer_function_00955C70.md) at `0x00955CC9`
- [EtwpCoverageSamplerQuery](../../page/95/EtwpCoverageSamplerQuery_function_0095C4A0.md) at `0x0095C5D2`
- [SPCallServerHandleQueryPolicy](../../page/96/SPCallServerHandleQueryPolicy_function_0096AF24.md) at `0x0096B483`
- [sub_0096C058](../../page/96/Unknown_function_0096C058.md) at `0x0096C1A5`
- [sub_0096C058](../../page/96/Unknown_function_0096C058.md) at `0x0096C1D6`
- [FsRtlSetFileSize](../../page/98/FsRtlSetFileSize_function_00982B04.md) at `0x00982BF5`
- [FsRtlGetFileSize](../../page/98/FsRtlGetFileSize_function_00985150.md) at `0x009852C6`
- [MiReadImageHeaders](../../page/98/MiReadImageHeaders_function_00987DAC.md) at `0x00987E6D`
- [IopInvalidateVolumesForDevice](../../page/9A/IopInvalidateVolumesForDevice_function_009A5E74.md) at `0x009A5EF8`
- [IopInvalidateVolumesForDevice](../../page/9A/IopInvalidateVolumesForDevice_function_009A5E74.md) at `0x009A609C`
- [CmpFileFlushAndPurge](../../page/9B/CmpFileFlushAndPurge_function_009B2BAC.md) at `0x009B2CFE`
- [CmpLockRegistryFreezeAware](../../page/9B/CmpLockRegistryFreezeAware_function_009B4AE4.md) at `0x009B4B9F`
- [EtwpStopTrace](../../page/9B/EtwpStopTrace_function_009BCE84.md) at `0x009BD007`
- [EtwpStopTrace](../../page/9B/EtwpStopTrace_function_009BCE84.md) at `0x009BD043`
- [EtwpLogger](../../page/9B/EtwpLogger_function_009BE310.md) at `0x009BE6BD`
- [NtNotifyChangeMultipleKeys](../../page/9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) at `0x009DCEE4`
- [WmipUpdateDataSource](../../page/9D/WmipUpdateDataSource_function_009DD474.md) at `0x009DD4F2`
- [WmipUpdateDataSource](../../page/9D/WmipUpdateDataSource_function_009DD474.md) at `0x009DD64D`
- [WmipRegistrationWorker](../../page/9D/WmipRegistrationWorker_function_009DD820.md) at `0x009DD84B`
- [WmipRegistrationWorker](../../page/9D/WmipRegistrationWorker_function_009DD820.md) at `0x009DD89E`
- [WmipAddDataSource](../../page/9D/WmipAddDataSource_function_009DDC30.md) at `0x009DDD79`
- [WmipQueryGuidInfo](../../page/9D/WmipQueryGuidInfo_function_009DE66C.md) at `0x009DE6DB`
- [WmipDisableCollectionForRemovedGuid](../../page/9D/WmipDisableCollectionForRemovedGuid_function_009DE88C.md) at `0x009DE8EE`
- [WmipDisableCollectionForRemovedGuid](../../page/9D/WmipDisableCollectionForRemovedGuid_function_009DE88C.md) at `0x009DE9B1`
- [WmipIncludeStaticNames](../../page/9D/WmipIncludeStaticNames_function_009DF754.md) at `0x009DF7BC`
- [WmipProcessEvent](../../page/9D/WmipProcessEvent_function_009DFA40.md) at `0x009DFAC0`
- [WmipEnableCollectionForNewGuid](../../page/9D/WmipEnableCollectionForNewGuid_function_009DFC0C.md) at `0x009DFC6E`
- [WmipEnableCollectionForNewGuid](../../page/9D/WmipEnableCollectionForNewGuid_function_009DFC0C.md) at `0x009DFD2A`
- [WmipIsQuerySetGuid](../../page/9D/WmipIsQuerySetGuid_function_009DFEB0.md) at `0x009DFED3`
- [WmipOpenBlock](../../page/9E/WmipOpenBlock_function_009E00D0.md) at `0x009E016F`
- [WmipOpenBlock](../../page/9E/WmipOpenBlock_function_009E00D0.md) at `0x009E0254`
- [WmipFindGEByGuid](../../page/9E/WmipFindGEByGuid_function_009E03A4.md) at `0x009E03CE`
- [WmipUnreferenceEntry](../../page/9E/WmipUnreferenceEntry_function_009E0CC8.md) at `0x009E0CF2`
- [WmipForwardWmiIrp](../../page/9E/WmipForwardWmiIrp_function_009E0DB4.md) at `0x009E0F94`
- [WmipPrepareWnodeSI](../../page/9E/WmipPrepareWnodeSI_function_009E1740.md) at `0x009E1818`
- [WmipPrepareForWnodeAD](../../page/9E/WmipPrepareForWnodeAD_function_009E1A48.md) at `0x009E1AC5`
- [WmipEnableCollectOrEvent](../../page/9E/WmipEnableCollectOrEvent_function_009E221C.md) at `0x009E2258`
- [WmipEnableCollectOrEvent](../../page/9E/WmipEnableCollectOrEvent_function_009E221C.md) at `0x009E22D7`
- [WmipUpdateDeviceStackSize](../../page/9E/WmipUpdateDeviceStackSize_function_009E23B0.md) at `0x009E23CD`
- [WmipDSCleanup](../../page/9E/WmipDSCleanup_function_009E2400.md) at `0x009E2437`
- [WmipDSCleanup](../../page/9E/WmipDSCleanup_function_009E2400.md) at `0x009E254D`
- [WmipDeleteMethod](../../page/9E/WmipDeleteMethod_function_009E25E0.md) at `0x009E2618`
- [WmipDeleteMethod](../../page/9E/WmipDeleteMethod_function_009E25E0.md) at `0x009E2693`
- [WmipDisableCollectOrEvent](../../page/9E/WmipDisableCollectOrEvent_function_009E26D0.md) at `0x009E2705`
- [WmipDetermineInstanceBaseIndex](../../page/9E/WmipDetermineInstanceBaseIndex_function_009E2740.md) at `0x009E276B`
- [WmipRegisterDevice](../../page/9E/WmipRegisterDevice_function_009E2808.md) at `0x009E2858`
- [WmipSendWmiIrpToTraceDeviceList](../../page/9E/WmipSendWmiIrpToTraceDeviceList_function_009E2988.md) at `0x009E29C5`
- [WmipQueueRegWork](../../page/9E/WmipQueueRegWork_function_009E2AC4.md) at `0x009E2B1B`
- [WmipFindISinGEbyName](../../page/9E/WmipFindISinGEbyName_function_009E2BF0.md) at `0x009E2C3B`
- [IoWMIRegistrationControl](../../page/9E/IoWMIRegistrationControl_function_009E2D60.md) at `0x009E2E52`
- [WmipLegacyEtwWorker](../../page/9E/WmipLegacyEtwWorker_function_009E3290.md) at `0x009E32BC`
- [WmipLegacyEtwWorker](../../page/9E/WmipLegacyEtwWorker_function_009E3290.md) at `0x009E335C`
- [WmipLegacyEtwCallback](../../page/9E/WmipLegacyEtwCallback_function_009E3480.md) at `0x009E34C4`
- [WmipSendEnableDisableRequest](../../page/9E/WmipSendEnableDisableRequest_function_009E3800.md) at `0x009E396E`
- [EtwpEnableDisableUMGL](../../page/9E/EtwpEnableDisableUMGL_function_009E3C88.md) at `0x009E3D26`
- [EtwpUpdateDisallowedGuids](../../page/9E/EtwpUpdateDisallowedGuids_function_009EA8FC.md) at `0x009EAA08`
- [PopInitSystemSleeperThread](../../page/9E/PopInitSystemSleeperThread_function_009ECBA8.md) at `0x009ECCB2`
- [FsRtlCancellableWaitForMultipleObjects](../../page/9F/FsRtlCancellableWaitForMultipleObjects_function_009F1EE0.md) at `0x009F1FA7`
- [IopLegacyResourceAllocation](../../page/A0/IopLegacyResourceAllocation_function_00A07224.md) at `0x00A07286`
- [FsRtlQueryKernelEaFile](../../page/A0/FsRtlQueryKernelEaFile_function_00A0C680.md) at `0x00A0C7E7`
- [FsRtlQueryKernelEaFile](../../page/A0/FsRtlQueryKernelEaFile_function_00A0C680.md) at `0x00A0C859`
- [FsRtlSetKernelEaFile](../../page/A0/FsRtlSetKernelEaFile_function_00A0C8B0.md) at `0x00A0C9C0`
- [FsRtlSetKernelEaFile](../../page/A0/FsRtlSetKernelEaFile_function_00A0C8B0.md) at `0x00A0CA22`
- [FsRtlKernelFsControlFile](../../page/A0/FsRtlKernelFsControlFile_function_00A0CA70.md) at `0x00A0CC80`
- [FsRtlKernelFsControlFile](../../page/A0/FsRtlKernelFsControlFile_function_00A0CA70.md) at `0x00A0CD7D`
- [MmCleanProcessAddressSpace](../../page/A1/MmCleanProcessAddressSpace_function_00A17EC0.md) at `0x00A1814F`
- [FsRtlCancellableWaitForSingleObject](../../page/A1/FsRtlCancellableWaitForSingleObject_function_00A1D890.md) at `0x00A1D8EF`
- [EtwpDisableTraceProviders](../../page/A2/EtwpDisableTraceProviders_function_00A22680.md) at `0x00A2272D`
- [IopInsertLegacyBusDeviceNode](../../page/A2/IopInsertLegacyBusDeviceNode_function_00A28154.md) at `0x00A281AF`
- [PnpQueryInterface](../../page/A2/PnpQueryInterface_function_00A28D38.md) at `0x00A28E94`
- [PnpAllocateResources](../../page/A2/PnpAllocateResources_function_00A2ACC4.md) at `0x00A2AD28`
- [IopAcquireReleaseDispatcherLock](../../page/A2/IopAcquireReleaseDispatcherLock_function_00A2BA60.md) at `0x00A2BA8D`
- [IopMountVolume](../../page/A3/IopMountVolume_function_00A329D0.md) at `0x00A32F5A`
- [IopGetSetObjectId](../../page/A3/IopGetSetObjectId_function_00A37190.md) at `0x00A37282`
- [IopGetVolumeId](../../page/A3/IopGetVolumeId_function_00A372CC.md) at `0x00A373DB`
- [FsRtlQueryInformationFile](../../page/A3/FsRtlQueryInformationFile_function_00A38780.md) at `0x00A38895`
- [FsRtlQueryInformationFile](../../page/A3/FsRtlQueryInformationFile_function_00A38780.md) at `0x00A38907`
- [FsRtlQueryCachedVdl](../../page/A4/FsRtlQueryCachedVdl_function_00A45570.md) at `0x00A4565F`
- [NtWaitForDebugEvent](../../page/A4/NtWaitForDebugEvent_function_00A464E0.md) at `0x00A4660C`
- [PopDirectedDripsAcquireTransitionLock](../../page/A4/PopDirectedDripsAcquireTransitionLock_function_00A4D5D8.md) at `0x00A4D607`
- [EtwpUpdateGlobalGroupMasks](../../page/A4/EtwpUpdateGlobalGroupMasks_function_00A4F55C.md) at `0x00A4F5B5`
- [SmStoreCompressionStop](../../page/A6/SmStoreCompressionStop_function_00A6197C.md) at `0x00A61A4E`
- [MiInSwapStore](../../page/A6/MiInSwapStore_function_00A61B74.md) at `0x00A61C33`
- [FsRtlGetSectorSizeInformation](../../page/A6/FsRtlGetSectorSizeInformation_function_00A62EB0.md) at `0x00A633E6`
- [FsRtlGetSectorSizeInformation](../../page/A6/FsRtlGetSectorSizeInformation_function_00A62EB0.md) at `0x00A63406`
- [FsRtlGetSectorSizeInformation](../../page/A6/FsRtlGetSectorSizeInformation_function_00A62EB0.md) at `0x00A63423`
- [FsRtlGetSectorSizeInformation](../../page/A6/FsRtlGetSectorSizeInformation_function_00A62EB0.md) at `0x00A63443`
- [FsRtlGetSectorSizeInformation](../../page/A6/FsRtlGetSectorSizeInformation_function_00A62EB0.md) at `0x00A63476`
- [FsRtlIssueDeviceIoControl](../../page/A6/FsRtlIssueDeviceIoControl_function_00A634C0.md) at `0x00A635BC`
- [PdcAcquireRwLockExclusive2](../../page/A6/PdcAcquireRwLockExclusive2_function_00A65230.md) at `0x00A65266`
- [EtwpSynchronizeWithLogger](../../page/A6/EtwpSynchronizeWithLogger_function_00A66250.md) at `0x00A662A5`
- [IoReportTargetDeviceChange](../../page/A6/IoReportTargetDeviceChange_function_00A66F20.md) at `0x00A6704C`
- [EtwpUpdatePerProcessTracing](../../page/A6/EtwpUpdatePerProcessTracing_function_00A67374.md) at `0x00A673B7`
- [ExSwapinWorkerThreads](../../page/A6/ExSwapinWorkerThreads_function_00A68C40.md) at `0x00A68D80`
- [ExSwapinWorkerThreads](../../page/A6/ExSwapinWorkerThreads_function_00A68C40.md) at `0x00A68DBD`
- [NtWaitForKeyedEvent](../../page/A7/NtWaitForKeyedEvent_function_00A71D50.md) at `0x00A71F2E`
- [NtWaitForKeyedEvent](../../page/A7/NtWaitForKeyedEvent_function_00A71D50.md) at `0x00A72010`
- [NtNotifyChangeSession](../../page/A7/NtNotifyChangeSession_function_00A7E630.md) at `0x00A7E711`
- [NtNotifyChangeSession](../../page/A7/NtNotifyChangeSession_function_00A7E630.md) at `0x00A7E8AC`
- [EtwpSampledProfileRunDown](../../page/A7/EtwpSampledProfileRunDown_function_00A7F60C.md) at `0x00A7F685`
- [WmipDeregisterDevice](../../page/A7/WmipDeregisterDevice_function_00A7F9D4.md) at `0x00A7FA00`
- [EtwpCrimsonProvEnableCallback](../../page/A8/EtwpCrimsonProvEnableCallback_function_00A80540.md) at `0x00A80589`
- [PopBsdFlush](../../page/A8/PopBsdFlush_function_00A82624.md) at `0x00A8265C`
- [PopBsdFlush](../../page/A8/PopBsdFlush_function_00A82624.md) at `0x00A82688`
- [WmipGetGuidObjectInstanceInfo](../../page/A8/WmipGetGuidObjectInstanceInfo_function_00A87470.md) at `0x00A874FC`
- [PopFxUnregisterDeviceOrWait](../../page/A8/PopFxUnregisterDeviceOrWait_function_00A8AD00.md) at `0x00A8AD3A`
- [PopFxUnregisterDevice](../../page/A8/PopFxUnregisterDevice_function_00A8AE84.md) at `0x00A8AEF3`
- [PopPepUnregisterDevice](../../page/A8/PopPepUnregisterDevice_function_00A8B048.md) at `0x00A8B098`
- [IopCreateArcName](../../page/A8/IopCreateArcName_function_00A8D580.md) at `0x00A8D925`
- [IopCreateArcName](../../page/A8/IopCreateArcName_function_00A8D580.md) at `0x00A8D942`
- [IopCreateArcName](../../page/A8/IopCreateArcName_function_00A8D580.md) at `0x00A8D962`
- [IopCreateArcName](../../page/A8/IopCreateArcName_function_00A8D580.md) at `0x00A8D995`
- [PopResizeHiberFile](../../page/A9/PopResizeHiberFile_function_00A90410.md) at `0x00A90578`
- [PopResizeHiberFile](../../page/A9/PopResizeHiberFile_function_00A90410.md) at `0x00A905A1`
- [PopSanityCheckHiberFile](../../page/A9/PopSanityCheckHiberFile_function_00A90840.md) at `0x00A9091D`
- [IopFilterResourceRequirementsCall](../../page/A9/IopFilterResourceRequirementsCall_function_00A92388.md) at `0x00A924A4`
- [WmipEnumerateMofResources](../../page/A9/WmipEnumerateMofResources_function_00A94410.md) at `0x00A9444A`
- [IopCancelAlertedRequest](../../page/A9/IopCancelAlertedRequest_function_00A948F8.md) at `0x00A949BE`
- [CmFcpManagerPublishFeatureUsageDataBuffers](../../page/A9/CmFcpManagerPublishFeatureUsageDataBuffers_function_00A9677C.md) at `0x00A967B0`
- [HalpQueryAcpiRealTimeClock](../../page/A9/HalpQueryAcpiRealTimeClock_function_00A98230.md) at `0x00A9830B`
- [HalpGetDynamicDevicePointer](../../page/A9/HalpGetDynamicDevicePointer_function_00A983AC.md) at `0x00A983DD`
- [EtwpStartTrace](../../page/A9/EtwpStartTrace_function_00A99D08.md) at `0x00A99D46`
- [EtwpStartLogger](../../page/A9/EtwpStartLogger_function_00A99D80.md) at `0x00A9AD29`
- [CmpWaitOnHiveWriteQueue](../../page/AA/CmpWaitOnHiveWriteQueue_function_00AA0110.md) at `0x00AA0190`
- [RawQueryFsSizeInfo](../../page/AA/RawQueryFsSizeInfo_function_00AA1DC8.md) at `0x00AA1FD2`
- [RawQueryFsSizeInfo](../../page/AA/RawQueryFsSizeInfo_function_00AA1DC8.md) at `0x00AA1FFA`
- [PnpSynchronizeDeviceEventQueue](../../page/AA/PnpSynchronizeDeviceEventQueue_function_00AA4F60.md) at `0x00AA4FEF`
- [PopIdleWakeNotifyModernStandbyExitWorker](../../page/AA/PopIdleWakeNotifyModernStandbyExitWorker_function_00AA55E0.md) at `0x00AA564D`
- [PopAcquireTransitionLock](../../page/AA/PopAcquireTransitionLock_function_00AA9E7C.md) at `0x00AA9EA0`
- [HalpCallWakeAlarmDriver](../../page/AA/HalpCallWakeAlarmDriver_function_00AAF5E0.md) at `0x00AAF6A8`
- [WmipFindMRByNames](../../page/AB/WmipFindMRByNames_function_00AB0054.md) at `0x00AB007E`
- [PopPowerAggregatorNotifySuspendResume](../../page/AB/PopPowerAggregatorNotifySuspendResume_function_00AB9728.md) at `0x00AB97BC`
- [PopGetWakeSource](../../page/AB/PopGetWakeSource_function_00ABDB68.md) at `0x00ABDBB8`
- [WmipSetTraceNotify](../../page/AB/WmipSetTraceNotify_function_00ABF0E0.md) at `0x00ABF168`
- [IopUnloadDriver](../../page/AB/IopUnloadDriver_function_00ABF868.md) at `0x00ABFC49`
- [IopSendMessageToTrackService](../../page/AC/IopSendMessageToTrackService_function_00AC0E5C.md) at `0x00AC0EE8`
- [IopSendMessageToTrackService](../../page/AC/IopSendMessageToTrackService_function_00AC0E5C.md) at `0x00AC0F59`
- [IopSendMessageToTrackService](../../page/AC/IopSendMessageToTrackService_function_00AC0E5C.md) at `0x00AC109F`
- [IoWMISetNotificationCallback](../../page/AC/IoWMISetNotificationCallback_function_00AC8390.md) at `0x00AC83BD`
- [PopReadPagesFromHiberFile](../../page/AC/PopReadPagesFromHiberFile_function_00AC8F78.md) at `0x00AC9166`
- [FsRtlGetDirectImageOriginalBase](../../page/AC/FsRtlGetDirectImageOriginalBase_function_00AC9C70.md) at `0x00AC9D43`
- [ArbArbiterHandler](../../page/AC/ArbArbiterHandler_function_00ACCFD0.md) at `0x00ACD00A`
- [EmPowerPagingEnabled](../../page/AC/EmPowerPagingEnabled_function_00ACE36C.md) at `0x00ACE444`
- [WmipProcessSynchronousEtw](../../page/AC/WmipProcessSynchronousEtw_function_00ACE5FC.md) at `0x00ACE6B2`
- [WmipDereferenceEvent](../../page/AC/WmipDereferenceEvent_function_00ACE6E4.md) at `0x00ACE714`
- [IoVerifyVolume](../../page/AC/IoVerifyVolume_function_00ACF200.md) at `0x00ACF261`
- [IoVerifyVolume](../../page/AC/IoVerifyVolume_function_00ACF200.md) at `0x00ACF352`
- [PiQueueDeviceRequest](../../page/AD/PiQueueDeviceRequest_function_00AD1878.md) at `0x00AD1952`
- [PiQueueDeviceRequest](../../page/AD/PiQueueDeviceRequest_function_00AD1878.md) at `0x00AD1998`
- [PopPowerRequestNotifyTtmSessionUninitialized](../../page/AD/PopPowerRequestNotifyTtmSessionUninitialized_function_00AD2B30.md) at `0x00AD2B6B`
- [EtwpGetPmcProfileSource](../../page/AD/EtwpGetPmcProfileSource_function_00ADC6EC.md) at `0x00ADC71E`
- [IopFreeBandwidthContract](../../page/AD/IopFreeBandwidthContract_function_00ADC7B4.md) at `0x00ADC8F1`
- [PopDeactiveThermalRequest](../../page/AD/PopDeactiveThermalRequest_function_00ADF634.md) at `0x00ADF7DD`
- [PopBatteryWorker](../../page/AE/PopBatteryWorker_function_00AE1650.md) at `0x00AE17C2`
- [PopBatteryWorker](../../page/AE/PopBatteryWorker_function_00AE1650.md) at `0x00AE17F3`
- [PopBatteryWorker](../../page/AE/PopBatteryWorker_function_00AE1650.md) at `0x00AE195D`
- [sub_00AECA88](../../page/AE/Unknown_function_00AECA88.md) at `0x00AECAAD`
- [RtlDecompressFragmentLZNT1](../../page/AE/RtlDecompressFragmentLZNT1_function_00AECAF0.md) at `0x00AECD78`
- [sub_00B174A6](../../page/B1/Unknown_function_00B174A6.md) at `0x00B17647`
- [sub_00B1D2FE](../../page/B1/Unknown_function_00B1D2FE.md) at `0x00B1D354`
- [sub_00B1D2FE](../../page/B1/Unknown_function_00B1D2FE.md) at `0x00B1D395`
- [sub_00B20160](../../page/B2/Unknown_function_00B20160.md) at `0x00B20199`
- [sub_00B260E4](../../page/B2/Unknown_function_00B260E4.md) at `0x00B26176`
- [sub_00B284C0](../../page/B2/Unknown_function_00B284C0.md) at `0x00B285AE`
- [sub_00B284C0](../../page/B2/Unknown_function_00B284C0.md) at `0x00B285F2`
- [sub_00B2FD86](../../page/B2/Unknown_function_00B2FD86.md) at `0x00B2FDDD`
- [sub_00B2FF46](../../page/B2/Unknown_function_00B2FF46.md) at `0x00B2FFAD`
- [sub_00B30AB8](../../page/B3/Unknown_function_00B30AB8.md) at `0x00B30ADA`
- [sub_00B36710](../../page/B3/Unknown_function_00B36710.md) at `0x00B3676A`
- [sub_00B3C988](../../page/B3/Unknown_function_00B3C988.md) at `0x00B3CA23`
- [sub_00B3C988](../../page/B3/Unknown_function_00B3C988.md) at `0x00B3CB12`
- [sub_00B3C988](../../page/B3/Unknown_function_00B3C988.md) at `0x00B3CB6E`
- [sub_00B3F12C](../../page/B3/Unknown_function_00B3F12C.md) at `0x00B3F242`
- [sub_00B3F12C](../../page/B3/Unknown_function_00B3F12C.md) at `0x00B3F25E`
- [sub_00B3F12C](../../page/B3/Unknown_function_00B3F12C.md) at `0x00B3F27A`
- [sub_00B4018A](../../page/B4/Unknown_function_00B4018A.md) at `0x00B4020A`
- [sub_00B4018A](../../page/B4/Unknown_function_00B4018A.md) at `0x00B402C5`
- [sub_00B465F2](../../page/B4/Unknown_function_00B465F2.md) at `0x00B46612`
- [sub_00B47726](../../page/B4/Unknown_function_00B47726.md) at `0x00B4779B`
- [sub_00B49880](../../page/B4/Unknown_function_00B49880.md) at `0x00B498EE`
- [IoShutdownSystem](../../pagelk/B6/IoShutdownSystem_function_00B63B8C.md) at `0x00B63C88`
- [IoShutdownSystem](../../pagelk/B6/IoShutdownSystem_function_00B63B8C.md) at `0x00B63DB3`
- [IopShutdownBaseFileSystems](../../pagelk/B6/IopShutdownBaseFileSystems_function_00B63E10.md) at `0x00B63EF4`
- [PnprInitiateReplaceOperation](../../pagelk/B6/PnprInitiateReplaceOperation_function_00B64034.md) at `0x00B64346`
- [PnprQuiesceWorker](../../pagelk/B6/PnprQuiesceWorker_function_00B654E0.md) at `0x00B655B0`
- [PfpScenCtxPrefetchWait](../../pagelk/B6/PfpScenCtxPrefetchWait_function_00B6B5B0.md) at `0x00B6B6FC`
- [PopGracefulShutdown](../../pagelk/B6/PopGracefulShutdown_function_00B6BEC8.md) at `0x00B6BFD7`
- [NtSetSystemPowerState](../../pagelk/B7/NtSetSystemPowerState_function_00B70890.md) at `0x00B70A2B`
- [MiZeroAllPageFiles](../../pagelk/B7/MiZeroAllPageFiles_function_00B73B2C.md) at `0x00B73C3B`
- [MmDuplicateMemory](../../pagelk/B7/MmDuplicateMemory_function_00B74158.md) at `0x00B7423A`
- [PopEndMirroring](../../pagelk/B7/PopEndMirroring_function_00B75E50.md) at `0x00B75EDB`
- [PopTransitionToSleep](../../pagelk/B7/PopTransitionToSleep_function_00B76970.md) at `0x00B769DA`
- [PopTransitionToSleep](../../pagelk/B7/PopTransitionToSleep_function_00B76970.md) at `0x00B76A5A`
- [PopBuildDeviceNotifyList](../../pagelk/B7/PopBuildDeviceNotifyList_function_00B789E8.md) at `0x00B78AFF`
- [PopTransitionSystemPowerStateEx](../../pagelk/B7/PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7F6F0`
- [sub_00B80E6E](../../pagelk/B8/Unknown_function_00B80E6E.md) at `0x00B8102E`
- [IovpUnloadDriver](../../pagevrfy/B9/IovpUnloadDriver_function_00B92AE8.md) at `0x00B92BD5`
- [VfDriverLock](../../pagevrfy/B9/VfDriverLock_function_00B9A4A4.md) at `0x00B9A4BF`
- [VfIrpSendSynchronousIrp](../../pagevrfy/B9/VfIrpSendSynchronousIrp_function_00B9DEF0.md) at `0x00B9E024`
- [ViPendingCompleteAfterWait](../../pagevrfy/BA/ViPendingCompleteAfterWait_function_00BA1D18.md) at `0x00BA1D4D`
- [ViPendingWorkerThread](../../pagevrfy/BA/ViPendingWorkerThread_function_00BA20D0.md) at `0x00BA20EF`
- [ViPoolDelayFreeTrimThreadRoutine](../../pagevrfy/BA/ViPoolDelayFreeTrimThreadRoutine_function_00BAA500.md) at `0x00BAA524`
- [sub_00BAD17D](../../pagevrfy/BA/Unknown_function_00BAD17D.md) at `0x00BAD1D6`
- [AnFwFadeCompletion](../../pagebgfx/BC/AnFwFadeCompletion_function_00BC358C.md) at `0x00BC35E9`
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1DAF8`
- [IopCreateArcNamesCd](../../init/C2/IopCreateArcNamesCd_function_00C2C060.md) at `0x00C2C2B1`
- [IopCreateArcNamesCd](../../init/C2/IopCreateArcNamesCd_function_00C2C060.md) at `0x00C2C3FB`
- [IopStoreBootDriveLetter](../../init/C2/IopStoreBootDriveLetter_function_00C2D5CC.md) at `0x00C2D6C3`
- [IopGetBootDiskInformation](../../init/C2/IopGetBootDiskInformation_function_00C2DAAC.md) at `0x00C2DCC5`
- [IopGetBootDiskInformation](../../init/C2/IopGetBootDiskInformation_function_00C2DAAC.md) at `0x00C2DD66`
- [EtwpFixBootLoggers](../../init/C4/EtwpFixBootLoggers_function_00C4F09C.md) at `0x00C4F204`
- [MiHotAddBootDeferredDescriptorsDiscardable](../../init/C6/MiHotAddBootDeferredDescriptorsDiscardable_function_00C624E4.md) at `0x00C6250B`
- [SbpAddTransportToInstance](../../init/C6/SbpAddTransportToInstance_function_00C6F314.md) at `0x00C6F4B1`
- [SbpStartLanman](../../init/C6/SbpStartLanman_function_00C6F500.md) at `0x00C6F6F7`
- [SbpStartLanman](../../init/C6/SbpStartLanman_function_00C6F500.md) at `0x00C6F861`
- [SbpWaitForVmbus](../../init/C6/SbpWaitForVmbus_function_00C6F8D8.md) at `0x00C6F96C`

### Static image references
- `0x0020E71D` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0020E7EB` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0020EC18` → RVA `0x00F110C0` (`.data`; read)
- `0x0020ECCE` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0020F68B` → RVA `0x00F210E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0020F623` → [sub_006D672E](../6D/Unknown_function_006D672E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0020E6B0  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
0020E6B5  44 88 44 24 18                  mov byte ptr [rsp + 0x18], r8b
0020E6BA  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0020E6BE  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0020E6C3  55                              push rbp
0020E6C4  53                              push rbx
0020E6C5  56                              push rsi
0020E6C6  57                              push rdi
0020E6C7  41 54                           push r12
0020E6C9  41 55                           push r13
0020E6CB  41 56                           push r14
0020E6CD  41 57                           push r15
0020E6CF  48 8D 6C 24 E9                  lea rbp, [rsp - 0x17]
0020E6D4  48 81 EC A8 00 00 00            sub rsp, 0xa8
0020E6DB  45 33 C9                        xor r9d, r9d
0020E6DE  45 0F B6 F0                     movzx r14d, r8b
0020E6E2  4C 89 4D E7                     mov qword ptr [rbp - 0x19], r9
0020E6E6  41 8B D9                        mov ebx, r9d
0020E6E9  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
0020E6F2  4C 89 4D AF                     mov qword ptr [rbp - 0x51], r9
0020E6F6  44 88 4D 9F                     mov byte ptr [rbp - 0x61], r9b
0020E6FA  45 8D 79 02                     lea r15d, [r9 + 2]
0020E6FE  4C 89 4D B7                     mov qword ptr [rbp - 0x49], r9
0020E702  0F BA 77 74 02                  btr dword ptr [rdi + 0x74], 2
0020E707  89 5D A7                        mov dword ptr [rbp - 0x59], ebx
0020E70A  0F 92 C0                        setb al
0020E70D  84 C0                           test al, al
0020E70F  0F 85 48 06 00 00               jne 0x14020ed5d
0020E715  44 0F 20 C6                     mov rsi, cr8
0020E719  45 0F 22 C7                     mov cr8, r15
0020E71D  39 1D FD 85 DB 00               cmp dword ptr [rip + 0xdb85fd], ebx
0020E723  0F 85 2C 05 00 00               jne 0x14020ec55
0020E729  4C 8D AF 86 01 00 00            lea r13, [rdi + 0x186]
0020E730  41 88 75 00                     mov byte ptr [r13], sil
0020E734  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
0020E73D  80 7E 20 01                     cmp byte ptr [rsi + 0x20], 1
0020E741  77 2F                           ja 0x14020e772
0020E743  48 83 BE F8 38 00 00 00         cmp qword ptr [rsi + 0x38f8], 0
0020E74B  0F 85 43 0B 00 00               jne 0x14020f294
0020E751  80 BE E5 38 00 00 00            cmp byte ptr [rsi + 0x38e5], 0
0020E758  0F 85 6D 0D 00 00               jne 0x14020f4cb
0020E75E  48 8B 96 E8 38 00 00            mov rdx, qword ptr [rsi + 0x38e8]
0020E765  48 3B 96 F0 38 00 00            cmp rdx, qword ptr [rsi + 0x38f0]
0020E76C  0F 85 A3 04 00 00               jne 0x14020ec15
0020E772  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
0020E776  BB 01 00 00 00                  mov ebx, 1
0020E77B  48 BA 08 00 00 00 80 F7 FF FF   movabs rdx, 0xfffff78000000008
0020E785  49 BB B0 03 00 00 80 F7 FF FF   movabs r11, 0xfffff780000003b0
0020E78F  48 85 C9                        test rcx, rcx
0020E792  74 19                           je 0x14020e7ad
0020E794  83 79 04 00                     cmp dword ptr [rcx + 4], 0
0020E798  0F 8C C8 02 00 00               jl 0x14020ea66
0020E79E  48 8B 01                        mov rax, qword ptr [rcx]
0020E7A1  45 33 D2                        xor r10d, r10d
0020E7A4  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
0020E7A8  89 5D A3                        mov dword ptr [rbp - 0x5d], ebx
0020E7AB  EB 07                           jmp 0x14020e7b4
0020E7AD  45 33 D2                        xor r10d, r10d
0020E7B0  44 89 55 A3                     mov dword ptr [rbp - 0x5d], r10d
0020E7B4  45 0F B6 7D 00                  movzx r15d, byte ptr [r13]
0020E7B9  44 0F B6 65 77                  movzx r12d, byte ptr [rbp + 0x77]
0020E7BE  4C 89 55 D7                     mov qword ptr [rbp - 0x29], r10
0020E7C2  83 67 74 EF                     and dword ptr [rdi + 0x74], 0xffffffef
0020E7C6  C6 47 70 00                     mov byte ptr [rdi + 0x70], 0
0020E7CA  44 88 B7 87 01 00 00            mov byte ptr [rdi + 0x187], r14b
0020E7D1  45 84 E4                        test r12b, r12b
0020E7D4  74 04                           je 0x14020e7da
0020E7D6  83 4F 74 10                     or dword ptr [rdi + 0x74], 0x10
0020E7DA  41 8B F2                        mov esi, r10d
0020E7DD  0F 1F 00                        nop dword ptr [rax]
0020E7E0  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
0020E7E7  73 1B                           jae 0x14020e804
0020E7E9  FF C6                           inc esi
0020E7EB  85 35 BB 6A DB 00               test dword ptr [rip + 0xdb6abb], esi
0020E7F1  0F 84 D7 04 00 00               je 0x14020ecce
0020E7F7  F3 90                           pause
0020E7F9  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020E7FD  48 85 C0                        test rax, rax
0020E800  74 DE                           je 0x14020e7e0
0020E802  EB E5                           jmp 0x14020e7e9
0020E804  80 BF C1 00 00 00 00            cmp byte ptr [rdi + 0xc1], 0
0020E80B  0F 85 6B 05 00 00               jne 0x14020ed7c
0020E811  8B 5D A7                        mov ebx, dword ptr [rbp - 0x59]
0020E814  45 84 E4                        test r12b, r12b
0020E817  4C 8B 65 5F                     mov r12, qword ptr [rbp + 0x5f]
0020E81B  0F 85 08 02 00 00               jne 0x14020ea29
0020E821  F6 87 C2 00 00 00 02            test byte ptr [rdi + 0xc2], 2
0020E828  0F 85 A8 08 00 00               jne 0x14020f0d6
0020E82E  45 33 D2                        xor r10d, r10d
0020E831  EB 19                           jmp 0x14020e84c
0020E833  45 33 D2                        xor r10d, r10d
0020E836  44 38 57 72                     cmp byte ptr [rdi + 0x72], r10b
0020E83A  0F 85 A2 09 00 00               jne 0x14020f1e2
0020E840  45 8B F2                        mov r14d, r10d
0020E843  45 85 F6                        test r14d, r14d
0020E846  0F 85 99 08 00 00               jne 0x14020f0e5
0020E84C  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
0020E84F  4C 8D 8F 40 01 00 00            lea r9, [rdi + 0x140]
0020E856  C6 87 84 01 00 00 05            mov byte ptr [rdi + 0x184], 5
0020E85D  45 8B F2                        mov r14d, r10d
0020E860  88 87 83 02 00 00               mov byte ptr [rdi + 0x283], al
0020E866  41 8B F2                        mov esi, r10d
0020E869  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0020E873  8B 00                           mov eax, dword ptr [rax]
0020E875  89 87 B4 01 00 00               mov dword ptr [rdi + 0x1b4], eax
0020E87B  4C 89 57 40                     mov qword ptr [rdi + 0x40], r10
0020E87F  65 4C 8B 3C 25 20 00 00 00      mov r15, qword ptr gs:[0x20]
0020E888  41 C6 41 10 01                  mov byte ptr [r9 + 0x10], 1
0020E88D  41 C6 41 11 04                  mov byte ptr [r9 + 0x11], 4
0020E892  66 45 89 51 12                  mov word ptr [r9 + 0x12], r10w
0020E897  4D 89 61 20                     mov qword ptr [r9 + 0x20], r12
0020E89B  F0 41 0F BA 2C 24 07            lock bts dword ptr [r12], 7
0020E8A2  0F 82 C8 03 00 00               jb 0x14020ec70
0020E8A8  41 0F B6 04 24                  movzx eax, byte ptr [r12]
0020E8AD  41 8B 54 24 04                  mov edx, dword ptr [r12 + 4]
0020E8B2  0F B6 C8                        movzx ecx, al
0020E8B5  80 E1 7F                        and cl, 0x7f
0020E8B8  80 F9 02                        cmp cl, 2
0020E8BB  0F 84 D2 01 00 00               je 0x14020ea93
0020E8C1  85 D2                           test edx, edx
0020E8C3  0F 8F D7 03 00 00               jg 0x14020eca0
0020E8C9  4C 8B 45 AF                     mov r8, qword ptr [rbp - 0x51]
0020E8CD  44 8B 75 A3                     mov r14d, dword ptr [rbp - 0x5d]
0020E8D1  49 8B C0                        mov rax, r8
0020E8D4  41 83 FE 02                     cmp r14d, 2
0020E8D8  0F 84 D1 00 00 00               je 0x14020e9af
0020E8DE  45 85 F6                        test r14d, r14d
0020E8E1  0F 84 28 01 00 00               je 0x14020ea0f
0020E8E7  4D 85 C0                        test r8, r8
0020E8EA  0F 85 CC 03 00 00               jne 0x14020ecbc
0020E8F0  41 BE 02 01 00 00               mov r14d, 0x102
0020E8F6  41 B9 7F FF FF FF               mov r9d, 0xffffff7f
0020E8FC  F0 45 21 0C 24                  lock and dword ptr [r12], r9d
0020E901  C6 87 84 01 00 00 02            mov byte ptr [rdi + 0x184], 2
0020E908  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0020E90D  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020E911  48 85 C0                        test rax, rax
0020E914  74 1A                           je 0x14020e930
0020E916  41 8B F2                        mov esi, r10d
0020E919  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0020E920  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
0020E927  72 67                           jb 0x14020e990
0020E929  45 33 D2                        xor r10d, r10d
0020E92C  4C 89 57 40                     mov qword ptr [rdi + 0x40], r10
0020E930  4C 89 55 C7                     mov qword ptr [rbp - 0x39], r10
0020E934  83 FB 02                        cmp ebx, 2
0020E937  0F 83 C2 03 00 00               jae 0x14020ecff
0020E93D  0F B6 47 70                     movzx eax, byte ptr [rdi + 0x70]
0020E941  83 E3 01                        and ebx, 1
0020E944  A8 38                           test al, 0x38
0020E946  0F 85 7E 08 00 00               jne 0x14020f1ca
0020E94C  0F B6 BF 86 01 00 00            movzx edi, byte ptr [rdi + 0x186]
0020E953  85 DB                           test ebx, ebx
0020E955  0F 85 66 07 00 00               jne 0x14020f0c1
0020E95B  39 1D BF 83 DB 00               cmp dword ptr [rip + 0xdb83bf], ebx
0020E961  74 0D                           je 0x14020e970
0020E963  44 0F 20 C1                     mov rcx, cr8
0020E967  40 0F B6 D7                     movzx edx, dil
0020E96B  E8 28 6D 2E 00                  call 0x1404f5698
0020E970  44 0F 22 C7                     mov cr8, rdi
0020E974  41 8B C6                        mov eax, r14d
0020E977  48 81 C4 A8 00 00 00            add rsp, 0xa8
0020E97E  41 5F                           pop r15
0020E980  41 5E                           pop r14
0020E982  41 5D                           pop r13
0020E984  41 5C                           pop r12
0020E986  5F                              pop rdi
0020E987  5E                              pop rsi
0020E988  5B                              pop rbx
0020E989  5D                              pop rbp
0020E98A  C3                              ret
0020E98B  CC                              int3
0020E98C  0F 1F 40 00                     nop dword ptr [rax]
0020E990  FF C6                           inc esi
0020E992  85 35 14 69 DB 00               test dword ptr [rip + 0xdb6914], esi
0020E998  0F 84 68 04 00 00               je 0x14020ee06
0020E99E  F3 90                           pause
0020E9A0  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020E9A4  48 85 C0                        test rax, rax
0020E9A7  0F 84 73 FF FF FF               je 0x14020e920
0020E9AD  EB E1                           jmp 0x14020e990
0020E9AF  48 B8 B0 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003b0
0020E9B9  48 B9 08 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000008
0020E9C3  48 8B 00                        mov rax, qword ptr [rax]
0020E9C6  48 8B 09                        mov rcx, qword ptr [rcx]
0020E9C9  48 2B 8F F8 00 00 00            sub rcx, qword ptr [rdi + 0xf8]
0020E9D0  8B 97 B8 03 00 00               mov edx, dword ptr [rdi + 0x3b8]
0020E9D6  48 2B C8                        sub rcx, rax
0020E9D9  80 BF 87 01 00 00 00            cmp byte ptr [rdi + 0x187], 0
0020E9E0  49 8B C0                        mov rax, r8
0020E9E3  74 21                           je 0x14020ea06
0020E9E5  83 BF E4 01 00 00 00            cmp dword ptr [rdi + 0x1e4], 0
0020E9EC  75 18                           jne 0x14020ea06
0020E9EE  41 80 7D 00 00                  cmp byte ptr [r13], 0
0020E9F3  75 11                           jne 0x14020ea06
0020E9F5  80 BF C0 00 00 00 00            cmp byte ptr [rdi + 0xc0], 0
0020E9FC  75 08                           jne 0x14020ea06
0020E9FE  85 D2                           test edx, edx
0020EA00  74 04                           je 0x14020ea06
0020EA02  49 8D 04 10                     lea rax, [r8 + rdx]
0020EA06  48 3B C8                        cmp rcx, rax
0020EA09  0F 87 E1 FE FF FF               ja 0x14020e8f0
0020EA0F  49 8B 4C 24 10                  mov rcx, qword ptr [r12 + 0x10]
0020EA14  49 8D 44 24 08                  lea rax, [r12 + 8]
0020EA19  48 39 01                        cmp qword ptr [rcx], rax
0020EA1C  0F 84 45 04 00 00               je 0x14020ee67
0020EA22  B9 03 00 00 00                  mov ecx, 3
0020EA27  CD 29                           int 0x29
0020EA29  49 0F BE C6                     movsx rax, r14b
0020EA2D  80 7C 38 72 00                  cmp byte ptr [rax + rdi + 0x72], 0
0020EA32  0F 85 1C 04 00 00               jne 0x14020ee54
0020EA38  45 84 F6                        test r14b, r14b
0020EA3B  0F 84 F2 FD FF FF               je 0x14020e833
0020EA41  48 8D 87 A8 00 00 00            lea rax, [rdi + 0xa8]
0020EA48  48 39 00                        cmp qword ptr [rax], rax
0020EA4B  0F 84 E2 FD FF FF               je 0x14020e833
0020EA51  80 8F C2 00 00 00 02            or byte ptr [rdi + 0xc2], 2
0020EA58  41 BE C0 00 00 00               mov r14d, 0xc0
0020EA5E  45 33 D2                        xor r10d, r10d
0020EA61  E9 DD FD FF FF                  jmp 0x14020e843
0020EA66  49 8B 03                        mov rax, qword ptr [r11]
0020EA69  4C 8D AF 86 01 00 00            lea r13, [rdi + 0x186]
0020EA70  48 8B 12                        mov rdx, qword ptr [rdx]
0020EA73  48 2B D0                        sub rdx, rax
0020EA76  44 89 7D A3                     mov dword ptr [rbp - 0x5d], r15d
0020EA7A  48 8B 87 F8 00 00 00            mov rax, qword ptr [rdi + 0xf8]
0020EA81  48 03 01                        add rax, qword ptr [rcx]
0020EA84  48 2B D0                        sub rdx, rax
0020EA87  48 89 55 AF                     mov qword ptr [rbp - 0x51], rdx
0020EA8B  45 33 D2                        xor r10d, r10d
0020EA8E  E9 21 FD FF FF                  jmp 0x14020e7b4
0020EA93  41 0F B6 44 24 30               movzx eax, byte ptr [r12 + 0x30]
0020EA99  D0 E8                           shr al, 1
0020EA9B  24 01                           and al, 1
0020EA9D  88 45 9F                        mov byte ptr [rbp - 0x61], al
0020EAA0  85 D2                           test edx, edx
0020EAA2  0F 8E 3B 03 00 00               jle 0x14020ede3
0020EAA8  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
0020EAAD  3D 00 00 00 80                  cmp eax, 0x80000000
0020EAB2  0F 84 AA 07 00 00               je 0x14020f262
0020EAB8  83 E8 01                        sub eax, 1
0020EABB  41 89 44 24 04                  mov dword ptr [r12 + 4], eax
0020EAC0  0F 85 30 FE FF FF               jne 0x14020e8f6
0020EAC6  4C 89 97 C8 00 00 00            mov qword ptr [rdi + 0xc8], r10
0020EACD  41 8B F2                        mov esi, r10d
0020EAD0  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
0020EAD7  73 1B                           jae 0x14020eaf4
0020EAD9  FF C6                           inc esi
0020EADB  85 35 CB 67 DB 00               test dword ptr [rip + 0xdb67cb], esi
0020EAE1  0F 84 46 03 00 00               je 0x14020ee2d
0020EAE7  F3 90                           pause
0020EAE9  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020EAED  48 85 C0                        test rax, rax
0020EAF0  74 DE                           je 0x14020ead0
0020EAF2  EB E5                           jmp 0x14020ead9
0020EAF4  41 80 7C 24 31 00               cmp byte ptr [r12 + 0x31], 0
0020EAFA  74 07                           je 0x14020eb03
0020EAFC  66 FF 8F E4 01 00 00            dec word ptr [rdi + 0x1e4]
0020EB03  49 39 7F 08                     cmp qword ptr [r15 + 8], rdi
0020EB07  0F 85 15 06 00 00               jne 0x14020f122
0020EB0D  41 0F B6 8F BA 38 00 00         movzx ecx, byte ptr [r15 + 0x38ba]
0020EB15  33 C0                           xor eax, eax
0020EB17  0F 57 C0                        xorps xmm0, xmm0
0020EB1A  48 89 45 FF                     mov qword ptr [rbp - 1], rax
0020EB1E  41 8B 04 24                     mov eax, dword ptr [r12]
0020EB22  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
0020EB26  89 45 EF                        mov dword ptr [rbp - 0x11], eax
0020EB29  88 4D F1                        mov byte ptr [rbp - 0xf], cl
0020EB2C  8B 45 EF                        mov eax, dword ptr [rbp - 0x11]
0020EB2F  41 89 04 24                     mov dword ptr [r12], eax
0020EB33  41 0F B6 44 24 30               movzx eax, byte ptr [r12 + 0x30]
0020EB39  49 89 7C 24 28                  mov qword ptr [r12 + 0x28], rdi
0020EB3E  A8 01                           test al, 1
0020EB40  74 12                           je 0x14020eb54
0020EB42  24 FE                           and al, 0xfe
0020EB44  41 88 44 24 30                  mov byte ptr [r12 + 0x30], al
0020EB49  48 81 8F C8 00 00 00 80 00 00 00  or qword ptr [rdi + 0xc8], 0x80
0020EB54  45 33 D2                        xor r10d, r10d
0020EB57  48 8B CF                        mov rcx, rdi
0020EB5A  41 F6 44 24 30 02               test byte ptr [r12 + 0x30], 2
0020EB60  B8 D0 03 00 00                  mov eax, 0x3d0
0020EB65  0F 85 EB 06 00 00               jne 0x14020f256
0020EB6B  4C 89 97 D0 03 00 00            mov qword ptr [rdi + 0x3d0], r10
0020EB72  4C 8D 04 01                     lea r8, [rcx + rax]
0020EB76  48 8D 87 08 03 00 00            lea rax, [rdi + 0x308]
0020EB7D  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
0020EB81  49 8D 4C 24 18                  lea rcx, [r12 + 0x18]
0020EB86  48 39 02                        cmp qword ptr [rdx], rax
0020EB89  0F 85 93 FE FF FF               jne 0x14020ea22
0020EB8F  48 89 01                        mov qword ptr [rcx], rax
0020EB92  48 89 51 08                     mov qword ptr [rcx + 8], rdx
0020EB96  48 89 0A                        mov qword ptr [rdx], rcx
0020EB99  48 89 48 08                     mov qword ptr [rax + 8], rcx
0020EB9D  F0 41 81 24 24 7F FF FF FF      lock and dword ptr [r12], 0xffffff7f
0020EBA6  C6 87 84 01 00 00 02            mov byte ptr [rdi + 0x184], 2
0020EBAD  41 BC 01 00 00 00               mov r12d, 1
0020EBB3  4C 89 57 40                     mov qword ptr [rdi + 0x40], r10
0020EBB7  48 8B B7 C8 00 00 00            mov rsi, qword ptr [rdi + 0xc8]
0020EBBE  49 8B 08                        mov rcx, qword ptr [r8]
0020EBC1  48 85 C9                        test rcx, rcx
0020EBC4  0F 85 5F 05 00 00               jne 0x14020f129
0020EBCA  4C 89 55 BF                     mov qword ptr [rbp - 0x41], r10
0020EBCE  83 FB 02                        cmp ebx, 2
0020EBD1  0F 83 78 05 00 00               jae 0x14020f14f
0020EBD7  0F B6 47 70                     movzx eax, byte ptr [rdi + 0x70]
0020EBDB  83 E3 01                        and ebx, 1
0020EBDE  A8 38                           test al, 0x38
0020EBE0  0F 85 58 09 00 00               jne 0x14020f53e
0020EBE6  0F B6 BF 86 01 00 00            movzx edi, byte ptr [rdi + 0x186]
0020EBED  85 DB                           test ebx, ebx
0020EBEF  0F 85 BF 08 00 00               jne 0x14020f4b4
0020EBF5  39 1D 25 81 DB 00               cmp dword ptr [rip + 0xdb8125], ebx
0020EBFB  74 0D                           je 0x14020ec0a
0020EBFD  44 0F 20 C1                     mov rcx, cr8
0020EC01  40 0F B6 D7                     movzx edx, dil
0020EC05  E8 8E 6A 2E 00                  call 0x1404f5698
0020EC0A  44 0F 22 C7                     mov cr8, rdi
0020EC0E  8B C6                           mov eax, esi
0020EC10  E9 62 FD FF FF                  jmp 0x14020e977
0020EC15  8B 4E 24                        mov ecx, dword ptr [rsi + 0x24]
0020EC18  48 8D 05 A1 24 D0 00            lea rax, [rip + 0xd024a1]
0020EC1F  48 C1 E1 05                     shl rcx, 5
0020EC23  48 03 C8                        add rcx, rax
0020EC26  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0020EC2A  4C 8B 01                        mov r8, qword ptr [rcx]
0020EC2D  4C 85 40 38                     test qword ptr [rax + 0x38], r8
0020EC31  0F 85 3B FB FF FF               jne 0x14020e772
0020EC37  E8 50 BF FF FF                  call 0x14020ab8c
0020EC3C  85 C0                           test eax, eax
0020EC3E  0F 84 2E FB FF FF               je 0x14020e772
0020EC44  0F B6 8E E6 38 00 00            movzx ecx, byte ptr [rsi + 0x38e6]
0020EC4B  E8 E8 C0 FF FF                  call 0x14020ad38
0020EC50  E9 1D FB FF FF                  jmp 0x14020e772
0020EC55  41 0F B6 D7                     movzx edx, r15b
0020EC59  40 0F B6 CE                     movzx ecx, sil
0020EC5D  E8 9A 6A 2E 00                  call 0x1404f56fc
0020EC62  45 33 C9                        xor r9d, r9d
0020EC65  E9 BF FA FF FF                  jmp 0x14020e729
0020EC6A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
0020EC70  FF C6                           inc esi
0020EC72  85 35 34 66 DB 00               test dword ptr [rip + 0xdb6634], esi
0020EC78  0F 84 EF 02 00 00               je 0x14020ef6d
0020EC7E  F3 90                           pause
0020EC80  41 8B 04 24                     mov eax, dword ptr [r12]
0020EC84  84 C0                           test al, al
0020EC86  78 E8                           js 0x14020ec70
0020EC88  F0 41 0F BA 2C 24 07            lock bts dword ptr [r12], 7
0020EC8F  72 DF                           jb 0x14020ec70
0020EC91  4C 8D 8F 40 01 00 00            lea r9, [rdi + 0x140]
0020EC98  45 33 D2                        xor r10d, r10d
0020EC9B  E9 08 FC FF FF                  jmp 0x14020e8a8
0020ECA0  24 07                           and al, 7
0020ECA2  3C 01                           cmp al, 1
0020ECA4  74 4F                           je 0x14020ecf5
0020ECA6  80 F9 05                        cmp cl, 5
0020ECA9  0F 85 47 FC FF FF               jne 0x14020e8f6
0020ECAF  8D 42 FF                        lea eax, [rdx - 1]
0020ECB2  41 89 44 24 04                  mov dword ptr [r12 + 4], eax
0020ECB7  E9 3A FC FF FF                  jmp 0x14020e8f6
0020ECBC  48 B9 14 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000014
0020ECC6  48 8B 09                        mov rcx, qword ptr [rcx]
0020ECC9  E9 38 FD FF FF                  jmp 0x14020ea06
0020ECCE  8B 05 E4 7D DB 00               mov eax, dword ptr [rip + 0xdb7de4]
0020ECD4  A8 40                           test al, 0x40
0020ECD6  0F 84 1B FB FF FF               je 0x14020e7f7
0020ECDC  E8 AF 07 10 00                  call 0x14030f490
0020ECE1  84 C0                           test al, al
0020ECE3  0F 84 0E FB FF FF               je 0x14020e7f7
0020ECE9  8B CE                           mov ecx, esi
0020ECEB  E8 70 07 10 00                  call 0x14030f460
0020ECF0  E9 04 FB FF FF                  jmp 0x14020e7f9
0020ECF5  45 89 54 24 04                  mov dword ptr [r12 + 4], r10d
0020ECFA  E9 F7 FB FF FF                  jmp 0x14020e8f6
0020ECFF  41 8B F2                        mov esi, r10d
0020ED02  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
0020ED09  73 1B                           jae 0x14020ed26
0020ED0B  FF C6                           inc esi
0020ED0D  85 35 99 65 DB 00               test dword ptr [rip + 0xdb6599], esi
0020ED13  0F 84 81 03 00 00               je 0x14020f09a
0020ED19  F3 90                           pause
0020ED1B  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020ED1F  48 85 C0                        test rax, rax
0020ED22  74 DE                           je 0x14020ed02
0020ED24  EB E5                           jmp 0x14020ed0b
0020ED26  48 0F BE 97 1B 03 00 00         movsx rdx, byte ptr [rdi + 0x31b]
0020ED2E  4C 8B C2                        mov r8, rdx
0020ED31  48 8D 0C 3A                     lea rcx, [rdx + rdi]
0020ED35  0F B6 81 38 03 00 00            movzx eax, byte ptr [rcx + 0x338]
0020ED3C  84 C0                           test al, al
0020ED3E  0F 85 5D 02 00 00               jne 0x14020efa1
0020ED44  33 C0                           xor eax, eax
0020ED46  48 8B D7                        mov rdx, rdi
0020ED49  B9 57 01 00 00                  mov ecx, 0x157
0020ED4E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0020ED53  44 8D 48 02                     lea r9d, [rax + 2]
0020ED57  E8 04 E9 2E 00                  call 0x1404fd660
0020ED5C  CC                              int3
0020ED5D  0F BA 77 74 10                  btr dword ptr [rdi + 0x74], 0x10
0020ED62  4C 8D AF 86 01 00 00            lea r13, [rdi + 0x186]
0020ED69  0F 92 C3                        setb bl
0020ED6C  83 E3 01                        and ebx, 1
0020ED6F  03 DB                           add ebx, ebx
0020ED71  83 CB 01                        or ebx, 1
0020ED74  89 5D A7                        mov dword ptr [rbp - 0x59], ebx
0020ED77  E9 B8 F9 FF FF                  jmp 0x14020e734
0020ED7C  66 83 BF E6 01 00 00 00         cmp word ptr [rdi + 0x1e6], 0
0020ED84  0F 85 87 FA FF FF               jne 0x14020e811
0020ED8A  41 80 FF 01                     cmp r15b, 1
0020ED8E  0F 83 7D FA FF FF               jae 0x14020e811
0020ED94  33 C9                           xor ecx, ecx
0020ED96  48 89 4F 40                     mov qword ptr [rdi + 0x40], rcx
0020ED9A  39 0D 80 7F DB 00               cmp dword ptr [rip + 0xdb7f80], ecx
0020EDA0  74 0B                           je 0x14020edad
0020EDA2  44 0F 20 C1                     mov rcx, cr8
0020EDA6  B2 01                           mov dl, 1
0020EDA8  E8 EB 68 2E 00                  call 0x1404f5698
0020EDAD  44 0F 22 C3                     mov cr8, rbx
0020EDB1  45 33 C0                        xor r8d, r8d
0020EDB4  33 D2                           xor edx, edx
0020EDB6  33 C9                           xor ecx, ecx
0020EDB8  E8 63 21 04 00                  call 0x140250f20
0020EDBD  44 0F 20 C1                     mov rcx, cr8
0020EDC1  B8 02 00 00 00                  mov eax, 2
0020EDC6  44 0F 22 C0                     mov cr8, rax
0020EDCA  83 3D 4F 7F DB 00 00            cmp dword ptr [rip + 0xdb7f4f], 0
0020EDD1  0F 85 89 01 00 00               jne 0x14020ef60
0020EDD7  45 88 7D 00                     mov byte ptr [r13], r15b
0020EDDB  45 33 D2                        xor r10d, r10d
0020EDDE  E9 DF F9 FF FF                  jmp 0x14020e7c2
0020EDE3  49 3B 7C 24 28                  cmp rdi, qword ptr [r12 + 0x28]
0020EDE8  0F 85 DB FA FF FF               jne 0x14020e8c9
0020EDEE  41 0F B6 87 BA 38 00 00         movzx eax, byte ptr [r15 + 0x38ba]
0020EDF6  41 38 44 24 02                  cmp byte ptr [r12 + 2], al
0020EDFB  0F 84 A7 FC FF FF               je 0x14020eaa8
0020EE01  E9 C3 FA FF FF                  jmp 0x14020e8c9
0020EE06  8B 05 AC 7C DB 00               mov eax, dword ptr [rip + 0xdb7cac]
0020EE0C  A8 40                           test al, 0x40
0020EE0E  0F 84 8A FB FF FF               je 0x14020e99e
0020EE14  E8 77 06 10 00                  call 0x14030f490
0020EE19  84 C0                           test al, al
0020EE1B  0F 84 7D FB FF FF               je 0x14020e99e
0020EE21  8B CE                           mov ecx, esi
0020EE23  E8 38 06 10 00                  call 0x14030f460
0020EE28  E9 73 FB FF FF                  jmp 0x14020e9a0
0020EE2D  8B 05 85 7C DB 00               mov eax, dword ptr [rip + 0xdb7c85]
0020EE33  A8 40                           test al, 0x40
0020EE35  0F 84 AC FC FF FF               je 0x14020eae7
0020EE3B  E8 50 06 10 00                  call 0x14030f490
0020EE40  84 C0                           test al, al
0020EE42  0F 84 9F FC FF FF               je 0x14020eae7
0020EE48  8B CE                           mov ecx, esi
0020EE4A  E8 11 06 10 00                  call 0x14030f460
0020EE4F  E9 95 FC FF FF                  jmp 0x14020eae9
0020EE54  C6 44 38 72 00                  mov byte ptr [rax + rdi + 0x72], 0
0020EE59  41 BE 01 01 00 00               mov r14d, 0x101
0020EE5F  45 33 D2                        xor r10d, r10d
0020EE62  E9 DC F9 FF FF                  jmp 0x14020e843
0020EE67  49 89 01                        mov qword ptr [r9], rax
0020EE6A  49 89 49 08                     mov qword ptr [r9 + 8], rcx
0020EE6E  4C 89 09                        mov qword ptr [rcx], r9
0020EE71  4C 89 48 08                     mov qword ptr [rax + 8], r9
0020EE75  F0 41 81 24 24 7F FF FF FF      lock and dword ptr [r12], 0xffffff7f
0020EE7E  80 7D 9F 00                     cmp byte ptr [rbp - 0x61], 0
0020EE82  C6 87 4B 02 00 00 01            mov byte ptr [rdi + 0x24b], 1
0020EE89  0F 84 C8 00 00 00               je 0x14020ef57
0020EE8F  45 33 C0                        xor r8d, r8d
0020EE92  33 D2                           xor edx, edx
0020EE94  49 8B CC                        mov rcx, r12
0020EE97  E8 94 13 00 00                  call 0x140210230
0020EE9C  4C 8B 45 AF                     mov r8, qword ptr [rbp - 0x51]
0020EEA0  48 8B F0                        mov rsi, rax
0020EEA3  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
0020EEA7  48 85 F6                        test rsi, rsi
0020EEAA  74 28                           je 0x14020eed4
0020EEAC  0F B6 0E                        movzx ecx, byte ptr [rsi]
0020EEAF  80 C9 02                        or cl, 2
0020EEB2  88 0E                           mov byte ptr [rsi], cl
0020EEB4  90                              nop
0020EEB5  48 8B 0E                        mov rcx, qword ptr [rsi]
0020EEB8  48 C1 E9 3F                     shr rcx, 0x3f
0020EEBC  84 C9                           test cl, cl
0020EEBE  0F 85 D0 00 00 00               jne 0x14020ef94
0020EEC4  4C 8B 45 AF                     mov r8, qword ptr [rbp - 0x51]
0020EEC8  C6 46 09 01                     mov byte ptr [rsi + 9], 1
0020EECC  90                              nop
0020EECD  0F B6 06                        movzx eax, byte ptr [rsi]
0020EED0  24 FD                           and al, 0xfd
0020EED2  88 06                           mov byte ptr [rsi], al
0020EED4  48 8D 45 E7                     lea rax, [rbp - 0x19]
0020EED8  4D 8B C8                        mov r9, r8
0020EEDB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0020EEE0  48 8D 97 40 01 00 00            lea rdx, [rdi + 0x140]
0020EEE7  45 8B C6                        mov r8d, r14d
0020EEEA  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0020EEEE  48 8B CF                        mov rcx, rdi
0020EEF1  E8 EA F0 FF FF                  call 0x14020dfe0
0020EEF6  45 33 D2                        xor r10d, r10d
0020EEF9  4C 8B F0                        mov r14, rax
0020EEFC  44 89 55 A7                     mov dword ptr [rbp - 0x59], r10d
0020EF00  48 85 F6                        test rsi, rsi
0020EF03  0F 85 E8 02 00 00               jne 0x14020f1f1
0020EF09  4C 89 97 D0 03 00 00            mov qword ptr [rdi + 0x3d0], r10
0020EF10  41 81 FE 00 01 00 00            cmp r14d, 0x100
0020EF17  0F 85 57 FA FF FF               jne 0x14020e974
0020EF1D  44 0F 20 C6                     mov rsi, cr8
0020EF21  B8 02 00 00 00                  mov eax, 2
0020EF26  44 0F 22 C0                     mov cr8, rax
0020EF2A  83 3D EF 7D DB 00 00            cmp dword ptr [rip + 0xdb7def], 0
0020EF31  75 13                           jne 0x14020ef46
0020EF33  44 0F B6 75 6F                  movzx r14d, byte ptr [rbp + 0x6f]
0020EF38  BB 01 00 00 00                  mov ebx, 1
0020EF3D  41 88 75 00                     mov byte ptr [r13], sil
0020EF41  E9 6E F8 FF FF                  jmp 0x14020e7b4
0020EF46  0F B6 D0                        movzx edx, al
0020EF49  40 0F B6 CE                     movzx ecx, sil
0020EF4D  E8 AA 67 2E 00                  call 0x1404f56fc
0020EF52  45 33 D2                        xor r10d, r10d
0020EF55  EB DC                           jmp 0x14020ef33
0020EF57  48 8B 75 B7                     mov rsi, qword ptr [rbp - 0x49]
0020EF5B  E9 47 FF FF FF                  jmp 0x14020eea7
0020EF60  0F B6 D0                        movzx edx, al
0020EF63  E8 94 67 2E 00                  call 0x1404f56fc
0020EF68  E9 6A FE FF FF                  jmp 0x14020edd7
0020EF6D  8B 05 45 7B DB 00               mov eax, dword ptr [rip + 0xdb7b45]
0020EF73  A8 40                           test al, 0x40
0020EF75  0F 84 03 FD FF FF               je 0x14020ec7e
0020EF7B  E8 10 05 10 00                  call 0x14030f490
0020EF80  84 C0                           test al, al
0020EF82  0F 84 F6 FC FF FF               je 0x14020ec7e
0020EF88  8B CE                           mov ecx, esi
0020EF8A  E8 D1 04 10 00                  call 0x14030f460
0020EF8F  E9 EC FC FF FF                  jmp 0x14020ec80
0020EF94  48 8B CE                        mov rcx, rsi
0020EF97  E8 74 34 05 00                  call 0x140262410
0020EF9C  E9 23 FF FF FF                  jmp 0x14020eec4
0020EFA1  2C 01                           sub al, 1
0020EFA3  88 81 38 03 00 00               mov byte ptr [rcx + 0x338], al
0020EFA9  0F 85 BB 00 00 00               jne 0x14020f06a
0020EFAF  8B 87 58 03 00 00               mov eax, dword ptr [rdi + 0x358]
0020EFB5  8B CA                           mov ecx, edx
0020EFB7  0F BB D0                        btc eax, edx
0020EFBA  41 BC 01 00 00 00               mov r12d, 1
0020EFC0  41 D3 E4                        shl r12d, cl
0020EFC3  89 87 58 03 00 00               mov dword ptr [rdi + 0x358], eax
0020EFC9  41 3B C4                        cmp eax, r12d
0020EFCC  0F 83 98 00 00 00               jae 0x14020f06a
0020EFD2  80 BF C3 00 00 00 1F            cmp byte ptr [rdi + 0xc3], 0x1f
0020EFD9  0F 8F 8B 00 00 00               jg 0x14020f06a
0020EFDF  E8 DC 07 2E 00                  call 0x1404ef7c0
0020EFE4  85 C0                           test eax, eax
0020EFE6  0F 84 90 00 00 00               je 0x14020f07c
0020EFEC  44 0F BE 87 33 02 00 00         movsx r8d, byte ptr [rdi + 0x233]
0020EFF4  45 8B D0                        mov r10d, r8d
0020EFF7  45 8B C8                        mov r9d, r8d
0020EFFA  41 83 F8 10                     cmp r8d, 0x10
0020EFFE  7D 48                           jge 0x14020f048
0020F000  0F B6 8F 66 03 00 00            movzx ecx, byte ptr [rdi + 0x366]
0020F007  0F B7 97 06 02 00 00            movzx edx, word ptr [rdi + 0x206]
0020F00E  8B C2                           mov eax, edx
0020F010  83 E0 0F                        and eax, 0xf
0020F013  41 03 C0                        add eax, r8d
0020F016  41 3B C1                        cmp eax, r9d
0020F019  44 8B C0                        mov r8d, eax
0020F01C  45 0F 4E C1                     cmovle r8d, r9d
0020F020  45 33 C9                        xor r9d, r9d
0020F023  84 C9                           test cl, cl
0020F025  41 8B C1                        mov eax, r9d
0020F028  0F 4F C1                        cmovg eax, ecx
0020F02B  0F BE C0                        movsx eax, al
0020F02E  44 03 C0                        add r8d, eax
0020F031  41 83 F8 10                     cmp r8d, 0x10
0020F035  0F 8D 6E 06 00 00               jge 0x14020f6a9
0020F03B  C1 EA 04                        shr edx, 4
0020F03E  0F B6 C2                        movzx eax, dl
0020F041  41 3B C0                        cmp eax, r8d
0020F044  44 0F 4F C0                     cmovg r8d, eax
0020F048  8B 87 58 03 00 00               mov eax, dword ptr [rdi + 0x358]
0020F04E  85 C0                           test eax, eax
0020F050  75 39                           jne 0x14020f08b
0020F052  0F BE 87 C3 00 00 00            movsx eax, byte ptr [rdi + 0xc3]
0020F059  44 3B C0                        cmp r8d, eax
0020F05C  7D 0C                           jge 0x14020f06a
0020F05E  48 8D 55 C7                     lea rdx, [rbp - 0x39]
0020F062  48 8B CF                        mov rcx, rdi
0020F065  E8 0E 1E 01 00                  call 0x140220e78
0020F06A  33 C0                           xor eax, eax
0020F06C  C6 87 1B 03 00 00 20            mov byte ptr [rdi + 0x31b], 0x20
0020F073  48 89 47 40                     mov qword ptr [rdi + 0x40], rax
0020F077  E9 C1 F8 FF FF                  jmp 0x14020e93d
0020F07C  33 D2                           xor edx, edx
0020F07E  48 8B CF                        mov rcx, rdi
0020F081  E8 96 B7 3B 00                  call 0x1405ca81c
0020F086  44 8B C0                        mov r8d, eax
0020F089  EB C7                           jmp 0x14020f052
0020F08B  0F BD C0                        bsr eax, eax
0020F08E  44 3B C0                        cmp r8d, eax
0020F091  89 45 D3                        mov dword ptr [rbp - 0x2d], eax
0020F094  44 0F 4C C0                     cmovl r8d, eax
0020F098  EB B8                           jmp 0x14020f052
0020F09A  8B 05 18 7A DB 00               mov eax, dword ptr [rip + 0xdb7a18]
0020F0A0  A8 40                           test al, 0x40
0020F0A2  0F 84 71 FC FF FF               je 0x14020ed19
0020F0A8  E8 E3 03 10 00                  call 0x14030f490
0020F0AD  84 C0                           test al, al
0020F0AF  0F 84 64 FC FF FF               je 0x14020ed19
0020F0B5  8B CE                           mov ecx, esi
0020F0B7  E8 A4 03 10 00                  call 0x14030f460
0020F0BC  E9 5A FC FF FF                  jmp 0x14020ed1b
0020F0C1  44 0F B6 C7                     movzx r8d, dil
0020F0C5  48 8D 55 C7                     lea rdx, [rbp - 0x39]
0020F0C9  49 8B CF                        mov rcx, r15
0020F0CC  E8 2F 17 04 00                  call 0x140250800
0020F0D1  E9 9E F8 FF FF                  jmp 0x14020e974
0020F0D6  45 84 F6                        test r14b, r14b
0020F0D9  0F 84 4F F7 FF FF               je 0x14020e82e
0020F0DF  41 BE C0 00 00 00               mov r14d, 0xc0
0020F0E5  4C 8D 4D D7                     lea r9, [rbp - 0x29]
0020F0E9  41 B0 01                        mov r8b, 1
0020F0EC  8B D3                           mov edx, ebx
0020F0EE  48 8B CF                        mov rcx, rdi
0020F0F1  E8 8A 13 01 00                  call 0x140220480
0020F0F6  33 C9                           xor ecx, ecx
0020F0F8  48 89 4F 40                     mov qword ptr [rdi + 0x40], rcx
0020F0FC  85 C0                           test eax, eax
0020F0FE  0F 85 AB 00 00 00               jne 0x14020f1af
0020F104  39 0D 16 7C DB 00               cmp dword ptr [rip + 0xdb7c16], ecx
0020F10A  74 0D                           je 0x14020f119
0020F10C  44 0F 20 C1                     mov rcx, cr8
0020F110  41 0F B6 D7                     movzx edx, r15b
0020F114  E8 7F 65 2E 00                  call 0x1404f5698
0020F119  45 0F 22 C7                     mov cr8, r15
0020F11D  E9 52 F8 FF FF                  jmp 0x14020e974
0020F122  32 C9                           xor cl, cl
0020F124  E9 EC F9 FF FF                  jmp 0x14020eb15
0020F129  45 8B C4                        mov r8d, r12d
0020F12C  4C 89 97 D0 03 00 00            mov qword ptr [rdi + 0x3d0], r10
0020F133  33 D2                           xor edx, edx
0020F135  E8 F6 10 00 00                  call 0x140210230
0020F13A  45 33 D2                        xor r10d, r10d
0020F13D  48 85 C0                        test rax, rax
0020F140  0F 84 84 FA FF FF               je 0x14020ebca
0020F146  44 88 60 0A                     mov byte ptr [rax + 0xa], r12b
0020F14A  E9 7B FA FF FF                  jmp 0x14020ebca
0020F14F  45 8B F2                        mov r14d, r10d
0020F152  F0 48 0F BA 6F 40 00            lock bts qword ptr [rdi + 0x40], 0
0020F159  73 1D                           jae 0x14020f178
0020F15B  41 FF C6                        inc r14d
0020F15E  44 85 35 47 61 DB 00            test dword ptr [rip + 0xdb6147], r14d
0020F165  0F 84 21 03 00 00               je 0x14020f48c
0020F16B  F3 90                           pause
0020F16D  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
0020F171  48 85 C0                        test rax, rax
0020F174  74 DC                           je 0x14020f152
0020F176  EB E3                           jmp 0x14020f15b
0020F178  48 0F BE 8F 1B 03 00 00         movsx rcx, byte ptr [rdi + 0x31b]
0020F180  4C 8B C1                        mov r8, rcx
0020F183  48 8D 14 39                     lea rdx, [rcx + rdi]
0020F187  0F B6 82 38 03 00 00            movzx eax, byte ptr [rdx + 0x338]
0020F18E  84 C0                           test al, al
0020F190  0F 85 05 02 00 00               jne 0x14020f39b
0020F196  33 C9                           xor ecx, ecx
0020F198  48 8B D7                        mov rdx, rdi
0020F19B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0020F1A0  44 8D 49 02                     lea r9d, [rcx + 2]
0020F1A4  B9 57 01 00 00                  mov ecx, 0x157
0020F1A9  E8 B2 E4 2E 00                  call 0x1404fd660
0020F1AE  CC                              int3
0020F1AF  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020F1B8  48 8D 55 D7                     lea rdx, [rbp - 0x29]
0020F1BC  45 0F B6 C7                     movzx r8d, r15b
0020F1C0  E8 3B 16 04 00                  call 0x140250800
0020F1C5  E9 AA F7 FF FF                  jmp 0x14020e974
0020F1CA  49 8B CF                        mov rcx, r15
0020F1CD  A8 18                           test al, 0x18
0020F1CF  74 4E                           je 0x14020f21f
0020F1D1  4C 8D 45 C7                     lea r8, [rbp - 0x39]
0020F1D5  48 8B D7                        mov rdx, rdi
0020F1D8  E8 EB 3C 14 00                  call 0x140352ec8
0020F1DD  E9 92 F7 FF FF                  jmp 0x14020e974
0020F1E2  C6 47 72 00                     mov byte ptr [rdi + 0x72], 0
0020F1E6  41 BE 01 01 00 00               mov r14d, 0x101
0020F1EC  E9 52 F6 FF FF                  jmp 0x14020e843
0020F1F1  45 33 C0                        xor r8d, r8d
0020F1F4  48 8B D6                        mov rdx, rsi
0020F1F7  49 8B CC                        mov rcx, r12
0020F1FA  E8 31 10 00 00                  call 0x140210230
0020F1FF  41 F7 C6 7F FF FF FF            test r14d, 0xffffff7f
0020F206  74 7C                           je 0x14020f284
0020F208  48 8B D0                        mov rdx, rax
0020F20B  49 8B CC                        mov rcx, r12
0020F20E  E8 FD 2F 05 00                  call 0x140262210
0020F213  45 33 D2                        xor r10d, r10d
0020F216  4C 89 55 B7                     mov qword ptr [rbp - 0x49], r10
0020F21A  E9 EA FC FF FF                  jmp 0x14020ef09
0020F21F  41 B0 01                        mov r8b, 1
0020F222  48 8D 55 C7                     lea rdx, [rbp - 0x39]
0020F226  E8 D5 15 04 00                  call 0x140250800
0020F22B  45 33 C0                        xor r8d, r8d
0020F22E  33 D2                           xor edx, edx
0020F230  33 C9                           xor ecx, ecx
0020F232  E8 E9 1C 04 00                  call 0x140250f20
0020F237  83 3D E2 7A DB 00 00            cmp dword ptr [rip + 0xdb7ae2], 0
0020F23E  74 0B                           je 0x14020f24b
0020F240  44 0F 20 C1                     mov rcx, cr8
0020F244  33 D2                           xor edx, edx
0020F246  E8 4D 64 2E 00                  call 0x1404f5698
0020F24B  33 C0                           xor eax, eax
0020F24D  44 0F 22 C0                     mov cr8, rax
0020F251  E9 1E F7 FF FF                  jmp 0x14020e974
0020F256  4C 89 A7 D0 03 00 00            mov qword ptr [rdi + 0x3d0], r12
0020F25D  E9 10 F9 FF FF                  jmp 0x14020eb72
0020F262  F0 41 81 24 24 7F FF FF FF      lock and dword ptr [r12], 0xffffff7f
0020F26B  44 8B C3                        mov r8d, ebx
0020F26E  48 8B D7                        mov rdx, rdi
0020F271  49 8B CF                        mov rcx, r15
0020F274  E8 37 19 01 00                  call 0x140220bb0
0020F279  B9 91 01 00 C0                  mov ecx, 0xc0000191
0020F27E  E8 CD 77 0E 00                  call 0x1402f6a50
0020F283  CC                              int3
0020F284  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
0020F288  45 33 D2                        xor r10d, r10d
0020F28B  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
0020F28F  E9 75 FC FF FF                  jmp 0x14020ef09
0020F294  E8 47 89 00 00                  call 0x140217be0
0020F299  4C 8B B6 F8 38 00 00            mov r14, qword ptr [rsi + 0x38f8]
0020F2A0  44 0F B6 C0                     movzx r8d, al
0020F2A4  4D 85 F6                        test r14, r14
0020F2A7  0F 84 4D 03 00 00               je 0x14020f5fa
0020F2AD  49 83 7E F8 00                  cmp qword ptr [r14 - 8], 0
0020F2B2  49 8B 06                        mov rax, qword ptr [r14]
0020F2B5  0F 85 6D 03 00 00               jne 0x14020f628
0020F2BB  49 3B C6                        cmp rax, r14
0020F2BE  0F 85 8B 00 00 00               jne 0x14020f34f
0020F2C4  4C 89 8E F8 38 00 00            mov qword ptr [rsi + 0x38f8], r9
0020F2CB  49 8B 46 30                     mov rax, qword ptr [r14 + 0x30]
0020F2CF  4D 89 0E                        mov qword ptr [r14], r9
0020F2D2  48 8B 40 38                     mov rax, qword ptr [rax + 0x38]
0020F2D6  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
0020F2DA  45 84 C0                        test r8b, r8b
0020F2DD  0F 85 99 00 00 00               jne 0x14020f37c
0020F2E3  4D 8B 46 10                     mov r8, qword ptr [r14 + 0x10]
0020F2E7  4D 3B 46 18                     cmp r8, qword ptr [r14 + 0x18]
0020F2EB  74 58                           je 0x14020f345
0020F2ED  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
0020F2F1  49 8B 56 20                     mov rdx, qword ptr [r14 + 0x20]
0020F2F5  48 8B 08                        mov rcx, qword ptr [rax]
0020F2F8  48 85 4A 28                     test qword ptr [rdx + 0x28], rcx
0020F2FC  0F 84 4E 03 00 00               je 0x14020f650
0020F302  E8 D9 88 00 00                  call 0x140217be0
0020F307  49 83 3E 00                     cmp qword ptr [r14], 0
0020F30B  44 0F B6 C0                     movzx r8d, al
0020F30F  75 2B                           jne 0x14020f33c
0020F311  48 8B 86 F8 38 00 00            mov rax, qword ptr [rsi + 0x38f8]
0020F318  48 85 C0                        test rax, rax
0020F31B  0F 84 1C 03 00 00               je 0x14020f63d
0020F321  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0020F325  48 39 01                        cmp qword ptr [rcx], rax
0020F328  0F 85 F4 F6 FF FF               jne 0x14020ea22
0020F32E  49 89 06                        mov qword ptr [r14], rax
0020F331  49 89 4E 08                     mov qword ptr [r14 + 8], rcx
0020F335  4C 89 31                        mov qword ptr [rcx], r14
0020F338  4C 89 70 08                     mov qword ptr [rax + 8], r14
0020F33C  45 84 C0                        test r8b, r8b
0020F33F  0F 85 13 02 00 00               jne 0x14020f558
0020F345  44 0F B6 75 6F                  movzx r14d, byte ptr [rbp + 0x6f]
0020F34A  E9 02 F4 FF FF                  jmp 0x14020e751
0020F34F  48 89 86 F8 38 00 00            mov qword ptr [rsi + 0x38f8], rax
0020F356  49 8B 0E                        mov rcx, qword ptr [r14]
0020F359  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0020F35D  4C 39 71 08                     cmp qword ptr [rcx + 8], r14
0020F361  0F 85 BB F6 FF FF               jne 0x14020ea22
0020F367  4C 39 30                        cmp qword ptr [rax], r14
0020F36A  0F 85 B2 F6 FF FF               jne 0x14020ea22
0020F370  48 89 08                        mov qword ptr [rax], rcx
0020F373  48 89 41 08                     mov qword ptr [rcx + 8], rax
0020F377  E9 4F FF FF FF                  jmp 0x14020f2cb
0020F37C  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020F385  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0020F38C  4D 85 C0                        test r8, r8
0020F38F  0F 85 81 01 00 00               jne 0x14020f516
0020F395  FB                              sti
0020F396  E9 48 FF FF FF                  jmp 0x14020f2e3
0020F39B  2C 01                           sub al, 1
0020F39D  88 82 38 03 00 00               mov byte ptr [rdx + 0x338], al
0020F3A3  0F 85 B3 00 00 00               jne 0x14020f45c
0020F3A9  8B 87 58 03 00 00               mov eax, dword ptr [rdi + 0x358]
0020F3AF  0F BB C8                        btc eax, ecx
0020F3B2  41 D3 E4                        shl r12d, cl
0020F3B5  89 87 58 03 00 00               mov dword ptr [rdi + 0x358], eax
0020F3BB  41 3B C4                        cmp eax, r12d
0020F3BE  0F 83 98 00 00 00               jae 0x14020f45c
0020F3C4  80 BF C3 00 00 00 1F            cmp byte ptr [rdi + 0xc3], 0x1f
0020F3CB  0F 8F 8B 00 00 00               jg 0x14020f45c
0020F3D1  E8 EA 03 2E 00                  call 0x1404ef7c0
0020F3D6  85 C0                           test eax, eax
0020F3D8  0F 84 90 00 00 00               je 0x14020f46e
0020F3DE  44 0F BE 87 33 02 00 00         movsx r8d, byte ptr [rdi + 0x233]
0020F3E6  45 8B D0                        mov r10d, r8d
0020F3E9  45 8B C8                        mov r9d, r8d
0020F3EC  41 83 F8 10                     cmp r8d, 0x10
0020F3F0  7D 48                           jge 0x14020f43a
0020F3F2  0F B6 8F 66 03 00 00            movzx ecx, byte ptr [rdi + 0x366]
0020F3F9  0F B7 97 06 02 00 00            movzx edx, word ptr [rdi + 0x206]
0020F400  8B C2                           mov eax, edx
0020F402  83 E0 0F                        and eax, 0xf
0020F405  41 03 C0                        add eax, r8d
0020F408  41 3B C1                        cmp eax, r9d
0020F40B  44 8B C0                        mov r8d, eax
0020F40E  45 0F 4E C1                     cmovle r8d, r9d
0020F412  45 33 C9                        xor r9d, r9d
0020F415  84 C9                           test cl, cl
0020F417  41 8B C1                        mov eax, r9d
0020F41A  0F 4F C1                        cmovg eax, ecx
0020F41D  0F BE C0                        movsx eax, al
0020F420  44 03 C0                        add r8d, eax
0020F423  41 83 F8 10                     cmp r8d, 0x10
0020F427  0F 8D 71 02 00 00               jge 0x14020f69e
0020F42D  C1 EA 04                        shr edx, 4
0020F430  0F B6 C2                        movzx eax, dl
0020F433  41 3B C0                        cmp eax, r8d
0020F436  44 0F 4F C0                     cmovg r8d, eax
0020F43A  8B 87 58 03 00 00               mov eax, dword ptr [rdi + 0x358]
0020F440  85 C0                           test eax, eax
0020F442  75 39                           jne 0x14020f47d
0020F444  0F BE 87 C3 00 00 00            movsx eax, byte ptr [rdi + 0xc3]
0020F44B  44 3B C0                        cmp r8d, eax
0020F44E  7D 0C                           jge 0x14020f45c
0020F450  48 8D 55 BF                     lea rdx, [rbp - 0x41]
0020F454  48 8B CF                        mov rcx, rdi
0020F457  E8 1C 1A 01 00                  call 0x140220e78
0020F45C  33 C9                           xor ecx, ecx
0020F45E  C6 87 1B 03 00 00 20            mov byte ptr [rdi + 0x31b], 0x20
0020F465  48 89 4F 40                     mov qword ptr [rdi + 0x40], rcx
0020F469  E9 69 F7 FF FF                  jmp 0x14020ebd7
0020F46E  33 D2                           xor edx, edx
0020F470  48 8B CF                        mov rcx, rdi
0020F473  E8 A4 B3 3B 00                  call 0x1405ca81c
0020F478  44 8B C0                        mov r8d, eax
0020F47B  EB C7                           jmp 0x14020f444
0020F47D  0F BD C0                        bsr eax, eax
0020F480  44 3B C0                        cmp r8d, eax
0020F483  89 45 CF                        mov dword ptr [rbp - 0x31], eax
0020F486  44 0F 4C C0                     cmovl r8d, eax
0020F48A  EB B8                           jmp 0x14020f444
0020F48C  8B 05 26 76 DB 00               mov eax, dword ptr [rip + 0xdb7626]
0020F492  A8 40                           test al, 0x40
0020F494  0F 84 D1 FC FF FF               je 0x14020f16b
0020F49A  E8 F1 FF 0F 00                  call 0x14030f490
0020F49F  84 C0                           test al, al
0020F4A1  0F 84 C4 FC FF FF               je 0x14020f16b
0020F4A7  41 8B CE                        mov ecx, r14d
0020F4AA  E8 B1 FF 0F 00                  call 0x14030f460
0020F4AF  E9 B9 FC FF FF                  jmp 0x14020f16d
0020F4B4  44 0F B6 C7                     movzx r8d, dil
0020F4B8  48 8D 55 BF                     lea rdx, [rbp - 0x41]
0020F4BC  49 8B CF                        mov rcx, r15
0020F4BF  E8 3C 13 04 00                  call 0x140250800
0020F4C4  8B C6                           mov eax, esi
0020F4C6  E9 AC F4 FF FF                  jmp 0x14020e977
0020F4CB  83 BE E0 38 00 00 00            cmp dword ptr [rsi + 0x38e0], 0
0020F4D2  0F 85 86 F2 FF FF               jne 0x14020e75e
0020F4D8  E8 03 87 00 00                  call 0x140217be0
0020F4DD  80 BE E5 38 00 00 00            cmp byte ptr [rsi + 0x38e5], 0
0020F4E4  44 0F B6 C0                     movzx r8d, al
0020F4E8  0F 85 84 01 00 00               jne 0x14020f672
0020F4EE  45 84 C0                        test r8b, r8b
0020F4F1  0F 84 67 F2 FF FF               je 0x14020e75e
0020F4F7  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020F500  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0020F507  4D 85 C0                        test r8, r8
0020F50A  0F 85 C2 00 00 00               jne 0x14020f5d2
0020F510  FB                              sti
0020F511  E9 48 F2 FF FF                  jmp 0x14020e75e
0020F516  41 0F 0D 08                     prefetchw byte ptr [r8]
0020F51A  41 8B 00                        mov eax, dword ptr [r8]
0020F51D  8B D0                           mov edx, eax
0020F51F  0F BA F2 15                     btr edx, 0x15
0020F523  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0020F528  75 F3                           jne 0x14020f51d
0020F52A  0F BA E0 15                     bt eax, 0x15
0020F52E  0F 83 61 FE FF FF               jae 0x14020f395
0020F534  E8 97 3C 05 00                  call 0x1402631d0
0020F539  E9 57 FE FF FF                  jmp 0x14020f395
0020F53E  49 8B CF                        mov rcx, r15
0020F541  A8 18                           test al, 0x18
0020F543  74 54                           je 0x14020f599
0020F545  4C 8D 45 BF                     lea r8, [rbp - 0x41]
0020F549  48 8B D7                        mov rdx, rdi
0020F54C  E8 77 39 14 00                  call 0x140352ec8
0020F551  8B C6                           mov eax, esi
0020F553  E9 1F F4 FF FF                  jmp 0x14020e977
0020F558  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020F561  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0020F568  4D 85 C0                        test r8, r8
0020F56B  75 0B                           jne 0x14020f578
0020F56D  FB                              sti
0020F56E  44 0F B6 75 6F                  movzx r14d, byte ptr [rbp + 0x6f]
0020F573  E9 D9 F1 FF FF                  jmp 0x14020e751
0020F578  41 0F 0D 08                     prefetchw byte ptr [r8]
0020F57C  41 8B 00                        mov eax, dword ptr [r8]
0020F57F  8B D0                           mov edx, eax
0020F581  0F BA F2 15                     btr edx, 0x15
0020F585  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0020F58A  75 F3                           jne 0x14020f57f
0020F58C  0F BA E0 15                     bt eax, 0x15
0020F590  73 DB                           jae 0x14020f56d
0020F592  E8 39 3C 05 00                  call 0x1402631d0
0020F597  EB D4                           jmp 0x14020f56d
0020F599  41 B0 01                        mov r8b, 1
0020F59C  48 8D 55 BF                     lea rdx, [rbp - 0x41]
0020F5A0  E8 5B 12 04 00                  call 0x140250800
0020F5A5  45 33 C0                        xor r8d, r8d
0020F5A8  33 D2                           xor edx, edx
0020F5AA  33 C9                           xor ecx, ecx
0020F5AC  E8 6F 19 04 00                  call 0x140250f20
0020F5B1  83 3D 68 77 DB 00 00            cmp dword ptr [rip + 0xdb7768], 0
0020F5B8  74 0B                           je 0x14020f5c5
0020F5BA  44 0F 20 C1                     mov rcx, cr8
0020F5BE  33 D2                           xor edx, edx
0020F5C0  E8 D3 60 2E 00                  call 0x1404f5698
0020F5C5  33 C0                           xor eax, eax
0020F5C7  44 0F 22 C0                     mov cr8, rax
0020F5CB  8B C6                           mov eax, esi
0020F5CD  E9 A5 F3 FF FF                  jmp 0x14020e977
0020F5D2  41 0F 0D 08                     prefetchw byte ptr [r8]
0020F5D6  41 8B 00                        mov eax, dword ptr [r8]
0020F5D9  8B D0                           mov edx, eax
0020F5DB  0F BA F2 15                     btr edx, 0x15
0020F5DF  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0020F5E4  75 F3                           jne 0x14020f5d9
0020F5E6  0F BA E0 15                     bt eax, 0x15
0020F5EA  0F 83 20 FF FF FF               jae 0x14020f510
0020F5F0  E8 DB 3B 05 00                  call 0x1402631d0
0020F5F5  E9 16 FF FF FF                  jmp 0x14020f510
0020F5FA  45 84 C0                        test r8b, r8b
0020F5FD  0F 84 42 FD FF FF               je 0x14020f345
0020F603  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0020F60C  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0020F613  4D 85 C0                        test r8, r8
0020F616  0F 84 51 FF FF FF               je 0x14020f56d
0020F61C  41 0F 0D 08                     prefetchw byte ptr [r8]
0020F620  41 8B 00                        mov eax, dword ptr [r8]
0020F623  E9 06 71 4C 00                  jmp 0x1406d672e
0020F628  4C 3B F0                        cmp r14, rax
0020F62B  0F 84 A9 FC FF FF               je 0x14020f2da
0020F631  48 89 86 F8 38 00 00            mov qword ptr [rsi + 0x38f8], rax
0020F638  E9 9D FC FF FF                  jmp 0x14020f2da
0020F63D  4D 89 76 08                     mov qword ptr [r14 + 8], r14
0020F641  4D 89 36                        mov qword ptr [r14], r14
0020F644  4C 89 B6 F8 38 00 00            mov qword ptr [rsi + 0x38f8], r14
0020F64B  E9 EC FC FF FF                  jmp 0x14020f33c
0020F650  49 8B D0                        mov rdx, r8
0020F653  49 8D 4E F8                     lea rcx, [r14 - 8]
0020F657  E8 AC 35 3B 00                  call 0x1405c2c08
0020F65C  85 C0                           test eax, eax
0020F65E  0F 84 E1 FC FF FF               je 0x14020f345
0020F664  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
0020F668  E8 47 2C 3B 00                  call 0x1405c22b4
0020F66D  E9 D3 FC FF FF                  jmp 0x14020f345
0020F672  83 BE E0 38 00 00 00            cmp dword ptr [rsi + 0x38e0], 0
0020F679  0F 85 6F FE FF FF               jne 0x14020f4ee
0020F67F  C6 86 E5 38 00 00 00            mov byte ptr [rsi + 0x38e5], 0
0020F686  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0020F68B  48 8B 05 56 1A D1 00            mov rax, qword ptr [rip + 0xd11a56]
0020F692  48 89 86 E8 38 00 00            mov qword ptr [rsi + 0x38e8], rax
0020F699  E9 50 FE FF FF                  jmp 0x14020f4ee
0020F69E  41 B8 0F 00 00 00               mov r8d, 0xf
0020F6A4  E9 84 FD FF FF                  jmp 0x14020f42d
0020F6A9  41 B8 0F 00 00 00               mov r8d, 0xf
0020F6AF  E9 87 F9 FF FF                  jmp 0x14020f03b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeWaitForSingleObject(__int64 a1, int a2, unsigned __int8 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m57;
    unsigned __int64 v_stack_m58;
    unsigned __int8 v_stack_m66;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned __int8 v_stack_mB8;
    unsigned int v_stack_mE8;
    unsigned int v_stack_p0;
    unsigned int v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = (unsigned __int8)(a4);
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (168);
    a4 = 0;
    v_stack_m70 = 0;
    v_stack_mA8 = 0;
    v_stack_mB8 = 0;
    v_stack_mA0 = 0;
    v_stack_mB0 = 0;
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_0020ED5D;
    if ((*(unsigned int *)(v_rip + 14386685)) != 0) goto loc_0020EC55;
loc_0020E729:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) = (unsigned __int8)(v_cr8);
loc_0020E734:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32)) > 1) goto loc_0020E772;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14584)) != 0) goto loc_0020F294;
loc_0020E751:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14565)) != 0) goto loc_0020F4CB;
loc_0020E75E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14568)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14576))) goto loc_0020EC15;
loc_0020E772:
    if (a5 == 0) goto loc_0020E7AD;
    if ((*(unsigned int *)(a5 + 4)) < 0) goto loc_0020EA66;
    v_r10 = 0;
    v_stack_mA8 = *(unsigned __int64 *)(a5);
    v_stack_mB4 = 1;
    goto loc_0020E7B4;
loc_0020E7AD:
    v_r10 = 0;
    v_stack_mB4 = 0;
loc_0020E7B4:
    v_stack_m80 = 0;
loc_0020E7C2:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 112) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 391) = a3;
    if ((unsigned __int8)(v_stack_p20) != 0) {
    }
loc_0020E7E0:
    if (condition_is_above_or_equal) goto loc_0020E804;
loc_0020E7E9:
    v_rsi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14379707)) & ((unsigned int)(v_rsi))) == 0) goto loc_0020ECCE;
loc_0020E7F7:
loc_0020E7F9:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) == 0) goto loc_0020E7E0;
    goto loc_0020E7E9;
loc_0020E804:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 193)) != 0) goto loc_0020ED7C;
loc_0020E811:
    if ((unsigned __int8)(v_stack_p20) != 0) goto loc_0020EA29;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 194)) & (2)) != 0) goto loc_0020F0D6;
loc_0020E82E:
    v_r10 = 0;
    goto loc_0020E84C;
loc_0020E833:
    v_r10 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 114)) != 0) goto loc_0020F1E2;
loc_0020E843:
    if (0 != 0) goto loc_0020F0E5;
loc_0020E84C:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 388) = 5;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 643) = (unsigned __int8)((unsigned int)(v_stack_p10));
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 436) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p10))));
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 320 + 16) = 1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 320 + 17) = 4;
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 320 + 18) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 320 + 32) = v_stack_p8;
    if (condition_is_below) goto loc_0020EC70;
loc_0020E8A8:
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8))) & (127));
    if (((unsigned __int8)(a1)) == 2) goto loc_0020EA93;
    if (condition_is_greater) goto loc_0020ECA0;
loc_0020E8C9:
    if (((unsigned int)((unsigned int)(v_stack_mB4))) == 2) goto loc_0020E9AF;
    if ((unsigned int)((unsigned int)(v_stack_mB4)) == 0) goto loc_0020EA0F;
    if (v_stack_mA8 != 0) goto loc_0020ECBC;
loc_0020E8F0:
loc_0020E8F6:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 388) = 2;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) == 0) goto loc_0020E930;
loc_0020E920:
    if (condition_is_below) goto loc_0020E990;
    v_r10 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 64) = 0;
loc_0020E930:
    v_stack_m90 = 0;
    if (((unsigned int)((unsigned int)(v_stack_mB0))) >= 2) goto loc_0020ECFF;
loc_0020E93D:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_mB0)) & (1));
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 112))) & (56)) != 0) goto loc_0020F1CA;
    if ((unsigned int)(v_rbx) != 0) goto loc_0020F0C1;
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 112);
    if ((*(unsigned int *)(v_rip + 14386111)) != ((unsigned int)(v_rbx))) {
        a1 = a4 + 2;
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_mA8, (unsigned int)(0xFFFFFF7FULL));
    }
loc_0020E974:
loc_0020E977:
    v_rsp = (v_rsp) + (168);
    return 258;
loc_0020E990:
    v_rsi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14379284)) & ((unsigned int)(v_rsi))) == 0) goto loc_0020EE06;
loc_0020E99E:
loc_0020E9A0:
    if (*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 64) == 0) goto loc_0020E920;
    goto loc_0020E990;
loc_0020E9AF:
    a1 = (*(unsigned __int64 *)(a1)) - (*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 248));
    a1 = (a1) - (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 64)));
    if ((*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 391)) == 0) goto loc_0020EA06;
    if ((*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 484)) != 0) goto loc_0020EA06;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390)) != 0) goto loc_0020EA06;
    if ((*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 192)) != 0) goto loc_0020EA06;
    result = v_stack_mA8;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 952))) != 0) {
        result = v_stack_mA8 + (unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 952)) * 1;
    }
    if (a1 > result) goto loc_0020E8F0;
loc_0020EA0F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 16))) == (v_stack_p8 + 8)) goto loc_0020EE67;
loc_0020EA22:
loc_0020EA29:
    if ((*(unsigned __int8 *)((__int8)(258) + *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) * 1 + 114)) != 0) goto loc_0020EE54;
    if (258 == 0) goto loc_0020E833;
    if ((*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 168)) == (*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 168)) goto loc_0020E833;
    v_r10 = 0;
    goto loc_0020E843;
loc_0020EA66:
    a2 = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 952)))) - (*(unsigned __int64 *)(v_r11));
    v_stack_mB4 = (unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32)));
    result = (*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 248)) + (*(unsigned __int64 *)(3));
    a2 = (a2) - (result);
    v_stack_mA8 = a2;
    v_r10 = 0;
    goto loc_0020E7B4;
loc_0020EA93:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p8 + 48)) >> (1));
    result = (unsigned __int8)((result) & (1));
    v_stack_mB8 = (unsigned __int8)(result);
    if (condition_is_less_or_equal) goto loc_0020EDE3;
loc_0020EAA8:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 4)))) == 0x80000000ULL) goto loc_0020F262;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 4))) - (1));
    *(unsigned int *)(v_stack_p8 + 4) = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_0020E8F6;
    *(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 200) = 0;
loc_0020EAD0:
    if (condition_is_above_or_equal) goto loc_0020EAF4;
loc_0020EAD9:
    v_rsi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14378955)) & ((unsigned int)(v_rsi))) == 0) goto loc_0020EE2D;
loc_0020EAE7:
loc_0020EAE9:
    if (*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 64) == 0) goto loc_0020EAD0;
    goto loc_0020EAD9;
loc_0020EAF4:
    if ((*(unsigned __int8 *)(v_stack_p8 + 49)) != 0) {
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 8)) != (*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390))) goto loc_0020F122;
loc_0020EB15:
    result = 0;
    v_stack_m58 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m68 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8)));
    v_stack_m66 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14522));
    *(unsigned int *)(v_stack_p8) = (unsigned int)((unsigned int)(v_stack_m68));
    *(unsigned __int64 *)(v_stack_p8 + 40) = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390);
    result = *(unsigned __int8 *)(v_stack_p8 + 48);
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 48))) & (1)) != 0) {
        result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p8 + 48)) & (254));
        *(unsigned __int8 *)(v_stack_p8 + 48) = (unsigned __int8)(result);
    }
    v_r10 = 0;
    if (((*(unsigned __int8 *)(v_stack_p8 + 48)) & (2)) != 0) goto loc_0020F256;
    *(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 976) = 0;
loc_0020EB72:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 776 + 8))) != (*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 776)) goto loc_0020EA22;
    *(unsigned __int64 *)(v_stack_p8 + 24) = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 776;
    *(unsigned __int64 *)(v_stack_p8 + 24 + 8) = *(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 776 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 776 + 8)) = v_stack_p8 + 24;
    *(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 776 + 8) = v_stack_p8 + 24;
    *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 388) = 2;
    *(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 64) = 0;
    if (*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 976 * 1) != 0) goto loc_0020F129;
loc_0020EBCA:
    v_stack_m98 = 0;
    if (((unsigned int)(v_rbx)) >= 2) goto loc_0020F14F;
loc_0020EBD7:
    v_rbx = (unsigned int)((v_rbx) & (1));
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 112))) & (56)) != 0) goto loc_0020F53E;
    if ((unsigned int)(v_rbx) != 0) goto loc_0020F4B4;
    result = *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 112);
    if ((*(unsigned int *)(v_rip + 14385445)) != ((unsigned int)(v_rbx))) {
        a1 = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390);
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 976 * 1, (unsigned int)(0xFFFFFF7FULL));
    }
    goto loc_0020E977;
loc_0020EC15:
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 200) + 36))) << (5);
    a1 = (a1) + (v_rip + 13640865);
    if (((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 56)) & (*(unsigned __int64 *)(a1))) != 0) goto loc_0020E772;
    result = KiRcuReportQuiescentState(a1, a2, *(unsigned __int64 *)(a1), (unsigned int)(0xFFFFFF7FULL));
    if ((unsigned int)(result) == 0) goto loc_0020E772;
    result = KiRcuFlushCompleted(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 200) + 14566), a2, *(unsigned __int64 *)(a1), (unsigned int)(0xFFFFFF7FULL));
    goto loc_0020E772;
loc_0020EC55:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 200)), (unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32))), *(unsigned __int64 *)(a1), (unsigned int)(0xFFFFFF7FULL));
    a4 = 0;
    goto loc_0020E729;
loc_0020EC70:
    v_rsi = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 200)) + 1);
    if (((*(unsigned int *)(v_rip + 14378548)) & ((unsigned int)(v_rsi))) == 0) goto loc_0020EF6D;
loc_0020EC7E:
loc_0020EC80:
    if (sign_flag) goto loc_0020EC70;
    if (condition_is_below) goto loc_0020EC70;
    v_r10 = 0;
    goto loc_0020E8A8;
loc_0020ECA0:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(1))) & (7));
    if (((unsigned __int8)(result)) == 1) goto loc_0020ECF5;
    if (((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 200)))) != 5) goto loc_0020E8F6;
    *(unsigned int *)(1 + 4) = (unsigned int)((unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32))) - 1);
    goto loc_0020E8F6;
loc_0020ECBC:
    goto loc_0020EA06;
loc_0020ECCE:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14384612)))) & (64)) == 0) goto loc_0020E7F7;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 200))), (unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32))), *(unsigned __int64 *)(a1), *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 320);
    if ((unsigned __int8)(result) == 0) goto loc_0020E7F7;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), (unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32))), *(unsigned __int64 *)(a1), *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 320);
    goto loc_0020E7F9;
loc_0020ECF5:
    *(unsigned int *)(1 + 4) = 0;
    goto loc_0020E8F6;
loc_0020ECFF:
loc_0020ED02:
    if (condition_is_above_or_equal) goto loc_0020ED26;
loc_0020ED0B:
    v_rsi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14378393)) & ((unsigned int)(v_rsi))) == 0) goto loc_0020F09A;
loc_0020ED19:
loc_0020ED1B:
    if (*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 64) == 0) goto loc_0020ED02;
    goto loc_0020ED0B;
loc_0020ED26:
    if ((unsigned __int8)(*(unsigned __int8 *)((__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 795)) + *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) * 1 + 824)) != 0) goto loc_0020EFA1;
    result = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(343, *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390), (__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 795)), result + 2);
loc_0020ED5D:
    v_rbx = (condition_is_below) ? 1 : 0;
    v_rbx = (unsigned int)((v_rbx) & (1));
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(v_rbx)));
    v_rbx = (unsigned int)((v_rbx) | (1));
    v_stack_mB0 = (unsigned int)(v_rbx);
    goto loc_0020E734;
loc_0020ED7C:
    if ((*(unsigned __int16 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 486)) != 0) goto loc_0020E811;
    if (((unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32)))) >= 1) goto loc_0020E811;
    a1 = 0;
    *(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 64) = 0;
    if ((*(unsigned int *)(v_rip + 14385024)) != 0) {
        a1 = *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390);
        a2 = 1;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 795)), result + 2);
    }
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = KiDeliverApc(a1, a2, a3, result + 2);
    if ((*(unsigned int *)(v_rip + 14384975)) != 0) goto loc_0020EF60;
loc_0020EDD7:
    *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 390) = (unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32)));
    v_r10 = 0;
    goto loc_0020E7C2;
loc_0020EDE3:
    if ((*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390)) != (*(unsigned __int64 *)(1 + 40))) goto loc_0020E8C9;
    if ((*(unsigned __int8 *)(1 + 2)) == ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 14522)))) goto loc_0020EAA8;
    goto loc_0020E8C9;
loc_0020EE06:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14384300)))) & (64)) == 0) goto loc_0020E99E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rbx, a2, a3, result + 2);
    if ((unsigned __int8)(result) == 0) goto loc_0020E99E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), a2, a3, result + 2);
    goto loc_0020E9A0;
loc_0020EE2D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14384261)))) & (64)) == 0) goto loc_0020EAE7;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rsi)), a2, a3, result + 2);
    if ((unsigned __int8)(result) == 0) goto loc_0020EAE7;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), a2, a3, result + 2);
    goto loc_0020EAE9;
loc_0020EE54:
    *(unsigned __int8 *)(result + *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) * 1 + 114) = 0;
    v_r10 = 0;
    goto loc_0020E843;
loc_0020EE67:
    *(unsigned __int64 *)(result + 2) = result;
    *(unsigned __int64 *)(result + 2 + 8) = (unsigned int)((unsigned int)(v_rsi));
    *(unsigned __int64 *)((unsigned int)((unsigned int)(v_rsi))) = result + 2;
    *(unsigned __int64 *)(result + 8) = result + 2;
    *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 587) = 1;
    if (v_stack_mB8 == 0) goto loc_0020EF57;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(1, a2, a3, result + 2);
    v_stack_mA0 = result;
loc_0020EEA7:
    if (result == 0) goto loc_0020EED4;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(result)) | (2));
    *(unsigned __int8 *)(result) = (unsigned __int8)(a1);
    a1 = (*(unsigned __int64 *)(result)) >> (63);
    if ((unsigned __int8)(a1) != 0) goto loc_0020EF94;
loc_0020EEC4:
    *(unsigned __int8 *)(result + 9) = 1;
    result = (unsigned __int8)((*(unsigned __int8 *)(result)) & (253));
    *(unsigned __int8 *)(result) = (unsigned __int8)(result);
loc_0020EED4:
    v_stack_p28 = v_stack_m70;
    v_stack_p20 = (unsigned int)(v_rbx);
    result = KiCommitThreadWait(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390), *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 320, 257, v_stack_mA8);
    v_r10 = 0;
    v_stack_mB0 = 0;
    if (result != 0) goto loc_0020F1F1;
loc_0020EF09:
    *(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 976) = 0;
    if (((unsigned int)(result)) != 256) goto loc_0020E974;
    if ((*(unsigned int *)(v_rip + 14384623)) != 0) goto loc_0020EF46;
loc_0020EF33:
    *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 390) = 2;
    goto loc_0020E7B4;
loc_0020EF46:
    result = KiRaiseIrqlProcessIrqlFlags(2, 2, 257, v_stack_mA8);
    v_r10 = 0;
    goto loc_0020EF33;
loc_0020EF57:
    goto loc_0020EEA7;
loc_0020EF60:
    result = KiRaiseIrqlProcessIrqlFlags(2, (unsigned __int8)(result), 257, v_stack_mA8);
    goto loc_0020EDD7;
loc_0020EF6D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14383941)))) & (64)) == 0) goto loc_0020EC7E;
    result = KiCheckVpBackingLongSpinWaitHypercall(2, (unsigned __int8)(result), 257, v_stack_mA8);
    if ((unsigned __int8)(result) == 0) goto loc_0020EC7E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_mA0)), (unsigned __int8)(result), 257, v_stack_mA8);
    goto loc_0020EC80;
loc_0020EF94:
    result = KiAbEntryRemoveFromTree(v_stack_mA0, (unsigned __int8)(result), 257, v_stack_mA8);
    goto loc_0020EEC4;
loc_0020EFA1:
    result = (unsigned __int8)((result) - (1));
    *(unsigned __int8 *)(v_stack_mA0 + 824) = (unsigned __int8)(result);
    if (condition_is_not_equal) goto loc_0020F06A;
    v_r12 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned __int8)(result))))));
    *(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 856) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 856)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 856)))) >= ((unsigned int)(v_r12))) goto loc_0020F06A;
    if ((*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 195)) > 31) goto loc_0020F06A;
    result = Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline((unsigned int)((unsigned int)((unsigned __int8)(result))), (unsigned __int8)(result), 257, v_stack_mA8);
    if ((unsigned int)(result) == 0) goto loc_0020F07C;
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 563)))) >= 16) goto loc_0020F048;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 518)))) & (15));
    result = (unsigned int)((result) + ((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 563)))));
    a3 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) <= ((unsigned int)((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 563))))))) { a3 = (unsigned int)((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 563))))); }
    a4 = 0;
    result = 0;
    if (condition_is_greater) { result = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 870)); }
    a3 = (unsigned int)((a3) + ((unsigned int)((__int8)((unsigned __int8)(result)))));
    if (a3 >= 16) goto loc_0020F6A9;
loc_0020F03B:
    a2 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 518)) >> (4));
    if (((unsigned int)((unsigned __int8)(a2))) > a3) { a3 = (unsigned int)((unsigned __int8)(a2)); }
loc_0020F048:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 856))) != 0) goto loc_0020F08B;
loc_0020F052:
    result = (__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 195));
    if (a3 < ((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 195))))) {
        a2 = v_stack_m90;
        a1 = *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390);
        result = KiSetPriorityThread(a1, a2, a3, a4);
    }
    result = 0;
    *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 795) = 32;
    *(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 64) = 0;
    goto loc_0020E93D;
loc_0020F07C:
    a2 = 0;
    result = KiComputeThreadPriorityNonStacking(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390), a2, a3, a4);
    goto loc_0020F052;
loc_0020F08B:
    v_stack_m84 = (unsigned int)(result);
    a3 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) < ((unsigned int)(result))) { a3 = (unsigned int)(result); }
    goto loc_0020F052;
loc_0020F09A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14383640)))) & (64)) == 0) goto loc_0020ED19;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0020ED19;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_mA0)), a2, a3, a4);
    goto loc_0020ED1B;
loc_0020F0C1:
    result = KiProcessDeferredReadyList(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m90, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390)), a4);
    goto loc_0020E974;
loc_0020F0D6:
    if ((unsigned __int8)(v_stack_p18) == 0) goto loc_0020E82E;
loc_0020F0E5:
    result = KiPerformWaitDeferredWork(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390), 1, 1, v_stack_m80);
    a1 = 0;
    *(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 64) = 0;
    if ((unsigned int)(result) != 0) goto loc_0020F1AF;
    if ((*(unsigned int *)(v_rip + 14384150)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32)));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 1, v_stack_m80);
    }
    goto loc_0020E974;
loc_0020F122:
    a1 = 0;
    goto loc_0020EB15;
loc_0020F129:
    *(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 976) = (unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 563))));
    a2 = 0;
    result = KeAbPreAcquire(a1, a2, (unsigned int)((unsigned int)(v_r12)), v_stack_m80);
    v_r10 = 0;
    if (result == 0) goto loc_0020EBCA;
    *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_r12);
    goto loc_0020EBCA;
loc_0020F14F:
loc_0020F152:
    if (condition_is_above_or_equal) goto loc_0020F178;
loc_0020F15B:
    v_r14 = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14377287)) & ((unsigned int)(v_r14))) == 0) goto loc_0020F48C;
loc_0020F16B:
loc_0020F16D:
    if (*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 64) == 0) goto loc_0020F152;
    goto loc_0020F15B;
loc_0020F178:
    if ((unsigned __int8)(*(unsigned __int8 *)((__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 795)) + *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) * 1 + 824)) != 0) goto loc_0020F39B;
    a1 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(343, *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390), (__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 795)), a1 + 2);
loc_0020F1AF:
    result = KiProcessDeferredReadyList(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m80, (unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32))), a1 + 2);
    goto loc_0020E974;
loc_0020F1CA:
    if ((((unsigned __int8)(result)) & (24)) == 0) goto loc_0020F21F;
    result = KiExitThreadWaitReschedule(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390), v_stack_m90, a1 + 2);
    goto loc_0020E974;
loc_0020F1E2:
    *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 114) = 0;
    goto loc_0020E843;
loc_0020F1F1:
    a3 = 0;
    result = KeAbPreAcquire(v_r12, v_stack_mA0, a3, a1 + 2);
    if (((257) & (0xFFFFFF7FULL)) == 0) goto loc_0020F284;
    result = KeAbPostReleaseEx(v_r12, result, a3, a1 + 2);
    v_r10 = 0;
    v_stack_mA0 = 0;
    goto loc_0020EF09;
loc_0020F21F:
    result = KiProcessDeferredReadyList(v_r12, v_stack_m90, 1, a1 + 2);
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = KiDeliverApc(a1, a2, a3, a1 + 2);
    if ((*(unsigned int *)(v_rip + 14383842)) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 32));
        a2 = 0;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a1 + 2);
    }
    result = 0;
    goto loc_0020E974;
loc_0020F256:
    *(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 976) = v_r12;
    goto loc_0020EB72;
loc_0020F262:
    result = KiFastExitThreadWait(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390), 1, a1 + 2);
    result = RtlRaiseStatus((unsigned int)(0xC0000191ULL), *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390), 1, a1 + 2);
loc_0020F284:
    v_stack_mA0 = result;
    v_r10 = 0;
    *(unsigned __int8 *)(result + 10) = 1;
    goto loc_0020EF09;
loc_0020F294:
    result = KeDisableInterrupts((unsigned int)(0xC0000191ULL), *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390), 1, a1 + 2);
    if (*(unsigned __int64 *)(v_stack_mA0 + 14584) == 0) goto loc_0020F5FA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) - 8)) != 0) goto loc_0020F628;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584))) != (*(unsigned __int64 *)(v_stack_mA0 + 14584))) goto loc_0020F34F;
    *(unsigned __int64 *)(v_stack_mA0 + 14584) = a1 + 2;
loc_0020F2CB:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584)) = a1 + 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 48) + 56);
loc_0020F2DA:
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0020F37C;
loc_0020F2E3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 16)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 24))) goto loc_0020F345;
    if (((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 32) + 40)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 40)))) == 0) goto loc_0020F650;
    result = KeDisableInterrupts(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 40)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 16), a1 + 2);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584))) != 0) goto loc_0020F33C;
    if (*(unsigned __int64 *)(v_stack_mA0 + 14584) == 0) goto loc_0020F63D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 8))) != (*(unsigned __int64 *)(v_stack_mA0 + 14584))) goto loc_0020EA22;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584)) = *(unsigned __int64 *)(v_stack_mA0 + 14584);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 8)) = *(unsigned __int64 *)(v_stack_mA0 + 14584);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 8) = *(unsigned __int64 *)(v_stack_mA0 + 14584);
loc_0020F33C:
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0020F558;
loc_0020F345:
    goto loc_0020E751;
loc_0020F34F:
    *(unsigned __int64 *)(v_stack_mA0 + 14584) = *(unsigned __int64 *)(v_stack_mA0 + 14584);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18) + 8)) != v_stack_p18) goto loc_0020EA22;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 8))) != v_stack_p18) goto loc_0020EA22;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 8)) = *(unsigned __int64 *)(v_stack_p18);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18) + 8) = *(unsigned __int64 *)(v_stack_p18 + 8);
    goto loc_0020F2CB;
loc_0020F37C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0020F516;
loc_0020F395:
    goto loc_0020F2E3;
loc_0020F39B:
    result = (unsigned __int8)((*(unsigned __int64 *)(v_stack_p18 + 8)) - (1));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 32) + 824) = (unsigned __int8)(result);
    if (condition_is_not_equal) goto loc_0020F45C;
    v_r12 = (unsigned int)((v_r12) << ((unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 32)))));
    *(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 856) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 856)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 856)))) >= ((unsigned int)(v_r12))) goto loc_0020F45C;
    if ((*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 195)) > 31) goto loc_0020F45C;
    result = Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 14584) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a1 + 2);
    if ((unsigned int)(result) == 0) goto loc_0020F46E;
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 563)))) >= 16) goto loc_0020F43A;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 518)))) & (15));
    result = (unsigned int)((result) + ((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 563)))));
    a3 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) <= ((unsigned int)((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 563))))))) { a3 = (unsigned int)((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 563))))); }
    a4 = 0;
    result = 0;
    if (condition_is_greater) { result = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 870)); }
    a3 = (unsigned int)((a3) + ((unsigned int)((__int8)((unsigned __int8)(result)))));
    if (a3 >= 16) goto loc_0020F69E;
loc_0020F42D:
    a2 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 518)) >> (4));
    if (((unsigned int)((unsigned __int8)(a2))) > a3) { a3 = (unsigned int)((unsigned __int8)(a2)); }
loc_0020F43A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 856))) != 0) goto loc_0020F47D;
loc_0020F444:
    result = (__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 195));
    if (a3 < ((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 195))))) {
        a2 = v_stack_m98;
        a1 = *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390);
        result = KiSetPriorityThread(a1, a2, a3, a4);
    }
    a1 = 0;
    *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 795) = 32;
    *(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390) + 64) = 0;
    goto loc_0020EBD7;
loc_0020F46E:
    a2 = 0;
    result = KiComputeThreadPriorityNonStacking(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390), a2, a3, a4);
    goto loc_0020F444;
loc_0020F47D:
    v_stack_m88 = (unsigned int)(result);
    a3 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) < ((unsigned int)(result))) { a3 = (unsigned int)(result); }
    goto loc_0020F444;
loc_0020F48C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14382630)))) & (64)) == 0) goto loc_0020F16B;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0020F16B;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_p18)), a2, a3, a4);
    goto loc_0020F16D;
loc_0020F4B4:
    result = KiProcessDeferredReadyList(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m98, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390)), a4);
    goto loc_0020E977;
loc_0020F4CB:
    if ((*(unsigned int *)(v_stack_mA0 + 14560)) != 0) goto loc_0020E75E;
    result = KeDisableInterrupts(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m98, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390)), a4);
    if ((*(unsigned __int8 *)(v_stack_mA0 + 14565)) != 0) goto loc_0020F672;
loc_0020F4EE:
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_0020E75E;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0020F5D2;
loc_0020F510:
    goto loc_0020E75E;
loc_0020F516:
loc_0020F51D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0020F51D;
    if (condition_is_above_or_equal) goto loc_0020F395;
    result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_0020F395;
loc_0020F53E:
    if ((((unsigned __int8)(result)) & (24)) == 0) goto loc_0020F599;
    result = KiExitThreadWaitReschedule(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int8 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 390) + 390), v_stack_m98, a4);
    goto loc_0020E977;
loc_0020F558:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0020F578;
loc_0020F56D:
    goto loc_0020E751;
loc_0020F578:
loc_0020F57F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0020F57F;
    if (condition_is_above_or_equal) goto loc_0020F56D;
    result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_0020F56D;
loc_0020F599:
    result = KiProcessDeferredReadyList(*(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m98, 1, a4);
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = KiDeliverApc(a1, a2, a3, a4);
    if ((*(unsigned int *)(v_rip + 14382952)) != 0) {
        a1 = 0;
        a2 = 0;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    result = 0;
    goto loc_0020E977;
loc_0020F5D2:
loc_0020F5D9:
    if (condition_is_not_equal) goto loc_0020F5D9;
    if (condition_is_above_or_equal) goto loc_0020F510;
    result = KiRemoveSystemWorkPriorityKick(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, a4);
    goto loc_0020F510;
loc_0020F5FA:
    if (0 == 0) goto loc_0020F345;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) == 0) goto loc_0020F56D;
loc_0020F628:
    if (v_stack_p18 == ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))) goto loc_0020F2DA;
    *(unsigned __int64 *)(v_stack_mA0 + 14584) = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536)));
    goto loc_0020F2DA;
loc_0020F63D:
    *(unsigned __int64 *)(v_stack_p18 + 8) = v_stack_p18;
    *(unsigned __int64 *)(v_stack_p18) = v_stack_p18;
    *(unsigned __int64 *)(v_stack_mA0 + 14584) = v_stack_p18;
    goto loc_0020F33C;
loc_0020F650:
    result = KiSrcuReportQuiescent(v_stack_p18 - 8, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    if ((unsigned int)(result) == 0) goto loc_0020F345;
    result = KiSrcuFlushCompleted(*(unsigned __int64 *)(v_stack_p18 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_0020F345;
loc_0020F672:
    if ((*(unsigned int *)(v_stack_mA0 + 14560)) != 0) goto loc_0020F4EE;
    *(unsigned __int8 *)(v_stack_mA0 + 14565) = 0;
    *(unsigned __int64 *)(v_stack_mA0 + 14568) = *(unsigned __int64 *)(v_rip + 13703766);
    goto loc_0020F4EE;
loc_0020F69E:
    goto loc_0020F42D;
loc_0020F6A9:
    goto loc_0020F03B;
}
```

## 5. (Beta) C Style

```c
int64_t KeWaitForSingleObject(void *Object, int32_t WaitReason, uint8_t WaitMode, int32_t Alertable, void *Timeout)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m57;
    uint64_t v_stack_m58;
    uint8_t v_stack_m66;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint8_t v_stack_mB8;
    uint32_t v_stack_mE8;
    uint32_t v_stack_p0;
    uint32_t v_stack_p10;
    uint8_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p20 = (uint8_t)(Alertable);
    v_stack_p18 = WaitMode;
    v_stack_p10 = WaitReason;
    v_stack_p8 = Object;
    local_rsp = (local_rsp) - (168);
    Alertable = 0;
    v_stack_m70 = 0;
    v_stack_mA8 = 0;
    v_stack_mB8 = 0;
    v_stack_mA0 = 0;
    v_stack_mB0 = 0;
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_0020ED5D;
    if ((*(uint32_t *)(v_rip + 0xDB85FD)) != 0) goto loc_0020EC55;
loc_0020E729:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) = (uint8_t)(v_cr8);
loc_0020E734:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20)) > 1) goto loc_0020E772;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38F8)) != 0) goto loc_0020F294;
loc_0020E751:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38E5)) != 0) goto loc_0020F4CB;
loc_0020E75E:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38E8)) != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38F0))) goto loc_0020EC15;
loc_0020E772:
    if (Timeout == NULL) goto loc_0020E7AD;
    if ((*(uint32_t *)(Timeout + 0x4)) < 0) goto loc_0020EA66;
    local_r10 = 0;
    v_stack_mA8 = *(uint64_t *)(Timeout);
    v_stack_mB4 = 1;
    goto loc_0020E7B4;
loc_0020E7AD:
    local_r10 = 0;
    v_stack_mB4 = 0;
loc_0020E7B4:
    v_stack_m80 = 0;
loc_0020E7C2:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x70) = 0;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x187) = WaitMode;
    if ((uint8_t)(v_stack_p20) != 0) {
    }
loc_0020E7E0:
    if (condition_is_above_or_equal) goto loc_0020E804;
loc_0020E7E9:
    local_rsi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xDB6ABB)) & ((uint32_t)(local_rsi))) == 0) goto loc_0020ECCE;
loc_0020E7F7:
loc_0020E7F9:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) == 0) goto loc_0020E7E0;
    goto loc_0020E7E9;
loc_0020E804:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC1)) != 0) goto loc_0020ED7C;
loc_0020E811:
    if ((uint8_t)(v_stack_p20) != 0) goto loc_0020EA29;
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC2)) & (2)) != 0) goto loc_0020F0D6;
loc_0020E82E:
    local_r10 = 0;
    goto loc_0020E84C;
loc_0020E833:
    local_r10 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x72)) != 0) goto loc_0020F1E2;
loc_0020E843:
    if (0 != 0) goto loc_0020F0E5;
loc_0020E84C:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x184) = 5;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x283) = (uint8_t)((uint32_t)(v_stack_p10));
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1B4) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p10))));
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = 0;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x140 + 0x10) = 1;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x140 + 0x11) = 4;
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x140 + 0x12) = 0;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x140 + 0x20) = v_stack_p8;
    if (condition_is_below) goto loc_0020EC70;
loc_0020E8A8:
    Object = (uint8_t)(((uint8_t)(*(uint8_t *)(v_stack_p8))) & (127));
    if (((uint8_t)(Object)) == 2) goto loc_0020EA93;
    if (condition_is_greater) goto loc_0020ECA0;
loc_0020E8C9:
    if (((uint32_t)((uint32_t)(v_stack_mB4))) == 2) goto loc_0020E9AF;
    if ((uint32_t)((uint32_t)(v_stack_mB4)) == 0) goto loc_0020EA0F;
    if (v_stack_mA8 != 0) goto loc_0020ECBC;
loc_0020E8F0:
loc_0020E8F6:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x184) = 2;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) == 0) goto loc_0020E930;
loc_0020E920:
    if (condition_is_below) goto loc_0020E990;
    local_r10 = 0;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x40) = 0;
loc_0020E930:
    v_stack_m90 = 0;
    if (((uint32_t)((uint32_t)(v_stack_mB0))) >= 2) goto loc_0020ECFF;
loc_0020E93D:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_mB0)) & (1));
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x70))) & (56)) != 0) goto loc_0020F1CA;
    if ((uint32_t)(local_rbx) != 0) goto loc_0020F0C1;
    result = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x70);
    if ((*(uint32_t *)(v_rip + 0xDB83BF)) != ((uint32_t)(local_rbx))) {
        Object = Alertable + 2;
        WaitReason = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186));
        result = KiLowerIrqlProcessIrqlFlags(Object, WaitReason, v_stack_mA8, (uint32_t)(0xFFFFFF7FULL));
    }
loc_0020E974:
loc_0020E977:
    local_rsp = (local_rsp) + (168);
    return 258;
loc_0020E990:
    local_rsi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xDB6914)) & ((uint32_t)(local_rsi))) == 0) goto loc_0020EE06;
loc_0020E99E:
loc_0020E9A0:
    if (*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x40) == 0) goto loc_0020E920;
    goto loc_0020E990;
loc_0020E9AF:
    Object = (*(uint64_t *)(Object)) - (*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0xF8));
    Object = (Object) - (*(uint64_t *)(*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x40)));
    if ((*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x187)) == 0) goto loc_0020EA06;
    if ((*(uint32_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x1E4)) != 0) goto loc_0020EA06;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186)) != 0) goto loc_0020EA06;
    if ((*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0xC0)) != 0) goto loc_0020EA06;
    result = v_stack_mA8;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x3B8))) != 0) {
        result = v_stack_mA8 + (uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x3B8)) * 1;
    }
    if (Object > result) goto loc_0020E8F0;
loc_0020EA0F:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x10))) == (v_stack_p8 + 8)) goto loc_0020EE67;
loc_0020EA22:
loc_0020EA29:
    if ((*(uint8_t *)((int8_t)(258) + *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) * 1 + 0x72)) != 0) goto loc_0020EE54;
    if (258 == 0) goto loc_0020E833;
    if ((*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0xA8)) == (*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 168)) goto loc_0020E833;
    local_r10 = 0;
    goto loc_0020E843;
loc_0020EA66:
    WaitReason = (*(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x3B8)))) - (*(uint64_t *)(local_r11));
    v_stack_mB4 = (uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20)));
    result = (*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0xF8)) + (*(uint64_t *)(3));
    WaitReason = (WaitReason) - (result);
    v_stack_mA8 = WaitReason;
    local_r10 = 0;
    goto loc_0020E7B4;
loc_0020EA93:
    result = (uint8_t)((*(uint8_t *)(v_stack_p8 + 0x30)) >> (1));
    result = (uint8_t)((result) & (1));
    v_stack_mB8 = (uint8_t)(result);
    if (condition_is_less_or_equal) goto loc_0020EDE3;
loc_0020EAA8:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4)))) == 0x80000000ULL) goto loc_0020F262;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x4))) - (1));
    *(uint32_t *)(v_stack_p8 + 0x4) = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_0020E8F6;
    *(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0xC8) = 0;
loc_0020EAD0:
    if (condition_is_above_or_equal) goto loc_0020EAF4;
loc_0020EAD9:
    local_rsi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xDB67CB)) & ((uint32_t)(local_rsi))) == 0) goto loc_0020EE2D;
loc_0020EAE7:
loc_0020EAE9:
    if (*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x40) == 0) goto loc_0020EAD0;
    goto loc_0020EAD9;
loc_0020EAF4:
    if ((*(uint8_t *)(v_stack_p8 + 0x31)) != 0) {
    }
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8)) != (*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186))) goto loc_0020F122;
loc_0020EB15:
    result = 0;
    v_stack_m58 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m68 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8)));
    v_stack_m66 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BA));
    *(uint32_t *)(v_stack_p8) = (uint32_t)((uint32_t)(v_stack_m68));
    *(uint64_t *)(v_stack_p8 + 0x28) = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186);
    result = *(uint8_t *)(v_stack_p8 + 0x30);
    if ((((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x30))) & (1)) != 0) {
        result = (uint8_t)((*(uint8_t *)(v_stack_p8 + 0x30)) & (254));
        *(uint8_t *)(v_stack_p8 + 0x30) = (uint8_t)(result);
    }
    local_r10 = 0;
    if (((*(uint8_t *)(v_stack_p8 + 0x30)) & (2)) != 0) goto loc_0020F256;
    *(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x3D0) = 0;
loc_0020EB72:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x308 + 0x8))) != (*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 776)) goto loc_0020EA22;
    *(uint64_t *)(v_stack_p8 + 0x18) = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 776;
    *(uint64_t *)(v_stack_p8 + 0x18 + 0x8) = *(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x308 + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x308 + 0x8)) = v_stack_p8 + 24;
    *(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x308 + 0x8) = v_stack_p8 + 24;
    *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x184) = 2;
    *(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x40) = 0;
    if (*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x3D0 * 1) != 0) goto loc_0020F129;
loc_0020EBCA:
    v_stack_m98 = 0;
    if (((uint32_t)(local_rbx)) >= 2) goto loc_0020F14F;
loc_0020EBD7:
    local_rbx = (uint32_t)((local_rbx) & (1));
    if ((((uint8_t)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x70))) & (56)) != 0) goto loc_0020F53E;
    if ((uint32_t)(local_rbx) != 0) goto loc_0020F4B4;
    result = *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x70);
    if ((*(uint32_t *)(v_rip + 0xDB8125)) != ((uint32_t)(local_rbx))) {
        Object = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186);
        WaitReason = (uint8_t)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186));
        result = KiLowerIrqlProcessIrqlFlags(Object, WaitReason, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 976 * 1, (uint32_t)(0xFFFFFF7FULL));
    }
    goto loc_0020E977;
loc_0020EC15:
    Object = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0xC8) + 0x24))) << (5);
    Object = (Object) + (v_rip + 13640865);
    if (((*(uint64_t *)(*(uint64_t *)(Object + 0x8) + 0x38)) & (*(uint64_t *)(Object))) != 0) goto loc_0020E772;
    result = KiRcuReportQuiescentState(Object, WaitReason, *(uint64_t *)(Object), (uint32_t)(0xFFFFFF7FULL));
    if ((uint32_t)(result) == 0) goto loc_0020E772;
    result = KiRcuFlushCompleted(*(uint8_t *)(*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0xC8) + 0x38E6), WaitReason, *(uint64_t *)(Object), (uint32_t)(0xFFFFFF7FULL));
    goto loc_0020E772;
loc_0020EC55:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0xC8)), (uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20))), *(uint64_t *)(Object), (uint32_t)(0xFFFFFF7FULL));
    Alertable = 0;
    goto loc_0020E729;
loc_0020EC70:
    local_rsi = (uint32_t)((*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0xC8)) + 1);
    if (((*(uint32_t *)(v_rip + 0xDB6634)) & ((uint32_t)(local_rsi))) == 0) goto loc_0020EF6D;
loc_0020EC7E:
loc_0020EC80:
    if (sign_flag) goto loc_0020EC70;
    if (condition_is_below) goto loc_0020EC70;
    local_r10 = 0;
    goto loc_0020E8A8;
loc_0020ECA0:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(1))) & (7));
    if (((uint8_t)(result)) == 1) goto loc_0020ECF5;
    if (((uint8_t)((uint8_t)(*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0xC8)))) != 5) goto loc_0020E8F6;
    *(uint32_t *)(1 + 0x4) = (uint32_t)((uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20))) - 1);
    goto loc_0020E8F6;
loc_0020ECBC:
    goto loc_0020EA06;
loc_0020ECCE:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDB7DE4)))) & (64)) == 0) goto loc_0020E7F7;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)((uint8_t)(*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0xC8))), (uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20))), *(uint64_t *)(Object), *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 320);
    if ((uint8_t)(result) == 0) goto loc_0020E7F7;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), (uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20))), *(uint64_t *)(Object), *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 320);
    goto loc_0020E7F9;
loc_0020ECF5:
    *(uint32_t *)(1 + 0x4) = 0;
    goto loc_0020E8F6;
loc_0020ECFF:
loc_0020ED02:
    if (condition_is_above_or_equal) goto loc_0020ED26;
loc_0020ED0B:
    local_rsi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xDB6599)) & ((uint32_t)(local_rsi))) == 0) goto loc_0020F09A;
loc_0020ED19:
loc_0020ED1B:
    if (*(uint64_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x40) == 0) goto loc_0020ED02;
    goto loc_0020ED0B;
loc_0020ED26:
    if ((uint8_t)(*(uint8_t *)((int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x31B)) + *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) * 1 + 0x338)) != 0) goto loc_0020EFA1;
    result = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(343, *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186), (int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x31B)), result + 2);
loc_0020ED5D:
    local_rbx = (condition_is_below) ? 1 : 0;
    local_rbx = (uint32_t)((local_rbx) & (1));
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(local_rbx)));
    local_rbx = (uint32_t)((local_rbx) | (1));
    v_stack_mB0 = (uint32_t)(local_rbx);
    goto loc_0020E734;
loc_0020ED7C:
    if ((*(uint16_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x1E6)) != 0) goto loc_0020E811;
    if (((uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20)))) >= 1) goto loc_0020E811;
    Object = 0;
    *(uint64_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x40) = 0;
    if ((*(uint32_t *)(v_rip + 0xDB7F80)) != 0) {
        Object = *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186);
        WaitReason = 1;
        result = KiLowerIrqlProcessIrqlFlags(Object, WaitReason, (int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x31B)), result + 2);
    }
    WaitMode = 0;
    WaitReason = 0;
    Object = 0;
    result = KiDeliverApc(Object, WaitReason, WaitMode, result + 2);
    if ((*(uint32_t *)(v_rip + 0xDB7F4F)) != 0) goto loc_0020EF60;
loc_0020EDD7:
    *(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x186) = (uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20)));
    local_r10 = 0;
    goto loc_0020E7C2;
loc_0020EDE3:
    if ((*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186)) != (*(uint64_t *)(1 + 0x28))) goto loc_0020E8C9;
    if ((*(uint8_t *)(1 + 0x2)) == ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x38BA)))) goto loc_0020EAA8;
    goto loc_0020E8C9;
loc_0020EE06:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDB7CAC)))) & (64)) == 0) goto loc_0020E99E;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_rbx, WaitReason, WaitMode, result + 2);
    if ((uint8_t)(result) == 0) goto loc_0020E99E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), WaitReason, WaitMode, result + 2);
    goto loc_0020E9A0;
loc_0020EE2D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDB7C85)))) & (64)) == 0) goto loc_0020EAE7;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rsi)), WaitReason, WaitMode, result + 2);
    if ((uint8_t)(result) == 0) goto loc_0020EAE7;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), WaitReason, WaitMode, result + 2);
    goto loc_0020EAE9;
loc_0020EE54:
    *(uint8_t *)(result + *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) * 1 + 0x72) = 0;
    local_r10 = 0;
    goto loc_0020E843;
loc_0020EE67:
    *(uint64_t *)(result + 0x2) = result;
    *(uint64_t *)(result + 0x2 + 0x8) = (uint32_t)((uint32_t)(local_rsi));
    *(uint64_t *)((uint32_t)((uint32_t)(local_rsi))) = result + 2;
    *(uint64_t *)(result + 0x8) = result + 2;
    *(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x24B) = 1;
    if (v_stack_mB8 == 0) goto loc_0020EF57;
    WaitMode = 0;
    WaitReason = 0;
    result = KeAbPreAcquire(1, WaitReason, WaitMode, result + 2);
    v_stack_mA0 = result;
loc_0020EEA7:
    if (result == 0) goto loc_0020EED4;
    Object = (uint8_t)((*(uint8_t *)(result)) | (2));
    *(uint8_t *)(result) = (uint8_t)(Object);
    Object = (*(uint64_t *)(result)) >> (63);
    if ((uint8_t)(Object) != 0) goto loc_0020EF94;
loc_0020EEC4:
    *(uint8_t *)(result + 0x9) = 1;
    result = (uint8_t)((*(uint8_t *)(result)) & (253));
    *(uint8_t *)(result) = (uint8_t)(result);
loc_0020EED4:
    v_stack_p28 = v_stack_m70;
    v_stack_p20 = (uint32_t)(local_rbx);
    result = KiCommitThreadWait(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186), *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 320, 257, v_stack_mA8);
    local_r10 = 0;
    v_stack_mB0 = 0;
    if (result != 0) goto loc_0020F1F1;
loc_0020EF09:
    *(uint64_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x3D0) = 0;
    if (((uint32_t)(result)) != 256) goto loc_0020E974;
    if ((*(uint32_t *)(v_rip + 0xDB7DEF)) != 0) goto loc_0020EF46;
loc_0020EF33:
    *(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x186) = 2;
    goto loc_0020E7B4;
loc_0020EF46:
    result = KiRaiseIrqlProcessIrqlFlags(2, 2, 257, v_stack_mA8);
    local_r10 = 0;
    goto loc_0020EF33;
loc_0020EF57:
    goto loc_0020EEA7;
loc_0020EF60:
    result = KiRaiseIrqlProcessIrqlFlags(2, (uint8_t)(result), 257, v_stack_mA8);
    goto loc_0020EDD7;
loc_0020EF6D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDB7B45)))) & (64)) == 0) goto loc_0020EC7E;
    result = KiCheckVpBackingLongSpinWaitHypercall(2, (uint8_t)(result), 257, v_stack_mA8);
    if ((uint8_t)(result) == 0) goto loc_0020EC7E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_mA0)), (uint8_t)(result), 257, v_stack_mA8);
    goto loc_0020EC80;
loc_0020EF94:
    result = KiAbEntryRemoveFromTree(v_stack_mA0, (uint8_t)(result), 257, v_stack_mA8);
    goto loc_0020EEC4;
loc_0020EFA1:
    result = (uint8_t)((result) - (1));
    *(uint8_t *)(v_stack_mA0 + 0x338) = (uint8_t)(result);
    if (condition_is_not_equal) goto loc_0020F06A;
    local_r12 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)((uint8_t)(result))))));
    *(uint32_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x358) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x358)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x358)))) >= ((uint32_t)(local_r12))) goto loc_0020F06A;
    if ((*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0xC3)) > 31) goto loc_0020F06A;
    result = Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline((uint32_t)((uint32_t)((uint8_t)(result))), (uint8_t)(result), 257, v_stack_mA8);
    if ((uint32_t)(result) == 0) goto loc_0020F07C;
    if (((uint32_t)((int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x233)))) >= 16) goto loc_0020F048;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x206)))) & (15));
    result = (uint32_t)((result) + ((uint32_t)((int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x233)))));
    WaitMode = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) <= ((uint32_t)((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x233))))))) { WaitMode = (uint32_t)((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x233))))); }
    Alertable = 0;
    result = 0;
    if (condition_is_greater) { result = (uint32_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x366)); }
    WaitMode = (uint32_t)((WaitMode) + ((uint32_t)((int8_t)((uint8_t)(result)))));
    if (WaitMode >= 16) goto loc_0020F6A9;
loc_0020F03B:
    WaitReason = (uint32_t)((*(uint16_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x206)) >> (4));
    if (((uint32_t)((uint8_t)(WaitReason))) > WaitMode) { WaitMode = (uint32_t)((uint8_t)(WaitReason)); }
loc_0020F048:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x358))) != 0) goto loc_0020F08B;
loc_0020F052:
    result = (int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0xC3));
    if (WaitMode < ((uint32_t)((int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0xC3))))) {
        WaitReason = v_stack_m90;
        Object = *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186);
        result = KiSetPriorityThread(Object, WaitReason, WaitMode, Alertable);
    }
    result = 0;
    *(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x31B) = 32;
    *(uint64_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x40) = 0;
    goto loc_0020E93D;
loc_0020F07C:
    WaitReason = 0;
    result = KiComputeThreadPriorityNonStacking(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186), WaitReason, WaitMode, Alertable);
    goto loc_0020F052;
loc_0020F08B:
    v_stack_m84 = (uint32_t)(result);
    WaitMode = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) < ((uint32_t)(result))) { WaitMode = (uint32_t)(result); }
    goto loc_0020F052;
loc_0020F09A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDB7A18)))) & (64)) == 0) goto loc_0020ED19;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186), WaitReason, WaitMode, Alertable);
    if ((uint8_t)(result) == 0) goto loc_0020ED19;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_mA0)), WaitReason, WaitMode, Alertable);
    goto loc_0020ED1B;
loc_0020F0C1:
    result = KiProcessDeferredReadyList(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m90, (uint8_t)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186)), Alertable);
    goto loc_0020E974;
loc_0020F0D6:
    if ((uint8_t)(v_stack_p18) == 0) goto loc_0020E82E;
loc_0020F0E5:
    result = KiPerformWaitDeferredWork(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186), 1, 1, v_stack_m80);
    Object = 0;
    *(uint64_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x40) = 0;
    if ((uint32_t)(result) != 0) goto loc_0020F1AF;
    if ((*(uint32_t *)(v_rip + 0xDB7C16)) != 0) {
        Object = 2;
        WaitReason = (uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20)));
        result = KiLowerIrqlProcessIrqlFlags(Object, WaitReason, 1, v_stack_m80);
    }
    goto loc_0020E974;
loc_0020F122:
    Object = 0;
    goto loc_0020EB15;
loc_0020F129:
    *(uint64_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x3D0) = (uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x233))));
    WaitReason = 0;
    result = KeAbPreAcquire(Object, WaitReason, (uint32_t)((uint32_t)(local_r12)), v_stack_m80);
    local_r10 = 0;
    if (result == 0) goto loc_0020EBCA;
    *(uint8_t *)(result + 0xA) = (uint8_t)(local_r12);
    goto loc_0020EBCA;
loc_0020F14F:
loc_0020F152:
    if (condition_is_above_or_equal) goto loc_0020F178;
loc_0020F15B:
    local_r14 = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xDB6147)) & ((uint32_t)(local_r14))) == 0) goto loc_0020F48C;
loc_0020F16B:
loc_0020F16D:
    if (*(uint64_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x40) == 0) goto loc_0020F152;
    goto loc_0020F15B;
loc_0020F178:
    if ((uint8_t)(*(uint8_t *)((int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x31B)) + *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) * 1 + 0x338)) != 0) goto loc_0020F39B;
    Object = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(343, *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186), (int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x31B)), Object + 2);
loc_0020F1AF:
    result = KiProcessDeferredReadyList(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m80, (uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20))), Object + 2);
    goto loc_0020E974;
loc_0020F1CA:
    if ((((uint8_t)(result)) & (24)) == 0) goto loc_0020F21F;
    result = KiExitThreadWaitReschedule(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186), v_stack_m90, Object + 2);
    goto loc_0020E974;
loc_0020F1E2:
    *(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x72) = 0;
    goto loc_0020E843;
loc_0020F1F1:
    WaitMode = 0;
    result = KeAbPreAcquire(local_r12, v_stack_mA0, WaitMode, Object + 2);
    if (((257) & (0xFFFFFF7FULL)) == 0) goto loc_0020F284;
    result = KeAbPostReleaseEx(local_r12, result, WaitMode, Object + 2);
    local_r10 = 0;
    v_stack_mA0 = 0;
    goto loc_0020EF09;
loc_0020F21F:
    result = KiProcessDeferredReadyList(local_r12, v_stack_m90, 1, Object + 2);
    WaitMode = 0;
    WaitReason = 0;
    Object = 0;
    result = KiDeliverApc(Object, WaitReason, WaitMode, Object + 2);
    if ((*(uint32_t *)(v_rip + 0xDB7AE2)) != 0) {
        Object = *(uint64_t *)(gs_base + (0 + 0x20));
        WaitReason = 0;
        result = KiLowerIrqlProcessIrqlFlags(Object, WaitReason, WaitMode, Object + 2);
    }
    result = 0;
    goto loc_0020E974;
loc_0020F256:
    *(uint64_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x3D0) = local_r12;
    goto loc_0020EB72;
loc_0020F262:
    result = KiFastExitThreadWait(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186), 1, Object + 2);
    result = RtlRaiseStatus((uint32_t)(0xC0000191ULL), *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186), 1, Object + 2);
loc_0020F284:
    v_stack_mA0 = result;
    local_r10 = 0;
    *(uint8_t *)(result + 0xA) = 1;
    goto loc_0020EF09;
loc_0020F294:
    result = KeDisableInterrupts((uint32_t)(0xC0000191ULL), *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186), 1, Object + 2);
    if (*(uint64_t *)(v_stack_mA0 + 0x38F8) == 0) goto loc_0020F5FA;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) - 0x8)) != 0) goto loc_0020F628;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8))) != (*(uint64_t *)(v_stack_mA0 + 0x38F8))) goto loc_0020F34F;
    *(void **)(v_stack_mA0 + 0x38F8) = Object + 2;
loc_0020F2CB:
    *(void **)(*(uint64_t *)(v_stack_mA0 + 0x38F8)) = Object + 2;
    *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x10) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x30) + 0x38);
loc_0020F2DA:
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0020F37C;
loc_0020F2E3:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x10)) == (*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x18))) goto loc_0020F345;
    if (((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x20) + 0x28)) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x28)))) == 0) goto loc_0020F650;
    result = KeDisableInterrupts(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x28)), *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x20), *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x10), Object + 2);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8))) != 0) goto loc_0020F33C;
    if (*(uint64_t *)(v_stack_mA0 + 0x38F8) == 0) goto loc_0020F63D;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x8))) != (*(uint64_t *)(v_stack_mA0 + 0x38F8))) goto loc_0020EA22;
    *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8)) = *(uint64_t *)(v_stack_mA0 + 0x38F8);
    *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x8) = *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x8)) = *(uint64_t *)(v_stack_mA0 + 0x38F8);
    *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x8) = *(uint64_t *)(v_stack_mA0 + 0x38F8);
loc_0020F33C:
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0020F558;
loc_0020F345:
    goto loc_0020E751;
loc_0020F34F:
    *(uint64_t *)(v_stack_mA0 + 0x38F8) = *(uint64_t *)(v_stack_mA0 + 0x38F8);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p18) + 0x8)) != v_stack_p18) goto loc_0020EA22;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0x8))) != v_stack_p18) goto loc_0020EA22;
    *(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0x8)) = *(uint64_t *)(v_stack_p18);
    *(uint64_t *)(*(uint64_t *)(v_stack_p18) + 0x8) = *(uint64_t *)(v_stack_p18 + 0x8);
    goto loc_0020F2CB;
loc_0020F37C:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0020F516;
loc_0020F395:
    goto loc_0020F2E3;
loc_0020F39B:
    result = (uint8_t)((*(uint64_t *)(v_stack_p18 + 0x8)) - (1));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x20) + 0x338) = (uint8_t)(result);
    if (condition_is_not_equal) goto loc_0020F45C;
    local_r12 = (uint32_t)((local_r12) << ((uint8_t)(*(uint64_t *)(gs_base + (0 + 0x20)))));
    *(uint32_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x358) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x358)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x358)))) >= ((uint32_t)(local_r12))) goto loc_0020F45C;
    if ((*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0xC3)) > 31) goto loc_0020F45C;
    result = Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x38F8) + 0x20), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Object + 2);
    if ((uint32_t)(result) == 0) goto loc_0020F46E;
    if (((uint32_t)((int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x233)))) >= 16) goto loc_0020F43A;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x206)))) & (15));
    result = (uint32_t)((result) + ((uint32_t)((int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x233)))));
    WaitMode = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) <= ((uint32_t)((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x233))))))) { WaitMode = (uint32_t)((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x233))))); }
    Alertable = 0;
    result = 0;
    if (condition_is_greater) { result = (uint32_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x366)); }
    WaitMode = (uint32_t)((WaitMode) + ((uint32_t)((int8_t)((uint8_t)(result)))));
    if (WaitMode >= 16) goto loc_0020F69E;
loc_0020F42D:
    WaitReason = (uint32_t)((*(uint16_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x206)) >> (4));
    if (((uint32_t)((uint8_t)(WaitReason))) > WaitMode) { WaitMode = (uint32_t)((uint8_t)(WaitReason)); }
loc_0020F43A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x358))) != 0) goto loc_0020F47D;
loc_0020F444:
    result = (int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0xC3));
    if (WaitMode < ((uint32_t)((int8_t)(*(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0xC3))))) {
        WaitReason = v_stack_m98;
        Object = *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186);
        result = KiSetPriorityThread(Object, WaitReason, WaitMode, Alertable);
    }
    Object = 0;
    *(uint8_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x31B) = 32;
    *(uint64_t *)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186) + 0x40) = 0;
    goto loc_0020EBD7;
loc_0020F46E:
    WaitReason = 0;
    result = KiComputeThreadPriorityNonStacking(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186), WaitReason, WaitMode, Alertable);
    goto loc_0020F444;
loc_0020F47D:
    v_stack_m88 = (uint32_t)(result);
    WaitMode = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) < ((uint32_t)(result))) { WaitMode = (uint32_t)(result); }
    goto loc_0020F444;
loc_0020F48C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDB7626)))) & (64)) == 0) goto loc_0020F16B;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186), WaitReason, WaitMode, Alertable);
    if ((uint8_t)(result) == 0) goto loc_0020F16B;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_p18)), WaitReason, WaitMode, Alertable);
    goto loc_0020F16D;
loc_0020F4B4:
    result = KiProcessDeferredReadyList(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m98, (uint8_t)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186)), Alertable);
    goto loc_0020E977;
loc_0020F4CB:
    if ((*(uint32_t *)(v_stack_mA0 + 0x38E0)) != 0) goto loc_0020E75E;
    result = KeDisableInterrupts(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m98, (uint8_t)(*(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186)), Alertable);
    if ((*(uint8_t *)(v_stack_mA0 + 0x38E5)) != 0) goto loc_0020F672;
loc_0020F4EE:
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_0020E75E;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0020F5D2;
loc_0020F510:
    goto loc_0020E75E;
loc_0020F516:
loc_0020F51D:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0020F51D;
    if (condition_is_above_or_equal) goto loc_0020F395;
    result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(gs_base + (0 + 0x20)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Alertable);
    goto loc_0020F395;
loc_0020F53E:
    if ((((uint8_t)(result)) & (24)) == 0) goto loc_0020F599;
    result = KiExitThreadWaitReschedule(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint8_t *)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x186) + 0x186), v_stack_m98, Alertable);
    goto loc_0020E977;
loc_0020F558:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0020F578;
loc_0020F56D:
    goto loc_0020E751;
loc_0020F578:
loc_0020F57F:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0020F57F;
    if (condition_is_above_or_equal) goto loc_0020F56D;
    result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(gs_base + (0 + 0x20)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Alertable);
    goto loc_0020F56D;
loc_0020F599:
    result = KiProcessDeferredReadyList(*(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m98, 1, Alertable);
    WaitMode = 0;
    WaitReason = 0;
    Object = 0;
    result = KiDeliverApc(Object, WaitReason, WaitMode, Alertable);
    if ((*(uint32_t *)(v_rip + 0xDB7768)) != 0) {
        Object = 0;
        WaitReason = 0;
        result = KiLowerIrqlProcessIrqlFlags(Object, WaitReason, WaitMode, Alertable);
    }
    result = 0;
    goto loc_0020E977;
loc_0020F5D2:
loc_0020F5D9:
    if (condition_is_not_equal) goto loc_0020F5D9;
    if (condition_is_above_or_equal) goto loc_0020F510;
    result = KiRemoveSystemWorkPriorityKick(Object, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(WaitMode)))), WaitMode, Alertable);
    goto loc_0020F510;
loc_0020F5FA:
    if (0 == 0) goto loc_0020F345;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) == 0) goto loc_0020F56D;
loc_0020F628:
    if (v_stack_p18 == ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))) goto loc_0020F2DA;
    *(uint64_t *)(v_stack_mA0 + 0x38F8) = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8)));
    goto loc_0020F2DA;
loc_0020F63D:
    *(uint64_t *)(v_stack_p18 + 0x8) = v_stack_p18;
    *(uint64_t *)(v_stack_p18) = v_stack_p18;
    *(uint64_t *)(v_stack_mA0 + 0x38F8) = v_stack_p18;
    goto loc_0020F33C;
loc_0020F650:
    result = KiSrcuReportQuiescent(v_stack_p18 - 8, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Alertable);
    if ((uint32_t)(result) == 0) goto loc_0020F345;
    result = KiSrcuFlushCompleted(*(uint64_t *)(v_stack_p18 + 0x30), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Alertable);
    goto loc_0020F345;
loc_0020F672:
    if ((*(uint32_t *)(v_stack_mA0 + 0x38E0)) != 0) goto loc_0020F4EE;
    *(uint8_t *)(v_stack_mA0 + 0x38E5) = 0;
    *(uint64_t *)(v_stack_mA0 + 0x38E8) = *(uint64_t *)(v_rip + 0xD11A56);
    goto loc_0020F4EE;
loc_0020F69E:
    goto loc_0020F42D;
loc_0020F6A9:
    goto loc_0020F03B;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0020E6B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
