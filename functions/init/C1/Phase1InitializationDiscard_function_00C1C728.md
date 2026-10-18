# Phase1InitializationDiscard

- RVA: `0x00C1C728`–`0x00C1DB45` (길이 `5,149` bytes)
- VA: `0x0000000140C1C728`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3738`
- 디코드: `1,226`개 명령, `5,149/5,149` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **182**; 고유 호출 대상: **97**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **136**

### Outgoing calls
- `0x00C1C7A9` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C1C7AE` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00C1C7C9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C1C7D9` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1C7FE` → [KeSetPriorityThread](../../text/2C/KeSetPriorityThread_function_002C76E0.md) (function, `0x002C76E0`)
- `0x00C1C813` → [strupr](../../text/4F/strupr_function_004FEEE0.md) (function, `0x004FEEE0`)
- `0x00C1C82E` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1C842` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1C850` → [atol](../../text/4F/atol_function_004FF8D0.md) (function, `0x004FF8D0`)
- `0x00C1C865` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1C87C` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1C898` → [atol](../../text/4F/atol_function_004FF8D0.md) (function, `0x004FF8D0`)
- `0x00C1C8E3` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1C8FA` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1C936` → [strtoul](../../text/4F/strtoul_function_004FF3B8.md) (function, `0x004FF3B8`)
- `0x00C1C95F` → [strtoul](../../text/4F/strtoul_function_004FF3B8.md) (function, `0x004FF3B8`)
- `0x00C1C9B5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C1C9EE` → [strtoui64](../../text/4F/strtoui64_function_004FF650.md) (function, `0x004FF650`)
- `0x00C1CA40` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1CA6B` → [KiPerformGroupConfiguration](../C3/KiPerformGroupConfiguration_function_00C38FB0.md) (function, `0x00C38FB0`)
- `0x00C1CA7B` → [KiCommitGroupSubNodeAssignments](../../text/5B/KiCommitGroupSubNodeAssignments_function_005BC674.md) (function, `0x005BC674`)
- `0x00C1CA8D` → [HalInitSystem](../../pagelk/B5/HalInitSystem_function_00B5B6E0.md) (function, `0x00B5B6E0`)
- `0x00C1CAA3` → [KeInitializeClock](../C7/KeInitializeClock_function_00C70C30.md) (function, `0x00C70C30`)
- `0x00C1CABC` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1CAE2` → [BgDisplayProgressIndicator](../../pagebgfx/BC/BgDisplayProgressIndicator_function_00BC0628.md) (function, `0x00BC0628`)
- `0x00C1CB07` → [BgDisplayBackgroundUpdate](../../pagebgfx/BC/BgDisplayBackgroundUpdate_function_00BC05EC.md) (function, `0x00BC05EC`)
- `0x00C1CB31` → [InbvDriverInitialize](../C2/InbvDriverInitialize_function_00C2A420.md) (function, `0x00C2A420`)
- `0x00C1CB38` → [DisplayBootBitmap](../../text/53/DisplayBootBitmap_function_0053B87C.md) (function, `0x0053B87C`)
- `0x00C1CB4C` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1CB67` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1CB9E` → [RtlFindMessage](../../page/99/RtlFindMessage_function_0099B220.md) (function, `0x0099B220`)
- `0x00C1CBEC` → [RtlStringCbPrintfExA](../../text/53/RtlStringCbPrintfExA_function_0053BC58.md) (function, `0x0053BC58`)
- `0x00C1CC0A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1CC49` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (function, `0x0053BC0C`)
- `0x00C1CC69` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1CC99` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (function, `0x0053BC0C`)
- `0x00C1CCB9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1CCC9` → [RtlStringCbCopyA](../../text/46/RtlStringCbCopyA_function_0046143C.md) (function, `0x0046143C`)
- `0x00C1CCE7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1CCF0` → [InbvDisplayString](../../text/59/InbvDisplayString_function_00590280.md) (function, `0x00590280`)
- `0x00C1CD5E` → [PoInitSystem](../C7/PoInitSystem_function_00C72358.md) (function, `0x00C72358`)
- `0x00C1CDC0` → [ExpWriteTimeZoneBias](../../page/A6/ExpWriteTimeZoneBias_function_00A6C028.md) (function, `0x00A6C028`)
- `0x00C1CDD1` → [GetBootSystemTime](GetBootSystemTime_function_00C1AFCC.md) (function, `0x00C1AFCC`)
- `0x00C1CDE5` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1CDF9` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1CE07` → [atol](../../text/4F/atol_function_004FF8D0.md) (function, `0x004FF8D0`)
- `0x00C1CE17` → [RtlpTimeToTimeFields](../../text/42/RtlpTimeToTimeFields_function_0042E110.md) (function, `0x0042E110`)
- `0x00C1CE29` → [RtlpTimeFieldsToTime](../../text/42/RtlpTimeFieldsToTime_function_0042E6C8.md) (function, `0x0042E6C8`)
- `0x00C1CE38` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00C1CE6B` → [KeSetSystemTime](../../text/2C/KeSetSystemTime_function_002C8E5C.md) (function, `0x002C8E5C`)
- `0x00C1CE70` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00C1CEA1` → [PoNotifySystemTimeSet](../../text/4D/PoNotifySystemTimeSet_function_004D4F7C.md) (function, `0x004D4F7C`)
- `0x00C1CEB1` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C1CED6` → [ZwQueryLicenseValue](../../text/6A/ZwQueryLicenseValue_function_006AFCF0.md) (function, `0x006AFCF0`)
- `0x00C1CF0A` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1CF1E` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1CF2C` → [atol](../../text/4F/atol_function_004FF8D0.md) (function, `0x004FF8D0`)
- `0x00C1CF41` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1CF55` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1CF63` → [atol](../../text/4F/atol_function_004FF8D0.md) (function, `0x004FF8D0`)
- `0x00C1CF78` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1CF8C` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1CF9A` → [atol](../../text/4F/atol_function_004FF8D0.md) (function, `0x004FF8D0`)
- `0x00C1CFB7` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1CFCB` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1CFD9` → [atol](../../text/4F/atol_function_004FF8D0.md) (function, `0x004FF8D0`)
- `0x00C1CFEE` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1D002` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1D010` → [atol](../../text/4F/atol_function_004FF8D0.md) (function, `0x004FF8D0`)
- `0x00C1D025` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1D03B` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C1D047` → [KeStartAllProcessors](../C3/KeStartAllProcessors_function_00C36F78.md) (function, `0x00C36F78`)
- `0x00C1D04E` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C1D05A` → [EtwTimeProfileReset](../../page/7B/EtwTimeProfileReset_function_007B7E8C.md) (function, `0x007B7E8C`)
- `0x00C1D078` → [KeSetAffinityProcess](../../text/3C/KeSetAffinityProcess_function_003C0A60.md) (function, `0x003C0A60`)
- `0x00C1D07D` → [MakeGdtReadOnly](../../text/53/MakeGdtReadOnly_function_0053BA98.md) (function, `0x0053BA98`)
- `0x00C1D0A0` → [RtlFindMessage](../../page/99/RtlFindMessage_function_0099B220.md) (function, `0x0099B220`)
- `0x00C1D0BB` → [HalAllProcessorsStarted](HalAllProcessorsStarted_function_00C1DD90.md) (function, `0x00C1DD90`)
- `0x00C1D0CF` → [RtlInitAnsiString](../../text/47/RtlInitAnsiString_function_00470F40.md) (function, `0x00470F40`)
- `0x00C1D118` → [RtlFindMessage](../../page/99/RtlFindMessage_function_0099B220.md) (function, `0x0099B220`)
- `0x00C1D181` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (function, `0x0053BC0C`)
- `0x00C1D19F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1D1A8` → [InbvDisplayString](../../text/59/InbvDisplayString_function_00590280.md) (function, `0x00590280`)
- `0x00C1D1B2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C1D1BE` → [ObInitSystem](../C7/ObInitSystem_function_00C71C7C.md) (function, `0x00C71C7C`)
- `0x00C1D1CD` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1D1D6` → [ExInitSystem](../C5/ExInitSystem_function_00C511A8.md) (function, `0x00C511A8`)
- `0x00C1D1F5` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1D1FE` → [HalReportResourceUsage](HalReportResourceUsage_function_00C1DDC0.md) (function, `0x00C1DDC0`)
- `0x00C1D203` → [IoCreateObjectTypes](../C2/IoCreateObjectTypes_function_00C2A854.md) (function, `0x00C2A854`)
- `0x00C1D225` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1D22D` → [KeInitSystem](../C7/KeInitSystem_function_00C71660.md) (function, `0x00C71660`)
- `0x00C1D24C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1D25A` → [KdInitSystem](../../pagekd/B8/KdInitSystem_function_00B85E30.md) (function, `0x00B85E30`)
- `0x00C1D27C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1D29E` → `ext-ms-win-ntos-tm-l1-1-0.dll!TmInitSystem` (import, 간접 대상; import `ext-ms-win-ntos-tm-l1-1-0.dll!TmInitSystem`)
- `0x00C1D2CD` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1D2D3` → [DbgkInitialize](../C2/DbgkInitialize_function_00C261E4.md) (function, `0x00C261E4`)
- `0x00C1D2EE` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1D2F6` → [UcInitialize](../../text/69/UcInitialize_function_0069AD9C.md) (function, `0x0069AD9C`)
- `0x00C1D2FB` → [BcdInitializeBcdSyncMutant](../C6/BcdInitializeBcdSyncMutant_function_00C6D18C.md) (function, `0x00C6D18C`)
- `0x00C1D302` → [VerifierInitSystem](../C4/VerifierInitSystem_function_00C4BC84.md) (function, `0x00C4BC84`)
- `0x00C1D307` → [SeInitSystem](../C4/SeInitSystem_function_00C4A74C.md) (function, `0x00C4A74C`)
- `0x00C1D315` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1D325` → [AlpcpInitSystem](../../page/74/AlpcpInitSystem_function_0074CB9C.md) (function, `0x0074CB9C`)
- `0x00C1D333` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1D34C` → [PsInitSystem](../BE/PsInitSystem_function_00BEED58.md) (function, `0x00BEED58`)
- `0x00C1D351` → [ExInitLicenseCallback](../../page/7C/ExInitLicenseCallback_function_007C7B14.md) (function, `0x007C7B14`)
- `0x00C1D359` → [CreateSystemRootLink](CreateSystemRootLink_function_00C1AA18.md) (function, `0x00C1AA18`)
- `0x00C1D374` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1D37C` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C1D38D` → [MmInitSystem](../BE/MmInitSystem_function_00BEE990.md) (function, `0x00BEE990`)
- `0x00C1D394` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C1D3A2` → [CcInitializeCacheManager](../BE/CcInitializeCacheManager_function_00BEE2E8.md) (function, `0x00BEE2E8`)
- `0x00C1D3B0` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1D3B9` → [CmInitSystem1](../C5/CmInitSystem1_function_00C559CC.md) (function, `0x00C559CC`)
- `0x00C1D3C7` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1D3CD` → [PsInitializeBootCpuPartitions](../C4/PsInitializeBootCpuPartitions_function_00C44D94.md) (function, `0x00C44D94`)
- `0x00C1D3D2` → [ExInitializeLeapSecondData](../../page/7C/ExInitializeLeapSecondData_function_007C562C.md) (function, `0x007C562C`)
- `0x00C1D3EE` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1D3FE` → [ExIsMultiSessionSku](../../page/7C/ExIsMultiSessionSku_function_007C7538.md) (function, `0x007C7538`)
- `0x00C1D44F` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C1D469` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C1D505` → [BgGetDisplayContext](../../pagebgfx/BC/BgGetDisplayContext_function_00BC06F4.md) (function, `0x00BC06F4`)
- `0x00C1D514` → `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrInitSystem` (import, 간접 대상; import `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrInitSystem`)
- `0x00C1D525` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C1D55A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1D588` → [EmInitSystem](../C7/EmInitSystem_function_00C71150.md) (function, `0x00C71150`)
- `0x00C1D5A4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1D5AD` → [MfgInitSystem](MfgInitSystem_function_00C1C390.md) (function, `0x00C1C390`)
- `0x00C1D5C9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1D5CF` → [PfInitializeSuperfetch](../C3/PfInitializeSuperfetch_function_00C3CACC.md) (function, `0x00C3CACC`)
- `0x00C1D5D6` → [SmInitSystem](../C7/SmInitSystem_function_00C7673C.md) (function, `0x00C7673C`)
- `0x00C1D5F2` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1D5FD` → [VmInitSystem](../BE/VmInitSystem_function_00BEEEB8.md) (function, `0x00BEEEB8`)
- `0x00C1D619` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1D639` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1D661` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00C1D690` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00C1D6A1` → [FsRtlSendModernAppTermination](../../text/49/FsRtlSendModernAppTermination_function_0049F340.md) (function, `0x0049F340`)
- `0x00C1D6A6` → [ExInitializeTimeRefresh](../C5/ExInitializeTimeRefresh_function_00C51090.md) (function, `0x00C51090`)
- `0x00C1D6AB` → [ExAcquireTimeRefreshLockExclusive](../../page/9C/ExAcquireTimeRefreshLockExclusive_function_009C5810.md) (function, `0x009C5810`)
- `0x00C1D6B5` → [ExInitializeUtcTimeZoneBias](../../page/7C/ExInitializeUtcTimeZoneBias_function_007C5818.md) (function, `0x007C5818`)
- `0x00C1D6C4` → [ExpRefreshTimeZoneInformation](../../page/A6/ExpRefreshTimeZoneInformation_function_00A6B46C.md) (function, `0x00A6B46C`)
- `0x00C1D6C9` → [ExReleaseTimeRefreshLockExclusive](../../page/9C/ExReleaseTimeRefreshLockExclusive_function_009C5874.md) (function, `0x009C5874`)
- `0x00C1D6D5` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00C1D704` → [KeSetSystemTime](../../text/2C/KeSetSystemTime_function_002C8E5C.md) (function, `0x002C8E5C`)
- `0x00C1D719` → [ZwSetSystemTime](../../text/6B/ZwSetSystemTime_function_006B08B0.md) (function, `0x006B08B0`)
- `0x00C1D71E` → [FsRtlInitSystem](../C2/FsRtlInitSystem_function_00C28EEC.md) (function, `0x00C28EEC`)
- `0x00C1D72C` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1D760` → [ExInitializeNPagedLookasideListInternal](../../text/46/ExInitializeNPagedLookasideListInternal_function_00468720.md) (function, `0x00468720`)
- `0x00C1D7CB` → [ExInitializePagedLookasideList](../../page/AA/ExInitializePagedLookasideList_function_00AACC30.md) (function, `0x00AACC30`)
- `0x00C1D7D3` → [HvlDebuggerSupportInitialize](../../text/58/HvlDebuggerSupportInitialize_function_00583790.md) (function, `0x00583790`)
- `0x00C1D7DA` → [HalReportResourceUsage](HalReportResourceUsage_function_00C1DDC0.md) (function, `0x00C1DDC0`)
- `0x00C1D7EC` → `kdcom.dll!KdInitialize` (import, 간접 대상; import `kdcom.dll!KdInitialize`)
- `0x00C1D7F8` → [PpInitSystem](../C3/PpInitSystem_function_00C32964.md) (function, `0x00C32964`)
- `0x00C1D806` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1D81F` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1D843` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (function, `0x006C6720`)
- `0x00C1D862` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (function, `0x006C6720`)
- `0x00C1D887` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (function, `0x006C6720`)
- `0x00C1D8BD` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (function, `0x006C6720`)
- `0x00C1D925` → [RtlFindMessage](../../page/99/RtlFindMessage_function_0099B220.md) (function, `0x0099B220`)
- `0x00C1D937` → [InbvDisplayString](../../text/59/InbvDisplayString_function_00590280.md) (function, `0x00590280`)
- `0x00C1D972` → [RtlFindMessage](../../page/99/RtlFindMessage_function_0099B220.md) (function, `0x0099B220`)
- `0x00C1D984` → [InbvDisplayString](../../text/59/InbvDisplayString_function_00590280.md) (function, `0x00590280`)
- `0x00C1D98F` → [IopInitializeBootLogging](../../page/71/IopInitializeBootLogging_function_0071B748.md) (function, `0x0071B748`)
- `0x00C1D994` → [ExpWatchProductTypeInitialization](../C5/ExpWatchProductTypeInitialization_function_00C52170.md) (function, `0x00C52170`)
- `0x00C1D9A9` → [BootApplicationPersistentDataProcess](../BE/BootApplicationPersistentDataProcess_function_00BEEBD4.md) (function, `0x00BEEBD4`)
- `0x00C1D9B1` → `ext-ms-win-ntos-ucode-l1-1-0.dll!ExpMicrocodeInitialization` (import, 간접 대상; import `ext-ms-win-ntos-ucode-l1-1-0.dll!ExpMicrocodeInitialization`)
- `0x00C1D9E2` → [ExpGetOriginalImageVersionRegistryValue](../../page/7D/ExpGetOriginalImageVersionRegistryValue_function_007D58B8.md) (function, `0x007D58B8`)
- `0x00C1D9F5` → [ExpComputeCyclesPerYield](ExpComputeCyclesPerYield_function_00C1AF20.md) (function, `0x00C1AF20`)
- `0x00C1DA11` → [CreateMiniNtBootKey](CreateMiniNtBootKey_function_00C1A840.md) (function, `0x00C1A840`)
- `0x00C1DA16` → `symcryptk.dll!SymCryptEntropyAccumulatorGlobalInitFromRegistry` (import, 간접 대상; import `symcryptk.dll!SymCryptEntropyAccumulatorGlobalInitFromRegistry`)
- `0x00C1DA25` → [SeCodeIntegrityInitializePolicy](../C4/SeCodeIntegrityInitializePolicy_function_00C4A5CC.md) (function, `0x00C4A5CC`)
- `0x00C1DA43` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1DAD6` → [PoInitSystem](../C7/PoInitSystem_function_00C72358.md) (function, `0x00C72358`)
- `0x00C1DADF` → [RtlInitFunctionalityCache](../../page/78/RtlInitFunctionalityCache_function_0078A5F8.md) (function, `0x0078A5F8`)
- `0x00C1DAF8` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00C1DB08` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00C1DB34` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1DB3F` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)

### Direct callers
- [Phase1Initialization](../../page/70/Phase1Initialization_function_007062C0.md) at `0x007062DE`

### Static image references
- `0x00C1C74C` → RVA `0x00E0A740` (`.data`; read)
- `0x00C1C7F3` → RVA `0x00FC41A0` (`.data`; write)
- `0x00C1C824` → RVA `0x00C78F80` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1C838` → RVA `0x00C78BD0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1C855` → RVA `0x00FC6BC0` (`ALMOSTRO`; write)
- `0x00C1C85B` → RVA `0x00C78FA0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1C889` → RVA `0x00FC6B90` (`ALMOSTRO`; read)
- `0x00C1C8A3` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00C1C8B8` → RVA `0x00FC6B90` (`ALMOSTRO`; write)
- `0x00C1C8D9` → RVA `0x00C78FC0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1C902` → RVA `0x00FC6AA7` (`ALMOSTRO`; write)
- `0x00C1CA51` → RVA `0x00F21AF0` (`.data`; read)
- `0x00C1CA5B` → RVA `0x00E668F8` (`.data`; write)
- `0x00C1CA80` → RVA `0x00FC41A0` (`.data`; read)
- `0x00C1CAB2` → RVA `0x00C78FE0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1CAC6` → RVA `0x00E65EB0` (`.data`; read)
- `0x00C1CACD` → RVA `0x00E65E4C` (`.data`; write)
- `0x00C1CAD6` → RVA `0x00E65EBA` (`.data`; read)
- `0x00C1CAEB` → RVA `0x00E65EB8` (`.data`; write)
- `0x00C1CB10` → RVA `0x00E65E81` (`.data`; write)
- `0x00C1CB17` → RVA `0x0053BA40` (`DisplayFilter`; read)
- `0x00C1CB27` → RVA `0x00E65E50` (`.data`; write)
- `0x00C1CB42` → RVA `0x00C78FF0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1CB56` → RVA `0x00C79000` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1CB5D` → RVA `0x00FC4148` (`.data`; write)
- `0x00C1CB71` → RVA `0x00E0F3D8` (`.data`; read/write)
- `0x00C1CBA3` → RVA `0x00FC41B0` (`.data`; read)
- `0x00C1CBD4` → RVA `0x00C79010` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1CC28` → RVA `0x00C78C30` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1CC77` → RVA `0x00E0A74C` (`.data`; read)
- `0x00C1CCBF` → RVA `0x00C79020` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1CD6D` → RVA `0x00E68570` (`.data`; read)
- `0x00C1CD82` → RVA `0x00FD9E08` (`PAGEDATA`; read)
- `0x00C1CDB3` → RVA `0x00FC5008` (`ALMOSTRO`; read)
- `0x00C1CDDB` → RVA `0x00C79040` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1CE88` → RVA `0x00E0EB98` (`.data`; read)
- `0x00C1CEA6` → RVA `0x00C79050` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1CEC1` → RVA `0x00FC6C68` (`ALMOSTRO`; read)
- `0x00C1CEED` → RVA `0x00FC6C68` (`ALMOSTRO`; write)
- `0x00C1CF00` → RVA `0x00C79090` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1CF31` → RVA `0x00FC6CF4` (`ALMOSTRO`; write)
- `0x00C1CF37` → RVA `0x00C790A0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1CF68` → RVA `0x00FC6C94` (`ALMOSTRO`; write)
- `0x00C1CF6E` → RVA `0x00C790B0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1CF9F` → RVA `0x00FC6D54` (`ALMOSTRO`; write)
- `0x00C1CFA5` → RVA `0x00FC6AA7` (`ALMOSTRO`; read)
- `0x00C1CFAD` → RVA `0x00C790D0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1CFDE` → RVA `0x00FC6C90` (`ALMOSTRO`; write)
- `0x00C1CFE4` → RVA `0x00C790F0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1D015` → RVA `0x00FC6C8C` (`ALMOSTRO`; write)
- `0x00C1D01B` → RVA `0x00C79110` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1D02F` → RVA `0x00FC6E5C` (`ALMOSTRO`; write)
- `0x00C1D040` → RVA `0x010087C8` (`INITDATA`; write)
- `0x00C1D053` → RVA `0x010087D0` (`INITDATA`; write)
- `0x00C1D068` → RVA `0x00FC7120` (`ALMOSTRO`; read)
- `0x00C1D0B4` → RVA `0x00C79120` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1D0EA` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x00C1D11D` → RVA `0x00FC6B88` (`ALMOSTRO`; read)
- `0x00C1D152` → RVA `0x00C79140` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1D282` → RVA `0x00FC6EF0` (`ALMOSTRO`; read)
- `0x00C1D289` → RVA `0x00FC7330` (`ALMOSTRO`; read)
- `0x00C1D290` → RVA `0x00FC73A8` (`ALMOSTRO`; read)
- `0x00C1D297` → RVA `0x00FC7338` (`ALMOSTRO`; read)
- `0x00C1D29E` → RVA `0x00151470` (`ext-ms-win-ntos-tm-l1-1-0.dll!TmInitSystem (IAT)`; read)
- `0x00C1D31B` → RVA `0x00FC6E50` (`ALMOSTRO`; write)
- `0x00C1D339` → RVA `0x00FC6C18` (`ALMOSTRO`; read)
- `0x00C1D345` → RVA `0x00FC6F70` (`ALMOSTRO`; write)
- `0x00C1D384` → RVA `0x010087E8` (`INITDATA`; write)
- `0x00C1D39B` → RVA `0x010087F0` (`INITDATA`; write)
- `0x00C1D41D` → RVA `0x00FC4190` (`.data`; read)
- `0x00C1D435` → RVA `0x00EEFB6C` (`.data`; read)
- `0x00C1D459` → RVA `0x010087B8` (`INITDATA`; write)
- `0x00C1D46E` → RVA `0x00FC6A84` (`ALMOSTRO`; read)
- `0x00C1D475` → RVA `0x007F9020` (`MmMapLockedRestartPages`; read)
- `0x00C1D480` → RVA `0x007F90E0` (`MmUnmapLockedRestartPages`; read)
- `0x00C1D48B` → RVA `0x00368C90` (`KeRemoveEnclavePage`; read)
- `0x00C1D496` → RVA `0x00B86680` (`KdPullRemoteFileEx`; read)
- `0x00C1D4A1` → RVA `0x00BC9010` (`CmSaveKeyToBuffer`; read)
- `0x00C1D4AC` → RVA `0x00418E70` (`KeIsBugCheckActive`; read)
- `0x00C1D4B7` → RVA `0x007DF3C0` (`CmOpenKeyForBugCheckRecovery`; read)
- `0x00C1D4C2` → RVA `0x00338CD0` (`MiPageToNode`; read)
- `0x00C1D4CD` → RVA `0x00436620` (`MmGetNextNode`; read)
- `0x00C1D4E2` → RVA `0x0058FB90` (`VslpKsrEnterIumSecureMode`; read)
- `0x00C1D4E9` → RVA `0x01008730` (`INITDATA`; write)
- `0x00C1D4F0` → RVA `0x01008730` (`INITDATA`; read)
- `0x00C1D4F7` → RVA `0x00C2A410` (`VslpRegisterKsrCallback`; read)
- `0x00C1D4FE` → RVA `0x01008738` (`INITDATA`; write)
- `0x00C1D514` → RVA `0x001512E0` (`ext-ms-win-ntos-ksr-l1-1-5.dll!KsrInitSystem (IAT)`; read)
- `0x00C1D52A` → RVA `0x010087C0` (`INITDATA`; write)
- `0x00C1D56D` → RVA `0x00EFEFE0` (`.data`; read)
- `0x00C1D579` → RVA `0x00EFF000` (`.data`; write)
- `0x00C1D581` → RVA `0x00EFEFF0` (`.data`; read)
- `0x00C1D62F` → RVA `0x00C79170` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1D648` → RVA `0x000208B8` (`.rdata`; read)
- `0x00C1D666` → RVA `0x00FC6A90` (`ALMOSTRO`; read)
- `0x00C1D677` → RVA `0x00020AA8` (`.rdata`; read)
- `0x00C1D737` → RVA `0x00E28280` (`.data`; read)
- `0x00C1D797` → RVA `0x00E67B44` (`.data`; write)
- `0x00C1D7BC` → RVA `0x00E28200` (`.data`; read)
- `0x00C1D7C3` → RVA `0x00E67B40` (`.data`; write)
- `0x00C1D7DF` → RVA `0x00F475E0` (`.data`; read)
- `0x00C1D7EC` → RVA `0x001516B8` (`kdcom.dll!KdInitialize (IAT)`; read)
- `0x00C1D815` → RVA `0x00C79180` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1D839` → RVA `0x00C79190` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1D84C` → RVA `0x00FC41C4` (`.data`; write)
- `0x00C1D858` → RVA `0x00C791A0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1D87D` → RVA `0x00C791B0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1D8B3` → RVA `0x00C791C0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1D8D3` → RVA `0x00FC41C4` (`.data`; read)
- `0x00C1D9B1` → RVA `0x00151610` (`ext-ms-win-ntos-ucode-l1-1-0.dll!ExpMicrocodeInitialization (IAT)`; read)
- `0x00C1D9BD` → RVA `0x00FC6AE8` (`ALMOSTRO`; read)
- `0x00C1D9C3` → RVA `0x00FD9B18` (`PAGEDATA`; read)
- `0x00C1D9CB` → RVA `0x00FD9B18` (`PAGEDATA`; write)
- `0x00C1D9DB` → RVA `0x00EFA108` (`.data`; write)
- `0x00C1D9FA` → RVA `0x00FC4148` (`.data`; read)
- `0x00C1DA16` → RVA `0x00151718` (`symcryptk.dll!SymCryptEntropyAccumulatorGlobalInitFromRegistry (IAT)`; read)
- `0x00C1DA49` → RVA `0x00EFAC80` (`.data`; read)
- `0x00C1DA50` → RVA `0x00E0AA58` (`.data`; write)
- `0x00C1DA57` → RVA `0x00EFAC88` (`.data`; write)
- `0x00C1DA61` → RVA `0x00EFAC80` (`.data`; write)
- `0x00C1DA6B` → RVA `0x00EFAC48` (`.data`; read)
- `0x00C1DA72` → RVA `0x00EFAC98` (`.data`; write)
- `0x00C1DA79` → RVA `0x00EFAC50` (`.data`; write)
- `0x00C1DA80` → RVA `0x00EFAC48` (`.data`; write)
- `0x00C1DA87` → RVA `0x00EFAC68` (`.data`; read)
- `0x00C1DA8E` → RVA `0x00EFAC70` (`.data`; write)
- `0x00C1DA95` → RVA `0x00EFAC68` (`.data`; write)
- `0x00C1DA9C` → RVA `0x00EFACA0` (`.data`; write)
- `0x00C1DAA3` → RVA `0x00EFAC90` (`.data`; write)
- `0x00C1DAAA` → RVA `0x00EFAC40` (`.data`; write)
- `0x00C1DAB2` → RVA `0x00EFAC42` (`.data`; write)
- `0x00C1DAB9` → RVA `0x00EFAC44` (`.data`; write)
- `0x00C1DAC0` → RVA `0x00EFAC60` (`.data`; write)
- `0x00C1DAC8` → RVA `0x00EFAC62` (`.data`; write)
- `0x00C1DACF` → RVA `0x00EFAC64` (`.data`; write)
- `0x00C1DAEF` → RVA `0x00E2FFA8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **140**
  - `0x00C1C7A9` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C1C7AE` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`INIT` → `.text`)
  - `0x00C1C7C9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C1C7D9` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1C7FE` → [KeSetPriorityThread](../../text/2C/KeSetPriorityThread_function_002C76E0.md) (`INIT` → `.text`)
  - `0x00C1C813` → [strupr](../../text/4F/strupr_function_004FEEE0.md) (`INIT` → `.text`)
  - `0x00C1C82E` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1C842` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1C850` → [atol](../../text/4F/atol_function_004FF8D0.md) (`INIT` → `.text`)
  - `0x00C1C865` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1C87C` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1C898` → [atol](../../text/4F/atol_function_004FF8D0.md) (`INIT` → `.text`)
  - `0x00C1C8E3` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1C8FA` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1C936` → [strtoul](../../text/4F/strtoul_function_004FF3B8.md) (`INIT` → `.text`)
  - `0x00C1C95F` → [strtoul](../../text/4F/strtoul_function_004FF3B8.md) (`INIT` → `.text`)
  - `0x00C1C9B5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C1C9EE` → [strtoui64](../../text/4F/strtoui64_function_004FF650.md) (`INIT` → `.text`)
  - `0x00C1CA40` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1CA7B` → [KiCommitGroupSubNodeAssignments](../../text/5B/KiCommitGroupSubNodeAssignments_function_005BC674.md) (`INIT` → `.text`)
  - `0x00C1CA8D` → [HalInitSystem](../../pagelk/B5/HalInitSystem_function_00B5B6E0.md) (`INIT` → `PAGELK`)
  - `0x00C1CABC` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1CAE2` → [BgDisplayProgressIndicator](../../pagebgfx/BC/BgDisplayProgressIndicator_function_00BC0628.md) (`INIT` → `PAGEBGFX`)
  - `0x00C1CB07` → [BgDisplayBackgroundUpdate](../../pagebgfx/BC/BgDisplayBackgroundUpdate_function_00BC05EC.md) (`INIT` → `PAGEBGFX`)
  - `0x00C1CB38` → [DisplayBootBitmap](../../text/53/DisplayBootBitmap_function_0053B87C.md) (`INIT` → `.text`)
  - `0x00C1CB4C` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1CB67` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1CB9E` → [RtlFindMessage](../../page/99/RtlFindMessage_function_0099B220.md) (`INIT` → `PAGE`)
  - `0x00C1CBEC` → [RtlStringCbPrintfExA](../../text/53/RtlStringCbPrintfExA_function_0053BC58.md) (`INIT` → `.text`)
  - `0x00C1CC0A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1CC49` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (`INIT` → `.text`)
  - `0x00C1CC69` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1CC99` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (`INIT` → `.text`)
  - `0x00C1CCB9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1CCC9` → [RtlStringCbCopyA](../../text/46/RtlStringCbCopyA_function_0046143C.md) (`INIT` → `.text`)
  - `0x00C1CCE7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1CCF0` → [InbvDisplayString](../../text/59/InbvDisplayString_function_00590280.md) (`INIT` → `.text`)
  - `0x00C1CDC0` → [ExpWriteTimeZoneBias](../../page/A6/ExpWriteTimeZoneBias_function_00A6C028.md) (`INIT` → `PAGE`)
  - `0x00C1CDE5` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1CDF9` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1CE07` → [atol](../../text/4F/atol_function_004FF8D0.md) (`INIT` → `.text`)
  - `0x00C1CE17` → [RtlpTimeToTimeFields](../../text/42/RtlpTimeToTimeFields_function_0042E110.md) (`INIT` → `.text`)
  - `0x00C1CE29` → [RtlpTimeFieldsToTime](../../text/42/RtlpTimeFieldsToTime_function_0042E6C8.md) (`INIT` → `.text`)
  - `0x00C1CE38` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`INIT` → `.text`)
  - `0x00C1CE6B` → [KeSetSystemTime](../../text/2C/KeSetSystemTime_function_002C8E5C.md) (`INIT` → `.text`)
  - `0x00C1CE70` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`INIT` → `.text`)
  - `0x00C1CEA1` → [PoNotifySystemTimeSet](../../text/4D/PoNotifySystemTimeSet_function_004D4F7C.md) (`INIT` → `.text`)
  - `0x00C1CEB1` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C1CED6` → [ZwQueryLicenseValue](../../text/6A/ZwQueryLicenseValue_function_006AFCF0.md) (`INIT` → `.text`)
  - `0x00C1CF0A` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1CF1E` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1CF2C` → [atol](../../text/4F/atol_function_004FF8D0.md) (`INIT` → `.text`)
  - `0x00C1CF41` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1CF55` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1CF63` → [atol](../../text/4F/atol_function_004FF8D0.md) (`INIT` → `.text`)
  - `0x00C1CF78` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1CF8C` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1CF9A` → [atol](../../text/4F/atol_function_004FF8D0.md) (`INIT` → `.text`)
  - `0x00C1CFB7` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1CFCB` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1CFD9` → [atol](../../text/4F/atol_function_004FF8D0.md) (`INIT` → `.text`)
  - `0x00C1CFEE` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1D002` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1D010` → [atol](../../text/4F/atol_function_004FF8D0.md) (`INIT` → `.text`)
  - `0x00C1D025` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1D03B` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C1D04E` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C1D05A` → [EtwTimeProfileReset](../../page/7B/EtwTimeProfileReset_function_007B7E8C.md) (`INIT` → `PAGE`)
  - `0x00C1D078` → [KeSetAffinityProcess](../../text/3C/KeSetAffinityProcess_function_003C0A60.md) (`INIT` → `.text`)
  - `0x00C1D07D` → [MakeGdtReadOnly](../../text/53/MakeGdtReadOnly_function_0053BA98.md) (`INIT` → `.text`)
  - `0x00C1D0A0` → [RtlFindMessage](../../page/99/RtlFindMessage_function_0099B220.md) (`INIT` → `PAGE`)
  - `0x00C1D0CF` → [RtlInitAnsiString](../../text/47/RtlInitAnsiString_function_00470F40.md) (`INIT` → `.text`)
  - `0x00C1D118` → [RtlFindMessage](../../page/99/RtlFindMessage_function_0099B220.md) (`INIT` → `PAGE`)
  - `0x00C1D181` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (`INIT` → `.text`)
  - `0x00C1D19F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1D1A8` → [InbvDisplayString](../../text/59/InbvDisplayString_function_00590280.md) (`INIT` → `.text`)
  - `0x00C1D1B2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C1D1CD` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1D1F5` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1D225` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1D24C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1D25A` → [KdInitSystem](../../pagekd/B8/KdInitSystem_function_00B85E30.md) (`INIT` → `PAGEKD`)
  - `0x00C1D27C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1D2CD` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1D2EE` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1D2F6` → [UcInitialize](../../text/69/UcInitialize_function_0069AD9C.md) (`INIT` → `.text`)
  - `0x00C1D315` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1D325` → [AlpcpInitSystem](../../page/74/AlpcpInitSystem_function_0074CB9C.md) (`INIT` → `PAGE`)
  - `0x00C1D333` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1D351` → [ExInitLicenseCallback](../../page/7C/ExInitLicenseCallback_function_007C7B14.md) (`INIT` → `PAGE`)
  - `0x00C1D374` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1D37C` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C1D394` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C1D3B0` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1D3C7` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1D3D2` → [ExInitializeLeapSecondData](../../page/7C/ExInitializeLeapSecondData_function_007C562C.md) (`INIT` → `PAGE`)
  - `0x00C1D3EE` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1D3FE` → [ExIsMultiSessionSku](../../page/7C/ExIsMultiSessionSku_function_007C7538.md) (`INIT` → `PAGE`)
  - `0x00C1D44F` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C1D469` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C1D505` → [BgGetDisplayContext](../../pagebgfx/BC/BgGetDisplayContext_function_00BC06F4.md) (`INIT` → `PAGEBGFX`)
  - `0x00C1D525` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C1D55A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1D5A4` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1D5C9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1D5F2` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1D619` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1D639` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1D661` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`INIT` → `.text`)
  - `0x00C1D690` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`INIT` → `.text`)
  - `0x00C1D6A1` → [FsRtlSendModernAppTermination](../../text/49/FsRtlSendModernAppTermination_function_0049F340.md) (`INIT` → `.text`)
  - `0x00C1D6AB` → [ExAcquireTimeRefreshLockExclusive](../../page/9C/ExAcquireTimeRefreshLockExclusive_function_009C5810.md) (`INIT` → `PAGE`)
  - `0x00C1D6B5` → [ExInitializeUtcTimeZoneBias](../../page/7C/ExInitializeUtcTimeZoneBias_function_007C5818.md) (`INIT` → `PAGE`)
  - `0x00C1D6C4` → [ExpRefreshTimeZoneInformation](../../page/A6/ExpRefreshTimeZoneInformation_function_00A6B46C.md) (`INIT` → `PAGE`)
  - `0x00C1D6C9` → [ExReleaseTimeRefreshLockExclusive](../../page/9C/ExReleaseTimeRefreshLockExclusive_function_009C5874.md) (`INIT` → `PAGE`)
  - `0x00C1D6D5` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`INIT` → `.text`)
  - `0x00C1D704` → [KeSetSystemTime](../../text/2C/KeSetSystemTime_function_002C8E5C.md) (`INIT` → `.text`)
  - `0x00C1D719` → [ZwSetSystemTime](../../text/6B/ZwSetSystemTime_function_006B08B0.md) (`INIT` → `.text`)
  - `0x00C1D72C` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1D760` → [ExInitializeNPagedLookasideListInternal](../../text/46/ExInitializeNPagedLookasideListInternal_function_00468720.md) (`INIT` → `.text`)
  - `0x00C1D7CB` → [ExInitializePagedLookasideList](../../page/AA/ExInitializePagedLookasideList_function_00AACC30.md) (`INIT` → `PAGE`)
  - `0x00C1D7D3` → [HvlDebuggerSupportInitialize](../../text/58/HvlDebuggerSupportInitialize_function_00583790.md) (`INIT` → `.text`)
  - `0x00C1D806` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1D81F` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1D843` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (`INIT` → `.text`)
  - `0x00C1D862` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (`INIT` → `.text`)
  - `0x00C1D887` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (`INIT` → `.text`)
  - `0x00C1D8BD` → [strncmp](../../text/6C/strncmp_function_006C6720.md) (`INIT` → `.text`)
  - `0x00C1D925` → [RtlFindMessage](../../page/99/RtlFindMessage_function_0099B220.md) (`INIT` → `PAGE`)
  - `0x00C1D937` → [InbvDisplayString](../../text/59/InbvDisplayString_function_00590280.md) (`INIT` → `.text`)
  - `0x00C1D972` → [RtlFindMessage](../../page/99/RtlFindMessage_function_0099B220.md) (`INIT` → `PAGE`)
  - `0x00C1D984` → [InbvDisplayString](../../text/59/InbvDisplayString_function_00590280.md) (`INIT` → `.text`)
  - `0x00C1D98F` → [IopInitializeBootLogging](../../page/71/IopInitializeBootLogging_function_0071B748.md) (`INIT` → `PAGE`)
  - `0x00C1D9E2` → [ExpGetOriginalImageVersionRegistryValue](../../page/7D/ExpGetOriginalImageVersionRegistryValue_function_007D58B8.md) (`INIT` → `PAGE`)
  - `0x00C1DA43` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1DADF` → [RtlInitFunctionalityCache](../../page/78/RtlInitFunctionalityCache_function_0078A5F8.md) (`INIT` → `PAGE`)
  - `0x00C1DAF8` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`INIT` → `.text`)
  - `0x00C1DB08` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
  - `0x00C1DB34` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1DB3F` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C1C728  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00C1C72D  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00C1C732  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00C1C737  55                              push rbp
00C1C738  41 54                           push r12
00C1C73A  41 55                           push r13
00C1C73C  41 56                           push r14
00C1C73E  41 57                           push r15
00C1C740  48 8D 6C 24 90                  lea rbp, [rsp - 0x70]
00C1C745  48 81 EC 70 01 00 00            sub rsp, 0x170
00C1C74C  48 8B 05 ED DF 1E 00            mov rax, qword ptr [rip + 0x1edfed]
00C1C753  48 33 C4                        xor rax, rsp
00C1C756  48 89 45 68                     mov qword ptr [rbp + 0x68], rax
00C1C75A  45 33 F6                        xor r14d, r14d
00C1C75D  0F 57 C0                        xorps xmm0, xmm0
00C1C760  48 8B F1                        mov rsi, rcx
00C1C763  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
00C1C768  33 C0                           xor eax, eax
00C1C76A  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
00C1C76F  33 D2                           xor edx, edx
00C1C771  4C 89 75 98                     mov qword ptr [rbp - 0x68], r14
00C1C775  45 8D 46 74                     lea r8d, [r14 + 0x74]
00C1C779  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
00C1C77E  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00C1C782  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
00C1C787  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
00C1C78B  44 88 74 24 58                  mov byte ptr [rsp + 0x58], r14b
00C1C790  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
00C1C794  44 89 75 80                     mov dword ptr [rbp - 0x80], r14d
00C1C798  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
00C1C79D  44 89 74 24 6C                  mov dword ptr [rsp + 0x6c], r14d
00C1C7A2  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00C1C7A6  89 45 D4                        mov dword ptr [rbp - 0x2c], eax
00C1C7A9  E8 92 A4 AA FF                  call 0x1406c6c40
00C1C7AE  E8 3D 1A 6E FF                  call 0x1402fe1f0
00C1C7B3  BA 00 02 00 00                  mov edx, 0x200
00C1C7B8  41 8D 4E 40                     lea ecx, [r14 + 0x40]
00C1C7BC  41 B8 49 6E 69 74               mov r8d, 0x74696e49
00C1C7C2  4C 8B A0 C8 04 00 00            mov r12, qword ptr [rax + 0x4c8]
00C1C7C9  E8 22 59 F6 FF                  call 0x140b820f0
00C1C7CE  4C 8B E8                        mov r13, rax
00C1C7D1  48 85 C0                        test rax, rax
00C1C7D4  75 09                           jne 0x140c1c7df
00C1C7D6  8D 48 31                        lea ecx, [rax + 0x31]
00C1C7D9  E8 62 0E 8E FF                  call 0x1404fd640
00C1C7DE  CC                              int3
00C1C7DF  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00C1C7E8  41 BF 01 00 00 00               mov r15d, 1
00C1C7EE  44 88 74 24 41                  mov byte ptr [rsp + 0x41], r14b
00C1C7F3  44 89 3D A6 79 3A 00            mov dword ptr [rip + 0x3a79a6], r15d
00C1C7FA  41 8D 57 1E                     lea edx, [r15 + 0x1e]
00C1C7FE  E8 DD AE 6A FF                  call 0x1402c76e0
00C1C803  48 8B 8E D8 00 00 00            mov rcx, qword ptr [rsi + 0xd8]
00C1C80A  48 85 C9                        test rcx, rcx
00C1C80D  0F 84 33 02 00 00               je 0x140c1ca46
00C1C813  E8 C8 26 8E FF                  call 0x1404feee0
00C1C818  48 8B F8                        mov rdi, rax
00C1C81B  48 85 C0                        test rax, rax
00C1C81E  0F 84 2D 02 00 00               je 0x140c1ca51
00C1C824  48 8D 15 55 C7 05 00            lea rdx, [rip + 0x5c755]
00C1C82B  48 8B C8                        mov rcx, rax
00C1C82E  E8 4D 2E 8E FF                  call 0x1404ff680
00C1C833  48 85 C0                        test rax, rax
00C1C836  74 23                           je 0x140c1c85b
00C1C838  48 8D 15 91 C3 05 00            lea rdx, [rip + 0x5c391]
00C1C83F  48 8B C8                        mov rcx, rax
00C1C842  E8 39 2E 8E FF                  call 0x1404ff680
00C1C847  48 85 C0                        test rax, rax
00C1C84A  74 0F                           je 0x140c1c85b
00C1C84C  48 8D 48 01                     lea rcx, [rax + 1]
00C1C850  E8 7B 30 8E FF                  call 0x1404ff8d0
00C1C855  89 05 65 A3 3A 00               mov dword ptr [rip + 0x3aa365], eax
00C1C85B  48 8D 15 3E C7 05 00            lea rdx, [rip + 0x5c73e]
00C1C862  48 8B CF                        mov rcx, rdi
00C1C865  E8 16 2E 8E FF                  call 0x1404ff680
00C1C86A  48 8B D8                        mov rbx, rax
00C1C86D  48 85 C0                        test rax, rax
00C1C870  74 12                           je 0x140c1c884
00C1C872  48 8D 15 57 C3 05 00            lea rdx, [rip + 0x5c357]
00C1C879  48 8B C8                        mov rcx, rax
00C1C87C  E8 FF 2D 8E FF                  call 0x1404ff680
00C1C881  48 8B D8                        mov rbx, rax
00C1C884  48 85 DB                        test rbx, rbx
00C1C887  74 50                           je 0x140c1c8d9
00C1C889  83 3D 00 A3 3A 00 40            cmp dword ptr [rip + 0x3aa300], 0x40
00C1C890  73 47                           jae 0x140c1c8d9
00C1C892  49 03 DF                        add rbx, r15
00C1C895  48 8B CB                        mov rcx, rbx
00C1C898  E8 33 30 8E FF                  call 0x1404ff8d0
00C1C89D  8B 15 ED A2 3A 00               mov edx, dword ptr [rip + 0x3aa2ed]
00C1C8A3  4C 8D 05 56 37 3E FF            lea r8, [rip - 0xc1c8aa]
00C1C8AA  66 41 89 84 50 90 76 FC 00      mov word ptr [r8 + rdx*2 + 0xfc7690], ax
00C1C8B3  41 03 D7                        add edx, r15d
00C1C8B6  8A 03                           mov al, byte ptr [rbx]
00C1C8B8  89 15 D2 A2 3A 00               mov dword ptr [rip + 0x3aa2d2], edx
00C1C8BE  3C 2C                           cmp al, 0x2c
00C1C8C0  74 13                           je 0x140c1c8d5
00C1C8C2  3C 20                           cmp al, 0x20
00C1C8C4  74 13                           je 0x140c1c8d9
00C1C8C6  84 C0                           test al, al
00C1C8C8  74 0F                           je 0x140c1c8d9
00C1C8CA  49 03 DF                        add rbx, r15
00C1C8CD  8A 03                           mov al, byte ptr [rbx]
00C1C8CF  3C 2C                           cmp al, 0x2c
00C1C8D1  75 EF                           jne 0x140c1c8c2
00C1C8D3  EB AF                           jmp 0x140c1c884
00C1C8D5  84 C0                           test al, al
00C1C8D7  75 AB                           jne 0x140c1c884
00C1C8D9  48 8D 15 E0 C6 05 00            lea rdx, [rip + 0x5c6e0]
00C1C8E0  48 8B CF                        mov rcx, rdi
00C1C8E3  E8 98 2D 8E FF                  call 0x1404ff680
00C1C8E8  48 8B D8                        mov rbx, rax
00C1C8EB  48 85 C0                        test rax, rax
00C1C8EE  74 27                           je 0x140c1c917
00C1C8F0  48 8D 15 D9 C2 05 00            lea rdx, [rip + 0x5c2d9]
00C1C8F7  48 8B C8                        mov rcx, rax
00C1C8FA  E8 81 2D 8E FF                  call 0x1404ff680
00C1C8FF  48 8B D8                        mov rbx, rax
00C1C902  44 88 3D 9E A1 3A 00            mov byte ptr [rip + 0x3aa19e], r15b
00C1C909  44 89 35 80 A2 3A 00            mov dword ptr [rip + 0x3aa280], r14d
00C1C910  44 89 35 A9 A2 3A 00            mov dword ptr [rip + 0x3aa2a9], r14d
00C1C917  48 85 DB                        test rbx, rbx
00C1C91A  0F 84 31 01 00 00               je 0x140c1ca51
00C1C920  49 03 DF                        add rbx, r15
00C1C923  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
00C1C928  48 8B CB                        mov rcx, rbx
00C1C92B  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00C1C930  41 B8 0A 00 00 00               mov r8d, 0xa
00C1C936  E8 7D 2A 8E FF                  call 0x1404ff3b8
00C1C93B  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00C1C940  44 8B F0                        mov r14d, eax
00C1C943  48 3B D9                        cmp rbx, rcx
00C1C946  74 28                           je 0x140c1c970
00C1C948  80 39 5F                        cmp byte ptr [rcx], 0x5f
00C1C94B  75 23                           jne 0x140c1c970
00C1C94D  48 8D 59 01                     lea rbx, [rcx + 1]
00C1C951  41 B8 0A 00 00 00               mov r8d, 0xa
00C1C957  48 8B CB                        mov rcx, rbx
00C1C95A  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00C1C95F  E8 54 2A 8E FF                  call 0x1404ff3b8
00C1C964  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00C1C969  44 8B F8                        mov r15d, eax
00C1C96C  33 C0                           xor eax, eax
00C1C96E  EB 05                           jmp 0x140c1c975
00C1C970  33 C0                           xor eax, eax
00C1C972  44 8B F8                        mov r15d, eax
00C1C975  48 3B D9                        cmp rbx, rcx
00C1C978  0F 84 8B 00 00 00               je 0x140c1ca09
00C1C97E  80 39 3D                        cmp byte ptr [rcx], 0x3d
00C1C981  0F 85 82 00 00 00               jne 0x140c1ca09
00C1C987  41 83 FE 40                     cmp r14d, 0x40
00C1C98B  73 7C                           jae 0x140c1ca09
00C1C98D  4D 03 F6                        add r14, r14
00C1C990  48 8D 59 01                     lea rbx, [rcx + 1]
00C1C994  48 8D 0D 65 36 3E FF            lea rcx, [rip - 0xc1c99b]
00C1C99B  4A 39 84 F1 48 CC FC 00         cmp qword ptr [rcx + r14*8 + 0xfccc48], rax
00C1C9A3  75 35                           jne 0x140c1c9da
00C1C9A5  BA 00 01 00 00                  mov edx, 0x100
00C1C9AA  B9 40 00 00 00                  mov ecx, 0x40
00C1C9AF  41 B8 00 08 00 00               mov r8d, 0x800
00C1C9B5  E8 36 57 F6 FF                  call 0x140b820f0
00C1C9BA  48 85 C0                        test rax, rax
00C1C9BD  74 7C                           je 0x140c1ca3b
00C1C9BF  48 8D 0D 3A 36 3E FF            lea rcx, [rip - 0xc1c9c6]
00C1C9C6  4A C7 84 F1 40 CC FC 00 00 08 00 00  mov qword ptr [rcx + r14*8 + 0xfccc40], 0x800
00C1C9D2  4A 89 84 F1 48 CC FC 00         mov qword ptr [rcx + r14*8 + 0xfccc48], rax
00C1C9DA  41 83 FF 20                     cmp r15d, 0x20
00C1C9DE  73 29                           jae 0x140c1ca09
00C1C9E0  41 B8 10 00 00 00               mov r8d, 0x10
00C1C9E6  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00C1C9EB  48 8B CB                        mov rcx, rbx
00C1C9EE  E8 5D 2C 8E FF                  call 0x1404ff650
00C1C9F3  48 8D 0D 06 36 3E FF            lea rcx, [rip - 0xc1c9fa]
00C1C9FA  41 8B D7                        mov edx, r15d
00C1C9FD  4A 8B 8C F1 48 CC FC 00         mov rcx, qword ptr [rcx + r14*8 + 0xfccc48]
00C1CA05  48 89 04 D1                     mov qword ptr [rcx + rdx*8], rax
00C1CA09  8A 03                           mov al, byte ptr [rbx]
00C1CA0B  45 33 F6                        xor r14d, r14d
00C1CA0E  3C 2C                           cmp al, 0x2c
00C1CA10  74 1A                           je 0x140c1ca2c
00C1CA12  45 8D 7E 01                     lea r15d, [r14 + 1]
00C1CA16  3C 20                           cmp al, 0x20
00C1CA18  74 37                           je 0x140c1ca51
00C1CA1A  84 C0                           test al, al
00C1CA1C  74 2D                           je 0x140c1ca4b
00C1CA1E  49 03 DF                        add rbx, r15
00C1CA21  8A 03                           mov al, byte ptr [rbx]
00C1CA23  3C 2C                           cmp al, 0x2c
00C1CA25  75 EF                           jne 0x140c1ca16
00C1CA27  E9 EB FE FF FF                  jmp 0x140c1c917
00C1CA2C  84 C0                           test al, al
00C1CA2E  74 1B                           je 0x140c1ca4b
00C1CA30  41 BF 01 00 00 00               mov r15d, 1
00C1CA36  E9 DC FE FF FF                  jmp 0x140c1c917
00C1CA3B  B9 31 00 00 00                  mov ecx, 0x31
00C1CA40  E8 FB 0B 8E FF                  call 0x1404fd640
00C1CA45  CC                              int3
00C1CA46  49 8B FE                        mov rdi, r14
00C1CA49  EB 06                           jmp 0x140c1ca51
00C1CA4B  41 BF 01 00 00 00               mov r15d, 1
00C1CA51  48 8B 05 98 50 30 00            mov rax, qword ptr [rip + 0x305098]
00C1CA58  48 8B CE                        mov rcx, rsi
00C1CA5B  66 44 89 35 95 9E 24 00         mov word ptr [rip + 0x249e95], r14w
00C1CA63  80 60 05 FC                     and byte ptr [rax + 5], 0xfc
00C1CA67  44 88 70 04                     mov byte ptr [rax + 4], r14b
00C1CA6B  E8 40 C5 01 00                  call 0x140c38fb0
00C1CA70  48 8B 1D 79 50 30 00            mov rbx, qword ptr [rip + 0x305079]
00C1CA77  0F B7 4B 06                     movzx ecx, word ptr [rbx + 6]
00C1CA7B  E8 F4 FB 99 FF                  call 0x1405bc674
00C1CA80  8B 0D 1A 77 3A 00               mov ecx, dword ptr [rip + 0x3a771a]
00C1CA86  48 8B D6                        mov rdx, rsi
00C1CA89  4C 09 7B 10                     or qword ptr [rbx + 0x10], r15
00C1CA8D  E8 4E EC F3 FF                  call 0x140b5b6e0
00C1CA92  84 C0                           test al, al
00C1CA94  0F 84 A0 10 00 00               je 0x140c1db3a
00C1CA9A  8B 0D 00 77 3A 00               mov ecx, dword ptr [rip + 0x3a7700]
00C1CAA0  48 8B D6                        mov rdx, rsi
00C1CAA3  E8 88 41 05 00                  call 0x140c70c30
00C1CAA8  BB 00 00 00 80                  mov ebx, 0x80000000
00C1CAAD  48 85 FF                        test rdi, rdi
00C1CAB0  74 14                           je 0x140c1cac6
00C1CAB2  48 8D 15 27 C5 05 00            lea rdx, [rip + 0x5c527]
00C1CAB9  48 8B CF                        mov rcx, rdi
00C1CABC  E8 BF 2B 8E FF                  call 0x1404ff680
00C1CAC1  48 85 C0                        test rax, rax
00C1CAC4  75 7C                           jne 0x140c1cb42
00C1CAC6  44 38 35 E3 93 24 00            cmp byte ptr [rip + 0x2493e3], r14b
00C1CACD  44 88 35 78 93 24 00            mov byte ptr [rip + 0x249378], r14b
00C1CAD4  74 41                           je 0x140c1cb17
00C1CAD6  44 38 35 DD 93 24 00            cmp byte ptr [rip + 0x2493dd], r14b
00C1CADD  74 13                           je 0x140c1caf2
00C1CADF  41 8A CF                        mov cl, r15b
00C1CAE2  E8 41 3B FA FF                  call 0x140bc0628
00C1CAE7  85 C0                           test eax, eax
00C1CAE9  78 07                           js 0x140c1caf2
00C1CAEB  44 88 3D C6 93 24 00            mov byte ptr [rip + 0x2493c6], r15b
00C1CAF2  44 38 35 B7 93 24 00            cmp byte ptr [rip + 0x2493b7], r14b
00C1CAF9  74 1C                           je 0x140c1cb17
00C1CAFB  44 38 35 B8 93 24 00            cmp byte ptr [rip + 0x2493b8], r14b
00C1CB02  74 13                           je 0x140c1cb17
00C1CB04  41 8A CF                        mov cl, r15b
00C1CB07  E8 E0 3A FA FF                  call 0x140bc05ec
00C1CB0C  85 C0                           test eax, eax
00C1CB0E  78 07                           js 0x140c1cb17
00C1CB10  44 88 3D 6A 93 24 00            mov byte ptr [rip + 0x24936a], r15b
00C1CB17  48 8D 05 22 EF 91 FF            lea rax, [rip - 0x6e10de]
00C1CB1E  41 B8 07 00 00 00               mov r8d, 7
00C1CB24  48 8B D6                        mov rdx, rsi
00C1CB27  48 89 05 22 93 24 00            mov qword ptr [rip + 0x249322], rax
00C1CB2E  41 8B CF                        mov ecx, r15d
00C1CB31  E8 EA D8 00 00                  call 0x140c2a420
00C1CB36  33 C9                           xor ecx, ecx
00C1CB38  E8 3F ED 91 FF                  call 0x14053b87c
00C1CB3D  48 85 FF                        test rdi, rdi
00C1CB40  74 3E                           je 0x140c1cb80
00C1CB42  48 8D 15 A7 C4 05 00            lea rdx, [rip + 0x5c4a7]
00C1CB49  48 8B CF                        mov rcx, rdi
00C1CB4C  E8 2F 2B 8E FF                  call 0x1404ff680
00C1CB51  48 85 C0                        test rax, rax
00C1CB54  74 2A                           je 0x140c1cb80
00C1CB56  48 8D 15 A3 C4 05 00            lea rdx, [rip + 0x5c4a3]
00C1CB5D  44 88 3D E4 75 3A 00            mov byte ptr [rip + 0x3a75e4], r15b
00C1CB64  48 8B CF                        mov rcx, rdi
00C1CB67  E8 14 2B 8E FF                  call 0x1404ff680
00C1CB6C  48 85 C0                        test rax, rax
00C1CB6F  74 08                           je 0x140c1cb79
00C1CB71  09 1D 61 28 1F 00               or dword ptr [rip + 0x1f2861], ebx
00C1CB77  EB 07                           jmp 0x140c1cb80
00C1CB79  44 09 3D 58 28 1F 00            or dword ptr [rip + 0x1f2858], r15d
00C1CB80  45 33 C0                        xor r8d, r8d
00C1CB83  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00C1CB88  41 B9 7E 00 00 40               mov r9d, 0x4000007e
00C1CB8E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C1CB93  48 8D 0D 66 34 3E FF            lea rcx, [rip - 0xc1cb9a]
00C1CB9A  41 8D 50 0B                     lea edx, [r8 + 0xb]
00C1CB9E  E8 7D E6 D7 FF                  call 0x14099b220
00C1CBA3  66 44 39 35 05 76 3A 00         cmp word ptr [rip + 0x3a7605], r14w
00C1CBAB  49 8B DD                        mov rbx, r13
00C1CBAE  48 89 5D 90                     mov qword ptr [rbp - 0x70], rbx
00C1CBB2  44 8B F8                        mov r15d, eax
00C1CBB5  48 C7 45 88 00 01 00 00         mov qword ptr [rbp - 0x78], 0x100
00C1CBBD  74 5B                           je 0x140c1cc1a
00C1CBBF  48 8D 05 EA 75 3A 00            lea rax, [rip + 0x3a75ea]
00C1CBC6  BA FF 00 00 00                  mov edx, 0xff
00C1CBCB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C1CBD0  4C 8D 4D 88                     lea r9, [rbp - 0x78]
00C1CBD4  48 8D 05 35 C4 05 00            lea rax, [rip + 0x5c435]
00C1CBDB  49 8B CD                        mov rcx, r13
00C1CBDE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C1CBE3  4C 8D 45 90                     lea r8, [rbp - 0x70]
00C1CBE7  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00C1CBEC  E8 67 F0 91 FF                  call 0x14053bc58
00C1CBF1  33 C9                           xor ecx, ecx
00C1CBF3  85 C0                           test eax, eax
00C1CBF5  79 19                           jns 0x140c1cc10
00C1CBF7  45 33 C9                        xor r9d, r9d
00C1CBFA  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C1CBFF  48 63 D0                        movsxd rdx, eax
00C1CC02  41 8D 49 32                     lea ecx, [r9 + 0x32]
00C1CC06  45 8D 41 07                     lea r8d, [r9 + 7]
00C1CC0A  E8 51 0A 8E FF                  call 0x1404fd660
00C1CC0F  CC                              int3
00C1CC10  48 8B 5D 90                     mov rbx, qword ptr [rbp - 0x70]
00C1CC14  4C 8B 75 88                     mov r14, qword ptr [rbp - 0x78]
00C1CC18  EB 0C                           jmp 0x140c1cc26
00C1CC1A  41 BE FF 00 00 00               mov r14d, 0xff
00C1CC20  33 C9                           xor ecx, ecx
00C1CC22  4C 89 75 88                     mov qword ptr [rbp - 0x78], r14
00C1CC26  88 0B                           mov byte ptr [rbx], cl
00C1CC28  4C 8D 05 01 C0 05 00            lea r8, [rip + 0x5c001]
00C1CC2F  41 B9 0A 00 00 00               mov r9d, 0xa
00C1CC35  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C1CC3A  48 FF C3                        inc rbx
00C1CC3D  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00C1CC41  48 89 5D 90                     mov qword ptr [rbp - 0x70], rbx
00C1CC45  41 8D 51 0E                     lea edx, [r9 + 0xe]
00C1CC49  E8 BE EF 91 FF                  call 0x14053bc0c
00C1CC4E  45 33 D2                        xor r10d, r10d
00C1CC51  85 C0                           test eax, eax
00C1CC53  79 1A                           jns 0x140c1cc6f
00C1CC55  48 63 D0                        movsxd rdx, eax
00C1CC58  41 8D 4A 32                     lea ecx, [r10 + 0x32]
00C1CC5C  45 8D 4A 01                     lea r9d, [r10 + 1]
00C1CC60  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
00C1CC65  45 8D 42 07                     lea r8d, [r10 + 7]
00C1CC69  E8 F2 09 8E FF                  call 0x1404fd660
00C1CC6E  CC                              int3
00C1CC6F  49 8B D6                        mov rdx, r14
00C1CC72  45 85 FF                        test r15d, r15d
00C1CC75  78 48                           js 0x140c1ccbf
00C1CC77  8B 05 CF DA 1E 00               mov eax, dword ptr [rip + 0x1edacf]
00C1CC7D  4C 8D 4D 50                     lea r9, [rbp + 0x50]
00C1CC81  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00C1CC86  0F B7 C8                        movzx ecx, ax
00C1CC89  49 83 C0 04                     add r8, 4
00C1CC8D  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00C1CC92  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00C1CC96  48 8B CB                        mov rcx, rbx
00C1CC99  E8 6E EF 91 FF                  call 0x14053bc0c
00C1CC9E  33 C9                           xor ecx, ecx
00C1CCA0  85 C0                           test eax, eax
00C1CCA2  79 49                           jns 0x140c1cced
00C1CCA4  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C1CCA9  B9 32 00 00 00                  mov ecx, 0x32
00C1CCAE  48 63 D0                        movsxd rdx, eax
00C1CCB1  44 8D 49 D0                     lea r9d, [rcx - 0x30]
00C1CCB5  44 8D 41 D5                     lea r8d, [rcx - 0x2b]
00C1CCB9  E8 A2 09 8E FF                  call 0x1404fd660
00C1CCBE  CC                              int3
00C1CCBF  4C 8D 05 5A C3 05 00            lea r8, [rip + 0x5c35a]
00C1CCC6  48 8B CB                        mov rcx, rbx
00C1CCC9  E8 6E 47 84 FF                  call 0x14046143c
00C1CCCE  85 C0                           test eax, eax
00C1CCD0  79 1B                           jns 0x140c1cced
00C1CCD2  B9 32 00 00 00                  mov ecx, 0x32
00C1CCD7  48 63 D0                        movsxd rdx, eax
00C1CCDA  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
00C1CCDF  44 8D 49 D1                     lea r9d, [rcx - 0x2f]
00C1CCE3  44 8D 41 D5                     lea r8d, [rcx - 0x2b]
00C1CCE7  E8 74 09 8E FF                  call 0x1404fd660
00C1CCEC  CC                              int3
00C1CCED  48 8B CB                        mov rcx, rbx
00C1CCF0  E8 8B 35 97 FF                  call 0x140590280
00C1CCF5  41 BE 02 00 00 00               mov r14d, 2
00C1CCFB  4D 8D BD 00 01 00 00            lea r15, [r13 + 0x100]
00C1CD02  49 8B C7                        mov rax, r15
00C1CD05  49 8B CD                        mov rcx, r13
00C1CD08  41 8B D6                        mov edx, r14d
00C1CD0B  41 8D 5E 7E                     lea ebx, [r14 + 0x7e]
00C1CD0F  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00C1CD12  0F 11 00                        movups xmmword ptr [rax], xmm0
00C1CD15  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
00C1CD19  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
00C1CD1D  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
00C1CD21  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00C1CD25  0F 10 49 30                     movups xmm1, xmmword ptr [rcx + 0x30]
00C1CD29  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
00C1CD2D  0F 10 41 40                     movups xmm0, xmmword ptr [rcx + 0x40]
00C1CD31  0F 11 40 40                     movups xmmword ptr [rax + 0x40], xmm0
00C1CD35  0F 10 49 50                     movups xmm1, xmmword ptr [rcx + 0x50]
00C1CD39  0F 11 48 50                     movups xmmword ptr [rax + 0x50], xmm1
00C1CD3D  0F 10 41 60                     movups xmm0, xmmword ptr [rcx + 0x60]
00C1CD41  0F 11 40 60                     movups xmmword ptr [rax + 0x60], xmm0
00C1CD45  48 03 C3                        add rax, rbx
00C1CD48  0F 10 49 70                     movups xmm1, xmmword ptr [rcx + 0x70]
00C1CD4C  48 03 CB                        add rcx, rbx
00C1CD4F  0F 11 48 F0                     movups xmmword ptr [rax - 0x10], xmm1
00C1CD53  48 83 EA 01                     sub rdx, 1
00C1CD57  75 B6                           jne 0x140c1cd0f
00C1CD59  48 8B D6                        mov rdx, rsi
00C1CD5C  33 C9                           xor ecx, ecx
00C1CD5E  E8 F5 55 05 00                  call 0x140c72358
00C1CD63  33 DB                           xor ebx, ebx
00C1CD65  84 C0                           test al, al
00C1CD67  0F 84 C2 0D 00 00               je 0x140c1db2f
00C1CD6D  39 1D FD B7 24 00               cmp dword ptr [rip + 0x24b7fd], ebx
00C1CD73  75 50                           jne 0x140c1cdc5
00C1CD75  41 8B 84 24 B4 01 00 00         mov eax, dword ptr [r12 + 0x1b4]
00C1CD7D  83 F8 FF                        cmp eax, -1
00C1CD80  75 19                           jne 0x140c1cd9b
00C1CD82  8B 05 80 D0 3B 00               mov eax, dword ptr [rip + 0x3bd080]
00C1CD88  41 89 84 24 B4 01 00 00         mov dword ptr [r12 + 0x1b4], eax
00C1CD90  8B 05 72 D0 3B 00               mov eax, dword ptr [rip + 0x3bd072]
00C1CD96  C6 44 24 41 01                  mov byte ptr [rsp + 0x41], 1
00C1CD9B  6B C0 3C                        imul eax, eax, 0x3c
00C1CD9E  49 8D 8C 24 B8 01 00 00         lea rcx, [r12 + 0x1b8]
00C1CDA6  48 63 D0                        movsxd rdx, eax
00C1CDA9  48 69 C2 80 96 98 00            imul rax, rdx, 0x989680
00C1CDB0  48 89 01                        mov qword ptr [rcx], rax
00C1CDB3  48 8B 05 4E 82 3A 00            mov rax, qword ptr [rip + 0x3a824e]
00C1CDBA  89 98 5C 02 00 00               mov dword ptr [rax + 0x25c], ebx
00C1CDC0  E8 63 F2 E4 FF                  call 0x140a6c028
00C1CDC5  48 8B 8E F0 00 00 00            mov rcx, qword ptr [rsi + 0xf0]
00C1CDCC  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00C1CDD1  E8 F6 E1 FF FF                  call 0x140c1afcc
00C1CDD6  48 85 FF                        test rdi, rdi
00C1CDD9  74 55                           je 0x140c1ce30
00C1CDDB  48 8D 15 5E C2 05 00            lea rdx, [rip + 0x5c25e]
00C1CDE2  48 8B CF                        mov rcx, rdi
00C1CDE5  E8 96 28 8E FF                  call 0x1404ff680
00C1CDEA  48 85 C0                        test rax, rax
00C1CDED  74 41                           je 0x140c1ce30
00C1CDEF  48 8D 15 DA BD 05 00            lea rdx, [rip + 0x5bdda]
00C1CDF6  48 8B C8                        mov rcx, rax
00C1CDF9  E8 82 28 8E FF                  call 0x1404ff680
00C1CDFE  48 85 C0                        test rax, rax
00C1CE01  74 2D                           je 0x140c1ce30
00C1CE03  48 8D 48 01                     lea rcx, [rax + 1]
00C1CE07  E8 C4 2A 8E FF                  call 0x1404ff8d0
00C1CE0C  48 8D 55 A0                     lea rdx, [rbp - 0x60]
00C1CE10  8B D8                           mov ebx, eax
00C1CE12  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C1CE17  E8 F4 12 81 FF                  call 0x14042e110
00C1CE1C  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00C1CE21  66 89 5D A0                     mov word ptr [rbp - 0x60], bx
00C1CE25  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00C1CE29  E8 9A 18 81 FF                  call 0x14042e6c8
00C1CE2E  33 DB                           xor ebx, ebx
00C1CE30  39 1D 3A B7 24 00               cmp dword ptr [rip + 0x24b73a], ebx
00C1CE36  75 1A                           jne 0x140c1ce52
00C1CE38  E8 B3 13 6E FF                  call 0x1402fe1f0
00C1CE3D  48 8B 88 C8 04 00 00            mov rcx, qword ptr [rax + 0x4c8]
00C1CE44  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00C1CE49  48 2B 81 B8 01 00 00            sub rax, qword ptr [rcx + 0x1b8]
00C1CE50  EB 05                           jmp 0x140c1ce57
00C1CE52  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00C1CE57  41 B8 04 00 00 00               mov r8d, 4
00C1CE5D  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00C1CE62  48 8D 55 98                     lea rdx, [rbp - 0x68]
00C1CE66  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C1CE6B  E8 EC BF 6A FF                  call 0x1402c8e5c
00C1CE70  E8 7B 13 6E FF                  call 0x1402fe1f0
00C1CE75  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
00C1CE7A  45 33 C0                        xor r8d, r8d
00C1CE7D  48 8D 55 98                     lea rdx, [rbp - 0x68]
00C1CE81  48 8B 88 C8 04 00 00            mov rcx, qword ptr [rax + 0x4c8]
00C1CE88  8A 05 0A 1D 1F 00               mov al, byte ptr [rip + 0x1f1d0a]
00C1CE8E  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00C1CE92  8B 81 B4 01 00 00               mov eax, dword ptr [rcx + 0x1b4]
00C1CE98  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C1CE9D  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00C1CEA1  E8 D6 80 8B FF                  call 0x1404d4f7c
00C1CEA6  48 8D 15 A3 C1 05 00            lea rdx, [rip + 0x5c1a3]
00C1CEAD  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00C1CEB1  E8 CA D8 80 FF                  call 0x14042a780
00C1CEB6  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00C1CEBB  41 B9 04 00 00 00               mov r9d, 4
00C1CEC1  4C 8D 05 A0 9D 3A 00            lea r8, [rip + 0x3a9da0]
00C1CEC8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C1CECD  48 8D 54 24 6C                  lea rdx, [rsp + 0x6c]
00C1CED2  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00C1CED6  E8 15 2E A9 FF                  call 0x1406afcf0
00C1CEDB  85 C0                           test eax, eax
00C1CEDD  78 0E                           js 0x140c1ceed
00C1CEDF  83 7C 24 68 04                  cmp dword ptr [rsp + 0x68], 4
00C1CEE4  75 07                           jne 0x140c1ceed
00C1CEE6  83 7C 24 6C 04                  cmp dword ptr [rsp + 0x6c], 4
00C1CEEB  74 0A                           je 0x140c1cef7
00C1CEED  C7 05 71 9D 3A 00 01 00 00 00   mov dword ptr [rip + 0x3a9d71], 1
00C1CEF7  48 85 FF                        test rdi, rdi
00C1CEFA  0F 84 39 01 00 00               je 0x140c1d039
00C1CF00  48 8D 15 89 C1 05 00            lea rdx, [rip + 0x5c189]
00C1CF07  48 8B CF                        mov rcx, rdi
00C1CF0A  E8 71 27 8E FF                  call 0x1404ff680
00C1CF0F  48 85 C0                        test rax, rax
00C1CF12  74 23                           je 0x140c1cf37
00C1CF14  48 8D 15 B5 BC 05 00            lea rdx, [rip + 0x5bcb5]
00C1CF1B  48 8B C8                        mov rcx, rax
00C1CF1E  E8 5D 27 8E FF                  call 0x1404ff680
00C1CF23  48 85 C0                        test rax, rax
00C1CF26  74 0F                           je 0x140c1cf37
00C1CF28  48 8D 48 01                     lea rcx, [rax + 1]
00C1CF2C  E8 9F 29 8E FF                  call 0x1404ff8d0
00C1CF31  89 05 BD 9D 3A 00               mov dword ptr [rip + 0x3a9dbd], eax
00C1CF37  48 8D 15 62 C1 05 00            lea rdx, [rip + 0x5c162]
00C1CF3E  48 8B CF                        mov rcx, rdi
00C1CF41  E8 3A 27 8E FF                  call 0x1404ff680
00C1CF46  48 85 C0                        test rax, rax
00C1CF49  74 23                           je 0x140c1cf6e
00C1CF4B  48 8D 15 7E BC 05 00            lea rdx, [rip + 0x5bc7e]
00C1CF52  48 8B C8                        mov rcx, rax
00C1CF55  E8 26 27 8E FF                  call 0x1404ff680
00C1CF5A  48 85 C0                        test rax, rax
00C1CF5D  74 0F                           je 0x140c1cf6e
00C1CF5F  48 8D 48 01                     lea rcx, [rax + 1]
00C1CF63  E8 68 29 8E FF                  call 0x1404ff8d0
00C1CF68  89 05 26 9D 3A 00               mov dword ptr [rip + 0x3a9d26], eax
00C1CF6E  48 8D 15 3B C1 05 00            lea rdx, [rip + 0x5c13b]
00C1CF75  48 8B CF                        mov rcx, rdi
00C1CF78  E8 03 27 8E FF                  call 0x1404ff680
00C1CF7D  48 85 C0                        test rax, rax
00C1CF80  74 23                           je 0x140c1cfa5
00C1CF82  48 8D 15 47 BC 05 00            lea rdx, [rip + 0x5bc47]
00C1CF89  48 8B C8                        mov rcx, rax
00C1CF8C  E8 EF 26 8E FF                  call 0x1404ff680
00C1CF91  48 85 C0                        test rax, rax
00C1CF94  74 0F                           je 0x140c1cfa5
00C1CF96  48 8D 48 01                     lea rcx, [rax + 1]
00C1CF9A  E8 31 29 8E FF                  call 0x1404ff8d0
00C1CF9F  89 05 AF 9D 3A 00               mov dword ptr [rip + 0x3a9daf], eax
00C1CFA5  38 1D FC 9A 3A 00               cmp byte ptr [rip + 0x3a9afc], bl
00C1CFAB  75 6E                           jne 0x140c1d01b
00C1CFAD  48 8D 15 1C C1 05 00            lea rdx, [rip + 0x5c11c]
00C1CFB4  48 8B CF                        mov rcx, rdi
00C1CFB7  E8 C4 26 8E FF                  call 0x1404ff680
00C1CFBC  48 85 C0                        test rax, rax
00C1CFBF  74 23                           je 0x140c1cfe4
00C1CFC1  48 8D 15 08 BC 05 00            lea rdx, [rip + 0x5bc08]
00C1CFC8  48 8B C8                        mov rcx, rax
00C1CFCB  E8 B0 26 8E FF                  call 0x1404ff680
00C1CFD0  48 85 C0                        test rax, rax
00C1CFD3  74 0F                           je 0x140c1cfe4
00C1CFD5  48 8D 48 01                     lea rcx, [rax + 1]
00C1CFD9  E8 F2 28 8E FF                  call 0x1404ff8d0
00C1CFDE  89 05 AC 9C 3A 00               mov dword ptr [rip + 0x3a9cac], eax
00C1CFE4  48 8D 15 05 C1 05 00            lea rdx, [rip + 0x5c105]
00C1CFEB  48 8B CF                        mov rcx, rdi
00C1CFEE  E8 8D 26 8E FF                  call 0x1404ff680
00C1CFF3  48 85 C0                        test rax, rax
00C1CFF6  74 23                           je 0x140c1d01b
00C1CFF8  48 8D 15 D1 BB 05 00            lea rdx, [rip + 0x5bbd1]
00C1CFFF  48 8B C8                        mov rcx, rax
00C1D002  E8 79 26 8E FF                  call 0x1404ff680
00C1D007  48 85 C0                        test rax, rax
00C1D00A  74 0F                           je 0x140c1d01b
00C1D00C  48 8D 48 01                     lea rcx, [rax + 1]
00C1D010  E8 BB 28 8E FF                  call 0x1404ff8d0
00C1D015  89 05 71 9C 3A 00               mov dword ptr [rip + 0x3a9c71], eax
00C1D01B  48 8D 15 EE C0 05 00            lea rdx, [rip + 0x5c0ee]
00C1D022  48 8B CF                        mov rcx, rdi
00C1D025  E8 56 26 8E FF                  call 0x1404ff680
00C1D02A  48 85 C0                        test rax, rax
00C1D02D  74 0A                           je 0x140c1d039
00C1D02F  C7 05 23 9E 3A 00 01 00 00 00   mov dword ptr [rip + 0x3a9e23], 1
00C1D039  33 C9                           xor ecx, ecx
00C1D03B  E8 A0 17 76 FF                  call 0x14037e7e0
00C1D040  48 89 05 81 B7 3E 00            mov qword ptr [rip + 0x3eb781], rax
00C1D047  E8 2C 9F 01 00                  call 0x140c36f78
00C1D04C  33 C9                           xor ecx, ecx
00C1D04E  E8 8D 17 76 FF                  call 0x14037e7e0
00C1D053  48 89 05 76 B7 3E 00            mov qword ptr [rip + 0x3eb776], rax
00C1D05A  E8 2D AE B9 FF                  call 0x1407b7e8c
00C1D05F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00C1D068  4C 8D 05 B1 A0 3A 00            lea r8, [rip + 0x3aa0b1]
00C1D06F  33 D2                           xor edx, edx
00C1D071  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00C1D078  E8 E3 39 7A FF                  call 0x1403c0a60
00C1D07D  E8 16 EA 91 FF                  call 0x14053ba98
00C1D082  45 33 C0                        xor r8d, r8d
00C1D085  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00C1D08A  41 B9 89 00 00 40               mov r9d, 0x40000089
00C1D090  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C1D095  48 8D 0D 64 2F 3E FF            lea rcx, [rip - 0xc1d09c]
00C1D09C  41 8D 50 0B                     lea edx, [r8 + 0xb]
00C1D0A0  E8 7B E1 D7 FF                  call 0x14099b220
00C1D0A5  85 C0                           test eax, eax
00C1D0A7  78 0B                           js 0x140c1d0b4
00C1D0A9  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00C1D0AE  48 83 C3 04                     add rbx, 4
00C1D0B2  EB 07                           jmp 0x140c1d0bb
00C1D0B4  48 8D 1D 65 C0 05 00            lea rbx, [rip + 0x5c065]
00C1D0BB  E8 D0 0C 00 00                  call 0x140c1dd90
00C1D0C0  84 C0                           test al, al
00C1D0C2  0F 84 72 0A 00 00               je 0x140c1db3a
00C1D0C8  48 8B D3                        mov rdx, rbx
00C1D0CB  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00C1D0CF  E8 6C 3E 85 FF                  call 0x140470f40
00C1D0D4  0F B7 45 B0                     movzx eax, word ptr [rbp - 0x50]
00C1D0D8  66 41 3B C6                     cmp ax, r14w
00C1D0DC  72 0C                           jb 0x140c1d0ea
00C1D0DE  B9 FE FF 00 00                  mov ecx, 0xfffe
00C1D0E3  66 03 C1                        add ax, cx
00C1D0E6  66 89 45 B0                     mov word ptr [rbp - 0x50], ax
00C1D0EA  8B 05 90 99 3A 00               mov eax, dword ptr [rip + 0x3a9990]
00C1D0F0  B9 88 00 00 40                  mov ecx, 0x40000088
00C1D0F5  83 F8 01                        cmp eax, 1
00C1D0F8  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00C1D0FD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C1D102  44 8D 49 15                     lea r9d, [rcx + 0x15]
00C1D106  44 0F 46 C9                     cmovbe r9d, ecx
00C1D10A  45 33 C0                        xor r8d, r8d
00C1D10D  48 8D 0D EC 2E 3E FF            lea rcx, [rip - 0xc1d114]
00C1D114  41 8D 50 0B                     lea edx, [r8 + 0xb]
00C1D118  E8 03 E1 D7 FF                  call 0x14099b220
00C1D11D  48 8B 0D 64 9A 3A 00            mov rcx, qword ptr [rip + 0x3a9a64]
00C1D124  45 33 C0                        xor r8d, r8d
00C1D127  41 8B D0                        mov edx, r8d
00C1D12A  8B 19                           mov ebx, dword ptr [rcx]
00C1D12C  85 DB                           test ebx, ebx
00C1D12E  74 11                           je 0x140c1d141
00C1D130  48 83 C1 18                     add rcx, 0x18
00C1D134  48 03 11                        add rdx, qword ptr [rcx]
00C1D137  48 8D 49 10                     lea rcx, [rcx + 0x10]
00C1D13B  48 83 EB 01                     sub rbx, 1
00C1D13F  75 F3                           jne 0x140c1d134
00C1D141  33 DB                           xor ebx, ebx
00C1D143  85 C0                           test eax, eax
00C1D145  78 0B                           js 0x140c1d152
00C1D147  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00C1D14C  49 83 C0 04                     add r8, 4
00C1D150  EB 07                           jmp 0x140c1d159
00C1D152  4C 8D 05 E7 BF 05 00            lea r8, [rip + 0x5bfe7]
00C1D159  44 8B 0D 20 99 3A 00            mov r9d, dword ptr [rip + 0x3a9920]
00C1D160  48 8D 82 FF 00 00 00            lea rax, [rdx + 0xff]
00C1D167  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00C1D16B  48 C1 E8 08                     shr rax, 8
00C1D16F  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00C1D174  BA 00 01 00 00                  mov edx, 0x100
00C1D179  49 8B CD                        mov rcx, r13
00C1D17C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C1D181  E8 86 EA 91 FF                  call 0x14053bc0c
00C1D186  85 C0                           test eax, eax
00C1D188  79 1B                           jns 0x140c1d1a5
00C1D18A  B9 32 00 00 00                  mov ecx, 0x32
00C1D18F  48 63 D0                        movsxd rdx, eax
00C1D192  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00C1D197  44 8D 49 D2                     lea r9d, [rcx - 0x2e]
00C1D19B  44 8D 41 D5                     lea r8d, [rcx - 0x2b]
00C1D19F  E8 BC 04 8E FF                  call 0x1404fd660
00C1D1A4  CC                              int3
00C1D1A5  49 8B CD                        mov rcx, r13
00C1D1A8  E8 D3 30 97 FF                  call 0x140590280
00C1D1AD  33 D2                           xor edx, edx
00C1D1AF  49 8B CD                        mov rcx, r13
00C1D1B2  E8 B9 56 F6 FF                  call 0x140b82870
00C1D1B7  BB 01 00 00 00                  mov ebx, 1
00C1D1BC  8B CB                           mov ecx, ebx
00C1D1BE  E8 B9 4A 05 00                  call 0x140c71c7c
00C1D1C3  45 33 ED                        xor r13d, r13d
00C1D1C6  84 C0                           test al, al
00C1D1C8  75 09                           jne 0x140c1d1d3
00C1D1CA  8D 4B 61                        lea ecx, [rbx + 0x61]
00C1D1CD  E8 6E 04 8E FF                  call 0x1404fd640
00C1D1D2  CC                              int3
00C1D1D3  48 8B CE                        mov rcx, rsi
00C1D1D6  E8 CD 3F 03 00                  call 0x140c511a8
00C1D1DB  84 C0                           test al, al
00C1D1DD  75 1C                           jne 0x140c1d1fb
00C1D1DF  45 33 C0                        xor r8d, r8d
00C1D1E2  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1D1E7  4C 8B CB                        mov r9, rbx
00C1D1EA  48 C7 C2 01 00 00 C0            mov rdx, 0xffffffffc0000001
00C1D1F1  41 8D 48 32                     lea ecx, [r8 + 0x32]
00C1D1F5  E8 66 04 8E FF                  call 0x1404fd660
00C1D1FA  CC                              int3
00C1D1FB  83 C9 FF                        or ecx, 0xffffffff
00C1D1FE  E8 BD 0B 00 00                  call 0x140c1ddc0
00C1D203  E8 4C D6 00 00                  call 0x140c2a854
00C1D208  84 C0                           test al, al
00C1D20A  75 1F                           jne 0x140c1d22b
00C1D20C  41 B9 04 00 00 00               mov r9d, 4
00C1D212  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1D217  45 33 C0                        xor r8d, r8d
00C1D21A  48 C7 C2 01 00 00 C0            mov rdx, 0xffffffffc0000001
00C1D221  41 8D 49 2E                     lea ecx, [r9 + 0x2e]
00C1D225  E8 36 04 8E FF                  call 0x1404fd660
00C1D22A  CC                              int3
00C1D22B  8B CB                           mov ecx, ebx
00C1D22D  E8 2E 44 05 00                  call 0x140c71660
00C1D232  84 C0                           test al, al
00C1D234  75 1C                           jne 0x140c1d252
00C1D236  45 33 C0                        xor r8d, r8d
00C1D239  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1D23E  4D 8B CE                        mov r9, r14
00C1D241  48 C7 C2 01 00 00 C0            mov rdx, 0xffffffffc0000001
00C1D248  41 8D 48 32                     lea ecx, [r8 + 0x32]
00C1D24C  E8 0F 04 8E FF                  call 0x1404fd660
00C1D251  CC                              int3
00C1D252  8B 0D 48 6F 3A 00               mov ecx, dword ptr [rip + 0x3a6f48]
00C1D258  33 D2                           xor edx, edx
00C1D25A  E8 D1 8B F6 FF                  call 0x140b85e30
00C1D25F  84 C0                           test al, al
00C1D261  75 1F                           jne 0x140c1d282
00C1D263  41 B9 03 00 00 00               mov r9d, 3
00C1D269  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1D26E  45 33 C0                        xor r8d, r8d
00C1D271  48 C7 C2 01 00 00 C0            mov rdx, 0xffffffffc0000001
00C1D278  41 8D 49 2F                     lea ecx, [r9 + 0x2f]
00C1D27C  E8 DF 03 8E FF                  call 0x1404fd660
00C1D281  CC                              int3
00C1D282  4C 8D 0D 67 9C 3A 00            lea r9, [rip + 0x3a9c67]
00C1D289  4C 8D 05 A0 A0 3A 00            lea r8, [rip + 0x3aa0a0]
00C1D290  48 8D 15 11 A1 3A 00            lea rdx, [rip + 0x3aa111]
00C1D297  48 8D 0D 9A A0 3A 00            lea rcx, [rip + 0x3aa09a]
00C1D29E  48 FF 15 CB 41 53 FF            call qword ptr [rip - 0xacbe35]
00C1D2A5  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00C1D2AA  BA 00 00 00 80                  mov edx, 0x80000000
00C1D2AF  8D 0C 10                        lea ecx, [rax + rdx]
00C1D2B2  85 CA                           test edx, ecx
00C1D2B4  75 1D                           jne 0x140c1d2d3
00C1D2B6  3D BB 00 00 C0                  cmp eax, 0xc00000bb
00C1D2BB  74 16                           je 0x140c1d2d3
00C1D2BD  33 D2                           xor edx, edx
00C1D2BF  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1D2C4  45 33 C9                        xor r9d, r9d
00C1D2C7  45 33 C0                        xor r8d, r8d
00C1D2CA  8D 4A 32                        lea ecx, [rdx + 0x32]
00C1D2CD  E8 8E 03 8E FF                  call 0x1404fd660
00C1D2D2  CC                              int3
00C1D2D3  E8 0C 8F 00 00                  call 0x140c261e4
00C1D2D8  85 C0                           test eax, eax
00C1D2DA  79 18                           jns 0x140c1d2f4
00C1D2DC  45 33 C9                        xor r9d, r9d
00C1D2DF  48 63 D0                        movsxd rdx, eax
00C1D2E2  45 33 C0                        xor r8d, r8d
00C1D2E5  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1D2EA  41 8D 49 32                     lea ecx, [r9 + 0x32]
00C1D2EE  E8 6D 03 8E FF                  call 0x1404fd660
00C1D2F3  CC                              int3
00C1D2F4  33 C9                           xor ecx, ecx
00C1D2F6  E8 A1 DA A7 FF                  call 0x14069ad9c
00C1D2FB  E8 8C FE 04 00                  call 0x140c6d18c
00C1D300  33 C9                           xor ecx, ecx
00C1D302  E8 7D E9 02 00                  call 0x140c4bc84
00C1D307  E8 40 D4 02 00                  call 0x140c4a74c
00C1D30C  84 C0                           test al, al
00C1D30E  75 0B                           jne 0x140c1d31b
00C1D310  B9 63 00 00 00                  mov ecx, 0x63
00C1D315  E8 26 03 8E FF                  call 0x1404fd640
00C1D31A  CC                              int3
00C1D31B  C7 05 2B 9B 3A 00 88 02 00 00   mov dword ptr [rip + 0x3a9b2b], 0x288
00C1D325  E8 72 F8 B2 FF                  call 0x14074cb9c
00C1D32A  85 C0                           test eax, eax
00C1D32C  79 0B                           jns 0x140c1d339
00C1D32E  B9 6A 00 00 00                  mov ecx, 0x6a
00C1D333  E8 08 03 8E FF                  call 0x1404fd640
00C1D338  CC                              int3
00C1D339  48 8B 05 D8 98 3A 00            mov rax, qword ptr [rip + 0x3a98d8]
00C1D340  48 8B D6                        mov rdx, rsi
00C1D343  8B CB                           mov ecx, ebx
00C1D345  48 89 05 24 9C 3A 00            mov qword ptr [rip + 0x3a9c24], rax
00C1D34C  E8 07 1A FD FF                  call 0x140beed58
00C1D351  E8 BE A7 BA FF                  call 0x1407c7b14
00C1D356  48 8B CE                        mov rcx, rsi
00C1D359  E8 BA D6 FF FF                  call 0x140c1aa18
00C1D35E  85 C0                           test eax, eax
00C1D360  79 18                           jns 0x140c1d37a
00C1D362  45 33 C9                        xor r9d, r9d
00C1D365  48 63 D0                        movsxd rdx, eax
00C1D368  45 33 C0                        xor r8d, r8d
00C1D36B  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1D370  41 8D 49 64                     lea ecx, [r9 + 0x64]
00C1D374  E8 E7 02 8E FF                  call 0x1404fd660
00C1D379  CC                              int3
00C1D37A  33 C9                           xor ecx, ecx
00C1D37C  E8 5F 14 76 FF                  call 0x14037e7e0
00C1D381  48 8B D6                        mov rdx, rsi
00C1D384  48 89 05 5D B4 3E 00            mov qword ptr [rip + 0x3eb45d], rax
00C1D38B  8B CB                           mov ecx, ebx
00C1D38D  E8 FE 15 FD FF                  call 0x140bee990
00C1D392  33 C9                           xor ecx, ecx
00C1D394  E8 47 14 76 FF                  call 0x14037e7e0
00C1D399  8B CB                           mov ecx, ebx
00C1D39B  48 89 05 4E B4 3E 00            mov qword ptr [rip + 0x3eb44e], rax
00C1D3A2  E8 41 0F FD FF                  call 0x140bee2e8
00C1D3A7  84 C0                           test al, al
00C1D3A9  75 0B                           jne 0x140c1d3b6
00C1D3AB  B9 66 00 00 00                  mov ecx, 0x66
00C1D3B0  E8 8B 02 8E FF                  call 0x1404fd640
00C1D3B5  CC                              int3
00C1D3B6  48 8B CE                        mov rcx, rsi
00C1D3B9  E8 0E 86 03 00                  call 0x140c559cc
00C1D3BE  84 C0                           test al, al
00C1D3C0  75 0B                           jne 0x140c1d3cd
00C1D3C2  B9 67 00 00 00                  mov ecx, 0x67
00C1D3C7  E8 74 02 8E FF                  call 0x1404fd640
00C1D3CC  CC                              int3
00C1D3CD  E8 C2 79 02 00                  call 0x140c44d94
00C1D3D2  E8 55 82 BA FF                  call 0x1407c562c
00C1D3D7  85 C0                           test eax, eax
00C1D3D9  79 19                           jns 0x140c1d3f4
00C1D3DB  45 33 C9                        xor r9d, r9d
00C1D3DE  48 63 D0                        movsxd rdx, eax
00C1D3E1  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1D3E6  41 8D 49 32                     lea ecx, [r9 + 0x32]
00C1D3EA  45 8D 41 0C                     lea r8d, [r9 + 0xc]
00C1D3EE  E8 6D 02 8E FF                  call 0x1404fd660
00C1D3F3  CC                              int3
00C1D3F4  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00C1D3F9  44 88 6C 24 40                  mov byte ptr [rsp + 0x40], r13b
00C1D3FE  E8 35 A1 BA FF                  call 0x1407c7538
00C1D403  85 C0                           test eax, eax
00C1D405  78 16                           js 0x140c1d41d
00C1D407  44 38 6C 24 40                  cmp byte ptr [rsp + 0x40], r13b
00C1D40C  74 0F                           je 0x140c1d41d
00C1D40E  48 8B 05 F3 7B 3A 00            mov rax, qword ptr [rip + 0x3a7bf3]
00C1D415  0F BA A8 F0 02 00 00 08         bts dword ptr [rax + 0x2f0], 8
00C1D41D  44 39 2D 6C 6D 3A 00            cmp dword ptr [rip + 0x3a6d6c], r13d
00C1D424  74 0F                           je 0x140c1d435
00C1D426  48 8B 05 DB 7B 3A 00            mov rax, qword ptr [rip + 0x3a7bdb]
00C1D42D  0F BA A8 F0 02 00 00 09         bts dword ptr [rax + 0x2f0], 9
00C1D435  44 39 2D 30 27 2D 00            cmp dword ptr [rip + 0x2d2730], r13d
00C1D43C  74 0F                           je 0x140c1d44d
00C1D43E  48 8B 05 C3 7B 3A 00            mov rax, qword ptr [rip + 0x3a7bc3]
00C1D445  0F BA A8 F0 02 00 00 0A         bts dword ptr [rax + 0x2f0], 0xa
00C1D44D  33 C9                           xor ecx, ecx
00C1D44F  E8 8C 13 76 FF                  call 0x14037e7e0
00C1D454  BB 78 00 00 00                  mov ebx, 0x78
00C1D459  48 89 05 58 B3 3E 00            mov qword ptr [rip + 0x3eb358], rax
00C1D460  44 8B C3                        mov r8d, ebx
00C1D463  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00C1D467  33 D2                           xor edx, edx
00C1D469  E8 D2 97 AA FF                  call 0x1406c6c40
00C1D46E  44 38 2D 0F 96 3A 00            cmp byte ptr [rip + 0x3a960f], r13b
00C1D475  48 8D 05 A4 BB BD FF            lea rax, [rip - 0x42445c]
00C1D47C  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00C1D480  48 8D 05 59 BC BD FF            lea rax, [rip - 0x4243a7]
00C1D487  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00C1D48B  48 8D 05 FE B7 74 FF            lea rax, [rip - 0x8b4802]
00C1D492  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00C1D496  48 8D 05 E3 91 F6 FF            lea rax, [rip - 0x96e1d]
00C1D49D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00C1D4A1  48 8D 05 68 BB FA FF            lea rax, [rip - 0x54498]
00C1D4A8  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00C1D4AC  48 8D 05 BD B9 7F FF            lea rax, [rip - 0x804643]
00C1D4B3  48 89 45 00                     mov qword ptr [rbp], rax
00C1D4B7  48 8D 05 02 1F BC FF            lea rax, [rip - 0x43e0fe]
00C1D4BE  48 89 45 08                     mov qword ptr [rbp + 8], rax
00C1D4C2  48 8D 05 07 B8 71 FF            lea rax, [rip - 0x8e47f9]
00C1D4C9  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00C1D4CD  48 8D 05 4C 91 81 FF            lea rax, [rip - 0x7e6eb4]
00C1D4D4  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
00C1D4D8  89 5D D0                        mov dword ptr [rbp - 0x30], ebx
00C1D4DB  75 05                           jne 0x140c1d4e2
00C1D4DD  4D 8B CD                        mov r9, r13
00C1D4E0  EB 23                           jmp 0x140c1d505
00C1D4E2  48 8D 05 A7 26 97 FF            lea rax, [rip - 0x68d959]
00C1D4E9  48 89 05 40 B2 3E 00            mov qword ptr [rip + 0x3eb240], rax
00C1D4F0  4C 8D 0D 39 B2 3E 00            lea r9, [rip + 0x3eb239]
00C1D4F7  48 8D 05 12 CF 00 00            lea rax, [rip + 0xcf12]
00C1D4FE  48 89 05 33 B2 3E 00            mov qword ptr [rip + 0x3eb233], rax
00C1D505  E8 EA 31 FA FF                  call 0x140bc06f4
00C1D50A  4C 8B C0                        mov r8, rax
00C1D50D  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00C1D511  48 8B CE                        mov rcx, rsi
00C1D514  48 FF 15 C5 3D 53 FF            call qword ptr [rip - 0xacc23b]
00C1D51B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00C1D520  33 C9                           xor ecx, ecx
00C1D522  48 63 D8                        movsxd rbx, eax
00C1D525  E8 B6 12 76 FF                  call 0x14037e7e0
00C1D52A  48 89 05 8F B2 3E 00            mov qword ptr [rip + 0x3eb28f], rax
00C1D531  B8 00 00 00 80                  mov eax, 0x80000000
00C1D536  8D 0C 03                        lea ecx, [rbx + rax]
00C1D539  85 C8                           test eax, ecx
00C1D53B  75 23                           jne 0x140c1d560
00C1D53D  81 FB BB 00 00 C0               cmp ebx, 0xc00000bb
00C1D543  74 1B                           je 0x140c1d560
00C1D545  41 B9 01 00 00 00               mov r9d, 1
00C1D54B  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1D550  48 8B D3                        mov rdx, rbx
00C1D553  45 33 C0                        xor r8d, r8d
00C1D556  41 8D 49 31                     lea ecx, [r9 + 0x31]
00C1D55A  E8 01 01 8E FF                  call 0x1404fd660
00C1D55F  CC                              int3
00C1D560  0F 28 45 20                     movaps xmm0, xmmword ptr [rbp + 0x20]
00C1D564  48 8B D6                        mov rdx, rsi
00C1D567  0F 28 4D 30                     movaps xmm1, xmmword ptr [rbp + 0x30]
00C1D56B  33 C9                           xor ecx, ecx
00C1D56D  0F 11 05 6C 1A 2E 00            movups xmmword ptr [rip + 0x2e1a6c], xmm0
00C1D574  F2 0F 10 45 40                  movsd xmm0, qword ptr [rbp + 0x40]
00C1D579  F2 0F 11 05 7F 1A 2E 00         movsd qword ptr [rip + 0x2e1a7f], xmm0
00C1D581  0F 11 0D 68 1A 2E 00            movups xmmword ptr [rip + 0x2e1a68], xmm1
00C1D588  E8 C3 3B 05 00                  call 0x140c71150
00C1D58D  85 C0                           test eax, eax
00C1D58F  79 19                           jns 0x140c1d5aa
00C1D591  45 33 C9                        xor r9d, r9d
00C1D594  48 63 D0                        movsxd rdx, eax
00C1D597  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1D59C  41 8D 49 32                     lea ecx, [r9 + 0x32]
00C1D5A0  45 8D 41 08                     lea r8d, [r9 + 8]
00C1D5A4  E8 B7 00 8E FF                  call 0x1404fd660
00C1D5A9  CC                              int3
00C1D5AA  48 8B CE                        mov rcx, rsi
00C1D5AD  E8 DE ED FF FF                  call 0x140c1c390
00C1D5B2  85 C0                           test eax, eax
00C1D5B4  79 19                           jns 0x140c1d5cf
00C1D5B6  45 33 C9                        xor r9d, r9d
00C1D5B9  48 63 D0                        movsxd rdx, eax
00C1D5BC  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1D5C1  41 8D 49 32                     lea ecx, [r9 + 0x32]
00C1D5C5  45 8D 41 09                     lea r8d, [r9 + 9]
00C1D5C9  E8 92 00 8E FF                  call 0x1404fd660
00C1D5CE  CC                              int3
00C1D5CF  E8 F8 F4 01 00                  call 0x140c3cacc
00C1D5D4  33 C9                           xor ecx, ecx
00C1D5D6  E8 61 91 05 00                  call 0x140c7673c
00C1D5DB  85 C0                           test eax, eax
00C1D5DD  79 19                           jns 0x140c1d5f8
00C1D5DF  45 33 C9                        xor r9d, r9d
00C1D5E2  48 63 D0                        movsxd rdx, eax
00C1D5E5  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1D5EA  41 8D 49 32                     lea ecx, [r9 + 0x32]
00C1D5EE  45 8D 41 0B                     lea r8d, [r9 + 0xb]
00C1D5F2  E8 69 00 8E FF                  call 0x1404fd660
00C1D5F7  CC                              int3
00C1D5F8  B9 01 00 00 00                  mov ecx, 1
00C1D5FD  E8 B6 18 FD FF                  call 0x140beeeb8
00C1D602  85 C0                           test eax, eax
00C1D604  79 19                           jns 0x140c1d61f
00C1D606  45 33 C9                        xor r9d, r9d
00C1D609  48 63 D0                        movsxd rdx, eax
00C1D60C  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1D611  41 8D 49 32                     lea ecx, [r9 + 0x32]
00C1D615  45 8D 41 0A                     lea r8d, [r9 + 0xa]
00C1D619  E8 42 00 8E FF                  call 0x1404fd660
00C1D61E  CC                              int3
00C1D61F  48 8B 86 F0 00 00 00            mov rax, qword ptr [rsi + 0xf0]
00C1D626  44 84 B0 60 0A 00 00            test byte ptr [rax + 0xa60], r14b
00C1D62D  74 14                           je 0x140c1d643
00C1D62F  48 8D 15 3A BB 05 00            lea rdx, [rip + 0x5bb3a]
00C1D636  48 8B CF                        mov rcx, rdi
00C1D639  E8 42 20 8E FF                  call 0x1404ff680
00C1D63E  48 85 C0                        test rax, rax
00C1D641  74 23                           je 0x140c1d666
00C1D643  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
00C1D648  48 8D 0D 69 32 40 FF            lea rcx, [rip - 0xbfcd97]
00C1D64F  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
00C1D654  45 33 C9                        xor r9d, r9d
00C1D657  45 33 C0                        xor r8d, r8d
00C1D65A  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1D65F  33 D2                           xor edx, edx
00C1D661  E8 AA 36 A9 FF                  call 0x1406b0d10
00C1D666  F7 05 20 94 3A 00 00 00 00 02   test dword ptr [rip + 0x3a9420], 0x2000000
00C1D670  74 23                           je 0x140c1d695
00C1D672  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
00C1D677  48 8D 0D 2A 34 40 FF            lea rcx, [rip - 0xbfcbd6]
00C1D67E  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
00C1D683  45 33 C9                        xor r9d, r9d
00C1D686  45 33 C0                        xor r8d, r8d
00C1D689  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1D68E  33 D2                           xor edx, edx
00C1D690  E8 7B 36 A9 FF                  call 0x1406b0d10
00C1D695  BA 01 00 00 00                  mov edx, 1
00C1D69A  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00C1D69E  44 8B C2                        mov r8d, edx
00C1D6A1  E8 9A 1C 88 FF                  call 0x14049f340
00C1D6A6  E8 E5 39 03 00                  call 0x140c51090
00C1D6AB  E8 60 81 DA FF                  call 0x1409c5810
00C1D6B0  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00C1D6B5  E8 5E 81 BA FF                  call 0x1407c5818
00C1D6BA  41 8B 9C 24 B4 01 00 00         mov ebx, dword ptr [r12 + 0x1b4]
00C1D6C2  33 C9                           xor ecx, ecx
00C1D6C4  E8 A3 DD E4 FF                  call 0x140a6b46c
00C1D6C9  E8 A6 81 DA FF                  call 0x1409c5874
00C1D6CE  44 38 6C 24 41                  cmp byte ptr [rsp + 0x41], r13b
00C1D6D3  74 36                           je 0x140c1d70b
00C1D6D5  E8 16 0B 6E FF                  call 0x1402fe1f0
00C1D6DA  41 B8 04 00 00 00               mov r8d, 4
00C1D6E0  48 8B 88 C8 04 00 00            mov rcx, qword ptr [rax + 0x4c8]
00C1D6E7  48 8B 91 B8 01 00 00            mov rdx, qword ptr [rcx + 0x1b8]
00C1D6EE  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00C1D6F3  48 03 CA                        add rcx, rdx
00C1D6F6  48 8D 55 98                     lea rdx, [rbp - 0x68]
00C1D6FA  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00C1D6FF  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C1D704  E8 53 B7 6A FF                  call 0x1402c8e5c
00C1D709  EB 13                           jmp 0x140c1d71e
00C1D70B  41 3B 9C 24 B4 01 00 00         cmp ebx, dword ptr [r12 + 0x1b4]
00C1D713  74 09                           je 0x140c1d71e
00C1D715  33 D2                           xor edx, edx
00C1D717  33 C9                           xor ecx, ecx
00C1D719  E8 92 31 A9 FF                  call 0x1406b08b0
00C1D71E  E8 C9 B7 00 00                  call 0x140c28eec
00C1D723  84 C0                           test al, al
00C1D725  75 0B                           jne 0x140c1d732
00C1D727  B9 68 00 00 00                  mov ecx, 0x68
00C1D72C  E8 0F FF 8D FF                  call 0x1404fd640
00C1D731  CC                              int3
00C1D732  44 89 6C 24 38                  mov dword ptr [rsp + 0x38], r13d
00C1D737  48 8D 0D 42 AB 20 00            lea rcx, [rip + 0x20ab42]
00C1D73E  66 44 89 6C 24 30               mov word ptr [rsp + 0x30], r13w
00C1D744  41 B9 00 02 00 00               mov r9d, 0x200
00C1D74A  C7 44 24 28 6C 7A 64 63         mov dword ptr [rsp + 0x28], 0x63647a6c
00C1D752  45 33 C0                        xor r8d, r8d
00C1D755  33 D2                           xor edx, edx
00C1D757  48 C7 44 24 20 58 00 00 00      mov qword ptr [rsp + 0x20], 0x58
00C1D760  E8 BB AF 84 FF                  call 0x140468720
00C1D765  33 C9                           xor ecx, ecx
00C1D767  66 C7 44 24 30 10 00            mov word ptr [rsp + 0x30], 0x10
00C1D76E  41 BC 01 00 00 00               mov r12d, 1
00C1D774  C7 44 24 28 52 52 6C 65         mov dword ptr [rsp + 0x28], 0x656c5252
00C1D77C  41 8B C4                        mov eax, r12d
00C1D77F  48 C7 44 24 20 38 00 00 00      mov qword ptr [rsp + 0x20], 0x38
00C1D788  0F A2                           cpuid
00C1D78A  44 8B C2                        mov r8d, edx
00C1D78D  8B C1                           mov eax, ecx
00C1D78F  25 00 02 00 00                  and eax, 0x200
00C1D794  41 8B D5                        mov edx, r13d
00C1D797  89 05 A7 A3 24 00               mov dword ptr [rip + 0x24a3a7], eax
00C1D79D  B8 02 00 10 00                  mov eax, 0x100002
00C1D7A2  23 C8                           and ecx, eax
00C1D7A4  3B C8                           cmp ecx, eax
00C1D7A6  0F 94 C2                        sete dl
00C1D7A9  41 0F BA E0 1A                  bt r8d, 0x1a
00C1D7AE  0F 92 C0                        setb al
00C1D7B1  45 33 C9                        xor r9d, r9d
00C1D7B4  0F B6 C8                        movzx ecx, al
00C1D7B7  45 33 C0                        xor r8d, r8d
00C1D7BA  23 D1                           and edx, ecx
00C1D7BC  48 8D 0D 3D AA 20 00            lea rcx, [rip + 0x20aa3d]
00C1D7C3  89 15 77 A3 24 00               mov dword ptr [rip + 0x24a377], edx
00C1D7C9  33 D2                           xor edx, edx
00C1D7CB  E8 60 F4 E8 FF                  call 0x140aacc30
00C1D7D0  48 8B CE                        mov rcx, rsi
00C1D7D3  E8 B8 5F 96 FF                  call 0x140583790
00C1D7D8  33 C9                           xor ecx, ecx
00C1D7DA  E8 E1 05 00 00                  call 0x140c1ddc0
00C1D7DF  4C 8D 05 FA 9D 32 00            lea r8, [rip + 0x329dfa]
00C1D7E6  48 8B D6                        mov rdx, rsi
00C1D7E9  41 8B CC                        mov ecx, r12d
00C1D7EC  48 FF 15 C5 3E 53 FF            call qword ptr [rip - 0xacc13b]
00C1D7F3  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00C1D7F8  E8 67 51 01 00                  call 0x140c32964
00C1D7FD  84 C0                           test al, al
00C1D7FF  75 0B                           jne 0x140c1d80c
00C1D801  B9 90 00 00 00                  mov ecx, 0x90
00C1D806  E8 35 FE 8D FF                  call 0x1404fd640
00C1D80B  CC                              int3
00C1D80C  48 85 FF                        test rdi, rdi
00C1D80F  0F 84 29 01 00 00               je 0x140c1d93e
00C1D815  48 8D 15 64 B9 05 00            lea rdx, [rip + 0x5b964]
00C1D81C  48 8B CF                        mov rcx, rdi
00C1D81F  E8 5C 1E 8E FF                  call 0x1404ff680
00C1D824  48 85 C0                        test rax, rax
00C1D827  0F 84 11 01 00 00               je 0x140c1d93e
00C1D82D  48 8D 58 09                     lea rbx, [rax + 9]
00C1D831  BF 07 00 00 00                  mov edi, 7
00C1D836  44 8B C7                        mov r8d, edi
00C1D839  48 8D 15 50 B9 05 00            lea rdx, [rip + 0x5b950]
00C1D840  48 8B CB                        mov rcx, rbx
00C1D843  E8 D8 8E AA FF                  call 0x1406c6720
00C1D848  85 C0                           test eax, eax
00C1D84A  75 09                           jne 0x140c1d855
00C1D84C  44 89 25 71 69 3A 00            mov dword ptr [rip + 0x3a6971], r12d
00C1D853  EB 1D                           jmp 0x140c1d872
00C1D855  4C 8B C7                        mov r8, rdi
00C1D858  48 8D 15 41 B9 05 00            lea rdx, [rip + 0x5b941]
00C1D85F  48 8B CB                        mov rcx, rbx
00C1D862  E8 B9 8E AA FF                  call 0x1406c6720
00C1D867  85 C0                           test eax, eax
00C1D869  75 0C                           jne 0x140c1d877
00C1D86B  44 89 35 52 69 3A 00            mov dword ptr [rip + 0x3a6952], r14d
00C1D872  48 03 DF                        add rbx, rdi
00C1D875  EB 31                           jmp 0x140c1d8a8
00C1D877  41 B8 08 00 00 00               mov r8d, 8
00C1D87D  48 8D 15 2C B9 05 00            lea rdx, [rip + 0x5b92c]
00C1D884  48 8B CB                        mov rcx, rbx
00C1D887  E8 94 8E AA FF                  call 0x1406c6720
00C1D88C  85 C0                           test eax, eax
00C1D88E  75 11                           jne 0x140c1d8a1
00C1D890  B8 03 00 00 00                  mov eax, 3
00C1D895  48 83 C3 08                     add rbx, 8
00C1D899  89 05 25 69 3A 00               mov dword ptr [rip + 0x3a6925], eax
00C1D89F  EB 07                           jmp 0x140c1d8a8
00C1D8A1  44 89 2D 1C 69 3A 00            mov dword ptr [rip + 0x3a691c], r13d
00C1D8A8  44 38 2B                        cmp byte ptr [rbx], r13b
00C1D8AB  74 26                           je 0x140c1d8d3
00C1D8AD  41 B8 10 00 00 00               mov r8d, 0x10
00C1D8B3  48 8D 15 06 B9 05 00            lea rdx, [rip + 0x5b906]
00C1D8BA  48 8B CB                        mov rcx, rbx
00C1D8BD  E8 5E 8E AA FF                  call 0x1406c6720
00C1D8C2  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
00C1D8C6  85 C0                           test eax, eax
00C1D8C8  0F B6 C9                        movzx ecx, cl
00C1D8CB  41 0F 44 CC                     cmove ecx, r12d
00C1D8CF  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
00C1D8D3  8B 05 EB 68 3A 00               mov eax, dword ptr [rip + 0x3a68eb]
00C1D8D9  85 C0                           test eax, eax
00C1D8DB  74 61                           je 0x140c1d93e
00C1D8DD  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
00C1D8E2  45 8B CD                        mov r9d, r13d
00C1D8E5  41 2B C4                        sub eax, r12d
00C1D8E8  74 1A                           je 0x140c1d904
00C1D8EA  41 2B C4                        sub eax, r12d
00C1D8ED  74 0D                           je 0x140c1d8fc
00C1D8EF  41 3B C4                        cmp eax, r12d
00C1D8F2  75 16                           jne 0x140c1d90a
00C1D8F4  41 B9 AA 00 00 00               mov r9d, 0xaa
00C1D8FA  EB 0E                           jmp 0x140c1d90a
00C1D8FC  41 B9 A9 00 00 00               mov r9d, 0xa9
00C1D902  EB 06                           jmp 0x140c1d90a
00C1D904  41 B9 A8 00 00 00               mov r9d, 0xa8
00C1D90A  45 33 C0                        xor r8d, r8d
00C1D90D  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00C1D912  48 8D 1D E7 26 3E FF            lea rbx, [rip - 0xc1d919]
00C1D919  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C1D91E  48 8B CB                        mov rcx, rbx
00C1D921  41 8D 50 0B                     lea edx, [r8 + 0xb]
00C1D925  E8 F6 D8 D7 FF                  call 0x14099b220
00C1D92A  85 C0                           test eax, eax
00C1D92C  78 17                           js 0x140c1d945
00C1D92E  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00C1D933  48 83 C1 04                     add rcx, 4
00C1D937  E8 44 29 97 FF                  call 0x140590280
00C1D93C  EB 07                           jmp 0x140c1d945
00C1D93E  48 8D 1D BB 26 3E FF            lea rbx, [rip - 0xc1d945]
00C1D945  48 8B 86 F0 00 00 00            mov rax, qword ptr [rsi + 0xf0]
00C1D94C  F7 80 84 00 00 00 00 08 00 00   test dword ptr [rax + 0x84], 0x800
00C1D956  74 3C                           je 0x140c1d994
00C1D958  45 33 C0                        xor r8d, r8d
00C1D95B  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00C1D960  41 B9 B7 00 00 00               mov r9d, 0xb7
00C1D966  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C1D96B  48 8B CB                        mov rcx, rbx
00C1D96E  41 8D 50 0B                     lea edx, [r8 + 0xb]
00C1D972  E8 A9 D8 D7 FF                  call 0x14099b220
00C1D977  85 C0                           test eax, eax
00C1D979  78 0E                           js 0x140c1d989
00C1D97B  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00C1D980  48 83 C1 04                     add rcx, 4
00C1D984  E8 F7 28 97 FF                  call 0x140590280
00C1D989  49 8B D7                        mov rdx, r15
00C1D98C  48 8B CE                        mov rcx, rsi
00C1D98F  E8 B4 DD AF FF                  call 0x14071b748
00C1D994  E8 D7 47 03 00                  call 0x140c52170
00C1D999  48 8B 05 68 76 3A 00            mov rax, qword ptr [rip + 0x3a7668]
00C1D9A0  33 C9                           xor ecx, ecx
00C1D9A2  83 88 E0 02 00 00 FF            or dword ptr [rax + 0x2e0], 0xffffffff
00C1D9A9  E8 26 12 FD FF                  call 0x140beebd4
00C1D9AE  41 8B CE                        mov ecx, r14d
00C1D9B1  48 FF 15 58 3C 53 FF            call qword ptr [rip - 0xacc3a8]
00C1D9B8  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00C1D9BD  8B 05 25 91 3A 00               mov eax, dword ptr [rip + 0x3a9125]
00C1D9C3  39 05 4F C1 3B 00               cmp dword ptr [rip + 0x3bc14f], eax
00C1D9C9  76 06                           jbe 0x140c1d9d1
00C1D9CB  89 05 47 C1 3B 00               mov dword ptr [rip + 0x3bc147], eax
00C1D9D1  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00C1D9D6  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
00C1D9DB  44 89 2D 26 C7 2D 00            mov dword ptr [rip + 0x2dc726], r13d
00C1D9E2  E8 D1 7E BB FF                  call 0x1407d58b8
00C1D9E7  85 C0                           test eax, eax
00C1D9E9  78 0A                           js 0x140c1d9f5
00C1D9EB  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00C1D9EF  89 05 13 C7 2D 00               mov dword ptr [rip + 0x2dc713], eax
00C1D9F5  E8 26 D5 FF FF                  call 0x140c1af20
00C1D9FA  44 38 2D 47 67 3A 00            cmp byte ptr [rip + 0x3a6747], r13b
00C1DA01  48 8B 0D 00 76 3A 00            mov rcx, qword ptr [rip + 0x3a7600]
00C1DA08  66 89 81 D6 02 00 00            mov word ptr [rcx + 0x2d6], ax
00C1DA0F  74 05                           je 0x140c1da16
00C1DA11  E8 2A CE FF FF                  call 0x140c1a840
00C1DA16  48 FF 15 FB 3C 53 FF            call qword ptr [rip - 0xacc305]
00C1DA1D  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00C1DA22  48 8B CE                        mov rcx, rsi
00C1DA25  E8 A2 CB 02 00                  call 0x140c4a5cc
00C1DA2A  85 C0                           test eax, eax
00C1DA2C  79 1B                           jns 0x140c1da49
00C1DA2E  45 33 C9                        xor r9d, r9d
00C1DA31  48 63 D0                        movsxd rdx, eax
00C1DA34  41 B8 53 65 43 69               mov r8d, 0x69436553
00C1DA3A  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1DA3F  41 8D 49 32                     lea ecx, [r9 + 0x32]
00C1DA43  E8 18 FC 8D FF                  call 0x1404fd660
00C1DA48  CC                              int3
00C1DA49  48 8D 05 30 D2 2D 00            lea rax, [rip + 0x2dd230]
00C1DA50  44 89 2D 01 D0 1E 00            mov dword ptr [rip + 0x1ed001], r13d
00C1DA57  48 89 05 2A D2 2D 00            mov qword ptr [rip + 0x2dd22a], rax
00C1DA5E  48 8B D6                        mov rdx, rsi
00C1DA61  48 89 05 18 D2 2D 00            mov qword ptr [rip + 0x2dd218], rax
00C1DA68  41 8B CC                        mov ecx, r12d
00C1DA6B  48 8D 05 D6 D1 2D 00            lea rax, [rip + 0x2dd1d6]
00C1DA72  44 89 2D 1F D2 2D 00            mov dword ptr [rip + 0x2dd21f], r13d
00C1DA79  48 89 05 D0 D1 2D 00            mov qword ptr [rip + 0x2dd1d0], rax
00C1DA80  48 89 05 C1 D1 2D 00            mov qword ptr [rip + 0x2dd1c1], rax
00C1DA87  48 8D 05 DA D1 2D 00            lea rax, [rip + 0x2dd1da]
00C1DA8E  48 89 05 DB D1 2D 00            mov qword ptr [rip + 0x2dd1db], rax
00C1DA95  48 89 05 CC D1 2D 00            mov qword ptr [rip + 0x2dd1cc], rax
00C1DA9C  4C 89 2D FD D1 2D 00            mov qword ptr [rip + 0x2dd1fd], r13
00C1DAA3  4C 89 2D E6 D1 2D 00            mov qword ptr [rip + 0x2dd1e6], r13
00C1DAAA  66 44 89 25 8E D1 2D 00         mov word ptr [rip + 0x2dd18e], r12w
00C1DAB2  C6 05 89 D1 2D 00 06            mov byte ptr [rip + 0x2dd189], 6
00C1DAB9  44 89 2D 84 D1 2D 00            mov dword ptr [rip + 0x2dd184], r13d
00C1DAC0  66 44 89 25 98 D1 2D 00         mov word ptr [rip + 0x2dd198], r12w
00C1DAC8  C6 05 93 D1 2D 00 06            mov byte ptr [rip + 0x2dd193], 6
00C1DACF  44 89 25 8E D1 2D 00            mov dword ptr [rip + 0x2dd18e], r12d
00C1DAD6  E8 7D 48 05 00                  call 0x140c72358
00C1DADB  84 C0                           test al, al
00C1DADD  74 50                           je 0x140c1db2f
00C1DADF  E8 14 CB B6 FF                  call 0x14078a5f8
00C1DAE4  45 33 C9                        xor r9d, r9d
00C1DAE7  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1DAEC  45 33 C0                        xor r8d, r8d
00C1DAEF  48 8D 0D B2 24 21 00            lea rcx, [rip + 0x2124b2]
00C1DAF6  33 D2                           xor edx, edx
00C1DAF8  E8 B3 0B 5F FF                  call 0x14020e6b0
00C1DAFD  8A 44 24 58                     mov al, byte ptr [rsp + 0x58]
00C1DB01  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
00C1DB05  48 33 CC                        xor rcx, rsp
00C1DB08  E8 33 EB A8 FF                  call 0x1406ac640
00C1DB0D  4C 8D 9C 24 70 01 00 00         lea r11, [rsp + 0x170]
00C1DB15  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00C1DB19  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00C1DB1D  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00C1DB21  49 8B E3                        mov rsp, r11
00C1DB24  41 5F                           pop r15
00C1DB26  41 5E                           pop r14
00C1DB28  41 5D                           pop r13
00C1DB2A  41 5C                           pop r12
00C1DB2C  5D                              pop rbp
00C1DB2D  C3                              ret
00C1DB2E  CC                              int3
00C1DB2F  B9 A0 00 00 00                  mov ecx, 0xa0
00C1DB34  E8 07 FB 8D FF                  call 0x1404fd640
00C1DB39  CC                              int3
00C1DB3A  B9 61 00 00 00                  mov ecx, 0x61
00C1DB3F  E8 FC FA 8D FF                  call 0x1404fd640
00C1DB44  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Phase1InitializationDiscard(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m12C;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int8 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int8 v_stack_m157;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (368);
    result = (*(unsigned __int64 *)(v_rip + 2023405)) ^ (v_rsp);
    v_stack_m30 = result;
    v_r14 = 0;
    v_stack_m150 = 0;
    result = 0;
    v_stack_m120 = 0;
    a2 = 0;
    v_stack_m100 = 0;
    v_stack_m138 = 0;
    v_stack_m148 = 0;
    v_stack_mE8 = v_xmm0;
    v_stack_m140 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_m118 = 0;
    v_stack_m130 = 0;
    v_stack_m12C = 0;
    v_stack_mD8 = v_xmm0;
    v_stack_mC4 = 0;
    result = memset(v_stack_mC8, a2, v_r14 + 116, a4);
    result = PsGetCurrentServerSiloGlobals(v_stack_mC8, a2, v_r14 + 116, a4);
    result = ExAllocatePool2(v_r14 + 64, 512, (unsigned int)(0x74696E49ULL), a4);
    if (result == 0) {
        a1 = result + 49;
        result = KeBugCheck(a1, 512, (unsigned int)(0x74696E49ULL), a4);
    }
    v_stack_m157 = 0;
    *(unsigned int *)(v_rip + 3832230) = 1;
    result = KeSetPriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 1 + 30, (unsigned int)(0x74696E49ULL), a4);
    if (*(unsigned __int64 *)(a1 + 216) == 0) goto loc_00C1CA46;
    result = strupr(*(unsigned __int64 *)(a1 + 216), 1 + 30, (unsigned int)(0x74696E49ULL), a4);
    if (result == 0) goto loc_00C1CA51;
    result = strstr(result, v_rip + 378709, (unsigned int)(0x74696E49ULL), a4);
    if (result == 0) goto loc_00C1C85B;
    result = strstr(result, v_rip + 377745, (unsigned int)(0x74696E49ULL), a4);
    if (result != 0) {
        a1 = result + 1;
        result = atol(a1, v_rip + 377745, (unsigned int)(0x74696E49ULL), a4);
        *(unsigned int *)(v_rip + 3842917) = (unsigned int)(result);
    }
    result = strstr(result, v_rip + 378686, (unsigned int)(0x74696E49ULL), a4);
    v_rbx = result;
    if (result != 0) {
        a2 = v_rip + 377687;
        a1 = result;
        result = strstr(a1, a2, (unsigned int)(0x74696E49ULL), a4);
        v_rbx = result;
    }
    if (v_rbx == 0) goto loc_00C1C8D9;
    if ((*(unsigned int *)(v_rip + 3842816)) >= 64) goto loc_00C1C8D9;
    v_rbx = (v_rbx) + (1);
    result = atol(v_rbx, a2, (unsigned int)(0x74696E49ULL), a4);
    *(unsigned __int16 *)(v_rip - 12699818 + (unsigned int)(*(unsigned int *)(v_rip + 3842797)) * 2 + 16545424) = (unsigned __int16)(result);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3842797))) + (1));
    *(unsigned int *)(v_rip + 3842770) = a2;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx))) == 44) goto loc_00C1C8D5;
loc_00C1C8C2:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx))) == 32) goto loc_00C1C8D9;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rbx)) == 0) goto loc_00C1C8D9;
    v_rbx = (v_rbx) + (1);
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx))) != 44) goto loc_00C1C8C2;
    goto loc_00C1C884;
loc_00C1C8D5:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rbx)) != 0) goto loc_00C1C884;
loc_00C1C8D9:
    result = strstr(result, v_rip + 378592, v_rip - 12699818, a4);
    v_rbx = result;
    if (result != 0) {
        a2 = v_rip + 377561;
        a1 = result;
        result = strstr(a1, a2, v_rip - 12699818, a4);
        v_rbx = result;
        *(unsigned __int8 *)(v_rip + 3842462) = 1;
        *(unsigned int *)(v_rip + 3842688) = 0;
        *(unsigned int *)(v_rip + 3842729) = 0;
    }
    if (v_rbx == 0) goto loc_00C1CA51;
    v_rbx = (v_rbx) + (1);
    v_stack_m128 = 0;
    result = strtoul(v_rbx, v_stack_m128, 10, a4);
    if (v_rbx == v_stack_m128) goto loc_00C1C970;
    if ((*(unsigned __int8 *)(v_stack_m128)) != 95) goto loc_00C1C970;
    result = strtoul(v_stack_m128 + 1, v_stack_m128, 10, a4);
    result = 0;
    goto loc_00C1C975;
loc_00C1C970:
    result = 0;
loc_00C1C975:
    if ((v_stack_m128 + 1) == v_stack_m128) goto loc_00C1CA09;
    if ((*(unsigned __int8 *)(v_stack_m128)) != 61) goto loc_00C1CA09;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) >= 64) goto loc_00C1CA09;
    v_r14 = ((unsigned int)((unsigned int)(result))) + ((unsigned int)((unsigned int)(result)));
    if ((*(unsigned __int64 *)(v_rip - 12700059 + v_r14 * 8 + 16567368)) != 0) goto loc_00C1C9DA;
    result = ExAllocatePool2(64, 256, (unsigned int)(0x800ULL), a4);
    if (result == 0) goto loc_00C1CA3B;
    *(unsigned __int64 *)(v_rip - 12700102 + v_r14 * 8 + 16567360) = 0x800ULL;
    *(unsigned __int64 *)(v_rip - 12700102 + v_r14 * 8 + 16567368) = result;
loc_00C1C9DA:
    if (0 < 32) {
        a3 = 16;
        a2 = v_stack_m128;
        a1 = v_stack_m128 + 1;
        result = strtoui64(a1, a2, a3, a4);
        a1 = v_rip - 12700154;
        a2 = 0;
        a1 = *(unsigned __int64 *)(a1 + v_r14 * 8 + 16567368);
        *(unsigned __int64 *)(a1 + a2 * 8) = result;
    }
    v_r14 = 0;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_m128 + 1))) == 44) goto loc_00C1CA2C;
loc_00C1CA16:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_m128 + 1))) == 32) goto loc_00C1CA51;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m128 + 1)) == 0) goto loc_00C1CA4B;
    v_rbx = (v_stack_m128 + 1) + (v_r14 + 1);
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx))) != 44) goto loc_00C1CA16;
    goto loc_00C1C917;
loc_00C1CA2C:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rbx)) == 0) goto loc_00C1CA4B;
    goto loc_00C1C917;
loc_00C1CA3B:
    result = KeBugCheck(49, a2, a3, a4);
loc_00C1CA46:
    goto loc_00C1CA51;
loc_00C1CA4B:
loc_00C1CA51:
    *(unsigned __int16 *)(v_rip + 2399893) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3166360) + 4) = 0;
    result = KiPerformGroupConfiguration(a1, a2, a3, a4);
    result = KiCommitGroupSubNodeAssignments(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3166329) + 6), a2, a3, a4);
    result = HalInitSystem((unsigned int)(*(unsigned int *)(v_rip + 3831578)), a1, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C1DB3A;
    result = KeInitializeClock((unsigned int)(*(unsigned int *)(v_rip + 3831552)), a1, a3, a4);
    if (0 == 0) goto loc_00C1CAC6;
    result = strstr(0, v_rip + 378151, a3, a4);
    if (result != 0) goto loc_00C1CB42;
loc_00C1CAC6:
    *(unsigned __int8 *)(v_rip + 2397048) = 0;
    if ((*(unsigned __int8 *)(v_rip + 2397155)) == 0) goto loc_00C1CB17;
    if ((*(unsigned __int8 *)(v_rip + 2397149)) == 0) goto loc_00C1CAF2;
    result = BgDisplayProgressIndicator(1, v_rip + 378151, a3, a4);
    if (!(sign_flag)) {
        *(unsigned __int8 *)(v_rip + 2397126) = 1;
    }
    if ((*(unsigned __int8 *)(v_rip + 2397111)) == 0) goto loc_00C1CB17;
    if ((*(unsigned __int8 *)(v_rip + 2397112)) == 0) goto loc_00C1CB17;
    result = BgDisplayBackgroundUpdate(1, v_rip + 378151, a3, a4);
    if (!(sign_flag)) {
        *(unsigned __int8 *)(v_rip + 2397034) = 1;
    }
    *(unsigned __int64 *)(v_rip + 2396962) = v_rip - 7213278;
    result = InbvDriverInitialize(1, a1, 7, a4);
    a1 = 0;
    result = DisplayBootBitmap(a1, a1, 7, a4);
    if (0 == 0) goto loc_00C1CB80;
loc_00C1CB42:
    result = strstr(0, v_rip + 378023, 7, a4);
    if (result == 0) goto loc_00C1CB80;
    *(unsigned __int8 *)(v_rip + 3831268) = 1;
    result = strstr(0, v_rip + 378019, 7, a4);
    if (result == 0) goto loc_00C1CB79;
    goto loc_00C1CB80;
loc_00C1CB79:
loc_00C1CB80:
    a3 = 0;
    v_stack_m178 = v_stack_m138;
    result = RtlFindMessage(v_rip - 12700570, a3 + 11, a3, (unsigned int)(0x4000007EULL));
    v_stack_m108 = result;
    v_stack_m110 = 256;
    if ((*(unsigned __int16 *)(v_rip + 3831301)) == 0) goto loc_00C1CC1A;
    v_stack_m168 = v_rip + 3831274;
    v_stack_m170 = v_rip + 377909;
    v_stack_m178 = 0;
    result = RtlStringCbPrintfExA(result, 255, v_stack_m108, v_stack_m110);
    a1 = 0;
    if (sign_flag) {
        a4 = 0;
        v_stack_m178 = 0;
        a2 = (int)((unsigned int)(result));
        a1 = a4 + 50;
        a3 = a4 + 7;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    goto loc_00C1CC26;
loc_00C1CC1A:
    a1 = 0;
    v_stack_m110 = 255;
loc_00C1CC26:
    *(unsigned __int8 *)(v_stack_m108) = 0;
    v_stack_m178 = 0;
    v_rbx = (v_stack_m108) + 1;
    v_stack_m108 = v_rbx;
    result = RtlStringCbPrintfA(v_stack_m48, 10 + 14, v_rip + 376833, 10);
    v_r10 = 0;
    if (sign_flag) {
        a2 = (int)((unsigned int)(result));
        a1 = v_r10 + 50;
        a4 = v_r10 + 1;
        v_stack_m178 = 0;
        a3 = v_r10 + 7;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (sign_flag) goto loc_00C1CCBF;
    a3 = (v_stack_m138) + (4);
    v_stack_m170 = result;
    v_stack_m178 = (unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip + 2022095))));
    result = RtlStringCbPrintfA(v_rbx, 255, a3, v_stack_m48);
    a1 = 0;
    if (!sign_flag) goto loc_00C1CCED;
    v_stack_m178 = 0;
    result = KeBugCheckEx(50, (int)((unsigned int)(result)), 50 - 43, 50 - 48);
loc_00C1CCBF:
    result = RtlStringCbCopyA(v_rbx, (int)((unsigned int)(result)), v_rip + 377690, 50 - 48);
    if (sign_flag) {
        a1 = 50;
        a2 = (int)((unsigned int)(result));
        v_stack_m178 = 0;
        a4 = a1 - 47;
        a3 = a1 - 43;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = InbvDisplayString(v_rbx, a2, a3, a4);
loc_00C1CD0F:
    *(unsigned __int64 *)(result + 256) = v_xmm0;
    *(unsigned __int64 *)(result + 256 + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 256 + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 256 + 48) = v_xmm1;
    *(unsigned __int64 *)(result + 256 + 64) = v_xmm0;
    *(unsigned __int64 *)(result + 256 + 80) = v_xmm1;
    *(unsigned __int64 *)(result + 256 + 96) = v_xmm0;
    result = (result + 256) + (2 + 126);
    a1 = (result) + (2 + 126);
    *(unsigned __int64 *)(result - 16) = v_xmm1;
    a2 = (2) - (1);
    if (condition_is_not_equal) goto loc_00C1CD0F;
    a1 = 0;
    result = PoInitSystem(a1, a1, a3, a4);
    v_rbx = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00C1DB2F;
    if ((*(unsigned int *)(v_rip + 2406397)) != 0) goto loc_00C1CDC5;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 436));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 436)))) == -1) {
        result = *(unsigned int *)(v_rip + 3920000);
        *(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 436) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 3919986);
        v_stack_m157 = 1;
    }
    result = (unsigned int)((result) * ((unsigned int)(result)));
    result = (result) * ((int)((unsigned int)(result)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 440) = result;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3834446) + 604) = 0;
    result = ExpWriteTimeZoneBias(*(unsigned __int64 *)(result + 1224) + 440, (int)((unsigned int)(result)), a3, a4);
loc_00C1CDC5:
    result = GetBootSystemTime(*(unsigned __int64 *)(a1 + 240), v_stack_m150, a3, a4);
    if (0 == 0) goto loc_00C1CE30;
    result = strstr(0, v_rip + 377438, a3, a4);
    if (result == 0) goto loc_00C1CE30;
    result = strstr(result, v_rip + 376282, a3, a4);
    if (result != 0) {
        a1 = result + 1;
        result = atol(a1, v_rip + 376282, a3, a4);
        a2 = v_stack_mF8;
        v_rbx = (unsigned int)(result);
        a1 = v_stack_m150;
        result = RtlpTimeToTimeFields(a1, a2, a3, a4);
        a2 = v_stack_m150;
        v_stack_mF8 = (unsigned __int16)(v_rbx);
        a1 = v_stack_mF8;
        result = RtlpTimeFieldsToTime(a1, a2, a3, a4);
        v_rbx = 0;
    }
    if ((*(unsigned int *)(v_rip + 2406202)) != 0) goto loc_00C1CE52;
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    result = (v_stack_m150) - (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 440));
    goto loc_00C1CE57;
loc_00C1CE52:
loc_00C1CE57:
    v_stack_m120 = v_stack_m150;
    result = KeSetSystemTime(v_stack_m150, v_stack_m100, 4, a4);
    result = PsGetCurrentServerSiloGlobals(v_stack_m150, v_stack_m100, 4, a4);
    a3 = 0;
    v_stack_m168 = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 2039050));
    v_stack_m178 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 436)));
    result = PoNotifySystemTimeSet(v_stack_m150, v_stack_m100, a3, v_stack_m120);
    result = RtlInitUnicodeString(v_stack_mD8, v_rip + 377251, a3, v_stack_m120);
    v_stack_m178 = v_stack_m130;
    result = ZwQueryLicenseValue(v_stack_mD8, v_stack_m12C, v_rip + 3841440, 4);
    if (sign_flag) goto loc_00C1CEED;
    if (v_stack_m130 != 4) goto loc_00C1CEED;
    if (v_stack_m12C != 4) {
        *(unsigned int *)(v_rip + 3841393) = 1;
    }
    if (0 == 0) goto loc_00C1D039;
    result = strstr(0, v_rip + 377225, v_rip + 3841440, 4);
    if (result == 0) goto loc_00C1CF37;
    result = strstr(result, v_rip + 375989, v_rip + 3841440, 4);
    if (result != 0) {
        a1 = result + 1;
        result = atol(a1, v_rip + 375989, v_rip + 3841440, 4);
        *(unsigned int *)(v_rip + 3841469) = (unsigned int)(result);
    }
    result = strstr(0, v_rip + 377186, v_rip + 3841440, 4);
    if (result == 0) goto loc_00C1CF6E;
    result = strstr(result, v_rip + 375934, v_rip + 3841440, 4);
    if (result != 0) {
        a1 = result + 1;
        result = atol(a1, v_rip + 375934, v_rip + 3841440, 4);
        *(unsigned int *)(v_rip + 3841318) = (unsigned int)(result);
    }
    result = strstr(0, v_rip + 377147, v_rip + 3841440, 4);
    if (result == 0) goto loc_00C1CFA5;
    result = strstr(result, v_rip + 375879, v_rip + 3841440, 4);
    if (result != 0) {
        a1 = result + 1;
        result = atol(a1, v_rip + 375879, v_rip + 3841440, 4);
        *(unsigned int *)(v_rip + 3841455) = (unsigned int)(result);
    }
    if ((*(unsigned __int8 *)(v_rip + 3840764)) != 0) goto loc_00C1D01B;
    result = strstr(0, v_rip + 377116, v_rip + 3841440, 4);
    if (result == 0) goto loc_00C1CFE4;
    result = strstr(result, v_rip + 375816, v_rip + 3841440, 4);
    if (result != 0) {
        a1 = result + 1;
        result = atol(a1, v_rip + 375816, v_rip + 3841440, 4);
        *(unsigned int *)(v_rip + 3841196) = (unsigned int)(result);
    }
    result = strstr(0, v_rip + 377093, v_rip + 3841440, 4);
    if (result == 0) goto loc_00C1D01B;
    result = strstr(result, v_rip + 375761, v_rip + 3841440, 4);
    if (result != 0) {
        a1 = result + 1;
        result = atol(a1, v_rip + 375761, v_rip + 3841440, 4);
        *(unsigned int *)(v_rip + 3841137) = (unsigned int)(result);
    }
    result = strstr(0, v_rip + 377070, v_rip + 3841440, 4);
    if (result != 0) {
        *(unsigned int *)(v_rip + 3841571) = 1;
    }
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, v_rip + 377070, v_rip + 3841440, 4);
    *(unsigned __int64 *)(v_rip + 4110209) = result;
    result = KeStartAllProcessors(a1, v_rip + 377070, v_rip + 3841440, 4);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, v_rip + 377070, v_rip + 3841440, 4);
    *(unsigned __int64 *)(v_rip + 4110198) = result;
    result = EtwTimeProfileReset(a1, v_rip + 377070, v_rip + 3841440, 4);
    a2 = 0;
    result = KeSetAffinityProcess(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, v_rip + 3842225, 4);
    result = MakeGdtReadOnly(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, v_rip + 3842225, 4);
    a3 = 0;
    v_stack_m178 = v_stack_m148;
    result = RtlFindMessage(v_rip - 12701852, a3 + 11, a3, (unsigned int)(0x40000089ULL));
    if (sign_flag) goto loc_00C1D0B4;
    v_rbx = (v_stack_m148) + (4);
    goto loc_00C1D0BB;
loc_00C1D0B4:
loc_00C1D0BB:
    result = HalAllProcessorsStarted(v_rip - 12701852, a3 + 11, a3, (unsigned int)(0x40000089ULL));
    if ((unsigned __int8)(result) == 0) goto loc_00C1DB3A;
    result = RtlInitAnsiString(v_stack_mE8, v_rip + 376933, a3, (unsigned int)(0x40000089ULL));
    result = v_stack_mE8;
    if (((unsigned __int16)(v_stack_mE8)) >= 2) {
        a1 = 0xFFFEULL;
        result = (unsigned __int16)((v_stack_mE8) + ((unsigned __int16)(a1)));
        v_stack_mE8 = (unsigned __int16)(result);
    }
    v_stack_m178 = v_stack_m138;
    a4 = (unsigned int)(0x40000088ULL) + 21;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3840400)))) <= 1) { a4 = (unsigned int)((unsigned int)(0x40000088ULL)); }
    a3 = 0;
    result = RtlFindMessage(v_rip - 12701972, a3 + 11, a3, a4);
    a3 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3840612)))) == 0) goto loc_00C1D141;
    a1 = (*(unsigned __int64 *)(v_rip + 3840612)) + (24);
loc_00C1D134:
    a2 = (0) + (*(unsigned __int64 *)(a1));
    v_rbx = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 3840612)))) - (1);
    if (condition_is_not_equal) goto loc_00C1D134;
loc_00C1D141:
    v_rbx = 0;
    if (sign_flag) goto loc_00C1D152;
    a3 = (v_stack_m138) + (4);
    goto loc_00C1D159;
loc_00C1D152:
loc_00C1D159:
    result = (a2 + 255) >> (8);
    v_stack_m170 = v_stack_mE8;
    v_stack_m178 = result;
    result = RtlStringCbPrintfA(result, 256, v_rip + 376807, (unsigned int)(*(unsigned int *)(v_rip + 3840288)));
    if (sign_flag) {
        a1 = 50;
        a2 = (int)((unsigned int)(result));
        v_stack_m178 = 0;
        a4 = a1 - 46;
        a3 = a1 - 43;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = InbvDisplayString(result, a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    result = ObInitSystem(1, a2, a3, a4);
    v_r13 = 0;
    if ((unsigned __int8)(result) == 0) {
        a1 = 1 + 97;
        result = KeBugCheck(a1, a2, a3, a4);
    }
    result = ExInitSystem(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a3 = 0;
        v_stack_m178 = 0;
        a4 = 1;
        a2 = 0xFFFFFFFFC0000001ULL;
        a1 = a3 + 50;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    result = HalReportResourceUsage(a1, a2, a3, a4);
    result = IoCreateObjectTypes(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a4 = 4;
        v_stack_m178 = 0;
        a3 = 0;
        a2 = 0xFFFFFFFFC0000001ULL;
        a1 = a4 + 46;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = KeInitSystem(1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a3 = 0;
        v_stack_m178 = 0;
        a4 = 2;
        a2 = 0xFFFFFFFFC0000001ULL;
        a1 = a3 + 50;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a2 = 0;
    result = KdInitSystem((unsigned int)(*(unsigned int *)(v_rip + 3829576)), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a4 = 3;
        v_stack_m178 = 0;
        a3 = 0;
        a2 = 0xFFFFFFFFC0000001ULL;
        a1 = a4 + 47;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = ext_ms_win_ntos_tm_l1_1_0_dll_TmInitSystem(v_rip + 3842202, v_rip + 3842321, v_rip + 3842208, v_rip + 3841127);
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result + (unsigned int)(0x80000000ULL) * 1))) != 0) goto loc_00C1D2D3;
    if (((unsigned int)(result)) != 0xC00000BBULL) {
        a2 = 0;
        v_stack_m178 = 0;
        a4 = 0;
        a3 = 0;
        a1 = a2 + 50;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = DbgkInitialize(a1, a2, a3, a4);
    if (sign_flag) {
        a4 = 0;
        a2 = (int)((unsigned int)(result));
        a3 = 0;
        v_stack_m178 = 0;
        a1 = a4 + 50;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a1 = 0;
    result = UcInitialize(a1, a2, a3, a4);
    result = BcdInitializeBcdSyncMutant(a1, a2, a3, a4);
    a1 = 0;
    result = VerifierInitSystem(a1, a2, a3, a4);
    result = SeInitSystem(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a1 = 99;
        result = KeBugCheck(a1, a2, a3, a4);
    }
    *(unsigned int *)(v_rip + 3840811) = 648;
    result = AlpcpInitSystem(a1, a2, a3, a4);
    if (sign_flag) {
        a1 = 106;
        result = KeBugCheck(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_rip + 3841060) = *(unsigned __int64 *)(v_rip + 3840216);
    result = PsInitSystem(1, a1, a3, a4);
    result = ExInitLicenseCallback(1, a1, a3, a4);
    result = CreateSystemRootLink(a1, a1, a3, a4);
    if (sign_flag) {
        a4 = 0;
        a2 = (int)((unsigned int)(result));
        a3 = 0;
        v_stack_m178 = 0;
        a1 = a4 + 100;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, a4);
    *(unsigned __int64 *)(v_rip + 4109405) = result;
    result = MmInitSystem(1, 0, a3, a4);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, 0, a3, a4);
    *(unsigned __int64 *)(v_rip + 4109390) = result;
    result = CcInitializeCacheManager(1, 0, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a1 = 102;
        result = KeBugCheck(a1, 0, a3, a4);
    }
    result = CmInitSystem1(a1, 0, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a1 = 103;
        result = KeBugCheck(a1, 0, a3, a4);
    }
    result = PsInitializeBootCpuPartitions(a1, 0, a3, a4);
    result = ExInitializeLeapSecondData(a1, 0, a3, a4);
    if (sign_flag) {
        a4 = 0;
        a2 = (int)((unsigned int)(result));
        v_stack_m178 = 0;
        a1 = a4 + 50;
        a3 = a4 + 12;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_stack_m158 = 0;
    result = ExIsMultiSessionSku(v_stack_m158, a2, a3, a4);
    if (sign_flag) goto loc_00C1D41D;
    if (v_stack_m158 != 0) {
        result = *(unsigned __int64 *)(v_rip + 3832819);
    }
    if ((*(unsigned int *)(v_rip + 3829100)) != 0) {
        result = *(unsigned __int64 *)(v_rip + 3832795);
    }
    if ((*(unsigned int *)(v_rip + 2959152)) != 0) {
        result = *(unsigned __int64 *)(v_rip + 3832771);
    }
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, a4);
    *(unsigned __int64 *)(v_rip + 4109144) = result;
    a2 = 0;
    result = memset(v_stack_mC8, a2, 120, a4);
    v_stack_mC0 = v_rip - 4342876;
    v_stack_mB8 = v_rip - 4342695;
    v_stack_mB0 = v_rip - 9127938;
    v_stack_mA8 = v_rip - 618013;
    v_stack_mA0 = v_rip - 345240;
    v_stack_m98 = v_rip - 8406595;
    v_stack_m90 = v_rip - 4448510;
    v_stack_m88 = v_rip - 9324537;
    v_stack_m80 = v_rip - 8285876;
    v_stack_mC8 = 120;
    if ((*(unsigned __int8 *)(v_rip + 3839503)) != 0) goto loc_00C1D4E2;
    goto loc_00C1D505;
loc_00C1D4E2:
    *(unsigned __int64 *)(v_rip + 4108864) = v_rip - 6871385;
    *(unsigned __int64 *)(v_rip + 4108851) = v_rip + 53010;
loc_00C1D505:
    result = BgGetDisplayContext(v_stack_mC8, a2, 120, v_rip + 4108857);
    result = ext_ms_win_ntos_ksr_l1_1_5_dll_KsrInitSystem(0, v_stack_mC8, result, v_rip + 4108857);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, v_stack_mC8, result, v_rip + 4108857);
    *(unsigned __int64 *)(v_rip + 4108943) = result;
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)((int)((unsigned int)(result)) + (unsigned int)(0x80000000ULL) * 1))) != 0) goto loc_00C1D560;
    result = (unsigned int)(0x80000000ULL);
    if (((unsigned int)((int)((unsigned int)(result)))) != 0xC00000BBULL) {
        a4 = 1;
        v_stack_m178 = 0;
        a2 = (int)((unsigned int)(result));
        a3 = 0;
        a1 = a4 + 49;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a1 = 0;
    *(unsigned __int64 *)(v_rip + 3021420) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 3021439) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 3021416) = v_xmm1;
    result = EmInitSystem(a1, a1, a3, a4);
    if (sign_flag) {
        a4 = 0;
        a2 = (int)((unsigned int)(result));
        v_stack_m178 = 0;
        a1 = a4 + 50;
        a3 = a4 + 8;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = MfgInitSystem(a1, a2, a3, a4);
    if (sign_flag) {
        a4 = 0;
        a2 = (int)((unsigned int)(result));
        v_stack_m178 = 0;
        a1 = a4 + 50;
        a3 = a4 + 9;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = PfInitializeSuperfetch(a1, a2, a3, a4);
    a1 = 0;
    result = SmInitSystem(a1, a2, a3, a4);
    if (sign_flag) {
        a4 = 0;
        a2 = (int)((unsigned int)(result));
        v_stack_m178 = 0;
        a1 = a4 + 50;
        a3 = a4 + 11;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = VmInitSystem(1, a2, a3, a4);
    if (sign_flag) {
        a4 = 0;
        a2 = (int)((unsigned int)(result));
        v_stack_m178 = 0;
        a1 = a4 + 50;
        a3 = a4 + 10;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 240) + 2656)) & (2)) == 0) goto loc_00C1D643;
    result = strstr(0, v_rip + 375610, a3, a4);
    if (result != 0) {
        v_stack_m168 = 0;
        a1 = v_rip - 12570007;
        v_stack_m170 = 0;
        a4 = 0;
        a3 = 0;
        v_stack_m178 = 0;
        a2 = 0;
        result = ZwUpdateWnfStateData(a1, a2, a3, a4);
    }
    if (((*(unsigned int *)(v_rip + 3839008)) & (0x2000000ULL)) != 0) {
        v_stack_m168 = 0;
        a1 = v_rip - 12569558;
        v_stack_m170 = 0;
        a4 = 0;
        a3 = 0;
        v_stack_m178 = 0;
        a2 = 0;
        result = ZwUpdateWnfStateData(a1, a2, a3, a4);
    }
    result = FsRtlSendModernAppTermination(v_stack_m118, 1, 1, a4);
    result = ExInitializeTimeRefresh(v_stack_m118, 1, 1, a4);
    result = ExAcquireTimeRefreshLockExclusive(v_stack_m118, 1, 1, a4);
    result = ExInitializeUtcTimeZoneBias(v_stack_m120, 1, 1, a4);
    a1 = 0;
    result = ExpRefreshTimeZoneInformation(a1, 1, 1, a4);
    result = ExReleaseTimeRefreshLockExclusive(a1, 1, 1, a4);
    if (v_stack_m157 == 0) goto loc_00C1D70B;
    result = PsGetCurrentServerSiloGlobals(a1, 1, 1, a4);
    a1 = (v_stack_m120) + (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 440));
    v_stack_m150 = a1;
    result = KeSetSystemTime(v_stack_m150, v_stack_m100, 4, a4);
    goto loc_00C1D71E;
loc_00C1D70B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 436)))) != (*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 436))) {
        a2 = 0;
        a1 = 0;
        result = ZwSetSystemTime(a1, a2, 4, a4);
    }
    result = FsRtlInitSystem(a1, a2, 4, a4);
    if ((unsigned __int8)(result) == 0) {
        a1 = 104;
        result = KeBugCheck(a1, a2, 4, a4);
    }
    v_stack_m160 = 0;
    v_stack_m168 = 0;
    v_stack_m170 = 0x63647A6CULL;
    a3 = 0;
    a2 = 0;
    v_stack_m178 = 88;
    result = ExInitializeNPagedLookasideListInternal(v_rip + 2140994, a2, a3, 512);
    a1 = 0;
    v_stack_m168 = 16;
    v_stack_m170 = 0x656C5252ULL;
    v_stack_m178 = 56;
    result = (unsigned int)((0) & (512));
    *(unsigned int *)(v_rip + 2401191) = (unsigned int)(result);
    a1 = (unsigned int)((a1) & ((unsigned int)((unsigned int)(0x100002ULL))));
    a2 = (((unsigned int)(a1)) == ((unsigned int)((unsigned int)(0x100002ULL)))) ? 1 : 0;
    result = (((unsigned int)(a1)) < ((unsigned int)((unsigned int)(0x100002ULL)))) ? 1 : 0;
    a4 = 0;
    a3 = 0;
    a2 = (unsigned int)((a2) & ((unsigned int)((unsigned __int8)(result))));
    *(unsigned int *)(v_rip + 2401143) = a2;
    a2 = 0;
    result = ExInitializePagedLookasideList(v_rip + 2140733, a2, a3, a4);
    result = HvlDebuggerSupportInitialize(a1, a2, a3, a4);
    a1 = 0;
    result = HalReportResourceUsage(a1, a2, a3, a4);
    result = kdcom_dll_KdInitialize(1, 0, v_rip + 3317242, a4);
    result = PpInitSystem(1, 0, v_rip + 3317242, a4);
    if ((unsigned __int8)(result) == 0) {
        a1 = 144;
        result = KeBugCheck(a1, 0, v_rip + 3317242, a4);
    }
    if (0 == 0) goto loc_00C1D93E;
    result = strstr(0, v_rip + 375140, v_rip + 3317242, a4);
    if (result == 0) goto loc_00C1D93E;
    result = strncmp(result + 9, v_rip + 375120, 7, a4);
    if ((unsigned int)(result) != 0) goto loc_00C1D855;
    *(unsigned int *)(v_rip + 3828081) = 1;
    goto loc_00C1D872;
loc_00C1D855:
    result = strncmp(result + 9, v_rip + 375105, 7, a4);
    if ((unsigned int)(result) != 0) goto loc_00C1D877;
    *(unsigned int *)(v_rip + 3828050) = 2;
loc_00C1D872:
    v_rbx = (result + 9) + (7);
    goto loc_00C1D8A8;
loc_00C1D877:
    result = strncmp(v_rbx, v_rip + 375084, 8, a4);
    if ((unsigned int)(result) != 0) goto loc_00C1D8A1;
    v_rbx = (v_rbx) + (8);
    *(unsigned int *)(v_rip + 3828005) = 3;
    goto loc_00C1D8A8;
loc_00C1D8A1:
    *(unsigned int *)(v_rip + 3827996) = 0;
loc_00C1D8A8:
    result = 3;
    if ((*(unsigned __int8 *)(v_rbx)) != 0) {
        a3 = 16;
        a2 = v_rip + 375046;
        a1 = v_rbx;
        result = strncmp(a1, a2, a3, a4);
        a1 = v_stack_m140;
        a1 = (unsigned __int8)(a1);
        if ((unsigned int)(result) == 0) { a1 = 1; }
        v_stack_m140 = (unsigned int)(a1);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3827947))) == 0) goto loc_00C1D93E;
    v_stack_m148 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3827947))) - (1));
    if (condition_is_equal) goto loc_00C1D904;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00C1D8FC;
    if (((unsigned int)(result)) != 1) goto loc_00C1D90A;
    goto loc_00C1D90A;
loc_00C1D8FC:
    goto loc_00C1D90A;
loc_00C1D904:
loc_00C1D90A:
    a3 = 0;
    v_stack_m178 = v_stack_m148;
    result = RtlFindMessage(v_rip - 12704025, a3 + 11, a3, 168);
    if (sign_flag) goto loc_00C1D945;
    a1 = (v_stack_m148) + (4);
    result = InbvDisplayString(a1, a3 + 11, a3, 168);
    goto loc_00C1D945;
loc_00C1D93E:
loc_00C1D945:
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 132)) & (0x800ULL)) == 0) goto loc_00C1D994;
    a3 = 0;
    v_stack_m178 = v_stack_m138;
    result = RtlFindMessage(v_rip - 12704069, a3 + 11, a3, 183);
    if (!(sign_flag)) {
        a1 = v_stack_m138;
        a1 = (a1) + (4);
        result = InbvDisplayString(a1, a3 + 11, a3, 183);
    }
    result = IopInitializeBootLogging(a1, result + 256, a3, 183);
loc_00C1D994:
    result = ExpWatchProductTypeInitialization(a1, result + 256, a3, 183);
    a1 = 0;
    result = BootApplicationPersistentDataProcess(a1, result + 256, a3, 183);
    result = ext_ms_win_ntos_ucode_l1_1_0_dll_ExpMicrocodeInitialization(2, result + 256, a3, 183);
    if ((*(unsigned int *)(v_rip + 3916111)) >= = ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3838245))))) {
        *(unsigned int *)(v_rip + 3916103) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3838245)));
    }
    v_stack_m148 = 0;
    *(unsigned int *)(v_rip + 3000102) = 0;
    result = ExpGetOriginalImageVersionRegistryValue(v_stack_m148, result + 256, a3, 183);
    if (!(sign_flag)) {
        result = v_stack_m148;
        *(unsigned int *)(v_rip + 3000083) = (unsigned int)(result);
    }
    result = ExpComputeCyclesPerYield(v_stack_m148, result + 256, a3, 183);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3831296) + 726) = (unsigned __int16)(result);
    if ((*(unsigned __int8 *)(v_rip + 3827527)) != 0) {
        result = CreateMiniNtBootKey(*(unsigned __int64 *)(v_rip + 3831296), result + 256, a3, 183);
    }
    result = symcryptk_dll_SymCryptEntropyAccumulatorGlobalInitFromRegistry(*(unsigned __int64 *)(v_rip + 3831296), result + 256, a3, 183);
    result = SeCodeIntegrityInitializePolicy(0, result + 256, a3, 183);
    if (sign_flag) {
        a4 = 0;
        a2 = (int)((unsigned int)(result));
        a3 = 0x69436553ULL;
        v_stack_m178 = 0;
        a1 = a4 + 50;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    *(unsigned int *)(v_rip + 2019329) = 0;
    *(unsigned __int64 *)(v_rip + 3002922) = v_rip + 3002928;
    *(unsigned __int64 *)(v_rip + 3002904) = v_rip + 3002928;
    *(unsigned int *)(v_rip + 3002911) = 0;
    *(unsigned __int64 *)(v_rip + 3002832) = v_rip + 3002838;
    *(unsigned __int64 *)(v_rip + 3002817) = v_rip + 3002838;
    *(unsigned __int64 *)(v_rip + 3002843) = v_rip + 3002842;
    *(unsigned __int64 *)(v_rip + 3002828) = v_rip + 3002842;
    *(unsigned __int64 *)(v_rip + 3002877) = 0;
    *(unsigned __int64 *)(v_rip + 3002854) = 0;
    *(unsigned __int16 *)(v_rip + 3002766) = 1;
    *(unsigned __int8 *)(v_rip + 3002761) = 6;
    *(unsigned int *)(v_rip + 3002756) = 0;
    *(unsigned __int16 *)(v_rip + 3002776) = 1;
    *(unsigned __int8 *)(v_rip + 3002771) = 6;
    *(unsigned int *)(v_rip + 3002766) = 1;
    result = PoInitSystem(1, a1, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C1DB2F;
    result = RtlInitFunctionalityCache(1, a1, a3, a4);
    a4 = 0;
    v_stack_m178 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_rip + 2172082, a2, a3, a4);
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_00C1DB2F:
    result = KeBugCheck(160, a2, a3, a4);
loc_00C1DB3A:
    result = KeBugCheck(97, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Phase1InitializationDiscard(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m12C;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint8_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint8_t v_stack_m157;
    uint64_t v_stack_m158;
    uint32_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (368);
    result = (*(uint64_t *)(v_rip + 0x1EDFED)) ^ (local_rsp);
    v_stack_m30 = result;
    local_r14 = 0;
    v_stack_m150 = 0;
    result = 0;
    v_stack_m120 = 0;
    Arg2 = 0;
    v_stack_m100 = 0;
    v_stack_m138 = 0;
    v_stack_m148 = 0;
    v_stack_mE8 = v_xmm0;
    v_stack_m140 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_m118 = 0;
    v_stack_m130 = 0;
    v_stack_m12C = 0;
    v_stack_mD8 = v_xmm0;
    v_stack_mC4 = 0;
    result = memset(v_stack_mC8, Arg2, local_r14 + 116, a4);
    result = PsGetCurrentServerSiloGlobals(v_stack_mC8, Arg2, local_r14 + 116, a4);
    result = ExAllocatePool2(local_r14 + 64, 512, (uint32_t)(0x74696E49ULL), a4);
    if (result == 0) {
        Arg1 = result + 49;
        result = KeBugCheck(Arg1, 512, (uint32_t)(0x74696E49ULL), a4);
    }
    v_stack_m157 = 0;
    *(uint32_t *)(v_rip + 0x3A79A6) = 1;
    result = KeSetPriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), 1 + 30, (uint32_t)(0x74696E49ULL), a4);
    if (*(uint64_t *)(arg1 + 0xD8) == 0) goto loc_00C1CA46;
    result = strupr(*(uint64_t *)(arg1 + 0xD8), 1 + 30, (uint32_t)(0x74696E49ULL), a4);
    if (result == 0) goto loc_00C1CA51;
    result = strstr(result, v_rip + 378709, (uint32_t)(0x74696E49ULL), a4);
    if (result == 0) goto loc_00C1C85B;
    result = strstr(result, v_rip + 377745, (uint32_t)(0x74696E49ULL), a4);
    if (result != 0) {
        Arg1 = result + 1;
        result = atol(Arg1, v_rip + 377745, (uint32_t)(0x74696E49ULL), a4);
        *(uint32_t *)(v_rip + 0x3AA365) = (uint32_t)(result);
    }
    result = strstr(result, v_rip + 378686, (uint32_t)(0x74696E49ULL), a4);
    local_rbx = result;
    if (result != 0) {
        Arg2 = v_rip + 377687;
        Arg1 = result;
        result = strstr(Arg1, Arg2, (uint32_t)(0x74696E49ULL), a4);
        local_rbx = result;
    }
    if (local_rbx == 0) goto loc_00C1C8D9;
    if ((*(uint32_t *)(v_rip + 0x3AA300)) >= 64) goto loc_00C1C8D9;
    local_rbx = (local_rbx) + (1);
    result = atol(local_rbx, Arg2, (uint32_t)(0x74696E49ULL), a4);
    *(uint16_t *)(v_rip - 0xC1C8AA + (uint32_t)(*(uint32_t *)(v_rip + 0x3AA2ED)) * 2 + 0xFC7690) = (uint16_t)(result);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x3AA2ED))) + (1));
    *(uint32_t *)(v_rip + 0x3AA2D2) = Arg2;
    if (((uint8_t)(*(uint8_t *)(local_rbx))) == 44) goto loc_00C1C8D5;
loc_00C1C8C2:
    if (((uint8_t)(*(uint8_t *)(local_rbx))) == 32) goto loc_00C1C8D9;
    if ((uint8_t)(*(uint8_t *)(local_rbx)) == 0) goto loc_00C1C8D9;
    local_rbx = (local_rbx) + (1);
    if (((uint8_t)(*(uint8_t *)(local_rbx))) != 44) goto loc_00C1C8C2;
    goto loc_00C1C884;
loc_00C1C8D5:
    if ((uint8_t)(*(uint8_t *)(local_rbx)) != 0) goto loc_00C1C884;
loc_00C1C8D9:
    result = strstr(result, v_rip + 378592, v_rip - 12699818, a4);
    local_rbx = result;
    if (result != 0) {
        Arg2 = v_rip + 377561;
        Arg1 = result;
        result = strstr(Arg1, Arg2, v_rip - 12699818, a4);
        local_rbx = result;
        *(uint8_t *)(v_rip + 0x3AA19E) = 1;
        *(uint32_t *)(v_rip + 0x3AA280) = 0;
        *(uint32_t *)(v_rip + 0x3AA2A9) = 0;
    }
    if (local_rbx == 0) goto loc_00C1CA51;
    local_rbx = (local_rbx) + (1);
    v_stack_m128 = 0;
    result = strtoul(local_rbx, v_stack_m128, 10, a4);
    if (local_rbx == v_stack_m128) goto loc_00C1C970;
    if ((*(uint8_t *)(v_stack_m128)) != 95) goto loc_00C1C970;
    result = strtoul(v_stack_m128 + 1, v_stack_m128, 10, a4);
    result = 0;
    goto loc_00C1C975;
loc_00C1C970:
    result = 0;
loc_00C1C975:
    if ((v_stack_m128 + 1) == v_stack_m128) goto loc_00C1CA09;
    if ((*(uint8_t *)(v_stack_m128)) != 61) goto loc_00C1CA09;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) >= 64) goto loc_00C1CA09;
    local_r14 = ((uint32_t)((uint32_t)(result))) + ((uint32_t)((uint32_t)(result)));
    if ((*(uint64_t *)(v_rip - 0xC1C99B + local_r14 * 8 + 0xFCCC48)) != 0) goto loc_00C1C9DA;
    result = ExAllocatePool2(64, 256, (uint32_t)(0x800ULL), a4);
    if (result == 0) goto loc_00C1CA3B;
    *(uint64_t *)(v_rip - 0xC1C9C6 + local_r14 * 8 + 0xFCCC40) = 0x800ULL;
    *(uint64_t *)(v_rip - 0xC1C9C6 + local_r14 * 8 + 0xFCCC48) = result;
loc_00C1C9DA:
    if (0 < 32) {
        a3 = 16;
        Arg2 = v_stack_m128;
        Arg1 = v_stack_m128 + 1;
        result = strtoui64(Arg1, Arg2, a3, a4);
        Arg1 = v_rip - 12700154;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg1 + local_r14 * 8 + 0xFCCC48);
        *(uint64_t *)(arg1 + Arg2 * 8) = result;
    }
    local_r14 = 0;
    if (((uint8_t)(*(uint8_t *)(v_stack_m128 + 0x1))) == 44) goto loc_00C1CA2C;
loc_00C1CA16:
    if (((uint8_t)(*(uint8_t *)(v_stack_m128 + 0x1))) == 32) goto loc_00C1CA51;
    if ((uint8_t)(*(uint8_t *)(v_stack_m128 + 0x1)) == 0) goto loc_00C1CA4B;
    local_rbx = (v_stack_m128 + 1) + (local_r14 + 1);
    if (((uint8_t)(*(uint8_t *)(local_rbx))) != 44) goto loc_00C1CA16;
    goto loc_00C1C917;
loc_00C1CA2C:
    if ((uint8_t)(*(uint8_t *)(local_rbx)) == 0) goto loc_00C1CA4B;
    goto loc_00C1C917;
loc_00C1CA3B:
    result = KeBugCheck(49, Arg2, a3, a4);
loc_00C1CA46:
    goto loc_00C1CA51;
loc_00C1CA4B:
loc_00C1CA51:
    *(uint16_t *)(v_rip + 0x249E95) = 0;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x305098) + 0x4) = 0;
    result = KiPerformGroupConfiguration(Arg1, Arg2, a3, a4);
    result = KiCommitGroupSubNodeAssignments(*(uint16_t *)(*(uint64_t *)(v_rip + 0x305079) + 0x6), Arg2, a3, a4);
    result = HalInitSystem((uint32_t)(*(uint32_t *)(v_rip + 0x3A771A)), Arg1, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C1DB3A;
    result = KeInitializeClock((uint32_t)(*(uint32_t *)(v_rip + 0x3A7700)), Arg1, a3, a4);
    if (0 == 0) goto loc_00C1CAC6;
    result = strstr(0, v_rip + 378151, a3, a4);
    if (result != 0) goto loc_00C1CB42;
loc_00C1CAC6:
    *(uint8_t *)(v_rip + 0x249378) = 0;
    if ((*(uint8_t *)(v_rip + 0x2493E3)) == 0) goto loc_00C1CB17;
    if ((*(uint8_t *)(v_rip + 0x2493DD)) == 0) goto loc_00C1CAF2;
    result = BgDisplayProgressIndicator(1, v_rip + 378151, a3, a4);
    if (!(sign_flag)) {
        *(uint8_t *)(v_rip + 0x2493C6) = 1;
    }
    if ((*(uint8_t *)(v_rip + 0x2493B7)) == 0) goto loc_00C1CB17;
    if ((*(uint8_t *)(v_rip + 0x2493B8)) == 0) goto loc_00C1CB17;
    result = BgDisplayBackgroundUpdate(1, v_rip + 378151, a3, a4);
    if (!(sign_flag)) {
        *(uint8_t *)(v_rip + 0x24936A) = 1;
    }
    *(uint64_t *)(v_rip + 0x249322) = v_rip - 7213278;
    result = InbvDriverInitialize(1, Arg1, 7, a4);
    Arg1 = 0;
    result = DisplayBootBitmap(Arg1, Arg1, 7, a4);
    if (0 == 0) goto loc_00C1CB80;
loc_00C1CB42:
    result = strstr(0, v_rip + 378023, 7, a4);
    if (result == 0) goto loc_00C1CB80;
    *(uint8_t *)(v_rip + 0x3A75E4) = 1;
    result = strstr(0, v_rip + 378019, 7, a4);
    if (result == 0) goto loc_00C1CB79;
    goto loc_00C1CB80;
loc_00C1CB79:
loc_00C1CB80:
    a3 = 0;
    v_stack_m178 = v_stack_m138;
    result = RtlFindMessage(v_rip - 12700570, a3 + 11, a3, (uint32_t)(0x4000007EULL));
    v_stack_m108 = result;
    v_stack_m110 = 256;
    if ((*(uint16_t *)(v_rip + 0x3A7605)) == 0) goto loc_00C1CC1A;
    v_stack_m168 = v_rip + 3831274;
    v_stack_m170 = v_rip + 377909;
    v_stack_m178 = 0;
    result = RtlStringCbPrintfExA(result, 255, v_stack_m108, v_stack_m110);
    Arg1 = 0;
    if (sign_flag) {
        a4 = 0;
        v_stack_m178 = 0;
        Arg2 = (int32_t)((uint32_t)(result));
        Arg1 = a4 + 50;
        a3 = a4 + 7;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    goto loc_00C1CC26;
loc_00C1CC1A:
    Arg1 = 0;
    v_stack_m110 = 255;
loc_00C1CC26:
    *(uint8_t *)(v_stack_m108) = 0;
    v_stack_m178 = 0;
    local_rbx = (v_stack_m108) + 1;
    v_stack_m108 = local_rbx;
    result = RtlStringCbPrintfA(v_stack_m48, 10 + 14, v_rip + 376833, 10);
    local_r10 = 0;
    if (sign_flag) {
        Arg2 = (int32_t)((uint32_t)(result));
        Arg1 = local_r10 + 50;
        a4 = local_r10 + 1;
        v_stack_m178 = 0;
        a3 = local_r10 + 7;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    if (sign_flag) goto loc_00C1CCBF;
    a3 = (v_stack_m138) + (4);
    v_stack_m170 = result;
    v_stack_m178 = (uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1EDACF))));
    result = RtlStringCbPrintfA(local_rbx, 255, a3, v_stack_m48);
    Arg1 = 0;
    if (!sign_flag) goto loc_00C1CCED;
    v_stack_m178 = 0;
    result = KeBugCheckEx(50, (int32_t)((uint32_t)(result)), 50 - 43, 50 - 48);
loc_00C1CCBF:
    result = RtlStringCbCopyA(local_rbx, (int32_t)((uint32_t)(result)), v_rip + 377690, 50 - 48);
    if (sign_flag) {
        Arg1 = 50;
        Arg2 = (int32_t)((uint32_t)(result));
        v_stack_m178 = 0;
        a4 = Arg1 - 47;
        a3 = Arg1 - 43;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = InbvDisplayString(local_rbx, Arg2, a3, a4);
loc_00C1CD0F:
    *(uint64_t *)(result + 0x100) = v_xmm0;
    *(uint64_t *)(result + 0x100 + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x100 + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x100 + 0x30) = v_xmm1;
    *(uint64_t *)(result + 0x100 + 0x40) = v_xmm0;
    *(uint64_t *)(result + 0x100 + 0x50) = v_xmm1;
    *(uint64_t *)(result + 0x100 + 0x60) = v_xmm0;
    result = (result + 256) + (2 + 126);
    Arg1 = (result) + (2 + 126);
    *(uint64_t *)(result - 0x10) = v_xmm1;
    Arg2 = (2) - (1);
    if (condition_is_not_equal) goto loc_00C1CD0F;
    Arg1 = 0;
    result = PoInitSystem(Arg1, Arg1, a3, a4);
    local_rbx = 0;
    if ((uint8_t)(result) == 0) goto loc_00C1DB2F;
    if ((*(uint32_t *)(v_rip + 0x24B7FD)) != 0) goto loc_00C1CDC5;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B4));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B4)))) == -1) {
        result = *(uint32_t *)(v_rip + 0x3BD080);
        *(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B4) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0x3BD072);
        v_stack_m157 = 1;
    }
    result = (uint32_t)((result) * ((uint32_t)(result)));
    result = (result) * ((int32_t)((uint32_t)(result)));
    *(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B8) = result;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x3A824E) + 0x25C) = 0;
    result = ExpWriteTimeZoneBias(*(uint64_t *)(result + 0x4C8) + 440, (int32_t)((uint32_t)(result)), a3, a4);
loc_00C1CDC5:
    result = GetBootSystemTime(*(uint64_t *)(arg1 + 0xF0), v_stack_m150, a3, a4);
    if (0 == 0) goto loc_00C1CE30;
    result = strstr(0, v_rip + 377438, a3, a4);
    if (result == 0) goto loc_00C1CE30;
    result = strstr(result, v_rip + 376282, a3, a4);
    if (result != 0) {
        Arg1 = result + 1;
        result = atol(Arg1, v_rip + 376282, a3, a4);
        Arg2 = v_stack_mF8;
        local_rbx = (uint32_t)(result);
        Arg1 = v_stack_m150;
        result = RtlpTimeToTimeFields(Arg1, Arg2, a3, a4);
        Arg2 = v_stack_m150;
        v_stack_mF8 = (uint16_t)(local_rbx);
        Arg1 = v_stack_mF8;
        result = RtlpTimeFieldsToTime(Arg1, Arg2, a3, a4);
        local_rbx = 0;
    }
    if ((*(uint32_t *)(v_rip + 0x24B73A)) != 0) goto loc_00C1CE52;
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, a3, a4);
    result = (v_stack_m150) - (*(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B8));
    goto loc_00C1CE57;
loc_00C1CE52:
loc_00C1CE57:
    v_stack_m120 = v_stack_m150;
    result = KeSetSystemTime(v_stack_m150, v_stack_m100, 4, a4);
    result = PsGetCurrentServerSiloGlobals(v_stack_m150, v_stack_m100, 4, a4);
    a3 = 0;
    v_stack_m168 = (uint8_t)(*(uint8_t *)(v_rip + 0x1F1D0A));
    v_stack_m178 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B4)));
    result = PoNotifySystemTimeSet(v_stack_m150, v_stack_m100, a3, v_stack_m120);
    result = RtlInitUnicodeString(v_stack_mD8, v_rip + 377251, a3, v_stack_m120);
    v_stack_m178 = v_stack_m130;
    result = ZwQueryLicenseValue(v_stack_mD8, v_stack_m12C, v_rip + 3841440, 4);
    if (sign_flag) goto loc_00C1CEED;
    if (v_stack_m130 != 4) goto loc_00C1CEED;
    if (v_stack_m12C != 4) {
        *(uint32_t *)(v_rip + 0x3A9D71) = 1;
    }
    if (0 == 0) goto loc_00C1D039;
    result = strstr(0, v_rip + 377225, v_rip + 3841440, 4);
    if (result == 0) goto loc_00C1CF37;
    result = strstr(result, v_rip + 375989, v_rip + 3841440, 4);
    if (result != 0) {
        Arg1 = result + 1;
        result = atol(Arg1, v_rip + 375989, v_rip + 3841440, 4);
        *(uint32_t *)(v_rip + 0x3A9DBD) = (uint32_t)(result);
    }
    result = strstr(0, v_rip + 377186, v_rip + 3841440, 4);
    if (result == 0) goto loc_00C1CF6E;
    result = strstr(result, v_rip + 375934, v_rip + 3841440, 4);
    if (result != 0) {
        Arg1 = result + 1;
        result = atol(Arg1, v_rip + 375934, v_rip + 3841440, 4);
        *(uint32_t *)(v_rip + 0x3A9D26) = (uint32_t)(result);
    }
    result = strstr(0, v_rip + 377147, v_rip + 3841440, 4);
    if (result == 0) goto loc_00C1CFA5;
    result = strstr(result, v_rip + 375879, v_rip + 3841440, 4);
    if (result != 0) {
        Arg1 = result + 1;
        result = atol(Arg1, v_rip + 375879, v_rip + 3841440, 4);
        *(uint32_t *)(v_rip + 0x3A9DAF) = (uint32_t)(result);
    }
    if ((*(uint8_t *)(v_rip + 0x3A9AFC)) != 0) goto loc_00C1D01B;
    result = strstr(0, v_rip + 377116, v_rip + 3841440, 4);
    if (result == 0) goto loc_00C1CFE4;
    result = strstr(result, v_rip + 375816, v_rip + 3841440, 4);
    if (result != 0) {
        Arg1 = result + 1;
        result = atol(Arg1, v_rip + 375816, v_rip + 3841440, 4);
        *(uint32_t *)(v_rip + 0x3A9CAC) = (uint32_t)(result);
    }
    result = strstr(0, v_rip + 377093, v_rip + 3841440, 4);
    if (result == 0) goto loc_00C1D01B;
    result = strstr(result, v_rip + 375761, v_rip + 3841440, 4);
    if (result != 0) {
        Arg1 = result + 1;
        result = atol(Arg1, v_rip + 375761, v_rip + 3841440, 4);
        *(uint32_t *)(v_rip + 0x3A9C71) = (uint32_t)(result);
    }
    result = strstr(0, v_rip + 377070, v_rip + 3841440, 4);
    if (result != 0) {
        *(uint32_t *)(v_rip + 0x3A9E23) = 1;
    }
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, v_rip + 377070, v_rip + 3841440, 4);
    *(uint64_t *)(v_rip + 0x3EB781) = result;
    result = KeStartAllProcessors(Arg1, v_rip + 377070, v_rip + 3841440, 4);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, v_rip + 377070, v_rip + 3841440, 4);
    *(uint64_t *)(v_rip + 0x3EB776) = result;
    result = EtwTimeProfileReset(Arg1, v_rip + 377070, v_rip + 3841440, 4);
    Arg2 = 0;
    result = KeSetAffinityProcess(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, v_rip + 3842225, 4);
    result = MakeGdtReadOnly(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, v_rip + 3842225, 4);
    a3 = 0;
    v_stack_m178 = v_stack_m148;
    result = RtlFindMessage(v_rip - 12701852, a3 + 11, a3, (uint32_t)(0x40000089ULL));
    if (sign_flag) goto loc_00C1D0B4;
    local_rbx = (v_stack_m148) + (4);
    goto loc_00C1D0BB;
loc_00C1D0B4:
loc_00C1D0BB:
    result = HalAllProcessorsStarted(v_rip - 12701852, a3 + 11, a3, (uint32_t)(0x40000089ULL));
    if ((uint8_t)(result) == 0) goto loc_00C1DB3A;
    result = RtlInitAnsiString(v_stack_mE8, v_rip + 376933, a3, (uint32_t)(0x40000089ULL));
    result = v_stack_mE8;
    if (((uint16_t)(v_stack_mE8)) >= 2) {
        Arg1 = 0xFFFEULL;
        result = (uint16_t)((v_stack_mE8) + ((uint16_t)(Arg1)));
        v_stack_mE8 = (uint16_t)(result);
    }
    v_stack_m178 = v_stack_m138;
    a4 = (uint32_t)(0x40000088ULL) + 21;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3A9990)))) <= 1) { a4 = (uint32_t)((uint32_t)(0x40000088ULL)); }
    a3 = 0;
    result = RtlFindMessage(v_rip - 12701972, a3 + 11, a3, a4);
    a3 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x3A9A64)))) == 0) goto loc_00C1D141;
    Arg1 = (*(uint64_t *)(v_rip + 0x3A9A64)) + (24);
loc_00C1D134:
    Arg2 = (0) + (*(uint64_t *)(arg1));
    local_rbx = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x3A9A64)))) - (1);
    if (condition_is_not_equal) goto loc_00C1D134;
loc_00C1D141:
    local_rbx = 0;
    if (sign_flag) goto loc_00C1D152;
    a3 = (v_stack_m138) + (4);
    goto loc_00C1D159;
loc_00C1D152:
loc_00C1D159:
    result = (Arg2 + 255) >> (8);
    v_stack_m170 = v_stack_mE8;
    v_stack_m178 = result;
    result = RtlStringCbPrintfA(result, 256, v_rip + 376807, (uint32_t)(*(uint32_t *)(v_rip + 0x3A9920)));
    if (sign_flag) {
        Arg1 = 50;
        Arg2 = (int32_t)((uint32_t)(result));
        v_stack_m178 = 0;
        a4 = Arg1 - 46;
        a3 = Arg1 - 43;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = InbvDisplayString(result, Arg2, a3, a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, a3, a4);
    result = ObInitSystem(1, Arg2, a3, a4);
    local_r13 = 0;
    if ((uint8_t)(result) == 0) {
        Arg1 = 1 + 97;
        result = KeBugCheck(Arg1, Arg2, a3, a4);
    }
    result = ExInitSystem(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) {
        a3 = 0;
        v_stack_m178 = 0;
        a4 = 1;
        Arg2 = 0xFFFFFFFFC0000001ULL;
        Arg1 = a3 + 50;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    result = HalReportResourceUsage(Arg1, Arg2, a3, a4);
    result = IoCreateObjectTypes(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) {
        a4 = 4;
        v_stack_m178 = 0;
        a3 = 0;
        Arg2 = 0xFFFFFFFFC0000001ULL;
        Arg1 = a4 + 46;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = KeInitSystem(1, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) {
        a3 = 0;
        v_stack_m178 = 0;
        a4 = 2;
        Arg2 = 0xFFFFFFFFC0000001ULL;
        Arg1 = a3 + 50;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    Arg2 = 0;
    result = KdInitSystem((uint32_t)(*(uint32_t *)(v_rip + 0x3A6F48)), Arg2, a3, a4);
    if ((uint8_t)(result) == 0) {
        a4 = 3;
        v_stack_m178 = 0;
        a3 = 0;
        Arg2 = 0xFFFFFFFFC0000001ULL;
        Arg1 = a4 + 47;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = kernel_indirect_call(v_rip + 3842202, v_rip + 3842321, v_rip + 3842208, v_rip + 3841127);
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result + (uint32_t)(0x80000000ULL) * 1))) != 0) goto loc_00C1D2D3;
    if (((uint32_t)(result)) != 0xC00000BBULL) {
        Arg2 = 0;
        v_stack_m178 = 0;
        a4 = 0;
        a3 = 0;
        Arg1 = Arg2 + 50;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = DbgkInitialize(Arg1, Arg2, a3, a4);
    if (sign_flag) {
        a4 = 0;
        Arg2 = (int32_t)((uint32_t)(result));
        a3 = 0;
        v_stack_m178 = 0;
        Arg1 = a4 + 50;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    Arg1 = 0;
    result = UcInitialize(Arg1, Arg2, a3, a4);
    result = BcdInitializeBcdSyncMutant(Arg1, Arg2, a3, a4);
    Arg1 = 0;
    result = VerifierInitSystem(Arg1, Arg2, a3, a4);
    result = SeInitSystem(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) {
        Arg1 = 99;
        result = KeBugCheck(Arg1, Arg2, a3, a4);
    }
    *(uint32_t *)(v_rip + 0x3A9B2B) = 648;
    result = AlpcpInitSystem(Arg1, Arg2, a3, a4);
    if (sign_flag) {
        Arg1 = 106;
        result = KeBugCheck(Arg1, Arg2, a3, a4);
    }
    *(uint64_t *)(v_rip + 0x3A9C24) = *(uint64_t *)(v_rip + 0x3A98D8);
    result = PsInitSystem(1, Arg1, a3, a4);
    result = ExInitLicenseCallback(1, Arg1, a3, a4);
    result = CreateSystemRootLink(Arg1, Arg1, a3, a4);
    if (sign_flag) {
        a4 = 0;
        Arg2 = (int32_t)((uint32_t)(result));
        a3 = 0;
        v_stack_m178 = 0;
        Arg1 = a4 + 100;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, a3, a4);
    *(uint64_t *)(v_rip + 0x3EB45D) = result;
    result = MmInitSystem(1, 0, a3, a4);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, 0, a3, a4);
    *(uint64_t *)(v_rip + 0x3EB44E) = result;
    result = CcInitializeCacheManager(1, 0, a3, a4);
    if ((uint8_t)(result) == 0) {
        Arg1 = 102;
        result = KeBugCheck(Arg1, 0, a3, a4);
    }
    result = CmInitSystem1(Arg1, 0, a3, a4);
    if ((uint8_t)(result) == 0) {
        Arg1 = 103;
        result = KeBugCheck(Arg1, 0, a3, a4);
    }
    result = PsInitializeBootCpuPartitions(Arg1, 0, a3, a4);
    result = ExInitializeLeapSecondData(Arg1, 0, a3, a4);
    if (sign_flag) {
        a4 = 0;
        Arg2 = (int32_t)((uint32_t)(result));
        v_stack_m178 = 0;
        Arg1 = a4 + 50;
        a3 = a4 + 12;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    v_stack_m158 = 0;
    result = ExIsMultiSessionSku(v_stack_m158, Arg2, a3, a4);
    if (sign_flag) goto loc_00C1D41D;
    if (v_stack_m158 != 0) {
        result = *(uint64_t *)(v_rip + 0x3A7BF3);
    }
    if ((*(uint32_t *)(v_rip + 0x3A6D6C)) != 0) {
        result = *(uint64_t *)(v_rip + 0x3A7BDB);
    }
    if ((*(uint32_t *)(v_rip + 0x2D2730)) != 0) {
        result = *(uint64_t *)(v_rip + 0x3A7BC3);
    }
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, a3, a4);
    *(uint64_t *)(v_rip + 0x3EB358) = result;
    Arg2 = 0;
    result = memset(v_stack_mC8, Arg2, 120, a4);
    v_stack_mC0 = v_rip - 4342876;
    v_stack_mB8 = v_rip - 4342695;
    v_stack_mB0 = v_rip - 9127938;
    v_stack_mA8 = v_rip - 618013;
    v_stack_mA0 = v_rip - 345240;
    v_stack_m98 = v_rip - 8406595;
    v_stack_m90 = v_rip - 4448510;
    v_stack_m88 = v_rip - 9324537;
    v_stack_m80 = v_rip - 8285876;
    v_stack_mC8 = 120;
    if ((*(uint8_t *)(v_rip + 0x3A960F)) != 0) goto loc_00C1D4E2;
    goto loc_00C1D505;
loc_00C1D4E2:
    *(uint64_t *)(v_rip + 0x3EB240) = v_rip - 6871385;
    *(uint64_t *)(v_rip + 0x3EB233) = v_rip + 53010;
loc_00C1D505:
    result = BgGetDisplayContext(v_stack_mC8, Arg2, 120, v_rip + 4108857);
    result = kernel_indirect_call(0, v_stack_mC8, result, v_rip + 4108857);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, v_stack_mC8, result, v_rip + 4108857);
    *(uint64_t *)(v_rip + 0x3EB28F) = result;
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)((int32_t)((uint32_t)(result)) + (uint32_t)(0x80000000ULL) * 1))) != 0) goto loc_00C1D560;
    result = (uint32_t)(0x80000000ULL);
    if (((uint32_t)((int32_t)((uint32_t)(result)))) != 0xC00000BBULL) {
        a4 = 1;
        v_stack_m178 = 0;
        Arg2 = (int32_t)((uint32_t)(result));
        a3 = 0;
        Arg1 = a4 + 49;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    Arg1 = 0;
    *(uint64_t *)(v_rip + 0x2E1A6C) = v_xmm0;
    *(uint64_t *)(v_rip + 0x2E1A7F) = v_xmm0;
    *(uint64_t *)(v_rip + 0x2E1A68) = v_xmm1;
    result = EmInitSystem(Arg1, Arg1, a3, a4);
    if (sign_flag) {
        a4 = 0;
        Arg2 = (int32_t)((uint32_t)(result));
        v_stack_m178 = 0;
        Arg1 = a4 + 50;
        a3 = a4 + 8;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = MfgInitSystem(Arg1, Arg2, a3, a4);
    if (sign_flag) {
        a4 = 0;
        Arg2 = (int32_t)((uint32_t)(result));
        v_stack_m178 = 0;
        Arg1 = a4 + 50;
        a3 = a4 + 9;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = PfInitializeSuperfetch(Arg1, Arg2, a3, a4);
    Arg1 = 0;
    result = SmInitSystem(Arg1, Arg2, a3, a4);
    if (sign_flag) {
        a4 = 0;
        Arg2 = (int32_t)((uint32_t)(result));
        v_stack_m178 = 0;
        Arg1 = a4 + 50;
        a3 = a4 + 11;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    result = VmInitSystem(1, Arg2, a3, a4);
    if (sign_flag) {
        a4 = 0;
        Arg2 = (int32_t)((uint32_t)(result));
        v_stack_m178 = 0;
        Arg1 = a4 + 50;
        a3 = a4 + 10;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xA60)) & (2)) == 0) goto loc_00C1D643;
    result = strstr(0, v_rip + 375610, a3, a4);
    if (result != 0) {
        v_stack_m168 = 0;
        Arg1 = v_rip - 12570007;
        v_stack_m170 = 0;
        a4 = 0;
        a3 = 0;
        v_stack_m178 = 0;
        Arg2 = 0;
        result = ZwUpdateWnfStateData(Arg1, Arg2, a3, a4);
    }
    if (((*(uint32_t *)(v_rip + 0x3A9420)) & (0x2000000ULL)) != 0) {
        v_stack_m168 = 0;
        Arg1 = v_rip - 12569558;
        v_stack_m170 = 0;
        a4 = 0;
        a3 = 0;
        v_stack_m178 = 0;
        Arg2 = 0;
        result = ZwUpdateWnfStateData(Arg1, Arg2, a3, a4);
    }
    result = FsRtlSendModernAppTermination(v_stack_m118, 1, 1, a4);
    result = ExInitializeTimeRefresh(v_stack_m118, 1, 1, a4);
    result = ExAcquireTimeRefreshLockExclusive(v_stack_m118, 1, 1, a4);
    result = ExInitializeUtcTimeZoneBias(v_stack_m120, 1, 1, a4);
    Arg1 = 0;
    result = ExpRefreshTimeZoneInformation(Arg1, 1, 1, a4);
    result = ExReleaseTimeRefreshLockExclusive(Arg1, 1, 1, a4);
    if (v_stack_m157 == 0) goto loc_00C1D70B;
    result = PsGetCurrentServerSiloGlobals(Arg1, 1, 1, a4);
    Arg1 = (v_stack_m120) + (*(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B8));
    v_stack_m150 = Arg1;
    result = KeSetSystemTime(v_stack_m150, v_stack_m100, 4, a4);
    goto loc_00C1D71E;
loc_00C1D70B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B4)))) != (*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B4))) {
        Arg2 = 0;
        Arg1 = 0;
        result = ZwSetSystemTime(Arg1, Arg2, 4, a4);
    }
    result = FsRtlInitSystem(Arg1, Arg2, 4, a4);
    if ((uint8_t)(result) == 0) {
        Arg1 = 104;
        result = KeBugCheck(Arg1, Arg2, 4, a4);
    }
    v_stack_m160 = 0;
    v_stack_m168 = 0;
    v_stack_m170 = 0x63647A6CULL;
    a3 = 0;
    Arg2 = 0;
    v_stack_m178 = 88;
    result = ExInitializeNPagedLookasideListInternal(v_rip + 2140994, Arg2, a3, 512);
    Arg1 = 0;
    v_stack_m168 = 16;
    v_stack_m170 = 0x656C5252ULL;
    v_stack_m178 = 56;
    result = (uint32_t)((0) & (512));
    *(uint32_t *)(v_rip + 0x24A3A7) = (uint32_t)(result);
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)((uint32_t)(0x100002ULL))));
    Arg2 = (((uint32_t)(Arg1)) == ((uint32_t)((uint32_t)(0x100002ULL)))) ? 1 : 0;
    result = (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)(0x100002ULL)))) ? 1 : 0;
    a4 = 0;
    a3 = 0;
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)((uint8_t)(result))));
    *(uint32_t *)(v_rip + 0x24A377) = Arg2;
    Arg2 = 0;
    result = ExInitializePagedLookasideList(v_rip + 2140733, Arg2, a3, a4);
    result = HvlDebuggerSupportInitialize(Arg1, Arg2, a3, a4);
    Arg1 = 0;
    result = HalReportResourceUsage(Arg1, Arg2, a3, a4);
    result = kernel_indirect_call(1, 0, v_rip + 3317242, a4);
    result = PpInitSystem(1, 0, v_rip + 3317242, a4);
    if ((uint8_t)(result) == 0) {
        Arg1 = 144;
        result = KeBugCheck(Arg1, 0, v_rip + 3317242, a4);
    }
    if (0 == 0) goto loc_00C1D93E;
    result = strstr(0, v_rip + 375140, v_rip + 3317242, a4);
    if (result == 0) goto loc_00C1D93E;
    result = strncmp(result + 9, v_rip + 375120, 7, a4);
    if ((uint32_t)(result) != 0) goto loc_00C1D855;
    *(uint32_t *)(v_rip + 0x3A6971) = 1;
    goto loc_00C1D872;
loc_00C1D855:
    result = strncmp(result + 9, v_rip + 375105, 7, a4);
    if ((uint32_t)(result) != 0) goto loc_00C1D877;
    *(uint32_t *)(v_rip + 0x3A6952) = 2;
loc_00C1D872:
    local_rbx = (result + 9) + (7);
    goto loc_00C1D8A8;
loc_00C1D877:
    result = strncmp(local_rbx, v_rip + 375084, 8, a4);
    if ((uint32_t)(result) != 0) goto loc_00C1D8A1;
    local_rbx = (local_rbx) + (8);
    *(uint32_t *)(v_rip + 0x3A6925) = 3;
    goto loc_00C1D8A8;
loc_00C1D8A1:
    *(uint32_t *)(v_rip + 0x3A691C) = 0;
loc_00C1D8A8:
    result = 3;
    if ((*(uint8_t *)(local_rbx)) != 0) {
        a3 = 16;
        Arg2 = v_rip + 375046;
        Arg1 = local_rbx;
        result = strncmp(Arg1, Arg2, a3, a4);
        Arg1 = v_stack_m140;
        Arg1 = (uint8_t)(Arg1);
        if ((uint32_t)(result) == 0) { Arg1 = 1; }
        v_stack_m140 = (uint32_t)(Arg1);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3A68EB))) == 0) goto loc_00C1D93E;
    v_stack_m148 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x3A68EB))) - (1));
    if (condition_is_equal) goto loc_00C1D904;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00C1D8FC;
    if (((uint32_t)(result)) != 1) goto loc_00C1D90A;
    goto loc_00C1D90A;
loc_00C1D8FC:
    goto loc_00C1D90A;
loc_00C1D904:
loc_00C1D90A:
    a3 = 0;
    v_stack_m178 = v_stack_m148;
    result = RtlFindMessage(v_rip - 12704025, a3 + 11, a3, 168);
    if (sign_flag) goto loc_00C1D945;
    Arg1 = (v_stack_m148) + (4);
    result = InbvDisplayString(Arg1, a3 + 11, a3, 168);
    goto loc_00C1D945;
loc_00C1D93E:
loc_00C1D945:
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x84)) & (0x800ULL)) == 0) goto loc_00C1D994;
    a3 = 0;
    v_stack_m178 = v_stack_m138;
    result = RtlFindMessage(v_rip - 12704069, a3 + 11, a3, 183);
    if (!(sign_flag)) {
        Arg1 = v_stack_m138;
        Arg1 = (Arg1) + (4);
        result = InbvDisplayString(Arg1, a3 + 11, a3, 183);
    }
    result = IopInitializeBootLogging(Arg1, result + 256, a3, 183);
loc_00C1D994:
    result = ExpWatchProductTypeInitialization(Arg1, result + 256, a3, 183);
    Arg1 = 0;
    result = BootApplicationPersistentDataProcess(Arg1, result + 256, a3, 183);
    result = kernel_indirect_call(2, result + 256, a3, 183);
    if ((*(uint32_t *)(v_rip + 0x3BC14F)) >= = ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3A9125))))) {
        *(uint32_t *)(v_rip + 0x3BC147) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3A9125)));
    }
    v_stack_m148 = 0;
    *(uint32_t *)(v_rip + 0x2DC726) = 0;
    result = ExpGetOriginalImageVersionRegistryValue(v_stack_m148, result + 256, a3, 183);
    if (!(sign_flag)) {
        result = v_stack_m148;
        *(uint32_t *)(v_rip + 0x2DC713) = (uint32_t)(result);
    }
    result = ExpComputeCyclesPerYield(v_stack_m148, result + 256, a3, 183);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x3A7600) + 0x2D6) = (uint16_t)(result);
    if ((*(uint8_t *)(v_rip + 0x3A6747)) != 0) {
        result = CreateMiniNtBootKey(*(uint64_t *)(v_rip + 0x3A7600), result + 256, a3, 183);
    }
    result = kernel_indirect_call(*(uint64_t *)(v_rip + 0x3A7600), result + 256, a3, 183);
    result = SeCodeIntegrityInitializePolicy(0, result + 256, a3, 183);
    if (sign_flag) {
        a4 = 0;
        Arg2 = (int32_t)((uint32_t)(result));
        a3 = 0x69436553ULL;
        v_stack_m178 = 0;
        Arg1 = a4 + 50;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    *(uint32_t *)(v_rip + 0x1ED001) = 0;
    *(uint64_t *)(v_rip + 0x2DD22A) = v_rip + 3002928;
    *(uint64_t *)(v_rip + 0x2DD218) = v_rip + 3002928;
    *(uint32_t *)(v_rip + 0x2DD21F) = 0;
    *(uint64_t *)(v_rip + 0x2DD1D0) = v_rip + 3002838;
    *(uint64_t *)(v_rip + 0x2DD1C1) = v_rip + 3002838;
    *(uint64_t *)(v_rip + 0x2DD1DB) = v_rip + 3002842;
    *(uint64_t *)(v_rip + 0x2DD1CC) = v_rip + 3002842;
    *(uint64_t *)(v_rip + 0x2DD1FD) = 0;
    *(uint64_t *)(v_rip + 0x2DD1E6) = 0;
    *(uint16_t *)(v_rip + 0x2DD18E) = 1;
    *(uint8_t *)(v_rip + 0x2DD189) = 6;
    *(uint32_t *)(v_rip + 0x2DD184) = 0;
    *(uint16_t *)(v_rip + 0x2DD198) = 1;
    *(uint8_t *)(v_rip + 0x2DD193) = 6;
    *(uint32_t *)(v_rip + 0x2DD18E) = 1;
    result = PoInitSystem(1, Arg1, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C1DB2F;
    result = RtlInitFunctionalityCache(1, Arg1, a3, a4);
    a4 = 0;
    v_stack_m178 = 0;
    a3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_rip + 2172082, Arg2, a3, a4);
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    return result;
loc_00C1DB2F:
    result = KeBugCheck(160, Arg2, a3, a4);
loc_00C1DB3A:
    result = KeBugCheck(97, Arg2, a3, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xD8` | `64` | `R` |
| `Arg1` | `+ 0xF0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C1C728&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
