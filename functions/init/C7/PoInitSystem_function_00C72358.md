# PoInitSystem

- RVA: `0x00C72358`–`0x00C73250` (길이 `3,832` bytes)
- VA: `0x0000000140C72358`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BAFA0`
- 디코드: `716`개 명령, `3,832/3,832` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **141**; 고유 호출 대상: **115**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **321**

### Outgoing calls
- `0x00C7239B` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C723B9` → [PopComputeCounterShifts](../../text/4F/PopComputeCounterShifts_function_004F8178.md) (function, `0x004F8178`)
- `0x00C723D1` → [PopComputeCounterShifts](../../text/4F/PopComputeCounterShifts_function_004F8178.md) (function, `0x004F8178`)
- `0x00C723DF` → [PopSleepstudyInitialize](PopSleepstudyInitialize_function_00C76C60.md) (function, `0x00C76C60`)
- `0x00C723E6` → [PopPowerAggregatorInitialize](PopPowerAggregatorInitialize_function_00C77B94.md) (function, `0x00C77B94`)
- `0x00C724AE` → [ExInitializeNPagedLookasideListInternal](../../text/46/ExInitializeNPagedLookasideListInternal_function_00468720.md) (function, `0x00468720`)
- `0x00C724DE` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C7259D` → [PopInitializeWorkItem](../../page/75/PopInitializeWorkItem_function_007540C8.md) (function, `0x007540C8`)
- `0x00C725B0` → [PopInitializeWorkItem](../../page/75/PopInitializeWorkItem_function_007540C8.md) (function, `0x007540C8`)
- `0x00C725C3` → [PopInitializeWorkItem](../../page/75/PopInitializeWorkItem_function_007540C8.md) (function, `0x007540C8`)
- `0x00C725D6` → [PopInitializeWorkItem](../../page/75/PopInitializeWorkItem_function_007540C8.md) (function, `0x007540C8`)
- `0x00C725FE` → [PopInitializeWorkItem](../../page/75/PopInitializeWorkItem_function_007540C8.md) (function, `0x007540C8`)
- `0x00C72611` → [PopInitializeWorkItem](../../page/75/PopInitializeWorkItem_function_007540C8.md) (function, `0x007540C8`)
- `0x00C72624` → [PopInitializeWorkItem](../../page/75/PopInitializeWorkItem_function_007540C8.md) (function, `0x007540C8`)
- `0x00C7266F` → [PpmCheckInit](../C4/PpmCheckInit_function_00C40578.md) (function, `0x00C40578`)
- `0x00C72674` → [PopInitializeIrpWorkers](../C4/PopInitializeIrpWorkers_function_00C40C64.md) (function, `0x00C40C64`)
- `0x00C7279C` → [PopInitShutdownList](../C3/PopInitShutdownList_function_00C3ED18.md) (function, `0x00C3ED18`)
- `0x00C7283F` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x00C72924` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00C7293E` → [PopResetActionDefaults](../../page/70/PopResetActionDefaults_function_007058E0.md) (function, `0x007058E0`)
- `0x00C72951` → [PopDefaultPolicy](../../page/75/PopDefaultPolicy_function_00753924.md) (function, `0x00753924`)
- `0x00C72985` → [Feature_VpciVscBootDiskHibernation__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_VpciVscBootDiskHibernation__private_IsEnabledDeviceUsageNoInline_function_005CE348.md) (function, `0x005CE348`)
- `0x00C729C1` → [PpmInitPolicyConfiguration](../C4/PpmInitPolicyConfiguration_function_00C40708.md) (function, `0x00C40708`)
- `0x00C729C6` → [PpmInitIdlePolicy](../C3/PpmInitIdlePolicy_function_00C3D8F4.md) (function, `0x00C3D8F4`)
- `0x00C729CB` → [PpmPerfInitialize](../C3/PpmPerfInitialize_function_00C3EB34.md) (function, `0x00C3EB34`)
- `0x00C729D0` → [PpmInitCoreParkingPolicy](../C3/PpmInitCoreParkingPolicy_function_00C3D84C.md) (function, `0x00C3D84C`)
- `0x00C729D5` → [PpmInitHeteroPolicy](../C4/PpmInitHeteroPolicy_function_00C41CCC.md) (function, `0x00C41CCC`)
- `0x00C729DA` → [PpmIdleRegisterDefaultStates](../../page/75/PpmIdleRegisterDefaultStates_function_00755110.md) (function, `0x00755110`)
- `0x00C729E1` → [PopDeepSleepInitialize](../C4/PopDeepSleepInitialize_function_00C409D0.md) (function, `0x00C409D0`)
- `0x00C729E6` → [PopInitializePowerSettings](../C3/PopInitializePowerSettings_function_00C3EE74.md) (function, `0x00C3EE74`)
- `0x00C729EB` → [PopInitilizeAcDcSettings](../../text/48/PopInitilizeAcDcSettings_function_004828D0.md) (function, `0x004828D0`)
- `0x00C729FE` → [PopBatteryInit](../C4/PopBatteryInit_function_00C41EE0.md) (function, `0x00C41EE0`)
- `0x00C72A03` → [PopThermalInit](../C3/PopThermalInit_function_00C3F128.md) (function, `0x00C3F128`)
- `0x00C72BCB` → [PopSmartSuspendInit](../C4/PopSmartSuspendInit_function_00C42358.md) (function, `0x00C42358`)
- `0x00C72BFB` → [PoFxInitPowerManagement](../C3/PoFxInitPowerManagement_function_00C3E83C.md) (function, `0x00C3E83C`)
- `0x00C72C22` → [PopNetInitialize](../C4/PopNetInitialize_function_00C423AC.md) (function, `0x00C423AC`)
- `0x00C72C29` → [PopInitializePowerButtonHold](../C4/PopInitializePowerButtonHold_function_00C425A8.md) (function, `0x00C425A8`)
- `0x00C72C3C` → [PopRecorderInit](../C4/PopRecorderInit_function_00C42820.md) (function, `0x00C42820`)
- `0x00C72C44` → [PopRecordFirmwareResetReason](../C3/PopRecordFirmwareResetReason_function_00C3E25C.md) (function, `0x00C3E25C`)
- `0x00C72C49` → [PopCreateTimebrokerServiceSid](../C3/PopCreateTimebrokerServiceSid_function_00C3D2C8.md) (function, `0x00C3D2C8`)
- `0x00C72C58` → [PopInitializeDirectedDrips](../C3/PopInitializeDirectedDrips_function_00C3E6B4.md) (function, `0x00C3E6B4`)
- `0x00C72C5F` → [SshInitialize](../C4/SshInitialize_function_00C4465C.md) (function, `0x00C4465C`)
- `0x00C72C72` → [HviIsAnyHypervisorPresent](../../text/4A/HviIsAnyHypervisorPresent_function_004ADC50.md) (function, `0x004ADC50`)
- `0x00C72CA0` → [PopSendFanNoiseChangeWnf](../../page/76/PopSendFanNoiseChangeWnf_function_00769240.md) (function, `0x00769240`)
- `0x00C72CD5` → [SshInitialize](../C4/SshInitialize_function_00C4465C.md) (function, `0x00C4465C`)
- `0x00C72CDA` → [PopUmpoInitializeChannel](../C4/PopUmpoInitializeChannel_function_00C428F0.md) (function, `0x00C428F0`)
- `0x00C72CDF` → [PopUmpoInitializeMonitorChannel](../C4/PopUmpoInitializeMonitorChannel_function_00C42B6C.md) (function, `0x00C42B6C`)
- `0x00C72D0A` → [PopEsInit](../C4/PopEsInit_function_00C42F24.md) (function, `0x00C42F24`)
- `0x00C72D0F` → [PopInitializePowerSettingCallbacks](../C3/PopInitializePowerSettingCallbacks_function_00C3E6E8.md) (function, `0x00C3E6E8`)
- `0x00C72D14` → [PopEtInit](../C4/PopEtInit_function_00C43018.md) (function, `0x00C43018`)
- `0x00C72D21` → [PopPowerRequestInitialize](../C3/PopPowerRequestInitialize_function_00C3E2AC.md) (function, `0x00C3E2AC`)
- `0x00C72D31` → [PopPowerAggregatorInitialize](PopPowerAggregatorInitialize_function_00C77B94.md) (function, `0x00C77B94`)
- `0x00C72D3E` → [PopInitializeHighPerfPowerRequest](../C3/PopInitializeHighPerfPowerRequest_function_00C3D718.md) (function, `0x00C3D718`)
- `0x00C72D4B` → [PopCheckPowerSourceAfterRtcWakeInitialize](../../text/5D/PopCheckPowerSourceAfterRtcWakeInitialize_function_005D5A24.md) (function, `0x005D5A24`)
- `0x00C72D50` → [PopWatchdogInit](../C4/PopWatchdogInit_function_00C43330.md) (function, `0x00C43330`)
- `0x00C72D58` → [PopInitializePowerButtonHold](../C4/PopInitializePowerButtonHold_function_00C425A8.md) (function, `0x00C425A8`)
- `0x00C72D5D` → [PopInitDripsWakeAccounting](../C3/PopInitDripsWakeAccounting_function_00C3D374.md) (function, `0x00C3D374`)
- `0x00C72D86` → [EmpProviderRegister](../../page/AC/EmpProviderRegister_function_00ACC5D0.md) (function, `0x00ACC5D0`)
- `0x00C72DA9` → [EmClientQueryRuleState](../../pagelk/B7/EmClientQueryRuleState_function_00B77D70.md) (function, `0x00B77D70`)
- `0x00C72DBB` → [PopDetectSimulatedHeteroProcessors](../C4/PopDetectSimulatedHeteroProcessors_function_00C40DD8.md) (function, `0x00C40DD8`)
- `0x00C72DC4` → [PpmHeteroHgsDetectContainmentPresence](../../text/5D/PpmHeteroHgsDetectContainmentPresence_function_005D8768.md) (function, `0x005D8768`)
- `0x00C72DD7` → [PoFxRegisterDebugger](../C4/PoFxRegisterDebugger_function_00C434E0.md) (function, `0x00C434E0`)
- `0x00C72DDF` → [HalReportResourceUsage](../C1/HalReportResourceUsage_function_00C1DDC0.md) (function, `0x00C1DDC0`)
- `0x00C72DE4` → [PopBatteryInitPhaseTwo](../C4/PopBatteryInitPhaseTwo_function_00C42148.md) (function, `0x00C42148`)
- `0x00C72DE9` → [PpmEventInitialize](../C4/PpmEventInitialize_function_00C437A0.md) (function, `0x00C437A0`)
- `0x00C72E02` → [KeRegisterProcessorChangeCallback](../../page/74/KeRegisterProcessorChangeCallback_function_00746520.md) (function, `0x00746520`)
- `0x00C72E0E` → [PpmAcquireLock](../../text/2D/PpmAcquireLock_function_002D9AA4.md) (function, `0x002D9AA4`)
- `0x00C72E16` → [PopInitializeHeteroProcessors](../../page/A5/PopInitializeHeteroProcessors_function_00A53570.md) (function, `0x00A53570`)
- `0x00C72E22` → [PpmReleaseLock](../../text/2D/PpmReleaseLock_function_002DA428.md) (function, `0x002DA428`)
- `0x00C72E40` → [PpmIdleRegisterDefaultStates](../../page/75/PpmIdleRegisterDefaultStates_function_00755110.md) (function, `0x00755110`)
- `0x00C72E45` → [PpmParkInitialize](../C4/PpmParkInitialize_function_00C437EC.md) (function, `0x00C437EC`)
- `0x00C72E57` → [PpmCheckInitProcessors](../../page/A8/PpmCheckInitProcessors_function_00A84AE8.md) (function, `0x00A84AE8`)
- `0x00C72E63` → [PpmAcquireLock](../../text/2D/PpmAcquireLock_function_002D9AA4.md) (function, `0x002D9AA4`)
- `0x00C72E68` → [PoFxSendSystemLatencyUpdate](../../text/46/PoFxSendSystemLatencyUpdate_function_0046A008.md) (function, `0x0046A008`)
- `0x00C72E74` → [PpmReleaseLock](../../text/2D/PpmReleaseLock_function_002DA428.md) (function, `0x002DA428`)
- `0x00C72E79` → [PopPdcCsCheckSystemVolumeDevice](../C4/PopPdcCsCheckSystemVolumeDevice_function_00C42D9C.md) (function, `0x00C42D9C`)
- `0x00C72E80` → [PopUpdateBackgroundCoolingStatus](../../page/AD/PopUpdateBackgroundCoolingStatus_function_00AD5890.md) (function, `0x00AD5890`)
- `0x00C72EA9` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00C72EAE` → [PopInitVideoWnfState](../C3/PopInitVideoWnfState_function_00C3D684.md) (function, `0x00C3D684`)
- `0x00C72EC7` → [PopDiagInitialize](../C3/PopDiagInitialize_function_00C3F2C0.md) (function, `0x00C3F2C0`)
- `0x00C72ED7` → [SshInitialize](../C4/SshInitialize_function_00C4465C.md) (function, `0x00C4465C`)
- `0x00C72EDF` → [PopSleepstudyInitialize](PopSleepstudyInitialize_function_00C76C60.md) (function, `0x00C76C60`)
- `0x00C72EF4` → [PopTriggerDiagTraceAoAcCapability](../C4/PopTriggerDiagTraceAoAcCapability_function_00C404D4.md) (function, `0x00C404D4`)
- `0x00C72EF9` → [PopFanReportBootStartDevices](../C4/PopFanReportBootStartDevices_function_00C4289C.md) (function, `0x00C4289C`)
- `0x00C72EFE` → [PopInitializeWin32kActivator](../C3/PopInitializeWin32kActivator_function_00C3E7C4.md) (function, `0x00C3E7C4`)
- `0x00C72F03` → [PopModernStandbyNotificationInit](../C4/PopModernStandbyNotificationInit_function_00C43948.md) (function, `0x00C43948`)
- `0x00C72F0B` → [PopPowerAggregatorInitialize](PopPowerAggregatorInitialize_function_00C77B94.md) (function, `0x00C77B94`)
- `0x00C72F10` → [PopUserShutdownScenarioInitialize](../C3/PopUserShutdownScenarioInitialize_function_00C3F0D0.md) (function, `0x00C3F0D0`)
- `0x00C72F46` → [HalGetInterruptTargetInformation](../../text/4C/HalGetInterruptTargetInformation_function_004C20F0.md) (function, `0x004C20F0`)
- `0x00C72F70` → [PopCheckSkipTick](../../page/75/PopCheckSkipTick_function_007538CC.md) (function, `0x007538CC`)
- `0x00C72F96` → [PopDiagTraceSkipTick](../../page/76/PopDiagTraceSkipTick_function_00762EA8.md) (function, `0x00762EA8`)
- `0x00C72F9B` → [PpmInitIllegalThrottleLogging](../../text/5C/PpmInitIllegalThrottleLogging_function_005CE39C.md) (function, `0x005CE39C`)
- `0x00C72FA3` → [PopCheckShutdownMarker](../C3/PopCheckShutdownMarker_function_00C3DAD4.md) (function, `0x00C3DAD4`)
- `0x00C72FA8` → [PopCheckAndClearBootError](../C3/PopCheckAndClearBootError_function_00C3DA4C.md) (function, `0x00C3DA4C`)
- `0x00C72FB4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C72FD9` → [PopDiagTraceAbnormalReset](../../text/5D/PopDiagTraceAbnormalReset_function_005D5D84.md) (function, `0x005D5D84`)
- `0x00C72FDE` → [PopIdleWakeInitialize](../../page/76/PopIdleWakeInitialize_function_0076B438.md) (function, `0x0076B438`)
- `0x00C72FE3` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00C72FEA` → [PopUpdateUpgradeInProgress](../../page/75/PopUpdateUpgradeInProgress_function_00754880.md) (function, `0x00754880`)
- `0x00C73005` → [PopLogSleepDisabled](../../page/91/PopLogSleepDisabled_function_009102D8.md) (function, `0x009102D8`)
- `0x00C73020` → [PopLogSleepDisabled](../../page/91/PopLogSleepDisabled_function_009102D8.md) (function, `0x009102D8`)
- `0x00C7306C` → [PopLogSleepDisabled](../../page/91/PopLogSleepDisabled_function_009102D8.md) (function, `0x009102D8`)
- `0x00C73074` → [PopDeepSleepInitialize](../C4/PopDeepSleepInitialize_function_00C409D0.md) (function, `0x00C409D0`)
- `0x00C73079` → [PopInitializePowerPolicySimulate](../../page/A9/PopInitializePowerPolicySimulate_function_00A9DA28.md) (function, `0x00A9DA28`)
- `0x00C730F5` → [PopResetCurrentPolicies](../../page/90/PopResetCurrentPolicies_function_0090FF64.md) (function, `0x0090FF64`)
- `0x00C730FA` → [PopInitializeAdpm](../C4/PopInitializeAdpm_function_00C43B1C.md) (function, `0x00C43B1C`)
- `0x00C73102` → [PopEsInit](../C4/PopEsInit_function_00C42F24.md) (function, `0x00C42F24`)
- `0x00C73107` → [PopInitilizeAcDcSettings](../../text/48/PopInitilizeAcDcSettings_function_004828D0.md) (function, `0x004828D0`)
- `0x00C73113` → [PopUpdateConsoleDisplayState](../../page/A3/PopUpdateConsoleDisplayState_function_00A31298.md) (function, `0x00A31298`)
- `0x00C73139` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00C73141` → [PopNetInitialize](../C4/PopNetInitialize_function_00C423AC.md) (function, `0x00C423AC`)
- `0x00C73146` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00C7314B` → [PopIdleInitAoAcDozeS4Timer](../../page/76/PopIdleInitAoAcDozeS4Timer_function_0076886C.md) (function, `0x0076886C`)
- `0x00C73150` → [PopCreateIdlePhaseWatchdog](../C4/PopCreateIdlePhaseWatchdog_function_00C42D20.md) (function, `0x00C42D20`)
- `0x00C73155` → [PopInitializeSystemIdleDetection](../C4/PopInitializeSystemIdleDetection_function_00C408EC.md) (function, `0x00C408EC`)
- `0x00C73173` → [PopSetupHighPerfPowerRequest](../../page/75/PopSetupHighPerfPowerRequest_function_00753AE0.md) (function, `0x00753AE0`)
- `0x00C73178` → [PpmEnableWmiInterface](../../page/76/PpmEnableWmiInterface_function_00768604.md) (function, `0x00768604`)
- `0x00C731A7` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00C731AC` → [PopCoalescingInitialize](../C3/PopCoalescingInitialize_function_00C3EDB4.md) (function, `0x00C3EDB4`)
- `0x00C731B1` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00C731B9` → [PopInitializeDirectedDrips](../C3/PopInitializeDirectedDrips_function_00C3E6B4.md) (function, `0x00C3E6B4`)
- `0x00C731BE` → [PopDripsWatchdogInitialize](../C4/PopDripsWatchdogInitialize_function_00C43BCC.md) (function, `0x00C43BCC`)
- `0x00C731C3` → [PopSetupAudioEventNotification](../../page/75/PopSetupAudioEventNotification_function_00753A2C.md) (function, `0x00753A2C`)
- `0x00C731C8` → [PopSetupMixedRealitytNotification](../../page/75/PopSetupMixedRealitytNotification_function_00753B1C.md) (function, `0x00753B1C`)
- `0x00C731CD` → [PopSetupFullScrenVideoNotification](../../page/75/PopSetupFullScrenVideoNotification_function_00753AA4.md) (function, `0x00753AA4`)
- `0x00C731D2` → [PopSetupUserPresencePredictionNotification](../../page/75/PopSetupUserPresencePredictionNotification_function_00753C4C.md) (function, `0x00753C4C`)
- `0x00C731D7` → [PopSetupSprActiveSessionChangeNotification](../../page/75/PopSetupSprActiveSessionChangeNotification_function_00753BD4.md) (function, `0x00753BD4`)
- `0x00C731DC` → [PopSetupAirplaneModeNotification](../../page/75/PopSetupAirplaneModeNotification_function_007539F0.md) (function, `0x007539F0`)
- `0x00C731E1` → [PopSetupBluetoothChargingNotification](../../page/75/PopSetupBluetoothChargingNotification_function_00753A68.md) (function, `0x00753A68`)
- `0x00C731E6` → [PopSetupMobileHotspotNotification](../../page/75/PopSetupMobileHotspotNotification_function_00753B98.md) (function, `0x00753B98`)
- `0x00C731EB` → [PopThermalHandlePreviousShutdown](../../page/75/PopThermalHandlePreviousShutdown_function_0075F400.md) (function, `0x0075F400`)
- `0x00C73201` → [TtmInit](../../page/77/TtmInit_function_00776D80.md) (function, `0x00776D80`)
- `0x00C73206` → [PopReadErrataForIncorrectLidNotification](../C4/PopReadErrataForIncorrectLidNotification_function_00C43428.md) (function, `0x00C43428`)
- `0x00C7320B` → [PopLidReliabilityInit](../../text/5D/PopLidReliabilityInit_function_005D5308.md) (function, `0x005D5308`)
- `0x00C73210` → [PopEvaluateInputSuppressionRequired](../C4/PopEvaluateInputSuppressionRequired_function_00C40A1C.md) (function, `0x00C40A1C`)
- `0x00C73215` → [PopSetupUsb4DisplayPresenceNotification](../../page/75/PopSetupUsb4DisplayPresenceNotification_function_00753C10.md) (function, `0x00753C10`)
- `0x00C7321A` → [PopPowerButtonSuppressionInit](../C4/PopPowerButtonSuppressionInit_function_00C40B00.md) (function, `0x00C40B00`)
- `0x00C73222` → [PopBatteryQueueWork](../../text/4A/PopBatteryQueueWork_function_004AE3DC.md) (function, `0x004AE3DC`)
- `0x00C73227` → [PopSetupKsrCallbacks](../C3/PopSetupKsrCallbacks_function_00C3F21C.md) (function, `0x00C3F21C`)
- `0x00C7322C` → [PopHiberEvaluateSkippingMemoryMapValidation](../C3/PopHiberEvaluateSkippingMemoryMapValidation_function_00C3EF2C.md) (function, `0x00C3EF2C`)
- `0x00C73231` → [PopReadErrataSkipMemoryOverwriteRequestControlLockAction](../C4/PopReadErrataSkipMemoryOverwriteRequestControlLockAction_function_00C43474.md) (function, `0x00C43474`)

### Direct callers
- [Phase1InitializationDiscard](../C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1CD5E`
- [Phase1InitializationDiscard](../C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1DAD6`
- [IoInitSystemPreDrivers](../C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2BC19`
- [Phase1InitializationIoReady](Phase1InitializationIoReady_function_00C70458.md) at `0x00C705D2`

### Static image references
- `0x00C7236E` → RVA `0x00F0CA60` (`.data`; write)
- `0x00C723A4` → RVA `0x00FC6FBC` (`ALMOSTRO`; read)
- `0x00C723AB` → RVA `0x00FC6FB8` (`ALMOSTRO`; read)
- `0x00C723B2` → RVA `0x00FC6BE0` (`ALMOSTRO`; write)
- `0x00C723C3` → RVA `0x00FC6FB4` (`ALMOSTRO`; read)
- `0x00C723CA` → RVA `0x00FC6FB0` (`ALMOSTRO`; read)
- `0x00C723D8` → RVA `0x00F0CA58` (`.data`; write)
- `0x00C723F3` → RVA `0x00F0AD68` (`.data`; read)
- `0x00C723FF` → RVA `0x00F0AD70` (`.data`; write)
- `0x00C72406` → RVA `0x00E27640` (`.data`; read)
- `0x00C7240D` → RVA `0x00F0AD68` (`.data`; write)
- `0x00C7241A` → RVA `0x00F0CA40` (`.data`; read)
- `0x00C72427` → RVA `0x00F0CA48` (`.data`; write)
- `0x00C72431` → RVA `0x00F0CA40` (`.data`; write)
- `0x00C7243A` → RVA `0x00F0CA30` (`.data`; read)
- `0x00C72449` → RVA `0x00F0CA38` (`.data`; write)
- `0x00C72450` → RVA `0x00F0CA30` (`.data`; write)
- `0x00C72457` → RVA `0x00F09708` (`.data`; write)
- `0x00C7245E` → RVA `0x00F09700` (`.data`; write)
- `0x00C72465` → RVA `0x00F093E8` (`.data`; write)
- `0x00C7246C` → RVA `0x00F093E0` (`.data`; write)
- `0x00C72473` → RVA `0x00F0E078` (`.data`; write)
- `0x00C7247A` → RVA `0x00F0E070` (`.data`; write)
- `0x00C72481` → RVA `0x00F0AD60` (`.data`; write)
- `0x00C72489` → RVA `0x00F0AD62` (`.data`; write)
- `0x00C72490` → RVA `0x00F0AD64` (`.data`; write)
- `0x00C72497` → RVA `0x00F09328` (`.data`; write)
- `0x00C7249E` → RVA `0x00F0CA50` (`.data`; write)
- `0x00C724B3` → RVA `0x00F092D0` (`.data`; read)
- `0x00C724BA` → RVA `0x00F092E0` (`.data`; write)
- `0x00C724C3` → RVA `0x00F092D8` (`.data`; write)
- `0x00C724D0` → RVA `0x00F092D0` (`.data`; write)
- `0x00C724D7` → RVA `0x00F0D180` (`.data`; read)
- `0x00C724E3` → RVA `0x00F0DD80` (`.data`; read/write)
- `0x00C724EA` → RVA `0x004A3EB0` (`PopDevicePowerTransitionInProgressWorker`; read)
- `0x00C724F1` → RVA `0x00F0CA10` (`.data`; write)
- `0x00C724F8` → RVA `0x00754680` (`PopSetUserShutdownMarkerWorker`; read)
- `0x00C724FF` → RVA `0x00EFF058` (`.data`; read)
- `0x00C72505` → RVA `0x00F0F180` (`.data`; read)
- `0x00C72515` → RVA `0x00F0CA20` (`.data`; write)
- `0x00C7251C` → RVA `0x00F05C30` (`.data`; write)
- `0x00C72525` → RVA `0x00F0F1C8` (`.data`; read)
- `0x00C7252C` → RVA `0x00F0CA18` (`.data`; write)
- `0x00C72533` → RVA `0x00F0DD88` (`.data`; read)
- `0x00C7253A` → RVA `0x00F0F1D0` (`.data`; write)
- `0x00C72541` → RVA `0x00F0F1C8` (`.data`; write)
- `0x00C72548` → RVA `0x00F0DD88` (`.data`; write)
- `0x00C7254F` → RVA `0x00F0CA00` (`.data`; write)
- `0x00C72556` → RVA `0x00F05C28` (`.data`; write)
- `0x00C7255D` → RVA `0x00F05C20` (`.data`; write)
- `0x00C72564` → RVA `0x00F05C40` (`.data`; write)
- `0x00C7256B` → RVA `0x00F05C38` (`.data`; write)
- `0x00C72572` → RVA `0x00F0F1F0` (`.data`; write)
- `0x00C72579` → RVA `0x00F0F1E8` (`.data`; write)
- `0x00C72580` → RVA `0x00F0F1E0` (`.data`; write)
- `0x00C72587` → RVA `0x00F0F1C0` (`.data`; write)
- `0x00C7258F` → RVA `0x00F0F1C2` (`.data`; write)
- `0x00C72596` → RVA `0x00F0F1C4` (`.data`; write)
- `0x00C725A2` → RVA `0x00754030` (`PopClearUserShutdownMarkerWorker`; read)
- `0x00C725A9` → RVA `0x00F0F140` (`.data`; read)
- `0x00C725B5` → RVA `0x00A82590` (`PopBsdFlushWorker`; read)
- `0x00C725BC` → RVA `0x00F0F100` (`.data`; read)
- `0x00C725C8` → RVA `0x00A825D0` (`PopBsdUpdateWorker`; read)
- `0x00C725CF` → RVA `0x00F0F0C0` (`.data`; read)
- `0x00C725DB` → RVA `0x000112D0` (`.rdata`; read)
- `0x00C725E2` → RVA `0x00F0B410` (`.data`; write)
- `0x00C725E9` → RVA `0x00F0B418` (`.data`; write)
- `0x00C725F0` → RVA `0x00AB0B20` (`PopExternalMonitorUpdatedWorker`; read)
- `0x00C725F7` → RVA `0x00F092A0` (`.data`; read)
- `0x00C72603` → RVA `0x00765690` (`PopUsb4DisplayPresenceUpdatedWorker`; read)
- `0x00C7260A` → RVA `0x00F09260` (`.data`; read)
- `0x00C72616` → RVA `0x00ACD4D0` (`PopRecordLidStateWorker`; read)
- `0x00C7261D` → RVA `0x00F0EA40` (`.data`; read)
- `0x00C72629` → RVA `0x00F0F090` (`.data`; read)
- `0x00C72630` → RVA `0x00F09248` (`.data`; write)
- `0x00C72637` → RVA `0x00F0F098` (`.data`; write)
- `0x00C7263E` → RVA `0x00F0F090` (`.data`; write)
- `0x00C72645` → RVA `0x00F09240` (`.data`; write)
- `0x00C7264C` → RVA `0x00F09238` (`.data`; write)
- `0x00C72653` → RVA `0x00F09230` (`.data`; write)
- `0x00C7265A` → RVA `0x00F0F0B8` (`.data`; write)
- `0x00C72661` → RVA `0x00F0F0B0` (`.data`; write)
- `0x00C72668` → RVA `0x00F0EA20` (`.data`; write)
- `0x00C72681` → RVA `0x00F0CC10` (`.data`; read)
- `0x00C72688` → RVA `0x00F0CA80` (`.data`; write)
- `0x00C7268F` → RVA `0x00F0CC18` (`.data`; write)
- `0x00C72696` → RVA `0x00F0CC10` (`.data`; write)
- `0x00C7269D` → RVA `0x00F0CBE0` (`.data`; read)
- `0x00C726A4` → RVA `0x00F0CBE8` (`.data`; write)
- `0x00C726AB` → RVA `0x00F0CBE0` (`.data`; write)
- `0x00C726B2` → RVA `0x00F0CBD0` (`.data`; read)
- `0x00C726B9` → RVA `0x00F0CBD8` (`.data`; write)
- `0x00C726C0` → RVA `0x00F0CBD0` (`.data`; write)
- `0x00C726C7` → RVA `0x00F0B908` (`.data`; read)
- `0x00C726CE` → RVA `0x00F0B910` (`.data`; write)
- `0x00C726D5` → RVA `0x00F0B908` (`.data`; write)
- `0x00C726DC` → RVA `0x00F0CBB0` (`.data`; read)
- `0x00C726E3` → RVA `0x00F0CBB8` (`.data`; write)
- `0x00C726EA` → RVA `0x00F0CBB0` (`.data`; write)
- `0x00C726F1` → RVA `0x00F0EAA0` (`.data`; read)
- `0x00C726F8` → RVA `0x00F0EAA8` (`.data`; write)
- `0x00C726FF` → RVA `0x00F0EAA0` (`.data`; write)
- `0x00C72706` → RVA `0x00F0EA70` (`.data`; read)
- `0x00C7270D` → RVA `0x00F0EA78` (`.data`; write)
- `0x00C72714` → RVA `0x00F0EA70` (`.data`; write)
- `0x00C7271B` → RVA `0x00F0CA78` (`.data`; write)
- `0x00C72722` → RVA `0x00F0CA70` (`.data`; write)
- `0x00C72729` → RVA `0x00F0CA68` (`.data`; write)
- `0x00C72730` → RVA `0x00F0CC20` (`.data`; write)
- `0x00C72737` → RVA `0x00E27EC8` (`.data`; write)
- `0x00C7273E` → RVA `0x00F0CC08` (`.data`; write)
- `0x00C72746` → RVA `0x00F0CC0A` (`.data`; write)
- `0x00C7274D` → RVA `0x00F0CC0C` (`.data`; write)
- `0x00C72754` → RVA `0x00F0CBC0` (`.data`; write)
- `0x00C7275B` → RVA `0x00F0B900` (`.data`; write)
- `0x00C72763` → RVA `0x00F0B902` (`.data`; write)
- `0x00C7276A` → RVA `0x00F0B904` (`.data`; write)
- `0x00C72771` → RVA `0x00F0EA80` (`.data`; write)
- `0x00C72778` → RVA `0x00F0EA88` (`.data`; write)
- `0x00C7277F` → RVA `0x00F0EA90` (`.data`; write)
- `0x00C72786` → RVA `0x00F0EA98` (`.data`; write)
- `0x00C7278E` → RVA `0x00F0EA9A` (`.data`; write)
- `0x00C72795` → RVA `0x00F0EA9C` (`.data`; write)
- `0x00C727A1` → RVA `0x00E0B558` (`.data`; read)
- `0x00C727A7` → RVA `0x00F0CB90` (`.data`; read)
- `0x00C727B1` → RVA `0x00F0CB98` (`.data`; write)
- `0x00C727B8` → RVA `0x00F0CB90` (`.data`; write)
- `0x00C727BF` → RVA `0x00F0CBA0` (`.data`; write)
- `0x00C727D2` → RVA `0x00E0B558` (`.data`; write)
- `0x00C727F4` → RVA `0x00F0E78C` (`.data`; write)
- `0x00C72802` → RVA `0x00F0E788` (`.data`; write)
- `0x00C72808` → RVA `0x00491FD0` (`PopPolicyWorkerThread`; read)
- `0x00C7280F` → RVA `0x00F0CB80` (`.data`; write)
- `0x00C72816` → RVA `0x00F0CB70` (`.data`; write)
- `0x00C7281D` → RVA `0x00F0CAE0` (`.data`; read)
- `0x00C72829` → RVA `0x00F0CB60` (`.data`; write)
- `0x00C72832` → RVA `0x00F0CB78` (`.data`; write)
- `0x00C72839` → RVA `0x00F0CB48` (`.data`; write)
- `0x00C72844` → RVA `0x00F0CAC0` (`.data`; read)
- `0x00C7284B` → RVA `0x00F0CAD8` (`.data`; write)
- `0x00C72852` → RVA `0x00F0CAC8` (`.data`; write)
- `0x00C72859` → RVA `0x00F0CE80` (`.data`; read)
- `0x00C72860` → RVA `0x00F0CAC0` (`.data`; write)
- `0x00C7286C` → RVA `0x00F0DFA8` (`.data`; read)
- `0x00C72873` → RVA `0x00F0CAA0` (`.data`; write)
- `0x00C7287A` → RVA `0x00F0DFB0` (`.data`; write)
- `0x00C72881` → RVA `0x00F0DFA8` (`.data`; write)
- `0x00C72888` → RVA `0x00F0CEB0` (`.data`; read)
- `0x00C7288F` → RVA `0x00F0CEB8` (`.data`; write)
- `0x00C72896` → RVA `0x00F0CEB0` (`.data`; write)
- `0x00C7289D` → RVA `0x00F0CEA0` (`.data`; read)
- `0x00C728A4` → RVA `0x00F0CEA8` (`.data`; write)
- `0x00C728AB` → RVA `0x00F0CEA0` (`.data`; write)
- `0x00C728B2` → RVA `0x00F0CE90` (`.data`; read)
- `0x00C728B9` → RVA `0x00F0CE98` (`.data`; write)
- `0x00C728C0` → RVA `0x00F0CE90` (`.data`; write)
- `0x00C728C7` → RVA `0x00F0CAA8` (`.data`; write)
- `0x00C728CE` → RVA `0x00F0CAB0` (`.data`; write)
- `0x00C728D5` → RVA `0x00F0CAB8` (`.data`; write)
- `0x00C728DD` → RVA `0x00F0CABA` (`.data`; write)
- `0x00C728E4` → RVA `0x00F0CABC` (`.data`; write)
- `0x00C728EB` → RVA `0x00F0DFA0` (`.data`; write)
- `0x00C728F3` → RVA `0x00F0DFA2` (`.data`; write)
- `0x00C728FA` → RVA `0x00F0DFA4` (`.data`; write)
- `0x00C72901` → RVA `0x00F0CE88` (`.data`; write)
- `0x00C72908` → RVA `0x00F0CE80` (`.data`; write)
- `0x00C7290F` → RVA `0x00F09169` (`.data`; write)
- `0x00C72916` → RVA `0x00F0B928` (`.data`; write)
- `0x00C7291D` → RVA `0x00F0B920` (`.data`; write)
- `0x00C72929` → RVA `0x00F0CE70` (`.data`; read)
- `0x00C72930` → RVA `0x00F0CE78` (`.data`; write)
- `0x00C72937` → RVA `0x00F0CE70` (`.data`; write)
- `0x00C72943` → RVA `0x00F0CD24` (`.data`; read)
- `0x00C7294A` → RVA `0x00F0CE68` (`.data`; write)
- `0x00C72956` → RVA `0x00F0CD00` (`.data`; write)
- `0x00C72960` → RVA `0x00F0CD04` (`.data`; write)
- `0x00C7296B` → RVA `0x00F0CD0C` (`.data`; write)
- `0x00C72971` → RVA `0x00F0CD10` (`.data`; write)
- `0x00C72978` → RVA `0x00F0CD14` (`.data`; write)
- `0x00C7297E` → RVA `0x00F0CCE8` (`.data`; write)
- `0x00C7298E` → RVA `0x00F0DF30` (`.data`; read)
- `0x00C72995` → RVA `0x00F0DF20` (`.data`; write)
- `0x00C7299C` → RVA `0x00F0DF38` (`.data`; write)
- `0x00C729A3` → RVA `0x00F0DF30` (`.data`; write)
- `0x00C729AA` → RVA `0x00E67848` (`.data`; write)
- `0x00C729B1` → RVA `0x00E27EC0` (`.data`; write)
- `0x00C729B7` → RVA `0x00E27EC4` (`.data`; write)
- `0x00C729F0` → RVA `0x00F0C908` (`.data`; write)
- `0x00C729F7` → RVA `0x00F0C900` (`.data`; write)
- `0x00C72A08` → RVA `0x00F0BB40` (`.data`; read)
- `0x00C72A0F` → RVA `0x00F08FC0` (`.data`; write)
- `0x00C72A16` → RVA `0x00F0BB48` (`.data`; write)
- `0x00C72A1D` → RVA `0x00F0BB40` (`.data`; write)
- `0x00C72A24` → RVA `0x00F0BB60` (`.data`; read)
- `0x00C72A2B` → RVA `0x00F0BB68` (`.data`; write)
- `0x00C72A32` → RVA `0x00F0BB60` (`.data`; write)
- `0x00C72A39` → RVA `0x00B71750` (`PopShutdownHandler`; read)
- `0x00C72A40` → RVA `0x00F0CCA8` (`.data`; write)
- `0x00C72A47` → RVA `0x00F0DE90` (`.data`; read)
- `0x00C72A4E` → RVA `0x00F0DE98` (`.data`; write)
- `0x00C72A55` → RVA `0x00F0DE90` (`.data`; write)
- `0x00C72A5C` → RVA `0x00F0DEC8` (`.data`; read)
- `0x00C72A63` → RVA `0x00F0DED0` (`.data`; write)
- `0x00C72A6A` → RVA `0x00F0DEC8` (`.data`; write)
- `0x00C72A71` → RVA `0x00F0DEE0` (`.data`; read)
- `0x00C72A78` → RVA `0x00F0DEE8` (`.data`; write)
- `0x00C72A7F` → RVA `0x00F0DEE0` (`.data`; write)
- `0x00C72A86` → RVA `0x00F08FC8` (`.data`; read)
- `0x00C72A8D` → RVA `0x00F08FD0` (`.data`; write)
- `0x00C72A94` → RVA `0x00F08FC8` (`.data`; write)
- `0x00C72A9B` → RVA `0x005D97B0` (`PpmWmiIdleAccountingProcedure`; read)
- `0x00C72AA2` → RVA `0x00F08F98` (`.data`; write)
- `0x00C72AA9` → RVA `0x0049D4F0` (`PopUserPresentSetWorker`; read)
- `0x00C72AB0` → RVA `0x00F0DF10` (`.data`; write)
- `0x00C72AB7` → RVA `0x00E67738` (`.data`; read)
- `0x00C72ABE` → RVA `0x00E67740` (`.data`; write)
- `0x00C72AC5` → RVA `0x00E67738` (`.data`; write)
- `0x00C72ACC` → RVA `0x00F0D168` (`.data`; read)
- `0x00C72AD3` → RVA `0x00E67730` (`.data`; write)
- `0x00C72ADA` → RVA `0x00F0D170` (`.data`; write)
- `0x00C72AE1` → RVA `0x00F0D168` (`.data`; write)
- `0x00C72AE8` → RVA `0x00F0BB38` (`.data`; write)
- `0x00C72AEF` → RVA `0x00F0BB30` (`.data`; write)
- `0x00C72AF6` → RVA `0x00F0BB58` (`.data`; write)
- `0x00C72AFD` → RVA `0x00F0BB50` (`.data`; write)
- `0x00C72B04` → RVA `0x00F0CCA0` (`.data`; write)
- `0x00C72B0E` → RVA `0x00F0CCA4` (`.data`; write)
- `0x00C72B15` → RVA `0x00F0DEA0` (`.data`; write)
- `0x00C72B1C` → RVA `0x00F0DEB0` (`.data`; write)
- `0x00C72B23` → RVA `0x00F0DEA8` (`.data`; write)
- `0x00C72B2A` → RVA `0x00F0DEC0` (`.data`; write)
- `0x00C72B32` → RVA `0x00F0DEC2` (`.data`; write)
- `0x00C72B39` → RVA `0x00F0DEC4` (`.data`; write)
- `0x00C72B40` → RVA `0x00F0DEF0` (`.data`; write)
- `0x00C72B4E` → RVA `0x00F08FD8` (`.data`; write)
- `0x00C72B55` → RVA `0x00F08FFC` (`.data`; write)
- `0x00C72B5C` → RVA `0x00F08FF8` (`.data`; write)
- `0x00C72B64` → RVA `0x00F08F80` (`.data`; write)
- `0x00C72B6E` → RVA `0x00F08FA0` (`.data`; write)
- `0x00C72B75` → RVA `0x00F08FB8` (`.data`; write)
- `0x00C72B7C` → RVA `0x00F08F90` (`.data`; write)
- `0x00C72B83` → RVA `0x00F0DEF8` (`.data`; write)
- `0x00C72B8A` → RVA `0x00F0DF18` (`.data`; write)
- `0x00C72B91` → RVA `0x00F0DF00` (`.data`; write)
- `0x00C72B9F` → RVA `0x00E67748` (`.data`; write)
- `0x00C72BA6` → RVA `0x00E6776C` (`.data`; write)
- `0x00C72BAD` → RVA `0x00E67768` (`.data`; write)
- `0x00C72BB5` → RVA `0x00F0D160` (`.data`; write)
- `0x00C72BBD` → RVA `0x00F0D162` (`.data`; write)
- `0x00C72BC4` → RVA `0x00F0D164` (`.data`; write)
- `0x00C72BD0` → RVA `0x00F0E770` (`.data`; read)
- `0x00C72BD7` → RVA `0x00F0E768` (`.data`; write)
- `0x00C72BDF` → RVA `0x00F0E778` (`.data`; write)
- `0x00C72BE6` → RVA `0x00F0E770` (`.data`; write)
- `0x00C72BED` → RVA `0x00F0E76A` (`.data`; write)
- `0x00C72BF4` → RVA `0x00F0E76C` (`.data`; write)
- `0x00C72C05` → RVA `0x00F0CE2C` (`.data`; write)
- `0x00C72C0E` → RVA `0x00F0CE30` (`.data`; write)
- `0x00C72C15` → RVA `0x00F0CE38` (`.data`; write)
- `0x00C72C1C` → RVA `0x00F0CE40` (`.data`; write)
- `0x00C72C2E` → RVA `0x00F08508` (`.data`; write)
- `0x00C72C35` → RVA `0x00F08500` (`.data`; write)
- `0x00C72C7B` → RVA `0x00FC535C` (`ALMOSTRO`; write)
- `0x00C72C82` → RVA `0x00E67668` (`.data`; write)
- `0x00C72C8B` → RVA `0x00F0C918` (`.data`; write)
- `0x00C72C92` → RVA `0x00F0C910` (`.data`; write)
- `0x00C72C99` → RVA `0x00F0C98C` (`.data`; write)
- `0x00C72CA5` → RVA `0x00FC6FC8` (`ALMOSTRO`; read)
- `0x00C72CB0` → RVA `0x00F0CFA8` (`.data`; write)
- `0x00C72CB9` → RVA `0x00F0D130` (`.data`; write)
- `0x00C72CC0` → RVA `0x00F0D138` (`.data`; write)
- `0x00C72CC7` → RVA `0x00F0D128` (`.data`; write)
- `0x00C72CCE` → RVA `0x00F0D120` (`.data`; write)
- `0x00C72CE4` → RVA `0x007696F0` (`PopDelayedPdcRegistrationWorker`; read)
- `0x00C72CEB` → RVA `0x00F08450` (`.data`; write)
- `0x00C72CF5` → RVA `0x00F08470` (`.data`; write)
- `0x00C72CFC` → RVA `0x00F08478` (`.data`; write)
- `0x00C72D03` → RVA `0x00F08460` (`.data`; write)
- `0x00C72D6E` → RVA `0x00008700` (`.rdata`; read)
- `0x00C72D75` → RVA `0x0000B4D0` (`.rdata`; read)
- `0x00C72D9B` → RVA `0x000296F8` (`.rdata`; read)
- `0x00C72DA2` → RVA `0x00F083F1` (`.data`; write)
- `0x00C72DF9` → RVA `0x007539A0` (`PopNewProcessorCallback`; read)
- `0x00C72E07` → RVA `0x00F0CC00` (`.data`; read)
- `0x00C72E27` → RVA `0x00FC5194` (`ALMOSTRO`; read)
- `0x00C72E3A` → RVA `0x00FC6CD4` (`ALMOSTRO`; write)
- `0x00C72E5C` → RVA `0x00F0E760` (`.data`; read)
- `0x00C72E92` → RVA `0x00F0E174` (`.data`; read)
- `0x00C72E99` → RVA `0x00020B10` (`.rdata`; read)
- `0x00C72EE4` → RVA `0x00E673A0` (`.data`; read)
- `0x00C72EEE` → RVA `0x00E6739C` (`.data`; read)
- `0x00C72F1D` → RVA `0x00FC5290` (`ALMOSTRO`; read)
- `0x00C72F52` → RVA `0x00FC5190` (`ALMOSTRO`; write)
- `0x00C72F60` → RVA `0x00FC5360` (`ALMOSTRO`; write)
- `0x00C72F66` → RVA `0x00FC5320` (`ALMOSTRO`; write)
- `0x00C72F7D` → RVA `0x00FC50DC` (`ALMOSTRO`; write)
- `0x00C72FAD` → RVA `0x00E00B30` (`.data`; read)
- `0x00C72FBD` → RVA `0x00F0F200` (`.data`; read)
- `0x00C72FCA` → RVA `0x00F0F204` (`.data`; read)
- `0x00C72FEF` → RVA `0x00FC4148` (`.data`; read)
- `0x00C7300A` → RVA `0x00F0CED4` (`.data`; read)
- `0x00C73038` → RVA `0x00F0DE60` (`.data`; write)
- `0x00C73044` → RVA `0x00FC6A90` (`ALMOSTRO`; read)
- `0x00C7304E` → RVA `0x00FC6A84` (`ALMOSTRO`; read)
- `0x00C7307E` → RVA `0x00F0CF0C` (`.data`; read)
- `0x00C7308E` → RVA `0x00F0CEDE` (`.data`; write)
- `0x00C73095` → RVA `0x00F0CEE0` (`.data`; write)
- `0x00C7309B` → RVA `0x00F0CEE4` (`.data`; write)
- `0x00C730A5` → RVA `0x00F0CEE8` (`.data`; write)
- `0x00C730AF` → RVA `0x00F0CEEC` (`.data`; write)
- `0x00C730B9` → RVA `0x00F0CF00` (`.data`; write)
- `0x00C730C3` → RVA `0x00F0CF08` (`.data`; write)
- `0x00C730D2` → RVA `0x00F0CEC0` (`.data`; write)
- `0x00C730DC` → RVA `0x00F0CEC4` (`.data`; write)
- `0x00C730E5` → RVA `0x00F0CEC6` (`.data`; write)
- `0x00C730EC` → RVA `0x00F0CED1` (`.data`; write)
- `0x00C73129` → RVA `0x00020AE8` (`.rdata`; read)
- `0x00C7316D` → RVA `0x00F0DE81` (`.data`; write)
- `0x00C73191` → RVA `0x00F0DE80` (`.data`; write)
- `0x00C7319F` → RVA `0x00F0DE70` (`.data`; write)
- `0x00C731FB` → RVA `0x00F084F8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **72**
  - `0x00C7239B` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C723B9` → [PopComputeCounterShifts](../../text/4F/PopComputeCounterShifts_function_004F8178.md) (`INIT` → `.text`)
  - `0x00C723D1` → [PopComputeCounterShifts](../../text/4F/PopComputeCounterShifts_function_004F8178.md) (`INIT` → `.text`)
  - `0x00C724AE` → [ExInitializeNPagedLookasideListInternal](../../text/46/ExInitializeNPagedLookasideListInternal_function_00468720.md) (`INIT` → `.text`)
  - `0x00C724DE` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C7259D` → [PopInitializeWorkItem](../../page/75/PopInitializeWorkItem_function_007540C8.md) (`INIT` → `PAGE`)
  - `0x00C725B0` → [PopInitializeWorkItem](../../page/75/PopInitializeWorkItem_function_007540C8.md) (`INIT` → `PAGE`)
  - `0x00C725C3` → [PopInitializeWorkItem](../../page/75/PopInitializeWorkItem_function_007540C8.md) (`INIT` → `PAGE`)
  - `0x00C725D6` → [PopInitializeWorkItem](../../page/75/PopInitializeWorkItem_function_007540C8.md) (`INIT` → `PAGE`)
  - `0x00C725FE` → [PopInitializeWorkItem](../../page/75/PopInitializeWorkItem_function_007540C8.md) (`INIT` → `PAGE`)
  - `0x00C72611` → [PopInitializeWorkItem](../../page/75/PopInitializeWorkItem_function_007540C8.md) (`INIT` → `PAGE`)
  - `0x00C72624` → [PopInitializeWorkItem](../../page/75/PopInitializeWorkItem_function_007540C8.md) (`INIT` → `PAGE`)
  - `0x00C7283F` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (`INIT` → `.text`)
  - `0x00C72924` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`INIT` → `.text`)
  - `0x00C7293E` → [PopResetActionDefaults](../../page/70/PopResetActionDefaults_function_007058E0.md) (`INIT` → `PAGE`)
  - `0x00C72951` → [PopDefaultPolicy](../../page/75/PopDefaultPolicy_function_00753924.md) (`INIT` → `PAGE`)
  - `0x00C72985` → [Feature_VpciVscBootDiskHibernation__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_VpciVscBootDiskHibernation__private_IsEnabledDeviceUsageNoInline_function_005CE348.md) (`INIT` → `.text`)
  - `0x00C729DA` → [PpmIdleRegisterDefaultStates](../../page/75/PpmIdleRegisterDefaultStates_function_00755110.md) (`INIT` → `PAGE`)
  - `0x00C729EB` → [PopInitilizeAcDcSettings](../../text/48/PopInitilizeAcDcSettings_function_004828D0.md) (`INIT` → `.text`)
  - `0x00C72C72` → [HviIsAnyHypervisorPresent](../../text/4A/HviIsAnyHypervisorPresent_function_004ADC50.md) (`INIT` → `.text`)
  - `0x00C72CA0` → [PopSendFanNoiseChangeWnf](../../page/76/PopSendFanNoiseChangeWnf_function_00769240.md) (`INIT` → `PAGE`)
  - `0x00C72D4B` → [PopCheckPowerSourceAfterRtcWakeInitialize](../../text/5D/PopCheckPowerSourceAfterRtcWakeInitialize_function_005D5A24.md) (`INIT` → `.text`)
  - `0x00C72D86` → [EmpProviderRegister](../../page/AC/EmpProviderRegister_function_00ACC5D0.md) (`INIT` → `PAGE`)
  - `0x00C72DA9` → [EmClientQueryRuleState](../../pagelk/B7/EmClientQueryRuleState_function_00B77D70.md) (`INIT` → `PAGELK`)
  - `0x00C72DC4` → [PpmHeteroHgsDetectContainmentPresence](../../text/5D/PpmHeteroHgsDetectContainmentPresence_function_005D8768.md) (`INIT` → `.text`)
  - `0x00C72E02` → [KeRegisterProcessorChangeCallback](../../page/74/KeRegisterProcessorChangeCallback_function_00746520.md) (`INIT` → `PAGE`)
  - `0x00C72E0E` → [PpmAcquireLock](../../text/2D/PpmAcquireLock_function_002D9AA4.md) (`INIT` → `.text`)
  - `0x00C72E16` → [PopInitializeHeteroProcessors](../../page/A5/PopInitializeHeteroProcessors_function_00A53570.md) (`INIT` → `PAGE`)
  - `0x00C72E22` → [PpmReleaseLock](../../text/2D/PpmReleaseLock_function_002DA428.md) (`INIT` → `.text`)
  - `0x00C72E40` → [PpmIdleRegisterDefaultStates](../../page/75/PpmIdleRegisterDefaultStates_function_00755110.md) (`INIT` → `PAGE`)
  - `0x00C72E57` → [PpmCheckInitProcessors](../../page/A8/PpmCheckInitProcessors_function_00A84AE8.md) (`INIT` → `PAGE`)
  - `0x00C72E63` → [PpmAcquireLock](../../text/2D/PpmAcquireLock_function_002D9AA4.md) (`INIT` → `.text`)
  - `0x00C72E68` → [PoFxSendSystemLatencyUpdate](../../text/46/PoFxSendSystemLatencyUpdate_function_0046A008.md) (`INIT` → `.text`)
  - `0x00C72E74` → [PpmReleaseLock](../../text/2D/PpmReleaseLock_function_002DA428.md) (`INIT` → `.text`)
  - `0x00C72E80` → [PopUpdateBackgroundCoolingStatus](../../page/AD/PopUpdateBackgroundCoolingStatus_function_00AD5890.md) (`INIT` → `PAGE`)
  - `0x00C72EA9` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`INIT` → `.text`)
  - `0x00C72F46` → [HalGetInterruptTargetInformation](../../text/4C/HalGetInterruptTargetInformation_function_004C20F0.md) (`INIT` → `.text`)
  - `0x00C72F70` → [PopCheckSkipTick](../../page/75/PopCheckSkipTick_function_007538CC.md) (`INIT` → `PAGE`)
  - `0x00C72F96` → [PopDiagTraceSkipTick](../../page/76/PopDiagTraceSkipTick_function_00762EA8.md) (`INIT` → `PAGE`)
  - `0x00C72F9B` → [PpmInitIllegalThrottleLogging](../../text/5C/PpmInitIllegalThrottleLogging_function_005CE39C.md) (`INIT` → `.text`)
  - `0x00C72FB4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C72FD9` → [PopDiagTraceAbnormalReset](../../text/5D/PopDiagTraceAbnormalReset_function_005D5D84.md) (`INIT` → `.text`)
  - `0x00C72FDE` → [PopIdleWakeInitialize](../../page/76/PopIdleWakeInitialize_function_0076B438.md) (`INIT` → `PAGE`)
  - `0x00C72FE3` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`INIT` → `PAGELK`)
  - `0x00C72FEA` → [PopUpdateUpgradeInProgress](../../page/75/PopUpdateUpgradeInProgress_function_00754880.md) (`INIT` → `PAGE`)
  - `0x00C73005` → [PopLogSleepDisabled](../../page/91/PopLogSleepDisabled_function_009102D8.md) (`INIT` → `PAGE`)
  - `0x00C73020` → [PopLogSleepDisabled](../../page/91/PopLogSleepDisabled_function_009102D8.md) (`INIT` → `PAGE`)
  - `0x00C7306C` → [PopLogSleepDisabled](../../page/91/PopLogSleepDisabled_function_009102D8.md) (`INIT` → `PAGE`)
  - `0x00C73079` → [PopInitializePowerPolicySimulate](../../page/A9/PopInitializePowerPolicySimulate_function_00A9DA28.md) (`INIT` → `PAGE`)
  - `0x00C730F5` → [PopResetCurrentPolicies](../../page/90/PopResetCurrentPolicies_function_0090FF64.md) (`INIT` → `PAGE`)
  - `0x00C73107` → [PopInitilizeAcDcSettings](../../text/48/PopInitilizeAcDcSettings_function_004828D0.md) (`INIT` → `.text`)
  - `0x00C73113` → [PopUpdateConsoleDisplayState](../../page/A3/PopUpdateConsoleDisplayState_function_00A31298.md) (`INIT` → `PAGE`)
  - `0x00C73139` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`INIT` → `.text`)
  - `0x00C73146` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`INIT` → `PAGELK`)
  - `0x00C7314B` → [PopIdleInitAoAcDozeS4Timer](../../page/76/PopIdleInitAoAcDozeS4Timer_function_0076886C.md) (`INIT` → `PAGE`)
  - `0x00C73173` → [PopSetupHighPerfPowerRequest](../../page/75/PopSetupHighPerfPowerRequest_function_00753AE0.md) (`INIT` → `PAGE`)
  - `0x00C73178` → [PpmEnableWmiInterface](../../page/76/PpmEnableWmiInterface_function_00768604.md) (`INIT` → `PAGE`)
  - `0x00C731A7` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`INIT` → `PAGELK`)
  - `0x00C731B1` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`INIT` → `PAGELK`)
  - `0x00C731C3` → [PopSetupAudioEventNotification](../../page/75/PopSetupAudioEventNotification_function_00753A2C.md) (`INIT` → `PAGE`)
  - `0x00C731C8` → [PopSetupMixedRealitytNotification](../../page/75/PopSetupMixedRealitytNotification_function_00753B1C.md) (`INIT` → `PAGE`)
  - `0x00C731CD` → [PopSetupFullScrenVideoNotification](../../page/75/PopSetupFullScrenVideoNotification_function_00753AA4.md) (`INIT` → `PAGE`)
  - `0x00C731D2` → [PopSetupUserPresencePredictionNotification](../../page/75/PopSetupUserPresencePredictionNotification_function_00753C4C.md) (`INIT` → `PAGE`)
  - `0x00C731D7` → [PopSetupSprActiveSessionChangeNotification](../../page/75/PopSetupSprActiveSessionChangeNotification_function_00753BD4.md) (`INIT` → `PAGE`)
  - `0x00C731DC` → [PopSetupAirplaneModeNotification](../../page/75/PopSetupAirplaneModeNotification_function_007539F0.md) (`INIT` → `PAGE`)
  - `0x00C731E1` → [PopSetupBluetoothChargingNotification](../../page/75/PopSetupBluetoothChargingNotification_function_00753A68.md) (`INIT` → `PAGE`)
  - `0x00C731E6` → [PopSetupMobileHotspotNotification](../../page/75/PopSetupMobileHotspotNotification_function_00753B98.md) (`INIT` → `PAGE`)
  - `0x00C731EB` → [PopThermalHandlePreviousShutdown](../../page/75/PopThermalHandlePreviousShutdown_function_0075F400.md) (`INIT` → `PAGE`)
  - `0x00C73201` → [TtmInit](../../page/77/TtmInit_function_00776D80.md) (`INIT` → `PAGE`)
  - `0x00C7320B` → [PopLidReliabilityInit](../../text/5D/PopLidReliabilityInit_function_005D5308.md) (`INIT` → `.text`)
  - `0x00C73215` → [PopSetupUsb4DisplayPresenceNotification](../../page/75/PopSetupUsb4DisplayPresenceNotification_function_00753C10.md) (`INIT` → `PAGE`)
  - `0x00C73222` → [PopBatteryQueueWork](../../text/4A/PopBatteryQueueWork_function_004AE3DC.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C72358  40 55                           push rbp
00C7235A  56                              push rsi
00C7235B  57                              push rdi
00C7235C  41 54                           push r12
00C7235E  41 55                           push r13
00C72360  41 56                           push r14
00C72362  41 57                           push r15
00C72364  48 8B EC                        mov rbp, rsp
00C72367  48 83 EC 60                     sub rsp, 0x60
00C7236B  45 33 FF                        xor r15d, r15d
00C7236E  89 0D EC A6 29 00               mov dword ptr [rip + 0x29a6ec], ecx
00C72374  33 C0                           xor eax, eax
00C72376  4C 89 7D 58                     mov qword ptr [rbp + 0x58], r15
00C7237A  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00C7237E  0F 57 C0                        xorps xmm0, xmm0
00C72381  89 45 F8                        mov dword ptr [rbp - 8], eax
00C72384  48 8B FA                        mov rdi, rdx
00C72387  45 8D 67 01                     lea r12d, [r15 + 1]
00C7238B  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00C7238F  85 C9                           test ecx, ecx
00C72391  0F 85 D2 08 00 00               jne 0x140c72c69
00C72397  48 8D 4D 58                     lea rcx, [rbp + 0x58]
00C7239B  E8 40 C4 70 FF                  call 0x14037e7e0
00C723A0  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
00C723A4  4C 8D 05 11 4C 35 00            lea r8, [rip + 0x354c11]
00C723AB  48 8D 15 06 4C 35 00            lea rdx, [rip + 0x354c06]
00C723B2  48 89 0D 27 48 35 00            mov qword ptr [rip + 0x354827], rcx
00C723B9  E8 BA 5D 88 FF                  call 0x1404f8178
00C723BE  B9 80 96 98 00                  mov ecx, 0x989680
00C723C3  4C 8D 05 EA 4B 35 00            lea r8, [rip + 0x354bea]
00C723CA  48 8D 15 DF 4B 35 00            lea rdx, [rip + 0x354bdf]
00C723D1  E8 A2 5D 88 FF                  call 0x1404f8178
00C723D6  33 C9                           xor ecx, ecx
00C723D8  4C 89 3D 79 A6 29 00            mov qword ptr [rip + 0x29a679], r15
00C723DF  E8 7C 48 00 00                  call 0x140c76c60
00C723E4  33 C9                           xor ecx, ecx
00C723E6  E8 A9 57 00 00                  call 0x140c77b94
00C723EB  85 C0                           test eax, eax
00C723ED  0F 88 46 0E 00 00               js 0x140c73239
00C723F3  48 8D 05 6E 89 29 00            lea rax, [rip + 0x29896e]
00C723FA  44 89 7C 24 38                  mov dword ptr [rsp + 0x38], r15d
00C723FF  48 89 05 6A 89 29 00            mov qword ptr [rip + 0x29896a], rax
00C72406  48 8D 0D 33 52 1B 00            lea rcx, [rip + 0x1b5233]
00C7240D  48 89 05 54 89 29 00            mov qword ptr [rip + 0x298954], rax
00C72414  41 B9 00 02 00 00               mov r9d, 0x200
00C7241A  48 8D 05 1F A6 29 00            lea rax, [rip + 0x29a61f]
00C72421  66 44 89 7C 24 30               mov word ptr [rsp + 0x30], r15w
00C72427  48 89 05 1A A6 29 00            mov qword ptr [rip + 0x29a61a], rax
00C7242E  45 33 C0                        xor r8d, r8d
00C72431  48 89 05 08 A6 29 00            mov qword ptr [rip + 0x29a608], rax
00C72438  33 D2                           xor edx, edx
00C7243A  48 8D 05 EF A5 29 00            lea rax, [rip + 0x29a5ef]
00C72441  C7 44 24 28 50 6F 49 72         mov dword ptr [rsp + 0x28], 0x72496f50
00C72449  48 89 05 E8 A5 29 00            mov qword ptr [rip + 0x29a5e8], rax
00C72450  48 89 05 D9 A5 29 00            mov qword ptr [rip + 0x29a5d9], rax
00C72457  4C 89 3D AA 72 29 00            mov qword ptr [rip + 0x2972aa], r15
00C7245E  4C 89 3D 9B 72 29 00            mov qword ptr [rip + 0x29729b], r15
00C72465  4C 89 3D 7C 6F 29 00            mov qword ptr [rip + 0x296f7c], r15
00C7246C  4C 89 3D 6D 6F 29 00            mov qword ptr [rip + 0x296f6d], r15
00C72473  4C 89 3D FE BB 29 00            mov qword ptr [rip + 0x29bbfe], r15
00C7247A  4C 89 3D EF BB 29 00            mov qword ptr [rip + 0x29bbef], r15
00C72481  66 44 89 3D D7 88 29 00         mov word ptr [rip + 0x2988d7], r15w
00C72489  C6 05 D2 88 29 00 06            mov byte ptr [rip + 0x2988d2], 6
00C72490  44 89 3D CD 88 29 00            mov dword ptr [rip + 0x2988cd], r15d
00C72497  4C 89 3D 8A 6E 29 00            mov qword ptr [rip + 0x296e8a], r15
00C7249E  4C 89 3D AB A5 29 00            mov qword ptr [rip + 0x29a5ab], r15
00C724A5  48 C7 44 24 20 38 01 00 00      mov qword ptr [rsp + 0x20], 0x138
00C724AE  E8 6D 62 7F FF                  call 0x140468720
00C724B3  48 8D 05 16 6E 29 00            lea rax, [rip + 0x296e16]
00C724BA  4C 89 3D 1F 6E 29 00            mov qword ptr [rip + 0x296e1f], r15
00C724C1  33 D2                           xor edx, edx
00C724C3  48 89 05 0E 6E 29 00            mov qword ptr [rip + 0x296e0e], rax
00C724CA  41 B8 18 0C 00 00               mov r8d, 0xc18
00C724D0  48 89 05 F9 6D 29 00            mov qword ptr [rip + 0x296df9], rax
00C724D7  48 8D 0D A2 AC 29 00            lea rcx, [rip + 0x29aca2]
00C724DE  E8 5D 47 A5 FF                  call 0x1406c6c40
00C724E3  83 0D 96 B8 29 00 FF            or dword ptr [rip + 0x29b896], 0xffffffff
00C724EA  48 8D 05 BF 19 83 FF            lea rax, [rip - 0x7ce641]
00C724F1  48 89 05 18 A5 29 00            mov qword ptr [rip + 0x29a518], rax
00C724F8  48 8D 15 81 21 AE FF            lea rdx, [rip - 0x51de7f]
00C724FF  8A 05 53 CB 28 00               mov al, byte ptr [rip + 0x28cb53]
00C72505  48 8D 0D 74 CC 29 00            lea rcx, [rip + 0x29cc74]
00C7250C  C0 E8 02                        shr al, 2
00C7250F  0F 57 C0                        xorps xmm0, xmm0
00C72512  41 22 C4                        and al, r12b
00C72515  4C 89 3D 04 A5 29 00            mov qword ptr [rip + 0x29a504], r15
00C7251C  88 05 0E 37 29 00               mov byte ptr [rip + 0x29370e], al
00C72522  45 33 C0                        xor r8d, r8d
00C72525  48 8D 05 9C CC 29 00            lea rax, [rip + 0x29cc9c]
00C7252C  4C 89 3D E5 A4 29 00            mov qword ptr [rip + 0x29a4e5], r15
00C72533  0F 11 05 4E B8 29 00            movups xmmword ptr [rip + 0x29b84e], xmm0
00C7253A  48 89 05 8F CC 29 00            mov qword ptr [rip + 0x29cc8f], rax
00C72541  48 89 05 80 CC 29 00            mov qword ptr [rip + 0x29cc80], rax
00C72548  4C 89 3D 39 B8 29 00            mov qword ptr [rip + 0x29b839], r15
00C7254F  4C 89 3D AA A4 29 00            mov qword ptr [rip + 0x29a4aa], r15
00C72556  4C 89 3D CB 36 29 00            mov qword ptr [rip + 0x2936cb], r15
00C7255D  44 88 3D BC 36 29 00            mov byte ptr [rip + 0x2936bc], r15b
00C72564  44 88 3D D5 36 29 00            mov byte ptr [rip + 0x2936d5], r15b
00C7256B  4C 89 3D C6 36 29 00            mov qword ptr [rip + 0x2936c6], r15
00C72572  44 88 3D 77 CC 29 00            mov byte ptr [rip + 0x29cc77], r15b
00C72579  4C 89 3D 68 CC 29 00            mov qword ptr [rip + 0x29cc68], r15
00C72580  4C 89 3D 59 CC 29 00            mov qword ptr [rip + 0x29cc59], r15
00C72587  66 44 89 25 31 CC 29 00         mov word ptr [rip + 0x29cc31], r12w
00C7258F  C6 05 2C CC 29 00 06            mov byte ptr [rip + 0x29cc2c], 6
00C72596  44 89 25 27 CC 29 00            mov dword ptr [rip + 0x29cc27], r12d
00C7259D  E8 26 1B AE FF                  call 0x1407540c8
00C725A2  48 8D 15 87 1A AE FF            lea rdx, [rip - 0x51e579]
00C725A9  48 8D 0D 90 CB 29 00            lea rcx, [rip + 0x29cb90]
00C725B0  E8 13 1B AE FF                  call 0x1407540c8
00C725B5  48 8D 15 D4 FF E0 FF            lea rdx, [rip - 0x1f002c]
00C725BC  48 8D 0D 3D CB 29 00            lea rcx, [rip + 0x29cb3d]
00C725C3  E8 00 1B AE FF                  call 0x1407540c8
00C725C8  48 8D 15 01 00 E1 FF            lea rdx, [rip - 0x1effff]
00C725CF  48 8D 0D EA CA 29 00            lea rcx, [rip + 0x29caea]
00C725D6  E8 ED 1A AE FF                  call 0x1407540c8
00C725DB  48 8D 0D EE EC 39 FF            lea rcx, [rip - 0xc61312]
00C725E2  4C 89 3D 27 8E 29 00            mov qword ptr [rip + 0x298e27], r15
00C725E9  48 89 0D 28 8E 29 00            mov qword ptr [rip + 0x298e28], rcx
00C725F0  48 8D 15 29 E5 E3 FF            lea rdx, [rip - 0x1c1ad7]
00C725F7  48 8D 0D A2 6C 29 00            lea rcx, [rip + 0x296ca2]
00C725FE  E8 C5 1A AE FF                  call 0x1407540c8
00C72603  48 8D 15 86 30 AF FF            lea rdx, [rip - 0x50cf7a]
00C7260A  48 8D 0D 4F 6C 29 00            lea rcx, [rip + 0x296c4f]
00C72611  E8 B2 1A AE FF                  call 0x1407540c8
00C72616  48 8D 15 B3 AE E5 FF            lea rdx, [rip - 0x1a514d]
00C7261D  48 8D 0D 1C C4 29 00            lea rcx, [rip + 0x29c41c]
00C72624  E8 9F 1A AE FF                  call 0x1407540c8
00C72629  48 8D 05 60 CA 29 00            lea rax, [rip + 0x29ca60]
00C72630  4C 89 3D 11 6C 29 00            mov qword ptr [rip + 0x296c11], r15
00C72637  48 89 05 5A CA 29 00            mov qword ptr [rip + 0x29ca5a], rax
00C7263E  48 89 05 4B CA 29 00            mov qword ptr [rip + 0x29ca4b], rax
00C72645  4C 89 3D F4 6B 29 00            mov qword ptr [rip + 0x296bf4], r15
00C7264C  4C 89 3D E5 6B 29 00            mov qword ptr [rip + 0x296be5], r15
00C72653  4C 89 3D D6 6B 29 00            mov qword ptr [rip + 0x296bd6], r15
00C7265A  4C 89 3D 57 CA 29 00            mov qword ptr [rip + 0x29ca57], r15
00C72661  4C 89 3D 48 CA 29 00            mov qword ptr [rip + 0x29ca48], r15
00C72668  44 88 3D B1 C3 29 00            mov byte ptr [rip + 0x29c3b1], r15b
00C7266F  E8 04 DF FC FF                  call 0x140c40578
00C72674  E8 EB E5 FC FF                  call 0x140c40c64
00C72679  85 C0                           test eax, eax
00C7267B  0F 88 B8 0B 00 00               js 0x140c73239
00C72681  48 8D 05 88 A5 29 00            lea rax, [rip + 0x29a588]
00C72688  4C 89 3D F1 A3 29 00            mov qword ptr [rip + 0x29a3f1], r15
00C7268F  48 89 05 82 A5 29 00            mov qword ptr [rip + 0x29a582], rax
00C72696  48 89 05 73 A5 29 00            mov qword ptr [rip + 0x29a573], rax
00C7269D  48 8D 05 3C A5 29 00            lea rax, [rip + 0x29a53c]
00C726A4  48 89 05 3D A5 29 00            mov qword ptr [rip + 0x29a53d], rax
00C726AB  48 89 05 2E A5 29 00            mov qword ptr [rip + 0x29a52e], rax
00C726B2  48 8D 05 17 A5 29 00            lea rax, [rip + 0x29a517]
00C726B9  48 89 05 18 A5 29 00            mov qword ptr [rip + 0x29a518], rax
00C726C0  48 89 05 09 A5 29 00            mov qword ptr [rip + 0x29a509], rax
00C726C7  48 8D 05 3A 92 29 00            lea rax, [rip + 0x29923a]
00C726CE  48 89 05 3B 92 29 00            mov qword ptr [rip + 0x29923b], rax
00C726D5  48 89 05 2C 92 29 00            mov qword ptr [rip + 0x29922c], rax
00C726DC  48 8D 05 CD A4 29 00            lea rax, [rip + 0x29a4cd]
00C726E3  48 89 05 CE A4 29 00            mov qword ptr [rip + 0x29a4ce], rax
00C726EA  48 89 05 BF A4 29 00            mov qword ptr [rip + 0x29a4bf], rax
00C726F1  48 8D 05 A8 C3 29 00            lea rax, [rip + 0x29c3a8]
00C726F8  48 89 05 A9 C3 29 00            mov qword ptr [rip + 0x29c3a9], rax
00C726FF  48 89 05 9A C3 29 00            mov qword ptr [rip + 0x29c39a], rax
00C72706  48 8D 05 63 C3 29 00            lea rax, [rip + 0x29c363]
00C7270D  48 89 05 64 C3 29 00            mov qword ptr [rip + 0x29c364], rax
00C72714  48 89 05 55 C3 29 00            mov qword ptr [rip + 0x29c355], rax
00C7271B  4C 89 3D 56 A3 29 00            mov qword ptr [rip + 0x29a356], r15
00C72722  4C 89 3D 47 A3 29 00            mov qword ptr [rip + 0x29a347], r15
00C72729  4C 89 3D 38 A3 29 00            mov qword ptr [rip + 0x29a338], r15
00C72730  4C 89 3D E9 A4 29 00            mov qword ptr [rip + 0x29a4e9], r15
00C72737  4C 89 3D 8A 57 1B 00            mov qword ptr [rip + 0x1b578a], r15
00C7273E  66 44 89 25 C2 A4 29 00         mov word ptr [rip + 0x29a4c2], r12w
00C72746  C6 05 BD A4 29 00 06            mov byte ptr [rip + 0x29a4bd], 6
00C7274D  44 89 25 B8 A4 29 00            mov dword ptr [rip + 0x29a4b8], r12d
00C72754  4C 89 3D 65 A4 29 00            mov qword ptr [rip + 0x29a465], r15
00C7275B  66 44 89 25 9D 91 29 00         mov word ptr [rip + 0x29919d], r12w
00C72763  C6 05 98 91 29 00 06            mov byte ptr [rip + 0x299198], 6
00C7276A  44 89 25 93 91 29 00            mov dword ptr [rip + 0x299193], r12d
00C72771  44 89 25 08 C3 29 00            mov dword ptr [rip + 0x29c308], r12d
00C72778  4C 89 3D 09 C3 29 00            mov qword ptr [rip + 0x29c309], r15
00C7277F  44 89 3D 0A C3 29 00            mov dword ptr [rip + 0x29c30a], r15d
00C72786  66 44 89 25 0A C3 29 00         mov word ptr [rip + 0x29c30a], r12w
00C7278E  C6 05 05 C3 29 00 06            mov byte ptr [rip + 0x29c305], 6
00C72795  44 89 3D 00 C3 29 00            mov dword ptr [rip + 0x29c300], r15d
00C7279C  E8 77 C5 FC FF                  call 0x140c3ed18
00C727A1  8B 0D B1 8D 19 00               mov ecx, dword ptr [rip + 0x198db1]
00C727A7  48 8D 05 E2 A3 29 00            lea rax, [rip + 0x29a3e2]
00C727AE  83 CE FF                        or esi, 0xffffffff
00C727B1  48 89 05 E0 A3 29 00            mov qword ptr [rip + 0x29a3e0], rax
00C727B8  48 89 05 D1 A3 29 00            mov qword ptr [rip + 0x29a3d1], rax
00C727BF  4C 89 3D DA A3 29 00            mov qword ptr [rip + 0x29a3da], r15
00C727C6  85 C9                           test ecx, ecx
00C727C8  74 3E                           je 0x140c72808
00C727CA  3B CE                           cmp ecx, esi
00C727CC  75 0C                           jne 0x140c727da
00C727CE  41 8D 4F 1E                     lea ecx, [r15 + 0x1e]
00C727D2  89 0D 80 8D 19 00               mov dword ptr [rip + 0x198d80], ecx
00C727D8  EB 11                           jmp 0x140c727eb
00C727DA  B8 2C 01 00 00                  mov eax, 0x12c
00C727DF  3B C8                           cmp ecx, eax
00C727E1  76 08                           jbe 0x140c727eb
00C727E3  8B C8                           mov ecx, eax
00C727E5  89 05 6D 8D 19 00               mov dword ptr [rip + 0x198d6d], eax
00C727EB  33 D2                           xor edx, edx
00C727ED  8D 41 3B                        lea eax, [rcx + 0x3b]
00C727F0  F7 F1                           div ecx
00C727F2  33 D2                           xor edx, edx
00C727F4  89 05 92 BF 29 00               mov dword ptr [rip + 0x29bf92], eax
00C727FA  8D 81 B3 00 00 00               lea eax, [rcx + 0xb3]
00C72800  F7 F1                           div ecx
00C72802  89 05 80 BF 29 00               mov dword ptr [rip + 0x29bf80], eax
00C72808  48 8D 05 C1 F7 81 FF            lea rax, [rip - 0x7e083f]
00C7280F  4C 89 3D 6A A3 29 00            mov qword ptr [rip + 0x29a36a], r15
00C72816  48 89 05 53 A3 29 00            mov qword ptr [rip + 0x29a353], rax
00C7281D  48 8D 0D BC A2 29 00            lea rcx, [rip + 0x29a2bc]
00C72824  B8 00 00 00 80                  mov eax, 0x80000000
00C72829  4C 89 3D 30 A3 29 00            mov qword ptr [rip + 0x29a330], r15
00C72830  8B D6                           mov edx, esi
00C72832  48 89 05 3F A3 29 00            mov qword ptr [rip + 0x29a33f], rax
00C72839  89 35 09 A3 29 00               mov dword ptr [rip + 0x29a309], esi
00C7283F  E8 CC CE 7A FF                  call 0x14041f710
00C72844  48 8D 05 75 A2 29 00            lea rax, [rip + 0x29a275]
00C7284B  4C 89 3D 86 A2 29 00            mov qword ptr [rip + 0x29a286], r15
00C72852  48 89 05 6F A2 29 00            mov qword ptr [rip + 0x29a26f], rax
00C72859  48 8D 0D 20 A6 29 00            lea rcx, [rip + 0x29a620]
00C72860  48 89 05 59 A2 29 00            mov qword ptr [rip + 0x29a259], rax
00C72867  BA 10 00 00 00                  mov edx, 0x10
00C7286C  48 8D 05 35 B7 29 00            lea rax, [rip + 0x29b735]
00C72873  44 89 25 26 A2 29 00            mov dword ptr [rip + 0x29a226], r12d
00C7287A  48 89 05 2F B7 29 00            mov qword ptr [rip + 0x29b72f], rax
00C72881  48 89 05 20 B7 29 00            mov qword ptr [rip + 0x29b720], rax
00C72888  48 8D 05 21 A6 29 00            lea rax, [rip + 0x29a621]
00C7288F  48 89 05 22 A6 29 00            mov qword ptr [rip + 0x29a622], rax
00C72896  48 89 05 13 A6 29 00            mov qword ptr [rip + 0x29a613], rax
00C7289D  48 8D 05 FC A5 29 00            lea rax, [rip + 0x29a5fc]
00C728A4  48 89 05 FD A5 29 00            mov qword ptr [rip + 0x29a5fd], rax
00C728AB  48 89 05 EE A5 29 00            mov qword ptr [rip + 0x29a5ee], rax
00C728B2  48 8D 05 D7 A5 29 00            lea rax, [rip + 0x29a5d7]
00C728B9  48 89 05 D8 A5 29 00            mov qword ptr [rip + 0x29a5d8], rax
00C728C0  48 89 05 C9 A5 29 00            mov qword ptr [rip + 0x29a5c9], rax
00C728C7  4C 89 3D DA A1 29 00            mov qword ptr [rip + 0x29a1da], r15
00C728CE  44 89 3D DB A1 29 00            mov dword ptr [rip + 0x29a1db], r15d
00C728D5  66 44 89 25 DB A1 29 00         mov word ptr [rip + 0x29a1db], r12w
00C728DD  C6 05 D6 A1 29 00 06            mov byte ptr [rip + 0x29a1d6], 6
00C728E4  44 89 3D D1 A1 29 00            mov dword ptr [rip + 0x29a1d1], r15d
00C728EB  66 44 89 3D AD B6 29 00         mov word ptr [rip + 0x29b6ad], r15w
00C728F3  C6 05 A8 B6 29 00 06            mov byte ptr [rip + 0x29b6a8], 6
00C728FA  44 89 3D A3 B6 29 00            mov dword ptr [rip + 0x29b6a3], r15d
00C72901  48 89 0D 80 A5 29 00            mov qword ptr [rip + 0x29a580], rcx
00C72908  48 89 0D 71 A5 29 00            mov qword ptr [rip + 0x29a571], rcx
00C7290F  44 88 3D 53 68 29 00            mov byte ptr [rip + 0x296853], r15b
00C72916  4C 89 3D 0B 90 29 00            mov qword ptr [rip + 0x29900b], r15
00C7291D  4C 89 3D FC 8F 29 00            mov qword ptr [rip + 0x298ffc], r15
00C72924  E8 4B 5A 7B FF                  call 0x140428374
00C72929  48 8D 05 40 A5 29 00            lea rax, [rip + 0x29a540]
00C72930  48 89 05 41 A5 29 00            mov qword ptr [rip + 0x29a541], rax
00C72937  48 89 05 32 A5 29 00            mov qword ptr [rip + 0x29a532], rax
00C7293E  E8 9D 2F A9 FF                  call 0x1407058e0
00C72943  48 8D 0D DA A3 29 00            lea rcx, [rip + 0x29a3da]
00C7294A  48 89 0D 17 A5 29 00            mov qword ptr [rip + 0x29a517], rcx
00C72951  E8 CE 0F AE FF                  call 0x140753924
00C72956  C7 05 A0 A3 29 00 02 00 00 00   mov dword ptr [rip + 0x29a3a0], 2
00C72960  48 C7 05 99 A3 29 00 05 00 00 00  mov qword ptr [rip + 0x29a399], 5
00C7296B  89 35 9B A3 29 00               mov dword ptr [rip + 0x29a39b], esi
00C72971  44 89 3D 98 A3 29 00            mov dword ptr [rip + 0x29a398], r15d
00C72978  89 35 96 A3 29 00               mov dword ptr [rip + 0x29a396], esi
00C7297E  44 89 25 63 A3 29 00            mov dword ptr [rip + 0x29a363], r12d
00C72985  E8 BE B9 95 FF                  call 0x1405ce348
00C7298A  85 C0                           test eax, eax
00C7298C  74 1C                           je 0x140c729aa
00C7298E  48 8D 05 9B B5 29 00            lea rax, [rip + 0x29b59b]
00C72995  4C 89 3D 84 B5 29 00            mov qword ptr [rip + 0x29b584], r15
00C7299C  48 89 05 95 B5 29 00            mov qword ptr [rip + 0x29b595], rax
00C729A3  48 89 05 86 B5 29 00            mov qword ptr [rip + 0x29b586], rax
00C729AA  44 89 3D 97 4E 1F 00            mov dword ptr [rip + 0x1f4e97], r15d
00C729B1  89 35 09 55 1B 00               mov dword ptr [rip + 0x1b5509], esi
00C729B7  C7 05 03 55 1B 00 02 00 00 00   mov dword ptr [rip + 0x1b5503], 2
00C729C1  E8 42 DD FC FF                  call 0x140c40708
00C729C6  E8 29 AF FC FF                  call 0x140c3d8f4
00C729CB  E8 64 C1 FC FF                  call 0x140c3eb34
00C729D0  E8 77 AE FC FF                  call 0x140c3d84c
00C729D5  E8 F2 F2 FC FF                  call 0x140c41ccc
00C729DA  E8 31 27 AE FF                  call 0x140755110
00C729DF  33 C9                           xor ecx, ecx
00C729E1  E8 EA DF FC FF                  call 0x140c409d0
00C729E6  E8 89 C4 FC FF                  call 0x140c3ee74
00C729EB  E8 E0 FE 80 FF                  call 0x1404828d0
00C729F0  4C 89 3D 11 9F 29 00            mov qword ptr [rip + 0x299f11], r15
00C729F7  4C 89 3D 02 9F 29 00            mov qword ptr [rip + 0x299f02], r15
00C729FE  E8 DD F4 FC FF                  call 0x140c41ee0
00C72A03  E8 20 C7 FC FF                  call 0x140c3f128
00C72A08  48 8D 05 31 91 29 00            lea rax, [rip + 0x299131]
00C72A0F  4C 89 3D AA 65 29 00            mov qword ptr [rip + 0x2965aa], r15
00C72A16  48 89 05 2B 91 29 00            mov qword ptr [rip + 0x29912b], rax
00C72A1D  48 89 05 1C 91 29 00            mov qword ptr [rip + 0x29911c], rax
00C72A24  48 8D 05 35 91 29 00            lea rax, [rip + 0x299135]
00C72A2B  48 89 05 36 91 29 00            mov qword ptr [rip + 0x299136], rax
00C72A32  48 89 05 27 91 29 00            mov qword ptr [rip + 0x299127], rax
00C72A39  48 8D 05 10 ED EF FF            lea rax, [rip - 0x1012f0]
00C72A40  48 89 05 61 A2 29 00            mov qword ptr [rip + 0x29a261], rax
00C72A47  48 8D 05 42 B4 29 00            lea rax, [rip + 0x29b442]
00C72A4E  48 89 05 43 B4 29 00            mov qword ptr [rip + 0x29b443], rax
00C72A55  48 89 05 34 B4 29 00            mov qword ptr [rip + 0x29b434], rax
00C72A5C  48 8D 05 65 B4 29 00            lea rax, [rip + 0x29b465]
00C72A63  48 89 05 66 B4 29 00            mov qword ptr [rip + 0x29b466], rax
00C72A6A  48 89 05 57 B4 29 00            mov qword ptr [rip + 0x29b457], rax
00C72A71  48 8D 05 68 B4 29 00            lea rax, [rip + 0x29b468]
00C72A78  48 89 05 69 B4 29 00            mov qword ptr [rip + 0x29b469], rax
00C72A7F  48 89 05 5A B4 29 00            mov qword ptr [rip + 0x29b45a], rax
00C72A86  48 8D 05 3B 65 29 00            lea rax, [rip + 0x29653b]
00C72A8D  48 89 05 3C 65 29 00            mov qword ptr [rip + 0x29653c], rax
00C72A94  48 89 05 2D 65 29 00            mov qword ptr [rip + 0x29652d], rax
00C72A9B  48 8D 05 0E 6D 96 FF            lea rax, [rip - 0x6992f2]
00C72AA2  48 89 05 EF 64 29 00            mov qword ptr [rip + 0x2964ef], rax
00C72AA9  48 8D 05 40 AA 82 FF            lea rax, [rip - 0x7d55c0]
00C72AB0  48 89 05 59 B4 29 00            mov qword ptr [rip + 0x29b459], rax
00C72AB7  48 8D 05 7A 4C 1F 00            lea rax, [rip + 0x1f4c7a]
00C72ABE  48 89 05 7B 4C 1F 00            mov qword ptr [rip + 0x1f4c7b], rax
00C72AC5  48 89 05 6C 4C 1F 00            mov qword ptr [rip + 0x1f4c6c], rax
00C72ACC  48 8D 05 95 A6 29 00            lea rax, [rip + 0x29a695]
00C72AD3  4C 89 3D 56 4C 1F 00            mov qword ptr [rip + 0x1f4c56], r15
00C72ADA  48 89 05 8F A6 29 00            mov qword ptr [rip + 0x29a68f], rax
00C72AE1  48 89 05 80 A6 29 00            mov qword ptr [rip + 0x29a680], rax
00C72AE8  4C 89 3D 49 90 29 00            mov qword ptr [rip + 0x299049], r15
00C72AEF  4C 89 3D 3A 90 29 00            mov qword ptr [rip + 0x29903a], r15
00C72AF6  4C 89 3D 5B 90 29 00            mov qword ptr [rip + 0x29905b], r15
00C72AFD  4C 89 3D 4C 90 29 00            mov qword ptr [rip + 0x29904c], r15
00C72B04  C7 05 92 A1 29 00 04 00 00 00   mov dword ptr [rip + 0x29a192], 4
00C72B0E  44 88 3D 8F A1 29 00            mov byte ptr [rip + 0x29a18f], r15b
00C72B15  44 89 3D 84 B3 29 00            mov dword ptr [rip + 0x29b384], r15d
00C72B1C  4C 89 3D 8D B3 29 00            mov qword ptr [rip + 0x29b38d], r15
00C72B23  4C 89 3D 7E B3 29 00            mov qword ptr [rip + 0x29b37e], r15
00C72B2A  66 44 89 3D 8E B3 29 00         mov word ptr [rip + 0x29b38e], r15w
00C72B32  C6 05 89 B3 29 00 06            mov byte ptr [rip + 0x29b389], 6
00C72B39  44 89 25 84 B3 29 00            mov dword ptr [rip + 0x29b384], r12d
00C72B40  44 89 3D A9 B3 29 00            mov dword ptr [rip + 0x29b3a9], r15d
00C72B47  C6 05 72 64 29 00 08            mov byte ptr [rip + 0x296472], 8
00C72B4E  4C 89 3D 83 64 29 00            mov qword ptr [rip + 0x296483], r15
00C72B55  44 89 3D A0 64 29 00            mov dword ptr [rip + 0x2964a0], r15d
00C72B5C  66 44 89 3D 94 64 29 00         mov word ptr [rip + 0x296494], r15w
00C72B64  C7 05 12 64 29 00 13 01 00 00   mov dword ptr [rip + 0x296412], 0x113
00C72B6E  4C 89 3D 2B 64 29 00            mov qword ptr [rip + 0x29642b], r15
00C72B75  4C 89 3D 3C 64 29 00            mov qword ptr [rip + 0x29643c], r15
00C72B7C  4C 89 3D 0D 64 29 00            mov qword ptr [rip + 0x29640d], r15
00C72B83  4C 89 3D 6E B3 29 00            mov qword ptr [rip + 0x29b36e], r15
00C72B8A  4C 89 3D 87 B3 29 00            mov qword ptr [rip + 0x29b387], r15
00C72B91  4C 89 3D 68 B3 29 00            mov qword ptr [rip + 0x29b368], r15
00C72B98  C6 05 91 4B 1F 00 08            mov byte ptr [rip + 0x1f4b91], 8
00C72B9F  4C 89 3D A2 4B 1F 00            mov qword ptr [rip + 0x1f4ba2], r15
00C72BA6  44 89 3D BF 4B 1F 00            mov dword ptr [rip + 0x1f4bbf], r15d
00C72BAD  66 44 89 3D B3 4B 1F 00         mov word ptr [rip + 0x1f4bb3], r15w
00C72BB5  66 44 89 25 A3 A5 29 00         mov word ptr [rip + 0x29a5a3], r12w
00C72BBD  C6 05 9E A5 29 00 06            mov byte ptr [rip + 0x29a59e], 6
00C72BC4  44 89 3D 99 A5 29 00            mov dword ptr [rip + 0x29a599], r15d
00C72BCB  E8 88 F7 FC FF                  call 0x140c42358
00C72BD0  48 8D 05 99 BB 29 00            lea rax, [rip + 0x29bb99]
00C72BD7  66 44 89 25 89 BB 29 00         mov word ptr [rip + 0x29bb89], r12w
00C72BDF  48 89 05 92 BB 29 00            mov qword ptr [rip + 0x29bb92], rax
00C72BE6  48 89 05 83 BB 29 00            mov qword ptr [rip + 0x29bb83], rax
00C72BED  C6 05 76 BB 29 00 06            mov byte ptr [rip + 0x29bb76], 6
00C72BF4  44 89 25 71 BB 29 00            mov dword ptr [rip + 0x29bb71], r12d
00C72BFB  E8 3C BC FC FF                  call 0x140c3e83c
00C72C00  B8 64 00 00 00                  mov eax, 0x64
00C72C05  44 89 3D 20 A2 29 00            mov dword ptr [rip + 0x29a220], r15d
00C72C0C  33 C9                           xor ecx, ecx
00C72C0E  48 89 05 1B A2 29 00            mov qword ptr [rip + 0x29a21b], rax
00C72C15  48 89 05 1C A2 29 00            mov qword ptr [rip + 0x29a21c], rax
00C72C1C  89 05 1E A2 29 00               mov dword ptr [rip + 0x29a21e], eax
00C72C22  E8 85 F7 FC FF                  call 0x140c423ac
00C72C27  33 C9                           xor ecx, ecx
00C72C29  E8 7A F9 FC FF                  call 0x140c425a8
00C72C2E  4C 89 3D D3 58 29 00            mov qword ptr [rip + 0x2958d3], r15
00C72C35  4C 89 3D C4 58 29 00            mov qword ptr [rip + 0x2958c4], r15
00C72C3C  E8 DF FB FC FF                  call 0x140c42820
00C72C41  48 8B CF                        mov rcx, rdi
00C72C44  E8 13 B6 FC FF                  call 0x140c3e25c
00C72C49  E8 7A A6 FC FF                  call 0x140c3d2c8
00C72C4E  85 C0                           test eax, eax
00C72C50  0F 88 E3 05 00 00               js 0x140c73239
00C72C56  33 C9                           xor ecx, ecx
00C72C58  E8 57 BA FC FF                  call 0x140c3e6b4
00C72C5D  33 C9                           xor ecx, ecx
00C72C5F  E8 F8 19 FD FF                  call 0x140c4465c
00C72C64  E9 CD 05 00 00                  jmp 0x140c73236
00C72C69  41 3B CC                        cmp ecx, r12d
00C72C6C  0F 85 5C 01 00 00               jne 0x140c72dce
00C72C72  E8 D9 AF 83 FF                  call 0x1404adc50
00C72C77  84 C0                           test al, al
00C72C79  74 0E                           je 0x140c72c89
00C72C7B  44 89 3D DA 26 35 00            mov dword ptr [rip + 0x3526da], r15d
00C72C82  44 89 3D DF 49 1F 00            mov dword ptr [rip + 0x1f49df], r15d
00C72C89  33 C9                           xor ecx, ecx
00C72C8B  4C 89 3D 86 9C 29 00            mov qword ptr [rip + 0x299c86], r15
00C72C92  4C 89 3D 77 9C 29 00            mov qword ptr [rip + 0x299c77], r15
00C72C99  44 89 3D EC 9C 29 00            mov dword ptr [rip + 0x299cec], r15d
00C72CA0  E8 9B 65 AF FF                  call 0x140769240
00C72CA5  8B 05 1D 43 35 00               mov eax, dword ptr [rip + 0x35431d]
00C72CAB  83 F8 10                        cmp eax, 0x10
00C72CAE  73 06                           jae 0x140c72cb6
00C72CB0  89 05 F2 A2 29 00               mov dword ptr [rip + 0x29a2f2], eax
00C72CB6  41 8B CC                        mov ecx, r12d
00C72CB9  4C 89 3D 70 A4 29 00            mov qword ptr [rip + 0x29a470], r15
00C72CC0  4C 89 3D 71 A4 29 00            mov qword ptr [rip + 0x29a471], r15
00C72CC7  4C 89 3D 5A A4 29 00            mov qword ptr [rip + 0x29a45a], r15
00C72CCE  4C 89 3D 4B A4 29 00            mov qword ptr [rip + 0x29a44b], r15
00C72CD5  E8 82 19 FD FF                  call 0x140c4465c
00C72CDA  E8 11 FC FC FF                  call 0x140c428f0
00C72CDF  E8 88 FE FC FF                  call 0x140c42b6c
00C72CE4  48 8D 05 05 6A AF FF            lea rax, [rip - 0x5095fb]
00C72CEB  4C 89 3D 5E 57 29 00            mov qword ptr [rip + 0x29575e], r15
00C72CF2  41 8B CC                        mov ecx, r12d
00C72CF5  48 89 05 74 57 29 00            mov qword ptr [rip + 0x295774], rax
00C72CFC  4C 89 3D 75 57 29 00            mov qword ptr [rip + 0x295775], r15
00C72D03  4C 89 3D 56 57 29 00            mov qword ptr [rip + 0x295756], r15
00C72D0A  E8 15 02 FD FF                  call 0x140c42f24
00C72D0F  E8 D4 B9 FC FF                  call 0x140c3e6e8
00C72D14  E8 FF 02 FD FF                  call 0x140c43018
00C72D19  85 C0                           test eax, eax
00C72D1B  0F 88 18 05 00 00               js 0x140c73239
00C72D21  E8 86 B5 FC FF                  call 0x140c3e2ac
00C72D26  85 C0                           test eax, eax
00C72D28  0F 88 0B 05 00 00               js 0x140c73239
00C72D2E  41 8B CC                        mov ecx, r12d
00C72D31  E8 5E 4E 00 00                  call 0x140c77b94
00C72D36  85 C0                           test eax, eax
00C72D38  0F 88 FB 04 00 00               js 0x140c73239
00C72D3E  E8 D5 A9 FC FF                  call 0x140c3d718
00C72D43  85 C0                           test eax, eax
00C72D45  0F 88 EE 04 00 00               js 0x140c73239
00C72D4B  E8 D4 2C 96 FF                  call 0x1405d5a24
00C72D50  E8 DB 05 FD FF                  call 0x140c43330
00C72D55  41 8B CC                        mov ecx, r12d
00C72D58  E8 4B F8 FC FF                  call 0x140c425a8
00C72D5D  E8 12 A6 FC FF                  call 0x140c3d374
00C72D62  48 8D 45 58                     lea rax, [rbp + 0x58]
00C72D66  45 8B C4                        mov r8d, r12d
00C72D69  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C72D6E  4C 8D 0D 8B 59 39 FF            lea r9, [rip - 0xc6a675]
00C72D75  48 8D 15 54 87 39 FF            lea rdx, [rip - 0xc678ac]
00C72D7C  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
00C72D84  33 C9                           xor ecx, ecx
00C72D86  E8 45 98 E5 FF                  call 0x140acc5d0
00C72D8B  85 C0                           test eax, eax
00C72D8D  0F 88 A6 04 00 00               js 0x140c73239
00C72D93  48 8D 55 40                     lea rdx, [rbp + 0x40]
00C72D97  44 89 65 40                     mov dword ptr [rbp + 0x40], r12d
00C72D9B  48 8D 0D 56 69 3B FF            lea rcx, [rip - 0xc496aa]
00C72DA2  44 88 3D 48 56 29 00            mov byte ptr [rip + 0x295648], r15b
00C72DA9  E8 C2 4F F0 FF                  call 0x140b77d70
00C72DAE  83 7D 40 02                     cmp dword ptr [rbp + 0x40], 2
00C72DB2  75 07                           jne 0x140c72dbb
00C72DB4  44 88 25 36 56 29 00            mov byte ptr [rip + 0x295636], r12b
00C72DBB  E8 18 E0 FC FF                  call 0x140c40dd8
00C72DC0  33 D2                           xor edx, edx
00C72DC2  33 C9                           xor ecx, ecx
00C72DC4  E8 9F 59 96 FF                  call 0x1405d8768
00C72DC9  E9 68 04 00 00                  jmp 0x140c73236
00C72DCE  83 F9 02                        cmp ecx, 2
00C72DD1  0F 85 E1 00 00 00               jne 0x140c72eb8
00C72DD7  E8 04 07 FD FF                  call 0x140c434e0
00C72DDC  41 8B CC                        mov ecx, r12d
00C72DDF  E8 DC AF FA FF                  call 0x140c1ddc0
00C72DE4  E8 5F F3 FC FF                  call 0x140c42148
00C72DE9  E8 B2 09 FD FF                  call 0x140c437a0
00C72DEE  85 C0                           test eax, eax
00C72DF0  0F 88 43 04 00 00               js 0x140c73239
00C72DF6  45 33 C0                        xor r8d, r8d
00C72DF9  48 8D 0D A0 0B AE FF            lea rcx, [rip - 0x51f460]
00C72E00  33 D2                           xor edx, edx
00C72E02  E8 19 37 AD FF                  call 0x140746520
00C72E07  48 8D 0D F2 9D 29 00            lea rcx, [rip + 0x299df2]
00C72E0E  E8 91 6C 66 FF                  call 0x1402d9aa4
00C72E13  41 8A CC                        mov cl, r12b
00C72E16  E8 55 07 DE FF                  call 0x140a53570
00C72E1B  48 8D 0D DE 9D 29 00            lea rcx, [rip + 0x299dde]
00C72E22  E8 01 76 66 FF                  call 0x1402da428
00C72E27  8B 0D 67 23 35 00               mov ecx, dword ptr [rip + 0x352367]
00C72E2D  83 F9 FF                        cmp ecx, -1
00C72E30  74 0E                           je 0x140c72e40
00C72E32  41 8B C7                        mov eax, r15d
00C72E35  85 C9                           test ecx, ecx
00C72E37  0F 95 C0                        setne al
00C72E3A  89 05 94 3E 35 00               mov dword ptr [rip + 0x353e94], eax
00C72E40  E8 CB 22 AE FF                  call 0x140755110
00C72E45  E8 A2 09 FD FF                  call 0x140c437ec
00C72E4A  85 C0                           test eax, eax
00C72E4C  0F 88 E7 03 00 00               js 0x140c73239
00C72E52  41 8B D4                        mov edx, r12d
00C72E55  33 C9                           xor ecx, ecx
00C72E57  E8 8C 1C E1 FF                  call 0x140a84ae8
00C72E5C  48 8D 0D FD B8 29 00            lea rcx, [rip + 0x29b8fd]
00C72E63  E8 3C 6C 66 FF                  call 0x1402d9aa4
00C72E68  E8 9B 71 7F FF                  call 0x14046a008
00C72E6D  48 8D 0D EC B8 29 00            lea rcx, [rip + 0x29b8ec]
00C72E74  E8 AF 75 66 FF                  call 0x1402da428
00C72E79  E8 1E FF FC FF                  call 0x140c42d9c
00C72E7E  33 C9                           xor ecx, ecx
00C72E80  E8 0B 2A E6 FF                  call 0x140ad5890
00C72E85  45 33 C9                        xor r9d, r9d
00C72E88  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
00C72E8D  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00C72E92  48 8D 15 DB B2 29 00            lea rdx, [rip + 0x29b2db]
00C72E99  48 8D 0D 70 DC 3A FF            lea rcx, [rip - 0xc52390]
00C72EA0  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C72EA5  45 8D 41 04                     lea r8d, [r9 + 4]
00C72EA9  E8 62 DE A3 FF                  call 0x1406b0d10
00C72EAE  E8 D1 A7 FC FF                  call 0x140c3d684
00C72EB3  E9 7E 03 00 00                  jmp 0x140c73236
00C72EB8  41 BD 03 00 00 00               mov r13d, 3
00C72EBE  41 3B CD                        cmp ecx, r13d
00C72EC1  0F 85 6F 03 00 00               jne 0x140c73236
00C72EC7  E8 F4 C3 FC FF                  call 0x140c3f2c0
00C72ECC  85 C0                           test eax, eax
00C72ECE  0F 88 65 03 00 00               js 0x140c73239
00C72ED4  41 8B CD                        mov ecx, r13d
00C72ED7  E8 80 17 FD FF                  call 0x140c4465c
00C72EDC  41 8B CD                        mov ecx, r13d
00C72EDF  E8 7C 3D 00 00                  call 0x140c76c60
00C72EE4  8B 05 B6 44 1F 00               mov eax, dword ptr [rip + 0x1f44b6]
00C72EEA  F7 D8                           neg eax
00C72EEC  1A C9                           sbb cl, cl
00C72EEE  22 0D A8 44 1F 00               and cl, byte ptr [rip + 0x1f44a8]
00C72EF4  E8 DB D5 FC FF                  call 0x140c404d4
00C72EF9  E8 9E F9 FC FF                  call 0x140c4289c
00C72EFE  E8 C1 B8 FC FF                  call 0x140c3e7c4
00C72F03  E8 40 0A FD FF                  call 0x140c43948
00C72F08  41 8B CD                        mov ecx, r13d
00C72F0B  E8 84 4C 00 00                  call 0x140c77b94
00C72F10  E8 BB C1 FC FF                  call 0x140c3f0d0
00C72F15  85 C0                           test eax, eax
00C72F17  0F 88 1C 03 00 00               js 0x140c73239
00C72F1D  8B 05 6D 23 35 00               mov eax, dword ptr [rip + 0x35236d]
00C72F23  41 8D 75 FF                     lea esi, [r13 - 1]
00C72F27  45 8A F4                        mov r14b, r12b
00C72F2A  85 C0                           test eax, eax
00C72F2C  74 57                           je 0x140c72f85
00C72F2E  41 3B C4                        cmp eax, r12d
00C72F31  74 08                           je 0x140c72f3b
00C72F33  41 8B F7                        mov esi, r15d
00C72F36  41 8B C7                        mov eax, r15d
00C72F39  EB 4C                           jmp 0x140c72f87
00C72F3B  4C 8D 45 E0                     lea r8, [rbp - 0x20]
00C72F3F  33 D2                           xor edx, edx
00C72F41  8B CE                           mov ecx, esi
00C72F43  45 8A F7                        mov r14b, r15b
00C72F46  E8 A5 F1 84 FF                  call 0x1404c20f0
00C72F4B  85 C0                           test eax, eax
00C72F4D  78 36                           js 0x140c72f85
00C72F4F  8B 45 F4                        mov eax, dword ptr [rbp - 0xc]
00C72F52  89 05 38 22 35 00               mov dword ptr [rip + 0x352238], eax
00C72F58  41 3B C5                        cmp eax, r13d
00C72F5B  75 13                           jne 0x140c72f70
00C72F5D  8B 45 F8                        mov eax, dword ptr [rbp - 8]
00C72F60  89 05 FA 23 35 00               mov dword ptr [rip + 0x3523fa], eax
00C72F66  C7 05 B0 23 35 00 08 00 00 00   mov dword ptr [rip + 0x3523b0], 8
00C72F70  E8 57 09 AE FF                  call 0x1407538cc
00C72F75  41 8B CF                        mov ecx, r15d
00C72F78  84 C0                           test al, al
00C72F7A  0F 94 C1                        sete cl
00C72F7D  89 0D 59 21 35 00               mov dword ptr [rip + 0x352159], ecx
00C72F83  EB 16                           jmp 0x140c72f9b
00C72F85  8B C6                           mov eax, esi
00C72F87  83 FE 02                        cmp esi, 2
00C72F8A  89 05 4C 21 35 00               mov dword ptr [rip + 0x35214c], eax
00C72F90  41 8A D6                        mov dl, r14b
00C72F93  0F 94 C1                        sete cl
00C72F96  E8 0D FF AE FF                  call 0x140762ea8
00C72F9B  E8 FC B3 95 FF                  call 0x1405ce39c
00C72FA0  48 8B CF                        mov rcx, rdi
00C72FA3  E8 2C AB FC FF                  call 0x140c3dad4
00C72FA8  E8 9F AA FC FF                  call 0x140c3da4c
00C72FAD  48 8B 05 7C DB 18 00            mov rax, qword ptr [rip + 0x18db7c]
00C72FB4  E8 17 7B A4 FF                  call 0x1406baad0
00C72FB9  84 C0                           test al, al
00C72FBB  75 16                           jne 0x140c72fd3
00C72FBD  8B 05 3D C2 29 00               mov eax, dword ptr [rip + 0x29c23d]
00C72FC3  FF C8                           dec eax
00C72FC5  83 F8 02                        cmp eax, 2
00C72FC8  77 14                           ja 0x140c72fde
00C72FCA  44 39 3D 33 C2 29 00            cmp dword ptr [rip + 0x29c233], r15d
00C72FD1  74 0B                           je 0x140c72fde
00C72FD3  8B 0D 2B C2 29 00               mov ecx, dword ptr [rip + 0x29c22b]
00C72FD9  E8 A6 2D 96 FF                  call 0x1405d5d84
00C72FDE  E8 55 84 AF FF                  call 0x14076b438
00C72FE3  E8 D8 53 F0 FF                  call 0x140b783c0
00C72FE8  33 C9                           xor ecx, ecx
00C72FEA  E8 91 18 AE FF                  call 0x140754880
00C72FEF  44 38 3D 52 11 35 00            cmp byte ptr [rip + 0x351152], r15b
00C72FF6  74 12                           je 0x140c7300a
00C72FF8  45 33 C9                        xor r9d, r9d
00C72FFB  45 33 C0                        xor r8d, r8d
00C72FFE  41 8D 51 0F                     lea edx, [r9 + 0xf]
00C73002  8D 4A 01                        lea ecx, [rdx + 1]
00C73005  E8 CE D2 C9 FF                  call 0x1409102d8
00C7300A  44 38 3D C3 9E 29 00            cmp byte ptr [rip + 0x299ec3], r15b
00C73011  74 12                           je 0x140c73025
00C73013  45 33 C9                        xor r9d, r9d
00C73016  45 33 C0                        xor r8d, r8d
00C73019  41 8D 51 07                     lea edx, [r9 + 7]
00C7301D  8D 4A 0A                        lea ecx, [rdx + 0xa]
00C73020  E8 B3 D2 C9 FF                  call 0x1409102d8
00C73025  48 8B 87 F0 00 00 00            mov rax, qword ptr [rdi + 0xf0]
00C7302C  41 8B D7                        mov edx, r15d
00C7302F  F6 80 58 0A 00 00 08            test byte ptr [rax + 0xa58], 8
00C73036  74 0C                           je 0x140c73044
00C73038  44 88 25 21 AE 29 00            mov byte ptr [rip + 0x29ae21], r12b
00C7303F  BA 04 00 00 00                  mov edx, 4
00C73044  8B 05 46 3A 35 00               mov eax, dword ptr [rip + 0x353a46]
00C7304A  A8 02                           test al, 2
00C7304C  75 10                           jne 0x140c7305e
00C7304E  44 38 3D 2F 3A 35 00            cmp byte ptr [rip + 0x353a2f], r15b
00C73055  74 07                           je 0x140c7305e
00C73057  BA 17 00 00 00                  mov edx, 0x17
00C7305C  EB 04                           jmp 0x140c73062
00C7305E  85 D2                           test edx, edx
00C73060  74 0F                           je 0x140c73071
00C73062  45 33 C9                        xor r9d, r9d
00C73065  45 33 C0                        xor r8d, r8d
00C73068  41 8D 49 15                     lea ecx, [r9 + 0x15]
00C7306C  E8 67 D2 C9 FF                  call 0x1409102d8
00C73071  41 8B CD                        mov ecx, r13d
00C73074  E8 57 D9 FC FF                  call 0x140c409d0
00C73079  E8 AA A9 E2 FF                  call 0x140a9da28
00C7307E  8B 0D 88 9E 29 00               mov ecx, dword ptr [rip + 0x299e88]
00C73084  41 84 CC                        test r12b, cl
00C73087  74 44                           je 0x140c730cd
00C73089  B8 64 00 00 00                  mov eax, 0x64
00C7308E  44 88 25 49 9E 29 00            mov byte ptr [rip + 0x299e49], r12b
00C73095  89 05 45 9E 29 00               mov dword ptr [rip + 0x299e45], eax
00C7309B  C7 05 3F 9E 29 00 90 01 00 00   mov dword ptr [rip + 0x299e3f], 0x190
00C730A5  C7 05 39 9E 29 00 0A 00 00 00   mov dword ptr [rip + 0x299e39], 0xa
00C730AF  C7 05 33 9E 29 00 FF FF 00 00   mov dword ptr [rip + 0x299e33], 0xffff
00C730B9  C7 05 3D 9E 29 00 04 00 00 00   mov dword ptr [rip + 0x299e3d], 4
00C730C3  C7 05 3B 9E 29 00 02 00 00 00   mov dword ptr [rip + 0x299e3b], 2
00C730CD  F6 C1 02                        test cl, 2
00C730D0  74 23                           je 0x140c730f5
00C730D2  C7 05 E4 9D 29 00 01 01 01 01   mov dword ptr [rip + 0x299de4], 0x1010101
00C730DC  66 C7 05 DF 9D 29 00 01 01      mov word ptr [rip + 0x299ddf], 0x101
00C730E5  44 88 25 DA 9D 29 00            mov byte ptr [rip + 0x299dda], r12b
00C730EC  66 C7 05 DC 9D 29 00 01 01      mov word ptr [rip + 0x299ddc], 0x101
00C730F5  E8 6A CE C9 FF                  call 0x14090ff64
00C730FA  E8 1D 0A FD FF                  call 0x140c43b1c
00C730FF  41 8B CD                        mov ecx, r13d
00C73102  E8 1D FE FC FF                  call 0x140c42f24
00C73107  E8 C4 F7 80 FF                  call 0x1404828d0
00C7310C  41 8B CC                        mov ecx, r12d
00C7310F  44 89 65 50                     mov dword ptr [rbp + 0x50], r12d
00C73113  E8 80 E1 DB FF                  call 0x140a31298
00C73118  45 33 C9                        xor r9d, r9d
00C7311B  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
00C73120  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00C73125  48 8D 55 50                     lea rdx, [rbp + 0x50]
00C73129  48 8D 0D B8 D9 3A FF            lea rcx, [rip - 0xc52648]
00C73130  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C73135  45 8D 41 04                     lea r8d, [r9 + 4]
00C73139  E8 D2 DB A3 FF                  call 0x1406b0d10
00C7313E  41 8B CD                        mov ecx, r13d
00C73141  E8 66 F2 FC FF                  call 0x140c423ac
00C73146  E8 C5 52 F0 FF                  call 0x140b78410
00C7314B  E8 1C 57 AF FF                  call 0x14076886c
00C73150  E8 CB FB FC FF                  call 0x140c42d20
00C73155  E8 92 D7 FC FF                  call 0x140c408ec
00C7315A  48 8B 87 F0 00 00 00            mov rax, qword ptr [rdi + 0xf0]
00C73161  8B 88 84 00 00 00               mov ecx, dword ptr [rax + 0x84]
00C73167  C1 E9 1C                        shr ecx, 0x1c
00C7316A  41 22 CC                        and cl, r12b
00C7316D  88 0D 0E AD 29 00               mov byte ptr [rip + 0x29ad0e], cl
00C73173  E8 68 09 AE FF                  call 0x140753ae0
00C73178  E8 87 54 AF FF                  call 0x140768604
00C7317D  48 8B 97 F0 00 00 00            mov rdx, qword ptr [rdi + 0xf0]
00C73184  8B 82 58 0A 00 00               mov eax, dword ptr [rdx + 0xa58]
00C7318A  48 0F BA E0 0F                  bt rax, 0xf
00C7318F  73 07                           jae 0x140c73198
00C73191  44 88 25 E8 AC 29 00            mov byte ptr [rip + 0x29ace8], r12b
00C73198  0F 10 82 20 11 00 00            movups xmm0, xmmword ptr [rdx + 0x1120]
00C7319F  F3 0F 7F 05 C9 AC 29 00         movdqu xmmword ptr [rip + 0x29acc9], xmm0
00C731A7  E8 14 52 F0 FF                  call 0x140b783c0
00C731AC  E8 03 BC FC FF                  call 0x140c3edb4
00C731B1  E8 5A 52 F0 FF                  call 0x140b78410
00C731B6  41 8B CD                        mov ecx, r13d
00C731B9  E8 F6 B4 FC FF                  call 0x140c3e6b4
00C731BE  E8 09 0A FD FF                  call 0x140c43bcc
00C731C3  E8 64 08 AE FF                  call 0x140753a2c
00C731C8  E8 4F 09 AE FF                  call 0x140753b1c
00C731CD  E8 D2 08 AE FF                  call 0x140753aa4
00C731D2  E8 75 0A AE FF                  call 0x140753c4c
00C731D7  E8 F8 09 AE FF                  call 0x140753bd4
00C731DC  E8 0F 08 AE FF                  call 0x1407539f0
00C731E1  E8 82 08 AE FF                  call 0x140753a68
00C731E6  E8 AD 09 AE FF                  call 0x140753b98
00C731EB  E8 10 C2 AE FF                  call 0x14075f400
00C731F0  8B 87 08 01 00 00               mov eax, dword ptr [rdi + 0x108]
00C731F6  D1 E8                           shr eax, 1
00C731F8  41 22 C4                        and al, r12b
00C731FB  88 05 F7 52 29 00               mov byte ptr [rip + 0x2952f7], al
00C73201  E8 7A 3B B0 FF                  call 0x140776d80
00C73206  E8 1D 02 FD FF                  call 0x140c43428
00C7320B  E8 F8 20 96 FF                  call 0x1405d5308
00C73210  E8 07 D8 FC FF                  call 0x140c40a1c
00C73215  E8 F6 09 AE FF                  call 0x140753c10
00C7321A  E8 E1 D8 FC FF                  call 0x140c40b00
00C7321F  41 8B CC                        mov ecx, r12d
00C73222  E8 B5 B1 83 FF                  call 0x1404ae3dc
00C73227  E8 F0 BF FC FF                  call 0x140c3f21c
00C7322C  E8 FB BC FC FF                  call 0x140c3ef2c
00C73231  E8 3E 02 FD FF                  call 0x140c43474
00C73236  41 8B C7                        mov eax, r15d
00C73239  C1 E8 1F                        shr eax, 0x1f
00C7323C  41 32 C4                        xor al, r12b
00C7323F  48 83 C4 60                     add rsp, 0x60
00C73243  41 5F                           pop r15
00C73245  41 5E                           pop r14
00C73247  41 5D                           pop r13
00C73249  41 5C                           pop r12
00C7324B  5F                              pop rdi
00C7324C  5E                              pop rsi
00C7324D  5D                              pop rbp
00C7324E  C3                              ret
00C7324F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PoInitSystem(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int16 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (96);
    v_r15 = 0;
    *(unsigned int *)(v_rip + 2729708) = a1;
    result = 0;
    v_stack_p20 = 0;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
    v_stack_m58 = v_xmm0;
    if (a1 != 0) goto loc_00C72C69;
    result = KeQueryPerformanceCounter(v_stack_p20, a2, a3, a4);
    *(unsigned __int64 *)(v_rip + 3491879) = v_stack_p20;
    result = PopComputeCounterShifts(v_stack_p20, v_rip + 3492870, v_rip + 3492881, a4);
    result = PopComputeCounterShifts((unsigned int)(0x989680ULL), v_rip + 3492831, v_rip + 3492842, a4);
    a1 = 0;
    *(unsigned __int64 *)(v_rip + 2729593) = 0;
    result = PopSleepstudyInitialize(a1, v_rip + 3492831, v_rip + 3492842, a4);
    a1 = 0;
    result = PopPowerAggregatorInitialize(a1, v_rip + 3492831, v_rip + 3492842, a4);
    if (sign_flag) goto loc_00C73239;
    v_stack_m60 = 0;
    *(unsigned __int64 *)(v_rip + 2722154) = v_rip + 2722158;
    *(unsigned __int64 *)(v_rip + 2722132) = v_rip + 2722158;
    v_stack_m68 = 0;
    *(unsigned __int64 *)(v_rip + 2729498) = v_rip + 2729503;
    a3 = 0;
    *(unsigned __int64 *)(v_rip + 2729480) = v_rip + 2729503;
    a2 = 0;
    v_stack_m70 = 0x72496F50ULL;
    *(unsigned __int64 *)(v_rip + 2729448) = v_rip + 2729455;
    *(unsigned __int64 *)(v_rip + 2729433) = v_rip + 2729455;
    *(unsigned __int64 *)(v_rip + 2716330) = 0;
    *(unsigned __int64 *)(v_rip + 2716315) = 0;
    *(unsigned __int64 *)(v_rip + 2715516) = 0;
    *(unsigned __int64 *)(v_rip + 2715501) = 0;
    *(unsigned __int64 *)(v_rip + 2735102) = 0;
    *(unsigned __int64 *)(v_rip + 2735087) = 0;
    *(unsigned __int16 *)(v_rip + 2722007) = 0;
    *(unsigned __int8 *)(v_rip + 2722002) = 6;
    *(unsigned int *)(v_rip + 2721997) = 0;
    *(unsigned __int64 *)(v_rip + 2715274) = 0;
    *(unsigned __int64 *)(v_rip + 2729387) = 0;
    v_stack_m78 = 312;
    result = ExInitializeNPagedLookasideListInternal(v_rip + 1790515, a2, a3, 512);
    *(unsigned __int64 *)(v_rip + 2715167) = 0;
    a2 = 0;
    *(unsigned __int64 *)(v_rip + 2715150) = v_rip + 2715158;
    *(unsigned __int64 *)(v_rip + 2715129) = v_rip + 2715158;
    result = memset(v_rip + 2731170, a2, (unsigned int)(0xC18ULL), 512);
    *(unsigned __int64 *)(v_rip + 2729240) = v_rip - 8185409;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 2673491)) >> (2));
    result = (unsigned __int8)((result) & ((unsigned __int8)(v_r15 + 1)));
    *(unsigned __int64 *)(v_rip + 2729220) = 0;
    *(unsigned __int8 *)(v_rip + 2701070) = (unsigned __int8)(result);
    a3 = 0;
    *(unsigned __int64 *)(v_rip + 2729189) = 0;
    *(unsigned __int64 *)(v_rip + 2734158) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 2739343) = v_rip + 2739356;
    *(unsigned __int64 *)(v_rip + 2739328) = v_rip + 2739356;
    *(unsigned __int64 *)(v_rip + 2734137) = 0;
    *(unsigned __int64 *)(v_rip + 2729130) = 0;
    *(unsigned __int64 *)(v_rip + 2701003) = 0;
    *(unsigned __int8 *)(v_rip + 2700988) = 0;
    *(unsigned __int8 *)(v_rip + 2701013) = 0;
    *(unsigned __int64 *)(v_rip + 2700998) = 0;
    *(unsigned __int8 *)(v_rip + 2739319) = 0;
    *(unsigned __int64 *)(v_rip + 2739304) = 0;
    *(unsigned __int64 *)(v_rip + 2739289) = 0;
    *(unsigned __int16 *)(v_rip + 2739249) = (unsigned __int16)(v_r15 + 1);
    *(unsigned __int8 *)(v_rip + 2739244) = 6;
    *(unsigned int *)(v_rip + 2739239) = (unsigned int)(v_r15 + 1);
    result = PopInitializeWorkItem(v_rip + 2739316, v_rip - 5365375, a3, 512);
    result = PopInitializeWorkItem(v_rip + 2739088, v_rip - 5367161, a3, 512);
    result = PopInitializeWorkItem(v_rip + 2739005, v_rip - 2031660, a3, 512);
    result = PopInitializeWorkItem(v_rip + 2738922, v_rip - 2031615, a3, 512);
    *(unsigned __int64 *)(v_rip + 2723367) = 0;
    *(unsigned __int64 *)(v_rip + 2723368) = v_rip - 12981010;
    result = PopInitializeWorkItem(v_rip + 2714786, v_rip - 1841879, a3, 512);
    result = PopInitializeWorkItem(v_rip + 2714703, v_rip - 5295994, a3, 512);
    result = PopInitializeWorkItem(v_rip + 2737180, v_rip - 1724749, a3, 512);
    *(unsigned __int64 *)(v_rip + 2714641) = 0;
    *(unsigned __int64 *)(v_rip + 2738778) = v_rip + 2738784;
    *(unsigned __int64 *)(v_rip + 2738763) = v_rip + 2738784;
    *(unsigned __int64 *)(v_rip + 2714612) = 0;
    *(unsigned __int64 *)(v_rip + 2714597) = 0;
    *(unsigned __int64 *)(v_rip + 2714582) = 0;
    *(unsigned __int64 *)(v_rip + 2738775) = 0;
    *(unsigned __int64 *)(v_rip + 2738760) = 0;
    *(unsigned __int8 *)(v_rip + 2737073) = 0;
    result = PpmCheckInit(v_rip + 2737180, v_rip - 1724749, a3, 512);
    result = PopInitializeIrpWorkers(v_rip + 2737180, v_rip - 1724749, a3, 512);
    if (sign_flag) goto loc_00C73239;
    *(unsigned __int64 *)(v_rip + 2728945) = 0;
    *(unsigned __int64 *)(v_rip + 2729346) = v_rip + 2729352;
    *(unsigned __int64 *)(v_rip + 2729331) = v_rip + 2729352;
    *(unsigned __int64 *)(v_rip + 2729277) = v_rip + 2729276;
    *(unsigned __int64 *)(v_rip + 2729262) = v_rip + 2729276;
    *(unsigned __int64 *)(v_rip + 2729240) = v_rip + 2729239;
    *(unsigned __int64 *)(v_rip + 2729225) = v_rip + 2729239;
    *(unsigned __int64 *)(v_rip + 2724411) = v_rip + 2724410;
    *(unsigned __int64 *)(v_rip + 2724396) = v_rip + 2724410;
    *(unsigned __int64 *)(v_rip + 2729166) = v_rip + 2729165;
    *(unsigned __int64 *)(v_rip + 2729151) = v_rip + 2729165;
    *(unsigned __int64 *)(v_rip + 2737065) = v_rip + 2737064;
    *(unsigned __int64 *)(v_rip + 2737050) = v_rip + 2737064;
    *(unsigned __int64 *)(v_rip + 2736996) = v_rip + 2736995;
    *(unsigned __int64 *)(v_rip + 2736981) = v_rip + 2736995;
    *(unsigned __int64 *)(v_rip + 2728790) = 0;
    *(unsigned __int64 *)(v_rip + 2728775) = 0;
    *(unsigned __int64 *)(v_rip + 2728760) = 0;
    *(unsigned __int64 *)(v_rip + 2729193) = 0;
    *(unsigned __int64 *)(v_rip + 1791882) = 0;
    *(unsigned __int16 *)(v_rip + 2729154) = (unsigned __int16)(v_r15 + 1);
    *(unsigned __int8 *)(v_rip + 2729149) = 6;
    *(unsigned int *)(v_rip + 2729144) = (unsigned int)(v_r15 + 1);
    *(unsigned __int64 *)(v_rip + 2729061) = 0;
    *(unsigned __int16 *)(v_rip + 2724253) = (unsigned __int16)(v_r15 + 1);
    *(unsigned __int8 *)(v_rip + 2724248) = 6;
    *(unsigned int *)(v_rip + 2724243) = (unsigned int)(v_r15 + 1);
    *(unsigned int *)(v_rip + 2736904) = (unsigned int)(v_r15 + 1);
    *(unsigned __int64 *)(v_rip + 2736905) = 0;
    *(unsigned int *)(v_rip + 2736906) = 0;
    *(unsigned __int16 *)(v_rip + 2736906) = (unsigned __int16)(v_r15 + 1);
    *(unsigned __int8 *)(v_rip + 2736901) = 6;
    *(unsigned int *)(v_rip + 2736896) = 0;
    result = PopInitShutdownList(v_rip + 2737180, v_rip - 1724749, a3, 512);
    v_rsi = (unsigned int)((v_rsi) | (0xFFFFFFFFULL));
    *(unsigned __int64 *)(v_rip + 2728928) = v_rip + 2728930;
    *(unsigned __int64 *)(v_rip + 2728913) = v_rip + 2728930;
    *(unsigned __int64 *)(v_rip + 2728922) = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1674673))) == 0) goto loc_00C72808;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1674673)))) != ((unsigned int)(v_rsi))) goto loc_00C727DA;
    *(unsigned int *)(v_rip + 1674624) = (unsigned int)(v_r15 + 30);
    goto loc_00C727EB;
loc_00C727DA:
    if (((unsigned int)(v_r15 + 30)) >= = 300) {
        a1 = 300;
        *(unsigned int *)(v_rip + 1674605) = 300;
    }
    a2 = 0;
    a2 = 0;
    *(unsigned int *)(v_rip + 2736018) = (unsigned int)(a1 + 59);
    *(unsigned int *)(v_rip + 2736000) = (unsigned int)(a1 + 179);
loc_00C72808:
    *(unsigned __int64 *)(v_rip + 2728810) = 0;
    *(unsigned __int64 *)(v_rip + 2728787) = v_rip - 8259647;
    *(unsigned __int64 *)(v_rip + 2728752) = 0;
    *(unsigned __int64 *)(v_rip + 2728767) = (unsigned int)(0x80000000ULL);
    *(unsigned int *)(v_rip + 2728713) = (unsigned int)(v_rsi);
    result = ExInitializeResourceLite2(v_rip + 2728636, (unsigned int)((unsigned int)(v_rsi)), a3, 512);
    *(unsigned __int64 *)(v_rip + 2728582) = 0;
    *(unsigned __int64 *)(v_rip + 2728559) = v_rip + 2728565;
    *(unsigned __int64 *)(v_rip + 2728537) = v_rip + 2728565;
    *(unsigned int *)(v_rip + 2728486) = (unsigned int)(v_r15 + 1);
    *(unsigned __int64 *)(v_rip + 2733871) = v_rip + 2733877;
    *(unsigned __int64 *)(v_rip + 2733856) = v_rip + 2733877;
    *(unsigned __int64 *)(v_rip + 2729506) = v_rip + 2729505;
    *(unsigned __int64 *)(v_rip + 2729491) = v_rip + 2729505;
    *(unsigned __int64 *)(v_rip + 2729469) = v_rip + 2729468;
    *(unsigned __int64 *)(v_rip + 2729454) = v_rip + 2729468;
    *(unsigned __int64 *)(v_rip + 2729432) = v_rip + 2729431;
    *(unsigned __int64 *)(v_rip + 2729417) = v_rip + 2729431;
    *(unsigned __int64 *)(v_rip + 2728410) = 0;
    *(unsigned int *)(v_rip + 2728411) = 0;
    *(unsigned __int16 *)(v_rip + 2728411) = (unsigned __int16)(v_r15 + 1);
    *(unsigned __int8 *)(v_rip + 2728406) = 6;
    *(unsigned int *)(v_rip + 2728401) = 0;
    *(unsigned __int16 *)(v_rip + 2733741) = 0;
    *(unsigned __int8 *)(v_rip + 2733736) = 6;
    *(unsigned int *)(v_rip + 2733731) = 0;
    *(unsigned __int64 *)(v_rip + 2729344) = v_rip + 2729504;
    *(unsigned __int64 *)(v_rip + 2729329) = v_rip + 2729504;
    *(unsigned __int8 *)(v_rip + 2713683) = 0;
    *(unsigned __int64 *)(v_rip + 2723851) = 0;
    *(unsigned __int64 *)(v_rip + 2723836) = 0;
    result = IoAddTriageDumpDataBlock(v_rip + 2729504, 16, a3, 512);
    *(unsigned __int64 *)(v_rip + 2729281) = v_rip + 2729280;
    *(unsigned __int64 *)(v_rip + 2729266) = v_rip + 2729280;
    result = PopResetActionDefaults(v_rip + 2729504, 16, a3, 512);
    *(unsigned __int64 *)(v_rip + 2729239) = v_rip + 2728922;
    result = PopDefaultPolicy(v_rip + 2728922, 16, a3, 512);
    *(unsigned int *)(v_rip + 2728864) = 2;
    *(unsigned __int64 *)(v_rip + 2728857) = 5;
    *(unsigned int *)(v_rip + 2728859) = (unsigned int)(v_rsi);
    *(unsigned int *)(v_rip + 2728856) = 0;
    *(unsigned int *)(v_rip + 2728854) = (unsigned int)(v_rsi);
    *(unsigned int *)(v_rip + 2728803) = (unsigned int)(v_r15 + 1);
    result = Feature_VpciVscBootDiskHibernation__private_IsEnabledDeviceUsageNoInline(v_rip + 2728922, 16, a3, 512);
    if ((unsigned int)(result) != 0) {
        result = v_rip + 2733467;
        *(unsigned __int64 *)(v_rip + 2733444) = 0;
        *(unsigned __int64 *)(v_rip + 2733461) = result;
        *(unsigned __int64 *)(v_rip + 2733446) = result;
    }
    *(unsigned int *)(v_rip + 2051735) = 0;
    *(unsigned int *)(v_rip + 1791241) = (unsigned int)(v_rsi);
    *(unsigned int *)(v_rip + 1791235) = 2;
    result = PpmInitPolicyConfiguration(v_rip + 2728922, 16, a3, 512);
    result = PpmInitIdlePolicy(v_rip + 2728922, 16, a3, 512);
    result = PpmPerfInitialize(v_rip + 2728922, 16, a3, 512);
    result = PpmInitCoreParkingPolicy(v_rip + 2728922, 16, a3, 512);
    result = PpmInitHeteroPolicy(v_rip + 2728922, 16, a3, 512);
    result = PpmIdleRegisterDefaultStates(v_rip + 2728922, 16, a3, 512);
    a1 = 0;
    result = PopDeepSleepInitialize(a1, 16, a3, 512);
    result = PopInitializePowerSettings(a1, 16, a3, 512);
    result = PopInitilizeAcDcSettings(a1, 16, a3, 512);
    *(unsigned __int64 *)(v_rip + 2727697) = 0;
    *(unsigned __int64 *)(v_rip + 2727682) = 0;
    result = PopBatteryInit(a1, 16, a3, 512);
    result = PopThermalInit(a1, 16, a3, 512);
    *(unsigned __int64 *)(v_rip + 2713002) = 0;
    *(unsigned __int64 *)(v_rip + 2724139) = v_rip + 2724145;
    *(unsigned __int64 *)(v_rip + 2724124) = v_rip + 2724145;
    *(unsigned __int64 *)(v_rip + 2724150) = v_rip + 2724149;
    *(unsigned __int64 *)(v_rip + 2724135) = v_rip + 2724149;
    *(unsigned __int64 *)(v_rip + 2728545) = v_rip - 1053424;
    *(unsigned __int64 *)(v_rip + 2733123) = v_rip + 2733122;
    *(unsigned __int64 *)(v_rip + 2733108) = v_rip + 2733122;
    *(unsigned __int64 *)(v_rip + 2733158) = v_rip + 2733157;
    *(unsigned __int64 *)(v_rip + 2733143) = v_rip + 2733157;
    *(unsigned __int64 *)(v_rip + 2733161) = v_rip + 2733160;
    *(unsigned __int64 *)(v_rip + 2733146) = v_rip + 2733160;
    *(unsigned __int64 *)(v_rip + 2712892) = v_rip + 2712891;
    *(unsigned __int64 *)(v_rip + 2712877) = v_rip + 2712891;
    *(unsigned __int64 *)(v_rip + 2712815) = v_rip - 6918898;
    *(unsigned __int64 *)(v_rip + 2733145) = v_rip - 8213952;
    *(unsigned __int64 *)(v_rip + 2051195) = v_rip + 2051194;
    *(unsigned __int64 *)(v_rip + 2051180) = v_rip + 2051194;
    *(unsigned __int64 *)(v_rip + 2051158) = 0;
    *(unsigned __int64 *)(v_rip + 2729615) = v_rip + 2729621;
    *(unsigned __int64 *)(v_rip + 2729600) = v_rip + 2729621;
    *(unsigned __int64 *)(v_rip + 2723913) = 0;
    *(unsigned __int64 *)(v_rip + 2723898) = 0;
    *(unsigned __int64 *)(v_rip + 2723931) = 0;
    *(unsigned __int64 *)(v_rip + 2723916) = 0;
    *(unsigned int *)(v_rip + 2728338) = 4;
    *(unsigned __int8 *)(v_rip + 2728335) = 0;
    *(unsigned int *)(v_rip + 2732932) = 0;
    *(unsigned __int64 *)(v_rip + 2732941) = 0;
    *(unsigned __int64 *)(v_rip + 2732926) = 0;
    *(unsigned __int16 *)(v_rip + 2732942) = 0;
    *(unsigned __int8 *)(v_rip + 2732937) = 6;
    *(unsigned int *)(v_rip + 2732932) = (unsigned int)(v_r15 + 1);
    *(unsigned int *)(v_rip + 2732969) = 0;
    *(unsigned __int8 *)(v_rip + 2712690) = 8;
    *(unsigned __int64 *)(v_rip + 2712707) = 0;
    *(unsigned int *)(v_rip + 2712736) = 0;
    *(unsigned __int16 *)(v_rip + 2712724) = 0;
    *(unsigned int *)(v_rip + 2712594) = 275;
    *(unsigned __int64 *)(v_rip + 2712619) = 0;
    *(unsigned __int64 *)(v_rip + 2712636) = 0;
    *(unsigned __int64 *)(v_rip + 2712589) = 0;
    *(unsigned __int64 *)(v_rip + 2732910) = 0;
    *(unsigned __int64 *)(v_rip + 2732935) = 0;
    *(unsigned __int64 *)(v_rip + 2732904) = 0;
    *(unsigned __int8 *)(v_rip + 2050961) = 8;
    *(unsigned __int64 *)(v_rip + 2050978) = 0;
    *(unsigned int *)(v_rip + 2051007) = 0;
    *(unsigned __int16 *)(v_rip + 2050995) = 0;
    *(unsigned __int16 *)(v_rip + 2729379) = (unsigned __int16)(v_r15 + 1);
    *(unsigned __int8 *)(v_rip + 2729374) = 6;
    *(unsigned int *)(v_rip + 2729369) = 0;
    result = PopSmartSuspendInit(a1, 16, a3, 512);
    *(unsigned __int16 *)(v_rip + 2734985) = (unsigned __int16)(v_r15 + 1);
    *(unsigned __int64 *)(v_rip + 2734994) = v_rip + 2735001;
    *(unsigned __int64 *)(v_rip + 2734979) = v_rip + 2735001;
    *(unsigned __int8 *)(v_rip + 2734966) = 6;
    *(unsigned int *)(v_rip + 2734961) = (unsigned int)(v_r15 + 1);
    result = PoFxInitPowerManagement(a1, 16, a3, 512);
    *(unsigned int *)(v_rip + 2728480) = 0;
    a1 = 0;
    *(unsigned __int64 *)(v_rip + 2728475) = 100;
    *(unsigned __int64 *)(v_rip + 2728476) = 100;
    *(unsigned int *)(v_rip + 2728478) = 100;
    result = PopNetInitialize(a1, 16, a3, 512);
    a1 = 0;
    result = PopInitializePowerButtonHold(a1, 16, a3, 512);
    *(unsigned __int64 *)(v_rip + 2709715) = 0;
    *(unsigned __int64 *)(v_rip + 2709700) = 0;
    result = PopRecorderInit(a1, 16, a3, 512);
    result = PopRecordFirmwareResetReason(0, 16, a3, 512);
    result = PopCreateTimebrokerServiceSid(0, 16, a3, 512);
    if (sign_flag) goto loc_00C73239;
    a1 = 0;
    result = PopInitializeDirectedDrips(a1, 16, a3, 512);
    a1 = 0;
    result = SshInitialize(a1, 16, a3, 512);
    goto loc_00C73236;
loc_00C72C69:
    if (0 != ((unsigned int)(v_r15 + 1))) goto loc_00C72DCE;
    result = HviIsAnyHypervisorPresent(a1, 16, a3, 512);
    if ((unsigned __int8)(result) != 0) {
        *(unsigned int *)(v_rip + 3483354) = 0;
        *(unsigned int *)(v_rip + 2050527) = 0;
    }
    a1 = 0;
    *(unsigned __int64 *)(v_rip + 2727046) = 0;
    *(unsigned __int64 *)(v_rip + 2727031) = 0;
    *(unsigned int *)(v_rip + 2727148) = 0;
    result = PopSendFanNoiseChangeWnf(a1, 16, a3, 512);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3490589)))) < 16) {
        *(unsigned int *)(v_rip + 2728690) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3490589)));
    }
    *(unsigned __int64 *)(v_rip + 2729072) = 0;
    *(unsigned __int64 *)(v_rip + 2729073) = 0;
    *(unsigned __int64 *)(v_rip + 2729050) = 0;
    *(unsigned __int64 *)(v_rip + 2729035) = 0;
    result = SshInitialize((unsigned int)((unsigned int)(v_r15 + 1)), 16, a3, 512);
    result = PopUmpoInitializeChannel((unsigned int)((unsigned int)(v_r15 + 1)), 16, a3, 512);
    result = PopUmpoInitializeMonitorChannel((unsigned int)((unsigned int)(v_r15 + 1)), 16, a3, 512);
    *(unsigned __int64 *)(v_rip + 2709342) = 0;
    *(unsigned __int64 *)(v_rip + 2709364) = v_rip - 5281275;
    *(unsigned __int64 *)(v_rip + 2709365) = 0;
    *(unsigned __int64 *)(v_rip + 2709334) = 0;
    result = PopEsInit((unsigned int)((unsigned int)(v_r15 + 1)), 16, a3, 512);
    result = PopInitializePowerSettingCallbacks((unsigned int)((unsigned int)(v_r15 + 1)), 16, a3, 512);
    result = PopEtInit((unsigned int)((unsigned int)(v_r15 + 1)), 16, a3, 512);
    if (sign_flag) goto loc_00C73239;
    result = PopPowerRequestInitialize((unsigned int)((unsigned int)(v_r15 + 1)), 16, a3, 512);
    if (sign_flag) goto loc_00C73239;
    result = PopPowerAggregatorInitialize((unsigned int)((unsigned int)(v_r15 + 1)), 16, a3, 512);
    if (sign_flag) goto loc_00C73239;
    result = PopInitializeHighPerfPowerRequest((unsigned int)((unsigned int)(v_r15 + 1)), 16, a3, 512);
    if (sign_flag) goto loc_00C73239;
    result = PopCheckPowerSourceAfterRtcWakeInitialize((unsigned int)((unsigned int)(v_r15 + 1)), 16, a3, 512);
    result = PopWatchdogInit((unsigned int)((unsigned int)(v_r15 + 1)), 16, a3, 512);
    result = PopInitializePowerButtonHold((unsigned int)((unsigned int)(v_r15 + 1)), 16, a3, 512);
    result = PopInitDripsWakeAccounting((unsigned int)((unsigned int)(v_r15 + 1)), 16, a3, 512);
    v_stack_m70 = v_stack_p20;
    v_stack_m78 = 2;
    a1 = 0;
    result = EmpProviderRegister(a1, v_rip - 13007020, (unsigned int)((unsigned int)(v_r15 + 1)), v_rip - 13018741);
    if (sign_flag) goto loc_00C73239;
    v_stack_p8 = (unsigned int)(v_r15 + 1);
    *(unsigned __int8 *)(v_rip + 2709064) = 0;
    result = EmClientQueryRuleState(v_rip - 12883626, v_stack_p8, (unsigned int)((unsigned int)(v_r15 + 1)), v_rip - 13018741);
    if (v_stack_p8 == 2) {
        *(unsigned __int8 *)(v_rip + 2709046) = (unsigned __int8)(v_r15 + 1);
    }
    result = PopDetectSimulatedHeteroProcessors(v_rip - 12883626, v_stack_p8, (unsigned int)((unsigned int)(v_r15 + 1)), v_rip - 13018741);
    a2 = 0;
    a1 = 0;
    result = PpmHeteroHgsDetectContainmentPresence(a1, a2, (unsigned int)((unsigned int)(v_r15 + 1)), v_rip - 13018741);
    goto loc_00C73236;
loc_00C72DCE:
    if (0 != 2) goto loc_00C72EB8;
    result = PoFxRegisterDebugger(a1, a2, (unsigned int)((unsigned int)(v_r15 + 1)), v_rip - 13018741);
    result = HalReportResourceUsage((unsigned int)((unsigned int)(v_r15 + 1)), a2, (unsigned int)((unsigned int)(v_r15 + 1)), v_rip - 13018741);
    result = PopBatteryInitPhaseTwo((unsigned int)((unsigned int)(v_r15 + 1)), a2, (unsigned int)((unsigned int)(v_r15 + 1)), v_rip - 13018741);
    result = PpmEventInitialize((unsigned int)((unsigned int)(v_r15 + 1)), a2, (unsigned int)((unsigned int)(v_r15 + 1)), v_rip - 13018741);
    if (sign_flag) goto loc_00C73239;
    a3 = 0;
    a2 = 0;
    result = KeRegisterProcessorChangeCallback(v_rip - 5370976, a2, a3, v_rip - 13018741);
    result = PpmAcquireLock(v_rip + 2727410, a2, a3, v_rip - 13018741);
    result = PopInitializeHeteroProcessors((unsigned __int8)(v_r15 + 1), a2, a3, v_rip - 13018741);
    result = PpmReleaseLock(v_rip + 2727390, a2, a3, v_rip - 13018741);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3482471)))) != -1) {
        result = 0;
        result = ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3482471))) != 0) ? 1 : 0;
        *(unsigned int *)(v_rip + 3489428) = (unsigned int)(result);
    }
    result = PpmIdleRegisterDefaultStates((unsigned int)(*(unsigned int *)(v_rip + 3482471)), a2, a3, v_rip - 13018741);
    result = PpmParkInitialize((unsigned int)(*(unsigned int *)(v_rip + 3482471)), a2, a3, v_rip - 13018741);
    if (sign_flag) goto loc_00C73239;
    a1 = 0;
    result = PpmCheckInitProcessors(a1, (unsigned int)((unsigned int)(v_r15 + 1)), a3, v_rip - 13018741);
    result = PpmAcquireLock(v_rip + 2734333, (unsigned int)((unsigned int)(v_r15 + 1)), a3, v_rip - 13018741);
    result = PoFxSendSystemLatencyUpdate(v_rip + 2734333, (unsigned int)((unsigned int)(v_r15 + 1)), a3, v_rip - 13018741);
    result = PpmReleaseLock(v_rip + 2734316, (unsigned int)((unsigned int)(v_r15 + 1)), a3, v_rip - 13018741);
    result = PopPdcCsCheckSystemVolumeDevice(v_rip + 2734316, (unsigned int)((unsigned int)(v_r15 + 1)), a3, v_rip - 13018741);
    a1 = 0;
    result = PopUpdateBackgroundCoolingStatus(a1, (unsigned int)((unsigned int)(v_r15 + 1)), a3, v_rip - 13018741);
    a4 = 0;
    v_stack_m68 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    result = ZwUpdateWnfStateData(v_rip - 12919696, v_rip + 2732763, a4 + 4, a4);
    result = PopInitVideoWnfState(v_rip - 12919696, v_rip + 2732763, a4 + 4, a4);
    goto loc_00C73236;
loc_00C72EB8:
    if (((unsigned int)(v_rip - 12919696)) != 3) goto loc_00C73236;
    result = PopDiagInitialize(v_rip - 12919696, v_rip + 2732763, a4 + 4, a4);
    if (sign_flag) goto loc_00C73239;
    result = SshInitialize(3, v_rip + 2732763, a4 + 4, a4);
    result = PopSleepstudyInitialize(3, v_rip + 2732763, a4 + 4, a4);
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rip + 2049206))));
    a1 = (unsigned __int8)((3) & (*(unsigned __int8 *)(v_rip + 2049192)));
    result = PopTriggerDiagTraceAoAcCapability(a1, v_rip + 2732763, a4 + 4, a4);
    result = PopFanReportBootStartDevices(a1, v_rip + 2732763, a4 + 4, a4);
    result = PopInitializeWin32kActivator(a1, v_rip + 2732763, a4 + 4, a4);
    result = PopModernStandbyNotificationInit(a1, v_rip + 2732763, a4 + 4, a4);
    result = PopPowerAggregatorInitialize(3, v_rip + 2732763, a4 + 4, a4);
    result = PopUserShutdownScenarioInitialize(3, v_rip + 2732763, a4 + 4, a4);
    if (sign_flag) goto loc_00C73239;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3482477))) == 0) goto loc_00C72F85;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3482477)))) == ((unsigned int)(v_r15 + 1))) goto loc_00C72F3B;
    goto loc_00C72F87;
loc_00C72F3B:
    a2 = 0;
    result = HalGetInterruptTargetInformation(0, a2, v_stack_m58, a4);
    if (sign_flag) goto loc_00C72F85;
    *(unsigned int *)(v_rip + 3482168) = (unsigned int)((unsigned int)(v_stack_m44));
    result = (unsigned int)(v_stack_m44);
    if (((unsigned int)((unsigned int)(v_stack_m44))) == 3) {
        result = v_stack_m40;
        *(unsigned int *)(v_rip + 3482618) = (unsigned int)(result);
        *(unsigned int *)(v_rip + 3482544) = 8;
    }
    result = PopCheckSkipTick(0, a2, v_stack_m58, a4);
    a1 = ((unsigned __int8)(result) == 0) ? 1 : 0;
    *(unsigned int *)(v_rip + 3481945) = a1;
    goto loc_00C72F9B;
loc_00C72F85:
loc_00C72F87:
    *(unsigned int *)(v_rip + 3481932) = 0;
    a1 = (0 == 2) ? 1 : 0;
    result = PopDiagTraceSkipTick(a1, 0, v_stack_m58, a4);
loc_00C72F9B:
    result = PpmInitIllegalThrottleLogging(a1, 0, v_stack_m58, a4);
    result = PopCheckShutdownMarker(0, 0, v_stack_m58, a4);
    result = PopCheckAndClearBootError(0, 0, v_stack_m58, a4);
    result = guard_dispatch_icall(0, 0, v_stack_m58, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00C72FD3;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 2736701))) - 1);
    if (((unsigned int)(result)) > 2) goto loc_00C72FDE;
    if ((*(unsigned int *)(v_rip + 2736691)) != 0) {
        a1 = *(unsigned int *)(v_rip + 2736683);
        result = PopDiagTraceAbnormalReset(a1, 0, v_stack_m58, a4);
    }
    result = PopIdleWakeInitialize(a1, 0, v_stack_m58, a4);
    result = PopAcquirePolicyLock(a1, 0, v_stack_m58, a4);
    a1 = 0;
    result = PopUpdateUpgradeInProgress(a1, 0, v_stack_m58, a4);
    if ((*(unsigned __int8 *)(v_rip + 3477842)) != 0) {
        a4 = 0;
        a3 = 0;
        a2 = a4 + 15;
        a1 = a2 + 1;
        result = PopLogSleepDisabled(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(v_rip + 2727619)) != 0) {
        a4 = 0;
        a3 = 0;
        a2 = a4 + 7;
        a1 = a2 + 10;
        result = PopLogSleepDisabled(a1, a2, a3, a4);
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 240) + 2648)) & (8)) != 0) {
        *(unsigned __int8 *)(v_rip + 2731553) = (unsigned __int8)(v_r15 + 1);
        a2 = 4;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3488326)))) & (2)) != 0) goto loc_00C7305E;
    if ((*(unsigned __int8 *)(v_rip + 3488303)) == 0) goto loc_00C7305E;
    goto loc_00C73062;
loc_00C7305E:
    result = (unsigned int)(*(unsigned int *)(v_rip + 3488326));
    if (23 != 0) {
        a4 = 0;
        a3 = 0;
        a1 = a4 + 21;
        result = PopLogSleepDisabled(a1, 23, a3, a4);
    }
    result = PopDeepSleepInitialize(3, 23, a3, a4);
    result = PopInitializePowerPolicySimulate(3, 23, a3, a4);
    if ((((unsigned __int8)(v_r15 + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2727560))))) != 0) {
        result = 100;
        *(unsigned __int8 *)(v_rip + 2727497) = (unsigned __int8)(v_r15 + 1);
        *(unsigned int *)(v_rip + 2727493) = (unsigned int)(result);
        *(unsigned int *)(v_rip + 2727487) = 400;
        *(unsigned int *)(v_rip + 2727481) = 10;
        *(unsigned int *)(v_rip + 2727475) = 0xFFFFULL;
        *(unsigned int *)(v_rip + 2727485) = 4;
        *(unsigned int *)(v_rip + 2727483) = 2;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2727560)))) & (2)) != 0) {
        *(unsigned int *)(v_rip + 2727396) = 0x1010101ULL;
        *(unsigned __int16 *)(v_rip + 2727391) = 257;
        *(unsigned __int8 *)(v_rip + 2727386) = (unsigned __int8)(v_r15 + 1);
        *(unsigned __int16 *)(v_rip + 2727388) = 257;
    }
    result = PopResetCurrentPolicies((unsigned int)(*(unsigned int *)(v_rip + 2727560)), 23, a3, a4);
    result = PopInitializeAdpm((unsigned int)(*(unsigned int *)(v_rip + 2727560)), 23, a3, a4);
    result = PopEsInit(3, 23, a3, a4);
    result = PopInitilizeAcDcSettings(3, 23, a3, a4);
    v_stack_p18 = (unsigned int)(v_r15 + 1);
    result = PopUpdateConsoleDisplayState((unsigned int)((unsigned int)(v_r15 + 1)), 23, a3, a4);
    a4 = 0;
    v_stack_m68 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    result = ZwUpdateWnfStateData(v_rip - 12920392, v_stack_p18, a4 + 4, a4);
    result = PopNetInitialize(3, v_stack_p18, a4 + 4, a4);
    result = PopReleasePolicyLock(3, v_stack_p18, a4 + 4, a4);
    result = PopIdleInitAoAcDozeS4Timer(3, v_stack_p18, a4 + 4, a4);
    result = PopCreateIdlePhaseWatchdog(3, v_stack_p18, a4 + 4, a4);
    result = PopInitializeSystemIdleDetection(3, v_stack_p18, a4 + 4, a4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 240) + 132))) >> (28));
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(v_r15 + 1)));
    *(unsigned __int8 *)(v_rip + 2731278) = (unsigned __int8)(a1);
    result = PopSetupHighPerfPowerRequest(a1, v_stack_p18, a4 + 4, a4);
    result = PpmEnableWmiInterface(a1, v_stack_p18, a4 + 4, a4);
    if (!(condition_is_above_or_equal)) {
        *(unsigned __int8 *)(v_rip + 2731240) = (unsigned __int8)(v_r15 + 1);
    }
    *(unsigned __int64 *)(v_rip + 2731209) = v_xmm0;
    result = PopAcquirePolicyLock(a1, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopCoalescingInitialize(a1, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopReleasePolicyLock(a1, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopInitializeDirectedDrips(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopDripsWatchdogInitialize(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopSetupAudioEventNotification(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopSetupMixedRealitytNotification(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopSetupFullScrenVideoNotification(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopSetupUserPresencePredictionNotification(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopSetupSprActiveSessionChangeNotification(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopSetupAirplaneModeNotification(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopSetupBluetoothChargingNotification(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopSetupMobileHotspotNotification(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopThermalHandlePreviousShutdown(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 264))) >> (1));
    result = (unsigned __int8)((result) & ((unsigned __int8)(v_r15 + 1)));
    *(unsigned __int8 *)(v_rip + 2708215) = (unsigned __int8)(result);
    result = TtmInit(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopReadErrataForIncorrectLidNotification(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopLidReliabilityInit(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopEvaluateInputSuppressionRequired(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopSetupUsb4DisplayPresenceNotification(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopPowerButtonSuppressionInit(3, *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopBatteryQueueWork((unsigned int)((unsigned int)(v_r15 + 1)), *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopSetupKsrCallbacks((unsigned int)((unsigned int)(v_r15 + 1)), *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopHiberEvaluateSkippingMemoryMapValidation((unsigned int)((unsigned int)(v_r15 + 1)), *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
    result = PopReadErrataSkipMemoryOverwriteRequestControlLockAction((unsigned int)((unsigned int)(v_r15 + 1)), *(unsigned __int64 *)(a2 + 240), a4 + 4, a4);
loc_00C73236:
loc_00C73239:
    result = (unsigned int)((0) >> (31));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(v_r15 + 1)));
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PoInitSystem(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m40;
    uint32_t v_stack_m44;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint16_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (96);
    local_r15 = 0;
    *(uint32_t *)(v_rip + 0x29A6EC) = Arg1;
    result = 0;
    v_stack_p20 = 0;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
    v_stack_m58 = v_xmm0;
    if (Arg1 != 0) goto loc_00C72C69;
    result = KeQueryPerformanceCounter(v_stack_p20, Arg2, a3, a4);
    *(uint64_t *)(v_rip + 0x354827) = v_stack_p20;
    result = PopComputeCounterShifts(v_stack_p20, v_rip + 3492870, v_rip + 3492881, a4);
    result = PopComputeCounterShifts((uint32_t)(0x989680ULL), v_rip + 3492831, v_rip + 3492842, a4);
    Arg1 = 0;
    *(uint64_t *)(v_rip + 0x29A679) = 0;
    result = PopSleepstudyInitialize(Arg1, v_rip + 3492831, v_rip + 3492842, a4);
    Arg1 = 0;
    result = PopPowerAggregatorInitialize(Arg1, v_rip + 3492831, v_rip + 3492842, a4);
    if (sign_flag) goto loc_00C73239;
    v_stack_m60 = 0;
    *(uint64_t *)(v_rip + 0x29896A) = v_rip + 2722158;
    *(uint64_t *)(v_rip + 0x298954) = v_rip + 2722158;
    v_stack_m68 = 0;
    *(uint64_t *)(v_rip + 0x29A61A) = v_rip + 2729503;
    a3 = 0;
    *(uint64_t *)(v_rip + 0x29A608) = v_rip + 2729503;
    Arg2 = 0;
    v_stack_m70 = 0x72496F50ULL;
    *(uint64_t *)(v_rip + 0x29A5E8) = v_rip + 2729455;
    *(uint64_t *)(v_rip + 0x29A5D9) = v_rip + 2729455;
    *(uint64_t *)(v_rip + 0x2972AA) = 0;
    *(uint64_t *)(v_rip + 0x29729B) = 0;
    *(uint64_t *)(v_rip + 0x296F7C) = 0;
    *(uint64_t *)(v_rip + 0x296F6D) = 0;
    *(uint64_t *)(v_rip + 0x29BBFE) = 0;
    *(uint64_t *)(v_rip + 0x29BBEF) = 0;
    *(uint16_t *)(v_rip + 0x2988D7) = 0;
    *(uint8_t *)(v_rip + 0x2988D2) = 6;
    *(uint32_t *)(v_rip + 0x2988CD) = 0;
    *(uint64_t *)(v_rip + 0x296E8A) = 0;
    *(uint64_t *)(v_rip + 0x29A5AB) = 0;
    v_stack_m78 = 312;
    result = ExInitializeNPagedLookasideListInternal(v_rip + 1790515, Arg2, a3, 512);
    *(uint64_t *)(v_rip + 0x296E1F) = 0;
    Arg2 = 0;
    *(uint64_t *)(v_rip + 0x296E0E) = v_rip + 2715158;
    *(uint64_t *)(v_rip + 0x296DF9) = v_rip + 2715158;
    result = memset(v_rip + 2731170, Arg2, (uint32_t)(0xC18ULL), 512);
    *(uint64_t *)(v_rip + 0x29A518) = v_rip - 8185409;
    result = (uint8_t)((*(uint8_t *)(v_rip + 0x28CB53)) >> (2));
    result = (uint8_t)((result) & ((uint8_t)(local_r15 + 1)));
    *(uint64_t *)(v_rip + 0x29A504) = 0;
    *(uint8_t *)(v_rip + 0x29370E) = (uint8_t)(result);
    a3 = 0;
    *(uint64_t *)(v_rip + 0x29A4E5) = 0;
    *(uint64_t *)(v_rip + 0x29B84E) = v_xmm0;
    *(uint64_t *)(v_rip + 0x29CC8F) = v_rip + 2739356;
    *(uint64_t *)(v_rip + 0x29CC80) = v_rip + 2739356;
    *(uint64_t *)(v_rip + 0x29B839) = 0;
    *(uint64_t *)(v_rip + 0x29A4AA) = 0;
    *(uint64_t *)(v_rip + 0x2936CB) = 0;
    *(uint8_t *)(v_rip + 0x2936BC) = 0;
    *(uint8_t *)(v_rip + 0x2936D5) = 0;
    *(uint64_t *)(v_rip + 0x2936C6) = 0;
    *(uint8_t *)(v_rip + 0x29CC77) = 0;
    *(uint64_t *)(v_rip + 0x29CC68) = 0;
    *(uint64_t *)(v_rip + 0x29CC59) = 0;
    *(uint16_t *)(v_rip + 0x29CC31) = (uint16_t)(local_r15 + 1);
    *(uint8_t *)(v_rip + 0x29CC2C) = 6;
    *(uint32_t *)(v_rip + 0x29CC27) = (uint32_t)(local_r15 + 1);
    result = PopInitializeWorkItem(v_rip + 2739316, v_rip - 5365375, a3, 512);
    result = PopInitializeWorkItem(v_rip + 2739088, v_rip - 5367161, a3, 512);
    result = PopInitializeWorkItem(v_rip + 2739005, v_rip - 2031660, a3, 512);
    result = PopInitializeWorkItem(v_rip + 2738922, v_rip - 2031615, a3, 512);
    *(uint64_t *)(v_rip + 0x298E27) = 0;
    *(uint64_t *)(v_rip + 0x298E28) = v_rip - 12981010;
    result = PopInitializeWorkItem(v_rip + 2714786, v_rip - 1841879, a3, 512);
    result = PopInitializeWorkItem(v_rip + 2714703, v_rip - 5295994, a3, 512);
    result = PopInitializeWorkItem(v_rip + 2737180, v_rip - 1724749, a3, 512);
    *(uint64_t *)(v_rip + 0x296C11) = 0;
    *(uint64_t *)(v_rip + 0x29CA5A) = v_rip + 2738784;
    *(uint64_t *)(v_rip + 0x29CA4B) = v_rip + 2738784;
    *(uint64_t *)(v_rip + 0x296BF4) = 0;
    *(uint64_t *)(v_rip + 0x296BE5) = 0;
    *(uint64_t *)(v_rip + 0x296BD6) = 0;
    *(uint64_t *)(v_rip + 0x29CA57) = 0;
    *(uint64_t *)(v_rip + 0x29CA48) = 0;
    *(uint8_t *)(v_rip + 0x29C3B1) = 0;
    result = PpmCheckInit(v_rip + 2737180, v_rip - 1724749, a3, 512);
    result = PopInitializeIrpWorkers(v_rip + 2737180, v_rip - 1724749, a3, 512);
    if (sign_flag) goto loc_00C73239;
    *(uint64_t *)(v_rip + 0x29A3F1) = 0;
    *(uint64_t *)(v_rip + 0x29A582) = v_rip + 2729352;
    *(uint64_t *)(v_rip + 0x29A573) = v_rip + 2729352;
    *(uint64_t *)(v_rip + 0x29A53D) = v_rip + 2729276;
    *(uint64_t *)(v_rip + 0x29A52E) = v_rip + 2729276;
    *(uint64_t *)(v_rip + 0x29A518) = v_rip + 2729239;
    *(uint64_t *)(v_rip + 0x29A509) = v_rip + 2729239;
    *(uint64_t *)(v_rip + 0x29923B) = v_rip + 2724410;
    *(uint64_t *)(v_rip + 0x29922C) = v_rip + 2724410;
    *(uint64_t *)(v_rip + 0x29A4CE) = v_rip + 2729165;
    *(uint64_t *)(v_rip + 0x29A4BF) = v_rip + 2729165;
    *(uint64_t *)(v_rip + 0x29C3A9) = v_rip + 2737064;
    *(uint64_t *)(v_rip + 0x29C39A) = v_rip + 2737064;
    *(uint64_t *)(v_rip + 0x29C364) = v_rip + 2736995;
    *(uint64_t *)(v_rip + 0x29C355) = v_rip + 2736995;
    *(uint64_t *)(v_rip + 0x29A356) = 0;
    *(uint64_t *)(v_rip + 0x29A347) = 0;
    *(uint64_t *)(v_rip + 0x29A338) = 0;
    *(uint64_t *)(v_rip + 0x29A4E9) = 0;
    *(uint64_t *)(v_rip + 0x1B578A) = 0;
    *(uint16_t *)(v_rip + 0x29A4C2) = (uint16_t)(local_r15 + 1);
    *(uint8_t *)(v_rip + 0x29A4BD) = 6;
    *(uint32_t *)(v_rip + 0x29A4B8) = (uint32_t)(local_r15 + 1);
    *(uint64_t *)(v_rip + 0x29A465) = 0;
    *(uint16_t *)(v_rip + 0x29919D) = (uint16_t)(local_r15 + 1);
    *(uint8_t *)(v_rip + 0x299198) = 6;
    *(uint32_t *)(v_rip + 0x299193) = (uint32_t)(local_r15 + 1);
    *(uint32_t *)(v_rip + 0x29C308) = (uint32_t)(local_r15 + 1);
    *(uint64_t *)(v_rip + 0x29C309) = 0;
    *(uint32_t *)(v_rip + 0x29C30A) = 0;
    *(uint16_t *)(v_rip + 0x29C30A) = (uint16_t)(local_r15 + 1);
    *(uint8_t *)(v_rip + 0x29C305) = 6;
    *(uint32_t *)(v_rip + 0x29C300) = 0;
    result = PopInitShutdownList(v_rip + 2737180, v_rip - 1724749, a3, 512);
    local_rsi = (uint32_t)((local_rsi) | (0xFFFFFFFFULL));
    *(uint64_t *)(v_rip + 0x29A3E0) = v_rip + 2728930;
    *(uint64_t *)(v_rip + 0x29A3D1) = v_rip + 2728930;
    *(uint64_t *)(v_rip + 0x29A3DA) = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x198DB1))) == 0) goto loc_00C72808;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x198DB1)))) != ((uint32_t)(local_rsi))) goto loc_00C727DA;
    *(uint32_t *)(v_rip + 0x198D80) = (uint32_t)(local_r15 + 30);
    goto loc_00C727EB;
loc_00C727DA:
    if (((uint32_t)(local_r15 + 30)) >= = 300) {
        Arg1 = 300;
        *(uint32_t *)(v_rip + 0x198D6D) = 300;
    }
    Arg2 = 0;
    Arg2 = 0;
    *(uint32_t *)(v_rip + 0x29BF92) = (uint32_t)(Arg1 + 59);
    *(uint32_t *)(v_rip + 0x29BF80) = (uint32_t)(Arg1 + 179);
loc_00C72808:
    *(uint64_t *)(v_rip + 0x29A36A) = 0;
    *(uint64_t *)(v_rip + 0x29A353) = v_rip - 8259647;
    *(uint64_t *)(v_rip + 0x29A330) = 0;
    *(uint64_t *)(v_rip + 0x29A33F) = (uint32_t)(0x80000000ULL);
    *(uint32_t *)(v_rip + 0x29A309) = (uint32_t)(local_rsi);
    result = ExInitializeResourceLite2(v_rip + 2728636, (uint32_t)((uint32_t)(local_rsi)), a3, 512);
    *(uint64_t *)(v_rip + 0x29A286) = 0;
    *(uint64_t *)(v_rip + 0x29A26F) = v_rip + 2728565;
    *(uint64_t *)(v_rip + 0x29A259) = v_rip + 2728565;
    *(uint32_t *)(v_rip + 0x29A226) = (uint32_t)(local_r15 + 1);
    *(uint64_t *)(v_rip + 0x29B72F) = v_rip + 2733877;
    *(uint64_t *)(v_rip + 0x29B720) = v_rip + 2733877;
    *(uint64_t *)(v_rip + 0x29A622) = v_rip + 2729505;
    *(uint64_t *)(v_rip + 0x29A613) = v_rip + 2729505;
    *(uint64_t *)(v_rip + 0x29A5FD) = v_rip + 2729468;
    *(uint64_t *)(v_rip + 0x29A5EE) = v_rip + 2729468;
    *(uint64_t *)(v_rip + 0x29A5D8) = v_rip + 2729431;
    *(uint64_t *)(v_rip + 0x29A5C9) = v_rip + 2729431;
    *(uint64_t *)(v_rip + 0x29A1DA) = 0;
    *(uint32_t *)(v_rip + 0x29A1DB) = 0;
    *(uint16_t *)(v_rip + 0x29A1DB) = (uint16_t)(local_r15 + 1);
    *(uint8_t *)(v_rip + 0x29A1D6) = 6;
    *(uint32_t *)(v_rip + 0x29A1D1) = 0;
    *(uint16_t *)(v_rip + 0x29B6AD) = 0;
    *(uint8_t *)(v_rip + 0x29B6A8) = 6;
    *(uint32_t *)(v_rip + 0x29B6A3) = 0;
    *(uint64_t *)(v_rip + 0x29A580) = v_rip + 2729504;
    *(uint64_t *)(v_rip + 0x29A571) = v_rip + 2729504;
    *(uint8_t *)(v_rip + 0x296853) = 0;
    *(uint64_t *)(v_rip + 0x29900B) = 0;
    *(uint64_t *)(v_rip + 0x298FFC) = 0;
    result = IoAddTriageDumpDataBlock(v_rip + 2729504, 16, a3, 512);
    *(uint64_t *)(v_rip + 0x29A541) = v_rip + 2729280;
    *(uint64_t *)(v_rip + 0x29A532) = v_rip + 2729280;
    result = PopResetActionDefaults(v_rip + 2729504, 16, a3, 512);
    *(uint64_t *)(v_rip + 0x29A517) = v_rip + 2728922;
    result = PopDefaultPolicy(v_rip + 2728922, 16, a3, 512);
    *(uint32_t *)(v_rip + 0x29A3A0) = 2;
    *(uint64_t *)(v_rip + 0x29A399) = 5;
    *(uint32_t *)(v_rip + 0x29A39B) = (uint32_t)(local_rsi);
    *(uint32_t *)(v_rip + 0x29A398) = 0;
    *(uint32_t *)(v_rip + 0x29A396) = (uint32_t)(local_rsi);
    *(uint32_t *)(v_rip + 0x29A363) = (uint32_t)(local_r15 + 1);
    result = Feature_VpciVscBootDiskHibernation__private_IsEnabledDeviceUsageNoInline(v_rip + 2728922, 16, a3, 512);
    if ((uint32_t)(result) != 0) {
        result = v_rip + 2733467;
        *(uint64_t *)(v_rip + 0x29B584) = 0;
        *(uint64_t *)(v_rip + 0x29B595) = result;
        *(uint64_t *)(v_rip + 0x29B586) = result;
    }
    *(uint32_t *)(v_rip + 0x1F4E97) = 0;
    *(uint32_t *)(v_rip + 0x1B5509) = (uint32_t)(local_rsi);
    *(uint32_t *)(v_rip + 0x1B5503) = 2;
    result = PpmInitPolicyConfiguration(v_rip + 2728922, 16, a3, 512);
    result = PpmInitIdlePolicy(v_rip + 2728922, 16, a3, 512);
    result = PpmPerfInitialize(v_rip + 2728922, 16, a3, 512);
    result = PpmInitCoreParkingPolicy(v_rip + 2728922, 16, a3, 512);
    result = PpmInitHeteroPolicy(v_rip + 2728922, 16, a3, 512);
    result = PpmIdleRegisterDefaultStates(v_rip + 2728922, 16, a3, 512);
    Arg1 = 0;
    result = PopDeepSleepInitialize(Arg1, 16, a3, 512);
    result = PopInitializePowerSettings(Arg1, 16, a3, 512);
    result = PopInitilizeAcDcSettings(Arg1, 16, a3, 512);
    *(uint64_t *)(v_rip + 0x299F11) = 0;
    *(uint64_t *)(v_rip + 0x299F02) = 0;
    result = PopBatteryInit(Arg1, 16, a3, 512);
    result = PopThermalInit(Arg1, 16, a3, 512);
    *(uint64_t *)(v_rip + 0x2965AA) = 0;
    *(uint64_t *)(v_rip + 0x29912B) = v_rip + 2724145;
    *(uint64_t *)(v_rip + 0x29911C) = v_rip + 2724145;
    *(uint64_t *)(v_rip + 0x299136) = v_rip + 2724149;
    *(uint64_t *)(v_rip + 0x299127) = v_rip + 2724149;
    *(uint64_t *)(v_rip + 0x29A261) = v_rip - 1053424;
    *(uint64_t *)(v_rip + 0x29B443) = v_rip + 2733122;
    *(uint64_t *)(v_rip + 0x29B434) = v_rip + 2733122;
    *(uint64_t *)(v_rip + 0x29B466) = v_rip + 2733157;
    *(uint64_t *)(v_rip + 0x29B457) = v_rip + 2733157;
    *(uint64_t *)(v_rip + 0x29B469) = v_rip + 2733160;
    *(uint64_t *)(v_rip + 0x29B45A) = v_rip + 2733160;
    *(uint64_t *)(v_rip + 0x29653C) = v_rip + 2712891;
    *(uint64_t *)(v_rip + 0x29652D) = v_rip + 2712891;
    *(uint64_t *)(v_rip + 0x2964EF) = v_rip - 6918898;
    *(uint64_t *)(v_rip + 0x29B459) = v_rip - 8213952;
    *(uint64_t *)(v_rip + 0x1F4C7B) = v_rip + 2051194;
    *(uint64_t *)(v_rip + 0x1F4C6C) = v_rip + 2051194;
    *(uint64_t *)(v_rip + 0x1F4C56) = 0;
    *(uint64_t *)(v_rip + 0x29A68F) = v_rip + 2729621;
    *(uint64_t *)(v_rip + 0x29A680) = v_rip + 2729621;
    *(uint64_t *)(v_rip + 0x299049) = 0;
    *(uint64_t *)(v_rip + 0x29903A) = 0;
    *(uint64_t *)(v_rip + 0x29905B) = 0;
    *(uint64_t *)(v_rip + 0x29904C) = 0;
    *(uint32_t *)(v_rip + 0x29A192) = 4;
    *(uint8_t *)(v_rip + 0x29A18F) = 0;
    *(uint32_t *)(v_rip + 0x29B384) = 0;
    *(uint64_t *)(v_rip + 0x29B38D) = 0;
    *(uint64_t *)(v_rip + 0x29B37E) = 0;
    *(uint16_t *)(v_rip + 0x29B38E) = 0;
    *(uint8_t *)(v_rip + 0x29B389) = 6;
    *(uint32_t *)(v_rip + 0x29B384) = (uint32_t)(local_r15 + 1);
    *(uint32_t *)(v_rip + 0x29B3A9) = 0;
    *(uint8_t *)(v_rip + 0x296472) = 8;
    *(uint64_t *)(v_rip + 0x296483) = 0;
    *(uint32_t *)(v_rip + 0x2964A0) = 0;
    *(uint16_t *)(v_rip + 0x296494) = 0;
    *(uint32_t *)(v_rip + 0x296412) = 275;
    *(uint64_t *)(v_rip + 0x29642B) = 0;
    *(uint64_t *)(v_rip + 0x29643C) = 0;
    *(uint64_t *)(v_rip + 0x29640D) = 0;
    *(uint64_t *)(v_rip + 0x29B36E) = 0;
    *(uint64_t *)(v_rip + 0x29B387) = 0;
    *(uint64_t *)(v_rip + 0x29B368) = 0;
    *(uint8_t *)(v_rip + 0x1F4B91) = 8;
    *(uint64_t *)(v_rip + 0x1F4BA2) = 0;
    *(uint32_t *)(v_rip + 0x1F4BBF) = 0;
    *(uint16_t *)(v_rip + 0x1F4BB3) = 0;
    *(uint16_t *)(v_rip + 0x29A5A3) = (uint16_t)(local_r15 + 1);
    *(uint8_t *)(v_rip + 0x29A59E) = 6;
    *(uint32_t *)(v_rip + 0x29A599) = 0;
    result = PopSmartSuspendInit(Arg1, 16, a3, 512);
    *(uint16_t *)(v_rip + 0x29BB89) = (uint16_t)(local_r15 + 1);
    *(uint64_t *)(v_rip + 0x29BB92) = v_rip + 2735001;
    *(uint64_t *)(v_rip + 0x29BB83) = v_rip + 2735001;
    *(uint8_t *)(v_rip + 0x29BB76) = 6;
    *(uint32_t *)(v_rip + 0x29BB71) = (uint32_t)(local_r15 + 1);
    result = PoFxInitPowerManagement(Arg1, 16, a3, 512);
    *(uint32_t *)(v_rip + 0x29A220) = 0;
    Arg1 = 0;
    *(uint64_t *)(v_rip + 0x29A21B) = 100;
    *(uint64_t *)(v_rip + 0x29A21C) = 100;
    *(uint32_t *)(v_rip + 0x29A21E) = 100;
    result = PopNetInitialize(Arg1, 16, a3, 512);
    Arg1 = 0;
    result = PopInitializePowerButtonHold(Arg1, 16, a3, 512);
    *(uint64_t *)(v_rip + 0x2958D3) = 0;
    *(uint64_t *)(v_rip + 0x2958C4) = 0;
    result = PopRecorderInit(Arg1, 16, a3, 512);
    result = PopRecordFirmwareResetReason(0, 16, a3, 512);
    result = PopCreateTimebrokerServiceSid(0, 16, a3, 512);
    if (sign_flag) goto loc_00C73239;
    Arg1 = 0;
    result = PopInitializeDirectedDrips(Arg1, 16, a3, 512);
    Arg1 = 0;
    result = SshInitialize(Arg1, 16, a3, 512);
    goto loc_00C73236;
loc_00C72C69:
    if (0 != ((uint32_t)(local_r15 + 1))) goto loc_00C72DCE;
    result = HviIsAnyHypervisorPresent(Arg1, 16, a3, 512);
    if ((uint8_t)(result) != 0) {
        *(uint32_t *)(v_rip + 0x3526DA) = 0;
        *(uint32_t *)(v_rip + 0x1F49DF) = 0;
    }
    Arg1 = 0;
    *(uint64_t *)(v_rip + 0x299C86) = 0;
    *(uint64_t *)(v_rip + 0x299C77) = 0;
    *(uint32_t *)(v_rip + 0x299CEC) = 0;
    result = PopSendFanNoiseChangeWnf(Arg1, 16, a3, 512);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x35431D)))) < 16) {
        *(uint32_t *)(v_rip + 0x29A2F2) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x35431D)));
    }
    *(uint64_t *)(v_rip + 0x29A470) = 0;
    *(uint64_t *)(v_rip + 0x29A471) = 0;
    *(uint64_t *)(v_rip + 0x29A45A) = 0;
    *(uint64_t *)(v_rip + 0x29A44B) = 0;
    result = SshInitialize((uint32_t)((uint32_t)(local_r15 + 1)), 16, a3, 512);
    result = PopUmpoInitializeChannel((uint32_t)((uint32_t)(local_r15 + 1)), 16, a3, 512);
    result = PopUmpoInitializeMonitorChannel((uint32_t)((uint32_t)(local_r15 + 1)), 16, a3, 512);
    *(uint64_t *)(v_rip + 0x29575E) = 0;
    *(uint64_t *)(v_rip + 0x295774) = v_rip - 5281275;
    *(uint64_t *)(v_rip + 0x295775) = 0;
    *(uint64_t *)(v_rip + 0x295756) = 0;
    result = PopEsInit((uint32_t)((uint32_t)(local_r15 + 1)), 16, a3, 512);
    result = PopInitializePowerSettingCallbacks((uint32_t)((uint32_t)(local_r15 + 1)), 16, a3, 512);
    result = PopEtInit((uint32_t)((uint32_t)(local_r15 + 1)), 16, a3, 512);
    if (sign_flag) goto loc_00C73239;
    result = PopPowerRequestInitialize((uint32_t)((uint32_t)(local_r15 + 1)), 16, a3, 512);
    if (sign_flag) goto loc_00C73239;
    result = PopPowerAggregatorInitialize((uint32_t)((uint32_t)(local_r15 + 1)), 16, a3, 512);
    if (sign_flag) goto loc_00C73239;
    result = PopInitializeHighPerfPowerRequest((uint32_t)((uint32_t)(local_r15 + 1)), 16, a3, 512);
    if (sign_flag) goto loc_00C73239;
    result = PopCheckPowerSourceAfterRtcWakeInitialize((uint32_t)((uint32_t)(local_r15 + 1)), 16, a3, 512);
    result = PopWatchdogInit((uint32_t)((uint32_t)(local_r15 + 1)), 16, a3, 512);
    result = PopInitializePowerButtonHold((uint32_t)((uint32_t)(local_r15 + 1)), 16, a3, 512);
    result = PopInitDripsWakeAccounting((uint32_t)((uint32_t)(local_r15 + 1)), 16, a3, 512);
    v_stack_m70 = v_stack_p20;
    v_stack_m78 = 2;
    Arg1 = 0;
    result = EmpProviderRegister(Arg1, v_rip - 13007020, (uint32_t)((uint32_t)(local_r15 + 1)), v_rip - 13018741);
    if (sign_flag) goto loc_00C73239;
    v_stack_p8 = (uint32_t)(local_r15 + 1);
    *(uint8_t *)(v_rip + 0x295648) = 0;
    result = EmClientQueryRuleState(v_rip - 12883626, v_stack_p8, (uint32_t)((uint32_t)(local_r15 + 1)), v_rip - 13018741);
    if (v_stack_p8 == 2) {
        *(uint8_t *)(v_rip + 0x295636) = (uint8_t)(local_r15 + 1);
    }
    result = PopDetectSimulatedHeteroProcessors(v_rip - 12883626, v_stack_p8, (uint32_t)((uint32_t)(local_r15 + 1)), v_rip - 13018741);
    Arg2 = 0;
    Arg1 = 0;
    result = PpmHeteroHgsDetectContainmentPresence(Arg1, Arg2, (uint32_t)((uint32_t)(local_r15 + 1)), v_rip - 13018741);
    goto loc_00C73236;
loc_00C72DCE:
    if (0 != 2) goto loc_00C72EB8;
    result = PoFxRegisterDebugger(Arg1, Arg2, (uint32_t)((uint32_t)(local_r15 + 1)), v_rip - 13018741);
    result = HalReportResourceUsage((uint32_t)((uint32_t)(local_r15 + 1)), Arg2, (uint32_t)((uint32_t)(local_r15 + 1)), v_rip - 13018741);
    result = PopBatteryInitPhaseTwo((uint32_t)((uint32_t)(local_r15 + 1)), Arg2, (uint32_t)((uint32_t)(local_r15 + 1)), v_rip - 13018741);
    result = PpmEventInitialize((uint32_t)((uint32_t)(local_r15 + 1)), Arg2, (uint32_t)((uint32_t)(local_r15 + 1)), v_rip - 13018741);
    if (sign_flag) goto loc_00C73239;
    a3 = 0;
    Arg2 = 0;
    result = KeRegisterProcessorChangeCallback(v_rip - 5370976, Arg2, a3, v_rip - 13018741);
    result = PpmAcquireLock(v_rip + 2727410, Arg2, a3, v_rip - 13018741);
    result = PopInitializeHeteroProcessors((uint8_t)(local_r15 + 1), Arg2, a3, v_rip - 13018741);
    result = PpmReleaseLock(v_rip + 2727390, Arg2, a3, v_rip - 13018741);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x352367)))) != -1) {
        result = 0;
        result = ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x352367))) != 0) ? 1 : 0;
        *(uint32_t *)(v_rip + 0x353E94) = (uint32_t)(result);
    }
    result = PpmIdleRegisterDefaultStates((uint32_t)(*(uint32_t *)(v_rip + 0x352367)), Arg2, a3, v_rip - 13018741);
    result = PpmParkInitialize((uint32_t)(*(uint32_t *)(v_rip + 0x352367)), Arg2, a3, v_rip - 13018741);
    if (sign_flag) goto loc_00C73239;
    Arg1 = 0;
    result = PpmCheckInitProcessors(Arg1, (uint32_t)((uint32_t)(local_r15 + 1)), a3, v_rip - 13018741);
    result = PpmAcquireLock(v_rip + 2734333, (uint32_t)((uint32_t)(local_r15 + 1)), a3, v_rip - 13018741);
    result = PoFxSendSystemLatencyUpdate(v_rip + 2734333, (uint32_t)((uint32_t)(local_r15 + 1)), a3, v_rip - 13018741);
    result = PpmReleaseLock(v_rip + 2734316, (uint32_t)((uint32_t)(local_r15 + 1)), a3, v_rip - 13018741);
    result = PopPdcCsCheckSystemVolumeDevice(v_rip + 2734316, (uint32_t)((uint32_t)(local_r15 + 1)), a3, v_rip - 13018741);
    Arg1 = 0;
    result = PopUpdateBackgroundCoolingStatus(Arg1, (uint32_t)((uint32_t)(local_r15 + 1)), a3, v_rip - 13018741);
    a4 = 0;
    v_stack_m68 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    result = ZwUpdateWnfStateData(v_rip - 12919696, v_rip + 2732763, a4 + 4, a4);
    result = PopInitVideoWnfState(v_rip - 12919696, v_rip + 2732763, a4 + 4, a4);
    goto loc_00C73236;
loc_00C72EB8:
    if (((uint32_t)(v_rip - 12919696)) != 3) goto loc_00C73236;
    result = PopDiagInitialize(v_rip - 12919696, v_rip + 2732763, a4 + 4, a4);
    if (sign_flag) goto loc_00C73239;
    result = SshInitialize(3, v_rip + 2732763, a4 + 4, a4);
    result = PopSleepstudyInitialize(3, v_rip + 2732763, a4 + 4, a4);
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_rip + 0x1F44B6))));
    Arg1 = (uint8_t)((3) & (*(uint8_t *)(v_rip + 0x1F44A8)));
    result = PopTriggerDiagTraceAoAcCapability(Arg1, v_rip + 2732763, a4 + 4, a4);
    result = PopFanReportBootStartDevices(Arg1, v_rip + 2732763, a4 + 4, a4);
    result = PopInitializeWin32kActivator(Arg1, v_rip + 2732763, a4 + 4, a4);
    result = PopModernStandbyNotificationInit(Arg1, v_rip + 2732763, a4 + 4, a4);
    result = PopPowerAggregatorInitialize(3, v_rip + 2732763, a4 + 4, a4);
    result = PopUserShutdownScenarioInitialize(3, v_rip + 2732763, a4 + 4, a4);
    if (sign_flag) goto loc_00C73239;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x35236D))) == 0) goto loc_00C72F85;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x35236D)))) == ((uint32_t)(local_r15 + 1))) goto loc_00C72F3B;
    goto loc_00C72F87;
loc_00C72F3B:
    Arg2 = 0;
    result = HalGetInterruptTargetInformation(0, Arg2, v_stack_m58, a4);
    if (sign_flag) goto loc_00C72F85;
    *(uint32_t *)(v_rip + 0x352238) = (uint32_t)((uint32_t)(v_stack_m44));
    result = (uint32_t)(v_stack_m44);
    if (((uint32_t)((uint32_t)(v_stack_m44))) == 3) {
        result = v_stack_m40;
        *(uint32_t *)(v_rip + 0x3523FA) = (uint32_t)(result);
        *(uint32_t *)(v_rip + 0x3523B0) = 8;
    }
    result = PopCheckSkipTick(0, Arg2, v_stack_m58, a4);
    Arg1 = ((uint8_t)(result) == 0) ? 1 : 0;
    *(uint32_t *)(v_rip + 0x352159) = Arg1;
    goto loc_00C72F9B;
loc_00C72F85:
loc_00C72F87:
    *(uint32_t *)(v_rip + 0x35214C) = 0;
    Arg1 = (0 == 2) ? 1 : 0;
    result = PopDiagTraceSkipTick(Arg1, 0, v_stack_m58, a4);
loc_00C72F9B:
    result = PpmInitIllegalThrottleLogging(Arg1, 0, v_stack_m58, a4);
    result = PopCheckShutdownMarker(0, 0, v_stack_m58, a4);
    result = PopCheckAndClearBootError(0, 0, v_stack_m58, a4);
    result = guard_dispatch_icall(0, 0, v_stack_m58, a4);
    if ((uint8_t)(result) != 0) goto loc_00C72FD3;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x29C23D))) - 1);
    if (((uint32_t)(result)) > 2) goto loc_00C72FDE;
    if ((*(uint32_t *)(v_rip + 0x29C233)) != 0) {
        Arg1 = *(uint32_t *)(v_rip + 0x29C22B);
        result = PopDiagTraceAbnormalReset(Arg1, 0, v_stack_m58, a4);
    }
    result = PopIdleWakeInitialize(Arg1, 0, v_stack_m58, a4);
    result = PopAcquirePolicyLock(Arg1, 0, v_stack_m58, a4);
    Arg1 = 0;
    result = PopUpdateUpgradeInProgress(Arg1, 0, v_stack_m58, a4);
    if ((*(uint8_t *)(v_rip + 0x351152)) != 0) {
        a4 = 0;
        a3 = 0;
        Arg2 = a4 + 15;
        Arg1 = Arg2 + 1;
        result = PopLogSleepDisabled(Arg1, Arg2, a3, a4);
    }
    if ((*(uint8_t *)(v_rip + 0x299EC3)) != 0) {
        a4 = 0;
        a3 = 0;
        Arg2 = a4 + 7;
        Arg1 = Arg2 + 10;
        result = PopLogSleepDisabled(Arg1, Arg2, a3, a4);
    }
    if (((*(uint8_t *)(*(uint64_t *)(arg2 + 0xF0) + 0xA58)) & (8)) != 0) {
        *(uint8_t *)(v_rip + 0x29AE21) = (uint8_t)(local_r15 + 1);
        Arg2 = 4;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x353A46)))) & (2)) != 0) goto loc_00C7305E;
    if ((*(uint8_t *)(v_rip + 0x353A2F)) == 0) goto loc_00C7305E;
    goto loc_00C73062;
loc_00C7305E:
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x353A46));
    if (23 != 0) {
        a4 = 0;
        a3 = 0;
        Arg1 = a4 + 21;
        result = PopLogSleepDisabled(Arg1, 23, a3, a4);
    }
    result = PopDeepSleepInitialize(3, 23, a3, a4);
    result = PopInitializePowerPolicySimulate(3, 23, a3, a4);
    if ((((uint8_t)(local_r15 + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x299E88))))) != 0) {
        result = 100;
        *(uint8_t *)(v_rip + 0x299E49) = (uint8_t)(local_r15 + 1);
        *(uint32_t *)(v_rip + 0x299E45) = (uint32_t)(result);
        *(uint32_t *)(v_rip + 0x299E3F) = 400;
        *(uint32_t *)(v_rip + 0x299E39) = 10;
        *(uint32_t *)(v_rip + 0x299E33) = 0xFFFFULL;
        *(uint32_t *)(v_rip + 0x299E3D) = 4;
        *(uint32_t *)(v_rip + 0x299E3B) = 2;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x299E88)))) & (2)) != 0) {
        *(uint32_t *)(v_rip + 0x299DE4) = 0x1010101ULL;
        *(uint16_t *)(v_rip + 0x299DDF) = 257;
        *(uint8_t *)(v_rip + 0x299DDA) = (uint8_t)(local_r15 + 1);
        *(uint16_t *)(v_rip + 0x299DDC) = 257;
    }
    result = PopResetCurrentPolicies((uint32_t)(*(uint32_t *)(v_rip + 0x299E88)), 23, a3, a4);
    result = PopInitializeAdpm((uint32_t)(*(uint32_t *)(v_rip + 0x299E88)), 23, a3, a4);
    result = PopEsInit(3, 23, a3, a4);
    result = PopInitilizeAcDcSettings(3, 23, a3, a4);
    v_stack_p18 = (uint32_t)(local_r15 + 1);
    result = PopUpdateConsoleDisplayState((uint32_t)((uint32_t)(local_r15 + 1)), 23, a3, a4);
    a4 = 0;
    v_stack_m68 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    result = ZwUpdateWnfStateData(v_rip - 12920392, v_stack_p18, a4 + 4, a4);
    result = PopNetInitialize(3, v_stack_p18, a4 + 4, a4);
    result = PopReleasePolicyLock(3, v_stack_p18, a4 + 4, a4);
    result = PopIdleInitAoAcDozeS4Timer(3, v_stack_p18, a4 + 4, a4);
    result = PopCreateIdlePhaseWatchdog(3, v_stack_p18, a4 + 4, a4);
    result = PopInitializeSystemIdleDetection(3, v_stack_p18, a4 + 4, a4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xF0) + 0x84))) >> (28));
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(local_r15 + 1)));
    *(uint8_t *)(v_rip + 0x29AD0E) = (uint8_t)(Arg1);
    result = PopSetupHighPerfPowerRequest(Arg1, v_stack_p18, a4 + 4, a4);
    result = PpmEnableWmiInterface(Arg1, v_stack_p18, a4 + 4, a4);
    if (!(condition_is_above_or_equal)) {
        *(uint8_t *)(v_rip + 0x29ACE8) = (uint8_t)(local_r15 + 1);
    }
    *(uint64_t *)(v_rip + 0x29ACC9) = v_xmm0;
    result = PopAcquirePolicyLock(Arg1, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopCoalescingInitialize(Arg1, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopReleasePolicyLock(Arg1, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopInitializeDirectedDrips(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopDripsWatchdogInitialize(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopSetupAudioEventNotification(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopSetupMixedRealitytNotification(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopSetupFullScrenVideoNotification(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopSetupUserPresencePredictionNotification(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopSetupSprActiveSessionChangeNotification(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopSetupAirplaneModeNotification(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopSetupBluetoothChargingNotification(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopSetupMobileHotspotNotification(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopThermalHandlePreviousShutdown(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x108))) >> (1));
    result = (uint8_t)((result) & ((uint8_t)(local_r15 + 1)));
    *(uint8_t *)(v_rip + 0x2952F7) = (uint8_t)(result);
    result = TtmInit(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopReadErrataForIncorrectLidNotification(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopLidReliabilityInit(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopEvaluateInputSuppressionRequired(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopSetupUsb4DisplayPresenceNotification(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopPowerButtonSuppressionInit(3, *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopBatteryQueueWork((uint32_t)((uint32_t)(local_r15 + 1)), *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopSetupKsrCallbacks((uint32_t)((uint32_t)(local_r15 + 1)), *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopHiberEvaluateSkippingMemoryMapValidation((uint32_t)((uint32_t)(local_r15 + 1)), *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
    result = PopReadErrataSkipMemoryOverwriteRequestControlLockAction((uint32_t)((uint32_t)(local_r15 + 1)), *(uint64_t *)(arg2 + 0xF0), a4 + 4, a4);
loc_00C73236:
loc_00C73239:
    result = (uint32_t)((0) >> (31));
    result = (uint8_t)((result) ^ ((uint8_t)(local_r15 + 1)));
    local_rsp = (local_rsp) + (96);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0xF0` | `64` | `R` |
| `Arg2` | `+ 0x108` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C72358&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
