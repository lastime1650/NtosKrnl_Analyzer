# PopTransitionSystemPowerStateEx

- RVA: `0x00B7E8C0`–`0x00B7FC1E` (길이 `4,958` bytes)
- VA: `0x0000000140B7E8C0`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CCD54`
- 디코드: `1,086`개 명령, `4,958/4,958` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **148**; 고유 호출 대상: **107**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **122**

### Outgoing calls
- `0x00B7E9BA` → [PopTransitionCheckpoint](../../page/A8/PopTransitionCheckpoint_function_00A8F3E8.md) (function, `0x00A8F3E8`)
- `0x00B7E9C6` → [PnpSurpriseFailUnsafeDmaDevices](../../page/A9/PnpSurpriseFailUnsafeDmaDevices_function_00A95B90.md) (function, `0x00A95B90`)
- `0x00B7E9D0` → [PopReadShutdownPolicy](../../text/5C/PopReadShutdownPolicy_function_005CEA64.md) (function, `0x005CEA64`)
- `0x00B7E9D5` → [PopAcquireTransitionLockAfterSleep](PopAcquireTransitionLockAfterSleep_function_00B7C61C.md) (function, `0x00B7C61C`)
- `0x00B7E9E1` → [MmLockPagableSectionByHandle](../../page/A4/MmLockPagableSectionByHandle_function_00A4D1E0.md) (function, `0x00A4D1E0`)
- `0x00B7E9E6` → [PopRunMaximumIrpWorkers](../../text/4A/PopRunMaximumIrpWorkers_function_004A1688.md) (function, `0x004A1688`)
- `0x00B7EA09` → [CmSetLazyFlushState](../../page/AB/CmSetLazyFlushState_function_00AB7824.md) (function, `0x00AB7824`)
- `0x00B7EA0E` → [PopNotifyCallbacksPreSleep](../../page/AD/PopNotifyCallbacksPreSleep_function_00AD3440.md) (function, `0x00AD3440`)
- `0x00B7EA15` → [ExSwapinWorkerThreads](../../page/A6/ExSwapinWorkerThreads_function_00A68C40.md) (function, `0x00A68C40`)
- `0x00B7EA2C` → [PoInitializeBroadcast](../../page/A4/PoInitializeBroadcast_function_00A4DD98.md) (function, `0x00A4DD98`)
- `0x00B7EA42` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00B7EA53` → [PopCheckPowerSourceAfterRtcWakeCancel](../../text/4D/PopCheckPowerSourceAfterRtcWakeCancel_function_004D7150.md) (function, `0x004D7150`)
- `0x00B7EA60` → [PopCurrentPowerStatePrecise](../../page/A3/PopCurrentPowerStatePrecise_function_00A35624.md) (function, `0x00A35624`)
- `0x00B7EA65` → [PopAcquirePolicyLock](PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00B7EA7C` → [PopFilterCapabilities](../../page/91/PopFilterCapabilities_function_0091141C.md) (function, `0x0091141C`)
- `0x00B7EA8F` → [PopReleasePolicyLock](PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00B7EA94` → [PoClearBroadcast](../../page/AA/PoClearBroadcast_function_00AA3CE8.md) (function, `0x00AA3CE8`)
- `0x00B7EAA3` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00B7EABB` → [PopResetActionDefaults](../../page/70/PopResetActionDefaults_function_007058E0.md) (function, `0x007058E0`)
- `0x00B7EAC2` → [PopSetPowerActionState](../../text/4B/PopSetPowerActionState_function_004BC8A8.md) (function, `0x004BC8A8`)
- `0x00B7EAD5` → [PopIgnoreBatteryStatusChange](../../text/4E/PopIgnoreBatteryStatusChange_function_004E347C.md) (function, `0x004E347C`)
- `0x00B7EADA` → [PopCheckResiliencyScenarios](../../page/A3/PopCheckResiliencyScenarios_function_00A31718.md) (function, `0x00A31718`)
- `0x00B7EAE6` → [PopEnforceResiliencyScenarios](../../page/AC/PopEnforceResiliencyScenarios_function_00AC3D90.md) (function, `0x00AC3D90`)
- `0x00B7EAFF` → [PopExecuteOnTargetProcessors](../../text/2D/PopExecuteOnTargetProcessors_function_002DD834.md) (function, `0x002DD834`)
- `0x00B7EB45` → [MmZeroPageFileAtShutdown](../../page/7F/MmZeroPageFileAtShutdown_function_007F9164.md) (function, `0x007F9164`)
- `0x00B7EB5C` → [PopZeroHiberFile](../../page/75/PopZeroHiberFile_function_0075E47C.md) (function, `0x0075E47C`)
- `0x00B7EB9C` → [PopAcquirePolicyLock](PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00B7EBFC` → [PopActionRetrieveInitialState](../../text/4B/PopActionRetrieveInitialState_function_004B8AEC.md) (function, `0x004B8AEC`)
- `0x00B7EC2D` → [PopReleasePolicyLock](PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00B7EC4D` → [PopQueryPowerSettingUlong](../../page/AC/PopQueryPowerSettingUlong_function_00ACCCC8.md) (function, `0x00ACCCC8`)
- `0x00B7EC7F` → [PopInitializePowerPolicySimulate](../../page/A9/PopInitializePowerPolicySimulate_function_00A9DA28.md) (function, `0x00A9DA28`)
- `0x00B7ECB1` → [PopAdvanceSystemPowerState](../../page/AD/PopAdvanceSystemPowerState_function_00AD2A20.md) (function, `0x00AD2A20`)
- `0x00B7ECDF` → [PopFastS4Check](../../page/AA/PopFastS4Check_function_00AAF5A4.md) (function, `0x00AAF5A4`)
- `0x00B7ED6E` → [PopSetSleepMarker](../../page/AA/PopSetSleepMarker_function_00AA86FC.md) (function, `0x00AA86FC`)
- `0x00B7ED75` → [PopSetShutdownMarker](../../page/70/PopSetShutdownMarker_function_00705A40.md) (function, `0x00705A40`)
- `0x00B7ED7A` → [PopSaveLidReliabilityState](../../page/75/PopSaveLidReliabilityState_function_0075F1E8.md) (function, `0x0075F1E8`)
- `0x00B7ED7F` → [PopAcquirePolicyLock](PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00B7EDAC` → [PopReleasePolicyLock](PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00B7EDB6` → [PopCheckpointSystemSleep](PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00B7EDC4` → [PopDiagTraceKernelQueriesAllowed](../../page/AB/PopDiagTraceKernelQueriesAllowed_function_00AB5C04.md) (function, `0x00AB5C04`)
- `0x00B7EDCE` → [PopSetDevicesSystemState](PopSetDevicesSystemState_function_00B76110.md) (function, `0x00B76110`)
- `0x00B7EDEB` → [PopFindNextSystemPowerState](../../page/AB/PopFindNextSystemPowerState_function_00AB5EE8.md) (function, `0x00AB5EE8`)
- `0x00B7EE33` → [PopFindNextSystemPowerState](../../page/AB/PopFindNextSystemPowerState_function_00AB5EE8.md) (function, `0x00AB5EE8`)
- `0x00B7EE54` → [PopGetPolicyWorker](../../text/48/PopGetPolicyWorker_function_00482D24.md) (function, `0x00482D24`)
- `0x00B7EE7A` → [PopReleasePolicyLock](PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00B7EE8A` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00B7EEA4` → [PopQpcTimeInMs](PopQpcTimeInMs_function_00B79780.md) (function, `0x00B79780`)
- `0x00B7EECA` → [ExUpdateSystemTimeFromCmos](ExUpdateSystemTimeFromCmos_function_00B7BD98.md) (function, `0x00B7BD98`)
- `0x00B7EEDA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B7EEEC` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00B7EEFF` → [PfPowerActionNotify](PfPowerActionNotify_function_00B7AC98.md) (function, `0x00B7AC98`)
- `0x00B7EF18` → [PopDiagComputeEarlyHiberStats](PopDiagComputeEarlyHiberStats_function_00B7D920.md) (function, `0x00B7D920`)
- `0x00B7EF23` → [PopDiagTraceFirmwareS3Stats](PopDiagTraceFirmwareS3Stats_function_00B710B8.md) (function, `0x00B710B8`)
- `0x00B7EF4B` → [PfPowerActionNotify](PfPowerActionNotify_function_00B7AC98.md) (function, `0x00B7AC98`)
- `0x00B7EF50` → [PopSetDevicesSystemState](PopSetDevicesSystemState_function_00B76110.md) (function, `0x00B76110`)
- `0x00B7EF5F` → [PfPowerActionNotify](PfPowerActionNotify_function_00B7AC98.md) (function, `0x00B7AC98`)
- `0x00B7EF6A` → [WheaResumedFromHibernate](../../text/65/WheaResumedFromHibernate_function_0065DC30.md) (function, `0x0065DC30`)
- `0x00B7EF6F` → [PpmCheckResumePpmEngineFromSx](../../text/49/PpmCheckResumePpmEngineFromSx_function_00499148.md) (function, `0x00499148`)
- `0x00B7EF7C` → [PopCurrentPowerStatePrecise](../../page/A3/PopCurrentPowerStatePrecise_function_00A35624.md) (function, `0x00A35624`)
- `0x00B7EFA8` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00B7EFAD` → [PopIsDetailedSleepReliabilityDiagEnabled](../../page/AC/PopIsDetailedSleepReliabilityDiagEnabled_function_00ACEEA4.md) (function, `0x00ACEEA4`)
- `0x00B7EFBC` → [RtlBootStatusDisableFlushing](../../text/4F/RtlBootStatusDisableFlushing_function_004FC6C0.md) (function, `0x004FC6C0`)
- `0x00B7EFD6` → [PopCheckpointSystemSleep](PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00B7EFDE` → [PopAllocateHiberContext](../../page/AD/PopAllocateHiberContext_function_00ADC05C.md) (function, `0x00ADC05C`)
- `0x00B7F00A` → [PopNotifyTelemetryOsState](../../page/AC/PopNotifyTelemetryOsState_function_00AC3CB4.md) (function, `0x00AC3CB4`)
- `0x00B7F017` → [PopTransitionCheckpoint](../../page/A8/PopTransitionCheckpoint_function_00A8F3E8.md) (function, `0x00A8F3E8`)
- `0x00B7F030` → [PopCurrentPowerState](../../page/A3/PopCurrentPowerState_function_00A356D8.md) (function, `0x00A356D8`)
- `0x00B7F035` → [Feature_2845206840__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_2845206840__private_IsEnabledDeviceUsageNoInline_function_005D5B64.md) (function, `0x005D5B64`)
- `0x00B7F03E` → [PopAcquirePolicyLock](PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00B7F072` → [PopDiagTracePreSleepNotification](../../page/76/PopDiagTracePreSleepNotification_function_00762BE4.md) (function, `0x00762BE4`)
- `0x00B7F077` → [PopReleasePolicyLock](PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00B7F0AD` → [PopDiagTracePreSleepNotification](../../page/76/PopDiagTracePreSleepNotification_function_00762BE4.md) (function, `0x00762BE4`)
- `0x00B7F0B7` → [PopCheckpointSystemSleep](PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00B7F0BC` → [PopUmpoSendFlushSleepStudyLoggerNotification](../../text/4C/PopUmpoSendFlushSleepStudyLoggerNotification_function_004C4314.md) (function, `0x004C4314`)
- `0x00B7F0C1` → [PopEsEnterSleepShutdown](../../page/AD/PopEsEnterSleepShutdown_function_00AD168C.md) (function, `0x00AD168C`)
- `0x00B7F0C6` → [PopThermalSxEntry](../../text/4E/PopThermalSxEntry_function_004E3D20.md) (function, `0x004E3D20`)
- `0x00B7F0CB` → [PopFanSxEntry](../../text/4B/PopFanSxEntry_function_004BEF04.md) (function, `0x004BEF04`)
- `0x00B7F120` → [RtlSetSystemBootStatusEx](../../page/A8/RtlSetSystemBootStatusEx_function_00A8B360.md) (function, `0x00A8B360`)
- `0x00B7F13A` → [PopFlushVolumes](PopFlushVolumes_function_00B7B938.md) (function, `0x00B7B938`)
- `0x00B7F181` → [PopInitSystemSleeperThread](../../page/9E/PopInitSystemSleeperThread_function_009ECBA8.md) (function, `0x009ECBA8`)
- `0x00B7F1A2` → [ExWakeTimersPause](../../text/4C/ExWakeTimersPause_function_004C6EB4.md) (function, `0x004C6EB4`)
- `0x00B7F278` → [PopIsDozeSupported](../../page/AA/PopIsDozeSupported_function_00AA3DC0.md) (function, `0x00AA3DC0`)
- `0x00B7F352` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B7F3F6` → [PopQueryPowerSettingUlong](../../page/AC/PopQueryPowerSettingUlong_function_00ACCCC8.md) (function, `0x00ACCCC8`)
- `0x00B7F517` → [ExGetNextWakeTime](ExGetNextWakeTime_function_00B7E018.md) (function, `0x00B7E018`)
- `0x00B7F584` → [ExGetNextWakeTime](ExGetNextWakeTime_function_00B7E018.md) (function, `0x00B7E018`)
- `0x00B7F608` → [PopTransitionGetWakeTimerType](../../page/70/PopTransitionGetWakeTimerType_function_00705974.md) (function, `0x00705974`)
- `0x00B7F61A` → [PopTransitionGetWakeTimerType](../../page/70/PopTransitionGetWakeTimerType_function_00705974.md) (function, `0x00705974`)
- `0x00B7F627` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00B7F633` → [ExAcquireTimeRefreshLockExclusive](../../page/9C/ExAcquireTimeRefreshLockExclusive_function_009C5810.md) (function, `0x009C5810`)
- `0x00B7F63F` → [ExUpdateSystemTimeFromCmos](ExUpdateSystemTimeFromCmos_function_00B7BD98.md) (function, `0x00B7BD98`)
- `0x00B7F644` → [ExReleaseTimeRefreshLockExclusive](../../page/9C/ExReleaseTimeRefreshLockExclusive_function_009C5874.md) (function, `0x009C5874`)
- `0x00B7F65E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B7F66A` → [PpmCheckPausePpmEngineForSx](../../text/49/PpmCheckPausePpmEngineForSx_function_00499104.md) (function, `0x00499104`)
- `0x00B7F677` → [PsLookupProcessByProcessId](../../page/8A/PsLookupProcessByProcessId_function_008A2AA0.md) (function, `0x008A2AA0`)
- `0x00B7F684` → [PsLookupThreadByThreadId](../../page/86/PsLookupThreadByThreadId_function_00868300.md) (function, `0x00868300`)
- `0x00B7F689` → [PopSetDevicesSystemState](PopSetDevicesSystemState_function_00B76110.md) (function, `0x00B76110`)
- `0x00B7F692` → [PopNewWakeInfo](PopNewWakeInfo_function_00B7D220.md) (function, `0x00B7D220`)
- `0x00B7F6C4` → [PopPushPowerStateTransitionRecordWithCallback](../../text/43/PopPushPowerStateTransitionRecordWithCallback_function_00430A04.md) (function, `0x00430A04`)
- `0x00B7F6D7` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00B7F6F0` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00B7F6F9` → [PoDelistPowerStateTransitionBlocker](PoDelistPowerStateTransitionBlocker_function_00B795D4.md) (function, `0x00B795D4`)
- `0x00B7F715` → [PopSetPowerActionWatchdogState](../../text/4C/PopSetPowerActionWatchdogState_function_004C86B8.md) (function, `0x004C86B8`)
- `0x00B7F798` → [PopDiagTracePostSleepNotification](PopDiagTracePostSleepNotification_function_00B7DC3C.md) (function, `0x00B7DC3C`)
- `0x00B7F7A6` → [PopDiagTraceMtrrError](PopDiagTraceMtrrError_function_00B71444.md) (function, `0x00B71444`)
- `0x00B7F7DF` → [StringCchPrintfW](../../text/47/StringCchPrintfW_function_0047BAD0.md) (function, `0x0047BAD0`)
- `0x00B7F7EF` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00B7F800` → [IoRaiseInformationalHardError](../../text/4B/IoRaiseInformationalHardError_function_004B82B0.md) (function, `0x004B82B0`)
- `0x00B7F808` → [PopDiagTraceHibernateErrorStatus](PopDiagTraceHibernateErrorStatus_function_00B713B4.md) (function, `0x00B713B4`)
- `0x00B7F82D` → [PopCheckpointSystemSleep](PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00B7F83D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B7F85E` → [PopNotifyTelemetryOsState](../../page/AC/PopNotifyTelemetryOsState_function_00AC3CB4.md) (function, `0x00AC3CB4`)
- `0x00B7F866` → [PopCancelIgnoreBatteryStatusChange](../../page/AD/PopCancelIgnoreBatteryStatusChange_function_00AD4338.md) (function, `0x00AD4338`)
- `0x00B7F87F` → [PopExecuteOnTargetProcessors](../../text/2D/PopExecuteOnTargetProcessors_function_002DD834.md) (function, `0x002DD834`)
- `0x00B7F88A` → [PopReleasePolicyLock](PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00B7F899` → [PopProcessDeviceWakeSource](../B6/PopProcessDeviceWakeSource_function_00B6C534.md) (function, `0x00B6C534`)
- `0x00B7F89E` → [PoClearBroadcast](../../page/AA/PoClearBroadcast_function_00AA3CE8.md) (function, `0x00AA3CE8`)
- `0x00B7F8AA` → [PopFanSxExit](../../text/4D/PopFanSxExit_function_004DAA14.md) (function, `0x004DAA14`)
- `0x00B7F8AF` → [PopEsExitSleep](../../page/AC/PopEsExitSleep_function_00AC5AF0.md) (function, `0x00AC5AF0`)
- `0x00B7F8E5` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00B7F8F4` → [PopCurrentPowerState](../../page/A3/PopCurrentPowerState_function_00A356D8.md) (function, `0x00A356D8`)
- `0x00B7F8FF` → [PopHandleWakeSources](../B6/PopHandleWakeSources_function_00B6C264.md) (function, `0x00B6C264`)
- `0x00B7F91A` → [PopQueryMostRecentWakeSourceAttributes](../../page/AB/PopQueryMostRecentWakeSourceAttributes_function_00AB437C.md) (function, `0x00AB437C`)
- `0x00B7F968` → [SshSessionManagerTracePostSleepNotification](../../page/A8/SshSessionManagerTracePostSleepNotification_function_00A87054.md) (function, `0x00A87054`)
- `0x00B7F973` → [PopAcquirePolicyLock](PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00B7F98B` → [PopUpdateSystemIdleContext](../../page/91/PopUpdateSystemIdleContext_function_00911BB4.md) (function, `0x00911BB4`)
- `0x00B7F993` → [PopPowerAggregatorNotifySystemWake](../../page/76/PopPowerAggregatorNotifySystemWake_function_00764DAC.md) (function, `0x00764DAC`)
- `0x00B7FA03` → [PopDeferDoze](../../page/75/PopDeferDoze_function_0075FF88.md) (function, `0x0075FF88`)
- `0x00B7FABA` → [PopCheckPowerSourceAfterRtcWakeSet](../../text/5D/PopCheckPowerSourceAfterRtcWakeSet_function_005D5A88.md) (function, `0x005D5A88`)
- `0x00B7FAC1` → [PopIsMostRecentWakeAttended](PopIsMostRecentWakeAttended_function_00B7D6C8.md) (function, `0x00B7D6C8`)
- `0x00B7FAF1` → [ExWakeTimersResume](../../text/65/ExWakeTimersResume_function_00659270.md) (function, `0x00659270`)
- `0x00B7FB0D` → [PopBootLoaderTraceProcess](../../page/75/PopBootLoaderTraceProcess_function_0075CC3C.md) (function, `0x0075CC3C`)
- `0x00B7FB19` → [PopResetActionDefaults](../../page/70/PopResetActionDefaults_function_007058E0.md) (function, `0x007058E0`)
- `0x00B7FB21` → [PopSetPowerActionState](../../text/4B/PopSetPowerActionState_function_004BC8A8.md) (function, `0x004BC8A8`)
- `0x00B7FB26` → [PopReleasePolicyLock](PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00B7FB3B` → [PoSetUserPresent](../../text/48/PoSetUserPresent_function_004829A0.md) (function, `0x004829A0`)
- `0x00B7FB4C` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00B7FB51` → [PopCheckForWork](../../text/48/PopCheckForWork_function_00482CAC.md) (function, `0x00482CAC`)
- `0x00B7FB5C` → [PpmPerfReApplyStates](../../page/75/PpmPerfReApplyStates_function_0075ADA4.md) (function, `0x0075ADA4`)
- `0x00B7FB6D` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00B7FB8C` → [ExDeleteWakeTimerInfo](../../text/65/ExDeleteWakeTimerInfo_function_00659254.md) (function, `0x00659254`)
- `0x00B7FBAF` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00B7FBBC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00B7FBCB` → [PopDiagTraceStateTransitionFailurePoint](../../page/76/PopDiagTraceStateTransitionFailurePoint_function_00763468.md) (function, `0x00763468`)
- `0x00B7FBE8` → [PopFxPrepareDevicesForShutdown](../../text/4F/PopFxPrepareDevicesForShutdown_function_004F5DF4.md) (function, `0x004F5DF4`)
- `0x00B7FBF8` → [IoFreePoDeviceNotifyList](IoFreePoDeviceNotifyList_function_00B7CF84.md) (function, `0x00B7CF84`)
- `0x00B7FC13` → [PopTransitionCheckpoint](../../page/A8/PopTransitionCheckpoint_function_00A8F3E8.md) (function, `0x00A8F3E8`)
- `0x00B7FC18` → [PopGracefulShutdown](../B6/PopGracefulShutdown_function_00B6BEC8.md) (function, `0x00B6BEC8`)

### Direct callers
- [PopTransitionSystemPowerState](../B5/PopTransitionSystemPowerState_function_00B5B0A0.md) at `0x00B5B0E7`

### Static image references
- `0x00B7E8E6` → RVA `0x00B7FF40` (` ?? ::OKHAJAOM::`string'`; read)
- `0x00B7E98E` → RVA `0x00F0CF0C` (`.data`; read)
- `0x00B7E9DA` → RVA `0x00FC6C00` (`ALMOSTRO`; read)
- `0x00B7E9EB` → RVA `0x00B782A0` (`PopUnlockAfterSleepWorker`; read)
- `0x00B7E9F2` → RVA `0x00F0B7F8` (`.data`; write)
- `0x00B7E9FB` → RVA `0x00F0B7F0` (`.data`; write)
- `0x00B7EA02` → RVA `0x00F0B7E0` (`.data`; write)
- `0x00B7EA1A` → RVA `0x00F0BEF4` (`.data`; read)
- `0x00B7EA3B` → RVA `0x00F0B7E0` (`.data`; read)
- `0x00B7EA6A` → RVA `0x00F0BE18` (`.data`; read)
- `0x00B7EA75` → RVA `0x00F0CEC0` (`.data`; read)
- `0x00B7EA81` → RVA `0x00F0BD41` (`.data`; read)
- `0x00B7EAC7` → RVA `0x00F0BCD0` (`.data`; read)
- `0x00B7EACE` → RVA `0x00F0BD88` (`.data`; write)
- `0x00B7EAEE` → RVA `0x004D3CE0` (`PpmStopIllegalProcessorThrottleLogging`; read)
- `0x00B7EAF8` → RVA `0x00FC7120` (`ALMOSTRO`; read)
- `0x00B7EB0F` → RVA `0x00F0BD44` (`.data`; write)
- `0x00B7EB20` → RVA `0x00F0BD20` (`.data`; write)
- `0x00B7EB2C` → RVA `0x00F0BD21` (`.data`; write)
- `0x00B7EB33` → RVA `0x00F0BF20` (`.data`; read)
- `0x00B7EB3C` → RVA `0x00F0BF28` (`.data`; read)
- `0x00B7EBAA` → RVA `0x00F0BD44` (`.data`; read)
- `0x00B7EBB7` → RVA `0x00F0BD40` (`.data`; read)
- `0x00B7EBC0` → RVA `0x00F0BD40` (`.data`; write)
- `0x00B7EBD6` → RVA `0x00F0BD4C` (`.data`; read)
- `0x00B7EBEB` → RVA `0x00F0BD6C` (`.data`; read)
- `0x00B7EBF5` → RVA `0x00F0BD48` (`.data`; read)
- `0x00B7EC0F` → RVA `0x00F0BD42` (`.data`; write)
- `0x00B7EC19` → RVA `0x00F0BD4C` (`.data`; write)
- `0x00B7EC35` → RVA `0x00024538` (`.rdata`; read)
- `0x00B7EC65` → RVA `0x00F0BE36` (`.data`; read)
- `0x00B7EC6D` → RVA `0x00F0BE24` (`.data`; read)
- `0x00B7EC75` → RVA `0x00F0BE2B` (`.data`; read)
- `0x00B7EC8A` → RVA `0x00F0BD70` (`.data`; read)
- `0x00B7EC97` → RVA `0x00F0BD70` (`.data`; write)
- `0x00B7ECBD` → RVA `0x00F0BF60` (`.data`; write)
- `0x00B7ECC8` → RVA `0x00F0BD74` (`.data`; write)
- `0x00B7ED1C` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00B7ED5F` → RVA `0x00F0BD42` (`.data`; read)
- `0x00B7ED84` → RVA `0x00F0BD40` (`.data`; reference)
- `0x00B7ED9D` → RVA `0x00F08F68` (`.data`; read)
- `0x00B7EDBB` → RVA `0x00F0BD68` (`.data`; write)
- `0x00B7EE7F` → RVA `0x00F0BF60` (`.data`; read)
- `0x00B7EE8F` → RVA `0x00F0C520` (`.data`; read)
- `0x00B7EE96` → RVA `0x00F0C520` (`.data`; write)
- `0x00B7EE9D` → RVA `0x00F0C518` (`.data`; read)
- `0x00B7EEA9` → RVA `0x00F0BF44` (`.data`; write)
- `0x00B7EEC3` → RVA `0x00F0BDA0` (`.data`; write)
- `0x00B7EECF` → RVA `0x00E00BA8` (`.data`; read)
- `0x00B7EEF4` → RVA `0x00F0C328` (`.data`; write)
- `0x00B7EF11` → RVA `0x00F0BD98` (`.data`; write)
- `0x00B7EF28` → RVA `0x00F0BD69` (`.data`; write)
- `0x00B7EF8F` → RVA `0x000208B8` (`.rdata`; read)
- `0x00B7EFF2` → RVA `0x00F0BD74` (`.data`; read)
- `0x00B7F043` → RVA `0x00F0BD60` (`.data`; read)
- `0x00B7F04A` → RVA `0x00F0BD58` (`.data`; read)
- `0x00B7F051` → RVA `0x00F0BD54` (`.data`; read)
- `0x00B7F17A` → RVA `0x00F10F0C` (`.data`; write)
- `0x00B7F199` → RVA `0x00F0BE00` (`.data`; read)
- `0x00B7F1A7` → RVA `0x00F0BE00` (`.data`; write)
- `0x00B7F1CC` → RVA `0x00F0C8A8` (`.data`; read)
- `0x00B7F1EA` → RVA `0x00F0C8A0` (`.data`; read)
- `0x00B7F1F7` → RVA `0x00F0CED4` (`.data`; read)
- `0x00B7F25B` → RVA `0x00F0CE68` (`.data`; read)
- `0x00B7F2D1` → RVA `0x00F0BC78` (`.data`; read)
- `0x00B7F2F0` → RVA `0x00FC5278` (`ALMOSTRO`; read)
- `0x00B7F32B` → RVA `0x00F0BE10` (`.data`; read)
- `0x00B7F33B` → RVA `0x00F0BE10` (`.data`; write)
- `0x00B7F344` → RVA `0x00F0BDB8` (`.data`; read)
- `0x00B7F357` → RVA `0x00F0BDB0` (`.data`; write)
- `0x00B7F36B` → RVA `0x00F0BDC8` (`.data`; write)
- `0x00B7F376` → RVA `0x00F0BDB8` (`.data`; write)
- `0x00B7F384` → RVA `0x00F0BDE0` (`.data`; write)
- `0x00B7F392` → RVA `0x00F0BDD0` (`.data`; write)
- `0x00B7F3EF` → RVA `0x00024918` (`.rdata`; read)
- `0x00B7F468` → RVA `0x00F0BDE8` (`.data`; read)
- `0x00B7F482` → RVA `0x00F0BDC8` (`.data`; read)
- `0x00B7F489` → RVA `0x00F0BDF8` (`.data`; read)
- `0x00B7F4A3` → RVA `0x00F0BE08` (`.data`; read)
- `0x00B7F5AE` → RVA `0x00F0BDC0` (`.data`; write)
- `0x00B7F5D4` → RVA `0x00F0BDD0` (`.data`; read)
- `0x00B7F5DB` → RVA `0x00F0BDD8` (`.data`; write)
- `0x00B7F613` → RVA `0x00F0BDE0` (`.data`; read)
- `0x00B7F62C` → RVA `0x00F0C310` (`.data`; write)
- `0x00B7F649` → RVA `0x00E00820` (`.data`; read)
- `0x00B7F650` → RVA `0x00F0BDD8` (`.data`; read)
- `0x00B7F657` → RVA `0x00F0BDC0` (`.data`; read)
- `0x00B7F663` → RVA `0x00E0B578` (`.data`; write)
- `0x00B7F6B6` → RVA `0x00F0CE0C` (`.data`; read)
- `0x00B7F6FE` → RVA `0x00F0C000` (`.data`; write)
- `0x00B7F723` → RVA `0x00F0C680` (`.data`; read)
- `0x00B7F739` → RVA `0x00F0BD78` (`.data`; write)
- `0x00B7F73F` → RVA `0x00E67898` (`.data`; write)
- `0x00B7F766` → RVA `0x00F0BD78` (`.data`; read)
- `0x00B7F79D` → RVA `0x00F10F0C` (`.data`; read)
- `0x00B7F7C8` → RVA `0x00B7FF50` (` ?? ::OKHAJAOM::`string'`; read)
- `0x00B7F7D4` → RVA `0x00F0B800` (`.data`; read)
- `0x00B7F86E` → RVA `0x004D04F0` (`PpmStartIllegalProcessorThrottleLogging`; read)
- `0x00B7F8BA` → RVA `0x00F0B700` (`.data`; read)
- `0x00B7F8C9` → RVA `0x007602A0` (`PopSpoilEstimatesOnPowerStateTransitionWorker`; read)
- `0x00B7F8D0` → RVA `0x00F0B718` (`.data`; write)
- `0x00B7F8D7` → RVA `0x00F0B710` (`.data`; write)
- `0x00B7F8DE` → RVA `0x00F0B700` (`.data`; write)
- `0x00B7F998` → RVA `0x00F0BDB0` (`.data`; read)
- `0x00B7F9C9` → RVA `0x00F0BE08` (`.data`; write)
- `0x00B7F9D8` → RVA `0x00F0CCE8` (`.data`; write)
- `0x00B7F9DF` → RVA `0x00F0C684` (`.data`; write)
- `0x00B7F9E6` → RVA `0x00F0C688` (`.data`; write)
- `0x00B7FA17` → RVA `0x00F0BD48` (`.data`; write)
- `0x00B7FA2F` → RVA `0x00F0BD40` (`.data`; read/write)
- `0x00B7FA3E` → RVA `0x00F0BDA8` (`.data`; read)
- `0x00B7FA4B` → RVA `0x00F0BD98` (`.data`; read)
- `0x00B7FA52` → RVA `0x00F0BDA8` (`.data`; write)
- `0x00B7FA64` → RVA `0x00F0C8A8` (`.data`; write)
- `0x00B7FA6B` → RVA `0x00F0C8A0` (`.data`; write)
- `0x00B7FB2B` → RVA `0x00F0C684` (`.data`; read)
- `0x00B7FB35` → RVA `0x00F0C688` (`.data`; read)
- `0x00B7FB63` → RVA `0x00F0BD54` (`.data`; write)
- `0x00B7FB72` → RVA `0x00F07770` (`.data`; read)
- `0x00B7FB79` → RVA `0x00F0C4B0` (`.data`; write)
- `0x00B7FBED` → RVA `0x00F0BD88` (`.data`; read)
- `0x00B7FC05` → RVA `0x00FC6AFE` (`ALMOSTRO`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **107**
  - `0x00B7E9BA` → [PopTransitionCheckpoint](../../page/A8/PopTransitionCheckpoint_function_00A8F3E8.md) (`PAGELK` → `PAGE`)
  - `0x00B7E9C6` → [PnpSurpriseFailUnsafeDmaDevices](../../page/A9/PnpSurpriseFailUnsafeDmaDevices_function_00A95B90.md) (`PAGELK` → `PAGE`)
  - `0x00B7E9D0` → [PopReadShutdownPolicy](../../text/5C/PopReadShutdownPolicy_function_005CEA64.md) (`PAGELK` → `.text`)
  - `0x00B7E9E1` → [MmLockPagableSectionByHandle](../../page/A4/MmLockPagableSectionByHandle_function_00A4D1E0.md) (`PAGELK` → `PAGE`)
  - `0x00B7E9E6` → [PopRunMaximumIrpWorkers](../../text/4A/PopRunMaximumIrpWorkers_function_004A1688.md) (`PAGELK` → `.text`)
  - `0x00B7EA09` → [CmSetLazyFlushState](../../page/AB/CmSetLazyFlushState_function_00AB7824.md) (`PAGELK` → `PAGE`)
  - `0x00B7EA0E` → [PopNotifyCallbacksPreSleep](../../page/AD/PopNotifyCallbacksPreSleep_function_00AD3440.md) (`PAGELK` → `PAGE`)
  - `0x00B7EA15` → [ExSwapinWorkerThreads](../../page/A6/ExSwapinWorkerThreads_function_00A68C40.md) (`PAGELK` → `PAGE`)
  - `0x00B7EA2C` → [PoInitializeBroadcast](../../page/A4/PoInitializeBroadcast_function_00A4DD98.md) (`PAGELK` → `PAGE`)
  - `0x00B7EA42` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`PAGELK` → `.text`)
  - `0x00B7EA53` → [PopCheckPowerSourceAfterRtcWakeCancel](../../text/4D/PopCheckPowerSourceAfterRtcWakeCancel_function_004D7150.md) (`PAGELK` → `.text`)
  - `0x00B7EA60` → [PopCurrentPowerStatePrecise](../../page/A3/PopCurrentPowerStatePrecise_function_00A35624.md) (`PAGELK` → `PAGE`)
  - `0x00B7EA7C` → [PopFilterCapabilities](../../page/91/PopFilterCapabilities_function_0091141C.md) (`PAGELK` → `PAGE`)
  - `0x00B7EA94` → [PoClearBroadcast](../../page/AA/PoClearBroadcast_function_00AA3CE8.md) (`PAGELK` → `PAGE`)
  - `0x00B7EAA3` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`PAGELK` → `.text`)
  - `0x00B7EABB` → [PopResetActionDefaults](../../page/70/PopResetActionDefaults_function_007058E0.md) (`PAGELK` → `PAGE`)
  - `0x00B7EAC2` → [PopSetPowerActionState](../../text/4B/PopSetPowerActionState_function_004BC8A8.md) (`PAGELK` → `.text`)
  - `0x00B7EAD5` → [PopIgnoreBatteryStatusChange](../../text/4E/PopIgnoreBatteryStatusChange_function_004E347C.md) (`PAGELK` → `.text`)
  - `0x00B7EADA` → [PopCheckResiliencyScenarios](../../page/A3/PopCheckResiliencyScenarios_function_00A31718.md) (`PAGELK` → `PAGE`)
  - `0x00B7EAE6` → [PopEnforceResiliencyScenarios](../../page/AC/PopEnforceResiliencyScenarios_function_00AC3D90.md) (`PAGELK` → `PAGE`)
  - `0x00B7EAFF` → [PopExecuteOnTargetProcessors](../../text/2D/PopExecuteOnTargetProcessors_function_002DD834.md) (`PAGELK` → `.text`)
  - `0x00B7EB45` → [MmZeroPageFileAtShutdown](../../page/7F/MmZeroPageFileAtShutdown_function_007F9164.md) (`PAGELK` → `PAGE`)
  - `0x00B7EB5C` → [PopZeroHiberFile](../../page/75/PopZeroHiberFile_function_0075E47C.md) (`PAGELK` → `PAGE`)
  - `0x00B7EBFC` → [PopActionRetrieveInitialState](../../text/4B/PopActionRetrieveInitialState_function_004B8AEC.md) (`PAGELK` → `.text`)
  - `0x00B7EC4D` → [PopQueryPowerSettingUlong](../../page/AC/PopQueryPowerSettingUlong_function_00ACCCC8.md) (`PAGELK` → `PAGE`)
  - `0x00B7EC7F` → [PopInitializePowerPolicySimulate](../../page/A9/PopInitializePowerPolicySimulate_function_00A9DA28.md) (`PAGELK` → `PAGE`)
  - `0x00B7ECB1` → [PopAdvanceSystemPowerState](../../page/AD/PopAdvanceSystemPowerState_function_00AD2A20.md) (`PAGELK` → `PAGE`)
  - `0x00B7ECDF` → [PopFastS4Check](../../page/AA/PopFastS4Check_function_00AAF5A4.md) (`PAGELK` → `PAGE`)
  - `0x00B7ED6E` → [PopSetSleepMarker](../../page/AA/PopSetSleepMarker_function_00AA86FC.md) (`PAGELK` → `PAGE`)
  - `0x00B7ED75` → [PopSetShutdownMarker](../../page/70/PopSetShutdownMarker_function_00705A40.md) (`PAGELK` → `PAGE`)
  - `0x00B7ED7A` → [PopSaveLidReliabilityState](../../page/75/PopSaveLidReliabilityState_function_0075F1E8.md) (`PAGELK` → `PAGE`)
  - `0x00B7EDC4` → [PopDiagTraceKernelQueriesAllowed](../../page/AB/PopDiagTraceKernelQueriesAllowed_function_00AB5C04.md) (`PAGELK` → `PAGE`)
  - `0x00B7EDEB` → [PopFindNextSystemPowerState](../../page/AB/PopFindNextSystemPowerState_function_00AB5EE8.md) (`PAGELK` → `PAGE`)
  - `0x00B7EE33` → [PopFindNextSystemPowerState](../../page/AB/PopFindNextSystemPowerState_function_00AB5EE8.md) (`PAGELK` → `PAGE`)
  - `0x00B7EE54` → [PopGetPolicyWorker](../../text/48/PopGetPolicyWorker_function_00482D24.md) (`PAGELK` → `.text`)
  - `0x00B7EE8A` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGELK` → `.text`)
  - `0x00B7EEDA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B7EEEC` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGELK` → `.text`)
  - `0x00B7EF6A` → [WheaResumedFromHibernate](../../text/65/WheaResumedFromHibernate_function_0065DC30.md) (`PAGELK` → `.text`)
  - `0x00B7EF6F` → [PpmCheckResumePpmEngineFromSx](../../text/49/PpmCheckResumePpmEngineFromSx_function_00499148.md) (`PAGELK` → `.text`)
  - `0x00B7EF7C` → [PopCurrentPowerStatePrecise](../../page/A3/PopCurrentPowerStatePrecise_function_00A35624.md) (`PAGELK` → `PAGE`)
  - `0x00B7EFA8` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGELK` → `.text`)
  - `0x00B7EFAD` → [PopIsDetailedSleepReliabilityDiagEnabled](../../page/AC/PopIsDetailedSleepReliabilityDiagEnabled_function_00ACEEA4.md) (`PAGELK` → `PAGE`)
  - `0x00B7EFBC` → [RtlBootStatusDisableFlushing](../../text/4F/RtlBootStatusDisableFlushing_function_004FC6C0.md) (`PAGELK` → `.text`)
  - `0x00B7EFDE` → [PopAllocateHiberContext](../../page/AD/PopAllocateHiberContext_function_00ADC05C.md) (`PAGELK` → `PAGE`)
  - `0x00B7F00A` → [PopNotifyTelemetryOsState](../../page/AC/PopNotifyTelemetryOsState_function_00AC3CB4.md) (`PAGELK` → `PAGE`)
  - `0x00B7F017` → [PopTransitionCheckpoint](../../page/A8/PopTransitionCheckpoint_function_00A8F3E8.md) (`PAGELK` → `PAGE`)
  - `0x00B7F030` → [PopCurrentPowerState](../../page/A3/PopCurrentPowerState_function_00A356D8.md) (`PAGELK` → `PAGE`)
  - `0x00B7F035` → [Feature_2845206840__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_2845206840__private_IsEnabledDeviceUsageNoInline_function_005D5B64.md) (`PAGELK` → `.text`)
  - `0x00B7F072` → [PopDiagTracePreSleepNotification](../../page/76/PopDiagTracePreSleepNotification_function_00762BE4.md) (`PAGELK` → `PAGE`)
  - `0x00B7F0AD` → [PopDiagTracePreSleepNotification](../../page/76/PopDiagTracePreSleepNotification_function_00762BE4.md) (`PAGELK` → `PAGE`)
  - `0x00B7F0BC` → [PopUmpoSendFlushSleepStudyLoggerNotification](../../text/4C/PopUmpoSendFlushSleepStudyLoggerNotification_function_004C4314.md) (`PAGELK` → `.text`)
  - `0x00B7F0C1` → [PopEsEnterSleepShutdown](../../page/AD/PopEsEnterSleepShutdown_function_00AD168C.md) (`PAGELK` → `PAGE`)
  - `0x00B7F0C6` → [PopThermalSxEntry](../../text/4E/PopThermalSxEntry_function_004E3D20.md) (`PAGELK` → `.text`)
  - `0x00B7F0CB` → [PopFanSxEntry](../../text/4B/PopFanSxEntry_function_004BEF04.md) (`PAGELK` → `.text`)
  - `0x00B7F120` → [RtlSetSystemBootStatusEx](../../page/A8/RtlSetSystemBootStatusEx_function_00A8B360.md) (`PAGELK` → `PAGE`)
  - `0x00B7F181` → [PopInitSystemSleeperThread](../../page/9E/PopInitSystemSleeperThread_function_009ECBA8.md) (`PAGELK` → `PAGE`)
  - `0x00B7F1A2` → [ExWakeTimersPause](../../text/4C/ExWakeTimersPause_function_004C6EB4.md) (`PAGELK` → `.text`)
  - `0x00B7F278` → [PopIsDozeSupported](../../page/AA/PopIsDozeSupported_function_00AA3DC0.md) (`PAGELK` → `PAGE`)
  - `0x00B7F352` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B7F3F6` → [PopQueryPowerSettingUlong](../../page/AC/PopQueryPowerSettingUlong_function_00ACCCC8.md) (`PAGELK` → `PAGE`)
  - `0x00B7F608` → [PopTransitionGetWakeTimerType](../../page/70/PopTransitionGetWakeTimerType_function_00705974.md) (`PAGELK` → `PAGE`)
  - `0x00B7F61A` → [PopTransitionGetWakeTimerType](../../page/70/PopTransitionGetWakeTimerType_function_00705974.md) (`PAGELK` → `PAGE`)
  - `0x00B7F627` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGELK` → `.text`)
  - `0x00B7F633` → [ExAcquireTimeRefreshLockExclusive](../../page/9C/ExAcquireTimeRefreshLockExclusive_function_009C5810.md) (`PAGELK` → `PAGE`)
  - `0x00B7F644` → [ExReleaseTimeRefreshLockExclusive](../../page/9C/ExReleaseTimeRefreshLockExclusive_function_009C5874.md) (`PAGELK` → `PAGE`)
  - `0x00B7F65E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B7F66A` → [PpmCheckPausePpmEngineForSx](../../text/49/PpmCheckPausePpmEngineForSx_function_00499104.md) (`PAGELK` → `.text`)
  - `0x00B7F677` → [PsLookupProcessByProcessId](../../page/8A/PsLookupProcessByProcessId_function_008A2AA0.md) (`PAGELK` → `PAGE`)
  - `0x00B7F684` → [PsLookupThreadByThreadId](../../page/86/PsLookupThreadByThreadId_function_00868300.md) (`PAGELK` → `PAGE`)
  - `0x00B7F6C4` → [PopPushPowerStateTransitionRecordWithCallback](../../text/43/PopPushPowerStateTransitionRecordWithCallback_function_00430A04.md) (`PAGELK` → `.text`)
  - `0x00B7F6D7` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGELK` → `.text`)
  - `0x00B7F6F0` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGELK` → `.text`)
  - `0x00B7F715` → [PopSetPowerActionWatchdogState](../../text/4C/PopSetPowerActionWatchdogState_function_004C86B8.md) (`PAGELK` → `.text`)
  - `0x00B7F7DF` → [StringCchPrintfW](../../text/47/StringCchPrintfW_function_0047BAD0.md) (`PAGELK` → `.text`)
  - `0x00B7F7EF` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGELK` → `.text`)
  - `0x00B7F800` → [IoRaiseInformationalHardError](../../text/4B/IoRaiseInformationalHardError_function_004B82B0.md) (`PAGELK` → `.text`)
  - `0x00B7F83D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B7F85E` → [PopNotifyTelemetryOsState](../../page/AC/PopNotifyTelemetryOsState_function_00AC3CB4.md) (`PAGELK` → `PAGE`)
  - `0x00B7F866` → [PopCancelIgnoreBatteryStatusChange](../../page/AD/PopCancelIgnoreBatteryStatusChange_function_00AD4338.md) (`PAGELK` → `PAGE`)
  - `0x00B7F87F` → [PopExecuteOnTargetProcessors](../../text/2D/PopExecuteOnTargetProcessors_function_002DD834.md) (`PAGELK` → `.text`)
  - `0x00B7F89E` → [PoClearBroadcast](../../page/AA/PoClearBroadcast_function_00AA3CE8.md) (`PAGELK` → `PAGE`)
  - `0x00B7F8AA` → [PopFanSxExit](../../text/4D/PopFanSxExit_function_004DAA14.md) (`PAGELK` → `.text`)
  - `0x00B7F8AF` → [PopEsExitSleep](../../page/AC/PopEsExitSleep_function_00AC5AF0.md) (`PAGELK` → `PAGE`)
  - `0x00B7F8E5` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`PAGELK` → `.text`)
  - `0x00B7F8F4` → [PopCurrentPowerState](../../page/A3/PopCurrentPowerState_function_00A356D8.md) (`PAGELK` → `PAGE`)
  - `0x00B7F91A` → [PopQueryMostRecentWakeSourceAttributes](../../page/AB/PopQueryMostRecentWakeSourceAttributes_function_00AB437C.md) (`PAGELK` → `PAGE`)
  - `0x00B7F968` → [SshSessionManagerTracePostSleepNotification](../../page/A8/SshSessionManagerTracePostSleepNotification_function_00A87054.md) (`PAGELK` → `PAGE`)
  - `0x00B7F98B` → [PopUpdateSystemIdleContext](../../page/91/PopUpdateSystemIdleContext_function_00911BB4.md) (`PAGELK` → `PAGE`)
  - `0x00B7F993` → [PopPowerAggregatorNotifySystemWake](../../page/76/PopPowerAggregatorNotifySystemWake_function_00764DAC.md) (`PAGELK` → `PAGE`)
  - `0x00B7FA03` → [PopDeferDoze](../../page/75/PopDeferDoze_function_0075FF88.md) (`PAGELK` → `PAGE`)
  - `0x00B7FABA` → [PopCheckPowerSourceAfterRtcWakeSet](../../text/5D/PopCheckPowerSourceAfterRtcWakeSet_function_005D5A88.md) (`PAGELK` → `.text`)
  - `0x00B7FAF1` → [ExWakeTimersResume](../../text/65/ExWakeTimersResume_function_00659270.md) (`PAGELK` → `.text`)
  - `0x00B7FB0D` → [PopBootLoaderTraceProcess](../../page/75/PopBootLoaderTraceProcess_function_0075CC3C.md) (`PAGELK` → `PAGE`)
  - `0x00B7FB19` → [PopResetActionDefaults](../../page/70/PopResetActionDefaults_function_007058E0.md) (`PAGELK` → `PAGE`)
  - `0x00B7FB21` → [PopSetPowerActionState](../../text/4B/PopSetPowerActionState_function_004BC8A8.md) (`PAGELK` → `.text`)
  - `0x00B7FB3B` → [PoSetUserPresent](../../text/48/PoSetUserPresent_function_004829A0.md) (`PAGELK` → `.text`)
  - `0x00B7FB4C` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`PAGELK` → `.text`)
  - `0x00B7FB51` → [PopCheckForWork](../../text/48/PopCheckForWork_function_00482CAC.md) (`PAGELK` → `.text`)
  - `0x00B7FB5C` → [PpmPerfReApplyStates](../../page/75/PpmPerfReApplyStates_function_0075ADA4.md) (`PAGELK` → `PAGE`)
  - `0x00B7FB6D` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGELK` → `.text`)
  - `0x00B7FB8C` → [ExDeleteWakeTimerInfo](../../text/65/ExDeleteWakeTimerInfo_function_00659254.md) (`PAGELK` → `.text`)
  - `0x00B7FBAF` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGELK` → `.text`)
  - `0x00B7FBBC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGELK` → `.text`)
  - `0x00B7FBCB` → [PopDiagTraceStateTransitionFailurePoint](../../page/76/PopDiagTraceStateTransitionFailurePoint_function_00763468.md) (`PAGELK` → `PAGE`)
  - `0x00B7FBE8` → [PopFxPrepareDevicesForShutdown](../../text/4F/PopFxPrepareDevicesForShutdown_function_004F5DF4.md) (`PAGELK` → `.text`)
  - `0x00B7FC13` → [PopTransitionCheckpoint](../../page/A8/PopTransitionCheckpoint_function_00A8F3E8.md) (`PAGELK` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B7E8C0  40 55                           push rbp
00B7E8C2  53                              push rbx
00B7E8C3  56                              push rsi
00B7E8C4  57                              push rdi
00B7E8C5  41 54                           push r12
00B7E8C7  41 55                           push r13
00B7E8C9  41 56                           push r14
00B7E8CB  41 57                           push r15
00B7E8CD  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00B7E8D2  48 81 EC D8 00 00 00            sub rsp, 0xd8
00B7E8D9  48 8B F9                        mov rdi, rcx
00B7E8DC  48 C7 45 B7 00 00 02 00         mov qword ptr [rbp - 0x49], 0x20000
00B7E8E4  33 C9                           xor ecx, ecx
00B7E8E6  48 8D 05 53 16 00 00            lea rax, [rip + 0x1653]
00B7E8ED  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00B7E8F1  8B F1                           mov esi, ecx
00B7E8F3  89 4D 6F                        mov dword ptr [rbp + 0x6f], ecx
00B7E8F6  48 8D 45 B7                     lea rax, [rbp - 0x49]
00B7E8FA  88 4F 0C                        mov byte ptr [rdi + 0xc], cl
00B7E8FD  4C 8D 77 6C                     lea r14, [rdi + 0x6c]
00B7E901  44 8D 69 01                     lea r13d, [rcx + 1]
00B7E905  88 4F 18                        mov byte ptr [rdi + 0x18], cl
00B7E908  89 4F 1C                        mov dword ptr [rdi + 0x1c], ecx
00B7E90B  4C 8D BF 48 01 00 00            lea r15, [rdi + 0x148]
00B7E912  48 89 4F 40                     mov qword ptr [rdi + 0x40], rcx
00B7E916  8B D9                           mov ebx, ecx
00B7E918  48 89 4F 28                     mov qword ptr [rdi + 0x28], rcx
00B7E91C  45 33 E4                        xor r12d, r12d
00B7E91F  89 4F 64                        mov dword ptr [rdi + 0x64], ecx
00B7E922  0F 57 C0                        xorps xmm0, xmm0
00B7E925  41 89 0E                        mov dword ptr [r14], ecx
00B7E928  41 8B D5                        mov edx, r13d
00B7E92B  48 89 8F C8 00 00 00            mov qword ptr [rdi + 0xc8], rcx
00B7E932  48 89 8F B0 00 00 00            mov qword ptr [rdi + 0xb0], rcx
00B7E939  48 89 8F B8 00 00 00            mov qword ptr [rdi + 0xb8], rcx
00B7E940  48 89 8F 30 01 00 00            mov qword ptr [rdi + 0x130], rcx
00B7E947  88 8F 50 01 00 00               mov byte ptr [rdi + 0x150], cl
00B7E94D  48 89 8F 40 01 00 00            mov qword ptr [rdi + 0x140], rcx
00B7E954  89 8F 4C 01 00 00               mov dword ptr [rdi + 0x14c], ecx
00B7E95A  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00B7E95E  48 8D 45 B7                     lea rax, [rbp - 0x49]
00B7E962  89 4D 77                        mov dword ptr [rbp + 0x77], ecx
00B7E965  48 89 4D 7F                     mov qword ptr [rbp + 0x7f], rcx
00B7E969  48 89 4D 97                     mov qword ptr [rbp - 0x69], rcx
00B7E96D  48 89 4D 9F                     mov qword ptr [rbp - 0x61], rcx
00B7E971  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
00B7E975  44 89 6F 70                     mov dword ptr [rdi + 0x70], r13d
00B7E979  44 89 6F 74                     mov dword ptr [rdi + 0x74], r13d
00B7E97D  44 88 AF D8 00 00 00            mov byte ptr [rdi + 0xd8], r13b
00B7E984  45 89 2F                        mov dword ptr [r15], r13d
00B7E987  4C 89 A7 C0 00 00 00            mov qword ptr [rdi + 0xc0], r12
00B7E98E  8B 05 78 E5 38 00               mov eax, dword ptr [rip + 0x38e578]
00B7E994  25 00 00 01 00                  and eax, 0x10000
00B7E999  44 89 67 58                     mov dword ptr [rdi + 0x58], r12d
00B7E99D  F7 D8                           neg eax
00B7E99F  0F 11 45 C7                     movups xmmword ptr [rbp - 0x39], xmm0
00B7E9A3  1B C9                           sbb ecx, ecx
00B7E9A5  81 E1 00 5D 1E EE               and ecx, 0xee1e5d00
00B7E9AB  81 C1 00 46 C3 23               add ecx, 0x23c34600
00B7E9B1  89 8F 54 01 00 00               mov dword ptr [rdi + 0x154], ecx
00B7E9B7  8D 4B 08                        lea ecx, [rbx + 8]
00B7E9BA  E8 29 0A F1 FF                  call 0x140a8f3e8
00B7E9BF  8D 43 02                        lea eax, [rbx + 2]
00B7E9C2  39 07                           cmp dword ptr [rdi], eax
00B7E9C4  75 05                           jne 0x140b7e9cb
00B7E9C6  E8 C5 71 F1 FF                  call 0x140a95b90
00B7E9CB  83 3F 04                        cmp dword ptr [rdi], 4
00B7E9CE  75 05                           jne 0x140b7e9d5
00B7E9D0  E8 8F 00 A5 FF                  call 0x1405cea64
00B7E9D5  E8 42 DC FF FF                  call 0x140b7c61c
00B7E9DA  48 8B 0D 1F 82 44 00            mov rcx, qword ptr [rip + 0x44821f]
00B7E9E1  E8 FA E7 EC FF                  call 0x140a4d1e0
00B7E9E6  E8 9D 2C 92 FF                  call 0x1404a1688
00B7E9EB  48 8D 05 AE 98 FF FF            lea rax, [rip - 0x6752]
00B7E9F2  4C 89 25 FF CD 38 00            mov qword ptr [rip + 0x38cdff], r12
00B7E9F9  33 C9                           xor ecx, ecx
00B7E9FB  48 89 05 EE CD 38 00            mov qword ptr [rip + 0x38cdee], rax
00B7EA02  4C 89 25 D7 CD 38 00            mov qword ptr [rip + 0x38cdd7], r12
00B7EA09  E8 16 8E F3 FF                  call 0x140ab7824
00B7EA0E  E8 2D 4A F5 FF                  call 0x140ad3440
00B7EA13  33 C9                           xor ecx, ecx
00B7EA15  E8 26 A2 EE FF                  call 0x140a68c40
00B7EA1A  44 39 2D D3 D4 38 00            cmp dword ptr [rip + 0x38d4d3], r13d
00B7EA21  41 8B CC                        mov ecx, r12d
00B7EA24  B8 02 00 00 00                  mov eax, 2
00B7EA29  0F 44 C8                        cmove ecx, eax
00B7EA2C  E8 67 F3 EC FF                  call 0x140a4dd98
00B7EA31  89 47 58                        mov dword ptr [rdi + 0x58], eax
00B7EA34  85 C0                           test eax, eax
00B7EA36  79 1B                           jns 0x140b7ea53
00B7EA38  41 8B D5                        mov edx, r13d
00B7EA3B  48 8D 0D 9E CD 38 00            lea rcx, [rip + 0x38cd9e]
00B7EA42  E8 D9 AA 77 FF                  call 0x1402f9520
00B7EA47  41 C7 06 05 00 00 00            mov dword ptr [r14], 5
00B7EA4E  E9 54 11 00 00                  jmp 0x140b7fba7
00B7EA53  E8 F8 86 95 FF                  call 0x1404d7150
00B7EA58  48 8D 4F 78                     lea rcx, [rdi + 0x78]
00B7EA5C  48 8D 55 9F                     lea rdx, [rbp - 0x61]
00B7EA60  E8 BF 6B EB FF                  call 0x140a35624
00B7EA65  E8 56 99 FF FF                  call 0x140b783c0
00B7EA6A  48 8D 15 A7 D3 38 00            lea rdx, [rip + 0x38d3a7]
00B7EA71  44 88 6F 30                     mov byte ptr [rdi + 0x30], r13b
00B7EA75  48 8D 0D 44 E4 38 00            lea rcx, [rip + 0x38e444]
00B7EA7C  E8 9B 29 D9 FF                  call 0x14091141c
00B7EA81  8A 05 BA D2 38 00               mov al, byte ptr [rip + 0x38d2ba]
00B7EA87  84 C0                           test al, al
00B7EA89  74 30                           je 0x140b7eabb
00B7EA8B  3C 02                           cmp al, 2
00B7EA8D  74 31                           je 0x140b7eac0
00B7EA8F  E8 7C 99 FF FF                  call 0x140b78410
00B7EA94  E8 4F 52 F2 FF                  call 0x140aa3ce8
00B7EA99  41 8B D5                        mov edx, r13d
00B7EA9C  48 8D 0D 3D CD 38 00            lea rcx, [rip + 0x38cd3d]
00B7EAA3  E8 78 AA 77 FF                  call 0x1402f9520
00B7EAA8  41 C7 06 06 00 00 00            mov dword ptr [r14], 6
00B7EAAF  C7 47 58 21 00 00 C0            mov dword ptr [rdi + 0x58], 0xc0000021
00B7EAB6  E9 EC 10 00 00                  jmp 0x140b7fba7
00B7EABB  E8 20 6E B8 FF                  call 0x1407058e0
00B7EAC0  B1 03                           mov cl, 3
00B7EAC2  E8 E1 DD 93 FF                  call 0x1404bc8a8
00B7EAC7  48 8B 05 02 D2 38 00            mov rax, qword ptr [rip + 0x38d202]
00B7EACE  48 89 05 B3 D2 38 00            mov qword ptr [rip + 0x38d2b3], rax
00B7EAD5  E8 A2 49 96 FF                  call 0x1404e347c
00B7EADA  E8 39 2C EB FF                  call 0x140a31718
00B7EADF  48 8D 8F D0 00 00 00            lea rcx, [rdi + 0xd0]
00B7EAE6  E8 A5 52 F4 FF                  call 0x140ac3d90
00B7EAEB  45 33 C9                        xor r9d, r9d
00B7EAEE  48 8D 15 EB 51 95 FF            lea rdx, [rip - 0x6aae15]
00B7EAF5  45 33 C0                        xor r8d, r8d
00B7EAF8  48 8D 0D 21 86 44 00            lea rcx, [rip + 0x448621]
00B7EAFF  E8 30 ED 75 FF                  call 0x1402dd834
00B7EB04  41 BD 06 00 00 00               mov r13d, 6
00B7EB0A  44 39 2F                        cmp dword ptr [rdi], r13d
00B7EB0D  75 07                           jne 0x140b7eb16
00B7EB0F  44 89 2D 2E D2 38 00            mov dword ptr [rip + 0x38d22e], r13d
00B7EB16  8B 0F                           mov ecx, dword ptr [rdi]
00B7EB18  8D 41 FC                        lea eax, [rcx - 4]
00B7EB1B  83 F8 02                        cmp eax, 2
00B7EB1E  77 41                           ja 0x140b7eb61
00B7EB20  C6 05 F9 D1 38 00 01            mov byte ptr [rip + 0x38d1f9], 1
00B7EB27  83 F9 05                        cmp ecx, 5
00B7EB2A  75 07                           jne 0x140b7eb33
00B7EB2C  C6 05 EE D1 38 00 01            mov byte ptr [rip + 0x38d1ee], 1
00B7EB33  4C 39 25 E6 D3 38 00            cmp qword ptr [rip + 0x38d3e6], r12
00B7EB3A  74 25                           je 0x140b7eb61
00B7EB3C  4C 39 25 E5 D3 38 00            cmp qword ptr [rip + 0x38d3e5], r12
00B7EB43  74 1C                           je 0x140b7eb61
00B7EB45  E8 1A A6 C7 FF                  call 0x1407f9164
00B7EB4A  85 C0                           test eax, eax
00B7EB4C  74 13                           je 0x140b7eb61
00B7EB4E  48 8B 15 D3 D3 38 00            mov rdx, qword ptr [rip + 0x38d3d3]
00B7EB55  48 8B 0D C4 D3 38 00            mov rcx, qword ptr [rip + 0x38d3c4]
00B7EB5C  E8 1B F9 BD FF                  call 0x14075e47c
00B7EB61  8B 07                           mov eax, dword ptr [rdi]
00B7EB63  48 8D 77 48                     lea rsi, [rdi + 0x48]
00B7EB67  44 88 26                        mov byte ptr [rsi], r12b
00B7EB6A  B9 02 00 00 00                  mov ecx, 2
00B7EB6F  4C 8D 67 10                     lea r12, [rdi + 0x10]
00B7EB73  2B C1                           sub eax, ecx
00B7EB75  41 21 1C 24                     and dword ptr [r12], ebx
00B7EB79  83 F8 01                        cmp eax, 1
00B7EB7C  77 07                           ja 0x140b7eb85
00B7EB7E  C6 05 9B D1 38 00 01            mov byte ptr [rip + 0x38d19b], 1
00B7EB85  88 5F 60                        mov byte ptr [rdi + 0x60], bl
00B7EB88  48 8D 9F 4C 01 00 00            lea rbx, [rdi + 0x14c]
00B7EB8F  C7 47 58 20 01 00 C0            mov dword ptr [rdi + 0x58], 0xc0000120
00B7EB96  80 7F 30 00                     cmp byte ptr [rdi + 0x30], 0
00B7EB9A  75 0E                           jne 0x140b7ebaa
00B7EB9C  E8 1F 98 FF FF                  call 0x140b783c0
00B7EBA1  B9 02 00 00 00                  mov ecx, 2
00B7EBA6  C6 47 30 01                     mov byte ptr [rdi + 0x30], 1
00B7EBAA  83 3D 93 D1 38 00 00            cmp dword ptr [rip + 0x38d193], 0
00B7EBB1  0F 84 5B 0C 00 00               je 0x140b7f812
00B7EBB7  8A 05 83 D1 38 00               mov al, byte ptr [rip + 0x38d183]
00B7EBBD  88 47 68                        mov byte ptr [rdi + 0x68], al
00B7EBC0  C6 05 79 D1 38 00 00            mov byte ptr [rip + 0x38d179], 0
00B7EBC7  8B 47 58                        mov eax, dword ptr [rdi + 0x58]
00B7EBCA  3D 20 01 00 C0                  cmp eax, 0xc0000120
00B7EBCF  75 54                           jne 0x140b7ec25
00B7EBD1  84 4F 68                        test byte ptr [rdi + 0x68], cl
00B7EBD4  74 12                           je 0x140b7ebe8
00B7EBD6  8B 05 70 D1 38 00               mov eax, dword ptr [rip + 0x38d170]
00B7EBDC  85 C0                           test eax, eax
00B7EBDE  78 08                           js 0x140b7ebe8
00B7EBE0  A8 03                           test al, 3
00B7EBE2  0F 85 65 02 00 00               jne 0x140b7ee4d
00B7EBE8  4C 8B CE                        mov r9, rsi
00B7EBEB  4C 8D 05 7A D1 38 00            lea r8, [rip + 0x38d17a]
00B7EBF2  49 8B D4                        mov rdx, r12
00B7EBF5  48 8D 0D 4C D1 38 00            lea rcx, [rip + 0x38d14c]
00B7EBFC  E8 EB 9E 93 FF                  call 0x1404b8aec
00B7EC01  8B 05 3D D1 38 00               mov eax, dword ptr [rip + 0x38d13d]
00B7EC07  83 C0 FC                        add eax, -4
00B7EC0A  83 F8 02                        cmp eax, 2
00B7EC0D  77 10                           ja 0x140b7ec1f
00B7EC0F  C6 05 2C D1 38 00 01            mov byte ptr [rip + 0x38d12c], 1
00B7EC16  8B 47 08                        mov eax, dword ptr [rdi + 8]
00B7EC19  89 05 2D D1 38 00               mov dword ptr [rip + 0x38d12d], eax
00B7EC1F  83 67 58 00                     and dword ptr [rdi + 0x58], 0
00B7EC23  EB 08                           jmp 0x140b7ec2d
00B7EC25  85 C0                           test eax, eax
00B7EC27  0F 88 3F 02 00 00               js 0x140b7ee6c
00B7EC2D  E8 DE 97 FF FF                  call 0x140b78410
00B7EC32  83 23 00                        and dword ptr [rbx], 0
00B7EC35  48 8D 0D FC 58 4A FF            lea rcx, [rip - 0xb5a704]
00B7EC3C  4C 8B C3                        mov r8, rbx
00B7EC3F  C6 47 30 00                     mov byte ptr [rdi + 0x30], 0
00B7EC43  49 8B D7                        mov rdx, r15
00B7EC46  41 C7 07 01 00 00 00            mov dword ptr [r15], 1
00B7EC4D  E8 76 E0 F4 FF                  call 0x140acccc8
00B7EC52  33 C0                           xor eax, eax
00B7EC54  F7 05 EE D0 38 00 00 00 00 40   test dword ptr [rip + 0x38d0ee], 0x40000000
00B7EC5E  74 05                           je 0x140b7ec65
00B7EC60  41 89 07                        mov dword ptr [r15], eax
00B7EC63  89 03                           mov dword ptr [rbx], eax
00B7EC65  38 05 CB D1 38 00               cmp byte ptr [rip + 0x38d1cb], al
00B7EC6B  75 12                           jne 0x140b7ec7f
00B7EC6D  38 05 B1 D1 38 00               cmp byte ptr [rip + 0x38d1b1], al
00B7EC73  75 0A                           jne 0x140b7ec7f
00B7EC75  38 05 B0 D1 38 00               cmp byte ptr [rip + 0x38d1b0], al
00B7EC7B  75 02                           jne 0x140b7ec7f
00B7EC7D  89 03                           mov dword ptr [rbx], eax
00B7EC7F  E8 A4 ED F1 FF                  call 0x140a9da28
00B7EC84  8B 15 C2 D0 38 00               mov edx, dword ptr [rip + 0x38d0c2]
00B7EC8A  48 8D 0D DF D0 38 00            lea rcx, [rip + 0x38d0df]
00B7EC91  8B 05 D5 D0 38 00               mov eax, dword ptr [rip + 0x38d0d5]
00B7EC97  89 05 D3 D0 38 00               mov dword ptr [rip + 0x38d0d3], eax
00B7EC9D  C1 EA 1B                        shr edx, 0x1b
00B7ECA0  83 E2 02                        and edx, 2
00B7ECA3  89 57 5C                        mov dword ptr [rdi + 0x5c], edx
00B7ECA6  45 8B 0C 24                     mov r9d, dword ptr [r12]
00B7ECAA  44 8B 05 97 D0 38 00            mov r8d, dword ptr [rip + 0x38d097]
00B7ECB1  E8 6A 3D F5 FF                  call 0x140ad2a20
00B7ECB6  8B 47 08                        mov eax, dword ptr [rdi + 8]
00B7ECB9  A8 08                           test al, 8
00B7ECBB  74 22                           je 0x140b7ecdf
00B7ECBD  C6 05 9C D2 38 00 01            mov byte ptr [rip + 0x38d29c], 1
00B7ECC4  C6 47 18 00                     mov byte ptr [rdi + 0x18], 0
00B7ECC8  C7 05 A2 D0 38 00 05 00 00 00   mov dword ptr [rip + 0x38d0a2], 5
00B7ECD2  44 89 6F 20                     mov dword ptr [rdi + 0x20], r13d
00B7ECD6  48 63 05 8F D0 38 00            movsxd rax, dword ptr [rip + 0x38d08f]
00B7ECDD  EB 3D                           jmp 0x140b7ed1c
00B7ECDF  E8 C0 08 F3 FF                  call 0x140aaf5a4
00B7ECE4  84 C0                           test al, al
00B7ECE6  8B 05 80 D0 38 00               mov eax, dword ptr [rip + 0x38d080]
00B7ECEC  74 1A                           je 0x140b7ed08
00B7ECEE  89 47 20                        mov dword ptr [rdi + 0x20], eax
00B7ECF1  41 8B CD                        mov ecx, r13d
00B7ECF4  C7 05 76 D0 38 00 05 00 00 00   mov dword ptr [rip + 0x38d076], 5
00B7ECFE  C6 47 18 01                     mov byte ptr [rdi + 0x18], 1
00B7ED02  44 89 6F 34                     mov dword ptr [rdi + 0x34], r13d
00B7ED06  EB 2E                           jmp 0x140b7ed36
00B7ED08  89 05 66 D0 38 00               mov dword ptr [rip + 0x38d066], eax
00B7ED0E  89 47 20                        mov dword ptr [rdi + 0x20], eax
00B7ED11  48 63 05 54 D0 38 00            movsxd rax, dword ptr [rip + 0x38d054]
00B7ED18  C6 47 18 00                     mov byte ptr [rdi + 0x18], 0
00B7ED1C  48 8D 0D DD 12 48 FF            lea rcx, [rip - 0xb7ed23]
00B7ED23  8B 8C 81 58 97 02 00            mov ecx, dword ptr [rcx + rax*4 + 0x29758]
00B7ED2A  89 4F 34                        mov dword ptr [rdi + 0x34], ecx
00B7ED2D  41 3B CD                        cmp ecx, r13d
00B7ED30  0F 87 F3 00 00 00               ja 0x140b7ee29
00B7ED36  48 63 C1                        movsxd rax, ecx
00B7ED39  48 8D 0C 40                     lea rcx, [rax + rax*2]
00B7ED3D  48 8D 05 BC 12 48 FF            lea rax, [rip - 0xb7ed44]
00B7ED44  48 83 BC C8 48 CC F0 00 00      cmp qword ptr [rax + rcx*8 + 0xf0cc48], 0
00B7ED4D  0F 84 D6 00 00 00               je 0x140b7ee29
00B7ED53  8B 47 08                        mov eax, dword ptr [rdi + 8]
00B7ED56  A8 08                           test al, 8
00B7ED58  74 05                           je 0x140b7ed5f
00B7ED5A  41 8B CD                        mov ecx, r13d
00B7ED5D  EB 0F                           jmp 0x140b7ed6e
00B7ED5F  80 3D DC CF 38 00 00            cmp byte ptr [rip + 0x38cfdc], 0
00B7ED66  75 0D                           jne 0x140b7ed75
00B7ED68  8B 0D FE CF 38 00               mov ecx, dword ptr [rip + 0x38cffe]
00B7ED6E  E8 89 99 F2 FF                  call 0x140aa86fc
00B7ED73  EB 0A                           jmp 0x140b7ed7f
00B7ED75  E8 C6 6C B8 FF                  call 0x140705a40
00B7ED7A  E8 69 04 BE FF                  call 0x14075f1e8
00B7ED7F  E8 3C 96 FF FF                  call 0x140b783c0
00B7ED84  44 84 2D B5 CF 38 00            test byte ptr [rip + 0x38cfb5], r13b
00B7ED8B  74 10                           je 0x140b7ed9d
00B7ED8D  C6 47 30 01                     mov byte ptr [rdi + 0x30], 1
00B7ED91  C7 47 58 20 01 00 C0            mov dword ptr [rdi + 0x58], 0xc0000120
00B7ED98  E9 A6 00 00 00                  jmp 0x140b7ee43
00B7ED9D  48 8B 05 C4 A1 38 00            mov rax, qword ptr [rip + 0x38a1c4]
00B7EDA4  44 8A 78 02                     mov r15b, byte ptr [rax + 2]
00B7EDA8  48 8B 58 38                     mov rbx, qword ptr [rax + 0x38]
00B7EDAC  E8 5F 96 FF FF                  call 0x140b78410
00B7EDB1  B9 0A 00 00 00                  mov ecx, 0xa
00B7EDB6  E8 D5 8E FF FF                  call 0x140b77c90
00B7EDBB  C6 05 A6 CF 38 00 03            mov byte ptr [rip + 0x38cfa6], 3
00B7EDC2  8A 0E                           mov cl, byte ptr [rsi]
00B7EDC4  E8 3B 6E F3 FF                  call 0x140ab5c04
00B7EDC9  80 3E 00                        cmp byte ptr [rsi], 0
00B7EDCC  74 3D                           je 0x140b7ee0b
00B7EDCE  E8 3D 73 FF FF                  call 0x140b76110
00B7EDD3  89 47 58                        mov dword ptr [rdi + 0x58], eax
00B7EDD6  85 C0                           test eax, eax
00B7EDD8  79 2D                           jns 0x140b7ee07
00B7EDDA  3D 20 01 00 C0                  cmp eax, 0xc0000120
00B7EDDF  74 2A                           je 0x140b7ee0b
00B7EDE1  8A 57 18                        mov dl, byte ptr [rdi + 0x18]
00B7EDE4  4C 8B C6                        mov r8, rsi
00B7EDE7  41 8B 0C 24                     mov ecx, dword ptr [r12]
00B7EDEB  E8 F8 70 F3 FF                  call 0x140ab5ee8
00B7EDF0  88 47 24                        mov byte ptr [rdi + 0x24], al
00B7EDF3  84 C0                           test al, al
00B7EDF5  74 6E                           je 0x140b7ee65
00B7EDF7  4C 8D BF 48 01 00 00            lea r15, [rdi + 0x148]
00B7EDFE  48 8D 9F 4C 01 00 00            lea rbx, [rdi + 0x14c]
00B7EE05  EB 38                           jmp 0x140b7ee3f
00B7EE07  C6 47 60 01                     mov byte ptr [rdi + 0x60], 1
00B7EE0B  8B 47 58                        mov eax, dword ptr [rdi + 0x58]
00B7EE0E  3D 20 01 00 C0                  cmp eax, 0xc0000120
00B7EE13  0F 85 AD 01 00 00               jne 0x140b7efc6
00B7EE19  4C 8D BF 48 01 00 00            lea r15, [rdi + 0x148]
00B7EE20  48 8D 9F 4C 01 00 00            lea rbx, [rdi + 0x14c]
00B7EE27  EB 1A                           jmp 0x140b7ee43
00B7EE29  8A 57 18                        mov dl, byte ptr [rdi + 0x18]
00B7EE2C  4C 8B C6                        mov r8, rsi
00B7EE2F  41 8B 0C 24                     mov ecx, dword ptr [r12]
00B7EE33  E8 B0 70 F3 FF                  call 0x140ab5ee8
00B7EE38  88 47 24                        mov byte ptr [rdi + 0x24], al
00B7EE3B  84 C0                           test al, al
00B7EE3D  74 2D                           je 0x140b7ee6c
00B7EE3F  83 67 58 00                     and dword ptr [rdi + 0x58], 0
00B7EE43  B9 02 00 00 00                  mov ecx, 2
00B7EE48  E9 49 FD FF FF                  jmp 0x140b7eb96
00B7EE4D  BE 02 00 00 00                  mov esi, 2
00B7EE52  8B CE                           mov ecx, esi
00B7EE54  E8 CB 3E 90 FF                  call 0x140482d24
00B7EE59  45 33 E4                        xor r12d, r12d
00B7EE5C  41 C7 06 08 00 00 00            mov dword ptr [r14], 8
00B7EE63  EB 0F                           jmp 0x140b7ee74
00B7EE65  41 C7 06 09 00 00 00            mov dword ptr [r14], 9
00B7EE6C  45 33 E4                        xor r12d, r12d
00B7EE6F  BE 02 00 00 00                  mov esi, 2
00B7EE74  44 38 67 30                     cmp byte ptr [rdi + 0x30], r12b
00B7EE78  74 05                           je 0x140b7ee7f
00B7EE7A  E8 91 95 FF FF                  call 0x140b78410
00B7EE7F  44 38 25 DA D0 38 00            cmp byte ptr [rip + 0x38d0da], r12b
00B7EE86  74 27                           je 0x140b7eeaf
00B7EE88  33 C9                           xor ecx, ecx
00B7EE8A  E8 51 F9 7F FF                  call 0x14037e7e0
00B7EE8F  48 8D 15 8A D6 38 00            lea rdx, [rip + 0x38d68a]
00B7EE96  48 89 05 83 D6 38 00            mov qword ptr [rip + 0x38d683], rax
00B7EE9D  48 8D 0D 74 D6 38 00            lea rcx, [rip + 0x38d674]
00B7EEA4  E8 D7 A8 FF FF                  call 0x140b79780
00B7EEA9  89 05 95 D0 38 00               mov dword ptr [rip + 0x38d095], eax
00B7EEAF  44 39 67 58                     cmp dword ptr [rdi + 0x58], r12d
00B7EEB3  7C 73                           jl 0x140b7ef28
00B7EEB5  48 8B 87 30 01 00 00            mov rax, qword ptr [rdi + 0x130]
00B7EEBC  BA 01 00 00 00                  mov edx, 1
00B7EEC1  8A CA                           mov cl, dl
00B7EEC3  48 89 05 D6 CE 38 00            mov qword ptr [rip + 0x38ced6], rax
00B7EECA  E8 C9 CE FF FF                  call 0x140b7bd98
00B7EECF  48 8B 05 D2 1C 28 00            mov rax, qword ptr [rip + 0x281cd2]
00B7EED6  33 D2                           xor edx, edx
00B7EED8  B1 01                           mov cl, 1
00B7EEDA  E8 F1 BB B3 FF                  call 0x1406baad0
00B7EEDF  85 C0                           test eax, eax
00B7EEE1  74 07                           je 0x140b7eeea
00B7EEE3  C6 87 A8 00 00 00 01            mov byte ptr [rdi + 0xa8], 1
00B7EEEA  33 C9                           xor ecx, ecx
00B7EEEC  E8 EF F8 7F FF                  call 0x14037e7e0
00B7EEF1  45 33 C0                        xor r8d, r8d
00B7EEF4  48 89 05 2D D4 38 00            mov qword ptr [rip + 0x38d42d], rax
00B7EEFB  33 D2                           xor edx, edx
00B7EEFD  8B CE                           mov ecx, esi
00B7EEFF  E8 94 BD FF FF                  call 0x140b7ac98
00B7EF04  48 B8 08 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000008
00B7EF0E  48 8B 00                        mov rax, qword ptr [rax]
00B7EF11  48 89 05 80 CE 38 00            mov qword ptr [rip + 0x38ce80], rax
00B7EF18  E8 03 EA FF FF                  call 0x140b7d920
00B7EF1D  83 7F 1C 04                     cmp dword ptr [rdi + 0x1c], 4
00B7EF21  75 05                           jne 0x140b7ef28
00B7EF23  E8 90 21 FF FF                  call 0x140b710b8
00B7EF28  C6 05 3A CE 38 00 01            mov byte ptr [rip + 0x38ce3a], 1
00B7EF2F  44 88 25 EA CD 38 00            mov byte ptr [rip + 0x38cdea], r12b
00B7EF36  44 88 25 E4 CD 38 00            mov byte ptr [rip + 0x38cde4], r12b
00B7EF3D  44 38 67 60                     cmp byte ptr [rdi + 0x60], r12b
00B7EF41  74 21                           je 0x140b7ef64
00B7EF43  33 D2                           xor edx, edx
00B7EF45  45 33 C0                        xor r8d, r8d
00B7EF48  8D 4A 03                        lea ecx, [rdx + 3]
00B7EF4B  E8 48 BD FF FF                  call 0x140b7ac98
00B7EF50  E8 BB 71 FF FF                  call 0x140b76110
00B7EF55  45 33 C0                        xor r8d, r8d
00B7EF58  41 8D 50 01                     lea edx, [r8 + 1]
00B7EF5C  8D 4A 02                        lea ecx, [rdx + 2]
00B7EF5F  E8 34 BD FF FF                  call 0x140b7ac98
00B7EF64  44 39 67 58                     cmp dword ptr [rdi + 0x58], r12d
00B7EF68  7C 05                           jl 0x140b7ef6f
00B7EF6A  E8 C1 EC AD FF                  call 0x14065dc30
00B7EF6F  E8 D4 A1 91 FF                  call 0x140499148
00B7EF74  48 8D 55 9F                     lea rdx, [rbp - 0x61]
00B7EF78  48 8D 4F 78                     lea rcx, [rdi + 0x78]
00B7EF7C  E8 A3 66 EB FF                  call 0x140a35624
00B7EF81  44 38 A7 A8 00 00 00            cmp byte ptr [rdi + 0xa8], r12b
00B7EF88  74 23                           je 0x140b7efad
00B7EF8A  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00B7EF8F  48 8D 0D 22 19 4A FF            lea rcx, [rip - 0xb5e6de]
00B7EF96  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00B7EF9B  45 33 C9                        xor r9d, r9d
00B7EF9E  45 33 C0                        xor r8d, r8d
00B7EFA1  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00B7EFA6  33 D2                           xor edx, edx
00B7EFA8  E8 63 1D B3 FF                  call 0x1406b0d10
00B7EFAD  E8 F2 FE F4 FF                  call 0x140aceea4
00B7EFB2  84 C0                           test al, al
00B7EFB4  0F 85 67 08 00 00               jne 0x140b7f821
00B7EFBA  B1 01                           mov cl, 1
00B7EFBC  E8 FF D6 97 FF                  call 0x1404fc6c0
00B7EFC1  E9 62 08 00 00                  jmp 0x140b7f828
00B7EFC6  45 33 E4                        xor r12d, r12d
00B7EFC9  85 C0                           test eax, eax
00B7EFCB  0F 88 9E FE FF FF               js 0x140b7ee6f
00B7EFD1  41 8D 4C 24 0D                  lea ecx, [r12 + 0xd]
00B7EFD6  E8 B5 8C FF FF                  call 0x140b77c90
00B7EFDB  49 8B CE                        mov rcx, r14
00B7EFDE  E8 79 D0 F5 FF                  call 0x140adc05c
00B7EFE3  89 47 58                        mov dword ptr [rdi + 0x58], eax
00B7EFE6  85 C0                           test eax, eax
00B7EFE8  0F 88 81 FE FF FF               js 0x140b7ee6f
00B7EFEE  44 8B 4F 08                     mov r9d, dword ptr [rdi + 8]
00B7EFF2  44 8B 05 7B CD 38 00            mov r8d, dword ptr [rip + 0x38cd7b]
00B7EFF9  8B 15 6D CD 38 00               mov edx, dword ptr [rip + 0x38cd6d]
00B7EFFF  8B 0D 3F CD 38 00               mov ecx, dword ptr [rip + 0x38cd3f]
00B7F005  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00B7F00A  E8 A5 4C F4 FF                  call 0x140ac3cb4
00B7F00F  33 D2                           xor edx, edx
00B7F011  89 47 64                        mov dword ptr [rdi + 0x64], eax
00B7F014  8D 4A 09                        lea ecx, [rdx + 9]
00B7F017  E8 CC 03 F1 FF                  call 0x140a8f3e8
00B7F01C  44 38 25 1F CD 38 00            cmp byte ptr [rip + 0x38cd1f], r12b
00B7F023  0F 85 98 00 00 00               jne 0x140b7f0c1
00B7F029  48 8D 77 78                     lea rsi, [rdi + 0x78]
00B7F02D  48 8B CE                        mov rcx, rsi
00B7F030  E8 A3 66 EB FF                  call 0x140a356d8
00B7F035  E8 2A 6B A5 FF                  call 0x1405d5b64
00B7F03A  85 C0                           test eax, eax
00B7F03C  74 40                           je 0x140b7f07e
00B7F03E  E8 7D 93 FF FF                  call 0x140b783c0
00B7F043  48 8B 05 16 CD 38 00            mov rax, qword ptr [rip + 0x38cd16]
00B7F04A  44 8B 0D 07 CD 38 00            mov r9d, dword ptr [rip + 0x38cd07]
00B7F051  44 8B 05 FC CC 38 00            mov r8d, dword ptr [rip + 0x38ccfc]
00B7F058  8B 15 16 CD 38 00               mov edx, dword ptr [rip + 0x38cd16]
00B7F05E  8B 4F 20                        mov ecx, dword ptr [rdi + 0x20]
00B7F061  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B7F066  8B 47 64                        mov eax, dword ptr [rdi + 0x64]
00B7F069  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00B7F06E  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00B7F072  E8 6D 3B BE FF                  call 0x140762be4
00B7F077  E8 94 93 FF FF                  call 0x140b78410
00B7F07C  EB 34                           jmp 0x140b7f0b2
00B7F07E  48 8B 05 DB CC 38 00            mov rax, qword ptr [rip + 0x38ccdb]
00B7F085  44 8B 0D CC CC 38 00            mov r9d, dword ptr [rip + 0x38cccc]
00B7F08C  44 8B 05 C1 CC 38 00            mov r8d, dword ptr [rip + 0x38ccc1]
00B7F093  8B 15 DB CC 38 00               mov edx, dword ptr [rip + 0x38ccdb]
00B7F099  8B 4F 20                        mov ecx, dword ptr [rdi + 0x20]
00B7F09C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B7F0A1  8B 47 64                        mov eax, dword ptr [rdi + 0x64]
00B7F0A4  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00B7F0A9  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00B7F0AD  E8 32 3B BE FF                  call 0x140762be4
00B7F0B2  B9 10 00 00 00                  mov ecx, 0x10
00B7F0B7  E8 D4 8B FF FF                  call 0x140b77c90
00B7F0BC  E8 53 52 94 FF                  call 0x1404c4314
00B7F0C1  E8 C6 25 F5 FF                  call 0x140ad168c
00B7F0C6  E8 55 4C 96 FF                  call 0x1404e3d20
00B7F0CB  E8 34 FE 93 FF                  call 0x1404bef04
00B7F0D0  44 38 67 0C                     cmp byte ptr [rdi + 0xc], r12b
00B7F0D4  75 53                           jne 0x140b7f129
00B7F0D6  44 38 25 65 CC 38 00            cmp byte ptr [rip + 0x38cc65], r12b
00B7F0DD  74 46                           je 0x140b7f125
00B7F0DF  45 33 C0                        xor r8d, r8d
00B7F0E2  C6 45 67 01                     mov byte ptr [rbp + 0x67], 1
00B7F0E6  48 8D 45 67                     lea rax, [rbp + 0x67]
00B7F0EA  C7 45 E7 05 00 00 00            mov dword ptr [rbp - 0x19], 5
00B7F0F1  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
00B7F0F5  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00B7F0F9  48 B8 C4 02 00 00 80 F7 FF FF   movabs rax, 0xfffff780000002c4
00B7F103  C7 45 F7 01 00 00 00            mov dword ptr [rbp - 9], 1
00B7F10A  41 8D 50 02                     lea edx, [r8 + 2]
00B7F10E  C7 45 FF 0B 00 00 00            mov dword ptr [rbp - 1], 0xb
00B7F115  48 89 45 07                     mov qword ptr [rbp + 7], rax
00B7F119  C7 45 0F 04 00 00 00            mov dword ptr [rbp + 0xf], 4
00B7F120  E8 3B C2 F0 FF                  call 0x140a8b360
00B7F125  C6 47 0C 01                     mov byte ptr [rdi + 0xc], 1
00B7F129  B9 05 00 00 00                  mov ecx, 5
00B7F12E  44 38 67 18                     cmp byte ptr [rdi + 0x18], r12b
00B7F132  75 06                           jne 0x140b7f13a
00B7F134  8B 0D 32 CC 38 00               mov ecx, dword ptr [rip + 0x38cc32]
00B7F13A  E8 F9 C7 FF FF                  call 0x140b7b938
00B7F13F  8B 05 27 CC 38 00               mov eax, dword ptr [rip + 0x38cc27]
00B7F145  39 05 29 CC 38 00               cmp dword ptr [rip + 0x38cc29], eax
00B7F14B  7D 06                           jge 0x140b7f153
00B7F14D  89 05 21 CC 38 00               mov dword ptr [rip + 0x38cc21], eax
00B7F153  44 38 25 E8 CB 38 00            cmp byte ptr [rip + 0x38cbe8], r12b
00B7F15A  BE 02 00 00 00                  mov esi, 2
00B7F15F  40 88 35 02 CC 38 00            mov byte ptr [rip + 0x38cc02], sil
00B7F166  0F 85 7C 0A 00 00               jne 0x140b7fbe8
00B7F16C  8B 4F 34                        mov ecx, dword ptr [rdi + 0x34]
00B7F16F  48 8D 97 E0 00 00 00            lea rdx, [rdi + 0xe0]
00B7F176  4C 8D 45 C7                     lea r8, [rbp - 0x39]
00B7F17A  44 88 25 8B 1D 39 00            mov byte ptr [rip + 0x391d8b], r12b
00B7F181  E8 22 DA E6 FF                  call 0x1409ecba8
00B7F186  89 47 58                        mov dword ptr [rdi + 0x58], eax
00B7F189  85 C0                           test eax, eax
00B7F18B  79 0C                           jns 0x140b7f199
00B7F18D  41 C7 06 14 00 00 00            mov dword ptr [r14], 0x14
00B7F194  E9 DB FC FF FF                  jmp 0x140b7ee74
00B7F199  44 38 25 60 CC 38 00            cmp byte ptr [rip + 0x38cc60], r12b
00B7F1A0  75 0C                           jne 0x140b7f1ae
00B7F1A2  E8 0D 7D 94 FF                  call 0x1404c6eb4
00B7F1A7  C6 05 52 CC 38 00 01            mov byte ptr [rip + 0x38cc52], 1
00B7F1AE  48 A1 08 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000008]
00B7F1B8  49 BA 14 00 00 00 80 F7 FF FF   movabs r10, 0xfffff78000000014
00B7F1C2  48 89 87 98 00 00 00            mov qword ptr [rdi + 0x98], rax
00B7F1C9  4D 8B 12                        mov r10, qword ptr [r10]
00B7F1CC  48 8B 35 D5 D6 38 00            mov rsi, qword ptr [rip + 0x38d6d5]
00B7F1D3  4C 89 97 A0 00 00 00            mov qword ptr [rdi + 0xa0], r10
00B7F1DA  4C 89 A7 B8 00 00 00            mov qword ptr [rdi + 0xb8], r12
00B7F1E1  48 85 F6                        test rsi, rsi
00B7F1E4  0F 85 2C 01 00 00               jne 0x140b7f316
00B7F1EA  4C 39 25 AF D6 38 00            cmp qword ptr [rip + 0x38d6af], r12
00B7F1F1  0F 85 1F 01 00 00               jne 0x140b7f316
00B7F1F7  44 8A 1D D6 DC 38 00            mov r11b, byte ptr [rip + 0x38dcd6]
00B7F1FE  45 84 DB                        test r11b, r11b
00B7F201  74 58                           je 0x140b7f25b
00B7F203  83 3D 62 CB 38 00 05            cmp dword ptr [rip + 0x38cb62], 5
00B7F20A  75 4F                           jne 0x140b7f25b
00B7F20C  44 38 25 4D CD 38 00            cmp byte ptr [rip + 0x38cd4d], r12b
00B7F213  75 46                           jne 0x140b7f25b
00B7F215  8D 46 02                        lea eax, [rsi + 2]
00B7F218  39 05 36 CB 38 00               cmp dword ptr [rip + 0x38cb36], eax
00B7F21E  74 3B                           je 0x140b7f25b
00B7F220  45 84 FF                        test r15b, r15b
00B7F223  74 36                           je 0x140b7f25b
00B7F225  48 83 FB FF                     cmp rbx, -1
00B7F229  74 30                           je 0x140b7f25b
00B7F22B  49 3B DA                        cmp rbx, r10
00B7F22E  76 2B                           jbe 0x140b7f25b
00B7F230  48 8B 8F 98 00 00 00            mov rcx, qword ptr [rdi + 0x98]
00B7F237  49 2B DA                        sub rbx, r10
00B7F23A  48 89 9F 38 01 00 00            mov qword ptr [rdi + 0x138], rbx
00B7F241  48 03 CB                        add rcx, rbx
00B7F244  48 89 8F B0 00 00 00            mov qword ptr [rdi + 0xb0], rcx
00B7F24B  48 C7 87 B8 00 00 00 FE FF FF FF  mov qword ptr [rdi + 0xb8], 0xfffffffffffffffe
00B7F256  E9 C6 00 00 00                  jmp 0x140b7f321
00B7F25B  4C 8B 0D 06 DC 38 00            mov r9, qword ptr [rip + 0x38dc06]
00B7F262  45 39 61 58                     cmp dword ptr [r9 + 0x58], r12d
00B7F266  74 52                           je 0x140b7f2ba
00B7F268  83 3D FD CA 38 00 05            cmp dword ptr [rip + 0x38cafd], 5
00B7F26F  74 49                           je 0x140b7f2ba
00B7F271  48 8D 0D 48 DC 38 00            lea rcx, [rip + 0x38dc48]
00B7F278  E8 43 4B F2 FF                  call 0x140aa3dc0
00B7F27D  84 C0                           test al, al
00B7F27F  74 39                           je 0x140b7f2ba
00B7F281  F7 05 C1 CA 38 00 00 00 00 40   test dword ptr [rip + 0x38cac1], 0x40000000
00B7F28B  75 2D                           jne 0x140b7f2ba
00B7F28D  48 8B 97 98 00 00 00            mov rdx, qword ptr [rdi + 0x98]
00B7F294  48 89 97 B0 00 00 00            mov qword ptr [rdi + 0xb0], rdx
00B7F29B  41 8B 41 58                     mov eax, dword ptr [r9 + 0x58]
00B7F29F  48 69 C8 80 96 98 00            imul rcx, rax, 0x989680
00B7F2A6  48 03 CA                        add rcx, rdx
00B7F2A9  48 83 8F B8 00 00 00 FF         or qword ptr [rdi + 0xb8], 0xffffffffffffffff
00B7F2B1  48 89 8F B0 00 00 00            mov qword ptr [rdi + 0xb0], rcx
00B7F2B8  EB 67                           jmp 0x140b7f321
00B7F2BA  45 84 DB                        test r11b, r11b
00B7F2BD  74 62                           je 0x140b7f321
00B7F2BF  83 3D A6 CA 38 00 05            cmp dword ptr [rip + 0x38caa6], 5
00B7F2C6  75 59                           jne 0x140b7f321
00B7F2C8  44 38 25 91 CC 38 00            cmp byte ptr [rip + 0x38cc91], r12b
00B7F2CF  75 50                           jne 0x140b7f321
00B7F2D1  48 8B 15 A0 C9 38 00            mov rdx, qword ptr [rip + 0x38c9a0]
00B7F2D8  48 85 D2                        test rdx, rdx
00B7F2DB  74 44                           je 0x140b7f321
00B7F2DD  83 3D 70 CA 38 00 0B            cmp dword ptr [rip + 0x38ca70], 0xb
00B7F2E4  75 3B                           jne 0x140b7f321
00B7F2E6  49 2B D2                        sub rdx, r10
00B7F2E9  48 89 97 38 01 00 00            mov qword ptr [rdi + 0x138], rdx
00B7F2F0  8B 05 82 5F 44 00               mov eax, dword ptr [rip + 0x445f82]
00B7F2F6  48 69 C8 80 69 67 FF            imul rcx, rax, -0x989680
00B7F2FD  48 03 D1                        add rdx, rcx
00B7F300  48 8B 8F 98 00 00 00            mov rcx, qword ptr [rdi + 0x98]
00B7F307  48 03 CA                        add rcx, rdx
00B7F30A  48 89 97 38 01 00 00            mov qword ptr [rdi + 0x138], rdx
00B7F311  E9 2E FF FF FF                  jmp 0x140b7f244
00B7F316  48 C7 87 B8 00 00 00 FD FF FF FF  mov qword ptr [rdi + 0xb8], 0xfffffffffffffffd
00B7F321  48 83 BF B8 00 00 00 FF         cmp qword ptr [rdi + 0xb8], -1
00B7F329  75 17                           jne 0x140b7f342
00B7F32B  4C 39 25 DE CA 38 00            cmp qword ptr [rip + 0x38cade], r12
00B7F332  75 0E                           jne 0x140b7f342
00B7F334  48 8B 87 98 00 00 00            mov rax, qword ptr [rdi + 0x98]
00B7F33B  48 89 05 CE CA 38 00            mov qword ptr [rip + 0x38cace], rax
00B7F342  33 D2                           xor edx, edx
00B7F344  48 8D 1D 6D CA 38 00            lea rbx, [rip + 0x38ca6d]
00B7F34B  48 8B CB                        mov rcx, rbx
00B7F34E  44 8D 42 48                     lea r8d, [rdx + 0x48]
00B7F352  E8 E9 78 B4 FF                  call 0x1406c6c40
00B7F357  C7 05 4F CA 38 00 03 00 00 00   mov dword ptr [rip + 0x38ca4f], 3
00B7F361  48 83 BF B8 00 00 00 FD         cmp qword ptr [rdi + 0xb8], -3
00B7F369  75 33                           jne 0x140b7f39e
00B7F36B  48 C7 05 52 CA 38 00 FD FF FF FF  mov qword ptr [rip + 0x38ca52], 0xfffffffffffffffd
00B7F376  48 89 35 3B CA 38 00            mov qword ptr [rip + 0x38ca3b], rsi
00B7F37D  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
00B7F384  48 89 05 55 CA 38 00            mov qword ptr [rip + 0x38ca55], rax
00B7F38B  48 8B 05 0E D5 38 00            mov rax, qword ptr [rip + 0x38d50e]
00B7F392  48 89 05 37 CA 38 00            mov qword ptr [rip + 0x38ca37], rax
00B7F399  E9 09 02 00 00                  jmp 0x140b7f5a7
00B7F39E  44 38 25 BB CB 38 00            cmp byte ptr [rip + 0x38cbbb], r12b
00B7F3A5  0F 85 FC 01 00 00               jne 0x140b7f5a7
00B7F3AB  83 3D A2 C9 38 00 0E            cmp dword ptr [rip + 0x38c9a2], 0xe
00B7F3B2  0F 84 EF 01 00 00               je 0x140b7f5a7
00B7F3B8  83 3D AD C9 38 00 05            cmp dword ptr [rip + 0x38c9ad], 5
00B7F3BF  48 8D B7 48 01 00 00            lea rsi, [rdi + 0x148]
00B7F3C6  4C 8D A7 4C 01 00 00            lea r12, [rdi + 0x14c]
00B7F3CD  75 40                           jne 0x140b7f40f
00B7F3CF  83 3E 01                        cmp dword ptr [rsi], 1
00B7F3D2  74 3B                           je 0x140b7f40f
00B7F3D4  41 83 3C 24 01                  cmp dword ptr [r12], 1
00B7F3D9  74 34                           je 0x140b7f40f
00B7F3DB  4C 8D B7 C4 00 00 00            lea r14, [rdi + 0xc4]
00B7F3E2  4C 8D BF C0 00 00 00            lea r15, [rdi + 0xc0]
00B7F3E9  4D 8B C6                        mov r8, r14
00B7F3EC  49 8B D7                        mov rdx, r15
00B7F3EF  48 8D 0D 22 55 4A FF            lea rcx, [rip - 0xb5aade]
00B7F3F6  E8 CD D8 F4 FF                  call 0x140acccc8
00B7F3FB  41 83 3F 00                     cmp dword ptr [r15], 0
00B7F3FF  75 06                           jne 0x140b7f407
00B7F401  41 83 3E 00                     cmp dword ptr [r14], 0
00B7F405  74 08                           je 0x140b7f40f
00B7F407  83 26 00                        and dword ptr [rsi], 0
00B7F40A  41 83 24 24 00                  and dword ptr [r12], 0
00B7F40F  48 8B 87 B0 00 00 00            mov rax, qword ptr [rdi + 0xb0]
00B7F416  48 85 C0                        test rax, rax
00B7F419  0F 84 84 00 00 00               je 0x140b7f4a3
00B7F41F  48 83 BF B8 00 00 00 FE         cmp qword ptr [rdi + 0xb8], -2
00B7F427  75 3F                           jne 0x140b7f468
00B7F429  83 3E 00                        cmp dword ptr [rsi], 0
00B7F42C  74 15                           je 0x140b7f443
00B7F42E  48 89 05 83 C9 38 00            mov qword ptr [rip + 0x38c983], rax
00B7F435  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
00B7F43C  48 89 05 85 C9 38 00            mov qword ptr [rip + 0x38c985], rax
00B7F443  41 83 3C 24 00                  cmp dword ptr [r12], 0
00B7F448  74 59                           je 0x140b7f4a3
00B7F44A  48 8B 87 B0 00 00 00            mov rax, qword ptr [rdi + 0xb0]
00B7F451  48 89 05 78 C9 38 00            mov qword ptr [rip + 0x38c978], rax
00B7F458  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
00B7F45F  48 89 05 7A C9 38 00            mov qword ptr [rip + 0x38c97a], rax
00B7F466  EB 3B                           jmp 0x140b7f4a3
00B7F468  48 8D 0D 79 C9 38 00            lea rcx, [rip + 0x38c979]
00B7F46F  48 8B 87 B0 00 00 00            mov rax, qword ptr [rdi + 0xb0]
00B7F476  48 89 03                        mov qword ptr [rbx], rax
00B7F479  48 83 C3 18                     add rbx, 0x18
00B7F47D  48 3B D9                        cmp rbx, rcx
00B7F480  7C ED                           jl 0x140b7f46f
00B7F482  48 8D 0D 3F C9 38 00            lea rcx, [rip + 0x38c93f]
00B7F489  48 8D 15 68 C9 38 00            lea rdx, [rip + 0x38c968]
00B7F490  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
00B7F497  48 89 01                        mov qword ptr [rcx], rax
00B7F49A  48 83 C1 18                     add rcx, 0x18
00B7F49E  48 3B CA                        cmp rcx, rdx
00B7F4A1  7C ED                           jl 0x140b7f490
00B7F4A3  48 8B 0D 5E C9 38 00            mov rcx, qword ptr [rip + 0x38c95e]
00B7F4AA  48 89 4F 40                     mov qword ptr [rdi + 0x40], rcx
00B7F4AE  48 8B D1                        mov rdx, rcx
00B7F4B1  48 85 C9                        test rcx, rcx
00B7F4B4  74 19                           je 0x140b7f4cf
00B7F4B6  48 8B 87 98 00 00 00            mov rax, qword ptr [rdi + 0x98]
00B7F4BD  48 05 00 2D 31 01               add rax, 0x1312d00
00B7F4C3  48 3B C8                        cmp rcx, rax
00B7F4C6  73 07                           jae 0x140b7f4cf
00B7F4C8  48 89 47 40                     mov qword ptr [rdi + 0x40], rax
00B7F4CC  48 8B D0                        mov rdx, rax
00B7F4CF  8B 06                           mov eax, dword ptr [rsi]
00B7F4D1  41 BE 02 00 00 00               mov r14d, 2
00B7F4D7  85 C0                           test eax, eax
00B7F4D9  74 61                           je 0x140b7f53c
00B7F4DB  41 3B C6                        cmp eax, r14d
00B7F4DE  75 0F                           jne 0x140b7f4ef
00B7F4E0  8B 05 26 DA 38 00               mov eax, dword ptr [rip + 0x38da26]
00B7F4E6  85 C0                           test eax, eax
00B7F4E8  78 05                           js 0x140b7f4ef
00B7F4EA  41 B0 01                        mov r8b, 1
00B7F4ED  EB 03                           jmp 0x140b7f4f2
00B7F4EF  45 32 C0                        xor r8b, r8b
00B7F4F2  44 88 87 A9 00 00 00            mov byte ptr [rdi + 0xa9], r8b
00B7F4F9  48 8D 4A 01                     lea rcx, [rdx + 1]
00B7F4FD  48 8B 97 B0 00 00 00            mov rdx, qword ptr [rdi + 0xb0]
00B7F504  48 8D 5F 28                     lea rbx, [rdi + 0x28]
00B7F508  48 8D B7 C8 00 00 00            lea rsi, [rdi + 0xc8]
00B7F50F  4C 8B CB                        mov r9, rbx
00B7F512  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00B7F517  E8 FC EA FF FF                  call 0x140b7e018
00B7F51C  88 87 50 01 00 00               mov byte ptr [rdi + 0x150], al
00B7F522  84 C0                           test al, al
00B7F524  74 21                           je 0x140b7f547
00B7F526  48 8B 03                        mov rax, qword ptr [rbx]
00B7F529  48 89 05 88 C8 38 00            mov qword ptr [rip + 0x38c888], rax
00B7F530  48 8B 06                        mov rax, qword ptr [rsi]
00B7F533  48 89 05 8E C8 38 00            mov qword ptr [rip + 0x38c88e], rax
00B7F53A  EB 0B                           jmp 0x140b7f547
00B7F53C  48 8D 5F 28                     lea rbx, [rdi + 0x28]
00B7F540  48 8D B7 C8 00 00 00            lea rsi, [rdi + 0xc8]
00B7F547  41 8B 04 24                     mov eax, dword ptr [r12]
00B7F54B  45 33 E4                        xor r12d, r12d
00B7F54E  85 C0                           test eax, eax
00B7F550  74 55                           je 0x140b7f5a7
00B7F552  41 3B C6                        cmp eax, r14d
00B7F555  75 0D                           jne 0x140b7f564
00B7F557  8B 05 AF D9 38 00               mov eax, dword ptr [rip + 0x38d9af]
00B7F55D  41 B0 01                        mov r8b, 1
00B7F560  85 C0                           test eax, eax
00B7F562  79 03                           jns 0x140b7f567
00B7F564  45 8A C4                        mov r8b, r12b
00B7F567  44 88 87 A9 00 00 00            mov byte ptr [rdi + 0xa9], r8b
00B7F56E  4C 8B CB                        mov r9, rbx
00B7F571  48 8B 4F 40                     mov rcx, qword ptr [rdi + 0x40]
00B7F575  48 8B 97 B0 00 00 00            mov rdx, qword ptr [rdi + 0xb0]
00B7F57C  48 FF C1                        inc rcx
00B7F57F  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00B7F584  E8 8F EA FF FF                  call 0x140b7e018
00B7F589  88 87 50 01 00 00               mov byte ptr [rdi + 0x150], al
00B7F58F  84 C0                           test al, al
00B7F591  74 14                           je 0x140b7f5a7
00B7F593  48 8B 03                        mov rax, qword ptr [rbx]
00B7F596  48 89 05 33 C8 38 00            mov qword ptr [rip + 0x38c833], rax
00B7F59D  48 8B 06                        mov rax, qword ptr [rsi]
00B7F5A0  48 89 05 39 C8 38 00            mov qword ptr [rip + 0x38c839], rax
00B7F5A7  48 8B 15 0A C8 38 00            mov rdx, qword ptr [rip + 0x38c80a]
00B7F5AE  48 89 15 0B C8 38 00            mov qword ptr [rip + 0x38c80b], rdx
00B7F5B5  48 85 D2                        test rdx, rdx
00B7F5B8  74 1A                           je 0x140b7f5d4
00B7F5BA  44 8B 87 54 01 00 00            mov r8d, dword ptr [rdi + 0x154]
00B7F5C1  4C 03 87 98 00 00 00            add r8, qword ptr [rdi + 0x98]
00B7F5C8  49 3B D0                        cmp rdx, r8
00B7F5CB  73 07                           jae 0x140b7f5d4
00B7F5CD  4C 89 05 EC C7 38 00            mov qword ptr [rip + 0x38c7ec], r8
00B7F5D4  48 8B 15 F5 C7 38 00            mov rdx, qword ptr [rip + 0x38c7f5]
00B7F5DB  48 89 15 F6 C7 38 00            mov qword ptr [rip + 0x38c7f6], rdx
00B7F5E2  48 85 D2                        test rdx, rdx
00B7F5E5  74 1A                           je 0x140b7f601
00B7F5E7  44 8B 87 54 01 00 00            mov r8d, dword ptr [rdi + 0x154]
00B7F5EE  4C 03 87 98 00 00 00            add r8, qword ptr [rdi + 0x98]
00B7F5F5  49 3B D0                        cmp rdx, r8
00B7F5F8  73 07                           jae 0x140b7f601
00B7F5FA  4C 89 05 D7 C7 38 00            mov qword ptr [rip + 0x38c7d7], r8
00B7F601  48 8B 0D C0 C7 38 00            mov rcx, qword ptr [rip + 0x38c7c0]
00B7F608  E8 67 63 B8 FF                  call 0x140705974
00B7F60D  89 87 40 01 00 00               mov dword ptr [rdi + 0x140], eax
00B7F613  48 8B 0D C6 C7 38 00            mov rcx, qword ptr [rip + 0x38c7c6]
00B7F61A  E8 55 63 B8 FF                  call 0x140705974
00B7F61F  33 C9                           xor ecx, ecx
00B7F621  89 87 44 01 00 00               mov dword ptr [rdi + 0x144], eax
00B7F627  E8 B4 F1 7F FF                  call 0x14037e7e0
00B7F62C  48 89 05 DD CC 38 00            mov qword ptr [rip + 0x38ccdd], rax
00B7F633  E8 D8 61 E4 FF                  call 0x1409c5810
00B7F638  BA 01 00 00 00                  mov edx, 1
00B7F63D  8A CA                           mov cl, dl
00B7F63F  E8 54 C7 FF FF                  call 0x140b7bd98
00B7F644  E8 2B 62 E4 FF                  call 0x1409c5874
00B7F649  48 8B 05 D0 11 28 00            mov rax, qword ptr [rip + 0x2811d0]
00B7F650  48 8B 15 81 C7 38 00            mov rdx, qword ptr [rip + 0x38c781]
00B7F657  48 8B 0D 62 C7 38 00            mov rcx, qword ptr [rip + 0x38c762]
00B7F65E  E8 6D B4 B3 FF                  call 0x1406baad0
00B7F663  44 88 25 0E BF 28 00            mov byte ptr [rip + 0x28bf0e], r12b
00B7F66A  E8 95 9A 91 FF                  call 0x140499104
00B7F66F  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
00B7F673  48 8D 55 7F                     lea rdx, [rbp + 0x7f]
00B7F677  E8 24 34 D2 FF                  call 0x1408a2aa0
00B7F67C  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00B7F680  48 8D 55 97                     lea rdx, [rbp - 0x69]
00B7F684  E8 77 8C CE FF                  call 0x140868300
00B7F689  E8 82 6A FF FF                  call 0x140b76110
00B7F68E  C6 47 60 01                     mov byte ptr [rdi + 0x60], 1
00B7F692  E8 89 DB FF FF                  call 0x140b7d220
00B7F697  48 A1 08 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000008]
00B7F6A1  45 33 C9                        xor r9d, r9d
00B7F6A4  48 8B 55 97                     mov rdx, qword ptr [rbp - 0x69]
00B7F6A8  45 33 C0                        xor r8d, r8d
00B7F6AB  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
00B7F6AF  48 89 87 30 01 00 00            mov qword ptr [rdi + 0x130], rax
00B7F6B6  8B 05 50 D7 38 00               mov eax, dword ptr [rip + 0x38d750]
00B7F6BC  89 47 70                        mov dword ptr [rdi + 0x70], eax
00B7F6BF  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00B7F6C4  E8 3B 13 8B FF                  call 0x140430a04
00B7F6C9  48 8D 8F F8 00 00 00            lea rcx, [rdi + 0xf8]
00B7F6D0  41 B0 01                        mov r8b, 1
00B7F6D3  33 D2                           xor edx, edx
00B7F6D5  8B D8                           mov ebx, eax
00B7F6D7  E8 34 FC 7B FF                  call 0x14033f310
00B7F6DC  48 8D 8F 10 01 00 00            lea rcx, [rdi + 0x110]
00B7F6E3  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00B7F6E8  45 33 C9                        xor r9d, r9d
00B7F6EB  45 33 C0                        xor r8d, r8d
00B7F6EE  33 D2                           xor edx, edx
00B7F6F0  E8 BB EF 68 FF                  call 0x14020e6b0
00B7F6F5  85 DB                           test ebx, ebx
00B7F6F7  78 05                           js 0x140b7f6fe
00B7F6F9  E8 D6 9E FF FF                  call 0x140b795d4
00B7F6FE  4C 89 25 FB C8 38 00            mov qword ptr [rip + 0x38c8fb], r12
00B7F705  BE 02 00 00 00                  mov esi, 2
00B7F70A  8B 87 2C 01 00 00               mov eax, dword ptr [rdi + 0x12c]
00B7F710  8B CE                           mov ecx, esi
00B7F712  89 47 58                        mov dword ptr [rdi + 0x58], eax
00B7F715  E8 9E 8F 94 FF                  call 0x1404c86b8
00B7F71A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B7F723  44 38 25 56 CF 38 00            cmp byte ptr [rip + 0x38cf56], r12b
00B7F72A  8B 15 3C C6 38 00               mov edx, dword ptr [rip + 0x38c63c]
00B7F730  8B CA                           mov ecx, edx
00B7F732  0F 45 0D 3B C6 38 00            cmovne ecx, dword ptr [rip + 0x38c63b]
00B7F739  89 0D 39 C6 38 00               mov dword ptr [rip + 0x38c639], ecx
00B7F73F  48 89 05 52 81 2E 00            mov qword ptr [rip + 0x2e8152], rax
00B7F746  8B 47 08                        mov eax, dword ptr [rdi + 8]
00B7F749  A8 08                           test al, 8
00B7F74B  74 06                           je 0x140b7f753
00B7F74D  44 89 6F 20                     mov dword ptr [rdi + 0x20], r13d
00B7F751  EB 0A                           jmp 0x140b7f75d
00B7F753  89 57 20                        mov dword ptr [rdi + 0x20], edx
00B7F756  44 8B 2D 0F C6 38 00            mov r13d, dword ptr [rip + 0x38c60f]
00B7F75D  8B 87 44 01 00 00               mov eax, dword ptr [rdi + 0x144]
00B7F763  41 8B CD                        mov ecx, r13d
00B7F766  44 8B 05 0B C6 38 00            mov r8d, dword ptr [rip + 0x38c60b]
00B7F76D  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00B7F771  8B 87 40 01 00 00               mov eax, dword ptr [rdi + 0x140]
00B7F777  44 89 47 1C                     mov dword ptr [rdi + 0x1c], r8d
00B7F77B  4C 8B 0D 3E C6 38 00            mov r9, qword ptr [rip + 0x38c63e]
00B7F782  8B 15 EC C5 38 00               mov edx, dword ptr [rip + 0x38c5ec]
00B7F788  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00B7F78C  48 8B 05 45 C6 38 00            mov rax, qword ptr [rip + 0x38c645]
00B7F793  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B7F798  E8 9F E4 FF FF                  call 0x140b7dc3c
00B7F79D  44 38 25 68 17 39 00            cmp byte ptr [rip + 0x391768], r12b
00B7F7A4  74 05                           je 0x140b7f7ab
00B7F7A6  E8 99 1C FF FF                  call 0x140b71444
00B7F7AB  44 8B 4F 58                     mov r9d, dword ptr [rdi + 0x58]
00B7F7AF  45 85 C9                        test r9d, r9d
00B7F7B2  0F 89 BC F6 FF FF               jns 0x140b7ee74
00B7F7B8  83 3D AD C5 38 00 05            cmp dword ptr [rip + 0x38c5ad], 5
00B7F7BF  0F 85 AF F6 FF FF               jne 0x140b7ee74
00B7F7C5  0F 57 C0                        xorps xmm0, xmm0
00B7F7C8  4C 8D 05 81 07 00 00            lea r8, [rip + 0x781]
00B7F7CF  BA 80 00 00 00                  mov edx, 0x80
00B7F7D4  48 8D 0D 25 C0 38 00            lea rcx, [rip + 0x38c025]
00B7F7DB  0F 11 45 D7                     movups xmmword ptr [rbp - 0x29], xmm0
00B7F7DF  E8 EC C2 8F FF                  call 0x14047bad0
00B7F7E4  48 8D 15 15 C0 38 00            lea rdx, [rip + 0x38c015]
00B7F7EB  48 8D 4D D7                     lea rcx, [rbp - 0x29]
00B7F7EF  E8 8C AF 8A FF                  call 0x14042a780
00B7F7F4  45 33 C0                        xor r8d, r8d
00B7F7F7  48 8D 55 D7                     lea rdx, [rbp - 0x29]
00B7F7FB  B9 11 04 00 C0                  mov ecx, 0xc0000411
00B7F800  E8 AB 8A 93 FF                  call 0x1404b82b0
00B7F805  8B 4F 58                        mov ecx, dword ptr [rdi + 0x58]
00B7F808  E8 A7 1B FF FF                  call 0x140b713b4
00B7F80D  E9 62 F6 FF FF                  jmp 0x140b7ee74
00B7F812  45 33 E4                        xor r12d, r12d
00B7F815  45 89 2E                        mov dword ptr [r14], r13d
00B7F818  44 89 67 58                     mov dword ptr [rdi + 0x58], r12d
00B7F81C  E9 4E F6 FF FF                  jmp 0x140b7ee6f
00B7F821  C6 05 50 BD 28 00 01            mov byte ptr [rip + 0x28bd50], 1
00B7F828  B9 38 00 00 00                  mov ecx, 0x38
00B7F82D  E8 5E 84 FF FF                  call 0x140b77c90
00B7F832  48 8B 05 E7 0F 28 00            mov rax, qword ptr [rip + 0x280fe7]
00B7F839  33 D2                           xor edx, edx
00B7F83B  33 C9                           xor ecx, ecx
00B7F83D  E8 8E B2 B3 FF                  call 0x1406baad0
00B7F842  44 8B 4F 08                     mov r9d, dword ptr [rdi + 8]
00B7F846  44 8B 05 27 C5 38 00            mov r8d, dword ptr [rip + 0x38c527]
00B7F84D  8B 15 19 C5 38 00               mov edx, dword ptr [rip + 0x38c519]
00B7F853  8B 0D EB C4 38 00               mov ecx, dword ptr [rip + 0x38c4eb]
00B7F859  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
00B7F85E  E8 51 44 F4 FF                  call 0x140ac3cb4
00B7F863  89 47 64                        mov dword ptr [rdi + 0x64], eax
00B7F866  E8 CD 4A F5 FF                  call 0x140ad4338
00B7F86B  45 33 C9                        xor r9d, r9d
00B7F86E  48 8D 15 7B 0C 95 FF            lea rdx, [rip - 0x6af385]
00B7F875  45 33 C0                        xor r8d, r8d
00B7F878  48 8D 0D A1 78 44 00            lea rcx, [rip + 0x4478a1]
00B7F87F  E8 B0 DF 75 FF                  call 0x1402dd834
00B7F884  44 38 67 30                     cmp byte ptr [rdi + 0x30], r12b
00B7F888  74 09                           je 0x140b7f893
00B7F88A  E8 81 8B FF FF                  call 0x140b78410
00B7F88F  44 88 67 30                     mov byte ptr [rdi + 0x30], r12b
00B7F893  44 38 67 60                     cmp byte ptr [rdi + 0x60], r12b
00B7F897  74 05                           je 0x140b7f89e
00B7F899  E8 96 CC FE FF                  call 0x140b6c534
00B7F89E  E8 45 44 F2 FF                  call 0x140aa3ce8
00B7F8A3  4C 89 25 DE C4 38 00            mov qword ptr [rip + 0x38c4de], r12
00B7F8AA  E8 65 B1 95 FF                  call 0x1404daa14
00B7F8AF  E8 3C 62 F4 FF                  call 0x140ac5af0
00B7F8B4  8B 05 52 D5 38 00               mov eax, dword ptr [rip + 0x38d552]
00B7F8BA  48 8D 0D 3F BE 38 00            lea rcx, [rip + 0x38be3f]
00B7F8C1  89 47 74                        mov dword ptr [rdi + 0x74], eax
00B7F8C4  BA 01 00 00 00                  mov edx, 1
00B7F8C9  48 8D 05 D0 09 BE FF            lea rax, [rip - 0x41f630]
00B7F8D0  4C 89 25 41 BE 38 00            mov qword ptr [rip + 0x38be41], r12
00B7F8D7  48 89 05 32 BE 38 00            mov qword ptr [rip + 0x38be32], rax
00B7F8DE  4C 89 25 1B BE 38 00            mov qword ptr [rip + 0x38be1b], r12
00B7F8E5  E8 36 9C 77 FF                  call 0x1402f9520
00B7F8EA  44 39 67 58                     cmp dword ptr [rdi + 0x58], r12d
00B7F8EE  7C 09                           jl 0x140b7f8f9
00B7F8F0  48 8D 4F 78                     lea rcx, [rdi + 0x78]
00B7F8F4  E8 DF 5D EB FF                  call 0x140a356d8
00B7F8F9  44 38 67 60                     cmp byte ptr [rdi + 0x60], r12b
00B7F8FD  74 05                           je 0x140b7f904
00B7F8FF  E8 60 C9 FE FF                  call 0x140b6c264
00B7F904  44 39 67 58                     cmp dword ptr [rdi + 0x58], r12d
00B7F908  7C 63                           jl 0x140b7f96d
00B7F90A  4C 8D 4D 77                     lea r9, [rbp + 0x77]
00B7F90E  4C 8D 45 A7                     lea r8, [rbp - 0x59]
00B7F912  48 8D 55 AF                     lea rdx, [rbp - 0x51]
00B7F916  48 8D 4D 6F                     lea rcx, [rbp + 0x6f]
00B7F91A  E8 5D 4A F3 FF                  call 0x140ab437c
00B7F91F  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
00B7F922  44 8B 8F 44 01 00 00            mov r9d, dword ptr [rdi + 0x144]
00B7F929  44 8B 87 40 01 00 00            mov r8d, dword ptr [rdi + 0x140]
00B7F930  48 8B 15 A1 C4 38 00            mov rdx, qword ptr [rip + 0x38c4a1]
00B7F937  48 8B 0D 82 C4 38 00            mov rcx, qword ptr [rip + 0x38c482]
00B7F93E  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00B7F942  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
00B7F946  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B7F94B  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
00B7F94F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B7F954  8B 87 80 00 00 00               mov eax, dword ptr [rdi + 0x80]
00B7F95A  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00B7F95E  8B 87 84 00 00 00               mov eax, dword ptr [rdi + 0x84]
00B7F964  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00B7F968  E8 E7 76 F0 FF                  call 0x140a87054
00B7F96D  44 38 67 30                     cmp byte ptr [rdi + 0x30], r12b
00B7F971  75 09                           jne 0x140b7f97c
00B7F973  E8 48 8A FF FF                  call 0x140b783c0
00B7F978  C6 47 30 01                     mov byte ptr [rdi + 0x30], 1
00B7F97C  44 39 67 58                     cmp dword ptr [rdi + 0x58], r12d
00B7F980  0F 8C 59 01 00 00               jl 0x140b7fadf
00B7F986  B9 01 00 00 00                  mov ecx, 1
00B7F98B  E8 24 22 D9 FF                  call 0x140911bb4
00B7F990  8B 4F 1C                        mov ecx, dword ptr [rdi + 0x1c]
00B7F993  E8 14 54 BE FF                  call 0x140764dac
00B7F998  48 63 0D 11 C4 38 00            movsxd rcx, dword ptr [rip + 0x38c411]
00B7F99F  41 8A D4                        mov dl, r12b
00B7F9A2  88 15 98 C3 38 00               mov byte ptr [rip + 0x38c398], dl
00B7F9A8  48 83 F9 03                     cmp rcx, 3
00B7F9AC  0F 83 0F 01 00 00               jae 0x140b7fac1
00B7F9B2  48 8D 04 49                     lea rax, [rcx + rcx*2]
00B7F9B6  4C 8D 05 43 06 48 FF            lea r8, [rip - 0xb7f9bd]
00B7F9BD  49 8B 84 C0 C0 BD F0 00         mov rax, qword ptr [r8 + rax*8 + 0xf0bdc0]
00B7F9C5  48 8D 0C 49                     lea rcx, [rcx + rcx*2]
00B7F9C9  48 89 05 38 C4 38 00            mov qword ptr [rip + 0x38c438], rax
00B7F9D0  49 8B 84 C8 C8 BD F0 00         mov rax, qword ptr [r8 + rcx*8 + 0xf0bdc8]
00B7F9D8  44 89 25 09 D3 38 00            mov dword ptr [rip + 0x38d309], r12d
00B7F9DF  44 89 25 9E CC 38 00            mov dword ptr [rip + 0x38cc9e], r12d
00B7F9E6  44 89 25 9B CC 38 00            mov dword ptr [rip + 0x38cc9b], r12d
00B7F9ED  48 83 F8 FF                     cmp rax, -1
00B7F9F1  75 45                           jne 0x140b7fa38
00B7F9F3  8B 97 4C 01 00 00               mov edx, dword ptr [rdi + 0x14c]
00B7F9F9  4C 8D 47 78                     lea r8, [rdi + 0x78]
00B7F9FD  8B 8F 48 01 00 00               mov ecx, dword ptr [rdi + 0x148]
00B7FA03  E8 80 05 BE FF                  call 0x14075ff88
00B7FA08  84 C0                           test al, al
00B7FA0A  74 13                           je 0x140b7fa1f
00B7FA0C  8B 07                           mov eax, dword ptr [rdi]
00B7FA0E  89 05 30 C3 38 00               mov dword ptr [rip + 0x38c330], eax
00B7FA14  8B 47 04                        mov eax, dword ptr [rdi + 4]
00B7FA17  89 05 2B C3 38 00               mov dword ptr [rip + 0x38c32b], eax
00B7FA1D  EB 10                           jmp 0x140b7fa2f
00B7FA1F  89 35 1F C3 38 00               mov dword ptr [rip + 0x38c31f], esi
00B7FA25  C7 05 19 C3 38 00 05 00 00 00   mov dword ptr [rip + 0x38c319], 5
00B7FA2F  40 08 35 0A C3 38 00            or byte ptr [rip + 0x38c30a], sil
00B7FA36  EB 68                           jmp 0x140b7faa0
00B7FA38  48 83 F8 FE                     cmp rax, -2
00B7FA3C  75 20                           jne 0x140b7fa5e
00B7FA3E  4C 39 25 63 C3 38 00            cmp qword ptr [rip + 0x38c363], r12
00B7FA45  0F 85 94 00 00 00               jne 0x140b7fadf
00B7FA4B  48 8B 05 46 C3 38 00            mov rax, qword ptr [rip + 0x38c346]
00B7FA52  48 89 05 4F C3 38 00            mov qword ptr [rip + 0x38c34f], rax
00B7FA59  E9 81 00 00 00                  jmp 0x140b7fadf
00B7FA5E  48 83 F8 FD                     cmp rax, -3
00B7FA62  75 10                           jne 0x140b7fa74
00B7FA64  4C 89 25 3D CE 38 00            mov qword ptr [rip + 0x38ce3d], r12
00B7FA6B  4C 89 25 2E CE 38 00            mov qword ptr [rip + 0x38ce2e], r12
00B7FA72  EB 6B                           jmp 0x140b7fadf
00B7FA74  83 3D 91 D3 38 00 01            cmp dword ptr [rip + 0x38d391], 1
00B7FA7B  75 2C                           jne 0x140b7faa9
00B7FA7D  44 39 A7 4C 01 00 00            cmp dword ptr [rdi + 0x14c], r12d
00B7FA84  75 59                           jne 0x140b7fadf
00B7FA86  8B 07                           mov eax, dword ptr [rdi]
00B7FA88  40 0A D6                        or dl, sil
00B7FA8B  89 05 B3 C2 38 00               mov dword ptr [rip + 0x38c2b3], eax
00B7FA91  8B 47 04                        mov eax, dword ptr [rdi + 4]
00B7FA94  89 05 AE C2 38 00               mov dword ptr [rip + 0x38c2ae], eax
00B7FA9A  88 15 A0 C2 38 00               mov byte ptr [rip + 0x38c2a0], dl
00B7FAA0  44 88 A7 D8 00 00 00            mov byte ptr [rdi + 0xd8], r12b
00B7FAA7  EB 36                           jmp 0x140b7fadf
00B7FAA9  44 39 A7 4C 01 00 00            cmp dword ptr [rdi + 0x14c], r12d
00B7FAB0  75 2D                           jne 0x140b7fadf
00B7FAB2  8B 47 74                        mov eax, dword ptr [rdi + 0x74]
00B7FAB5  39 47 70                        cmp dword ptr [rdi + 0x70], eax
00B7FAB8  75 25                           jne 0x140b7fadf
00B7FABA  E8 C9 5F A5 FF                  call 0x1405d5a88
00B7FABF  EB 1E                           jmp 0x140b7fadf
00B7FAC1  E8 02 DC FF FF                  call 0x140b7d6c8
00B7FAC6  84 C0                           test al, al
00B7FAC8  75 15                           jne 0x140b7fadf
00B7FACA  44 89 25 17 D2 38 00            mov dword ptr [rip + 0x38d217], r12d
00B7FAD1  44 89 25 AC CB 38 00            mov dword ptr [rip + 0x38cbac], r12d
00B7FAD8  44 89 25 A9 CB 38 00            mov dword ptr [rip + 0x38cba9], r12d
00B7FADF  44 38 25 1A C3 38 00            cmp byte ptr [rip + 0x38c31a], r12b
00B7FAE6  74 1C                           je 0x140b7fb04
00B7FAE8  44 38 A7 D8 00 00 00            cmp byte ptr [rdi + 0xd8], r12b
00B7FAEF  74 13                           je 0x140b7fb04
00B7FAF1  E8 7A 97 AD FF                  call 0x140659270
00B7FAF6  44 88 25 03 C3 38 00            mov byte ptr [rip + 0x38c303], r12b
00B7FAFD  4C 89 25 04 C3 38 00            mov qword ptr [rip + 0x38c304], r12
00B7FB04  44 38 25 75 CB 38 00            cmp byte ptr [rip + 0x38cb75], r12b
00B7FB0B  74 05                           je 0x140b7fb12
00B7FB0D  E8 2A D1 BD FF                  call 0x14075cc3c
00B7FB12  44 88 25 47 C4 38 00            mov byte ptr [rip + 0x38c447], r12b
00B7FB19  E8 C2 5D B8 FF                  call 0x1407058e0
00B7FB1E  40 8A CE                        mov cl, sil
00B7FB21  E8 82 CD 93 FF                  call 0x1404bc8a8
00B7FB26  E8 E5 88 FF FF                  call 0x140b78410
00B7FB2B  8B 05 53 CB 38 00               mov eax, dword ptr [rip + 0x38cb53]
00B7FB31  85 C0                           test eax, eax
00B7FB33  74 0B                           je 0x140b7fb40
00B7FB35  8B 0D 4D CB 38 00               mov ecx, dword ptr [rip + 0x38cb4d]
00B7FB3B  E8 60 2E 90 FF                  call 0x1404829a0
00B7FB40  BA 01 00 00 00                  mov edx, 1
00B7FB45  48 8D 0D 94 BC 38 00            lea rcx, [rip + 0x38bc94]
00B7FB4C  E8 CF 99 77 FF                  call 0x1402f9520
00B7FB51  E8 56 31 90 FF                  call 0x140482cac
00B7FB56  44 39 67 58                     cmp dword ptr [rdi + 0x58], r12d
00B7FB5A  7C 05                           jl 0x140b7fb61
00B7FB5C  E8 43 B2 BD FF                  call 0x14075ada4
00B7FB61  33 C9                           xor ecx, ecx
00B7FB63  C7 05 E7 C1 38 00 11 00 00 00   mov dword ptr [rip + 0x38c1e7], 0x11
00B7FB6D  E8 6E EC 7F FF                  call 0x14037e7e0
00B7FB72  48 2B 05 F7 7B 38 00            sub rax, qword ptr [rip + 0x387bf7]
00B7FB79  48 89 05 30 C9 38 00            mov qword ptr [rip + 0x38c930], rax
00B7FB80  48 8B 8F C8 00 00 00            mov rcx, qword ptr [rdi + 0xc8]
00B7FB87  48 85 C9                        test rcx, rcx
00B7FB8A  74 0C                           je 0x140b7fb98
00B7FB8C  E8 C3 96 AD FF                  call 0x140659254
00B7FB91  4C 89 A7 C8 00 00 00            mov qword ptr [rdi + 0xc8], r12
00B7FB98  48 8B 75 7F                     mov rsi, qword ptr [rbp + 0x7f]
00B7FB9C  48 8B 5D 97                     mov rbx, qword ptr [rbp - 0x69]
00B7FBA0  4C 89 25 F1 7C 2E 00            mov qword ptr [rip + 0x2e7cf1], r12
00B7FBA7  48 85 F6                        test rsi, rsi
00B7FBAA  74 08                           je 0x140b7fbb4
00B7FBAC  48 8B CE                        mov rcx, rsi
00B7FBAF  E8 9C 97 77 FF                  call 0x1402f9350
00B7FBB4  48 85 DB                        test rbx, rbx
00B7FBB7  74 08                           je 0x140b7fbc1
00B7FBB9  48 8B CB                        mov rcx, rbx
00B7FBBC  E8 8F 97 77 FF                  call 0x1402f9350
00B7FBC1  8B 57 6C                        mov edx, dword ptr [rdi + 0x6c]
00B7FBC4  85 D2                           test edx, edx
00B7FBC6  74 08                           je 0x140b7fbd0
00B7FBC8  8B 4F 58                        mov ecx, dword ptr [rdi + 0x58]
00B7FBCB  E8 98 38 BE FF                  call 0x140763468
00B7FBD0  8B 47 58                        mov eax, dword ptr [rdi + 0x58]
00B7FBD3  48 81 C4 D8 00 00 00            add rsp, 0xd8
00B7FBDA  41 5F                           pop r15
00B7FBDC  41 5E                           pop r14
00B7FBDE  41 5D                           pop r13
00B7FBE0  41 5C                           pop r12
00B7FBE2  5F                              pop rdi
00B7FBE3  5E                              pop rsi
00B7FBE4  5B                              pop rbx
00B7FBE5  5D                              pop rbp
00B7FBE6  C3                              ret
00B7FBE7  CC                              int3
00B7FBE8  E8 07 62 97 FF                  call 0x1404f5df4
00B7FBED  48 8B 0D 94 C1 38 00            mov rcx, qword ptr [rip + 0x38c194]
00B7FBF4  48 83 C1 30                     add rcx, 0x30
00B7FBF8  E8 87 D3 FF FF                  call 0x140b7cf84
00B7FBFD  39 35 51 C1 38 00               cmp dword ptr [rip + 0x38c151], esi
00B7FC03  75 07                           jne 0x140b7fc0c
00B7FC05  C6 05 F2 6E 44 00 01            mov byte ptr [rip + 0x446ef2], 1
00B7FC0C  8B D6                           mov edx, esi
00B7FC0E  B9 08 00 00 00                  mov ecx, 8
00B7FC13  E8 D0 F7 F0 FF                  call 0x140a8f3e8
00B7FC18  E8 AB C2 FE FF                  call 0x140b6bec8
00B7FC1D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopTransitionSystemPowerStateEx(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_rsp = (v_rsp) - (216);
    v_stack_mA8 = 0x20000ULL;
    a1 = 0;
    v_stack_mA0 = v_rip + 5715;
    v_stack_p10 = 0;
    *(unsigned __int8 *)(a1 + 12) = 0;
    *(unsigned __int8 *)(a1 + 24) = 0;
    *(unsigned int *)(a1 + 28) = 0;
    *(unsigned __int64 *)(a1 + 64) = 0;
    *(unsigned __int64 *)(a1 + 40) = 0;
    v_r12 = 0;
    *(unsigned int *)(a1 + 100) = 0;
    *(unsigned int *)(a1 + 108) = 0;
    *(unsigned __int64 *)(a1 + 200) = 0;
    *(unsigned __int64 *)(a1 + 176) = 0;
    *(unsigned __int64 *)(a1 + 184) = 0;
    *(unsigned __int64 *)(a1 + 304) = 0;
    *(unsigned __int8 *)(a1 + 336) = 0;
    *(unsigned __int64 *)(a1 + 320) = 0;
    *(unsigned int *)(a1 + 332) = 0;
    v_stack_mB0 = v_stack_mA8;
    v_stack_p18 = 0;
    v_stack_p20 = 0;
    v_stack_mC8 = 0;
    v_stack_mC0 = 0;
    v_stack_mB8 = v_stack_mA8;
    *(unsigned int *)(a1 + 112) = (unsigned int)(a1 + 1);
    *(unsigned int *)(a1 + 116) = (unsigned int)(a1 + 1);
    *(unsigned __int8 *)(a1 + 216) = (unsigned __int8)(a1 + 1);
    *(unsigned int *)(a1 + 328) = (unsigned int)(a1 + 1);
    *(unsigned __int64 *)(a1 + 192) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3728760))) & (0x10000ULL));
    *(unsigned int *)(a1 + 88) = 0;
    result = (unsigned int)(-(result));
    v_stack_m98 = v_xmm0;
    a1 = (unsigned int)((a1) & (0xEE1E5D00ULL));
    a1 = (unsigned int)((a1) + (0x23C34600ULL));
    *(unsigned int *)(a1 + 340) = (unsigned int)(a1);
    result = PopTransitionCheckpoint(0 + 8, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    result = 0 + 2;
    if ((*(unsigned int *)(a1)) == ((unsigned int)(0 + 2))) {
        result = PnpSurpriseFailUnsafeDmaDevices(0 + 8, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    }
    if ((*(unsigned int *)(a1)) == 4) {
        result = PopReadShutdownPolicy(0 + 8, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    }
    result = PopAcquireTransitionLockAfterSleep(0 + 8, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    result = MmLockPagableSectionByHandle(*(unsigned __int64 *)(v_rip + 4489759), (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    result = PopRunMaximumIrpWorkers(*(unsigned __int64 *)(v_rip + 4489759), (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    *(unsigned __int64 *)(v_rip + 3722751) = 0;
    a1 = 0;
    *(unsigned __int64 *)(v_rip + 3722734) = v_rip - 26450;
    *(unsigned __int64 *)(v_rip + 3722711) = 0;
    result = CmSetLazyFlushState(a1, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    result = PopNotifyCallbacksPreSleep(a1, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    a1 = 0;
    result = ExSwapinWorkerThreads(a1, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    a1 = 0;
    if ((*(unsigned int *)(v_rip + 3724499)) == ((unsigned int)(a1 + 1))) { a1 = 2; }
    result = PoInitializeBroadcast(a1, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    *(unsigned int *)(a1 + 88) = (unsigned int)(result);
    if (!sign_flag) goto loc_00B7EA53;
    result = ExQueueWorkItem(v_rip + 3722654, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    *(unsigned int *)(a1 + 108) = 5;
    goto loc_00B7FBA7;
loc_00B7EA53:
    result = PopCheckPowerSourceAfterRtcWakeCancel(v_rip + 3722654, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    result = PopCurrentPowerStatePrecise(a1 + 120, v_stack_mC0, a3, a4);
    result = PopAcquirePolicyLock(a1 + 120, v_stack_mC0, a3, a4);
    *(unsigned __int8 *)(a1 + 48) = (unsigned __int8)(a1 + 1);
    result = PopFilterCapabilities(v_rip + 3728452, v_rip + 3724199, a3, a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 3723962)) == 0) goto loc_00B7EABB;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rip + 3723962))) == 2) goto loc_00B7EAC0;
    result = PopReleasePolicyLock(v_rip + 3728452, v_rip + 3724199, a3, a4);
    result = PoClearBroadcast(v_rip + 3728452, v_rip + 3724199, a3, a4);
    result = ExQueueWorkItem(v_rip + 3722557, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    *(unsigned int *)(a1 + 108) = 6;
    *(unsigned int *)(a1 + 88) = 0xC0000021ULL;
    goto loc_00B7FBA7;
loc_00B7EABB:
    result = PopResetActionDefaults(v_rip + 3722557, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
loc_00B7EAC0:
    result = PopSetPowerActionState(3, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    *(unsigned __int64 *)(v_rip + 3723955) = *(unsigned __int64 *)(v_rip + 3723778);
    result = PopIgnoreBatteryStatusChange(3, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    result = PopCheckResiliencyScenarios(3, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    result = PopEnforceResiliencyScenarios(a1 + 208, (unsigned int)((unsigned int)(a1 + 1)), a3, a4);
    a4 = 0;
    a3 = 0;
    result = PopExecuteOnTargetProcessors(v_rip + 4490785, v_rip - 6991381, a3, a4);
    if ((*(unsigned int *)(a1)) == 6) {
        *(unsigned int *)(v_rip + 3723822) = 6;
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)) - 4)) > 2) goto loc_00B7EB61;
    *(unsigned __int8 *)(v_rip + 3723769) = 1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) == 5) {
        *(unsigned __int8 *)(v_rip + 3723758) = 1;
    }
    if ((*(unsigned __int64 *)(v_rip + 3724262)) == 0) goto loc_00B7EB61;
    if ((*(unsigned __int64 *)(v_rip + 3724261)) == 0) goto loc_00B7EB61;
    result = MmZeroPageFileAtShutdown((unsigned int)(*(unsigned int *)(a1)), v_rip - 6991381, a3, a4);
    if ((unsigned int)(result) != 0) {
        a2 = *(unsigned __int64 *)(v_rip + 3724243);
        a1 = *(unsigned __int64 *)(v_rip + 3724228);
        result = PopZeroHiberFile(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(a1 + 72) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) - (2));
    if (((unsigned int)(result)) <= 1) {
        *(unsigned __int8 *)(v_rip + 3723675) = 1;
    }
    *(unsigned __int8 *)(a1 + 96) = 0;
    *(unsigned int *)(a1 + 88) = 0xC0000120ULL;
loc_00B7EB96:
    if ((*(unsigned __int8 *)(a1 + 48)) == 0) {
        result = PopAcquirePolicyLock(2, a2, a3, a4);
        a1 = 2;
        *(unsigned __int8 *)(a1 + 48) = 1;
    }
    if ((*(unsigned int *)(v_rip + 3723667)) == 0) goto loc_00B7F812;
    *(unsigned __int8 *)(a1 + 104) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 3723651));
    *(unsigned __int8 *)(v_rip + 3723641) = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 88)))) != 0xC0000120ULL) goto loc_00B7EC25;
    if (((*(unsigned __int8 *)(a1 + 104)) & ((unsigned __int8)(a1))) == 0) goto loc_00B7EBE8;
    if (sign_flag) goto loc_00B7EBE8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3723632)))) & (3)) != 0) goto loc_00B7EE4D;
loc_00B7EBE8:
    result = PopActionRetrieveInitialState(v_rip + 3723596, a1 + 16, v_rip + 3723642, a1 + 72);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3723581))) + (-4));
    if (((unsigned int)(result)) <= 2) {
        *(unsigned __int8 *)(v_rip + 3723564) = 1;
        result = *(unsigned int *)(a1 + 8);
        *(unsigned int *)(v_rip + 3723565) = (unsigned int)(result);
    }
    goto loc_00B7EC2D;
loc_00B7EC25:
    if (sign_flag) goto loc_00B7EE6C;
loc_00B7EC2D:
    result = PopReleasePolicyLock(v_rip + 3723596, a1 + 16, v_rip + 3723642, a1 + 72);
    *(unsigned __int8 *)(a1 + 48) = 0;
    *(unsigned int *)(a1 + 328) = 1;
    result = PopQueryPowerSettingUlong(v_rip - 11904772, a1 + 328, a1 + 332, a1 + 72);
    result = 0;
    if (((*(unsigned int *)(v_rip + 3723502)) & (0x40000000ULL)) != 0) {
        *(unsigned int *)(a1 + 328) = 0;
        *(unsigned int *)(a1 + 332) = 0;
    }
    if ((*(unsigned __int8 *)(v_rip + 3723723)) != 0) goto loc_00B7EC7F;
    if ((*(unsigned __int8 *)(v_rip + 3723697)) != 0) goto loc_00B7EC7F;
    if ((*(unsigned __int8 *)(v_rip + 3723696)) == 0) {
        *(unsigned int *)(a1 + 332) = 0;
    }
    result = PopInitializePowerPolicySimulate(v_rip - 11904772, a1 + 328, a1 + 332, a1 + 72);
    *(unsigned int *)(v_rip + 3723475) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3723477)));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3723458))) >> (27));
    a2 = (unsigned int)((a2) & (2));
    *(unsigned int *)(a1 + 92) = (unsigned int)(a2);
    result = PopAdvanceSystemPowerState(v_rip + 3723487, a2, (unsigned int)(*(unsigned int *)(v_rip + 3723415)), (unsigned int)(*(unsigned int *)(a1 + 16)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 8)))) & (8)) == 0) goto loc_00B7ECDF;
    *(unsigned __int8 *)(v_rip + 3723932) = 1;
    *(unsigned __int8 *)(a1 + 24) = 0;
    *(unsigned int *)(v_rip + 3723426) = 5;
    *(unsigned int *)(a1 + 32) = 6;
    goto loc_00B7ED1C;
loc_00B7ECDF:
    result = PopFastS4Check(v_rip + 3723487, a2, (unsigned int)(*(unsigned int *)(v_rip + 3723415)), (unsigned int)(*(unsigned int *)(a1 + 16)));
    if ((unsigned __int8)(result) == 0) goto loc_00B7ED08;
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3723392)));
    *(unsigned int *)(v_rip + 3723382) = 5;
    *(unsigned __int8 *)(a1 + 24) = 1;
    *(unsigned int *)(a1 + 52) = 6;
    goto loc_00B7ED36;
loc_00B7ED08:
    *(unsigned int *)(v_rip + 3723366) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3723392)));
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3723392)));
    *(unsigned __int8 *)(a1 + 24) = 0;
loc_00B7ED1C:
    *(unsigned int *)(a1 + 52) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 12053795 + (int)(*(unsigned int *)(v_rip + 3723348)) * 4 + 169816)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 12053795 + (int)(*(unsigned int *)(v_rip + 3723348)) * 4 + 169816)))) > 6) goto loc_00B7EE29;
loc_00B7ED36:
    if ((*(unsigned __int64 *)(v_rip - 12053828 + (int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 12053795 + (int)(*(unsigned int *)(v_rip + 3723348)) * 4 + 169816)))) + (int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 12053795 + (int)(*(unsigned int *)(v_rip + 3723348)) * 4 + 169816)))) * 2 * 8 + 15780936)) == 0) goto loc_00B7EE29;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 8)))) & (8)) == 0) goto loc_00B7ED5F;
    goto loc_00B7ED6E;
loc_00B7ED5F:
    if ((*(unsigned __int8 *)(v_rip + 3723228)) != 0) goto loc_00B7ED75;
loc_00B7ED6E:
    result = PopSetSleepMarker((unsigned int)(*(unsigned int *)(v_rip + 3723262)), a2, (unsigned int)(*(unsigned int *)(v_rip + 3723415)), (unsigned int)(*(unsigned int *)(a1 + 16)));
    goto loc_00B7ED7F;
loc_00B7ED75:
    result = PopSetShutdownMarker((unsigned int)(*(unsigned int *)(v_rip + 3723262)), a2, (unsigned int)(*(unsigned int *)(v_rip + 3723415)), (unsigned int)(*(unsigned int *)(a1 + 16)));
    result = PopSaveLidReliabilityState((unsigned int)(*(unsigned int *)(v_rip + 3723262)), a2, (unsigned int)(*(unsigned int *)(v_rip + 3723415)), (unsigned int)(*(unsigned int *)(a1 + 16)));
loc_00B7ED7F:
    result = PopAcquirePolicyLock((unsigned int)(*(unsigned int *)(v_rip + 3723262)), a2, (unsigned int)(*(unsigned int *)(v_rip + 3723415)), (unsigned int)(*(unsigned int *)(a1 + 16)));
    if (((*(unsigned __int8 *)(v_rip + 3723189)) & (6)) == 0) goto loc_00B7ED9D;
    *(unsigned __int8 *)(a1 + 48) = 1;
    *(unsigned int *)(a1 + 88) = 0xC0000120ULL;
    goto loc_00B7EE43;
loc_00B7ED9D:
    result = PopReleasePolicyLock((unsigned int)(*(unsigned int *)(v_rip + 3723262)), a2, (unsigned int)(*(unsigned int *)(v_rip + 3723415)), (unsigned int)(*(unsigned int *)(a1 + 16)));
    result = PopCheckpointSystemSleep(10, a2, (unsigned int)(*(unsigned int *)(v_rip + 3723415)), (unsigned int)(*(unsigned int *)(a1 + 16)));
    *(unsigned __int8 *)(v_rip + 3723174) = 3;
    result = PopDiagTraceKernelQueriesAllowed(*(unsigned __int8 *)(a1 + 72), a2, (unsigned int)(*(unsigned int *)(v_rip + 3723415)), (unsigned int)(*(unsigned int *)(a1 + 16)));
    if ((*(unsigned __int8 *)(a1 + 72)) == 0) goto loc_00B7EE0B;
    result = PopSetDevicesSystemState(*(unsigned __int8 *)(a1 + 72), a2, (unsigned int)(*(unsigned int *)(v_rip + 3723415)), (unsigned int)(*(unsigned int *)(a1 + 16)));
    *(unsigned int *)(a1 + 88) = (unsigned int)(result);
    if (!sign_flag) goto loc_00B7EE07;
    if (((unsigned int)(result)) == 0xC0000120ULL) goto loc_00B7EE0B;
    result = PopFindNextSystemPowerState((unsigned int)(*(unsigned int *)(a1 + 16)), *(unsigned __int8 *)(a1 + 24), a1 + 72, (unsigned int)(*(unsigned int *)(a1 + 16)));
    *(unsigned __int8 *)(a1 + 36) = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_00B7EE65;
    goto loc_00B7EE3F;
loc_00B7EE07:
    *(unsigned __int8 *)(a1 + 96) = 1;
loc_00B7EE0B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 88)))) != 0xC0000120ULL) goto loc_00B7EFC6;
    goto loc_00B7EE43;
loc_00B7EE29:
    result = PopFindNextSystemPowerState((unsigned int)(*(unsigned int *)(a1 + 16)), *(unsigned __int8 *)(a1 + 24), a1 + 72, (unsigned int)(*(unsigned int *)(a1 + 16)));
    *(unsigned __int8 *)(a1 + 36) = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_00B7EE6C;
loc_00B7EE3F:
loc_00B7EE43:
    goto loc_00B7EB96;
loc_00B7EE4D:
    result = PopGetPolicyWorker(2, *(unsigned __int8 *)(a1 + 24), a1 + 72, (unsigned int)(*(unsigned int *)(a1 + 16)));
    v_r12 = 0;
    *(unsigned int *)(a1 + 108) = 8;
    goto loc_00B7EE74;
loc_00B7EE65:
    *(unsigned int *)(a1 + 108) = 9;
loc_00B7EE6C:
    v_r12 = 0;
loc_00B7EE6F:
loc_00B7EE74:
    if ((*(unsigned __int8 *)(a1 + 48)) != 0) {
        result = PopReleasePolicyLock(2, *(unsigned __int8 *)(a1 + 24), a1 + 72, (unsigned int)(*(unsigned int *)(a1 + 16)));
    }
    if ((*(unsigned __int8 *)(v_rip + 3723482)) != 0) {
        a1 = 0;
        result = KeQueryPerformanceCounter(a1, *(unsigned __int8 *)(a1 + 24), a1 + 72, (unsigned int)(*(unsigned int *)(a1 + 16)));
        a2 = v_rip + 3724938;
        *(unsigned __int64 *)(v_rip + 3724931) = result;
        a1 = v_rip + 3724916;
        result = PopQpcTimeInMs(a1, a2, a1 + 72, (unsigned int)(*(unsigned int *)(a1 + 16)));
        *(unsigned int *)(v_rip + 3723413) = (unsigned int)(result);
    }
    if ((*(unsigned int *)(a1 + 88)) < 0) goto loc_00B7EF28;
    *(unsigned __int64 *)(v_rip + 3722966) = *(unsigned __int64 *)(a1 + 304);
    result = ExUpdateSystemTimeFromCmos(1, 1, a1 + 72, (unsigned int)(*(unsigned int *)(a1 + 16)));
    a2 = 0;
    result = guard_dispatch_icall(1, a2, a1 + 72, (unsigned int)(*(unsigned int *)(a1 + 16)));
    if ((unsigned int)(result) != 0) {
        *(unsigned __int8 *)(a1 + 168) = 1;
    }
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a1 + 72, (unsigned int)(*(unsigned int *)(a1 + 16)));
    a3 = 0;
    *(unsigned __int64 *)(v_rip + 3724333) = result;
    a2 = 0;
    result = PfPowerActionNotify(2, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 16)));
    *(unsigned __int64 *)(v_rip + 3722880) = *(unsigned __int64 *)(result);
    result = PopDiagComputeEarlyHiberStats(2, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 16)));
    if ((*(unsigned int *)(a1 + 28)) == 4) {
        result = PopDiagTraceFirmwareS3Stats(2, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 16)));
    }
    *(unsigned __int8 *)(v_rip + 3722810) = 1;
    *(unsigned __int8 *)(v_rip + 3722730) = 0;
    *(unsigned __int8 *)(v_rip + 3722724) = 0;
    if ((*(unsigned __int8 *)(a1 + 96)) != 0) {
        a2 = 0;
        a3 = 0;
        a1 = a2 + 3;
        result = PfPowerActionNotify(a1, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 16)));
        result = PopSetDevicesSystemState(a1, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 16)));
        a3 = 0;
        a2 = a3 + 1;
        a1 = a2 + 2;
        result = PfPowerActionNotify(a1, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 16)));
    }
    if ((*(unsigned int *)(a1 + 88)) >= 0) {
        result = WheaResumedFromHibernate(a1, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 16)));
    }
    result = PpmCheckResumePpmEngineFromSx(a1, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 16)));
    result = PopCurrentPowerStatePrecise(a1 + 120, v_stack_mC0, a3, (unsigned int)(*(unsigned int *)(a1 + 16)));
    if ((*(unsigned __int8 *)(a1 + 168)) != 0) {
        v_stack_mE8 = 0;
        a1 = v_rip - 11921118;
        v_stack_mF0 = 0;
        a4 = 0;
        a3 = 0;
        v_stack_mF8 = 0;
        a2 = 0;
        result = ZwUpdateWnfStateData(a1, a2, a3, a4);
    }
    result = PopIsDetailedSleepReliabilityDiagEnabled(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00B7F821;
    result = RtlBootStatusDisableFlushing(1, a2, a3, a4);
    goto loc_00B7F828;
loc_00B7EFC6:
    v_r12 = 0;
    if (sign_flag) goto loc_00B7EE6F;
    result = PopCheckpointSystemSleep(v_r12 + 13, a2, a3, a4);
    result = PopAllocateHiberContext(a1 + 108, a2, a3, a4);
    *(unsigned int *)(a1 + 88) = (unsigned int)(result);
    if (sign_flag) goto loc_00B7EE6F;
    v_stack_mF8 = 1;
    result = PopNotifyTelemetryOsState((unsigned int)(*(unsigned int *)(v_rip + 3722559)), (unsigned int)(*(unsigned int *)(v_rip + 3722605)), (unsigned int)(*(unsigned int *)(v_rip + 3722619)), (unsigned int)(*(unsigned int *)(a1 + 8)));
    a2 = 0;
    *(unsigned int *)(a1 + 100) = (unsigned int)(result);
    result = PopTransitionCheckpoint(a2 + 9, a2, (unsigned int)(*(unsigned int *)(v_rip + 3722619)), (unsigned int)(*(unsigned int *)(a1 + 8)));
    if ((*(unsigned __int8 *)(v_rip + 3722527)) != 0) goto loc_00B7F0C1;
    result = PopCurrentPowerState(a1 + 120, a2, (unsigned int)(*(unsigned int *)(v_rip + 3722619)), (unsigned int)(*(unsigned int *)(a1 + 8)));
    result = Feature_2845206840__private_IsEnabledDeviceUsageNoInline(a1 + 120, a2, (unsigned int)(*(unsigned int *)(v_rip + 3722619)), (unsigned int)(*(unsigned int *)(a1 + 8)));
    if ((unsigned int)(result) == 0) goto loc_00B7F07E;
    result = PopAcquirePolicyLock(a1 + 120, a2, (unsigned int)(*(unsigned int *)(v_rip + 3722619)), (unsigned int)(*(unsigned int *)(a1 + 8)));
    v_stack_mE8 = *(unsigned __int64 *)(v_rip + 3722518);
    v_stack_mF0 = a1 + 120;
    v_stack_mF8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 100)));
    result = PopDiagTracePreSleepNotification((unsigned int)(*(unsigned int *)(a1 + 32)), (unsigned int)(*(unsigned int *)(v_rip + 3722518)), (unsigned int)(*(unsigned int *)(v_rip + 3722492)), (unsigned int)(*(unsigned int *)(v_rip + 3722503)));
    result = PopReleasePolicyLock((unsigned int)(*(unsigned int *)(a1 + 32)), (unsigned int)(*(unsigned int *)(v_rip + 3722518)), (unsigned int)(*(unsigned int *)(v_rip + 3722492)), (unsigned int)(*(unsigned int *)(v_rip + 3722503)));
    goto loc_00B7F0B2;
loc_00B7F07E:
    v_stack_mE8 = *(unsigned __int64 *)(v_rip + 3722459);
    v_stack_mF0 = a1 + 120;
    v_stack_mF8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 100)));
    result = PopDiagTracePreSleepNotification((unsigned int)(*(unsigned int *)(a1 + 32)), (unsigned int)(*(unsigned int *)(v_rip + 3722459)), (unsigned int)(*(unsigned int *)(v_rip + 3722433)), (unsigned int)(*(unsigned int *)(v_rip + 3722444)));
loc_00B7F0B2:
    result = PopCheckpointSystemSleep(16, (unsigned int)(*(unsigned int *)(v_rip + 3722459)), (unsigned int)(*(unsigned int *)(v_rip + 3722433)), (unsigned int)(*(unsigned int *)(v_rip + 3722444)));
    result = PopUmpoSendFlushSleepStudyLoggerNotification(16, (unsigned int)(*(unsigned int *)(v_rip + 3722459)), (unsigned int)(*(unsigned int *)(v_rip + 3722433)), (unsigned int)(*(unsigned int *)(v_rip + 3722444)));
loc_00B7F0C1:
    result = PopEsEnterSleepShutdown(16, (unsigned int)(*(unsigned int *)(v_rip + 3722459)), (unsigned int)(*(unsigned int *)(v_rip + 3722433)), (unsigned int)(*(unsigned int *)(v_rip + 3722444)));
    result = PopThermalSxEntry(16, (unsigned int)(*(unsigned int *)(v_rip + 3722459)), (unsigned int)(*(unsigned int *)(v_rip + 3722433)), (unsigned int)(*(unsigned int *)(v_rip + 3722444)));
    result = PopFanSxEntry(16, (unsigned int)(*(unsigned int *)(v_rip + 3722459)), (unsigned int)(*(unsigned int *)(v_rip + 3722433)), (unsigned int)(*(unsigned int *)(v_rip + 3722444)));
    if ((*(unsigned __int8 *)(a1 + 12)) != 0) goto loc_00B7F129;
    if ((*(unsigned __int8 *)(v_rip + 3722341)) != 0) {
        a3 = 0;
        v_stack_p8 = 1;
        result = v_stack_p8;
        v_stack_m78 = 5;
        v_stack_m70 = result;
        a1 = v_stack_m78;
        v_stack_m68 = 1;
        a2 = a3 + 2;
        v_stack_m60 = 11;
        v_stack_m58 = result;
        v_stack_m50 = 4;
        result = RtlSetSystemBootStatusEx(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_rip + 3722444)));
    }
    *(unsigned __int8 *)(a1 + 12) = 1;
loc_00B7F129:
    if ((*(unsigned __int8 *)(a1 + 24)) == 0) {
        a1 = *(unsigned int *)(v_rip + 3722290);
    }
    result = PopFlushVolumes(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_rip + 3722444)));
    if ((*(unsigned int *)(v_rip + 3722281)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3722279))))) {
        *(unsigned int *)(v_rip + 3722273) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3722279)));
    }
    *(unsigned __int8 *)(v_rip + 3722242) = 2;
    if ((*(unsigned __int8 *)(v_rip + 3722216)) != 0) goto loc_00B7FBE8;
    *(unsigned __int8 *)(v_rip + 3743115) = 0;
    result = PopInitSystemSleeperThread((unsigned int)(*(unsigned int *)(a1 + 52)), a1 + 224, v_stack_m98, (unsigned int)(*(unsigned int *)(v_rip + 3722444)));
    *(unsigned int *)(a1 + 88) = (unsigned int)(result);
    if (!sign_flag) goto loc_00B7F199;
    *(unsigned int *)(a1 + 108) = 20;
    goto loc_00B7EE74;
loc_00B7F199:
    if ((*(unsigned __int8 *)(v_rip + 3722336)) == 0) {
        result = ExWakeTimersPause((unsigned int)(*(unsigned int *)(a1 + 52)), a1 + 224, v_stack_m98, (unsigned int)(*(unsigned int *)(v_rip + 3722444)));
        *(unsigned __int8 *)(v_rip + 3722322) = 1;
    }
    *(unsigned __int64 *)(a1 + 152) = result;
    *(unsigned __int64 *)(a1 + 160) = *(unsigned __int64 *)(v_r10);
    *(unsigned __int64 *)(a1 + 184) = 0;
    if (*(unsigned __int64 *)(v_rip + 3725013) != 0) goto loc_00B7F316;
    if ((*(unsigned __int64 *)(v_rip + 3724975)) != 0) goto loc_00B7F316;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 3726550)) == 0) goto loc_00B7F25B;
    if ((*(unsigned int *)(v_rip + 3722082)) != 5) goto loc_00B7F25B;
    if ((*(unsigned __int8 *)(v_rip + 3722573)) != 0) goto loc_00B7F25B;
    if ((*(unsigned int *)(v_rip + 3722038)) == ((unsigned int)(*(unsigned __int64 *)(v_rip + 3725013) + 2))) goto loc_00B7F25B;
    if ((unsigned __int8)(a1 + 328) == 0) goto loc_00B7F25B;
    if ((a1 + 332) == -1) goto loc_00B7F25B;
    if ((a1 + 332) <= (*(unsigned __int64 *)(v_r10))) goto loc_00B7F25B;
    v_rbx = (a1 + 332) - (*(unsigned __int64 *)(v_r10));
    *(unsigned __int64 *)(a1 + 312) = v_rbx;
    a1 = (*(unsigned __int64 *)(a1 + 152)) + (v_rbx);
loc_00B7F244:
    *(unsigned __int64 *)(a1 + 176) = a1;
    *(unsigned __int64 *)(a1 + 184) = -2;
    goto loc_00B7F321;
loc_00B7F25B:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3726342) + 88)) == 0) goto loc_00B7F2BA;
    if ((*(unsigned int *)(v_rip + 3721981)) == 5) goto loc_00B7F2BA;
    result = PopIsDozeSupported(v_rip + 3726408, a1 + 224, v_stack_m98, *(unsigned __int64 *)(v_rip + 3726342));
    if ((unsigned __int8)(result) == 0) goto loc_00B7F2BA;
    if (((*(unsigned int *)(v_rip + 3721921)) & (0x40000000ULL)) != 0) goto loc_00B7F2BA;
    *(unsigned __int64 *)(a1 + 176) = *(unsigned __int64 *)(a1 + 152);
    a1 = (v_rip + 3726408) * ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3726342) + 88)));
    a1 = (a1) + (*(unsigned __int64 *)(a1 + 152));
    *(unsigned __int64 *)(a1 + 176) = a1;
    goto loc_00B7F321;
loc_00B7F2BA:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 3726550)) == 0) goto loc_00B7F321;
    if ((*(unsigned int *)(v_rip + 3721894)) != 5) goto loc_00B7F321;
    if ((*(unsigned __int8 *)(v_rip + 3722385)) != 0) goto loc_00B7F321;
    if (*(unsigned __int64 *)(v_rip + 3721632) == 0) goto loc_00B7F321;
    if ((*(unsigned int *)(v_rip + 3721840)) != 11) goto loc_00B7F321;
    a2 = (*(unsigned __int64 *)(v_rip + 3721632)) - (*(unsigned __int64 *)(v_r10));
    *(unsigned __int64 *)(a1 + 312) = a2;
    a1 = (a1) * ((unsigned int)(*(unsigned int *)(v_rip + 4480898)));
    a2 = (a2) + (a1);
    a1 = (*(unsigned __int64 *)(a1 + 152)) + (a2);
    *(unsigned __int64 *)(a1 + 312) = a2;
    goto loc_00B7F244;
loc_00B7F316:
    *(unsigned __int64 *)(a1 + 184) = -3;
loc_00B7F321:
    if ((*(unsigned __int64 *)(a1 + 184)) != -1) goto loc_00B7F342;
    result = (unsigned int)(*(unsigned int *)(v_rip + 4480898));
    if ((*(unsigned __int64 *)(v_rip + 3721950)) == 0) {
        result = *(unsigned __int64 *)(a1 + 152);
        *(unsigned __int64 *)(v_rip + 3721934) = result;
    }
    a2 = 0;
    result = memset(v_rip + 3721837, a2, a2 + 72, *(unsigned __int64 *)(v_rip + 3726342));
    *(unsigned int *)(v_rip + 3721807) = 3;
    if ((*(unsigned __int64 *)(a1 + 184)) != -3) goto loc_00B7F39E;
    *(unsigned __int64 *)(v_rip + 3721810) = -3;
    *(unsigned __int64 *)(v_rip + 3721787) = *(unsigned __int64 *)(v_rip + 3725013);
    *(unsigned __int64 *)(v_rip + 3721813) = *(unsigned __int64 *)(a1 + 184);
    *(unsigned __int64 *)(v_rip + 3721783) = *(unsigned __int64 *)(v_rip + 3724558);
    goto loc_00B7F5A7;
loc_00B7F39E:
    if ((*(unsigned __int8 *)(v_rip + 3722171)) != 0) goto loc_00B7F5A7;
    if ((*(unsigned int *)(v_rip + 3721634)) == 14) goto loc_00B7F5A7;
    if ((*(unsigned int *)(v_rip + 3721645)) != 5) goto loc_00B7F40F;
    if ((*(unsigned int *)(a1 + 328)) == 1) goto loc_00B7F40F;
    if ((*(unsigned int *)(a1 + 332)) == 1) goto loc_00B7F40F;
    result = PopQueryPowerSettingUlong(v_rip - 11905758, a1 + 192, a1 + 196, *(unsigned __int64 *)(v_rip + 3726342));
    if ((*(unsigned int *)(a1 + 192)) != 0) goto loc_00B7F407;
    if ((*(unsigned int *)(a1 + 196)) != 0) {
    }
    if (*(unsigned __int64 *)(a1 + 176) == 0) goto loc_00B7F4A3;
    if ((*(unsigned __int64 *)(a1 + 184)) != -2) goto loc_00B7F468;
    result = *(unsigned __int64 *)(a1 + 176);
    if ((*(unsigned int *)(a1 + 328)) != 0) {
        *(unsigned __int64 *)(v_rip + 3721603) = *(unsigned __int64 *)(a1 + 176);
        result = *(unsigned __int64 *)(a1 + 184);
        *(unsigned __int64 *)(v_rip + 3721605) = result;
    }
    if ((*(unsigned int *)(a1 + 332)) == 0) goto loc_00B7F4A3;
    *(unsigned __int64 *)(v_rip + 3721592) = *(unsigned __int64 *)(a1 + 176);
    *(unsigned __int64 *)(v_rip + 3721594) = *(unsigned __int64 *)(a1 + 184);
    goto loc_00B7F4A3;
loc_00B7F468:
loc_00B7F46F:
    *(unsigned __int64 *)(v_rip + 3721837) = *(unsigned __int64 *)(a1 + 176);
    v_rbx = (v_rip + 3721837) + (24);
    if (v_rbx < (v_rip + 3721593)) goto loc_00B7F46F;
loc_00B7F490:
    *(unsigned __int64 *)(v_rip + 3721535) = *(unsigned __int64 *)(a1 + 184);
    a1 = (v_rip + 3721535) + (24);
    if (a1 < (v_rip + 3721576)) goto loc_00B7F490;
loc_00B7F4A3:
    *(unsigned __int64 *)(a1 + 64) = *(unsigned __int64 *)(v_rip + 3721566);
    if (*(unsigned __int64 *)(v_rip + 3721566) == 0) goto loc_00B7F4CF;
    result = (*(unsigned __int64 *)(a1 + 152)) + (0x1312D00ULL);
    if ((*(unsigned __int64 *)(v_rip + 3721566)) < result) {
        *(unsigned __int64 *)(a1 + 64) = result;
        a2 = result;
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 328))) == 0) goto loc_00B7F53C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 328)))) != 2) goto loc_00B7F4EF;
    if (sign_flag) goto loc_00B7F4EF;
    goto loc_00B7F4F2;
loc_00B7F4EF:
    a3 = 0;
loc_00B7F4F2:
    *(unsigned __int8 *)(a1 + 169) = 0;
    v_stack_mF8 = a1 + 200;
    result = ExGetNextWakeTime(a2 + 1, *(unsigned __int64 *)(a1 + 176), a3, a1 + 40);
    *(unsigned __int8 *)(a1 + 336) = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_00B7F547;
    *(unsigned __int64 *)(v_rip + 3721352) = *(unsigned __int64 *)(a1 + 40);
    *(unsigned __int64 *)(v_rip + 3721358) = *(unsigned __int64 *)(a1 + 200);
    goto loc_00B7F547;
loc_00B7F53C:
loc_00B7F547:
    v_r12 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 332))) == 0) goto loc_00B7F5A7;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 332)))) != 2) goto loc_00B7F564;
    if (sign_flag) {
        a3 = 0;
    }
    *(unsigned __int8 *)(a1 + 169) = (unsigned __int8)(a3);
    a1 = (*(unsigned __int64 *)(a1 + 64)) + 1;
    v_stack_mF8 = a1 + 200;
    result = ExGetNextWakeTime(a1, *(unsigned __int64 *)(a1 + 176), a3, a1 + 40);
    *(unsigned __int8 *)(a1 + 336) = (unsigned __int8)(result);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int64 *)(a1 + 40);
        *(unsigned __int64 *)(v_rip + 3721267) = result;
        result = *(unsigned __int64 *)(a1 + 200);
        *(unsigned __int64 *)(v_rip + 3721273) = result;
    }
    *(unsigned __int64 *)(v_rip + 3721227) = *(unsigned __int64 *)(v_rip + 3721226);
    if (*(unsigned __int64 *)(v_rip + 3721226) == 0) goto loc_00B7F5D4;
    a3 = ((unsigned int)(*(unsigned int *)(a1 + 340))) + (*(unsigned __int64 *)(a1 + 152));
    if ((*(unsigned __int64 *)(v_rip + 3721226)) < a3) {
        *(unsigned __int64 *)(v_rip + 3721196) = a3;
    }
    *(unsigned __int64 *)(v_rip + 3721206) = *(unsigned __int64 *)(v_rip + 3721205);
    if (*(unsigned __int64 *)(v_rip + 3721205) == 0) goto loc_00B7F601;
    a3 = ((unsigned int)(*(unsigned int *)(a1 + 340))) + (*(unsigned __int64 *)(a1 + 152));
    if ((*(unsigned __int64 *)(v_rip + 3721205)) < a3) {
        *(unsigned __int64 *)(v_rip + 3721175) = a3;
    }
    result = PopTransitionGetWakeTimerType(*(unsigned __int64 *)(v_rip + 3721152), *(unsigned __int64 *)(v_rip + 3721205), a3, a1 + 40);
    *(unsigned int *)(a1 + 320) = (unsigned int)(result);
    result = PopTransitionGetWakeTimerType(*(unsigned __int64 *)(v_rip + 3721158), *(unsigned __int64 *)(v_rip + 3721205), a3, a1 + 40);
    a1 = 0;
    *(unsigned int *)(a1 + 324) = (unsigned int)(result);
    result = KeQueryPerformanceCounter(a1, *(unsigned __int64 *)(v_rip + 3721205), a3, a1 + 40);
    *(unsigned __int64 *)(v_rip + 3722461) = result;
    result = ExAcquireTimeRefreshLockExclusive(a1, *(unsigned __int64 *)(v_rip + 3721205), a3, a1 + 40);
    result = ExUpdateSystemTimeFromCmos(1, 1, a3, a1 + 40);
    result = ExReleaseTimeRefreshLockExclusive(1, 1, a3, a1 + 40);
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rip + 3721058), *(unsigned __int64 *)(v_rip + 3721089), a3, a1 + 40);
    *(unsigned __int8 *)(v_rip + 2670350) = 0;
    result = PpmCheckPausePpmEngineForSx(*(unsigned __int64 *)(v_rip + 3721058), *(unsigned __int64 *)(v_rip + 3721089), a3, a1 + 40);
    result = PsLookupProcessByProcessId(v_stack_m98, v_stack_p20, a3, a1 + 40);
    result = PsLookupThreadByThreadId(v_stack_m90, v_stack_mC8, a3, a1 + 40);
    result = PopSetDevicesSystemState(v_stack_m90, v_stack_mC8, a3, a1 + 40);
    *(unsigned __int8 *)(a1 + 96) = 1;
    result = PopNewWakeInfo(v_stack_m90, v_stack_mC8, a3, a1 + 40);
    a4 = 0;
    a3 = 0;
    *(unsigned __int64 *)(a1 + 304) = result;
    *(unsigned int *)(a1 + 112) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3725136)));
    v_stack_mF8 = 0;
    result = PopPushPowerStateTransitionRecordWithCallback(v_stack_p20, v_stack_mC8, a3, a4);
    a2 = 0;
    result = KeSetEvent(a1 + 248, a2, 1, a4);
    v_stack_mF8 = 0;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(a1 + 272, a2, a3, a4);
    if (!(sign_flag)) {
        result = PoDelistPowerStateTransitionBlocker(a1 + 272, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_rip + 3721467) = 0;
    *(unsigned int *)(a1 + 88) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 300)));
    result = PopSetPowerActionWatchdogState(2, a2, a3, a4);
    a1 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3720764))));
    if ((*(unsigned __int8 *)(v_rip + 3723094)) != 0) { a1 = *(unsigned int *)(v_rip + 3720763); }
    *(unsigned int *)(v_rip + 3720761) = (unsigned int)(a1);
    *(unsigned __int64 *)(v_rip + 3047762) = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 8)))) & (8)) == 0) goto loc_00B7F753;
    *(unsigned int *)(a1 + 32) = 6;
    goto loc_00B7F75D;
loc_00B7F753:
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3720764)));
loc_00B7F75D:
    v_stack_mE8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 324)));
    *(unsigned int *)(a1 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3720715)));
    v_stack_mF0 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 320)));
    v_stack_mF8 = *(unsigned __int64 *)(v_rip + 3720773);
    result = PopDiagTracePostSleepNotification((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3720719)))), (unsigned int)(*(unsigned int *)(v_rip + 3720684)), (unsigned int)(*(unsigned int *)(v_rip + 3720715)), *(unsigned __int64 *)(v_rip + 3720766));
    if ((*(unsigned __int8 *)(v_rip + 3741544)) != 0) {
        result = PopDiagTraceMtrrError((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3720719)))), (unsigned int)(*(unsigned int *)(v_rip + 3720684)), (unsigned int)(*(unsigned int *)(v_rip + 3720715)), *(unsigned __int64 *)(v_rip + 3720766));
    }
    if (!sign_flag) goto loc_00B7EE74;
    if ((*(unsigned int *)(v_rip + 3720621)) != 5) goto loc_00B7EE74;
    v_stack_m88 = v_xmm0;
    result = StringCchPrintfW(v_rip + 3719205, 128, v_rip + 1921, (unsigned int)(*(unsigned int *)(a1 + 88)));
    result = RtlInitUnicodeString(v_stack_m88, v_rip + 3719189, v_rip + 1921, (unsigned int)(*(unsigned int *)(a1 + 88)));
    a3 = 0;
    result = IoRaiseInformationalHardError((unsigned int)(0xC0000411ULL), v_stack_m88, a3, (unsigned int)(*(unsigned int *)(a1 + 88)));
    result = PopDiagTraceHibernateErrorStatus((unsigned int)(*(unsigned int *)(a1 + 88)), v_stack_m88, a3, (unsigned int)(*(unsigned int *)(a1 + 88)));
    goto loc_00B7EE74;
loc_00B7F812:
    v_r12 = 0;
    *(unsigned int *)(2) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3720719)));
    *(unsigned int *)(a1 + 88) = 0;
    goto loc_00B7EE6F;
loc_00B7F821:
    *(unsigned __int8 *)(v_rip + 2669904) = 1;
loc_00B7F828:
    result = PopCheckpointSystemSleep(56, v_stack_m88, a3, (unsigned int)(*(unsigned int *)(a1 + 88)));
    a2 = 0;
    a1 = 0;
    result = guard_dispatch_icall(a1, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 88)));
    v_stack_mF8 = 0;
    result = PopNotifyTelemetryOsState((unsigned int)(*(unsigned int *)(v_rip + 3720427)), (unsigned int)(*(unsigned int *)(v_rip + 3720473)), (unsigned int)(*(unsigned int *)(v_rip + 3720487)), (unsigned int)(*(unsigned int *)(a1 + 8)));
    *(unsigned int *)(a1 + 100) = (unsigned int)(result);
    result = PopCancelIgnoreBatteryStatusChange((unsigned int)(*(unsigned int *)(v_rip + 3720427)), (unsigned int)(*(unsigned int *)(v_rip + 3720473)), (unsigned int)(*(unsigned int *)(v_rip + 3720487)), (unsigned int)(*(unsigned int *)(a1 + 8)));
    a4 = 0;
    a3 = 0;
    result = PopExecuteOnTargetProcessors(v_rip + 4487329, v_rip - 7009157, a3, a4);
    if ((*(unsigned __int8 *)(a1 + 48)) != 0) {
        result = PopReleasePolicyLock(v_rip + 4487329, v_rip - 7009157, a3, a4);
        *(unsigned __int8 *)(a1 + 48) = 0;
    }
    if ((*(unsigned __int8 *)(a1 + 96)) != 0) {
        result = PopProcessDeviceWakeSource(v_rip + 4487329, v_rip - 7009157, a3, a4);
    }
    result = PoClearBroadcast(v_rip + 4487329, v_rip - 7009157, a3, a4);
    *(unsigned __int64 *)(v_rip + 3720414) = 0;
    result = PopFanSxExit(v_rip + 4487329, v_rip - 7009157, a3, a4);
    result = PopEsExitSleep(v_rip + 4487329, v_rip - 7009157, a3, a4);
    *(unsigned int *)(a1 + 116) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3724626)));
    *(unsigned __int64 *)(v_rip + 3718721) = 0;
    *(unsigned __int64 *)(v_rip + 3718706) = v_rip - 4322864;
    *(unsigned __int64 *)(v_rip + 3718683) = 0;
    result = ExQueueWorkItem(v_rip + 3718719, 1, a3, a4);
    if ((*(unsigned int *)(a1 + 88)) >= 0) {
        a1 = a1 + 120;
        result = PopCurrentPowerState(a1, 1, a3, a4);
    }
    if ((*(unsigned __int8 *)(a1 + 96)) != 0) {
        result = PopHandleWakeSources(a1, 1, a3, a4);
    }
    if ((*(unsigned int *)(a1 + 88)) >= 0) {
        a4 = v_stack_p18;
        a3 = v_stack_mB8;
        a2 = v_stack_mB0;
        a1 = v_stack_p10;
        result = PopQueryMostRecentWakeSourceAttributes(a1, a2, a3, a4);
        result = v_stack_p10;
        a4 = *(unsigned int *)(a1 + 324);
        a3 = *(unsigned int *)(a1 + 320);
        a2 = *(unsigned __int64 *)(v_rip + 3720353);
        a1 = *(unsigned __int64 *)(v_rip + 3720322);
        v_stack_mD8 = (unsigned int)(result);
        result = v_stack_mB8;
        v_stack_mE0 = result;
        result = v_stack_mB0;
        v_stack_mE8 = result;
        result = *(unsigned int *)(a1 + 128);
        v_stack_mF0 = (unsigned int)(result);
        result = *(unsigned int *)(a1 + 132);
        v_stack_mF8 = (unsigned int)(result);
        result = SshSessionManagerTracePostSleepNotification(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(a1 + 48)) == 0) {
        result = PopAcquirePolicyLock(a1, a2, a3, a4);
        *(unsigned __int8 *)(a1 + 48) = 1;
    }
    if ((*(unsigned int *)(a1 + 88)) < 0) goto loc_00B7FADF;
    result = PopUpdateSystemIdleContext(1, a2, a3, a4);
    result = PopPowerAggregatorNotifySystemWake((unsigned int)(*(unsigned int *)(a1 + 28)), a2, a3, a4);
    *(unsigned __int8 *)(v_rip + 3720088) = 0;
    if (((int)(*(unsigned int *)(v_rip + 3720209))) >= 3) goto loc_00B7FAC1;
    *(unsigned __int64 *)(v_rip + 3720248) = *(unsigned __int64 *)(v_rip - 12057021 + (int)(*(unsigned int *)(v_rip + 3720209)) + (int)(*(unsigned int *)(v_rip + 3720209)) * 2 * 8 + 15777216);
    *(unsigned int *)(v_rip + 3724041) = 0;
    *(unsigned int *)(v_rip + 3722398) = 0;
    *(unsigned int *)(v_rip + 3722395) = 0;
    if ((*(unsigned __int64 *)(v_rip - 12057021 + (int)(*(unsigned int *)(v_rip + 3720209)) + (int)(*(unsigned int *)(v_rip + 3720209)) * 2 * 8 + 15777224)) != -1) goto loc_00B7FA38;
    result = PopDeferDoze((unsigned int)(*(unsigned int *)(a1 + 328)), (unsigned int)(*(unsigned int *)(a1 + 332)), a1 + 120, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00B7FA1F;
    *(unsigned int *)(v_rip + 3719984) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    *(unsigned int *)(v_rip + 3719979) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    goto loc_00B7FA2F;
loc_00B7FA1F:
    *(unsigned int *)(v_rip + 3719967) = 2;
    *(unsigned int *)(v_rip + 3719961) = 5;
loc_00B7FA2F:
    goto loc_00B7FAA0;
loc_00B7FA38:
    if (((unsigned int)(*(unsigned int *)(a1 + 4))) != -2) goto loc_00B7FA5E;
    if ((*(unsigned __int64 *)(v_rip + 3720035)) != 0) goto loc_00B7FADF;
    *(unsigned __int64 *)(v_rip + 3720015) = *(unsigned __int64 *)(v_rip + 3720006);
    goto loc_00B7FADF;
loc_00B7FA5E:
    if ((*(unsigned __int64 *)(v_rip + 3720006)) != -3) goto loc_00B7FA74;
    *(unsigned __int64 *)(v_rip + 3722813) = 0;
    *(unsigned __int64 *)(v_rip + 3722798) = 0;
    goto loc_00B7FADF;
loc_00B7FA74:
    if ((*(unsigned int *)(v_rip + 3724177)) != 1) goto loc_00B7FAA9;
    if ((*(unsigned int *)(a1 + 332)) != 0) goto loc_00B7FADF;
    a2 = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 332))) | (2));
    *(unsigned int *)(v_rip + 3719859) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    *(unsigned int *)(v_rip + 3719854) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    *(unsigned __int8 *)(v_rip + 3719840) = (unsigned __int8)(a2);
loc_00B7FAA0:
    *(unsigned __int8 *)(a1 + 216) = 0;
    goto loc_00B7FADF;
loc_00B7FAA9:
    if ((*(unsigned int *)(a1 + 332)) != 0) goto loc_00B7FADF;
    if ((*(unsigned int *)(a1 + 112)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 116))))) goto loc_00B7FADF;
    result = PopCheckPowerSourceAfterRtcWakeSet((unsigned int)(*(unsigned int *)(a1 + 328)), a2, a1 + 120, a4);
    goto loc_00B7FADF;
loc_00B7FAC1:
    result = PopIsMostRecentWakeAttended((unsigned int)(*(unsigned int *)(a1 + 328)), a2, a1 + 120, a4);
    if ((unsigned __int8)(result) == 0) {
        *(unsigned int *)(v_rip + 3723799) = 0;
        *(unsigned int *)(v_rip + 3722156) = 0;
        *(unsigned int *)(v_rip + 3722153) = 0;
    }
    if ((*(unsigned __int8 *)(v_rip + 3719962)) == 0) goto loc_00B7FB04;
    if ((*(unsigned __int8 *)(a1 + 216)) != 0) {
        result = ExWakeTimersResume((unsigned int)(*(unsigned int *)(a1 + 328)), a2, a1 + 120, a4);
        *(unsigned __int8 *)(v_rip + 3719939) = 0;
        *(unsigned __int64 *)(v_rip + 3719940) = 0;
    }
    if ((*(unsigned __int8 *)(v_rip + 3722101)) != 0) {
        result = PopBootLoaderTraceProcess((unsigned int)(*(unsigned int *)(a1 + 328)), a2, a1 + 120, a4);
    }
    *(unsigned __int8 *)(v_rip + 3720263) = 0;
    result = PopResetActionDefaults((unsigned int)(*(unsigned int *)(a1 + 328)), a2, a1 + 120, a4);
    result = PopSetPowerActionState(2, a2, a1 + 120, a4);
    result = PopReleasePolicyLock(2, a2, a1 + 120, a4);
    result = (unsigned int)(*(unsigned int *)(v_rip + 3722067));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3722067))) != 0) {
        a1 = *(unsigned int *)(v_rip + 3722061);
        result = PoSetUserPresent(a1, a2, a1 + 120, a4);
    }
    result = ExQueueWorkItem(v_rip + 3718292, 1, a1 + 120, a4);
    result = PopCheckForWork(v_rip + 3718292, 1, a1 + 120, a4);
    if ((*(unsigned int *)(a1 + 88)) >= 0) {
        result = PpmPerfReApplyStates(v_rip + 3718292, 1, a1 + 120, a4);
    }
    a1 = 0;
    *(unsigned int *)(v_rip + 3719655) = 17;
    result = KeQueryPerformanceCounter(a1, 1, a1 + 120, a4);
    result = (result) - (*(unsigned __int64 *)(v_rip + 3701751));
    *(unsigned __int64 *)(v_rip + 3721520) = result;
    if (*(unsigned __int64 *)(a1 + 200) != 0) {
        result = ExDeleteWakeTimerInfo(*(unsigned __int64 *)(a1 + 200), 1, a1 + 120, a4);
        *(unsigned __int64 *)(a1 + 200) = 0;
    }
    *(unsigned __int64 *)(v_rip + 3046641) = 0;
loc_00B7FBA7:
    if (v_stack_p20 != 0) {
        a1 = v_stack_p20;
        result = ObfDereferenceObject(a1, 1, a1 + 120, a4);
    }
    if (v_stack_mC8 != 0) {
        a1 = v_stack_mC8;
        result = ObfDereferenceObject(a1, 1, a1 + 120, a4);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 108))) != 0) {
        a1 = *(unsigned int *)(a1 + 88);
        result = PopDiagTraceStateTransitionFailurePoint(a1, (unsigned int)(*(unsigned int *)(a1 + 108)), a1 + 120, a4);
    }
    v_rsp = (v_rsp) + (216);
    return (unsigned int)(*(unsigned int *)(a1 + 88));
loc_00B7FBE8:
    result = PopFxPrepareDevicesForShutdown(a1, (unsigned int)(*(unsigned int *)(a1 + 108)), a1 + 120, a4);
    a1 = (*(unsigned __int64 *)(v_rip + 3719572)) + (48);
    result = IoFreePoDeviceNotifyList(a1, (unsigned int)(*(unsigned int *)(a1 + 108)), a1 + 120, a4);
    if ((*(unsigned int *)(v_rip + 3719505)) == ((unsigned int)(v_stack_p20))) {
        *(unsigned __int8 *)(v_rip + 4484850) = 1;
    }
    result = PopTransitionCheckpoint(8, (unsigned int)((unsigned int)(v_stack_p20)), a1 + 120, a4);
    result = PopGracefulShutdown(8, (unsigned int)((unsigned int)(v_stack_p20)), a1 + 120, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopTransitionSystemPowerStateEx(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint32_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p8;

    local_rsp = (local_rsp) - (216);
    v_stack_mA8 = 0x20000ULL;
    Arg1 = 0;
    v_stack_mA0 = v_rip + 5715;
    v_stack_p10 = 0;
    *(uint8_t *)(arg1 + 0xC) = 0;
    *(uint8_t *)(arg1 + 0x18) = 0;
    *(uint32_t *)(arg1 + 0x1C) = 0;
    *(uint64_t *)(arg1 + 0x40) = 0;
    *(uint64_t *)(arg1 + 0x28) = 0;
    local_r12 = 0;
    *(uint32_t *)(arg1 + 0x64) = 0;
    *(uint32_t *)(arg1 + 0x6C) = 0;
    *(uint64_t *)(arg1 + 0xC8) = 0;
    *(uint64_t *)(arg1 + 0xB0) = 0;
    *(uint64_t *)(arg1 + 0xB8) = 0;
    *(uint64_t *)(arg1 + 0x130) = 0;
    *(uint8_t *)(arg1 + 0x150) = 0;
    *(uint64_t *)(arg1 + 0x140) = 0;
    *(uint32_t *)(arg1 + 0x14C) = 0;
    v_stack_mB0 = v_stack_mA8;
    v_stack_p18 = 0;
    v_stack_p20 = 0;
    v_stack_mC8 = 0;
    v_stack_mC0 = 0;
    v_stack_mB8 = v_stack_mA8;
    *(uint32_t *)(arg1 + 0x70) = (uint32_t)(Arg1 + 1);
    *(uint32_t *)(arg1 + 0x74) = (uint32_t)(Arg1 + 1);
    *(uint8_t *)(arg1 + 0xD8) = (uint8_t)(Arg1 + 1);
    *(uint32_t *)(arg1 + 0x148) = (uint32_t)(Arg1 + 1);
    *(uint64_t *)(arg1 + 0xC0) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x38E578))) & (0x10000ULL));
    *(uint32_t *)(arg1 + 0x58) = 0;
    result = (uint32_t)(-(result));
    v_stack_m98 = v_xmm0;
    Arg1 = (uint32_t)((Arg1) & (0xEE1E5D00ULL));
    Arg1 = (uint32_t)((Arg1) + (0x23C34600ULL));
    *(uint32_t *)(arg1 + 0x154) = (uint32_t)(Arg1);
    result = PopTransitionCheckpoint(0 + 8, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    result = 0 + 2;
    if ((*(uint32_t *)(arg1)) == ((uint32_t)(0 + 2))) {
        result = PnpSurpriseFailUnsafeDmaDevices(0 + 8, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    }
    if ((*(uint32_t *)(arg1)) == 4) {
        result = PopReadShutdownPolicy(0 + 8, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    }
    result = PopAcquireTransitionLockAfterSleep(0 + 8, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    result = MmLockPagableSectionByHandle(*(uint64_t *)(v_rip + 0x44821F), (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    result = PopRunMaximumIrpWorkers(*(uint64_t *)(v_rip + 0x44821F), (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x38CDFF) = 0;
    Arg1 = 0;
    *(uint64_t *)(v_rip + 0x38CDEE) = v_rip - 26450;
    *(uint64_t *)(v_rip + 0x38CDD7) = 0;
    result = CmSetLazyFlushState(Arg1, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    result = PopNotifyCallbacksPreSleep(Arg1, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    Arg1 = 0;
    result = ExSwapinWorkerThreads(Arg1, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    Arg1 = 0;
    if ((*(uint32_t *)(v_rip + 0x38D4D3)) == ((uint32_t)(Arg1 + 1))) { Arg1 = 2; }
    result = PoInitializeBroadcast(Arg1, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    *(uint32_t *)(arg1 + 0x58) = (uint32_t)(result);
    if (!sign_flag) goto loc_00B7EA53;
    result = ExQueueWorkItem(v_rip + 3722654, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    *(uint32_t *)(arg1 + 0x6C) = 5;
    goto loc_00B7FBA7;
loc_00B7EA53:
    result = PopCheckPowerSourceAfterRtcWakeCancel(v_rip + 3722654, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    result = PopCurrentPowerStatePrecise(Arg1 + 120, v_stack_mC0, Arg3, Arg4);
    result = PopAcquirePolicyLock(Arg1 + 120, v_stack_mC0, Arg3, Arg4);
    *(uint8_t *)(arg1 + 0x30) = (uint8_t)(Arg1 + 1);
    result = PopFilterCapabilities(v_rip + 3728452, v_rip + 3724199, Arg3, Arg4);
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x38D2BA)) == 0) goto loc_00B7EABB;
    if (((uint8_t)(*(uint8_t *)(v_rip + 0x38D2BA))) == 2) goto loc_00B7EAC0;
    result = PopReleasePolicyLock(v_rip + 3728452, v_rip + 3724199, Arg3, Arg4);
    result = PoClearBroadcast(v_rip + 3728452, v_rip + 3724199, Arg3, Arg4);
    result = ExQueueWorkItem(v_rip + 3722557, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    *(uint32_t *)(arg1 + 0x6C) = 6;
    *(uint32_t *)(arg1 + 0x58) = 0xC0000021ULL;
    goto loc_00B7FBA7;
loc_00B7EABB:
    result = PopResetActionDefaults(v_rip + 3722557, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
loc_00B7EAC0:
    result = PopSetPowerActionState(3, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x38D2B3) = *(uint64_t *)(v_rip + 0x38D202);
    result = PopIgnoreBatteryStatusChange(3, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    result = PopCheckResiliencyScenarios(3, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    result = PopEnforceResiliencyScenarios(Arg1 + 208, (uint32_t)((uint32_t)(Arg1 + 1)), Arg3, Arg4);
    Arg4 = 0;
    Arg3 = 0;
    result = PopExecuteOnTargetProcessors(v_rip + 4490785, v_rip - 6991381, Arg3, Arg4);
    if ((*(uint32_t *)(arg1)) == 6) {
        *(uint32_t *)(v_rip + 0x38D22E) = 6;
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)) - 4)) > 2) goto loc_00B7EB61;
    *(uint8_t *)(v_rip + 0x38D1F9) = 1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) == 5) {
        *(uint8_t *)(v_rip + 0x38D1EE) = 1;
    }
    if ((*(uint64_t *)(v_rip + 0x38D3E6)) == 0) goto loc_00B7EB61;
    if ((*(uint64_t *)(v_rip + 0x38D3E5)) == 0) goto loc_00B7EB61;
    result = MmZeroPageFileAtShutdown((uint32_t)(*(uint32_t *)(arg1)), v_rip - 6991381, Arg3, Arg4);
    if ((uint32_t)(result) != 0) {
        Arg2 = *(uint64_t *)(v_rip + 0x38D3D3);
        Arg1 = *(uint64_t *)(v_rip + 0x38D3C4);
        result = PopZeroHiberFile(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint8_t *)(arg1 + 0x48) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) - (2));
    if (((uint32_t)(result)) <= 1) {
        *(uint8_t *)(v_rip + 0x38D19B) = 1;
    }
    *(uint8_t *)(arg1 + 0x60) = 0;
    *(uint32_t *)(arg1 + 0x58) = 0xC0000120ULL;
loc_00B7EB96:
    if ((*(uint8_t *)(arg1 + 0x30)) == 0) {
        result = PopAcquirePolicyLock(2, Arg2, Arg3, Arg4);
        Arg1 = 2;
        *(uint8_t *)(arg1 + 0x30) = 1;
    }
    if ((*(uint32_t *)(v_rip + 0x38D193)) == 0) goto loc_00B7F812;
    *(uint8_t *)(arg1 + 0x68) = (uint8_t)(*(uint8_t *)(v_rip + 0x38D183));
    *(uint8_t *)(v_rip + 0x38D179) = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x58)))) != 0xC0000120ULL) goto loc_00B7EC25;
    if (((*(uint8_t *)(arg1 + 0x68)) & ((uint8_t)(Arg1))) == 0) goto loc_00B7EBE8;
    if (sign_flag) goto loc_00B7EBE8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38D170)))) & (3)) != 0) goto loc_00B7EE4D;
loc_00B7EBE8:
    result = PopActionRetrieveInitialState(v_rip + 3723596, Arg1 + 16, v_rip + 3723642, Arg1 + 72);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x38D13D))) + (-4));
    if (((uint32_t)(result)) <= 2) {
        *(uint8_t *)(v_rip + 0x38D12C) = 1;
        result = *(uint32_t *)(arg1 + 0x8);
        *(uint32_t *)(v_rip + 0x38D12D) = (uint32_t)(result);
    }
    goto loc_00B7EC2D;
loc_00B7EC25:
    if (sign_flag) goto loc_00B7EE6C;
loc_00B7EC2D:
    result = PopReleasePolicyLock(v_rip + 3723596, Arg1 + 16, v_rip + 3723642, Arg1 + 72);
    *(uint8_t *)(arg1 + 0x30) = 0;
    *(uint32_t *)(arg1 + 0x148) = 1;
    result = PopQueryPowerSettingUlong(v_rip - 11904772, Arg1 + 328, Arg1 + 332, Arg1 + 72);
    result = 0;
    if (((*(uint32_t *)(v_rip + 0x38D0EE)) & (0x40000000ULL)) != 0) {
        *(uint32_t *)(arg1 + 0x148) = 0;
        *(uint32_t *)(arg1 + 0x14C) = 0;
    }
    if ((*(uint8_t *)(v_rip + 0x38D1CB)) != 0) goto loc_00B7EC7F;
    if ((*(uint8_t *)(v_rip + 0x38D1B1)) != 0) goto loc_00B7EC7F;
    if ((*(uint8_t *)(v_rip + 0x38D1B0)) == 0) {
        *(uint32_t *)(arg1 + 0x14C) = 0;
    }
    result = PopInitializePowerPolicySimulate(v_rip - 11904772, Arg1 + 328, Arg1 + 332, Arg1 + 72);
    *(uint32_t *)(v_rip + 0x38D0D3) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38D0D5)));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x38D0C2))) >> (27));
    Arg2 = (uint32_t)((Arg2) & (2));
    *(uint32_t *)(arg1 + 0x5C) = (uint32_t)(Arg2);
    result = PopAdvanceSystemPowerState(v_rip + 3723487, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x38D097)), (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) & (8)) == 0) goto loc_00B7ECDF;
    *(uint8_t *)(v_rip + 0x38D29C) = 1;
    *(uint8_t *)(arg1 + 0x18) = 0;
    *(uint32_t *)(v_rip + 0x38D0A2) = 5;
    *(uint32_t *)(arg1 + 0x20) = 6;
    goto loc_00B7ED1C;
loc_00B7ECDF:
    result = PopFastS4Check(v_rip + 3723487, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x38D097)), (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    if ((uint8_t)(result) == 0) goto loc_00B7ED08;
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38D080)));
    *(uint32_t *)(v_rip + 0x38D076) = 5;
    *(uint8_t *)(arg1 + 0x18) = 1;
    *(uint32_t *)(arg1 + 0x34) = 6;
    goto loc_00B7ED36;
loc_00B7ED08:
    *(uint32_t *)(v_rip + 0x38D066) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38D080)));
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38D080)));
    *(uint8_t *)(arg1 + 0x18) = 0;
loc_00B7ED1C:
    *(uint32_t *)(arg1 + 0x34) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB7ED23 + (int32_t)(*(uint32_t *)(v_rip + 0x38D054)) * 4 + 0x29758)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB7ED23 + (int32_t)(*(uint32_t *)(v_rip + 0x38D054)) * 4 + 0x29758)))) > 6) goto loc_00B7EE29;
loc_00B7ED36:
    if ((*(uint64_t *)(v_rip - 0xB7ED44 + (int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB7ED23 + (int32_t)(*(uint32_t *)(v_rip + 0x38D054)) * 4 + 0x29758)))) + (int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xB7ED23 + (int32_t)(*(uint32_t *)(v_rip + 0x38D054)) * 4 + 0x29758)))) * 2 * 8 + 0xF0CC48)) == 0) goto loc_00B7EE29;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) & (8)) == 0) goto loc_00B7ED5F;
    goto loc_00B7ED6E;
loc_00B7ED5F:
    if ((*(uint8_t *)(v_rip + 0x38CFDC)) != 0) goto loc_00B7ED75;
loc_00B7ED6E:
    result = PopSetSleepMarker((uint32_t)(*(uint32_t *)(v_rip + 0x38CFFE)), Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x38D097)), (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    goto loc_00B7ED7F;
loc_00B7ED75:
    result = PopSetShutdownMarker((uint32_t)(*(uint32_t *)(v_rip + 0x38CFFE)), Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x38D097)), (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    result = PopSaveLidReliabilityState((uint32_t)(*(uint32_t *)(v_rip + 0x38CFFE)), Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x38D097)), (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
loc_00B7ED7F:
    result = PopAcquirePolicyLock((uint32_t)(*(uint32_t *)(v_rip + 0x38CFFE)), Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x38D097)), (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    if (((*(uint8_t *)(v_rip + 0x38CFB5)) & (6)) == 0) goto loc_00B7ED9D;
    *(uint8_t *)(arg1 + 0x30) = 1;
    *(uint32_t *)(arg1 + 0x58) = 0xC0000120ULL;
    goto loc_00B7EE43;
loc_00B7ED9D:
    result = PopReleasePolicyLock((uint32_t)(*(uint32_t *)(v_rip + 0x38CFFE)), Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x38D097)), (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    result = PopCheckpointSystemSleep(10, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x38D097)), (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    *(uint8_t *)(v_rip + 0x38CFA6) = 3;
    result = PopDiagTraceKernelQueriesAllowed(*(uint8_t *)(arg1 + 0x48), Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x38D097)), (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    if ((*(uint8_t *)(arg1 + 0x48)) == 0) goto loc_00B7EE0B;
    result = PopSetDevicesSystemState(*(uint8_t *)(arg1 + 0x48), Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x38D097)), (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    *(uint32_t *)(arg1 + 0x58) = (uint32_t)(result);
    if (!sign_flag) goto loc_00B7EE07;
    if (((uint32_t)(result)) == 0xC0000120ULL) goto loc_00B7EE0B;
    result = PopFindNextSystemPowerState((uint32_t)(*(uint32_t *)(arg1 + 0x10)), *(uint8_t *)(arg1 + 0x18), Arg1 + 72, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    *(uint8_t *)(arg1 + 0x24) = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_00B7EE65;
    goto loc_00B7EE3F;
loc_00B7EE07:
    *(uint8_t *)(arg1 + 0x60) = 1;
loc_00B7EE0B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x58)))) != 0xC0000120ULL) goto loc_00B7EFC6;
    goto loc_00B7EE43;
loc_00B7EE29:
    result = PopFindNextSystemPowerState((uint32_t)(*(uint32_t *)(arg1 + 0x10)), *(uint8_t *)(arg1 + 0x18), Arg1 + 72, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    *(uint8_t *)(arg1 + 0x24) = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_00B7EE6C;
loc_00B7EE3F:
loc_00B7EE43:
    goto loc_00B7EB96;
loc_00B7EE4D:
    result = PopGetPolicyWorker(2, *(uint8_t *)(arg1 + 0x18), Arg1 + 72, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    local_r12 = 0;
    *(uint32_t *)(arg1 + 0x6C) = 8;
    goto loc_00B7EE74;
loc_00B7EE65:
    *(uint32_t *)(arg1 + 0x6C) = 9;
loc_00B7EE6C:
    local_r12 = 0;
loc_00B7EE6F:
loc_00B7EE74:
    if ((*(uint8_t *)(arg1 + 0x30)) != 0) {
        result = PopReleasePolicyLock(2, *(uint8_t *)(arg1 + 0x18), Arg1 + 72, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    }
    if ((*(uint8_t *)(v_rip + 0x38D0DA)) != 0) {
        Arg1 = 0;
        result = KeQueryPerformanceCounter(Arg1, *(uint8_t *)(arg1 + 0x18), Arg1 + 72, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
        Arg2 = v_rip + 3724938;
        *(uint64_t *)(v_rip + 0x38D683) = result;
        Arg1 = v_rip + 3724916;
        result = PopQpcTimeInMs(Arg1, Arg2, Arg1 + 72, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
        *(uint32_t *)(v_rip + 0x38D095) = (uint32_t)(result);
    }
    if ((*(uint32_t *)(arg1 + 0x58)) < 0) goto loc_00B7EF28;
    *(uint64_t *)(v_rip + 0x38CED6) = *(uint64_t *)(arg1 + 0x130);
    result = ExUpdateSystemTimeFromCmos(1, 1, Arg1 + 72, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    Arg2 = 0;
    result = guard_dispatch_icall(1, Arg2, Arg1 + 72, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    if ((uint32_t)(result) != 0) {
        *(uint8_t *)(arg1 + 0xA8) = 1;
    }
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg1 + 72, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    Arg3 = 0;
    *(uint64_t *)(v_rip + 0x38D42D) = result;
    Arg2 = 0;
    result = PfPowerActionNotify(2, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    *(uint64_t *)(v_rip + 0x38CE80) = *(uint64_t *)(result);
    result = PopDiagComputeEarlyHiberStats(2, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    if ((*(uint32_t *)(arg1 + 0x1C)) == 4) {
        result = PopDiagTraceFirmwareS3Stats(2, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    }
    *(uint8_t *)(v_rip + 0x38CE3A) = 1;
    *(uint8_t *)(v_rip + 0x38CDEA) = 0;
    *(uint8_t *)(v_rip + 0x38CDE4) = 0;
    if ((*(uint8_t *)(arg1 + 0x60)) != 0) {
        Arg2 = 0;
        Arg3 = 0;
        Arg1 = Arg2 + 3;
        result = PfPowerActionNotify(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
        result = PopSetDevicesSystemState(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
        Arg3 = 0;
        Arg2 = Arg3 + 1;
        Arg1 = Arg2 + 2;
        result = PfPowerActionNotify(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    }
    if ((*(uint32_t *)(arg1 + 0x58)) >= 0) {
        result = WheaResumedFromHibernate(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    }
    result = PpmCheckResumePpmEngineFromSx(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    result = PopCurrentPowerStatePrecise(Arg1 + 120, v_stack_mC0, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    if ((*(uint8_t *)(arg1 + 0xA8)) != 0) {
        v_stack_mE8 = 0;
        Arg1 = v_rip - 11921118;
        v_stack_mF0 = 0;
        Arg4 = 0;
        Arg3 = 0;
        v_stack_mF8 = 0;
        Arg2 = 0;
        result = ZwUpdateWnfStateData(Arg1, Arg2, Arg3, Arg4);
    }
    result = PopIsDetailedSleepReliabilityDiagEnabled(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00B7F821;
    result = RtlBootStatusDisableFlushing(1, Arg2, Arg3, Arg4);
    goto loc_00B7F828;
loc_00B7EFC6:
    local_r12 = 0;
    if (sign_flag) goto loc_00B7EE6F;
    result = PopCheckpointSystemSleep(local_r12 + 13, Arg2, Arg3, Arg4);
    result = PopAllocateHiberContext(Arg1 + 108, Arg2, Arg3, Arg4);
    *(uint32_t *)(arg1 + 0x58) = (uint32_t)(result);
    if (sign_flag) goto loc_00B7EE6F;
    v_stack_mF8 = 1;
    result = PopNotifyTelemetryOsState((uint32_t)(*(uint32_t *)(v_rip + 0x38CD3F)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CD6D)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CD7B)), (uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    Arg2 = 0;
    *(uint32_t *)(arg1 + 0x64) = (uint32_t)(result);
    result = PopTransitionCheckpoint(Arg2 + 9, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x38CD7B)), (uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    if ((*(uint8_t *)(v_rip + 0x38CD1F)) != 0) goto loc_00B7F0C1;
    result = PopCurrentPowerState(Arg1 + 120, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x38CD7B)), (uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    result = Feature_2845206840__private_IsEnabledDeviceUsageNoInline(Arg1 + 120, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x38CD7B)), (uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    if ((uint32_t)(result) == 0) goto loc_00B7F07E;
    result = PopAcquirePolicyLock(Arg1 + 120, Arg2, (uint32_t)(*(uint32_t *)(v_rip + 0x38CD7B)), (uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    v_stack_mE8 = *(uint64_t *)(v_rip + 0x38CD16);
    v_stack_mF0 = Arg1 + 120;
    v_stack_mF8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x64)));
    result = PopDiagTracePreSleepNotification((uint32_t)(*(uint32_t *)(arg1 + 0x20)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CD16)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CCFC)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CD07)));
    result = PopReleasePolicyLock((uint32_t)(*(uint32_t *)(arg1 + 0x20)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CD16)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CCFC)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CD07)));
    goto loc_00B7F0B2;
loc_00B7F07E:
    v_stack_mE8 = *(uint64_t *)(v_rip + 0x38CCDB);
    v_stack_mF0 = Arg1 + 120;
    v_stack_mF8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x64)));
    result = PopDiagTracePreSleepNotification((uint32_t)(*(uint32_t *)(arg1 + 0x20)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CCDB)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CCC1)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CCCC)));
loc_00B7F0B2:
    result = PopCheckpointSystemSleep(16, (uint32_t)(*(uint32_t *)(v_rip + 0x38CCDB)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CCC1)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CCCC)));
    result = PopUmpoSendFlushSleepStudyLoggerNotification(16, (uint32_t)(*(uint32_t *)(v_rip + 0x38CCDB)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CCC1)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CCCC)));
loc_00B7F0C1:
    result = PopEsEnterSleepShutdown(16, (uint32_t)(*(uint32_t *)(v_rip + 0x38CCDB)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CCC1)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CCCC)));
    result = PopThermalSxEntry(16, (uint32_t)(*(uint32_t *)(v_rip + 0x38CCDB)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CCC1)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CCCC)));
    result = PopFanSxEntry(16, (uint32_t)(*(uint32_t *)(v_rip + 0x38CCDB)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CCC1)), (uint32_t)(*(uint32_t *)(v_rip + 0x38CCCC)));
    if ((*(uint8_t *)(arg1 + 0xC)) != 0) goto loc_00B7F129;
    if ((*(uint8_t *)(v_rip + 0x38CC65)) != 0) {
        Arg3 = 0;
        v_stack_p8 = 1;
        result = v_stack_p8;
        v_stack_m78 = 5;
        v_stack_m70 = result;
        Arg1 = v_stack_m78;
        v_stack_m68 = 1;
        Arg2 = Arg3 + 2;
        v_stack_m60 = 11;
        v_stack_m58 = result;
        v_stack_m50 = 4;
        result = RtlSetSystemBootStatusEx(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0x38CCCC)));
    }
    *(uint8_t *)(arg1 + 0xC) = 1;
loc_00B7F129:
    if ((*(uint8_t *)(arg1 + 0x18)) == 0) {
        Arg1 = *(uint32_t *)(v_rip + 0x38CC32);
    }
    result = PopFlushVolumes(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0x38CCCC)));
    if ((*(uint32_t *)(v_rip + 0x38CC29)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38CC27))))) {
        *(uint32_t *)(v_rip + 0x38CC21) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38CC27)));
    }
    *(uint8_t *)(v_rip + 0x38CC02) = 2;
    if ((*(uint8_t *)(v_rip + 0x38CBE8)) != 0) goto loc_00B7FBE8;
    *(uint8_t *)(v_rip + 0x391D8B) = 0;
    result = PopInitSystemSleeperThread((uint32_t)(*(uint32_t *)(arg1 + 0x34)), Arg1 + 224, v_stack_m98, (uint32_t)(*(uint32_t *)(v_rip + 0x38CCCC)));
    *(uint32_t *)(arg1 + 0x58) = (uint32_t)(result);
    if (!sign_flag) goto loc_00B7F199;
    *(uint32_t *)(arg1 + 0x6C) = 20;
    goto loc_00B7EE74;
loc_00B7F199:
    if ((*(uint8_t *)(v_rip + 0x38CC60)) == 0) {
        result = ExWakeTimersPause((uint32_t)(*(uint32_t *)(arg1 + 0x34)), Arg1 + 224, v_stack_m98, (uint32_t)(*(uint32_t *)(v_rip + 0x38CCCC)));
        *(uint8_t *)(v_rip + 0x38CC52) = 1;
    }
    *(uint64_t *)(arg1 + 0x98) = result;
    *(uint64_t *)(arg1 + 0xA0) = *(uint64_t *)(local_r10);
    *(uint64_t *)(arg1 + 0xB8) = 0;
    if (*(uint64_t *)(v_rip + 0x38D6D5) != 0) goto loc_00B7F316;
    if ((*(uint64_t *)(v_rip + 0x38D6AF)) != 0) goto loc_00B7F316;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x38DCD6)) == 0) goto loc_00B7F25B;
    if ((*(uint32_t *)(v_rip + 0x38CB62)) != 5) goto loc_00B7F25B;
    if ((*(uint8_t *)(v_rip + 0x38CD4D)) != 0) goto loc_00B7F25B;
    if ((*(uint32_t *)(v_rip + 0x38CB36)) == ((uint32_t)(*(uint64_t *)(v_rip + 0x38D6D5) + 2))) goto loc_00B7F25B;
    if ((uint8_t)(Arg1 + 328) == 0) goto loc_00B7F25B;
    if ((Arg1 + 332) == -1) goto loc_00B7F25B;
    if ((Arg1 + 332) <= (*(uint64_t *)(local_r10))) goto loc_00B7F25B;
    local_rbx = (Arg1 + 332) - (*(uint64_t *)(local_r10));
    *(uint64_t *)(arg1 + 0x138) = local_rbx;
    Arg1 = (*(uint64_t *)(arg1 + 0x98)) + (local_rbx);
loc_00B7F244:
    *(void **)(arg1 + 0xB0) = Arg1;
    *(uint64_t *)(arg1 + 0xB8) = -2;
    goto loc_00B7F321;
loc_00B7F25B:
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x38DC06) + 0x58)) == 0) goto loc_00B7F2BA;
    if ((*(uint32_t *)(v_rip + 0x38CAFD)) == 5) goto loc_00B7F2BA;
    result = PopIsDozeSupported(v_rip + 3726408, Arg1 + 224, v_stack_m98, *(uint64_t *)(v_rip + 0x38DC06));
    if ((uint8_t)(result) == 0) goto loc_00B7F2BA;
    if (((*(uint32_t *)(v_rip + 0x38CAC1)) & (0x40000000ULL)) != 0) goto loc_00B7F2BA;
    *(uint64_t *)(arg1 + 0xB0) = *(uint64_t *)(arg1 + 0x98);
    Arg1 = (v_rip + 3726408) * ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x38DC06) + 0x58)));
    Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x98));
    *(void **)(arg1 + 0xB0) = Arg1;
    goto loc_00B7F321;
loc_00B7F2BA:
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x38DCD6)) == 0) goto loc_00B7F321;
    if ((*(uint32_t *)(v_rip + 0x38CAA6)) != 5) goto loc_00B7F321;
    if ((*(uint8_t *)(v_rip + 0x38CC91)) != 0) goto loc_00B7F321;
    if (*(uint64_t *)(v_rip + 0x38C9A0) == 0) goto loc_00B7F321;
    if ((*(uint32_t *)(v_rip + 0x38CA70)) != 11) goto loc_00B7F321;
    Arg2 = (*(uint64_t *)(v_rip + 0x38C9A0)) - (*(uint64_t *)(local_r10));
    *(uint64_t *)(arg1 + 0x138) = Arg2;
    Arg1 = (Arg1) * ((uint32_t)(*(uint32_t *)(v_rip + 0x445F82)));
    Arg2 = (Arg2) + (Arg1);
    Arg1 = (*(uint64_t *)(arg1 + 0x98)) + (Arg2);
    *(uint64_t *)(arg1 + 0x138) = Arg2;
    goto loc_00B7F244;
loc_00B7F316:
    *(uint64_t *)(arg1 + 0xB8) = -3;
loc_00B7F321:
    if ((*(uint64_t *)(arg1 + 0xB8)) != -1) goto loc_00B7F342;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x445F82));
    if ((*(uint64_t *)(v_rip + 0x38CADE)) == 0) {
        result = *(uint64_t *)(arg1 + 0x98);
        *(uint64_t *)(v_rip + 0x38CACE) = result;
    }
    Arg2 = 0;
    result = memset(v_rip + 3721837, Arg2, Arg2 + 72, *(uint64_t *)(v_rip + 0x38DC06));
    *(uint32_t *)(v_rip + 0x38CA4F) = 3;
    if ((*(uint64_t *)(arg1 + 0xB8)) != -3) goto loc_00B7F39E;
    *(uint64_t *)(v_rip + 0x38CA52) = -3;
    *(uint64_t *)(v_rip + 0x38CA3B) = *(uint64_t *)(v_rip + 0x38D6D5);
    *(uint64_t *)(v_rip + 0x38CA55) = *(uint64_t *)(arg1 + 0xB8);
    *(uint64_t *)(v_rip + 0x38CA37) = *(uint64_t *)(v_rip + 0x38D50E);
    goto loc_00B7F5A7;
loc_00B7F39E:
    if ((*(uint8_t *)(v_rip + 0x38CBBB)) != 0) goto loc_00B7F5A7;
    if ((*(uint32_t *)(v_rip + 0x38C9A2)) == 14) goto loc_00B7F5A7;
    if ((*(uint32_t *)(v_rip + 0x38C9AD)) != 5) goto loc_00B7F40F;
    if ((*(uint32_t *)(arg1 + 0x148)) == 1) goto loc_00B7F40F;
    if ((*(uint32_t *)(arg1 + 0x14C)) == 1) goto loc_00B7F40F;
    result = PopQueryPowerSettingUlong(v_rip - 11905758, Arg1 + 192, Arg1 + 196, *(uint64_t *)(v_rip + 0x38DC06));
    if ((*(uint32_t *)(arg1 + 0xC0)) != 0) goto loc_00B7F407;
    if ((*(uint32_t *)(arg1 + 0xC4)) != 0) {
    }
    if (*(uint64_t *)(arg1 + 0xB0) == 0) goto loc_00B7F4A3;
    if ((*(uint64_t *)(arg1 + 0xB8)) != -2) goto loc_00B7F468;
    result = *(uint64_t *)(arg1 + 0xB0);
    if ((*(uint32_t *)(arg1 + 0x148)) != 0) {
        *(uint64_t *)(v_rip + 0x38C983) = *(uint64_t *)(arg1 + 0xB0);
        result = *(uint64_t *)(arg1 + 0xB8);
        *(uint64_t *)(v_rip + 0x38C985) = result;
    }
    if ((*(uint32_t *)(arg1 + 0x14C)) == 0) goto loc_00B7F4A3;
    *(uint64_t *)(v_rip + 0x38C978) = *(uint64_t *)(arg1 + 0xB0);
    *(uint64_t *)(v_rip + 0x38C97A) = *(uint64_t *)(arg1 + 0xB8);
    goto loc_00B7F4A3;
loc_00B7F468:
loc_00B7F46F:
    *(uint64_t *)(v_rip + 0x38CA6D) = *(uint64_t *)(arg1 + 0xB0);
    local_rbx = (v_rip + 3721837) + (24);
    if (local_rbx < (v_rip + 3721593)) goto loc_00B7F46F;
loc_00B7F490:
    *(uint64_t *)(v_rip + 0x38C93F) = *(uint64_t *)(arg1 + 0xB8);
    Arg1 = (v_rip + 3721535) + (24);
    if (Arg1 < (v_rip + 3721576)) goto loc_00B7F490;
loc_00B7F4A3:
    *(uint64_t *)(arg1 + 0x40) = *(uint64_t *)(v_rip + 0x38C95E);
    if (*(uint64_t *)(v_rip + 0x38C95E) == 0) goto loc_00B7F4CF;
    result = (*(uint64_t *)(arg1 + 0x98)) + (0x1312D00ULL);
    if ((*(uint64_t *)(v_rip + 0x38C95E)) < result) {
        *(uint64_t *)(arg1 + 0x40) = result;
        Arg2 = result;
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x148))) == 0) goto loc_00B7F53C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x148)))) != 2) goto loc_00B7F4EF;
    if (sign_flag) goto loc_00B7F4EF;
    goto loc_00B7F4F2;
loc_00B7F4EF:
    Arg3 = 0;
loc_00B7F4F2:
    *(uint8_t *)(arg1 + 0xA9) = 0;
    v_stack_mF8 = Arg1 + 200;
    result = ExGetNextWakeTime(Arg2 + 1, *(uint64_t *)(arg1 + 0xB0), Arg3, Arg1 + 40);
    *(uint8_t *)(arg1 + 0x150) = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_00B7F547;
    *(uint64_t *)(v_rip + 0x38C888) = *(uint64_t *)(arg1 + 0x28);
    *(uint64_t *)(v_rip + 0x38C88E) = *(uint64_t *)(arg1 + 0xC8);
    goto loc_00B7F547;
loc_00B7F53C:
loc_00B7F547:
    local_r12 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14C))) == 0) goto loc_00B7F5A7;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14C)))) != 2) goto loc_00B7F564;
    if (sign_flag) {
        Arg3 = 0;
    }
    *(uint8_t *)(arg1 + 0xA9) = (uint8_t)(Arg3);
    Arg1 = (*(uint64_t *)(arg1 + 0x40)) + 1;
    v_stack_mF8 = Arg1 + 200;
    result = ExGetNextWakeTime(Arg1, *(uint64_t *)(arg1 + 0xB0), Arg3, Arg1 + 40);
    *(uint8_t *)(arg1 + 0x150) = (uint8_t)(result);
    if ((uint8_t)(result) != 0) {
        result = *(uint64_t *)(arg1 + 0x28);
        *(uint64_t *)(v_rip + 0x38C833) = result;
        result = *(uint64_t *)(arg1 + 0xC8);
        *(uint64_t *)(v_rip + 0x38C839) = result;
    }
    *(uint64_t *)(v_rip + 0x38C80B) = *(uint64_t *)(v_rip + 0x38C80A);
    if (*(uint64_t *)(v_rip + 0x38C80A) == 0) goto loc_00B7F5D4;
    Arg3 = ((uint32_t)(*(uint32_t *)(arg1 + 0x154))) + (*(uint64_t *)(arg1 + 0x98));
    if ((*(uint64_t *)(v_rip + 0x38C80A)) < Arg3) {
        *(uint64_t *)(v_rip + 0x38C7EC) = Arg3;
    }
    *(uint64_t *)(v_rip + 0x38C7F6) = *(uint64_t *)(v_rip + 0x38C7F5);
    if (*(uint64_t *)(v_rip + 0x38C7F5) == 0) goto loc_00B7F601;
    Arg3 = ((uint32_t)(*(uint32_t *)(arg1 + 0x154))) + (*(uint64_t *)(arg1 + 0x98));
    if ((*(uint64_t *)(v_rip + 0x38C7F5)) < Arg3) {
        *(uint64_t *)(v_rip + 0x38C7D7) = Arg3;
    }
    result = PopTransitionGetWakeTimerType(*(uint64_t *)(v_rip + 0x38C7C0), *(uint64_t *)(v_rip + 0x38C7F5), Arg3, Arg1 + 40);
    *(uint32_t *)(arg1 + 0x140) = (uint32_t)(result);
    result = PopTransitionGetWakeTimerType(*(uint64_t *)(v_rip + 0x38C7C6), *(uint64_t *)(v_rip + 0x38C7F5), Arg3, Arg1 + 40);
    Arg1 = 0;
    *(uint32_t *)(arg1 + 0x144) = (uint32_t)(result);
    result = KeQueryPerformanceCounter(Arg1, *(uint64_t *)(v_rip + 0x38C7F5), Arg3, Arg1 + 40);
    *(uint64_t *)(v_rip + 0x38CCDD) = result;
    result = ExAcquireTimeRefreshLockExclusive(Arg1, *(uint64_t *)(v_rip + 0x38C7F5), Arg3, Arg1 + 40);
    result = ExUpdateSystemTimeFromCmos(1, 1, Arg3, Arg1 + 40);
    result = ExReleaseTimeRefreshLockExclusive(1, 1, Arg3, Arg1 + 40);
    result = guard_dispatch_icall(*(uint64_t *)(v_rip + 0x38C762), *(uint64_t *)(v_rip + 0x38C781), Arg3, Arg1 + 40);
    *(uint8_t *)(v_rip + 0x28BF0E) = 0;
    result = PpmCheckPausePpmEngineForSx(*(uint64_t *)(v_rip + 0x38C762), *(uint64_t *)(v_rip + 0x38C781), Arg3, Arg1 + 40);
    result = PsLookupProcessByProcessId(v_stack_m98, v_stack_p20, Arg3, Arg1 + 40);
    result = PsLookupThreadByThreadId(v_stack_m90, v_stack_mC8, Arg3, Arg1 + 40);
    result = PopSetDevicesSystemState(v_stack_m90, v_stack_mC8, Arg3, Arg1 + 40);
    *(uint8_t *)(arg1 + 0x60) = 1;
    result = PopNewWakeInfo(v_stack_m90, v_stack_mC8, Arg3, Arg1 + 40);
    Arg4 = 0;
    Arg3 = 0;
    *(uint64_t *)(arg1 + 0x130) = result;
    *(uint32_t *)(arg1 + 0x70) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38D750)));
    v_stack_mF8 = 0;
    result = PopPushPowerStateTransitionRecordWithCallback(v_stack_p20, v_stack_mC8, Arg3, Arg4);
    Arg2 = 0;
    result = KeSetEvent(Arg1 + 248, Arg2, 1, Arg4);
    v_stack_mF8 = 0;
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(Arg1 + 272, Arg2, Arg3, Arg4);
    if (!(sign_flag)) {
        result = PoDelistPowerStateTransitionBlocker(Arg1 + 272, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(v_rip + 0x38C8FB) = 0;
    *(uint32_t *)(arg1 + 0x58) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x12C)));
    result = PopSetPowerActionWatchdogState(2, Arg2, Arg3, Arg4);
    Arg1 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38C63C))));
    if ((*(uint8_t *)(v_rip + 0x38CF56)) != 0) { Arg1 = *(uint32_t *)(v_rip + 0x38C63B); }
    *(uint32_t *)(v_rip + 0x38C639) = (uint32_t)(Arg1);
    *(uint64_t *)(v_rip + 0x2E8152) = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) & (8)) == 0) goto loc_00B7F753;
    *(uint32_t *)(arg1 + 0x20) = 6;
    goto loc_00B7F75D;
loc_00B7F753:
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38C63C)));
loc_00B7F75D:
    v_stack_mE8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x144)));
    *(uint32_t *)(arg1 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38C60B)));
    v_stack_mF0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x140)));
    v_stack_mF8 = *(uint64_t *)(v_rip + 0x38C645);
    result = PopDiagTracePostSleepNotification((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38C60F)))), (uint32_t)(*(uint32_t *)(v_rip + 0x38C5EC)), (uint32_t)(*(uint32_t *)(v_rip + 0x38C60B)), *(uint64_t *)(v_rip + 0x38C63E));
    if ((*(uint8_t *)(v_rip + 0x391768)) != 0) {
        result = PopDiagTraceMtrrError((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38C60F)))), (uint32_t)(*(uint32_t *)(v_rip + 0x38C5EC)), (uint32_t)(*(uint32_t *)(v_rip + 0x38C60B)), *(uint64_t *)(v_rip + 0x38C63E));
    }
    if (!sign_flag) goto loc_00B7EE74;
    if ((*(uint32_t *)(v_rip + 0x38C5AD)) != 5) goto loc_00B7EE74;
    v_stack_m88 = v_xmm0;
    result = StringCchPrintfW(v_rip + 3719205, 128, v_rip + 1921, (uint32_t)(*(uint32_t *)(arg1 + 0x58)));
    result = RtlInitUnicodeString(v_stack_m88, v_rip + 3719189, v_rip + 1921, (uint32_t)(*(uint32_t *)(arg1 + 0x58)));
    Arg3 = 0;
    result = IoRaiseInformationalHardError((uint32_t)(0xC0000411ULL), v_stack_m88, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x58)));
    result = PopDiagTraceHibernateErrorStatus((uint32_t)(*(uint32_t *)(arg1 + 0x58)), v_stack_m88, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x58)));
    goto loc_00B7EE74;
loc_00B7F812:
    local_r12 = 0;
    *(uint32_t *)(2) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38C60F)));
    *(uint32_t *)(arg1 + 0x58) = 0;
    goto loc_00B7EE6F;
loc_00B7F821:
    *(uint8_t *)(v_rip + 0x28BD50) = 1;
loc_00B7F828:
    result = PopCheckpointSystemSleep(56, v_stack_m88, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x58)));
    Arg2 = 0;
    Arg1 = 0;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x58)));
    v_stack_mF8 = 0;
    result = PopNotifyTelemetryOsState((uint32_t)(*(uint32_t *)(v_rip + 0x38C4EB)), (uint32_t)(*(uint32_t *)(v_rip + 0x38C519)), (uint32_t)(*(uint32_t *)(v_rip + 0x38C527)), (uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    *(uint32_t *)(arg1 + 0x64) = (uint32_t)(result);
    result = PopCancelIgnoreBatteryStatusChange((uint32_t)(*(uint32_t *)(v_rip + 0x38C4EB)), (uint32_t)(*(uint32_t *)(v_rip + 0x38C519)), (uint32_t)(*(uint32_t *)(v_rip + 0x38C527)), (uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    Arg4 = 0;
    Arg3 = 0;
    result = PopExecuteOnTargetProcessors(v_rip + 4487329, v_rip - 7009157, Arg3, Arg4);
    if ((*(uint8_t *)(arg1 + 0x30)) != 0) {
        result = PopReleasePolicyLock(v_rip + 4487329, v_rip - 7009157, Arg3, Arg4);
        *(uint8_t *)(arg1 + 0x30) = 0;
    }
    if ((*(uint8_t *)(arg1 + 0x60)) != 0) {
        result = PopProcessDeviceWakeSource(v_rip + 4487329, v_rip - 7009157, Arg3, Arg4);
    }
    result = PoClearBroadcast(v_rip + 4487329, v_rip - 7009157, Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x38C4DE) = 0;
    result = PopFanSxExit(v_rip + 4487329, v_rip - 7009157, Arg3, Arg4);
    result = PopEsExitSleep(v_rip + 4487329, v_rip - 7009157, Arg3, Arg4);
    *(uint32_t *)(arg1 + 0x74) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38D552)));
    *(uint64_t *)(v_rip + 0x38BE41) = 0;
    *(uint64_t *)(v_rip + 0x38BE32) = v_rip - 4322864;
    *(uint64_t *)(v_rip + 0x38BE1B) = 0;
    result = ExQueueWorkItem(v_rip + 3718719, 1, Arg3, Arg4);
    if ((*(uint32_t *)(arg1 + 0x58)) >= 0) {
        Arg1 = Arg1 + 120;
        result = PopCurrentPowerState(Arg1, 1, Arg3, Arg4);
    }
    if ((*(uint8_t *)(arg1 + 0x60)) != 0) {
        result = PopHandleWakeSources(Arg1, 1, Arg3, Arg4);
    }
    if ((*(uint32_t *)(arg1 + 0x58)) >= 0) {
        Arg4 = v_stack_p18;
        Arg3 = v_stack_mB8;
        Arg2 = v_stack_mB0;
        Arg1 = v_stack_p10;
        result = PopQueryMostRecentWakeSourceAttributes(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_p10;
        Arg4 = *(uint32_t *)(arg1 + 0x144);
        Arg3 = *(uint32_t *)(arg1 + 0x140);
        Arg2 = *(uint64_t *)(v_rip + 0x38C4A1);
        Arg1 = *(uint64_t *)(v_rip + 0x38C482);
        v_stack_mD8 = (uint32_t)(result);
        result = v_stack_mB8;
        v_stack_mE0 = result;
        result = v_stack_mB0;
        v_stack_mE8 = result;
        result = *(uint32_t *)(arg1 + 0x80);
        v_stack_mF0 = (uint32_t)(result);
        result = *(uint32_t *)(arg1 + 0x84);
        v_stack_mF8 = (uint32_t)(result);
        result = SshSessionManagerTracePostSleepNotification(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint8_t *)(arg1 + 0x30)) == 0) {
        result = PopAcquirePolicyLock(Arg1, Arg2, Arg3, Arg4);
        *(uint8_t *)(arg1 + 0x30) = 1;
    }
    if ((*(uint32_t *)(arg1 + 0x58)) < 0) goto loc_00B7FADF;
    result = PopUpdateSystemIdleContext(1, Arg2, Arg3, Arg4);
    result = PopPowerAggregatorNotifySystemWake((uint32_t)(*(uint32_t *)(arg1 + 0x1C)), Arg2, Arg3, Arg4);
    *(uint8_t *)(v_rip + 0x38C398) = 0;
    if (((int32_t)(*(uint32_t *)(v_rip + 0x38C411))) >= 3) goto loc_00B7FAC1;
    *(uint64_t *)(v_rip + 0x38C438) = *(uint64_t *)(v_rip - 0xB7F9BD + (int32_t)(*(uint32_t *)(v_rip + 0x38C411)) + (int32_t)(*(uint32_t *)(v_rip + 0x38C411)) * 2 * 8 + 0xF0BDC0);
    *(uint32_t *)(v_rip + 0x38D309) = 0;
    *(uint32_t *)(v_rip + 0x38CC9E) = 0;
    *(uint32_t *)(v_rip + 0x38CC9B) = 0;
    if ((*(uint64_t *)(v_rip - 0xB7F9BD + (int32_t)(*(uint32_t *)(v_rip + 0x38C411)) + (int32_t)(*(uint32_t *)(v_rip + 0x38C411)) * 2 * 8 + 0xF0BDC8)) != -1) goto loc_00B7FA38;
    result = PopDeferDoze((uint32_t)(*(uint32_t *)(arg1 + 0x148)), (uint32_t)(*(uint32_t *)(arg1 + 0x14C)), Arg1 + 120, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00B7FA1F;
    *(uint32_t *)(v_rip + 0x38C330) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    *(uint32_t *)(v_rip + 0x38C32B) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    goto loc_00B7FA2F;
loc_00B7FA1F:
    *(uint32_t *)(v_rip + 0x38C31F) = 2;
    *(uint32_t *)(v_rip + 0x38C319) = 5;
loc_00B7FA2F:
    goto loc_00B7FAA0;
loc_00B7FA38:
    if (((uint32_t)(*(uint32_t *)(arg1 + 0x4))) != -2) goto loc_00B7FA5E;
    if ((*(uint64_t *)(v_rip + 0x38C363)) != 0) goto loc_00B7FADF;
    *(uint64_t *)(v_rip + 0x38C34F) = *(uint64_t *)(v_rip + 0x38C346);
    goto loc_00B7FADF;
loc_00B7FA5E:
    if ((*(uint64_t *)(v_rip + 0x38C346)) != -3) goto loc_00B7FA74;
    *(uint64_t *)(v_rip + 0x38CE3D) = 0;
    *(uint64_t *)(v_rip + 0x38CE2E) = 0;
    goto loc_00B7FADF;
loc_00B7FA74:
    if ((*(uint32_t *)(v_rip + 0x38D391)) != 1) goto loc_00B7FAA9;
    if ((*(uint32_t *)(arg1 + 0x14C)) != 0) goto loc_00B7FADF;
    Arg2 = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x14C))) | (2));
    *(uint32_t *)(v_rip + 0x38C2B3) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    *(uint32_t *)(v_rip + 0x38C2AE) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    *(uint8_t *)(v_rip + 0x38C2A0) = (uint8_t)(Arg2);
loc_00B7FAA0:
    *(uint8_t *)(arg1 + 0xD8) = 0;
    goto loc_00B7FADF;
loc_00B7FAA9:
    if ((*(uint32_t *)(arg1 + 0x14C)) != 0) goto loc_00B7FADF;
    if ((*(uint32_t *)(arg1 + 0x70)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x74))))) goto loc_00B7FADF;
    result = PopCheckPowerSourceAfterRtcWakeSet((uint32_t)(*(uint32_t *)(arg1 + 0x148)), Arg2, Arg1 + 120, Arg4);
    goto loc_00B7FADF;
loc_00B7FAC1:
    result = PopIsMostRecentWakeAttended((uint32_t)(*(uint32_t *)(arg1 + 0x148)), Arg2, Arg1 + 120, Arg4);
    if ((uint8_t)(result) == 0) {
        *(uint32_t *)(v_rip + 0x38D217) = 0;
        *(uint32_t *)(v_rip + 0x38CBAC) = 0;
        *(uint32_t *)(v_rip + 0x38CBA9) = 0;
    }
    if ((*(uint8_t *)(v_rip + 0x38C31A)) == 0) goto loc_00B7FB04;
    if ((*(uint8_t *)(arg1 + 0xD8)) != 0) {
        result = ExWakeTimersResume((uint32_t)(*(uint32_t *)(arg1 + 0x148)), Arg2, Arg1 + 120, Arg4);
        *(uint8_t *)(v_rip + 0x38C303) = 0;
        *(uint64_t *)(v_rip + 0x38C304) = 0;
    }
    if ((*(uint8_t *)(v_rip + 0x38CB75)) != 0) {
        result = PopBootLoaderTraceProcess((uint32_t)(*(uint32_t *)(arg1 + 0x148)), Arg2, Arg1 + 120, Arg4);
    }
    *(uint8_t *)(v_rip + 0x38C447) = 0;
    result = PopResetActionDefaults((uint32_t)(*(uint32_t *)(arg1 + 0x148)), Arg2, Arg1 + 120, Arg4);
    result = PopSetPowerActionState(2, Arg2, Arg1 + 120, Arg4);
    result = PopReleasePolicyLock(2, Arg2, Arg1 + 120, Arg4);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x38CB53));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x38CB53))) != 0) {
        Arg1 = *(uint32_t *)(v_rip + 0x38CB4D);
        result = PoSetUserPresent(Arg1, Arg2, Arg1 + 120, Arg4);
    }
    result = ExQueueWorkItem(v_rip + 3718292, 1, Arg1 + 120, Arg4);
    result = PopCheckForWork(v_rip + 3718292, 1, Arg1 + 120, Arg4);
    if ((*(uint32_t *)(arg1 + 0x58)) >= 0) {
        result = PpmPerfReApplyStates(v_rip + 3718292, 1, Arg1 + 120, Arg4);
    }
    Arg1 = 0;
    *(uint32_t *)(v_rip + 0x38C1E7) = 17;
    result = KeQueryPerformanceCounter(Arg1, 1, Arg1 + 120, Arg4);
    result = (result) - (*(uint64_t *)(v_rip + 0x387BF7));
    *(uint64_t *)(v_rip + 0x38C930) = result;
    if (*(uint64_t *)(arg1 + 0xC8) != 0) {
        result = ExDeleteWakeTimerInfo(*(uint64_t *)(arg1 + 0xC8), 1, Arg1 + 120, Arg4);
        *(uint64_t *)(arg1 + 0xC8) = 0;
    }
    *(uint64_t *)(v_rip + 0x2E7CF1) = 0;
loc_00B7FBA7:
    if (v_stack_p20 != 0) {
        Arg1 = v_stack_p20;
        result = ObfDereferenceObject(Arg1, 1, Arg1 + 120, Arg4);
    }
    if (v_stack_mC8 != 0) {
        Arg1 = v_stack_mC8;
        result = ObfDereferenceObject(Arg1, 1, Arg1 + 120, Arg4);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x6C))) != 0) {
        Arg1 = *(uint32_t *)(arg1 + 0x58);
        result = PopDiagTraceStateTransitionFailurePoint(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x6C)), Arg1 + 120, Arg4);
    }
    local_rsp = (local_rsp) + (216);
    return (uint32_t)(*(uint32_t *)(arg1 + 0x58));
loc_00B7FBE8:
    result = PopFxPrepareDevicesForShutdown(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x6C)), Arg1 + 120, Arg4);
    Arg1 = (*(uint64_t *)(v_rip + 0x38C194)) + (48);
    result = IoFreePoDeviceNotifyList(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x6C)), Arg1 + 120, Arg4);
    if ((*(uint32_t *)(v_rip + 0x38C151)) == ((uint32_t)(v_stack_p20))) {
        *(uint8_t *)(v_rip + 0x446EF2) = 1;
    }
    result = PopTransitionCheckpoint(8, (uint32_t)((uint32_t)(v_stack_p20)), Arg1 + 120, Arg4);
    result = PopGracefulShutdown(8, (uint32_t)((uint32_t)(v_stack_p20)), Arg1 + 120, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `8` | `W` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `8` | `R` |
| `Arg1` | `+ 0xC` | `8` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `8` | `R` |
| `Arg1` | `+ 0x18` | `8` | `W` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `W` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `W` |
| `Arg1` | `+ 0x24` | `8` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `8` | `R` |
| `Arg1` | `+ 0x30` | `8` | `W` |
| `Arg1` | `+ 0x34` | `32` | `R` |
| `Arg1` | `+ 0x34` | `32` | `W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `W` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x58` | `32` | `R` |
| `Arg1` | `+ 0x58` | `32` | `R/W` |
| `Arg1` | `+ 0x58` | `32` | `W` |
| `Arg1` | `+ 0x5C` | `32` | `W` |
| `Arg1` | `+ 0x60` | `8` | `R` |

추가 오프셋 53개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B7E8C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
