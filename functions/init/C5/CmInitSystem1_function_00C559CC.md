# CmInitSystem1

- RVA: `0x00C559CC`–`0x00C563DB` (길이 `2,575` bytes)
- VA: `0x0000000140C559CC`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D129C`
- 디코드: `596`개 명령, `2,575/2,575` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **96**; 고유 호출 대상: **59**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **68**

### Outgoing calls
- `0x00C55A37` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C55A4F` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C55A67` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x00C55A73` → [CmpInitializeParseContext](../../page/87/CmpInitializeParseContext_function_008767F0.md) (function, `0x008767F0`)
- `0x00C55AEA` → [CmpInitializeRegistryNames](CmpInitializeRegistryNames_function_00C5AEC8.md) (function, `0x00C5AEC8`)
- `0x00C55AEF` → [CmpInitGlobalQuotaAllowed](CmpInitGlobalQuotaAllowed_function_00C59ACC.md) (function, `0x00C59ACC`)
- `0x00C55B4F` → [Feature_Servicing_CmpRegistryLockToCacheAwarePushlock__private_IsEnabledDeviceUsageNoInline](../../text/66/Feature_Servicing_CmpRegistryLockToCacheAwarePushlock__private_IsEnabledDeviceUsageNoInline_function_0066A394.md) (function, `0x0066A394`)
- `0x00C55B6C` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x00C55B84` → [ExAllocateCacheAwarePushLock](../../text/4C/ExAllocateCacheAwarePushLock_function_004C68C0.md) (function, `0x004C68C0`)
- `0x00C55BEC` → [CmpInitializeNameCache](../../page/7E/CmpInitializeNameCache_function_007EAE0C.md) (function, `0x007EAE0C`)
- `0x00C55C2A` → [ExInitializeLookasideListExInternal](../../text/46/ExInitializeLookasideListExInternal_function_00468890.md) (function, `0x00468890`)
- `0x00C55C2F` → [CmpInitSIDToHiveMapping](../../page/7E/CmpInitSIDToHiveMapping_function_007EBA2C.md) (function, `0x007EBA2C`)
- `0x00C55C34` → [CmpAdminSystemSecurityDescriptor](../../page/7E/CmpAdminSystemSecurityDescriptor_function_007EBED8.md) (function, `0x007EBED8`)
- `0x00C55C40` → [CmpInitializeTrustedInstallerSid](CmpInitializeTrustedInstallerSid_function_00C5B108.md) (function, `0x00C5B108`)
- `0x00C55C45` → [CmpInitializeDelayedCloseTable](../../page/7E/CmpInitializeDelayedCloseTable_function_007EDA34.md) (function, `0x007EDA34`)
- `0x00C55C4A` → [CmpInitCallbacks](../../page/7E/CmpInitCallbacks_function_007E19A0.md) (function, `0x007E19A0`)
- `0x00C55C4F` → [CmpInitializeMachineHiveLoadedCallbacks](../../page/7E/CmpInitializeMachineHiveLoadedCallbacks_function_007E1EA0.md) (function, `0x007E1EA0`)
- `0x00C55C54` → [CmpInitializeFreezeThaw](../../page/7E/CmpInitializeFreezeThaw_function_007E86B8.md) (function, `0x007E86B8`)
- `0x00C55C59` → [HvInitializeHashLibrary](../../page/7E/HvInitializeHashLibrary_function_007EDC44.md) (function, `0x007EDC44`)
- `0x00C55C5E` → [CmpValidateGlobalFlushControlFlags](../../page/7E/CmpValidateGlobalFlushControlFlags_function_007E7F50.md) (function, `0x007E7F50`)
- `0x00C55C63` → [CmpInitializeGlobalKeyLockTracker](../../page/7E/CmpInitializeGlobalKeyLockTracker_function_007EDE50.md) (function, `0x007EDE50`)
- `0x00C55C68` → [CmpInitializeTransactions](CmpInitializeTransactions_function_00C5B18C.md) (function, `0x00C5B18C`)
- `0x00C55C6D` → [CmpVolumeManagerInitialize](../../page/7E/CmpVolumeManagerInitialize_function_007E8B38.md) (function, `0x007E8B38`)
- `0x00C55C87` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C55C90` → [CmpHashUnicodeComponent](../../page/84/CmpHashUnicodeComponent_function_0084AC24.md) (function, `0x0084AC24`)
- `0x00C55CA0` → [CmpCreateObjectTypes](CmpCreateObjectTypes_function_00C57780.md) (function, `0x00C57780`)
- `0x00C55CBB` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C55CC1` → [CmpInitializeLightWeightTransactionType](../../page/7E/CmpInitializeLightWeightTransactionType_function_007EE204.md) (function, `0x007EE204`)
- `0x00C55CDF` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C55CE5` → [CmpInitializeRegistryProcess](../../page/7E/CmpInitializeRegistryProcess_function_007E8180.md) (function, `0x007E8180`)
- `0x00C55D03` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C55D0D` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (function, `0x00BC98E0`)
- `0x00C55D12` → [CmpLockRegistryExclusive](../../page/84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x00C55D1C` → [CmpInitializePreloadedHives](CmpInitializePreloadedHives_function_00C584D4.md) (function, `0x00C584D4`)
- `0x00C55D64` → [CmpCreateHive](../../page/87/CmpCreateHive_function_00879DF0.md) (function, `0x00879DF0`)
- `0x00C55D86` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C55D98` → [CmpInitializeKcbCache](../../page/87/CmpInitializeKcbCache_function_00878208.md) (function, `0x00878208`)
- `0x00C55DB6` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C55DBC` → [CmpCreateRegistryRoot](CmpCreateRegistryRoot_function_00C57880.md) (function, `0x00C57880`)
- `0x00C55DD8` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C55DE0` → [CmpInitSiloSupport](../../page/7E/CmpInitSiloSupport_function_007E5B94.md) (function, `0x007E5B94`)
- `0x00C55DFE` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C55E04` → [CmpHiveRootSecurityDescriptor](../../page/7E/CmpHiveRootSecurityDescriptor_function_007ED104.md) (function, `0x007ED104`)
- `0x00C55E5A` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x00C55E6B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C55E85` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C55E90` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00C55EE3` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x00C55EF4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C55F0E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C55F19` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00C55F7E` → [ObOpenObjectByName](../../page/89/ObOpenObjectByName_function_00899F50.md) (function, `0x00899F50`)
- `0x00C55F8F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C55F9D` → [CmpCleanupParseContext](../../page/87/CmpCleanupParseContext_function_00876910.md) (function, `0x00876910`)
- `0x00C55FB5` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C55FC2` → [CmpCleanupParseContext](../../page/87/CmpCleanupParseContext_function_00876910.md) (function, `0x00876910`)
- `0x00C55FCC` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00C5601F` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x00C56030` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C5604A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C56055` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00C56064` → [CmpInitializeLoadOptions](../../text/66/CmpInitializeLoadOptions_function_0066A228.md) (function, `0x0066A228`)
- `0x00C5606F` → [CmpInitializePreloadedHives](CmpInitializePreloadedHives_function_00C584D4.md) (function, `0x00C584D4`)
- `0x00C5608D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C5609C` → [CmpCreateControlSet](CmpCreateControlSet_function_00C56910.md) (function, `0x00C56910`)
- `0x00C560BA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C56139` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C5617E` → [CmpCreateHive](../../page/87/CmpCreateHive_function_00879DF0.md) (function, `0x00879DF0`)
- `0x00C5618F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C561AD` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C561F4` → [CmpLinkHiveToMaster](../../page/87/CmpLinkHiveToMaster_function_00877D6C.md) (function, `0x00877D6C`)
- `0x00C56212` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C5621C` → [CmpAddToHiveFileList](../../page/A8/CmpAddToHiveFileList_function_00A81914.md) (function, `0x00A81914`)
- `0x00C56226` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C56239` → [CmpInitializeHardwareConfiguration](CmpInitializeHardwareConfiguration_function_00C5B4D0.md) (function, `0x00C5B4D0`)
- `0x00C56257` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C56260` → [CmpInitializeDriverStores](CmpInitializeDriverStores_function_00C57CF0.md) (function, `0x00C57CF0`)
- `0x00C5627E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C56287` → [CmpCreateExtendedControlSets](CmpCreateExtendedControlSets_function_00C56E38.md) (function, `0x00C56E38`)
- `0x00C562A5` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C562AE` → [CmpCreateHardwareProfiles](CmpCreateHardwareProfiles_function_00C56EF4.md) (function, `0x00C56EF4`)
- `0x00C562B6` → `ext-ms-win-ntos-kcminitcfg-l1-1-0.dll!CmSetInitMachineConfig` (import, 간접 대상; import `ext-ms-win-ntos-kcminitcfg-l1-1-0.dll!CmSetInitMachineConfig`)
- `0x00C562C2` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00C562C7` → [CmpMarkCurrentProfileDirty](../../page/7D/CmpMarkCurrentProfileDirty_function_007DBBAC.md) (function, `0x007DBBAC`)
- `0x00C562CF` → [CmpInitializeMachineDependentConfiguration](CmpInitializeMachineDependentConfiguration_function_00C5A02C.md) (function, `0x00C5A02C`)
- `0x00C562ED` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C562F6` → [CmpSetSystemValues](CmpSetSystemValues_function_00C58BB0.md) (function, `0x00C58BB0`)
- `0x00C56314` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C5631A` → [CmpMigrateOOBELanguageToInstallationLanguage](CmpMigrateOOBELanguageToInstallationLanguage_function_00C589A0.md) (function, `0x00C589A0`)
- `0x00C56328` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C56342` → [CmpSetNetworkValue](CmpSetNetworkValue_function_00C58AC4.md) (function, `0x00C58AC4`)
- `0x00C56360` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C56366` → [CmFcInitSystem2](CmFcInitSystem2_function_00C5AD0C.md) (function, `0x00C5AD0C`)
- `0x00C56384` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C5638E` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (function, `0x00BC9920`)
- `0x00C563B4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [Phase1InitializationDiscard](../C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1D3B9`

### Static image references
- `0x00C559F2` → RVA `0x00E0A740` (`.data`; read)
- `0x00C55A78` → RVA `0x00FC6AE0` (`ALMOSTRO`; read)
- `0x00C55A7F` → RVA `0x00EF7C68` (`.data`; write)
- `0x00C55A8B` → RVA `0x00FC4148` (`.data`; read)
- `0x00C55A95` → RVA `0x00FD8006` (`PAGEDATA`; write)
- `0x00C55A9B` → RVA `0x00FD8004` (`PAGEDATA`; write)
- `0x00C55AA2` → RVA `0x00FD8016` (`PAGEDATA`; write)
- `0x00C55AA9` → RVA `0x00EEFB5C` (`.data`; read)
- `0x00C55AB9` → RVA `0x00FD8004` (`PAGEDATA`; read)
- `0x00C55AC0` → RVA `0x00E098C0` (`.data`; read)
- `0x00C55AF4` → RVA `0x00EF5990` (`.data`; read)
- `0x00C55AFB` → RVA `0x00EF7C70` (`.data`; write)
- `0x00C55B02` → RVA `0x00FD9D18` (`PAGEDATA`; read)
- `0x00C55B09` → RVA `0x00EF5998` (`.data`; write)
- `0x00C55B10` → RVA `0x00EF5990` (`.data`; write)
- `0x00C55B17` → RVA `0x00FD9D20` (`PAGEDATA`; write)
- `0x00C55B1E` → RVA `0x00FD9D18` (`PAGEDATA`; write)
- `0x00C55B25` → RVA `0x00EF7C78` (`.data`; write)
- `0x00C55B2C` → RVA `0x00EF7B20` (`.data`; write)
- `0x00C55B33` → RVA `0x00EF7B28` (`.data`; write)
- `0x00C55B3A` → RVA `0x00EF7B30` (`.data`; write)
- `0x00C55B41` → RVA `0x00EF59A0` (`.data`; write)
- `0x00C55B48` → RVA `0x00EF5980` (`.data`; write)
- `0x00C55B58` → RVA `0x00EF70A0` (`.data`; read)
- `0x00C55B5F` → RVA `0x00EF7108` (`.data`; write)
- `0x00C55B71` → RVA `0x00EF7110` (`.data`; write)
- `0x00C55B89` → RVA `0x00EF70A0` (`.data`; write)
- `0x00C55B97` → RVA `0x00EF5960` (`.data`; read)
- `0x00C55B9E` → RVA `0x00EF5940` (`.data`; write)
- `0x00C55BA5` → RVA `0x00EF5968` (`.data`; write)
- `0x00C55BAC` → RVA `0x00EF5960` (`.data`; write)
- `0x00C55BB3` → RVA `0x00FD85D8` (`PAGEDATA`; read)
- `0x00C55BBA` → RVA `0x00FD85E0` (`PAGEDATA`; write)
- `0x00C55BC1` → RVA `0x00FD85D8` (`PAGEDATA`; write)
- `0x00C55BC8` → RVA `0x00EF5948` (`.data`; write)
- `0x00C55BCF` → RVA `0x00EF5950` (`.data`; write)
- `0x00C55BD6` → RVA `0x00EF5958` (`.data`; write)
- `0x00C55BDE` → RVA `0x00EF595A` (`.data`; write)
- `0x00C55BE5` → RVA `0x00EF595C` (`.data`; write)
- `0x00C55BF6` → RVA `0x00475D80` (`CmSiFreeMemory`; read)
- `0x00C55C03` → RVA `0x0047FD60` (`CmpAllocatePoolLookaside`; read)
- `0x00C55C12` → RVA `0x00E2CAC0` (`.data`; read)
- `0x00C55C39` → RVA `0x00EEFC28` (`.data`; write)
- `0x00C55C72` → RVA `0x00E09E6C` (`.data`; read)
- `0x00C55D2D` → RVA `0x00FD9A90` (`PAGEDATA`; read)
- `0x00C55E11` → RVA `0x00FD9DD8` (`PAGEDATA`; read)
- `0x00C55E26` → RVA `0x00B4AE90` (`nullclass`; read)
- `0x00C55E95` → RVA `0x00FDA388` (`PAGEDATA`; read)
- `0x00C55F1E` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)
- `0x00C55F25` → RVA `0x00FDA398` (`PAGEDATA`; read)
- `0x00C55FD1` → RVA `0x00FDA3A8` (`PAGEDATA`; read)
- `0x00C5605D` → RVA `0x00FD9A77` (`PAGEDATA`; write)
- `0x00C56095` → RVA `0x00C7A7A0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C560C0` → RVA `0x00FD8108` (`PAGEDATA`; read)
- `0x00C560C9` → RVA `0x00FC5008` (`ALMOSTRO`; read)
- `0x00C560D7` → RVA `0x00EEFB6C` (`.data`; read)
- `0x00C560E0` → RVA `0x00EEFB74` (`.data`; read)
- `0x00C560FE` → RVA `0x00EEFB70` (`.data`; read)
- `0x00C56105` → RVA `0x00E09994` (`.data`; write)
- `0x00C56113` → RVA `0x00E09A30` (`.data`; read/write)
- `0x00C56119` → RVA `0x00E09AE8` (`.data`; read/write)
- `0x00C5611F` → RVA `0x00E09C74` (`.data`; write)
- `0x00C56126` → RVA `0x00E09D2B` (`.data`; write)
- `0x00C561C0` → RVA `0x00FDA3B8` (`PAGEDATA`; read)
- `0x00C561C7` → RVA `0x00E098C8` (`.data`; read)
- `0x00C56232` → RVA `0x00E098B8` (`.data`; write)
- `0x00C562B6` → RVA `0x001512B8` (`ext-ms-win-ntos-kcminitcfg-l1-1-0.dll!CmSetInitMachineConfig (IAT)`; read)
- `0x00C5631F` → RVA `0x010086E0` (`INITDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **77**
  - `0x00C55A37` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C55A4F` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C55A67` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`INIT` → `.text`)
  - `0x00C55A73` → [CmpInitializeParseContext](../../page/87/CmpInitializeParseContext_function_008767F0.md) (`INIT` → `PAGE`)
  - `0x00C55B4F` → [Feature_Servicing_CmpRegistryLockToCacheAwarePushlock__private_IsEnabledDeviceUsageNoInline](../../text/66/Feature_Servicing_CmpRegistryLockToCacheAwarePushlock__private_IsEnabledDeviceUsageNoInline_function_0066A394.md) (`INIT` → `.text`)
  - `0x00C55B6C` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (`INIT` → `.text`)
  - `0x00C55B84` → [ExAllocateCacheAwarePushLock](../../text/4C/ExAllocateCacheAwarePushLock_function_004C68C0.md) (`INIT` → `.text`)
  - `0x00C55BEC` → [CmpInitializeNameCache](../../page/7E/CmpInitializeNameCache_function_007EAE0C.md) (`INIT` → `PAGE`)
  - `0x00C55C2A` → [ExInitializeLookasideListExInternal](../../text/46/ExInitializeLookasideListExInternal_function_00468890.md) (`INIT` → `.text`)
  - `0x00C55C2F` → [CmpInitSIDToHiveMapping](../../page/7E/CmpInitSIDToHiveMapping_function_007EBA2C.md) (`INIT` → `PAGE`)
  - `0x00C55C34` → [CmpAdminSystemSecurityDescriptor](../../page/7E/CmpAdminSystemSecurityDescriptor_function_007EBED8.md) (`INIT` → `PAGE`)
  - `0x00C55C45` → [CmpInitializeDelayedCloseTable](../../page/7E/CmpInitializeDelayedCloseTable_function_007EDA34.md) (`INIT` → `PAGE`)
  - `0x00C55C4A` → [CmpInitCallbacks](../../page/7E/CmpInitCallbacks_function_007E19A0.md) (`INIT` → `PAGE`)
  - `0x00C55C4F` → [CmpInitializeMachineHiveLoadedCallbacks](../../page/7E/CmpInitializeMachineHiveLoadedCallbacks_function_007E1EA0.md) (`INIT` → `PAGE`)
  - `0x00C55C54` → [CmpInitializeFreezeThaw](../../page/7E/CmpInitializeFreezeThaw_function_007E86B8.md) (`INIT` → `PAGE`)
  - `0x00C55C59` → [HvInitializeHashLibrary](../../page/7E/HvInitializeHashLibrary_function_007EDC44.md) (`INIT` → `PAGE`)
  - `0x00C55C5E` → [CmpValidateGlobalFlushControlFlags](../../page/7E/CmpValidateGlobalFlushControlFlags_function_007E7F50.md) (`INIT` → `PAGE`)
  - `0x00C55C63` → [CmpInitializeGlobalKeyLockTracker](../../page/7E/CmpInitializeGlobalKeyLockTracker_function_007EDE50.md) (`INIT` → `PAGE`)
  - `0x00C55C6D` → [CmpVolumeManagerInitialize](../../page/7E/CmpVolumeManagerInitialize_function_007E8B38.md) (`INIT` → `PAGE`)
  - `0x00C55C87` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C55C90` → [CmpHashUnicodeComponent](../../page/84/CmpHashUnicodeComponent_function_0084AC24.md) (`INIT` → `PAGE`)
  - `0x00C55CBB` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C55CC1` → [CmpInitializeLightWeightTransactionType](../../page/7E/CmpInitializeLightWeightTransactionType_function_007EE204.md) (`INIT` → `PAGE`)
  - `0x00C55CDF` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C55CE5` → [CmpInitializeRegistryProcess](../../page/7E/CmpInitializeRegistryProcess_function_007E8180.md) (`INIT` → `PAGE`)
  - `0x00C55D03` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C55D0D` → [CmpAttachToRegistryProcess](../../pagecmrc/BC/CmpAttachToRegistryProcess_function_00BC98E0.md) (`INIT` → `PAGECMRC`)
  - `0x00C55D12` → [CmpLockRegistryExclusive](../../page/84/CmpLockRegistryExclusive_function_0084F9B4.md) (`INIT` → `PAGE`)
  - `0x00C55D64` → [CmpCreateHive](../../page/87/CmpCreateHive_function_00879DF0.md) (`INIT` → `PAGE`)
  - `0x00C55D86` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C55D98` → [CmpInitializeKcbCache](../../page/87/CmpInitializeKcbCache_function_00878208.md) (`INIT` → `PAGE`)
  - `0x00C55DB6` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C55DD8` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C55DE0` → [CmpInitSiloSupport](../../page/7E/CmpInitSiloSupport_function_007E5B94.md) (`INIT` → `PAGE`)
  - `0x00C55DFE` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C55E04` → [CmpHiveRootSecurityDescriptor](../../page/7E/CmpHiveRootSecurityDescriptor_function_007ED104.md) (`INIT` → `PAGE`)
  - `0x00C55E5A` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`INIT` → `.text`)
  - `0x00C55E6B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C55E85` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C55E90` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`INIT` → `.text`)
  - `0x00C55EE3` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`INIT` → `.text`)
  - `0x00C55EF4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C55F0E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C55F19` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`INIT` → `.text`)
  - `0x00C55F7E` → [ObOpenObjectByName](../../page/89/ObOpenObjectByName_function_00899F50.md) (`INIT` → `PAGE`)
  - `0x00C55F8F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C55F9D` → [CmpCleanupParseContext](../../page/87/CmpCleanupParseContext_function_00876910.md) (`INIT` → `PAGE`)
  - `0x00C55FB5` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C55FC2` → [CmpCleanupParseContext](../../page/87/CmpCleanupParseContext_function_00876910.md) (`INIT` → `PAGE`)
  - `0x00C55FCC` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`INIT` → `.text`)
  - `0x00C5601F` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`INIT` → `.text`)
  - `0x00C56030` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C5604A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C56055` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`INIT` → `.text`)
  - `0x00C56064` → [CmpInitializeLoadOptions](../../text/66/CmpInitializeLoadOptions_function_0066A228.md) (`INIT` → `.text`)
  - `0x00C5608D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C560BA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C56139` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C5617E` → [CmpCreateHive](../../page/87/CmpCreateHive_function_00879DF0.md) (`INIT` → `PAGE`)
  - `0x00C5618F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C561AD` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C561F4` → [CmpLinkHiveToMaster](../../page/87/CmpLinkHiveToMaster_function_00877D6C.md) (`INIT` → `PAGE`)
  - `0x00C56212` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C5621C` → [CmpAddToHiveFileList](../../page/A8/CmpAddToHiveFileList_function_00A81914.md) (`INIT` → `PAGE`)
  - `0x00C56226` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C56257` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C5627E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C562A5` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C562C2` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`INIT` → `PAGECMRC`)
  - `0x00C562C7` → [CmpMarkCurrentProfileDirty](../../page/7D/CmpMarkCurrentProfileDirty_function_007DBBAC.md) (`INIT` → `PAGE`)
  - `0x00C562ED` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C56314` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C56328` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C56360` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C56384` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C5638E` → [CmpDetachFromRegistryProcess](../../pagecmrc/BC/CmpDetachFromRegistryProcess_function_00BC9920.md) (`INIT` → `PAGECMRC`)
  - `0x00C563B4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C559CC  48 8B C4                        mov rax, rsp
00C559CF  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00C559D3  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00C559D7  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00C559DB  55                              push rbp
00C559DC  41 54                           push r12
00C559DE  41 55                           push r13
00C559E0  41 56                           push r14
00C559E2  41 57                           push r15
00C559E4  48 8D A8 38 FC FF FF            lea rbp, [rax - 0x3c8]
00C559EB  48 81 EC A0 04 00 00            sub rsp, 0x4a0
00C559F2  48 8B 05 47 4D 1B 00            mov rax, qword ptr [rip + 0x1b4d47]
00C559F9  48 33 C4                        xor rax, rsp
00C559FC  48 89 85 90 03 00 00            mov qword ptr [rbp + 0x390], rax
00C55A03  45 33 E4                        xor r12d, r12d
00C55A06  48 8B D9                        mov rbx, rcx
00C55A09  0F 57 C0                        xorps xmm0, xmm0
00C55A0C  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
00C55A11  33 C0                           xor eax, eax
00C55A13  44 89 64 24 7C                  mov dword ptr [rsp + 0x7c], r12d
00C55A18  48 8D 8D C0 01 00 00            lea rcx, [rbp + 0x1c0]
00C55A1F  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00C55A23  33 D2                           xor edx, edx
00C55A25  44 89 65 94                     mov dword ptr [rbp - 0x6c], r12d
00C55A29  41 B8 D0 01 00 00               mov r8d, 0x1d0
00C55A2F  4C 89 65 A8                     mov qword ptr [rbp - 0x58], r12
00C55A33  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00C55A37  E8 04 12 A7 FF                  call 0x1406c6c40
00C55A3C  0F 57 C0                        xorps xmm0, xmm0
00C55A3F  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00C55A43  33 D2                           xor edx, edx
00C55A45  41 B8 B0 01 00 00               mov r8d, 0x1b0
00C55A4B  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
00C55A4F  E8 EC 11 A7 FF                  call 0x1406c6c40
00C55A54  0F 57 C0                        xorps xmm0, xmm0
00C55A57  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00C55A5B  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00C55A5F  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00C55A63  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
00C55A67  E8 04 64 7A FF                  call 0x1403fbe70
00C55A6C  48 8D 8D C0 01 00 00            lea rcx, [rbp + 0x1c0]
00C55A73  E8 78 0D C2 FF                  call 0x1408767f0
00C55A78  48 8D 05 61 10 37 00            lea rax, [rip + 0x371061]
00C55A7F  48 89 05 E2 21 2A 00            mov qword ptr [rip + 0x2a21e2], rax
00C55A86  45 8D 6C 24 01                  lea r13d, [r12 + 1]
00C55A8B  8A 05 B7 E6 36 00               mov al, byte ptr [rip + 0x36e6b7]
00C55A91  84 C0                           test al, al
00C55A93  74 14                           je 0x140c55aa9
00C55A95  88 05 6B 25 38 00               mov byte ptr [rip + 0x38256b], al
00C55A9B  44 88 2D 62 25 38 00            mov byte ptr [rip + 0x382562], r13b
00C55AA2  44 88 2D 6D 25 38 00            mov byte ptr [rip + 0x38256d], r13b
00C55AA9  44 39 25 AC A0 29 00            cmp dword ptr [rip + 0x29a0ac], r12d
00C55AB0  74 07                           je 0x140c55ab9
00C55AB2  44 88 2D 4B 25 38 00            mov byte ptr [rip + 0x38254b], r13b
00C55AB9  44 38 25 44 25 38 00            cmp byte ptr [rip + 0x382544], r12b
00C55AC0  48 8D 35 F9 3D 1B 00            lea rsi, [rip + 0x1b3df9]
00C55AC7  41 BE 07 00 00 00               mov r14d, 7
00C55ACD  74 1B                           je 0x140c55aea
00C55ACF  48 8B C6                        mov rax, rsi
00C55AD2  41 8B CE                        mov ecx, r14d
00C55AD5  4C 39 60 E0                     cmp qword ptr [rax - 0x20], r12
00C55AD9  74 04                           je 0x140c55adf
00C55ADB  0F BA 28 0F                     bts dword ptr [rax], 0xf
00C55ADF  48 05 B8 00 00 00               add rax, 0xb8
00C55AE5  49 2B CD                        sub rcx, r13
00C55AE8  75 EB                           jne 0x140c55ad5
00C55AEA  E8 D9 53 00 00                  call 0x140c5aec8
00C55AEF  E8 D8 3F 00 00                  call 0x140c59acc
00C55AF4  48 8D 05 95 FE 29 00            lea rax, [rip + 0x29fe95]
00C55AFB  4C 89 25 6E 21 2A 00            mov qword ptr [rip + 0x2a216e], r12
00C55B02  4C 8D 0D 0F 42 38 00            lea r9, [rip + 0x38420f]
00C55B09  48 89 05 88 FE 29 00            mov qword ptr [rip + 0x29fe88], rax
00C55B10  48 89 05 79 FE 29 00            mov qword ptr [rip + 0x29fe79], rax
00C55B17  4C 89 0D 02 42 38 00            mov qword ptr [rip + 0x384202], r9
00C55B1E  4C 89 0D F3 41 38 00            mov qword ptr [rip + 0x3841f3], r9
00C55B25  4C 89 25 4C 21 2A 00            mov qword ptr [rip + 0x2a214c], r12
00C55B2C  4C 89 25 ED 1F 2A 00            mov qword ptr [rip + 0x2a1fed], r12
00C55B33  4C 89 25 EE 1F 2A 00            mov qword ptr [rip + 0x2a1fee], r12
00C55B3A  4C 89 25 EF 1F 2A 00            mov qword ptr [rip + 0x2a1fef], r12
00C55B41  4C 89 25 58 FE 29 00            mov qword ptr [rip + 0x29fe58], r12
00C55B48  4C 89 25 31 FE 29 00            mov qword ptr [rip + 0x29fe31], r12
00C55B4F  E8 40 48 A1 FF                  call 0x14066a394
00C55B54  85 C0                           test eax, eax
00C55B56  75 22                           jne 0x140c55b7a
00C55B58  48 8D 3D 41 15 2A 00            lea rdi, [rip + 0x2a1541]
00C55B5F  44 89 25 A2 15 2A 00            mov dword ptr [rip + 0x2a15a2], r12d
00C55B66  48 8B CF                        mov rcx, rdi
00C55B69  83 CA FF                        or edx, 0xffffffff
00C55B6C  E8 9F 9B 7C FF                  call 0x14041f710
00C55B71  48 89 3D 98 15 2A 00            mov qword ptr [rip + 0x2a1598], rdi
00C55B78  EB 1D                           jmp 0x140c55b97
00C55B7A  41 8B CD                        mov ecx, r13d
00C55B7D  44 89 2D 84 15 2A 00            mov dword ptr [rip + 0x2a1584], r13d
00C55B84  E8 37 0D 87 FF                  call 0x1404c68c0
00C55B89  48 89 05 10 15 2A 00            mov qword ptr [rip + 0x2a1510], rax
00C55B90  48 89 05 79 15 2A 00            mov qword ptr [rip + 0x2a1579], rax
00C55B97  48 8D 05 C2 FD 29 00            lea rax, [rip + 0x29fdc2]
00C55B9E  44 89 2D 9B FD 29 00            mov dword ptr [rip + 0x29fd9b], r13d
00C55BA5  48 89 05 BC FD 29 00            mov qword ptr [rip + 0x29fdbc], rax
00C55BAC  48 89 05 AD FD 29 00            mov qword ptr [rip + 0x29fdad], rax
00C55BB3  48 8D 05 1E 2A 38 00            lea rax, [rip + 0x382a1e]
00C55BBA  48 89 05 1F 2A 38 00            mov qword ptr [rip + 0x382a1f], rax
00C55BC1  48 89 05 10 2A 38 00            mov qword ptr [rip + 0x382a10], rax
00C55BC8  4C 89 25 79 FD 29 00            mov qword ptr [rip + 0x29fd79], r12
00C55BCF  44 89 25 7A FD 29 00            mov dword ptr [rip + 0x29fd7a], r12d
00C55BD6  66 44 89 2D 7A FD 29 00         mov word ptr [rip + 0x29fd7a], r13w
00C55BDE  C6 05 75 FD 29 00 06            mov byte ptr [rip + 0x29fd75], 6
00C55BE5  44 89 25 70 FD 29 00            mov dword ptr [rip + 0x29fd70], r12d
00C55BEC  E8 1B 52 B9 FF                  call 0x1407eae0c
00C55BF1  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
00C55BF6  4C 8D 05 83 01 82 FF            lea r8, [rip - 0x7dfe7d]
00C55BFD  66 44 89 64 24 38               mov word ptr [rsp + 0x38], r12w
00C55C03  48 8D 15 56 A1 82 FF            lea rdx, [rip - 0x7d5eaa]
00C55C0A  C7 44 24 30 43 4D 6B 62         mov dword ptr [rsp + 0x30], 0x626b4d43
00C55C12  48 8D 0D A7 6E 1D 00            lea rcx, [rip + 0x1d6ea7]
00C55C19  48 C7 44 24 28 38 01 00 00      mov qword ptr [rsp + 0x28], 0x138
00C55C22  45 8B CD                        mov r9d, r13d
00C55C25  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00C55C2A  E8 61 2C 81 FF                  call 0x140468890
00C55C2F  E8 F8 5D B9 FF                  call 0x1407eba2c
00C55C34  E8 9F 62 B9 FF                  call 0x1407ebed8
00C55C39  48 89 05 E8 9F 29 00            mov qword ptr [rip + 0x299fe8], rax
00C55C40  E8 C3 54 00 00                  call 0x140c5b108
00C55C45  E8 EA 7D B9 FF                  call 0x1407eda34
00C55C4A  E8 51 BD B8 FF                  call 0x1407e19a0
00C55C4F  E8 4C C2 B8 FF                  call 0x1407e1ea0
00C55C54  E8 5F 2A B9 FF                  call 0x1407e86b8
00C55C59  E8 E6 7F B9 FF                  call 0x1407edc44
00C55C5E  E8 ED 22 B9 FF                  call 0x1407e7f50
00C55C63  E8 E8 81 B9 FF                  call 0x1407ede50
00C55C68  E8 1F 55 00 00                  call 0x140c5b18c
00C55C6D  E8 C6 2E B9 FF                  call 0x1407e8b38
00C55C72  48 8D 3D F3 41 1B 00            lea rdi, [rip + 0x1b41f3]
00C55C79  41 BF 08 00 00 00               mov r15d, 8
00C55C7F  48 8B 57 F4                     mov rdx, qword ptr [rdi - 0xc]
00C55C83  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00C55C87  E8 F4 4A 7D FF                  call 0x14042a780
00C55C8C  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00C55C90  E8 8F 4F BF FF                  call 0x14084ac24
00C55C95  89 07                           mov dword ptr [rdi], eax
00C55C97  48 8D 7F 18                     lea rdi, [rdi + 0x18]
00C55C9B  4D 2B FD                        sub r15, r13
00C55C9E  75 DF                           jne 0x140c55c7f
00C55CA0  E8 DB 1A 00 00                  call 0x140c57780
00C55CA5  85 C0                           test eax, eax
00C55CA7  79 18                           jns 0x140c55cc1
00C55CA9  4C 63 C8                        movsxd r9, eax
00C55CAC  41 8D 4F 67                     lea ecx, [r15 + 0x67]
00C55CB0  4D 8B C5                        mov r8, r13
00C55CB3  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C55CB8  49 8B D5                        mov rdx, r13
00C55CBB  E8 A0 79 8A FF                  call 0x1404fd660
00C55CC0  CC                              int3
00C55CC1  E8 3E 85 B9 FF                  call 0x1407ee204
00C55CC6  85 C0                           test eax, eax
00C55CC8  79 1B                           jns 0x140c55ce5
00C55CCA  41 B8 18 00 00 00               mov r8d, 0x18
00C55CD0  4C 63 C8                        movsxd r9, eax
00C55CD3  49 8B D5                        mov rdx, r13
00C55CD6  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C55CDB  41 8D 48 4F                     lea ecx, [r8 + 0x4f]
00C55CDF  E8 7C 79 8A FF                  call 0x1404fd660
00C55CE4  CC                              int3
00C55CE5  E8 96 24 B9 FF                  call 0x1407e8180
00C55CEA  85 C0                           test eax, eax
00C55CEC  79 1B                           jns 0x140c55d09
00C55CEE  41 B8 19 00 00 00               mov r8d, 0x19
00C55CF4  4C 63 C8                        movsxd r9, eax
00C55CF7  49 8B D5                        mov rdx, r13
00C55CFA  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C55CFF  41 8D 48 4E                     lea ecx, [r8 + 0x4e]
00C55D03  E8 58 79 8A FF                  call 0x1404fd660
00C55D08  CC                              int3
00C55D09  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00C55D0D  E8 CE 3B F7 FF                  call 0x140bc98e0
00C55D12  E8 9D 9C BF FF                  call 0x14084f9b4
00C55D17  33 D2                           xor edx, edx
00C55D19  48 8B CB                        mov rcx, rbx
00C55D1C  E8 B3 27 00 00                  call 0x140c584d4
00C55D21  48 8D 45 10                     lea rax, [rbp + 0x10]
00C55D25  45 33 C9                        xor r9d, r9d
00C55D28  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00C55D2D  48 8D 0D 5C 3D 38 00            lea rcx, [rip + 0x383d5c]
00C55D34  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
00C55D39  45 8B C5                        mov r8d, r13d
00C55D3C  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
00C55D41  33 D2                           xor edx, edx
00C55D43  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
00C55D48  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00C55D4D  C7 44 24 38 00 00 02 00         mov dword ptr [rsp + 0x38], 0x20000
00C55D55  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
00C55D5A  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00C55D5F  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C55D64  E8 87 40 C2 FF                  call 0x140879df0
00C55D69  85 C0                           test eax, eax
00C55D6B  79 1F                           jns 0x140c55d8c
00C55D6D  41 B8 02 00 00 00               mov r8d, 2
00C55D73  4C 63 C8                        movsxd r9, eax
00C55D76  48 8D 45 10                     lea rax, [rbp + 0x10]
00C55D7A  49 8B D5                        mov rdx, r13
00C55D7D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C55D82  41 8D 48 65                     lea ecx, [r8 + 0x65]
00C55D86  E8 D5 78 8A FF                  call 0x1404fd660
00C55D8B  CC                              int3
00C55D8C  48 8B 0D FD 3C 38 00            mov rcx, qword ptr [rip + 0x383cfd]
00C55D93  BA 80 00 00 00                  mov edx, 0x80
00C55D98  E8 6B 24 C2 FF                  call 0x140878208
00C55D9D  85 C0                           test eax, eax
00C55D9F  79 1B                           jns 0x140c55dbc
00C55DA1  41 B8 03 00 00 00               mov r8d, 3
00C55DA7  4C 63 C8                        movsxd r9, eax
00C55DAA  49 8B D5                        mov rdx, r13
00C55DAD  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C55DB2  41 8D 48 64                     lea ecx, [r8 + 0x64]
00C55DB6  E8 A5 78 8A FF                  call 0x1404fd660
00C55DBB  CC                              int3
00C55DBC  E8 BF 1A 00 00                  call 0x140c57880
00C55DC1  85 C0                           test eax, eax
00C55DC3  79 19                           jns 0x140c55dde
00C55DC5  45 33 C9                        xor r9d, r9d
00C55DC8  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C55DCD  49 8B D5                        mov rdx, r13
00C55DD0  45 8D 41 04                     lea r8d, [r9 + 4]
00C55DD4  41 8D 49 67                     lea ecx, [r9 + 0x67]
00C55DD8  E8 83 78 8A FF                  call 0x1404fd660
00C55DDD  CC                              int3
00C55DDE  33 C9                           xor ecx, ecx
00C55DE0  E8 AF FD B8 FF                  call 0x1407e5b94
00C55DE5  85 C0                           test eax, eax
00C55DE7  79 1B                           jns 0x140c55e04
00C55DE9  41 B8 1A 00 00 00               mov r8d, 0x1a
00C55DEF  4C 63 C8                        movsxd r9, eax
00C55DF2  49 8B D5                        mov rdx, r13
00C55DF5  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C55DFA  41 8D 48 4D                     lea ecx, [r8 + 0x4d]
00C55DFE  E8 5D 78 8A FF                  call 0x1404fd660
00C55E03  CC                              int3
00C55E04  E8 FB 72 B9 FF                  call 0x1407ed104
00C55E09  48 8B F8                        mov rdi, rax
00C55E0C  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
00C55E11  48 8D 05 C0 3F 38 00            lea rax, [rip + 0x383fc0]
00C55E18  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00C55E1D  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00C55E21  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00C55E26  48 8D 05 63 50 EF FF            lea rax, [rip - 0x10af9d]
00C55E2D  C7 44 24 78 30 00 00 00         mov dword ptr [rsp + 0x78], 0x30
00C55E35  45 33 C9                        xor r9d, r9d
00C55E38  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C55E3D  BA 1F 00 02 00                  mov edx, 0x2001f
00C55E42  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
00C55E46  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00C55E4B  C7 45 90 40 02 00 00            mov dword ptr [rbp - 0x70], 0x240
00C55E52  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
00C55E56  4C 89 65 A0                     mov qword ptr [rbp - 0x60], r12
00C55E5A  E8 11 76 A5 FF                  call 0x1406ad470
00C55E5F  4C 63 F8                        movsxd r15, eax
00C55E62  85 C0                           test eax, eax
00C55E64  79 25                           jns 0x140c55e8b
00C55E66  33 D2                           xor edx, edx
00C55E68  48 8B CF                        mov rcx, rdi
00C55E6B  E8 00 CA F2 FF                  call 0x140b82870
00C55E70  41 B8 05 00 00 00               mov r8d, 5
00C55E76  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C55E7B  4D 8B CF                        mov r9, r15
00C55E7E  49 8B D5                        mov rdx, r13
00C55E81  41 8D 48 62                     lea ecx, [r8 + 0x62]
00C55E85  E8 D6 77 8A FF                  call 0x1404fd660
00C55E8A  CC                              int3
00C55E8B  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00C55E90  E8 1B 74 A5 FF                  call 0x1406ad2b0
00C55E95  48 8D 05 EC 44 38 00            lea rax, [rip + 0x3844ec]
00C55E9C  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
00C55EA1  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00C55EA5  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00C55EAA  48 8D 05 DF 4F EF FF            lea rax, [rip - 0x10b021]
00C55EB1  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00C55EB6  45 33 C9                        xor r9d, r9d
00C55EB9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C55EBE  BA 1F 00 02 00                  mov edx, 0x2001f
00C55EC3  C7 44 24 78 30 00 00 00         mov dword ptr [rsp + 0x78], 0x30
00C55ECB  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00C55ED0  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
00C55ED4  C7 45 90 40 02 00 00            mov dword ptr [rbp - 0x70], 0x240
00C55EDB  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
00C55EDF  4C 89 65 A0                     mov qword ptr [rbp - 0x60], r12
00C55EE3  E8 88 75 A5 FF                  call 0x1406ad470
00C55EE8  4C 63 F8                        movsxd r15, eax
00C55EEB  85 C0                           test eax, eax
00C55EED  79 25                           jns 0x140c55f14
00C55EEF  33 D2                           xor edx, edx
00C55EF1  48 8B CF                        mov rcx, rdi
00C55EF4  E8 77 C9 F2 FF                  call 0x140b82870
00C55EF9  41 B8 06 00 00 00               mov r8d, 6
00C55EFF  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C55F04  4D 8B CF                        mov r9, r15
00C55F07  49 8B D5                        mov rdx, r13
00C55F0A  41 8D 48 61                     lea ecx, [r8 + 0x61]
00C55F0E  E8 4D 77 8A FF                  call 0x1404fd660
00C55F13  CC                              int3
00C55F14  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00C55F19  E8 92 73 A5 FF                  call 0x1406ad2b0
00C55F1E  48 8B 15 9B 0B 37 00            mov rdx, qword ptr [rip + 0x370b9b]
00C55F25  48 8D 05 6C 44 38 00            lea rax, [rip + 0x38446c]
00C55F2C  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00C55F30  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00C55F35  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00C55F3A  C7 44 24 78 30 00 00 00         mov dword ptr [rsp + 0x78], 0x30
00C55F42  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C55F47  45 33 C9                        xor r9d, r9d
00C55F4A  48 8D 85 C0 01 00 00            lea rax, [rbp + 0x1c0]
00C55F51  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
00C55F55  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C55F5A  45 33 C0                        xor r8d, r8d
00C55F5D  C7 44 24 20 1F 00 02 00         mov dword ptr [rsp + 0x20], 0x2001f
00C55F65  C7 45 90 40 02 00 00            mov dword ptr [rbp - 0x70], 0x240
00C55F6C  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
00C55F70  4C 89 65 A0                     mov qword ptr [rbp - 0x60], r12
00C55F74  C7 85 C0 01 00 00 41 00 00 00   mov dword ptr [rbp + 0x1c0], 0x41
00C55F7E  E8 CD 3F C4 FF                  call 0x140899f50
00C55F83  33 D2                           xor edx, edx
00C55F85  4C 63 F8                        movsxd r15, eax
00C55F88  85 C0                           test eax, eax
00C55F8A  79 2F                           jns 0x140c55fbb
00C55F8C  48 8B CF                        mov rcx, rdi
00C55F8F  E8 DC C8 F2 FF                  call 0x140b82870
00C55F94  33 D2                           xor edx, edx
00C55F96  48 8D 8D C0 01 00 00            lea rcx, [rbp + 0x1c0]
00C55F9D  E8 6E 09 C2 FF                  call 0x140876910
00C55FA2  4D 8B CF                        mov r9, r15
00C55FA5  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C55FAA  4D 8B C6                        mov r8, r14
00C55FAD  49 8B D5                        mov rdx, r13
00C55FB0  B9 67 00 00 00                  mov ecx, 0x67
00C55FB5  E8 A6 76 8A FF                  call 0x1404fd660
00C55FBA  CC                              int3
00C55FBB  48 8D 8D C0 01 00 00            lea rcx, [rbp + 0x1c0]
00C55FC2  E8 49 09 C2 FF                  call 0x140876910
00C55FC7  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00C55FCC  E8 DF 72 A5 FF                  call 0x1406ad2b0
00C55FD1  48 8D 05 D0 43 38 00            lea rax, [rip + 0x3843d0]
00C55FD8  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
00C55FDD  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00C55FE1  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00C55FE6  48 8D 05 A3 4E EF FF            lea rax, [rip - 0x10b15d]
00C55FED  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00C55FF2  45 33 C9                        xor r9d, r9d
00C55FF5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C55FFA  BA 1F 00 02 00                  mov edx, 0x2001f
00C55FFF  C7 44 24 78 30 00 00 00         mov dword ptr [rsp + 0x78], 0x30
00C56007  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00C5600C  4C 89 65 80                     mov qword ptr [rbp - 0x80], r12
00C56010  C7 45 90 40 02 00 00            mov dword ptr [rbp - 0x70], 0x240
00C56017  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
00C5601B  4C 89 65 A0                     mov qword ptr [rbp - 0x60], r12
00C5601F  E8 4C 74 A5 FF                  call 0x1406ad470
00C56024  4C 63 F8                        movsxd r15, eax
00C56027  85 C0                           test eax, eax
00C56029  79 25                           jns 0x140c56050
00C5602B  33 D2                           xor edx, edx
00C5602D  48 8B CF                        mov rcx, rdi
00C56030  E8 3B C8 F2 FF                  call 0x140b82870
00C56035  41 B8 08 00 00 00               mov r8d, 8
00C5603B  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C56040  4D 8B CF                        mov r9, r15
00C56043  49 8B D5                        mov rdx, r13
00C56046  41 8D 48 5F                     lea ecx, [r8 + 0x5f]
00C5604A  E8 11 76 8A FF                  call 0x1404fd660
00C5604F  CC                              int3
00C56050  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00C56055  E8 56 72 A5 FF                  call 0x1406ad2b0
00C5605A  48 8B CB                        mov rcx, rbx
00C5605D  44 88 2D 13 3A 38 00            mov byte ptr [rip + 0x383a13], r13b
00C56064  E8 BF 41 A1 FF                  call 0x14066a228
00C56069  41 8B D5                        mov edx, r13d
00C5606C  48 8B CB                        mov rcx, rbx
00C5606F  E8 60 24 00 00                  call 0x140c584d4
00C56074  85 C0                           test eax, eax
00C56076  79 1B                           jns 0x140c56093
00C56078  41 B8 14 00 00 00               mov r8d, 0x14
00C5607E  4C 63 C8                        movsxd r9, eax
00C56081  49 8B D5                        mov rdx, r13
00C56084  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C56089  41 8D 48 53                     lea ecx, [r8 + 0x53]
00C5608D  E8 CE 75 8A FF                  call 0x1404fd660
00C56092  CC                              int3
00C56093  33 D2                           xor edx, edx
00C56095  48 8D 0D 04 47 02 00            lea rcx, [rip + 0x24704]
00C5609C  E8 6F 08 00 00                  call 0x140c56910
00C560A1  85 C0                           test eax, eax
00C560A3  79 1B                           jns 0x140c560c0
00C560A5  41 B8 0D 00 00 00               mov r8d, 0xd
00C560AB  4C 63 C8                        movsxd r9, eax
00C560AE  49 8B D5                        mov rdx, r13
00C560B1  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C560B6  41 8D 48 5A                     lea ecx, [r8 + 0x5a]
00C560BA  E8 A1 75 8A FF                  call 0x1404fd660
00C560BF  CC                              int3
00C560C0  44 39 25 41 20 38 00            cmp dword ptr [rip + 0x382041], r12d
00C560C7  74 0E                           je 0x140c560d7
00C560C9  48 8B 05 38 EF 36 00            mov rax, qword ptr [rip + 0x36ef38]
00C560D0  83 88 F0 02 00 00 10            or dword ptr [rax + 0x2f0], 0x10
00C560D7  44 39 25 8E 9A 29 00            cmp dword ptr [rip + 0x299a8e], r12d
00C560DE  74 4D                           je 0x140c5612d
00C560E0  44 39 25 8D 9A 29 00            cmp dword ptr [rip + 0x299a8d], r12d
00C560E7  74 15                           je 0x140c560fe
00C560E9  B8 00 80 00 00                  mov eax, 0x8000
00C560EE  09 06                           or dword ptr [rsi], eax
00C560F0  48 8D B6 B8 00 00 00            lea rsi, [rsi + 0xb8]
00C560F7  4D 2B F5                        sub r14, r13
00C560FA  75 F2                           jne 0x140c560ee
00C560FC  EB 2F                           jmp 0x140c5612d
00C560FE  44 39 25 6B 9A 29 00            cmp dword ptr [rip + 0x299a6b], r12d
00C56105  44 88 25 88 38 1B 00            mov byte ptr [rip + 0x1b3888], r12b
00C5610C  75 11                           jne 0x140c5611f
00C5610E  B8 00 80 00 00                  mov eax, 0x8000
00C56113  09 05 17 39 1B 00               or dword ptr [rip + 0x1b3917], eax
00C56119  09 05 C9 39 1B 00               or dword ptr [rip + 0x1b39c9], eax
00C5611F  44 88 25 4E 3B 1B 00            mov byte ptr [rip + 0x1b3b4e], r12b
00C56126  44 88 2D FE 3B 1B 00            mov byte ptr [rip + 0x1b3bfe], r13b
00C5612D  33 D2                           xor edx, edx
00C5612F  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00C56133  41 B8 B0 01 00 00               mov r8d, 0x1b0
00C56139  E8 02 0B A7 FF                  call 0x1406c6c40
00C5613E  48 8D 45 10                     lea rax, [rbp + 0x10]
00C56142  45 33 C9                        xor r9d, r9d
00C56145  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00C5614A  48 8D 4D A8                     lea rcx, [rbp - 0x58]
00C5614E  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
00C56153  45 8B C5                        mov r8d, r13d
00C56156  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
00C5615B  33 D2                           xor edx, edx
00C5615D  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
00C56162  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00C56167  C7 44 24 38 00 00 02 00         mov dword ptr [rsp + 0x38], 0x20000
00C5616F  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
00C56174  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00C56179  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C5617E  E8 6D 3C C2 FF                  call 0x140879df0
00C56183  48 63 F0                        movsxd rsi, eax
00C56186  85 C0                           test eax, eax
00C56188  79 29                           jns 0x140c561b3
00C5618A  33 D2                           xor edx, edx
00C5618C  48 8B CF                        mov rcx, rdi
00C5618F  E8 DC C6 F2 FF                  call 0x140b82870
00C56194  41 B8 10 00 00 00               mov r8d, 0x10
00C5619A  48 8D 45 10                     lea rax, [rbp + 0x10]
00C5619E  4C 8B CE                        mov r9, rsi
00C561A1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C561A6  49 8B D5                        mov rdx, r13
00C561A9  41 8D 48 57                     lea ecx, [r8 + 0x57]
00C561AD  E8 AE 74 8A FF                  call 0x1404fd660
00C561B2  CC                              int3
00C561B3  4C 8B 45 A8                     mov r8, qword ptr [rbp - 0x58]
00C561B7  48 8D 45 10                     lea rax, [rbp + 0x10]
00C561BB  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00C561C0  48 8D 0D F1 41 38 00            lea rcx, [rip + 0x3841f1]
00C561C7  8B 05 FB 36 1B 00               mov eax, dword ptr [rip + 0x1b36fb]
00C561CD  45 8A CD                        mov r9b, r13b
00C561D0  44 88 6C 24 50                  mov byte ptr [rsp + 0x50], r13b
00C561D5  33 D2                           xor edx, edx
00C561D7  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
00C561DC  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00C561E1  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00C561E6  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
00C561EB  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
00C561F0  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00C561F4  E8 73 1B C2 FF                  call 0x140877d6c
00C561F9  85 C0                           test eax, eax
00C561FB  74 1B                           je 0x140c56218
00C561FD  41 B8 11 00 00 00               mov r8d, 0x11
00C56203  4C 63 C8                        movsxd r9, eax
00C56206  49 8B D5                        mov rdx, r13
00C56209  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C5620E  41 8D 48 56                     lea ecx, [r8 + 0x56]
00C56212  E8 49 74 8A FF                  call 0x1404fd660
00C56217  CC                              int3
00C56218  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00C5621C  E8 F3 B6 E2 FF                  call 0x140a81914
00C56221  33 D2                           xor edx, edx
00C56223  48 8B CF                        mov rcx, rdi
00C56226  E8 45 C6 F2 FF                  call 0x140b82870
00C5622B  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
00C5622F  48 8B CB                        mov rcx, rbx
00C56232  48 89 05 7F 36 1B 00            mov qword ptr [rip + 0x1b367f], rax
00C56239  E8 92 52 00 00                  call 0x140c5b4d0
00C5623E  85 C0                           test eax, eax
00C56240  79 1B                           jns 0x140c5625d
00C56242  41 B8 12 00 00 00               mov r8d, 0x12
00C56248  4C 63 C8                        movsxd r9, eax
00C5624B  49 8B D5                        mov rdx, r13
00C5624E  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C56253  41 8D 48 55                     lea ecx, [r8 + 0x55]
00C56257  E8 04 74 8A FF                  call 0x1404fd660
00C5625C  CC                              int3
00C5625D  48 8B CB                        mov rcx, rbx
00C56260  E8 8B 1A 00 00                  call 0x140c57cf0
00C56265  85 C0                           test eax, eax
00C56267  79 1B                           jns 0x140c56284
00C56269  41 B8 13 00 00 00               mov r8d, 0x13
00C5626F  4C 63 C8                        movsxd r9, eax
00C56272  49 8B D5                        mov rdx, r13
00C56275  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C5627A  41 8D 48 54                     lea ecx, [r8 + 0x54]
00C5627E  E8 DD 73 8A FF                  call 0x1404fd660
00C56283  CC                              int3
00C56284  48 8B CB                        mov rcx, rbx
00C56287  E8 AC 0B 00 00                  call 0x140c56e38
00C5628C  85 C0                           test eax, eax
00C5628E  79 1B                           jns 0x140c562ab
00C56290  41 B8 1B 00 00 00               mov r8d, 0x1b
00C56296  4C 63 C8                        movsxd r9, eax
00C56299  49 8B D5                        mov rdx, r13
00C5629C  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C562A1  41 8D 48 4C                     lea ecx, [r8 + 0x4c]
00C562A5  E8 B6 73 8A FF                  call 0x1404fd660
00C562AA  CC                              int3
00C562AB  48 8B CB                        mov rcx, rbx
00C562AE  E8 41 0C 00 00                  call 0x140c56ef4
00C562B3  48 8B CB                        mov rcx, rbx
00C562B6  48 FF 15 FB AF 4F FF            call qword ptr [rip - 0xb05005]
00C562BD  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00C562C2  E8 BD 37 F7 FF                  call 0x140bc9a84
00C562C7  E8 E0 58 B8 FF                  call 0x1407dbbac
00C562CC  48 8B CB                        mov rcx, rbx
00C562CF  E8 58 3D 00 00                  call 0x140c5a02c
00C562D4  85 C0                           test eax, eax
00C562D6  79 1B                           jns 0x140c562f3
00C562D8  41 B8 15 00 00 00               mov r8d, 0x15
00C562DE  4C 63 C8                        movsxd r9, eax
00C562E1  49 8B D5                        mov rdx, r13
00C562E4  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C562E9  41 8D 48 52                     lea ecx, [r8 + 0x52]
00C562ED  E8 6E 73 8A FF                  call 0x1404fd660
00C562F2  CC                              int3
00C562F3  48 8B CB                        mov rcx, rbx
00C562F6  E8 B5 28 00 00                  call 0x140c58bb0
00C562FB  85 C0                           test eax, eax
00C562FD  79 1B                           jns 0x140c5631a
00C562FF  41 B8 16 00 00 00               mov r8d, 0x16
00C56305  4C 63 C8                        movsxd r9, eax
00C56308  49 8B D5                        mov rdx, r13
00C5630B  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C56310  41 8D 48 51                     lea ecx, [r8 + 0x51]
00C56314  E8 47 73 8A FF                  call 0x1404fd660
00C56319  CC                              int3
00C5631A  E8 81 26 00 00                  call 0x140c589a0
00C5631F  48 8B 0D BA 23 3B 00            mov rcx, qword ptr [rip + 0x3b23ba]
00C56326  33 D2                           xor edx, edx
00C56328  E8 43 C5 F2 FF                  call 0x140b82870
00C5632D  48 8B 8B F0 00 00 00            mov rcx, qword ptr [rbx + 0xf0]
00C56334  83 39 68                        cmp dword ptr [rcx], 0x68
00C56337  72 2D                           jb 0x140c56366
00C56339  48 8B 49 60                     mov rcx, qword ptr [rcx + 0x60]
00C5633D  48 85 C9                        test rcx, rcx
00C56340  74 24                           je 0x140c56366
00C56342  E8 7D 27 00 00                  call 0x140c58ac4
00C56347  85 C0                           test eax, eax
00C56349  79 1B                           jns 0x140c56366
00C5634B  41 B8 17 00 00 00               mov r8d, 0x17
00C56351  4C 63 C8                        movsxd r9, eax
00C56354  49 8B D5                        mov rdx, r13
00C56357  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C5635C  41 8D 48 50                     lea ecx, [r8 + 0x50]
00C56360  E8 FB 72 8A FF                  call 0x1404fd660
00C56365  CC                              int3
00C56366  E8 A1 49 00 00                  call 0x140c5ad0c
00C5636B  85 C0                           test eax, eax
00C5636D  79 1B                           jns 0x140c5638a
00C5636F  41 B8 1A 00 00 00               mov r8d, 0x1a
00C56375  4C 63 C8                        movsxd r9, eax
00C56378  49 8B D5                        mov rdx, r13
00C5637B  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C56380  41 8D 48 4D                     lea ecx, [r8 + 0x4d]
00C56384  E8 D7 72 8A FF                  call 0x1404fd660
00C56389  CC                              int3
00C5638A  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00C5638E  E8 8D 35 F7 FF                  call 0x140bc9920
00C56393  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00C5639C  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00C563A0  48 89 81 E8 06 00 00            mov qword ptr [rcx + 0x6e8], rax
00C563A7  41 8A C5                        mov al, r13b
00C563AA  48 8B 8D 90 03 00 00            mov rcx, qword ptr [rbp + 0x390]
00C563B1  48 33 CC                        xor rcx, rsp
00C563B4  E8 87 62 A5 FF                  call 0x1406ac640
00C563B9  4C 8D 9C 24 A0 04 00 00         lea r11, [rsp + 0x4a0]
00C563C1  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00C563C5  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00C563C9  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00C563CD  49 8B E3                        mov rsp, r11
00C563D0  41 5F                           pop r15
00C563D2  41 5E                           pop r14
00C563D4  41 5D                           pop r13
00C563D6  41 5C                           pop r12
00C563D8  5D                              pop rbp
00C563D9  C3                              ret
00C563DA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmInitSystem1(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m44C;
    unsigned __int64 v_stack_m450;
    unsigned __int64 v_stack_m458;
    unsigned __int64 v_stack_m468;
    unsigned __int64 v_stack_m470;
    unsigned __int64 v_stack_m478;
    unsigned __int64 v_stack_m480;
    unsigned int v_stack_m488;
    unsigned __int16 v_stack_m490;
    unsigned int v_stack_m498;
    unsigned __int64 v_stack_m4A0;
    unsigned int v_stack_m4A8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (0x4A0ULL);
    result = (*(unsigned __int64 *)(v_rip + 1789255)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 968 + 912) = result;
    v_r12 = 0;
    v_stack_m458 = 0;
    result = 0;
    v_stack_m44C = 0;
    *(unsigned __int64 *)(v_rsp - 968 - 48) = 0;
    a2 = 0;
    *(unsigned int *)(v_rsp - 968 - 108) = 0;
    *(unsigned __int64 *)(v_rsp - 968 - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 968 - 64) = v_xmm0;
    result = memset(v_rsp - 968 + 448, a2, 464, a4);
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 968 - 80) = v_xmm0;
    result = memset(v_rsp - 968 + 16, a2, 432, a4);
    *(unsigned __int64 *)(v_rsp - 968 - 40) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 968 - 24) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 968 - 8) = v_xmm0;
    result = CmpInitializeThreadInfo(v_rsp - 968 - 64, a2, 432, a4);
    result = CmpInitializeParseContext(v_rsp - 968 + 448, a2, 432, a4);
    *(unsigned __int64 *)(v_rip + 2761186) = v_rip + 3608673;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 3598007)) != 0) {
        *(unsigned __int8 *)(v_rip + 3679595) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 3598007));
        *(unsigned __int8 *)(v_rip + 3679586) = (unsigned __int8)(v_r12 + 1);
        *(unsigned __int8 *)(v_rip + 3679597) = (unsigned __int8)(v_r12 + 1);
    }
    if ((*(unsigned int *)(v_rip + 2728108)) != 0) {
        *(unsigned __int8 *)(v_rip + 3679563) = (unsigned __int8)(v_r12 + 1);
    }
    if ((*(unsigned __int8 *)(v_rip + 3679556)) == 0) goto loc_00C55AEA;
loc_00C55AD5:
    if ((*(unsigned __int64 *)(v_rip + 1785337 - 32)) != 0) {
    }
    result = (v_rip + 1785337) + (184);
    a1 = (7) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_00C55AD5;
loc_00C55AEA:
    result = CmpInitializeRegistryNames(a1, a2, 432, a4);
    result = CmpInitGlobalQuotaAllowed(a1, a2, 432, a4);
    *(unsigned __int64 *)(v_rip + 2761070) = 0;
    *(unsigned __int64 *)(v_rip + 2752136) = v_rip + 2752149;
    *(unsigned __int64 *)(v_rip + 2752121) = v_rip + 2752149;
    *(unsigned __int64 *)(v_rip + 3686914) = v_rip + 3686927;
    *(unsigned __int64 *)(v_rip + 3686899) = v_rip + 3686927;
    *(unsigned __int64 *)(v_rip + 2761036) = 0;
    *(unsigned __int64 *)(v_rip + 2760685) = 0;
    *(unsigned __int64 *)(v_rip + 2760686) = 0;
    *(unsigned __int64 *)(v_rip + 2760687) = 0;
    *(unsigned __int64 *)(v_rip + 2752088) = 0;
    *(unsigned __int64 *)(v_rip + 2752049) = 0;
    result = Feature_Servicing_CmpRegistryLockToCacheAwarePushlock__private_IsEnabledDeviceUsageNoInline(a1, a2, 432, v_rip + 3686927);
    if ((unsigned int)(result) != 0) goto loc_00C55B7A;
    *(unsigned int *)(v_rip + 2758050) = 0;
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    result = ExInitializeResourceLite2(v_rip + 2757953, a2, 432, v_rip + 3686927);
    *(unsigned __int64 *)(v_rip + 2758040) = v_rip + 2757953;
    goto loc_00C55B97;
loc_00C55B7A:
    *(unsigned int *)(v_rip + 2758020) = (unsigned int)(v_r12 + 1);
    result = ExAllocateCacheAwarePushLock((unsigned int)((unsigned int)(v_r12 + 1)), a2, 432, v_rip + 3686927);
    *(unsigned __int64 *)(v_rip + 2757904) = result;
    *(unsigned __int64 *)(v_rip + 2758009) = result;
loc_00C55B97:
    *(unsigned int *)(v_rip + 2751899) = (unsigned int)(v_r12 + 1);
    *(unsigned __int64 *)(v_rip + 2751932) = v_rip + 2751938;
    *(unsigned __int64 *)(v_rip + 2751917) = v_rip + 2751938;
    *(unsigned __int64 *)(v_rip + 3680799) = v_rip + 3680798;
    *(unsigned __int64 *)(v_rip + 3680784) = v_rip + 3680798;
    *(unsigned __int64 *)(v_rip + 2751865) = 0;
    *(unsigned int *)(v_rip + 2751866) = 0;
    *(unsigned __int16 *)(v_rip + 2751866) = (unsigned __int16)(v_r12 + 1);
    *(unsigned __int8 *)(v_rip + 2751861) = 6;
    *(unsigned int *)(v_rip + 2751856) = 0;
    result = CmpInitializeNameCache((unsigned int)((unsigned int)(v_r12 + 1)), a2, 432, v_rip + 3686927);
    v_stack_m488 = 0;
    v_stack_m490 = 0;
    v_stack_m498 = 0x626B4D43ULL;
    v_stack_m4A0 = 312;
    v_stack_m4A8 = 0;
    result = ExInitializeLookasideListExInternal(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
    result = CmpInitSIDToHiveMapping(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
    result = CmpAdminSystemSecurityDescriptor(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
    *(unsigned __int64 *)(v_rip + 2727912) = result;
    result = CmpInitializeTrustedInstallerSid(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
    result = CmpInitializeDelayedCloseTable(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
    result = CmpInitCallbacks(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
    result = CmpInitializeMachineHiveLoadedCallbacks(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
    result = CmpInitializeFreezeThaw(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
    result = HvInitializeHashLibrary(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
    result = CmpValidateGlobalFlushControlFlags(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
    result = CmpInitializeGlobalKeyLockTracker(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
    result = CmpInitializeTransactions(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
    result = CmpVolumeManagerInitialize(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
loc_00C55C7F:
    result = RtlInitUnicodeString(v_rsp - 968 - 80, *(unsigned __int64 *)(v_rip + 1786355 - 12), v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
    result = CmpHashUnicodeComponent(v_rsp - 968 - 80, *(unsigned __int64 *)(v_rip + 1786355 - 12), v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
    *(unsigned int *)(v_rip + 1786355) = (unsigned int)(result);
    v_r15 = (8) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_00C55C7F;
    result = CmpCreateObjectTypes(v_rsp - 968 - 80, *(unsigned __int64 *)(v_rip + 1786355 - 12), v_rip - 8257149, (unsigned int)((unsigned int)(v_r12 + 1)));
    if (sign_flag) {
        a4 = (int)((unsigned int)(result));
        a1 = v_r15 + 103;
        a3 = v_r12 + 1;
        v_stack_m4A8 = 0;
        a2 = v_r12 + 1;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpInitializeLightWeightTransactionType(a1, a2, a3, a4);
    if (sign_flag) {
        a3 = 24;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        v_stack_m4A8 = 0;
        a1 = a3 + 79;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpInitializeRegistryProcess(a1, a2, a3, a4);
    if (sign_flag) {
        a3 = 25;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        v_stack_m4A8 = 0;
        a1 = a3 + 78;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpAttachToRegistryProcess(v_rsp - 968 - 40, a2, a3, a4);
    result = CmpLockRegistryExclusive(v_rsp - 968 - 40, a2, a3, a4);
    a2 = 0;
    result = CmpInitializePreloadedHives(a1, a2, a3, a4);
    a4 = 0;
    v_stack_m468 = v_rsp - 968 + 16;
    v_stack_m470 = 0;
    v_stack_m478 = 0;
    a2 = 0;
    v_stack_m480 = 0;
    v_stack_m488 = 0;
    v_stack_m490 = 0x20000ULL;
    v_stack_m498 = 0;
    v_stack_m4A0 = 0;
    v_stack_m4A8 = 0;
    result = CmpCreateHive(v_rip + 3685724, a2, (unsigned int)((unsigned int)(v_r12 + 1)), a4);
    if (sign_flag) {
        a3 = 2;
        a4 = (int)((unsigned int)(result));
        result = v_rsp - 968 + 16;
        a2 = v_r12 + 1;
        v_stack_m4A8 = result;
        a1 = a3 + 101;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpInitializeKcbCache(*(unsigned __int64 *)(v_rip + 3685629), 128, a3, a4);
    if (sign_flag) {
        a3 = 3;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        v_stack_m4A8 = 0;
        a1 = a3 + 100;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpCreateRegistryRoot(a1, a2, a3, a4);
    if (sign_flag) {
        a4 = 0;
        v_stack_m4A8 = 0;
        a2 = v_r12 + 1;
        a3 = a4 + 4;
        a1 = a4 + 103;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a1 = 0;
    result = CmpInitSiloSupport(a1, a2, a3, a4);
    if (sign_flag) {
        a3 = 26;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        v_stack_m4A8 = 0;
        a1 = a3 + 77;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpHiveRootSecurityDescriptor(a1, a2, a3, a4);
    v_stack_m498 = 0;
    v_stack_m4A0 = 0;
    *(unsigned __int64 *)(v_rsp - 968 - 120) = v_rip + 3686336;
    v_stack_m450 = 48;
    a4 = 0;
    v_stack_m4A8 = v_rip - 1093533;
    *(unsigned __int64 *)(v_rsp - 968 - 128) = 0;
    *(unsigned int *)(v_rsp - 968 - 112) = 576;
    *(unsigned __int64 *)(v_rsp - 968 - 104) = result;
    *(unsigned __int64 *)(v_rsp - 968 - 96) = 0;
    result = ZwCreateKey(v_stack_m458, (unsigned int)(0x2001FULL), v_stack_m450, a4);
    if (sign_flag) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_stack_m450, a4);
        a3 = 5;
        v_stack_m4A8 = 0;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        a1 = a3 + 98;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = ZwClose(v_stack_m458, a2, a3, a4);
    v_stack_m498 = 0;
    *(unsigned __int64 *)(v_rsp - 968 - 120) = v_rip + 3687660;
    v_stack_m4A0 = 0;
    a4 = 0;
    v_stack_m4A8 = v_rip - 1093665;
    v_stack_m450 = 48;
    *(unsigned __int64 *)(v_rsp - 968 - 128) = 0;
    *(unsigned int *)(v_rsp - 968 - 112) = 576;
    *(unsigned __int64 *)(v_rsp - 968 - 104) = result;
    *(unsigned __int64 *)(v_rsp - 968 - 96) = 0;
    result = ZwCreateKey(v_stack_m458, (unsigned int)(0x2001FULL), v_stack_m450, a4);
    if (sign_flag) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_stack_m450, a4);
        a3 = 6;
        v_stack_m4A8 = 0;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        a1 = a3 + 97;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = ZwClose(v_stack_m458, a2, a3, a4);
    *(unsigned __int64 *)(v_rsp - 968 - 120) = v_rip + 3687532;
    v_stack_m450 = 48;
    v_stack_m498 = v_stack_m458;
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 968 - 128) = 0;
    v_stack_m4A0 = v_rsp - 968 + 448;
    a3 = 0;
    v_stack_m4A8 = 0x2001FULL;
    *(unsigned int *)(v_rsp - 968 - 112) = 576;
    *(unsigned __int64 *)(v_rsp - 968 - 104) = result;
    *(unsigned __int64 *)(v_rsp - 968 - 96) = 0;
    *(unsigned int *)(v_rsp - 968 + 448) = 65;
    result = ObOpenObjectByName(v_stack_m450, *(unsigned __int64 *)(v_rip + 3607451), a3, a4);
    a2 = 0;
    if (sign_flag) {
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
        a2 = 0;
        a1 = v_rsp - 968 + 448;
        result = CmpCleanupParseContext(a1, a2, a3, a4);
        a4 = (int)((unsigned int)(result));
        v_stack_m4A8 = 0;
        a3 = 7;
        a2 = v_r12 + 1;
        a1 = 103;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpCleanupParseContext(v_rsp - 968 + 448, a2, a3, a4);
    result = ZwClose(v_stack_m458, a2, a3, a4);
    v_stack_m498 = 0;
    *(unsigned __int64 *)(v_rsp - 968 - 120) = v_rip + 3687376;
    v_stack_m4A0 = 0;
    a4 = 0;
    v_stack_m4A8 = v_rip - 1093981;
    v_stack_m450 = 48;
    *(unsigned __int64 *)(v_rsp - 968 - 128) = 0;
    *(unsigned int *)(v_rsp - 968 - 112) = 576;
    *(unsigned __int64 *)(v_rsp - 968 - 104) = result;
    *(unsigned __int64 *)(v_rsp - 968 - 96) = 0;
    result = ZwCreateKey(v_stack_m458, (unsigned int)(0x2001FULL), v_stack_m450, a4);
    if (sign_flag) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_stack_m450, a4);
        a3 = 8;
        v_stack_m4A8 = 0;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        a1 = a3 + 95;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = ZwClose(v_stack_m458, a2, a3, a4);
    *(unsigned __int8 *)(v_rip + 3684883) = (unsigned __int8)(v_r12 + 1);
    result = CmpInitializeLoadOptions(a1, a2, a3, a4);
    result = CmpInitializePreloadedHives(a1, (unsigned int)((unsigned int)(v_r12 + 1)), a3, a4);
    if (sign_flag) {
        a3 = 20;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        v_stack_m4A8 = 0;
        a1 = a3 + 83;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a2 = 0;
    result = CmpCreateControlSet(v_rip + 149252, a2, a3, a4);
    if (sign_flag) {
        a3 = 13;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        v_stack_m4A8 = 0;
        a1 = a3 + 90;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if ((*(unsigned int *)(v_rip + 3678273)) != 0) {
        result = *(unsigned __int64 *)(v_rip + 3600184);
    }
    if ((*(unsigned int *)(v_rip + 2726542)) == 0) goto loc_00C5612D;
    if ((*(unsigned int *)(v_rip + 2726541)) == 0) goto loc_00C560FE;
loc_00C560EE:
    v_r14 = (7) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_00C560EE;
    goto loc_00C5612D;
loc_00C560FE:
    *(unsigned __int8 *)(v_rip + 1783944) = 0;
    result = (unsigned int)(0x8000ULL);
    if ((*(unsigned int *)(v_rip + 2726507)) == 0) {
        result = 0x8000ULL;
    }
    *(unsigned __int8 *)(v_rip + 1784654) = 0;
    *(unsigned __int8 *)(v_rip + 1784830) = (unsigned __int8)(v_r12 + 1);
loc_00C5612D:
    a2 = 0;
    result = memset(v_rsp - 968 + 16, a2, 432, a4);
    a4 = 0;
    v_stack_m468 = v_rsp - 968 + 16;
    v_stack_m470 = 0;
    v_stack_m478 = 0;
    a2 = 0;
    v_stack_m480 = 0;
    v_stack_m488 = 0;
    v_stack_m490 = 0x20000ULL;
    v_stack_m498 = 0;
    v_stack_m4A0 = 0;
    v_stack_m4A8 = 0;
    result = CmpCreateHive(v_rsp - 968 - 88, a2, (unsigned int)((unsigned int)(v_r12 + 1)), a4);
    if (sign_flag) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)(v_r12 + 1)), a4);
        a3 = 16;
        result = v_rsp - 968 + 16;
        a4 = (int)((unsigned int)(result));
        v_stack_m4A8 = result;
        a2 = v_r12 + 1;
        a1 = a3 + 87;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_stack_m470 = v_rsp - 968 + 16;
    v_stack_m478 = (unsigned __int8)(v_r12 + 1);
    a2 = 0;
    v_stack_m480 = 0;
    v_stack_m488 = 0;
    v_stack_m490 = result;
    v_stack_m498 = 0;
    v_stack_m4A0 = 0;
    v_stack_m4A8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1783547)));
    result = CmpLinkHiveToMaster(v_rip + 3686897, a2, *(unsigned __int64 *)(v_rsp - 968 - 88), (unsigned __int8)(v_r12 + 1));
    if ((unsigned int)(result) != 0) {
        a3 = 17;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        v_stack_m4A8 = 0;
        a1 = a3 + 86;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpAddToHiveFileList(*(unsigned __int64 *)(v_rsp - 968 - 88), a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    *(unsigned __int64 *)(v_rip + 1783423) = *(unsigned __int64 *)(v_rsp - 968 - 88);
    result = CmpInitializeHardwareConfiguration(a1, a2, a3, a4);
    if (sign_flag) {
        a3 = 18;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        v_stack_m4A8 = 0;
        a1 = a3 + 85;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpInitializeDriverStores(a1, a2, a3, a4);
    if (sign_flag) {
        a3 = 19;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        v_stack_m4A8 = 0;
        a1 = a3 + 84;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpCreateExtendedControlSets(a1, a2, a3, a4);
    if (sign_flag) {
        a3 = 27;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        v_stack_m4A8 = 0;
        a1 = a3 + 76;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpCreateHardwareProfiles(a1, a2, a3, a4);
    result = ext_ms_win_ntos_kcminitcfg_l1_1_0_dll_CmSetInitMachineConfig(a1, a2, a3, a4);
    result = CmpUnlockRegistry(a1, a2, a3, a4);
    result = CmpMarkCurrentProfileDirty(a1, a2, a3, a4);
    result = CmpInitializeMachineDependentConfiguration(a1, a2, a3, a4);
    if (sign_flag) {
        a3 = 21;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        v_stack_m4A8 = 0;
        a1 = a3 + 82;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpSetSystemValues(a1, a2, a3, a4);
    if (sign_flag) {
        a3 = 22;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        v_stack_m4A8 = 0;
        a1 = a3 + 81;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpMigrateOOBELanguageToInstallationLanguage(a1, a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rip + 3875770), a2, a3, a4);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 240))) < 104) goto loc_00C56366;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 96) == 0) goto loc_00C56366;
    result = CmpSetNetworkValue(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 96), a2, a3, a4);
    if (sign_flag) {
        a3 = 23;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        v_stack_m4A8 = 0;
        a1 = a3 + 80;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmFcInitSystem2(a1, a2, a3, a4);
    if (sign_flag) {
        a3 = 26;
        a4 = (int)((unsigned int)(result));
        a2 = v_r12 + 1;
        v_stack_m4A8 = 0;
        a1 = a3 + 77;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpDetachFromRegistryProcess(v_rsp - 968 - 40, a2, a3, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1768) = *(unsigned __int64 *)(v_rsp - 968 - 64);
    a1 = (*(unsigned __int64 *)(v_rsp - 968 + 912)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmInitSystem1(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m44C;
    uint64_t v_stack_m450;
    uint64_t v_stack_m458;
    uint64_t v_stack_m468;
    uint64_t v_stack_m470;
    uint64_t v_stack_m478;
    uint64_t v_stack_m480;
    uint32_t v_stack_m488;
    uint16_t v_stack_m490;
    uint32_t v_stack_m498;
    uint64_t v_stack_m4A0;
    uint32_t v_stack_m4A8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (0x4A0ULL);
    result = (*(uint64_t *)(v_rip + 0x1B4D47)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x3C8 + 0x390) = result;
    local_r12 = 0;
    v_stack_m458 = 0;
    result = 0;
    v_stack_m44C = 0;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x30) = 0;
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x3C8 - 0x6C) = 0;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x40) = v_xmm0;
    result = memset(local_rsp - 968 + 448, Arg2, 464, a4);
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x50) = v_xmm0;
    result = memset(local_rsp - 968 + 16, Arg2, 432, a4);
    *(uint64_t *)(local_rsp - 0x3C8 - 0x28) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x18) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x8) = v_xmm0;
    result = CmpInitializeThreadInfo(local_rsp - 968 - 64, Arg2, 432, a4);
    result = CmpInitializeParseContext(local_rsp - 968 + 448, Arg2, 432, a4);
    *(uint64_t *)(v_rip + 0x2A21E2) = v_rip + 3608673;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x36E6B7)) != 0) {
        *(uint8_t *)(v_rip + 0x38256B) = (uint8_t)(*(uint8_t *)(v_rip + 0x36E6B7));
        *(uint8_t *)(v_rip + 0x382562) = (uint8_t)(local_r12 + 1);
        *(uint8_t *)(v_rip + 0x38256D) = (uint8_t)(local_r12 + 1);
    }
    if ((*(uint32_t *)(v_rip + 0x29A0AC)) != 0) {
        *(uint8_t *)(v_rip + 0x38254B) = (uint8_t)(local_r12 + 1);
    }
    if ((*(uint8_t *)(v_rip + 0x382544)) == 0) goto loc_00C55AEA;
loc_00C55AD5:
    if ((*(uint64_t *)(v_rip + 0x1B3DF9 - 0x20)) != 0) {
    }
    result = (v_rip + 1785337) + (184);
    Arg1 = (7) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_00C55AD5;
loc_00C55AEA:
    result = CmpInitializeRegistryNames(Arg1, Arg2, 432, a4);
    result = CmpInitGlobalQuotaAllowed(Arg1, Arg2, 432, a4);
    *(uint64_t *)(v_rip + 0x2A216E) = 0;
    *(uint64_t *)(v_rip + 0x29FE88) = v_rip + 2752149;
    *(uint64_t *)(v_rip + 0x29FE79) = v_rip + 2752149;
    *(uint64_t *)(v_rip + 0x384202) = v_rip + 3686927;
    *(uint64_t *)(v_rip + 0x3841F3) = v_rip + 3686927;
    *(uint64_t *)(v_rip + 0x2A214C) = 0;
    *(uint64_t *)(v_rip + 0x2A1FED) = 0;
    *(uint64_t *)(v_rip + 0x2A1FEE) = 0;
    *(uint64_t *)(v_rip + 0x2A1FEF) = 0;
    *(uint64_t *)(v_rip + 0x29FE58) = 0;
    *(uint64_t *)(v_rip + 0x29FE31) = 0;
    result = Feature_Servicing_CmpRegistryLockToCacheAwarePushlock__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, 432, v_rip + 3686927);
    if ((uint32_t)(result) != 0) goto loc_00C55B7A;
    *(uint32_t *)(v_rip + 0x2A15A2) = 0;
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    result = ExInitializeResourceLite2(v_rip + 2757953, Arg2, 432, v_rip + 3686927);
    *(uint64_t *)(v_rip + 0x2A1598) = v_rip + 2757953;
    goto loc_00C55B97;
loc_00C55B7A:
    *(uint32_t *)(v_rip + 0x2A1584) = (uint32_t)(local_r12 + 1);
    result = ExAllocateCacheAwarePushLock((uint32_t)((uint32_t)(local_r12 + 1)), Arg2, 432, v_rip + 3686927);
    *(uint64_t *)(v_rip + 0x2A1510) = result;
    *(uint64_t *)(v_rip + 0x2A1579) = result;
loc_00C55B97:
    *(uint32_t *)(v_rip + 0x29FD9B) = (uint32_t)(local_r12 + 1);
    *(uint64_t *)(v_rip + 0x29FDBC) = v_rip + 2751938;
    *(uint64_t *)(v_rip + 0x29FDAD) = v_rip + 2751938;
    *(uint64_t *)(v_rip + 0x382A1F) = v_rip + 3680798;
    *(uint64_t *)(v_rip + 0x382A10) = v_rip + 3680798;
    *(uint64_t *)(v_rip + 0x29FD79) = 0;
    *(uint32_t *)(v_rip + 0x29FD7A) = 0;
    *(uint16_t *)(v_rip + 0x29FD7A) = (uint16_t)(local_r12 + 1);
    *(uint8_t *)(v_rip + 0x29FD75) = 6;
    *(uint32_t *)(v_rip + 0x29FD70) = 0;
    result = CmpInitializeNameCache((uint32_t)((uint32_t)(local_r12 + 1)), Arg2, 432, v_rip + 3686927);
    v_stack_m488 = 0;
    v_stack_m490 = 0;
    v_stack_m498 = 0x626B4D43ULL;
    v_stack_m4A0 = 312;
    v_stack_m4A8 = 0;
    result = ExInitializeLookasideListExInternal(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
    result = CmpInitSIDToHiveMapping(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
    result = CmpAdminSystemSecurityDescriptor(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
    *(uint64_t *)(v_rip + 0x299FE8) = result;
    result = CmpInitializeTrustedInstallerSid(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
    result = CmpInitializeDelayedCloseTable(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
    result = CmpInitCallbacks(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
    result = CmpInitializeMachineHiveLoadedCallbacks(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
    result = CmpInitializeFreezeThaw(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
    result = HvInitializeHashLibrary(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
    result = CmpValidateGlobalFlushControlFlags(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
    result = CmpInitializeGlobalKeyLockTracker(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
    result = CmpInitializeTransactions(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
    result = CmpVolumeManagerInitialize(v_rip + 1928871, v_rip - 8216234, v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
loc_00C55C7F:
    result = RtlInitUnicodeString(local_rsp - 968 - 80, *(uint64_t *)(v_rip + 0x1B41F3 - 0xC), v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
    result = CmpHashUnicodeComponent(local_rsp - 968 - 80, *(uint64_t *)(v_rip + 0x1B41F3 - 0xC), v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
    *(uint32_t *)(v_rip + 0x1B41F3) = (uint32_t)(result);
    local_r15 = (8) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_00C55C7F;
    result = CmpCreateObjectTypes(local_rsp - 968 - 80, *(uint64_t *)(v_rip + 0x1B41F3 - 0xC), v_rip - 8257149, (uint32_t)((uint32_t)(local_r12 + 1)));
    if (sign_flag) {
        a4 = (int32_t)((uint32_t)(result));
        Arg1 = local_r15 + 103;
        a3 = local_r12 + 1;
        v_stack_m4A8 = 0;
        Arg2 = local_r12 + 1;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = CmpInitializeLightWeightTransactionType(Arg1, Arg2, a3, a4);
    if (sign_flag) {
        a3 = 24;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        v_stack_m4A8 = 0;
        Arg1 = a3 + 79;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = CmpInitializeRegistryProcess(Arg1, Arg2, a3, a4);
    if (sign_flag) {
        a3 = 25;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        v_stack_m4A8 = 0;
        Arg1 = a3 + 78;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = CmpAttachToRegistryProcess(local_rsp - 968 - 40, Arg2, a3, a4);
    result = CmpLockRegistryExclusive(local_rsp - 968 - 40, Arg2, a3, a4);
    Arg2 = 0;
    result = CmpInitializePreloadedHives(Arg1, Arg2, a3, a4);
    a4 = 0;
    v_stack_m468 = local_rsp - 968 + 16;
    v_stack_m470 = 0;
    v_stack_m478 = 0;
    Arg2 = 0;
    v_stack_m480 = 0;
    v_stack_m488 = 0;
    v_stack_m490 = 0x20000ULL;
    v_stack_m498 = 0;
    v_stack_m4A0 = 0;
    v_stack_m4A8 = 0;
    result = CmpCreateHive(v_rip + 3685724, Arg2, (uint32_t)((uint32_t)(local_r12 + 1)), a4);
    if (sign_flag) {
        a3 = 2;
        a4 = (int32_t)((uint32_t)(result));
        result = local_rsp - 968 + 16;
        Arg2 = local_r12 + 1;
        v_stack_m4A8 = result;
        Arg1 = a3 + 101;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = CmpInitializeKcbCache(*(uint64_t *)(v_rip + 0x383CFD), 128, a3, a4);
    if (sign_flag) {
        a3 = 3;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        v_stack_m4A8 = 0;
        Arg1 = a3 + 100;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = CmpCreateRegistryRoot(Arg1, Arg2, a3, a4);
    if (sign_flag) {
        a4 = 0;
        v_stack_m4A8 = 0;
        Arg2 = local_r12 + 1;
        a3 = a4 + 4;
        Arg1 = a4 + 103;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    Arg1 = 0;
    result = CmpInitSiloSupport(Arg1, Arg2, a3, a4);
    if (sign_flag) {
        a3 = 26;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        v_stack_m4A8 = 0;
        Arg1 = a3 + 77;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = CmpHiveRootSecurityDescriptor(Arg1, Arg2, a3, a4);
    v_stack_m498 = 0;
    v_stack_m4A0 = 0;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x78) = v_rip + 3686336;
    v_stack_m450 = 48;
    a4 = 0;
    v_stack_m4A8 = v_rip - 1093533;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x80) = 0;
    *(uint32_t *)(local_rsp - 0x3C8 - 0x70) = 576;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x68) = result;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x60) = 0;
    result = ZwCreateKey(v_stack_m458, (uint32_t)(0x2001FULL), v_stack_m450, a4);
    if (sign_flag) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m450, a4);
        a3 = 5;
        v_stack_m4A8 = 0;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        Arg1 = a3 + 98;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = ZwClose(v_stack_m458, Arg2, a3, a4);
    v_stack_m498 = 0;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x78) = v_rip + 3687660;
    v_stack_m4A0 = 0;
    a4 = 0;
    v_stack_m4A8 = v_rip - 1093665;
    v_stack_m450 = 48;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x80) = 0;
    *(uint32_t *)(local_rsp - 0x3C8 - 0x70) = 576;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x68) = result;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x60) = 0;
    result = ZwCreateKey(v_stack_m458, (uint32_t)(0x2001FULL), v_stack_m450, a4);
    if (sign_flag) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m450, a4);
        a3 = 6;
        v_stack_m4A8 = 0;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        Arg1 = a3 + 97;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = ZwClose(v_stack_m458, Arg2, a3, a4);
    *(uint64_t *)(local_rsp - 0x3C8 - 0x78) = v_rip + 3687532;
    v_stack_m450 = 48;
    v_stack_m498 = v_stack_m458;
    a4 = 0;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x80) = 0;
    v_stack_m4A0 = local_rsp - 968 + 448;
    a3 = 0;
    v_stack_m4A8 = 0x2001FULL;
    *(uint32_t *)(local_rsp - 0x3C8 - 0x70) = 576;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x68) = result;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x60) = 0;
    *(uint32_t *)(local_rsp - 0x3C8 + 0x1C0) = 65;
    result = ObOpenObjectByName(v_stack_m450, *(uint64_t *)(v_rip + 0x370B9B), a3, a4);
    Arg2 = 0;
    if (sign_flag) {
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
        Arg2 = 0;
        Arg1 = local_rsp - 968 + 448;
        result = CmpCleanupParseContext(Arg1, Arg2, a3, a4);
        a4 = (int32_t)((uint32_t)(result));
        v_stack_m4A8 = 0;
        a3 = 7;
        Arg2 = local_r12 + 1;
        Arg1 = 103;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = CmpCleanupParseContext(local_rsp - 968 + 448, Arg2, a3, a4);
    result = ZwClose(v_stack_m458, Arg2, a3, a4);
    v_stack_m498 = 0;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x78) = v_rip + 3687376;
    v_stack_m4A0 = 0;
    a4 = 0;
    v_stack_m4A8 = v_rip - 1093981;
    v_stack_m450 = 48;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x80) = 0;
    *(uint32_t *)(local_rsp - 0x3C8 - 0x70) = 576;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x68) = result;
    *(uint64_t *)(local_rsp - 0x3C8 - 0x60) = 0;
    result = ZwCreateKey(v_stack_m458, (uint32_t)(0x2001FULL), v_stack_m450, a4);
    if (sign_flag) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m450, a4);
        a3 = 8;
        v_stack_m4A8 = 0;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        Arg1 = a3 + 95;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = ZwClose(v_stack_m458, Arg2, a3, a4);
    *(uint8_t *)(v_rip + 0x383A13) = (uint8_t)(local_r12 + 1);
    result = CmpInitializeLoadOptions(Arg1, Arg2, a3, a4);
    result = CmpInitializePreloadedHives(Arg1, (uint32_t)((uint32_t)(local_r12 + 1)), a3, a4);
    if (sign_flag) {
        a3 = 20;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        v_stack_m4A8 = 0;
        Arg1 = a3 + 83;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    Arg2 = 0;
    result = CmpCreateControlSet(v_rip + 149252, Arg2, a3, a4);
    if (sign_flag) {
        a3 = 13;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        v_stack_m4A8 = 0;
        Arg1 = a3 + 90;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    if ((*(uint32_t *)(v_rip + 0x382041)) != 0) {
        result = *(uint64_t *)(v_rip + 0x36EF38);
    }
    if ((*(uint32_t *)(v_rip + 0x299A8E)) == 0) goto loc_00C5612D;
    if ((*(uint32_t *)(v_rip + 0x299A8D)) == 0) goto loc_00C560FE;
loc_00C560EE:
    local_r14 = (7) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_00C560EE;
    goto loc_00C5612D;
loc_00C560FE:
    *(uint8_t *)(v_rip + 0x1B3888) = 0;
    result = (uint32_t)(0x8000ULL);
    if ((*(uint32_t *)(v_rip + 0x299A6B)) == 0) {
        result = 0x8000ULL;
    }
    *(uint8_t *)(v_rip + 0x1B3B4E) = 0;
    *(uint8_t *)(v_rip + 0x1B3BFE) = (uint8_t)(local_r12 + 1);
loc_00C5612D:
    Arg2 = 0;
    result = memset(local_rsp - 968 + 16, Arg2, 432, a4);
    a4 = 0;
    v_stack_m468 = local_rsp - 968 + 16;
    v_stack_m470 = 0;
    v_stack_m478 = 0;
    Arg2 = 0;
    v_stack_m480 = 0;
    v_stack_m488 = 0;
    v_stack_m490 = 0x20000ULL;
    v_stack_m498 = 0;
    v_stack_m4A0 = 0;
    v_stack_m4A8 = 0;
    result = CmpCreateHive(local_rsp - 968 - 88, Arg2, (uint32_t)((uint32_t)(local_r12 + 1)), a4);
    if (sign_flag) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)(local_r12 + 1)), a4);
        a3 = 16;
        result = local_rsp - 968 + 16;
        a4 = (int32_t)((uint32_t)(result));
        v_stack_m4A8 = result;
        Arg2 = local_r12 + 1;
        Arg1 = a3 + 87;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    v_stack_m470 = local_rsp - 968 + 16;
    v_stack_m478 = (uint8_t)(local_r12 + 1);
    Arg2 = 0;
    v_stack_m480 = 0;
    v_stack_m488 = 0;
    v_stack_m490 = result;
    v_stack_m498 = 0;
    v_stack_m4A0 = 0;
    v_stack_m4A8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1B36FB)));
    result = CmpLinkHiveToMaster(v_rip + 3686897, Arg2, *(uint64_t *)(local_rsp - 0x3C8 - 0x58), (uint8_t)(local_r12 + 1));
    if ((uint32_t)(result) != 0) {
        a3 = 17;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        v_stack_m4A8 = 0;
        Arg1 = a3 + 86;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = CmpAddToHiveFileList(*(uint64_t *)(local_rsp - 0x3C8 - 0x58), Arg2, a3, a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, a3, a4);
    *(uint64_t *)(v_rip + 0x1B367F) = *(uint64_t *)(local_rsp - 0x3C8 - 0x58);
    result = CmpInitializeHardwareConfiguration(Arg1, Arg2, a3, a4);
    if (sign_flag) {
        a3 = 18;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        v_stack_m4A8 = 0;
        Arg1 = a3 + 85;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = CmpInitializeDriverStores(Arg1, Arg2, a3, a4);
    if (sign_flag) {
        a3 = 19;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        v_stack_m4A8 = 0;
        Arg1 = a3 + 84;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = CmpCreateExtendedControlSets(Arg1, Arg2, a3, a4);
    if (sign_flag) {
        a3 = 27;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        v_stack_m4A8 = 0;
        Arg1 = a3 + 76;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = CmpCreateHardwareProfiles(Arg1, Arg2, a3, a4);
    result = kernel_indirect_call(Arg1, Arg2, a3, a4);
    result = CmpUnlockRegistry(Arg1, Arg2, a3, a4);
    result = CmpMarkCurrentProfileDirty(Arg1, Arg2, a3, a4);
    result = CmpInitializeMachineDependentConfiguration(Arg1, Arg2, a3, a4);
    if (sign_flag) {
        a3 = 21;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        v_stack_m4A8 = 0;
        Arg1 = a3 + 82;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = CmpSetSystemValues(Arg1, Arg2, a3, a4);
    if (sign_flag) {
        a3 = 22;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        v_stack_m4A8 = 0;
        Arg1 = a3 + 81;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = CmpMigrateOOBELanguageToInstallationLanguage(Arg1, Arg2, a3, a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_rip + 0x3B23BA), Arg2, a3, a4);
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0))) < 104) goto loc_00C56366;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x60) == 0) goto loc_00C56366;
    result = CmpSetNetworkValue(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x60), Arg2, a3, a4);
    if (sign_flag) {
        a3 = 23;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        v_stack_m4A8 = 0;
        Arg1 = a3 + 80;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = CmFcInitSystem2(Arg1, Arg2, a3, a4);
    if (sign_flag) {
        a3 = 26;
        a4 = (int32_t)((uint32_t)(result));
        Arg2 = local_r12 + 1;
        v_stack_m4A8 = 0;
        Arg1 = a3 + 77;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = CmpDetachFromRegistryProcess(local_rsp - 968 - 40, Arg2, a3, a4);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6E8) = *(uint64_t *)(local_rsp - 0x3C8 - 0x40);
    Arg1 = (*(uint64_t *)(local_rsp - 0x3C8 + 0x390)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xF0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C559CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
