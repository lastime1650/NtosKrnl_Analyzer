# NtSetSystemInformation

- RVA: `0x00AF4A60`–`0x00AF68A0` (길이 `7,744` bytes)
- VA: `0x0000000140AF4A60`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D4330`
- 디코드: `1,737`개 명령, `7,744/7,744` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **161**; 고유 호출 대상: **97**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **45**

### Outgoing calls
- `0x00AF4AEB` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF4BF7` → [MmUnloadSystemImage](../AA/MmUnloadSystemImage_function_00AA2F60.md) (function, `0x00AA2F60`)
- `0x00AF4C1F` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF4C7A` → [KeSynchronizeWithDynamicProcessors](../A1/KeSynchronizeWithDynamicProcessors_function_00A17094.md) (function, `0x00A17094`)
- `0x00AF4C84` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (function, `0x00249EF0`)
- `0x00AF4CDD` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF4D40` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF4D4D` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00AF4D8C` → [ExAcquireTimeRefreshLockExclusive](../9C/ExAcquireTimeRefreshLockExclusive_function_009C5810.md) (function, `0x009C5810`)
- `0x00AF4DA0` → [ExpUpdateTimerConfiguration](../../text/39/ExpUpdateTimerConfiguration_function_00398B2C.md) (function, `0x00398B2C`)
- `0x00AF4DA7` → [ExReleaseTimeRefreshLockExclusive](../9C/ExReleaseTimeRefreshLockExclusive_function_009C5874.md) (function, `0x009C5874`)
- `0x00AF4E65` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF4E86` → [RtlReadULongFromUser](../70/RtlReadULongFromUser_function_00705E08.md) (function, `0x00705E08`)
- `0x00AF4E96` → [RtlReadULong64FromUser](../70/RtlReadULong64FromUser_function_00705DCC.md) (function, `0x00705DCC`)
- `0x00AF4ED1` → [RtlCopyFromUser](../../text/4F/RtlCopyFromUser_function_004FDAE8.md) (function, `0x004FDAE8`)
- `0x00AF4F14` → [RtlCopyFromUser](../../text/4F/RtlCopyFromUser_function_004FDAE8.md) (function, `0x004FDAE8`)
- `0x00AF4F2F` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00AF4F75` → [ZwSetSystemInformation](../../text/6B/ZwSetSystemInformation_function_006B0870.md) (function, `0x006B0870`)
- `0x00AF4FC7` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x00AF4FE2` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (function, `0x00443B60`)
- `0x00AF4FF3` → [MmUnloadSystemImage](../AA/MmUnloadSystemImage_function_00AA2F60.md) (function, `0x00AA2F60`)
- `0x00AF500E` → [ExpInitializeSessionDriver](ExpInitializeSessionDriver_function_00AF49D4.md) (function, `0x00AF49D4`)
- `0x00AF502D` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00AF5041` → [MmUnloadSystemImage](../AA/MmUnloadSystemImage_function_00AA2F60.md) (function, `0x00AA2F60`)
- `0x00AF5064` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5074` → [CmSetRegistryQuotaInformation](../7E/CmSetRegistryQuotaInformation_function_007E21DC.md) (function, `0x007E21DC`)
- `0x00AF508D` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF509A` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00AF50B2` → [IoConfigureCrashDump](../../text/59/IoConfigureCrashDump_function_00591CB4.md) (function, `0x00591CB4`)
- `0x00AF510B` → [WheaCrashDumpInitializationComplete](../7D/WheaCrashDumpInitializationComplete_function_007D877C.md) (function, `0x007D877C`)
- `0x00AF5124` → [EtwSetPerformanceTraceInformation](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (function, `0x00A53928`)
- `0x00AF512E` → [MmCreateMirror](../7F/MmCreateMirror_function_007FCB50.md) (function, `0x007FCB50`)
- `0x00AF514C` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5166` → [PsChangeQuantumTable](../A3/PsChangeQuantumTable_function_00A3BE70.md) (function, `0x00A3BE70`)
- `0x00AF51D4` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF51E1` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00AF522E` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00AF5245` → [KdUpdateTimeSlipEvent](../../text/5B/KdUpdateTimeSlipEvent_function_005B0C1C.md) (function, `0x005B0C1C`)
- `0x00AF526D` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5285` → [VfProbeAndCaptureUnicodeString](../../pagevrfy/B9/VfProbeAndCaptureUnicodeString_function_00B92FBC.md) (function, `0x00B92FBC`)
- `0x00AF52B3` → [VfRemoveVerifierEntry](../../pagevrfy/BA/VfRemoveVerifierEntry_function_00BAC4C4.md) (function, `0x00BAC4C4`)
- `0x00AF52C0` → [VfAddVerifierEntry](../../pagevrfy/BA/VfAddVerifierEntry_function_00BAC31C.md) (function, `0x00BAC31C`)
- `0x00AF52D4` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF52EA` → [VfSetVerifierInformation](../../pagevrfy/BA/VfSetVerifierInformation_function_00BAC4EC.md) (function, `0x00BAC4EC`)
- `0x00AF532C` → [ExpUpdateComPlusPackage](../7C/ExpUpdateComPlusPackage_function_007C5580.md) (function, `0x007C5580`)
- `0x00AF535B` → [PfSnSetPrefetcherInformation](../96/PfSnSetPrefetcherInformation_function_0096139C.md) (function, `0x0096139C`)
- `0x00AF53BF` → [MmLoadSystemImage](../99/MmLoadSystemImage_function_0099A9A0.md) (function, `0x0099A9A0`)
- `0x00AF53E8` → [RtlImageDirectoryEntryToData](../../text/43/RtlImageDirectoryEntryToData_function_004328D0.md) (function, `0x004328D0`)
- `0x00AF53F8` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (function, `0x00443B60`)
- `0x00AF54E2` → [MmIssueMemoryListCommand](../7F/MmIssueMemoryListCommand_function_007FE8B0.md) (function, `0x007FE8B0`)
- `0x00AF54F7` → [PfSetSuperfetchInformation](../AD/PfSetSuperfetchInformation_function_00ADE6E8.md) (function, `0x00ADE6E8`)
- `0x00AF550A` → [ExpRegisterFirmwareTableInformationHandler](../7C/ExpRegisterFirmwareTableInformationHandler_function_007C504C.md) (function, `0x007C504C`)
- `0x00AF5592` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AF55B5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AF560D` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5646` → [MmAdjustWorkingSetSizeEx](../../text/47/MmAdjustWorkingSetSizeEx_function_0047D8D4.md) (function, `0x0047D8D4`)
- `0x00AF56CF` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5722` → [DbgkRegisterErrorPort](../A9/DbgkRegisterErrorPort_function_00A9C39C.md) (function, `0x00A9C39C`)
- `0x00AF5736` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5785` → [ObSetRefTraceInformation](../74/ObSetRefTraceInformation_function_0074F7B0.md) (function, `0x0074F7B0`)
- `0x00AF57A3` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF580E` → [PsLookupProcessThreadByCid](../A3/PsLookupProcessThreadByCid_function_00A37420.md) (function, `0x00A37420`)
- `0x00AF5839` → [KeSetActualBasePriorityThread](../../text/3C/KeSetActualBasePriorityThread_function_003C4370.md) (function, `0x003C4370`)
- `0x00AF5846` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF585A` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5874` → [VfSetVerifierInformationEx](../../pagevrfy/BA/VfSetVerifierInformationEx_function_00BAC624.md) (function, `0x00BAC624`)
- `0x00AF58D7` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF58E9` → [ExpSetTimeZoneInformation](../7C/ExpSetTimeZoneInformation_function_007C5240.md) (function, `0x007C5240`)
- `0x00AF5910` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5950` → [VfProbeAndCaptureUnicodeStringBuffer](../../pagevrfy/B9/VfProbeAndCaptureUnicodeStringBuffer_function_00B92FF8.md) (function, `0x00B92FF8`)
- `0x00AF5968` → [VfProbeAndCaptureUnicodeStringBuffer](../../pagevrfy/B9/VfProbeAndCaptureUnicodeStringBuffer_function_00B92FF8.md) (function, `0x00B92FF8`)
- `0x00AF597B` → [VfFreeCapturedUnicodeString](../../pagevrfy/B9/VfFreeCapturedUnicodeString_function_00B92E54.md) (function, `0x00B92E54`)
- `0x00AF5999` → [VfFaultsSetParameters](../../pagevrfy/BA/VfFaultsSetParameters_function_00BA67E4.md) (function, `0x00BA67E4`)
- `0x00AF59AD` → [VfFreeCapturedUnicodeString](../../pagevrfy/B9/VfFreeCapturedUnicodeString_function_00B92E54.md) (function, `0x00B92E54`)
- `0x00AF59CF` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5A3F` → [ExpSetProcessorMicrocodeUpdateInformation](../7C/ExpSetProcessorMicrocodeUpdateInformation_function_007C51D8.md) (function, `0x007C51D8`)
- `0x00AF5A79` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5AB3` → [SmSetStoreInformation](../A7/SmSetStoreInformation_function_00A781B8.md) (function, `0x00A781B8`)
- `0x00AF5AC6` → [PsSetCpuQuotaInformation](../../text/5E/PsSetCpuQuotaInformation_function_005E28F8.md) (function, `0x005E28F8`)
- `0x00AF5B50` → [KeInitializeEntropySystem](../74/KeInitializeEntropySystem_function_00747EDC.md) (function, `0x00747EDC`)
- `0x00AF5B7D` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5B98` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF5BB4` → [MiGetThreadPartition](../../text/43/MiGetThreadPartition_function_0043F570.md) (function, `0x0043F570`)
- `0x00AF5BEF` → [MiCombineIdenticalPages](../AB/MiCombineIdenticalPages_function_00AB2324.md) (function, `0x00AB2324`)
- `0x00AF5C22` → [KeProcessorProfileControlArea](../../text/5B/KeProcessorProfileControlArea_function_005B184C.md) (function, `0x005B184C`)
- `0x00AF5C40` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5C60` → [MmScrubMemory](../80/MmScrubMemory_function_0080EFA0.md) (function, `0x0080EFA0`)
- `0x00AF5CA0` → [BgkSetBootGraphicsInformation](../../pagebgfx/BC/BgkSetBootGraphicsInformation_function_00BC0424.md) (function, `0x00BC0424`)
- `0x00AF5D08` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00AF5D21` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00AF5D37` → [ZwLoadDriver](../../text/6A/ZwLoadDriver_function_006AF290.md) (function, `0x006AF290`)
- `0x00AF5D52` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00AF5D5A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00AF5D5F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF5D73` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5D88` → [ZwUnloadDriver](../../text/6B/ZwUnloadDriver_function_006B0C10.md) (function, `0x006B0C10`)
- `0x00AF5DE1` → [ExpQueryElamCertInfo](../7C/ExpQueryElamCertInfo_function_007C4564.md) (function, `0x007C4564`)
- `0x00AF5E01` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5E45` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5E60` → [ExpSetSoftRebootFlags](../../text/65/ExpSetSoftRebootFlags_function_006550DC.md) (function, `0x006550DC`)
- `0x00AF5E79` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5E8C` → [ExpSetBootLoaderMetadata](../../text/65/ExpSetBootLoaderMetadata_function_00654F98.md) (function, `0x00654F98`)
- `0x00AF5EA1` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00AF5EC6` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF5F8C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AF5FA2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF5FFE` → [sub_00A179B0](../A1/Unknown_function_00A179B0.md) (function, `0x00A179B0`)
- `0x00AF6008` → [CmReconcileAndValidateAllHives](../7E/CmReconcileAndValidateAllHives_function_007E7D90.md) (function, `0x007E7D90`)
- `0x00AF6072` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF60A3` → [KeIntSteerAssignCpuSetForGsiv](../../text/5C/KeIntSteerAssignCpuSetForGsiv_function_005C5700.md) (function, `0x005C5700`)
- `0x00AF60D7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF60E0` → [ExCpuSetResourceManagerAccessCheck](../../text/3A/ExCpuSetResourceManagerAccessCheck_function_003A5444.md) (function, `0x003A5444`)
- `0x00AF60FF` → [KeModifySystemAllowedCpuSets](../../text/30/KeModifySystemAllowedCpuSets_function_00303308.md) (function, `0x00303308`)
- `0x00AF612F` → `kdcom.dll!KdInitialize` (import, 간접 대상; import `kdcom.dll!KdInitialize`)
- `0x00AF617F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF6188` → [ExCpuSetResourceManagerAccessCheck](../../text/3A/ExCpuSetResourceManagerAccessCheck_function_003A5444.md) (function, `0x003A5444`)
- `0x00AF61A9` → [KeSetTagCpuSets](../../text/5C/KeSetTagCpuSets_function_005C11BC.md) (function, `0x005C11BC`)
- `0x00AF61FB` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF6208` → [VslRelaxQuotas](../71/VslRelaxQuotas_function_00719530.md) (function, `0x00719530`)
- `0x00AF6242` → [VfProbeAndCaptureUnicodeStringBuffer](../../pagevrfy/B9/VfProbeAndCaptureUnicodeStringBuffer_function_00B92FF8.md) (function, `0x00B92FF8`)
- `0x00AF6266` → [PsSetExeModerationState](../../text/5E/PsSetExeModerationState_function_005E2DF0.md) (function, `0x005E2DF0`)
- `0x00AF62A8` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF62E9` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00AF6303` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00AF6332` → [PsInvokeWin32Callout](../91/PsInvokeWin32Callout_function_009133C0.md) (function, `0x009133C0`)
- `0x00AF6361` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00AF638F` → [PsInvokeWin32Callout](../91/PsInvokeWin32Callout_function_009133C0.md) (function, `0x009133C0`)
- `0x00AF63AC` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF63B9` → [VslProvisionDumpEncryption](../../text/58/VslProvisionDumpEncryption_function_0058ECB8.md) (function, `0x0058ECB8`)
- `0x00AF63C8` → [IoProvisionCrashDumpKey](../../text/59/IoProvisionCrashDumpKey_function_00592BF0.md) (function, `0x00592BF0`)
- `0x00AF642E` → [CmUpdateFeatureConfiguration](../7E/CmUpdateFeatureConfiguration_function_007E5C10.md) (function, `0x007E5C10`)
- `0x00AF644C` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF64B9` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF64C6` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00AF64ED` → [ExSetLeapSecondEnabled](../7C/ExSetLeapSecondEnabled_function_007C59F8.md) (function, `0x007C59F8`)
- `0x00AF655A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF6573` → [ExCpuSetResourceManagerAccessCheck](../../text/3A/ExCpuSetResourceManagerAccessCheck_function_003A5444.md) (function, `0x003A5444`)
- `0x00AF65A4` → [CmUpdateFeatureUsageSubscription](../7E/CmUpdateFeatureUsageSubscription_function_007E5E78.md) (function, `0x007E5E78`)
- `0x00AF65EC` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF6604` → [VfProbeAndCaptureUnicodeString](../../pagevrfy/B9/VfProbeAndCaptureUnicodeString_function_00B92FBC.md) (function, `0x00B92FBC`)
- `0x00AF663E` → [VfVolatileRemoveDifVerification](../../text/61/VfVolatileRemoveDifVerification_function_006169F0.md) (function, `0x006169F0`)
- `0x00AF6648` → [VfVolatileApplyDifVerification](../../text/61/VfVolatileApplyDifVerification_function_00616874.md) (function, `0x00616874`)
- `0x00AF665B` → [VfFreeCapturedUnicodeString](../../pagevrfy/B9/VfFreeCapturedUnicodeString_function_00B92E54.md) (function, `0x00B92E54`)
- `0x00AF666F` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF6678` → [VfVolatileClearDifRuleClass](../../text/61/VfVolatileClearDifRuleClass_function_006168E0.md) (function, `0x006168E0`)
- `0x00AF668C` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF66A5` → [VfVolatileSetDifRuleClass](../../text/61/VfVolatileSetDifRuleClass_function_00616AA4.md) (function, `0x00616AA4`)
- `0x00AF66B8` → [ExPoolSetLimit](../../text/65/ExPoolSetLimit_function_00656498.md) (function, `0x00656498`)
- `0x00AF670A` → [RtlCheckTokenMembership](../../text/3A/RtlCheckTokenMembership_function_003A5A10.md) (function, `0x003A5A10`)
- `0x00AF672B` → [KeUpdateDpcWatchdogConfiguration](../../text/5B/KeUpdateDpcWatchdogConfiguration_function_005B5A34.md) (function, `0x005B5A34`)
- `0x00AF673F` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF6752` → [VfPtGenerateTraceInformation](../../pagevrfy/B9/VfPtGenerateTraceInformation_function_00B9BF5C.md) (function, `0x00B9BF5C`)
- `0x00AF6774` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AF6784` → [PnpIommuBlockUnblockDevice](../74/PnpIommuBlockUnblockDevice_function_00740408.md) (function, `0x00740408`)
- `0x00AF67CB` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF6809` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF6860` → [HvlQuerySetBootPagesInfo](../71/HvlQuerySetBootPagesInfo_function_00717D7C.md) (function, `0x00717D7C`)
- `0x00AF6874` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00AF688D` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00AF6893` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00AF6899` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- [WmipRegisterFirmwareProviders](../../init/C4/WmipRegisterFirmwareProviders_function_00C4D62C.md) at `0x00C4D66D`
- [WmipRegisterFirmwareProviders](../../init/C4/WmipRegisterFirmwareProviders_function_00C4D62C.md) at `0x00C4D6AA`

### Static image references
- `0x00AF4A75` → RVA `0x00E0A740` (`.data`; read)
- `0x00AF4C18` → RVA `0x00FD9B20` (`PAGEDATA`; read)
- `0x00AF4C4F` → RVA `0x00FC50C0` (`ALMOSTRO`; write)
- `0x00AF4C5C` → RVA `0x00FC50E8` (`ALMOSTRO`; write)
- `0x00AF4C6E` → RVA `0x00FC50C4` (`ALMOSTRO`; write)
- `0x00AF4C74` → RVA `0x00FC51A0` (`ALMOSTRO`; write)
- `0x00AF4C91` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x00AF4C9E` → RVA `0x00FC50C0` (`ALMOSTRO`; read)
- `0x00AF4CAA` → RVA `0x00FC50E8` (`ALMOSTRO`; read)
- `0x00AF4CD6` → RVA `0x00FD9A80` (`PAGEDATA`; read)
- `0x00AF4CF0` → RVA `0x00FC42C0` (`.data`; read)
- `0x00AF4D0D` → RVA `0x00FC42C0` (`.data`; write)
- `0x00AF4D39` → RVA `0x00FD9BE0` (`PAGEDATA`; read)
- `0x00AF4DC9` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x00AF4F1D` → RVA `0x00038AE0` (`.rdata`; read)
- `0x00AF4FD4` → RVA `0x00F067D0` (`.data`; read)
- `0x00AF505D` → RVA `0x00FD9B70` (`PAGEDATA`; read)
- `0x00AF5145` → RVA `0x00FD9A78` (`PAGEDATA`; read)
- `0x00AF5205` → RVA `0x00FC6B80` (`ALMOSTRO`; read)
- `0x00AF533B` → RVA `0x00FC5008` (`ALMOSTRO`; read)
- `0x00AF5572` → RVA `0x004FC600` (`BvgaSetVirtualFrameBuffer`; read)
- `0x00AF5579` → RVA `0x00E00B38` (`.data`; read)
- `0x00AF559C` → RVA `0x00E00B18` (`.data`; read)
- `0x00AF55A5` → RVA `0x00E00B28` (`.data`; read)
- `0x00AF55AE` → RVA `0x00E00B20` (`.data`; read)
- `0x00AF56A5` → RVA `0x00FC6A97` (`ALMOSTRO`; read)
- `0x00AF575F` → RVA `0x00FC6C28` (`ALMOSTRO`; write)
- `0x00AF576F` → RVA `0x00FC5124` (`ALMOSTRO`; write)
- `0x00AF579C` → RVA `0x00FD9AE8` (`PAGEDATA`; read)
- `0x00AF58D0` → RVA `0x00FD9D70` (`PAGEDATA`; read)
- `0x00AF5A72` → RVA `0x00FD9B08` (`PAGEDATA`; read)
- `0x00AF5CC0` → RVA `0x00B083F0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AF5CFE` → RVA `0x00FD8228` (`PAGEDATA`; read)
- `0x00AF5D3E` → RVA `0x00FD8228` (`PAGEDATA`; read/write)
- `0x00AF5EBF` → RVA `0x00FD9B30` (`PAGEDATA`; read)
- `0x00AF6121` → RVA `0x00F475E0` (`.data`; read)
- `0x00AF612F` → RVA `0x001516B8` (`kdcom.dll!KdInitialize (IAT)`; read)
- `0x00AF62C0` → RVA `0x00FC6A98` (`ALMOSTRO`; read)
- `0x00AF6477` → RVA `0x00FC43C0` (`.data`; read)
- `0x00AF6488` → RVA `0x00FC43C0` (`.data`; write)
- `0x00AF6500` → RVA `0x00EFEE38` (`.data`; read)
- `0x00AF6701` → RVA `0x00FD9A68` (`PAGEDATA`; read)
- `0x00AF675C` → RVA `0x00F04EE0` (`.data`; read)
- `0x00AF67E8` → RVA `0x00FC6DDC` (`ALMOSTRO`; write)
- `0x00AF6843` → RVA `0x00EEEFEC` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **77**
  - `0x00AF4AEB` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF4C84` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (`PAGE` → `.text`)
  - `0x00AF4D4D` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00AF4DA0` → [ExpUpdateTimerConfiguration](../../text/39/ExpUpdateTimerConfiguration_function_00398B2C.md) (`PAGE` → `.text`)
  - `0x00AF4ED1` → [RtlCopyFromUser](../../text/4F/RtlCopyFromUser_function_004FDAE8.md) (`PAGE` → `.text`)
  - `0x00AF4F14` → [RtlCopyFromUser](../../text/4F/RtlCopyFromUser_function_004FDAE8.md) (`PAGE` → `.text`)
  - `0x00AF4F2F` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00AF4F75` → [ZwSetSystemInformation](../../text/6B/ZwSetSystemInformation_function_006B0870.md) (`PAGE` → `.text`)
  - `0x00AF4FC7` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x00AF4FE2` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (`PAGE` → `.text`)
  - `0x00AF502D` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00AF509A` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00AF50B2` → [IoConfigureCrashDump](../../text/59/IoConfigureCrashDump_function_00591CB4.md) (`PAGE` → `.text`)
  - `0x00AF51E1` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00AF5245` → [KdUpdateTimeSlipEvent](../../text/5B/KdUpdateTimeSlipEvent_function_005B0C1C.md) (`PAGE` → `.text`)
  - `0x00AF5285` → [VfProbeAndCaptureUnicodeString](../../pagevrfy/B9/VfProbeAndCaptureUnicodeString_function_00B92FBC.md) (`PAGE` → `PAGEVRFY`)
  - `0x00AF52B3` → [VfRemoveVerifierEntry](../../pagevrfy/BA/VfRemoveVerifierEntry_function_00BAC4C4.md) (`PAGE` → `PAGEVRFY`)
  - `0x00AF52C0` → [VfAddVerifierEntry](../../pagevrfy/BA/VfAddVerifierEntry_function_00BAC31C.md) (`PAGE` → `PAGEVRFY`)
  - `0x00AF52EA` → [VfSetVerifierInformation](../../pagevrfy/BA/VfSetVerifierInformation_function_00BAC4EC.md) (`PAGE` → `PAGEVRFY`)
  - `0x00AF53E8` → [RtlImageDirectoryEntryToData](../../text/43/RtlImageDirectoryEntryToData_function_004328D0.md) (`PAGE` → `.text`)
  - `0x00AF53F8` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (`PAGE` → `.text`)
  - `0x00AF5592` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AF55B5` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AF5646` → [MmAdjustWorkingSetSizeEx](../../text/47/MmAdjustWorkingSetSizeEx_function_0047D8D4.md) (`PAGE` → `.text`)
  - `0x00AF5839` → [KeSetActualBasePriorityThread](../../text/3C/KeSetActualBasePriorityThread_function_003C4370.md) (`PAGE` → `.text`)
  - `0x00AF5846` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF5874` → [VfSetVerifierInformationEx](../../pagevrfy/BA/VfSetVerifierInformationEx_function_00BAC624.md) (`PAGE` → `PAGEVRFY`)
  - `0x00AF5950` → [VfProbeAndCaptureUnicodeStringBuffer](../../pagevrfy/B9/VfProbeAndCaptureUnicodeStringBuffer_function_00B92FF8.md) (`PAGE` → `PAGEVRFY`)
  - `0x00AF5968` → [VfProbeAndCaptureUnicodeStringBuffer](../../pagevrfy/B9/VfProbeAndCaptureUnicodeStringBuffer_function_00B92FF8.md) (`PAGE` → `PAGEVRFY`)
  - `0x00AF597B` → [VfFreeCapturedUnicodeString](../../pagevrfy/B9/VfFreeCapturedUnicodeString_function_00B92E54.md) (`PAGE` → `PAGEVRFY`)
  - `0x00AF5999` → [VfFaultsSetParameters](../../pagevrfy/BA/VfFaultsSetParameters_function_00BA67E4.md) (`PAGE` → `PAGEVRFY`)
  - `0x00AF59AD` → [VfFreeCapturedUnicodeString](../../pagevrfy/B9/VfFreeCapturedUnicodeString_function_00B92E54.md) (`PAGE` → `PAGEVRFY`)
  - `0x00AF5AC6` → [PsSetCpuQuotaInformation](../../text/5E/PsSetCpuQuotaInformation_function_005E28F8.md) (`PAGE` → `.text`)
  - `0x00AF5B98` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF5BB4` → [MiGetThreadPartition](../../text/43/MiGetThreadPartition_function_0043F570.md) (`PAGE` → `.text`)
  - `0x00AF5C22` → [KeProcessorProfileControlArea](../../text/5B/KeProcessorProfileControlArea_function_005B184C.md) (`PAGE` → `.text`)
  - `0x00AF5CA0` → [BgkSetBootGraphicsInformation](../../pagebgfx/BC/BgkSetBootGraphicsInformation_function_00BC0424.md) (`PAGE` → `PAGEBGFX`)
  - `0x00AF5D08` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00AF5D21` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00AF5D37` → [ZwLoadDriver](../../text/6A/ZwLoadDriver_function_006AF290.md) (`PAGE` → `.text`)
  - `0x00AF5D52` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00AF5D5A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00AF5D5F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF5D88` → [ZwUnloadDriver](../../text/6B/ZwUnloadDriver_function_006B0C10.md) (`PAGE` → `.text`)
  - `0x00AF5E60` → [ExpSetSoftRebootFlags](../../text/65/ExpSetSoftRebootFlags_function_006550DC.md) (`PAGE` → `.text`)
  - `0x00AF5E8C` → [ExpSetBootLoaderMetadata](../../text/65/ExpSetBootLoaderMetadata_function_00654F98.md) (`PAGE` → `.text`)
  - `0x00AF5EA1` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x00AF5F8C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AF5FA2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF60A3` → [KeIntSteerAssignCpuSetForGsiv](../../text/5C/KeIntSteerAssignCpuSetForGsiv_function_005C5700.md) (`PAGE` → `.text`)
  - `0x00AF60D7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF60E0` → [ExCpuSetResourceManagerAccessCheck](../../text/3A/ExCpuSetResourceManagerAccessCheck_function_003A5444.md) (`PAGE` → `.text`)
  - `0x00AF60FF` → [KeModifySystemAllowedCpuSets](../../text/30/KeModifySystemAllowedCpuSets_function_00303308.md) (`PAGE` → `.text`)
  - `0x00AF617F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF6188` → [ExCpuSetResourceManagerAccessCheck](../../text/3A/ExCpuSetResourceManagerAccessCheck_function_003A5444.md) (`PAGE` → `.text`)
  - `0x00AF61A9` → [KeSetTagCpuSets](../../text/5C/KeSetTagCpuSets_function_005C11BC.md) (`PAGE` → `.text`)
  - `0x00AF6242` → [VfProbeAndCaptureUnicodeStringBuffer](../../pagevrfy/B9/VfProbeAndCaptureUnicodeStringBuffer_function_00B92FF8.md) (`PAGE` → `PAGEVRFY`)
  - `0x00AF6266` → [PsSetExeModerationState](../../text/5E/PsSetExeModerationState_function_005E2DF0.md) (`PAGE` → `.text`)
  - `0x00AF6303` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00AF6361` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00AF63B9` → [VslProvisionDumpEncryption](../../text/58/VslProvisionDumpEncryption_function_0058ECB8.md) (`PAGE` → `.text`)
  - `0x00AF63C8` → [IoProvisionCrashDumpKey](../../text/59/IoProvisionCrashDumpKey_function_00592BF0.md) (`PAGE` → `.text`)
  - `0x00AF64C6` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00AF655A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF6573` → [ExCpuSetResourceManagerAccessCheck](../../text/3A/ExCpuSetResourceManagerAccessCheck_function_003A5444.md) (`PAGE` → `.text`)
  - `0x00AF6604` → [VfProbeAndCaptureUnicodeString](../../pagevrfy/B9/VfProbeAndCaptureUnicodeString_function_00B92FBC.md) (`PAGE` → `PAGEVRFY`)
  - `0x00AF663E` → [VfVolatileRemoveDifVerification](../../text/61/VfVolatileRemoveDifVerification_function_006169F0.md) (`PAGE` → `.text`)
  - `0x00AF6648` → [VfVolatileApplyDifVerification](../../text/61/VfVolatileApplyDifVerification_function_00616874.md) (`PAGE` → `.text`)
  - `0x00AF665B` → [VfFreeCapturedUnicodeString](../../pagevrfy/B9/VfFreeCapturedUnicodeString_function_00B92E54.md) (`PAGE` → `PAGEVRFY`)
  - `0x00AF6678` → [VfVolatileClearDifRuleClass](../../text/61/VfVolatileClearDifRuleClass_function_006168E0.md) (`PAGE` → `.text`)
  - `0x00AF66A5` → [VfVolatileSetDifRuleClass](../../text/61/VfVolatileSetDifRuleClass_function_00616AA4.md) (`PAGE` → `.text`)
  - `0x00AF66B8` → [ExPoolSetLimit](../../text/65/ExPoolSetLimit_function_00656498.md) (`PAGE` → `.text`)
  - `0x00AF670A` → [RtlCheckTokenMembership](../../text/3A/RtlCheckTokenMembership_function_003A5A10.md) (`PAGE` → `.text`)
  - `0x00AF672B` → [KeUpdateDpcWatchdogConfiguration](../../text/5B/KeUpdateDpcWatchdogConfiguration_function_005B5A34.md) (`PAGE` → `.text`)
  - `0x00AF6752` → [VfPtGenerateTraceInformation](../../pagevrfy/B9/VfPtGenerateTraceInformation_function_00B9BF5C.md) (`PAGE` → `PAGEVRFY`)
  - `0x00AF6774` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AF6874` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AF4A60  4C 8B DC                        mov r11, rsp
00AF4A63  53                              push rbx
00AF4A64  56                              push rsi
00AF4A65  57                              push rdi
00AF4A66  41 54                           push r12
00AF4A68  41 55                           push r13
00AF4A6A  41 56                           push r14
00AF4A6C  41 57                           push r15
00AF4A6E  48 81 EC 30 05 00 00            sub rsp, 0x530
00AF4A75  48 8B 05 C4 5C 31 00            mov rax, qword ptr [rip + 0x315cc4]
00AF4A7C  48 33 C4                        xor rax, rsp
00AF4A7F  48 89 84 24 20 05 00 00         mov qword ptr [rsp + 0x520], rax
00AF4A87  45 8B F8                        mov r15d, r8d
00AF4A8A  4C 8B F2                        mov r14, rdx
00AF4A8D  8B D9                           mov ebx, ecx
00AF4A8F  0F 57 C0                        xorps xmm0, xmm0
00AF4A92  0F 11 84 24 58 01 00 00         movups xmmword ptr [rsp + 0x158], xmm0
00AF4A9A  33 F6                           xor esi, esi
00AF4A9C  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
00AF4AA1  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
00AF4AA6  49 89 B3 50 FB FF FF            mov qword ptr [r11 - 0x4b0], rsi
00AF4AAD  40 88 74 24 54                  mov byte ptr [rsp + 0x54], sil
00AF4AB2  44 8D 6E 01                     lea r13d, [rsi + 1]
00AF4AB6  44 89 6C 24 78                  mov dword ptr [rsp + 0x78], r13d
00AF4ABB  49 89 B3 70 FB FF FF            mov qword ptr [r11 - 0x490], rsi
00AF4AC2  49 89 B3 68 FB FF FF            mov qword ptr [r11 - 0x498], rsi
00AF4AC9  49 89 B3 58 FB FF FF            mov qword ptr [r11 - 0x4a8], rsi
00AF4AD0  49 89 B3 60 FB FF FF            mov qword ptr [r11 - 0x4a0], rsi
00AF4AD7  49 89 B3 28 FB FF FF            mov qword ptr [r11 - 0x4d8], rsi
00AF4ADE  33 D2                           xor edx, edx
00AF4AE0  45 8D 45 7F                     lea r8d, [r13 + 0x7f]
00AF4AE4  49 8D 8B 38 FC FF FF            lea rcx, [r11 - 0x3c8]
00AF4AEB  E8 50 21 BD FF                  call 0x1406c6c40
00AF4AF0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF4AF9  44 8A A0 32 02 00 00            mov r12b, byte ptr [rax + 0x232]
00AF4B00  44 88 64 24 38                  mov byte ptr [rsp + 0x38], r12b
00AF4B05  45 84 E4                        test r12b, r12b
00AF4B08  74 66                           je 0x140af4b70
00AF4B0A  83 FB 59                        cmp ebx, 0x59
00AF4B0D  75 05                           jne 0x140af4b14
00AF4B0F  41 8B C5                        mov eax, r13d
00AF4B12  EB 2D                           jmp 0x140af4b41
00AF4B14  81 FB CC 00 00 00               cmp ebx, 0xcc
00AF4B1A  74 20                           je 0x140af4b3c
00AF4B1C  81 FB D2 00 00 00               cmp ebx, 0xd2
00AF4B22  74 18                           je 0x140af4b3c
00AF4B24  81 FB D4 00 00 00               cmp ebx, 0xd4
00AF4B2A  74 10                           je 0x140af4b3c
00AF4B2C  81 FB 97 00 00 00               cmp ebx, 0x97
00AF4B32  75 08                           jne 0x140af4b3c
00AF4B34  45 3B FD                        cmp r15d, r13d
00AF4B37  48 8B C6                        mov rax, rsi
00AF4B3A  74 05                           je 0x140af4b41
00AF4B3C  B8 03 00 00 00                  mov eax, 3
00AF4B41  45 85 FF                        test r15d, r15d
00AF4B44  74 23                           je 0x140af4b69
00AF4B46  4C 85 F0                        test rax, r14
00AF4B49  0F 85 3E 1D 00 00               jne 0x140af688d
00AF4B4F  4B 8D 0C 3E                     lea rcx, [r14 + r15]
00AF4B53  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00AF4B5D  48 3B C8                        cmp rcx, rax
00AF4B60  77 05                           ja 0x140af4b67
00AF4B62  49 3B CE                        cmp rcx, r14
00AF4B65  73 02                           jae 0x140af4b69
00AF4B67  8A 00                           mov al, byte ptr [rax]
00AF4B69  EB 05                           jmp 0x140af4b70
00AF4B6B  E9 F9 1C 00 00                  jmp 0x140af6869
00AF4B70  8B FE                           mov edi, esi
00AF4B72  83 FB 71                        cmp ebx, 0x71
00AF4B75  0F 8F 55 0F 00 00               jg 0x140af5ad0
00AF4B7B  0F 84 3C 0F 00 00               je 0x140af5abd
00AF4B81  83 FB 47                        cmp ebx, 0x47
00AF4B84  0F 8F CD 08 00 00               jg 0x140af5457
00AF4B8A  0F 84 2B 0E 00 00               je 0x140af59bb
00AF4B90  83 FB 27                        cmp ebx, 0x27
00AF4B93  0F 8F DE 05 00 00               jg 0x140af5177
00AF4B99  0F 84 99 05 00 00               je 0x140af5138
00AF4B9F  83 FB 1C                        cmp ebx, 0x1c
00AF4BA2  0F 8F 49 02 00 00               jg 0x140af4df1
00AF4BA8  0F 84 74 01 00 00               je 0x140af4d22
00AF4BAE  8B CB                           mov ecx, ebx
00AF4BB0  83 E9 09                        sub ecx, 9
00AF4BB3  0F 84 10 01 00 00               je 0x140af4cc9
00AF4BB9  83 E9 0C                        sub ecx, 0xc
00AF4BBC  0F 84 FD 09 00 00               je 0x140af55bf
00AF4BC2  83 E9 03                        sub ecx, 3
00AF4BC5  74 3F                           je 0x140af4c06
00AF4BC7  83 E9 02                        sub ecx, 2
00AF4BCA  0F 84 99 07 00 00               je 0x140af5369
00AF4BD0  83 F9 01                        cmp ecx, 1
00AF4BD3  0F 85 D8 05 00 00               jne 0x140af51b1
00AF4BD9  41 83 FF 08                     cmp r15d, 8
00AF4BDD  0F 85 D4 1B 00 00               jne 0x140af67b7
00AF4BE3  45 84 E4                        test r12b, r12b
00AF4BE6  0F 85 E8 1B 00 00               jne 0x140af67d4
00AF4BEC  49 8B 0E                        mov rcx, qword ptr [r14]
00AF4BEF  48 89 8C 24 70 01 00 00         mov qword ptr [rsp + 0x170], rcx
00AF4BF7  E8 64 E3 FA FF                  call 0x140aa2f60
00AF4BFC  E9 6A 05 00 00                  jmp 0x140af516b
00AF4C01  E9 63 1C 00 00                  jmp 0x140af6869
00AF4C06  41 83 FF 14                     cmp r15d, 0x14
00AF4C0A  0F 85 A7 1B 00 00               jne 0x140af67b7
00AF4C10  45 84 E4                        test r12b, r12b
00AF4C13  74 17                           je 0x140af4c2c
00AF4C15  41 8A D4                        mov dl, r12b
00AF4C18  48 8B 0D 01 4F 4E 00            mov rcx, qword ptr [rip + 0x4e4f01]
00AF4C1F  E8 FC D1 D7 FF                  call 0x140871e20
00AF4C24  84 C0                           test al, al
00AF4C26  0F 84 A8 1B 00 00               je 0x140af67d4
00AF4C2C  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
00AF4C30  0F 29 84 24 A0 01 00 00         movaps xmmword ptr [rsp + 0x1a0], xmm0
00AF4C38  41 8B 4E 10                     mov ecx, dword ptr [r14 + 0x10]
00AF4C3C  89 8C 24 B0 01 00 00            mov dword ptr [rsp + 0x1b0], ecx
00AF4C43  48 8B 84 24 A0 01 00 00         mov rax, qword ptr [rsp + 0x1a0]
00AF4C4B  48 C1 E8 20                     shr rax, 0x20
00AF4C4F  89 05 6B 04 4D 00               mov dword ptr [rip + 0x4d046b], eax
00AF4C55  8B 84 24 A8 01 00 00            mov eax, dword ptr [rsp + 0x1a8]
00AF4C5C  89 05 86 04 4D 00               mov dword ptr [rip + 0x4d0486], eax
00AF4C62  48 8B 84 24 A8 01 00 00         mov rax, qword ptr [rsp + 0x1a8]
00AF4C6A  48 C1 E8 20                     shr rax, 0x20
00AF4C6E  89 05 50 04 4D 00               mov dword ptr [rip + 0x4d0450], eax
00AF4C74  89 0D 26 05 4D 00               mov dword ptr [rip + 0x4d0526], ecx
00AF4C7A  E8 15 24 F2 FF                  call 0x140a17094
00AF4C7F  B9 FF FF 00 00                  mov ecx, 0xffff
00AF4C84  E8 67 52 75 FF                  call 0x140249ef0
00AF4C89  85 C0                           test eax, eax
00AF4C8B  0F 84 D6 1B 00 00               je 0x140af6867
00AF4C91  48 8D 15 A8 3F 4D 00            lea rdx, [rip + 0x4d3fa8]
00AF4C98  44 8B C0                        mov r8d, eax
00AF4C9B  48 8B 0A                        mov rcx, qword ptr [rdx]
00AF4C9E  8B 05 1C 04 4D 00               mov eax, dword ptr [rip + 0x4d041c]
00AF4CA4  89 81 A8 38 00 00               mov dword ptr [rcx + 0x38a8], eax
00AF4CAA  8B 05 38 04 4D 00               mov eax, dword ptr [rip + 0x4d0438]
00AF4CB0  89 81 B0 38 00 00               mov dword ptr [rcx + 0x38b0], eax
00AF4CB6  48 8D 52 08                     lea rdx, [rdx + 8]
00AF4CBA  4D 2B C5                        sub r8, r13
00AF4CBD  75 DC                           jne 0x140af4c9b
00AF4CBF  E9 A3 1B 00 00                  jmp 0x140af6867
00AF4CC4  E9 A0 1B 00 00                  jmp 0x140af6869
00AF4CC9  41 83 FF 04                     cmp r15d, 4
00AF4CCD  0F 85 CF 07 00 00               jne 0x140af54a2
00AF4CD3  41 8A D4                        mov dl, r12b
00AF4CD6  48 8B 0D A3 4D 4E 00            mov rcx, qword ptr [rip + 0x4e4da3]
00AF4CDD  E8 3E D1 D7 FF                  call 0x140871e20
00AF4CE2  84 C0                           test al, al
00AF4CE4  75 0A                           jne 0x140af4cf0
00AF4CE6  BF 22 00 00 C0                  mov edi, 0xc0000022
00AF4CEB  E9 77 1B 00 00                  jmp 0x140af6867
00AF4CF0  8B 0D CA F5 4C 00               mov ecx, dword ptr [rip + 0x4cf5ca]
00AF4CF6  81 E1 0F 64 CE 6D               and ecx, 0x6dce640f
00AF4CFC  41 8B 06                        mov eax, dword ptr [r14]
00AF4CFF  25 F0 9B 31 92                  and eax, 0x92319bf0
00AF4D04  0B C8                           or ecx, eax
00AF4D06  89 8C 24 20 01 00 00            mov dword ptr [rsp + 0x120], ecx
00AF4D0D  89 0D AD F5 4C 00               mov dword ptr [rip + 0x4cf5ad], ecx
00AF4D13  41 89 0E                        mov dword ptr [r14], ecx
00AF4D16  E9 4C 1B 00 00                  jmp 0x140af6867
00AF4D1B  8B F8                           mov edi, eax
00AF4D1D  E9 45 1B 00 00                  jmp 0x140af6867
00AF4D22  41 8D 47 F8                     lea eax, [r15 - 8]
00AF4D26  A9 F7 FF FF FF                  test eax, 0xfffffff7
00AF4D2B  0F 85 86 1A 00 00               jne 0x140af67b7
00AF4D31  45 84 E4                        test r12b, r12b
00AF4D34  74 17                           je 0x140af4d4d
00AF4D36  41 8A D4                        mov dl, r12b
00AF4D39  48 8B 0D A0 4E 4E 00            mov rcx, qword ptr [rip + 0x4e4ea0]
00AF4D40  E8 DB D0 D7 FF                  call 0x140871e20
00AF4D45  84 C0                           test al, al
00AF4D47  0F 84 87 1A 00 00               je 0x140af67d4
00AF4D4D  E8 8E 15 94 FF                  call 0x1404362e0
00AF4D52  84 C0                           test al, al
00AF4D54  0F 85 3B 19 00 00               jne 0x140af6695
00AF4D5A  41 83 FF 10                     cmp r15d, 0x10
00AF4D5E  75 51                           jne 0x140af4db1
00AF4D60  41 8A 4E 08                     mov cl, byte ptr [r14 + 8]
00AF4D64  88 4C 24 30                     mov byte ptr [rsp + 0x30], cl
00AF4D68  49 8B 06                        mov rax, qword ptr [r14]
00AF4D6B  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00AF4D73  49 B8 00 03 00 00 80 F7 FF FF   movabs r8, 0xfffff78000000300
00AF4D7D  84 C9                           test cl, cl
00AF4D7F  74 0B                           je 0x140af4d8c
00AF4D81  49 8B 00                        mov rax, qword ptr [r8]
00AF4D84  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00AF4D8C  E8 7F 0A ED FF                  call 0x1409c5810
00AF4D91  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
00AF4D96  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
00AF4D9E  33 C9                           xor ecx, ecx
00AF4DA0  E8 87 3D 8A FF                  call 0x140398b2c
00AF4DA5  8B F8                           mov edi, eax
00AF4DA7  E8 C8 0A ED FF                  call 0x1409c5874
00AF4DAC  E9 B6 1A 00 00                  jmp 0x140af6867
00AF4DB1  41 8A 4E 04                     mov cl, byte ptr [r14 + 4]
00AF4DB5  88 4C 24 30                     mov byte ptr [rsp + 0x30], cl
00AF4DB9  45 8B 0E                        mov r9d, dword ptr [r14]
00AF4DBC  4C 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], r9
00AF4DC4  4D 85 C9                        test r9, r9
00AF4DC7  74 AA                           je 0x140af4d73
00AF4DC9  8B 05 D1 1C 4D 00               mov eax, dword ptr [rip + 0x4d1cd1]
00AF4DCF  49 B8 00 03 00 00 80 F7 FF FF   movabs r8, 0xfffff78000000300
00AF4DD9  49 0F AF 00                     imul rax, qword ptr [r8]
00AF4DDD  33 D2                           xor edx, edx
00AF4DDF  49 F7 F1                        div r9
00AF4DE2  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00AF4DEA  EB 91                           jmp 0x140af4d7d
00AF4DEC  E9 78 1A 00 00                  jmp 0x140af6869
00AF4DF1  83 EB 1E                        sub ebx, 0x1e
00AF4DF4  0F 84 34 03 00 00               je 0x140af512e
00AF4DFA  83 EB 01                        sub ebx, 1
00AF4DFD  0F 84 18 03 00 00               je 0x140af511b
00AF4E03  83 EB 03                        sub ebx, 3
00AF4E06  0F 84 72 02 00 00               je 0x140af507e
00AF4E0C  83 EB 03                        sub ebx, 3
00AF4E0F  0F 84 36 02 00 00               je 0x140af504b
00AF4E15  83 FB 01                        cmp ebx, 1
00AF4E18  0F 85 93 03 00 00               jne 0x140af51b1
00AF4E1E  41 8D 47 F0                     lea eax, [r15 - 0x10]
00AF4E22  A9 F7 FF FF FF                  test eax, 0xfffffff7
00AF4E27  0F 85 8A 19 00 00               jne 0x140af67b7
00AF4E2D  45 84 E4                        test r12b, r12b
00AF4E30  0F 84 53 01 00 00               je 0x140af4f89
00AF4E36  89 B4 24 88 00 00 00            mov dword ptr [rsp + 0x88], esi
00AF4E3D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF4E46  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00AF4E4D  8B 81 DC 07 00 00               mov eax, dword ptr [rcx + 0x7dc]
00AF4E53  A8 08                           test al, 8
00AF4E55  0F 84 79 19 00 00               je 0x140af67d4
00AF4E5B  41 8A D5                        mov dl, r13b
00AF4E5E  48 8B 0D BB 4C 4E 00            mov rcx, qword ptr [rip + 0x4e4cbb]
00AF4E65  E8 B6 CF D7 FF                  call 0x140871e20
00AF4E6A  84 C0                           test al, al
00AF4E6C  0F 84 62 19 00 00               je 0x140af67d4
00AF4E72  41 83 FF 10                     cmp r15d, 0x10
00AF4E76  75 48                           jne 0x140af4ec0
00AF4E78  0F 57 C0                        xorps xmm0, xmm0
00AF4E7B  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
00AF4E83  49 8B CE                        mov rcx, r14
00AF4E86  E8 7D 0F C1 FF                  call 0x140705e08
00AF4E8B  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
00AF4E92  49 8D 4E 08                     lea rcx, [r14 + 8]
00AF4E96  E8 31 0F C1 FF                  call 0x140705dcc
00AF4E9B  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00AF4EA3  0F 28 84 24 A0 00 00 00         movaps xmm0, xmmword ptr [rsp + 0xa0]
00AF4EAB  66 0F 7F 44 24 60               movdqa xmmword ptr [rsp + 0x60], xmm0
00AF4EB1  44 8B B4 24 88 00 00 00         mov r14d, dword ptr [rsp + 0x88]
00AF4EB9  EB 39                           jmp 0x140af4ef4
00AF4EBB  E9 A9 19 00 00                  jmp 0x140af6869
00AF4EC0  41 B8 18 00 00 00               mov r8d, 0x18
00AF4EC6  49 8B D6                        mov rdx, r14
00AF4EC9  48 8D 8C 24 A0 01 00 00         lea rcx, [rsp + 0x1a0]
00AF4ED1  E8 12 8C A0 FF                  call 0x1404fdae8
00AF4ED6  0F 10 84 24 A8 01 00 00         movups xmm0, xmmword ptr [rsp + 0x1a8]
00AF4EDE  F3 0F 7F 44 24 60               movdqu xmmword ptr [rsp + 0x60], xmm0
00AF4EE4  44 8B B4 24 A0 01 00 00         mov r14d, dword ptr [rsp + 0x1a0]
00AF4EEC  44 89 B4 24 88 00 00 00         mov dword ptr [rsp + 0x88], r14d
00AF4EF4  BB 3E 00 00 00                  mov ebx, 0x3e
00AF4EF9  66 39 5C 24 60                  cmp word ptr [rsp + 0x60], bx
00AF4EFE  0F 85 D0 18 00 00               jne 0x140af67d4
00AF4F04  44 8B C3                        mov r8d, ebx
00AF4F07  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00AF4F0C  48 8D 8C 24 A0 01 00 00         lea rcx, [rsp + 0x1a0]
00AF4F14  E8 CF 8B A0 FF                  call 0x1404fdae8
00AF4F19  90                              nop
00AF4F1A  4C 8B C3                        mov r8, rbx
00AF4F1D  48 8D 3D BC 3B 54 FF            lea rdi, [rip - 0xabc444]
00AF4F24  48 8B D7                        mov rdx, rdi
00AF4F27  48 8D 8C 24 A0 01 00 00         lea rcx, [rsp + 0x1a0]
00AF4F2F  E8 DC 1B BD FF                  call 0x1406c6b10
00AF4F34  85 C0                           test eax, eax
00AF4F36  0F 85 98 18 00 00               jne 0x140af67d4
00AF4F3C  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
00AF4F41  66 89 5C 24 62                  mov word ptr [rsp + 0x62], bx
00AF4F46  48 89 BC 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], rdi
00AF4F4E  66 89 9C 24 AA 01 00 00         mov word ptr [rsp + 0x1aa], bx
00AF4F56  41 83 FF 10                     cmp r15d, 0x10
00AF4F5A  44 0F 44 F6                     cmove r14d, esi
00AF4F5E  44 89 B4 24 A0 01 00 00         mov dword ptr [rsp + 0x1a0], r14d
00AF4F66  44 8D 40 18                     lea r8d, [rax + 0x18]
00AF4F6A  48 8D 94 24 A0 01 00 00         lea rdx, [rsp + 0x1a0]
00AF4F72  8D 48 26                        lea ecx, [rax + 0x26]
00AF4F75  E8 F6 B8 BB FF                  call 0x1406b0870
00AF4F7A  E9 EA 18 00 00                  jmp 0x140af6869
00AF4F7F  E9 E5 18 00 00                  jmp 0x140af6869
00AF4F84  E9 E0 18 00 00                  jmp 0x140af6869
00AF4F89  41 83 FF 10                     cmp r15d, 0x10
00AF4F8D  75 0B                           jne 0x140af4f9a
00AF4F8F  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
00AF4F93  44 8B 74 24 54                  mov r14d, dword ptr [rsp + 0x54]
00AF4F98  EB 15                           jmp 0x140af4faf
00AF4F9A  41 0F 10 46 08                  movups xmm0, xmmword ptr [r14 + 8]
00AF4F9F  45 84 2E                        test byte ptr [r14], r13b
00AF4FA2  44 8B 74 24 54                  mov r14d, dword ptr [rsp + 0x54]
00AF4FA7  45 0F B6 F6                     movzx r14d, r14b
00AF4FAB  45 0F 45 F5                     cmovne r14d, r13d
00AF4FAF  F3 0F 7F 44 24 60               movdqu xmmword ptr [rsp + 0x60], xmm0
00AF4FB5  41 B8 3E 00 00 00               mov r8d, 0x3e
00AF4FBB  48 8D 15 1E 3B 54 FF            lea rdx, [rip - 0xabc4e2]
00AF4FC2  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00AF4FC7  E8 44 1B BD FF                  call 0x1406c6b10
00AF4FCC  85 C0                           test eax, eax
00AF4FCE  0F 85 E7 09 00 00               jne 0x140af59bb
00AF4FD4  48 8B 05 F5 17 41 00            mov rax, qword ptr [rip + 0x4117f5]
00AF4FDB  48 8B 58 30                     mov rbx, qword ptr [rax + 0x30]
00AF4FDF  48 8B CB                        mov rcx, rbx
00AF4FE2  E8 79 EB 94 FF                  call 0x140443b60
00AF4FE7  48 85 C0                        test rax, rax
00AF4FEA  75 16                           jne 0x140af5002
00AF4FEC  48 8B 0D DD 17 41 00            mov rcx, qword ptr [rip + 0x4117dd]
00AF4FF3  E8 68 DF FA FF                  call 0x140aa2f60
00AF4FF8  B8 7B 00 00 C0                  mov eax, 0xc000007b
00AF4FFD  E9 67 18 00 00                  jmp 0x140af6869
00AF5002  8B 48 28                        mov ecx, dword ptr [rax + 0x28]
00AF5005  48 03 CB                        add rcx, rbx
00AF5008  45 8A C6                        mov r8b, r14b
00AF500B  48 8B D3                        mov rdx, rbx
00AF500E  E8 C1 F9 FF FF                  call 0x140af49d4
00AF5013  8B F8                           mov edi, eax
00AF5015  85 C0                           test eax, eax
00AF5017  0F 89 4A 18 00 00               jns 0x140af6867
00AF501D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00AF5026  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00AF502D  E8 BE A8 73 FF                  call 0x14022f8f0
00AF5032  85 C0                           test eax, eax
00AF5034  0F 85 2D 18 00 00               jne 0x140af6867
00AF503A  48 8B 0D 8F 17 41 00            mov rcx, qword ptr [rip + 0x41178f]
00AF5041  E8 1A DF FA FF                  call 0x140aa2f60
00AF5046  E9 1C 18 00 00                  jmp 0x140af6867
00AF504B  41 83 FF 10                     cmp r15d, 0x10
00AF504F  0F 85 62 17 00 00               jne 0x140af67b7
00AF5055  45 84 E4                        test r12b, r12b
00AF5058  74 17                           je 0x140af5071
00AF505A  41 8A D4                        mov dl, r12b
00AF505D  48 8B 0D 0C 4B 4E 00            mov rcx, qword ptr [rip + 0x4e4b0c]
00AF5064  E8 B7 CD D7 FF                  call 0x140871e20
00AF5069  84 C0                           test al, al
00AF506B  0F 84 63 17 00 00               je 0x140af67d4
00AF5071  49 8B CE                        mov rcx, r14
00AF5074  E8 63 D1 CE FF                  call 0x1407e21dc
00AF5079  E9 E7 17 00 00                  jmp 0x140af6865
00AF507E  45 84 E4                        test r12b, r12b
00AF5081  74 17                           je 0x140af509a
00AF5083  41 8A D4                        mov dl, r12b
00AF5086  48 8B 0D F3 49 4E 00            mov rcx, qword ptr [rip + 0x4e49f3]
00AF508D  E8 8E CD D7 FF                  call 0x140871e20
00AF5092  84 C0                           test al, al
00AF5094  0F 84 3A 17 00 00               je 0x140af67d4
00AF509A  E8 41 12 94 FF                  call 0x1404362e0
00AF509F  84 C0                           test al, al
00AF50A1  0F 85 2D 17 00 00               jne 0x140af67d4
00AF50A7  41 83 FF 04                     cmp r15d, 4
00AF50AB  74 0F                           je 0x140af50bc
00AF50AD  33 D2                           xor edx, edx
00AF50AF  41 8B CD                        mov ecx, r13d
00AF50B2  E8 FD CB A9 FF                  call 0x140591cb4
00AF50B7  E9 A9 17 00 00                  jmp 0x140af6865
00AF50BC  45 84 E4                        test r12b, r12b
00AF50BF  74 35                           je 0x140af50f6
00AF50C1  41 F6 C6 03                     test r14b, 3
00AF50C5  0F 85 C8 17 00 00               jne 0x140af6893
00AF50CB  49 8D 4E 04                     lea rcx, [r14 + 4]
00AF50CF  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00AF50D9  48 3B C8                        cmp rcx, rax
00AF50DC  77 05                           ja 0x140af50e3
00AF50DE  49 3B CE                        cmp rcx, r14
00AF50E1  73 02                           jae 0x140af50e5
00AF50E3  8A 00                           mov al, byte ptr [rax]
00AF50E5  41 8B 0E                        mov ecx, dword ptr [r14]
00AF50E8  89 8C 24 24 01 00 00            mov dword ptr [rsp + 0x124], ecx
00AF50EF  EB 08                           jmp 0x140af50f9
00AF50F1  E9 73 17 00 00                  jmp 0x140af6869
00AF50F6  41 8B 0E                        mov ecx, dword ptr [r14]
00AF50F9  85 C9                           test ecx, ecx
00AF50FB  74 18                           je 0x140af5115
00AF50FD  83 E9 01                        sub ecx, 1
00AF5100  74 AB                           je 0x140af50ad
00AF5102  83 F9 01                        cmp ecx, 1
00AF5105  0F 85 5B 14 00 00               jne 0x140af6566
00AF510B  E8 6C 36 CE FF                  call 0x1407d877c
00AF5110  E9 50 17 00 00                  jmp 0x140af6865
00AF5115  33 D2                           xor edx, edx
00AF5117  33 C9                           xor ecx, ecx
00AF5119  EB 97                           jmp 0x140af50b2
00AF511B  45 8A C4                        mov r8b, r12b
00AF511E  41 8B D7                        mov edx, r15d
00AF5121  49 8B CE                        mov rcx, r14
00AF5124  E8 FF E7 F5 FF                  call 0x140a53928
00AF5129  E9 37 17 00 00                  jmp 0x140af6865
00AF512E  E8 1D 7A D0 FF                  call 0x1407fcb50
00AF5133  E9 2D 17 00 00                  jmp 0x140af6865
00AF5138  41 83 FF 04                     cmp r15d, 4
00AF513C  0F 85 75 16 00 00               jne 0x140af67b7
00AF5142  41 8A D4                        mov dl, r12b
00AF5145  48 8B 0D 2C 49 4E 00            mov rcx, qword ptr [rip + 0x4e492c]
00AF514C  E8 CF CC D7 FF                  call 0x140871e20
00AF5151  84 C0                           test al, al
00AF5153  0F 84 7B 16 00 00               je 0x140af67d4
00AF5159  41 8B 16                        mov edx, dword ptr [r14]
00AF515C  89 94 24 28 01 00 00            mov dword ptr [rsp + 0x128], edx
00AF5163  41 8A CD                        mov cl, r13b
00AF5166  E8 05 6D F4 FF                  call 0x140a3be70
00AF516B  8B FE                           mov edi, esi
00AF516D  E9 F5 16 00 00                  jmp 0x140af6867
00AF5172  E9 F2 16 00 00                  jmp 0x140af6869
00AF5177  83 FB 33                        cmp ebx, 0x33
00AF517A  0F 8F 74 01 00 00               jg 0x140af52f4
00AF5180  0F 84 44 01 00 00               je 0x140af52ca
00AF5186  8B CB                           mov ecx, ebx
00AF5188  83 E9 28                        sub ecx, 0x28
00AF518B  0F 84 C3 00 00 00               je 0x140af5254
00AF5191  83 E9 01                        sub ecx, 1
00AF5194  0F 84 BA 00 00 00               je 0x140af5254
00AF519A  83 E9 05                        sub ecx, 5
00AF519D  74 1C                           je 0x140af51bb
00AF519F  83 E9 01                        sub ecx, 1
00AF51A2  0F 84 6C 03 00 00               je 0x140af5514
00AF51A8  83 F9 01                        cmp ecx, 1
00AF51AB  0F 84 63 03 00 00               je 0x140af5514
00AF51B1  BF 03 00 00 C0                  mov edi, 0xc0000003
00AF51B6  E9 AC 16 00 00                  jmp 0x140af6867
00AF51BB  41 83 FF 08                     cmp r15d, 8
00AF51BF  0F 85 F2 15 00 00               jne 0x140af67b7
00AF51C5  45 84 E4                        test r12b, r12b
00AF51C8  74 17                           je 0x140af51e1
00AF51CA  41 8A D4                        mov dl, r12b
00AF51CD  48 8B 0D 0C 4A 4E 00            mov rcx, qword ptr [rip + 0x4e4a0c]
00AF51D4  E8 47 CC D7 FF                  call 0x140871e20
00AF51D9  84 C0                           test al, al
00AF51DB  0F 84 F3 15 00 00               je 0x140af67d4
00AF51E1  E8 FA 10 94 FF                  call 0x1404362e0
00AF51E6  84 C0                           test al, al
00AF51E8  0F 85 A7 14 00 00               jne 0x140af6695
00AF51EE  49 8B 0E                        mov rcx, qword ptr [r14]
00AF51F1  48 89 8C 24 10 01 00 00         mov qword ptr [rsp + 0x110], rcx
00AF51F9  48 85 C9                        test rcx, rcx
00AF51FC  75 07                           jne 0x140af5205
00AF51FE  48 8B CE                        mov rcx, rsi
00AF5201  8B FE                           mov edi, esi
00AF5203  EB 40                           jmp 0x140af5245
00AF5205  4C 8B 05 74 19 4D 00            mov r8, qword ptr [rip + 0x4d1974]
00AF520C  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
00AF5214  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00AF5219  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00AF5221  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AF5226  45 8A CC                        mov r9b, r12b
00AF5229  BA 02 00 00 00                  mov edx, 2
00AF522E  E8 7D 3B D7 FF                  call 0x140868db0
00AF5233  8B F8                           mov edi, eax
00AF5235  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00AF523D  85 C0                           test eax, eax
00AF523F  0F 88 22 16 00 00               js 0x140af6867
00AF5245  E8 D2 B9 AB FF                  call 0x1405b0c1c
00AF524A  E9 18 16 00 00                  jmp 0x140af6867
00AF524F  E9 15 16 00 00                  jmp 0x140af6869
00AF5254  41 83 FF 10                     cmp r15d, 0x10
00AF5258  0F 85 59 15 00 00               jne 0x140af67b7
00AF525E  45 84 E4                        test r12b, r12b
00AF5261  74 3F                           je 0x140af52a2
00AF5263  41 8A D4                        mov dl, r12b
00AF5266  48 8B 0D 13 48 4E 00            mov rcx, qword ptr [rip + 0x4e4813]
00AF526D  E8 AE CB D7 FF                  call 0x140871e20
00AF5272  84 C0                           test al, al
00AF5274  0F 84 5A 15 00 00               je 0x140af67d4
00AF527A  45 8B C5                        mov r8d, r13d
00AF527D  49 8B D6                        mov rdx, r14
00AF5280  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00AF5285  E8 32 DD 09 00                  call 0x140b92fbc
00AF528A  85 C0                           test eax, eax
00AF528C  0F 88 D7 15 00 00               js 0x140af6869
00AF5292  4C 8D 74 24 60                  lea r14, [rsp + 0x60]
00AF5297  66 39 74 24 60                  cmp word ptr [rsp + 0x60], si
00AF529C  0F 84 7B 13 00 00               je 0x140af661d
00AF52A2  83 EB 28                        sub ebx, 0x28
00AF52A5  74 16                           je 0x140af52bd
00AF52A7  83 FB 01                        cmp ebx, 1
00AF52AA  0F 85 84 13 00 00               jne 0x140af6634
00AF52B0  49 8B CE                        mov rcx, r14
00AF52B3  E8 0C 72 0B 00                  call 0x140bac4c4
00AF52B8  E9 90 13 00 00                  jmp 0x140af664d
00AF52BD  49 8B CE                        mov rcx, r14
00AF52C0  E8 57 70 0B 00                  call 0x140bac31c
00AF52C5  E9 83 13 00 00                  jmp 0x140af664d
00AF52CA  41 8A D4                        mov dl, r12b
00AF52CD  48 8B 0D AC 47 4E 00            mov rcx, qword ptr [rip + 0x4e47ac]
00AF52D4  E8 47 CB D7 FF                  call 0x140871e20
00AF52D9  84 C0                           test al, al
00AF52DB  0F 84 B4 13 00 00               je 0x140af6695
00AF52E1  45 33 C0                        xor r8d, r8d
00AF52E4  41 8B D7                        mov edx, r15d
00AF52E7  49 8B CE                        mov rcx, r14
00AF52EA  E8 FD 71 0B 00                  call 0x140bac4ec
00AF52EF  E9 71 15 00 00                  jmp 0x140af6865
00AF52F4  83 FB 36                        cmp ebx, 0x36
00AF52F7  74 6C                           je 0x140af5365
00AF52F9  83 FB 38                        cmp ebx, 0x38
00AF52FC  74 54                           je 0x140af5352
00AF52FE  83 FB 3B                        cmp ebx, 0x3b
00AF5301  74 13                           je 0x140af5316
00AF5303  83 FB 45                        cmp ebx, 0x45
00AF5306  0F 85 A5 FE FF FF               jne 0x140af51b1
00AF530C  BF BB 00 00 C0                  mov edi, 0xc00000bb
00AF5311  E9 51 15 00 00                  jmp 0x140af6867
00AF5316  41 83 FF 04                     cmp r15d, 4
00AF531A  0F 85 97 14 00 00               jne 0x140af67b7
00AF5320  41 8B 1E                        mov ebx, dword ptr [r14]
00AF5323  89 9C 24 00 01 00 00            mov dword ptr [rsp + 0x100], ebx
00AF532A  8B CB                           mov ecx, ebx
00AF532C  E8 4F 02 CD FF                  call 0x1407c5580
00AF5331  8B F8                           mov edi, eax
00AF5333  85 C0                           test eax, eax
00AF5335  0F 88 2C 15 00 00               js 0x140af6867
00AF533B  48 8B 05 C6 FC 4C 00            mov rax, qword ptr [rip + 0x4cfcc6]
00AF5342  89 98 E0 02 00 00               mov dword ptr [rax + 0x2e0], ebx
00AF5348  E9 1A 15 00 00                  jmp 0x140af6867
00AF534D  E9 17 15 00 00                  jmp 0x140af6869
00AF5352  45 8A CC                        mov r9b, r12b
00AF5355  45 8B C7                        mov r8d, r15d
00AF5358  49 8B D6                        mov rdx, r14
00AF535B  E8 3C C0 E6 FF                  call 0x14096139c
00AF5360  E9 00 15 00 00                  jmp 0x140af6865
00AF5365  8B C6                           mov eax, esi
00AF5367  EB 04                           jmp 0x140af536d
00AF5369  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00AF536D  41 83 FF 30                     cmp r15d, 0x30
00AF5371  75 05                           jne 0x140af5378
00AF5373  44 8A FE                        mov r15b, sil
00AF5376  EB 0D                           jmp 0x140af5385
00AF5378  41 83 FF 38                     cmp r15d, 0x38
00AF537C  0F 85 35 14 00 00               jne 0x140af67b7
00AF5382  45 8A FD                        mov r15b, r13b
00AF5385  45 84 E4                        test r12b, r12b
00AF5388  0F 85 46 14 00 00               jne 0x140af67d4
00AF538E  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
00AF5392  F3 0F 7F 44 24 60               movdqu xmmword ptr [rsp + 0x60], xmm0
00AF5398  48 8D 8C 24 B8 00 00 00         lea rcx, [rsp + 0xb8]
00AF53A0  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00AF53A5  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
00AF53AD  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00AF53B2  44 8B C8                        mov r9d, eax
00AF53B5  45 33 C0                        xor r8d, r8d
00AF53B8  33 D2                           xor edx, edx
00AF53BA  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00AF53BF  E8 DC 55 EA FF                  call 0x14099a9a0
00AF53C4  8B F8                           mov edi, eax
00AF53C6  85 C0                           test eax, eax
00AF53C8  78 73                           js 0x140af543d
00AF53CA  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
00AF53D2  45 84 FF                        test r15b, r15b
00AF53D5  74 1B                           je 0x140af53f2
00AF53D7  45 33 C0                        xor r8d, r8d
00AF53DA  4C 8D 8C 24 A0 00 00 00         lea r9, [rsp + 0xa0]
00AF53E2  41 8A D5                        mov dl, r13b
00AF53E5  48 8B CB                        mov rcx, rbx
00AF53E8  E8 E3 D4 93 FF                  call 0x1404328d0
00AF53ED  4C 8B E0                        mov r12, rax
00AF53F0  EB 03                           jmp 0x140af53f5
00AF53F2  4C 8B E6                        mov r12, rsi
00AF53F5  48 8B CB                        mov rcx, rbx
00AF53F8  E8 63 E7 94 FF                  call 0x140443b60
00AF53FD  90                              nop
00AF53FE  8B 50 28                        mov edx, dword ptr [rax + 0x28]
00AF5401  48 03 D3                        add rdx, rbx
00AF5404  49 89 5E 10                     mov qword ptr [r14 + 0x10], rbx
00AF5408  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00AF5410  49 89 4E 18                     mov qword ptr [r14 + 0x18], rcx
00AF5414  49 89 56 20                     mov qword ptr [r14 + 0x20], rdx
00AF5418  45 84 FF                        test r15b, r15b
00AF541B  74 0D                           je 0x140af542a
00AF541D  4D 89 66 28                     mov qword ptr [r14 + 0x28], r12
00AF5421  8B 40 50                        mov eax, dword ptr [rax + 0x50]
00AF5424  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
00AF5428  EB 07                           jmp 0x140af5431
00AF542A  8B 40 50                        mov eax, dword ptr [rax + 0x50]
00AF542D  41 89 46 28                     mov dword ptr [r14 + 0x28], eax
00AF5431  E9 31 14 00 00                  jmp 0x140af6867
00AF5436  8B F8                           mov edi, eax
00AF5438  E9 2A 14 00 00                  jmp 0x140af6867
00AF543D  3D 9D 01 00 C0                  cmp eax, 0xc000019d
00AF5442  0F 85 1F 14 00 00               jne 0x140af6867
00AF5448  BF 0E 01 00 C0                  mov edi, 0xc000010e
00AF544D  E9 15 14 00 00                  jmp 0x140af6867
00AF5452  E9 12 14 00 00                  jmp 0x140af6869
00AF5457  83 FB 5C                        cmp ebx, 0x5c
00AF545A  0F 8F 1E 04 00 00               jg 0x140af587e
00AF5460  0F 84 EA 03 00 00               je 0x140af5850
00AF5466  83 FB 51                        cmp ebx, 0x51
00AF5469  0F 8F F5 01 00 00               jg 0x140af5664
00AF546F  0F 84 4A 01 00 00               je 0x140af55bf
00AF5475  8B CB                           mov ecx, ebx
00AF5477  83 E9 48                        sub ecx, 0x48
00AF547A  0F 84 9E 00 00 00               je 0x140af551e
00AF5480  83 E9 02                        sub ecx, 2
00AF5483  0F 84 8B 00 00 00               je 0x140af5514
00AF5489  83 E9 01                        sub ecx, 1
00AF548C  74 73                           je 0x140af5501
00AF548E  83 E9 04                        sub ecx, 4
00AF5491  74 59                           je 0x140af54ec
00AF5493  83 F9 01                        cmp ecx, 1
00AF5496  0F 85 15 FD FF FF               jne 0x140af51b1
00AF549C  41 83 FF 04                     cmp r15d, 4
00AF54A0  73 0A                           jae 0x140af54ac
00AF54A2  BF 04 00 00 C0                  mov edi, 0xc0000004
00AF54A7  E9 BB 13 00 00                  jmp 0x140af6867
00AF54AC  8B FE                           mov edi, esi
00AF54AE  C7 84 24 98 00 00 00 06 00 00 00  mov dword ptr [rsp + 0x98], 6
00AF54B9  41 8B 0E                        mov ecx, dword ptr [r14]
00AF54BC  89 8C 24 98 00 00 00            mov dword ptr [rsp + 0x98], ecx
00AF54C3  EB 0E                           jmp 0x140af54d3
00AF54C5  8B F8                           mov edi, eax
00AF54C7  44 8A 64 24 38                  mov r12b, byte ptr [rsp + 0x38]
00AF54CC  8B 8C 24 98 00 00 00            mov ecx, dword ptr [rsp + 0x98]
00AF54D3  85 FF                           test edi, edi
00AF54D5  0F 88 8C 13 00 00               js 0x140af6867
00AF54DB  49 83 C8 FF                     or r8, 0xffffffffffffffff
00AF54DF  41 8A D4                        mov dl, r12b
00AF54E2  E8 C9 93 D0 FF                  call 0x1407fe8b0
00AF54E7  E9 79 13 00 00                  jmp 0x140af6865
00AF54EC  45 8A CC                        mov r9b, r12b
00AF54EF  45 8B C7                        mov r8d, r15d
00AF54F2  49 8B D6                        mov rdx, r14
00AF54F5  8B CB                           mov ecx, ebx
00AF54F7  E8 EC 91 FE FF                  call 0x140ade6e8
00AF54FC  E9 64 13 00 00                  jmp 0x140af6865
00AF5501  45 8A C4                        mov r8b, r12b
00AF5504  41 8B D7                        mov edx, r15d
00AF5507  49 8B CE                        mov rcx, r14
00AF550A  E8 3D FB CC FF                  call 0x1407c504c
00AF550F  E9 51 13 00 00                  jmp 0x140af6865
00AF5514  B8 02 00 00 C0                  mov eax, 0xc0000002
00AF5519  E9 4B 13 00 00                  jmp 0x140af6869
00AF551E  45 84 E4                        test r12b, r12b
00AF5521  0F 85 3F 10 00 00               jne 0x140af6566
00AF5527  4D 85 F6                        test r14, r14
00AF552A  0F 84 36 10 00 00               je 0x140af6566
00AF5530  41 83 FF 08                     cmp r15d, 8
00AF5534  0F 85 2C 10 00 00               jne 0x140af6566
00AF553A  41 8B 0E                        mov ecx, dword ptr [r14]
00AF553D  85 C9                           test ecx, ecx
00AF553F  0F 84 C7 FD FF FF               je 0x140af530c
00AF5545  83 E9 01                        sub ecx, 1
00AF5548  74 64                           je 0x140af55ae
00AF554A  83 E9 01                        sub ecx, 1
00AF554D  74 56                           je 0x140af55a5
00AF554F  83 E9 01                        sub ecx, 1
00AF5552  74 48                           je 0x140af559c
00AF5554  83 E9 01                        sub ecx, 1
00AF5557  0F 84 AF FD FF FF               je 0x140af530c
00AF555D  83 E9 02                        sub ecx, 2
00AF5560  74 26                           je 0x140af5588
00AF5562  83 F9 01                        cmp ecx, 1
00AF5565  0F 85 77 0C 00 00               jne 0x140af61e2
00AF556B  8B FE                           mov edi, esi
00AF556D  B9 02 00 00 C0                  mov ecx, 0xc0000002
00AF5572  48 8D 15 87 70 A0 FF            lea rdx, [rip - 0x5f8f79]
00AF5579  48 39 15 B8 B5 30 00            cmp qword ptr [rip + 0x30b5b8], rdx
00AF5580  0F 44 F9                        cmove edi, ecx
00AF5583  E9 DF 12 00 00                  jmp 0x140af6867
00AF5588  48 8B 05 A9 B5 30 00            mov rax, qword ptr [rip + 0x30b5a9]
00AF558F  41 8A CD                        mov cl, r13b
00AF5592  E8 39 55 BC FF                  call 0x1406baad0
00AF5597  E9 C9 12 00 00                  jmp 0x140af6865
00AF559C  48 8B 05 75 B5 30 00            mov rax, qword ptr [rip + 0x30b575]
00AF55A3  EB 10                           jmp 0x140af55b5
00AF55A5  48 8B 05 7C B5 30 00            mov rax, qword ptr [rip + 0x30b57c]
00AF55AC  EB 07                           jmp 0x140af55b5
00AF55AE  48 8B 05 6B B5 30 00            mov rax, qword ptr [rip + 0x30b56b]
00AF55B5  E8 16 55 BC FF                  call 0x1406baad0
00AF55BA  E9 AC FB FF FF                  jmp 0x140af516b
00AF55BF  40 88 74 24 39                  mov byte ptr [rsp + 0x39], sil
00AF55C4  41 83 FF 40                     cmp r15d, 0x40
00AF55C8  0F 82 E9 11 00 00               jb 0x140af67b7
00AF55CE  83 FB 15                        cmp ebx, 0x15
00AF55D1  75 0B                           jne 0x140af55de
00AF55D3  8B DE                           mov ebx, esi
00AF55D5  89 9C 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], ebx
00AF55DC  EB 25                           jmp 0x140af5603
00AF55DE  41 8B 5E 3C                     mov ebx, dword ptr [r14 + 0x3c]
00AF55E2  89 9C 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], ebx
00AF55E9  F7 C3 F0 FF FF FF               test ebx, 0xfffffff0
00AF55EF  75 64                           jne 0x140af5655
00AF55F1  8B C3                           mov eax, ebx
00AF55F3  83 E0 0C                        and eax, 0xc
00AF55F6  3C 0C                           cmp al, 0xc
00AF55F8  74 5B                           je 0x140af5655
00AF55FA  8B C3                           mov eax, ebx
00AF55FC  83 E0 03                        and eax, 3
00AF55FF  3C 03                           cmp al, 3
00AF5601  74 52                           je 0x140af5655
00AF5603  41 8A D4                        mov dl, r12b
00AF5606  48 8B 0D 63 45 4E 00            mov rcx, qword ptr [rip + 0x4e4563]
00AF560D  E8 0E C8 D7 FF                  call 0x140871e20
00AF5612  84 C0                           test al, al
00AF5614  0F 84 7B 10 00 00               je 0x140af6695
00AF561A  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
00AF561E  48 89 8C 24 78 01 00 00         mov qword ptr [rsp + 0x178], rcx
00AF5626  49 8B 56 20                     mov rdx, qword ptr [r14 + 0x20]
00AF562A  48 89 94 24 80 01 00 00         mov qword ptr [rsp + 0x180], rdx
00AF5632  48 8D 44 24 39                  lea rax, [rsp + 0x39]
00AF5637  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AF563C  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00AF5640  45 8A CD                        mov r9b, r13b
00AF5643  45 8B C5                        mov r8d, r13d
00AF5646  E8 89 82 98 FF                  call 0x14047d8d4
00AF564B  E9 19 12 00 00                  jmp 0x140af6869
00AF5650  E9 14 12 00 00                  jmp 0x140af6869
00AF5655  B8 F0 00 00 C0                  mov eax, 0xc00000f0
00AF565A  E9 0A 12 00 00                  jmp 0x140af6869
00AF565F  E9 05 12 00 00                  jmp 0x140af6869
00AF5664  83 EB 52                        sub ebx, 0x52
00AF5667  0F 84 22 01 00 00               je 0x140af578f
00AF566D  83 EB 04                        sub ebx, 4
00AF5670  0F 84 09 01 00 00               je 0x140af577f
00AF5676  83 EB 01                        sub ebx, 1
00AF5679  0F 84 AD 00 00 00               je 0x140af572c
00AF567F  83 EB 02                        sub ebx, 2
00AF5682  74 38                           je 0x140af56bc
00AF5684  83 FB 02                        cmp ebx, 2
00AF5687  0F 85 24 FB FF FF               jne 0x140af51b1
00AF568D  45 84 E4                        test r12b, r12b
00AF5690  0F 85 50 F6 FF FF               jne 0x140af4ce6
00AF5696  45 85 FF                        test r15d, r15d
00AF5699  74 0A                           je 0x140af56a5
00AF569B  BF F0 00 00 C0                  mov edi, 0xc00000f0
00AF56A0  E9 C2 11 00 00                  jmp 0x140af6867
00AF56A5  8A 05 EC 13 4D 00               mov al, byte ptr [rip + 0x4d13ec]
00AF56AB  F6 D8                           neg al
00AF56AD  1B FF                           sbb edi, edi
00AF56AF  F7 D7                           not edi
00AF56B1  81 E7 00 10 35 C0               and edi, 0xc0351000
00AF56B7  E9 AB 11 00 00                  jmp 0x140af6867
00AF56BC  45 3A E5                        cmp r12b, r13b
00AF56BF  0F 85 47 FC FF FF               jne 0x140af530c
00AF56C5  41 8A D5                        mov dl, r13b
00AF56C8  48 8B 0D A9 43 4E 00            mov rcx, qword ptr [rip + 0x4e43a9]
00AF56CF  E8 4C C7 D7 FF                  call 0x140871e20
00AF56D4  84 C0                           test al, al
00AF56D6  0F 84 36 11 00 00               je 0x140af6812
00AF56DC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF56E5  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00AF56EC  48 39 B1 10 03 00 00            cmp qword ptr [rcx + 0x310], rsi
00AF56F3  74 27                           je 0x140af571c
00AF56F5  0F B7 81 EC 06 00 00            movzx eax, word ptr [rcx + 0x6ec]
00AF56FC  B9 4C 01 00 00                  mov ecx, 0x14c
00AF5701  66 3B C1                        cmp ax, cx
00AF5704  74 0D                           je 0x140af5713
00AF5706  B9 C4 01 00 00                  mov ecx, 0x1c4
00AF570B  66 3B C1                        cmp ax, cx
00AF570E  74 03                           je 0x140af5713
00AF5710  44 8A EE                        mov r13b, sil
00AF5713  45 84 ED                        test r13b, r13b
00AF5716  0F 85 F0 FB FF FF               jne 0x140af530c
00AF571C  41 8B D7                        mov edx, r15d
00AF571F  49 8B CE                        mov rcx, r14
00AF5722  E8 75 6C FA FF                  call 0x140a9c39c
00AF5727  E9 39 11 00 00                  jmp 0x140af6865
00AF572C  41 8A D4                        mov dl, r12b
00AF572F  48 8B 0D 4A 43 4E 00            mov rcx, qword ptr [rip + 0x4e434a]
00AF5736  E8 E5 C6 D7 FF                  call 0x140871e20
00AF573B  84 C0                           test al, al
00AF573D  0F 84 A3 F5 FF FF               je 0x140af4ce6
00AF5743  41 83 FF 08                     cmp r15d, 8
00AF5747  0F 85 55 FD FF FF               jne 0x140af54a2
00AF574D  49 8B 06                        mov rax, qword ptr [r14]
00AF5750  48 89 84 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rax
00AF5758  8B 8C 24 A0 01 00 00            mov ecx, dword ptr [rsp + 0x1a0]
00AF575F  89 0D C3 14 4D 00               mov dword ptr [rip + 0x4d14c3], ecx
00AF5765  48 C1 E8 20                     shr rax, 0x20
00AF5769  0F B6 C8                        movzx ecx, al
00AF576C  41 23 CD                        and ecx, r13d
00AF576F  89 0D AF F9 4C 00               mov dword ptr [rip + 0x4cf9af], ecx
00AF5775  E9 ED 10 00 00                  jmp 0x140af6867
00AF577A  E9 EA 10 00 00                  jmp 0x140af6869
00AF577F  41 8B D7                        mov edx, r15d
00AF5782  49 8B CE                        mov rcx, r14
00AF5785  E8 26 A0 C5 FF                  call 0x14074f7b0
00AF578A  E9 D6 10 00 00                  jmp 0x140af6865
00AF578F  41 83 FF 18                     cmp r15d, 0x18
00AF5793  0F 82 1E 10 00 00               jb 0x140af67b7
00AF5799  41 8A D4                        mov dl, r12b
00AF579C  48 8B 0D 45 43 4E 00            mov rcx, qword ptr [rip + 0x4e4345]
00AF57A3  E8 78 C6 D7 FF                  call 0x140871e20
00AF57A8  84 C0                           test al, al
00AF57AA  0F 84 24 10 00 00               je 0x140af67d4
00AF57B0  45 84 E4                        test r12b, r12b
00AF57B3  74 2A                           je 0x140af57df
00AF57B5  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
00AF57B9  0F 29 84 24 A0 01 00 00         movaps xmmword ptr [rsp + 0x1a0], xmm0
00AF57C1  F2 41 0F 10 4E 10               movsd xmm1, qword ptr [r14 + 0x10]
00AF57C7  F2 0F 11 8C 24 B0 01 00 00      movsd qword ptr [rsp + 0x1b0], xmm1
00AF57D0  4C 8D B4 24 A0 01 00 00         lea r14, [rsp + 0x1a0]
00AF57D8  EB 05                           jmp 0x140af57df
00AF57DA  E9 8A 10 00 00                  jmp 0x140af6869
00AF57DF  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00AF57E3  41 2B C5                        sub eax, r13d
00AF57E6  83 F8 1E                        cmp eax, 0x1e
00AF57E9  0F 87 77 0D 00 00               ja 0x140af6566
00AF57EF  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
00AF57F3  F3 0F 7F 84 24 58 01 00 00      movdqu xmmword ptr [rsp + 0x158], xmm0
00AF57FC  4C 8D 84 24 C8 00 00 00         lea r8, [rsp + 0xc8]
00AF5804  33 D2                           xor edx, edx
00AF5806  48 8D 8C 24 58 01 00 00         lea rcx, [rsp + 0x158]
00AF580E  E8 0D 1C F4 FF                  call 0x140a37420
00AF5813  8B F8                           mov edi, eax
00AF5815  85 C0                           test eax, eax
00AF5817  0F 88 4A 10 00 00               js 0x140af6867
00AF581D  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
00AF5825  40 38 73 04                     cmp byte ptr [rbx + 4], sil
00AF5829  74 07                           je 0x140af5832
00AF582B  BF 4B 00 00 C0                  mov edi, 0xc000004b
00AF5830  EB 11                           jmp 0x140af5843
00AF5832  41 8B 56 10                     mov edx, dword ptr [r14 + 0x10]
00AF5836  48 8B CB                        mov rcx, rbx
00AF5839  E8 32 EB 8C FF                  call 0x1403c4370
00AF583E  BF 03 01 00 00                  mov edi, 0x103
00AF5843  48 8B CB                        mov rcx, rbx
00AF5846  E8 05 3B 80 FF                  call 0x1402f9350
00AF584B  E9 17 10 00 00                  jmp 0x140af6867
00AF5850  41 8A D4                        mov dl, r12b
00AF5853  48 8B 0D 26 42 4E 00            mov rcx, qword ptr [rip + 0x4e4226]
00AF585A  E8 C1 C5 D7 FF                  call 0x140871e20
00AF585F  84 C0                           test al, al
00AF5861  0F 84 2E 0E 00 00               je 0x140af6695
00AF5867  41 83 FF 28                     cmp r15d, 0x28
00AF586B  0F 85 46 0F 00 00               jne 0x140af67b7
00AF5871  49 8B CE                        mov rcx, r14
00AF5874  E8 AB 6D 0B 00                  call 0x140bac624
00AF5879  E9 E7 0F 00 00                  jmp 0x140af6865
00AF587E  83 FB 68                        cmp ebx, 0x68
00AF5881  0F 8F C2 01 00 00               jg 0x140af5a49
00AF5887  0F 84 A9 01 00 00               je 0x140af5a36
00AF588D  83 EB 5D                        sub ebx, 0x5d
00AF5890  0F 84 96 01 00 00               je 0x140af5a2c
00AF5896  83 EB 01                        sub ebx, 1
00AF5899  0F 84 26 01 00 00               je 0x140af59c5
00AF589F  83 EB 01                        sub ebx, 1
00AF58A2  0F 84 13 01 00 00               je 0x140af59bb
00AF58A8  83 EB 02                        sub ebx, 2
00AF58AB  74 46                           je 0x140af58f3
00AF58AD  B8 05 00 00 00                  mov eax, 5
00AF58B2  3B D8                           cmp ebx, eax
00AF58B4  0F 85 F7 F8 FF FF               jne 0x140af51b1
00AF58BA  BB B0 01 00 00                  mov ebx, 0x1b0
00AF58BF  44 3B FB                        cmp r15d, ebx
00AF58C2  0F 85 EF 0E 00 00               jne 0x140af67b7
00AF58C8  45 84 E4                        test r12b, r12b
00AF58CB  74 17                           je 0x140af58e4
00AF58CD  41 8A D4                        mov dl, r12b
00AF58D0  48 8B 0D 99 44 4E 00            mov rcx, qword ptr [rip + 0x4e4499]
00AF58D7  E8 44 C5 D7 FF                  call 0x140871e20
00AF58DC  84 C0                           test al, al
00AF58DE  0F 84 F0 0E 00 00               je 0x140af67d4
00AF58E4  8B D3                           mov edx, ebx
00AF58E6  49 8B CE                        mov rcx, r14
00AF58E9  E8 52 F9 CC FF                  call 0x1407c5240
00AF58EE  E9 72 0F 00 00                  jmp 0x140af6865
00AF58F3  41 83 FF 28                     cmp r15d, 0x28
00AF58F7  0F 85 BA 0E 00 00               jne 0x140af67b7
00AF58FD  45 84 E4                        test r12b, r12b
00AF5900  0F 84 90 00 00 00               je 0x140af5996
00AF5906  41 8A D4                        mov dl, r12b
00AF5909  48 8B 0D 70 41 4E 00            mov rcx, qword ptr [rip + 0x4e4170]
00AF5910  E8 0B C5 D7 FF                  call 0x140871e20
00AF5915  84 C0                           test al, al
00AF5917  0F 84 B7 0E 00 00               je 0x140af67d4
00AF591D  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
00AF5921  0F 29 84 24 A0 01 00 00         movaps xmmword ptr [rsp + 0x1a0], xmm0
00AF5929  41 0F 10 4E 10                  movups xmm1, xmmword ptr [r14 + 0x10]
00AF592E  0F 29 8C 24 B0 01 00 00         movaps xmmword ptr [rsp + 0x1b0], xmm1
00AF5936  F2 41 0F 10 46 20               movsd xmm0, qword ptr [r14 + 0x20]
00AF593C  F2 0F 11 84 24 C0 01 00 00      movsd qword ptr [rsp + 0x1c0], xmm0
00AF5945  41 8B D5                        mov edx, r13d
00AF5948  48 8D 8C 24 A8 01 00 00         lea rcx, [rsp + 0x1a8]
00AF5950  E8 A3 D6 09 00                  call 0x140b92ff8
00AF5955  85 C0                           test eax, eax
00AF5957  0F 88 0C 0F 00 00               js 0x140af6869
00AF595D  41 8B D5                        mov edx, r13d
00AF5960  48 8D 8C 24 B8 01 00 00         lea rcx, [rsp + 0x1b8]
00AF5968  E8 8B D6 09 00                  call 0x140b92ff8
00AF596D  8B D8                           mov ebx, eax
00AF596F  85 C0                           test eax, eax
00AF5971  79 14                           jns 0x140af5987
00AF5973  48 8D 8C 24 A8 01 00 00         lea rcx, [rsp + 0x1a8]
00AF597B  E8 D4 D4 09 00                  call 0x140b92e54
00AF5980  8B C3                           mov eax, ebx
00AF5982  E9 E2 0E 00 00                  jmp 0x140af6869
00AF5987  4C 8D B4 24 A0 01 00 00         lea r14, [rsp + 0x1a0]
00AF598F  EB 05                           jmp 0x140af5996
00AF5991  E9 D3 0E 00 00                  jmp 0x140af6869
00AF5996  49 8B CE                        mov rcx, r14
00AF5999  E8 46 0E 0B 00                  call 0x140ba67e4
00AF599E  8B F8                           mov edi, eax
00AF59A0  45 84 E4                        test r12b, r12b
00AF59A3  0F 84 BE 0E 00 00               je 0x140af6867
00AF59A9  49 8D 4E 08                     lea rcx, [r14 + 8]
00AF59AD  E8 A2 D4 09 00                  call 0x140b92e54
00AF59B2  49 8D 4E 18                     lea rcx, [r14 + 0x18]
00AF59B6  E9 A0 0C 00 00                  jmp 0x140af665b
00AF59BB  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00AF59C0  E9 A4 0E 00 00                  jmp 0x140af6869
00AF59C5  41 8A D4                        mov dl, r12b
00AF59C8  48 8B 0D A9 40 4E 00            mov rcx, qword ptr [rip + 0x4e40a9]
00AF59CF  E8 4C C4 D7 FF                  call 0x140871e20
00AF59D4  84 C0                           test al, al
00AF59D6  0F 84 0A F3 FF FF               je 0x140af4ce6
00AF59DC  41 83 FF 08                     cmp r15d, 8
00AF59E0  0F 85 BC FA FF FF               jne 0x140af54a2
00AF59E6  49 8B 06                        mov rax, qword ptr [r14]
00AF59E9  48 89 84 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rax
00AF59F1  48 8B 0D 10 F6 4C 00            mov rcx, qword ptr [rip + 0x4cf610]
00AF59F8  8B 84 24 A0 01 00 00            mov eax, dword ptr [rsp + 0x1a0]
00AF59FF  F0 09 81 A0 03 00 00            lock or dword ptr [rcx + 0x3a0], eax
00AF5A06  48 8B 84 24 A0 01 00 00         mov rax, qword ptr [rsp + 0x1a0]
00AF5A0E  48 C1 E8 20                     shr rax, 0x20
00AF5A12  F7 D0                           not eax
00AF5A14  48 8B 0D ED F5 4C 00            mov rcx, qword ptr [rip + 0x4cf5ed]
00AF5A1B  F0 21 81 A0 03 00 00            lock and dword ptr [rcx + 0x3a0], eax
00AF5A22  E9 40 0E 00 00                  jmp 0x140af6867
00AF5A27  E9 3D 0E 00 00                  jmp 0x140af6869
00AF5A2C  BB AC 00 00 00                  mov ebx, 0xac
00AF5A31  E9 89 FE FF FF                  jmp 0x140af58bf
00AF5A36  45 8A C4                        mov r8b, r12b
00AF5A39  41 8B D7                        mov edx, r15d
00AF5A3C  49 8B CE                        mov rcx, r14
00AF5A3F  E8 94 F7 CC FF                  call 0x1407c51d8
00AF5A44  E9 1C 0E 00 00                  jmp 0x140af6865
00AF5A49  83 EB 6A                        sub ebx, 0x6a
00AF5A4C  0F 84 5F F7 FF FF               je 0x140af51b1
00AF5A52  83 EB 03                        sub ebx, 3
00AF5A55  74 53                           je 0x140af5aaa
00AF5A57  83 EB 01                        sub ebx, 1
00AF5A5A  74 44                           je 0x140af5aa0
00AF5A5C  83 FB 01                        cmp ebx, 1
00AF5A5F  0F 85 4C F7 FF FF               jne 0x140af51b1
00AF5A65  41 83 FF 04                     cmp r15d, 4
00AF5A69  0F 85 48 0D 00 00               jne 0x140af67b7
00AF5A6F  41 8A D4                        mov dl, r12b
00AF5A72  48 8B 0D 8F 40 4E 00            mov rcx, qword ptr [rip + 0x4e408f]
00AF5A79  E8 A2 C3 D7 FF                  call 0x140871e20
00AF5A7E  84 C0                           test al, al
00AF5A80  0F 84 0F 0C 00 00               je 0x140af6695
00AF5A86  41 8B 0E                        mov ecx, dword ptr [r14]
00AF5A89  48 8B 05 78 F5 4C 00            mov rax, qword ptr [rip + 0x4cf578]
00AF5A90  89 88 48 02 00 00               mov dword ptr [rax + 0x248], ecx
00AF5A96  E9 D0 F6 FF FF                  jmp 0x140af516b
00AF5A9B  E9 C9 0D 00 00                  jmp 0x140af6869
00AF5AA0  BF 02 00 00 C0                  mov edi, 0xc0000002
00AF5AA5  E9 BD 0D 00 00                  jmp 0x140af6867
00AF5AAA  45 8A CC                        mov r9b, r12b
00AF5AAD  45 8B C7                        mov r8d, r15d
00AF5AB0  49 8B D6                        mov rdx, r14
00AF5AB3  E8 00 27 F8 FF                  call 0x140a781b8
00AF5AB8  E9 A8 0D 00 00                  jmp 0x140af6865
00AF5ABD  45 8A C4                        mov r8b, r12b
00AF5AC0  41 8B D7                        mov edx, r15d
00AF5AC3  49 8B CE                        mov rcx, r14
00AF5AC6  E8 2D CE AE FF                  call 0x1405e28f8
00AF5ACB  E9 95 0D 00 00                  jmp 0x140af6865
00AF5AD0  B8 C2 00 00 00                  mov eax, 0xc2
00AF5AD5  3B D8                           cmp ebx, eax
00AF5AD7  0F 8F F5 08 00 00               jg 0x140af63d2
00AF5ADD  0F 84 B6 08 00 00               je 0x140af6399
00AF5AE3  B8 9B 00 00 00                  mov eax, 0x9b
00AF5AE8  3B D8                           cmp ebx, eax
00AF5AEA  0F 8F 22 05 00 00               jg 0x140af6012
00AF5AF0  0F 84 12 05 00 00               je 0x140af6008
00AF5AF6  B8 84 00 00 00                  mov eax, 0x84
00AF5AFB  3B D8                           cmp ebx, eax
00AF5AFD  0F 8F 94 02 00 00               jg 0x140af5d97
00AF5B03  0F 84 A1 01 00 00               je 0x140af5caa
00AF5B09  83 EB 7E                        sub ebx, 0x7e
00AF5B0C  0F 84 78 01 00 00               je 0x140af5c8a
00AF5B12  83 EB 01                        sub ebx, 1
00AF5B15  0F 84 11 01 00 00               je 0x140af5c2c
00AF5B1B  83 EB 02                        sub ebx, 2
00AF5B1E  0F 84 F5 00 00 00               je 0x140af5c19
00AF5B24  83 EB 01                        sub ebx, 1
00AF5B27  74 31                           je 0x140af5b5a
00AF5B29  83 FB 01                        cmp ebx, 1
00AF5B2C  0F 85 7F F6 FF FF               jne 0x140af51b1
00AF5B32  45 84 E4                        test r12b, r12b
00AF5B35  0F 85 5A 0B 00 00               jne 0x140af6695
00AF5B3B  41 83 FF 18                     cmp r15d, 0x18
00AF5B3F  0F 85 72 0C 00 00               jne 0x140af67b7
00AF5B45  4D 8B 46 10                     mov r8, qword ptr [r14 + 0x10]
00AF5B49  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00AF5B4D  49 8B 0E                        mov rcx, qword ptr [r14]
00AF5B50  E8 87 23 C5 FF                  call 0x140747edc
00AF5B55  E9 0B 0D 00 00                  jmp 0x140af6865
00AF5B5A  41 8D 47 F0                     lea eax, [r15 - 0x10]
00AF5B5E  A9 E7 FF FF FF                  test eax, 0xffffffe7
00AF5B63  0F 85 4E 0C 00 00               jne 0x140af67b7
00AF5B69  41 83 FF 28                     cmp r15d, 0x28
00AF5B6D  0F 84 44 0C 00 00               je 0x140af67b7
00AF5B73  41 8A D4                        mov dl, r12b
00AF5B76  48 8B 0D 8B 3F 4E 00            mov rcx, qword ptr [rip + 0x4e3f8b]
00AF5B7D  E8 9E C2 D7 FF                  call 0x140871e20
00AF5B82  84 C0                           test al, al
00AF5B84  0F 84 4A 0C 00 00               je 0x140af67d4
00AF5B8A  4D 8B C7                        mov r8, r15
00AF5B8D  49 8B D6                        mov rdx, r14
00AF5B90  48 8D 8C 24 A0 01 00 00         lea rcx, [rsp + 0x1a0]
00AF5B98  E8 A3 0C BD FF                  call 0x1406c6840
00AF5B9D  90                              nop
00AF5B9E  41 83 FF 20                     cmp r15d, 0x20
00AF5BA2  48 0F 44 B4 24 B8 01 00 00      cmove rsi, qword ptr [rsp + 0x1b8]
00AF5BAB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00AF5BB4  E8 B7 99 94 FF                  call 0x14043f570
00AF5BB9  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00AF5BC2  8A 91 32 02 00 00               mov dl, byte ptr [rcx + 0x232]
00AF5BC8  48 8D 8C 24 D0 00 00 00         lea rcx, [rsp + 0xd0]
00AF5BD0  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00AF5BD5  88 54 24 20                     mov byte ptr [rsp + 0x20], dl
00AF5BD9  4C 8B CE                        mov r9, rsi
00AF5BDC  44 8B 84 24 B0 01 00 00         mov r8d, dword ptr [rsp + 0x1b0]
00AF5BE4  48 8B 94 24 A0 01 00 00         mov rdx, qword ptr [rsp + 0x1a0]
00AF5BEC  48 8B C8                        mov rcx, rax
00AF5BEF  E8 30 C7 FB FF                  call 0x140ab2324
00AF5BF4  8B F8                           mov edi, eax
00AF5BF6  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00AF5BFA  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00AF5C02  49 89 46 08                     mov qword ptr [r14 + 8], rax
00AF5C06  E9 5C 0C 00 00                  jmp 0x140af6867
00AF5C0B  8B 7C 24 54                     mov edi, dword ptr [rsp + 0x54]
00AF5C0F  E9 53 0C 00 00                  jmp 0x140af6867
00AF5C14  E9 50 0C 00 00                  jmp 0x140af6869
00AF5C19  45 8A C4                        mov r8b, r12b
00AF5C1C  41 8B D7                        mov edx, r15d
00AF5C1F  49 8B CE                        mov rcx, r14
00AF5C22  E8 25 BC AB FF                  call 0x1405b184c
00AF5C27  E9 39 0C 00 00                  jmp 0x140af6865
00AF5C2C  41 83 FF 10                     cmp r15d, 0x10
00AF5C30  0F 85 81 0B 00 00               jne 0x140af67b7
00AF5C36  41 8A D4                        mov dl, r12b
00AF5C39  48 8B 0D C8 3E 4E 00            mov rcx, qword ptr [rip + 0x4e3ec8]
00AF5C40  E8 DB C1 D7 FF                  call 0x140871e20
00AF5C45  84 C0                           test al, al
00AF5C47  0F 84 87 0B 00 00               je 0x140af67d4
00AF5C4D  49 8B 16                        mov rdx, qword ptr [r14]
00AF5C50  48 89 94 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdx
00AF5C58  4C 8D 84 24 D8 00 00 00         lea r8, [rsp + 0xd8]
00AF5C60  E8 3B 93 D1 FF                  call 0x14080efa0
00AF5C65  8B F8                           mov edi, eax
00AF5C67  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00AF5C6B  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00AF5C73  49 89 46 08                     mov qword ptr [r14 + 8], rax
00AF5C77  E9 EB 0B 00 00                  jmp 0x140af6867
00AF5C7C  8B 7C 24 54                     mov edi, dword ptr [rsp + 0x54]
00AF5C80  E9 E2 0B 00 00                  jmp 0x140af6867
00AF5C85  E9 DF 0B 00 00                  jmp 0x140af6869
00AF5C8A  45 84 E4                        test r12b, r12b
00AF5C8D  0F 85 41 0B 00 00               jne 0x140af67d4
00AF5C93  41 83 FF 20                     cmp r15d, 0x20
00AF5C97  0F 85 05 F8 FF FF               jne 0x140af54a2
00AF5C9D  49 8B D6                        mov rdx, r14
00AF5CA0  E8 7F A7 0C 00                  call 0x140bc0424
00AF5CA5  E9 BB 0B 00 00                  jmp 0x140af6865
00AF5CAA  41 83 FF 04                     cmp r15d, 4
00AF5CAE  0F 85 03 0B 00 00               jne 0x140af67b7
00AF5CB4  48 C7 84 24 E0 00 00 00 74 00 76 00  mov qword ptr [rsp + 0xe0], 0x760074
00AF5CC0  48 8D 05 29 27 01 00            lea rax, [rip + 0x12729]
00AF5CC7  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
00AF5CCF  41 8A 06                        mov al, byte ptr [r14]
00AF5CD2  41 22 C5                        and al, r13b
00AF5CD5  88 84 24 80 00 00 00            mov byte ptr [rsp + 0x80], al
00AF5CDC  84 C0                           test al, al
00AF5CDE  0F 84 85 00 00 00               je 0x140af5d69
00AF5CE4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF5CED  48 83 CB FF                     or rbx, 0xffffffffffffffff
00AF5CF1  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
00AF5CF8  90                              nop
00AF5CF9  45 33 C0                        xor r8d, r8d
00AF5CFC  33 D2                           xor edx, edx
00AF5CFE  4C 8D 35 23 25 4E 00            lea r14, [rip + 0x4e2523]
00AF5D05  49 8B CE                        mov rcx, r14
00AF5D08  E8 23 A5 71 FF                  call 0x140210230
00AF5D0D  48 8B F8                        mov rdi, rax
00AF5D10  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
00AF5D16  73 0E                           jae 0x140af5d26
00AF5D18  4D 8B C6                        mov r8, r14
00AF5D1B  48 8B D0                        mov rdx, rax
00AF5D1E  49 8B CE                        mov rcx, r14
00AF5D21  E8 6A 9F 71 FF                  call 0x14020fc90
00AF5D26  48 85 FF                        test rdi, rdi
00AF5D29  74 04                           je 0x140af5d2f
00AF5D2B  44 88 6F 0A                     mov byte ptr [rdi + 0xa], r13b
00AF5D2F  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00AF5D37  E8 54 95 BB FF                  call 0x1406af290
00AF5D3C  8B F8                           mov edi, eax
00AF5D3E  F0 48 0F C1 1D E1 24 4E 00      lock xadd qword ptr [rip + 0x4e24e1], rbx
00AF5D47  80 E3 06                        and bl, 6
00AF5D4A  80 FB 02                        cmp bl, 2
00AF5D4D  75 08                           jne 0x140af5d57
00AF5D4F  49 8B CE                        mov rcx, r14
00AF5D52  E8 79 00 77 FF                  call 0x140265dd0
00AF5D57  49 8B CE                        mov rcx, r14
00AF5D5A  E8 A1 B8 7E FF                  call 0x1402e1600
00AF5D5F  E8 4C 7B 76 FF                  call 0x14025d8b0
00AF5D64  E9 FE 0A 00 00                  jmp 0x140af6867
00AF5D69  41 8A D4                        mov dl, r12b
00AF5D6C  48 8B 0D AD 3D 4E 00            mov rcx, qword ptr [rip + 0x4e3dad]
00AF5D73  E8 A8 C0 D7 FF                  call 0x140871e20
00AF5D78  84 C0                           test al, al
00AF5D7A  0F 84 54 0A 00 00               je 0x140af67d4
00AF5D80  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00AF5D88  E8 83 AE BB FF                  call 0x1406b0c10
00AF5D8D  E9 D3 0A 00 00                  jmp 0x140af6865
00AF5D92  E9 D2 0A 00 00                  jmp 0x140af6869
00AF5D97  81 EB 86 00 00 00               sub ebx, 0x86
00AF5D9D  0F 84 4E 02 00 00               je 0x140af5ff1
00AF5DA3  83 EB 08                        sub ebx, 8
00AF5DA6  0F 84 EA 00 00 00               je 0x140af5e96
00AF5DAC  83 EB 08                        sub ebx, 8
00AF5DAF  0F 84 BA 00 00 00               je 0x140af5e6f
00AF5DB5  83 EB 01                        sub ebx, 1
00AF5DB8  74 36                           je 0x140af5df0
00AF5DBA  83 FB 01                        cmp ebx, 1
00AF5DBD  0F 85 EE F3 FF FF               jne 0x140af51b1
00AF5DC3  41 83 FF 08                     cmp r15d, 8
00AF5DC7  0F 85 EA 09 00 00               jne 0x140af67b7
00AF5DCD  45 84 E4                        test r12b, r12b
00AF5DD0  0F 84 90 07 00 00               je 0x140af6566
00AF5DD6  49 8B 0E                        mov rcx, qword ptr [r14]
00AF5DD9  48 89 8C 24 88 01 00 00         mov qword ptr [rsp + 0x188], rcx
00AF5DE1  E8 7E E7 CC FF                  call 0x1407c4564
00AF5DE6  E9 7A 0A 00 00                  jmp 0x140af6865
00AF5DEB  E9 79 0A 00 00                  jmp 0x140af6869
00AF5DF0  48 C7 44 24 78 13 00 00 00      mov qword ptr [rsp + 0x78], 0x13
00AF5DF9  41 8A D4                        mov dl, r12b
00AF5DFC  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00AF5E01  E8 1A C0 D7 FF                  call 0x140871e20
00AF5E06  84 C0                           test al, al
00AF5E08  0F 84 C6 09 00 00               je 0x140af67d4
00AF5E0E  41 83 EF 01                     sub r15d, 1
00AF5E12  74 1C                           je 0x140af5e30
00AF5E14  41 83 FF 03                     cmp r15d, 3
00AF5E18  0F 85 99 09 00 00               jne 0x140af67b7
00AF5E1E  45 8B 2E                        mov r13d, dword ptr [r14]
00AF5E21  44 89 AC 24 04 01 00 00         mov dword ptr [rsp + 0x104], r13d
00AF5E29  EB 32                           jmp 0x140af5e5d
00AF5E2B  E9 39 0A 00 00                  jmp 0x140af6869
00AF5E30  41 8A 1E                        mov bl, byte ptr [r14]
00AF5E33  88 5C 24 70                     mov byte ptr [rsp + 0x70], bl
00AF5E37  84 DB                           test bl, bl
00AF5E39  74 17                           je 0x140af5e52
00AF5E3B  41 8A D4                        mov dl, r12b
00AF5E3E  48 8B 0D 33 3C 4E 00            mov rcx, qword ptr [rip + 0x4e3c33]
00AF5E45  E8 D6 BF D7 FF                  call 0x140871e20
00AF5E4A  84 C0                           test al, al
00AF5E4C  0F 84 82 09 00 00               je 0x140af67d4
00AF5E52  B8 05 00 00 00                  mov eax, 5
00AF5E57  84 DB                           test bl, bl
00AF5E59  44 0F 44 E8                     cmove r13d, eax
00AF5E5D  41 8B CD                        mov ecx, r13d
00AF5E60  E8 77 F2 B5 FF                  call 0x1406550dc
00AF5E65  E9 FB 09 00 00                  jmp 0x140af6865
00AF5E6A  E9 FA 09 00 00                  jmp 0x140af6869
00AF5E6F  41 8A D4                        mov dl, r12b
00AF5E72  48 8B 0D FF 3B 4E 00            mov rcx, qword ptr [rip + 0x4e3bff]
00AF5E79  E8 A2 BF D7 FF                  call 0x140871e20
00AF5E7E  84 C0                           test al, al
00AF5E80  0F 84 4E 09 00 00               je 0x140af67d4
00AF5E86  41 8B D7                        mov edx, r15d
00AF5E89  49 8B CE                        mov rcx, r14
00AF5E8C  E8 07 F1 B5 FF                  call 0x140654f98
00AF5E91  E9 CF 09 00 00                  jmp 0x140af6865
00AF5E96  0F 57 C0                        xorps xmm0, xmm0
00AF5E99  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
00AF5EA1  E8 4A 83 80 FF                  call 0x1402fe1f0
00AF5EA6  48 8D B8 58 05 00 00            lea rdi, [rax + 0x558]
00AF5EAD  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00AF5EB2  41 83 FF 30                     cmp r15d, 0x30
00AF5EB6  0F 85 FB 08 00 00               jne 0x140af67b7
00AF5EBC  41 8A D4                        mov dl, r12b
00AF5EBF  48 8B 0D 6A 3C 4E 00            mov rcx, qword ptr [rip + 0x4e3c6a]
00AF5EC6  E8 55 BF D7 FF                  call 0x140871e20
00AF5ECB  84 C0                           test al, al
00AF5ECD  0F 84 01 09 00 00               je 0x140af67d4
00AF5ED3  41 0F 10 16                     movups xmm2, xmmword ptr [r14]
00AF5ED7  0F 29 94 24 A0 01 00 00         movaps xmmword ptr [rsp + 0x1a0], xmm2
00AF5EDF  41 0F 10 46 10                  movups xmm0, xmmword ptr [r14 + 0x10]
00AF5EE4  0F 29 84 24 B0 01 00 00         movaps xmmword ptr [rsp + 0x1b0], xmm0
00AF5EEC  41 0F 10 4E 20                  movups xmm1, xmmword ptr [r14 + 0x20]
00AF5EF1  0F 29 8C 24 C0 01 00 00         movaps xmmword ptr [rsp + 0x1c0], xmm1
00AF5EF9  66 0F 7E D1                     movd ecx, xmm2
00AF5EFD  33 C0                           xor eax, eax
00AF5EFF  F0 0F B1 0F                     lock cmpxchg dword ptr [rdi], ecx
00AF5F03  74 07                           je 0x140af5f0c
00AF5F05  33 C0                           xor eax, eax
00AF5F07  E9 5D 09 00 00                  jmp 0x140af6869
00AF5F0C  0F 28 8C 24 B0 01 00 00         movaps xmm1, xmmword ptr [rsp + 0x1b0]
00AF5F14  0F 11 8C 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm1
00AF5F1C  0F 57 C0                        xorps xmm0, xmm0
00AF5F1F  0F 11 84 24 B0 01 00 00         movups xmmword ptr [rsp + 0x1b0], xmm0
00AF5F27  66 0F 7E CB                     movd ebx, xmm1
00AF5F2B  66 85 DB                        test bx, bx
00AF5F2E  0F 84 90 00 00 00               je 0x140af5fc4
00AF5F34  41 84 DD                        test r13b, bl
00AF5F37  0F 85 87 00 00 00               jne 0x140af5fc4
00AF5F3D  48 8B BC 24 F8 00 00 00         mov rdi, qword ptr [rsp + 0xf8]
00AF5F45  41 84 FD                        test r13b, dil
00AF5F48  0F 85 4B 09 00 00               jne 0x140af6899
00AF5F4E  0F B7 CB                        movzx ecx, bx
00AF5F51  48 03 CF                        add rcx, rdi
00AF5F54  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00AF5F5E  48 3B C8                        cmp rcx, rax
00AF5F61  77 05                           ja 0x140af5f68
00AF5F63  48 3B CF                        cmp rcx, rdi
00AF5F66  73 12                           jae 0x140af5f7a
00AF5F68  8A 00                           mov al, byte ptr [rax]
00AF5F6A  48 8B BC 24 F8 00 00 00         mov rdi, qword ptr [rsp + 0xf8]
00AF5F72  0F B7 9C 24 F0 00 00 00         movzx ebx, word ptr [rsp + 0xf0]
00AF5F7A  44 0F B7 FB                     movzx r15d, bx
00AF5F7E  41 B8 45 58 53 50               mov r8d, 0x50535845
00AF5F84  41 8B D7                        mov edx, r15d
00AF5F87  B9 01 01 00 00                  mov ecx, 0x101
00AF5F8C  E8 5F C1 08 00                  call 0x140b820f0
00AF5F91  4C 8B F0                        mov r14, rax
00AF5F94  48 85 C0                        test rax, rax
00AF5F97  74 26                           je 0x140af5fbf
00AF5F99  45 8B C7                        mov r8d, r15d
00AF5F9C  48 8B D7                        mov rdx, rdi
00AF5F9F  48 8B C8                        mov rcx, rax
00AF5FA2  E8 99 08 BD FF                  call 0x1406c6840
00AF5FA7  4C 89 B4 24 B8 01 00 00         mov qword ptr [rsp + 0x1b8], r14
00AF5FAF  66 89 9C 24 B0 01 00 00         mov word ptr [rsp + 0x1b0], bx
00AF5FB7  66 89 9C 24 B2 01 00 00         mov word ptr [rsp + 0x1b2], bx
00AF5FBF  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00AF5FC4  0F 28 84 24 A0 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x1a0]
00AF5FCC  0F 11 07                        movups xmmword ptr [rdi], xmm0
00AF5FCF  0F 28 8C 24 B0 01 00 00         movaps xmm1, xmmword ptr [rsp + 0x1b0]
00AF5FD7  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
00AF5FDB  0F 28 84 24 C0 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x1c0]
00AF5FE3  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
00AF5FE7  E9 7F F1 FF FF                  jmp 0x140af516b
00AF5FEC  E9 78 08 00 00                  jmp 0x140af6869
00AF5FF1  41 83 FF 20                     cmp r15d, 0x20
00AF5FF5  0F 85 BC 07 00 00               jne 0x140af67b7
00AF5FFB  49 8B D6                        mov rdx, r14
00AF5FFE  E8 AD 19 F2 FF                  call 0x140a179b0
00AF6003  E9 5D 08 00 00                  jmp 0x140af6865
00AF6008  E8 83 1D CF FF                  call 0x1407e7d90
00AF600D  E9 53 08 00 00                  jmp 0x140af6865
00AF6012  B8 B0 00 00 00                  mov eax, 0xb0
00AF6017  3B D8                           cmp ebx, eax
00AF6019  0F 8F 99 01 00 00               jg 0x140af61b8
00AF601F  0F 84 1B 01 00 00               je 0x140af6140
00AF6025  8B CB                           mov ecx, ebx
00AF6027  81 E9 9F 00 00 00               sub ecx, 0x9f
00AF602D  0F 84 D9 F2 FF FF               je 0x140af530c
00AF6033  83 E9 02                        sub ecx, 2
00AF6036  0F 84 D2 00 00 00               je 0x140af610e
00AF603C  83 E9 03                        sub ecx, 3
00AF603F  0F 84 17 07 00 00               je 0x140af675c
00AF6045  83 E9 04                        sub ecx, 4
00AF6048  74 68                           je 0x140af60b2
00AF604A  83 F9 02                        cmp ecx, 2
00AF604D  0F 85 5E F1 FF FF               jne 0x140af51b1
00AF6053  0F 57 C0                        xorps xmm0, xmm0
00AF6056  0F 11 84 24 30 01 00 00         movups xmmword ptr [rsp + 0x130], xmm0
00AF605E  41 83 FF 10                     cmp r15d, 0x10
00AF6062  0F 85 4F 07 00 00               jne 0x140af67b7
00AF6068  41 8A D4                        mov dl, r12b
00AF606B  48 8B 0D 76 3A 4E 00            mov rcx, qword ptr [rip + 0x4e3a76]
00AF6072  E8 A9 BD D7 FF                  call 0x140871e20
00AF6077  84 C0                           test al, al
00AF6079  0F 84 55 07 00 00               je 0x140af67d4
00AF607F  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
00AF6083  F3 0F 7F 84 24 30 01 00 00      movdqu xmmword ptr [rsp + 0x130], xmm0
00AF608C  48 8B 8C 24 30 01 00 00         mov rcx, qword ptr [rsp + 0x130]
00AF6094  48 8B D1                        mov rdx, rcx
00AF6097  48 C1 EA 20                     shr rdx, 0x20
00AF609B  4C 8B 84 24 38 01 00 00         mov r8, qword ptr [rsp + 0x138]
00AF60A3  E8 58 F6 AC FF                  call 0x1405c5700
00AF60A8  E9 B8 07 00 00                  jmp 0x140af6865
00AF60AD  E9 B7 07 00 00                  jmp 0x140af6869
00AF60B2  41 F6 C7 07                     test r15b, 7
00AF60B6  0F 85 FB 06 00 00               jne 0x140af67b7
00AF60BC  41 81 FF 00 01 00 00            cmp r15d, 0x100
00AF60C3  0F 87 EE 06 00 00               ja 0x140af67b7
00AF60C9  4D 8B C7                        mov r8, r15
00AF60CC  49 8B D6                        mov rdx, r14
00AF60CF  48 8D 8C 24 20 02 00 00         lea rcx, [rsp + 0x220]
00AF60D7  E8 64 07 BD FF                  call 0x1406c6840
00AF60DC  90                              nop
00AF60DD  41 8A CC                        mov cl, r12b
00AF60E0  E8 5F F3 8A FF                  call 0x1403a5444
00AF60E5  85 C0                           test eax, eax
00AF60E7  0F 88 7C 07 00 00               js 0x140af6869
00AF60ED  41 C1 EF 03                     shr r15d, 3
00AF60F1  45 33 C9                        xor r9d, r9d
00AF60F4  48 8D 94 24 20 02 00 00         lea rdx, [rsp + 0x220]
00AF60FC  41 8B CF                        mov ecx, r15d
00AF60FF  E8 04 D2 80 FF                  call 0x140303308
00AF6104  E9 5C 07 00 00                  jmp 0x140af6865
00AF6109  E9 5B 07 00 00                  jmp 0x140af6869
00AF610E  45 84 E4                        test r12b, r12b
00AF6111  0F 85 7E 05 00 00               jne 0x140af6695
00AF6117  41 83 FF 08                     cmp r15d, 8
00AF611B  0F 85 96 06 00 00               jne 0x140af67b7
00AF6121  4C 8D 05 B8 14 45 00            lea r8, [rip + 0x4514b8]
00AF6128  49 8B D6                        mov rdx, r14
00AF612B  41 8D 4F FB                     lea ecx, [r15 - 5]
00AF612F  48 FF 15 82 B5 65 FF            call qword ptr [rip - 0x9a4a7e]
00AF6136  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00AF613B  E9 25 07 00 00                  jmp 0x140af6865
00AF6140  41 83 FF 08                     cmp r15d, 8
00AF6144  0F 82 6D 06 00 00               jb 0x140af67b7
00AF614A  41 83 C7 F8                     add r15d, -8
00AF614E  41 F6 C7 07                     test r15b, 7
00AF6152  0F 85 5F 06 00 00               jne 0x140af67b7
00AF6158  41 81 FF 00 01 00 00            cmp r15d, 0x100
00AF615F  0F 87 52 06 00 00               ja 0x140af67b7
00AF6165  49 8B 1E                        mov rbx, qword ptr [r14]
00AF6168  48 89 9C 24 90 01 00 00         mov qword ptr [rsp + 0x190], rbx
00AF6170  45 8B C7                        mov r8d, r15d
00AF6173  49 8D 56 08                     lea rdx, [r14 + 8]
00AF6177  48 8D 8C 24 20 03 00 00         lea rcx, [rsp + 0x320]
00AF617F  E8 BC 06 BD FF                  call 0x1406c6840
00AF6184  90                              nop
00AF6185  41 8A CC                        mov cl, r12b
00AF6188  E8 B7 F2 8A FF                  call 0x1403a5444
00AF618D  8B F8                           mov edi, eax
00AF618F  85 C0                           test eax, eax
00AF6191  0F 88 D0 06 00 00               js 0x140af6867
00AF6197  41 C1 EF 03                     shr r15d, 3
00AF619B  4C 8B C3                        mov r8, rbx
00AF619E  48 8D 94 24 20 03 00 00         lea rdx, [rsp + 0x320]
00AF61A6  41 8B CF                        mov ecx, r15d
00AF61A9  E8 0E B0 AC FF                  call 0x1405c11bc
00AF61AE  E9 B2 06 00 00                  jmp 0x140af6865
00AF61B3  E9 B1 06 00 00                  jmp 0x140af6869
00AF61B8  8B CB                           mov ecx, ebx
00AF61BA  81 E9 B1 00 00 00               sub ecx, 0xb1
00AF61C0  0F 84 B9 00 00 00               je 0x140af627f
00AF61C6  83 E9 0A                        sub ecx, 0xa
00AF61C9  74 47                           je 0x140af6212
00AF61CB  83 E9 03                        sub ecx, 3
00AF61CE  0F 84 88 05 00 00               je 0x140af675c
00AF61D4  83 F9 01                        cmp ecx, 1
00AF61D7  0F 85 D4 EF FF FF               jne 0x140af51b1
00AF61DD  45 85 FF                        test r15d, r15d
00AF61E0  74 0A                           je 0x140af61ec
00AF61E2  BF 0D 00 00 C0                  mov edi, 0xc000000d
00AF61E7  E9 7B 06 00 00                  jmp 0x140af6867
00AF61EC  45 84 E4                        test r12b, r12b
00AF61EF  74 17                           je 0x140af6208
00AF61F1  41 8A D4                        mov dl, r12b
00AF61F4  48 8B 0D 85 38 4E 00            mov rcx, qword ptr [rip + 0x4e3885]
00AF61FB  E8 20 BC D7 FF                  call 0x140871e20
00AF6200  84 C0                           test al, al
00AF6202  0F 84 CC 05 00 00               je 0x140af67d4
00AF6208  E8 23 33 C2 FF                  call 0x140719530
00AF620D  E9 53 06 00 00                  jmp 0x140af6865
00AF6212  41 83 FF 18                     cmp r15d, 0x18
00AF6216  0F 85 9B 05 00 00               jne 0x140af67b7
00AF621C  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
00AF6220  0F 29 84 24 A0 01 00 00         movaps xmmword ptr [rsp + 0x1a0], xmm0
00AF6228  F2 41 0F 10 4E 10               movsd xmm1, qword ptr [r14 + 0x10]
00AF622E  F2 0F 11 8C 24 B0 01 00 00      movsd qword ptr [rsp + 0x1b0], xmm1
00AF6237  41 8B D5                        mov edx, r13d
00AF623A  48 8D 8C 24 A0 01 00 00         lea rcx, [rsp + 0x1a0]
00AF6242  E8 B1 CD 09 00                  call 0x140b92ff8
00AF6247  85 C0                           test eax, eax
00AF6249  0F 88 1A 06 00 00               js 0x140af6869
00AF624F  44 8B 84 24 B4 01 00 00         mov r8d, dword ptr [rsp + 0x1b4]
00AF6257  8B 94 24 B0 01 00 00            mov edx, dword ptr [rsp + 0x1b0]
00AF625E  48 8D 8C 24 A0 01 00 00         lea rcx, [rsp + 0x1a0]
00AF6266  E8 85 CB AE FF                  call 0x1405e2df0
00AF626B  8B F8                           mov edi, eax
00AF626D  48 8D 8C 24 A0 01 00 00         lea rcx, [rsp + 0x1a0]
00AF6275  E9 E1 03 00 00                  jmp 0x140af665b
00AF627A  E9 EA 05 00 00                  jmp 0x140af6869
00AF627F  0F 57 C0                        xorps xmm0, xmm0
00AF6282  33 C0                           xor eax, eax
00AF6284  0F 11 84 24 40 01 00 00         movups xmmword ptr [rsp + 0x140], xmm0
00AF628C  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
00AF6294  41 83 FF 08                     cmp r15d, 8
00AF6298  0F 85 A5 00 00 00               jne 0x140af6343
00AF629E  41 8A D4                        mov dl, r12b
00AF62A1  48 8B 0D D0 37 4E 00            mov rcx, qword ptr [rip + 0x4e37d0]
00AF62A8  E8 73 BB D7 FF                  call 0x140871e20
00AF62AD  84 C0                           test al, al
00AF62AF  0F 84 1F 05 00 00               je 0x140af67d4
00AF62B5  49 8B 0E                        mov rcx, qword ptr [r14]
00AF62B8  48 89 8C 24 68 01 00 00         mov qword ptr [rsp + 0x168], rcx
00AF62C0  4C 8B 05 D1 07 4D 00            mov r8, qword ptr [rip + 0x4d07d1]
00AF62C7  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
00AF62CF  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00AF62D4  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00AF62DC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AF62E1  45 8A CC                        mov r9b, r12b
00AF62E4  BA 00 10 00 00                  mov edx, 0x1000
00AF62E9  E8 C2 2A D7 FF                  call 0x140868db0
00AF62EE  8B F8                           mov edi, eax
00AF62F0  85 C0                           test eax, eax
00AF62F2  0F 88 6F 05 00 00               js 0x140af6867
00AF62F8  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
00AF6300  48 8B CB                        mov rcx, rbx
00AF6303  E8 E8 95 73 FF                  call 0x14022f8f0
00AF6308  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
00AF630C  83 F8 FF                        cmp eax, -1
00AF630F  0F 84 2E F5 FF FF               je 0x140af5843
00AF6315  48 89 9C 24 50 01 00 00         mov qword ptr [rsp + 0x150], rbx
00AF631D  4C 8D 4C 24 74                  lea r9, [rsp + 0x74]
00AF6322  45 8B C5                        mov r8d, r13d
00AF6325  48 8D 94 24 40 01 00 00         lea rdx, [rsp + 0x140]
00AF632D  B9 20 00 00 00                  mov ecx, 0x20
00AF6332  E8 89 D0 E1 FF                  call 0x1409133c0
00AF6337  8B F8                           mov edi, eax
00AF6339  E9 05 F5 FF FF                  jmp 0x140af5843
00AF633E  E9 26 05 00 00                  jmp 0x140af6869
00AF6343  45 85 FF                        test r15d, r15d
00AF6346  0F 85 6B 04 00 00               jne 0x140af67b7
00AF634C  8B FE                           mov edi, esi
00AF634E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF6357  48 8B 98 B8 00 00 00            mov rbx, qword ptr [rax + 0xb8]
00AF635E  48 8B CB                        mov rcx, rbx
00AF6361  E8 8A 95 73 FF                  call 0x14022f8f0
00AF6366  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
00AF636A  83 F8 FF                        cmp eax, -1
00AF636D  0F 84 F4 04 00 00               je 0x140af6867
00AF6373  48 89 9C 24 50 01 00 00         mov qword ptr [rsp + 0x150], rbx
00AF637B  4C 8D 4C 24 74                  lea r9, [rsp + 0x74]
00AF6380  45 8B C5                        mov r8d, r13d
00AF6383  48 8D 94 24 40 01 00 00         lea rdx, [rsp + 0x140]
00AF638B  41 8D 4F 20                     lea ecx, [r15 + 0x20]
00AF638F  E8 2C D0 E1 FF                  call 0x1409133c0
00AF6394  E9 CC 04 00 00                  jmp 0x140af6865
00AF6399  45 85 FF                        test r15d, r15d
00AF639C  0F 85 40 FE FF FF               jne 0x140af61e2
00AF63A2  41 8A D4                        mov dl, r12b
00AF63A5  48 8B 0D CC 36 4E 00            mov rcx, qword ptr [rip + 0x4e36cc]
00AF63AC  E8 6F BA D7 FF                  call 0x140871e20
00AF63B1  84 C0                           test al, al
00AF63B3  0F 84 1B 04 00 00               je 0x140af67d4
00AF63B9  E8 FA 88 A9 FF                  call 0x14058ecb8
00AF63BE  8B F8                           mov edi, eax
00AF63C0  85 C0                           test eax, eax
00AF63C2  0F 88 9F 04 00 00               js 0x140af6867
00AF63C8  E8 23 C8 A9 FF                  call 0x140592bf0
00AF63CD  E9 93 04 00 00                  jmp 0x140af6865
00AF63D2  B8 DF 00 00 00                  mov eax, 0xdf
00AF63D7  3B D8                           cmp ebx, eax
00AF63D9  0F 8F E3 02 00 00               jg 0x140af66c2
00AF63DF  0F 84 CA 02 00 00               je 0x140af66af
00AF63E5  81 FB D4 00 00 00               cmp ebx, 0xd4
00AF63EB  0F 8F BD 01 00 00               jg 0x140af65ae
00AF63F1  0F 84 A4 01 00 00               je 0x140af659b
00AF63F7  8B CB                           mov ecx, ebx
00AF63F9  81 E9 C7 00 00 00               sub ecx, 0xc7
00AF63FF  0F 84 57 03 00 00               je 0x140af675c
00AF6405  83 E9 05                        sub ecx, 5
00AF6408  0F 84 05 01 00 00               je 0x140af6513
00AF640E  83 E9 02                        sub ecx, 2
00AF6411  0F 84 89 00 00 00               je 0x140af64a0
00AF6417  83 E9 01                        sub ecx, 1
00AF641A  74 1C                           je 0x140af6438
00AF641C  83 F9 03                        cmp ecx, 3
00AF641F  0F 85 8C ED FF FF               jne 0x140af51b1
00AF6425  45 8A C4                        mov r8b, r12b
00AF6428  41 8B D7                        mov edx, r15d
00AF642B  49 8B CE                        mov rcx, r14
00AF642E  E8 DD F7 CE FF                  call 0x1407e5c10
00AF6433  E9 2D 04 00 00                  jmp 0x140af6865
00AF6438  41 83 FF 04                     cmp r15d, 4
00AF643C  0F 85 75 03 00 00               jne 0x140af67b7
00AF6442  41 8A D4                        mov dl, r12b
00AF6445  48 8B 0D 34 36 4E 00            mov rcx, qword ptr [rip + 0x4e3634]
00AF644C  E8 CF B9 D7 FF                  call 0x140871e20
00AF6451  84 C0                           test al, al
00AF6453  0F 84 3C 02 00 00               je 0x140af6695
00AF6459  89 B4 24 84 00 00 00            mov dword ptr [rsp + 0x84], esi
00AF6460  41 8B 0E                        mov ecx, dword ptr [r14]
00AF6463  89 8C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ecx
00AF646A  BA 18 20 00 00                  mov edx, 0x2018
00AF646F  85 CA                           test edx, ecx
00AF6471  0F 85 EF 00 00 00               jne 0x140af6566
00AF6477  8B 05 43 DF 4C 00               mov eax, dword ptr [rip + 0x4cdf43]
00AF647D  23 C2                           and eax, edx
00AF647F  0B C8                           or ecx, eax
00AF6481  89 8C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ecx
00AF6488  89 0D 32 DF 4C 00               mov dword ptr [rip + 0x4cdf32], ecx
00AF648E  41 89 0E                        mov dword ptr [r14], ecx
00AF6491  E9 D1 03 00 00                  jmp 0x140af6867
00AF6496  E9 CE 03 00 00                  jmp 0x140af6869
00AF649B  E9 C9 03 00 00                  jmp 0x140af6869
00AF64A0  41 83 FF 08                     cmp r15d, 8
00AF64A4  0F 85 0D 03 00 00               jne 0x140af67b7
00AF64AA  45 84 E4                        test r12b, r12b
00AF64AD  74 17                           je 0x140af64c6
00AF64AF  41 8A D4                        mov dl, r12b
00AF64B2  48 8B 0D 27 37 4E 00            mov rcx, qword ptr [rip + 0x4e3727]
00AF64B9  E8 62 B9 D7 FF                  call 0x140871e20
00AF64BE  84 C0                           test al, al
00AF64C0  0F 84 0E 03 00 00               je 0x140af67d4
00AF64C6  E8 15 FE 93 FF                  call 0x1404362e0
00AF64CB  84 C0                           test al, al
00AF64CD  0F 85 C2 01 00 00               jne 0x140af6695
00AF64D3  49 8B 06                        mov rax, qword ptr [r14]
00AF64D6  48 89 84 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rax
00AF64DE  40 38 B4 24 A0 01 00 00         cmp byte ptr [rsp + 0x1a0], sil
00AF64E6  0F 95 C1                        setne cl
00AF64E9  88 4C 24 30                     mov byte ptr [rsp + 0x30], cl
00AF64ED  E8 06 F5 CC FF                  call 0x1407c59f8
00AF64F2  8B F8                           mov edi, eax
00AF64F4  85 C0                           test eax, eax
00AF64F6  0F 88 6D 03 00 00               js 0x140af6869
00AF64FC  8A 4C 24 30                     mov cl, byte ptr [rsp + 0x30]
00AF6500  48 8B 05 31 89 40 00            mov rax, qword ptr [rip + 0x408931]
00AF6507  88 08                           mov byte ptr [rax], cl
00AF6509  E9 59 03 00 00                  jmp 0x140af6867
00AF650E  E9 56 03 00 00                  jmp 0x140af6869
00AF6513  48 89 B4 24 18 01 00 00         mov qword ptr [rsp + 0x118], rsi
00AF651B  41 83 FF 08                     cmp r15d, 8
00AF651F  0F 82 92 02 00 00               jb 0x140af67b7
00AF6525  41 83 C7 F8                     add r15d, -8
00AF6529  41 F6 C7 07                     test r15b, 7
00AF652D  0F 85 84 02 00 00               jne 0x140af67b7
00AF6533  41 81 FF 00 01 00 00            cmp r15d, 0x100
00AF653A  0F 87 77 02 00 00               ja 0x140af67b7
00AF6540  49 8B 1E                        mov rbx, qword ptr [r14]
00AF6543  48 89 9C 24 18 01 00 00         mov qword ptr [rsp + 0x118], rbx
00AF654B  45 8B C7                        mov r8d, r15d
00AF654E  49 8D 56 08                     lea rdx, [r14 + 8]
00AF6552  48 8D 8C 24 20 04 00 00         lea rcx, [rsp + 0x420]
00AF655A  E8 E1 02 BD FF                  call 0x1406c6840
00AF655F  90                              nop
00AF6560  48 83 FB 02                     cmp rbx, 2
00AF6564  72 0A                           jb 0x140af6570
00AF6566  B8 0D 00 00 C0                  mov eax, 0xc000000d
00AF656B  E9 F9 02 00 00                  jmp 0x140af6869
00AF6570  41 8A CC                        mov cl, r12b
00AF6573  E8 CC EE 8A FF                  call 0x1403a5444
00AF6578  8B F8                           mov edi, eax
00AF657A  85 C0                           test eax, eax
00AF657C  0F 88 E5 02 00 00               js 0x140af6867
00AF6582  41 C1 EF 03                     shr r15d, 3
00AF6586  44 8B CB                        mov r9d, ebx
00AF6589  48 8D 94 24 20 04 00 00         lea rdx, [rsp + 0x420]
00AF6591  E9 66 FB FF FF                  jmp 0x140af60fc
00AF6596  E9 CE 02 00 00                  jmp 0x140af6869
00AF659B  45 8A C4                        mov r8b, r12b
00AF659E  41 8B D7                        mov edx, r15d
00AF65A1  49 8B CE                        mov rcx, r14
00AF65A4  E8 CF F8 CE FF                  call 0x1407e5e78
00AF65A9  E9 B7 02 00 00                  jmp 0x140af6865
00AF65AE  8B CB                           mov ecx, ebx
00AF65B0  81 E9 D9 00 00 00               sub ecx, 0xd9
00AF65B6  0F 84 C6 00 00 00               je 0x140af6682
00AF65BC  83 E9 01                        sub ecx, 1
00AF65BF  0F 84 A0 00 00 00               je 0x140af6665
00AF65C5  83 E9 01                        sub ecx, 1
00AF65C8  74 09                           je 0x140af65d3
00AF65CA  83 F9 01                        cmp ecx, 1
00AF65CD  0F 85 DE EB FF FF               jne 0x140af51b1
00AF65D3  41 83 FF 10                     cmp r15d, 0x10
00AF65D7  0F 85 DA 01 00 00               jne 0x140af67b7
00AF65DD  45 84 E4                        test r12b, r12b
00AF65E0  74 45                           je 0x140af6627
00AF65E2  41 8A D4                        mov dl, r12b
00AF65E5  48 8B 0D 94 34 4E 00            mov rcx, qword ptr [rip + 0x4e3494]
00AF65EC  E8 2F B8 D7 FF                  call 0x140871e20
00AF65F1  84 C0                           test al, al
00AF65F3  0F 84 DB 01 00 00               je 0x140af67d4
00AF65F9  45 8B C5                        mov r8d, r13d
00AF65FC  49 8B D6                        mov rdx, r14
00AF65FF  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00AF6604  E8 B3 C9 09 00                  call 0x140b92fbc
00AF6609  85 C0                           test eax, eax
00AF660B  0F 88 58 02 00 00               js 0x140af6869
00AF6611  4C 8D 74 24 60                  lea r14, [rsp + 0x60]
00AF6616  66 39 74 24 60                  cmp word ptr [rsp + 0x60], si
00AF661B  75 0A                           jne 0x140af6627
00AF661D  B8 EF 00 00 C0                  mov eax, 0xc00000ef
00AF6622  E9 42 02 00 00                  jmp 0x140af6869
00AF6627  81 EB DB 00 00 00               sub ebx, 0xdb
00AF662D  74 16                           je 0x140af6645
00AF662F  83 FB 01                        cmp ebx, 1
00AF6632  74 07                           je 0x140af663b
00AF6634  BF 03 00 00 C0                  mov edi, 0xc0000003
00AF6639  EB 14                           jmp 0x140af664f
00AF663B  49 8B CE                        mov rcx, r14
00AF663E  E8 AD 03 B2 FF                  call 0x1406169f0
00AF6643  EB 08                           jmp 0x140af664d
00AF6645  49 8B CE                        mov rcx, r14
00AF6648  E8 27 02 B2 FF                  call 0x140616874
00AF664D  8B F8                           mov edi, eax
00AF664F  45 84 E4                        test r12b, r12b
00AF6652  0F 84 0F 02 00 00               je 0x140af6867
00AF6658  49 8B CE                        mov rcx, r14
00AF665B  E8 F4 C7 09 00                  call 0x140b92e54
00AF6660  E9 02 02 00 00                  jmp 0x140af6867
00AF6665  41 8A D4                        mov dl, r12b
00AF6668  48 8B 0D 11 34 4E 00            mov rcx, qword ptr [rip + 0x4e3411]
00AF666F  E8 AC B7 D7 FF                  call 0x140871e20
00AF6674  84 C0                           test al, al
00AF6676  74 1D                           je 0x140af6695
00AF6678  E8 63 02 B2 FF                  call 0x1406168e0
00AF667D  E9 E3 01 00 00                  jmp 0x140af6865
00AF6682  41 8A D4                        mov dl, r12b
00AF6685  48 8B 0D F4 33 4E 00            mov rcx, qword ptr [rip + 0x4e33f4]
00AF668C  E8 8F B7 D7 FF                  call 0x140871e20
00AF6691  84 C0                           test al, al
00AF6693  75 0A                           jne 0x140af669f
00AF6695  B8 22 00 00 C0                  mov eax, 0xc0000022
00AF669A  E9 CA 01 00 00                  jmp 0x140af6869
00AF669F  41 8B D7                        mov edx, r15d
00AF66A2  49 8B CE                        mov rcx, r14
00AF66A5  E8 FA 03 B2 FF                  call 0x140616aa4
00AF66AA  E9 B6 01 00 00                  jmp 0x140af6865
00AF66AF  49 8B D7                        mov rdx, r15
00AF66B2  45 8A C4                        mov r8b, r12b
00AF66B5  49 8B CE                        mov rcx, r14
00AF66B8  E8 DB FD B5 FF                  call 0x140656498
00AF66BD  E9 A3 01 00 00                  jmp 0x140af6865
00AF66C2  B8 E9 00 00 00                  mov eax, 0xe9
00AF66C7  3B D8                           cmp ebx, eax
00AF66C9  0F 8F BF 00 00 00               jg 0x140af678e
00AF66CF  0F 84 A9 00 00 00               je 0x140af677e
00AF66D5  8B CB                           mov ecx, ebx
00AF66D7  81 E9 E0 00 00 00               sub ecx, 0xe0
00AF66DD  74 7D                           je 0x140af675c
00AF66DF  83 E9 01                        sub ecx, 1
00AF66E2  74 78                           je 0x140af675c
00AF66E4  83 E9 01                        sub ecx, 1
00AF66E7  74 4C                           je 0x140af6735
00AF66E9  83 E9 02                        sub ecx, 2
00AF66EC  74 09                           je 0x140af66f7
00AF66EE  83 F9 01                        cmp ecx, 1
00AF66F1  0F 85 BA EA FF FF               jne 0x140af51b1
00AF66F7  40 88 74 24 31                  mov byte ptr [rsp + 0x31], sil
00AF66FC  4C 8D 44 24 31                  lea r8, [rsp + 0x31]
00AF6701  48 8B 15 60 33 4E 00            mov rdx, qword ptr [rip + 0x4e3360]
00AF6708  33 C9                           xor ecx, ecx
00AF670A  E8 01 F3 8A FF                  call 0x1403a5a10
00AF670F  85 C0                           test eax, eax
00AF6711  0F 88 BD 00 00 00               js 0x140af67d4
00AF6717  40 38 74 24 31                  cmp byte ptr [rsp + 0x31], sil
00AF671C  0F 84 B2 00 00 00               je 0x140af67d4
00AF6722  44 8B C3                        mov r8d, ebx
00AF6725  41 8B D7                        mov edx, r15d
00AF6728  49 8B CE                        mov rcx, r14
00AF672B  E8 04 F3 AB FF                  call 0x1405b5a34
00AF6730  E9 30 01 00 00                  jmp 0x140af6865
00AF6735  41 8A D4                        mov dl, r12b
00AF6738  48 8B 0D 41 33 4E 00            mov rcx, qword ptr [rip + 0x4e3341]
00AF673F  E8 DC B6 D7 FF                  call 0x140871e20
00AF6744  84 C0                           test al, al
00AF6746  0F 84 88 00 00 00               je 0x140af67d4
00AF674C  45 85 FF                        test r15d, r15d
00AF674F  0F 94 C1                        sete cl
00AF6752  E8 05 58 0A 00                  call 0x140b9bf5c
00AF6757  E9 09 01 00 00                  jmp 0x140af6865
00AF675C  48 8B 05 7D E7 40 00            mov rax, qword ptr [rip + 0x40e77d]
00AF6763  48 85 C0                        test rax, rax
00AF6766  0F 84 A0 EB FF FF               je 0x140af530c
00AF676C  45 8B C7                        mov r8d, r15d
00AF676F  49 8B D6                        mov rdx, r14
00AF6772  8B CB                           mov ecx, ebx
00AF6774  E8 57 43 BC FF                  call 0x1406baad0
00AF6779  E9 E7 00 00 00                  jmp 0x140af6865
00AF677E  41 8B D7                        mov edx, r15d
00AF6781  49 8B CE                        mov rcx, r14
00AF6784  E8 7F 9C C4 FF                  call 0x140740408
00AF6789  E9 D7 00 00 00                  jmp 0x140af6865
00AF678E  81 EB EB 00 00 00               sub ebx, 0xeb
00AF6794  0F 84 B5 00 00 00               je 0x140af684f
00AF679A  83 EB 08                        sub ebx, 8
00AF679D  0F 84 69 EB FF FF               je 0x140af530c
00AF67A3  83 EB 02                        sub ebx, 2
00AF67A6  74 4D                           je 0x140af67f5
00AF67A8  83 FB 01                        cmp ebx, 1
00AF67AB  0F 85 00 EA FF FF               jne 0x140af51b1
00AF67B1  41 83 FF 04                     cmp r15d, 4
00AF67B5  74 0A                           je 0x140af67c1
00AF67B7  B8 04 00 00 C0                  mov eax, 0xc0000004
00AF67BC  E9 A8 00 00 00                  jmp 0x140af6869
00AF67C1  41 8A D4                        mov dl, r12b
00AF67C4  48 8B 0D B5 32 4E 00            mov rcx, qword ptr [rip + 0x4e32b5]
00AF67CB  E8 50 B6 D7 FF                  call 0x140871e20
00AF67D0  84 C0                           test al, al
00AF67D2  75 0A                           jne 0x140af67de
00AF67D4  B8 61 00 00 C0                  mov eax, 0xc0000061
00AF67D9  E9 8B 00 00 00                  jmp 0x140af6869
00AF67DE  41 8B 06                        mov eax, dword ptr [r14]
00AF67E1  89 84 24 A0 01 00 00            mov dword ptr [rsp + 0x1a0], eax
00AF67E8  89 05 EE 05 4D 00               mov dword ptr [rip + 0x4d05ee], eax
00AF67EE  E9 78 E9 FF FF                  jmp 0x140af516b
00AF67F3  EB 74                           jmp 0x140af6869
00AF67F5  41 83 FF 04                     cmp r15d, 4
00AF67F9  0F 85 A3 EC FF FF               jne 0x140af54a2
00AF67FF  41 8A D4                        mov dl, r12b
00AF6802  48 8B 0D 77 32 4E 00            mov rcx, qword ptr [rip + 0x4e3277]
00AF6809  E8 12 B6 D7 FF                  call 0x140871e20
00AF680E  84 C0                           test al, al
00AF6810  75 07                           jne 0x140af6819
00AF6812  BF 61 00 00 C0                  mov edi, 0xc0000061
00AF6817  EB 4E                           jmp 0x140af6867
00AF6819  41 8B 06                        mov eax, dword ptr [r14]
00AF681C  89 84 24 08 01 00 00            mov dword ptr [rsp + 0x108], eax
00AF6823  8D 88 9F 0F 00 00               lea ecx, [rax + 0xf9f]
00AF6829  48 B8 77 BE 9F 1A 2F DD 24 06   movabs rax, 0x624dd2f1a9fbe77
00AF6833  48 F7 E1                        mul rcx
00AF6836  48 2B CA                        sub rcx, rdx
00AF6839  48 D1 E9                        shr rcx, 1
00AF683C  48 03 CA                        add rcx, rdx
00AF683F  48 C1 E9 0B                     shr rcx, 0xb
00AF6843  89 0D A3 87 3F 00               mov dword ptr [rip + 0x3f87a3], ecx
00AF6849  EB 1C                           jmp 0x140af6867
00AF684B  8B F8                           mov edi, eax
00AF684D  EB 18                           jmp 0x140af6867
00AF684F  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00AF6854  45 33 C9                        xor r9d, r9d
00AF6857  45 8A C4                        mov r8b, r12b
00AF685A  41 8B D7                        mov edx, r15d
00AF685D  49 8B CE                        mov rcx, r14
00AF6860  E8 17 15 C2 FF                  call 0x140717d7c
00AF6865  8B F8                           mov edi, eax
00AF6867  8B C7                           mov eax, edi
00AF6869  48 8B 8C 24 20 05 00 00         mov rcx, qword ptr [rsp + 0x520]
00AF6871  48 33 CC                        xor rcx, rsp
00AF6874  E8 C7 5D BB FF                  call 0x1406ac640
00AF6879  48 81 C4 30 05 00 00            add rsp, 0x530
00AF6880  41 5F                           pop r15
00AF6882  41 5E                           pop r14
00AF6884  41 5D                           pop r13
00AF6886  41 5C                           pop r12
00AF6888  5F                              pop rdi
00AF6889  5E                              pop rsi
00AF688A  5B                              pop rbx
00AF688B  C3                              ret
00AF688C  CC                              int3
00AF688D  E8 3E 37 DA FF                  call 0x140899fd0
00AF6892  90                              nop
00AF6893  E8 38 37 DA FF                  call 0x140899fd0
00AF6898  90                              nop
00AF6899  E8 32 37 DA FF                  call 0x140899fd0
00AF689E  90                              nop
00AF689F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSetSystemInformation(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m348;
    unsigned __int64 v_stack_m3A8;
    unsigned __int64 v_stack_m3B0;
    unsigned int v_stack_m3B4;
    unsigned __int16 v_stack_m3B6;
    unsigned int v_stack_m3B8;
    unsigned __int16 v_stack_m3BE;
    unsigned int v_stack_m3C0;
    unsigned __int64 v_stack_m3C8;
    unsigned __int64 v_stack_m3D8;
    unsigned __int64 v_stack_m3E0;
    unsigned __int64 v_stack_m3E8;
    unsigned __int64 v_stack_m3F0;
    unsigned __int64 v_stack_m3F8;
    unsigned __int64 v_stack_m400;
    unsigned __int64 v_stack_m410;
    unsigned __int64 v_stack_m418;
    unsigned __int64 v_stack_m428;
    unsigned __int64 v_stack_m430;
    unsigned __int64 v_stack_m438;
    unsigned int v_stack_m440;
    unsigned int v_stack_m444;
    unsigned int v_stack_m448;
    unsigned __int64 v_stack_m450;
    unsigned __int64 v_stack_m458;
    unsigned int v_stack_m460;
    unsigned int v_stack_m464;
    unsigned int v_stack_m468;
    unsigned __int64 v_stack_m470;
    unsigned __int64 v_stack_m478;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m480;
    unsigned __int64 v_stack_m488;
    unsigned __int64 v_stack_m490;
    unsigned __int64 v_stack_m498;
    unsigned __int64 v_stack_m4A0;
    unsigned __int64 v_stack_m4A8;
    unsigned __int64 v_stack_m4B0;
    unsigned int v_stack_m4B8;
    unsigned __int64 v_stack_m4C0;
    unsigned __int64 v_stack_m4C8;
    unsigned int v_stack_m4D0;
    unsigned __int64 v_stack_m4D8;
    unsigned int v_stack_m4E0;
    unsigned int v_stack_m4E4;
    unsigned __int8 v_stack_m4E8;
    unsigned int v_stack_m4F0;
    unsigned int v_stack_m4F4;
    unsigned __int8 v_stack_m4F8;
    unsigned __int64 v_stack_m500;
    unsigned __int16 v_stack_m506;
    unsigned __int64 v_stack_m508;
    unsigned __int8 v_stack_m514;
    unsigned __int8 v_stack_m52F;
    unsigned __int8 v_stack_m530;
    unsigned __int8 v_stack_m537;
    unsigned __int8 v_stack_m538;
    unsigned __int64 v_stack_m540;
    unsigned __int64 v_stack_m548;

    v_rsp = (v_rsp) - (0x530ULL);
    result = (*(unsigned __int64 *)(v_rip + 3235012)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m410 = v_xmm0;
    v_rsi = 0;
    v_stack_m538 = 0;
    v_stack_m508 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 1200) = 0;
    v_stack_m514 = 0;
    v_stack_m4F0 = (unsigned int)(v_rsi + 1);
    *(unsigned __int64 *)(v_rsp - 1168) = 0;
    *(unsigned __int64 *)(v_rsp - 1176) = 0;
    *(unsigned __int64 *)(v_rsp - 1192) = 0;
    *(unsigned __int64 *)(v_rsp - 1184) = 0;
    *(unsigned __int64 *)(v_rsp - 1240) = 0;
    a2 = 0;
    result = memset(v_rsp - 968, a2, v_rsi + 1 + 127, a4);
    v_stack_m530 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF4B70;
    if (((unsigned int)((unsigned int)(a1))) != 89) goto loc_00AF4B14;
    goto loc_00AF4B41;
loc_00AF4B14:
    if (((unsigned int)((unsigned int)(a1))) == 204) goto loc_00AF4B3C;
    if (((unsigned int)((unsigned int)(a1))) == 210) goto loc_00AF4B3C;
    if (((unsigned int)((unsigned int)(a1))) == 212) goto loc_00AF4B3C;
    if (((unsigned int)((unsigned int)(a1))) != 151) goto loc_00AF4B3C;
    result = 0;
    if (((unsigned int)((unsigned int)(a3))) != ((unsigned int)(v_rsi + 1))) {
        result = 3;
    }
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_00AF4B69;
    if (((result) & (0)) != 0) goto loc_00AF688D;
    if ((a2 + (unsigned int)(a3) * 1) > result) goto loc_00AF4B67;
    if ((a2 + (unsigned int)(a3) * 1) < 0) {
        result = *(unsigned __int8 *)(result);
    }
    goto loc_00AF4B70;
loc_00AF4B70:
    if (((unsigned int)((unsigned int)(a1))) > 113) goto loc_00AF5AD0;
    if (((unsigned int)((unsigned int)(a1))) == 113) goto loc_00AF5ABD;
    if (((unsigned int)((unsigned int)(a1))) > 71) goto loc_00AF5457;
    if (((unsigned int)((unsigned int)(a1))) == 71) goto loc_00AF59BB;
    if (((unsigned int)((unsigned int)(a1))) > 39) goto loc_00AF5177;
    if (((unsigned int)((unsigned int)(a1))) == 39) goto loc_00AF5138;
    if (((unsigned int)((unsigned int)(a1))) > 28) goto loc_00AF4DF1;
    if (((unsigned int)((unsigned int)(a1))) == 28) goto loc_00AF4D22;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (9));
    if (condition_is_equal) goto loc_00AF4CC9;
    a1 = (unsigned int)((a1) - (12));
    if (condition_is_equal) goto loc_00AF55BF;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00AF4C06;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00AF5369;
    if (a1 != 1) goto loc_00AF51B1;
    if (((unsigned int)((unsigned int)(a3))) != 8) goto loc_00AF67B7;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_00AF67D4;
    v_stack_m3F8 = *(unsigned __int64 *)(a2);
    result = MmUnloadSystemImage(*(unsigned __int64 *)(a2), a2, v_rsi + 1 + 127, a4);
    goto loc_00AF516B;
loc_00AF4C06:
    if (((unsigned int)((unsigned int)(a3))) != 20) goto loc_00AF67B7;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF4C2C;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5132033), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_rsi + 1 + 127, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
loc_00AF4C2C:
    v_stack_m3C8 = v_xmm0;
    v_stack_m3B8 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)));
    result = (v_stack_m3C8) >> (32);
    *(unsigned int *)(v_rip + 5047403) = (unsigned int)(result);
    *(unsigned int *)(v_rip + 5047430) = (unsigned int)((unsigned int)(v_stack_m3C0));
    result = (v_stack_m3C0) >> (32);
    *(unsigned int *)(v_rip + 5047376) = (unsigned int)(result);
    *(unsigned int *)(v_rip + 5047590) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)));
    result = KeSynchronizeWithDynamicProcessors((unsigned int)(*(unsigned int *)(a2 + 16)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_rsi + 1 + 127, a4);
    result = KeQueryActiveProcessorCountEx((unsigned int)(0xFFFFULL), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_rsi + 1 + 127, a4);
    if ((unsigned int)(result) == 0) goto loc_00AF6867;
loc_00AF4C9B:
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 5062568) + 14504) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5047324)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 5062568) + 14512) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5047352)));
    a3 = ((unsigned int)((unsigned int)(result))) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_00AF4C9B;
    goto loc_00AF6867;
loc_00AF4CC9:
    if (((unsigned int)((unsigned int)(a3))) != 4) goto loc_00AF54A2;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5131683), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00AF4CF0;
loc_00AF4CE6:
    goto loc_00AF6867;
loc_00AF4CF0:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 5043658))) & (0x6DCE640FULL));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (0x92319BF0ULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    v_stack_m448 = a1;
    *(unsigned int *)(v_rip + 5043629) = a1;
    *(unsigned int *)(a2) = a1;
    goto loc_00AF6867;
loc_00AF4D22:
    if ((((unsigned int)((unsigned int)(a3) - 8)) & (0xFFFFFFF7ULL)) != 0) goto loc_00AF67B7;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF4D4D;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5131936), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
loc_00AF4D4D:
    result = PsIsCurrentThreadInServerSilo(*(unsigned __int64 *)(v_rip + 5131936), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00AF6695;
    if (((unsigned int)((unsigned int)(a3))) != 16) goto loc_00AF4DB1;
    v_stack_m538 = (unsigned __int8)(*(unsigned __int8 *)(a2 + 8));
    v_stack_m4D8 = *(unsigned __int64 *)(a2);
loc_00AF4D73:
loc_00AF4D7D:
    result = *(unsigned __int64 *)(a2);
    if ((unsigned __int8)(*(unsigned __int8 *)(a2 + 8)) != 0) {
        result = *(unsigned __int64 *)(a3);
        v_stack_m4D8 = result;
    }
    result = ExAcquireTimeRefreshLockExclusive(*(unsigned __int8 *)(a2 + 8), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, a4);
    a1 = 0;
    result = ExpUpdateTimerConfiguration(a1, v_stack_m4D8, v_stack_m538, a4);
    result = ExReleaseTimeRefreshLockExclusive(a1, v_stack_m4D8, v_stack_m538, a4);
    goto loc_00AF6867;
loc_00AF4DB1:
    v_stack_m538 = (unsigned __int8)(*(unsigned __int8 *)(a2 + 4));
    v_stack_m4D8 = (unsigned int)(*(unsigned int *)(a2));
    if ((unsigned int)(*(unsigned int *)(a2)) == 0) goto loc_00AF4D73;
    result = ((unsigned int)(*(unsigned int *)(v_rip + 5053649))) * (*(unsigned __int64 *)(v_stack_m538));
    a2 = 0;
    v_stack_m4D8 = result;
    goto loc_00AF4D7D;
loc_00AF4DF1:
    v_rbx = (unsigned int)(((unsigned int)(a1)) - (30));
    if (condition_is_equal) goto loc_00AF512E;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00AF511B;
    v_rbx = (unsigned int)((v_rbx) - (3));
    if (condition_is_equal) goto loc_00AF507E;
    v_rbx = (unsigned int)((v_rbx) - (3));
    if (condition_is_equal) goto loc_00AF504B;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00AF51B1;
    if ((((unsigned int)((unsigned int)(a3) - 16)) & (0xFFFFFFF7ULL)) != 0) goto loc_00AF67B7;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF4F89;
    v_stack_m4E0 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 2012)))) & (8)) == 0) goto loc_00AF67D4;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5131451), (unsigned __int8)(v_rsi + 1), v_stack_m538, (unsigned int)(*(unsigned int *)(a2)));
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    if (((unsigned int)((unsigned int)(a3))) != 16) goto loc_00AF4EC0;
    v_stack_m4C8 = v_xmm0;
    result = RtlReadULongFromUser(0, (unsigned __int8)(v_rsi + 1), v_stack_m538, (unsigned int)(*(unsigned int *)(a2)));
    v_stack_m4C8 = (unsigned int)(result);
    result = RtlReadULong64FromUser(a2 + 8, (unsigned __int8)(v_rsi + 1), v_stack_m538, (unsigned int)(*(unsigned int *)(a2)));
    v_stack_m4C0 = result;
    v_stack_m508 = v_xmm0;
    goto loc_00AF4EF4;
loc_00AF4EC0:
    result = RtlCopyFromUser(v_stack_m3C8, (unsigned int)(v_stack_m4E0), 24, (unsigned int)(*(unsigned int *)(a2)));
    v_stack_m508 = v_xmm0;
    v_stack_m4E0 = (unsigned int)((unsigned int)(v_stack_m3C8));
loc_00AF4EF4:
    if (v_stack_m508 != 62) goto loc_00AF67D4;
    result = RtlCopyFromUser(v_stack_m3C8, v_stack_m500, 62, (unsigned int)(*(unsigned int *)(a2)));
    result = memcmp(v_stack_m3C8, v_rip - 11256900, 62, (unsigned int)(*(unsigned int *)(a2)));
    if ((unsigned int)(result) != 0) goto loc_00AF67D4;
    v_stack_m500 = v_rip - 11256900;
    v_stack_m506 = 62;
    v_stack_m3B8 = v_rip - 11256900;
    v_stack_m3BE = 62;
    v_r14 = (unsigned int)(v_stack_m3C8);
    if (((unsigned int)((unsigned int)(a3))) == 16) { v_r14 = 0; }
    v_stack_m3C8 = (unsigned int)(v_r14);
    result = ZwSetSystemInformation(result + 38, v_stack_m3C8, result + 24, (unsigned int)(*(unsigned int *)(a2)));
    goto loc_00AF6869;
loc_00AF4F89:
    if (((unsigned int)((unsigned int)(a3))) != 16) goto loc_00AF4F9A;
    goto loc_00AF4FAF;
loc_00AF4F9A:
    v_r14 = (unsigned __int8)((unsigned int)(v_stack_m514));
    if (((*(unsigned __int8 *)((unsigned int)(v_stack_m514))) & ((unsigned __int8)(v_rsi + 1))) != 0) { v_r14 = (unsigned int)(v_rsi + 1); }
loc_00AF4FAF:
    v_stack_m508 = v_xmm0;
    result = memcmp(v_stack_m500, v_rip - 11257058, 62, (unsigned int)(*(unsigned int *)(a2)));
    if ((unsigned int)(result) != 0) goto loc_00AF59BB;
    result = RtlImageNtHeader(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4265973) + 48), v_rip - 11257058, 62, (unsigned int)(*(unsigned int *)(a2)));
    if (result != 0) goto loc_00AF5002;
    result = MmUnloadSystemImage(*(unsigned __int64 *)(v_rip + 4265949), v_rip - 11257058, 62, (unsigned int)(*(unsigned int *)(a2)));
    goto loc_00AF6869;
loc_00AF5002:
    a1 = ((unsigned int)(*(unsigned int *)((unsigned int)(0xC000007BULL) + 40))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4265973) + 48));
    result = ExpInitializeSessionDriver(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4265973) + 48), (unsigned __int8)(v_r14), (unsigned int)(*(unsigned int *)(a2)));
    if (!sign_flag) goto loc_00AF6867;
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4265973) + 48), (unsigned __int8)(v_r14), (unsigned int)(*(unsigned int *)(a2)));
    if ((unsigned int)(result) != 0) goto loc_00AF6867;
    result = MmUnloadSystemImage(*(unsigned __int64 *)(v_rip + 4265871), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4265973) + 48), (unsigned __int8)(v_r14), (unsigned int)(*(unsigned int *)(a2)));
    goto loc_00AF6867;
loc_00AF504B:
    if (((unsigned int)((unsigned int)(a3))) != 16) goto loc_00AF67B7;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF5071;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5131020), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(v_r14), (unsigned int)(*(unsigned int *)(a2)));
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
loc_00AF5071:
    result = CmSetRegistryQuotaInformation(v_r14, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(v_r14), (unsigned int)(*(unsigned int *)(a2)));
    goto loc_00AF6865;
loc_00AF507E:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF509A;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5130739), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(v_r14), (unsigned int)(*(unsigned int *)(a2)));
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
loc_00AF509A:
    result = PsIsCurrentThreadInServerSilo(*(unsigned __int64 *)(v_rip + 5130739), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(v_r14), (unsigned int)(*(unsigned int *)(a2)));
    if ((unsigned __int8)(result) != 0) goto loc_00AF67D4;
    if (((unsigned int)((unsigned int)(a3))) == 4) goto loc_00AF50BC;
loc_00AF50AD:
    a2 = 0;
loc_00AF50B2:
    result = IoConfigureCrashDump((unsigned int)((unsigned int)(v_rsi + 1)), a2, (unsigned __int8)(v_r14), (unsigned int)(*(unsigned int *)(a2)));
    goto loc_00AF6865;
loc_00AF50BC:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF50F6;
    if ((((unsigned __int8)(v_r14)) & (3)) != 0) goto loc_00AF6893;
    if ((v_r14 + 4) > result) goto loc_00AF50E3;
    if ((v_r14 + 4) < v_r14) {
        result = *(unsigned __int8 *)(result);
    }
    v_stack_m444 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14)));
    goto loc_00AF50F9;
loc_00AF50F6:
loc_00AF50F9:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14))) == 0) goto loc_00AF5115;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14))) - (1));
    if (condition_is_equal) goto loc_00AF50AD;
    if (a1 != 1) goto loc_00AF6566;
    result = WheaCrashDumpInitializationComplete(a1, a2, (unsigned __int8)(v_r14), (unsigned int)(*(unsigned int *)(a2)));
    goto loc_00AF6865;
loc_00AF5115:
    a2 = 0;
    a1 = 0;
    goto loc_00AF50B2;
loc_00AF511B:
    result = EtwSetPerformanceTraceInformation(v_r14, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(*(unsigned int *)(a2)));
    goto loc_00AF6865;
loc_00AF512E:
    result = MmCreateMirror(v_r14, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(*(unsigned int *)(a2)));
    goto loc_00AF6865;
loc_00AF5138:
    if (((unsigned int)((unsigned int)(a3))) != 4) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5130540), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(*(unsigned int *)(a2)));
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    v_stack_m440 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14)));
    result = PsChangeQuantumTable((unsigned __int8)(v_rsi + 1), (unsigned int)(*(unsigned int *)(v_r14)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(*(unsigned int *)(a2)));
loc_00AF516B:
    goto loc_00AF6867;
loc_00AF5177:
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4265973) + 48))) > 51) goto loc_00AF52F4;
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4265973) + 48))) == 51) goto loc_00AF52CA;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4265973) + 48)))) - (40));
    if (condition_is_equal) goto loc_00AF5254;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF5254;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_00AF51BB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF5514;
    if (a1 == 1) goto loc_00AF5514;
loc_00AF51B1:
    goto loc_00AF6867;
loc_00AF51BB:
    if (((unsigned int)((unsigned int)(a3))) != 8) goto loc_00AF67B7;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF51E1;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5130764), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(*(unsigned int *)(a2)));
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
loc_00AF51E1:
    result = PsIsCurrentThreadInServerSilo(*(unsigned __int64 *)(v_rip + 5130764), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(*(unsigned int *)(a2)));
    if ((unsigned __int8)(result) != 0) goto loc_00AF6695;
    v_stack_m458 = *(unsigned __int64 *)(v_r14);
    if (*(unsigned __int64 *)(v_r14) != 0) goto loc_00AF5205;
    goto loc_00AF5245;
loc_00AF5205:
    v_stack_m4C8 = 0;
    v_stack_m540 = 0;
    v_stack_m548 = v_stack_m4C8;
    result = ObReferenceObjectByHandle(0, 2, *(unsigned __int64 *)(v_rip + 5052788), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_00AF6867;
loc_00AF5245:
    result = KdUpdateTimeSlipEvent(v_stack_m4C8, 2, *(unsigned __int64 *)(v_rip + 5052788), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_00AF6867;
loc_00AF5254:
    if (((unsigned int)((unsigned int)(a3))) != 16) goto loc_00AF67B7;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF52A2;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5130259), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_rip + 5052788), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    result = VfProbeAndCaptureUnicodeString(v_stack_m508, v_r14, (unsigned int)((unsigned int)(v_rsi + 1)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_00AF6869;
    if (v_stack_m508 == 0) goto loc_00AF661D;
loc_00AF52A2:
    v_rbx = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4265973) + 48)) - (40));
    if (condition_is_equal) goto loc_00AF52BD;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00AF6634;
    result = VfRemoveVerifierEntry(v_stack_m508, v_r14, (unsigned int)((unsigned int)(v_rsi + 1)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_00AF664D;
loc_00AF52BD:
    result = VfAddVerifierEntry(v_stack_m508, v_r14, (unsigned int)((unsigned int)(v_rsi + 1)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_00AF664D;
loc_00AF52CA:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5130156), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)((unsigned int)(v_rsi + 1)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if ((unsigned __int8)(result) == 0) goto loc_00AF6695;
    a3 = 0;
    result = VfSetVerifierInformation(v_stack_m508, (unsigned int)((unsigned int)((unsigned int)(a3))), a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_00AF6865;
loc_00AF52F4:
    if (((unsigned int)(v_rbx)) == 54) goto loc_00AF5365;
    if (((unsigned int)(v_rbx)) == 56) goto loc_00AF5352;
    if (((unsigned int)(v_rbx)) == 59) goto loc_00AF5316;
    if (((unsigned int)(v_rbx)) != 69) goto loc_00AF51B1;
loc_00AF530C:
    goto loc_00AF6867;
loc_00AF5316:
    if (((unsigned int)((unsigned int)(a3))) != 4) goto loc_00AF67B7;
    v_stack_m468 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m508)));
    result = ExpUpdateComPlusPackage((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m508)))), (unsigned int)((unsigned int)((unsigned int)(a3))), a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_00AF6867;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 5045446) + 736) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m508)));
    goto loc_00AF6867;
loc_00AF5352:
    result = PfSnSetPrefetcherInformation((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m508)))), v_stack_m508, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_00AF6865;
loc_00AF5365:
    goto loc_00AF536D;
loc_00AF5369:
loc_00AF536D:
    if (((unsigned int)((unsigned int)(a3))) != 48) goto loc_00AF5378;
    goto loc_00AF5385;
loc_00AF5378:
    if (0 != 56) goto loc_00AF67B7;
loc_00AF5385:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_00AF67D4;
    v_stack_m508 = v_xmm0;
    v_stack_m540 = v_stack_m4B0;
    v_stack_m548 = v_stack_m4A8;
    a3 = 0;
    a2 = 0;
    result = MmLoadSystemImage(v_stack_m508, a2, a3, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4F0))));
    if (sign_flag) goto loc_00AF543D;
    if ((unsigned __int8)((unsigned __int8)(v_rsi + 1)) == 0) goto loc_00AF53F2;
    a3 = 0;
    result = RtlImageDirectoryEntryToData(v_stack_m4B0, (unsigned __int8)(v_rsi + 1), a3, v_stack_m4C8);
    goto loc_00AF53F5;
loc_00AF53F2:
loc_00AF53F5:
    result = RtlImageNtHeader(v_stack_m4B0, (unsigned __int8)(v_rsi + 1), a3, v_stack_m4C8);
    a2 = ((unsigned int)(*(unsigned int *)(result + 40))) + (v_stack_m4B0);
    *(unsigned __int64 *)(v_stack_m508 + 16) = v_stack_m4B0;
    *(unsigned __int64 *)(v_stack_m508 + 24) = v_stack_m4A8;
    *(unsigned __int64 *)(v_stack_m508 + 32) = a2;
    if ((unsigned __int8)((unsigned __int8)(v_rsi + 1)) == 0) goto loc_00AF542A;
    *(unsigned __int64 *)(v_stack_m508 + 40) = 0;
    *(unsigned int *)(v_stack_m508 + 48) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 80)));
    goto loc_00AF5431;
loc_00AF542A:
    *(unsigned int *)(v_stack_m508 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 80)) + 80)));
loc_00AF5431:
    goto loc_00AF6867;
loc_00AF543D:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(result + 80)) + 80)))) != 0xC000019DULL) goto loc_00AF6867;
    goto loc_00AF6867;
loc_00AF5457:
    if (((unsigned int)(v_stack_m4B0)) > 92) goto loc_00AF587E;
    if (((unsigned int)(v_stack_m4B0)) == 92) goto loc_00AF5850;
    if (((unsigned int)(v_stack_m4B0)) > 81) goto loc_00AF5664;
    if (((unsigned int)(v_stack_m4B0)) == 81) goto loc_00AF55BF;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m4B0))) - (72));
    if (condition_is_equal) goto loc_00AF551E;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00AF5514;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF5501;
    a1 = (unsigned int)((a1) - (4));
    if (condition_is_equal) goto loc_00AF54EC;
    if (a1 != 1) goto loc_00AF51B1;
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) >= 4) goto loc_00AF54AC;
loc_00AF54A2:
    goto loc_00AF6867;
loc_00AF54AC:
    v_stack_m4D0 = 6;
    v_stack_m4D0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m508)));
    goto loc_00AF54D3;
loc_00AF54D3:
    if (sign_flag) goto loc_00AF6867;
    a3 = (a3) | (-1);
    result = MmIssueMemoryListCommand((unsigned int)(*(unsigned int *)(v_stack_m508)), 0, a3, v_stack_m4C8);
    goto loc_00AF6865;
loc_00AF54EC:
    result = PfSetSuperfetchInformation((unsigned int)((unsigned int)(v_stack_m4B0)), v_stack_m508, (unsigned int)((unsigned int)((unsigned __int8)(v_rsi + 1))), 0);
    goto loc_00AF6865;
loc_00AF5501:
    result = ExpRegisterFirmwareTableInformationHandler(v_stack_m508, (unsigned int)((unsigned int)((unsigned __int8)(v_rsi + 1))), 0, 0);
    goto loc_00AF6865;
loc_00AF5514:
    goto loc_00AF6869;
loc_00AF551E:
    if (0 != 0) goto loc_00AF6566;
    if (v_stack_m508 == 0) goto loc_00AF6566;
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) != 8) goto loc_00AF6566;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m508))) == 0) goto loc_00AF530C;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m508))) - (1));
    if (condition_is_equal) goto loc_00AF55AE;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF55A5;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF559C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF530C;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00AF5588;
    if (a1 != 1) goto loc_00AF61E2;
    v_rdi = 0;
    if ((*(unsigned __int64 *)(v_rip + 3192248)) == (v_rip - 6262649)) { v_rdi = (unsigned int)((unsigned int)(0xC0000002ULL)); }
    goto loc_00AF6867;
loc_00AF5588:
    result = guard_dispatch_icall((unsigned __int8)(v_rsi + 1), v_rip - 6262649, 0, 0);
    goto loc_00AF6865;
loc_00AF559C:
    goto loc_00AF55B5;
loc_00AF55A5:
    goto loc_00AF55B5;
loc_00AF55AE:
loc_00AF55B5:
    result = guard_dispatch_icall((unsigned __int8)(v_rsi + 1), v_rip - 6262649, 0, 0);
    goto loc_00AF516B;
loc_00AF55BF:
    v_stack_m52F = 0;
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) < 64) goto loc_00AF67B7;
    if (((unsigned int)(v_stack_m4B0)) != 21) goto loc_00AF55DE;
    v_stack_m4B8 = 0;
    goto loc_00AF5603;
loc_00AF55DE:
    v_stack_m4B8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m508 + 60)));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m508 + 60)))) & (0xFFFFFFF0ULL)) != 0) goto loc_00AF5655;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m508 + 60))))) & (12));
    if (((unsigned __int8)(result)) == 12) goto loc_00AF5655;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m508 + 60))))) & (3));
    if (((unsigned __int8)(result)) == 3) goto loc_00AF5655;
loc_00AF5603:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5129571), 0, 0, 0);
    if ((unsigned __int8)(result) == 0) goto loc_00AF6695;
    v_stack_m3F0 = *(unsigned __int64 *)(v_stack_m508 + 24);
    v_stack_m3E8 = *(unsigned __int64 *)(v_stack_m508 + 32);
    v_stack_m540 = v_stack_m52F;
    v_stack_m548 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m508 + 60)));
    result = MmAdjustWorkingSetSizeEx(*(unsigned __int64 *)(v_stack_m508 + 24), *(unsigned __int64 *)(v_stack_m508 + 32), (unsigned int)((unsigned int)(v_rsi + 1)), (unsigned __int8)(v_rsi + 1));
    goto loc_00AF6869;
loc_00AF5655:
    goto loc_00AF6869;
loc_00AF5664:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m508 + 60))) - (82));
    if (condition_is_equal) goto loc_00AF578F;
    v_rbx = (unsigned int)((v_rbx) - (4));
    if (condition_is_equal) goto loc_00AF577F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00AF572C;
    v_rbx = (unsigned int)((v_rbx) - (2));
    if (condition_is_equal) goto loc_00AF56BC;
    if (((unsigned int)(v_rbx)) != 2) goto loc_00AF51B1;
    if (0 != 0) goto loc_00AF4CE6;
    if ((unsigned int)((unsigned __int8)(v_rsi + 1)) == 0) goto loc_00AF56A5;
    goto loc_00AF6867;
loc_00AF56A5:
    result = (unsigned __int8)(-(*(unsigned __int8 *)(v_rip + 5051372)));
    v_rdi = (unsigned int)(~((unsigned int)(0xC00000F0ULL)));
    v_rdi = (unsigned int)((v_rdi) & (0xC0351000ULL));
    goto loc_00AF6867;
loc_00AF56BC:
    if (0 != ((unsigned __int8)(v_rsi + 1))) goto loc_00AF530C;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5129129), (unsigned __int8)(v_rsi + 1), (unsigned int)((unsigned int)(v_rsi + 1)), (unsigned __int8)(v_rsi + 1));
    if ((unsigned __int8)(result) == 0) goto loc_00AF6812;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) == 0) goto loc_00AF571C;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) == 332) goto loc_00AF5713;
    v_r13 = v_rsi + 1;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) != 452) {
        v_r13 = 0;
    }
    if ((unsigned __int8)(v_r13) != 0) goto loc_00AF530C;
loc_00AF571C:
    result = DbgkRegisterErrorPort(v_stack_m508, (unsigned int)((unsigned int)((unsigned __int8)(v_rsi + 1))), (unsigned int)((unsigned int)(v_rsi + 1)), (unsigned __int8)(v_rsi + 1));
    goto loc_00AF6865;
loc_00AF572C:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5129034), 0, (unsigned int)((unsigned int)(v_rsi + 1)), (unsigned __int8)(v_rsi + 1));
    if ((unsigned __int8)(result) == 0) goto loc_00AF4CE6;
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) != 8) goto loc_00AF54A2;
    v_stack_m3C8 = *(unsigned __int64 *)(v_stack_m508);
    *(unsigned int *)(v_rip + 5051587) = (unsigned int)((unsigned int)(v_stack_m3C8));
    result = (*(unsigned __int64 *)(v_stack_m508)) >> (32);
    a1 = (unsigned int)(((unsigned __int8)(result)) & ((unsigned int)(v_r13)));
    *(unsigned int *)(v_rip + 5044655) = a1;
    goto loc_00AF6867;
loc_00AF577F:
    result = ObSetRefTraceInformation(v_stack_m508, (unsigned int)((unsigned int)((unsigned __int8)(v_rsi + 1))), (unsigned int)((unsigned int)(v_rsi + 1)), (unsigned __int8)(v_rsi + 1));
    goto loc_00AF6865;
loc_00AF578F:
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) < 24) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5129029), 0, (unsigned int)((unsigned int)(v_rsi + 1)), (unsigned __int8)(v_rsi + 1));
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    if (0 == 0) goto loc_00AF57DF;
    v_stack_m3C8 = v_xmm0;
    v_stack_m3B8 = v_xmm1;
    goto loc_00AF57DF;
loc_00AF57DF:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m3C8 + 16))) - ((unsigned int)(v_r13)));
    if (((unsigned int)(result)) > 30) goto loc_00AF6566;
    v_stack_m410 = v_xmm0;
    a2 = 0;
    result = PsLookupProcessThreadByCid(v_stack_m410, a2, v_stack_m4A0, (unsigned __int8)(v_rsi + 1));
    if (sign_flag) goto loc_00AF6867;
    if ((*(unsigned __int8 *)(v_stack_m4A0 + 4)) == 0) goto loc_00AF5832;
    goto loc_00AF5843;
loc_00AF5832:
    result = KeSetActualBasePriorityThread(v_stack_m4A0, (unsigned int)(*(unsigned int *)(v_stack_m3C8 + 16)), v_stack_m4A0, (unsigned __int8)(v_rsi + 1));
loc_00AF5843:
    result = ObfDereferenceObject(v_stack_m4A0, (unsigned int)(*(unsigned int *)(v_stack_m3C8 + 16)), v_stack_m4A0, (unsigned __int8)(v_rsi + 1));
    goto loc_00AF6867;
loc_00AF5850:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5128742), 0, v_stack_m4A0, (unsigned __int8)(v_rsi + 1));
    if ((unsigned __int8)(result) == 0) goto loc_00AF6695;
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) != 40) goto loc_00AF67B7;
    result = VfSetVerifierInformationEx(v_stack_m3C8, 0, v_stack_m4A0, (unsigned __int8)(v_rsi + 1));
    goto loc_00AF6865;
loc_00AF587E:
    if (((unsigned int)(v_stack_m4A0)) > 104) goto loc_00AF5A49;
    if (((unsigned int)(v_stack_m4A0)) == 104) goto loc_00AF5A36;
    v_rbx = (unsigned int)((v_stack_m4A0) - (93));
    if (condition_is_equal) goto loc_00AF5A2C;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00AF59C5;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00AF59BB;
    v_rbx = (unsigned int)((v_rbx) - (2));
    if (condition_is_equal) goto loc_00AF58F3;
    if (((unsigned int)(v_rbx)) != 5) goto loc_00AF51B1;
loc_00AF58BF:
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) != 432) goto loc_00AF67B7;
    if (0 == 0) goto loc_00AF58E4;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5129369), 0, v_stack_m4A0, (unsigned __int8)(v_rsi + 1));
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
loc_00AF58E4:
    result = ExpSetTimeZoneInformation(v_stack_m3C8, 432, v_stack_m4A0, (unsigned __int8)(v_rsi + 1));
    goto loc_00AF6865;
loc_00AF58F3:
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) != 40) goto loc_00AF67B7;
    if (0 == 0) goto loc_00AF5996;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5128560), 0, v_stack_m4A0, (unsigned __int8)(v_rsi + 1));
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    v_stack_m3C8 = v_xmm0;
    v_stack_m3B8 = v_xmm1;
    v_stack_m3A8 = v_xmm0;
    result = VfProbeAndCaptureUnicodeStringBuffer(v_stack_m3C0, (unsigned int)((unsigned int)(v_r13)), v_stack_m4A0, (unsigned __int8)(v_rsi + 1));
    if (sign_flag) goto loc_00AF6869;
    result = VfProbeAndCaptureUnicodeStringBuffer(v_stack_m3B0, (unsigned int)((unsigned int)(v_r13)), v_stack_m4A0, (unsigned __int8)(v_rsi + 1));
    if (!sign_flag) goto loc_00AF5987;
    result = VfFreeCapturedUnicodeString(v_stack_m3C0, (unsigned int)((unsigned int)(v_r13)), v_stack_m4A0, (unsigned __int8)(v_rsi + 1));
    goto loc_00AF6869;
loc_00AF5987:
    goto loc_00AF5996;
loc_00AF5996:
    result = VfFaultsSetParameters(v_stack_m3C8, (unsigned int)((unsigned int)(v_r13)), v_stack_m4A0, (unsigned __int8)(v_rsi + 1));
    if (0 == 0) goto loc_00AF6867;
    result = VfFreeCapturedUnicodeString(v_stack_m3C8 + 8, (unsigned int)((unsigned int)(v_r13)), v_stack_m4A0, (unsigned __int8)(v_rsi + 1));
    goto loc_00AF665B;
loc_00AF59BB:
    goto loc_00AF6869;
loc_00AF59C5:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5128361), 0, v_stack_m4A0, (unsigned __int8)(v_rsi + 1));
    if ((unsigned __int8)(result) == 0) goto loc_00AF4CE6;
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) != 8) goto loc_00AF54A2;
    v_stack_m3C8 = *(unsigned __int64 *)(v_stack_m3C8);
    result = (v_stack_m3C8) >> (32);
    result = (unsigned int)(~(result));
    goto loc_00AF6867;
loc_00AF5A2C:
    goto loc_00AF58BF;
loc_00AF5A36:
    result = ExpSetProcessorMicrocodeUpdateInformation(v_stack_m3C8, (unsigned int)((unsigned int)((unsigned __int8)(v_rsi + 1))), 0, (unsigned __int8)(v_rsi + 1));
    goto loc_00AF6865;
loc_00AF5A49:
    v_rbx = (unsigned int)((172) - (106));
    if (condition_is_equal) goto loc_00AF51B1;
    v_rbx = (unsigned int)((v_rbx) - (3));
    if (condition_is_equal) goto loc_00AF5AAA;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00AF5AA0;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00AF51B1;
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) != 4) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5128335), 0, 0, (unsigned __int8)(v_rsi + 1));
    if ((unsigned __int8)(result) == 0) goto loc_00AF6695;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 5043576) + 584) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m3C8)));
    goto loc_00AF516B;
loc_00AF5AA0:
    goto loc_00AF6867;
loc_00AF5AAA:
    result = SmSetStoreInformation((unsigned int)(*(unsigned int *)(v_stack_m3C8)), v_stack_m3C8, (unsigned int)((unsigned int)((unsigned __int8)(v_rsi + 1))), 0);
    goto loc_00AF6865;
loc_00AF5ABD:
    result = PsSetCpuQuotaInformation(v_stack_m3C8, (unsigned int)((unsigned int)((unsigned __int8)(v_rsi + 1))), 0, 0);
    goto loc_00AF6865;
loc_00AF5AD0:
    if (((unsigned int)(v_rbx)) > 194) goto loc_00AF63D2;
    if (((unsigned int)(v_rbx)) == 194) goto loc_00AF6399;
    if (((unsigned int)(v_rbx)) > 155) goto loc_00AF6012;
    if (((unsigned int)(v_rbx)) == 155) goto loc_00AF6008;
    if (((unsigned int)(v_rbx)) > 132) goto loc_00AF5D97;
    if (((unsigned int)(v_rbx)) == 132) goto loc_00AF5CAA;
    v_rbx = (unsigned int)((v_rbx) - (126));
    if (condition_is_equal) goto loc_00AF5C8A;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00AF5C2C;
    v_rbx = (unsigned int)((v_rbx) - (2));
    if (condition_is_equal) goto loc_00AF5C19;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00AF5B5A;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00AF51B1;
    if (0 != 0) goto loc_00AF6695;
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) != 24) goto loc_00AF67B7;
    result = KeInitializeEntropySystem(*(unsigned __int64 *)(v_stack_m3C8), *(unsigned __int64 *)(v_stack_m3C8 + 8), *(unsigned __int64 *)(v_stack_m3C8 + 16), 0);
    goto loc_00AF6865;
loc_00AF5B5A:
    if ((((unsigned int)((unsigned __int8)(v_rsi + 1) - 16)) & (0xFFFFFFE7ULL)) != 0) goto loc_00AF67B7;
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) == 40) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5128075), 0, *(unsigned __int64 *)(v_stack_m3C8 + 16), 0);
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    result = memcpy(v_stack_m3C8, v_stack_m3C8, (unsigned __int8)(v_rsi + 1), 0);
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) == 32) { v_rsi = v_stack_m3B0; }
    result = MiGetThreadPartition(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m3C8, (unsigned __int8)(v_rsi + 1), 0);
    v_stack_m540 = v_stack_m498;
    v_stack_m548 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = MiCombineIdenticalPages(result, v_stack_m3C8, (unsigned int)(v_stack_m3B8), v_rsi);
    v_stack_m514 = (unsigned int)(result);
    *(unsigned __int64 *)(v_stack_m3C8 + 8) = v_stack_m498;
    goto loc_00AF6867;
loc_00AF5C19:
    result = KeProcessorProfileControlArea(v_stack_m3C8, (unsigned int)((unsigned int)((unsigned __int8)(v_rsi + 1))), 0, v_rsi);
    goto loc_00AF6865;
loc_00AF5C2C:
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) != 16) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5127880), 0, 0, v_rsi);
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    v_stack_m458 = *(unsigned __int64 *)(v_stack_m3C8);
    result = MmScrubMemory(*(unsigned __int64 *)(v_rip + 5127880), *(unsigned __int64 *)(v_stack_m3C8), v_stack_m490, v_rsi);
    v_stack_m514 = (unsigned int)(result);
    *(unsigned __int64 *)(v_stack_m3C8 + 8) = v_stack_m490;
    goto loc_00AF6867;
loc_00AF5C8A:
    if (0 != 0) goto loc_00AF67D4;
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) != 32) goto loc_00AF54A2;
    result = BgkSetBootGraphicsInformation(*(unsigned __int64 *)(v_rip + 5127880), v_stack_m3C8, v_stack_m490, v_rsi);
    goto loc_00AF6865;
loc_00AF5CAA:
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) != 4) goto loc_00AF67B7;
    v_stack_m488 = 0x760074ULL;
    v_stack_m480 = v_rip + 75561;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m3C8)) & ((unsigned __int8)(v_r13)));
    v_stack_m4E8 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_00AF5D69;
    v_rbx = (v_rbx) | (-1);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 5121315, a2, a3, v_rsi);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 5121315;
        a2 = result;
        a1 = v_rip + 5121315;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_rsi);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_r13);
    }
    result = ZwLoadDriver(v_stack_m488, a2, a3, v_rsi);
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = v_rip + 5121315;
        result = ExfTryToWakePushLock(a1, a2, a3, v_rsi);
    }
    result = KeAbPostRelease(v_rip + 5121315, a2, a3, v_rsi);
    result = KeLeaveCriticalRegion(v_rip + 5121315, a2, a3, v_rsi);
    goto loc_00AF6867;
loc_00AF5D69:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5127597), 0, a3, v_rsi);
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    result = ZwUnloadDriver(v_stack_m488, 0, a3, v_rsi);
    goto loc_00AF6865;
loc_00AF5D97:
    v_rbx = (unsigned int)((v_rbx) - (134));
    if (condition_is_equal) goto loc_00AF5FF1;
    v_rbx = (unsigned int)((v_rbx) - (8));
    if (condition_is_equal) goto loc_00AF5E96;
    v_rbx = (unsigned int)((v_rbx) - (8));
    if (condition_is_equal) goto loc_00AF5E6F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00AF5DF0;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00AF51B1;
    if (((unsigned int)((unsigned __int8)(v_rsi + 1))) != 8) goto loc_00AF67B7;
    if (0 == 0) goto loc_00AF6566;
    v_stack_m3E0 = *(unsigned __int64 *)(v_rip + 5121315);
    result = ExpQueryElamCertInfo(*(unsigned __int64 *)(v_rip + 5121315), 0, a3, v_rsi);
    goto loc_00AF6865;
loc_00AF5DF0:
    v_stack_m4F0 = 19;
    result = SeSinglePrivilegeCheck(v_stack_m4F0, 0, a3, v_rsi);
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    v_r15 = (unsigned int)(((unsigned __int8)(v_rsi + 1)) - (1));
    if (condition_is_equal) goto loc_00AF5E30;
    if (((unsigned int)(v_r15)) != 3) goto loc_00AF67B7;
    v_stack_m464 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5121315)));
    goto loc_00AF5E5D;
loc_00AF5E30:
    v_stack_m4F8 = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 5121315));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 5121315)) == 0) goto loc_00AF5E52;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5127219), 0, a3, v_rsi);
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
loc_00AF5E52:
    v_r13 = (unsigned int)(*(unsigned int *)(v_rip + 5121315));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 5121315)) == 0) { v_r13 = 5; }
loc_00AF5E5D:
    result = ExpSetSoftRebootFlags((unsigned int)((unsigned int)(v_r13)), 0, a3, v_rsi);
    goto loc_00AF6865;
loc_00AF5E6F:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5127167), 0, a3, v_rsi);
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    result = ExpSetBootLoaderMetadata(v_rip + 5121315, (unsigned int)((unsigned int)(v_r15)), a3, v_rsi);
    goto loc_00AF6865;
loc_00AF5E96:
    v_stack_m478 = v_xmm0;
    result = PsGetCurrentServerSiloGlobals(v_rip + 5121315, (unsigned int)((unsigned int)(v_r15)), a3, v_rsi);
    v_stack_m4F0 = result + 1368;
    if (((unsigned int)(v_r15)) != 48) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5127274), 0, a3, v_rsi);
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    v_stack_m3C8 = v_xmm2;
    v_stack_m3B8 = v_xmm0;
    v_stack_m3A8 = v_xmm1;
    result = 0;
    if (condition_is_equal) goto loc_00AF5F0C;
    result = 0;
    goto loc_00AF6869;
loc_00AF5F0C:
    v_stack_m478 = v_xmm1;
    v_stack_m3B8 = v_xmm0;
    if ((unsigned __int16)(*(unsigned __int8 *)(v_rip + 5121315)) == 0) goto loc_00AF5FC4;
    if ((((unsigned __int8)(v_r13)) & ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 5121315)))) != 0) goto loc_00AF5FC4;
    if ((((unsigned __int8)(v_r13)) & ((unsigned __int8)(v_stack_m470))) != 0) goto loc_00AF6899;
    a1 = ((unsigned __int16)(*(unsigned __int8 *)(v_rip + 5121315))) + (v_stack_m470);
    if (a1 > 0) goto loc_00AF5F68;
    v_rbx = *(unsigned __int8 *)(v_rip + 5121315);
    v_rdi = v_stack_m470;
    if (a1 < v_stack_m470) {
        result = *(unsigned __int8 *)(result);
        v_rdi = v_stack_m470;
        v_rbx = v_stack_m478;
    }
    result = ExAllocatePool2(257, (unsigned int)((unsigned int)((unsigned __int16)(v_rbx))), (unsigned int)(0x50535845ULL), v_rsi);
    if (result != 0) {
        a3 = (unsigned int)((unsigned __int16)(v_rbx));
        a2 = v_rdi;
        a1 = result;
        result = memcpy(a1, a2, a3, v_rsi);
        v_stack_m3B0 = result;
        v_stack_m3B8 = (unsigned __int16)(v_rbx);
        v_stack_m3B6 = (unsigned __int16)(v_rbx);
    }
loc_00AF5FC4:
    *(unsigned __int64 *)(v_stack_m4F0) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m4F0 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m4F0 + 32) = v_xmm0;
    goto loc_00AF516B;
loc_00AF5FF1:
    if (((unsigned int)((unsigned __int16)(v_rbx))) != 32) goto loc_00AF67B7;
    result = sub_00A179B0(a1, result, a3, v_rsi);
    goto loc_00AF6865;
loc_00AF6008:
    result = CmReconcileAndValidateAllHives(a1, result, a3, v_rsi);
    goto loc_00AF6865;
loc_00AF6012:
    if (((unsigned int)(v_rbx)) > 176) goto loc_00AF61B8;
    if (((unsigned int)(v_rbx)) == 176) goto loc_00AF6140;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (159));
    if (condition_is_equal) goto loc_00AF530C;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00AF610E;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00AF675C;
    a1 = (unsigned int)((a1) - (4));
    if (condition_is_equal) goto loc_00AF60B2;
    if (a1 != 2) goto loc_00AF51B1;
    v_stack_m438 = v_xmm0;
    if (((unsigned int)((unsigned __int16)(v_rbx))) != 16) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5126774), 0, a3, v_rsi);
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    v_stack_m438 = v_xmm0;
    a2 = (v_stack_m438) >> (32);
    result = KeIntSteerAssignCpuSetForGsiv(v_stack_m438, a2, v_stack_m430, v_rsi);
    goto loc_00AF6865;
loc_00AF60B2:
    if ((((unsigned __int8)((unsigned __int16)(v_rbx))) & (7)) != 0) goto loc_00AF67B7;
    if (((unsigned int)((unsigned __int16)(v_rbx))) > 256) goto loc_00AF67B7;
    result = memcpy(v_stack_m348, result, (unsigned __int16)(v_rbx), v_rsi);
    result = ExCpuSetResourceManagerAccessCheck(0, result, (unsigned __int16)(v_rbx), v_rsi);
    if (sign_flag) goto loc_00AF6869;
    v_r15 = (unsigned int)(((unsigned __int16)(v_rbx)) >> (3));
    a4 = 0;
loc_00AF60FC:
    result = KeModifySystemAllowedCpuSets((unsigned int)((unsigned int)(v_r15)), v_stack_m348, (unsigned __int16)(v_rbx), a4);
    goto loc_00AF6865;
loc_00AF610E:
    if (0 != 0) goto loc_00AF6695;
    if (((unsigned int)(v_r15)) != 8) goto loc_00AF67B7;
    result = kdcom_dll_KdInitialize(v_r15 - 5, result, v_rip + 4527288, a4);
    goto loc_00AF6865;
loc_00AF6140:
    if (((unsigned int)(v_r15)) < 8) goto loc_00AF67B7;
    v_r15 = (unsigned int)((v_r15) + (-8));
    if ((((unsigned __int8)(v_r15)) & (7)) != 0) goto loc_00AF67B7;
    if (((unsigned int)(v_r15)) > 256) goto loc_00AF67B7;
    v_stack_m3D8 = *(unsigned __int64 *)(result);
    result = memcpy(v_stack_m248, result + 8, (unsigned int)((unsigned int)(v_r15)), a4);
    result = ExCpuSetResourceManagerAccessCheck(0, result + 8, (unsigned int)((unsigned int)(v_r15)), a4);
    if (sign_flag) goto loc_00AF6867;
    v_r15 = (unsigned int)((v_r15) >> (3));
    result = KeSetTagCpuSets((unsigned int)((unsigned int)(v_r15)), v_stack_m248, *(unsigned __int64 *)(result), a4);
    goto loc_00AF6865;
loc_00AF61B8:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(result)))) - (177));
    if (condition_is_equal) goto loc_00AF627F;
    a1 = (unsigned int)((a1) - (10));
    if (condition_is_equal) goto loc_00AF6212;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00AF675C;
    if (a1 != 1) goto loc_00AF51B1;
    if ((unsigned int)(v_r15) == 0) goto loc_00AF61EC;
loc_00AF61E2:
    goto loc_00AF6867;
loc_00AF61EC:
    if (0 == 0) goto loc_00AF6208;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5126277), 0, *(unsigned __int64 *)(result), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
loc_00AF6208:
    result = VslRelaxQuotas(*(unsigned __int64 *)(v_rip + 5126277), 0, *(unsigned __int64 *)(result), a4);
    goto loc_00AF6865;
loc_00AF6212:
    if (((unsigned int)(v_r15)) != 24) goto loc_00AF67B7;
    v_stack_m3C8 = v_xmm0;
    v_stack_m3B8 = v_xmm1;
    result = VfProbeAndCaptureUnicodeStringBuffer(v_stack_m3C8, (unsigned int)((unsigned int)(v_r13)), *(unsigned __int64 *)(result), a4);
    if (sign_flag) goto loc_00AF6869;
    result = PsSetExeModerationState(v_stack_m3C8, (unsigned int)(v_stack_m3B8), (unsigned int)(v_stack_m3B4), a4);
    goto loc_00AF665B;
loc_00AF627F:
    result = 0;
    v_stack_m428 = v_xmm0;
    v_stack_m418 = 0;
    if (((unsigned int)(v_r15)) != 8) goto loc_00AF6343;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5126096), 0, (unsigned int)(v_stack_m3B4), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    v_stack_m400 = *(unsigned __int64 *)(result);
    v_stack_m4C8 = v_rsi;
    v_stack_m540 = v_rsi;
    v_stack_m548 = v_stack_m4C8;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(result), (unsigned int)(0x1000ULL), *(unsigned __int64 *)(v_rip + 5048273), 0);
    if (sign_flag) goto loc_00AF6867;
    result = PsGetProcessSessionIdEx(v_stack_m4C8, (unsigned int)(0x1000ULL), *(unsigned __int64 *)(v_rip + 5048273), 0);
    v_stack_m4F4 = (unsigned int)(result);
    if (((unsigned int)(result)) == -1) goto loc_00AF5843;
    v_stack_m418 = v_stack_m4C8;
    result = PsInvokeWin32Callout(32, v_stack_m428, (unsigned int)((unsigned int)(v_r13)), v_stack_m4F4);
    goto loc_00AF5843;
loc_00AF6343:
    if ((unsigned int)(v_r15) != 0) goto loc_00AF67B7;
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_stack_m428, (unsigned int)((unsigned int)(v_r13)), v_stack_m4F4);
    v_stack_m4F4 = (unsigned int)(result);
    if (((unsigned int)(result)) == -1) goto loc_00AF6867;
    v_stack_m418 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    result = PsInvokeWin32Callout(v_r15 + 32, v_stack_m428, (unsigned int)((unsigned int)(v_r13)), v_stack_m4F4);
    goto loc_00AF6865;
loc_00AF6399:
    if ((unsigned int)(v_r15) != 0) goto loc_00AF61E2;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5125836), 0, (unsigned int)((unsigned int)(v_r13)), v_stack_m4F4);
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    result = VslProvisionDumpEncryption(*(unsigned __int64 *)(v_rip + 5125836), 0, (unsigned int)((unsigned int)(v_r13)), v_stack_m4F4);
    if (sign_flag) goto loc_00AF6867;
    result = IoProvisionCrashDumpKey(*(unsigned __int64 *)(v_rip + 5125836), 0, (unsigned int)((unsigned int)(v_r13)), v_stack_m4F4);
    goto loc_00AF6865;
loc_00AF63D2:
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) > 223) goto loc_00AF66C2;
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) == 223) goto loc_00AF66AF;
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) > 212) goto loc_00AF65AE;
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) == 212) goto loc_00AF659B;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)))) - (199));
    if (condition_is_equal) goto loc_00AF675C;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_00AF6513;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00AF64A0;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF6438;
    if (a1 != 3) goto loc_00AF51B1;
    result = CmUpdateFeatureConfiguration(result, (unsigned int)((unsigned int)(v_r15)), 0, v_stack_m4F4);
    goto loc_00AF6865;
loc_00AF6438:
    if (((unsigned int)(v_r15)) != 4) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5125684), 0, 0, v_stack_m4F4);
    if ((unsigned __int8)(result) == 0) goto loc_00AF6695;
    v_stack_m4E4 = (unsigned int)(v_rsi);
    v_stack_m4E4 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if ((((unsigned int)((unsigned int)(0x2018ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(result))))) != 0) goto loc_00AF6566;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 5037891))) & ((unsigned int)((unsigned int)(0x2018ULL))));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) | ((unsigned int)(result)));
    v_stack_m4E4 = a1;
    *(unsigned int *)(v_rip + 5037874) = a1;
    *(unsigned int *)(result) = a1;
    goto loc_00AF6867;
loc_00AF64A0:
    if (((unsigned int)(v_r15)) != 8) goto loc_00AF67B7;
    if (0 == 0) goto loc_00AF64C6;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5125927), 0, 0, v_stack_m4F4);
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
loc_00AF64C6:
    result = PsIsCurrentThreadInServerSilo(*(unsigned __int64 *)(v_rip + 5125927), 0, 0, v_stack_m4F4);
    if ((unsigned __int8)(result) != 0) goto loc_00AF6695;
    v_stack_m3C8 = *(unsigned __int64 *)(result);
    a1 = (v_stack_m3C8 != ((unsigned __int8)(v_rsi))) ? 1 : 0;
    v_stack_m538 = (unsigned __int8)(a1);
    result = ExSetLeapSecondEnabled(a1, 0, 0, v_stack_m4F4);
    if (sign_flag) goto loc_00AF6869;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4229425)) = (unsigned __int8)(v_stack_m538);
    goto loc_00AF6867;
loc_00AF6513:
    v_stack_m450 = v_rsi;
    if (((unsigned int)(v_r15)) < 8) goto loc_00AF67B7;
    v_r15 = (unsigned int)((v_r15) + (-8));
    if ((((unsigned __int8)(v_r15)) & (7)) != 0) goto loc_00AF67B7;
    if (((unsigned int)(v_r15)) > 256) goto loc_00AF67B7;
    v_stack_m450 = *(unsigned __int64 *)(result);
    result = memcpy(v_stack_m148, result + 8, (unsigned int)((unsigned int)(v_r15)), v_stack_m4F4);
    if ((*(unsigned __int64 *)(result)) < 2) goto loc_00AF6570;
loc_00AF6566:
    goto loc_00AF6869;
loc_00AF6570:
    result = ExCpuSetResourceManagerAccessCheck(0, result + 8, (unsigned int)((unsigned int)(v_r15)), v_stack_m4F4);
    if (sign_flag) goto loc_00AF6867;
    v_r15 = (unsigned int)((v_r15) >> (3));
    goto loc_00AF60FC;
loc_00AF659B:
    result = CmUpdateFeatureUsageSubscription(result, (unsigned int)((unsigned int)(v_r15)), 0, (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    goto loc_00AF6865;
loc_00AF65AE:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(result)))) - (217));
    if (condition_is_equal) goto loc_00AF6682;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF6665;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF65D3;
    if (a1 != 1) goto loc_00AF51B1;
loc_00AF65D3:
    if (((unsigned int)(v_r15)) != 16) goto loc_00AF67B7;
    if (0 == 0) goto loc_00AF6627;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5125268), 0, 0, (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    result = VfProbeAndCaptureUnicodeString(v_stack_m508, result, (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    if (sign_flag) goto loc_00AF6869;
    if (v_stack_m508 != ((unsigned __int16)(v_rsi))) goto loc_00AF6627;
loc_00AF661D:
    goto loc_00AF6869;
loc_00AF6627:
    v_rbx = (unsigned int)((*(unsigned __int64 *)(result)) - (219));
    if (condition_is_equal) goto loc_00AF6645;
    if (((unsigned int)(v_rbx)) == 1) goto loc_00AF663B;
loc_00AF6634:
    goto loc_00AF664F;
loc_00AF663B:
    result = VfVolatileRemoveDifVerification(v_stack_m508, result, (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    goto loc_00AF664D;
loc_00AF6645:
    result = VfVolatileApplyDifVerification(v_stack_m508, result, (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
loc_00AF664D:
loc_00AF664F:
    if (0 == 0) goto loc_00AF6867;
loc_00AF665B:
    result = VfFreeCapturedUnicodeString(v_stack_m508, result, (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    goto loc_00AF6867;
loc_00AF6665:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5125137), 0, (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    if ((unsigned __int8)(result) == 0) goto loc_00AF6695;
    result = VfVolatileClearDifRuleClass(*(unsigned __int64 *)(v_rip + 5125137), 0, (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    goto loc_00AF6865;
loc_00AF6682:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5125108), 0, (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    if ((unsigned __int8)(result) != 0) goto loc_00AF669F;
loc_00AF6695:
    goto loc_00AF6869;
loc_00AF669F:
    result = VfVolatileSetDifRuleClass(v_stack_m508, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    goto loc_00AF6865;
loc_00AF66AF:
    result = ExPoolSetLimit(v_stack_m508, v_r15, 0, (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    goto loc_00AF6865;
loc_00AF66C2:
    if (((unsigned int)(v_rbx)) > 233) goto loc_00AF678E;
    if (((unsigned int)(v_rbx)) == 233) goto loc_00AF677E;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (224));
    if (condition_is_equal) goto loc_00AF675C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF675C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AF6735;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00AF66F7;
    if (a1 != 1) goto loc_00AF51B1;
loc_00AF66F7:
    v_stack_m537 = (unsigned __int8)(v_rsi);
    a1 = 0;
    result = RtlCheckTokenMembership(a1, *(unsigned __int64 *)(v_rip + 5124960), v_stack_m537, (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    if (sign_flag) goto loc_00AF67D4;
    if (v_stack_m537 == ((unsigned __int8)(v_rsi))) goto loc_00AF67D4;
    result = KeUpdateDpcWatchdogConfiguration(v_stack_m508, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    goto loc_00AF6865;
loc_00AF6735:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5124929), 0, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    if ((unsigned __int8)(result) == 0) goto loc_00AF67D4;
    a1 = ((unsigned int)(v_r15) == 0) ? 1 : 0;
    result = VfPtGenerateTraceInformation(a1, 0, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    goto loc_00AF6865;
loc_00AF675C:
    if (*(unsigned __int64 *)(v_rip + 4253565) == 0) goto loc_00AF530C;
    result = guard_dispatch_icall((unsigned int)((unsigned int)(v_rbx)), v_stack_m508, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    goto loc_00AF6865;
loc_00AF677E:
    result = PnpIommuBlockUnblockDevice(v_stack_m508, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    goto loc_00AF6865;
loc_00AF678E:
    v_rbx = (unsigned int)((v_rbx) - (235));
    if (condition_is_equal) goto loc_00AF684F;
    v_rbx = (unsigned int)((v_rbx) - (8));
    if (condition_is_equal) goto loc_00AF530C;
    v_rbx = (unsigned int)((v_rbx) - (2));
    if (condition_is_equal) goto loc_00AF67F5;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00AF51B1;
    if (((unsigned int)(v_r15)) == 4) goto loc_00AF67C1;
loc_00AF67B7:
    goto loc_00AF6869;
loc_00AF67C1:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5124789), 0, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    if ((unsigned __int8)(result) != 0) goto loc_00AF67DE;
loc_00AF67D4:
    goto loc_00AF6869;
loc_00AF67DE:
    v_stack_m3C8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m508)));
    *(unsigned int *)(v_rip + 5047790) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m508)));
    goto loc_00AF516B;
loc_00AF67F5:
    if (((unsigned int)(v_r15)) != 4) goto loc_00AF54A2;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5124727), 0, (unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(*(unsigned __int64 *)(result))));
    if ((unsigned __int8)(result) != 0) goto loc_00AF6819;
loc_00AF6812:
    goto loc_00AF6867;
loc_00AF6819:
    v_stack_m460 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m508)));
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_m508)) + 3999) - (0);
    a1 = (a1) >> (1);
    a1 = (a1) + (0);
    a1 = (a1) >> (11);
    *(unsigned int *)(v_rip + 4163491) = a1;
    goto loc_00AF6867;
loc_00AF684F:
    v_stack_m548 = v_rsi;
    a4 = 0;
    result = HvlQuerySetBootPagesInfo(v_stack_m508, (unsigned int)((unsigned int)(v_r15)), 0, a4);
loc_00AF6865:
loc_00AF6867:
loc_00AF6869:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)((unsigned int)(v_r15)), 0, a4);
    v_rsp = (v_rsp) + (0x530ULL);
    return result;
loc_00AF688D:
    result = ExRaiseDatatypeMisalignment(a1, (unsigned int)((unsigned int)(v_r15)), 0, a4);
loc_00AF6893:
    result = ExRaiseDatatypeMisalignment(a1, (unsigned int)((unsigned int)(v_r15)), 0, a4);
loc_00AF6899:
    result = ExRaiseDatatypeMisalignment(a1, (unsigned int)((unsigned int)(v_r15)), 0, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtSetSystemInformation(int32_t Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m148;
    uint64_t v_stack_m248;
    uint64_t v_stack_m348;
    uint64_t v_stack_m3A8;
    uint64_t v_stack_m3B0;
    uint32_t v_stack_m3B4;
    uint16_t v_stack_m3B6;
    uint32_t v_stack_m3B8;
    uint16_t v_stack_m3BE;
    uint32_t v_stack_m3C0;
    uint64_t v_stack_m3C8;
    uint64_t v_stack_m3D8;
    uint64_t v_stack_m3E0;
    uint64_t v_stack_m3E8;
    uint64_t v_stack_m3F0;
    uint64_t v_stack_m3F8;
    uint64_t v_stack_m400;
    uint64_t v_stack_m410;
    uint64_t v_stack_m418;
    uint64_t v_stack_m428;
    uint64_t v_stack_m430;
    uint64_t v_stack_m438;
    uint32_t v_stack_m440;
    uint32_t v_stack_m444;
    uint32_t v_stack_m448;
    uint64_t v_stack_m450;
    uint64_t v_stack_m458;
    uint32_t v_stack_m460;
    uint32_t v_stack_m464;
    uint32_t v_stack_m468;
    uint64_t v_stack_m470;
    uint64_t v_stack_m478;
    uint64_t v_stack_m48;
    uint64_t v_stack_m480;
    uint64_t v_stack_m488;
    uint64_t v_stack_m490;
    uint64_t v_stack_m498;
    uint64_t v_stack_m4A0;
    uint64_t v_stack_m4A8;
    uint64_t v_stack_m4B0;
    uint32_t v_stack_m4B8;
    uint64_t v_stack_m4C0;
    uint64_t v_stack_m4C8;
    uint32_t v_stack_m4D0;
    uint64_t v_stack_m4D8;
    uint32_t v_stack_m4E0;
    uint32_t v_stack_m4E4;
    uint8_t v_stack_m4E8;
    uint32_t v_stack_m4F0;
    uint32_t v_stack_m4F4;
    uint8_t v_stack_m4F8;
    uint64_t v_stack_m500;
    uint16_t v_stack_m506;
    uint64_t v_stack_m508;
    uint8_t v_stack_m514;
    uint8_t v_stack_m52F;
    uint8_t v_stack_m530;
    uint8_t v_stack_m537;
    uint8_t v_stack_m538;
    uint64_t v_stack_m540;
    uint64_t v_stack_m548;

    local_rsp = (local_rsp) - (0x530ULL);
    result = (*(uint64_t *)(v_rip + 0x315CC4)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m410 = v_xmm0;
    local_rsi = 0;
    v_stack_m538 = 0;
    v_stack_m508 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x4B0) = 0;
    v_stack_m514 = 0;
    v_stack_m4F0 = (uint32_t)(local_rsi + 1);
    *(uint64_t *)(local_rsp - 0x490) = 0;
    *(uint64_t *)(local_rsp - 0x498) = 0;
    *(uint64_t *)(local_rsp - 0x4A8) = 0;
    *(uint64_t *)(local_rsp - 0x4A0) = 0;
    *(uint64_t *)(local_rsp - 0x4D8) = 0;
    Arg2 = 0;
    result = memset(local_rsp - 968, Arg2, local_rsi + 1 + 127, a4);
    v_stack_m530 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF4B70;
    if (((uint32_t)((uint32_t)(Arg1))) != 89) goto loc_00AF4B14;
    goto loc_00AF4B41;
loc_00AF4B14:
    if (((uint32_t)((uint32_t)(Arg1))) == 204) goto loc_00AF4B3C;
    if (((uint32_t)((uint32_t)(Arg1))) == 210) goto loc_00AF4B3C;
    if (((uint32_t)((uint32_t)(Arg1))) == 212) goto loc_00AF4B3C;
    if (((uint32_t)((uint32_t)(Arg1))) != 151) goto loc_00AF4B3C;
    result = 0;
    if (((uint32_t)((uint32_t)(Arg3))) != ((uint32_t)(local_rsi + 1))) {
        result = 3;
    }
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_00AF4B69;
    if (((result) & (0)) != 0) goto loc_00AF688D;
    if ((Arg2 + (uint32_t)(Arg3) * 1) > result) goto loc_00AF4B67;
    if ((Arg2 + (uint32_t)(Arg3) * 1) < 0) {
        result = *(uint8_t *)(result);
    }
    goto loc_00AF4B70;
loc_00AF4B70:
    if (((uint32_t)((uint32_t)(Arg1))) > 113) goto loc_00AF5AD0;
    if (((uint32_t)((uint32_t)(Arg1))) == 113) goto loc_00AF5ABD;
    if (((uint32_t)((uint32_t)(Arg1))) > 71) goto loc_00AF5457;
    if (((uint32_t)((uint32_t)(Arg1))) == 71) goto loc_00AF59BB;
    if (((uint32_t)((uint32_t)(Arg1))) > 39) goto loc_00AF5177;
    if (((uint32_t)((uint32_t)(Arg1))) == 39) goto loc_00AF5138;
    if (((uint32_t)((uint32_t)(Arg1))) > 28) goto loc_00AF4DF1;
    if (((uint32_t)((uint32_t)(Arg1))) == 28) goto loc_00AF4D22;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (9));
    if (condition_is_equal) goto loc_00AF4CC9;
    Arg1 = (uint32_t)((Arg1) - (12));
    if (condition_is_equal) goto loc_00AF55BF;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00AF4C06;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00AF5369;
    if (Arg1 != 1) goto loc_00AF51B1;
    if (((uint32_t)((uint32_t)(Arg3))) != 8) goto loc_00AF67B7;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_00AF67D4;
    v_stack_m3F8 = *(uint64_t *)(arg2);
    result = MmUnloadSystemImage(*(uint64_t *)(arg2), Arg2, local_rsi + 1 + 127, a4);
    goto loc_00AF516B;
loc_00AF4C06:
    if (((uint32_t)((uint32_t)(Arg3))) != 20) goto loc_00AF67B7;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF4C2C;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E4F01), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), local_rsi + 1 + 127, a4);
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
loc_00AF4C2C:
    v_stack_m3C8 = v_xmm0;
    v_stack_m3B8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)));
    result = (v_stack_m3C8) >> (32);
    *(uint32_t *)(v_rip + 0x4D046B) = (uint32_t)(result);
    *(uint32_t *)(v_rip + 0x4D0486) = (uint32_t)((uint32_t)(v_stack_m3C0));
    result = (v_stack_m3C0) >> (32);
    *(uint32_t *)(v_rip + 0x4D0450) = (uint32_t)(result);
    *(uint32_t *)(v_rip + 0x4D0526) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)));
    result = KeSynchronizeWithDynamicProcessors((uint32_t)(*(uint32_t *)(arg2 + 0x10)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), local_rsi + 1 + 127, a4);
    result = KeQueryActiveProcessorCountEx((uint32_t)(0xFFFFULL), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), local_rsi + 1 + 127, a4);
    if ((uint32_t)(result) == 0) goto loc_00AF6867;
loc_00AF4C9B:
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x4D3FA8) + 0x38A8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4D041C)));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x4D3FA8) + 0x38B0) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4D0438)));
    Arg3 = ((uint32_t)((uint32_t)(result))) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_00AF4C9B;
    goto loc_00AF6867;
loc_00AF4CC9:
    if (((uint32_t)((uint32_t)(Arg3))) != 4) goto loc_00AF54A2;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E4DA3), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, a4);
    if ((uint8_t)(result) != 0) goto loc_00AF4CF0;
loc_00AF4CE6:
    goto loc_00AF6867;
loc_00AF4CF0:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x4CF5CA))) & (0x6DCE640FULL));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (0x92319BF0ULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    v_stack_m448 = Arg1;
    *(uint32_t *)(v_rip + 0x4CF5AD) = Arg1;
    *(uint32_t *)(arg2) = Arg1;
    goto loc_00AF6867;
loc_00AF4D22:
    if ((((uint32_t)((uint32_t)(Arg3) - 8)) & (0xFFFFFFF7ULL)) != 0) goto loc_00AF67B7;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF4D4D;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E4EA0), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
loc_00AF4D4D:
    result = PsIsCurrentThreadInServerSilo(*(uint64_t *)(v_rip + 0x4E4EA0), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, a4);
    if ((uint8_t)(result) != 0) goto loc_00AF6695;
    if (((uint32_t)((uint32_t)(Arg3))) != 16) goto loc_00AF4DB1;
    v_stack_m538 = (uint8_t)(*(uint8_t *)(arg2 + 0x8));
    v_stack_m4D8 = *(uint64_t *)(arg2);
loc_00AF4D73:
loc_00AF4D7D:
    result = *(uint64_t *)(arg2);
    if ((uint8_t)(*(uint8_t *)(arg2 + 0x8)) != 0) {
        result = *(uint64_t *)(Arg3);
        v_stack_m4D8 = result;
    }
    result = ExAcquireTimeRefreshLockExclusive(*(uint8_t *)(arg2 + 0x8), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, a4);
    Arg1 = 0;
    result = ExpUpdateTimerConfiguration(Arg1, v_stack_m4D8, v_stack_m538, a4);
    result = ExReleaseTimeRefreshLockExclusive(Arg1, v_stack_m4D8, v_stack_m538, a4);
    goto loc_00AF6867;
loc_00AF4DB1:
    v_stack_m538 = (uint8_t)(*(uint8_t *)(arg2 + 0x4));
    v_stack_m4D8 = (uint32_t)(*(uint32_t *)(arg2));
    if ((uint32_t)(*(uint32_t *)(arg2)) == 0) goto loc_00AF4D73;
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0x4D1CD1))) * (*(uint64_t *)(v_stack_m538));
    Arg2 = 0;
    v_stack_m4D8 = result;
    goto loc_00AF4D7D;
loc_00AF4DF1:
    local_rbx = (uint32_t)(((uint32_t)(Arg1)) - (30));
    if (condition_is_equal) goto loc_00AF512E;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00AF511B;
    local_rbx = (uint32_t)((local_rbx) - (3));
    if (condition_is_equal) goto loc_00AF507E;
    local_rbx = (uint32_t)((local_rbx) - (3));
    if (condition_is_equal) goto loc_00AF504B;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00AF51B1;
    if ((((uint32_t)((uint32_t)(Arg3) - 16)) & (0xFFFFFFF7ULL)) != 0) goto loc_00AF67B7;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF4F89;
    v_stack_m4E0 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x7DC)))) & (8)) == 0) goto loc_00AF67D4;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E4CBB), (uint8_t)(local_rsi + 1), v_stack_m538, (uint32_t)(*(uint32_t *)(arg2)));
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    if (((uint32_t)((uint32_t)(Arg3))) != 16) goto loc_00AF4EC0;
    v_stack_m4C8 = v_xmm0;
    result = RtlReadULongFromUser(0, (uint8_t)(local_rsi + 1), v_stack_m538, (uint32_t)(*(uint32_t *)(arg2)));
    v_stack_m4C8 = (uint32_t)(result);
    result = RtlReadULong64FromUser(Arg2 + 8, (uint8_t)(local_rsi + 1), v_stack_m538, (uint32_t)(*(uint32_t *)(arg2)));
    v_stack_m4C0 = result;
    v_stack_m508 = v_xmm0;
    goto loc_00AF4EF4;
loc_00AF4EC0:
    result = RtlCopyFromUser(v_stack_m3C8, (uint32_t)(v_stack_m4E0), 24, (uint32_t)(*(uint32_t *)(arg2)));
    v_stack_m508 = v_xmm0;
    v_stack_m4E0 = (uint32_t)((uint32_t)(v_stack_m3C8));
loc_00AF4EF4:
    if (v_stack_m508 != 62) goto loc_00AF67D4;
    result = RtlCopyFromUser(v_stack_m3C8, v_stack_m500, 62, (uint32_t)(*(uint32_t *)(arg2)));
    result = memcmp(v_stack_m3C8, v_rip - 11256900, 62, (uint32_t)(*(uint32_t *)(arg2)));
    if ((uint32_t)(result) != 0) goto loc_00AF67D4;
    v_stack_m500 = v_rip - 11256900;
    v_stack_m506 = 62;
    v_stack_m3B8 = v_rip - 11256900;
    v_stack_m3BE = 62;
    local_r14 = (uint32_t)(v_stack_m3C8);
    if (((uint32_t)((uint32_t)(Arg3))) == 16) { local_r14 = 0; }
    v_stack_m3C8 = (uint32_t)(local_r14);
    result = ZwSetSystemInformation(result + 38, v_stack_m3C8, result + 24, (uint32_t)(*(uint32_t *)(arg2)));
    goto loc_00AF6869;
loc_00AF4F89:
    if (((uint32_t)((uint32_t)(Arg3))) != 16) goto loc_00AF4F9A;
    goto loc_00AF4FAF;
loc_00AF4F9A:
    local_r14 = (uint8_t)((uint32_t)(v_stack_m514));
    if (((*(uint8_t *)((uint32_t)(v_stack_m514))) & ((uint8_t)(local_rsi + 1))) != 0) { local_r14 = (uint32_t)(local_rsi + 1); }
loc_00AF4FAF:
    v_stack_m508 = v_xmm0;
    result = memcmp(v_stack_m500, v_rip - 11257058, 62, (uint32_t)(*(uint32_t *)(arg2)));
    if ((uint32_t)(result) != 0) goto loc_00AF59BB;
    result = RtlImageNtHeader(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4117F5) + 0x30), v_rip - 11257058, 62, (uint32_t)(*(uint32_t *)(arg2)));
    if (result != 0) goto loc_00AF5002;
    result = MmUnloadSystemImage(*(uint64_t *)(v_rip + 0x4117DD), v_rip - 11257058, 62, (uint32_t)(*(uint32_t *)(arg2)));
    goto loc_00AF6869;
loc_00AF5002:
    Arg1 = ((uint32_t)(*(uint32_t *)((uint32_t)(0xC000007BULL) + 0x28))) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0x4117F5) + 0x30));
    result = ExpInitializeSessionDriver(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0x4117F5) + 0x30), (uint8_t)(local_r14), (uint32_t)(*(uint32_t *)(arg2)));
    if (!sign_flag) goto loc_00AF6867;
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), *(uint64_t *)(*(uint64_t *)(v_rip + 0x4117F5) + 0x30), (uint8_t)(local_r14), (uint32_t)(*(uint32_t *)(arg2)));
    if ((uint32_t)(result) != 0) goto loc_00AF6867;
    result = MmUnloadSystemImage(*(uint64_t *)(v_rip + 0x41178F), *(uint64_t *)(*(uint64_t *)(v_rip + 0x4117F5) + 0x30), (uint8_t)(local_r14), (uint32_t)(*(uint32_t *)(arg2)));
    goto loc_00AF6867;
loc_00AF504B:
    if (((uint32_t)((uint32_t)(Arg3))) != 16) goto loc_00AF67B7;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF5071;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E4B0C), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(local_r14), (uint32_t)(*(uint32_t *)(arg2)));
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
loc_00AF5071:
    result = CmSetRegistryQuotaInformation(local_r14, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(local_r14), (uint32_t)(*(uint32_t *)(arg2)));
    goto loc_00AF6865;
loc_00AF507E:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF509A;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E49F3), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(local_r14), (uint32_t)(*(uint32_t *)(arg2)));
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
loc_00AF509A:
    result = PsIsCurrentThreadInServerSilo(*(uint64_t *)(v_rip + 0x4E49F3), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(local_r14), (uint32_t)(*(uint32_t *)(arg2)));
    if ((uint8_t)(result) != 0) goto loc_00AF67D4;
    if (((uint32_t)((uint32_t)(Arg3))) == 4) goto loc_00AF50BC;
loc_00AF50AD:
    Arg2 = 0;
loc_00AF50B2:
    result = IoConfigureCrashDump((uint32_t)((uint32_t)(local_rsi + 1)), Arg2, (uint8_t)(local_r14), (uint32_t)(*(uint32_t *)(arg2)));
    goto loc_00AF6865;
loc_00AF50BC:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF50F6;
    if ((((uint8_t)(local_r14)) & (3)) != 0) goto loc_00AF6893;
    if ((local_r14 + 4) > result) goto loc_00AF50E3;
    if ((local_r14 + 4) < local_r14) {
        result = *(uint8_t *)(result);
    }
    v_stack_m444 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14)));
    goto loc_00AF50F9;
loc_00AF50F6:
loc_00AF50F9:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14))) == 0) goto loc_00AF5115;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14))) - (1));
    if (condition_is_equal) goto loc_00AF50AD;
    if (Arg1 != 1) goto loc_00AF6566;
    result = WheaCrashDumpInitializationComplete(Arg1, Arg2, (uint8_t)(local_r14), (uint32_t)(*(uint32_t *)(arg2)));
    goto loc_00AF6865;
loc_00AF5115:
    Arg2 = 0;
    Arg1 = 0;
    goto loc_00AF50B2;
loc_00AF511B:
    result = EtwSetPerformanceTraceInformation(local_r14, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(*(uint32_t *)(arg2)));
    goto loc_00AF6865;
loc_00AF512E:
    result = MmCreateMirror(local_r14, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(*(uint32_t *)(arg2)));
    goto loc_00AF6865;
loc_00AF5138:
    if (((uint32_t)((uint32_t)(Arg3))) != 4) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E492C), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(*(uint32_t *)(arg2)));
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    v_stack_m440 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14)));
    result = PsChangeQuantumTable((uint8_t)(local_rsi + 1), (uint32_t)(*(uint32_t *)(local_r14)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(*(uint32_t *)(arg2)));
loc_00AF516B:
    goto loc_00AF6867;
loc_00AF5177:
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4117F5) + 0x30))) > 51) goto loc_00AF52F4;
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4117F5) + 0x30))) == 51) goto loc_00AF52CA;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x4117F5) + 0x30)))) - (40));
    if (condition_is_equal) goto loc_00AF5254;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF5254;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_00AF51BB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF5514;
    if (Arg1 == 1) goto loc_00AF5514;
loc_00AF51B1:
    goto loc_00AF6867;
loc_00AF51BB:
    if (((uint32_t)((uint32_t)(Arg3))) != 8) goto loc_00AF67B7;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF51E1;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E4A0C), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(*(uint32_t *)(arg2)));
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
loc_00AF51E1:
    result = PsIsCurrentThreadInServerSilo(*(uint64_t *)(v_rip + 0x4E4A0C), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(*(uint32_t *)(arg2)));
    if ((uint8_t)(result) != 0) goto loc_00AF6695;
    v_stack_m458 = *(uint64_t *)(local_r14);
    if (*(uint64_t *)(local_r14) != 0) goto loc_00AF5205;
    goto loc_00AF5245;
loc_00AF5205:
    v_stack_m4C8 = 0;
    v_stack_m540 = 0;
    v_stack_m548 = v_stack_m4C8;
    result = ObReferenceObjectByHandle(0, 2, *(uint64_t *)(v_rip + 0x4D1974), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_00AF6867;
loc_00AF5245:
    result = KdUpdateTimeSlipEvent(v_stack_m4C8, 2, *(uint64_t *)(v_rip + 0x4D1974), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_00AF6867;
loc_00AF5254:
    if (((uint32_t)((uint32_t)(Arg3))) != 16) goto loc_00AF67B7;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF52A2;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E4813), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_rip + 0x4D1974), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    result = VfProbeAndCaptureUnicodeString(v_stack_m508, local_r14, (uint32_t)((uint32_t)(local_rsi + 1)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_00AF6869;
    if (v_stack_m508 == 0) goto loc_00AF661D;
loc_00AF52A2:
    local_rbx = (uint32_t)((*(uint64_t *)(*(uint64_t *)(v_rip + 0x4117F5) + 0x30)) - (40));
    if (condition_is_equal) goto loc_00AF52BD;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00AF6634;
    result = VfRemoveVerifierEntry(v_stack_m508, local_r14, (uint32_t)((uint32_t)(local_rsi + 1)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_00AF664D;
loc_00AF52BD:
    result = VfAddVerifierEntry(v_stack_m508, local_r14, (uint32_t)((uint32_t)(local_rsi + 1)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_00AF664D;
loc_00AF52CA:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E47AC), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)((uint32_t)(local_rsi + 1)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if ((uint8_t)(result) == 0) goto loc_00AF6695;
    Arg3 = 0;
    result = VfSetVerifierInformation(v_stack_m508, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_00AF6865;
loc_00AF52F4:
    if (((uint32_t)(local_rbx)) == 54) goto loc_00AF5365;
    if (((uint32_t)(local_rbx)) == 56) goto loc_00AF5352;
    if (((uint32_t)(local_rbx)) == 59) goto loc_00AF5316;
    if (((uint32_t)(local_rbx)) != 69) goto loc_00AF51B1;
loc_00AF530C:
    goto loc_00AF6867;
loc_00AF5316:
    if (((uint32_t)((uint32_t)(Arg3))) != 4) goto loc_00AF67B7;
    v_stack_m468 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m508)));
    result = ExpUpdateComPlusPackage((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m508)))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_00AF6867;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x4CFCC6) + 0x2E0) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m508)));
    goto loc_00AF6867;
loc_00AF5352:
    result = PfSnSetPrefetcherInformation((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m508)))), v_stack_m508, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_00AF6865;
loc_00AF5365:
    goto loc_00AF536D;
loc_00AF5369:
loc_00AF536D:
    if (((uint32_t)((uint32_t)(Arg3))) != 48) goto loc_00AF5378;
    goto loc_00AF5385;
loc_00AF5378:
    if (0 != 56) goto loc_00AF67B7;
loc_00AF5385:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_00AF67D4;
    v_stack_m508 = v_xmm0;
    v_stack_m540 = v_stack_m4B0;
    v_stack_m548 = v_stack_m4A8;
    Arg3 = 0;
    Arg2 = 0;
    result = MmLoadSystemImage(v_stack_m508, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4F0))));
    if (sign_flag) goto loc_00AF543D;
    if ((uint8_t)((uint8_t)(local_rsi + 1)) == 0) goto loc_00AF53F2;
    Arg3 = 0;
    result = RtlImageDirectoryEntryToData(v_stack_m4B0, (uint8_t)(local_rsi + 1), Arg3, v_stack_m4C8);
    goto loc_00AF53F5;
loc_00AF53F2:
loc_00AF53F5:
    result = RtlImageNtHeader(v_stack_m4B0, (uint8_t)(local_rsi + 1), Arg3, v_stack_m4C8);
    Arg2 = ((uint32_t)(*(uint32_t *)(result + 0x28))) + (v_stack_m4B0);
    *(uint64_t *)(v_stack_m508 + 0x10) = v_stack_m4B0;
    *(uint64_t *)(v_stack_m508 + 0x18) = v_stack_m4A8;
    *(void **)(v_stack_m508 + 0x20) = Arg2;
    if ((uint8_t)((uint8_t)(local_rsi + 1)) == 0) goto loc_00AF542A;
    *(uint64_t *)(v_stack_m508 + 0x28) = 0;
    *(uint32_t *)(v_stack_m508 + 0x30) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x50)));
    goto loc_00AF5431;
loc_00AF542A:
    *(uint32_t *)(v_stack_m508 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x50)) + 0x50)));
loc_00AF5431:
    goto loc_00AF6867;
loc_00AF543D:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(result + 0x50)) + 0x50)))) != 0xC000019DULL) goto loc_00AF6867;
    goto loc_00AF6867;
loc_00AF5457:
    if (((uint32_t)(v_stack_m4B0)) > 92) goto loc_00AF587E;
    if (((uint32_t)(v_stack_m4B0)) == 92) goto loc_00AF5850;
    if (((uint32_t)(v_stack_m4B0)) > 81) goto loc_00AF5664;
    if (((uint32_t)(v_stack_m4B0)) == 81) goto loc_00AF55BF;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m4B0))) - (72));
    if (condition_is_equal) goto loc_00AF551E;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00AF5514;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF5501;
    Arg1 = (uint32_t)((Arg1) - (4));
    if (condition_is_equal) goto loc_00AF54EC;
    if (Arg1 != 1) goto loc_00AF51B1;
    if (((uint32_t)((uint8_t)(local_rsi + 1))) >= 4) goto loc_00AF54AC;
loc_00AF54A2:
    goto loc_00AF6867;
loc_00AF54AC:
    v_stack_m4D0 = 6;
    v_stack_m4D0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m508)));
    goto loc_00AF54D3;
loc_00AF54D3:
    if (sign_flag) goto loc_00AF6867;
    Arg3 = (Arg3) | (-1);
    result = MmIssueMemoryListCommand((uint32_t)(*(uint32_t *)(v_stack_m508)), 0, Arg3, v_stack_m4C8);
    goto loc_00AF6865;
loc_00AF54EC:
    result = PfSetSuperfetchInformation((uint32_t)((uint32_t)(v_stack_m4B0)), v_stack_m508, (uint32_t)((uint32_t)((uint8_t)(local_rsi + 1))), 0);
    goto loc_00AF6865;
loc_00AF5501:
    result = ExpRegisterFirmwareTableInformationHandler(v_stack_m508, (uint32_t)((uint32_t)((uint8_t)(local_rsi + 1))), 0, 0);
    goto loc_00AF6865;
loc_00AF5514:
    goto loc_00AF6869;
loc_00AF551E:
    if (0 != 0) goto loc_00AF6566;
    if (v_stack_m508 == 0) goto loc_00AF6566;
    if (((uint32_t)((uint8_t)(local_rsi + 1))) != 8) goto loc_00AF6566;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m508))) == 0) goto loc_00AF530C;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m508))) - (1));
    if (condition_is_equal) goto loc_00AF55AE;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF55A5;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF559C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF530C;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00AF5588;
    if (Arg1 != 1) goto loc_00AF61E2;
    local_rdi = 0;
    if ((*(uint64_t *)(v_rip + 0x30B5B8)) == (v_rip - 6262649)) { local_rdi = (uint32_t)((uint32_t)(0xC0000002ULL)); }
    goto loc_00AF6867;
loc_00AF5588:
    result = guard_dispatch_icall((uint8_t)(local_rsi + 1), v_rip - 6262649, 0, 0);
    goto loc_00AF6865;
loc_00AF559C:
    goto loc_00AF55B5;
loc_00AF55A5:
    goto loc_00AF55B5;
loc_00AF55AE:
loc_00AF55B5:
    result = guard_dispatch_icall((uint8_t)(local_rsi + 1), v_rip - 6262649, 0, 0);
    goto loc_00AF516B;
loc_00AF55BF:
    v_stack_m52F = 0;
    if (((uint32_t)((uint8_t)(local_rsi + 1))) < 64) goto loc_00AF67B7;
    if (((uint32_t)(v_stack_m4B0)) != 21) goto loc_00AF55DE;
    v_stack_m4B8 = 0;
    goto loc_00AF5603;
loc_00AF55DE:
    v_stack_m4B8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m508 + 0x3C)));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m508 + 0x3C)))) & (0xFFFFFFF0ULL)) != 0) goto loc_00AF5655;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m508 + 0x3C))))) & (12));
    if (((uint8_t)(result)) == 12) goto loc_00AF5655;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m508 + 0x3C))))) & (3));
    if (((uint8_t)(result)) == 3) goto loc_00AF5655;
loc_00AF5603:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E4563), 0, 0, 0);
    if ((uint8_t)(result) == 0) goto loc_00AF6695;
    v_stack_m3F0 = *(uint64_t *)(v_stack_m508 + 0x18);
    v_stack_m3E8 = *(uint64_t *)(v_stack_m508 + 0x20);
    v_stack_m540 = v_stack_m52F;
    v_stack_m548 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m508 + 0x3C)));
    result = MmAdjustWorkingSetSizeEx(*(uint64_t *)(v_stack_m508 + 0x18), *(uint64_t *)(v_stack_m508 + 0x20), (uint32_t)((uint32_t)(local_rsi + 1)), (uint8_t)(local_rsi + 1));
    goto loc_00AF6869;
loc_00AF5655:
    goto loc_00AF6869;
loc_00AF5664:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m508 + 0x3C))) - (82));
    if (condition_is_equal) goto loc_00AF578F;
    local_rbx = (uint32_t)((local_rbx) - (4));
    if (condition_is_equal) goto loc_00AF577F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00AF572C;
    local_rbx = (uint32_t)((local_rbx) - (2));
    if (condition_is_equal) goto loc_00AF56BC;
    if (((uint32_t)(local_rbx)) != 2) goto loc_00AF51B1;
    if (0 != 0) goto loc_00AF4CE6;
    if ((uint32_t)((uint8_t)(local_rsi + 1)) == 0) goto loc_00AF56A5;
    goto loc_00AF6867;
loc_00AF56A5:
    result = (uint8_t)(-(*(uint8_t *)(v_rip + 0x4D13EC)));
    local_rdi = (uint32_t)(~((uint32_t)(0xC00000F0ULL)));
    local_rdi = (uint32_t)((local_rdi) & (0xC0351000ULL));
    goto loc_00AF6867;
loc_00AF56BC:
    if (0 != ((uint8_t)(local_rsi + 1))) goto loc_00AF530C;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E43A9), (uint8_t)(local_rsi + 1), (uint32_t)((uint32_t)(local_rsi + 1)), (uint8_t)(local_rsi + 1));
    if ((uint8_t)(result) == 0) goto loc_00AF6812;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) == 0) goto loc_00AF571C;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) == 332) goto loc_00AF5713;
    local_r13 = local_rsi + 1;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) != 452) {
        local_r13 = 0;
    }
    if ((uint8_t)(local_r13) != 0) goto loc_00AF530C;
loc_00AF571C:
    result = DbgkRegisterErrorPort(v_stack_m508, (uint32_t)((uint32_t)((uint8_t)(local_rsi + 1))), (uint32_t)((uint32_t)(local_rsi + 1)), (uint8_t)(local_rsi + 1));
    goto loc_00AF6865;
loc_00AF572C:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E434A), 0, (uint32_t)((uint32_t)(local_rsi + 1)), (uint8_t)(local_rsi + 1));
    if ((uint8_t)(result) == 0) goto loc_00AF4CE6;
    if (((uint32_t)((uint8_t)(local_rsi + 1))) != 8) goto loc_00AF54A2;
    v_stack_m3C8 = *(uint64_t *)(v_stack_m508);
    *(uint32_t *)(v_rip + 0x4D14C3) = (uint32_t)((uint32_t)(v_stack_m3C8));
    result = (*(uint64_t *)(v_stack_m508)) >> (32);
    Arg1 = (uint32_t)(((uint8_t)(result)) & ((uint32_t)(local_r13)));
    *(uint32_t *)(v_rip + 0x4CF9AF) = Arg1;
    goto loc_00AF6867;
loc_00AF577F:
    result = ObSetRefTraceInformation(v_stack_m508, (uint32_t)((uint32_t)((uint8_t)(local_rsi + 1))), (uint32_t)((uint32_t)(local_rsi + 1)), (uint8_t)(local_rsi + 1));
    goto loc_00AF6865;
loc_00AF578F:
    if (((uint32_t)((uint8_t)(local_rsi + 1))) < 24) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E4345), 0, (uint32_t)((uint32_t)(local_rsi + 1)), (uint8_t)(local_rsi + 1));
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    if (0 == 0) goto loc_00AF57DF;
    v_stack_m3C8 = v_xmm0;
    v_stack_m3B8 = v_xmm1;
    goto loc_00AF57DF;
loc_00AF57DF:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m3C8 + 0x10))) - ((uint32_t)(local_r13)));
    if (((uint32_t)(result)) > 30) goto loc_00AF6566;
    v_stack_m410 = v_xmm0;
    Arg2 = 0;
    result = PsLookupProcessThreadByCid(v_stack_m410, Arg2, v_stack_m4A0, (uint8_t)(local_rsi + 1));
    if (sign_flag) goto loc_00AF6867;
    if ((*(uint8_t *)(v_stack_m4A0 + 0x4)) == 0) goto loc_00AF5832;
    goto loc_00AF5843;
loc_00AF5832:
    result = KeSetActualBasePriorityThread(v_stack_m4A0, (uint32_t)(*(uint32_t *)(v_stack_m3C8 + 0x10)), v_stack_m4A0, (uint8_t)(local_rsi + 1));
loc_00AF5843:
    result = ObfDereferenceObject(v_stack_m4A0, (uint32_t)(*(uint32_t *)(v_stack_m3C8 + 0x10)), v_stack_m4A0, (uint8_t)(local_rsi + 1));
    goto loc_00AF6867;
loc_00AF5850:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E4226), 0, v_stack_m4A0, (uint8_t)(local_rsi + 1));
    if ((uint8_t)(result) == 0) goto loc_00AF6695;
    if (((uint32_t)((uint8_t)(local_rsi + 1))) != 40) goto loc_00AF67B7;
    result = VfSetVerifierInformationEx(v_stack_m3C8, 0, v_stack_m4A0, (uint8_t)(local_rsi + 1));
    goto loc_00AF6865;
loc_00AF587E:
    if (((uint32_t)(v_stack_m4A0)) > 104) goto loc_00AF5A49;
    if (((uint32_t)(v_stack_m4A0)) == 104) goto loc_00AF5A36;
    local_rbx = (uint32_t)((v_stack_m4A0) - (93));
    if (condition_is_equal) goto loc_00AF5A2C;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00AF59C5;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00AF59BB;
    local_rbx = (uint32_t)((local_rbx) - (2));
    if (condition_is_equal) goto loc_00AF58F3;
    if (((uint32_t)(local_rbx)) != 5) goto loc_00AF51B1;
loc_00AF58BF:
    if (((uint32_t)((uint8_t)(local_rsi + 1))) != 432) goto loc_00AF67B7;
    if (0 == 0) goto loc_00AF58E4;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E4499), 0, v_stack_m4A0, (uint8_t)(local_rsi + 1));
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
loc_00AF58E4:
    result = ExpSetTimeZoneInformation(v_stack_m3C8, 432, v_stack_m4A0, (uint8_t)(local_rsi + 1));
    goto loc_00AF6865;
loc_00AF58F3:
    if (((uint32_t)((uint8_t)(local_rsi + 1))) != 40) goto loc_00AF67B7;
    if (0 == 0) goto loc_00AF5996;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E4170), 0, v_stack_m4A0, (uint8_t)(local_rsi + 1));
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    v_stack_m3C8 = v_xmm0;
    v_stack_m3B8 = v_xmm1;
    v_stack_m3A8 = v_xmm0;
    result = VfProbeAndCaptureUnicodeStringBuffer(v_stack_m3C0, (uint32_t)((uint32_t)(local_r13)), v_stack_m4A0, (uint8_t)(local_rsi + 1));
    if (sign_flag) goto loc_00AF6869;
    result = VfProbeAndCaptureUnicodeStringBuffer(v_stack_m3B0, (uint32_t)((uint32_t)(local_r13)), v_stack_m4A0, (uint8_t)(local_rsi + 1));
    if (!sign_flag) goto loc_00AF5987;
    result = VfFreeCapturedUnicodeString(v_stack_m3C0, (uint32_t)((uint32_t)(local_r13)), v_stack_m4A0, (uint8_t)(local_rsi + 1));
    goto loc_00AF6869;
loc_00AF5987:
    goto loc_00AF5996;
loc_00AF5996:
    result = VfFaultsSetParameters(v_stack_m3C8, (uint32_t)((uint32_t)(local_r13)), v_stack_m4A0, (uint8_t)(local_rsi + 1));
    if (0 == 0) goto loc_00AF6867;
    result = VfFreeCapturedUnicodeString(v_stack_m3C8 + 8, (uint32_t)((uint32_t)(local_r13)), v_stack_m4A0, (uint8_t)(local_rsi + 1));
    goto loc_00AF665B;
loc_00AF59BB:
    goto loc_00AF6869;
loc_00AF59C5:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E40A9), 0, v_stack_m4A0, (uint8_t)(local_rsi + 1));
    if ((uint8_t)(result) == 0) goto loc_00AF4CE6;
    if (((uint32_t)((uint8_t)(local_rsi + 1))) != 8) goto loc_00AF54A2;
    v_stack_m3C8 = *(uint64_t *)(v_stack_m3C8);
    result = (v_stack_m3C8) >> (32);
    result = (uint32_t)(~(result));
    goto loc_00AF6867;
loc_00AF5A2C:
    goto loc_00AF58BF;
loc_00AF5A36:
    result = ExpSetProcessorMicrocodeUpdateInformation(v_stack_m3C8, (uint32_t)((uint32_t)((uint8_t)(local_rsi + 1))), 0, (uint8_t)(local_rsi + 1));
    goto loc_00AF6865;
loc_00AF5A49:
    local_rbx = (uint32_t)((172) - (106));
    if (condition_is_equal) goto loc_00AF51B1;
    local_rbx = (uint32_t)((local_rbx) - (3));
    if (condition_is_equal) goto loc_00AF5AAA;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00AF5AA0;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00AF51B1;
    if (((uint32_t)((uint8_t)(local_rsi + 1))) != 4) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E408F), 0, 0, (uint8_t)(local_rsi + 1));
    if ((uint8_t)(result) == 0) goto loc_00AF6695;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x4CF578) + 0x248) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m3C8)));
    goto loc_00AF516B;
loc_00AF5AA0:
    goto loc_00AF6867;
loc_00AF5AAA:
    result = SmSetStoreInformation((uint32_t)(*(uint32_t *)(v_stack_m3C8)), v_stack_m3C8, (uint32_t)((uint32_t)((uint8_t)(local_rsi + 1))), 0);
    goto loc_00AF6865;
loc_00AF5ABD:
    result = PsSetCpuQuotaInformation(v_stack_m3C8, (uint32_t)((uint32_t)((uint8_t)(local_rsi + 1))), 0, 0);
    goto loc_00AF6865;
loc_00AF5AD0:
    if (((uint32_t)(local_rbx)) > 194) goto loc_00AF63D2;
    if (((uint32_t)(local_rbx)) == 194) goto loc_00AF6399;
    if (((uint32_t)(local_rbx)) > 155) goto loc_00AF6012;
    if (((uint32_t)(local_rbx)) == 155) goto loc_00AF6008;
    if (((uint32_t)(local_rbx)) > 132) goto loc_00AF5D97;
    if (((uint32_t)(local_rbx)) == 132) goto loc_00AF5CAA;
    local_rbx = (uint32_t)((local_rbx) - (126));
    if (condition_is_equal) goto loc_00AF5C8A;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00AF5C2C;
    local_rbx = (uint32_t)((local_rbx) - (2));
    if (condition_is_equal) goto loc_00AF5C19;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00AF5B5A;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00AF51B1;
    if (0 != 0) goto loc_00AF6695;
    if (((uint32_t)((uint8_t)(local_rsi + 1))) != 24) goto loc_00AF67B7;
    result = KeInitializeEntropySystem(*(uint64_t *)(v_stack_m3C8), *(uint64_t *)(v_stack_m3C8 + 0x8), *(uint64_t *)(v_stack_m3C8 + 0x10), 0);
    goto loc_00AF6865;
loc_00AF5B5A:
    if ((((uint32_t)((uint8_t)(local_rsi + 1) - 16)) & (0xFFFFFFE7ULL)) != 0) goto loc_00AF67B7;
    if (((uint32_t)((uint8_t)(local_rsi + 1))) == 40) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E3F8B), 0, *(uint64_t *)(v_stack_m3C8 + 0x10), 0);
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    result = memcpy(v_stack_m3C8, v_stack_m3C8, (uint8_t)(local_rsi + 1), 0);
    if (((uint32_t)((uint8_t)(local_rsi + 1))) == 32) { local_rsi = v_stack_m3B0; }
    result = MiGetThreadPartition(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m3C8, (uint8_t)(local_rsi + 1), 0);
    v_stack_m540 = v_stack_m498;
    v_stack_m548 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = MiCombineIdenticalPages(result, v_stack_m3C8, (uint32_t)(v_stack_m3B8), local_rsi);
    v_stack_m514 = (uint32_t)(result);
    *(uint64_t *)(v_stack_m3C8 + 0x8) = v_stack_m498;
    goto loc_00AF6867;
loc_00AF5C19:
    result = KeProcessorProfileControlArea(v_stack_m3C8, (uint32_t)((uint32_t)((uint8_t)(local_rsi + 1))), 0, local_rsi);
    goto loc_00AF6865;
loc_00AF5C2C:
    if (((uint32_t)((uint8_t)(local_rsi + 1))) != 16) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E3EC8), 0, 0, local_rsi);
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    v_stack_m458 = *(uint64_t *)(v_stack_m3C8);
    result = MmScrubMemory(*(uint64_t *)(v_rip + 0x4E3EC8), *(uint64_t *)(v_stack_m3C8), v_stack_m490, local_rsi);
    v_stack_m514 = (uint32_t)(result);
    *(uint64_t *)(v_stack_m3C8 + 0x8) = v_stack_m490;
    goto loc_00AF6867;
loc_00AF5C8A:
    if (0 != 0) goto loc_00AF67D4;
    if (((uint32_t)((uint8_t)(local_rsi + 1))) != 32) goto loc_00AF54A2;
    result = BgkSetBootGraphicsInformation(*(uint64_t *)(v_rip + 0x4E3EC8), v_stack_m3C8, v_stack_m490, local_rsi);
    goto loc_00AF6865;
loc_00AF5CAA:
    if (((uint32_t)((uint8_t)(local_rsi + 1))) != 4) goto loc_00AF67B7;
    v_stack_m488 = 0x760074ULL;
    v_stack_m480 = v_rip + 75561;
    result = (uint8_t)((*(uint8_t *)(v_stack_m3C8)) & ((uint8_t)(local_r13)));
    v_stack_m4E8 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_00AF5D69;
    local_rbx = (local_rbx) | (-1);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 5121315, Arg2, Arg3, local_rsi);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 5121315;
        Arg2 = result;
        Arg1 = v_rip + 5121315;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, local_rsi);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_r13);
    }
    result = ZwLoadDriver(v_stack_m488, Arg2, Arg3, local_rsi);
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = v_rip + 5121315;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, local_rsi);
    }
    result = KeAbPostRelease(v_rip + 5121315, Arg2, Arg3, local_rsi);
    result = KeLeaveCriticalRegion(v_rip + 5121315, Arg2, Arg3, local_rsi);
    goto loc_00AF6867;
loc_00AF5D69:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E3DAD), 0, Arg3, local_rsi);
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    result = ZwUnloadDriver(v_stack_m488, 0, Arg3, local_rsi);
    goto loc_00AF6865;
loc_00AF5D97:
    local_rbx = (uint32_t)((local_rbx) - (134));
    if (condition_is_equal) goto loc_00AF5FF1;
    local_rbx = (uint32_t)((local_rbx) - (8));
    if (condition_is_equal) goto loc_00AF5E96;
    local_rbx = (uint32_t)((local_rbx) - (8));
    if (condition_is_equal) goto loc_00AF5E6F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00AF5DF0;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00AF51B1;
    if (((uint32_t)((uint8_t)(local_rsi + 1))) != 8) goto loc_00AF67B7;
    if (0 == 0) goto loc_00AF6566;
    v_stack_m3E0 = *(uint64_t *)(v_rip + 0x4E2523);
    result = ExpQueryElamCertInfo(*(uint64_t *)(v_rip + 0x4E2523), 0, Arg3, local_rsi);
    goto loc_00AF6865;
loc_00AF5DF0:
    v_stack_m4F0 = 19;
    result = SeSinglePrivilegeCheck(v_stack_m4F0, 0, Arg3, local_rsi);
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    local_r15 = (uint32_t)(((uint8_t)(local_rsi + 1)) - (1));
    if (condition_is_equal) goto loc_00AF5E30;
    if (((uint32_t)(local_r15)) != 3) goto loc_00AF67B7;
    v_stack_m464 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4E2523)));
    goto loc_00AF5E5D;
loc_00AF5E30:
    v_stack_m4F8 = (uint8_t)(*(uint8_t *)(v_rip + 0x4E2523));
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x4E2523)) == 0) goto loc_00AF5E52;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E3C33), 0, Arg3, local_rsi);
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
loc_00AF5E52:
    local_r13 = (uint32_t)(*(uint32_t *)(v_rip + 0x4E2523));
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x4E2523)) == 0) { local_r13 = 5; }
loc_00AF5E5D:
    result = ExpSetSoftRebootFlags((uint32_t)((uint32_t)(local_r13)), 0, Arg3, local_rsi);
    goto loc_00AF6865;
loc_00AF5E6F:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E3BFF), 0, Arg3, local_rsi);
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    result = ExpSetBootLoaderMetadata(v_rip + 5121315, (uint32_t)((uint32_t)(local_r15)), Arg3, local_rsi);
    goto loc_00AF6865;
loc_00AF5E96:
    v_stack_m478 = v_xmm0;
    result = PsGetCurrentServerSiloGlobals(v_rip + 5121315, (uint32_t)((uint32_t)(local_r15)), Arg3, local_rsi);
    v_stack_m4F0 = result + 1368;
    if (((uint32_t)(local_r15)) != 48) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E3C6A), 0, Arg3, local_rsi);
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    v_stack_m3C8 = v_xmm2;
    v_stack_m3B8 = v_xmm0;
    v_stack_m3A8 = v_xmm1;
    result = 0;
    if (condition_is_equal) goto loc_00AF5F0C;
    result = 0;
    goto loc_00AF6869;
loc_00AF5F0C:
    v_stack_m478 = v_xmm1;
    v_stack_m3B8 = v_xmm0;
    if ((uint16_t)(*(uint8_t *)(v_rip + 0x4E2523)) == 0) goto loc_00AF5FC4;
    if ((((uint8_t)(local_r13)) & ((uint8_t)(*(uint8_t *)(v_rip + 0x4E2523)))) != 0) goto loc_00AF5FC4;
    if ((((uint8_t)(local_r13)) & ((uint8_t)(v_stack_m470))) != 0) goto loc_00AF6899;
    Arg1 = ((uint16_t)(*(uint8_t *)(v_rip + 0x4E2523))) + (v_stack_m470);
    if (Arg1 > 0) goto loc_00AF5F68;
    local_rbx = *(uint8_t *)(v_rip + 0x4E2523);
    local_rdi = v_stack_m470;
    if (Arg1 < v_stack_m470) {
        result = *(uint8_t *)(result);
        local_rdi = v_stack_m470;
        local_rbx = v_stack_m478;
    }
    result = ExAllocatePool2(257, (uint32_t)((uint32_t)((uint16_t)(local_rbx))), (uint32_t)(0x50535845ULL), local_rsi);
    if (result != 0) {
        Arg3 = (uint32_t)((uint16_t)(local_rbx));
        Arg2 = local_rdi;
        Arg1 = result;
        result = memcpy(Arg1, Arg2, Arg3, local_rsi);
        v_stack_m3B0 = result;
        v_stack_m3B8 = (uint16_t)(local_rbx);
        v_stack_m3B6 = (uint16_t)(local_rbx);
    }
loc_00AF5FC4:
    *(uint64_t *)(v_stack_m4F0) = v_xmm0;
    *(uint64_t *)(v_stack_m4F0 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_m4F0 + 0x20) = v_xmm0;
    goto loc_00AF516B;
loc_00AF5FF1:
    if (((uint32_t)((uint16_t)(local_rbx))) != 32) goto loc_00AF67B7;
    result = sub_00A179B0(Arg1, result, Arg3, local_rsi);
    goto loc_00AF6865;
loc_00AF6008:
    result = CmReconcileAndValidateAllHives(Arg1, result, Arg3, local_rsi);
    goto loc_00AF6865;
loc_00AF6012:
    if (((uint32_t)(local_rbx)) > 176) goto loc_00AF61B8;
    if (((uint32_t)(local_rbx)) == 176) goto loc_00AF6140;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (159));
    if (condition_is_equal) goto loc_00AF530C;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00AF610E;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00AF675C;
    Arg1 = (uint32_t)((Arg1) - (4));
    if (condition_is_equal) goto loc_00AF60B2;
    if (Arg1 != 2) goto loc_00AF51B1;
    v_stack_m438 = v_xmm0;
    if (((uint32_t)((uint16_t)(local_rbx))) != 16) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E3A76), 0, Arg3, local_rsi);
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    v_stack_m438 = v_xmm0;
    Arg2 = (v_stack_m438) >> (32);
    result = KeIntSteerAssignCpuSetForGsiv(v_stack_m438, Arg2, v_stack_m430, local_rsi);
    goto loc_00AF6865;
loc_00AF60B2:
    if ((((uint8_t)((uint16_t)(local_rbx))) & (7)) != 0) goto loc_00AF67B7;
    if (((uint32_t)((uint16_t)(local_rbx))) > 256) goto loc_00AF67B7;
    result = memcpy(v_stack_m348, result, (uint16_t)(local_rbx), local_rsi);
    result = ExCpuSetResourceManagerAccessCheck(0, result, (uint16_t)(local_rbx), local_rsi);
    if (sign_flag) goto loc_00AF6869;
    local_r15 = (uint32_t)(((uint16_t)(local_rbx)) >> (3));
    a4 = 0;
loc_00AF60FC:
    result = KeModifySystemAllowedCpuSets((uint32_t)((uint32_t)(local_r15)), v_stack_m348, (uint16_t)(local_rbx), a4);
    goto loc_00AF6865;
loc_00AF610E:
    if (0 != 0) goto loc_00AF6695;
    if (((uint32_t)(local_r15)) != 8) goto loc_00AF67B7;
    result = kernel_indirect_call(local_r15 - 5, result, v_rip + 4527288, a4);
    goto loc_00AF6865;
loc_00AF6140:
    if (((uint32_t)(local_r15)) < 8) goto loc_00AF67B7;
    local_r15 = (uint32_t)((local_r15) + (-8));
    if ((((uint8_t)(local_r15)) & (7)) != 0) goto loc_00AF67B7;
    if (((uint32_t)(local_r15)) > 256) goto loc_00AF67B7;
    v_stack_m3D8 = *(uint64_t *)(result);
    result = memcpy(v_stack_m248, result + 8, (uint32_t)((uint32_t)(local_r15)), a4);
    result = ExCpuSetResourceManagerAccessCheck(0, result + 8, (uint32_t)((uint32_t)(local_r15)), a4);
    if (sign_flag) goto loc_00AF6867;
    local_r15 = (uint32_t)((local_r15) >> (3));
    result = KeSetTagCpuSets((uint32_t)((uint32_t)(local_r15)), v_stack_m248, *(uint64_t *)(result), a4);
    goto loc_00AF6865;
loc_00AF61B8:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(result)))) - (177));
    if (condition_is_equal) goto loc_00AF627F;
    Arg1 = (uint32_t)((Arg1) - (10));
    if (condition_is_equal) goto loc_00AF6212;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00AF675C;
    if (Arg1 != 1) goto loc_00AF51B1;
    if ((uint32_t)(local_r15) == 0) goto loc_00AF61EC;
loc_00AF61E2:
    goto loc_00AF6867;
loc_00AF61EC:
    if (0 == 0) goto loc_00AF6208;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E3885), 0, *(uint64_t *)(result), a4);
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
loc_00AF6208:
    result = VslRelaxQuotas(*(uint64_t *)(v_rip + 0x4E3885), 0, *(uint64_t *)(result), a4);
    goto loc_00AF6865;
loc_00AF6212:
    if (((uint32_t)(local_r15)) != 24) goto loc_00AF67B7;
    v_stack_m3C8 = v_xmm0;
    v_stack_m3B8 = v_xmm1;
    result = VfProbeAndCaptureUnicodeStringBuffer(v_stack_m3C8, (uint32_t)((uint32_t)(local_r13)), *(uint64_t *)(result), a4);
    if (sign_flag) goto loc_00AF6869;
    result = PsSetExeModerationState(v_stack_m3C8, (uint32_t)(v_stack_m3B8), (uint32_t)(v_stack_m3B4), a4);
    goto loc_00AF665B;
loc_00AF627F:
    result = 0;
    v_stack_m428 = v_xmm0;
    v_stack_m418 = 0;
    if (((uint32_t)(local_r15)) != 8) goto loc_00AF6343;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E37D0), 0, (uint32_t)(v_stack_m3B4), a4);
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    v_stack_m400 = *(uint64_t *)(result);
    v_stack_m4C8 = local_rsi;
    v_stack_m540 = local_rsi;
    v_stack_m548 = v_stack_m4C8;
    result = ObReferenceObjectByHandle(*(uint64_t *)(result), (uint32_t)(0x1000ULL), *(uint64_t *)(v_rip + 0x4D07D1), 0);
    if (sign_flag) goto loc_00AF6867;
    result = PsGetProcessSessionIdEx(v_stack_m4C8, (uint32_t)(0x1000ULL), *(uint64_t *)(v_rip + 0x4D07D1), 0);
    v_stack_m4F4 = (uint32_t)(result);
    if (((uint32_t)(result)) == -1) goto loc_00AF5843;
    v_stack_m418 = v_stack_m4C8;
    result = PsInvokeWin32Callout(32, v_stack_m428, (uint32_t)((uint32_t)(local_r13)), v_stack_m4F4);
    goto loc_00AF5843;
loc_00AF6343:
    if ((uint32_t)(local_r15) != 0) goto loc_00AF67B7;
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), v_stack_m428, (uint32_t)((uint32_t)(local_r13)), v_stack_m4F4);
    v_stack_m4F4 = (uint32_t)(result);
    if (((uint32_t)(result)) == -1) goto loc_00AF6867;
    v_stack_m418 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    result = PsInvokeWin32Callout(local_r15 + 32, v_stack_m428, (uint32_t)((uint32_t)(local_r13)), v_stack_m4F4);
    goto loc_00AF6865;
loc_00AF6399:
    if ((uint32_t)(local_r15) != 0) goto loc_00AF61E2;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E36CC), 0, (uint32_t)((uint32_t)(local_r13)), v_stack_m4F4);
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    result = VslProvisionDumpEncryption(*(uint64_t *)(v_rip + 0x4E36CC), 0, (uint32_t)((uint32_t)(local_r13)), v_stack_m4F4);
    if (sign_flag) goto loc_00AF6867;
    result = IoProvisionCrashDumpKey(*(uint64_t *)(v_rip + 0x4E36CC), 0, (uint32_t)((uint32_t)(local_r13)), v_stack_m4F4);
    goto loc_00AF6865;
loc_00AF63D2:
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) > 223) goto loc_00AF66C2;
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) == 223) goto loc_00AF66AF;
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) > 212) goto loc_00AF65AE;
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) == 212) goto loc_00AF659B;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)))) - (199));
    if (condition_is_equal) goto loc_00AF675C;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_00AF6513;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00AF64A0;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF6438;
    if (Arg1 != 3) goto loc_00AF51B1;
    result = CmUpdateFeatureConfiguration(result, (uint32_t)((uint32_t)(local_r15)), 0, v_stack_m4F4);
    goto loc_00AF6865;
loc_00AF6438:
    if (((uint32_t)(local_r15)) != 4) goto loc_00AF67B7;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E3634), 0, 0, v_stack_m4F4);
    if ((uint8_t)(result) == 0) goto loc_00AF6695;
    v_stack_m4E4 = (uint32_t)(local_rsi);
    v_stack_m4E4 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if ((((uint32_t)((uint32_t)(0x2018ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(result))))) != 0) goto loc_00AF6566;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x4CDF43))) & ((uint32_t)((uint32_t)(0x2018ULL))));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) | ((uint32_t)(result)));
    v_stack_m4E4 = Arg1;
    *(uint32_t *)(v_rip + 0x4CDF32) = Arg1;
    *(uint32_t *)(result) = Arg1;
    goto loc_00AF6867;
loc_00AF64A0:
    if (((uint32_t)(local_r15)) != 8) goto loc_00AF67B7;
    if (0 == 0) goto loc_00AF64C6;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E3727), 0, 0, v_stack_m4F4);
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
loc_00AF64C6:
    result = PsIsCurrentThreadInServerSilo(*(uint64_t *)(v_rip + 0x4E3727), 0, 0, v_stack_m4F4);
    if ((uint8_t)(result) != 0) goto loc_00AF6695;
    v_stack_m3C8 = *(uint64_t *)(result);
    Arg1 = (v_stack_m3C8 != ((uint8_t)(local_rsi))) ? 1 : 0;
    v_stack_m538 = (uint8_t)(Arg1);
    result = ExSetLeapSecondEnabled(Arg1, 0, 0, v_stack_m4F4);
    if (sign_flag) goto loc_00AF6869;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x408931)) = (uint8_t)(v_stack_m538);
    goto loc_00AF6867;
loc_00AF6513:
    v_stack_m450 = local_rsi;
    if (((uint32_t)(local_r15)) < 8) goto loc_00AF67B7;
    local_r15 = (uint32_t)((local_r15) + (-8));
    if ((((uint8_t)(local_r15)) & (7)) != 0) goto loc_00AF67B7;
    if (((uint32_t)(local_r15)) > 256) goto loc_00AF67B7;
    v_stack_m450 = *(uint64_t *)(result);
    result = memcpy(v_stack_m148, result + 8, (uint32_t)((uint32_t)(local_r15)), v_stack_m4F4);
    if ((*(uint64_t *)(result)) < 2) goto loc_00AF6570;
loc_00AF6566:
    goto loc_00AF6869;
loc_00AF6570:
    result = ExCpuSetResourceManagerAccessCheck(0, result + 8, (uint32_t)((uint32_t)(local_r15)), v_stack_m4F4);
    if (sign_flag) goto loc_00AF6867;
    local_r15 = (uint32_t)((local_r15) >> (3));
    goto loc_00AF60FC;
loc_00AF659B:
    result = CmUpdateFeatureUsageSubscription(result, (uint32_t)((uint32_t)(local_r15)), 0, (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    goto loc_00AF6865;
loc_00AF65AE:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(result)))) - (217));
    if (condition_is_equal) goto loc_00AF6682;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF6665;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF65D3;
    if (Arg1 != 1) goto loc_00AF51B1;
loc_00AF65D3:
    if (((uint32_t)(local_r15)) != 16) goto loc_00AF67B7;
    if (0 == 0) goto loc_00AF6627;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E3494), 0, 0, (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    result = VfProbeAndCaptureUnicodeString(v_stack_m508, result, (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    if (sign_flag) goto loc_00AF6869;
    if (v_stack_m508 != ((uint16_t)(local_rsi))) goto loc_00AF6627;
loc_00AF661D:
    goto loc_00AF6869;
loc_00AF6627:
    local_rbx = (uint32_t)((*(uint64_t *)(result)) - (219));
    if (condition_is_equal) goto loc_00AF6645;
    if (((uint32_t)(local_rbx)) == 1) goto loc_00AF663B;
loc_00AF6634:
    goto loc_00AF664F;
loc_00AF663B:
    result = VfVolatileRemoveDifVerification(v_stack_m508, result, (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    goto loc_00AF664D;
loc_00AF6645:
    result = VfVolatileApplyDifVerification(v_stack_m508, result, (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)(*(uint64_t *)(result))));
loc_00AF664D:
loc_00AF664F:
    if (0 == 0) goto loc_00AF6867;
loc_00AF665B:
    result = VfFreeCapturedUnicodeString(v_stack_m508, result, (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    goto loc_00AF6867;
loc_00AF6665:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E3411), 0, (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    if ((uint8_t)(result) == 0) goto loc_00AF6695;
    result = VfVolatileClearDifRuleClass(*(uint64_t *)(v_rip + 0x4E3411), 0, (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    goto loc_00AF6865;
loc_00AF6682:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E33F4), 0, (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    if ((uint8_t)(result) != 0) goto loc_00AF669F;
loc_00AF6695:
    goto loc_00AF6869;
loc_00AF669F:
    result = VfVolatileSetDifRuleClass(v_stack_m508, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    goto loc_00AF6865;
loc_00AF66AF:
    result = ExPoolSetLimit(v_stack_m508, local_r15, 0, (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    goto loc_00AF6865;
loc_00AF66C2:
    if (((uint32_t)(local_rbx)) > 233) goto loc_00AF678E;
    if (((uint32_t)(local_rbx)) == 233) goto loc_00AF677E;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (224));
    if (condition_is_equal) goto loc_00AF675C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF675C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AF6735;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00AF66F7;
    if (Arg1 != 1) goto loc_00AF51B1;
loc_00AF66F7:
    v_stack_m537 = (uint8_t)(local_rsi);
    Arg1 = 0;
    result = RtlCheckTokenMembership(Arg1, *(uint64_t *)(v_rip + 0x4E3360), v_stack_m537, (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    if (sign_flag) goto loc_00AF67D4;
    if (v_stack_m537 == ((uint8_t)(local_rsi))) goto loc_00AF67D4;
    result = KeUpdateDpcWatchdogConfiguration(v_stack_m508, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    goto loc_00AF6865;
loc_00AF6735:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E3341), 0, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    if ((uint8_t)(result) == 0) goto loc_00AF67D4;
    Arg1 = ((uint32_t)(local_r15) == 0) ? 1 : 0;
    result = VfPtGenerateTraceInformation(Arg1, 0, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    goto loc_00AF6865;
loc_00AF675C:
    if (*(uint64_t *)(v_rip + 0x40E77D) == 0) goto loc_00AF530C;
    result = guard_dispatch_icall((uint32_t)((uint32_t)(local_rbx)), v_stack_m508, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    goto loc_00AF6865;
loc_00AF677E:
    result = PnpIommuBlockUnblockDevice(v_stack_m508, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    goto loc_00AF6865;
loc_00AF678E:
    local_rbx = (uint32_t)((local_rbx) - (235));
    if (condition_is_equal) goto loc_00AF684F;
    local_rbx = (uint32_t)((local_rbx) - (8));
    if (condition_is_equal) goto loc_00AF530C;
    local_rbx = (uint32_t)((local_rbx) - (2));
    if (condition_is_equal) goto loc_00AF67F5;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00AF51B1;
    if (((uint32_t)(local_r15)) == 4) goto loc_00AF67C1;
loc_00AF67B7:
    goto loc_00AF6869;
loc_00AF67C1:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E32B5), 0, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    if ((uint8_t)(result) != 0) goto loc_00AF67DE;
loc_00AF67D4:
    goto loc_00AF6869;
loc_00AF67DE:
    v_stack_m3C8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m508)));
    *(uint32_t *)(v_rip + 0x4D05EE) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m508)));
    goto loc_00AF516B;
loc_00AF67F5:
    if (((uint32_t)(local_r15)) != 4) goto loc_00AF54A2;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E3277), 0, (uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(*(uint64_t *)(result))));
    if ((uint8_t)(result) != 0) goto loc_00AF6819;
loc_00AF6812:
    goto loc_00AF6867;
loc_00AF6819:
    v_stack_m460 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m508)));
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_m508)) + 3999) - (0);
    Arg1 = (Arg1) >> (1);
    Arg1 = (Arg1) + (0);
    Arg1 = (Arg1) >> (11);
    *(uint32_t *)(v_rip + 0x3F87A3) = Arg1;
    goto loc_00AF6867;
loc_00AF684F:
    v_stack_m548 = local_rsi;
    a4 = 0;
    result = HvlQuerySetBootPagesInfo(v_stack_m508, (uint32_t)((uint32_t)(local_r15)), 0, a4);
loc_00AF6865:
loc_00AF6867:
loc_00AF6869:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)((uint32_t)(local_r15)), 0, a4);
    local_rsp = (local_rsp) + (0x530ULL);
    return result;
loc_00AF688D:
    result = ExRaiseDatatypeMisalignment(Arg1, (uint32_t)((uint32_t)(local_r15)), 0, a4);
loc_00AF6893:
    result = ExRaiseDatatypeMisalignment(Arg1, (uint32_t)((uint32_t)(local_r15)), 0, a4);
loc_00AF6899:
    result = ExRaiseDatatypeMisalignment(Arg1, (uint32_t)((uint32_t)(local_r15)), 0, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x0 + r15*1` | `64` | `R` |
| `Arg2` | `+ 0x4` | `8` | `R` |
| `Arg2` | `+ 0x8` | `8` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x8` | `128` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `W` |
| `Arg2` | `+ 0x10` | `128` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `W` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `W` |
| `Arg2` | `+ 0x20` | `128` | `R` |
| `Arg2` | `+ 0x28` | `32` | `W` |
| `Arg2` | `+ 0x28` | `64` | `W` |
| `Arg2` | `+ 0x30` | `32` | `W` |
| `Arg2` | `+ 0x3C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AF4A60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
