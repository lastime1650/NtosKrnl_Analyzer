# NtPowerInformation

- RVA: `0x00955D80`–`0x00957F4A` (길이 `8,650` bytes)
- VA: `0x0000000140955D80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009238C`
- 디코드: `1,949`개 명령, `8,650/8,650` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **154**; 고유 호출 대상: **111**
- 직접 호출자로 확인된 함수: **13**
- RIP 상대 이미지 참조: **76**

### Outgoing calls
- `0x00955DCF` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00955EEB` → [SeIsAppContainerOrIdentifyLevelContext](../A2/SeIsAppContainerOrIdentifyLevelContext_function_00A21A74.md) (function, `0x00A21A74`)
- `0x00955F12` → [PopCapabilityCheck](../../text/4D/PopCapabilityCheck_function_004DFF10.md) (function, `0x004DFF10`)
- `0x00955F74` → [ExCheckFullProcessInformationAccess](ExCheckFullProcessInformationAccess_function_0095D93C.md) (function, `0x0095D93C`)
- `0x00955FA8` → [EtwpCoverageUserIsAdmin](../9F/EtwpCoverageUserIsAdmin_function_009FE548.md) (function, `0x009FE548`)
- `0x00955FCC` → [PopIsRunningAsLocalSystem](../A8/PopIsRunningAsLocalSystem_function_00A88594.md) (function, `0x00A88594`)
- `0x0095600C` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00956048` → [EtwpCoverageUserIsAdmin](../9F/EtwpCoverageUserIsAdmin_function_009FE548.md) (function, `0x009FE548`)
- `0x009560AA` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x0095610A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0095611F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00956159` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x009561C2` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00956259` → [PopCurrentPowerState](../A3/PopCurrentPowerState_function_00A356D8.md) (function, `0x00A356D8`)
- `0x009562EA` → [PopResetCurrentPolicies](../90/PopResetCurrentPolicies_function_0090FF64.md) (function, `0x0090FF64`)
- `0x00956313` → [PopDisksRegisteredForIdle](../../text/4A/PopDisksRegisteredForIdle_function_004A527C.md) (function, `0x004A527C`)
- `0x0095632D` → [PopFilterCapabilities](../91/PopFilterCapabilities_function_0091141C.md) (function, `0x0091141C`)
- `0x0095637B` → [PopVerifySystemPowerPolicy](../91/PopVerifySystemPowerPolicy_function_00910A8C.md) (function, `0x00910A8C`)
- `0x009563DA` → [PopApplyPolicy](../91/PopApplyPolicy_function_009107B0.md) (function, `0x009107B0`)
- `0x00956541` → [PopChangeCapability](../90/PopChangeCapability_function_0090FF48.md) (function, `0x0090FF48`)
- `0x0095658F` → [KeQueryPrimaryGroupThread](../../text/49/KeQueryPrimaryGroupThread_function_004903B4.md) (function, `0x004903B4`)
- `0x009565A5` → [PopProcessorInformation](../A1/PopProcessorInformation_function_00A11CA0.md) (function, `0x00A11CA0`)
- `0x009565F0` → [PopAcquireTransitionLock](../AA/PopAcquireTransitionLock_function_00AA9E7C.md) (function, `0x00AA9E7C`)
- `0x009565F5` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x0095660D` → [PopSetHiberPersistedRegValue](../6F/PopSetHiberPersistedRegValue_function_006FE9F0.md) (function, `0x006FE9F0`)
- `0x00956619` → [PopHibernateEvaluation](../90/PopHibernateEvaluation_function_0090F7B0.md) (function, `0x0090F7B0`)
- `0x00956620` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00956627` → [PopReleaseTransitionLock](../AB/PopReleaseTransitionLock_function_00ABDABC.md) (function, `0x00ABDABC`)
- `0x00956653` → [PopApplyAdminPolicy](../AD/PopApplyAdminPolicy_function_00AD1B34.md) (function, `0x00AD1B34`)
- `0x00956665` → [PopResetCurrentPolicies](../90/PopResetCurrentPolicies_function_0090FF64.md) (function, `0x0090FF64`)
- `0x00956888` → [PopLoggingInformation](../A3/PopLoggingInformation_function_00A395B0.md) (function, `0x00A395B0`)
- `0x009568E0` → [PopLogSleepDisabled](../91/PopLogSleepDisabled_function_009102D8.md) (function, `0x009102D8`)
- `0x00956953` → [PopDiagTraceAppPowerMessage](../A7/PopDiagTraceAppPowerMessage_function_00A7080C.md) (function, `0x00A7080C`)
- `0x0095695D` → [PopDiagTraceAppPowerMessageEnd](../A7/PopDiagTraceAppPowerMessageEnd_function_00A7DFA0.md) (function, `0x00A7DFA0`)
- `0x00956990` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009569C4` → [PopSuspendResumePdc](../A9/PopSuspendResumePdc_function_00A910AC.md) (function, `0x00A910AC`)
- `0x009569D4` → [PoPowerOffMonitor](../../text/4D/PoPowerOffMonitor_function_004D63C0.md) (function, `0x004D63C0`)
- `0x00956A78` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00956AA4` → [PopSetPowerSettingValue](../91/PopSetPowerSettingValue_function_00914E54.md) (function, `0x00914E54`)
- `0x00956B14` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (function, `0x004575EC`)
- `0x00956B2E` → [PopDiagTraceServiceNotification](../A7/PopDiagTraceServiceNotification_function_00A7BBB0.md) (function, `0x00A7BBB0`)
- `0x00956B69` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00956B9A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00956BCF` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00956BE0` → [PopGetWakeSource](../AB/PopGetWakeSource_function_00ABDB68.md) (function, `0x00ABDB68`)
- `0x00956C01` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00956C25` → [PopGetWakeSource](../AB/PopGetWakeSource_function_00ABDB68.md) (function, `0x00ABDB68`)
- `0x00956C44` → [PpmSetSimulatedLoad](../AC/PpmSetSimulatedLoad_function_00ACD710.md) (function, `0x00ACD710`)
- `0x00956C54` → [PpmClearSimulatedLoad](../AC/PpmClearSimulatedLoad_function_00ACE938.md) (function, `0x00ACE938`)
- `0x00956CB6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00956CCC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00956CD8` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00956CFC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00956D2D` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (function, `0x0049BF40`)
- `0x00956DAE` → [DbgkWerCaptureLiveKernelDump2](../AC/DbgkWerCaptureLiveKernelDump2_function_00AC1F10.md) (function, `0x00AC1F10`)
- `0x00956DC4` → [PopProcessSessionDisplayStateChange](../91/PopProcessSessionDisplayStateChange_function_00914380.md) (function, `0x00914380`)
- `0x00956DCD` → [PopSetDisplayStatus](../91/PopSetDisplayStatus_function_009129E0.md) (function, `0x009129E0`)
- `0x00956DD6` → [PopUpdateConsoleDisplayState](../A3/PopUpdateConsoleDisplayState_function_00A31298.md) (function, `0x00A31298`)
- `0x00956DE6` → [PopPowerAggregatorNotifyDisplayPoweredOn](../70/PopPowerAggregatorNotifyDisplayPoweredOn_function_007003C4.md) (function, `0x007003C4`)
- `0x00956E1A` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00956E3C` → [PopDiagTraceSessionDisplayStateChange](../../text/4B/PopDiagTraceSessionDisplayStateChange_function_004B7C00.md) (function, `0x004B7C00`)
- `0x00956E6E` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00956E81` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)
- `0x00956E9E` → [TtmIsEnabled](../91/TtmIsEnabled_function_009143D8.md) (function, `0x009143D8`)
- `0x00956EAA` → [TtmIsEnabled](../91/TtmIsEnabled_function_009143D8.md) (function, `0x009143D8`)
- `0x00956EB3` → [TtmInitCurrentSession](../98/TtmInitCurrentSession_function_0098AA18.md) (function, `0x0098AA18`)
- `0x00956EC9` → [PopPowerRequestNotifyTtmSessionInitialized](../AD/PopPowerRequestNotifyTtmSessionInitialized_function_00AD1608.md) (function, `0x00AD1608`)
- `0x00956ECE` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00956FBD` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00956FD3` → [PopPrintEx](../../text/48/PopPrintEx_function_0048EF24.md) (function, `0x0048EF24`)
- `0x00956FE4` → [PopDiagTraceSessionState](../91/PopDiagTraceSessionState_function_00912C5C.md) (function, `0x00912C5C`)
- `0x00956FE9` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00957033` → [PopSetPowerSettingValueAcDc](../91/PopSetPowerSettingValueAcDc_function_00914D6C.md) (function, `0x00914D6C`)
- `0x0095705C` → [PopShutdownListenerInsertCallback](../../text/4D/PopShutdownListenerInsertCallback_function_004D94C4.md) (function, `0x004D94C4`)
- `0x00957087` → [PopPowerRequestActionInfo](../A2/PopPowerRequestActionInfo_function_00A21968.md) (function, `0x00A21968`)
- `0x009570E7` → [PpmParkApplyForcedMask](../76/PpmParkApplyForcedMask_function_0076A904.md) (function, `0x0076A904`)
- `0x009570FE` → [PpmParkClearForcedMask](../76/PpmParkClearForcedMask_function_0076AB20.md) (function, `0x0076AB20`)
- `0x0095711E` → [PopUmpoSendLegacyEvent](../AA/PopUmpoSendLegacyEvent_function_00AA48E8.md) (function, `0x00AA48E8`)
- `0x00957160` → [KeQueryActiveGroupCount](../../text/48/KeQueryActiveGroupCount_function_0048C600.md) (function, `0x0048C600`)
- `0x0095717F` → [PopProcessorInformation](../A1/PopProcessorInformation_function_00A11CA0.md) (function, `0x00A11CA0`)
- `0x009571A5` → [PopGetPowerRequestListInfo](../A9/PopGetPowerRequestListInfo_function_00A92948.md) (function, `0x00A92948`)
- `0x009571E1` → [ExGetWakeTimerList](../../text/4C/ExGetWakeTimerList_function_004CB964.md) (function, `0x004CB964`)
- `0x00957281` → [PpmParkSetLpiCap](../../text/4D/PpmParkSetLpiCap_function_004D9358.md) (function, `0x004D9358`)
- `0x009572CF` → [PpmSetSimulatedIdle](../../text/4D/PpmSetSimulatedIdle_function_004D74C0.md) (function, `0x004D74C0`)
- `0x009572E6` → [PpmClearSimulatedIdle](../../text/4D/PpmClearSimulatedIdle_function_004D8C9C.md) (function, `0x004D8C9C`)
- `0x00957311` → [PopAcquireTransitionLock](../AA/PopAcquireTransitionLock_function_00AA9E7C.md) (function, `0x00AA9E7C`)
- `0x00957316` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x0095732B` → [PopSetHiberFileSize](../70/PopSetHiberFileSize_function_00703974.md) (function, `0x00703974`)
- `0x00957332` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x0095733C` → [PopReleaseTransitionLock](../AB/PopReleaseTransitionLock_function_00ABDABC.md) (function, `0x00ABDABC`)
- `0x0095738B` → [Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline_function_004F5DA0.md) (function, `0x004F5DA0`)
- `0x009573D3` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x009573E2` → [PopSessionConnectionChange](../76/PopSessionConnectionChange_function_0076BDEC.md) (function, `0x0076BDEC`)
- `0x009573F7` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x009573FE` → [Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline_function_004F5DA0.md) (function, `0x004F5DA0`)
- `0x00957421` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00957483` → [PopEnforceResiliencyScenarios](../AC/PopEnforceResiliencyScenarios_function_00AC3D90.md) (function, `0x00AC3D90`)
- `0x009574BF` → [PopGetSettingValue](../91/PopGetSettingValue_function_00913310.md) (function, `0x00913310`)
- `0x009574F4` → [PopGetSettingNotificationName](../91/PopGetSettingNotificationName_function_0091346C.md) (function, `0x0091346C`)
- `0x0095751D` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00957532` → [PopPrintEx](../../text/48/PopPrintEx_function_0048EF24.md) (function, `0x0048EF24`)
- `0x00957543` → [PopDiagTraceSessionState](../91/PopDiagTraceSessionState_function_00912C5C.md) (function, `0x00912C5C`)
- `0x0095754A` → [PopFreeSessionState](../91/PopFreeSessionState_function_00912D00.md) (function, `0x00912D00`)
- `0x0095754F` → [TtmIsEnabled](../91/TtmIsEnabled_function_009143D8.md) (function, `0x009143D8`)
- `0x0095755C` → [PopPowerRequestNotifyTtmSessionUninitialized](../AD/PopPowerRequestNotifyTtmSessionUninitialized_function_00AD2B30.md) (function, `0x00AD2B30`)
- `0x00957561` → [TtmCleanupCurrentSession](../AC/TtmCleanupCurrentSession_function_00AC54DC.md) (function, `0x00AC54DC`)
- `0x009575C8` → [PopMonitorInvocation](../76/PopMonitorInvocation_function_00769710.md) (function, `0x00769710`)
- `0x00957601` → [PopPdcInvocation](../AD/PopPdcInvocation_function_00AD87F8.md) (function, `0x00AD87F8`)
- `0x0095761D` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (function, `0x0049BF40`)
- `0x0095763F` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00957673` → [PopFilterCapabilities](../91/PopFilterCapabilities_function_0091141C.md) (function, `0x0091141C`)
- `0x0095768A` → [PopReadHiberbootPolicy](../A9/PopReadHiberbootPolicy_function_00A9517C.md) (function, `0x00A9517C`)
- `0x009576CA` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x009576D9` → [PopSessionWinlogonNotification](../76/PopSessionWinlogonNotification_function_0076BF60.md) (function, `0x0076BF60`)
- `0x009576F9` → [PopInitPlatformSettings](../../init/C3/PopInitPlatformSettings_function_00C3D40C.md) (function, `0x00C3D40C`)
- `0x00957700` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (function, `0x0049BF40`)
- `0x0095776F` → [PopPdcCsDeviceNotification](../AA/PopPdcCsDeviceNotification_function_00AA1B28.md) (function, `0x00AA1B28`)
- `0x009577B5` → [PopPowerRequestCreateUserModeRequest](../../text/22/PopPowerRequestCreateUserModeRequest_function_0022F91C.md) (function, `0x0022F91C`)
- `0x009577E3` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00957806` → [PopCapturePlatformRole](../A8/PopCapturePlatformRole_function_00A864AC.md) (function, `0x00A864AC`)
- `0x0095788B` → [PpmSetExitLatencySamplingPercentage](../../text/4D/PpmSetExitLatencySamplingPercentage_function_004DA9B0.md) (function, `0x004DA9B0`)
- `0x00957895` → [PpmClearExitLatencySamplingPercentage](../../text/4E/PpmClearExitLatencySamplingPercentage_function_004E1538.md) (function, `0x004E1538`)
- `0x009578B8` → [TtmIsEnabled](../91/TtmIsEnabled_function_009143D8.md) (function, `0x009143D8`)
- `0x009578D1` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x009578E3` → [TtmNotifySessionDisplayBurst](../98/TtmNotifySessionDisplayBurst_function_0098B300.md) (function, `0x0098B300`)
- `0x00957922` → [PopEventCalloutDispatch](../../text/4B/PopEventCalloutDispatch_function_004B4870.md) (function, `0x004B4870`)
- `0x00957933` → [PopDiagTraceDisplayBurstWin32kCallout](../AC/PopDiagTraceDisplayBurstWin32kCallout_function_00AC1CF8.md) (function, `0x00AC1CF8`)
- `0x009579DE` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (function, `0x004575EC`)
- `0x009579FB` → [PopBatteryDeviceState](../A7/PopBatteryDeviceState_function_00A7905C.md) (function, `0x00A7905C`)
- `0x00957A31` → [PopPowerRequestReferenceAcquire](../../text/47/PopPowerRequestReferenceAcquire_function_004776C0.md) (function, `0x004776C0`)
- `0x00957A3B` → [PopPowerRequestReferenceRelease](../../text/47/PopPowerRequestReferenceRelease_function_004775B0.md) (function, `0x004775B0`)
- `0x00957A79` → [PopThermalProcessUsermodeEvent](../AB/PopThermalProcessUsermodeEvent_function_00AB7D58.md) (function, `0x00AB7D58`)
- `0x00957A9F` → [PopCurrentPowerStatePrecise](../A3/PopCurrentPowerStatePrecise_function_00A35624.md) (function, `0x00A35624`)
- `0x00957AF3` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00957B03` → [PopCapabilityCheck](../../text/4D/PopCapabilityCheck_function_004DFF10.md) (function, `0x004DFF10`)
- `0x00957B47` → [TtmDispatchApi](../98/TtmDispatchApi_function_0098AD08.md) (function, `0x0098AD08`)
- `0x00957B84` → [PopPowerInformationInternal](../A8/PopPowerInformationInternal_function_00A8B7C0.md) (function, `0x00A8B7C0`)
- `0x00957BFE` → [PopEtEnergyTrackerCreate](../76/PopEtEnergyTrackerCreate_function_00769EE0.md) (function, `0x00769EE0`)
- `0x00957C08` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (function, `0x0049BF40`)
- `0x00957C37` → [PopFxIsDevicePotentialDripsConstraint](../../text/4A/PopFxIsDevicePotentialDripsConstraint_function_004A5D34.md) (function, `0x004A5D34`)
- `0x00957C82` → [PopUpdatePowerButtonHoldState](../../text/4D/PopUpdatePowerButtonHoldState_function_004D4EB4.md) (function, `0x004D4EB4`)
- `0x00957CAD` → [PopAcquireTransitionLock](../AA/PopAcquireTransitionLock_function_00AA9E7C.md) (function, `0x00AA9E7C`)
- `0x00957CB2` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00957CC7` → [PopSetHiberFileType](../70/PopSetHiberFileType_function_00703268.md) (function, `0x00703268`)
- `0x00957CCE` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00957CFC` → [PopScreenOff](../98/PopScreenOff_function_0098A758.md) (function, `0x0098A758`)
- `0x00957D3C` → [PopEtEnergyTrackerQuery](../98/PopEtEnergyTrackerQuery_function_0098B668.md) (function, `0x0098B668`)
- `0x00957D96` → [PopCurrentSystemPowerSourceState](../AE/PopCurrentSystemPowerSourceState_function_00AE2D3C.md) (function, `0x00AE2D3C`)
- `0x00957DFE` → [PopBlackBoxDirectAccess](../AC/PopBlackBoxDirectAccess_function_00ACD824.md) (function, `0x00ACD824`)
- `0x00957E48` → [PopSendSuspendResumeNotifications](../AD/PopSendSuspendResumeNotifications_function_00AD425C.md) (function, `0x00AD425C`)
- `0x00957E77` → [ExNotifyCallback](../../text/39/ExNotifyCallback_function_003926B0.md) (function, `0x003926B0`)
- `0x00957EAB` → [PopBlackBoxUpdate](../A2/PopBlackBoxUpdate_function_00A26078.md) (function, `0x00A26078`)
- `0x00957EE6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00957F32` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopRecordPoIrpBlackboxInformation](../../text/4C/PopRecordPoIrpBlackboxInformation_function_004CE14C.md) at `0x004CE3BA`
- [PopRecordPowerWatchdogBlackboxInformation](../../text/4D/PopRecordPowerWatchdogBlackboxInformation_function_004D3A18.md) at `0x004D3BCE`
- [PopRecordPepWorkorderBlackboxInformation](../../text/5D/PopRecordPepWorkorderBlackboxInformation_function_005DF8F8.md) at `0x005DFA67`
- [WheaLogInternalEvent](../../text/66/WheaLogInternalEvent_function_006605B0.md) at `0x00660620`
- [PnpRecordBlackboxDelayedRemoveWorkerInformation](../73/PnpRecordBlackboxDelayedRemoveWorkerInformation_function_0073F908.md) at `0x0073F9E7`
- [TtmpCalloutArmWatchdog](../77/TtmpCalloutArmWatchdog_function_007761DC.md) at `0x00776269`
- [TtmpCalloutWatchdogCallback](../77/TtmpCalloutWatchdogCallback_function_00776280.md) at `0x007762CA`
- [TtmpStartCallout](../77/TtmpStartCallout_function_00776AA4.md) at `0x00776B9F`
- [TtmpStopCallout](../77/TtmpStopCallout_function_00776C24.md) at `0x00776C98`
- [PnpRecordBlackboxDeviceCompletionQueueInformation](PnpRecordBlackboxDeviceCompletionQueueInformation_function_00955A20.md) at `0x00955A84`
- [PnpRecordBlackboxPnpEventWorkerInformation](PnpRecordBlackboxPnpEventWorkerInformation_function_00955CD8.md) at `0x00955D3C`
- [PnpRecordBlackboxPnpEventInformation](../A0/PnpRecordBlackboxPnpEventInformation_function_00A04EE0.md) at `0x00A04FF6`
- [VslRegisterIumPowerCallbacks](../../init/C2/VslRegisterIumPowerCallbacks_function_00C29DF0.md) at `0x00C29E1B`

### Static image references
- `0x00955D93` → RVA `0x00E0A740` (`.data`; read)
- `0x00955F0B` → RVA `0x00B01C10` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0095608C` → RVA `0x00FD9B30` (`PAGEDATA`; read)
- `0x00956096` → RVA `0x00FD9D40` (`PAGEDATA`; read)
- `0x0095628B` → RVA `0x00F0CF0C` (`.data`; read)
- `0x009562A7` → RVA `0x00F0CEC0` (`.data`; read)
- `0x009562B3` → RVA `0x00F0CED0` (`.data`; read)
- `0x009562BF` → RVA `0x00F0CEE0` (`.data`; read)
- `0x009562CB` → RVA `0x00F0CEF0` (`.data`; read)
- `0x009562D8` → RVA `0x00F0CF00` (`.data`; write)
- `0x009562E4` → RVA `0x00F0CF08` (`.data`; write)
- `0x00956305` → RVA `0x00F0CCE8` (`.data`; read)
- `0x0095630D` → RVA `0x00F0CEC9` (`.data`; write)
- `0x00956318` → RVA `0x00F0CED5` (`.data`; write)
- `0x009563EC` → RVA `0x00F0CD24` (`.data`; read)
- `0x0095641D` → RVA `0x00F0CC40` (`.data`; read)
- `0x00956439` → RVA `0x00B71750` (`PopShutdownHandler`; read)
- `0x00956440` → RVA `0x00F0CCA8` (`.data`; read)
- `0x009564A7` → RVA `0x00F0CED1` (`.data`; read)
- `0x009564B0` → RVA `0x00F0CEC7` (`.data`; read)
- `0x009564C9` → RVA `0x00F0CEC6` (`.data`; read)
- `0x009564E0` → RVA `0x00F0CEC5` (`.data`; read)
- `0x009564F7` → RVA `0x00F0CEC4` (`.data`; read)
- `0x0095650E` → RVA `0x00F0CEC3` (`.data`; read)
- `0x00956525` → RVA `0x00F0CF00` (`.data`; read)
- `0x00956602` → RVA `0x00FC5104` (`ALMOSTRO`; write)
- `0x00956674` → RVA `0x00F0CD00` (`.data`; read)
- `0x0095669F` → RVA `0x00F0CE68` (`.data`; read)
- `0x009566BD` → RVA `0x00B50DC0` (`PpmProcessorDriverDispatchTable`; read)
- `0x009566E8` → RVA `0x00F0BC64` (`.data`; read)
- `0x009566F5` → RVA `0x00F0BC6C` (`.data`; read)
- `0x009566FB` → RVA `0x00F0BC68` (`.data`; read)
- `0x00956708` → RVA `0x00E67848` (`.data`; read)
- `0x00956783` → RVA `0x00F0C700` (`.data`; read)
- `0x00956799` → RVA `0x00F0C700` (`.data`; write)
- `0x009567B8` → RVA `0x00E019F8` (`.data`; read)
- `0x009567C8` → RVA `0x00E019C8` (`.data`; read)
- `0x00956805` → RVA `0x00F0BDA0` (`.data`; read)
- `0x00956830` → RVA `0x00F0BD98` (`.data`; read)
- `0x009569B2` → RVA `0x00E67A50` (`.data`; read)
- `0x009569CE` → RVA `0x00E67A55` (`.data`; write)
- `0x00956B41` → RVA `0x00F0BF40` (`.data`; read)
- `0x00956B4B` → RVA `0x00F0BF38` (`.data`; read)
- `0x00956DA7` → RVA `0x00B01C40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00956E13` → RVA `0x00020AE8` (`.rdata`; read)
- `0x00956E67` → RVA `0x00F08440` (`.data`; read)
- `0x00956E73` → RVA `0x00E67A28` (`.data`; read)
- `0x00956EDA` → RVA `0x00F0C6F4` (`.data`; read)
- `0x00956EE9` → RVA `0x00E67A55` (`.data`; read)
- `0x00956EFA` → RVA `0x00F0CE11` (`.data`; read)
- `0x00956F0B` → RVA `0x00F0CE0C` (`.data`; read)
- `0x00956F18` → RVA `0x00F0CE2C` (`.data`; read)
- `0x00956F25` → RVA `0x00F0CE30` (`.data`; read)
- `0x00956F32` → RVA `0x00F0CE34` (`.data`; read)
- `0x00956F3F` → RVA `0x00F0CE38` (`.data`; read)
- `0x00956F4C` → RVA `0x00F0CE3C` (`.data`; read)
- `0x00956F59` → RVA `0x00F0CE40` (`.data`; read)
- `0x00956F66` → RVA `0x00E0B579` (`.data`; read)
- `0x00956F73` → RVA `0x00E0B570` (`.data`; read)
- `0x00956FC7` → RVA `0x00B03110` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00956FDD` → RVA `0x000119F8` (`.rdata`; read)
- `0x0095702C` → RVA `0x0001C338` (`.rdata`; read)
- `0x009570B1` → RVA `0x00F475F8` (`.data`; read)
- `0x0095740F` → RVA `0x00E67798` (`.data`; read)
- `0x00957527` → RVA `0x00B03150` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0095753C` → RVA `0x000119E8` (`.rdata`; read)
- `0x00957705` → RVA `0x00F0CED4` (`.data`; write)
- `0x009577E8` → RVA `0x00F0E790` (`.data`; write)
- `0x009578B1` → RVA `0x00E67A38` (`.data`; read)
- `0x00957906` → RVA `0x00E67A54` (`.data`; read)
- `0x0095794F` → RVA `0x00F0C3D0` (`.data`; read)
- `0x0095795C` → RVA `0x00F0C580` (`.data`; read)
- `0x0095796B` → RVA `0x00F0C588` (`.data`; read)
- `0x0095797A` → RVA `0x00F0C300` (`.data`; read)
- `0x00957AFC` → RVA `0x00B01C80` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00957E70` → RVA `0x00F8A990` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **69**
  - `0x00955DCF` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00955F12` → [PopCapabilityCheck](../../text/4D/PopCapabilityCheck_function_004DFF10.md) (`PAGE` → `.text`)
  - `0x0095600C` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x0095610A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0095611F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009561C2` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00956313` → [PopDisksRegisteredForIdle](../../text/4A/PopDisksRegisteredForIdle_function_004A527C.md) (`PAGE` → `.text`)
  - `0x0095658F` → [KeQueryPrimaryGroupThread](../../text/49/KeQueryPrimaryGroupThread_function_004903B4.md) (`PAGE` → `.text`)
  - `0x009565F5` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00956620` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x00956990` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009569D4` → [PoPowerOffMonitor](../../text/4D/PoPowerOffMonitor_function_004D63C0.md) (`PAGE` → `.text`)
  - `0x00956A78` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00956B14` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (`PAGE` → `.text`)
  - `0x00956B69` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00956B9A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00956BCF` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x00956C01` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00956CB6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00956CCC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00956CD8` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x00956CFC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00956D2D` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (`PAGE` → `.text`)
  - `0x00956E1A` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
  - `0x00956E3C` → [PopDiagTraceSessionDisplayStateChange](../../text/4B/PopDiagTraceSessionDisplayStateChange_function_004B7C00.md) (`PAGE` → `.text`)
  - `0x00956E6E` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00956E81` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
  - `0x00956ECE` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00956FBD` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00956FD3` → [PopPrintEx](../../text/48/PopPrintEx_function_0048EF24.md) (`PAGE` → `.text`)
  - `0x00956FE9` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x0095705C` → [PopShutdownListenerInsertCallback](../../text/4D/PopShutdownListenerInsertCallback_function_004D94C4.md) (`PAGE` → `.text`)
  - `0x00957160` → [KeQueryActiveGroupCount](../../text/48/KeQueryActiveGroupCount_function_0048C600.md) (`PAGE` → `.text`)
  - `0x009571E1` → [ExGetWakeTimerList](../../text/4C/ExGetWakeTimerList_function_004CB964.md) (`PAGE` → `.text`)
  - `0x00957281` → [PpmParkSetLpiCap](../../text/4D/PpmParkSetLpiCap_function_004D9358.md) (`PAGE` → `.text`)
  - `0x009572CF` → [PpmSetSimulatedIdle](../../text/4D/PpmSetSimulatedIdle_function_004D74C0.md) (`PAGE` → `.text`)
  - `0x009572E6` → [PpmClearSimulatedIdle](../../text/4D/PpmClearSimulatedIdle_function_004D8C9C.md) (`PAGE` → `.text`)
  - `0x00957316` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00957332` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x0095738B` → [Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline_function_004F5DA0.md) (`PAGE` → `.text`)
  - `0x009573D3` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x009573F7` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x009573FE` → [Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline_function_004F5DA0.md) (`PAGE` → `.text`)
  - `0x00957421` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0095751D` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00957532` → [PopPrintEx](../../text/48/PopPrintEx_function_0048EF24.md) (`PAGE` → `.text`)
  - `0x0095761D` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (`PAGE` → `.text`)
  - `0x0095763F` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x009576CA` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x009576F9` → [PopInitPlatformSettings](../../init/C3/PopInitPlatformSettings_function_00C3D40C.md) (`PAGE` → `INIT`)
  - `0x00957700` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (`PAGE` → `.text`)
  - `0x009577B5` → [PopPowerRequestCreateUserModeRequest](../../text/22/PopPowerRequestCreateUserModeRequest_function_0022F91C.md) (`PAGE` → `.text`)
  - `0x009577E3` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGE` → `.text`)
  - `0x0095788B` → [PpmSetExitLatencySamplingPercentage](../../text/4D/PpmSetExitLatencySamplingPercentage_function_004DA9B0.md) (`PAGE` → `.text`)
  - `0x00957895` → [PpmClearExitLatencySamplingPercentage](../../text/4E/PpmClearExitLatencySamplingPercentage_function_004E1538.md) (`PAGE` → `.text`)
  - `0x009578D1` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00957922` → [PopEventCalloutDispatch](../../text/4B/PopEventCalloutDispatch_function_004B4870.md) (`PAGE` → `.text`)
  - `0x009579DE` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (`PAGE` → `.text`)
  - `0x00957A31` → [PopPowerRequestReferenceAcquire](../../text/47/PopPowerRequestReferenceAcquire_function_004776C0.md) (`PAGE` → `.text`)
  - `0x00957A3B` → [PopPowerRequestReferenceRelease](../../text/47/PopPowerRequestReferenceRelease_function_004775B0.md) (`PAGE` → `.text`)
  - `0x00957B03` → [PopCapabilityCheck](../../text/4D/PopCapabilityCheck_function_004DFF10.md) (`PAGE` → `.text`)
  - `0x00957C08` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (`PAGE` → `.text`)
  - `0x00957C37` → [PopFxIsDevicePotentialDripsConstraint](../../text/4A/PopFxIsDevicePotentialDripsConstraint_function_004A5D34.md) (`PAGE` → `.text`)
  - `0x00957C82` → [PopUpdatePowerButtonHoldState](../../text/4D/PopUpdatePowerButtonHoldState_function_004D4EB4.md) (`PAGE` → `.text`)
  - `0x00957CB2` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00957CCE` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x00957E77` → [ExNotifyCallback](../../text/39/ExNotifyCallback_function_003926B0.md) (`PAGE` → `.text`)
  - `0x00957EE6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00957F32` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00955D80  40 53                           push rbx
00955D82  56                              push rsi
00955D83  57                              push rdi
00955D84  41 54                           push r12
00955D86  41 55                           push r13
00955D88  41 56                           push r14
00955D8A  41 57                           push r15
00955D8C  48 81 EC 30 07 00 00            sub rsp, 0x730
00955D93  48 8B 05 A6 49 4B 00            mov rax, qword ptr [rip + 0x4b49a6]
00955D9A  48 33 C4                        xor rax, rsp
00955D9D  48 89 84 24 20 07 00 00         mov qword ptr [rsp + 0x720], rax
00955DA5  49 8B D9                        mov rbx, r9
00955DA8  45 8B F0                        mov r14d, r8d
00955DAB  48 8B F2                        mov rsi, rdx
00955DAE  44 8B E9                        mov r13d, ecx
00955DB1  89 8C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ecx
00955DB8  33 FF                           xor edi, edi
00955DBA  40 88 7C 24 69                  mov byte ptr [rsp + 0x69], dil
00955DBF  33 D2                           xor edx, edx
00955DC1  41 B8 00 06 00 00               mov r8d, 0x600
00955DC7  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00955DCF  E8 6C 0E D7 FF                  call 0x1406c6c40
00955DD4  89 BC 24 90 00 00 00            mov dword ptr [rsp + 0x90], edi
00955DDB  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
00955DE3  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00955DE8  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
00955DEC  44 8B FF                        mov r15d, edi
00955DEF  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00955DF4  48 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdi
00955DFC  40 8A D7                        mov dl, dil
00955DFF  88 54 24 68                     mov byte ptr [rsp + 0x68], dl
00955E03  40 88 7C 24 59                  mov byte ptr [rsp + 0x59], dil
00955E08  89 7C 24 78                     mov dword ptr [rsp + 0x78], edi
00955E0C  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
00955E10  41 83 FD 62                     cmp r13d, 0x62
00955E14  0F 87 88 0E 00 00               ja 0x140956ca2
00955E1A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00955E23  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
00955E29  88 4C 24 58                     mov byte ptr [rsp + 0x58], cl
00955E2D  48 8B C6                        mov rax, rsi
00955E30  48 F7 D8                        neg rax
00955E33  45 1B ED                        sbb r13d, r13d
00955E36  45 23 EE                        and r13d, r14d
00955E39  41 8B C5                        mov eax, r13d
00955E3C  F7 D8                           neg eax
00955E3E  4D 1B F6                        sbb r14, r14
00955E41  4C 23 F6                        and r14, rsi
00955E44  4C 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r14
00955E4C  48 8B C3                        mov rax, rbx
00955E4F  48 F7 D8                        neg rax
00955E52  1B C0                           sbb eax, eax
00955E54  23 84 24 90 07 00 00            and eax, dword ptr [rsp + 0x790]
00955E5B  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00955E5F  F7 D8                           neg eax
00955E61  4D 1B E4                        sbb r12, r12
00955E64  4C 23 E3                        and r12, rbx
00955E67  84 C9                           test cl, cl
00955E69  0F 84 14 03 00 00               je 0x140956183
00955E6F  48 63 B4 24 84 00 00 00         movsxd rsi, dword ptr [rsp + 0x84]
00955E77  83 FE 22                        cmp esi, 0x22
00955E7A  77 10                           ja 0x140955e8c
00955E7C  48 BA C0 00 02 C3 07 00 00 00   movabs rdx, 0x7c30200c0
00955E86  48 0F A3 F2                     bt rdx, rsi
00955E8A  72 18                           jb 0x140955ea4
00955E8C  8D 46 D9                        lea eax, [rsi - 0x27]
00955E8F  83 F8 3A                        cmp eax, 0x3a
00955E92  77 22                           ja 0x140955eb6
00955E94  48 BA 0F E5 C2 71 00 4F 10 04   movabs rdx, 0x4104f0071c2e50f
00955E9E  48 0F A3 C2                     bt rdx, rax
00955EA2  73 12                           jae 0x140955eb6
00955EA4  BB 22 00 00 C0                  mov ebx, 0xc0000022
00955EA9  49 8B F6                        mov rsi, r14
00955EAC  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00955EB1  E9 F1 0D 00 00                  jmp 0x140956ca7
00955EB6  8D 46 DB                        lea eax, [rsi - 0x25]
00955EB9  83 F8 3A                        cmp eax, 0x3a
00955EBC  77 18                           ja 0x140955ed6
00955EBE  48 BA 03 09 94 08 18 80 08 06   movabs rdx, 0x608801808940903
00955EC8  48 0F A3 C2                     bt rdx, rax
00955ECC  73 08                           jae 0x140955ed6
00955ECE  41 BF 01 00 00 00               mov r15d, 1
00955ED4  EB 0E                           jmp 0x140955ee4
00955ED6  8D 46 FE                        lea eax, [rsi - 2]
00955ED9  41 BF 01 00 00 00               mov r15d, 1
00955EDF  41 3B C7                        cmp eax, r15d
00955EE2  77 7E                           ja 0x140955f62
00955EE4  48 8D 54 24 69                  lea rdx, [rsp + 0x69]
00955EE9  33 C9                           xor ecx, ecx
00955EEB  E8 84 BB 0C 00                  call 0x140a21a74
00955EF0  8B D8                           mov ebx, eax
00955EF2  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
00955EF6  85 C0                           test eax, eax
00955EF8  78 5B                           js 0x140955f55
00955EFA  40 38 7C 24 69                  cmp byte ptr [rsp + 0x69], dil
00955EFF  74 67                           je 0x140955f68
00955F01  83 FE 49                        cmp esi, 0x49
00955F04  74 05                           je 0x140955f0b
00955F06  83 FE 58                        cmp esi, 0x58
00955F09  75 2D                           jne 0x140955f38
00955F0B  48 8D 0D FE BC 1A 00            lea rcx, [rip + 0x1abcfe]
00955F12  E8 F9 9F B8 FF                  call 0x1404dff10
00955F17  88 84 24 80 00 00 00            mov byte ptr [rsp + 0x80], al
00955F1E  84 C0                           test al, al
00955F20  75 46                           jne 0x140955f68
00955F22  BB 22 00 00 C0                  mov ebx, 0xc0000022
00955F27  89 5C 24 5C                     mov dword ptr [rsp + 0x5c], ebx
00955F2B  49 8B F6                        mov rsi, r14
00955F2E  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00955F33  E9 6F 0D 00 00                  jmp 0x140956ca7
00955F38  40 38 7C 24 69                  cmp byte ptr [rsp + 0x69], dil
00955F3D  74 29                           je 0x140955f68
00955F3F  BB 22 00 00 C0                  mov ebx, 0xc0000022
00955F44  89 5C 24 5C                     mov dword ptr [rsp + 0x5c], ebx
00955F48  49 8B F6                        mov rsi, r14
00955F4B  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00955F50  E9 52 0D 00 00                  jmp 0x140956ca7
00955F55  49 8B F6                        mov rsi, r14
00955F58  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00955F5D  E9 45 0D 00 00                  jmp 0x140956ca7
00955F62  8B 5C 24 5C                     mov ebx, dword ptr [rsp + 0x5c]
00955F66  EB 04                           jmp 0x140955f6c
00955F68  8A 4C 24 58                     mov cl, byte ptr [rsp + 0x58]
00955F6C  8D 46 A4                        lea eax, [rsi - 0x5c]
00955F6F  41 3B C7                        cmp eax, r15d
00955F72  77 1C                           ja 0x140955f90
00955F74  E8 C3 79 00 00                  call 0x14095d93c
00955F79  8B D8                           mov ebx, eax
00955F7B  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
00955F7F  85 C0                           test eax, eax
00955F81  79 0D                           jns 0x140955f90
00955F83  49 8B F6                        mov rsi, r14
00955F86  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00955F8B  E9 17 0D 00 00                  jmp 0x140956ca7
00955F90  8D 46 E4                        lea eax, [rsi - 0x1c]
00955F93  83 F8 32                        cmp eax, 0x32
00955F96  77 2F                           ja 0x140955fc7
00955F98  48 B9 01 00 42 00 00 00 04 00   movabs rcx, 0x4000000420001
00955FA2  48 0F A3 C1                     bt rcx, rax
00955FA6  73 1F                           jae 0x140955fc7
00955FA8  E8 9B 85 0A 00                  call 0x1409fe548
00955FAD  84 C0                           test al, al
00955FAF  75 16                           jne 0x140955fc7
00955FB1  BB 22 00 00 C0                  mov ebx, 0xc0000022
00955FB6  89 5C 24 5C                     mov dword ptr [rsp + 0x5c], ebx
00955FBA  49 8B F6                        mov rsi, r14
00955FBD  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00955FC2  E9 E0 0C 00 00                  jmp 0x140956ca7
00955FC7  83 FE 47                        cmp esi, 0x47
00955FCA  75 1F                           jne 0x140955feb
00955FCC  E8 C3 25 13 00                  call 0x140a88594
00955FD1  84 C0                           test al, al
00955FD3  75 16                           jne 0x140955feb
00955FD5  BB 22 00 00 C0                  mov ebx, 0xc0000022
00955FDA  89 5C 24 5C                     mov dword ptr [rsp + 0x5c], ebx
00955FDE  49 8B F6                        mov rsi, r14
00955FE1  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00955FE6  E9 BC 0C 00 00                  jmp 0x140956ca7
00955FEB  4D 85 F6                        test r14, r14
00955FEE  0F 84 4E 01 00 00               je 0x140956142
00955FF4  8D 46 F5                        lea eax, [rsi - 0xb]
00955FF7  83 F8 3D                        cmp eax, 0x3d
00955FFA  77 10                           ja 0x14095600c
00955FFC  48 B9 01 00 00 00 09 80 01 20   movabs rcx, 0x2001800900000001
00956006  48 0F A3 C1                     bt rcx, rax
0095600A  72 1F                           jb 0x14095602b
0095600C  E8 CF 02 AE FF                  call 0x1404362e0
00956011  84 C0                           test al, al
00956013  74 16                           je 0x14095602b
00956015  BB BB 00 00 C0                  mov ebx, 0xc00000bb
0095601A  89 5C 24 5C                     mov dword ptr [rsp + 0x5c], ebx
0095601E  49 8B F6                        mov rsi, r14
00956021  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00956026  E9 7C 0C 00 00                  jmp 0x140956ca7
0095602B  83 FE 09                        cmp esi, 9
0095602E  74 18                           je 0x140956048
00956030  8D 46 DA                        lea eax, [rsi - 0x26]
00956033  83 F8 39                        cmp eax, 0x39
00956036  77 2F                           ja 0x140956067
00956038  48 B9 01 24 42 04 00 00 18 02   movabs rcx, 0x218000004422401
00956042  48 0F A3 C1                     bt rcx, rax
00956046  73 1F                           jae 0x140956067
00956048  E8 FB 84 0A 00                  call 0x1409fe548
0095604D  84 C0                           test al, al
0095604F  75 16                           jne 0x140956067
00956051  BB 22 00 00 C0                  mov ebx, 0xc0000022
00956056  89 5C 24 5C                     mov dword ptr [rsp + 0x5c], ebx
0095605A  49 8B F6                        mov rsi, r14
0095605D  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00956062  E9 40 0C 00 00                  jmp 0x140956ca7
00956067  8D 46 FE                        lea eax, [rsi - 2]
0095606A  41 3B C7                        cmp eax, r15d
0095606D  76 5A                           jbe 0x1409560c9
0095606F  8D 46 DB                        lea eax, [rsi - 0x25]
00956072  83 F8 3D                        cmp eax, 0x3d
00956075  77 10                           ja 0x140956087
00956077  48 B9 C3 0B F4 28 5C 00 AE 2F   movabs rcx, 0x2fae005c28f40bc3
00956081  48 0F A3 C1                     bt rcx, rax
00956085  72 42                           jb 0x1409560c9
00956087  83 FE 0B                        cmp esi, 0xb
0095608A  74 3D                           je 0x1409560c9
0095608C  48 8B 0D 9D 3A 68 00            mov rcx, qword ptr [rip + 0x683a9d]
00956093  83 FE 0A                        cmp esi, 0xa
00956096  48 0F 44 0D A2 3C 68 00         cmove rcx, qword ptr [rip + 0x683ca2]
0095609E  48 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rcx
009560A6  8A 54 24 58                     mov dl, byte ptr [rsp + 0x58]
009560AA  E8 71 BD F1 FF                  call 0x140871e20
009560AF  84 C0                           test al, al
009560B1  75 16                           jne 0x1409560c9
009560B3  BB 61 00 00 C0                  mov ebx, 0xc0000061
009560B8  89 5C 24 5C                     mov dword ptr [rsp + 0x5c], ebx
009560BC  49 8B F6                        mov rsi, r14
009560BF  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
009560C4  E9 DE 0B 00 00                  jmp 0x140956ca7
009560C9  45 85 ED                        test r13d, r13d
009560CC  74 20                           je 0x1409560ee
009560CE  41 8B CD                        mov ecx, r13d
009560D1  49 03 CE                        add rcx, r14
009560D4  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
009560DE  48 3B C8                        cmp rcx, rax
009560E1  77 05                           ja 0x1409560e8
009560E3  49 3B CE                        cmp rcx, r14
009560E6  73 06                           jae 0x1409560ee
009560E8  8A 00                           mov al, byte ptr [rax]
009560EA  8B 5C 24 5C                     mov ebx, dword ptr [rsp + 0x5c]
009560EE  41 83 FD 40                     cmp r13d, 0x40
009560F2  77 1D                           ja 0x140956111
009560F4  4C 8D BC 24 E0 06 00 00         lea r15, [rsp + 0x6e0]
009560FC  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
00956101  45 8B C5                        mov r8d, r13d
00956104  49 8B D6                        mov rdx, r14
00956107  49 8B CF                        mov rcx, r15
0095610A  E8 31 07 D7 FF                  call 0x1406c6840
0095610F  EB 36                           jmp 0x140956147
00956111  41 8B D5                        mov edx, r13d
00956114  B9 00 01 00 00                  mov ecx, 0x100
00956119  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
0095611F  E8 CC BF 22 00                  call 0x140b820f0
00956124  4C 8B F8                        mov r15, rax
00956127  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0095612C  48 85 C0                        test rax, rax
0095612F  75 D0                           jne 0x140956101
00956131  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00956136  89 5C 24 5C                     mov dword ptr [rsp + 0x5c], ebx
0095613A  49 8B F6                        mov rsi, r14
0095613D  E9 65 0B 00 00                  jmp 0x140956ca7
00956142  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00956147  4D 85 E4                        test r12, r12
0095614A  74 12                           je 0x14095615e
0095614C  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
00956150  41 B8 01 00 00 00               mov r8d, 1
00956156  49 8B CC                        mov rcx, r12
00956159  E8 62 30 F9 FF                  call 0x1408e91c0
0095615E  B9 01 00 00 00                  mov ecx, 1
00956163  8A 54 24 68                     mov dl, byte ptr [rsp + 0x68]
00956167  EB 32                           jmp 0x14095619b
00956169  8B D8                           mov ebx, eax
0095616B  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
0095616F  48 8B B4 24 A0 00 00 00         mov rsi, qword ptr [rsp + 0xa0]
00956177  33 FF                           xor edi, edi
00956179  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
0095617E  E9 24 0B 00 00                  jmp 0x140956ca7
00956183  4D 8B FE                        mov r15, r14
00956186  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
0095618B  B9 01 00 00 00                  mov ecx, 1
00956190  8B 5C 24 5C                     mov ebx, dword ptr [rsp + 0x5c]
00956194  8B B4 24 84 00 00 00            mov esi, dword ptr [rsp + 0x84]
0095619B  83 FE 1F                        cmp esi, 0x1f
0095619E  77 0A                           ja 0x1409561aa
009561A0  B8 A0 0C 01 F2                  mov eax, 0xf2010ca0
009561A5  0F A3 F0                        bt eax, esi
009561A8  72 28                           jb 0x1409561d2
009561AA  8D 46 DA                        lea eax, [rsi - 0x26]
009561AD  83 F8 3C                        cmp eax, 0x3c
009561B0  77 10                           ja 0x1409561c2
009561B2  49 B8 ED 36 BE F5 BE E3 FF 1F   movabs r8, 0x1fffe3bef5be36ed
009561BC  49 0F A3 C0                     bt r8, rax
009561C0  72 10                           jb 0x1409561d2
009561C2  E8 F9 21 22 00                  call 0x140b783c0
009561C7  B9 01 00 00 00                  mov ecx, 1
009561CC  8A D1                           mov dl, cl
009561CE  88 4C 24 68                     mov byte ptr [rsp + 0x68], cl
009561D2  83 FE 32                        cmp esi, 0x32
009561D5  0F 8F 0D 10 00 00               jg 0x1409571e8
009561DB  0F 84 E4 0F 00 00               je 0x1409571c5
009561E1  83 FE 18                        cmp esi, 0x18
009561E4  0F 8F 00 07 00 00               jg 0x1409568ea
009561EA  0F 84 C7 06 00 00               je 0x1409568b7
009561F0  83 FE 0C                        cmp esi, 0xc
009561F3  0F 8F 36 05 00 00               jg 0x14095672f
009561F9  0F 84 D7 04 00 00               je 0x1409566d6
009561FF  83 FE 06                        cmp esi, 6
00956202  0F 8F 43 03 00 00               jg 0x14095654b
00956208  0F 84 E7 01 00 00               je 0x1409563f5
0095620E  85 F6                           test esi, esi
00956210  0F 84 91 01 00 00               je 0x1409563a7
00956216  83 EE 01                        sub esi, 1
00956219  0F 84 88 01 00 00               je 0x1409563a7
0095621F  83 EE 01                        sub esi, 1
00956222  0F 84 2D 01 00 00               je 0x140956355
00956228  83 EE 01                        sub esi, 1
0095622B  0F 84 24 01 00 00               je 0x140956355
00956231  83 EE 01                        sub esi, 1
00956234  74 42                           je 0x140956278
00956236  83 FE 01                        cmp esi, 1
00956239  0F 85 60 0A 00 00               jne 0x140956c9f
0095623F  4D 85 FF                        test r15, r15
00956242  0F 85 57 0A 00 00               jne 0x140956c9f
00956248  4D 85 E4                        test r12, r12
0095624B  0F 84 4E 0A 00 00               je 0x140956c9f
00956251  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00956259  E8 7A F4 0D 00                  call 0x140a356d8
0095625E  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
00956266  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0095626B  C7 44 24 54 20 00 00 00         mov dword ptr [rsp + 0x54], 0x20
00956273  E9 45 1C 00 00                  jmp 0x140957ebd
00956278  4D 85 FF                        test r15, r15
0095627B  75 0E                           jne 0x14095628b
0095627D  4D 85 E4                        test r12, r12
00956280  0F 84 19 0A 00 00               je 0x140956c9f
00956286  4D 85 FF                        test r15, r15
00956289  74 7A                           je 0x140956305
0095628B  8B 05 7B 6C 5B 00               mov eax, dword ptr [rip + 0x5b6c7b]
00956291  84 C1                           test cl, al
00956293  0F 84 06 0A 00 00               je 0x140956c9f
00956299  41 83 FD 4C                     cmp r13d, 0x4c
0095629D  0F 82 20 01 00 00               jb 0x1409563c3
009562A3  41 0F 10 07                     movups xmm0, xmmword ptr [r15]
009562A7  0F 11 05 12 6C 5B 00            movups xmmword ptr [rip + 0x5b6c12], xmm0
009562AE  41 0F 10 4F 10                  movups xmm1, xmmword ptr [r15 + 0x10]
009562B3  0F 11 0D 16 6C 5B 00            movups xmmword ptr [rip + 0x5b6c16], xmm1
009562BA  41 0F 10 47 20                  movups xmm0, xmmword ptr [r15 + 0x20]
009562BF  0F 11 05 1A 6C 5B 00            movups xmmword ptr [rip + 0x5b6c1a], xmm0
009562C6  41 0F 10 4F 30                  movups xmm1, xmmword ptr [r15 + 0x30]
009562CB  0F 11 0D 1E 6C 5B 00            movups xmmword ptr [rip + 0x5b6c1e], xmm1
009562D2  F2 41 0F 10 47 40               movsd xmm0, qword ptr [r15 + 0x40]
009562D8  F2 0F 11 05 20 6C 5B 00         movsd qword ptr [rip + 0x5b6c20], xmm0
009562E0  41 8B 47 48                     mov eax, dword ptr [r15 + 0x48]
009562E4  89 05 1E 6C 5B 00               mov dword ptr [rip + 0x5b6c1e], eax
009562EA  E8 75 9C FB FF                  call 0x14090ff64
009562EF  8B D8                           mov ebx, eax
009562F1  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
009562F5  49 8B F6                        mov rsi, r14
009562F8  85 C0                           test eax, eax
009562FA  0F 88 A7 09 00 00               js 0x140956ca7
00956300  B9 01 00 00 00                  mov ecx, 1
00956305  8B 05 DD 69 5B 00               mov eax, dword ptr [rip + 0x5b69dd]
0095630B  22 C1                           and al, cl
0095630D  88 05 B6 6B 5B 00               mov byte ptr [rip + 0x5b6bb6], al
00956313  E8 64 EF B4 FF                  call 0x1404a527c
00956318  88 05 B7 6B 5B 00               mov byte ptr [rip + 0x5b6bb7], al
0095631E  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
00956326  48 8D 0D 93 6B 5B 00            lea rcx, [rip + 0x5b6b93]
0095632D  E8 EA B0 FB FF                  call 0x14091141c
00956332  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
0095633A  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0095633F  C7 44 24 54 4C 00 00 00         mov dword ptr [rsp + 0x54], 0x4c
00956347  8B 5C 24 5C                     mov ebx, dword ptr [rsp + 0x5c]
0095634B  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00956350  E9 68 1B 00 00                  jmp 0x140957ebd
00956355  4D 85 FF                        test r15, r15
00956358  0F 84 41 09 00 00               je 0x140956c9f
0095635E  4D 85 E4                        test r12, r12
00956361  0F 84 38 09 00 00               je 0x140956c9f
00956367  41 81 FD E8 00 00 00            cmp r13d, 0xe8
0095636E  72 53                           jb 0x1409563c3
00956370  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
00956378  49 8B CF                        mov rcx, r15
0095637B  E8 0C A7 FB FF                  call 0x140910a8c
00956380  8B D8                           mov ebx, eax
00956382  49 8B F6                        mov rsi, r14
00956385  85 C0                           test eax, eax
00956387  0F 88 1A 09 00 00               js 0x140956ca7
0095638D  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
00956395  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0095639A  C7 44 24 54 E8 00 00 00         mov dword ptr [rsp + 0x54], 0xe8
009563A2  E9 16 1B 00 00                  jmp 0x140957ebd
009563A7  4D 85 FF                        test r15, r15
009563AA  75 0E                           jne 0x1409563ba
009563AC  4D 85 E4                        test r12, r12
009563AF  0F 84 EA 08 00 00               je 0x140956c9f
009563B5  4D 85 FF                        test r15, r15
009563B8  74 32                           je 0x1409563ec
009563BA  41 81 FD E8 00 00 00            cmp r13d, 0xe8
009563C1  73 0D                           jae 0x1409563d0
009563C3  BB 23 00 00 C0                  mov ebx, 0xc0000023
009563C8  49 8B F6                        mov rsi, r14
009563CB  E9 D7 08 00 00                  jmp 0x140956ca7
009563D0  45 8B CD                        mov r9d, r13d
009563D3  4D 8B C7                        mov r8, r15
009563D6  33 D2                           xor edx, edx
009563D8  33 C9                           xor ecx, ecx
009563DA  E8 D1 A3 FB FF                  call 0x1409107b0
009563DF  8B D8                           mov ebx, eax
009563E1  49 8B F6                        mov rsi, r14
009563E4  85 C0                           test eax, eax
009563E6  0F 88 BB 08 00 00               js 0x140956ca7
009563EC  48 8D 05 31 69 5B 00            lea rax, [rip + 0x5b6931]
009563F3  EB A0                           jmp 0x140956395
009563F5  4D 85 FF                        test r15, r15
009563F8  0F 84 A1 08 00 00               je 0x140956c9f
009563FE  4D 85 E4                        test r12, r12
00956401  0F 85 98 08 00 00               jne 0x140956c9f
00956407  41 83 FD 18                     cmp r13d, 0x18
0095640B  72 B6                           jb 0x1409563c3
0095640D  41 8B 17                        mov edx, dword ptr [r15]
00956410  83 FA 07                        cmp edx, 7
00956413  0F 83 86 08 00 00               jae 0x140956c9f
00956419  4C 8D 14 52                     lea r10, [rdx + rdx*2]
0095641D  4C 8D 1D 1C 68 5B 00            lea r11, [rip + 0x5b681c]
00956424  4B 39 7C D3 08                  cmp qword ptr [r11 + r10*8 + 8], rdi
00956429  74 22                           je 0x14095644d
0095642B  83 FA 05                        cmp edx, 5
0095642E  74 1D                           je 0x14095644d
00956430  83 FA 04                        cmp edx, 4
00956433  0F 85 66 08 00 00               jne 0x140956c9f
00956439  4C 8D 05 10 B3 21 00            lea r8, [rip + 0x21b310]
00956440  4C 39 05 61 68 5B 00            cmp qword ptr [rip + 0x5b6861], r8
00956447  0F 85 52 08 00 00               jne 0x140956c9f
0095644D  41 0F 10 07                     movups xmm0, xmmword ptr [r15]
00956451  43 0F 11 04 D3                  movups xmmword ptr [r11 + r10*8], xmm0
00956456  F2 41 0F 10 4F 10               movsd xmm1, qword ptr [r15 + 0x10]
0095645C  F2 43 0F 11 4C D3 10            movsd qword ptr [r11 + r10*8 + 0x10], xmm1
00956463  66 43 89 7C D3 05               mov word ptr [r11 + r10*8 + 5], di
00956469  43 88 7C D3 07                  mov byte ptr [r11 + r10*8 + 7], dil
0095646E  4C 8B C7                        mov r8, rdi
00956471  44 8B CF                        mov r9d, edi
00956474  85 D2                           test edx, edx
00956476  0F 84 84 00 00 00               je 0x140956500
0095647C  83 EA 01                        sub edx, 1
0095647F  74 68                           je 0x1409564e9
00956481  83 EA 01                        sub edx, 1
00956484  74 4C                           je 0x1409564d2
00956486  83 EA 01                        sub edx, 1
00956489  74 2E                           je 0x1409564b9
0095648B  83 EA 01                        sub edx, 1
0095648E  74 20                           je 0x1409564b0
00956490  83 FA 02                        cmp edx, 2
00956493  0F 85 80 00 00 00               jne 0x140956519
00956499  44 8D 4A 02                     lea r9d, [rdx + 2]
0095649D  F7 05 65 6A 5B 00 00 20 00 00   test dword ptr [rip + 0x5b6a65], 0x2000
009564A7  4C 8D 05 23 6A 5B 00            lea r8, [rip + 0x5b6a23]
009564AE  EB 65                           jmp 0x140956515
009564B0  4C 8D 05 10 6A 5B 00            lea r8, [rip + 0x5b6a10]
009564B7  EB 60                           jmp 0x140956519
009564B9  41 B9 05 00 00 00               mov r9d, 5
009564BF  F7 05 43 6A 5B 00 00 20 00 00   test dword ptr [rip + 0x5b6a43], 0x2000
009564C9  4C 8D 05 F6 69 5B 00            lea r8, [rip + 0x5b69f6]
009564D0  EB 43                           jmp 0x140956515
009564D2  41 B9 04 00 00 00               mov r9d, 4
009564D8  8B 05 2E 6A 5B 00               mov eax, dword ptr [rip + 0x5b6a2e]
009564DE  A8 20                           test al, 0x20
009564E0  4C 8D 05 DE 69 5B 00            lea r8, [rip + 0x5b69de]
009564E7  EB 2C                           jmp 0x140956515
009564E9  41 B9 03 00 00 00               mov r9d, 3
009564EF  8B 05 17 6A 5B 00               mov eax, dword ptr [rip + 0x5b6a17]
009564F5  A8 40                           test al, 0x40
009564F7  4C 8D 05 C6 69 5B 00            lea r8, [rip + 0x5b69c6]
009564FE  EB 15                           jmp 0x140956515
00956500  41 B9 02 00 00 00               mov r9d, 2
00956506  8B 05 00 6A 5B 00               mov eax, dword ptr [rip + 0x5b6a00]
0095650C  A8 08                           test al, 8
0095650E  4C 8D 05 AE 69 5B 00            lea r8, [rip + 0x5b69ae]
00956515  4C 0F 45 C7                     cmovne r8, rdi
00956519  43 8A 44 D3 04                  mov al, byte ptr [r11 + r10*8 + 4]
0095651E  F6 D8                           neg al
00956520  1B D2                           sbb edx, edx
00956522  41 23 D1                        and edx, r9d
00956525  3B 15 D5 69 5B 00               cmp edx, dword ptr [rip + 0x5b69d5]
0095652B  7E 06                           jle 0x140956533
0095652D  89 15 CD 69 5B 00               mov dword ptr [rip + 0x5b69cd], edx
00956533  4D 85 C0                        test r8, r8
00956536  0F 84 81 19 00 00               je 0x140957ebd
0095653C  8A D1                           mov dl, cl
0095653E  49 8B C8                        mov rcx, r8
00956541  E8 02 9A FB FF                  call 0x14090ff48
00956546  E9 72 19 00 00                  jmp 0x140957ebd
0095654B  83 EE 07                        sub esi, 7
0095654E  0F 84 57 01 00 00               je 0x1409566ab
00956554  83 EE 01                        sub esi, 1
00956557  0F 84 30 01 00 00               je 0x14095668d
0095655D  83 EE 01                        sub esi, 1
00956560  0F 84 CD 00 00 00               je 0x140956633
00956566  83 EE 01                        sub esi, 1
00956569  74 63                           je 0x1409565ce
0095656B  83 FE 01                        cmp esi, 1
0095656E  0F 85 2B 07 00 00               jne 0x140956c9f
00956574  4D 85 FF                        test r15, r15
00956577  0F 85 22 07 00 00               jne 0x140956c9f
0095657D  4D 85 E4                        test r12, r12
00956580  0F 84 19 07 00 00               je 0x140956c9f
00956586  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0095658F  E8 20 9E B3 FF                  call 0x1404903b4
00956594  4C 8D 4C 24 54                  lea r9, [rsp + 0x54]
00956599  44 0F B7 C0                     movzx r8d, ax
0095659D  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
009565A5  E8 F6 B6 0B 00                  call 0x140a11ca0
009565AA  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
009565AF  49 8B F6                        mov rsi, r14
009565B2  8B D8                           mov ebx, eax
009565B4  85 C0                           test eax, eax
009565B6  0F 88 EB 06 00 00               js 0x140956ca7
009565BC  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
009565C4  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009565C9  E9 EF 18 00 00                  jmp 0x140957ebd
009565CE  4D 85 FF                        test r15, r15
009565D1  0F 84 C8 06 00 00               je 0x140956c9f
009565D7  4D 85 E4                        test r12, r12
009565DA  0F 85 BF 06 00 00               jne 0x140956c9f
009565E0  44 3B E9                        cmp r13d, ecx
009565E3  0F 82 DA FD FF FF               jb 0x1409563c3
009565E9  41 8D 74 24 03                  lea esi, [r12 + 3]
009565EE  8B CE                           mov ecx, esi
009565F0  E8 87 38 15 00                  call 0x140aa9e7c
009565F5  E8 C6 1D 22 00                  call 0x140b783c0
009565FA  8B D7                           mov edx, edi
009565FC  41 38 3F                        cmp byte ptr [r15], dil
009565FF  0F 95 C2                        setne dl
00956602  89 15 FC EA 66 00               mov dword ptr [rip + 0x66eafc], edx
00956608  45 33 C0                        xor r8d, r8d
0095660B  33 C9                           xor ecx, ecx
0095660D  E8 DE 83 DA FF                  call 0x1406fe9f0
00956612  45 33 C0                        xor r8d, r8d
00956615  33 D2                           xor edx, edx
00956617  33 C9                           xor ecx, ecx
00956619  E8 92 91 FB FF                  call 0x14090f7b0
0095661E  8B D8                           mov ebx, eax
00956620  E8 EB 1D 22 00                  call 0x140b78410
00956625  8B CE                           mov ecx, esi
00956627  E8 90 74 16 00                  call 0x140abdabc
0095662C  85 DB                           test ebx, ebx
0095662E  E9 81 18 00 00                  jmp 0x140957eb4
00956633  4D 85 FF                        test r15, r15
00956636  75 0E                           jne 0x140956646
00956638  4D 85 E4                        test r12, r12
0095663B  0F 84 5E 06 00 00               je 0x140956c9f
00956641  4D 85 FF                        test r15, r15
00956644  74 2E                           je 0x140956674
00956646  41 83 FD 18                     cmp r13d, 0x18
0095664A  0F 82 73 FD FF FF               jb 0x1409563c3
00956650  49 8B D7                        mov rdx, r15
00956653  E8 DC B4 17 00                  call 0x140ad1b34
00956658  8B D8                           mov ebx, eax
0095665A  49 8B F6                        mov rsi, r14
0095665D  85 C0                           test eax, eax
0095665F  0F 88 42 06 00 00               js 0x140956ca7
00956665  E8 FA 98 FB FF                  call 0x14090ff64
0095666A  8B D8                           mov ebx, eax
0095666C  85 C0                           test eax, eax
0095666E  0F 88 33 06 00 00               js 0x140956ca7
00956674  48 8D 05 85 66 5B 00            lea rax, [rip + 0x5b6685]
0095667B  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00956680  C7 44 24 54 18 00 00 00         mov dword ptr [rsp + 0x54], 0x18
00956688  E9 30 18 00 00                  jmp 0x140957ebd
0095668D  4D 85 FF                        test r15, r15
00956690  0F 85 09 06 00 00               jne 0x140956c9f
00956696  4D 85 E4                        test r12, r12
00956699  0F 84 00 06 00 00               je 0x140956c9f
0095669F  48 8B 05 C2 67 5B 00            mov rax, qword ptr [rip + 0x5b67c2]
009566A6  E9 EA FC FF FF                  jmp 0x140956395
009566AB  4D 85 FF                        test r15, r15
009566AE  0F 85 EB 05 00 00               jne 0x140956c9f
009566B4  4D 85 E4                        test r12, r12
009566B7  0F 84 E2 05 00 00               je 0x140956c9f
009566BD  48 8D 05 FC A6 1F 00            lea rax, [rip + 0x1fa6fc]
009566C4  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009566C9  C7 44 24 54 18 01 00 00         mov dword ptr [rsp + 0x54], 0x118
009566D1  E9 E7 17 00 00                  jmp 0x140957ebd
009566D6  4D 85 FF                        test r15, r15
009566D9  0F 85 C0 05 00 00               jne 0x140956c9f
009566DF  4D 85 E4                        test r12, r12
009566E2  0F 84 B7 05 00 00               je 0x140956c9f
009566E8  8B 05 76 55 5B 00               mov eax, dword ptr [rip + 0x5b5576]
009566EE  89 84 24 E4 00 00 00            mov dword ptr [rsp + 0xe4], eax
009566F5  8B 0D 71 55 5B 00               mov ecx, dword ptr [rip + 0x5b5571]
009566FB  2B 0D 67 55 5B 00               sub ecx, dword ptr [rip + 0x5b5567]
00956701  89 8C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ecx
00956708  8B 05 3A 11 51 00               mov eax, dword ptr [rip + 0x51113a]
0095670E  88 84 24 EC 00 00 00            mov byte ptr [rsp + 0xec], al
00956715  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
0095671D  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00956722  C7 44 24 54 10 00 00 00         mov dword ptr [rsp + 0x54], 0x10
0095672A  E9 8E 17 00 00                  jmp 0x140957ebd
0095672F  83 FE 12                        cmp esi, 0x12
00956732  0F 8F 01 01 00 00               jg 0x140956839
00956738  0F 84 14 11 00 00               je 0x140957852
0095673E  83 EE 0D                        sub esi, 0xd
00956741  0F 84 0B 11 00 00               je 0x140957852
00956747  83 EE 01                        sub esi, 1
0095674A  0F 84 CE 00 00 00               je 0x14095681e
00956750  83 EE 01                        sub esi, 1
00956753  0F 84 9A 00 00 00               je 0x1409567f3
00956759  83 EE 01                        sub esi, 1
0095675C  74 48                           je 0x1409567a6
0095675E  83 FE 01                        cmp esi, 1
00956761  0F 85 38 05 00 00               jne 0x140956c9f
00956767  4D 85 FF                        test r15, r15
0095676A  0F 84 2F 05 00 00               je 0x140956c9f
00956770  4D 85 E4                        test r12, r12
00956773  0F 85 26 05 00 00               jne 0x140956c9f
00956779  41 83 FD 10                     cmp r13d, 0x10
0095677D  0F 82 40 FC FF FF               jb 0x1409563c3
00956783  4C 39 25 76 5F 5B 00            cmp qword ptr [rip + 0x5b5f76], r12
0095678A  74 09                           je 0x140956795
0095678C  49 39 3F                        cmp qword ptr [r15], rdi
0095678F  0F 85 0A 05 00 00               jne 0x140956c9f
00956795  41 0F 10 07                     movups xmm0, xmmword ptr [r15]
00956799  F3 0F 7F 05 5F 5F 5B 00         movdqu xmmword ptr [rip + 0x5b5f5f], xmm0
009567A1  E9 17 17 00 00                  jmp 0x140957ebd
009567A6  4D 85 FF                        test r15, r15
009567A9  0F 85 F0 04 00 00               jne 0x140956c9f
009567AF  4D 85 E4                        test r12, r12
009567B2  0F 84 E7 04 00 00               je 0x140956c9f
009567B8  44 39 3D 39 B2 4A 00            cmp dword ptr [rip + 0x4ab239], r15d
009567BF  74 07                           je 0x1409567c8
009567C1  09 8C 24 E0 00 00 00            or dword ptr [rsp + 0xe0], ecx
009567C8  83 3D F9 B1 4A 00 00            cmp dword ptr [rip + 0x4ab1f9], 0
009567CF  74 08                           je 0x1409567d9
009567D1  83 8C 24 E0 00 00 00 02         or dword ptr [rsp + 0xe0], 2
009567D9  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
009567E1  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009567E6  C7 44 24 54 04 00 00 00         mov dword ptr [rsp + 0x54], 4
009567EE  E9 CA 16 00 00                  jmp 0x140957ebd
009567F3  4D 85 FF                        test r15, r15
009567F6  0F 85 A3 04 00 00               jne 0x140956c9f
009567FC  4D 85 E4                        test r12, r12
009567FF  0F 84 9A 04 00 00               je 0x140956c9f
00956805  48 8D 05 94 55 5B 00            lea rax, [rip + 0x5b5594]
0095680C  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00956811  C7 44 24 54 08 00 00 00         mov dword ptr [rsp + 0x54], 8
00956819  E9 9F 16 00 00                  jmp 0x140957ebd
0095681E  4D 85 FF                        test r15, r15
00956821  0F 85 78 04 00 00               jne 0x140956c9f
00956827  4D 85 E4                        test r12, r12
0095682A  0F 84 6F 04 00 00               je 0x140956c9f
00956830  48 8D 05 61 55 5B 00            lea rax, [rip + 0x5b5561]
00956837  EB D3                           jmp 0x14095680c
00956839  83 EE 13                        sub esi, 0x13
0095683C  0F 84 10 10 00 00               je 0x140957852
00956842  83 EE 01                        sub esi, 1
00956845  0F 84 07 10 00 00               je 0x140957852
0095684B  83 EE 01                        sub esi, 1
0095684E  0F 84 FE 0F 00 00               je 0x140957852
00956854  83 EE 01                        sub esi, 1
00956857  0F 84 F5 0F 00 00               je 0x140957852
0095685D  83 FE 01                        cmp esi, 1
00956860  0F 85 39 04 00 00               jne 0x140956c9f
00956866  4D 85 FF                        test r15, r15
00956869  0F 85 30 04 00 00               jne 0x140956c9f
0095686F  4D 85 E4                        test r12, r12
00956872  0F 84 27 04 00 00               je 0x140956c9f
00956878  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
00956880  48 8D 8C 24 98 00 00 00         lea rcx, [rsp + 0x98]
00956888  E8 23 2D 0E 00                  call 0x140a395b0
0095688D  8B D8                           mov ebx, eax
0095688F  49 8B F6                        mov rsi, r14
00956892  85 C0                           test eax, eax
00956894  0F 88 0D 04 00 00               js 0x140956ca7
0095689A  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
009568A2  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009568A7  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
009568AE  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
009568B2  E9 06 16 00 00                  jmp 0x140957ebd
009568B7  4D 85 FF                        test r15, r15
009568BA  0F 84 DF 03 00 00               je 0x140956c9f
009568C0  4D 85 E4                        test r12, r12
009568C3  0F 85 D6 03 00 00               jne 0x140956c9f
009568C9  41 83 FD 08                     cmp r13d, 8
009568CD  0F 82 F0 FA FF FF               jb 0x1409563c3
009568D3  45 33 C9                        xor r9d, r9d
009568D6  45 33 C0                        xor r8d, r8d
009568D9  41 8B 57 04                     mov edx, dword ptr [r15 + 4]
009568DD  41 8B 0F                        mov ecx, dword ptr [r15]
009568E0  E8 F3 99 FB FF                  call 0x1409102d8
009568E5  E9 C6 15 00 00                  jmp 0x140957eb0
009568EA  83 FE 26                        cmp esi, 0x26
009568ED  0F 8F 72 03 00 00               jg 0x140956c65
009568F3  0F 84 38 03 00 00               je 0x140956c31
009568F9  83 FE 20                        cmp esi, 0x20
009568FC  0F 8F AC 01 00 00               jg 0x140956aae
00956902  0F 84 4A 0F 00 00               je 0x140957852
00956908  8B D6                           mov edx, esi
0095690A  83 EA 19                        sub edx, 0x19
0095690D  0F 84 CB 00 00 00               je 0x1409569de
00956913  83 EA 03                        sub edx, 3
00956916  0F 84 A8 00 00 00               je 0x1409569c4
0095691C  83 EA 01                        sub edx, 1
0095691F  74 46                           je 0x140956967
00956921  83 EA 01                        sub edx, 1
00956924  74 09                           je 0x14095692f
00956926  83 FA 01                        cmp edx, 1
00956929  0F 85 70 03 00 00               jne 0x140956c9f
0095692F  4D 85 FF                        test r15, r15
00956932  0F 84 67 03 00 00               je 0x140956c9f
00956938  4D 85 E4                        test r12, r12
0095693B  0F 85 5E 03 00 00               jne 0x140956c9f
00956941  41 83 FD 08                     cmp r13d, 8
00956945  0F 82 78 FA FF FF               jb 0x1409563c3
0095694B  49 8B CF                        mov rcx, r15
0095694E  83 FE 1E                        cmp esi, 0x1e
00956951  75 0A                           jne 0x14095695d
00956953  E8 B4 9E 11 00                  call 0x140a7080c
00956958  E9 60 15 00 00                  jmp 0x140957ebd
0095695D  E8 3E 76 12 00                  call 0x140a7dfa0
00956962  E9 56 15 00 00                  jmp 0x140957ebd
00956967  4D 85 FF                        test r15, r15
0095696A  0F 85 2F 03 00 00               jne 0x140956c9f
00956970  4D 85 E4                        test r12, r12
00956973  0F 84 26 03 00 00               je 0x140956c9f
00956979  C7 44 24 54 04 00 00 00         mov dword ptr [rsp + 0x54], 4
00956981  41 8D 57 04                     lea edx, [r15 + 4]
00956985  B9 00 01 00 00                  mov ecx, 0x100
0095698A  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00956990  E8 5B B7 22 00                  call 0x140b820f0
00956995  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0095699A  48 85 C0                        test rax, rax
0095699D  75 0A                           jne 0x1409569a9
0095699F  BB 9A 00 00 C0                  mov ebx, 0xc000009a
009569A4  E9 1F FA FF FF                  jmp 0x1409563c8
009569A9  B9 01 00 00 00                  mov ecx, 1
009569AE  88 4C 24 59                     mov byte ptr [rsp + 0x59], cl
009569B2  8B 0D 98 10 51 00               mov ecx, dword ptr [rip + 0x511098]
009569B8  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
009569BD  89 08                           mov dword ptr [rax], ecx
009569BF  E9 F9 14 00 00                  jmp 0x140957ebd
009569C4  E8 E3 A6 13 00                  call 0x140a910ac
009569C9  B9 01 00 00 00                  mov ecx, 1
009569CE  88 0D 81 10 51 00               mov byte ptr [rip + 0x511081], cl
009569D4  E8 E7 F9 B7 FF                  call 0x1404d63c0
009569D9  E9 E6 0A 00 00                  jmp 0x1409574c4
009569DE  4D 85 FF                        test r15, r15
009569E1  0F 84 B8 02 00 00               je 0x140956c9f
009569E7  4D 85 E4                        test r12, r12
009569EA  0F 85 AF 02 00 00               jne 0x140956c9f
009569F0  39 7C 24 50                     cmp dword ptr [rsp + 0x50], edi
009569F4  0F 85 A5 02 00 00               jne 0x140956c9f
009569FA  41 83 FD 1C                     cmp r13d, 0x1c
009569FE  0F 82 9B 02 00 00               jb 0x140956c9f
00956A04  49 8D 47 18                     lea rax, [r15 + 0x18]
00956A08  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00956A10  8B 00                           mov eax, dword ptr [rax]
00956A12  85 C0                           test eax, eax
00956A14  0F 84 85 02 00 00               je 0x140956c9f
00956A1A  49 8D 57 14                     lea rdx, [r15 + 0x14]
00956A1E  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
00956A23  83 3A 02                        cmp dword ptr [rdx], 2
00956A26  0F 87 73 02 00 00               ja 0x140956c9f
00956A2C  49 8B F6                        mov rsi, r14
00956A2F  41 39 0F                        cmp dword ptr [r15], ecx
00956A32  74 0A                           je 0x140956a3e
00956A34  BB 58 00 00 C0                  mov ebx, 0xc0000058
00956A39  E9 69 02 00 00                  jmp 0x140956ca7
00956A3E  83 C0 1C                        add eax, 0x1c
00956A41  83 C9 FF                        or ecx, 0xffffffff
00956A44  83 F8 1C                        cmp eax, 0x1c
00956A47  0F 43 C8                        cmovae ecx, eax
00956A4A  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
00956A4E  1B DB                           sbb ebx, ebx
00956A50  81 E3 95 00 00 C0               and ebx, 0xc0000095
00956A56  83 F8 1C                        cmp eax, 0x1c
00956A59  0F 82 48 02 00 00               jb 0x140956ca7
00956A5F  44 3B E9                        cmp r13d, ecx
00956A62  0F 82 37 02 00 00               jb 0x140956c9f
00956A68  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00956A71  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00956A78  E8 73 8E 8D FF                  call 0x14022f8f0
00956A7D  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00956A82  49 8D 57 1C                     lea rdx, [r15 + 0x1c]
00956A86  49 8D 4F 04                     lea rcx, [r15 + 4]
00956A8A  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00956A8F  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
00956A97  45 8B 09                        mov r9d, dword ptr [r9]
00956A9A  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
00956A9F  45 8B 00                        mov r8d, dword ptr [r8]
00956AA2  8B D0                           mov edx, eax
00956AA4  E8 AB E3 FB FF                  call 0x140914e54
00956AA9  E9 02 14 00 00                  jmp 0x140957eb0
00956AAE  83 EE 21                        sub esi, 0x21
00956AB1  0F 84 9B 0D 00 00               je 0x140957852
00956AB7  83 EE 01                        sub esi, 1
00956ABA  0F 84 92 0D 00 00               je 0x140957852
00956AC0  83 EE 01                        sub esi, 1
00956AC3  0F 84 F0 00 00 00               je 0x140956bb9
00956AC9  83 EE 01                        sub esi, 1
00956ACC  74 6A                           je 0x140956b38
00956ACE  83 FE 01                        cmp esi, 1
00956AD1  0F 85 C8 01 00 00               jne 0x140956c9f
00956AD7  4D 85 FF                        test r15, r15
00956ADA  0F 84 BF 01 00 00               je 0x140956c9f
00956AE0  4D 85 E4                        test r12, r12
00956AE3  0F 85 B6 01 00 00               jne 0x140956c9f
00956AE9  38 4C 24 58                     cmp byte ptr [rsp + 0x58], cl
00956AED  74 0A                           je 0x140956af9
00956AEF  BB 22 00 00 C0                  mov ebx, 0xc0000022
00956AF4  E9 CF F8 FF FF                  jmp 0x1409563c8
00956AF9  41 83 FD 04                     cmp r13d, 4
00956AFD  73 07                           jae 0x140956b06
00956AFF  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00956B04  EB 1A                           jmp 0x140956b20
00956B06  41 83 C5 FC                     add r13d, -4
00956B0A  41 8B D5                        mov edx, r13d
00956B0D  49 8D 4F 04                     lea rcx, [r15 + 4]
00956B11  45 33 C0                        xor r8d, r8d
00956B14  E8 D3 0A B0 FF                  call 0x1404575ec
00956B19  8B D8                           mov ebx, eax
00956B1B  85 C0                           test eax, eax
00956B1D  0F 49 DF                        cmovns ebx, edi
00956B20  49 8B F6                        mov rsi, r14
00956B23  85 DB                           test ebx, ebx
00956B25  0F 88 7C 01 00 00               js 0x140956ca7
00956B2B  49 8B CF                        mov rcx, r15
00956B2E  E8 7D 50 12 00                  call 0x140a7bbb0
00956B33  E9 85 13 00 00                  jmp 0x140957ebd
00956B38  4D 85 E4                        test r12, r12
00956B3B  0F 84 5E 01 00 00               je 0x140956c9f
00956B41  8B 0D F9 53 5B 00               mov ecx, dword ptr [rip + 0x5b53f9]
00956B47  85 C9                           test ecx, ecx
00956B49  74 64                           je 0x140956baf
00956B4B  48 83 3D E5 53 5B 00 00         cmp qword ptr [rip + 0x5b53e5], 0
00956B53  74 5A                           je 0x140956baf
00956B55  8D 41 08                        lea eax, [rcx + 8]
00956B58  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00956B5C  8B D0                           mov edx, eax
00956B5E  B9 00 01 00 00                  mov ecx, 0x100
00956B63  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00956B69  E8 82 B5 22 00                  call 0x140b820f0
00956B6E  48 8B F0                        mov rsi, rax
00956B71  48 85 C0                        test rax, rax
00956B74  0F 84 25 FE FF FF               je 0x14095699f
00956B7A  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00956B7F  B9 01 00 00 00                  mov ecx, 1
00956B84  88 4C 24 59                     mov byte ptr [rsp + 0x59], cl
00956B88  44 8B 05 B1 53 5B 00            mov r8d, dword ptr [rip + 0x5b53b1]
00956B8F  48 8D 48 08                     lea rcx, [rax + 8]
00956B93  48 8B 15 9E 53 5B 00            mov rdx, qword ptr [rip + 0x5b539e]
00956B9A  E8 A1 FC D6 FF                  call 0x1406c6840
00956B9F  8B 05 9B 53 5B 00               mov eax, dword ptr [rip + 0x5b539b]
00956BA5  C1 E8 04                        shr eax, 4
00956BA8  89 06                           mov dword ptr [rsi], eax
00956BAA  E9 0E 13 00 00                  jmp 0x140957ebd
00956BAF  BB 25 02 00 C0                  mov ebx, 0xc0000225
00956BB4  E9 0F F8 FF FF                  jmp 0x1409563c8
00956BB9  4D 85 FF                        test r15, r15
00956BBC  0F 85 DD 00 00 00               jne 0x140956c9f
00956BC2  4D 85 E4                        test r12, r12
00956BC5  0F 84 D4 00 00 00               je 0x140956c9f
00956BCB  84 D2                           test dl, dl
00956BCD  74 0A                           je 0x140956bd9
00956BCF  E8 3C 18 22 00                  call 0x140b78410
00956BD4  40 88 7C 24 68                  mov byte ptr [rsp + 0x68], dil
00956BD9  48 8D 54 24 54                  lea rdx, [rsp + 0x54]
00956BDE  33 C9                           xor ecx, ecx
00956BE0  E8 83 6F 16 00                  call 0x140abdb68
00956BE5  8B D8                           mov ebx, eax
00956BE7  3D 23 00 00 C0                  cmp eax, 0xc0000023
00956BEC  0F 85 3A FA FF FF               jne 0x14095662c
00956BF2  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
00956BF6  B9 40 00 00 00                  mov ecx, 0x40
00956BFB  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00956C01  E8 EA B4 22 00                  call 0x140b820f0
00956C06  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00956C0B  48 85 C0                        test rax, rax
00956C0E  0F 84 8B FD FF FF               je 0x14095699f
00956C14  B9 01 00 00 00                  mov ecx, 1
00956C19  88 4C 24 59                     mov byte ptr [rsp + 0x59], cl
00956C1D  48 8D 54 24 54                  lea rdx, [rsp + 0x54]
00956C22  48 8B C8                        mov rcx, rax
00956C25  E8 3E 6F 16 00                  call 0x140abdb68
00956C2A  8B D8                           mov ebx, eax
00956C2C  E9 FB F9 FF FF                  jmp 0x14095662c
00956C31  4D 85 FF                        test r15, r15
00956C34  74 69                           je 0x140956c9f
00956C36  4D 85 E4                        test r12, r12
00956C39  75 64                           jne 0x140956c9f
00956C3B  41 83 FD 08                     cmp r13d, 8
00956C3F  75 0A                           jne 0x140956c4b
00956C41  49 8B CF                        mov rcx, r15
00956C44  E8 C7 6A 17 00                  call 0x140acd710
00956C49  EB DF                           jmp 0x140956c2a
00956C4B  41 83 FD 04                     cmp r13d, 4
00956C4F  75 0A                           jne 0x140956c5b
00956C51  49 8B CF                        mov rcx, r15
00956C54  E8 DF 7C 17 00                  call 0x140ace938
00956C59  EB CF                           jmp 0x140956c2a
00956C5B  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00956C60  E9 C7 F9 FF FF                  jmp 0x14095662c
00956C65  83 FE 2C                        cmp esi, 0x2c
00956C68  0F 8F 23 04 00 00               jg 0x140957091
00956C6E  0F 84 F4 03 00 00               je 0x140957068
00956C74  8B D6                           mov edx, esi
00956C76  83 EA 27                        sub edx, 0x27
00956C79  0F 84 BE 03 00 00               je 0x14095703d
00956C7F  83 EA 01                        sub edx, 1
00956C82  0F 84 74 03 00 00               je 0x140956ffc
00956C88  83 EA 01                        sub edx, 1
00956C8B  0F 84 B5 01 00 00               je 0x140956e46
00956C91  83 EA 01                        sub edx, 1
00956C94  74 73                           je 0x140956d09
00956C96  83 FA 01                        cmp edx, 1
00956C99  0F 84 DA 0A 00 00               je 0x140957779
00956C9F  49 8B F6                        mov rsi, r14
00956CA2  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00956CA7  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00956CAF  48 85 C9                        test rcx, rcx
00956CB2  74 07                           je 0x140956cbb
00956CB4  33 D2                           xor edx, edx
00956CB6  E8 B5 BB 22 00                  call 0x140b82870
00956CBB  40 38 7C 24 59                  cmp byte ptr [rsp + 0x59], dil
00956CC0  74 0F                           je 0x140956cd1
00956CC2  BA 4D 65 6D 20                  mov edx, 0x206d654d
00956CC7  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00956CCC  E8 9F BB 22 00                  call 0x140b82870
00956CD1  40 38 7C 24 68                  cmp byte ptr [rsp + 0x68], dil
00956CD6  74 05                           je 0x140956cdd
00956CD8  E8 33 17 22 00                  call 0x140b78410
00956CDD  4D 85 FF                        test r15, r15
00956CE0  74 1F                           je 0x140956d01
00956CE2  4C 3B FE                        cmp r15, rsi
00956CE5  74 1A                           je 0x140956d01
00956CE7  48 8D 84 24 E0 06 00 00         lea rax, [rsp + 0x6e0]
00956CEF  4C 3B F8                        cmp r15, rax
00956CF2  74 0D                           je 0x140956d01
00956CF4  BA 4D 65 6D 20                  mov edx, 0x206d654d
00956CF9  49 8B CF                        mov rcx, r15
00956CFC  E8 6F BB 22 00                  call 0x140b82870
00956D01  8B C3                           mov eax, ebx
00956D03  E9 1F 12 00 00                  jmp 0x140957f27
00956D08  CC                              int3
00956D09  4D 85 FF                        test r15, r15
00956D0C  74 91                           je 0x140956c9f
00956D0E  41 83 FD 10                     cmp r13d, 0x10
00956D12  75 8B                           jne 0x140956c9f
00956D14  4D 85 E4                        test r12, r12
00956D17  75 86                           jne 0x140956c9f
00956D19  41 38 7F 0D                     cmp byte ptr [r15 + 0xd], dil
00956D1D  0F 84 C8 00 00 00               je 0x140956deb
00956D23  41 38 7F 0C                     cmp byte ptr [r15 + 0xc], dil
00956D27  0F 84 BE 00 00 00               je 0x140956deb
00956D2D  E8 0E 52 B4 FF                  call 0x14049bf40
00956D32  84 C0                           test al, al
00956D34  74 7F                           je 0x140956db5
00956D36  44 39 25 13 0D 51 00            cmp dword ptr [rip + 0x510d13], r12d
00956D3D  75 76                           jne 0x140956db5
00956D3F  41 83 7F 04 02                  cmp dword ptr [r15 + 4], 2
00956D44  75 76                           jne 0x140956dbc
00956D46  41 8B 07                        mov eax, dword ptr [r15]
00956D49  4D 63 4F 08                     movsxd r9, dword ptr [r15 + 8]
00956D4D  48 89 BC 24 C4 00 00 00         mov qword ptr [rsp + 0xc4], rdi
00956D55  89 BC 24 CC 00 00 00            mov dword ptr [rsp + 0xcc], edi
00956D5C  89 8C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ecx
00956D63  C7 84 24 AC 00 00 00 28 00 00 00  mov dword ptr [rsp + 0xac], 0x28
00956D6E  48 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdi
00956D76  48 89 BC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdi
00956D7E  89 BC 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], edi
00956D85  48 8D 8C 24 A8 00 00 00         lea rcx, [rsp + 0xa8]
00956D8D  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00956D92  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00956D97  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00956D9C  BA A0 00 00 00                  mov edx, 0xa0
00956DA1  41 B8 01 08 00 00               mov r8d, 0x801
00956DA7  48 8D 0D 92 AE 1A 00            lea rcx, [rip + 0x1aae92]
00956DAE  E8 5D B1 16 00                  call 0x140ac1f10
00956DB3  8B D8                           mov ebx, eax
00956DB5  41 83 7F 04 02                  cmp dword ptr [r15 + 4], 2
00956DBA  74 0D                           je 0x140956dc9
00956DBC  41 8B 57 08                     mov edx, dword ptr [r15 + 8]
00956DC0  41 8A 4F 0F                     mov cl, byte ptr [r15 + 0xf]
00956DC4  E8 B7 D5 FB FF                  call 0x140914380
00956DC9  41 8B 4F 04                     mov ecx, dword ptr [r15 + 4]
00956DCD  E8 0E BC FB FF                  call 0x1409129e0
00956DD2  41 8B 4F 04                     mov ecx, dword ptr [r15 + 4]
00956DD6  E8 BD A4 0D 00                  call 0x140a31298
00956DDB  B9 01 00 00 00                  mov ecx, 1
00956DE0  41 39 4F 04                     cmp dword ptr [r15 + 4], ecx
00956DE4  75 05                           jne 0x140956deb
00956DE6  E8 D9 95 DA FF                  call 0x1407003c4
00956DEB  41 38 7F 0E                     cmp byte ptr [r15 + 0xe], dil
00956DEF  0F 84 C8 10 00 00               je 0x140957ebd
00956DF5  41 38 7F 0C                     cmp byte ptr [r15 + 0xc], dil
00956DF9  74 24                           je 0x140956e1f
00956DFB  49 8D 57 04                     lea rdx, [r15 + 4]
00956DFF  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
00956E03  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
00956E07  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00956E0C  45 33 C9                        xor r9d, r9d
00956E0F  45 8D 41 04                     lea r8d, [r9 + 4]
00956E13  48 8D 0D CE 9C 6C FF            lea rcx, [rip - 0x936332]
00956E1A  E8 F1 9E D5 FF                  call 0x1406b0d10
00956E1F  41 38 7F 0E                     cmp byte ptr [r15 + 0xe], dil
00956E23  0F 84 94 10 00 00               je 0x140957ebd
00956E29  45 0F B6 47 0C                  movzx r8d, byte ptr [r15 + 0xc]
00956E2E  41 39 7F 04                     cmp dword ptr [r15 + 4], edi
00956E32  0F 94 C1                        sete cl
00956E35  45 8B 4F 08                     mov r9d, dword ptr [r15 + 8]
00956E39  41 8B 17                        mov edx, dword ptr [r15]
00956E3C  E8 BF 0D B6 FF                  call 0x1404b7c00
00956E41  E9 77 10 00 00                  jmp 0x140957ebd
00956E46  4D 85 FF                        test r15, r15
00956E49  0F 85 50 FE FF FF               jne 0x140956c9f
00956E4F  4D 85 E4                        test r12, r12
00956E52  0F 84 47 FE FF FF               je 0x140956c9f
00956E58  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
00956E5D  41 83 FD 40                     cmp r13d, 0x40
00956E61  0F 85 38 FE FF FF               jne 0x140956c9f
00956E67  48 8D 0D D2 15 5B 00            lea rcx, [rip + 0x5b15d2]
00956E6E  E8 D1 9C AD FF                  call 0x140430b44
00956E73  48 8B 1D AE 0B 51 00            mov rbx, qword ptr [rip + 0x510bae]
00956E7A  48 8D 0D BF 15 5B 00            lea rcx, [rip + 0x5b15bf]
00956E81  E8 36 8D 98 FF                  call 0x1402dfbbc
00956E86  0F B6 84 24 10 01 00 00         movzx eax, byte ptr [rsp + 0x110]
00956E8E  41 8D 4F 01                     lea ecx, [r15 + 1]
00956E92  3B D9                           cmp ebx, ecx
00956E94  0F 44 C1                        cmove eax, ecx
00956E97  88 84 24 10 01 00 00            mov byte ptr [rsp + 0x110], al
00956E9E  E8 35 D5 FB FF                  call 0x1409143d8
00956EA3  88 84 24 18 01 00 00            mov byte ptr [rsp + 0x118], al
00956EAA  E8 29 D5 FB FF                  call 0x1409143d8
00956EAF  84 C0                           test al, al
00956EB1  74 1B                           je 0x140956ece
00956EB3  E8 60 3B 03 00                  call 0x14098aa18
00956EB8  8B D8                           mov ebx, eax
00956EBA  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
00956EBE  49 8B F6                        mov rsi, r14
00956EC1  85 C0                           test eax, eax
00956EC3  0F 88 DE FD FF FF               js 0x140956ca7
00956EC9  E8 3A A7 17 00                  call 0x140ad1608
00956ECE  E8 ED 14 22 00                  call 0x140b783c0
00956ED3  89 BC 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], edi
00956EDA  48 8D 05 13 58 5B 00            lea rax, [rip + 0x5b5813]
00956EE1  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
00956EE9  48 8D 05 65 0B 51 00            lea rax, [rip + 0x510b65]
00956EF0  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
00956EF8  8B CF                           mov ecx, edi
00956EFA  40 38 3D 10 5F 5B 00            cmp byte ptr [rip + 0x5b5f10], dil
00956F01  0F 95 C1                        setne cl
00956F04  89 8C 24 F8 00 00 00            mov dword ptr [rsp + 0xf8], ecx
00956F0B  8B 05 FB 5E 5B 00               mov eax, dword ptr [rip + 0x5b5efb]
00956F11  89 84 24 FC 00 00 00            mov dword ptr [rsp + 0xfc], eax
00956F18  8B 05 0E 5F 5B 00               mov eax, dword ptr [rip + 0x5b5f0e]
00956F1E  89 84 24 F4 00 00 00            mov dword ptr [rsp + 0xf4], eax
00956F25  8B 05 05 5F 5B 00               mov eax, dword ptr [rip + 0x5b5f05]
00956F2B  89 84 24 00 01 00 00            mov dword ptr [rsp + 0x100], eax
00956F32  8B 05 FC 5E 5B 00               mov eax, dword ptr [rip + 0x5b5efc]
00956F38  89 84 24 04 01 00 00            mov dword ptr [rsp + 0x104], eax
00956F3F  8B 05 F3 5E 5B 00               mov eax, dword ptr [rip + 0x5b5ef3]
00956F45  89 84 24 08 01 00 00            mov dword ptr [rsp + 0x108], eax
00956F4C  8B 05 EA 5E 5B 00               mov eax, dword ptr [rip + 0x5b5eea]
00956F52  89 84 24 14 01 00 00            mov dword ptr [rsp + 0x114], eax
00956F59  8B 05 E1 5E 5B 00               mov eax, dword ptr [rip + 0x5b5ee1]
00956F5F  89 84 24 0C 01 00 00            mov dword ptr [rsp + 0x10c], eax
00956F66  8A 05 0D 46 4B 00               mov al, byte ptr [rip + 0x4b460d]
00956F6C  88 84 24 11 01 00 00            mov byte ptr [rsp + 0x111], al
00956F73  0F 0D 0D F6 45 4B 00            prefetchw byte ptr [rip + 0x4b45f6]
00956F7A  8B 05 F0 45 4B 00               mov eax, dword ptr [rip + 0x4b45f0]
00956F80  8B C8                           mov ecx, eax
00956F82  0B CF                           or ecx, edi
00956F84  F0 0F B1 0D E4 45 4B 00         lock cmpxchg dword ptr [rip + 0x4b45e4], ecx
00956F8C  75 F2                           jne 0x140956f80
00956F8E  85 C0                           test eax, eax
00956F90  0F 95 84 24 19 01 00 00         setne byte ptr [rsp + 0x119]
00956F98  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
00956FA0  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00956FA5  C7 44 24 54 40 00 00 00         mov dword ptr [rsp + 0x54], 0x40
00956FAD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00956FB6  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00956FBD  E8 2E 89 8D FF                  call 0x14022f8f0
00956FC2  8B D8                           mov ebx, eax
00956FC4  44 8B C0                        mov r8d, eax
00956FC7  48 8D 15 42 C1 1A 00            lea rdx, [rip + 0x1ac142]
00956FCE  B9 03 00 00 00                  mov ecx, 3
00956FD3  E8 4C 7F B3 FF                  call 0x14048ef24
00956FD8  45 33 C0                        xor r8d, r8d
00956FDB  8B D3                           mov edx, ebx
00956FDD  48 8D 0D 14 AA 6B FF            lea rcx, [rip - 0x9455ec]
00956FE4  E8 73 BC FB FF                  call 0x140912c5c
00956FE9  E8 22 14 22 00                  call 0x140b78410
00956FEE  8B 5C 24 5C                     mov ebx, dword ptr [rsp + 0x5c]
00956FF2  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00956FF7  E9 C6 0E 00 00                  jmp 0x140957ec2
00956FFC  4D 85 FF                        test r15, r15
00956FFF  0F 84 9A FC FF FF               je 0x140956c9f
00957005  41 83 FD 04                     cmp r13d, 4
00957009  0F 85 90 FC FF FF               jne 0x140956c9f
0095700F  4D 85 E4                        test r12, r12
00957012  0F 85 87 FC FF FF               jne 0x140956c9f
00957018  8B C7                           mov eax, edi
0095701A  41 39 3F                        cmp dword ptr [r15], edi
0095701D  0F 95 C0                        setne al
00957020  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
00957024  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00957029  41 8B D5                        mov edx, r13d
0095702C  48 8D 0D 05 53 6C FF            lea rcx, [rip - 0x93acfb]
00957033  E8 34 DD FB FF                  call 0x140914d6c
00957038  E9 80 0E 00 00                  jmp 0x140957ebd
0095703D  4D 85 FF                        test r15, r15
00957040  0F 84 59 FC FF FF               je 0x140956c9f
00957046  4D 85 E4                        test r12, r12
00957049  0F 85 50 FC FF FF               jne 0x140956c9f
0095704F  41 83 FD 18                     cmp r13d, 0x18
00957053  0F 85 46 FC FF FF               jne 0x140956c9f
00957059  49 8B CF                        mov rcx, r15
0095705C  E8 63 24 B8 FF                  call 0x1404d94c4
00957061  8B D8                           mov ebx, eax
00957063  E9 55 0E 00 00                  jmp 0x140957ebd
00957068  4D 85 FF                        test r15, r15
0095706B  0F 84 2E FC FF FF               je 0x140956c9f
00957071  4D 85 E4                        test r12, r12
00957074  0F 85 25 FC FF FF               jne 0x140956c9f
0095707A  41 83 FD 18                     cmp r13d, 0x18
0095707E  0F 85 3F F3 FF FF               jne 0x1409563c3
00957084  49 8B CF                        mov rcx, r15
00957087  E8 DC A8 0C 00                  call 0x140a21968
0095708C  E9 1F 0E 00 00                  jmp 0x140957eb0
00957091  83 EE 2D                        sub esi, 0x2d
00957094  0F 84 EF 00 00 00               je 0x140957189
0095709A  83 EE 01                        sub esi, 1
0095709D  0F 84 9D 00 00 00               je 0x140957140
009570A3  83 EE 01                        sub esi, 1
009570A6  74 60                           je 0x140957108
009570A8  83 EE 01                        sub esi, 1
009570AB  0F 85 98 07 00 00               jne 0x140957849
009570B1  40 38 35 40 05 5F 00            cmp byte ptr [rip + 0x5f0540], sil
009570B8  0F 84 31 FA FF FF               je 0x140956aef
009570BE  4D 85 FF                        test r15, r15
009570C1  0F 84 D8 FB FF FF               je 0x140956c9f
009570C7  4D 85 E4                        test r12, r12
009570CA  0F 85 CF FB FF FF               jne 0x140956c9f
009570D0  41 83 FD 10                     cmp r13d, 0x10
009570D4  75 04                           jne 0x1409570da
009570D6  33 D2                           xor edx, edx
009570D8  EB 0A                           jmp 0x1409570e4
009570DA  41 83 FD 18                     cmp r13d, 0x18
009570DE  75 11                           jne 0x1409570f1
009570E0  49 8D 57 10                     lea rdx, [r15 + 0x10]
009570E4  49 8B CF                        mov rcx, r15
009570E7  E8 18 38 E1 FF                  call 0x14076a904
009570EC  E9 39 FB FF FF                  jmp 0x140956c2a
009570F1  41 83 FD 02                     cmp r13d, 2
009570F5  0F 85 60 FB FF FF               jne 0x140956c5b
009570FB  49 8B CF                        mov rcx, r15
009570FE  E8 1D 3A E1 FF                  call 0x14076ab20
00957103  E9 22 FB FF FF                  jmp 0x140956c2a
00957108  4D 85 FF                        test r15, r15
0095710B  0F 84 8E FB FF FF               je 0x140956c9f
00957111  41 83 FD 10                     cmp r13d, 0x10
00957115  0F 85 84 FB FF FF               jne 0x140956c9f
0095711B  49 8B CF                        mov rcx, r15
0095711E  E8 C5 D7 14 00                  call 0x140aa48e8
00957123  8B D8                           mov ebx, eax
00957125  85 C0                           test eax, eax
00957127  0F 89 90 0D 00 00               jns 0x140957ebd
0095712D  49 8B F6                        mov rsi, r14
00957130  3D 20 01 00 C0                  cmp eax, 0xc0000120
00957135  0F 85 6C FB FF FF               jne 0x140956ca7
0095713B  E9 7D 0D 00 00                  jmp 0x140957ebd
00957140  4D 85 FF                        test r15, r15
00957143  0F 84 56 FB FF FF               je 0x140956c9f
00957149  41 83 FD 02                     cmp r13d, 2
0095714D  0F 82 4C FB FF FF               jb 0x140956c9f
00957153  4D 85 E4                        test r12, r12
00957156  0F 84 43 FB FF FF               je 0x140956c9f
0095715C  41 0F B7 1F                     movzx ebx, word ptr [r15]
00957160  E8 9B 54 B3 FF                  call 0x14048c600
00957165  66 3B D8                        cmp bx, ax
00957168  0F 83 31 FB FF FF               jae 0x140956c9f
0095716E  4C 8D 4C 24 54                  lea r9, [rsp + 0x54]
00957173  44 0F B7 C3                     movzx r8d, bx
00957177  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
0095717F  E8 1C AB 0B 00                  call 0x140a11ca0
00957184  E9 26 F4 FF FF                  jmp 0x1409565af
00957189  4D 85 FF                        test r15, r15
0095718C  0F 85 0D FB FF FF               jne 0x140956c9f
00957192  4D 85 E4                        test r12, r12
00957195  0F 84 04 FB FF FF               je 0x140956c9f
0095719B  48 8D 54 24 54                  lea rdx, [rsp + 0x54]
009571A0  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
009571A5  E8 9E B7 13 00                  call 0x140a92948
009571AA  8B D8                           mov ebx, eax
009571AC  49 8B F6                        mov rsi, r14
009571AF  85 C0                           test eax, eax
009571B1  0F 88 F0 FA FF FF               js 0x140956ca7
009571B7  B9 01 00 00 00                  mov ecx, 1
009571BC  88 4C 24 59                     mov byte ptr [rsp + 0x59], cl
009571C0  E9 F8 0C 00 00                  jmp 0x140957ebd
009571C5  4D 85 FF                        test r15, r15
009571C8  0F 85 D1 FA FF FF               jne 0x140956c9f
009571CE  4D 85 E4                        test r12, r12
009571D1  0F 84 C8 FA FF FF               je 0x140956c9f
009571D7  48 8D 54 24 54                  lea rdx, [rsp + 0x54]
009571DC  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
009571E1  E8 7E 47 B7 FF                  call 0x1404cb964
009571E6  EB C2                           jmp 0x1409571aa
009571E8  83 FE 4B                        cmp esi, 0x4b
009571EB  0F 8F 26 06 00 00               jg 0x140957817
009571F1  0F 84 FD 05 00 00               je 0x1409577f4
009571F7  83 FE 3F                        cmp esi, 0x3f
009571FA  0F 8F 6B 03 00 00               jg 0x14095756b
00957200  0F 84 F5 02 00 00               je 0x1409574fb
00957206  83 FE 39                        cmp esi, 0x39
00957209  0F 8F 4F 01 00 00               jg 0x14095735e
0095720F  0F 84 3D 06 00 00               je 0x140957852
00957215  83 EE 33                        sub esi, 0x33
00957218  0F 84 D2 00 00 00               je 0x1409572f0
0095721E  83 EE 01                        sub esi, 1
00957221  0F 84 2B 06 00 00               je 0x140957852
00957227  83 EE 01                        sub esi, 1
0095722A  0F 84 22 06 00 00               je 0x140957852
00957230  83 EE 01                        sub esi, 1
00957233  0F 84 19 06 00 00               je 0x140957852
00957239  83 EE 01                        sub esi, 1
0095723C  74 69                           je 0x1409572a7
0095723E  83 FE 01                        cmp esi, 1
00957241  0F 85 58 FA FF FF               jne 0x140956c9f
00957247  4D 85 FF                        test r15, r15
0095724A  0F 84 4F FA FF FF               je 0x140956c9f
00957250  4D 85 E4                        test r12, r12
00957253  0F 84 46 FA FF FF               je 0x140956c9f
00957259  41 83 FD 08                     cmp r13d, 8
0095725D  0F 85 60 F1 FF FF               jne 0x1409563c3
00957263  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
00957268  41 83 FD 04                     cmp r13d, 4
0095726C  0F 85 51 F1 FF FF               jne 0x1409563c3
00957272  4C 8D 84 24 E0 00 00 00         lea r8, [rsp + 0xe0]
0095727A  41 8B 57 04                     mov edx, dword ptr [r15 + 4]
0095727E  41 8B 0F                        mov ecx, dword ptr [r15]
00957281  E8 D2 20 B8 FF                  call 0x1404d9358
00957286  8B D8                           mov ebx, eax
00957288  85 C0                           test eax, eax
0095728A  0F 88 38 F1 FF FF               js 0x1409563c8
00957290  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
00957298  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0095729D  44 89 6C 24 54                  mov dword ptr [rsp + 0x54], r13d
009572A2  E9 1B 0C 00 00                  jmp 0x140957ec2
009572A7  80 3D 4A 03 5F 00 00            cmp byte ptr [rip + 0x5f034a], 0
009572AE  0F 84 3B F8 FF FF               je 0x140956aef
009572B4  4D 85 FF                        test r15, r15
009572B7  0F 84 E2 F9 FF FF               je 0x140956c9f
009572BD  4D 85 E4                        test r12, r12
009572C0  0F 85 D9 F9 FF FF               jne 0x140956c9f
009572C6  41 83 FD 08                     cmp r13d, 8
009572CA  75 0D                           jne 0x1409572d9
009572CC  49 8B CF                        mov rcx, r15
009572CF  E8 EC 01 B8 FF                  call 0x1404d74c0
009572D4  E9 51 F9 FF FF                  jmp 0x140956c2a
009572D9  41 83 FD 04                     cmp r13d, 4
009572DD  0F 85 78 F9 FF FF               jne 0x140956c5b
009572E3  49 8B CF                        mov rcx, r15
009572E6  E8 B1 19 B8 FF                  call 0x1404d8c9c
009572EB  E9 3A F9 FF FF                  jmp 0x140956c2a
009572F0  4D 85 FF                        test r15, r15
009572F3  0F 84 A6 F9 FF FF               je 0x140956c9f
009572F9  4D 85 E4                        test r12, r12
009572FC  0F 84 9D F9 FF FF               je 0x140956c9f
00957302  41 83 FD 04                     cmp r13d, 4
00957306  0F 82 B7 F0 FF FF               jb 0x1409563c3
0095730C  B9 05 00 00 00                  mov ecx, 5
00957311  E8 66 2B 15 00                  call 0x140aa9e7c
00957316  E8 A5 10 22 00                  call 0x140b783c0
0095731B  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00957320  48 8D 94 24 88 00 00 00         lea rdx, [rsp + 0x88]
00957328  41 8B 0F                        mov ecx, dword ptr [r15]
0095732B  E8 44 C6 DA FF                  call 0x140703974
00957330  8B D8                           mov ebx, eax
00957332  E8 D9 10 22 00                  call 0x140b78410
00957337  B9 05 00 00 00                  mov ecx, 5
0095733C  E8 7B 67 16 00                  call 0x140abdabc
00957341  85 DB                           test ebx, ebx
00957343  79 0C                           jns 0x140957351
00957345  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00957349  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00957351  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00957359  E9 AE F4 FF FF                  jmp 0x14095680c
0095735E  83 EE 3A                        sub esi, 0x3a
00957361  0F 84 64 01 00 00               je 0x1409574cb
00957367  83 EE 01                        sub esi, 1
0095736A  0F 84 1D 01 00 00               je 0x14095748d
00957370  83 EE 01                        sub esi, 1
00957373  0F 84 EB 00 00 00               je 0x140957464
00957379  83 EE 01                        sub esi, 1
0095737C  0F 84 AD 00 00 00               je 0x14095742f
00957382  83 FE 01                        cmp esi, 1
00957385  0F 85 14 F9 FF FF               jne 0x140956c9f
0095738B  E8 10 EA B9 FF                  call 0x1404f5da0
00957390  85 C0                           test eax, eax
00957392  0F 85 07 F9 FF FF               jne 0x140956c9f
00957398  4D 85 FF                        test r15, r15
0095739B  0F 84 FE F8 FF FF               je 0x140956c9f
009573A1  41 83 FD 28                     cmp r13d, 0x28
009573A5  0F 85 F4 F8 FF FF               jne 0x140956c9f
009573AB  4D 85 E4                        test r12, r12
009573AE  0F 84 EB F8 FF FF               je 0x140956c9f
009573B4  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
009573B9  41 83 FD 10                     cmp r13d, 0x10
009573BD  0F 85 DC F8 FF FF               jne 0x140956c9f
009573C3  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009573CC  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009573D3  E8 18 85 8D FF                  call 0x14022f8f0
009573D8  8B C8                           mov ecx, eax
009573DA  4D 8B C4                        mov r8, r12
009573DD  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
009573E2  E8 05 4A E1 FF                  call 0x14076bdec
009573E7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009573F0  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009573F7  E8 F4 84 8D FF                  call 0x14022f8f0
009573FC  8B D8                           mov ebx, eax
009573FE  E8 9D E9 B9 FF                  call 0x1404f5da0
00957403  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00957408  45 8A 07                        mov r8b, byte ptr [r15]
0095740B  41 8A 57 01                     mov dl, byte ptr [r15 + 1]
0095740F  48 8B 05 82 03 51 00            mov rax, qword ptr [rip + 0x510382]
00957416  48 85 C0                        test rax, rax
00957419  74 0B                           je 0x140957426
0095741B  44 8D 4E 02                     lea r9d, [rsi + 2]
0095741F  8B CB                           mov ecx, ebx
00957421  E8 AA 36 D6 FF                  call 0x1406baad0
00957426  8B 5C 24 5C                     mov ebx, dword ptr [rsp + 0x5c]
0095742A  E9 93 0A 00 00                  jmp 0x140957ec2
0095742F  4D 85 FF                        test r15, r15
00957432  0F 84 67 F8 FF FF               je 0x140956c9f
00957438  41 83 FD 10                     cmp r13d, 0x10
0095743C  0F 85 5D F8 FF FF               jne 0x140956c9f
00957442  4D 85 E4                        test r12, r12
00957445  0F 84 54 F8 FF FF               je 0x140956c9f
0095744B  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
00957450  41 83 FD 08                     cmp r13d, 8
00957454  0F 85 45 F8 FF FF               jne 0x140956c9f
0095745A  BB BB 00 00 C0                  mov ebx, 0xc00000bb
0095745F  E9 5E 0A 00 00                  jmp 0x140957ec2
00957464  4D 85 FF                        test r15, r15
00957467  0F 84 32 F8 FF FF               je 0x140956c9f
0095746D  4D 85 E4                        test r12, r12
00957470  0F 85 29 F8 FF FF               jne 0x140956c9f
00957476  41 83 FD 08                     cmp r13d, 8
0095747A  0F 82 43 EF FF FF               jb 0x1409563c3
00957480  49 8B CF                        mov rcx, r15
00957483  E8 08 C9 16 00                  call 0x140ac3d90
00957488  E9 30 0A 00 00                  jmp 0x140957ebd
0095748D  4D 85 FF                        test r15, r15
00957490  0F 84 09 F8 FF FF               je 0x140956c9f
00957496  4D 85 E4                        test r12, r12
00957499  0F 84 00 F8 FF FF               je 0x140956c9f
0095749F  41 83 FD 10                     cmp r13d, 0x10
009574A3  0F 85 1A EF FF FF               jne 0x1409563c3
009574A9  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
009574AD  83 F8 04                        cmp eax, 4
009574B0  0F 82 0D EF FF FF               jb 0x1409563c3
009574B6  44 8B C0                        mov r8d, eax
009574B9  49 8B D4                        mov rdx, r12
009574BC  49 8B CF                        mov rcx, r15
009574BF  E8 4C BE FB FF                  call 0x140913310
009574C4  8B D8                           mov ebx, eax
009574C6  E9 FD EE FF FF                  jmp 0x1409563c8
009574CB  4D 85 E4                        test r12, r12
009574CE  0F 84 CB F7 FF FF               je 0x140956c9f
009574D4  4D 85 F6                        test r14, r14
009574D7  74 0A                           je 0x1409574e3
009574D9  41 83 FD 14                     cmp r13d, 0x14
009574DD  0F 85 E0 EE FF FF               jne 0x1409563c3
009574E3  83 7C 24 50 08                  cmp dword ptr [rsp + 0x50], 8
009574E8  0F 85 D5 EE FF FF               jne 0x1409563c3
009574EE  49 8B D4                        mov rdx, r12
009574F1  49 8B CF                        mov rcx, r15
009574F4  E8 73 BF FB FF                  call 0x14091346c
009574F9  EB C9                           jmp 0x1409574c4
009574FB  4D 85 FF                        test r15, r15
009574FE  0F 85 9B F7 FF FF               jne 0x140956c9f
00957504  4D 85 E4                        test r12, r12
00957507  0F 85 92 F7 FF FF               jne 0x140956c9f
0095750D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00957516  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0095751D  E8 CE 83 8D FF                  call 0x14022f8f0
00957522  8B D8                           mov ebx, eax
00957524  44 8B C0                        mov r8d, eax
00957527  48 8D 15 22 BC 1A 00            lea rdx, [rip + 0x1abc22]
0095752E  41 8D 4F 03                     lea ecx, [r15 + 3]
00957532  E8 ED 79 B3 FF                  call 0x14048ef24
00957537  45 33 C0                        xor r8d, r8d
0095753A  8B D3                           mov edx, ebx
0095753C  48 8D 0D A5 A4 6B FF            lea rcx, [rip - 0x945b5b]
00957543  E8 14 B7 FB FF                  call 0x140912c5c
00957548  8B CB                           mov ecx, ebx
0095754A  E8 B1 B7 FB FF                  call 0x140912d00
0095754F  E8 84 CE FB FF                  call 0x1409143d8
00957554  84 C0                           test al, al
00957556  0F 84 EB ED FF FF               je 0x140956347
0095755C  E8 CF B5 17 00                  call 0x140ad2b30
00957561  E8 76 DF 16 00                  call 0x140ac54dc
00957566  E9 DC ED FF FF                  jmp 0x140956347
0095756B  83 FE 45                        cmp esi, 0x45
0095756E  0F 8F 9C 01 00 00               jg 0x140957710
00957574  0F 84 6D 01 00 00               je 0x1409576e7
0095757A  83 EE 40                        sub esi, 0x40
0095757D  0F 84 1B 01 00 00               je 0x14095769e
00957583  83 EE 01                        sub esi, 1
00957586  0F 84 B3 00 00 00               je 0x14095763f
0095758C  83 EE 01                        sub esi, 1
0095758F  74 7A                           je 0x14095760b
00957591  83 EE 01                        sub esi, 1
00957594  74 3C                           je 0x1409575d2
00957596  83 FE 01                        cmp esi, 1
00957599  0F 85 00 F7 FF FF               jne 0x140956c9f
0095759F  4D 85 FF                        test r15, r15
009575A2  0F 84 F7 F6 FF FF               je 0x140956c9f
009575A8  41 83 FD 08                     cmp r13d, 8
009575AC  0F 85 ED F6 FF FF               jne 0x140956c9f
009575B2  4D 85 E4                        test r12, r12
009575B5  0F 85 E4 F6 FF FF               jne 0x140956c9f
009575BB  39 7C 24 50                     cmp dword ptr [rsp + 0x50], edi
009575BF  0F 85 DA F6 FF FF               jne 0x140956c9f
009575C5  49 8B CF                        mov rcx, r15
009575C8  E8 43 21 E1 FF                  call 0x140769710
009575CD  E9 F2 FE FF FF                  jmp 0x1409574c4
009575D2  4D 85 FF                        test r15, r15
009575D5  0F 84 C4 F6 FF FF               je 0x140956c9f
009575DB  41 81 FD E0 00 00 00            cmp r13d, 0xe0
009575E2  0F 85 B7 F6 FF FF               jne 0x140956c9f
009575E8  4D 85 E4                        test r12, r12
009575EB  74 0E                           je 0x1409575fb
009575ED  81 7C 24 50 A8 00 00 00         cmp dword ptr [rsp + 0x50], 0xa8
009575F5  0F 85 A4 F6 FF FF               jne 0x140956c9f
009575FB  49 8B D4                        mov rdx, r12
009575FE  49 8B CF                        mov rcx, r15
00957601  E8 F2 11 18 00                  call 0x140ad87f8
00957606  E9 B9 FE FF FF                  jmp 0x1409574c4
0095760B  4D 85 FF                        test r15, r15
0095760E  0F 85 8B F6 FF FF               jne 0x140956c9f
00957614  4D 85 E4                        test r12, r12
00957617  0F 84 82 F6 FF FF               je 0x140956c9f
0095761D  E8 1E 49 B4 FF                  call 0x14049bf40
00957622  88 84 24 E0 00 00 00            mov byte ptr [rsp + 0xe0], al
00957629  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
00957631  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00957636  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
0095763A  E9 7E 08 00 00                  jmp 0x140957ebd
0095763F  E8 9C EC AD FF                  call 0x1404362e0
00957644  84 C0                           test al, al
00957646  74 0A                           je 0x140957652
00957648  BB BB 00 00 C0                  mov ebx, 0xc00000bb
0095764D  E9 76 ED FF FF                  jmp 0x1409563c8
00957652  4D 85 FF                        test r15, r15
00957655  0F 85 44 F6 FF FF               jne 0x140956c9f
0095765B  4D 85 E4                        test r12, r12
0095765E  0F 84 3B F6 FF FF               je 0x140956c9f
00957664  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
0095766C  48 8D 0D 4D 58 5B 00            lea rcx, [rip + 0x5b584d]
00957673  E8 A4 9D FB FF                  call 0x14091141c
00957678  40 38 BC 24 F2 00 00 00         cmp byte ptr [rsp + 0xf2], dil
00957680  74 0D                           je 0x14095768f
00957682  48 8D 8C 24 F2 00 00 00         lea rcx, [rsp + 0xf2]
0095768A  E8 ED DA 13 00                  call 0x140a9517c
0095768F  48 8D 84 24 F2 00 00 00         lea rax, [rsp + 0xf2]
00957697  B9 01 00 00 00                  mov ecx, 1
0095769C  EB 93                           jmp 0x140957631
0095769E  4D 85 FF                        test r15, r15
009576A1  0F 84 F8 F5 FF FF               je 0x140956c9f
009576A7  41 83 FD 08                     cmp r13d, 8
009576AB  0F 85 EE F5 FF FF               jne 0x140956c9f
009576B1  4D 85 E4                        test r12, r12
009576B4  0F 85 E5 F5 FF FF               jne 0x140956c9f
009576BA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009576C3  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009576CA  E8 21 82 8D FF                  call 0x14022f8f0
009576CF  8B C8                           mov ecx, eax
009576D1  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
009576D6  49 8B D7                        mov rdx, r15
009576D9  E8 82 48 E1 FF                  call 0x14076bf60
009576DE  8B 5C 24 5C                     mov ebx, dword ptr [rsp + 0x5c]
009576E2  E9 D6 07 00 00                  jmp 0x140957ebd
009576E7  4D 85 FF                        test r15, r15
009576EA  0F 85 AF F5 FF FF               jne 0x140956c9f
009576F0  4D 85 E4                        test r12, r12
009576F3  0F 85 A6 F5 FF FF               jne 0x140956c9f
009576F9  E8 0E 5D 2E 00                  call 0x140c3d40c
009576FE  8B D8                           mov ebx, eax
00957700  E8 3B 48 B4 FF                  call 0x14049bf40
00957705  88 05 C9 57 5B 00               mov byte ptr [rip + 0x5b57c9], al
0095770B  E9 B8 EC FF FF                  jmp 0x1409563c8
00957710  8B CE                           mov ecx, esi
00957712  83 E9 46                        sub ecx, 0x46
00957715  0F 84 C6 00 00 00               je 0x1409577e1
0095771B  83 E9 01                        sub ecx, 1
0095771E  0F 84 24 FF FF FF               je 0x140957648
00957724  83 E9 01                        sub ecx, 1
00957727  74 50                           je 0x140957779
00957729  83 E9 01                        sub ecx, 1
0095772C  0F 84 AB 05 00 00               je 0x140957cdd
00957732  83 F9 01                        cmp ecx, 1
00957735  0F 85 64 F5 FF FF               jne 0x140956c9f
0095773B  40 38 7C 24 58                  cmp byte ptr [rsp + 0x58], dil
00957740  0F 85 A9 F3 FF FF               jne 0x140956aef
00957746  4D 85 FF                        test r15, r15
00957749  0F 84 50 F5 FF FF               je 0x140956c9f
0095774F  41 83 FD 10                     cmp r13d, 0x10
00957753  0F 85 46 F5 FF FF               jne 0x140956c9f
00957759  4D 85 E4                        test r12, r12
0095775C  0F 85 3D F5 FF FF               jne 0x140956c9f
00957762  39 7C 24 50                     cmp dword ptr [rsp + 0x50], edi
00957766  0F 85 33 F5 FF FF               jne 0x140956c9f
0095776C  49 8B CF                        mov rcx, r15
0095776F  E8 B4 A3 14 00                  call 0x140aa1b28
00957774  E9 4B FD FF FF                  jmp 0x1409574c4
00957779  4D 85 FF                        test r15, r15
0095777C  0F 84 1D F5 FF FF               je 0x140956c9f
00957782  4D 85 E4                        test r12, r12
00957785  0F 84 14 F5 FF FF               je 0x140956c9f
0095778B  41 83 FD 28                     cmp r13d, 0x28
0095778F  0F 85 2E EC FF FF               jne 0x1409563c3
00957795  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
0095779A  41 83 FD 08                     cmp r13d, 8
0095779E  0F 85 1F EC FF FF               jne 0x1409563c3
009577A4  83 FE 48                        cmp esi, 0x48
009577A7  0F 94 C2                        sete dl
009577AA  4C 8D 84 24 E0 00 00 00         lea r8, [rsp + 0xe0]
009577B2  49 8B CF                        mov rcx, r15
009577B5  E8 62 81 8D FF                  call 0x14022f91c
009577BA  8B D8                           mov ebx, eax
009577BC  49 8B F6                        mov rsi, r14
009577BF  85 C0                           test eax, eax
009577C1  0F 88 E0 F4 FF FF               js 0x140956ca7
009577C7  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
009577CF  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009577D4  C7 44 24 54 08 00 00 00         mov dword ptr [rsp + 0x54], 8
009577DC  E9 E1 06 00 00                  jmp 0x140957ec2
009577E1  33 C9                           xor ecx, ecx
009577E3  E8 F8 6F A2 FF                  call 0x14037e7e0
009577E8  48 89 05 A1 6F 5B 00            mov qword ptr [rip + 0x5b6fa1], rax
009577EF  E9 C9 06 00 00                  jmp 0x140957ebd
009577F4  4D 85 FF                        test r15, r15
009577F7  0F 85 A2 F4 FF FF               jne 0x140956c9f
009577FD  4D 85 E4                        test r12, r12
00957800  0F 84 99 F4 FF FF               je 0x140956c9f
00957806  E8 A1 EC 12 00                  call 0x140a864ac
0095780B  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
00957812  E9 C2 EF FF FF                  jmp 0x1409567d9
00957817  83 FE 57                        cmp esi, 0x57
0095781A  0F 8F 6E 03 00 00               jg 0x140957b8e
00957820  0F 84 83 02 00 00               je 0x140957aa9
00957826  83 FE 51                        cmp esi, 0x51
00957829  0F 8F 6B 01 00 00               jg 0x14095799a
0095782F  74 21                           je 0x140957852
00957831  83 EE 4C                        sub esi, 0x4c
00957834  0F 84 03 01 00 00               je 0x14095793d
0095783A  83 EE 01                        sub esi, 1
0095783D  74 60                           je 0x14095789f
0095783F  83 EE 01                        sub esi, 1
00957842  74 18                           je 0x14095785c
00957844  83 EE 01                        sub esi, 1
00957847  74 09                           je 0x140957852
00957849  83 FE 01                        cmp esi, 1
0095784C  0F 85 4D F4 FF FF               jne 0x140956c9f
00957852  BB 02 00 00 C0                  mov ebx, 0xc0000002
00957857  E9 6C EB FF FF                  jmp 0x1409563c8
0095785C  38 4C 24 58                     cmp byte ptr [rsp + 0x58], cl
00957860  0F 85 89 F2 FF FF               jne 0x140956aef
00957866  4D 85 E4                        test r12, r12
00957869  0F 85 30 F4 FF FF               jne 0x140956c9f
0095786F  39 7C 24 50                     cmp dword ptr [rsp + 0x50], edi
00957873  0F 85 26 F4 FF FF               jne 0x140956c9f
00957879  4D 85 FF                        test r15, r15
0095787C  74 17                           je 0x140957895
0095787E  41 83 FD 04                     cmp r13d, 4
00957882  0F 85 17 F4 FF FF               jne 0x140956c9f
00957888  49 8B CF                        mov rcx, r15
0095788B  E8 20 31 B8 FF                  call 0x1404da9b0
00957890  E9 CC F7 FF FF                  jmp 0x140957061
00957895  E8 9E 9C B8 FF                  call 0x1404e1538
0095789A  E9 1E 06 00 00                  jmp 0x140957ebd
0095789F  4D 85 FF                        test r15, r15
009578A2  0F 85 F7 F3 FF FF               jne 0x140956c9f
009578A8  4D 85 E4                        test r12, r12
009578AB  0F 85 EE F3 FF FF               jne 0x140956c9f
009578B1  44 8A 2D 80 01 51 00            mov r13b, byte ptr [rip + 0x510180]
009578B8  E8 1B CB FB FF                  call 0x1409143d8
009578BD  84 C0                           test al, al
009578BF  74 38                           je 0x1409578f9
009578C1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009578CA  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009578D1  E8 1A 80 8D FF                  call 0x14022f8f0
009578D6  83 C9 FF                        or ecx, 0xffffffff
009578D9  3B C1                           cmp eax, ecx
009578DB  74 12                           je 0x1409578ef
009578DD  41 8D 57 06                     lea edx, [r15 + 6]
009578E1  8B C8                           mov ecx, eax
009578E3  E8 18 3A 03 00                  call 0x14098b300
009578E8  8B D8                           mov ebx, eax
009578EA  E9 5C EA FF FF                  jmp 0x14095634b
009578EF  BB 55 04 00 C0                  mov ebx, 0xc0000455
009578F4  E9 52 EA FF FF                  jmp 0x14095634b
009578F9  40 0F B6 F7                     movzx esi, dil
009578FD  80 3D 75 3C 4B 00 00            cmp byte ptr [rip + 0x4b3c75], 0
00957904  75 0F                           jne 0x140957915
00957906  80 3D 47 01 51 00 00            cmp byte ptr [rip + 0x510147], 0
0095790D  B9 01 00 00 00                  mov ecx, 1
00957912  0F 44 F1                        cmove esi, ecx
00957915  40 84 F6                        test sil, sil
00957918  75 0D                           jne 0x140957927
0095791A  BA 06 00 00 00                  mov edx, 6
0095791F  8D 4A 04                        lea ecx, [rdx + 4]
00957922  E8 49 CF B5 FF                  call 0x1404b4870
00957927  45 84 ED                        test r13b, r13b
0095792A  0F 85 8D 05 00 00               jne 0x140957ebd
00957930  44 8A C6                        mov r8b, sil
00957933  E8 C0 A3 16 00                  call 0x140ac1cf8
00957938  E9 80 05 00 00                  jmp 0x140957ebd
0095793D  4D 85 FF                        test r15, r15
00957940  0F 85 59 F3 FF FF               jne 0x140956c9f
00957946  4D 85 E4                        test r12, r12
00957949  0F 84 50 F3 FF FF               je 0x140956c9f
0095794F  8B 05 7B 4A 5B 00               mov eax, dword ptr [rip + 0x5b4a7b]
00957955  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
0095795C  48 8B 05 1D 4C 5B 00            mov rax, qword ptr [rip + 0x5b4c1d]
00957963  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
0095796B  48 8B 05 16 4C 5B 00            mov rax, qword ptr [rip + 0x5b4c16]
00957972  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
0095797A  44 38 3D 7F 49 5B 00            cmp byte ptr [rip + 0x5b497f], r15b
00957981  75 0A                           jne 0x14095798d
00957983  BB 01 00 00 C0                  mov ebx, 0xc0000001
00957988  E9 3B EA FF FF                  jmp 0x1409563c8
0095798D  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
00957995  E9 E1 EC FF FF                  jmp 0x14095667b
0095799A  83 EE 52                        sub esi, 0x52
0095799D  0F 84 AF FE FF FF               je 0x140957852
009579A3  83 EE 01                        sub esi, 1
009579A6  0F 84 D7 00 00 00               je 0x140957a83
009579AC  83 EE 01                        sub esi, 1
009579AF  0F 84 90 00 00 00               je 0x140957a45
009579B5  83 EE 01                        sub esi, 1
009579B8  74 6A                           je 0x140957a24
009579BA  83 FE 01                        cmp esi, 1
009579BD  0F 85 DC F2 FF FF               jne 0x140956c9f
009579C3  4D 85 FF                        test r15, r15
009579C6  0F 84 D3 F2 FF FF               je 0x140956c9f
009579CC  4D 85 E4                        test r12, r12
009579CF  0F 84 CA F2 FF FF               je 0x140956c9f
009579D5  41 8B D5                        mov edx, r13d
009579D8  45 33 C0                        xor r8d, r8d
009579DB  49 8B CF                        mov rcx, r15
009579DE  E8 09 FC AF FF                  call 0x1404575ec
009579E3  8B D8                           mov ebx, eax
009579E5  49 8B F6                        mov rsi, r14
009579E8  85 C0                           test eax, eax
009579EA  0F 88 B7 F2 FF FF               js 0x140956ca7
009579F0  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
009579F8  49 8B CF                        mov rcx, r15
009579FB  E8 5C 16 12 00                  call 0x140a7905c
00957A00  8B D8                           mov ebx, eax
00957A02  85 C0                           test eax, eax
00957A04  0F 88 9D F2 FF FF               js 0x140956ca7
00957A0A  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
00957A12  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00957A17  C7 44 24 54 34 00 00 00         mov dword ptr [rsp + 0x54], 0x34
00957A1F  E9 99 04 00 00                  jmp 0x140957ebd
00957A24  41 8B 57 08                     mov edx, dword ptr [r15 + 8]
00957A28  49 8B 0F                        mov rcx, qword ptr [r15]
00957A2B  41 38 7F 0C                     cmp byte ptr [r15 + 0xc], dil
00957A2F  74 0A                           je 0x140957a3b
00957A31  E8 8A FC B1 FF                  call 0x1404776c0
00957A36  E9 26 F6 FF FF                  jmp 0x140957061
00957A3B  E8 70 FB B1 FF                  call 0x1404775b0
00957A40  E9 1C F6 FF FF                  jmp 0x140957061
00957A45  4D 85 FF                        test r15, r15
00957A48  0F 84 51 F2 FF FF               je 0x140956c9f
00957A4E  4D 85 E4                        test r12, r12
00957A51  0F 85 48 F2 FF FF               jne 0x140956c9f
00957A57  41 83 FD 10                     cmp r13d, 0x10
00957A5B  0F 82 62 E9 FF FF               jb 0x1409563c3
00957A61  41 0F B7 47 0C                  movzx eax, word ptr [r15 + 0xc]
00957A66  8D 04 45 0E 00 00 00            lea eax, [rax*2 + 0xe]
00957A6D  44 3B E8                        cmp r13d, eax
00957A70  0F 82 4D E9 FF FF               jb 0x1409563c3
00957A76  49 8B CF                        mov rcx, r15
00957A79  E8 DA 02 16 00                  call 0x140ab7d58
00957A7E  E9 2D 04 00 00                  jmp 0x140957eb0
00957A83  4D 85 FF                        test r15, r15
00957A86  0F 85 13 F2 FF FF               jne 0x140956c9f
00957A8C  4D 85 E4                        test r12, r12
00957A8F  0F 84 0A F2 FF FF               je 0x140956c9f
00957A95  33 D2                           xor edx, edx
00957A97  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00957A9F  E8 80 DB 0D 00                  call 0x140a35624
00957AA4  E9 B5 E7 FF FF                  jmp 0x14095625e
00957AA9  4D 85 FF                        test r15, r15
00957AAC  0F 84 ED F1 FF FF               je 0x140956c9f
00957AB2  41 83 FD 08                     cmp r13d, 8
00957AB6  0F 82 E3 F1 FF FF               jb 0x140956c9f
00957ABC  41 8B 1F                        mov ebx, dword ptr [r15]
00957ABF  41 8B 57 04                     mov edx, dword ptr [r15 + 4]
00957AC3  8D 43 9C                        lea eax, [rbx - 0x64]
00957AC6  3D 9B 0F 00 00                  cmp eax, 0xf9b
00957ACB  0F 86 CE F1 FF FF               jbe 0x140956c9f
00957AD1  81 FB 0B 10 00 00               cmp ebx, 0x100b
00957AD7  0F 8D C2 F1 FF FF               jge 0x140956c9f
00957ADD  8D 83 00 F0 FF FF               lea eax, [rbx - 0x1000]
00957AE3  83 F8 0A                        cmp eax, 0xa
00957AE6  77 69                           ja 0x140957b51
00957AE8  8A 54 24 58                     mov dl, byte ptr [rsp + 0x58]
00957AEC  48 8B 0D 3D 20 68 00            mov rcx, qword ptr [rip + 0x68203d]
00957AF3  E8 28 A3 F1 FF                  call 0x140871e20
00957AF8  84 C0                           test al, al
00957AFA  75 1A                           jne 0x140957b16
00957AFC  48 8D 0D 7D A1 1A 00            lea rcx, [rip + 0x1aa17d]
00957B03  E8 08 84 B8 FF                  call 0x1404dff10
00957B08  84 C0                           test al, al
00957B0A  75 0A                           jne 0x140957b16
00957B0C  BB 61 00 00 C0                  mov ebx, 0xc0000061
00957B11  E9 B2 E8 FF FF                  jmp 0x1409563c8
00957B16  48 8D 44 24 59                  lea rax, [rsp + 0x59]
00957B1B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00957B20  48 8D 44 24 54                  lea rax, [rsp + 0x54]
00957B25  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00957B2A  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00957B2F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00957B34  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00957B38  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00957B3C  4D 8B CC                        mov r9, r12
00957B3F  45 8B C5                        mov r8d, r13d
00957B42  49 8B D7                        mov rdx, r15
00957B45  8B CB                           mov ecx, ebx
00957B47  E8 BC 31 03 00                  call 0x14098ad08
00957B4C  E9 D9 F0 FF FF                  jmp 0x140956c2a
00957B51  48 8D 44 24 59                  lea rax, [rsp + 0x59]
00957B56  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00957B5B  48 8D 44 24 54                  lea rax, [rsp + 0x54]
00957B60  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00957B65  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00957B6A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00957B6F  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00957B73  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00957B77  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00957B7C  45 8B CD                        mov r9d, r13d
00957B7F  4D 8B C7                        mov r8, r15
00957B82  8B CB                           mov ecx, ebx
00957B84  E8 37 3C 13 00                  call 0x140a8b7c0
00957B89  E9 9C F0 FF FF                  jmp 0x140956c2a
00957B8E  83 FE 5D                        cmp esi, 0x5d
00957B91  0F 8F BC 01 00 00               jg 0x140957d53
00957B97  0F 84 6B 01 00 00               je 0x140957d08
00957B9D  8B CE                           mov ecx, esi
00957B9F  83 E9 58                        sub ecx, 0x58
00957BA2  0F 84 35 01 00 00               je 0x140957cdd
00957BA8  83 E9 01                        sub ecx, 1
00957BAB  0F 84 DB 00 00 00               je 0x140957c8c
00957BB1  83 E9 01                        sub ecx, 1
00957BB4  0F 84 A6 00 00 00               je 0x140957c60
00957BBA  83 E9 01                        sub ecx, 1
00957BBD  74 49                           je 0x140957c08
00957BBF  83 F9 01                        cmp ecx, 1
00957BC2  0F 85 D7 F0 FF FF               jne 0x140956c9f
00957BC8  4D 85 FF                        test r15, r15
00957BCB  0F 84 CE F0 FF FF               je 0x140956c9f
00957BD1  4D 85 E4                        test r12, r12
00957BD4  0F 84 C5 F0 FF FF               je 0x140956c9f
00957BDA  41 83 FD 0C                     cmp r13d, 0xc
00957BDE  0F 85 DF E7 FF FF               jne 0x1409563c3
00957BE4  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
00957BE9  41 83 FD 08                     cmp r13d, 8
00957BED  0F 85 D0 E7 FF FF               jne 0x1409563c3
00957BF3  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
00957BFB  49 8B CF                        mov rcx, r15
00957BFE  E8 DD 22 E1 FF                  call 0x140769ee0
00957C03  E9 B2 FB FF FF                  jmp 0x1409577ba
00957C08  E8 33 43 B4 FF                  call 0x14049bf40
00957C0D  84 C0                           test al, al
00957C0F  0F 84 33 FA FF FF               je 0x140957648
00957C15  4D 85 FF                        test r15, r15
00957C18  0F 84 81 F0 FF FF               je 0x140956c9f
00957C1E  41 81 FD 50 01 00 00            cmp r13d, 0x150
00957C25  0F 85 74 F0 FF FF               jne 0x140956c9f
00957C2B  4D 85 E4                        test r12, r12
00957C2E  0F 84 6B F0 FF FF               je 0x140956c9f
00957C34  49 8B CF                        mov rcx, r15
00957C37  E8 F8 E0 B4 FF                  call 0x1404a5d34
00957C3C  88 84 24 E0 00 00 00            mov byte ptr [rsp + 0xe0], al
00957C43  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
00957C4B  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00957C50  B9 01 00 00 00                  mov ecx, 1
00957C55  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
00957C59  8B DF                           mov ebx, edi
00957C5B  E9 5D 02 00 00                  jmp 0x140957ebd
00957C60  4D 85 FF                        test r15, r15
00957C63  0F 84 36 F0 FF FF               je 0x140956c9f
00957C69  41 83 FD 04                     cmp r13d, 4
00957C6D  0F 82 2C F0 FF FF               jb 0x140956c9f
00957C73  4D 85 E4                        test r12, r12
00957C76  0F 85 23 F0 FF FF               jne 0x140956c9f
00957C7C  41 39 3F                        cmp dword ptr [r15], edi
00957C7F  0F 95 C1                        setne cl
00957C82  E8 2D D2 B7 FF                  call 0x1404d4eb4
00957C87  E9 31 02 00 00                  jmp 0x140957ebd
00957C8C  4D 85 FF                        test r15, r15
00957C8F  0F 84 0A F0 FF FF               je 0x140956c9f
00957C95  4D 85 E4                        test r12, r12
00957C98  0F 84 01 F0 FF FF               je 0x140956c9f
00957C9E  41 83 FD 04                     cmp r13d, 4
00957CA2  0F 82 1B E7 FF FF               jb 0x1409563c3
00957CA8  B9 06 00 00 00                  mov ecx, 6
00957CAD  E8 CA 21 15 00                  call 0x140aa9e7c
00957CB2  E8 09 07 22 00                  call 0x140b783c0
00957CB7  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00957CBC  48 8D 94 24 88 00 00 00         lea rdx, [rsp + 0x88]
00957CC4  41 8B 0F                        mov ecx, dword ptr [r15]
00957CC7  E8 9C B5 DA FF                  call 0x140703268
00957CCC  8B D8                           mov ebx, eax
00957CCE  E8 3D 07 22 00                  call 0x140b78410
00957CD3  B9 06 00 00 00                  mov ecx, 6
00957CD8  E9 5F F6 FF FF                  jmp 0x14095733c
00957CDD  4D 85 FF                        test r15, r15
00957CE0  0F 85 B9 EF FF FF               jne 0x140956c9f
00957CE6  4D 85 E4                        test r12, r12
00957CE9  0F 85 B0 EF FF FF               jne 0x140956c9f
00957CEF  41 8D 4F 17                     lea ecx, [r15 + 0x17]
00957CF3  83 FE 58                        cmp esi, 0x58
00957CF6  8D 41 F4                        lea eax, [rcx - 0xc]
00957CF9  0F 45 C8                        cmovne ecx, eax
00957CFC  E8 57 2A 03 00                  call 0x14098a758
00957D01  8B DF                           mov ebx, edi
00957D03  E9 C0 E6 FF FF                  jmp 0x1409563c8
00957D08  4D 85 FF                        test r15, r15
00957D0B  0F 84 8E EF FF FF               je 0x140956c9f
00957D11  4D 85 E4                        test r12, r12
00957D14  0F 84 85 EF FF FF               je 0x140956c9f
00957D1A  41 83 FD 08                     cmp r13d, 8
00957D1E  0F 85 9F E6 FF FF               jne 0x1409563c3
00957D24  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
00957D29  41 83 FD 0C                     cmp r13d, 0xc
00957D2D  0F 82 90 E6 FF FF               jb 0x1409563c3
00957D33  45 8B C5                        mov r8d, r13d
00957D36  49 8B D4                        mov rdx, r12
00957D39  49 8B 0F                        mov rcx, qword ptr [r15]
00957D3C  E8 27 39 03 00                  call 0x14098b668
00957D41  8B D8                           mov ebx, eax
00957D43  49 8B F6                        mov rsi, r14
00957D46  85 C0                           test eax, eax
00957D48  0F 88 59 EF FF FF               js 0x140956ca7
00957D4E  E9 6F 01 00 00                  jmp 0x140957ec2
00957D53  83 EE 5E                        sub esi, 0x5e
00957D56  0F 84 22 01 00 00               je 0x140957e7e
00957D5C  83 EE 01                        sub esi, 1
00957D5F  0F 84 EA 00 00 00               je 0x140957e4f
00957D65  83 EE 01                        sub esi, 1
00957D68  0F 84 BC 00 00 00               je 0x140957e2a
00957D6E  83 EE 01                        sub esi, 1
00957D71  74 42                           je 0x140957db5
00957D73  83 FE 01                        cmp esi, 1
00957D76  0F 85 23 EF FF FF               jne 0x140956c9f
00957D7C  4D 85 FF                        test r15, r15
00957D7F  0F 85 1A EF FF FF               jne 0x140956c9f
00957D85  4D 85 E4                        test r12, r12
00957D88  0F 84 11 EF FF FF               je 0x140956c9f
00957D8E  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00957D96  E8 A1 AF 18 00                  call 0x140ae2d3c
00957D9B  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
00957DA3  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00957DA8  C7 44 24 54 44 00 00 00         mov dword ptr [rsp + 0x54], 0x44
00957DB0  E9 08 01 00 00                  jmp 0x140957ebd
00957DB5  4D 85 FF                        test r15, r15
00957DB8  0F 84 E1 EE FF FF               je 0x140956c9f
00957DBE  45 85 ED                        test r13d, r13d
00957DC1  0F 84 D8 EE FF FF               je 0x140956c9f
00957DC7  4D 85 E4                        test r12, r12
00957DCA  0F 84 CF EE FF FF               je 0x140956c9f
00957DD0  39 7C 24 50                     cmp dword ptr [rsp + 0x50], edi
00957DD4  0F 84 C5 EE FF FF               je 0x140956c9f
00957DDA  41 83 FD 20                     cmp r13d, 0x20
00957DDE  0F 82 DF E5 FF FF               jb 0x1409563c3
00957DE4  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
00957DE9  41 83 FD 10                     cmp r13d, 0x10
00957DED  0F 82 D0 E5 FF FF               jb 0x1409563c3
00957DF3  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
00957DFB  49 8B CF                        mov rcx, r15
00957DFE  E8 21 5A 17 00                  call 0x140acd824
00957E03  8B D8                           mov ebx, eax
00957E05  49 8B F6                        mov rsi, r14
00957E08  85 C0                           test eax, eax
00957E0A  0F 88 97 EE FF FF               js 0x140956ca7
00957E10  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
00957E18  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00957E1D  C7 44 24 54 10 00 00 00         mov dword ptr [rsp + 0x54], 0x10
00957E25  E9 98 00 00 00                  jmp 0x140957ec2
00957E2A  4D 85 FF                        test r15, r15
00957E2D  0F 84 6C EE FF FF               je 0x140956c9f
00957E33  4D 85 E4                        test r12, r12
00957E36  0F 85 63 EE FF FF               jne 0x140956c9f
00957E3C  44 3B E9                        cmp r13d, ecx
00957E3F  0F 82 7E E5 FF FF               jb 0x1409563c3
00957E45  41 8A 0F                        mov cl, byte ptr [r15]
00957E48  E8 0F C4 17 00                  call 0x140ad425c
00957E4D  EB 61                           jmp 0x140957eb0
00957E4F  4D 85 FF                        test r15, r15
00957E52  0F 84 47 EE FF FF               je 0x140956c9f
00957E58  44 3B E9                        cmp r13d, ecx
00957E5B  0F 85 3E EE FF FF               jne 0x140956c9f
00957E61  4D 85 E4                        test r12, r12
00957E64  0F 85 35 EE FF FF               jne 0x140956c9f
00957E6A  45 33 C0                        xor r8d, r8d
00957E6D  49 8B D7                        mov rdx, r15
00957E70  48 8B 0D 19 2B 63 00            mov rcx, qword ptr [rip + 0x632b19]
00957E77  E8 34 A8 A3 FF                  call 0x1403926b0
00957E7C  EB 3F                           jmp 0x140957ebd
00957E7E  4D 85 FF                        test r15, r15
00957E81  0F 84 18 EE FF FF               je 0x140956c9f
00957E87  4D 85 E4                        test r12, r12
00957E8A  0F 85 0F EE FF FF               jne 0x140956c9f
00957E90  39 7C 24 50                     cmp dword ptr [rsp + 0x50], edi
00957E94  0F 85 05 EE FF FF               jne 0x140956c9f
00957E9A  41 83 FD 20                     cmp r13d, 0x20
00957E9E  0F 85 1F E5 FF FF               jne 0x1409563c3
00957EA4  8A 54 24 58                     mov dl, byte ptr [rsp + 0x58]
00957EA8  49 8B CF                        mov rcx, r15
00957EAB  E8 C8 E1 0C 00                  call 0x140a26078
00957EB0  85 C0                           test eax, eax
00957EB2  8B D8                           mov ebx, eax
00957EB4  49 8B F6                        mov rsi, r14
00957EB7  0F 88 EA ED FF FF               js 0x140956ca7
00957EBD  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
00957EC2  48 39 7C 24 60                  cmp qword ptr [rsp + 0x60], rdi
00957EC7  74 3A                           je 0x140957f03
00957EC9  4D 85 E4                        test r12, r12
00957ECC  74 35                           je 0x140957f03
00957ECE  44 3B 6C 24 54                  cmp r13d, dword ptr [rsp + 0x54]
00957ED3  0F 82 EA E4 FF FF               jb 0x1409563c3
00957ED9  44 8B 44 24 54                  mov r8d, dword ptr [rsp + 0x54]
00957EDE  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00957EE3  49 8B CC                        mov rcx, r12
00957EE6  E8 55 E9 D6 FF                  call 0x1406c6840
00957EEB  EB 16                           jmp 0x140957f03
00957EED  8B D8                           mov ebx, eax
00957EEF  48 8B B4 24 A0 00 00 00         mov rsi, qword ptr [rsp + 0xa0]
00957EF7  33 FF                           xor edi, edi
00957EF9  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00957EFE  E9 A4 ED FF FF                  jmp 0x140956ca7
00957F03  49 8B F6                        mov rsi, r14
00957F06  44 8B AC 24 84 00 00 00         mov r13d, dword ptr [rsp + 0x84]
00957F0E  41 83 FD 33                     cmp r13d, 0x33
00957F12  0F 84 8F ED FF FF               je 0x140956ca7
00957F18  41 83 FD 59                     cmp r13d, 0x59
00957F1C  0F 84 85 ED FF FF               je 0x140956ca7
00957F22  E9 DA FD FF FF                  jmp 0x140957d01
00957F27  48 8B 8C 24 20 07 00 00         mov rcx, qword ptr [rsp + 0x720]
00957F2F  48 33 CC                        xor rcx, rsp
00957F32  E8 09 47 D5 FF                  call 0x1406ac640
00957F37  48 81 C4 30 07 00 00            add rsp, 0x730
00957F3E  41 5F                           pop r15
00957F40  41 5E                           pop r14
00957F42  41 5D                           pop r13
00957F44  41 5C                           pop r12
00957F46  5F                              pop rdi
00957F47  5E                              pop rsi
00957F48  5B                              pop rbx
00957F49  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtPowerInformation(int a1, __int64 a2, int a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m64F;
    unsigned __int8 v_stack_m650;
    unsigned int v_stack_m654;
    unsigned __int8 v_stack_m657;
    unsigned __int8 v_stack_m658;
    unsigned int v_stack_m65C;
    unsigned int v_stack_m660;
    unsigned int v_stack_m664;
    unsigned int v_stack_m668;
    unsigned int v_stack_m66C;
    unsigned int v_stack_m670;
    unsigned int v_stack_m674;
    unsigned __int8 v_stack_m676;
    unsigned int v_stack_m678;
    unsigned __int8 v_stack_m67C;
    unsigned int v_stack_m680;
    unsigned int v_stack_m684;
    unsigned __int64 v_stack_m688;
    unsigned __int64 v_stack_m698;
    unsigned int v_stack_m69C;
    unsigned __int64 v_stack_m6A4;
    unsigned int v_stack_m6A8;
    unsigned __int64 v_stack_m6B0;
    unsigned __int64 v_stack_m6B8;
    unsigned int v_stack_m6BC;
    unsigned int v_stack_m6C0;
    unsigned __int64 v_stack_m6C8;
    unsigned __int64 v_stack_m6D0;
    unsigned int v_stack_m6D8;
    unsigned __int64 v_stack_m6E0;
    unsigned int v_stack_m6E4;
    unsigned __int8 v_stack_m6E8;
    unsigned int v_stack_m6F0;
    unsigned __int64 v_stack_m6F8;
    unsigned __int8 v_stack_m6FF;
    unsigned __int8 v_stack_m700;
    unsigned __int64 v_stack_m708;
    unsigned int v_stack_m70C;
    unsigned __int8 v_stack_m70F;
    unsigned __int8 v_stack_m710;
    unsigned int v_stack_m714;
    unsigned int v_stack_m718;
    unsigned __int64 v_stack_m728;
    unsigned __int64 v_stack_m730;
    unsigned __int64 v_stack_m738;
    unsigned __int64 v_stack_m740;
    unsigned __int64 v_stack_m748;
    unsigned __int64 v_stack_m88;

    v_rsp = (v_rsp) - (0x730ULL);
    result = (*(unsigned __int64 *)(v_rip + 4934054)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m6E4 = a1;
    v_rdi = 0;
    v_stack_m6FF = 0;
    a2 = 0;
    result = memset(v_stack_m688, a2, (unsigned int)(0x600ULL), a4);
    v_stack_m6D8 = 0;
    v_stack_m6E0 = 0;
    v_stack_m708 = 0;
    v_stack_m714 = 0;
    v_stack_m6F8 = 0;
    v_stack_m6D0 = 0;
    v_stack_m700 = 0;
    v_stack_m70F = 0;
    v_stack_m6F0 = 0;
    v_stack_m70C = 0;
    if (((unsigned int)((unsigned int)(a1))) > 98) goto loc_00956CA2;
    v_stack_m710 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = -(0);
    v_r13 = (unsigned int)(((unsigned int)(a1)) & ((unsigned int)((unsigned int)(a3))));
    result = (unsigned int)(-((unsigned int)((unsigned int)(v_r13))));
    v_r14 = ((unsigned int)(a3)) & (0);
    v_stack_m6C8 = v_r14;
    result = -(a4);
    result = (unsigned int)((result) & (a5));
    v_stack_m718 = (unsigned int)(result);
    result = (unsigned int)(-(result));
    v_r12 = (v_r12) & (a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00956183;
    if (((unsigned int)((int)(v_stack_m6E4))) > 34) goto loc_00955E8C;
    if (((unsigned int)((int)(v_stack_m6E4))) < 34) goto loc_00955EA4;
loc_00955E8C:
    if (((unsigned int)((int)(v_stack_m6E4) - 39)) > 58) goto loc_00955EB6;
    if (((unsigned int)((int)(v_stack_m6E4) - 39)) >= 58) goto loc_00955EB6;
loc_00955EA4:
    goto loc_00956CA7;
loc_00955EB6:
    if (((unsigned int)(v_r14 - 37)) > 58) goto loc_00955ED6;
    if (((unsigned int)(v_r14 - 37)) >= 58) goto loc_00955ED6;
    goto loc_00955EE4;
loc_00955ED6:
    if (((unsigned int)(v_r14 - 2)) > 1) goto loc_00955F62;
loc_00955EE4:
    a1 = 0;
    result = SeIsAppContainerOrIdentifyLevelContext(a1, v_stack_m6FF, (unsigned int)(0x600ULL), a4);
    v_stack_m70C = (unsigned int)(result);
    if (sign_flag) goto loc_00955F55;
    if (v_stack_m6FF == 0) goto loc_00955F68;
    if (((unsigned int)(v_r14)) == 73) goto loc_00955F0B;
    if (((unsigned int)(v_r14)) != 88) goto loc_00955F38;
loc_00955F0B:
    result = PopCapabilityCheck(v_rip + 1752318, v_stack_m6FF, (unsigned int)(0x600ULL), a4);
    v_stack_m6E8 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) != 0) goto loc_00955F68;
    v_stack_m70C = (unsigned int)((unsigned int)(0xC0000022ULL));
    goto loc_00956CA7;
loc_00955F38:
    if (v_stack_m6FF == 0) goto loc_00955F68;
    v_stack_m70C = (unsigned int)((unsigned int)(0xC0000022ULL));
    goto loc_00956CA7;
loc_00955F55:
    goto loc_00956CA7;
loc_00955F62:
    goto loc_00955F6C;
loc_00955F68:
loc_00955F6C:
    if (((unsigned int)(v_r14 - 92)) > ((unsigned int)(v_stack_m6F8))) goto loc_00955F90;
    result = ExCheckFullProcessInformationAccess(v_stack_m710, v_stack_m6FF, (unsigned int)(0x600ULL), a4);
    v_stack_m70C = (unsigned int)(result);
    if (!sign_flag) goto loc_00955F90;
    goto loc_00956CA7;
loc_00955F90:
    if (((unsigned int)(v_r14 - 28)) > 50) goto loc_00955FC7;
    if (((unsigned int)(v_r14 - 28)) >= 50) goto loc_00955FC7;
    result = EtwpCoverageUserIsAdmin(v_stack_m710, v_stack_m6FF, (unsigned int)(0x600ULL), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00955FC7;
    v_stack_m70C = (unsigned int)((unsigned int)(0xC0000022ULL));
    goto loc_00956CA7;
loc_00955FC7:
    if (((unsigned int)(v_r14)) != 71) goto loc_00955FEB;
    result = PopIsRunningAsLocalSystem(v_stack_m710, v_stack_m6FF, (unsigned int)(0x600ULL), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00955FEB;
    v_stack_m70C = (unsigned int)((unsigned int)(0xC0000022ULL));
    goto loc_00956CA7;
loc_00955FEB:
    if (v_r14 == 0) goto loc_00956142;
    if (((unsigned int)(v_r14 - 11)) > 61) goto loc_0095600C;
    if (((unsigned int)(v_r14 - 11)) < 61) goto loc_0095602B;
loc_0095600C:
    result = PsIsCurrentThreadInServerSilo(v_stack_m710, v_stack_m6FF, (unsigned int)(0x600ULL), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0095602B;
    v_stack_m70C = (unsigned int)((unsigned int)(0xC00000BBULL));
    goto loc_00956CA7;
loc_0095602B:
    if (((unsigned int)(v_r14)) == 9) goto loc_00956048;
    if (((unsigned int)(v_r14 - 38)) > 57) goto loc_00956067;
    if (((unsigned int)(v_r14 - 38)) >= 57) goto loc_00956067;
loc_00956048:
    result = EtwpCoverageUserIsAdmin(v_stack_m710, v_stack_m6FF, (unsigned int)(0x600ULL), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00956067;
    v_stack_m70C = (unsigned int)((unsigned int)(0xC0000022ULL));
    goto loc_00956CA7;
loc_00956067:
    if (((unsigned int)(v_r14 - 2)) <= ((unsigned int)(v_stack_m6F8))) goto loc_009560C9;
    if (((unsigned int)(v_r14 - 37)) > 61) goto loc_00956087;
    if (((unsigned int)(v_r14 - 37)) < 61) goto loc_009560C9;
loc_00956087:
    if (((unsigned int)(v_r14)) == 11) goto loc_009560C9;
    a1 = *(unsigned __int64 *)(v_rip + 6830749);
    if (((unsigned int)(v_r14)) == 10) { a1 = *(unsigned __int64 *)(v_rip + 6831266); }
    v_stack_m698 = a1;
    result = SeSinglePrivilegeCheck(a1, v_stack_m710, (unsigned int)(0x600ULL), a4);
    if ((unsigned __int8)(result) != 0) goto loc_009560C9;
    v_stack_m70C = (unsigned int)((unsigned int)(0xC0000061ULL));
    goto loc_00956CA7;
loc_009560C9:
    if ((unsigned int)(v_r13) == 0) goto loc_009560EE;
    a1 = ((unsigned int)((unsigned int)(v_r13))) + (v_r14);
    if (a1 > result) goto loc_009560E8;
    v_rbx = (unsigned int)(0xC0000061ULL);
    if (a1 < v_r14) {
        result = *(unsigned __int8 *)(result);
        v_rbx = v_stack_m70C;
    }
    if (((unsigned int)(v_r13)) > 64) goto loc_00956111;
    v_stack_m6F8 = v_stack_m88;
loc_00956101:
    result = memcpy(v_stack_m88, v_r14, (unsigned int)((unsigned int)(v_r13)), a4);
    goto loc_00956147;
loc_00956111:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_r13)), (unsigned int)(0x206D654DULL), a4);
    v_stack_m6F8 = result;
    if (result != 0) goto loc_00956101;
    v_stack_m70C = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_00956CA7;
loc_00956142:
loc_00956147:
    if (v_r12 != 0) {
        a2 = v_stack_m718;
        a3 = 1;
        a1 = v_r12;
        result = ProbeForWrite(a1, a2, a3, a4);
    }
    goto loc_0095619B;
loc_00956183:
    v_stack_m6F8 = v_r14;
loc_0095619B:
    if (((unsigned int)((unsigned int)(v_stack_m6E4))) > 31) goto loc_009561AA;
    if (((unsigned int)((unsigned int)(v_stack_m6E4))) < 31) goto loc_009561D2;
loc_009561AA:
    if (((unsigned int)((unsigned int)(v_stack_m6E4) - 38)) > 60) goto loc_009561C2;
    result = (unsigned int)(v_stack_m6E4) - 38;
    if (((unsigned int)((unsigned int)(v_stack_m6E4) - 38)) >= 60) {
        result = PopAcquirePolicyLock(1, v_stack_m700, a3, a4);
        a1 = 1;
        a2 = (unsigned __int8)(a1);
        v_stack_m700 = (unsigned __int8)(a1);
    }
    if (((unsigned int)((unsigned int)(v_stack_m6E4))) > 50) goto loc_009571E8;
    if (((unsigned int)((unsigned int)(v_stack_m6E4))) == 50) goto loc_009571C5;
    if (((unsigned int)((unsigned int)(v_stack_m6E4))) > 24) goto loc_009568EA;
    if (((unsigned int)((unsigned int)(v_stack_m6E4))) == 24) goto loc_009568B7;
    if (((unsigned int)((unsigned int)(v_stack_m6E4))) > 12) goto loc_0095672F;
    if (((unsigned int)((unsigned int)(v_stack_m6E4))) == 12) goto loc_009566D6;
    if (((unsigned int)((unsigned int)(v_stack_m6E4))) > 6) goto loc_0095654B;
    if (((unsigned int)((unsigned int)(v_stack_m6E4))) == 6) goto loc_009563F5;
    if ((unsigned int)((unsigned int)(v_stack_m6E4)) == 0) goto loc_009563A7;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m6E4)) - (1));
    if (condition_is_equal) goto loc_009563A7;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00956355;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00956355;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00956278;
    if (((unsigned int)(v_rsi)) != 1) goto loc_00956C9F;
    if (v_r14 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    result = PopCurrentPowerState(v_stack_m688, a2, a3, a4);
loc_0095625E:
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 32;
    goto loc_00957EBD;
loc_00956278:
    if (v_r14 != 0) goto loc_0095628B;
    if (v_r12 == 0) goto loc_00956C9F;
    if (v_r14 == 0) goto loc_00956305;
loc_0095628B:
    if ((((unsigned __int8)(v_stack_m688)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5991547))))) == 0) goto loc_00956C9F;
    if (((unsigned int)(v_r13)) < 76) goto loc_009563C3;
    *(unsigned __int64 *)(v_rip + 5991442) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 5991446) = v_xmm1;
    *(unsigned __int64 *)(v_rip + 5991450) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 5991454) = v_xmm1;
    *(unsigned __int64 *)(v_rip + 5991456) = v_xmm0;
    *(unsigned int *)(v_rip + 5991454) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 72)));
    result = PopResetCurrentPolicies(v_stack_m688, a2, a3, a4);
    v_stack_m70C = (unsigned int)(result);
    if (sign_flag) goto loc_00956CA7;
loc_00956305:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_rip + 5990877))) & (1));
    *(unsigned __int8 *)(v_rip + 5991350) = (unsigned __int8)(result);
    result = PopDisksRegisteredForIdle(1, a2, a3, a4);
    *(unsigned __int8 *)(v_rip + 5991351) = (unsigned __int8)(result);
    result = PopFilterCapabilities(v_rip + 5991315, v_stack_m688, a3, a4);
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 76;
loc_00956347:
loc_0095634B:
    goto loc_00957EBD;
loc_00956355:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    if (((unsigned int)(v_r13)) < 232) goto loc_009563C3;
    result = PopVerifySystemPowerPolicy(v_stack_m6F8, v_stack_m688, a3, a4);
    if (sign_flag) goto loc_00956CA7;
loc_00956395:
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 232;
    goto loc_00957EBD;
loc_009563A7:
    if (v_stack_m6F8 != 0) goto loc_009563BA;
    if (v_r12 == 0) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_009563EC;
loc_009563BA:
    if (((unsigned int)(v_r13)) >= 232) goto loc_009563D0;
loc_009563C3:
loc_009563C8:
    goto loc_00956CA7;
loc_009563D0:
    a2 = 0;
    a1 = 0;
    result = PopApplyPolicy(a1, a2, v_stack_m6F8, (unsigned int)((unsigned int)(v_r13)));
    if (sign_flag) goto loc_00956CA7;
loc_009563EC:
    goto loc_00956395;
loc_009563F5:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (((unsigned int)(v_r13)) < 24) goto loc_009563C3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m6F8)))) >= 7) goto loc_00956C9F;
    if ((*(unsigned __int64 *)(v_rip + 5990428 + (unsigned int)(*(unsigned int *)(v_stack_m6F8)) + (unsigned int)(*(unsigned int *)(v_stack_m6F8)) * 2 * 8 + 8)) == 0) goto loc_0095644D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m6F8)))) == 5) goto loc_0095644D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m6F8)))) != 4) goto loc_00956C9F;
    if ((*(unsigned __int64 *)(v_rip + 5990497)) != (v_rip + 2208528)) goto loc_00956C9F;
loc_0095644D:
    *(unsigned __int64 *)(v_rip + 5990428 + (unsigned int)(*(unsigned int *)(v_stack_m6F8)) + (unsigned int)(*(unsigned int *)(v_stack_m6F8)) * 2 * 8) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 5990428 + (unsigned int)(*(unsigned int *)(v_stack_m6F8)) + (unsigned int)(*(unsigned int *)(v_stack_m6F8)) * 2 * 8 + 16) = v_xmm1;
    *(unsigned __int16 *)(v_rip + 5990428 + (unsigned int)(*(unsigned int *)(v_stack_m6F8)) + (unsigned int)(*(unsigned int *)(v_stack_m6F8)) * 2 * 8 + 5) = 0;
    *(unsigned __int8 *)(v_rip + 5990428 + (unsigned int)(*(unsigned int *)(v_stack_m6F8)) + (unsigned int)(*(unsigned int *)(v_stack_m6F8)) * 2 * 8 + 7) = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m6F8))) == 0) goto loc_00956500;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m6F8))) - (1));
    if (condition_is_equal) goto loc_009564E9;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_009564D2;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_009564B9;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_009564B0;
    if (((unsigned int)(a2)) != 2) goto loc_00956519;
    goto loc_00956515;
loc_009564B0:
    goto loc_00956519;
loc_009564B9:
    goto loc_00956515;
loc_009564D2:
    goto loc_00956515;
loc_009564E9:
    goto loc_00956515;
loc_00956500:
loc_00956515:
    a3 = v_rip + 5990830;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5990912)))) & (8)) != 0) { a3 = 0; }
loc_00956519:
    result = (unsigned __int8)(-(*(unsigned __int8 *)(v_rip + 5990428 + (unsigned int)(*(unsigned int *)(v_stack_m6F8)) + (unsigned int)(*(unsigned int *)(v_stack_m6F8)) * 2 * 8 + 4)));
    a2 = (unsigned int)((a2) & (2));
    if (((unsigned int)(a2)) >= = (*(unsigned int *)(v_rip + 5990869))) {
        *(unsigned int *)(v_rip + 5990861) = (unsigned int)(a2);
    }
    if (a3 == 0) goto loc_00957EBD;
    result = PopChangeCapability(a3, 0, a3, 2);
    goto loc_00957EBD;
loc_0095654B:
    v_rsi = (unsigned int)((v_r14) - (7));
    if (condition_is_equal) goto loc_009566AB;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_0095668D;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00956633;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_009565CE;
    if (((unsigned int)(v_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    result = KeQueryPrimaryGroupThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 0, a3, 2);
    result = PopProcessorInformation(v_stack_m688, 0, (unsigned __int16)(result), v_stack_m714);
loc_009565AF:
    if (sign_flag) goto loc_00956CA7;
    v_stack_m708 = v_stack_m688;
    goto loc_00957EBD;
loc_009565CE:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (((unsigned int)(v_r13)) < ((unsigned int)(v_stack_m688))) goto loc_009563C3;
    result = PopAcquireTransitionLock((unsigned int)((unsigned int)(v_r12 + 3)), 0, (unsigned __int16)(result), v_stack_m714);
    result = PopAcquirePolicyLock((unsigned int)((unsigned int)(v_r12 + 3)), 0, (unsigned __int16)(result), v_stack_m714);
    a2 = ((*(unsigned __int8 *)(v_stack_m6F8)) != 0) ? 1 : 0;
    *(unsigned int *)(v_rip + 6744828) = (unsigned int)(a2);
    a3 = 0;
    a1 = 0;
    result = PopSetHiberPersistedRegValue(a1, a2, a3, v_stack_m714);
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = PopHibernateEvaluation(a1, a2, a3, v_stack_m714);
    result = PopReleasePolicyLock(a1, a2, a3, v_stack_m714);
    result = PopReleaseTransitionLock((unsigned int)((unsigned int)(v_r12 + 3)), a2, a3, v_stack_m714);
loc_0095662C:
    goto loc_00957EB4;
loc_00956633:
    if (v_stack_m6F8 != 0) goto loc_00956646;
    if (v_r12 == 0) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956674;
loc_00956646:
    if (((unsigned int)(v_r13)) < 24) goto loc_009563C3;
    result = PopApplyAdminPolicy((unsigned int)((unsigned int)(v_r12 + 3)), v_stack_m6F8, a3, v_stack_m714);
    if (sign_flag) goto loc_00956CA7;
    result = PopResetCurrentPolicies((unsigned int)((unsigned int)(v_r12 + 3)), v_stack_m6F8, a3, v_stack_m714);
    if (sign_flag) goto loc_00956CA7;
loc_00956674:
loc_0095667B:
    v_stack_m708 = v_rip + 5990021;
    v_stack_m714 = 24;
    goto loc_00957EBD;
loc_0095668D:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    goto loc_00956395;
loc_009566AB:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    v_stack_m708 = v_rip + 2074364;
    v_stack_m714 = 280;
    goto loc_00957EBD;
loc_009566D6:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    v_stack_m684 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5985654)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 5985649))) - (*(unsigned int *)(v_rip + 5985639)));
    v_stack_m680 = a1;
    v_stack_m67C = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5312826)));
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 16;
    goto loc_00957EBD;
loc_0095672F:
    if (((unsigned int)(v_r14)) > 18) goto loc_00956839;
    if (((unsigned int)(v_r14)) == 18) goto loc_00957852;
    v_rsi = (unsigned int)((v_r14) - (13));
    if (condition_is_equal) goto loc_00957852;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_0095681E;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_009567F3;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_009567A6;
    if (((unsigned int)(v_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (((unsigned int)(v_r13)) < 16) goto loc_009563C3;
    if ((*(unsigned __int64 *)(v_rip + 5988214)) == v_r12) goto loc_00956795;
    if ((*(unsigned __int64 *)(v_stack_m6F8)) != 0) goto loc_00956C9F;
loc_00956795:
    *(unsigned __int64 *)(v_rip + 5988191) = v_xmm0;
    goto loc_00957EBD;
loc_009567A6:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    if ((*(unsigned int *)(v_rip + 4895289)) != ((unsigned int)(v_stack_m6F8))) {
    }
    if ((*(unsigned int *)(v_rip + 4895225)) != 0) {
    }
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 4;
    goto loc_00957EBD;
loc_009567F3:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
loc_0095680C:
    v_stack_m708 = v_rip + 5985684;
    v_stack_m714 = 8;
    goto loc_00957EBD;
loc_0095681E:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    goto loc_0095680C;
loc_00956839:
    v_rsi = (unsigned int)((v_rsi) - (19));
    if (condition_is_equal) goto loc_00957852;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
    if (((unsigned int)(v_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    result = PopLoggingInformation(v_stack_m6D0, v_stack_m6D8, a3, v_stack_m714);
    if (sign_flag) goto loc_00956CA7;
    v_stack_m708 = v_stack_m6D0;
    v_stack_m714 = (unsigned int)((unsigned int)(v_stack_m6D8));
    goto loc_00957EBD;
loc_009568B7:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (((unsigned int)(v_r13)) < 8) goto loc_009563C3;
    a4 = 0;
    a3 = 0;
    result = PopLogSleepDisabled((unsigned int)(*(unsigned int *)(v_stack_m6F8)), (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 4)), a3, a4);
    goto loc_00957EB0;
loc_009568EA:
    if (((unsigned int)(v_r14)) > 38) goto loc_00956C65;
    if (((unsigned int)(v_r14)) == 38) goto loc_00956C31;
    if (((unsigned int)(v_r14)) > 32) goto loc_00956AAE;
    if (((unsigned int)(v_r14)) == 32) goto loc_00957852;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - (25));
    if (condition_is_equal) goto loc_009569DE;
    a2 = (unsigned int)((a2) - (3));
    if (condition_is_equal) goto loc_009569C4;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00956967;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_0095692F;
    if (((unsigned int)(a2)) != 1) goto loc_00956C9F;
loc_0095692F:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (((unsigned int)(v_r13)) < 8) goto loc_009563C3;
    if (((unsigned int)(v_r14)) != 30) goto loc_0095695D;
    result = PopDiagTraceAppPowerMessage(v_stack_m6F8, a2, a3, a4);
    goto loc_00957EBD;
loc_0095695D:
    result = PopDiagTraceAppPowerMessageEnd(v_stack_m6F8, a2, a3, a4);
    goto loc_00957EBD;
loc_00956967:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    v_stack_m714 = 4;
    result = ExAllocatePool2(256, v_stack_m6F8 + 4, (unsigned int)(0x206D654DULL), a4);
    v_stack_m708 = result;
    if (result != 0) goto loc_009569A9;
loc_0095699F:
    goto loc_009563C8;
loc_009569A9:
    v_stack_m70F = 1;
    *(unsigned int *)(v_stack_m708) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5312664)));
    goto loc_00957EBD;
loc_009569C4:
    result = PopSuspendResumePdc((unsigned int)(*(unsigned int *)(v_rip + 5312664)), v_stack_m6F8 + 4, (unsigned int)(0x206D654DULL), a4);
    *(unsigned __int8 *)(v_rip + 5312641) = 1;
    result = PoPowerOffMonitor(1, v_stack_m6F8 + 4, (unsigned int)(0x206D654DULL), a4);
    goto loc_009574C4;
loc_009569DE:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (v_stack_m718 != 0) goto loc_00956C9F;
    if (((unsigned int)(v_r13)) < 28) goto loc_00956C9F;
    v_stack_m6D8 = v_stack_m6F8 + 24;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m6F8 + 24))) == 0) goto loc_00956C9F;
    v_stack_m6F0 = v_stack_m6F8 + 20;
    if ((*(unsigned int *)(v_stack_m6F8 + 20)) > 2) goto loc_00956C9F;
    if ((*(unsigned int *)(v_stack_m6F8)) == 1) goto loc_00956A3E;
    goto loc_00956CA7;
loc_00956A3E:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m6F8 + 24))) + (28));
    a1 = (unsigned int)((1) | (0xFFFFFFFFULL));
    if (((unsigned int)(result)) >= 28) { a1 = (unsigned int)(result); }
    v_stack_m714 = a1;
    v_rbx = (unsigned int)(((unsigned int)(0xC0000058ULL)) & (0xC0000095ULL));
    if (((unsigned int)(result)) < 28) goto loc_00956CA7;
    if (((unsigned int)(v_r13)) < a1) goto loc_00956C9F;
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_stack_m6F8 + 20, (unsigned int)(0x206D654DULL), a4);
    v_stack_m748 = v_stack_m6F8 + 28;
    result = PopSetPowerSettingValue(v_stack_m6F8 + 4, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(v_stack_m6F0)), (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
    goto loc_00957EB0;
loc_00956AAE:
    v_rsi = (unsigned int)((v_r14) - (33));
    if (condition_is_equal) goto loc_00957852;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00956BB9;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00956B38;
    if (((unsigned int)(v_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (v_stack_m710 == ((unsigned __int8)(v_stack_m6F8 + 4))) goto loc_00956AF9;
loc_00956AEF:
    goto loc_009563C8;
loc_00956AF9:
    if (((unsigned int)(v_r13)) >= 4) goto loc_00956B06;
    goto loc_00956B20;
loc_00956B06:
    v_r13 = (unsigned int)((v_r13) + (-4));
    a3 = 0;
    result = RtlStringCbLengthW(v_stack_m6F8 + 4, (unsigned int)((unsigned int)(v_r13)), a3, (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!sign_flag) { v_rbx = 0; }
loc_00956B20:
    if (sign_flag) goto loc_00956CA7;
    result = PopDiagTraceServiceNotification(v_stack_m6F8, (unsigned int)((unsigned int)(v_r13)), a3, (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
    goto loc_00957EBD;
loc_00956B38:
    if (v_r12 == 0) goto loc_00956C9F;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5985273))) == 0) goto loc_00956BAF;
    if ((*(unsigned __int64 *)(v_rip + 5985253)) == 0) goto loc_00956BAF;
    v_stack_m714 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5985273)) + 8);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5985273)) + 8)), (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
    if (result == 0) goto loc_0095699F;
    v_stack_m708 = result;
    v_stack_m70F = 1;
    result = memcpy(result + 8, *(unsigned __int64 *)(v_rip + 5985182), (unsigned int)(*(unsigned int *)(v_rip + 5985201)), (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 5985179))) >> (4));
    *(unsigned int *)(result) = (unsigned int)(result);
    goto loc_00957EBD;
loc_00956BAF:
    goto loc_009563C8;
loc_00956BB9:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    if ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 5985182)) != 0) {
        result = PopReleasePolicyLock(result + 8, *(unsigned __int64 *)(v_rip + 5985182), (unsigned int)(*(unsigned int *)(v_rip + 5985201)), (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
        v_stack_m700 = 0;
    }
    a1 = 0;
    result = PopGetWakeSource(a1, v_stack_m714, (unsigned int)(*(unsigned int *)(v_rip + 5985201)), (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_0095662C;
    result = ExAllocatePool2(64, (unsigned int)(v_stack_m714), (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
    v_stack_m708 = result;
    if (result == 0) goto loc_0095699F;
    v_stack_m70F = 1;
    result = PopGetWakeSource(result, v_stack_m714, (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
loc_00956C2A:
    goto loc_0095662C;
loc_00956C31:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (((unsigned int)(v_r13)) != 8) goto loc_00956C4B;
    result = PpmSetSimulatedLoad(v_stack_m6F8, v_stack_m714, (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
    goto loc_00956C2A;
loc_00956C4B:
    if (((unsigned int)(v_r13)) != 4) goto loc_00956C5B;
    result = PpmClearSimulatedLoad(v_stack_m6F8, v_stack_m714, (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
    goto loc_00956C2A;
loc_00956C5B:
    goto loc_0095662C;
loc_00956C65:
    if (((unsigned int)(result)) > 44) goto loc_00957091;
    if (((unsigned int)(result)) == 44) goto loc_00957068;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) - (39));
    if (condition_is_equal) goto loc_0095703D;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00956FFC;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00956E46;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00956D09;
    if (((unsigned int)(a2)) == 1) goto loc_00957779;
loc_00956C9F:
loc_00956CA2:
loc_00956CA7:
    if (v_stack_m6D0 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m6D0, a2, (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
    }
    if (v_stack_m70F != 0) {
        a2 = 0x206D654DULL;
        a1 = v_stack_m708;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
    }
    if (v_stack_m700 != 0) {
        result = PopReleasePolicyLock(a1, a2, (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
    }
    if (v_stack_m6F8 == 0) goto loc_00956D01;
    if (v_stack_m6F8 == v_r14) goto loc_00956D01;
    result = v_stack_m88;
    if (v_stack_m6F8 != v_stack_m88) {
        a2 = 0x206D654DULL;
        a1 = v_stack_m6F8;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
    }
    goto loc_00957F27;
loc_00956D09:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((unsigned int)(v_r13)) != 16) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if ((*(unsigned __int8 *)(v_stack_m6F8 + 13)) == 0) goto loc_00956DEB;
    if ((*(unsigned __int8 *)(v_stack_m6F8 + 12)) == 0) goto loc_00956DEB;
    result = PopIsPlatformAoAcCapable(a1, a2, (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(v_stack_m6D8)));
    if ((unsigned __int8)(result) == 0) goto loc_00956DB5;
    if ((*(unsigned int *)(v_rip + 5311763)) != ((unsigned int)(v_r12))) goto loc_00956DB5;
    if ((*(unsigned int *)(v_stack_m6F8 + 4)) != 2) goto loc_00956DBC;
    v_stack_m6A4 = 0;
    v_stack_m69C = 0;
    v_stack_m6C0 = a1;
    v_stack_m6BC = 40;
    v_stack_m6B8 = 0;
    v_stack_m6B0 = 0;
    v_stack_m6A8 = 0;
    v_stack_m738 = v_stack_m6C0;
    v_stack_m740 = 0;
    v_stack_m748 = (unsigned int)(*(unsigned int *)(v_stack_m6F8));
    result = DbgkWerCaptureLiveKernelDump2(v_rip + 1748626, 160, (unsigned int)(0x801ULL), (int)(*(unsigned int *)(v_stack_m6F8 + 8)));
loc_00956DB5:
    if ((*(unsigned int *)(v_stack_m6F8 + 4)) != 2) {
        a2 = *(unsigned int *)(v_stack_m6F8 + 8);
        a1 = *(unsigned __int8 *)(v_stack_m6F8 + 15);
        result = PopProcessSessionDisplayStateChange(a1, a2, (unsigned int)(0x801ULL), (int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    }
    result = PopSetDisplayStatus((unsigned int)(*(unsigned int *)(v_stack_m6F8 + 4)), a2, (unsigned int)(0x801ULL), (int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    result = PopUpdateConsoleDisplayState((unsigned int)(*(unsigned int *)(v_stack_m6F8 + 4)), a2, (unsigned int)(0x801ULL), (int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    if ((*(unsigned int *)(v_stack_m6F8 + 4)) == 1) {
        result = PopPowerAggregatorNotifyDisplayPoweredOn(1, a2, (unsigned int)(0x801ULL), (int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    }
    if ((*(unsigned __int8 *)(v_stack_m6F8 + 14)) == 0) goto loc_00957EBD;
    if ((*(unsigned __int8 *)(v_stack_m6F8 + 12)) != 0) {
        a2 = v_stack_m6F8 + 4;
        v_stack_m738 = 0;
        v_stack_m740 = 0;
        v_stack_m748 = 0;
        a4 = 0;
        a3 = a4 + 4;
        a1 = v_rip - 9659186;
        result = ZwUpdateWnfStateData(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_stack_m6F8 + 14)) == 0) goto loc_00957EBD;
    a1 = ((*(unsigned int *)(v_stack_m6F8 + 4)) == 0) ? 1 : 0;
    result = PopDiagTraceSessionDisplayStateChange(a1, (unsigned int)(*(unsigned int *)(v_stack_m6F8)), *(unsigned __int8 *)(v_stack_m6F8 + 12), (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    goto loc_00957EBD;
loc_00956E46:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 64) goto loc_00956C9F;
    result = PopAcquireRwLockExclusive(v_rip + 5969362, (unsigned int)(*(unsigned int *)(v_stack_m6F8)), *(unsigned __int8 *)(v_stack_m6F8 + 12), (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    result = PopReleaseRwLock(v_rip + 5969343, (unsigned int)(*(unsigned int *)(v_stack_m6F8)), *(unsigned __int8 *)(v_stack_m6F8 + 12), (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    result = v_stack_m658;
    if (((unsigned int)(*(unsigned __int64 *)(v_rip + 5311406))) == ((unsigned int)(v_stack_m6F8 + 1))) { result = (unsigned int)(v_stack_m6F8 + 1); }
    v_stack_m658 = (unsigned __int8)(result);
    result = TtmIsEnabled(v_stack_m6F8 + 1, (unsigned int)(*(unsigned int *)(v_stack_m6F8)), *(unsigned __int8 *)(v_stack_m6F8 + 12), (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    v_stack_m650 = (unsigned __int8)(result);
    result = TtmIsEnabled(v_stack_m6F8 + 1, (unsigned int)(*(unsigned int *)(v_stack_m6F8)), *(unsigned __int8 *)(v_stack_m6F8 + 12), (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    if ((unsigned __int8)(result) == 0) goto loc_00956ECE;
    result = TtmInitCurrentSession(v_stack_m6F8 + 1, (unsigned int)(*(unsigned int *)(v_stack_m6F8)), *(unsigned __int8 *)(v_stack_m6F8 + 12), (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    v_stack_m70C = (unsigned int)(result);
    if (sign_flag) goto loc_00956CA7;
    result = PopPowerRequestNotifyTtmSessionInitialized(v_stack_m6F8 + 1, (unsigned int)(*(unsigned int *)(v_stack_m6F8)), *(unsigned __int8 *)(v_stack_m6F8 + 12), (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
loc_00956ECE:
    result = PopAcquirePolicyLock(v_stack_m6F8 + 1, (unsigned int)(*(unsigned int *)(v_stack_m6F8)), *(unsigned __int8 *)(v_stack_m6F8 + 12), (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    v_stack_m678 = 0;
    v_stack_m688 = v_rip + 5986323;
    v_stack_m680 = v_rip + 5311333;
    a1 = ((*(unsigned __int8 *)(v_rip + 5988112)) != 0) ? 1 : 0;
    v_stack_m670 = a1;
    v_stack_m66C = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5988091)));
    v_stack_m674 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5988110)));
    v_stack_m668 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5988101)));
    v_stack_m664 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5988092)));
    v_stack_m660 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5988083)));
    v_stack_m654 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5988074)));
    v_stack_m65C = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5988065)));
    v_stack_m657 = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 4933133));
loc_00956F80:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4933104))))) | (0));
    if (condition_is_not_equal) goto loc_00956F80;
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 64;
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), (unsigned int)(*(unsigned int *)(v_stack_m6F8)), *(unsigned __int8 *)(v_stack_m6F8 + 12), (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    result = PopPrintEx(3, v_rip + 1753410, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    a3 = 0;
    result = PopDiagTraceSessionState(v_rip - 9721324, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    result = PopReleasePolicyLock(v_rip - 9721324, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    goto loc_00957EC2;
loc_00956FFC:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 4) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    result = ((*(unsigned int *)(v_stack_m6F8)) != 0) ? 1 : 0;
    v_stack_m6F0 = (unsigned int)(result);
    result = PopSetPowerSettingValueAcDc(v_rip - 9678075, (unsigned int)((unsigned int)((unsigned int)(v_stack_m718))), v_stack_m6F0, (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    goto loc_00957EBD;
loc_0095703D:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 24) goto loc_00956C9F;
    result = PopShutdownListenerInsertCallback(v_stack_m6F8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m718))), v_stack_m6F0, (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
loc_00957061:
    goto loc_00957EBD;
loc_00957068:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 24) goto loc_009563C3;
    result = PopPowerRequestActionInfo(v_stack_m6F8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m718))), v_stack_m6F0, (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    goto loc_00957EB0;
loc_00957091:
    v_rsi = (unsigned int)((v_r14) - (45));
    if (condition_is_equal) goto loc_00957189;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957140;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957108;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_not_equal) goto loc_00957849;
    if ((*(unsigned __int8 *)(v_rip + 6227264)) == ((unsigned __int8)(v_rsi))) goto loc_00956AEF;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 16) goto loc_009570DA;
    a2 = 0;
    goto loc_009570E4;
loc_009570DA:
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 24) goto loc_009570F1;
loc_009570E4:
    result = PpmParkApplyForcedMask(v_stack_m6F8, v_stack_m6F8 + 16, v_stack_m6F0, (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    goto loc_00956C2A;
loc_009570F1:
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 2) goto loc_00956C5B;
    result = PpmParkClearForcedMask(v_stack_m6F8, v_stack_m6F8 + 16, v_stack_m6F0, (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    goto loc_00956C2A;
loc_00957108:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 16) goto loc_00956C9F;
    result = PopUmpoSendLegacyEvent(v_stack_m6F8, v_stack_m6F8 + 16, v_stack_m6F0, (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    if (!sign_flag) goto loc_00957EBD;
    if (((unsigned int)(result)) != 0xC0000120ULL) goto loc_00956CA7;
    goto loc_00957EBD;
loc_00957140:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) < 2) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    result = KeQueryActiveGroupCount(v_stack_m6F8, v_stack_m6F8 + 16, v_stack_m6F0, (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)));
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m6F8))) >= ((unsigned __int16)(result))) goto loc_00956C9F;
    result = PopProcessorInformation(v_stack_m688, v_stack_m6F8 + 16, (unsigned __int16)(*(unsigned __int16 *)(v_stack_m6F8)), v_stack_m714);
    goto loc_009565AF;
loc_00957189:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    result = PopGetPowerRequestListInfo(v_stack_m708, v_stack_m714, (unsigned __int16)(*(unsigned __int16 *)(v_stack_m6F8)), v_stack_m714);
loc_009571AA:
    if (sign_flag) goto loc_00956CA7;
    v_stack_m70F = 1;
    goto loc_00957EBD;
loc_009571C5:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    result = ExGetWakeTimerList(v_stack_m708, v_stack_m714, (unsigned __int16)(*(unsigned __int16 *)(v_stack_m6F8)), v_stack_m714);
    goto loc_009571AA;
loc_009571E8:
    if (((unsigned int)(v_r14)) > 75) goto loc_00957817;
    if (((unsigned int)(v_r14)) == 75) goto loc_009577F4;
    if (((unsigned int)(v_r14)) > 63) goto loc_0095756B;
    if (((unsigned int)(v_r14)) == 63) goto loc_009574FB;
    if (((unsigned int)(v_r14)) > 57) goto loc_0095735E;
    if (((unsigned int)(v_r14)) == 57) goto loc_00957852;
    v_rsi = (unsigned int)((v_r14) - (51));
    if (condition_is_equal) goto loc_009572F0;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_009572A7;
    if (((unsigned int)(v_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 8) goto loc_009563C3;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 4) goto loc_009563C3;
    result = PpmParkSetLpiCap((unsigned int)(*(unsigned int *)(v_stack_m6F8)), (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 4)), v_stack_m688, v_stack_m714);
    if (sign_flag) goto loc_009563C8;
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = (unsigned int)((unsigned int)(v_stack_m718));
    goto loc_00957EC2;
loc_009572A7:
    if ((*(unsigned __int8 *)(v_rip + 6226762)) == 0) goto loc_00956AEF;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 8) goto loc_009572D9;
    result = PpmSetSimulatedIdle(v_stack_m6F8, (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 4)), v_stack_m688, v_stack_m714);
    goto loc_00956C2A;
loc_009572D9:
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 4) goto loc_00956C5B;
    result = PpmClearSimulatedIdle(v_stack_m6F8, (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 4)), v_stack_m688, v_stack_m714);
    goto loc_00956C2A;
loc_009572F0:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) < 4) goto loc_009563C3;
    result = PopAcquireTransitionLock(5, (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 4)), v_stack_m688, v_stack_m714);
    result = PopAcquirePolicyLock(5, (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 4)), v_stack_m688, v_stack_m714);
    result = PopSetHiberFileSize((unsigned int)(*(unsigned int *)(v_stack_m6F8)), v_stack_m6E0, v_stack_m6F0, v_stack_m714);
    result = PopReleasePolicyLock((unsigned int)(*(unsigned int *)(v_stack_m6F8)), v_stack_m6E0, v_stack_m6F0, v_stack_m714);
loc_0095733C:
    result = PopReleaseTransitionLock(5, v_stack_m6E0, v_stack_m6F0, v_stack_m714);
    if (sign_flag) {
        result = v_stack_m6F0;
        v_stack_m6E0 = result;
    }
    goto loc_0095680C;
loc_0095735E:
    v_rsi = (unsigned int)((v_rsi) - (58));
    if (condition_is_equal) goto loc_009574CB;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_0095748D;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957464;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_0095742F;
    if (((unsigned int)(v_rsi)) != 1) goto loc_00956C9F;
    result = Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline(5, v_stack_m6E0, v_stack_m6F0, v_stack_m714);
    if ((unsigned int)(result) != 0) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 40) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 16) goto loc_00956C9F;
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_stack_m6E0, v_stack_m6F0, v_stack_m714);
    result = PopSessionConnectionChange((unsigned int)((unsigned int)(result)), v_stack_m6F8, v_r12, v_stack_m714);
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_stack_m6F8, v_r12, v_stack_m714);
    result = Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_stack_m6F8, v_r12, v_stack_m714);
    result = *(unsigned __int64 *)(v_rip + 5309314);
    if (*(unsigned __int64 *)(v_rip + 5309314) != 0) {
        a4 = v_rsi + 2;
        a1 = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = guard_dispatch_icall(a1, *(unsigned __int8 *)(v_stack_m6F8 + 1), *(unsigned __int8 *)(v_stack_m6F8), a4);
    }
    goto loc_00957EC2;
loc_0095742F:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 16) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 8) goto loc_00956C9F;
    goto loc_00957EC2;
loc_00957464:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) < 8) goto loc_009563C3;
    result = PopEnforceResiliencyScenarios(v_stack_m6F8, *(unsigned __int8 *)(v_stack_m6F8 + 1), *(unsigned __int8 *)(v_stack_m6F8), a4);
    goto loc_00957EBD;
loc_0095748D:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 16) goto loc_009563C3;
    if (((unsigned int)((unsigned int)(v_stack_m718))) < 4) goto loc_009563C3;
    result = PopGetSettingValue(v_stack_m6F8, v_r12, (unsigned int)((unsigned int)((unsigned int)(v_stack_m718))), a4);
loc_009574C4:
    goto loc_009563C8;
loc_009574CB:
    if (v_r12 == 0) goto loc_00956C9F;
    if (v_r14 == 0) goto loc_009574E3;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 20) goto loc_009563C3;
loc_009574E3:
    if (v_stack_m718 != 8) goto loc_009563C3;
    result = PopGetSettingNotificationName(v_stack_m6F8, v_r12, (unsigned int)((unsigned int)((unsigned int)(v_stack_m718))), a4);
    goto loc_009574C4;
loc_009574FB:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_r12, (unsigned int)((unsigned int)((unsigned int)(v_stack_m718))), a4);
    result = PopPrintEx(v_stack_m6F8 + 3, v_rip + 1752098, (unsigned int)((unsigned int)(result)), a4);
    a3 = 0;
    result = PopDiagTraceSessionState(v_rip - 9722715, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, a4);
    result = PopFreeSessionState((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, a4);
    result = TtmIsEnabled((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00956347;
    result = PopPowerRequestNotifyTtmSessionUninitialized((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, a4);
    result = TtmCleanupCurrentSession((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, a4);
    goto loc_00956347;
loc_0095756B:
    if (((unsigned int)(v_rsi)) > 69) goto loc_00957710;
    if (((unsigned int)(v_rsi)) == 69) goto loc_009576E7;
    v_rsi = (unsigned int)((v_rsi) - (64));
    if (condition_is_equal) goto loc_0095769E;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_0095763F;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_0095760B;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_009575D2;
    if (((unsigned int)(v_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 8) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (v_stack_m718 != 0) goto loc_00956C9F;
    result = PopMonitorInvocation(v_stack_m6F8, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, a4);
    goto loc_009574C4;
loc_009575D2:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 224) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_009575FB;
    if (v_stack_m718 != 168) goto loc_00956C9F;
loc_009575FB:
    result = PopPdcInvocation(v_stack_m6F8, v_r12, a3, a4);
    goto loc_009574C4;
loc_0095760B:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    result = PopIsPlatformAoAcCapable(v_stack_m6F8, v_r12, a3, a4);
    v_stack_m688 = (unsigned __int8)(result);
loc_00957631:
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = (unsigned int)(v_stack_m6F8);
    goto loc_00957EBD;
loc_0095763F:
    result = PsIsCurrentThreadInServerSilo(v_stack_m6F8, v_r12, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00957652;
loc_00957648:
    goto loc_009563C8;
loc_00957652:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    result = PopFilterCapabilities(v_rip + 5986381, v_stack_m688, a3, a4);
    if (v_stack_m676 != 0) {
        a1 = v_stack_m676;
        result = PopReadHiberbootPolicy(a1, v_stack_m688, a3, a4);
    }
    goto loc_00957631;
loc_0095769E:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 8) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_stack_m688, a3, a4);
    result = PopSessionWinlogonNotification((unsigned int)((unsigned int)(result)), v_stack_m6F8, a3, a4);
    goto loc_00957EBD;
loc_009576E7:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    result = PopInitPlatformSettings((unsigned int)((unsigned int)(result)), v_stack_m6F8, a3, a4);
    result = PopIsPlatformAoAcCapable((unsigned int)((unsigned int)(result)), v_stack_m6F8, a3, a4);
    *(unsigned __int8 *)(v_rip + 5986249) = (unsigned __int8)(result);
    goto loc_009563C8;
loc_00957710:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) - (70));
    if (condition_is_equal) goto loc_009577E1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00957648;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00957779;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00957CDD;
    if (a1 != 1) goto loc_00956C9F;
    if (v_stack_m710 != 0) goto loc_00956AEF;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 16) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (v_stack_m718 != 0) goto loc_00956C9F;
    result = PopPdcCsDeviceNotification(v_stack_m6F8, v_stack_m6F8, a3, a4);
    goto loc_009574C4;
loc_00957779:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 40) goto loc_009563C3;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 8) goto loc_009563C3;
    a2 = (((unsigned int)(v_rsi)) == 72) ? 1 : 0;
    result = PopPowerRequestCreateUserModeRequest(v_stack_m6F8, a2, v_stack_m688, a4);
loc_009577BA:
    if (sign_flag) goto loc_00956CA7;
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 8;
    goto loc_00957EC2;
loc_009577E1:
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, v_stack_m688, a4);
    *(unsigned __int64 *)(v_rip + 5992353) = result;
    goto loc_00957EBD;
loc_009577F4:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    result = PopCapturePlatformRole(a1, a2, v_stack_m688, a4);
    v_stack_m688 = (unsigned int)(result);
    goto loc_009567D9;
loc_00957817:
    if (((unsigned int)(v_r14)) > 87) goto loc_00957B8E;
    if (((unsigned int)(v_r14)) == 87) goto loc_00957AA9;
    if (((unsigned int)(v_r14)) > 81) goto loc_0095799A;
    if (((unsigned int)(v_r14)) == 81) goto loc_00957852;
    v_rsi = (unsigned int)((v_r14) - (76));
    if (condition_is_equal) goto loc_0095793D;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_0095789F;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_0095785C;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
loc_00957849:
    if (((unsigned int)(v_rsi)) != 1) goto loc_00956C9F;
loc_00957852:
    goto loc_009563C8;
loc_0095785C:
    if (v_stack_m710 != 0) goto loc_00956AEF;
    if (v_r12 != 0) goto loc_00956C9F;
    if (v_stack_m718 != 0) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00957895;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 4) goto loc_00956C9F;
    result = PpmSetExitLatencySamplingPercentage(v_stack_m6F8, a2, v_stack_m688, a4);
    goto loc_00957061;
loc_00957895:
    result = PpmClearExitLatencySamplingPercentage(v_stack_m6F8, a2, v_stack_m688, a4);
    goto loc_00957EBD;
loc_0095789F:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    result = TtmIsEnabled(v_stack_m6F8, a2, v_stack_m688, a4);
    if ((unsigned __int8)(result) == 0) goto loc_009578F9;
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, v_stack_m688, a4);
    a1 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) | (0xFFFFFFFFULL));
    if (((unsigned int)(result)) == a1) goto loc_009578EF;
    result = TtmNotifySessionDisplayBurst((unsigned int)((unsigned int)(result)), v_stack_m6F8 + 6, v_stack_m688, a4);
    goto loc_0095634B;
loc_009578EF:
    goto loc_0095634B;
loc_009578F9:
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 4930677)) == 0) {
        a1 = 1;
        v_rsi = 0;
        if ((*(unsigned __int8 *)(v_rip + 5308743)) == 0) { v_rsi = a1; }
    }
    if ((unsigned __int8)(v_rsi) == 0) {
        a2 = 6;
        a1 = a2 + 4;
        result = PopEventCalloutDispatch(a1, a2, v_stack_m688, a4);
    }
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 5308800)) != 0) goto loc_00957EBD;
    result = PopDiagTraceDisplayBurstWin32kCallout(a1, a2, (unsigned __int8)(v_rsi), a4);
    goto loc_00957EBD;
loc_0095793D:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    v_stack_m688 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5982843)));
    v_stack_m680 = *(unsigned __int64 *)(v_rip + 5983261);
    v_stack_m678 = *(unsigned __int64 *)(v_rip + 5983254);
    if ((*(unsigned __int8 *)(v_rip + 5982591)) != ((unsigned __int8)(v_stack_m6F8))) goto loc_0095798D;
    goto loc_009563C8;
loc_0095798D:
    goto loc_0095667B;
loc_0095799A:
    v_rsi = (unsigned int)((v_rsi) - (82));
    if (condition_is_equal) goto loc_00957852;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957A83;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957A45;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957A24;
    if (((unsigned int)(v_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    a3 = 0;
    result = RtlStringCbLengthW(v_stack_m6F8, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))), a3, a4);
    if (sign_flag) goto loc_00956CA7;
    result = PopBatteryDeviceState(v_stack_m6F8, v_stack_m688, a3, a4);
    if (sign_flag) goto loc_00956CA7;
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 52;
    goto loc_00957EBD;
loc_00957A24:
    if ((*(unsigned __int8 *)(v_stack_m6F8 + 12)) == 0) goto loc_00957A3B;
    result = PopPowerRequestReferenceAcquire(*(unsigned __int64 *)(v_stack_m6F8), (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)), a3, a4);
    goto loc_00957061;
loc_00957A3B:
    result = PopPowerRequestReferenceRelease(*(unsigned __int64 *)(v_stack_m6F8), (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)), a3, a4);
    goto loc_00957061;
loc_00957A45:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))) < 16) goto loc_009563C3;
    if (((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))) < ((unsigned int)(*(unsigned __int16 *)(v_stack_m6F8 + 12) * 2 + 14))) goto loc_009563C3;
    result = PopThermalProcessUsermodeEvent(v_stack_m6F8, (unsigned int)(*(unsigned int *)(v_stack_m6F8 + 8)), a3, a4);
    goto loc_00957EB0;
loc_00957A83:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    a2 = 0;
    result = PopCurrentPowerStatePrecise(v_stack_m688, a2, a3, a4);
    goto loc_0095625E;
loc_00957AA9:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))) < 8) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m6F8)) - 100)) <= 0xF9BULL) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m6F8)))) >= 0x100BULL) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m6F8)) - 4096)) > 10) goto loc_00957B51;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 6823997), v_stack_m710, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00957B16;
    result = PopCapabilityCheck(v_rip + 1745277, v_stack_m710, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00957B16;
    goto loc_009563C8;
loc_00957B16:
    v_stack_m730 = v_stack_m70F;
    v_stack_m738 = v_stack_m714;
    v_stack_m740 = v_stack_m708;
    v_stack_m748 = (unsigned int)((unsigned int)(v_stack_m718));
    result = TtmDispatchApi((unsigned int)((unsigned int)((unsigned int)(0xC0000061ULL))), v_stack_m6F8, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))), v_r12);
    goto loc_00956C2A;
loc_00957B51:
    v_stack_m728 = v_stack_m70F;
    v_stack_m730 = v_stack_m714;
    v_stack_m738 = v_stack_m708;
    v_stack_m740 = (unsigned int)((unsigned int)(v_stack_m718));
    v_stack_m748 = v_r12;
    result = PopPowerInformationInternal((unsigned int)((unsigned int)((unsigned int)(0xC0000061ULL))), v_stack_m6F8, v_stack_m6F8, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    goto loc_00956C2A;
loc_00957B8E:
    if (((unsigned int)(v_r14)) > 93) goto loc_00957D53;
    if (((unsigned int)(v_r14)) == 93) goto loc_00957D08;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - (88));
    if (condition_is_equal) goto loc_00957CDD;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00957C8C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00957C60;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00957C08;
    if (a1 != 1) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    if (((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))) != 12) goto loc_009563C3;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 8) goto loc_009563C3;
    result = PopEtEnergyTrackerCreate(v_stack_m6F8, v_stack_m688, v_stack_m6F8, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    goto loc_009577BA;
loc_00957C08:
    result = PopIsPlatformAoAcCapable(v_stack_m6F8, v_stack_m688, v_stack_m6F8, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    if ((unsigned __int8)(result) == 0) goto loc_00957648;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 336) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    result = PopFxIsDevicePotentialDripsConstraint(v_stack_m6F8, v_stack_m688, v_stack_m6F8, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    v_stack_m688 = (unsigned __int8)(result);
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 1;
    goto loc_00957EBD;
loc_00957C60:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) < 4) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    a1 = ((*(unsigned int *)(v_stack_m6F8)) != 0) ? 1 : 0;
    result = PopUpdatePowerButtonHoldState(a1, v_stack_m688, v_stack_m6F8, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    goto loc_00957EBD;
loc_00957C8C:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) < 4) goto loc_009563C3;
    result = PopAcquireTransitionLock(6, v_stack_m688, v_stack_m6F8, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    result = PopAcquirePolicyLock(6, v_stack_m688, v_stack_m6F8, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    result = PopSetHiberFileType((unsigned int)(*(unsigned int *)(v_stack_m6F8)), v_stack_m6E0, v_stack_m6F0, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    result = PopReleasePolicyLock((unsigned int)(*(unsigned int *)(v_stack_m6F8)), v_stack_m6E0, v_stack_m6F0, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    goto loc_0095733C;
loc_00957CDD:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    a1 = v_stack_m6F8 + 23;
    if (((unsigned int)(v_r14)) != 88) { a1 = (unsigned int)(v_stack_m6F8 + 23 - 12); }
    result = PopScreenOff(a1, v_stack_m6E0, v_stack_m6F0, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
loc_00957D01:
    goto loc_009563C8;
loc_00957D08:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 8) goto loc_009563C3;
    if (((unsigned int)((unsigned int)(v_stack_m718))) < 12) goto loc_009563C3;
    result = PopEtEnergyTrackerQuery(*(unsigned __int64 *)(v_stack_m6F8), v_r12, (unsigned int)((unsigned int)((unsigned int)(v_stack_m718))), (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    if (sign_flag) goto loc_00956CA7;
    goto loc_00957EC2;
loc_00957D53:
    v_rsi = (unsigned int)((v_r14) - (94));
    if (condition_is_equal) goto loc_00957E7E;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957E4F;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957E2A;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_00957DB5;
    if (((unsigned int)(v_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    result = PopCurrentSystemPowerSourceState(v_stack_m688, v_r12, (unsigned int)((unsigned int)((unsigned int)(v_stack_m718))), (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 68;
    goto loc_00957EBD;
loc_00957DB5:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if ((unsigned int)((unsigned int)(v_stack_m718)) == 0) goto loc_00956C9F;
    if (v_r12 == 0) goto loc_00956C9F;
    if (v_stack_m718 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) < 32) goto loc_009563C3;
    if (((unsigned int)((unsigned int)(v_stack_m718))) < 16) goto loc_009563C3;
    result = PopBlackBoxDirectAccess(v_stack_m6F8, v_stack_m688, (unsigned int)((unsigned int)((unsigned int)(v_stack_m718))), (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    if (sign_flag) goto loc_00956CA7;
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 16;
    goto loc_00957EC2;
loc_00957E2A:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) < ((unsigned int)(v_stack_m6F8))) goto loc_009563C3;
    result = PopSendSuspendResumeNotifications(*(unsigned __int8 *)(v_stack_m6F8), v_stack_m688, (unsigned int)((unsigned int)((unsigned int)(v_stack_m718))), (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    goto loc_00957EB0;
loc_00957E4F:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != ((unsigned int)(*(unsigned __int8 *)(v_stack_m6F8)))) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    a3 = 0;
    result = ExNotifyCallback(*(unsigned __int64 *)(v_rip + 6499097), v_stack_m6F8, a3, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    goto loc_00957EBD;
loc_00957E7E:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (v_r12 != 0) goto loc_00956C9F;
    if (v_stack_m718 != 0) goto loc_00956C9F;
    if (((unsigned int)((unsigned int)(v_stack_m718))) != 32) goto loc_009563C3;
    result = PopBlackBoxUpdate(v_stack_m6F8, v_stack_m710, a3, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
loc_00957EB0:
loc_00957EB4:
    if (sign_flag) goto loc_00956CA7;
loc_00957EBD:
loc_00957EC2:
    if (v_stack_m708 == 0) goto loc_00957F03;
    if (v_r12 == 0) goto loc_00957F03;
    if (((unsigned int)((unsigned int)(v_stack_m718))) < v_stack_m714) goto loc_009563C3;
    result = memcpy(v_r12, v_stack_m708, (unsigned int)(v_stack_m714), (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    goto loc_00957F03;
loc_00957F03:
    if (((unsigned int)((unsigned int)(v_stack_m6E4))) == 51) goto loc_00956CA7;
    if (((unsigned int)((unsigned int)(v_stack_m6E4))) == 89) goto loc_00956CA7;
    goto loc_00957D01;
loc_00957F27:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m708, (unsigned int)(v_stack_m714), (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rip + 5308800))));
    v_rsp = (v_rsp) + (0x730ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtPowerInformation(int32_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint8_t v_stack_m64F;
    uint8_t v_stack_m650;
    uint32_t v_stack_m654;
    uint8_t v_stack_m657;
    uint8_t v_stack_m658;
    uint32_t v_stack_m65C;
    uint32_t v_stack_m660;
    uint32_t v_stack_m664;
    uint32_t v_stack_m668;
    uint32_t v_stack_m66C;
    uint32_t v_stack_m670;
    uint32_t v_stack_m674;
    uint8_t v_stack_m676;
    uint32_t v_stack_m678;
    uint8_t v_stack_m67C;
    uint32_t v_stack_m680;
    uint32_t v_stack_m684;
    uint64_t v_stack_m688;
    uint64_t v_stack_m698;
    uint32_t v_stack_m69C;
    uint64_t v_stack_m6A4;
    uint32_t v_stack_m6A8;
    uint64_t v_stack_m6B0;
    uint64_t v_stack_m6B8;
    uint32_t v_stack_m6BC;
    uint32_t v_stack_m6C0;
    uint64_t v_stack_m6C8;
    uint64_t v_stack_m6D0;
    uint32_t v_stack_m6D8;
    uint64_t v_stack_m6E0;
    uint32_t v_stack_m6E4;
    uint8_t v_stack_m6E8;
    uint32_t v_stack_m6F0;
    uint64_t v_stack_m6F8;
    uint8_t v_stack_m6FF;
    uint8_t v_stack_m700;
    uint64_t v_stack_m708;
    uint32_t v_stack_m70C;
    uint8_t v_stack_m70F;
    uint8_t v_stack_m710;
    uint32_t v_stack_m714;
    uint32_t v_stack_m718;
    uint64_t v_stack_m728;
    uint64_t v_stack_m730;
    uint64_t v_stack_m738;
    uint64_t v_stack_m740;
    uint64_t v_stack_m748;
    uint64_t v_stack_m88;

    local_rsp = (local_rsp) - (0x730ULL);
    result = (*(uint64_t *)(v_rip + 0x4B49A6)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m6E4 = Arg1;
    local_rdi = 0;
    v_stack_m6FF = 0;
    Arg2 = 0;
    result = memset(v_stack_m688, Arg2, (uint32_t)(0x600ULL), Arg4);
    v_stack_m6D8 = 0;
    v_stack_m6E0 = 0;
    v_stack_m708 = 0;
    v_stack_m714 = 0;
    v_stack_m6F8 = 0;
    v_stack_m6D0 = 0;
    v_stack_m700 = 0;
    v_stack_m70F = 0;
    v_stack_m6F0 = 0;
    v_stack_m70C = 0;
    if (((uint32_t)((uint32_t)(Arg1))) > 98) goto loc_00956CA2;
    v_stack_m710 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = -(0);
    local_r13 = (uint32_t)(((uint32_t)(Arg1)) & ((uint32_t)((uint32_t)(Arg3))));
    result = (uint32_t)(-((uint32_t)((uint32_t)(local_r13))));
    local_r14 = ((uint32_t)(Arg3)) & (0);
    v_stack_m6C8 = local_r14;
    result = -(Arg4);
    result = (uint32_t)((result) & (Arg5));
    v_stack_m718 = (uint32_t)(result);
    result = (uint32_t)(-(result));
    local_r12 = (local_r12) & (Arg4);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00956183;
    if (((uint32_t)((int32_t)(v_stack_m6E4))) > 34) goto loc_00955E8C;
    if (((uint32_t)((int32_t)(v_stack_m6E4))) < 34) goto loc_00955EA4;
loc_00955E8C:
    if (((uint32_t)((int32_t)(v_stack_m6E4) - 39)) > 58) goto loc_00955EB6;
    if (((uint32_t)((int32_t)(v_stack_m6E4) - 39)) >= 58) goto loc_00955EB6;
loc_00955EA4:
    goto loc_00956CA7;
loc_00955EB6:
    if (((uint32_t)(local_r14 - 37)) > 58) goto loc_00955ED6;
    if (((uint32_t)(local_r14 - 37)) >= 58) goto loc_00955ED6;
    goto loc_00955EE4;
loc_00955ED6:
    if (((uint32_t)(local_r14 - 2)) > 1) goto loc_00955F62;
loc_00955EE4:
    Arg1 = 0;
    result = SeIsAppContainerOrIdentifyLevelContext(Arg1, v_stack_m6FF, (uint32_t)(0x600ULL), Arg4);
    v_stack_m70C = (uint32_t)(result);
    if (sign_flag) goto loc_00955F55;
    if (v_stack_m6FF == 0) goto loc_00955F68;
    if (((uint32_t)(local_r14)) == 73) goto loc_00955F0B;
    if (((uint32_t)(local_r14)) != 88) goto loc_00955F38;
loc_00955F0B:
    result = PopCapabilityCheck(v_rip + 1752318, v_stack_m6FF, (uint32_t)(0x600ULL), Arg4);
    v_stack_m6E8 = (uint8_t)(result);
    if ((uint8_t)(result) != 0) goto loc_00955F68;
    v_stack_m70C = (uint32_t)((uint32_t)(0xC0000022ULL));
    goto loc_00956CA7;
loc_00955F38:
    if (v_stack_m6FF == 0) goto loc_00955F68;
    v_stack_m70C = (uint32_t)((uint32_t)(0xC0000022ULL));
    goto loc_00956CA7;
loc_00955F55:
    goto loc_00956CA7;
loc_00955F62:
    goto loc_00955F6C;
loc_00955F68:
loc_00955F6C:
    if (((uint32_t)(local_r14 - 92)) > ((uint32_t)(v_stack_m6F8))) goto loc_00955F90;
    result = ExCheckFullProcessInformationAccess(v_stack_m710, v_stack_m6FF, (uint32_t)(0x600ULL), Arg4);
    v_stack_m70C = (uint32_t)(result);
    if (!sign_flag) goto loc_00955F90;
    goto loc_00956CA7;
loc_00955F90:
    if (((uint32_t)(local_r14 - 28)) > 50) goto loc_00955FC7;
    if (((uint32_t)(local_r14 - 28)) >= 50) goto loc_00955FC7;
    result = EtwpCoverageUserIsAdmin(v_stack_m710, v_stack_m6FF, (uint32_t)(0x600ULL), Arg4);
    if ((uint8_t)(result) != 0) goto loc_00955FC7;
    v_stack_m70C = (uint32_t)((uint32_t)(0xC0000022ULL));
    goto loc_00956CA7;
loc_00955FC7:
    if (((uint32_t)(local_r14)) != 71) goto loc_00955FEB;
    result = PopIsRunningAsLocalSystem(v_stack_m710, v_stack_m6FF, (uint32_t)(0x600ULL), Arg4);
    if ((uint8_t)(result) != 0) goto loc_00955FEB;
    v_stack_m70C = (uint32_t)((uint32_t)(0xC0000022ULL));
    goto loc_00956CA7;
loc_00955FEB:
    if (local_r14 == 0) goto loc_00956142;
    if (((uint32_t)(local_r14 - 11)) > 61) goto loc_0095600C;
    if (((uint32_t)(local_r14 - 11)) < 61) goto loc_0095602B;
loc_0095600C:
    result = PsIsCurrentThreadInServerSilo(v_stack_m710, v_stack_m6FF, (uint32_t)(0x600ULL), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0095602B;
    v_stack_m70C = (uint32_t)((uint32_t)(0xC00000BBULL));
    goto loc_00956CA7;
loc_0095602B:
    if (((uint32_t)(local_r14)) == 9) goto loc_00956048;
    if (((uint32_t)(local_r14 - 38)) > 57) goto loc_00956067;
    if (((uint32_t)(local_r14 - 38)) >= 57) goto loc_00956067;
loc_00956048:
    result = EtwpCoverageUserIsAdmin(v_stack_m710, v_stack_m6FF, (uint32_t)(0x600ULL), Arg4);
    if ((uint8_t)(result) != 0) goto loc_00956067;
    v_stack_m70C = (uint32_t)((uint32_t)(0xC0000022ULL));
    goto loc_00956CA7;
loc_00956067:
    if (((uint32_t)(local_r14 - 2)) <= ((uint32_t)(v_stack_m6F8))) goto loc_009560C9;
    if (((uint32_t)(local_r14 - 37)) > 61) goto loc_00956087;
    if (((uint32_t)(local_r14 - 37)) < 61) goto loc_009560C9;
loc_00956087:
    if (((uint32_t)(local_r14)) == 11) goto loc_009560C9;
    Arg1 = *(uint64_t *)(v_rip + 0x683A9D);
    if (((uint32_t)(local_r14)) == 10) { Arg1 = *(uint64_t *)(v_rip + 0x683CA2); }
    v_stack_m698 = Arg1;
    result = SeSinglePrivilegeCheck(Arg1, v_stack_m710, (uint32_t)(0x600ULL), Arg4);
    if ((uint8_t)(result) != 0) goto loc_009560C9;
    v_stack_m70C = (uint32_t)((uint32_t)(0xC0000061ULL));
    goto loc_00956CA7;
loc_009560C9:
    if ((uint32_t)(local_r13) == 0) goto loc_009560EE;
    Arg1 = ((uint32_t)((uint32_t)(local_r13))) + (local_r14);
    if (Arg1 > result) goto loc_009560E8;
    local_rbx = (uint32_t)(0xC0000061ULL);
    if (Arg1 < local_r14) {
        result = *(uint8_t *)(result);
        local_rbx = v_stack_m70C;
    }
    if (((uint32_t)(local_r13)) > 64) goto loc_00956111;
    v_stack_m6F8 = v_stack_m88;
loc_00956101:
    result = memcpy(v_stack_m88, local_r14, (uint32_t)((uint32_t)(local_r13)), Arg4);
    goto loc_00956147;
loc_00956111:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_r13)), (uint32_t)(0x206D654DULL), Arg4);
    v_stack_m6F8 = result;
    if (result != 0) goto loc_00956101;
    v_stack_m70C = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_00956CA7;
loc_00956142:
loc_00956147:
    if (local_r12 != 0) {
        Arg2 = v_stack_m718;
        Arg3 = 1;
        Arg1 = local_r12;
        result = ProbeForWrite(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_0095619B;
loc_00956183:
    v_stack_m6F8 = local_r14;
loc_0095619B:
    if (((uint32_t)((uint32_t)(v_stack_m6E4))) > 31) goto loc_009561AA;
    if (((uint32_t)((uint32_t)(v_stack_m6E4))) < 31) goto loc_009561D2;
loc_009561AA:
    if (((uint32_t)((uint32_t)(v_stack_m6E4) - 38)) > 60) goto loc_009561C2;
    result = (uint32_t)(v_stack_m6E4) - 38;
    if (((uint32_t)((uint32_t)(v_stack_m6E4) - 38)) >= 60) {
        result = PopAcquirePolicyLock(1, v_stack_m700, Arg3, Arg4);
        Arg1 = 1;
        Arg2 = (uint8_t)(Arg1);
        v_stack_m700 = (uint8_t)(Arg1);
    }
    if (((uint32_t)((uint32_t)(v_stack_m6E4))) > 50) goto loc_009571E8;
    if (((uint32_t)((uint32_t)(v_stack_m6E4))) == 50) goto loc_009571C5;
    if (((uint32_t)((uint32_t)(v_stack_m6E4))) > 24) goto loc_009568EA;
    if (((uint32_t)((uint32_t)(v_stack_m6E4))) == 24) goto loc_009568B7;
    if (((uint32_t)((uint32_t)(v_stack_m6E4))) > 12) goto loc_0095672F;
    if (((uint32_t)((uint32_t)(v_stack_m6E4))) == 12) goto loc_009566D6;
    if (((uint32_t)((uint32_t)(v_stack_m6E4))) > 6) goto loc_0095654B;
    if (((uint32_t)((uint32_t)(v_stack_m6E4))) == 6) goto loc_009563F5;
    if ((uint32_t)((uint32_t)(v_stack_m6E4)) == 0) goto loc_009563A7;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m6E4)) - (1));
    if (condition_is_equal) goto loc_009563A7;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00956355;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00956355;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00956278;
    if (((uint32_t)(local_rsi)) != 1) goto loc_00956C9F;
    if (local_r14 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    result = PopCurrentPowerState(v_stack_m688, Arg2, Arg3, Arg4);
loc_0095625E:
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 32;
    goto loc_00957EBD;
loc_00956278:
    if (local_r14 != 0) goto loc_0095628B;
    if (local_r12 == 0) goto loc_00956C9F;
    if (local_r14 == 0) goto loc_00956305;
loc_0095628B:
    if ((((uint8_t)(v_stack_m688)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5B6C7B))))) == 0) goto loc_00956C9F;
    if (((uint32_t)(local_r13)) < 76) goto loc_009563C3;
    *(uint64_t *)(v_rip + 0x5B6C12) = v_xmm0;
    *(uint64_t *)(v_rip + 0x5B6C16) = v_xmm1;
    *(uint64_t *)(v_rip + 0x5B6C1A) = v_xmm0;
    *(uint64_t *)(v_rip + 0x5B6C1E) = v_xmm1;
    *(uint64_t *)(v_rip + 0x5B6C20) = v_xmm0;
    *(uint32_t *)(v_rip + 0x5B6C1E) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x48)));
    result = PopResetCurrentPolicies(v_stack_m688, Arg2, Arg3, Arg4);
    v_stack_m70C = (uint32_t)(result);
    if (sign_flag) goto loc_00956CA7;
loc_00956305:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x5B69DD))) & (1));
    *(uint8_t *)(v_rip + 0x5B6BB6) = (uint8_t)(result);
    result = PopDisksRegisteredForIdle(1, Arg2, Arg3, Arg4);
    *(uint8_t *)(v_rip + 0x5B6BB7) = (uint8_t)(result);
    result = PopFilterCapabilities(v_rip + 5991315, v_stack_m688, Arg3, Arg4);
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 76;
loc_00956347:
loc_0095634B:
    goto loc_00957EBD;
loc_00956355:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    if (((uint32_t)(local_r13)) < 232) goto loc_009563C3;
    result = PopVerifySystemPowerPolicy(v_stack_m6F8, v_stack_m688, Arg3, Arg4);
    if (sign_flag) goto loc_00956CA7;
loc_00956395:
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 232;
    goto loc_00957EBD;
loc_009563A7:
    if (v_stack_m6F8 != 0) goto loc_009563BA;
    if (local_r12 == 0) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_009563EC;
loc_009563BA:
    if (((uint32_t)(local_r13)) >= 232) goto loc_009563D0;
loc_009563C3:
loc_009563C8:
    goto loc_00956CA7;
loc_009563D0:
    Arg2 = 0;
    Arg1 = 0;
    result = PopApplyPolicy(Arg1, Arg2, v_stack_m6F8, (uint32_t)((uint32_t)(local_r13)));
    if (sign_flag) goto loc_00956CA7;
loc_009563EC:
    goto loc_00956395;
loc_009563F5:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (((uint32_t)(local_r13)) < 24) goto loc_009563C3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m6F8)))) >= 7) goto loc_00956C9F;
    if ((*(uint64_t *)(v_rip + 0x5B681C + (uint32_t)(*(uint32_t *)(v_stack_m6F8)) + (uint32_t)(*(uint32_t *)(v_stack_m6F8)) * 2 * 8 + 0x8)) == 0) goto loc_0095644D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m6F8)))) == 5) goto loc_0095644D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m6F8)))) != 4) goto loc_00956C9F;
    if ((*(uint64_t *)(v_rip + 0x5B6861)) != (v_rip + 2208528)) goto loc_00956C9F;
loc_0095644D:
    *(uint64_t *)(v_rip + 0x5B681C + (uint32_t)(*(uint32_t *)(v_stack_m6F8)) + (uint32_t)(*(uint32_t *)(v_stack_m6F8)) * 2 * 8) = v_xmm0;
    *(uint64_t *)(v_rip + 0x5B681C + (uint32_t)(*(uint32_t *)(v_stack_m6F8)) + (uint32_t)(*(uint32_t *)(v_stack_m6F8)) * 2 * 8 + 0x10) = v_xmm1;
    *(uint16_t *)(v_rip + 0x5B681C + (uint32_t)(*(uint32_t *)(v_stack_m6F8)) + (uint32_t)(*(uint32_t *)(v_stack_m6F8)) * 2 * 8 + 0x5) = 0;
    *(uint8_t *)(v_rip + 0x5B681C + (uint32_t)(*(uint32_t *)(v_stack_m6F8)) + (uint32_t)(*(uint32_t *)(v_stack_m6F8)) * 2 * 8 + 0x7) = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m6F8))) == 0) goto loc_00956500;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m6F8))) - (1));
    if (condition_is_equal) goto loc_009564E9;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_009564D2;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_009564B9;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_009564B0;
    if (((uint32_t)(Arg2)) != 2) goto loc_00956519;
    goto loc_00956515;
loc_009564B0:
    goto loc_00956519;
loc_009564B9:
    goto loc_00956515;
loc_009564D2:
    goto loc_00956515;
loc_009564E9:
    goto loc_00956515;
loc_00956500:
loc_00956515:
    Arg3 = v_rip + 5990830;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5B6A00)))) & (8)) != 0) { Arg3 = 0; }
loc_00956519:
    result = (uint8_t)(-(*(uint8_t *)(v_rip + 0x5B681C + (uint32_t)(*(uint32_t *)(v_stack_m6F8)) + (uint32_t)(*(uint32_t *)(v_stack_m6F8)) * 2 * 8 + 0x4)));
    Arg2 = (uint32_t)((Arg2) & (2));
    if (((uint32_t)(Arg2)) >= = (*(uint32_t *)(v_rip + 0x5B69D5))) {
        *(uint32_t *)(v_rip + 0x5B69CD) = (uint32_t)(Arg2);
    }
    if (Arg3 == 0) goto loc_00957EBD;
    result = PopChangeCapability(Arg3, 0, Arg3, 2);
    goto loc_00957EBD;
loc_0095654B:
    local_rsi = (uint32_t)((local_r14) - (7));
    if (condition_is_equal) goto loc_009566AB;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_0095668D;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00956633;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_009565CE;
    if (((uint32_t)(local_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    result = KeQueryPrimaryGroupThread(*(uint64_t *)(gs_base + (0 + 0x188)), 0, Arg3, 2);
    result = PopProcessorInformation(v_stack_m688, 0, (uint16_t)(result), v_stack_m714);
loc_009565AF:
    if (sign_flag) goto loc_00956CA7;
    v_stack_m708 = v_stack_m688;
    goto loc_00957EBD;
loc_009565CE:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (((uint32_t)(local_r13)) < ((uint32_t)(v_stack_m688))) goto loc_009563C3;
    result = PopAcquireTransitionLock((uint32_t)((uint32_t)(local_r12 + 3)), 0, (uint16_t)(result), v_stack_m714);
    result = PopAcquirePolicyLock((uint32_t)((uint32_t)(local_r12 + 3)), 0, (uint16_t)(result), v_stack_m714);
    Arg2 = ((*(uint8_t *)(v_stack_m6F8)) != 0) ? 1 : 0;
    *(uint32_t *)(v_rip + 0x66EAFC) = (uint32_t)(Arg2);
    Arg3 = 0;
    Arg1 = 0;
    result = PopSetHiberPersistedRegValue(Arg1, Arg2, Arg3, v_stack_m714);
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = PopHibernateEvaluation(Arg1, Arg2, Arg3, v_stack_m714);
    result = PopReleasePolicyLock(Arg1, Arg2, Arg3, v_stack_m714);
    result = PopReleaseTransitionLock((uint32_t)((uint32_t)(local_r12 + 3)), Arg2, Arg3, v_stack_m714);
loc_0095662C:
    goto loc_00957EB4;
loc_00956633:
    if (v_stack_m6F8 != 0) goto loc_00956646;
    if (local_r12 == 0) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956674;
loc_00956646:
    if (((uint32_t)(local_r13)) < 24) goto loc_009563C3;
    result = PopApplyAdminPolicy((uint32_t)((uint32_t)(local_r12 + 3)), v_stack_m6F8, Arg3, v_stack_m714);
    if (sign_flag) goto loc_00956CA7;
    result = PopResetCurrentPolicies((uint32_t)((uint32_t)(local_r12 + 3)), v_stack_m6F8, Arg3, v_stack_m714);
    if (sign_flag) goto loc_00956CA7;
loc_00956674:
loc_0095667B:
    v_stack_m708 = v_rip + 5990021;
    v_stack_m714 = 24;
    goto loc_00957EBD;
loc_0095668D:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    goto loc_00956395;
loc_009566AB:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    v_stack_m708 = v_rip + 2074364;
    v_stack_m714 = 280;
    goto loc_00957EBD;
loc_009566D6:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    v_stack_m684 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5B5576)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x5B5571))) - (*(uint32_t *)(v_rip + 0x5B5567)));
    v_stack_m680 = Arg1;
    v_stack_m67C = (uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x51113A)));
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 16;
    goto loc_00957EBD;
loc_0095672F:
    if (((uint32_t)(local_r14)) > 18) goto loc_00956839;
    if (((uint32_t)(local_r14)) == 18) goto loc_00957852;
    local_rsi = (uint32_t)((local_r14) - (13));
    if (condition_is_equal) goto loc_00957852;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_0095681E;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_009567F3;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_009567A6;
    if (((uint32_t)(local_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (((uint32_t)(local_r13)) < 16) goto loc_009563C3;
    if ((*(uint64_t *)(v_rip + 0x5B5F76)) == local_r12) goto loc_00956795;
    if ((*(uint64_t *)(v_stack_m6F8)) != 0) goto loc_00956C9F;
loc_00956795:
    *(uint64_t *)(v_rip + 0x5B5F5F) = v_xmm0;
    goto loc_00957EBD;
loc_009567A6:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    if ((*(uint32_t *)(v_rip + 0x4AB239)) != ((uint32_t)(v_stack_m6F8))) {
    }
    if ((*(uint32_t *)(v_rip + 0x4AB1F9)) != 0) {
    }
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 4;
    goto loc_00957EBD;
loc_009567F3:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
loc_0095680C:
    v_stack_m708 = v_rip + 5985684;
    v_stack_m714 = 8;
    goto loc_00957EBD;
loc_0095681E:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    goto loc_0095680C;
loc_00956839:
    local_rsi = (uint32_t)((local_rsi) - (19));
    if (condition_is_equal) goto loc_00957852;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
    if (((uint32_t)(local_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    result = PopLoggingInformation(v_stack_m6D0, v_stack_m6D8, Arg3, v_stack_m714);
    if (sign_flag) goto loc_00956CA7;
    v_stack_m708 = v_stack_m6D0;
    v_stack_m714 = (uint32_t)((uint32_t)(v_stack_m6D8));
    goto loc_00957EBD;
loc_009568B7:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (((uint32_t)(local_r13)) < 8) goto loc_009563C3;
    Arg4 = 0;
    Arg3 = 0;
    result = PopLogSleepDisabled((uint32_t)(*(uint32_t *)(v_stack_m6F8)), (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x4)), Arg3, Arg4);
    goto loc_00957EB0;
loc_009568EA:
    if (((uint32_t)(local_r14)) > 38) goto loc_00956C65;
    if (((uint32_t)(local_r14)) == 38) goto loc_00956C31;
    if (((uint32_t)(local_r14)) > 32) goto loc_00956AAE;
    if (((uint32_t)(local_r14)) == 32) goto loc_00957852;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - (25));
    if (condition_is_equal) goto loc_009569DE;
    Arg2 = (uint32_t)((Arg2) - (3));
    if (condition_is_equal) goto loc_009569C4;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00956967;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_0095692F;
    if (((uint32_t)(Arg2)) != 1) goto loc_00956C9F;
loc_0095692F:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (((uint32_t)(local_r13)) < 8) goto loc_009563C3;
    if (((uint32_t)(local_r14)) != 30) goto loc_0095695D;
    result = PopDiagTraceAppPowerMessage(v_stack_m6F8, Arg2, Arg3, Arg4);
    goto loc_00957EBD;
loc_0095695D:
    result = PopDiagTraceAppPowerMessageEnd(v_stack_m6F8, Arg2, Arg3, Arg4);
    goto loc_00957EBD;
loc_00956967:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    v_stack_m714 = 4;
    result = ExAllocatePool2(256, v_stack_m6F8 + 4, (uint32_t)(0x206D654DULL), Arg4);
    v_stack_m708 = result;
    if (result != 0) goto loc_009569A9;
loc_0095699F:
    goto loc_009563C8;
loc_009569A9:
    v_stack_m70F = 1;
    *(uint32_t *)(v_stack_m708) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x511098)));
    goto loc_00957EBD;
loc_009569C4:
    result = PopSuspendResumePdc((uint32_t)(*(uint32_t *)(v_rip + 0x511098)), v_stack_m6F8 + 4, (uint32_t)(0x206D654DULL), Arg4);
    *(uint8_t *)(v_rip + 0x511081) = 1;
    result = PoPowerOffMonitor(1, v_stack_m6F8 + 4, (uint32_t)(0x206D654DULL), Arg4);
    goto loc_009574C4;
loc_009569DE:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (v_stack_m718 != 0) goto loc_00956C9F;
    if (((uint32_t)(local_r13)) < 28) goto loc_00956C9F;
    v_stack_m6D8 = v_stack_m6F8 + 24;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x18))) == 0) goto loc_00956C9F;
    v_stack_m6F0 = v_stack_m6F8 + 20;
    if ((*(uint32_t *)(v_stack_m6F8 + 0x14)) > 2) goto loc_00956C9F;
    if ((*(uint32_t *)(v_stack_m6F8)) == 1) goto loc_00956A3E;
    goto loc_00956CA7;
loc_00956A3E:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x18))) + (28));
    Arg1 = (uint32_t)((1) | (0xFFFFFFFFULL));
    if (((uint32_t)(result)) >= 28) { Arg1 = (uint32_t)(result); }
    v_stack_m714 = Arg1;
    local_rbx = (uint32_t)(((uint32_t)(0xC0000058ULL)) & (0xC0000095ULL));
    if (((uint32_t)(result)) < 28) goto loc_00956CA7;
    if (((uint32_t)(local_r13)) < Arg1) goto loc_00956C9F;
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), v_stack_m6F8 + 20, (uint32_t)(0x206D654DULL), Arg4);
    v_stack_m748 = v_stack_m6F8 + 28;
    result = PopSetPowerSettingValue(v_stack_m6F8 + 4, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(v_stack_m6F0)), (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
    goto loc_00957EB0;
loc_00956AAE:
    local_rsi = (uint32_t)((local_r14) - (33));
    if (condition_is_equal) goto loc_00957852;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00956BB9;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00956B38;
    if (((uint32_t)(local_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (v_stack_m710 == ((uint8_t)(v_stack_m6F8 + 4))) goto loc_00956AF9;
loc_00956AEF:
    goto loc_009563C8;
loc_00956AF9:
    if (((uint32_t)(local_r13)) >= 4) goto loc_00956B06;
    goto loc_00956B20;
loc_00956B06:
    local_r13 = (uint32_t)((local_r13) + (-4));
    Arg3 = 0;
    result = RtlStringCbLengthW(v_stack_m6F8 + 4, (uint32_t)((uint32_t)(local_r13)), Arg3, (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!sign_flag) { local_rbx = 0; }
loc_00956B20:
    if (sign_flag) goto loc_00956CA7;
    result = PopDiagTraceServiceNotification(v_stack_m6F8, (uint32_t)((uint32_t)(local_r13)), Arg3, (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
    goto loc_00957EBD;
loc_00956B38:
    if (local_r12 == 0) goto loc_00956C9F;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5B53F9))) == 0) goto loc_00956BAF;
    if ((*(uint64_t *)(v_rip + 0x5B53E5)) == 0) goto loc_00956BAF;
    v_stack_m714 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5B53F9)) + 8);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5B53F9)) + 8)), (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
    if (result == 0) goto loc_0095699F;
    v_stack_m708 = result;
    v_stack_m70F = 1;
    result = memcpy(result + 8, *(uint64_t *)(v_rip + 0x5B539E), (uint32_t)(*(uint32_t *)(v_rip + 0x5B53B1)), (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x5B539B))) >> (4));
    *(uint32_t *)(result) = (uint32_t)(result);
    goto loc_00957EBD;
loc_00956BAF:
    goto loc_009563C8;
loc_00956BB9:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    if ((uint8_t)(*(uint64_t *)(v_rip + 0x5B539E)) != 0) {
        result = PopReleasePolicyLock(result + 8, *(uint64_t *)(v_rip + 0x5B539E), (uint32_t)(*(uint32_t *)(v_rip + 0x5B53B1)), (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
        v_stack_m700 = 0;
    }
    Arg1 = 0;
    result = PopGetWakeSource(Arg1, v_stack_m714, (uint32_t)(*(uint32_t *)(v_rip + 0x5B53B1)), (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_0095662C;
    result = ExAllocatePool2(64, (uint32_t)(v_stack_m714), (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
    v_stack_m708 = result;
    if (result == 0) goto loc_0095699F;
    v_stack_m70F = 1;
    result = PopGetWakeSource(result, v_stack_m714, (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
loc_00956C2A:
    goto loc_0095662C;
loc_00956C31:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (((uint32_t)(local_r13)) != 8) goto loc_00956C4B;
    result = PpmSetSimulatedLoad(v_stack_m6F8, v_stack_m714, (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
    goto loc_00956C2A;
loc_00956C4B:
    if (((uint32_t)(local_r13)) != 4) goto loc_00956C5B;
    result = PpmClearSimulatedLoad(v_stack_m6F8, v_stack_m714, (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
    goto loc_00956C2A;
loc_00956C5B:
    goto loc_0095662C;
loc_00956C65:
    if (((uint32_t)(result)) > 44) goto loc_00957091;
    if (((uint32_t)(result)) == 44) goto loc_00957068;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) - (39));
    if (condition_is_equal) goto loc_0095703D;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00956FFC;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00956E46;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00956D09;
    if (((uint32_t)(Arg2)) == 1) goto loc_00957779;
loc_00956C9F:
loc_00956CA2:
loc_00956CA7:
    if (v_stack_m6D0 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m6D0, Arg2, (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
    }
    if (v_stack_m70F != 0) {
        Arg2 = 0x206D654DULL;
        Arg1 = v_stack_m708;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
    }
    if (v_stack_m700 != 0) {
        result = PopReleasePolicyLock(Arg1, Arg2, (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
    }
    if (v_stack_m6F8 == 0) goto loc_00956D01;
    if (v_stack_m6F8 == local_r14) goto loc_00956D01;
    result = v_stack_m88;
    if (v_stack_m6F8 != v_stack_m88) {
        Arg2 = 0x206D654DULL;
        Arg1 = v_stack_m6F8;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
    }
    goto loc_00957F27;
loc_00956D09:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((uint32_t)(local_r13)) != 16) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if ((*(uint8_t *)(v_stack_m6F8 + 0xD)) == 0) goto loc_00956DEB;
    if ((*(uint8_t *)(v_stack_m6F8 + 0xC)) == 0) goto loc_00956DEB;
    result = PopIsPlatformAoAcCapable(Arg1, Arg2, (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(v_stack_m6D8)));
    if ((uint8_t)(result) == 0) goto loc_00956DB5;
    if ((*(uint32_t *)(v_rip + 0x510D13)) != ((uint32_t)(local_r12))) goto loc_00956DB5;
    if ((*(uint32_t *)(v_stack_m6F8 + 0x4)) != 2) goto loc_00956DBC;
    v_stack_m6A4 = 0;
    v_stack_m69C = 0;
    v_stack_m6C0 = Arg1;
    v_stack_m6BC = 40;
    v_stack_m6B8 = 0;
    v_stack_m6B0 = 0;
    v_stack_m6A8 = 0;
    v_stack_m738 = v_stack_m6C0;
    v_stack_m740 = 0;
    v_stack_m748 = (uint32_t)(*(uint32_t *)(v_stack_m6F8));
    result = DbgkWerCaptureLiveKernelDump2(v_rip + 1748626, 160, (uint32_t)(0x801ULL), (int32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
loc_00956DB5:
    if ((*(uint32_t *)(v_stack_m6F8 + 0x4)) != 2) {
        Arg2 = *(uint32_t *)(v_stack_m6F8 + 0x8);
        Arg1 = *(uint8_t *)(v_stack_m6F8 + 0xF);
        result = PopProcessSessionDisplayStateChange(Arg1, Arg2, (uint32_t)(0x801ULL), (int32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    }
    result = PopSetDisplayStatus((uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x4)), Arg2, (uint32_t)(0x801ULL), (int32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    result = PopUpdateConsoleDisplayState((uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x4)), Arg2, (uint32_t)(0x801ULL), (int32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    if ((*(uint32_t *)(v_stack_m6F8 + 0x4)) == 1) {
        result = PopPowerAggregatorNotifyDisplayPoweredOn(1, Arg2, (uint32_t)(0x801ULL), (int32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    }
    if ((*(uint8_t *)(v_stack_m6F8 + 0xE)) == 0) goto loc_00957EBD;
    if ((*(uint8_t *)(v_stack_m6F8 + 0xC)) != 0) {
        Arg2 = v_stack_m6F8 + 4;
        v_stack_m738 = 0;
        v_stack_m740 = 0;
        v_stack_m748 = 0;
        Arg4 = 0;
        Arg3 = Arg4 + 4;
        Arg1 = v_rip - 9659186;
        result = ZwUpdateWnfStateData(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint8_t *)(v_stack_m6F8 + 0xE)) == 0) goto loc_00957EBD;
    Arg1 = ((*(uint32_t *)(v_stack_m6F8 + 0x4)) == 0) ? 1 : 0;
    result = PopDiagTraceSessionDisplayStateChange(Arg1, (uint32_t)(*(uint32_t *)(v_stack_m6F8)), *(uint8_t *)(v_stack_m6F8 + 0xC), (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    goto loc_00957EBD;
loc_00956E46:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 64) goto loc_00956C9F;
    result = PopAcquireRwLockExclusive(v_rip + 5969362, (uint32_t)(*(uint32_t *)(v_stack_m6F8)), *(uint8_t *)(v_stack_m6F8 + 0xC), (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    result = PopReleaseRwLock(v_rip + 5969343, (uint32_t)(*(uint32_t *)(v_stack_m6F8)), *(uint8_t *)(v_stack_m6F8 + 0xC), (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    result = v_stack_m658;
    if (((uint32_t)(*(uint64_t *)(v_rip + 0x510BAE))) == ((uint32_t)(v_stack_m6F8 + 1))) { result = (uint32_t)(v_stack_m6F8 + 1); }
    v_stack_m658 = (uint8_t)(result);
    result = TtmIsEnabled(v_stack_m6F8 + 1, (uint32_t)(*(uint32_t *)(v_stack_m6F8)), *(uint8_t *)(v_stack_m6F8 + 0xC), (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    v_stack_m650 = (uint8_t)(result);
    result = TtmIsEnabled(v_stack_m6F8 + 1, (uint32_t)(*(uint32_t *)(v_stack_m6F8)), *(uint8_t *)(v_stack_m6F8 + 0xC), (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    if ((uint8_t)(result) == 0) goto loc_00956ECE;
    result = TtmInitCurrentSession(v_stack_m6F8 + 1, (uint32_t)(*(uint32_t *)(v_stack_m6F8)), *(uint8_t *)(v_stack_m6F8 + 0xC), (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    v_stack_m70C = (uint32_t)(result);
    if (sign_flag) goto loc_00956CA7;
    result = PopPowerRequestNotifyTtmSessionInitialized(v_stack_m6F8 + 1, (uint32_t)(*(uint32_t *)(v_stack_m6F8)), *(uint8_t *)(v_stack_m6F8 + 0xC), (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
loc_00956ECE:
    result = PopAcquirePolicyLock(v_stack_m6F8 + 1, (uint32_t)(*(uint32_t *)(v_stack_m6F8)), *(uint8_t *)(v_stack_m6F8 + 0xC), (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    v_stack_m678 = 0;
    v_stack_m688 = v_rip + 5986323;
    v_stack_m680 = v_rip + 5311333;
    Arg1 = ((*(uint8_t *)(v_rip + 0x5B5F10)) != 0) ? 1 : 0;
    v_stack_m670 = Arg1;
    v_stack_m66C = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5B5EFB)));
    v_stack_m674 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5B5F0E)));
    v_stack_m668 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5B5F05)));
    v_stack_m664 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5B5EFC)));
    v_stack_m660 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5B5EF3)));
    v_stack_m654 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5B5EEA)));
    v_stack_m65C = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5B5EE1)));
    v_stack_m657 = (uint8_t)(*(uint8_t *)(v_rip + 0x4B460D));
loc_00956F80:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4B45F0))))) | (0));
    if (condition_is_not_equal) goto loc_00956F80;
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 64;
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), (uint32_t)(*(uint32_t *)(v_stack_m6F8)), *(uint8_t *)(v_stack_m6F8 + 0xC), (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    result = PopPrintEx(3, v_rip + 1753410, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    Arg3 = 0;
    result = PopDiagTraceSessionState(v_rip - 9721324, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    result = PopReleasePolicyLock(v_rip - 9721324, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    goto loc_00957EC2;
loc_00956FFC:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 4) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    result = ((*(uint32_t *)(v_stack_m6F8)) != 0) ? 1 : 0;
    v_stack_m6F0 = (uint32_t)(result);
    result = PopSetPowerSettingValueAcDc(v_rip - 9678075, (uint32_t)((uint32_t)((uint32_t)(v_stack_m718))), v_stack_m6F0, (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    goto loc_00957EBD;
loc_0095703D:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 24) goto loc_00956C9F;
    result = PopShutdownListenerInsertCallback(v_stack_m6F8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m718))), v_stack_m6F0, (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
loc_00957061:
    goto loc_00957EBD;
loc_00957068:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 24) goto loc_009563C3;
    result = PopPowerRequestActionInfo(v_stack_m6F8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m718))), v_stack_m6F0, (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    goto loc_00957EB0;
loc_00957091:
    local_rsi = (uint32_t)((local_r14) - (45));
    if (condition_is_equal) goto loc_00957189;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957140;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957108;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_not_equal) goto loc_00957849;
    if ((*(uint8_t *)(v_rip + 0x5F0540)) == ((uint8_t)(local_rsi))) goto loc_00956AEF;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 16) goto loc_009570DA;
    Arg2 = 0;
    goto loc_009570E4;
loc_009570DA:
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 24) goto loc_009570F1;
loc_009570E4:
    result = PpmParkApplyForcedMask(v_stack_m6F8, v_stack_m6F8 + 16, v_stack_m6F0, (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    goto loc_00956C2A;
loc_009570F1:
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 2) goto loc_00956C5B;
    result = PpmParkClearForcedMask(v_stack_m6F8, v_stack_m6F8 + 16, v_stack_m6F0, (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    goto loc_00956C2A;
loc_00957108:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 16) goto loc_00956C9F;
    result = PopUmpoSendLegacyEvent(v_stack_m6F8, v_stack_m6F8 + 16, v_stack_m6F0, (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    if (!sign_flag) goto loc_00957EBD;
    if (((uint32_t)(result)) != 0xC0000120ULL) goto loc_00956CA7;
    goto loc_00957EBD;
loc_00957140:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) < 2) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    result = KeQueryActiveGroupCount(v_stack_m6F8, v_stack_m6F8 + 16, v_stack_m6F0, (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)));
    if (((uint16_t)(*(uint16_t *)(v_stack_m6F8))) >= ((uint16_t)(result))) goto loc_00956C9F;
    result = PopProcessorInformation(v_stack_m688, v_stack_m6F8 + 16, (uint16_t)(*(uint16_t *)(v_stack_m6F8)), v_stack_m714);
    goto loc_009565AF;
loc_00957189:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    result = PopGetPowerRequestListInfo(v_stack_m708, v_stack_m714, (uint16_t)(*(uint16_t *)(v_stack_m6F8)), v_stack_m714);
loc_009571AA:
    if (sign_flag) goto loc_00956CA7;
    v_stack_m70F = 1;
    goto loc_00957EBD;
loc_009571C5:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    result = ExGetWakeTimerList(v_stack_m708, v_stack_m714, (uint16_t)(*(uint16_t *)(v_stack_m6F8)), v_stack_m714);
    goto loc_009571AA;
loc_009571E8:
    if (((uint32_t)(local_r14)) > 75) goto loc_00957817;
    if (((uint32_t)(local_r14)) == 75) goto loc_009577F4;
    if (((uint32_t)(local_r14)) > 63) goto loc_0095756B;
    if (((uint32_t)(local_r14)) == 63) goto loc_009574FB;
    if (((uint32_t)(local_r14)) > 57) goto loc_0095735E;
    if (((uint32_t)(local_r14)) == 57) goto loc_00957852;
    local_rsi = (uint32_t)((local_r14) - (51));
    if (condition_is_equal) goto loc_009572F0;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_009572A7;
    if (((uint32_t)(local_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 8) goto loc_009563C3;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 4) goto loc_009563C3;
    result = PpmParkSetLpiCap((uint32_t)(*(uint32_t *)(v_stack_m6F8)), (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x4)), v_stack_m688, v_stack_m714);
    if (sign_flag) goto loc_009563C8;
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = (uint32_t)((uint32_t)(v_stack_m718));
    goto loc_00957EC2;
loc_009572A7:
    if ((*(uint8_t *)(v_rip + 0x5F034A)) == 0) goto loc_00956AEF;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 8) goto loc_009572D9;
    result = PpmSetSimulatedIdle(v_stack_m6F8, (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x4)), v_stack_m688, v_stack_m714);
    goto loc_00956C2A;
loc_009572D9:
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 4) goto loc_00956C5B;
    result = PpmClearSimulatedIdle(v_stack_m6F8, (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x4)), v_stack_m688, v_stack_m714);
    goto loc_00956C2A;
loc_009572F0:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) < 4) goto loc_009563C3;
    result = PopAcquireTransitionLock(5, (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x4)), v_stack_m688, v_stack_m714);
    result = PopAcquirePolicyLock(5, (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x4)), v_stack_m688, v_stack_m714);
    result = PopSetHiberFileSize((uint32_t)(*(uint32_t *)(v_stack_m6F8)), v_stack_m6E0, v_stack_m6F0, v_stack_m714);
    result = PopReleasePolicyLock((uint32_t)(*(uint32_t *)(v_stack_m6F8)), v_stack_m6E0, v_stack_m6F0, v_stack_m714);
loc_0095733C:
    result = PopReleaseTransitionLock(5, v_stack_m6E0, v_stack_m6F0, v_stack_m714);
    if (sign_flag) {
        result = v_stack_m6F0;
        v_stack_m6E0 = result;
    }
    goto loc_0095680C;
loc_0095735E:
    local_rsi = (uint32_t)((local_rsi) - (58));
    if (condition_is_equal) goto loc_009574CB;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_0095748D;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957464;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_0095742F;
    if (((uint32_t)(local_rsi)) != 1) goto loc_00956C9F;
    result = Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline(5, v_stack_m6E0, v_stack_m6F0, v_stack_m714);
    if ((uint32_t)(result) != 0) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 40) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 16) goto loc_00956C9F;
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), v_stack_m6E0, v_stack_m6F0, v_stack_m714);
    result = PopSessionConnectionChange((uint32_t)((uint32_t)(result)), v_stack_m6F8, local_r12, v_stack_m714);
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), v_stack_m6F8, local_r12, v_stack_m714);
    result = Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), v_stack_m6F8, local_r12, v_stack_m714);
    result = *(uint64_t *)(v_rip + 0x510382);
    if (*(uint64_t *)(v_rip + 0x510382) != 0) {
        Arg4 = local_rsi + 2;
        Arg1 = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = guard_dispatch_icall(Arg1, *(uint8_t *)(v_stack_m6F8 + 0x1), *(uint8_t *)(v_stack_m6F8), Arg4);
    }
    goto loc_00957EC2;
loc_0095742F:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 16) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 8) goto loc_00956C9F;
    goto loc_00957EC2;
loc_00957464:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) < 8) goto loc_009563C3;
    result = PopEnforceResiliencyScenarios(v_stack_m6F8, *(uint8_t *)(v_stack_m6F8 + 0x1), *(uint8_t *)(v_stack_m6F8), Arg4);
    goto loc_00957EBD;
loc_0095748D:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 16) goto loc_009563C3;
    if (((uint32_t)((uint32_t)(v_stack_m718))) < 4) goto loc_009563C3;
    result = PopGetSettingValue(v_stack_m6F8, local_r12, (uint32_t)((uint32_t)((uint32_t)(v_stack_m718))), Arg4);
loc_009574C4:
    goto loc_009563C8;
loc_009574CB:
    if (local_r12 == 0) goto loc_00956C9F;
    if (local_r14 == 0) goto loc_009574E3;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 20) goto loc_009563C3;
loc_009574E3:
    if (v_stack_m718 != 8) goto loc_009563C3;
    result = PopGetSettingNotificationName(v_stack_m6F8, local_r12, (uint32_t)((uint32_t)((uint32_t)(v_stack_m718))), Arg4);
    goto loc_009574C4;
loc_009574FB:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), local_r12, (uint32_t)((uint32_t)((uint32_t)(v_stack_m718))), Arg4);
    result = PopPrintEx(v_stack_m6F8 + 3, v_rip + 1752098, (uint32_t)((uint32_t)(result)), Arg4);
    Arg3 = 0;
    result = PopDiagTraceSessionState(v_rip - 9722715, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, Arg4);
    result = PopFreeSessionState((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, Arg4);
    result = TtmIsEnabled((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00956347;
    result = PopPowerRequestNotifyTtmSessionUninitialized((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, Arg4);
    result = TtmCleanupCurrentSession((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, Arg4);
    goto loc_00956347;
loc_0095756B:
    if (((uint32_t)(local_rsi)) > 69) goto loc_00957710;
    if (((uint32_t)(local_rsi)) == 69) goto loc_009576E7;
    local_rsi = (uint32_t)((local_rsi) - (64));
    if (condition_is_equal) goto loc_0095769E;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_0095763F;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_0095760B;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_009575D2;
    if (((uint32_t)(local_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 8) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (v_stack_m718 != 0) goto loc_00956C9F;
    result = PopMonitorInvocation(v_stack_m6F8, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg3, Arg4);
    goto loc_009574C4;
loc_009575D2:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 224) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_009575FB;
    if (v_stack_m718 != 168) goto loc_00956C9F;
loc_009575FB:
    result = PopPdcInvocation(v_stack_m6F8, local_r12, Arg3, Arg4);
    goto loc_009574C4;
loc_0095760B:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    result = PopIsPlatformAoAcCapable(v_stack_m6F8, local_r12, Arg3, Arg4);
    v_stack_m688 = (uint8_t)(result);
loc_00957631:
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = (uint32_t)(v_stack_m6F8);
    goto loc_00957EBD;
loc_0095763F:
    result = PsIsCurrentThreadInServerSilo(v_stack_m6F8, local_r12, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00957652;
loc_00957648:
    goto loc_009563C8;
loc_00957652:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    result = PopFilterCapabilities(v_rip + 5986381, v_stack_m688, Arg3, Arg4);
    if (v_stack_m676 != 0) {
        Arg1 = v_stack_m676;
        result = PopReadHiberbootPolicy(Arg1, v_stack_m688, Arg3, Arg4);
    }
    goto loc_00957631;
loc_0095769E:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 8) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), v_stack_m688, Arg3, Arg4);
    result = PopSessionWinlogonNotification((uint32_t)((uint32_t)(result)), v_stack_m6F8, Arg3, Arg4);
    goto loc_00957EBD;
loc_009576E7:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    result = PopInitPlatformSettings((uint32_t)((uint32_t)(result)), v_stack_m6F8, Arg3, Arg4);
    result = PopIsPlatformAoAcCapable((uint32_t)((uint32_t)(result)), v_stack_m6F8, Arg3, Arg4);
    *(uint8_t *)(v_rip + 0x5B57C9) = (uint8_t)(result);
    goto loc_009563C8;
loc_00957710:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) - (70));
    if (condition_is_equal) goto loc_009577E1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00957648;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00957779;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00957CDD;
    if (Arg1 != 1) goto loc_00956C9F;
    if (v_stack_m710 != 0) goto loc_00956AEF;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 16) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (v_stack_m718 != 0) goto loc_00956C9F;
    result = PopPdcCsDeviceNotification(v_stack_m6F8, v_stack_m6F8, Arg3, Arg4);
    goto loc_009574C4;
loc_00957779:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 40) goto loc_009563C3;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 8) goto loc_009563C3;
    Arg2 = (((uint32_t)(local_rsi)) == 72) ? 1 : 0;
    result = PopPowerRequestCreateUserModeRequest(v_stack_m6F8, Arg2, v_stack_m688, Arg4);
loc_009577BA:
    if (sign_flag) goto loc_00956CA7;
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 8;
    goto loc_00957EC2;
loc_009577E1:
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, v_stack_m688, Arg4);
    *(uint64_t *)(v_rip + 0x5B6FA1) = result;
    goto loc_00957EBD;
loc_009577F4:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    result = PopCapturePlatformRole(Arg1, Arg2, v_stack_m688, Arg4);
    v_stack_m688 = (uint32_t)(result);
    goto loc_009567D9;
loc_00957817:
    if (((uint32_t)(local_r14)) > 87) goto loc_00957B8E;
    if (((uint32_t)(local_r14)) == 87) goto loc_00957AA9;
    if (((uint32_t)(local_r14)) > 81) goto loc_0095799A;
    if (((uint32_t)(local_r14)) == 81) goto loc_00957852;
    local_rsi = (uint32_t)((local_r14) - (76));
    if (condition_is_equal) goto loc_0095793D;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_0095789F;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_0095785C;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957852;
loc_00957849:
    if (((uint32_t)(local_rsi)) != 1) goto loc_00956C9F;
loc_00957852:
    goto loc_009563C8;
loc_0095785C:
    if (v_stack_m710 != 0) goto loc_00956AEF;
    if (local_r12 != 0) goto loc_00956C9F;
    if (v_stack_m718 != 0) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00957895;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 4) goto loc_00956C9F;
    result = PpmSetExitLatencySamplingPercentage(v_stack_m6F8, Arg2, v_stack_m688, Arg4);
    goto loc_00957061;
loc_00957895:
    result = PpmClearExitLatencySamplingPercentage(v_stack_m6F8, Arg2, v_stack_m688, Arg4);
    goto loc_00957EBD;
loc_0095789F:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    result = TtmIsEnabled(v_stack_m6F8, Arg2, v_stack_m688, Arg4);
    if ((uint8_t)(result) == 0) goto loc_009578F9;
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, v_stack_m688, Arg4);
    Arg1 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) | (0xFFFFFFFFULL));
    if (((uint32_t)(result)) == Arg1) goto loc_009578EF;
    result = TtmNotifySessionDisplayBurst((uint32_t)((uint32_t)(result)), v_stack_m6F8 + 6, v_stack_m688, Arg4);
    goto loc_0095634B;
loc_009578EF:
    goto loc_0095634B;
loc_009578F9:
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x4B3C75)) == 0) {
        Arg1 = 1;
        local_rsi = 0;
        if ((*(uint8_t *)(v_rip + 0x510147)) == 0) { local_rsi = Arg1; }
    }
    if ((uint8_t)(local_rsi) == 0) {
        Arg2 = 6;
        Arg1 = Arg2 + 4;
        result = PopEventCalloutDispatch(Arg1, Arg2, v_stack_m688, Arg4);
    }
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x510180)) != 0) goto loc_00957EBD;
    result = PopDiagTraceDisplayBurstWin32kCallout(Arg1, Arg2, (uint8_t)(local_rsi), Arg4);
    goto loc_00957EBD;
loc_0095793D:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    v_stack_m688 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5B4A7B)));
    v_stack_m680 = *(uint64_t *)(v_rip + 0x5B4C1D);
    v_stack_m678 = *(uint64_t *)(v_rip + 0x5B4C16);
    if ((*(uint8_t *)(v_rip + 0x5B497F)) != ((uint8_t)(v_stack_m6F8))) goto loc_0095798D;
    goto loc_009563C8;
loc_0095798D:
    goto loc_0095667B;
loc_0095799A:
    local_rsi = (uint32_t)((local_rsi) - (82));
    if (condition_is_equal) goto loc_00957852;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957A83;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957A45;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957A24;
    if (((uint32_t)(local_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    Arg3 = 0;
    result = RtlStringCbLengthW(v_stack_m6F8, (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))), Arg3, Arg4);
    if (sign_flag) goto loc_00956CA7;
    result = PopBatteryDeviceState(v_stack_m6F8, v_stack_m688, Arg3, Arg4);
    if (sign_flag) goto loc_00956CA7;
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 52;
    goto loc_00957EBD;
loc_00957A24:
    if ((*(uint8_t *)(v_stack_m6F8 + 0xC)) == 0) goto loc_00957A3B;
    result = PopPowerRequestReferenceAcquire(*(uint64_t *)(v_stack_m6F8), (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)), Arg3, Arg4);
    goto loc_00957061;
loc_00957A3B:
    result = PopPowerRequestReferenceRelease(*(uint64_t *)(v_stack_m6F8), (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)), Arg3, Arg4);
    goto loc_00957061;
loc_00957A45:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (((uint32_t)(*(uint8_t *)(v_rip + 0x510180))) < 16) goto loc_009563C3;
    if (((uint32_t)(*(uint8_t *)(v_rip + 0x510180))) < ((uint32_t)(*(uint16_t *)(v_stack_m6F8 + 0xC) * 2 + 14))) goto loc_009563C3;
    result = PopThermalProcessUsermodeEvent(v_stack_m6F8, (uint32_t)(*(uint32_t *)(v_stack_m6F8 + 0x8)), Arg3, Arg4);
    goto loc_00957EB0;
loc_00957A83:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    Arg2 = 0;
    result = PopCurrentPowerStatePrecise(v_stack_m688, Arg2, Arg3, Arg4);
    goto loc_0095625E;
loc_00957AA9:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((uint32_t)(*(uint8_t *)(v_rip + 0x510180))) < 8) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m6F8)) - 100)) <= 0xF9BULL) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m6F8)))) >= 0x100BULL) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m6F8)) - 4096)) > 10) goto loc_00957B51;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x68203D), v_stack_m710, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00957B16;
    result = PopCapabilityCheck(v_rip + 1745277, v_stack_m710, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00957B16;
    goto loc_009563C8;
loc_00957B16:
    v_stack_m730 = v_stack_m70F;
    v_stack_m738 = v_stack_m714;
    v_stack_m740 = v_stack_m708;
    v_stack_m748 = (uint32_t)((uint32_t)(v_stack_m718));
    result = TtmDispatchApi((uint32_t)((uint32_t)((uint32_t)(0xC0000061ULL))), v_stack_m6F8, (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))), local_r12);
    goto loc_00956C2A;
loc_00957B51:
    v_stack_m728 = v_stack_m70F;
    v_stack_m730 = v_stack_m714;
    v_stack_m738 = v_stack_m708;
    v_stack_m740 = (uint32_t)((uint32_t)(v_stack_m718));
    v_stack_m748 = local_r12;
    result = PopPowerInformationInternal((uint32_t)((uint32_t)((uint32_t)(0xC0000061ULL))), v_stack_m6F8, v_stack_m6F8, (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    goto loc_00956C2A;
loc_00957B8E:
    if (((uint32_t)(local_r14)) > 93) goto loc_00957D53;
    if (((uint32_t)(local_r14)) == 93) goto loc_00957D08;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - (88));
    if (condition_is_equal) goto loc_00957CDD;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00957C8C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00957C60;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00957C08;
    if (Arg1 != 1) goto loc_00956C9F;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    if (((uint32_t)(*(uint8_t *)(v_rip + 0x510180))) != 12) goto loc_009563C3;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 8) goto loc_009563C3;
    result = PopEtEnergyTrackerCreate(v_stack_m6F8, v_stack_m688, v_stack_m6F8, (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    goto loc_009577BA;
loc_00957C08:
    result = PopIsPlatformAoAcCapable(v_stack_m6F8, v_stack_m688, v_stack_m6F8, (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    if ((uint8_t)(result) == 0) goto loc_00957648;
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 336) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    result = PopFxIsDevicePotentialDripsConstraint(v_stack_m6F8, v_stack_m688, v_stack_m6F8, (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    v_stack_m688 = (uint8_t)(result);
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 1;
    goto loc_00957EBD;
loc_00957C60:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) < 4) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    Arg1 = ((*(uint32_t *)(v_stack_m6F8)) != 0) ? 1 : 0;
    result = PopUpdatePowerButtonHoldState(Arg1, v_stack_m688, v_stack_m6F8, (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    goto loc_00957EBD;
loc_00957C8C:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) < 4) goto loc_009563C3;
    result = PopAcquireTransitionLock(6, v_stack_m688, v_stack_m6F8, (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    result = PopAcquirePolicyLock(6, v_stack_m688, v_stack_m6F8, (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    result = PopSetHiberFileType((uint32_t)(*(uint32_t *)(v_stack_m6F8)), v_stack_m6E0, v_stack_m6F0, (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    result = PopReleasePolicyLock((uint32_t)(*(uint32_t *)(v_stack_m6F8)), v_stack_m6E0, v_stack_m6F0, (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    goto loc_0095733C;
loc_00957CDD:
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    Arg1 = v_stack_m6F8 + 23;
    if (((uint32_t)(local_r14)) != 88) { Arg1 = (uint32_t)(v_stack_m6F8 + 23 - 12); }
    result = PopScreenOff(Arg1, v_stack_m6E0, v_stack_m6F0, (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
loc_00957D01:
    goto loc_009563C8;
loc_00957D08:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 8) goto loc_009563C3;
    if (((uint32_t)((uint32_t)(v_stack_m718))) < 12) goto loc_009563C3;
    result = PopEtEnergyTrackerQuery(*(uint64_t *)(v_stack_m6F8), local_r12, (uint32_t)((uint32_t)((uint32_t)(v_stack_m718))), (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    if (sign_flag) goto loc_00956CA7;
    goto loc_00957EC2;
loc_00957D53:
    local_rsi = (uint32_t)((local_r14) - (94));
    if (condition_is_equal) goto loc_00957E7E;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957E4F;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957E2A;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_00957DB5;
    if (((uint32_t)(local_rsi)) != 1) goto loc_00956C9F;
    if (v_stack_m6F8 != 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    result = PopCurrentSystemPowerSourceState(v_stack_m688, local_r12, (uint32_t)((uint32_t)((uint32_t)(v_stack_m718))), (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 68;
    goto loc_00957EBD;
loc_00957DB5:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if ((uint32_t)((uint32_t)(v_stack_m718)) == 0) goto loc_00956C9F;
    if (local_r12 == 0) goto loc_00956C9F;
    if (v_stack_m718 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) < 32) goto loc_009563C3;
    if (((uint32_t)((uint32_t)(v_stack_m718))) < 16) goto loc_009563C3;
    result = PopBlackBoxDirectAccess(v_stack_m6F8, v_stack_m688, (uint32_t)((uint32_t)((uint32_t)(v_stack_m718))), (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    if (sign_flag) goto loc_00956CA7;
    v_stack_m708 = v_stack_m688;
    v_stack_m714 = 16;
    goto loc_00957EC2;
loc_00957E2A:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) < ((uint32_t)(v_stack_m6F8))) goto loc_009563C3;
    result = PopSendSuspendResumeNotifications(*(uint8_t *)(v_stack_m6F8), v_stack_m688, (uint32_t)((uint32_t)((uint32_t)(v_stack_m718))), (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    goto loc_00957EB0;
loc_00957E4F:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != ((uint32_t)(*(uint8_t *)(v_stack_m6F8)))) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    Arg3 = 0;
    result = ExNotifyCallback(*(uint64_t *)(v_rip + 0x632B19), v_stack_m6F8, Arg3, (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    goto loc_00957EBD;
loc_00957E7E:
    if (v_stack_m6F8 == 0) goto loc_00956C9F;
    if (local_r12 != 0) goto loc_00956C9F;
    if (v_stack_m718 != 0) goto loc_00956C9F;
    if (((uint32_t)((uint32_t)(v_stack_m718))) != 32) goto loc_009563C3;
    result = PopBlackBoxUpdate(v_stack_m6F8, v_stack_m710, Arg3, (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
loc_00957EB0:
loc_00957EB4:
    if (sign_flag) goto loc_00956CA7;
loc_00957EBD:
loc_00957EC2:
    if (v_stack_m708 == 0) goto loc_00957F03;
    if (local_r12 == 0) goto loc_00957F03;
    if (((uint32_t)((uint32_t)(v_stack_m718))) < v_stack_m714) goto loc_009563C3;
    result = memcpy(local_r12, v_stack_m708, (uint32_t)(v_stack_m714), (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    goto loc_00957F03;
loc_00957F03:
    if (((uint32_t)((uint32_t)(v_stack_m6E4))) == 51) goto loc_00956CA7;
    if (((uint32_t)((uint32_t)(v_stack_m6E4))) == 89) goto loc_00956CA7;
    goto loc_00957D01;
loc_00957F27:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m708, (uint32_t)(v_stack_m714), (uint32_t)((uint32_t)(*(uint8_t *)(v_rip + 0x510180))));
    local_rsp = (local_rsp) + (0x730ULL);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00955D80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
