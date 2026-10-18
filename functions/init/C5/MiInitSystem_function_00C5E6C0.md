# MiInitSystem

- RVA: `0x00C5E6C0`–`0x00C5ED6A` (길이 `1,706` bytes)
- VA: `0x0000000140C5E6C0`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D7658`
- 디코드: `397`개 명령, `1,706/1,706` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **80**; 고유 호출 대상: **51**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **71**

### Outgoing calls
- `0x00C5E743` → [Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline_function_005D4A08.md) (function, `0x005D4A08`)
- `0x00C5E756` → [MiReservePtes](../../text/31/MiReservePtes_function_00318D20.md) (function, `0x00318D20`)
- `0x00C5E764` → [MiReservePtes](../../text/31/MiReservePtes_function_00318D20.md) (function, `0x00318D20`)
- `0x00C5E787` → [MiInitializeWorkingSetManagerParameters](../../text/67/MiInitializeWorkingSetManagerParameters_function_0067E7F8.md) (function, `0x0067E7F8`)
- `0x00C5E793` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5E799` → [ExInitializePagedHeaps](../../text/65/ExInitializePagedHeaps_function_0065C23C.md) (function, `0x0065C23C`)
- `0x00C5E7A7` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5E7AF` → [PsInitializeQuotaSystem](../C4/PsInitializeQuotaSystem_function_00C46364.md) (function, `0x00C46364`)
- `0x00C5E7BD` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5E7C3` → [MiGenerateSecureCookie](../../page/7F/MiGenerateSecureCookie_function_007FE754.md) (function, `0x007FE754`)
- `0x00C5E7D9` → [ExecuteHotpatchTestBootFunction](../../text/52/ExecuteHotpatchTestBootFunction_function_00522CC8.md) (function, `0x00522CC8`)
- `0x00C5E7DE` → [MiInitializeSharedUserData](MiInitializeSharedUserData_function_00C5F098.md) (function, `0x00C5F098`)
- `0x00C5E7EA` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5E7F0` → [MiInitializeBootProcess](MiInitializeBootProcess_function_00C5EEFC.md) (function, `0x00C5EEFC`)
- `0x00C5E7FE` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5E80D` → [MI_FLUSH_ENTIRE_TB](../../text/31/MI_FLUSH_ENTIRE_TB_function_00314110.md) (function, `0x00314110`)
- `0x00C5E81C` → [MiAddLoaderHalIoMappings](MiAddLoaderHalIoMappings_function_00C5E568.md) (function, `0x00C5E568`)
- `0x00C5E835` → [MiAddLoaderHalIoMappings](MiAddLoaderHalIoMappings_function_00C5E568.md) (function, `0x00C5E568`)
- `0x00C5E844` → [KdSetDbgPrintBufferSize](../../text/5B/KdSetDbgPrintBufferSize_function_005B0F54.md) (function, `0x005B0F54`)
- `0x00C5E84C` → [MiSetSlabAllocatorPolicy](../../text/68/MiSetSlabAllocatorPolicy_function_0068F174.md) (function, `0x0068F174`)
- `0x00C5E854` → [MiInitializeHotPatches](../C6/MiInitializeHotPatches_function_00C67430.md) (function, `0x00C67430`)
- `0x00C5E860` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5E868` → [MmInitializeImageViewExtension](../C6/MmInitializeImageViewExtension_function_00C64F08.md) (function, `0x00C64F08`)
- `0x00C5E86D` → [MiInitializeKernelScp](../C6/MiInitializeKernelScp_function_00C664B8.md) (function, `0x00C664B8`)
- `0x00C5E87B` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5E883` → [ExGenRandom](../../text/41/ExGenRandom_function_0041B010.md) (function, `0x0041B010`)
- `0x00C5E8A3` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C5E8EE` → [MiActOnLargeKernelHalPages](../../page/7F/MiActOnLargeKernelHalPages_function_007F852C.md) (function, `0x007F852C`)
- `0x00C5E900` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5E91E` → [MiCreateSlabAllocationsFromLoaderBlock](../C6/MiCreateSlabAllocationsFromLoaderBlock_function_00C69E3C.md) (function, `0x00C69E3C`)
- `0x00C5E92C` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5E932` → [MiInitializeSystemSpaceMap](../C6/MiInitializeSystemSpaceMap_function_00C64E60.md) (function, `0x00C64E60`)
- `0x00C5E94E` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C5E95D` → [MiInitializeBootKernelShadowStacks](../C6/MiInitializeBootKernelShadowStacks_function_00C67CA8.md) (function, `0x00C67CA8`)
- `0x00C5E965` → [MiInitializeSystemImageRegion](../C6/MiInitializeSystemImageRegion_function_00C6C05C.md) (function, `0x00C6C05C`)
- `0x00C5E971` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5E97A` → [MiInitializeLoadedModuleList](../C6/MiInitializeLoadedModuleList_function_00C6BCDC.md) (function, `0x00C6BCDC`)
- `0x00C5E981` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C5E98D` → [MiUpdateSharedUserDataNumberOfPages](../../page/7F/MiUpdateSharedUserDataNumberOfPages_function_007FB160.md) (function, `0x007FB160`)
- `0x00C5E9B5` → [MmConfigurePrefetchSeekThreshold](../../page/7F/MmConfigurePrefetchSeekThreshold_function_007FE6BC.md) (function, `0x007FE6BC`)
- `0x00C5E9C8` → [PsSetPagePriorityThread](../../text/3C/PsSetPagePriorityThread_function_003C4138.md) (function, `0x003C4138`)
- `0x00C5E9D9` → [MiEnumerateSystemImages](../../text/2A/MiEnumerateSystemImages_function_002A3D40.md) (function, `0x002A3D40`)
- `0x00C5E9E5` → [MmLockPagableDataSection](../../page/A7/MmLockPagableDataSection_function_00A73E80.md) (function, `0x00A73E80`)
- `0x00C5E9F4` → [MmUnlockPagableImageSection](../../text/2A/MmUnlockPagableImageSection_function_002A39F0.md) (function, `0x002A39F0`)
- `0x00C5E9F9` → [MiAllocateDummyPage](MiAllocateDummyPage_function_00C5F6E8.md) (function, `0x00C5F6E8`)
- `0x00C5EA2A` → [MiReservePtes](../../text/31/MiReservePtes_function_00318D20.md) (function, `0x00318D20`)
- `0x00C5EA41` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5EA67` → [MiInitializeRelocations](../C6/MiInitializeRelocations_function_00C69790.md) (function, `0x00C69790`)
- `0x00C5EA73` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5EA7B` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C5EA87` → [KeGetTbSize](../C3/KeGetTbSize_function_00C3964C.md) (function, `0x00C3964C`)
- `0x00C5EAA2` → [MiInitializeTbFlush](../C6/MiInitializeTbFlush_function_00C6B01C.md) (function, `0x00C6B01C`)
- `0x00C5EABF` → [MiInitializeTbFlush](../C6/MiInitializeTbFlush_function_00C6B01C.md) (function, `0x00C6B01C`)
- `0x00C5EAC6` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C5EAD2` → [MiInitializeMirroring](../C6/MiInitializeMirroring_function_00C64730.md) (function, `0x00C64730`)
- `0x00C5EAE2` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5EB43` → [VslInitializeSecurePool](../../text/58/VslInitializeSecurePool_function_0058E970.md) (function, `0x0058E970`)
- `0x00C5EB51` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5EB57` → [MiSectionInitialization](../C6/MiSectionInitialization_function_00C644A4.md) (function, `0x00C644A4`)
- `0x00C5EB63` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5EB69` → [MiInitializeCfg](../C6/MiInitializeCfg_function_00C69958.md) (function, `0x00C69958`)
- `0x00C5EB77` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5EB80` → [MiCreateEnclaveRegions](../C6/MiCreateEnclaveRegions_function_00C68AD4.md) (function, `0x00C68AD4`)
- `0x00C5EB8C` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5EB99` → [MiInitializeCacheFlushing](../C6/MiInitializeCacheFlushing_function_00C6ACF8.md) (function, `0x00C6ACF8`)
- `0x00C5EBA8` → [MiInitializeMemoryEvents](../../page/81/MiInitializeMemoryEvents_function_0081123C.md) (function, `0x0081123C`)
- `0x00C5EBB4` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5EC15` → [MiComputeMemoryNodeProcessorAssignments](../C6/MiComputeMemoryNodeProcessorAssignments_function_00C68F8C.md) (function, `0x00C68F8C`)
- `0x00C5EC82` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00C5ECB5` → [PsCreateSystemThread](../../page/9E/PsCreateSystemThread_function_009ED0D0.md) (function, `0x009ED0D0`)
- `0x00C5ECC5` → [ObCloseHandle](../../page/8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00C5ECD3` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5ECE5` → [MiEnumerateSystemImages](../../text/2A/MiEnumerateSystemImages_function_002A3D40.md) (function, `0x002A3D40`)
- `0x00C5ECF8` → [MiInitializeApiSets](../C6/MiInitializeApiSets_function_00C6BA2C.md) (function, `0x00C6BA2C`)
- `0x00C5ED04` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C5ED24` → [MiRegisterForHardwareAcceleratorChanges](../C6/MiRegisterForHardwareAcceleratorChanges_function_00C6CB08.md) (function, `0x00C6CB08`)
- `0x00C5ED35` → [MiEnumerateSystemImages](../../text/2A/MiEnumerateSystemImages_function_002A3D40.md) (function, `0x002A3D40`)
- `0x00C5ED3A` → [MiFlushStrongCodeDriverLoadFailures](../C6/MiFlushStrongCodeDriverLoadFailures_function_00C61680.md) (function, `0x00C61680`)
- `0x00C5ED3F` → [MiFlushDeferredRetpolineImageLoadEvents](../../page/80/MiFlushDeferredRetpolineImageLoadEvents_function_00801540.md) (function, `0x00801540`)
- `0x00C5ED4C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MmInitSystem](../BE/MmInitSystem_function_00BEE990.md) at `0x00BEEA80`
- [MmInitSystem](../BE/MmInitSystem_function_00BEE990.md) at `0x00BEEAD4`

### Static image references
- `0x00C5E6D6` → RVA `0x00E0A740` (`.data`; read)
- `0x00C5E6E8` → RVA `0x005C5B30` (`KeBalanceSetManager`; read)
- `0x00C5E6F3` → RVA `0x005C5E00` (`KeSwapProcessOrStack`; read)
- `0x00C5E6FE` → RVA `0x00379AC0` (`MiRebuildLargePagesThread`; read)
- `0x00C5E709` → RVA `0x00696D80` (`MiZeroPageThread`; read)
- `0x00C5E714` → RVA `0x00464890` (`MiDereferenceSegmentThread`; read)
- `0x00C5E71F` → RVA `0x00404AC0` (`MiMappedPageWriter`; read)
- `0x00C5E73D` → RVA `0x00FC6BBC` (`ALMOSTRO`; read/write)
- `0x00C5E748` → RVA `0x00E37668` (`.data`; read)
- `0x00C5E769` → RVA `0x00E301C0` (`.data`; write)
- `0x00C5E76F` → RVA `0x00E301B8` (`.data`; write)
- `0x00C5E776` → RVA `0x00E374C4` (`.data`; read/write)
- `0x00C5E77D` → RVA `0x00E38D00` (`.data`; read)
- `0x00C5E7C8` → RVA `0x00E2DB80` (`.data`; write)
- `0x00C5E7CF` → RVA `0x00E2DB48` (`.data`; write)
- `0x00C5E812` → RVA `0x01008700` (`INITDATA`; read)
- `0x00C5E821` → RVA `0x00E38CC0` (`.data`; read)
- `0x00C5E828` → RVA `0x00E38CB8` (`.data`; read)
- `0x00C5E83A` → RVA `0x00F55C60` (`.data`; read)
- `0x00C5E88D` → RVA `0x00E2EE78` (`.data`; write)
- `0x00C5E89D` → RVA `0x00E2EE80` (`.data`; write)
- `0x00C5E8A8` → RVA `0x00FC5258` (`ALMOSTRO`; read)
- `0x00C5E8AF` → RVA `0x01008878` (`INITDATA`; write)
- `0x00C5E8B8` → RVA `0x00FC5258` (`ALMOSTRO`; write)
- `0x00C5E8BF` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00C5E8CF` → RVA `0x00E2CB40` (`.data`; read)
- `0x00C5E8DB` → RVA `0x00C69C80` (`MiCreateKernelHalSlabRange`; read)
- `0x00C5E913` → RVA `0x00E38D04` (`.data`; read/write)
- `0x00C5E939` → RVA `0x00E2D708` (`.data`; write)
- `0x00C5E940` → RVA `0x00E2FF28` (`.data`; write)
- `0x00C5E947` → RVA `0x00E2FF38` (`.data`; write)
- `0x00C5E956` → RVA `0x01008880` (`INITDATA`; write)
- `0x00C5E986` → RVA `0x01008888` (`INITDATA`; write)
- `0x00C5E992` → RVA `0x00FC5008` (`ALMOSTRO`; read)
- `0x00C5E9A5` → RVA `0x00FC6A88` (`ALMOSTRO`; read/write)
- `0x00C5E9AE` → RVA `0x00E39140` (`.data`; write)
- `0x00C5E9D0` → RVA `0x00C5F550` (`MiEnablePagingOfDriver`; read)
- `0x00C5E9DE` → RVA `0x00B73D80` (`MmShutdownSystem`; read)
- `0x00C5E9ED` → RVA `0x00FC6C00` (`ALMOSTRO`; write)
- `0x00C5E9FE` → RVA `0x00E37438` (`.data`; write)
- `0x00C5EA23` → RVA `0x00E37430` (`.data`; write)
- `0x00C5EA2F` → RVA `0x00FC6C08` (`ALMOSTRO`; write)
- `0x00C5EA80` → RVA `0x01008898` (`INITDATA`; write)
- `0x00C5EA8E` → RVA `0x00E2DCD0` (`.data`; write)
- `0x00C5EAA9` → RVA `0x00E2DCD0` (`.data`; read)
- `0x00C5EACB` → RVA `0x010088A0` (`INITDATA`; write)
- `0x00C5EB35` → RVA `0x00E38C90` (`.data`; read)
- `0x00C5EB3C` → RVA `0x00E38C88` (`.data`; read)
- `0x00C5EB92` → RVA `0x00E2FF08` (`.data`; write)
- `0x00C5EBBA` → RVA `0x00FC520C` (`ALMOSTRO`; read)
- `0x00C5EBD5` → RVA `0x00FC520C` (`ALMOSTRO`; write)
- `0x00C5EBDB` → RVA `0x00FC5200` (`ALMOSTRO`; read)
- `0x00C5EBEB` → RVA `0x00FC5200` (`ALMOSTRO`; write)
- `0x00C5EBF5` → RVA `0x00E3738C` (`.data`; write)
- `0x00C5EBFF` → RVA `0x00E37390` (`.data`; write)
- `0x00C5EC1A` → RVA `0x00E37540` (`.data`; read)
- `0x00C5EC21` → RVA `0x00E2FFA8` (`.data`; write)
- `0x00C5EC29` → RVA `0x00E37548` (`.data`; write)
- `0x00C5EC30` → RVA `0x01008778` (`INITDATA`; read)
- `0x00C5EC37` → RVA `0x00E37540` (`.data`; write)
- `0x00C5EC43` → RVA `0x00E2FFB0` (`.data`; read)
- `0x00C5EC4A` → RVA `0x00E2FFAA` (`.data`; write)
- `0x00C5EC51` → RVA `0x00E2FFB8` (`.data`; write)
- `0x00C5EC58` → RVA `0x00E2FFB0` (`.data`; write)
- `0x00C5EC5F` → RVA `0x007F94D0` (`MiHotAddBootDeferredDescriptors`; read)
- `0x00C5EC66` → RVA `0x01008788` (`INITDATA`; write)
- `0x00C5EC6D` → RVA `0x00E2FFAC` (`.data`; write)
- `0x00C5EC74` → RVA `0x01008790` (`INITDATA`; write)
- `0x00C5EC7B` → RVA `0x01008778` (`INITDATA`; write)
- `0x00C5ECDC` → RVA `0x007F8F50` (`MiWriteProtectSystemImages`; read)
- `0x00C5ED2C` → RVA `0x00C6C7D0` (`MiUnlockBootPageSections`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **53**
  - `0x00C5E743` → [Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline_function_005D4A08.md) (`INIT` → `.text`)
  - `0x00C5E756` → [MiReservePtes](../../text/31/MiReservePtes_function_00318D20.md) (`INIT` → `.text`)
  - `0x00C5E764` → [MiReservePtes](../../text/31/MiReservePtes_function_00318D20.md) (`INIT` → `.text`)
  - `0x00C5E787` → [MiInitializeWorkingSetManagerParameters](../../text/67/MiInitializeWorkingSetManagerParameters_function_0067E7F8.md) (`INIT` → `.text`)
  - `0x00C5E793` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5E799` → [ExInitializePagedHeaps](../../text/65/ExInitializePagedHeaps_function_0065C23C.md) (`INIT` → `.text`)
  - `0x00C5E7A7` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5E7BD` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5E7C3` → [MiGenerateSecureCookie](../../page/7F/MiGenerateSecureCookie_function_007FE754.md) (`INIT` → `PAGE`)
  - `0x00C5E7D9` → [ExecuteHotpatchTestBootFunction](../../text/52/ExecuteHotpatchTestBootFunction_function_00522CC8.md) (`INIT` → `.text`)
  - `0x00C5E7EA` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5E7FE` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5E80D` → [MI_FLUSH_ENTIRE_TB](../../text/31/MI_FLUSH_ENTIRE_TB_function_00314110.md) (`INIT` → `.text`)
  - `0x00C5E844` → [KdSetDbgPrintBufferSize](../../text/5B/KdSetDbgPrintBufferSize_function_005B0F54.md) (`INIT` → `.text`)
  - `0x00C5E84C` → [MiSetSlabAllocatorPolicy](../../text/68/MiSetSlabAllocatorPolicy_function_0068F174.md) (`INIT` → `.text`)
  - `0x00C5E860` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5E87B` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5E883` → [ExGenRandom](../../text/41/ExGenRandom_function_0041B010.md) (`INIT` → `.text`)
  - `0x00C5E8A3` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C5E8EE` → [MiActOnLargeKernelHalPages](../../page/7F/MiActOnLargeKernelHalPages_function_007F852C.md) (`INIT` → `PAGE`)
  - `0x00C5E900` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5E92C` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5E94E` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C5E971` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5E981` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C5E98D` → [MiUpdateSharedUserDataNumberOfPages](../../page/7F/MiUpdateSharedUserDataNumberOfPages_function_007FB160.md) (`INIT` → `PAGE`)
  - `0x00C5E9B5` → [MmConfigurePrefetchSeekThreshold](../../page/7F/MmConfigurePrefetchSeekThreshold_function_007FE6BC.md) (`INIT` → `PAGE`)
  - `0x00C5E9C8` → [PsSetPagePriorityThread](../../text/3C/PsSetPagePriorityThread_function_003C4138.md) (`INIT` → `.text`)
  - `0x00C5E9D9` → [MiEnumerateSystemImages](../../text/2A/MiEnumerateSystemImages_function_002A3D40.md) (`INIT` → `.text`)
  - `0x00C5E9E5` → [MmLockPagableDataSection](../../page/A7/MmLockPagableDataSection_function_00A73E80.md) (`INIT` → `PAGE`)
  - `0x00C5E9F4` → [MmUnlockPagableImageSection](../../text/2A/MmUnlockPagableImageSection_function_002A39F0.md) (`INIT` → `.text`)
  - `0x00C5EA2A` → [MiReservePtes](../../text/31/MiReservePtes_function_00318D20.md) (`INIT` → `.text`)
  - `0x00C5EA41` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5EA73` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5EA7B` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C5EAC6` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C5EAE2` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5EB43` → [VslInitializeSecurePool](../../text/58/VslInitializeSecurePool_function_0058E970.md) (`INIT` → `.text`)
  - `0x00C5EB51` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5EB63` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5EB77` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5EB8C` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5EBA8` → [MiInitializeMemoryEvents](../../page/81/MiInitializeMemoryEvents_function_0081123C.md) (`INIT` → `PAGE`)
  - `0x00C5EBB4` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5EC82` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`INIT` → `.text`)
  - `0x00C5ECB5` → [PsCreateSystemThread](../../page/9E/PsCreateSystemThread_function_009ED0D0.md) (`INIT` → `PAGE`)
  - `0x00C5ECC5` → [ObCloseHandle](../../page/8A/ObCloseHandle_function_008A1870.md) (`INIT` → `PAGE`)
  - `0x00C5ECD3` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5ECE5` → [MiEnumerateSystemImages](../../text/2A/MiEnumerateSystemImages_function_002A3D40.md) (`INIT` → `.text`)
  - `0x00C5ED04` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C5ED35` → [MiEnumerateSystemImages](../../text/2A/MiEnumerateSystemImages_function_002A3D40.md) (`INIT` → `.text`)
  - `0x00C5ED3F` → [MiFlushDeferredRetpolineImageLoadEvents](../../page/80/MiFlushDeferredRetpolineImageLoadEvents_function_00801540.md) (`INIT` → `PAGE`)
  - `0x00C5ED4C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C5E6C0  4C 8B DC                        mov r11, rsp
00C5E6C3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00C5E6C7  49 89 6B 18                     mov qword ptr [r11 + 0x18], rbp
00C5E6CB  56                              push rsi
00C5E6CC  57                              push rdi
00C5E6CD  41 56                           push r14
00C5E6CF  48 81 EC 80 00 00 00            sub rsp, 0x80
00C5E6D6  48 8B 05 63 C0 1A 00            mov rax, qword ptr [rip + 0x1ac063]
00C5E6DD  48 33 C4                        xor rax, rsp
00C5E6E0  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00C5E6E5  45 33 F6                        xor r14d, r14d
00C5E6E8  48 8D 05 41 74 96 FF            lea rax, [rip - 0x698bbf]
00C5E6EF  49 89 43 B0                     mov qword ptr [r11 - 0x50], rax
00C5E6F3  48 8D 05 06 77 96 FF            lea rax, [rip - 0x6988fa]
00C5E6FA  49 89 43 B8                     mov qword ptr [r11 - 0x48], rax
00C5E6FE  48 8D 05 BB B3 71 FF            lea rax, [rip - 0x8e4c45]
00C5E705  49 89 43 C0                     mov qword ptr [r11 - 0x40], rax
00C5E709  48 8D 05 70 86 A3 FF            lea rax, [rip - 0x5c7990]
00C5E710  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
00C5E714  48 8D 05 75 61 80 FF            lea rax, [rip - 0x7f9e8b]
00C5E71B  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
00C5E71F  48 8D 05 9A 63 7A FF            lea rax, [rip - 0x859c66]
00C5E726  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00C5E72A  48 8B F2                        mov rsi, rdx
00C5E72D  4D 89 73 A8                     mov qword ptr [r11 - 0x58], r14
00C5E731  41 8D 5E 01                     lea ebx, [r14 + 1]
00C5E735  85 C9                           test ecx, ecx
00C5E737  0F 85 AB 03 00 00               jne 0x140c5eae8
00C5E73D  21 1D 79 84 36 00               and dword ptr [rip + 0x368479], ebx
00C5E743  E8 C0 62 97 FF                  call 0x1405d4a08
00C5E748  48 8D 0D 19 8F 1D 00            lea rcx, [rip + 0x1d8f19]
00C5E74F  85 C0                           test eax, eax
00C5E751  75 0A                           jne 0x140c5e75d
00C5E753  8D 53 1F                        lea edx, [rbx + 0x1f]
00C5E756  E8 C5 A5 6B FF                  call 0x140318d20
00C5E75B  EB 12                           jmp 0x140c5e76f
00C5E75D  BF 01 01 00 00                  mov edi, 0x101
00C5E762  8B D7                           mov edx, edi
00C5E764  E8 B7 A5 6B FF                  call 0x140318d20
00C5E769  89 3D 51 1A 1D 00               mov dword ptr [rip + 0x1d1a51], edi
00C5E76F  48 89 05 42 1A 1D 00            mov qword ptr [rip + 0x1d1a42], rax
00C5E776  F0 01 1D 47 8D 1D 00            lock add dword ptr [rip + 0x1d8d47], ebx
00C5E77D  48 8D 3D 7C A5 1D 00            lea rdi, [rip + 0x1da57c]
00C5E784  48 8B CF                        mov rcx, rdi
00C5E787  E8 6C 00 A2 FF                  call 0x14067e7f8
00C5E78C  85 C0                           test eax, eax
00C5E78E  75 09                           jne 0x140c5e799
00C5E790  8D 48 17                        lea ecx, [rax + 0x17]
00C5E793  E8 6C 32 A1 FF                  call 0x140671a04
00C5E798  CC                              int3
00C5E799  E8 9E DA 9F FF                  call 0x14065c23c
00C5E79E  85 C0                           test eax, eax
00C5E7A0  79 0B                           jns 0x140c5e7ad
00C5E7A2  B9 18 00 00 00                  mov ecx, 0x18
00C5E7A7  E8 58 32 A1 FF                  call 0x140671a04
00C5E7AC  CC                              int3
00C5E7AD  33 C9                           xor ecx, ecx
00C5E7AF  E8 B0 7B FE FF                  call 0x140c46364
00C5E7B4  84 C0                           test al, al
00C5E7B6  75 0B                           jne 0x140c5e7c3
00C5E7B8  B9 19 00 00 00                  mov ecx, 0x19
00C5E7BD  E8 42 32 A1 FF                  call 0x140671a04
00C5E7C2  CC                              int3
00C5E7C3  E8 8C FF B9 FF                  call 0x1407fe754
00C5E7C8  48 89 05 B1 F3 1C 00            mov qword ptr [rip + 0x1cf3b1], rax
00C5E7CF  C7 05 6F F3 1C 00 78 56 34 12   mov dword ptr [rip + 0x1cf36f], 0x12345678
00C5E7D9  E8 EA 44 8C FF                  call 0x140522cc8
00C5E7DE  E8 B5 08 00 00                  call 0x140c5f098
00C5E7E3  85 C0                           test eax, eax
00C5E7E5  75 09                           jne 0x140c5e7f0
00C5E7E7  8D 48 1A                        lea ecx, [rax + 0x1a]
00C5E7EA  E8 15 32 A1 FF                  call 0x140671a04
00C5E7EF  CC                              int3
00C5E7F0  E8 07 07 00 00                  call 0x140c5eefc
00C5E7F5  85 C0                           test eax, eax
00C5E7F7  79 0B                           jns 0x140c5e804
00C5E7F9  B9 1B 00 00 00                  mov ecx, 0x1b
00C5E7FE  E8 01 32 A1 FF                  call 0x140671a04
00C5E803  CC                              int3
00C5E804  48 83 CD FF                     or rbp, 0xffffffffffffffff
00C5E808  8B D5                           mov edx, ebp
00C5E80A  8D 4D 03                        lea ecx, [rbp + 3]
00C5E80D  E8 FE 58 6B FF                  call 0x140314110
00C5E812  48 8B 0D E7 9E 3A 00            mov rcx, qword ptr [rip + 0x3a9ee7]
00C5E819  48 8B D5                        mov rdx, rbp
00C5E81C  E8 47 FD FF FF                  call 0x140c5e568
00C5E821  48 8B 15 98 A4 1D 00            mov rdx, qword ptr [rip + 0x1da498]
00C5E828  48 8B 0D 89 A4 1D 00            mov rcx, qword ptr [rip + 0x1da489]
00C5E82F  48 FF CA                        dec rdx
00C5E832  48 03 D1                        add rdx, rcx
00C5E835  E8 2E FD FF FF                  call 0x140c5e568
00C5E83A  8B 0D 20 74 2F 00               mov ecx, dword ptr [rip + 0x2f7420]
00C5E840  85 C9                           test ecx, ecx
00C5E842  74 05                           je 0x140c5e849
00C5E844  E8 0B 27 95 FF                  call 0x1405b0f54
00C5E849  48 8B CF                        mov rcx, rdi
00C5E84C  E8 23 09 A3 FF                  call 0x14068f174
00C5E851  48 8B CE                        mov rcx, rsi
00C5E854  E8 D7 8B 00 00                  call 0x140c67430
00C5E859  85 C0                           test eax, eax
00C5E85B  75 09                           jne 0x140c5e866
00C5E85D  8D 48 1C                        lea ecx, [rax + 0x1c]
00C5E860  E8 9F 31 A1 FF                  call 0x140671a04
00C5E865  CC                              int3
00C5E866  33 C9                           xor ecx, ecx
00C5E868  E8 9B 66 00 00                  call 0x140c64f08
00C5E86D  E8 46 7C 00 00                  call 0x140c664b8
00C5E872  85 C0                           test eax, eax
00C5E874  79 0B                           jns 0x140c5e881
00C5E876  B9 1D 00 00 00                  mov ecx, 0x1d
00C5E87B  E8 84 31 A1 FF                  call 0x140671a04
00C5E880  CC                              int3
00C5E881  8B CB                           mov ecx, ebx
00C5E883  E8 88 C7 7B FF                  call 0x14041b010
00C5E888  8B C8                           mov ecx, eax
00C5E88A  83 E0 03                        and eax, 3
00C5E88D  48 89 0D E4 05 1D 00            mov qword ptr [rip + 0x1d05e4], rcx
00C5E894  33 C9                           xor ecx, ecx
00C5E896  8D 04 C5 08 00 00 00            lea eax, [rax*8 + 8]
00C5E89D  89 05 DD 05 1D 00               mov dword ptr [rip + 0x1d05dd], eax
00C5E8A3  E8 38 FF 71 FF                  call 0x14037e7e0
00C5E8A8  83 3D A9 69 36 00 02            cmp dword ptr [rip + 0x3669a9], 2
00C5E8AF  48 89 05 C2 9F 3A 00            mov qword ptr [rip + 0x3a9fc2], rax
00C5E8B6  76 07                           jbe 0x140c5e8bf
00C5E8B8  44 89 35 99 69 36 00            mov dword ptr [rip + 0x366999], r14d
00C5E8BF  F6 05 C2 81 36 00 04            test byte ptr [rip + 0x3681c2], 4
00C5E8C6  74 53                           je 0x140c5e91b
00C5E8C8  41 8B FE                        mov edi, r14d
00C5E8CB  3B FB                           cmp edi, ebx
00C5E8CD  73 37                           jae 0x140c5e906
00C5E8CF  48 8D 0D 6A E2 1C 00            lea rcx, [rip + 0x1ce26a]
00C5E8D6  8B C7                           mov eax, edi
00C5E8D8  45 33 C0                        xor r8d, r8d
00C5E8DB  48 8D 15 9E B3 00 00            lea rdx, [rip + 0xb39e]
00C5E8E2  48 8B 84 C1 00 0E 00 00         mov rax, qword ptr [rcx + rax*8 + 0xe00]
00C5E8EA  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
00C5E8EE  E8 39 9C B9 FF                  call 0x1407f852c
00C5E8F3  85 C0                           test eax, eax
00C5E8F5  78 04                           js 0x140c5e8fb
00C5E8F7  03 FB                           add edi, ebx
00C5E8F9  EB D0                           jmp 0x140c5e8cb
00C5E8FB  B9 1E 00 00 00                  mov ecx, 0x1e
00C5E900  E8 FF 30 A1 FF                  call 0x140671a04
00C5E905  CC                              int3
00C5E906  48 F7 05 77 81 36 00 00 40 00 00  test qword ptr [rip + 0x368177], 0x4000
00C5E911  74 08                           je 0x140c5e91b
00C5E913  F0 83 0D E9 A3 1D 00 08         lock or dword ptr [rip + 0x1da3e9], 8
00C5E91B  48 8B CE                        mov rcx, rsi
00C5E91E  E8 19 B5 00 00                  call 0x140c69e3c
00C5E923  85 C0                           test eax, eax
00C5E925  79 0B                           jns 0x140c5e932
00C5E927  B9 1F 00 00 00                  mov ecx, 0x1f
00C5E92C  E8 D3 30 A1 FF                  call 0x140671a04
00C5E931  CC                              int3
00C5E932  E8 29 65 00 00                  call 0x140c64e60
00C5E937  33 C9                           xor ecx, ecx
00C5E939  4C 89 35 C8 ED 1C 00            mov qword ptr [rip + 0x1cedc8], r14
00C5E940  4C 89 35 E1 15 1D 00            mov qword ptr [rip + 0x1d15e1], r14
00C5E947  4C 89 35 EA 15 1D 00            mov qword ptr [rip + 0x1d15ea], r14
00C5E94E  E8 8D FE 71 FF                  call 0x14037e7e0
00C5E953  48 8B CE                        mov rcx, rsi
00C5E956  48 89 05 23 9F 3A 00            mov qword ptr [rip + 0x3a9f23], rax
00C5E95D  E8 46 93 00 00                  call 0x140c67ca8
00C5E962  48 8B CE                        mov rcx, rsi
00C5E965  E8 F2 D6 00 00                  call 0x140c6c05c
00C5E96A  85 C0                           test eax, eax
00C5E96C  75 09                           jne 0x140c5e977
00C5E96E  8D 48 20                        lea ecx, [rax + 0x20]
00C5E971  E8 8E 30 A1 FF                  call 0x140671a04
00C5E976  CC                              int3
00C5E977  48 8B CE                        mov rcx, rsi
00C5E97A  E8 5D D3 00 00                  call 0x140c6bcdc
00C5E97F  33 C9                           xor ecx, ecx
00C5E981  E8 5A FE 71 FF                  call 0x14037e7e0
00C5E986  48 89 05 FB 9E 3A 00            mov qword ptr [rip + 0x3a9efb], rax
00C5E98D  E8 CE C7 B9 FF                  call 0x1407fb160
00C5E992  48 8B 15 6F 66 36 00            mov rdx, qword ptr [rip + 0x36666f]
00C5E999  B9 20 00 00 00                  mov ecx, 0x20
00C5E99E  44 89 B2 44 02 00 00            mov dword ptr [rdx + 0x244], r14d
00C5E9A5  48 0F BA 2D DA 80 36 00 17      bts qword ptr [rip + 0x3680da], 0x17
00C5E9AE  4C 89 35 8B A7 1D 00            mov qword ptr [rip + 0x1da78b], r14
00C5E9B5  E8 02 FD B9 FF                  call 0x1407fe6bc
00C5E9BA  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00C5E9C3  BA 05 00 00 00                  mov edx, 5
00C5E9C8  E8 6B 57 76 FF                  call 0x1403c4138
00C5E9CD  45 33 C0                        xor r8d, r8d
00C5E9D0  48 8D 0D 79 0B 00 00            lea rcx, [rip + 0xb79]
00C5E9D7  33 D2                           xor edx, edx
00C5E9D9  E8 62 53 64 FF                  call 0x1402a3d40
00C5E9DE  48 8D 0D 9B 53 F1 FF            lea rcx, [rip - 0xeac65]
00C5E9E5  E8 96 54 E1 FF                  call 0x140a73e80
00C5E9EA  48 8B C8                        mov rcx, rax
00C5E9ED  48 89 05 0C 82 36 00            mov qword ptr [rip + 0x36820c], rax
00C5E9F4  E8 F7 4F 64 FF                  call 0x1402a39f0
00C5E9F9  E8 EA 0C 00 00                  call 0x140c5f6e8
00C5E9FE  48 89 05 33 8A 1D 00            mov qword ptr [rip + 0x1d8a33], rax
00C5EA05  4C 8D 04 40                     lea r8, [rax + rax*2]
00C5EA09  49 C1 E0 04                     shl r8, 4
00C5EA0D  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00C5EA17  4C 03 C0                        add r8, rax
00C5EA1A  48 8D 0D 47 8C 1D 00            lea rcx, [rip + 0x1d8c47]
00C5EA21  8B D3                           mov edx, ebx
00C5EA23  4C 89 05 06 8A 1D 00            mov qword ptr [rip + 0x1d8a06], r8
00C5EA2A  E8 F1 A2 6B FF                  call 0x140318d20
00C5EA2F  48 89 05 D2 81 36 00            mov qword ptr [rip + 0x3681d2], rax
00C5EA36  48 8B C8                        mov rcx, rax
00C5EA39  48 85 C0                        test rax, rax
00C5EA3C  75 09                           jne 0x140c5ea47
00C5EA3E  8D 48 21                        lea ecx, [rax + 0x21]
00C5EA41  E8 BE 2F A1 FF                  call 0x140671a04
00C5EA46  CC                              int3
00C5EA47  48 C1 E1 19                     shl rcx, 0x19
00C5EA4B  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00C5EA55  48 C1 E0 19                     shl rax, 0x19
00C5EA59  48 2B C8                        sub rcx, rax
00C5EA5C  48 C1 F9 10                     sar rcx, 0x10
00C5EA60  48 89 0D A1 81 36 00            mov qword ptr [rip + 0x3681a1], rcx
00C5EA67  E8 24 AD 00 00                  call 0x140c69790
00C5EA6C  85 C0                           test eax, eax
00C5EA6E  75 09                           jne 0x140c5ea79
00C5EA70  8D 48 22                        lea ecx, [rax + 0x22]
00C5EA73  E8 8C 2F A1 FF                  call 0x140671a04
00C5EA78  CC                              int3
00C5EA79  33 C9                           xor ecx, ecx
00C5EA7B  E8 60 FD 71 FF                  call 0x14037e7e0
00C5EA80  48 89 05 11 9E 3A 00            mov qword ptr [rip + 0x3a9e11], rax
00C5EA87  E8 C0 AB FD FF                  call 0x140c3964c
00C5EA8C  85 C0                           test eax, eax
00C5EA8E  48 89 2D 3B F2 1C 00            mov qword ptr [rip + 0x1cf23b], rbp
00C5EA95  48 8B D8                        mov rbx, rax
00C5EA98  BF 00 08 00 00                  mov edi, 0x800
00C5EA9D  0F 44 DF                        cmove ebx, edi
00C5EAA0  8B CB                           mov ecx, ebx
00C5EAA2  E8 75 C5 00 00                  call 0x140c6b01c
00C5EAA7  8B D3                           mov edx, ebx
00C5EAA9  48 39 15 20 F2 1C 00            cmp qword ptr [rip + 0x1cf220], rdx
00C5EAB0  75 12                           jne 0x140c5eac4
00C5EAB2  3B DF                           cmp ebx, edi
00C5EAB4  74 0E                           je 0x140c5eac4
00C5EAB6  8B CF                           mov ecx, edi
00C5EAB8  48 89 2D 11 F2 1C 00            mov qword ptr [rip + 0x1cf211], rbp
00C5EABF  E8 58 C5 00 00                  call 0x140c6b01c
00C5EAC4  33 C9                           xor ecx, ecx
00C5EAC6  E8 15 FD 71 FF                  call 0x14037e7e0
00C5EACB  48 89 05 CE 9D 3A 00            mov qword ptr [rip + 0x3a9dce], rax
00C5EAD2  E8 59 5C 00 00                  call 0x140c64730
00C5EAD7  85 C0                           test eax, eax
00C5EAD9  0F 85 65 02 00 00               jne 0x140c5ed44
00C5EADF  8D 48 2C                        lea ecx, [rax + 0x2c]
00C5EAE2  E8 1D 2F A1 FF                  call 0x140671a04
00C5EAE7  CC                              int3
00C5EAE8  3B CB                           cmp ecx, ebx
00C5EAEA  0F 85 1A 02 00 00               jne 0x140c5ed0a
00C5EAF0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00C5EAF9  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00C5EB00  F0 81 89 F4 01 00 00 00 04 00 00  lock or dword ptr [rcx + 0x1f4], 0x400
00C5EB0B  BF 00 08 00 00                  mov edi, 0x800
00C5EB10  F0 09 B9 F4 01 00 00            lock or dword ptr [rcx + 0x1f4], edi
00C5EB17  48 8B 05 EA 64 36 00            mov rax, qword ptr [rip + 0x3664ea]
00C5EB1E  C7 80 44 02 00 00 00 00 20 00   mov dword ptr [rax + 0x244], 0x200000
00C5EB28  48 F7 05 55 7F 36 00 00 40 00 00  test qword ptr [rip + 0x367f55], 0x4000
00C5EB33  74 22                           je 0x140c5eb57
00C5EB35  48 8B 15 54 A1 1D 00            mov rdx, qword ptr [rip + 0x1da154]
00C5EB3C  48 8B 0D 45 A1 1D 00            mov rcx, qword ptr [rip + 0x1da145]
00C5EB43  E8 28 FE 92 FF                  call 0x14058e970
00C5EB48  85 C0                           test eax, eax
00C5EB4A  79 0B                           jns 0x140c5eb57
00C5EB4C  B9 23 00 00 00                  mov ecx, 0x23
00C5EB51  E8 AE 2E A1 FF                  call 0x140671a04
00C5EB56  CC                              int3
00C5EB57  E8 48 59 00 00                  call 0x140c644a4
00C5EB5C  85 C0                           test eax, eax
00C5EB5E  75 09                           jne 0x140c5eb69
00C5EB60  8D 48 24                        lea ecx, [rax + 0x24]
00C5EB63  E8 9C 2E A1 FF                  call 0x140671a04
00C5EB68  CC                              int3
00C5EB69  E8 EA AD 00 00                  call 0x140c69958
00C5EB6E  85 C0                           test eax, eax
00C5EB70  79 0B                           jns 0x140c5eb7d
00C5EB72  B9 25 00 00 00                  mov ecx, 0x25
00C5EB77  E8 88 2E A1 FF                  call 0x140671a04
00C5EB7C  CC                              int3
00C5EB7D  48 8B CE                        mov rcx, rsi
00C5EB80  E8 4F 9F 00 00                  call 0x140c68ad4
00C5EB85  85 C0                           test eax, eax
00C5EB87  75 09                           jne 0x140c5eb92
00C5EB89  8D 48 27                        lea ecx, [rax + 0x27]
00C5EB8C  E8 73 2E A1 FF                  call 0x140671a04
00C5EB91  CC                              int3
00C5EB92  4C 89 35 6F 13 1D 00            mov qword ptr [rip + 0x1d136f], r14
00C5EB99  E8 5A C1 00 00                  call 0x140c6acf8
00C5EB9E  48 8D 3D 5B A1 1D 00            lea rdi, [rip + 0x1da15b]
00C5EBA5  48 8B CF                        mov rcx, rdi
00C5EBA8  E8 8F 26 BB FF                  call 0x14081123c
00C5EBAD  85 C0                           test eax, eax
00C5EBAF  75 09                           jne 0x140c5ebba
00C5EBB1  8D 48 29                        lea ecx, [rax + 0x29]
00C5EBB4  E8 4B 2E A1 FF                  call 0x140671a04
00C5EBB9  CC                              int3
00C5EBBA  8B 05 4C 66 36 00               mov eax, dword ptr [rip + 0x36664c]
00C5EBC0  83 F8 40                        cmp eax, 0x40
00C5EBC3  76 07                           jbe 0x140c5ebcc
00C5EBC5  B8 40 00 00 00                  mov eax, 0x40
00C5EBCA  EB 06                           jmp 0x140c5ebd2
00C5EBCC  85 C0                           test eax, eax
00C5EBCE  75 02                           jne 0x140c5ebd2
00C5EBD0  8B C3                           mov eax, ebx
00C5EBD2  C1 E0 08                        shl eax, 8
00C5EBD5  89 05 31 66 36 00               mov dword ptr [rip + 0x366631], eax
00C5EBDB  8B 05 1F 66 36 00               mov eax, dword ptr [rip + 0x36661f]
00C5EBE1  A9 F8 FF FF FF                  test eax, 0xfffffff8
00C5EBE6  74 09                           je 0x140c5ebf1
00C5EBE8  41 8B C6                        mov eax, r14d
00C5EBEB  89 05 0F 66 36 00               mov dword ptr [rip + 0x36660f], eax
00C5EBF1  A8 04                           test al, 4
00C5EBF3  74 16                           je 0x140c5ec0b
00C5EBF5  C7 05 8D 87 1D 00 10 00 00 00   mov dword ptr [rip + 0x1d878d], 0x10
00C5EBFF  C7 05 87 87 1D 00 08 00 00 00   mov dword ptr [rip + 0x1d8787], 8
00C5EC09  EB 0A                           jmp 0x140c5ec15
00C5EC0B  C7 05 77 87 1D 00 04 00 00 00   mov dword ptr [rip + 0x1d8777], 4
00C5EC15  E8 72 A3 00 00                  call 0x140c68f8c
00C5EC1A  48 8D 05 1F 89 1D 00            lea rax, [rip + 0x1d891f]
00C5EC21  66 44 89 35 7F 13 1D 00         mov word ptr [rip + 0x1d137f], r14w
00C5EC29  48 89 05 18 89 1D 00            mov qword ptr [rip + 0x1d8918], rax
00C5EC30  48 8D 0D 41 9B 3A 00            lea rcx, [rip + 0x3a9b41]
00C5EC37  48 89 05 02 89 1D 00            mov qword ptr [rip + 0x1d8902], rax
00C5EC3E  BA 03 00 00 00                  mov edx, 3
00C5EC43  48 8D 05 66 13 1D 00            lea rax, [rip + 0x1d1366]
00C5EC4A  C6 05 59 13 1D 00 06            mov byte ptr [rip + 0x1d1359], 6
00C5EC51  48 89 05 60 13 1D 00            mov qword ptr [rip + 0x1d1360], rax
00C5EC58  48 89 05 51 13 1D 00            mov qword ptr [rip + 0x1d1351], rax
00C5EC5F  48 8D 05 6A A8 B9 FF            lea rax, [rip - 0x465796]
00C5EC66  48 89 05 1B 9B 3A 00            mov qword ptr [rip + 0x3a9b1b], rax
00C5EC6D  44 89 35 38 13 1D 00            mov dword ptr [rip + 0x1d1338], r14d
00C5EC74  4C 89 35 15 9B 3A 00            mov qword ptr [rip + 0x3a9b15], r14
00C5EC7B  4C 89 35 F6 9A 3A 00            mov qword ptr [rip + 0x3a9af6], r14
00C5EC82  E8 99 A8 69 FF                  call 0x1402f9520
00C5EC87  41 8B EE                        mov ebp, r14d
00C5EC8A  83 FD 06                        cmp ebp, 6
00C5EC8D  73 4A                           jae 0x140c5ecd9
00C5EC8F  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00C5EC94  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00C5EC99  8B C5                           mov eax, ebp
00C5EC9B  45 33 C9                        xor r9d, r9d
00C5EC9E  45 33 C0                        xor r8d, r8d
00C5ECA1  BA FF FF 1F 00                  mov edx, 0x1fffff
00C5ECA6  48 8B 44 C4 48                  mov rax, qword ptr [rsp + rax*8 + 0x48]
00C5ECAB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C5ECB0  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00C5ECB5  E8 16 E4 D8 FF                  call 0x1409ed0d0
00C5ECBA  85 C0                           test eax, eax
00C5ECBC  78 10                           js 0x140c5ecce
00C5ECBE  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00C5ECC3  33 D2                           xor edx, edx
00C5ECC5  E8 A6 2B C4 FF                  call 0x1408a1870
00C5ECCA  03 EB                           add ebp, ebx
00C5ECCC  EB BC                           jmp 0x140c5ec8a
00C5ECCE  B9 2B 00 00 00                  mov ecx, 0x2b
00C5ECD3  E8 2C 2D A1 FF                  call 0x140671a04
00C5ECD8  CC                              int3
00C5ECD9  45 33 C0                        xor r8d, r8d
00C5ECDC  48 8D 0D 6D A2 B9 FF            lea rcx, [rip - 0x465d93]
00C5ECE3  33 D2                           xor edx, edx
00C5ECE5  E8 56 50 64 FF                  call 0x1402a3d40
00C5ECEA  48 83 CD FF                     or rbp, 0xffffffffffffffff
00C5ECEE  F0 01 2D CF 87 1D 00            lock add dword ptr [rip + 0x1d87cf], ebp
00C5ECF5  48 8B CE                        mov rcx, rsi
00C5ECF8  E8 2F CD 00 00                  call 0x140c6ba2c
00C5ECFD  85 C0                           test eax, eax
00C5ECFF  79 43                           jns 0x140c5ed44
00C5ED01  8D 4D 2E                        lea ecx, [rbp + 0x2e]
00C5ED04  E8 FB 2C A1 FF                  call 0x140671a04
00C5ED09  CC                              int3
00C5ED0A  83 F9 02                        cmp ecx, 2
00C5ED0D  75 35                           jne 0x140c5ed44
00C5ED0F  48 8D 05 2A 88 1D 00            lea rax, [rip + 0x1d882a]
00C5ED16  48 89 05 2B 88 1D 00            mov qword ptr [rip + 0x1d882b], rax
00C5ED1D  48 89 05 1C 88 1D 00            mov qword ptr [rip + 0x1d881c], rax
00C5ED24  E8 DF DD 00 00                  call 0x140c6cb08
00C5ED29  45 33 C0                        xor r8d, r8d
00C5ED2C  48 8D 0D 9D DA 00 00            lea rcx, [rip + 0xda9d]
00C5ED33  33 D2                           xor edx, edx
00C5ED35  E8 06 50 64 FF                  call 0x1402a3d40
00C5ED3A  E8 41 29 00 00                  call 0x140c61680
00C5ED3F  E8 FC 27 BA FF                  call 0x140801540
00C5ED44  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00C5ED49  48 33 CC                        xor rcx, rsp
00C5ED4C  E8 EF D8 A4 FF                  call 0x1406ac640
00C5ED51  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
00C5ED59  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
00C5ED5D  49 8B 6B 30                     mov rbp, qword ptr [r11 + 0x30]
00C5ED61  49 8B E3                        mov rsp, r11
00C5ED64  41 5E                           pop r14
00C5ED66  5F                              pop rdi
00C5ED67  5E                              pop rsi
00C5ED68  C3                              ret
00C5ED69  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInitSystem(int a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rbp;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 1753187)) ^ (v_rsp);
    v_stack_m20 = result;
    v_r14 = 0;
    *(unsigned __int64 *)(v_rsp - 80) = v_rip - 6917055;
    *(unsigned __int64 *)(v_rsp - 72) = v_rip - 6916346;
    *(unsigned __int64 *)(v_rsp - 64) = v_rip - 9325637;
    *(unsigned __int64 *)(v_rsp - 56) = v_rip - 6060432;
    *(unsigned __int64 *)(v_rsp - 48) = v_rip - 8363659;
    *(unsigned __int64 *)(v_rsp - 40) = v_rip - 8756326;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    if (a1 != 0) goto loc_00C5EAE8;
    result = Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00C5E75D;
    result = MiReservePtes(v_rip + 1937177, v_r14 + 1 + 31, a3, a4);
    goto loc_00C5E76F;
loc_00C5E75D:
    result = MiReservePtes(v_rip + 1937177, 257, a3, a4);
    *(unsigned int *)(v_rip + 1907281) = 257;
loc_00C5E76F:
    *(unsigned __int64 *)(v_rip + 1907266) = result;
    result = MiInitializeWorkingSetManagerParameters(v_rip + 1942908, 257, a3, a4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 23;
        result = MxInstallMoreMemory(a1, 257, a3, a4);
    }
    result = ExInitializePagedHeaps(a1, 257, a3, a4);
    if (sign_flag) {
        a1 = 24;
        result = MxInstallMoreMemory(a1, 257, a3, a4);
    }
    a1 = 0;
    result = PsInitializeQuotaSystem(a1, 257, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a1 = 25;
        result = MxInstallMoreMemory(a1, 257, a3, a4);
    }
    result = MiGenerateSecureCookie(a1, 257, a3, a4);
    *(unsigned __int64 *)(v_rip + 1897393) = result;
    *(unsigned int *)(v_rip + 1897327) = 0x12345678ULL;
    result = ExecuteHotpatchTestBootFunction(a1, 257, a3, a4);
    result = MiInitializeSharedUserData(a1, 257, a3, a4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 26;
        result = MxInstallMoreMemory(a1, 257, a3, a4);
    }
    result = MiInitializeBootProcess(a1, 257, a3, a4);
    if (sign_flag) {
        a1 = 27;
        result = MxInstallMoreMemory(a1, 257, a3, a4);
    }
    v_rbp = (v_rbp) | (-1);
    result = MI_FLUSH_ENTIRE_TB(v_rbp + 3, (unsigned int)((unsigned int)(v_rbp)), a3, a4);
    result = MiAddLoaderHalIoMappings(*(unsigned __int64 *)(v_rip + 3841767), v_rbp, a3, a4);
    a2 = (*(unsigned __int64 *)(v_rip + 1942680)) - 1;
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 1942665));
    result = MiAddLoaderHalIoMappings(*(unsigned __int64 *)(v_rip + 1942665), a2, a3, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3109920))) != 0) {
        result = KdSetDbgPrintBufferSize((unsigned int)(*(unsigned int *)(v_rip + 3109920)), a2, a3, a4);
    }
    result = MiSetSlabAllocatorPolicy(v_rip + 1942908, a2, a3, a4);
    result = MiInitializeHotPatches(a2, a2, a3, a4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 28;
        result = MxInstallMoreMemory(a1, a2, a3, a4);
    }
    a1 = 0;
    result = MmInitializeImageViewExtension(a1, a2, a3, a4);
    result = MiInitializeKernelScp(a1, a2, a3, a4);
    if (sign_flag) {
        a1 = 29;
        result = MxInstallMoreMemory(a1, a2, a3, a4);
    }
    result = ExGenRandom((unsigned int)((unsigned int)(v_r14 + 1)), a2, a3, a4);
    result = (unsigned int)((result) & (3));
    *(unsigned __int64 *)(v_rip + 1902052) = (unsigned int)((unsigned int)(result));
    a1 = 0;
    *(unsigned int *)(v_rip + 1902045) = (unsigned int)(result * 8 + 8);
    result = KeQueryPerformanceCounter(a1, a2, a3, a4);
    *(unsigned __int64 *)(v_rip + 3841986) = result;
    if ((*(unsigned int *)(v_rip + 3565993)) >= = 2) {
        *(unsigned int *)(v_rip + 3565977) = 0;
    }
    if (((*(unsigned __int8 *)(v_rip + 3572162)) & (4)) == 0) goto loc_00C5E91B;
loc_00C5E8CB:
    if (0 >= ((unsigned int)(v_r14 + 1))) goto loc_00C5E906;
    a3 = 0;
    result = MiActOnLargeKernelHalPages(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 1892970 + 0 * 8 + 3584) + 48), v_rip + 45982, a3, a4);
    if (sign_flag) goto loc_00C5E8FB;
    v_rdi = (unsigned int)((0) + ((unsigned int)(v_r14 + 1)));
    goto loc_00C5E8CB;
loc_00C5E8FB:
    result = MxInstallMoreMemory(30, v_rip + 45982, a3, a4);
loc_00C5E906:
    if (((*(unsigned __int64 *)(v_rip + 3572087)) & (0x4000ULL)) != 0) {
    }
    result = MiCreateSlabAllocationsFromLoaderBlock(a2, v_rip + 45982, a3, a4);
    if (sign_flag) {
        a1 = 31;
        result = MxInstallMoreMemory(a1, v_rip + 45982, a3, a4);
    }
    result = MiInitializeSystemSpaceMap(a1, v_rip + 45982, a3, a4);
    a1 = 0;
    *(unsigned __int64 *)(v_rip + 1895880) = 0;
    *(unsigned __int64 *)(v_rip + 1906145) = 0;
    *(unsigned __int64 *)(v_rip + 1906154) = 0;
    result = KeQueryPerformanceCounter(a1, v_rip + 45982, a3, a4);
    *(unsigned __int64 *)(v_rip + 3841827) = result;
    result = MiInitializeBootKernelShadowStacks(a2, v_rip + 45982, a3, a4);
    result = MiInitializeSystemImageRegion(a2, v_rip + 45982, a3, a4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 32;
        result = MxInstallMoreMemory(a1, v_rip + 45982, a3, a4);
    }
    result = MiInitializeLoadedModuleList(a2, v_rip + 45982, a3, a4);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, v_rip + 45982, a3, a4);
    *(unsigned __int64 *)(v_rip + 3841787) = result;
    result = MiUpdateSharedUserDataNumberOfPages(a1, v_rip + 45982, a3, a4);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3565167) + 580) = 0;
    *(unsigned __int64 *)(v_rip + 1943435) = 0;
    result = MmConfigurePrefetchSeekThreshold(32, *(unsigned __int64 *)(v_rip + 3565167), a3, a4);
    result = PsSetPagePriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 5, a3, a4);
    a3 = 0;
    a2 = 0;
    result = MiEnumerateSystemImages(v_rip + 2937, a2, a3, a4);
    result = MmLockPagableDataSection(v_rip - 961637, a2, a3, a4);
    *(unsigned __int64 *)(v_rip + 3572236) = result;
    result = MmUnlockPagableImageSection(result, a2, a3, a4);
    result = MiAllocateDummyPage(result, a2, a3, a4);
    *(unsigned __int64 *)(v_rip + 1935923) = result;
    a3 = (result + result * 2) << (4);
    a3 = (a3) + (result);
    *(unsigned __int64 *)(v_rip + 1935878) = a3;
    result = MiReservePtes(v_rip + 1936455, (unsigned int)((unsigned int)(v_r14 + 1)), a3, a4);
    *(unsigned __int64 *)(v_rip + 3572178) = result;
    if (result == 0) {
        a1 = result + 33;
        result = MxInstallMoreMemory(a1, (unsigned int)((unsigned int)(v_r14 + 1)), a3, a4);
    }
    a1 = (a1) << (25);
    result = (result) << (25);
    a1 = (a1) - (result);
    a1 = (a1) >> (16);
    *(unsigned __int64 *)(v_rip + 3572129) = a1;
    result = MiInitializeRelocations(a1, (unsigned int)((unsigned int)(v_r14 + 1)), a3, a4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 34;
        result = MxInstallMoreMemory(a1, (unsigned int)((unsigned int)(v_r14 + 1)), a3, a4);
    }
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, (unsigned int)((unsigned int)(v_r14 + 1)), a3, a4);
    *(unsigned __int64 *)(v_rip + 3841553) = result;
    result = KeGetTbSize(a1, (unsigned int)((unsigned int)(v_r14 + 1)), a3, a4);
    *(unsigned __int64 *)(v_rip + 1897019) = v_rbp;
    v_rbx = result;
    if ((unsigned int)(result) == 0) { v_rbx = (unsigned int)((unsigned int)(0x800ULL)); }
    result = MiInitializeTbFlush((unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_r14 + 1)), a3, a4);
    if ((*(unsigned __int64 *)(v_rip + 1896992)) != ((unsigned int)((unsigned int)(v_rbx)))) goto loc_00C5EAC4;
    if (((unsigned int)(v_rbx)) != ((unsigned int)((unsigned int)(0x800ULL)))) {
        a1 = (unsigned int)((unsigned int)(0x800ULL));
        *(unsigned __int64 *)(v_rip + 1896977) = v_rbp;
        result = MiInitializeTbFlush(a1, (unsigned int)((unsigned int)(v_rbx)), a3, a4);
    }
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, (unsigned int)((unsigned int)(v_rbx)), a3, a4);
    *(unsigned __int64 *)(v_rip + 3841486) = result;
    result = MiInitializeMirroring(a1, (unsigned int)((unsigned int)(v_rbx)), a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00C5ED44;
    result = MxInstallMoreMemory(result + 44, (unsigned int)((unsigned int)(v_rbx)), a3, a4);
loc_00C5EAE8:
    if (((unsigned int)(result + 44)) != ((unsigned int)(v_rbx))) goto loc_00C5ED0A;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3564778) + 580) = 0x200000ULL;
    if (((*(unsigned __int64 *)(v_rip + 3571541)) & (0x4000ULL)) == 0) goto loc_00C5EB57;
    result = VslInitializeSecurePool(*(unsigned __int64 *)(v_rip + 1941829), *(unsigned __int64 *)(v_rip + 1941844), a3, a4);
    if (sign_flag) {
        a1 = 35;
        result = MxInstallMoreMemory(a1, *(unsigned __int64 *)(v_rip + 1941844), a3, a4);
    }
    result = MiSectionInitialization(a1, *(unsigned __int64 *)(v_rip + 1941844), a3, a4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 36;
        result = MxInstallMoreMemory(a1, *(unsigned __int64 *)(v_rip + 1941844), a3, a4);
    }
    result = MiInitializeCfg(a1, *(unsigned __int64 *)(v_rip + 1941844), a3, a4);
    if (sign_flag) {
        a1 = 37;
        result = MxInstallMoreMemory(a1, *(unsigned __int64 *)(v_rip + 1941844), a3, a4);
    }
    result = MiCreateEnclaveRegions(0, *(unsigned __int64 *)(v_rip + 1941844), a3, a4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 39;
        result = MxInstallMoreMemory(a1, *(unsigned __int64 *)(v_rip + 1941844), a3, a4);
    }
    *(unsigned __int64 *)(v_rip + 1905519) = 0;
    result = MiInitializeCacheFlushing(a1, *(unsigned __int64 *)(v_rip + 1941844), a3, a4);
    result = MiInitializeMemoryEvents(v_rip + 1941851, *(unsigned __int64 *)(v_rip + 1941844), a3, a4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 41;
        result = MxInstallMoreMemory(a1, *(unsigned __int64 *)(v_rip + 1941844), a3, a4);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3565132)))) <= 64) goto loc_00C5EBCC;
    goto loc_00C5EBD2;
loc_00C5EBCC:
    result = 64;
    if (64 == 0) {
        result = (unsigned int)(v_rbx);
    }
    result = (unsigned int)((result) << (8));
    *(unsigned int *)(v_rip + 3565105) = (unsigned int)(result);
    result = (unsigned int)(*(unsigned int *)(v_rip + 3565087));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3565087)))) & (0xFFFFFFF8ULL)) != 0) {
        result = 0;
        *(unsigned int *)(v_rip + 3565071) = (unsigned int)(result);
    }
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_00C5EC0B;
    *(unsigned int *)(v_rip + 1935245) = 16;
    *(unsigned int *)(v_rip + 1935239) = 8;
    goto loc_00C5EC15;
loc_00C5EC0B:
    *(unsigned int *)(v_rip + 1935223) = 4;
loc_00C5EC15:
    result = MiComputeMemoryNodeProcessorAssignments(a1, *(unsigned __int64 *)(v_rip + 1941844), a3, a4);
    *(unsigned __int16 *)(v_rip + 1905535) = 0;
    *(unsigned __int64 *)(v_rip + 1935640) = v_rip + 1935647;
    *(unsigned __int64 *)(v_rip + 1935618) = v_rip + 1935647;
    *(unsigned __int8 *)(v_rip + 1905497) = 6;
    *(unsigned __int64 *)(v_rip + 1905504) = v_rip + 1905510;
    *(unsigned __int64 *)(v_rip + 1905489) = v_rip + 1905510;
    *(unsigned __int64 *)(v_rip + 3840795) = v_rip - 4609942;
    *(unsigned int *)(v_rip + 1905464) = 0;
    *(unsigned __int64 *)(v_rip + 3840789) = 0;
    *(unsigned __int64 *)(v_rip + 3840758) = 0;
    result = ExQueueWorkItem(v_rip + 3840833, 3, a3, a4);
loc_00C5EC8A:
    if (0 >= 6) goto loc_00C5ECD9;
    v_stack_m68 = v_rip + 1941851;
    a4 = 0;
    a3 = 0;
    v_stack_m70 = *(unsigned __int64 *)(v_rsp + 0 * 8 + 72);
    v_stack_m78 = 0;
    result = PsCreateSystemThread(v_stack_m58, (unsigned int)(0x1FFFFFULL), a3, a4);
    if (sign_flag) goto loc_00C5ECCE;
    a2 = 0;
    result = ObCloseHandle(v_stack_m58, a2, a3, a4);
    v_rbp = (unsigned int)((0) + ((unsigned int)(v_rbx)));
    goto loc_00C5EC8A;
loc_00C5ECCE:
    result = MxInstallMoreMemory(43, a2, a3, a4);
loc_00C5ECD9:
    a3 = 0;
    a2 = 0;
    result = MiEnumerateSystemImages(v_rip - 4611475, a2, a3, a4);
    v_rbp = (v_rbp) | (-1);
    result = MiInitializeApiSets(0, a2, a3, a4);
    if (!sign_flag) goto loc_00C5ED44;
    result = MxInstallMoreMemory(v_rbp + 46, a2, a3, a4);
loc_00C5ED0A:
    if (((unsigned int)(v_rbp + 46)) == 2) {
        result = v_rip + 1935402;
        *(unsigned __int64 *)(v_rip + 1935403) = result;
        *(unsigned __int64 *)(v_rip + 1935388) = result;
        result = MiRegisterForHardwareAcceleratorChanges(v_rbp + 46, a2, a3, a4);
        a3 = 0;
        a1 = v_rip + 55965;
        a2 = 0;
        result = MiEnumerateSystemImages(a1, a2, a3, a4);
        result = MiFlushStrongCodeDriverLoadFailures(a1, a2, a3, a4);
        result = MiFlushDeferredRetpolineImageLoadEvents(a1, a2, a3, a4);
    }
    a1 = (v_stack_m20) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiInitSystem(int32_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rbp;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x1AC063)) ^ (local_rsp);
    v_stack_m20 = result;
    local_r14 = 0;
    *(uint64_t *)(local_rsp - 0x50) = v_rip - 6917055;
    *(uint64_t *)(local_rsp - 0x48) = v_rip - 6916346;
    *(uint64_t *)(local_rsp - 0x40) = v_rip - 9325637;
    *(uint64_t *)(local_rsp - 0x38) = v_rip - 6060432;
    *(uint64_t *)(local_rsp - 0x30) = v_rip - 8363659;
    *(uint64_t *)(local_rsp - 0x28) = v_rip - 8756326;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    if (Arg1 != 0) goto loc_00C5EAE8;
    result = Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00C5E75D;
    result = MiReservePtes(v_rip + 1937177, local_r14 + 1 + 31, Arg3, Arg4);
    goto loc_00C5E76F;
loc_00C5E75D:
    result = MiReservePtes(v_rip + 1937177, 257, Arg3, Arg4);
    *(uint32_t *)(v_rip + 0x1D1A51) = 257;
loc_00C5E76F:
    *(uint64_t *)(v_rip + 0x1D1A42) = result;
    result = MiInitializeWorkingSetManagerParameters(v_rip + 1942908, 257, Arg3, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 23;
        result = MxInstallMoreMemory(Arg1, 257, Arg3, Arg4);
    }
    result = ExInitializePagedHeaps(Arg1, 257, Arg3, Arg4);
    if (sign_flag) {
        Arg1 = 24;
        result = MxInstallMoreMemory(Arg1, 257, Arg3, Arg4);
    }
    Arg1 = 0;
    result = PsInitializeQuotaSystem(Arg1, 257, Arg3, Arg4);
    if ((uint8_t)(result) == 0) {
        Arg1 = 25;
        result = MxInstallMoreMemory(Arg1, 257, Arg3, Arg4);
    }
    result = MiGenerateSecureCookie(Arg1, 257, Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x1CF3B1) = result;
    *(uint32_t *)(v_rip + 0x1CF36F) = 0x12345678ULL;
    result = ExecuteHotpatchTestBootFunction(Arg1, 257, Arg3, Arg4);
    result = MiInitializeSharedUserData(Arg1, 257, Arg3, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 26;
        result = MxInstallMoreMemory(Arg1, 257, Arg3, Arg4);
    }
    result = MiInitializeBootProcess(Arg1, 257, Arg3, Arg4);
    if (sign_flag) {
        Arg1 = 27;
        result = MxInstallMoreMemory(Arg1, 257, Arg3, Arg4);
    }
    local_rbp = (local_rbp) | (-1);
    result = MI_FLUSH_ENTIRE_TB(local_rbp + 3, (uint32_t)((uint32_t)(local_rbp)), Arg3, Arg4);
    result = MiAddLoaderHalIoMappings(*(uint64_t *)(v_rip + 0x3A9EE7), local_rbp, Arg3, Arg4);
    Arg2 = (*(uint64_t *)(v_rip + 0x1DA498)) - 1;
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0x1DA489));
    result = MiAddLoaderHalIoMappings(*(uint64_t *)(v_rip + 0x1DA489), Arg2, Arg3, Arg4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x2F7420))) != 0) {
        result = KdSetDbgPrintBufferSize((uint32_t)(*(uint32_t *)(v_rip + 0x2F7420)), Arg2, Arg3, Arg4);
    }
    result = MiSetSlabAllocatorPolicy(v_rip + 1942908, Arg2, Arg3, Arg4);
    result = MiInitializeHotPatches(Arg2, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 28;
        result = MxInstallMoreMemory(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = 0;
    result = MmInitializeImageViewExtension(Arg1, Arg2, Arg3, Arg4);
    result = MiInitializeKernelScp(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) {
        Arg1 = 29;
        result = MxInstallMoreMemory(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExGenRandom((uint32_t)((uint32_t)(local_r14 + 1)), Arg2, Arg3, Arg4);
    result = (uint32_t)((result) & (3));
    *(uint64_t *)(v_rip + 0x1D05E4) = (uint32_t)((uint32_t)(result));
    Arg1 = 0;
    *(uint32_t *)(v_rip + 0x1D05DD) = (uint32_t)(result * 8 + 8);
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x3A9FC2) = result;
    if ((*(uint32_t *)(v_rip + 0x3669A9)) >= = 2) {
        *(uint32_t *)(v_rip + 0x366999) = 0;
    }
    if (((*(uint8_t *)(v_rip + 0x3681C2)) & (4)) == 0) goto loc_00C5E91B;
loc_00C5E8CB:
    if (0 >= ((uint32_t)(local_r14 + 1))) goto loc_00C5E906;
    Arg3 = 0;
    result = MiActOnLargeKernelHalPages(*(uint64_t *)(*(uint64_t *)(v_rip + 0x1CE26A + 0x0 * 8 + 0xE00) + 0x30), v_rip + 45982, Arg3, Arg4);
    if (sign_flag) goto loc_00C5E8FB;
    local_rdi = (uint32_t)((0) + ((uint32_t)(local_r14 + 1)));
    goto loc_00C5E8CB;
loc_00C5E8FB:
    result = MxInstallMoreMemory(30, v_rip + 45982, Arg3, Arg4);
loc_00C5E906:
    if (((*(uint64_t *)(v_rip + 0x368177)) & (0x4000ULL)) != 0) {
    }
    result = MiCreateSlabAllocationsFromLoaderBlock(Arg2, v_rip + 45982, Arg3, Arg4);
    if (sign_flag) {
        Arg1 = 31;
        result = MxInstallMoreMemory(Arg1, v_rip + 45982, Arg3, Arg4);
    }
    result = MiInitializeSystemSpaceMap(Arg1, v_rip + 45982, Arg3, Arg4);
    Arg1 = 0;
    *(uint64_t *)(v_rip + 0x1CEDC8) = 0;
    *(uint64_t *)(v_rip + 0x1D15E1) = 0;
    *(uint64_t *)(v_rip + 0x1D15EA) = 0;
    result = KeQueryPerformanceCounter(Arg1, v_rip + 45982, Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x3A9F23) = result;
    result = MiInitializeBootKernelShadowStacks(Arg2, v_rip + 45982, Arg3, Arg4);
    result = MiInitializeSystemImageRegion(Arg2, v_rip + 45982, Arg3, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 32;
        result = MxInstallMoreMemory(Arg1, v_rip + 45982, Arg3, Arg4);
    }
    result = MiInitializeLoadedModuleList(Arg2, v_rip + 45982, Arg3, Arg4);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, v_rip + 45982, Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x3A9EFB) = result;
    result = MiUpdateSharedUserDataNumberOfPages(Arg1, v_rip + 45982, Arg3, Arg4);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x36666F) + 0x244) = 0;
    *(uint64_t *)(v_rip + 0x1DA78B) = 0;
    result = MmConfigurePrefetchSeekThreshold(32, *(uint64_t *)(v_rip + 0x36666F), Arg3, Arg4);
    result = PsSetPagePriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), 5, Arg3, Arg4);
    Arg3 = 0;
    Arg2 = 0;
    result = MiEnumerateSystemImages(v_rip + 2937, Arg2, Arg3, Arg4);
    result = MmLockPagableDataSection(v_rip - 961637, Arg2, Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x36820C) = result;
    result = MmUnlockPagableImageSection(result, Arg2, Arg3, Arg4);
    result = MiAllocateDummyPage(result, Arg2, Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x1D8A33) = result;
    Arg3 = (result + result * 2) << (4);
    Arg3 = (Arg3) + (result);
    *(uint64_t *)(v_rip + 0x1D8A06) = Arg3;
    result = MiReservePtes(v_rip + 1936455, (uint32_t)((uint32_t)(local_r14 + 1)), Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x3681D2) = result;
    if (result == 0) {
        Arg1 = result + 33;
        result = MxInstallMoreMemory(Arg1, (uint32_t)((uint32_t)(local_r14 + 1)), Arg3, Arg4);
    }
    Arg1 = (Arg1) << (25);
    result = (result) << (25);
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (16);
    *(uint64_t *)(v_rip + 0x3681A1) = Arg1;
    result = MiInitializeRelocations(Arg1, (uint32_t)((uint32_t)(local_r14 + 1)), Arg3, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 34;
        result = MxInstallMoreMemory(Arg1, (uint32_t)((uint32_t)(local_r14 + 1)), Arg3, Arg4);
    }
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, (uint32_t)((uint32_t)(local_r14 + 1)), Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x3A9E11) = result;
    result = KeGetTbSize(Arg1, (uint32_t)((uint32_t)(local_r14 + 1)), Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x1CF23B) = local_rbp;
    local_rbx = result;
    if ((uint32_t)(result) == 0) { local_rbx = (uint32_t)((uint32_t)(0x800ULL)); }
    result = MiInitializeTbFlush((uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_r14 + 1)), Arg3, Arg4);
    if ((*(uint64_t *)(v_rip + 0x1CF220)) != ((uint32_t)((uint32_t)(local_rbx)))) goto loc_00C5EAC4;
    if (((uint32_t)(local_rbx)) != ((uint32_t)((uint32_t)(0x800ULL)))) {
        Arg1 = (uint32_t)((uint32_t)(0x800ULL));
        *(uint64_t *)(v_rip + 0x1CF211) = local_rbp;
        result = MiInitializeTbFlush(Arg1, (uint32_t)((uint32_t)(local_rbx)), Arg3, Arg4);
    }
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, (uint32_t)((uint32_t)(local_rbx)), Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x3A9DCE) = result;
    result = MiInitializeMirroring(Arg1, (uint32_t)((uint32_t)(local_rbx)), Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00C5ED44;
    result = MxInstallMoreMemory(result + 44, (uint32_t)((uint32_t)(local_rbx)), Arg3, Arg4);
loc_00C5EAE8:
    if (((uint32_t)(result + 44)) != ((uint32_t)(local_rbx))) goto loc_00C5ED0A;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x3664EA) + 0x244) = 0x200000ULL;
    if (((*(uint64_t *)(v_rip + 0x367F55)) & (0x4000ULL)) == 0) goto loc_00C5EB57;
    result = VslInitializeSecurePool(*(uint64_t *)(v_rip + 0x1DA145), *(uint64_t *)(v_rip + 0x1DA154), Arg3, Arg4);
    if (sign_flag) {
        Arg1 = 35;
        result = MxInstallMoreMemory(Arg1, *(uint64_t *)(v_rip + 0x1DA154), Arg3, Arg4);
    }
    result = MiSectionInitialization(Arg1, *(uint64_t *)(v_rip + 0x1DA154), Arg3, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 36;
        result = MxInstallMoreMemory(Arg1, *(uint64_t *)(v_rip + 0x1DA154), Arg3, Arg4);
    }
    result = MiInitializeCfg(Arg1, *(uint64_t *)(v_rip + 0x1DA154), Arg3, Arg4);
    if (sign_flag) {
        Arg1 = 37;
        result = MxInstallMoreMemory(Arg1, *(uint64_t *)(v_rip + 0x1DA154), Arg3, Arg4);
    }
    result = MiCreateEnclaveRegions(0, *(uint64_t *)(v_rip + 0x1DA154), Arg3, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 39;
        result = MxInstallMoreMemory(Arg1, *(uint64_t *)(v_rip + 0x1DA154), Arg3, Arg4);
    }
    *(uint64_t *)(v_rip + 0x1D136F) = 0;
    result = MiInitializeCacheFlushing(Arg1, *(uint64_t *)(v_rip + 0x1DA154), Arg3, Arg4);
    result = MiInitializeMemoryEvents(v_rip + 1941851, *(uint64_t *)(v_rip + 0x1DA154), Arg3, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 41;
        result = MxInstallMoreMemory(Arg1, *(uint64_t *)(v_rip + 0x1DA154), Arg3, Arg4);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x36664C)))) <= 64) goto loc_00C5EBCC;
    goto loc_00C5EBD2;
loc_00C5EBCC:
    result = 64;
    if (64 == 0) {
        result = (uint32_t)(local_rbx);
    }
    result = (uint32_t)((result) << (8));
    *(uint32_t *)(v_rip + 0x366631) = (uint32_t)(result);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x36661F));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x36661F)))) & (0xFFFFFFF8ULL)) != 0) {
        result = 0;
        *(uint32_t *)(v_rip + 0x36660F) = (uint32_t)(result);
    }
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_00C5EC0B;
    *(uint32_t *)(v_rip + 0x1D878D) = 16;
    *(uint32_t *)(v_rip + 0x1D8787) = 8;
    goto loc_00C5EC15;
loc_00C5EC0B:
    *(uint32_t *)(v_rip + 0x1D8777) = 4;
loc_00C5EC15:
    result = MiComputeMemoryNodeProcessorAssignments(Arg1, *(uint64_t *)(v_rip + 0x1DA154), Arg3, Arg4);
    *(uint16_t *)(v_rip + 0x1D137F) = 0;
    *(uint64_t *)(v_rip + 0x1D8918) = v_rip + 1935647;
    *(uint64_t *)(v_rip + 0x1D8902) = v_rip + 1935647;
    *(uint8_t *)(v_rip + 0x1D1359) = 6;
    *(uint64_t *)(v_rip + 0x1D1360) = v_rip + 1905510;
    *(uint64_t *)(v_rip + 0x1D1351) = v_rip + 1905510;
    *(uint64_t *)(v_rip + 0x3A9B1B) = v_rip - 4609942;
    *(uint32_t *)(v_rip + 0x1D1338) = 0;
    *(uint64_t *)(v_rip + 0x3A9B15) = 0;
    *(uint64_t *)(v_rip + 0x3A9AF6) = 0;
    result = ExQueueWorkItem(v_rip + 3840833, 3, Arg3, Arg4);
loc_00C5EC8A:
    if (0 >= 6) goto loc_00C5ECD9;
    v_stack_m68 = v_rip + 1941851;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_m70 = *(uint64_t *)(local_rsp + 0x0 * 8 + 0x48);
    v_stack_m78 = 0;
    result = PsCreateSystemThread(v_stack_m58, (uint32_t)(0x1FFFFFULL), Arg3, Arg4);
    if (sign_flag) goto loc_00C5ECCE;
    Arg2 = 0;
    result = ObCloseHandle(v_stack_m58, Arg2, Arg3, Arg4);
    local_rbp = (uint32_t)((0) + ((uint32_t)(local_rbx)));
    goto loc_00C5EC8A;
loc_00C5ECCE:
    result = MxInstallMoreMemory(43, Arg2, Arg3, Arg4);
loc_00C5ECD9:
    Arg3 = 0;
    Arg2 = 0;
    result = MiEnumerateSystemImages(v_rip - 4611475, Arg2, Arg3, Arg4);
    local_rbp = (local_rbp) | (-1);
    result = MiInitializeApiSets(0, Arg2, Arg3, Arg4);
    if (!sign_flag) goto loc_00C5ED44;
    result = MxInstallMoreMemory(local_rbp + 46, Arg2, Arg3, Arg4);
loc_00C5ED0A:
    if (((uint32_t)(local_rbp + 46)) == 2) {
        result = v_rip + 1935402;
        *(uint64_t *)(v_rip + 0x1D882B) = result;
        *(uint64_t *)(v_rip + 0x1D881C) = result;
        result = MiRegisterForHardwareAcceleratorChanges(local_rbp + 46, Arg2, Arg3, Arg4);
        Arg3 = 0;
        Arg1 = v_rip + 55965;
        Arg2 = 0;
        result = MiEnumerateSystemImages(Arg1, Arg2, Arg3, Arg4);
        result = MiFlushStrongCodeDriverLoadFailures(Arg1, Arg2, Arg3, Arg4);
        result = MiFlushDeferredRetpolineImageLoadEvents(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m20) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C5E6C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
