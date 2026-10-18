# ZwOpenKey

- RVA: `0x006AD310`–`0x006AD32F` (길이 `31` bytes)
- VA: `0x00000001406AD310`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFF68`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **214**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [BiZwOpenKey](../4A/BiZwOpenKey_function_004AF654.md) at `0x004AF658`
- [PiDevCfgPushCopyKeyEntry](../4A/PiDevCfgPushCopyKeyEntry_function_004AFBA4.md) at `0x004AFC91`
- [PiDevCfgPushCopyKeyEntry](../4A/PiDevCfgPushCopyKeyEntry_function_004AFBA4.md) at `0x004AFCD7`
- [PopOpenKey](../4B/PopOpenKey_function_004B4330.md) at `0x004B4397`
- [PopReadRegKeyValue](../4B/PopReadRegKeyValue_function_004B5F64.md) at `0x004B6000`
- [PrpWriteLogsToRegistry](../4C/PrpWriteLogsToRegistry_function_004CC288.md) at `0x004CC2E2`
- [HalpMcaExtendedLogGetL1DirectoryBase](../54/HalpMcaExtendedLogGetL1DirectoryBase_function_00541520.md) at `0x005415AB`
- [HalpMcEnumerateAndSetPatchConfig](../55/HalpMcEnumerateAndSetPatchConfig_function_0055AB38.md) at `0x0055ADAF`
- [HalpMcPatchConfiguration](../55/HalpMcPatchConfiguration_function_0055B184.md) at `0x0055B1E2`
- [CcCheckContainerWaitForRestore](../57/CcCheckContainerWaitForRestore_function_0057AEE4.md) at `0x0057AF69`
- [CcGetContainerPolicyForDTP](../57/CcGetContainerPolicyForDTP_function_0057B0D8.md) at `0x0057B13E`
- [CcOpenRegistryPath](../57/CcOpenRegistryPath_function_0057CA80.md) at `0x0057CAB9`
- [CcQueryRegKeyValue](../57/CcQueryRegKeyValue_function_0057CACC.md) at `0x0057CB2C`
- [FsRtlpGetMaxVirtualDiskNestingLevel](../58/FsRtlpGetMaxVirtualDiskNestingLevel_function_00582FDC.md) at `0x00583087`
- [IopInitializeSystemVariableService](../5A/IopInitializeSystemVariableService_function_005A0310.md) at `0x005A0397`
- [KiInitializeNormalPriorityAntiStarvationPolicies](../5B/KiInitializeNormalPriorityAntiStarvationPolicies_function_005B8178.md) at `0x005B81DC`
- [KeCommitSmtState](../5B/KeCommitSmtState_function_005BE7AC.md) at `0x005BE82B`
- [PopReadShutdownPolicy](../5C/PopReadShutdownPolicy_function_005CEA64.md) at `0x005CEAE0`
- [PspReadDfssConfigurationValues](../5E/PspReadDfssConfigurationValues_function_005E2508.md) at `0x005E2571`
- [RtlpGetBootStatusPathFromRegistry](../5E/RtlpGetBootStatusPathFromRegistry_function_005E7A68.md) at `0x005E7AD7`
- [RtlQueryValidationRunlevel](../5E/RtlQueryValidationRunlevel_function_005EE220.md) at `0x005EE280`
- [VfClearVerifierSettings](../61/VfClearVerifierSettings_function_00611DB0.md) at `0x00611E3D`
- [DifZwOpenKeyWrapper](../64/DifZwOpenKeyWrapper_function_00644080.md) at `0x00644163`
- [EtwpGetCurrentSiloMaxLoggers](../64/EtwpGetCurrentSiloMaxLoggers_function_0064E86C.md) at `0x0064E8D8`
- [EtwpQueryPartitionRegistryInformation](../64/EtwpQueryPartitionRegistryInformation_function_0064ECCC.md) at `0x0064ED87`
- [EtwpQuerySiloRegistrySettings](../64/EtwpQuerySiloRegistrySettings_function_0064EF78.md) at `0x0064EFF7`
- [BapdpMarshallBootDataToRegistry](../65/BapdpMarshallBootDataToRegistry_function_006548A8.md) at `0x00654A10`
- [ExpRecordShutdownTime](../65/ExpRecordShutdownTime_function_006555FC.md) at `0x00655674`
- [MigrateOOBELanguageToInstallationLanguage](../65/MigrateOOBELanguageToInstallationLanguage_function_0065CEA8.md) at `0x0065CF5B`
- [OpenGlobalizationUserSettingsKey_ForMua](../65/OpenGlobalizationUserSettingsKey_ForMua_function_0065D0C8.md) at `0x0065D2B7`
- [OpenGlobalizationUserSettingsKey_ForMua](../65/OpenGlobalizationUserSettingsKey_ForMua_function_0065D0C8.md) at `0x0065D2DD`
- [OpenRegistryKey](../65/OpenRegistryKey_function_0065D588.md) at `0x0065D5BF`
- [RtlpOpenBaseImageFileOptionsKeyEx](../../page/70/RtlpOpenBaseImageFileOptionsKeyEx_function_0070244C.md) at `0x007024BA`
- [PopOpenHiberPersistedKey](../../page/70/PopOpenHiberPersistedKey_function_007024E0.md) at `0x00702596`
- [HalpAddDevice](../../page/70/HalpAddDevice_function_00708060.md) at `0x0070823B`
- [HalpRecordSecondaryGsivRange](../../page/70/HalpRecordSecondaryGsivRange_function_0070A4F8.md) at `0x0070A599`
- [HalpRecordSecondaryGsivRange](../../page/70/HalpRecordSecondaryGsivRange_function_0070A4F8.md) at `0x0070A5DD`
- [HalpPutAcpiHacksInRegistry](../../page/70/HalpPutAcpiHacksInRegistry_function_0070BC04.md) at `0x0070BCE9`
- [ArbAddInaccessibleAllocationRange](../../page/70/ArbAddInaccessibleAllocationRange_function_0070DEB0.md) at `0x0070DF32`
- [ArbAddInaccessibleAllocationRange](../../page/70/ArbAddInaccessibleAllocationRange_function_0070DEB0.md) at `0x0070DF7C`
- [ArbBuildAssignmentOrdering](../../page/70/ArbBuildAssignmentOrdering_function_0070E43C.md) at `0x0070E54C`
- [ArbBuildAssignmentOrdering](../../page/70/ArbBuildAssignmentOrdering_function_0070E43C.md) at `0x0070E597`
- [ArbRegReadMmConfigRanges](../../page/70/ArbRegReadMmConfigRanges_function_0070F7AC.md) at `0x0070F81D`
- [ArbRegReadMmConfigRanges](../../page/70/ArbRegReadMmConfigRanges_function_0070F7AC.md) at `0x0070F86A`
- [DbgkpLkmdSqmIsOptedIn](../../page/71/DbgkpLkmdSqmIsOptedIn_function_00711C4C.md) at `0x00711CF3`
- [DbgkpLkmdSqmIsOptedIn](../../page/71/DbgkpLkmdSqmIsOptedIn_function_00711C4C.md) at `0x00711D7C`
- [DbgkpWerIsFullLiveDumpDisabled](../../page/71/DbgkpWerIsFullLiveDumpDisabled_function_00712470.md) at `0x007124FB`
- [FsRtlGetTunnelParameterValue](../../page/71/FsRtlGetTunnelParameterValue_function_00713FA8.md) at `0x0071402F`
- [FsRtlpOplockGetAckTimeoutOverride](../../page/71/FsRtlpOplockGetAckTimeoutOverride_function_00714F54.md) at `0x00714FDC`
- [FsRtlOpenFileSystemRegistryKeyFromFsGuid](../../page/71/FsRtlOpenFileSystemRegistryKeyFromFsGuid_function_00715980.md) at `0x00715ABB`
- [FsRtlpDedupChangeQueryValueKey](../../page/71/FsRtlpDedupChangeQueryValueKey_function_00715E34.md) at `0x00715E94`
- [FsRtlpQueryValueKey](../../page/71/FsRtlpQueryValueKey_function_00716BA0.md) at `0x00716C00`
- [PiCreateServiceKeyUnderPath](../../page/72/PiCreateServiceKeyUnderPath_function_00728DEC.md) at `0x00728F1F`
- [PiOpenDriverRedirectedStateRootKey](../../page/72/PiOpenDriverRedirectedStateRootKey_function_0072935C.md) at `0x007293EF`
- [PnprGetPluginDriverImagePath](../../page/73/PnprGetPluginDriverImagePath_function_007398E8.md) at `0x0073998C`
- [PiDrvDbSetupNodeHive](../../page/74/PiDrvDbSetupNodeHive_function_00743884.md) at `0x00743943`
- [PiDrvDbSetupNodeHive](../../page/74/PiDrvDbSetupNodeHive_function_00743884.md) at `0x00743A00`
- [PopUpdateDeviceFamily](../../page/75/PopUpdateDeviceFamily_function_007546D0.md) at `0x0075476B`
- [PopUpdateUpgradeInProgress](../../page/75/PopUpdateUpgradeInProgress_function_00754880.md) at `0x0075490E`
- [PopDirectedDripsQueryRegistryValues](../../page/75/PopDirectedDripsQueryRegistryValues_function_00757B40.md) at `0x00757BDD`
- [TtmpGetConfigOverride](../../page/77/TtmpGetConfigOverride_function_007765F8.md) at `0x00776687`
- [PsBootPhaseComplete](../../page/77/PsBootPhaseComplete_function_0077EA18.md) at `0x0077EB8F`
- [PsBootPhaseComplete](../../page/77/PsBootPhaseComplete_function_0077EA18.md) at `0x0077EC1F`
- [PspIsDfssEnabled](../../page/77/PspIsDfssEnabled_function_0077EFF4.md) at `0x0077F058`
- [RtlpQueryNlsSystemCodePages](../../page/78/RtlpQueryNlsSystemCodePages_function_0078C33C.md) at `0x0078C3CF`
- [RtlOpenCurrentUser](../../page/78/RtlOpenCurrentUser_function_0078F940.md) at `0x0078F9AF`
- [RtlOpenCurrentUser](../../page/78/RtlOpenCurrentUser_function_0078F940.md) at `0x0078FA03`
- [RtlpUpdateDynamicTimeZones](../../page/79/RtlpUpdateDynamicTimeZones_function_0079019C.md) at `0x007902E7`
- [RtlpUpdateDynamicTimeZones](../../page/79/RtlpUpdateDynamicTimeZones_function_0079019C.md) at `0x00790340`
- [LdrpOpenKey](../../page/79/LdrpOpenKey_function_00791984.md) at `0x007919BD`
- [RtlOsDeploymentState](../../page/79/RtlOsDeploymentState_function_00794770.md) at `0x0079480D`
- [SepLoadNgenLocations](../../page/79/SepLoadNgenLocations_function_0079BCCC.md) at `0x0079BD54`
- [SmKmKeyGenLoadKey](../../page/7A/SmKmKeyGenLoadKey_function_007A8814.md) at `0x007A889E`
- [WdipSemOpenRegistryKey](../../page/7B/WdipSemOpenRegistryKey_function_007B17C8.md) at `0x007B183D`
- [EtwpFindMatchingPmcRegistryGroup](../../page/7B/EtwpFindMatchingPmcRegistryGroup_function_007B644C.md) at `0x007B65D7`
- [EtwpLoadMicroarchitecturalPmcs](../../page/7B/EtwpLoadMicroarchitecturalPmcs_function_007B6D48.md) at `0x007B6E30`
- [EtwpLoadMicroarchitecturalPmcs](../../page/7B/EtwpLoadMicroarchitecturalPmcs_function_007B6D48.md) at `0x007B6EEA`
- [EtwpLoadMicroarchitecturalProfileGroup](../../page/7B/EtwpLoadMicroarchitecturalProfileGroup_function_007B6F74.md) at `0x007B7216`
- [EtwpRemoveMicroarchitecturalPmcFromPmcGroup](../../page/7B/EtwpRemoveMicroarchitecturalPmcFromPmcGroup_function_007B7844.md) at `0x007B7944`
- [EtwpRemoveMicroarchitecturalPmcFromPmcGroup](../../page/7B/EtwpRemoveMicroarchitecturalPmcFromPmcGroup_function_007B7844.md) at `0x007B7A14`
- [EtwStartAutoLogger](../../page/7B/EtwStartAutoLogger_function_007BD2F8.md) at `0x007BD40C`
- [EtwpEnumerateAutologgerPath](../../page/7B/EtwpEnumerateAutologgerPath_function_007BE398.md) at `0x007BE487`
- [ExpInitFullProcessSecurityInfo](../../page/7C/ExpInitFullProcessSecurityInfo_function_007C43D0.md) at `0x007C444E`
- [ExpUpdateComPlusPackage](../../page/7C/ExpUpdateComPlusPackage_function_007C5580.md) at `0x007C55A4`
- [ExpUuidLoadSequenceNumber](../../page/7D/ExpUuidLoadSequenceNumber_function_007D0B18.md) at `0x007D0BEF`
- [ExpUuidSaveSequenceNumber](../../page/7D/ExpUuidSaveSequenceNumber_function_007D0C84.md) at `0x007D0D5D`
- [KitpOpenRegKey](../../page/7D/KitpOpenRegKey_function_007D117C.md) at `0x007D11BC`
- [ExpGetOriginalImageVersionRegistryValue](../../page/7D/ExpGetOriginalImageVersionRegistryValue_function_007D58B8.md) at `0x007D5945`
- [ApiSetLoadSchemaWithExtensions](../../page/7D/ApiSetLoadSchemaWithExtensions_function_007D9810.md) at `0x007D98CB`
- [ApiSetpLoadSchemaExtensions](../../page/7D/ApiSetpLoadSchemaExtensions_function_007D9B28.md) at `0x007D9BEE`
- [CmpCreatePerfKeys](../../page/7D/CmpCreatePerfKeys_function_007D9F70.md) at `0x007D9FCB`
- [CmpInterlockedFunction](../../page/7D/CmpInterlockedFunction_function_007DAD70.md) at `0x007DADE3`
- [CmpInterlockedFunction](../../page/7D/CmpInterlockedFunction_function_007DAD70.md) at `0x007DAE22`
- [CmpMarkCurrentProfileDirty](../../page/7D/CmpMarkCurrentProfileDirty_function_007DBBAC.md) at `0x007DBC1C`
- [CmpOpenDevicesControlSet](../../page/7D/CmpOpenDevicesControlSet_function_007DC5B0.md) at `0x007DC680`
- [CmpOpenDevicesControlSet](../../page/7D/CmpOpenDevicesControlSet_function_007DC5B0.md) at `0x007DC6DF`
- [CmpSaveBootControlSet](../../page/7D/CmpSaveBootControlSet_function_007DC744.md) at `0x007DC831`
- [CmDeleteKeyRecursive](../../page/7E/CmDeleteKeyRecursive_function_007E23F8.md) at `0x007E2472`
- [CmSetAcpiHwProfile](../../page/7E/CmSetAcpiHwProfile_function_007E2584.md) at `0x007E267E`
- [CmSetAcpiHwProfile](../../page/7E/CmSetAcpiHwProfile_function_007E2584.md) at `0x007E26F8`
- [CmSetAcpiHwProfile](../../page/7E/CmSetAcpiHwProfile_function_007E2584.md) at `0x007E2752`
- [CmSetAcpiHwProfile](../../page/7E/CmSetAcpiHwProfile_function_007E2584.md) at `0x007E2911`
- [CmSetAcpiHwProfile](../../page/7E/CmSetAcpiHwProfile_function_007E2584.md) at `0x007E2A60`
- [CmpAddAcpiAliasEntry](../../page/7E/CmpAddAcpiAliasEntry_function_007E2DC4.md) at `0x007E2E50`
- [CmpAddAcpiAliasEntry](../../page/7E/CmpAddAcpiAliasEntry_function_007E2DC4.md) at `0x007E2EF9`
- [CmpCloneHwProfile](../../page/7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E3160`
- [CmpCloneHwProfile](../../page/7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E332E`
- [CmpCloneHwProfile](../../page/7E/CmpCloneHwProfile_function_007E303C.md) at `0x007E3432`
- [CmpCreateHwProfileFriendlyName](../../page/7E/CmpCreateHwProfileFriendlyName_function_007E3840.md) at `0x007E39CA`
- [CmpGetAcpiProfileInformation](../../page/7E/CmpGetAcpiProfileInformation_function_007E3D7C.md) at `0x007E3E2E`
- [CmpGetAcpiProfileInformation](../../page/7E/CmpGetAcpiProfileInformation_function_007E3D7C.md) at `0x007E3F50`
- [CmpGetAcpiProfileInformation](../../page/7E/CmpGetAcpiProfileInformation_function_007E3D7C.md) at `0x007E4205`
- [CmpGetAcpiProfileInformation](../../page/7E/CmpGetAcpiProfileInformation_function_007E3D7C.md) at `0x007E431A`
- [CmpMoveBiosAliasTable](../../page/7E/CmpMoveBiosAliasTable_function_007E4578.md) at `0x007E46DA`
- [CmpMoveBiosAliasTable](../../page/7E/CmpMoveBiosAliasTable_function_007E4578.md) at `0x007E47B6`
- [CmpMoveBiosAliasTable](../../page/7E/CmpMoveBiosAliasTable_function_007E4578.md) at `0x007E4977`
- [CmpMoveBiosAliasTable](../../page/7E/CmpMoveBiosAliasTable_function_007E4578.md) at `0x007E49E0`
- [CmpMoveBiosAliasTable](../../page/7E/CmpMoveBiosAliasTable_function_007E4578.md) at `0x007E4AC1`
- [CmpReadBuildVersion](../../page/7E/CmpReadBuildVersion_function_007E52F4.md) at `0x007E538D`
- [CmpLoadLayerVersion](../../page/7E/CmpLoadLayerVersion_function_007E6A74.md) at `0x007E6AFA`
- [CmpLoadLayerVersions](../../page/7E/CmpLoadLayerVersions_function_007E6EC4.md) at `0x007E6F5C`
- [CmpLoadSystemVersionData](../../page/7E/CmpLoadSystemVersionData_function_007E70BC.md) at `0x007E7139`
- [MmZeroPageFileAtShutdown](../../page/7F/MmZeroPageFileAtShutdown_function_007F9164.md) at `0x007F91E5`
- [SdbpCheckMatchingRegistryEntry](../../page/81/SdbpCheckMatchingRegistryEntry_function_0081444C.md) at `0x0081453E`
- [SdbpCheckMatchingRegistryEntry](../../page/81/SdbpCheckMatchingRegistryEntry_function_0081444C.md) at `0x008145A0`
- [AslRegistryGetKey](../../page/81/AslRegistryGetKey_function_00819F64.md) at `0x0081A026`
- [AslRegistryOpenKey_UStr](../../page/81/AslRegistryOpenKey_UStr_function_0081A398.md) at `0x0081A3CE`
- [AslRegistryOpenSubKey](../../page/81/AslRegistryOpenSubKey_function_0081A3E0.md) at `0x0081A478`
- [NtEnableLastKnownGood](../../page/83/NtEnableLastKnownGood_function_0083C680.md) at `0x0083C812`
- [NtEnableLastKnownGood](../../page/83/NtEnableLastKnownGood_function_0083C680.md) at `0x0083C85C`
- [RtlGetPersistedStateLocation](../../page/8C/RtlGetPersistedStateLocation_function_008C8DE0.md) at `0x008C8F16`
- [RtlGetPersistedStateLocation](../../page/8C/RtlGetPersistedStateLocation_function_008C8DE0.md) at `0x008C8F6B`
- [RtlpQueryRegistryValues](../../page/8C/RtlpQueryRegistryValues_function_008C9050.md) at `0x008C92B8`
- [RtlpGetRegistryHandle](../../page/8C/RtlpGetRegistryHandle_function_008C955C.md) at `0x008C968D`
- [sub_0093345B](../../page/93/Unknown_function_0093345B.md) at `0x009336A1`
- [VrpHandleIoctlGetVirtualRootKey](../../page/93/VrpHandleIoctlGetVirtualRootKey_function_00935374.md) at `0x0093548A`
- [VrpLoadDifferencingHive](../../page/93/VrpLoadDifferencingHive_function_00935F40.md) at `0x009360C0`
- [VrpLoadDifferencingHive](../../page/93/VrpLoadDifferencingHive_function_00935F40.md) at `0x00936232`
- [PipCheckForDenyExecute](../../page/94/PipCheckForDenyExecute_function_0094F880.md) at `0x0094F947`
- [KsepRegistryQueryDriverShims](../../page/95/KsepRegistryQueryDriverShims_function_00959524.md) at `0x00959605`
- [KsepRegistryOpenKey](../../page/95/KsepRegistryOpenKey_function_0095A79C.md) at `0x0095A87E`
- [KsepDbQueryRegistryDeviceData](../../page/95/KsepDbQueryRegistryDeviceData_function_0095B174.md) at `0x0095B29A`
- [PiDevCfgConfigureDeviceInterface](../../page/96/PiDevCfgConfigureDeviceInterface_function_00963C18.md) at `0x00963C8C`
- [PiDevCfgConfigureDeviceInterface](../../page/96/PiDevCfgConfigureDeviceInterface_function_00963C18.md) at `0x00963CE3`
- [PiDevCfgInitMigrationContext](../../page/96/PiDevCfgInitMigrationContext_function_009642E0.md) at `0x009643A7`
- [PiDevCfgInitMigrationContext](../../page/96/PiDevCfgInitMigrationContext_function_009642E0.md) at `0x00964415`
- [PiDevCfgConfigureDeviceKeys](../../page/96/PiDevCfgConfigureDeviceKeys_function_00964BA8.md) at `0x00964CF7`
- [PiDevCfgEnumDeviceKeys](../../page/96/PiDevCfgEnumDeviceKeys_function_00964EE8.md) at `0x00964FD4`
- [PiDevCfgInitResolveContext](../../page/96/PiDevCfgInitResolveContext_function_00965178.md) at `0x009651F9`
- [PiDevCfgConfigureSoftwareDevices](../../page/96/PiDevCfgConfigureSoftwareDevices_function_009652EC.md) at `0x00965354`
- [PiOpenDriverRedirectedStateKey](../../page/96/PiOpenDriverRedirectedStateKey_function_00965D04.md) at `0x00965E3C`
- [PiDevCfgVerifyDeviceAllowed](../../page/96/PiDevCfgVerifyDeviceAllowed_function_009664E4.md) at `0x00966561`
- [SPCallServerHandleQueryPolicy](../../page/96/SPCallServerHandleQueryPolicy_function_0096AF24.md) at `0x0096BA4C`
- [PiDevCfgBuildIndirectString](../../page/97/PiDevCfgBuildIndirectString_function_0097A890.md) at `0x0097A94C`
- [IopLoadUnloadDriver](../../page/99/IopLoadUnloadDriver_function_00996B80.md) at `0x00996BDE`
- [PnpPrepareDriverLoading](../../page/99/PnpPrepareDriverLoading_function_00996CC8.md) at `0x00996DCC`
- [pIoQueryBusDescription](../../page/99/pIoQueryBusDescription_function_00996F58.md) at `0x009970AC`
- [PiDevCfgCopyDeviceKey](../../page/99/PiDevCfgCopyDeviceKey_function_00997374.md) at `0x00997890`
- [IoOpenDriverRegistryKey](../../page/99/IoOpenDriverRegistryKey_function_00998BB0.md) at `0x00998D1E`
- [PipOpenServiceEnumKeys](../../page/99/PipOpenServiceEnumKeys_function_00998E94.md) at `0x00998F33`
- [PipOpenServiceEnumKeys](../../page/99/PipOpenServiceEnumKeys_function_00998E94.md) at `0x0099900F`
- [PipOpenServiceEnumKeys](../../page/99/PipOpenServiceEnumKeys_function_00998E94.md) at `0x0099909F`
- [PiCreateServiceStateKey](../../page/99/PiCreateServiceStateKey_function_009993E0.md) at `0x0099947F`
- [PiNormalizeDeviceText](../../page/99/PiNormalizeDeviceText_function_0099A43C.md) at `0x0099A5B7`
- [PspAllocateProcess](../../page/A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A14784`
- [PspAllocateProcess](../../page/A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A14982`
- [RtlpInitNlsFileName](../../page/A1/RtlpInitNlsFileName_function_00A19B9C.md) at `0x00A19C62`
- [RtlCapabilityCheck](../../page/A2/RtlCapabilityCheck_function_00A20340.md) at `0x00A20458`
- [PopConfigureHeteroPolicies](../../page/A3/PopConfigureHeteroPolicies_function_00A35B30.md) at `0x00A360E8`
- [PopConfigureHeteroPolicies](../../page/A3/PopConfigureHeteroPolicies_function_00A35B30.md) at `0x00A3612C`
- [SiOpenRegistryKey](../../page/A3/SiOpenRegistryKey_function_00A37F00.md) at `0x00A37F69`
- [SepRegOpenKey](../../page/A3/SepRegOpenKey_function_00A3A6B4.md) at `0x00A3A717`
- [RtlpOpenImageFileOptionsKeyEx](../../page/A3/RtlpOpenImageFileOptionsKeyEx_function_00A3B8A8.md) at `0x00A3B980`
- [RtlpProcessIFEOKeyFilter](../../page/A3/RtlpProcessIFEOKeyFilter_function_00A3BA78.md) at `0x00A3BC89`
- [BiOpenKeyNonBcd](../../page/A4/BiOpenKeyNonBcd_function_00A40B48.md) at `0x00A40BD3`
- [BiLoadHive](../../page/A4/BiLoadHive_function_00A412F4.md) at `0x00A41528`
- [NtLockProductActivationKeys](../../page/A4/NtLockProductActivationKeys_function_00A492E0.md) at `0x00A494CE`
- [NtLockProductActivationKeys](../../page/A4/NtLockProductActivationKeys_function_00A492E0.md) at `0x00A4962F`
- [WmipGetRegistryHideMachine](../../page/A4/WmipGetRegistryHideMachine_function_00A4F174.md) at `0x00A4F1E6`
- [IopOpenRegistryKeyEx](../../page/A5/IopOpenRegistryKeyEx_function_00A51B44.md) at `0x00A51B78`
- [PspReadUserQuotaLimits](../../page/A6/PspReadUserQuotaLimits_function_00A68108.md) at `0x00A681CE`
- [KGetUnlockSetting](../../page/A6/KGetUnlockSetting_function_00A691BC.md) at `0x00A69221`
- [PiDevCfgResolveVariable](../../page/A8/PiDevCfgResolveVariable_function_00A81AB8.md) at `0x00A81BC9`
- [CmEtwRunDown](../../page/A8/CmEtwRunDown_function_00A85AC0.md) at `0x00A85CC0`
- [ExpSetPendingUILanguage](../../page/A8/ExpSetPendingUILanguage_function_00A87E70.md) at `0x00A87F5B`
- [ExpSetPendingUILanguage](../../page/A8/ExpSetPendingUILanguage_function_00A87E70.md) at `0x00A87FF0`
- [ExpSetPendingUILanguage](../../page/A8/ExpSetPendingUILanguage_function_00A87E70.md) at `0x00A8802D`
- [ExpSetPendingUILanguage](../../page/A8/ExpSetPendingUILanguage_function_00A87E70.md) at `0x00A88127`
- [ExpSetPendingUILanguage](../../page/A8/ExpSetPendingUILanguage_function_00A87E70.md) at `0x00A8816C`
- [PiDevCfgEnforceDevicePolicy](../../page/A8/PiDevCfgEnforceDevicePolicy_function_00A89454.md) at `0x00A894EC`
- [IopOpenRegistryKey](../../page/A8/IopOpenRegistryKey_function_00A8F200.md) at `0x00A8F23F`
- [PiDevCfgConfigureDeviceInterfaces](../../page/A9/PiDevCfgConfigureDeviceInterfaces_function_00A90060.md) at `0x00A9010E`
- [PiDevCfgConfigureDeviceInterfaces](../../page/A9/PiDevCfgConfigureDeviceInterfaces_function_00A90060.md) at `0x00A901B5`
- [PiDevCfgConfigureDeviceInterfaces](../../page/A9/PiDevCfgConfigureDeviceInterfaces_function_00A90060.md) at `0x00A9029A`
- [PiDrvDbLoadHive](../../page/A9/PiDrvDbLoadHive_function_00A91EE4.md) at `0x00A91FA0`
- [EtwpEnableAutoLoggerProvider](../../page/A9/EtwpEnableAutoLoggerProvider_function_00A92B00.md) at `0x00A92C83`
- [EtwpEnableAutoLoggerProvider](../../page/A9/EtwpEnableAutoLoggerProvider_function_00A92B00.md) at `0x00A92D37`
- [EtwpGetAutoLoggerProviderFilter](../../page/A9/EtwpGetAutoLoggerProviderFilter_function_00A93248.md) at `0x00A933D2`
- [EtwpGetAutoLoggerProviderFilter](../../page/A9/EtwpGetAutoLoggerProviderFilter_function_00A93248.md) at `0x00A93530`
- [EtwpGetAutoLoggerLevelKwFilter](../../page/A9/EtwpGetAutoLoggerLevelKwFilter_function_00A93AA8.md) at `0x00A93BAB`
- [EtwpGetAutoLoggerLevelKwFilter](../../page/A9/EtwpGetAutoLoggerLevelKwFilter_function_00A93AA8.md) at `0x00A93C50`
- [EtwpGetAutoLoggerEventNameFilter](../../page/A9/EtwpGetAutoLoggerEventNameFilter_function_00A93E78.md) at `0x00A93FAB`
- [EtwpGetAutoLoggerEventNameFilter](../../page/A9/EtwpGetAutoLoggerEventNameFilter_function_00A93E78.md) at `0x00A94070`
- [PopReadHiberbootGroupPolicy](../../page/A9/PopReadHiberbootGroupPolicy_function_00A95204.md) at `0x00A95289`
- [IopRegistryOpenDeepestPath](../../page/A9/IopRegistryOpenDeepestPath_function_00A96114.md) at `0x00A9617E`
- [PpDevCfgProcessDeviceOperations](../../page/A9/PpDevCfgProcessDeviceOperations_function_00A97CFC.md) at `0x00A97D95`
- [PiDevCfgOpenDriverConfiguration](../../page/A9/PiDevCfgOpenDriverConfiguration_function_00A995F0.md) at `0x00A99660`
- [PiDevCfgOpenDriverConfiguration](../../page/A9/PiDevCfgOpenDriverConfiguration_function_00A995F0.md) at `0x00A996D8`
- [IoQueryDeviceDescription](../../page/A9/IoQueryDeviceDescription_function_00A9D8E0.md) at `0x00A9D9A7`
- [PopInitializePowerPolicySimulate](../../page/A9/PopInitializePowerPolicySimulate_function_00A9DA28.md) at `0x00A9DAB7`
- [PipDmgGetDriverDmarCompatLevel](../../page/AA/PipDmgGetDriverDmarCompatLevel_function_00AA0A40.md) at `0x00AA0AD6`
- [RtlpGetNtProductTypeFromRegistry](../../page/AA/RtlpGetNtProductTypeFromRegistry_function_00AA26D8.md) at `0x00AA27A9`
- [PiDevCfgConfigureDeviceFilters](../../page/AA/PiDevCfgConfigureDeviceFilters_function_00AA67DC.md) at `0x00AA6849`
- [NtSetDefaultLocale](../../page/AA/NtSetDefaultLocale_function_00AAE850.md) at `0x00AAE96C`
- [NtSetDefaultLocale](../../page/AA/NtSetDefaultLocale_function_00AAE850.md) at `0x00AAEA62`
- [NtSetDefaultLocale](../../page/AA/NtSetDefaultLocale_function_00AAE850.md) at `0x00AAEA94`
- [EtwpEnumerateKeyProviders](../../page/AB/EtwpEnumerateKeyProviders_function_00AB029C.md) at `0x00AB0328`
- [ExpReadComPlusPackage](../../page/AB/ExpReadComPlusPackage_function_00AB78D4.md) at `0x00AB7917`
- [PnpDriverLoadingFailed](../../page/AB/PnpDriverLoadingFailed_function_00AB8928.md) at `0x00AB89EB`
- [PerfDiagpIsTracingAllowed](../../page/AD/PerfDiagpIsTracingAllowed_function_00AD06C0.md) at `0x00AD0758`
- [PopIsRemoteDesktopEnabled](../../page/AD/PopIsRemoteDesktopEnabled_function_00AD6E64.md) at `0x00AD6EFD`
- [sub_00B246DA](../../page/B2/Unknown_function_00B246DA.md) at `0x00B2479B`
- [sub_00B24914](../../page/B2/Unknown_function_00B24914.md) at `0x00B24A41`
- [sub_00B2C5F4](../../page/B2/Unknown_function_00B2C5F4.md) at `0x00B2CA45`
- [sub_00B2C5F4](../../page/B2/Unknown_function_00B2C5F4.md) at `0x00B2CAED`
- [sub_00B44C1A](../../page/B4/Unknown_function_00B44C1A.md) at `0x00B44D0F`
- [PopGetBitlockerKeyLocation](../../pagelk/B6/PopGetBitlockerKeyLocation_function_00B6BBFC.md) at `0x00B6BC90`
- [HalpPiix4Detect](../../pagelk/B7/HalpPiix4Detect_function_00B79E00.md) at `0x00B79F3C`
- [BapdGetISRegistryKey](../../pagelk/B7/BapdGetISRegistryKey_function_00B7B838.md) at `0x00B7B8A6`
- [BapdpWriteEventDataToRegistry](../../pagelk/B7/BapdpWriteEventDataToRegistry_function_00B7C1E8.md) at `0x00B7C264`
- [sub_00B80E6E](../../pagelk/B8/Unknown_function_00B80E6E.md) at `0x00B80EAE`
- [LogFwpRegisterWorker](../../pagebgfx/BC/LogFwpRegisterWorker_function_00BC4B90.md) at `0x00BC4C01`
- [CreateMiniNtBootKey](../../init/C1/CreateMiniNtBootKey_function_00C1A840.md) at `0x00C1A8F5`
- [InitSafeBoot](../../init/C1/InitSafeBoot_function_00C1BFE0.md) at `0x00C1C06B`
- [MfgInitSystem](../../init/C1/MfgInitSystem_function_00C1C390.md) at `0x00C1C50F`
- [MfgInitSystem](../../init/C1/MfgInitSystem_function_00C1C390.md) at `0x00C1C555`
- [RegistryOverwriteCentralProcessor](../../init/C1/RegistryOverwriteCentralProcessor_function_00C1DB4C.md) at `0x00C1DBF2`
- [RegistryOverwriteCentralProcessor](../../init/C1/RegistryOverwriteCentralProcessor_function_00C1DB4C.md) at `0x00C1DC61`
- [HalpDmaFinalizeDoubleBufferingDisposition](../../init/C1/HalpDmaFinalizeDoubleBufferingDisposition_function_00C1E354.md) at `0x00C1E3E1`
- [HalpInitChipHacks](../../init/C2/HalpInitChipHacks_function_00C24274.md) at `0x00C24317`
- [ArbDeleteMmConfigRange](../../init/C2/ArbDeleteMmConfigRange_function_00C25D5C.md) at `0x00C25DC7`
- [ArbDeleteMmConfigRange](../../init/C2/ArbDeleteMmConfigRange_function_00C25D5C.md) at `0x00C25E15`
- [ArbInitializeMmConfigRange](../../init/C2/ArbInitializeMmConfigRange_function_00C25E6C.md) at `0x00C25EDF`
- [ArbInitializeMmConfigRange](../../init/C2/ArbInitializeMmConfigRange_function_00C25E6C.md) at `0x00C25F2D`
- [ArbInitializeOsInaccessibleRange](../../init/C2/ArbInitializeOsInaccessibleRange_function_00C25F9C.md) at `0x00C26034`
- [FsRtlGetCompatibilityModeValue](../../init/C2/FsRtlGetCompatibilityModeValue_function_00C28D84.md) at `0x00C28E0B`
- [IoInitSystemPreDrivers](../../init/C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2B131`
- [PiLastGoodCopyKeyContents](../../init/C3/PiLastGoodCopyKeyContents_function_00C336E4.md) at `0x00C33784`
- [PiLastGoodRevertLastKnownDirectory](../../init/C3/PiLastGoodRevertLastKnownDirectory_function_00C33980.md) at `0x00C33A56`
- [KiInitializeReservedCpuSets](../../init/C3/KiInitializeReservedCpuSets_function_00C39DAC.md) at `0x00C39E71`
- [PopReadSimulatedArchitecturalClasses](../../init/C4/PopReadSimulatedArchitecturalClasses_function_00C41284.md) at `0x00C41350`
- [PopReadSimulatedArchitecturalClasses](../../init/C4/PopReadSimulatedArchitecturalClasses_function_00C41284.md) at `0x00C413CE`
- [PopReadSimulatedHGSClasses](../../init/C4/PopReadSimulatedHGSClasses_function_00C41470.md) at `0x00C41654`
- [PopReadSimulatedHGSClasses](../../init/C4/PopReadSimulatedHGSClasses_function_00C41470.md) at `0x00C416EE`
- [PopReadSimulatedHGSClasses](../../init/C4/PopReadSimulatedHGSClasses_function_00C41470.md) at `0x00C41712`
- [PopReadSimulatedHGSClasses](../../init/C4/PopReadSimulatedHGSClasses_function_00C41470.md) at `0x00C41772`
- [PopReadSimulatedHGSClasses](../../init/C4/PopReadSimulatedHGSClasses_function_00C41470.md) at `0x00C41799`
- [PopReadSimulatedHGSClasses](../../init/C4/PopReadSimulatedHGSClasses_function_00C41470.md) at `0x00C4181C`
- [PopInitializePowerButtonHold](../../init/C4/PopInitializePowerButtonHold_function_00C425A8.md) at `0x00C4273D`
- [PopInitializePowerButtonHold](../../init/C4/PopInitializePowerButtonHold_function_00C425A8.md) at `0x00C427BD`
- [PsInitializeBootCpuPartitions](../../init/C4/PsInitializeBootCpuPartitions_function_00C44D94.md) at `0x00C44EAA`
- [PsInitializeBootCpuPartitions](../../init/C4/PsInitializeBootCpuPartitions_function_00C44D94.md) at `0x00C44F59`
- [PsInitializeBootCpuPartitions](../../init/C4/PsInitializeBootCpuPartitions_function_00C44D94.md) at `0x00C44F9B`
- [SepSecureBootCheckForUpdates](../../init/C4/SepSecureBootCheckForUpdates_function_00C4B688.md) at `0x00C4B6EE`
- [EtwpReadConfigParameters](../../init/C4/EtwpReadConfigParameters_function_00C4E32C.md) at `0x00C4E3B9`
- [EtwpInitializeSecurity](../../init/C4/EtwpInitializeSecurity_function_00C4EDF0.md) at `0x00C4EE7E`
- [EtwpInitializeSecurity](../../init/C4/EtwpInitializeSecurity_function_00C4EDF0.md) at `0x00C4EF0B`
- [BapdpRegisterBitlockerStatus](../../init/C5/BapdpRegisterBitlockerStatus_function_00C50528.md) at `0x00C505AB`
- [BapdpRegisterEDrvHintInfo](../../init/C5/BapdpRegisterEDrvHintInfo_function_00C5067C.md) at `0x00C50706`
- [BapdpRegisterFwUpdateResults](../../init/C5/BapdpRegisterFwUpdateResults_function_00C507E4.md) at `0x00C50890`
- [BapdpRegisterResumeInformation](../../init/C5/BapdpRegisterResumeInformation_function_00C509F4.md) at `0x00C50A76`
- [BapdpRegisterWmdResult](../../init/C5/BapdpRegisterWmdResult_function_00C50C58.md) at `0x00C50CD1`
- [CmpAddAliasEntry](../../init/C5/CmpAddAliasEntry_function_00C56584.md) at `0x00C5660E`
- [CmpAddAliasEntry](../../init/C5/CmpAddAliasEntry_function_00C56584.md) at `0x00C566CE`
- [CmpCreateControlSet](../../init/C5/CmpCreateControlSet_function_00C56910.md) at `0x00C569E3`
- [CmpCreateControlSet](../../init/C5/CmpCreateControlSet_function_00C56910.md) at `0x00C56A2D`
- [CmpCreateControlSetOverride](../../init/C5/CmpCreateControlSetOverride_function_00C56CC8.md) at `0x00C56D84`
- [CmpCreateHardwareProfiles](../../init/C5/CmpCreateHardwareProfiles_function_00C56EF4.md) at `0x00C56FD4`
- [CmpCreateHardwareProfiles](../../init/C5/CmpCreateHardwareProfiles_function_00C56EF4.md) at `0x00C5725C`
- [CmpCreateHardwareProfiles](../../init/C5/CmpCreateHardwareProfiles_function_00C56EF4.md) at `0x00C57312`
- [CmpCreateHardwareProfiles](../../init/C5/CmpCreateHardwareProfiles_function_00C56EF4.md) at `0x00C574D1`
- [CmpMigrateOOBELanguageToInstallationLanguage](../../init/C5/CmpMigrateOOBELanguageToInstallationLanguage_function_00C589A0.md) at `0x00C58A17`
- [CmpSetSystemValues](../../init/C5/CmpSetSystemValues_function_00C58BB0.md) at `0x00C58C3C`
- [CmpInitializeMachineDependentConfiguration](../../init/C5/CmpInitializeMachineDependentConfiguration_function_00C5A02C.md) at `0x00C5A135`
- [QueryRegistryHideMachine](../../init/C6/QueryRegistryHideMachine_function_00C6FC84.md) at `0x00C6FD0C`
- [CmGetSystemDriverList](../../init/C7/CmGetSystemDriverList_function_00C7380C.md) at `0x00C73C50`
- [CmpOpenSystemDriverHiveContext](../../init/C7/CmpOpenSystemDriverHiveContext_function_00C73D90.md) at `0x00C73E81`

### Static image references
- `0x006AD31C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD329` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD310  48 8B C4                        mov rax, rsp
006AD313  FA                              cli
006AD314  48 83 EC 10                     sub rsp, 0x10
006AD318  50                              push rax
006AD319  9C                              pushfq
006AD31A  6A 10                           push 0x10
006AD31C  48 8D 05 3D 61 00 00            lea rax, [rip + 0x613d]
006AD323  50                              push rax
006AD324  B8 12 00 00 00                  mov eax, 0x12
006AD329  E9 92 76 01 00                  jmp 0x1406c49c0
006AD32E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwOpenKey(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwOpenKey(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD310&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD310[BB_006AD310]
  bb_006AD32E[BB_006AD32E]
```
