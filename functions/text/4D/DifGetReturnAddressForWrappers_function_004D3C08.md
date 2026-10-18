# DifGetReturnAddressForWrappers

- RVA: `0x004D3C08`–`0x004D3C46` (길이 `62` bytes)
- VA: `0x00000001404D3C08`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068D5C`
- 디코드: `19`개 명령, `62/62` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **468**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004D3C29` → [RtlCaptureStackBackTrace](../2F/RtlCaptureStackBackTrace_function_002F9FF0.md) (function, `0x002F9FF0`)

### Direct callers
- [DifCcCopyWriteExWrapper](../61/DifCcCopyWriteExWrapper_function_0061C0E0.md) at `0x0061C14E`
- [DifCcCopyWriteWrapper](../61/DifCcCopyWriteWrapper_function_0061C2A0.md) at `0x0061C306`
- [DifCcDeferWriteWrapper](../61/DifCcDeferWriteWrapper_function_0061C450.md) at `0x0061C4B6`
- [DifCcFastCopyWriteWrapper](../61/DifCcFastCopyWriteWrapper_function_0061C5F0.md) at `0x0061C650`
- [DifCmRegisterCallbackExWrapper](../61/DifCmRegisterCallbackExWrapper_function_0061C780.md) at `0x0061C7E8`
- [DifCmRegisterCallbackWrapper](../61/DifCmRegisterCallbackWrapper_function_0061C930.md) at `0x0061C994`
- [DifCmUnRegisterCallbackWrapper](../61/DifCmUnRegisterCallbackWrapper_function_0061CAB0.md) at `0x0061CB07`
- [DifEtwRegisterWrapper](../61/DifEtwRegisterWrapper_function_0061D1A0.md) at `0x0061D206`
- [DifEtwUnregisterWrapper](../61/DifEtwUnregisterWrapper_function_0061D330.md) at `0x0061D387`
- [DifExAcquireFastMutexUnsafeWrapper](../61/DifExAcquireFastMutexUnsafeWrapper_function_0061D4A0.md) at `0x0061D4F0`
- [DifExAcquireFastMutexWrapper](../61/DifExAcquireFastMutexWrapper_function_0061D600.md) at `0x0061D650`
- [DifExAcquireFastResourceExclusiveWrapper](../61/DifExAcquireFastResourceExclusiveWrapper_function_0061D760.md) at `0x0061D7C4`
- [DifExAcquireFastResourceSharedStarveExclusiveWrapper](../61/DifExAcquireFastResourceSharedStarveExclusiveWrapper_function_0061D8E0.md) at `0x0061D944`
- [DifExAcquireFastResourceSharedWrapper](../61/DifExAcquireFastResourceSharedWrapper_function_0061DA60.md) at `0x0061DAC4`
- [DifExAcquireResourceExclusiveLiteWrapper](../61/DifExAcquireResourceExclusiveLiteWrapper_function_0061DBE0.md) at `0x0061DC36`
- [DifExAcquireResourceSharedLiteWrapper](../61/DifExAcquireResourceSharedLiteWrapper_function_0061DD50.md) at `0x0061DDA6`
- [DifExAcquireSharedStarveExclusiveWrapper](../61/DifExAcquireSharedStarveExclusiveWrapper_function_0061DEC0.md) at `0x0061DF16`
- [DifExAcquireSharedWaitForExclusiveWrapper](../61/DifExAcquireSharedWaitForExclusiveWrapper_function_0061E030.md) at `0x0061E086`
- [DifExAllocateCacheAwareRundownProtectionWrapper](../61/DifExAllocateCacheAwareRundownProtectionWrapper_function_0061E1A0.md) at `0x0061E1F9`
- [DifExAllocatePool2Wrapper](../61/DifExAllocatePool2Wrapper_function_0061E310.md) at `0x0061E377`
- [DifExAllocatePool3Wrapper](../61/DifExAllocatePool3Wrapper_function_0061E4E0.md) at `0x0061E547`
- [DifExAllocatePoolWithQuotaTagWrapper](../61/DifExAllocatePoolWithQuotaTagWrapper_function_0061E6B0.md) at `0x0061E717`
- [DifExAllocatePoolWithQuotaWrapper](../61/DifExAllocatePoolWithQuotaWrapper_function_0061E880.md) at `0x0061E8E7`
- [DifExAllocatePoolWithTagPriorityWrapper](../61/DifExAllocatePoolWithTagPriorityWrapper_function_0061EA50.md) at `0x0061EAB7`
- [DifExAllocatePoolWithTagWrapper](../61/DifExAllocatePoolWithTagWrapper_function_0061EC20.md) at `0x0061EC87`
- [DifExAllocatePoolWrapper](../61/DifExAllocatePoolWrapper_function_0061EDF0.md) at `0x0061EE57`
- [DifExConvertExclusiveToSharedLiteWrapper](../61/DifExConvertExclusiveToSharedLiteWrapper_function_0061EFC0.md) at `0x0061F010`
- [DifExConvertFastResourceExclusiveToSharedWrapper](../61/DifExConvertFastResourceExclusiveToSharedWrapper_function_0061F120.md) at `0x0061F179`
- [DifExCreateCallbackWrapper](../61/DifExCreateCallbackWrapper_function_0061F290.md) at `0x0061F2FA`
- [DifExDeleteFastResourceWrapper](../61/DifExDeleteFastResourceWrapper_function_0061F420.md) at `0x0061F470`
- [DifExDeleteLookasideListExWrapper](../61/DifExDeleteLookasideListExWrapper_function_0061F5F0.md) at `0x0061F640`
- [DifExDeleteNPagedLookasideListWrapper](../61/DifExDeleteNPagedLookasideListWrapper_function_0061F750.md) at `0x0061F7A0`
- [DifExDeletePagedLookasideListWrapper](../61/DifExDeletePagedLookasideListWrapper_function_0061F8B0.md) at `0x0061F900`
- [DifExDeleteResourceLiteWrapper](../61/DifExDeleteResourceLiteWrapper_function_0061FA10.md) at `0x0061FA67`
- [DifExDisownFastResourceWrapper](../61/DifExDisownFastResourceWrapper_function_0061FB80.md) at `0x0061FBD9`
- [DifExEnterCriticalRegionAndAcquireResourceExclusiveWrapper](../61/DifExEnterCriticalRegionAndAcquireResourceExclusiveWrapper_function_0061FCF0.md) at `0x0061FD47`
- [DifExEnterCriticalRegionAndAcquireResourceSharedWrapper](../61/DifExEnterCriticalRegionAndAcquireResourceSharedWrapper_function_0061FE60.md) at `0x0061FEB7`
- [DifExEnterCriticalRegionAndAcquireSharedWaitForExclusiveWrapper](../61/DifExEnterCriticalRegionAndAcquireSharedWaitForExclusiveWrapper_function_0061FFD0.md) at `0x00620027`
- [DifExEnterPriorityRegionAndAcquireResourceExclusiveWrapper](../62/DifExEnterPriorityRegionAndAcquireResourceExclusiveWrapper_function_00620140.md) at `0x00620197`
- [DifExEnterPriorityRegionAndAcquireResourceSharedWrapper](../62/DifExEnterPriorityRegionAndAcquireResourceSharedWrapper_function_006202B0.md) at `0x00620307`
- [DifExFreePoolWithTagWrapper](../62/DifExFreePoolWithTagWrapper_function_00620420.md) at `0x00620479`
- [DifExFreePoolWrapper](../62/DifExFreePoolWrapper_function_00620590.md) at `0x006205E0`
- [DifExInitializeFastOwnerEntryWrapper](../62/DifExInitializeFastOwnerEntryWrapper_function_006206F0.md) at `0x00620740`
- [DifExInitializeFastResourceAcquiredWrapper](../62/DifExInitializeFastResourceAcquiredWrapper_function_00620850.md) at `0x006208AE`
- [DifExInitializeFastResourceWrapper](../62/DifExInitializeFastResourceWrapper_function_006209D0.md) at `0x00620A29`
- [DifExInitializeLookasideListExWrapper](../62/DifExInitializeLookasideListExWrapper_function_00620B40.md) at `0x00620BA8`
- [DifExInitializeNPagedLookasideListWrapper](../62/DifExInitializeNPagedLookasideListWrapper_function_00620D20.md) at `0x00620D88`
- [DifExInitializePagedLookasideListWrapper](../62/DifExInitializePagedLookasideListWrapper_function_00620EF0.md) at `0x00620F58`
- [DifExInitializeResourceLiteWrapper](../62/DifExInitializeResourceLiteWrapper_function_006210C0.md) at `0x00621117`
- [DifExIsFastResourceContendedWrapper](../62/DifExIsFastResourceContendedWrapper_function_00621230.md) at `0x00621287`
- [DifExIsFastResourceHeldExclusiveWrapper](../62/DifExIsFastResourceHeldExclusiveWrapper_function_006213A0.md) at `0x006213F7`
- [DifExIsFastResourceHeldWrapper](../62/DifExIsFastResourceHeldWrapper_function_00621510.md) at `0x00621567`
- [DifExIsProcessorFeaturePresentWrapper](../62/DifExIsProcessorFeaturePresentWrapper_function_00621680.md) at `0x006216CF`
- [DifExIsResourceAcquiredExclusiveLiteWrapper](../62/DifExIsResourceAcquiredExclusiveLiteWrapper_function_006217E0.md) at `0x00621837`
- [DifExIsResourceAcquiredSharedLiteWrapper](../62/DifExIsResourceAcquiredSharedLiteWrapper_function_00621950.md) at `0x006219A7`
- [DifExRaiseAccessViolationWrapper](../62/DifExRaiseAccessViolationWrapper_function_00621AC0.md) at `0x00621B02`
- [DifExRaiseDatatypeMisalignmentWrapper](../62/DifExRaiseDatatypeMisalignmentWrapper_function_00621B80.md) at `0x00621BC2`
- [DifExRaiseStatusWrapper](../62/DifExRaiseStatusWrapper_function_00621C40.md) at `0x00621C8A`
- [DifExRegisterCallbackWrapper](../62/DifExRegisterCallbackWrapper_function_00621D10.md) at `0x00621D74`
- [DifExReinitializeFastResourceWrapper](../62/DifExReinitializeFastResourceWrapper_function_00621E90.md) at `0x00621EE0`
- [DifExReleaseDisownedFastResourceExclusiveWrapper](../62/DifExReleaseDisownedFastResourceExclusiveWrapper_function_00621FF0.md) at `0x00622049`
- [DifExReleaseDisownedFastResourceSharedWrapper](../62/DifExReleaseDisownedFastResourceSharedWrapper_function_00622160.md) at `0x006221B9`
- [DifExReleaseDisownedFastResourceWrapper](../62/DifExReleaseDisownedFastResourceWrapper_function_006222D0.md) at `0x00622329`
- [DifExReleaseFastMutexUnsafeWrapper](../62/DifExReleaseFastMutexUnsafeWrapper_function_00622440.md) at `0x00622490`
- [DifExReleaseFastMutexWrapper](../62/DifExReleaseFastMutexWrapper_function_006225A0.md) at `0x006225F0`
- [DifExReleaseFastResourceExclusiveWrapper](../62/DifExReleaseFastResourceExclusiveWrapper_function_00622700.md) at `0x00622759`
- [DifExReleaseFastResourceSharedWrapper](../62/DifExReleaseFastResourceSharedWrapper_function_00622870.md) at `0x006228C9`
- [DifExReleaseFastResourceWrapper](../62/DifExReleaseFastResourceWrapper_function_006229E0.md) at `0x00622A39`
- [DifExReleaseResourceAndLeaveCriticalRegionWrapper](../62/DifExReleaseResourceAndLeaveCriticalRegionWrapper_function_00622B50.md) at `0x00622BA0`
- [DifExReleaseResourceAndLeavePriorityRegionWrapper](../62/DifExReleaseResourceAndLeavePriorityRegionWrapper_function_00622CB0.md) at `0x00622D00`
- [DifExReleaseResourceForThreadLiteWrapper](../62/DifExReleaseResourceForThreadLiteWrapper_function_00622E10.md) at `0x00622E69`
- [DifExReleaseResourceLiteWrapper](../62/DifExReleaseResourceLiteWrapper_function_00622F80.md) at `0x00622FD0`
- [DifExSetTimerResolutionWrapper](../62/DifExSetTimerResolutionWrapper_function_006230E0.md) at `0x00623139`
- [DifExTryToAcquireFastMutexWrapper](../62/DifExTryToAcquireFastMutexWrapper_function_00623250.md) at `0x006232A7`
- [DifExTryToAcquireResourceExclusiveLiteWrapper](../62/DifExTryToAcquireResourceExclusiveLiteWrapper_function_006233C0.md) at `0x00623417`
- [DifExTryToConvertFastResourceSharedToExclusiveWrapper](../62/DifExTryToConvertFastResourceSharedToExclusiveWrapper_function_00623530.md) at `0x00623586`
- [DifExUnregisterCallbackWrapper](../62/DifExUnregisterCallbackWrapper_function_006236A0.md) at `0x006236F0`
- [DifExUuidCreateWrapper](../62/DifExUuidCreateWrapper_function_00623800.md) at `0x00623857`
- [DifExfAcquirePushLockExclusiveWrapper](../62/DifExfAcquirePushLockExclusiveWrapper_function_00623970.md) at `0x006239C0`
- [DifExfAcquirePushLockSharedWrapper](../62/DifExfAcquirePushLockSharedWrapper_function_00623AD0.md) at `0x00623B20`
- [DifExfReleasePushLockSharedWrapper](../62/DifExfReleasePushLockSharedWrapper_function_00623C30.md) at `0x00623C80`
- [DifExfReleasePushLockWrapper](../62/DifExfReleasePushLockWrapper_function_00623D90.md) at `0x00623DE0`
- [DifExfTryAcquirePushLockSharedWrapper](../62/DifExfTryAcquirePushLockSharedWrapper_function_00623EF0.md) at `0x00623F47`
- [DifExfTryToWakePushLockWrapper](../62/DifExfTryToWakePushLockWrapper_function_00624060.md) at `0x006240B0`
- [DifHalAllocateCrashDumpRegistersWrapper](../62/DifHalAllocateCrashDumpRegistersWrapper_function_006241C0.md) at `0x00624216`
- [DifHalDmaAllocateCrashDumpRegistersExWrapper](../62/DifHalDmaAllocateCrashDumpRegistersExWrapper_function_00624330.md) at `0x00624396`
- [DifHalDmaFreeCrashDumpRegistersExWrapper](../62/DifHalDmaFreeCrashDumpRegistersExWrapper_function_006244D0.md) at `0x00624526`
- [DifIoAcquireRemoveLockExWrapper](../62/DifIoAcquireRemoveLockExWrapper_function_00627200.md) at `0x00627266`
- [DifIoAllocateControllerWrapper](../62/DifIoAllocateControllerWrapper_function_006273A0.md) at `0x00627408`
- [DifIoAllocateDriverObjectExtensionWrapper](../62/DifIoAllocateDriverObjectExtensionWrapper_function_00627530.md) at `0x00627596`
- [DifIoAllocateErrorLogEntryWrapper](../62/DifIoAllocateErrorLogEntryWrapper_function_006276C0.md) at `0x00627716`
- [DifIoAllocateIrpExWrapper](../62/DifIoAllocateIrpExWrapper_function_00627830.md) at `0x0062789A`
- [DifIoAllocateIrpWrapper](../62/DifIoAllocateIrpWrapper_function_006279D0.md) at `0x00627A3A`
- [DifIoAllocateMdlWrapper](../62/DifIoAllocateMdlWrapper_function_00627B70.md) at `0x00627BD8`
- [DifIoAllocateWorkItemWrapper](../62/DifIoAllocateWorkItemWrapper_function_00627D30.md) at `0x00627D8E`
- [DifIoAttachDeviceWrapper](../62/DifIoAttachDeviceWrapper_function_00627EB0.md) at `0x00627F14`
- [DifIoBuildAsynchronousFsdRequestWrapper](../62/DifIoBuildAsynchronousFsdRequestWrapper_function_00628030.md) at `0x00628097`
- [DifIoBuildDeviceIoControlRequestWrapper](../62/DifIoBuildDeviceIoControlRequestWrapper_function_00628200.md) at `0x00628267`
- [DifIoBuildSynchronousFsdRequestWrapper](../62/DifIoBuildSynchronousFsdRequestWrapper_function_00628400.md) at `0x00628467`
- [DifIoCheckShareAccessWrapper](../62/DifIoCheckShareAccessWrapper_function_006285E0.md) at `0x00628645`
- [DifIoConnectInterruptExWrapper](../62/DifIoConnectInterruptExWrapper_function_00628780.md) at `0x006287D7`
- [DifIoConnectInterruptWrapper](../62/DifIoConnectInterruptWrapper_function_006288F0.md) at `0x00628958`
- [DifIoCreateControllerWrapper](../62/DifIoCreateControllerWrapper_function_00628AF0.md) at `0x00628B46`
- [DifIoCreateDeviceWrapper](../62/DifIoCreateDeviceWrapper_function_00628C60.md) at `0x00628CC7`
- [DifIoCreateFileExWrapper](../62/DifIoCreateFileExWrapper_function_00628E20.md) at `0x00628E86`
- [DifIoCreateFileSpecifyDeviceObjectHintWrapper](../62/DifIoCreateFileSpecifyDeviceObjectHintWrapper_function_00629070.md) at `0x006290D6`
- [DifIoCreateFileWrapper](../62/DifIoCreateFileWrapper_function_006292C0.md) at `0x00629326`
- [DifIoCreateNotificationEventWrapper](../62/DifIoCreateNotificationEventWrapper_function_00629500.md) at `0x00629556`
- [DifIoCreateSymbolicLinkWrapper](../62/DifIoCreateSymbolicLinkWrapper_function_00629670.md) at `0x006296C6`
- [DifIoCreateSynchronizationEventWrapper](../62/DifIoCreateSynchronizationEventWrapper_function_006297E0.md) at `0x00629836`
- [DifIoCreateUnprotectedSymbolicLinkWrapper](../62/DifIoCreateUnprotectedSymbolicLinkWrapper_function_00629950.md) at `0x006299A6`
- [DifIoDeleteControllerWrapper](../62/DifIoDeleteControllerWrapper_function_00629AC0.md) at `0x00629B10`
- [DifIoDeleteDeviceWrapper](../62/DifIoDeleteDeviceWrapper_function_00629C20.md) at `0x00629C70`
- [DifIoDeleteSymbolicLinkWrapper](../62/DifIoDeleteSymbolicLinkWrapper_function_00629D80.md) at `0x00629DD7`
- [DifIoDetachDeviceWrapper](../62/DifIoDetachDeviceWrapper_function_00629EF0.md) at `0x00629F40`
- [DifIoDisconnectInterruptExWrapper](../62/DifIoDisconnectInterruptExWrapper_function_0062A050.md) at `0x0062A0A0`
- [DifIoDisconnectInterruptWrapper](../62/DifIoDisconnectInterruptWrapper_function_0062A1B0.md) at `0x0062A200`
- [DifIoFreeControllerWrapper](../62/DifIoFreeControllerWrapper_function_0062A310.md) at `0x0062A360`
- [DifIoFreeIrpWrapper](../62/DifIoFreeIrpWrapper_function_0062A470.md) at `0x0062A4C0`
- [DifIoFreeMdlWrapper](../62/DifIoFreeMdlWrapper_function_0062A5D0.md) at `0x0062A620`
- [DifIoGetConfigurationInformationWrapper](../62/DifIoGetConfigurationInformationWrapper_function_0062A730.md) at `0x0062A779`
- [DifIoGetDeviceDirectoryWrapper](../62/DifIoGetDeviceDirectoryWrapper_function_0062A880.md) at `0x0062A8E6`
- [DifIoGetDeviceObjectPointerWrapper](../62/DifIoGetDeviceObjectPointerWrapper_function_0062AA20.md) at `0x0062AA86`
- [DifIoGetDeviceToVerifyWrapper](../62/DifIoGetDeviceToVerifyWrapper_function_0062ABB0.md) at `0x0062AC07`
- [DifIoGetDmaAdapterWrapper](../62/DifIoGetDmaAdapterWrapper_function_0062AD20.md) at `0x0062AD84`
- [DifIoGetDriverDirectoryWrapper](../62/DifIoGetDriverDirectoryWrapper_function_0062AEA0.md) at `0x0062AF0A`
- [DifIoGetFileObjectGenericMappingWrapper](../62/DifIoGetFileObjectGenericMappingWrapper_function_0062B030.md) at `0x0062B079`
- [DifIoGetInitialStackWrapper](../62/DifIoGetInitialStackWrapper_function_0062B180.md) at `0x0062B1C9`
- [DifIoInitializeRemoveLockExWrapper](../62/DifIoInitializeRemoveLockExWrapper_function_0062B2D0.md) at `0x0062B330`
- [DifIoInitializeTimerWrapper](../62/DifIoInitializeTimerWrapper_function_0062B470.md) at `0x0062B4D4`
- [DifIoInitializeWorkItemWrapper](../62/DifIoInitializeWorkItemWrapper_function_0062B5F0.md) at `0x0062B649`
- [DifIoIsWdmVersionAvailableWrapper](../62/DifIoIsWdmVersionAvailableWrapper_function_0062B760.md) at `0x0062B7B2`
- [DifIoOpenDeviceInterfaceRegistryKeyWrapper](../62/DifIoOpenDeviceInterfaceRegistryKeyWrapper_function_0062B8D0.md) at `0x0062B934`
- [DifIoOpenDeviceRegistryKeyWrapper](../62/DifIoOpenDeviceRegistryKeyWrapper_function_0062BA50.md) at `0x0062BABA`
- [DifIoOpenDriverRegistryKeyWrapper](../62/DifIoOpenDriverRegistryKeyWrapper_function_0062BBE0.md) at `0x0062BC46`
- [DifIoRaiseHardErrorWrapper](../62/DifIoRaiseHardErrorWrapper_function_0062BD80.md) at `0x0062BDDE`
- [DifIoRaiseInformationalHardErrorWrapper](../62/DifIoRaiseInformationalHardErrorWrapper_function_0062BF00.md) at `0x0062BF5E`
- [DifIoReadPartitionTableWrapper](../62/DifIoReadPartitionTableWrapper_function_0062C080.md) at `0x0062C0EA`
- [DifIoRegisterDeviceInterfaceWrapper](../62/DifIoRegisterDeviceInterfaceWrapper_function_0062C210.md) at `0x0062C276`
- [DifIoRegisterDriverReinitializationWrapper](../62/DifIoRegisterDriverReinitializationWrapper_function_0062C3A0.md) at `0x0062C3FE`
- [DifIoRegisterShutdownNotificationWrapper](../62/DifIoRegisterShutdownNotificationWrapper_function_0062C520.md) at `0x0062C577`
- [DifIoReleaseRemoveLockAndWaitExWrapper](../62/DifIoReleaseRemoveLockAndWaitExWrapper_function_0062C690.md) at `0x0062C6EE`
- [DifIoReleaseRemoveLockExWrapper](../62/DifIoReleaseRemoveLockExWrapper_function_0062C810.md) at `0x0062C86E`
- [DifIoRemoveShareAccessWrapper](../62/DifIoRemoveShareAccessWrapper_function_0062C990.md) at `0x0062C9E9`
- [DifIoSetCompletionRoutineExWrapper](../62/DifIoSetCompletionRoutineExWrapper_function_0062CB00.md) at `0x0062CB6D`
- [DifIoSetDeviceInterfaceStateWrapper](../62/DifIoSetDeviceInterfaceStateWrapper_function_0062CCC0.md) at `0x0062CD16`
- [DifIoSetDeviceToVerifyWrapper](../62/DifIoSetDeviceToVerifyWrapper_function_0062CE30.md) at `0x0062CE89`
- [DifIoSetPartitionInformationWrapper](../62/DifIoSetPartitionInformationWrapper_function_0062CFA0.md) at `0x0062D00A`
- [DifIoSetShareAccessWrapper](../62/DifIoSetShareAccessWrapper_function_0062D130.md) at `0x0062D190`
- [DifIoStartNextPacketWrapper](../62/DifIoStartNextPacketWrapper_function_0062D2C0.md) at `0x0062D319`
- [DifIoUnregisterShutdownNotificationWrapper](../62/DifIoUnregisterShutdownNotificationWrapper_function_0062D430.md) at `0x0062D480`
- [DifIoUpdateShareAccessWrapper](../62/DifIoUpdateShareAccessWrapper_function_0062D590.md) at `0x0062D5E9`
- [DifIoWMIAllocateInstanceIdsWrapper](../62/DifIoWMIAllocateInstanceIdsWrapper_function_0062D700.md) at `0x0062D764`
- [DifIoWMIRegistrationControlWrapper](../62/DifIoWMIRegistrationControlWrapper_function_0062D880.md) at `0x0062D8D6`
- [DifIoWriteErrorLogEntryWrapper](../62/DifIoWriteErrorLogEntryWrapper_function_0062D9F0.md) at `0x0062DA40`
- [DifIoWritePartitionTableWrapper](../62/DifIoWritePartitionTableWrapper_function_0062DB50.md) at `0x0062DBB6`
- [DifIofCallDriverWrapper](../62/DifIofCallDriverWrapper_function_0062DCF0.md) at `0x0062DD5A`
- [DifIofCompleteRequestWrapper](../62/DifIofCompleteRequestWrapper_function_0062DE80.md) at `0x0062DED9`
- [DifKeAcquireGuardedMutexUnsafeWrapper](../62/DifKeAcquireGuardedMutexUnsafeWrapper_function_0062DFF0.md) at `0x0062E040`
- [DifKeAcquireGuardedMutexWrapper](../62/DifKeAcquireGuardedMutexWrapper_function_0062E150.md) at `0x0062E1A0`
- [DifKeAcquireInStackQueuedSpinLockAtDpcLevelWrapper](../62/DifKeAcquireInStackQueuedSpinLockAtDpcLevelWrapper_function_0062E2B0.md) at `0x0062E309`
- [DifKeAcquireInStackQueuedSpinLockForDpcWrapper](../62/DifKeAcquireInStackQueuedSpinLockForDpcWrapper_function_0062E420.md) at `0x0062E479`
- [DifKeAcquireInStackQueuedSpinLockRaiseToSynchWrapper](../62/DifKeAcquireInStackQueuedSpinLockRaiseToSynchWrapper_function_0062E590.md) at `0x0062E5E9`
- [DifKeAcquireInStackQueuedSpinLockWrapper](../62/DifKeAcquireInStackQueuedSpinLockWrapper_function_0062E700.md) at `0x0062E759`
- [DifKeAcquireQueuedSpinLockRaiseToSynchWrapper](../62/DifKeAcquireQueuedSpinLockRaiseToSynchWrapper_function_0062E870.md) at `0x0062E8C7`
- [DifKeAcquireQueuedSpinLockWrapper](../62/DifKeAcquireQueuedSpinLockWrapper_function_0062E9E0.md) at `0x0062EA37`
- [DifKeAcquireSpinLockAtDpcLevelWrapper](../62/DifKeAcquireSpinLockAtDpcLevelWrapper_function_0062EB50.md) at `0x0062EBA0`
- [DifKeAcquireSpinLockRaiseToDpcWrapper](../62/DifKeAcquireSpinLockRaiseToDpcWrapper_function_0062ECB0.md) at `0x0062ED07`
- [DifKeCancelTimerWrapper](../62/DifKeCancelTimerWrapper_function_0062EE20.md) at `0x0062EE77`
- [DifKeClearEventWrapper](../62/DifKeClearEventWrapper_function_0062EF90.md) at `0x0062EFE0`
- [DifKeDelayExecutionThreadWrapper](../62/DifKeDelayExecutionThreadWrapper_function_0062F0F0.md) at `0x0062F151`
- [DifKeDeregisterNmiCallbackWrapper](../62/DifKeDeregisterNmiCallbackWrapper_function_0062F280.md) at `0x0062F2D7`
- [DifKeEnterCriticalRegionWrapper](../62/DifKeEnterCriticalRegionWrapper_function_0062F3F0.md) at `0x0062F437`
- [DifKeEnterGuardedRegionWrapper](../62/DifKeEnterGuardedRegionWrapper_function_0062F540.md) at `0x0062F587`
- [DifKeInitializeDeviceQueueWrapper](../62/DifKeInitializeDeviceQueueWrapper_function_0062F690.md) at `0x0062F6E0`
- [DifKeInitializeEventWrapper](../62/DifKeInitializeEventWrapper_function_0062F800.md) at `0x0062F862`
- [DifKeInitializeMutantWrapper](../62/DifKeInitializeMutantWrapper_function_0062F990.md) at `0x0062F9E9`
- [DifKeInitializeMutexWrapper](../62/DifKeInitializeMutexWrapper_function_0062FB00.md) at `0x0062FB59`
- [DifKeInitializeSemaphoreWrapper](../62/DifKeInitializeSemaphoreWrapper_function_0062FC70.md) at `0x0062FCD1`
- [DifKeInitializeTimerExWrapper](../62/DifKeInitializeTimerExWrapper_function_0062FE00.md) at `0x0062FE61`
- [DifKeInitializeTimerWrapper](../62/DifKeInitializeTimerWrapper_function_0062FF90.md) at `0x0062FFE2`
- [DifKeInsertByKeyDeviceQueueWrapper](../63/DifKeInsertByKeyDeviceQueueWrapper_function_00630100.md) at `0x00630164`
- [DifKeInsertDeviceQueueWrapper](../63/DifKeInsertDeviceQueueWrapper_function_00630280.md) at `0x006302D6`
- [DifKeInsertQueueDpcWrapper](../63/DifKeInsertQueueDpcWrapper_function_006303F0.md) at `0x00630454`
- [DifKeLeaveCriticalRegionWrapper](../63/DifKeLeaveCriticalRegionWrapper_function_00630570.md) at `0x006305B7`
- [DifKeLeaveGuardedRegionWrapper](../63/DifKeLeaveGuardedRegionWrapper_function_006306C0.md) at `0x00630707`
- [DifKeLowerIrqlWrapper](../63/DifKeLowerIrqlWrapper_function_00630810.md) at `0x00630860`
- [DifKePulseEventWrapper](../63/DifKePulseEventWrapper_function_00630980.md) at `0x006309DE`
- [DifKeRaiseIrqlToDpcLevelWrapper](../63/DifKeRaiseIrqlToDpcLevelWrapper_function_00630B00.md) at `0x00630B49`
- [DifKeReadStateEventWrapper](../63/DifKeReadStateEventWrapper_function_00630C70.md) at `0x00630CC7`
- [DifKeReadStateTimerWrapper](../63/DifKeReadStateTimerWrapper_function_00630DD0.md) at `0x00630E27`
- [DifKeRegisterNmiCallbackWrapper](../63/DifKeRegisterNmiCallbackWrapper_function_00630F30.md) at `0x00630F86`
- [DifKeReleaseGuardedMutexUnsafeWrapper](../63/DifKeReleaseGuardedMutexUnsafeWrapper_function_006310F0.md) at `0x00631140`
- [DifKeReleaseGuardedMutexWrapper](../63/DifKeReleaseGuardedMutexWrapper_function_00631250.md) at `0x006312A0`
- [DifKeReleaseInStackQueuedSpinLockForDpcWrapper](../63/DifKeReleaseInStackQueuedSpinLockForDpcWrapper_function_006313B0.md) at `0x00631400`
- [DifKeReleaseInStackQueuedSpinLockFromDpcLevelWrapper](../63/DifKeReleaseInStackQueuedSpinLockFromDpcLevelWrapper_function_00631510.md) at `0x00631560`
- [DifKeReleaseInStackQueuedSpinLockWrapper](../63/DifKeReleaseInStackQueuedSpinLockWrapper_function_00631670.md) at `0x006316C0`
- [DifKeReleaseMutantWrapper](../63/DifKeReleaseMutantWrapper_function_006317D0.md) at `0x00631832`
- [DifKeReleaseMutexWrapper](../63/DifKeReleaseMutexWrapper_function_00631960.md) at `0x006319B6`
- [DifKeReleaseQueuedSpinLockWrapper](../63/DifKeReleaseQueuedSpinLockWrapper_function_00631AE0.md) at `0x00631B39`
- [DifKeReleaseSpinLockFromDpcLevelWrapper](../63/DifKeReleaseSpinLockFromDpcLevelWrapper_function_00631C50.md) at `0x00631CA0`
- [DifKeReleaseSpinLockWrapper](../63/DifKeReleaseSpinLockWrapper_function_00631DB0.md) at `0x00631E09`
- [DifKeRemoveByKeyDeviceQueueWrapper](../63/DifKeRemoveByKeyDeviceQueueWrapper_function_00631F20.md) at `0x00631F76`
- [DifKeRemoveDeviceQueueWrapper](../63/DifKeRemoveDeviceQueueWrapper_function_00632090.md) at `0x006320E7`
- [DifKeRemoveEntryDeviceQueueWrapper](../63/DifKeRemoveEntryDeviceQueueWrapper_function_00632200.md) at `0x00632256`
- [DifKeRemoveQueueDpcWrapper](../63/DifKeRemoveQueueDpcWrapper_function_00632370.md) at `0x006323C7`
- [DifKeResetEventWrapper](../63/DifKeResetEventWrapper_function_006324E0.md) at `0x00632537`
- [DifKeRestoreExtendedProcessorStateWrapper](../63/DifKeRestoreExtendedProcessorStateWrapper_function_00632650.md) at `0x006326A0`
- [DifKeSaveExtendedProcessorStateWrapper](../63/DifKeSaveExtendedProcessorStateWrapper_function_006327B0.md) at `0x00632806`
- [DifKeSetEventWrapper](../63/DifKeSetEventWrapper_function_00632920.md) at `0x0063297E`
- [DifKeSetTimerExWrapper](../63/DifKeSetTimerExWrapper_function_00632AA0.md) at `0x00632B06`
- [DifKeSetTimerWrapper](../63/DifKeSetTimerWrapper_function_00632C30.md) at `0x00632C94`
- [DifKeSynchronizeExecutionWrapper](../63/DifKeSynchronizeExecutionWrapper_function_00632DC0.md) at `0x00632E24`
- [DifKeTryToAcquireGuardedMutexWrapper](../63/DifKeTryToAcquireGuardedMutexWrapper_function_00632F40.md) at `0x00632F97`
- [DifKeTryToAcquireQueuedSpinLockRaiseToSynchWrapper](../63/DifKeTryToAcquireQueuedSpinLockRaiseToSynchWrapper_function_006330B0.md) at `0x00633106`
- [DifKeTryToAcquireQueuedSpinLockWrapper](../63/DifKeTryToAcquireQueuedSpinLockWrapper_function_00633220.md) at `0x00633276`
- [DifKeTryToAcquireSpinLockAtDpcLevelWrapper](../63/DifKeTryToAcquireSpinLockAtDpcLevelWrapper_function_00633390.md) at `0x006333E7`
- [DifKeWaitForMultipleObjectsWrapper](../63/DifKeWaitForMultipleObjectsWrapper_function_00633500.md) at `0x0063356C`
- [DifKeWaitForSingleObjectWrapper](../63/DifKeWaitForSingleObjectWrapper_function_006336D0.md) at `0x0063373A`
- [DifKfRaiseIrqlWrapper](../63/DifKfRaiseIrqlWrapper_function_00633870.md) at `0x006338C0`
- [DifMmAllocateContiguousMemoryExWrapper](../63/DifMmAllocateContiguousMemoryExWrapper_function_006339F0.md) at `0x00633A58`
- [DifMmAllocateContiguousMemorySpecifyCacheNodeWrapper](../63/DifMmAllocateContiguousMemorySpecifyCacheNodeWrapper_function_00633BE0.md) at `0x00633C4E`
- [DifMmAllocateContiguousMemorySpecifyCacheWrapper](../63/DifMmAllocateContiguousMemorySpecifyCacheWrapper_function_00633D90.md) at `0x00633DFE`
- [DifMmAllocateContiguousMemoryWrapper](../63/DifMmAllocateContiguousMemoryWrapper_function_00633F40.md) at `0x00633F96`
- [DifMmAllocateContiguousNodeMemoryWrapper](../63/DifMmAllocateContiguousNodeMemoryWrapper_function_006340B0.md) at `0x0063411E`
- [DifMmAllocateMappingAddressExWrapper](../63/DifMmAllocateMappingAddressExWrapper_function_00634260.md) at `0x006342BE`
- [DifMmAllocateMappingAddressWrapper](../63/DifMmAllocateMappingAddressWrapper_function_006343F0.md) at `0x00634446`
- [DifMmAllocateNodePagesForMdlExWrapper](../63/DifMmAllocateNodePagesForMdlExWrapper_function_00634560.md) at `0x006345C7`
- [DifMmAllocateNonCachedMemoryWrapper](../63/DifMmAllocateNonCachedMemoryWrapper_function_00634720.md) at `0x00634777`
- [DifMmAllocatePagesForMdlExWrapper](../63/DifMmAllocatePagesForMdlExWrapper_function_00634890.md) at `0x006348FE`
- [DifMmAllocatePagesForMdlWrapper](../63/DifMmAllocatePagesForMdlWrapper_function_00634A40.md) at `0x00634AA6`
- [DifMmBuildMdlForNonPagedPoolWrapper](../63/DifMmBuildMdlForNonPagedPoolWrapper_function_00634BD0.md) at `0x00634C20`
- [DifMmCreateMdlWrapper](../63/DifMmCreateMdlWrapper_function_00634D30.md) at `0x00634D94`
- [DifMmCreateSectionWrapper](../63/DifMmCreateSectionWrapper_function_00634EB0.md) at `0x00634F18`
- [DifMmFreeContiguousMemorySpecifyCacheWrapper](../63/DifMmFreeContiguousMemorySpecifyCacheWrapper_function_00635080.md) at `0x006350DA`
- [DifMmFreeContiguousMemoryWrapper](../63/DifMmFreeContiguousMemoryWrapper_function_006351F0.md) at `0x00635240`
- [DifMmFreeMappingAddressWrapper](../63/DifMmFreeMappingAddressWrapper_function_00635350.md) at `0x006353A9`
- [DifMmFreeNonCachedMemoryWrapper](../63/DifMmFreeNonCachedMemoryWrapper_function_006354C0.md) at `0x00635519`
- [DifMmFreePagesFromMdlWrapper](../63/DifMmFreePagesFromMdlWrapper_function_00635630.md) at `0x00635680`
- [DifMmLockPagableDataSectionWrapper](../63/DifMmLockPagableDataSectionWrapper_function_00635790.md) at `0x006357E7`
- [DifMmLockPagableSectionByHandleWrapper](../63/DifMmLockPagableSectionByHandleWrapper_function_00635900.md) at `0x00635950`
- [DifMmMapIoSpaceExWrapper](../63/DifMmMapIoSpaceExWrapper_function_00635A60.md) at `0x00635AC4`
- [DifMmMapIoSpaceWrapper](../63/DifMmMapIoSpaceWrapper_function_00635BE0.md) at `0x00635C44`
- [DifMmMapLockedPagesSpecifyCacheWrapper](../63/DifMmMapLockedPagesSpecifyCacheWrapper_function_00635D60.md) at `0x00635DC8`
- [DifMmMapLockedPagesWrapper](../63/DifMmMapLockedPagesWrapper_function_00635F10.md) at `0x00635F66`
- [DifMmMapViewOfSectionWrapper](../63/DifMmMapViewOfSectionWrapper_function_006360A0.md) at `0x00636108`
- [DifMmPageEntireDriverWrapper](../63/DifMmPageEntireDriverWrapper_function_00636290.md) at `0x006362E7`
- [DifMmProbeAndLockPagesWrapper](../63/DifMmProbeAndLockPagesWrapper_function_00636400.md) at `0x00636461`
- [DifMmProbeAndLockProcessPagesWrapper](../63/DifMmProbeAndLockProcessPagesWrapper_function_00636580.md) at `0x006365E0`
- [DifMmProtectMdlSystemAddressWrapper](../63/DifMmProtectMdlSystemAddressWrapper_function_00636710.md) at `0x00636766`
- [DifMmResetDriverPagingWrapper](../63/DifMmResetDriverPagingWrapper_function_00636880.md) at `0x006368D0`
- [DifMmSecureVirtualMemoryWrapper](../63/DifMmSecureVirtualMemoryWrapper_function_006369E0.md) at `0x00636A44`
- [DifMmUnlockPagableImageSectionWrapper](../63/DifMmUnlockPagableImageSectionWrapper_function_00636B60.md) at `0x00636BB0`
- [DifMmUnlockPagesWrapper](../63/DifMmUnlockPagesWrapper_function_00636CC0.md) at `0x00636D10`
- [DifMmUnmapIoSpaceWrapper](../63/DifMmUnmapIoSpaceWrapper_function_00636E20.md) at `0x00636E79`
- [DifMmUnmapLockedPagesWrapper](../63/DifMmUnmapLockedPagesWrapper_function_00636F90.md) at `0x00636FE9`
- [DifMmUnsecureVirtualMemoryWrapper](../63/DifMmUnsecureVirtualMemoryWrapper_function_00637100.md) at `0x00637150`
- [DifNtCreateFileWrapper](../63/DifNtCreateFileWrapper_function_00637260.md) at `0x006372C8`
- [DifNtCreateSectionWrapper](../63/DifNtCreateSectionWrapper_function_00637460.md) at `0x006374C7`
- [DifNtDeleteFileWrapper](../63/DifNtDeleteFileWrapper_function_00637620.md) at `0x00637677`
- [DifNtMapViewOfSectionWrapper](../63/DifNtMapViewOfSectionWrapper_function_00637790.md) at `0x006377F8`
- [DifNtOpenFileWrapper](../63/DifNtOpenFileWrapper_function_00637980.md) at `0x006379EE`
- [DifNtSetInformationFileWrapper](../63/DifNtSetInformationFileWrapper_function_00637B30.md) at `0x00637B96`
- [DifNtWriteFileWrapper](../63/DifNtWriteFileWrapper_function_00637CD0.md) at `0x00637D38`
- [DifObGetObjectSecurityWrapper](../63/DifObGetObjectSecurityWrapper_function_00637EC0.md) at `0x00637F24`
- [DifObReferenceObjectByHandleWrapper](../63/DifObReferenceObjectByHandleWrapper_function_00638040.md) at `0x006380AB`
- [DifObReferenceObjectByPointerWithTagWrapper](../63/DifObReferenceObjectByPointerWithTagWrapper_function_00638210.md) at `0x00638276`
- [DifObReferenceObjectByPointerWrapper](../63/DifObReferenceObjectByPointerWrapper_function_006383B0.md) at `0x00638416`
- [DifObReleaseObjectSecurityWrapper](../63/DifObReleaseObjectSecurityWrapper_function_00638550.md) at `0x006385A9`
- [DifObfDereferenceObjectWithTagWrapper](../63/DifObfDereferenceObjectWithTagWrapper_function_006386C0.md) at `0x00638716`
- [DifObfDereferenceObjectWrapper](../63/DifObfDereferenceObjectWrapper_function_00638830.md) at `0x00638887`
- [DifObfReferenceObjectWithTagWrapper](../63/DifObfReferenceObjectWithTagWrapper_function_006389A0.md) at `0x006389F6`
- [DifObfReferenceObjectWrapper](../63/DifObfReferenceObjectWrapper_function_00638B10.md) at `0x00638B67`
- [DifPoCallDriverWrapper](../63/DifPoCallDriverWrapper_function_00638C80.md) at `0x00638CEA`
- [DifPoFxActivateComponentWrapper](../63/DifPoFxActivateComponentWrapper_function_00638E10.md) at `0x00638E71`
- [DifPoFxCompleteDevicePowerNotRequiredWrapper](../63/DifPoFxCompleteDevicePowerNotRequiredWrapper_function_00638F90.md) at `0x00638FE0`
- [DifPoFxCompleteIdleConditionWrapper](../63/DifPoFxCompleteIdleConditionWrapper_function_006390F0.md) at `0x00639149`
- [DifPoFxCompleteIdleStateWrapper](../63/DifPoFxCompleteIdleStateWrapper_function_00639260.md) at `0x006392B9`
- [DifPoFxIdleComponentWrapper](../63/DifPoFxIdleComponentWrapper_function_006393D0.md) at `0x00639431`
- [DifPoFxNotifySurprisePowerOnWrapper](../63/DifPoFxNotifySurprisePowerOnWrapper_function_00639550.md) at `0x006395A0`
- [DifPoFxPowerControlWrapper](../63/DifPoFxPowerControlWrapper_function_006396B0.md) at `0x00639718`
- [DifPoFxRegisterDeviceWrapper](../63/DifPoFxRegisterDeviceWrapper_function_00639880.md) at `0x006398E4`
- [DifPoFxReportDevicePoweredOnWrapper](../63/DifPoFxReportDevicePoweredOnWrapper_function_00639A00.md) at `0x00639A50`
- [DifPoFxSetComponentLatencyWrapper](../63/DifPoFxSetComponentLatencyWrapper_function_00639B60.md) at `0x00639BBE`
- [DifPoFxSetComponentResidencyWrapper](../63/DifPoFxSetComponentResidencyWrapper_function_00639CE0.md) at `0x00639D3E`
- [DifPoFxSetComponentWakeWrapper](../63/DifPoFxSetComponentWakeWrapper_function_00639E60.md) at `0x00639EC1`
- [DifPoFxSetDeviceIdleTimeoutWrapper](../63/DifPoFxSetDeviceIdleTimeoutWrapper_function_00639FE0.md) at `0x0063A039`
- [DifPoFxStartDevicePowerManagementWrapper](../63/DifPoFxStartDevicePowerManagementWrapper_function_0063A150.md) at `0x0063A1A0`
- [DifPoFxUnregisterDeviceWrapper](../63/DifPoFxUnregisterDeviceWrapper_function_0063A2B0.md) at `0x0063A300`
- [DifPoRequestPowerIrpWrapper](../63/DifPoRequestPowerIrpWrapper_function_0063A410.md) at `0x0063A481`
- [DifProbeForReadWrapper](../63/DifProbeForReadWrapper_function_0063A5D0.md) at `0x0063A62E`
- [DifProbeForWriteWrapper](../63/DifProbeForWriteWrapper_function_0063A770.md) at `0x0063A7CE`
- [DifPsCreateSystemThreadWrapper](../63/DifPsCreateSystemThreadWrapper_function_0063A8F0.md) at `0x0063A958`
- [DifPsGetVersionWrapper](../63/DifPsGetVersionWrapper_function_0063AAC0.md) at `0x0063AB26`
- [DifPsSetCreateProcessNotifyRoutineWrapper](../63/DifPsSetCreateProcessNotifyRoutineWrapper_function_0063AC50.md) at `0x0063ACA6`
- [DifPsSetCreateThreadNotifyRoutineWrapper](../63/DifPsSetCreateThreadNotifyRoutineWrapper_function_0063ADC0.md) at `0x0063AE17`
- [DifPsSetLoadImageNotifyRoutineWrapper](../63/DifPsSetLoadImageNotifyRoutineWrapper_function_0063AF30.md) at `0x0063AF87`
- [DifPsTerminateSystemThreadWrapper](../63/DifPsTerminateSystemThreadWrapper_function_0063B0A0.md) at `0x0063B0EF`
- [DifRtlAnsiStringToUnicodeStringWrapper](../63/DifRtlAnsiStringToUnicodeStringWrapper_function_0063B200.md) at `0x0063B264`
- [DifRtlCheckRegistryKeyWrapper](../63/DifRtlCheckRegistryKeyWrapper_function_0063B380.md) at `0x0063B3D9`
- [DifRtlCreateRegistryKeyWrapper](../63/DifRtlCreateRegistryKeyWrapper_function_0063B4F0.md) at `0x0063B549`
- [DifRtlCreateSystemVolumeInformationFolderWrapper](../63/DifRtlCreateSystemVolumeInformationFolderWrapper_function_0063B660.md) at `0x0063B6B7`
- [DifRtlCreateUnicodeStringWrapper](../63/DifRtlCreateUnicodeStringWrapper_function_0063B7D0.md) at `0x0063B826`
- [DifRtlDeleteRegistryValueWrapper](../63/DifRtlDeleteRegistryValueWrapper_function_0063B940.md) at `0x0063B99E`
- [DifRtlDowncaseUnicodeStringWrapper](../63/DifRtlDowncaseUnicodeStringWrapper_function_0063BAC0.md) at `0x0063BB24`
- [DifRtlDuplicateUnicodeStringWrapper](../63/DifRtlDuplicateUnicodeStringWrapper_function_0063BC40.md) at `0x0063BC9E`
- [DifRtlOemStringToCountedUnicodeStringWrapper](../63/DifRtlOemStringToCountedUnicodeStringWrapper_function_0063BDC0.md) at `0x0063BE24`
- [DifRtlOemStringToUnicodeStringWrapper](../63/DifRtlOemStringToUnicodeStringWrapper_function_0063BF40.md) at `0x0063BFA4`
- [DifRtlQueryRegistryValueWithFallbackWrapper](../63/DifRtlQueryRegistryValueWithFallbackWrapper_function_0063C0C0.md) at `0x0063C128`
- [DifRtlQueryRegistryValuesExWrapper](../63/DifRtlQueryRegistryValuesExWrapper_function_0063C290.md) at `0x0063C2F5`
- [DifRtlQueryRegistryValuesWrapper](../63/DifRtlQueryRegistryValuesWrapper_function_0063C430.md) at `0x0063C495`
- [DifRtlUnicodeStringToAnsiStringWrapper](../63/DifRtlUnicodeStringToAnsiStringWrapper_function_0063C5D0.md) at `0x0063C634`
- [DifRtlUnicodeStringToCountedOemStringWrapper](../63/DifRtlUnicodeStringToCountedOemStringWrapper_function_0063C750.md) at `0x0063C7B4`
- [DifRtlUnicodeStringToOemStringWrapper](../63/DifRtlUnicodeStringToOemStringWrapper_function_0063C8D0.md) at `0x0063C934`
- [DifRtlUpcaseUnicodeStringToAnsiStringWrapper](../63/DifRtlUpcaseUnicodeStringToAnsiStringWrapper_function_0063CA50.md) at `0x0063CAB4`
- [DifRtlUpcaseUnicodeStringToCountedOemStringWrapper](../63/DifRtlUpcaseUnicodeStringToCountedOemStringWrapper_function_0063CBD0.md) at `0x0063CC34`
- [DifRtlUpcaseUnicodeStringToOemStringWrapper](../63/DifRtlUpcaseUnicodeStringToOemStringWrapper_function_0063CD50.md) at `0x0063CDB4`
- [DifRtlUpcaseUnicodeStringWrapper](../63/DifRtlUpcaseUnicodeStringWrapper_function_0063CED0.md) at `0x0063CF34`
- [DifRtlWriteRegistryValueWrapper](../63/DifRtlWriteRegistryValueWrapper_function_0063D050.md) at `0x0063D0BD`
- [DifZwAccessCheckAndAuditAlarmWrapper](../63/DifZwAccessCheckAndAuditAlarmWrapper_function_0063D200.md) at `0x0063D268`
- [DifZwAddBootEntryWrapper](../63/DifZwAddBootEntryWrapper_function_0063D410.md) at `0x0063D466`
- [DifZwAddDriverEntryWrapper](../63/DifZwAddDriverEntryWrapper_function_0063D580.md) at `0x0063D5D6`
- [DifZwAdjustPrivilegesTokenWrapper](../63/DifZwAdjustPrivilegesTokenWrapper_function_0063D6F0.md) at `0x0063D758`
- [DifZwAllocateVirtualMemoryWrapper](../63/DifZwAllocateVirtualMemoryWrapper_function_0063D8A0.md) at `0x0063D90E`
- [DifZwAlpcAcceptConnectPortWrapper](../63/DifZwAlpcAcceptConnectPortWrapper_function_0063DA50.md) at `0x0063DAB8`
- [DifZwAlpcConnectPortWrapper](../63/DifZwAlpcConnectPortWrapper_function_0063DC40.md) at `0x0063DCA8`
- [DifZwAlpcCreatePortSectionWrapper](../63/DifZwAlpcCreatePortSectionWrapper_function_0063DE50.md) at `0x0063DEB8`
- [DifZwAlpcCreatePortWrapper](../63/DifZwAlpcCreatePortWrapper_function_0063E000.md) at `0x0063E064`
- [DifZwAlpcCreateResourceReserveWrapper](../63/DifZwAlpcCreateResourceReserveWrapper_function_0063E180.md) at `0x0063E1E6`
- [DifZwAlpcCreateSectionViewWrapper](../63/DifZwAlpcCreateSectionViewWrapper_function_0063E310.md) at `0x0063E374`
- [DifZwAlpcCreateSecurityContextWrapper](../63/DifZwAlpcCreateSecurityContextWrapper_function_0063E490.md) at `0x0063E4F4`
- [DifZwAlpcQueryInformationWrapper](../63/DifZwAlpcQueryInformationWrapper_function_0063E610.md) at `0x0063E67E`
- [DifZwAlpcSendWaitReceivePortWrapper](../63/DifZwAlpcSendWaitReceivePortWrapper_function_0063E7C0.md) at `0x0063E828`
- [DifZwAlpcSetInformationWrapper](../63/DifZwAlpcSetInformationWrapper_function_0063E9A0.md) at `0x0063EA06`
- [DifZwCancelIoFileWrapper](../63/DifZwCancelIoFileWrapper_function_0063EB30.md) at `0x0063EB86`
- [DifZwCancelTimerWrapper](../63/DifZwCancelTimerWrapper_function_0063ECA0.md) at `0x0063ECF6`
- [DifZwCloseObjectAuditAlarmWrapper](../63/DifZwCloseObjectAuditAlarmWrapper_function_0063EE10.md) at `0x0063EE74`
- [DifZwCloseWrapper](../63/DifZwCloseWrapper_function_0063EF90.md) at `0x0063EFE7`
- [DifZwCommitEnlistmentWrapper](../63/DifZwCommitEnlistmentWrapper_function_0063F100.md) at `0x0063F156`
- [DifZwConnectPortWrapper](../63/DifZwConnectPortWrapper_function_0063F270.md) at `0x0063F2D8`
- [DifZwCreateDirectoryObjectWrapper](../63/DifZwCreateDirectoryObjectWrapper_function_0063F450.md) at `0x0063F4B2`
- [DifZwCreateEnlistmentWrapper](../63/DifZwCreateEnlistmentWrapper_function_0063F5D0.md) at `0x0063F638`
- [DifZwCreateEventWrapper](../63/DifZwCreateEventWrapper_function_0063F7A0.md) at `0x0063F806`
- [DifZwCreateFileWrapper](../63/DifZwCreateFileWrapper_function_0063F940.md) at `0x0063F9A8`
- [DifZwCreateJobObjectWrapper](../63/DifZwCreateJobObjectWrapper_function_0063FB40.md) at `0x0063FBA2`
- [DifZwCreateKeyTransactedWrapper](../63/DifZwCreateKeyTransactedWrapper_function_0063FCC0.md) at `0x0063FD28`
- [DifZwCreateKeyWrapper](../63/DifZwCreateKeyWrapper_function_0063FE90.md) at `0x0063FEF8`
- [DifZwCreateResourceManagerWrapper](../64/DifZwCreateResourceManagerWrapper_function_00640050.md) at `0x006400B8`
- [DifZwCreateSectionWrapper](../64/DifZwCreateSectionWrapper_function_00640210.md) at `0x00640277`
- [DifZwCreateSymbolicLinkObjectWrapper](../64/DifZwCreateSymbolicLinkObjectWrapper_function_006403D0.md) at `0x00640436`
- [DifZwCreateTimerWrapper](../64/DifZwCreateTimerWrapper_function_00640560.md) at `0x006405C6`
- [DifZwCreateTransactionManagerWrapper](../64/DifZwCreateTransactionManagerWrapper_function_006406F0.md) at `0x0064075C`
- [DifZwCreateTransactionWrapper](../64/DifZwCreateTransactionWrapper_function_006408A0.md) at `0x00640908`
- [DifZwDeleteBootEntryWrapper](../64/DifZwDeleteBootEntryWrapper_function_00640A90.md) at `0x00640ADF`
- [DifZwDeleteFileWrapper](../64/DifZwDeleteFileWrapper_function_00640BF0.md) at `0x00640C45`
- [DifZwDeleteKeyWrapper](../64/DifZwDeleteKeyWrapper_function_00640D60.md) at `0x00640DB5`
- [DifZwDeleteValueKeyWrapper](../64/DifZwDeleteValueKeyWrapper_function_00640ED0.md) at `0x00640F26`
- [DifZwDeviceIoControlFileWrapper](../64/DifZwDeviceIoControlFileWrapper_function_00641040.md) at `0x006410A8`
- [DifZwDisplayStringWrapper](../64/DifZwDisplayStringWrapper_function_00641230.md) at `0x00641285`
- [DifZwDuplicateObjectWrapper](../64/DifZwDuplicateObjectWrapper_function_006413A0.md) at `0x00641407`
- [DifZwDuplicateTokenWrapper](../64/DifZwDuplicateTokenWrapper_function_00641560.md) at `0x006415CC`
- [DifZwEnumerateBootEntriesWrapper](../64/DifZwEnumerateBootEntriesWrapper_function_00641710.md) at `0x00641766`
- [DifZwEnumerateDriverEntriesWrapper](../64/DifZwEnumerateDriverEntriesWrapper_function_00641880.md) at `0x006418D6`
- [DifZwEnumerateKeyWrapper](../64/DifZwEnumerateKeyWrapper_function_006419F0.md) at `0x00641A5C`
- [DifZwEnumerateValueKeyWrapper](../64/DifZwEnumerateValueKeyWrapper_function_00641BA0.md) at `0x00641C0C`
- [DifZwFlushBuffersFileExWrapper](../64/DifZwFlushBuffersFileExWrapper_function_00641D50.md) at `0x00641DBC`
- [DifZwFlushBuffersFileWrapper](../64/DifZwFlushBuffersFileWrapper_function_00641F00.md) at `0x00641F56`
- [DifZwFlushInstructionCacheWrapper](../64/DifZwFlushInstructionCacheWrapper_function_00642070.md) at `0x006420D2`
- [DifZwFlushKeyWrapper](../64/DifZwFlushKeyWrapper_function_006421F0.md) at `0x00642245`
- [DifZwFlushVirtualMemoryWrapper](../64/DifZwFlushVirtualMemoryWrapper_function_00642360.md) at `0x006423C6`
- [DifZwFreeVirtualMemoryWrapper](../64/DifZwFreeVirtualMemoryWrapper_function_006424F0.md) at `0x00642556`
- [DifZwFsControlFileWrapper](../64/DifZwFsControlFileWrapper_function_00642680.md) at `0x006426E9`
- [DifZwGetNotificationResourceManagerWrapper](../64/DifZwGetNotificationResourceManagerWrapper_function_00642870.md) at `0x006428D8`
- [DifZwLoadDriverWrapper](../64/DifZwLoadDriverWrapper_function_00642A30.md) at `0x00642A85`
- [DifZwLoadKeyWrapper](../64/DifZwLoadKeyWrapper_function_00642BA0.md) at `0x00642BF6`
- [DifZwMapViewOfSectionWrapper](../64/DifZwMapViewOfSectionWrapper_function_00642D10.md) at `0x00642D78`
- [DifZwModifyBootEntryWrapper](../64/DifZwModifyBootEntryWrapper_function_00642F00.md) at `0x00642F55`
- [DifZwModifyDriverEntryWrapper](../64/DifZwModifyDriverEntryWrapper_function_00643070.md) at `0x006430C5`
- [DifZwNotifyChangeKeyWrapper](../64/DifZwNotifyChangeKeyWrapper_function_006431E0.md) at `0x00643248`
- [DifZwOpenDirectoryObjectWrapper](../64/DifZwOpenDirectoryObjectWrapper_function_006433D0.md) at `0x00643432`
- [DifZwOpenEnlistmentWrapper](../64/DifZwOpenEnlistmentWrapper_function_00643550.md) at `0x006435BC`
- [DifZwOpenEventWrapper](../64/DifZwOpenEventWrapper_function_00643700.md) at `0x00643762`
- [DifZwOpenFileWrapper](../64/DifZwOpenFileWrapper_function_00643880.md) at `0x006438EC`
- [DifZwOpenJobObjectWrapper](../64/DifZwOpenJobObjectWrapper_function_00643A30.md) at `0x00643A92`
- [DifZwOpenKeyExWrapper](../64/DifZwOpenKeyExWrapper_function_00643BB0.md) at `0x00643C16`
- [DifZwOpenKeyTransactedExWrapper](../64/DifZwOpenKeyTransactedExWrapper_function_00643D40.md) at `0x00643DAC`
- [DifZwOpenKeyTransactedWrapper](../64/DifZwOpenKeyTransactedWrapper_function_00643EF0.md) at `0x00643F56`
- [DifZwOpenKeyWrapper](../64/DifZwOpenKeyWrapper_function_00644080.md) at `0x006440E2`
- [DifZwOpenProcessTokenExWrapper](../64/DifZwOpenProcessTokenExWrapper_function_00644200.md) at `0x00644268`
- [DifZwOpenProcessTokenWrapper](../64/DifZwOpenProcessTokenWrapper_function_00644390.md) at `0x006443F2`
- [DifZwOpenProcessWrapper](../64/DifZwOpenProcessWrapper_function_00644510.md) at `0x00644576`
- [DifZwOpenResourceManagerWrapper](../64/DifZwOpenResourceManagerWrapper_function_006446A0.md) at `0x0064470C`
- [DifZwOpenSectionWrapper](../64/DifZwOpenSectionWrapper_function_00644850.md) at `0x006448B2`
- [DifZwOpenSymbolicLinkObjectWrapper](../64/DifZwOpenSymbolicLinkObjectWrapper_function_006449D0.md) at `0x00644A32`
- [DifZwOpenThreadTokenExWrapper](../64/DifZwOpenThreadTokenExWrapper_function_00644B50.md) at `0x00644BB6`
- [DifZwOpenThreadTokenWrapper](../64/DifZwOpenThreadTokenWrapper_function_00644CF0.md) at `0x00644D58`
- [DifZwOpenThreadWrapper](../64/DifZwOpenThreadWrapper_function_00644E80.md) at `0x00644EE6`
- [DifZwOpenTimerWrapper](../64/DifZwOpenTimerWrapper_function_00645010.md) at `0x00645072`
- [DifZwOpenTransactionManagerWrapper](../64/DifZwOpenTransactionManagerWrapper_function_00645190.md) at `0x006451F8`
- [DifZwOpenTransactionWrapper](../64/DifZwOpenTransactionWrapper_function_00645340.md) at `0x006453AC`
- [DifZwPowerInformationWrapper](../64/DifZwPowerInformationWrapper_function_006454F0.md) at `0x00645555`
- [DifZwPrePrepareEnlistmentWrapper](../64/DifZwPrePrepareEnlistmentWrapper_function_00645690.md) at `0x006456E6`
- [DifZwPrepareCompleteWrapper](../64/DifZwPrepareCompleteWrapper_function_00645800.md) at `0x00645856`
- [DifZwPrepareEnlistmentWrapper](../64/DifZwPrepareEnlistmentWrapper_function_00645970.md) at `0x006459C6`
- [DifZwProtectVirtualMemoryWrapper](../64/DifZwProtectVirtualMemoryWrapper_function_00645AE0.md) at `0x00645B4C`
- [DifZwPulseEventWrapper](../64/DifZwPulseEventWrapper_function_00645C90.md) at `0x00645CE6`
- [DifZwQueryBootEntryOrderWrapper](../64/DifZwQueryBootEntryOrderWrapper_function_00645E00.md) at `0x00645E56`
- [DifZwQueryBootOptionsWrapper](../64/DifZwQueryBootOptionsWrapper_function_00645F70.md) at `0x00645FC6`
- [DifZwQueryDefaultLocaleWrapper](../64/DifZwQueryDefaultLocaleWrapper_function_006460E0.md) at `0x00646137`
- [DifZwQueryDefaultUILanguageWrapper](../64/DifZwQueryDefaultUILanguageWrapper_function_00646250.md) at `0x006462A5`
- [DifZwQueryDirectoryFileExWrapper](../64/DifZwQueryDirectoryFileExWrapper_function_006463C0.md) at `0x00646428`
- [DifZwQueryDirectoryFileWrapper](../64/DifZwQueryDirectoryFileWrapper_function_006465B0.md) at `0x00646618`
- [DifZwQueryDirectoryObjectWrapper](../64/DifZwQueryDirectoryObjectWrapper_function_006467B0.md) at `0x0064681B`
- [DifZwQueryDriverEntryOrderWrapper](../64/DifZwQueryDriverEntryOrderWrapper_function_00646980.md) at `0x006469D6`
- [DifZwQueryEaFileWrapper](../64/DifZwQueryEaFileWrapper_function_00646AF0.md) at `0x00646B58`
- [DifZwQueryFullAttributesFileWrapper](../64/DifZwQueryFullAttributesFileWrapper_function_00646CD0.md) at `0x00646D26`
- [DifZwQueryInformationEnlistmentWrapper](../64/DifZwQueryInformationEnlistmentWrapper_function_00646E40.md) at `0x00646EAC`
- [DifZwQueryInformationFileWrapper](../64/DifZwQueryInformationFileWrapper_function_00646FF0.md) at `0x00647056`
- [DifZwQueryInformationJobObjectWrapper](../64/DifZwQueryInformationJobObjectWrapper_function_00647190.md) at `0x006471FC`
- [DifZwQueryInformationProcessWrapper](../64/DifZwQueryInformationProcessWrapper_function_00647340.md) at `0x006473AC`
- [DifZwQueryInformationResourceManagerWrapper](../64/DifZwQueryInformationResourceManagerWrapper_function_006474F0.md) at `0x0064755C`
- [DifZwQueryInformationThreadWrapper](../64/DifZwQueryInformationThreadWrapper_function_006476A0.md) at `0x0064770C`
- [DifZwQueryInformationTokenWrapper](../64/DifZwQueryInformationTokenWrapper_function_00647850.md) at `0x006478BC`
- [DifZwQueryInformationTransactionManagerWrapper](../64/DifZwQueryInformationTransactionManagerWrapper_function_00647A00.md) at `0x00647A6C`
- [DifZwQueryInformationTransactionWrapper](../64/DifZwQueryInformationTransactionWrapper_function_00647BB0.md) at `0x00647C1C`
- [DifZwQueryInstallUILanguageWrapper](../64/DifZwQueryInstallUILanguageWrapper_function_00647D60.md) at `0x00647DB5`
- [DifZwQueryKeyWrapper](../64/DifZwQueryKeyWrapper_function_00647ED0.md) at `0x00647F3C`
- [DifZwQueryLicenseValueWrapper](../64/DifZwQueryLicenseValueWrapper_function_00648080.md) at `0x006480EC`
- [DifZwQueryObjectWrapper](../64/DifZwQueryObjectWrapper_function_00648230.md) at `0x0064829C`
- [DifZwQuerySectionWrapper](../64/DifZwQuerySectionWrapper_function_006483E0.md) at `0x0064844C`
- [DifZwQuerySecurityObjectWrapper](../64/DifZwQuerySecurityObjectWrapper_function_00648590.md) at `0x006485FC`
- [DifZwQuerySymbolicLinkObjectWrapper](../64/DifZwQuerySymbolicLinkObjectWrapper_function_00648740.md) at `0x006487A2`
- [DifZwQuerySystemInformationWrapper](../64/DifZwQuerySystemInformationWrapper_function_006488C0.md) at `0x00648927`
- [DifZwQueryValueKeyWrapper](../64/DifZwQueryValueKeyWrapper_function_00648A50.md) at `0x00648AB8`
- [DifZwQueryVolumeInformationFileWrapper](../64/DifZwQueryVolumeInformationFileWrapper_function_00648C00.md) at `0x00648C66`
- [DifZwReadFileWrapper](../64/DifZwReadFileWrapper_function_00648DA0.md) at `0x00648E08`
- [DifZwRemoveIoCompletionExWrapper](../64/DifZwRemoveIoCompletionExWrapper_function_00648F90.md) at `0x00648FF8`
- [DifZwRenameKeyWrapper](../64/DifZwRenameKeyWrapper_function_00649140.md) at `0x00649196`
- [DifZwReplaceKeyWrapper](../64/DifZwReplaceKeyWrapper_function_006492B0.md) at `0x00649312`
- [DifZwRequestWaitReplyPortWrapper](../64/DifZwRequestWaitReplyPortWrapper_function_00649430.md) at `0x00649492`
- [DifZwResetEventWrapper](../64/DifZwResetEventWrapper_function_006495B0.md) at `0x00649606`
- [DifZwRestoreKeyWrapper](../64/DifZwRestoreKeyWrapper_function_00649720.md) at `0x00649782`
- [DifZwRollbackEnlistmentWrapper](../64/DifZwRollbackEnlistmentWrapper_function_006498A0.md) at `0x006498F6`
- [DifZwSetBootEntryOrderWrapper](../64/DifZwSetBootEntryOrderWrapper_function_00649A10.md) at `0x00649A66`
- [DifZwSetBootOptionsWrapper](../64/DifZwSetBootOptionsWrapper_function_00649B80.md) at `0x00649BD6`
- [DifZwSetDriverEntryOrderWrapper](../64/DifZwSetDriverEntryOrderWrapper_function_00649CF0.md) at `0x00649D46`
- [DifZwSetEaFileWrapper](../64/DifZwSetEaFileWrapper_function_00649E60.md) at `0x00649EC6`
- [DifZwSetEventWrapper](../64/DifZwSetEventWrapper_function_00649FF0.md) at `0x0064A046`
- [DifZwSetInformationEnlistmentWrapper](../64/DifZwSetInformationEnlistmentWrapper_function_0064A160.md) at `0x0064A1C6`
- [DifZwSetInformationFileWrapper](../64/DifZwSetInformationFileWrapper_function_0064A2F0.md) at `0x0064A356`
- [DifZwSetInformationJobObjectWrapper](../64/DifZwSetInformationJobObjectWrapper_function_0064A490.md) at `0x0064A4F6`
- [DifZwSetInformationKeyWrapper](../64/DifZwSetInformationKeyWrapper_function_0064A620.md) at `0x0064A686`
- [DifZwSetInformationObjectWrapper](../64/DifZwSetInformationObjectWrapper_function_0064A7B0.md) at `0x0064A816`
- [DifZwSetInformationProcessWrapper](../64/DifZwSetInformationProcessWrapper_function_0064A940.md) at `0x0064A9A6`
- [DifZwSetInformationThreadWrapper](../64/DifZwSetInformationThreadWrapper_function_0064AAD0.md) at `0x0064AB36`
- [DifZwSetInformationTransactionWrapper](../64/DifZwSetInformationTransactionWrapper_function_0064AC60.md) at `0x0064ACC6`
- [DifZwSetSecurityObjectWrapper](../64/DifZwSetSecurityObjectWrapper_function_0064ADF0.md) at `0x0064AE52`
- [DifZwSetSystemInformationWrapper](../64/DifZwSetSystemInformationWrapper_function_0064AF70.md) at `0x0064AFCE`
- [DifZwSetSystemTimeWrapper](../64/DifZwSetSystemTimeWrapper_function_0064B0F0.md) at `0x0064B146`
- [DifZwSetTimerWrapper](../64/DifZwSetTimerWrapper_function_0064B260.md) at `0x0064B2C7`
- [DifZwSetValueKeyWrapper](../64/DifZwSetValueKeyWrapper_function_0064B420.md) at `0x0064B48C`
- [DifZwSetVolumeInformationFileWrapper](../64/DifZwSetVolumeInformationFileWrapper_function_0064B5D0.md) at `0x0064B636`
- [DifZwTranslateFilePathWrapper](../64/DifZwTranslateFilePathWrapper_function_0064B770.md) at `0x0064B7D6`
- [DifZwUnloadDriverWrapper](../64/DifZwUnloadDriverWrapper_function_0064B900.md) at `0x0064B955`
- [DifZwUnloadKeyWrapper](../64/DifZwUnloadKeyWrapper_function_0064BA70.md) at `0x0064BAC5`
- [DifZwWaitForMultipleObjectsWrapper](../64/DifZwWaitForMultipleObjectsWrapper_function_0064BBE0.md) at `0x0064BC47`
- [DifZwWaitForSingleObjectWrapper](../64/DifZwWaitForSingleObjectWrapper_function_0064BD80.md) at `0x0064BDE2`
- [DifZwWriteFileWrapper](../64/DifZwWriteFileWrapper_function_0064BF00.md) at `0x0064BF65`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004D3C08  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
004D3C0D  57                              push rdi
004D3C0E  48 83 EC 20                     sub rsp, 0x20
004D3C12  33 DB                           xor ebx, ebx
004D3C14  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
004D3C19  45 33 C9                        xor r9d, r9d
004D3C1C  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
004D3C21  8D 7B 01                        lea edi, [rbx + 1]
004D3C24  8B D7                           mov edx, edi
004D3C26  8D 4B 03                        lea ecx, [rbx + 3]
004D3C29  E8 C2 63 E2 FF                  call 0x1402f9ff0
004D3C2E  66 3B C7                        cmp ax, di
004D3C31  48 0F 43 5C 24 30               cmovae rbx, qword ptr [rsp + 0x30]
004D3C37  48 8B C3                        mov rax, rbx
004D3C3A  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
004D3C3F  48 83 C4 20                     add rsp, 0x20
004D3C43  5F                              pop rdi
004D3C44  C3                              ret
004D3C45  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifGetReturnAddressForWrappers(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    a4 = 0;
    v_stack_p8 = 0;
    result = RtlCaptureStackBackTrace(v_rbx + 3, (unsigned int)((unsigned int)(v_rbx + 1)), v_stack_p8, a4);
    if (((unsigned __int16)(result)) >= ((unsigned __int16)(v_rbx + 1))) { v_rbx = v_stack_p8; }
    v_rsp = (v_rsp) + (32);
    return v_rbx;
}
```

## 5. (Beta) C Style

```c
int64_t DifGetReturnAddressForWrappers(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    Arg4 = 0;
    v_stack_p8 = 0;
    result = RtlCaptureStackBackTrace(local_rbx + 3, (uint32_t)((uint32_t)(local_rbx + 1)), v_stack_p8, Arg4);
    if (((uint16_t)(result)) >= ((uint16_t)(local_rbx + 1))) { local_rbx = v_stack_p8; }
    local_rsp = (local_rsp) + (32);
    return local_rbx;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004D3C08&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004D3C08[BB_004D3C08]
  bb_004D3C45[BB_004D3C45]
```
