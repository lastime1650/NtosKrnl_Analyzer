# ZwQueryValueKey

- RVA: `0x006AD3B0`–`0x006AD3CF` (길이 `31` bytes)
- VA: `0x00000001406AD3B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFFA4`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **133**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [BiZwQueryValueKey](../4A/BiZwQueryValueKey_function_004A8184.md) at `0x004A81A0`
- [PopQueryPowerButtonConfiguration](../4C/PopQueryPowerButtonConfiguration_function_004CA6EC.md) at `0x004CA808`
- [PopQueryPowerButtonConfiguration](../4C/PopQueryPowerButtonConfiguration_function_004CA6EC.md) at `0x004CA861`
- [PopQueryPowerButtonConfiguration](../4C/PopQueryPowerButtonConfiguration_function_004CA6EC.md) at `0x004CA902`
- [PopQueryPowerButtonConfiguration](../4C/PopQueryPowerButtonConfiguration_function_004CA6EC.md) at `0x004CA95E`
- [HalpMcaExtendedLogGetL1DirectoryBase](../54/HalpMcaExtendedLogGetL1DirectoryBase_function_00541520.md) at `0x005415E7`
- [CcCheckContainerWaitForRestore](../57/CcCheckContainerWaitForRestore_function_0057AEE4.md) at `0x0057AF95`
- [CcQueryRegKeyValue](../57/CcQueryRegKeyValue_function_0057CACC.md) at `0x0057CB72`
- [FsRtlpGetMaxVirtualDiskNestingLevel](../58/FsRtlpGetMaxVirtualDiskNestingLevel_function_00582FDC.md) at `0x005830C3`
- [IopInitializeSystemVariableService](../5A/IopInitializeSystemVariableService_function_005A0310.md) at `0x005A03D3`
- [PipIs32bitKey](../5A/PipIs32bitKey_function_005A45F0.md) at `0x005A4676`
- [PnpRegistryValueExists](../5A/PnpRegistryValueExists_function_005A81A0.md) at `0x005A81DD`
- [KeCommitSmtState](../5B/KeCommitSmtState_function_005BE7AC.md) at `0x005BE85B`
- [PpmInitIllegalThrottleLogging](../5C/PpmInitIllegalThrottleLogging_function_005CE39C.md) at `0x005CE416`
- [PopReadShutdownPolicy](../5C/PopReadShutdownPolicy_function_005CEA64.md) at `0x005CEB1C`
- [PopLidReliabilityInit](../5D/PopLidReliabilityInit_function_005D5308.md) at `0x005D5382`
- [RtlpGetBootStatusPathFromRegistry](../5E/RtlpGetBootStatusPathFromRegistry_function_005E7A68.md) at `0x005E7B13`
- [RtlpGetBootStatusPathFromRegistry](../5E/RtlpGetBootStatusPathFromRegistry_function_005E7A68.md) at `0x005E7B78`
- [RtlQueryValidationRunlevel](../5E/RtlQueryValidationRunlevel_function_005EE220.md) at `0x005EE2A9`
- [DifZwQueryValueKeyWrapper](../64/DifZwQueryValueKeyWrapper_function_00648A50.md) at `0x00648B63`
- [MigrateOOBELanguageToInstallationLanguage](../65/MigrateOOBELanguageToInstallationLanguage_function_0065CEA8.md) at `0x0065CFD3`
- [OpenGlobalizationUserSettingsKey_ForSingleUserModel](../65/OpenGlobalizationUserSettingsKey_ForSingleUserModel_function_0065D368.md) at `0x0065D41C`
- [OpenGlobalizationUserSettingsKey_ForSingleUserModel](../65/OpenGlobalizationUserSettingsKey_ForSingleUserModel_function_0065D368.md) at `0x0065D47B`
- [WheaPersistBadPageToRegistry](../65/WheaPersistBadPageToRegistry_function_0065F58C.md) at `0x0065F671`
- [WheaPersistBadPageToRegistry](../65/WheaPersistBadPageToRegistry_function_0065F58C.md) at `0x0065F6E6`
- [sub_006FBC78](../6F/Unknown_function_006FBC78.md) at `0x006FBC9F`
- [sub_006FBC78](../6F/Unknown_function_006FBC78.md) at `0x006FBCF3`
- [ArbpGetRegistryValue](../../page/71/ArbpGetRegistryValue_function_00710124.md) at `0x0071016C`
- [ArbpGetRegistryValue](../../page/71/ArbpGetRegistryValue_function_00710124.md) at `0x007101CC`
- [DbgkpLkmdSqmIsOptedIn](../../page/71/DbgkpLkmdSqmIsOptedIn_function_00711C4C.md) at `0x00711D19`
- [DbgkpLkmdSqmIsOptedIn](../../page/71/DbgkpLkmdSqmIsOptedIn_function_00711C4C.md) at `0x00711DA4`
- [DbgkpWerIsFullLiveDumpDisabled](../../page/71/DbgkpWerIsFullLiveDumpDisabled_function_00712470.md) at `0x00712527`
- [FsRtlGetTunnelParameterValue](../../page/71/FsRtlGetTunnelParameterValue_function_00713FA8.md) at `0x00714064`
- [FsRtlpOplockGetAckTimeoutOverride](../../page/71/FsRtlpOplockGetAckTimeoutOverride_function_00714F54.md) at `0x00715019`
- [FsRtlpDedupChangeQueryValueKey](../../page/71/FsRtlpDedupChangeQueryValueKey_function_00715E34.md) at `0x00715EDA`
- [FsRtlpQueryValueKey](../../page/71/FsRtlpQueryValueKey_function_00716BA0.md) at `0x00716C46`
- [IopSymlinkQueryEnabledClasses](../../page/71/IopSymlinkQueryEnabledClasses_function_0071EF6C.md) at `0x0071F078`
- [PipCheckComputerSupported](../../page/72/PipCheckComputerSupported_function_007232B0.md) at `0x00723364`
- [PnprGetPluginDriverImagePath](../../page/73/PnprGetPluginDriverImagePath_function_007398E8.md) at `0x007399CA`
- [PnprGetPluginDriverImagePath](../../page/73/PnprGetPluginDriverImagePath_function_007398E8.md) at `0x00739A36`
- [KsepRegistryQueryDWORD](../../page/74/KsepRegistryQueryDWORD_function_0074B348.md) at `0x0074B456`
- [KsepRegistryQuerySZ](../../page/74/KsepRegistryQuerySZ_function_0074B58C.md) at `0x0074B6EB`
- [KsepRegistryQuerySZ](../../page/74/KsepRegistryQuerySZ_function_0074B58C.md) at `0x0074B78C`
- [KsepRegistryQueryValue](../../page/74/KsepRegistryQueryValue_function_0074B7F8.md) at `0x0074B957`
- [KsepRegistryQueryValue](../../page/74/KsepRegistryQueryValue_function_0074B7F8.md) at `0x0074B9F8`
- [PfpGetParameter](../../page/75/PfpGetParameter_function_00752E80.md) at `0x00752EFD`
- [PoGetLightestSystemStateForEject](../../page/75/PoGetLightestSystemStateForEject_function_00753E30.md) at `0x00753EF4`
- [PopUpdateDeviceFamily](../../page/75/PopUpdateDeviceFamily_function_007546D0.md) at `0x007547AB`
- [PopUpdateUpgradeInProgress](../../page/75/PopUpdateUpgradeInProgress_function_00754880.md) at `0x0075494E`
- [PopDirectedDripsQueryRegistryValues](../../page/75/PopDirectedDripsQueryRegistryValues_function_00757B40.md) at `0x00757C7E`
- [PopQueryHiberPersistedRegValue](../../page/75/PopQueryHiberPersistedRegValue_function_0075DDFC.md) at `0x0075DEB1`
- [PopThermalHandlePreviousShutdown](../../page/75/PopThermalHandlePreviousShutdown_function_0075F400.md) at `0x0075F4EE`
- [PopThermalHandlePreviousShutdown](../../page/75/PopThermalHandlePreviousShutdown_function_0075F400.md) at `0x0075F52D`
- [PopThermalHandlePreviousShutdown](../../page/75/PopThermalHandlePreviousShutdown_function_0075F400.md) at `0x0075F570`
- [PopThermalHandlePreviousShutdown](../../page/75/PopThermalHandlePreviousShutdown_function_0075F400.md) at `0x0075F5C3`
- [PopThermalHandlePreviousShutdown](../../page/75/PopThermalHandlePreviousShutdown_function_0075F400.md) at `0x0075F610`
- [PopBatteryTestExemptPolicyRegKeyAccess](../../page/76/PopBatteryTestExemptPolicyRegKeyAccess_function_00766E04.md) at `0x00766EB1`
- [TtmpGetConfigOverride](../../page/77/TtmpGetConfigOverride_function_007765F8.md) at `0x007766BF`
- [PsBootPhaseComplete](../../page/77/PsBootPhaseComplete_function_0077EA18.md) at `0x0077EBC2`
- [PsBootPhaseComplete](../../page/77/PsBootPhaseComplete_function_0077EA18.md) at `0x0077EC6A`
- [PsBootPhaseComplete](../../page/77/PsBootPhaseComplete_function_0077EA18.md) at `0x0077ECD7`
- [RtlpQueryNlsSystemCodePages](../../page/78/RtlpQueryNlsSystemCodePages_function_0078C33C.md) at `0x0078C41B`
- [RtlpQueryNlsSystemCodePages](../../page/78/RtlpQueryNlsSystemCodePages_function_0078C33C.md) at `0x0078C48B`
- [LdrpQueryValueKey](../../page/79/LdrpQueryValueKey_function_007919D0.md) at `0x00791A69`
- [RtlOsDeploymentState](../../page/79/RtlOsDeploymentState_function_00794770.md) at `0x00794857`
- [SepRmFetchGlobalSacl](../../page/7A/SepRmFetchGlobalSacl_function_007A298C.md) at `0x007A2A47`
- [SepRmFetchGlobalSacl](../../page/7A/SepRmFetchGlobalSacl_function_007A298C.md) at `0x007A2AC8`
- [SepReadAndPopulateCapes](../../page/7A/SepReadAndPopulateCapes_function_007A3CB8.md) at `0x007A3F36`
- [SepReadAndPopulateCapes](../../page/7A/SepReadAndPopulateCapes_function_007A3CB8.md) at `0x007A3F74`
- [SepReadAndPopulateCapes](../../page/7A/SepReadAndPopulateCapes_function_007A3CB8.md) at `0x007A3FAD`
- [SepReadAndPopulateCapes](../../page/7A/SepReadAndPopulateCapes_function_007A3CB8.md) at `0x007A3FEC`
- [SepReadAndPopulateCapes](../../page/7A/SepReadAndPopulateCapes_function_007A3CB8.md) at `0x007A40E8`
- [SepReadAndPopulateCapes](../../page/7A/SepReadAndPopulateCapes_function_007A3CB8.md) at `0x007A4137`
- [SepReadAndPopulateCapes](../../page/7A/SepReadAndPopulateCapes_function_007A3CB8.md) at `0x007A41AF`
- [SepReadAndPopulateCapes](../../page/7A/SepReadAndPopulateCapes_function_007A3CB8.md) at `0x007A4225`
- [SepReadAndPopulateCapes](../../page/7A/SepReadAndPopulateCapes_function_007A3CB8.md) at `0x007A42A0`
- [SepReadSingleCap](../../page/7A/SepReadSingleCap_function_007A43E4.md) at `0x007A4458`
- [SepReadSingleCap](../../page/7A/SepReadSingleCap_function_007A43E4.md) at `0x007A4495`
- [SepReadSingleCap](../../page/7A/SepReadSingleCap_function_007A43E4.md) at `0x007A44D0`
- [SepReadSingleCap](../../page/7A/SepReadSingleCap_function_007A43E4.md) at `0x007A452A`
- [SepReadSingleCap](../../page/7A/SepReadSingleCap_function_007A43E4.md) at `0x007A456D`
- [SepReadSingleCap](../../page/7A/SepReadSingleCap_function_007A43E4.md) at `0x007A45E7`
- [SepReadSingleCap](../../page/7A/SepReadSingleCap_function_007A43E4.md) at `0x007A4636`
- [SmKmKeyGenLoadKey](../../page/7A/SmKmKeyGenLoadKey_function_007A8814.md) at `0x007A8915`
- [WdipSemQueryValueFromRegistry](../../page/7B/WdipSemQueryValueFromRegistry_function_007B185C.md) at `0x007B18F4`
- [IoWMISuggestInstanceName](../../page/7B/IoWMISuggestInstanceName_function_007B2520.md) at `0x007B263A`
- [IoWMISuggestInstanceName](../../page/7B/IoWMISuggestInstanceName_function_007B2520.md) at `0x007B2690`
- [ExpInitFullProcessSecurityInfo](../../page/7C/ExpInitFullProcessSecurityInfo_function_007C43D0.md) at `0x007C447D`
- [ExpReadLeapSecondData](../../page/7C/ExpReadLeapSecondData_function_007C5EAC.md) at `0x007C600C`
- [ExpReadLeapSecondData](../../page/7C/ExpReadLeapSecondData_function_007C5EAC.md) at `0x007C6051`
- [ExpReadLeapSecondData](../../page/7C/ExpReadLeapSecondData_function_007C5EAC.md) at `0x007C609B`
- [ExpOsProductCacheProviderHelper](../../page/7C/ExpOsProductCacheProviderHelper_function_007C8A58.md) at `0x007C8ABF`
- [ExpOsProductCacheProviderHelper](../../page/7C/ExpOsProductCacheProviderHelper_function_007C8A58.md) at `0x007C8B23`
- [ExpUuidLoadSequenceNumber](../../page/7D/ExpUuidLoadSequenceNumber_function_007D0B18.md) at `0x007D0C22`
- [KitpReadUlongFromKey](../../page/7D/KitpReadUlongFromKey_function_007D11D0.md) at `0x007D1221`
- [CMFRegisterEventTime](../../page/7D/CMFRegisterEventTime_function_007D382C.md) at `0x007D3952`
- [CMFRegisterEventTime](../../page/7D/CMFRegisterEventTime_function_007D382C.md) at `0x007D39CE`
- [ExpGetOriginalImageVersionRegistryValue](../../page/7D/ExpGetOriginalImageVersionRegistryValue_function_007D58B8.md) at `0x007D5981`
- [WheapScanRegistryForPolicyChanges](../../page/7D/WheapScanRegistryForPolicyChanges_function_007D8D58.md) at `0x007D8DCD`
- [ApiSetpLoadSchemaExtension](../../page/7D/ApiSetpLoadSchemaExtension_function_007D9A0C.md) at `0x007D9A8C`
- [CmpInterlockedFunction](../../page/7D/CmpInterlockedFunction_function_007DAD70.md) at `0x007DAE6D`
- [CmSetAcpiHwProfile](../../page/7E/CmSetAcpiHwProfile_function_007E2584.md) at `0x007E279F`
- [CmSetAcpiHwProfile](../../page/7E/CmSetAcpiHwProfile_function_007E2584.md) at `0x007E27F0`
- [CmSetAcpiHwProfile](../../page/7E/CmSetAcpiHwProfile_function_007E2584.md) at `0x007E286A`
- [CmpCloneHwProfile](../../page/7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E3472`
- [CmpCreateHwProfileFriendlyName](../../page/7E/CmpCreateHwProfileFriendlyName_function_007E3840.md) at `0x007E3A05`
- [CmpGetAcpiProfileInformation](../../page/7E/CmpGetAcpiProfileInformation_function_007E3D7C.md) at `0x007E3F9F`
- [CmpGetAcpiProfileInformation](../../page/7E/CmpGetAcpiProfileInformation_function_007E3D7C.md) at `0x007E3FEE`
- [CmpGetAcpiProfileInformation](../../page/7E/CmpGetAcpiProfileInformation_function_007E3D7C.md) at `0x007E40AC`
- [CmpGetAcpiProfileInformation](../../page/7E/CmpGetAcpiProfileInformation_function_007E3D7C.md) at `0x007E4101`
- [CmpGetAcpiProfileInformation](../../page/7E/CmpGetAcpiProfileInformation_function_007E3D7C.md) at `0x007E435F`
- [CmpGetAcpiProfileInformation](../../page/7E/CmpGetAcpiProfileInformation_function_007E3D7C.md) at `0x007E43C2`
- [CmpGetAcpiProfileInformation](../../page/7E/CmpGetAcpiProfileInformation_function_007E3D7C.md) at `0x007E441A`
- [CmpMoveBiosAliasTable](../../page/7E/CmpMoveBiosAliasTable_function_007E4578.md) at `0x007E4625`
- [CmpMoveBiosAliasTable](../../page/7E/CmpMoveBiosAliasTable_function_007E4578.md) at `0x007E4677`
- [CmpMoveBiosAliasTable](../../page/7E/CmpMoveBiosAliasTable_function_007E4578.md) at `0x007E47FB`
- [CmpMoveBiosAliasTable](../../page/7E/CmpMoveBiosAliasTable_function_007E4578.md) at `0x007E4868`
- [CmpMoveBiosAliasTable](../../page/7E/CmpMoveBiosAliasTable_function_007E4578.md) at `0x007E48C0`
- [CmpMoveBiosAliasTable](../../page/7E/CmpMoveBiosAliasTable_function_007E4578.md) at `0x007E4A21`
- [CmpReadBuildVersion](../../page/7E/CmpReadBuildVersion_function_007E52F4.md) at `0x007E53C8`
- [CmpReadBuildVersion](../../page/7E/CmpReadBuildVersion_function_007E52F4.md) at `0x007E5423`
- [CmpReadBuildVersion](../../page/7E/CmpReadBuildVersion_function_007E52F4.md) at `0x007E5491`
- [CmpQueryLayerVersionString](../../page/7E/CmpQueryLayerVersionString_function_007E7480.md) at `0x007E7512`
- [CmpQueryLayerVersionUlong](../../page/7E/CmpQueryLayerVersionUlong_function_007E75B4.md) at `0x007E7633`
- [MmZeroPageFileAtShutdown](../../page/7F/MmZeroPageFileAtShutdown_function_007F9164.md) at `0x007F920F`
- [SdbpCheckMatchingRegistryValue](../../page/81/SdbpCheckMatchingRegistryValue_function_0081462C.md) at `0x008146D5`
- [SdbpCheckMatchingRegistryValue](../../page/81/SdbpCheckMatchingRegistryValue_function_0081462C.md) at `0x00814742`
- [AslRegistryGetString](../../page/81/AslRegistryGetString_function_0081A084.md) at `0x0081A0D5`
- [AslRegistryGetString](../../page/81/AslRegistryGetString_function_0081A084.md) at `0x0081A17D`
- [AslRegistryGetUInt32_UStr](../../page/81/AslRegistryGetUInt32_UStr_function_0081A2A8.md) at `0x0081A300`
- [RtlpMuiRegPopulateBaseLanguages](../../page/83/RtlpMuiRegPopulateBaseLanguages_function_0083FC4C.md) at `0x0083FDD8`
- [RtlpMuiRegPopulateBaseLanguages](../../page/83/RtlpMuiRegPopulateBaseLanguages_function_0083FC4C.md) at `0x0083FEEC`
- [ExpWnfLookupPermanentName](../../page/8B/ExpWnfLookupPermanentName_function_008BD914.md) at `0x008BD9C9`
- [ExpWnfAllocateNextPersistentNameSequence](../../page/8B/ExpWnfAllocateNextPersistentNameSequence_function_008BDE84.md) at `0x008BDF77`
- [ExpWnfPopulateStateData](../../page/8B/ExpWnfPopulateStateData_function_008BF354.md) at `0x008BF4F5`
- [EtwpGetGuidSecurityDescriptor](../../page/8C/EtwpGetGuidSecurityDescriptor_function_008C05D4.md) at `0x008C06B3`
- [EtwpGetGuidSecurityDescriptor](../../page/8C/EtwpGetGuidSecurityDescriptor_function_008C05D4.md) at `0x008C07E9`
- [RtlpQueryRegistryValues](../../page/8C/RtlpQueryRegistryValues_function_008C9050.md) at `0x008C91AA`
- [PnpRegQueryValueIndirect](../../page/8E/PnpRegQueryValueIndirect_function_008EE210.md) at `0x008EE323`
- [PopEnableHiberFile](../../page/90/PopEnableHiberFile_function_0090F850.md) at `0x0090FAA8`
- [PopEnableHiberFile](../../page/90/PopEnableHiberFile_function_0090F850.md) at `0x0090FB15`
- [PopEnableHiberFile](../../page/90/PopEnableHiberFile_function_0090F850.md) at `0x0090FB71`
- [PopResetCurrentPolicies](../../page/90/PopResetCurrentPolicies_function_0090FF64.md) at `0x0090FFED`
- [DrvDbGetRegValueMappedProperty](../../page/92/DrvDbGetRegValueMappedProperty_function_0092FB80.md) at `0x0092FC5B`
- [PnpCtxRegQueryValue](../../page/99/PnpCtxRegQueryValue_function_009940FC.md) at `0x009941C4`
- [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) at `0x009991AA`
- [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) at `0x00999223`
- [PiFindDevInstMatch](../../page/99/PiFindDevInstMatch_function_009996A0.md) at `0x009997F0`
- [EtwpCapturePreviousRegistryData](../../page/99/EtwpCapturePreviousRegistryData_function_0099D3EC.md) at `0x0099D4AB`
- [sub_009DD363](../../page/9D/Unknown_function_009DD363.md) at `0x009DD3DB`
- [RtlQueryRegistryValueWithFallback](../../page/9F/RtlQueryRegistryValueWithFallback_function_009F7780.md) at `0x009F7814`
- [RtlQueryRegistryValueWithFallback](../../page/9F/RtlQueryRegistryValueWithFallback_function_009F7780.md) at `0x009F78C5`
- [RtlpInitNlsFileName](../../page/A1/RtlpInitNlsFileName_function_00A19B9C.md) at `0x00A19CC0`
- [RtlCapabilityCheck](../../page/A2/RtlCapabilityCheck_function_00A20340.md) at `0x00A20483`
- [RtlQueryImageFileKeyOption](../../page/A2/RtlQueryImageFileKeyOption_function_00A2D110.md) at `0x00A2D197`
- [RtlQueryImageFileKeyOption](../../page/A2/RtlQueryImageFileKeyOption_function_00A2D110.md) at `0x00A2D217`
- [PopConfigureHeteroPolicies](../../page/A3/PopConfigureHeteroPolicies_function_00A35B30.md) at `0x00A36166`
- [SiGetRegistryValue](../../page/A3/SiGetRegistryValue_function_00A37D8C.md) at `0x00A37E14`
- [SiGetRegistryValue](../../page/A3/SiGetRegistryValue_function_00A37D8C.md) at `0x00A37E65`
- [SepRegQueryValue](../../page/A3/SepRegQueryValue_function_00A3A730.md) at `0x00A3A79F`
- [RtlpProcessIFEOKeyFilter](../../page/A3/RtlpProcessIFEOKeyFilter_function_00A3BA78.md) at `0x00A3BB19`
- [RtlpProcessIFEOKeyFilter](../../page/A3/RtlpProcessIFEOKeyFilter_function_00A3BA78.md) at `0x00A3BCE3`
- [KGetUnlockSetting](../../page/A6/KGetUnlockSetting_function_00A691BC.md) at `0x00A6924E`
- [PipMakeGloballyUniqueId](../../page/A6/PipMakeGloballyUniqueId_function_00A6F428.md) at `0x00A6F522`
- [PipMakeGloballyUniqueId](../../page/A6/PipMakeGloballyUniqueId_function_00A6F428.md) at `0x00A6F58B`
- [ExpSetPendingUILanguage](../../page/A8/ExpSetPendingUILanguage_function_00A87E70.md) at `0x00A87FA7`
- [ExpSetPendingUILanguage](../../page/A8/ExpSetPendingUILanguage_function_00A87E70.md) at `0x00A8806D`
- [PopReadSystemAwayModePolicy](../../page/A9/PopReadSystemAwayModePolicy_function_00A9D368.md) at `0x00A9D406`
- [PopInitializePowerPolicySimulate](../../page/A9/PopInitializePowerPolicySimulate_function_00A9DA28.md) at `0x00A9DB7A`
- [PopInitializePowerPolicySimulate](../../page/A9/PopInitializePowerPolicySimulate_function_00A9DA28.md) at `0x00A9DBB2`
- [RtlpGetNtProductTypeFromRegistry](../../page/AA/RtlpGetNtProductTypeFromRegistry_function_00AA26D8.md) at `0x00AA27DE`
- [NtSetDefaultLocale](../../page/AA/NtSetDefaultLocale_function_00AAE850.md) at `0x00AAE99F`
- [ExpReadComPlusPackage](../../page/AB/ExpReadComPlusPackage_function_00AB78D4.md) at `0x00AB7946`
- [PerfDiagpIsTracingAllowed](../../page/AD/PerfDiagpIsTracingAllowed_function_00AD06C0.md) at `0x00AD0781`
- [PopLoadResumeContext](../../page/AD/PopLoadResumeContext_function_00AD1C0C.md) at `0x00AD1C7C`
- [PopLoadResumeContext](../../page/AD/PopLoadResumeContext_function_00AD1C0C.md) at `0x00AD1CCD`
- [PopIsRemoteDesktopEnabled](../../page/AD/PopIsRemoteDesktopEnabled_function_00AD6E64.md) at `0x00AD6F29`
- [sub_00B17EE2](../../page/B1/Unknown_function_00B17EE2.md) at `0x00B17FA0`
- [sub_00B1B202](../../page/B1/Unknown_function_00B1B202.md) at `0x00B1B26C`
- [sub_00B38904](../../page/B3/Unknown_function_00B38904.md) at `0x00B38B31`
- [sub_00B3C4A0](../../page/B3/Unknown_function_00B3C4A0.md) at `0x00B3C4CC`
- [sub_00B3C4A0](../../page/B3/Unknown_function_00B3C4A0.md) at `0x00B3C51C`
- [sub_00B3EB8C](../../page/B3/Unknown_function_00B3EB8C.md) at `0x00B3EC49`
- [sub_00B3FE90](../../page/B3/Unknown_function_00B3FE90.md) at `0x00B3FF6E`
- [sub_00B4442A](../../page/B4/Unknown_function_00B4442A.md) at `0x00B4445F`
- [sub_00B44C1A](../../page/B4/Unknown_function_00B44C1A.md) at `0x00B44D42`
- [sub_00B47552](../../page/B4/Unknown_function_00B47552.md) at `0x00B47591`
- [sub_00B475B2](../../page/B4/Unknown_function_00B475B2.md) at `0x00B475F1`
- [PopGetBitlockerKeyLocation](../../pagelk/B6/PopGetBitlockerKeyLocation_function_00B6BBFC.md) at `0x00B6BCD0`
- [PopGetBitlockerKeyLocation](../../pagelk/B6/PopGetBitlockerKeyLocation_function_00B6BBFC.md) at `0x00B6BD45`
- [HalpPiix4Detect](../../pagelk/B7/HalpPiix4Detect_function_00B79E00.md) at `0x00B7A3DD`
- [HalpDmaFinalizeDoubleBufferingDisposition](../../init/C1/HalpDmaFinalizeDoubleBufferingDisposition_function_00C1E354.md) at `0x00C1E413`
- [HalpDmaFinalizeDoubleBufferingDisposition](../../init/C1/HalpDmaFinalizeDoubleBufferingDisposition_function_00C1E354.md) at `0x00C1E46B`
- [FsRtlGetCompatibilityModeValue](../../init/C2/FsRtlGetCompatibilityModeValue_function_00C28D84.md) at `0x00C28E40`
- [KiInitializeReservedCpuSets](../../init/C3/KiInitializeReservedCpuSets_function_00C39DAC.md) at `0x00C39EA2`
- [PopReadLegacySimulatedArchitecturalClasses](../../init/C4/PopReadLegacySimulatedArchitecturalClasses_function_00C41138.md) at `0x00C411E7`
- [PopReadSimulatedProcessorClass](../../init/C4/PopReadSimulatedProcessorClass_function_00C41978.md) at `0x00C41A77`
- [SepSecureBootCheckForUpdates](../../init/C4/SepSecureBootCheckForUpdates_function_00C4B688.md) at `0x00C4B71B`
- [BapdpProcessVsmKeyBlobs](../../init/C4/BapdpProcessVsmKeyBlobs_function_00C4FD60.md) at `0x00C4FF99`
- [BapdpProcessVsmKeyBlobs](../../init/C4/BapdpProcessVsmKeyBlobs_function_00C4FD60.md) at `0x00C4FFF2`
- [CmpCreateControlSet](../../init/C5/CmpCreateControlSet_function_00C56910.md) at `0x00C56B92`
- [CmpCreateHardwareProfiles](../../init/C5/CmpCreateHardwareProfiles_function_00C56EF4.md) at `0x00C57207`
- [CmpSetSystemValues](../../init/C5/CmpSetSystemValues_function_00C58BB0.md) at `0x00C58DD6`
- [CmpGetRegistryValue](../../init/C5/CmpGetRegistryValue_function_00C5D860.md) at `0x00C5D8A8`
- [CmpGetRegistryValue](../../init/C5/CmpGetRegistryValue_function_00C5D860.md) at `0x00C5D905`
- [QueryRegistryHideMachine](../../init/C6/QueryRegistryHideMachine_function_00C6FC84.md) at `0x00C6FD44`
- [QueryRegistryHideMachine](../../init/C6/QueryRegistryHideMachine_function_00C6FC84.md) at `0x00C6FD89`
- [SaveNodeDistanceInformation](../../init/C6/SaveNodeDistanceInformation_function_00C6FE60.md) at `0x00C7024B`

### Static image references
- `0x006AD3BC` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD3C9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD3B0  48 8B C4                        mov rax, rsp
006AD3B3  FA                              cli
006AD3B4  48 83 EC 10                     sub rsp, 0x10
006AD3B8  50                              push rax
006AD3B9  9C                              pushfq
006AD3BA  6A 10                           push 0x10
006AD3BC  48 8D 05 9D 60 00 00            lea rax, [rip + 0x609d]
006AD3C3  50                              push rax
006AD3C4  B8 17 00 00 00                  mov eax, 0x17
006AD3C9  E9 F2 75 01 00                  jmp 0x1406c49c0
006AD3CE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwQueryValueKey(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwQueryValueKey(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD3B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD3B0[BB_006AD3B0]
  bb_006AD3CE[BB_006AD3CE]
```
