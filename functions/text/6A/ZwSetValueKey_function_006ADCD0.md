# ZwSetValueKey

- RVA: `0x006ADCD0`–`0x006ADCEF` (길이 `31` bytes)
- VA: `0x00000001406ADCD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C0310`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **112**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [BiZwSetValueKey](../4B/BiZwSetValueKey_function_004BC668.md) at `0x004BC681`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC32B`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC395`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC3E3`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC431`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC47F`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC4CD`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC51B`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC569`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC5B8`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC60A`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC659`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC6A8`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC6F5`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC73D`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC785`
- [PopThermalWriteShutdownToRegistry](../4C/PopThermalWriteShutdownToRegistry_function_004CDA6C.md) at `0x004CDB40`
- [PopThermalWriteShutdownToRegistry](../4C/PopThermalWriteShutdownToRegistry_function_004CDA6C.md) at `0x004CDB75`
- [PopThermalWriteShutdownToRegistry](../4C/PopThermalWriteShutdownToRegistry_function_004CDA6C.md) at `0x004CDB9C`
- [PopThermalWriteShutdownToRegistry](../4C/PopThermalWriteShutdownToRegistry_function_004CDA6C.md) at `0x004CDBC4`
- [IopLiveDumpPolicyChangeWnfCallback](../59/IopLiveDumpPolicyChangeWnfCallback_function_0059D6E0.md) at `0x0059D7F7`
- [KeCommitSmtState](../5B/KeCommitSmtState_function_005BE7AC.md) at `0x005BE8B3`
- [VfClearVerifierSettings](../61/VfClearVerifierSettings_function_00611DB0.md) at `0x00611E79`
- [DifZwSetValueKeyWrapper](../64/DifZwSetValueKeyWrapper_function_0064B420.md) at `0x0064B537`
- [BapdpMarshallBootDataToRegistry](../65/BapdpMarshallBootDataToRegistry_function_006548A8.md) at `0x00654BDD`
- [ExpRecordShutdownTime](../65/ExpRecordShutdownTime_function_006555FC.md) at `0x006556AF`
- [MigrateOOBELanguageToInstallationLanguage](../65/MigrateOOBELanguageToInstallationLanguage_function_0065CEA8.md) at `0x0065D010`
- [MigrateOOBELanguageToInstallationLanguage](../65/MigrateOOBELanguageToInstallationLanguage_function_0065CEA8.md) at `0x0065D039`
- [WheaPersistBadPageToRegistry](../65/WheaPersistBadPageToRegistry_function_0065F58C.md) at `0x0065F7A9`
- [CmpSetSystemRegistryString](../66/CmpSetSystemRegistryString_function_0066A2F0.md) at `0x0066A352`
- [PopSetHiberPersistedRegValue](../../page/6F/PopSetHiberPersistedRegValue_function_006FE9F0.md) at `0x006FEAD8`
- [HalpRecordSecondaryGsivRange](../../page/70/HalpRecordSecondaryGsivRange_function_0070A4F8.md) at `0x0070A637`
- [HalpRecordSecondaryGsivRange](../../page/70/HalpRecordSecondaryGsivRange_function_0070A4F8.md) at `0x0070A667`
- [HalpPutAcpiHacksInRegistry](../../page/70/HalpPutAcpiHacksInRegistry_function_0070BC04.md) at `0x0070BD81`
- [HalpPutAcpiHacksInRegistry](../../page/70/HalpPutAcpiHacksInRegistry_function_0070BC04.md) at `0x0070BDAB`
- [HalpPutAcpiHacksInRegistry](../../page/70/HalpPutAcpiHacksInRegistry_function_0070BC04.md) at `0x0070BDDD`
- [HalpPutAcpiHacksInRegistry](../../page/70/HalpPutAcpiHacksInRegistry_function_0070BC04.md) at `0x0070BE06`
- [IopCrashDumpPolicyChangeWnfCallback](../../page/71/IopCrashDumpPolicyChangeWnfCallback_function_00719E40.md) at `0x00719F51`
- [IoSetSystemPartition](../../page/71/IoSetSystemPartition_function_0071DF90.md) at `0x0071E0B9`
- [PipHardwareConfigTriggerRespecialize](../../page/72/PipHardwareConfigTriggerRespecialize_function_0072364C.md) at `0x007236E2`
- [IoReportDetectedDevice](../../page/72/IoReportDetectedDevice_function_00725CD0.md) at `0x007265A7`
- [IoReportDetectedDevice](../../page/72/IoReportDetectedDevice_function_00725CD0.md) at `0x007265F2`
- [IopIsReportedAlready](../../page/72/IopIsReportedAlready_function_00726C6C.md) at `0x00726EF0`
- [IopWriteResourceList](../../page/72/IopWriteResourceList_function_0072A5F0.md) at `0x0072A6A2`
- [PnpSetRegistryDword](../../page/72/PnpSetRegistryDword_function_0072C2AC.md) at `0x0072C2EF`
- [PiDevCfgFindDeviceMigrationNode](../../page/73/PiDevCfgFindDeviceMigrationNode_function_00732920.md) at `0x0073323E`
- [PiDevCfgMakeServiceBootStart](../../page/73/PiDevCfgMakeServiceBootStart_function_00733BC8.md) at `0x00733D4E`
- [PiDevCfgMakeServiceBootStart](../../page/73/PiDevCfgMakeServiceBootStart_function_00733BC8.md) at `0x00733DA7`
- [PnpProfileUpdateHardwareProfile](../../page/73/PnpProfileUpdateHardwareProfile_function_0073773C.md) at `0x007377F9`
- [KseSetDeviceFlags](../../page/74/KseSetDeviceFlags_function_00748B20.md) at `0x00748C21`
- [PfpSetParameter](../../page/75/PfpSetParameter_function_007533FC.md) at `0x00753448`
- [PopSaveLidReliabilityState](../../page/75/PopSaveLidReliabilityState_function_0075F1E8.md) at `0x0075F23D`
- [PopThermalHandlePreviousShutdown](../../page/75/PopThermalHandlePreviousShutdown_function_0075F400.md) at `0x0075F66D`
- [PopThermalHandlePreviousShutdown](../../page/75/PopThermalHandlePreviousShutdown_function_0075F400.md) at `0x0075F69A`
- [PopThermalHandlePreviousShutdown](../../page/75/PopThermalHandlePreviousShutdown_function_0075F400.md) at `0x0075F6C6`
- [PopBatteryTestExemptPolicyRegKeyAccess](../../page/76/PopBatteryTestExemptPolicyRegKeyAccess_function_00766E04.md) at `0x00766E88`
- [EtwpAddMicroarchitecturalPmcToPmcGroup](../../page/7B/EtwpAddMicroarchitecturalPmcToPmcGroup_function_007B5228.md) at `0x007B535C`
- [EtwpAddMicroarchitecturalPmcToPmcGroup](../../page/7B/EtwpAddMicroarchitecturalPmcToPmcGroup_function_007B5228.md) at `0x007B53B7`
- [EtwpAddMicroarchitecturalPmcToPmcGroup](../../page/7B/EtwpAddMicroarchitecturalPmcToPmcGroup_function_007B5228.md) at `0x007B540E`
- [EtwpAddMicroarchitecturalPmcToPmcGroup](../../page/7B/EtwpAddMicroarchitecturalPmcToPmcGroup_function_007B5228.md) at `0x007B5459`
- [EtwpAddMicroarchitecturalPmcToPmcGroup](../../page/7B/EtwpAddMicroarchitecturalPmcToPmcGroup_function_007B5228.md) at `0x007B549B`
- [EtwpAddMicroarchitecturalPmcToPmcGroup](../../page/7B/EtwpAddMicroarchitecturalPmcToPmcGroup_function_007B5228.md) at `0x007B54D9`
- [EtwpAddMicroarchitecturalPmcToPmcGroup](../../page/7B/EtwpAddMicroarchitecturalPmcToPmcGroup_function_007B5228.md) at `0x007B5517`
- [EtwpAddMicroarchitecturalPmcToRegistry](../../page/7B/EtwpAddMicroarchitecturalPmcToRegistry_function_007B5558.md) at `0x007B5727`
- [EtwpAddMicroarchitecturalPmcToRegistry](../../page/7B/EtwpAddMicroarchitecturalPmcToRegistry_function_007B5558.md) at `0x007B576B`
- [ExpUpdateComPlusPackage](../../page/7C/ExpUpdateComPlusPackage_function_007C5580.md) at `0x007C560A`
- [ExSetLeapSecondEnabled](../../page/7C/ExSetLeapSecondEnabled_function_007C59F8.md) at `0x007C5A4F`
- [sub_007C8D5C](../../page/7C/Unknown_function_007C8D5C.md) at `0x007C8E2C`
- [ExpUuidSaveSequenceNumber](../../page/7D/ExpUuidSaveSequenceNumber_function_007D0C84.md) at `0x007D0D8C`
- [CMFRegisterEventTime](../../page/7D/CMFRegisterEventTime_function_007D382C.md) at `0x007D3996`
- [CMFRegisterEventTime](../../page/7D/CMFRegisterEventTime_function_007D382C.md) at `0x007D3A12`
- [CMFRegisterEventTime](../../page/7D/CMFRegisterEventTime_function_007D382C.md) at `0x007D3A36`
- [CmpInterlockedFunction](../../page/7D/CmpInterlockedFunction_function_007DAD70.md) at `0x007DAEB6`
- [CmpInterlockedFunction](../../page/7D/CmpInterlockedFunction_function_007DAD70.md) at `0x007DAEF5`
- [CmpLinkKeyToHive](../../page/7D/CmpLinkKeyToHive_function_007DAF30.md) at `0x007DB017`
- [CmSetAcpiHwProfile](../../page/7E/CmSetAcpiHwProfile_function_007E2584.md) at `0x007E2B14`
- [CmSetAcpiHwProfile](../../page/7E/CmSetAcpiHwProfile_function_007E2584.md) at `0x007E2C7E`
- [CmSetAcpiHwProfile](../../page/7E/CmSetAcpiHwProfile_function_007E2584.md) at `0x007E2CBB`
- [CmSetAcpiHwProfile](../../page/7E/CmSetAcpiHwProfile_function_007E2584.md) at `0x007E2D9E`
- [CmpAddAcpiAliasEntry](../../page/7E/CmpAddAcpiAliasEntry_function_007E2DC4.md) at `0x007E2F88`
- [CmpAddAcpiAliasEntry](../../page/7E/CmpAddAcpiAliasEntry_function_007E2DC4.md) at `0x007E2FBE`
- [CmpAddAcpiAliasEntry](../../page/7E/CmpAddAcpiAliasEntry_function_007E2DC4.md) at `0x007E2FF2`
- [CmpCloneHwProfile](../../page/7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E34F5`
- [CmpCloneHwProfile](../../page/7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E354D`
- [CmpCloneHwProfile](../../page/7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E3597`
- [CmpCloneHwProfile](../../page/7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E35D0`
- [CmpCloneHwProfile](../../page/7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E3628`
- [CmpCreateHwProfileFriendlyName](../../page/7E/CmpCreateHwProfileFriendlyName_function_007E3840.md) at `0x007E3A4D`
- [CmpMoveBiosAliasTable](../../page/7E/CmpMoveBiosAliasTable_function_007E4578.md) at `0x007E4919`
- [CmpAddProcessorConfigurationEntry](../../page/7E/CmpAddProcessorConfigurationEntry_function_007E4CF8.md) at `0x007E4FC3`
- [CmpAddProcessorConfigurationEntry](../../page/7E/CmpAddProcessorConfigurationEntry_function_007E4CF8.md) at `0x007E503F`
- [CmpAddProcessorConfigurationEntry](../../page/7E/CmpAddProcessorConfigurationEntry_function_007E4CF8.md) at `0x007E50A1`
- [CmpAddProcessorConfigurationEntry](../../page/7E/CmpAddProcessorConfigurationEntry_function_007E4CF8.md) at `0x007E50E2`
- [CmpAddProcessorConfigurationEntry](../../page/7E/CmpAddProcessorConfigurationEntry_function_007E4CF8.md) at `0x007E5129`
- [CmpRecordShutdownStopTime](../../page/7E/CmpRecordShutdownStopTime_function_007E551C.md) at `0x007E5650`
- [CmpRecordShutdownStopTime](../../page/7E/CmpRecordShutdownStopTime_function_007E551C.md) at `0x007E5691`
- [CmpRecordShutdownStopTime](../../page/7E/CmpRecordShutdownStopTime_function_007E551C.md) at `0x007E56E8`
- [CmpRecordShutdownStopTime](../../page/7E/CmpRecordShutdownStopTime_function_007E551C.md) at `0x007E5722`
- [CmpRestampVersion](../../page/7E/CmpRestampVersion_function_007E769C.md) at `0x007E772F`
- [CmpRestampVersion](../../page/7E/CmpRestampVersion_function_007E769C.md) at `0x007E7752`
- [CmpRestampVersion](../../page/7E/CmpRestampVersion_function_007E769C.md) at `0x007E7782`
- [CmpRestampVersion](../../page/7E/CmpRestampVersion_function_007E769C.md) at `0x007E77B5`
- [CmpRestampVersion](../../page/7E/CmpRestampVersion_function_007E769C.md) at `0x007E77E8`
- [CmpRestampVersion](../../page/7E/CmpRestampVersion_function_007E769C.md) at `0x007E781B`
- [CmpSetVersionData](../../page/7E/CmpSetVersionData_function_007E7854.md) at `0x007E7AE5`
- [CmpSetVersionData](../../page/7E/CmpSetVersionData_function_007E7854.md) at `0x007E7B17`
- [CmpSetVersionData](../../page/7E/CmpSetVersionData_function_007E7854.md) at `0x007E7B41`
- [CmpSetVersionData](../../page/7E/CmpSetVersionData_function_007E7854.md) at `0x007E7BF0`
- [CmpSetVersionData](../../page/7E/CmpSetVersionData_function_007E7854.md) at `0x007E7C26`
- [CmpSetVersionData](../../page/7E/CmpSetVersionData_function_007E7854.md) at `0x007E7CCB`
- [CmpSetVersionData](../../page/7E/CmpSetVersionData_function_007E7854.md) at `0x007E7D1C`
- [CmpUpdateReorganizeRegistryValues](../../page/7E/CmpUpdateReorganizeRegistryValues_function_007EA7D4.md) at `0x007EA933`
- [CmpUpdateReorganizeRegistryValues](../../page/7E/CmpUpdateReorganizeRegistryValues_function_007EA7D4.md) at `0x007EA971`
- [CmpSyncNextBackupHive](../../page/7E/CmpSyncNextBackupHive_function_007EC6C8.md) at `0x007EC7FC`
- [CmpInitializeRegistryNode](../../page/7E/CmpInitializeRegistryNode_function_007EE81C.md) at `0x007EE9FF`
- [CmpInitializeRegistryNode](../../page/7E/CmpInitializeRegistryNode_function_007EE81C.md) at `0x007EEA7C`
- [CmpInitializeRegistryNode](../../page/7E/CmpInitializeRegistryNode_function_007EE81C.md) at `0x007EEB5C`
- [CmpDoReDoRecord](../../page/7F/CmpDoReDoRecord_function_007F76B8.md) at `0x007F787C`
- [NtDisableLastKnownGood](../../page/83/NtDisableLastKnownGood_function_0083C560.md) at `0x0083C653`
- [SepAuditFailed](../../page/86/SepAuditFailed_function_0086EE20.md) at `0x0086EE9B`
- [ExpWnfAllocateNextPersistentNameSequence](../../page/8B/ExpWnfAllocateNextPersistentNameSequence_function_008BDE84.md) at `0x008BE08F`
- [ExpWnfRegisterPermanentName](../../page/8B/ExpWnfRegisterPermanentName_function_008BE17C.md) at `0x008BE275`
- [ExpWnfWriteStateData](../../page/90/ExpWnfWriteStateData_function_0090B7B0.md) at `0x0090BA34`
- [PopApplyPolicy](../../page/91/PopApplyPolicy_function_009107B0.md) at `0x00910A3F`
- [RegRtlSetValue](../../page/99/RegRtlSetValue_function_00991B28.md) at `0x00991B70`
- [PiDevCfgCopyDeviceKey](../../page/99/PiDevCfgCopyDeviceKey_function_00997374.md) at `0x00997623`
- [PiProcessDriverInstance](../../page/99/PiProcessDriverInstance_function_00998530.md) at `0x00998682`
- [PiProcessDriverInstance](../../page/99/PiProcessDriverInstance_function_00998530.md) at `0x009986CA`
- [PiProcessDriverInstance](../../page/99/PiProcessDriverInstance_function_00998530.md) at `0x009986FB`
- [PiRearrangeDeviceInstances](../../page/99/PiRearrangeDeviceInstances_function_0099AF9C.md) at `0x0099B11F`
- [IopUpdateSecureDeviceClassState](../../page/9A/IopUpdateSecureDeviceClassState_function_009A2CE8.md) at `0x009A2F11`
- [IopReleaseDeviceResources](../../page/A0/IopReleaseDeviceResources_function_00A0867C.md) at `0x00A087EA`
- [DrvDbSetDeviceIdDriverInfMatches](../../page/A6/DrvDbSetDeviceIdDriverInfMatches_function_00A6251C.md) at `0x00A62775`
- [RtlWriteRegistryValue](../../page/A6/RtlWriteRegistryValue_function_00A6C620.md) at `0x00A6C68F`
- [PopDiagTraceHiberStats](../../page/A7/PopDiagTraceHiberStats_function_00A72FB4.md) at `0x00A73150`
- [PopDiagTraceHiberStats](../../page/A7/PopDiagTraceHiberStats_function_00A72FB4.md) at `0x00A73273`
- [PopDiagTraceHiberStats](../../page/A7/PopDiagTraceHiberStats_function_00A72FB4.md) at `0x00A732A7`
- [PopDiagTraceHiberStats](../../page/A7/PopDiagTraceHiberStats_function_00A72FB4.md) at `0x00A73318`
- [PopDiagTraceHiberStats](../../page/A7/PopDiagTraceHiberStats_function_00A72FB4.md) at `0x00A73374`
- [CmpAddToHiveFileList](../../page/A8/CmpAddToHiveFileList_function_00A81914.md) at `0x00A819F5`
- [ExpSetPendingUILanguage](../../page/A8/ExpSetPendingUILanguage_function_00A87E70.md) at `0x00A880D5`
- [IopWriteAllocatedResourcesToRegistry](../../page/AA/IopWriteAllocatedResourcesToRegistry_function_00AA54E4.md) at `0x00AA5597`
- [NtSetDefaultLocale](../../page/AA/NtSetDefaultLocale_function_00AAE850.md) at `0x00AAEB30`
- [PnpDriverLoadingFailed](../../page/AB/PnpDriverLoadingFailed_function_00AB8928.md) at `0x00AB8A2F`
- [PnpDriverLoadingFailed](../../page/AB/PnpDriverLoadingFailed_function_00AB8928.md) at `0x00AB8CE7`
- [PnpDriverLoadingFailed](../../page/AB/PnpDriverLoadingFailed_function_00AB8928.md) at `0x00AB8D3C`
- [PnpDriverLoadingFailed](../../page/AB/PnpDriverLoadingFailed_function_00AB8928.md) at `0x00AB8D6E`
- [sub_00B1FB42](../../page/B1/Unknown_function_00B1FB42.md) at `0x00B1FC28`
- [sub_00B1FD92](../../page/B1/Unknown_function_00B1FD92.md) at `0x00B1FDF7`
- [sub_00B1FEC0](../../page/B1/Unknown_function_00B1FEC0.md) at `0x00B1FF15`
- [sub_00B2D22A](../../page/B2/Unknown_function_00B2D22A.md) at `0x00B2D447`
- [sub_00B2D22A](../../page/B2/Unknown_function_00B2D22A.md) at `0x00B2D48B`
- [sub_00B2D22A](../../page/B2/Unknown_function_00B2D22A.md) at `0x00B2D4C4`
- [sub_00B3FE90](../../page/B3/Unknown_function_00B3FE90.md) at `0x00B3FFAC`
- [sub_00B3FE90](../../page/B3/Unknown_function_00B3FE90.md) at `0x00B40046`
- [sub_00B44C1A](../../page/B4/Unknown_function_00B44C1A.md) at `0x00B44C6E`
- [sub_00B44C1A](../../page/B4/Unknown_function_00B44C1A.md) at `0x00B44DE2`
- [sub_00B44C1A](../../page/B4/Unknown_function_00B44C1A.md) at `0x00B450B9`
- [sub_00B46996](../../page/B4/Unknown_function_00B46996.md) at `0x00B46ADF`
- [BapdRegisterSiData](../../pagelk/B7/BapdRegisterSiData_function_00B7B5B8.md) at `0x00B7B676`
- [BapdRegisterSiData](../../pagelk/B7/BapdRegisterSiData_function_00B7B5B8.md) at `0x00B7B6AC`
- [BapdRegisterSiData](../../pagelk/B7/BapdRegisterSiData_function_00B7B5B8.md) at `0x00B7B6E6`
- [BapdRegisterSiData](../../pagelk/B7/BapdRegisterSiData_function_00B7B5B8.md) at `0x00B7B760`
- [BapdRegisterSiData](../../pagelk/B7/BapdRegisterSiData_function_00B7B5B8.md) at `0x00B7B798`
- [BapdRegisterSiData](../../pagelk/B7/BapdRegisterSiData_function_00B7B5B8.md) at `0x00B7B7D0`
- [BapdRegisterSiData](../../pagelk/B7/BapdRegisterSiData_function_00B7B5B8.md) at `0x00B7B81D`
- [BapdpWriteEventDataToRegistry](../../pagelk/B7/BapdpWriteEventDataToRegistry_function_00B7C1E8.md) at `0x00B7C30C`
- [sub_00B80DDC](../../pagelk/B8/Unknown_function_00B80DDC.md) at `0x00B80E0B`
- [sub_00B80DDC](../../pagelk/B8/Unknown_function_00B80DDC.md) at `0x00B80E37`
- [sub_00B80DDC](../../pagelk/B8/Unknown_function_00B80DDC.md) at `0x00B80E63`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC4CC4`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC4CFD`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC4D36`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC4D6F`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC4DA8`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC4DE1`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC4E1A`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC4E61`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC4EA8`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC4EEF`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC4F35`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC4F7C`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC4FC3`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC500A`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC5043`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC507C`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC50B5`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC50EE`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC5127`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC516E`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC51B5`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC51FC`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC5243`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC528A`
- [MfgInitSystem](../../init/C1/MfgInitSystem_function_00C1C390.md) at `0x00C1C5AD`
- [MfgInitSystem](../../init/C1/MfgInitSystem_function_00C1C390.md) at `0x00C1C6CD`
- [RegistryOverwriteCentralProcessor](../../init/C1/RegistryOverwriteCentralProcessor_function_00C1DB4C.md) at `0x00C1DCB3`
- [RegistryOverwriteCentralProcessor](../../init/C1/RegistryOverwriteCentralProcessor_function_00C1DB4C.md) at `0x00C1DCE2`
- [RegistryOverwriteCentralProcessor](../../init/C1/RegistryOverwriteCentralProcessor_function_00C1DB4C.md) at `0x00C1DD11`
- [ArbInitializeMmConfigRange](../../init/C2/ArbInitializeMmConfigRange_function_00C25E6C.md) at `0x00C25F66`
- [ArbInitializeOsInaccessibleRange](../../init/C2/ArbInitializeOsInaccessibleRange_function_00C25F9C.md) at `0x00C26118`
- [IopCachePreviousBootData](../../init/C2/IopCachePreviousBootData_function_00C2A790.md) at `0x00C2A82C`
- [PiInitFirmwareResources](../../init/C3/PiInitFirmwareResources_function_00C301C8.md) at `0x00C30314`
- [PiInitFirmwareResources](../../init/C3/PiInitFirmwareResources_function_00C301C8.md) at `0x00C3034B`
- [PiInitFirmwareResources](../../init/C3/PiInitFirmwareResources_function_00C301C8.md) at `0x00C30382`
- [PiInitFirmwareResources](../../init/C3/PiInitFirmwareResources_function_00C301C8.md) at `0x00C303B9`
- [PiInitFirmwareResources](../../init/C3/PiInitFirmwareResources_function_00C301C8.md) at `0x00C303F0`
- [PipCheckSystemFirmwareUpdated](../../init/C3/PipCheckSystemFirmwareUpdated_function_00C3048C.md) at `0x00C3058F`
- [PipCreateComputerId](../../init/C3/PipCreateComputerId_function_00C305F4.md) at `0x00C30756`
- [PipCreateComputerId](../../init/C3/PipCreateComputerId_function_00C305F4.md) at `0x00C307D5`
- [PipHardwareConfigInit](../../init/C3/PipHardwareConfigInit_function_00C30D24.md) at `0x00C30E7B`
- [PipHardwareConfigInit](../../init/C3/PipHardwareConfigInit_function_00C30D24.md) at `0x00C30FCE`
- [PipHardwareConfigInit](../../init/C3/PipHardwareConfigInit_function_00C30D24.md) at `0x00C31003`
- [PipHardwareConfigInit](../../init/C3/PipHardwareConfigInit_function_00C30D24.md) at `0x00C31070`
- [PipHardwareConfigInit](../../init/C3/PipHardwareConfigInit_function_00C30D24.md) at `0x00C31107`
- [PiLastGoodCopyKeyContents](../../init/C3/PiLastGoodCopyKeyContents_function_00C336E4.md) at `0x00C3384D`
- [SepSecureBootSetRegistryKey](../../init/C4/SepSecureBootSetRegistryKey_function_00C4B798.md) at `0x00C4B8C8`
- [SepSecureBootSetRegistryKey](../../init/C4/SepSecureBootSetRegistryKey_function_00C4B798.md) at `0x00C4B92D`
- [SepSecureBootSetRegistryKey](../../init/C4/SepSecureBootSetRegistryKey_function_00C4B798.md) at `0x00C4B95D`
- [BapdpProcessVsmKeyBlobs](../../init/C4/BapdpProcessVsmKeyBlobs_function_00C4FD60.md) at `0x00C4FF46`
- [BapdpRegisterBitlockerStatus](../../init/C5/BapdpRegisterBitlockerStatus_function_00C50528.md) at `0x00C50655`
- [BapdpRegisterEDrvHintInfo](../../init/C5/BapdpRegisterEDrvHintInfo_function_00C5067C.md) at `0x00C507B3`
- [BapdpRegisterFwUpdateResults](../../init/C5/BapdpRegisterFwUpdateResults_function_00C507E4.md) at `0x00C50962`
- [BapdpRegisterFwUpdateResults](../../init/C5/BapdpRegisterFwUpdateResults_function_00C507E4.md) at `0x00C50999`
- [BapdpRegisterResumeInformation](../../init/C5/BapdpRegisterResumeInformation_function_00C509F4.md) at `0x00C50B1C`
- [BapdpRegisterWmdResult](../../init/C5/BapdpRegisterWmdResult_function_00C50C58.md) at `0x00C50D77`
- [BapdpRegisterWmdResult](../../init/C5/BapdpRegisterWmdResult_function_00C50C58.md) at `0x00C50DB6`
- [CmpAddAliasEntry](../../init/C5/CmpAddAliasEntry_function_00C56584.md) at `0x00C5675D`
- [CmpCreateControlSet](../../init/C5/CmpCreateControlSet_function_00C56910.md) at `0x00C56AA7`
- [CmpCreateControlSet](../../init/C5/CmpCreateControlSet_function_00C56910.md) at `0x00C56C62`
- [CmpCreateHardwareProfiles](../../init/C5/CmpCreateHardwareProfiles_function_00C56EF4.md) at `0x00C571CB`
- [CmpCreateHardwareProfiles](../../init/C5/CmpCreateHardwareProfiles_function_00C56EF4.md) at `0x00C57401`
- [CmpCreateHardwareProfiles](../../init/C5/CmpCreateHardwareProfiles_function_00C56EF4.md) at `0x00C57593`
- [CmpCreateHardwareProfiles](../../init/C5/CmpCreateHardwareProfiles_function_00C56EF4.md) at `0x00C576B3`
- [CmpInitializeSystemBiosInformation](../../init/C5/CmpInitializeSystemBiosInformation_function_00C58620.md) at `0x00C58757`
- [CmpMigrateOOBELanguageToInstallationLanguage](../../init/C5/CmpMigrateOOBELanguageToInstallationLanguage_function_00C589A0.md) at `0x00C58A79`
- [CmpSetNetworkValue](../../init/C5/CmpSetNetworkValue_function_00C58AC4.md) at `0x00C58B54`
- [CmpSetNetworkValue](../../init/C5/CmpSetNetworkValue_function_00C58AC4.md) at `0x00C58B81`
- [CmpSetSystemValues](../../init/C5/CmpSetSystemValues_function_00C58BB0.md) at `0x00C58C77`
- [CmpSetSystemValues](../../init/C5/CmpSetSystemValues_function_00C58BB0.md) at `0x00C58D49`
- [CmpSetSystemValues](../../init/C5/CmpSetSystemValues_function_00C58BB0.md) at `0x00C58D8F`
- [CmpSetSystemValues](../../init/C5/CmpSetSystemValues_function_00C58BB0.md) at `0x00C58E1A`
- [CmpInitializeMachineDependentConfiguration](../../init/C5/CmpInitializeMachineDependentConfiguration_function_00C5A02C.md) at `0x00C5A185`
- [CmpInitializeMachineDependentConfiguration](../../init/C5/CmpInitializeMachineDependentConfiguration_function_00C5A02C.md) at `0x00C5A4EF`
- [CmpInitializeMachineDependentConfiguration](../../init/C5/CmpInitializeMachineDependentConfiguration_function_00C5A02C.md) at `0x00C5A52D`
- [CmpInitializeMachineDependentConfiguration](../../init/C5/CmpInitializeMachineDependentConfiguration_function_00C5A02C.md) at `0x00C5A56B`
- [CmpSetSystemBiosInformation](../../init/C5/CmpSetSystemBiosInformation_function_00C5A5D0.md) at `0x00C5A77E`
- [CmpSetSystemBiosInformation](../../init/C5/CmpSetSystemBiosInformation_function_00C5A5D0.md) at `0x00C5A811`
- [CmpSetSystemBiosInformation](../../init/C5/CmpSetSystemBiosInformation_function_00C5A5D0.md) at `0x00C5A920`
- [CmpSetVideoBiosInformation](../../init/C5/CmpSetVideoBiosInformation_function_00C5A970.md) at `0x00C5AB2E`
- [CmpSetVideoBiosInformation](../../init/C5/CmpSetVideoBiosInformation_function_00C5A970.md) at `0x00C5AC0E`
- [SaveNodeDistanceInformation](../../init/C6/SaveNodeDistanceInformation_function_00C6FE60.md) at `0x00C70346`
- [PipInitComputerIds](../../init/C7/PipInitComputerIds_function_00C74734.md) at `0x00C74CC8`
- [PipInitComputerIds](../../init/C7/PipInitComputerIds_function_00C74734.md) at `0x00C74D95`

### Static image references
- `0x006ADCDC` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006ADCE9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006ADCD0  48 8B C4                        mov rax, rsp
006ADCD3  FA                              cli
006ADCD4  48 83 EC 10                     sub rsp, 0x10
006ADCD8  50                              push rax
006ADCD9  9C                              pushfq
006ADCDA  6A 10                           push 0x10
006ADCDC  48 8D 05 7D 57 00 00            lea rax, [rip + 0x577d]
006ADCE3  50                              push rax
006ADCE4  B8 60 00 00 00                  mov eax, 0x60
006ADCE9  E9 D2 6C 01 00                  jmp 0x1406c49c0
006ADCEE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwSetValueKey(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwSetValueKey(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006ADCD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006ADCD0[BB_006ADCD0]
  bb_006ADCEE[BB_006ADCEE]
```
