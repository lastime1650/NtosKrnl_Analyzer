# AslLogCallPrintf

- RVA: `0x0095E4EC`–`0x0095E518` (길이 `44` bytes)
- VA: `0x000000014095E4EC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00092F10`
- 디코드: `12`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **177**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0095E511` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [SdbpCheckApplicationTypeAttributes](../../text/69/SdbpCheckApplicationTypeAttributes_function_0069C93C.md) at `0x0069CC58`
- [SdbpGetPathAppPatchPreRS3](../../text/69/SdbpGetPathAppPatchPreRS3_function_0069CCF0.md) at `0x0069CDA6`
- [SdbpGetPathCustomSdbPreRS3](../../text/69/SdbpGetPathCustomSdbPreRS3_function_0069CE80.md) at `0x0069CF5B`
- [SdbGetMergeRedirectPath](../81/SdbGetMergeRedirectPath_function_0081210C.md) at `0x0081219B`
- [SdbGetMergeRedirectPath](../81/SdbGetMergeRedirectPath_function_0081210C.md) at `0x008121E7`
- [SdbOpenDatabaseEx](../81/SdbOpenDatabaseEx_function_00812284.md) at `0x008122E6`
- [SdbOpenDatabaseEx](../81/SdbOpenDatabaseEx_function_00812284.md) at `0x00812314`
- [SdbOpenDatabaseEx](../81/SdbOpenDatabaseEx_function_00812284.md) at `0x00812381`
- [SdbOpenDatabaseEx](../81/SdbOpenDatabaseEx_function_00812284.md) at `0x008123D5`
- [SdbOpenDatabaseEx](../81/SdbOpenDatabaseEx_function_00812284.md) at `0x00812425`
- [SdbOpenDatabaseEx](../81/SdbOpenDatabaseEx_function_00812284.md) at `0x008124E9`
- [SdbOpenDatabaseEx](../81/SdbOpenDatabaseEx_function_00812284.md) at `0x00812524`
- [SdbpGetFileTimestamp](../81/SdbpGetFileTimestamp_function_00812558.md) at `0x008126A2`
- [SdbpGetFileTimestamp](../81/SdbpGetFileTimestamp_function_00812558.md) at `0x008126F2`
- [SdbpGetManifestedMergeStubAlloc](../81/SdbpGetManifestedMergeStubAlloc_function_0081275C.md) at `0x008127D9`
- [SdbpGetManifestedMergeStubAlloc](../81/SdbpGetManifestedMergeStubAlloc_function_0081275C.md) at `0x0081283C`
- [SdbpGetManifestedMergeStubAlloc](../81/SdbpGetManifestedMergeStubAlloc_function_0081275C.md) at `0x008128CC`
- [SdbpGetManifestedMergeStubAlloc](../81/SdbpGetManifestedMergeStubAlloc_function_0081275C.md) at `0x00812A33`
- [SdbpGetMergeRedirectPathInternal](../81/SdbpGetMergeRedirectPathInternal_function_00812B00.md) at `0x00812C3A`
- [SdbpGetMergeRedirectPathInternal](../81/SdbpGetMergeRedirectPathInternal_function_00812B00.md) at `0x00812C8F`
- [SdbpGetMergeRedirectPathInternal](../81/SdbpGetMergeRedirectPathInternal_function_00812B00.md) at `0x00812CEB`
- [SdbpGetMergeRedirectPathInternal](../81/SdbpGetMergeRedirectPathInternal_function_00812B00.md) at `0x00812DFE`
- [SdbpGetMergeRedirectPathInternal](../81/SdbpGetMergeRedirectPathInternal_function_00812B00.md) at `0x00812EB0`
- [SdbpGetMergeRedirectPathInternal](../81/SdbpGetMergeRedirectPathInternal_function_00812B00.md) at `0x00812F00`
- [SdbpGetMergeRedirectPathInternal](../81/SdbpGetMergeRedirectPathInternal_function_00812B00.md) at `0x00812F74`
- [SdbpGetMergeRedirectPathInternal](../81/SdbpGetMergeRedirectPathInternal_function_00812B00.md) at `0x00813041`
- [SdbpGetMergeSdbsDisabled](../81/SdbpGetMergeSdbsDisabled_function_008130A8.md) at `0x0081310F`
- [SdbpGetMergeSdbsDisabled](../81/SdbpGetMergeSdbsDisabled_function_008130A8.md) at `0x00813156`
- [SdbpSafeAllocAndConcatW](../81/SdbpSafeAllocAndConcatW_function_00813198.md) at `0x00813300`
- [SdbpSafeAllocAndConcatW](../81/SdbpSafeAllocAndConcatW_function_00813198.md) at `0x0081333F`
- [SdbQueryDataEx](../81/SdbQueryDataEx_function_0081363C.md) at `0x0081368A`
- [SdbQueryDataExTagID](../81/SdbQueryDataExTagID_function_008136E0.md) at `0x00813744`
- [SdbQueryDataExTagID](../81/SdbQueryDataExTagID_function_008136E0.md) at `0x00813797`
- [SdbQueryDataExTagID](../81/SdbQueryDataExTagID_function_008136E0.md) at `0x0081387F`
- [SdbQueryDataExTagID](../81/SdbQueryDataExTagID_function_008136E0.md) at `0x008138E2`
- [SdbQueryDataExTagID](../81/SdbQueryDataExTagID_function_008136E0.md) at `0x00813A30`
- [SdbQueryDataExTagID](../81/SdbQueryDataExTagID_function_008136E0.md) at `0x00813A82`
- [SdbReadEntryInformation](../81/SdbReadEntryInformation_function_00813AEC.md) at `0x00813B5C`
- [SdbReadEntryInformation](../81/SdbReadEntryInformation_function_00813AEC.md) at `0x00813BA2`
- [SdbReadEntryInformation](../81/SdbReadEntryInformation_function_00813AEC.md) at `0x00813C07`
- [SdbpCheckContainment](../81/SdbpCheckContainment_function_00813D30.md) at `0x00813DC7`
- [SdbpCheckMatchingDevice](../81/SdbpCheckMatchingDevice_function_00813E20.md) at `0x00813E63`
- [SdbpCheckMatchingDir](../81/SdbpCheckMatchingDir_function_00813EF0.md) at `0x00813F5C`
- [SdbpCheckMatchingFiles](../81/SdbpCheckMatchingFiles_function_00814080.md) at `0x008140FD`
- [SdbpCheckMatchingFiles](../81/SdbpCheckMatchingFiles_function_00814080.md) at `0x0081416A`
- [SdbpCheckMatchingFiles](../81/SdbpCheckMatchingFiles_function_00814080.md) at `0x00814302`
- [SdbpCheckMatchingRegistry](../81/SdbpCheckMatchingRegistry_function_00814320.md) at `0x008143C2`
- [SdbpCheckMatchingRegistryEntry](../81/SdbpCheckMatchingRegistryEntry_function_0081444C.md) at `0x008144F1`
- [SdbpCheckMatchingRegistryEntry](../81/SdbpCheckMatchingRegistryEntry_function_0081444C.md) at `0x0081457C`
- [SdbpCheckMatchingRegistryValue](../81/SdbpCheckMatchingRegistryValue_function_0081462C.md) at `0x0081471B`
- [SdbpCheckMatchingRegistryValue](../81/SdbpCheckMatchingRegistryValue_function_0081462C.md) at `0x00814765`
- [SdbpCheckMatchingText](../81/SdbpCheckMatchingText_function_00814950.md) at `0x008149D7`
- [SdbpCheckMatchingTextEntry](../81/SdbpCheckMatchingTextEntry_function_00814A70.md) at `0x00814AF6`
- [SdbpCheckMatchingTextEntry](../81/SdbpCheckMatchingTextEntry_function_00814A70.md) at `0x00814BEF`
- [SdbpCheckMatchingTextEntry](../81/SdbpCheckMatchingTextEntry_function_00814A70.md) at `0x00814D51`
- [SdbpCheckMatchingTextEntry](../81/SdbpCheckMatchingTextEntry_function_00814A70.md) at `0x00814DA9`
- [SdbpCheckMatchingWildcardFiles](../81/SdbpCheckMatchingWildcardFiles_function_00814E30.md) at `0x00814EE2`
- [SdbpCheckMatchingWildcardFiles](../81/SdbpCheckMatchingWildcardFiles_function_00814E30.md) at `0x00814F29`
- [SdbpCheckMatchingWildcardFiles](../81/SdbpCheckMatchingWildcardFiles_function_00814E30.md) at `0x00815055`
- [SdbpCheckMatchingWildcardFiles](../81/SdbpCheckMatchingWildcardFiles_function_00814E30.md) at `0x00815093`
- [SdbpCheckMatchingWildcardRegistry](../81/SdbpCheckMatchingWildcardRegistry_function_00815110.md) at `0x008151B2`
- [SdbpCheckSdbCapability](../81/SdbpCheckSdbCapability_function_00815570.md) at `0x008155CF`
- [SdbpFindFirstTagWithoutIndex](../81/SdbpFindFirstTagWithoutIndex_function_00815610.md) at `0x00815676`
- [SdbpFindFirstWildcardTagWithoutIndex](../81/SdbpFindFirstWildcardTagWithoutIndex_function_008156C8.md) at `0x0081572E`
- [SdbpFindNextTagWithoutIndex](../81/SdbpFindNextTagWithoutIndex_function_00815784.md) at `0x008157BE`
- [SdbpFindNextWildcardTagWithoutIndex](../81/SdbpFindNextWildcardTagWithoutIndex_function_00815800.md) at `0x0081583A`
- [SdbpGetExeEntryFlags](../81/SdbpGetExeEntryFlags_function_00815A00.md) at `0x00815A5C`
- [SdbpGetMatchingTextAttributes](../81/SdbpGetMatchingTextAttributes_function_00815B38.md) at `0x00815BB3`
- [SdbpGetMatchingTextAttributes](../81/SdbpGetMatchingTextAttributes_function_00815B38.md) at `0x00815D2C`
- [SdbpGetRegistryMatchingAttributes](../81/SdbpGetRegistryMatchingAttributes_function_00815D5C.md) at `0x0081605E`
- [SdbpInitializeSearchDBContext](../81/SdbpInitializeSearchDBContext_function_00816210.md) at `0x008162D8`
- [SdbpResolveMatchingFile](../81/SdbpResolveMatchingFile_function_00816A20.md) at `0x00816AC0`
- [SdbpResolveMatchingFile](../81/SdbpResolveMatchingFile_function_00816A20.md) at `0x00816C66`
- [SdbpResolveMatchingFile](../81/SdbpResolveMatchingFile_function_00816A20.md) at `0x00816CC8`
- [SdbpResolveMatchingFile](../81/SdbpResolveMatchingFile_function_00816A20.md) at `0x00816D71`
- [SdbpFindNextNamedTagHelper](../81/SdbpFindNextNamedTagHelper_function_00816DF8.md) at `0x00816E50`
- [SdbpFindNextNamedTagHelper](../81/SdbpFindNextNamedTagHelper_function_00816DF8.md) at `0x00816EF2`
- [SdbGetBinaryTagData](../81/SdbGetBinaryTagData_function_00816F8C.md) at `0x00816FE0`
- [SdbReadGUIDTag](../81/SdbReadGUIDTag_function_00817000.md) at `0x0081704A`
- [SdbReadQWORDTag](../81/SdbReadQWORDTag_function_0081706C.md) at `0x008170CD`
- [SdbTagIDToTagRef](../81/SdbTagIDToTagRef_function_0081710C.md) at `0x0081715C`
- [SdbpGetProcessHistory](../81/SdbpGetProcessHistory_function_00817250.md) at `0x0081730B`
- [SdbpIsEntryIdAvailableInOtherDb](../81/SdbpIsEntryIdAvailableInOtherDb_function_008173D4.md) at `0x00817476`
- [SdbGuestHostArchsToRuntimePlatformFlag](../81/SdbGuestHostArchsToRuntimePlatformFlag_function_008174A0.md) at `0x008174FD`
- [SdbGuestTargetPlatformFlagsToRuntimePlatformFlags](../81/SdbGuestTargetPlatformFlagsToRuntimePlatformFlags_function_00817550.md) at `0x00817598`
- [SdbpOpenLocalDatabaseEx](../81/SdbpOpenLocalDatabaseEx_function_0081770C.md) at `0x00817817`
- [SdbpOpenLocalDatabaseEx](../81/SdbpOpenLocalDatabaseEx_function_0081770C.md) at `0x00817921`
- [SdbGetPathCustomSdb](../81/SdbGetPathCustomSdb_function_0081795C.md) at `0x008179C7`
- [SdbResolveDatabaseEx](../81/SdbResolveDatabaseEx_function_00817A54.md) at `0x00817B49`
- [SdbResolveDatabaseEx](../81/SdbResolveDatabaseEx_function_00817A54.md) at `0x00817BA3`
- [SdbResolveDatabaseEx](../81/SdbResolveDatabaseEx_function_00817A54.md) at `0x00817BE1`
- [SdbResolveDatabaseEx](../81/SdbResolveDatabaseEx_function_00817A54.md) at `0x00817C5D`
- [SdbResolveDatabaseEx](../81/SdbResolveDatabaseEx_function_00817A54.md) at `0x00817CA1`
- [SdbResolveDatabaseEx](../81/SdbResolveDatabaseEx_function_00817A54.md) at `0x00817CF2`
- [SdbResolveDatabaseEx](../81/SdbResolveDatabaseEx_function_00817A54.md) at `0x00817D31`
- [SdbpGetCustomSdbFileName](../81/SdbpGetCustomSdbFileName_function_00817DA0.md) at `0x00817DE2`
- [SdbpGetPathAppPatch](../81/SdbpGetPathAppPatch_function_00817E30.md) at `0x00817EF5`
- [SdbpGetPathAppraiser](../81/SdbpGetPathAppraiser_function_00817F30.md) at `0x00817FFC`
- [SdbpGetPathCustomSdb](../81/SdbpGetPathCustomSdb_function_00818080.md) at `0x0081812A`
- [SdbpGetPathMergeSource](../81/SdbpGetPathMergeSource_function_00818180.md) at `0x0081823A`
- [SdbpGetPathSystem](../81/SdbpGetPathSystem_function_00818290.md) at `0x00818325`
- [SdbpGetProcessHostGuestArchitectures](../81/SdbpGetProcessHostGuestArchitectures_function_00818350.md) at `0x008183A9`
- [SdbpGetSystemSdbFilePath](../81/SdbpGetSystemSdbFilePath_function_008183F4.md) at `0x00818475`
- [SdbpGetSystemSdbFilePath](../81/SdbpGetSystemSdbFilePath_function_008183F4.md) at `0x008184CF`
- [SdbpGetSystemSdbFilePath](../81/SdbpGetSystemSdbFilePath_function_008183F4.md) at `0x008184F7`
- [SdbpOpenCompressedDatabase](../81/SdbpOpenCompressedDatabase_function_00818524.md) at `0x008185FB`
- [SdbpOpenCompressedDatabase](../81/SdbpOpenCompressedDatabase_function_00818524.md) at `0x00818646`
- [SdbpQueryAppCompatFlagsByExeID](../81/SdbpQueryAppCompatFlagsByExeID_function_00818704.md) at `0x0081876B`
- [SdbpQueryAppCompatFlagsByExeID](../81/SdbpQueryAppCompatFlagsByExeID_function_00818704.md) at `0x008187B2`
- [SdbpCheckAllAttributes](../81/SdbpCheckAllAttributes_function_008187EC.md) at `0x00818A1C`
- [SdbpCheckAllAttributes](../81/SdbpCheckAllAttributes_function_008187EC.md) at `0x00818A56`
- [SdbpCheckAttribute](../81/SdbpCheckAttribute_function_00818A84.md) at `0x00818B2C`
- [SdbMergeIsEntryUpdated](../81/SdbMergeIsEntryUpdated_function_00819158.md) at `0x00819257`
- [SdbMergeIsEntryUpdated](../81/SdbMergeIsEntryUpdated_function_00819158.md) at `0x00819372`
- [SdbMergeIsEntryUpdated](../81/SdbMergeIsEntryUpdated_function_00819158.md) at `0x008193DD`
- [SdbMergeIsEntryUpdated](../81/SdbMergeIsEntryUpdated_function_00819158.md) at `0x00819427`
- [SdbpMergeAreTagValuesEqual](../81/SdbpMergeAreTagValuesEqual_function_00819524.md) at `0x00819629`
- [AslGuidToString_UStr](../81/AslGuidToString_UStr_function_008196DC.md) at `0x0081972E`
- [AslGuidToString_UStr](../81/AslGuidToString_UStr_function_008196DC.md) at `0x008197E3`
- [AslStringAnsiToUnicode](../81/AslStringAnsiToUnicode_function_00819824.md) at `0x008198A5`
- [AslStringAnsiToUnicode](../81/AslStringAnsiToUnicode_function_00819824.md) at `0x008198DF`
- [AslRegistryBuildMachinePath](../81/AslRegistryBuildMachinePath_function_00819CCC.md) at `0x00819D57`
- [AslRegistryBuildUserPath](../81/AslRegistryBuildUserPath_function_00819DB0.md) at `0x00819E04`
- [AslRegistryBuildUserPath](../81/AslRegistryBuildUserPath_function_00819DB0.md) at `0x00819E5E`
- [AslRegistryGetKey](../81/AslRegistryGetKey_function_00819F64.md) at `0x00819FD7`
- [AslRegistryGetString](../81/AslRegistryGetString_function_0081A084.md) at `0x0081A110`
- [AslRegistryGetString](../81/AslRegistryGetString_function_0081A084.md) at `0x0081A150`
- [AslRegistryGetString](../81/AslRegistryGetString_function_0081A084.md) at `0x0081A1BA`
- [AslRegistryGetString](../81/AslRegistryGetString_function_0081A084.md) at `0x0081A1FF`
- [AslRegistryGetUInt32](../81/AslRegistryGetUInt32_function_0081A228.md) at `0x0081A274`
- [AslRegistryGetUInt32_UStr](../81/AslRegistryGetUInt32_UStr_function_0081A2A8.md) at `0x0081A32F`
- [AslRegistryGetUInt32_UStr](../81/AslRegistryGetUInt32_UStr_function_0081A2A8.md) at `0x0081A367`
- [AslRegistryOpenSubKey](../81/AslRegistryOpenSubKey_function_0081A3E0.md) at `0x0081A441`
- [AslFileMappingCreateFromImageView](../81/AslFileMappingCreateFromImageView_function_0081A49C.md) at `0x0081A536`
- [AslFileMappingCreateFromImageView](../81/AslFileMappingCreateFromImageView_function_0081A49C.md) at `0x0081A5B1`
- [AslFileMappingEnsure](../81/AslFileMappingEnsure_function_0081A5EC.md) at `0x0081A692`
- [AslFileMappingEnsureMappedAs](../81/AslFileMappingEnsureMappedAs_function_0081A6BC.md) at `0x0081A761`
- [AslFileMappingGetFileKindDetail](../81/AslFileMappingGetFileKindDetail_function_0081A78C.md) at `0x0081A7F4`
- [AslFileMappingGetImageTypeEx](../81/AslFileMappingGetImageTypeEx_function_0081A950.md) at `0x0081A9D9`
- [AslFileMappingGetImageTypeEx](../81/AslFileMappingGetImageTypeEx_function_0081A950.md) at `0x0081AAAC`
- [AslFileMappingGetImageTypeEx](../81/AslFileMappingGetImageTypeEx_function_0081A950.md) at `0x0081AB09`
- [AslPathCleanUstr](../81/AslPathCleanUstr_function_0081AE0C.md) at `0x0081B08E`
- [AslPathCleanUstr](../81/AslPathCleanUstr_function_0081AE0C.md) at `0x0081B0D2`
- [AslPathCombine](../81/AslPathCombine_function_0081B100.md) at `0x0081B24C`
- [AslPathToNetworkPathNt](../81/AslPathToNetworkPathNt_function_0081B2A4.md) at `0x0081B31A`
- [AslPathToSystemPath](../81/AslPathToSystemPath_function_0081B370.md) at `0x0081B3D6`
- [AslPathToSystemPathBuf](../81/AslPathToSystemPathBuf_function_0081B430.md) at `0x0081B48D`
- [AslPathToSystemPathBuf](../81/AslPathToSystemPathBuf_function_0081B430.md) at `0x0081B4C5`
- [AslPathWildcardFindFirst](../81/AslPathWildcardFindFirst_function_0081B534.md) at `0x0081B5F0`
- [AslPathWildcardFindFirst](../81/AslPathWildcardFindFirst_function_0081B534.md) at `0x0081B626`
- [AslPathWildcardFindFirst](../81/AslPathWildcardFindFirst_function_0081B534.md) at `0x0081B919`
- [AslPathWildcardFindFirst](../81/AslPathWildcardFindFirst_function_0081B534.md) at `0x0081BAC8`
- [AslPathWildcardFindNext](../81/AslPathWildcardFindNext_function_0081BB2C.md) at `0x0081BC2D`
- [AslPathWildcardFindNext](../81/AslPathWildcardFindNext_function_0081BB2C.md) at `0x0081BC8F`
- [AslPathWildcardFindNext](../81/AslPathWildcardFindNext_function_0081BB2C.md) at `0x0081BEFA`
- [AslPathWildcardFindNext](../81/AslPathWildcardFindNext_function_0081BB2C.md) at `0x0081BF2A`
- [AslPathWildcardFindNext](../81/AslPathWildcardFindNext_function_0081BB2C.md) at `0x0081C13B`
- [AslPathWildcardFindNext](../81/AslPathWildcardFindNext_function_0081BB2C.md) at `0x0081C21D`
- [AslPathWildcardFindNext](../81/AslPathWildcardFindNext_function_0081BB2C.md) at `0x0081C242`
- [AslpPathWildcardAllocMatchNode](../81/AslpPathWildcardAllocMatchNode_function_0081C620.md) at `0x0081C816`
- [AslpPathWildcardMakeLeaves](../81/AslpPathWildcardMakeLeaves_function_0081C960.md) at `0x0081CADE`
- [AslEnvExpandStrings](../81/AslEnvExpandStrings_function_0081CCF4.md) at `0x0081CE0F`
- [AslEnvExpandStrings2](../81/AslEnvExpandStrings2_function_0081CECC.md) at `0x0081CF7C`
- [AslEnvExpandStrings2](../81/AslEnvExpandStrings2_function_0081CECC.md) at `0x0081D082`
- [AslEnvGetProcessWowInfo](../81/AslEnvGetProcessWowInfo_function_0081D0A8.md) at `0x0081D11A`
- [AslEnvGetSysNativeDirPathForGuestBuf](../81/AslEnvGetSysNativeDirPathForGuestBuf_function_0081D184.md) at `0x0081D274`
- [AslEnvGetSystem32DirPathBuf](../81/AslEnvGetSystem32DirPathBuf_function_0081D2BC.md) at `0x0081D380`
- [AslpEnvResolveVars](../81/AslpEnvResolveVars_function_0081D608.md) at `0x0081D7A9`
- [AslpEnvResolveVars](../81/AslpEnvResolveVars_function_0081D608.md) at `0x0081D85A`
- [AslFileAllocAndGetAttributes](../81/AslFileAllocAndGetAttributes_function_0081D8EC.md) at `0x0081DA27`
- [AslFileAllocAndGetAttributes](../81/AslFileAllocAndGetAttributes_function_0081D8EC.md) at `0x0081DB19`
- [AslFileAllocAndGetAttributes](../81/AslFileAllocAndGetAttributes_function_0081D8EC.md) at `0x0081DD6E`
- [AslpFileGet16BitDescription](../81/AslpFileGet16BitDescription_function_0081DE94.md) at `0x0081DF0F`
- [AslpFileGet16BitDescription](../81/AslpFileGet16BitDescription_function_0081DE94.md) at `0x0081DF48`
- [AslpFileGet16BitModuleName](../81/AslpFileGet16BitModuleName_function_0081DF78.md) at `0x0081DFF3`
- [AslpFileGet16BitModuleName](../81/AslpFileGet16BitModuleName_function_0081DF78.md) at `0x0081E02C`
- [AslpFileGetChecksum](../81/AslpFileGetChecksum_function_0081E05C.md) at `0x0081E11B`
- [AslpFileGetChecksumAttributes](../81/AslpFileGetChecksumAttributes_function_0081E130.md) at `0x0081E180`
- [AslpFileGetChecksumAttributes](../81/AslpFileGetChecksumAttributes_function_0081E130.md) at `0x0081E1F8`
- [AslpFileGetClrVersion](../81/AslpFileGetClrVersion_function_0081E388.md) at `0x0081E3D7`
- [AslpFileGetClrVersion](../81/AslpFileGetClrVersion_function_0081E388.md) at `0x0081E460`
- [AslpFileGetClrVersion](../81/AslpFileGetClrVersion_function_0081E388.md) at `0x0081E524`
- [AslpFileGetClrVersionAttribute](../81/AslpFileGetClrVersionAttribute_function_0081E54C.md) at `0x0081E5B9`
- [AslpFileGetCrcChecksum](../81/AslpFileGetCrcChecksum_function_0081E6DC.md) at `0x0081E78D`
- [AslpFileGetCrcChecksum](../81/AslpFileGetCrcChecksum_function_0081E6DC.md) at `0x0081E7B7`
- [AslpFileGetCrcChecksumBoot](../81/AslpFileGetCrcChecksumBoot_function_0081E7D4.md) at `0x0081E861`
- [AslpFileGetCrcChecksumBoot](../81/AslpFileGetCrcChecksumBoot_function_0081E7D4.md) at `0x0081E899`
- [AslpFileGetCrcChecksumBoot](../81/AslpFileGetCrcChecksumBoot_function_0081E7D4.md) at `0x0081E906`
- [AslpFileGetCrcChecksumBoot](../81/AslpFileGetCrcChecksumBoot_function_0081E7D4.md) at `0x0081EA2F`
- [AslpFileGetCrcChecksumBoot](../81/AslpFileGetCrcChecksumBoot_function_0081E7D4.md) at `0x0081EACC`
- [AslpFileGetExeWrapper](../81/AslpFileGetExeWrapper_function_0081EAF4.md) at `0x0081EB59`
- [AslpFileGetExeWrapper](../81/AslpFileGetExeWrapper_function_0081EAF4.md) at `0x0081EBC9`
- [AslpFileGetExeWrapper](../81/AslpFileGetExeWrapper_function_0081EAF4.md) at `0x0081EBE6`
- [AslpFileGetExeWrapper](../81/AslpFileGetExeWrapper_function_0081EAF4.md) at `0x0081EC62`
- [AslpFileGetExeWrapperAttribute](../81/AslpFileGetExeWrapperAttribute_function_0081EC80.md) at `0x0081ECC5`
- [AslpFileGetExportName](../81/AslpFileGetExportName_function_0081ED30.md) at `0x0081EDA5`
- [AslpFileGetFileKindDetailAttribute](../81/AslpFileGetFileKindDetailAttribute_function_0081EDFC.md) at `0x0081EE3B`
- [AslpFileGetHeaderAttributesNE](../81/AslpFileGetHeaderAttributesNE_function_0081EE80.md) at `0x0081EED0`
- [AslpFileGetHeaderAttributesPE](../81/AslpFileGetHeaderAttributesPE_function_0081F028.md) at `0x0081F096`
- [AslpFileGetImageCodeSectionHeader](../81/AslpFileGetImageCodeSectionHeader_function_0081F298.md) at `0x0081F343`
- [AslpFileGetImageCodeSectionHeader](../81/AslpFileGetImageCodeSectionHeader_function_0081F298.md) at `0x0081F3E0`
- [AslpFileGetImageCodeSectionHeader](../81/AslpFileGetImageCodeSectionHeader_function_0081F298.md) at `0x0081F405`
- [AslpFileGetImageNtHeader](../81/AslpFileGetImageNtHeader_function_0081F434.md) at `0x0081F476`
- [AslpFileGetImageNtHeader](../81/AslpFileGetImageNtHeader_function_0081F434.md) at `0x0081F4EB`
- [AslpFileGetImageNtHeader](../81/AslpFileGetImageNtHeader_function_0081F434.md) at `0x0081F515`
- [AslpFileGetImageResourceDirectoryRoot](../81/AslpFileGetImageResourceDirectoryRoot_function_0081F53C.md) at `0x0081F582`
- [AslpFileGetImageResourceDirectoryRoot](../81/AslpFileGetImageResourceDirectoryRoot_function_0081F53C.md) at `0x0081F614`
- [AslpFileGetImageResourceDirectoryRoot](../81/AslpFileGetImageResourceDirectoryRoot_function_0081F53C.md) at `0x0081F6FA`
- [AslpFileGetNtHeaderAttributes](../81/AslpFileGetNtHeaderAttributes_function_0081F724.md) at `0x0081F784`
- [AslpFileGetNtHeaderAttributes](../81/AslpFileGetNtHeaderAttributes_function_0081F724.md) at `0x0081F857`
- [AslpFileGetPeExportNameAttribute](../81/AslpFileGetPeExportNameAttribute_function_0081F884.md) at `0x0081F8CF`
- [AslpFileGetVersionAttributes](../81/AslpFileGetVersionAttributes_function_0081F968.md) at `0x0081F9E7`
- [AslpFileGetVersionAttributes](../81/AslpFileGetVersionAttributes_function_0081F968.md) at `0x0081FA30`
- [AslpFileGetVersionBlock](../81/AslpFileGetVersionBlock_function_0081FA50.md) at `0x0081FB03`
- [AslpFileGetVersionBlock](../81/AslpFileGetVersionBlock_function_0081FA50.md) at `0x0081FC90`
- [AslpFileGetVersionBlock](../81/AslpFileGetVersionBlock_function_0081FA50.md) at `0x0081FCB2`
- [AslpFileGetVersionBlock](../81/AslpFileGetVersionBlock_function_0081FA50.md) at `0x0081FD2F`
- [AslpFileGetVersionBlock](../81/AslpFileGetVersionBlock_function_0081FA50.md) at `0x0081FD82`
- [AslpFileGetVersionBlock](../81/AslpFileGetVersionBlock_function_0081FA50.md) at `0x0081FDB6`
- [AslpFileGetVersionBlock](../81/AslpFileGetVersionBlock_function_0081FA50.md) at `0x0081FF23`
- [AslpFileGetVersionBlock](../81/AslpFileGetVersionBlock_function_0081FA50.md) at `0x0081FF5D`
- [AslpFileGetVersionBlockFromResourceRoot](../81/AslpFileGetVersionBlockFromResourceRoot_function_0081FF98.md) at `0x00820072`
- [AslpFileGetVersionBlockFromResourceRoot](../81/AslpFileGetVersionBlockFromResourceRoot_function_0081FF98.md) at `0x0082022B`
- [AslpFileGetVersionBlockImageOnly](../82/AslpFileGetVersionBlockImageOnly_function_00820260.md) at `0x008202F0`
- [AslpFileGetVersionBlockImageOnly](../82/AslpFileGetVersionBlockImageOnly_function_00820260.md) at `0x00820359`
- [AslpFileGetVersionBlockImageOnly](../82/AslpFileGetVersionBlockImageOnly_function_00820260.md) at `0x008203E9`
- [AslpFileGetVersionBlockImageOnly](../82/AslpFileGetVersionBlockImageOnly_function_00820260.md) at `0x00820412`
- [AslpFileGetVersionBlockImageOnly](../82/AslpFileGetVersionBlockImageOnly_function_00820260.md) at `0x008204CF`
- [AslpFileHasActiveMarkWrapper](../82/AslpFileHasActiveMarkWrapper_function_00820504.md) at `0x00820619`
- [AslpFileIsArm64XBinary](../82/AslpFileIsArm64XBinary_function_008206B0.md) at `0x0082070E`
- [AslpFileIsArm64XBinary](../82/AslpFileIsArm64XBinary_function_008206B0.md) at `0x0082080A`
- [AslpFileMakeStringVersionAttributes](../82/AslpFileMakeStringVersionAttributes_function_00820964.md) at `0x00820A22`
- [AslpFileQuery16BitDescription](../82/AslpFileQuery16BitDescription_function_00820B70.md) at `0x00820CB3`
- [AslpFileQuery16BitDescription](../82/AslpFileQuery16BitDescription_function_00820B70.md) at `0x00820CDD`
- [AslpFileQuery16BitModuleName](../82/AslpFileQuery16BitModuleName_function_00820D08.md) at `0x00820E9E`
- [AslpFileQuery16BitModuleName](../82/AslpFileQuery16BitModuleName_function_00820D08.md) at `0x00820EC8`
- [AslpFileQueryExportName](../82/AslpFileQueryExportName_function_00820EF8.md) at `0x00820F80`
- [AslpFileQueryExportName](../82/AslpFileQueryExportName_function_00820EF8.md) at `0x0082104C`
- [AslpFileQueryExportName](../82/AslpFileQueryExportName_function_00820EF8.md) at `0x008210A9`
- [AslpFileQueryExportName](../82/AslpFileQueryExportName_function_00820EF8.md) at `0x0082110C`
- [AslpFileQueryVersionString](../82/AslpFileQueryVersionString_function_0082113C.md) at `0x008212EC`
- [AslpFileLargeEnsureLargeFileMapping](../82/AslpFileLargeEnsureLargeFileMapping_function_00821538.md) at `0x0082164E`
- [AslpFileLargeGetChecksum](../82/AslpFileLargeGetChecksum_function_008216E8.md) at `0x008217AA`
- [AslpFileLargeGetChecksumAttributes](../82/AslpFileLargeGetChecksumAttributes_function_008217C8.md) at `0x0082180E`
- [AslpFileLargeGetChecksumAttributes](../82/AslpFileLargeGetChecksumAttributes_function_008217C8.md) at `0x00821873`
- [AslpFileLargeGetCrcChecksum](../82/AslpFileLargeGetCrcChecksum_function_008218BC.md) at `0x00821968`
- [AslpFileLargeGetCrcChecksum](../82/AslpFileLargeGetCrcChecksum_function_008218BC.md) at `0x0082198E`
- [AslpFileLargeGetCrcChecksum](../82/AslpFileLargeGetCrcChecksum_function_008218BC.md) at `0x008219AE`
- [AslpFileLargeGetCrcChecksum](../82/AslpFileLargeGetCrcChecksum_function_008218BC.md) at `0x008219CC`
- [AslpFileLargeGetCrcChecksum](../82/AslpFileLargeGetCrcChecksum_function_008218BC.md) at `0x008219E8`
- [AslpFileLargeGetCrcChecksum](../82/AslpFileLargeGetCrcChecksum_function_008218BC.md) at `0x00821A02`
- [AslpFileLargeGetCrcChecksum](../82/AslpFileLargeGetCrcChecksum_function_008218BC.md) at `0x00821A54`
- [AslpFileLargeMapCreate](../82/AslpFileLargeMapCreate_function_00821A88.md) at `0x00821B4A`
- [AslpFileLargeMapCreate](../82/AslpFileLargeMapCreate_function_00821A88.md) at `0x00821BEB`
- [SdbGetDatabaseMatch](SdbGetDatabaseMatch_function_00958240.md) at `0x00958305`
- [SdbGetDatabaseMatch](SdbGetDatabaseMatch_function_00958240.md) at `0x009583B4`
- [SdbGetDatabaseMatch](SdbGetDatabaseMatch_function_00958240.md) at `0x0095840A`
- [AslStringDuplicate](AslStringDuplicate_function_00958604.md) at `0x009586F5`
- [AslStringDuplicate](AslStringDuplicate_function_00958604.md) at `0x00958731`
- [AslStringUpcaseToMultiByteN](AslStringUpcaseToMultiByteN_function_0095965C.md) at `0x00959729`
- [AslStringUpcaseToMultiByteN](AslStringUpcaseToMultiByteN_function_0095965C.md) at `0x0095977E`
- [AslStringUpcaseToMultiByteN](AslStringUpcaseToMultiByteN_function_0095965C.md) at `0x009597A2`
- [SdbpCreateSearchPathPartsFromPath](SdbpCreateSearchPathPartsFromPath_function_0095A238.md) at `0x0095A2B5`
- [SdbpOpenDatabaseInMemory](SdbpOpenDatabaseInMemory_function_0095A574.md) at `0x0095A5C3`
- [SdbpOpenDatabaseInMemory](SdbpOpenDatabaseInMemory_function_0095A574.md) at `0x0095A60E`
- [SdbpOpenDatabaseInMemory](SdbpOpenDatabaseInMemory_function_0095A574.md) at `0x0095A667`
- [SdbReleaseDatabase](SdbReleaseDatabase_function_0095B57C.md) at `0x0095B59E`
- [SdbReleaseDatabase](SdbReleaseDatabase_function_0095B57C.md) at `0x0095B5FF`
- [SdbReleaseDatabase](SdbReleaseDatabase_function_0095B57C.md) at `0x0095B651`
- [SdbGetDatabaseEdition](SdbGetDatabaseEdition_function_0095BBE4.md) at `0x0095BC4E`
- [SdbInitDatabaseInMemory](SdbInitDatabaseInMemory_function_0095BC5C.md) at `0x0095BC99`
- [SdbInitDatabaseInMemory](SdbInitDatabaseInMemory_function_0095BC5C.md) at `0x0095BD0F`
- [SdbpGetIndex](SdbpGetIndex_function_0095BF94.md) at `0x0095C011`
- [SdbpGetFirstIndexedRecord](SdbpGetFirstIndexedRecord_function_0095C0C4.md) at `0x0095C18D`
- [SdbFindFirstStringIndexedTag](SdbFindFirstStringIndexedTag_function_0095C1D8.md) at `0x0095C29A`
- [SdbGetIndex](SdbGetIndex_function_0095C3C4.md) at `0x0095C491`
- [SdbReadDWORDTag](SdbReadDWORDTag_function_0095D408.md) at `0x0095D495`
- [InitOnceScanIndexes](InitOnceScanIndexes_function_0095D4C0.md) at `0x0095D696`
- [InitOnceScanIndexes](InitOnceScanIndexes_function_0095D4C0.md) at `0x0095D6C5`
- [InitOnceScanIndexes](InitOnceScanIndexes_function_0095D4C0.md) at `0x0095D6FA`
- [SdbpGetNextTagId](SdbpGetNextTagId_function_0095D740.md) at `0x0095D7D4`
- [SdbFindNextTag](SdbFindNextTag_function_0095D7F4.md) at `0x0095D888`
- [SdbReadWORDTag](SdbReadWORDTag_function_0095D898.md) at `0x0095D92A`
- [SdbpGetMappedStringFromTable](SdbpGetMappedStringFromTable_function_0095DA0C.md) at `0x0095DA63`
- [SdbpGetStringTableItemFromStringRef](SdbpGetStringTableItemFromStringRef_function_0095DA74.md) at `0x0095DB5A`
- [SdbpGetStringTableItemFromStringRef](SdbpGetStringTableItemFromStringRef_function_0095DA74.md) at `0x0095DB7A`
- [SdbpGetStringTableItemFromStringRef](SdbpGetStringTableItemFromStringRef_function_0095DA74.md) at `0x0095DBBB`
- [SdbpGetStringTableItemFromStringRef](SdbpGetStringTableItemFromStringRef_function_0095DA74.md) at `0x0095DBE3`
- [SdbpGetMappedTagData](SdbpGetMappedTagData_function_0095DD24.md) at `0x0095DD79`
- [SdbpGetMappedTagData](SdbpGetMappedTagData_function_0095DD24.md) at `0x0095DD99`
- [SdbGetStringTagPtr](SdbGetStringTagPtr_function_0095DDA8.md) at `0x0095DE2C`
- [SdbpFindFirstIndexedWildCardTag](SdbpFindFirstIndexedWildCardTag_function_0095DE58.md) at `0x0095E002`
- [SdbpFindFirstIndexedWildCardTag](SdbpFindFirstIndexedWildCardTag_function_0095DE58.md) at `0x0095E047`
- [SdbpFindFirstIndexedWildCardTag](SdbpFindFirstIndexedWildCardTag_function_0095DE58.md) at `0x0095E067`
- [SdbpReadTagData](SdbpReadTagData_function_0095E170.md) at `0x0095E200`
- [SdbpReadTagData](SdbpReadTagData_function_0095E170.md) at `0x0095E222`
- [SdbGetTagDataSize](SdbGetTagDataSize_function_0095E230.md) at `0x0095E2DD`
- [SdbGetTagDataSize](SdbGetTagDataSize_function_0095E230.md) at `0x0095E33A`
- [SdbGetTagFromTagID](SdbGetTagFromTagID_function_0095E3C0.md) at `0x0095E401`
- [SdbGetTagFromTagID](SdbGetTagFromTagID_function_0095E3C0.md) at `0x0095E41F`
- [SdbGetTagFromTagID](SdbGetTagFromTagID_function_0095E3C0.md) at `0x0095E452`
- [SdbpReadMappedData](SdbpReadMappedData_function_0095E460.md) at `0x0095E4AD`
- [SdbpReadMappedData](SdbpReadMappedData_function_0095E460.md) at `0x0095E4DC`
- [SdbGetNextChild](SdbGetNextChild_function_0095E520.md) at `0x0095E5D2`
- [SdbGetNextChild](SdbGetNextChild_function_0095E520.md) at `0x0095E600`
- [SdbGetFirstChild](SdbGetFirstChild_function_0095E610.md) at `0x0095E6A0`
- [SdbpGetTagHeadSize](SdbpGetTagHeadSize_function_0095E6B0.md) at `0x0095E761`
- [SdbpGetTagHeadSize](SdbpGetTagHeadSize_function_0095E6B0.md) at `0x0095E791`
- [SdbpReadStringRef](SdbpReadStringRef_function_0095E7A0.md) at `0x0095E81D`
- [SdbpReadStringRef](SdbpReadStringRef_function_0095E7A0.md) at `0x0095E83F`
- [SdbMakeIndexKeyFromStringEx](SdbMakeIndexKeyFromStringEx_function_0095E9F4.md) at `0x0095EAC4`
- [SdbGetDatabaseID](../A7/SdbGetDatabaseID_function_00A7EB20.md) at `0x00A7EBF5`
- [SdbGetDatabaseID](../A7/SdbGetDatabaseID_function_00A7EB20.md) at `0x00A7EC19`
- [SdbReadBinaryTag](../A7/SdbReadBinaryTag_function_00A7EC28.md) at `0x00A7ECA2`
- [SdbReadBinaryTag](../A7/SdbReadBinaryTag_function_00A7EC28.md) at `0x00A7ECD8`
- [SdbpFindMatchingName](../A9/SdbpFindMatchingName_function_00A91508.md) at `0x00A915C5`
- [SdbpFindMatchingName](../A9/SdbpFindMatchingName_function_00A91508.md) at `0x00A915F5`
- [SdbpGetNextIndexedRecord](../A9/SdbpGetNextIndexedRecord_function_00A91608.md) at `0x00A916B8`
- [InitOnceGetStringTableOffset](../A9/InitOnceGetStringTableOffset_function_00A97EA0.md) at `0x00A97EF5`
- [InitOnceGetStringTableOffset](../A9/InitOnceGetStringTableOffset_function_00A97EA0.md) at `0x00A97F17`
- [SdbpCreateSearchDBContext](../A9/SdbpCreateSearchDBContext_function_00A9D544.md) at `0x00A9D5EB`
- [SdbpCreateSearchDBContext](../A9/SdbpCreateSearchDBContext_function_00A9D544.md) at `0x00A9D664`
- [SdbpCheckExe](../AB/SdbpCheckExe_function_00AB31A0.md) at `0x00AB3244`
- [SdbpSearchDB](../AB/SdbpSearchDB_function_00AB3294.md) at `0x00AB3327`
- [SdbpSearchDB](../AB/SdbpSearchDB_function_00AB3294.md) at `0x00AB340D`
- [SdbGetEntryFlags](../AB/SdbGetEntryFlags_function_00ABD3E0.md) at `0x00ABD433`
- [AslGuidToString](../AB/AslGuidToString_function_00ABD4AC.md) at `0x00ABD557`
- [AslPathSplit](../AB/AslPathSplit_function_00ABE87C.md) at `0x00ABE94A`
- [SdbpValidateRootTagSizes](../AC/SdbpValidateRootTagSizes_function_00AC5280.md) at `0x00AC5424`
- [SdbpFindFirstNamedTagHelper](../AD/SdbpFindFirstNamedTagHelper_function_00AD4D2C.md) at `0x00AD4DE7`
- [SdbpValidateAndApplyCompatFlags](../AF/SdbpValidateAndApplyCompatFlags_function_00AF93D8.md) at `0x00AF942B`
- [SdbpValidateAndApplyCompatFlags](../AF/SdbpValidateAndApplyCompatFlags_function_00AF93D8.md) at `0x00AF9475`
- [SdbpValidateAndApplyCompatFlags](../AF/SdbpValidateAndApplyCompatFlags_function_00AF93D8.md) at `0x00AF94C7`
- [AslpFileMappingGetFileKind](../AF/AslpFileMappingGetFileKind_function_00AF950C.md) at `0x00AF9630`
- [AslpFileMappingGetFileKind](../AF/AslpFileMappingGetFileKind_function_00AF950C.md) at `0x00AF9662`
- [AslpFileVerQueryBlock](../AF/AslpFileVerQueryBlock_function_00AF9694.md) at `0x00AF96EA`
- [AslpFileVerQueryBlock](../AF/AslpFileVerQueryBlock_function_00AF9694.md) at `0x00AF9724`
- [SdbReleaseDatabase$filt$0](../B0/SdbReleaseDatabase_filt_0_function_00B0FC8F.md) at `0x00B0FD14`
- [sub_00B26AF0](../B2/Unknown_function_00B26AF0.md) at `0x00B26B0D`
- [sub_00B26AF0](../B2/Unknown_function_00B26AF0.md) at `0x00B26B4F`
- [sub_00B26AF0](../B2/Unknown_function_00B26AF0.md) at `0x00B26B86`
- [sub_00B26AF0](../B2/Unknown_function_00B26AF0.md) at `0x00B26BCB`
- [sub_00B27968](../B2/Unknown_function_00B27968.md) at `0x00B27A70`
- [sub_00B27B86](../B2/Unknown_function_00B27B86.md) at `0x00B27BD3`
- [sub_00B27B86](../B2/Unknown_function_00B27B86.md) at `0x00B27C67`
- [sub_00B27B86](../B2/Unknown_function_00B27B86.md) at `0x00B27CBA`
- [sub_00B488F0](../B4/Unknown_function_00B488F0.md) at `0x00B48919`
- [sub_00B488F0](../B4/Unknown_function_00B488F0.md) at `0x00B489FE`

### Static image references
- `0x0095E4F5` → RVA `0x00EF0DA8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0095E511` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0095E4EC  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0095E4F1  48 83 EC 48                     sub rsp, 0x48
0095E4F5  48 8B 05 AC 28 59 00            mov rax, qword ptr [rip + 0x5928ac]
0095E4FC  48 85 C0                        test rax, rax
0095E4FF  75 06                           jne 0x14095e507
0095E501  48 83 C4 48                     add rsp, 0x48
0095E505  C3                              ret
0095E506  CC                              int3
0095E507  4C 8D 54 24 70                  lea r10, [rsp + 0x70]
0095E50C  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
0095E511  E8 BA C5 D5 FF                  call 0x1406baad0
0095E516  EB E9                           jmp 0x14095e501
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AslLogCallPrintf(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (72);
    if (*(unsigned __int64 *)(v_rip + 5843116) != 0) goto loc_0095E507;
loc_0095E501:
    v_rsp = (v_rsp) + (72);
    return *(unsigned __int64 *)(v_rip + 5843116);
loc_0095E507:
    v_stack_p20 = a5;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    goto loc_0095E501;
}
```

## 5. (Beta) C Style

```c
int64_t AslLogCallPrintf(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p20;

    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (72);
    if (*(uint64_t *)(v_rip + 0x5928AC) != 0) goto loc_0095E507;
loc_0095E501:
    local_rsp = (local_rsp) + (72);
    return *(uint64_t *)(v_rip + 0x5928AC);
loc_0095E507:
    v_stack_p20 = Arg5;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    goto loc_0095E501;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0095E4EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0095E4EC[BB_0095E4EC]
  bb_0095E501[BB_0095E501]
  bb_0095E506[BB_0095E506]
  bb_0095E507[BB_0095E507]
  bb_0095E4EC -->|branch| bb_0095E507
  bb_0095E4EC -->|fallthrough| bb_0095E501
  bb_0095E506 -->|flow| bb_0095E507
  bb_0095E507 -->|branch| bb_0095E501
```
