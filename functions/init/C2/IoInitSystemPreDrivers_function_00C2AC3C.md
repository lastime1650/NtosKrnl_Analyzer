# IoInitSystemPreDrivers

- RVA: `0x00C2AC3C`–`0x00C2BF13` (길이 `4,823` bytes)
- VA: `0x0000000140C2AC3C`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C6434`
- 디코드: `996`개 명령, `4,823/4,823` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **142**; 고유 호출 대상: **92**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **246**

### Outgoing calls
- `0x00C2ACD4` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x00C2ACE2` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x00C2ACF0` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x00C2ACFE` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x00C2AD0C` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x00C2AEB7` → [IopQueryProcessorInitValues](../../page/71/IopQueryProcessorInitValues_function_0071AB80.md) (function, `0x0071AB80`)
- `0x00C2AEED` → [ExInitializeSystemLookasideList](../../pagelk/B7/ExInitializeSystemLookasideList_function_00B7E57C.md) (function, `0x00B7E57C`)
- `0x00C2AF14` → [ExInitializeSystemLookasideList](../../pagelk/B7/ExInitializeSystemLookasideList_function_00B7E57C.md) (function, `0x00B7E57C`)
- `0x00C2AF3B` → [ExInitializeSystemLookasideList](../../pagelk/B7/ExInitializeSystemLookasideList_function_00B7E57C.md) (function, `0x00B7E57C`)
- `0x00C2AF62` → [ExInitializeSystemLookasideList](../../pagelk/B7/ExInitializeSystemLookasideList_function_00B7E57C.md) (function, `0x00B7E57C`)
- `0x00C2AF89` → [ExInitializeSystemLookasideList](../../pagelk/B7/ExInitializeSystemLookasideList_function_00B7E57C.md) (function, `0x00B7E57C`)
- `0x00C2AFC0` → [ExInitializeNPagedLookasideListInternal](../../text/46/ExInitializeNPagedLookasideListInternal_function_00468720.md) (function, `0x00468720`)
- `0x00C2AFDA` → [FsRtlInitExtraCreateParameterLookasideList](../../page/71/FsRtlInitExtraCreateParameterLookasideList_function_00713910.md) (function, `0x00713910`)
- `0x00C2B00A` → [ExInitializeNPagedLookasideListInternal](../../text/46/ExInitializeNPagedLookasideListInternal_function_00468720.md) (function, `0x00468720`)
- `0x00C2B014` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (function, `0x00249EF0`)
- `0x00C2B036` → [IoInitializeProcessor](../../page/71/IoInitializeProcessor_function_0071A91C.md) (function, `0x0071A91C`)
- `0x00C2B066` → [IopInitializeReserveIrps](IopInitializeReserveIrps_function_00C2CDD0.md) (function, `0x00C2CDD0`)
- `0x00C2B131` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x00C2B145` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C2B16F` → [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) (function, `0x008B2A00`)
- `0x00C2B19B` → [ObCloseHandle](../../page/8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00C2B32D` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C2B36D` → [NtCreateEvent](../../page/8B/NtCreateEvent_function_008B9140.md) (function, `0x008B9140`)
- `0x00C2B37C` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2B3B7` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00C2B452` → [ObCloseHandle](../../page/8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00C2B457` → [IopCreateRootDirectories](IopCreateRootDirectories_function_00C2C728.md) (function, `0x00C2C728`)
- `0x00C2B464` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2B478` → [IopInitializeSessionNotifications](IopInitializeSessionNotifications_function_00C2E248.md) (function, `0x00C2E248`)
- `0x00C2B495` → [IopInitializePlugPlayServices](IopInitializePlugPlayServices_function_00C2F298.md) (function, `0x00C2F298`)
- `0x00C2B4A5` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2B4C0` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (function, `0x007D6800`)
- `0x00C2B4CA` → [KseInitialize](../C3/KseInitialize_function_00C3B5AC.md) (function, `0x00C3B5AC`)
- `0x00C2B4CF` → [PoInitDriverServices](../C3/PoInitDriverServices_function_00C3D08C.md) (function, `0x00C3D08C`)
- `0x00C2B4DB` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C2B51A` → [PipSetDevNodeFlags](../../page/8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00C2B524` → [WMIInitialize](../C4/WMIInitialize_function_00C4D264.md) (function, `0x00C4D264`)
- `0x00C2B549` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (function, `0x007D6800`)
- `0x00C2B54E` → [CmIsStateSeparationDevModeEnabled](../../page/7D/CmIsStateSeparationDevModeEnabled_function_007DF1D8.md) (function, `0x007DF1D8`)
- `0x00C2B555` → [RtlIsStateSeparationEnabled](../../page/A3/RtlIsStateSeparationEnabled_function_00A3C560.md) (function, `0x00A3C560`)
- `0x00C2B55E` → `ext-ms-win-ntos-stateseparation-l1-1-0.dll!ExpInitializeStateSeparationPhase0` (import, 간접 대상; import `ext-ms-win-ntos-stateseparation-l1-1-0.dll!ExpInitializeStateSeparationPhase0`)
- `0x00C2B596` → [RtlGetNtProductType](../../text/43/RtlGetNtProductType_function_00436270.md) (function, `0x00436270`)
- `0x00C2B5BD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C2B5DE` → [AstInitializeBloomFilter](../../page/72/AstInitializeBloomFilter_function_00722E34.md) (function, `0x00722E34`)
- `0x00C2B5F2` → [EtwInitialize](../../page/7B/EtwInitialize_function_007B4D40.md) (function, `0x007B4D40`)
- `0x00C2B60F` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (function, `0x00920960`)
- `0x00C2B63D` → [McGenEventRegister_EtwRegister](../../text/57/McGenEventRegister_EtwRegister_function_0057EF04.md) (function, `0x0057EF04`)
- `0x00C2B669` → [TlgRegisterAggregateProviderEx](../../page/AD/TlgRegisterAggregateProviderEx_function_00ADBA94.md) (function, `0x00ADBA94`)
- `0x00C2B69A` → [MiLogBadMapper](../../text/2F/MiLogBadMapper_function_002F1140.md) (function, `0x002F1140`)
- `0x00C2B6B7` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (function, `0x00920960`)
- `0x00C2B6C8` → [TraceLoggingRegisterEx_EtwRegister_EtwSetInformation](../../page/92/TraceLoggingRegisterEx_EtwRegister_EtwSetInformation_function_009208A0.md) (function, `0x009208A0`)
- `0x00C2B6D0` → [IopInitializeDumpPolicySettings](../../page/71/IopInitializeDumpPolicySettings_function_0071A444.md) (function, `0x0071A444`)
- `0x00C2B6DC` → [TlgRegisterAggregateProvider](../../page/70/TlgRegisterAggregateProvider_function_0070526C.md) (function, `0x0070526C`)
- `0x00C2B6EF` → [SeAuditBootConfiguration](../../page/79/SeAuditBootConfiguration_function_0079E374.md) (function, `0x0079E374`)
- `0x00C2B6F7` → [BootApplicationPersistentDataProcess](../BE/BootApplicationPersistentDataProcess_function_00BEEBD4.md) (function, `0x00BEEBD4`)
- `0x00C2B708` → `kdcom.dll!KdInitialize` (import, 간접 대상; import `kdcom.dll!KdInitialize`)
- `0x00C2B719` → [KeInitSystem](../C7/KeInitSystem_function_00C71660.md) (function, `0x00C71660`)
- `0x00C2B72E` → [KeAcquireSpinLockRaiseToDpc](../../text/20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x00C2B774` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00C2B782` → [KeReleaseSpinLock](../../text/39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x00C2B794` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (function, `0x007D6800`)
- `0x00C2B7B8` → [McTemplateK0q_EtwWriteTransfer](../../text/59/McTemplateK0q_EtwWriteTransfer_function_00596B68.md) (function, `0x00596B68`)
- `0x00C2B7C2` → [WheaInitialize](../C5/WheaInitialize_function_00C54C08.md) (function, `0x00C54C08`)
- `0x00C2B7DE` → [McTemplateK0_EtwWriteTransfer](../../text/59/McTemplateK0_EtwWriteTransfer_function_00596B24.md) (function, `0x00596B24`)
- `0x00C2B7F0` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (function, `0x007D6800`)
- `0x00C2B7F8` → [IopStoreArcInformation](IopStoreArcInformation_function_00C2D3C4.md) (function, `0x00C2D3C4`)
- `0x00C2B816` → [IopInitializePlugPlayServices](IopInitializePlugPlayServices_function_00C2F298.md) (function, `0x00C2F298`)
- `0x00C2B826` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2B84A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C2B8CE` → [KitpInitAitSampleRate](../C5/KitpInitAitSampleRate_function_00C53FC8.md) (function, `0x00C53FC8`)
- `0x00C2B8E6` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (function, `0x00920960`)
- `0x00C2B8FC` → [KseInitialize](../C3/KseInitialize_function_00C3B5AC.md) (function, `0x00C3B5AC`)
- `0x00C2B904` → [HvlPhase2Initialize](../../text/58/HvlPhase2Initialize_function_00583EA0.md) (function, `0x00583EA0`)
- `0x00C2B929` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (function, `0x007D6800`)
- `0x00C2B930` → [KeOptimizeSpecCtrlSettings](../../text/5B/KeOptimizeSpecCtrlSettings_function_005BE95C.md) (function, `0x005BE95C`)
- `0x00C2B935` → [PsInitializeSyscallProviders](../C4/PsInitializeSyscallProviders_function_00C44BA4.md) (function, `0x00C44BA4`)
- `0x00C2B93A` → [VslpIumPhase4Initialize](../../text/58/VslpIumPhase4Initialize_function_0058FAE0.md) (function, `0x0058FAE0`)
- `0x00C2B944` → [BootApplicationPersistentDataProcess](../BE/BootApplicationPersistentDataProcess_function_00BEEBD4.md) (function, `0x00BEEBD4`)
- `0x00C2B94C` → [BapdRecordFirmwareBootStats](../../pagelk/B7/BapdRecordFirmwareBootStats_function_00B72474.md) (function, `0x00B72474`)
- `0x00C2B95B` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (function, `0x007D6800`)
- `0x00C2B982` → [EtwWriteStartScenario](../../page/AB/EtwWriteStartScenario_function_00AB75B0.md) (function, `0x00AB75B0`)
- `0x00C2B9C6` → [IopQueryPassiveInterruptRegistryOptions](../../page/72/IopQueryPassiveInterruptRegistryOptions_function_0072BBB4.md) (function, `0x0072BBB4`)
- `0x00C2B9F5` → [KeInitializeQueue](../../text/48/KeInitializeQueue_function_00480C90.md) (function, `0x00480C90`)
- `0x00C2B9FA` → [IopCreatePassiveInterruptRealtimeThreads](../../page/72/IopCreatePassiveInterruptRealtimeThreads_function_0072BA98.md) (function, `0x0072BA98`)
- `0x00C2BA17` → [SecureDump_PrepareForInit](../../text/5A/SecureDump_PrepareForInit_function_005A317C.md) (function, `0x005A317C`)
- `0x00C2BA35` → [IopInitDumpCapsuleSupport](../../text/59/IopInitDumpCapsuleSupport_function_0059578C.md) (function, `0x0059578C`)
- `0x00C2BA50` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (function, `0x007D6800`)
- `0x00C2BA5F` → [EtwTraceLeapSecondDataParseFailure](../../page/7B/EtwTraceLeapSecondDataParseFailure_function_007B7F70.md) (function, `0x007B7F70`)
- `0x00C2BA78` → [EtwTraceLeapSecondDataUpdate](../../page/7B/EtwTraceLeapSecondDataUpdate_function_007B8050.md) (function, `0x007B8050`)
- `0x00C2BABA` → [ExRegisterHost](../../page/7D/ExRegisterHost_function_007D06CC.md) (function, `0x007D06CC`)
- `0x00C2BB12` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (function, `0x007D6800`)
- `0x00C2BB41` → [McTemplateK0_EtwWriteTransfer](../../text/59/McTemplateK0_EtwWriteTransfer_function_00596B24.md) (function, `0x00596B24`)
- `0x00C2BB4C` → [IopInitCrashDumpDuringSysInit](IopInitCrashDumpDuringSysInit_function_00C2CAE4.md) (function, `0x00C2CAE4`)
- `0x00C2BB6B` → [McTemplateK0q_EtwWriteTransfer](../../text/59/McTemplateK0q_EtwWriteTransfer_function_00596B68.md) (function, `0x00596B68`)
- `0x00C2BB77` → [IopInitializeBootDrivers](IopInitializeBootDrivers_function_00C2E6F4.md) (function, `0x00C2E6F4`)
- `0x00C2BB87` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2BBB5` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (function, `0x007D6800`)
- `0x00C2BBD1` → [McTemplateK0_EtwWriteTransfer](../../text/59/McTemplateK0_EtwWriteTransfer_function_00596B24.md) (function, `0x00596B24`)
- `0x00C2BBD9` → [MmRegisterHotPatches](../C6/MmRegisterHotPatches_function_00C678DC.md) (function, `0x00C678DC`)
- `0x00C2BBF7` → [McTemplateK0_EtwWriteTransfer](../../text/59/McTemplateK0_EtwWriteTransfer_function_00596B24.md) (function, `0x00596B24`)
- `0x00C2BC19` → [PoInitSystem](../C7/PoInitSystem_function_00C72358.md) (function, `0x00C72358`)
- `0x00C2BC27` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C2BC3A` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (function, `0x007D6800`)
- `0x00C2BC42` → [SmInitSystem](../C7/SmInitSystem_function_00C7673C.md) (function, `0x00C7673C`)
- `0x00C2BC4C` → [EtwInitialize](../../page/7B/EtwInitialize_function_007B4D40.md) (function, `0x007B4D40`)
- `0x00C2BC51` → [VslRegisterIumPowerCallbacks](VslRegisterIumPowerCallbacks_function_00C29DF0.md) (function, `0x00C29DF0`)
- `0x00C2BC56` → [IopInitializeSystemVariableService](../../text/5A/IopInitializeSystemVariableService_function_005A0310.md) (function, `0x005A0310`)
- `0x00C2BC5B` → [SecureDump_ProvisionCrashDumpKey](../../text/5A/SecureDump_ProvisionCrashDumpKey_function_005A33C8.md) (function, `0x005A33C8`)
- `0x00C2BC69` → [IopDumpTraceForceDumpDisabled](../../page/71/IopDumpTraceForceDumpDisabled_function_0071A138.md) (function, `0x0071A138`)
- `0x00C2BC77` → [IoInitializeLiveDump](../../text/59/IoInitializeLiveDump_function_00598B14.md) (function, `0x00598B14`)
- `0x00C2BC85` → [IopLiveDumpTraceDumpDisabledOnBoot](../../text/59/IopLiveDumpTraceDumpDisabledOnBoot_function_0059EA10.md) (function, `0x0059EA10`)
- `0x00C2BC8A` → [IopInitializeBugCheckDriverData](../../page/71/IopInitializeBugCheckDriverData_function_0071A238.md) (function, `0x0071A238`)
- `0x00C2BC8F` → [IopInitializeTriageDumpData](../../page/71/IopInitializeTriageDumpData_function_0071A740.md) (function, `0x0071A740`)
- `0x00C2BCAB` → [McTemplateK0_EtwWriteTransfer](../../text/59/McTemplateK0_EtwWriteTransfer_function_00596B24.md) (function, `0x00596B24`)
- `0x00C2BCB7` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (function, `0x007D6800`)
- `0x00C2BCC1` → [IopInitCrashDumpDuringSysInit](IopInitCrashDumpDuringSysInit_function_00C2CAE4.md) (function, `0x00C2CAE4`)
- `0x00C2BCE2` → [McTemplateK0q_EtwWriteTransfer](../../text/59/McTemplateK0q_EtwWriteTransfer_function_00596B68.md) (function, `0x00596B68`)
- `0x00C2BCF3` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (function, `0x007D6800`)
- `0x00C2BCFC` → [IopRemoveDumpCapsuleSupport](../../text/59/IopRemoveDumpCapsuleSupport_function_00595E6C.md) (function, `0x00595E6C`)
- `0x00C2BD0C` → [IopTraceCrashDumpDisabledOnBoot](../../page/71/IopTraceCrashDumpDisabledOnBoot_function_0071A81C.md) (function, `0x0071A81C`)
- `0x00C2BD11` → [RtlIsStateSeparationEnabled](../../page/A3/RtlIsStateSeparationEnabled_function_00A3C560.md) (function, `0x00A3C560`)
- `0x00C2BD1A` → [PpLastGoodDoBootProcessing](../C3/PpLastGoodDoBootProcessing_function_00C33BC4.md) (function, `0x00C33BC4`)
- `0x00C2BD31` → [PsLocateSystemDlls](../../page/77/PsLocateSystemDlls_function_0077ED90.md) (function, `0x0077ED90`)
- `0x00C2BD48` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2BD62` → [MmInitializeImageViewExtension](../C6/MmInitializeImageViewExtension_function_00C64F08.md) (function, `0x00C64F08`)
- `0x00C2BD69` → [PfSnBeginBootPhase](../../pagelk/B6/PfSnBeginBootPhase_function_00B6BAC4.md) (function, `0x00B6BAC4`)
- `0x00C2BD75` → [IopReassignSystemRoot](IopReassignSystemRoot_function_00C2D1D0.md) (function, `0x00C2D1D0`)
- `0x00C2BD83` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2BD9A` → [IopProtectSystemPartition](IopProtectSystemPartition_function_00C2E5EC.md) (function, `0x00C2E5EC`)
- `0x00C2BDA8` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2BE04` → [ZwOpenFile](../../text/6A/ZwOpenFile_function_006AD730.md) (function, `0x006AD730`)
- `0x00C2BE31` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00C2BE3F` → [PpPagePathAssign](../../page/72/PpPagePathAssign_function_0072BF28.md) (function, `0x0072BF28`)
- `0x00C2BE4E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00C2BE58` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00C2BE62` → [WMIInitialize](../C4/WMIInitialize_function_00C4D264.md) (function, `0x00C4D264`)
- `0x00C2BE86` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (function, `0x007D6800`)
- `0x00C2BEA5` → [McTemplateK0q_EtwWriteTransfer](../../text/59/McTemplateK0q_EtwWriteTransfer_function_00596B68.md) (function, `0x00596B68`)
- `0x00C2BEB0` → [WheaInitialize](../C5/WheaInitialize_function_00C54C08.md) (function, `0x00C54C08`)
- `0x00C2BECC` → [McTemplateK0_EtwWriteTransfer](../../text/59/McTemplateK0_EtwWriteTransfer_function_00596B24.md) (function, `0x00596B24`)
- `0x00C2BEDE` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (function, `0x007D6800`)
- `0x00C2BEEC` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [IoInitSystem](IoInitSystem_function_00C2ABB8.md) at `0x00C2ABCA`

### Static image references
- `0x00C2AC5F` → RVA `0x00E0A740` (`.data`; read)
- `0x00C2AC87` → RVA `0x01008FD0` (`INITDATA`; read)
- `0x00C2ACAC` → RVA `0x00F8D3A0` (`.data`; read)
- `0x00C2ACDB` → RVA `0x00F8D320` (`.data`; read)
- `0x00C2ACE9` → RVA `0x00F8D2A0` (`.data`; read)
- `0x00C2ACF7` → RVA `0x00F8E900` (`.data`; read)
- `0x00C2AD05` → RVA `0x00F8D0A0` (`.data`; read)
- `0x00C2AD11` → RVA `0x00F8D280` (`.data`; read)
- `0x00C2AD18` → RVA `0x00F8D290` (`.data`; write)
- `0x00C2AD1F` → RVA `0x00F8D288` (`.data`; write)
- `0x00C2AD29` → RVA `0x00F8D280` (`.data`; write)
- `0x00C2AD30` → RVA `0x00F8D270` (`.data`; read)
- `0x00C2AD37` → RVA `0x00F8D278` (`.data`; write)
- `0x00C2AD3E` → RVA `0x00F8D270` (`.data`; write)
- `0x00C2AD45` → RVA `0x00F8D260` (`.data`; read)
- `0x00C2AD4C` → RVA `0x00F8D268` (`.data`; write)
- `0x00C2AD53` → RVA `0x00F8D260` (`.data`; write)
- `0x00C2AD5A` → RVA `0x00F8D250` (`.data`; read)
- `0x00C2AD61` → RVA `0x00F8D258` (`.data`; write)
- `0x00C2AD68` → RVA `0x00F8D250` (`.data`; write)
- `0x00C2AD6F` → RVA `0x00F8D240` (`.data`; read)
- `0x00C2AD76` → RVA `0x00F8D248` (`.data`; write)
- `0x00C2AD7D` → RVA `0x00F8D240` (`.data`; write)
- `0x00C2AD84` → RVA `0x00F8D230` (`.data`; read)
- `0x00C2AD8B` → RVA `0x00F8D238` (`.data`; write)
- `0x00C2AD92` → RVA `0x00F8D230` (`.data`; write)
- `0x00C2AD99` → RVA `0x00F8D220` (`.data`; read)
- `0x00C2ADA0` → RVA `0x00F8D228` (`.data`; write)
- `0x00C2ADA7` → RVA `0x00F8D220` (`.data`; write)
- `0x00C2ADAE` → RVA `0x00F8D460` (`.data`; read)
- `0x00C2ADB5` → RVA `0x00F8D468` (`.data`; write)
- `0x00C2ADBC` → RVA `0x00F8D460` (`.data`; write)
- `0x00C2ADC3` → RVA `0x00F8D450` (`.data`; read)
- `0x00C2ADCA` → RVA `0x00F8D458` (`.data`; write)
- `0x00C2ADD1` → RVA `0x00F8D450` (`.data`; write)
- `0x00C2ADD8` → RVA `0x00F8D440` (`.data`; read)
- `0x00C2ADDF` → RVA `0x00F8D448` (`.data`; write)
- `0x00C2ADE6` → RVA `0x00F8D440` (`.data`; write)
- `0x00C2ADED` → RVA `0x00F8D438` (`.data`; write)
- `0x00C2ADF4` → RVA `0x00FCF900` (`CACHEALI`; write)
- `0x00C2ADFB` → RVA `0x00F8D430` (`.data`; write)
- `0x00C2AE02` → RVA `0x00F8D420` (`.data`; write)
- `0x00C2AE0A` → RVA `0x00F8D414` (`.data`; write)
- `0x00C2AE1F` → RVA `0x00F8D210` (`.data`; write)
- `0x00C2AE58` → RVA `0x00F8D40C` (`.data`; read)
- `0x00C2AE5F` → RVA `0x00F8D410` (`.data`; write)
- `0x00C2AE68` → RVA `0x00F8D40C` (`.data`; write)
- `0x00C2AE7C` → RVA `0x00F8D408` (`.data`; read)
- `0x00C2AE8D` → RVA `0x00F8D408` (`.data`; write)
- `0x00C2AE99` → RVA `0x00E660FC` (`.data`; read)
- `0x00C2AEA9` → RVA `0x00E660FC` (`.data`; write)
- `0x00C2AEC0` → RVA `0x00EFAC00` (`.data`; read)
- `0x00C2AEE0` → RVA `0x00E12480` (`.data`; read)
- `0x00C2AEF6` → RVA `0x00E12500` (`.data`; read)
- `0x00C2AF1D` → RVA `0x00E12580` (`.data`; read)
- `0x00C2AF44` → RVA `0x00E12600` (`.data`; read)
- `0x00C2AF6B` → RVA `0x00E12680` (`.data`; read)
- `0x00C2AF93` → RVA `0x00E12300` (`.data`; read)
- `0x00C2AFC7` → RVA `0x00E12380` (`.data`; read)
- `0x00C2AFE4` → RVA `0x00E12400` (`.data`; read)
- `0x00C2B027` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x00C2B04A` → RVA `0x00F8D670` (`.data`; read)
- `0x00C2B051` → RVA `0x00FCF1C0` (`CACHEALI`; write)
- `0x00C2B058` → RVA `0x00F8D678` (`.data`; write)
- `0x00C2B05F` → RVA `0x00F8D670` (`.data`; write)
- `0x00C2B06F` → RVA `0x00F8D8D0` (`.data`; write)
- `0x00C2B080` → RVA `0x00F8D210` (`.data`; read)
- `0x00C2B08A` → RVA `0x00475420` (`IopIrpStackProfilerDpcRoutine`; read)
- `0x00C2B091` → RVA `0x00F8D564` (`.data`; write)
- `0x00C2B09D` → RVA `0x00F8D538` (`.data`; write)
- `0x00C2B0AA` → RVA `0x00F8D560` (`.data`; write)
- `0x00C2B0B4` → RVA `0x00F8D520` (`.data`; write)
- `0x00C2B0BE` → RVA `0x00F8D540` (`.data`; write)
- `0x00C2B0C5` → RVA `0x00F8D558` (`.data`; write)
- `0x00C2B0CC` → RVA `0x00F8D530` (`.data`; write)
- `0x00C2B0D3` → RVA `0x00E0A9C4` (`.data`; read)
- `0x00C2B0E4` → RVA `0x00E0A9C4` (`.data`; write)
- `0x00C2B0FB` → RVA `0x00FDA3E8` (`PAGEDATA`; read)
- `0x00C2B13A` → RVA `0x00C79970` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2B159` → RVA `0x010088A8` (`INITDATA`; read)
- `0x00C2B178` → RVA `0x010088AC` (`INITDATA`; read)
- `0x00C2B180` → RVA `0x010088B4` (`INITDATA`; read)
- `0x00C2B195` → RVA `0x00F8D05A` (`.data`; write)
- `0x00C2B1A9` → RVA `0x00F8D510` (`.data`; read)
- `0x00C2B1B0` → RVA `0x00F8D480` (`.data`; write)
- `0x00C2B1B7` → RVA `0x00F8D518` (`.data`; write)
- `0x00C2B1C4` → RVA `0x00F8D510` (`.data`; write)
- `0x00C2B1CB` → RVA `0x003A3900` (`IopTimerDispatch`; read)
- `0x00C2B1D2` → RVA `0x00F8D4D8` (`.data`; write)
- `0x00C2B1D9` → RVA `0x00F8D500` (`.data`; read)
- `0x00C2B1E0` → RVA `0x00F8D4E0` (`.data`; write)
- `0x00C2B1E7` → RVA `0x00F8D488` (`.data`; read)
- `0x00C2B1EE` → RVA `0x00F8D490` (`.data`; write)
- `0x00C2B1F5` → RVA `0x00F8D488` (`.data`; write)
- `0x00C2B1FC` → RVA `0x00F8D470` (`.data`; read)
- `0x00C2B203` → RVA `0x00F8D478` (`.data`; write)
- `0x00C2B20A` → RVA `0x00F8D470` (`.data`; write)
- `0x00C2B211` → RVA `0x0071B690` (`IopHardErrorThread`; read)
- `0x00C2B218` → RVA `0x00F8D790` (`.data`; write)
- `0x00C2B21F` → RVA `0x00F8D7A0` (`.data`; read)
- `0x00C2B226` → RVA `0x00F8D7A8` (`.data`; write)
- `0x00C2B22D` → RVA `0x00F8D7A0` (`.data`; write)
- `0x00C2B234` → RVA `0x00F8D7C0` (`.data`; read)
- `0x00C2B23B` → RVA `0x00F8D7C8` (`.data`; write)
- `0x00C2B242` → RVA `0x00F8D7C0` (`.data`; write)
- `0x00C2B249` → RVA `0x00E0A9BC` (`.data`; read)
- `0x00C2B254` → RVA `0x00FCF140` (`CACHEALI`; write)
- `0x00C2B25B` → RVA `0x00F8D4C0` (`.data`; write)
- `0x00C2B265` → RVA `0x00F8D4F8` (`.data`; write)
- `0x00C2B26C` → RVA `0x00F8D4D0` (`.data`; write)
- `0x00C2B27A` → RVA `0x00F8D498` (`.data`; write)
- `0x00C2B281` → RVA `0x00F8D4BC` (`.data`; write)
- `0x00C2B288` → RVA `0x00F8D4B8` (`.data`; write)
- `0x00C2B290` → RVA `0x00F8D798` (`.data`; write)
- `0x00C2B297` → RVA `0x00F8D780` (`.data`; write)
- `0x00C2B29E` → RVA `0x00F8D7B0` (`.data`; write)
- `0x00C2B2A5` → RVA `0x00F8D7B8` (`.data`; write)
- `0x00C2B2AC` → RVA `0x00F8D7BA` (`.data`; write)
- `0x00C2B2B3` → RVA `0x00F8D7BC` (`.data`; write)
- `0x00C2B2BA` → RVA `0x00F8D7D0` (`.data`; write)
- `0x00C2B2C4` → RVA `0x00F8D7D8` (`.data`; write)
- `0x00C2B2D2` → RVA `0x00E0A9BC` (`.data`; write)
- `0x00C2B2DC` → RVA `0x00494FD0` (`IopKeepAliveWorker`; read)
- `0x00C2B2E3` → RVA `0x00F8D718` (`.data`; write)
- `0x00C2B2EA` → RVA `0x00F8D710` (`.data`; write)
- `0x00C2B2F1` → RVA `0x00C79940` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2B2F8` → RVA `0x00F8D720` (`.data`; read)
- `0x00C2B2FF` → RVA `0x00F8D700` (`.data`; write)
- `0x00C2B30A` → RVA `0x00F8D728` (`.data`; write)
- `0x00C2B311` → RVA `0x00F8D720` (`.data`; write)
- `0x00C2B318` → RVA `0x00F8D730` (`.data`; write)
- `0x00C2B31F` → RVA `0x00F8D758` (`.data`; write)
- `0x00C2B326` → RVA `0x00F8D05B` (`.data`; write)
- `0x00C2B392` → RVA `0x00FC6B80` (`ALMOSTRO`; read)
- `0x00C2B3CD` → RVA `0x00FD9F88` (`PAGEDATA`; write)
- `0x00C2B3D4` → RVA `0x00F8D6E8` (`.data`; read)
- `0x00C2B3DB` → RVA `0x00F8D6F0` (`.data`; write)
- `0x00C2B3E2` → RVA `0x00F8D6E8` (`.data`; write)
- `0x00C2B3E9` → RVA `0x00F8D6C8` (`.data`; read)
- `0x00C2B3F0` → RVA `0x00F8D6D0` (`.data`; write)
- `0x00C2B3F7` → RVA `0x00F8D6C8` (`.data`; write)
- `0x00C2B3FE` → RVA `0x00F8D688` (`.data`; read)
- `0x00C2B405` → RVA `0x00F8D690` (`.data`; write)
- `0x00C2B40C` → RVA `0x00F8D688` (`.data`; write)
- `0x00C2B413` → RVA `0x00F8D6E0` (`.data`; write)
- `0x00C2B41B` → RVA `0x00F8D6E2` (`.data`; write)
- `0x00C2B421` → RVA `0x00F8D6E4` (`.data`; write)
- `0x00C2B428` → RVA `0x00F8D6C0` (`.data`; write)
- `0x00C2B430` → RVA `0x00F8D6C2` (`.data`; write)
- `0x00C2B436` → RVA `0x00F8D6C4` (`.data`; write)
- `0x00C2B43D` → RVA `0x00F8D680` (`.data`; write)
- `0x00C2B445` → RVA `0x00F8D682` (`.data`; write)
- `0x00C2B44B` → RVA `0x00F8D684` (`.data`; write)
- `0x00C2B4D4` → RVA `0x00E00690` (`.data`; read)
- `0x00C2B4E0` → RVA `0x00F8C438` (`.data`; read)
- `0x00C2B513` → RVA `0x01008690` (`INITDATA`; write)
- `0x00C2B55E` → RVA `0x00151378` (`ext-ms-win-ntos-stateseparation-l1-1-0.dll!ExpInitializeStateSeparationPhase0 (IAT)`; read)
- `0x00C2B5AB` → RVA `0x00F8D058` (`.data`; write)
- `0x00C2B5F7` → RVA `0x00F8D7E0` (`.data`; read)
- `0x00C2B601` → RVA `0x0071B450` (`IopEtwEnableCallback`; read)
- `0x00C2B608` → RVA `0x00023528` (`.rdata`; read)
- `0x00C2B628` → RVA `0x00E06E20` (`.data`; read)
- `0x00C2B636` → RVA `0x00021628` (`.rdata`; read)
- `0x00C2B655` → RVA `0x00E0A058` (`.data`; read)
- `0x00C2B662` → RVA `0x00AB6510` (`MiTracingEnabledCallback`; read)
- `0x00C2B681` → RVA `0x00E37618` (`.data`; write)
- `0x00C2B688` → RVA `0x00E302C0` (`.data`; read)
- `0x00C2B69F` → RVA `0x00E65EF0` (`.data`; read)
- `0x00C2B6A9` → RVA `0x005953D0` (`IopDumpTracingControlCallback`; read)
- `0x00C2B6B0` → RVA `0x00021C00` (`.rdata`; read)
- `0x00C2B6BF` → RVA `0x00E06DE8` (`.data`; read)
- `0x00C2B6D5` → RVA `0x00E06E68` (`.data`; read)
- `0x00C2B6FE` → RVA `0x00F475E0` (`.data`; read)
- `0x00C2B708` → RVA `0x001516B8` (`kdcom.dll!KdInitialize (IAT)`; read)
- `0x00C2B71E` → RVA `0x00F8D05A` (`.data`; read)
- `0x00C2B727` → RVA `0x00FCF1C0` (`CACHEALI`; read)
- `0x00C2B74E` → RVA `0x00A5DC80` (`IopErrorLogThread`; read)
- `0x00C2B755` → RVA `0x00F8D078` (`.data`; write)
- `0x00C2B75F` → RVA `0x00F8D070` (`.data`; write)
- `0x00C2B766` → RVA `0x00F8D060` (`.data`; read)
- `0x00C2B76D` → RVA `0x00F8D060` (`.data`; write)
- `0x00C2B79E` → RVA `0x00F8D8D4` (`.data`; reference)
- `0x00C2B7AA` → RVA `0x00022AB8` (`.rdata`; read)
- `0x00C2B7D0` → RVA `0x00021018` (`.rdata`; read)
- `0x00C2B83C` → RVA `0x00F8D800` (`.data`; read)
- `0x00C2B84F` → RVA `0x009A8D60` (`IopCompareIosbRanges`; read)
- `0x00C2B856` → RVA `0x00F8D800` (`.data`; write)
- `0x00C2B85D` → RVA `0x00F8D848` (`.data`; write)
- `0x00C2B869` → RVA `0x0071AD30` (`IopAllocateGenericTableEntry`; read)
- `0x00C2B870` → RVA `0x00F8D860` (`.data`; write)
- `0x00C2B877` → RVA `0x00F8D850` (`.data`; write)
- `0x00C2B881` → RVA `0x0071B480` (`IopFreeGenericTableEntry`; read)
- `0x00C2B888` → RVA `0x00F8D880` (`.data`; write)
- `0x00C2B88F` → RVA `0x00F8D858` (`.data`; write)
- `0x00C2B896` → RVA `0x00F8D8A0` (`.data`; read)
- `0x00C2B89D` → RVA `0x00F8D8A8` (`.data`; write)
- `0x00C2B8A4` → RVA `0x00F8D8A0` (`.data`; write)
- `0x00C2B8AB` → RVA `0x00F8D888` (`.data`; write)
- `0x00C2B8B2` → RVA `0x00F8D890` (`.data`; write)
- `0x00C2B8B9` → RVA `0x00F8D898` (`.data`; write)
- `0x00C2B8C1` → RVA `0x00F8D89A` (`.data`; write)
- `0x00C2B8C7` → RVA `0x00F8D89C` (`.data`; write)
- `0x00C2B8D3` → RVA `0x00E685E0` (`.data`; read)
- `0x00C2B8DF` → RVA `0x00022CF8` (`.rdata`; read)
- `0x00C2B8EF` → RVA `0x00E685E0` (`.data`; write)
- `0x00C2B960` → RVA `0x00E662D8` (`.data`; read)
- `0x00C2B974` → RVA `0x00E0A9F0` (`.data`; read)
- `0x00C2B97B` → RVA `0x00027400` (`.rdata`; read)
- `0x00C2B987` → RVA `0x00F8CCC0` (`.data`; read)
- `0x00C2B98E` → RVA `0x00F8CCA0` (`.data`; write)
- `0x00C2B996` → RVA `0x00F8CCC8` (`.data`; write)
- `0x00C2B99D` → RVA `0x00F8CCC0` (`.data`; write)
- `0x00C2B9A4` → RVA `0x00F8CCA8` (`.data`; read)
- `0x00C2B9AB` → RVA `0x00F8CCB0` (`.data`; write)
- `0x00C2B9B2` → RVA `0x00F8CCA8` (`.data`; write)
- `0x00C2B9B9` → RVA `0x00F8CCA2` (`.data`; write)
- `0x00C2B9BF` → RVA `0x00F8CCA4` (`.data`; write)
- `0x00C2B9CB` → RVA `0x00E0AA01` (`.data`; read)
- `0x00C2B9D2` → RVA `0x00F8CC90` (`.data`; read)
- `0x00C2B9D9` → RVA `0x00F8CC40` (`.data`; read)
- `0x00C2B9E0` → RVA `0x00F8CC98` (`.data`; write)
- `0x00C2B9E7` → RVA `0x00F8CC90` (`.data`; write)
- `0x00C2B9EE` → RVA `0x00F8CC80` (`.data`; write)
- `0x00C2BA1C` → RVA `0x00E660BC` (`.data`; read)
- `0x00C2BA2C` → RVA `0x00E0A9BA` (`.data`; read)
- `0x00C2BA3C` → RVA `0x00E0A9B9` (`.data`; write)
- `0x00C2BA55` → RVA `0x00FD9BC4` (`PAGEDATA`; read)
- `0x00C2BA64` → RVA `0x00EFEE38` (`.data`; read)
- `0x00C2BA7D` → RVA `0x00007F70` (`.rdata`; read)
- `0x00C2BAA2` → RVA `0x00F8D130` (`.data`; read)
- `0x00C2BAC3` → RVA `0x00F8D130` (`.data`; write)
- `0x00C2BACA` → RVA `0x005E4080` (`PsPicoAltSystemCallDispatch`; read)
- `0x00C2BAD1` → RVA `0x00F06588` (`.data`; write)
- `0x00C2BAD8` → RVA `0x00FC72C0` (`ALMOSTRO`; write)
- `0x00C2BADF` → RVA `0x00448EB0` (`HalSetEnvironmentVariableEx`; read)
- `0x00C2BAE6` → RVA `0x00F8E968` (`.data`; write)
- `0x00C2BAF7` → RVA `0x0058F230` (`VslReportBugCheckProgress`; read)
- `0x00C2BB33` → RVA `0x00022FC8` (`.rdata`; read)
- `0x00C2BB5D` → RVA `0x000230A0` (`.rdata`; read)
- `0x00C2BB8C` → RVA `0x00F8D8D0` (`.data`; read)
- `0x00C2BBC3` → RVA `0x00021E58` (`.rdata`; read)
- `0x00C2BBE9` → RVA `0x000224A8` (`.rdata`; read)
- `0x00C2BC7C` → RVA `0x00E0A9B8` (`.data`; read)
- `0x00C2BD1F` → RVA `0x00FC42C0` (`.data`; read)
- `0x00C2BD2B` → RVA `0x00FC42C0` (`.data`; write)
- `0x00C2BDBC` → RVA `0x00EF54C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **111**
  - `0x00C2ACD4` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (`INIT` → `.text`)
  - `0x00C2ACE2` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (`INIT` → `.text`)
  - `0x00C2ACF0` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (`INIT` → `.text`)
  - `0x00C2ACFE` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (`INIT` → `.text`)
  - `0x00C2AD0C` → [ExInitializeResourceLite2](../../text/41/ExInitializeResourceLite2_function_0041F710.md) (`INIT` → `.text`)
  - `0x00C2AEB7` → [IopQueryProcessorInitValues](../../page/71/IopQueryProcessorInitValues_function_0071AB80.md) (`INIT` → `PAGE`)
  - `0x00C2AEED` → [ExInitializeSystemLookasideList](../../pagelk/B7/ExInitializeSystemLookasideList_function_00B7E57C.md) (`INIT` → `PAGELK`)
  - `0x00C2AF14` → [ExInitializeSystemLookasideList](../../pagelk/B7/ExInitializeSystemLookasideList_function_00B7E57C.md) (`INIT` → `PAGELK`)
  - `0x00C2AF3B` → [ExInitializeSystemLookasideList](../../pagelk/B7/ExInitializeSystemLookasideList_function_00B7E57C.md) (`INIT` → `PAGELK`)
  - `0x00C2AF62` → [ExInitializeSystemLookasideList](../../pagelk/B7/ExInitializeSystemLookasideList_function_00B7E57C.md) (`INIT` → `PAGELK`)
  - `0x00C2AF89` → [ExInitializeSystemLookasideList](../../pagelk/B7/ExInitializeSystemLookasideList_function_00B7E57C.md) (`INIT` → `PAGELK`)
  - `0x00C2AFC0` → [ExInitializeNPagedLookasideListInternal](../../text/46/ExInitializeNPagedLookasideListInternal_function_00468720.md) (`INIT` → `.text`)
  - `0x00C2AFDA` → [FsRtlInitExtraCreateParameterLookasideList](../../page/71/FsRtlInitExtraCreateParameterLookasideList_function_00713910.md) (`INIT` → `PAGE`)
  - `0x00C2B00A` → [ExInitializeNPagedLookasideListInternal](../../text/46/ExInitializeNPagedLookasideListInternal_function_00468720.md) (`INIT` → `.text`)
  - `0x00C2B014` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (`INIT` → `.text`)
  - `0x00C2B036` → [IoInitializeProcessor](../../page/71/IoInitializeProcessor_function_0071A91C.md) (`INIT` → `PAGE`)
  - `0x00C2B131` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`INIT` → `.text`)
  - `0x00C2B145` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C2B16F` → [NtQueryValueKey](../../page/8B/NtQueryValueKey_function_008B2A00.md) (`INIT` → `PAGE`)
  - `0x00C2B19B` → [ObCloseHandle](../../page/8A/ObCloseHandle_function_008A1870.md) (`INIT` → `PAGE`)
  - `0x00C2B32D` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C2B36D` → [NtCreateEvent](../../page/8B/NtCreateEvent_function_008B9140.md) (`INIT` → `PAGE`)
  - `0x00C2B37C` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2B3B7` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (`INIT` → `PAGE`)
  - `0x00C2B452` → [ObCloseHandle](../../page/8A/ObCloseHandle_function_008A1870.md) (`INIT` → `PAGE`)
  - `0x00C2B464` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2B4A5` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2B4C0` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (`INIT` → `PAGE`)
  - `0x00C2B4DB` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C2B51A` → [PipSetDevNodeFlags](../../page/8F/PipSetDevNodeFlags_function_008FC048.md) (`INIT` → `PAGE`)
  - `0x00C2B549` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (`INIT` → `PAGE`)
  - `0x00C2B54E` → [CmIsStateSeparationDevModeEnabled](../../page/7D/CmIsStateSeparationDevModeEnabled_function_007DF1D8.md) (`INIT` → `PAGE`)
  - `0x00C2B555` → [RtlIsStateSeparationEnabled](../../page/A3/RtlIsStateSeparationEnabled_function_00A3C560.md) (`INIT` → `PAGE`)
  - `0x00C2B596` → [RtlGetNtProductType](../../text/43/RtlGetNtProductType_function_00436270.md) (`INIT` → `.text`)
  - `0x00C2B5BD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C2B5DE` → [AstInitializeBloomFilter](../../page/72/AstInitializeBloomFilter_function_00722E34.md) (`INIT` → `PAGE`)
  - `0x00C2B5F2` → [EtwInitialize](../../page/7B/EtwInitialize_function_007B4D40.md) (`INIT` → `PAGE`)
  - `0x00C2B60F` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (`INIT` → `PAGE`)
  - `0x00C2B63D` → [McGenEventRegister_EtwRegister](../../text/57/McGenEventRegister_EtwRegister_function_0057EF04.md) (`INIT` → `.text`)
  - `0x00C2B669` → [TlgRegisterAggregateProviderEx](../../page/AD/TlgRegisterAggregateProviderEx_function_00ADBA94.md) (`INIT` → `PAGE`)
  - `0x00C2B69A` → [MiLogBadMapper](../../text/2F/MiLogBadMapper_function_002F1140.md) (`INIT` → `.text`)
  - `0x00C2B6B7` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (`INIT` → `PAGE`)
  - `0x00C2B6C8` → [TraceLoggingRegisterEx_EtwRegister_EtwSetInformation](../../page/92/TraceLoggingRegisterEx_EtwRegister_EtwSetInformation_function_009208A0.md) (`INIT` → `PAGE`)
  - `0x00C2B6D0` → [IopInitializeDumpPolicySettings](../../page/71/IopInitializeDumpPolicySettings_function_0071A444.md) (`INIT` → `PAGE`)
  - `0x00C2B6DC` → [TlgRegisterAggregateProvider](../../page/70/TlgRegisterAggregateProvider_function_0070526C.md) (`INIT` → `PAGE`)
  - `0x00C2B6EF` → [SeAuditBootConfiguration](../../page/79/SeAuditBootConfiguration_function_0079E374.md) (`INIT` → `PAGE`)
  - `0x00C2B72E` → [KeAcquireSpinLockRaiseToDpc](../../text/20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (`INIT` → `.text`)
  - `0x00C2B774` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`INIT` → `.text`)
  - `0x00C2B782` → [KeReleaseSpinLock](../../text/39/KeReleaseSpinLock_function_00392BA0.md) (`INIT` → `.text`)
  - `0x00C2B794` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (`INIT` → `PAGE`)
  - `0x00C2B7B8` → [McTemplateK0q_EtwWriteTransfer](../../text/59/McTemplateK0q_EtwWriteTransfer_function_00596B68.md) (`INIT` → `.text`)
  - `0x00C2B7DE` → [McTemplateK0_EtwWriteTransfer](../../text/59/McTemplateK0_EtwWriteTransfer_function_00596B24.md) (`INIT` → `.text`)
  - `0x00C2B7F0` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (`INIT` → `PAGE`)
  - `0x00C2B826` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2B84A` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C2B8E6` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (`INIT` → `PAGE`)
  - `0x00C2B904` → [HvlPhase2Initialize](../../text/58/HvlPhase2Initialize_function_00583EA0.md) (`INIT` → `.text`)
  - `0x00C2B929` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (`INIT` → `PAGE`)
  - `0x00C2B930` → [KeOptimizeSpecCtrlSettings](../../text/5B/KeOptimizeSpecCtrlSettings_function_005BE95C.md) (`INIT` → `.text`)
  - `0x00C2B93A` → [VslpIumPhase4Initialize](../../text/58/VslpIumPhase4Initialize_function_0058FAE0.md) (`INIT` → `.text`)
  - `0x00C2B94C` → [BapdRecordFirmwareBootStats](../../pagelk/B7/BapdRecordFirmwareBootStats_function_00B72474.md) (`INIT` → `PAGELK`)
  - `0x00C2B95B` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (`INIT` → `PAGE`)
  - `0x00C2B982` → [EtwWriteStartScenario](../../page/AB/EtwWriteStartScenario_function_00AB75B0.md) (`INIT` → `PAGE`)
  - `0x00C2B9C6` → [IopQueryPassiveInterruptRegistryOptions](../../page/72/IopQueryPassiveInterruptRegistryOptions_function_0072BBB4.md) (`INIT` → `PAGE`)
  - `0x00C2B9F5` → [KeInitializeQueue](../../text/48/KeInitializeQueue_function_00480C90.md) (`INIT` → `.text`)
  - `0x00C2B9FA` → [IopCreatePassiveInterruptRealtimeThreads](../../page/72/IopCreatePassiveInterruptRealtimeThreads_function_0072BA98.md) (`INIT` → `PAGE`)
  - `0x00C2BA17` → [SecureDump_PrepareForInit](../../text/5A/SecureDump_PrepareForInit_function_005A317C.md) (`INIT` → `.text`)
  - `0x00C2BA35` → [IopInitDumpCapsuleSupport](../../text/59/IopInitDumpCapsuleSupport_function_0059578C.md) (`INIT` → `.text`)
  - `0x00C2BA50` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (`INIT` → `PAGE`)
  - `0x00C2BA5F` → [EtwTraceLeapSecondDataParseFailure](../../page/7B/EtwTraceLeapSecondDataParseFailure_function_007B7F70.md) (`INIT` → `PAGE`)
  - `0x00C2BA78` → [EtwTraceLeapSecondDataUpdate](../../page/7B/EtwTraceLeapSecondDataUpdate_function_007B8050.md) (`INIT` → `PAGE`)
  - `0x00C2BABA` → [ExRegisterHost](../../page/7D/ExRegisterHost_function_007D06CC.md) (`INIT` → `PAGE`)
  - `0x00C2BB12` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (`INIT` → `PAGE`)
  - `0x00C2BB41` → [McTemplateK0_EtwWriteTransfer](../../text/59/McTemplateK0_EtwWriteTransfer_function_00596B24.md) (`INIT` → `.text`)
  - `0x00C2BB6B` → [McTemplateK0q_EtwWriteTransfer](../../text/59/McTemplateK0q_EtwWriteTransfer_function_00596B68.md) (`INIT` → `.text`)
  - `0x00C2BB87` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2BBB5` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (`INIT` → `PAGE`)
  - `0x00C2BBD1` → [McTemplateK0_EtwWriteTransfer](../../text/59/McTemplateK0_EtwWriteTransfer_function_00596B24.md) (`INIT` → `.text`)
  - `0x00C2BBF7` → [McTemplateK0_EtwWriteTransfer](../../text/59/McTemplateK0_EtwWriteTransfer_function_00596B24.md) (`INIT` → `.text`)
  - `0x00C2BC27` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C2BC3A` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (`INIT` → `PAGE`)
  - `0x00C2BC4C` → [EtwInitialize](../../page/7B/EtwInitialize_function_007B4D40.md) (`INIT` → `PAGE`)
  - `0x00C2BC56` → [IopInitializeSystemVariableService](../../text/5A/IopInitializeSystemVariableService_function_005A0310.md) (`INIT` → `.text`)
  - `0x00C2BC5B` → [SecureDump_ProvisionCrashDumpKey](../../text/5A/SecureDump_ProvisionCrashDumpKey_function_005A33C8.md) (`INIT` → `.text`)
  - `0x00C2BC69` → [IopDumpTraceForceDumpDisabled](../../page/71/IopDumpTraceForceDumpDisabled_function_0071A138.md) (`INIT` → `PAGE`)
  - `0x00C2BC77` → [IoInitializeLiveDump](../../text/59/IoInitializeLiveDump_function_00598B14.md) (`INIT` → `.text`)
  - `0x00C2BC85` → [IopLiveDumpTraceDumpDisabledOnBoot](../../text/59/IopLiveDumpTraceDumpDisabledOnBoot_function_0059EA10.md) (`INIT` → `.text`)
  - `0x00C2BC8A` → [IopInitializeBugCheckDriverData](../../page/71/IopInitializeBugCheckDriverData_function_0071A238.md) (`INIT` → `PAGE`)
  - `0x00C2BC8F` → [IopInitializeTriageDumpData](../../page/71/IopInitializeTriageDumpData_function_0071A740.md) (`INIT` → `PAGE`)
  - `0x00C2BCAB` → [McTemplateK0_EtwWriteTransfer](../../text/59/McTemplateK0_EtwWriteTransfer_function_00596B24.md) (`INIT` → `.text`)
  - `0x00C2BCB7` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (`INIT` → `PAGE`)
  - `0x00C2BCE2` → [McTemplateK0q_EtwWriteTransfer](../../text/59/McTemplateK0q_EtwWriteTransfer_function_00596B68.md) (`INIT` → `.text`)
  - `0x00C2BCF3` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (`INIT` → `PAGE`)
  - `0x00C2BCFC` → [IopRemoveDumpCapsuleSupport](../../text/59/IopRemoveDumpCapsuleSupport_function_00595E6C.md) (`INIT` → `.text`)
  - `0x00C2BD0C` → [IopTraceCrashDumpDisabledOnBoot](../../page/71/IopTraceCrashDumpDisabledOnBoot_function_0071A81C.md) (`INIT` → `PAGE`)
  - `0x00C2BD11` → [RtlIsStateSeparationEnabled](../../page/A3/RtlIsStateSeparationEnabled_function_00A3C560.md) (`INIT` → `PAGE`)
  - `0x00C2BD31` → [PsLocateSystemDlls](../../page/77/PsLocateSystemDlls_function_0077ED90.md) (`INIT` → `PAGE`)
  - `0x00C2BD48` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2BD69` → [PfSnBeginBootPhase](../../pagelk/B6/PfSnBeginBootPhase_function_00B6BAC4.md) (`INIT` → `PAGELK`)
  - `0x00C2BD83` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2BDA8` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2BE04` → [ZwOpenFile](../../text/6A/ZwOpenFile_function_006AD730.md) (`INIT` → `.text`)
  - `0x00C2BE31` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (`INIT` → `PAGE`)
  - `0x00C2BE3F` → [PpPagePathAssign](../../page/72/PpPagePathAssign_function_0072BF28.md) (`INIT` → `PAGE`)
  - `0x00C2BE4E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`INIT` → `.text`)
  - `0x00C2BE58` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`INIT` → `.text`)
  - `0x00C2BE86` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (`INIT` → `PAGE`)
  - `0x00C2BEA5` → [McTemplateK0q_EtwWriteTransfer](../../text/59/McTemplateK0q_EtwWriteTransfer_function_00596B68.md) (`INIT` → `.text`)
  - `0x00C2BECC` → [McTemplateK0_EtwWriteTransfer](../../text/59/McTemplateK0_EtwWriteTransfer_function_00596B24.md) (`INIT` → `.text`)
  - `0x00C2BEDE` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (`INIT` → `PAGE`)
  - `0x00C2BEEC` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C2AC3C  48 8B C4                        mov rax, rsp
00C2AC3F  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00C2AC43  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00C2AC47  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00C2AC4B  55                              push rbp
00C2AC4C  41 54                           push r12
00C2AC4E  41 55                           push r13
00C2AC50  41 56                           push r14
00C2AC52  41 57                           push r15
00C2AC54  48 8D 68 C8                     lea rbp, [rax - 0x38]
00C2AC58  48 81 EC 10 01 00 00            sub rsp, 0x110
00C2AC5F  48 8B 05 DA FA 1D 00            mov rax, qword ptr [rip + 0x1dfada]
00C2AC66  48 33 C4                        xor rax, rsp
00C2AC69  48 89 45 00                     mov qword ptr [rbp], rax
00C2AC6D  45 33 E4                        xor r12d, r12d
00C2AC70  48 C7 45 B0 00 00 00 01         mov qword ptr [rbp - 0x50], 0x1000000
00C2AC78  0F 57 C0                        xorps xmm0, xmm0
00C2AC7B  4C 89 65 C0                     mov qword ptr [rbp - 0x40], r12
00C2AC7F  0F 57 C9                        xorps xmm1, xmm1
00C2AC82  44 89 64 24 74                  mov dword ptr [rsp + 0x74], r12d
00C2AC87  48 8D 05 42 E3 3D 00            lea rax, [rip + 0x3de342]
00C2AC8E  44 89 65 8C                     mov dword ptr [rbp - 0x74], r12d
00C2AC92  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00C2AC96  48 8B F9                        mov rdi, rcx
00C2AC99  48 8B 81 F0 00 00 00            mov rax, qword ptr [rcx + 0xf0]
00C2ACA0  83 CB FF                        or ebx, 0xffffffff
00C2ACA3  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
00C2ACA7  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
00C2ACAC  48 8D 0D ED 26 36 00            lea rcx, [rip + 0x3626ed]
00C2ACB3  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
00C2ACB7  44 8B B0 84 00 00 00            mov r14d, dword ptr [rax + 0x84]
00C2ACBE  8B D3                           mov edx, ebx
00C2ACC0  41 81 E6 00 00 08 00            and r14d, 0x80000
00C2ACC7  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00C2ACCC  0F 11 4D D8                     movups xmmword ptr [rbp - 0x28], xmm1
00C2ACD0  0F 11 4D E8                     movups xmmword ptr [rbp - 0x18], xmm1
00C2ACD4  E8 37 4A 7F FF                  call 0x14041f710
00C2ACD9  8B D3                           mov edx, ebx
00C2ACDB  48 8D 0D 3E 26 36 00            lea rcx, [rip + 0x36263e]
00C2ACE2  E8 29 4A 7F FF                  call 0x14041f710
00C2ACE7  8B D3                           mov edx, ebx
00C2ACE9  48 8D 0D B0 25 36 00            lea rcx, [rip + 0x3625b0]
00C2ACF0  E8 1B 4A 7F FF                  call 0x14041f710
00C2ACF5  8B D3                           mov edx, ebx
00C2ACF7  48 8D 0D 02 3C 36 00            lea rcx, [rip + 0x363c02]
00C2ACFE  E8 0D 4A 7F FF                  call 0x14041f710
00C2AD03  8B D3                           mov edx, ebx
00C2AD05  48 8D 0D 94 23 36 00            lea rcx, [rip + 0x362394]
00C2AD0C  E8 FF 49 7F FF                  call 0x14041f710
00C2AD11  48 8D 05 68 25 36 00            lea rax, [rip + 0x362568]
00C2AD18  4C 89 25 71 25 36 00            mov qword ptr [rip + 0x362571], r12
00C2AD1F  48 89 05 62 25 36 00            mov qword ptr [rip + 0x362562], rax
00C2AD26  0F 57 C0                        xorps xmm0, xmm0
00C2AD29  48 89 05 50 25 36 00            mov qword ptr [rip + 0x362550], rax
00C2AD30  48 8D 05 39 25 36 00            lea rax, [rip + 0x362539]
00C2AD37  48 89 05 3A 25 36 00            mov qword ptr [rip + 0x36253a], rax
00C2AD3E  48 89 05 2B 25 36 00            mov qword ptr [rip + 0x36252b], rax
00C2AD45  48 8D 05 14 25 36 00            lea rax, [rip + 0x362514]
00C2AD4C  48 89 05 15 25 36 00            mov qword ptr [rip + 0x362515], rax
00C2AD53  48 89 05 06 25 36 00            mov qword ptr [rip + 0x362506], rax
00C2AD5A  48 8D 05 EF 24 36 00            lea rax, [rip + 0x3624ef]
00C2AD61  48 89 05 F0 24 36 00            mov qword ptr [rip + 0x3624f0], rax
00C2AD68  48 89 05 E1 24 36 00            mov qword ptr [rip + 0x3624e1], rax
00C2AD6F  48 8D 05 CA 24 36 00            lea rax, [rip + 0x3624ca]
00C2AD76  48 89 05 CB 24 36 00            mov qword ptr [rip + 0x3624cb], rax
00C2AD7D  48 89 05 BC 24 36 00            mov qword ptr [rip + 0x3624bc], rax
00C2AD84  48 8D 05 A5 24 36 00            lea rax, [rip + 0x3624a5]
00C2AD8B  48 89 05 A6 24 36 00            mov qword ptr [rip + 0x3624a6], rax
00C2AD92  48 89 05 97 24 36 00            mov qword ptr [rip + 0x362497], rax
00C2AD99  48 8D 05 80 24 36 00            lea rax, [rip + 0x362480]
00C2ADA0  48 89 05 81 24 36 00            mov qword ptr [rip + 0x362481], rax
00C2ADA7  48 89 05 72 24 36 00            mov qword ptr [rip + 0x362472], rax
00C2ADAE  48 8D 05 AB 26 36 00            lea rax, [rip + 0x3626ab]
00C2ADB5  48 89 05 AC 26 36 00            mov qword ptr [rip + 0x3626ac], rax
00C2ADBC  48 89 05 9D 26 36 00            mov qword ptr [rip + 0x36269d], rax
00C2ADC3  48 8D 05 86 26 36 00            lea rax, [rip + 0x362686]
00C2ADCA  48 89 05 87 26 36 00            mov qword ptr [rip + 0x362687], rax
00C2ADD1  48 89 05 78 26 36 00            mov qword ptr [rip + 0x362678], rax
00C2ADD8  48 8D 05 61 26 36 00            lea rax, [rip + 0x362661]
00C2ADDF  48 89 05 62 26 36 00            mov qword ptr [rip + 0x362662], rax
00C2ADE6  48 89 05 53 26 36 00            mov qword ptr [rip + 0x362653], rax
00C2ADED  4C 89 25 44 26 36 00            mov qword ptr [rip + 0x362644], r12
00C2ADF4  4C 89 25 05 4B 3A 00            mov qword ptr [rip + 0x3a4b05], r12
00C2ADFB  4C 89 25 2E 26 36 00            mov qword ptr [rip + 0x36262e], r12
00C2AE02  F3 0F 7F 05 16 26 36 00         movdqu xmmword ptr [rip + 0x362616], xmm0
00C2AE0A  44 89 25 03 26 36 00            mov dword ptr [rip + 0x362603], r12d
00C2AE11  0F 31                           rdtsc
00C2AE13  48 C1 E2 20                     shl rdx, 0x20
00C2AE17  45 8D 6C 24 01                  lea r13d, [r12 + 1]
00C2AE1C  48 0B C2                        or rax, rdx
00C2AE1F  44 89 25 EA 23 36 00            mov dword ptr [rip + 0x3623ea], r12d
00C2AE26  4C 8B C0                        mov r8, rax
00C2AE29  48 B8 15 AE 47 E1 7A 14 AE 47   movabs rax, 0x47ae147ae147ae15
00C2AE33  49 C1 E8 04                     shr r8, 4
00C2AE37  49 F7 E0                        mul r8
00C2AE3A  49 8B C8                        mov rcx, r8
00C2AE3D  41 8B C4                        mov eax, r12d
00C2AE40  48 2B CA                        sub rcx, rdx
00C2AE43  48 D1 E9                        shr rcx, 1
00C2AE46  48 03 CA                        add rcx, rdx
00C2AE49  48 C1 E9 06                     shr rcx, 6
00C2AE4D  48 6B C9 64                     imul rcx, rcx, 0x64
00C2AE51  4C 2B C1                        sub r8, rcx
00C2AE54  41 83 C0 0A                     add r8d, 0xa
00C2AE58  44 39 25 AD 25 36 00            cmp dword ptr [rip + 0x3625ad], r12d
00C2AE5F  44 89 05 AA 25 36 00            mov dword ptr [rip + 0x3625aa], r8d
00C2AE66  75 14                           jne 0x140c2ae7c
00C2AE68  C7 05 9A 25 36 00 0E 00 00 00   mov dword ptr [rip + 0x36259a], 0xe
00C2AE72  41 8B C5                        mov eax, r13d
00C2AE75  44 89 2D 94 23 36 00            mov dword ptr [rip + 0x362394], r13d
00C2AE7C  44 39 25 85 25 36 00            cmp dword ptr [rip + 0x362585], r12d
00C2AE83  BE 04 00 00 00                  mov esi, 4
00C2AE88  75 0F                           jne 0x140c2ae99
00C2AE8A  83 C8 02                        or eax, 2
00C2AE8D  89 35 75 25 36 00               mov dword ptr [rip + 0x362575], esi
00C2AE93  89 05 77 23 36 00               mov dword ptr [rip + 0x362377], eax
00C2AE99  8B 05 5D B2 23 00               mov eax, dword ptr [rip + 0x23b25d]
00C2AE9F  83 C0 FE                        add eax, -2
00C2AEA2  3D 2A 01 00 00                  cmp eax, 0x12a
00C2AEA7  76 0A                           jbe 0x140c2aeb3
00C2AEA9  C7 05 49 B2 23 00 2C 01 00 00   mov dword ptr [rip + 0x23b249], 0x12c
00C2AEB3  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00C2AEB7  E8 C4 FC AE FF                  call 0x14071ab80
00C2AEBC  0F B7 45 DE                     movzx eax, word ptr [rbp - 0x22]
00C2AEC0  48 8D 1D 39 FD 2C 00            lea rbx, [rip + 0x2cfd39]
00C2AEC7  41 BF 00 02 00 00               mov r15d, 0x200
00C2AECD  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00C2AED2  41 8B D7                        mov edx, r15d
00C2AED5  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
00C2AEDA  41 B9 49 63 70 20               mov r9d, 0x20706349
00C2AEE0  48 8D 0D 99 75 1E 00            lea rcx, [rip + 0x1e7599]
00C2AEE7  41 B8 38 00 00 00               mov r8d, 0x38
00C2AEED  E8 8A 36 F5 FF                  call 0x140b7e57c
00C2AEF2  0F B7 45 DC                     movzx eax, word ptr [rbp - 0x24]
00C2AEF6  48 8D 0D 03 76 1E 00            lea rcx, [rip + 0x1e7603]
00C2AEFD  44 8B 45 EC                     mov r8d, dword ptr [rbp - 0x14]
00C2AF01  41 B9 49 72 70 6C               mov r9d, 0x6c707249
00C2AF07  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00C2AF0C  41 8B D7                        mov edx, r15d
00C2AF0F  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
00C2AF14  E8 63 36 F5 FF                  call 0x140b7e57c
00C2AF19  0F B7 45 DA                     movzx eax, word ptr [rbp - 0x26]
00C2AF1D  48 8D 0D 5C 76 1E 00            lea rcx, [rip + 0x1e765c]
00C2AF24  44 8B 45 E8                     mov r8d, dword ptr [rbp - 0x18]
00C2AF28  41 B9 49 72 70 6D               mov r9d, 0x6d707249
00C2AF2E  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00C2AF33  41 8B D7                        mov edx, r15d
00C2AF36  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
00C2AF3B  E8 3C 36 F5 FF                  call 0x140b7e57c
00C2AF40  0F B7 45 D8                     movzx eax, word ptr [rbp - 0x28]
00C2AF44  48 8D 0D B5 76 1E 00            lea rcx, [rip + 0x1e76b5]
00C2AF4B  44 8B 45 E4                     mov r8d, dword ptr [rbp - 0x1c]
00C2AF4F  41 B9 49 72 70 73               mov r9d, 0x73707249
00C2AF55  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00C2AF5A  41 8B D7                        mov edx, r15d
00C2AF5D  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
00C2AF62  E8 15 36 F5 FF                  call 0x140b7e57c
00C2AF67  0F B7 45 E0                     movzx eax, word ptr [rbp - 0x20]
00C2AF6B  48 8D 0D 0E 77 1E 00            lea rcx, [rip + 0x1e770e]
00C2AF72  44 8B 45 F0                     mov r8d, dword ptr [rbp - 0x10]
00C2AF76  41 B9 4D 64 6C 20               mov r9d, 0x206c644d
00C2AF7C  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00C2AF81  41 8B D7                        mov edx, r15d
00C2AF84  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
00C2AF89  E8 EE 35 F5 FF                  call 0x140b7e57c
00C2AF8E  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00C2AF93  48 8D 0D 66 73 1E 00            lea rcx, [rip + 0x1e7366]
00C2AF9A  66 44 89 64 24 30               mov word ptr [rsp + 0x30], r12w
00C2AFA0  BB 00 02 00 00                  mov ebx, 0x200
00C2AFA5  41 BF 20 00 00 00               mov r15d, 0x20
00C2AFAB  C7 44 24 28 49 6F 55 73         mov dword ptr [rsp + 0x28], 0x73556f49
00C2AFB3  44 8B CB                        mov r9d, ebx
00C2AFB6  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C2AFBB  45 33 C0                        xor r8d, r8d
00C2AFBE  33 D2                           xor edx, edx
00C2AFC0  E8 5B D7 83 FF                  call 0x140468720
00C2AFC5  33 D2                           xor edx, edx
00C2AFC7  48 8D 0D B2 73 1E 00            lea rcx, [rip + 0x1e73b2]
00C2AFCE  41 B9 49 6F 53 69               mov r9d, 0x69536f49
00C2AFD4  41 B8 1E 01 00 00               mov r8d, 0x11e
00C2AFDA  E8 31 89 AE FF                  call 0x140713910
00C2AFDF  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00C2AFE4  48 8D 0D 15 74 1E 00            lea rcx, [rip + 0x1e7415]
00C2AFEB  66 44 89 64 24 30               mov word ptr [rsp + 0x30], r12w
00C2AFF1  44 8B CB                        mov r9d, ebx
00C2AFF4  C7 44 24 28 4F 70 43 74         mov dword ptr [rsp + 0x28], 0x7443704f
00C2AFFC  45 33 C0                        xor r8d, r8d
00C2AFFF  33 D2                           xor edx, edx
00C2B001  48 C7 44 24 20 30 00 00 00      mov qword ptr [rsp + 0x20], 0x30
00C2B00A  E8 11 D7 83 FF                  call 0x140468720
00C2B00F  B9 FF FF 00 00                  mov ecx, 0xffff
00C2B014  E8 D7 EE 61 FF                  call 0x140249ef0
00C2B019  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00C2B01E  8B D8                           mov ebx, eax
00C2B020  85 C0                           test eax, eax
00C2B022  74 26                           je 0x140c2b04a
00C2B024  41 8B CC                        mov ecx, r12d
00C2B027  48 8D 05 12 DC 39 00            lea rax, [rip + 0x39dc12]
00C2B02E  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
00C2B032  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00C2B036  E8 E1 F8 AE FF                  call 0x14071a91c
00C2B03B  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
00C2B03F  41 03 CD                        add ecx, r13d
00C2B042  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
00C2B046  3B CB                           cmp ecx, ebx
00C2B048  72 DD                           jb 0x140c2b027
00C2B04A  48 8D 05 1F 26 36 00            lea rax, [rip + 0x36261f]
00C2B051  4C 89 25 68 41 3A 00            mov qword ptr [rip + 0x3a4168], r12
00C2B058  48 89 05 19 26 36 00            mov qword ptr [rip + 0x362619], rax
00C2B05F  48 89 05 0A 26 36 00            mov qword ptr [rip + 0x36260a], rax
00C2B066  E8 65 1D 00 00                  call 0x140c2cdd0
00C2B06B  84 C0                           test al, al
00C2B06D  75 11                           jne 0x140c2b080
00C2B06F  44 89 2D 5A 28 36 00            mov dword ptr [rip + 0x36285a], r13d
00C2B076  B8 01 00 00 C0                  mov eax, 0xc0000001
00C2B07B  E9 65 0E 00 00                  jmp 0x140c2bee5
00C2B080  8B 05 8A 21 36 00               mov eax, dword ptr [rip + 0x36218a]
00C2B086  A8 03                           test al, 3
00C2B088  74 49                           je 0x140c2b0d3
00C2B08A  48 8D 0D 8F A3 84 FF            lea rcx, [rip - 0x7b5c71]
00C2B091  C7 05 C9 24 36 00 90 01 00 00   mov dword ptr [rip + 0x3624c9], 0x190
00C2B09B  0B C6                           or eax, esi
00C2B09D  48 89 0D 94 24 36 00            mov qword ptr [rip + 0x362494], rcx
00C2B0A4  89 05 66 21 36 00               mov dword ptr [rip + 0x362166], eax
00C2B0AA  C7 05 AC 24 36 00 D0 07 00 00   mov dword ptr [rip + 0x3624ac], 0x7d0
00C2B0B4  C7 05 62 24 36 00 13 01 00 00   mov dword ptr [rip + 0x362462], 0x113
00C2B0BE  4C 89 25 7B 24 36 00            mov qword ptr [rip + 0x36247b], r12
00C2B0C5  4C 89 25 8C 24 36 00            mov qword ptr [rip + 0x36248c], r12
00C2B0CC  4C 89 25 5D 24 36 00            mov qword ptr [rip + 0x36245d], r12
00C2B0D3  8B 05 EB F8 1D 00               mov eax, dword ptr [rip + 0x1df8eb]
00C2B0D9  B9 00 00 40 00                  mov ecx, 0x400000
00C2B0DE  3B C1                           cmp eax, ecx
00C2B0E0  72 08                           jb 0x140c2b0ea
00C2B0E2  8B C1                           mov eax, ecx
00C2B0E4  89 0D DA F8 1D 00               mov dword ptr [rip + 0x1df8da], ecx
00C2B0EA  3D 00 10 00 00                  cmp eax, 0x1000
00C2B0EF  77 0A                           ja 0x140c2b0fb
00C2B0F1  C7 05 C9 F8 1D 00 00 10 00 00   mov dword ptr [rip + 0x1df8c9], 0x1000
00C2B0FB  48 8D 05 E6 F2 3A 00            lea rax, [rip + 0x3af2e6]
00C2B102  C7 44 24 70 30 00 00 00         mov dword ptr [rsp + 0x70], 0x30
00C2B10A  0F 57 C0                        xorps xmm0, xmm0
00C2B10D  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00C2B111  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00C2B116  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
00C2B11B  BA 19 00 02 00                  mov edx, 0x20019
00C2B120  C7 45 88 40 02 00 00            mov dword ptr [rbp - 0x78], 0x240
00C2B127  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C2B12C  F3 0F 7F 45 90                  movdqu xmmword ptr [rbp - 0x70], xmm0
00C2B131  E8 DA 21 A8 FF                  call 0x1406ad310
00C2B136  85 C0                           test eax, eax
00C2B138  78 68                           js 0x140c2b1a2
00C2B13A  48 8D 15 2F E8 04 00            lea rdx, [rip + 0x4e82f]
00C2B141  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00C2B145  E8 36 F6 7F FF                  call 0x14042a780
00C2B14A  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2B14F  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00C2B154  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C2B159  4C 8D 0D 48 D7 3D 00            lea r9, [rip + 0x3dd748]
00C2B160  41 B8 02 00 00 00               mov r8d, 2
00C2B166  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
00C2B16B  48 8D 55 A0                     lea rdx, [rbp - 0x60]
00C2B16F  E8 8C 78 C8 FF                  call 0x1408b2a00
00C2B174  85 C0                           test eax, eax
00C2B176  78 13                           js 0x140c2b18b
00C2B178  39 35 2E D7 3D 00               cmp dword ptr [rip + 0x3dd72e], esi
00C2B17E  75 0B                           jne 0x140c2b18b
00C2B180  39 35 2E D7 3D 00               cmp dword ptr [rip + 0x3dd72e], esi
00C2B186  0F 94 C0                        sete al
00C2B189  EB 03                           jmp 0x140c2b18e
00C2B18B  41 8A C5                        mov al, r13b
00C2B18E  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2B193  33 D2                           xor edx, edx
00C2B195  88 05 BF 1E 36 00               mov byte ptr [rip + 0x361ebf], al
00C2B19B  E8 D0 66 C7 FF                  call 0x1408a1870
00C2B1A0  EB 07                           jmp 0x140c2b1a9
00C2B1A2  44 88 2D B1 1E 36 00            mov byte ptr [rip + 0x361eb1], r13b
00C2B1A9  48 8D 05 60 23 36 00            lea rax, [rip + 0x362360]
00C2B1B0  4C 89 25 C9 22 36 00            mov qword ptr [rip + 0x3622c9], r12
00C2B1B7  48 89 05 5A 23 36 00            mov qword ptr [rip + 0x36235a], rax
00C2B1BE  41 BF 08 00 00 00               mov r15d, 8
00C2B1C4  48 89 05 45 23 36 00            mov qword ptr [rip + 0x362345], rax
00C2B1CB  48 8D 05 2E 87 77 FF            lea rax, [rip - 0x8878d2]
00C2B1D2  48 89 05 FF 22 36 00            mov qword ptr [rip + 0x3622ff], rax
00C2B1D9  48 8D 05 20 23 36 00            lea rax, [rip + 0x362320]
00C2B1E0  48 89 05 F9 22 36 00            mov qword ptr [rip + 0x3622f9], rax
00C2B1E7  48 8D 05 9A 22 36 00            lea rax, [rip + 0x36229a]
00C2B1EE  48 89 05 9B 22 36 00            mov qword ptr [rip + 0x36229b], rax
00C2B1F5  48 89 05 8C 22 36 00            mov qword ptr [rip + 0x36228c], rax
00C2B1FC  48 8D 05 6D 22 36 00            lea rax, [rip + 0x36226d]
00C2B203  48 89 05 6E 22 36 00            mov qword ptr [rip + 0x36226e], rax
00C2B20A  48 89 05 5F 22 36 00            mov qword ptr [rip + 0x36225f], rax
00C2B211  48 8D 05 78 04 AF FF            lea rax, [rip - 0x50fb88]
00C2B218  48 89 05 71 25 36 00            mov qword ptr [rip + 0x362571], rax
00C2B21F  48 8D 05 7A 25 36 00            lea rax, [rip + 0x36257a]
00C2B226  48 89 05 7B 25 36 00            mov qword ptr [rip + 0x36257b], rax
00C2B22D  48 89 05 6C 25 36 00            mov qword ptr [rip + 0x36256c], rax
00C2B234  48 8D 05 85 25 36 00            lea rax, [rip + 0x362585]
00C2B23B  48 89 05 86 25 36 00            mov qword ptr [rip + 0x362586], rax
00C2B242  48 89 05 77 25 36 00            mov qword ptr [rip + 0x362577], rax
00C2B249  8B 05 6D F7 1D 00               mov eax, dword ptr [rip + 0x1df76d]
00C2B24F  05 18 FC FF FF                  add eax, 0xfffffc18
00C2B254  4C 89 25 E5 3E 3A 00            mov qword ptr [rip + 0x3a3ee5], r12
00C2B25B  C7 05 5B 22 36 00 13 01 00 00   mov dword ptr [rip + 0x36225b], 0x113
00C2B265  4C 89 25 8C 22 36 00            mov qword ptr [rip + 0x36228c], r12
00C2B26C  4C 89 25 5D 22 36 00            mov qword ptr [rip + 0x36225d], r12
00C2B273  C6 05 06 22 36 00 09            mov byte ptr [rip + 0x362206], 9
00C2B27A  4C 89 25 17 22 36 00            mov qword ptr [rip + 0x362217], r12
00C2B281  44 89 25 34 22 36 00            mov dword ptr [rip + 0x362234], r12d
00C2B288  66 44 89 25 28 22 36 00         mov word ptr [rip + 0x362228], r12w
00C2B290  4C 89 25 01 25 36 00            mov qword ptr [rip + 0x362501], r12
00C2B297  4C 89 25 E2 24 36 00            mov qword ptr [rip + 0x3624e2], r12
00C2B29E  4C 89 25 0B 25 36 00            mov qword ptr [rip + 0x36250b], r12
00C2B2A5  C6 05 0C 25 36 00 05            mov byte ptr [rip + 0x36250c], 5
00C2B2AC  44 88 3D 07 25 36 00            mov byte ptr [rip + 0x362507], r15b
00C2B2B3  44 89 25 02 25 36 00            mov dword ptr [rip + 0x362502], r12d
00C2B2BA  C7 05 0C 25 36 00 FF FF FF 7F   mov dword ptr [rip + 0x36250c], 0x7fffffff
00C2B2C4  44 88 25 0D 25 36 00            mov byte ptr [rip + 0x36250d], r12b
00C2B2CB  3D 28 23 00 00                  cmp eax, 0x2328
00C2B2D0  76 0A                           jbe 0x140c2b2dc
00C2B2D2  C7 05 E0 F6 1D 00 88 13 00 00   mov dword ptr [rip + 0x1df6e0], 0x1388
00C2B2DC  48 8D 05 ED 9C 86 FF            lea rax, [rip - 0x796313]
00C2B2E3  4C 89 25 2E 24 36 00            mov qword ptr [rip + 0x36242e], r12
00C2B2EA  48 89 05 1F 24 36 00            mov qword ptr [rip + 0x36241f], rax
00C2B2F1  48 8D 15 48 E6 04 00            lea rdx, [rip + 0x4e648]
00C2B2F8  48 8D 05 21 24 36 00            lea rax, [rip + 0x362421]
00C2B2FF  4C 89 25 FA 23 36 00            mov qword ptr [rip + 0x3623fa], r12
00C2B306  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00C2B30A  48 89 05 17 24 36 00            mov qword ptr [rip + 0x362417], rax
00C2B311  48 89 05 08 24 36 00            mov qword ptr [rip + 0x362408], rax
00C2B318  4C 89 25 11 24 36 00            mov qword ptr [rip + 0x362411], r12
00C2B31F  44 88 25 32 24 36 00            mov byte ptr [rip + 0x362432], r12b
00C2B326  44 88 2D 2E 1D 36 00            mov byte ptr [rip + 0x361d2e], r13b
00C2B32D  E8 4E F4 7F FF                  call 0x14042a780
00C2B332  48 8D 45 A0                     lea rax, [rbp - 0x60]
00C2B336  C7 44 24 70 30 00 00 00         mov dword ptr [rsp + 0x70], 0x30
00C2B33E  0F 57 C0                        xorps xmm0, xmm0
00C2B341  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00C2B345  45 33 C9                        xor r9d, r9d
00C2B348  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
00C2B34D  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00C2B352  C7 45 88 10 02 00 00            mov dword ptr [rbp - 0x78], 0x210
00C2B359  BA 03 00 1F 00                  mov edx, 0x1f0003
00C2B35E  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
00C2B363  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C2B368  F3 0F 7F 45 90                  movdqu xmmword ptr [rbp - 0x70], xmm0
00C2B36D  E8 CE DD C8 FF                  call 0x1408b9140
00C2B372  8B D8                           mov ebx, eax
00C2B374  85 C0                           test eax, eax
00C2B376  79 1A                           jns 0x140c2b392
00C2B378  33 D2                           xor edx, edx
00C2B37A  8B CE                           mov ecx, esi
00C2B37C  E8 6B CA 88 FF                  call 0x1404b7dec
00C2B381  C7 05 45 25 36 00 1A 00 00 00   mov dword ptr [rip + 0x362545], 0x1a
00C2B38B  8B C3                           mov eax, ebx
00C2B38D  E9 53 0B 00 00                  jmp 0x140c2bee5
00C2B392  4C 8B 05 E7 B7 39 00            mov r8, qword ptr [rip + 0x39b7e7]
00C2B399  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00C2B39E  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2B3A3  45 33 C9                        xor r9d, r9d
00C2B3A6  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00C2B3AB  33 D2                           xor edx, edx
00C2B3AD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C2B3B2  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
00C2B3B7  E8 F4 D9 C3 FF                  call 0x140868db0
00C2B3BC  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00C2B3C1  BB 06 00 00 00                  mov ebx, 6
00C2B3C6  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2B3CB  33 D2                           xor edx, edx
00C2B3CD  48 89 05 B4 EB 3A 00            mov qword ptr [rip + 0x3aebb4], rax
00C2B3D4  48 8D 05 0D 23 36 00            lea rax, [rip + 0x36230d]
00C2B3DB  48 89 05 0E 23 36 00            mov qword ptr [rip + 0x36230e], rax
00C2B3E2  48 89 05 FF 22 36 00            mov qword ptr [rip + 0x3622ff], rax
00C2B3E9  48 8D 05 D8 22 36 00            lea rax, [rip + 0x3622d8]
00C2B3F0  48 89 05 D9 22 36 00            mov qword ptr [rip + 0x3622d9], rax
00C2B3F7  48 89 05 CA 22 36 00            mov qword ptr [rip + 0x3622ca], rax
00C2B3FE  48 8D 05 83 22 36 00            lea rax, [rip + 0x362283]
00C2B405  48 89 05 84 22 36 00            mov qword ptr [rip + 0x362284], rax
00C2B40C  48 89 05 75 22 36 00            mov qword ptr [rip + 0x362275], rax
00C2B413  66 44 89 25 C5 22 36 00         mov word ptr [rip + 0x3622c5], r12w
00C2B41B  88 1D C1 22 36 00               mov byte ptr [rip + 0x3622c1], bl
00C2B421  44 89 25 BC 22 36 00            mov dword ptr [rip + 0x3622bc], r12d
00C2B428  66 44 89 25 90 22 36 00         mov word ptr [rip + 0x362290], r12w
00C2B430  88 1D 8C 22 36 00               mov byte ptr [rip + 0x36228c], bl
00C2B436  44 89 25 87 22 36 00            mov dword ptr [rip + 0x362287], r12d
00C2B43D  66 44 89 2D 3B 22 36 00         mov word ptr [rip + 0x36223b], r13w
00C2B445  88 1D 37 22 36 00               mov byte ptr [rip + 0x362237], bl
00C2B44B  44 89 2D 32 22 36 00            mov dword ptr [rip + 0x362232], r13d
00C2B452  E8 19 64 C7 FF                  call 0x1408a1870
00C2B457  E8 CC 12 00 00                  call 0x140c2c728
00C2B45C  84 C0                           test al, al
00C2B45E  75 18                           jne 0x140c2b478
00C2B460  33 D2                           xor edx, edx
00C2B462  8B CB                           mov ecx, ebx
00C2B464  E8 83 C9 88 FF                  call 0x1404b7dec
00C2B469  C7 05 5D 24 36 00 03 00 00 00   mov dword ptr [rip + 0x36245d], 3
00C2B473  E9 FE FB FF FF                  jmp 0x140c2b076
00C2B478  E8 CB 2D 00 00                  call 0x140c2e248
00C2B47D  85 C0                           test eax, eax
00C2B47F  79 0F                           jns 0x140c2b490
00C2B481  C7 05 45 24 36 00 0F 00 00 00   mov dword ptr [rip + 0x362445], 0xf
00C2B48B  E9 55 0A 00 00                  jmp 0x140c2bee5
00C2B490  33 D2                           xor edx, edx
00C2B492  48 8B CF                        mov rcx, rdi
00C2B495  E8 FE 3D 00 00                  call 0x140c2f298
00C2B49A  8B D8                           mov ebx, eax
00C2B49C  85 C0                           test eax, eax
00C2B49E  79 15                           jns 0x140c2b4b5
00C2B4A0  33 D2                           xor edx, edx
00C2B4A2  8D 4A 07                        lea ecx, [rdx + 7]
00C2B4A5  E8 42 C9 88 FF                  call 0x1404b7dec
00C2B4AA  89 35 20 24 36 00               mov dword ptr [rip + 0x362420], esi
00C2B4B0  E9 D6 FE FF FF                  jmp 0x140c2b38b
00C2B4B5  45 85 F6                        test r14d, r14d
00C2B4B8  74 0B                           je 0x140c2b4c5
00C2B4BA  41 8B CF                        mov ecx, r15d
00C2B4BD  41 8B D5                        mov edx, r13d
00C2B4C0  E8 3B B3 BA FF                  call 0x1407d6800
00C2B4C5  33 D2                           xor edx, edx
00C2B4C7  48 8B CF                        mov rcx, rdi
00C2B4CA  E8 DD 00 01 00                  call 0x140c3b5ac
00C2B4CF  E8 B8 1B 01 00                  call 0x140c3d08c
00C2B4D4  48 8B 05 B5 51 1D 00            mov rax, qword ptr [rip + 0x1d51b5]
00C2B4DB  E8 F0 F5 A8 FF                  call 0x1406baad0
00C2B4E0  48 8B 05 51 0F 36 00            mov rax, qword ptr [rip + 0x360f51]
00C2B4E7  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00C2B4EB  48 85 C9                        test rcx, rcx
00C2B4EE  74 2F                           je 0x140c2b51f
00C2B4F0  8B 81 2C 01 00 00               mov eax, dword ptr [rcx + 0x12c]
00C2B4F6  2D 09 03 00 00                  sub eax, 0x309
00C2B4FB  41 3B C5                        cmp eax, r13d
00C2B4FE  77 0C                           ja 0x140c2b50c
00C2B500  F7 81 8C 01 00 00 00 10 00 00   test dword ptr [rcx + 0x18c], 0x1000
00C2B50A  74 05                           je 0x140c2b511
00C2B50C  48 8B 09                        mov rcx, qword ptr [rcx]
00C2B50F  EB DA                           jmp 0x140c2b4eb
00C2B511  8B D6                           mov edx, esi
00C2B513  48 89 0D 76 D1 3D 00            mov qword ptr [rip + 0x3dd176], rcx
00C2B51A  E8 29 0B CD FF                  call 0x1408fc048
00C2B51F  48 8B D7                        mov rdx, rdi
00C2B522  33 C9                           xor ecx, ecx
00C2B524  E8 3B 1D 02 00                  call 0x140c4d264
00C2B529  84 C0                           test al, al
00C2B52B  75 0F                           jne 0x140c2b53c
00C2B52D  C7 05 99 23 36 00 12 00 00 00   mov dword ptr [rip + 0x362399], 0x12
00C2B537  E9 3A FB FF FF                  jmp 0x140c2b076
00C2B53C  45 85 F6                        test r14d, r14d
00C2B53F  74 0D                           je 0x140c2b54e
00C2B541  41 8B CF                        mov ecx, r15d
00C2B544  BA 02 00 00 00                  mov edx, 2
00C2B549  E8 B2 B2 BA FF                  call 0x1407d6800
00C2B54E  E8 85 3C BB FF                  call 0x1407df1d8
00C2B553  8A D8                           mov bl, al
00C2B555  E8 06 10 E1 FF                  call 0x140a3c560
00C2B55A  8A C8                           mov cl, al
00C2B55C  8A D3                           mov dl, bl
00C2B55E  48 FF 15 13 5E 52 FF            call qword ptr [rip - 0xada1ed]
00C2B565  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00C2B56A  BA 00 00 00 80                  mov edx, 0x80000000
00C2B56F  8D 0C 10                        lea ecx, [rax + rdx]
00C2B572  85 CA                           test edx, ecx
00C2B574  75 16                           jne 0x140c2b58c
00C2B576  3D BB 00 00 C0                  cmp eax, 0xc00000bb
00C2B57B  74 0F                           je 0x140c2b58c
00C2B57D  C7 05 49 23 36 00 13 00 00 00   mov dword ptr [rip + 0x362349], 0x13
00C2B587  E9 59 09 00 00                  jmp 0x140c2bee5
00C2B58C  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00C2B591  44 89 64 24 58                  mov dword ptr [rsp + 0x58], r12d
00C2B596  E8 D5 AC 80 FF                  call 0x140436270
00C2B59B  84 C0                           test al, al
00C2B59D  74 46                           je 0x140c2b5e5
00C2B59F  44 39 6C 24 58                  cmp dword ptr [rsp + 0x58], r13d
00C2B5A4  75 3F                           jne 0x140c2b5e5
00C2B5A6  BA 00 10 00 00                  mov edx, 0x1000
00C2B5AB  44 88 2D A6 1A 36 00            mov byte ptr [rip + 0x361aa6], r13b
00C2B5B2  B9 00 01 00 00                  mov ecx, 0x100
00C2B5B7  41 B8 41 63 44 6E               mov r8d, 0x6e446341
00C2B5BD  E8 2E 6B F5 FF                  call 0x140b820f0
00C2B5C2  48 85 C0                        test rax, rax
00C2B5C5  75 14                           jne 0x140c2b5db
00C2B5C7  C7 05 FF 22 36 00 11 00 00 00   mov dword ptr [rip + 0x3622ff], 0x11
00C2B5D1  B8 17 00 00 C0                  mov eax, 0xc0000017
00C2B5D6  E9 0A 09 00 00                  jmp 0x140c2bee5
00C2B5DB  4C 8B C0                        mov r8, rax
00C2B5DE  E8 51 78 AF FF                  call 0x140722e34
00C2B5E3  EB 07                           jmp 0x140c2b5ec
00C2B5E5  44 88 25 6C 1A 36 00            mov byte ptr [rip + 0x361a6c], r12b
00C2B5EC  48 8B D7                        mov rdx, rdi
00C2B5EF  41 8B CD                        mov ecx, r13d
00C2B5F2  E8 49 97 B8 FF                  call 0x1407b4d40
00C2B5F7  4C 8D 0D E2 21 36 00            lea r9, [rip + 0x3621e2]
00C2B5FE  45 33 C0                        xor r8d, r8d
00C2B601  48 8D 15 48 FE AE FF            lea rdx, [rip - 0x5101b8]
00C2B608  48 8D 0D 19 7F 3F FF            lea rcx, [rip - 0xc080e7]
00C2B60F  E8 4C 53 CF FF                  call 0x140920960
00C2B614  85 C0                           test eax, eax
00C2B616  79 10                           jns 0x140c2b628
00C2B618  BE 10 00 00 00                  mov esi, 0x10
00C2B61D  89 35 AD 22 36 00               mov dword ptr [rip + 0x3622ad], esi
00C2B623  E9 BD 08 00 00                  jmp 0x140c2bee5
00C2B628  4C 8D 0D F1 B7 1D 00            lea r9, [rip + 0x1db7f1]
00C2B62F  4C 8D 05 EA B7 1D 00            lea r8, [rip + 0x1db7ea]
00C2B636  48 8D 0D EB 5F 3F FF            lea rcx, [rip - 0xc0a015]
00C2B63D  E8 C2 38 95 FF                  call 0x14057ef04
00C2B642  85 C0                           test eax, eax
00C2B644  79 0F                           jns 0x140c2b655
00C2B646  C7 05 80 22 36 00 0B 00 00 00   mov dword ptr [rip + 0x362280], 0xb
00C2B650  E9 90 08 00 00                  jmp 0x140c2bee5
00C2B655  48 8D 1D FC E9 1D 00            lea rbx, [rip + 0x1de9fc]
00C2B65C  45 33 C0                        xor r8d, r8d
00C2B65F  48 8B CB                        mov rcx, rbx
00C2B662  48 8D 15 A7 AE E8 FF            lea rdx, [rip - 0x175159]
00C2B669  E8 26 04 EB FF                  call 0x140adba94
00C2B66E  85 C0                           test eax, eax
00C2B670  79 0F                           jns 0x140c2b681
00C2B672  C7 05 54 22 36 00 16 00 00 00   mov dword ptr [rip + 0x362254], 0x16
00C2B67C  E9 64 08 00 00                  jmp 0x140c2bee5
00C2B681  48 89 1D 90 BF 20 00            mov qword ptr [rip + 0x20bf90], rbx
00C2B688  8B 05 32 4C 20 00               mov eax, dword ptr [rip + 0x204c32]
00C2B68E  85 C0                           test eax, eax
00C2B690  74 0D                           je 0x140c2b69f
00C2B692  45 33 C0                        xor r8d, r8d
00C2B695  83 CA FF                        or edx, 0xffffffff
00C2B698  33 C9                           xor ecx, ecx
00C2B69A  E8 A1 5A 6C FF                  call 0x1402f1140
00C2B69F  4C 8D 0D 4A A8 23 00            lea r9, [rip + 0x23a84a]
00C2B6A6  45 33 C0                        xor r8d, r8d
00C2B6A9  48 8D 15 20 9D 96 FF            lea rdx, [rip - 0x6962e0]
00C2B6B0  48 8D 0D 49 65 3F FF            lea rcx, [rip - 0xc09ab7]
00C2B6B7  E8 A4 52 CF FF                  call 0x140920960
00C2B6BC  45 33 C0                        xor r8d, r8d
00C2B6BF  48 8D 0D 22 B7 1D 00            lea rcx, [rip + 0x1db722]
00C2B6C6  33 D2                           xor edx, edx
00C2B6C8  E8 D3 51 CF FF                  call 0x1409208a0
00C2B6CD  41 8A CD                        mov cl, r13b
00C2B6D0  E8 6F ED AE FF                  call 0x14071a444
00C2B6D5  48 8D 0D 8C B7 1D 00            lea rcx, [rip + 0x1db78c]
00C2B6DC  E8 8B 9B AD FF                  call 0x14070526c
00C2B6E1  48 8B 8F F0 00 00 00            mov rcx, qword ptr [rdi + 0xf0]
00C2B6E8  48 8B 89 40 0B 00 00            mov rcx, qword ptr [rcx + 0xb40]
00C2B6EF  E8 80 2C B7 FF                  call 0x14079e374
00C2B6F4  41 8B CD                        mov ecx, r13d
00C2B6F7  E8 D8 34 FC FF                  call 0x140beebd4
00C2B6FC  33 D2                           xor edx, edx
00C2B6FE  4C 8D 05 DB BE 31 00            lea r8, [rip + 0x31bedb]
00C2B705  8D 4A 02                        lea ecx, [rdx + 2]
00C2B708  48 FF 15 A9 5F 52 FF            call qword ptr [rip - 0xada057]
00C2B70F  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00C2B714  B9 02 00 00 00                  mov ecx, 2
00C2B719  E8 42 5F 04 00                  call 0x140c71660
00C2B71E  44 38 25 35 19 36 00            cmp byte ptr [rip + 0x361935], r12b
00C2B725  75 60                           jne 0x140c2b787
00C2B727  48 8D 0D 92 3A 3A 00            lea rcx, [rip + 0x3a3a92]
00C2B72E  E8 3D CD 5D FF                  call 0x140208470
00C2B733  8A D8                           mov bl, al
00C2B735  48 8D 05 34 1F 36 00            lea rax, [rip + 0x361f34]
00C2B73C  48 39 05 2D 1F 36 00            cmp qword ptr [rip + 0x361f2d], rax
00C2B743  75 09                           jne 0x140c2b74e
00C2B745  44 88 25 0F 19 36 00            mov byte ptr [rip + 0x36190f], r12b
00C2B74C  EB 2B                           jmp 0x140c2b779
00C2B74E  48 8D 05 2B 25 E3 FF            lea rax, [rip - 0x1cdad5]
00C2B755  4C 89 25 1C 19 36 00            mov qword ptr [rip + 0x36191c], r12
00C2B75C  41 8B D5                        mov edx, r13d
00C2B75F  48 89 05 0A 19 36 00            mov qword ptr [rip + 0x36190a], rax
00C2B766  48 8D 0D F3 18 36 00            lea rcx, [rip + 0x3618f3]
00C2B76D  4C 89 25 EC 18 36 00            mov qword ptr [rip + 0x3618ec], r12
00C2B774  E8 A7 DD 6C FF                  call 0x1402f9520
00C2B779  8A D3                           mov dl, bl
00C2B77B  48 8D 0D 3E 3A 3A 00            lea rcx, [rip + 0x3a3a3e]
00C2B782  E8 19 74 76 FF                  call 0x140392ba0
00C2B787  45 85 F6                        test r14d, r14d
00C2B78A  74 0D                           je 0x140c2b799
00C2B78C  41 8B CF                        mov ecx, r15d
00C2B78F  BA 03 00 00 00                  mov edx, 3
00C2B794  E8 67 B0 BA FF                  call 0x1407d6800
00C2B799  BE 10 00 00 00                  mov esi, 0x10
00C2B79E  40 84 35 2F 21 36 00            test byte ptr [rip + 0x36212f], sil
00C2B7A5  74 16                           je 0x140c2b7bd
00C2B7A7  45 33 C9                        xor r9d, r9d
00C2B7AA  48 8D 15 07 73 3F FF            lea rdx, [rip - 0xc08cf9]
00C2B7B1  48 8D 0D 68 B6 1D 00            lea rcx, [rip + 0x1db668]
00C2B7B8  E8 AB B3 96 FF                  call 0x140596b68
00C2B7BD  33 D2                           xor edx, edx
00C2B7BF  48 8B CF                        mov rcx, rdi
00C2B7C2  E8 41 94 02 00                  call 0x140c54c08
00C2B7C7  40 84 35 06 21 36 00            test byte ptr [rip + 0x362106], sil
00C2B7CE  74 13                           je 0x140c2b7e3
00C2B7D0  48 8D 15 41 58 3F FF            lea rdx, [rip - 0xc0a7bf]
00C2B7D7  48 8D 0D 42 B6 1D 00            lea rcx, [rip + 0x1db642]
00C2B7DE  E8 41 B3 96 FF                  call 0x140596b24
00C2B7E3  45 85 F6                        test r14d, r14d
00C2B7E6  74 0D                           je 0x140c2b7f5
00C2B7E8  41 8B CF                        mov ecx, r15d
00C2B7EB  BA 04 00 00 00                  mov edx, 4
00C2B7F0  E8 0B B0 BA FF                  call 0x1407d6800
00C2B7F5  48 8B CF                        mov rcx, rdi
00C2B7F8  E8 C7 1B 00 00                  call 0x140c2d3c4
00C2B7FD  85 C0                           test eax, eax
00C2B7FF  79 0F                           jns 0x140c2b810
00C2B801  C7 05 C5 20 36 00 14 00 00 00   mov dword ptr [rip + 0x3620c5], 0x14
00C2B80B  E9 D5 06 00 00                  jmp 0x140c2bee5
00C2B810  41 8B D5                        mov edx, r13d
00C2B813  48 8B CF                        mov rcx, rdi
00C2B816  E8 7D 3A 00 00                  call 0x140c2f298
00C2B81B  8B D8                           mov ebx, eax
00C2B81D  85 C0                           test eax, eax
00C2B81F  79 19                           jns 0x140c2b83a
00C2B821  33 D2                           xor edx, edx
00C2B823  41 8B CF                        mov ecx, r15d
00C2B826  E8 C1 C5 88 FF                  call 0x1404b7dec
00C2B82B  C7 05 9B 20 36 00 05 00 00 00   mov dword ptr [rip + 0x36209b], 5
00C2B835  E9 51 FB FF FF                  jmp 0x140c2b38b
00C2B83A  33 D2                           xor edx, edx
00C2B83C  48 8D 1D BD 1F 36 00            lea rbx, [rip + 0x361fbd]
00C2B843  48 8B CB                        mov rcx, rbx
00C2B846  44 8D 42 68                     lea r8d, [rdx + 0x68]
00C2B84A  E8 F1 B3 A9 FF                  call 0x1406c6c40
00C2B84F  48 8D 05 0A D5 D7 FF            lea rax, [rip - 0x282af6]
00C2B856  48 89 1D A3 1F 36 00            mov qword ptr [rip + 0x361fa3], rbx
00C2B85D  48 89 05 E4 1F 36 00            mov qword ptr [rip + 0x361fe4], rax
00C2B864  BB 06 00 00 00                  mov ebx, 6
00C2B869  48 8D 05 C0 F4 AE FF            lea rax, [rip - 0x510b40]
00C2B870  4C 89 25 E9 1F 36 00            mov qword ptr [rip + 0x361fe9], r12
00C2B877  48 89 05 D2 1F 36 00            mov qword ptr [rip + 0x361fd2], rax
00C2B87E  48 8B CF                        mov rcx, rdi
00C2B881  48 8D 05 F8 FB AE FF            lea rax, [rip - 0x510408]
00C2B888  44 89 2D F1 1F 36 00            mov dword ptr [rip + 0x361ff1], r13d
00C2B88F  48 89 05 C2 1F 36 00            mov qword ptr [rip + 0x361fc2], rax
00C2B896  48 8D 05 03 20 36 00            lea rax, [rip + 0x362003]
00C2B89D  48 89 05 04 20 36 00            mov qword ptr [rip + 0x362004], rax
00C2B8A4  48 89 05 F5 1F 36 00            mov qword ptr [rip + 0x361ff5], rax
00C2B8AB  4C 89 25 D6 1F 36 00            mov qword ptr [rip + 0x361fd6], r12
00C2B8B2  44 89 25 D7 1F 36 00            mov dword ptr [rip + 0x361fd7], r12d
00C2B8B9  66 44 89 2D D7 1F 36 00         mov word ptr [rip + 0x361fd7], r13w
00C2B8C1  88 1D D3 1F 36 00               mov byte ptr [rip + 0x361fd3], bl
00C2B8C7  44 89 25 CE 1F 36 00            mov dword ptr [rip + 0x361fce], r12d
00C2B8CE  E8 F5 86 02 00                  call 0x140c53fc8
00C2B8D3  4C 8D 0D 06 CD 23 00            lea r9, [rip + 0x23cd06]
00C2B8DA  45 33 C0                        xor r8d, r8d
00C2B8DD  33 D2                           xor edx, edx
00C2B8DF  48 8D 0D 12 74 3F FF            lea rcx, [rip - 0xc08bee]
00C2B8E6  E8 75 50 CF FF                  call 0x140920960
00C2B8EB  85 C0                           test eax, eax
00C2B8ED  79 07                           jns 0x140c2b8f6
00C2B8EF  4C 89 25 EA CC 23 00            mov qword ptr [rip + 0x23ccea], r12
00C2B8F6  41 8B D5                        mov edx, r13d
00C2B8F9  48 8B CF                        mov rcx, rdi
00C2B8FC  E8 AB FC 00 00                  call 0x140c3b5ac
00C2B901  48 8B CF                        mov rcx, rdi
00C2B904  E8 97 85 95 FF                  call 0x140583ea0
00C2B909  85 C0                           test eax, eax
00C2B90B  79 0F                           jns 0x140c2b91c
00C2B90D  C7 05 B9 1F 36 00 17 00 00 00   mov dword ptr [rip + 0x361fb9], 0x17
00C2B917  E9 C9 05 00 00                  jmp 0x140c2bee5
00C2B91C  45 85 F6                        test r14d, r14d
00C2B91F  74 0D                           je 0x140c2b92e
00C2B921  41 8B CF                        mov ecx, r15d
00C2B924  BA 05 00 00 00                  mov edx, 5
00C2B929  E8 D2 AE BA FF                  call 0x1407d6800
00C2B92E  33 C9                           xor ecx, ecx
00C2B930  E8 27 30 99 FF                  call 0x1405be95c
00C2B935  E8 6A 92 01 00                  call 0x140c44ba4
00C2B93A  E8 A1 41 96 FF                  call 0x14058fae0
00C2B93F  B9 02 00 00 00                  mov ecx, 2
00C2B944  E8 8B 32 FC FF                  call 0x140beebd4
00C2B949  48 8B CF                        mov rcx, rdi
00C2B94C  E8 23 6B F4 FF                  call 0x140b72474
00C2B951  45 85 F6                        test r14d, r14d
00C2B954  74 0A                           je 0x140c2b960
00C2B956  41 8B CF                        mov ecx, r15d
00C2B959  8B D3                           mov edx, ebx
00C2B95B  E8 A0 AE BA FF                  call 0x1407d6800
00C2B960  48 8B 0D 71 A9 23 00            mov rcx, qword ptr [rip + 0x23a971]
00C2B967  48 85 C9                        test rcx, rcx
00C2B96A  74 1B                           je 0x140c2b987
00C2B96C  45 33 C9                        xor r9d, r9d
00C2B96F  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C2B974  4C 8D 05 75 F0 1D 00            lea r8, [rip + 0x1df075]
00C2B97B  48 8D 15 7E BA 3F FF            lea rdx, [rip - 0xc04582]
00C2B982  E8 29 BC E8 FF                  call 0x140ab75b0
00C2B987  48 8D 05 32 13 36 00            lea rax, [rip + 0x361332]
00C2B98E  66 44 89 2D 0A 13 36 00         mov word ptr [rip + 0x36130a], r13w
00C2B996  48 89 05 2B 13 36 00            mov qword ptr [rip + 0x36132b], rax
00C2B99D  48 89 05 1C 13 36 00            mov qword ptr [rip + 0x36131c], rax
00C2B9A4  48 8D 05 FD 12 36 00            lea rax, [rip + 0x3612fd]
00C2B9AB  48 89 05 FE 12 36 00            mov qword ptr [rip + 0x3612fe], rax
00C2B9B2  48 89 05 EF 12 36 00            mov qword ptr [rip + 0x3612ef], rax
00C2B9B9  88 1D E3 12 36 00               mov byte ptr [rip + 0x3612e3], bl
00C2B9BF  44 89 2D DE 12 36 00            mov dword ptr [rip + 0x3612de], r13d
00C2B9C6  E8 E9 01 B0 FF                  call 0x14072bbb4
00C2B9CB  0F B6 15 2F F0 1D 00            movzx edx, byte ptr [rip + 0x1df02f]
00C2B9D2  48 8D 05 B7 12 36 00            lea rax, [rip + 0x3612b7]
00C2B9D9  48 8D 0D 60 12 36 00            lea rcx, [rip + 0x361260]
00C2B9E0  48 89 05 B1 12 36 00            mov qword ptr [rip + 0x3612b1], rax
00C2B9E7  48 89 05 A2 12 36 00            mov qword ptr [rip + 0x3612a2], rax
00C2B9EE  4C 89 25 8B 12 36 00            mov qword ptr [rip + 0x36128b], r12
00C2B9F5  E8 96 52 85 FF                  call 0x140480c90
00C2B9FA  E8 99 00 B0 FF                  call 0x14072ba98
00C2B9FF  85 C0                           test eax, eax
00C2BA01  79 0F                           jns 0x140c2ba12
00C2BA03  C7 05 C3 1E 36 00 18 00 00 00   mov dword ptr [rip + 0x361ec3], 0x18
00C2BA0D  E9 D3 04 00 00                  jmp 0x140c2bee5
00C2BA12  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00C2BA17  E8 60 77 97 FF                  call 0x1405a317c
00C2BA1C  44 38 25 99 A6 23 00            cmp byte ptr [rip + 0x23a699], r12b
00C2BA23  75 17                           jne 0x140c2ba3c
00C2BA25  44 38 64 24 40                  cmp byte ptr [rsp + 0x40], r12b
00C2BA2A  75 10                           jne 0x140c2ba3c
00C2BA2C  44 38 25 87 EF 1D 00            cmp byte ptr [rip + 0x1def87], r12b
00C2BA33  74 07                           je 0x140c2ba3c
00C2BA35  E8 52 9D 96 FF                  call 0x14059578c
00C2BA3A  EB 07                           jmp 0x140c2ba43
00C2BA3C  44 88 25 76 EF 1D 00            mov byte ptr [rip + 0x1def76], r12b
00C2BA43  45 85 F6                        test r14d, r14d
00C2BA46  74 0D                           je 0x140c2ba55
00C2BA48  41 8B CF                        mov ecx, r15d
00C2BA4B  BA 06 01 00 00                  mov edx, 0x106
00C2BA50  E8 AB AD BA FF                  call 0x1407d6800
00C2BA55  8B 0D 69 E1 3A 00               mov ecx, dword ptr [rip + 0x3ae169]
00C2BA5B  85 C9                           test ecx, ecx
00C2BA5D  74 05                           je 0x140c2ba64
00C2BA5F  E8 0C C5 B8 FF                  call 0x1407b7f70
00C2BA64  4C 8B 05 CD 33 2D 00            mov r8, qword ptr [rip + 0x2d33cd]
00C2BA6B  45 33 C9                        xor r9d, r9d
00C2BA6E  33 C9                           xor ecx, ecx
00C2BA70  41 0F B6 10                     movzx edx, byte ptr [r8]
00C2BA74  45 8B 40 04                     mov r8d, dword ptr [r8 + 4]
00C2BA78  E8 D3 C5 B8 FF                  call 0x1407b8050
00C2BA7D  48 8D 05 EC C4 3D FF            lea rax, [rip - 0xc23b14]
00C2BA84  48 C7 45 D8 06 00 01 00         mov qword ptr [rbp - 0x28], 0x10006
00C2BA8C  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00C2BA91  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00C2BA95  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00C2BA9A  48 C7 45 E8 00 02 00 00         mov qword ptr [rbp - 0x18], 0x200
00C2BAA2  48 8D 0D 87 16 36 00            lea rcx, [rip + 0x361687]
00C2BAA9  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00C2BAAD  44 89 6C 24 60                  mov dword ptr [rsp + 0x60], r13d
00C2BAB2  4C 89 65 F0                     mov qword ptr [rbp - 0x10], r12
00C2BAB6  4C 89 65 F8                     mov qword ptr [rbp - 8], r12
00C2BABA  E8 0D 4C BA FF                  call 0x1407d06cc
00C2BABF  85 C0                           test eax, eax
00C2BAC1  79 07                           jns 0x140c2baca
00C2BAC3  4C 89 25 66 16 36 00            mov qword ptr [rip + 0x361666], r12
00C2BACA  48 8D 05 AF 85 9B FF            lea rax, [rip - 0x647a51]
00C2BAD1  4C 89 25 B0 AA 2D 00            mov qword ptr [rip + 0x2daab0], r12
00C2BAD8  48 89 05 E1 B7 39 00            mov qword ptr [rip + 0x39b7e1], rax
00C2BADF  48 8D 05 CA D3 81 FF            lea rax, [rip - 0x7e2c36]
00C2BAE6  48 89 05 7B 2E 36 00            mov qword ptr [rip + 0x362e7b], rax
00C2BAED  8B 87 08 01 00 00               mov eax, dword ptr [rdi + 0x108]
00C2BAF3  A8 02                           test al, 2
00C2BAF5  74 0E                           je 0x140c2bb05
00C2BAF7  48 8D 05 32 37 96 FF            lea rax, [rip - 0x69c8ce]
00C2BAFE  48 89 05 63 2E 36 00            mov qword ptr [rip + 0x362e63], rax
00C2BB05  45 85 F6                        test r14d, r14d
00C2BB08  74 0D                           je 0x140c2bb17
00C2BB0A  41 8B CF                        mov ecx, r15d
00C2BB0D  BA 06 02 00 00                  mov edx, 0x206
00C2BB12  E8 E9 AC BA FF                  call 0x1407d6800
00C2BB17  48 8B 87 F0 00 00 00            mov rax, qword ptr [rdi + 0xf0]
00C2BB1E  F7 80 84 00 00 00 00 00 10 00   test dword ptr [rax + 0x84], 0x100000
00C2BB28  74 46                           je 0x140c2bb70
00C2BB2A  40 84 35 A3 1D 36 00            test byte ptr [rip + 0x361da3], sil
00C2BB31  74 13                           je 0x140c2bb46
00C2BB33  48 8D 15 8E 74 3F FF            lea rdx, [rip - 0xc08b72]
00C2BB3A  48 8D 0D DF B2 1D 00            lea rcx, [rip + 0x1db2df]
00C2BB41  E8 DE AF 96 FF                  call 0x140596b24
00C2BB46  41 8A D5                        mov dl, r13b
00C2BB49  48 8B CF                        mov rcx, rdi
00C2BB4C  E8 93 0F 00 00                  call 0x140c2cae4
00C2BB51  40 84 35 7C 1D 36 00            test byte ptr [rip + 0x361d7c], sil
00C2BB58  74 16                           je 0x140c2bb70
00C2BB5A  44 8B C8                        mov r9d, eax
00C2BB5D  48 8D 15 3C 75 3F FF            lea rdx, [rip - 0xc08ac4]
00C2BB64  48 8D 0D B5 B2 1D 00            lea rcx, [rip + 0x1db2b5]
00C2BB6B  E8 F8 AF 96 FF                  call 0x140596b68
00C2BB70  48 8D 55 C0                     lea rdx, [rbp - 0x40]
00C2BB74  48 8B CF                        mov rcx, rdi
00C2BB77  E8 78 2B 00 00                  call 0x140c2e6f4
00C2BB7C  8B D8                           mov ebx, eax
00C2BB7E  85 C0                           test eax, eax
00C2BB80  79 26                           jns 0x140c2bba8
00C2BB82  33 D2                           xor edx, edx
00C2BB84  8D 4A 09                        lea ecx, [rdx + 9]
00C2BB87  E8 60 C2 88 FF                  call 0x1404b7dec
00C2BB8C  44 39 25 3D 1D 36 00            cmp dword ptr [rip + 0x361d3d], r12d
00C2BB93  0F 85 F2 F7 FF FF               jne 0x140c2b38b
00C2BB99  C7 05 2D 1D 36 00 06 00 00 00   mov dword ptr [rip + 0x361d2d], 6
00C2BBA3  E9 E3 F7 FF FF                  jmp 0x140c2b38b
00C2BBA8  45 85 F6                        test r14d, r14d
00C2BBAB  74 0D                           je 0x140c2bbba
00C2BBAD  41 8B CF                        mov ecx, r15d
00C2BBB0  BA 06 03 00 00                  mov edx, 0x306
00C2BBB5  E8 46 AC BA FF                  call 0x1407d6800
00C2BBBA  44 84 3D 13 1D 36 00            test byte ptr [rip + 0x361d13], r15b
00C2BBC1  74 13                           je 0x140c2bbd6
00C2BBC3  48 8D 15 8E 62 3F FF            lea rdx, [rip - 0xc09d72]
00C2BBCA  48 8D 0D 4F B2 1D 00            lea rcx, [rip + 0x1db24f]
00C2BBD1  E8 4E AF 96 FF                  call 0x140596b24
00C2BBD6  48 8B CF                        mov rcx, rdi
00C2BBD9  E8 FE BC 03 00                  call 0x140c678dc
00C2BBDE  44 84 3D EF 1C 36 00            test byte ptr [rip + 0x361cef], r15b
00C2BBE5  8B D8                           mov ebx, eax
00C2BBE7  74 13                           je 0x140c2bbfc
00C2BBE9  48 8D 15 B8 68 3F FF            lea rdx, [rip - 0xc09748]
00C2BBF0  48 8D 0D 29 B2 1D 00            lea rcx, [rip + 0x1db229]
00C2BBF7  E8 28 AF 96 FF                  call 0x140596b24
00C2BBFC  85 DB                           test ebx, ebx
00C2BBFE  79 0F                           jns 0x140c2bc0f
00C2BC00  C7 05 C6 1C 36 00 15 00 00 00   mov dword ptr [rip + 0x361cc6], 0x15
00C2BC0A  E9 7C F7 FF FF                  jmp 0x140c2b38b
00C2BC0F  BB 02 00 00 00                  mov ebx, 2
00C2BC14  48 8B D7                        mov rdx, rdi
00C2BC17  8B CB                           mov ecx, ebx
00C2BC19  E8 3A 67 04 00                  call 0x140c72358
00C2BC1E  84 C0                           test al, al
00C2BC20  75 0B                           jne 0x140c2bc2d
00C2BC22  B9 A0 00 00 00                  mov ecx, 0xa0
00C2BC27  E8 14 1A 8D FF                  call 0x1404fd640
00C2BC2C  CC                              int3
00C2BC2D  45 85 F6                        test r14d, r14d
00C2BC30  74 0D                           je 0x140c2bc3f
00C2BC32  41 8B CF                        mov ecx, r15d
00C2BC35  BA 07 00 00 00                  mov edx, 7
00C2BC3A  E8 C1 AB BA FF                  call 0x1407d6800
00C2BC3F  41 8B CD                        mov ecx, r13d
00C2BC42  E8 F5 AA 04 00                  call 0x140c7673c
00C2BC47  48 8B D7                        mov rdx, rdi
00C2BC4A  8B CB                           mov ecx, ebx
00C2BC4C  E8 EF 90 B8 FF                  call 0x1407b4d40
00C2BC51  E8 9A E1 FF FF                  call 0x140c29df0
00C2BC56  E8 B5 46 97 FF                  call 0x1405a0310
00C2BC5B  E8 68 77 97 FF                  call 0x1405a33c8
00C2BC60  44 38 25 55 A4 23 00            cmp byte ptr [rip + 0x23a455], r12b
00C2BC67  74 0E                           je 0x140c2bc77
00C2BC69  E8 CA E4 AE FF                  call 0x14071a138
00C2BC6E  44 38 25 47 A4 23 00            cmp byte ptr [rip + 0x23a447], r12b
00C2BC75  75 13                           jne 0x140c2bc8a
00C2BC77  E8 98 CE 96 FF                  call 0x140598b14
00C2BC7C  44 38 25 35 ED 1D 00            cmp byte ptr [rip + 0x1ded35], r12b
00C2BC83  75 05                           jne 0x140c2bc8a
00C2BC85  E8 86 2D 97 FF                  call 0x14059ea10
00C2BC8A  E8 A9 E5 AE FF                  call 0x14071a238
00C2BC8F  E8 AC EA AE FF                  call 0x14071a740
00C2BC94  40 84 35 39 1C 36 00            test byte ptr [rip + 0x361c39], sil
00C2BC9B  74 13                           je 0x140c2bcb0
00C2BC9D  48 8D 15 24 73 3F FF            lea rdx, [rip - 0xc08cdc]
00C2BCA4  48 8D 0D 75 B1 1D 00            lea rcx, [rip + 0x1db175]
00C2BCAB  E8 74 AE 96 FF                  call 0x140596b24
00C2BCB0  B9 53 00 00 00                  mov ecx, 0x53
00C2BCB5  33 D2                           xor edx, edx
00C2BCB7  E8 44 AB BA FF                  call 0x1407d6800
00C2BCBC  33 D2                           xor edx, edx
00C2BCBE  48 8B CF                        mov rcx, rdi
00C2BCC1  E8 1E 0E 00 00                  call 0x140c2cae4
00C2BCC6  40 84 35 07 1C 36 00            test byte ptr [rip + 0x361c07], sil
00C2BCCD  8B D8                           mov ebx, eax
00C2BCCF  74 16                           je 0x140c2bce7
00C2BCD1  44 8B C8                        mov r9d, eax
00C2BCD4  48 8D 15 C5 73 3F FF            lea rdx, [rip - 0xc08c3b]
00C2BCDB  48 8D 0D 3E B1 1D 00            lea rcx, [rip + 0x1db13e]
00C2BCE2  E8 81 AE 96 FF                  call 0x140596b68
00C2BCE7  45 85 F6                        test r14d, r14d
00C2BCEA  74 0C                           je 0x140c2bcf8
00C2BCEC  B9 50 00 00 00                  mov ecx, 0x50
00C2BCF1  8B D3                           mov edx, ebx
00C2BCF3  E8 08 AB BA FF                  call 0x1407d6800
00C2BCF8  85 DB                           test ebx, ebx
00C2BCFA  78 07                           js 0x140c2bd03
00C2BCFC  E8 6B A1 96 FF                  call 0x140595e6c
00C2BD01  EB 0E                           jmp 0x140c2bd11
00C2BD03  44 38 25 B0 EC 1D 00            cmp byte ptr [rip + 0x1decb0], r12b
00C2BD0A  75 05                           jne 0x140c2bd11
00C2BD0C  E8 0B EB AE FF                  call 0x14071a81c
00C2BD11  E8 4A 08 E1 FF                  call 0x140a3c560
00C2BD16  84 C0                           test al, al
00C2BD18  75 05                           jne 0x140c2bd1f
00C2BD1A  E8 A5 7E 00 00                  call 0x140c33bc4
00C2BD1F  8B 1D 9B 85 39 00               mov ebx, dword ptr [rip + 0x39859b]
00C2BD25  8B C3                           mov eax, ebx
00C2BD27  0F BA E8 12                     bts eax, 0x12
00C2BD2B  89 05 8F 85 39 00               mov dword ptr [rip + 0x39858f], eax
00C2BD31  E8 5A 30 B5 FF                  call 0x14077ed90
00C2BD36  89 1D 84 85 39 00               mov dword ptr [rip + 0x398584], ebx
00C2BD3C  44 8B F8                        mov r15d, eax
00C2BD3F  85 C0                           test eax, eax
00C2BD41  79 1C                           jns 0x140c2bd5f
00C2BD43  33 D2                           xor edx, edx
00C2BD45  8D 4A 0A                        lea ecx, [rdx + 0xa]
00C2BD48  E8 9F C0 88 FF                  call 0x1404b7dec
00C2BD4D  41 8B C7                        mov eax, r15d
00C2BD50  C7 05 76 1B 36 00 07 00 00 00   mov dword ptr [rip + 0x361b76], 7
00C2BD5A  E9 86 01 00 00                  jmp 0x140c2bee5
00C2BD5F  41 8B CD                        mov ecx, r13d
00C2BD62  E8 A1 91 03 00                  call 0x140c64f08
00C2BD67  33 C9                           xor ecx, ecx
00C2BD69  E8 56 FD F3 FF                  call 0x140b6bac4
00C2BD6E  48 8D 55 B0                     lea rdx, [rbp - 0x50]
00C2BD72  48 8B CF                        mov rcx, rdi
00C2BD75  E8 56 14 00 00                  call 0x140c2d1d0
00C2BD7A  84 C0                           test al, al
00C2BD7C  75 19                           jne 0x140c2bd97
00C2BD7E  33 D2                           xor edx, edx
00C2BD80  8D 4A 0C                        lea ecx, [rdx + 0xc]
00C2BD83  E8 64 C0 88 FF                  call 0x1404b7dec
00C2BD88  C7 05 3E 1B 36 00 09 00 00 00   mov dword ptr [rip + 0x361b3e], 9
00C2BD92  E9 DF F2 FF FF                  jmp 0x140c2b076
00C2BD97  48 8B CF                        mov rcx, rdi
00C2BD9A  E8 4D 28 00 00                  call 0x140c2e5ec
00C2BD9F  84 C0                           test al, al
00C2BDA1  75 19                           jne 0x140c2bdbc
00C2BDA3  33 D2                           xor edx, edx
00C2BDA5  8D 4A 0D                        lea ecx, [rdx + 0xd]
00C2BDA8  E8 3F C0 88 FF                  call 0x1404b7dec
00C2BDAD  C7 05 19 1B 36 00 0A 00 00 00   mov dword ptr [rip + 0x361b19], 0xa
00C2BDB7  E9 BA F2 FF FF                  jmp 0x140c2b076
00C2BDBC  48 8B 05 FD 96 2C 00            mov rax, qword ptr [rip + 0x2c96fd]
00C2BDC3  4C 8D 4D C8                     lea r9, [rbp - 0x38]
00C2BDC7  48 83 C0 48                     add rax, 0x48
00C2BDCB  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00C2BDD0  0F 57 C0                        xorps xmm0, xmm0
00C2BDD3  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00C2BDD7  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00C2BDDC  C7 44 24 70 30 00 00 00         mov dword ptr [rsp + 0x70], 0x30
00C2BDE4  BA 00 00 00 80                  mov edx, 0x80000000
00C2BDE9  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
00C2BDEE  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C2BDF3  C7 45 88 40 02 00 00            mov dword ptr [rbp - 0x78], 0x240
00C2BDFA  F3 0F 7F 45 90                  movdqu xmmword ptr [rbp - 0x70], xmm0
00C2BDFF  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
00C2BE04  E8 27 19 A8 FF                  call 0x1406ad730
00C2BE09  85 C0                           test eax, eax
00C2BE0B  78 50                           js 0x140c2be5d
00C2BE0D  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2BE12  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00C2BE17  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00C2BE1C  45 33 C9                        xor r9d, r9d
00C2BE1F  45 33 C0                        xor r8d, r8d
00C2BE22  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C2BE27  BA 80 00 00 00                  mov edx, 0x80
00C2BE2C  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
00C2BE31  E8 7A CF C3 FF                  call 0x140868db0
00C2BE36  85 C0                           test eax, eax
00C2BE38  78 19                           js 0x140c2be53
00C2BE3A  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00C2BE3F  E8 E4 00 B0 FF                  call 0x14072bf28
00C2BE44  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00C2BE49  BA 44 66 6C 74                  mov edx, 0x746c6644
00C2BE4E  E8 8D BA 6C FF                  call 0x1402f78e0
00C2BE53  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2BE58  E8 53 14 A8 FF                  call 0x1406ad2b0
00C2BE5D  33 D2                           xor edx, edx
00C2BE5F  41 8B CD                        mov ecx, r13d
00C2BE62  E8 FD 13 02 00                  call 0x140c4d264
00C2BE67  84 C0                           test al, al
00C2BE69  75 0F                           jne 0x140c2be7a
00C2BE6B  C7 05 5B 1A 36 00 19 00 00 00   mov dword ptr [rip + 0x361a5b], 0x19
00C2BE75  E9 FC F1 FF FF                  jmp 0x140c2b076
00C2BE7A  45 85 F6                        test r14d, r14d
00C2BE7D  74 0C                           je 0x140c2be8b
00C2BE7F  B9 08 00 00 00                  mov ecx, 8
00C2BE84  8B D1                           mov edx, ecx
00C2BE86  E8 75 A9 BA FF                  call 0x1407d6800
00C2BE8B  40 84 35 42 1A 36 00            test byte ptr [rip + 0x361a42], sil
00C2BE92  74 16                           je 0x140c2beaa
00C2BE94  45 8B CD                        mov r9d, r13d
00C2BE97  48 8D 15 1A 6C 3F FF            lea rdx, [rip - 0xc093e6]
00C2BE9E  48 8D 0D 7B AF 1D 00            lea rcx, [rip + 0x1daf7b]
00C2BEA5  E8 BE AC 96 FF                  call 0x140596b68
00C2BEAA  41 8B D5                        mov edx, r13d
00C2BEAD  48 8B CF                        mov rcx, rdi
00C2BEB0  E8 53 8D 02 00                  call 0x140c54c08
00C2BEB5  40 84 35 18 1A 36 00            test byte ptr [rip + 0x361a18], sil
00C2BEBC  74 13                           je 0x140c2bed1
00C2BEBE  48 8D 15 53 51 3F FF            lea rdx, [rip - 0xc0aead]
00C2BEC5  48 8D 0D 54 AF 1D 00            lea rcx, [rip + 0x1daf54]
00C2BECC  E8 53 AC 96 FF                  call 0x140596b24
00C2BED1  45 85 F6                        test r14d, r14d
00C2BED4  74 0D                           je 0x140c2bee3
00C2BED6  B9 08 00 00 00                  mov ecx, 8
00C2BEDB  8D 51 01                        lea edx, [rcx + 1]
00C2BEDE  E8 1D A9 BA FF                  call 0x1407d6800
00C2BEE3  33 C0                           xor eax, eax
00C2BEE5  48 8B 4D 00                     mov rcx, qword ptr [rbp]
00C2BEE9  48 33 CC                        xor rcx, rsp
00C2BEEC  E8 4F 07 A8 FF                  call 0x1406ac640
00C2BEF1  4C 8D 9C 24 10 01 00 00         lea r11, [rsp + 0x110]
00C2BEF9  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00C2BEFD  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00C2BF01  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00C2BF05  49 8B E3                        mov rsp, r11
00C2BF08  41 5F                           pop r15
00C2BF0A  41 5E                           pop r14
00C2BF0C  41 5D                           pop r13
00C2BF0E  41 5C                           pop r12
00C2BF10  5D                              pop rbp
00C2BF11  C3                              ret
00C2BF12  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoInitSystemPreDrivers(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int16 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int16 v_stack_m118;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int8 v_stack_mF8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 1964762)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 56) = result;
    v_r12 = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 80) = 0x1000000ULL;
    *(unsigned __int64 *)(v_rsp - 56 - 64) = 0;
    v_stack_mC4 = 0;
    *(unsigned int *)(v_rsp - 56 - 116) = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 72) = v_rip + 4055874;
    v_rbx = (unsigned int)((v_rbx) | (0xFFFFFFFFULL));
    *(unsigned __int64 *)(v_rsp - 56 - 96) = v_xmm0;
    v_stack_mF0 = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 56) = v_xmm0;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 132))) & (0x80000ULL));
    v_stack_mF8 = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 40) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 56 - 24) = v_xmm1;
    result = ExInitializeResourceLite2(v_rip + 3548909, (unsigned int)((unsigned int)(v_rbx)), a3, a4);
    result = ExInitializeResourceLite2(v_rip + 3548734, (unsigned int)((unsigned int)(v_rbx)), a3, a4);
    result = ExInitializeResourceLite2(v_rip + 3548592, (unsigned int)((unsigned int)(v_rbx)), a3, a4);
    result = ExInitializeResourceLite2(v_rip + 3554306, (unsigned int)((unsigned int)(v_rbx)), a3, a4);
    result = ExInitializeResourceLite2(v_rip + 3548052, (unsigned int)((unsigned int)(v_rbx)), a3, a4);
    *(unsigned __int64 *)(v_rip + 3548529) = 0;
    *(unsigned __int64 *)(v_rip + 3548514) = v_rip + 3548520;
    *(unsigned __int64 *)(v_rip + 3548496) = v_rip + 3548520;
    *(unsigned __int64 *)(v_rip + 3548474) = v_rip + 3548473;
    *(unsigned __int64 *)(v_rip + 3548459) = v_rip + 3548473;
    *(unsigned __int64 *)(v_rip + 3548437) = v_rip + 3548436;
    *(unsigned __int64 *)(v_rip + 3548422) = v_rip + 3548436;
    *(unsigned __int64 *)(v_rip + 3548400) = v_rip + 3548399;
    *(unsigned __int64 *)(v_rip + 3548385) = v_rip + 3548399;
    *(unsigned __int64 *)(v_rip + 3548363) = v_rip + 3548362;
    *(unsigned __int64 *)(v_rip + 3548348) = v_rip + 3548362;
    *(unsigned __int64 *)(v_rip + 3548326) = v_rip + 3548325;
    *(unsigned __int64 *)(v_rip + 3548311) = v_rip + 3548325;
    *(unsigned __int64 *)(v_rip + 3548289) = v_rip + 3548288;
    *(unsigned __int64 *)(v_rip + 3548274) = v_rip + 3548288;
    *(unsigned __int64 *)(v_rip + 3548844) = v_rip + 3548843;
    *(unsigned __int64 *)(v_rip + 3548829) = v_rip + 3548843;
    *(unsigned __int64 *)(v_rip + 3548807) = v_rip + 3548806;
    *(unsigned __int64 *)(v_rip + 3548792) = v_rip + 3548806;
    *(unsigned __int64 *)(v_rip + 3548770) = v_rip + 3548769;
    *(unsigned __int64 *)(v_rip + 3548755) = v_rip + 3548769;
    *(unsigned __int64 *)(v_rip + 3548740) = 0;
    *(unsigned __int64 *)(v_rip + 3820293) = 0;
    *(unsigned __int64 *)(v_rip + 3548718) = 0;
    *(unsigned __int64 *)(v_rip + 3548694) = v_xmm0;
    *(unsigned int *)(v_rip + 3548675) = 0;
    a2 = ((unsigned int)((unsigned int)(v_rbx))) << (32);
    result = (v_rip + 3548769) | (a2);
    *(unsigned int *)(v_rip + 3548138) = 0;
    a3 = (result) >> (4);
    a1 = (a3) - (a2);
    a1 = (a1) >> (1);
    a1 = (a1) + (a2);
    a1 = (a1) >> (6);
    a1 = (a1) * (a1);
    a3 = (a3) - (a1);
    a3 = (unsigned int)((a3) + (10));
    *(unsigned int *)(v_rip + 3548586) = (unsigned int)(a3);
    result = 0;
    if ((*(unsigned int *)(v_rip + 3548589)) == 0) {
        *(unsigned int *)(v_rip + 3548570) = 14;
        result = (unsigned int)(v_r12 + 1);
        *(unsigned int *)(v_rip + 3548052) = (unsigned int)(v_r12 + 1);
    }
    if ((*(unsigned int *)(v_rip + 3548549)) == 0) {
        result = (unsigned int)((result) | (2));
        *(unsigned int *)(v_rip + 3548533) = 4;
        *(unsigned int *)(v_rip + 3548023) = (unsigned int)(result);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 2339421))) + (-2));
    if (((unsigned int)(result)) >= = 298) {
        *(unsigned int *)(v_rip + 2339401) = 300;
    }
    result = IopQueryProcessorInitValues(v_rsp - 56 - 40, a2, a3, a4);
    v_stack_m110 = v_rip + 2948409;
    v_stack_m118 = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 56 - 34));
    result = ExInitializeSystemLookasideList(v_rip + 1996185, 512, 56, (unsigned int)(0x20706349ULL));
    v_stack_m110 = v_rip + 2948409;
    v_stack_m118 = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 56 - 36));
    result = ExInitializeSystemLookasideList(v_rip + 1996291, 512, (unsigned int)(*(unsigned int *)(v_rsp - 56 - 20)), (unsigned int)(0x6C707249ULL));
    v_stack_m110 = v_rip + 2948409;
    v_stack_m118 = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 56 - 38));
    result = ExInitializeSystemLookasideList(v_rip + 1996380, 512, (unsigned int)(*(unsigned int *)(v_rsp - 56 - 24)), (unsigned int)(0x6D707249ULL));
    v_stack_m110 = v_rip + 2948409;
    v_stack_m118 = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 56 - 40));
    result = ExInitializeSystemLookasideList(v_rip + 1996469, 512, (unsigned int)(*(unsigned int *)(v_rsp - 56 - 28)), (unsigned int)(0x73707249ULL));
    v_stack_m110 = v_rip + 2948409;
    v_stack_m118 = (unsigned __int16)(*(unsigned __int16 *)(v_rsp - 56 - 32));
    result = ExInitializeSystemLookasideList(v_rip + 1996558, 512, (unsigned int)(*(unsigned int *)(v_rsp - 56 - 16)), (unsigned int)(0x206C644DULL));
    v_stack_m100 = 0;
    v_stack_m108 = 0;
    v_stack_m110 = 0x73556F49ULL;
    v_stack_m118 = 32;
    a3 = 0;
    a2 = 0;
    result = ExInitializeNPagedLookasideListInternal(v_rip + 1995622, a2, a3, 512);
    a2 = 0;
    result = FsRtlInitExtraCreateParameterLookasideList(v_rip + 1995698, a2, 286, (unsigned int)(0x69536F49ULL));
    v_stack_m100 = 0;
    v_stack_m108 = 0;
    v_stack_m110 = 0x7443704FULL;
    a3 = 0;
    a2 = 0;
    v_stack_m118 = 48;
    result = ExInitializeNPagedLookasideListInternal(v_rip + 1995797, a2, a3, 512);
    result = KeQueryActiveProcessorCountEx((unsigned int)(0xFFFFULL), a2, a3, 512);
    v_stack_mE8 = 0;
    if ((unsigned int)(result) == 0) goto loc_00C2B04A;
loc_00C2B027:
    result = IoInitializeProcessor(*(unsigned __int64 *)(v_rip + 3791890 + 0 * 8), v_rsp - 56 - 40, a3, 512);
    a1 = (unsigned int)(((unsigned int)(v_stack_mE8)) + ((unsigned int)(v_r12 + 1)));
    v_stack_mE8 = (unsigned int)(a1);
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_00C2B027;
loc_00C2B04A:
    *(unsigned __int64 *)(v_rip + 3817832) = 0;
    *(unsigned __int64 *)(v_rip + 3548697) = v_rip + 3548703;
    *(unsigned __int64 *)(v_rip + 3548682) = v_rip + 3548703;
    result = IopInitializeReserveIrps(a1, v_rsp - 56 - 40, a3, 512);
    if ((unsigned __int8)(result) != 0) goto loc_00C2B080;
    *(unsigned int *)(v_rip + 3549274) = (unsigned int)(v_r12 + 1);
loc_00C2B076:
    goto loc_00C2BEE5;
loc_00C2B080:
    result = (unsigned int)(*(unsigned int *)(v_rip + 3547530));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3547530)))) & (3)) != 0) {
        a1 = v_rip - 8084593;
        *(unsigned int *)(v_rip + 3548361) = 400;
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3547530))) | (4));
        *(unsigned __int64 *)(v_rip + 3548308) = a1;
        *(unsigned int *)(v_rip + 3547494) = (unsigned int)(result);
        *(unsigned int *)(v_rip + 3548332) = 0x7D0ULL;
        *(unsigned int *)(v_rip + 3548258) = 275;
        *(unsigned __int64 *)(v_rip + 3548283) = 0;
        *(unsigned __int64 *)(v_rip + 3548300) = 0;
        *(unsigned __int64 *)(v_rip + 3548253) = 0;
    }
    result = (unsigned int)(*(unsigned int *)(v_rip + 1964267));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1964267)))) >= ((unsigned int)((unsigned int)(0x400000ULL)))) {
        result = (unsigned int)((unsigned int)(0x400000ULL));
        *(unsigned int *)(v_rip + 1964250) = (unsigned int)((unsigned int)(0x400000ULL));
    }
    if (((unsigned int)(result)) <= 0x1000ULL) {
        *(unsigned int *)(v_rip + 1964233) = 0x1000ULL;
    }
    v_stack_mC8 = 48;
    *(unsigned __int64 *)(v_rsp - 56 - 128) = v_rip + 3863270;
    v_stack_mC0 = 0;
    *(unsigned int *)(v_rsp - 56 - 120) = 576;
    *(unsigned __int64 *)(v_rsp - 56 - 112) = v_xmm0;
    result = ZwOpenKey(v_stack_mF0, (unsigned int)(0x20019ULL), v_stack_mC8, 512);
    if (sign_flag) goto loc_00C2B1A2;
    result = RtlInitUnicodeString(v_rsp - 56 - 96, v_rip + 321583, v_stack_mC8, 512);
    v_stack_m110 = v_stack_mE8;
    v_stack_m118 = 32;
    result = NtQueryValueKey(v_stack_mF0, v_rsp - 56 - 96, 2, v_rip + 4052808);
    if (sign_flag) goto loc_00C2B18B;
    if ((*(unsigned int *)(v_rip + 4052782)) != 4) goto loc_00C2B18B;
    result = ((*(unsigned int *)(v_rip + 4052782)) == 4) ? 1 : 0;
    goto loc_00C2B18E;
loc_00C2B18B:
loc_00C2B18E:
    a2 = 0;
    *(unsigned __int8 *)(v_rip + 3546815) = (unsigned __int8)((unsigned __int8)(v_r12 + 1));
    result = ObCloseHandle(v_stack_mF0, a2, 2, v_rip + 4052808);
    goto loc_00C2B1A9;
loc_00C2B1A2:
    *(unsigned __int8 *)(v_rip + 3546801) = (unsigned __int8)(v_r12 + 1);
loc_00C2B1A9:
    *(unsigned __int64 *)(v_rip + 3547849) = 0;
    *(unsigned __int64 *)(v_rip + 3547994) = v_rip + 3548000;
    *(unsigned __int64 *)(v_rip + 3547973) = v_rip + 3548000;
    *(unsigned __int64 *)(v_rip + 3547903) = v_rip - 8943826;
    *(unsigned __int64 *)(v_rip + 3547897) = v_rip + 3547936;
    *(unsigned __int64 *)(v_rip + 3547803) = v_rip + 3547802;
    *(unsigned __int64 *)(v_rip + 3547788) = v_rip + 3547802;
    *(unsigned __int64 *)(v_rip + 3547758) = v_rip + 3547757;
    *(unsigned __int64 *)(v_rip + 3547743) = v_rip + 3547757;
    *(unsigned __int64 *)(v_rip + 3548529) = v_rip - 5307272;
    *(unsigned __int64 *)(v_rip + 3548539) = v_rip + 3548538;
    *(unsigned __int64 *)(v_rip + 3548524) = v_rip + 3548538;
    *(unsigned __int64 *)(v_rip + 3548550) = v_rip + 3548549;
    *(unsigned __int64 *)(v_rip + 3548535) = v_rip + 3548549;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 1963885))) + (0xFFFFFC18ULL));
    *(unsigned __int64 *)(v_rip + 3817189) = 0;
    *(unsigned int *)(v_rip + 3547739) = 275;
    *(unsigned __int64 *)(v_rip + 3547788) = 0;
    *(unsigned __int64 *)(v_rip + 3547741) = 0;
    *(unsigned __int8 *)(v_rip + 3547654) = 9;
    *(unsigned __int64 *)(v_rip + 3547671) = 0;
    *(unsigned int *)(v_rip + 3547700) = 0;
    *(unsigned __int16 *)(v_rip + 3547688) = 0;
    *(unsigned __int64 *)(v_rip + 3548417) = 0;
    *(unsigned __int64 *)(v_rip + 3548386) = 0;
    *(unsigned __int64 *)(v_rip + 3548427) = 0;
    *(unsigned __int8 *)(v_rip + 3548428) = 5;
    *(unsigned __int8 *)(v_rip + 3548423) = 8;
    *(unsigned int *)(v_rip + 3548418) = 0;
    *(unsigned int *)(v_rip + 3548428) = 0x7FFFFFFFULL;
    *(unsigned __int8 *)(v_rip + 3548429) = 0;
    if (((unsigned int)(result)) >= = 0x2328ULL) {
        *(unsigned int *)(v_rip + 1963744) = 0x1388ULL;
    }
    *(unsigned __int64 *)(v_rip + 3548206) = 0;
    *(unsigned __int64 *)(v_rip + 3548191) = v_rip - 7955219;
    *(unsigned __int64 *)(v_rip + 3548154) = 0;
    *(unsigned __int64 *)(v_rip + 3548183) = v_rip + 3548193;
    *(unsigned __int64 *)(v_rip + 3548168) = v_rip + 3548193;
    *(unsigned __int64 *)(v_rip + 3548177) = 0;
    *(unsigned __int8 *)(v_rip + 3548210) = 0;
    *(unsigned __int8 *)(v_rip + 3546414) = (unsigned __int8)(v_r12 + 1);
    result = RtlInitUnicodeString(v_rsp - 56 - 96, v_rip + 321096, 2, v_rip + 4052808);
    v_stack_mC8 = 48;
    *(unsigned __int64 *)(v_rsp - 56 - 128) = v_rsp - 56 - 96;
    a4 = 0;
    v_stack_mC0 = 0;
    *(unsigned int *)(v_rsp - 56 - 120) = 528;
    v_stack_m118 = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 112) = v_xmm0;
    result = NtCreateEvent(v_stack_mF0, (unsigned int)(0x1F0003ULL), v_stack_mC8, a4);
    if (!sign_flag) goto loc_00C2B392;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(4, a2, v_stack_mC8, a4);
    *(unsigned int *)(v_rip + 3548485) = 26;
loc_00C2B38B:
    goto loc_00C2BEE5;
loc_00C2B392:
    a4 = 0;
    v_stack_m110 = 0;
    a2 = 0;
    v_stack_m118 = v_stack_mD8;
    v_stack_mD8 = 0;
    result = ObReferenceObjectByHandle(v_stack_mF0, a2, *(unsigned __int64 *)(v_rip + 3782631), a4);
    a2 = 0;
    *(unsigned __int64 *)(v_rip + 3861428) = v_stack_mD8;
    *(unsigned __int64 *)(v_rip + 3547918) = v_rip + 3547917;
    *(unsigned __int64 *)(v_rip + 3547903) = v_rip + 3547917;
    *(unsigned __int64 *)(v_rip + 3547865) = v_rip + 3547864;
    *(unsigned __int64 *)(v_rip + 3547850) = v_rip + 3547864;
    *(unsigned __int64 *)(v_rip + 3547780) = v_rip + 3547779;
    *(unsigned __int64 *)(v_rip + 3547765) = v_rip + 3547779;
    *(unsigned __int16 *)(v_rip + 3547845) = 0;
    *(unsigned __int8 *)(v_rip + 3547841) = 6;
    *(unsigned int *)(v_rip + 3547836) = 0;
    *(unsigned __int16 *)(v_rip + 3547792) = 0;
    *(unsigned __int8 *)(v_rip + 3547788) = 6;
    *(unsigned int *)(v_rip + 3547783) = 0;
    *(unsigned __int16 *)(v_rip + 3547707) = (unsigned __int16)(v_r12 + 1);
    *(unsigned __int8 *)(v_rip + 3547703) = 6;
    *(unsigned int *)(v_rip + 3547698) = (unsigned int)(v_r12 + 1);
    result = ObCloseHandle(v_stack_mF0, a2, *(unsigned __int64 *)(v_rip + 3782631), a4);
    result = IopCreateRootDirectories(v_stack_mF0, a2, *(unsigned __int64 *)(v_rip + 3782631), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00C2B478;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(6, a2, *(unsigned __int64 *)(v_rip + 3782631), a4);
    *(unsigned int *)(v_rip + 3548253) = 3;
    goto loc_00C2B076;
loc_00C2B478:
    result = IopInitializeSessionNotifications(6, a2, *(unsigned __int64 *)(v_rip + 3782631), a4);
    if (!sign_flag) goto loc_00C2B490;
    *(unsigned int *)(v_rip + 3548229) = 15;
    goto loc_00C2BEE5;
loc_00C2B490:
    a2 = 0;
    result = IopInitializePlugPlayServices(a1, a2, *(unsigned __int64 *)(v_rip + 3782631), a4);
    if (!sign_flag) goto loc_00C2B4B5;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(a2 + 7, a2, *(unsigned __int64 *)(v_rip + 3782631), a4);
    *(unsigned int *)(v_rip + 3548192) = 4;
    goto loc_00C2B38B;
loc_00C2B4B5:
    if ((unsigned int)(v_r14) != 0) {
        a1 = 8;
        a2 = (unsigned int)(v_r12 + 1);
        result = WheaSelLogCheckPoint(a1, a2, *(unsigned __int64 *)(v_rip + 3782631), a4);
    }
    a2 = 0;
    result = KseInitialize(a1, a2, *(unsigned __int64 *)(v_rip + 3782631), a4);
    result = PoInitDriverServices(a1, a2, *(unsigned __int64 *)(v_rip + 3782631), a4);
    result = guard_dispatch_icall(a1, a2, *(unsigned __int64 *)(v_rip + 3782631), a4);
loc_00C2B4EB:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3542865) + 8) == 0) goto loc_00C2B51F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3542865) + 8) + 300))) - (777));
    if (((unsigned int)(result)) > ((unsigned int)(v_r12 + 1))) goto loc_00C2B50C;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3542865) + 8) + 396)) & (0x1000ULL)) == 0) goto loc_00C2B511;
loc_00C2B50C:
    goto loc_00C2B4EB;
loc_00C2B511:
    *(unsigned __int64 *)(v_rip + 4051318) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3542865) + 8));
    result = PipSetDevNodeFlags(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3542865) + 8)), 4, *(unsigned __int64 *)(v_rip + 3782631), a4);
loc_00C2B51F:
    a1 = 0;
    result = WMIInitialize(a1, a1, *(unsigned __int64 *)(v_rip + 3782631), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00C2B53C;
    *(unsigned int *)(v_rip + 3548057) = 18;
    goto loc_00C2B076;
loc_00C2B53C:
    if ((unsigned int)(v_r14) != 0) {
        a1 = 8;
        a2 = 2;
        result = WheaSelLogCheckPoint(a1, a2, *(unsigned __int64 *)(v_rip + 3782631), a4);
    }
    result = CmIsStateSeparationDevModeEnabled(a1, a2, *(unsigned __int64 *)(v_rip + 3782631), a4);
    result = RtlIsStateSeparationEnabled(a1, a2, *(unsigned __int64 *)(v_rip + 3782631), a4);
    result = ext_ms_win_ntos_stateseparation_l1_1_0_dll_ExpInitializeStateSeparationPhase0((unsigned __int8)(result), (unsigned __int8)((unsigned __int8)(result)), *(unsigned __int64 *)(v_rip + 3782631), a4);
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result + (unsigned int)(0x80000000ULL) * 1))) != 0) goto loc_00C2B58C;
    if (((unsigned int)(result)) == 0xC00000BBULL) goto loc_00C2B58C;
    *(unsigned int *)(v_rip + 3547977) = 19;
    goto loc_00C2BEE5;
loc_00C2B58C:
    v_stack_mE0 = 0;
    result = RtlGetNtProductType(v_stack_mE0, (unsigned int)(0x80000000ULL), *(unsigned __int64 *)(v_rip + 3782631), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C2B5E5;
    if (v_stack_mE0 != ((unsigned int)(v_r12 + 1))) goto loc_00C2B5E5;
    *(unsigned __int8 *)(v_rip + 3545766) = (unsigned __int8)(v_r12 + 1);
    result = ExAllocatePool2(256, (unsigned int)(0x1000ULL), (unsigned int)(0x6E446341ULL), a4);
    if (result != 0) goto loc_00C2B5DB;
    *(unsigned int *)(v_rip + 3547903) = 17;
    goto loc_00C2BEE5;
loc_00C2B5DB:
    result = AstInitializeBloomFilter(256, (unsigned int)(0x1000ULL), (unsigned int)(0xC0000017ULL), a4);
    goto loc_00C2B5EC;
loc_00C2B5E5:
    *(unsigned __int8 *)(v_rip + 3545708) = 0;
loc_00C2B5EC:
    result = EtwInitialize((unsigned int)((unsigned int)(v_r12 + 1)), a1, (unsigned int)(0xC0000017ULL), a4);
    a3 = 0;
    result = EtwRegister(v_rip - 12615911, v_rip - 5308856, a3, v_rip + 3547618);
    if (!sign_flag) goto loc_00C2B628;
    *(unsigned int *)(v_rip + 3547821) = 16;
    goto loc_00C2BEE5;
loc_00C2B628:
    result = McGenEventRegister_EtwRegister(v_rip - 12623893, v_rip - 5308856, v_rip + 1947626, v_rip + 1947633);
    if (!sign_flag) goto loc_00C2B655;
    *(unsigned int *)(v_rip + 3547776) = 11;
    goto loc_00C2BEE5;
loc_00C2B655:
    a3 = 0;
    result = TlgRegisterAggregateProviderEx(v_rip + 1960444, v_rip - 1528153, a3, v_rip + 1947633);
    if (!sign_flag) goto loc_00C2B681;
    *(unsigned int *)(v_rip + 3547732) = 22;
    goto loc_00C2BEE5;
loc_00C2B681:
    *(unsigned __int64 *)(v_rip + 2146192) = v_rip + 1960444;
    result = (unsigned int)(*(unsigned int *)(v_rip + 2116658));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 2116658))) != 0) {
        a3 = 0;
        a2 = (unsigned int)((v_rip - 1528153) | (0xFFFFFFFFULL));
        a1 = 0;
        result = MiLogBadMapper(a1, a2, a3, v_rip + 1947633);
    }
    a3 = 0;
    result = EtwRegister(v_rip - 12622519, v_rip - 6906592, a3, v_rip + 2336842);
    a3 = 0;
    a2 = 0;
    result = TraceLoggingRegisterEx_EtwRegister_EtwSetInformation(v_rip + 1947426, a2, a3, v_rip + 2336842);
    result = IopInitializeDumpPolicySettings((unsigned __int8)(v_r12 + 1), a2, a3, v_rip + 2336842);
    result = TlgRegisterAggregateProvider(v_rip + 1947532, a2, a3, v_rip + 2336842);
    result = SeAuditBootConfiguration(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 2880), a2, a3, v_rip + 2336842);
    result = BootApplicationPersistentDataProcess((unsigned int)((unsigned int)(v_r12 + 1)), a2, a3, v_rip + 2336842);
    a2 = 0;
    result = kdcom_dll_KdInitialize(a2 + 2, a2, v_rip + 3260123, v_rip + 2336842);
    result = KeInitSystem(2, a2, v_rip + 3260123, v_rip + 2336842);
    if ((*(unsigned __int8 *)(v_rip + 3545397)) != 0) goto loc_00C2B787;
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 3816082, a2, v_rip + 3260123, v_rip + 2336842);
    if ((*(unsigned __int64 *)(v_rip + 3546925)) != (v_rip + 3546932)) goto loc_00C2B74E;
    *(unsigned __int8 *)(v_rip + 3545359) = 0;
    goto loc_00C2B779;
loc_00C2B74E:
    *(unsigned __int64 *)(v_rip + 3545372) = 0;
    *(unsigned __int64 *)(v_rip + 3545354) = v_rip - 1891029;
    *(unsigned __int64 *)(v_rip + 3545324) = 0;
    result = ExQueueWorkItem(v_rip + 3545331, (unsigned int)((unsigned int)(v_r12 + 1)), v_rip + 3260123, v_rip + 2336842);
loc_00C2B779:
    result = KeReleaseSpinLock(v_rip + 3815998, (unsigned __int8)((unsigned __int8)(result)), v_rip + 3260123, v_rip + 2336842);
loc_00C2B787:
    if ((unsigned int)(v_r14) != 0) {
        a1 = 8;
        a2 = 3;
        result = WheaSelLogCheckPoint(a1, a2, v_rip + 3260123, v_rip + 2336842);
    }
    if (((*(unsigned __int8 *)(v_rip + 3547439)) & (16)) != 0) {
        a4 = 0;
        a2 = v_rip - 12619001;
        a1 = v_rip + 1947240;
        result = McTemplateK0q_EtwWriteTransfer(a1, a2, v_rip + 3260123, a4);
    }
    a2 = 0;
    result = WheaInitialize(a1, a2, v_rip + 3260123, a4);
    if (((*(unsigned __int8 *)(v_rip + 3547398)) & (16)) != 0) {
        a2 = v_rip - 12625855;
        a1 = v_rip + 1947202;
        result = McTemplateK0_EtwWriteTransfer(a1, a2, v_rip + 3260123, a4);
    }
    if ((unsigned int)(v_r14) != 0) {
        a1 = 8;
        a2 = 4;
        result = WheaSelLogCheckPoint(a1, a2, v_rip + 3260123, a4);
    }
    result = IopStoreArcInformation(a1, a2, v_rip + 3260123, a4);
    if (!sign_flag) goto loc_00C2B810;
    *(unsigned int *)(v_rip + 3547333) = 20;
    goto loc_00C2BEE5;
loc_00C2B810:
    result = IopInitializePlugPlayServices(a1, (unsigned int)((unsigned int)(v_r12 + 1)), v_rip + 3260123, a4);
    if (!sign_flag) goto loc_00C2B83A;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(8, a2, v_rip + 3260123, a4);
    *(unsigned int *)(v_rip + 3547291) = 5;
    goto loc_00C2B38B;
loc_00C2B83A:
    a2 = 0;
    result = memset(v_rip + 3547069, a2, a2 + 104, a4);
    *(unsigned __int64 *)(v_rip + 3547043) = v_rip + 3547069;
    *(unsigned __int64 *)(v_rip + 3547108) = v_rip - 2632438;
    *(unsigned __int64 *)(v_rip + 3547113) = 0;
    *(unsigned __int64 *)(v_rip + 3547090) = v_rip - 5311296;
    *(unsigned int *)(v_rip + 3547121) = (unsigned int)(v_r12 + 1);
    *(unsigned __int64 *)(v_rip + 3547074) = v_rip - 5309448;
    *(unsigned __int64 *)(v_rip + 3547140) = v_rip + 3547139;
    *(unsigned __int64 *)(v_rip + 3547125) = v_rip + 3547139;
    *(unsigned __int64 *)(v_rip + 3547094) = 0;
    *(unsigned int *)(v_rip + 3547095) = 0;
    *(unsigned __int16 *)(v_rip + 3547095) = (unsigned __int16)(v_r12 + 1);
    *(unsigned __int8 *)(v_rip + 3547091) = 6;
    *(unsigned int *)(v_rip + 3547086) = 0;
    result = KitpInitAitSampleRate(a1, a2, a2 + 104, a4);
    a3 = 0;
    a2 = 0;
    result = EtwRegister(v_rip - 12618734, a2, a3, v_rip + 2346246);
    if (sign_flag) {
        *(unsigned __int64 *)(v_rip + 2346218) = 0;
    }
    result = KseInitialize(a1, (unsigned int)((unsigned int)(v_r12 + 1)), a3, v_rip + 2346246);
    result = HvlPhase2Initialize(a1, (unsigned int)((unsigned int)(v_r12 + 1)), a3, v_rip + 2346246);
    if (!sign_flag) goto loc_00C2B91C;
    *(unsigned int *)(v_rip + 3547065) = 23;
    goto loc_00C2BEE5;
loc_00C2B91C:
    if ((unsigned int)(v_r14) != 0) {
        a1 = 8;
        a2 = 5;
        result = WheaSelLogCheckPoint(a1, a2, a3, v_rip + 2346246);
    }
    a1 = 0;
    result = KeOptimizeSpecCtrlSettings(a1, a2, a3, v_rip + 2346246);
    result = PsInitializeSyscallProviders(a1, a2, a3, v_rip + 2346246);
    result = VslpIumPhase4Initialize(a1, a2, a3, v_rip + 2346246);
    result = BootApplicationPersistentDataProcess(2, a2, a3, v_rip + 2346246);
    result = BapdRecordFirmwareBootStats(0, a2, a3, v_rip + 2346246);
    if ((unsigned int)(v_r14) != 0) {
        a1 = 8;
        a2 = 6;
        result = WheaSelLogCheckPoint(a1, a2, a3, v_rip + 2346246);
    }
    if (*(unsigned __int64 *)(v_rip + 2337137) != 0) {
        a4 = 0;
        v_stack_m118 = 0;
        a3 = v_rip + 1962101;
        a2 = v_rip - 12600706;
        result = EtwWriteStartScenario(*(unsigned __int64 *)(v_rip + 2337137), a2, a3, a4);
    }
    *(unsigned __int16 *)(v_rip + 3543818) = (unsigned __int16)(v_r12 + 1);
    *(unsigned __int64 *)(v_rip + 3543851) = v_rip + 3543858;
    *(unsigned __int64 *)(v_rip + 3543836) = v_rip + 3543858;
    *(unsigned __int64 *)(v_rip + 3543806) = v_rip + 3543805;
    *(unsigned __int64 *)(v_rip + 3543791) = v_rip + 3543805;
    *(unsigned __int8 *)(v_rip + 3543779) = 6;
    *(unsigned int *)(v_rip + 3543774) = (unsigned int)(v_r12 + 1);
    result = IopQueryPassiveInterruptRegistryOptions(*(unsigned __int64 *)(v_rip + 2337137), a2, a3, a4);
    *(unsigned __int64 *)(v_rip + 3543729) = v_rip + 3543735;
    *(unsigned __int64 *)(v_rip + 3543714) = v_rip + 3543735;
    *(unsigned __int64 *)(v_rip + 3543691) = 0;
    result = KeInitializeQueue(v_rip + 3543648, *(unsigned __int8 *)(v_rip + 1962031), a3, a4);
    result = IopCreatePassiveInterruptRealtimeThreads(v_rip + 3543648, *(unsigned __int8 *)(v_rip + 1962031), a3, a4);
    if (!sign_flag) goto loc_00C2BA12;
    *(unsigned int *)(v_rip + 3546819) = 24;
    goto loc_00C2BEE5;
loc_00C2BA12:
    result = SecureDump_PrepareForInit(v_rip + 3543648, v_stack_mF8, a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 2336409)) != 0) goto loc_00C2BA3C;
    if (v_stack_mF8 != 0) goto loc_00C2BA3C;
    if ((*(unsigned __int8 *)(v_rip + 1961863)) == 0) goto loc_00C2BA3C;
    result = IopInitDumpCapsuleSupport(v_rip + 3543648, v_stack_mF8, a3, a4);
    goto loc_00C2BA43;
loc_00C2BA3C:
    *(unsigned __int8 *)(v_rip + 1961846) = 0;
loc_00C2BA43:
    if ((unsigned int)(v_r14) != 0) {
        a1 = 8;
        a2 = 262;
        result = WheaSelLogCheckPoint(a1, a2, a3, a4);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3858793))) != 0) {
        result = EtwTraceLeapSecondDataParseFailure((unsigned int)(*(unsigned int *)(v_rip + 3858793)), a2, a3, a4);
    }
    a4 = 0;
    a1 = 0;
    result = EtwTraceLeapSecondDataUpdate(a1, *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 2962381)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2962381) + 4)), a4);
    *(unsigned __int64 *)(v_rsp - 56 - 40) = 0x10006ULL;
    v_stack_mD0 = v_rip - 12729108;
    *(unsigned __int64 *)(v_rsp - 56 - 24) = 512;
    *(unsigned __int64 *)(v_rsp - 56 - 32) = v_stack_mD8;
    v_stack_mD8 = (unsigned int)(v_r12 + 1);
    *(unsigned __int64 *)(v_rsp - 56 - 16) = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 8) = 0;
    result = ExRegisterHost(v_rip + 3544711, *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 2962381)), v_rsp - 56 - 40, a4);
    if (sign_flag) {
        *(unsigned __int64 *)(v_rip + 3544678) = 0;
    }
    *(unsigned __int64 *)(v_rip + 2992816) = 0;
    *(unsigned __int64 *)(v_rip + 3782625) = v_rip - 6584913;
    *(unsigned __int64 *)(v_rip + 3550843) = v_rip - 8268854;
    result = (unsigned int)(*(unsigned int *)(a1 + 264));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 264)))) & (2)) != 0) {
        result = v_rip - 6932686;
        *(unsigned __int64 *)(v_rip + 3550819) = result;
    }
    if ((unsigned int)(v_r14) != 0) {
        a1 = 8;
        a2 = 518;
        result = WheaSelLogCheckPoint(a1, a2, v_rsp - 56 - 40, a4);
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 132)) & (0x100000ULL)) == 0) goto loc_00C2BB70;
    result = *(unsigned __int64 *)(a1 + 240);
    if (((*(unsigned __int8 *)(v_rip + 3546531)) & (16)) != 0) {
        a2 = v_rip - 12618610;
        a1 = v_rip + 1946335;
        result = McTemplateK0_EtwWriteTransfer(a1, a2, v_rsp - 56 - 40, a4);
    }
    result = IopInitCrashDumpDuringSysInit(a1, (unsigned __int8)(v_r12 + 1), v_rsp - 56 - 40, a4);
    if (((*(unsigned __int8 *)(v_rip + 3546492)) & (16)) != 0) {
        a4 = (unsigned int)(result);
        a2 = v_rip - 12618436;
        a1 = v_rip + 1946293;
        result = McTemplateK0q_EtwWriteTransfer(a1, a2, v_rsp - 56 - 40, a4);
    }
    result = IopInitializeBootDrivers(a1, v_rsp - 56 - 64, v_rsp - 56 - 40, a4);
    if (!sign_flag) goto loc_00C2BBA8;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(a2 + 9, a2, v_rsp - 56 - 40, a4);
    if ((*(unsigned int *)(v_rip + 3546429)) != 0) goto loc_00C2B38B;
    *(unsigned int *)(v_rip + 3546413) = 6;
    goto loc_00C2B38B;
loc_00C2BBA8:
    if ((unsigned int)(v_r14) != 0) {
        a1 = 8;
        a2 = 774;
        result = WheaSelLogCheckPoint(a1, a2, v_rsp - 56 - 40, a4);
    }
    if (((*(unsigned __int8 *)(v_rip + 3546387)) & (8)) != 0) {
        a2 = v_rip - 12623218;
        a1 = v_rip + 1946191;
        result = McTemplateK0_EtwWriteTransfer(a1, a2, v_rsp - 56 - 40, a4);
    }
    result = MmRegisterHotPatches(a1, a2, v_rsp - 56 - 40, a4);
    if (((*(unsigned __int8 *)(v_rip + 3546351)) & (8)) != 0) {
        a2 = v_rip - 12621640;
        a1 = v_rip + 1946153;
        result = McTemplateK0_EtwWriteTransfer(a1, a2, v_rsp - 56 - 40, a4);
    }
    if (!sign_flag) goto loc_00C2BC0F;
    *(unsigned int *)(v_rip + 3546310) = 21;
    goto loc_00C2B38B;
loc_00C2BC0F:
    result = PoInitSystem(2, a1, v_rsp - 56 - 40, a4);
    if ((unsigned __int8)(result) == 0) {
        a1 = 160;
        result = KeBugCheck(a1, a1, v_rsp - 56 - 40, a4);
    }
    if ((unsigned int)(v_r14) != 0) {
        a1 = 8;
        a2 = 7;
        result = WheaSelLogCheckPoint(a1, a2, v_rsp - 56 - 40, a4);
    }
    result = SmInitSystem((unsigned int)((unsigned int)(v_r12 + 1)), a2, v_rsp - 56 - 40, a4);
    result = EtwInitialize(2, a1, v_rsp - 56 - 40, a4);
    result = VslRegisterIumPowerCallbacks(2, a1, v_rsp - 56 - 40, a4);
    result = IopInitializeSystemVariableService(2, a1, v_rsp - 56 - 40, a4);
    result = SecureDump_ProvisionCrashDumpKey(2, a1, v_rsp - 56 - 40, a4);
    if ((*(unsigned __int8 *)(v_rip + 2335829)) == 0) goto loc_00C2BC77;
    result = IopDumpTraceForceDumpDisabled(2, a1, v_rsp - 56 - 40, a4);
    if ((*(unsigned __int8 *)(v_rip + 2335815)) != 0) goto loc_00C2BC8A;
loc_00C2BC77:
    result = IoInitializeLiveDump(2, a1, v_rsp - 56 - 40, a4);
    if ((*(unsigned __int8 *)(v_rip + 1961269)) == 0) {
        result = IopLiveDumpTraceDumpDisabledOnBoot(2, a1, v_rsp - 56 - 40, a4);
    }
    result = IopInitializeBugCheckDriverData(2, a1, v_rsp - 56 - 40, a4);
    result = IopInitializeTriageDumpData(2, a1, v_rsp - 56 - 40, a4);
    if (((*(unsigned __int8 *)(v_rip + 3546169)) & (16)) != 0) {
        a2 = v_rip - 12618972;
        a1 = v_rip + 1945973;
        result = McTemplateK0_EtwWriteTransfer(a1, a2, v_rsp - 56 - 40, a4);
    }
    a2 = 0;
    result = WheaSelLogCheckPoint(83, a2, v_rsp - 56 - 40, a4);
    a2 = 0;
    result = IopInitCrashDumpDuringSysInit(a1, a2, v_rsp - 56 - 40, a4);
    if (((*(unsigned __int8 *)(v_rip + 3546119)) & (16)) != 0) {
        a4 = (unsigned int)(result);
        a2 = v_rip - 12618811;
        a1 = v_rip + 1945918;
        result = McTemplateK0q_EtwWriteTransfer(a1, a2, v_rsp - 56 - 40, a4);
    }
    if ((unsigned int)(v_r14) != 0) {
        a1 = 80;
        a2 = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = WheaSelLogCheckPoint(a1, a2, v_rsp - 56 - 40, a4);
    }
    if (sign_flag) goto loc_00C2BD03;
    result = IopRemoveDumpCapsuleSupport(a1, a2, v_rsp - 56 - 40, a4);
    goto loc_00C2BD11;
loc_00C2BD03:
    if ((*(unsigned __int8 *)(v_rip + 1961136)) == 0) {
        result = IopTraceCrashDumpDisabledOnBoot(a1, a2, v_rsp - 56 - 40, a4);
    }
    result = RtlIsStateSeparationEnabled(a1, a2, v_rsp - 56 - 40, a4);
    if ((unsigned __int8)(result) == 0) {
        result = PpLastGoodDoBootProcessing(a1, a2, v_rsp - 56 - 40, a4);
    }
    *(unsigned int *)(v_rip + 3769743) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3769755)))));
    result = PsLocateSystemDlls(a1, a2, v_rsp - 56 - 40, a4);
    *(unsigned int *)(v_rip + 3769732) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3769755)));
    if (!sign_flag) goto loc_00C2BD5F;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(a2 + 10, a2, v_rsp - 56 - 40, a4);
    *(unsigned int *)(v_rip + 3545974) = 7;
    goto loc_00C2BEE5;
loc_00C2BD5F:
    result = MmInitializeImageViewExtension((unsigned int)((unsigned int)(v_r12 + 1)), a2, v_rsp - 56 - 40, a4);
    a1 = 0;
    result = PfSnBeginBootPhase(a1, a2, v_rsp - 56 - 40, a4);
    result = IopReassignSystemRoot(0, v_rsp - 56 - 80, v_rsp - 56 - 40, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00C2BD97;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(a2 + 12, a2, v_rsp - 56 - 40, a4);
    *(unsigned int *)(v_rip + 3545918) = 9;
    goto loc_00C2B076;
loc_00C2BD97:
    result = IopProtectSystemPartition(0, a2, v_rsp - 56 - 40, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00C2BDBC;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(a2 + 13, a2, v_rsp - 56 - 40, a4);
    *(unsigned int *)(v_rip + 3545881) = 10;
    goto loc_00C2B076;
loc_00C2BDBC:
    result = (*(unsigned __int64 *)(v_rip + 2922237)) + (72);
    v_stack_m110 = 0;
    *(unsigned __int64 *)(v_rsp - 56 - 128) = result;
    v_stack_mC8 = 48;
    v_stack_mC0 = 0;
    *(unsigned int *)(v_rsp - 56 - 120) = 576;
    *(unsigned __int64 *)(v_rsp - 56 - 112) = v_xmm0;
    v_stack_m118 = (unsigned int)(v_r12 + 1);
    result = ZwOpenFile(v_stack_mF0, (unsigned int)(0x80000000ULL), v_stack_mC8, v_rsp - 56 - 56);
    if (sign_flag) goto loc_00C2BE5D;
    v_stack_m110 = 0;
    a4 = 0;
    a3 = 0;
    v_stack_m118 = v_stack_mE0;
    v_stack_mE0 = 0;
    result = ObReferenceObjectByHandle(v_stack_mF0, 128, a3, a4);
    if (!(sign_flag)) {
        a1 = v_stack_mE0;
        result = PpPagePathAssign(a1, 128, a3, a4);
        a1 = v_stack_mE0;
        a2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(a1, a2, a3, a4);
    }
    result = ZwClose(v_stack_mF0, a2, a3, a4);
loc_00C2BE5D:
    a2 = 0;
    result = WMIInitialize((unsigned int)((unsigned int)(v_r12 + 1)), a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00C2BE7A;
    *(unsigned int *)(v_rip + 3545691) = 25;
    goto loc_00C2B076;
loc_00C2BE7A:
    if ((unsigned int)(v_r14) != 0) {
        a1 = 8;
        a2 = (unsigned int)(a1);
        result = WheaSelLogCheckPoint(a1, a2, a3, a4);
    }
    if (((*(unsigned __int8 *)(v_rip + 3545666)) & (16)) != 0) {
        a4 = (unsigned int)(v_r12 + 1);
        a2 = v_rip - 12620774;
        a1 = v_rip + 1945467;
        result = McTemplateK0q_EtwWriteTransfer(a1, a2, a3, a4);
    }
    result = WheaInitialize(a1, (unsigned int)((unsigned int)(v_r12 + 1)), a3, a4);
    if (((*(unsigned __int8 *)(v_rip + 3545624)) & (16)) != 0) {
        a2 = v_rip - 12627629;
        a1 = v_rip + 1945428;
        result = McTemplateK0_EtwWriteTransfer(a1, a2, a3, a4);
    }
    if ((unsigned int)(v_r14) != 0) {
        a1 = 8;
        a2 = a1 + 1;
        result = WheaSelLogCheckPoint(a1, a2, a3, a4);
    }
    result = 0;
loc_00C2BEE5:
    a1 = (*(unsigned __int64 *)(v_rsp - 56)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoInitSystemPreDrivers(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint16_t v_stack_m108;
    uint64_t v_stack_m110;
    uint16_t v_stack_m118;
    uint64_t v_stack_m28;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint8_t v_stack_mF8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0x1DFADA)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x38) = result;
    local_r12 = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x50) = 0x1000000ULL;
    *(uint64_t *)(local_rsp - 0x38 - 0x40) = 0;
    v_stack_mC4 = 0;
    *(uint32_t *)(local_rsp - 0x38 - 0x74) = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x48) = v_rip + 4055874;
    local_rbx = (uint32_t)((local_rbx) | (0xFFFFFFFFULL));
    *(uint64_t *)(local_rsp - 0x38 - 0x60) = v_xmm0;
    v_stack_mF0 = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x38) = v_xmm0;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x84))) & (0x80000ULL));
    v_stack_mF8 = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x28) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x38 - 0x18) = v_xmm1;
    result = ExInitializeResourceLite2(v_rip + 3548909, (uint32_t)((uint32_t)(local_rbx)), a3, a4);
    result = ExInitializeResourceLite2(v_rip + 3548734, (uint32_t)((uint32_t)(local_rbx)), a3, a4);
    result = ExInitializeResourceLite2(v_rip + 3548592, (uint32_t)((uint32_t)(local_rbx)), a3, a4);
    result = ExInitializeResourceLite2(v_rip + 3554306, (uint32_t)((uint32_t)(local_rbx)), a3, a4);
    result = ExInitializeResourceLite2(v_rip + 3548052, (uint32_t)((uint32_t)(local_rbx)), a3, a4);
    *(uint64_t *)(v_rip + 0x362571) = 0;
    *(uint64_t *)(v_rip + 0x362562) = v_rip + 3548520;
    *(uint64_t *)(v_rip + 0x362550) = v_rip + 3548520;
    *(uint64_t *)(v_rip + 0x36253A) = v_rip + 3548473;
    *(uint64_t *)(v_rip + 0x36252B) = v_rip + 3548473;
    *(uint64_t *)(v_rip + 0x362515) = v_rip + 3548436;
    *(uint64_t *)(v_rip + 0x362506) = v_rip + 3548436;
    *(uint64_t *)(v_rip + 0x3624F0) = v_rip + 3548399;
    *(uint64_t *)(v_rip + 0x3624E1) = v_rip + 3548399;
    *(uint64_t *)(v_rip + 0x3624CB) = v_rip + 3548362;
    *(uint64_t *)(v_rip + 0x3624BC) = v_rip + 3548362;
    *(uint64_t *)(v_rip + 0x3624A6) = v_rip + 3548325;
    *(uint64_t *)(v_rip + 0x362497) = v_rip + 3548325;
    *(uint64_t *)(v_rip + 0x362481) = v_rip + 3548288;
    *(uint64_t *)(v_rip + 0x362472) = v_rip + 3548288;
    *(uint64_t *)(v_rip + 0x3626AC) = v_rip + 3548843;
    *(uint64_t *)(v_rip + 0x36269D) = v_rip + 3548843;
    *(uint64_t *)(v_rip + 0x362687) = v_rip + 3548806;
    *(uint64_t *)(v_rip + 0x362678) = v_rip + 3548806;
    *(uint64_t *)(v_rip + 0x362662) = v_rip + 3548769;
    *(uint64_t *)(v_rip + 0x362653) = v_rip + 3548769;
    *(uint64_t *)(v_rip + 0x362644) = 0;
    *(uint64_t *)(v_rip + 0x3A4B05) = 0;
    *(uint64_t *)(v_rip + 0x36262E) = 0;
    *(uint64_t *)(v_rip + 0x362616) = v_xmm0;
    *(uint32_t *)(v_rip + 0x362603) = 0;
    a2 = ((uint32_t)((uint32_t)(local_rbx))) << (32);
    result = (v_rip + 3548769) | (a2);
    *(uint32_t *)(v_rip + 0x3623EA) = 0;
    a3 = (result) >> (4);
    Arg1 = (a3) - (a2);
    Arg1 = (Arg1) >> (1);
    Arg1 = (Arg1) + (a2);
    Arg1 = (Arg1) >> (6);
    Arg1 = (Arg1) * (Arg1);
    a3 = (a3) - (Arg1);
    a3 = (uint32_t)((a3) + (10));
    *(uint32_t *)(v_rip + 0x3625AA) = (uint32_t)(a3);
    result = 0;
    if ((*(uint32_t *)(v_rip + 0x3625AD)) == 0) {
        *(uint32_t *)(v_rip + 0x36259A) = 14;
        result = (uint32_t)(local_r12 + 1);
        *(uint32_t *)(v_rip + 0x362394) = (uint32_t)(local_r12 + 1);
    }
    if ((*(uint32_t *)(v_rip + 0x362585)) == 0) {
        result = (uint32_t)((result) | (2));
        *(uint32_t *)(v_rip + 0x362575) = 4;
        *(uint32_t *)(v_rip + 0x362377) = (uint32_t)(result);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x23B25D))) + (-2));
    if (((uint32_t)(result)) >= = 298) {
        *(uint32_t *)(v_rip + 0x23B249) = 300;
    }
    result = IopQueryProcessorInitValues(local_rsp - 56 - 40, a2, a3, a4);
    v_stack_m110 = v_rip + 2948409;
    v_stack_m118 = (uint16_t)(*(uint16_t *)(local_rsp - 0x38 - 0x22));
    result = ExInitializeSystemLookasideList(v_rip + 1996185, 512, 56, (uint32_t)(0x20706349ULL));
    v_stack_m110 = v_rip + 2948409;
    v_stack_m118 = (uint16_t)(*(uint16_t *)(local_rsp - 0x38 - 0x24));
    result = ExInitializeSystemLookasideList(v_rip + 1996291, 512, (uint32_t)(*(uint32_t *)(local_rsp - 0x38 - 0x14)), (uint32_t)(0x6C707249ULL));
    v_stack_m110 = v_rip + 2948409;
    v_stack_m118 = (uint16_t)(*(uint16_t *)(local_rsp - 0x38 - 0x26));
    result = ExInitializeSystemLookasideList(v_rip + 1996380, 512, (uint32_t)(*(uint32_t *)(local_rsp - 0x38 - 0x18)), (uint32_t)(0x6D707249ULL));
    v_stack_m110 = v_rip + 2948409;
    v_stack_m118 = (uint16_t)(*(uint16_t *)(local_rsp - 0x38 - 0x28));
    result = ExInitializeSystemLookasideList(v_rip + 1996469, 512, (uint32_t)(*(uint32_t *)(local_rsp - 0x38 - 0x1C)), (uint32_t)(0x73707249ULL));
    v_stack_m110 = v_rip + 2948409;
    v_stack_m118 = (uint16_t)(*(uint16_t *)(local_rsp - 0x38 - 0x20));
    result = ExInitializeSystemLookasideList(v_rip + 1996558, 512, (uint32_t)(*(uint32_t *)(local_rsp - 0x38 - 0x10)), (uint32_t)(0x206C644DULL));
    v_stack_m100 = 0;
    v_stack_m108 = 0;
    v_stack_m110 = 0x73556F49ULL;
    v_stack_m118 = 32;
    a3 = 0;
    a2 = 0;
    result = ExInitializeNPagedLookasideListInternal(v_rip + 1995622, a2, a3, 512);
    a2 = 0;
    result = FsRtlInitExtraCreateParameterLookasideList(v_rip + 1995698, a2, 286, (uint32_t)(0x69536F49ULL));
    v_stack_m100 = 0;
    v_stack_m108 = 0;
    v_stack_m110 = 0x7443704FULL;
    a3 = 0;
    a2 = 0;
    v_stack_m118 = 48;
    result = ExInitializeNPagedLookasideListInternal(v_rip + 1995797, a2, a3, 512);
    result = KeQueryActiveProcessorCountEx((uint32_t)(0xFFFFULL), a2, a3, 512);
    v_stack_mE8 = 0;
    if ((uint32_t)(result) == 0) goto loc_00C2B04A;
loc_00C2B027:
    result = IoInitializeProcessor(*(uint64_t *)(v_rip + 0x39DC12 + 0x0 * 8), local_rsp - 56 - 40, a3, 512);
    Arg1 = (uint32_t)(((uint32_t)(v_stack_mE8)) + ((uint32_t)(local_r12 + 1)));
    v_stack_mE8 = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_00C2B027;
loc_00C2B04A:
    *(uint64_t *)(v_rip + 0x3A4168) = 0;
    *(uint64_t *)(v_rip + 0x362619) = v_rip + 3548703;
    *(uint64_t *)(v_rip + 0x36260A) = v_rip + 3548703;
    result = IopInitializeReserveIrps(Arg1, local_rsp - 56 - 40, a3, 512);
    if ((uint8_t)(result) != 0) goto loc_00C2B080;
    *(uint32_t *)(v_rip + 0x36285A) = (uint32_t)(local_r12 + 1);
loc_00C2B076:
    goto loc_00C2BEE5;
loc_00C2B080:
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x36218A));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x36218A)))) & (3)) != 0) {
        Arg1 = v_rip - 8084593;
        *(uint32_t *)(v_rip + 0x3624C9) = 400;
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x36218A))) | (4));
        *(void **)(v_rip + 0x362494) = Arg1;
        *(uint32_t *)(v_rip + 0x362166) = (uint32_t)(result);
        *(uint32_t *)(v_rip + 0x3624AC) = 0x7D0ULL;
        *(uint32_t *)(v_rip + 0x362462) = 275;
        *(uint64_t *)(v_rip + 0x36247B) = 0;
        *(uint64_t *)(v_rip + 0x36248C) = 0;
        *(uint64_t *)(v_rip + 0x36245D) = 0;
    }
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x1DF8EB));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1DF8EB)))) >= ((uint32_t)((uint32_t)(0x400000ULL)))) {
        result = (uint32_t)((uint32_t)(0x400000ULL));
        *(uint32_t *)(v_rip + 0x1DF8DA) = (uint32_t)((uint32_t)(0x400000ULL));
    }
    if (((uint32_t)(result)) <= 0x1000ULL) {
        *(uint32_t *)(v_rip + 0x1DF8C9) = 0x1000ULL;
    }
    v_stack_mC8 = 48;
    *(uint64_t *)(local_rsp - 0x38 - 0x80) = v_rip + 3863270;
    v_stack_mC0 = 0;
    *(uint32_t *)(local_rsp - 0x38 - 0x78) = 576;
    *(uint64_t *)(local_rsp - 0x38 - 0x70) = v_xmm0;
    result = ZwOpenKey(v_stack_mF0, (uint32_t)(0x20019ULL), v_stack_mC8, 512);
    if (sign_flag) goto loc_00C2B1A2;
    result = RtlInitUnicodeString(local_rsp - 56 - 96, v_rip + 321583, v_stack_mC8, 512);
    v_stack_m110 = v_stack_mE8;
    v_stack_m118 = 32;
    result = NtQueryValueKey(v_stack_mF0, local_rsp - 56 - 96, 2, v_rip + 4052808);
    if (sign_flag) goto loc_00C2B18B;
    if ((*(uint32_t *)(v_rip + 0x3DD72E)) != 4) goto loc_00C2B18B;
    result = ((*(uint32_t *)(v_rip + 0x3DD72E)) == 4) ? 1 : 0;
    goto loc_00C2B18E;
loc_00C2B18B:
loc_00C2B18E:
    a2 = 0;
    *(uint8_t *)(v_rip + 0x361EBF) = (uint8_t)((uint8_t)(local_r12 + 1));
    result = ObCloseHandle(v_stack_mF0, a2, 2, v_rip + 4052808);
    goto loc_00C2B1A9;
loc_00C2B1A2:
    *(uint8_t *)(v_rip + 0x361EB1) = (uint8_t)(local_r12 + 1);
loc_00C2B1A9:
    *(uint64_t *)(v_rip + 0x3622C9) = 0;
    *(uint64_t *)(v_rip + 0x36235A) = v_rip + 3548000;
    *(uint64_t *)(v_rip + 0x362345) = v_rip + 3548000;
    *(uint64_t *)(v_rip + 0x3622FF) = v_rip - 8943826;
    *(uint64_t *)(v_rip + 0x3622F9) = v_rip + 3547936;
    *(uint64_t *)(v_rip + 0x36229B) = v_rip + 3547802;
    *(uint64_t *)(v_rip + 0x36228C) = v_rip + 3547802;
    *(uint64_t *)(v_rip + 0x36226E) = v_rip + 3547757;
    *(uint64_t *)(v_rip + 0x36225F) = v_rip + 3547757;
    *(uint64_t *)(v_rip + 0x362571) = v_rip - 5307272;
    *(uint64_t *)(v_rip + 0x36257B) = v_rip + 3548538;
    *(uint64_t *)(v_rip + 0x36256C) = v_rip + 3548538;
    *(uint64_t *)(v_rip + 0x362586) = v_rip + 3548549;
    *(uint64_t *)(v_rip + 0x362577) = v_rip + 3548549;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x1DF76D))) + (0xFFFFFC18ULL));
    *(uint64_t *)(v_rip + 0x3A3EE5) = 0;
    *(uint32_t *)(v_rip + 0x36225B) = 275;
    *(uint64_t *)(v_rip + 0x36228C) = 0;
    *(uint64_t *)(v_rip + 0x36225D) = 0;
    *(uint8_t *)(v_rip + 0x362206) = 9;
    *(uint64_t *)(v_rip + 0x362217) = 0;
    *(uint32_t *)(v_rip + 0x362234) = 0;
    *(uint16_t *)(v_rip + 0x362228) = 0;
    *(uint64_t *)(v_rip + 0x362501) = 0;
    *(uint64_t *)(v_rip + 0x3624E2) = 0;
    *(uint64_t *)(v_rip + 0x36250B) = 0;
    *(uint8_t *)(v_rip + 0x36250C) = 5;
    *(uint8_t *)(v_rip + 0x362507) = 8;
    *(uint32_t *)(v_rip + 0x362502) = 0;
    *(uint32_t *)(v_rip + 0x36250C) = 0x7FFFFFFFULL;
    *(uint8_t *)(v_rip + 0x36250D) = 0;
    if (((uint32_t)(result)) >= = 0x2328ULL) {
        *(uint32_t *)(v_rip + 0x1DF6E0) = 0x1388ULL;
    }
    *(uint64_t *)(v_rip + 0x36242E) = 0;
    *(uint64_t *)(v_rip + 0x36241F) = v_rip - 7955219;
    *(uint64_t *)(v_rip + 0x3623FA) = 0;
    *(uint64_t *)(v_rip + 0x362417) = v_rip + 3548193;
    *(uint64_t *)(v_rip + 0x362408) = v_rip + 3548193;
    *(uint64_t *)(v_rip + 0x362411) = 0;
    *(uint8_t *)(v_rip + 0x362432) = 0;
    *(uint8_t *)(v_rip + 0x361D2E) = (uint8_t)(local_r12 + 1);
    result = RtlInitUnicodeString(local_rsp - 56 - 96, v_rip + 321096, 2, v_rip + 4052808);
    v_stack_mC8 = 48;
    *(uint64_t *)(local_rsp - 0x38 - 0x80) = local_rsp - 56 - 96;
    a4 = 0;
    v_stack_mC0 = 0;
    *(uint32_t *)(local_rsp - 0x38 - 0x78) = 528;
    v_stack_m118 = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x70) = v_xmm0;
    result = NtCreateEvent(v_stack_mF0, (uint32_t)(0x1F0003ULL), v_stack_mC8, a4);
    if (!sign_flag) goto loc_00C2B392;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(4, a2, v_stack_mC8, a4);
    *(uint32_t *)(v_rip + 0x362545) = 26;
loc_00C2B38B:
    goto loc_00C2BEE5;
loc_00C2B392:
    a4 = 0;
    v_stack_m110 = 0;
    a2 = 0;
    v_stack_m118 = v_stack_mD8;
    v_stack_mD8 = 0;
    result = ObReferenceObjectByHandle(v_stack_mF0, a2, *(uint64_t *)(v_rip + 0x39B7E7), a4);
    a2 = 0;
    *(uint64_t *)(v_rip + 0x3AEBB4) = v_stack_mD8;
    *(uint64_t *)(v_rip + 0x36230E) = v_rip + 3547917;
    *(uint64_t *)(v_rip + 0x3622FF) = v_rip + 3547917;
    *(uint64_t *)(v_rip + 0x3622D9) = v_rip + 3547864;
    *(uint64_t *)(v_rip + 0x3622CA) = v_rip + 3547864;
    *(uint64_t *)(v_rip + 0x362284) = v_rip + 3547779;
    *(uint64_t *)(v_rip + 0x362275) = v_rip + 3547779;
    *(uint16_t *)(v_rip + 0x3622C5) = 0;
    *(uint8_t *)(v_rip + 0x3622C1) = 6;
    *(uint32_t *)(v_rip + 0x3622BC) = 0;
    *(uint16_t *)(v_rip + 0x362290) = 0;
    *(uint8_t *)(v_rip + 0x36228C) = 6;
    *(uint32_t *)(v_rip + 0x362287) = 0;
    *(uint16_t *)(v_rip + 0x36223B) = (uint16_t)(local_r12 + 1);
    *(uint8_t *)(v_rip + 0x362237) = 6;
    *(uint32_t *)(v_rip + 0x362232) = (uint32_t)(local_r12 + 1);
    result = ObCloseHandle(v_stack_mF0, a2, *(uint64_t *)(v_rip + 0x39B7E7), a4);
    result = IopCreateRootDirectories(v_stack_mF0, a2, *(uint64_t *)(v_rip + 0x39B7E7), a4);
    if ((uint8_t)(result) != 0) goto loc_00C2B478;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(6, a2, *(uint64_t *)(v_rip + 0x39B7E7), a4);
    *(uint32_t *)(v_rip + 0x36245D) = 3;
    goto loc_00C2B076;
loc_00C2B478:
    result = IopInitializeSessionNotifications(6, a2, *(uint64_t *)(v_rip + 0x39B7E7), a4);
    if (!sign_flag) goto loc_00C2B490;
    *(uint32_t *)(v_rip + 0x362445) = 15;
    goto loc_00C2BEE5;
loc_00C2B490:
    a2 = 0;
    result = IopInitializePlugPlayServices(Arg1, a2, *(uint64_t *)(v_rip + 0x39B7E7), a4);
    if (!sign_flag) goto loc_00C2B4B5;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(a2 + 7, a2, *(uint64_t *)(v_rip + 0x39B7E7), a4);
    *(uint32_t *)(v_rip + 0x362420) = 4;
    goto loc_00C2B38B;
loc_00C2B4B5:
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = 8;
        a2 = (uint32_t)(local_r12 + 1);
        result = WheaSelLogCheckPoint(Arg1, a2, *(uint64_t *)(v_rip + 0x39B7E7), a4);
    }
    a2 = 0;
    result = KseInitialize(Arg1, a2, *(uint64_t *)(v_rip + 0x39B7E7), a4);
    result = PoInitDriverServices(Arg1, a2, *(uint64_t *)(v_rip + 0x39B7E7), a4);
    result = guard_dispatch_icall(Arg1, a2, *(uint64_t *)(v_rip + 0x39B7E7), a4);
loc_00C2B4EB:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x360F51) + 0x8) == 0) goto loc_00C2B51F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x360F51) + 0x8) + 0x12C))) - (777));
    if (((uint32_t)(result)) > ((uint32_t)(local_r12 + 1))) goto loc_00C2B50C;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x360F51) + 0x8) + 0x18C)) & (0x1000ULL)) == 0) goto loc_00C2B511;
loc_00C2B50C:
    goto loc_00C2B4EB;
loc_00C2B511:
    *(uint64_t *)(v_rip + 0x3DD176) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x360F51) + 0x8));
    result = PipSetDevNodeFlags(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x360F51) + 0x8)), 4, *(uint64_t *)(v_rip + 0x39B7E7), a4);
loc_00C2B51F:
    Arg1 = 0;
    result = WMIInitialize(Arg1, Arg1, *(uint64_t *)(v_rip + 0x39B7E7), a4);
    if ((uint8_t)(result) != 0) goto loc_00C2B53C;
    *(uint32_t *)(v_rip + 0x362399) = 18;
    goto loc_00C2B076;
loc_00C2B53C:
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = 8;
        a2 = 2;
        result = WheaSelLogCheckPoint(Arg1, a2, *(uint64_t *)(v_rip + 0x39B7E7), a4);
    }
    result = CmIsStateSeparationDevModeEnabled(Arg1, a2, *(uint64_t *)(v_rip + 0x39B7E7), a4);
    result = RtlIsStateSeparationEnabled(Arg1, a2, *(uint64_t *)(v_rip + 0x39B7E7), a4);
    result = kernel_indirect_call((uint8_t)(result), (uint8_t)((uint8_t)(result)), *(uint64_t *)(v_rip + 0x39B7E7), a4);
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result + (uint32_t)(0x80000000ULL) * 1))) != 0) goto loc_00C2B58C;
    if (((uint32_t)(result)) == 0xC00000BBULL) goto loc_00C2B58C;
    *(uint32_t *)(v_rip + 0x362349) = 19;
    goto loc_00C2BEE5;
loc_00C2B58C:
    v_stack_mE0 = 0;
    result = RtlGetNtProductType(v_stack_mE0, (uint32_t)(0x80000000ULL), *(uint64_t *)(v_rip + 0x39B7E7), a4);
    if ((uint8_t)(result) == 0) goto loc_00C2B5E5;
    if (v_stack_mE0 != ((uint32_t)(local_r12 + 1))) goto loc_00C2B5E5;
    *(uint8_t *)(v_rip + 0x361AA6) = (uint8_t)(local_r12 + 1);
    result = ExAllocatePool2(256, (uint32_t)(0x1000ULL), (uint32_t)(0x6E446341ULL), a4);
    if (result != 0) goto loc_00C2B5DB;
    *(uint32_t *)(v_rip + 0x3622FF) = 17;
    goto loc_00C2BEE5;
loc_00C2B5DB:
    result = AstInitializeBloomFilter(256, (uint32_t)(0x1000ULL), (uint32_t)(0xC0000017ULL), a4);
    goto loc_00C2B5EC;
loc_00C2B5E5:
    *(uint8_t *)(v_rip + 0x361A6C) = 0;
loc_00C2B5EC:
    result = EtwInitialize((uint32_t)((uint32_t)(local_r12 + 1)), Arg1, (uint32_t)(0xC0000017ULL), a4);
    a3 = 0;
    result = EtwRegister(v_rip - 12615911, v_rip - 5308856, a3, v_rip + 3547618);
    if (!sign_flag) goto loc_00C2B628;
    *(uint32_t *)(v_rip + 0x3622AD) = 16;
    goto loc_00C2BEE5;
loc_00C2B628:
    result = McGenEventRegister_EtwRegister(v_rip - 12623893, v_rip - 5308856, v_rip + 1947626, v_rip + 1947633);
    if (!sign_flag) goto loc_00C2B655;
    *(uint32_t *)(v_rip + 0x362280) = 11;
    goto loc_00C2BEE5;
loc_00C2B655:
    a3 = 0;
    result = TlgRegisterAggregateProviderEx(v_rip + 1960444, v_rip - 1528153, a3, v_rip + 1947633);
    if (!sign_flag) goto loc_00C2B681;
    *(uint32_t *)(v_rip + 0x362254) = 22;
    goto loc_00C2BEE5;
loc_00C2B681:
    *(uint64_t *)(v_rip + 0x20BF90) = v_rip + 1960444;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x204C32));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x204C32))) != 0) {
        a3 = 0;
        a2 = (uint32_t)((v_rip - 1528153) | (0xFFFFFFFFULL));
        Arg1 = 0;
        result = MiLogBadMapper(Arg1, a2, a3, v_rip + 1947633);
    }
    a3 = 0;
    result = EtwRegister(v_rip - 12622519, v_rip - 6906592, a3, v_rip + 2336842);
    a3 = 0;
    a2 = 0;
    result = TraceLoggingRegisterEx_EtwRegister_EtwSetInformation(v_rip + 1947426, a2, a3, v_rip + 2336842);
    result = IopInitializeDumpPolicySettings((uint8_t)(local_r12 + 1), a2, a3, v_rip + 2336842);
    result = TlgRegisterAggregateProvider(v_rip + 1947532, a2, a3, v_rip + 2336842);
    result = SeAuditBootConfiguration(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xB40), a2, a3, v_rip + 2336842);
    result = BootApplicationPersistentDataProcess((uint32_t)((uint32_t)(local_r12 + 1)), a2, a3, v_rip + 2336842);
    a2 = 0;
    result = kernel_indirect_call(a2 + 2, a2, v_rip + 3260123, v_rip + 2336842);
    result = KeInitSystem(2, a2, v_rip + 3260123, v_rip + 2336842);
    if ((*(uint8_t *)(v_rip + 0x361935)) != 0) goto loc_00C2B787;
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 3816082, a2, v_rip + 3260123, v_rip + 2336842);
    if ((*(uint64_t *)(v_rip + 0x361F2D)) != (v_rip + 3546932)) goto loc_00C2B74E;
    *(uint8_t *)(v_rip + 0x36190F) = 0;
    goto loc_00C2B779;
loc_00C2B74E:
    *(uint64_t *)(v_rip + 0x36191C) = 0;
    *(uint64_t *)(v_rip + 0x36190A) = v_rip - 1891029;
    *(uint64_t *)(v_rip + 0x3618EC) = 0;
    result = ExQueueWorkItem(v_rip + 3545331, (uint32_t)((uint32_t)(local_r12 + 1)), v_rip + 3260123, v_rip + 2336842);
loc_00C2B779:
    result = KeReleaseSpinLock(v_rip + 3815998, (uint8_t)((uint8_t)(result)), v_rip + 3260123, v_rip + 2336842);
loc_00C2B787:
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = 8;
        a2 = 3;
        result = WheaSelLogCheckPoint(Arg1, a2, v_rip + 3260123, v_rip + 2336842);
    }
    if (((*(uint8_t *)(v_rip + 0x36212F)) & (16)) != 0) {
        a4 = 0;
        a2 = v_rip - 12619001;
        Arg1 = v_rip + 1947240;
        result = McTemplateK0q_EtwWriteTransfer(Arg1, a2, v_rip + 3260123, a4);
    }
    a2 = 0;
    result = WheaInitialize(Arg1, a2, v_rip + 3260123, a4);
    if (((*(uint8_t *)(v_rip + 0x362106)) & (16)) != 0) {
        a2 = v_rip - 12625855;
        Arg1 = v_rip + 1947202;
        result = McTemplateK0_EtwWriteTransfer(Arg1, a2, v_rip + 3260123, a4);
    }
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = 8;
        a2 = 4;
        result = WheaSelLogCheckPoint(Arg1, a2, v_rip + 3260123, a4);
    }
    result = IopStoreArcInformation(Arg1, a2, v_rip + 3260123, a4);
    if (!sign_flag) goto loc_00C2B810;
    *(uint32_t *)(v_rip + 0x3620C5) = 20;
    goto loc_00C2BEE5;
loc_00C2B810:
    result = IopInitializePlugPlayServices(Arg1, (uint32_t)((uint32_t)(local_r12 + 1)), v_rip + 3260123, a4);
    if (!sign_flag) goto loc_00C2B83A;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(8, a2, v_rip + 3260123, a4);
    *(uint32_t *)(v_rip + 0x36209B) = 5;
    goto loc_00C2B38B;
loc_00C2B83A:
    a2 = 0;
    result = memset(v_rip + 3547069, a2, a2 + 104, a4);
    *(uint64_t *)(v_rip + 0x361FA3) = v_rip + 3547069;
    *(uint64_t *)(v_rip + 0x361FE4) = v_rip - 2632438;
    *(uint64_t *)(v_rip + 0x361FE9) = 0;
    *(uint64_t *)(v_rip + 0x361FD2) = v_rip - 5311296;
    *(uint32_t *)(v_rip + 0x361FF1) = (uint32_t)(local_r12 + 1);
    *(uint64_t *)(v_rip + 0x361FC2) = v_rip - 5309448;
    *(uint64_t *)(v_rip + 0x362004) = v_rip + 3547139;
    *(uint64_t *)(v_rip + 0x361FF5) = v_rip + 3547139;
    *(uint64_t *)(v_rip + 0x361FD6) = 0;
    *(uint32_t *)(v_rip + 0x361FD7) = 0;
    *(uint16_t *)(v_rip + 0x361FD7) = (uint16_t)(local_r12 + 1);
    *(uint8_t *)(v_rip + 0x361FD3) = 6;
    *(uint32_t *)(v_rip + 0x361FCE) = 0;
    result = KitpInitAitSampleRate(Arg1, a2, a2 + 104, a4);
    a3 = 0;
    a2 = 0;
    result = EtwRegister(v_rip - 12618734, a2, a3, v_rip + 2346246);
    if (sign_flag) {
        *(uint64_t *)(v_rip + 0x23CCEA) = 0;
    }
    result = KseInitialize(Arg1, (uint32_t)((uint32_t)(local_r12 + 1)), a3, v_rip + 2346246);
    result = HvlPhase2Initialize(Arg1, (uint32_t)((uint32_t)(local_r12 + 1)), a3, v_rip + 2346246);
    if (!sign_flag) goto loc_00C2B91C;
    *(uint32_t *)(v_rip + 0x361FB9) = 23;
    goto loc_00C2BEE5;
loc_00C2B91C:
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = 8;
        a2 = 5;
        result = WheaSelLogCheckPoint(Arg1, a2, a3, v_rip + 2346246);
    }
    Arg1 = 0;
    result = KeOptimizeSpecCtrlSettings(Arg1, a2, a3, v_rip + 2346246);
    result = PsInitializeSyscallProviders(Arg1, a2, a3, v_rip + 2346246);
    result = VslpIumPhase4Initialize(Arg1, a2, a3, v_rip + 2346246);
    result = BootApplicationPersistentDataProcess(2, a2, a3, v_rip + 2346246);
    result = BapdRecordFirmwareBootStats(0, a2, a3, v_rip + 2346246);
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = 8;
        a2 = 6;
        result = WheaSelLogCheckPoint(Arg1, a2, a3, v_rip + 2346246);
    }
    if (*(uint64_t *)(v_rip + 0x23A971) != 0) {
        a4 = 0;
        v_stack_m118 = 0;
        a3 = v_rip + 1962101;
        a2 = v_rip - 12600706;
        result = EtwWriteStartScenario(*(uint64_t *)(v_rip + 0x23A971), a2, a3, a4);
    }
    *(uint16_t *)(v_rip + 0x36130A) = (uint16_t)(local_r12 + 1);
    *(uint64_t *)(v_rip + 0x36132B) = v_rip + 3543858;
    *(uint64_t *)(v_rip + 0x36131C) = v_rip + 3543858;
    *(uint64_t *)(v_rip + 0x3612FE) = v_rip + 3543805;
    *(uint64_t *)(v_rip + 0x3612EF) = v_rip + 3543805;
    *(uint8_t *)(v_rip + 0x3612E3) = 6;
    *(uint32_t *)(v_rip + 0x3612DE) = (uint32_t)(local_r12 + 1);
    result = IopQueryPassiveInterruptRegistryOptions(*(uint64_t *)(v_rip + 0x23A971), a2, a3, a4);
    *(uint64_t *)(v_rip + 0x3612B1) = v_rip + 3543735;
    *(uint64_t *)(v_rip + 0x3612A2) = v_rip + 3543735;
    *(uint64_t *)(v_rip + 0x36128B) = 0;
    result = KeInitializeQueue(v_rip + 3543648, *(uint8_t *)(v_rip + 0x1DF02F), a3, a4);
    result = IopCreatePassiveInterruptRealtimeThreads(v_rip + 3543648, *(uint8_t *)(v_rip + 0x1DF02F), a3, a4);
    if (!sign_flag) goto loc_00C2BA12;
    *(uint32_t *)(v_rip + 0x361EC3) = 24;
    goto loc_00C2BEE5;
loc_00C2BA12:
    result = SecureDump_PrepareForInit(v_rip + 3543648, v_stack_mF8, a3, a4);
    if ((*(uint8_t *)(v_rip + 0x23A699)) != 0) goto loc_00C2BA3C;
    if (v_stack_mF8 != 0) goto loc_00C2BA3C;
    if ((*(uint8_t *)(v_rip + 0x1DEF87)) == 0) goto loc_00C2BA3C;
    result = IopInitDumpCapsuleSupport(v_rip + 3543648, v_stack_mF8, a3, a4);
    goto loc_00C2BA43;
loc_00C2BA3C:
    *(uint8_t *)(v_rip + 0x1DEF76) = 0;
loc_00C2BA43:
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = 8;
        a2 = 262;
        result = WheaSelLogCheckPoint(Arg1, a2, a3, a4);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3AE169))) != 0) {
        result = EtwTraceLeapSecondDataParseFailure((uint32_t)(*(uint32_t *)(v_rip + 0x3AE169)), a2, a3, a4);
    }
    a4 = 0;
    Arg1 = 0;
    result = EtwTraceLeapSecondDataUpdate(Arg1, *(uint8_t *)(*(uint64_t *)(v_rip + 0x2D33CD)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x2D33CD) + 0x4)), a4);
    *(uint64_t *)(local_rsp - 0x38 - 0x28) = 0x10006ULL;
    v_stack_mD0 = v_rip - 12729108;
    *(uint64_t *)(local_rsp - 0x38 - 0x18) = 512;
    *(uint64_t *)(local_rsp - 0x38 - 0x20) = v_stack_mD8;
    v_stack_mD8 = (uint32_t)(local_r12 + 1);
    *(uint64_t *)(local_rsp - 0x38 - 0x10) = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x8) = 0;
    result = ExRegisterHost(v_rip + 3544711, *(uint8_t *)(*(uint64_t *)(v_rip + 0x2D33CD)), local_rsp - 56 - 40, a4);
    if (sign_flag) {
        *(uint64_t *)(v_rip + 0x361666) = 0;
    }
    *(uint64_t *)(v_rip + 0x2DAAB0) = 0;
    *(uint64_t *)(v_rip + 0x39B7E1) = v_rip - 6584913;
    *(uint64_t *)(v_rip + 0x362E7B) = v_rip - 8268854;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x108));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x108)))) & (2)) != 0) {
        result = v_rip - 6932686;
        *(uint64_t *)(v_rip + 0x362E63) = result;
    }
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = 8;
        a2 = 518;
        result = WheaSelLogCheckPoint(Arg1, a2, local_rsp - 56 - 40, a4);
    }
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x84)) & (0x100000ULL)) == 0) goto loc_00C2BB70;
    result = *(uint64_t *)(arg1 + 0xF0);
    if (((*(uint8_t *)(v_rip + 0x361DA3)) & (16)) != 0) {
        a2 = v_rip - 12618610;
        Arg1 = v_rip + 1946335;
        result = McTemplateK0_EtwWriteTransfer(Arg1, a2, local_rsp - 56 - 40, a4);
    }
    result = IopInitCrashDumpDuringSysInit(Arg1, (uint8_t)(local_r12 + 1), local_rsp - 56 - 40, a4);
    if (((*(uint8_t *)(v_rip + 0x361D7C)) & (16)) != 0) {
        a4 = (uint32_t)(result);
        a2 = v_rip - 12618436;
        Arg1 = v_rip + 1946293;
        result = McTemplateK0q_EtwWriteTransfer(Arg1, a2, local_rsp - 56 - 40, a4);
    }
    result = IopInitializeBootDrivers(Arg1, local_rsp - 56 - 64, local_rsp - 56 - 40, a4);
    if (!sign_flag) goto loc_00C2BBA8;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(a2 + 9, a2, local_rsp - 56 - 40, a4);
    if ((*(uint32_t *)(v_rip + 0x361D3D)) != 0) goto loc_00C2B38B;
    *(uint32_t *)(v_rip + 0x361D2D) = 6;
    goto loc_00C2B38B;
loc_00C2BBA8:
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = 8;
        a2 = 774;
        result = WheaSelLogCheckPoint(Arg1, a2, local_rsp - 56 - 40, a4);
    }
    if (((*(uint8_t *)(v_rip + 0x361D13)) & (8)) != 0) {
        a2 = v_rip - 12623218;
        Arg1 = v_rip + 1946191;
        result = McTemplateK0_EtwWriteTransfer(Arg1, a2, local_rsp - 56 - 40, a4);
    }
    result = MmRegisterHotPatches(Arg1, a2, local_rsp - 56 - 40, a4);
    if (((*(uint8_t *)(v_rip + 0x361CEF)) & (8)) != 0) {
        a2 = v_rip - 12621640;
        Arg1 = v_rip + 1946153;
        result = McTemplateK0_EtwWriteTransfer(Arg1, a2, local_rsp - 56 - 40, a4);
    }
    if (!sign_flag) goto loc_00C2BC0F;
    *(uint32_t *)(v_rip + 0x361CC6) = 21;
    goto loc_00C2B38B;
loc_00C2BC0F:
    result = PoInitSystem(2, Arg1, local_rsp - 56 - 40, a4);
    if ((uint8_t)(result) == 0) {
        Arg1 = 160;
        result = KeBugCheck(Arg1, Arg1, local_rsp - 56 - 40, a4);
    }
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = 8;
        a2 = 7;
        result = WheaSelLogCheckPoint(Arg1, a2, local_rsp - 56 - 40, a4);
    }
    result = SmInitSystem((uint32_t)((uint32_t)(local_r12 + 1)), a2, local_rsp - 56 - 40, a4);
    result = EtwInitialize(2, Arg1, local_rsp - 56 - 40, a4);
    result = VslRegisterIumPowerCallbacks(2, Arg1, local_rsp - 56 - 40, a4);
    result = IopInitializeSystemVariableService(2, Arg1, local_rsp - 56 - 40, a4);
    result = SecureDump_ProvisionCrashDumpKey(2, Arg1, local_rsp - 56 - 40, a4);
    if ((*(uint8_t *)(v_rip + 0x23A455)) == 0) goto loc_00C2BC77;
    result = IopDumpTraceForceDumpDisabled(2, Arg1, local_rsp - 56 - 40, a4);
    if ((*(uint8_t *)(v_rip + 0x23A447)) != 0) goto loc_00C2BC8A;
loc_00C2BC77:
    result = IoInitializeLiveDump(2, Arg1, local_rsp - 56 - 40, a4);
    if ((*(uint8_t *)(v_rip + 0x1DED35)) == 0) {
        result = IopLiveDumpTraceDumpDisabledOnBoot(2, Arg1, local_rsp - 56 - 40, a4);
    }
    result = IopInitializeBugCheckDriverData(2, Arg1, local_rsp - 56 - 40, a4);
    result = IopInitializeTriageDumpData(2, Arg1, local_rsp - 56 - 40, a4);
    if (((*(uint8_t *)(v_rip + 0x361C39)) & (16)) != 0) {
        a2 = v_rip - 12618972;
        Arg1 = v_rip + 1945973;
        result = McTemplateK0_EtwWriteTransfer(Arg1, a2, local_rsp - 56 - 40, a4);
    }
    a2 = 0;
    result = WheaSelLogCheckPoint(83, a2, local_rsp - 56 - 40, a4);
    a2 = 0;
    result = IopInitCrashDumpDuringSysInit(Arg1, a2, local_rsp - 56 - 40, a4);
    if (((*(uint8_t *)(v_rip + 0x361C07)) & (16)) != 0) {
        a4 = (uint32_t)(result);
        a2 = v_rip - 12618811;
        Arg1 = v_rip + 1945918;
        result = McTemplateK0q_EtwWriteTransfer(Arg1, a2, local_rsp - 56 - 40, a4);
    }
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = 80;
        a2 = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = WheaSelLogCheckPoint(Arg1, a2, local_rsp - 56 - 40, a4);
    }
    if (sign_flag) goto loc_00C2BD03;
    result = IopRemoveDumpCapsuleSupport(Arg1, a2, local_rsp - 56 - 40, a4);
    goto loc_00C2BD11;
loc_00C2BD03:
    if ((*(uint8_t *)(v_rip + 0x1DECB0)) == 0) {
        result = IopTraceCrashDumpDisabledOnBoot(Arg1, a2, local_rsp - 56 - 40, a4);
    }
    result = RtlIsStateSeparationEnabled(Arg1, a2, local_rsp - 56 - 40, a4);
    if ((uint8_t)(result) == 0) {
        result = PpLastGoodDoBootProcessing(Arg1, a2, local_rsp - 56 - 40, a4);
    }
    *(uint32_t *)(v_rip + 0x39858F) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x39859B)))));
    result = PsLocateSystemDlls(Arg1, a2, local_rsp - 56 - 40, a4);
    *(uint32_t *)(v_rip + 0x398584) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x39859B)));
    if (!sign_flag) goto loc_00C2BD5F;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(a2 + 10, a2, local_rsp - 56 - 40, a4);
    *(uint32_t *)(v_rip + 0x361B76) = 7;
    goto loc_00C2BEE5;
loc_00C2BD5F:
    result = MmInitializeImageViewExtension((uint32_t)((uint32_t)(local_r12 + 1)), a2, local_rsp - 56 - 40, a4);
    Arg1 = 0;
    result = PfSnBeginBootPhase(Arg1, a2, local_rsp - 56 - 40, a4);
    result = IopReassignSystemRoot(0, local_rsp - 56 - 80, local_rsp - 56 - 40, a4);
    if ((uint8_t)(result) != 0) goto loc_00C2BD97;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(a2 + 12, a2, local_rsp - 56 - 40, a4);
    *(uint32_t *)(v_rip + 0x361B3E) = 9;
    goto loc_00C2B076;
loc_00C2BD97:
    result = IopProtectSystemPartition(0, a2, local_rsp - 56 - 40, a4);
    if ((uint8_t)(result) != 0) goto loc_00C2BDBC;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(a2 + 13, a2, local_rsp - 56 - 40, a4);
    *(uint32_t *)(v_rip + 0x361B19) = 10;
    goto loc_00C2B076;
loc_00C2BDBC:
    result = (*(uint64_t *)(v_rip + 0x2C96FD)) + (72);
    v_stack_m110 = 0;
    *(uint64_t *)(local_rsp - 0x38 - 0x80) = result;
    v_stack_mC8 = 48;
    v_stack_mC0 = 0;
    *(uint32_t *)(local_rsp - 0x38 - 0x78) = 576;
    *(uint64_t *)(local_rsp - 0x38 - 0x70) = v_xmm0;
    v_stack_m118 = (uint32_t)(local_r12 + 1);
    result = ZwOpenFile(v_stack_mF0, (uint32_t)(0x80000000ULL), v_stack_mC8, local_rsp - 56 - 56);
    if (sign_flag) goto loc_00C2BE5D;
    v_stack_m110 = 0;
    a4 = 0;
    a3 = 0;
    v_stack_m118 = v_stack_mE0;
    v_stack_mE0 = 0;
    result = ObReferenceObjectByHandle(v_stack_mF0, 128, a3, a4);
    if (!(sign_flag)) {
        Arg1 = v_stack_mE0;
        result = PpPagePathAssign(Arg1, 128, a3, a4);
        Arg1 = v_stack_mE0;
        a2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(Arg1, a2, a3, a4);
    }
    result = ZwClose(v_stack_mF0, a2, a3, a4);
loc_00C2BE5D:
    a2 = 0;
    result = WMIInitialize((uint32_t)((uint32_t)(local_r12 + 1)), a2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_00C2BE7A;
    *(uint32_t *)(v_rip + 0x361A5B) = 25;
    goto loc_00C2B076;
loc_00C2BE7A:
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = 8;
        a2 = (uint32_t)(Arg1);
        result = WheaSelLogCheckPoint(Arg1, a2, a3, a4);
    }
    if (((*(uint8_t *)(v_rip + 0x361A42)) & (16)) != 0) {
        a4 = (uint32_t)(local_r12 + 1);
        a2 = v_rip - 12620774;
        Arg1 = v_rip + 1945467;
        result = McTemplateK0q_EtwWriteTransfer(Arg1, a2, a3, a4);
    }
    result = WheaInitialize(Arg1, (uint32_t)((uint32_t)(local_r12 + 1)), a3, a4);
    if (((*(uint8_t *)(v_rip + 0x361A18)) & (16)) != 0) {
        a2 = v_rip - 12627629;
        Arg1 = v_rip + 1945428;
        result = McTemplateK0_EtwWriteTransfer(Arg1, a2, a3, a4);
    }
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = 8;
        a2 = Arg1 + 1;
        result = WheaSelLogCheckPoint(Arg1, a2, a3, a4);
    }
    result = 0;
loc_00C2BEE5:
    Arg1 = (*(uint64_t *)(local_rsp - 0x38)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, a2, a3, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xF0` | `64` | `R` |
| `Arg1` | `+ 0x108` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C2AC3C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
