# IopInitializePlugPlayServices

- RVA: `0x00C2F298`–`0x00C300DF` (길이 `3,655` bytes)
- VA: `0x0000000140C2F298`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C8188`
- 디코드: `769`개 명령, `3,655/3,655` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **107**; 고유 호출 대상: **81**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **178**

### Outgoing calls
- `0x00C2F353` → [CmRegisterSystemHiveLimitCallback](../../page/7E/CmRegisterSystemHiveLimitCallback_function_007E213C.md) (function, `0x007E213C`)
- `0x00C2F3AC` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x00C2F3CC` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00C2F3F2` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00C2F40F` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C2F41E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C2F439` → [PnpLogEvent](../../page/72/PnpLogEvent_function_0072C8FC.md) (function, `0x0072C8FC`)
- `0x00C2F443` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C2F44D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C2F457` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00C2F4CB` → [PiInitFirmwareResources](../C3/PiInitFirmwareResources_function_00C301C8.md) (function, `0x00C301C8`)
- `0x00C2F4E8` → [PpInitializeBootDDB](../C3/PpInitializeBootDDB_function_00C34018.md) (function, `0x00C34018`)
- `0x00C2F4ED` → [PipInitDeviceOverrideCache](../C3/PipInitDeviceOverrideCache_function_00C312C8.md) (function, `0x00C312C8`)
- `0x00C2F51D` → [PiInitCacheGroupInformation](../C3/PiInitCacheGroupInformation_function_00C300E8.md) (function, `0x00C300E8`)
- `0x00C2F57F` → [IopInitializeResourceMap](../C3/IopInitializeResourceMap_function_00C33198.md) (function, `0x00C33198`)
- `0x00C2F5A5` → [ArbInitializeOsInaccessibleRange](ArbInitializeOsInaccessibleRange_function_00C25F9C.md) (function, `0x00C25F9C`)
- `0x00C2F5AA` → [ArbLibraryInitialize](../../page/70/ArbLibraryInitialize_function_0070F180.md) (function, `0x0070F180`)
- `0x00C2F5B9` → [IopPortInitialize](../../page/72/IopPortInitialize_function_0072F500.md) (function, `0x0072F500`)
- `0x00C2F5C8` → [IopMemInitialize](../../page/72/IopMemInitialize_function_0072F078.md) (function, `0x0072F078`)
- `0x00C2F5D7` → [IopDmaInitialize](../../page/72/IopDmaInitialize_function_0072F634.md) (function, `0x0072F634`)
- `0x00C2F5E6` → [IopIrqInitialize](../../page/72/IopIrqInitialize_function_0072F758.md) (function, `0x0072F758`)
- `0x00C2F5F5` → [IopBusNumberInitialize](../../page/72/IopBusNumberInitialize_function_0072F828.md) (function, `0x0072F828`)
- `0x00C2F606` → [PiPnpRtlInit](../../page/73/PiPnpRtlInit_function_007300A4.md) (function, `0x007300A4`)
- `0x00C2F615` → [PipMigratePnpState](../C3/PipMigratePnpState_function_00C317D4.md) (function, `0x00C317D4`)
- `0x00C2F61A` → [PiDmInit](../C3/PiDmInit_function_00C343EC.md) (function, `0x00C343EC`)
- `0x00C2F63D` → [_PnpCtxGetCachedContextBaseKey](../../page/8E/_PnpCtxGetCachedContextBaseKey_function_008EFB2C.md) (function, `0x008EFB2C`)
- `0x00C2F67B` → [IopCreateRegistryKeyEx](../../page/A8/IopCreateRegistryKeyEx_function_00A89038.md) (function, `0x00A89038`)
- `0x00C2F69B` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00C2F6C2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C2F6DA` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00C2F701` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C2F71C` → [PnpGetRegistryDword](../../text/4B/PnpGetRegistryDword_function_004BFDE8.md) (function, `0x004BFDE8`)
- `0x00C2F737` → [PiUEventProcessRegistry](../C3/PiUEventProcessRegistry_function_00C33EC0.md) (function, `0x00C33EC0`)
- `0x00C2F752` → [PnpGetRegistryDword](../../text/4B/PnpGetRegistryDword_function_004BFDE8.md) (function, `0x004BFDE8`)
- `0x00C2F7A7` → [PipUpdateAsyncOptionsCallback](../../page/72/PipUpdateAsyncOptionsCallback_function_00723740.md) (function, `0x00723740`)
- `0x00C2F7D7` → [IopOpenRegistryKeyEx](../../page/A5/IopOpenRegistryKeyEx_function_00A51B44.md) (function, `0x00A51B44`)
- `0x00C2F7E9` → [PipUpdateSetupInProgress](../../page/72/PipUpdateSetupInProgress_function_007237F8.md) (function, `0x007237F8`)
- `0x00C2F802` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00C2F82E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C2F847` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00C2F873` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C2F88F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00C2F8B9` → [PipUpdateSetupInProgressNotify](../../page/72/PipUpdateSetupInProgressNotify_function_00723918.md) (function, `0x00723918`)
- `0x00C2F8D1` → [PipHardwareConfigInit](../C3/PipHardwareConfigInit_function_00C30D24.md) (function, `0x00C30D24`)
- `0x00C2F8E5` → [PipCheckSystemFirmwareUpdated](../C3/PipCheckSystemFirmwareUpdated_function_00C3048C.md) (function, `0x00C3048C`)
- `0x00C2F8EC` → [PiDcInit](../C3/PiDcInit_function_00C344DC.md) (function, `0x00C344DC`)
- `0x00C2F905` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C2F90E` → [PiAuCreateUserSids](../C3/PiAuCreateUserSids_function_00C34C2C.md) (function, `0x00C34C2C`)
- `0x00C2F91D` → [PiAuCreateStandardSecurityObject](../C3/PiAuCreateStandardSecurityObject_function_00C34710.md) (function, `0x00C34710`)
- `0x00C2F92C` → [PiAuCreateLocalSystemSecurityObject](../C3/PiAuCreateLocalSystemSecurityObject_function_00C34570.md) (function, `0x00C34570`)
- `0x00C2F937` → [PiAuFreeUserSids](../C3/PiAuFreeUserSids_function_00C34E54.md) (function, `0x00C34E54`)
- `0x00C2F944` → [PiDqInit](../C3/PiDqInit_function_00C35120.md) (function, `0x00C35120`)
- `0x00C2F953` → [PpDevCfgInit](../C3/PpDevCfgInit_function_00C351A4.md) (function, `0x00C351A4`)
- `0x00C2F962` → [PipResetDevices](../C3/PipResetDevices_function_00C32190.md) (function, `0x00C32190`)
- `0x00C2F989` → [CmCreateDevice](../../page/8F/CmCreateDevice_function_008FFABC.md) (function, `0x008FFABC`)
- `0x00C2F9CC` → [CmSetDeviceRegProp](../../page/8F/CmSetDeviceRegProp_function_008FD68C.md) (function, `0x008FD68C`)
- `0x00C2FA00` → [CmSetDeviceRegProp](../../page/8F/CmSetDeviceRegProp_function_008FD68C.md) (function, `0x008FD68C`)
- `0x00C2FA08` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00C2FA43` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x00C2FA51` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x00C2FA5F` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x00C2FAF0` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x00C2FAFF` → [PnpAcquireDependencyRelationsLock](../../page/A0/PnpAcquireDependencyRelationsLock_function_00A06788.md) (function, `0x00A06788`)
- `0x00C2FB43` → [PnpReleaseDependencyRelationsLock](../../page/A0/PnpReleaseDependencyRelationsLock_function_00A06E14.md) (function, `0x00A06E14`)
- `0x00C2FC71` → [IoCreateDriver](../../page/AC/IoCreateDriver_function_00AC9D70.md) (function, `0x00AC9D70`)
- `0x00C2FCA3` → [IoCreateDevice](../../page/9A/IoCreateDevice_function_009A4B00.md) (function, `0x009A4B00`)
- `0x00C2FCC6` → [PipAllocateDeviceNode](../../page/A9/PipAllocateDeviceNode_function_00A9C8F8.md) (function, `0x00A9C8F8`)
- `0x00C2FCDC` → [IoDeleteDevice](../../text/26/IoDeleteDevice_function_0026FE90.md) (function, `0x0026FE90`)
- `0x00C2FCE8` → [IoDeleteDriver](../../page/71/IoDeleteDriver_function_0071D400.md) (function, `0x0071D400`)
- `0x00C2FCFF` → [PipSetDevNodeFlags](../../page/8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00C2FD10` → [PipSetDevNodeUserFlags](../../page/8F/PipSetDevNodeUserFlags_function_008FB8FC.md) (function, `0x008FB8FC`)
- `0x00C2FD32` → [PnpAllocateDeviceInstancePath](../../page/72/PnpAllocateDeviceInstancePath_function_0072DC30.md) (function, `0x0072DC30`)
- `0x00C2FD57` → [PnpCopyDeviceInstancePath](../../page/72/PnpCopyDeviceInstancePath_function_0072DC70.md) (function, `0x0072DC70`)
- `0x00C2FD6B` → [PnpMapDeviceObjectToDeviceInstance](../../page/A9/PnpMapDeviceObjectToDeviceInstance_function_00A9D884.md) (function, `0x00A9D884`)
- `0x00C2FD97` → [RtlGUIDFromString](../../page/8F/RtlGUIDFromString_function_008F1EF0.md) (function, `0x008F1EF0`)
- `0x00C2FDA3` → [PnpQueryAndSaveDeviceNodeCapabilities](../../page/8F/PnpQueryAndSaveDeviceNodeCapabilities_function_008FBCE8.md) (function, `0x008FBCE8`)
- `0x00C2FDB4` → [PipSetDevNodeState](../../text/47/PipSetDevNodeState_function_00470708.md) (function, `0x00470708`)
- `0x00C2FDCE` → [CmAddDeviceToContainer](../../page/8F/CmAddDeviceToContainer_function_008FF190.md) (function, `0x008FF190`)
- `0x00C2FDE4` → [PiDcHandleSystemFirmwareUpdate](../../page/73/PiDcHandleSystemFirmwareUpdate_function_00730B20.md) (function, `0x00730B20`)
- `0x00C2FDE9` → [PnpInitializePnpWatchdogs](../C3/PnpInitializePnpWatchdogs_function_00C3357C.md) (function, `0x00C3357C`)
- `0x00C2FDEE` → [PnpInitializeDeviceEvents](../C3/PnpInitializeDeviceEvents_function_00C3557C.md) (function, `0x00C3557C`)
- `0x00C2FDFD` → [PnpInitializeNotification](../C3/PnpInitializeNotification_function_00C32E64.md) (function, `0x00C32E64`)
- `0x00C2FE02` → [PnpBusTypeGuidInitialize](../C3/PnpBusTypeGuidInitialize_function_00C33C90.md) (function, `0x00C33C90`)
- `0x00C2FE3A` → [PiSwInit](../C3/PiSwInit_function_00C3567C.md) (function, `0x00C3567C`)
- `0x00C2FE4B` → [PiUEventInit](../C3/PiUEventInit_function_00C33D24.md) (function, `0x00C33D24`)
- `0x00C2FE78` → [IoCreateDriver](../../page/AC/IoCreateDriver_function_00AC9D70.md) (function, `0x00AC9D70`)
- `0x00C2FE89` → [PiDmaGuardInitialize](../../text/5A/PiDmaGuardInitialize_function_005A9F0C.md) (function, `0x005A9F0C`)
- `0x00C2FE98` → [IoInvalidateInit](../C3/IoInvalidateInit_function_00C32B78.md) (function, `0x00C32B78`)
- `0x00C2FE9D` → [PipProcessPendingServices](../C3/PipProcessPendingServices_function_00C3620C.md) (function, `0x00C3620C`)
- `0x00C2FEA6` → [PipProcessPendingOsExtensionResources](../C3/PipProcessPendingOsExtensionResources_function_00C36164.md) (function, `0x00C36164`)
- `0x00C2FECF` → [PnpRequestDeviceAction](../../text/47/PnpRequestDeviceAction_function_00477FF8.md) (function, `0x00477FF8`)
- `0x00C2FEF7` → [McGenEventRegister_EtwRegister](../../text/57/McGenEventRegister_EtwRegister_function_0057EF04.md) (function, `0x0057EF04`)
- `0x00C2FF2A` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (function, `0x00920960`)
- `0x00C2FF48` → [TlgRegisterAggregateProvider](../../page/70/TlgRegisterAggregateProvider_function_0070526C.md) (function, `0x0070526C`)
- `0x00C2FF54` → [TlgRegisterAggregateProvider](../../page/70/TlgRegisterAggregateProvider_function_0070526C.md) (function, `0x0070526C`)
- `0x00C2FF65` → [TraceLoggingRegisterEx_EtwRegister_EtwSetInformation](../../page/92/TraceLoggingRegisterEx_EtwRegister_EtwSetInformation_function_009208A0.md) (function, `0x009208A0`)
- `0x00C2FF6C` → [PiDcInit](../C3/PiDcInit_function_00C344DC.md) (function, `0x00C344DC`)
- `0x00C2FF7B` → [PiUEventInit](../C3/PiUEventInit_function_00C33D24.md) (function, `0x00C33D24`)
- `0x00C2FFC9` → [PnpDiagnosticTrace](../../text/26/PnpDiagnosticTrace_function_0026E384.md) (function, `0x0026E384`)
- `0x00C2FFD0` → [PiPnpRtlInit](../../page/73/PiPnpRtlInit_function_007300A4.md) (function, `0x007300A4`)
- `0x00C2FFDD` → [PiCslInitialize](../C3/PiCslInitialize_function_00C362B8.md) (function, `0x00C362B8`)
- `0x00C2FFEC` → [PiDmaGuardInitialize](../../text/5A/PiDmaGuardInitialize_function_005A9F0C.md) (function, `0x005A9F0C`)
- `0x00C30005` → `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrGetFirmwareInformation` (import, 간접 대상; import `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrGetFirmwareInformation`)
- `0x00C3001C` → [PiKsrNotifyInitialize](../C3/PiKsrNotifyInitialize_function_00C36540.md) (function, `0x00C36540`)
- `0x00C30055` → [PnpRequestDeviceAction](../../text/47/PnpRequestDeviceAction_function_00477FF8.md) (function, `0x00477FF8`)
- `0x00C3009D` → [PpInitializeBootDDB](../C3/PpInitializeBootDDB_function_00C34018.md) (function, `0x00C34018`)
- `0x00C300B8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [IoInitSystemPreDrivers](IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2B495`
- [IoInitSystemPreDrivers](IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2B816`

### Static image references
- `0x00C2F2BE` → RVA `0x00E0A740` (`.data`; read)
- `0x00C2F331` → RVA `0x00E662F8` (`.data`; read)
- `0x00C2F338` → RVA `0x00F8C380` (`.data`; write)
- `0x00C2F33F` → RVA `0x00E662F8` (`.data`; write)
- `0x00C2F349` → RVA `0x00E662FC` (`.data`; write)
- `0x00C2F358` → RVA `0x00FD9DE8` (`PAGEDATA`; read)
- `0x00C2F35F` → RVA `0x00E662F0` (`.data`; write)
- `0x00C2F3C5` → RVA `0x00C79E50` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2F3EB` → RVA `0x00C79E80` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2F45C` → RVA `0x00F8C300` (`.data`; read)
- `0x00C2F463` → RVA `0x00F8C348` (`.data`; write)
- `0x00C2F46A` → RVA `0x00F8C308` (`.data`; write)
- `0x00C2F474` → RVA `0x00F8C300` (`.data`; write)
- `0x00C2F47B` → RVA `0x00F8C330` (`.data`; read)
- `0x00C2F482` → RVA `0x00F8C338` (`.data`; write)
- `0x00C2F489` → RVA `0x00F8C330` (`.data`; write)
- `0x00C2F490` → RVA `0x00F8C318` (`.data`; read)
- `0x00C2F497` → RVA `0x00F8C320` (`.data`; write)
- `0x00C2F49E` → RVA `0x00F8C318` (`.data`; write)
- `0x00C2F4A5` → RVA `0x00F8C310` (`.data`; write)
- `0x00C2F4AC` → RVA `0x00F8C328` (`.data`; write)
- `0x00C2F4B3` → RVA `0x00F8C32A` (`.data`; write)
- `0x00C2F4BA` → RVA `0x00F8C32C` (`.data`; write)
- `0x00C2F4C1` → RVA `0x00F8C340` (`.data`; write)
- `0x00C2F4F2` → RVA `0x00F8CFC8` (`.data`; read)
- `0x00C2F4F9` → RVA `0x00F8CFC0` (`.data`; write)
- `0x00C2F501` → RVA `0x00F8CFD0` (`.data`; write)
- `0x00C2F508` → RVA `0x00F8CFC8` (`.data`; write)
- `0x00C2F50F` → RVA `0x00F8CFC2` (`.data`; write)
- `0x00C2F516` → RVA `0x00F8CFC4` (`.data`; write)
- `0x00C2F52A` → RVA `0x00F8C368` (`.data`; read)
- `0x00C2F531` → RVA `0x00F8C360` (`.data`; write)
- `0x00C2F53D` → RVA `0x00F8C370` (`.data`; write)
- `0x00C2F544` → RVA `0x00F8C368` (`.data`; write)
- `0x00C2F54B` → RVA `0x00F8C280` (`.data`; read)
- `0x00C2F552` → RVA `0x00F8C160` (`.data`; read)
- `0x00C2F559` → RVA `0x00F8C362` (`.data`; write)
- `0x00C2F560` → RVA `0x00F8C364` (`.data`; write)
- `0x00C2F566` → RVA `0x00F8C378` (`.data`; write)
- `0x00C2F584` → RVA `0x00E2DC38` (`.data`; read)
- `0x00C2F58A` → RVA `0x00C342D0` (`IopReportBootResources`; read)
- `0x00C2F591` → RVA `0x00F8C138` (`.data`; write)
- `0x00C2F598` → RVA `0x010086B8` (`INITDATA`; write)
- `0x00C2F59F` → RVA `0x00E0AA14` (`.data`; write)
- `0x00C2F629` → RVA `0x00E66398` (`.data`; read)
- `0x00C2F650` → RVA `0x00C79EA0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2F694` → RVA `0x00C79EC0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2F6BA` → RVA `0x00E0A9DC` (`.data`; write)
- `0x00C2F6D3` → RVA `0x00C79F80` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2F6F9` → RVA `0x00E0A9E4` (`.data`; write)
- `0x00C2F710` → RVA `0x00C7AF30` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2F72B` → RVA `0x00F8B408` (`.data`; write)
- `0x00C2F746` → RVA `0x00C7AC70` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2F771` → RVA `0x00E0A9E8` (`.data`; write)
- `0x00C2F78B` → RVA `0x00723740` (`PipUpdateAsyncOptionsCallback`; read)
- `0x00C2F792` → RVA `0x00F8CF90` (`.data`; write)
- `0x00C2F799` → RVA `0x00F8CF98` (`.data`; write)
- `0x00C2F7A0` → RVA `0x00F8CF80` (`.data`; write)
- `0x00C2F7B1` → RVA `0x00C79FC0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2F7FB` → RVA `0x00C7A000` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2F825` → RVA `0x00E6627A` (`.data`; write)
- `0x00C2F840` → RVA `0x00C7A010` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2F86A` → RVA `0x00E66278` (`.data`; write)
- `0x00C2F878` → RVA `0x00E66245` (`.data`; read)
- `0x00C2F881` → RVA `0x00E66279` (`.data`; read)
- `0x00C2F89B` → RVA `0x00723900` (`PipUpdateSetupInProgressCallback`; read)
- `0x00C2F8A4` → RVA `0x00F8CF50` (`.data`; write)
- `0x00C2F8AB` → RVA `0x00F8CF58` (`.data`; write)
- `0x00C2F8B2` → RVA `0x00F8CF40` (`.data`; write)
- `0x00C2F97A` → RVA `0x00C79EE0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2F99C` → RVA `0x00C79F00` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2FA0D` → RVA `0x00F8C450` (`.data`; read)
- `0x00C2FA17` → RVA `0x00F8C458` (`.data`; write)
- `0x00C2FA1E` → RVA `0x00F8C560` (`.data`; read)
- `0x00C2FA25` → RVA `0x00F8C450` (`.data`; write)
- `0x00C2FA2E` → RVA `0x00F8C550` (`.data`; read)
- `0x00C2FA35` → RVA `0x00F8C558` (`.data`; write)
- `0x00C2FA3C` → RVA `0x00F8C550` (`.data`; write)
- `0x00C2FA4A` → RVA `0x00F8C460` (`.data`; read)
- `0x00C2FA58` → RVA `0x00F8C4E0` (`.data`; read)
- `0x00C2FA64` → RVA `0x00F8C400` (`.data`; read)
- `0x00C2FA6B` → RVA `0x00F8AD90` (`.data`; write)
- `0x00C2FA72` → RVA `0x00F8C408` (`.data`; write)
- `0x00C2FA79` → RVA `0x00F8CEA0` (`.data`; read)
- `0x00C2FA80` → RVA `0x00F8C400` (`.data`; write)
- `0x00C2FA89` → RVA `0x00F8C3C0` (`.data`; read)
- `0x00C2FA90` → RVA `0x00F8C3E0` (`.data`; write)
- `0x00C2FA96` → RVA `0x00F8C3C8` (`.data`; write)
- `0x00C2FA9D` → RVA `0x00F8C3C0` (`.data`; write)
- `0x00C2FAA4` → RVA `0x00F8C3E8` (`.data`; write)
- `0x00C2FAAB` → RVA `0x00F8C3F0` (`.data`; write)
- `0x00C2FAB2` → RVA `0x00F8C3F8` (`.data`; write)
- `0x00C2FAB9` → RVA `0x00F8C3FA` (`.data`; write)
- `0x00C2FAC0` → RVA `0x00F8C3FC` (`.data`; write)
- `0x00C2FAC7` → RVA `0x00F8C3A0` (`.data`; write)
- `0x00C2FACD` → RVA `0x00F8C3A8` (`.data`; write)
- `0x00C2FAD4` → RVA `0x00F8C3B0` (`.data`; write)
- `0x00C2FADB` → RVA `0x00F8C3B8` (`.data`; write)
- `0x00C2FAE2` → RVA `0x00F8C3BA` (`.data`; write)
- `0x00C2FAE9` → RVA `0x00F8C3BC` (`.data`; write)
- `0x00C2FAF8` → RVA `0x00F8CF08` (`.data`; write)
- `0x00C2FB04` → RVA `0x00F8CE80` (`.data`; read)
- `0x00C2FB0B` → RVA `0x00F8CE88` (`.data`; write)
- `0x00C2FB12` → RVA `0x00F8CE80` (`.data`; write)
- `0x00C2FB19` → RVA `0x00F8CE70` (`.data`; read)
- `0x00C2FB20` → RVA `0x00F8CE78` (`.data`; write)
- `0x00C2FB27` → RVA `0x00F8CE70` (`.data`; write)
- `0x00C2FB2E` → RVA `0x00F8CE60` (`.data`; read)
- `0x00C2FB35` → RVA `0x00F8CE68` (`.data`; write)
- `0x00C2FB3C` → RVA `0x00F8CE60` (`.data`; write)
- `0x00C2FB4B` → RVA `0x00E663B0` (`.data`; read/write)
- `0x00C2FB52` → RVA `0x00F8AD40` (`.data`; write)
- `0x00C2FB59` → RVA `0x00F8AD60` (`.data`; write)
- `0x00C2FB61` → RVA `0x00F8AD62` (`.data`; write)
- `0x00C2FB68` → RVA `0x00F8AD64` (`.data`; write)
- `0x00C2FB6E` → RVA `0x00F8AD68` (`.data`; read)
- `0x00C2FB75` → RVA `0x00F8ACA0` (`.data`; write)
- `0x00C2FB7B` → RVA `0x00F8AD70` (`.data`; write)
- `0x00C2FB82` → RVA `0x00C35530` (`PipPnPDriverEntry`; read)
- `0x00C2FB89` → RVA `0x00F8AD68` (`.data`; write)
- `0x00C2FB95` → RVA `0x00F8AD80` (`.data`; read)
- `0x00C2FB9C` → RVA `0x00F8ACA8` (`.data`; write)
- `0x00C2FBA3` → RVA `0x00F8AD88` (`.data`; write)
- `0x00C2FBAA` → RVA `0x00F8AD80` (`.data`; write)
- `0x00C2FBB1` → RVA `0x00F8ACE0` (`.data`; read)
- `0x00C2FBB8` → RVA `0x00F8ACE8` (`.data`; write)
- `0x00C2FBBF` → RVA `0x00F8ACE0` (`.data`; write)
- `0x00C2FBC6` → RVA `0x00F8ACC0` (`.data`; read)
- `0x00C2FBCD` → RVA `0x00F8ACC8` (`.data`; write)
- `0x00C2FBD4` → RVA `0x00F8ACC0` (`.data`; write)
- `0x00C2FBDB` → RVA `0x00F8AD08` (`.data`; read)
- `0x00C2FBE2` → RVA `0x00F8AD10` (`.data`; write)
- `0x00C2FBE9` → RVA `0x00F8AD08` (`.data`; write)
- `0x00C2FBF0` → RVA `0x00F8C428` (`.data`; read)
- `0x00C2FBF7` → RVA `0x00F8C430` (`.data`; write)
- `0x00C2FBFE` → RVA `0x00F8C428` (`.data`; write)
- `0x00C2FC05` → RVA `0x00C79F50` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2FC11` → RVA `0x00F8ACB0` (`.data`; write)
- `0x00C2FC18` → RVA `0x00F8ACB8` (`.data`; write)
- `0x00C2FC1F` → RVA `0x00F8ACBA` (`.data`; write)
- `0x00C2FC26` → RVA `0x00F8ACBC` (`.data`; write)
- `0x00C2FC2D` → RVA `0x00F8ACD8` (`.data`; write)
- `0x00C2FC34` → RVA `0x00F8AD00` (`.data`; write)
- `0x00C2FC3B` → RVA `0x00F8AD02` (`.data`; write)
- `0x00C2FC42` → RVA `0x00F8AD04` (`.data`; write)
- `0x00C2FC48` → RVA `0x00F8AD18` (`.data`; write)
- `0x00C2FC4E` → RVA `0x00F8C418` (`.data`; write)
- `0x00C2FC55` → RVA `0x00F8C420` (`.data`; write)
- `0x00C2FC5C` → RVA `0x00F8C422` (`.data`; write)
- `0x00C2FC63` → RVA `0x00F8C424` (`.data`; write)
- `0x00C2FC80` → RVA `0x00F8C440` (`.data`; read)
- `0x00C2FCB7` → RVA `0x00F8C438` (`.data`; read)
- `0x00C2FE11` → RVA `0x00F8AC28` (`.data`; read)
- `0x00C2FE18` → RVA `0x00F8AC20` (`.data`; write)
- `0x00C2FE1F` → RVA `0x00F8AC30` (`.data`; write)
- `0x00C2FE26` → RVA `0x00F8AC28` (`.data`; write)
- `0x00C2FE2D` → RVA `0x00F8AC22` (`.data`; write)
- `0x00C2FE34` → RVA `0x00F8AC24` (`.data`; write)
- `0x00C2FE5A` → RVA `0x00C7B030` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2FE69` → RVA `0x00C357E0` (`PiDaDriverEntry`; read)
- `0x00C2FEE6` → RVA `0x00E06DA0` (`.data`; read)
- `0x00C2FEF0` → RVA `0x00026E10` (`.rdata`; read)
- `0x00C2FF03` → RVA `0x00E662D0` (`.data`; read)
- `0x00C2FF0C` → RVA `0x00E662D8` (`.data`; write)
- `0x00C2FF16` → RVA `0x00A516A0` (`PnpDiagRundownRegisterCallback`; read)
- `0x00C2FF20` → RVA `0x00026D30` (`.rdata`; read)
- `0x00C2FF41` → RVA `0x00E06F90` (`.data`; read)
- `0x00C2FF4D` → RVA `0x00E06F58` (`.data`; read)
- `0x00C2FF5C` → RVA `0x00E06FC8` (`.data`; read)
- `0x00C2FFBB` → RVA `0x00027570` (`.rdata`; read)
- `0x00C30005` → RVA `0x00151318` (`ext-ms-win-ntos-ksr-l1-1-5.dll!KsrGetFirmwareInformation (IAT)`; read)
- `0x00C30015` → RVA `0x00F8A988` (`.data`; write)
- `0x00C3005A` → RVA `0x00F8C5E8` (`.data`; read)
- `0x00C30061` → RVA `0x00F8C5E0` (`.data`; write)
- `0x00C30069` → RVA `0x00F8C5F0` (`.data`; write)
- `0x00C30070` → RVA `0x00F8C5E8` (`.data`; write)
- `0x00C30077` → RVA `0x00F8C5E2` (`.data`; write)
- `0x00C3007E` → RVA `0x00F8C5E4` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **73**
  - `0x00C2F353` → [CmRegisterSystemHiveLimitCallback](../../page/7E/CmRegisterSystemHiveLimitCallback_function_007E213C.md) (`INIT` → `PAGE`)
  - `0x00C2F3AC` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`INIT` → `.text`)
  - `0x00C2F3CC` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (`INIT` → `PAGE`)
  - `0x00C2F3F2` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (`INIT` → `PAGE`)
  - `0x00C2F40F` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C2F41E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C2F439` → [PnpLogEvent](../../page/72/PnpLogEvent_function_0072C8FC.md) (`INIT` → `PAGE`)
  - `0x00C2F443` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C2F44D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C2F457` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`INIT` → `.text`)
  - `0x00C2F5AA` → [ArbLibraryInitialize](../../page/70/ArbLibraryInitialize_function_0070F180.md) (`INIT` → `PAGE`)
  - `0x00C2F5B9` → [IopPortInitialize](../../page/72/IopPortInitialize_function_0072F500.md) (`INIT` → `PAGE`)
  - `0x00C2F5C8` → [IopMemInitialize](../../page/72/IopMemInitialize_function_0072F078.md) (`INIT` → `PAGE`)
  - `0x00C2F5D7` → [IopDmaInitialize](../../page/72/IopDmaInitialize_function_0072F634.md) (`INIT` → `PAGE`)
  - `0x00C2F5E6` → [IopIrqInitialize](../../page/72/IopIrqInitialize_function_0072F758.md) (`INIT` → `PAGE`)
  - `0x00C2F5F5` → [IopBusNumberInitialize](../../page/72/IopBusNumberInitialize_function_0072F828.md) (`INIT` → `PAGE`)
  - `0x00C2F606` → [PiPnpRtlInit](../../page/73/PiPnpRtlInit_function_007300A4.md) (`INIT` → `PAGE`)
  - `0x00C2F63D` → [_PnpCtxGetCachedContextBaseKey](../../page/8E/_PnpCtxGetCachedContextBaseKey_function_008EFB2C.md) (`INIT` → `PAGE`)
  - `0x00C2F67B` → [IopCreateRegistryKeyEx](../../page/A8/IopCreateRegistryKeyEx_function_00A89038.md) (`INIT` → `PAGE`)
  - `0x00C2F69B` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (`INIT` → `PAGE`)
  - `0x00C2F6C2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C2F6DA` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (`INIT` → `PAGE`)
  - `0x00C2F701` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C2F71C` → [PnpGetRegistryDword](../../text/4B/PnpGetRegistryDword_function_004BFDE8.md) (`INIT` → `.text`)
  - `0x00C2F752` → [PnpGetRegistryDword](../../text/4B/PnpGetRegistryDword_function_004BFDE8.md) (`INIT` → `.text`)
  - `0x00C2F7A7` → [PipUpdateAsyncOptionsCallback](../../page/72/PipUpdateAsyncOptionsCallback_function_00723740.md) (`INIT` → `PAGE`)
  - `0x00C2F7D7` → [IopOpenRegistryKeyEx](../../page/A5/IopOpenRegistryKeyEx_function_00A51B44.md) (`INIT` → `PAGE`)
  - `0x00C2F7E9` → [PipUpdateSetupInProgress](../../page/72/PipUpdateSetupInProgress_function_007237F8.md) (`INIT` → `PAGE`)
  - `0x00C2F802` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (`INIT` → `PAGE`)
  - `0x00C2F82E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C2F847` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (`INIT` → `PAGE`)
  - `0x00C2F873` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C2F88F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`INIT` → `.text`)
  - `0x00C2F8B9` → [PipUpdateSetupInProgressNotify](../../page/72/PipUpdateSetupInProgressNotify_function_00723918.md) (`INIT` → `PAGE`)
  - `0x00C2F905` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C2F989` → [CmCreateDevice](../../page/8F/CmCreateDevice_function_008FFABC.md) (`INIT` → `PAGE`)
  - `0x00C2F9CC` → [CmSetDeviceRegProp](../../page/8F/CmSetDeviceRegProp_function_008FD68C.md) (`INIT` → `PAGE`)
  - `0x00C2FA00` → [CmSetDeviceRegProp](../../page/8F/CmSetDeviceRegProp_function_008FD68C.md) (`INIT` → `PAGE`)
  - `0x00C2FA08` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`INIT` → `.text`)
  - `0x00C2FA43` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (`INIT` → `.text`)
  - `0x00C2FA51` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (`INIT` → `.text`)
  - `0x00C2FA5F` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (`INIT` → `.text`)
  - `0x00C2FAF0` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (`INIT` → `.text`)
  - `0x00C2FAFF` → [PnpAcquireDependencyRelationsLock](../../page/A0/PnpAcquireDependencyRelationsLock_function_00A06788.md) (`INIT` → `PAGE`)
  - `0x00C2FB43` → [PnpReleaseDependencyRelationsLock](../../page/A0/PnpReleaseDependencyRelationsLock_function_00A06E14.md) (`INIT` → `PAGE`)
  - `0x00C2FC71` → [IoCreateDriver](../../page/AC/IoCreateDriver_function_00AC9D70.md) (`INIT` → `PAGE`)
  - `0x00C2FCA3` → [IoCreateDevice](../../page/9A/IoCreateDevice_function_009A4B00.md) (`INIT` → `PAGE`)
  - `0x00C2FCC6` → [PipAllocateDeviceNode](../../page/A9/PipAllocateDeviceNode_function_00A9C8F8.md) (`INIT` → `PAGE`)
  - `0x00C2FCDC` → [IoDeleteDevice](../../text/26/IoDeleteDevice_function_0026FE90.md) (`INIT` → `.text`)
  - `0x00C2FCE8` → [IoDeleteDriver](../../page/71/IoDeleteDriver_function_0071D400.md) (`INIT` → `PAGE`)
  - `0x00C2FCFF` → [PipSetDevNodeFlags](../../page/8F/PipSetDevNodeFlags_function_008FC048.md) (`INIT` → `PAGE`)
  - `0x00C2FD10` → [PipSetDevNodeUserFlags](../../page/8F/PipSetDevNodeUserFlags_function_008FB8FC.md) (`INIT` → `PAGE`)
  - `0x00C2FD32` → [PnpAllocateDeviceInstancePath](../../page/72/PnpAllocateDeviceInstancePath_function_0072DC30.md) (`INIT` → `PAGE`)
  - `0x00C2FD57` → [PnpCopyDeviceInstancePath](../../page/72/PnpCopyDeviceInstancePath_function_0072DC70.md) (`INIT` → `PAGE`)
  - `0x00C2FD6B` → [PnpMapDeviceObjectToDeviceInstance](../../page/A9/PnpMapDeviceObjectToDeviceInstance_function_00A9D884.md) (`INIT` → `PAGE`)
  - `0x00C2FD97` → [RtlGUIDFromString](../../page/8F/RtlGUIDFromString_function_008F1EF0.md) (`INIT` → `PAGE`)
  - `0x00C2FDA3` → [PnpQueryAndSaveDeviceNodeCapabilities](../../page/8F/PnpQueryAndSaveDeviceNodeCapabilities_function_008FBCE8.md) (`INIT` → `PAGE`)
  - `0x00C2FDB4` → [PipSetDevNodeState](../../text/47/PipSetDevNodeState_function_00470708.md) (`INIT` → `.text`)
  - `0x00C2FDCE` → [CmAddDeviceToContainer](../../page/8F/CmAddDeviceToContainer_function_008FF190.md) (`INIT` → `PAGE`)
  - `0x00C2FDE4` → [PiDcHandleSystemFirmwareUpdate](../../page/73/PiDcHandleSystemFirmwareUpdate_function_00730B20.md) (`INIT` → `PAGE`)
  - `0x00C2FE78` → [IoCreateDriver](../../page/AC/IoCreateDriver_function_00AC9D70.md) (`INIT` → `PAGE`)
  - `0x00C2FE89` → [PiDmaGuardInitialize](../../text/5A/PiDmaGuardInitialize_function_005A9F0C.md) (`INIT` → `.text`)
  - `0x00C2FECF` → [PnpRequestDeviceAction](../../text/47/PnpRequestDeviceAction_function_00477FF8.md) (`INIT` → `.text`)
  - `0x00C2FEF7` → [McGenEventRegister_EtwRegister](../../text/57/McGenEventRegister_EtwRegister_function_0057EF04.md) (`INIT` → `.text`)
  - `0x00C2FF2A` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (`INIT` → `PAGE`)
  - `0x00C2FF48` → [TlgRegisterAggregateProvider](../../page/70/TlgRegisterAggregateProvider_function_0070526C.md) (`INIT` → `PAGE`)
  - `0x00C2FF54` → [TlgRegisterAggregateProvider](../../page/70/TlgRegisterAggregateProvider_function_0070526C.md) (`INIT` → `PAGE`)
  - `0x00C2FF65` → [TraceLoggingRegisterEx_EtwRegister_EtwSetInformation](../../page/92/TraceLoggingRegisterEx_EtwRegister_EtwSetInformation_function_009208A0.md) (`INIT` → `PAGE`)
  - `0x00C2FFC9` → [PnpDiagnosticTrace](../../text/26/PnpDiagnosticTrace_function_0026E384.md) (`INIT` → `.text`)
  - `0x00C2FFD0` → [PiPnpRtlInit](../../page/73/PiPnpRtlInit_function_007300A4.md) (`INIT` → `PAGE`)
  - `0x00C2FFEC` → [PiDmaGuardInitialize](../../text/5A/PiDmaGuardInitialize_function_005A9F0C.md) (`INIT` → `.text`)
  - `0x00C30055` → [PnpRequestDeviceAction](../../text/47/PnpRequestDeviceAction_function_00477FF8.md) (`INIT` → `.text`)
  - `0x00C300B8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C2F298  48 8B C4                        mov rax, rsp
00C2F29B  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00C2F29F  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00C2F2A3  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00C2F2A7  55                              push rbp
00C2F2A8  41 54                           push r12
00C2F2AA  41 55                           push r13
00C2F2AC  41 56                           push r14
00C2F2AE  41 57                           push r15
00C2F2B0  48 8D A8 38 FF FF FF            lea rbp, [rax - 0xc8]
00C2F2B7  48 81 EC A0 01 00 00            sub rsp, 0x1a0
00C2F2BE  48 8B 05 7B B4 1D 00            mov rax, qword ptr [rip + 0x1db47b]
00C2F2C5  48 33 C4                        xor rax, rsp
00C2F2C8  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
00C2F2CF  45 33 F6                        xor r14d, r14d
00C2F2D2  0F 57 C0                        xorps xmm0, xmm0
00C2F2D5  4C 89 75 88                     mov qword ptr [rbp - 0x78], r14
00C2F2D9  0F 57 C9                        xorps xmm1, xmm1
00C2F2DC  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
00C2F2E1  48 8B F1                        mov rsi, rcx
00C2F2E4  4C 89 75 A0                     mov qword ptr [rbp - 0x60], r14
00C2F2E8  44 89 74 24 5C                  mov dword ptr [rsp + 0x5c], r14d
00C2F2ED  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
00C2F2F2  44 89 75 80                     mov dword ptr [rbp - 0x80], r14d
00C2F2F6  44 89 75 FC                     mov dword ptr [rbp - 4], r14d
00C2F2FA  44 89 75 14                     mov dword ptr [rbp + 0x14], r14d
00C2F2FE  4C 89 75 98                     mov qword ptr [rbp - 0x68], r14
00C2F302  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
00C2F307  4C 89 75 A8                     mov qword ptr [rbp - 0x58], r14
00C2F30B  4C 89 75 B0                     mov qword ptr [rbp - 0x50], r14
00C2F30F  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
00C2F314  44 89 75 BC                     mov dword ptr [rbp - 0x44], r14d
00C2F318  44 89 75 CC                     mov dword ptr [rbp - 0x34], r14d
00C2F31C  44 88 74 24 40                  mov byte ptr [rsp + 0x40], r14b
00C2F321  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00C2F325  0F 11 4D D8                     movups xmmword ptr [rbp - 0x28], xmm1
00C2F329  85 D2                           test edx, edx
00C2F32B  0F 85 A8 0B 00 00               jne 0x140c2fed9
00C2F331  4C 8D 05 C0 6F 23 00            lea r8, [rip + 0x236fc0]
00C2F338  44 88 35 41 D0 35 00            mov byte ptr [rip + 0x35d041], r14b
00C2F33F  C7 05 AF 6F 23 00 50 00 00 00   mov dword ptr [rip + 0x236faf], 0x50
00C2F349  C7 05 A9 6F 23 00 5A 00 00 00   mov dword ptr [rip + 0x236fa9], 0x5a
00C2F353  E8 E4 2D BB FF                  call 0x1407e213c
00C2F358  48 8D 05 89 AA 3A 00            lea rax, [rip + 0x3aaa89]
00C2F35F  44 88 35 8A 6F 23 00            mov byte ptr [rip + 0x236f8a], r14b
00C2F366  48 89 45 08                     mov qword ptr [rbp + 8], rax
00C2F36A  4C 8D 45 F8                     lea r8, [rbp - 8]
00C2F36E  48 8D 45 80                     lea rax, [rbp - 0x80]
00C2F372  C7 45 F8 30 00 00 00            mov dword ptr [rbp - 8], 0x30
00C2F379  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C2F37E  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00C2F383  0F 57 C0                        xorps xmm0, xmm0
00C2F386  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00C2F38B  41 BC 3F 00 0F 00               mov r12d, 0xf003f
00C2F391  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00C2F396  45 33 C9                        xor r9d, r9d
00C2F399  4C 89 75 00                     mov qword ptr [rbp], r14
00C2F39D  41 8B D4                        mov edx, r12d
00C2F3A0  C7 45 10 40 02 00 00            mov dword ptr [rbp + 0x10], 0x240
00C2F3A7  F3 0F 7F 45 18                  movdqu xmmword ptr [rbp + 0x18], xmm0
00C2F3AC  E8 BF E0 A7 FF                  call 0x1406ad470
00C2F3B1  85 C0                           test eax, eax
00C2F3B3  0F 88 A3 00 00 00               js 0x140c2f45c
00C2F3B9  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00C2F3BE  4C 8D 4D 98                     lea r9, [rbp - 0x68]
00C2F3C2  45 33 C0                        xor r8d, r8d
00C2F3C5  48 8D 15 84 AA 04 00            lea rdx, [rip + 0x4aa84]
00C2F3CC  E8 1B 9D D6 FF                  call 0x1409990ec
00C2F3D1  85 C0                           test eax, eax
00C2F3D3  78 7D                           js 0x140c2f452
00C2F3D5  48 8B 5D 98                     mov rbx, qword ptr [rbp - 0x68]
00C2F3D9  48 85 DB                        test rbx, rbx
00C2F3DC  74 74                           je 0x140c2f452
00C2F3DE  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00C2F3E3  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
00C2F3E8  45 33 C0                        xor r8d, r8d
00C2F3EB  48 8D 15 8E AA 04 00            lea rdx, [rip + 0x4aa8e]
00C2F3F2  E8 F5 9C D6 FF                  call 0x1409990ec
00C2F3F7  85 C0                           test eax, eax
00C2F3F9  78 4D                           js 0x140c2f448
00C2F3FB  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
00C2F400  48 85 FF                        test rdi, rdi
00C2F403  74 43                           je 0x140c2f448
00C2F405  8B 53 08                        mov edx, dword ptr [rbx + 8]
00C2F408  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00C2F40C  48 03 D3                        add rdx, rbx
00C2F40F  E8 6C B3 7F FF                  call 0x14042a780
00C2F414  8B 57 08                        mov edx, dword ptr [rdi + 8]
00C2F417  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00C2F41B  48 03 D7                        add rdx, rdi
00C2F41E  E8 5D B3 7F FF                  call 0x14042a780
00C2F423  45 33 C9                        xor r9d, r9d
00C2F426  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00C2F42B  41 B8 2C 00 00 40               mov r8d, 0x4000002c
00C2F431  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00C2F435  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00C2F439  E8 BE D4 AF FF                  call 0x14072c8fc
00C2F43E  33 D2                           xor edx, edx
00C2F440  48 8B CF                        mov rcx, rdi
00C2F443  E8 28 34 F5 FF                  call 0x140b82870
00C2F448  33 D2                           xor edx, edx
00C2F44A  48 8B CB                        mov rcx, rbx
00C2F44D  E8 1E 34 F5 FF                  call 0x140b82870
00C2F452  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00C2F457  E8 54 DE A7 FF                  call 0x1406ad2b0
00C2F45C  48 8D 05 9D CE 35 00            lea rax, [rip + 0x35ce9d]
00C2F463  4C 89 35 DE CE 35 00            mov qword ptr [rip + 0x35cede], r14
00C2F46A  48 89 05 97 CE 35 00            mov qword ptr [rip + 0x35ce97], rax
00C2F471  48 8B CE                        mov rcx, rsi
00C2F474  48 89 05 85 CE 35 00            mov qword ptr [rip + 0x35ce85], rax
00C2F47B  48 8D 05 AE CE 35 00            lea rax, [rip + 0x35ceae]
00C2F482  48 89 05 AF CE 35 00            mov qword ptr [rip + 0x35ceaf], rax
00C2F489  48 89 05 A0 CE 35 00            mov qword ptr [rip + 0x35cea0], rax
00C2F490  48 8D 05 81 CE 35 00            lea rax, [rip + 0x35ce81]
00C2F497  48 89 05 82 CE 35 00            mov qword ptr [rip + 0x35ce82], rax
00C2F49E  48 89 05 73 CE 35 00            mov qword ptr [rip + 0x35ce73], rax
00C2F4A5  44 89 35 64 CE 35 00            mov dword ptr [rip + 0x35ce64], r14d
00C2F4AC  C6 05 75 CE 35 00 05            mov byte ptr [rip + 0x35ce75], 5
00C2F4B3  C6 05 70 CE 35 00 08            mov byte ptr [rip + 0x35ce70], 8
00C2F4BA  44 89 35 6B CE 35 00            mov dword ptr [rip + 0x35ce6b], r14d
00C2F4C1  C7 05 75 CE 35 00 FF FF FF 7F   mov dword ptr [rip + 0x35ce75], 0x7fffffff
00C2F4CB  E8 F8 0C 00 00                  call 0x140c301c8
00C2F4D0  48 8B 86 F0 00 00 00            mov rax, qword ptr [rsi + 0xf0]
00C2F4D7  F7 80 84 00 00 00 00 04 00 00   test dword ptr [rax + 0x84], 0x400
00C2F4E1  75 0A                           jne 0x140c2f4ed
00C2F4E3  33 D2                           xor edx, edx
00C2F4E5  48 8B CE                        mov rcx, rsi
00C2F4E8  E8 2B 4B 00 00                  call 0x140c34018
00C2F4ED  E8 D6 1D 00 00                  call 0x140c312c8
00C2F4F2  48 8D 05 CF DA 35 00            lea rax, [rip + 0x35dacf]
00C2F4F9  66 44 89 35 BF DA 35 00         mov word ptr [rip + 0x35dabf], r14w
00C2F501  48 89 05 C8 DA 35 00            mov qword ptr [rip + 0x35dac8], rax
00C2F508  48 89 05 B9 DA 35 00            mov qword ptr [rip + 0x35dab9], rax
00C2F50F  C6 05 AC DA 35 00 06            mov byte ptr [rip + 0x35daac], 6
00C2F516  44 89 35 A7 DA 35 00            mov dword ptr [rip + 0x35daa7], r14d
00C2F51D  E8 C6 0B 00 00                  call 0x140c300e8
00C2F522  85 C0                           test eax, eax
00C2F524  0F 88 84 0B 00 00               js 0x140c300ae
00C2F52A  48 8D 05 37 CE 35 00            lea rax, [rip + 0x35ce37]
00C2F531  C6 05 28 CE 35 00 05            mov byte ptr [rip + 0x35ce28], 5
00C2F538  BF 01 00 00 00                  mov edi, 1
00C2F53D  48 89 05 2C CE 35 00            mov qword ptr [rip + 0x35ce2c], rax
00C2F544  48 89 05 1D CE 35 00            mov qword ptr [rip + 0x35ce1d], rax
00C2F54B  48 8D 0D 2E CD 35 00            lea rcx, [rip + 0x35cd2e]
00C2F552  48 8D 05 07 CC 35 00            lea rax, [rip + 0x35cc07]
00C2F559  C6 05 02 CE 35 00 08            mov byte ptr [rip + 0x35ce02], 8
00C2F560  89 3D FE CD 35 00               mov dword ptr [rip + 0x35cdfe], edi
00C2F566  89 3D 0C CE 35 00               mov dword ptr [rip + 0x35ce0c], edi
00C2F56C  48 89 40 08                     mov qword ptr [rax + 8], rax
00C2F570  48 89 00                        mov qword ptr [rax], rax
00C2F573  48 83 C0 10                     add rax, 0x10
00C2F577  48 3B C1                        cmp rax, rcx
00C2F57A  7C F0                           jl 0x140c2f56c
00C2F57C  48 8B CE                        mov rcx, rsi
00C2F57F  E8 14 3C 00 00                  call 0x140c33198
00C2F584  8B 0D AE E6 1F 00               mov ecx, dword ptr [rip + 0x1fe6ae]
00C2F58A  48 8D 05 3F 4D 00 00            lea rax, [rip + 0x4d3f]
00C2F591  48 89 05 A0 CB 35 00            mov qword ptr [rip + 0x35cba0], rax
00C2F598  4C 89 35 19 91 3D 00            mov qword ptr [rip + 0x3d9119], r14
00C2F59F  89 3D 6F B4 1D 00               mov dword ptr [rip + 0x1db46f], edi
00C2F5A5  E8 F2 69 FF FF                  call 0x140c25f9c
00C2F5AA  E8 D1 FB AD FF                  call 0x14070f180
00C2F5AF  8B D8                           mov ebx, eax
00C2F5B1  85 C0                           test eax, eax
00C2F5B3  0F 88 F3 0A 00 00               js 0x140c300ac
00C2F5B9  E8 42 FF AF FF                  call 0x14072f500
00C2F5BE  8B D8                           mov ebx, eax
00C2F5C0  85 C0                           test eax, eax
00C2F5C2  0F 88 E4 0A 00 00               js 0x140c300ac
00C2F5C8  E8 AB FA AF FF                  call 0x14072f078
00C2F5CD  8B D8                           mov ebx, eax
00C2F5CF  85 C0                           test eax, eax
00C2F5D1  0F 88 D5 0A 00 00               js 0x140c300ac
00C2F5D7  E8 58 00 B0 FF                  call 0x14072f634
00C2F5DC  8B D8                           mov ebx, eax
00C2F5DE  85 C0                           test eax, eax
00C2F5E0  0F 88 C6 0A 00 00               js 0x140c300ac
00C2F5E6  E8 6D 01 B0 FF                  call 0x14072f758
00C2F5EB  8B D8                           mov ebx, eax
00C2F5ED  85 C0                           test eax, eax
00C2F5EF  0F 88 B7 0A 00 00               js 0x140c300ac
00C2F5F5  E8 2E 02 B0 FF                  call 0x14072f828
00C2F5FA  8B D8                           mov ebx, eax
00C2F5FC  85 C0                           test eax, eax
00C2F5FE  0F 88 A8 0A 00 00               js 0x140c300ac
00C2F604  33 C9                           xor ecx, ecx
00C2F606  E8 99 0A B0 FF                  call 0x1407300a4
00C2F60B  8B D8                           mov ebx, eax
00C2F60D  85 C0                           test eax, eax
00C2F60F  0F 88 97 0A 00 00               js 0x140c300ac
00C2F615  E8 BA 21 00 00                  call 0x140c317d4
00C2F61A  E8 CD 4D 00 00                  call 0x140c343ec
00C2F61F  8B D8                           mov ebx, eax
00C2F621  85 C0                           test eax, eax
00C2F623  0F 88 83 0A 00 00               js 0x140c300ac
00C2F629  48 8B 0D 68 6D 23 00            mov rcx, qword ptr [rip + 0x236d68]
00C2F630  4C 8D 45 A0                     lea r8, [rbp - 0x60]
00C2F634  41 BF 04 00 00 00               mov r15d, 4
00C2F63A  41 8B D7                        mov edx, r15d
00C2F63D  E8 EA 04 CC FF                  call 0x1408efb2c
00C2F642  8B D8                           mov ebx, eax
00C2F644  85 C0                           test eax, eax
00C2F646  0F 88 60 0A 00 00               js 0x140c300ac
00C2F64C  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
00C2F650  48 8D 05 49 A8 04 00            lea rax, [rip + 0x4a849]
00C2F657  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00C2F65C  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00C2F661  45 8B CC                        mov r9d, r12d
00C2F664  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00C2F669  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C2F66E  C7 44 24 58 16 00 18 00         mov dword ptr [rsp + 0x58], 0x180016
00C2F676  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00C2F67B  E8 B8 99 E5 FF                  call 0x140a89038
00C2F680  85 C0                           test eax, eax
00C2F682  0F 88 29 01 00 00               js 0x140c2f7b1
00C2F688  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2F68D  4C 8D 4D A8                     lea r9, [rbp - 0x58]
00C2F691  45 33 C0                        xor r8d, r8d
00C2F694  48 8D 15 25 A8 04 00            lea rdx, [rip + 0x4a825]
00C2F69B  E8 4C 9A D6 FF                  call 0x1409990ec
00C2F6A0  85 C0                           test eax, eax
00C2F6A2  78 23                           js 0x140c2f6c7
00C2F6A4  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00C2F6A8  44 39 79 04                     cmp dword ptr [rcx + 4], r15d
00C2F6AC  75 12                           jne 0x140c2f6c0
00C2F6AE  44 39 79 0C                     cmp dword ptr [rcx + 0xc], r15d
00C2F6B2  75 0C                           jne 0x140c2f6c0
00C2F6B4  8B 41 08                        mov eax, dword ptr [rcx + 8]
00C2F6B7  8B 14 08                        mov edx, dword ptr [rax + rcx]
00C2F6BA  89 15 1C B3 1D 00               mov dword ptr [rip + 0x1db31c], edx
00C2F6C0  33 D2                           xor edx, edx
00C2F6C2  E8 A9 31 F5 FF                  call 0x140b82870
00C2F6C7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2F6CC  4C 8D 4D B0                     lea r9, [rbp - 0x50]
00C2F6D0  45 33 C0                        xor r8d, r8d
00C2F6D3  48 8D 15 A6 A8 04 00            lea rdx, [rip + 0x4a8a6]
00C2F6DA  E8 0D 9A D6 FF                  call 0x1409990ec
00C2F6DF  85 C0                           test eax, eax
00C2F6E1  78 23                           js 0x140c2f706
00C2F6E3  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
00C2F6E7  44 39 79 04                     cmp dword ptr [rcx + 4], r15d
00C2F6EB  75 12                           jne 0x140c2f6ff
00C2F6ED  44 39 79 0C                     cmp dword ptr [rcx + 0xc], r15d
00C2F6F1  75 0C                           jne 0x140c2f6ff
00C2F6F3  8B 41 08                        mov eax, dword ptr [rcx + 8]
00C2F6F6  8B 14 08                        mov edx, dword ptr [rax + rcx]
00C2F6F9  89 15 E5 B2 1D 00               mov dword ptr [rip + 0x1db2e5], edx
00C2F6FF  33 D2                           xor edx, edx
00C2F701  E8 6A 31 F5 FF                  call 0x140b82870
00C2F706  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2F70B  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00C2F710  48 8D 15 19 B8 04 00            lea rdx, [rip + 0x4b819]
00C2F717  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
00C2F71C  E8 C7 06 89 FF                  call 0x1404bfde8
00C2F721  85 C0                           test eax, eax
00C2F723  78 0D                           js 0x140c2f732
00C2F725  39 7C 24 68                     cmp dword ptr [rsp + 0x68], edi
00C2F729  75 07                           jne 0x140c2f732
00C2F72B  40 88 3D D6 BC 35 00            mov byte ptr [rip + 0x35bcd6], dil
00C2F732  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2F737  E8 84 47 00 00                  call 0x140c33ec0
00C2F73C  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2F741  4C 8D 44 24 6C                  lea r8, [rsp + 0x6c]
00C2F746  48 8D 15 23 B5 04 00            lea rdx, [rip + 0x4b523]
00C2F74D  44 89 74 24 6C                  mov dword ptr [rsp + 0x6c], r14d
00C2F752  E8 91 06 89 FF                  call 0x1404bfde8
00C2F757  85 C0                           test eax, eax
00C2F759  78 1F                           js 0x140c2f77a
00C2F75B  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
00C2F75F  B9 64 00 00 00                  mov ecx, 0x64
00C2F764  3B C1                           cmp eax, ecx
00C2F766  72 09                           jb 0x140c2f771
00C2F768  B9 60 EA 00 00                  mov ecx, 0xea60
00C2F76D  3B C1                           cmp eax, ecx
00C2F76F  76 0E                           jbe 0x140c2f77f
00C2F771  66 89 0D 70 B2 1D 00            mov word ptr [rip + 0x1db270], cx
00C2F778  EB 0C                           jmp 0x140c2f786
00C2F77A  B8 88 13 00 00                  mov eax, 0x1388
00C2F77F  66 89 05 62 B2 1D 00            mov word ptr [rip + 0x1db262], ax
00C2F786  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2F78B  48 8D 05 AE 3F AF FF            lea rax, [rip - 0x50c052]
00C2F792  48 89 05 F7 D7 35 00            mov qword ptr [rip + 0x35d7f7], rax
00C2F799  48 89 0D F8 D7 35 00            mov qword ptr [rip + 0x35d7f8], rcx
00C2F7A0  4C 89 35 D9 D7 35 00            mov qword ptr [rip + 0x35d7d9], r14
00C2F7A7  E8 94 3F AF FF                  call 0x140723740
00C2F7AC  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
00C2F7B1  48 8D 05 08 A8 04 00            lea rax, [rip + 0x4a808]
00C2F7B8  C7 44 24 58 3C 00 3E 00         mov dword ptr [rsp + 0x58], 0x3e003c
00C2F7C0  41 B9 19 00 02 00               mov r9d, 0x20019
00C2F7C6  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00C2F7CB  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00C2F7D0  33 D2                           xor edx, edx
00C2F7D2  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C2F7D7  E8 68 23 E2 FF                  call 0x140a51b44
00C2F7DC  85 C0                           test eax, eax
00C2F7DE  0F 88 DF 00 00 00               js 0x140c2f8c3
00C2F7E4  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2F7E9  E8 0A 40 AF FF                  call 0x1407237f8
00C2F7EE  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2F7F3  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
00C2F7F8  45 33 C0                        xor r8d, r8d
00C2F7FB  48 8D 15 FE A7 04 00            lea rdx, [rip + 0x4a7fe]
00C2F802  E8 E5 98 D6 FF                  call 0x1409990ec
00C2F807  85 C0                           test eax, eax
00C2F809  78 28                           js 0x140c2f833
00C2F80B  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00C2F810  44 39 79 04                     cmp dword ptr [rcx + 4], r15d
00C2F814  75 16                           jne 0x140c2f82c
00C2F816  44 39 79 0C                     cmp dword ptr [rcx + 0xc], r15d
00C2F81A  75 10                           jne 0x140c2f82c
00C2F81C  8B 41 08                        mov eax, dword ptr [rcx + 8]
00C2F81F  44 39 34 08                     cmp dword ptr [rax + rcx], r14d
00C2F823  74 07                           je 0x140c2f82c
00C2F825  40 88 3D 4E 6A 23 00            mov byte ptr [rip + 0x236a4e], dil
00C2F82C  33 D2                           xor edx, edx
00C2F82E  E8 3D 30 F5 FF                  call 0x140b82870
00C2F833  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2F838  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
00C2F83D  45 33 C0                        xor r8d, r8d
00C2F840  48 8D 15 C9 A7 04 00            lea rdx, [rip + 0x4a7c9]
00C2F847  E8 A0 98 D6 FF                  call 0x1409990ec
00C2F84C  85 C0                           test eax, eax
00C2F84E  78 28                           js 0x140c2f878
00C2F850  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00C2F855  44 39 79 04                     cmp dword ptr [rcx + 4], r15d
00C2F859  75 16                           jne 0x140c2f871
00C2F85B  44 39 79 0C                     cmp dword ptr [rcx + 0xc], r15d
00C2F85F  75 10                           jne 0x140c2f871
00C2F861  8B 41 08                        mov eax, dword ptr [rcx + 8]
00C2F864  44 39 34 08                     cmp dword ptr [rax + rcx], r14d
00C2F868  74 07                           je 0x140c2f871
00C2F86A  40 88 3D 07 6A 23 00            mov byte ptr [rip + 0x236a07], dil
00C2F871  33 D2                           xor edx, edx
00C2F873  E8 F8 2F F5 FF                  call 0x140b82870
00C2F878  44 38 35 C6 69 23 00            cmp byte ptr [rip + 0x2369c6], r14b
00C2F87F  75 15                           jne 0x140c2f896
00C2F881  44 38 35 F1 69 23 00            cmp byte ptr [rip + 0x2369f1], r14b
00C2F888  75 0C                           jne 0x140c2f896
00C2F88A  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2F88F  E8 1C DA A7 FF                  call 0x1406ad2b0
00C2F894  EB 28                           jmp 0x140c2f8be
00C2F896  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2F89B  48 8D 05 5E 40 AF FF            lea rax, [rip - 0x50bfa2]
00C2F8A2  33 D2                           xor edx, edx
00C2F8A4  48 89 05 A5 D6 35 00            mov qword ptr [rip + 0x35d6a5], rax
00C2F8AB  48 89 0D A6 D6 35 00            mov qword ptr [rip + 0x35d6a6], rcx
00C2F8B2  4C 89 35 87 D6 35 00            mov qword ptr [rip + 0x35d687], r14
00C2F8B9  E8 5A 40 AF FF                  call 0x140723918
00C2F8BE  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
00C2F8C3  48 8B 8E F0 00 00 00            mov rcx, qword ptr [rsi + 0xf0]
00C2F8CA  48 81 C1 08 0A 00 00            add rcx, 0xa08
00C2F8D1  E8 4E 14 00 00                  call 0x140c30d24
00C2F8D6  8B D8                           mov ebx, eax
00C2F8D8  85 C0                           test eax, eax
00C2F8DA  0F 88 CC 07 00 00               js 0x140c300ac
00C2F8E0  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00C2F8E5  E8 A2 0B 00 00                  call 0x140c3048c
00C2F8EA  33 C9                           xor ecx, ecx
00C2F8EC  E8 EB 4B 00 00                  call 0x140c344dc
00C2F8F1  8B D8                           mov ebx, eax
00C2F8F3  85 C0                           test eax, eax
00C2F8F5  0F 88 B1 07 00 00               js 0x140c300ac
00C2F8FB  33 D2                           xor edx, edx
00C2F8FD  48 8D 4D 30                     lea rcx, [rbp + 0x30]
00C2F901  44 8D 42 40                     lea r8d, [rdx + 0x40]
00C2F905  E8 36 73 A9 FF                  call 0x1406c6c40
00C2F90A  48 8D 4D 30                     lea rcx, [rbp + 0x30]
00C2F90E  E8 19 53 00 00                  call 0x140c34c2c
00C2F913  8B D8                           mov ebx, eax
00C2F915  85 C0                           test eax, eax
00C2F917  78 1A                           js 0x140c2f933
00C2F919  48 8D 4D 30                     lea rcx, [rbp + 0x30]
00C2F91D  E8 EE 4D 00 00                  call 0x140c34710
00C2F922  8B D8                           mov ebx, eax
00C2F924  85 C0                           test eax, eax
00C2F926  78 0B                           js 0x140c2f933
00C2F928  48 8D 4D 30                     lea rcx, [rbp + 0x30]
00C2F92C  E8 3F 4C 00 00                  call 0x140c34570
00C2F931  8B D8                           mov ebx, eax
00C2F933  48 8D 4D 30                     lea rcx, [rbp + 0x30]
00C2F937  E8 18 55 00 00                  call 0x140c34e54
00C2F93C  85 DB                           test ebx, ebx
00C2F93E  0F 88 68 07 00 00               js 0x140c300ac
00C2F944  E8 D7 57 00 00                  call 0x140c35120
00C2F949  8B D8                           mov ebx, eax
00C2F94B  85 C0                           test eax, eax
00C2F94D  0F 88 59 07 00 00               js 0x140c300ac
00C2F953  E8 4C 58 00 00                  call 0x140c351a4
00C2F958  8B D8                           mov ebx, eax
00C2F95A  85 C0                           test eax, eax
00C2F95C  0F 88 4A 07 00 00               js 0x140c300ac
00C2F962  E8 29 28 00 00                  call 0x140c32190
00C2F967  48 8B 0D 2A 6A 23 00            mov rcx, qword ptr [rip + 0x236a2a]
00C2F96E  4C 8D 4D 88                     lea r9, [rbp - 0x78]
00C2F972  45 8B C4                        mov r8d, r12d
00C2F975  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00C2F97A  4C 8D 25 5F A5 04 00            lea r12, [rip + 0x4a55f]
00C2F981  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00C2F986  49 8B D4                        mov rdx, r12
00C2F989  E8 2E 01 CD FF                  call 0x1408ffabc
00C2F98E  8B D8                           mov ebx, eax
00C2F990  85 C0                           test eax, eax
00C2F992  0F 88 14 07 00 00               js 0x140c300ac
00C2F998  48 8B 5D 88                     mov rbx, qword ptr [rbp - 0x78]
00C2F99C  4C 8D 2D 5D A5 04 00            lea r13, [rip + 0x4a55d]
00C2F9A3  48 8B 0D EE 69 23 00            mov rcx, qword ptr [rip + 0x2369ee]
00C2F9AA  4C 8B C3                        mov r8, rbx
00C2F9AD  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00C2F9B2  41 B9 25 00 00 00               mov r9d, 0x25
00C2F9B8  C7 44 24 30 4E 00 00 00         mov dword ptr [rsp + 0x30], 0x4e
00C2F9C0  49 8B D4                        mov rdx, r12
00C2F9C3  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00C2F9C8  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00C2F9CC  E8 BB DC CC FF                  call 0x1408fd68c
00C2F9D1  48 8B 0D C0 69 23 00            mov rcx, qword ptr [rip + 0x2369c0]
00C2F9D8  48 8D 45 84                     lea rax, [rbp - 0x7c]
00C2F9DC  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00C2F9E1  41 B9 0B 00 00 00               mov r9d, 0xb
00C2F9E7  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
00C2F9EC  4C 8B C3                        mov r8, rbx
00C2F9EF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C2F9F4  49 8B D4                        mov rdx, r12
00C2F9F7  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
00C2F9FC  44 89 75 84                     mov dword ptr [rbp - 0x7c], r14d
00C2FA00  E8 87 DC CC FF                  call 0x1408fd68c
00C2FA05  48 8B CB                        mov rcx, rbx
00C2FA08  E8 A3 D8 A7 FF                  call 0x1406ad2b0
00C2FA0D  48 8D 05 3C CA 35 00            lea rax, [rip + 0x35ca3c]
00C2FA14  83 CB FF                        or ebx, 0xffffffff
00C2FA17  48 89 05 3A CA 35 00            mov qword ptr [rip + 0x35ca3a], rax
00C2FA1E  48 8D 0D 3B CB 35 00            lea rcx, [rip + 0x35cb3b]
00C2FA25  48 89 05 24 CA 35 00            mov qword ptr [rip + 0x35ca24], rax
00C2FA2C  8B D3                           mov edx, ebx
00C2FA2E  48 8D 05 1B CB 35 00            lea rax, [rip + 0x35cb1b]
00C2FA35  48 89 05 1C CB 35 00            mov qword ptr [rip + 0x35cb1c], rax
00C2FA3C  48 89 05 0D CB 35 00            mov qword ptr [rip + 0x35cb0d], rax
00C2FA43  E8 C8 FC 7E FF                  call 0x14041f710
00C2FA48  8B D3                           mov edx, ebx
00C2FA4A  48 8D 0D 0F CA 35 00            lea rcx, [rip + 0x35ca0f]
00C2FA51  E8 BA FC 7E FF                  call 0x14041f710
00C2FA56  8B D3                           mov edx, ebx
00C2FA58  48 8D 0D 81 CA 35 00            lea rcx, [rip + 0x35ca81]
00C2FA5F  E8 AC FC 7E FF                  call 0x14041f710
00C2FA64  48 8D 05 95 C9 35 00            lea rax, [rip + 0x35c995]
00C2FA6B  4C 89 35 1E B3 35 00            mov qword ptr [rip + 0x35b31e], r14
00C2FA72  48 89 05 8F C9 35 00            mov qword ptr [rip + 0x35c98f], rax
00C2FA79  48 8D 0D 20 D4 35 00            lea rcx, [rip + 0x35d420]
00C2FA80  48 89 05 79 C9 35 00            mov qword ptr [rip + 0x35c979], rax
00C2FA87  8B D3                           mov edx, ebx
00C2FA89  48 8D 05 30 C9 35 00            lea rax, [rip + 0x35c930]
00C2FA90  89 3D 4A C9 35 00               mov dword ptr [rip + 0x35c94a], edi
00C2FA96  48 89 05 2B C9 35 00            mov qword ptr [rip + 0x35c92b], rax
00C2FA9D  48 89 05 1C C9 35 00            mov qword ptr [rip + 0x35c91c], rax
00C2FAA4  4C 89 35 3D C9 35 00            mov qword ptr [rip + 0x35c93d], r14
00C2FAAB  44 89 35 3E C9 35 00            mov dword ptr [rip + 0x35c93e], r14d
00C2FAB2  66 89 3D 3F C9 35 00            mov word ptr [rip + 0x35c93f], di
00C2FAB9  C6 05 3A C9 35 00 06            mov byte ptr [rip + 0x35c93a], 6
00C2FAC0  44 89 35 35 C9 35 00            mov dword ptr [rip + 0x35c935], r14d
00C2FAC7  89 3D D3 C8 35 00               mov dword ptr [rip + 0x35c8d3], edi
00C2FACD  4C 89 35 D4 C8 35 00            mov qword ptr [rip + 0x35c8d4], r14
00C2FAD4  44 89 35 D5 C8 35 00            mov dword ptr [rip + 0x35c8d5], r14d
00C2FADB  66 89 3D D6 C8 35 00            mov word ptr [rip + 0x35c8d6], di
00C2FAE2  C6 05 D1 C8 35 00 06            mov byte ptr [rip + 0x35c8d1], 6
00C2FAE9  44 89 35 CC C8 35 00            mov dword ptr [rip + 0x35c8cc], r14d
00C2FAF0  E8 1B FC 7E FF                  call 0x14041f710
00C2FAF5  40 8A CF                        mov cl, dil
00C2FAF8  4C 89 35 09 D4 35 00            mov qword ptr [rip + 0x35d409], r14
00C2FAFF  E8 84 6C DD FF                  call 0x140a06788
00C2FB04  48 8D 05 75 D3 35 00            lea rax, [rip + 0x35d375]
00C2FB0B  48 89 05 76 D3 35 00            mov qword ptr [rip + 0x35d376], rax
00C2FB12  48 89 05 67 D3 35 00            mov qword ptr [rip + 0x35d367], rax
00C2FB19  48 8D 05 50 D3 35 00            lea rax, [rip + 0x35d350]
00C2FB20  48 89 05 51 D3 35 00            mov qword ptr [rip + 0x35d351], rax
00C2FB27  48 89 05 42 D3 35 00            mov qword ptr [rip + 0x35d342], rax
00C2FB2E  48 8D 05 2B D3 35 00            lea rax, [rip + 0x35d32b]
00C2FB35  48 89 05 2C D3 35 00            mov qword ptr [rip + 0x35d32c], rax
00C2FB3C  48 89 05 1D D3 35 00            mov qword ptr [rip + 0x35d31d], rax
00C2FB43  E8 CC 72 DD FF                  call 0x140a06e14
00C2FB48  49 8B C6                        mov rax, r14
00C2FB4B  48 87 05 5E 68 23 00            xchg qword ptr [rip + 0x23685e], rax
00C2FB52  44 88 35 E7 B1 35 00            mov byte ptr [rip + 0x35b1e7], r14b
00C2FB59  66 44 89 35 FF B1 35 00         mov word ptr [rip + 0x35b1ff], r14w
00C2FB61  C6 05 FA B1 35 00 06            mov byte ptr [rip + 0x35b1fa], 6
00C2FB68  89 3D F6 B1 35 00               mov dword ptr [rip + 0x35b1f6], edi
00C2FB6E  48 8D 05 F3 B1 35 00            lea rax, [rip + 0x35b1f3]
00C2FB75  89 3D 25 B1 35 00               mov dword ptr [rip + 0x35b125], edi
00C2FB7B  48 89 05 EE B1 35 00            mov qword ptr [rip + 0x35b1ee], rax
00C2FB82  48 8D 15 A7 59 00 00            lea rdx, [rip + 0x59a7]
00C2FB89  48 89 05 D8 B1 35 00            mov qword ptr [rip + 0x35b1d8], rax
00C2FB90  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00C2FB95  48 8D 05 E4 B1 35 00            lea rax, [rip + 0x35b1e4]
00C2FB9C  4C 89 35 05 B1 35 00            mov qword ptr [rip + 0x35b105], r14
00C2FBA3  48 89 05 DE B1 35 00            mov qword ptr [rip + 0x35b1de], rax
00C2FBAA  48 89 05 CF B1 35 00            mov qword ptr [rip + 0x35b1cf], rax
00C2FBB1  48 8D 05 28 B1 35 00            lea rax, [rip + 0x35b128]
00C2FBB8  48 89 05 29 B1 35 00            mov qword ptr [rip + 0x35b129], rax
00C2FBBF  48 89 05 1A B1 35 00            mov qword ptr [rip + 0x35b11a], rax
00C2FBC6  48 8D 05 F3 B0 35 00            lea rax, [rip + 0x35b0f3]
00C2FBCD  48 89 05 F4 B0 35 00            mov qword ptr [rip + 0x35b0f4], rax
00C2FBD4  48 89 05 E5 B0 35 00            mov qword ptr [rip + 0x35b0e5], rax
00C2FBDB  48 8D 05 26 B1 35 00            lea rax, [rip + 0x35b126]
00C2FBE2  48 89 05 27 B1 35 00            mov qword ptr [rip + 0x35b127], rax
00C2FBE9  48 89 05 18 B1 35 00            mov qword ptr [rip + 0x35b118], rax
00C2FBF0  48 8D 05 31 C8 35 00            lea rax, [rip + 0x35c831]
00C2FBF7  48 89 05 32 C8 35 00            mov qword ptr [rip + 0x35c832], rax
00C2FBFE  48 89 05 23 C8 35 00            mov qword ptr [rip + 0x35c823], rax
00C2FC05  48 8D 05 44 A3 04 00            lea rax, [rip + 0x4a344]
00C2FC0C  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00C2FC11  44 89 35 98 B0 35 00            mov dword ptr [rip + 0x35b098], r14d
00C2FC18  66 89 3D 99 B0 35 00            mov word ptr [rip + 0x35b099], di
00C2FC1F  C6 05 94 B0 35 00 06            mov byte ptr [rip + 0x35b094], 6
00C2FC26  44 89 35 8F B0 35 00            mov dword ptr [rip + 0x35b08f], r14d
00C2FC2D  44 89 35 A4 B0 35 00            mov dword ptr [rip + 0x35b0a4], r14d
00C2FC34  C6 05 C5 B0 35 00 05            mov byte ptr [rip + 0x35b0c5], 5
00C2FC3B  C6 05 C0 B0 35 00 08            mov byte ptr [rip + 0x35b0c0], 8
00C2FC42  89 3D BC B0 35 00               mov dword ptr [rip + 0x35b0bc], edi
00C2FC48  89 3D CA B0 35 00               mov dword ptr [rip + 0x35b0ca], edi
00C2FC4E  4C 89 35 C3 C7 35 00            mov qword ptr [rip + 0x35c7c3], r14
00C2FC55  66 89 3D C4 C7 35 00            mov word ptr [rip + 0x35c7c4], di
00C2FC5C  C6 05 BF C7 35 00 06            mov byte ptr [rip + 0x35c7bf], 6
00C2FC63  89 3D BB C7 35 00               mov dword ptr [rip + 0x35c7bb], edi
00C2FC69  C7 44 24 58 24 00 26 00         mov dword ptr [rsp + 0x58], 0x260024
00C2FC71  E8 FA A0 E9 FF                  call 0x140ac9d70
00C2FC76  8B D8                           mov ebx, eax
00C2FC78  85 C0                           test eax, eax
00C2FC7A  0F 88 2C 04 00 00               js 0x140c300ac
00C2FC80  48 8B 0D B9 C7 35 00            mov rcx, qword ptr [rip + 0x35c7b9]
00C2FC87  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00C2FC8C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C2FC91  45 8B CF                        mov r9d, r15d
00C2FC94  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
00C2FC99  45 33 C0                        xor r8d, r8d
00C2FC9C  33 D2                           xor edx, edx
00C2FC9E  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00C2FCA3  E8 58 4E D7 FF                  call 0x1409a4b00
00C2FCA8  8B D8                           mov ebx, eax
00C2FCAA  85 C0                           test eax, eax
00C2FCAC  0F 88 FA 03 00 00               js 0x140c300ac
00C2FCB2  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00C2FCB7  48 8D 15 7A C7 35 00            lea rdx, [rip + 0x35c77a]
00C2FCBE  48 8B CE                        mov rcx, rsi
00C2FCC1  0F BA 6E 30 0C                  bts dword ptr [rsi + 0x30], 0xc
00C2FCC6  E8 2D CC E6 FF                  call 0x140a9c8f8
00C2FCCB  48 8B 0D 66 C7 35 00            mov rcx, qword ptr [rip + 0x35c766]
00C2FCD2  8B D8                           mov ebx, eax
00C2FCD4  48 85 C9                        test rcx, rcx
00C2FCD7  75 21                           jne 0x140c2fcfa
00C2FCD9  48 8B CE                        mov rcx, rsi
00C2FCDC  E8 AF 01 64 FF                  call 0x14026fe90
00C2FCE1  48 8B 0D 58 C7 35 00            mov rcx, qword ptr [rip + 0x35c758]
00C2FCE8  E8 13 D7 AE FF                  call 0x14071d400
00C2FCED  85 DB                           test ebx, ebx
00C2FCEF  0F 88 B7 03 00 00               js 0x140c300ac
00C2FCF5  E9 BF 00 00 00                  jmp 0x140c2fdb9
00C2FCFA  BA 31 01 00 00                  mov edx, 0x131
00C2FCFF  E8 44 C3 CC FF                  call 0x1408fc048
00C2FD04  48 8B 0D 2D C7 35 00            mov rcx, qword ptr [rip + 0x35c72d]
00C2FD0B  BA 0A 00 00 00                  mov edx, 0xa
00C2FD10  E8 E7 BB CC FF                  call 0x1408fb8fc
00C2FD15  48 8B 05 1C C7 35 00            mov rax, qword ptr [rip + 0x35c71c]
00C2FD1C  BA 1A 00 00 00                  mov edx, 0x1a
00C2FD21  C7 80 94 02 00 00 FE FF FF FF   mov dword ptr [rax + 0x294], 0xfffffffe
00C2FD2B  48 8B 0D 06 C7 35 00            mov rcx, qword ptr [rip + 0x35c706]
00C2FD32  E8 F9 DE AF FF                  call 0x14072dc30
00C2FD37  8B D8                           mov ebx, eax
00C2FD39  85 C0                           test eax, eax
00C2FD3B  0F 88 6B 03 00 00               js 0x140c300ac
00C2FD41  48 8B 0D F0 C6 35 00            mov rcx, qword ptr [rip + 0x35c6f0]
00C2FD48  48 8D 55 B8                     lea rdx, [rbp - 0x48]
00C2FD4C  C7 45 B8 18 00 1A 00            mov dword ptr [rbp - 0x48], 0x1a0018
00C2FD53  4C 89 65 C0                     mov qword ptr [rbp - 0x40], r12
00C2FD57  E8 14 DF AF FF                  call 0x14072dc70
00C2FD5C  48 8B 0D D5 C6 35 00            mov rcx, qword ptr [rip + 0x35c6d5]
00C2FD63  48 8D 51 28                     lea rdx, [rcx + 0x28]
00C2FD67  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00C2FD6B  E8 14 DB E6 FF                  call 0x140a9d884
00C2FD70  8B D8                           mov ebx, eax
00C2FD72  85 C0                           test eax, eax
00C2FD74  0F 88 32 03 00 00               js 0x140c300ac
00C2FD7A  48 8B 15 B7 C6 35 00            mov rdx, qword ptr [rip + 0x35c6b7]
00C2FD81  48 8D 4D C8                     lea rcx, [rbp - 0x38]
00C2FD85  48 81 C2 98 02 00 00            add rdx, 0x298
00C2FD8C  C7 45 C8 4C 00 4E 00            mov dword ptr [rbp - 0x38], 0x4e004c
00C2FD93  4C 89 6D D0                     mov qword ptr [rbp - 0x30], r13
00C2FD97  E8 54 21 CC FF                  call 0x1408f1ef0
00C2FD9C  48 8B 0D 95 C6 35 00            mov rcx, qword ptr [rip + 0x35c695]
00C2FDA3  E8 40 BF CC FF                  call 0x1408fbce8
00C2FDA8  48 8B 0D 89 C6 35 00            mov rcx, qword ptr [rip + 0x35c689]
00C2FDAF  BA 0A 03 00 00                  mov edx, 0x30a
00C2FDB4  E8 4F 09 84 FF                  call 0x140470708
00C2FDB9  48 8B 0D D8 65 23 00            mov rcx, qword ptr [rip + 0x2365d8]
00C2FDC0  4D 8B CC                        mov r9, r12
00C2FDC3  4D 8B C5                        mov r8, r13
00C2FDC6  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00C2FDCB  49 8B D5                        mov rdx, r13
00C2FDCE  E8 BD F3 CC FF                  call 0x1408ff190
00C2FDD3  8B D8                           mov ebx, eax
00C2FDD5  85 C0                           test eax, eax
00C2FDD7  0F 88 CF 02 00 00               js 0x140c300ac
00C2FDDD  44 38 74 24 40                  cmp byte ptr [rsp + 0x40], r14b
00C2FDE2  74 05                           je 0x140c2fde9
00C2FDE4  E8 37 0D B0 FF                  call 0x140730b20
00C2FDE9  E8 8E 37 00 00                  call 0x140c3357c
00C2FDEE  E8 89 57 00 00                  call 0x140c3557c
00C2FDF3  8B D8                           mov ebx, eax
00C2FDF5  85 C0                           test eax, eax
00C2FDF7  0F 88 AF 02 00 00               js 0x140c300ac
00C2FDFD  E8 62 30 00 00                  call 0x140c32e64
00C2FE02  E8 89 3E 00 00                  call 0x140c33c90
00C2FE07  8B D8                           mov ebx, eax
00C2FE09  85 C0                           test eax, eax
00C2FE0B  0F 88 9B 02 00 00               js 0x140c300ac
00C2FE11  48 8D 05 10 AE 35 00            lea rax, [rip + 0x35ae10]
00C2FE18  66 89 3D 01 AE 35 00            mov word ptr [rip + 0x35ae01], di
00C2FE1F  48 89 05 0A AE 35 00            mov qword ptr [rip + 0x35ae0a], rax
00C2FE26  48 89 05 FB AD 35 00            mov qword ptr [rip + 0x35adfb], rax
00C2FE2D  C6 05 EE AD 35 00 06            mov byte ptr [rip + 0x35adee], 6
00C2FE34  89 3D EA AD 35 00               mov dword ptr [rip + 0x35adea], edi
00C2FE3A  E8 3D 58 00 00                  call 0x140c3567c
00C2FE3F  8B D8                           mov ebx, eax
00C2FE41  85 C0                           test eax, eax
00C2FE43  0F 88 63 02 00 00               js 0x140c300ac
00C2FE49  33 C9                           xor ecx, ecx
00C2FE4B  E8 D4 3E 00 00                  call 0x140c33d24
00C2FE50  8B D8                           mov ebx, eax
00C2FE52  85 C0                           test eax, eax
00C2FE54  0F 88 52 02 00 00               js 0x140c300ac
00C2FE5A  48 8D 05 CF B1 04 00            lea rax, [rip + 0x4b1cf]
00C2FE61  48 C7 45 88 22 00 24 00         mov qword ptr [rbp - 0x78], 0x240022
00C2FE69  48 8D 15 70 59 00 00            lea rdx, [rip + 0x5970]
00C2FE70  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00C2FE74  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00C2FE78  E8 F3 9E E9 FF                  call 0x140ac9d70
00C2FE7D  8B D8                           mov ebx, eax
00C2FE7F  85 C0                           test eax, eax
00C2FE81  0F 88 25 02 00 00               js 0x140c300ac
00C2FE87  33 C9                           xor ecx, ecx
00C2FE89  E8 7E A0 97 FF                  call 0x1405a9f0c
00C2FE8E  8B D8                           mov ebx, eax
00C2FE90  85 C0                           test eax, eax
00C2FE92  0F 88 14 02 00 00               js 0x140c300ac
00C2FE98  E8 DB 2C 00 00                  call 0x140c32b78
00C2FE9D  E8 6A 63 00 00                  call 0x140c3620c
00C2FEA2  85 C0                           test eax, eax
00C2FEA4  78 05                           js 0x140c2feab
00C2FEA6  E8 B9 62 00 00                  call 0x140c36164
00C2FEAB  48 8B 0D 86 C5 35 00            mov rcx, qword ptr [rip + 0x35c586]
00C2FEB2  45 33 C9                        xor r9d, r9d
00C2FEB5  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00C2FEBA  45 33 C0                        xor r8d, r8d
00C2FEBD  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00C2FEC2  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00C2FEC7  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00C2FECB  41 8D 51 0A                     lea edx, [r9 + 0xa]
00C2FECF  E8 24 81 84 FF                  call 0x140477ff8
00C2FED4  E9 D3 01 00 00                  jmp 0x140c300ac
00C2FED9  BF 01 00 00 00                  mov edi, 1
00C2FEDE  3B D7                           cmp edx, edi
00C2FEE0  0F 85 C1 01 00 00               jne 0x140c300a7
00C2FEE6  4C 8D 05 B3 6E 1D 00            lea r8, [rip + 0x1d6eb3]
00C2FEED  4D 8B C8                        mov r9, r8
00C2FEF0  48 8D 0D 19 6F 3F FF            lea rcx, [rip - 0xc090e7]
00C2FEF7  E8 08 F0 94 FF                  call 0x14057ef04
00C2FEFC  48 8B 0D 9D 6E 1D 00            mov rcx, qword ptr [rip + 0x1d6e9d]
00C2FF03  4C 8D 0D C6 63 23 00            lea r9, [rip + 0x2363c6]
00C2FF0A  85 C0                           test eax, eax
00C2FF0C  48 89 0D C5 63 23 00            mov qword ptr [rip + 0x2363c5], rcx
00C2FF13  41 8B DE                        mov ebx, r14d
00C2FF16  48 8D 15 83 17 E2 FF            lea rdx, [rip - 0x1de87d]
00C2FF1D  0F 48 D8                        cmovs ebx, eax
00C2FF20  48 8D 0D 09 6E 3F FF            lea rcx, [rip - 0xc091f7]
00C2FF27  45 33 C0                        xor r8d, r8d
00C2FF2A  E8 31 0A CF FF                  call 0x140920960
00C2FF2F  85 C0                           test eax, eax
00C2FF31  0F 88 77 01 00 00               js 0x140c300ae
00C2FF37  8B C3                           mov eax, ebx
00C2FF39  85 DB                           test ebx, ebx
00C2FF3B  0F 88 6D 01 00 00               js 0x140c300ae
00C2FF41  48 8D 0D 48 70 1D 00            lea rcx, [rip + 0x1d7048]
00C2FF48  E8 1F 53 AD FF                  call 0x14070526c
00C2FF4D  48 8D 0D 04 70 1D 00            lea rcx, [rip + 0x1d7004]
00C2FF54  E8 13 53 AD FF                  call 0x14070526c
00C2FF59  45 33 C0                        xor r8d, r8d
00C2FF5C  48 8D 0D 65 70 1D 00            lea rcx, [rip + 0x1d7065]
00C2FF63  33 D2                           xor edx, edx
00C2FF65  E8 36 09 CF FF                  call 0x1409208a0
00C2FF6A  8B CF                           mov ecx, edi
00C2FF6C  E8 6B 45 00 00                  call 0x140c344dc
00C2FF71  85 C0                           test eax, eax
00C2FF73  0F 88 35 01 00 00               js 0x140c300ae
00C2FF79  8B CF                           mov ecx, edi
00C2FF7B  E8 A4 3D 00 00                  call 0x140c33d24
00C2FF80  85 C0                           test eax, eax
00C2FF82  0F 88 26 01 00 00               js 0x140c300ae
00C2FF88  48 8B 8E F0 00 00 00            mov rcx, qword ptr [rsi + 0xf0]
00C2FF8F  4C 8D 45 70                     lea r8, [rbp + 0x70]
00C2FF93  8D 57 01                        lea edx, [rdi + 1]
00C2FF96  48 C7 45 78 50 00 00 00         mov qword ptr [rbp + 0x78], 0x50
00C2FF9E  48 C7 85 88 00 00 00 08 00 00 00  mov qword ptr [rbp + 0x88], 8
00C2FFA9  48 8D 81 88 00 00 00            lea rax, [rcx + 0x88]
00C2FFB0  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00C2FFB4  48 8D 81 18 0F 00 00            lea rax, [rcx + 0xf18]
00C2FFBB  48 8D 0D AE 75 3F FF            lea rcx, [rip - 0xc08a52]
00C2FFC2  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00C2FFC9  E8 B6 E3 63 FF                  call 0x14026e384
00C2FFCE  8B CF                           mov ecx, edi
00C2FFD0  E8 CF 00 B0 FF                  call 0x1407300a4
00C2FFD5  85 C0                           test eax, eax
00C2FFD7  0F 88 D1 00 00 00               js 0x140c300ae
00C2FFDD  E8 D6 62 00 00                  call 0x140c362b8
00C2FFE2  85 C0                           test eax, eax
00C2FFE4  0F 88 C4 00 00 00               js 0x140c300ae
00C2FFEA  8B CF                           mov ecx, edi
00C2FFEC  E8 1B 9F 97 FF                  call 0x1405a9f0c
00C2FFF1  8B D8                           mov ebx, eax
00C2FFF3  85 C0                           test eax, eax
00C2FFF5  0F 88 B1 00 00 00               js 0x140c300ac
00C2FFFB  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00C30000  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
00C30005  48 FF 15 0C 13 52 FF            call qword ptr [rip - 0xadecf4]
00C3000C  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00C30011  85 C0                           test eax, eax
00C30013  78 15                           js 0x140c3002a
00C30015  40 88 3D 6C A9 35 00            mov byte ptr [rip + 0x35a96c], dil
00C3001C  E8 1F 65 00 00                  call 0x140c36540
00C30021  85 C0                           test eax, eax
00C30023  79 0C                           jns 0x140c30031
00C30025  E9 84 00 00 00                  jmp 0x140c300ae
00C3002A  44 88 35 57 A9 35 00            mov byte ptr [rip + 0x35a957], r14b
00C30031  48 8B 0D 00 C4 35 00            mov rcx, qword ptr [rip + 0x35c400]
00C30038  45 33 C9                        xor r9d, r9d
00C3003B  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00C30040  45 33 C0                        xor r8d, r8d
00C30043  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00C30048  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00C3004D  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00C30051  41 8D 51 0A                     lea edx, [r9 + 0xa]
00C30055  E8 9E 7F 84 FF                  call 0x140477ff8
00C3005A  48 8D 05 87 C5 35 00            lea rax, [rip + 0x35c587]
00C30061  66 44 89 35 77 C5 35 00         mov word ptr [rip + 0x35c577], r14w
00C30069  48 89 05 80 C5 35 00            mov qword ptr [rip + 0x35c580], rax
00C30070  48 89 05 71 C5 35 00            mov qword ptr [rip + 0x35c571], rax
00C30077  C6 05 64 C5 35 00 06            mov byte ptr [rip + 0x35c564], 6
00C3007E  44 89 35 5F C5 35 00            mov dword ptr [rip + 0x35c55f], r14d
00C30085  48 8B 86 F0 00 00 00            mov rax, qword ptr [rsi + 0xf0]
00C3008C  F7 80 84 00 00 00 00 04 00 00   test dword ptr [rax + 0x84], 0x400
00C30096  75 0A                           jne 0x140c300a2
00C30098  8B D7                           mov edx, edi
00C3009A  48 8B CE                        mov rcx, rsi
00C3009D  E8 76 3F 00 00                  call 0x140c34018
00C300A2  41 8B DE                        mov ebx, r14d
00C300A5  EB 05                           jmp 0x140c300ac
00C300A7  BB F0 00 00 C0                  mov ebx, 0xc00000f0
00C300AC  8B C3                           mov eax, ebx
00C300AE  48 8B 8D 90 00 00 00            mov rcx, qword ptr [rbp + 0x90]
00C300B5  48 33 CC                        xor rcx, rsp
00C300B8  E8 83 C5 A7 FF                  call 0x1406ac640
00C300BD  4C 8D 9C 24 A0 01 00 00         lea r11, [rsp + 0x1a0]
00C300C5  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00C300C9  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00C300CD  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00C300D1  49 8B E3                        mov rsp, r11
00C300D4  41 5F                           pop r15
00C300D6  41 5E                           pop r14
00C300D8  41 5D                           pop r13
00C300DA  41 5C                           pop r12
00C300DC  5D                              pop rbp
00C300DD  C3                              ret
00C300DE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopInitializePlugPlayServices(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m15C;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m16C;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int8 v_stack_m188;
    unsigned int v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (416);
    result = (*(unsigned __int64 *)(v_rip + 1946747)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 200 + 144) = result;
    v_r14 = 0;
    *(unsigned __int64 *)(v_rsp - 200 - 120) = 0;
    v_stack_m180 = 0;
    *(unsigned __int64 *)(v_rsp - 200 - 96) = 0;
    v_stack_m16C = 0;
    v_stack_m150 = 0;
    *(unsigned int *)(v_rsp - 200 - 128) = 0;
    *(unsigned int *)(v_rsp - 200 - 4) = 0;
    *(unsigned int *)(v_rsp - 200 + 20) = 0;
    *(unsigned __int64 *)(v_rsp - 200 - 104) = 0;
    v_stack_m178 = 0;
    *(unsigned __int64 *)(v_rsp - 200 - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 200 - 80) = 0;
    v_stack_m158 = 0;
    *(unsigned int *)(v_rsp - 200 - 68) = 0;
    *(unsigned int *)(v_rsp - 200 - 52) = 0;
    v_stack_m188 = 0;
    *(unsigned __int64 *)(v_rsp - 200 - 24) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 200 - 40) = v_xmm1;
    if (a2 != 0) goto loc_00C2FED9;
    *(unsigned __int8 *)(v_rip + 3526721) = 0;
    *(unsigned int *)(v_rip + 2322351) = 80;
    *(unsigned int *)(v_rip + 2322345) = 90;
    result = CmRegisterSystemHiveLimitCallback(a1, a2, v_rip + 2322368, a4);
    *(unsigned __int8 *)(v_rip + 2322314) = 0;
    *(unsigned __int64 *)(v_rsp - 200 + 8) = v_rip + 3844745;
    *(unsigned int *)(v_rsp - 200 - 8) = 48;
    v_stack_m198 = v_rsp - 200 - 128;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = 0;
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 200) = 0;
    *(unsigned int *)(v_rsp - 200 + 16) = 576;
    *(unsigned __int64 *)(v_rsp - 200 + 24) = v_xmm0;
    result = ZwCreateKey(v_stack_m158, (unsigned int)((unsigned int)((unsigned int)(0xF003FULL))), v_rsp - 200 - 8, a4);
    if (sign_flag) goto loc_00C2F45C;
    a3 = 0;
    result = IopGetRegistryValue(v_stack_m158, v_rip + 305796, a3, v_rsp - 200 - 104);
    if (sign_flag) goto loc_00C2F452;
    if (*(unsigned __int64 *)(v_rsp - 200 - 104) == 0) goto loc_00C2F452;
    a3 = 0;
    result = IopGetRegistryValue(v_stack_m158, v_rip + 305806, a3, v_stack_m178);
    if (sign_flag) goto loc_00C2F448;
    if (v_stack_m178 != 0) {
        a2 = *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 200 - 104) + 8);
        a1 = v_rsp - 200 - 24;
        a2 = (a2) + (*(unsigned __int64 *)(v_rsp - 200 - 104));
        result = RtlInitUnicodeString(a1, a2, a3, v_stack_m178);
        a2 = *(unsigned int *)(v_stack_m178 + 8);
        a1 = v_rsp - 200 - 40;
        a2 = (a2) + (v_stack_m178);
        result = RtlInitUnicodeString(a1, a2, a3, v_stack_m178);
        a4 = 0;
        v_stack_m1A8 = 0;
        a3 = 0x4000002CULL;
        a2 = v_rsp - 200 - 40;
        a1 = v_rsp - 200 - 24;
        result = PnpLogEvent(a1, a2, a3, a4);
        a2 = 0;
        a1 = v_stack_m178;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 200 - 104), a2, a3, a4);
loc_00C2F452:
    result = ZwClose(v_stack_m158, a2, a3, a4);
loc_00C2F45C:
    *(unsigned __int64 *)(v_rip + 3526366) = 0;
    *(unsigned __int64 *)(v_rip + 3526295) = v_rip + 3526301;
    *(unsigned __int64 *)(v_rip + 3526277) = v_rip + 3526301;
    *(unsigned __int64 *)(v_rip + 3526319) = v_rip + 3526318;
    *(unsigned __int64 *)(v_rip + 3526304) = v_rip + 3526318;
    *(unsigned __int64 *)(v_rip + 3526274) = v_rip + 3526273;
    *(unsigned __int64 *)(v_rip + 3526259) = v_rip + 3526273;
    *(unsigned int *)(v_rip + 3526244) = 0;
    *(unsigned __int8 *)(v_rip + 3526261) = 5;
    *(unsigned __int8 *)(v_rip + 3526256) = 8;
    *(unsigned int *)(v_rip + 3526251) = 0;
    *(unsigned int *)(v_rip + 3526261) = 0x7FFFFFFFULL;
    result = PiInitFirmwareResources(a1, a2, a3, a4);
    result = *(unsigned __int64 *)(a1 + 240);
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 132)) & (0x400ULL)) == 0) {
        a2 = 0;
        a1 = a1;
        result = PpInitializeBootDDB(a1, a2, a3, a4);
    }
    result = PipInitDeviceOverrideCache(a1, a2, a3, a4);
    *(unsigned __int16 *)(v_rip + 3529407) = 0;
    *(unsigned __int64 *)(v_rip + 3529416) = v_rip + 3529423;
    *(unsigned __int64 *)(v_rip + 3529401) = v_rip + 3529423;
    *(unsigned __int8 *)(v_rip + 3529388) = 6;
    *(unsigned int *)(v_rip + 3529383) = 0;
    result = PiInitCacheGroupInformation(a1, a2, a3, a4);
    if (sign_flag) goto loc_00C300AE;
    *(unsigned __int8 *)(v_rip + 3526184) = 5;
    *(unsigned __int64 *)(v_rip + 3526188) = v_rip + 3526199;
    *(unsigned __int64 *)(v_rip + 3526173) = v_rip + 3526199;
    *(unsigned __int8 *)(v_rip + 3526146) = 8;
    *(unsigned int *)(v_rip + 3526142) = 1;
    *(unsigned int *)(v_rip + 3526156) = 1;
loc_00C2F56C:
    *(unsigned __int64 *)(v_rip + 3525639 + 8) = v_rip + 3525639;
    *(unsigned __int64 *)(v_rip + 3525639) = v_rip + 3525639;
    result = (v_rip + 3525639) + (16);
    if (result < (v_rip + 3525934)) goto loc_00C2F56C;
    result = IopInitializeResourceMap(a1, a2, a3, a4);
    *(unsigned __int64 *)(v_rip + 3525536) = v_rip + 19775;
    *(unsigned __int64 *)(v_rip + 4034841) = 0;
    *(unsigned int *)(v_rip + 1946735) = 1;
    result = ArbInitializeOsInaccessibleRange((unsigned int)(*(unsigned int *)(v_rip + 2090670)), a2, a3, a4);
    result = ArbLibraryInitialize((unsigned int)(*(unsigned int *)(v_rip + 2090670)), a2, a3, a4);
    if (sign_flag) goto loc_00C300AC;
    result = IopPortInitialize((unsigned int)(*(unsigned int *)(v_rip + 2090670)), a2, a3, a4);
    if (sign_flag) goto loc_00C300AC;
    result = IopMemInitialize((unsigned int)(*(unsigned int *)(v_rip + 2090670)), a2, a3, a4);
    if (sign_flag) goto loc_00C300AC;
    result = IopDmaInitialize((unsigned int)(*(unsigned int *)(v_rip + 2090670)), a2, a3, a4);
    if (sign_flag) goto loc_00C300AC;
    result = IopIrqInitialize((unsigned int)(*(unsigned int *)(v_rip + 2090670)), a2, a3, a4);
    if (sign_flag) goto loc_00C300AC;
    result = IopBusNumberInitialize((unsigned int)(*(unsigned int *)(v_rip + 2090670)), a2, a3, a4);
    if (sign_flag) goto loc_00C300AC;
    a1 = 0;
    result = PiPnpRtlInit(a1, a2, a3, a4);
    if (sign_flag) goto loc_00C300AC;
    result = PipMigratePnpState(a1, a2, a3, a4);
    result = PiDmInit(a1, a2, a3, a4);
    if (sign_flag) goto loc_00C300AC;
    result = _PnpCtxGetCachedContextBaseKey(*(unsigned __int64 *)(v_rip + 2321768), 4, v_rsp - 200 - 96, a4);
    if (sign_flag) goto loc_00C300AC;
    v_stack_m1A0 = 0;
    v_stack_m168 = v_rip + 305225;
    v_stack_m170 = 0x180016ULL;
    v_stack_m1A8 = 0;
    result = IopCreateRegistryKeyEx(v_stack_m180, *(unsigned __int64 *)(v_rsp - 200 - 96), v_stack_m170, (unsigned int)((unsigned int)((unsigned int)(0xF003FULL))));
    if (sign_flag) goto loc_00C2F7B1;
    a3 = 0;
    result = IopGetRegistryValue(v_stack_m180, v_rip + 305189, a3, v_rsp - 200 - 88);
    if (sign_flag) goto loc_00C2F6C7;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 200 - 88) + 4)) != 4) goto loc_00C2F6C0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 200 - 88) + 12)) == 4) {
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 200 - 88) + 8);
        a2 = *(unsigned int *)(result + *(unsigned __int64 *)(v_rsp - 200 - 88) * 1);
        *(unsigned int *)(v_rip + 1946396) = a2;
    }
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 200 - 88), a2, a3, v_rsp - 200 - 88);
loc_00C2F6C7:
    a3 = 0;
    result = IopGetRegistryValue(v_stack_m180, v_rip + 305318, a3, v_rsp - 200 - 80);
    if (sign_flag) goto loc_00C2F706;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 200 - 80) + 4)) != 4) goto loc_00C2F6FF;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 200 - 80) + 12)) == 4) {
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 200 - 80) + 8);
        a2 = *(unsigned int *)(result + *(unsigned __int64 *)(v_rsp - 200 - 80) * 1);
        *(unsigned int *)(v_rip + 1946341) = a2;
    }
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 200 - 80), a2, a3, v_rsp - 200 - 80);
loc_00C2F706:
    v_stack_m160 = 0;
    result = PnpGetRegistryDword(v_stack_m180, v_rip + 309273, v_stack_m160, v_rsp - 200 - 80);
    if (sign_flag) goto loc_00C2F732;
    if (v_stack_m160 == 1) {
        *(unsigned __int8 *)(v_rip + 3521750) = 1;
    }
    result = PiUEventProcessRegistry(v_stack_m180, v_rip + 309273, v_stack_m160, v_rsp - 200 - 80);
    v_stack_m15C = 0;
    result = PnpGetRegistryDword(v_stack_m180, v_rip + 308515, v_stack_m15C, v_rsp - 200 - 80);
    if (sign_flag) goto loc_00C2F77A;
    if (((unsigned int)((unsigned int)(v_stack_m15C))) < 100) goto loc_00C2F771;
    if (((unsigned int)((unsigned int)(v_stack_m15C))) <= ((unsigned int)((unsigned int)(0xEA60ULL)))) goto loc_00C2F77F;
loc_00C2F771:
    *(unsigned __int16 *)(v_rip + 1946224) = (unsigned __int16)((unsigned int)(0xEA60ULL));
    goto loc_00C2F786;
loc_00C2F77A:
loc_00C2F77F:
    *(unsigned __int16 *)(v_rip + 1946210) = (unsigned __int16)((unsigned int)(0x1388ULL));
loc_00C2F786:
    *(unsigned __int64 *)(v_rip + 3528695) = v_rip - 5292114;
    *(unsigned __int64 *)(v_rip + 3528696) = v_stack_m180;
    *(unsigned __int64 *)(v_rip + 3528665) = 0;
    result = PipUpdateAsyncOptionsCallback(v_stack_m180, v_rip + 308515, v_stack_m15C, v_rsp - 200 - 80);
    v_stack_m180 = 0;
loc_00C2F7B1:
    v_stack_m170 = 0x3E003CULL;
    v_stack_m168 = v_rip + 305160;
    a2 = 0;
    result = IopOpenRegistryKeyEx(v_stack_m180, a2, v_stack_m170, (unsigned int)(0x20019ULL));
    if (sign_flag) goto loc_00C2F8C3;
    result = PipUpdateSetupInProgress(v_stack_m180, a2, v_stack_m170, (unsigned int)(0x20019ULL));
    a3 = 0;
    result = IopGetRegistryValue(v_stack_m180, v_rip + 305150, a3, v_stack_m178);
    if (sign_flag) goto loc_00C2F833;
    if ((*(unsigned int *)(v_stack_m178 + 4)) != 4) goto loc_00C2F82C;
    if ((*(unsigned int *)(v_stack_m178 + 12)) != 4) goto loc_00C2F82C;
    if ((*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m178 + 8)) + v_stack_m178 * 1)) != 0) {
        *(unsigned __int8 *)(v_rip + 2320974) = 1;
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m178, a2, a3, v_stack_m178);
loc_00C2F833:
    a3 = 0;
    result = IopGetRegistryValue(v_stack_m180, v_rip + 305097, a3, v_stack_m178);
    if (sign_flag) goto loc_00C2F878;
    if ((*(unsigned int *)(v_stack_m178 + 4)) != 4) goto loc_00C2F871;
    if ((*(unsigned int *)(v_stack_m178 + 12)) != 4) goto loc_00C2F871;
    if ((*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m178 + 8)) + v_stack_m178 * 1)) != 0) {
        *(unsigned __int8 *)(v_rip + 2320903) = 1;
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m178, a2, a3, v_stack_m178);
loc_00C2F878:
    if ((*(unsigned __int8 *)(v_rip + 2320838)) != 0) goto loc_00C2F896;
    if ((*(unsigned __int8 *)(v_rip + 2320881)) != 0) goto loc_00C2F896;
    result = ZwClose(v_stack_m180, a2, a3, v_stack_m178);
    goto loc_00C2F8BE;
loc_00C2F896:
    a2 = 0;
    *(unsigned __int64 *)(v_rip + 3528357) = v_rip - 5291938;
    *(unsigned __int64 *)(v_rip + 3528358) = v_stack_m180;
    *(unsigned __int64 *)(v_rip + 3528327) = 0;
    result = PipUpdateSetupInProgressNotify(v_stack_m180, a2, a3, v_stack_m178);
loc_00C2F8BE:
    v_stack_m180 = 0;
loc_00C2F8C3:
    a1 = (*(unsigned __int64 *)(a1 + 240)) + (0xA08ULL);
    result = PipHardwareConfigInit(a1, a2, a3, v_stack_m178);
    if (sign_flag) goto loc_00C300AC;
    result = PipCheckSystemFirmwareUpdated(v_stack_m188, a2, a3, v_stack_m178);
    a1 = 0;
    result = PiDcInit(a1, a2, a3, v_stack_m178);
    if (sign_flag) goto loc_00C300AC;
    a2 = 0;
    result = memset(v_rsp - 200 + 48, a2, a2 + 64, v_stack_m178);
    result = PiAuCreateUserSids(v_rsp - 200 + 48, a2, a2 + 64, v_stack_m178);
    if (sign_flag) goto loc_00C2F933;
    result = PiAuCreateStandardSecurityObject(v_rsp - 200 + 48, a2, a2 + 64, v_stack_m178);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        a1 = v_rsp - 200 + 48;
        result = PiAuCreateLocalSystemSecurityObject(a1, a2, a2 + 64, v_stack_m178);
        v_rbx = (unsigned int)(result);
    }
    result = PiAuFreeUserSids(v_rsp - 200 + 48, a2, a2 + 64, v_stack_m178);
    if (sign_flag) goto loc_00C300AC;
    result = PiDqInit(v_rsp - 200 + 48, a2, a2 + 64, v_stack_m178);
    if (sign_flag) goto loc_00C300AC;
    result = PpDevCfgInit(v_rsp - 200 + 48, a2, a2 + 64, v_stack_m178);
    if (sign_flag) goto loc_00C300AC;
    result = PipResetDevices(v_rsp - 200 + 48, a2, a2 + 64, v_stack_m178);
    v_stack_m1A0 = 0;
    v_stack_m1A8 = 0;
    result = CmCreateDevice(*(unsigned __int64 *)(v_rip + 2320938), v_rip + 304479, (unsigned int)((unsigned int)((unsigned int)(0xF003FULL))), v_rsp - 200 - 120);
    if (sign_flag) goto loc_00C300AC;
    v_stack_m190 = 0;
    v_stack_m198 = 78;
    v_stack_m1A0 = v_rip + 304477;
    v_stack_m1A8 = 1;
    result = CmSetDeviceRegProp(*(unsigned __int64 *)(v_rip + 2320878), v_rip + 304479, *(unsigned __int64 *)(v_rsp - 200 - 120), 37);
    v_stack_m190 = 0;
    v_stack_m198 = 4;
    v_stack_m1A0 = v_rsp - 200 - 124;
    v_stack_m1A8 = 4;
    *(unsigned int *)(v_rsp - 200 - 124) = 0;
    result = CmSetDeviceRegProp(*(unsigned __int64 *)(v_rip + 2320832), v_rip + 304479, *(unsigned __int64 *)(v_rsp - 200 - 120), 11);
    result = ZwClose(*(unsigned __int64 *)(v_rsp - 200 - 120), v_rip + 304479, *(unsigned __int64 *)(v_rsp - 200 - 120), 11);
    v_rbx = (unsigned int)((*(unsigned __int64 *)(v_rsp - 200 - 120)) | (0xFFFFFFFFULL));
    *(unsigned __int64 *)(v_rip + 3525178) = v_rip + 3525180;
    *(unsigned __int64 *)(v_rip + 3525156) = v_rip + 3525180;
    *(unsigned __int64 *)(v_rip + 3525404) = v_rip + 3525403;
    *(unsigned __int64 *)(v_rip + 3525389) = v_rip + 3525403;
    result = ExInitializeResourceLite2(v_rip + 3525435, (unsigned int)((unsigned int)(v_rbx)), *(unsigned __int64 *)(v_rsp - 200 - 120), 11);
    result = ExInitializeResourceLite2(v_rip + 3525135, (unsigned int)((unsigned int)(v_rbx)), *(unsigned __int64 *)(v_rsp - 200 - 120), 11);
    result = ExInitializeResourceLite2(v_rip + 3525249, (unsigned int)((unsigned int)(v_rbx)), *(unsigned __int64 *)(v_rsp - 200 - 120), 11);
    *(unsigned __int64 *)(v_rip + 3519262) = 0;
    *(unsigned __int64 *)(v_rip + 3525007) = v_rip + 3525013;
    *(unsigned __int64 *)(v_rip + 3524985) = v_rip + 3525013;
    *(unsigned int *)(v_rip + 3524938) = 1;
    *(unsigned __int64 *)(v_rip + 3524907) = v_rip + 3524912;
    *(unsigned __int64 *)(v_rip + 3524892) = v_rip + 3524912;
    *(unsigned __int64 *)(v_rip + 3524925) = 0;
    *(unsigned int *)(v_rip + 3524926) = 0;
    *(unsigned __int16 *)(v_rip + 3524927) = 1;
    *(unsigned __int8 *)(v_rip + 3524922) = 6;
    *(unsigned int *)(v_rip + 3524917) = 0;
    *(unsigned int *)(v_rip + 3524819) = 1;
    *(unsigned __int64 *)(v_rip + 3524820) = 0;
    *(unsigned int *)(v_rip + 3524821) = 0;
    *(unsigned __int16 *)(v_rip + 3524822) = 1;
    *(unsigned __int8 *)(v_rip + 3524817) = 6;
    *(unsigned int *)(v_rip + 3524812) = 0;
    result = ExInitializeResourceLite2(v_rip + 3527712, (unsigned int)((unsigned int)(v_rbx)), *(unsigned __int64 *)(v_rsp - 200 - 120), 11);
    *(unsigned __int64 *)(v_rip + 3527689) = 0;
    result = PnpAcquireDependencyRelationsLock(1, (unsigned int)((unsigned int)(v_rbx)), *(unsigned __int64 *)(v_rsp - 200 - 120), 11);
    *(unsigned __int64 *)(v_rip + 3527542) = v_rip + 3527541;
    *(unsigned __int64 *)(v_rip + 3527527) = v_rip + 3527541;
    *(unsigned __int64 *)(v_rip + 3527505) = v_rip + 3527504;
    *(unsigned __int64 *)(v_rip + 3527490) = v_rip + 3527504;
    *(unsigned __int64 *)(v_rip + 3527468) = v_rip + 3527467;
    *(unsigned __int64 *)(v_rip + 3527453) = v_rip + 3527467;
    result = PnpReleaseDependencyRelationsLock(1, (unsigned int)((unsigned int)(v_rbx)), *(unsigned __int64 *)(v_rsp - 200 - 120), 11);
    *(unsigned __int8 *)(v_rip + 3518951) = 0;
    *(unsigned __int16 *)(v_rip + 3518975) = 0;
    *(unsigned __int8 *)(v_rip + 3518970) = 6;
    *(unsigned int *)(v_rip + 3518966) = 1;
    *(unsigned int *)(v_rip + 3518757) = 1;
    *(unsigned __int64 *)(v_rip + 3518958) = v_rip + 3518963;
    *(unsigned __int64 *)(v_rip + 3518936) = v_rip + 3518963;
    *(unsigned __int64 *)(v_rip + 3518725) = 0;
    *(unsigned __int64 *)(v_rip + 3518942) = v_rip + 3518948;
    *(unsigned __int64 *)(v_rip + 3518927) = v_rip + 3518948;
    *(unsigned __int64 *)(v_rip + 3518761) = v_rip + 3518760;
    *(unsigned __int64 *)(v_rip + 3518746) = v_rip + 3518760;
    *(unsigned __int64 *)(v_rip + 3518708) = v_rip + 3518707;
    *(unsigned __int64 *)(v_rip + 3518693) = v_rip + 3518707;
    *(unsigned __int64 *)(v_rip + 3518759) = v_rip + 3518758;
    *(unsigned __int64 *)(v_rip + 3518744) = v_rip + 3518758;
    *(unsigned __int64 *)(v_rip + 3524658) = v_rip + 3524657;
    *(unsigned __int64 *)(v_rip + 3524643) = v_rip + 3524657;
    v_stack_m168 = v_rip + 303940;
    *(unsigned int *)(v_rip + 3518616) = 0;
    *(unsigned __int16 *)(v_rip + 3518617) = 1;
    *(unsigned __int8 *)(v_rip + 3518612) = 6;
    *(unsigned int *)(v_rip + 3518607) = 0;
    *(unsigned int *)(v_rip + 3518628) = 0;
    *(unsigned __int8 *)(v_rip + 3518661) = 5;
    *(unsigned __int8 *)(v_rip + 3518656) = 8;
    *(unsigned int *)(v_rip + 3518652) = 1;
    *(unsigned int *)(v_rip + 3518666) = 1;
    *(unsigned __int64 *)(v_rip + 3524547) = 0;
    *(unsigned __int16 *)(v_rip + 3524548) = 1;
    *(unsigned __int8 *)(v_rip + 3524543) = 6;
    *(unsigned int *)(v_rip + 3524539) = 1;
    v_stack_m170 = 0x260024ULL;
    result = IoCreateDriver(v_stack_m170, v_rip + 22951, *(unsigned __int64 *)(v_rsp - 200 - 120), 11);
    if (sign_flag) goto loc_00C300AC;
    v_stack_m198 = v_stack_m150;
    v_stack_m1A0 = 0;
    a3 = 0;
    a2 = 0;
    v_stack_m1A8 = 0;
    result = IoCreateDevice(*(unsigned __int64 *)(v_rip + 3524537), a2, a3, 4);
    if (sign_flag) goto loc_00C300AC;
    result = PipAllocateDeviceNode(v_stack_m150, v_rip + 3524474, a3, 4);
    if (*(unsigned __int64 *)(v_rip + 3524454) != 0) goto loc_00C2FCFA;
    result = IoDeleteDevice(v_stack_m150, v_rip + 3524474, a3, 4);
    result = IoDeleteDriver(*(unsigned __int64 *)(v_rip + 3524440), v_rip + 3524474, a3, 4);
    if (sign_flag) goto loc_00C300AC;
    goto loc_00C2FDB9;
loc_00C2FCFA:
    result = PipSetDevNodeFlags(*(unsigned __int64 *)(v_rip + 3524440), 305, a3, 4);
    result = PipSetDevNodeUserFlags(*(unsigned __int64 *)(v_rip + 3524397), 10, a3, 4);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3524380) + 660) = 0xFFFFFFFEULL;
    result = PnpAllocateDeviceInstancePath(*(unsigned __int64 *)(v_rip + 3524358), 26, a3, 4);
    if (sign_flag) goto loc_00C300AC;
    *(unsigned int *)(v_rsp - 200 - 72) = 0x1A0018ULL;
    *(unsigned __int64 *)(v_rsp - 200 - 64) = v_rip + 304479;
    result = PnpCopyDeviceInstancePath(*(unsigned __int64 *)(v_rip + 3524336), v_rsp - 200 - 72, a3, 4);
    result = PnpMapDeviceObjectToDeviceInstance(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3524309) + 32), *(unsigned __int64 *)(v_rip + 3524309) + 40, a3, 4);
    if (sign_flag) goto loc_00C300AC;
    a2 = (*(unsigned __int64 *)(v_rip + 3524279)) + (664);
    *(unsigned int *)(v_rsp - 200 - 56) = 0x4E004CULL;
    *(unsigned __int64 *)(v_rsp - 200 - 48) = v_rip + 304477;
    result = RtlGUIDFromString(v_rsp - 200 - 56, a2, a3, 4);
    result = PnpQueryAndSaveDeviceNodeCapabilities(*(unsigned __int64 *)(v_rip + 3524245), a2, a3, 4);
    result = PipSetDevNodeState(*(unsigned __int64 *)(v_rip + 3524233), 778, a3, 4);
loc_00C2FDB9:
    v_stack_m1A8 = 0;
    result = CmAddDeviceToContainer(*(unsigned __int64 *)(v_rip + 2319832), v_rip + 304477, v_rip + 304477, v_rip + 304479);
    if (sign_flag) goto loc_00C300AC;
    if (v_stack_m188 != 0) {
        result = PiDcHandleSystemFirmwareUpdate(*(unsigned __int64 *)(v_rip + 2319832), v_rip + 304477, v_rip + 304477, v_rip + 304479);
    }
    result = PnpInitializePnpWatchdogs(*(unsigned __int64 *)(v_rip + 2319832), v_rip + 304477, v_rip + 304477, v_rip + 304479);
    result = PnpInitializeDeviceEvents(*(unsigned __int64 *)(v_rip + 2319832), v_rip + 304477, v_rip + 304477, v_rip + 304479);
    if (sign_flag) goto loc_00C300AC;
    result = PnpInitializeNotification(*(unsigned __int64 *)(v_rip + 2319832), v_rip + 304477, v_rip + 304477, v_rip + 304479);
    result = PnpBusTypeGuidInitialize(*(unsigned __int64 *)(v_rip + 2319832), v_rip + 304477, v_rip + 304477, v_rip + 304479);
    if (sign_flag) goto loc_00C300AC;
    *(unsigned __int16 *)(v_rip + 3517953) = 1;
    *(unsigned __int64 *)(v_rip + 3517962) = v_rip + 3517968;
    *(unsigned __int64 *)(v_rip + 3517947) = v_rip + 3517968;
    *(unsigned __int8 *)(v_rip + 3517934) = 6;
    *(unsigned int *)(v_rip + 3517930) = 1;
    result = PiSwInit(*(unsigned __int64 *)(v_rip + 2319832), v_rip + 304477, v_rip + 304477, v_rip + 304479);
    if (sign_flag) goto loc_00C300AC;
    a1 = 0;
    result = PiUEventInit(a1, v_rip + 304477, v_rip + 304477, v_rip + 304479);
    if (sign_flag) goto loc_00C300AC;
    *(unsigned __int64 *)(v_rsp - 200 - 120) = 0x240022ULL;
    *(unsigned __int64 *)(v_rsp - 200 - 112) = v_rip + 307663;
    result = IoCreateDriver(v_rsp - 200 - 120, v_rip + 22896, v_rip + 304477, v_rip + 304479);
    if (sign_flag) goto loc_00C300AC;
    a1 = 0;
    result = PiDmaGuardInitialize(a1, v_rip + 22896, v_rip + 304477, v_rip + 304479);
    if (sign_flag) goto loc_00C300AC;
    result = IoInvalidateInit(a1, v_rip + 22896, v_rip + 304477, v_rip + 304479);
    result = PipProcessPendingServices(a1, v_rip + 22896, v_rip + 304477, v_rip + 304479);
    if (!(sign_flag)) {
        result = PipProcessPendingOsExtensionResources(a1, v_rip + 22896, v_rip + 304477, v_rip + 304479);
    }
    a4 = 0;
    v_stack_m198 = 0;
    a3 = 0;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = 0;
    result = PnpRequestDeviceAction(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3523974) + 32), a4 + 10, a3, a4);
    goto loc_00C300AC;
loc_00C2FED9:
    if (((unsigned int)(a4 + 10)) != 1) goto loc_00C300A7;
    result = McGenEventRegister_EtwRegister(v_rip - 12620007, a4 + 10, v_rip + 1928883, v_rip + 1928883);
    *(unsigned __int64 *)(v_rip + 2319301) = *(unsigned __int64 *)(v_rip + 1928861);
    v_rbx = 0;
    if (sign_flag) { v_rbx = (unsigned int)(result); }
    a3 = 0;
    result = EtwRegister(v_rip - 12620279, v_rip - 1960061, a3, v_rip + 2319302);
    if (sign_flag) goto loc_00C300AE;
    if (sign_flag) goto loc_00C300AE;
    result = TlgRegisterAggregateProvider(v_rip + 1929288, v_rip - 1960061, a3, v_rip + 2319302);
    result = TlgRegisterAggregateProvider(v_rip + 1929220, v_rip - 1960061, a3, v_rip + 2319302);
    a3 = 0;
    a2 = 0;
    result = TraceLoggingRegisterEx_EtwRegister_EtwSetInformation(v_rip + 1929317, a2, a3, v_rip + 2319302);
    result = PiDcInit(1, a2, a3, v_rip + 2319302);
    if (sign_flag) goto loc_00C300AE;
    result = PiUEventInit(1, a2, a3, v_rip + 2319302);
    if (sign_flag) goto loc_00C300AE;
    *(unsigned __int64 *)(v_rsp - 200 + 120) = 80;
    *(unsigned __int64 *)(v_rsp - 200 + 136) = 8;
    *(unsigned __int64 *)(v_rsp - 200 + 112) = *(unsigned __int64 *)(v_stack_m150 + 240) + 136;
    *(unsigned __int64 *)(v_rsp - 200 + 128) = *(unsigned __int64 *)(v_stack_m150 + 240) + 3864;
    result = PnpDiagnosticTrace(v_rip - 12618322, 1 + 1, v_rsp - 200 + 112, v_rip + 2319302);
    result = PiPnpRtlInit(1, 1 + 1, v_rsp - 200 + 112, v_rip + 2319302);
    if (sign_flag) goto loc_00C300AE;
    result = PiCslInitialize(1, 1 + 1, v_rsp - 200 + 112, v_rip + 2319302);
    if (sign_flag) goto loc_00C300AE;
    result = PiDmaGuardInitialize(1, 1 + 1, v_rsp - 200 + 112, v_rip + 2319302);
    if (sign_flag) goto loc_00C300AC;
    v_stack_m150 = 0;
    result = ext_ms_win_ntos_ksr_l1_1_5_dll_KsrGetFirmwareInformation(v_stack_m150, 1 + 1, v_rsp - 200 + 112, v_rip + 2319302);
    if (sign_flag) goto loc_00C3002A;
    *(unsigned __int8 *)(v_rip + 3516780) = 1;
    result = PiKsrNotifyInitialize(v_stack_m150, 1 + 1, v_rsp - 200 + 112, v_rip + 2319302);
    if (!sign_flag) goto loc_00C30031;
    goto loc_00C300AE;
loc_00C3002A:
    *(unsigned __int8 *)(v_rip + 3516759) = 0;
loc_00C30031:
    a4 = 0;
    v_stack_m198 = 0;
    a3 = 0;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = 0;
    result = PnpRequestDeviceAction(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3523584) + 32), a4 + 10, a3, a4);
    *(unsigned __int16 *)(v_rip + 3523959) = 0;
    *(unsigned __int64 *)(v_rip + 3523968) = v_rip + 3523975;
    *(unsigned __int64 *)(v_rip + 3523953) = v_rip + 3523975;
    *(unsigned __int8 *)(v_rip + 3523940) = 6;
    *(unsigned int *)(v_rip + 3523935) = 0;
    result = *(unsigned __int64 *)(v_stack_m150 + 240);
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m150 + 240) + 132)) & (0x400ULL)) == 0) {
        a2 = 1;
        a1 = v_stack_m150;
        result = PpInitializeBootDDB(a1, a2, a3, a4);
    }
    goto loc_00C300AC;
loc_00C300A7:
loc_00C300AC:
loc_00C300AE:
    a1 = (*(unsigned __int64 *)(v_rsp - 200 + 144)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopInitializePlugPlayServices(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m15C;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m16C;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint8_t v_stack_m188;
    uint32_t v_stack_m190;
    uint64_t v_stack_m198;
    uint32_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (416);
    result = (*(uint64_t *)(v_rip + 0x1DB47B)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0xC8 + 0x90) = result;
    local_r14 = 0;
    *(uint64_t *)(local_rsp - 0xC8 - 0x78) = 0;
    v_stack_m180 = 0;
    *(uint64_t *)(local_rsp - 0xC8 - 0x60) = 0;
    v_stack_m16C = 0;
    v_stack_m150 = 0;
    *(uint32_t *)(local_rsp - 0xC8 - 0x80) = 0;
    *(uint32_t *)(local_rsp - 0xC8 - 0x4) = 0;
    *(uint32_t *)(local_rsp - 0xC8 + 0x14) = 0;
    *(uint64_t *)(local_rsp - 0xC8 - 0x68) = 0;
    v_stack_m178 = 0;
    *(uint64_t *)(local_rsp - 0xC8 - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0xC8 - 0x50) = 0;
    v_stack_m158 = 0;
    *(uint32_t *)(local_rsp - 0xC8 - 0x44) = 0;
    *(uint32_t *)(local_rsp - 0xC8 - 0x34) = 0;
    v_stack_m188 = 0;
    *(uint64_t *)(local_rsp - 0xC8 - 0x18) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xC8 - 0x28) = v_xmm1;
    if (Arg2 != 0) goto loc_00C2FED9;
    *(uint8_t *)(v_rip + 0x35D041) = 0;
    *(uint32_t *)(v_rip + 0x236FAF) = 80;
    *(uint32_t *)(v_rip + 0x236FA9) = 90;
    result = CmRegisterSystemHiveLimitCallback(Arg1, Arg2, v_rip + 2322368, Arg4);
    *(uint8_t *)(v_rip + 0x236F8A) = 0;
    *(uint64_t *)(local_rsp - 0xC8 + 0x8) = v_rip + 3844745;
    *(uint32_t *)(local_rsp - 0xC8 - 0x8) = 48;
    v_stack_m198 = local_rsp - 200 - 128;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = 0;
    Arg4 = 0;
    *(uint64_t *)(local_rsp - 0xC8) = 0;
    *(uint32_t *)(local_rsp - 0xC8 + 0x10) = 576;
    *(uint64_t *)(local_rsp - 0xC8 + 0x18) = v_xmm0;
    result = ZwCreateKey(v_stack_m158, (uint32_t)((uint32_t)((uint32_t)(0xF003FULL))), local_rsp - 200 - 8, Arg4);
    if (sign_flag) goto loc_00C2F45C;
    Arg3 = 0;
    result = IopGetRegistryValue(v_stack_m158, v_rip + 305796, Arg3, local_rsp - 200 - 104);
    if (sign_flag) goto loc_00C2F452;
    if (*(uint64_t *)(local_rsp - 0xC8 - 0x68) == 0) goto loc_00C2F452;
    Arg3 = 0;
    result = IopGetRegistryValue(v_stack_m158, v_rip + 305806, Arg3, v_stack_m178);
    if (sign_flag) goto loc_00C2F448;
    if (v_stack_m178 != 0) {
        Arg2 = *(uint32_t *)(*(uint64_t *)(local_rsp - 0xC8 - 0x68) + 0x8);
        Arg1 = local_rsp - 200 - 24;
        Arg2 = (Arg2) + (*(uint64_t *)(local_rsp - 0xC8 - 0x68));
        result = RtlInitUnicodeString(Arg1, Arg2, Arg3, v_stack_m178);
        Arg2 = *(uint32_t *)(v_stack_m178 + 0x8);
        Arg1 = local_rsp - 200 - 40;
        Arg2 = (Arg2) + (v_stack_m178);
        result = RtlInitUnicodeString(Arg1, Arg2, Arg3, v_stack_m178);
        Arg4 = 0;
        v_stack_m1A8 = 0;
        Arg3 = 0x4000002CULL;
        Arg2 = local_rsp - 200 - 40;
        Arg1 = local_rsp - 200 - 24;
        result = PnpLogEvent(Arg1, Arg2, Arg3, Arg4);
        Arg2 = 0;
        Arg1 = v_stack_m178;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0xC8 - 0x68), Arg2, Arg3, Arg4);
loc_00C2F452:
    result = ZwClose(v_stack_m158, Arg2, Arg3, Arg4);
loc_00C2F45C:
    *(uint64_t *)(v_rip + 0x35CEDE) = 0;
    *(uint64_t *)(v_rip + 0x35CE97) = v_rip + 3526301;
    *(uint64_t *)(v_rip + 0x35CE85) = v_rip + 3526301;
    *(uint64_t *)(v_rip + 0x35CEAF) = v_rip + 3526318;
    *(uint64_t *)(v_rip + 0x35CEA0) = v_rip + 3526318;
    *(uint64_t *)(v_rip + 0x35CE82) = v_rip + 3526273;
    *(uint64_t *)(v_rip + 0x35CE73) = v_rip + 3526273;
    *(uint32_t *)(v_rip + 0x35CE64) = 0;
    *(uint8_t *)(v_rip + 0x35CE75) = 5;
    *(uint8_t *)(v_rip + 0x35CE70) = 8;
    *(uint32_t *)(v_rip + 0x35CE6B) = 0;
    *(uint32_t *)(v_rip + 0x35CE75) = 0x7FFFFFFFULL;
    result = PiInitFirmwareResources(Arg1, Arg2, Arg3, Arg4);
    result = *(uint64_t *)(arg1 + 0xF0);
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x84)) & (0x400ULL)) == 0) {
        Arg2 = 0;
        Arg1 = Arg1;
        result = PpInitializeBootDDB(Arg1, Arg2, Arg3, Arg4);
    }
    result = PipInitDeviceOverrideCache(Arg1, Arg2, Arg3, Arg4);
    *(uint16_t *)(v_rip + 0x35DABF) = 0;
    *(uint64_t *)(v_rip + 0x35DAC8) = v_rip + 3529423;
    *(uint64_t *)(v_rip + 0x35DAB9) = v_rip + 3529423;
    *(uint8_t *)(v_rip + 0x35DAAC) = 6;
    *(uint32_t *)(v_rip + 0x35DAA7) = 0;
    result = PiInitCacheGroupInformation(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00C300AE;
    *(uint8_t *)(v_rip + 0x35CE28) = 5;
    *(uint64_t *)(v_rip + 0x35CE2C) = v_rip + 3526199;
    *(uint64_t *)(v_rip + 0x35CE1D) = v_rip + 3526199;
    *(uint8_t *)(v_rip + 0x35CE02) = 8;
    *(uint32_t *)(v_rip + 0x35CDFE) = 1;
    *(uint32_t *)(v_rip + 0x35CE0C) = 1;
loc_00C2F56C:
    *(uint64_t *)(v_rip + 0x35CC07 + 0x8) = v_rip + 3525639;
    *(uint64_t *)(v_rip + 0x35CC07) = v_rip + 3525639;
    result = (v_rip + 3525639) + (16);
    if (result < (v_rip + 3525934)) goto loc_00C2F56C;
    result = IopInitializeResourceMap(Arg1, Arg2, Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x35CBA0) = v_rip + 19775;
    *(uint64_t *)(v_rip + 0x3D9119) = 0;
    *(uint32_t *)(v_rip + 0x1DB46F) = 1;
    result = ArbInitializeOsInaccessibleRange((uint32_t)(*(uint32_t *)(v_rip + 0x1FE6AE)), Arg2, Arg3, Arg4);
    result = ArbLibraryInitialize((uint32_t)(*(uint32_t *)(v_rip + 0x1FE6AE)), Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00C300AC;
    result = IopPortInitialize((uint32_t)(*(uint32_t *)(v_rip + 0x1FE6AE)), Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00C300AC;
    result = IopMemInitialize((uint32_t)(*(uint32_t *)(v_rip + 0x1FE6AE)), Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00C300AC;
    result = IopDmaInitialize((uint32_t)(*(uint32_t *)(v_rip + 0x1FE6AE)), Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00C300AC;
    result = IopIrqInitialize((uint32_t)(*(uint32_t *)(v_rip + 0x1FE6AE)), Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00C300AC;
    result = IopBusNumberInitialize((uint32_t)(*(uint32_t *)(v_rip + 0x1FE6AE)), Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00C300AC;
    Arg1 = 0;
    result = PiPnpRtlInit(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00C300AC;
    result = PipMigratePnpState(Arg1, Arg2, Arg3, Arg4);
    result = PiDmInit(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00C300AC;
    result = _PnpCtxGetCachedContextBaseKey(*(uint64_t *)(v_rip + 0x236D68), 4, local_rsp - 200 - 96, Arg4);
    if (sign_flag) goto loc_00C300AC;
    v_stack_m1A0 = 0;
    v_stack_m168 = v_rip + 305225;
    v_stack_m170 = 0x180016ULL;
    v_stack_m1A8 = 0;
    result = IopCreateRegistryKeyEx(v_stack_m180, *(uint64_t *)(local_rsp - 0xC8 - 0x60), v_stack_m170, (uint32_t)((uint32_t)((uint32_t)(0xF003FULL))));
    if (sign_flag) goto loc_00C2F7B1;
    Arg3 = 0;
    result = IopGetRegistryValue(v_stack_m180, v_rip + 305189, Arg3, local_rsp - 200 - 88);
    if (sign_flag) goto loc_00C2F6C7;
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xC8 - 0x58) + 0x4)) != 4) goto loc_00C2F6C0;
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xC8 - 0x58) + 0xC)) == 4) {
        result = *(uint32_t *)(*(uint64_t *)(local_rsp - 0xC8 - 0x58) + 0x8);
        Arg2 = *(uint32_t *)(result + *(uint64_t *)(local_rsp - 0xC8 - 0x58) * 1);
        *(uint32_t *)(v_rip + 0x1DB31C) = Arg2;
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0xC8 - 0x58), Arg2, Arg3, local_rsp - 200 - 88);
loc_00C2F6C7:
    Arg3 = 0;
    result = IopGetRegistryValue(v_stack_m180, v_rip + 305318, Arg3, local_rsp - 200 - 80);
    if (sign_flag) goto loc_00C2F706;
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xC8 - 0x50) + 0x4)) != 4) goto loc_00C2F6FF;
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0xC8 - 0x50) + 0xC)) == 4) {
        result = *(uint32_t *)(*(uint64_t *)(local_rsp - 0xC8 - 0x50) + 0x8);
        Arg2 = *(uint32_t *)(result + *(uint64_t *)(local_rsp - 0xC8 - 0x50) * 1);
        *(uint32_t *)(v_rip + 0x1DB2E5) = Arg2;
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0xC8 - 0x50), Arg2, Arg3, local_rsp - 200 - 80);
loc_00C2F706:
    v_stack_m160 = 0;
    result = PnpGetRegistryDword(v_stack_m180, v_rip + 309273, v_stack_m160, local_rsp - 200 - 80);
    if (sign_flag) goto loc_00C2F732;
    if (v_stack_m160 == 1) {
        *(uint8_t *)(v_rip + 0x35BCD6) = 1;
    }
    result = PiUEventProcessRegistry(v_stack_m180, v_rip + 309273, v_stack_m160, local_rsp - 200 - 80);
    v_stack_m15C = 0;
    result = PnpGetRegistryDword(v_stack_m180, v_rip + 308515, v_stack_m15C, local_rsp - 200 - 80);
    if (sign_flag) goto loc_00C2F77A;
    if (((uint32_t)((uint32_t)(v_stack_m15C))) < 100) goto loc_00C2F771;
    if (((uint32_t)((uint32_t)(v_stack_m15C))) <= ((uint32_t)((uint32_t)(0xEA60ULL)))) goto loc_00C2F77F;
loc_00C2F771:
    *(uint16_t *)(v_rip + 0x1DB270) = (uint16_t)((uint32_t)(0xEA60ULL));
    goto loc_00C2F786;
loc_00C2F77A:
loc_00C2F77F:
    *(uint16_t *)(v_rip + 0x1DB262) = (uint16_t)((uint32_t)(0x1388ULL));
loc_00C2F786:
    *(uint64_t *)(v_rip + 0x35D7F7) = v_rip - 5292114;
    *(uint64_t *)(v_rip + 0x35D7F8) = v_stack_m180;
    *(uint64_t *)(v_rip + 0x35D7D9) = 0;
    result = PipUpdateAsyncOptionsCallback(v_stack_m180, v_rip + 308515, v_stack_m15C, local_rsp - 200 - 80);
    v_stack_m180 = 0;
loc_00C2F7B1:
    v_stack_m170 = 0x3E003CULL;
    v_stack_m168 = v_rip + 305160;
    Arg2 = 0;
    result = IopOpenRegistryKeyEx(v_stack_m180, Arg2, v_stack_m170, (uint32_t)(0x20019ULL));
    if (sign_flag) goto loc_00C2F8C3;
    result = PipUpdateSetupInProgress(v_stack_m180, Arg2, v_stack_m170, (uint32_t)(0x20019ULL));
    Arg3 = 0;
    result = IopGetRegistryValue(v_stack_m180, v_rip + 305150, Arg3, v_stack_m178);
    if (sign_flag) goto loc_00C2F833;
    if ((*(uint32_t *)(v_stack_m178 + 0x4)) != 4) goto loc_00C2F82C;
    if ((*(uint32_t *)(v_stack_m178 + 0xC)) != 4) goto loc_00C2F82C;
    if ((*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m178 + 0x8)) + v_stack_m178 * 1)) != 0) {
        *(uint8_t *)(v_rip + 0x236A4E) = 1;
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m178, Arg2, Arg3, v_stack_m178);
loc_00C2F833:
    Arg3 = 0;
    result = IopGetRegistryValue(v_stack_m180, v_rip + 305097, Arg3, v_stack_m178);
    if (sign_flag) goto loc_00C2F878;
    if ((*(uint32_t *)(v_stack_m178 + 0x4)) != 4) goto loc_00C2F871;
    if ((*(uint32_t *)(v_stack_m178 + 0xC)) != 4) goto loc_00C2F871;
    if ((*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m178 + 0x8)) + v_stack_m178 * 1)) != 0) {
        *(uint8_t *)(v_rip + 0x236A07) = 1;
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m178, Arg2, Arg3, v_stack_m178);
loc_00C2F878:
    if ((*(uint8_t *)(v_rip + 0x2369C6)) != 0) goto loc_00C2F896;
    if ((*(uint8_t *)(v_rip + 0x2369F1)) != 0) goto loc_00C2F896;
    result = ZwClose(v_stack_m180, Arg2, Arg3, v_stack_m178);
    goto loc_00C2F8BE;
loc_00C2F896:
    Arg2 = 0;
    *(uint64_t *)(v_rip + 0x35D6A5) = v_rip - 5291938;
    *(uint64_t *)(v_rip + 0x35D6A6) = v_stack_m180;
    *(uint64_t *)(v_rip + 0x35D687) = 0;
    result = PipUpdateSetupInProgressNotify(v_stack_m180, Arg2, Arg3, v_stack_m178);
loc_00C2F8BE:
    v_stack_m180 = 0;
loc_00C2F8C3:
    Arg1 = (*(uint64_t *)(arg1 + 0xF0)) + (0xA08ULL);
    result = PipHardwareConfigInit(Arg1, Arg2, Arg3, v_stack_m178);
    if (sign_flag) goto loc_00C300AC;
    result = PipCheckSystemFirmwareUpdated(v_stack_m188, Arg2, Arg3, v_stack_m178);
    Arg1 = 0;
    result = PiDcInit(Arg1, Arg2, Arg3, v_stack_m178);
    if (sign_flag) goto loc_00C300AC;
    Arg2 = 0;
    result = memset(local_rsp - 200 + 48, Arg2, Arg2 + 64, v_stack_m178);
    result = PiAuCreateUserSids(local_rsp - 200 + 48, Arg2, Arg2 + 64, v_stack_m178);
    if (sign_flag) goto loc_00C2F933;
    result = PiAuCreateStandardSecurityObject(local_rsp - 200 + 48, Arg2, Arg2 + 64, v_stack_m178);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        Arg1 = local_rsp - 200 + 48;
        result = PiAuCreateLocalSystemSecurityObject(Arg1, Arg2, Arg2 + 64, v_stack_m178);
        local_rbx = (uint32_t)(result);
    }
    result = PiAuFreeUserSids(local_rsp - 200 + 48, Arg2, Arg2 + 64, v_stack_m178);
    if (sign_flag) goto loc_00C300AC;
    result = PiDqInit(local_rsp - 200 + 48, Arg2, Arg2 + 64, v_stack_m178);
    if (sign_flag) goto loc_00C300AC;
    result = PpDevCfgInit(local_rsp - 200 + 48, Arg2, Arg2 + 64, v_stack_m178);
    if (sign_flag) goto loc_00C300AC;
    result = PipResetDevices(local_rsp - 200 + 48, Arg2, Arg2 + 64, v_stack_m178);
    v_stack_m1A0 = 0;
    v_stack_m1A8 = 0;
    result = CmCreateDevice(*(uint64_t *)(v_rip + 0x236A2A), v_rip + 304479, (uint32_t)((uint32_t)((uint32_t)(0xF003FULL))), local_rsp - 200 - 120);
    if (sign_flag) goto loc_00C300AC;
    v_stack_m190 = 0;
    v_stack_m198 = 78;
    v_stack_m1A0 = v_rip + 304477;
    v_stack_m1A8 = 1;
    result = CmSetDeviceRegProp(*(uint64_t *)(v_rip + 0x2369EE), v_rip + 304479, *(uint64_t *)(local_rsp - 0xC8 - 0x78), 37);
    v_stack_m190 = 0;
    v_stack_m198 = 4;
    v_stack_m1A0 = local_rsp - 200 - 124;
    v_stack_m1A8 = 4;
    *(uint32_t *)(local_rsp - 0xC8 - 0x7C) = 0;
    result = CmSetDeviceRegProp(*(uint64_t *)(v_rip + 0x2369C0), v_rip + 304479, *(uint64_t *)(local_rsp - 0xC8 - 0x78), 11);
    result = ZwClose(*(uint64_t *)(local_rsp - 0xC8 - 0x78), v_rip + 304479, *(uint64_t *)(local_rsp - 0xC8 - 0x78), 11);
    local_rbx = (uint32_t)((*(uint64_t *)(local_rsp - 0xC8 - 0x78)) | (0xFFFFFFFFULL));
    *(uint64_t *)(v_rip + 0x35CA3A) = v_rip + 3525180;
    *(uint64_t *)(v_rip + 0x35CA24) = v_rip + 3525180;
    *(uint64_t *)(v_rip + 0x35CB1C) = v_rip + 3525403;
    *(uint64_t *)(v_rip + 0x35CB0D) = v_rip + 3525403;
    result = ExInitializeResourceLite2(v_rip + 3525435, (uint32_t)((uint32_t)(local_rbx)), *(uint64_t *)(local_rsp - 0xC8 - 0x78), 11);
    result = ExInitializeResourceLite2(v_rip + 3525135, (uint32_t)((uint32_t)(local_rbx)), *(uint64_t *)(local_rsp - 0xC8 - 0x78), 11);
    result = ExInitializeResourceLite2(v_rip + 3525249, (uint32_t)((uint32_t)(local_rbx)), *(uint64_t *)(local_rsp - 0xC8 - 0x78), 11);
    *(uint64_t *)(v_rip + 0x35B31E) = 0;
    *(uint64_t *)(v_rip + 0x35C98F) = v_rip + 3525013;
    *(uint64_t *)(v_rip + 0x35C979) = v_rip + 3525013;
    *(uint32_t *)(v_rip + 0x35C94A) = 1;
    *(uint64_t *)(v_rip + 0x35C92B) = v_rip + 3524912;
    *(uint64_t *)(v_rip + 0x35C91C) = v_rip + 3524912;
    *(uint64_t *)(v_rip + 0x35C93D) = 0;
    *(uint32_t *)(v_rip + 0x35C93E) = 0;
    *(uint16_t *)(v_rip + 0x35C93F) = 1;
    *(uint8_t *)(v_rip + 0x35C93A) = 6;
    *(uint32_t *)(v_rip + 0x35C935) = 0;
    *(uint32_t *)(v_rip + 0x35C8D3) = 1;
    *(uint64_t *)(v_rip + 0x35C8D4) = 0;
    *(uint32_t *)(v_rip + 0x35C8D5) = 0;
    *(uint16_t *)(v_rip + 0x35C8D6) = 1;
    *(uint8_t *)(v_rip + 0x35C8D1) = 6;
    *(uint32_t *)(v_rip + 0x35C8CC) = 0;
    result = ExInitializeResourceLite2(v_rip + 3527712, (uint32_t)((uint32_t)(local_rbx)), *(uint64_t *)(local_rsp - 0xC8 - 0x78), 11);
    *(uint64_t *)(v_rip + 0x35D409) = 0;
    result = PnpAcquireDependencyRelationsLock(1, (uint32_t)((uint32_t)(local_rbx)), *(uint64_t *)(local_rsp - 0xC8 - 0x78), 11);
    *(uint64_t *)(v_rip + 0x35D376) = v_rip + 3527541;
    *(uint64_t *)(v_rip + 0x35D367) = v_rip + 3527541;
    *(uint64_t *)(v_rip + 0x35D351) = v_rip + 3527504;
    *(uint64_t *)(v_rip + 0x35D342) = v_rip + 3527504;
    *(uint64_t *)(v_rip + 0x35D32C) = v_rip + 3527467;
    *(uint64_t *)(v_rip + 0x35D31D) = v_rip + 3527467;
    result = PnpReleaseDependencyRelationsLock(1, (uint32_t)((uint32_t)(local_rbx)), *(uint64_t *)(local_rsp - 0xC8 - 0x78), 11);
    *(uint8_t *)(v_rip + 0x35B1E7) = 0;
    *(uint16_t *)(v_rip + 0x35B1FF) = 0;
    *(uint8_t *)(v_rip + 0x35B1FA) = 6;
    *(uint32_t *)(v_rip + 0x35B1F6) = 1;
    *(uint32_t *)(v_rip + 0x35B125) = 1;
    *(uint64_t *)(v_rip + 0x35B1EE) = v_rip + 3518963;
    *(uint64_t *)(v_rip + 0x35B1D8) = v_rip + 3518963;
    *(uint64_t *)(v_rip + 0x35B105) = 0;
    *(uint64_t *)(v_rip + 0x35B1DE) = v_rip + 3518948;
    *(uint64_t *)(v_rip + 0x35B1CF) = v_rip + 3518948;
    *(uint64_t *)(v_rip + 0x35B129) = v_rip + 3518760;
    *(uint64_t *)(v_rip + 0x35B11A) = v_rip + 3518760;
    *(uint64_t *)(v_rip + 0x35B0F4) = v_rip + 3518707;
    *(uint64_t *)(v_rip + 0x35B0E5) = v_rip + 3518707;
    *(uint64_t *)(v_rip + 0x35B127) = v_rip + 3518758;
    *(uint64_t *)(v_rip + 0x35B118) = v_rip + 3518758;
    *(uint64_t *)(v_rip + 0x35C832) = v_rip + 3524657;
    *(uint64_t *)(v_rip + 0x35C823) = v_rip + 3524657;
    v_stack_m168 = v_rip + 303940;
    *(uint32_t *)(v_rip + 0x35B098) = 0;
    *(uint16_t *)(v_rip + 0x35B099) = 1;
    *(uint8_t *)(v_rip + 0x35B094) = 6;
    *(uint32_t *)(v_rip + 0x35B08F) = 0;
    *(uint32_t *)(v_rip + 0x35B0A4) = 0;
    *(uint8_t *)(v_rip + 0x35B0C5) = 5;
    *(uint8_t *)(v_rip + 0x35B0C0) = 8;
    *(uint32_t *)(v_rip + 0x35B0BC) = 1;
    *(uint32_t *)(v_rip + 0x35B0CA) = 1;
    *(uint64_t *)(v_rip + 0x35C7C3) = 0;
    *(uint16_t *)(v_rip + 0x35C7C4) = 1;
    *(uint8_t *)(v_rip + 0x35C7BF) = 6;
    *(uint32_t *)(v_rip + 0x35C7BB) = 1;
    v_stack_m170 = 0x260024ULL;
    result = IoCreateDriver(v_stack_m170, v_rip + 22951, *(uint64_t *)(local_rsp - 0xC8 - 0x78), 11);
    if (sign_flag) goto loc_00C300AC;
    v_stack_m198 = v_stack_m150;
    v_stack_m1A0 = 0;
    Arg3 = 0;
    Arg2 = 0;
    v_stack_m1A8 = 0;
    result = IoCreateDevice(*(uint64_t *)(v_rip + 0x35C7B9), Arg2, Arg3, 4);
    if (sign_flag) goto loc_00C300AC;
    result = PipAllocateDeviceNode(v_stack_m150, v_rip + 3524474, Arg3, 4);
    if (*(uint64_t *)(v_rip + 0x35C766) != 0) goto loc_00C2FCFA;
    result = IoDeleteDevice(v_stack_m150, v_rip + 3524474, Arg3, 4);
    result = IoDeleteDriver(*(uint64_t *)(v_rip + 0x35C758), v_rip + 3524474, Arg3, 4);
    if (sign_flag) goto loc_00C300AC;
    goto loc_00C2FDB9;
loc_00C2FCFA:
    result = PipSetDevNodeFlags(*(uint64_t *)(v_rip + 0x35C758), 305, Arg3, 4);
    result = PipSetDevNodeUserFlags(*(uint64_t *)(v_rip + 0x35C72D), 10, Arg3, 4);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x35C71C) + 0x294) = 0xFFFFFFFEULL;
    result = PnpAllocateDeviceInstancePath(*(uint64_t *)(v_rip + 0x35C706), 26, Arg3, 4);
    if (sign_flag) goto loc_00C300AC;
    *(uint32_t *)(local_rsp - 0xC8 - 0x48) = 0x1A0018ULL;
    *(uint64_t *)(local_rsp - 0xC8 - 0x40) = v_rip + 304479;
    result = PnpCopyDeviceInstancePath(*(uint64_t *)(v_rip + 0x35C6F0), local_rsp - 200 - 72, Arg3, 4);
    result = PnpMapDeviceObjectToDeviceInstance(*(uint64_t *)(*(uint64_t *)(v_rip + 0x35C6D5) + 0x20), *(uint64_t *)(v_rip + 0x35C6D5) + 40, Arg3, 4);
    if (sign_flag) goto loc_00C300AC;
    Arg2 = (*(uint64_t *)(v_rip + 0x35C6B7)) + (664);
    *(uint32_t *)(local_rsp - 0xC8 - 0x38) = 0x4E004CULL;
    *(uint64_t *)(local_rsp - 0xC8 - 0x30) = v_rip + 304477;
    result = RtlGUIDFromString(local_rsp - 200 - 56, Arg2, Arg3, 4);
    result = PnpQueryAndSaveDeviceNodeCapabilities(*(uint64_t *)(v_rip + 0x35C695), Arg2, Arg3, 4);
    result = PipSetDevNodeState(*(uint64_t *)(v_rip + 0x35C689), 778, Arg3, 4);
loc_00C2FDB9:
    v_stack_m1A8 = 0;
    result = CmAddDeviceToContainer(*(uint64_t *)(v_rip + 0x2365D8), v_rip + 304477, v_rip + 304477, v_rip + 304479);
    if (sign_flag) goto loc_00C300AC;
    if (v_stack_m188 != 0) {
        result = PiDcHandleSystemFirmwareUpdate(*(uint64_t *)(v_rip + 0x2365D8), v_rip + 304477, v_rip + 304477, v_rip + 304479);
    }
    result = PnpInitializePnpWatchdogs(*(uint64_t *)(v_rip + 0x2365D8), v_rip + 304477, v_rip + 304477, v_rip + 304479);
    result = PnpInitializeDeviceEvents(*(uint64_t *)(v_rip + 0x2365D8), v_rip + 304477, v_rip + 304477, v_rip + 304479);
    if (sign_flag) goto loc_00C300AC;
    result = PnpInitializeNotification(*(uint64_t *)(v_rip + 0x2365D8), v_rip + 304477, v_rip + 304477, v_rip + 304479);
    result = PnpBusTypeGuidInitialize(*(uint64_t *)(v_rip + 0x2365D8), v_rip + 304477, v_rip + 304477, v_rip + 304479);
    if (sign_flag) goto loc_00C300AC;
    *(uint16_t *)(v_rip + 0x35AE01) = 1;
    *(uint64_t *)(v_rip + 0x35AE0A) = v_rip + 3517968;
    *(uint64_t *)(v_rip + 0x35ADFB) = v_rip + 3517968;
    *(uint8_t *)(v_rip + 0x35ADEE) = 6;
    *(uint32_t *)(v_rip + 0x35ADEA) = 1;
    result = PiSwInit(*(uint64_t *)(v_rip + 0x2365D8), v_rip + 304477, v_rip + 304477, v_rip + 304479);
    if (sign_flag) goto loc_00C300AC;
    Arg1 = 0;
    result = PiUEventInit(Arg1, v_rip + 304477, v_rip + 304477, v_rip + 304479);
    if (sign_flag) goto loc_00C300AC;
    *(uint64_t *)(local_rsp - 0xC8 - 0x78) = 0x240022ULL;
    *(uint64_t *)(local_rsp - 0xC8 - 0x70) = v_rip + 307663;
    result = IoCreateDriver(local_rsp - 200 - 120, v_rip + 22896, v_rip + 304477, v_rip + 304479);
    if (sign_flag) goto loc_00C300AC;
    Arg1 = 0;
    result = PiDmaGuardInitialize(Arg1, v_rip + 22896, v_rip + 304477, v_rip + 304479);
    if (sign_flag) goto loc_00C300AC;
    result = IoInvalidateInit(Arg1, v_rip + 22896, v_rip + 304477, v_rip + 304479);
    result = PipProcessPendingServices(Arg1, v_rip + 22896, v_rip + 304477, v_rip + 304479);
    if (!(sign_flag)) {
        result = PipProcessPendingOsExtensionResources(Arg1, v_rip + 22896, v_rip + 304477, v_rip + 304479);
    }
    Arg4 = 0;
    v_stack_m198 = 0;
    Arg3 = 0;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = 0;
    result = PnpRequestDeviceAction(*(uint64_t *)(*(uint64_t *)(v_rip + 0x35C586) + 0x20), Arg4 + 10, Arg3, Arg4);
    goto loc_00C300AC;
loc_00C2FED9:
    if (((uint32_t)(Arg4 + 10)) != 1) goto loc_00C300A7;
    result = McGenEventRegister_EtwRegister(v_rip - 12620007, Arg4 + 10, v_rip + 1928883, v_rip + 1928883);
    *(uint64_t *)(v_rip + 0x2363C5) = *(uint64_t *)(v_rip + 0x1D6E9D);
    local_rbx = 0;
    if (sign_flag) { local_rbx = (uint32_t)(result); }
    Arg3 = 0;
    result = EtwRegister(v_rip - 12620279, v_rip - 1960061, Arg3, v_rip + 2319302);
    if (sign_flag) goto loc_00C300AE;
    if (sign_flag) goto loc_00C300AE;
    result = TlgRegisterAggregateProvider(v_rip + 1929288, v_rip - 1960061, Arg3, v_rip + 2319302);
    result = TlgRegisterAggregateProvider(v_rip + 1929220, v_rip - 1960061, Arg3, v_rip + 2319302);
    Arg3 = 0;
    Arg2 = 0;
    result = TraceLoggingRegisterEx_EtwRegister_EtwSetInformation(v_rip + 1929317, Arg2, Arg3, v_rip + 2319302);
    result = PiDcInit(1, Arg2, Arg3, v_rip + 2319302);
    if (sign_flag) goto loc_00C300AE;
    result = PiUEventInit(1, Arg2, Arg3, v_rip + 2319302);
    if (sign_flag) goto loc_00C300AE;
    *(uint64_t *)(local_rsp - 0xC8 + 0x78) = 80;
    *(uint64_t *)(local_rsp - 0xC8 + 0x88) = 8;
    *(uint64_t *)(local_rsp - 0xC8 + 0x70) = *(uint64_t *)(v_stack_m150 + 0xF0) + 136;
    *(uint64_t *)(local_rsp - 0xC8 + 0x80) = *(uint64_t *)(v_stack_m150 + 0xF0) + 3864;
    result = PnpDiagnosticTrace(v_rip - 12618322, 1 + 1, local_rsp - 200 + 112, v_rip + 2319302);
    result = PiPnpRtlInit(1, 1 + 1, local_rsp - 200 + 112, v_rip + 2319302);
    if (sign_flag) goto loc_00C300AE;
    result = PiCslInitialize(1, 1 + 1, local_rsp - 200 + 112, v_rip + 2319302);
    if (sign_flag) goto loc_00C300AE;
    result = PiDmaGuardInitialize(1, 1 + 1, local_rsp - 200 + 112, v_rip + 2319302);
    if (sign_flag) goto loc_00C300AC;
    v_stack_m150 = 0;
    result = kernel_indirect_call(v_stack_m150, 1 + 1, local_rsp - 200 + 112, v_rip + 2319302);
    if (sign_flag) goto loc_00C3002A;
    *(uint8_t *)(v_rip + 0x35A96C) = 1;
    result = PiKsrNotifyInitialize(v_stack_m150, 1 + 1, local_rsp - 200 + 112, v_rip + 2319302);
    if (!sign_flag) goto loc_00C30031;
    goto loc_00C300AE;
loc_00C3002A:
    *(uint8_t *)(v_rip + 0x35A957) = 0;
loc_00C30031:
    Arg4 = 0;
    v_stack_m198 = 0;
    Arg3 = 0;
    v_stack_m1A0 = 0;
    v_stack_m1A8 = 0;
    result = PnpRequestDeviceAction(*(uint64_t *)(*(uint64_t *)(v_rip + 0x35C400) + 0x20), Arg4 + 10, Arg3, Arg4);
    *(uint16_t *)(v_rip + 0x35C577) = 0;
    *(uint64_t *)(v_rip + 0x35C580) = v_rip + 3523975;
    *(uint64_t *)(v_rip + 0x35C571) = v_rip + 3523975;
    *(uint8_t *)(v_rip + 0x35C564) = 6;
    *(uint32_t *)(v_rip + 0x35C55F) = 0;
    result = *(uint64_t *)(v_stack_m150 + 0xF0);
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m150 + 0xF0) + 0x84)) & (0x400ULL)) == 0) {
        Arg2 = 1;
        Arg1 = v_stack_m150;
        result = PpInitializeBootDDB(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_00C300AC;
loc_00C300A7:
loc_00C300AC:
loc_00C300AE:
    Arg1 = (*(uint64_t *)(local_rsp - 0xC8 + 0x90)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xF0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C2F298&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
