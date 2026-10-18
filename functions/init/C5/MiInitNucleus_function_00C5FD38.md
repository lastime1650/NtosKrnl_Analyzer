# MiInitNucleus

- RVA: `0x00C5FD38`–`0x00C605C4` (길이 `2,188` bytes)
- VA: `0x0000000140C5FD38`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D781C`
- 디코드: `517`개 명령, `2,188/2,188` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **79**; 고유 호출 대상: **56**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **63**

### Outgoing calls
- `0x00C5FD89` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C5FD8F` → [MiConstructLoaderMemoryTree](MiConstructLoaderMemoryTree_function_00C5F868.md) (function, `0x00C5F868`)
- `0x00C5FD96` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C5FDC8` → [MiCompensateForProcessorErrata](../C6/MiCompensateForProcessorErrata_function_00C68950.md) (function, `0x00C68950`)
- `0x00C5FDD7` → [MI_READ_PTE_LOCK_FREE](../../text/28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00C5FE11` → [MiExamineHalVa](MiExamineHalVa_function_00C5FAA4.md) (function, `0x00C5FAA4`)
- `0x00C5FE20` → [MiInitializeBootDefaults](MiInitializeBootDefaults_function_00C5ED70.md) (function, `0x00C5ED70`)
- `0x00C5FEA7` → [MiCountBootDriverRegions](../C6/MiCountBootDriverRegions_function_00C659B4.md) (function, `0x00C659B4`)
- `0x00C5FEB8` → [MiSystemVaTypeToVm](../../text/28/MiSystemVaTypeToVm_function_0028EB50.md) (function, `0x0028EB50`)
- `0x00C5FEE3` → [MiInitializeNumaRangesTemporary](MiInitializeNumaRangesTemporary_function_00C5E4D8.md) (function, `0x00C5E4D8`)
- `0x00C5FEE8` → [MiInitializeChannelRangesTemporary](../C6/MiInitializeChannelRangesTemporary_function_00C68424.md) (function, `0x00C68424`)
- `0x00C5FEF0` → [MiMemoryLicense](../C6/MiMemoryLicense_function_00C66E5C.md) (function, `0x00C66E5C`)
- `0x00C5FEF7` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C5FF06` → [MiRemoveLargeFreeLoaderDescriptors](../C6/MiRemoveLargeFreeLoaderDescriptors_function_00C6283C.md) (function, `0x00C6283C`)
- `0x00C5FF0D` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C5FF24` → [MiInitializeLoaderDescriptors](../C6/MiInitializeLoaderDescriptors_function_00C625B4.md) (function, `0x00C625B4`)
- `0x00C5FF2C` → [MiCheckLargePageOk](../C6/MiCheckLargePageOk_function_00C667E4.md) (function, `0x00C667E4`)
- `0x00C60003` → [MiCopyPfnEntryRaw](../../text/44/MiCopyPfnEntryRaw_function_00448500.md) (function, `0x00448500`)
- `0x00C60075` → [MxMarkValidMappings](../C6/MxMarkValidMappings_function_00C611C0.md) (function, `0x00C611C0`)
- `0x00C6007C` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C6008B` → [MiCreatePfnDatabase](MiCreatePfnDatabase_function_00C5F930.md) (function, `0x00C5F930`)
- `0x00C60092` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C600A1` → [MiInitializePfnsForValidMappings](../C6/MiInitializePfnsForValidMappings_function_00C6267C.md) (function, `0x00C6267C`)
- `0x00C600A8` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C600B7` → [MiSwitchToPfns](../C6/MiSwitchToPfns_function_00C62C90.md) (function, `0x00C62C90`)
- `0x00C600BE` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C6015D` → [MiInitializeSections](../../page/7F/MiInitializeSections_function_007FC738.md) (function, `0x007FC738`)
- `0x00C60165` → [MiInitializeCommitment](../../text/68/MiInitializeCommitment_function_0068CC08.md) (function, `0x0068CC08`)
- `0x00C6016A` → [MiInitializeDummyPages](../C6/MiInitializeDummyPages_function_00C605CC.md) (function, `0x00C605CC`)
- `0x00C6016F` → [MiInitializeSystemPtes](../C6/MiInitializeSystemPtes_function_00C6A998.md) (function, `0x00C6A998`)
- `0x00C6017A` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C60180` → [MiInitializeDebuggerSupport](../../text/68/MiInitializeDebuggerSupport_function_0068605C.md) (function, `0x0068605C`)
- `0x00C60185` → [MiProtectSharedUserPage](../C6/MiProtectSharedUserPage_function_00C60F44.md) (function, `0x00C60F44`)
- `0x00C6018A` → [MiInitializeNonPagedPool](../C6/MiInitializeNonPagedPool_function_00C64A24.md) (function, `0x00C64A24`)
- `0x00C60196` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C6019C` → [MiMapDummyPages](../C6/MiMapDummyPages_function_00C60A58.md) (function, `0x00C60A58`)
- `0x00C601A4` → [MiInitializeKasan](../C6/MiInitializeKasan_function_00C60810.md) (function, `0x00C60810`)
- `0x00C601AB` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C601C8` → [ExInitializePoolHeapManagement](../../text/65/ExInitializePoolHeapManagement_function_0065C3D0.md) (function, `0x0065C3D0`)
- `0x00C601D6` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C601DF` → [MiInitializePhysicalMemoryBlocks](../C6/MiInitializePhysicalMemoryBlocks_function_00C60920.md) (function, `0x00C60920`)
- `0x00C60230` → [MxZeroBootMappings](../C6/MxZeroBootMappings_function_00C61344.md) (function, `0x00C61344`)
- `0x00C6023A` → [MI_FLUSH_ENTIRE_TB](../../text/31/MI_FLUSH_ENTIRE_TB_function_00314110.md) (function, `0x00314110`)
- `0x00C60242` → [MiInitializeFunctionOverrides](../C6/MiInitializeFunctionOverrides_function_00C60788.md) (function, `0x00C60788`)
- `0x00C60247` → [MiInitializeDecayPfns](../C6/MiInitializeDecayPfns_function_00C6CC04.md) (function, `0x00C6CC04`)
- `0x00C6028C` → [ExAllocatePoolMm](../../text/35/ExAllocatePoolMm_function_0035B690.md) (function, `0x0035B690`)
- `0x00C602F3` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C602FB` → [MiGetAnyMultiplexedVm](../../text/44/MiGetAnyMultiplexedVm_function_00448BD0.md) (function, `0x00448BD0`)
- `0x00C60332` → [MiInitializeSystemWorkingSetList](../../page/7F/MiInitializeSystemWorkingSetList_function_007FB7D4.md) (function, `0x007FB7D4`)
- `0x00C60340` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C60357` → [MiInitializeSystemWorkingSetList](../../page/7F/MiInitializeSystemWorkingSetList_function_007FB7D4.md) (function, `0x007FB7D4`)
- `0x00C6035C` → [MiInitializeKernelStacks](../C6/MiInitializeKernelStacks_function_00C680B8.md) (function, `0x00C680B8`)
- `0x00C60368` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C6036E` → [MiInitializeNonCachedMappingRegion](../C6/MiInitializeNonCachedMappingRegion_function_00C6A738.md) (function, `0x00C6A738`)
- `0x00C6037A` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C60380` → [MiCreateTopLevelUltraMappings](../C6/MiCreateTopLevelUltraMappings_function_00C6CCB0.md) (function, `0x00C6CCB0`)
- `0x00C6038C` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C6039B` → [MmInitializeProcessor](../../pagelk/B7/MmInitializeProcessor_function_00B737F8.md) (function, `0x00B737F8`)
- `0x00C603A7` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C603AD` → [MiBuildSystemDataViews](../C6/MiBuildSystemDataViews_function_00C64DCC.md) (function, `0x00C64DCC`)
- `0x00C603B9` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C603E5` → [MiFillGapAddresses](../C6/MiFillGapAddresses_function_00C65A3C.md) (function, `0x00C65A3C`)
- `0x00C603F5` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C60403` → [MiFreeUnusedPfnPages](../../text/67/MiFreeUnusedPfnPages_function_006720C0.md) (function, `0x006720C0`)
- `0x00C6040A` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C60416` → [MiInitializePageFaultResources](../../text/67/MiInitializePageFaultResources_function_0067E490.md) (function, `0x0067E490`)
- `0x00C60422` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C60428` → [MiBuildPagedPool](../C6/MiBuildPagedPool_function_00C64918.md) (function, `0x00C64918`)
- `0x00C60434` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (function, `0x00671A04`)
- `0x00C60496` → [MiCreateHugeIoRanges](../C6/MiCreateHugeIoRanges_function_00C6437C.md) (function, `0x00C6437C`)
- `0x00C6049E` → [MiInitializeWsSwapping](../../page/80/MiInitializeWsSwapping_function_0080C60C.md) (function, `0x0080C60C`)
- `0x00C604CE` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00C604E8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C60514` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00C6052E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C60566` → [ExInitializeNPagedLookasideListInternal](../../text/46/ExInitializeNPagedLookasideListInternal_function_00468720.md) (function, `0x00468720`)
- `0x00C6056B` → [MiMeasureDemandCoalesceTimeBounds](../C6/MiMeasureDemandCoalesceTimeBounds_function_00C6A4FC.md) (function, `0x00C6A4FC`)
- `0x00C6059A` → [MiEnumerateSlabAllocatorsEx](../../text/47/MiEnumerateSlabAllocatorsEx_function_004746F8.md) (function, `0x004746F8`)
- `0x00C605BE` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)

### Direct callers
- [MmInitSystem](../BE/MmInitSystem_function_00BEE990.md) at `0x00BEEA41`

### Static image references
- `0x00C5FD4E` → RVA `0x00FC54D8` (`ALMOSTRO`; read)
- `0x00C5FD5F` → RVA `0x00E0A050` (`.data`; read)
- `0x00C5FD6B` → RVA `0x00E30248` (`.data`; read)
- `0x00C5FD9B` → RVA `0x01008808` (`INITDATA`; write)
- `0x00C5FDA7` → RVA `0x00E376F4` (`.data`; write)
- `0x00C5FDC1` → RVA `0x00E2DC41` (`.data`; write)
- `0x00C5FE19` → RVA `0x01008700` (`INITDATA`; write)
- `0x00C5FE25` → RVA `0x00E35E00` (`.data`; read)
- `0x00C5FE37` → RVA `0x00E388F0` (`.data`; read)
- `0x00C5FE3E` → RVA `0x00E35E00` (`.data`; write)
- `0x00C5FE61` → RVA `0x00E37280` (`.data`; read)
- `0x00C5FE73` → RVA `0x00E39688` (`.data`; read)
- `0x00C5FE7A` → RVA `0x00E39680` (`.data`; write)
- `0x00C5FE84` → RVA `0x00E39690` (`.data`; write)
- `0x00C5FE8B` → RVA `0x00E37300` (`.data`; write)
- `0x00C5FE93` → RVA `0x00E39688` (`.data`; write)
- `0x00C5FE9A` → RVA `0x00E39682` (`.data`; write)
- `0x00C5FEA1` → RVA `0x00E39684` (`.data`; write)
- `0x00C5FEB1` → RVA `0x00E38A60` (`.data`; write)
- `0x00C5FEFF` → RVA `0x01008810` (`INITDATA`; write)
- `0x00C5FF12` → RVA `0x00E2DCD0` (`.data`; read/write)
- `0x00C5FF1D` → RVA `0x01008818` (`INITDATA`; write)
- `0x00C5FF34` → RVA `0x00E2FF40` (`.data`; read)
- `0x00C5FF3B` → RVA `0x00E2FF60` (`.data`; read)
- `0x00C5FF65` → RVA `0x00E2FF50` (`.data`; read)
- `0x00C5FF73` → RVA `0x00E2FF60` (`.data`; write)
- `0x00C5FF99` → RVA `0x00E2FF68` (`.data`; read)
- `0x00C5FFAD` → RVA `0x00E2FF68` (`.data`; write)
- `0x00C5FFB4` → RVA `0x00E2FF58` (`.data`; read)
- `0x00C5FFCB` → RVA `0x00E2FF58` (`.data`; write)
- `0x00C5FFF5` → RVA `0x00E2FF70` (`.data`; read)
- `0x00C60008` → RVA `0x00E2FF88` (`.data`; read)
- `0x00C6001C` → RVA `0x00E2FF88` (`.data`; write)
- `0x00C60023` → RVA `0x00E2FF90` (`.data`; read)
- `0x00C60036` → RVA `0x00E2FF90` (`.data`; write)
- `0x00C60084` → RVA `0x01008820` (`INITDATA`; write)
- `0x00C6009A` → RVA `0x01008828` (`INITDATA`; write)
- `0x00C600B0` → RVA `0x01008830` (`INITDATA`; write)
- `0x00C600C3` → RVA `0x01008838` (`INITDATA`; write)
- `0x00C600CA` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x00C600D1` → RVA `0x00E2DCD8` (`.data`; write)
- `0x00C600E2` → RVA `0x00E2DBF8` (`.data`; read)
- `0x00C60153` → RVA `0x00E38D00` (`.data`; read)
- `0x00C601B0` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00C601C1` → RVA `0x01008840` (`INITDATA`; write)
- `0x00C6024C` → RVA `0x00E35D40` (`.data`; read)
- `0x00C60260` → RVA `0x00E35D40` (`.data`; write)
- `0x00C6030C` → RVA `0x00E38840` (`.data`; read)
- `0x00C6031C` → RVA `0x00E2D9C0` (`.data`; read)
- `0x00C60349` → RVA `0x00E38700` (`.data`; read)
- `0x00C603BF` → RVA `0x00E2DCE0` (`.data`; read)
- `0x00C603EA` → RVA `0x00FC6A88` (`ALMOSTRO`; read/write)
- `0x00C603FC` → RVA `0x01008848` (`INITDATA`; write)
- `0x00C6040F` → RVA `0x01008850` (`INITDATA`; write)
- `0x00C604A3` → RVA `0x00E2DC00` (`.data`; read)
- `0x00C604AF` → RVA `0x00E2DC20` (`.data`; read)
- `0x00C604B8` → RVA `0x00E2DBC4` (`.data`; read)
- `0x00C604ED` → RVA `0x00E2DC20` (`.data`; write)
- `0x00C604F4` → RVA `0x00E2DC28` (`.data`; read)
- `0x00C604FD` → RVA `0x00E2DBCB` (`.data`; read)
- `0x00C60533` → RVA `0x00E2DC28` (`.data`; write)
- `0x00C6053E` → RVA `0x00E35D80` (`.data`; read)
- `0x00C60589` → RVA `0x0068E830` (`MiInitialSlabPopulate`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **46**
  - `0x00C5FD89` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C5FD96` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C5FDD7` → [MI_READ_PTE_LOCK_FREE](../../text/28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (`INIT` → `.text`)
  - `0x00C5FEB8` → [MiSystemVaTypeToVm](../../text/28/MiSystemVaTypeToVm_function_0028EB50.md) (`INIT` → `.text`)
  - `0x00C5FEF7` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C5FF0D` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C60003` → [MiCopyPfnEntryRaw](../../text/44/MiCopyPfnEntryRaw_function_00448500.md) (`INIT` → `.text`)
  - `0x00C6007C` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C60092` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C600A8` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C600BE` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C6015D` → [MiInitializeSections](../../page/7F/MiInitializeSections_function_007FC738.md) (`INIT` → `PAGE`)
  - `0x00C60165` → [MiInitializeCommitment](../../text/68/MiInitializeCommitment_function_0068CC08.md) (`INIT` → `.text`)
  - `0x00C6017A` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C60180` → [MiInitializeDebuggerSupport](../../text/68/MiInitializeDebuggerSupport_function_0068605C.md) (`INIT` → `.text`)
  - `0x00C60196` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C601AB` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C601C8` → [ExInitializePoolHeapManagement](../../text/65/ExInitializePoolHeapManagement_function_0065C3D0.md) (`INIT` → `.text`)
  - `0x00C601D6` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C6023A` → [MI_FLUSH_ENTIRE_TB](../../text/31/MI_FLUSH_ENTIRE_TB_function_00314110.md) (`INIT` → `.text`)
  - `0x00C6028C` → [ExAllocatePoolMm](../../text/35/ExAllocatePoolMm_function_0035B690.md) (`INIT` → `.text`)
  - `0x00C602F3` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C602FB` → [MiGetAnyMultiplexedVm](../../text/44/MiGetAnyMultiplexedVm_function_00448BD0.md) (`INIT` → `.text`)
  - `0x00C60332` → [MiInitializeSystemWorkingSetList](../../page/7F/MiInitializeSystemWorkingSetList_function_007FB7D4.md) (`INIT` → `PAGE`)
  - `0x00C60340` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C60357` → [MiInitializeSystemWorkingSetList](../../page/7F/MiInitializeSystemWorkingSetList_function_007FB7D4.md) (`INIT` → `PAGE`)
  - `0x00C60368` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C6037A` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C6038C` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C6039B` → [MmInitializeProcessor](../../pagelk/B7/MmInitializeProcessor_function_00B737F8.md) (`INIT` → `PAGELK`)
  - `0x00C603A7` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C603B9` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C603F5` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C60403` → [MiFreeUnusedPfnPages](../../text/67/MiFreeUnusedPfnPages_function_006720C0.md) (`INIT` → `.text`)
  - `0x00C6040A` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C60416` → [MiInitializePageFaultResources](../../text/67/MiInitializePageFaultResources_function_0067E490.md) (`INIT` → `.text`)
  - `0x00C60422` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C60434` → [MxInstallMoreMemory](../../text/67/MxInstallMoreMemory_function_00671A04.md) (`INIT` → `.text`)
  - `0x00C6049E` → [MiInitializeWsSwapping](../../page/80/MiInitializeWsSwapping_function_0080C60C.md) (`INIT` → `PAGE`)
  - `0x00C604CE` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`INIT` → `.text`)
  - `0x00C604E8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C60514` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`INIT` → `.text`)
  - `0x00C6052E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C60566` → [ExInitializeNPagedLookasideListInternal](../../text/46/ExInitializeNPagedLookasideListInternal_function_00468720.md) (`INIT` → `.text`)
  - `0x00C6059A` → [MiEnumerateSlabAllocatorsEx](../../text/47/MiEnumerateSlabAllocatorsEx_function_004746F8.md) (`INIT` → `.text`)
  - `0x00C605BE` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C5FD38  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C5FD3D  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00C5FD42  56                              push rsi
00C5FD43  57                              push rdi
00C5FD44  41 54                           push r12
00C5FD46  41 55                           push r13
00C5FD48  41 56                           push r14
00C5FD4A  48 83 EC 40                     sub rsp, 0x40
00C5FD4E  48 8D 05 83 57 36 00            lea rax, [rip + 0x365783]
00C5FD55  33 F6                           xor esi, esi
00C5FD57  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00C5FD5C  48 8B F9                        mov rdi, rcx
00C5FD5F  48 8D 05 EA A2 1A 00            lea rax, [rip + 0x1aa2ea]
00C5FD66  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00C5FD6B  48 63 05 D6 04 1D 00            movsxd rax, dword ptr [rip + 0x1d04d6]
00C5FD72  85 C0                           test eax, eax
00C5FD74  74 19                           je 0x140c5fd8f
00C5FD76  4C 8B C0                        mov r8, rax
00C5FD79  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00C5FD7E  45 33 C9                        xor r9d, r9d
00C5FD81  8D 4E 1A                        lea ecx, [rsi + 0x1a]
00C5FD84  BA 00 03 00 00                  mov edx, 0x300
00C5FD89  E8 D2 D8 89 FF                  call 0x1404fd660
00C5FD8E  CC                              int3
00C5FD8F  E8 D4 FA FF FF                  call 0x140c5f868
00C5FD94  33 C9                           xor ecx, ecx
00C5FD96  E8 45 EA 71 FF                  call 0x14037e7e0
00C5FD9B  48 89 05 66 8A 3A 00            mov qword ptr [rip + 0x3a8a66], rax
00C5FDA2  BD 01 00 00 00                  mov ebp, 1
00C5FDA7  C6 05 46 79 1D 00 04            mov byte ptr [rip + 0x1d7946], 4
00C5FDAE  48 8B CF                        mov rcx, rdi
00C5FDB1  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00C5FDBA  40 38 A8 8D 00 00 00            cmp byte ptr [rax + 0x8d], bpl
00C5FDC1  0F 94 05 79 DE 1C 00            sete byte ptr [rip + 0x1cde79]
00C5FDC8  E8 83 8B 00 00                  call 0x140c68950
00C5FDCD  48 B9 68 DF BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbedf68
00C5FDD7  E8 C4 2A 62 FF                  call 0x1402828a0
00C5FDDC  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00C5FDE6  48 C1 E8 0C                     shr rax, 0xc
00C5FDEA  48 23 C1                        and rax, rcx
00C5FDED  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00C5FDF6  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
00C5FDFD  0F 20 D9                        mov rcx, cr3
00C5FE00  81 E1 FF 0F 00 00               and ecx, 0xfff
00C5FE06  48 C1 E0 0C                     shl rax, 0xc
00C5FE0A  48 0B C8                        or rcx, rax
00C5FE0D  48 89 4A 28                     mov qword ptr [rdx + 0x28], rcx
00C5FE11  E8 8E FC FF FF                  call 0x140c5faa4
00C5FE16  48 8B CF                        mov rcx, rdi
00C5FE19  48 89 05 E0 88 3A 00            mov qword ptr [rip + 0x3a88e0], rax
00C5FE20  E8 4B EF FF FF                  call 0x140c5ed70
00C5FE25  48 8D 05 D4 5F 1D 00            lea rax, [rip + 0x1d5fd4]
00C5FE2C  A8 0F                           test al, 0xf
00C5FE2E  0F 85 85 07 00 00               jne 0x140c605b9
00C5FE34  0F 57 C0                        xorps xmm0, xmm0
00C5FE37  48 8D 05 B2 8A 1D 00            lea rax, [rip + 0x1d8ab2]
00C5FE3E  0F 29 05 BB 5F 1D 00            movaps xmmword ptr [rip + 0x1d5fbb], xmm0
00C5FE45  8D 4D 0F                        lea ecx, [rbp + 0xf]
00C5FE48  48 89 40 08                     mov qword ptr [rax + 8], rax
00C5FE4C  48 89 00                        mov qword ptr [rax], rax
00C5FE4F  48 83 C0 10                     add rax, 0x10
00C5FE53  48 2B CD                        sub rcx, rbp
00C5FE56  75 F0                           jne 0x140c5fe48
00C5FE58  8D 59 02                        lea ebx, [rcx + 2]
00C5FE5B  8B CB                           mov ecx, ebx
00C5FE5D  44 8D 6B 3E                     lea r13d, [rbx + 0x3e]
00C5FE61  48 8D 05 18 74 1D 00            lea rax, [rip + 0x1d7418]
00C5FE68  48 89 30                        mov qword ptr [rax], rsi
00C5FE6B  49 03 C5                        add rax, r13
00C5FE6E  48 2B CD                        sub rcx, rbp
00C5FE71  75 F5                           jne 0x140c5fe68
00C5FE73  48 8D 05 0E 98 1D 00            lea rax, [rip + 0x1d980e]
00C5FE7A  66 89 35 FF 97 1D 00            mov word ptr [rip + 0x1d97ff], si
00C5FE81  0F 57 C0                        xorps xmm0, xmm0
00C5FE84  48 89 05 05 98 1D 00            mov qword ptr [rip + 0x1d9805], rax
00C5FE8B  66 0F 7F 05 6D 74 1D 00         movdqa xmmword ptr [rip + 0x1d746d], xmm0
00C5FE93  48 89 05 EE 97 1D 00            mov qword ptr [rip + 0x1d97ee], rax
00C5FE9A  C6 05 E1 97 1D 00 06            mov byte ptr [rip + 0x1d97e1], 6
00C5FEA1  89 35 DD 97 1D 00               mov dword ptr [rip + 0x1d97dd], esi
00C5FEA7  E8 08 5B 00 00                  call 0x140c659b4
00C5FEAC  B9 0B 00 00 00                  mov ecx, 0xb
00C5FEB1  48 89 05 A8 8B 1D 00            mov qword ptr [rip + 0x1d8ba8], rax
00C5FEB8  E8 93 EC 62 FF                  call 0x14028eb50
00C5FEBD  41 BC 03 00 00 00               mov r12d, 3
00C5FEC3  8B 88 B8 00 00 00               mov ecx, dword ptr [rax + 0xb8]
00C5FEC9  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
00C5FECD  80 E1 F3                        and cl, 0xf3
00C5FED0  41 0A CC                        or cl, r12b
00C5FED3  88 4C 24 78                     mov byte ptr [rsp + 0x78], cl
00C5FED7  0F B7 4C 24 78                  movzx ecx, word ptr [rsp + 0x78]
00C5FEDC  66 89 88 B8 00 00 00            mov word ptr [rax + 0xb8], cx
00C5FEE3  E8 F0 E5 FF FF                  call 0x140c5e4d8
00C5FEE8  E8 37 85 00 00                  call 0x140c68424
00C5FEED  48 8B CF                        mov rcx, rdi
00C5FEF0  E8 67 6F 00 00                  call 0x140c66e5c
00C5FEF5  33 C9                           xor ecx, ecx
00C5FEF7  E8 E4 E8 71 FF                  call 0x14037e7e0
00C5FEFC  48 8B CF                        mov rcx, rdi
00C5FEFF  48 89 05 0A 89 3A 00            mov qword ptr [rip + 0x3a890a], rax
00C5FF06  E8 31 29 00 00                  call 0x140c6283c
00C5FF0B  33 C9                           xor ecx, ecx
00C5FF0D  E8 CE E8 71 FF                  call 0x14037e7e0
00C5FF12  48 83 0D B6 DD 1C 00 FF         or qword ptr [rip + 0x1cddb6], 0xffffffffffffffff
00C5FF1A  48 8B CF                        mov rcx, rdi
00C5FF1D  48 89 05 F4 88 3A 00            mov qword ptr [rip + 0x3a88f4], rax
00C5FF24  E8 8B 26 00 00                  call 0x140c625b4
00C5FF29  48 8B CF                        mov rcx, rdi
00C5FF2C  E8 B3 68 00 00                  call 0x140c667e4
00C5FF31  0F 57 C0                        xorps xmm0, xmm0
00C5FF34  48 8D 15 05 00 1D 00            lea rdx, [rip + 0x1d0005]
00C5FF3B  0F 11 05 1E 00 1D 00            movups xmmword ptr [rip + 0x1d001e], xmm0
00C5FF42  8B 05 18 00 1D 00               mov eax, dword ptr [rip + 0x1d0018]
00C5FF48  48 B9 00 00 00 00 00 00 40 00   movabs rcx, 0x40000000000000
00C5FF52  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
00C5FF56  C1 E8 10                        shr eax, 0x10
00C5FF59  24 FE                           and al, 0xfe
00C5FF5B  0C 06                           or al, 6
00C5FF5D  88 44 24 7A                     mov byte ptr [rsp + 0x7a], al
00C5FF61  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00C5FF65  0F 11 05 E4 FF 1C 00            movups xmmword ptr [rip + 0x1cffe4], xmm0
00C5FF6C  0F 11 05 CD FF 1C 00            movups xmmword ptr [rip + 0x1cffcd], xmm0
00C5FF73  89 05 E7 FF 1C 00               mov dword ptr [rip + 0x1cffe7], eax
00C5FF79  8B 05 E1 FF 1C 00               mov eax, dword ptr [rip + 0x1cffe1]
00C5FF7F  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
00C5FF83  C1 E8 10                        shr eax, 0x10
00C5FF86  24 3F                           and al, 0x3f
00C5FF88  41 0A C5                        or al, r13b
00C5FF8B  88 44 24 7A                     mov byte ptr [rsp + 0x7a], al
00C5FF8F  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00C5FF93  89 05 C7 FF 1C 00               mov dword ptr [rip + 0x1cffc7], eax
00C5FF99  48 8B 05 C8 FF 1C 00            mov rax, qword ptr [rip + 0x1cffc8]
00C5FFA0  48 0B C1                        or rax, rcx
00C5FFA3  48 B9 01 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000001
00C5FFAD  48 89 05 B4 FF 1C 00            mov qword ptr [rip + 0x1cffb4], rax
00C5FFB4  48 8B 05 9D FF 1C 00            mov rax, qword ptr [rip + 0x1cff9d]
00C5FFBB  48 23 C1                        and rax, rcx
00C5FFBE  48 B9 00 00 00 00 00 01 00 00   movabs rcx, 0x10000000000
00C5FFC8  48 0B C5                        or rax, rbp
00C5FFCB  48 89 05 86 FF 1C 00            mov qword ptr [rip + 0x1cff86], rax
00C5FFD2  8B 05 88 FF 1C 00               mov eax, dword ptr [rip + 0x1cff88]
00C5FFD8  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
00C5FFDC  66 89 5C 24 78                  mov word ptr [rsp + 0x78], bx
00C5FFE1  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00C5FFE5  89 05 75 FF 1C 00               mov dword ptr [rip + 0x1cff75], eax
00C5FFEB  48 8B 05 76 FF 1C 00            mov rax, qword ptr [rip + 0x1cff76]
00C5FFF2  48 0B C1                        or rax, rcx
00C5FFF5  48 8D 0D 74 FF 1C 00            lea rcx, [rip + 0x1cff74]
00C5FFFC  48 89 05 65 FF 1C 00            mov qword ptr [rip + 0x1cff65], rax
00C60003  E8 F8 84 7E FF                  call 0x140448500
00C60008  4C 8B 0D 79 FF 1C 00            mov r9, qword ptr [rip + 0x1cff79]
00C6000F  48 B8 00 00 00 00 00 00 00 C0   movabs rax, 0xc000000000000000
00C60019  4C 23 C8                        and r9, rax
00C6001C  4C 89 0D 65 FF 1C 00            mov qword ptr [rip + 0x1cff65], r9
00C60023  8B 05 67 FF 1C 00               mov eax, dword ptr [rip + 0x1cff67]
00C60029  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
00C6002D  66 89 74 24 78                  mov word ptr [rsp + 0x78], si
00C60032  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00C60036  89 05 54 FF 1C 00               mov dword ptr [rip + 0x1cff54], eax
00C6003C  8B 05 4E FF 1C 00               mov eax, dword ptr [rip + 0x1cff4e]
00C60042  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
00C60046  C1 E8 10                        shr eax, 0x10
00C60049  24 FD                           and al, 0xfd
00C6004B  0C 05                           or al, 5
00C6004D  88 44 24 7A                     mov byte ptr [rsp + 0x7a], al
00C60051  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00C60055  89 05 35 FF 1C 00               mov dword ptr [rip + 0x1cff35], eax
00C6005B  48 BA F8 DF BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbedff8
00C60065  48 B9 00 D8 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed800
00C6006F  4C 8B CF                        mov r9, rdi
00C60072  45 8B C4                        mov r8d, r12d
00C60075  E8 46 11 00 00                  call 0x140c611c0
00C6007A  33 C9                           xor ecx, ecx
00C6007C  E8 5F E7 71 FF                  call 0x14037e7e0
00C60081  48 8B CF                        mov rcx, rdi
00C60084  48 89 05 95 87 3A 00            mov qword ptr [rip + 0x3a8795], rax
00C6008B  E8 A0 F8 FF FF                  call 0x140c5f930
00C60090  33 C9                           xor ecx, ecx
00C60092  E8 49 E7 71 FF                  call 0x14037e7e0
00C60097  48 8B CF                        mov rcx, rdi
00C6009A  48 89 05 87 87 3A 00            mov qword ptr [rip + 0x3a8787], rax
00C600A1  E8 D6 25 00 00                  call 0x140c6267c
00C600A6  33 C9                           xor ecx, ecx
00C600A8  E8 33 E7 71 FF                  call 0x14037e7e0
00C600AD  48 8B CF                        mov rcx, rdi
00C600B0  48 89 05 79 87 3A 00            mov qword ptr [rip + 0x3a8779], rax
00C600B7  E8 D4 2B 00 00                  call 0x140c62c90
00C600BC  33 C9                           xor ecx, ecx
00C600BE  E8 1D E7 71 FF                  call 0x14037e7e0
00C600C3  48 89 05 6E 87 3A 00            mov qword ptr [rip + 0x3a876e], rax
00C600CA  0F B7 05 2F 4F 36 00            movzx eax, word ptr [rip + 0x364f2f]
00C600D1  40 88 35 00 DC 1C 00            mov byte ptr [rip + 0x1cdc00], sil
00C600D8  85 C0                           test eax, eax
00C600DA  74 77                           je 0x140c60153
00C600DC  48 8B CE                        mov rcx, rsi
00C600DF  44 8B D0                        mov r10d, eax
00C600E2  4C 8B 05 0F DB 1C 00            mov r8, qword ptr [rip + 0x1cdb0f]
00C600E9  8B C6                           mov eax, esi
00C600EB  4D 8D 48 78                     lea r9, [r8 + 0x78]
00C600EF  4C 03 C9                        add r9, rcx
00C600F2  49 8B D1                        mov rdx, r9
00C600F5  89 02                           mov dword ptr [rdx], eax
00C600F7  89 42 04                        mov dword ptr [rdx + 4], eax
00C600FA  89 42 08                        mov dword ptr [rdx + 8], eax
00C600FD  89 42 0C                        mov dword ptr [rdx + 0xc], eax
00C60100  48 8D 52 10                     lea rdx, [rdx + 0x10]
00C60104  03 C5                           add eax, ebp
00C60106  41 3B C4                        cmp eax, r12d
00C60109  72 EA                           jb 0x140c600f5
00C6010B  49 8D 90 A8 00 00 00            lea rdx, [r8 + 0xa8]
00C60112  8B C6                           mov eax, esi
00C60114  48 03 D1                        add rdx, rcx
00C60117  89 02                           mov dword ptr [rdx], eax
00C60119  03 C5                           add eax, ebp
00C6011B  48 8D 52 04                     lea rdx, [rdx + 4]
00C6011F  41 3B C4                        cmp eax, r12d
00C60122  72 F3                           jb 0x140c60117
00C60124  49 8D 90 84 00 00 00            lea rdx, [r8 + 0x84]
00C6012B  42 89 9C 01 B4 00 00 00         mov dword ptr [rcx + r8 + 0xb4], ebx
00C60133  48 03 D1                        add rdx, rcx
00C60136  8B C6                           mov eax, esi
00C60138  03 C5                           add eax, ebp
00C6013A  4D 8D 49 04                     lea r9, [r9 + 4]
00C6013E  48 8D 52 10                     lea rdx, [rdx + 0x10]
00C60142  41 3B C4                        cmp eax, r12d
00C60145  72 F1                           jb 0x140c60138
00C60147  48 81 C1 80 01 00 00            add rcx, 0x180
00C6014E  4C 2B D5                        sub r10, rbp
00C60151  75 8F                           jne 0x140c600e2
00C60153  4C 8D 35 A6 8B 1D 00            lea r14, [rip + 0x1d8ba6]
00C6015A  49 8B CE                        mov rcx, r14
00C6015D  E8 D6 C5 B9 FF                  call 0x1407fc738
00C60162  49 8B CE                        mov rcx, r14
00C60165  E8 9E CA A2 FF                  call 0x14068cc08
00C6016A  E8 5D 04 00 00                  call 0x140c605cc
00C6016F  E8 24 A8 00 00                  call 0x140c6a998
00C60174  85 C0                           test eax, eax
00C60176  75 08                           jne 0x140c60180
00C60178  8B CD                           mov ecx, ebp
00C6017A  E8 85 18 A1 FF                  call 0x140671a04
00C6017F  CC                              int3
00C60180  E8 D7 5E A2 FF                  call 0x14068605c
00C60185  E8 BA 0D 00 00                  call 0x140c60f44
00C6018A  E8 95 48 00 00                  call 0x140c64a24
00C6018F  85 C0                           test eax, eax
00C60191  75 09                           jne 0x140c6019c
00C60193  8D 48 05                        lea ecx, [rax + 5]
00C60196  E8 69 18 A1 FF                  call 0x140671a04
00C6019B  CC                              int3
00C6019C  E8 B7 08 00 00                  call 0x140c60a58
00C601A1  48 8B CF                        mov rcx, rdi
00C601A4  E8 67 06 00 00                  call 0x140c60810
00C601A9  33 C9                           xor ecx, ecx
00C601AB  E8 30 E6 71 FF                  call 0x14037e7e0
00C601B0  48 8B 0D D1 68 36 00            mov rcx, qword ptr [rip + 0x3668d1]
00C601B7  48 C1 E9 05                     shr rcx, 5
00C601BB  81 E1 00 04 00 00               and ecx, 0x400
00C601C1  48 89 05 78 86 3A 00            mov qword ptr [rip + 0x3a8678], rax
00C601C8  E8 03 C2 9F FF                  call 0x14065c3d0
00C601CD  85 C0                           test eax, eax
00C601CF  79 0B                           jns 0x140c601dc
00C601D1  B9 0B 00 00 00                  mov ecx, 0xb
00C601D6  E8 29 18 A1 FF                  call 0x140671a04
00C601DB  CC                              int3
00C601DC  48 8B CF                        mov rcx, rdi
00C601DF  E8 3C 07 00 00                  call 0x140c60920
00C601E4  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
00C601EE  49 8B C9                        mov rcx, r9
00C601F1  49 8B D1                        mov rdx, r9
00C601F4  48 B8 00 00 00 00 40 00 00 00   movabs rax, 0x4000000000
00C601FE  4D 8B C4                        mov r8, r12
00C60201  48 03 D0                        add rdx, rax
00C60204  49 BA F8 FF FF FF 7F 00 00 00   movabs r10, 0x7ffffffff8
00C6020E  48 C1 E9 09                     shr rcx, 9
00C60212  49 23 CA                        and rcx, r10
00C60215  49 8B C1                        mov rax, r9
00C60218  48 C1 EA 09                     shr rdx, 9
00C6021C  48 03 C8                        add rcx, rax
00C6021F  49 23 D2                        and rdx, r10
00C60222  49 8B C1                        mov rax, r9
00C60225  48 03 D0                        add rdx, rax
00C60228  4C 2B C5                        sub r8, rbp
00C6022B  75 E1                           jne 0x140c6020e
00C6022D  45 8B C4                        mov r8d, r12d
00C60230  E8 0F 11 00 00                  call 0x140c61344
00C60235  83 CA FF                        or edx, 0xffffffff
00C60238  8B CD                           mov ecx, ebp
00C6023A  E8 D1 3E 6B FF                  call 0x140314110
00C6023F  48 8B CF                        mov rcx, rdi
00C60242  E8 41 05 00 00                  call 0x140c60788
00C60247  E8 B8 C9 00 00                  call 0x140c6cc04
00C6024C  48 8D 05 ED 5A 1D 00            lea rax, [rip + 0x1d5aed]
00C60253  A8 0F                           test al, 0xf
00C60255  0F 85 5E 03 00 00               jne 0x140c605b9
00C6025B  0F 57 C0                        xorps xmm0, xmm0
00C6025E  8B DE                           mov ebx, esi
00C60260  0F 29 05 D9 5A 1D 00            movaps xmmword ptr [rip + 0x1d5ad9], xmm0
00C60267  0F B7 05 92 4D 36 00            movzx eax, word ptr [rip + 0x364d92]
00C6026E  3B D8                           cmp ebx, eax
00C60270  0F 83 83 00 00 00               jae 0x140c602f9
00C60276  44 8B CB                        mov r9d, ebx
00C60279  BA 40 03 00 00                  mov edx, 0x340
00C6027E  41 0F BA E9 1F                  bts r9d, 0x1f
00C60283  41 B8 4D 69 49 6F               mov r8d, 0x6f49694d
00C60289  49 8B CD                        mov rcx, r13
00C6028C  E8 FF B3 6F FF                  call 0x14035b690
00C60291  48 8B D0                        mov rdx, rax
00C60294  48 85 C0                        test rax, rax
00C60297  74 55                           je 0x140c602ee
00C60299  48 8D 88 88 02 00 00            lea rcx, [rax + 0x288]
00C602A0  B8 04 00 00 00                  mov eax, 4
00C602A5  48 89 71 10                     mov qword ptr [rcx + 0x10], rsi
00C602A9  48 89 49 08                     mov qword ptr [rcx + 8], rcx
00C602AD  48 89 09                        mov qword ptr [rcx], rcx
00C602B0  48 83 C1 20                     add rcx, 0x20
00C602B4  48 2B C5                        sub rax, rbp
00C602B7  75 EC                           jne 0x140c602a5
00C602B9  48 89 B2 18 03 00 00            mov qword ptr [rdx + 0x318], rsi
00C602C0  48 8D 82 08 03 00 00            lea rax, [rdx + 0x308]
00C602C7  48 89 40 08                     mov qword ptr [rax + 8], rax
00C602CB  48 89 00                        mov qword ptr [rax], rax
00C602CE  8B C3                           mov eax, ebx
00C602D0  48 8D 0C 40                     lea rcx, [rax + rax*2]
00C602D4  48 8B 05 1D D9 1C 00            mov rax, qword ptr [rip + 0x1cd91d]
00C602DB  48 C1 E1 07                     shl rcx, 7
00C602DF  03 DD                           add ebx, ebp
00C602E1  48 89 94 01 78 01 00 00         mov qword ptr [rcx + rax + 0x178], rdx
00C602E9  E9 79 FF FF FF                  jmp 0x140c60267
00C602EE  B9 0C 00 00 00                  mov ecx, 0xc
00C602F3  E8 0C 17 A1 FF                  call 0x140671a04
00C602F8  CC                              int3
00C602F9  8B CD                           mov ecx, ebp
00C602FB  E8 D0 88 7E FF                  call 0x140448bd0
00C60300  8B 88 B8 00 00 00               mov ecx, dword ptr [rax + 0xb8]
00C60306  80 E1 0F                        and cl, 0xf
00C60309  40 3A CD                        cmp cl, bpl
00C6030C  48 8D 0D 2D 85 1D 00            lea rcx, [rip + 0x1d852d]
00C60313  74 07                           je 0x140c6031c
00C60315  48 8D 88 C0 00 00 00            lea rcx, [rax + 0xc0]
00C6031C  48 8D 15 9D D6 1C 00            lea rdx, [rip + 0x1cd69d]
00C60323  45 33 C9                        xor r9d, r9d
00C60326  48 89 11                        mov qword ptr [rcx], rdx
00C60329  45 8B C4                        mov r8d, r12d
00C6032C  48 8B D0                        mov rdx, rax
00C6032F  49 8B CE                        mov rcx, r14
00C60332  E8 9D B4 B9 FF                  call 0x1407fb7d4
00C60337  85 C0                           test eax, eax
00C60339  79 0B                           jns 0x140c60346
00C6033B  B9 10 00 00 00                  mov ecx, 0x10
00C60340  E8 BF 16 A1 FF                  call 0x140671a04
00C60345  CC                              int3
00C60346  45 33 C9                        xor r9d, r9d
00C60349  48 8D 15 B0 83 1D 00            lea rdx, [rip + 0x1d83b0]
00C60350  49 8B CE                        mov rcx, r14
00C60353  45 8D 41 09                     lea r8d, [r9 + 9]
00C60357  E8 78 B4 B9 FF                  call 0x1407fb7d4
00C6035C  E8 57 7D 00 00                  call 0x140c680b8
00C60361  85 C0                           test eax, eax
00C60363  75 09                           jne 0x140c6036e
00C60365  8D 48 0D                        lea ecx, [rax + 0xd]
00C60368  E8 97 16 A1 FF                  call 0x140671a04
00C6036D  CC                              int3
00C6036E  E8 C5 A3 00 00                  call 0x140c6a738
00C60373  85 C0                           test eax, eax
00C60375  75 09                           jne 0x140c60380
00C60377  8D 48 30                        lea ecx, [rax + 0x30]
00C6037A  E8 85 16 A1 FF                  call 0x140671a04
00C6037F  CC                              int3
00C60380  E8 2B C9 00 00                  call 0x140c6ccb0
00C60385  85 C0                           test eax, eax
00C60387  75 09                           jne 0x140c60392
00C60389  8D 48 0E                        lea ecx, [rax + 0xe]
00C6038C  E8 73 16 A1 FF                  call 0x140671a04
00C60391  CC                              int3
00C60392  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00C6039B  E8 58 34 F1 FF                  call 0x140b737f8
00C603A0  85 C0                           test eax, eax
00C603A2  75 09                           jne 0x140c603ad
00C603A4  8D 48 0F                        lea ecx, [rax + 0xf]
00C603A7  E8 58 16 A1 FF                  call 0x140671a04
00C603AC  CC                              int3
00C603AD  E8 1A 4A 00 00                  call 0x140c64dcc
00C603B2  85 C0                           test eax, eax
00C603B4  75 09                           jne 0x140c603bf
00C603B6  8D 48 33                        lea ecx, [rax + 0x33]
00C603B9  E8 46 16 A1 FF                  call 0x140671a04
00C603BE  CC                              int3
00C603BF  48 8B 05 1A D9 1C 00            mov rax, qword ptr [rip + 0x1cd91a]
00C603C6  48 8D 14 40                     lea rdx, [rax + rax*2]
00C603CA  48 C1 E2 04                     shl rdx, 4
00C603CE  48 B8 2F 00 00 00 00 DE FF FF   movabs rax, 0xffffde000000002f
00C603D8  48 03 D0                        add rdx, rax
00C603DB  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
00C603E5  E8 52 56 00 00                  call 0x140c65a3c
00C603EA  48 0F BA 2D 95 66 36 00 1D      bts qword ptr [rip + 0x366695], 0x1d
00C603F3  33 C9                           xor ecx, ecx
00C603F5  E8 E6 E3 71 FF                  call 0x14037e7e0
00C603FA  33 C9                           xor ecx, ecx
00C603FC  48 89 05 45 84 3A 00            mov qword ptr [rip + 0x3a8445], rax
00C60403  E8 B8 1C A1 FF                  call 0x1406720c0
00C60408  33 C9                           xor ecx, ecx
00C6040A  E8 D1 E3 71 FF                  call 0x14037e7e0
00C6040F  48 89 05 3A 84 3A 00            mov qword ptr [rip + 0x3a843a], rax
00C60416  E8 75 E0 A1 FF                  call 0x14067e490
00C6041B  85 C0                           test eax, eax
00C6041D  75 09                           jne 0x140c60428
00C6041F  8D 48 14                        lea ecx, [rax + 0x14]
00C60422  E8 DD 15 A1 FF                  call 0x140671a04
00C60427  CC                              int3
00C60428  E8 EB 44 00 00                  call 0x140c64918
00C6042D  85 C0                           test eax, eax
00C6042F  75 09                           jne 0x140c6043a
00C60431  8D 48 15                        lea ecx, [rax + 0x15]
00C60434  E8 CB 15 A1 FF                  call 0x140671a04
00C60439  CC                              int3
00C6043A  48 8D 8F 60 01 00 00            lea rcx, [rdi + 0x160]
00C60441  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00C60445  40 84 C5                        test bpl, al
00C60448  74 0D                           je 0x140c60457
00C6044A  48 3B C5                        cmp rax, rbp
00C6044D  74 44                           je 0x140c60493
00C6044F  48 0B CD                        or rcx, rbp
00C60452  48 33 C8                        xor rcx, rax
00C60455  EB 37                           jmp 0x140c6048e
00C60457  48 8B C8                        mov rcx, rax
00C6045A  EB 32                           jmp 0x140c6048e
00C6045C  81 61 18 FF FF FF 1F            and dword ptr [rcx + 0x18], 0x1fffffff
00C60463  48 8B D1                        mov rdx, rcx
00C60466  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00C6046A  48 85 C0                        test rax, rax
00C6046D  74 15                           je 0x140c60484
00C6046F  48 8B C8                        mov rcx, rax
00C60472  48 8B 00                        mov rax, qword ptr [rax]
00C60475  48 85 C0                        test rax, rax
00C60478  75 F5                           jne 0x140c6046f
00C6047A  EB 12                           jmp 0x140c6048e
00C6047C  48 39 11                        cmp qword ptr [rcx], rdx
00C6047F  74 0D                           je 0x140c6048e
00C60481  48 8B D1                        mov rdx, rcx
00C60484  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00C60488  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
00C6048C  75 EE                           jne 0x140c6047c
00C6048E  48 85 C9                        test rcx, rcx
00C60491  75 C9                           jne 0x140c6045c
00C60493  48 8B CF                        mov rcx, rdi
00C60496  E8 E1 3E 00 00                  call 0x140c6437c
00C6049B  49 8B CE                        mov rcx, r14
00C6049E  E8 69 C1 BA FF                  call 0x14080c60c
00C604A3  48 8D 0D 56 D7 1C 00            lea rcx, [rip + 0x1cd756]
00C604AA  BD 4D 6D 20 20                  mov ebp, 0x20206d4d
00C604AF  48 39 0D 6A D7 1C 00            cmp qword ptr [rip + 0x1cd76a], rcx
00C604B6  74 3C                           je 0x140c604f4
00C604B8  8B 05 06 D7 1C 00               mov eax, dword ptr [rip + 0x1cd706]
00C604BE  44 8B C5                        mov r8d, ebp
00C604C1  83 C0 02                        add eax, 2
00C604C4  49 8B CD                        mov rcx, r13
00C604C7  C1 E0 04                        shl eax, 4
00C604CA  8B D0                           mov edx, eax
00C604CC  8B F8                           mov edi, eax
00C604CE  E8 6D B0 6F FF                  call 0x14035b540
00C604D3  48 8B D8                        mov rbx, rax
00C604D6  48 85 C0                        test rax, rax
00C604D9  74 19                           je 0x140c604f4
00C604DB  48 8B 15 3E D7 1C 00            mov rdx, qword ptr [rip + 0x1cd73e]
00C604E2  44 8B C7                        mov r8d, edi
00C604E5  48 8B C8                        mov rcx, rax
00C604E8  E8 53 63 A6 FF                  call 0x1406c6840
00C604ED  48 89 1D 2C D7 1C 00            mov qword ptr [rip + 0x1cd72c], rbx
00C604F4  48 39 35 2D D7 1C 00            cmp qword ptr [rip + 0x1cd72d], rsi
00C604FB  74 3D                           je 0x140c6053a
00C604FD  0F B6 05 C7 D6 1C 00            movzx eax, byte ptr [rip + 0x1cd6c7]
00C60504  44 8B C5                        mov r8d, ebp
00C60507  83 C0 02                        add eax, 2
00C6050A  49 8B CD                        mov rcx, r13
00C6050D  C1 E0 04                        shl eax, 4
00C60510  8B D0                           mov edx, eax
00C60512  8B F8                           mov edi, eax
00C60514  E8 27 B0 6F FF                  call 0x14035b540
00C60519  48 8B D8                        mov rbx, rax
00C6051C  48 85 C0                        test rax, rax
00C6051F  74 19                           je 0x140c6053a
00C60521  48 8B 15 00 D7 1C 00            mov rdx, qword ptr [rip + 0x1cd700]
00C60528  44 8B C7                        mov r8d, edi
00C6052B  48 8B C8                        mov rcx, rax
00C6052E  E8 0D 63 A6 FF                  call 0x1406c6840
00C60533  48 89 1D EE D6 1C 00            mov qword ptr [rip + 0x1cd6ee], rbx
00C6053A  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
00C6053E  48 8D 0D 3B 58 1D 00            lea rcx, [rip + 0x1d583b]
00C60545  66 89 74 24 30                  mov word ptr [rsp + 0x30], si
00C6054A  41 B9 00 02 00 00               mov r9d, 0x200
00C60550  C7 44 24 28 4D 6D 4C 6B         mov dword ptr [rsp + 0x28], 0x6b4c6d4d
00C60558  45 33 C0                        xor r8d, r8d
00C6055B  33 D2                           xor edx, edx
00C6055D  48 C7 44 24 20 C0 00 00 00      mov qword ptr [rsp + 0x20], 0xc0
00C60566  E8 B5 81 80 FF                  call 0x140468720
00C6056B  E8 8C 9F 00 00                  call 0x140c6a4fc
00C60570  48 B8 00 00 00 00 04 00 00 00   movabs rax, 0x400000000
00C6057A  C7 44 24 20 09 00 00 00         mov dword ptr [rsp + 0x20], 9
00C60582  48 09 05 FF 64 36 00            or qword ptr [rip + 0x3664ff], rax
00C60589  48 8D 15 A0 E2 A2 FF            lea rdx, [rip - 0x5d1d60]
00C60590  41 83 C9 FF                     or r9d, 0xffffffff
00C60594  45 33 C0                        xor r8d, r8d
00C60597  49 8B CE                        mov rcx, r14
00C6059A  E8 59 41 81 FF                  call 0x1404746f8
00C6059F  4C 8D 5C 24 40                  lea r11, [rsp + 0x40]
00C605A4  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00C605A8  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
00C605AC  49 8B E3                        mov rsp, r11
00C605AF  41 5E                           pop r14
00C605B1  41 5D                           pop r13
00C605B3  41 5C                           pop r12
00C605B5  5F                              pop rdi
00C605B6  5E                              pop rsi
00C605B7  C3                              ret
00C605B8  CC                              int3
00C605B9  B9 02 00 00 80                  mov ecx, 0x80000002
00C605BE  E8 8D 64 69 FF                  call 0x1402f6a50
00C605C3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInitNucleus(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int16 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p12;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rbp;
    v_rsp = (v_rsp) - (64);
    v_rsi = 0;
    v_stack_p10 = v_rip + 3561347;
    v_stack_p10 = v_rip + 1745642;
    result = (int)(*(unsigned int *)(v_rip + 1901782));
    if ((unsigned int)((int)(*(unsigned int *)(v_rip + 1901782))) != 0) {
        a3 = (int)(*(unsigned int *)(v_rip + 1901782));
        v_stack_m48 = 0;
        a4 = 0;
        a1 = v_rsi + 26;
        a2 = 768;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = MiConstructLoaderMemoryTree(a1, a2, a3, a4);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, a4);
    *(unsigned __int64 *)(v_rip + 3836518) = result;
    *(unsigned __int8 *)(v_rip + 1931590) = 4;
    result = MiCompensateForProcessorErrata(0, a2, a3, a4);
    result = MI_READ_PTE_LOCK_FREE(0, a2, a3, a4);
    result = (result) >> (12);
    result = (result) & (0);
    a1 = (unsigned int)((v_cr3) & (0xFFFULL));
    result = (result) << (12);
    a1 = (a1) | (result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 40) = a1;
    result = MiExamineHalVa(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    *(unsigned __int64 *)(v_rip + 3836128) = result;
    result = MiInitializeBootDefaults(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    if ((((unsigned __int8)(v_rip + 1925076)) & (15)) != 0) goto loc_00C605B9;
    *(unsigned __int64 *)(v_rip + 1925051) = v_xmm0;
loc_00C5FE48:
    *(unsigned __int64 *)(v_rip + 1936050 + 8) = v_rip + 1936050;
    *(unsigned __int64 *)(v_rip + 1936050) = v_rip + 1936050;
    result = (v_rip + 1936050) + (16);
    a1 = (1 + 15) - (1);
    if (condition_is_not_equal) goto loc_00C5FE48;
loc_00C5FE68:
    *(unsigned __int64 *)(v_rip + 1930264) = 0;
    result = (v_rip + 1930264) + (a1 + 2 + 62);
    a1 = ((unsigned int)((unsigned int)(a1 + 2))) - (1);
    if (condition_is_not_equal) goto loc_00C5FE68;
    *(unsigned __int16 *)(v_rip + 1939455) = 0;
    *(unsigned __int64 *)(v_rip + 1939461) = v_rip + 1939470;
    *(unsigned __int64 *)(v_rip + 1930349) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 1939438) = v_rip + 1939470;
    *(unsigned __int8 *)(v_rip + 1939425) = 6;
    *(unsigned int *)(v_rip + 1939421) = 0;
    result = MiCountBootDriverRegions(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    *(unsigned __int64 *)(v_rip + 1936296) = result;
    result = MiSystemVaTypeToVm(11, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 184)));
    a1 = (unsigned __int8)(((unsigned int)(*(unsigned int *)(result + 184))) & (243));
    a1 = (unsigned __int8)((a1) | (3));
    v_stack_p10 = (unsigned __int8)(a1);
    *(unsigned __int16 *)(result + 184) = (unsigned __int16)(v_stack_p10);
    result = MiInitializeNumaRangesTemporary(v_stack_p10, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    result = MiInitializeChannelRangesTemporary(v_stack_p10, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    result = MiMemoryLicense(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    *(unsigned __int64 *)(v_rip + 3836170) = result;
    result = MiRemoveLargeFreeLoaderDescriptors(0, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    *(unsigned __int64 *)(v_rip + 3836148) = result;
    result = MiInitializeLoaderDescriptors(0, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    result = MiCheckLargePageOk(0, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    *(unsigned __int64 *)(v_rip + 1900574) = v_xmm0;
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1900568)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 1900568))) >> (16));
    result = (unsigned __int8)((result) & (254));
    result = (unsigned __int8)((result) | (6));
    v_stack_p12 = (unsigned __int8)(result);
    *(unsigned __int64 *)(v_rip + 1900516) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 1900493) = v_xmm0;
    *(unsigned int *)(v_rip + 1900519) = (unsigned int)((unsigned int)(v_stack_p10));
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1900513)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 1900513))) >> (16));
    result = (unsigned __int8)((result) & (63));
    result = (unsigned __int8)((result) | ((unsigned __int8)(a1 + 2 + 62)));
    v_stack_p12 = (unsigned __int8)(result);
    *(unsigned int *)(v_rip + 1900487) = (unsigned int)((unsigned int)(v_stack_p10));
    result = (*(unsigned __int64 *)(v_rip + 1900488)) | (0);
    *(unsigned __int64 *)(v_rip + 1900468) = result;
    result = (*(unsigned __int64 *)(v_rip + 1900445)) & (0);
    result = (result) | (1);
    *(unsigned __int64 *)(v_rip + 1900422) = result;
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1900424)));
    v_stack_p10 = (unsigned __int16)(a1 + 2);
    *(unsigned int *)(v_rip + 1900405) = (unsigned int)((unsigned int)(v_stack_p10));
    result = (*(unsigned __int64 *)(v_rip + 1900406)) | (0);
    *(unsigned __int64 *)(v_rip + 1900389) = result;
    result = MiCopyPfnEntryRaw(v_rip + 1900404, v_rip + 1900549, a3, a4);
    a4 = (*(unsigned __int64 *)(v_rip + 1900409)) & (result);
    *(unsigned __int64 *)(v_rip + 1900389) = a4;
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1900391)));
    v_stack_p10 = 0;
    *(unsigned int *)(v_rip + 1900372) = (unsigned int)((unsigned int)(v_stack_p10));
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1900366)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 1900366))) >> (16));
    result = (unsigned __int8)((result) & (253));
    result = (unsigned __int8)((result) | (5));
    v_stack_p12 = (unsigned __int8)(result);
    *(unsigned int *)(v_rip + 1900341) = (unsigned int)((unsigned int)(v_stack_p10));
    result = MxMarkValidMappings(v_rip + 1900404, v_rip + 1900549, 3, 0);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, v_rip + 1900549, 3, 0);
    *(unsigned __int64 *)(v_rip + 3835797) = result;
    result = MiCreatePfnDatabase(0, v_rip + 1900549, 3, 0);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, v_rip + 1900549, 3, 0);
    *(unsigned __int64 *)(v_rip + 3835783) = result;
    result = MiInitializePfnsForValidMappings(0, v_rip + 1900549, 3, 0);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, v_rip + 1900549, 3, 0);
    *(unsigned __int64 *)(v_rip + 3835769) = result;
    result = MiSwitchToPfns(0, v_rip + 1900549, 3, 0);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, v_rip + 1900549, 3, 0);
    *(unsigned __int64 *)(v_rip + 3835758) = result;
    *(unsigned __int8 *)(v_rip + 1891328) = 0;
    if ((unsigned int)(*(unsigned __int16 *)(v_rip + 3559215)) == 0) goto loc_00C60153;
loc_00C600E2:
    a4 = (*(unsigned __int64 *)(v_rip + 1891087) + 120) + (0);
loc_00C600F5:
    *(unsigned int *)(a4) = 0;
    *(unsigned int *)(a4 + 4) = 0;
    *(unsigned int *)(a4 + 8) = 0;
    *(unsigned int *)(a4 + 12) = 0;
    result = (unsigned int)((0) + (1));
    if (((unsigned int)(result)) < 3) goto loc_00C600F5;
    a2 = (*(unsigned __int64 *)(v_rip + 1891087) + 168) + (0);
loc_00C60117:
    *(unsigned int *)(a2) = 0;
    result = (unsigned int)((0) + (1));
    if (((unsigned int)(result)) < 3) goto loc_00C60117;
    *(unsigned int *)(0 + *(unsigned __int64 *)(v_rip + 1891087) * 1 + 180) = (unsigned int)(a1 + 2);
    a2 = (*(unsigned __int64 *)(v_rip + 1891087) + 132) + (0);
loc_00C60138:
    result = (unsigned int)((0) + (1));
    if (((unsigned int)(result)) < 3) goto loc_00C60138;
    a1 = (0) + (384);
    v_r10 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 3559215)))) - (1);
    if (condition_is_not_equal) goto loc_00C600E2;
loc_00C60153:
    result = MiInitializeSections(v_rip + 1936294, a2 + 16, *(unsigned __int64 *)(v_rip + 1891087), a4 + 4);
    result = MiInitializeCommitment(v_rip + 1936294, a2 + 16, *(unsigned __int64 *)(v_rip + 1891087), a4 + 4);
    result = MiInitializeDummyPages(v_rip + 1936294, a2 + 16, *(unsigned __int64 *)(v_rip + 1891087), a4 + 4);
    result = MiInitializeSystemPtes(v_rip + 1936294, a2 + 16, *(unsigned __int64 *)(v_rip + 1891087), a4 + 4);
    if ((unsigned int)(result) == 0) {
        a1 = 1;
        result = MxInstallMoreMemory(a1, a2 + 16, *(unsigned __int64 *)(v_rip + 1891087), a4 + 4);
    }
    result = MiInitializeDebuggerSupport(a1, a2 + 16, *(unsigned __int64 *)(v_rip + 1891087), a4 + 4);
    result = MiProtectSharedUserPage(a1, a2 + 16, *(unsigned __int64 *)(v_rip + 1891087), a4 + 4);
    result = MiInitializeNonPagedPool(a1, a2 + 16, *(unsigned __int64 *)(v_rip + 1891087), a4 + 4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 5;
        result = MxInstallMoreMemory(a1, a2 + 16, *(unsigned __int64 *)(v_rip + 1891087), a4 + 4);
    }
    result = MiMapDummyPages(a1, a2 + 16, *(unsigned __int64 *)(v_rip + 1891087), a4 + 4);
    result = MiInitializeKasan(a1, a2 + 16, *(unsigned __int64 *)(v_rip + 1891087), a4 + 4);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2 + 16, *(unsigned __int64 *)(v_rip + 1891087), a4 + 4);
    a1 = (*(unsigned __int64 *)(v_rip + 3565777)) >> (5);
    a1 = (unsigned int)((a1) & (0x400ULL));
    *(unsigned __int64 *)(v_rip + 3835512) = result;
    result = ExInitializePoolHeapManagement(a1, a2 + 16, *(unsigned __int64 *)(v_rip + 1891087), a4 + 4);
    if (sign_flag) {
        a1 = 11;
        result = MxInstallMoreMemory(a1, a2 + 16, *(unsigned __int64 *)(v_rip + 1891087), a4 + 4);
    }
    result = MiInitializePhysicalMemoryBlocks(a1, a2 + 16, *(unsigned __int64 *)(v_rip + 1891087), a4 + 4);
    a2 = (a4 + 4) + (result);
loc_00C6020E:
    a1 = (a4 + 4) >> (9);
    a1 = (a1) & (v_r10);
    a2 = (a2) >> (9);
    a1 = (a1) + (a4 + 4);
    a2 = (a2) & (v_r10);
    a2 = (a2) + (a4 + 4);
    a3 = (3) - (1);
    if (condition_is_not_equal) goto loc_00C6020E;
    result = MxZeroBootMappings(a1, a2, 3, a4 + 4);
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    result = MI_FLUSH_ENTIRE_TB(1, a2, 3, a4 + 4);
    result = MiInitializeFunctionOverrides(a1, a2, 3, a4 + 4);
    result = MiInitializeDecayPfns(a1, a2, 3, a4 + 4);
    if ((((unsigned __int8)(v_rip + 1923821)) & (15)) != 0) goto loc_00C605B9;
    *(unsigned __int64 *)(v_rip + 1923801) = v_xmm0;
loc_00C60267:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 3558802)))) goto loc_00C602F9;
    result = ExAllocatePoolMm(a1 + 2 + 62, 832, (unsigned int)(0x6F49694DULL), 0);
    if (result == 0) goto loc_00C602EE;
loc_00C602A5:
    *(unsigned __int64 *)(result + 648 + 16) = 0;
    *(unsigned __int64 *)(result + 648 + 8) = result + 648;
    *(unsigned __int64 *)(result + 648) = result + 648;
    a1 = (result + 648) + (32);
    result = (4) - (1);
    if (condition_is_not_equal) goto loc_00C602A5;
    *(unsigned __int64 *)(result + 792) = 0;
    *(unsigned __int64 *)(result + 776 + 8) = result + 776;
    *(unsigned __int64 *)(result + 776) = result + 776;
    a1 = (0 + 0 * 2) << (7);
    v_rbx = (unsigned int)((0) + (1));
    *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(v_rip + 1890589) * 1 + 376) = result;
    goto loc_00C60267;
loc_00C602EE:
    result = MxInstallMoreMemory(12, result, (unsigned int)(0x6F49694DULL), 0);
loc_00C602F9:
    result = MiGetAnyMultiplexedVm(1, result, (unsigned int)(0x6F49694DULL), 0);
    a1 = (unsigned __int8)(((unsigned int)(*(unsigned int *)(result + 184))) & (15));
    if (((unsigned __int8)(a1)) != 1) {
        a1 = result + 192;
    }
    a4 = 0;
    *(unsigned __int64 *)(a1) = v_rip + 1889949;
    result = MiInitializeSystemWorkingSetList(v_rip + 1936294, result, 3, a4);
    if (sign_flag) {
        a1 = 16;
        result = MxInstallMoreMemory(a1, result, 3, a4);
    }
    a4 = 0;
    result = MiInitializeSystemWorkingSetList(v_rip + 1936294, v_rip + 1934256, a4 + 9, a4);
    result = MiInitializeKernelStacks(v_rip + 1936294, v_rip + 1934256, a4 + 9, a4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 13;
        result = MxInstallMoreMemory(a1, v_rip + 1934256, a4 + 9, a4);
    }
    result = MiInitializeNonCachedMappingRegion(a1, v_rip + 1934256, a4 + 9, a4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 48;
        result = MxInstallMoreMemory(a1, v_rip + 1934256, a4 + 9, a4);
    }
    result = MiCreateTopLevelUltraMappings(a1, v_rip + 1934256, a4 + 9, a4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 14;
        result = MxInstallMoreMemory(a1, v_rip + 1934256, a4 + 9, a4);
    }
    result = MmInitializeProcessor(*(unsigned __int64 *)(gs_base + (0 + 32)), v_rip + 1934256, a4 + 9, a4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 15;
        result = MxInstallMoreMemory(a1, v_rip + 1934256, a4 + 9, a4);
    }
    result = MiBuildSystemDataViews(a1, v_rip + 1934256, a4 + 9, a4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 51;
        result = MxInstallMoreMemory(a1, v_rip + 1934256, a4 + 9, a4);
    }
    a2 = (*(unsigned __int64 *)(v_rip + 1890586) + *(unsigned __int64 *)(v_rip + 1890586) * 2) << (4);
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 1890586));
    result = MiFillGapAddresses(a1, a2, a4 + 9, a4);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a4 + 9, a4);
    a1 = 0;
    *(unsigned __int64 *)(v_rip + 3834949) = result;
    result = MiFreeUnusedPfnPages(a1, a2, a4 + 9, a4);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a4 + 9, a4);
    *(unsigned __int64 *)(v_rip + 3834938) = result;
    result = MiInitializePageFaultResources(a1, a2, a4 + 9, a4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 20;
        result = MxInstallMoreMemory(a1, a2, a4 + 9, a4);
    }
    result = MiBuildPagedPool(a1, a2, a4 + 9, a4);
    if ((unsigned int)(result) == 0) {
        a1 = result + 21;
        result = MxInstallMoreMemory(a1, a2, a4 + 9, a4);
    }
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(a1 + 352 + 8)))) == 0) goto loc_00C60457;
    if ((*(unsigned __int64 *)(a1 + 352 + 8)) == 1) goto loc_00C60493;
    a1 = (a1 + 352) | (1);
    a1 = (a1) ^ (*(unsigned __int64 *)(a1 + 352 + 8));
    goto loc_00C6048E;
loc_00C60457:
    goto loc_00C6048E;
loc_00C6045C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 8) == 0) goto loc_00C60484;
loc_00C6046F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 8)) != 0) goto loc_00C6046F;
    goto loc_00C6048E;
loc_00C6047C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 8))) == (*(unsigned __int64 *)(a1 + 352 + 8))) goto loc_00C6048E;
loc_00C60484:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 8) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_00C6047C;
loc_00C6048E:
    if (a1 != 0) goto loc_00C6045C;
loc_00C60493:
    result = MiCreateHugeIoRanges(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 8), a4 + 9, a4);
    result = MiInitializeWsSwapping(v_rip + 1936294, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 352 + 8) + 8), a4 + 9, a4);
    if ((*(unsigned __int64 *)(v_rip + 1890154)) == (v_rip + 1890134)) goto loc_00C604F4;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 1890054))) + (2));
    result = (unsigned int)((result) << (4));
    result = MiAllocatePool(a1 + 2 + 62, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned int)(0x20206D4DULL))), a4);
    if (result != 0) {
        a2 = *(unsigned __int64 *)(v_rip + 1890110);
        a3 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = result;
        result = memcpy(a1, a2, a3, a4);
        *(unsigned __int64 *)(v_rip + 1890092) = result;
    }
    if ((*(unsigned __int64 *)(v_rip + 1890093)) == 0) goto loc_00C6053A;
    result = (unsigned int)((*(unsigned __int8 *)(v_rip + 1889991)) + (2));
    result = (unsigned int)((result) << (4));
    result = MiAllocatePool(a1 + 2 + 62, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned int)(0x20206D4DULL))), a4);
    if (result != 0) {
        a2 = *(unsigned __int64 *)(v_rip + 1890048);
        a3 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = result;
        result = memcpy(a1, a2, a3, a4);
        *(unsigned __int64 *)(v_rip + 1890030) = result;
    }
    v_stack_m30 = 0;
    v_stack_m38 = 0;
    v_stack_m40 = 0x6B4C6D4DULL;
    a3 = 0;
    a2 = 0;
    v_stack_m48 = 192;
    result = ExInitializeNPagedLookasideListInternal(v_rip + 1923131, a2, a3, 512);
    result = MiMeasureDemandCoalesceTimeBounds(v_rip + 1923131, a2, a3, 512);
    v_stack_m48 = 9;
    a4 = (unsigned int)((512) | (0xFFFFFFFFULL));
    a3 = 0;
    result = MiEnumerateSlabAllocatorsEx(v_rip + 1936294, v_rip - 6102368, a3, a4);
    return result;
loc_00C605B9:
    result = RtlRaiseStatus((unsigned int)(0x80000002ULL), v_rip - 6102368, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiInitNucleus(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint16_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint8_t v_stack_p12;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rbp;
    local_rsp = (local_rsp) - (64);
    local_rsi = 0;
    v_stack_p10 = v_rip + 3561347;
    v_stack_p10 = v_rip + 1745642;
    result = (int32_t)(*(uint32_t *)(v_rip + 0x1D04D6));
    if ((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0x1D04D6))) != 0) {
        Arg3 = (int32_t)(*(uint32_t *)(v_rip + 0x1D04D6));
        v_stack_m48 = 0;
        Arg4 = 0;
        Arg1 = local_rsi + 26;
        Arg2 = 768;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = MiConstructLoaderMemoryTree(Arg1, Arg2, Arg3, Arg4);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x3A8A66) = result;
    *(uint8_t *)(v_rip + 0x1D7946) = 4;
    result = MiCompensateForProcessorErrata(0, Arg2, Arg3, Arg4);
    result = MI_READ_PTE_LOCK_FREE(0, Arg2, Arg3, Arg4);
    result = (result) >> (12);
    result = (result) & (0);
    Arg1 = (uint32_t)((v_cr3) & (0xFFFULL));
    result = (result) << (12);
    Arg1 = (Arg1) | (result);
    *(void **)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x28) = Arg1;
    result = MiExamineHalVa(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x3A88E0) = result;
    result = MiInitializeBootDefaults(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg4);
    if ((((uint8_t)(v_rip + 1925076)) & (15)) != 0) goto loc_00C605B9;
    *(uint64_t *)(v_rip + 0x1D5FBB) = v_xmm0;
loc_00C5FE48:
    *(uint64_t *)(v_rip + 0x1D8AB2 + 0x8) = v_rip + 1936050;
    *(uint64_t *)(v_rip + 0x1D8AB2) = v_rip + 1936050;
    result = (v_rip + 1936050) + (16);
    Arg1 = (1 + 15) - (1);
    if (condition_is_not_equal) goto loc_00C5FE48;
loc_00C5FE68:
    *(uint64_t *)(v_rip + 0x1D7418) = 0;
    result = (v_rip + 1930264) + (Arg1 + 2 + 62);
    Arg1 = ((uint32_t)((uint32_t)(Arg1 + 2))) - (1);
    if (condition_is_not_equal) goto loc_00C5FE68;
    *(uint16_t *)(v_rip + 0x1D97FF) = 0;
    *(uint64_t *)(v_rip + 0x1D9805) = v_rip + 1939470;
    *(uint64_t *)(v_rip + 0x1D746D) = v_xmm0;
    *(uint64_t *)(v_rip + 0x1D97EE) = v_rip + 1939470;
    *(uint8_t *)(v_rip + 0x1D97E1) = 6;
    *(uint32_t *)(v_rip + 0x1D97DD) = 0;
    result = MiCountBootDriverRegions(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x1D8BA8) = result;
    result = MiSystemVaTypeToVm(11, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg4);
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xB8)));
    Arg1 = (uint8_t)(((uint32_t)(*(uint32_t *)(result + 0xB8))) & (243));
    Arg1 = (uint8_t)((Arg1) | (3));
    v_stack_p10 = (uint8_t)(Arg1);
    *(uint16_t *)(result + 0xB8) = (uint16_t)(v_stack_p10);
    result = MiInitializeNumaRangesTemporary(v_stack_p10, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg4);
    result = MiInitializeChannelRangesTemporary(v_stack_p10, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg4);
    result = MiMemoryLicense(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg4);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x3A890A) = result;
    result = MiRemoveLargeFreeLoaderDescriptors(0, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg4);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x3A88F4) = result;
    result = MiInitializeLoaderDescriptors(0, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg4);
    result = MiCheckLargePageOk(0, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg4);
    *(uint64_t *)(v_rip + 0x1D001E) = v_xmm0;
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1D0018)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x1D0018))) >> (16));
    result = (uint8_t)((result) & (254));
    result = (uint8_t)((result) | (6));
    v_stack_p12 = (uint8_t)(result);
    *(uint64_t *)(v_rip + 0x1CFFE4) = v_xmm0;
    *(uint64_t *)(v_rip + 0x1CFFCD) = v_xmm0;
    *(uint32_t *)(v_rip + 0x1CFFE7) = (uint32_t)((uint32_t)(v_stack_p10));
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1CFFE1)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x1CFFE1))) >> (16));
    result = (uint8_t)((result) & (63));
    result = (uint8_t)((result) | ((uint8_t)(Arg1 + 2 + 62)));
    v_stack_p12 = (uint8_t)(result);
    *(uint32_t *)(v_rip + 0x1CFFC7) = (uint32_t)((uint32_t)(v_stack_p10));
    result = (*(uint64_t *)(v_rip + 0x1CFFC8)) | (0);
    *(uint64_t *)(v_rip + 0x1CFFB4) = result;
    result = (*(uint64_t *)(v_rip + 0x1CFF9D)) & (0);
    result = (result) | (1);
    *(uint64_t *)(v_rip + 0x1CFF86) = result;
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1CFF88)));
    v_stack_p10 = (uint16_t)(Arg1 + 2);
    *(uint32_t *)(v_rip + 0x1CFF75) = (uint32_t)((uint32_t)(v_stack_p10));
    result = (*(uint64_t *)(v_rip + 0x1CFF76)) | (0);
    *(uint64_t *)(v_rip + 0x1CFF65) = result;
    result = MiCopyPfnEntryRaw(v_rip + 1900404, v_rip + 1900549, Arg3, Arg4);
    Arg4 = (*(uint64_t *)(v_rip + 0x1CFF79)) & (result);
    *(uint64_t *)(v_rip + 0x1CFF65) = Arg4;
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1CFF67)));
    v_stack_p10 = 0;
    *(uint32_t *)(v_rip + 0x1CFF54) = (uint32_t)((uint32_t)(v_stack_p10));
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1CFF4E)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x1CFF4E))) >> (16));
    result = (uint8_t)((result) & (253));
    result = (uint8_t)((result) | (5));
    v_stack_p12 = (uint8_t)(result);
    *(uint32_t *)(v_rip + 0x1CFF35) = (uint32_t)((uint32_t)(v_stack_p10));
    result = MxMarkValidMappings(v_rip + 1900404, v_rip + 1900549, 3, 0);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, v_rip + 1900549, 3, 0);
    *(uint64_t *)(v_rip + 0x3A8795) = result;
    result = MiCreatePfnDatabase(0, v_rip + 1900549, 3, 0);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, v_rip + 1900549, 3, 0);
    *(uint64_t *)(v_rip + 0x3A8787) = result;
    result = MiInitializePfnsForValidMappings(0, v_rip + 1900549, 3, 0);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, v_rip + 1900549, 3, 0);
    *(uint64_t *)(v_rip + 0x3A8779) = result;
    result = MiSwitchToPfns(0, v_rip + 1900549, 3, 0);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, v_rip + 1900549, 3, 0);
    *(uint64_t *)(v_rip + 0x3A876E) = result;
    *(uint8_t *)(v_rip + 0x1CDC00) = 0;
    if ((uint32_t)(*(uint16_t *)(v_rip + 0x364F2F)) == 0) goto loc_00C60153;
loc_00C600E2:
    Arg4 = (*(uint64_t *)(v_rip + 0x1CDB0F) + 120) + (0);
loc_00C600F5:
    *(uint32_t *)(Arg4) = 0;
    *(uint32_t *)(Arg4 + 0x4) = 0;
    *(uint32_t *)(Arg4 + 0x8) = 0;
    *(uint32_t *)(Arg4 + 0xC) = 0;
    result = (uint32_t)((0) + (1));
    if (((uint32_t)(result)) < 3) goto loc_00C600F5;
    Arg2 = (*(uint64_t *)(v_rip + 0x1CDB0F) + 168) + (0);
loc_00C60117:
    *(uint32_t *)(Arg2) = 0;
    result = (uint32_t)((0) + (1));
    if (((uint32_t)(result)) < 3) goto loc_00C60117;
    *(uint32_t *)(0 + *(uint64_t *)(v_rip + 0x1CDB0F) * 1 + 0xB4) = (uint32_t)(Arg1 + 2);
    Arg2 = (*(uint64_t *)(v_rip + 0x1CDB0F) + 132) + (0);
loc_00C60138:
    result = (uint32_t)((0) + (1));
    if (((uint32_t)(result)) < 3) goto loc_00C60138;
    Arg1 = (0) + (384);
    local_r10 = ((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0x364F2F)))) - (1);
    if (condition_is_not_equal) goto loc_00C600E2;
loc_00C60153:
    result = MiInitializeSections(v_rip + 1936294, Arg2 + 16, *(uint64_t *)(v_rip + 0x1CDB0F), Arg4 + 4);
    result = MiInitializeCommitment(v_rip + 1936294, Arg2 + 16, *(uint64_t *)(v_rip + 0x1CDB0F), Arg4 + 4);
    result = MiInitializeDummyPages(v_rip + 1936294, Arg2 + 16, *(uint64_t *)(v_rip + 0x1CDB0F), Arg4 + 4);
    result = MiInitializeSystemPtes(v_rip + 1936294, Arg2 + 16, *(uint64_t *)(v_rip + 0x1CDB0F), Arg4 + 4);
    if ((uint32_t)(result) == 0) {
        Arg1 = 1;
        result = MxInstallMoreMemory(Arg1, Arg2 + 16, *(uint64_t *)(v_rip + 0x1CDB0F), Arg4 + 4);
    }
    result = MiInitializeDebuggerSupport(Arg1, Arg2 + 16, *(uint64_t *)(v_rip + 0x1CDB0F), Arg4 + 4);
    result = MiProtectSharedUserPage(Arg1, Arg2 + 16, *(uint64_t *)(v_rip + 0x1CDB0F), Arg4 + 4);
    result = MiInitializeNonPagedPool(Arg1, Arg2 + 16, *(uint64_t *)(v_rip + 0x1CDB0F), Arg4 + 4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 5;
        result = MxInstallMoreMemory(Arg1, Arg2 + 16, *(uint64_t *)(v_rip + 0x1CDB0F), Arg4 + 4);
    }
    result = MiMapDummyPages(Arg1, Arg2 + 16, *(uint64_t *)(v_rip + 0x1CDB0F), Arg4 + 4);
    result = MiInitializeKasan(Arg1, Arg2 + 16, *(uint64_t *)(v_rip + 0x1CDB0F), Arg4 + 4);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2 + 16, *(uint64_t *)(v_rip + 0x1CDB0F), Arg4 + 4);
    Arg1 = (*(uint64_t *)(v_rip + 0x3668D1)) >> (5);
    Arg1 = (uint32_t)((Arg1) & (0x400ULL));
    *(uint64_t *)(v_rip + 0x3A8678) = result;
    result = ExInitializePoolHeapManagement(Arg1, Arg2 + 16, *(uint64_t *)(v_rip + 0x1CDB0F), Arg4 + 4);
    if (sign_flag) {
        Arg1 = 11;
        result = MxInstallMoreMemory(Arg1, Arg2 + 16, *(uint64_t *)(v_rip + 0x1CDB0F), Arg4 + 4);
    }
    result = MiInitializePhysicalMemoryBlocks(Arg1, Arg2 + 16, *(uint64_t *)(v_rip + 0x1CDB0F), Arg4 + 4);
    Arg2 = (Arg4 + 4) + (result);
loc_00C6020E:
    Arg1 = (Arg4 + 4) >> (9);
    Arg1 = (Arg1) & (local_r10);
    Arg2 = (Arg2) >> (9);
    Arg1 = (Arg1) + (Arg4 + 4);
    Arg2 = (Arg2) & (local_r10);
    Arg2 = (Arg2) + (Arg4 + 4);
    Arg3 = (3) - (1);
    if (condition_is_not_equal) goto loc_00C6020E;
    result = MxZeroBootMappings(Arg1, Arg2, 3, Arg4 + 4);
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    result = MI_FLUSH_ENTIRE_TB(1, Arg2, 3, Arg4 + 4);
    result = MiInitializeFunctionOverrides(Arg1, Arg2, 3, Arg4 + 4);
    result = MiInitializeDecayPfns(Arg1, Arg2, 3, Arg4 + 4);
    if ((((uint8_t)(v_rip + 1923821)) & (15)) != 0) goto loc_00C605B9;
    *(uint64_t *)(v_rip + 0x1D5AD9) = v_xmm0;
loc_00C60267:
    if (0 >= ((uint32_t)(*(uint16_t *)(v_rip + 0x364D92)))) goto loc_00C602F9;
    result = ExAllocatePoolMm(Arg1 + 2 + 62, 832, (uint32_t)(0x6F49694DULL), 0);
    if (result == 0) goto loc_00C602EE;
loc_00C602A5:
    *(uint64_t *)(result + 0x288 + 0x10) = 0;
    *(uint64_t *)(result + 0x288 + 0x8) = result + 648;
    *(uint64_t *)(result + 0x288) = result + 648;
    Arg1 = (result + 648) + (32);
    result = (4) - (1);
    if (condition_is_not_equal) goto loc_00C602A5;
    *(uint64_t *)(result + 0x318) = 0;
    *(uint64_t *)(result + 0x308 + 0x8) = result + 776;
    *(uint64_t *)(result + 0x308) = result + 776;
    Arg1 = (0 + 0 * 2) << (7);
    local_rbx = (uint32_t)((0) + (1));
    *(uint64_t *)(arg1 + *(uint64_t *)(v_rip + 0x1CD91D) * 1 + 0x178) = result;
    goto loc_00C60267;
loc_00C602EE:
    result = MxInstallMoreMemory(12, result, (uint32_t)(0x6F49694DULL), 0);
loc_00C602F9:
    result = MiGetAnyMultiplexedVm(1, result, (uint32_t)(0x6F49694DULL), 0);
    Arg1 = (uint8_t)(((uint32_t)(*(uint32_t *)(result + 0xB8))) & (15));
    if (((uint8_t)(Arg1)) != 1) {
        Arg1 = result + 192;
    }
    Arg4 = 0;
    *(uint64_t *)(arg1) = v_rip + 1889949;
    result = MiInitializeSystemWorkingSetList(v_rip + 1936294, result, 3, Arg4);
    if (sign_flag) {
        Arg1 = 16;
        result = MxInstallMoreMemory(Arg1, result, 3, Arg4);
    }
    Arg4 = 0;
    result = MiInitializeSystemWorkingSetList(v_rip + 1936294, v_rip + 1934256, Arg4 + 9, Arg4);
    result = MiInitializeKernelStacks(v_rip + 1936294, v_rip + 1934256, Arg4 + 9, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 13;
        result = MxInstallMoreMemory(Arg1, v_rip + 1934256, Arg4 + 9, Arg4);
    }
    result = MiInitializeNonCachedMappingRegion(Arg1, v_rip + 1934256, Arg4 + 9, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 48;
        result = MxInstallMoreMemory(Arg1, v_rip + 1934256, Arg4 + 9, Arg4);
    }
    result = MiCreateTopLevelUltraMappings(Arg1, v_rip + 1934256, Arg4 + 9, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 14;
        result = MxInstallMoreMemory(Arg1, v_rip + 1934256, Arg4 + 9, Arg4);
    }
    result = MmInitializeProcessor(*(uint64_t *)(gs_base + (0 + 0x20)), v_rip + 1934256, Arg4 + 9, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 15;
        result = MxInstallMoreMemory(Arg1, v_rip + 1934256, Arg4 + 9, Arg4);
    }
    result = MiBuildSystemDataViews(Arg1, v_rip + 1934256, Arg4 + 9, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 51;
        result = MxInstallMoreMemory(Arg1, v_rip + 1934256, Arg4 + 9, Arg4);
    }
    Arg2 = (*(uint64_t *)(v_rip + 0x1CD91A) + *(uint64_t *)(v_rip + 0x1CD91A) * 2) << (4);
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0x1CD91A));
    result = MiFillGapAddresses(Arg1, Arg2, Arg4 + 9, Arg4);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg4 + 9, Arg4);
    Arg1 = 0;
    *(uint64_t *)(v_rip + 0x3A8445) = result;
    result = MiFreeUnusedPfnPages(Arg1, Arg2, Arg4 + 9, Arg4);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg4 + 9, Arg4);
    *(uint64_t *)(v_rip + 0x3A843A) = result;
    result = MiInitializePageFaultResources(Arg1, Arg2, Arg4 + 9, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 20;
        result = MxInstallMoreMemory(Arg1, Arg2, Arg4 + 9, Arg4);
    }
    result = MiBuildPagedPool(Arg1, Arg2, Arg4 + 9, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg1 = result + 21;
        result = MxInstallMoreMemory(Arg1, Arg2, Arg4 + 9, Arg4);
    }
    if (((1) & ((uint8_t)(*(uint64_t *)(arg1 + 0x160 + 0x8)))) == 0) goto loc_00C60457;
    if ((*(uint64_t *)(arg1 + 0x160 + 0x8)) == 1) goto loc_00C60493;
    Arg1 = (Arg1 + 352) | (1);
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg1 + 0x160 + 0x8));
    goto loc_00C6048E;
loc_00C60457:
    goto loc_00C6048E;
loc_00C6045C:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x8) == 0) goto loc_00C60484;
loc_00C6046F:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x8)) != 0) goto loc_00C6046F;
    goto loc_00C6048E;
loc_00C6047C:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x8))) == (*(uint64_t *)(arg1 + 0x160 + 0x8))) goto loc_00C6048E;
loc_00C60484:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x8) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_00C6047C;
loc_00C6048E:
    if (Arg1 != NULL) goto loc_00C6045C;
loc_00C60493:
    result = MiCreateHugeIoRanges(Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x8), Arg4 + 9, Arg4);
    result = MiInitializeWsSwapping(v_rip + 1936294, *(uint64_t *)(*(uint64_t *)(arg1 + 0x160 + 0x8) + 0x8), Arg4 + 9, Arg4);
    if ((*(uint64_t *)(v_rip + 0x1CD76A)) == (v_rip + 1890134)) goto loc_00C604F4;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x1CD706))) + (2));
    result = (uint32_t)((result) << (4));
    result = MiAllocatePool(Arg1 + 2 + 62, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint32_t)(0x20206D4DULL))), Arg4);
    if (result != 0) {
        Arg2 = *(uint64_t *)(v_rip + 0x1CD73E);
        Arg3 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = result;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
        *(uint64_t *)(v_rip + 0x1CD72C) = result;
    }
    if ((*(uint64_t *)(v_rip + 0x1CD72D)) == 0) goto loc_00C6053A;
    result = (uint32_t)((*(uint8_t *)(v_rip + 0x1CD6C7)) + (2));
    result = (uint32_t)((result) << (4));
    result = MiAllocatePool(Arg1 + 2 + 62, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint32_t)(0x20206D4DULL))), Arg4);
    if (result != 0) {
        Arg2 = *(uint64_t *)(v_rip + 0x1CD700);
        Arg3 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = result;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
        *(uint64_t *)(v_rip + 0x1CD6EE) = result;
    }
    v_stack_m30 = 0;
    v_stack_m38 = 0;
    v_stack_m40 = 0x6B4C6D4DULL;
    Arg3 = 0;
    Arg2 = 0;
    v_stack_m48 = 192;
    result = ExInitializeNPagedLookasideListInternal(v_rip + 1923131, Arg2, Arg3, 512);
    result = MiMeasureDemandCoalesceTimeBounds(v_rip + 1923131, Arg2, Arg3, 512);
    v_stack_m48 = 9;
    Arg4 = (uint32_t)((512) | (0xFFFFFFFFULL));
    Arg3 = 0;
    result = MiEnumerateSlabAllocatorsEx(v_rip + 1936294, v_rip - 6102368, Arg3, Arg4);
    return result;
loc_00C605B9:
    result = RtlRaiseStatus((uint32_t)(0x80000002ULL), v_rip - 6102368, Arg3, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x160` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C5FD38&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
