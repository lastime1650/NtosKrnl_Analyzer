# SeSinglePrivilegeCheck

- RVA: `0x00871E20`–`0x00871E3E` (길이 `30` bytes)
- VA: `0x0000000140871E20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C4D4`
- 디코드: `8`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **129**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [NtSetInformationFile](../../text/29/NtSetInformationFile_function_0029C5E0.md) at `0x0029D4D9`
- [ExCpuSetResourceManagerAccessCheck](../../text/3A/ExCpuSetResourceManagerAccessCheck_function_003A5444.md) at `0x003A5475`
- [SepVerifyDesktopAppPolicyOverrideCaller](../../text/45/SepVerifyDesktopAppPolicyOverrideCaller_function_0045C1F0.md) at `0x0045C265`
- [EtwpUpdateSelectedGroupMasks](../../text/49/EtwpUpdateSelectedGroupMasks_function_0049B114.md) at `0x0049B454`
- [SepLinkLogonSessions](../../text/4A/SepLinkLogonSessions_function_004AAE78.md) at `0x004AAED2`
- [IopLoadDriverImage](../../text/4F/IopLoadDriverImage_function_004FA0FC.md) at `0x004FA15B`
- [PsQueryCpuQuotaInformation](../../text/5E/PsQueryCpuQuotaInformation_function_005E27C0.md) at `0x005E2809`
- [PsSetCpuQuotaInformation](../../text/5E/PsSetCpuQuotaInformation_function_005E28F8.md) at `0x005E2951`
- [SepOneWayLinkLogonSessions](../../text/60/SepOneWayLinkLogonSessions_function_006068D8.md) at `0x0060694C`
- [EtwpGetPmcOwnership](../../text/64/EtwpGetPmcOwnership_function_0064E960.md) at `0x0064E988`
- [NtDrawText](../../text/65/NtDrawText_function_006559F0.md) at `0x00655A2E`
- [NtShutdownSystem](../../text/65/NtShutdownSystem_function_00655B70.md) at `0x00655BAD`
- [ExPoolQueryLimits](../../text/65/ExPoolQueryLimits_function_006562A0.md) at `0x006562EC`
- [ExPoolSetLimit](../../text/65/ExPoolSetLimit_function_00656498.md) at `0x006564C9`
- [NtReplacePartitionUnit](../../text/6A/NtReplacePartitionUnit_function_006A85A0.md) at `0x006A860C`
- [VslTransformDumpKey](../71/VslTransformDumpKey_function_00719A08.md) at `0x00719A8A`
- [NtSetInformationSymbolicLink](../74/NtSetInformationSymbolicLink_function_0074E910.md) at `0x0074E999`
- [NtSetInformationSymbolicLink](../74/NtSetInformationSymbolicLink_function_0074E910.md) at `0x0074EA18`
- [ObSetRefTraceInformation](../74/ObSetRefTraceInformation_function_0074F7B0.md) at `0x0074F7DE`
- [NtInitiatePowerAction](../75/NtInitiatePowerAction_function_0075FCB0.md) at `0x0075FD1C`
- [PspApplyIFEOPerfOptions](../78/PspApplyIFEOPerfOptions_function_00783ED8.md) at `0x00783F12`
- [PsCreatePartition](../78/PsCreatePartition_function_00787EB0.md) at `0x00787F2F`
- [NtFilterBootOption](../7A/NtFilterBootOption_function_007A1BE0.md) at `0x007A1C85`
- [SmProcessConfigRequest](../7A/SmProcessConfigRequest_function_007A62E4.md) at `0x007A65B7`
- [SmProcessStatsRequest](../7A/SmProcessStatsRequest_function_007A6E68.md) at `0x007A6F6D`
- [EtwpSetMark](../7B/EtwpSetMark_function_007B878C.md) at `0x007B882F`
- [NtSetSystemTime](../7C/NtSetSystemTime_function_007C65F0.md) at `0x007C6675`
- [NtDisplayString](../7C/NtDisplayString_function_007C7270.md) at `0x007C72B4`
- [ExpSetBootEntry](../7C/ExpSetBootEntry_function_007CBD2C.md) at `0x007CBE4D`
- [ExpSetDriverEntry](../7C/ExpSetDriverEntry_function_007CC424.md) at `0x007CC539`
- [NtDeleteBootEntry](../7C/NtDeleteBootEntry_function_007CD2B0.md) at `0x007CD311`
- [NtDeleteDriverEntry](../7C/NtDeleteDriverEntry_function_007CD440.md) at `0x007CD4A1`
- [NtEnumerateDriverEntries](../7C/NtEnumerateDriverEntries_function_007CD5D0.md) at `0x007CD69A`
- [NtEnumerateSystemEnvironmentValuesEx](../7C/NtEnumerateSystemEnvironmentValuesEx_function_007CDA30.md) at `0x007CDAD9`
- [NtQueryDriverEntryOrder](../7C/NtQueryDriverEntryOrder_function_007CDCE0.md) at `0x007CDD93`
- [NtQuerySystemEnvironmentValue](../7C/NtQuerySystemEnvironmentValue_function_007CDFB0.md) at `0x007CE0CA`
- [NtSetBootOptions](../7C/NtSetBootOptions_function_007CE2B0.md) at `0x007CE36A`
- [NtSetDriverEntryOrder](../7C/NtSetDriverEntryOrder_function_007CE490.md) at `0x007CE4F5`
- [NtSetSystemEnvironmentValue](../7C/NtSetSystemEnvironmentValue_function_007CE650.md) at `0x007CE791`
- [NtSetSystemEnvironmentValueEx](../7C/NtSetSystemEnvironmentValueEx_function_007CE990.md) at `0x007CEABD`
- [NtSetDefaultHardErrorPort](../7D/NtSetDefaultHardErrorPort_function_007D0340.md) at `0x007D036B`
- [ExpProfileCreate](../7D/ExpProfileCreate_function_007D1AB8.md) at `0x007D1DA6`
- [NtSetIntervalProfile](../7D/NtSetIntervalProfile_function_007D2260.md) at `0x007D2284`
- [NtFlushInstallUILanguage](../7D/NtFlushInstallUILanguage_function_007D4200.md) at `0x007D4233`
- [NtCompactKeys](../7D/NtCompactKeys_function_007DF730.md) at `0x007DF79E`
- [NtCompressKey](../7D/NtCompressKey_function_007DF9D0.md) at `0x007DFA4B`
- [NtFreezeRegistry](../7D/NtFreezeRegistry_function_007DFBD0.md) at `0x007DFC37`
- [NtInitializeRegistry](../7D/NtInitializeRegistry_function_007DFC90.md) at `0x007DFCE2`
- [NtQueryOpenSubKeysEx](../7E/NtQueryOpenSubKeysEx_function_007E0190.md) at `0x007E0270`
- [NtReplaceKey](../7E/NtReplaceKey_function_007E0970.md) at `0x007E0A2D`
- [NtRestoreKey](../7E/NtRestoreKey_function_007E0CC0.md) at `0x007E0D7B`
- [NtSaveMergedKeys](../7E/NtSaveMergedKeys_function_007E1070.md) at `0x007E113B`
- [NtThawRegistry](../7E/NtThawRegistry_function_007E1320.md) at `0x007E1376`
- [MmCreateMirror](../7F/MmCreateMirror_function_007FCB50.md) at `0x007FCBC0`
- [MmIssueMemoryListCommand](../7F/MmIssueMemoryListCommand_function_007FE8B0.md) at `0x007FE8D0`
- [MiCreatePagingFile](../7F/MiCreatePagingFile_function_007FEFF4.md) at `0x007FF0CE`
- [MiAllocateAweInfo](../80/MiAllocateAweInfo_function_00809518.md) at `0x0080964F`
- [MiAllocateUserPhysicalPages](../80/MiAllocateUserPhysicalPages_function_00809828.md) at `0x00809AD1`
- [MmManagePartitionCharges](../80/MmManagePartitionCharges_function_0080DDAC.md) at `0x0080DE0B`
- [MmManagePartitionCreateLargePages](../80/MmManagePartitionCreateLargePages_function_0080E000.md) at `0x0080E028`
- [MmManagePartitionMoveMemory](../80/MmManagePartitionMoveMemory_function_0080E1F4.md) at `0x0080E356`
- [MmManagePartitionUpdateAttributes](../80/MmManagePartitionUpdateAttributes_function_0080E5A4.md) at `0x0080E61F`
- [MiOpenSpecialPurposeMemory](../80/MiOpenSpecialPurposeMemory_function_0080FA28.md) at `0x0080FA8E`
- [VrpHandleIoctlLoadDifferencingHiveForHost](../83/VrpHandleIoctlLoadDifferencingHiveForHost_function_0083B464.md) at `0x0083B514`
- [VrpHandleIoctlLoadDifferencingHiveForHost](../83/VrpHandleIoctlLoadDifferencingHiveForHost_function_0083B464.md) at `0x0083B531`
- [VrpHandleIoctlUnloadDifferencingHiveForHost](../83/VrpHandleIoctlUnloadDifferencingHiveForHost_function_0083B7A4.md) at `0x0083B80A`
- [VrpHandleIoctlUnloadDifferencingHiveForHost](../83/VrpHandleIoctlUnloadDifferencingHiveForHost_function_0083B7A4.md) at `0x0083B827`
- [NtDisableLastKnownGood](../83/NtDisableLastKnownGood_function_0083C560.md) at `0x0083C5A3`
- [NtEnableLastKnownGood](../83/NtEnableLastKnownGood_function_0083C680.md) at `0x0083C6F7`
- [NtSerializeBoot](../83/NtSerializeBoot_function_0083C940.md) at `0x0083C965`
- [NtSetDebugFilterState](../83/NtSetDebugFilterState_function_0083C990.md) at `0x0083C9C0`
- [CmLoadDifferencingKey](CmLoadDifferencingKey_function_00875670.md) at `0x00876232`
- [MiAllocateVirtualMemory](../88/MiAllocateVirtualMemory_function_00883B40.md) at `0x008842AD`
- [PsOpenProcess](../89/PsOpenProcess_function_00894A30.md) at `0x00894CE3`
- [PsOpenProcess](../89/PsOpenProcess_function_00894A30.md) at `0x00894CFA`
- [ObpLookupObjectName](../89/ObpLookupObjectName_function_0089BE90.md) at `0x0089D90E`
- [NtCreateWnfStateName](../8B/NtCreateWnfStateName_function_008BE2B0.md) at `0x008BE645`
- [sub_008C28B0](../8C/Unknown_function_008C28B0.md) at `0x008C28B9`
- [NtCreateSemaphore](../8C/NtCreateSemaphore_function_008C38D0.md) at `0x008C3B35`
- [sub_008C3F6B](../8C/Unknown_function_008C3F6B.md) at `0x008C3FA5`
- [NtCreateMutant](../8C/NtCreateMutant_function_008C43D0.md) at `0x008C461B`
- [NtCreateWaitCompletionPacket](../8C/NtCreateWaitCompletionPacket_function_008C4700.md) at `0x008C4932`
- [NtGetNextThread](../8C/NtGetNextThread_function_008C7D40.md) at `0x008C7EDB`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CAC8D`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CB4EF`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CB81C`
- [sub_008E40CB](../8E/Unknown_function_008E40CB.md) at `0x008E40E0`
- [PfQuerySuperfetchInformation](../90/PfQuerySuperfetchInformation_function_0090210C.md) at `0x00902237`
- [ExpWnfCheckCrossScopeAccess](../90/ExpWnfCheckCrossScopeAccess_function_0090CA94.md) at `0x0090CB9D`
- [PfpPrivSourceEnum](../91/PfpPrivSourceEnum_function_0091BF00.md) at `0x0091C01C`
- [NtGetNextProcess](../91/NtGetNextProcess_function_0091DF50.md) at `0x0091E08E`
- [VrpHandleIoctlLoadDifferencingHive](../93/VrpHandleIoctlLoadDifferencingHive_function_00935C5C.md) at `0x00935CA9`
- [VrpHandleIoctlLoadDifferencingHive](../93/VrpHandleIoctlLoadDifferencingHive_function_00935C5C.md) at `0x00935CC0`
- [NtQuerySystemEnvironmentValueEx](../95/NtQuerySystemEnvironmentValueEx_function_00952180.md) at `0x00952204`
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x009560AA`
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x00957AF3`
- [PfSnSetPrefetcherInformation](../96/PfSnSetPrefetcherInformation_function_0096139C.md) at `0x00961448`
- [CmUnloadKey](../9A/CmUnloadKey_function_009AF2FC.md) at `0x009AF3FD`
- [PsOpenThread](../9C/PsOpenThread_function_009C5CC0.md) at `0x009C5EAE`
- [PsOpenThread](../9C/PsOpenThread_function_009C5CC0.md) at `0x009C5F79`
- [NtCreateTokenEx](../9C/NtCreateTokenEx_function_009C7C80.md) at `0x009C7E58`
- [MiLockUnlockCommon](../9E/MiLockUnlockCommon_function_009EA5D0.md) at `0x009EA716`
- [PspSetProcessPriorityClass](../9F/PspSetProcessPriorityClass_function_009F61E4.md) at `0x009F62B5`
- [NtSetInformationJobObject](../9F/NtSetInformationJobObject_function_009F84C0.md) at `0x009F8DCD`
- [NtSetInformationJobObject](../9F/NtSetInformationJobObject_function_009F84C0.md) at `0x009FA252`
- [NtSetInformationJobObject](../9F/NtSetInformationJobObject_function_009F84C0.md) at `0x009FA2CF`
- [NtSetInformationJobObject](../9F/NtSetInformationJobObject_function_009F84C0.md) at `0x009FAD1E`
- [SmQueryStoreInformation](../A0/SmQueryStoreInformation_function_00A0E7BC.md) at `0x00A0E834`
- [PspAllocateProcess](../A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A14CC3`
- [PspAllocateProcess](../A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A14F9D`
- [PspAllocateProcess](../A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A15B87`
- [ExIsRestrictedCaller](../A2/ExIsRestrictedCaller_function_00A217E8.md) at `0x00A21839`
- [NtTranslateFilePath](../A2/NtTranslateFilePath_function_00A24D50.md) at `0x00A24EBC`
- [NtEnumerateBootEntries](../A2/NtEnumerateBootEntries_function_00A25040.md) at `0x00A25119`
- [SmProcessCreateRequest](../A5/SmProcessCreateRequest_function_00A50DD0.md) at `0x00A5125F`
- [PfSnQueryPrefetcherInformation](../A5/PfSnQueryPrefetcherInformation_function_00A51B8C.md) at `0x00A51BBB`
- [ExpQuerySystemInformation](../A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A58D48`
- [ExpQuerySystemInformation](../A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A59CCF`
- [ExpQuerySystemInformation](../A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A5A055`
- [ExpQuerySystemInformation](../A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A5A84C`
- [MmProcessWorkingSetControl](../A6/MmProcessWorkingSetControl_function_00A616C4.md) at `0x00A618FC`
- [ExpRaiseHardError](../A6/ExpRaiseHardError_function_00A64AD4.md) at `0x00A64C7D`
- [NtSystemDebugControl](../A6/NtSystemDebugControl_function_00A6E760.md) at `0x00A6E83B`
- [SmSetStoreInformation](../A7/SmSetStoreInformation_function_00A781B8.md) at `0x00A781F8`
- [NtSaveKeyEx](../A8/NtSaveKeyEx_function_00A853C0.md) at `0x00A85469`
- [PopPowerInformationInternal](../A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8B90D`
- [NtQueryBootEntryOrder](../A9/NtQueryBootEntryOrder_function_00A91720.md) at `0x00A917DB`
- [NtSetBootEntryOrder](../A9/NtSetBootEntryOrder_function_00A91930.md) at `0x00A91A1B`
- [NtMakePermanentObject](../A9/NtMakePermanentObject_function_00A979F0.md) at `0x00A97A1F`
- [NtQueryBootOptions](../AA/NtQueryBootOptions_function_00AAFBC0.md) at `0x00AAFC6B`
- [IopUnloadDriver](../AB/IopUnloadDriver_function_00ABF868.md) at `0x00ABF8F8`
- [PfSetSuperfetchInformation](../AD/PfSetSuperfetchInformation_function_00ADE6E8.md) at `0x00ADE79F`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE5F1C`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE6269`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE63D1`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE67F1`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE6888`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE7431`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE7E3E`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE8CDE`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE91CC`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE9596`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE95AA`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE971B`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEAB10`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEAE4A`
- [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AED558`
- [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AEE0C7`
- [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AEE599`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF06F7`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF0D1A`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF0DFB`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF0EFB`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF0FA1`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF124A`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF141B`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF14F3`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1569`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF16BB`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF17D8`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1842`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1A3F`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF4C1F`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF4CDD`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF4D40`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF4E65`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF5064`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF508D`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF514C`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF51D4`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF526D`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF52D4`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF560D`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF56CF`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF5736`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF57A3`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF585A`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF58D7`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF5910`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF59CF`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF5A79`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF5B7D`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF5C40`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF5D73`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF5E01`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF5E45`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF5E79`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF5EC6`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF6072`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF61FB`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF62A8`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF63AC`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF644C`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF64B9`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF65EC`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF666F`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF668C`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF673F`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF67CB`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF6809`
- [NtManageHotPatch](../AF/NtManageHotPatch_function_00AF8660.md) at `0x00AF8763`
- [sub_00B18F20](../B1/Unknown_function_00B18F20.md) at `0x00B18F3A`
- [sub_00B19B64](../B1/Unknown_function_00B19B64.md) at `0x00B19B8B`
- [sub_00B2AD32](../B2/Unknown_function_00B2AD32.md) at `0x00B2AD51`
- [sub_00B2E606](../B2/Unknown_function_00B2E606.md) at `0x00B2E610`
- [sub_00B31388](../B3/Unknown_function_00B31388.md) at `0x00B31460`
- [sub_00B334D2](../B3/Unknown_function_00B334D2.md) at `0x00B334EA`
- [sub_00B334D2](../B3/Unknown_function_00B334D2.md) at `0x00B335BB`
- [sub_00B3C988](../B3/Unknown_function_00B3C988.md) at `0x00B3CC7D`
- [sub_00B3C988](../B3/Unknown_function_00B3C988.md) at `0x00B3CD7A`
- [sub_00B3C988](../B3/Unknown_function_00B3C988.md) at `0x00B3D38D`
- [NtSetSystemPowerState](../../pagelk/B7/NtSetSystemPowerState_function_00B70890.md) at `0x00B70938`

### Static image references
- `0x00871E30` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00871E20  4C 8B DC                        mov r11, rsp
00871E23  55                              push rbp
00871E24  53                              push rbx
00871E25  49 8D 6B A1                     lea rbp, [r11 - 0x5f]
00871E29  48 81 EC 98 00 00 00            sub rsp, 0x98
00871E30  48 8B 05 09 89 59 00            mov rax, qword ptr [rip + 0x598909]
00871E37  48 33 C4                        xor rax, rsp
00871E3A  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeSinglePrivilegeCheck(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (152);
    result = (*(unsigned __int64 *)(v_rip + 5867785)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 47) = result;
    return result;
}
```

## 5. (Beta) C Style

```c
void SeSinglePrivilegeCheck(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (152);
    result = (*(uint64_t *)(v_rip + 0x598909)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x2F) = result;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00871E20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00871E20[BB_00871E20]
```
