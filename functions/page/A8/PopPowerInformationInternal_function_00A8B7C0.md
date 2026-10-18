# PopPowerInformationInternal

- RVA: `0x00A8B7C0`–`0x00A8D46F` (길이 `7,343` bytes)
- VA: `0x0000000140A8B7C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B8754`
- 디코드: `1,771`개 명령, `7,343/7,343` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **150**; 고유 호출 대상: **96**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **58**

### Outgoing calls
- `0x00A8B882` → [Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline_function_004F5DA0.md) (function, `0x004F5DA0`)
- `0x00A8B8B5` → [EtwpCoverageUserIsAdmin](../9F/EtwpCoverageUserIsAdmin_function_009FE548.md) (function, `0x009FE548`)
- `0x00A8B8C9` → [PopCheckTestsigningEnabled](../75/PopCheckTestsigningEnabled_function_00753FE0.md) (function, `0x00753FE0`)
- `0x00A8B8F2` → [PopIsRunningAsLocalSystem](PopIsRunningAsLocalSystem_function_00A88594.md) (function, `0x00A88594`)
- `0x00A8B90D` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00A8B92C` → [PopCheckTestsigningEnabled](../75/PopCheckTestsigningEnabled_function_00753FE0.md) (function, `0x00753FE0`)
- `0x00A8B939` → [EtwpCoverageUserIsAdmin](../9F/EtwpCoverageUserIsAdmin_function_009FE548.md) (function, `0x009FE548`)
- `0x00A8B95E` → [PopAcquireTransitionLock](../AA/PopAcquireTransitionLock_function_00AA9E7C.md) (function, `0x00AA9E7C`)
- `0x00A8B96E` → [PopReadPagesFromHiberFile](../AC/PopReadPagesFromHiberFile_function_00AC8F78.md) (function, `0x00AC8F78`)
- `0x00A8B97A` → [PopReleaseTransitionLock](../AB/PopReleaseTransitionLock_function_00ABDABC.md) (function, `0x00ABDABC`)
- `0x00A8B996` → [PopIsRunningAsLocalSystem](PopIsRunningAsLocalSystem_function_00A88594.md) (function, `0x00A88594`)
- `0x00A8B9A5` → [PopCheckTestsigningEnabled](../75/PopCheckTestsigningEnabled_function_00753FE0.md) (function, `0x00753FE0`)
- `0x00A8B9B2` → [EtwpCoverageUserIsAdmin](../9F/EtwpCoverageUserIsAdmin_function_009FE548.md) (function, `0x009FE548`)
- `0x00A8BA19` → [RtlCapabilityCheckForSingleSessionSku](../78/RtlCapabilityCheckForSingleSessionSku_function_0078E410.md) (function, `0x0078E410`)
- `0x00A8BAF4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8BB0D` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (function, `0x0049BF40`)
- `0x00A8BB16` → [RtlIsMultiSessionSku](../A2/RtlIsMultiSessionSku_function_00A20730.md) (function, `0x00A20730`)
- `0x00A8BB63` → [PopUpdateSmartUserPresencePredictions](../76/PopUpdateSmartUserPresencePredictions_function_0076894C.md) (function, `0x0076894C`)
- `0x00A8BB9B` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00A8BBC0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8BBD4` → [PopS0LowPowerIdleInfo](../A7/PopS0LowPowerIdleInfo_function_00A7C330.md) (function, `0x00A7C330`)
- `0x00A8BBE7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A8BC29` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8BC40` → [PopFxPlatformRegisterInterface](../70/PopFxPlatformRegisterInterface_function_007030FC.md) (function, `0x007030FC`)
- `0x00A8BC78` → [PoLatencySensitivityHint](../../text/3B/PoLatencySensitivityHint_function_003BE9B0.md) (function, `0x003BE9B0`)
- `0x00A8BCC4` → [TtmNotifySessionPowerStateChange](../98/TtmNotifySessionPowerStateChange_function_0098A8F4.md) (function, `0x0098A8F4`)
- `0x00A8BCD9` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00A8BCE6` → [PopSetDisplayStatus](../91/PopSetDisplayStatus_function_009129E0.md) (function, `0x009129E0`)
- `0x00A8BCED` → [PopUpdateConsoleDisplayState](../A3/PopUpdateConsoleDisplayState_function_00A31298.md) (function, `0x00A31298`)
- `0x00A8BCF7` → [PopPowerAggregatorNotifyDisplayPoweredOn](../70/PopPowerAggregatorNotifyDisplayPoweredOn_function_007003C4.md) (function, `0x007003C4`)
- `0x00A8BD0F` → [PopDiagTraceSessionDisplayStateChange](../../text/4B/PopDiagTraceSessionDisplayStateChange_function_004B7C00.md) (function, `0x004B7C00`)
- `0x00A8BD17` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00A8BD21` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (function, `0x0049BF40`)
- `0x00A8BD4B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8BD5F` → [PopQueryBootSessionStandbyActivationInfo](../../text/43/PopQueryBootSessionStandbyActivationInfo_function_0043AD74.md) (function, `0x0043AD74`)
- `0x00A8BD90` → [PopUpdateBackgroundCoolingStatus](../AD/PopUpdateBackgroundCoolingStatus_function_00AD5890.md) (function, `0x00AD5890`)
- `0x00A8BDBD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8BE0D` → [PopNetUpdateStandbyRequest](../AD/PopNetUpdateStandbyRequest_function_00ADB704.md) (function, `0x00ADB704`)
- `0x00A8BE34` → [TtmNotifySessionTerminalInput](../98/TtmNotifySessionTerminalInput_function_0098A984.md) (function, `0x0098A984`)
- `0x00A8BE8F` → [PopScreenOn](../76/PopScreenOn_function_007697E0.md) (function, `0x007697E0`)
- `0x00A8BE9E` → [PopScreenOff](../98/PopScreenOff_function_0098A758.md) (function, `0x0098A758`)
- `0x00A8BEFA` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00A8BF06` → [PopDiagTraceEventNoPayload](../../text/49/PopDiagTraceEventNoPayload_function_004982F8.md) (function, `0x004982F8`)
- `0x00A8BF51` → [PopBroadcastSessionInfo](../91/PopBroadcastSessionInfo_function_00912598.md) (function, `0x00912598`)
- `0x00A8BF68` → [PopUpdateExternalDisplayState](../76/PopUpdateExternalDisplayState_function_0076C0DC.md) (function, `0x0076C0DC`)
- `0x00A8BF95` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8C03F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8C05C` → [PopSetWatchdog](../../text/46/PopSetWatchdog_function_00460CAC.md) (function, `0x00460CAC`)
- `0x00A8C099` → [PpmAcquireLock](../../text/2D/PpmAcquireLock_function_002D9AA4.md) (function, `0x002D9AA4`)
- `0x00A8C0EA` → [PpmPerfUpdateDomainPolicy](../A9/PpmPerfUpdateDomainPolicy_function_00A97030.md) (function, `0x00A97030`)
- `0x00A8C0FB` → [PpmReleaseLock](../../text/2D/PpmReleaseLock_function_002DA428.md) (function, `0x002DA428`)
- `0x00A8C14A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8C1B0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8C20F` → [PopSetPowerSettingValueAcDc](../91/PopSetPowerSettingValueAcDc_function_00914D6C.md) (function, `0x00914D6C`)
- `0x00A8C232` → [PopTransitionCheckpoint](PopTransitionCheckpoint_function_00A8F3E8.md) (function, `0x00A8F3E8`)
- `0x00A8C2A2` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00A8C2B4` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)
- `0x00A8C2BB` → [PopEsQueueStateEvaluation](../A4/PopEsQueueStateEvaluation_function_00A4A398.md) (function, `0x00A4A398`)
- `0x00A8C2E8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8C356` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8C3C5` → [PopDeepSleepSetDisengageReason](../../text/38/PopDeepSleepSetDisengageReason_function_0038FEC4.md) (function, `0x0038FEC4`)
- `0x00A8C3CF` → [PopDeepSleepClearDisengageReason](../../text/39/PopDeepSleepClearDisengageReason_function_0039010C.md) (function, `0x0039010C`)
- `0x00A8C433` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8C471` → [PopBootStatGet](../A4/PopBootStatGet_function_00A4C398.md) (function, `0x00A4C398`)
- `0x00A8C489` → [PopBootStatSet](../A4/PopBootStatSet_function_00A4C77C.md) (function, `0x00A4C77C`)
- `0x00A8C49E` → [PopBootStatCheckIntegrity](../AC/PopBootStatCheckIntegrity_function_00ACDF4C.md) (function, `0x00ACDF4C`)
- `0x00A8C4AA` → [PopBootStatRestoreDefaults](../AC/PopBootStatRestoreDefaults_function_00AC38E8.md) (function, `0x00AC38E8`)
- `0x00A8C4B6` → [PopBootStatUnlock](../6F/PopBootStatUnlock_function_006FE704.md) (function, `0x006FE704`)
- `0x00A8C516` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8C59D` → [PpmInternalProcessorIdleVeto](../../text/4E/PpmInternalProcessorIdleVeto_function_004E3F00.md) (function, `0x004E3F00`)
- `0x00A8C5C5` → [PopPowerRequestNotifyUserSessionAttributed](../AD/PopPowerRequestNotifyUserSessionAttributed_function_00ADF48C.md) (function, `0x00ADF48C`)
- `0x00A8C5E0` → [PoUserShutdownInitiated](../AB/PoUserShutdownInitiated_function_00AB81D0.md) (function, `0x00AB81D0`)
- `0x00A8C5EA` → [PoUserShutdownCancelled](../70/PoUserShutdownCancelled_function_007051C0.md) (function, `0x007051C0`)
- `0x00A8C617` → [RtlCheckTokenMembership](../../text/3A/RtlCheckTokenMembership_function_003A5A10.md) (function, `0x003A5A10`)
- `0x00A8C633` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (function, `0x0049BF40`)
- `0x00A8C651` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (function, `0x004575EC`)
- `0x00A8C680` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00A8C69B` → [RtlStringCbCopyW](../../text/43/RtlStringCbCopyW_function_0043B910.md) (function, `0x0043B910`)
- `0x00A8C6DD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8C6FF` → [PpmPerfGetBrandedFrequency](../AD/PpmPerfGetBrandedFrequency_function_00AD4900.md) (function, `0x00AD4900`)
- `0x00A8C739` → [PpmInternalPlatformIdleVeto](../../text/4F/PpmInternalPlatformIdleVeto_function_004FB6A8.md) (function, `0x004FB6A8`)
- `0x00A8C779` → [PopDirectedDripsUmPowerInformationInternal](../70/PopDirectedDripsUmPowerInformationInternal_function_007010E4.md) (function, `0x007010E4`)
- `0x00A8C7F7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8C82C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8C83F` → [PopQueryPowerButtonBugcheckEnabled](../AC/PopQueryPowerButtonBugcheckEnabled_function_00ACA4E4.md) (function, `0x00ACA4E4`)
- `0x00A8C8AB` → [PopAcquireTransitionLock](../AA/PopAcquireTransitionLock_function_00AA9E7C.md) (function, `0x00AA9E7C`)
- `0x00A8C8B8` → [PopReadResumeContext](../AC/PopReadResumeContext_function_00AC8E20.md) (function, `0x00AC8E20`)
- `0x00A8C8C4` → [PopReleaseTransitionLock](../AB/PopReleaseTransitionLock_function_00ABDABC.md) (function, `0x00ABDABC`)
- `0x00A8C8F7` → [PoDirectedDripsClearDeviceFlags](../../text/4F/PoDirectedDripsClearDeviceFlags_function_004FB540.md) (function, `0x004FB540`)
- `0x00A8C912` → [PoDirectedDripsSetDeviceFlags](../../text/4B/PoDirectedDripsSetDeviceFlags_function_004BD210.md) (function, `0x004BD210`)
- `0x00A8C92B` → [PopPlRegisterPowerPlane](../../text/4D/PopPlRegisterPowerPlane_function_004DB504.md) (function, `0x004DB504`)
- `0x00A8C98A` → [PopFxClearDeviceConstraints](../../text/4B/PopFxClearDeviceConstraints_function_004B05F8.md) (function, `0x004B05F8`)
- `0x00A8C9A9` → [SSHSupportQueryIsLibraryEnabled](../../text/4D/SSHSupportQueryIsLibraryEnabled_function_004D2F9C.md) (function, `0x004D2F9C`)
- `0x00A8C9D3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8CA05` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8CA3A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8CAAD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8CAC1` → [PpmPerfGetFrequencyBandStats](../A5/PpmPerfGetFrequencyBandStats_function_00A542B0.md) (function, `0x00A542B0`)
- `0x00A8CAE9` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00A8CAFE` → [PopDiagTraceSleepReliabilityDiagConfigUpdate](../70/PopDiagTraceSleepReliabilityDiagConfigUpdate_function_007025D8.md) (function, `0x007025D8`)
- `0x00A8CB0A` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)
- `0x00A8CB51` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8CB88` → [PpmPerfGetVmCppcConfig](../../text/5D/PpmPerfGetVmCppcConfig_function_005D41A8.md) (function, `0x005D41A8`)
- `0x00A8CB95` → [PpmPerfGetVmPerfConfig](../../text/4D/PpmPerfGetVmPerfConfig_function_004DE504.md) (function, `0x004DE504`)
- `0x00A8CBBC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8CBD2` → [PpmPerfGetVmPerfControlSupport](../AD/PpmPerfGetVmPerfControlSupport_function_00ADB2BC.md) (function, `0x00ADB2BC`)
- `0x00A8CC1D` → [PopUserPresenceHostStateChange](../91/PopUserPresenceHostStateChange_function_00912DB8.md) (function, `0x00912DB8`)
- `0x00A8CC62` → [PpmIdleGetConcurrencyStats](../A7/PpmIdleGetConcurrencyStats_function_00A798E4.md) (function, `0x00A798E4`)
- `0x00A8CCC1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8CCDB` → [PpmIdleGetPackageIdleIntervalStats](../A7/PpmIdleGetPackageIdleIntervalStats_function_00A7EE4C.md) (function, `0x00A7EE4C`)
- `0x00A8CD0B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8CD45` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A8CDD0` → [PopAdaptiveSetSystemInitiatedRebootTargetStateOverride](../76/PopAdaptiveSetSystemInitiatedRebootTargetStateOverride_function_0076B9F0.md) (function, `0x0076B9F0`)
- `0x00A8CE14` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00A8CE36` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00A8CE41` → [PopSessionWinlogonNotification](../76/PopSessionWinlogonNotification_function_0076BF60.md) (function, `0x0076BF60`)
- `0x00A8CE83` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00A8CE91` → [PopAdaptiveGetSessionState](../91/PopAdaptiveGetSessionState_function_00913894.md) (function, `0x00913894`)
- `0x00A8CEBE` → [PopAdaptiveGetSystemInitiatedRebootTargetState](../70/PopAdaptiveGetSystemInitiatedRebootTargetState_function_00701398.md) (function, `0x00701398`)
- `0x00A8CEFC` → [PpmPerfQueryProcMeasurementValues](../A9/PpmPerfQueryProcMeasurementValues_function_00A950C0.md) (function, `0x00A950C0`)
- `0x00A8CF2D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8CF69` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8CFA1` → [PpmPerfQueryProcMeasurementValues](../A9/PpmPerfQueryProcMeasurementValues_function_00A950C0.md) (function, `0x00A950C0`)
- `0x00A8CFC7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8CFE2` → [PopFanReadFanNoiseInfo](../A9/PopFanReadFanNoiseInfo_function_00A91138.md) (function, `0x00A91138`)
- `0x00A8D00E` → [PopManageTransitionRecordRequest](../A6/PopManageTransitionRecordRequest_function_00A63B34.md) (function, `0x00A63B34`)
- `0x00A8D037` → [PopShutdownListenerRemoveCallback](../../text/5D/PopShutdownListenerRemoveCallback_function_005D9310.md) (function, `0x005D9310`)
- `0x00A8D064` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8D0B5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8D0E2` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00A8D0FF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8D19E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8D1B5` → [PpmPerfGetVmPerfPriorityConfig](../../text/5D/PpmPerfGetVmPerfPriorityConfig_function_005D4454.md) (function, `0x005D4454`)
- `0x00A8D1E0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8D1F6` → [PpmPerfGetVmPerfPrioritySupport](../75/PpmPerfGetVmPerfPrioritySupport_function_0075AD28.md) (function, `0x0075AD28`)
- `0x00A8D222` → [PopHandleProvIdentifierRequest](../75/PopHandleProvIdentifierRequest_function_007581F8.md) (function, `0x007581F8`)
- `0x00A8D253` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A8D269` → [PopGetEnergyEstimationInfo](../../text/5C/PopGetEnergyEstimationInfo_function_005CEF20.md) (function, `0x005CEF20`)
- `0x00A8D2B0` → [PopSuspendResumeInvocation](../AA/PopSuspendResumeInvocation_function_00AAE544.md) (function, `0x00AAE544`)
- `0x00A8D2DC` → [Feature_Servicing_BatteryTestExempt__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_Servicing_BatteryTestExempt__private_IsEnabledDeviceUsageNoInline_function_005D12D8.md) (function, `0x005D12D8`)
- `0x00A8D308` → [PopBatteryUpdateTestExempt](../76/PopBatteryUpdateTestExempt_function_00766F54.md) (function, `0x00766F54`)
- `0x00A8D312` → [Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline_function_004F5DA0.md) (function, `0x004F5DA0`)
- `0x00A8D32C` → [SeIsAppContainerOrIdentifyLevelContext](../A2/SeIsAppContainerOrIdentifyLevelContext_function_00A21A74.md) (function, `0x00A21A74`)
- `0x00A8D370` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00A8D382` → [PopSessionConnectionChangeV2](../76/PopSessionConnectionChangeV2_function_0076BEA8.md) (function, `0x0076BEA8`)
- `0x00A8D397` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00A8D3B4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A8D3EB` → [Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline_function_004F5DA0.md) (function, `0x004F5DA0`)
- `0x00A8D43E` → [PopNotifyWin32kRequestStatus](PopNotifyWin32kRequestStatus_function_00A80220.md) (function, `0x00A80220`)
- `0x00A8D44F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x00957B84`

### Static image references
- `0x00A8B7DC` → RVA `0x00E0A740` (`.data`; read)
- `0x00A8B906` → RVA `0x00FD9B30` (`PAGEDATA`; read)
- `0x00A8B9D0` → RVA `0x00B01CB0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A8BB52` → RVA `0x00F0CF0C` (`.data`; read)
- `0x00A8BB71` → RVA `0x00F0EAB9` (`.data`; write)
- `0x00A8BB78` → RVA `0x00F0EAB9` (`.data`; read)
- `0x00A8BB7F` → RVA `0x00020968` (`.rdata`; read)
- `0x00A8BDCD` → RVA `0x00E675C0` (`.data`; read)
- `0x00A8BDD7` → RVA `0x00E675D0` (`.data`; read)
- `0x00A8BEBB` → RVA `0x00F0EAB8` (`.data`; read)
- `0x00A8BEE1` → RVA `0x000208E8` (`.rdata`; read)
- `0x00A8BEF3` → RVA `0x00F0EAB8` (`.data`; write)
- `0x00A8BEFF` → RVA `0x0001E2E8` (`.rdata`; read)
- `0x00A8BFA5` → RVA `0x00E67560` (`.data`; read)
- `0x00A8BFAF` → RVA `0x00E67570` (`.data`; read)
- `0x00A8BFBA` → RVA `0x00E67580` (`.data`; read)
- `0x00A8BFC5` → RVA `0x00E67590` (`.data`; read)
- `0x00A8C011` → RVA `0x00E67554` (`.data`; write)
- `0x00A8C017` → RVA `0x00E67558` (`.data`; write)
- `0x00A8C092` → RVA `0x00F0CC00` (`.data`; read)
- `0x00A8C09E` → RVA `0x00FC6CD0` (`ALMOSTRO`; read)
- `0x00A8C0B8` → RVA `0x00FC6CD0` (`ALMOSTRO`; write)
- `0x00A8C15D` → RVA `0x00FC6B6C` (`ALMOSTRO`; read)
- `0x00A8C165` → RVA `0x00FC6ADC` (`ALMOSTRO`; read)
- `0x00A8C16E` → RVA `0x00FC6DA8` (`ALMOSTRO`; read)
- `0x00A8C1C0` → RVA `0x00E67430` (`.data`; read)
- `0x00A8C1CA` → RVA `0x00E67440` (`.data`; read)
- `0x00A8C1D5` → RVA `0x00E67450` (`.data`; read)
- `0x00A8C208` → RVA `0x00011A18` (`.rdata`; read)
- `0x00A8C29B` → RVA `0x00F08440` (`.data`; read)
- `0x00A8C2AE` → RVA `0x00F08410` (`.data`; write)
- `0x00A8C2FB` → RVA `0x00F0BD44` (`.data`; read)
- `0x00A8C3ED` → RVA `0x0001E0F8` (`.rdata`; read)
- `0x00A8C526` → RVA `0x00E675A0` (`.data`; read)
- `0x00A8C530` → RVA `0x00E675B0` (`.data`; read)
- `0x00A8C60A` → RVA `0x00F0CFB0` (`.data`; read)
- `0x00A8C689` → RVA `0x00F0E7A0` (`.data`; write)
- `0x00A8C694` → RVA `0x00F0E7A0` (`.data`; read)
- `0x00A8C6A9` → RVA `0x00F0E820` (`.data`; write)
- `0x00A8C7CA` → RVA `0x00F0C8A8` (`.data`; write)
- `0x00A8C7D1` → RVA `0x00F0C8A0` (`.data`; write)
- `0x00A8C80A` → RVA `0x00E67464` (`.data`; read)
- `0x00A8C9B0` → RVA `0x00E01D90` (`.data`; read)
- `0x00A8CA18` → RVA `0x00E67470` (`.data`; read)
- `0x00A8CA4D` → RVA `0x00E0B3C8` (`.data`; read)
- `0x00A8CAE2` → RVA `0x00F08500` (`.data`; read)
- `0x00A8CAEE` → RVA `0x00FC6AFD` (`ALMOSTRO`; read)
- `0x00A8CAF8` → RVA `0x00FC6AFD` (`ALMOSTRO`; write)
- `0x00A8CBEF` → RVA `0x00E0B558` (`.data`; read)
- `0x00A8CD1E` → RVA `0x00FC6BA8` (`ALMOSTRO`; read)
- `0x00A8CEC3` → RVA `0x00FD8210` (`PAGEDATA`; write)
- `0x00A8CECA` → RVA `0x00FD8208` (`PAGEDATA`; write)
- `0x00A8D077` → RVA `0x00E6856C` (`.data`; read)
- `0x00A8D07F` → RVA `0x00E68568` (`.data`; read)
- `0x00A8D0E9` → RVA `0x00F0CED3` (`.data`; read)
- `0x00A8D109` → RVA `0x00F090E0` (`.data`; read)
- `0x00A8D113` → RVA `0x00F090F0` (`.data`; read)
- `0x00A8D39E` → RVA `0x00E67798` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **83**
  - `0x00A8B882` → [Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline_function_004F5DA0.md) (`PAGE` → `.text`)
  - `0x00A8BAF4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8BB0D` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (`PAGE` → `.text`)
  - `0x00A8BB9B` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
  - `0x00A8BBC0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8BBE7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A8BC29` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8BC78` → [PoLatencySensitivityHint](../../text/3B/PoLatencySensitivityHint_function_003BE9B0.md) (`PAGE` → `.text`)
  - `0x00A8BCD9` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00A8BD0F` → [PopDiagTraceSessionDisplayStateChange](../../text/4B/PopDiagTraceSessionDisplayStateChange_function_004B7C00.md) (`PAGE` → `.text`)
  - `0x00A8BD17` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x00A8BD21` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (`PAGE` → `.text`)
  - `0x00A8BD4B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8BD5F` → [PopQueryBootSessionStandbyActivationInfo](../../text/43/PopQueryBootSessionStandbyActivationInfo_function_0043AD74.md) (`PAGE` → `.text`)
  - `0x00A8BDBD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8BEFA` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
  - `0x00A8BF06` → [PopDiagTraceEventNoPayload](../../text/49/PopDiagTraceEventNoPayload_function_004982F8.md) (`PAGE` → `.text`)
  - `0x00A8BF95` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8C03F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8C05C` → [PopSetWatchdog](../../text/46/PopSetWatchdog_function_00460CAC.md) (`PAGE` → `.text`)
  - `0x00A8C099` → [PpmAcquireLock](../../text/2D/PpmAcquireLock_function_002D9AA4.md) (`PAGE` → `.text`)
  - `0x00A8C0FB` → [PpmReleaseLock](../../text/2D/PpmReleaseLock_function_002DA428.md) (`PAGE` → `.text`)
  - `0x00A8C14A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8C1B0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8C2A2` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00A8C2B4` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
  - `0x00A8C2E8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8C356` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8C3C5` → [PopDeepSleepSetDisengageReason](../../text/38/PopDeepSleepSetDisengageReason_function_0038FEC4.md) (`PAGE` → `.text`)
  - `0x00A8C3CF` → [PopDeepSleepClearDisengageReason](../../text/39/PopDeepSleepClearDisengageReason_function_0039010C.md) (`PAGE` → `.text`)
  - `0x00A8C433` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8C516` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8C59D` → [PpmInternalProcessorIdleVeto](../../text/4E/PpmInternalProcessorIdleVeto_function_004E3F00.md) (`PAGE` → `.text`)
  - `0x00A8C617` → [RtlCheckTokenMembership](../../text/3A/RtlCheckTokenMembership_function_003A5A10.md) (`PAGE` → `.text`)
  - `0x00A8C633` → [PopIsPlatformAoAcCapable](../../text/49/PopIsPlatformAoAcCapable_function_0049BF40.md) (`PAGE` → `.text`)
  - `0x00A8C651` → [RtlStringCbLengthW](../../text/45/RtlStringCbLengthW_function_004575EC.md) (`PAGE` → `.text`)
  - `0x00A8C680` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00A8C69B` → [RtlStringCbCopyW](../../text/43/RtlStringCbCopyW_function_0043B910.md) (`PAGE` → `.text`)
  - `0x00A8C6DD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8C739` → [PpmInternalPlatformIdleVeto](../../text/4F/PpmInternalPlatformIdleVeto_function_004FB6A8.md) (`PAGE` → `.text`)
  - `0x00A8C7F7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8C82C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8C8F7` → [PoDirectedDripsClearDeviceFlags](../../text/4F/PoDirectedDripsClearDeviceFlags_function_004FB540.md) (`PAGE` → `.text`)
  - `0x00A8C912` → [PoDirectedDripsSetDeviceFlags](../../text/4B/PoDirectedDripsSetDeviceFlags_function_004BD210.md) (`PAGE` → `.text`)
  - `0x00A8C92B` → [PopPlRegisterPowerPlane](../../text/4D/PopPlRegisterPowerPlane_function_004DB504.md) (`PAGE` → `.text`)
  - `0x00A8C98A` → [PopFxClearDeviceConstraints](../../text/4B/PopFxClearDeviceConstraints_function_004B05F8.md) (`PAGE` → `.text`)
  - `0x00A8C9A9` → [SSHSupportQueryIsLibraryEnabled](../../text/4D/SSHSupportQueryIsLibraryEnabled_function_004D2F9C.md) (`PAGE` → `.text`)
  - `0x00A8C9D3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8CA05` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8CA3A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8CAAD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8CAE9` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00A8CB0A` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
  - `0x00A8CB51` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8CB88` → [PpmPerfGetVmCppcConfig](../../text/5D/PpmPerfGetVmCppcConfig_function_005D41A8.md) (`PAGE` → `.text`)
  - `0x00A8CB95` → [PpmPerfGetVmPerfConfig](../../text/4D/PpmPerfGetVmPerfConfig_function_004DE504.md) (`PAGE` → `.text`)
  - `0x00A8CBBC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8CCC1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8CD0B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8CD45` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A8CE14` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00A8CE36` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00A8CE83` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00A8CF2D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8CF69` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8CFC7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8D037` → [PopShutdownListenerRemoveCallback](../../text/5D/PopShutdownListenerRemoveCallback_function_005D9310.md) (`PAGE` → `.text`)
  - `0x00A8D064` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8D0B5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8D0E2` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00A8D0FF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8D19E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8D1B5` → [PpmPerfGetVmPerfPriorityConfig](../../text/5D/PpmPerfGetVmPerfPriorityConfig_function_005D4454.md) (`PAGE` → `.text`)
  - `0x00A8D1E0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8D253` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A8D269` → [PopGetEnergyEstimationInfo](../../text/5C/PopGetEnergyEstimationInfo_function_005CEF20.md) (`PAGE` → `.text`)
  - `0x00A8D2DC` → [Feature_Servicing_BatteryTestExempt__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_Servicing_BatteryTestExempt__private_IsEnabledDeviceUsageNoInline_function_005D12D8.md) (`PAGE` → `.text`)
  - `0x00A8D312` → [Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline_function_004F5DA0.md) (`PAGE` → `.text`)
  - `0x00A8D370` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00A8D397` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00A8D3B4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A8D3EB` → [Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline_function_004F5DA0.md) (`PAGE` → `.text`)
  - `0x00A8D44F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A8B7C0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A8B7C5  55                              push rbp
00A8B7C6  56                              push rsi
00A8B7C7  57                              push rdi
00A8B7C8  41 54                           push r12
00A8B7CA  41 55                           push r13
00A8B7CC  41 56                           push r14
00A8B7CE  41 57                           push r15
00A8B7D0  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
00A8B7D5  48 81 EC B0 00 00 00            sub rsp, 0xb0
00A8B7DC  48 8B 05 5D EF 37 00            mov rax, qword ptr [rip + 0x37ef5d]
00A8B7E3  48 33 C4                        xor rax, rsp
00A8B7E6  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00A8B7EA  4C 8B 7D 77                     mov r15, qword ptr [rbp + 0x77]
00A8B7EE  0F 57 C0                        xorps xmm0, xmm0
00A8B7F1  4C 8B 65 7F                     mov r12, qword ptr [rbp + 0x7f]
00A8B7F5  8B D9                           mov ebx, ecx
00A8B7F7  4C 8B AD 87 00 00 00            mov r13, qword ptr [rbp + 0x87]
00A8B7FE  49 8B F8                        mov rdi, r8
00A8B801  48 8B 75 67                     mov rsi, qword ptr [rbp + 0x67]
00A8B805  0F 11 45 C7                     movups xmmword ptr [rbp - 0x39], xmm0
00A8B809  45 8B F1                        mov r14d, r9d
00A8B80C  45 33 C9                        xor r9d, r9d
00A8B80F  4D 89 0F                        mov qword ptr [r15], r9
00A8B812  45 89 0C 24                     mov dword ptr [r12], r9d
00A8B816  45 88 4D 00                     mov byte ptr [r13], r9b
00A8B81A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A8B823  45 8D 51 01                     lea r10d, [r9 + 1]
00A8B827  89 55 9F                        mov dword ptr [rbp - 0x61], edx
00A8B82A  44 88 4D 98                     mov byte ptr [rbp - 0x68], r9b
00A8B82E  44 88 4D 97                     mov byte ptr [rbp - 0x69], r9b
00A8B832  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
00A8B838  4C 89 4D AF                     mov qword ptr [rbp - 0x51], r9
00A8B83C  44 89 4D A7                     mov dword ptr [rbp - 0x59], r9d
00A8B840  4C 89 4D B7                     mov qword ptr [rbp - 0x49], r9
00A8B844  4C 89 4D BF                     mov qword ptr [rbp - 0x41], r9
00A8B848  44 89 4D AB                     mov dword ptr [rbp - 0x55], r9d
00A8B84C  4C 89 4D D7                     mov qword ptr [rbp - 0x29], r9
00A8B850  88 4D 99                        mov byte ptr [rbp - 0x67], cl
00A8B853  84 C9                           test cl, cl
00A8B855  0F 84 DB 01 00 00               je 0x140a8ba36
00A8B85B  83 FB 1C                        cmp ebx, 0x1c
00A8B85E  77 0A                           ja 0x140a8b86a
00A8B860  B8 05 01 B8 14                  mov eax, 0x14b80105
00A8B865  0F A3 D8                        bt eax, ebx
00A8B868  72 29                           jb 0x140a8b893
00A8B86A  8D 43 D8                        lea eax, [rbx - 0x28]
00A8B86D  83 F8 38                        cmp eax, 0x38
00A8B870  77 10                           ja 0x140a8b882
00A8B872  48 B9 03 00 8E 0A 00 82 80 01   movabs rcx, 0x18082000a8e0003
00A8B87C  48 0F A3 C1                     bt rcx, rax
00A8B880  72 11                           jb 0x140a8b893
00A8B882  E8 19 A5 A6 FF                  call 0x1404f5da0
00A8B887  45 33 C9                        xor r9d, r9d
00A8B88A  85 C0                           test eax, eax
00A8B88C  74 0F                           je 0x140a8b89d
00A8B88E  83 FB 62                        cmp ebx, 0x62
00A8B891  75 0A                           jne 0x140a8b89d
00A8B893  BB 22 00 00 C0                  mov ebx, 0xc0000022
00A8B898  E9 C0 01 00 00                  jmp 0x140a8ba5d
00A8B89D  8D 43 E3                        lea eax, [rbx - 0x1d]
00A8B8A0  83 F8 23                        cmp eax, 0x23
00A8B8A3  77 1C                           ja 0x140a8b8c1
00A8B8A5  48 B9 01 00 4C 8B 08 00 00 00   movabs rcx, 0x88b4c0001
00A8B8AF  48 0F A3 C1                     bt rcx, rax
00A8B8B3  73 0C                           jae 0x140a8b8c1
00A8B8B5  E8 8E 2C F7 FF                  call 0x1409fe548
00A8B8BA  45 33 C9                        xor r9d, r9d
00A8B8BD  84 C0                           test al, al
00A8B8BF  74 D2                           je 0x140a8b893
00A8B8C1  8D 43 AE                        lea eax, [rbx - 0x52]
00A8B8C4  83 F8 01                        cmp eax, 1
00A8B8C7  77 0C                           ja 0x140a8b8d5
00A8B8C9  E8 12 87 CC FF                  call 0x140753fe0
00A8B8CE  45 33 C9                        xor r9d, r9d
00A8B8D1  84 C0                           test al, al
00A8B8D3  74 BE                           je 0x140a8b893
00A8B8D5  83 FB 18                        cmp ebx, 0x18
00A8B8D8  74 18                           je 0x140a8b8f2
00A8B8DA  8D 43 DD                        lea eax, [rbx - 0x23]
00A8B8DD  83 F8 37                        cmp eax, 0x37
00A8B8E0  77 1C                           ja 0x140a8b8fe
00A8B8E2  48 B9 03 00 00 00 10 00 A0 00   movabs rcx, 0xa0001000000003
00A8B8EC  48 0F A3 C1                     bt rcx, rax
00A8B8F0  73 0C                           jae 0x140a8b8fe
00A8B8F2  E8 9D CC FF FF                  call 0x140a88594
00A8B8F7  45 33 C9                        xor r9d, r9d
00A8B8FA  84 C0                           test al, al
00A8B8FC  74 95                           je 0x140a8b893
00A8B8FE  83 FB 50                        cmp ebx, 0x50
00A8B901  75 24                           jne 0x140a8b927
00A8B903  8A 55 99                        mov dl, byte ptr [rbp - 0x67]
00A8B906  48 8B 0D 23 E2 54 00            mov rcx, qword ptr [rip + 0x54e223]
00A8B90D  E8 0E 65 DE FF                  call 0x140871e20
00A8B912  45 33 C9                        xor r9d, r9d
00A8B915  84 C0                           test al, al
00A8B917  0F 85 7B 15 00 00               jne 0x140a8ce98
00A8B91D  BB 61 00 00 C0                  mov ebx, 0xc0000061
00A8B922  E9 36 01 00 00                  jmp 0x140a8ba5d
00A8B927  83 FB 3D                        cmp ebx, 0x3d
00A8B92A  75 65                           jne 0x140a8b991
00A8B92C  E8 AF 86 CC FF                  call 0x140753fe0
00A8B931  84 C0                           test al, al
00A8B933  0F 84 5A FF FF FF               je 0x140a8b893
00A8B939  E8 0A 2C F7 FF                  call 0x1409fe548
00A8B93E  84 C0                           test al, al
00A8B940  0F 84 4D FF FF FF               je 0x140a8b893
00A8B946  41 83 FE 0C                     cmp r14d, 0xc
00A8B94A  0F 82 F8 01 00 00               jb 0x140a8bb48
00A8B950  48 85 F6                        test rsi, rsi
00A8B953  0F 84 7E 01 00 00               je 0x140a8bad7
00A8B959  B9 08 00 00 00                  mov ecx, 8
00A8B95E  E8 19 E5 01 00                  call 0x140aa9e7c
00A8B963  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00A8B966  4D 8B C7                        mov r8, r15
00A8B969  BA 01 00 00 00                  mov edx, 1
00A8B96E  E8 05 D6 03 00                  call 0x140ac8f78
00A8B973  B9 08 00 00 00                  mov ecx, 8
00A8B978  8B D8                           mov ebx, eax
00A8B97A  E8 3D 21 03 00                  call 0x140abdabc
00A8B97F  33 C0                           xor eax, eax
00A8B981  85 DB                           test ebx, ebx
00A8B983  0F 89 AC 0F 00 00               jns 0x140a8c935
00A8B989  49 89 07                        mov qword ptr [r15], rax
00A8B98C  E9 CC 00 00 00                  jmp 0x140a8ba5d
00A8B991  83 FB 2D                        cmp ebx, 0x2d
00A8B994  75 2E                           jne 0x140a8b9c4
00A8B996  E8 F9 CB FF FF                  call 0x140a88594
00A8B99B  33 DB                           xor ebx, ebx
00A8B99D  84 C0                           test al, al
00A8B99F  0F 85 2C 0C 00 00               jne 0x140a8c5d1
00A8B9A5  E8 36 86 CC FF                  call 0x140753fe0
00A8B9AA  84 C0                           test al, al
00A8B9AC  0F 84 E1 FE FF FF               je 0x140a8b893
00A8B9B2  E8 91 2B F7 FF                  call 0x1409fe548
00A8B9B7  84 C0                           test al, al
00A8B9B9  0F 85 12 0C 00 00               jne 0x140a8c5d1
00A8B9BF  E9 CF FE FF FF                  jmp 0x140a8b893
00A8B9C4  83 FB 19                        cmp ebx, 0x19
00A8B9C7  0F 85 98 00 00 00               jne 0x140a8ba65
00A8B9CD  0F 57 C0                        xorps xmm0, xmm0
00A8B9D0  4C 8D 15 D9 62 07 00            lea r10, [rip + 0x762d9]
00A8B9D7  B8 FF 7F 00 00                  mov eax, 0x7fff
00A8B9DC  8D 53 E9                        lea edx, [rbx - 0x17]
00A8B9DF  0F 11 45 C7                     movups xmmword ptr [rbp - 0x39], xmm0
00A8B9E3  44 8B C0                        mov r8d, eax
00A8B9E6  49 8B CA                        mov rcx, r10
00A8B9E9  66 44 39 09                     cmp word ptr [rcx], r9w
00A8B9ED  74 0B                           je 0x140a8b9fa
00A8B9EF  48 03 CA                        add rcx, rdx
00A8B9F2  49 83 E8 01                     sub r8, 1
00A8B9F6  75 F1                           jne 0x140a8b9e9
00A8B9F8  EB 15                           jmp 0x140a8ba0f
00A8B9FA  49 2B C0                        sub rax, r8
00A8B9FD  4C 89 55 CF                     mov qword ptr [rbp - 0x31], r10
00A8BA01  66 03 C0                        add ax, ax
00A8BA04  66 89 45 C7                     mov word ptr [rbp - 0x39], ax
00A8BA08  66 03 C2                        add ax, dx
00A8BA0B  66 89 45 C9                     mov word ptr [rbp - 0x37], ax
00A8BA0F  4C 8D 45 98                     lea r8, [rbp - 0x68]
00A8BA13  33 C9                           xor ecx, ecx
00A8BA15  48 8D 55 C7                     lea rdx, [rbp - 0x39]
00A8BA19  E8 F2 29 D0 FF                  call 0x14078e410
00A8BA1E  45 33 C9                        xor r9d, r9d
00A8BA21  8B D8                           mov ebx, eax
00A8BA23  85 C0                           test eax, eax
00A8BA25  78 36                           js 0x140a8ba5d
00A8BA27  44 38 4D 98                     cmp byte ptr [rbp - 0x68], r9b
00A8BA2B  0F 85 45 04 00 00               jne 0x140a8be76
00A8BA31  E9 5D FE FF FF                  jmp 0x140a8b893
00A8BA36  8D 43 E8                        lea eax, [rbx - 0x18]
00A8BA39  83 F8 3B                        cmp eax, 0x3b
00A8BA3C  77 10                           ja 0x140a8ba4e
00A8BA3E  49 B8 01 92 F0 69 11 81 00 0D   movabs r8, 0xd00811169f09201
00A8BA48  49 0F A3 C0                     bt r8, rax
00A8BA4C  72 0A                           jb 0x140a8ba58
00A8BA4E  83 FB 05                        cmp ebx, 5
00A8BA51  74 05                           je 0x140a8ba58
00A8BA53  83 FB 07                        cmp ebx, 7
00A8BA56  75 19                           jne 0x140a8ba71
00A8BA58  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00A8BA5D  8B C3                           mov eax, ebx
00A8BA5F  E9 E4 19 00 00                  jmp 0x140a8d448
00A8BA64  CC                              int3
00A8BA65  8B 55 9F                        mov edx, dword ptr [rbp - 0x61]
00A8BA68  41 BA 01 00 00 00               mov r10d, 1
00A8BA6E  8A 4D 99                        mov cl, byte ptr [rbp - 0x67]
00A8BA71  83 FB 36                        cmp ebx, 0x36
00A8BA74  0F 8F CF 0D 00 00               jg 0x140a8c849
00A8BA7A  0F 84 E9 0C 00 00               je 0x140a8c769
00A8BA80  83 FB 1F                        cmp ebx, 0x1f
00A8BA83  0F 8F B3 07 00 00               jg 0x140a8c23c
00A8BA89  0F 84 6A 09 00 00               je 0x140a8c3f9
00A8BA8F  83 FB 14                        cmp ebx, 0x14
00A8BA92  0F 8F A6 03 00 00               jg 0x140a8be3e
00A8BA98  0F 84 79 03 00 00               je 0x140a8be17
00A8BA9E  83 FB 05                        cmp ebx, 5
00A8BAA1  0F 8F DB 01 00 00               jg 0x140a8bc82
00A8BAA7  0F 84 B5 01 00 00               je 0x140a8bc62
00A8BAAD  85 DB                           test ebx, ebx
00A8BAAF  0F 84 51 01 00 00               je 0x140a8bc06
00A8BAB5  83 EB 01                        sub ebx, 1
00A8BAB8  0F 84 E9 00 00 00               je 0x140a8bba7
00A8BABE  83 EB 01                        sub ebx, 1
00A8BAC1  0F 84 AA 00 00 00               je 0x140a8bb71
00A8BAC7  83 EB 01                        sub ebx, 1
00A8BACA  74 71                           je 0x140a8bb3d
00A8BACC  83 FB 01                        cmp ebx, 1
00A8BACF  75 77                           jne 0x140a8bb48
00A8BAD1  41 83 FE 08                     cmp r14d, 8
00A8BAD5  73 0A                           jae 0x140a8bae1
00A8BAD7  BB 23 00 00 C0                  mov ebx, 0xc0000023
00A8BADC  E9 7C FF FF FF                  jmp 0x140a8ba5d
00A8BAE1  48 85 F6                        test rsi, rsi
00A8BAE4  74 F1                           je 0x140a8bad7
00A8BAE6  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8BAEC  49 8B D2                        mov rdx, r10
00A8BAEF  B9 00 01 00 00                  mov ecx, 0x100
00A8BAF4  E8 F7 65 0F 00                  call 0x140b820f0
00A8BAF9  33 FF                           xor edi, edi
00A8BAFB  48 8B D8                        mov rbx, rax
00A8BAFE  48 85 C0                        test rax, rax
00A8BB01  75 0A                           jne 0x140a8bb0d
00A8BB03  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A8BB08  E9 50 FF FF FF                  jmp 0x140a8ba5d
00A8BB0D  E8 2E 04 A1 FF                  call 0x14049bf40
00A8BB12  84 C0                           test al, al
00A8BB14  74 0B                           je 0x140a8bb21
00A8BB16  E8 15 4C F9 FF                  call 0x140a20730
00A8BB1B  84 C0                           test al, al
00A8BB1D  B0 01                           mov al, 1
00A8BB1F  75 03                           jne 0x140a8bb24
00A8BB21  40 8A C7                        mov al, dil
00A8BB24  88 03                           mov byte ptr [rbx], al
00A8BB26  49 89 1F                        mov qword ptr [r15], rbx
00A8BB29  41 C7 04 24 01 00 00 00         mov dword ptr [r12], 1
00A8BB31  41 C6 45 00 01                  mov byte ptr [r13], 1
00A8BB36  8B DF                           mov ebx, edi
00A8BB38  E9 20 FF FF FF                  jmp 0x140a8ba5d
00A8BB3D  41 83 FE 10                     cmp r14d, 0x10
00A8BB41  72 94                           jb 0x140a8bad7
00A8BB43  48 85 F6                        test rsi, rsi
00A8BB46  74 0A                           je 0x140a8bb52
00A8BB48  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A8BB4D  E9 0B FF FF FF                  jmp 0x140a8ba5d
00A8BB52  8B 05 B4 13 48 00               mov eax, dword ptr [rip + 0x4813b4]
00A8BB58  41 84 C2                        test r10b, al
00A8BB5B  74 EB                           je 0x140a8bb48
00A8BB5D  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00A8BB61  33 D2                           xor edx, edx
00A8BB63  E8 E4 CD CD FF                  call 0x14076894c
00A8BB68  33 C9                           xor ecx, ecx
00A8BB6A  8B D9                           mov ebx, ecx
00A8BB6C  E9 EC FE FF FF                  jmp 0x140a8ba5d
00A8BB71  44 88 15 41 2F 48 00            mov byte ptr [rip + 0x482f41], r10b
00A8BB78  48 8D 15 3A 2F 48 00            lea rdx, [rip + 0x482f3a]
00A8BB7F  48 8D 0D E2 4D 59 FF            lea rcx, [rip - 0xa6b21e]
00A8BB86  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
00A8BB8B  45 8B C2                        mov r8d, r10d
00A8BB8E  44 89 4C 24 28                  mov dword ptr [rsp + 0x28], r9d
00A8BB93  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00A8BB98  45 33 C9                        xor r9d, r9d
00A8BB9B  E8 70 51 C2 FF                  call 0x1406b0d10
00A8BBA0  8B D8                           mov ebx, eax
00A8BBA2  E9 B6 FE FF FF                  jmp 0x140a8ba5d
00A8BBA7  48 85 F6                        test rsi, rsi
00A8BBAA  0F 84 27 FF FF FF               je 0x140a8bad7
00A8BBB0  BA 08 00 00 00                  mov edx, 8
00A8BBB5  B9 00 01 00 00                  mov ecx, 0x100
00A8BBBA  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8BBC0  E8 2B 65 0F 00                  call 0x140b820f0
00A8BBC5  48 8B F8                        mov rdi, rax
00A8BBC8  48 85 C0                        test rax, rax
00A8BBCB  0F 84 32 FF FF FF               je 0x140a8bb03
00A8BBD1  48 8B C8                        mov rcx, rax
00A8BBD4  E8 57 07 FF FF                  call 0x140a7c330
00A8BBD9  8B D8                           mov ebx, eax
00A8BBDB  85 C0                           test eax, eax
00A8BBDD  79 12                           jns 0x140a8bbf1
00A8BBDF  BA 4D 65 6D 20                  mov edx, 0x206d654d
00A8BBE4  48 8B CF                        mov rcx, rdi
00A8BBE7  E8 84 6C 0F 00                  call 0x140b82870
00A8BBEC  E9 6C FE FF FF                  jmp 0x140a8ba5d
00A8BBF1  49 89 3F                        mov qword ptr [r15], rdi
00A8BBF4  41 C7 04 24 08 00 00 00         mov dword ptr [r12], 8
00A8BBFC  41 C6 45 00 01                  mov byte ptr [r13], 1
00A8BC01  E9 57 FE FF FF                  jmp 0x140a8ba5d
00A8BC06  41 83 FE 20                     cmp r14d, 0x20
00A8BC0A  0F 82 C7 FE FF FF               jb 0x140a8bad7
00A8BC10  48 85 F6                        test rsi, rsi
00A8BC13  0F 84 BE FE FF FF               je 0x140a8bad7
00A8BC19  BA 10 00 00 00                  mov edx, 0x10
00A8BC1E  B9 00 01 00 00                  mov ecx, 0x100
00A8BC23  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8BC29  E8 C2 64 0F 00                  call 0x140b820f0
00A8BC2E  48 8B F0                        mov rsi, rax
00A8BC31  48 85 C0                        test rax, rax
00A8BC34  0F 84 C9 FE FF FF               je 0x140a8bb03
00A8BC3A  48 8B D0                        mov rdx, rax
00A8BC3D  48 8B CF                        mov rcx, rdi
00A8BC40  E8 B7 74 C7 FF                  call 0x1407030fc
00A8BC45  8B D8                           mov ebx, eax
00A8BC47  85 C0                           test eax, eax
00A8BC49  79 0A                           jns 0x140a8bc55
00A8BC4B  BA 4D 65 6D 20                  mov edx, 0x206d654d
00A8BC50  48 8B CE                        mov rcx, rsi
00A8BC53  EB 92                           jmp 0x140a8bbe7
00A8BC55  49 89 37                        mov qword ptr [r15], rsi
00A8BC58  41 C7 04 24 10 00 00 00         mov dword ptr [r12], 0x10
00A8BC60  EB 9A                           jmp 0x140a8bbfc
00A8BC62  41 83 FE 0C                     cmp r14d, 0xc
00A8BC66  0F 82 6B FE FF FF               jb 0x140a8bad7
00A8BC6C  48 85 F6                        test rsi, rsi
00A8BC6F  0F 85 D3 FE FF FF               jne 0x140a8bb48
00A8BC75  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00A8BC78  E8 33 2D 93 FF                  call 0x1403be9b0
00A8BC7D  E9 E6 FE FF FF                  jmp 0x140a8bb68
00A8BC82  83 EB 06                        sub ebx, 6
00A8BC85  0F 84 6C 01 00 00               je 0x140a8bdf7
00A8BC8B  83 EB 01                        sub ebx, 1
00A8BC8E  0F 84 06 01 00 00               je 0x140a8bd9a
00A8BC94  83 EB 01                        sub ebx, 1
00A8BC97  0F 84 DD 00 00 00               je 0x140a8bd7a
00A8BC9D  83 EB 0A                        sub ebx, 0xa
00A8BCA0  74 7F                           je 0x140a8bd21
00A8BCA2  83 FB 01                        cmp ebx, 1
00A8BCA5  0F 85 9D FE FF FF               jne 0x140a8bb48
00A8BCAB  41 83 FE 14                     cmp r14d, 0x14
00A8BCAF  0F 85 93 FE FF FF               jne 0x140a8bb48
00A8BCB5  48 85 F6                        test rsi, rsi
00A8BCB8  0F 85 8A FE FF FF               jne 0x140a8bb48
00A8BCBE  8A 57 0C                        mov dl, byte ptr [rdi + 0xc]
00A8BCC1  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00A8BCC4  E8 2B EC EF FF                  call 0x14098a8f4
00A8BCC9  40 8A 77 0C                     mov sil, byte ptr [rdi + 0xc]
00A8BCCD  45 33 F6                        xor r14d, r14d
00A8BCD0  40 84 F6                        test sil, sil
00A8BCD3  41 8B DE                        mov ebx, r14d
00A8BCD6  0F 95 C3                        setne bl
00A8BCD9  E8 E2 C6 0E 00                  call 0x140b783c0
00A8BCDE  44 38 77 0D                     cmp byte ptr [rdi + 0xd], r14b
00A8BCE2  74 18                           je 0x140a8bcfc
00A8BCE4  8B CB                           mov ecx, ebx
00A8BCE6  E8 F5 6C E8 FF                  call 0x1409129e0
00A8BCEB  8B CB                           mov ecx, ebx
00A8BCED  E8 A6 55 FA FF                  call 0x140a31298
00A8BCF2  40 84 F6                        test sil, sil
00A8BCF5  74 05                           je 0x140a8bcfc
00A8BCF7  E8 C8 46 C7 FF                  call 0x1407003c4
00A8BCFC  44 38 77 0C                     cmp byte ptr [rdi + 0xc], r14b
00A8BD00  44 0F B6 47 0D                  movzx r8d, byte ptr [rdi + 0xd]
00A8BD05  44 8B 4F 10                     mov r9d, dword ptr [rdi + 0x10]
00A8BD09  0F 94 C1                        sete cl
00A8BD0C  8B 57 08                        mov edx, dword ptr [rdi + 8]
00A8BD0F  E8 EC BE A2 FF                  call 0x1404b7c00
00A8BD14  41 8B DE                        mov ebx, r14d
00A8BD17  E8 F4 C6 0E 00                  call 0x140b78410
00A8BD1C  E9 3C FD FF FF                  jmp 0x140a8ba5d
00A8BD21  E8 1A 02 A1 FF                  call 0x14049bf40
00A8BD26  84 C0                           test al, al
00A8BD28  0F 84 2A FD FF FF               je 0x140a8ba58
00A8BD2E  48 85 F6                        test rsi, rsi
00A8BD31  0F 84 A0 FD FF FF               je 0x140a8bad7
00A8BD37  41 BE 00 04 00 00               mov r14d, 0x400
00A8BD3D  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8BD43  41 8B D6                        mov edx, r14d
00A8BD46  B9 00 01 00 00                  mov ecx, 0x100
00A8BD4B  E8 A0 63 0F 00                  call 0x140b820f0
00A8BD50  48 8B F8                        mov rdi, rax
00A8BD53  48 85 C0                        test rax, rax
00A8BD56  0F 84 A7 FD FF FF               je 0x140a8bb03
00A8BD5C  48 8B C8                        mov rcx, rax
00A8BD5F  E8 10 F0 9A FF                  call 0x14043ad74
00A8BD64  8B D8                           mov ebx, eax
00A8BD66  85 C0                           test eax, eax
00A8BD68  0F 88 EF FC FF FF               js 0x140a8ba5d
00A8BD6E  49 89 3F                        mov qword ptr [r15], rdi
00A8BD71  45 89 34 24                     mov dword ptr [r12], r14d
00A8BD75  E9 82 FE FF FF                  jmp 0x140a8bbfc
00A8BD7A  41 83 FE 08                     cmp r14d, 8
00A8BD7E  0F 82 53 FD FF FF               jb 0x140a8bad7
00A8BD84  48 85 F6                        test rsi, rsi
00A8BD87  0F 85 BB FD FF FF               jne 0x140a8bb48
00A8BD8D  8A 4F 08                        mov cl, byte ptr [rdi + 8]
00A8BD90  E8 FB 9A 04 00                  call 0x140ad5890
00A8BD95  E9 06 FE FF FF                  jmp 0x140a8bba0
00A8BD9A  41 83 FE 08                     cmp r14d, 8
00A8BD9E  0F 82 33 FD FF FF               jb 0x140a8bad7
00A8BDA4  48 85 F6                        test rsi, rsi
00A8BDA7  0F 84 2A FD FF FF               je 0x140a8bad7
00A8BDAD  BA 20 00 00 00                  mov edx, 0x20
00A8BDB2  B9 00 01 00 00                  mov ecx, 0x100
00A8BDB7  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8BDBD  E8 2E 63 0F 00                  call 0x140b820f0
00A8BDC2  33 C9                           xor ecx, ecx
00A8BDC4  48 85 C0                        test rax, rax
00A8BDC7  0F 84 36 FD FF FF               je 0x140a8bb03
00A8BDCD  0F 10 05 EC B7 3D 00            movups xmm0, xmmword ptr [rip + 0x3db7ec]
00A8BDD4  0F 11 00                        movups xmmword ptr [rax], xmm0
00A8BDD7  0F 10 0D F2 B7 3D 00            movups xmm1, xmmword ptr [rip + 0x3db7f2]
00A8BDDE  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
00A8BDE2  49 89 07                        mov qword ptr [r15], rax
00A8BDE5  41 C7 04 24 20 00 00 00         mov dword ptr [r12], 0x20
00A8BDED  41 C6 45 00 01                  mov byte ptr [r13], 1
00A8BDF2  E9 73 FD FF FF                  jmp 0x140a8bb6a
00A8BDF7  41 83 FE 0C                     cmp r14d, 0xc
00A8BDFB  0F 82 D6 FC FF FF               jb 0x140a8bad7
00A8BE01  48 85 F6                        test rsi, rsi
00A8BE04  0F 85 3E FD FF FF               jne 0x140a8bb48
00A8BE0A  8A 4F 08                        mov cl, byte ptr [rdi + 8]
00A8BE0D  E8 F2 F8 04 00                  call 0x140adb704
00A8BE12  E9 89 FD FF FF                  jmp 0x140a8bba0
00A8BE17  41 83 FE 14                     cmp r14d, 0x14
00A8BE1B  0F 85 27 FD FF FF               jne 0x140a8bb48
00A8BE21  48 85 F6                        test rsi, rsi
00A8BE24  0F 85 1E FD FF FF               jne 0x140a8bb48
00A8BE2A  44 8A 47 10                     mov r8b, byte ptr [rdi + 0x10]
00A8BE2E  8B 57 0C                        mov edx, dword ptr [rdi + 0xc]
00A8BE31  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00A8BE34  E8 4B EB EF FF                  call 0x14098a984
00A8BE39  E9 2A FD FF FF                  jmp 0x140a8bb68
00A8BE3E  83 FB 1A                        cmp ebx, 0x1a
00A8BE41  0F 8F BE 02 00 00               jg 0x140a8c105
00A8BE47  0F 84 32 02 00 00               je 0x140a8c07f
00A8BE4D  83 EB 15                        sub ebx, 0x15
00A8BE50  0F 84 8A 01 00 00               je 0x140a8bfe0
00A8BE56  83 EB 01                        sub ebx, 1
00A8BE59  0F 84 13 01 00 00               je 0x140a8bf72
00A8BE5F  83 EB 01                        sub ebx, 1
00A8BE62  0F 84 F3 00 00 00               je 0x140a8bf5b
00A8BE68  83 EB 01                        sub ebx, 1
00A8BE6B  74 3B                           je 0x140a8bea8
00A8BE6D  83 FB 01                        cmp ebx, 1
00A8BE70  0F 85 D2 FC FF FF               jne 0x140a8bb48
00A8BE76  41 83 FE 0C                     cmp r14d, 0xc
00A8BE7A  0F 82 57 FC FF FF               jb 0x140a8bad7
00A8BE80  48 85 F6                        test rsi, rsi
00A8BE83  0F 85 BF FC FF FF               jne 0x140a8bb48
00A8BE89  44 38 4F 08                     cmp byte ptr [rdi + 8], r9b
00A8BE8D  74 0A                           je 0x140a8be99
00A8BE8F  E8 4C D9 CD FF                  call 0x1407697e0
00A8BE94  E9 CF FC FF FF                  jmp 0x140a8bb68
00A8BE99  B9 1E 00 00 00                  mov ecx, 0x1e
00A8BE9E  E8 B5 E8 EF FF                  call 0x14098a758
00A8BEA3  E9 C0 FC FF FF                  jmp 0x140a8bb68
00A8BEA8  41 83 FE 28                     cmp r14d, 0x28
00A8BEAC  0F 82 25 FC FF FF               jb 0x140a8bad7
00A8BEB2  48 85 F6                        test rsi, rsi
00A8BEB5  0F 85 8D FC FF FF               jne 0x140a8bb48
00A8BEBB  44 38 0D F6 2B 48 00            cmp byte ptr [rip + 0x482bf6], r9b
00A8BEC2  B8 FF FF FF FF                  mov eax, 0xffffffff
00A8BEC7  8B 4F 0C                        mov ecx, dword ptr [rdi + 0xc]
00A8BECA  75 41                           jne 0x140a8bf0d
00A8BECC  3B C8                           cmp ecx, eax
00A8BECE  74 45                           je 0x140a8bf15
00A8BED0  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
00A8BED5  48 8D 15 DC 2B 48 00            lea rdx, [rip + 0x482bdc]
00A8BEDC  44 89 4C 24 28                  mov dword ptr [rsp + 0x28], r9d
00A8BEE1  48 8D 0D 00 4A 59 FF            lea rcx, [rip - 0xa6b600]
00A8BEE8  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00A8BEED  45 8B C2                        mov r8d, r10d
00A8BEF0  45 33 C9                        xor r9d, r9d
00A8BEF3  44 88 15 BE 2B 48 00            mov byte ptr [rip + 0x482bbe], r10b
00A8BEFA  E8 11 4E C2 FF                  call 0x1406b0d10
00A8BEFF  48 8D 0D E2 23 59 FF            lea rcx, [rip - 0xa6dc1e]
00A8BF06  E8 ED C3 A0 FF                  call 0x1404982f8
00A8BF0B  EB 08                           jmp 0x140a8bf15
00A8BF0D  3B C8                           cmp ecx, eax
00A8BF0F  0F 84 43 FB FF FF               je 0x140a8ba58
00A8BF15  8B 47 08                        mov eax, dword ptr [rdi + 8]
00A8BF18  4C 8D 45 DF                     lea r8, [rbp - 0x21]
00A8BF1C  89 45 DF                        mov dword ptr [rbp - 0x21], eax
00A8BF1F  BA 20 00 00 00                  mov edx, 0x20
00A8BF24  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
00A8BF27  89 45 E3                        mov dword ptr [rbp - 0x1d], eax
00A8BF2A  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
00A8BF2D  89 45 E7                        mov dword ptr [rbp - 0x19], eax
00A8BF30  8D 4A E4                        lea ecx, [rdx - 0x1c]
00A8BF33  8B 47 14                        mov eax, dword ptr [rdi + 0x14]
00A8BF36  89 45 EB                        mov dword ptr [rbp - 0x15], eax
00A8BF39  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
00A8BF3C  89 45 EF                        mov dword ptr [rbp - 0x11], eax
00A8BF3F  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
00A8BF42  89 45 F3                        mov dword ptr [rbp - 0xd], eax
00A8BF45  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
00A8BF48  89 45 F7                        mov dword ptr [rbp - 9], eax
00A8BF4B  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
00A8BF4E  89 45 FB                        mov dword ptr [rbp - 5], eax
00A8BF51  E8 42 66 E8 FF                  call 0x140912598
00A8BF56  E9 0D FC FF FF                  jmp 0x140a8bb68
00A8BF5B  41 83 FE 0C                     cmp r14d, 0xc
00A8BF5F  0F 85 E3 FB FF FF               jne 0x140a8bb48
00A8BF65  8A 4F 08                        mov cl, byte ptr [rdi + 8]
00A8BF68  E8 6F 01 CE FF                  call 0x14076c0dc
00A8BF6D  E9 F6 FB FF FF                  jmp 0x140a8bb68
00A8BF72  41 83 FE 08                     cmp r14d, 8
00A8BF76  0F 82 5B FB FF FF               jb 0x140a8bad7
00A8BF7C  48 85 F6                        test rsi, rsi
00A8BF7F  0F 84 52 FB FF FF               je 0x140a8bad7
00A8BF85  BA 40 00 00 00                  mov edx, 0x40
00A8BF8A  B9 00 01 00 00                  mov ecx, 0x100
00A8BF8F  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8BF95  E8 56 61 0F 00                  call 0x140b820f0
00A8BF9A  33 C9                           xor ecx, ecx
00A8BF9C  48 85 C0                        test rax, rax
00A8BF9F  0F 84 5E FB FF FF               je 0x140a8bb03
00A8BFA5  0F 28 05 B4 B5 3D 00            movaps xmm0, xmmword ptr [rip + 0x3db5b4]
00A8BFAC  0F 11 00                        movups xmmword ptr [rax], xmm0
00A8BFAF  0F 28 0D BA B5 3D 00            movaps xmm1, xmmword ptr [rip + 0x3db5ba]
00A8BFB6  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
00A8BFBA  0F 28 05 BF B5 3D 00            movaps xmm0, xmmword ptr [rip + 0x3db5bf]
00A8BFC1  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00A8BFC5  0F 28 0D C4 B5 3D 00            movaps xmm1, xmmword ptr [rip + 0x3db5c4]
00A8BFCC  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
00A8BFD0  49 89 07                        mov qword ptr [r15], rax
00A8BFD3  41 C7 04 24 40 00 00 00         mov dword ptr [r12], 0x40
00A8BFDB  E9 0D FE FF FF                  jmp 0x140a8bded
00A8BFE0  41 83 FE 60                     cmp r14d, 0x60
00A8BFE4  0F 82 ED FA FF FF               jb 0x140a8bad7
00A8BFEA  4C 39 4F 08                     cmp qword ptr [rdi + 8], r9
00A8BFEE  75 09                           jne 0x140a8bff9
00A8BFF0  48 85 F6                        test rsi, rsi
00A8BFF3  0F 84 DE FA FF FF               je 0x140a8bad7
00A8BFF9  81 7F 18 9C 01 00 00            cmp dword ptr [rdi + 0x18], 0x19c
00A8C000  75 25                           jne 0x140a8c027
00A8C002  44 38 4F 58                     cmp byte ptr [rdi + 0x58], r9b
00A8C006  75 18                           jne 0x140a8c020
00A8C008  44 39 4F 10                     cmp dword ptr [rdi + 0x10], r9d
00A8C00C  74 12                           je 0x140a8c020
00A8C00E  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
00A8C011  89 05 3D B5 3D 00               mov dword ptr [rip + 0x3db53d], eax
00A8C017  44 89 15 3A B5 3D 00            mov dword ptr [rip + 0x3db53a], r10d
00A8C01E  EB 07                           jmp 0x140a8c027
00A8C020  44 89 0D 31 B5 3D 00            mov dword ptr [rip + 0x3db531], r9d
00A8C027  49 8B D9                        mov rbx, r9
00A8C02A  48 85 F6                        test rsi, rsi
00A8C02D  74 21                           je 0x140a8c050
00A8C02F  BA 08 00 00 00                  mov edx, 8
00A8C034  B9 00 01 00 00                  mov ecx, 0x100
00A8C039  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8C03F  E8 AC 60 0F 00                  call 0x140b820f0
00A8C044  48 8B D8                        mov rbx, rax
00A8C047  48 85 C0                        test rax, rax
00A8C04A  0F 84 B3 FA FF FF               je 0x140a8bb03
00A8C050  44 8A 47 58                     mov r8b, byte ptr [rdi + 0x58]
00A8C054  48 8D 57 10                     lea rdx, [rdi + 0x10]
00A8C058  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00A8C05C  E8 4B 4C 9D FF                  call 0x140460cac
00A8C061  33 C9                           xor ecx, ecx
00A8C063  48 85 F6                        test rsi, rsi
00A8C066  0F 84 FE FA FF FF               je 0x140a8bb6a
00A8C06C  48 89 03                        mov qword ptr [rbx], rax
00A8C06F  49 89 1F                        mov qword ptr [r15], rbx
00A8C072  41 C7 04 24 08 00 00 00         mov dword ptr [r12], 8
00A8C07A  E9 6E FD FF FF                  jmp 0x140a8bded
00A8C07F  41 83 FE 0C                     cmp r14d, 0xc
00A8C083  0F 82 4E FA FF FF               jb 0x140a8bad7
00A8C089  48 85 F6                        test rsi, rsi
00A8C08C  0F 85 B6 FA FF FF               jne 0x140a8bb48
00A8C092  48 8D 0D 67 0B 48 00            lea rcx, [rip + 0x480b67]
00A8C099  E8 06 DA 84 FF                  call 0x1402d9aa4
00A8C09E  8B 0D 2C AC 53 00               mov ecx, dword ptr [rip + 0x53ac2c]
00A8C0A4  33 D2                           xor edx, edx
00A8C0A6  38 57 08                        cmp byte ptr [rdi + 8], dl
00A8C0A9  74 1F                           je 0x140a8c0ca
00A8C0AB  B8 FF FF FF FF                  mov eax, 0xffffffff
00A8C0B0  3B C8                           cmp ecx, eax
00A8C0B2  73 0C                           jae 0x140a8c0c0
00A8C0B4  FF C1                           inc ecx
00A8C0B6  8B DA                           mov ebx, edx
00A8C0B8  89 0D 12 AC 53 00               mov dword ptr [rip + 0x53ac12], ecx
00A8C0BE  EB 05                           jmp 0x140a8c0c5
00A8C0C0  BB 95 00 00 C0                  mov ebx, 0xc0000095
00A8C0C5  83 F9 01                        cmp ecx, 1
00A8C0C8  EB 1C                           jmp 0x140a8c0e6
00A8C0CA  85 C9                           test ecx, ecx
00A8C0CC  74 11                           je 0x140a8c0df
00A8C0CE  B8 FF FF FF FF                  mov eax, 0xffffffff
00A8C0D3  8B DA                           mov ebx, edx
00A8C0D5  03 C8                           add ecx, eax
00A8C0D7  89 0D F3 AB 53 00               mov dword ptr [rip + 0x53abf3], ecx
00A8C0DD  EB 05                           jmp 0x140a8c0e4
00A8C0DF  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00A8C0E4  85 C9                           test ecx, ecx
00A8C0E6  75 0C                           jne 0x140a8c0f4
00A8C0E8  33 C9                           xor ecx, ecx
00A8C0EA  E8 41 AF 00 00                  call 0x140a97030
00A8C0EF  E9 69 F9 FF FF                  jmp 0x140a8ba5d
00A8C0F4  48 8D 0D 05 0B 48 00            lea rcx, [rip + 0x480b05]
00A8C0FB  E8 28 E3 84 FF                  call 0x1402da428
00A8C100  E9 58 F9 FF FF                  jmp 0x140a8ba5d
00A8C105  83 EB 1B                        sub ebx, 0x1b
00A8C108  0F 84 0B 01 00 00               je 0x140a8c219
00A8C10E  83 EB 01                        sub ebx, 1
00A8C111  0F 84 D9 00 00 00               je 0x140a8c1f0
00A8C117  83 EB 01                        sub ebx, 1
00A8C11A  74 71                           je 0x140a8c18d
00A8C11C  83 FB 01                        cmp ebx, 1
00A8C11F  0F 85 23 FA FF FF               jne 0x140a8bb48
00A8C125  41 83 FE 08                     cmp r14d, 8
00A8C129  0F 82 A8 F9 FF FF               jb 0x140a8bad7
00A8C12F  48 85 F6                        test rsi, rsi
00A8C132  0F 84 9F F9 FF FF               je 0x140a8bad7
00A8C138  BB 03 00 00 00                  mov ebx, 3
00A8C13D  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8C143  8B D3                           mov edx, ebx
00A8C145  B9 00 01 00 00                  mov ecx, 0x100
00A8C14A  E8 A1 5F 0F 00                  call 0x140b820f0
00A8C14F  33 D2                           xor edx, edx
00A8C151  48 8B C8                        mov rcx, rax
00A8C154  48 85 C0                        test rax, rax
00A8C157  0F 84 A6 F9 FF FF               je 0x140a8bb03
00A8C15D  8A 05 09 AA 53 00               mov al, byte ptr [rip + 0x53aa09]
00A8C163  88 01                           mov byte ptr [rcx], al
00A8C165  8A 05 71 A9 53 00               mov al, byte ptr [rip + 0x53a971]
00A8C16B  88 41 01                        mov byte ptr [rcx + 1], al
00A8C16E  39 15 34 AC 53 00               cmp dword ptr [rip + 0x53ac34], edx
00A8C174  0F 95 C0                        setne al
00A8C177  88 41 02                        mov byte ptr [rcx + 2], al
00A8C17A  49 89 0F                        mov qword ptr [r15], rcx
00A8C17D  41 89 1C 24                     mov dword ptr [r12], ebx
00A8C181  41 C6 45 00 01                  mov byte ptr [r13], 1
00A8C186  8B DA                           mov ebx, edx
00A8C188  E9 D0 F8 FF FF                  jmp 0x140a8ba5d
00A8C18D  41 83 FE 08                     cmp r14d, 8
00A8C191  0F 82 40 F9 FF FF               jb 0x140a8bad7
00A8C197  48 85 F6                        test rsi, rsi
00A8C19A  0F 84 37 F9 FF FF               je 0x140a8bad7
00A8C1A0  BA 30 00 00 00                  mov edx, 0x30
00A8C1A5  B9 00 01 00 00                  mov ecx, 0x100
00A8C1AA  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8C1B0  E8 3B 5F 0F 00                  call 0x140b820f0
00A8C1B5  33 C9                           xor ecx, ecx
00A8C1B7  48 85 C0                        test rax, rax
00A8C1BA  0F 84 43 F9 FF FF               je 0x140a8bb03
00A8C1C0  0F 10 05 69 B2 3D 00            movups xmm0, xmmword ptr [rip + 0x3db269]
00A8C1C7  0F 11 00                        movups xmmword ptr [rax], xmm0
00A8C1CA  0F 10 0D 6F B2 3D 00            movups xmm1, xmmword ptr [rip + 0x3db26f]
00A8C1D1  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
00A8C1D5  0F 10 05 74 B2 3D 00            movups xmm0, xmmword ptr [rip + 0x3db274]
00A8C1DC  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00A8C1E0  49 89 07                        mov qword ptr [r15], rax
00A8C1E3  41 C7 04 24 30 00 00 00         mov dword ptr [r12], 0x30
00A8C1EB  E9 FD FB FF FF                  jmp 0x140a8bded
00A8C1F0  41 83 FE 0C                     cmp r14d, 0xc
00A8C1F4  0F 85 4E F9 FF FF               jne 0x140a8bb48
00A8C1FA  8B 47 08                        mov eax, dword ptr [rdi + 8]
00A8C1FD  4C 8D 45 9F                     lea r8, [rbp - 0x61]
00A8C201  41 8D 56 F8                     lea edx, [r14 - 8]
00A8C205  89 45 9F                        mov dword ptr [rbp - 0x61], eax
00A8C208  48 8D 0D 09 58 58 FF            lea rcx, [rip - 0xa7a7f7]
00A8C20F  E8 58 8B E8 FF                  call 0x140914d6c
00A8C214  E9 4F F9 FF FF                  jmp 0x140a8bb68
00A8C219  41 83 FE 10                     cmp r14d, 0x10
00A8C21D  0F 82 B4 F8 FF FF               jb 0x140a8bad7
00A8C223  48 85 F6                        test rsi, rsi
00A8C226  0F 85 1C F9 FF FF               jne 0x140a8bb48
00A8C22C  8B 57 0C                        mov edx, dword ptr [rdi + 0xc]
00A8C22F  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00A8C232  E8 B1 31 00 00                  call 0x140a8f3e8
00A8C237  E9 2C F9 FF FF                  jmp 0x140a8bb68
00A8C23C  83 FB 2A                        cmp ebx, 0x2a
00A8C23F  0F 8F F7 02 00 00               jg 0x140a8c53c
00A8C245  0F 84 A8 02 00 00               je 0x140a8c4f3
00A8C24B  83 FB 25                        cmp ebx, 0x25
00A8C24E  0F 8F BF 00 00 00               jg 0x140a8c313
00A8C254  74 6F                           je 0x140a8c2c5
00A8C256  8B CB                           mov ecx, ebx
00A8C258  83 E9 20                        sub ecx, 0x20
00A8C25B  0F 84 98 01 00 00               je 0x140a8c3f9
00A8C261  83 E9 01                        sub ecx, 1
00A8C264  0F 84 EE F7 FF FF               je 0x140a8ba58
00A8C26A  83 E9 01                        sub ecx, 1
00A8C26D  0F 84 86 01 00 00               je 0x140a8c3f9
00A8C273  83 E9 01                        sub ecx, 1
00A8C276  0F 84 7D 01 00 00               je 0x140a8c3f9
00A8C27C  83 F9 01                        cmp ecx, 1
00A8C27F  0F 85 C3 F8 FF FF               jne 0x140a8bb48
00A8C285  41 83 FE 0C                     cmp r14d, 0xc
00A8C289  0F 82 48 F8 FF FF               jb 0x140a8bad7
00A8C28F  48 85 F6                        test rsi, rsi
00A8C292  0F 85 B0 F8 FF FF               jne 0x140a8bb48
00A8C298  8A 5F 08                        mov bl, byte ptr [rdi + 8]
00A8C29B  48 8D 0D 9E C1 47 00            lea rcx, [rip + 0x47c19e]
00A8C2A2  E8 9D 48 9A FF                  call 0x140430b44
00A8C2A7  48 8D 0D 92 C1 47 00            lea rcx, [rip + 0x47c192]
00A8C2AE  88 1D 5C C1 47 00               mov byte ptr [rip + 0x47c15c], bl
00A8C2B4  E8 03 39 85 FF                  call 0x1402dfbbc
00A8C2B9  33 C9                           xor ecx, ecx
00A8C2BB  E8 D8 E0 FB FF                  call 0x140a4a398
00A8C2C0  E9 A3 F8 FF FF                  jmp 0x140a8bb68
00A8C2C5  41 83 FE 08                     cmp r14d, 8
00A8C2C9  0F 82 08 F8 FF FF               jb 0x140a8bad7
00A8C2CF  48 85 F6                        test rsi, rsi
00A8C2D2  0F 84 FF F7 FF FF               je 0x140a8bad7
00A8C2D8  BA 04 00 00 00                  mov edx, 4
00A8C2DD  B9 00 01 00 00                  mov ecx, 0x100
00A8C2E2  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8C2E8  E8 03 5E 0F 00                  call 0x140b820f0
00A8C2ED  33 D2                           xor edx, edx
00A8C2EF  48 8B C8                        mov rcx, rax
00A8C2F2  48 85 C0                        test rax, rax
00A8C2F5  0F 84 08 F8 FF FF               je 0x140a8bb03
00A8C2FB  8B 05 43 FA 47 00               mov eax, dword ptr [rip + 0x47fa43]
00A8C301  89 01                           mov dword ptr [rcx], eax
00A8C303  49 89 0F                        mov qword ptr [r15], rcx
00A8C306  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
00A8C30E  E9 6E FE FF FF                  jmp 0x140a8c181
00A8C313  8B CB                           mov ecx, ebx
00A8C315  83 E9 26                        sub ecx, 0x26
00A8C318  0F 84 DB 00 00 00               je 0x140a8c3f9
00A8C31E  83 E9 01                        sub ecx, 1
00A8C321  0F 84 B2 00 00 00               je 0x140a8c3d9
00A8C327  83 E9 01                        sub ecx, 1
00A8C32A  74 7B                           je 0x140a8c3a7
00A8C32C  83 F9 01                        cmp ecx, 1
00A8C32F  0F 85 13 F8 FF FF               jne 0x140a8bb48
00A8C335  41 83 FE 10                     cmp r14d, 0x10
00A8C339  0F 85 09 F8 FF FF               jne 0x140a8bb48
00A8C33F  48 85 F6                        test rsi, rsi
00A8C342  0F 84 8F F7 FF FF               je 0x140a8bad7
00A8C348  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8C34E  49 8B D2                        mov rdx, r10
00A8C351  B9 00 01 00 00                  mov ecx, 0x100
00A8C356  E8 95 5D 0F 00                  call 0x140b820f0
00A8C35B  33 D2                           xor edx, edx
00A8C35D  48 8B C8                        mov rcx, rax
00A8C360  48 85 C0                        test rax, rax
00A8C363  0F 84 9A F7 FF FF               je 0x140a8bb03
00A8C369  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00A8C36D  48 85 C0                        test rax, rax
00A8C370  74 21                           je 0x140a8c393
00A8C372  48 8B 80 38 01 00 00            mov rax, qword ptr [rax + 0x138]
00A8C379  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
00A8C37D  48 85 C0                        test rax, rax
00A8C380  74 11                           je 0x140a8c393
00A8C382  48 8B 40 50                     mov rax, qword ptr [rax + 0x50]
00A8C386  48 85 C0                        test rax, rax
00A8C389  74 08                           je 0x140a8c393
00A8C38B  48 39 50 40                     cmp qword ptr [rax + 0x40], rdx
00A8C38F  B0 01                           mov al, 1
00A8C391  75 02                           jne 0x140a8c395
00A8C393  8A C2                           mov al, dl
00A8C395  88 01                           mov byte ptr [rcx], al
00A8C397  49 89 0F                        mov qword ptr [r15], rcx
00A8C39A  41 C7 04 24 01 00 00 00         mov dword ptr [r12], 1
00A8C3A2  E9 DA FD FF FF                  jmp 0x140a8c181
00A8C3A7  41 83 FE 10                     cmp r14d, 0x10
00A8C3AB  0F 85 97 F7 FF FF               jne 0x140a8bb48
00A8C3B1  44 39 4F 08                     cmp dword ptr [rdi + 8], r9d
00A8C3B5  0F 85 8D F7 FF FF               jne 0x140a8bb48
00A8C3BB  41 8D 4E F7                     lea ecx, [r14 - 9]
00A8C3BF  44 38 4F 0C                     cmp byte ptr [rdi + 0xc], r9b
00A8C3C3  74 0A                           je 0x140a8c3cf
00A8C3C5  E8 FA 3A 90 FF                  call 0x14038fec4
00A8C3CA  E9 99 F7 FF FF                  jmp 0x140a8bb68
00A8C3CF  E8 38 3D 90 FF                  call 0x14039010c
00A8C3D4  E9 8F F7 FF FF                  jmp 0x140a8bb68
00A8C3D9  41 83 FE 0C                     cmp r14d, 0xc
00A8C3DD  0F 85 65 F7 FF FF               jne 0x140a8bb48
00A8C3E3  8A 47 08                        mov al, byte ptr [rdi + 8]
00A8C3E6  48 8D 55 97                     lea rdx, [rbp - 0x69]
00A8C3EA  88 45 97                        mov byte ptr [rbp - 0x69], al
00A8C3ED  48 8D 0D 04 1D 59 FF            lea rcx, [rip - 0xa6e2fc]
00A8C3F4  E9 8D F7 FF FF                  jmp 0x140a8bb86
00A8C3F9  41 83 FE 18                     cmp r14d, 0x18
00A8C3FD  0F 85 45 F7 FF FF               jne 0x140a8bb48
00A8C403  48 85 F6                        test rsi, rsi
00A8C406  74 4A                           je 0x140a8c452
00A8C408  8B 47 08                        mov eax, dword ptr [rdi + 8]
00A8C40B  85 C0                           test eax, eax
00A8C40D  0F 84 35 F7 FF FF               je 0x140a8bb48
00A8C413  8B C8                           mov ecx, eax
00A8C415  B8 FF FF FF FF                  mov eax, 0xffffffff
00A8C41A  48 C1 E1 02                     shl rcx, 2
00A8C41E  48 3B C8                        cmp rcx, rax
00A8C421  77 25                           ja 0x140a8c448
00A8C423  44 8B F1                        mov r14d, ecx
00A8C426  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8C42C  8B D1                           mov edx, ecx
00A8C42E  B9 00 01 00 00                  mov ecx, 0x100
00A8C433  E8 B8 5C 0F 00                  call 0x140b820f0
00A8C438  45 33 C9                        xor r9d, r9d
00A8C43B  48 8B F0                        mov rsi, rax
00A8C43E  48 85 C0                        test rax, rax
00A8C441  75 16                           jne 0x140a8c459
00A8C443  E9 BB F6 FF FF                  jmp 0x140a8bb03
00A8C448  BB 95 00 00 C0                  mov ebx, 0xc0000095
00A8C44D  E9 0B F6 FF FF                  jmp 0x140a8ba5d
00A8C452  48 8B 75 D7                     mov rsi, qword ptr [rbp - 0x29]
00A8C456  45 8B F1                        mov r14d, r9d
00A8C459  83 FB 1F                        cmp ebx, 0x1f
00A8C45C  75 1A                           jne 0x140a8c478
00A8C45E  44 39 4F 08                     cmp dword ptr [rdi + 8], r9d
00A8C462  75 07                           jne 0x140a8c46b
00A8C464  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A8C469  EB 78                           jmp 0x140a8c4e3
00A8C46B  48 8B D6                        mov rdx, rsi
00A8C46E  48 8B CF                        mov rcx, rdi
00A8C471  E8 22 FF FB FF                  call 0x140a4c398
00A8C476  EB 43                           jmp 0x140a8c4bb
00A8C478  83 FB 20                        cmp ebx, 0x20
00A8C47B  75 13                           jne 0x140a8c490
00A8C47D  44 39 4F 08                     cmp dword ptr [rdi + 8], r9d
00A8C481  74 E1                           je 0x140a8c464
00A8C483  48 8B D6                        mov rdx, rsi
00A8C486  48 8B CF                        mov rcx, rdi
00A8C489  E8 EE 02 FC FF                  call 0x140a4c77c
00A8C48E  EB 2B                           jmp 0x140a8c4bb
00A8C490  83 FB 22                        cmp ebx, 0x22
00A8C493  75 10                           jne 0x140a8c4a5
00A8C495  44 39 4F 08                     cmp dword ptr [rdi + 8], r9d
00A8C499  74 C9                           je 0x140a8c464
00A8C49B  48 8B CF                        mov rcx, rdi
00A8C49E  E8 A9 1A 04 00                  call 0x140acdf4c
00A8C4A3  EB 16                           jmp 0x140a8c4bb
00A8C4A5  83 FB 23                        cmp ebx, 0x23
00A8C4A8  75 07                           jne 0x140a8c4b1
00A8C4AA  E8 39 74 03 00                  call 0x140ac38e8
00A8C4AF  EB 0A                           jmp 0x140a8c4bb
00A8C4B1  83 FB 26                        cmp ebx, 0x26
00A8C4B4  75 28                           jne 0x140a8c4de
00A8C4B6  E8 49 22 C7 FF                  call 0x1406fe704
00A8C4BB  45 33 C9                        xor r9d, r9d
00A8C4BE  8B D8                           mov ebx, eax
00A8C4C0  85 C0                           test eax, eax
00A8C4C2  78 1F                           js 0x140a8c4e3
00A8C4C4  48 85 F6                        test rsi, rsi
00A8C4C7  0F 84 0B 03 00 00               je 0x140a8c7d8
00A8C4CD  49 89 37                        mov qword ptr [r15], rsi
00A8C4D0  45 89 34 24                     mov dword ptr [r12], r14d
00A8C4D4  41 C6 45 00 01                  mov byte ptr [r13], 1
00A8C4D9  E9 FA 02 00 00                  jmp 0x140a8c7d8
00A8C4DE  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00A8C4E3  48 85 F6                        test rsi, rsi
00A8C4E6  0F 84 71 F5 FF FF               je 0x140a8ba5d
00A8C4EC  33 D2                           xor edx, edx
00A8C4EE  E9 5D F7 FF FF                  jmp 0x140a8bc50
00A8C4F3  41 83 FE 08                     cmp r14d, 8
00A8C4F7  0F 82 DA F5 FF FF               jb 0x140a8bad7
00A8C4FD  48 85 F6                        test rsi, rsi
00A8C500  0F 84 D1 F5 FF FF               je 0x140a8bad7
00A8C506  BA 20 00 00 00                  mov edx, 0x20
00A8C50B  B9 00 01 00 00                  mov ecx, 0x100
00A8C510  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8C516  E8 D5 5B 0F 00                  call 0x140b820f0
00A8C51B  33 C9                           xor ecx, ecx
00A8C51D  48 85 C0                        test rax, rax
00A8C520  0F 84 DD F5 FF FF               je 0x140a8bb03
00A8C526  0F 10 05 73 B0 3D 00            movups xmm0, xmmword ptr [rip + 0x3db073]
00A8C52D  0F 11 00                        movups xmmword ptr [rax], xmm0
00A8C530  0F 10 0D 79 B0 3D 00            movups xmm1, xmmword ptr [rip + 0x3db079]
00A8C537  E9 A2 F8 FF FF                  jmp 0x140a8bdde
00A8C53C  83 FB 30                        cmp ebx, 0x30
00A8C53F  0F 8F FE 01 00 00               jg 0x140a8c743
00A8C545  0F 84 CB 01 00 00               je 0x140a8c716
00A8C54B  83 EB 2B                        sub ebx, 0x2b
00A8C54E  0F 84 61 01 00 00               je 0x140a8c6b5
00A8C554  83 EB 01                        sub ebx, 1
00A8C557  0F 84 97 00 00 00               je 0x140a8c5f4
00A8C55D  83 EB 01                        sub ebx, 1
00A8C560  74 6D                           je 0x140a8c5cf
00A8C562  83 EB 01                        sub ebx, 1
00A8C565  74 40                           je 0x140a8c5a7
00A8C567  83 FB 01                        cmp ebx, 1
00A8C56A  0F 85 D8 F5 FF FF               jne 0x140a8bb48
00A8C570  41 83 FE 14                     cmp r14d, 0x14
00A8C574  0F 82 5D F5 FF FF               jb 0x140a8bad7
00A8C57A  48 85 F6                        test rsi, rsi
00A8C57D  0F 85 C5 F5 FF FF               jne 0x140a8bb48
00A8C583  44 39 4F 04                     cmp dword ptr [rdi + 4], r9d
00A8C587  74 0A                           je 0x140a8c593
00A8C589  BB 59 00 00 C0                  mov ebx, 0xc0000059
00A8C58E  E9 CA F4 FF FF                  jmp 0x140a8ba5d
00A8C593  44 8A 47 10                     mov r8b, byte ptr [rdi + 0x10]
00A8C597  8B 57 0C                        mov edx, dword ptr [rdi + 0xc]
00A8C59A  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00A8C59D  E8 5E 79 A5 FF                  call 0x1404e3f00
00A8C5A2  E9 F9 F5 FF FF                  jmp 0x140a8bba0
00A8C5A7  41 83 FE 20                     cmp r14d, 0x20
00A8C5AB  0F 85 97 F5 FF FF               jne 0x140a8bb48
00A8C5B1  48 85 F6                        test rsi, rsi
00A8C5B4  0F 85 8E F5 FF FF               jne 0x140a8bb48
00A8C5BA  4C 8B 47 10                     mov r8, qword ptr [rdi + 0x10]
00A8C5BE  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00A8C5C2  8B 4F 18                        mov ecx, dword ptr [rdi + 0x18]
00A8C5C5  E8 C2 2E 05 00                  call 0x140adf48c
00A8C5CA  E9 99 F5 FF FF                  jmp 0x140a8bb68
00A8C5CF  33 DB                           xor ebx, ebx
00A8C5D1  41 83 FE 0C                     cmp r14d, 0xc
00A8C5D5  0F 85 6D F5 FF FF               jne 0x140a8bb48
00A8C5DB  38 5F 08                        cmp byte ptr [rdi + 8], bl
00A8C5DE  74 0A                           je 0x140a8c5ea
00A8C5E0  E8 EB BB 02 00                  call 0x140ab81d0
00A8C5E5  E9 73 F4 FF FF                  jmp 0x140a8ba5d
00A8C5EA  E8 D1 8B C7 FF                  call 0x1407051c0
00A8C5EF  E9 69 F4 FF FF                  jmp 0x140a8ba5d
00A8C5F4  41 81 FE 90 00 00 00            cmp r14d, 0x90
00A8C5FB  0F 82 D6 F4 FF FF               jb 0x140a8bad7
00A8C601  48 85 F6                        test rsi, rsi
00A8C604  0F 85 3E F5 FF FF               jne 0x140a8bb48
00A8C60A  48 8B 15 9F 09 48 00            mov rdx, qword ptr [rip + 0x48099f]
00A8C611  4C 8D 45 97                     lea r8, [rbp - 0x69]
00A8C615  33 C9                           xor ecx, ecx
00A8C617  E8 F4 93 91 FF                  call 0x1403a5a10
00A8C61C  45 33 F6                        xor r14d, r14d
00A8C61F  8B D8                           mov ebx, eax
00A8C621  85 C0                           test eax, eax
00A8C623  0F 88 34 F4 FF FF               js 0x140a8ba5d
00A8C629  44 38 75 97                     cmp byte ptr [rbp - 0x69], r14b
00A8C62D  0F 84 60 F2 FF FF               je 0x140a8b893
00A8C633  E8 08 F9 A0 FF                  call 0x14049bf40
00A8C638  84 C0                           test al, al
00A8C63A  0F 84 18 F4 FF FF               je 0x140a8ba58
00A8C640  41 BF 80 00 00 00               mov r15d, 0x80
00A8C646  4C 8D 45 AF                     lea r8, [rbp - 0x51]
00A8C64A  41 8B D7                        mov edx, r15d
00A8C64D  48 8D 4F 08                     lea rcx, [rdi + 8]
00A8C651  E8 96 AF 9C FF                  call 0x1404575ec
00A8C656  8B D8                           mov ebx, eax
00A8C658  85 C0                           test eax, eax
00A8C65A  0F 88 FD F3 FF FF               js 0x140a8ba5d
00A8C660  48 8B 87 88 00 00 00            mov rax, qword ptr [rdi + 0x88]
00A8C667  4C 39 75 AF                     cmp qword ptr [rbp - 0x51], r14
00A8C66B  75 0A                           jne 0x140a8c677
00A8C66D  48 85 C0                        test rax, rax
00A8C670  74 0E                           je 0x140a8c680
00A8C672  E9 D1 F4 FF FF                  jmp 0x140a8bb48
00A8C677  48 85 C0                        test rax, rax
00A8C67A  0F 84 C8 F4 FF FF               je 0x140a8bb48
00A8C680  E8 3B BD 0E 00                  call 0x140b783c0
00A8C685  4C 8D 47 08                     lea r8, [rdi + 8]
00A8C689  66 44 89 35 0F 21 48 00         mov word ptr [rip + 0x48210f], r14w
00A8C691  49 8B D7                        mov rdx, r15
00A8C694  48 8D 0D 05 21 48 00            lea rcx, [rip + 0x482105]
00A8C69B  E8 70 F2 9A FF                  call 0x14043b910
00A8C6A0  8B D8                           mov ebx, eax
00A8C6A2  48 8B 87 88 00 00 00            mov rax, qword ptr [rdi + 0x88]
00A8C6A9  48 89 05 70 21 48 00            mov qword ptr [rip + 0x482170], rax
00A8C6B0  E9 62 F6 FF FF                  jmp 0x140a8bd17
00A8C6B5  41 8D 46 F8                     lea eax, [r14 - 8]
00A8C6B9  A9 FB FF FF FF                  test eax, 0xfffffffb
00A8C6BE  0F 85 84 F4 FF FF               jne 0x140a8bb48
00A8C6C4  48 85 F6                        test rsi, rsi
00A8C6C7  0F 84 0A F4 FF FF               je 0x140a8bad7
00A8C6CD  BA 08 00 00 00                  mov edx, 8
00A8C6D2  B9 00 01 00 00                  mov ecx, 0x100
00A8C6D7  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8C6DD  E8 0E 5A 0F 00                  call 0x140b820f0
00A8C6E2  48 8B F0                        mov rsi, rax
00A8C6E5  33 C0                           xor eax, eax
00A8C6E7  48 85 F6                        test rsi, rsi
00A8C6EA  0F 84 13 F4 FF FF               je 0x140a8bb03
00A8C6F0  48 8D 4F 08                     lea rcx, [rdi + 8]
00A8C6F4  41 83 FE 0C                     cmp r14d, 0xc
00A8C6F8  74 02                           je 0x140a8c6fc
00A8C6FA  8B C8                           mov ecx, eax
00A8C6FC  48 8B D6                        mov rdx, rsi
00A8C6FF  E8 FC 81 04 00                  call 0x140ad4900
00A8C704  8B D8                           mov ebx, eax
00A8C706  85 C0                           test eax, eax
00A8C708  0F 88 3D F5 FF FF               js 0x140a8bc4b
00A8C70E  49 89 37                        mov qword ptr [r15], rsi
00A8C711  E9 DE F4 FF FF                  jmp 0x140a8bbf4
00A8C716  41 83 FE 10                     cmp r14d, 0x10
00A8C71A  0F 82 B7 F3 FF FF               jb 0x140a8bad7
00A8C720  48 85 F6                        test rsi, rsi
00A8C723  0F 85 1F F4 FF FF               jne 0x140a8bb48
00A8C729  44 39 4F 04                     cmp dword ptr [rdi + 4], r9d
00A8C72D  0F 85 56 FE FF FF               jne 0x140a8c589
00A8C733  8A 57 0C                        mov dl, byte ptr [rdi + 0xc]
00A8C736  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00A8C739  E8 6A EF A6 FF                  call 0x1404fb6a8
00A8C73E  E9 5D F4 FF FF                  jmp 0x140a8bba0
00A8C743  8B CB                           mov ecx, ebx
00A8C745  83 E9 31                        sub ecx, 0x31
00A8C748  0F 84 C7 00 00 00               je 0x140a8c815
00A8C74E  83 E9 01                        sub ecx, 1
00A8C751  0F 84 89 00 00 00               je 0x140a8c7e0
00A8C757  83 E9 01                        sub ecx, 1
00A8C75A  74 3C                           je 0x140a8c798
00A8C75C  BA 02 00 00 00                  mov edx, 2
00A8C761  3B CA                           cmp ecx, edx
00A8C763  0F 85 DF F3 FF FF               jne 0x140a8bb48
00A8C769  4D 8B CC                        mov r9, r12
00A8C76C  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00A8C771  4C 8B C7                        mov r8, rdi
00A8C774  41 8B D6                        mov edx, r14d
00A8C777  8B CB                           mov ecx, ebx
00A8C779  E8 66 49 C7 FF                  call 0x1407010e4
00A8C77E  8B D8                           mov ebx, eax
00A8C780  33 C0                           xor eax, eax
00A8C782  85 DB                           test ebx, ebx
00A8C784  0F 88 D3 F2 FF FF               js 0x140a8ba5d
00A8C78A  49 39 07                        cmp qword ptr [r15], rax
00A8C78D  0F 84 CA F2 FF FF               je 0x140a8ba5d
00A8C793  E9 64 F4 FF FF                  jmp 0x140a8bbfc
00A8C798  85 D2                           test edx, edx
00A8C79A  75 13                           jne 0x140a8c7af
00A8C79C  41 83 FE 10                     cmp r14d, 0x10
00A8C7A0  0F 82 31 F3 FF FF               jb 0x140a8bad7
00A8C7A6  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00A8C7AA  48 8B C8                        mov rcx, rax
00A8C7AD  EB 1B                           jmp 0x140a8c7ca
00A8C7AF  41 3B D2                        cmp edx, r10d
00A8C7B2  0F 85 90 F3 FF FF               jne 0x140a8bb48
00A8C7B8  41 83 FE 18                     cmp r14d, 0x18
00A8C7BC  0F 82 15 F3 FF FF               jb 0x140a8bad7
00A8C7C2  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00A8C7C6  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00A8C7CA  48 89 0D D7 00 48 00            mov qword ptr [rip + 0x4800d7], rcx
00A8C7D1  48 89 05 C8 00 48 00            mov qword ptr [rip + 0x4800c8], rax
00A8C7D8  41 8B D9                        mov ebx, r9d
00A8C7DB  E9 7D F2 FF FF                  jmp 0x140a8ba5d
00A8C7E0  48 85 F6                        test rsi, rsi
00A8C7E3  0F 84 EE F2 FF FF               je 0x140a8bad7
00A8C7E9  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8C7EF  49 8B D2                        mov rdx, r10
00A8C7F2  B9 00 01 00 00                  mov ecx, 0x100
00A8C7F7  E8 F4 58 0F 00                  call 0x140b820f0
00A8C7FC  33 D2                           xor edx, edx
00A8C7FE  48 8B C8                        mov rcx, rax
00A8C801  48 85 C0                        test rax, rax
00A8C804  0F 84 F9 F2 FF FF               je 0x140a8bb03
00A8C80A  8A 05 54 AC 3D 00               mov al, byte ptr [rip + 0x3dac54]
00A8C810  E9 80 FB FF FF                  jmp 0x140a8c395
00A8C815  48 85 F6                        test rsi, rsi
00A8C818  0F 84 B9 F2 FF FF               je 0x140a8bad7
00A8C81E  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8C824  49 8B D2                        mov rdx, r10
00A8C827  B9 00 01 00 00                  mov ecx, 0x100
00A8C82C  E8 BF 58 0F 00                  call 0x140b820f0
00A8C831  33 FF                           xor edi, edi
00A8C833  48 8B D8                        mov rbx, rax
00A8C836  48 85 C0                        test rax, rax
00A8C839  0F 84 C4 F2 FF FF               je 0x140a8bb03
00A8C83F  E8 A0 DC 03 00                  call 0x140aca4e4
00A8C844  E9 DB F2 FF FF                  jmp 0x140a8bb24
00A8C849  83 FB 4E                        cmp ebx, 0x4e
00A8C84C  0F 8F 0E 05 00 00               jg 0x140a8cd60
00A8C852  0F 84 9A 04 00 00               je 0x140a8ccf2
00A8C858  83 FB 43                        cmp ebx, 0x43
00A8C85B  0F 8F F7 01 00 00               jg 0x140a8ca58
00A8C861  0F 84 BC 01 00 00               je 0x140a8ca23
00A8C867  83 FB 3D                        cmp ebx, 0x3d
00A8C86A  0F 8F D7 00 00 00               jg 0x140a8c947
00A8C870  0F 84 D0 F0 FF FF               je 0x140a8b946
00A8C876  8B CB                           mov ecx, ebx
00A8C878  83 E9 38                        sub ecx, 0x38
00A8C87B  0F 84 E8 FE FF FF               je 0x140a8c769
00A8C881  83 E9 01                        sub ecx, 1
00A8C884  0F 84 92 00 00 00               je 0x140a8c91c
00A8C88A  83 E9 01                        sub ecx, 1
00A8C88D  74 72                           je 0x140a8c901
00A8C88F  83 E9 01                        sub ecx, 1
00A8C892  74 52                           je 0x140a8c8e6
00A8C894  83 F9 01                        cmp ecx, 1
00A8C897  0F 85 AB F2 FF FF               jne 0x140a8bb48
00A8C89D  48 85 F6                        test rsi, rsi
00A8C8A0  0F 84 31 F2 FF FF               je 0x140a8bad7
00A8C8A6  B9 08 00 00 00                  mov ecx, 8
00A8C8AB  E8 CC D5 01 00                  call 0x140aa9e7c
00A8C8B0  48 8D 55 B7                     lea rdx, [rbp - 0x49]
00A8C8B4  48 8D 4D A7                     lea rcx, [rbp - 0x59]
00A8C8B8  E8 63 C5 03 00                  call 0x140ac8e20
00A8C8BD  B9 08 00 00 00                  mov ecx, 8
00A8C8C2  8B D8                           mov ebx, eax
00A8C8C4  E8 F3 11 03 00                  call 0x140abdabc
00A8C8C9  33 C9                           xor ecx, ecx
00A8C8CB  85 DB                           test ebx, ebx
00A8C8CD  0F 88 8A F1 FF FF               js 0x140a8ba5d
00A8C8D3  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
00A8C8D7  49 89 07                        mov qword ptr [r15], rax
00A8C8DA  8B 45 A7                        mov eax, dword ptr [rbp - 0x59]
00A8C8DD  41 89 04 24                     mov dword ptr [r12], eax
00A8C8E1  E9 07 F5 FF FF                  jmp 0x140a8bded
00A8C8E6  41 83 FE 18                     cmp r14d, 0x18
00A8C8EA  0F 82 58 F2 FF FF               jb 0x140a8bb48
00A8C8F0  8B 57 10                        mov edx, dword ptr [rdi + 0x10]
00A8C8F3  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00A8C8F7  E8 44 EC A6 FF                  call 0x1404fb540
00A8C8FC  E9 9F F2 FF FF                  jmp 0x140a8bba0
00A8C901  41 83 FE 18                     cmp r14d, 0x18
00A8C905  0F 82 3D F2 FF FF               jb 0x140a8bb48
00A8C90B  8B 57 10                        mov edx, dword ptr [rdi + 0x10]
00A8C90E  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00A8C912  E8 F9 08 A3 FF                  call 0x1404bd210
00A8C917  E9 84 F2 FF FF                  jmp 0x140a8bba0
00A8C91C  48 85 F6                        test rsi, rsi
00A8C91F  0F 85 23 F2 FF FF               jne 0x140a8bb48
00A8C925  49 8B D6                        mov rdx, r14
00A8C928  48 8B CF                        mov rcx, rdi
00A8C92B  E8 D4 EB A4 FF                  call 0x1404db504
00A8C930  E9 6B F2 FF FF                  jmp 0x140a8bba0
00A8C935  41 C7 04 24 00 10 00 00         mov dword ptr [r12], 0x1000
00A8C93D  41 C6 45 00 01                  mov byte ptr [r13], 1
00A8C942  E9 59 F2 FF FF                  jmp 0x140a8bba0
00A8C947  8B CB                           mov ecx, ebx
00A8C949  83 E9 3E                        sub ecx, 0x3e
00A8C94C  0F 84 9C 00 00 00               je 0x140a8c9ee
00A8C952  83 E9 01                        sub ecx, 1
00A8C955  74 49                           je 0x140a8c9a0
00A8C957  83 E9 01                        sub ecx, 1
00A8C95A  0F 84 09 FE FF FF               je 0x140a8c769
00A8C960  83 E9 01                        sub ecx, 1
00A8C963  74 0E                           je 0x140a8c973
00A8C965  83 F9 01                        cmp ecx, 1
00A8C968  0F 85 DA F1 FF FF               jne 0x140a8bb48
00A8C96E  E9 E5 F0 FF FF                  jmp 0x140a8ba58
00A8C973  41 83 FE 10                     cmp r14d, 0x10
00A8C977  0F 85 CB F1 FF FF               jne 0x140a8bb48
00A8C97D  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00A8C981  48 85 C9                        test rcx, rcx
00A8C984  0F 84 BE F1 FF FF               je 0x140a8bb48
00A8C98A  E8 69 3C A2 FF                  call 0x1404b05f8
00A8C98F  8B D8                           mov ebx, eax
00A8C991  33 C0                           xor eax, eax
00A8C993  85 DB                           test ebx, ebx
00A8C995  0F 88 C2 F0 FF FF               js 0x140a8ba5d
00A8C99B  E9 00 F2 FF FF                  jmp 0x140a8bba0
00A8C9A0  48 85 F6                        test rsi, rsi
00A8C9A3  0F 84 9F F1 FF FF               je 0x140a8bb48
00A8C9A9  E8 EE 65 A4 FF                  call 0x1404d2f9c
00A8C9AE  F6 D8                           neg al
00A8C9B0  48 8D 0D D9 53 37 00            lea rcx, [rip + 0x3753d9]
00A8C9B7  48 1B DB                        sbb rbx, rbx
00A8C9BA  48 23 D9                        and rbx, rcx
00A8C9BD  0F 84 95 F0 FF FF               je 0x140a8ba58
00A8C9C3  BA 08 00 00 00                  mov edx, 8
00A8C9C8  B9 00 01 00 00                  mov ecx, 0x100
00A8C9CD  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8C9D3  E8 18 57 0F 00                  call 0x140b820f0
00A8C9D8  33 C9                           xor ecx, ecx
00A8C9DA  48 85 C0                        test rax, rax
00A8C9DD  0F 84 20 F1 FF FF               je 0x140a8bb03
00A8C9E3  48 89 18                        mov qword ptr [rax], rbx
00A8C9E6  49 89 07                        mov qword ptr [r15], rax
00A8C9E9  E9 84 F6 FF FF                  jmp 0x140a8c072
00A8C9EE  48 85 F6                        test rsi, rsi
00A8C9F1  0F 84 E0 F0 FF FF               je 0x140a8bad7
00A8C9F7  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8C9FD  49 8B D2                        mov rdx, r10
00A8CA00  B9 00 01 00 00                  mov ecx, 0x100
00A8CA05  E8 E6 56 0F 00                  call 0x140b820f0
00A8CA0A  33 D2                           xor edx, edx
00A8CA0C  48 8B C8                        mov rcx, rax
00A8CA0F  48 85 C0                        test rax, rax
00A8CA12  0F 84 EB F0 FF FF               je 0x140a8bb03
00A8CA18  8A 05 52 AA 3D 00               mov al, byte ptr [rip + 0x3daa52]
00A8CA1E  E9 72 F9 FF FF                  jmp 0x140a8c395
00A8CA23  45 89 0C 24                     mov dword ptr [r12], r9d
00A8CA27  BA 04 00 00 00                  mov edx, 4
00A8CA2C  B9 00 01 00 00                  mov ecx, 0x100
00A8CA31  4D 89 0F                        mov qword ptr [r15], r9
00A8CA34  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8CA3A  E8 B1 56 0F 00                  call 0x140b820f0
00A8CA3F  33 D2                           xor edx, edx
00A8CA41  48 8B C8                        mov rcx, rax
00A8CA44  48 85 C0                        test rax, rax
00A8CA47  0F 84 B6 F0 FF FF               je 0x140a8bb03
00A8CA4D  8B 05 75 E9 37 00               mov eax, dword ptr [rip + 0x37e975]
00A8CA53  E9 A9 F8 FF FF                  jmp 0x140a8c301
00A8CA58  83 FB 49                        cmp ebx, 0x49
00A8CA5B  0F 8F C6 01 00 00               jg 0x140a8cc27
00A8CA61  0F 84 A0 01 00 00               je 0x140a8cc07
00A8CA67  83 EB 44                        sub ebx, 0x44
00A8CA6A  0F 84 7F 01 00 00               je 0x140a8cbef
00A8CA70  83 EB 01                        sub ebx, 1
00A8CA73  0F 84 2A 01 00 00               je 0x140a8cba3
00A8CA79  83 EB 01                        sub ebx, 1
00A8CA7C  0F 84 92 00 00 00               je 0x140a8cb14
00A8CA82  83 EB 01                        sub ebx, 1
00A8CA85  74 4E                           je 0x140a8cad5
00A8CA87  83 FB 01                        cmp ebx, 1
00A8CA8A  0F 85 B8 F0 FF FF               jne 0x140a8bb48
00A8CA90  48 85 F6                        test rsi, rsi
00A8CA93  0F 84 AF F0 FF FF               je 0x140a8bb48
00A8CA99  41 BE 00 09 00 00               mov r14d, 0x900
00A8CA9F  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8CAA5  41 8B D6                        mov edx, r14d
00A8CAA8  B9 00 01 00 00                  mov ecx, 0x100
00A8CAAD  E8 3E 56 0F 00                  call 0x140b820f0
00A8CAB2  48 8B F8                        mov rdi, rax
00A8CAB5  48 85 C0                        test rax, rax
00A8CAB8  0F 84 45 F0 FF FF               je 0x140a8bb03
00A8CABE  48 8B C8                        mov rcx, rax
00A8CAC1  E8 EA 77 FC FF                  call 0x140a542b0
00A8CAC6  8B D8                           mov ebx, eax
00A8CAC8  85 C0                           test eax, eax
00A8CACA  0F 89 9E F2 FF FF               jns 0x140a8bd6e
00A8CAD0  E9 0A F1 FF FF                  jmp 0x140a8bbdf
00A8CAD5  41 83 FE 0C                     cmp r14d, 0xc
00A8CAD9  0F 85 69 F0 FF FF               jne 0x140a8bb48
00A8CADF  8A 5F 08                        mov bl, byte ptr [rdi + 8]
00A8CAE2  48 8D 0D 17 BA 47 00            lea rcx, [rip + 0x47ba17]
00A8CAE9  E8 56 40 9A FF                  call 0x140430b44
00A8CAEE  38 1D 09 A0 53 00               cmp byte ptr [rip + 0x53a009], bl
00A8CAF4  74 0D                           je 0x140a8cb03
00A8CAF6  8A CB                           mov cl, bl
00A8CAF8  88 1D FF 9F 53 00               mov byte ptr [rip + 0x539fff], bl
00A8CAFE  E8 D5 5A C7 FF                  call 0x1407025d8
00A8CB03  48 8D 0D F6 B9 47 00            lea rcx, [rip + 0x47b9f6]
00A8CB0A  E8 AD 30 85 FF                  call 0x1402dfbbc
00A8CB0F  E9 54 F0 FF FF                  jmp 0x140a8bb68
00A8CB14  41 83 FE 0C                     cmp r14d, 0xc
00A8CB18  0F 82 B9 EF FF FF               jb 0x140a8bad7
00A8CB1E  BB 02 00 00 00                  mov ebx, 2
00A8CB23  39 5F 04                        cmp dword ptr [rdi + 4], ebx
00A8CB26  0F 87 2C EF FF FF               ja 0x140a8ba58
00A8CB2C  75 0A                           jne 0x140a8cb38
00A8CB2E  41 83 FE 20                     cmp r14d, 0x20
00A8CB32  0F 82 9F EF FF FF               jb 0x140a8bad7
00A8CB38  48 85 F6                        test rsi, rsi
00A8CB3B  0F 84 07 F0 FF FF               je 0x140a8bb48
00A8CB41  BA 08 00 00 00                  mov edx, 8
00A8CB46  B9 00 01 00 00                  mov ecx, 0x100
00A8CB4B  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8CB51  E8 9A 55 0F 00                  call 0x140b820f0
00A8CB56  48 8B F0                        mov rsi, rax
00A8CB59  48 85 C0                        test rax, rax
00A8CB5C  0F 84 A1 EF FF FF               je 0x140a8bb03
00A8CB62  39 5F 04                        cmp dword ptr [rdi + 4], ebx
00A8CB65  75 28                           jne 0x140a8cb8f
00A8CB67  44 8B 4F 14                     mov r9d, dword ptr [rdi + 0x14]
00A8CB6B  44 8B 47 10                     mov r8d, dword ptr [rdi + 0x10]
00A8CB6F  8B 57 08                        mov edx, dword ptr [rdi + 8]
00A8CB72  8B 4F 0C                        mov ecx, dword ptr [rdi + 0xc]
00A8CB75  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A8CB7A  8A 47 1C                        mov al, byte ptr [rdi + 0x1c]
00A8CB7D  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00A8CB81  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
00A8CB84  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00A8CB88  E8 1B 76 B4 FF                  call 0x1405d41a8
00A8CB8D  EB 0B                           jmp 0x140a8cb9a
00A8CB8F  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00A8CB92  48 8B D6                        mov rdx, rsi
00A8CB95  E8 6A 19 A5 FF                  call 0x1404de504
00A8CB9A  8B D8                           mov ebx, eax
00A8CB9C  85 C0                           test eax, eax
00A8CB9E  E9 65 FB FF FF                  jmp 0x140a8c708
00A8CBA3  48 85 F6                        test rsi, rsi
00A8CBA6  0F 84 9C EF FF FF               je 0x140a8bb48
00A8CBAC  BA 14 00 00 00                  mov edx, 0x14
00A8CBB1  B9 00 01 00 00                  mov ecx, 0x100
00A8CBB6  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8CBBC  E8 2F 55 0F 00                  call 0x140b820f0
00A8CBC1  33 FF                           xor edi, edi
00A8CBC3  48 8B D8                        mov rbx, rax
00A8CBC6  48 85 C0                        test rax, rax
00A8CBC9  0F 84 34 EF FF FF               je 0x140a8bb03
00A8CBCF  48 8B C8                        mov rcx, rax
00A8CBD2  E8 E5 E6 04 00                  call 0x140adb2bc
00A8CBD7  83 7D 6F 14                     cmp dword ptr [rbp + 0x6f], 0x14
00A8CBDB  49 89 1F                        mov qword ptr [r15], rbx
00A8CBDE  1B C0                           sbb eax, eax
00A8CBE0  83 E0 ED                        and eax, 0xffffffed
00A8CBE3  83 C0 14                        add eax, 0x14
00A8CBE6  41 89 04 24                     mov dword ptr [r12], eax
00A8CBEA  E9 42 EF FF FF                  jmp 0x140a8bb31
00A8CBEF  8B 05 63 E9 37 00               mov eax, dword ptr [rip + 0x37e963]
00A8CBF5  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00A8CBFA  F7 D8                           neg eax
00A8CBFC  1B C9                           sbb ecx, ecx
00A8CBFE  F7 D1                           not ecx
00A8CC00  23 D9                           and ebx, ecx
00A8CC02  E9 56 EE FF FF                  jmp 0x140a8ba5d
00A8CC07  41 83 FE 0C                     cmp r14d, 0xc
00A8CC0B  0F 82 C6 EE FF FF               jb 0x140a8bad7
00A8CC11  48 85 F6                        test rsi, rsi
00A8CC14  0F 85 2E EF FF FF               jne 0x140a8bb48
00A8CC1A  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00A8CC1D  E8 96 61 E8 FF                  call 0x140912db8
00A8CC22  E9 41 EF FF FF                  jmp 0x140a8bb68
00A8CC27  8B CB                           mov ecx, ebx
00A8CC29  83 E9 4A                        sub ecx, 0x4a
00A8CC2C  74 56                           je 0x140a8cc84
00A8CC2E  83 E9 01                        sub ecx, 1
00A8CC31  74 51                           je 0x140a8cc84
00A8CC33  83 E9 01                        sub ecx, 1
00A8CC36  74 09                           je 0x140a8cc41
00A8CC38  83 F9 01                        cmp ecx, 1
00A8CC3B  0F 85 07 EF FF FF               jne 0x140a8bb48
00A8CC41  41 83 FE 0C                     cmp r14d, 0xc
00A8CC45  0F 85 8C EE FF FF               jne 0x140a8bad7
00A8CC4B  48 85 F6                        test rsi, rsi
00A8CC4E  0F 84 F4 EE FF FF               je 0x140a8bb48
00A8CC54  0F B7 57 08                     movzx edx, word ptr [rdi + 8]
00A8CC58  4C 8D 4D AB                     lea r9, [rbp - 0x55]
00A8CC5C  4C 8D 45 BF                     lea r8, [rbp - 0x41]
00A8CC60  8B CB                           mov ecx, ebx
00A8CC62  E8 7D CC FE FF                  call 0x140a798e4
00A8CC67  8B D8                           mov ebx, eax
00A8CC69  85 C0                           test eax, eax
00A8CC6B  0F 88 EC ED FF FF               js 0x140a8ba5d
00A8CC71  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
00A8CC75  49 89 07                        mov qword ptr [r15], rax
00A8CC78  8B 45 AB                        mov eax, dword ptr [rbp - 0x55]
00A8CC7B  41 89 04 24                     mov dword ptr [r12], eax
00A8CC7F  E9 78 EF FF FF                  jmp 0x140a8bbfc
00A8CC84  41 83 FE 0C                     cmp r14d, 0xc
00A8CC88  0F 85 49 EE FF FF               jne 0x140a8bad7
00A8CC8E  48 85 F6                        test rsi, rsi
00A8CC91  0F 84 B1 EE FF FF               je 0x140a8bb48
00A8CC97  83 FB 4A                        cmp ebx, 0x4a
00A8CC9A  75 08                           jne 0x140a8cca4
00A8CC9C  41 BE 28 01 00 00               mov r14d, 0x128
00A8CCA2  EB 0F                           jmp 0x140a8ccb3
00A8CCA4  83 FB 4B                        cmp ebx, 0x4b
00A8CCA7  0F 85 9B EE FF FF               jne 0x140a8bb48
00A8CCAD  41 BE 50 02 00 00               mov r14d, 0x250
00A8CCB3  41 8B D6                        mov edx, r14d
00A8CCB6  B9 00 01 00 00                  mov ecx, 0x100
00A8CCBB  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8CCC1  E8 2A 54 0F 00                  call 0x140b820f0
00A8CCC6  48 8B F0                        mov rsi, rax
00A8CCC9  48 85 C0                        test rax, rax
00A8CCCC  0F 84 31 EE FF FF               je 0x140a8bb03
00A8CCD2  0F B7 57 08                     movzx edx, word ptr [rdi + 8]
00A8CCD6  4C 8B C0                        mov r8, rax
00A8CCD9  8B CB                           mov ecx, ebx
00A8CCDB  E8 6C 21 FF FF                  call 0x140a7ee4c
00A8CCE0  8B D8                           mov ebx, eax
00A8CCE2  85 C0                           test eax, eax
00A8CCE4  0F 88 61 EF FF FF               js 0x140a8bc4b
00A8CCEA  49 89 37                        mov qword ptr [r15], rsi
00A8CCED  E9 7F F0 FF FF                  jmp 0x140a8bd71
00A8CCF2  48 85 F6                        test rsi, rsi
00A8CCF5  0F 84 4D EE FF FF               je 0x140a8bb48
00A8CCFB  BA 04 00 00 00                  mov edx, 4
00A8CD00  B9 00 01 00 00                  mov ecx, 0x100
00A8CD05  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8CD0B  E8 E0 53 0F 00                  call 0x140b820f0
00A8CD10  33 FF                           xor edi, edi
00A8CD12  48 8B D8                        mov rbx, rax
00A8CD15  48 85 C0                        test rax, rax
00A8CD18  0F 84 E5 ED FF FF               je 0x140a8bb03
00A8CD1E  48 8B 05 83 9E 53 00            mov rax, qword ptr [rip + 0x539e83]
00A8CD25  48 8D 0D 7C 9E 53 00            lea rcx, [rip + 0x539e7c]
00A8CD2C  48 3B C1                        cmp rax, rcx
00A8CD2F  74 1B                           je 0x140a8cd4c
00A8CD31  48 8B 88 A8 01 00 00            mov rcx, qword ptr [rax + 0x1a8]
00A8CD38  48 85 C9                        test rcx, rcx
00A8CD3B  75 05                           jne 0x140a8cd42
00A8CD3D  48 8B 00                        mov rax, qword ptr [rax]
00A8CD40  EB E3                           jmp 0x140a8cd25
00A8CD42  48 8B C1                        mov rax, rcx
00A8CD45  E8 86 DD C2 FF                  call 0x1406baad0
00A8CD4A  EB 02                           jmp 0x140a8cd4e
00A8CD4C  8B C7                           mov eax, edi
00A8CD4E  89 03                           mov dword ptr [rbx], eax
00A8CD50  49 89 1F                        mov qword ptr [r15], rbx
00A8CD53  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
00A8CD5B  E9 D1 ED FF FF                  jmp 0x140a8bb31
00A8CD60  83 FB 59                        cmp ebx, 0x59
00A8CD63  0F 8F DC 03 00 00               jg 0x140a8d145
00A8CD69  0F 84 60 03 00 00               je 0x140a8d0cf
00A8CD6F  83 FB 54                        cmp ebx, 0x54
00A8CD72  0F 8F 74 02 00 00               jg 0x140a8cfec
00A8CD78  0F 84 2D 02 00 00               je 0x140a8cfab
00A8CD7E  83 EB 4F                        sub ebx, 0x4f
00A8CD81  0F 84 4F 01 00 00               je 0x140a8ced6
00A8CD87  83 EB 01                        sub ebx, 1
00A8CD8A  0F 84 08 01 00 00               je 0x140a8ce98
00A8CD90  83 EB 01                        sub ebx, 1
00A8CD93  0F 84 B4 00 00 00               je 0x140a8ce4d
00A8CD99  83 EB 01                        sub ebx, 1
00A8CD9C  74 3C                           je 0x140a8cdda
00A8CD9E  83 FB 01                        cmp ebx, 1
00A8CDA1  0F 85 A1 ED FF FF               jne 0x140a8bb48
00A8CDA7  41 83 FE 10                     cmp r14d, 0x10
00A8CDAB  0F 85 97 ED FF FF               jne 0x140a8bb48
00A8CDB1  48 85 FF                        test rdi, rdi
00A8CDB4  0F 84 8E ED FF FF               je 0x140a8bb48
00A8CDBA  44 39 4D 6F                     cmp dword ptr [rbp + 0x6f], r9d
00A8CDBE  0F 85 84 ED FF FF               jne 0x140a8bb48
00A8CDC4  48 85 F6                        test rsi, rsi
00A8CDC7  0F 85 7B ED FF FF               jne 0x140a8bb48
00A8CDCD  48 8B CF                        mov rcx, rdi
00A8CDD0  E8 1B EC CD FF                  call 0x14076b9f0
00A8CDD5  E9 C6 ED FF FF                  jmp 0x140a8bba0
00A8CDDA  41 83 FE 0C                     cmp r14d, 0xc
00A8CDDE  0F 85 64 ED FF FF               jne 0x140a8bb48
00A8CDE4  48 85 FF                        test rdi, rdi
00A8CDE7  0F 84 5B ED FF FF               je 0x140a8bb48
00A8CDED  44 39 4D 6F                     cmp dword ptr [rbp + 0x6f], r9d
00A8CDF1  0F 85 51 ED FF FF               jne 0x140a8bb48
00A8CDF7  48 85 F6                        test rsi, rsi
00A8CDFA  0F 85 48 ED FF FF               jne 0x140a8bb48
00A8CE00  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00A8CE09  4C 89 4D 9F                     mov qword ptr [rbp - 0x61], r9
00A8CE0D  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00A8CE14  E8 D7 2A 7A FF                  call 0x14022f8f0
00A8CE19  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00A8CE22  89 45 9F                        mov dword ptr [rbp - 0x61], eax
00A8CE25  8A 47 08                        mov al, byte ptr [rdi + 8]
00A8CE28  C6 45 A3 01                     mov byte ptr [rbp - 0x5d], 1
00A8CE2C  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00A8CE33  88 45 A4                        mov byte ptr [rbp - 0x5c], al
00A8CE36  E8 B5 2A 7A FF                  call 0x14022f8f0
00A8CE3B  48 8D 55 9F                     lea rdx, [rbp - 0x61]
00A8CE3F  8B C8                           mov ecx, eax
00A8CE41  E8 1A F1 CD FF                  call 0x14076bf60
00A8CE46  33 C0                           xor eax, eax
00A8CE48  E9 53 ED FF FF                  jmp 0x140a8bba0
00A8CE4D  41 83 FE 28                     cmp r14d, 0x28
00A8CE51  0F 85 F1 EC FF FF               jne 0x140a8bb48
00A8CE57  48 85 FF                        test rdi, rdi
00A8CE5A  0F 84 E8 EC FF FF               je 0x140a8bb48
00A8CE60  83 7D 6F 10                     cmp dword ptr [rbp + 0x6f], 0x10
00A8CE64  0F 85 DE EC FF FF               jne 0x140a8bb48
00A8CE6A  48 85 F6                        test rsi, rsi
00A8CE6D  0F 84 D5 EC FF FF               je 0x140a8bb48
00A8CE73  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00A8CE7C  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00A8CE83  E8 68 2A 7A FF                  call 0x14022f8f0
00A8CE88  48 8D 57 08                     lea rdx, [rdi + 8]
00A8CE8C  4C 8B C6                        mov r8, rsi
00A8CE8F  8B C8                           mov ecx, eax
00A8CE91  E8 FE 69 E8 FF                  call 0x140913894
00A8CE96  EB AE                           jmp 0x140a8ce46
00A8CE98  41 83 FE 08                     cmp r14d, 8
00A8CE9C  0F 85 A6 EC FF FF               jne 0x140a8bb48
00A8CEA2  48 85 FF                        test rdi, rdi
00A8CEA5  0F 84 9D EC FF FF               je 0x140a8bb48
00A8CEAB  44 39 4D 6F                     cmp dword ptr [rbp + 0x6f], r9d
00A8CEAF  0F 85 93 EC FF FF               jne 0x140a8bb48
00A8CEB5  48 85 F6                        test rsi, rsi
00A8CEB8  0F 85 8A EC FF FF               jne 0x140a8bb48
00A8CEBE  E8 D5 44 C7 FF                  call 0x140701398
00A8CEC3  48 89 05 46 B3 54 00            mov qword ptr [rip + 0x54b346], rax
00A8CECA  C6 05 37 B3 54 00 01            mov byte ptr [rip + 0x54b337], 1
00A8CED1  E9 70 FF FF FF                  jmp 0x140a8ce46
00A8CED6  48 85 FF                        test rdi, rdi
00A8CED9  0F 84 69 EC FF FF               je 0x140a8bb48
00A8CEDF  41 83 FE 0C                     cmp r14d, 0xc
00A8CEE3  0F 85 5F EC FF FF               jne 0x140a8bb48
00A8CEE9  8B 77 08                        mov esi, dword ptr [rdi + 8]
00A8CEEC  48 8D 55 9B                     lea rdx, [rbp - 0x65]
00A8CEF0  44 89 4D 9B                     mov dword ptr [rbp - 0x65], r9d
00A8CEF4  8B CE                           mov ecx, esi
00A8CEF6  45 33 C9                        xor r9d, r9d
00A8CEF9  45 33 C0                        xor r8d, r8d
00A8CEFC  E8 BF 81 00 00                  call 0x140a950c0
00A8CF01  8B D8                           mov ebx, eax
00A8CF03  85 C0                           test eax, eax
00A8CF05  0F 88 52 EB FF FF               js 0x140a8ba5d
00A8CF0B  83 7D 6F 04                     cmp dword ptr [rbp + 0x6f], 4
00A8CF0F  8B 45 9B                        mov eax, dword ptr [rbp - 0x65]
00A8CF12  8D 0C 40                        lea ecx, [rax + rax*2]
00A8CF15  8D 3C CD 08 00 00 00            lea edi, [rcx*8 + 8]
00A8CF1C  75 35                           jne 0x140a8cf53
00A8CF1E  41 8D 56 F8                     lea edx, [r14 - 8]
00A8CF22  B9 00 01 00 00                  mov ecx, 0x100
00A8CF27  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8CF2D  E8 BE 51 0F 00                  call 0x140b820f0
00A8CF32  48 8B C8                        mov rcx, rax
00A8CF35  48 85 C0                        test rax, rax
00A8CF38  0F 84 C5 EB FF FF               je 0x140a8bb03
00A8CF3E  8B 45 9B                        mov eax, dword ptr [rbp - 0x65]
00A8CF41  89 01                           mov dword ptr [rcx], eax
00A8CF43  49 89 0F                        mov qword ptr [r15], rcx
00A8CF46  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
00A8CF4E  E9 A9 EC FF FF                  jmp 0x140a8bbfc
00A8CF53  39 7D 6F                        cmp dword ptr [rbp + 0x6f], edi
00A8CF56  0F 82 7B EB FF FF               jb 0x140a8bad7
00A8CF5C  8B D7                           mov edx, edi
00A8CF5E  B9 40 00 00 00                  mov ecx, 0x40
00A8CF63  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8CF69  E8 82 51 0F 00                  call 0x140b820f0
00A8CF6E  4C 8B C0                        mov r8, rax
00A8CF71  48 85 C0                        test rax, rax
00A8CF74  0F 84 89 EB FF FF               je 0x140a8bb03
00A8CF7A  41 89 3C 24                     mov dword ptr [r12], edi
00A8CF7E  48 8D 55 9B                     lea rdx, [rbp - 0x65]
00A8CF82  41 C6 45 00 01                  mov byte ptr [r13], 1
00A8CF87  8B CE                           mov ecx, esi
00A8CF89  49 89 07                        mov qword ptr [r15], rax
00A8CF8C  8B 45 9B                        mov eax, dword ptr [rbp - 0x65]
00A8CF8F  41 89 00                        mov dword ptr [r8], eax
00A8CF92  49 83 C0 08                     add r8, 8
00A8CF96  8B 45 9B                        mov eax, dword ptr [rbp - 0x65]
00A8CF99  44 8D 0C 40                     lea r9d, [rax + rax*2]
00A8CF9D  41 C1 E1 03                     shl r9d, 3
00A8CFA1  E8 1A 81 00 00                  call 0x140a950c0
00A8CFA6  E9 F5 EB FF FF                  jmp 0x140a8bba0
00A8CFAB  48 85 F6                        test rsi, rsi
00A8CFAE  0F 84 94 EB FF FF               je 0x140a8bb48
00A8CFB4  41 BE A0 00 00 00               mov r14d, 0xa0
00A8CFBA  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8CFC0  41 8B D6                        mov edx, r14d
00A8CFC3  41 8D 4E 60                     lea ecx, [r14 + 0x60]
00A8CFC7  E8 24 51 0F 00                  call 0x140b820f0
00A8CFCC  48 8B F8                        mov rdi, rax
00A8CFCF  48 85 C0                        test rax, rax
00A8CFD2  0F 84 2B EB FF FF               je 0x140a8bb03
00A8CFD8  41 8D 4E B4                     lea ecx, [r14 - 0x4c]
00A8CFDC  48 8B D7                        mov rdx, rdi
00A8CFDF  45 8B C6                        mov r8d, r14d
00A8CFE2  E8 51 41 00 00                  call 0x140a91138
00A8CFE7  E9 DA FA FF FF                  jmp 0x140a8cac6
00A8CFEC  83 EB 55                        sub ebx, 0x55
00A8CFEF  0F 84 A3 00 00 00               je 0x140a8d098
00A8CFF5  83 EB 01                        sub ebx, 1
00A8CFF8  74 47                           je 0x140a8d041
00A8CFFA  83 EB 01                        sub ebx, 1
00A8CFFD  74 19                           je 0x140a8d018
00A8CFFF  83 FB 01                        cmp ebx, 1
00A8D002  0F 85 40 EB FF FF               jne 0x140a8bb48
00A8D008  45 8B C6                        mov r8d, r14d
00A8D00B  48 8B D7                        mov rdx, rdi
00A8D00E  E8 21 6B FD FF                  call 0x140a63b34
00A8D013  E9 88 EB FF FF                  jmp 0x140a8bba0
00A8D018  48 85 FF                        test rdi, rdi
00A8D01B  0F 84 27 EB FF FF               je 0x140a8bb48
00A8D021  41 83 FE 18                     cmp r14d, 0x18
00A8D025  0F 85 1D EB FF FF               jne 0x140a8bb48
00A8D02B  48 85 F6                        test rsi, rsi
00A8D02E  0F 85 14 EB FF FF               jne 0x140a8bb48
00A8D034  48 8B CF                        mov rcx, rdi
00A8D037  E8 D4 C2 B4 FF                  call 0x1405d9310
00A8D03C  E9 5F EB FF FF                  jmp 0x140a8bba0
00A8D041  41 83 FE 08                     cmp r14d, 8
00A8D045  0F 82 8C EA FF FF               jb 0x140a8bad7
00A8D04B  48 85 F6                        test rsi, rsi
00A8D04E  0F 84 83 EA FF FF               je 0x140a8bad7
00A8D054  BA 08 00 00 00                  mov edx, 8
00A8D059  B9 00 01 00 00                  mov ecx, 0x100
00A8D05E  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8D064  E8 87 50 0F 00                  call 0x140b820f0
00A8D069  33 D2                           xor edx, edx
00A8D06B  48 8B C8                        mov rcx, rax
00A8D06E  48 85 C0                        test rax, rax
00A8D071  0F 84 8C EA FF FF               je 0x140a8bb03
00A8D077  8B 05 EF B4 3D 00               mov eax, dword ptr [rip + 0x3db4ef]
00A8D07D  89 01                           mov dword ptr [rcx], eax
00A8D07F  8B 05 E3 B4 3D 00               mov eax, dword ptr [rip + 0x3db4e3]
00A8D085  89 41 04                        mov dword ptr [rcx + 4], eax
00A8D088  49 89 0F                        mov qword ptr [r15], rcx
00A8D08B  41 C7 04 24 08 00 00 00         mov dword ptr [r12], 8
00A8D093  E9 E9 F0 FF FF                  jmp 0x140a8c181
00A8D098  48 85 F6                        test rsi, rsi
00A8D09B  0F 84 A7 EA FF FF               je 0x140a8bb48
00A8D0A1  41 BE 58 00 00 00               mov r14d, 0x58
00A8D0A7  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8D0AD  41 8B D6                        mov edx, r14d
00A8D0B0  B9 00 01 00 00                  mov ecx, 0x100
00A8D0B5  E8 36 50 0F 00                  call 0x140b820f0
00A8D0BA  48 8B F8                        mov rdi, rax
00A8D0BD  48 85 C0                        test rax, rax
00A8D0C0  0F 84 3D EA FF FF               je 0x140a8bb03
00A8D0C6  41 8D 4E FD                     lea ecx, [r14 - 3]
00A8D0CA  E9 0D FF FF FF                  jmp 0x140a8cfdc
00A8D0CF  48 85 F6                        test rsi, rsi
00A8D0D2  0F 84 FF E9 FF FF               je 0x140a8bad7
00A8D0D8  83 7D 6F 14                     cmp dword ptr [rbp + 0x6f], 0x14
00A8D0DC  0F 85 F5 E9 FF FF               jne 0x140a8bad7
00A8D0E2  E8 D9 B2 0E 00                  call 0x140b783c0
00A8D0E7  33 DB                           xor ebx, ebx
00A8D0E9  38 1D E4 FD 47 00               cmp byte ptr [rip + 0x47fde4], bl
00A8D0EF  74 4A                           je 0x140a8d13b
00A8D0F1  8D 53 14                        lea edx, [rbx + 0x14]
00A8D0F4  B9 00 01 00 00                  mov ecx, 0x100
00A8D0F9  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8D0FF  E8 EC 4F 0F 00                  call 0x140b820f0
00A8D104  48 85 C0                        test rax, rax
00A8D107  74 28                           je 0x140a8d131
00A8D109  0F 10 05 D0 BF 47 00            movups xmm0, xmmword ptr [rip + 0x47bfd0]
00A8D110  0F 11 00                        movups xmmword ptr [rax], xmm0
00A8D113  8B 0D D7 BF 47 00               mov ecx, dword ptr [rip + 0x47bfd7]
00A8D119  89 48 10                        mov dword ptr [rax + 0x10], ecx
00A8D11C  49 89 07                        mov qword ptr [r15], rax
00A8D11F  41 C7 04 24 14 00 00 00         mov dword ptr [r12], 0x14
00A8D127  41 C6 45 00 01                  mov byte ptr [r13], 1
00A8D12C  E9 E6 EB FF FF                  jmp 0x140a8bd17
00A8D131  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A8D136  E9 DC EB FF FF                  jmp 0x140a8bd17
00A8D13B  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00A8D140  E9 D2 EB FF FF                  jmp 0x140a8bd17
00A8D145  83 FB 5F                        cmp ebx, 0x5f
00A8D148  0F 8F 6C 01 00 00               jg 0x140a8d2ba
00A8D14E  0F 84 BB 02 00 00               je 0x140a8d40f
00A8D154  83 EB 5A                        sub ebx, 0x5a
00A8D157  0F 84 2E 01 00 00               je 0x140a8d28b
00A8D15D  83 EB 01                        sub ebx, 1
00A8D160  0F 84 C6 00 00 00               je 0x140a8d22c
00A8D166  83 EB 01                        sub ebx, 1
00A8D169  0F 84 9C 00 00 00               je 0x140a8d20b
00A8D16F  83 EB 01                        sub ebx, 1
00A8D172  74 4B                           je 0x140a8d1bf
00A8D174  83 FB 01                        cmp ebx, 1
00A8D177  0F 85 CB E9 FF FF               jne 0x140a8bb48
00A8D17D  41 83 FE 0C                     cmp r14d, 0xc
00A8D181  0F 82 50 E9 FF FF               jb 0x140a8bad7
00A8D187  48 85 F6                        test rsi, rsi
00A8D18A  0F 84 B8 E9 FF FF               je 0x140a8bb48
00A8D190  8D 53 07                        lea edx, [rbx + 7]
00A8D193  B9 00 01 00 00                  mov ecx, 0x100
00A8D198  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8D19E  E8 4D 4F 0F 00                  call 0x140b820f0
00A8D1A3  48 8B F0                        mov rsi, rax
00A8D1A6  48 85 C0                        test rax, rax
00A8D1A9  0F 84 54 E9 FF FF               je 0x140a8bb03
00A8D1AF  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00A8D1B2  48 8B D0                        mov rdx, rax
00A8D1B5  E8 9A 72 B4 FF                  call 0x1405d4454
00A8D1BA  E9 45 F5 FF FF                  jmp 0x140a8c704
00A8D1BF  85 D2                           test edx, edx
00A8D1C1  0F 85 91 E8 FF FF               jne 0x140a8ba58
00A8D1C7  48 85 F6                        test rsi, rsi
00A8D1CA  0F 84 78 E9 FF FF               je 0x140a8bb48
00A8D1D0  BA 08 00 00 00                  mov edx, 8
00A8D1D5  B9 00 01 00 00                  mov ecx, 0x100
00A8D1DA  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8D1E0  E8 0B 4F 0F 00                  call 0x140b820f0
00A8D1E5  33 FF                           xor edi, edi
00A8D1E7  48 8B D8                        mov rbx, rax
00A8D1EA  48 85 C0                        test rax, rax
00A8D1ED  0F 84 10 E9 FF FF               je 0x140a8bb03
00A8D1F3  48 8B C8                        mov rcx, rax
00A8D1F6  E8 2D DB CC FF                  call 0x14075ad28
00A8D1FB  49 89 1F                        mov qword ptr [r15], rbx
00A8D1FE  41 C7 04 24 08 00 00 00         mov dword ptr [r12], 8
00A8D206  E9 26 E9 FF FF                  jmp 0x140a8bb31
00A8D20B  44 8B 4D 6F                     mov r9d, dword ptr [rbp + 0x6f]
00A8D20F  4C 8B C6                        mov r8, rsi
00A8D212  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00A8D217  41 8B D6                        mov edx, r14d
00A8D21A  48 8B CF                        mov rcx, rdi
00A8D21D  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00A8D222  E8 D1 AF CC FF                  call 0x1407581f8
00A8D227  E9 74 E9 FF FF                  jmp 0x140a8bba0
00A8D22C  48 85 F6                        test rsi, rsi
00A8D22F  0F 84 A2 E8 FF FF               je 0x140a8bad7
00A8D235  41 BE 24 00 00 00               mov r14d, 0x24
00A8D23B  44 39 75 6F                     cmp dword ptr [rbp + 0x6f], r14d
00A8D23F  0F 82 92 E8 FF FF               jb 0x140a8bad7
00A8D245  41 B8 4D 65 6D 20               mov r8d, 0x206d654d
00A8D24B  41 8B D6                        mov edx, r14d
00A8D24E  B9 00 01 00 00                  mov ecx, 0x100
00A8D253  E8 98 4E 0F 00                  call 0x140b820f0
00A8D258  33 F6                           xor esi, esi
00A8D25A  48 8B F8                        mov rdi, rax
00A8D25D  48 85 C0                        test rax, rax
00A8D260  0F 84 9D E8 FF FF               je 0x140a8bb03
00A8D266  48 8B C8                        mov rcx, rax
00A8D269  E8 B2 1C B4 FF                  call 0x1405cef20
00A8D26E  8B D8                           mov ebx, eax
00A8D270  85 C0                           test eax, eax
00A8D272  0F 88 67 E9 FF FF               js 0x140a8bbdf
00A8D278  49 89 3F                        mov qword ptr [r15], rdi
00A8D27B  8B DE                           mov ebx, esi
00A8D27D  45 89 34 24                     mov dword ptr [r12], r14d
00A8D281  41 C6 45 00 01                  mov byte ptr [r13], 1
00A8D286  E9 D2 E7 FF FF                  jmp 0x140a8ba5d
00A8D28B  48 85 FF                        test rdi, rdi
00A8D28E  0F 84 B4 E8 FF FF               je 0x140a8bb48
00A8D294  41 83 FE 14                     cmp r14d, 0x14
00A8D298  0F 82 AA E8 FF FF               jb 0x140a8bb48
00A8D29E  48 85 F6                        test rsi, rsi
00A8D2A1  74 0A                           je 0x140a8d2ad
00A8D2A3  44 39 4D 6F                     cmp dword ptr [rbp + 0x6f], r9d
00A8D2A7  0F 85 9B E8 FF FF               jne 0x140a8bb48
00A8D2AD  48 8B CF                        mov rcx, rdi
00A8D2B0  E8 8F 12 02 00                  call 0x140aae544
00A8D2B5  E9 E6 E8 FF FF                  jmp 0x140a8bba0
00A8D2BA  8B CB                           mov ecx, ebx
00A8D2BC  83 E9 60                        sub ecx, 0x60
00A8D2BF  0F 84 4A 01 00 00               je 0x140a8d40f
00A8D2C5  83 E9 01                        sub ecx, 1
00A8D2C8  0F 84 FD 00 00 00               je 0x140a8d3cb
00A8D2CE  83 E9 01                        sub ecx, 1
00A8D2D1  74 3F                           je 0x140a8d312
00A8D2D3  83 F9 01                        cmp ecx, 1
00A8D2D6  0F 85 6C E8 FF FF               jne 0x140a8bb48
00A8D2DC  E8 F7 3F B4 FF                  call 0x1405d12d8
00A8D2E1  85 C0                           test eax, eax
00A8D2E3  0F 84 5F E8 FF FF               je 0x140a8bb48
00A8D2E9  48 85 FF                        test rdi, rdi
00A8D2EC  0F 84 56 E8 FF FF               je 0x140a8bb48
00A8D2F2  48 85 F6                        test rsi, rsi
00A8D2F5  0F 85 4D E8 FF FF               jne 0x140a8bb48
00A8D2FB  41 83 FE 0C                     cmp r14d, 0xc
00A8D2FF  0F 82 D2 E7 FF FF               jb 0x140a8bad7
00A8D305  8A 4F 08                        mov cl, byte ptr [rdi + 8]
00A8D308  E8 47 9C CD FF                  call 0x140766f54
00A8D30D  E9 8E E8 FF FF                  jmp 0x140a8bba0
00A8D312  E8 89 8A A6 FF                  call 0x1404f5da0
00A8D317  45 33 FF                        xor r15d, r15d
00A8D31A  85 C0                           test eax, eax
00A8D31C  0F 84 26 E8 FF FF               je 0x140a8bb48
00A8D322  48 8D 55 97                     lea rdx, [rbp - 0x69]
00A8D326  44 88 7D 97                     mov byte ptr [rbp - 0x69], r15b
00A8D32A  33 C9                           xor ecx, ecx
00A8D32C  E8 43 47 F9 FF                  call 0x140a21a74
00A8D331  8B D8                           mov ebx, eax
00A8D333  85 C0                           test eax, eax
00A8D335  0F 88 22 E7 FF FF               js 0x140a8ba5d
00A8D33B  44 38 7D 97                     cmp byte ptr [rbp - 0x69], r15b
00A8D33F  0F 85 4E E5 FF FF               jne 0x140a8b893
00A8D345  44 39 7D 9F                     cmp dword ptr [rbp - 0x61], r15d
00A8D349  0F 85 F9 E7 FF FF               jne 0x140a8bb48
00A8D34F  41 83 FE 30                     cmp r14d, 0x30
00A8D353  75 6C                           jne 0x140a8d3c1
00A8D355  48 85 F6                        test rsi, rsi
00A8D358  74 67                           je 0x140a8d3c1
00A8D35A  83 7D 6F 10                     cmp dword ptr [rbp + 0x6f], 0x10
00A8D35E  75 61                           jne 0x140a8d3c1
00A8D360  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00A8D369  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00A8D370  E8 7B 25 7A FF                  call 0x14022f8f0
00A8D375  4C 8D 47 10                     lea r8, [rdi + 0x10]
00A8D379  4C 8B CE                        mov r9, rsi
00A8D37C  48 8D 57 08                     lea rdx, [rdi + 8]
00A8D380  8B C8                           mov ecx, eax
00A8D382  E8 21 EB CD FF                  call 0x14076bea8
00A8D387  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00A8D390  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00A8D397  E8 54 25 7A FF                  call 0x14022f8f0
00A8D39C  8B C8                           mov ecx, eax
00A8D39E  48 8B 05 F3 A3 3D 00            mov rax, qword ptr [rip + 0x3da3f3]
00A8D3A5  48 85 C0                        test rax, rax
00A8D3A8  74 0F                           je 0x140a8d3b9
00A8D3AA  44 8B 4F 0C                     mov r9d, dword ptr [rdi + 0xc]
00A8D3AE  33 D2                           xor edx, edx
00A8D3B0  44 8A 47 08                     mov r8b, byte ptr [rdi + 8]
00A8D3B4  E8 17 D7 C2 FF                  call 0x1406baad0
00A8D3B9  41 8B DF                        mov ebx, r15d
00A8D3BC  E9 9C E6 FF FF                  jmp 0x140a8ba5d
00A8D3C1  BB 06 02 00 C0                  mov ebx, 0xc0000206
00A8D3C6  E9 92 E6 FF FF                  jmp 0x140a8ba5d
00A8D3CB  41 83 FE 0C                     cmp r14d, 0xc
00A8D3CF  0F 85 73 E7 FF FF               jne 0x140a8bb48
00A8D3D5  48 85 F6                        test rsi, rsi
00A8D3D8  0F 84 6A E7 FF FF               je 0x140a8bb48
00A8D3DE  44 39 55 6F                     cmp dword ptr [rbp + 0x6f], r10d
00A8D3E2  0F 85 60 E7 FF FF               jne 0x140a8bb48
00A8D3E8  44 88 0E                        mov byte ptr [rsi], r9b
00A8D3EB  E8 B0 89 A6 FF                  call 0x1404f5da0
00A8D3F0  33 C9                           xor ecx, ecx
00A8D3F2  85 C0                           test eax, eax
00A8D3F4  0F 84 70 E7 FF FF               je 0x140a8bb6a
00A8D3FA  81 7F 08 27 7A 93 03            cmp dword ptr [rdi + 8], 0x3937a27
00A8D401  0F 85 63 E7 FF FF               jne 0x140a8bb6a
00A8D407  C6 06 01                        mov byte ptr [rsi], 1
00A8D40A  E9 5B E7 FF FF                  jmp 0x140a8bb6a
00A8D40F  41 83 FE 0C                     cmp r14d, 0xc
00A8D413  0F 85 2F E7 FF FF               jne 0x140a8bb48
00A8D419  48 85 F6                        test rsi, rsi
00A8D41C  0F 85 26 E7 FF FF               jne 0x140a8bb48
00A8D422  44 39 4F 04                     cmp dword ptr [rdi + 4], r9d
00A8D426  0F 85 1C E7 FF FF               jne 0x140a8bb48
00A8D42C  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00A8D42F  83 F9 20                        cmp ecx, 0x20
00A8D432  0F 83 10 E7 FF FF               jae 0x140a8bb48
00A8D438  83 FB 5F                        cmp ebx, 0x5f
00A8D43B  0F 94 C2                        sete dl
00A8D43E  E8 DD 2D FF FF                  call 0x140a80220
00A8D443  E9 58 E7 FF FF                  jmp 0x140a8bba0
00A8D448  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
00A8D44C  48 33 CC                        xor rcx, rsp
00A8D44F  E8 EC F1 C1 FF                  call 0x1406ac640
00A8D454  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
00A8D45C  48 81 C4 B0 00 00 00            add rsp, 0xb0
00A8D463  41 5F                           pop r15
00A8D465  41 5E                           pop r14
00A8D467  41 5D                           pop r13
00A8D469  41 5C                           pop r12
00A8D46B  5F                              pop rdi
00A8D46C  5E                              pop rsi
00A8D46D  5D                              pop rbp
00A8D46E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPowerInformationInternal(int a1, int a2, __int64 a3, int a4, __int64 a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m3F;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned int v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int16 v_stack_m76;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned __int8 v_stack_m9B;
    unsigned __int8 v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA4;
    unsigned __int8 v_stack_mA6;
    unsigned __int8 v_stack_mA7;
    unsigned __int8 v_stack_mA8;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 3665757)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m78 = v_xmm0;
    a4 = 0;
    *(unsigned __int64 *)(a7) = 0;
    *(unsigned int *)(a8) = 0;
    *(unsigned __int8 *)(a9) = 0;
    v_stack_mA0 = a2;
    v_stack_mA7 = 0;
    v_stack_mA8 = 0;
    v_stack_m90 = 0;
    v_stack_m98 = 0;
    v_stack_m88 = 0;
    v_stack_m80 = 0;
    v_stack_m94 = 0;
    v_stack_m68 = 0;
    v_stack_mA6 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00A8BA36;
    if (((unsigned int)((unsigned int)(a1))) > 28) goto loc_00A8B86A;
    if (((unsigned int)((unsigned int)(a1))) < 28) goto loc_00A8B893;
loc_00A8B86A:
    if (((unsigned int)((unsigned int)(a1) - 40)) > 56) goto loc_00A8B882;
    if (((unsigned int)((unsigned int)(a1) - 40)) < 56) goto loc_00A8B893;
loc_00A8B882:
    result = Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), a2, a3, a4);
    a4 = 0;
    if ((unsigned int)(result) == 0) goto loc_00A8B89D;
    if (((unsigned int)((unsigned int)(a1))) != 98) goto loc_00A8B89D;
loc_00A8B893:
    goto loc_00A8BA5D;
loc_00A8B89D:
    if (((unsigned int)((unsigned int)(0xC0000022ULL) - 29)) > 35) goto loc_00A8B8C1;
    if (((unsigned int)((unsigned int)(0xC0000022ULL) - 29)) >= 35) goto loc_00A8B8C1;
    result = EtwpCoverageUserIsAdmin(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), a2, a3, a4);
    a4 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00A8B893;
loc_00A8B8C1:
    if (((unsigned int)((unsigned int)(0xC0000022ULL) - 82)) > 1) goto loc_00A8B8D5;
    result = PopCheckTestsigningEnabled(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), a2, a3, a4);
    a4 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00A8B893;
loc_00A8B8D5:
    if (((unsigned int)((unsigned int)(0xC0000022ULL))) == 24) goto loc_00A8B8F2;
    if (((unsigned int)((unsigned int)(0xC0000022ULL) - 35)) > 55) goto loc_00A8B8FE;
    if (((unsigned int)((unsigned int)(0xC0000022ULL) - 35)) >= 55) goto loc_00A8B8FE;
loc_00A8B8F2:
    result = PopIsRunningAsLocalSystem(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), a2, a3, a4);
    a4 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00A8B893;
loc_00A8B8FE:
    if (((unsigned int)((unsigned int)(0xC0000022ULL))) != 80) goto loc_00A8B927;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5562915), v_stack_mA6, a3, a4);
    a4 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00A8CE98;
    goto loc_00A8BA5D;
loc_00A8B927:
    if (((unsigned int)((unsigned int)(0xC0000061ULL))) != 61) goto loc_00A8B991;
    result = PopCheckTestsigningEnabled(*(unsigned __int64 *)(v_rip + 5562915), v_stack_mA6, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A8B893;
    result = EtwpCoverageUserIsAdmin(*(unsigned __int64 *)(v_rip + 5562915), v_stack_mA6, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A8B893;
loc_00A8B946:
    if (((unsigned int)((unsigned int)(a4))) < 12) goto loc_00A8BB48;
    if (a5 == 0) goto loc_00A8BAD7;
    result = PopAcquireTransitionLock(8, v_stack_mA6, a3, a4);
    result = PopReadPagesFromHiberFile((unsigned int)(*(unsigned int *)(a3 + 8)), 1, a7, a4);
    result = PopReleaseTransitionLock(8, 1, a7, a4);
    result = 0;
    if (!sign_flag) goto loc_00A8C935;
    *(unsigned __int64 *)(a7) = 0;
    goto loc_00A8BA5D;
loc_00A8B991:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 45) goto loc_00A8B9C4;
    result = PopIsRunningAsLocalSystem(8, 1, a7, a4);
    v_rbx = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00A8C5D1;
    result = PopCheckTestsigningEnabled(8, 1, a7, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A8B893;
    result = EtwpCoverageUserIsAdmin(8, 1, a7, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A8C5D1;
    goto loc_00A8B893;
loc_00A8B9C4:
    if (0 != 25) goto loc_00A8BA65;
    v_stack_m78 = v_xmm0;
loc_00A8B9E9:
    if ((*(unsigned __int16 *)(v_rip + 484057)) == 0) goto loc_00A8B9FA;
    a1 = (v_rip + 484057) + (v_rbx - 23);
    a3 = ((unsigned int)((unsigned int)((unsigned int)(0x7FFFULL)))) - (1);
    if (condition_is_not_equal) goto loc_00A8B9E9;
    goto loc_00A8BA0F;
loc_00A8B9FA:
    result = ((unsigned int)(0x7FFFULL)) - (a3);
    v_stack_m70 = v_rip + 484057;
    result = (unsigned __int16)((result) + ((unsigned __int16)(result)));
    v_stack_m78 = (unsigned __int16)(result);
    result = (unsigned __int16)((result) + ((unsigned __int16)(v_rbx - 23)));
    v_stack_m76 = (unsigned __int16)(result);
loc_00A8BA0F:
    a1 = 0;
    result = RtlCapabilityCheckForSingleSessionSku(a1, v_stack_m78, v_stack_mA7, a4);
    a4 = 0;
    if (sign_flag) goto loc_00A8BA5D;
    if (v_stack_mA7 != 0) goto loc_00A8BE76;
    goto loc_00A8B893;
loc_00A8BA36:
    if (((unsigned int)((unsigned int)((unsigned int)(result)) - 24)) > 59) goto loc_00A8BA4E;
    if (((unsigned int)((unsigned int)((unsigned int)(result)) - 24)) < 59) goto loc_00A8BA58;
loc_00A8BA4E:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 5) goto loc_00A8BA58;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 7) goto loc_00A8BA71;
loc_00A8BA58:
loc_00A8BA5D:
    goto loc_00A8D448;
loc_00A8BA65:
loc_00A8BA71:
    if (((unsigned int)((unsigned int)(0xC00000BBULL))) > 54) goto loc_00A8C849;
    if (((unsigned int)((unsigned int)(0xC00000BBULL))) == 54) goto loc_00A8C769;
    if (((unsigned int)((unsigned int)(0xC00000BBULL))) > 31) goto loc_00A8C23C;
    if (((unsigned int)((unsigned int)(0xC00000BBULL))) == 31) goto loc_00A8C3F9;
    if (((unsigned int)((unsigned int)(0xC00000BBULL))) > 20) goto loc_00A8BE3E;
    if (((unsigned int)((unsigned int)(0xC00000BBULL))) == 20) goto loc_00A8BE17;
    if (((unsigned int)((unsigned int)(0xC00000BBULL))) > 5) goto loc_00A8BC82;
    if (((unsigned int)((unsigned int)(0xC00000BBULL))) == 5) goto loc_00A8BC62;
    if ((unsigned int)((unsigned int)(0xC00000BBULL)) == 0) goto loc_00A8BC06;
    v_rbx = (unsigned int)(((unsigned int)(0xC00000BBULL)) - (1));
    if (condition_is_equal) goto loc_00A8BBA7;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8BB71;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8BB3D;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A8BB48;
    if (((unsigned int)((unsigned int)(a4))) >= 8) goto loc_00A8BAE1;
loc_00A8BAD7:
    goto loc_00A8BA5D;
loc_00A8BAE1:
    if (a5 == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 1, (unsigned int)(0x206D654DULL), a4);
    v_rdi = 0;
    if (result != 0) goto loc_00A8BB0D;
loc_00A8BB03:
    goto loc_00A8BA5D;
loc_00A8BB0D:
    result = PopIsPlatformAoAcCapable(256, 1, (unsigned int)(0x206D654DULL), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A8BB21;
    result = RtlIsMultiSessionSku(256, 1, (unsigned int)(0x206D654DULL), a4);
    result = 1;
    if ((unsigned __int8)(result) == 0) {
        result = 0;
    }
    *(unsigned __int8 *)((unsigned int)(0xC000009AULL)) = (unsigned __int8)(result);
    *(unsigned __int64 *)(a7) = (unsigned int)(0xC000009AULL);
    *(unsigned int *)(a8) = 1;
loc_00A8BB31:
    *(unsigned __int8 *)(a9) = 1;
    goto loc_00A8BA5D;
loc_00A8BB3D:
    if (((unsigned int)((unsigned int)(a4))) < 16) goto loc_00A8BAD7;
    if (a5 == 0) goto loc_00A8BB52;
loc_00A8BB48:
    goto loc_00A8BA5D;
loc_00A8BB52:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4723636))))) == 0) goto loc_00A8BB48;
    a2 = 0;
    result = PopUpdateSmartUserPresencePredictions(*(unsigned __int64 *)(v_rdi + 8), a2, (unsigned int)(0x206D654DULL), a4);
loc_00A8BB68:
    a1 = 0;
loc_00A8BB6A:
    goto loc_00A8BA5D;
loc_00A8BB71:
    *(unsigned __int8 *)(v_rip + 4730689) = 1;
loc_00A8BB86:
    v_stack_mB8 = 0;
    v_stack_mC0 = 0;
    v_stack_mC8 = 0;
    a4 = 0;
    result = ZwUpdateWnfStateData(v_rip - 10924574, v_rip + 4730682, 1, a4);
loc_00A8BBA0:
    goto loc_00A8BA5D;
loc_00A8BBA7:
    if (a5 == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 8, (unsigned int)(0x206D654DULL), a4);
    if (result == 0) goto loc_00A8BB03;
    result = PopS0LowPowerIdleInfo(result, 8, (unsigned int)(0x206D654DULL), a4);
    if (!sign_flag) goto loc_00A8BBF1;
loc_00A8BBDF:
loc_00A8BBE7:
    result = ExFreePoolWithTag(result, (unsigned int)(0x206D654DULL), (unsigned int)(0x206D654DULL), a4);
    goto loc_00A8BA5D;
loc_00A8BBF1:
    *(unsigned __int64 *)(a7) = result;
loc_00A8BBF4:
    *(unsigned int *)(a8) = 8;
loc_00A8BBFC:
    *(unsigned __int8 *)(a9) = 1;
    goto loc_00A8BA5D;
loc_00A8BC06:
    if (((unsigned int)((unsigned int)(a4))) < 32) goto loc_00A8BAD7;
    if (a5 == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 16, (unsigned int)(0x206D654DULL), a4);
    if (result == 0) goto loc_00A8BB03;
    result = PopFxPlatformRegisterInterface(result, result, (unsigned int)(0x206D654DULL), a4);
    if (!sign_flag) goto loc_00A8BC55;
loc_00A8BC4B:
loc_00A8BC50:
    goto loc_00A8BBE7;
loc_00A8BC55:
    *(unsigned __int64 *)(a7) = result;
    *(unsigned int *)(a8) = 16;
    goto loc_00A8BBFC;
loc_00A8BC62:
    if (((unsigned int)((unsigned int)(a4))) < 12) goto loc_00A8BAD7;
    if (result != 0) goto loc_00A8BB48;
    result = PoLatencySensitivityHint((unsigned int)(*(unsigned int *)(result + 8)), (unsigned int)(0x206D654DULL), (unsigned int)(0x206D654DULL), a4);
    goto loc_00A8BB68;
loc_00A8BC82:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) - (6));
    if (condition_is_equal) goto loc_00A8BDF7;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8BD9A;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8BD7A;
    v_rbx = (unsigned int)((v_rbx) - (10));
    if (condition_is_equal) goto loc_00A8BD21;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A8BB48;
    if (((unsigned int)((unsigned int)(a4))) != 20) goto loc_00A8BB48;
    if (result != 0) goto loc_00A8BB48;
    result = TtmNotifySessionPowerStateChange((unsigned int)(*(unsigned int *)(result + 8)), *(unsigned __int8 *)(result + 12), (unsigned int)(0x206D654DULL), a4);
    v_r14 = 0;
    v_rbx = ((unsigned __int8)(*(unsigned __int8 *)(result + 12)) != 0) ? 1 : 0;
    result = PopAcquirePolicyLock((unsigned int)(*(unsigned int *)(result + 8)), *(unsigned __int8 *)(result + 12), (unsigned int)(0x206D654DULL), a4);
    if ((*(unsigned __int8 *)(result + 13)) == 0) goto loc_00A8BCFC;
    result = PopSetDisplayStatus((unsigned int)((unsigned int)(v_rbx)), *(unsigned __int8 *)(result + 12), (unsigned int)(0x206D654DULL), a4);
    result = PopUpdateConsoleDisplayState((unsigned int)((unsigned int)(v_rbx)), *(unsigned __int8 *)(result + 12), (unsigned int)(0x206D654DULL), a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(result + 12)) != 0) {
        result = PopPowerAggregatorNotifyDisplayPoweredOn((unsigned int)((unsigned int)(v_rbx)), *(unsigned __int8 *)(result + 12), (unsigned int)(0x206D654DULL), a4);
    }
    a1 = ((*(unsigned __int8 *)(result + 12)) == 0) ? 1 : 0;
    result = PopDiagTraceSessionDisplayStateChange(a1, (unsigned int)(*(unsigned int *)(result + 8)), *(unsigned __int8 *)(result + 13), (unsigned int)(*(unsigned int *)(result + 16)));
loc_00A8BD17:
    result = PopReleasePolicyLock(a1, (unsigned int)(*(unsigned int *)(result + 8)), *(unsigned __int8 *)(result + 13), (unsigned int)(*(unsigned int *)(result + 16)));
    goto loc_00A8BA5D;
loc_00A8BD21:
    result = PopIsPlatformAoAcCapable(a1, (unsigned int)(*(unsigned int *)(result + 8)), *(unsigned __int8 *)(result + 13), (unsigned int)(*(unsigned int *)(result + 16)));
    if ((unsigned __int8)(result) == 0) goto loc_00A8BA58;
    if (*(unsigned __int8 *)(result + 12) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(0x400ULL))), (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(result + 16)));
    if (result == 0) goto loc_00A8BB03;
    result = PopQueryBootSessionStandbyActivationInfo(result, (unsigned int)((unsigned int)((unsigned int)(0x400ULL))), (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(result + 16)));
    if (sign_flag) goto loc_00A8BA5D;
loc_00A8BD6E:
    *(unsigned __int64 *)(a7) = result;
loc_00A8BD71:
    *(unsigned int *)(a8) = (unsigned int)((unsigned int)(0x400ULL));
    goto loc_00A8BBFC;
loc_00A8BD7A:
    if (((unsigned int)((unsigned int)(0x400ULL))) < 8) goto loc_00A8BAD7;
    if (*(unsigned __int8 *)(result + 12) != 0) goto loc_00A8BB48;
    result = PopUpdateBackgroundCoolingStatus(*(unsigned __int8 *)(result + 8), (unsigned int)((unsigned int)((unsigned int)(0x400ULL))), (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(result + 16)));
    goto loc_00A8BBA0;
loc_00A8BD9A:
    if (((unsigned int)((unsigned int)(0x400ULL))) < 8) goto loc_00A8BAD7;
    if (*(unsigned __int8 *)(result + 12) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 32, (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(result + 16)));
    a1 = 0;
    if (result == 0) goto loc_00A8BB03;
    *(unsigned __int64 *)(result) = v_xmm0;
loc_00A8BDDE:
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(a7) = result;
    *(unsigned int *)(a8) = 32;
loc_00A8BDED:
    *(unsigned __int8 *)(a9) = 1;
    goto loc_00A8BB6A;
loc_00A8BDF7:
    if (((unsigned int)((unsigned int)(0x400ULL))) < 12) goto loc_00A8BAD7;
    if (*(unsigned __int8 *)(result + 12) != 0) goto loc_00A8BB48;
    result = PopNetUpdateStandbyRequest(*(unsigned __int8 *)(result + 8), 32, (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(result + 16)));
    goto loc_00A8BBA0;
loc_00A8BE17:
    if (((unsigned int)((unsigned int)(0x400ULL))) != 20) goto loc_00A8BB48;
    if (*(unsigned __int8 *)(result + 12) != 0) goto loc_00A8BB48;
    result = TtmNotifySessionTerminalInput((unsigned int)(*(unsigned int *)(result + 8)), (unsigned int)(*(unsigned int *)(result + 12)), *(unsigned __int8 *)(result + 16), (unsigned int)(*(unsigned int *)(result + 16)));
    goto loc_00A8BB68;
loc_00A8BE3E:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) > 26) goto loc_00A8C105;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 26) goto loc_00A8C07F;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) - (21));
    if (condition_is_equal) goto loc_00A8BFE0;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8BF72;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8BF5B;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8BEA8;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A8BB48;
loc_00A8BE76:
    if (((unsigned int)((unsigned int)(0x400ULL))) < 12) goto loc_00A8BAD7;
    if (*(unsigned __int8 *)(result + 12) != 0) goto loc_00A8BB48;
    if ((*(unsigned __int8 *)(result + 8)) == ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 16))))) goto loc_00A8BE99;
    result = PopScreenOn((unsigned int)(*(unsigned int *)(result + 8)), (unsigned int)(*(unsigned int *)(result + 12)), *(unsigned __int8 *)(result + 16), (unsigned int)(*(unsigned int *)(result + 16)));
    goto loc_00A8BB68;
loc_00A8BE99:
    result = PopScreenOff(30, (unsigned int)(*(unsigned int *)(result + 12)), *(unsigned __int8 *)(result + 16), (unsigned int)(*(unsigned int *)(result + 16)));
    goto loc_00A8BB68;
loc_00A8BEA8:
    if (((unsigned int)((unsigned int)(0x400ULL))) < 40) goto loc_00A8BAD7;
    if (*(unsigned __int8 *)(result + 12) != 0) goto loc_00A8BB48;
    if ((*(unsigned __int8 *)(v_rip + 4729846)) != ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 16))))) goto loc_00A8BF0D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 12)))) == ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_00A8BF15;
    v_stack_mB8 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 16)));
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 16)));
    v_stack_mC8 = (unsigned int)(*(unsigned int *)(result + 16));
    a4 = 0;
    *(unsigned __int8 *)(v_rip + 4729790) = 1;
    result = ZwUpdateWnfStateData(v_rip - 10925568, v_rip + 4729820, 1, a4);
    result = PopDiagTraceEventNoPayload(v_rip - 10935326, v_rip + 4729820, 1, a4);
    goto loc_00A8BF15;
loc_00A8BF0D:
    if (((unsigned int)(v_rip - 10935326)) == ((unsigned int)(result))) goto loc_00A8BA58;
loc_00A8BF15:
    v_stack_m60 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8)));
    v_stack_m5C = (unsigned int)((unsigned int)(*(unsigned int *)(result + 12)));
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 16)));
    v_stack_m54 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 20)));
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 24)));
    v_stack_m4C = (unsigned int)((unsigned int)(*(unsigned int *)(result + 28)));
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 32)));
    v_stack_m44 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 36)));
    result = PopBroadcastSessionInfo(32 - 28, 32, v_stack_m60, a4);
    goto loc_00A8BB68;
loc_00A8BF5B:
    if (((unsigned int)((unsigned int)(0x400ULL))) != 12) goto loc_00A8BB48;
    result = PopUpdateExternalDisplayState(*(unsigned __int8 *)(result + 8), 32, v_stack_m60, a4);
    goto loc_00A8BB68;
loc_00A8BF72:
    if (((unsigned int)((unsigned int)(0x400ULL))) < 8) goto loc_00A8BAD7;
    if (*(unsigned __int8 *)(result + 12) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 64, (unsigned int)(0x206D654DULL), a4);
    a1 = 0;
    if (result == 0) goto loc_00A8BB03;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = v_xmm1;
    *(unsigned __int64 *)(a7) = result;
    *(unsigned int *)(a8) = 64;
    goto loc_00A8BDED;
loc_00A8BFE0:
    if (((unsigned int)((unsigned int)(0x400ULL))) < 96) goto loc_00A8BAD7;
    if ((*(unsigned __int64 *)(result + 8)) != 0) goto loc_00A8BFF9;
    if (*(unsigned __int8 *)(result + 12) == 0) goto loc_00A8BAD7;
loc_00A8BFF9:
    if ((*(unsigned int *)(result + 24)) != 412) goto loc_00A8C027;
    if ((*(unsigned __int8 *)(result + 88)) != 0) goto loc_00A8C020;
    if ((*(unsigned int *)(result + 16)) == 0) goto loc_00A8C020;
    *(unsigned int *)(v_rip + 4044093) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 32)));
    *(unsigned int *)(v_rip + 4044090) = 1;
    goto loc_00A8C027;
loc_00A8C020:
    *(unsigned int *)(v_rip + 4044081) = 0;
loc_00A8C027:
    if (*(unsigned __int8 *)(result + 12) == 0) goto loc_00A8C050;
    result = ExAllocatePool2(256, 8, (unsigned int)(0x206D654DULL), a4);
    if (result == 0) goto loc_00A8BB03;
loc_00A8C050:
    result = PopSetWatchdog(*(unsigned __int64 *)(result + 8), result + 16, *(unsigned __int8 *)(result + 88), a4);
    a1 = 0;
    if (*(unsigned __int8 *)(result + 12) == 0) goto loc_00A8BB6A;
    *(unsigned __int64 *)(result) = result;
    *(unsigned __int64 *)(a7) = result;
loc_00A8C072:
    *(unsigned int *)(a8) = 8;
    goto loc_00A8BDED;
loc_00A8C07F:
    if (((unsigned int)((unsigned int)(0x400ULL))) < 12) goto loc_00A8BAD7;
    if (*(unsigned __int8 *)(result + 12) != 0) goto loc_00A8BB48;
    result = PpmAcquireLock(v_rip + 4721511, result + 16, *(unsigned __int8 *)(result + 88), a4);
    a2 = 0;
    if ((*(unsigned __int8 *)(result + 8)) == 0) goto loc_00A8C0CA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5483564)))) >= ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_00A8C0C0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 5483564))) + 1);
    *(unsigned int *)(v_rip + 5483538) = a1;
    goto loc_00A8C0C5;
loc_00A8C0C0:
loc_00A8C0C5:
    goto loc_00A8C0E6;
loc_00A8C0CA:
    if (a1 == 0) goto loc_00A8C0DF;
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned int)(0xFFFFFFFFULL))));
    *(unsigned int *)(v_rip + 5483507) = a1;
    goto loc_00A8C0E4;
loc_00A8C0DF:
loc_00A8C0E4:
loc_00A8C0E6:
    if (a1 != 0) goto loc_00A8C0F4;
    a1 = 0;
    result = PpmPerfUpdateDomainPolicy(a1, a2, *(unsigned __int8 *)(result + 88), a4);
    goto loc_00A8BA5D;
loc_00A8C0F4:
    result = PpmReleaseLock(v_rip + 4721413, a2, *(unsigned __int8 *)(result + 88), a4);
    goto loc_00A8BA5D;
loc_00A8C105:
    v_rbx = (unsigned int)(((unsigned int)(0xC00000BBULL)) - (27));
    if (condition_is_equal) goto loc_00A8C219;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8C1F0;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8C18D;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A8BB48;
    if (((unsigned int)((unsigned int)(0x400ULL))) < 8) goto loc_00A8BAD7;
    if (*(unsigned __int8 *)(result + 12) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 3, (unsigned int)(0x206D654DULL), a4);
    a2 = 0;
    if (result == 0) goto loc_00A8BB03;
    *(unsigned __int8 *)(result) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 5483017));
    *(unsigned __int8 *)(result + 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 5482865));
    result = ((*(unsigned int *)(v_rip + 5483572)) != 0) ? 1 : 0;
    *(unsigned __int8 *)(result + 2) = (unsigned __int8)(result);
    *(unsigned __int64 *)(a7) = result;
    *(unsigned int *)(a8) = 3;
loc_00A8C181:
    *(unsigned __int8 *)(a9) = 1;
    goto loc_00A8BA5D;
loc_00A8C18D:
    if (((unsigned int)((unsigned int)(0x400ULL))) < 8) goto loc_00A8BAD7;
    if (*(unsigned __int8 *)(result + 12) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 48, (unsigned int)(0x206D654DULL), a4);
    a1 = 0;
    if (result == 0) goto loc_00A8BB03;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(a7) = result;
    *(unsigned int *)(a8) = 48;
    goto loc_00A8BDED;
loc_00A8C1F0:
    if (((unsigned int)((unsigned int)(0x400ULL))) != 12) goto loc_00A8BB48;
    v_stack_mA0 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8)));
    result = PopSetPowerSettingValueAcDc(v_rip - 10987511, (unsigned int)(0x400ULL) - 8, v_stack_mA0, a4);
    goto loc_00A8BB68;
loc_00A8C219:
    if (((unsigned int)((unsigned int)(0x400ULL))) < 16) goto loc_00A8BAD7;
    if (*(unsigned __int8 *)(result + 12) != 0) goto loc_00A8BB48;
    result = PopTransitionCheckpoint((unsigned int)(*(unsigned int *)(result + 8)), (unsigned int)(*(unsigned int *)(result + 12)), v_stack_mA0, a4);
    goto loc_00A8BB68;
loc_00A8C23C:
    if (0 > 42) goto loc_00A8C53C;
    if (0 == 42) goto loc_00A8C4F3;
    if (0 > 37) goto loc_00A8C313;
    if (0 == 37) goto loc_00A8C2C5;
    a1 = (unsigned int)((0) - (32));
    if (condition_is_equal) goto loc_00A8C3F9;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8BA58;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8C3F9;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8C3F9;
    if (a1 != 1) goto loc_00A8BB48;
    if (((unsigned int)((unsigned int)(0x400ULL))) < 12) goto loc_00A8BAD7;
    if (*(unsigned __int8 *)(result + 12) != 0) goto loc_00A8BB48;
    result = PopAcquireRwLockExclusive(v_rip + 4702622, (unsigned int)(*(unsigned int *)(result + 12)), v_stack_mA0, a4);
    *(unsigned __int8 *)(v_rip + 4702556) = (unsigned __int8)(*(unsigned __int8 *)(result + 8));
    result = PopReleaseRwLock(v_rip + 4702610, (unsigned int)(*(unsigned int *)(result + 12)), v_stack_mA0, a4);
    a1 = 0;
    result = PopEsQueueStateEvaluation(a1, (unsigned int)(*(unsigned int *)(result + 12)), v_stack_mA0, a4);
    goto loc_00A8BB68;
loc_00A8C2C5:
    if (((unsigned int)((unsigned int)(0x400ULL))) < 8) goto loc_00A8BAD7;
    if (*(unsigned __int8 *)(result + 12) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 4, (unsigned int)(0x206D654DULL), a4);
    a2 = 0;
    if (result == 0) goto loc_00A8BB03;
loc_00A8C301:
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4717123)));
    *(unsigned __int64 *)(a7) = result;
    *(unsigned int *)(a8) = 4;
    goto loc_00A8C181;
loc_00A8C313:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(result + 8)))) - (38));
    if (condition_is_equal) goto loc_00A8C3F9;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8C3D9;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8C3A7;
    if (a1 != 1) goto loc_00A8BB48;
    if (((unsigned int)((unsigned int)(0x400ULL))) != 16) goto loc_00A8BB48;
    if (*(unsigned __int8 *)(result + 12) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 1, (unsigned int)(0x206D654DULL), a4);
    a2 = 0;
    if (result == 0) goto loc_00A8BB03;
    if (*(unsigned __int64 *)(result + 8) == 0) goto loc_00A8C393;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 312) + 40) == 0) goto loc_00A8C393;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 312) + 40) + 80) == 0) goto loc_00A8C393;
    result = 1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 312) + 40) + 80) + 64)) == 0) {
        result = 0;
    }
    *(unsigned __int8 *)(result) = (unsigned __int8)(result);
    *(unsigned __int64 *)(a7) = result;
    *(unsigned int *)(a8) = 1;
    goto loc_00A8C181;
loc_00A8C3A7:
    if (((unsigned int)((unsigned int)(0x400ULL))) != 16) goto loc_00A8BB48;
    if ((*(unsigned int *)(result + 8)) != 0) goto loc_00A8BB48;
    if ((*(unsigned __int8 *)(result + 12)) == 0) goto loc_00A8C3CF;
    result = PopDeepSleepSetDisengageReason((unsigned int)(0x400ULL) - 9, a2, (unsigned int)(0x206D654DULL), a4);
    goto loc_00A8BB68;
loc_00A8C3CF:
    result = PopDeepSleepClearDisengageReason((unsigned int)(0x400ULL) - 9, a2, (unsigned int)(0x206D654DULL), a4);
    goto loc_00A8BB68;
loc_00A8C3D9:
    if (((unsigned int)((unsigned int)(0x400ULL))) != 12) goto loc_00A8BB48;
    v_stack_mA8 = (unsigned __int8)(*(unsigned __int8 *)(result + 8));
    goto loc_00A8BB86;
loc_00A8C3F9:
    if (((unsigned int)((unsigned int)(0x400ULL))) != 24) goto loc_00A8BB48;
    if (*(unsigned __int8 *)(result + 12) == 0) goto loc_00A8C452;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 8))) == 0) goto loc_00A8BB48;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 8))))) << (2);
    if (a1 > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00A8C448;
    result = ExAllocatePool2(256, (unsigned int)(a1), (unsigned int)(0x206D654DULL), a4);
    a4 = 0;
    if (result != 0) goto loc_00A8C459;
    goto loc_00A8BB03;
loc_00A8C448:
    goto loc_00A8BA5D;
loc_00A8C452:
loc_00A8C459:
    if (((unsigned int)((unsigned int)(0xC0000095ULL))) != 31) goto loc_00A8C478;
    if ((*(unsigned int *)(result + 8)) != 0) goto loc_00A8C46B;
loc_00A8C464:
    goto loc_00A8C4E3;
loc_00A8C46B:
    result = PopBootStatGet(result, v_stack_m68, (unsigned int)(0x206D654DULL), a4);
    goto loc_00A8C4BB;
loc_00A8C478:
    if (((unsigned int)((unsigned int)(0xC000000DULL))) != 32) goto loc_00A8C490;
    if ((*(unsigned int *)(result + 8)) == 0) goto loc_00A8C464;
    result = PopBootStatSet(result, v_stack_m68, (unsigned int)(0x206D654DULL), a4);
    goto loc_00A8C4BB;
loc_00A8C490:
    if (((unsigned int)((unsigned int)(0xC000000DULL))) != 34) goto loc_00A8C4A5;
    if ((*(unsigned int *)(result + 8)) == 0) goto loc_00A8C464;
    result = PopBootStatCheckIntegrity(result, v_stack_m68, (unsigned int)(0x206D654DULL), a4);
    goto loc_00A8C4BB;
loc_00A8C4A5:
    if (((unsigned int)((unsigned int)(0xC000000DULL))) != 35) goto loc_00A8C4B1;
    result = PopBootStatRestoreDefaults(result, v_stack_m68, (unsigned int)(0x206D654DULL), a4);
    goto loc_00A8C4BB;
loc_00A8C4B1:
    if (((unsigned int)((unsigned int)(0xC000000DULL))) != 38) goto loc_00A8C4DE;
    result = PopBootStatUnlock(result, v_stack_m68, (unsigned int)(0x206D654DULL), a4);
loc_00A8C4BB:
    a4 = 0;
    if (sign_flag) goto loc_00A8C4E3;
    if (v_stack_m68 == 0) goto loc_00A8C7D8;
    *(unsigned __int64 *)(a7) = v_stack_m68;
    *(unsigned int *)(a8) = 0;
    *(unsigned __int8 *)(a9) = 1;
    goto loc_00A8C7D8;
loc_00A8C4DE:
loc_00A8C4E3:
    if (v_stack_m68 == 0) goto loc_00A8BA5D;
    a2 = 0;
    goto loc_00A8BC50;
loc_00A8C4F3:
    if (0 < 8) goto loc_00A8BAD7;
    if (v_stack_m68 == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 32, (unsigned int)(0x206D654DULL), a4);
    a1 = 0;
    if (result == 0) goto loc_00A8BB03;
    *(unsigned __int64 *)(result) = v_xmm0;
    goto loc_00A8BDDE;
loc_00A8C53C:
    if (((unsigned int)((unsigned int)(0xC00000BBULL))) > 48) goto loc_00A8C743;
    if (((unsigned int)((unsigned int)(0xC00000BBULL))) == 48) goto loc_00A8C716;
    v_rbx = (unsigned int)(((unsigned int)(0xC00000BBULL)) - (43));
    if (condition_is_equal) goto loc_00A8C6B5;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8C5F4;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8C5CF;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8C5A7;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A8BB48;
    if (0 < 20) goto loc_00A8BAD7;
    if (v_stack_m68 != 0) goto loc_00A8BB48;
    if ((*(unsigned int *)(result + 4)) == 0) goto loc_00A8C593;
loc_00A8C589:
    goto loc_00A8BA5D;
loc_00A8C593:
    result = PpmInternalProcessorIdleVeto((unsigned int)(*(unsigned int *)(result + 8)), (unsigned int)(*(unsigned int *)(result + 12)), *(unsigned __int8 *)(result + 16), a4);
    goto loc_00A8BBA0;
loc_00A8C5A7:
    if (0 != 32) goto loc_00A8BB48;
    if (v_stack_m68 != 0) goto loc_00A8BB48;
    result = PopPowerRequestNotifyUserSessionAttributed((unsigned int)(*(unsigned int *)(result + 24)), *(unsigned __int64 *)(result + 8), *(unsigned __int64 *)(result + 16), a4);
    goto loc_00A8BB68;
loc_00A8C5CF:
    v_rbx = 0;
loc_00A8C5D1:
    if (0 != 12) goto loc_00A8BB48;
    if ((*(unsigned __int8 *)(result + 8)) == 0) goto loc_00A8C5EA;
    result = PoUserShutdownInitiated((unsigned int)(*(unsigned int *)(result + 24)), *(unsigned __int64 *)(result + 8), *(unsigned __int64 *)(result + 16), a4);
    goto loc_00A8BA5D;
loc_00A8C5EA:
    result = PoUserShutdownCancelled((unsigned int)(*(unsigned int *)(result + 24)), *(unsigned __int64 *)(result + 8), *(unsigned __int64 *)(result + 16), a4);
    goto loc_00A8BA5D;
loc_00A8C5F4:
    if (0 < 144) goto loc_00A8BAD7;
    if (v_stack_m68 != 0) goto loc_00A8BB48;
    a1 = 0;
    result = RtlCheckTokenMembership(a1, *(unsigned __int64 *)(v_rip + 4721055), v_stack_mA8, a4);
    v_r14 = 0;
    if (sign_flag) goto loc_00A8BA5D;
    if (v_stack_mA8 == 0) goto loc_00A8B893;
    result = PopIsPlatformAoAcCapable(a1, *(unsigned __int64 *)(v_rip + 4721055), v_stack_mA8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A8BA58;
    result = RtlStringCbLengthW(result + 8, 128, v_stack_m90, a4);
    if (sign_flag) goto loc_00A8BA5D;
    if (v_stack_m90 != 0) goto loc_00A8C677;
    if (*(unsigned __int64 *)(result + 136) == 0) goto loc_00A8C680;
    goto loc_00A8BB48;
loc_00A8C677:
    if (*(unsigned __int64 *)(result + 136) == 0) goto loc_00A8BB48;
loc_00A8C680:
    result = PopAcquirePolicyLock(result + 8, 128, v_stack_m90, a4);
    *(unsigned __int16 *)(v_rip + 4727055) = 0;
    result = RtlStringCbCopyW(v_rip + 4727045, 128, result + 8, a4);
    *(unsigned __int64 *)(v_rip + 4727152) = *(unsigned __int64 *)(result + 136);
    goto loc_00A8BD17;
loc_00A8C6B5:
    if ((((unsigned int)(v_r14 - 8)) & (0xFFFFFFFBULL)) != 0) goto loc_00A8BB48;
    if (v_stack_m68 == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 8, (unsigned int)(0x206D654DULL), a4);
    result = 0;
    if (0 == 0) goto loc_00A8BB03;
    if (0 != 12) {
        a1 = 0;
    }
    result = PpmPerfGetBrandedFrequency(a1, 0, (unsigned int)(0x206D654DULL), a4);
loc_00A8C704:
loc_00A8C708:
    if (sign_flag) goto loc_00A8BC4B;
    *(unsigned __int64 *)(128) = result;
    goto loc_00A8BBF4;
loc_00A8C716:
    if (0 < 16) goto loc_00A8BAD7;
    if (result != 0) goto loc_00A8BB48;
    if ((*(unsigned int *)(result + 4)) != 0) goto loc_00A8C589;
    result = PpmInternalPlatformIdleVeto((unsigned int)(*(unsigned int *)(result + 8)), *(unsigned __int8 *)(result + 12), (unsigned int)(0x206D654DULL), a4);
    goto loc_00A8BBA0;
loc_00A8C743:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) - (49));
    if (condition_is_equal) goto loc_00A8C815;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8C7E0;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8C798;
    if (a1 != 2) goto loc_00A8BB48;
loc_00A8C769:
    v_stack_mC8 = 128;
    result = PopDirectedDripsUmPowerInformationInternal((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), 0, result, a8);
    result = 0;
    if (sign_flag) goto loc_00A8BA5D;
    if ((*(unsigned __int64 *)(128)) == 0) goto loc_00A8BA5D;
    goto loc_00A8BBFC;
loc_00A8C798:
    if (0 != 0) goto loc_00A8C7AF;
    if (0 < 16) goto loc_00A8BAD7;
    goto loc_00A8C7CA;
loc_00A8C7AF:
    if (0 != 1) goto loc_00A8BB48;
    if (0 < 24) goto loc_00A8BAD7;
loc_00A8C7CA:
    *(unsigned __int64 *)(v_rip + 4718807) = *(unsigned __int64 *)(result + 8);
    *(unsigned __int64 *)(v_rip + 4718792) = *(unsigned __int64 *)(result + 16);
loc_00A8C7D8:
    goto loc_00A8BA5D;
loc_00A8C7E0:
    if (0 == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 1, (unsigned int)(0x206D654DULL), a8);
    a2 = 0;
    if (result == 0) goto loc_00A8BB03;
    goto loc_00A8C395;
loc_00A8C815:
    if (result == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 1, (unsigned int)(0x206D654DULL), a8);
    v_rdi = 0;
    if (result == 0) goto loc_00A8BB03;
    result = PopQueryPowerButtonBugcheckEnabled(256, 1, (unsigned int)(0x206D654DULL), a8);
    goto loc_00A8BB24;
loc_00A8C849:
    if (((unsigned int)(result)) > 78) goto loc_00A8CD60;
    if (((unsigned int)(result)) == 78) goto loc_00A8CCF2;
    if (((unsigned int)(result)) > 67) goto loc_00A8CA58;
    if (((unsigned int)(result)) == 67) goto loc_00A8CA23;
    if (((unsigned int)(result)) > 61) goto loc_00A8C947;
    if (((unsigned int)(result)) == 61) goto loc_00A8B946;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) - (56));
    if (condition_is_equal) goto loc_00A8C769;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8C91C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8C901;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8C8E6;
    if (a1 != 1) goto loc_00A8BB48;
    if (result == 0) goto loc_00A8BAD7;
    result = PopAcquireTransitionLock(8, 1, (unsigned int)(0x206D654DULL), a8);
    result = PopReadResumeContext(v_stack_m98, v_stack_m88, (unsigned int)(0x206D654DULL), a8);
    result = PopReleaseTransitionLock(8, v_stack_m88, (unsigned int)(0x206D654DULL), a8);
    a1 = 0;
    if (sign_flag) goto loc_00A8BA5D;
    *(unsigned __int64 *)(128) = v_stack_m88;
    *(unsigned int *)(a8) = (unsigned int)((unsigned int)(v_stack_m98));
    goto loc_00A8BDED;
loc_00A8C8E6:
    if (0 < 24) goto loc_00A8BB48;
    result = PoDirectedDripsClearDeviceFlags(*(unsigned __int64 *)(v_rdi + 8), (unsigned int)(*(unsigned int *)(v_rdi + 16)), (unsigned int)(0x206D654DULL), a8);
    goto loc_00A8BBA0;
loc_00A8C901:
    if (0 < 24) goto loc_00A8BB48;
    result = PoDirectedDripsSetDeviceFlags(*(unsigned __int64 *)(v_rdi + 8), (unsigned int)(*(unsigned int *)(v_rdi + 16)), (unsigned int)(0x206D654DULL), a8);
    goto loc_00A8BBA0;
loc_00A8C91C:
    if (result != 0) goto loc_00A8BB48;
    result = PopPlRegisterPowerPlane(0, 0, (unsigned int)(0x206D654DULL), a8);
    goto loc_00A8BBA0;
loc_00A8C935:
    *(unsigned int *)(a8) = 0x1000ULL;
    *(unsigned __int8 *)(a9) = 1;
    goto loc_00A8BBA0;
loc_00A8C947:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) - (62));
    if (condition_is_equal) goto loc_00A8C9EE;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8C9A0;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8C769;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8C973;
    if (a1 != 1) goto loc_00A8BB48;
    goto loc_00A8BA58;
loc_00A8C973:
    if (0 != 16) goto loc_00A8BB48;
    if (*(unsigned __int64 *)(v_rdi + 8) == 0) goto loc_00A8BB48;
    result = PopFxClearDeviceConstraints(*(unsigned __int64 *)(v_rdi + 8), 0, (unsigned int)(0x206D654DULL), a8);
    result = 0;
    if (sign_flag) goto loc_00A8BA5D;
    goto loc_00A8BBA0;
loc_00A8C9A0:
    if (0 == 0) goto loc_00A8BB48;
    result = SSHSupportQueryIsLibraryEnabled(*(unsigned __int64 *)(v_rdi + 8), 0, (unsigned int)(0x206D654DULL), a8);
    result = (unsigned __int8)(-(result));
    v_rbx = ((unsigned int)((unsigned int)(result))) & (v_rip + 3625945);
    if (condition_is_equal) goto loc_00A8BA58;
    result = ExAllocatePool2(256, 8, (unsigned int)(0x206D654DULL), a8);
    a1 = 0;
    if (result == 0) goto loc_00A8BB03;
    *(unsigned __int64 *)(result) = v_rbx;
    *(unsigned __int64 *)(128) = result;
    goto loc_00A8C072;
loc_00A8C9EE:
    if (result == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 1, (unsigned int)(0x206D654DULL), a8);
    a2 = 0;
    if (result == 0) goto loc_00A8BB03;
    goto loc_00A8C395;
loc_00A8CA23:
    *(unsigned int *)(a8) = (unsigned int)(a8);
    *(unsigned __int64 *)(128) = a8;
    result = ExAllocatePool2(256, 4, (unsigned int)(0x206D654DULL), a8);
    a2 = 0;
    if (result == 0) goto loc_00A8BB03;
    goto loc_00A8C301;
loc_00A8CA58:
    if (((unsigned int)(v_rbx)) > 73) goto loc_00A8CC27;
    if (((unsigned int)(v_rbx)) == 73) goto loc_00A8CC07;
    v_rbx = (unsigned int)((v_rbx) - (68));
    if (condition_is_equal) goto loc_00A8CBEF;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8CBA3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8CB14;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8CAD5;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A8BB48;
    if (result == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(0x900ULL))), (unsigned int)(0x206D654DULL), a8);
    if (result == 0) goto loc_00A8BB03;
    result = PpmPerfGetFrequencyBandStats(result, (unsigned int)((unsigned int)((unsigned int)(0x900ULL))), (unsigned int)(0x206D654DULL), a8);
loc_00A8CAC6:
    if (!sign_flag) goto loc_00A8BD6E;
    goto loc_00A8BBDF;
loc_00A8CAD5:
    if (((unsigned int)((unsigned int)(0x900ULL))) != 12) goto loc_00A8BB48;
    result = PopAcquireRwLockExclusive(v_rip + 4700695, (unsigned int)((unsigned int)((unsigned int)(0x900ULL))), (unsigned int)(0x206D654DULL), a8);
    if ((*(unsigned __int8 *)(v_rip + 5480457)) != ((unsigned __int8)(*(unsigned __int8 *)(result + 8)))) {
        a1 = (unsigned __int8)(*(unsigned __int8 *)(result + 8));
        *(unsigned __int8 *)(v_rip + 5480447) = (unsigned __int8)(*(unsigned __int8 *)(result + 8));
        result = PopDiagTraceSleepReliabilityDiagConfigUpdate(a1, (unsigned int)((unsigned int)((unsigned int)(0x900ULL))), (unsigned int)(0x206D654DULL), a8);
    }
    result = PopReleaseRwLock(v_rip + 4700662, (unsigned int)((unsigned int)((unsigned int)(0x900ULL))), (unsigned int)(0x206D654DULL), a8);
    goto loc_00A8BB68;
loc_00A8CB14:
    if (((unsigned int)((unsigned int)(0x900ULL))) < 12) goto loc_00A8BAD7;
    if ((*(unsigned int *)(result + 4)) > 2) goto loc_00A8BA58;
    if ((*(unsigned int *)(result + 4)) != 2) goto loc_00A8CB38;
    if (((unsigned int)((unsigned int)(0x900ULL))) < 32) goto loc_00A8BAD7;
loc_00A8CB38:
    if (result == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(256, 8, (unsigned int)(0x206D654DULL), a8);
    if (result == 0) goto loc_00A8BB03;
    if ((*(unsigned int *)(result + 4)) != 2) goto loc_00A8CB8F;
    v_stack_mB8 = result;
    v_stack_mC0 = (unsigned __int8)(*(unsigned __int8 *)(result + 28));
    v_stack_mC8 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 24)));
    result = PpmPerfGetVmCppcConfig((unsigned int)(*(unsigned int *)(result + 12)), (unsigned int)(*(unsigned int *)(result + 8)), (unsigned int)(*(unsigned int *)(result + 16)), (unsigned int)(*(unsigned int *)(result + 20)));
    goto loc_00A8CB9A;
loc_00A8CB8F:
    result = PpmPerfGetVmPerfConfig((unsigned int)(*(unsigned int *)(result + 8)), result, (unsigned int)(*(unsigned int *)(result + 16)), (unsigned int)(*(unsigned int *)(result + 20)));
loc_00A8CB9A:
    goto loc_00A8C708;
loc_00A8CBA3:
    if (result == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(256, 20, (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(result + 20)));
    v_rdi = 0;
    if (result == 0) goto loc_00A8BB03;
    result = PpmPerfGetVmPerfControlSupport(result, 20, (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(result + 20)));
    *(unsigned __int64 *)(128) = result;
    result = (unsigned int)((result) & (0xFFFFFFEDULL));
    result = (unsigned int)((result) + (20));
    *(unsigned int *)(a8) = (unsigned int)(result);
    goto loc_00A8BB31;
loc_00A8CBEF:
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rip + 3664227))));
    a1 = (unsigned int)(~(result));
    v_rbx = (unsigned int)(((unsigned int)(0xC00000BBULL)) & (a1));
    goto loc_00A8BA5D;
loc_00A8CC07:
    if (((unsigned int)((unsigned int)(0x900ULL))) < 12) goto loc_00A8BAD7;
    if (result != 0) goto loc_00A8BB48;
    result = PopUserPresenceHostStateChange((unsigned int)(*(unsigned int *)(v_rdi + 8)), 20, (unsigned int)(0x206D654DULL), (unsigned int)(*(unsigned int *)(result + 20)));
    goto loc_00A8BB68;
loc_00A8CC27:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (74));
    if (condition_is_equal) goto loc_00A8CC84;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8CC84;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8CC41;
    if (a1 != 1) goto loc_00A8BB48;
loc_00A8CC41:
    if (((unsigned int)((unsigned int)(0x900ULL))) != 12) goto loc_00A8BAD7;
    if (result == 0) goto loc_00A8BB48;
    result = PpmIdleGetConcurrencyStats((unsigned int)((unsigned int)(v_rbx)), *(unsigned __int16 *)(v_rdi + 8), v_stack_m80, v_stack_m94);
    if (sign_flag) goto loc_00A8BA5D;
    *(unsigned __int64 *)(128) = v_stack_m80;
    *(unsigned int *)(a8) = (unsigned int)((unsigned int)(v_stack_m94));
    goto loc_00A8BBFC;
loc_00A8CC84:
    if (((unsigned int)((unsigned int)(0x900ULL))) != 12) goto loc_00A8BAD7;
    if (result == 0) goto loc_00A8BB48;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 74) goto loc_00A8CCA4;
    goto loc_00A8CCB3;
loc_00A8CCA4:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 75) goto loc_00A8BB48;
loc_00A8CCB3:
    result = ExAllocatePool2(256, 592, (unsigned int)(0x206D654DULL), v_stack_m94);
    if (result == 0) goto loc_00A8BB03;
    result = PpmIdleGetPackageIdleIntervalStats((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int16 *)(v_rdi + 8), result, v_stack_m94);
    if (sign_flag) goto loc_00A8BC4B;
    *(unsigned __int64 *)(128) = result;
    goto loc_00A8BD71;
loc_00A8CCF2:
    if (result == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(256, 4, (unsigned int)(0x206D654DULL), v_stack_m94);
    v_rdi = 0;
    if (result == 0) goto loc_00A8BB03;
loc_00A8CD25:
    if ((*(unsigned __int64 *)(v_rip + 5480067)) == (v_rip + 5480060)) goto loc_00A8CD4C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5480067) + 424) != 0) goto loc_00A8CD42;
    goto loc_00A8CD25;
loc_00A8CD42:
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5480067) + 424), 4, (unsigned int)(0x206D654DULL), v_stack_m94);
    goto loc_00A8CD4E;
loc_00A8CD4C:
loc_00A8CD4E:
    *(unsigned int *)(result) = 0;
    *(unsigned __int64 *)(128) = result;
    *(unsigned int *)(a8) = 4;
    goto loc_00A8BB31;
loc_00A8CD60:
    if (((unsigned int)(result)) > 89) goto loc_00A8D145;
    if (((unsigned int)(result)) == 89) goto loc_00A8D0CF;
    if (((unsigned int)(result)) > 84) goto loc_00A8CFEC;
    if (((unsigned int)(result)) == 84) goto loc_00A8CFAB;
    v_rbx = (unsigned int)((result) - (79));
    if (condition_is_equal) goto loc_00A8CED6;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8CE98;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8CE4D;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8CDDA;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A8BB48;
    if (592 != 16) goto loc_00A8BB48;
    if (0 == 0) goto loc_00A8BB48;
    if (a6 != ((unsigned int)(v_stack_m94))) goto loc_00A8BB48;
    if (result != 0) goto loc_00A8BB48;
    result = PopAdaptiveSetSystemInitiatedRebootTargetStateOverride(0, 4, (unsigned int)(0x206D654DULL), v_stack_m94);
    goto loc_00A8BBA0;
loc_00A8CDDA:
    if (592 != 12) goto loc_00A8BB48;
    if (0 == 0) goto loc_00A8BB48;
    if (a6 != ((unsigned int)(v_stack_m94))) goto loc_00A8BB48;
    if (result != 0) goto loc_00A8BB48;
    v_stack_mA0 = v_stack_m94;
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), 4, (unsigned int)(0x206D654DULL), v_stack_m94);
    v_stack_mA0 = (unsigned int)(result);
    v_stack_m9C = 1;
    v_stack_m9B = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 8));
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), 4, (unsigned int)(0x206D654DULL), v_stack_m94);
    result = PopSessionWinlogonNotification((unsigned int)((unsigned int)(result)), v_stack_mA0, (unsigned int)(0x206D654DULL), v_stack_m94);
loc_00A8CE46:
    result = 0;
    goto loc_00A8BBA0;
loc_00A8CE4D:
    if (592 != 40) goto loc_00A8BB48;
    if (0 == 0) goto loc_00A8BB48;
    if (a6 != 16) goto loc_00A8BB48;
    if (0 == 0) goto loc_00A8BB48;
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_stack_mA0, (unsigned int)(0x206D654DULL), v_stack_m94);
    result = PopAdaptiveGetSessionState((unsigned int)((unsigned int)(result)), v_rdi + 8, result, v_stack_m94);
    goto loc_00A8CE46;
loc_00A8CE98:
    if (592 != 8) goto loc_00A8BB48;
    if (0 == 0) goto loc_00A8BB48;
    if (a6 != ((unsigned int)(v_stack_m94))) goto loc_00A8BB48;
    if (result != 0) goto loc_00A8BB48;
    result = PopAdaptiveGetSystemInitiatedRebootTargetState((unsigned int)((unsigned int)(result)), v_rdi + 8, result, v_stack_m94);
    *(unsigned __int64 *)(v_rip + 5550918) = result;
    *(unsigned __int8 *)(v_rip + 5550903) = 1;
    goto loc_00A8CE46;
loc_00A8CED6:
    if (0 == 0) goto loc_00A8BB48;
    if (592 != 12) goto loc_00A8BB48;
    v_stack_mA4 = (unsigned int)(v_stack_m94);
    a4 = 0;
    a3 = 0;
    result = PpmPerfQueryProcMeasurementValues((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8)))), v_stack_mA4, a3, a4);
    if (sign_flag) goto loc_00A8BA5D;
    if (a6 != 4) goto loc_00A8CF53;
    result = ExAllocatePool2(256, 592 - 8, (unsigned int)(0x206D654DULL), a4);
    if (result == 0) goto loc_00A8BB03;
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(v_stack_mA4));
    *(unsigned __int64 *)(128) = result;
    *(unsigned int *)(a8) = 4;
    goto loc_00A8BBFC;
loc_00A8CF53:
    if (a6 < ((unsigned int)((unsigned int)(v_stack_mA4) + (unsigned int)(v_stack_mA4) * 2 * 8 + 8))) goto loc_00A8BAD7;
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)((unsigned int)(v_stack_mA4) + (unsigned int)(v_stack_mA4) * 2 * 8 + 8)), (unsigned int)(0x206D654DULL), a4);
    if (result == 0) goto loc_00A8BB03;
    *(unsigned int *)(a8) = (unsigned int)((unsigned int)(v_stack_mA4) + (unsigned int)(v_stack_mA4) * 2 * 8 + 8);
    *(unsigned __int8 *)(a9) = 1;
    *(unsigned __int64 *)(128) = result;
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(v_stack_mA4));
    a3 = (result) + (8);
    a4 = (unsigned int)(((unsigned int)(v_stack_mA4) + (unsigned int)(v_stack_mA4) * 2) << (3));
    result = PpmPerfQueryProcMeasurementValues((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8)))), v_stack_mA4, a3, a4);
    goto loc_00A8BBA0;
loc_00A8CFAB:
    if ((unsigned int)(*(unsigned int *)(v_rdi + 8)) == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(160 + 96, 160, (unsigned int)(0x206D654DULL), a4);
    if (result == 0) goto loc_00A8BB03;
loc_00A8CFDC:
    result = PopFanReadFanNoiseInfo(160 - 76, result, 160, a4);
    goto loc_00A8CAC6;
loc_00A8CFEC:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) - (85));
    if (condition_is_equal) goto loc_00A8D098;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8D041;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8D018;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A8BB48;
    result = PopManageTransitionRecordRequest(160 - 76, result, 160, a4);
    goto loc_00A8BBA0;
loc_00A8D018:
    if (result == 0) goto loc_00A8BB48;
    if (160 != 24) goto loc_00A8BB48;
    if ((unsigned int)(*(unsigned int *)(v_rdi + 8)) != 0) goto loc_00A8BB48;
    result = PopShutdownListenerRemoveCallback(result, result, 160, a4);
    goto loc_00A8BBA0;
loc_00A8D041:
    if (160 < 8) goto loc_00A8BAD7;
    if ((unsigned int)(*(unsigned int *)(v_rdi + 8)) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 8, (unsigned int)(0x206D654DULL), a4);
    a2 = 0;
    if (result == 0) goto loc_00A8BB03;
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4044015)));
    *(unsigned int *)(result + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4044003)));
    *(unsigned __int64 *)(128) = result;
    *(unsigned int *)(a8) = 8;
    goto loc_00A8C181;
loc_00A8D098:
    if ((unsigned int)(*(unsigned int *)(v_rdi + 8)) == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(256, 88, (unsigned int)(0x206D654DULL), a4);
    if (result == 0) goto loc_00A8BB03;
    goto loc_00A8CFDC;
loc_00A8D0CF:
    if ((unsigned int)(*(unsigned int *)(v_rdi + 8)) == 0) goto loc_00A8BAD7;
    if (a6 != 20) goto loc_00A8BAD7;
    result = PopAcquirePolicyLock(88 - 3, 88, (unsigned int)(0x206D654DULL), a4);
    v_rbx = 0;
    if ((*(unsigned __int8 *)(v_rip + 4718052)) == 0) goto loc_00A8D13B;
    result = ExAllocatePool2(256, v_rbx + 20, (unsigned int)(0x206D654DULL), a4);
    if (result == 0) goto loc_00A8D131;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4702167)));
    *(unsigned __int64 *)(128) = result;
    *(unsigned int *)(a8) = 20;
    *(unsigned __int8 *)(a9) = 1;
    goto loc_00A8BD17;
loc_00A8D131:
    goto loc_00A8BD17;
loc_00A8D13B:
    goto loc_00A8BD17;
loc_00A8D145:
    if (((unsigned int)((unsigned int)(0xC00000BBULL))) > 95) goto loc_00A8D2BA;
    if (((unsigned int)((unsigned int)(0xC00000BBULL))) == 95) goto loc_00A8D40F;
    v_rbx = (unsigned int)(((unsigned int)(0xC00000BBULL)) - (90));
    if (condition_is_equal) goto loc_00A8D28B;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8D22C;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8D20B;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A8D1BF;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A8BB48;
    if (88 < 12) goto loc_00A8BAD7;
    if ((unsigned int)(*(unsigned int *)(v_rdi + 8)) == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(256, v_rbx + 7, (unsigned int)(0x206D654DULL), a4);
    if (result == 0) goto loc_00A8BB03;
    result = PpmPerfGetVmPerfPriorityConfig((unsigned int)(*(unsigned int *)(result + 8)), result, (unsigned int)(0x206D654DULL), a4);
    goto loc_00A8C704;
loc_00A8D1BF:
    if ((unsigned int)(result) != 0) goto loc_00A8BA58;
    if (result == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(256, 8, (unsigned int)(0x206D654DULL), a4);
    v_rdi = 0;
    if (result == 0) goto loc_00A8BB03;
    result = PpmPerfGetVmPerfPrioritySupport(result, 8, (unsigned int)(0x206D654DULL), a4);
    *(unsigned __int64 *)(128) = result;
    *(unsigned int *)(a8) = 8;
    goto loc_00A8BB31;
loc_00A8D20B:
    v_stack_mC0 = a8;
    v_stack_mC8 = 128;
    result = PopHandleProvIdentifierRequest(0, 88, result, (unsigned int)(a6));
    goto loc_00A8BBA0;
loc_00A8D22C:
    if (result == 0) goto loc_00A8BAD7;
    if (a6 < 36) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 36, (unsigned int)(0x206D654DULL), (unsigned int)(a6));
    v_rsi = 0;
    if (result == 0) goto loc_00A8BB03;
    result = PopGetEnergyEstimationInfo(result, 36, (unsigned int)(0x206D654DULL), (unsigned int)(a6));
    if (sign_flag) goto loc_00A8BBDF;
    *(unsigned __int64 *)(128) = result;
    *(unsigned int *)(a8) = 36;
    *(unsigned __int8 *)(a9) = 1;
    goto loc_00A8BA5D;
loc_00A8D28B:
    if (result == 0) goto loc_00A8BB48;
    if (36 < 20) goto loc_00A8BB48;
    if (0 == 0) goto loc_00A8D2AD;
    if (a6 != ((unsigned int)((unsigned int)(a6)))) goto loc_00A8BB48;
loc_00A8D2AD:
    result = PopSuspendResumeInvocation(result, 36, (unsigned int)(0x206D654DULL), (unsigned int)(a6));
    goto loc_00A8BBA0;
loc_00A8D2BA:
    a1 = (unsigned int)((0) - (96));
    if (condition_is_equal) goto loc_00A8D40F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8D3CB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A8D312;
    if (a1 != 1) goto loc_00A8BB48;
    result = Feature_Servicing_BatteryTestExempt__private_IsEnabledDeviceUsageNoInline(a1, 36, (unsigned int)(0x206D654DULL), (unsigned int)(a6));
    if ((unsigned int)(result) == 0) goto loc_00A8BB48;
    if (result == 0) goto loc_00A8BB48;
    if (0 != 0) goto loc_00A8BB48;
    if (36 < 12) goto loc_00A8BAD7;
    result = PopBatteryUpdateTestExempt(*(unsigned __int8 *)(result + 8), 36, (unsigned int)(0x206D654DULL), (unsigned int)(a6));
    goto loc_00A8BBA0;
loc_00A8D312:
    result = Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline(*(unsigned __int8 *)(result + 8), 36, (unsigned int)(0x206D654DULL), (unsigned int)(a6));
    v_r15 = 0;
    if ((unsigned int)(result) == 0) goto loc_00A8BB48;
    v_stack_mA8 = 0;
    a1 = 0;
    result = SeIsAppContainerOrIdentifyLevelContext(a1, v_stack_mA8, (unsigned int)(0x206D654DULL), (unsigned int)(a6));
    if (sign_flag) goto loc_00A8BA5D;
    if (v_stack_mA8 != 0) goto loc_00A8B893;
    if (v_stack_mA0 != 0) goto loc_00A8BB48;
    if (36 != 48) goto loc_00A8D3C1;
    if (0 == 0) goto loc_00A8D3C1;
    if (a6 != 16) goto loc_00A8D3C1;
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_stack_mA8, (unsigned int)(0x206D654DULL), (unsigned int)(a6));
    result = PopSessionConnectionChangeV2((unsigned int)((unsigned int)(result)), result + 8, result + 16, 0);
    result = PsGetProcessSessionIdEx(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), result + 8, result + 16, 0);
    result = *(unsigned __int64 *)(v_rip + 4039667);
    if (*(unsigned __int64 *)(v_rip + 4039667) != 0) {
        a4 = *(unsigned int *)(result + 12);
        a2 = 0;
        a3 = *(unsigned __int8 *)(result + 8);
        result = guard_dispatch_icall((unsigned int)((unsigned int)(result)), a2, a3, a4);
    }
    goto loc_00A8BA5D;
loc_00A8D3C1:
    goto loc_00A8BA5D;
loc_00A8D3CB:
    if (36 != 12) goto loc_00A8BB48;
    if (0 == 0) goto loc_00A8BB48;
    if (a6 != 1) goto loc_00A8BB48;
    *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(a4);
    result = Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline((unsigned int)((unsigned int)(result)), a2, a3, a4);
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00A8BB6A;
    if ((*(unsigned int *)(result + 8)) != 0x3937A27ULL) goto loc_00A8BB6A;
    *(unsigned __int8 *)(v_rsi) = 1;
    goto loc_00A8BB6A;
loc_00A8D40F:
    if (36 != 12) goto loc_00A8BB48;
    if (0 != 0) goto loc_00A8BB48;
    if ((*(unsigned int *)(result + 4)) != a4) goto loc_00A8BB48;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 8)))) >= 32) goto loc_00A8BB48;
    a2 = (((unsigned int)((unsigned int)(0xC0000206ULL))) == 95) ? 1 : 0;
    result = PopNotifyWin32kRequestStatus((unsigned int)(*(unsigned int *)(result + 8)), a2, a3, a4);
    goto loc_00A8BBA0;
loc_00A8D448:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (176);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopPowerInformationInternal(void *Arg1, int32_t Arg2, void *Arg3, void *Arg4, int64_t Arg5, uint32_t Arg6, void *Arg7, void *Arg8, void *Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg9 = (uint8_t *)Arg9;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m3F;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint32_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint16_t v_stack_m76;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint8_t v_stack_m9B;
    uint8_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA4;
    uint8_t v_stack_mA6;
    uint8_t v_stack_mA7;
    uint8_t v_stack_mA8;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x37EF5D)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m78 = v_xmm0;
    Arg4 = 0;
    *(uint64_t *)(arg7) = 0;
    *(uint32_t *)(arg8) = 0;
    *(uint8_t *)(arg9) = 0;
    v_stack_mA0 = Arg2;
    v_stack_mA7 = 0;
    v_stack_mA8 = 0;
    v_stack_m90 = 0;
    v_stack_m98 = 0;
    v_stack_m88 = 0;
    v_stack_m80 = 0;
    v_stack_m94 = 0;
    v_stack_m68 = 0;
    v_stack_mA6 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00A8BA36;
    if (((uint32_t)((uint32_t)(Arg1))) > 28) goto loc_00A8B86A;
    if (((uint32_t)((uint32_t)(Arg1))) < 28) goto loc_00A8B893;
loc_00A8B86A:
    if (((uint32_t)((uint32_t)(Arg1) - 40)) > 56) goto loc_00A8B882;
    if (((uint32_t)((uint32_t)(Arg1) - 40)) < 56) goto loc_00A8B893;
loc_00A8B882:
    result = Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), Arg2, Arg3, Arg4);
    Arg4 = 0;
    if ((uint32_t)(result) == 0) goto loc_00A8B89D;
    if (((uint32_t)((uint32_t)(Arg1))) != 98) goto loc_00A8B89D;
loc_00A8B893:
    goto loc_00A8BA5D;
loc_00A8B89D:
    if (((uint32_t)((uint32_t)(0xC0000022ULL) - 29)) > 35) goto loc_00A8B8C1;
    if (((uint32_t)((uint32_t)(0xC0000022ULL) - 29)) >= 35) goto loc_00A8B8C1;
    result = EtwpCoverageUserIsAdmin(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), Arg2, Arg3, Arg4);
    Arg4 = 0;
    if ((uint8_t)(result) == 0) goto loc_00A8B893;
loc_00A8B8C1:
    if (((uint32_t)((uint32_t)(0xC0000022ULL) - 82)) > 1) goto loc_00A8B8D5;
    result = PopCheckTestsigningEnabled(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), Arg2, Arg3, Arg4);
    Arg4 = 0;
    if ((uint8_t)(result) == 0) goto loc_00A8B893;
loc_00A8B8D5:
    if (((uint32_t)((uint32_t)(0xC0000022ULL))) == 24) goto loc_00A8B8F2;
    if (((uint32_t)((uint32_t)(0xC0000022ULL) - 35)) > 55) goto loc_00A8B8FE;
    if (((uint32_t)((uint32_t)(0xC0000022ULL) - 35)) >= 55) goto loc_00A8B8FE;
loc_00A8B8F2:
    result = PopIsRunningAsLocalSystem(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), Arg2, Arg3, Arg4);
    Arg4 = 0;
    if ((uint8_t)(result) == 0) goto loc_00A8B893;
loc_00A8B8FE:
    if (((uint32_t)((uint32_t)(0xC0000022ULL))) != 80) goto loc_00A8B927;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x54E223), v_stack_mA6, Arg3, Arg4);
    Arg4 = 0;
    if ((uint8_t)(result) != 0) goto loc_00A8CE98;
    goto loc_00A8BA5D;
loc_00A8B927:
    if (((uint32_t)((uint32_t)(0xC0000061ULL))) != 61) goto loc_00A8B991;
    result = PopCheckTestsigningEnabled(*(uint64_t *)(v_rip + 0x54E223), v_stack_mA6, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A8B893;
    result = EtwpCoverageUserIsAdmin(*(uint64_t *)(v_rip + 0x54E223), v_stack_mA6, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A8B893;
loc_00A8B946:
    if (((uint32_t)((uint32_t)(Arg4))) < 12) goto loc_00A8BB48;
    if (Arg5 == 0) goto loc_00A8BAD7;
    result = PopAcquireTransitionLock(8, v_stack_mA6, Arg3, Arg4);
    result = PopReadPagesFromHiberFile((uint32_t)(*(uint32_t *)(arg3 + 0x8)), 1, Arg7, Arg4);
    result = PopReleaseTransitionLock(8, 1, Arg7, Arg4);
    result = 0;
    if (!sign_flag) goto loc_00A8C935;
    *(uint64_t *)(arg7) = 0;
    goto loc_00A8BA5D;
loc_00A8B991:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 45) goto loc_00A8B9C4;
    result = PopIsRunningAsLocalSystem(8, 1, Arg7, Arg4);
    local_rbx = 0;
    if ((uint8_t)(result) != 0) goto loc_00A8C5D1;
    result = PopCheckTestsigningEnabled(8, 1, Arg7, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A8B893;
    result = EtwpCoverageUserIsAdmin(8, 1, Arg7, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00A8C5D1;
    goto loc_00A8B893;
loc_00A8B9C4:
    if (0 != 25) goto loc_00A8BA65;
    v_stack_m78 = v_xmm0;
loc_00A8B9E9:
    if ((*(uint16_t *)(v_rip + 0x762D9)) == 0) goto loc_00A8B9FA;
    Arg1 = (v_rip + 484057) + (local_rbx - 23);
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(0x7FFFULL)))) - (1);
    if (condition_is_not_equal) goto loc_00A8B9E9;
    goto loc_00A8BA0F;
loc_00A8B9FA:
    result = ((uint32_t)(0x7FFFULL)) - (Arg3);
    v_stack_m70 = v_rip + 484057;
    result = (uint16_t)((result) + ((uint16_t)(result)));
    v_stack_m78 = (uint16_t)(result);
    result = (uint16_t)((result) + ((uint16_t)(local_rbx - 23)));
    v_stack_m76 = (uint16_t)(result);
loc_00A8BA0F:
    Arg1 = 0;
    result = RtlCapabilityCheckForSingleSessionSku(Arg1, v_stack_m78, v_stack_mA7, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_00A8BA5D;
    if (v_stack_mA7 != 0) goto loc_00A8BE76;
    goto loc_00A8B893;
loc_00A8BA36:
    if (((uint32_t)((uint32_t)((uint32_t)(result)) - 24)) > 59) goto loc_00A8BA4E;
    if (((uint32_t)((uint32_t)((uint32_t)(result)) - 24)) < 59) goto loc_00A8BA58;
loc_00A8BA4E:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 5) goto loc_00A8BA58;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 7) goto loc_00A8BA71;
loc_00A8BA58:
loc_00A8BA5D:
    goto loc_00A8D448;
loc_00A8BA65:
loc_00A8BA71:
    if (((uint32_t)((uint32_t)(0xC00000BBULL))) > 54) goto loc_00A8C849;
    if (((uint32_t)((uint32_t)(0xC00000BBULL))) == 54) goto loc_00A8C769;
    if (((uint32_t)((uint32_t)(0xC00000BBULL))) > 31) goto loc_00A8C23C;
    if (((uint32_t)((uint32_t)(0xC00000BBULL))) == 31) goto loc_00A8C3F9;
    if (((uint32_t)((uint32_t)(0xC00000BBULL))) > 20) goto loc_00A8BE3E;
    if (((uint32_t)((uint32_t)(0xC00000BBULL))) == 20) goto loc_00A8BE17;
    if (((uint32_t)((uint32_t)(0xC00000BBULL))) > 5) goto loc_00A8BC82;
    if (((uint32_t)((uint32_t)(0xC00000BBULL))) == 5) goto loc_00A8BC62;
    if ((uint32_t)((uint32_t)(0xC00000BBULL)) == 0) goto loc_00A8BC06;
    local_rbx = (uint32_t)(((uint32_t)(0xC00000BBULL)) - (1));
    if (condition_is_equal) goto loc_00A8BBA7;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8BB71;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8BB3D;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A8BB48;
    if (((uint32_t)((uint32_t)(Arg4))) >= 8) goto loc_00A8BAE1;
loc_00A8BAD7:
    goto loc_00A8BA5D;
loc_00A8BAE1:
    if (Arg5 == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 1, (uint32_t)(0x206D654DULL), Arg4);
    local_rdi = 0;
    if (result != 0) goto loc_00A8BB0D;
loc_00A8BB03:
    goto loc_00A8BA5D;
loc_00A8BB0D:
    result = PopIsPlatformAoAcCapable(256, 1, (uint32_t)(0x206D654DULL), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A8BB21;
    result = RtlIsMultiSessionSku(256, 1, (uint32_t)(0x206D654DULL), Arg4);
    result = 1;
    if ((uint8_t)(result) == 0) {
        result = 0;
    }
    *(uint8_t *)((uint32_t)(0xC000009AULL)) = (uint8_t)(result);
    *(uint64_t *)(arg7) = (uint32_t)(0xC000009AULL);
    *(uint32_t *)(arg8) = 1;
loc_00A8BB31:
    *(uint8_t *)(arg9) = 1;
    goto loc_00A8BA5D;
loc_00A8BB3D:
    if (((uint32_t)((uint32_t)(Arg4))) < 16) goto loc_00A8BAD7;
    if (Arg5 == 0) goto loc_00A8BB52;
loc_00A8BB48:
    goto loc_00A8BA5D;
loc_00A8BB52:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4813B4))))) == 0) goto loc_00A8BB48;
    Arg2 = 0;
    result = PopUpdateSmartUserPresencePredictions(*(uint64_t *)(local_rdi + 0x8), Arg2, (uint32_t)(0x206D654DULL), Arg4);
loc_00A8BB68:
    Arg1 = 0;
loc_00A8BB6A:
    goto loc_00A8BA5D;
loc_00A8BB71:
    *(uint8_t *)(v_rip + 0x482F41) = 1;
loc_00A8BB86:
    v_stack_mB8 = 0;
    v_stack_mC0 = 0;
    v_stack_mC8 = 0;
    Arg4 = 0;
    result = ZwUpdateWnfStateData(v_rip - 10924574, v_rip + 4730682, 1, Arg4);
loc_00A8BBA0:
    goto loc_00A8BA5D;
loc_00A8BBA7:
    if (Arg5 == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 8, (uint32_t)(0x206D654DULL), Arg4);
    if (result == 0) goto loc_00A8BB03;
    result = PopS0LowPowerIdleInfo(result, 8, (uint32_t)(0x206D654DULL), Arg4);
    if (!sign_flag) goto loc_00A8BBF1;
loc_00A8BBDF:
loc_00A8BBE7:
    result = ExFreePoolWithTag(result, (uint32_t)(0x206D654DULL), (uint32_t)(0x206D654DULL), Arg4);
    goto loc_00A8BA5D;
loc_00A8BBF1:
    *(uint64_t *)(arg7) = result;
loc_00A8BBF4:
    *(uint32_t *)(arg8) = 8;
loc_00A8BBFC:
    *(uint8_t *)(arg9) = 1;
    goto loc_00A8BA5D;
loc_00A8BC06:
    if (((uint32_t)((uint32_t)(Arg4))) < 32) goto loc_00A8BAD7;
    if (Arg5 == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 16, (uint32_t)(0x206D654DULL), Arg4);
    if (result == 0) goto loc_00A8BB03;
    result = PopFxPlatformRegisterInterface(result, result, (uint32_t)(0x206D654DULL), Arg4);
    if (!sign_flag) goto loc_00A8BC55;
loc_00A8BC4B:
loc_00A8BC50:
    goto loc_00A8BBE7;
loc_00A8BC55:
    *(uint64_t *)(arg7) = result;
    *(uint32_t *)(arg8) = 16;
    goto loc_00A8BBFC;
loc_00A8BC62:
    if (((uint32_t)((uint32_t)(Arg4))) < 12) goto loc_00A8BAD7;
    if (result != 0) goto loc_00A8BB48;
    result = PoLatencySensitivityHint((uint32_t)(*(uint32_t *)(result + 0x8)), (uint32_t)(0x206D654DULL), (uint32_t)(0x206D654DULL), Arg4);
    goto loc_00A8BB68;
loc_00A8BC82:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) - (6));
    if (condition_is_equal) goto loc_00A8BDF7;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8BD9A;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8BD7A;
    local_rbx = (uint32_t)((local_rbx) - (10));
    if (condition_is_equal) goto loc_00A8BD21;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A8BB48;
    if (((uint32_t)((uint32_t)(Arg4))) != 20) goto loc_00A8BB48;
    if (result != 0) goto loc_00A8BB48;
    result = TtmNotifySessionPowerStateChange((uint32_t)(*(uint32_t *)(result + 0x8)), *(uint8_t *)(result + 0xC), (uint32_t)(0x206D654DULL), Arg4);
    local_r14 = 0;
    local_rbx = ((uint8_t)(*(uint8_t *)(result + 0xC)) != 0) ? 1 : 0;
    result = PopAcquirePolicyLock((uint32_t)(*(uint32_t *)(result + 0x8)), *(uint8_t *)(result + 0xC), (uint32_t)(0x206D654DULL), Arg4);
    if ((*(uint8_t *)(result + 0xD)) == 0) goto loc_00A8BCFC;
    result = PopSetDisplayStatus((uint32_t)((uint32_t)(local_rbx)), *(uint8_t *)(result + 0xC), (uint32_t)(0x206D654DULL), Arg4);
    result = PopUpdateConsoleDisplayState((uint32_t)((uint32_t)(local_rbx)), *(uint8_t *)(result + 0xC), (uint32_t)(0x206D654DULL), Arg4);
    if ((uint8_t)(*(uint8_t *)(result + 0xC)) != 0) {
        result = PopPowerAggregatorNotifyDisplayPoweredOn((uint32_t)((uint32_t)(local_rbx)), *(uint8_t *)(result + 0xC), (uint32_t)(0x206D654DULL), Arg4);
    }
    Arg1 = ((*(uint8_t *)(result + 0xC)) == 0) ? 1 : 0;
    result = PopDiagTraceSessionDisplayStateChange(Arg1, (uint32_t)(*(uint32_t *)(result + 0x8)), *(uint8_t *)(result + 0xD), (uint32_t)(*(uint32_t *)(result + 0x10)));
loc_00A8BD17:
    result = PopReleasePolicyLock(Arg1, (uint32_t)(*(uint32_t *)(result + 0x8)), *(uint8_t *)(result + 0xD), (uint32_t)(*(uint32_t *)(result + 0x10)));
    goto loc_00A8BA5D;
loc_00A8BD21:
    result = PopIsPlatformAoAcCapable(Arg1, (uint32_t)(*(uint32_t *)(result + 0x8)), *(uint8_t *)(result + 0xD), (uint32_t)(*(uint32_t *)(result + 0x10)));
    if ((uint8_t)(result) == 0) goto loc_00A8BA58;
    if (*(uint8_t *)(result + 0xC) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(0x400ULL))), (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(result + 0x10)));
    if (result == 0) goto loc_00A8BB03;
    result = PopQueryBootSessionStandbyActivationInfo(result, (uint32_t)((uint32_t)((uint32_t)(0x400ULL))), (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(result + 0x10)));
    if (sign_flag) goto loc_00A8BA5D;
loc_00A8BD6E:
    *(uint64_t *)(arg7) = result;
loc_00A8BD71:
    *(uint32_t *)(arg8) = (uint32_t)((uint32_t)(0x400ULL));
    goto loc_00A8BBFC;
loc_00A8BD7A:
    if (((uint32_t)((uint32_t)(0x400ULL))) < 8) goto loc_00A8BAD7;
    if (*(uint8_t *)(result + 0xC) != 0) goto loc_00A8BB48;
    result = PopUpdateBackgroundCoolingStatus(*(uint8_t *)(result + 0x8), (uint32_t)((uint32_t)((uint32_t)(0x400ULL))), (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(result + 0x10)));
    goto loc_00A8BBA0;
loc_00A8BD9A:
    if (((uint32_t)((uint32_t)(0x400ULL))) < 8) goto loc_00A8BAD7;
    if (*(uint8_t *)(result + 0xC) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 32, (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(result + 0x10)));
    Arg1 = 0;
    if (result == 0) goto loc_00A8BB03;
    *(uint64_t *)(result) = v_xmm0;
loc_00A8BDDE:
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(arg7) = result;
    *(uint32_t *)(arg8) = 32;
loc_00A8BDED:
    *(uint8_t *)(arg9) = 1;
    goto loc_00A8BB6A;
loc_00A8BDF7:
    if (((uint32_t)((uint32_t)(0x400ULL))) < 12) goto loc_00A8BAD7;
    if (*(uint8_t *)(result + 0xC) != 0) goto loc_00A8BB48;
    result = PopNetUpdateStandbyRequest(*(uint8_t *)(result + 0x8), 32, (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(result + 0x10)));
    goto loc_00A8BBA0;
loc_00A8BE17:
    if (((uint32_t)((uint32_t)(0x400ULL))) != 20) goto loc_00A8BB48;
    if (*(uint8_t *)(result + 0xC) != 0) goto loc_00A8BB48;
    result = TtmNotifySessionTerminalInput((uint32_t)(*(uint32_t *)(result + 0x8)), (uint32_t)(*(uint32_t *)(result + 0xC)), *(uint8_t *)(result + 0x10), (uint32_t)(*(uint32_t *)(result + 0x10)));
    goto loc_00A8BB68;
loc_00A8BE3E:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) > 26) goto loc_00A8C105;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 26) goto loc_00A8C07F;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) - (21));
    if (condition_is_equal) goto loc_00A8BFE0;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8BF72;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8BF5B;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8BEA8;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A8BB48;
loc_00A8BE76:
    if (((uint32_t)((uint32_t)(0x400ULL))) < 12) goto loc_00A8BAD7;
    if (*(uint8_t *)(result + 0xC) != 0) goto loc_00A8BB48;
    if ((*(uint8_t *)(result + 0x8)) == ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x10))))) goto loc_00A8BE99;
    result = PopScreenOn((uint32_t)(*(uint32_t *)(result + 0x8)), (uint32_t)(*(uint32_t *)(result + 0xC)), *(uint8_t *)(result + 0x10), (uint32_t)(*(uint32_t *)(result + 0x10)));
    goto loc_00A8BB68;
loc_00A8BE99:
    result = PopScreenOff(30, (uint32_t)(*(uint32_t *)(result + 0xC)), *(uint8_t *)(result + 0x10), (uint32_t)(*(uint32_t *)(result + 0x10)));
    goto loc_00A8BB68;
loc_00A8BEA8:
    if (((uint32_t)((uint32_t)(0x400ULL))) < 40) goto loc_00A8BAD7;
    if (*(uint8_t *)(result + 0xC) != 0) goto loc_00A8BB48;
    if ((*(uint8_t *)(v_rip + 0x482BF6)) != ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x10))))) goto loc_00A8BF0D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) == ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_00A8BF15;
    v_stack_mB8 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)));
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)));
    v_stack_mC8 = (uint32_t)(*(uint32_t *)(result + 0x10));
    Arg4 = 0;
    *(uint8_t *)(v_rip + 0x482BBE) = 1;
    result = ZwUpdateWnfStateData(v_rip - 10925568, v_rip + 4729820, 1, Arg4);
    result = PopDiagTraceEventNoPayload(v_rip - 10935326, v_rip + 4729820, 1, Arg4);
    goto loc_00A8BF15;
loc_00A8BF0D:
    if (((uint32_t)(v_rip - 10935326)) == ((uint32_t)(result))) goto loc_00A8BA58;
loc_00A8BF15:
    v_stack_m60 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)));
    v_stack_m5C = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC)));
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)));
    v_stack_m54 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x14)));
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x18)));
    v_stack_m4C = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1C)));
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20)));
    v_stack_m44 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24)));
    result = PopBroadcastSessionInfo(32 - 28, 32, v_stack_m60, Arg4);
    goto loc_00A8BB68;
loc_00A8BF5B:
    if (((uint32_t)((uint32_t)(0x400ULL))) != 12) goto loc_00A8BB48;
    result = PopUpdateExternalDisplayState(*(uint8_t *)(result + 0x8), 32, v_stack_m60, Arg4);
    goto loc_00A8BB68;
loc_00A8BF72:
    if (((uint32_t)((uint32_t)(0x400ULL))) < 8) goto loc_00A8BAD7;
    if (*(uint8_t *)(result + 0xC) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 64, (uint32_t)(0x206D654DULL), Arg4);
    Arg1 = 0;
    if (result == 0) goto loc_00A8BB03;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = v_xmm1;
    *(uint64_t *)(arg7) = result;
    *(uint32_t *)(arg8) = 64;
    goto loc_00A8BDED;
loc_00A8BFE0:
    if (((uint32_t)((uint32_t)(0x400ULL))) < 96) goto loc_00A8BAD7;
    if ((*(uint64_t *)(result + 0x8)) != 0) goto loc_00A8BFF9;
    if (*(uint8_t *)(result + 0xC) == 0) goto loc_00A8BAD7;
loc_00A8BFF9:
    if ((*(uint32_t *)(result + 0x18)) != 412) goto loc_00A8C027;
    if ((*(uint8_t *)(result + 0x58)) != 0) goto loc_00A8C020;
    if ((*(uint32_t *)(result + 0x10)) == 0) goto loc_00A8C020;
    *(uint32_t *)(v_rip + 0x3DB53D) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20)));
    *(uint32_t *)(v_rip + 0x3DB53A) = 1;
    goto loc_00A8C027;
loc_00A8C020:
    *(uint32_t *)(v_rip + 0x3DB531) = 0;
loc_00A8C027:
    if (*(uint8_t *)(result + 0xC) == 0) goto loc_00A8C050;
    result = ExAllocatePool2(256, 8, (uint32_t)(0x206D654DULL), Arg4);
    if (result == 0) goto loc_00A8BB03;
loc_00A8C050:
    result = PopSetWatchdog(*(uint64_t *)(result + 0x8), result + 16, *(uint8_t *)(result + 0x58), Arg4);
    Arg1 = 0;
    if (*(uint8_t *)(result + 0xC) == 0) goto loc_00A8BB6A;
    *(uint64_t *)(result) = result;
    *(uint64_t *)(arg7) = result;
loc_00A8C072:
    *(uint32_t *)(arg8) = 8;
    goto loc_00A8BDED;
loc_00A8C07F:
    if (((uint32_t)((uint32_t)(0x400ULL))) < 12) goto loc_00A8BAD7;
    if (*(uint8_t *)(result + 0xC) != 0) goto loc_00A8BB48;
    result = PpmAcquireLock(v_rip + 4721511, result + 16, *(uint8_t *)(result + 0x58), Arg4);
    Arg2 = 0;
    if ((*(uint8_t *)(result + 0x8)) == 0) goto loc_00A8C0CA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x53AC2C)))) >= ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_00A8C0C0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x53AC2C))) + 1);
    *(uint32_t *)(v_rip + 0x53AC12) = Arg1;
    goto loc_00A8C0C5;
loc_00A8C0C0:
loc_00A8C0C5:
    goto loc_00A8C0E6;
loc_00A8C0CA:
    if (Arg1 == NULL) goto loc_00A8C0DF;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint32_t)(0xFFFFFFFFULL))));
    *(uint32_t *)(v_rip + 0x53ABF3) = Arg1;
    goto loc_00A8C0E4;
loc_00A8C0DF:
loc_00A8C0E4:
loc_00A8C0E6:
    if (Arg1 != NULL) goto loc_00A8C0F4;
    Arg1 = 0;
    result = PpmPerfUpdateDomainPolicy(Arg1, Arg2, *(uint8_t *)(result + 0x58), Arg4);
    goto loc_00A8BA5D;
loc_00A8C0F4:
    result = PpmReleaseLock(v_rip + 4721413, Arg2, *(uint8_t *)(result + 0x58), Arg4);
    goto loc_00A8BA5D;
loc_00A8C105:
    local_rbx = (uint32_t)(((uint32_t)(0xC00000BBULL)) - (27));
    if (condition_is_equal) goto loc_00A8C219;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8C1F0;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8C18D;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A8BB48;
    if (((uint32_t)((uint32_t)(0x400ULL))) < 8) goto loc_00A8BAD7;
    if (*(uint8_t *)(result + 0xC) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 3, (uint32_t)(0x206D654DULL), Arg4);
    Arg2 = 0;
    if (result == 0) goto loc_00A8BB03;
    *(uint8_t *)(result) = (uint8_t)(*(uint8_t *)(v_rip + 0x53AA09));
    *(uint8_t *)(result + 0x1) = (uint8_t)(*(uint8_t *)(v_rip + 0x53A971));
    result = ((*(uint32_t *)(v_rip + 0x53AC34)) != 0) ? 1 : 0;
    *(uint8_t *)(result + 0x2) = (uint8_t)(result);
    *(uint64_t *)(arg7) = result;
    *(uint32_t *)(arg8) = 3;
loc_00A8C181:
    *(uint8_t *)(arg9) = 1;
    goto loc_00A8BA5D;
loc_00A8C18D:
    if (((uint32_t)((uint32_t)(0x400ULL))) < 8) goto loc_00A8BAD7;
    if (*(uint8_t *)(result + 0xC) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 48, (uint32_t)(0x206D654DULL), Arg4);
    Arg1 = 0;
    if (result == 0) goto loc_00A8BB03;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(arg7) = result;
    *(uint32_t *)(arg8) = 48;
    goto loc_00A8BDED;
loc_00A8C1F0:
    if (((uint32_t)((uint32_t)(0x400ULL))) != 12) goto loc_00A8BB48;
    v_stack_mA0 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)));
    result = PopSetPowerSettingValueAcDc(v_rip - 10987511, (uint32_t)(0x400ULL) - 8, v_stack_mA0, Arg4);
    goto loc_00A8BB68;
loc_00A8C219:
    if (((uint32_t)((uint32_t)(0x400ULL))) < 16) goto loc_00A8BAD7;
    if (*(uint8_t *)(result + 0xC) != 0) goto loc_00A8BB48;
    result = PopTransitionCheckpoint((uint32_t)(*(uint32_t *)(result + 0x8)), (uint32_t)(*(uint32_t *)(result + 0xC)), v_stack_mA0, Arg4);
    goto loc_00A8BB68;
loc_00A8C23C:
    if (0 > 42) goto loc_00A8C53C;
    if (0 == 42) goto loc_00A8C4F3;
    if (0 > 37) goto loc_00A8C313;
    if (0 == 37) goto loc_00A8C2C5;
    Arg1 = (uint32_t)((0) - (32));
    if (condition_is_equal) goto loc_00A8C3F9;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8BA58;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8C3F9;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8C3F9;
    if (Arg1 != 1) goto loc_00A8BB48;
    if (((uint32_t)((uint32_t)(0x400ULL))) < 12) goto loc_00A8BAD7;
    if (*(uint8_t *)(result + 0xC) != 0) goto loc_00A8BB48;
    result = PopAcquireRwLockExclusive(v_rip + 4702622, (uint32_t)(*(uint32_t *)(result + 0xC)), v_stack_mA0, Arg4);
    *(uint8_t *)(v_rip + 0x47C15C) = (uint8_t)(*(uint8_t *)(result + 0x8));
    result = PopReleaseRwLock(v_rip + 4702610, (uint32_t)(*(uint32_t *)(result + 0xC)), v_stack_mA0, Arg4);
    Arg1 = 0;
    result = PopEsQueueStateEvaluation(Arg1, (uint32_t)(*(uint32_t *)(result + 0xC)), v_stack_mA0, Arg4);
    goto loc_00A8BB68;
loc_00A8C2C5:
    if (((uint32_t)((uint32_t)(0x400ULL))) < 8) goto loc_00A8BAD7;
    if (*(uint8_t *)(result + 0xC) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 4, (uint32_t)(0x206D654DULL), Arg4);
    Arg2 = 0;
    if (result == 0) goto loc_00A8BB03;
loc_00A8C301:
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x47FA43)));
    *(uint64_t *)(arg7) = result;
    *(uint32_t *)(arg8) = 4;
    goto loc_00A8C181;
loc_00A8C313:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(result + 0x8)))) - (38));
    if (condition_is_equal) goto loc_00A8C3F9;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8C3D9;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8C3A7;
    if (Arg1 != 1) goto loc_00A8BB48;
    if (((uint32_t)((uint32_t)(0x400ULL))) != 16) goto loc_00A8BB48;
    if (*(uint8_t *)(result + 0xC) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 1, (uint32_t)(0x206D654DULL), Arg4);
    Arg2 = 0;
    if (result == 0) goto loc_00A8BB03;
    if (*(uint64_t *)(result + 0x8) == 0) goto loc_00A8C393;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x138) + 0x28) == 0) goto loc_00A8C393;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x138) + 0x28) + 0x50) == 0) goto loc_00A8C393;
    result = 1;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x138) + 0x28) + 0x50) + 0x40)) == 0) {
        result = 0;
    }
    *(uint8_t *)(result) = (uint8_t)(result);
    *(uint64_t *)(arg7) = result;
    *(uint32_t *)(arg8) = 1;
    goto loc_00A8C181;
loc_00A8C3A7:
    if (((uint32_t)((uint32_t)(0x400ULL))) != 16) goto loc_00A8BB48;
    if ((*(uint32_t *)(result + 0x8)) != 0) goto loc_00A8BB48;
    if ((*(uint8_t *)(result + 0xC)) == 0) goto loc_00A8C3CF;
    result = PopDeepSleepSetDisengageReason((uint32_t)(0x400ULL) - 9, Arg2, (uint32_t)(0x206D654DULL), Arg4);
    goto loc_00A8BB68;
loc_00A8C3CF:
    result = PopDeepSleepClearDisengageReason((uint32_t)(0x400ULL) - 9, Arg2, (uint32_t)(0x206D654DULL), Arg4);
    goto loc_00A8BB68;
loc_00A8C3D9:
    if (((uint32_t)((uint32_t)(0x400ULL))) != 12) goto loc_00A8BB48;
    v_stack_mA8 = (uint8_t)(*(uint8_t *)(result + 0x8));
    goto loc_00A8BB86;
loc_00A8C3F9:
    if (((uint32_t)((uint32_t)(0x400ULL))) != 24) goto loc_00A8BB48;
    if (*(uint8_t *)(result + 0xC) == 0) goto loc_00A8C452;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8))) == 0) goto loc_00A8BB48;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8))))) << (2);
    if (Arg1 > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00A8C448;
    result = ExAllocatePool2(256, (uint32_t)(Arg1), (uint32_t)(0x206D654DULL), Arg4);
    Arg4 = 0;
    if (result != 0) goto loc_00A8C459;
    goto loc_00A8BB03;
loc_00A8C448:
    goto loc_00A8BA5D;
loc_00A8C452:
loc_00A8C459:
    if (((uint32_t)((uint32_t)(0xC0000095ULL))) != 31) goto loc_00A8C478;
    if ((*(uint32_t *)(result + 0x8)) != 0) goto loc_00A8C46B;
loc_00A8C464:
    goto loc_00A8C4E3;
loc_00A8C46B:
    result = PopBootStatGet(result, v_stack_m68, (uint32_t)(0x206D654DULL), Arg4);
    goto loc_00A8C4BB;
loc_00A8C478:
    if (((uint32_t)((uint32_t)(0xC000000DULL))) != 32) goto loc_00A8C490;
    if ((*(uint32_t *)(result + 0x8)) == 0) goto loc_00A8C464;
    result = PopBootStatSet(result, v_stack_m68, (uint32_t)(0x206D654DULL), Arg4);
    goto loc_00A8C4BB;
loc_00A8C490:
    if (((uint32_t)((uint32_t)(0xC000000DULL))) != 34) goto loc_00A8C4A5;
    if ((*(uint32_t *)(result + 0x8)) == 0) goto loc_00A8C464;
    result = PopBootStatCheckIntegrity(result, v_stack_m68, (uint32_t)(0x206D654DULL), Arg4);
    goto loc_00A8C4BB;
loc_00A8C4A5:
    if (((uint32_t)((uint32_t)(0xC000000DULL))) != 35) goto loc_00A8C4B1;
    result = PopBootStatRestoreDefaults(result, v_stack_m68, (uint32_t)(0x206D654DULL), Arg4);
    goto loc_00A8C4BB;
loc_00A8C4B1:
    if (((uint32_t)((uint32_t)(0xC000000DULL))) != 38) goto loc_00A8C4DE;
    result = PopBootStatUnlock(result, v_stack_m68, (uint32_t)(0x206D654DULL), Arg4);
loc_00A8C4BB:
    Arg4 = 0;
    if (sign_flag) goto loc_00A8C4E3;
    if (v_stack_m68 == 0) goto loc_00A8C7D8;
    *(uint64_t *)(arg7) = v_stack_m68;
    *(uint32_t *)(arg8) = 0;
    *(uint8_t *)(arg9) = 1;
    goto loc_00A8C7D8;
loc_00A8C4DE:
loc_00A8C4E3:
    if (v_stack_m68 == 0) goto loc_00A8BA5D;
    Arg2 = 0;
    goto loc_00A8BC50;
loc_00A8C4F3:
    if (0 < 8) goto loc_00A8BAD7;
    if (v_stack_m68 == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 32, (uint32_t)(0x206D654DULL), Arg4);
    Arg1 = 0;
    if (result == 0) goto loc_00A8BB03;
    *(uint64_t *)(result) = v_xmm0;
    goto loc_00A8BDDE;
loc_00A8C53C:
    if (((uint32_t)((uint32_t)(0xC00000BBULL))) > 48) goto loc_00A8C743;
    if (((uint32_t)((uint32_t)(0xC00000BBULL))) == 48) goto loc_00A8C716;
    local_rbx = (uint32_t)(((uint32_t)(0xC00000BBULL)) - (43));
    if (condition_is_equal) goto loc_00A8C6B5;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8C5F4;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8C5CF;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8C5A7;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A8BB48;
    if (0 < 20) goto loc_00A8BAD7;
    if (v_stack_m68 != 0) goto loc_00A8BB48;
    if ((*(uint32_t *)(result + 0x4)) == 0) goto loc_00A8C593;
loc_00A8C589:
    goto loc_00A8BA5D;
loc_00A8C593:
    result = PpmInternalProcessorIdleVeto((uint32_t)(*(uint32_t *)(result + 0x8)), (uint32_t)(*(uint32_t *)(result + 0xC)), *(uint8_t *)(result + 0x10), Arg4);
    goto loc_00A8BBA0;
loc_00A8C5A7:
    if (0 != 32) goto loc_00A8BB48;
    if (v_stack_m68 != 0) goto loc_00A8BB48;
    result = PopPowerRequestNotifyUserSessionAttributed((uint32_t)(*(uint32_t *)(result + 0x18)), *(uint64_t *)(result + 0x8), *(uint64_t *)(result + 0x10), Arg4);
    goto loc_00A8BB68;
loc_00A8C5CF:
    local_rbx = 0;
loc_00A8C5D1:
    if (0 != 12) goto loc_00A8BB48;
    if ((*(uint8_t *)(result + 0x8)) == 0) goto loc_00A8C5EA;
    result = PoUserShutdownInitiated((uint32_t)(*(uint32_t *)(result + 0x18)), *(uint64_t *)(result + 0x8), *(uint64_t *)(result + 0x10), Arg4);
    goto loc_00A8BA5D;
loc_00A8C5EA:
    result = PoUserShutdownCancelled((uint32_t)(*(uint32_t *)(result + 0x18)), *(uint64_t *)(result + 0x8), *(uint64_t *)(result + 0x10), Arg4);
    goto loc_00A8BA5D;
loc_00A8C5F4:
    if (0 < 144) goto loc_00A8BAD7;
    if (v_stack_m68 != 0) goto loc_00A8BB48;
    Arg1 = 0;
    result = RtlCheckTokenMembership(Arg1, *(uint64_t *)(v_rip + 0x48099F), v_stack_mA8, Arg4);
    local_r14 = 0;
    if (sign_flag) goto loc_00A8BA5D;
    if (v_stack_mA8 == 0) goto loc_00A8B893;
    result = PopIsPlatformAoAcCapable(Arg1, *(uint64_t *)(v_rip + 0x48099F), v_stack_mA8, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A8BA58;
    result = RtlStringCbLengthW(result + 8, 128, v_stack_m90, Arg4);
    if (sign_flag) goto loc_00A8BA5D;
    if (v_stack_m90 != 0) goto loc_00A8C677;
    if (*(uint64_t *)(result + 0x88) == 0) goto loc_00A8C680;
    goto loc_00A8BB48;
loc_00A8C677:
    if (*(uint64_t *)(result + 0x88) == 0) goto loc_00A8BB48;
loc_00A8C680:
    result = PopAcquirePolicyLock(result + 8, 128, v_stack_m90, Arg4);
    *(uint16_t *)(v_rip + 0x48210F) = 0;
    result = RtlStringCbCopyW(v_rip + 4727045, 128, result + 8, Arg4);
    *(uint64_t *)(v_rip + 0x482170) = *(uint64_t *)(result + 0x88);
    goto loc_00A8BD17;
loc_00A8C6B5:
    if ((((uint32_t)(local_r14 - 8)) & (0xFFFFFFFBULL)) != 0) goto loc_00A8BB48;
    if (v_stack_m68 == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 8, (uint32_t)(0x206D654DULL), Arg4);
    result = 0;
    if (0 == 0) goto loc_00A8BB03;
    if (0 != 12) {
        Arg1 = 0;
    }
    result = PpmPerfGetBrandedFrequency(Arg1, 0, (uint32_t)(0x206D654DULL), Arg4);
loc_00A8C704:
loc_00A8C708:
    if (sign_flag) goto loc_00A8BC4B;
    *(uint64_t *)(128) = result;
    goto loc_00A8BBF4;
loc_00A8C716:
    if (0 < 16) goto loc_00A8BAD7;
    if (result != 0) goto loc_00A8BB48;
    if ((*(uint32_t *)(result + 0x4)) != 0) goto loc_00A8C589;
    result = PpmInternalPlatformIdleVeto((uint32_t)(*(uint32_t *)(result + 0x8)), *(uint8_t *)(result + 0xC), (uint32_t)(0x206D654DULL), Arg4);
    goto loc_00A8BBA0;
loc_00A8C743:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) - (49));
    if (condition_is_equal) goto loc_00A8C815;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8C7E0;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8C798;
    if (Arg1 != 2) goto loc_00A8BB48;
loc_00A8C769:
    v_stack_mC8 = 128;
    result = PopDirectedDripsUmPowerInformationInternal((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), 0, result, Arg8);
    result = 0;
    if (sign_flag) goto loc_00A8BA5D;
    if ((*(uint64_t *)(128)) == 0) goto loc_00A8BA5D;
    goto loc_00A8BBFC;
loc_00A8C798:
    if (0 != 0) goto loc_00A8C7AF;
    if (0 < 16) goto loc_00A8BAD7;
    goto loc_00A8C7CA;
loc_00A8C7AF:
    if (0 != 1) goto loc_00A8BB48;
    if (0 < 24) goto loc_00A8BAD7;
loc_00A8C7CA:
    *(uint64_t *)(v_rip + 0x4800D7) = *(uint64_t *)(result + 0x8);
    *(uint64_t *)(v_rip + 0x4800C8) = *(uint64_t *)(result + 0x10);
loc_00A8C7D8:
    goto loc_00A8BA5D;
loc_00A8C7E0:
    if (0 == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 1, (uint32_t)(0x206D654DULL), Arg8);
    Arg2 = 0;
    if (result == 0) goto loc_00A8BB03;
    goto loc_00A8C395;
loc_00A8C815:
    if (result == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 1, (uint32_t)(0x206D654DULL), Arg8);
    local_rdi = 0;
    if (result == 0) goto loc_00A8BB03;
    result = PopQueryPowerButtonBugcheckEnabled(256, 1, (uint32_t)(0x206D654DULL), Arg8);
    goto loc_00A8BB24;
loc_00A8C849:
    if (((uint32_t)(result)) > 78) goto loc_00A8CD60;
    if (((uint32_t)(result)) == 78) goto loc_00A8CCF2;
    if (((uint32_t)(result)) > 67) goto loc_00A8CA58;
    if (((uint32_t)(result)) == 67) goto loc_00A8CA23;
    if (((uint32_t)(result)) > 61) goto loc_00A8C947;
    if (((uint32_t)(result)) == 61) goto loc_00A8B946;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) - (56));
    if (condition_is_equal) goto loc_00A8C769;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8C91C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8C901;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8C8E6;
    if (Arg1 != 1) goto loc_00A8BB48;
    if (result == 0) goto loc_00A8BAD7;
    result = PopAcquireTransitionLock(8, 1, (uint32_t)(0x206D654DULL), Arg8);
    result = PopReadResumeContext(v_stack_m98, v_stack_m88, (uint32_t)(0x206D654DULL), Arg8);
    result = PopReleaseTransitionLock(8, v_stack_m88, (uint32_t)(0x206D654DULL), Arg8);
    Arg1 = 0;
    if (sign_flag) goto loc_00A8BA5D;
    *(uint64_t *)(128) = v_stack_m88;
    *(uint32_t *)(arg8) = (uint32_t)((uint32_t)(v_stack_m98));
    goto loc_00A8BDED;
loc_00A8C8E6:
    if (0 < 24) goto loc_00A8BB48;
    result = PoDirectedDripsClearDeviceFlags(*(uint64_t *)(local_rdi + 0x8), (uint32_t)(*(uint32_t *)(local_rdi + 0x10)), (uint32_t)(0x206D654DULL), Arg8);
    goto loc_00A8BBA0;
loc_00A8C901:
    if (0 < 24) goto loc_00A8BB48;
    result = PoDirectedDripsSetDeviceFlags(*(uint64_t *)(local_rdi + 0x8), (uint32_t)(*(uint32_t *)(local_rdi + 0x10)), (uint32_t)(0x206D654DULL), Arg8);
    goto loc_00A8BBA0;
loc_00A8C91C:
    if (result != 0) goto loc_00A8BB48;
    result = PopPlRegisterPowerPlane(0, 0, (uint32_t)(0x206D654DULL), Arg8);
    goto loc_00A8BBA0;
loc_00A8C935:
    *(uint32_t *)(arg8) = 0x1000ULL;
    *(uint8_t *)(arg9) = 1;
    goto loc_00A8BBA0;
loc_00A8C947:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) - (62));
    if (condition_is_equal) goto loc_00A8C9EE;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8C9A0;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8C769;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8C973;
    if (Arg1 != 1) goto loc_00A8BB48;
    goto loc_00A8BA58;
loc_00A8C973:
    if (0 != 16) goto loc_00A8BB48;
    if (*(uint64_t *)(local_rdi + 0x8) == 0) goto loc_00A8BB48;
    result = PopFxClearDeviceConstraints(*(uint64_t *)(local_rdi + 0x8), 0, (uint32_t)(0x206D654DULL), Arg8);
    result = 0;
    if (sign_flag) goto loc_00A8BA5D;
    goto loc_00A8BBA0;
loc_00A8C9A0:
    if (0 == 0) goto loc_00A8BB48;
    result = SSHSupportQueryIsLibraryEnabled(*(uint64_t *)(local_rdi + 0x8), 0, (uint32_t)(0x206D654DULL), Arg8);
    result = (uint8_t)(-(result));
    local_rbx = ((uint32_t)((uint32_t)(result))) & (v_rip + 3625945);
    if (condition_is_equal) goto loc_00A8BA58;
    result = ExAllocatePool2(256, 8, (uint32_t)(0x206D654DULL), Arg8);
    Arg1 = 0;
    if (result == 0) goto loc_00A8BB03;
    *(uint64_t *)(result) = local_rbx;
    *(uint64_t *)(128) = result;
    goto loc_00A8C072;
loc_00A8C9EE:
    if (result == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 1, (uint32_t)(0x206D654DULL), Arg8);
    Arg2 = 0;
    if (result == 0) goto loc_00A8BB03;
    goto loc_00A8C395;
loc_00A8CA23:
    *(uint32_t *)(arg8) = (uint32_t)(Arg8);
    *(void **)(128) = Arg8;
    result = ExAllocatePool2(256, 4, (uint32_t)(0x206D654DULL), Arg8);
    Arg2 = 0;
    if (result == 0) goto loc_00A8BB03;
    goto loc_00A8C301;
loc_00A8CA58:
    if (((uint32_t)(local_rbx)) > 73) goto loc_00A8CC27;
    if (((uint32_t)(local_rbx)) == 73) goto loc_00A8CC07;
    local_rbx = (uint32_t)((local_rbx) - (68));
    if (condition_is_equal) goto loc_00A8CBEF;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8CBA3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8CB14;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8CAD5;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A8BB48;
    if (result == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(0x900ULL))), (uint32_t)(0x206D654DULL), Arg8);
    if (result == 0) goto loc_00A8BB03;
    result = PpmPerfGetFrequencyBandStats(result, (uint32_t)((uint32_t)((uint32_t)(0x900ULL))), (uint32_t)(0x206D654DULL), Arg8);
loc_00A8CAC6:
    if (!sign_flag) goto loc_00A8BD6E;
    goto loc_00A8BBDF;
loc_00A8CAD5:
    if (((uint32_t)((uint32_t)(0x900ULL))) != 12) goto loc_00A8BB48;
    result = PopAcquireRwLockExclusive(v_rip + 4700695, (uint32_t)((uint32_t)((uint32_t)(0x900ULL))), (uint32_t)(0x206D654DULL), Arg8);
    if ((*(uint8_t *)(v_rip + 0x53A009)) != ((uint8_t)(*(uint8_t *)(result + 0x8)))) {
        Arg1 = (uint8_t)(*(uint8_t *)(result + 0x8));
        *(uint8_t *)(v_rip + 0x539FFF) = (uint8_t)(*(uint8_t *)(result + 0x8));
        result = PopDiagTraceSleepReliabilityDiagConfigUpdate(Arg1, (uint32_t)((uint32_t)((uint32_t)(0x900ULL))), (uint32_t)(0x206D654DULL), Arg8);
    }
    result = PopReleaseRwLock(v_rip + 4700662, (uint32_t)((uint32_t)((uint32_t)(0x900ULL))), (uint32_t)(0x206D654DULL), Arg8);
    goto loc_00A8BB68;
loc_00A8CB14:
    if (((uint32_t)((uint32_t)(0x900ULL))) < 12) goto loc_00A8BAD7;
    if ((*(uint32_t *)(result + 0x4)) > 2) goto loc_00A8BA58;
    if ((*(uint32_t *)(result + 0x4)) != 2) goto loc_00A8CB38;
    if (((uint32_t)((uint32_t)(0x900ULL))) < 32) goto loc_00A8BAD7;
loc_00A8CB38:
    if (result == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(256, 8, (uint32_t)(0x206D654DULL), Arg8);
    if (result == 0) goto loc_00A8BB03;
    if ((*(uint32_t *)(result + 0x4)) != 2) goto loc_00A8CB8F;
    v_stack_mB8 = result;
    v_stack_mC0 = (uint8_t)(*(uint8_t *)(result + 0x1C));
    v_stack_mC8 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x18)));
    result = PpmPerfGetVmCppcConfig((uint32_t)(*(uint32_t *)(result + 0xC)), (uint32_t)(*(uint32_t *)(result + 0x8)), (uint32_t)(*(uint32_t *)(result + 0x10)), (uint32_t)(*(uint32_t *)(result + 0x14)));
    goto loc_00A8CB9A;
loc_00A8CB8F:
    result = PpmPerfGetVmPerfConfig((uint32_t)(*(uint32_t *)(result + 0x8)), result, (uint32_t)(*(uint32_t *)(result + 0x10)), (uint32_t)(*(uint32_t *)(result + 0x14)));
loc_00A8CB9A:
    goto loc_00A8C708;
loc_00A8CBA3:
    if (result == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(256, 20, (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(result + 0x14)));
    local_rdi = 0;
    if (result == 0) goto loc_00A8BB03;
    result = PpmPerfGetVmPerfControlSupport(result, 20, (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(result + 0x14)));
    *(uint64_t *)(128) = result;
    result = (uint32_t)((result) & (0xFFFFFFEDULL));
    result = (uint32_t)((result) + (20));
    *(uint32_t *)(arg8) = (uint32_t)(result);
    goto loc_00A8BB31;
loc_00A8CBEF:
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_rip + 0x37E963))));
    Arg1 = (uint32_t)(~(result));
    local_rbx = (uint32_t)(((uint32_t)(0xC00000BBULL)) & (Arg1));
    goto loc_00A8BA5D;
loc_00A8CC07:
    if (((uint32_t)((uint32_t)(0x900ULL))) < 12) goto loc_00A8BAD7;
    if (result != 0) goto loc_00A8BB48;
    result = PopUserPresenceHostStateChange((uint32_t)(*(uint32_t *)(local_rdi + 0x8)), 20, (uint32_t)(0x206D654DULL), (uint32_t)(*(uint32_t *)(result + 0x14)));
    goto loc_00A8BB68;
loc_00A8CC27:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (74));
    if (condition_is_equal) goto loc_00A8CC84;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8CC84;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8CC41;
    if (Arg1 != 1) goto loc_00A8BB48;
loc_00A8CC41:
    if (((uint32_t)((uint32_t)(0x900ULL))) != 12) goto loc_00A8BAD7;
    if (result == 0) goto loc_00A8BB48;
    result = PpmIdleGetConcurrencyStats((uint32_t)((uint32_t)(local_rbx)), *(uint16_t *)(local_rdi + 0x8), v_stack_m80, v_stack_m94);
    if (sign_flag) goto loc_00A8BA5D;
    *(uint64_t *)(128) = v_stack_m80;
    *(uint32_t *)(arg8) = (uint32_t)((uint32_t)(v_stack_m94));
    goto loc_00A8BBFC;
loc_00A8CC84:
    if (((uint32_t)((uint32_t)(0x900ULL))) != 12) goto loc_00A8BAD7;
    if (result == 0) goto loc_00A8BB48;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 74) goto loc_00A8CCA4;
    goto loc_00A8CCB3;
loc_00A8CCA4:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 75) goto loc_00A8BB48;
loc_00A8CCB3:
    result = ExAllocatePool2(256, 592, (uint32_t)(0x206D654DULL), v_stack_m94);
    if (result == 0) goto loc_00A8BB03;
    result = PpmIdleGetPackageIdleIntervalStats((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint16_t *)(local_rdi + 0x8), result, v_stack_m94);
    if (sign_flag) goto loc_00A8BC4B;
    *(uint64_t *)(128) = result;
    goto loc_00A8BD71;
loc_00A8CCF2:
    if (result == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(256, 4, (uint32_t)(0x206D654DULL), v_stack_m94);
    local_rdi = 0;
    if (result == 0) goto loc_00A8BB03;
loc_00A8CD25:
    if ((*(uint64_t *)(v_rip + 0x539E83)) == (v_rip + 5480060)) goto loc_00A8CD4C;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x539E83) + 0x1A8) != 0) goto loc_00A8CD42;
    goto loc_00A8CD25;
loc_00A8CD42:
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(v_rip + 0x539E83) + 0x1A8), 4, (uint32_t)(0x206D654DULL), v_stack_m94);
    goto loc_00A8CD4E;
loc_00A8CD4C:
loc_00A8CD4E:
    *(uint32_t *)(result) = 0;
    *(uint64_t *)(128) = result;
    *(uint32_t *)(arg8) = 4;
    goto loc_00A8BB31;
loc_00A8CD60:
    if (((uint32_t)(result)) > 89) goto loc_00A8D145;
    if (((uint32_t)(result)) == 89) goto loc_00A8D0CF;
    if (((uint32_t)(result)) > 84) goto loc_00A8CFEC;
    if (((uint32_t)(result)) == 84) goto loc_00A8CFAB;
    local_rbx = (uint32_t)((result) - (79));
    if (condition_is_equal) goto loc_00A8CED6;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8CE98;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8CE4D;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8CDDA;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A8BB48;
    if (592 != 16) goto loc_00A8BB48;
    if (0 == 0) goto loc_00A8BB48;
    if (Arg6 != ((uint32_t)(v_stack_m94))) goto loc_00A8BB48;
    if (result != 0) goto loc_00A8BB48;
    result = PopAdaptiveSetSystemInitiatedRebootTargetStateOverride(0, 4, (uint32_t)(0x206D654DULL), v_stack_m94);
    goto loc_00A8BBA0;
loc_00A8CDDA:
    if (592 != 12) goto loc_00A8BB48;
    if (0 == 0) goto loc_00A8BB48;
    if (Arg6 != ((uint32_t)(v_stack_m94))) goto loc_00A8BB48;
    if (result != 0) goto loc_00A8BB48;
    v_stack_mA0 = v_stack_m94;
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), 4, (uint32_t)(0x206D654DULL), v_stack_m94);
    v_stack_mA0 = (uint32_t)(result);
    v_stack_m9C = 1;
    v_stack_m9B = (uint8_t)(*(uint8_t *)(local_rdi + 0x8));
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), 4, (uint32_t)(0x206D654DULL), v_stack_m94);
    result = PopSessionWinlogonNotification((uint32_t)((uint32_t)(result)), v_stack_mA0, (uint32_t)(0x206D654DULL), v_stack_m94);
loc_00A8CE46:
    result = 0;
    goto loc_00A8BBA0;
loc_00A8CE4D:
    if (592 != 40) goto loc_00A8BB48;
    if (0 == 0) goto loc_00A8BB48;
    if (Arg6 != 16) goto loc_00A8BB48;
    if (0 == 0) goto loc_00A8BB48;
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), v_stack_mA0, (uint32_t)(0x206D654DULL), v_stack_m94);
    result = PopAdaptiveGetSessionState((uint32_t)((uint32_t)(result)), local_rdi + 8, result, v_stack_m94);
    goto loc_00A8CE46;
loc_00A8CE98:
    if (592 != 8) goto loc_00A8BB48;
    if (0 == 0) goto loc_00A8BB48;
    if (Arg6 != ((uint32_t)(v_stack_m94))) goto loc_00A8BB48;
    if (result != 0) goto loc_00A8BB48;
    result = PopAdaptiveGetSystemInitiatedRebootTargetState((uint32_t)((uint32_t)(result)), local_rdi + 8, result, v_stack_m94);
    *(uint64_t *)(v_rip + 0x54B346) = result;
    *(uint8_t *)(v_rip + 0x54B337) = 1;
    goto loc_00A8CE46;
loc_00A8CED6:
    if (0 == 0) goto loc_00A8BB48;
    if (592 != 12) goto loc_00A8BB48;
    v_stack_mA4 = (uint32_t)(v_stack_m94);
    Arg4 = 0;
    Arg3 = 0;
    result = PpmPerfQueryProcMeasurementValues((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))), v_stack_mA4, Arg3, Arg4);
    if (sign_flag) goto loc_00A8BA5D;
    if (Arg6 != 4) goto loc_00A8CF53;
    result = ExAllocatePool2(256, 592 - 8, (uint32_t)(0x206D654DULL), Arg4);
    if (result == 0) goto loc_00A8BB03;
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(v_stack_mA4));
    *(uint64_t *)(128) = result;
    *(uint32_t *)(arg8) = 4;
    goto loc_00A8BBFC;
loc_00A8CF53:
    if (Arg6 < ((uint32_t)((uint32_t)(v_stack_mA4) + (uint32_t)(v_stack_mA4) * 2 * 8 + 8))) goto loc_00A8BAD7;
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)((uint32_t)(v_stack_mA4) + (uint32_t)(v_stack_mA4) * 2 * 8 + 8)), (uint32_t)(0x206D654DULL), Arg4);
    if (result == 0) goto loc_00A8BB03;
    *(uint32_t *)(arg8) = (uint32_t)((uint32_t)(v_stack_mA4) + (uint32_t)(v_stack_mA4) * 2 * 8 + 8);
    *(uint8_t *)(arg9) = 1;
    *(uint64_t *)(128) = result;
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(v_stack_mA4));
    Arg3 = (result) + (8);
    Arg4 = (uint32_t)(((uint32_t)(v_stack_mA4) + (uint32_t)(v_stack_mA4) * 2) << (3));
    result = PpmPerfQueryProcMeasurementValues((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))), v_stack_mA4, Arg3, Arg4);
    goto loc_00A8BBA0;
loc_00A8CFAB:
    if ((uint32_t)(*(uint32_t *)(local_rdi + 0x8)) == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(160 + 96, 160, (uint32_t)(0x206D654DULL), Arg4);
    if (result == 0) goto loc_00A8BB03;
loc_00A8CFDC:
    result = PopFanReadFanNoiseInfo(160 - 76, result, 160, Arg4);
    goto loc_00A8CAC6;
loc_00A8CFEC:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) - (85));
    if (condition_is_equal) goto loc_00A8D098;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8D041;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8D018;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A8BB48;
    result = PopManageTransitionRecordRequest(160 - 76, result, 160, Arg4);
    goto loc_00A8BBA0;
loc_00A8D018:
    if (result == 0) goto loc_00A8BB48;
    if (160 != 24) goto loc_00A8BB48;
    if ((uint32_t)(*(uint32_t *)(local_rdi + 0x8)) != 0) goto loc_00A8BB48;
    result = PopShutdownListenerRemoveCallback(result, result, 160, Arg4);
    goto loc_00A8BBA0;
loc_00A8D041:
    if (160 < 8) goto loc_00A8BAD7;
    if ((uint32_t)(*(uint32_t *)(local_rdi + 0x8)) == 0) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 8, (uint32_t)(0x206D654DULL), Arg4);
    Arg2 = 0;
    if (result == 0) goto loc_00A8BB03;
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3DB4EF)));
    *(uint32_t *)(result + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3DB4E3)));
    *(uint64_t *)(128) = result;
    *(uint32_t *)(arg8) = 8;
    goto loc_00A8C181;
loc_00A8D098:
    if ((uint32_t)(*(uint32_t *)(local_rdi + 0x8)) == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(256, 88, (uint32_t)(0x206D654DULL), Arg4);
    if (result == 0) goto loc_00A8BB03;
    goto loc_00A8CFDC;
loc_00A8D0CF:
    if ((uint32_t)(*(uint32_t *)(local_rdi + 0x8)) == 0) goto loc_00A8BAD7;
    if (Arg6 != 20) goto loc_00A8BAD7;
    result = PopAcquirePolicyLock(88 - 3, 88, (uint32_t)(0x206D654DULL), Arg4);
    local_rbx = 0;
    if ((*(uint8_t *)(v_rip + 0x47FDE4)) == 0) goto loc_00A8D13B;
    result = ExAllocatePool2(256, local_rbx + 20, (uint32_t)(0x206D654DULL), Arg4);
    if (result == 0) goto loc_00A8D131;
    *(uint64_t *)(result) = v_xmm0;
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x47BFD7)));
    *(uint64_t *)(128) = result;
    *(uint32_t *)(arg8) = 20;
    *(uint8_t *)(arg9) = 1;
    goto loc_00A8BD17;
loc_00A8D131:
    goto loc_00A8BD17;
loc_00A8D13B:
    goto loc_00A8BD17;
loc_00A8D145:
    if (((uint32_t)((uint32_t)(0xC00000BBULL))) > 95) goto loc_00A8D2BA;
    if (((uint32_t)((uint32_t)(0xC00000BBULL))) == 95) goto loc_00A8D40F;
    local_rbx = (uint32_t)(((uint32_t)(0xC00000BBULL)) - (90));
    if (condition_is_equal) goto loc_00A8D28B;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8D22C;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8D20B;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A8D1BF;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A8BB48;
    if (88 < 12) goto loc_00A8BAD7;
    if ((uint32_t)(*(uint32_t *)(local_rdi + 0x8)) == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(256, local_rbx + 7, (uint32_t)(0x206D654DULL), Arg4);
    if (result == 0) goto loc_00A8BB03;
    result = PpmPerfGetVmPerfPriorityConfig((uint32_t)(*(uint32_t *)(result + 0x8)), result, (uint32_t)(0x206D654DULL), Arg4);
    goto loc_00A8C704;
loc_00A8D1BF:
    if ((uint32_t)(result) != 0) goto loc_00A8BA58;
    if (result == 0) goto loc_00A8BB48;
    result = ExAllocatePool2(256, 8, (uint32_t)(0x206D654DULL), Arg4);
    local_rdi = 0;
    if (result == 0) goto loc_00A8BB03;
    result = PpmPerfGetVmPerfPrioritySupport(result, 8, (uint32_t)(0x206D654DULL), Arg4);
    *(uint64_t *)(128) = result;
    *(uint32_t *)(arg8) = 8;
    goto loc_00A8BB31;
loc_00A8D20B:
    v_stack_mC0 = Arg8;
    v_stack_mC8 = 128;
    result = PopHandleProvIdentifierRequest(0, 88, result, (uint32_t)(Arg6));
    goto loc_00A8BBA0;
loc_00A8D22C:
    if (result == 0) goto loc_00A8BAD7;
    if (Arg6 < 36) goto loc_00A8BAD7;
    result = ExAllocatePool2(256, 36, (uint32_t)(0x206D654DULL), (uint32_t)(Arg6));
    local_rsi = 0;
    if (result == 0) goto loc_00A8BB03;
    result = PopGetEnergyEstimationInfo(result, 36, (uint32_t)(0x206D654DULL), (uint32_t)(Arg6));
    if (sign_flag) goto loc_00A8BBDF;
    *(uint64_t *)(128) = result;
    *(uint32_t *)(arg8) = 36;
    *(uint8_t *)(arg9) = 1;
    goto loc_00A8BA5D;
loc_00A8D28B:
    if (result == 0) goto loc_00A8BB48;
    if (36 < 20) goto loc_00A8BB48;
    if (0 == 0) goto loc_00A8D2AD;
    if (Arg6 != ((uint32_t)((uint32_t)(Arg6)))) goto loc_00A8BB48;
loc_00A8D2AD:
    result = PopSuspendResumeInvocation(result, 36, (uint32_t)(0x206D654DULL), (uint32_t)(Arg6));
    goto loc_00A8BBA0;
loc_00A8D2BA:
    Arg1 = (uint32_t)((0) - (96));
    if (condition_is_equal) goto loc_00A8D40F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8D3CB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A8D312;
    if (Arg1 != 1) goto loc_00A8BB48;
    result = Feature_Servicing_BatteryTestExempt__private_IsEnabledDeviceUsageNoInline(Arg1, 36, (uint32_t)(0x206D654DULL), (uint32_t)(Arg6));
    if ((uint32_t)(result) == 0) goto loc_00A8BB48;
    if (result == 0) goto loc_00A8BB48;
    if (0 != 0) goto loc_00A8BB48;
    if (36 < 12) goto loc_00A8BAD7;
    result = PopBatteryUpdateTestExempt(*(uint8_t *)(result + 0x8), 36, (uint32_t)(0x206D654DULL), (uint32_t)(Arg6));
    goto loc_00A8BBA0;
loc_00A8D312:
    result = Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline(*(uint8_t *)(result + 0x8), 36, (uint32_t)(0x206D654DULL), (uint32_t)(Arg6));
    local_r15 = 0;
    if ((uint32_t)(result) == 0) goto loc_00A8BB48;
    v_stack_mA8 = 0;
    Arg1 = 0;
    result = SeIsAppContainerOrIdentifyLevelContext(Arg1, v_stack_mA8, (uint32_t)(0x206D654DULL), (uint32_t)(Arg6));
    if (sign_flag) goto loc_00A8BA5D;
    if (v_stack_mA8 != 0) goto loc_00A8B893;
    if (v_stack_mA0 != 0) goto loc_00A8BB48;
    if (36 != 48) goto loc_00A8D3C1;
    if (0 == 0) goto loc_00A8D3C1;
    if (Arg6 != 16) goto loc_00A8D3C1;
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), v_stack_mA8, (uint32_t)(0x206D654DULL), (uint32_t)(Arg6));
    result = PopSessionConnectionChangeV2((uint32_t)((uint32_t)(result)), result + 8, result + 16, 0);
    result = PsGetProcessSessionIdEx(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), result + 8, result + 16, 0);
    result = *(uint64_t *)(v_rip + 0x3DA3F3);
    if (*(uint64_t *)(v_rip + 0x3DA3F3) != 0) {
        Arg4 = *(uint32_t *)(result + 0xC);
        Arg2 = 0;
        Arg3 = *(uint8_t *)(result + 0x8);
        result = guard_dispatch_icall((uint32_t)((uint32_t)(result)), Arg2, Arg3, Arg4);
    }
    goto loc_00A8BA5D;
loc_00A8D3C1:
    goto loc_00A8BA5D;
loc_00A8D3CB:
    if (36 != 12) goto loc_00A8BB48;
    if (0 == 0) goto loc_00A8BB48;
    if (Arg6 != 1) goto loc_00A8BB48;
    *(uint8_t *)(local_rsi) = (uint8_t)(Arg4);
    result = Feature_Servicing_PDCAgentSessions__private_IsEnabledDeviceUsageNoInline((uint32_t)((uint32_t)(result)), Arg2, Arg3, Arg4);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00A8BB6A;
    if ((*(uint32_t *)(result + 0x8)) != 0x3937A27ULL) goto loc_00A8BB6A;
    *(uint8_t *)(local_rsi) = 1;
    goto loc_00A8BB6A;
loc_00A8D40F:
    if (36 != 12) goto loc_00A8BB48;
    if (0 != 0) goto loc_00A8BB48;
    if ((*(uint32_t *)(result + 0x4)) != Arg4) goto loc_00A8BB48;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)))) >= 32) goto loc_00A8BB48;
    Arg2 = (((uint32_t)((uint32_t)(0xC0000206ULL))) == 95) ? 1 : 0;
    result = PopNotifyWin32kRequestStatus((uint32_t)(*(uint32_t *)(result + 0x8)), Arg2, Arg3, Arg4);
    goto loc_00A8BBA0;
loc_00A8D448:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (176);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x18` | `32` | `R` |
| `Arg3` | `+ 0x4` | `32` | `R` |
| `Arg3` | `+ 0x8` | `8` | `R` |
| `Arg3` | `+ 0x8` | `16` | `R` |
| `Arg3` | `+ 0x8` | `32` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0xC` | `8` | `R` |
| `Arg3` | `+ 0xC` | `32` | `R` |
| `Arg3` | `+ 0xD` | `8` | `R` |
| `Arg3` | `+ 0x10` | `8` | `R` |
| `Arg3` | `+ 0x10` | `32` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x14` | `32` | `R` |
| `Arg3` | `+ 0x18` | `32` | `R` |
| `Arg3` | `+ 0x1C` | `8` | `R` |
| `Arg3` | `+ 0x1C` | `32` | `R` |
| `Arg3` | `+ 0x20` | `32` | `R` |
| `Arg3` | `+ 0x24` | `32` | `R` |
| `Arg3` | `+ 0x58` | `8` | `R` |
| `Arg3` | `+ 0x88` | `64` | `R` |
| `Arg4` | `- 0x8` | `32` | `R` |
| `Arg7` | `+ 0x0` | `64` | `R` |
| `Arg7` | `+ 0x0` | `64` | `W` |
| `Arg8` | `+ 0x0` | `32` | `W` |
| `Arg9` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8B7C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
