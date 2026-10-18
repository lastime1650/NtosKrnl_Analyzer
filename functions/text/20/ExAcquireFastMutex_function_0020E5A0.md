# ExAcquireFastMutex

- RVA: `0x0020E5A0`–`0x0020E5AC` (길이 `12` bytes)
- VA: `0x000000014020E5A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005DAD4`
- 디코드: `5`개 명령, `12/12` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **208**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [FsRtlLookupPerStreamContextInternal](../26/FsRtlLookupPerStreamContextInternal_function_00265020.md) at `0x0026510B`
- [FsRtlInsertPerStreamContext](../26/FsRtlInsertPerStreamContext_function_00265F70.md) at `0x0026602B`
- [FsRtlRemovePerStreamContext](../26/FsRtlRemovePerStreamContext_function_00267760.md) at `0x00267865`
- [PopIrpWorker](../26/PopIrpWorker_function_0026D410.md) at `0x0026D47C`
- [PopIrpWorker](../26/PopIrpWorker_function_0026D410.md) at `0x0026D55A`
- [PopIrpWorker](../26/PopIrpWorker_function_0026D410.md) at `0x0026D677`
- [PopIrpWorker](../26/PopIrpWorker_function_0026D410.md) at `0x0026D715`
- [CcAcquireBcbLockAndVacbLock](../26/CcAcquireBcbLockAndVacbLock_function_0026FC58.md) at `0x0026FC70`
- [PoRunDownDeviceObject](../26/PoRunDownDeviceObject_function_0026FFFC.md) at `0x0027004C`
- [CcUnmapInactiveViewsInternal](../27/CcUnmapInactiveViewsInternal_function_0027174C.md) at `0x00271BC9`
- [CcGetVacbMiss](../27/CcGetVacbMiss_function_00272900.md) at `0x00272AFD`
- [CcPinFileData](../33/CcPinFileData_function_0033FB40.md) at `0x0033FFD2`
- [CcPinFileData](../33/CcPinFileData_function_0033FB40.md) at `0x00340387`
- [CcPinFileData](../33/CcPinFileData_function_0033FB40.md) at `0x00340692`
- [CcPinFileData](../33/CcPinFileData_function_0033FB40.md) at `0x00340777`
- [CcWriteBehindPreProcess](../35/CcWriteBehindPreProcess_function_00357784.md) at `0x0035793C`
- [CcWriteBehindPostProcess](../35/CcWriteBehindPostProcess_function_00357BB4.md) at `0x00357C3B`
- [CcWriteBehindPostProcess](../35/CcWriteBehindPostProcess_function_00357BB4.md) at `0x00357E16`
- [CcGetDirtyPagesHelper](../35/CcGetDirtyPagesHelper_function_00358D40.md) at `0x00358E74`
- [CcGetDirtyPagesHelper](../35/CcGetDirtyPagesHelper_function_00358D40.md) at `0x00358F89`
- [CcUnpinFileDataEx](../35/CcUnpinFileDataEx_function_00359DEC.md) at `0x00359EAD`
- [CcSetDirtyPinnedData](../35/CcSetDirtyPinnedData_function_0035A120.md) at `0x0035A216`
- [FsRtlRemoveLargeMcbEntry](../38/FsRtlRemoveLargeMcbEntry_function_00386C40.md) at `0x00386C60`
- [FsRtlAddLargeMcbEntry](../38/FsRtlAddLargeMcbEntry_function_00386EB0.md) at `0x00386ED8`
- [CcDeleteMbcb](../38/CcDeleteMbcb_function_0038C088.md) at `0x0038C0D4`
- [FsRtlPrivateInitializeFileLock](../38/FsRtlPrivateInitializeFileLock_function_0038ED34.md) at `0x0038ED50`
- [CcSetDirtyInMask](../3C/CcSetDirtyInMask_function_003CB688.md) at `0x003CB790`
- [CcSetDirtyInMask](../3C/CcSetDirtyInMask_function_003CB688.md) at `0x003CBB24`
- [HalMatchAcpiOemId](../3F/HalMatchAcpiOemId_function_003F6A90.md) at `0x003F6AD9`
- [HalpAcpiGetTable](../3F/HalpAcpiGetTable_function_003F6BF8.md) at `0x003F6C23`
- [HalAcpiGetTableDispatch](../3F/HalAcpiGetTableDispatch_function_003F6C80.md) at `0x003F6C9E`
- [FsRtlTruncateLargeMcb](../3F/FsRtlTruncateLargeMcb_function_003FB420.md) at `0x003FB433`
- [CcAcquireByteRangeForWrite](../40/CcAcquireByteRangeForWrite_function_00401E74.md) at `0x00401F3E`
- [CcAcquireByteRangeForWrite](../40/CcAcquireByteRangeForWrite_function_00401E74.md) at `0x004025C8`
- [CcAcquireByteRangeForWrite](../40/CcAcquireByteRangeForWrite_function_00401E74.md) at `0x0040273E`
- [CcAcquireByteRangeForWrite](../40/CcAcquireByteRangeForWrite_function_00401E74.md) at `0x004027A3`
- [CcAcquireByteRangeForWrite](../40/CcAcquireByteRangeForWrite_function_00401E74.md) at `0x004027FD`
- [CcGetFlushedValidData](../40/CcGetFlushedValidData_function_00402920.md) at `0x00402A82`
- [FsRtlLookupLargeMcbEntry](../40/FsRtlLookupLargeMcbEntry_function_0040A540.md) at `0x0040A568`
- [FsRtlGetNextLargeMcbEntry](../40/FsRtlGetNextLargeMcbEntry_function_0040DBB0.md) at `0x0040DBD3`
- [CcZeroEndOfLastPage](../45/CcZeroEndOfLastPage_function_00453584.md) at `0x004535DC`
- [PnpUnregisterPlugPlayNotification](../47/PnpUnregisterPlugPlayNotification_function_0047AFAC.md) at `0x0047AFDC`
- [PnpUnregisterPlugPlayNotification](../47/PnpUnregisterPlugPlayNotification_function_0047AFAC.md) at `0x0047B044`
- [PnpUnregisterPlugPlayNotification](../47/PnpUnregisterPlugPlayNotification_function_0047AFAC.md) at `0x0047B09F`
- [PnpUnregisterPlugPlayNotification](../47/PnpUnregisterPlugPlayNotification_function_0047AFAC.md) at `0x0047B0F1`
- [PnpUnregisterPlugPlayNotification](../47/PnpUnregisterPlugPlayNotification_function_0047AFAC.md) at `0x0047B134`
- [PopInitilizeAcDcSettings](../48/PopInitilizeAcDcSettings_function_004828D0.md) at `0x00482930`
- [FsRtlLookupLastLargeMcbEntryAndIndex](../48/FsRtlLookupLastLargeMcbEntryAndIndex_function_00485A80.md) at `0x00485AA8`
- [FsRtlNumberOfRunsInLargeMcb](../48/FsRtlNumberOfRunsInLargeMcb_function_00489620.md) at `0x00489630`
- [RawCompletionRoutine](../48/RawCompletionRoutine_function_0048E660.md) at `0x0048E6B6`
- [RawInitiateDeleteVolume](../48/RawInitiateDeleteVolume_function_0048FDFC.md) at `0x0048FEBC`
- [RawInitiateDeleteVolume](../48/RawInitiateDeleteVolume_function_0048FDFC.md) at `0x0048FFC2`
- [CcPrepareMdlWrite](../49/CcPrepareMdlWrite_function_004996D0.md) at `0x00499800`
- [CcPrepareMdlWrite](../49/CcPrepareMdlWrite_function_004996D0.md) at `0x004998CF`
- [PopGetPowerSettingValue](../49/PopGetPowerSettingValue_function_0049C6CC.md) at `0x0049C6EB`
- [PopRunMaximumIrpWorkers](../4A/PopRunMaximumIrpWorkers_function_004A1688.md) at `0x004A16AD`
- [FsRtlpCancelOplockRHIrp](../4A/FsRtlpCancelOplockRHIrp_function_004A55F0.md) at `0x004A56F0`
- [CcRepinBcb](../4A/CcRepinBcb_function_004A7BF0.md) at `0x004A7C11`
- [PpDevNodeRemoveFromTree](../4A/PpDevNodeRemoveFromTree_function_004AD5A0.md) at `0x004AD691`
- [PnpAcquirePowerRelationsQueueLock](../4B/PnpAcquirePowerRelationsQueueLock_function_004B9534.md) at `0x004B953F`
- [IopInvalidateBusRelationsWorker](../4C/IopInvalidateBusRelationsWorker_function_004C8900.md) at `0x004C892D`
- [FsRtlResetLargeMcb](../4C/FsRtlResetLargeMcb_function_004CC1E0.md) at `0x004CC1FB`
- [FsRtlpCancelWaitingIrp](../4E/FsRtlpCancelWaitingIrp_function_004E4698.md) at `0x004E47A5`
- [FsRtlpWaitOnIrp](../4E/FsRtlpWaitOnIrp_function_004E7998.md) at `0x004E7D80`
- [FsRtlpCancelExclusiveIrp](../4F/FsRtlpCancelExclusiveIrp_function_004F96CC.md) at `0x004F970D`
- [PopRunNormalIrpWorkers](../4F/PopRunNormalIrpWorkers_function_004FB768.md) at `0x004FB773`
- [HalpAcpiGetAllTables](../53/HalpAcpiGetAllTables_function_0053EEB0.md) at `0x0053EEBD`
- [HalpAcpiGetFacsMapping](../53/HalpAcpiGetFacsMapping_function_0053F0F0.md) at `0x0053F105`
- [CcGetLsnForFileObject](../57/CcGetLsnForFileObject_function_0057D6F0.md) at `0x0057D731`
- [FsRtlLookupLastLargeMcbEntry](../58/FsRtlLookupLastLargeMcbEntry_function_00581250.md) at `0x00581270`
- [FsRtlSplitLargeMcb](../58/FsRtlSplitLargeMcb_function_00581560.md) at `0x00581580`
- [FsRtlpCancelReadOnlyOplockIrp](../58/FsRtlpCancelReadOnlyOplockIrp_function_00582380.md) at `0x005823C5`
- [PnpDisableUserModeNotifications](../5A/PnpDisableUserModeNotifications_function_005A78F8.md) at `0x005A791D`
- [PnpDisableUserModeNotifications](../5A/PnpDisableUserModeNotifications_function_005A78F8.md) at `0x005A793A`
- [KeConfigureDynamicMemory](../5B/KeConfigureDynamicMemory_function_005B8C9C.md) at `0x005B8CC4`
- [KeAllocateKernelHiberSwapShadowStacks](../5B/KeAllocateKernelHiberSwapShadowStacks_function_005BD658.md) at `0x005BD694`
- [KiOpPatchCode](../5C/KiOpPatchCode_function_005C6900.md) at `0x005C6958`
- [PopIrpWorkerControl](../5D/PopIrpWorkerControl_function_005D93E0.md) at `0x005D9409`
- [RawVerifyVolume](../5E/RawVerifyVolume_function_005E5120.md) at `0x005E517F`
- [RawVerifyVolume](../5E/RawVerifyVolume_function_005E5120.md) at `0x005E51B0`
- [RtlpTraceDatabaseAcquireLock](../5E/RtlpTraceDatabaseAcquireLock_function_005EE938.md) at `0x005EE956`
- [DifExAcquireFastMutexWrapper](../61/DifExAcquireFastMutexWrapper_function_0061D600.md) at `0x0061D6C6`
- [DifKeAcquireGuardedMutexWrapper](../62/DifKeAcquireGuardedMutexWrapper_function_0062E150.md) at `0x0062E216`
- [sub_006DA07A](../6D/Unknown_function_006DA07A.md) at `0x006DA0A5`
- [sub_006F6F06](../6F/Unknown_function_006F6F06.md) at `0x006F6F32`
- [sub_006F875C](../6F/Unknown_function_006F875C.md) at `0x006F8763`
- [HalpIrtAllocateDeviceAperture](../../page/70/HalpIrtAllocateDeviceAperture_function_0070A884.md) at `0x0070A8B8`
- [HalpIrtAllocateDeviceAperture](../../page/70/HalpIrtAllocateDeviceAperture_function_0070A884.md) at `0x0070A93C`
- [HalpIrtAllocateIndex](../../page/70/HalpIrtAllocateIndex_function_0070A9D4.md) at `0x0070AA7C`
- [HalpIrtAllocateIndex](../../page/70/HalpIrtAllocateIndex_function_0070A9D4.md) at `0x0070AAB3`
- [HalpIrtAllocateIndex](../../page/70/HalpIrtAllocateIndex_function_0070A9D4.md) at `0x0070ABE3`
- [HalpIrtExtendApertureRange](../../page/70/HalpIrtExtendApertureRange_function_0070AC38.md) at `0x0070AC79`
- [HalpIrtExtendRemappingRange](../../page/70/HalpIrtExtendRemappingRange_function_0070AD40.md) at `0x0070ADCB`
- [HalpIrtFreeIndex](../../page/70/HalpIrtFreeIndex_function_0070AE30.md) at `0x0070AE7C`
- [HalpIrtReleaseDeviceAperture](../../page/70/HalpIrtReleaseDeviceAperture_function_0070AF00.md) at `0x0070AF15`
- [NtSetInformationDebugObject](../../page/71/NtSetInformationDebugObject_function_007107B0.md) at `0x007108AF`
- [IopSetFileObjectIosbRange](../../page/71/IopSetFileObjectIosbRange_function_0071C1C8.md) at `0x0071C25C`
- [PnpNotifyHwProfileChange](../../page/72/PnpNotifyHwProfileChange_function_00729B04.md) at `0x00729B4C`
- [PnpNotifyHwProfileChange](../../page/72/PnpNotifyHwProfileChange_function_00729B04.md) at `0x00729C5A`
- [PnpNotifyHwProfileChange](../../page/72/PnpNotifyHwProfileChange_function_00729B04.md) at `0x00729CC8`
- [PnpNotifyHwProfileChange](../../page/72/PnpNotifyHwProfileChange_function_00729B04.md) at `0x00729D39`
- [PnpRestartDeviceNode](../../page/72/PnpRestartDeviceNode_function_0072CD60.md) at `0x0072CDF9`
- [PnpProcessCompletedEject](../../page/72/PnpProcessCompletedEject_function_0072D090.md) at `0x0072D13E`
- [IopReleaseResources](../../page/72/IopReleaseResources_function_0072D964.md) at `0x0072D979`
- [PiDqObjectManagerMakeInconsistent](../../page/73/PiDqObjectManagerMakeInconsistent_function_00731A98.md) at `0x00731AB1`
- [PnpProfileUpdateHardwareProfile](../../page/73/PnpProfileUpdateHardwareProfile_function_0073773C.md) at `0x00737768`
- [PpProfileCancelHardwareProfileTransition](../../page/73/PpProfileCancelHardwareProfileTransition_function_00737918.md) at `0x00737923`
- [PpProfileCancelTransitioningDock](../../page/73/PpProfileCancelTransitioningDock_function_007379A0.md) at `0x007379B8`
- [PpProfileCommitTransitioningDock](../../page/73/PpProfileCommitTransitioningDock_function_00737A4C.md) at `0x00737A8B`
- [PpProfileIncludeInHardwareProfileTransition](../../page/73/PpProfileIncludeInHardwareProfileTransition_function_00737B9C.md) at `0x00737BCE`
- [PpProfileQueryHardwareProfileChange](../../page/73/PpProfileQueryHardwareProfileChange_function_00737C5C.md) at `0x00737C87`
- [PnpRemoveEventFromQueue](../../page/73/PnpRemoveEventFromQueue_function_0073808C.md) at `0x007380A6`
- [PiRegisterKernelSoftRestartNotification](../../page/73/PiRegisterKernelSoftRestartNotification_function_0073E28C.md) at `0x0073E341`
- [PipKsrNotifyDrivers](../../page/73/PipKsrNotifyDrivers_function_0073E48C.md) at `0x0073E4C7`
- [PipKsrNotifyDrivers](../../page/73/PipKsrNotifyDrivers_function_0073E48C.md) at `0x0073E5F8`
- [PnpBuildCmResourceLists](../../page/73/PnpBuildCmResourceLists_function_0073E684.md) at `0x0073E6D4`
- [PnpBuildCmResourceLists](../../page/73/PnpBuildCmResourceLists_function_0073E684.md) at `0x0073E7C4`
- [PiUpdateDeviceResourceLists](../../page/74/PiUpdateDeviceResourceLists_function_007406BC.md) at `0x00740758`
- [KeRegisterProcessorChangeCallback](../../page/74/KeRegisterProcessorChangeCallback_function_00746520.md) at `0x007465CC`
- [PfTCleanup](../../page/75/PfTCleanup_function_00751208.md) at `0x007512E2`
- [PfTInitialize](../../page/75/PfTInitialize_function_00751554.md) at `0x00751628`
- [PfTStart](../../page/75/PfTStart_function_007517AC.md) at `0x00751A84`
- [PfSnTracingStateExWorkerRoutine](../../page/75/PfSnTracingStateExWorkerRoutine_function_007528B0.md) at `0x007528C4`
- [PoDisableSleepStates](../../page/75/PoDisableSleepStates_function_00757EE0.md) at `0x00757F33`
- [PoReenableSleepStates](../../page/75/PoReenableSleepStates_function_00757FA0.md) at `0x00757FB0`
- [PoQueueShutdownWorkItem](../../page/75/PoQueueShutdownWorkItem_function_0075BE80.md) at `0x0075BE94`
- [WheaCrashDumpInitializationComplete](../../page/7D/WheaCrashDumpInitializationComplete_function_007D877C.md) at `0x007D878F`
- [WheapReportDeferredLiveDumps](../../page/7D/WheapReportDeferredLiveDumps_function_007D87E0.md) at `0x007D87FD`
- [WheapReportDeferredLiveDumps](../../page/7D/WheapReportDeferredLiveDumps_function_007D87E0.md) at `0x007D8883`
- [CmpGetMappingHiveForString](../../page/84/CmpGetMappingHiveForString_function_0084A5C8.md) at `0x0084A5F2`
- [ExpUpdateDebugInfo](../../page/86/ExpUpdateDebugInfo_function_0086B174.md) at `0x0086B1CC`
- [DbgkpQueueMessage](../../page/8A/DbgkpQueueMessage_function_008A31C0.md) at `0x008A32F7`
- [DbgkpQueueMessage](../../page/8A/DbgkpQueueMessage_function_008A31C0.md) at `0x008A3426`
- [PfSnEndTrace](../../page/8B/PfSnEndTrace_function_008B04A8.md) at `0x008B05F1`
- [EtwpReleaseProviderTraitsReference](../../page/8C/EtwpReleaseProviderTraitsReference_function_008C11EC.md) at `0x008C1236`
- [PiDqObjectManagerUnregisterQuery](../../page/8D/PiDqObjectManagerUnregisterQuery_function_008DC820.md) at `0x008DC839`
- [PiDqObjectManagerEnumerateAndRegisterQuery](../../page/8D/PiDqObjectManagerEnumerateAndRegisterQuery_function_008DCF74.md) at `0x008DD238`
- [PiDqObjectManagerServiceActionQueue](../../page/8D/PiDqObjectManagerServiceActionQueue_function_008DD640.md) at `0x008DD6C8`
- [PiDqObjectManagerServiceActionQueue](../../page/8D/PiDqObjectManagerServiceActionQueue_function_008DD640.md) at `0x008DD7FD`
- [sub_008E5659](../../page/8E/Unknown_function_008E5659.md) at `0x008E568A`
- [PiUEventNotifyTargetDeviceChange](../../page/8E/PiUEventNotifyTargetDeviceChange_function_008E65B0.md) at `0x008E6639`
- [PiUEventNotifyClient](../../page/8E/PiUEventNotifyClient_function_008E6BEC.md) at `0x008E6C1E`
- [PiUEventNotifyClient](../../page/8E/PiUEventNotifyClient_function_008E6BEC.md) at `0x008E6C72`
- [PnpDeviceObjectFromDeviceInstanceWithTag](../../page/8E/PnpDeviceObjectFromDeviceInstanceWithTag_function_008E7490.md) at `0x008E74AF`
- [PiGetRelatedDevice](../../page/8E/PiGetRelatedDevice_function_008E846C.md) at `0x008E84CD`
- [PnpBusTypeGuidGet](../../page/8F/PnpBusTypeGuidGet_function_008FC720.md) at `0x008FC737`
- [PfGetCompletedTrace](../../page/90/PfGetCompletedTrace_function_00902950.md) at `0x00902AC4`
- [PfGetCompletedTrace](../../page/90/PfGetCompletedTrace_function_00902950.md) at `0x00902D33`
- [PopLogDisabledSleepReason](../../page/91/PopLogDisabledSleepReason_function_00911730.md) at `0x00911756`
- [PopFreeSessionState](../../page/91/PopFreeSessionState_function_00912D00.md) at `0x00912D1D`
- [PopGetSettingValue](../../page/91/PopGetSettingValue_function_00913310.md) at `0x0091332F`
- [PopGetSettingNotificationName](../../page/91/PopGetSettingNotificationName_function_0091346C.md) at `0x009134B7`
- [PopSetPowerSettingValue](../../page/91/PopSetPowerSettingValue_function_00914E54.md) at `0x00914EED`
- [PopDispatchPowerSettingCallbacks](../../page/91/PopDispatchPowerSettingCallbacks_function_00916190.md) at `0x009161C4`
- [PopCallPowerSettingCallback](../../page/91/PopCallPowerSettingCallback_function_009162CC.md) at `0x009163A9`
- [sub_0091BE12](../../page/91/Unknown_function_0091BE12.md) at `0x0091BE2E`
- [DbgkpCloseObject](../../page/91/DbgkpCloseObject_function_0091D5F0.md) at `0x0091D61A`
- [DbgkpCloseObject](../../page/91/DbgkpCloseObject_function_0091D5F0.md) at `0x0091D6A7`
- [FsRtlFindInTunnelCacheEx](../../page/93/FsRtlFindInTunnelCacheEx_function_00937A50.md) at `0x00937AA5`
- [FsRtlAddToTunnelCacheEx](../../page/93/FsRtlAddToTunnelCacheEx_function_00937C00.md) at `0x00937CB0`
- [DbgkCopyProcessDebugPort](../../page/94/DbgkCopyProcessDebugPort_function_00947BE8.md) at `0x00947CA1`
- [PnpDeferNotification](../../page/95/PnpDeferNotification_function_00951888.md) at `0x009518AB`
- [PnpDeferNotification](../../page/95/PnpDeferNotification_function_00951888.md) at `0x009518F2`
- [PnpInsertEventInQueue](../../page/95/PnpInsertEventInQueue_function_00951B78.md) at `0x00951BD4`
- [PnpInsertEventInQueue](../../page/95/PnpInsertEventInQueue_function_00951B78.md) at `0x00951BE0`
- [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) at `0x009536B9`
- [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) at `0x009537B8`
- [PnpNotifyDeviceClassChange](../../page/95/PnpNotifyDeviceClassChange_function_0095441C.md) at `0x00954481`
- [PnpNotifyDeviceClassChange](../../page/95/PnpNotifyDeviceClassChange_function_0095441C.md) at `0x009544DD`
- [PnpProcessDeferredRegistrations](../../page/95/PnpProcessDeferredRegistrations_function_009545BC.md) at `0x0095460B`
- [PnpProcessDeferredRegistrations](../../page/95/PnpProcessDeferredRegistrations_function_009545BC.md) at `0x0095469B`
- [PnpNotifyTargetDeviceChange](../../page/95/PnpNotifyTargetDeviceChange_function_00954790.md) at `0x00954811`
- [PnpNotifyTargetDeviceChange](../../page/95/PnpNotifyTargetDeviceChange_function_00954790.md) at `0x00954901`
- [PiUEventNotifyUserMode](../../page/95/PiUEventNotifyUserMode_function_00954CB4.md) at `0x00954F68`
- [PiUEventNotifyUserMode](../../page/95/PiUEventNotifyUserMode_function_00954CB4.md) at `0x009551DB`
- [PiUEventNotifyUserMode](../../page/95/PiUEventNotifyUserMode_function_00954CB4.md) at `0x00955229`
- [PnpDeviceEventWorker](../../page/95/PnpDeviceEventWorker_function_009556B0.md) at `0x0095572A`
- [PnpDeviceEventWorker](../../page/95/PnpDeviceEventWorker_function_009556B0.md) at `0x00955813`
- [PnpDeviceEventWorker](../../page/95/PnpDeviceEventWorker_function_009556B0.md) at `0x009558FF`
- [RawDispatch](../../page/9A/RawDispatch_function_009A3920.md) at `0x009A39D8`
- [RawCleanup](../../page/9A/RawCleanup_function_009A3B38.md) at `0x009A3B67`
- [RawClose](../../page/9A/RawClose_function_009A3CCC.md) at `0x009A3CF8`
- [RawReadWriteDeviceControl](../../page/9A/RawReadWriteDeviceControl_function_009A3D50.md) at `0x009A3E27`
- [RawCreate](../../page/9A/RawCreate_function_009A3E5C.md) at `0x009A3E88`
- [RawUserFsCtrl](../../page/9A/RawUserFsCtrl_function_009A45F4.md) at `0x009A46D5`
- [RawUserFsCtrl](../../page/9A/RawUserFsCtrl_function_009A45F4.md) at `0x009A4737`
- [RawUserFsCtrl](../../page/9A/RawUserFsCtrl_function_009A45F4.md) at `0x009A4773`
- [RawUserFsCtrl](../../page/9A/RawUserFsCtrl_function_009A45F4.md) at `0x009A47AE`
- [RawMountVolume](../../page/9A/RawMountVolume_function_009A4844.md) at `0x009A4A64`
- [RawScanDeletedList](../../page/9A/RawScanDeletedList_function_009A55F0.md) at `0x009A561B`
- [FsRtlTeardownPerStreamContexts](../../page/9A/FsRtlTeardownPerStreamContexts_function_009A5CD0.md) at `0x009A5DE4`
- [FsRtlTeardownPerStreamContexts](../../page/9A/FsRtlTeardownPerStreamContexts_function_009A5CD0.md) at `0x009A5E59`
- [NtQueryInformationProcess](../../page/9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AD5A2`
- [CmpVERemoveHiveFromSIDMappingTable](../../page/9B/CmpVERemoveHiveFromSIDMappingTable_function_009B3244.md) at `0x009B326E`
- [PiUEventHandleVetoEvent](../../page/9C/PiUEventHandleVetoEvent_function_009C2744.md) at `0x009C27A9`
- [PiUEventProcessEventWorker](../../page/9C/PiUEventProcessEventWorker_function_009C2870.md) at `0x009C2898`
- [PiUEventProcessEventWorker](../../page/9C/PiUEventProcessEventWorker_function_009C2870.md) at `0x009C2901`
- [PiUEventHandleGetEvent](../../page/9C/PiUEventHandleGetEvent_function_009C2C30.md) at `0x009C2C8F`
- [PiUEventDereferenceEventEntry](../../page/9C/PiUEventDereferenceEventEntry_function_009C3244.md) at `0x009C3255`
- [PiUEventHandleRegistration](../../page/9C/PiUEventHandleRegistration_function_009C3304.md) at `0x009C356B`
- [PiUEventFreeClientRegistrationContext](../../page/9C/PiUEventFreeClientRegistrationContext_function_009C3A2C.md) at `0x009C3A4D`
- [PiUEventFreeClientRegistrationContext](../../page/9C/PiUEventFreeClientRegistrationContext_function_009C3A2C.md) at `0x009C3A56`
- [PiUEventHandleUnregisterClient](../../page/9C/PiUEventHandleUnregisterClient_function_009C3BBC.md) at `0x009C3BD5`
- [PiUEventNotifyDeviceInstancePropertyChange](../../page/9C/PiUEventNotifyDeviceInstancePropertyChange_function_009C3C04.md) at `0x009C3C39`
- [PiUEventNotifyDeviceInterfaceChange](../../page/9C/PiUEventNotifyDeviceInterfaceChange_function_009C3CF4.md) at `0x009C3D3E`
- [PiUEventNotifyDeviceInstanceChange](../../page/9C/PiUEventNotifyDeviceInstanceChange_function_009C3E2C.md) at `0x009C3E6F`
- [PiUEventQueueBroadcastEventEntry](../../page/9C/PiUEventQueueBroadcastEventEntry_function_009C3F44.md) at `0x009C3F5D`
- [FsRtlAcquireToCreateMappedSection](../../page/9D/FsRtlAcquireToCreateMappedSection_function_009D8D48.md) at `0x009D8DFC`
- [CmpDelayCloseWorker](../../page/9D/CmpDelayCloseWorker_function_009DB8E0.md) at `0x009DB97F`
- [IopCleanupFileObjectIosbRange](../../page/9E/IopCleanupFileObjectIosbRange_function_009E88A8.md) at `0x009E88E8`
- [EtwpSetProviderTraitsCommon](../../page/9F/EtwpSetProviderTraitsCommon_function_009F36EC.md) at `0x009F3797`
- [IopDestroyDeviceNode](../../page/A0/IopDestroyDeviceNode_function_00A06A3C.md) at `0x00A06AE4`
- [IopLegacyResourceAllocation](../../page/A0/IopLegacyResourceAllocation_function_00A07224.md) at `0x00A07395`
- [IopLegacyResourceAllocation](../../page/A0/IopLegacyResourceAllocation_function_00A07224.md) at `0x00A073DE`
- [PnpFreeDeviceInstancePath](../../page/A0/PnpFreeDeviceInstancePath_function_00A074F0.md) at `0x00A07504`
- [PnpCleanupDeviceRegistryValues](../../page/A0/PnpCleanupDeviceRegistryValues_function_00A0797C.md) at `0x00A07997`
- [DbgkClearProcessDebugObject](../../page/A1/DbgkClearProcessDebugObject_function_00A10110.md) at `0x00A10138`
- [DbgkClearProcessDebugObject](../../page/A1/DbgkClearProcessDebugObject_function_00A10110.md) at `0x00A1019E`
- [NtDebugContinue](../../page/A1/NtDebugContinue_function_00A10280.md) at `0x00A10330`
- [DbgkpSetProcessDebugObject](../../page/A1/DbgkpSetProcessDebugObject_function_00A10468.md) at `0x00A104D7`
- [KeSynchronizeWithDynamicProcessors](../../page/A1/KeSynchronizeWithDynamicProcessors_function_00A17094.md) at `0x00A170BD`
- [PiUEventNotifyClientPendingEvent](../../page/A1/PiUEventNotifyClientPendingEvent_function_00A1E784.md) at `0x00A1E791`
- [PiUEventReferenceEventEntry](../../page/A2/PiUEventReferenceEventEntry_function_00A2143C.md) at `0x00A2144D`
- [PnpProcessAssignResources](../../page/A2/PnpProcessAssignResources_function_00A2A950.md) at `0x00A2AAD6`
- [PnpGetResourceRequirementsForAssignTable](../../page/A2/PnpGetResourceRequirementsForAssignTable_function_00A2ADBC.md) at `0x00A2AE27`
- [PnpGetResourceRequirementsForAssignTable](../../page/A2/PnpGetResourceRequirementsForAssignTable_function_00A2ADBC.md) at `0x00A2AEC2`
- [PnpBusTypeGuidGetIndex](../../page/A2/PnpBusTypeGuidGetIndex_function_00A2B088.md) at `0x00A2B0A6`
- [PopRundownPowerSettings](../../page/A3/PopRundownPowerSettings_function_00A39360.md) at `0x00A39376`
- [PopDispatchNotificationsToList](../../page/A3/PopDispatchNotificationsToList_function_00A3ADA8.md) at `0x00A3ADE1`
- [PopDispatchNotificationsToList](../../page/A3/PopDispatchNotificationsToList_function_00A3ADA8.md) at `0x00A3AEFA`
- [PiDqObjectManagerHandleObjectEvent](../../page/A4/PiDqObjectManagerHandleObjectEvent_function_00A4402C.md) at `0x00A4405D`
- [NtWaitForDebugEvent](../../page/A4/NtWaitForDebugEvent_function_00A464E0.md) at `0x00A466D8`
- [PfSnGetCompletedTrace](../../page/A5/PfSnGetCompletedTrace_function_00A51C74.md) at `0x00A51CA0`
- [PfSnGetCompletedTrace](../../page/A5/PfSnGetCompletedTrace_function_00A51C74.md) at `0x00A51DE9`
- [FsRtlDeleteKeyFromTunnelCache](../../page/A5/FsRtlDeleteKeyFromTunnelCache_function_00A51E30.md) at `0x00A51E6B`
- [PfTTraceListAdd](../../page/A6/PfTTraceListAdd_function_00A60E00.md) at `0x00A60E3C`
- [ExSwapinWorkerThreads](../../page/A6/ExSwapinWorkerThreads_function_00A68C40.md) at `0x00A68C9F`
- [PopRequestShutdownWait](../../page/A6/PopRequestShutdownWait_function_00A6AE34.md) at `0x00A6AE84`
- [PiUEventBroadcastEventWorker](../../page/A7/PiUEventBroadcastEventWorker_function_00A764D0.md) at `0x00A764FD`
- [PiUEventBroadcastEventWorker](../../page/A7/PiUEventBroadcastEventWorker_function_00A764D0.md) at `0x00A76527`
- [PoRegisterPowerSettingCallback](../../page/A8/PoRegisterPowerSettingCallback_function_00A82150.md) at `0x00A82274`
- [DbgkOpenProcessDebugPort](../../page/A8/DbgkOpenProcessDebugPort_function_00A82414.md) at `0x00A8245F`
- [PoUnregisterPowerSettingCallback](../../page/A8/PoUnregisterPowerSettingCallback_function_00A8E940.md) at `0x00A8E975`
- [PnpMapDeviceObjectToDeviceInstance](../../page/A9/PnpMapDeviceObjectToDeviceInstance_function_00A9D884.md) at `0x00A9D89B`
- [CmpAddStringToMapping](../../page/AA/CmpAddStringToMapping_function_00AA222C.md) at `0x00AA224F`
- [PnpOrphanNotification](../../page/AA/PnpOrphanNotification_function_00AAF78C.md) at `0x00AAF7A5`
- [CmpDelayFreeRMWorker](../../page/AB/CmpDelayFreeRMWorker_function_00AB65B0.md) at `0x00AB65DA`
- [CmpDelayFreeRMWorker](../../page/AB/CmpDelayFreeRMWorker_function_00AB65B0.md) at `0x00AB6650`
- [CmpDelayFreeCmRm](../../page/AC/CmpDelayFreeCmRm_function_00AC71B8.md) at `0x00AC71C8`
- [DbgkpMarkProcessPeb](../../page/AC/DbgkpMarkProcessPeb_function_00AC8D0C.md) at `0x00AC8D78`
- [PoVolumeDevice](../../page/AC/PoVolumeDevice_function_00AC9290.md) at `0x00AC92AA`
- [PopQueryPowerSettingUlong](../../page/AC/PopQueryPowerSettingUlong_function_00ACCCC8.md) at `0x00ACCCEF`
- [sub_00B1F43A](../../page/B1/Unknown_function_00B1F43A.md) at `0x00B1F45D`
- [sub_00B1F43A](../../page/B1/Unknown_function_00B1F43A.md) at `0x00B1F4D1`
- [sub_00B1FEC0](../../page/B1/Unknown_function_00B1FEC0.md) at `0x00B1FF21`
- [sub_00B256F6](../../page/B2/Unknown_function_00B256F6.md) at `0x00B2578B`
- [sub_00B26446](../../page/B2/Unknown_function_00B26446.md) at `0x00B264B2`
- [sub_00B26560](../../page/B2/Unknown_function_00B26560.md) at `0x00B26586`
- [sub_00B26560](../../page/B2/Unknown_function_00B26560.md) at `0x00B26623`
- [sub_00B2EDF4](../../page/B2/Unknown_function_00B2EDF4.md) at `0x00B2EDFB`
- [sub_00B36A42](../../page/B3/Unknown_function_00B36A42.md) at `0x00B36A4D`
- [sub_00B465F2](../../page/B4/Unknown_function_00B465F2.md) at `0x00B4662A`
- [PopGracefulShutdown](../../pagelk/B6/PopGracefulShutdown_function_00B6BEC8.md) at `0x00B6BF5B`
- [WheapCreateLiveDumpFromPreviousSession](../../pagelk/B7/WheapCreateLiveDumpFromPreviousSession_function_00B73698.md) at `0x00B736D7`
- [WheapSaveRecordForLiveDump](../../pagelk/B7/WheapSaveRecordForLiveDump_function_00B7372C.md) at `0x00B73797`
- [PopFlushVolumeWorker](../../pagelk/B7/PopFlushVolumeWorker_function_00B7AEB0.md) at `0x00B7AF1C`
- [PopFlushVolumeWorker](../../pagelk/B7/PopFlushVolumeWorker_function_00B7AEB0.md) at `0x00B7B070`
- [PopFlushVolumes](../../pagelk/B7/PopFlushVolumes_function_00B7B938.md) at `0x00B7BA12`
- [sub_00B80E6E](../../pagelk/B8/Unknown_function_00B80E6E.md) at `0x00B80FCC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0020E5A0  40 53                           push rbx
0020E5A2  56                              push rsi
0020E5A3  41 56                           push r14
0020E5A5  48 83 EC 30                     sub rsp, 0x30
0020E5A9  45 33 C0                        xor r8d, r8d
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall ExAcquireFastMutex(__int64 a1, __int64 a2, int a3)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    a3 = 0;
    return;
}
```

## 5. (Beta) C Style

```c
void ExAcquireFastMutex(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    Arg3 = 0;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0020E5A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0020E5A0[BB_0020E5A0]
```
