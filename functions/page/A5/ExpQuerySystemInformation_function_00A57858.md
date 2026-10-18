# ExpQuerySystemInformation

- RVA: `0x00A57858`–`0x00A5B7E9` (길이 `16,273` bytes)
- VA: `0x0000000140A57858`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B1740`
- 디코드: `3,700`개 명령, `16,273/16,273` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **207**; 고유 호출 대상: **143**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **69**

### Outgoing calls
- `0x00A57923` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A57A94` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00A57BCC` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (function, `0x00249EF0`)
- `0x00A57C83` → [KeQueryActiveGroupCount](../../text/48/KeQueryActiveGroupCount_function_0048C600.md) (function, `0x0048C600`)
- `0x00A57E61` → [KeQueryBootTimeValues](../../text/49/KeQueryBootTimeValues_function_0049F444.md) (function, `0x0049F444`)
- `0x00A57E66` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00A57EB1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A57EFF` → [ExpQuerySystemPerformanceInformation](../9D/ExpQuerySystemPerformanceInformation_function_009D648C.md) (function, `0x009D648C`)
- `0x00A57F36` → [ExpGetSystemProcessorInformation](../../text/26/ExpGetSystemProcessorInformation_function_00265AFC.md) (function, `0x00265AFC`)
- `0x00A57F80` → [ExIsRestrictedCaller](../A2/ExIsRestrictedCaller_function_00A217E8.md) (function, `0x00A217E8`)
- `0x00A57F9C` → [ExpQueryModuleInformation](../A9/ExpQueryModuleInformation_function_00A9BC30.md) (function, `0x00A9BC30`)
- `0x00A57FA9` → [EtwTiLogSyscallUsage](../90/EtwTiLogSyscallUsage_function_00903890.md) (function, `0x00903890`)
- `0x00A5807A` → [ExIsRestrictedCaller](../A2/ExIsRestrictedCaller_function_00A217E8.md) (function, `0x00A217E8`)
- `0x00A58096` → [ExpGetLockInformation](../7C/ExpGetLockInformation_function_007C3AE0.md) (function, `0x007C3AE0`)
- `0x00A58101` → [ExIsRestrictedCaller](../A2/ExIsRestrictedCaller_function_00A217E8.md) (function, `0x00A217E8`)
- `0x00A5811D` → [ExpGetObjectInformation](../7C/ExpGetObjectInformation_function_007C3B74.md) (function, `0x007C3B74`)
- `0x00A58160` → [ExIsRestrictedCaller](../A2/ExIsRestrictedCaller_function_00A217E8.md) (function, `0x00A217E8`)
- `0x00A5817C` → [ExpGetHandleInformation](../A8/ExpGetHandleInformation_function_00A8FB40.md) (function, `0x00A8FB40`)
- `0x00A58279` → [KeGetProcessorIndexFromNumber](../../text/2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (function, `0x002DD2D0`)
- `0x00A582F6` → [ExGetPoolTagInfo](../A1/ExGetPoolTagInfo_function_00A170D8.md) (function, `0x00A170D8`)
- `0x00A583FD` → [EtwQueryPerformanceTraceInformation](../AF/EtwQueryPerformanceTraceInformation_function_00AF28A4.md) (function, `0x00AF28A4`)
- `0x00A5842D` → [ExAcquireTimeRefreshLockShared](../A2/ExAcquireTimeRefreshLockShared_function_00A201D0.md) (function, `0x00A201D0`)
- `0x00A58440` → [ExReleaseTimeRefreshLockShared](../A2/ExReleaseTimeRefreshLockShared_function_00A2023C.md) (function, `0x00A2023C`)
- `0x00A58581` → [ExpGetLookasideInformation](../../text/4E/ExpGetLookasideInformation_function_004E2468.md) (function, `0x004E2468`)
- `0x00A585AC` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00A585B8` → [ExAcquireTimeRefreshLockShared](../A2/ExAcquireTimeRefreshLockShared_function_00A201D0.md) (function, `0x00A201D0`)
- `0x00A5862B` → [ExReleaseTimeRefreshLockShared](../A2/ExReleaseTimeRefreshLockShared_function_00A2023C.md) (function, `0x00A2023C`)
- `0x00A586D9` → [ExpQueryLegacyDriverInformation](../7C/ExpQueryLegacyDriverInformation_function_007C4948.md) (function, `0x007C4948`)
- `0x00A58733` → [PoGetIdleTimes](../../text/2D/PoGetIdleTimes_function_002DF570.md) (function, `0x002DF570`)
- `0x00A58796` → [CmQueryRegistryQuotaInformation](../AA/CmQueryRegistryQuotaInformation_function_00AA02B8.md) (function, `0x00AA02B8`)
- `0x00A5882F` → [PfSnQueryPrefetcherInformation](PfSnQueryPrefetcherInformation_function_00A51B8C.md) (function, `0x00A51B8C`)
- `0x00A58844` → [ExpQueryNumaProcessorMap](ExpQueryNumaProcessorMap_function_00A5E784.md) (function, `0x00A5E784`)
- `0x00A58898` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00A588F6` → [VfGetVerifierInformation](../../text/61/VfGetVerifierInformation_function_006167C4.md) (function, `0x006167C4`)
- `0x00A58920` → [KeGetRecommendedSharedDataAlignment](../../text/49/KeGetRecommendedSharedDataAlignment_function_00494040.md) (function, `0x00494040`)
- `0x00A58979` → [ExpGetSystemEmulationProcessorInformation](../../text/26/ExpGetSystemEmulationProcessorInformation_function_0026603C.md) (function, `0x0026603C`)
- `0x00A589A1` → [ExpGetSystemEmulationBasicInformation](../../text/47/ExpGetSystemEmulationBasicInformation_function_0047486C.md) (function, `0x0047486C`)
- `0x00A58A05` → [KeGetProcessorIndexFromNumber](../../text/2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (function, `0x002DD2D0`)
- `0x00A58A2D` → [PoGetPerfStateAndParkingInfo](../../text/2D/PoGetPerfStateAndParkingInfo_function_002DD484.md) (function, `0x002DD484`)
- `0x00A58A3B` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A58ADE` → [ExpQueryNumaAvailableMemory](../7C/ExpQueryNumaAvailableMemory_function_007C4AA0.md) (function, `0x007C4AA0`)
- `0x00A58B17` → [ExpReadComPlusPackage](../AB/ExpReadComPlusPackage_function_00AB78D4.md) (function, `0x00AB78D4`)
- `0x00A58B76` → [ExIsRestrictedCaller](../A2/ExIsRestrictedCaller_function_00A217E8.md) (function, `0x00A217E8`)
- `0x00A58B92` → [ExpGetHandleInformationEx](../A9/ExpGetHandleInformationEx_function_00A999B8.md) (function, `0x00A999B8`)
- `0x00A58C32` → [ExIsRestrictedCaller](../A2/ExIsRestrictedCaller_function_00A217E8.md) (function, `0x00A217E8`)
- `0x00A58C4E` → [ExGetBigPoolInfo](../../text/44/ExGetBigPoolInfo_function_00446970.md) (function, `0x00446970`)
- `0x00A58D1D` → [PfQuerySuperfetchInformation](../90/PfQuerySuperfetchInformation_function_0090210C.md) (function, `0x0090210C`)
- `0x00A58D32` → [ExIsRestrictedCaller](../A2/ExIsRestrictedCaller_function_00A217E8.md) (function, `0x00A217E8`)
- `0x00A58D48` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00A58D6A` → [ExpQueryModuleInformationEx](../7C/ExpQueryModuleInformationEx_function_007C4A0C.md) (function, `0x007C4A0C`)
- `0x00A58D86` → [ExpGetSystemFirmwareTableInformation](../A3/ExpGetSystemFirmwareTableInformation_function_00A38A2C.md) (function, `0x00A38A2C`)
- `0x00A58DA4` → [KeBuildLogicalProcessorSystemInformation](../A2/KeBuildLogicalProcessorSystemInformation_function_00A22B64.md) (function, `0x00A22B64`)
- `0x00A58DE2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A58E29` → [MmQueryMemoryListInformation](../../text/3B/MmQueryMemoryListInformation_function_003B9EDC.md) (function, `0x003B9EDC`)
- `0x00A58F52` → [PsLookupProcessByProcessId](../8A/PsLookupProcessByProcessId_function_008A2AA0.md) (function, `0x008A2AA0`)
- `0x00A58F61` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00A58F8A` → [PsQueryFullProcessImageName](../A1/PsQueryFullProcessImageName_function_00A115D0.md) (function, `0x00A115D0`)
- `0x00A58FA3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00A58FAB` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00A5901F` → [ObQueryRefTraceInformation](../74/ObQueryRefTraceInformation_function_0074F4D4.md) (function, `0x0074F4D4`)
- `0x00A5906B` → [KeFlushProcessWriteBuffers](../../text/2C/KeFlushProcessWriteBuffers_function_002CE4FC.md) (function, `0x002CE4FC`)
- `0x00A59099` → [KeGetProcessorIndexFromNumber](../../text/2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (function, `0x002DD2D0`)
- `0x00A591B0` → [VfGetVerifierInformationEx](../../pagevrfy/BA/VfGetVerifierInformationEx_function_00BAC47C.md) (function, `0x00BAC47C`)
- `0x00A591D2` → [HvlQueryEnlightenmentInfo](../71/HvlQueryEnlightenmentInfo_function_00717CF8.md) (function, `0x00717CF8`)
- `0x00A59245` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A59288` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A592BF` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A592DF` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A59315` → [SeCodeIntegrityQueryInformation](../A4/SeCodeIntegrityQueryInformation_function_00A454D4.md) (function, `0x00A454D4`)
- `0x00A59340` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00A5934C` → [ExAcquireTimeRefreshLockShared](../A2/ExAcquireTimeRefreshLockShared_function_00A201D0.md) (function, `0x00A201D0`)
- `0x00A593DC` → [ExReleaseTimeRefreshLockShared](../A2/ExReleaseTimeRefreshLockShared_function_00A2023C.md) (function, `0x00A2023C`)
- `0x00A59464` → [ExpQueryNumaProximityNode](../7C/ExpQueryNumaProximityNode_function_007C4C20.md) (function, `0x007C4C20`)
- `0x00A5947B` → [KeQueryGroupAffinity](../../text/47/KeQueryGroupAffinity_function_00471A60.md) (function, `0x00471A60`)
- `0x00A594AE` → [PpmCapturePerformanceDistribution](../../text/48/PpmCapturePerformanceDistribution_function_00489C88.md) (function, `0x00489C88`)
- `0x00A594E7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A59527` → [PpmCapturePerformanceDistribution](../../text/48/PpmCapturePerformanceDistribution_function_00489C88.md) (function, `0x00489C88`)
- `0x00A5953F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A5955C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A595A6` → [PsQueryCpuQuotaInformation](../../text/5E/PsQueryCpuQuotaInformation_function_005E27C0.md) (function, `0x005E27C0`)
- `0x00A595BB` → [IoQueryVhdBootInformation](../83/IoQueryVhdBootInformation_function_0083BB24.md) (function, `0x0083BB24`)
- `0x00A595DA` → [SmQueryStoreInformation](../A0/SmQueryStoreInformation_function_00A0E7BC.md) (function, `0x00A0E7BC`)
- `0x00A5964F` → [KeGetProcessorIndexFromNumber](../../text/2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (function, `0x002DD2D0`)
- `0x00A596EB` → [KeQueryLogicalProcessorRelationship](../../text/2C/KeQueryLogicalProcessorRelationship_function_002CEA60.md) (function, `0x002CEA60`)
- `0x00A59707` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A59750` → [ExpGetSystemBasicInformation](../../text/45/ExpGetSystemBasicInformation_function_004572E4.md) (function, `0x004572E4`)
- `0x00A597F6` → [ExQueryBootEntropyInformation](../70/ExQueryBootEntropyInformation_function_00702E20.md) (function, `0x00702E20`)
- `0x00A5980B` → [IoQueryLowPriorityIoInformation](../A9/IoQueryLowPriorityIoInformation_function_00A97514.md) (function, `0x00A97514`)
- `0x00A5988E` → [MmQuerySystemWorkingSetInformation](../../text/2C/MmQuerySystemWorkingSetInformation_function_002C0710.md) (function, `0x002C0710`)
- `0x00A599BD` → [MmGetProcessPartitionId](../../text/47/MmGetProcessPartitionId_function_0047BB44.md) (function, `0x0047BB44`)
- `0x00A599C5` → [MmGetAvailablePages](../../text/46/MmGetAvailablePages_function_0046A4C0.md) (function, `0x0046A4C0`)
- `0x00A599D2` → [MmGetTotalCommittedPages](../../text/46/MmGetTotalCommittedPages_function_0046B638.md) (function, `0x0046B638`)
- `0x00A599DF` → [MmGetTotalCommitLimit](../../text/46/MmGetTotalCommitLimit_function_0046B754.md) (function, `0x0046B754`)
- `0x00A599EC` → [MmGetPeakCommitment](../../text/46/MmGetPeakCommitment_function_0046BCF4.md) (function, `0x0046BCF4`)
- `0x00A59A6A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A59A96` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A59B73` → [BgkQueryBootGraphicsInformation](../../pagebgfx/BC/BgkQueryBootGraphicsInformation_function_00BC0064.md) (function, `0x00BC0064`)
- `0x00A59BAD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A59C5C` → [HvlQueryActiveProcessors](../../text/58/HvlQueryActiveProcessors_function_005847B0.md) (function, `0x005847B0`)
- `0x00A59C73` → [HvlQueryProcessorTopologyCount](../../text/58/HvlQueryProcessorTopologyCount_function_00584B20.md) (function, `0x00584B20`)
- `0x00A59CB8` → [sub_00A179B0](../A1/Unknown_function_00A179B0.md) (function, `0x00A179B0`)
- `0x00A59CCF` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00A59CE5` → [ExpGetSystemPlatformBinary](../7C/ExpGetSystemPlatformBinary_function_007C3C18.md) (function, `0x007C3C18`)
- `0x00A59D1D` → [ExpGetDeviceDataInformation](../95/ExpGetDeviceDataInformation_function_0095A300.md) (function, `0x0095A300`)
- `0x00A59D62` → [SeSecureBootQueryInformation](../A6/SeSecureBootQueryInformation_function_00A6D57C.md) (function, `0x00A6D57C`)
- `0x00A59DC9` → [KeGetProcessorIndexFromNumber](../../text/2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (function, `0x002DD2D0`)
- `0x00A59E0A` → [PoGetIdleTimes](../../text/2D/PoGetIdleTimes_function_002DF570.md) (function, `0x002DF570`)
- `0x00A59EF7` → [BgkQueryBootGraphicsInformation](../../pagebgfx/BC/BgkQueryBootGraphicsInformation_function_00BC0064.md) (function, `0x00BC0064`)
- `0x00A59F28` → [BgkQueryBootGraphicsInformation](../../pagebgfx/BC/BgkQueryBootGraphicsInformation_function_00BC0064.md) (function, `0x00BC0064`)
- `0x00A59F55` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A59F82` → [ExpQueryChannelInformation](../A7/ExpQueryChannelInformation_function_00A70F20.md) (function, `0x00A70F20`)
- `0x00A59F9C` → [ExpQueryMemoryTopologyInformation](../A8/ExpQueryMemoryTopologyInformation_function_00A826E0.md) (function, `0x00A826E0`)
- `0x00A59FFA` → [MmGetPageFileInformation](../A7/MmGetPageFileInformation_function_00A73F64.md) (function, `0x00A73F64`)
- `0x00A5A055` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00A5A06D` → [ExpQueryBootLoaderMetadata](../../text/65/ExpQueryBootLoaderMetadata_function_00654E8C.md) (function, `0x00654E8C`)
- `0x00A5A0D7` → [ExpQueryPortableWorkspaceEfiLauncherInformation](../7C/ExpQueryPortableWorkspaceEfiLauncherInformation_function_007C4D04.md) (function, `0x007C4D04`)
- `0x00A5A170` → [PoEnergyEstimationEnabled](../../text/45/PoEnergyEstimationEnabled_function_00450000.md) (function, `0x00450000`)
- `0x00A5A1E3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A5A21C` → [BgkQueryBootGraphicsInformation](../../pagebgfx/BC/BgkQueryBootGraphicsInformation_function_00BC0064.md) (function, `0x00BC0064`)
- `0x00A5A23D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A5A279` → [ExpGetSystemProcessorFeaturesInformation](../7C/ExpGetSystemProcessorFeaturesInformation_function_007C40D0.md) (function, `0x007C40D0`)
- `0x00A5A324` → [HvlQueryDetailInfo](../71/HvlQueryDetailInfo_function_00717BDC.md) (function, `0x00717BDC`)
- `0x00A5A3CC` → [VslIsSecureKernelRunning](../../text/4C/VslIsSecureKernelRunning_function_004C75F4.md) (function, `0x004C75F4`)
- `0x00A5A3EA` → [VslGetNestedPageProtectionFlags](../../text/2F/VslGetNestedPageProtectionFlags_function_002F2164.md) (function, `0x002F2164`)
- `0x00A5A44A` → [VslIsTrustletRunning](../../text/4B/VslIsTrustletRunning_function_004BDC88.md) (function, `0x004BDC88`)
- `0x00A5A4CB` → [VslIsEncryptionKeyAvailable](../AA/VslIsEncryptionKeyAvailable_function_00AA1924.md) (function, `0x00AA1924`)
- `0x00A5A53C` → [SeQueryTrustedPlatformModuleInformation](../../text/60/SeQueryTrustedPlatformModuleInformation_function_00609B74.md) (function, `0x00609B74`)
- `0x00A5A5B1` → [KeGetProcessorIndexFromNumber](../../text/2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (function, `0x002DD2D0`)
- `0x00A5A5BF` → [KeQueryCycleTimeStatsProcessor](../../text/48/KeQueryCycleTimeStatsProcessor_function_0048665C.md) (function, `0x0048665C`)
- `0x00A5A600` → [SeQueryHSTIResults](../84/SeQueryHSTIResults_function_00841388.md) (function, `0x00841388`)
- `0x00A5A640` → [ExCpuSetResourceManagerAccessCheck](../../text/3A/ExCpuSetResourceManagerAccessCheck_function_003A5444.md) (function, `0x003A5444`)
- `0x00A5A670` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A5A6A2` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A5A6AA` → [KeGetAffinitizedInterruptsInfo](../../text/5C/KeGetAffinitizedInterruptsInfo_function_005C5634.md) (function, `0x005C5634`)
- `0x00A5A71E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A5A735` → [HvlQueryVsmProtectionInfo](../A9/HvlQueryVsmProtectionInfo_function_00A96E30.md) (function, `0x00A96E30`)
- `0x00A5A74F` → [ExpQuerySingleModuleInformation](../7C/ExpQuerySingleModuleInformation_function_007C4FB0.md) (function, `0x007C4FB0`)
- `0x00A5A764` → [PsRootSiloInformation](../77/PsRootSiloInformation_function_0077F510.md) (function, `0x0077F510`)
- `0x00A5A7EB` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00A5A828` → [ExpQueryInterruptSteeringInformation](../7C/ExpQueryInterruptSteeringInformation_function_007C4844.md) (function, `0x007C4844`)
- `0x00A5A84C` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00A5A867` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A5A890` → [VslQuerySecureKernelProfileInformation](../../text/58/VslQuerySecureKernelProfileInformation_function_0058EED8.md) (function, `0x0058EED8`)
- `0x00A5A8AC` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A5A901` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00A5A93C` → [KeQueryCpuSetInformation](../A8/KeQueryCpuSetInformation_function_00A8ED54.md) (function, `0x00A8ED54`)
- `0x00A5A951` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A5A98B` → [MmGetProcessPartitionId](../../text/47/MmGetProcessPartitionId_function_0047BB44.md) (function, `0x0047BB44`)
- `0x00A5A996` → [MmGetNumberOfPhysicalPages](../../text/46/MmGetNumberOfPhysicalPages_function_00467F80.md) (function, `0x00467F80`)
- `0x00A5A9AA` → [MmGetAvailablePages](../../text/46/MmGetAvailablePages_function_0046A4C0.md) (function, `0x0046A4C0`)
- `0x00A5A9BB` → [MmGetResidentAvailablePages](../../text/46/MmGetResidentAvailablePages_function_0046C480.md) (function, `0x0046C480`)
- `0x00A5A9CC` → [MmGetTotalCommittedPages](../../text/46/MmGetTotalCommittedPages_function_0046B638.md) (function, `0x0046B638`)
- `0x00A5A9DD` → [MmGetTotalCommitLimit](../../text/46/MmGetTotalCommitLimit_function_0046B754.md) (function, `0x0046B754`)
- `0x00A5A9EE` → [MmGetPeakCommitment](../../text/46/MmGetPeakCommitment_function_0046BCF4.md) (function, `0x0046BCF4`)
- `0x00A5A9FF` → [MmGetSharedCommit](../../text/47/MmGetSharedCommit_function_0047BAC0.md) (function, `0x0047BAC0`)
- `0x00A5AAE8` → [PsQueryActivityModerationUserSettings](../../text/5E/PsQueryActivityModerationUserSettings_function_005E2D84.md) (function, `0x005E2D84`)
- `0x00A5AB4C` → [ZwFilterBootOption](../../text/6A/ZwFilterBootOption_function_006AEE50.md) (function, `0x006AEE50`)
- `0x00A5AB5C` → [sub_008D3420](../8D/Unknown_function_008D3420.md) (function, `0x008D3420`)
- `0x00A5AB96` → [MmGetProcessPartitionId](../../text/47/MmGetProcessPartitionId_function_0047BB44.md) (function, `0x0047BB44`)
- `0x00A5ABA1` → [MmGetNumberOfPhysicalPages](../../text/46/MmGetNumberOfPhysicalPages_function_00467F80.md) (function, `0x00467F80`)
- `0x00A5ABB5` → [MmGetLowestPhysicalPage](../../text/48/MmGetLowestPhysicalPage_function_00484310.md) (function, `0x00484310`)
- `0x00A5ABC6` → [MmGetHighestPhysicalPage](../../text/47/MmGetHighestPhysicalPage_function_00479040.md) (function, `0x00479040`)
- `0x00A5AC27` → [ExpQueryCodeIntegrityCertificateInfo](../A8/ExpQueryCodeIntegrityCertificateInfo_function_00A8552C.md) (function, `0x00A8552C`)
- `0x00A5ACBB` → [ExpGetSystemWriteConstraintInformation](../7C/ExpGetSystemWriteConstraintInformation_function_007C4100.md) (function, `0x007C4100`)
- `0x00A5ACE9` → [VslTransformDumpKey](../71/VslTransformDumpKey_function_00719A08.md) (function, `0x00719A08`)
- `0x00A5ACF3` → [KeQueryActiveGroupCount](../../text/48/KeQueryActiveGroupCount_function_0048C600.md) (function, `0x0048C600`)
- `0x00A5AD13` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A5AD44` → [KeInitializeSchedulerSubNodeEnumerationContext](../../text/41/KeInitializeSchedulerSubNodeEnumerationContext_function_0041E4B0.md) (function, `0x0041E4B0`)
- `0x00A5AD59` → [KeEnumerateNextSchedulerSubNodeInNode](../../text/25/KeEnumerateNextSchedulerSubNodeInNode_function_002566D8.md) (function, `0x002566D8`)
- `0x00A5ADCD` → [ExpGetSystemFlushInformation](ExpGetSystemFlushInformation_function_00A540A4.md) (function, `0x00A540A4`)
- `0x00A5ADE2` → [KeQueryKvaShadowInformation](../74/KeQueryKvaShadowInformation_function_00747280.md) (function, `0x00747280`)
- `0x00A5AE21` → [KeQuerySpeculationControlInformation](../74/KeQuerySpeculationControlInformation_function_007468A8.md) (function, `0x007468A8`)
- `0x00A5AE3B` → [IoQuerySystemDeviceName](../A6/IoQuerySystemDeviceName_function_00A6CB24.md) (function, `0x00A6CB24`)
- `0x00A5AE59` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A5AEA2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A5AED9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A5AEFD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A5AF94` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A5B024` → [CmQuerySingleFeatureConfiguration](../AC/CmQuerySingleFeatureConfiguration_function_00AC70A8.md) (function, `0x00AC70A8`)
- `0x00A5B039` → [SeSecurityModelQueryInformation](../79/SeSecurityModelQueryInformation_function_0079D9CC.md) (function, `0x0079D9CC`)
- `0x00A5B0E4` → [CmQueryFeatureConfigurationSections](../A3/CmQueryFeatureConfigurationSections_function_00A300C4.md) (function, `0x00A300C4`)
- `0x00A5B13E` → [KeIsCetCapable](../../text/4C/KeIsCetCapable_function_004CA57C.md) (function, `0x004CA57C`)
- `0x00A5B14B` → [KeIsUserCetAllowed](../../text/4A/KeIsUserCetAllowed_function_004A22B4.md) (function, `0x004A22B4`)
- `0x00A5B15E` → [KeIsKernelCetEnabled](../../text/45/KeIsKernelCetEnabled_function_0045D610.md) (function, `0x0045D610`)
- `0x00A5B170` → [KeIsKernelCetAuditModeEnabled](../../text/4D/KeIsKernelCetAuditModeEnabled_function_004D2F88.md) (function, `0x004D2F88`)
- `0x00A5B1A6` → [WheaQuerySystemInformation](../7D/WheaQuerySystemInformation_function_007D67A0.md) (function, `0x007D67A0`)
- `0x00A5B255` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A5B26A` → [KeQuerySecureSpeculationInformation](../../text/5B/KeQuerySecureSpeculationInformation_function_005BEA14.md) (function, `0x005BEA14`)
- `0x00A5B29F` → [CmQueryBuildVersionInformation](CmQueryBuildVersionInformation_function_00A5E884.md) (function, `0x00A5E884`)
- `0x00A5B2FC` → [KeQueryDpcWatchdogConfiguration](../../text/5B/KeQueryDpcWatchdogConfiguration_function_005B5800.md) (function, `0x005B5800`)
- `0x00A5B321` → [PsGetSupportedProcessorArchitectures](../8D/PsGetSupportedProcessorArchitectures_function_008D1F90.md) (function, `0x008D1F90`)
- `0x00A5B38E` → [ExPoolQueryLimits](../../text/65/ExPoolQueryLimits_function_006562A0.md) (function, `0x006562A0`)
- `0x00A5B3EE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A5B402` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A5B472` → [HvlQuerySetBootPagesInfo](../71/HvlQuerySetBootPagesInfo_function_00717D7C.md) (function, `0x00717D7C`)
- `0x00A5B499` → [HvlQueryMinrootInfo](../../text/58/HvlQueryMinrootInfo_function_00584880.md) (function, `0x00584880`)
- `0x00A5B4B6` → [ExpQueryOriginalImageFeatureInformation](../7D/ExpQueryOriginalImageFeatureInformation_function_007D59E0.md) (function, `0x007D59E0`)
- `0x00A5B516` → [MmEnumerateBadPages](../7F/MmEnumerateBadPages_function_007FDE28.md) (function, `0x007FDE28`)
- `0x00A5B5D8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A5B611` → [VslQueryTrustedAppRuntimeInformation](../71/VslQueryTrustedAppRuntimeInformation_function_007193C4.md) (function, `0x007193C4`)
- `0x00A5B659` → [ExpQuerySystemMemoryNumaPerformanceInformation](../7D/ExpQuerySystemMemoryNumaPerformanceInformation_function_007D5BD4.md) (function, `0x007D5BD4`)
- `0x00A5B67B` → [ExpQuerySystemMemoryNumaInformation](../7D/ExpQuerySystemMemoryNumaInformation_function_007D5A88.md) (function, `0x007D5A88`)
- `0x00A5B709` → [SeCodeIntegrityQueryPolicyInformation](../A4/SeCodeIntegrityQueryPolicyInformation_function_00A4AA7C.md) (function, `0x00A4AA7C`)
- `0x00A5B730` → [ExpQueryRuntimeAttestationReport](../7C/ExpQueryRuntimeAttestationReport_function_007C4EE0.md) (function, `0x007C4EE0`)
- `0x00A5B76E` → [ExpGetProcessInformation](../91/ExpGetProcessInformation_function_0091A878.md) (function, `0x0091A878`)
- `0x00A5B7C9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A5B7E2` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- [NtQuerySystemInformationEx](NtQuerySystemInformationEx_function_00A57690.md) at `0x00A57742`
- [NtQuerySystemInformation](NtQuerySystemInformation_function_00A57780.md) at `0x00A577D8`

### Static image references
- `0x00A5786D` → RVA `0x00E0A740` (`.data`; read)
- `0x00A57C48` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x00A57FD3` → RVA `0x00FC42C0` (`.data`; read)
- `0x00A5800D` → RVA `0x00FD8838` (`PAGEDATA`; read)
- `0x00A58015` → RVA `0x00FD883C` (`PAGEDATA`; read)
- `0x00A5801F` → RVA `0x00FD8840` (`PAGEDATA`; read)
- `0x00A58029` → RVA `0x00FD8844` (`PAGEDATA`; read)
- `0x00A58033` → RVA `0x00FD884C` (`PAGEDATA`; read)
- `0x00A5803D` → RVA `0x00FD8850` (`PAGEDATA`; read)
- `0x00A581E9` → RVA `0x00FC50C0` (`ALMOSTRO`; read)
- `0x00A581F2` → RVA `0x00FC50E8` (`ALMOSTRO`; read)
- `0x00A581FB` → RVA `0x00FC50C4` (`ALMOSTRO`; read)
- `0x00A58204` → RVA `0x00FC51A0` (`ALMOSTRO`; read)
- `0x00A5824C` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x00A5829E` → RVA `0x00FC6B7C` (`ALMOSTRO`; read)
- `0x00A58362` → RVA `0x00F475F8` (`.data`; read)
- `0x00A5836A` → RVA `0x00F475DC` (`.data`; read)
- `0x00A58432` → RVA `0x00FC7070` (`ALMOSTRO`; read)
- `0x00A58439` → RVA `0x00FC5017` (`ALMOSTRO`; read)
- `0x00A58463` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x00A584E0` → RVA `0x00F231C0` (`.data`; read)
- `0x00A584E9` → RVA `0x00F231C8` (`.data`; read)
- `0x00A584F2` → RVA `0x00F231C4` (`.data`; read)
- `0x00A584FB` → RVA `0x00F231CC` (`.data`; read)
- `0x00A58504` → RVA `0x00F231D0` (`.data`; read)
- `0x00A5850D` → RVA `0x00F231D8` (`.data`; read)
- `0x00A58516` → RVA `0x00F231D4` (`.data`; read)
- `0x00A5851F` → RVA `0x00F231DC` (`.data`; read)
- `0x00A58528` → RVA `0x00F231E0` (`.data`; read)
- `0x00A58531` → RVA `0x00F231E4` (`.data`; read)
- `0x00A5853A` → RVA `0x00F231E8` (`.data`; read)
- `0x00A58CD1` → RVA `0x00E0B384` (`.data`; read)
- `0x00A58D41` → RVA `0x00FD9B20` (`PAGEDATA`; read)
- `0x00A58DDB` → RVA `0x00E00B30` (`.data`; read)
- `0x00A58DF7` → RVA `0x004FC600` (`BvgaSetVirtualFrameBuffer`; read)
- `0x00A58DFE` → RVA `0x00E00B38` (`.data`; read)
- `0x00A58FF4` → RVA `0x00FC6C28` (`ALMOSTRO`; read)
- `0x00A58FFE` → RVA `0x00FC5124` (`ALMOSTRO`; read)
- `0x00A59113` → RVA `0x00EFF040` (`.data`; read)
- `0x00A5911E` → RVA `0x00EFF050` (`.data`; read)
- `0x00A59132` → RVA `0x00EFF058` (`.data`; read)
- `0x00A59231` → RVA `0x00E00638` (`.data`; read)
- `0x00A59830` → RVA `0x00FC51DC` (`ALMOSTRO`; read)
- `0x00A59838` → RVA `0x00FC5388` (`ALMOSTRO`; read)
- `0x00A59B29` → RVA `0x00FC50A8` (`ALMOSTRO`; read)
- `0x00A59CC8` → RVA `0x00FD9A78` (`PAGEDATA`; read)
- `0x00A5A09C` → RVA `0x00E0AA1D` (`.data`; read)
- `0x00A5A109` → RVA `0x00E68544` (`.data`; read)
- `0x00A5A181` → RVA `0x00EFF06A` (`.data`; read)
- `0x00A5A1A8` → RVA `0x00EFF060` (`.data`; read)
- `0x00A5A1B0` → RVA `0x00EFF068` (`.data`; read)
- `0x00A5A1DC` → RVA `0x00EFF070` (`.data`; read)
- `0x00A5A29E` → RVA `0x00F0F200` (`.data`; read)
- `0x00A5A2A6` → RVA `0x00F0F204` (`.data`; read)
- `0x00A5A2AF` → RVA `0x00F0F208` (`.data`; read)
- `0x00A5A2B8` → RVA `0x00F0F210` (`.data`; read)
- `0x00A5A2C3` → RVA `0x00F0F218` (`.data`; read)
- `0x00A5A3AE` → RVA `0x00EFF078` (`.data`; read)
- `0x00A5A51A` → RVA `0x00F55CA0` (`.data`; read)
- `0x00A5A7B8` → RVA `0x00FC6A98` (`ALMOSTRO`; read)
- `0x00A5A845` → RVA `0x00FD9B48` (`PAGEDATA`; read)
- `0x00A5AD31` → RVA `0x00FCF6C0` (`CACHEALI`; read)
- `0x00A5AF2C` → RVA `0x00E2DB78` (`.data`; read)
- `0x00A5B063` → RVA `0x00FC43C0` (`.data`; read)
- `0x00A5B095` → RVA `0x00EFEE38` (`.data`; read)
- `0x00A5B1C9` → RVA `0x00EFF028` (`.data`; read)
- `0x00A5B21A` → RVA `0x00EFF020` (`.data`; read)
- `0x00A5B690` → RVA `0x00EFF030` (`.data`; read)
- `0x00A5B795` → RVA `0x00FC7458` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **116**
  - `0x00A57923` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A57BCC` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (`PAGE` → `.text`)
  - `0x00A57C83` → [KeQueryActiveGroupCount](../../text/48/KeQueryActiveGroupCount_function_0048C600.md) (`PAGE` → `.text`)
  - `0x00A57E61` → [KeQueryBootTimeValues](../../text/49/KeQueryBootTimeValues_function_0049F444.md) (`PAGE` → `.text`)
  - `0x00A57E66` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x00A57EB1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A57F36` → [ExpGetSystemProcessorInformation](../../text/26/ExpGetSystemProcessorInformation_function_00265AFC.md) (`PAGE` → `.text`)
  - `0x00A58279` → [KeGetProcessorIndexFromNumber](../../text/2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (`PAGE` → `.text`)
  - `0x00A58581` → [ExpGetLookasideInformation](../../text/4E/ExpGetLookasideInformation_function_004E2468.md) (`PAGE` → `.text`)
  - `0x00A585AC` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x00A58733` → [PoGetIdleTimes](../../text/2D/PoGetIdleTimes_function_002DF570.md) (`PAGE` → `.text`)
  - `0x00A588F6` → [VfGetVerifierInformation](../../text/61/VfGetVerifierInformation_function_006167C4.md) (`PAGE` → `.text`)
  - `0x00A58920` → [KeGetRecommendedSharedDataAlignment](../../text/49/KeGetRecommendedSharedDataAlignment_function_00494040.md) (`PAGE` → `.text`)
  - `0x00A58979` → [ExpGetSystemEmulationProcessorInformation](../../text/26/ExpGetSystemEmulationProcessorInformation_function_0026603C.md) (`PAGE` → `.text`)
  - `0x00A589A1` → [ExpGetSystemEmulationBasicInformation](../../text/47/ExpGetSystemEmulationBasicInformation_function_0047486C.md) (`PAGE` → `.text`)
  - `0x00A58A05` → [KeGetProcessorIndexFromNumber](../../text/2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (`PAGE` → `.text`)
  - `0x00A58A2D` → [PoGetPerfStateAndParkingInfo](../../text/2D/PoGetPerfStateAndParkingInfo_function_002DD484.md) (`PAGE` → `.text`)
  - `0x00A58A3B` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A58C4E` → [ExGetBigPoolInfo](../../text/44/ExGetBigPoolInfo_function_00446970.md) (`PAGE` → `.text`)
  - `0x00A58DE2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A58E29` → [MmQueryMemoryListInformation](../../text/3B/MmQueryMemoryListInformation_function_003B9EDC.md) (`PAGE` → `.text`)
  - `0x00A58F61` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00A58FA3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00A58FAB` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00A5906B` → [KeFlushProcessWriteBuffers](../../text/2C/KeFlushProcessWriteBuffers_function_002CE4FC.md) (`PAGE` → `.text`)
  - `0x00A59099` → [KeGetProcessorIndexFromNumber](../../text/2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (`PAGE` → `.text`)
  - `0x00A591B0` → [VfGetVerifierInformationEx](../../pagevrfy/BA/VfGetVerifierInformationEx_function_00BAC47C.md) (`PAGE` → `PAGEVRFY`)
  - `0x00A59245` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A59288` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A592BF` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A592DF` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A59340` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x00A5947B` → [KeQueryGroupAffinity](../../text/47/KeQueryGroupAffinity_function_00471A60.md) (`PAGE` → `.text`)
  - `0x00A594AE` → [PpmCapturePerformanceDistribution](../../text/48/PpmCapturePerformanceDistribution_function_00489C88.md) (`PAGE` → `.text`)
  - `0x00A594E7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A59527` → [PpmCapturePerformanceDistribution](../../text/48/PpmCapturePerformanceDistribution_function_00489C88.md) (`PAGE` → `.text`)
  - `0x00A5953F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A5955C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A595A6` → [PsQueryCpuQuotaInformation](../../text/5E/PsQueryCpuQuotaInformation_function_005E27C0.md) (`PAGE` → `.text`)
  - `0x00A5964F` → [KeGetProcessorIndexFromNumber](../../text/2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (`PAGE` → `.text`)
  - `0x00A596EB` → [KeQueryLogicalProcessorRelationship](../../text/2C/KeQueryLogicalProcessorRelationship_function_002CEA60.md) (`PAGE` → `.text`)
  - `0x00A59707` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A59750` → [ExpGetSystemBasicInformation](../../text/45/ExpGetSystemBasicInformation_function_004572E4.md) (`PAGE` → `.text`)
  - `0x00A5988E` → [MmQuerySystemWorkingSetInformation](../../text/2C/MmQuerySystemWorkingSetInformation_function_002C0710.md) (`PAGE` → `.text`)
  - `0x00A599BD` → [MmGetProcessPartitionId](../../text/47/MmGetProcessPartitionId_function_0047BB44.md) (`PAGE` → `.text`)
  - `0x00A599C5` → [MmGetAvailablePages](../../text/46/MmGetAvailablePages_function_0046A4C0.md) (`PAGE` → `.text`)
  - `0x00A599D2` → [MmGetTotalCommittedPages](../../text/46/MmGetTotalCommittedPages_function_0046B638.md) (`PAGE` → `.text`)
  - `0x00A599DF` → [MmGetTotalCommitLimit](../../text/46/MmGetTotalCommitLimit_function_0046B754.md) (`PAGE` → `.text`)
  - `0x00A599EC` → [MmGetPeakCommitment](../../text/46/MmGetPeakCommitment_function_0046BCF4.md) (`PAGE` → `.text`)
  - `0x00A59A6A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A59A96` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A59B73` → [BgkQueryBootGraphicsInformation](../../pagebgfx/BC/BgkQueryBootGraphicsInformation_function_00BC0064.md) (`PAGE` → `PAGEBGFX`)
  - `0x00A59BAD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A59C5C` → [HvlQueryActiveProcessors](../../text/58/HvlQueryActiveProcessors_function_005847B0.md) (`PAGE` → `.text`)
  - `0x00A59C73` → [HvlQueryProcessorTopologyCount](../../text/58/HvlQueryProcessorTopologyCount_function_00584B20.md) (`PAGE` → `.text`)
  - `0x00A59DC9` → [KeGetProcessorIndexFromNumber](../../text/2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (`PAGE` → `.text`)
  - `0x00A59E0A` → [PoGetIdleTimes](../../text/2D/PoGetIdleTimes_function_002DF570.md) (`PAGE` → `.text`)
  - `0x00A59EF7` → [BgkQueryBootGraphicsInformation](../../pagebgfx/BC/BgkQueryBootGraphicsInformation_function_00BC0064.md) (`PAGE` → `PAGEBGFX`)
  - `0x00A59F28` → [BgkQueryBootGraphicsInformation](../../pagebgfx/BC/BgkQueryBootGraphicsInformation_function_00BC0064.md) (`PAGE` → `PAGEBGFX`)
  - `0x00A59F55` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A5A06D` → [ExpQueryBootLoaderMetadata](../../text/65/ExpQueryBootLoaderMetadata_function_00654E8C.md) (`PAGE` → `.text`)
  - `0x00A5A170` → [PoEnergyEstimationEnabled](../../text/45/PoEnergyEstimationEnabled_function_00450000.md) (`PAGE` → `.text`)
  - `0x00A5A1E3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A5A21C` → [BgkQueryBootGraphicsInformation](../../pagebgfx/BC/BgkQueryBootGraphicsInformation_function_00BC0064.md) (`PAGE` → `PAGEBGFX`)
  - `0x00A5A23D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A5A3CC` → [VslIsSecureKernelRunning](../../text/4C/VslIsSecureKernelRunning_function_004C75F4.md) (`PAGE` → `.text`)
  - `0x00A5A3EA` → [VslGetNestedPageProtectionFlags](../../text/2F/VslGetNestedPageProtectionFlags_function_002F2164.md) (`PAGE` → `.text`)
  - `0x00A5A44A` → [VslIsTrustletRunning](../../text/4B/VslIsTrustletRunning_function_004BDC88.md) (`PAGE` → `.text`)
  - `0x00A5A53C` → [SeQueryTrustedPlatformModuleInformation](../../text/60/SeQueryTrustedPlatformModuleInformation_function_00609B74.md) (`PAGE` → `.text`)
  - `0x00A5A5B1` → [KeGetProcessorIndexFromNumber](../../text/2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (`PAGE` → `.text`)
  - `0x00A5A5BF` → [KeQueryCycleTimeStatsProcessor](../../text/48/KeQueryCycleTimeStatsProcessor_function_0048665C.md) (`PAGE` → `.text`)
  - `0x00A5A640` → [ExCpuSetResourceManagerAccessCheck](../../text/3A/ExCpuSetResourceManagerAccessCheck_function_003A5444.md) (`PAGE` → `.text`)
  - `0x00A5A670` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A5A6A2` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A5A6AA` → [KeGetAffinitizedInterruptsInfo](../../text/5C/KeGetAffinitizedInterruptsInfo_function_005C5634.md) (`PAGE` → `.text`)
  - `0x00A5A71E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A5A867` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A5A890` → [VslQuerySecureKernelProfileInformation](../../text/58/VslQuerySecureKernelProfileInformation_function_0058EED8.md) (`PAGE` → `.text`)
  - `0x00A5A8AC` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A5A951` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A5A98B` → [MmGetProcessPartitionId](../../text/47/MmGetProcessPartitionId_function_0047BB44.md) (`PAGE` → `.text`)
  - `0x00A5A996` → [MmGetNumberOfPhysicalPages](../../text/46/MmGetNumberOfPhysicalPages_function_00467F80.md) (`PAGE` → `.text`)
  - `0x00A5A9AA` → [MmGetAvailablePages](../../text/46/MmGetAvailablePages_function_0046A4C0.md) (`PAGE` → `.text`)
  - `0x00A5A9BB` → [MmGetResidentAvailablePages](../../text/46/MmGetResidentAvailablePages_function_0046C480.md) (`PAGE` → `.text`)
  - `0x00A5A9CC` → [MmGetTotalCommittedPages](../../text/46/MmGetTotalCommittedPages_function_0046B638.md) (`PAGE` → `.text`)
  - `0x00A5A9DD` → [MmGetTotalCommitLimit](../../text/46/MmGetTotalCommitLimit_function_0046B754.md) (`PAGE` → `.text`)
  - `0x00A5A9EE` → [MmGetPeakCommitment](../../text/46/MmGetPeakCommitment_function_0046BCF4.md) (`PAGE` → `.text`)
  - `0x00A5A9FF` → [MmGetSharedCommit](../../text/47/MmGetSharedCommit_function_0047BAC0.md) (`PAGE` → `.text`)
  - `0x00A5AAE8` → [PsQueryActivityModerationUserSettings](../../text/5E/PsQueryActivityModerationUserSettings_function_005E2D84.md) (`PAGE` → `.text`)
  - `0x00A5AB4C` → [ZwFilterBootOption](../../text/6A/ZwFilterBootOption_function_006AEE50.md) (`PAGE` → `.text`)
  - `0x00A5AB96` → [MmGetProcessPartitionId](../../text/47/MmGetProcessPartitionId_function_0047BB44.md) (`PAGE` → `.text`)
  - `0x00A5ABA1` → [MmGetNumberOfPhysicalPages](../../text/46/MmGetNumberOfPhysicalPages_function_00467F80.md) (`PAGE` → `.text`)
  - `0x00A5ABB5` → [MmGetLowestPhysicalPage](../../text/48/MmGetLowestPhysicalPage_function_00484310.md) (`PAGE` → `.text`)
  - `0x00A5ABC6` → [MmGetHighestPhysicalPage](../../text/47/MmGetHighestPhysicalPage_function_00479040.md) (`PAGE` → `.text`)
  - `0x00A5ACF3` → [KeQueryActiveGroupCount](../../text/48/KeQueryActiveGroupCount_function_0048C600.md) (`PAGE` → `.text`)
  - `0x00A5AD13` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A5AD44` → [KeInitializeSchedulerSubNodeEnumerationContext](../../text/41/KeInitializeSchedulerSubNodeEnumerationContext_function_0041E4B0.md) (`PAGE` → `.text`)
  - `0x00A5AD59` → [KeEnumerateNextSchedulerSubNodeInNode](../../text/25/KeEnumerateNextSchedulerSubNodeInNode_function_002566D8.md) (`PAGE` → `.text`)
  - `0x00A5AE59` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A5AEA2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A5AED9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A5AEFD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A5AF94` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A5B13E` → [KeIsCetCapable](../../text/4C/KeIsCetCapable_function_004CA57C.md) (`PAGE` → `.text`)
  - `0x00A5B14B` → [KeIsUserCetAllowed](../../text/4A/KeIsUserCetAllowed_function_004A22B4.md) (`PAGE` → `.text`)
  - `0x00A5B15E` → [KeIsKernelCetEnabled](../../text/45/KeIsKernelCetEnabled_function_0045D610.md) (`PAGE` → `.text`)
  - `0x00A5B170` → [KeIsKernelCetAuditModeEnabled](../../text/4D/KeIsKernelCetAuditModeEnabled_function_004D2F88.md) (`PAGE` → `.text`)
  - `0x00A5B255` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A5B26A` → [KeQuerySecureSpeculationInformation](../../text/5B/KeQuerySecureSpeculationInformation_function_005BEA14.md) (`PAGE` → `.text`)
  - `0x00A5B2FC` → [KeQueryDpcWatchdogConfiguration](../../text/5B/KeQueryDpcWatchdogConfiguration_function_005B5800.md) (`PAGE` → `.text`)
  - `0x00A5B38E` → [ExPoolQueryLimits](../../text/65/ExPoolQueryLimits_function_006562A0.md) (`PAGE` → `.text`)
  - `0x00A5B3EE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A5B402` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A5B499` → [HvlQueryMinrootInfo](../../text/58/HvlQueryMinrootInfo_function_00584880.md) (`PAGE` → `.text`)
  - `0x00A5B5D8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A5B7C9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A57858  4C 8B DC                        mov r11, rsp
00A5785B  53                              push rbx
00A5785C  56                              push rsi
00A5785D  57                              push rdi
00A5785E  41 54                           push r12
00A57860  41 55                           push r13
00A57862  41 56                           push r14
00A57864  41 57                           push r15
00A57866  48 81 EC B0 03 00 00            sub rsp, 0x3b0
00A5786D  48 8B 05 CC 2E 3B 00            mov rax, qword ptr [rip + 0x3b2ecc]
00A57874  48 33 C4                        xor rax, rsp
00A57877  48 89 84 24 A8 03 00 00         mov qword ptr [rsp + 0x3a8], rax
00A5787F  49 8B F9                        mov rdi, r9
00A57882  44 89 44 24 58                  mov dword ptr [rsp + 0x58], r8d
00A57887  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
00A5788C  8B D9                           mov ebx, ecx
00A5788E  4C 8B BC 24 18 04 00 00         mov r15, qword ptr [rsp + 0x418]
00A57896  44 8B B4 24 10 04 00 00         mov r14d, dword ptr [rsp + 0x410]
00A5789E  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
00A578A3  33 F6                           xor esi, esi
00A578A5  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
00A578A9  49 89 B3 90 FD FF FF            mov qword ptr [r11 - 0x270], rsi
00A578B0  89 B4 24 2C 01 00 00            mov dword ptr [rsp + 0x12c], esi
00A578B7  89 B4 24 30 01 00 00            mov dword ptr [rsp + 0x130], esi
00A578BE  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
00A578C2  89 B4 24 3C 01 00 00            mov dword ptr [rsp + 0x13c], esi
00A578C9  66 89 74 24 78                  mov word ptr [rsp + 0x78], si
00A578CE  66 89 74 24 54                  mov word ptr [rsp + 0x54], si
00A578D3  0F 57 C0                        xorps xmm0, xmm0
00A578D6  0F 11 84 24 A0 01 00 00         movups xmmword ptr [rsp + 0x1a0], xmm0
00A578DE  49 89 B3 38 FD FF FF            mov qword ptr [r11 - 0x2c8], rsi
00A578E5  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
00A578E9  49 89 B3 70 FD FF FF            mov qword ptr [r11 - 0x290], rsi
00A578F0  49 89 B3 58 FD FF FF            mov qword ptr [r11 - 0x2a8], rsi
00A578F7  89 B4 24 38 01 00 00            mov dword ptr [rsp + 0x138], esi
00A578FE  89 74 24 5C                     mov dword ptr [rsp + 0x5c], esi
00A57902  49 89 B3 A8 FD FF FF            mov qword ptr [r11 - 0x258], rsi
00A57909  33 C0                           xor eax, eax
00A5790B  41 0F 11 43 A8                  movups xmmword ptr [r11 - 0x58], xmm0
00A57910  49 89 43 B8                     mov qword ptr [r11 - 0x48], rax
00A57914  33 D2                           xor edx, edx
00A57916  41 B8 B0 01 00 00               mov r8d, 0x1b0
00A5791C  49 8D 8B F8 FD FF FF            lea rcx, [r11 - 0x208]
00A57923  E8 18 F3 C6 FF                  call 0x1406c6c40
00A57928  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00A5792C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A57935  8A 80 32 02 00 00               mov al, byte ptr [rax + 0x232]
00A5793B  88 44 24 38                     mov byte ptr [rsp + 0x38], al
00A5793F  84 C0                           test al, al
00A57941  0F 84 7B 01 00 00               je 0x140a57ac2
00A57947  B8 9D 00 00 00                  mov eax, 0x9d
00A5794C  3B D8                           cmp ebx, eax
00A5794E  0F 8F A0 00 00 00               jg 0x140a579f4
00A57954  0F 84 22 01 00 00               je 0x140a57a7c
00A5795A  83 FB 7E                        cmp ebx, 0x7e
00A5795D  7F 49                           jg 0x140a579a8
00A5795F  0F 84 17 01 00 00               je 0x140a57a7c
00A57965  83 FB 05                        cmp ebx, 5
00A57968  0F 84 0E 01 00 00               je 0x140a57a7c
00A5796E  83 FB 0C                        cmp ebx, 0xc
00A57971  74 26                           je 0x140a57999
00A57973  83 FB 11                        cmp ebx, 0x11
00A57976  0F 84 00 01 00 00               je 0x140a57a7c
00A5797C  83 FB 23                        cmp ebx, 0x23
00A5797F  0F 85 F7 00 00 00               jne 0x140a57a7c
00A57985  41 BC 02 00 00 00               mov r12d, 2
00A5798B  41 BD 01 00 00 00               mov r13d, 1
00A57991  45 8B C5                        mov r8d, r13d
00A57994  E9 F5 00 00 00                  jmp 0x140a57a8e
00A57999  41 B8 08 00 00 00               mov r8d, 8
00A5799F  45 8D 60 FA                     lea r12d, [r8 - 6]
00A579A3  E9 E0 00 00 00                  jmp 0x140a57a88
00A579A8  8B CB                           mov ecx, ebx
00A579AA  81 E9 85 00 00 00               sub ecx, 0x85
00A579B0  0F 84 C6 00 00 00               je 0x140a57a7c
00A579B6  83 E9 05                        sub ecx, 5
00A579B9  0F 84 BD 00 00 00               je 0x140a57a7c
00A579BF  83 E9 01                        sub ecx, 1
00A579C2  0F 84 B4 00 00 00               je 0x140a57a7c
00A579C8  83 E9 01                        sub ecx, 1
00A579CB  41 BC 02 00 00 00               mov r12d, 2
00A579D1  0F 84 AB 00 00 00               je 0x140a57a82
00A579D7  83 E9 05                        sub ecx, 5
00A579DA  74 AF                           je 0x140a5798b
00A579DC  41 2B CC                        sub ecx, r12d
00A579DF  74 AA                           je 0x140a5798b
00A579E1  83 E9 01                        sub ecx, 1
00A579E4  0F 84 98 00 00 00               je 0x140a57a82
00A579EA  83 E9 01                        sub ecx, 1
00A579ED  74 9C                           je 0x140a5798b
00A579EF  E9 8E 00 00 00                  jmp 0x140a57a82
00A579F4  81 FB CA 00 00 00               cmp ebx, 0xca
00A579FA  7F 49                           jg 0x140a57a45
00A579FC  41 BC 02 00 00 00               mov r12d, 2
00A57A02  74 87                           je 0x140a5798b
00A57A04  8B CB                           mov ecx, ebx
00A57A06  81 E9 9E 00 00 00               sub ecx, 0x9e
00A57A0C  0F 84 79 FF FF FF               je 0x140a5798b
00A57A12  41 2B CC                        sub ecx, r12d
00A57A15  74 6B                           je 0x140a57a82
00A57A17  41 8D 44 24 01                  lea eax, [r12 + 1]
00A57A1C  2B C8                           sub ecx, eax
00A57A1E  0F 84 67 FF FF FF               je 0x140a5798b
00A57A24  83 E9 06                        sub ecx, 6
00A57A27  0F 84 5E FF FF FF               je 0x140a5798b
00A57A2D  83 E9 04                        sub ecx, 4
00A57A30  74 50                           je 0x140a57a82
00A57A32  83 E9 0F                        sub ecx, 0xf
00A57A35  74 4B                           je 0x140a57a82
00A57A37  83 E9 04                        sub ecx, 4
00A57A3A  74 46                           je 0x140a57a82
00A57A3C  2B C8                           sub ecx, eax
00A57A3E  74 42                           je 0x140a57a82
00A57A40  41 3B CC                        cmp ecx, r12d
00A57A43  EB 3D                           jmp 0x140a57a82
00A57A45  8B CB                           mov ecx, ebx
00A57A47  81 E9 D2 00 00 00               sub ecx, 0xd2
00A57A4D  74 2D                           je 0x140a57a7c
00A57A4F  83 E9 01                        sub ecx, 1
00A57A52  74 28                           je 0x140a57a7c
00A57A54  83 E9 05                        sub ecx, 5
00A57A57  74 23                           je 0x140a57a7c
00A57A59  83 E9 06                        sub ecx, 6
00A57A5C  74 1E                           je 0x140a57a7c
00A57A5E  83 E9 05                        sub ecx, 5
00A57A61  0F 84 1E FF FF FF               je 0x140a57985
00A57A67  83 E9 10                        sub ecx, 0x10
00A57A6A  41 BC 02 00 00 00               mov r12d, 2
00A57A70  74 10                           je 0x140a57a82
00A57A72  83 E9 07                        sub ecx, 7
00A57A75  74 0B                           je 0x140a57a82
00A57A77  41 2B CC                        sub ecx, r12d
00A57A7A  EB 06                           jmp 0x140a57a82
00A57A7C  41 BC 02 00 00 00               mov r12d, 2
00A57A82  41 B8 04 00 00 00               mov r8d, 4
00A57A88  41 BD 01 00 00 00               mov r13d, 1
00A57A8E  49 8B D6                        mov rdx, r14
00A57A91  48 8B CF                        mov rcx, rdi
00A57A94  E8 27 17 E9 FF                  call 0x1408e91c0
00A57A99  4D 85 FF                        test r15, r15
00A57A9C  74 18                           je 0x140a57ab6
00A57A9E  49 BB 00 00 FF FF FF 7F 00 00   movabs r11, 0x7fffffff0000
00A57AA8  49 8B CB                        mov rcx, r11
00A57AAB  4D 3B FB                        cmp r15, r11
00A57AAE  49 0F 42 CF                     cmovb rcx, r15
00A57AB2  8B 01                           mov eax, dword ptr [rcx]
00A57AB4  89 01                           mov dword ptr [rcx], eax
00A57AB6  B9 03 00 00 00                  mov ecx, 3
00A57ABB  EB 12                           jmp 0x140a57acf
00A57ABD  E9 FC 3C 00 00                  jmp 0x140a5b7be
00A57AC2  B9 03 00 00 00                  mov ecx, 3
00A57AC7  44 8D 61 FF                     lea r12d, [rcx - 1]
00A57ACB  44 8D 69 FE                     lea r13d, [rcx - 2]
00A57ACF  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
00A57AD3  41 BB FF FF 00 00               mov r11d, 0xffff
00A57AD9  44 89 9C 24 18 01 00 00         mov dword ptr [rsp + 0x118], r11d
00A57AE1  44 8B CE                        mov r9d, esi
00A57AE4  89 74 24 64                     mov dword ptr [rsp + 0x64], esi
00A57AE8  44 0F B7 D6                     movzx r10d, si
00A57AEC  44 89 54 24 68                  mov dword ptr [rsp + 0x68], r10d
00A57AF1  66 89 74 24 54                  mov word ptr [rsp + 0x54], si
00A57AF6  66 89 74 24 78                  mov word ptr [rsp + 0x78], si
00A57AFB  48 89 B4 24 48 01 00 00         mov qword ptr [rsp + 0x148], rsi
00A57B03  4C 8B C6                        mov r8, rsi
00A57B06  48 89 B4 24 50 01 00 00         mov qword ptr [rsp + 0x150], rsi
00A57B0E  48 89 B4 24 80 01 00 00         mov qword ptr [rsp + 0x180], rsi
00A57B16  BA 09 00 00 00                  mov edx, 9
00A57B1B  89 94 24 80 00 00 00            mov dword ptr [rsp + 0x80], edx
00A57B22  89 94 24 38 01 00 00            mov dword ptr [rsp + 0x138], edx
00A57B29  83 FB 64                        cmp ebx, 0x64
00A57B2C  0F 8F C4 00 00 00               jg 0x140a57bf6
00A57B32  0F 84 2C 01 00 00               je 0x140a57c64
00A57B38  83 FB 2A                        cmp ebx, 0x2a
00A57B3B  7F 36                           jg 0x140a57b73
00A57B3D  0F 84 21 01 00 00               je 0x140a57c64
00A57B43  41 3B DC                        cmp ebx, r12d
00A57B46  74 78                           je 0x140a57bc0
00A57B48  83 FB 08                        cmp ebx, 8
00A57B4B  0F 84 13 01 00 00               je 0x140a57c64
00A57B51  83 FB 17                        cmp ebx, 0x17
00A57B54  0F 84 0A 01 00 00               je 0x140a57c64
00A57B5A  83 FB 21                        cmp ebx, 0x21
00A57B5D  74 61                           je 0x140a57bc0
00A57B5F  83 FB 24                        cmp ebx, 0x24
00A57B62  74 5C                           je 0x140a57bc0
00A57B64  44 8B 5C 24 58                  mov r11d, dword ptr [rsp + 0x58]
00A57B69  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A57B6E  E9 34 02 00 00                  jmp 0x140a57da7
00A57B73  8B CB                           mov ecx, ebx
00A57B75  83 E9 3D                        sub ecx, 0x3d
00A57B78  0F 84 E6 00 00 00               je 0x140a57c64
00A57B7E  83 E9 04                        sub ecx, 4
00A57B81  74 3D                           je 0x140a57bc0
00A57B83  83 E9 07                        sub ecx, 7
00A57B86  74 11                           je 0x140a57b99
00A57B88  83 E9 01                        sub ecx, 1
00A57B8B  0F 84 D3 00 00 00               je 0x140a57c64
00A57B91  83 F9 0A                        cmp ecx, 0xa
00A57B94  E9 8D 00 00 00                  jmp 0x140a57c26
00A57B99  44 8B 5C 24 58                  mov r11d, dword ptr [rsp + 0x58]
00A57B9E  41 83 FB 04                     cmp r11d, 4
00A57BA2  0F 85 11 3C 00 00               jne 0x140a5b7b9
00A57BA8  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A57BAD  8B 11                           mov edx, dword ptr [rcx]
00A57BAF  89 94 24 38 01 00 00            mov dword ptr [rsp + 0x138], edx
00A57BB6  E9 EC 01 00 00                  jmp 0x140a57da7
00A57BBB  E9 FE 3B 00 00                  jmp 0x140a5b7be
00A57BC0  41 8B CB                        mov ecx, r11d
00A57BC3  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
00A57BC7  66 89 4C 24 54                  mov word ptr [rsp + 0x54], cx
00A57BCC  E8 1F 23 7F FF                  call 0x140249ef0
00A57BD1  44 8B C8                        mov r9d, eax
00A57BD4  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00A57BD8  44 8B 54 24 68                  mov r10d, dword ptr [rsp + 0x68]
00A57BDD  44 8B 5C 24 58                  mov r11d, dword ptr [rsp + 0x58]
00A57BE2  8B 94 24 80 00 00 00            mov edx, dword ptr [rsp + 0x80]
00A57BE9  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A57BEE  4C 8B C6                        mov r8, rsi
00A57BF1  E9 B1 01 00 00                  jmp 0x140a57da7
00A57BF6  B8 A5 00 00 00                  mov eax, 0xa5
00A57BFB  3B D8                           cmp ebx, eax
00A57BFD  0F 8F FE 00 00 00               jg 0x140a57d01
00A57C03  0F 84 BD 00 00 00               je 0x140a57cc6
00A57C09  8B CB                           mov ecx, ebx
00A57C0B  83 E9 6B                        sub ecx, 0x6b
00A57C0E  0F 84 8B 00 00 00               je 0x140a57c9f
00A57C14  83 E9 01                        sub ecx, 1
00A57C17  74 4B                           je 0x140a57c64
00A57C19  83 E9 0D                        sub ecx, 0xd
00A57C1C  74 0F                           je 0x140a57c2d
00A57C1E  83 E9 14                        sub ecx, 0x14
00A57C21  74 41                           je 0x140a57c64
00A57C23  83 F9 13                        cmp ecx, 0x13
00A57C26  74 3C                           je 0x140a57c64
00A57C28  E9 37 FF FF FF                  jmp 0x140a57b64
00A57C2D  44 8B 5C 24 58                  mov r11d, dword ptr [rsp + 0x58]
00A57C32  45 3B DC                        cmp r11d, r12d
00A57C35  0F 82 7E 3B 00 00               jb 0x140a5b7b9
00A57C3B  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A57C40  0F B7 01                        movzx eax, word ptr [rcx]
00A57C43  66 89 44 24 78                  mov word ptr [rsp + 0x78], ax
00A57C48  0F B7 05 B1 D3 56 00            movzx eax, word ptr [rip + 0x56d3b1]
00A57C4F  66 39 44 24 78                  cmp word ptr [rsp + 0x78], ax
00A57C54  0F 83 5F 3B 00 00               jae 0x140a5b7b9
00A57C5A  E9 48 01 00 00                  jmp 0x140a57da7
00A57C5F  E9 5A 3B 00 00                  jmp 0x140a5b7be
00A57C64  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00A57C68  41 3B C4                        cmp eax, r12d
00A57C6B  0F 82 48 3B 00 00               jb 0x140a5b7b9
00A57C71  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
00A57C76  41 0F B7 02                     movzx eax, word ptr [r10]
00A57C7A  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00A57C7E  66 89 44 24 54                  mov word ptr [rsp + 0x54], ax
00A57C83  E8 78 49 A3 FF                  call 0x14048c600
00A57C88  8B 4C 24 68                     mov ecx, dword ptr [rsp + 0x68]
00A57C8C  66 3B C8                        cmp cx, ax
00A57C8F  0F 83 24 3B 00 00               jae 0x140a5b7b9
00A57C95  E9 32 FF FF FF                  jmp 0x140a57bcc
00A57C9A  E9 1F 3B 00 00                  jmp 0x140a5b7be
00A57C9F  44 8B 5C 24 58                  mov r11d, dword ptr [rsp + 0x58]
00A57CA4  41 83 FB 04                     cmp r11d, 4
00A57CA8  0F 82 0B 3B 00 00               jb 0x140a5b7b9
00A57CAE  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A57CB3  8B 01                           mov eax, dword ptr [rcx]
00A57CB5  89 84 24 18 01 00 00            mov dword ptr [rsp + 0x118], eax
00A57CBC  E9 E6 00 00 00                  jmp 0x140a57da7
00A57CC1  E9 F8 3A 00 00                  jmp 0x140a5b7be
00A57CC6  44 8B 5C 24 58                  mov r11d, dword ptr [rsp + 0x58]
00A57CCB  45 85 DB                        test r11d, r11d
00A57CCE  74 24                           je 0x140a57cf4
00A57CD0  41 83 FB 08                     cmp r11d, 8
00A57CD4  0F 85 DF 3A 00 00               jne 0x140a5b7b9
00A57CDA  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A57CDF  48 8B 01                        mov rax, qword ptr [rcx]
00A57CE2  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
00A57CEA  E9 7F FE FF FF                  jmp 0x140a57b6e
00A57CEF  E9 CA 3A 00 00                  jmp 0x140a5b7be
00A57CF4  48 89 B4 24 48 01 00 00         mov qword ptr [rsp + 0x148], rsi
00A57CFC  E9 68 FE FF FF                  jmp 0x140a57b69
00A57D01  8B D3                           mov edx, ebx
00A57D03  81 EA AF 00 00 00               sub edx, 0xaf
00A57D09  74 76                           je 0x140a57d81
00A57D0B  2B D1                           sub edx, ecx
00A57D0D  74 4C                           je 0x140a57d5b
00A57D0F  2B D1                           sub edx, ecx
00A57D11  74 6E                           je 0x140a57d81
00A57D13  83 EA 31                        sub edx, 0x31
00A57D16  74 69                           je 0x140a57d81
00A57D18  44 8B 5C 24 58                  mov r11d, dword ptr [rsp + 0x58]
00A57D1D  83 FA 01                        cmp edx, 1
00A57D20  75 2D                           jne 0x140a57d4f
00A57D22  41 83 FB 08                     cmp r11d, 8
00A57D26  0F 82 8D 3A 00 00               jb 0x140a5b7b9
00A57D2C  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A57D31  8B 41 04                        mov eax, dword ptr [rcx + 4]
00A57D34  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
00A57D38  8B 01                           mov eax, dword ptr [rcx]
00A57D3A  89 84 24 18 01 00 00            mov dword ptr [rsp + 0x118], eax
00A57D41  8B 94 24 80 00 00 00            mov edx, dword ptr [rsp + 0x80]
00A57D48  EB 5D                           jmp 0x140a57da7
00A57D4A  E9 6F 3A 00 00                  jmp 0x140a5b7be
00A57D4F  8B 94 24 80 00 00 00            mov edx, dword ptr [rsp + 0x80]
00A57D56  E9 0E FE FF FF                  jmp 0x140a57b69
00A57D5B  44 8B 5C 24 58                  mov r11d, dword ptr [rsp + 0x58]
00A57D60  41 83 FB 08                     cmp r11d, 8
00A57D64  0F 85 4F 3A 00 00               jne 0x140a5b7b9
00A57D6A  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A57D6F  48 8B 01                        mov rax, qword ptr [rcx]
00A57D72  48 89 84 24 80 01 00 00         mov qword ptr [rsp + 0x180], rax
00A57D7A  EB C5                           jmp 0x140a57d41
00A57D7C  E9 3D 3A 00 00                  jmp 0x140a5b7be
00A57D81  44 8B 5C 24 58                  mov r11d, dword ptr [rsp + 0x58]
00A57D86  41 83 FB 08                     cmp r11d, 8
00A57D8A  0F 85 29 3A 00 00               jne 0x140a5b7b9
00A57D90  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A57D95  4C 8B 01                        mov r8, qword ptr [rcx]
00A57D98  4C 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], r8
00A57DA0  8B 94 24 80 00 00 00            mov edx, dword ptr [rsp + 0x80]
00A57DA7  83 FB 7E                        cmp ebx, 0x7e
00A57DAA  0F 8F 15 1E 00 00               jg 0x140a59bc5
00A57DB0  0F 84 9F 1D 00 00               je 0x140a59b55
00A57DB6  B9 40 00 00 00                  mov ecx, 0x40
00A57DBB  3B D9                           cmp ebx, ecx
00A57DBD  0F 8F DE 0D 00 00               jg 0x140a58ba1
00A57DC3  0F 84 74 0D 00 00               je 0x140a58b3d
00A57DC9  83 FB 19                        cmp ebx, 0x19
00A57DCC  0F 8F 2E 05 00 00               jg 0x140a58300
00A57DD2  0F 84 9F 13 00 00               je 0x140a59177
00A57DD8  83 FB 0C                        cmp ebx, 0xc
00A57DDB  0F 8F C4 02 00 00               jg 0x140a580a5
00A57DE1  0F 84 6A 02 00 00               je 0x140a58051
00A57DE7  83 FB 06                        cmp ebx, 6
00A57DEA  0F 8F 5C 01 00 00               jg 0x140a57f4c
00A57DF0  0F 84 77 30 00 00               je 0x140a5ae6d
00A57DF6  8B D3                           mov edx, ebx
00A57DF8  85 DB                           test ebx, ebx
00A57DFA  0F 84 32 19 00 00               je 0x140a59732
00A57E00  83 EA 01                        sub edx, 1
00A57E03  0F 84 0A 01 00 00               je 0x140a57f13
00A57E09  83 EA 01                        sub edx, 1
00A57E0C  0F 84 B4 00 00 00               je 0x140a57ec6
00A57E12  83 EA 01                        sub edx, 1
00A57E15  74 11                           je 0x140a57e28
00A57E17  83 EA 01                        sub edx, 1
00A57E1A  0F 84 57 13 00 00               je 0x140a59177
00A57E20  83 FA 01                        cmp edx, 1
00A57E23  E9 E7 09 00 00                  jmp 0x140a5880f
00A57E28  41 BC 30 00 00 00               mov r12d, 0x30
00A57E2E  45 3B F4                        cmp r14d, r12d
00A57E31  76 16                           jbe 0x140a57e49
00A57E33  4D 85 FF                        test r15, r15
00A57E36  0F 84 19 39 00 00               je 0x140a5b755
00A57E3C  45 89 27                        mov dword ptr [r15], r12d
00A57E3F  E9 11 39 00 00                  jmp 0x140a5b755
00A57E44  E9 75 39 00 00                  jmp 0x140a5b7be
00A57E49  4C 8D 84 24 00 02 00 00         lea r8, [rsp + 0x200]
00A57E51  48 8D 94 24 E0 01 00 00         lea rdx, [rsp + 0x1e0]
00A57E59  48 8D 8C 24 E8 01 00 00         lea rcx, [rsp + 0x1e8]
00A57E61  E8 DE 75 A4 FF                  call 0x14049f444
00A57E66  E8 85 63 8A FF                  call 0x1402fe1f0
00A57E6B  48 8B 88 C8 04 00 00            mov rcx, qword ptr [rax + 0x4c8]
00A57E72  48 8B 81 B8 01 00 00            mov rax, qword ptr [rcx + 0x1b8]
00A57E79  48 89 84 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rax
00A57E81  8B 81 B0 01 00 00               mov eax, dword ptr [rcx + 0x1b0]
00A57E87  89 84 24 F8 01 00 00            mov dword ptr [rsp + 0x1f8], eax
00A57E8E  48 B8 B0 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003b0
00A57E98  48 8B 00                        mov rax, qword ptr [rax]
00A57E9B  48 89 84 24 08 02 00 00         mov qword ptr [rsp + 0x208], rax
00A57EA3  4D 8B C6                        mov r8, r14
00A57EA6  48 8D 94 24 E0 01 00 00         lea rdx, [rsp + 0x1e0]
00A57EAE  48 8B CF                        mov rcx, rdi
00A57EB1  E8 8A E9 C6 FF                  call 0x1406c6840
00A57EB6  90                              nop
00A57EB7  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
00A57EBC  E9 DE 38 00 00                  jmp 0x140a5b79f
00A57EC1  E9 F8 38 00 00                  jmp 0x140a5b7be
00A57EC6  41 81 FE 38 01 00 00            cmp r14d, 0x138
00A57ECD  73 1B                           jae 0x140a57eea
00A57ECF  4D 85 FF                        test r15, r15
00A57ED2  0F 84 7D 38 00 00               je 0x140a5b755
00A57ED8  BB 78 01 00 00                  mov ebx, 0x178
00A57EDD  41 89 1F                        mov dword ptr [r15], ebx
00A57EE0  E9 70 38 00 00                  jmp 0x140a5b755
00A57EE5  E9 D4 38 00 00                  jmp 0x140a5b7be
00A57EEA  BB 78 01 00 00                  mov ebx, 0x178
00A57EEF  44 3B F3                        cmp r14d, ebx
00A57EF2  41 0F 46 DE                     cmovbe ebx, r14d
00A57EF6  44 8B C3                        mov r8d, ebx
00A57EF9  48 8B D7                        mov rdx, rdi
00A57EFC  41 8B C9                        mov ecx, r9d
00A57EFF  E8 88 E5 F7 FF                  call 0x1409d648c
00A57F04  90                              nop
00A57F05  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
00A57F09  E9 91 38 00 00                  jmp 0x140a5b79f
00A57F0E  E9 AB 38 00 00                  jmp 0x140a5b7be
00A57F13  41 83 FE 0C                     cmp r14d, 0xc
00A57F17  73 1A                           jae 0x140a57f33
00A57F19  4D 85 FF                        test r15, r15
00A57F1C  0F 84 33 38 00 00               je 0x140a5b755
00A57F22  41 C7 07 0C 00 00 00            mov dword ptr [r15], 0xc
00A57F29  E9 27 38 00 00                  jmp 0x140a5b755
00A57F2E  E9 8B 38 00 00                  jmp 0x140a5b7be
00A57F33  48 8B CF                        mov rcx, rdi
00A57F36  E8 C1 DB 80 FF                  call 0x140265afc
00A57F3B  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A57F3F  C7 44 24 34 0C 00 00 00         mov dword ptr [rsp + 0x34], 0xc
00A57F47  E9 53 38 00 00                  jmp 0x140a5b79f
00A57F4C  8B CB                           mov ecx, ebx
00A57F4E  83 E9 07                        sub ecx, 7
00A57F51  0F 84 96 00 00 00               je 0x140a57fed
00A57F57  83 E9 01                        sub ecx, 1
00A57F5A  0F 84 0C 1E 00 00               je 0x140a59d6c
00A57F60  83 E9 01                        sub ecx, 1
00A57F63  74 4E                           je 0x140a57fb3
00A57F65  83 E9 01                        sub ecx, 1
00A57F68  0F 84 09 12 00 00               je 0x140a59177
00A57F6E  83 F9 01                        cmp ecx, 1
00A57F71  0F 85 6C 37 00 00               jne 0x140a5b6e3
00A57F77  48 8D 54 24 5C                  lea rdx, [rsp + 0x5c]
00A57F7C  8A 4C 24 38                     mov cl, byte ptr [rsp + 0x38]
00A57F80  E8 63 98 FC FF                  call 0x140a217e8
00A57F85  85 C0                           test eax, eax
00A57F87  0F 85 5C 18 00 00               jne 0x140a597e9
00A57F8D  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A57F92  45 8B C6                        mov r8d, r14d
00A57F95  48 8B D7                        mov rdx, rdi
00A57F98  8B 4C 24 5C                     mov ecx, dword ptr [rsp + 0x5c]
00A57F9C  E8 8F 3C 04 00                  call 0x140a9bc30
00A57FA1  33 D2                           xor edx, edx
00A57FA3  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A57FA7  8B C8                           mov ecx, eax
00A57FA9  E8 E2 B8 EA FF                  call 0x140903890
00A57FAE  E9 EC 37 00 00                  jmp 0x140a5b79f
00A57FB3  41 83 FE 04                     cmp r14d, 4
00A57FB7  74 1A                           je 0x140a57fd3
00A57FB9  4D 85 FF                        test r15, r15
00A57FBC  0F 84 93 37 00 00               je 0x140a5b755
00A57FC2  41 C7 07 04 00 00 00            mov dword ptr [r15], 4
00A57FC9  E9 87 37 00 00                  jmp 0x140a5b755
00A57FCE  E9 EB 37 00 00                  jmp 0x140a5b7be
00A57FD3  8B 05 E7 C2 56 00               mov eax, dword ptr [rip + 0x56c2e7]
00A57FD9  89 07                           mov dword ptr [rdi], eax
00A57FDB  C7 44 24 34 04 00 00 00         mov dword ptr [rsp + 0x34], 4
00A57FE3  E9 B7 37 00 00                  jmp 0x140a5b79f
00A57FE8  E9 D1 37 00 00                  jmp 0x140a5b7be
00A57FED  41 83 FE 18                     cmp r14d, 0x18
00A57FF1  74 1A                           je 0x140a5800d
00A57FF3  4D 85 FF                        test r15, r15
00A57FF6  0F 84 59 37 00 00               je 0x140a5b755
00A57FFC  41 C7 07 18 00 00 00            mov dword ptr [r15], 0x18
00A58003  E9 4D 37 00 00                  jmp 0x140a5b755
00A58008  E9 B1 37 00 00                  jmp 0x140a5b7be
00A5800D  8B 05 25 08 58 00               mov eax, dword ptr [rip + 0x580825]
00A58013  89 07                           mov dword ptr [rdi], eax
00A58015  48 8B 05 20 08 58 00            mov rax, qword ptr [rip + 0x580820]
00A5801C  89 47 04                        mov dword ptr [rdi + 4], eax
00A5801F  48 8B 05 1A 08 58 00            mov rax, qword ptr [rip + 0x58081a]
00A58026  89 47 08                        mov dword ptr [rdi + 8], eax
00A58029  48 8B 05 14 08 58 00            mov rax, qword ptr [rip + 0x580814]
00A58030  89 47 0C                        mov dword ptr [rdi + 0xc], eax
00A58033  48 8B 05 12 08 58 00            mov rax, qword ptr [rip + 0x580812]
00A5803A  89 47 10                        mov dword ptr [rdi + 0x10], eax
00A5803D  48 8B 05 0C 08 58 00            mov rax, qword ptr [rip + 0x58080c]
00A58044  89 47 14                        mov dword ptr [rdi + 0x14], eax
00A58047  E9 AA 2B 00 00                  jmp 0x140a5abf6
00A5804C  E9 6D 37 00 00                  jmp 0x140a5b7be
00A58051  41 83 FE 38                     cmp r14d, 0x38
00A58055  73 1A                           jae 0x140a58071
00A58057  4D 85 FF                        test r15, r15
00A5805A  0F 84 F5 36 00 00               je 0x140a5b755
00A58060  41 C7 07 38 00 00 00            mov dword ptr [r15], 0x38
00A58067  E9 E9 36 00 00                  jmp 0x140a5b755
00A5806C  E9 4D 37 00 00                  jmp 0x140a5b7be
00A58071  48 8D 54 24 5C                  lea rdx, [rsp + 0x5c]
00A58076  8A 4C 24 38                     mov cl, byte ptr [rsp + 0x38]
00A5807A  E8 69 97 FC FF                  call 0x140a217e8
00A5807F  85 C0                           test eax, eax
00A58081  0F 85 62 17 00 00               jne 0x140a597e9
00A58087  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A5808C  45 8B C6                        mov r8d, r14d
00A5808F  48 8B D7                        mov rdx, rdi
00A58092  8B 4C 24 5C                     mov ecx, dword ptr [rsp + 0x5c]
00A58096  E8 45 BA D6 FF                  call 0x1407c3ae0
00A5809B  BA 02 00 00 00                  mov edx, 2
00A580A0  E9 FE FE FF FF                  jmp 0x140a57fa3
00A580A5  83 FB 12                        cmp ebx, 0x12
00A580A8  0F 8F F4 00 00 00               jg 0x140a581a2
00A580AE  0F 84 E4 00 00 00               je 0x140a58198
00A580B4  83 EB 0D                        sub ebx, 0xd
00A580B7  0F 84 CE 00 00 00               je 0x140a5818b
00A580BD  83 EB 01                        sub ebx, 1
00A580C0  0F 84 C5 00 00 00               je 0x140a5818b
00A580C6  83 EB 01                        sub ebx, 1
00A580C9  0F 84 BC 00 00 00               je 0x140a5818b
00A580CF  83 EB 01                        sub ebx, 1
00A580D2  74 58                           je 0x140a5812c
00A580D4  83 FB 01                        cmp ebx, 1
00A580D7  0F 85 06 36 00 00               jne 0x140a5b6e3
00A580DD  44 3B F1                        cmp r14d, ecx
00A580E0  73 16                           jae 0x140a580f8
00A580E2  4D 85 FF                        test r15, r15
00A580E5  0F 84 6A 36 00 00               je 0x140a5b755
00A580EB  41 89 0F                        mov dword ptr [r15], ecx
00A580EE  E9 62 36 00 00                  jmp 0x140a5b755
00A580F3  E9 C6 36 00 00                  jmp 0x140a5b7be
00A580F8  48 8D 54 24 5C                  lea rdx, [rsp + 0x5c]
00A580FD  8A 4C 24 38                     mov cl, byte ptr [rsp + 0x38]
00A58101  E8 E2 96 FC FF                  call 0x140a217e8
00A58106  85 C0                           test eax, eax
00A58108  0F 85 DB 16 00 00               jne 0x140a597e9
00A5810E  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A58113  45 8B C6                        mov r8d, r14d
00A58116  48 8B D7                        mov rdx, rdi
00A58119  8B 4C 24 5C                     mov ecx, dword ptr [rsp + 0x5c]
00A5811D  E8 52 BA D6 FF                  call 0x1407c3b74
00A58122  BA 06 00 00 00                  mov edx, 6
00A58127  E9 77 FE FF FF                  jmp 0x140a57fa3
00A5812C  41 BC 20 00 00 00               mov r12d, 0x20
00A58132  45 3B F4                        cmp r14d, r12d
00A58135  73 16                           jae 0x140a5814d
00A58137  4D 85 FF                        test r15, r15
00A5813A  0F 84 15 36 00 00               je 0x140a5b755
00A58140  45 89 27                        mov dword ptr [r15], r12d
00A58143  E9 0D 36 00 00                  jmp 0x140a5b755
00A58148  E9 71 36 00 00                  jmp 0x140a5b7be
00A5814D  40 F6 C7 07                     test dil, 7
00A58151  0F 85 0C 0A 00 00               jne 0x140a58b63
00A58157  48 8D 54 24 5C                  lea rdx, [rsp + 0x5c]
00A5815C  8A 4C 24 38                     mov cl, byte ptr [rsp + 0x38]
00A58160  E8 83 96 FC FF                  call 0x140a217e8
00A58165  85 C0                           test eax, eax
00A58167  0F 85 7C 16 00 00               jne 0x140a597e9
00A5816D  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A58172  45 8B C6                        mov r8d, r14d
00A58175  48 8B D7                        mov rdx, rdi
00A58178  8B 4C 24 5C                     mov ecx, dword ptr [rsp + 0x5c]
00A5817C  E8 BF 79 03 00                  call 0x140a8fb40
00A58181  BA 04 00 00 00                  mov edx, 4
00A58186  E9 18 FE FF FF                  jmp 0x140a57fa3
00A5818B  C7 44 24 30 02 00 00 C0         mov dword ptr [rsp + 0x30], 0xc0000002
00A58193  E9 07 36 00 00                  jmp 0x140a5b79f
00A58198  B8 90 00 00 00                  mov eax, 0x90
00A5819D  E9 09 1E 00 00                  jmp 0x140a59fab
00A581A2  8B D3                           mov edx, ebx
00A581A4  83 EA 13                        sub edx, 0x13
00A581A7  74 E2                           je 0x140a5818b
00A581A9  41 2B D4                        sub edx, r12d
00A581AC  0F 84 A2 16 00 00               je 0x140a59854
00A581B2  83 EA 01                        sub edx, 1
00A581B5  0F 84 0F 01 00 00               je 0x140a582ca
00A581BB  83 EA 01                        sub edx, 1
00A581BE  74 5F                           je 0x140a5821f
00A581C0  83 FA 01                        cmp edx, 1
00A581C3  0F 85 1A 35 00 00               jne 0x140a5b6e3
00A581C9  41 83 FE 14                     cmp r14d, 0x14
00A581CD  74 1A                           je 0x140a581e9
00A581CF  4D 85 FF                        test r15, r15
00A581D2  0F 84 7D 35 00 00               je 0x140a5b755
00A581D8  41 C7 07 14 00 00 00            mov dword ptr [r15], 0x14
00A581DF  E9 71 35 00 00                  jmp 0x140a5b755
00A581E4  E9 D5 35 00 00                  jmp 0x140a5b7be
00A581E9  8B 05 D1 CE 56 00               mov eax, dword ptr [rip + 0x56ced1]
00A581EF  89 47 04                        mov dword ptr [rdi + 4], eax
00A581F2  8B 05 F0 CE 56 00               mov eax, dword ptr [rip + 0x56cef0]
00A581F8  89 47 08                        mov dword ptr [rdi + 8], eax
00A581FB  8B 05 C3 CE 56 00               mov eax, dword ptr [rip + 0x56cec3]
00A58201  89 47 0C                        mov dword ptr [rdi + 0xc], eax
00A58204  8B 05 96 CF 56 00               mov eax, dword ptr [rip + 0x56cf96]
00A5820A  89 47 10                        mov dword ptr [rdi + 0x10], eax
00A5820D  C7 44 24 34 14 00 00 00         mov dword ptr [rsp + 0x34], 0x14
00A58215  E9 85 35 00 00                  jmp 0x140a5b79f
00A5821A  E9 9F 35 00 00                  jmp 0x140a5b7be
00A5821F  43 8D 04 49                     lea eax, [r9 + r9*2]
00A58223  C1 E0 03                        shl eax, 3
00A58226  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00A5822A  44 3B F0                        cmp r14d, eax
00A5822D  73 16                           jae 0x140a58245
00A5822F  4D 85 FF                        test r15, r15
00A58232  0F 84 1D 35 00 00               je 0x140a5b755
00A58238  41 89 07                        mov dword ptr [r15], eax
00A5823B  E9 15 35 00 00                  jmp 0x140a5b755
00A58240  E9 79 35 00 00                  jmp 0x140a5b7be
00A58245  44 8B F6                        mov r14d, esi
00A58248  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
00A5824C  48 8D 1D ED 09 57 00            lea rbx, [rip + 0x5709ed]
00A58253  48 89 BC 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdi
00A5825B  45 3B F1                        cmp r14d, r9d
00A5825E  0F 83 3A 04 00 00               jae 0x140a5869e
00A58264  66 44 89 54 24 3C               mov word ptr [rsp + 0x3c], r10w
00A5826A  44 88 74 24 3E                  mov byte ptr [rsp + 0x3e], r14b
00A5826F  40 88 74 24 3F                  mov byte ptr [rsp + 0x3f], sil
00A58274  48 8D 4C 24 3C                  lea rcx, [rsp + 0x3c]
00A58279  E8 52 50 88 FF                  call 0x1402dd2d0
00A5827E  8B C8                           mov ecx, eax
00A58280  48 8B 14 CB                     mov rdx, qword ptr [rbx + rcx*8]
00A58284  8B 82 3C 2D 00 00               mov eax, dword ptr [rdx + 0x2d3c]
00A5828A  89 07                           mov dword ptr [rdi], eax
00A5828C  8B 82 5C 38 00 00               mov eax, dword ptr [rdx + 0x385c]
00A58292  89 47 04                        mov dword ptr [rdi + 4], eax
00A58295  8B 82 AC 38 00 00               mov eax, dword ptr [rdx + 0x38ac]
00A5829B  89 47 08                        mov dword ptr [rdi + 8], eax
00A5829E  8B 05 D8 E8 56 00               mov eax, dword ptr [rip + 0x56e8d8]
00A582A4  89 47 0C                        mov dword ptr [rdi + 0xc], eax
00A582A7  89 77 10                        mov dword ptr [rdi + 0x10], esi
00A582AA  89 77 14                        mov dword ptr [rdi + 0x14], esi
00A582AD  48 83 C7 18                     add rdi, 0x18
00A582B1  45 03 F5                        add r14d, r13d
00A582B4  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
00A582B9  44 8B 4C 24 64                  mov r9d, dword ptr [rsp + 0x64]
00A582BE  44 8B 54 24 68                  mov r10d, dword ptr [rsp + 0x68]
00A582C3  EB 8E                           jmp 0x140a58253
00A582C5  E9 F4 34 00 00                  jmp 0x140a5b7be
00A582CA  41 BC 30 00 00 00               mov r12d, 0x30
00A582D0  45 3B F4                        cmp r14d, r12d
00A582D3  73 16                           jae 0x140a582eb
00A582D5  4D 85 FF                        test r15, r15
00A582D8  0F 84 77 34 00 00               je 0x140a5b755
00A582DE  45 89 27                        mov dword ptr [r15], r12d
00A582E1  E9 6F 34 00 00                  jmp 0x140a5b755
00A582E6  E9 D3 34 00 00                  jmp 0x140a5b7be
00A582EB  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A582F0  41 8B D6                        mov edx, r14d
00A582F3  48 8B CF                        mov rcx, rdi
00A582F6  E8 DD ED FB FF                  call 0x140a170d8
00A582FB  E9 73 34 00 00                  jmp 0x140a5b773
00A58300  83 FB 32                        cmp ebx, 0x32
00A58303  0F 8F DA 04 00 00               jg 0x140a587e3
00A58309  0F 84 9D 04 00 00               je 0x140a587ac
00A5830F  83 FB 24                        cmp ebx, 0x24
00A58312  0F 8F 35 02 00 00               jg 0x140a5854d
00A58318  0F 84 77 01 00 00               je 0x140a58495
00A5831E  83 EB 1C                        sub ebx, 0x1c
00A58321  0F 84 E0 00 00 00               je 0x140a58407
00A58327  83 EB 01                        sub ebx, 1
00A5832A  0F 84 47 0E 00 00               je 0x140a59177
00A58330  41 2B DC                        sub ebx, r12d
00A58333  0F 84 B4 00 00 00               je 0x140a583ed
00A58339  41 2B DC                        sub ebx, r12d
00A5833C  74 3F                           je 0x140a5837d
00A5833E  41 3B DC                        cmp ebx, r12d
00A58341  0F 85 9C 33 00 00               jne 0x140a5b6e3
00A58347  45 3B F4                        cmp r14d, r12d
00A5834A  73 16                           jae 0x140a58362
00A5834C  4D 85 FF                        test r15, r15
00A5834F  0F 84 00 34 00 00               je 0x140a5b755
00A58355  45 89 27                        mov dword ptr [r15], r12d
00A58358  E9 F8 33 00 00                  jmp 0x140a5b755
00A5835D  E9 5C 34 00 00                  jmp 0x140a5b7be
00A58362  8A 05 90 F2 4E 00               mov al, byte ptr [rip + 0x4ef290]
00A58368  88 07                           mov byte ptr [rdi], al
00A5836A  8A 05 6C F2 4E 00               mov al, byte ptr [rip + 0x4ef26c]
00A58370  88 47 01                        mov byte ptr [rdi + 1], al
00A58373  E9 BA 16 00 00                  jmp 0x140a59a32
00A58378  E9 41 34 00 00                  jmp 0x140a5b7be
00A5837D  41 83 FE 10                     cmp r14d, 0x10
00A58381  73 1A                           jae 0x140a5839d
00A58383  4D 85 FF                        test r15, r15
00A58386  0F 84 C9 33 00 00               je 0x140a5b755
00A5838C  41 C7 07 10 00 00 00            mov dword ptr [r15], 0x10
00A58393  E9 BD 33 00 00                  jmp 0x140a5b755
00A58398  E9 21 34 00 00                  jmp 0x140a5b7be
00A5839D  C7 44 24 34 10 00 00 00         mov dword ptr [rsp + 0x34], 0x10
00A583A5  8B D6                           mov edx, esi
00A583A7  44 8B C6                        mov r8d, esi
00A583AA  45 85 C9                        test r9d, r9d
00A583AD  74 28                           je 0x140a583d7
00A583AF  48 8D 0D 8A 08 57 00            lea rcx, [rip + 0x57088a]
00A583B6  45 8B D1                        mov r10d, r9d
00A583B9  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
00A583BE  48 8B 01                        mov rax, qword ptr [rcx]
00A583C1  03 90 B8 8B 00 00               add edx, dword ptr [rax + 0x8bb8]
00A583C7  44 03 80 70 86 00 00            add r8d, dword ptr [rax + 0x8670]
00A583CE  48 8D 49 08                     lea rcx, [rcx + 8]
00A583D2  4D 2B D5                        sub r10, r13
00A583D5  75 E7                           jne 0x140a583be
00A583D7  89 17                           mov dword ptr [rdi], edx
00A583D9  44 89 47 04                     mov dword ptr [rdi + 4], r8d
00A583DD  89 77 08                        mov dword ptr [rdi + 8], esi
00A583E0  89 77 0C                        mov dword ptr [rdi + 0xc], esi
00A583E3  E9 B7 33 00 00                  jmp 0x140a5b79f
00A583E8  E9 D1 33 00 00                  jmp 0x140a5b7be
00A583ED  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A583F2  44 8A 44 24 38                  mov r8b, byte ptr [rsp + 0x38]
00A583F7  41 8B D6                        mov edx, r14d
00A583FA  48 8B CF                        mov rcx, rdi
00A583FD  E8 A2 A4 09 00                  call 0x140af28a4
00A58402  E9 6C 33 00 00                  jmp 0x140a5b773
00A58407  41 83 FE 0C                     cmp r14d, 0xc
00A5840B  74 20                           je 0x140a5842d
00A5840D  41 83 FE 18                     cmp r14d, 0x18
00A58411  74 1A                           je 0x140a5842d
00A58413  4D 85 FF                        test r15, r15
00A58416  0F 84 39 33 00 00               je 0x140a5b755
00A5841C  41 C7 07 0C 00 00 00            mov dword ptr [r15], 0xc
00A58423  E9 2D 33 00 00                  jmp 0x140a5b755
00A58428  E9 91 33 00 00                  jmp 0x140a5b7be
00A5842D  E8 9E 7D FC FF                  call 0x140a201d0
00A58432  48 8B 1D 37 EC 56 00            mov rbx, qword ptr [rip + 0x56ec37]
00A58439  44 8A 25 D7 CB 56 00            mov r12b, byte ptr [rip + 0x56cbd7]
00A58440  E8 F7 7D FC FF                  call 0x140a2023c
00A58445  90                              nop
00A58446  41 83 FE 18                     cmp r14d, 0x18
00A5844A  75 17                           jne 0x140a58463
00A5844C  48 89 1F                        mov qword ptr [rdi], rbx
00A5844F  48 A1 00 03 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000300]
00A58459  48 89 47 08                     mov qword ptr [rdi + 8], rax
00A5845D  44 88 67 10                     mov byte ptr [rdi + 0x10], r12b
00A58461  EB 28                           jmp 0x140a5848b
00A58463  8B 05 37 E6 56 00               mov eax, dword ptr [rip + 0x56e637]
00A58469  48 B9 00 03 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000300
00A58473  48 0F AF 01                     imul rax, qword ptr [rcx]
00A58477  33 D2                           xor edx, edx
00A58479  48 F7 F3                        div rbx
00A5847C  89 07                           mov dword ptr [rdi], eax
00A5847E  8B 05 1C E6 56 00               mov eax, dword ptr [rip + 0x56e61c]
00A58484  89 47 04                        mov dword ptr [rdi + 4], eax
00A58487  44 88 67 08                     mov byte ptr [rdi + 8], r12b
00A5848B  E9 27 FA FF FF                  jmp 0x140a57eb7
00A58490  E9 29 33 00 00                  jmp 0x140a5b7be
00A58495  41 BC 30 00 00 00               mov r12d, 0x30
00A5849B  45 3B F4                        cmp r14d, r12d
00A5849E  73 16                           jae 0x140a584b6
00A584A0  4D 85 FF                        test r15, r15
00A584A3  0F 84 AC 32 00 00               je 0x140a5b755
00A584A9  45 89 27                        mov dword ptr [r15], r12d
00A584AC  E9 A4 32 00 00                  jmp 0x140a5b755
00A584B1  E9 08 33 00 00                  jmp 0x140a5b7be
00A584B6  8B D6                           mov edx, esi
00A584B8  45 85 C9                        test r9d, r9d
00A584BB  74 21                           je 0x140a584de
00A584BD  48 8D 0D 7C 07 57 00            lea rcx, [rip + 0x57077c]
00A584C4  45 8B C1                        mov r8d, r9d
00A584C7  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
00A584CC  48 8B 01                        mov rax, qword ptr [rcx]
00A584CF  03 90 3C 2D 00 00               add edx, dword ptr [rax + 0x2d3c]
00A584D5  48 8D 49 08                     lea rcx, [rcx + 8]
00A584D9  4D 2B C5                        sub r8, r13
00A584DC  75 EE                           jne 0x140a584cc
00A584DE  89 17                           mov dword ptr [rdi], edx
00A584E0  8B 05 DA AC 4C 00               mov eax, dword ptr [rip + 0x4cacda]
00A584E6  89 47 04                        mov dword ptr [rdi + 4], eax
00A584E9  8B 05 D9 AC 4C 00               mov eax, dword ptr [rip + 0x4cacd9]
00A584EF  89 47 08                        mov dword ptr [rdi + 8], eax
00A584F2  8B 05 CC AC 4C 00               mov eax, dword ptr [rip + 0x4caccc]
00A584F8  89 47 0C                        mov dword ptr [rdi + 0xc], eax
00A584FB  8B 05 CB AC 4C 00               mov eax, dword ptr [rip + 0x4caccb]
00A58501  89 47 10                        mov dword ptr [rdi + 0x10], eax
00A58504  8B 05 C6 AC 4C 00               mov eax, dword ptr [rip + 0x4cacc6]
00A5850A  89 47 14                        mov dword ptr [rdi + 0x14], eax
00A5850D  8B 05 C5 AC 4C 00               mov eax, dword ptr [rip + 0x4cacc5]
00A58513  89 47 18                        mov dword ptr [rdi + 0x18], eax
00A58516  8B 05 B8 AC 4C 00               mov eax, dword ptr [rip + 0x4cacb8]
00A5851C  89 47 1C                        mov dword ptr [rdi + 0x1c], eax
00A5851F  8B 05 B7 AC 4C 00               mov eax, dword ptr [rip + 0x4cacb7]
00A58525  89 47 20                        mov dword ptr [rdi + 0x20], eax
00A58528  8B 05 B2 AC 4C 00               mov eax, dword ptr [rip + 0x4cacb2]
00A5852E  89 47 24                        mov dword ptr [rdi + 0x24], eax
00A58531  8B 05 AD AC 4C 00               mov eax, dword ptr [rip + 0x4cacad]
00A58537  89 47 28                        mov dword ptr [rdi + 0x28], eax
00A5853A  8B 05 A8 AC 4C 00               mov eax, dword ptr [rip + 0x4caca8]
00A58540  89 47 2C                        mov dword ptr [rdi + 0x2c], eax
00A58543  E9 EA 14 00 00                  jmp 0x140a59a32
00A58548  E9 71 32 00 00                  jmp 0x140a5b7be
00A5854D  83 EB 25                        sub ebx, 0x25
00A58550  0F 84 1D 02 00 00               je 0x140a58773
00A58556  83 EB 05                        sub ebx, 5
00A58559  0F 84 84 01 00 00               je 0x140a586e3
00A5855F  83 EB 01                        sub ebx, 1
00A58562  0F 84 44 01 00 00               je 0x140a586ac
00A58568  83 EB 01                        sub ebx, 1
00A5856B  74 1E                           je 0x140a5858b
00A5856D  83 FB 01                        cmp ebx, 1
00A58570  0F 85 6D 31 00 00               jne 0x140a5b6e3
00A58576  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5857B  41 8B D6                        mov edx, r14d
00A5857E  48 8B CF                        mov rcx, rdi
00A58581  E8 E2 9E A8 FF                  call 0x1404e2468
00A58586  E9 E8 31 00 00                  jmp 0x140a5b773
00A5858B  41 BC AC 00 00 00               mov r12d, 0xac
00A58591  45 3B F4                        cmp r14d, r12d
00A58594  73 16                           jae 0x140a585ac
00A58596  4D 85 FF                        test r15, r15
00A58599  0F 84 B6 31 00 00               je 0x140a5b755
00A5859F  45 89 27                        mov dword ptr [r15], r12d
00A585A2  E9 AE 31 00 00                  jmp 0x140a5b755
00A585A7  E9 12 32 00 00                  jmp 0x140a5b7be
00A585AC  E8 3F 5C 8A FF                  call 0x1402fe1f0
00A585B1  48 8B 98 C8 04 00 00            mov rbx, qword ptr [rax + 0x4c8]
00A585B8  E8 13 7C FC FF                  call 0x140a201d0
00A585BD  48 8D 8C 24 E0 01 00 00         lea rcx, [rsp + 0x1e0]
00A585C5  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00A585C8  0F 11 01                        movups xmmword ptr [rcx], xmm0
00A585CB  0F 10 4B 10                     movups xmm1, xmmword ptr [rbx + 0x10]
00A585CF  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00A585D3  0F 10 43 20                     movups xmm0, xmmword ptr [rbx + 0x20]
00A585D7  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00A585DB  0F 10 4B 30                     movups xmm1, xmmword ptr [rbx + 0x30]
00A585DF  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
00A585E3  0F 10 43 40                     movups xmm0, xmmword ptr [rbx + 0x40]
00A585E7  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
00A585EB  0F 10 4B 50                     movups xmm1, xmmword ptr [rbx + 0x50]
00A585EF  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
00A585F3  0F 10 43 60                     movups xmm0, xmmword ptr [rbx + 0x60]
00A585F7  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
00A585FB  41 BE 80 00 00 00               mov r14d, 0x80
00A58601  49 03 CE                        add rcx, r14
00A58604  0F 10 43 70                     movups xmm0, xmmword ptr [rbx + 0x70]
00A58608  0F 11 41 F0                     movups xmmword ptr [rcx - 0x10], xmm0
00A5860C  49 03 DE                        add rbx, r14
00A5860F  0F 10 0B                        movups xmm1, xmmword ptr [rbx]
00A58612  0F 11 09                        movups xmmword ptr [rcx], xmm1
00A58615  0F 10 43 10                     movups xmm0, xmmword ptr [rbx + 0x10]
00A58619  0F 11 41 10                     movups xmmword ptr [rcx + 0x10], xmm0
00A5861D  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
00A58621  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
00A58625  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
00A58628  89 41 28                        mov dword ptr [rcx + 0x28], eax
00A5862B  E8 0C 7C FC FF                  call 0x140a2023c
00A58630  90                              nop
00A58631  48 8D 8C 24 E0 01 00 00         lea rcx, [rsp + 0x1e0]
00A58639  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00A5863C  0F 11 07                        movups xmmword ptr [rdi], xmm0
00A5863F  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
00A58643  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
00A58647  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
00A5864B  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
00A5864F  0F 10 49 30                     movups xmm1, xmmword ptr [rcx + 0x30]
00A58653  0F 11 4F 30                     movups xmmword ptr [rdi + 0x30], xmm1
00A58657  0F 10 41 40                     movups xmm0, xmmword ptr [rcx + 0x40]
00A5865B  0F 11 47 40                     movups xmmword ptr [rdi + 0x40], xmm0
00A5865F  0F 10 49 50                     movups xmm1, xmmword ptr [rcx + 0x50]
00A58663  0F 11 4F 50                     movups xmmword ptr [rdi + 0x50], xmm1
00A58667  0F 10 41 60                     movups xmm0, xmmword ptr [rcx + 0x60]
00A5866B  0F 11 47 60                     movups xmmword ptr [rdi + 0x60], xmm0
00A5866F  49 03 FE                        add rdi, r14
00A58672  0F 10 49 70                     movups xmm1, xmmword ptr [rcx + 0x70]
00A58676  0F 11 4F F0                     movups xmmword ptr [rdi - 0x10], xmm1
00A5867A  49 03 CE                        add rcx, r14
00A5867D  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00A58680  0F 11 07                        movups xmmword ptr [rdi], xmm0
00A58683  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
00A58687  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
00A5868B  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
00A5868F  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
00A58693  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
00A58696  89 47 28                        mov dword ptr [rdi + 0x28], eax
00A58699  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
00A5869E  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00A586A2  E9 F8 30 00 00                  jmp 0x140a5b79f
00A586A7  E9 12 31 00 00                  jmp 0x140a5b7be
00A586AC  41 83 FE 18                     cmp r14d, 0x18
00A586B0  73 1A                           jae 0x140a586cc
00A586B2  4D 85 FF                        test r15, r15
00A586B5  0F 84 9A 30 00 00               je 0x140a5b755
00A586BB  41 C7 07 18 00 00 00            mov dword ptr [r15], 0x18
00A586C2  E9 8E 30 00 00                  jmp 0x140a5b755
00A586C7  E9 F2 30 00 00                  jmp 0x140a5b7be
00A586CC  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
00A586D1  48 8D 54 24 34                  lea rdx, [rsp + 0x34]
00A586D6  48 8B CF                        mov rcx, rdi
00A586D9  E8 6A C2 D6 FF                  call 0x1407c4948
00A586DE  E9 90 30 00 00                  jmp 0x140a5b773
00A586E3  43 8D 04 49                     lea eax, [r9 + r9*2]
00A586E7  C1 E0 04                        shl eax, 4
00A586EA  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00A586EE  44 3B F0                        cmp r14d, eax
00A586F1  0F 82 C4 02 00 00               jb 0x140a589bb
00A586F7  8B DE                           mov ebx, esi
00A586F9  41 BC 30 00 00 00               mov r12d, 0x30
00A586FF  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00A58703  48 89 BC 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdi
00A5870B  41 3B D9                        cmp ebx, r9d
00A5870E  0F 83 8B 30 00 00               jae 0x140a5b79f
00A58714  66 44 89 54 24 3C               mov word ptr [rsp + 0x3c], r10w
00A5871A  88 5C 24 3E                     mov byte ptr [rsp + 0x3e], bl
00A5871E  40 88 74 24 3F                  mov byte ptr [rsp + 0x3f], sil
00A58723  45 33 C0                        xor r8d, r8d
00A58726  48 8D 94 24 E0 01 00 00         lea rdx, [rsp + 0x1e0]
00A5872E  48 8D 4C 24 3C                  lea rcx, [rsp + 0x3c]
00A58733  E8 38 6E 88 FF                  call 0x1402df570
00A58738  90                              nop
00A58739  0F 28 84 24 E0 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x1e0]
00A58741  0F 11 07                        movups xmmword ptr [rdi], xmm0
00A58744  0F 28 8C 24 F0 01 00 00         movaps xmm1, xmmword ptr [rsp + 0x1f0]
00A5874C  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
00A58750  0F 28 84 24 00 02 00 00         movaps xmm0, xmmword ptr [rsp + 0x200]
00A58758  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
00A5875C  49 03 FC                        add rdi, r12
00A5875F  41 03 DD                        add ebx, r13d
00A58762  44 8B 4C 24 64                  mov r9d, dword ptr [rsp + 0x64]
00A58767  44 8B 54 24 68                  mov r10d, dword ptr [rsp + 0x68]
00A5876C  EB 91                           jmp 0x140a586ff
00A5876E  E9 4B 30 00 00                  jmp 0x140a5b7be
00A58773  41 83 FE 10                     cmp r14d, 0x10
00A58777  73 1A                           jae 0x140a58793
00A58779  4D 85 FF                        test r15, r15
00A5877C  0F 84 D3 2F 00 00               je 0x140a5b755
00A58782  41 C7 07 10 00 00 00            mov dword ptr [r15], 0x10
00A58789  E9 C7 2F 00 00                  jmp 0x140a5b755
00A5878E  E9 2B 30 00 00                  jmp 0x140a5b7be
00A58793  48 8B CF                        mov rcx, rdi
00A58796  E8 1D 7B 04 00                  call 0x140aa02b8
00A5879B  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5879F  C7 44 24 34 10 00 00 00         mov dword ptr [rsp + 0x34], 0x10
00A587A7  E9 F3 2F 00 00                  jmp 0x140a5b79f
00A587AC  41 83 FE 08                     cmp r14d, 8
00A587B0  74 1A                           je 0x140a587cc
00A587B2  4D 85 FF                        test r15, r15
00A587B5  0F 84 9A 2F 00 00               je 0x140a5b755
00A587BB  41 C7 07 08 00 00 00            mov dword ptr [r15], 8
00A587C2  E9 8E 2F 00 00                  jmp 0x140a5b755
00A587C7  E9 F2 2F 00 00                  jmp 0x140a5b7be
00A587CC  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00A587D6  48 89 07                        mov qword ptr [rdi], rax
00A587D9  E9 C9 28 00 00                  jmp 0x140a5b0a7
00A587DE  E9 DB 2F 00 00                  jmp 0x140a5b7be
00A587E3  83 FB 3A                        cmp ebx, 0x3a
00A587E6  0F 8F 45 01 00 00               jg 0x140a58931
00A587EC  0F 84 0E 01 00 00               je 0x140a58900
00A587F2  8B CB                           mov ecx, ebx
00A587F4  83 E9 33                        sub ecx, 0x33
00A587F7  0F 84 C0 00 00 00               je 0x140a588bd
00A587FD  41 2B CC                        sub ecx, r12d
00A58800  74 4C                           je 0x140a5884e
00A58802  41 2B CC                        sub ecx, r12d
00A58805  74 32                           je 0x140a58839
00A58807  83 E9 01                        sub ecx, 1
00A5880A  74 0E                           je 0x140a5881a
00A5880C  83 F9 01                        cmp ecx, 1
00A5880F  0F 84 22 2F 00 00               je 0x140a5b737
00A58815  E9 C9 2E 00 00                  jmp 0x140a5b6e3
00A5881A  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A5881F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A58824  44 8A 4C 24 38                  mov r9b, byte ptr [rsp + 0x38]
00A58829  45 8B C6                        mov r8d, r14d
00A5882C  48 8B D7                        mov rdx, rdi
00A5882F  E8 58 93 FF FF                  call 0x140a51b8c
00A58834  E9 3A 2F 00 00                  jmp 0x140a5b773
00A58839  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5883E  41 8B D6                        mov edx, r14d
00A58841  48 8B CF                        mov rcx, rdi
00A58844  E8 3B 5F 00 00                  call 0x140a5e784
00A58849  E9 25 2F 00 00                  jmp 0x140a5b773
00A5884E  41 83 FE 10                     cmp r14d, 0x10
00A58852  73 1A                           jae 0x140a5886e
00A58854  4D 85 FF                        test r15, r15
00A58857  0F 84 F8 2E 00 00               je 0x140a5b755
00A5885D  41 C7 07 10 00 00 00            mov dword ptr [r15], 0x10
00A58864  E9 EC 2E 00 00                  jmp 0x140a5b755
00A58869  E9 50 2F 00 00                  jmp 0x140a5b7be
00A5886E  8B 07                           mov eax, dword ptr [rdi]
00A58870  89 84 24 3C 01 00 00            mov dword ptr [rsp + 0x13c], eax
00A58877  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
00A5887B  48 89 9C 24 C8 01 00 00         mov qword ptr [rsp + 0x1c8], rbx
00A58883  8B 7F 04                        mov edi, dword ptr [rdi + 4]
00A58886  89 BC 24 B0 01 00 00            mov dword ptr [rsp + 0x1b0], edi
00A5888D  8B D7                           mov edx, edi
00A5888F  41 B8 04 00 00 00               mov r8d, 4
00A58895  48 8B CB                        mov rcx, rbx
00A58898  E8 23 09 E9 FF                  call 0x1408e91c0
00A5889D  90                              nop
00A5889E  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
00A588A6  4C 8D 8C 24 3C 01 00 00         lea r9, [rsp + 0x13c]
00A588AE  8B D7                           mov edx, edi
00A588B0  48 8B CB                        mov rcx, rbx
00A588B3  E9 B1 2E 00 00                  jmp 0x140a5b769
00A588B8  E9 01 2F 00 00                  jmp 0x140a5b7be
00A588BD  80 7C 24 38 00                  cmp byte ptr [rsp + 0x38], 0
00A588C2  0F 84 A5 25 00 00               je 0x140a5ae6d
00A588C8  B8 90 00 00 00                  mov eax, 0x90
00A588CD  44 3B F0                        cmp r14d, eax
00A588D0  73 16                           jae 0x140a588e8
00A588D2  4D 85 FF                        test r15, r15
00A588D5  0F 84 7A 2E 00 00               je 0x140a5b755
00A588DB  41 89 07                        mov dword ptr [r15], eax
00A588DE  E9 72 2E 00 00                  jmp 0x140a5b755
00A588E3  E9 D6 2E 00 00                  jmp 0x140a5b7be
00A588E8  45 33 C9                        xor r9d, r9d
00A588EB  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A588F0  41 8B D6                        mov edx, r14d
00A588F3  48 8B CF                        mov rcx, rdi
00A588F6  E8 C9 DE BB FF                  call 0x1406167c4
00A588FB  E9 73 2E 00 00                  jmp 0x140a5b773
00A58900  41 83 FE 04                     cmp r14d, 4
00A58904  73 1A                           jae 0x140a58920
00A58906  4D 85 FF                        test r15, r15
00A58909  0F 84 46 2E 00 00               je 0x140a5b755
00A5890F  41 C7 07 04 00 00 00            mov dword ptr [r15], 4
00A58916  E9 3A 2E 00 00                  jmp 0x140a5b755
00A5891B  E9 9E 2E 00 00                  jmp 0x140a5b7be
00A58920  E8 1B B7 A3 FF                  call 0x140494040
00A58925  89 07                           mov dword ptr [rdi], eax
00A58927  E9 AF F6 FF FF                  jmp 0x140a57fdb
00A5892C  E9 8D 2E 00 00                  jmp 0x140a5b7be
00A58931  83 EB 3B                        sub ebx, 0x3b
00A58934  0F 84 AE 01 00 00               je 0x140a58ae8
00A5893A  83 EB 01                        sub ebx, 1
00A5893D  0F 84 90 01 00 00               je 0x140a58ad3
00A58943  83 EB 01                        sub ebx, 1
00A58946  74 63                           je 0x140a589ab
00A58948  83 EB 01                        sub ebx, 1
00A5894B  74 36                           je 0x140a58983
00A5894D  83 FB 01                        cmp ebx, 1
00A58950  0F 85 8D 2D 00 00               jne 0x140a5b6e3
00A58956  41 83 FE 0C                     cmp r14d, 0xc
00A5895A  73 1A                           jae 0x140a58976
00A5895C  4D 85 FF                        test r15, r15
00A5895F  0F 84 F0 2D 00 00               je 0x140a5b755
00A58965  41 C7 07 0C 00 00 00            mov dword ptr [r15], 0xc
00A5896C  E9 E4 2D 00 00                  jmp 0x140a5b755
00A58971  E9 48 2E 00 00                  jmp 0x140a5b7be
00A58976  48 8B CF                        mov rcx, rdi
00A58979  E8 BE D6 80 FF                  call 0x14026603c
00A5897E  E9 B8 F5 FF FF                  jmp 0x140a57f3b
00A58983  44 3B F1                        cmp r14d, ecx
00A58986  74 16                           je 0x140a5899e
00A58988  4D 85 FF                        test r15, r15
00A5898B  0F 84 C4 2D 00 00               je 0x140a5b755
00A58991  41 89 0F                        mov dword ptr [r15], ecx
00A58994  E9 BC 2D 00 00                  jmp 0x140a5b755
00A58999  E9 20 2E 00 00                  jmp 0x140a5b7be
00A5899E  48 8B CF                        mov rcx, rdi
00A589A1  E8 C6 BE A1 FF                  call 0x14047486c
00A589A6  E9 AA 0D 00 00                  jmp 0x140a59755
00A589AB  43 8D 04 89                     lea eax, [r9 + r9*4]
00A589AF  C1 E0 04                        shl eax, 4
00A589B2  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00A589B6  44 3B F0                        cmp r14d, eax
00A589B9  73 10                           jae 0x140a589cb
00A589BB  41 BD 04 00 00 C0               mov r13d, 0xc0000004
00A589C1  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
00A589C6  E9 D4 2D 00 00                  jmp 0x140a5b79f
00A589CB  48 89 BC 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdi
00A589D3  44 8B E6                        mov r12d, esi
00A589D6  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
00A589DA  48 8D 1D 5F 02 57 00            lea rbx, [rip + 0x57025f]
00A589E1  41 BE 50 00 00 00               mov r14d, 0x50
00A589E7  45 3B E1                        cmp r12d, r9d
00A589EA  0F 83 AF 2D 00 00               jae 0x140a5b79f
00A589F0  66 44 89 54 24 3C               mov word ptr [rsp + 0x3c], r10w
00A589F6  44 88 64 24 3E                  mov byte ptr [rsp + 0x3e], r12b
00A589FB  40 88 74 24 3F                  mov byte ptr [rsp + 0x3f], sil
00A58A00  48 8D 4C 24 3C                  lea rcx, [rsp + 0x3c]
00A58A05  E8 C6 48 88 FF                  call 0x1402dd2d0
00A58A0A  8B C8                           mov ecx, eax
00A58A0C  48 8B 04 CB                     mov rax, qword ptr [rbx + rcx*8]
00A58A10  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00A58A15  4C 8D 8C 24 78 01 00 00         lea r9, [rsp + 0x178]
00A58A1D  45 33 C0                        xor r8d, r8d
00A58A20  48 8D 94 24 E0 01 00 00         lea rdx, [rsp + 0x1e0]
00A58A28  48 8D 4C 24 3C                  lea rcx, [rsp + 0x3c]
00A58A2D  E8 52 4A 88 FF                  call 0x1402dd484
00A58A32  90                              nop
00A58A33  4D 8B C6                        mov r8, r14
00A58A36  33 D2                           xor edx, edx
00A58A38  48 8B CF                        mov rcx, rdi
00A58A3B  E8 00 E2 C6 FF                  call 0x1406c6c40
00A58A40  8B 05 5A E0 56 00               mov eax, dword ptr [rip + 0x56e05a]
00A58A46  8B D0                           mov edx, eax
00A58A48  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
00A58A4D  41 8B 88 48 86 00 00            mov ecx, dword ptr [r8 + 0x8648]
00A58A54  41 03 88 44 86 00 00            add ecx, dword ptr [r8 + 0x8644]
00A58A5B  48 0F AF C8                     imul rcx, rax
00A58A5F  48 89 4F 28                     mov qword ptr [rdi + 0x28], rcx
00A58A63  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
00A58A67  8B 88 8C 02 00 00               mov ecx, dword ptr [rax + 0x28c]
00A58A6D  48 0F AF CA                     imul rcx, rdx
00A58A71  48 89 4F 30                     mov qword ptr [rdi + 0x30], rcx
00A58A75  40 38 B4 24 FC 01 00 00         cmp byte ptr [rsp + 0x1fc], sil
00A58A7D  74 21                           je 0x140a58aa0
00A58A7F  8A 84 24 E8 01 00 00            mov al, byte ptr [rsp + 0x1e8]
00A58A86  88 07                           mov byte ptr [rdi], al
00A58A88  8A 84 24 EC 01 00 00            mov al, byte ptr [rsp + 0x1ec]
00A58A8F  88 47 07                        mov byte ptr [rdi + 7], al
00A58A92  8A 84 24 F0 01 00 00            mov al, byte ptr [rsp + 0x1f0]
00A58A99  88 47 08                        mov byte ptr [rdi + 8], al
00A58A9C  44 89 6F 0C                     mov dword ptr [rdi + 0xc], r13d
00A58AA0  48 8B 84 24 78 01 00 00         mov rax, qword ptr [rsp + 0x178]
00A58AA8  48 89 47 48                     mov qword ptr [rdi + 0x48], rax
00A58AAC  49 03 FE                        add rdi, r14
00A58AAF  48 89 BC 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdi
00A58AB7  45 03 E5                        add r12d, r13d
00A58ABA  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
00A58ABF  44 8B 4C 24 64                  mov r9d, dword ptr [rsp + 0x64]
00A58AC4  44 8B 54 24 68                  mov r10d, dword ptr [rsp + 0x68]
00A58AC9  E9 19 FF FF FF                  jmp 0x140a589e7
00A58ACE  E9 EB 2C 00 00                  jmp 0x140a5b7be
00A58AD3  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A58AD8  41 8B D6                        mov edx, r14d
00A58ADB  48 8B CF                        mov rcx, rdi
00A58ADE  E8 BD BF D6 FF                  call 0x1407c4aa0
00A58AE3  E9 8B 2C 00 00                  jmp 0x140a5b773
00A58AE8  41 83 FE 04                     cmp r14d, 4
00A58AEC  74 1A                           je 0x140a58b08
00A58AEE  4D 85 FF                        test r15, r15
00A58AF1  0F 84 5E 2C 00 00               je 0x140a5b755
00A58AF7  41 C7 07 04 00 00 00            mov dword ptr [r15], 4
00A58AFE  E9 52 2C 00 00                  jmp 0x140a5b755
00A58B03  E9 B6 2C 00 00                  jmp 0x140a5b7be
00A58B08  48 B8 E0 02 00 00 80 F7 FF FF   movabs rax, 0xfffff780000002e0
00A58B12  83 38 FF                        cmp dword ptr [rax], -1
00A58B15  75 11                           jne 0x140a58b28
00A58B17  E8 B8 ED 05 00                  call 0x140ab78d4
00A58B1C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A58B20  85 C0                           test eax, eax
00A58B22  0F 88 96 2C 00 00               js 0x140a5b7be
00A58B28  A1 E0 02 00 00 80 F7 FF FF      movabs eax, dword ptr [0xfffff780000002e0]
00A58B31  89 07                           mov dword ptr [rdi], eax
00A58B33  E9 A3 F4 FF FF                  jmp 0x140a57fdb
00A58B38  E9 81 2C 00 00                  jmp 0x140a5b7be
00A58B3D  41 83 FE 38                     cmp r14d, 0x38
00A58B41  73 1A                           jae 0x140a58b5d
00A58B43  4D 85 FF                        test r15, r15
00A58B46  0F 84 09 2C 00 00               je 0x140a5b755
00A58B4C  41 C7 07 38 00 00 00            mov dword ptr [r15], 0x38
00A58B53  E9 FD 2B 00 00                  jmp 0x140a5b755
00A58B58  E9 61 2C 00 00                  jmp 0x140a5b7be
00A58B5D  40 F6 C7 07                     test dil, 7
00A58B61  74 0A                           je 0x140a58b6d
00A58B63  B8 02 00 00 80                  mov eax, 0x80000002
00A58B68  E9 51 2C 00 00                  jmp 0x140a5b7be
00A58B6D  48 8D 54 24 5C                  lea rdx, [rsp + 0x5c]
00A58B72  8A 4C 24 38                     mov cl, byte ptr [rsp + 0x38]
00A58B76  E8 6D 8C FC FF                  call 0x140a217e8
00A58B7B  85 C0                           test eax, eax
00A58B7D  0F 85 66 0C 00 00               jne 0x140a597e9
00A58B83  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A58B88  45 8B C6                        mov r8d, r14d
00A58B8B  48 8B D7                        mov rdx, rdi
00A58B8E  8B 4C 24 5C                     mov ecx, dword ptr [rsp + 0x5c]
00A58B92  E8 21 0E 04 00                  call 0x140a999b8
00A58B97  BA 05 00 00 00                  mov edx, 5
00A58B9C  E9 02 F4 FF FF                  jmp 0x140a57fa3
00A58BA1  83 FB 63                        cmp ebx, 0x63
00A58BA4  0F 8F 3C 06 00 00               jg 0x140a591e6
00A58BAA  0F 84 2C 06 00 00               je 0x140a591dc
00A58BB0  B8 50 00 00 00                  mov eax, 0x50
00A58BB5  3B D8                           cmp ebx, eax
00A58BB7  0F 8F 76 02 00 00               jg 0x140a58e33
00A58BBD  0F 84 52 02 00 00               je 0x140a58e15
00A58BC3  83 FB 46                        cmp ebx, 0x46
00A58BC6  0F 8F 17 01 00 00               jg 0x140a58ce3
00A58BCC  0F 84 DF 00 00 00               je 0x140a58cb1
00A58BD2  83 EB 41                        sub ebx, 0x41
00A58BD5  0F 84 82 00 00 00               je 0x140a58c5d
00A58BDB  83 EB 01                        sub ebx, 1
00A58BDE  74 28                           je 0x140a58c08
00A58BE0  83 EB 01                        sub ebx, 1
00A58BE3  0F 84 FA 2A 00 00               je 0x140a5b6e3
00A58BE9  83 EB 01                        sub ebx, 1
00A58BEC  0F 84 F1 2A 00 00               je 0x140a5b6e3
00A58BF2  83 FB 01                        cmp ebx, 1
00A58BF5  0F 85 E8 2A 00 00               jne 0x140a5b6e3
00A58BFB  C7 44 24 30 BB 00 00 C0         mov dword ptr [rsp + 0x30], 0xc00000bb
00A58C03  E9 97 2B 00 00                  jmp 0x140a5b79f
00A58C08  41 BC 20 00 00 00               mov r12d, 0x20
00A58C0E  45 3B F4                        cmp r14d, r12d
00A58C11  73 16                           jae 0x140a58c29
00A58C13  4D 85 FF                        test r15, r15
00A58C16  0F 84 39 2B 00 00               je 0x140a5b755
00A58C1C  45 89 27                        mov dword ptr [r15], r12d
00A58C1F  E9 31 2B 00 00                  jmp 0x140a5b755
00A58C24  E9 95 2B 00 00                  jmp 0x140a5b7be
00A58C29  48 8D 54 24 5C                  lea rdx, [rsp + 0x5c]
00A58C2E  8A 4C 24 38                     mov cl, byte ptr [rsp + 0x38]
00A58C32  E8 B1 8B FC FF                  call 0x140a217e8
00A58C37  85 C0                           test eax, eax
00A58C39  0F 85 AA 0B 00 00               jne 0x140a597e9
00A58C3F  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A58C44  45 8B C6                        mov r8d, r14d
00A58C47  48 8B D7                        mov rdx, rdi
00A58C4A  8B 4C 24 5C                     mov ecx, dword ptr [rsp + 0x5c]
00A58C4E  E8 1D DD 9E FF                  call 0x140446970
00A58C53  BA 07 00 00 00                  mov edx, 7
00A58C58  E9 46 F3 FF FF                  jmp 0x140a57fa3
00A58C5D  41 83 FE 04                     cmp r14d, 4
00A58C61  73 1A                           jae 0x140a58c7d
00A58C63  4D 85 FF                        test r15, r15
00A58C66  0F 84 E9 2A 00 00               je 0x140a5b755
00A58C6C  41 C7 07 04 00 00 00            mov dword ptr [r15], 4
00A58C73  E9 DD 2A 00 00                  jmp 0x140a5b755
00A58C78  E9 41 2B 00 00                  jmp 0x140a5b7be
00A58C7D  8B D6                           mov edx, esi
00A58C7F  45 85 C9                        test r9d, r9d
00A58C82  74 21                           je 0x140a58ca5
00A58C84  48 8D 0D B5 FF 56 00            lea rcx, [rip + 0x56ffb5]
00A58C8B  45 8B C1                        mov r8d, r9d
00A58C8E  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
00A58C93  48 8B 01                        mov rax, qword ptr [rcx]
00A58C96  03 90 FC 87 00 00               add edx, dword ptr [rax + 0x87fc]
00A58C9C  48 8D 49 08                     lea rcx, [rcx + 8]
00A58CA0  4D 2B C5                        sub r8, r13
00A58CA3  75 EE                           jne 0x140a58c93
00A58CA5  89 17                           mov dword ptr [rdi], edx
00A58CA7  E9 2F F3 FF FF                  jmp 0x140a57fdb
00A58CAC  E9 0D 2B 00 00                  jmp 0x140a5b7be
00A58CB1  41 83 FE 04                     cmp r14d, 4
00A58CB5  74 1A                           je 0x140a58cd1
00A58CB7  4D 85 FF                        test r15, r15
00A58CBA  0F 84 95 2A 00 00               je 0x140a5b755
00A58CC0  41 C7 07 04 00 00 00            mov dword ptr [r15], 4
00A58CC7  E9 89 2A 00 00                  jmp 0x140a5b755
00A58CCC  E9 ED 2A 00 00                  jmp 0x140a5b7be
00A58CD1  8B 05 AD 26 3B 00               mov eax, dword ptr [rip + 0x3b26ad]
00A58CD7  89 07                           mov dword ptr [rdi], eax
00A58CD9  E9 FD F2 FF FF                  jmp 0x140a57fdb
00A58CDE  E9 DB 2A 00 00                  jmp 0x140a5b7be
00A58CE3  83 EB 48                        sub ebx, 0x48
00A58CE6  0F 84 CB 00 00 00               je 0x140a58db7
00A58CEC  83 EB 01                        sub ebx, 1
00A58CEF  0F 84 A0 00 00 00               je 0x140a58d95
00A58CF5  83 EB 03                        sub ebx, 3
00A58CF8  74 7D                           je 0x140a58d77
00A58CFA  83 EB 01                        sub ebx, 1
00A58CFD  74 28                           je 0x140a58d27
00A58CFF  41 3B DC                        cmp ebx, r12d
00A58D02  0F 85 DB 29 00 00               jne 0x140a5b6e3
00A58D08  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A58D0D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A58D12  44 8A 4C 24 38                  mov r9b, byte ptr [rsp + 0x38]
00A58D17  45 8B C6                        mov r8d, r14d
00A58D1A  48 8B D7                        mov rdx, rdi
00A58D1D  E8 EA 93 EA FF                  call 0x14090210c
00A58D22  E9 4C 2A 00 00                  jmp 0x140a5b773
00A58D27  48 8D 54 24 5C                  lea rdx, [rsp + 0x5c]
00A58D2C  8A 5C 24 38                     mov bl, byte ptr [rsp + 0x38]
00A58D30  8A CB                           mov cl, bl
00A58D32  E8 B1 8A FC FF                  call 0x140a217e8
00A58D37  85 C0                           test eax, eax
00A58D39  0F 85 AA 0A 00 00               jne 0x140a597e9
00A58D3F  8A D3                           mov dl, bl
00A58D41  48 8B 0D D8 0D 58 00            mov rcx, qword ptr [rip + 0x580dd8]
00A58D48  E8 D3 90 E1 FF                  call 0x140871e20
00A58D4D  44 8B CE                        mov r9d, esi
00A58D50  84 C0                           test al, al
00A58D52  41 0F 94 C1                     sete r9b
00A58D56  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A58D5B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A58D60  45 8B C6                        mov r8d, r14d
00A58D63  48 8B D7                        mov rdx, rdi
00A58D66  8B 4C 24 5C                     mov ecx, dword ptr [rsp + 0x5c]
00A58D6A  E8 9D BC D6 FF                  call 0x1407c4a0c
00A58D6F  41 8B D5                        mov edx, r13d
00A58D72  E9 2C F2 FF FF                  jmp 0x140a57fa3
00A58D77  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A58D7C  45 8B C6                        mov r8d, r14d
00A58D7F  8A 54 24 38                     mov dl, byte ptr [rsp + 0x38]
00A58D83  48 8B CF                        mov rcx, rdi
00A58D86  E8 A1 FC FD FF                  call 0x140a38a2c
00A58D8B  BA 0E 00 00 00                  mov edx, 0xe
00A58D90  E9 0E F2 FF FF                  jmp 0x140a57fa3
00A58D95  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A58D9A  45 8B C6                        mov r8d, r14d
00A58D9D  48 8B D7                        mov rdx, rdi
00A58DA0  41 0F B7 CA                     movzx ecx, r10w
00A58DA4  E8 BB 9D FC FF                  call 0x140a22b64
00A58DA9  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A58DAD  E9 ED 29 00 00                  jmp 0x140a5b79f
00A58DB2  E9 07 2A 00 00                  jmp 0x140a5b7be
00A58DB7  41 83 FE 08                     cmp r14d, 8
00A58DBB  0F 85 F8 29 00 00               jne 0x140a5b7b9
00A58DC1  83 EA 07                        sub edx, 7
00A58DC4  74 29                           je 0x140a58def
00A58DC6  83 FA 01                        cmp edx, 1
00A58DC9  74 0A                           je 0x140a58dd5
00A58DCB  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00A58DD0  E9 E9 29 00 00                  jmp 0x140a5b7be
00A58DD5  C7 07 08 00 00 00               mov dword ptr [rdi], 8
00A58DDB  48 8B 05 4E 7D 3A 00            mov rax, qword ptr [rip + 0x3a7d4e]
00A58DE2  E8 E9 1C C6 FF                  call 0x1406baad0
00A58DE7  0F B6 C0                        movzx eax, al
00A58DEA  89 47 04                        mov dword ptr [rdi + 4], eax
00A58DED  EB 1C                           jmp 0x140a58e0b
00A58DEF  C7 07 07 00 00 00               mov dword ptr [rdi], 7
00A58DF5  8B CE                           mov ecx, esi
00A58DF7  48 8D 15 02 38 AA FF            lea rdx, [rip - 0x55c7fe]
00A58DFE  48 39 15 33 7D 3A 00            cmp qword ptr [rip + 0x3a7d33], rdx
00A58E05  0F 95 C1                        setne cl
00A58E08  89 4F 04                        mov dword ptr [rdi + 4], ecx
00A58E0B  E9 97 22 00 00                  jmp 0x140a5b0a7
00A58E10  E9 A9 29 00 00                  jmp 0x140a5b7be
00A58E15  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A58E1A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A58E1F  45 8B C6                        mov r8d, r14d
00A58E22  48 8B D7                        mov rdx, rdi
00A58E25  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00A58E29  E8 AE 10 96 FF                  call 0x1403b9edc
00A58E2E  E9 40 29 00 00                  jmp 0x140a5b773
00A58E33  83 FB 5A                        cmp ebx, 0x5a
00A58E36  0F 8F 10 03 00 00               jg 0x140a5914c
00A58E3C  0F 84 AA 02 00 00               je 0x140a590ec
00A58E42  8B D3                           mov edx, ebx
00A58E44  83 EA 51                        sub edx, 0x51
00A58E47  0F 84 07 0A 00 00               je 0x140a59854
00A58E4D  41 2B D4                        sub edx, r12d
00A58E50  0F 84 D3 01 00 00               je 0x140a59029
00A58E56  83 EA 03                        sub edx, 3
00A58E59  0F 84 B5 01 00 00               je 0x140a59014
00A58E5F  83 EA 01                        sub edx, 1
00A58E62  0F 84 7A 01 00 00               je 0x140a58fe2
00A58E68  83 FA 01                        cmp edx, 1
00A58E6B  0F 85 72 28 00 00               jne 0x140a5b6e3
00A58E71  0F 57 C0                        xorps xmm0, xmm0
00A58E74  33 C0                           xor eax, eax
00A58E76  0F 11 84 24 60 01 00 00         movups xmmword ptr [rsp + 0x160], xmm0
00A58E7E  48 89 84 24 70 01 00 00         mov qword ptr [rsp + 0x170], rax
00A58E86  C7 44 24 34 18 00 00 00         mov dword ptr [rsp + 0x34], 0x18
00A58E8E  41 83 FE 18                     cmp r14d, 0x18
00A58E92  0F 85 23 FB FF FF               jne 0x140a589bb
00A58E98  0F 10 07                        movups xmm0, xmmword ptr [rdi]
00A58E9B  0F 11 84 24 60 01 00 00         movups xmmword ptr [rsp + 0x160], xmm0
00A58EA3  F2 0F 10 4F 10                  movsd xmm1, qword ptr [rdi + 0x10]
00A58EA8  F2 0F 11 8C 24 70 01 00 00      movsd qword ptr [rsp + 0x170], xmm1
00A58EB1  66 39 B4 24 68 01 00 00         cmp word ptr [rsp + 0x168], si
00A58EB9  0F 85 FA 28 00 00               jne 0x140a5b7b9
00A58EBF  48 8B 84 24 68 01 00 00         mov rax, qword ptr [rsp + 0x168]
00A58EC7  48 C1 E8 10                     shr rax, 0x10
00A58ECB  41 84 C5                        test r13b, al
00A58ECE  0F 85 E5 28 00 00               jne 0x140a5b7b9
00A58ED4  80 7C 24 38 00                  cmp byte ptr [rsp + 0x38], 0
00A58ED9  74 43                           je 0x140a58f1e
00A58EDB  66 85 C0                        test ax, ax
00A58EDE  74 37                           je 0x140a58f17
00A58EE0  44 84 AC 24 70 01 00 00         test byte ptr [rsp + 0x170], r13b
00A58EE8  0F 85 F4 28 00 00               jne 0x140a5b7e2
00A58EEE  0F B7 94 24 6A 01 00 00         movzx edx, word ptr [rsp + 0x16a]
00A58EF6  48 8B 8C 24 70 01 00 00         mov rcx, qword ptr [rsp + 0x170]
00A58EFE  48 03 D1                        add rdx, rcx
00A58F01  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00A58F0B  48 3B D0                        cmp rdx, rax
00A58F0E  77 05                           ja 0x140a58f15
00A58F10  48 3B D1                        cmp rdx, rcx
00A58F13  73 02                           jae 0x140a58f17
00A58F15  8A 00                           mov al, byte ptr [rax]
00A58F17  EB 05                           jmp 0x140a58f1e
00A58F19  E9 A0 28 00 00                  jmp 0x140a5b7be
00A58F1E  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
00A58F27  0F B7 84 24 6A 01 00 00         movzx eax, word ptr [rsp + 0x16a]
00A58F2F  89 84 24 28 01 00 00            mov dword ptr [rsp + 0x128], eax
00A58F36  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A58F3A  66 01 83 E4 01 00 00            add word ptr [rbx + 0x1e4], ax
00A58F41  90                              nop
00A58F42  48 8D 94 24 20 01 00 00         lea rdx, [rsp + 0x120]
00A58F4A  48 8B 8C 24 60 01 00 00         mov rcx, qword ptr [rsp + 0x160]
00A58F52  E8 49 9B E4 FF                  call 0x1408a2aa0
00A58F57  44 8B F0                        mov r14d, eax
00A58F5A  85 C0                           test eax, eax
00A58F5C  79 10                           jns 0x140a58f6e
00A58F5E  48 8B CB                        mov rcx, rbx
00A58F61  E8 AA 60 80 FF                  call 0x14025f010
00A58F66  41 8B C6                        mov eax, r14d
00A58F69  E9 50 28 00 00                  jmp 0x140a5b7be
00A58F6E  48 8D 57 08                     lea rdx, [rdi + 8]
00A58F72  4C 8D 8C 24 28 01 00 00         lea r9, [rsp + 0x128]
00A58F7A  4C 8B 84 24 70 01 00 00         mov r8, qword ptr [rsp + 0x170]
00A58F82  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
00A58F8A  E8 41 86 FB FF                  call 0x140a115d0
00A58F8F  44 8B E0                        mov r12d, eax
00A58F92  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A58F96  BA 44 66 6C 74                  mov edx, 0x746c6644
00A58F9B  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
00A58FA3  E8 38 E9 89 FF                  call 0x1402f78e0
00A58FA8  48 8B CB                        mov rcx, rbx
00A58FAB  E8 60 60 80 FF                  call 0x14025f010
00A58FB0  41 BD 04 00 00 C0               mov r13d, 0xc0000004
00A58FB6  45 3B E5                        cmp r12d, r13d
00A58FB9  0F 85 E0 27 00 00               jne 0x140a5b79f
00A58FBF  8B 84 24 28 01 00 00            mov eax, dword ptr [rsp + 0x128]
00A58FC6  66 89 47 0A                     mov word ptr [rdi + 0xa], ax
00A58FCA  E9 D0 27 00 00                  jmp 0x140a5b79f
00A58FCF  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A58FD3  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A58FD8  E9 C2 27 00 00                  jmp 0x140a5b79f
00A58FDD  E9 DC 27 00 00                  jmp 0x140a5b7be
00A58FE2  C7 44 24 34 08 00 00 00         mov dword ptr [rsp + 0x34], 8
00A58FEA  41 83 FE 08                     cmp r14d, 8
00A58FEE  0F 85 C7 F9 FF FF               jne 0x140a589bb
00A58FF4  8B 05 2E DC 56 00               mov eax, dword ptr [rip + 0x56dc2e]
00A58FFA  89 07                           mov dword ptr [rdi], eax
00A58FFC  8B CE                           mov ecx, esi
00A58FFE  39 0D 20 C1 56 00               cmp dword ptr [rip + 0x56c120], ecx
00A59004  0F 95 C1                        setne cl
00A59007  89 4F 04                        mov dword ptr [rdi + 4], ecx
00A5900A  E9 90 27 00 00                  jmp 0x140a5b79f
00A5900F  E9 AA 27 00 00                  jmp 0x140a5b7be
00A59014  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A59019  41 8B D6                        mov edx, r14d
00A5901C  48 8B CF                        mov rcx, rdi
00A5901F  E8 B0 64 CF FF                  call 0x14074f4d4
00A59024  E9 4A 27 00 00                  jmp 0x140a5b773
00A59029  41 C1 E1 03                     shl r9d, 3
00A5902D  44 89 4C 24 34                  mov dword ptr [rsp + 0x34], r9d
00A59032  41 83 FE 08                     cmp r14d, 8
00A59036  0F 82 A3 00 00 00               jb 0x140a590df
00A5903C  45 3B F1                        cmp r14d, r9d
00A5903F  73 09                           jae 0x140a5904a
00A59041  45 8B E6                        mov r12d, r14d
00A59044  41 C1 EC 03                     shr r12d, 3
00A59048  EB 05                           jmp 0x140a5904f
00A5904A  44 8B 64 24 64                  mov r12d, dword ptr [rsp + 0x64]
00A5904F  45 3B F1                        cmp r14d, r9d
00A59052  45 1B F6                        sbb r14d, r14d
00A59055  41 81 E6 04 00 00 C0            and r14d, 0xc0000004
00A5905C  48 89 BC 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdi
00A59064  BB 01 00 00 00                  mov ebx, 1
00A59069  8A CB                           mov cl, bl
00A5906B  E8 8C 54 87 FF                  call 0x1402ce4fc
00A59070  8B C6                           mov eax, esi
00A59072  48 8D 3D C7 FB 56 00            lea rdi, [rip + 0x56fbc7]
00A59079  8B 4C 24 68                     mov ecx, dword ptr [rsp + 0x68]
00A5907D  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A59081  41 3B C4                        cmp eax, r12d
00A59084  73 4F                           jae 0x140a590d5
00A59086  66 89 4C 24 3C                  mov word ptr [rsp + 0x3c], cx
00A5908B  88 44 24 3E                     mov byte ptr [rsp + 0x3e], al
00A5908F  40 88 74 24 3F                  mov byte ptr [rsp + 0x3f], sil
00A59094  48 8D 4C 24 3C                  lea rcx, [rsp + 0x3c]
00A59099  E8 32 42 88 FF                  call 0x1402dd2d0
00A5909E  8B C8                           mov ecx, eax
00A590A0  48 8B 0C CF                     mov rcx, qword ptr [rdi + rcx*8]
00A590A4  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
00A590A8  48 8B 49 48                     mov rcx, qword ptr [rcx + 0x48]
00A590AC  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
00A590B4  48 89 08                        mov qword ptr [rax], rcx
00A590B7  48 83 C0 08                     add rax, 8
00A590BB  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
00A590C3  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00A590C7  03 C3                           add eax, ebx
00A590C9  0F B7 4C 24 54                  movzx ecx, word ptr [rsp + 0x54]
00A590CE  EB AD                           jmp 0x140a5907d
00A590D0  E9 E9 26 00 00                  jmp 0x140a5b7be
00A590D5  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00A590DA  E9 C0 26 00 00                  jmp 0x140a5b79f
00A590DF  C7 44 24 30 23 00 00 C0         mov dword ptr [rsp + 0x30], 0xc0000023
00A590E7  E9 B3 26 00 00                  jmp 0x140a5b79f
00A590EC  41 BC 20 00 00 00               mov r12d, 0x20
00A590F2  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
00A590F7  41 83 FE 14                     cmp r14d, 0x14
00A590FB  73 16                           jae 0x140a59113
00A590FD  4D 85 FF                        test r15, r15
00A59100  0F 84 4F 26 00 00               je 0x140a5b755
00A59106  45 89 27                        mov dword ptr [r15], r12d
00A59109  E9 47 26 00 00                  jmp 0x140a5b755
00A5910E  E9 42 26 00 00                  jmp 0x140a5b755
00A59113  0F 10 05 26 5F 4A 00            movups xmm0, xmmword ptr [rip + 0x4a5f26]
00A5911A  F3 0F 7F 07                     movdqu xmmword ptr [rdi], xmm0
00A5911E  8B 05 2C 5F 4A 00               mov eax, dword ptr [rip + 0x4a5f2c]
00A59124  89 47 10                        mov dword ptr [rdi + 0x10], eax
00A59127  44 3B 74 24 34                  cmp r14d, dword ptr [rsp + 0x34]
00A5912C  0F 82 DB F0 FF FF               jb 0x140a5820d
00A59132  48 8B 05 1F 5F 4A 00            mov rax, qword ptr [rip + 0x4a5f1f]
00A59139  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
00A5913D  E9 5D 26 00 00                  jmp 0x140a5b79f
00A59142  E9 77 26 00 00                  jmp 0x140a5b7be
00A59147  E9 72 26 00 00                  jmp 0x140a5b7be
00A5914C  83 EB 5B                        sub ebx, 0x5b
00A5914F  74 76                           je 0x140a591c7
00A59151  83 EB 01                        sub ebx, 1
00A59154  74 2B                           je 0x140a59181
00A59156  83 EB 03                        sub ebx, 3
00A59159  0F 84 0E 1D 00 00               je 0x140a5ae6d
00A5915F  83 EB 01                        sub ebx, 1
00A59162  74 13                           je 0x140a59177
00A59164  41 3B DC                        cmp ebx, r12d
00A59167  0F 85 76 25 00 00               jne 0x140a5b6e3
00A5916D  B9 62 00 00 00                  mov ecx, 0x62
00A59172  E9 B9 1C 00 00                  jmp 0x140a5ae30
00A59177  B8 02 00 00 C0                  mov eax, 0xc0000002
00A5917C  E9 3D 26 00 00                  jmp 0x140a5b7be
00A59181  80 7C 24 38 00                  cmp byte ptr [rsp + 0x38], 0
00A59186  0F 84 E1 1C 00 00               je 0x140a5ae6d
00A5918C  41 BD 28 00 00 00               mov r13d, 0x28
00A59192  45 3B F5                        cmp r14d, r13d
00A59195  74 16                           je 0x140a591ad
00A59197  4D 85 FF                        test r15, r15
00A5919A  0F 84 B5 25 00 00               je 0x140a5b755
00A591A0  45 89 2F                        mov dword ptr [r15], r13d
00A591A3  E9 AD 25 00 00                  jmp 0x140a5b755
00A591A8  E9 11 26 00 00                  jmp 0x140a5b7be
00A591AD  48 8B CF                        mov rcx, rdi
00A591B0  E8 C7 32 15 00                  call 0x140bac47c
00A591B5  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A591B9  C1 F8 1F                        sar eax, 0x1f
00A591BC  83 E0 D8                        and eax, 0xffffffd8
00A591BF  41 03 C5                        add eax, r13d
00A591C2  E9 ED 0C 00 00                  jmp 0x140a59eb4
00A591C7  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A591CC  41 8B D6                        mov edx, r14d
00A591CF  48 8B CF                        mov rcx, rdi
00A591D2  E8 21 EB CB FF                  call 0x140717cf8
00A591D7  E9 97 25 00 00                  jmp 0x140a5b773
00A591DC  B9 63 00 00 00                  mov ecx, 0x63
00A591E1  E9 4A 1C 00 00                  jmp 0x140a5ae30
00A591E6  83 FB 72                        cmp ebx, 0x72
00A591E9  0F 8F 77 05 00 00               jg 0x140a59766
00A591EF  0F 84 3D 05 00 00               je 0x140a59732
00A591F5  83 FB 6A                        cmp ebx, 0x6a
00A591F8  0F 8F 75 03 00 00               jg 0x140a59573
00A591FE  0F 84 62 03 00 00               je 0x140a59566
00A59204  83 EB 64                        sub ebx, 0x64
00A59207  0F 84 61 02 00 00               je 0x140a5946e
00A5920D  83 EB 01                        sub ebx, 1
00A59210  0F 84 43 02 00 00               je 0x140a59459
00A59216  83 EB 01                        sub ebx, 1
00A59219  0F 84 00 01 00 00               je 0x140a5931f
00A5921F  83 EB 01                        sub ebx, 1
00A59222  0F 84 E2 00 00 00               je 0x140a5930a
00A59228  41 3B DC                        cmp ebx, r12d
00A5922B  0F 85 B2 24 00 00               jne 0x140a5b6e3
00A59231  48 8B 05 00 74 3A 00            mov rax, qword ptr [rip + 0x3a7400]
00A59238  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
00A5923D  45 33 C0                        xor r8d, r8d
00A59240  33 D2                           xor edx, edx
00A59242  8D 4A 17                        lea ecx, [rdx + 0x17]
00A59245  E8 86 18 C6 FF                  call 0x1406baad0
00A5924A  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5924E  41 BD 04 00 00 C0               mov r13d, 0xc0000004
00A59254  41 3B C5                        cmp eax, r13d
00A59257  0F 85 9E F9 FF FF               jne 0x140a58bfb
00A5925D  44 3B 74 24 50                  cmp r14d, dword ptr [rsp + 0x50]
00A59262  0F 82 99 00 00 00               jb 0x140a59301
00A59268  48 85 FF                        test rdi, rdi
00A5926B  0F 84 90 00 00 00               je 0x140a59301
00A59271  8A 5C 24 38                     mov bl, byte ptr [rsp + 0x38]
00A59275  84 DB                           test bl, bl
00A59277  74 26                           je 0x140a5929f
00A59279  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
00A5927D  B9 01 01 00 00                  mov ecx, 0x101
00A59282  41 B8 49 6E 66 6F               mov r8d, 0x6f666e49
00A59288  E8 63 8E 12 00                  call 0x140b820f0
00A5928D  4C 8B F0                        mov r14, rax
00A59290  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A59295  48 85 C0                        test rax, rax
00A59298  75 0D                           jne 0x140a592a7
00A5929A  E9 5A 02 00 00                  jmp 0x140a594f9
00A5929F  4C 8B F7                        mov r14, rdi
00A592A2  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00A592A7  48 8B 05 8A 73 3A 00            mov rax, qword ptr [rip + 0x3a738a]
00A592AE  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A592B3  4D 8B C6                        mov r8, r14
00A592B6  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
00A592BA  B9 17 00 00 00                  mov ecx, 0x17
00A592BF  E8 0C 18 C6 FF                  call 0x1406baad0
00A592C4  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A592C8  84 DB                           test bl, bl
00A592CA  0F 84 CF 24 00 00               je 0x140a5b79f
00A592D0  85 C0                           test eax, eax
00A592D2  78 20                           js 0x140a592f4
00A592D4  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00A592D9  49 8B D6                        mov rdx, r14
00A592DC  48 8B CF                        mov rcx, rdi
00A592DF  E8 5C D5 C6 FF                  call 0x1406c6840
00A592E4  EB 0E                           jmp 0x140a592f4
00A592E6  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A592EA  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00A592EF  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A592F4  BA 49 6E 66 6F                  mov edx, 0x6f666e49
00A592F9  49 8B CE                        mov rcx, r14
00A592FC  E9 5B 02 00 00                  jmp 0x140a5955c
00A59301  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00A59305  E9 AA 0B 00 00                  jmp 0x140a59eb4
00A5930A  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5930F  41 8B D6                        mov edx, r14d
00A59312  48 8B CF                        mov rcx, rdi
00A59315  E8 BA C1 FE FF                  call 0x140a454d4
00A5931A  E9 54 24 00 00                  jmp 0x140a5b773
00A5931F  41 BD B0 01 00 00               mov r13d, 0x1b0
00A59325  45 3B F5                        cmp r14d, r13d
00A59328  73 16                           jae 0x140a59340
00A5932A  4D 85 FF                        test r15, r15
00A5932D  0F 84 22 24 00 00               je 0x140a5b755
00A59333  45 89 2F                        mov dword ptr [r15], r13d
00A59336  E9 1A 24 00 00                  jmp 0x140a5b755
00A5933B  E9 7E 24 00 00                  jmp 0x140a5b7be
00A59340  E8 AB 4E 8A FF                  call 0x1402fe1f0
00A59345  4C 8B A0 C8 04 00 00            mov r12, qword ptr [rax + 0x4c8]
00A5934C  E8 7F 6E FC FF                  call 0x140a201d0
00A59351  48 8D 84 24 E0 01 00 00         lea rax, [rsp + 0x1e0]
00A59359  41 BE 03 00 00 00               mov r14d, 3
00A5935F  41 8B CE                        mov ecx, r14d
00A59362  41 8D 5E 7D                     lea ebx, [r14 + 0x7d]
00A59366  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
00A5936B  0F 11 00                        movups xmmword ptr [rax], xmm0
00A5936E  41 0F 10 4C 24 10               movups xmm1, xmmword ptr [r12 + 0x10]
00A59374  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
00A59378  41 0F 10 44 24 20               movups xmm0, xmmword ptr [r12 + 0x20]
00A5937E  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00A59382  41 0F 10 4C 24 30               movups xmm1, xmmword ptr [r12 + 0x30]
00A59388  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
00A5938C  41 0F 10 44 24 40               movups xmm0, xmmword ptr [r12 + 0x40]
00A59392  0F 11 40 40                     movups xmmword ptr [rax + 0x40], xmm0
00A59396  41 0F 10 4C 24 50               movups xmm1, xmmword ptr [r12 + 0x50]
00A5939C  0F 11 48 50                     movups xmmword ptr [rax + 0x50], xmm1
00A593A0  41 0F 10 44 24 60               movups xmm0, xmmword ptr [r12 + 0x60]
00A593A6  0F 11 40 60                     movups xmmword ptr [rax + 0x60], xmm0
00A593AA  48 03 C3                        add rax, rbx
00A593AD  41 0F 10 4C 24 70               movups xmm1, xmmword ptr [r12 + 0x70]
00A593B3  0F 11 48 F0                     movups xmmword ptr [rax - 0x10], xmm1
00A593B7  4C 03 E3                        add r12, rbx
00A593BA  48 83 E9 01                     sub rcx, 1
00A593BE  75 A6                           jne 0x140a59366
00A593C0  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
00A593C5  0F 11 00                        movups xmmword ptr [rax], xmm0
00A593C8  41 0F 10 4C 24 10               movups xmm1, xmmword ptr [r12 + 0x10]
00A593CE  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
00A593D2  41 0F 10 44 24 20               movups xmm0, xmmword ptr [r12 + 0x20]
00A593D8  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00A593DC  E8 5B 6E FC FF                  call 0x140a2023c
00A593E1  90                              nop
00A593E2  48 8D 84 24 E0 01 00 00         lea rax, [rsp + 0x1e0]
00A593EA  0F 10 00                        movups xmm0, xmmword ptr [rax]
00A593ED  0F 11 07                        movups xmmword ptr [rdi], xmm0
00A593F0  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00A593F4  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
00A593F8  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
00A593FC  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
00A59400  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
00A59404  0F 11 4F 30                     movups xmmword ptr [rdi + 0x30], xmm1
00A59408  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
00A5940C  0F 11 47 40                     movups xmmword ptr [rdi + 0x40], xmm0
00A59410  0F 10 48 50                     movups xmm1, xmmword ptr [rax + 0x50]
00A59414  0F 11 4F 50                     movups xmmword ptr [rdi + 0x50], xmm1
00A59418  0F 10 40 60                     movups xmm0, xmmword ptr [rax + 0x60]
00A5941C  0F 11 47 60                     movups xmmword ptr [rdi + 0x60], xmm0
00A59420  48 03 FB                        add rdi, rbx
00A59423  0F 10 48 70                     movups xmm1, xmmword ptr [rax + 0x70]
00A59427  0F 11 4F F0                     movups xmmword ptr [rdi - 0x10], xmm1
00A5942B  48 03 C3                        add rax, rbx
00A5942E  49 83 EE 01                     sub r14, 1
00A59432  75 B6                           jne 0x140a593ea
00A59434  0F 10 00                        movups xmm0, xmmword ptr [rax]
00A59437  0F 11 07                        movups xmmword ptr [rdi], xmm0
00A5943A  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00A5943E  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
00A59442  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
00A59446  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
00A5944A  44 89 6C 24 34                  mov dword ptr [rsp + 0x34], r13d
00A5944F  E9 4A F2 FF FF                  jmp 0x140a5869e
00A59454  E9 65 23 00 00                  jmp 0x140a5b7be
00A59459  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5945E  41 8B D6                        mov edx, r14d
00A59461  48 8B CF                        mov rcx, rdi
00A59464  E8 B7 B7 D6 FF                  call 0x1407c4c20
00A59469  E9 05 23 00 00                  jmp 0x140a5b773
00A5946E  66 44 89 94 24 A8 01 00 00      mov word ptr [rsp + 0x1a8], r10w
00A59477  41 0F B7 CA                     movzx ecx, r10w
00A5947B  E8 E0 85 A1 FF                  call 0x140471a60
00A59480  48 89 84 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rax
00A59488  F3 48 0F B8 C0                  popcnt rax, rax
00A5948D  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00A59495  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00A5949A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A5949F  4C 8D 8C 24 A0 01 00 00         lea r9, [rsp + 0x1a0]
00A594A7  44 8B C0                        mov r8d, eax
00A594AA  33 D2                           xor edx, edx
00A594AC  33 C9                           xor ecx, ecx
00A594AE  E8 D5 07 A3 FF                  call 0x140489c88
00A594B3  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A594B7  41 BD 04 00 00 C0               mov r13d, 0xc0000004
00A594BD  41 3B C5                        cmp eax, r13d
00A594C0  0F 85 D9 22 00 00               jne 0x140a5b79f
00A594C6  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00A594CA  41 3B C6                        cmp eax, r14d
00A594CD  76 0A                           jbe 0x140a594d9
00A594CF  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
00A594D4  E9 DB 09 00 00                  jmp 0x140a59eb4
00A594D9  48 8B D0                        mov rdx, rax
00A594DC  B9 40 00 00 00                  mov ecx, 0x40
00A594E1  41 B8 50 50 4D 74               mov r8d, 0x744d5050
00A594E7  E8 04 8C 12 00                  call 0x140b820f0
00A594EC  48 8B D8                        mov rbx, rax
00A594EF  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A594F4  48 85 C0                        test rax, rax
00A594F7  75 0D                           jne 0x140a59506
00A594F9  C7 44 24 30 9A 00 00 C0         mov dword ptr [rsp + 0x30], 0xc000009a
00A59501  E9 99 22 00 00                  jmp 0x140a5b79f
00A59506  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A5950B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A59510  4C 8D 8C 24 A0 01 00 00         lea r9, [rsp + 0x1a0]
00A59518  44 8B 84 24 80 00 00 00         mov r8d, dword ptr [rsp + 0x80]
00A59520  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
00A59524  48 8B CB                        mov rcx, rbx
00A59527  E8 5C 07 A3 FF                  call 0x140489c88
00A5952C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A59530  85 C0                           test eax, eax
00A59532  78 20                           js 0x140a59554
00A59534  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00A59539  48 8B D3                        mov rdx, rbx
00A5953C  48 8B CF                        mov rcx, rdi
00A5953F  E8 FC D2 C6 FF                  call 0x1406c6840
00A59544  EB 0E                           jmp 0x140a59554
00A59546  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5954A  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00A5954F  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A59554  BA 50 50 4D 74                  mov edx, 0x744d5050
00A59559  48 8B CB                        mov rcx, rbx
00A5955C  E8 0F 93 12 00                  call 0x140b82870
00A59561  E9 39 22 00 00                  jmp 0x140a5b79f
00A59566  C7 44 24 30 03 00 00 C0         mov dword ptr [rsp + 0x30], 0xc0000003
00A5956E  E9 2C 22 00 00                  jmp 0x140a5b79f
00A59573  8B CB                           mov ecx, ebx
00A59575  83 E9 6B                        sub ecx, 0x6b
00A59578  0F 84 12 01 00 00               je 0x140a59690
00A5957E  83 E9 01                        sub ecx, 1
00A59581  74 61                           je 0x140a595e4
00A59583  83 E9 01                        sub ecx, 1
00A59586  74 3D                           je 0x140a595c5
00A59588  83 E9 03                        sub ecx, 3
00A5958B  74 23                           je 0x140a595b0
00A5958D  83 F9 01                        cmp ecx, 1
00A59590  0F 85 4D 21 00 00               jne 0x140a5b6e3
00A59596  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A5959B  44 8A 44 24 38                  mov r8b, byte ptr [rsp + 0x38]
00A595A0  41 8B D6                        mov edx, r14d
00A595A3  48 8B CF                        mov rcx, rdi
00A595A6  E8 15 92 B8 FF                  call 0x1405e27c0
00A595AB  E9 C3 21 00 00                  jmp 0x140a5b773
00A595B0  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A595B5  45 8B C6                        mov r8d, r14d
00A595B8  48 8B D7                        mov rdx, rdi
00A595BB  E8 64 25 DE FF                  call 0x14083bb24
00A595C0  E9 AE 21 00 00                  jmp 0x140a5b773
00A595C5  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A595CA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A595CF  44 8A 4C 24 38                  mov r9b, byte ptr [rsp + 0x38]
00A595D4  45 8B C6                        mov r8d, r14d
00A595D7  48 8B D7                        mov rdx, rdi
00A595DA  E8 DD 51 FB FF                  call 0x140a0e7bc
00A595DF  E9 8F 21 00 00                  jmp 0x140a5b773
00A595E4  42 8D 04 CD 00 00 00 00         lea eax, [r9*8]
00A595EC  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00A595F0  41 83 FE 08                     cmp r14d, 8
00A595F4  0F 82 E5 FA FF FF               jb 0x140a590df
00A595FA  44 3B F0                        cmp r14d, eax
00A595FD  73 0F                           jae 0x140a5960e
00A595FF  45 8B CE                        mov r9d, r14d
00A59602  41 C1 E9 03                     shr r9d, 3
00A59606  44 89 4C 24 64                  mov dword ptr [rsp + 0x64], r9d
00A5960B  44 3B F0                        cmp r14d, eax
00A5960E  45 1B F6                        sbb r14d, r14d
00A59611  41 81 E6 04 00 00 C0            and r14d, 0xc0000004
00A59618  48 89 BC 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdi
00A59620  8B C6                           mov eax, esi
00A59622  48 8D 3D 17 F6 56 00            lea rdi, [rip + 0x56f617]
00A59629  BB 01 00 00 00                  mov ebx, 1
00A5962E  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A59632  41 3B C1                        cmp eax, r9d
00A59635  0F 83 9A FA FF FF               jae 0x140a590d5
00A5963B  66 44 89 54 24 3C               mov word ptr [rsp + 0x3c], r10w
00A59641  88 44 24 3E                     mov byte ptr [rsp + 0x3e], al
00A59645  40 88 74 24 3F                  mov byte ptr [rsp + 0x3f], sil
00A5964A  48 8D 4C 24 3C                  lea rcx, [rsp + 0x3c]
00A5964F  E8 7C 3C 88 FF                  call 0x1402dd2d0
00A59654  8B C8                           mov ecx, eax
00A59656  48 8B 0C CF                     mov rcx, qword ptr [rdi + rcx*8]
00A5965A  48 8B 89 78 87 00 00            mov rcx, qword ptr [rcx + 0x8778]
00A59661  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
00A59669  48 89 08                        mov qword ptr [rax], rcx
00A5966C  48 83 C0 08                     add rax, 8
00A59670  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
00A59678  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00A5967C  03 C3                           add eax, ebx
00A5967E  44 0F B7 54 24 54               movzx r10d, word ptr [rsp + 0x54]
00A59684  44 8B 4C 24 64                  mov r9d, dword ptr [rsp + 0x64]
00A59689  EB A3                           jmp 0x140a5962e
00A5968B  E9 2E 21 00 00                  jmp 0x140a5b7be
00A59690  B9 E7 00 00 00                  mov ecx, 0xe7
00A59695  48 8D 84 24 E0 01 00 00         lea rax, [rsp + 0x1e0]
00A5969D  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A596A2  B8 50 00 00 00                  mov eax, 0x50
00A596A7  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00A596AB  44 3B F0                        cmp r14d, eax
00A596AE  73 07                           jae 0x140a596b7
00A596B0  41 8B C6                        mov eax, r14d
00A596B3  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00A596B7  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00A596BB  48 8D 44 24 3C                  lea rax, [rsp + 0x3c]
00A596C0  3B D9                           cmp ebx, ecx
00A596C2  48 0F 45 C6                     cmovne rax, rsi
00A596C6  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00A596CE  41 BD 04 00 00 C0               mov r13d, 0xc0000004
00A596D4  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00A596D9  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A596DE  4C 8B C3                        mov r8, rbx
00A596E1  8B 94 24 18 01 00 00            mov edx, dword ptr [rsp + 0x118]
00A596E8  48 8B C8                        mov rcx, rax
00A596EB  E8 70 53 87 FF                  call 0x1402cea60
00A596F0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A596F4  85 C0                           test eax, eax
00A596F6  0F 88 BF 1C 00 00               js 0x140a5b3bb
00A596FC  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00A59701  48 8B D3                        mov rdx, rbx
00A59704  48 8B CF                        mov rcx, rdi
00A59707  E8 34 D1 C6 FF                  call 0x1406c6840
00A5970C  90                              nop
00A5970D  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00A59711  48 85 DB                        test rbx, rbx
00A59714  0F 84 85 20 00 00               je 0x140a5b79f
00A5971A  48 8D 84 24 E0 01 00 00         lea rax, [rsp + 0x1e0]
00A59722  48 3B D8                        cmp rbx, rax
00A59725  0F 84 74 20 00 00               je 0x140a5b79f
00A5972B  33 D2                           xor edx, edx
00A5972D  E9 27 FE FF FF                  jmp 0x140a59559
00A59732  44 3B F1                        cmp r14d, ecx
00A59735  74 16                           je 0x140a5974d
00A59737  4D 85 FF                        test r15, r15
00A5973A  0F 84 15 20 00 00               je 0x140a5b755
00A59740  41 89 0F                        mov dword ptr [r15], ecx
00A59743  E9 0D 20 00 00                  jmp 0x140a5b755
00A59748  E9 71 20 00 00                  jmp 0x140a5b7be
00A5974D  48 8B CF                        mov rcx, rdi
00A59750  E8 8F DB 9F FF                  call 0x1404572e4
00A59755  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A59759  C7 44 24 34 40 00 00 00         mov dword ptr [rsp + 0x34], 0x40
00A59761  E9 39 20 00 00                  jmp 0x140a5b79f
00A59766  83 FB 78                        cmp ebx, 0x78
00A59769  0F 8F A1 01 00 00               jg 0x140a59910
00A5976F  0F 84 DF 00 00 00               je 0x140a59854
00A59775  8B D3                           mov edx, ebx
00A59777  83 EA 73                        sub edx, 0x73
00A5977A  0F 84 95 00 00 00               je 0x140a59815
00A59780  83 EA 01                        sub edx, 1
00A59783  74 7B                           je 0x140a59800
00A59785  83 EA 01                        sub edx, 1
00A59788  74 46                           je 0x140a597d0
00A5978A  83 EA 01                        sub edx, 1
00A5978D  74 0E                           je 0x140a5979d
00A5978F  83 FA 01                        cmp edx, 1
00A59792  0F 84 BC 00 00 00               je 0x140a59854
00A59798  E9 46 1F 00 00                  jmp 0x140a5b6e3
00A5979D  80 7C 24 38 00                  cmp byte ptr [rsp + 0x38], 0
00A597A2  0F 84 C5 16 00 00               je 0x140a5ae6d
00A597A8  B8 10 01 00 00                  mov eax, 0x110
00A597AD  44 3B F0                        cmp r14d, eax
00A597B0  73 16                           jae 0x140a597c8
00A597B2  4D 85 FF                        test r15, r15
00A597B5  0F 84 9A 1F 00 00               je 0x140a5b755
00A597BB  41 89 07                        mov dword ptr [r15], eax
00A597BE  E9 92 1F 00 00                  jmp 0x140a5b755
00A597C3  E9 F6 1F 00 00                  jmp 0x140a5b7be
00A597C8  45 8B CD                        mov r9d, r13d
00A597CB  E9 1B F1 FF FF                  jmp 0x140a588eb
00A597D0  B8 48 04 00 00                  mov eax, 0x448
00A597D5  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00A597D9  44 3B F0                        cmp r14d, eax
00A597DC  0F 85 D9 F1 FF FF               jne 0x140a589bb
00A597E2  80 7C 24 38 00                  cmp byte ptr [rsp + 0x38], 0
00A597E7  74 0A                           je 0x140a597f3
00A597E9  B8 22 00 00 C0                  mov eax, 0xc0000022
00A597EE  E9 CB 1F 00 00                  jmp 0x140a5b7be
00A597F3  48 8B CF                        mov rcx, rdi
00A597F6  E8 25 96 CA FF                  call 0x140702e20
00A597FB  E9 73 1F 00 00                  jmp 0x140a5b773
00A59800  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A59805  45 8B C6                        mov r8d, r14d
00A59808  48 8B D7                        mov rdx, rdi
00A5980B  E8 04 DD 03 00                  call 0x140a97514
00A59810  E9 5E 1F 00 00                  jmp 0x140a5b773
00A59815  45 85 DB                        test r11d, r11d
00A59818  0F 85 9D F1 FF FF               jne 0x140a589bb
00A5981E  C7 44 24 34 08 00 00 00         mov dword ptr [rsp + 0x34], 8
00A59826  41 83 FE 08                     cmp r14d, 8
00A5982A  0F 82 8B F1 FF FF               jb 0x140a589bb
00A59830  8B 05 A6 B9 56 00               mov eax, dword ptr [rip + 0x56b9a6]
00A59836  89 07                           mov dword ptr [rdi], eax
00A59838  8B 05 4A BB 56 00               mov eax, dword ptr [rip + 0x56bb4a]
00A5983E  89 47 04                        mov dword ptr [rdi + 4], eax
00A59841  E9 59 1F 00 00                  jmp 0x140a5b79f
00A59846  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5984A  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A5984F  E9 4B 1F 00 00                  jmp 0x140a5b79f
00A59854  44 3B F1                        cmp r14d, ecx
00A59857  73 16                           jae 0x140a5986f
00A59859  4D 85 FF                        test r15, r15
00A5985C  0F 84 F3 1E 00 00               je 0x140a5b755
00A59862  41 89 0F                        mov dword ptr [r15], ecx
00A59865  E9 EB 1E 00 00                  jmp 0x140a5b755
00A5986A  E9 4F 1F 00 00                  jmp 0x140a5b7be
00A5986F  83 FB 77                        cmp ebx, 0x77
00A59872  74 0F                           je 0x140a59883
00A59874  83 FB 78                        cmp ebx, 0x78
00A59877  B8 03 00 00 00                  mov eax, 3
00A5987C  44 0F 44 E8                     cmove r13d, eax
00A59880  45 8B E5                        mov r12d, r13d
00A59883  48 8D 94 24 E0 01 00 00         lea rdx, [rsp + 0x1e0]
00A5988B  41 8B CC                        mov ecx, r12d
00A5988E  E8 7D 6E 86 FF                  call 0x1402c0710
00A59893  90                              nop
00A59894  48 8B 84 24 E0 01 00 00         mov rax, qword ptr [rsp + 0x1e0]
00A5989C  48 89 07                        mov qword ptr [rdi], rax
00A5989F  48 8B 84 24 E8 01 00 00         mov rax, qword ptr [rsp + 0x1e8]
00A598A7  48 89 47 08                     mov qword ptr [rdi + 8], rax
00A598AB  8B 84 24 F0 01 00 00            mov eax, dword ptr [rsp + 0x1f0]
00A598B2  89 47 10                        mov dword ptr [rdi + 0x10], eax
00A598B5  C7 44 24 40 40 00 00 00         mov dword ptr [rsp + 0x40], 0x40
00A598BD  48 8B 84 24 F8 01 00 00         mov rax, qword ptr [rsp + 0x1f8]
00A598C5  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
00A598C9  48 8B 84 24 00 02 00 00         mov rax, qword ptr [rsp + 0x200]
00A598D1  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
00A598D5  48 8B 84 24 08 02 00 00         mov rax, qword ptr [rsp + 0x208]
00A598DD  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
00A598E1  48 8B 84 24 10 02 00 00         mov rax, qword ptr [rsp + 0x210]
00A598E9  48 89 47 30                     mov qword ptr [rdi + 0x30], rax
00A598ED  8B 84 24 18 02 00 00            mov eax, dword ptr [rsp + 0x218]
00A598F4  89 47 38                        mov dword ptr [rdi + 0x38], eax
00A598F7  8B 84 24 1C 02 00 00            mov eax, dword ptr [rsp + 0x21c]
00A598FE  89 47 3C                        mov dword ptr [rdi + 0x3c], eax
00A59901  E9 53 FE FF FF                  jmp 0x140a59759
00A59906  E9 B3 1E 00 00                  jmp 0x140a5b7be
00A5990B  E9 AE 1E 00 00                  jmp 0x140a5b7be
00A59910  83 EB 79                        sub ebx, 0x79
00A59913  0F 84 D2 01 00 00               je 0x140a59aeb
00A59919  83 EB 01                        sub ebx, 1
00A5991C  0F 84 1F 01 00 00               je 0x140a59a41
00A59922  83 EB 01                        sub ebx, 1
00A59925  74 65                           je 0x140a5998c
00A59927  83 FB 01                        cmp ebx, 1
00A5992A  0F 85 B3 1D 00 00               jne 0x140a5b6e3
00A59930  C7 44 24 34 0C 00 00 00         mov dword ptr [rsp + 0x34], 0xc
00A59938  41 83 FE 04                     cmp r14d, 4
00A5993C  0F 82 79 F0 FF FF               jb 0x140a589bb
00A59942  8B 07                           mov eax, dword ptr [rdi]
00A59944  89 84 24 B8 01 00 00            mov dword ptr [rsp + 0x1b8], eax
00A5994B  83 F8 01                        cmp eax, 1
00A5994E  0F 85 A7 F2 FF FF               jne 0x140a58bfb
00A59954  41 83 FE 0C                     cmp r14d, 0xc
00A59958  0F 82 5D F0 FF FF               jb 0x140a589bb
00A5995E  89 77 08                        mov dword ptr [rdi + 8], esi
00A59961  89 77 04                        mov dword ptr [rdi + 4], esi
00A59964  44 89 6F 08                     mov dword ptr [rdi + 8], r13d
00A59968  44 89 6F 04                     mov dword ptr [rdi + 4], r13d
00A5996C  A0 C6 03 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff780000003c6]
00A59975  84 C0                           test al, al
00A59977  74 04                           je 0x140a5997d
00A59979  83 67 04 FE                     and dword ptr [rdi + 4], 0xfffffffe
00A5997D  E9 1D 1E 00 00                  jmp 0x140a5b79f
00A59982  E9 37 1E 00 00                  jmp 0x140a5b7be
00A59987  E9 32 1E 00 00                  jmp 0x140a5b7be
00A5998C  41 BC 20 00 00 00               mov r12d, 0x20
00A59992  45 3B F4                        cmp r14d, r12d
00A59995  74 16                           je 0x140a599ad
00A59997  4D 85 FF                        test r15, r15
00A5999A  0F 84 B5 1D 00 00               je 0x140a5b755
00A599A0  45 89 27                        mov dword ptr [r15], r12d
00A599A3  E9 AD 1D 00 00                  jmp 0x140a5b755
00A599A8  E9 11 1E 00 00                  jmp 0x140a5b7be
00A599AD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A599B6  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00A599BD  E8 82 21 A2 FF                  call 0x14047bb44
00A599C2  0F B7 C8                        movzx ecx, ax
00A599C5  E8 F6 0A A1 FF                  call 0x14046a4c0
00A599CA  48 89 84 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rax
00A599D2  E8 61 1C A1 FF                  call 0x14046b638
00A599D7  48 89 84 24 E8 01 00 00         mov qword ptr [rsp + 0x1e8], rax
00A599DF  E8 70 1D A1 FF                  call 0x14046b754
00A599E4  48 89 84 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rax
00A599EC  E8 03 23 A1 FF                  call 0x14046bcf4
00A599F1  48 89 84 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rax
00A599F9  90                              nop
00A599FA  48 8B 84 24 F8 01 00 00         mov rax, qword ptr [rsp + 0x1f8]
00A59A02  48 3B 84 24 E8 01 00 00         cmp rax, qword ptr [rsp + 0x1e8]
00A59A0A  48 0F 42 84 24 E8 01 00 00      cmovb rax, qword ptr [rsp + 0x1e8]
00A59A13  48 89 84 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rax
00A59A1B  0F 28 84 24 E0 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x1e0]
00A59A23  0F 11 07                        movups xmmword ptr [rdi], xmm0
00A59A26  0F 28 8C 24 F0 01 00 00         movaps xmm1, xmmword ptr [rsp + 0x1f0]
00A59A2E  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
00A59A32  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
00A59A37  E9 63 1D 00 00                  jmp 0x140a5b79f
00A59A3C  E9 7D 1D 00 00                  jmp 0x140a5b7be
00A59A41  C7 44 24 34 08 00 00 00         mov dword ptr [rsp + 0x34], 8
00A59A49  41 83 FE 08                     cmp r14d, 8
00A59A4D  0F 85 68 EF FF FF               jne 0x140a589bb
00A59A53  48 85 FF                        test rdi, rdi
00A59A56  0F 84 5F EF FF FF               je 0x140a589bb
00A59A5C  41 8B D6                        mov edx, r14d
00A59A5F  B9 01 01 00 00                  mov ecx, 0x101
00A59A64  41 B8 49 6E 66 6F               mov r8d, 0x6f666e49
00A59A6A  E8 81 86 12 00                  call 0x140b820f0
00A59A6F  48 8B D8                        mov rbx, rax
00A59A72  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A59A77  48 85 C0                        test rax, rax
00A59A7A  0F 84 79 FA FF FF               je 0x140a594f9
00A59A80  48 8B 05 B1 6B 3A 00            mov rax, qword ptr [rip + 0x3a6bb1]
00A59A87  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A59A8C  4C 8B C3                        mov r8, rbx
00A59A8F  41 8B D6                        mov edx, r14d
00A59A92  41 8D 4E 12                     lea ecx, [r14 + 0x12]
00A59A96  E8 35 10 C6 FF                  call 0x1406baad0
00A59A9B  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A59A9F  85 C0                           test eax, eax
00A59AA1  78 3E                           js 0x140a59ae1
00A59AA3  8B 03                           mov eax, dword ptr [rbx]
00A59AA5  89 07                           mov dword ptr [rdi], eax
00A59AA7  8B 47 04                        mov eax, dword ptr [rdi + 4]
00A59AAA  8B C8                           mov ecx, eax
00A59AAC  33 4B 04                        xor ecx, dword ptr [rbx + 4]
00A59AAF  41 23 CD                        and ecx, r13d
00A59AB2  33 C8                           xor ecx, eax
00A59AB4  89 4F 04                        mov dword ptr [rdi + 4], ecx
00A59AB7  8B D1                           mov edx, ecx
00A59AB9  33 53 04                        xor edx, dword ptr [rbx + 4]
00A59ABC  83 E2 02                        and edx, 2
00A59ABF  33 D1                           xor edx, ecx
00A59AC1  89 57 04                        mov dword ptr [rdi + 4], edx
00A59AC4  8B C2                           mov eax, edx
00A59AC6  33 43 04                        xor eax, dword ptr [rbx + 4]
00A59AC9  83 E0 04                        and eax, 4
00A59ACC  33 C2                           xor eax, edx
00A59ACE  89 47 04                        mov dword ptr [rdi + 4], eax
00A59AD1  EB 0E                           jmp 0x140a59ae1
00A59AD3  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A59AD7  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00A59ADC  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A59AE1  BA 49 6E 66 6F                  mov edx, 0x6f666e49
00A59AE6  E9 6E FA FF FF                  jmp 0x140a59559
00A59AEB  0F B7 0D 0E B5 56 00            movzx ecx, word ptr [rip + 0x56b50e]
00A59AF2  C1 E1 02                        shl ecx, 2
00A59AF5  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
00A59AF9  44 3B F1                        cmp r14d, ecx
00A59AFC  0F 82 B9 EE FF FF               jb 0x140a589bb
00A59B02  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
00A59B06  8B CE                           mov ecx, esi
00A59B08  44 8B C6                        mov r8d, esi
00A59B0B  44 8B CE                        mov r9d, esi
00A59B0E  8B D6                           mov edx, esi
00A59B10  0F B7 05 E9 B4 56 00            movzx eax, word ptr [rip + 0x56b4e9]
00A59B17  44 8B D0                        mov r10d, eax
00A59B1A  3B C8                           cmp ecx, eax
00A59B1C  73 2D                           jae 0x140a59b4b
00A59B1E  0F B7 4C 24 78                  movzx ecx, word ptr [rsp + 0x78]
00A59B23  41 0F AF CA                     imul ecx, r10d
00A59B27  03 CA                           add ecx, edx
00A59B29  48 8B 05 78 B5 56 00            mov rax, qword ptr [rip + 0x56b578]
00A59B30  8B 14 88                        mov edx, dword ptr [rax + rcx*4]
00A59B33  41 8B C0                        mov eax, r8d
00A59B36  89 14 87                        mov dword ptr [rdi + rax*4], edx
00A59B39  41 8D 49 01                     lea ecx, [r9 + 1]
00A59B3D  8B D1                           mov edx, ecx
00A59B3F  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00A59B43  44 8B C1                        mov r8d, ecx
00A59B46  44 8B C9                        mov r9d, ecx
00A59B49  EB C5                           jmp 0x140a59b10
00A59B4B  E9 4F 1C 00 00                  jmp 0x140a5b79f
00A59B50  E9 69 1C 00 00                  jmp 0x140a5b7be
00A59B55  41 BC 20 00 00 00               mov r12d, 0x20
00A59B5B  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
00A59B60  45 3B F4                        cmp r14d, r12d
00A59B63  0F 85 52 EE FF FF               jne 0x140a589bb
00A59B69  48 8D 94 24 E0 01 00 00         lea rdx, [rsp + 0x1e0]
00A59B71  33 C9                           xor ecx, ecx
00A59B73  E8 EC 64 16 00                  call 0x140bc0064
00A59B78  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A59B7C  85 C0                           test eax, eax
00A59B7E  0F 88 1B 1C 00 00               js 0x140a5b79f
00A59B84  48 8B 84 24 E0 01 00 00         mov rax, qword ptr [rsp + 0x1e0]
00A59B8C  80 7C 24 38 00                  cmp byte ptr [rsp + 0x38], 0
00A59B91  48 0F 45 C6                     cmovne rax, rsi
00A59B95  48 89 84 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rax
00A59B9D  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00A59BA2  48 8D 94 24 E0 01 00 00         lea rdx, [rsp + 0x1e0]
00A59BAA  48 8B CF                        mov rcx, rdi
00A59BAD  E8 8E CC C6 FF                  call 0x1406c6840
00A59BB2  E9 E8 1B 00 00                  jmp 0x140a5b79f
00A59BB7  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A59BBB  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A59BC0  E9 DA 1B 00 00                  jmp 0x140a5b79f
00A59BC5  B8 BD 00 00 00                  mov eax, 0xbd
00A59BCA  3B D8                           cmp ebx, eax
00A59BCC  0F 8F 64 10 00 00               jg 0x140a5ac36
00A59BD2  0F 84 15 1B 00 00               je 0x140a5b6ed
00A59BD8  B8 9F 00 00 00                  mov eax, 0x9f
00A59BDD  3B D8                           cmp ebx, eax
00A59BDF  0F 8F 49 07 00 00               jg 0x140a5a32e
00A59BE5  0F 84 2E 07 00 00               je 0x140a5a319
00A59BEB  B8 90 00 00 00                  mov eax, 0x90
00A59BF0  3B D8                           cmp ebx, eax
00A59BF2  0F 8F 0C 04 00 00               jg 0x140a5a004
00A59BF8  0F 84 AD 03 00 00               je 0x140a59fab
00A59BFE  B8 89 00 00 00                  mov eax, 0x89
00A59C03  3B D8                           cmp ebx, eax
00A59C05  0F 8F 1C 01 00 00               jg 0x140a59d27
00A59C0B  0F 84 E3 00 00 00               je 0x140a59cf4
00A59C11  8B CB                           mov ecx, ebx
00A59C13  81 E9 80 00 00 00               sub ecx, 0x80
00A59C19  0F 84 E6 18 00 00               je 0x140a5b505
00A59C1F  83 E9 05                        sub ecx, 5
00A59C22  0F 84 9A 00 00 00               je 0x140a59cc2
00A59C28  83 E9 01                        sub ecx, 1
00A59C2B  74 74                           je 0x140a59ca1
00A59C2D  83 E9 01                        sub ecx, 1
00A59C30  74 0E                           je 0x140a59c40
00A59C32  83 F9 01                        cmp ecx, 1
00A59C35  0F 84 B9 00 00 00               je 0x140a59cf4
00A59C3B  E9 A3 1A 00 00                  jmp 0x140a5b6e3
00A59C40  C7 44 24 34 08 00 00 00         mov dword ptr [rsp + 0x34], 8
00A59C48  41 83 FE 08                     cmp r14d, 8
00A59C4C  0F 82 69 ED FF FF               jb 0x140a589bb
00A59C52  33 D2                           xor edx, edx
00A59C54  48 8D 8C 24 2C 01 00 00         lea rcx, [rsp + 0x12c]
00A59C5C  E8 4F AB B2 FF                  call 0x1405847b0
00A59C61  85 C0                           test eax, eax
00A59C63  0F 85 92 EF FF FF               jne 0x140a58bfb
00A59C69  48 8D 94 24 30 01 00 00         lea rdx, [rsp + 0x130]
00A59C71  33 C9                           xor ecx, ecx
00A59C73  E8 A8 AE B2 FF                  call 0x140584b20
00A59C78  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A59C7C  85 C0                           test eax, eax
00A59C7E  0F 85 77 EF FF FF               jne 0x140a58bfb
00A59C84  8B 84 24 2C 01 00 00            mov eax, dword ptr [rsp + 0x12c]
00A59C8B  89 07                           mov dword ptr [rdi], eax
00A59C8D  8B 84 24 30 01 00 00            mov eax, dword ptr [rsp + 0x130]
00A59C94  89 47 04                        mov dword ptr [rdi + 4], eax
00A59C97  E9 03 1B 00 00                  jmp 0x140a5b79f
00A59C9C  E9 1D 1B 00 00                  jmp 0x140a5b7be
00A59CA1  41 BC 20 00 00 00               mov r12d, 0x20
00A59CA7  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
00A59CAC  45 3B F4                        cmp r14d, r12d
00A59CAF  0F 85 06 ED FF FF               jne 0x140a589bb
00A59CB5  48 8B D7                        mov rdx, rdi
00A59CB8  E8 F3 DC FB FF                  call 0x140a179b0
00A59CBD  E9 B1 1A 00 00                  jmp 0x140a5b773
00A59CC2  8A 5C 24 38                     mov bl, byte ptr [rsp + 0x38]
00A59CC6  8A D3                           mov dl, bl
00A59CC8  48 8B 0D A9 FD 57 00            mov rcx, qword ptr [rip + 0x57fda9]
00A59CCF  E8 4C 81 E1 FF                  call 0x140871e20
00A59CD4  84 C0                           test al, al
00A59CD6  0F 84 34 15 00 00               je 0x140a5b210
00A59CDC  44 8A C3                        mov r8b, bl
00A59CDF  41 8B D6                        mov edx, r14d
00A59CE2  48 8B CF                        mov rcx, rdi
00A59CE5  E8 2E 9F D6 FF                  call 0x1407c3c18
00A59CEA  BA 0D 00 00 00                  mov edx, 0xd
00A59CEF  E9 AF E2 FF FF                  jmp 0x140a57fa3
00A59CF4  41 BC 30 00 00 00               mov r12d, 0x30
00A59CFA  45 3B F4                        cmp r14d, r12d
00A59CFD  74 16                           je 0x140a59d15
00A59CFF  4D 85 FF                        test r15, r15
00A59D02  0F 84 4D 1A 00 00               je 0x140a5b755
00A59D08  45 89 27                        mov dword ptr [r15], r12d
00A59D0B  E9 45 1A 00 00                  jmp 0x140a5b755
00A59D10  E9 A9 1A 00 00                  jmp 0x140a5b7be
00A59D15  45 8B C4                        mov r8d, r12d
00A59D18  48 8B D7                        mov rdx, rdi
00A59D1B  8B CB                           mov ecx, ebx
00A59D1D  E8 DE 05 F0 FF                  call 0x14095a300
00A59D22  E9 97 1A 00 00                  jmp 0x140a5b7be
00A59D27  8B CB                           mov ecx, ebx
00A59D29  81 E9 8A 00 00 00               sub ecx, 0x8a
00A59D2F  0F 84 5C 02 00 00               je 0x140a59f91
00A59D35  83 E9 01                        sub ecx, 1
00A59D38  0F 84 39 02 00 00               je 0x140a59f77
00A59D3E  83 E9 01                        sub ecx, 1
00A59D41  0F 84 90 01 00 00               je 0x140a59ed7
00A59D47  83 E9 01                        sub ecx, 1
00A59D4A  74 20                           je 0x140a59d6c
00A59D4C  41 3B CC                        cmp ecx, r12d
00A59D4F  0F 85 8E 19 00 00               jne 0x140a5b6e3
00A59D55  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A59D5A  45 8B C6                        mov r8d, r14d
00A59D5D  48 8B D7                        mov rdx, rdi
00A59D60  8B CB                           mov ecx, ebx
00A59D62  E8 15 38 01 00                  call 0x140a6d57c
00A59D67  E9 07 1A 00 00                  jmp 0x140a5b773
00A59D6C  41 BC 30 00 00 00               mov r12d, 0x30
00A59D72  83 FB 08                        cmp ebx, 8
00A59D75  41 8D 44 24 18                  lea eax, [r12 + 0x18]
00A59D7A  44 0F 45 E0                     cmovne r12d, eax
00A59D7E  45 85 F6                        test r14d, r14d
00A59D81  0F 84 36 01 00 00               je 0x140a59ebd
00A59D87  33 D2                           xor edx, edx
00A59D89  41 8B C6                        mov eax, r14d
00A59D8C  41 F7 F4                        div r12d
00A59D8F  85 D2                           test edx, edx
00A59D91  0F 85 26 01 00 00               jne 0x140a59ebd
00A59D97  89 B4 24 80 00 00 00            mov dword ptr [rsp + 0x80], esi
00A59D9E  8B C6                           mov eax, esi
00A59DA0  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A59DA4  48 89 BC 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdi
00A59DAC  41 3B C1                        cmp eax, r9d
00A59DAF  0F 83 F8 00 00 00               jae 0x140a59ead
00A59DB5  66 44 89 54 24 3C               mov word ptr [rsp + 0x3c], r10w
00A59DBB  88 44 24 3E                     mov byte ptr [rsp + 0x3e], al
00A59DBF  40 88 74 24 3F                  mov byte ptr [rsp + 0x3f], sil
00A59DC4  48 8D 4C 24 3C                  lea rcx, [rsp + 0x3c]
00A59DC9  E8 02 35 88 FF                  call 0x1402dd2d0
00A59DCE  8B C8                           mov ecx, eax
00A59DD0  48 8D 05 69 EE 56 00            lea rax, [rip + 0x56ee69]
00A59DD7  48 8B 14 C8                     mov rdx, qword ptr [rax + rcx*8]
00A59DDB  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
00A59DE0  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
00A59DE7  41 8D 0C 04                     lea ecx, [r12 + rax]
00A59DEB  44 3B F1                        cmp r14d, ecx
00A59DEE  0F 82 C0 00 00 00               jb 0x140a59eb4
00A59DF4  89 8C 24 80 00 00 00            mov dword ptr [rsp + 0x80], ecx
00A59DFB  4C 8D 84 24 E0 01 00 00         lea r8, [rsp + 0x1e0]
00A59E03  33 D2                           xor edx, edx
00A59E05  48 8D 4C 24 3C                  lea rcx, [rsp + 0x3c]
00A59E0A  E8 61 57 88 FF                  call 0x1402df570
00A59E0F  90                              nop
00A59E10  8B 0D 8A CC 56 00               mov ecx, dword ptr [rip + 0x56cc8a]
00A59E16  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
00A59E1B  8B 82 48 86 00 00               mov eax, dword ptr [rdx + 0x8648]
00A59E21  48 0F AF C1                     imul rax, rcx
00A59E25  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00A59E29  8B 84 24 E4 01 00 00            mov eax, dword ptr [rsp + 0x1e4]
00A59E30  48 0F AF C1                     imul rax, rcx
00A59E34  48 89 47 08                     mov qword ptr [rdi + 8], rax
00A59E38  8B 82 4C 86 00 00               mov eax, dword ptr [rdx + 0x864c]
00A59E3E  48 0F AF C1                     imul rax, rcx
00A59E42  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
00A59E46  8B 82 50 86 00 00               mov eax, dword ptr [rdx + 0x8650]
00A59E4C  48 0F AF C1                     imul rax, rcx
00A59E50  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
00A59E54  8B 84 24 E0 01 00 00            mov eax, dword ptr [rsp + 0x1e0]
00A59E5B  48 0F AF C1                     imul rax, rcx
00A59E5F  48 89 07                        mov qword ptr [rdi], rax
00A59E62  8B 82 40 86 00 00               mov eax, dword ptr [rdx + 0x8640]
00A59E68  89 47 28                        mov dword ptr [rdi + 0x28], eax
00A59E6B  81 FB 8D 00 00 00               cmp ebx, 0x8d
00A59E71  75 19                           jne 0x140a59e8c
00A59E73  8B 82 6C 86 00 00               mov eax, dword ptr [rdx + 0x866c]
00A59E79  48 0F AF C1                     imul rax, rcx
00A59E7D  48 89 47 30                     mov qword ptr [rdi + 0x30], rax
00A59E81  89 77 2C                        mov dword ptr [rdi + 0x2c], esi
00A59E84  48 89 77 38                     mov qword ptr [rdi + 0x38], rsi
00A59E88  48 89 77 40                     mov qword ptr [rdi + 0x40], rsi
00A59E8C  41 8B C4                        mov eax, r12d
00A59E8F  48 03 F8                        add rdi, rax
00A59E92  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00A59E96  41 03 C5                        add eax, r13d
00A59E99  44 8B 4C 24 64                  mov r9d, dword ptr [rsp + 0x64]
00A59E9E  44 8B 54 24 68                  mov r10d, dword ptr [rsp + 0x68]
00A59EA3  E9 F8 FE FF FF                  jmp 0x140a59da0
00A59EA8  E9 11 19 00 00                  jmp 0x140a5b7be
00A59EAD  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
00A59EB4  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00A59EB8  E9 E2 18 00 00                  jmp 0x140a5b79f
00A59EBD  4D 85 FF                        test r15, r15
00A59EC0  0F 84 8F 18 00 00               je 0x140a5b755
00A59EC6  45 0F AF E1                     imul r12d, r9d
00A59ECA  45 89 27                        mov dword ptr [r15], r12d
00A59ECD  E9 83 18 00 00                  jmp 0x140a5b755
00A59ED2  E9 E7 18 00 00                  jmp 0x140a5b7be
00A59ED7  4D 85 FF                        test r15, r15
00A59EDA  75 13                           jne 0x140a59eef
00A59EDC  41 83 FE 08                     cmp r14d, 8
00A59EE0  73 0D                           jae 0x140a59eef
00A59EE2  C7 44 24 30 0D 00 00 C0         mov dword ptr [rsp + 0x30], 0xc000000d
00A59EEA  E9 B0 18 00 00                  jmp 0x140a5b79f
00A59EEF  48 8D 54 24 34                  lea rdx, [rsp + 0x34]
00A59EF4  41 8B CC                        mov ecx, r12d
00A59EF7  E8 68 61 16 00                  call 0x140bc0064
00A59EFC  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A59F00  85 C0                           test eax, eax
00A59F02  0F 88 97 18 00 00               js 0x140a5b79f
00A59F08  39 74 24 34                     cmp dword ptr [rsp + 0x34], esi
00A59F0C  0F 84 E7 F5 FF FF               je 0x140a594f9
00A59F12  44 3B 74 24 34                  cmp r14d, dword ptr [rsp + 0x34]
00A59F17  0F 82 C2 F1 FF FF               jb 0x140a590df
00A59F1D  48 8D 94 24 40 01 00 00         lea rdx, [rsp + 0x140]
00A59F25  41 8B CD                        mov ecx, r13d
00A59F28  E8 37 61 16 00                  call 0x140bc0064
00A59F2D  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A59F31  85 C0                           test eax, eax
00A59F33  0F 88 66 18 00 00               js 0x140a5b79f
00A59F39  48 8B 9C 24 40 01 00 00         mov rbx, qword ptr [rsp + 0x140]
00A59F41  48 85 DB                        test rbx, rbx
00A59F44  0F 84 AF F5 FF FF               je 0x140a594f9
00A59F4A  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00A59F4F  48 8B D3                        mov rdx, rbx
00A59F52  48 8B CF                        mov rcx, rdi
00A59F55  E8 E6 C8 C6 FF                  call 0x1406c6840
00A59F5A  EB 11                           jmp 0x140a59f6d
00A59F5C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A59F60  48 8B 9C 24 40 01 00 00         mov rbx, qword ptr [rsp + 0x140]
00A59F68  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A59F6D  BA 42 47 49 4B                  mov edx, 0x4b494742
00A59F72  E9 E2 F5 FF FF                  jmp 0x140a59559
00A59F77  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A59F7C  41 8B D6                        mov edx, r14d
00A59F7F  48 8B CF                        mov rcx, rdi
00A59F82  E8 99 6F 01 00                  call 0x140a70f20
00A59F87  BA 0B 00 00 00                  mov edx, 0xb
00A59F8C  E9 12 E0 FF FF                  jmp 0x140a57fa3
00A59F91  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A59F96  41 8B D6                        mov edx, r14d
00A59F99  48 8B CF                        mov rcx, rdi
00A59F9C  E8 3F 87 02 00                  call 0x140a826e0
00A59FA1  BA 0A 00 00 00                  mov edx, 0xa
00A59FA6  E9 F8 DF FF FF                  jmp 0x140a57fa3
00A59FAB  41 BC 20 00 00 00               mov r12d, 0x20
00A59FB1  45 8D 6C 24 08                  lea r13d, [r12 + 8]
00A59FB6  83 FB 12                        cmp ebx, 0x12
00A59FB9  45 0F 45 E5                     cmovne r12d, r13d
00A59FBD  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
00A59FC2  45 3B F4                        cmp r14d, r12d
00A59FC5  73 16                           jae 0x140a59fdd
00A59FC7  4D 85 FF                        test r15, r15
00A59FCA  0F 84 85 17 00 00               je 0x140a5b755
00A59FD0  45 89 27                        mov dword ptr [r15], r12d
00A59FD3  E9 7D 17 00 00                  jmp 0x140a5b755
00A59FD8  E9 E1 17 00 00                  jmp 0x140a5b7be
00A59FDD  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
00A59FE1  44 8B CE                        mov r9d, esi
00A59FE4  3B D8                           cmp ebx, eax
00A59FE6  41 0F 94 C1                     sete r9b
00A59FEA  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A59FEF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A59FF4  45 8B C6                        mov r8d, r14d
00A59FF7  48 8B D7                        mov rdx, rdi
00A59FFA  E8 65 9F 01 00                  call 0x140a73f64
00A59FFF  E9 6F 17 00 00                  jmp 0x140a5b773
00A5A004  B8 97 00 00 00                  mov eax, 0x97
00A5A009  3B D8                           cmp ebx, eax
00A5A00B  0F 8F 13 01 00 00               jg 0x140a5a124
00A5A011  0F 84 CA 00 00 00               je 0x140a5a0e1
00A5A017  8B CB                           mov ecx, ebx
00A5A019  81 E9 91 00 00 00               sub ecx, 0x91
00A5A01F  0F 84 30 FD FF FF               je 0x140a59d55
00A5A025  41 2B CC                        sub ecx, r12d
00A5A028  0F 84 9E 00 00 00               je 0x140a5a0cc
00A5A02E  83 E9 01                        sub ecx, 1
00A5A031  0F 84 00 17 00 00               je 0x140a5b737
00A5A037  83 E9 01                        sub ecx, 1
00A5A03A  74 40                           je 0x140a5a07c
00A5A03C  83 F9 01                        cmp ecx, 1
00A5A03F  0F 85 9E 16 00 00               jne 0x140a5b6e3
00A5A045  48 85 FF                        test rdi, rdi
00A5A048  74 18                           je 0x140a5a062
00A5A04A  8A 54 24 38                     mov dl, byte ptr [rsp + 0x38]
00A5A04E  48 8B 0D 23 FA 57 00            mov rcx, qword ptr [rip + 0x57fa23]
00A5A055  E8 C6 7D E1 FF                  call 0x140871e20
00A5A05A  84 C0                           test al, al
00A5A05C  0F 84 AE 11 00 00               je 0x140a5b210
00A5A062  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5A067  41 8B D6                        mov edx, r14d
00A5A06A  48 8B CF                        mov rcx, rdi
00A5A06D  E8 1A AE BF FF                  call 0x140654e8c
00A5A072  BA 0F 00 00 00                  mov edx, 0xf
00A5A077  E9 27 DF FF FF                  jmp 0x140a57fa3
00A5A07C  B9 03 00 00 00                  mov ecx, 3
00A5A081  44 3B F1                        cmp r14d, ecx
00A5A084  73 16                           jae 0x140a5a09c
00A5A086  4D 85 FF                        test r15, r15
00A5A089  0F 84 C6 16 00 00               je 0x140a5b755
00A5A08F  41 89 0F                        mov dword ptr [r15], ecx
00A5A092  E9 BE 16 00 00                  jmp 0x140a5b755
00A5A097  E9 22 17 00 00                  jmp 0x140a5b7be
00A5A09C  80 3D 7A 09 3B 00 00            cmp byte ptr [rip + 0x3b097a], 0
00A5A0A3  0F 94 C0                        sete al
00A5A0A6  88 07                           mov byte ptr [rdi], al
00A5A0A8  8A 05 4A D5 4E 00               mov al, byte ptr [rip + 0x4ed54a]
00A5A0AE  88 47 01                        mov byte ptr [rdi + 1], al
00A5A0B1  80 3D 24 D5 4E 00 00            cmp byte ptr [rip + 0x4ed524], 0
00A5A0B8  0F 94 C0                        sete al
00A5A0BB  88 47 02                        mov byte ptr [rdi + 2], al
00A5A0BE  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
00A5A0C2  E9 D8 16 00 00                  jmp 0x140a5b79f
00A5A0C7  E9 F2 16 00 00                  jmp 0x140a5b7be
00A5A0CC  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5A0D1  41 8B D6                        mov edx, r14d
00A5A0D4  48 8B CF                        mov rcx, rdi
00A5A0D7  E8 28 AC D6 FF                  call 0x1407c4d04
00A5A0DC  E9 92 16 00 00                  jmp 0x140a5b773
00A5A0E1  C7 44 24 34 04 00 00 00         mov dword ptr [rsp + 0x34], 4
00A5A0E9  41 83 FE 04                     cmp r14d, 4
00A5A0ED  73 1A                           jae 0x140a5a109
00A5A0EF  4D 85 FF                        test r15, r15
00A5A0F2  0F 84 5D 16 00 00               je 0x140a5b755
00A5A0F8  41 C7 07 04 00 00 00            mov dword ptr [r15], 4
00A5A0FF  E9 51 16 00 00                  jmp 0x140a5b755
00A5A104  E9 4C 16 00 00                  jmp 0x140a5b755
00A5A109  8B 05 35 E4 40 00               mov eax, dword ptr [rip + 0x40e435]
00A5A10F  89 07                           mov dword ptr [rdi], eax
00A5A111  E9 89 16 00 00                  jmp 0x140a5b79f
00A5A116  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5A11A  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A5A11F  E9 7B 16 00 00                  jmp 0x140a5b79f
00A5A124  81 EB 99 00 00 00               sub ebx, 0x99
00A5A12A  0F 84 57 01 00 00               je 0x140a5a287
00A5A130  83 EB 01                        sub ebx, 1
00A5A133  0F 84 1C 01 00 00               je 0x140a5a255
00A5A139  41 2B DC                        sub ebx, r12d
00A5A13C  0F 84 B9 00 00 00               je 0x140a5a1fb
00A5A142  83 EB 01                        sub ebx, 1
00A5A145  74 3A                           je 0x140a5a181
00A5A147  83 FB 01                        cmp ebx, 1
00A5A14A  0F 85 93 15 00 00               jne 0x140a5b6e3
00A5A150  44 89 6C 24 34                  mov dword ptr [rsp + 0x34], r13d
00A5A155  45 3B F5                        cmp r14d, r13d
00A5A158  73 16                           jae 0x140a5a170
00A5A15A  4D 85 FF                        test r15, r15
00A5A15D  0F 84 58 E8 FF FF               je 0x140a589bb
00A5A163  45 89 2F                        mov dword ptr [r15], r13d
00A5A166  E9 50 E8 FF FF                  jmp 0x140a589bb
00A5A16B  E9 4E 16 00 00                  jmp 0x140a5b7be
00A5A170  E8 8B 5E 9F FF                  call 0x140450000
00A5A175  88 07                           mov byte ptr [rdi], al
00A5A177  E9 23 16 00 00                  jmp 0x140a5b79f
00A5A17C  E9 3D 16 00 00                  jmp 0x140a5b7be
00A5A181  0F B7 0D E2 4E 4A 00            movzx ecx, word ptr [rip + 0x4a4ee2]
00A5A188  83 C1 18                        add ecx, 0x18
00A5A18B  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
00A5A18F  44 3B F1                        cmp r14d, ecx
00A5A192  0F 82 23 E8 FF FF               jb 0x140a589bb
00A5A198  48 8D 4F 18                     lea rcx, [rdi + 0x18]
00A5A19C  0F 57 C0                        xorps xmm0, xmm0
00A5A19F  33 C0                           xor eax, eax
00A5A1A1  0F 11 07                        movups xmmword ptr [rdi], xmm0
00A5A1A4  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00A5A1A8  8B 05 B2 4E 4A 00               mov eax, dword ptr [rip + 0x4a4eb2]
00A5A1AE  89 07                           mov dword ptr [rdi], eax
00A5A1B0  0F B7 05 B1 4E 4A 00            movzx eax, word ptr [rip + 0x4a4eb1]
00A5A1B7  66 89 47 08                     mov word ptr [rdi + 8], ax
00A5A1BB  0F B7 05 A8 4E 4A 00            movzx eax, word ptr [rip + 0x4a4ea8]
00A5A1C2  66 89 47 0A                     mov word ptr [rdi + 0xa], ax
00A5A1C6  66 83 3D 9A 4E 4A 00 00         cmp word ptr [rip + 0x4a4e9a], 0
00A5A1CE  74 18                           je 0x140a5a1e8
00A5A1D0  48 89 4F 10                     mov qword ptr [rdi + 0x10], rcx
00A5A1D4  44 0F B7 05 8E 4E 4A 00         movzx r8d, word ptr [rip + 0x4a4e8e]
00A5A1DC  48 8B 15 8D 4E 4A 00            mov rdx, qword ptr [rip + 0x4a4e8d]
00A5A1E3  E8 58 C6 C6 FF                  call 0x1406c6840
00A5A1E8  E9 B2 15 00 00                  jmp 0x140a5b79f
00A5A1ED  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5A1F1  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A5A1F6  E9 A4 15 00 00                  jmp 0x140a5b79f
00A5A1FB  C7 44 24 34 80 00 00 00         mov dword ptr [rsp + 0x34], 0x80
00A5A203  41 81 FE 80 00 00 00            cmp r14d, 0x80
00A5A20A  0F 85 AB E7 FF FF               jne 0x140a589bb
00A5A210  48 8D 94 24 E0 01 00 00         lea rdx, [rsp + 0x1e0]
00A5A218  41 8D 4E 83                     lea ecx, [r14 - 0x7d]
00A5A21C  E8 43 5E 16 00                  call 0x140bc0064
00A5A221  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5A225  85 C0                           test eax, eax
00A5A227  0F 88 72 15 00 00               js 0x140a5b79f
00A5A22D  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00A5A232  48 8D 94 24 E0 01 00 00         lea rdx, [rsp + 0x1e0]
00A5A23A  48 8B CF                        mov rcx, rdi
00A5A23D  E8 FE C5 C6 FF                  call 0x1406c6840
00A5A242  E9 58 15 00 00                  jmp 0x140a5b79f
00A5A247  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5A24B  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A5A250  E9 4A 15 00 00                  jmp 0x140a5b79f
00A5A255  41 BC 20 00 00 00               mov r12d, 0x20
00A5A25B  45 3B F4                        cmp r14d, r12d
00A5A25E  73 16                           jae 0x140a5a276
00A5A260  4D 85 FF                        test r15, r15
00A5A263  0F 84 EC 14 00 00               je 0x140a5b755
00A5A269  45 89 27                        mov dword ptr [r15], r12d
00A5A26C  E9 E4 14 00 00                  jmp 0x140a5b755
00A5A271  E9 48 15 00 00                  jmp 0x140a5b7be
00A5A276  48 8B CF                        mov rcx, rdi
00A5A279  E8 52 9E D6 FF                  call 0x1407c40d0
00A5A27E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5A282  E9 AB F7 FF FF                  jmp 0x140a59a32
00A5A287  45 85 DB                        test r11d, r11d
00A5A28A  0F 85 2B E7 FF FF               jne 0x140a589bb
00A5A290  45 8D 63 20                     lea r12d, [r11 + 0x20]
00A5A294  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
00A5A299  45 3B F4                        cmp r14d, r12d
00A5A29C  72 30                           jb 0x140a5a2ce
00A5A29E  8B 05 5C 4F 4B 00               mov eax, dword ptr [rip + 0x4b4f5c]
00A5A2A4  89 07                           mov dword ptr [rdi], eax
00A5A2A6  8B 05 58 4F 4B 00               mov eax, dword ptr [rip + 0x4b4f58]
00A5A2AC  89 47 04                        mov dword ptr [rdi + 4], eax
00A5A2AF  8B 05 53 4F 4B 00               mov eax, dword ptr [rip + 0x4b4f53]
00A5A2B5  89 47 08                        mov dword ptr [rdi + 8], eax
00A5A2B8  48 8B 05 51 4F 4B 00            mov rax, qword ptr [rip + 0x4b4f51]
00A5A2BF  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
00A5A2C3  8B 05 4F 4F 4B 00               mov eax, dword ptr [rip + 0x4b4f4f]
00A5A2C9  89 47 18                        mov dword ptr [rdi + 0x18], eax
00A5A2CC  EB 28                           jmp 0x140a5a2f6
00A5A2CE  41 83 FE 0C                     cmp r14d, 0xc
00A5A2D2  72 27                           jb 0x140a5a2fb
00A5A2D4  C7 44 24 34 0C 00 00 00         mov dword ptr [rsp + 0x34], 0xc
00A5A2DC  8B 05 1E 4F 4B 00               mov eax, dword ptr [rip + 0x4b4f1e]
00A5A2E2  89 07                           mov dword ptr [rdi], eax
00A5A2E4  8B 05 1A 4F 4B 00               mov eax, dword ptr [rip + 0x4b4f1a]
00A5A2EA  89 47 04                        mov dword ptr [rdi + 4], eax
00A5A2ED  8B 05 15 4F 4B 00               mov eax, dword ptr [rip + 0x4b4f15]
00A5A2F3  89 47 08                        mov dword ptr [rdi + 8], eax
00A5A2F6  E9 A4 14 00 00                  jmp 0x140a5b79f
00A5A2FB  41 BD 04 00 00 C0               mov r13d, 0xc0000004
00A5A301  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
00A5A306  E9 94 14 00 00                  jmp 0x140a5b79f
00A5A30B  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5A30F  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A5A314  E9 86 14 00 00                  jmp 0x140a5b79f
00A5A319  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A5A31E  41 8B D6                        mov edx, r14d
00A5A321  48 8B CF                        mov rcx, rdi
00A5A324  E8 B3 D8 CB FF                  call 0x140717bdc
00A5A329  E9 45 14 00 00                  jmp 0x140a5b773
00A5A32E  B8 AE 00 00 00                  mov eax, 0xae
00A5A333  3B D8                           cmp ebx, eax
00A5A335  0F 8F 33 04 00 00               jg 0x140a5a76e
00A5A33B  0F 84 18 04 00 00               je 0x140a5a759
00A5A341  B8 A6 00 00 00                  mov eax, 0xa6
00A5A346  3B D8                           cmp ebx, eax
00A5A348  0F 8F BC 02 00 00               jg 0x140a5a60a
00A5A34E  0F 84 A1 02 00 00               je 0x140a5a5f5
00A5A354  8B CB                           mov ecx, ebx
00A5A356  81 E9 A0 00 00 00               sub ecx, 0xa0
00A5A35C  0F 84 E4 01 00 00               je 0x140a5a546
00A5A362  41 2B CC                        sub ecx, r12d
00A5A365  0F 84 C6 01 00 00               je 0x140a5a531
00A5A36B  83 E9 01                        sub ecx, 1
00A5A36E  0F 84 8B 01 00 00               je 0x140a5a4ff
00A5A374  83 E9 01                        sub ecx, 1
00A5A377  0F 84 70 13 00 00               je 0x140a5b6ed
00A5A37D  83 F9 01                        cmp ecx, 1
00A5A380  0F 85 5D 13 00 00               jne 0x140a5b6e3
00A5A386  C7 44 24 34 10 00 00 00         mov dword ptr [rsp + 0x34], 0x10
00A5A38E  41 83 FE 10                     cmp r14d, 0x10
00A5A392  74 1A                           je 0x140a5a3ae
00A5A394  4D 85 FF                        test r15, r15
00A5A397  0F 84 1E E6 FF FF               je 0x140a589bb
00A5A39D  41 C7 07 10 00 00 00            mov dword ptr [r15], 0x10
00A5A3A4  E9 12 E6 FF FF                  jmp 0x140a589bb
00A5A3A9  E9 10 14 00 00                  jmp 0x140a5b7be
00A5A3AE  8A 0D C4 4C 4A 00               mov cl, byte ptr [rip + 0x4a4cc4]
00A5A3B4  41 22 CD                        and cl, r13b
00A5A3B7  C0 E1 04                        shl cl, 4
00A5A3BA  8A 84 24 E0 01 00 00            mov al, byte ptr [rsp + 0x1e0]
00A5A3C1  24 EF                           and al, 0xef
00A5A3C3  0A C8                           or cl, al
00A5A3C5  88 8C 24 E0 01 00 00            mov byte ptr [rsp + 0x1e0], cl
00A5A3CC  E8 23 D2 A6 FF                  call 0x1404c75f4
00A5A3D1  84 C0                           test al, al
00A5A3D3  0F 84 10 01 00 00               je 0x140a5a4e9
00A5A3D9  40 88 74 24 60                  mov byte ptr [rsp + 0x60], sil
00A5A3DE  41 0A CD                        or cl, r13b
00A5A3E1  88 8C 24 E0 01 00 00            mov byte ptr [rsp + 0x1e0], cl
00A5A3E8  33 C9                           xor ecx, ecx
00A5A3EA  E8 75 7D 89 FF                  call 0x1402f2164
00A5A3EF  8B D8                           mov ebx, eax
00A5A3F1  41 84 C4                        test r12b, al
00A5A3F4  74 08                           je 0x140a5a3fe
00A5A3F6  44 08 A4 24 E0 01 00 00         or byte ptr [rsp + 0x1e0], r12b
00A5A3FE  41 BC 20 00 00 00               mov r12d, 0x20
00A5A404  41 84 DC                        test r12b, bl
00A5A407  74 08                           je 0x140a5a411
00A5A409  80 8C 24 E0 01 00 00 04         or byte ptr [rsp + 0x1e0], 4
00A5A411  F6 C3 10                        test bl, 0x10
00A5A414  74 08                           je 0x140a5a41e
00A5A416  80 8C 24 E0 01 00 00 08         or byte ptr [rsp + 0x1e0], 8
00A5A41E  8A 8C 24 E1 01 00 00            mov cl, byte ptr [rsp + 0x1e1]
00A5A425  0F BA E3 09                     bt ebx, 9
00A5A429  73 0A                           jae 0x140a5a435
00A5A42B  80 C9 02                        or cl, 2
00A5A42E  88 8C 24 E1 01 00 00            mov byte ptr [rsp + 0x1e1], cl
00A5A435  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
00A5A43D  48 85 C0                        test rax, rax
00A5A440  74 2B                           je 0x140a5a46d
00A5A442  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00A5A447  48 8B C8                        mov rcx, rax
00A5A44A  E8 39 38 A6 FF                  call 0x1404bdc88
00A5A44F  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5A453  8A 8C 24 E1 01 00 00            mov cl, byte ptr [rsp + 0x1e1]
00A5A45A  80 E1 FE                        and cl, 0xfe
00A5A45D  8A 44 24 60                     mov al, byte ptr [rsp + 0x60]
00A5A461  41 22 C5                        and al, r13b
00A5A464  0A C8                           or cl, al
00A5A466  88 8C 24 E1 01 00 00            mov byte ptr [rsp + 0x1e1], cl
00A5A46D  0F BA E3 0B                     bt ebx, 0xb
00A5A471  73 0A                           jae 0x140a5a47d
00A5A473  80 C9 04                        or cl, 4
00A5A476  88 8C 24 E1 01 00 00            mov byte ptr [rsp + 0x1e1], cl
00A5A47D  0F BA E3 0C                     bt ebx, 0xc
00A5A481  73 0A                           jae 0x140a5a48d
00A5A483  80 C9 08                        or cl, 8
00A5A486  88 8C 24 E1 01 00 00            mov byte ptr [rsp + 0x1e1], cl
00A5A48D  0F BA E3 0D                     bt ebx, 0xd
00A5A491  73 0A                           jae 0x140a5a49d
00A5A493  80 C9 10                        or cl, 0x10
00A5A496  88 8C 24 E1 01 00 00            mov byte ptr [rsp + 0x1e1], cl
00A5A49D  0F BA E3 10                     bt ebx, 0x10
00A5A4A1  73 0A                           jae 0x140a5a4ad
00A5A4A3  41 0A CC                        or cl, r12b
00A5A4A6  88 8C 24 E1 01 00 00            mov byte ptr [rsp + 0x1e1], cl
00A5A4AD  0F BA E3 12                     bt ebx, 0x12
00A5A4B1  73 0A                           jae 0x140a5a4bd
00A5A4B3  80 C9 40                        or cl, 0x40
00A5A4B6  88 8C 24 E1 01 00 00            mov byte ptr [rsp + 0x1e1], cl
00A5A4BD  0F BA E3 13                     bt ebx, 0x13
00A5A4C1  73 08                           jae 0x140a5a4cb
00A5A4C3  44 08 AC 24 E2 01 00 00         or byte ptr [rsp + 0x1e2], r13b
00A5A4CB  E8 54 74 04 00                  call 0x140aa1924
00A5A4D0  41 22 C5                        and al, r13b
00A5A4D3  C0 E0 05                        shl al, 5
00A5A4D6  8A 8C 24 E0 01 00 00            mov cl, byte ptr [rsp + 0x1e0]
00A5A4DD  80 E1 DF                        and cl, 0xdf
00A5A4E0  0A C1                           or al, cl
00A5A4E2  88 84 24 E0 01 00 00            mov byte ptr [rsp + 0x1e0], al
00A5A4E9  0F 28 84 24 E0 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x1e0]
00A5A4F1  F3 0F 7F 07                     movdqu xmmword ptr [rdi], xmm0
00A5A4F5  E9 A5 12 00 00                  jmp 0x140a5b79f
00A5A4FA  E9 BF 12 00 00                  jmp 0x140a5b7be
00A5A4FF  45 3B F5                        cmp r14d, r13d
00A5A502  73 16                           jae 0x140a5a51a
00A5A504  4D 85 FF                        test r15, r15
00A5A507  0F 84 48 12 00 00               je 0x140a5b755
00A5A50D  45 89 2F                        mov dword ptr [r15], r13d
00A5A510  E9 40 12 00 00                  jmp 0x140a5b755
00A5A515  E9 A4 12 00 00                  jmp 0x140a5b7be
00A5A51A  8A 05 80 B7 4F 00               mov al, byte ptr [rip + 0x4fb780]
00A5A520  88 07                           mov byte ptr [rdi], al
00A5A522  44 89 6C 24 34                  mov dword ptr [rsp + 0x34], r13d
00A5A527  E9 73 12 00 00                  jmp 0x140a5b79f
00A5A52C  E9 8D 12 00 00                  jmp 0x140a5b7be
00A5A531  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5A536  41 8B D6                        mov edx, r14d
00A5A539  48 8B CF                        mov rcx, rdi
00A5A53C  E8 33 F6 BA FF                  call 0x140609b74
00A5A541  E9 2D 12 00 00                  jmp 0x140a5b773
00A5A546  41 8B C1                        mov eax, r9d
00A5A549  C1 E0 06                        shl eax, 6
00A5A54C  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00A5A550  41 83 FE 40                     cmp r14d, 0x40
00A5A554  0F 82 85 EB FF FF               jb 0x140a590df
00A5A55A  44 3B F0                        cmp r14d, eax
00A5A55D  73 0F                           jae 0x140a5a56e
00A5A55F  45 8B CE                        mov r9d, r14d
00A5A562  41 C1 E9 06                     shr r9d, 6
00A5A566  44 89 4C 24 64                  mov dword ptr [rsp + 0x64], r9d
00A5A56B  44 3B F0                        cmp r14d, eax
00A5A56E  1B C0                           sbb eax, eax
00A5A570  25 04 00 00 C0                  and eax, 0xc0000004
00A5A575  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
00A5A57C  48 89 BC 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdi
00A5A584  44 8B E6                        mov r12d, esi
00A5A587  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
00A5A58B  4C 8D 35 AE E6 56 00            lea r14, [rip + 0x56e6ae]
00A5A592  BB 01 00 00 00                  mov ebx, 1
00A5A597  45 3B E1                        cmp r12d, r9d
00A5A59A  73 4D                           jae 0x140a5a5e9
00A5A59C  66 44 89 54 24 3C               mov word ptr [rsp + 0x3c], r10w
00A5A5A2  44 88 64 24 3E                  mov byte ptr [rsp + 0x3e], r12b
00A5A5A7  40 88 74 24 3F                  mov byte ptr [rsp + 0x3f], sil
00A5A5AC  48 8D 4C 24 3C                  lea rcx, [rsp + 0x3c]
00A5A5B1  E8 1A 2D 88 FF                  call 0x1402dd2d0
00A5A5B6  8B C8                           mov ecx, eax
00A5A5B8  49 8B 0C CE                     mov rcx, qword ptr [r14 + rcx*8]
00A5A5BC  48 8B D7                        mov rdx, rdi
00A5A5BF  E8 98 C0 A2 FF                  call 0x14048665c
00A5A5C4  48 83 C7 40                     add rdi, 0x40
00A5A5C8  48 89 BC 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdi
00A5A5D0  44 03 E3                        add r12d, ebx
00A5A5D3  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
00A5A5D8  44 8B 4C 24 64                  mov r9d, dword ptr [rsp + 0x64]
00A5A5DD  44 8B 54 24 68                  mov r10d, dword ptr [rsp + 0x68]
00A5A5E2  EB B3                           jmp 0x140a5a597
00A5A5E4  E9 D5 11 00 00                  jmp 0x140a5b7be
00A5A5E9  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
00A5A5F0  E9 7E 11 00 00                  jmp 0x140a5b773
00A5A5F5  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5A5FA  41 8B D6                        mov edx, r14d
00A5A5FD  48 8B CF                        mov rcx, rdi
00A5A600  E8 83 6D DE FF                  call 0x140841388
00A5A605  E9 69 11 00 00                  jmp 0x140a5b773
00A5A60A  8B CB                           mov ecx, ebx
00A5A60C  81 E9 A7 00 00 00               sub ecx, 0xa7
00A5A612  0F 84 27 01 00 00               je 0x140a5a73f
00A5A618  41 2B CC                        sub ecx, r12d
00A5A61B  0F 84 09 01 00 00               je 0x140a5a72a
00A5A621  41 2B CC                        sub ecx, r12d
00A5A624  0F 84 2B F7 FF FF               je 0x140a59d55
00A5A62A  83 E9 01                        sub ecx, 1
00A5A62D  0F 84 BA 10 00 00               je 0x140a5b6ed
00A5A633  83 F9 01                        cmp ecx, 1
00A5A636  0F 85 A7 10 00 00               jne 0x140a5b6e3
00A5A63C  8A 4C 24 38                     mov cl, byte ptr [rsp + 0x38]
00A5A640  E8 FF AD 94 FF                  call 0x1403a5444
00A5A645  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5A649  85 C0                           test eax, eax
00A5A64B  0F 88 6D 11 00 00               js 0x140a5b7be
00A5A651  BA 08 01 00 00                  mov edx, 0x108
00A5A656  89 54 24 34                     mov dword ptr [rsp + 0x34], edx
00A5A65A  44 3B F2                        cmp r14d, edx
00A5A65D  0F 85 58 E3 FF FF               jne 0x140a589bb
00A5A663  41 B8 49 6E 66 6F               mov r8d, 0x6f666e49
00A5A669  44 8D 72 F8                     lea r14d, [rdx - 8]
00A5A66D  41 8B CE                        mov ecx, r14d
00A5A670  E8 7B 7A 12 00                  call 0x140b820f0
00A5A675  48 8B D8                        mov rbx, rax
00A5A678  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A5A67D  48 85 C0                        test rax, rax
00A5A680  75 0A                           jne 0x140a5a68c
00A5A682  B8 9A 00 00 C0                  mov eax, 0xc000009a
00A5A687  E9 32 11 00 00                  jmp 0x140a5b7be
00A5A68C  66 44 89 28                     mov word ptr [rax], r13w
00A5A690  66 C7 40 02 20 00               mov word ptr [rax + 2], 0x20
00A5A696  89 70 04                        mov dword ptr [rax + 4], esi
00A5A699  48 8D 48 08                     lea rcx, [rax + 8]
00A5A69D  4D 8B C6                        mov r8, r14
00A5A6A0  33 D2                           xor edx, edx
00A5A6A2  E8 99 C5 C6 FF                  call 0x1406c6c40
00A5A6A7  48 8B CB                        mov rcx, rbx
00A5A6AA  E8 85 AF B6 FF                  call 0x1405c5634
00A5A6AF  90                              nop
00A5A6B0  48 8B CB                        mov rcx, rbx
00A5A6B3  B8 02 00 00 00                  mov eax, 2
00A5A6B8  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00A5A6BB  0F 11 07                        movups xmmword ptr [rdi], xmm0
00A5A6BE  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
00A5A6C2  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
00A5A6C6  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
00A5A6CA  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
00A5A6CE  0F 10 49 30                     movups xmm1, xmmword ptr [rcx + 0x30]
00A5A6D2  0F 11 4F 30                     movups xmmword ptr [rdi + 0x30], xmm1
00A5A6D6  0F 10 41 40                     movups xmm0, xmmword ptr [rcx + 0x40]
00A5A6DA  0F 11 47 40                     movups xmmword ptr [rdi + 0x40], xmm0
00A5A6DE  0F 10 49 50                     movups xmm1, xmmword ptr [rcx + 0x50]
00A5A6E2  0F 11 4F 50                     movups xmmword ptr [rdi + 0x50], xmm1
00A5A6E6  0F 10 41 60                     movups xmm0, xmmword ptr [rcx + 0x60]
00A5A6EA  0F 11 47 60                     movups xmmword ptr [rdi + 0x60], xmm0
00A5A6EE  48 8D BF 80 00 00 00            lea rdi, [rdi + 0x80]
00A5A6F5  0F 10 49 70                     movups xmm1, xmmword ptr [rcx + 0x70]
00A5A6F9  0F 11 4F F0                     movups xmmword ptr [rdi - 0x10], xmm1
00A5A6FD  48 8D 89 80 00 00 00            lea rcx, [rcx + 0x80]
00A5A704  48 83 E8 01                     sub rax, 1
00A5A708  75 AE                           jne 0x140a5a6b8
00A5A70A  48 8B 01                        mov rax, qword ptr [rcx]
00A5A70D  48 89 07                        mov qword ptr [rdi], rax
00A5A710  E9 16 F0 FF FF                  jmp 0x140a5972b
00A5A715  8B D8                           mov ebx, eax
00A5A717  33 D2                           xor edx, edx
00A5A719  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A5A71E  E8 4D 81 12 00                  call 0x140b82870
00A5A723  8B C3                           mov eax, ebx
00A5A725  E9 94 10 00 00                  jmp 0x140a5b7be
00A5A72A  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5A72F  41 8B D6                        mov edx, r14d
00A5A732  48 8B CF                        mov rcx, rdi
00A5A735  E8 F6 C6 03 00                  call 0x140a96e30
00A5A73A  E9 34 10 00 00                  jmp 0x140a5b773
00A5A73F  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A5A744  44 8A 44 24 38                  mov r8b, byte ptr [rsp + 0x38]
00A5A749  41 8B D6                        mov edx, r14d
00A5A74C  48 8B CF                        mov rcx, rdi
00A5A74F  E8 5C A8 D6 FF                  call 0x1407c4fb0
00A5A754  E9 1A 10 00 00                  jmp 0x140a5b773
00A5A759  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5A75E  41 8B D6                        mov edx, r14d
00A5A761  48 8B CF                        mov rcx, rdi
00A5A764  E8 A7 4D D2 FF                  call 0x14077f510
00A5A769  E9 05 10 00 00                  jmp 0x140a5b773
00A5A76E  B8 B6 00 00 00                  mov eax, 0xb6
00A5A773  3B D8                           cmp ebx, eax
00A5A775  0F 8F 2F 03 00 00               jg 0x140a5aaaa
00A5A77B  0F 84 DA 01 00 00               je 0x140a5a95b
00A5A781  8B CB                           mov ecx, ebx
00A5A783  81 E9 AF 00 00 00               sub ecx, 0xaf
00A5A789  0F 84 3A 01 00 00               je 0x140a5a8c9
00A5A78F  83 E9 03                        sub ecx, 3
00A5A792  0F 84 9A 00 00 00               je 0x140a5a832
00A5A798  83 E9 01                        sub ecx, 1
00A5A79B  0F 84 B4 F5 FF FF               je 0x140a59d55
00A5A7A1  83 E9 01                        sub ecx, 1
00A5A7A4  74 6A                           je 0x140a5a810
00A5A7A6  83 F9 01                        cmp ecx, 1
00A5A7A9  0F 85 34 0F 00 00               jne 0x140a5b6e3
00A5A7AF  4D 85 C0                        test r8, r8
00A5A7B2  0F 84 4E 0B 00 00               je 0x140a5b306
00A5A7B8  4C 8B 05 D9 C2 56 00            mov r8, qword ptr [rip + 0x56c2d9]
00A5A7BF  48 89 B4 24 98 01 00 00         mov qword ptr [rsp + 0x198], rsi
00A5A7C7  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00A5A7CC  48 8D 84 24 98 01 00 00         lea rax, [rsp + 0x198]
00A5A7D4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5A7D9  44 8A 4C 24 38                  mov r9b, byte ptr [rsp + 0x38]
00A5A7DE  BA 00 10 00 00                  mov edx, 0x1000
00A5A7E3  48 8B 8C 24 50 01 00 00         mov rcx, qword ptr [rsp + 0x150]
00A5A7EB  E8 C0 E5 E0 FF                  call 0x140868db0
00A5A7F0  48 8B 9C 24 98 01 00 00         mov rbx, qword ptr [rsp + 0x198]
00A5A7F8  48 89 9C 24 20 01 00 00         mov qword ptr [rsp + 0x120], rbx
00A5A800  85 C0                           test eax, eax
00A5A802  0F 88 B6 0F 00 00               js 0x140a5b7be
00A5A808  4C 8B E3                        mov r12, rbx
00A5A80B  E9 01 0B 00 00                  jmp 0x140a5b311
00A5A810  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A5A815  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5A81A  45 8B CE                        mov r9d, r14d
00A5A81D  4C 8B C7                        mov r8, rdi
00A5A820  41 8B D3                        mov edx, r11d
00A5A823  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A5A828  E8 17 A0 D6 FF                  call 0x1407c4844
00A5A82D  E9 41 0F 00 00                  jmp 0x140a5b773
00A5A832  45 85 F6                        test r14d, r14d
00A5A835  0F 84 A4 E8 FF FF               je 0x140a590df
00A5A83B  8A 5C 24 38                     mov bl, byte ptr [rsp + 0x38]
00A5A83F  84 DB                           test bl, bl
00A5A841  74 16                           je 0x140a5a859
00A5A843  8A D3                           mov dl, bl
00A5A845  48 8B 0D FC F2 57 00            mov rcx, qword ptr [rip + 0x57f2fc]
00A5A84C  E8 CF 75 E1 FF                  call 0x140871e20
00A5A851  84 C0                           test al, al
00A5A853  0F 84 B7 09 00 00               je 0x140a5b210
00A5A859  49 8B D6                        mov rdx, r14
00A5A85C  B9 41 00 00 00                  mov ecx, 0x41
00A5A861  41 B8 49 6E 66 6F               mov r8d, 0x6f666e49
00A5A867  E8 84 78 12 00                  call 0x140b820f0
00A5A86C  48 8B D8                        mov rbx, rax
00A5A86F  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A5A874  48 85 C0                        test rax, rax
00A5A877  0F 84 7C EC FF FF               je 0x140a594f9
00A5A87D  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A5A882  45 8B C6                        mov r8d, r14d
00A5A885  48 8B D0                        mov rdx, rax
00A5A888  48 8B 8C 24 80 01 00 00         mov rcx, qword ptr [rsp + 0x180]
00A5A890  E8 43 46 B3 FF                  call 0x14058eed8
00A5A895  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5A899  85 C0                           test eax, eax
00A5A89B  0F 88 40 F2 FF FF               js 0x140a59ae1
00A5A8A1  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00A5A8A6  48 8B D3                        mov rdx, rbx
00A5A8A9  48 8B CF                        mov rcx, rdi
00A5A8AC  E8 8F BF C6 FF                  call 0x1406c6840
00A5A8B1  E9 2B F2 FF FF                  jmp 0x140a59ae1
00A5A8B6  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5A8BA  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00A5A8BF  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A5A8C4  E9 18 F2 FF FF                  jmp 0x140a59ae1
00A5A8C9  4D 85 C0                        test r8, r8
00A5A8CC  74 55                           je 0x140a5a923
00A5A8CE  4C 8B 05 C3 C1 56 00            mov r8, qword ptr [rip + 0x56c1c3]
00A5A8D5  48 89 B4 24 88 01 00 00         mov qword ptr [rsp + 0x188], rsi
00A5A8DD  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00A5A8E2  48 8D 84 24 88 01 00 00         lea rax, [rsp + 0x188]
00A5A8EA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5A8EF  44 8A 4C 24 38                  mov r9b, byte ptr [rsp + 0x38]
00A5A8F4  BA 00 10 00 00                  mov edx, 0x1000
00A5A8F9  48 8B 8C 24 50 01 00 00         mov rcx, qword ptr [rsp + 0x150]
00A5A901  E8 AA E4 E0 FF                  call 0x140868db0
00A5A906  48 8B 9C 24 88 01 00 00         mov rbx, qword ptr [rsp + 0x188]
00A5A90E  48 89 9C 24 20 01 00 00         mov qword ptr [rsp + 0x120], rbx
00A5A916  85 C0                           test eax, eax
00A5A918  0F 88 A0 0E 00 00               js 0x140a5b7be
00A5A91E  4C 8B E3                        mov r12, rbx
00A5A921  EB 0B                           jmp 0x140a5a92e
00A5A923  4C 8B E6                        mov r12, rsi
00A5A926  48 8B 9C 24 20 01 00 00         mov rbx, qword ptr [rsp + 0x120]
00A5A92E  4C 8B CB                        mov r9, rbx
00A5A931  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5A936  41 8B D6                        mov edx, r14d
00A5A939  48 8B CF                        mov rcx, rdi
00A5A93C  E8 13 44 03 00                  call 0x140a8ed54
00A5A941  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5A945  4D 85 E4                        test r12, r12
00A5A948  0F 84 51 0E 00 00               je 0x140a5b79f
00A5A94E  48 8B CB                        mov rcx, rbx
00A5A951  E8 FA E9 89 FF                  call 0x1402f9350
00A5A956  E9 44 0E 00 00                  jmp 0x140a5b79f
00A5A95B  41 83 FE 38                     cmp r14d, 0x38
00A5A95F  74 1A                           je 0x140a5a97b
00A5A961  4D 85 FF                        test r15, r15
00A5A964  0F 84 EB 0D 00 00               je 0x140a5b755
00A5A96A  41 C7 07 38 00 00 00            mov dword ptr [r15], 0x38
00A5A971  E9 DF 0D 00 00                  jmp 0x140a5b755
00A5A976  E9 43 0E 00 00                  jmp 0x140a5b7be
00A5A97B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A5A984  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00A5A98B  E8 B4 11 A2 FF                  call 0x14047bb44
00A5A990  0F B7 D8                        movzx ebx, ax
00A5A993  0F B7 C8                        movzx ecx, ax
00A5A996  E8 E5 D5 A0 FF                  call 0x140467f80
00A5A99B  48 C1 E0 0C                     shl rax, 0xc
00A5A99F  48 89 84 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rax
00A5A9A7  0F B7 CB                        movzx ecx, bx
00A5A9AA  E8 11 FB A0 FF                  call 0x14046a4c0
00A5A9AF  48 C1 E0 0C                     shl rax, 0xc
00A5A9B3  48 89 84 24 E8 01 00 00         mov qword ptr [rsp + 0x1e8], rax
00A5A9BB  E8 C0 1A A1 FF                  call 0x14046c480
00A5A9C0  48 C1 E0 0C                     shl rax, 0xc
00A5A9C4  48 89 84 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rax
00A5A9CC  E8 67 0C A1 FF                  call 0x14046b638
00A5A9D1  48 C1 E0 0C                     shl rax, 0xc
00A5A9D5  48 89 84 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rax
00A5A9DD  E8 72 0D A1 FF                  call 0x14046b754
00A5A9E2  48 C1 E0 0C                     shl rax, 0xc
00A5A9E6  48 89 84 24 08 02 00 00         mov qword ptr [rsp + 0x208], rax
00A5A9EE  E8 01 13 A1 FF                  call 0x14046bcf4
00A5A9F3  48 C1 E0 0C                     shl rax, 0xc
00A5A9F7  48 89 84 24 10 02 00 00         mov qword ptr [rsp + 0x210], rax
00A5A9FF  E8 BC 10 A2 FF                  call 0x14047bac0
00A5AA04  48 C1 E0 0C                     shl rax, 0xc
00A5AA08  48 89 84 24 00 02 00 00         mov qword ptr [rsp + 0x200], rax
00A5AA10  48 8B 84 24 E0 01 00 00         mov rax, qword ptr [rsp + 0x1e0]
00A5AA18  48 3B 84 24 E8 01 00 00         cmp rax, qword ptr [rsp + 0x1e8]
00A5AA20  48 0F 42 84 24 E8 01 00 00      cmovb rax, qword ptr [rsp + 0x1e8]
00A5AA29  48 89 84 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rax
00A5AA31  48 8B 84 24 08 02 00 00         mov rax, qword ptr [rsp + 0x208]
00A5AA39  48 8B 8C 24 F8 01 00 00         mov rcx, qword ptr [rsp + 0x1f8]
00A5AA41  48 3B C1                        cmp rax, rcx
00A5AA44  48 0F 42 C1                     cmovb rax, rcx
00A5AA48  48 89 84 24 08 02 00 00         mov qword ptr [rsp + 0x208], rax
00A5AA50  48 8B 84 24 10 02 00 00         mov rax, qword ptr [rsp + 0x210]
00A5AA58  48 3B C1                        cmp rax, rcx
00A5AA5B  48 0F 42 C1                     cmovb rax, rcx
00A5AA5F  48 89 84 24 10 02 00 00         mov qword ptr [rsp + 0x210], rax
00A5AA67  0F 28 84 24 E0 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x1e0]
00A5AA6F  0F 11 07                        movups xmmword ptr [rdi], xmm0
00A5AA72  0F 28 8C 24 F0 01 00 00         movaps xmm1, xmmword ptr [rsp + 0x1f0]
00A5AA7A  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
00A5AA7E  0F 28 84 24 00 02 00 00         movaps xmm0, xmmword ptr [rsp + 0x200]
00A5AA86  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
00A5AA8A  F2 0F 10 84 24 10 02 00 00      movsd xmm0, qword ptr [rsp + 0x210]
00A5AA93  F2 0F 11 47 30                  movsd qword ptr [rdi + 0x30], xmm0
00A5AA98  C7 44 24 34 38 00 00 00         mov dword ptr [rsp + 0x34], 0x38
00A5AAA0  E9 FA 0C 00 00                  jmp 0x140a5b79f
00A5AAA5  E9 14 0D 00 00                  jmp 0x140a5b7be
00A5AAAA  81 EB B7 00 00 00               sub ebx, 0xb7
00A5AAB0  0F 84 52 01 00 00               je 0x140a5ac08
00A5AAB6  83 EB 01                        sub ebx, 1
00A5AAB9  0F 84 A7 00 00 00               je 0x140a5ab66
00A5AABF  83 EB 01                        sub ebx, 1
00A5AAC2  0F 84 8E 00 00 00               je 0x140a5ab56
00A5AAC8  83 EB 01                        sub ebx, 1
00A5AACB  74 41                           je 0x140a5ab0e
00A5AACD  41 3B DC                        cmp ebx, r12d
00A5AAD0  0F 85 0D 0C 00 00               jne 0x140a5b6e3
00A5AAD6  41 83 FE 08                     cmp r14d, 8
00A5AADA  0F 85 75 0C 00 00               jne 0x140a5b755
00A5AAE0  48 8D 8C 24 E0 01 00 00         lea rcx, [rsp + 0x1e0]
00A5AAE8  E8 97 82 B8 FF                  call 0x1405e2d84
00A5AAED  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5AAF1  85 C0                           test eax, eax
00A5AAF3  0F 88 A6 0C 00 00               js 0x140a5b79f
00A5AAF9  48 8B 84 24 E0 01 00 00         mov rax, qword ptr [rsp + 0x1e0]
00A5AB01  48 89 07                        mov qword ptr [rdi], rax
00A5AB04  E9 96 0C 00 00                  jmp 0x140a5b79f
00A5AB09  E9 B0 0C 00 00                  jmp 0x140a5b7be
00A5AB0E  45 85 F6                        test r14d, r14d
00A5AB11  74 16                           je 0x140a5ab29
00A5AB13  4D 85 FF                        test r15, r15
00A5AB16  0F 84 39 0C 00 00               je 0x140a5b755
00A5AB1C  41 89 37                        mov dword ptr [r15], esi
00A5AB1F  E9 31 0C 00 00                  jmp 0x140a5b755
00A5AB24  E9 95 0C 00 00                  jmp 0x140a5b7be
00A5AB29  44 88 AC 24 E6 00 00 00         mov byte ptr [rsp + 0xe6], r13b
00A5AB31  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
00A5AB36  4C 8D 8C 24 E6 00 00 00         lea r9, [rsp + 0xe6]
00A5AB3E  BA 03 00 20 10                  mov edx, 0x10200003
00A5AB43  41 B8 A0 00 00 26               mov r8d, 0x260000a0
00A5AB49  41 8B CD                        mov ecx, r13d
00A5AB4C  E8 FF 42 C5 FF                  call 0x1406aee50
00A5AB51  E9 68 0C 00 00                  jmp 0x140a5b7be
00A5AB56  41 8B D6                        mov edx, r14d
00A5AB59  48 8B CF                        mov rcx, rdi
00A5AB5C  E8 BF 88 E7 FF                  call 0x1408d3420
00A5AB61  E9 0D 0C 00 00                  jmp 0x140a5b773
00A5AB66  41 83 FE 18                     cmp r14d, 0x18
00A5AB6A  74 1A                           je 0x140a5ab86
00A5AB6C  4D 85 FF                        test r15, r15
00A5AB6F  0F 84 E0 0B 00 00               je 0x140a5b755
00A5AB75  41 C7 07 18 00 00 00            mov dword ptr [r15], 0x18
00A5AB7C  E9 D4 0B 00 00                  jmp 0x140a5b755
00A5AB81  E9 38 0C 00 00                  jmp 0x140a5b7be
00A5AB86  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A5AB8F  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00A5AB96  E8 A9 0F A2 FF                  call 0x14047bb44
00A5AB9B  0F B7 D8                        movzx ebx, ax
00A5AB9E  0F B7 C8                        movzx ecx, ax
00A5ABA1  E8 DA D3 A0 FF                  call 0x140467f80
00A5ABA6  48 C1 E0 0C                     shl rax, 0xc
00A5ABAA  48 89 84 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rax
00A5ABB2  0F B7 CB                        movzx ecx, bx
00A5ABB5  E8 56 97 A2 FF                  call 0x140484310
00A5ABBA  48 C1 E0 0C                     shl rax, 0xc
00A5ABBE  48 89 84 24 E8 01 00 00         mov qword ptr [rsp + 0x1e8], rax
00A5ABC6  E8 75 E4 A1 FF                  call 0x140479040
00A5ABCB  48 C1 E0 0C                     shl rax, 0xc
00A5ABCF  48 05 FF 0F 00 00               add rax, 0xfff
00A5ABD5  48 89 84 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rax
00A5ABDD  0F 28 84 24 E0 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x1e0]
00A5ABE5  0F 11 07                        movups xmmword ptr [rdi], xmm0
00A5ABE8  F2 0F 10 84 24 F0 01 00 00      movsd xmm0, qword ptr [rsp + 0x1f0]
00A5ABF1  F2 0F 11 47 10                  movsd qword ptr [rdi + 0x10], xmm0
00A5ABF6  C7 44 24 34 18 00 00 00         mov dword ptr [rsp + 0x34], 0x18
00A5ABFE  E9 9C 0B 00 00                  jmp 0x140a5b79f
00A5AC03  E9 B6 0B 00 00                  jmp 0x140a5b7be
00A5AC08  41 83 FE 10                     cmp r14d, 0x10
00A5AC0C  0F 85 43 0B 00 00               jne 0x140a5b755
00A5AC12  48 8B 0F                        mov rcx, qword ptr [rdi]
00A5AC15  48 89 8C 24 D0 01 00 00         mov qword ptr [rsp + 0x1d0], rcx
00A5AC1D  8B 57 08                        mov edx, dword ptr [rdi + 8]
00A5AC20  89 94 24 C0 01 00 00            mov dword ptr [rsp + 0x1c0], edx
00A5AC27  E8 00 A9 02 00                  call 0x140a8552c
00A5AC2C  E9 42 0B 00 00                  jmp 0x140a5b773
00A5AC31  E9 88 0B 00 00                  jmp 0x140a5b7be
00A5AC36  B8 DE 00 00 00                  mov eax, 0xde
00A5AC3B  3B D8                           cmp ebx, eax
00A5AC3D  0F 8F 66 06 00 00               jg 0x140a5b2a9
00A5AC43  0F 84 2B 06 00 00               je 0x140a5b274
00A5AC49  81 FB CA 00 00 00               cmp ebx, 0xca
00A5AC4F  0F 8F 7A 03 00 00               jg 0x140a5afcf
00A5AC55  0F 84 F3 02 00 00               je 0x140a5af4e
00A5AC5B  B8 C4 00 00 00                  mov eax, 0xc4
00A5AC60  3B D8                           cmp ebx, eax
00A5AC62  0F 8F 84 01 00 00               jg 0x140a5adec
00A5AC68  0F 84 69 01 00 00               je 0x140a5add7
00A5AC6E  8B CB                           mov ecx, ebx
00A5AC70  81 E9 BE 00 00 00               sub ecx, 0xbe
00A5AC76  0F 84 71 0A 00 00               je 0x140a5b6ed
00A5AC7C  41 2B CC                        sub ecx, r12d
00A5AC7F  0F 84 24 01 00 00               je 0x140a5ada9
00A5AC85  83 E9 01                        sub ecx, 1
00A5AC88  74 69                           je 0x140a5acf3
00A5AC8A  83 E9 01                        sub ecx, 1
00A5AC8D  74 3A                           je 0x140a5acc9
00A5AC8F  83 F9 01                        cmp ecx, 1
00A5AC92  0F 85 4B 0A 00 00               jne 0x140a5b6e3
00A5AC98  41 83 FE 08                     cmp r14d, 8
00A5AC9C  73 1A                           jae 0x140a5acb8
00A5AC9E  4D 85 FF                        test r15, r15
00A5ACA1  0F 84 AE 0A 00 00               je 0x140a5b755
00A5ACA7  41 C7 07 08 00 00 00            mov dword ptr [r15], 8
00A5ACAE  E9 A2 0A 00 00                  jmp 0x140a5b755
00A5ACB3  E9 06 0B 00 00                  jmp 0x140a5b7be
00A5ACB8  48 8B CF                        mov rcx, rdi
00A5ACBB  E8 40 94 D6 FF                  call 0x1407c4100
00A5ACC0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5ACC4  E9 DE 03 00 00                  jmp 0x140a5b0a7
00A5ACC9  8A 5C 24 38                     mov bl, byte ptr [rsp + 0x38]
00A5ACCD  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
00A5ACD1  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A5ACD6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5ACDB  45 8B CE                        mov r9d, r14d
00A5ACDE  4C 8B C7                        mov r8, rdi
00A5ACE1  41 8B D3                        mov edx, r11d
00A5ACE4  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A5ACE9  E8 1A ED CB FF                  call 0x140719a08
00A5ACEE  E9 80 0A 00 00                  jmp 0x140a5b773
00A5ACF3  E8 08 19 A3 FF                  call 0x14048c600
00A5ACF8  0F B7 C0                        movzx eax, ax
00A5ACFB  C1 E0 03                        shl eax, 3
00A5ACFE  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00A5AD02  44 3B F0                        cmp r14d, eax
00A5AD05  0F 82 D4 E3 FF FF               jb 0x140a590df
00A5AD0B  44 8B C0                        mov r8d, eax
00A5AD0E  33 D2                           xor edx, edx
00A5AD10  48 8B CF                        mov rcx, rdi
00A5AD13  E8 28 BF C6 FF                  call 0x1406c6c40
00A5AD18  8B DE                           mov ebx, esi
00A5AD1A  8B D6                           mov edx, esi
00A5AD1C  44 8B C6                        mov r8d, esi
00A5AD1F  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00A5AD23  0F B7 05 D6 A2 56 00            movzx eax, word ptr [rip + 0x56a2d6]
00A5AD2A  3B D0                           cmp edx, eax
00A5AD2C  73 68                           jae 0x140a5ad96
00A5AD2E  41 8B D0                        mov edx, r8d
00A5AD31  48 8D 05 88 49 57 00            lea rax, [rip + 0x574988]
00A5AD38  48 8B 14 D0                     mov rdx, qword ptr [rax + rdx*8]
00A5AD3C  48 8D 8C 24 90 03 00 00         lea rcx, [rsp + 0x390]
00A5AD44  E8 67 37 9C FF                  call 0x14041e4b0
00A5AD49  48 8D 94 24 90 01 00 00         lea rdx, [rsp + 0x190]
00A5AD51  48 8D 8C 24 90 03 00 00         lea rcx, [rsp + 0x390]
00A5AD59  E8 7A B9 7F FF                  call 0x1402566d8
00A5AD5E  85 C0                           test eax, eax
00A5AD60  75 2B                           jne 0x140a5ad8d
00A5AD62  48 8B 8C 24 90 01 00 00         mov rcx, qword ptr [rsp + 0x190]
00A5AD6A  0F B7 81 88 00 00 00            movzx eax, word ptr [rcx + 0x88]
00A5AD71  66 89 44 24 54                  mov word ptr [rsp + 0x54], ax
00A5AD76  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
00A5AD7A  0F B7 44 24 54                  movzx eax, word ptr [rsp + 0x54]
00A5AD7F  48 0B 14 C7                     or rdx, qword ptr [rdi + rax*8]
00A5AD83  48 89 14 C7                     mov qword ptr [rdi + rax*8], rdx
00A5AD87  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
00A5AD8B  EB BC                           jmp 0x140a5ad49
00A5AD8D  FF C3                           inc ebx
00A5AD8F  8B D3                           mov edx, ebx
00A5AD91  44 8B C3                        mov r8d, ebx
00A5AD94  EB 89                           jmp 0x140a5ad1f
00A5AD96  E9 04 0A 00 00                  jmp 0x140a5b79f
00A5AD9B  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5AD9F  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A5ADA4  E9 F6 09 00 00                  jmp 0x140a5b79f
00A5ADA9  41 BC 20 00 00 00               mov r12d, 0x20
00A5ADAF  45 3B F4                        cmp r14d, r12d
00A5ADB2  73 16                           jae 0x140a5adca
00A5ADB4  4D 85 FF                        test r15, r15
00A5ADB7  0F 84 98 09 00 00               je 0x140a5b755
00A5ADBD  45 89 27                        mov dword ptr [r15], r12d
00A5ADC0  E9 90 09 00 00                  jmp 0x140a5b755
00A5ADC5  E9 F4 09 00 00                  jmp 0x140a5b7be
00A5ADCA  48 8B CF                        mov rcx, rdi
00A5ADCD  E8 D2 92 FF FF                  call 0x140a540a4
00A5ADD2  E9 A7 F4 FF FF                  jmp 0x140a5a27e
00A5ADD7  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5ADDC  41 8B D6                        mov edx, r14d
00A5ADDF  48 8B CF                        mov rcx, rdi
00A5ADE2  E8 99 C4 CE FF                  call 0x140747280
00A5ADE7  E9 87 09 00 00                  jmp 0x140a5b773
00A5ADEC  8B CB                           mov ecx, ebx
00A5ADEE  81 E9 C5 00 00 00               sub ecx, 0xc5
00A5ADF4  0F 84 20 01 00 00               je 0x140a5af1a
00A5ADFA  83 E9 01                        sub ecx, 1
00A5ADFD  74 46                           je 0x140a5ae45
00A5ADFF  83 E9 01                        sub ecx, 1
00A5AE02  0F 84 E5 08 00 00               je 0x140a5b6ed
00A5AE08  83 E9 01                        sub ecx, 1
00A5AE0B  74 1E                           je 0x140a5ae2b
00A5AE0D  83 F9 01                        cmp ecx, 1
00A5AE10  0F 85 CD 08 00 00               jne 0x140a5b6e3
00A5AE16  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5AE1B  41 8B D6                        mov edx, r14d
00A5AE1E  48 8B CF                        mov rcx, rdi
00A5AE21  E8 82 BA CE FF                  call 0x1407468a8
00A5AE26  E9 48 09 00 00                  jmp 0x140a5b773
00A5AE2B  B9 C8 00 00 00                  mov ecx, 0xc8
00A5AE30  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A5AE35  45 8B C6                        mov r8d, r14d
00A5AE38  48 8B D7                        mov rdx, rdi
00A5AE3B  E8 E4 1C 01 00                  call 0x140a6cb24
00A5AE40  E9 2E 09 00 00                  jmp 0x140a5b773
00A5AE45  48 8B 05 EC 57 3A 00            mov rax, qword ptr [rip + 0x3a57ec]
00A5AE4C  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
00A5AE51  45 33 C0                        xor r8d, r8d
00A5AE54  33 D2                           xor edx, edx
00A5AE56  8D 4A 22                        lea ecx, [rdx + 0x22]
00A5AE59  E8 72 FC C5 FF                  call 0x1406baad0
00A5AE5E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5AE62  41 BD 04 00 00 C0               mov r13d, 0xc0000004
00A5AE68  41 3B C5                        cmp eax, r13d
00A5AE6B  74 0A                           je 0x140a5ae77
00A5AE6D  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00A5AE72  E9 47 09 00 00                  jmp 0x140a5b7be
00A5AE77  44 3B 74 24 50                  cmp r14d, dword ptr [rsp + 0x50]
00A5AE7C  0F 82 7F E4 FF FF               jb 0x140a59301
00A5AE82  48 85 FF                        test rdi, rdi
00A5AE85  0F 84 76 E4 FF FF               je 0x140a59301
00A5AE8B  8A 5C 24 38                     mov bl, byte ptr [rsp + 0x38]
00A5AE8F  84 DB                           test bl, bl
00A5AE91  74 26                           je 0x140a5aeb9
00A5AE93  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
00A5AE97  B9 01 01 00 00                  mov ecx, 0x101
00A5AE9C  41 B8 49 6E 66 6F               mov r8d, 0x6f666e49
00A5AEA2  E8 49 72 12 00                  call 0x140b820f0
00A5AEA7  4C 8B F0                        mov r14, rax
00A5AEAA  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A5AEAF  48 85 C0                        test rax, rax
00A5AEB2  75 0D                           jne 0x140a5aec1
00A5AEB4  E9 40 E6 FF FF                  jmp 0x140a594f9
00A5AEB9  4C 8B F7                        mov r14, rdi
00A5AEBC  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00A5AEC1  48 8B 05 70 57 3A 00            mov rax, qword ptr [rip + 0x3a5770]
00A5AEC8  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A5AECD  4D 8B C6                        mov r8, r14
00A5AED0  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
00A5AED4  B9 22 00 00 00                  mov ecx, 0x22
00A5AED9  E8 F2 FB C5 FF                  call 0x1406baad0
00A5AEDE  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5AEE2  84 DB                           test bl, bl
00A5AEE4  0F 84 B5 08 00 00               je 0x140a5b79f
00A5AEEA  85 C0                           test eax, eax
00A5AEEC  0F 88 02 E4 FF FF               js 0x140a592f4
00A5AEF2  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00A5AEF7  49 8B D6                        mov rdx, r14
00A5AEFA  48 8B CF                        mov rcx, rdi
00A5AEFD  E8 3E B9 C6 FF                  call 0x1406c6840
00A5AF02  E9 ED E3 FF FF                  jmp 0x140a592f4
00A5AF07  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5AF0B  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00A5AF10  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A5AF15  E9 DA E3 FF FF                  jmp 0x140a592f4
00A5AF1A  C7 44 24 34 08 00 00 00         mov dword ptr [rsp + 0x34], 8
00A5AF22  41 83 FE 08                     cmp r14d, 8
00A5AF26  0F 82 8F DA FF FF               jb 0x140a589bb
00A5AF2C  48 8B 05 45 2C 3D 00            mov rax, qword ptr [rip + 0x3d2c45]
00A5AF33  33 C9                           xor ecx, ecx
00A5AF35  48 89 0F                        mov qword ptr [rdi], rcx
00A5AF38  48 89 07                        mov qword ptr [rdi], rax
00A5AF3B  E9 5F 08 00 00                  jmp 0x140a5b79f
00A5AF40  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5AF44  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A5AF49  E9 51 08 00 00                  jmp 0x140a5b79f
00A5AF4E  44 89 6C 24 34                  mov dword ptr [rsp + 0x34], r13d
00A5AF53  45 3B F5                        cmp r14d, r13d
00A5AF56  74 16                           je 0x140a5af6e
00A5AF58  4D 85 FF                        test r15, r15
00A5AF5B  0F 84 5A DA FF FF               je 0x140a589bb
00A5AF61  45 89 2F                        mov dword ptr [r15], r13d
00A5AF64  E9 52 DA FF FF                  jmp 0x140a589bb
00A5AF69  E9 50 08 00 00                  jmp 0x140a5b7be
00A5AF6E  89 B4 24 34 01 00 00            mov dword ptr [rsp + 0x134], esi
00A5AF75  48 8B 05 BC 56 3A 00            mov rax, qword ptr [rip + 0x3a56bc]
00A5AF7C  4C 8D 8C 24 34 01 00 00         lea r9, [rsp + 0x134]
00A5AF84  4C 8D 84 24 E0 01 00 00         lea r8, [rsp + 0x1e0]
00A5AF8C  41 8B D5                        mov edx, r13d
00A5AF8F  B9 30 00 00 00                  mov ecx, 0x30
00A5AF94  E8 37 FB C5 FF                  call 0x1406baad0
00A5AF99  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5AF9D  85 C0                           test eax, eax
00A5AF9F  0F 88 56 DC FF FF               js 0x140a58bfb
00A5AFA5  44 39 AC 24 34 01 00 00         cmp dword ptr [rsp + 0x134], r13d
00A5AFAD  0F 85 48 DC FF FF               jne 0x140a58bfb
00A5AFB3  8A 84 24 E0 01 00 00            mov al, byte ptr [rsp + 0x1e0]
00A5AFBA  88 07                           mov byte ptr [rdi], al
00A5AFBC  E9 DE 07 00 00                  jmp 0x140a5b79f
00A5AFC1  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5AFC5  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A5AFCA  E9 D0 07 00 00                  jmp 0x140a5b79f
00A5AFCF  B8 D3 00 00 00                  mov eax, 0xd3
00A5AFD4  3B D8                           cmp ebx, eax
00A5AFD6  0F 8F 12 01 00 00               jg 0x140a5b0ee
00A5AFDC  0F 84 D7 00 00 00               je 0x140a5b0b9
00A5AFE2  8B CB                           mov ecx, ebx
00A5AFE4  81 E9 CE 00 00 00               sub ecx, 0xce
00A5AFEA  0F 84 85 00 00 00               je 0x140a5b075
00A5AFF0  83 E9 01                        sub ecx, 1
00A5AFF3  74 4E                           je 0x140a5b043
00A5AFF5  83 E9 01                        sub ecx, 1
00A5AFF8  74 34                           je 0x140a5b02e
00A5AFFA  83 E9 01                        sub ecx, 1
00A5AFFD  0F 84 EA 06 00 00               je 0x140a5b6ed
00A5B003  83 F9 01                        cmp ecx, 1
00A5B006  0F 85 D7 06 00 00               jne 0x140a5b6e3
00A5B00C  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A5B011  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5B016  45 8B CE                        mov r9d, r14d
00A5B019  4C 8B C7                        mov r8, rdi
00A5B01C  41 8B D3                        mov edx, r11d
00A5B01F  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A5B024  E8 7F C0 06 00                  call 0x140ac70a8
00A5B029  E9 45 07 00 00                  jmp 0x140a5b773
00A5B02E  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5B033  41 8B D6                        mov edx, r14d
00A5B036  48 8B CF                        mov rcx, rdi
00A5B039  E8 8E 29 D4 FF                  call 0x14079d9cc
00A5B03E  E9 30 07 00 00                  jmp 0x140a5b773
00A5B043  41 83 FE 04                     cmp r14d, 4
00A5B047  74 1A                           je 0x140a5b063
00A5B049  4D 85 FF                        test r15, r15
00A5B04C  0F 84 03 07 00 00               je 0x140a5b755
00A5B052  41 C7 07 04 00 00 00            mov dword ptr [r15], 4
00A5B059  E9 F7 06 00 00                  jmp 0x140a5b755
00A5B05E  E9 5B 07 00 00                  jmp 0x140a5b7be
00A5B063  8B 05 57 93 56 00               mov eax, dword ptr [rip + 0x569357]
00A5B069  89 07                           mov dword ptr [rdi], eax
00A5B06B  E9 6B CF FF FF                  jmp 0x140a57fdb
00A5B070  E9 49 07 00 00                  jmp 0x140a5b7be
00A5B075  41 83 FE 08                     cmp r14d, 8
00A5B079  74 1A                           je 0x140a5b095
00A5B07B  4D 85 FF                        test r15, r15
00A5B07E  0F 84 D1 06 00 00               je 0x140a5b755
00A5B084  41 C7 07 08 00 00 00            mov dword ptr [r15], 8
00A5B08B  E9 C5 06 00 00                  jmp 0x140a5b755
00A5B090  E9 29 07 00 00                  jmp 0x140a5b7be
00A5B095  48 8B 05 9C 3D 4A 00            mov rax, qword ptr [rip + 0x4a3d9c]
00A5B09C  40 38 30                        cmp byte ptr [rax], sil
00A5B09F  0F 95 C0                        setne al
00A5B0A2  88 07                           mov byte ptr [rdi], al
00A5B0A4  89 77 04                        mov dword ptr [rdi + 4], esi
00A5B0A7  C7 44 24 34 08 00 00 00         mov dword ptr [rsp + 0x34], 8
00A5B0AF  E9 EB 06 00 00                  jmp 0x140a5b79f
00A5B0B4  E9 05 07 00 00                  jmp 0x140a5b7be
00A5B0B9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A5B0C2  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
00A5B0C8  88 4C 24 28                     mov byte ptr [rsp + 0x28], cl
00A5B0CC  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A5B0D1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5B0D6  45 8B CE                        mov r9d, r14d
00A5B0D9  4C 8B C7                        mov r8, rdi
00A5B0DC  41 8B D3                        mov edx, r11d
00A5B0DF  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A5B0E4  E8 DB 4F FD FF                  call 0x140a300c4
00A5B0E9  E9 85 06 00 00                  jmp 0x140a5b773
00A5B0EE  81 EB D5 00 00 00               sub ebx, 0xd5
00A5B0F4  0F 84 65 01 00 00               je 0x140a5b25f
00A5B0FA  83 EB 01                        sub ebx, 1
00A5B0FD  0F 84 06 01 00 00               je 0x140a5b209
00A5B103  83 EB 01                        sub ebx, 1
00A5B106  0F 84 A9 00 00 00               je 0x140a5b1b5
00A5B10C  83 EB 01                        sub ebx, 1
00A5B10F  74 7B                           je 0x140a5b18c
00A5B111  83 FB 05                        cmp ebx, 5
00A5B114  0F 85 C9 05 00 00               jne 0x140a5b6e3
00A5B11A  41 83 FE 04                     cmp r14d, 4
00A5B11E  74 1A                           je 0x140a5b13a
00A5B120  4D 85 FF                        test r15, r15
00A5B123  0F 84 2C 06 00 00               je 0x140a5b755
00A5B129  41 C7 07 04 00 00 00            mov dword ptr [r15], 4
00A5B130  E9 20 06 00 00                  jmp 0x140a5b755
00A5B135  E9 84 06 00 00                  jmp 0x140a5b7be
00A5B13A  33 C0                           xor eax, eax
00A5B13C  89 07                           mov dword ptr [rdi], eax
00A5B13E  E8 39 F4 A6 FF                  call 0x1404ca57c
00A5B143  0F B6 C8                        movzx ecx, al
00A5B146  41 23 CD                        and ecx, r13d
00A5B149  89 0F                           mov dword ptr [rdi], ecx
00A5B14B  E8 64 71 A4 FF                  call 0x1404a22b4
00A5B150  0F B6 D8                        movzx ebx, al
00A5B153  03 DB                           add ebx, ebx
00A5B155  33 D9                           xor ebx, ecx
00A5B157  41 23 DC                        and ebx, r12d
00A5B15A  33 D9                           xor ebx, ecx
00A5B15C  89 1F                           mov dword ptr [rdi], ebx
00A5B15E  E8 AD 24 A0 FF                  call 0x14045d610
00A5B163  0F B6 D0                        movzx edx, al
00A5B166  41 23 D5                        and edx, r13d
00A5B169  C1 E2 08                        shl edx, 8
00A5B16C  0B D3                           or edx, ebx
00A5B16E  89 17                           mov dword ptr [rdi], edx
00A5B170  E8 13 7E A7 FF                  call 0x1404d2f88
00A5B175  0F B6 C8                        movzx ecx, al
00A5B178  41 23 CD                        and ecx, r13d
00A5B17B  C1 E1 09                        shl ecx, 9
00A5B17E  0B CA                           or ecx, edx
00A5B180  89 0F                           mov dword ptr [rdi], ecx
00A5B182  E9 54 CE FF FF                  jmp 0x140a57fdb
00A5B187  E9 32 06 00 00                  jmp 0x140a5b7be
00A5B18C  41 BC 20 00 00 00               mov r12d, 0x20
00A5B192  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
00A5B197  45 3B F4                        cmp r14d, r12d
00A5B19A  0F 85 1B D8 FF FF               jne 0x140a589bb
00A5B1A0  41 8B D6                        mov edx, r14d
00A5B1A3  48 8B CF                        mov rcx, rdi
00A5B1A6  E8 F5 B5 D7 FF                  call 0x1407d67a0
00A5B1AB  41 8D 54 24 F0                  lea edx, [r12 - 0x10]
00A5B1B0  E9 EE CD FF FF                  jmp 0x140a57fa3
00A5B1B5  80 7C 24 38 00                  cmp byte ptr [rsp + 0x38], 0
00A5B1BA  74 0D                           je 0x140a5b1c9
00A5B1BC  C7 44 24 30 61 00 00 C0         mov dword ptr [rsp + 0x30], 0xc0000061
00A5B1C4  E9 D6 05 00 00                  jmp 0x140a5b79f
00A5B1C9  48 8B 05 58 3E 4A 00            mov rax, qword ptr [rip + 0x4a3e58]
00A5B1D0  48 85 C0                        test rax, rax
00A5B1D3  75 0D                           jne 0x140a5b1e2
00A5B1D5  C7 44 24 30 0E 00 00 C0         mov dword ptr [rsp + 0x30], 0xc000000e
00A5B1DD  E9 BD 05 00 00                  jmp 0x140a5b79f
00A5B1E2  C7 44 24 34 18 00 00 00         mov dword ptr [rsp + 0x34], 0x18
00A5B1EA  41 83 FE 18                     cmp r14d, 0x18
00A5B1EE  0F 82 C7 D7 FF FF               jb 0x140a589bb
00A5B1F4  0F 10 00                        movups xmm0, xmmword ptr [rax]
00A5B1F7  0F 11 07                        movups xmmword ptr [rdi], xmm0
00A5B1FA  F2 0F 10 48 10                  movsd xmm1, qword ptr [rax + 0x10]
00A5B1FF  F2 0F 11 4F 10                  movsd qword ptr [rdi + 0x10], xmm1
00A5B204  E9 96 05 00 00                  jmp 0x140a5b79f
00A5B209  80 7C 24 38 00                  cmp byte ptr [rsp + 0x38], 0
00A5B20E  74 0A                           je 0x140a5b21a
00A5B210  B8 61 00 00 C0                  mov eax, 0xc0000061
00A5B215  E9 A4 05 00 00                  jmp 0x140a5b7be
00A5B21A  48 8B 15 FF 3D 4A 00            mov rdx, qword ptr [rip + 0x4a3dff]
00A5B221  48 85 D2                        test rdx, rdx
00A5B224  0F 84 75 05 00 00               je 0x140a5b79f
00A5B22A  48 39 32                        cmp qword ptr [rdx], rsi
00A5B22D  0F 84 6C 05 00 00               je 0x140a5b79f
00A5B233  8B 02                           mov eax, dword ptr [rdx]
00A5B235  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00A5B239  48 85 FF                        test rdi, rdi
00A5B23C  0F 84 5D 05 00 00               je 0x140a5b79f
00A5B242  44 3B F0                        cmp r14d, eax
00A5B245  0F 82 70 D7 FF FF               jb 0x140a589bb
00A5B24B  48 83 C2 08                     add rdx, 8
00A5B24F  4C 8B C0                        mov r8, rax
00A5B252  48 8B CF                        mov rcx, rdi
00A5B255  E8 E6 B5 C6 FF                  call 0x1406c6840
00A5B25A  E9 40 05 00 00                  jmp 0x140a5b79f
00A5B25F  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5B264  41 8B D6                        mov edx, r14d
00A5B267  48 8B CF                        mov rcx, rdi
00A5B26A  E8 A5 37 B6 FF                  call 0x1405bea14
00A5B26F  E9 FF 04 00 00                  jmp 0x140a5b773
00A5B274  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A5B27D  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
00A5B283  88 4C 24 28                     mov byte ptr [rsp + 0x28], cl
00A5B287  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A5B28C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5B291  45 8B CE                        mov r9d, r14d
00A5B294  4C 8B C7                        mov r8, rdi
00A5B297  41 8B D3                        mov edx, r11d
00A5B29A  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A5B29F  E8 E0 35 00 00                  call 0x140a5e884
00A5B2A4  E9 CA 04 00 00                  jmp 0x140a5b773
00A5B2A9  B8 EE 00 00 00                  mov eax, 0xee
00A5B2AE  3B D8                           cmp ebx, eax
00A5B2B0  0F 8F 0A 02 00 00               jg 0x140a5b4c0
00A5B2B6  0F 84 E7 01 00 00               je 0x140a5b4a3
00A5B2BC  8D 48 F9                        lea ecx, [rax - 7]
00A5B2BF  3B D9                           cmp ebx, ecx
00A5B2C1  0F 8F 6F 01 00 00               jg 0x140a5b436
00A5B2C7  0F 84 C8 E3 FF FF               je 0x140a59695
00A5B2CD  8B CB                           mov ecx, ebx
00A5B2CF  81 E9 DF 00 00 00               sub ecx, 0xdf
00A5B2D5  0F 84 86 00 00 00               je 0x140a5b361
00A5B2DB  83 E9 04                        sub ecx, 4
00A5B2DE  74 4B                           je 0x140a5b32b
00A5B2E0  83 E9 01                        sub ecx, 1
00A5B2E3  74 09                           je 0x140a5b2ee
00A5B2E5  83 E9 01                        sub ecx, 1
00A5B2E8  0F 85 B8 F4 FF FF               jne 0x140a5a7a6
00A5B2EE  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
00A5B2F3  44 8B C3                        mov r8d, ebx
00A5B2F6  41 8B D6                        mov edx, r14d
00A5B2F9  48 8B CF                        mov rcx, rdi
00A5B2FC  E8 FF A4 B5 FF                  call 0x1405b5800
00A5B301  E9 6D 04 00 00                  jmp 0x140a5b773
00A5B306  4C 8B E6                        mov r12, rsi
00A5B309  48 8B 9C 24 20 01 00 00         mov rbx, qword ptr [rsp + 0x120]
00A5B311  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A5B316  4C 8D 4C 24 34                  lea r9, [rsp + 0x34]
00A5B31B  45 8B C6                        mov r8d, r14d
00A5B31E  48 8B CF                        mov rcx, rdi
00A5B321  E8 6A 6C E7 FF                  call 0x1408d1f90
00A5B326  E9 16 F6 FF FF                  jmp 0x140a5a941
00A5B32B  44 89 6C 24 34                  mov dword ptr [rsp + 0x34], r13d
00A5B330  45 3B F5                        cmp r14d, r13d
00A5B333  74 16                           je 0x140a5b34b
00A5B335  4D 85 FF                        test r15, r15
00A5B338  0F 84 7D D6 FF FF               je 0x140a589bb
00A5B33E  45 89 2F                        mov dword ptr [r15], r13d
00A5B341  E9 75 D6 FF FF                  jmp 0x140a589bb
00A5B346  E9 73 04 00 00                  jmp 0x140a5b7be
00A5B34B  44 88 2F                        mov byte ptr [rdi], r13b
00A5B34E  E9 4C 04 00 00                  jmp 0x140a5b79f
00A5B353  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5B357  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A5B35C  E9 3E 04 00 00                  jmp 0x140a5b79f
00A5B361  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
00A5B366  4D 85 D2                        test r10, r10
00A5B369  0F 84 74 03 00 00               je 0x140a5b6e3
00A5B36F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A5B378  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
00A5B37E  4D 8B CE                        mov r9, r14
00A5B381  41 8B D3                        mov edx, r11d
00A5B384  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
00A5B388  4C 8B C7                        mov r8, rdi
00A5B38B  49 8B CA                        mov rcx, r10
00A5B38E  E8 0D AF BF FF                  call 0x1406562a0
00A5B393  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5B397  85 C0                           test eax, eax
00A5B399  0F 88 00 04 00 00               js 0x140a5b79f
00A5B39F  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00A5B3A3  E9 0C EB FF FF                  jmp 0x140a59eb4
00A5B3A8  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5B3AC  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A5B3B1  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00A5B3B6  E9 56 E3 FF FF                  jmp 0x140a59711
00A5B3BB  44 39 6C 24 30                  cmp dword ptr [rsp + 0x30], r13d
00A5B3C0  0F 85 4B E3 FF FF               jne 0x140a59711
00A5B3C6  44 39 74 24 34                  cmp dword ptr [rsp + 0x34], r14d
00A5B3CB  76 0A                           jbe 0x140a5b3d7
00A5B3CD  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
00A5B3D2  E9 3A E3 FF FF                  jmp 0x140a59711
00A5B3D7  48 85 DB                        test rbx, rbx
00A5B3DA  74 17                           je 0x140a5b3f3
00A5B3DC  48 8D 84 24 E0 01 00 00         lea rax, [rsp + 0x1e0]
00A5B3E4  48 3B D8                        cmp rbx, rax
00A5B3E7  74 0A                           je 0x140a5b3f3
00A5B3E9  33 D2                           xor edx, edx
00A5B3EB  48 8B CB                        mov rcx, rbx
00A5B3EE  E8 7D 74 12 00                  call 0x140b82870
00A5B3F3  8B 54 24 34                     mov edx, dword ptr [rsp + 0x34]
00A5B3F7  B9 01 01 00 00                  mov ecx, 0x101
00A5B3FC  41 B8 49 6E 66 6F               mov r8d, 0x6f666e49
00A5B402  E8 E9 6C 12 00                  call 0x140b820f0
00A5B407  48 8B D8                        mov rbx, rax
00A5B40A  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A5B40F  48 85 C0                        test rax, rax
00A5B412  75 0D                           jne 0x140a5b421
00A5B414  C7 44 24 30 9A 00 00 C0         mov dword ptr [rsp + 0x30], 0xc000009a
00A5B41C  E9 F0 E2 FF FF                  jmp 0x140a59711
00A5B421  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
00A5B425  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00A5B429  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00A5B431  E9 A3 E2 FF FF                  jmp 0x140a596d9
00A5B436  81 EB E8 00 00 00               sub ebx, 0xe8
00A5B43C  0F 84 B9 D7 FF FF               je 0x140a58bfb
00A5B442  41 2B DC                        sub ebx, r12d
00A5B445  74 35                           je 0x140a5b47c
00A5B447  83 EB 01                        sub ebx, 1
00A5B44A  74 0E                           je 0x140a5b45a
00A5B44C  83 EB 01                        sub ebx, 1
00A5B44F  0F 84 A6 D7 FF FF               je 0x140a58bfb
00A5B455  E9 98 D7 FF FF                  jmp 0x140a58bf2
00A5B45A  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A5B45F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5B464  45 8A CD                        mov r9b, r13b
00A5B467  44 8A 44 24 38                  mov r8b, byte ptr [rsp + 0x38]
00A5B46C  41 8B D6                        mov edx, r14d
00A5B46F  48 8B CF                        mov rcx, rdi
00A5B472  E8 05 C9 CB FF                  call 0x140717d7c
00A5B477  E9 F7 02 00 00                  jmp 0x140a5b773
00A5B47C  B8 98 42 00 00                  mov eax, 0x4298
00A5B481  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00A5B485  44 3B F0                        cmp r14d, eax
00A5B488  0F 82 2D D5 FF FF               jb 0x140a589bb
00A5B48E  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5B493  41 8B D6                        mov edx, r14d
00A5B496  48 8B CF                        mov rcx, rdi
00A5B499  E8 E2 93 B2 FF                  call 0x140584880
00A5B49E  E9 D0 02 00 00                  jmp 0x140a5b773
00A5B4A3  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A5B4A8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5B4AD  45 8B CE                        mov r9d, r14d
00A5B4B0  4C 8B C7                        mov r8, rdi
00A5B4B3  41 8B D3                        mov edx, r11d
00A5B4B6  E8 25 A5 D7 FF                  call 0x1407d59e0
00A5B4BB  E9 B3 02 00 00                  jmp 0x140a5b773
00A5B4C0  B8 F7 00 00 00                  mov eax, 0xf7
00A5B4C5  3B D8                           cmp ebx, eax
00A5B4C7  0F 8F F4 01 00 00               jg 0x140a5b6c1
00A5B4CD  0F 84 B2 01 00 00               je 0x140a5b685
00A5B4D3  8B CB                           mov ecx, ebx
00A5B4D5  81 E9 EF 00 00 00               sub ecx, 0xef
00A5B4DB  0F 84 82 01 00 00               je 0x140a5b663
00A5B4E1  83 E9 01                        sub ecx, 1
00A5B4E4  0F 84 57 01 00 00               je 0x140a5b641
00A5B4EA  83 E9 01                        sub ecx, 1
00A5B4ED  0F 84 FA 01 00 00               je 0x140a5b6ed
00A5B4F3  41 2B CC                        sub ecx, r12d
00A5B4F6  0F 84 FB 00 00 00               je 0x140a5b5f7
00A5B4FC  83 F9 01                        cmp ecx, 1
00A5B4FF  0F 85 DE 01 00 00               jne 0x140a5b6e3
00A5B505  45 85 DB                        test r11d, r11d
00A5B508  0F 85 AD D4 FF FF               jne 0x140a589bb
00A5B50E  48 8D 8C 24 58 01 00 00         lea rcx, [rsp + 0x158]
00A5B516  E8 0D 29 DA FF                  call 0x1407fde28
00A5B51B  44 8B E0                        mov r12d, eax
00A5B51E  48 8B CE                        mov rcx, rsi
00A5B521  8B C6                           mov eax, esi
00A5B523  48 8B 94 24 58 01 00 00         mov rdx, qword ptr [rsp + 0x158]
00A5B52B  41 BD 04 00 00 C0               mov r13d, 0xc0000004
00A5B531  48 85 D2                        test rdx, rdx
00A5B534  74 2B                           je 0x140a5b561
00A5B536  48 8B 0A                        mov rcx, qword ptr [rdx]
00A5B539  48 B8 FF FF FF FF FF FF 0F 00   movabs rax, 0xfffffffffffff
00A5B543  48 23 C8                        and rcx, rax
00A5B546  48 81 F9 FF FF FF 1F            cmp rcx, 0x1fffffff
00A5B54D  76 07                           jbe 0x140a5b556
00A5B54F  45 8B E5                        mov r12d, r13d
00A5B552  8B C6                           mov eax, esi
00A5B554  EB 0B                           jmp 0x140a5b561
00A5B556  8D 04 CD 00 00 00 00            lea eax, [rcx*8]
00A5B55D  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00A5B561  44 3B F0                        cmp r14d, eax
00A5B564  45 0F 42 E5                     cmovb r12d, r13d
00A5B568  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00A5B56D  48 85 D2                        test rdx, rdx
00A5B570  0F 84 29 02 00 00               je 0x140a5b79f
00A5B576  45 85 E4                        test r12d, r12d
00A5B579  78 6D                           js 0x140a5b5e8
00A5B57B  81 FB 80 00 00 00               cmp ebx, 0x80
00A5B581  75 49                           jne 0x140a5b5cc
00A5B583  4C 8D 42 08                     lea r8, [rdx + 8]
00A5B587  49 8B C0                        mov rax, r8
00A5B58A  48 85 C9                        test rcx, rcx
00A5B58D  74 2F                           je 0x140a5b5be
00A5B58F  BB 01 00 00 00                  mov ebx, 1
00A5B594  4D 8B 08                        mov r9, qword ptr [r8]
00A5B597  49 0F BA E1 3E                  bt r9, 0x3e
00A5B59C  72 17                           jb 0x140a5b5b5
00A5B59E  49 BA FF FF FF FF FF FF FF 7F   movabs r10, 0x7fffffffffffffff
00A5B5A8  4D 23 CA                        and r9, r10
00A5B5AB  4D 89 08                        mov qword ptr [r8], r9
00A5B5AE  4C 89 08                        mov qword ptr [rax], r9
00A5B5B1  48 83 C0 08                     add rax, 8
00A5B5B5  49 83 C0 08                     add r8, 8
00A5B5B9  48 2B CB                        sub rcx, rbx
00A5B5BC  75 D6                           jne 0x140a5b594
00A5B5BE  48 2B C2                        sub rax, rdx
00A5B5C1  48 83 E8 08                     sub rax, 8
00A5B5C5  83 E0 F8                        and eax, 0xfffffff8
00A5B5C8  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00A5B5CC  44 8B 44 24 34                  mov r8d, dword ptr [rsp + 0x34]
00A5B5D1  48 83 C2 08                     add rdx, 8
00A5B5D5  48 8B CF                        mov rcx, rdi
00A5B5D8  E8 63 B2 C6 FF                  call 0x1406c6840
00A5B5DD  EB 09                           jmp 0x140a5b5e8
00A5B5DF  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5B5E3  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
00A5B5E8  33 D2                           xor edx, edx
00A5B5EA  48 8B 8C 24 58 01 00 00         mov rcx, qword ptr [rsp + 0x158]
00A5B5F2  E9 65 DF FF FF                  jmp 0x140a5955c
00A5B5F7  C7 44 24 34 10 00 00 00         mov dword ptr [rsp + 0x34], 0x10
00A5B5FF  41 83 FE 10                     cmp r14d, 0x10
00A5B603  0F 82 B2 D3 FF FF               jb 0x140a589bb
00A5B609  48 8D 8C 24 E0 01 00 00         lea rcx, [rsp + 0x1e0]
00A5B611  E8 AE DD CB FF                  call 0x1407193c4
00A5B616  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5B61A  85 C0                           test eax, eax
00A5B61C  79 0D                           jns 0x140a5b62b
00A5B61E  48 83 A4 24 E0 01 00 00 FE      and qword ptr [rsp + 0x1e0], 0xfffffffffffffffe
00A5B627  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00A5B62B  0F 28 84 24 E0 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x1e0]
00A5B633  F3 0F 7F 07                     movdqu xmmword ptr [rdi], xmm0
00A5B637  E9 63 01 00 00                  jmp 0x140a5b79f
00A5B63C  E9 7D 01 00 00                  jmp 0x140a5b7be
00A5B641  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A5B646  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5B64B  45 8B CE                        mov r9d, r14d
00A5B64E  4C 8B C7                        mov r8, rdi
00A5B651  41 8B D3                        mov edx, r11d
00A5B654  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A5B659  E8 76 A5 D7 FF                  call 0x1407d5bd4
00A5B65E  E9 10 01 00 00                  jmp 0x140a5b773
00A5B663  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A5B668  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5B66D  45 8B CE                        mov r9d, r14d
00A5B670  4C 8B C7                        mov r8, rdi
00A5B673  41 8B D3                        mov edx, r11d
00A5B676  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A5B67B  E8 08 A4 D7 FF                  call 0x1407d5a88
00A5B680  E9 EE 00 00 00                  jmp 0x140a5b773
00A5B685  80 7C 24 38 00                  cmp byte ptr [rsp + 0x38], 0
00A5B68A  0F 85 2C FB FF FF               jne 0x140a5b1bc
00A5B690  48 8B 15 99 39 4A 00            mov rdx, qword ptr [rip + 0x4a3999]
00A5B697  48 85 D2                        test rdx, rdx
00A5B69A  0F 84 35 FB FF FF               je 0x140a5b1d5
00A5B6A0  8B 42 04                        mov eax, dword ptr [rdx + 4]
00A5B6A3  8D 0C 40                        lea ecx, [rax + rax*2]
00A5B6A6  8D 0C CD 08 00 00 00            lea ecx, [rcx*8 + 8]
00A5B6AD  8B C1                           mov eax, ecx
00A5B6AF  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
00A5B6B3  44 3B F1                        cmp r14d, ecx
00A5B6B6  0F 82 FF D2 FF FF               jb 0x140a589bb
00A5B6BC  E9 8E FB FF FF                  jmp 0x140a5b24f
00A5B6C1  8B CB                           mov ecx, ebx
00A5B6C3  81 E9 FA 00 00 00               sub ecx, 0xfa
00A5B6C9  0F 84 AA 00 00 00               je 0x140a5b779
00A5B6CF  41 2B CC                        sub ecx, r12d
00A5B6D2  74 63                           je 0x140a5b737
00A5B6D4  83 E9 01                        sub ecx, 1
00A5B6D7  74 5E                           je 0x140a5b737
00A5B6D9  83 E9 01                        sub ecx, 1
00A5B6DC  74 32                           je 0x140a5b710
00A5B6DE  41 3B CC                        cmp ecx, r12d
00A5B6E1  74 0A                           je 0x140a5b6ed
00A5B6E3  B8 03 00 00 C0                  mov eax, 0xc0000003
00A5B6E8  E9 D1 00 00 00                  jmp 0x140a5b7be
00A5B6ED  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A5B6F2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A5B6F7  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00A5B6FC  4C 8B CF                        mov r9, rdi
00A5B6FF  45 8B C3                        mov r8d, r11d
00A5B702  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00A5B707  8B CB                           mov ecx, ebx
00A5B709  E8 6E F3 FE FF                  call 0x140a4aa7c
00A5B70E  EB 63                           jmp 0x140a5b773
00A5B710  8A 5C 24 38                     mov bl, byte ptr [rsp + 0x38]
00A5B714  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
00A5B718  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00A5B71D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A5B722  45 8B CE                        mov r9d, r14d
00A5B725  4C 8B C7                        mov r8, rdi
00A5B728  41 8B D3                        mov edx, r11d
00A5B72B  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A5B730  E8 AB 97 D6 FF                  call 0x1407c4ee0
00A5B735  EB 3C                           jmp 0x140a5b773
00A5B737  81 FB FD 00 00 00               cmp ebx, 0xfd
00A5B73D  75 1D                           jne 0x140a5b75c
00A5B73F  41 83 FE 0C                     cmp r14d, 0xc
00A5B743  73 17                           jae 0x140a5b75c
00A5B745  4D 85 FF                        test r15, r15
00A5B748  74 0B                           je 0x140a5b755
00A5B74A  41 C7 07 0C 00 00 00            mov dword ptr [r15], 0xc
00A5B751  EB 02                           jmp 0x140a5b755
00A5B753  EB 69                           jmp 0x140a5b7be
00A5B755  B8 04 00 00 C0                  mov eax, 0xc0000004
00A5B75A  EB 62                           jmp 0x140a5b7be
00A5B75C  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00A5B760  45 33 C9                        xor r9d, r9d
00A5B763  41 8B D6                        mov edx, r14d
00A5B766  48 8B CF                        mov rcx, rdi
00A5B769  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A5B76E  E8 05 F1 EB FF                  call 0x14091a878
00A5B773  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5B777  EB 26                           jmp 0x140a5b79f
00A5B779  C7 44 24 34 10 00 00 00         mov dword ptr [rsp + 0x34], 0x10
00A5B781  41 83 FE 10                     cmp r14d, 0x10
00A5B785  0F 82 30 D2 FF FF               jb 0x140a589bb
00A5B78B  41 F6 C6 07                     test r14b, 7
00A5B78F  0F 85 26 D2 FF FF               jne 0x140a589bb
00A5B795  0F 10 05 BC BC 56 00            movups xmm0, xmmword ptr [rip + 0x56bcbc]
00A5B79C  0F 11 07                        movups xmmword ptr [rdi], xmm0
00A5B79F  4D 85 FF                        test r15, r15
00A5B7A2  74 0D                           je 0x140a5b7b1
00A5B7A4  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
00A5B7A8  41 89 07                        mov dword ptr [r15], eax
00A5B7AB  EB 04                           jmp 0x140a5b7b1
00A5B7AD  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A5B7B1  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00A5B7B5  EB 07                           jmp 0x140a5b7be
00A5B7B7  EB 05                           jmp 0x140a5b7be
00A5B7B9  B8 0D 00 00 C0                  mov eax, 0xc000000d
00A5B7BE  48 8B 8C 24 A8 03 00 00         mov rcx, qword ptr [rsp + 0x3a8]
00A5B7C6  48 33 CC                        xor rcx, rsp
00A5B7C9  E8 72 0E C5 FF                  call 0x1406ac640
00A5B7CE  48 81 C4 B0 03 00 00            add rsp, 0x3b0
00A5B7D5  41 5F                           pop r15
00A5B7D7  41 5E                           pop r14
00A5B7D9  41 5D                           pop r13
00A5B7DB  41 5C                           pop r12
00A5B7DD  5F                              pop rdi
00A5B7DE  5E                              pop rsi
00A5B7DF  5B                              pop rbx
00A5B7E0  C3                              ret
00A5B7E1  CC                              int3
00A5B7E2  E8 E9 E7 E3 FF                  call 0x140899fd0
00A5B7E7  90                              nop
00A5B7E8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpQuerySystemInformation(int a1, __int64 a2, int a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m1CC;
    unsigned int v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int8 v_stack_m1EC;
    unsigned int v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int8 v_stack_m1FC;
    unsigned __int64 v_stack_m200;
    unsigned int v_stack_m204;
    unsigned __int8 v_stack_m206;
    unsigned __int8 v_stack_m207;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned int v_stack_m228;
    unsigned int v_stack_m230;
    unsigned int v_stack_m238;
    unsigned __int16 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int16 v_stack_m27E;
    unsigned __int16 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned int v_stack_m2AC;
    unsigned int v_stack_m2B0;
    unsigned int v_stack_m2B4;
    unsigned int v_stack_m2B8;
    unsigned int v_stack_m2BC;
    unsigned int v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned int v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int8 v_stack_m302;
    unsigned int v_stack_m368;
    unsigned __int16 v_stack_m370;
    unsigned __int64 v_stack_m378;
    unsigned int v_stack_m380;
    unsigned int v_stack_m384;
    unsigned __int8 v_stack_m388;
    unsigned int v_stack_m38C;
    unsigned int v_stack_m390;
    unsigned __int16 v_stack_m394;
    unsigned int v_stack_m398;
    unsigned __int64 v_stack_m3A0;
    unsigned int v_stack_m3A8;
    unsigned __int8 v_stack_m3A9;
    unsigned __int8 v_stack_m3AA;
    unsigned int v_stack_m3AC;
    unsigned __int8 v_stack_m3B0;
    unsigned int v_stack_m3B4;
    unsigned int v_stack_m3B8;
    unsigned __int64 v_stack_m3C0;
    unsigned __int64 v_stack_m3C8;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m58;

    v_rsp = (v_rsp) - (944);
    result = (*(unsigned __int64 *)(v_rip + 3878604)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m390 = a3;
    v_stack_m3A0 = a2;
    v_stack_m378 = a6;
    v_rsi = 0;
    v_stack_m398 = 0;
    *(unsigned __int64 *)(v_rsp - 624) = 0;
    v_stack_m2BC = 0;
    v_stack_m2B8 = 0;
    v_stack_m3A8 = 0;
    v_stack_m2AC = 0;
    v_stack_m370 = 0;
    v_stack_m394 = 0;
    v_stack_m248 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 712) = 0;
    v_stack_m3AC = 0;
    *(unsigned __int64 *)(v_rsp - 656) = 0;
    *(unsigned __int64 *)(v_rsp - 680) = 0;
    v_stack_m2B0 = 0;
    v_stack_m38C = 0;
    *(unsigned __int64 *)(v_rsp - 600) = 0;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 72) = 0;
    a2 = 0;
    result = memset(v_rsp - 520, a2, 432, a4);
    v_stack_m3B8 = 0;
    v_stack_m3B0 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00A57AC2;
    if (((unsigned int)((unsigned int)(a1))) > 157) goto loc_00A579F4;
    if (((unsigned int)((unsigned int)(a1))) == 157) goto loc_00A57A7C;
    if (((unsigned int)((unsigned int)(a1))) > 126) goto loc_00A579A8;
    if (((unsigned int)((unsigned int)(a1))) == 126) goto loc_00A57A7C;
    if (((unsigned int)((unsigned int)(a1))) == 5) goto loc_00A57A7C;
    if (((unsigned int)((unsigned int)(a1))) == 12) goto loc_00A57999;
    if (((unsigned int)((unsigned int)(a1))) == 17) goto loc_00A57A7C;
    if (((unsigned int)((unsigned int)(a1))) != 35) goto loc_00A57A7C;
loc_00A57985:
loc_00A5798B:
    goto loc_00A57A8E;
loc_00A57999:
    goto loc_00A57A88;
loc_00A579A8:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (133));
    if (condition_is_equal) goto loc_00A57A7C;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_00A57A7C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A57A7C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A57A82;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_00A5798B;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00A5798B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A57A82;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5798B;
    goto loc_00A57A82;
loc_00A579F4:
    if (((unsigned int)((unsigned int)(a1))) > 202) goto loc_00A57A45;
    if (((unsigned int)((unsigned int)(a1))) == 202) goto loc_00A5798B;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (158));
    if (condition_is_equal) goto loc_00A5798B;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00A57A82;
    a1 = (unsigned int)((a1) - ((unsigned int)(2 + 1)));
    if (condition_is_equal) goto loc_00A5798B;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_00A5798B;
    a1 = (unsigned int)((a1) - (4));
    if (condition_is_equal) goto loc_00A57A82;
    a1 = (unsigned int)((a1) - (15));
    if (condition_is_equal) goto loc_00A57A82;
    a1 = (unsigned int)((a1) - (4));
    if (condition_is_equal) goto loc_00A57A82;
    a1 = (unsigned int)((a1) - ((unsigned int)(2 + 1)));
    if (condition_is_equal) goto loc_00A57A82;
    goto loc_00A57A82;
loc_00A57A45:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (210));
    if (condition_is_equal) goto loc_00A57A7C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A57A7C;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_00A57A7C;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_00A57A7C;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_00A57985;
    a1 = (unsigned int)((a1) - (16));
    if (condition_is_equal) goto loc_00A57A82;
    a1 = (unsigned int)((a1) - (7));
    if (condition_is_equal) goto loc_00A57A82;
    a1 = (unsigned int)((a1) - (2));
    goto loc_00A57A82;
loc_00A57A7C:
loc_00A57A82:
loc_00A57A88:
loc_00A57A8E:
    result = ProbeForWrite(a4, (unsigned int)(a5), 4, a4);
    if (a6 != 0) {
        a1 = v_rsp;
        if (a6 < v_rsp) { a1 = a6; }
        result = *(unsigned int *)(a1);
        *(unsigned int *)(a1) = (unsigned int)(result);
    }
    goto loc_00A57ACF;
loc_00A57AC2:
loc_00A57ACF:
    v_stack_m3B4 = 0;
    v_stack_m2D0 = (unsigned int)((unsigned int)(0xFFFFULL));
    v_stack_m384 = 0;
    v_stack_m380 = 0;
    v_stack_m394 = 0;
    v_stack_m370 = 0;
    v_stack_m2A0 = 0;
    v_stack_m298 = 0;
    v_stack_m268 = 0;
    v_stack_m368 = 9;
    v_stack_m2B0 = 9;
    if (((unsigned int)((unsigned int)(a1))) > 100) goto loc_00A57BF6;
    if (((unsigned int)((unsigned int)(a1))) == 100) goto loc_00A57C64;
    if (((unsigned int)((unsigned int)(a1))) > 42) goto loc_00A57B73;
    if (((unsigned int)((unsigned int)(a1))) == 42) goto loc_00A57C64;
    if (((unsigned int)((unsigned int)(a1))) == ((unsigned int)(3 - 1))) goto loc_00A57BC0;
    if (((unsigned int)((unsigned int)(a1))) == 8) goto loc_00A57C64;
    if (((unsigned int)((unsigned int)(a1))) == 23) goto loc_00A57C64;
    if (((unsigned int)((unsigned int)(a1))) == 33) goto loc_00A57BC0;
    if (((unsigned int)((unsigned int)(a1))) == 36) goto loc_00A57BC0;
loc_00A57B64:
loc_00A57B69:
loc_00A57B6E:
    goto loc_00A57DA7;
loc_00A57B73:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (61));
    if (condition_is_equal) goto loc_00A57C64;
    a1 = (unsigned int)((a1) - (4));
    if (condition_is_equal) goto loc_00A57BC0;
    a1 = (unsigned int)((a1) - (7));
    if (condition_is_equal) goto loc_00A57B99;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A57C64;
    goto loc_00A57C26;
loc_00A57B99:
    if (((unsigned int)((unsigned int)(v_stack_m390))) != 4) goto loc_00A5B7B9;
    v_stack_m2B0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m3A0)));
    goto loc_00A57DA7;
loc_00A57BC0:
    v_stack_m380 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m390))));
    v_stack_m394 = (unsigned __int16)((unsigned int)((unsigned int)((unsigned int)(v_stack_m390))));
loc_00A57BCC:
    result = KeQueryActiveProcessorCountEx((unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), (unsigned int)(*(unsigned int *)(v_stack_m3A0)), 0, 0);
    v_stack_m384 = (unsigned int)(result);
    goto loc_00A57DA7;
loc_00A57BF6:
    if (((unsigned int)((unsigned int)(a1))) > 165) goto loc_00A57D01;
    if (((unsigned int)((unsigned int)(a1))) == 165) goto loc_00A57CC6;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (107));
    if (condition_is_equal) goto loc_00A57C9F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A57C64;
    a1 = (unsigned int)((a1) - (13));
    if (condition_is_equal) goto loc_00A57C2D;
    a1 = (unsigned int)((a1) - (20));
    if (condition_is_equal) goto loc_00A57C64;
loc_00A57C26:
    if (a1 == 19) goto loc_00A57C64;
    goto loc_00A57B64;
loc_00A57C2D:
    if (((unsigned int)((unsigned int)(v_stack_m390))) < ((unsigned int)(3 - 1))) goto loc_00A5B7B9;
    v_stack_m370 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m3A0));
    if (v_stack_m370 >= ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 5690289)))) goto loc_00A5B7B9;
    goto loc_00A57DA7;
loc_00A57C64:
    if (((unsigned int)((unsigned int)(v_stack_m390))) < ((unsigned int)(3 - 1))) goto loc_00A5B7B9;
    v_stack_m380 = (unsigned int)(*(unsigned __int16 *)(v_stack_m3A0));
    v_stack_m394 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m3A0));
    result = KeQueryActiveGroupCount(v_stack_m3A0, (unsigned int)(v_stack_m368), 0, (unsigned int)((unsigned int)(result)));
    if (((unsigned __int16)((unsigned int)(v_stack_m380))) >= ((unsigned __int16)(result))) goto loc_00A5B7B9;
    goto loc_00A57BCC;
loc_00A57C9F:
    if (((unsigned int)((unsigned int)(v_stack_m390))) < 4) goto loc_00A5B7B9;
    v_stack_m2D0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m3A0)));
    goto loc_00A57DA7;
loc_00A57CC6:
    if ((unsigned int)((unsigned int)(v_stack_m390)) == 0) goto loc_00A57CF4;
    if (((unsigned int)((unsigned int)(v_stack_m390))) != 8) goto loc_00A5B7B9;
    v_stack_m2A0 = *(unsigned __int64 *)(v_stack_m3A0);
    goto loc_00A57B6E;
loc_00A57CF4:
    v_stack_m2A0 = 0;
    goto loc_00A57B69;
loc_00A57D01:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (175));
    if (condition_is_equal) goto loc_00A57D81;
    a2 = (unsigned int)((a2) - ((unsigned int)(v_stack_m3A0)));
    if (condition_is_equal) goto loc_00A57D5B;
    a2 = (unsigned int)((a2) - ((unsigned int)(v_stack_m3A0)));
    if (condition_is_equal) goto loc_00A57D81;
    a2 = (unsigned int)((a2) - (49));
    if (condition_is_equal) goto loc_00A57D81;
    if (((unsigned int)(a2)) != 1) goto loc_00A57D4F;
    if (((unsigned int)((unsigned int)(v_stack_m390))) < 8) goto loc_00A5B7B9;
    v_stack_m3AC = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m3A0 + 4)));
    v_stack_m2D0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m3A0)));
loc_00A57D41:
    goto loc_00A57DA7;
loc_00A57D4F:
    goto loc_00A57B69;
loc_00A57D5B:
    if (((unsigned int)((unsigned int)(v_stack_m390))) != 8) goto loc_00A5B7B9;
    v_stack_m268 = *(unsigned __int64 *)(v_stack_m3A0);
    goto loc_00A57D41;
loc_00A57D81:
    if (((unsigned int)((unsigned int)(v_stack_m390))) != 8) goto loc_00A5B7B9;
    v_stack_m298 = *(unsigned __int64 *)(v_stack_m3A0);
loc_00A57DA7:
    if (((unsigned int)((unsigned int)(a1))) > 126) goto loc_00A59BC5;
    if (((unsigned int)((unsigned int)(a1))) == 126) goto loc_00A59B55;
    if (((unsigned int)((unsigned int)(a1))) > 64) goto loc_00A58BA1;
    if (((unsigned int)((unsigned int)(a1))) == 64) goto loc_00A58B3D;
    if (((unsigned int)((unsigned int)(a1))) > 25) goto loc_00A58300;
    if (((unsigned int)((unsigned int)(a1))) == 25) goto loc_00A59177;
    if (((unsigned int)((unsigned int)(a1))) > 12) goto loc_00A580A5;
    if (((unsigned int)((unsigned int)(a1))) == 12) goto loc_00A58051;
    if (((unsigned int)((unsigned int)(a1))) > 6) goto loc_00A57F4C;
    if (((unsigned int)((unsigned int)(a1))) == 6) goto loc_00A5AE6D;
    if ((unsigned int)((unsigned int)(a1)) == 0) goto loc_00A59732;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) - (1));
    if (condition_is_equal) goto loc_00A57F13;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00A57EC6;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00A57E28;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00A59177;
    goto loc_00A5880F;
loc_00A57E28:
    if (((unsigned int)((unsigned int)(a5))) <= 48) goto loc_00A57E49;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 48;
    goto loc_00A5B755;
loc_00A57E49:
    result = KeQueryBootTimeValues(v_stack_m200, v_stack_m208, v_stack_m1E8, (unsigned int)((unsigned int)(result)));
    result = PsGetCurrentServerSiloGlobals(v_stack_m200, v_stack_m208, v_stack_m1E8, (unsigned int)((unsigned int)(result)));
    v_stack_m1F8 = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1224) + 440);
    v_stack_m1F0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 432)));
    v_stack_m1E0 = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 1224) + 432)));
    result = memcpy(a4, v_stack_m208, (unsigned int)(a5), (unsigned int)((unsigned int)(result)));
loc_00A57EB7:
    v_stack_m3B4 = (unsigned int)((unsigned int)(a5));
    goto loc_00A5B79F;
loc_00A57EC6:
    if (((unsigned int)((unsigned int)(a5))) >= 312) goto loc_00A57EEA;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 376;
    goto loc_00A5B755;
loc_00A57EEA:
    v_rbx = 376;
    if (((unsigned int)((unsigned int)(a5))) <= 376) { v_rbx = (unsigned int)((unsigned int)(a5)); }
    result = ExpQuerySystemPerformanceInformation((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(result)));
    v_stack_m3B4 = (unsigned int)(v_rbx);
    goto loc_00A5B79F;
loc_00A57F13:
    if (((unsigned int)((unsigned int)(a5))) >= 12) goto loc_00A57F33;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 12;
    goto loc_00A5B755;
loc_00A57F33:
    result = ExpGetSystemProcessorInformation(a4, a4, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(result)));
loc_00A57F3B:
    v_stack_m3B8 = (unsigned int)(result);
    v_stack_m3B4 = 12;
    goto loc_00A5B79F;
loc_00A57F4C:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (7));
    if (condition_is_equal) goto loc_00A57FED;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A59D6C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A57FB3;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A59177;
    if (a1 != 1) goto loc_00A5B6E3;
    result = ExIsRestrictedCaller(v_stack_m3B0, v_stack_m38C, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(result)));
    if ((unsigned int)(result) != 0) goto loc_00A597E9;
    result = ExpQueryModuleInformation((unsigned int)(v_stack_m38C), a4, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m3B4);
    a2 = 0;
loc_00A57FA3:
    v_stack_m3B8 = (unsigned int)(result);
    result = EtwTiLogSyscallUsage((unsigned int)((unsigned int)(result)), a2, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m3B4);
    goto loc_00A5B79F;
loc_00A57FB3:
    if (((unsigned int)((unsigned int)(a5))) == 4) goto loc_00A57FD3;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 4;
    goto loc_00A5B755;
loc_00A57FD3:
    *(unsigned int *)(a4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5685991)));
loc_00A57FDB:
    v_stack_m3B4 = 4;
    goto loc_00A5B79F;
loc_00A57FED:
    if (((unsigned int)((unsigned int)(a5))) == 24) goto loc_00A5800D;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 24;
    goto loc_00A5B755;
loc_00A5800D:
    *(unsigned int *)(a4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5769253)));
    *(unsigned int *)(a4 + 4) = (unsigned int)(*(unsigned __int64 *)(v_rip + 5769248));
    *(unsigned int *)(a4 + 8) = (unsigned int)(*(unsigned __int64 *)(v_rip + 5769242));
    *(unsigned int *)(a4 + 12) = (unsigned int)(*(unsigned __int64 *)(v_rip + 5769236));
    *(unsigned int *)(a4 + 16) = (unsigned int)(*(unsigned __int64 *)(v_rip + 5769234));
    *(unsigned int *)(a4 + 20) = (unsigned int)(*(unsigned __int64 *)(v_rip + 5769228));
    goto loc_00A5ABF6;
loc_00A58051:
    if (((unsigned int)((unsigned int)(a5))) >= 56) goto loc_00A58071;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 56;
    goto loc_00A5B755;
loc_00A58071:
    result = ExIsRestrictedCaller(v_stack_m3B0, v_stack_m38C, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m3B4);
    if ((unsigned int)(result) != 0) goto loc_00A597E9;
    result = ExpGetLockInformation((unsigned int)(v_stack_m38C), a4, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m3B4);
    goto loc_00A57FA3;
loc_00A580A5:
    if (((unsigned int)(v_rbx)) > 18) goto loc_00A581A2;
    if (((unsigned int)(v_rbx)) == 18) goto loc_00A58198;
    v_rbx = (unsigned int)((v_rbx) - (13));
    if (condition_is_equal) goto loc_00A5818B;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5818B;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5818B;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5812C;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A5B6E3;
    if (((unsigned int)((unsigned int)(a5))) >= ((unsigned int)((unsigned int)(v_stack_m38C)))) goto loc_00A580F8;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(v_stack_m38C));
    goto loc_00A5B755;
loc_00A580F8:
    result = ExIsRestrictedCaller(v_stack_m3B0, v_stack_m38C, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m3B4);
    if ((unsigned int)(result) != 0) goto loc_00A597E9;
    result = ExpGetObjectInformation((unsigned int)(v_stack_m38C), a4, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m3B4);
    goto loc_00A57FA3;
loc_00A5812C:
    if (((unsigned int)((unsigned int)(a5))) >= 32) goto loc_00A5814D;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 32;
    goto loc_00A5B755;
loc_00A5814D:
    if ((((unsigned __int8)(a4)) & (7)) != 0) goto loc_00A58B63;
    result = ExIsRestrictedCaller(v_stack_m3B0, v_stack_m38C, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m3B4);
    if ((unsigned int)(result) != 0) goto loc_00A597E9;
    result = ExpGetHandleInformation((unsigned int)(v_stack_m38C), a4, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m3B4);
    goto loc_00A57FA3;
loc_00A5818B:
    v_stack_m3B8 = 0xC0000002ULL;
    goto loc_00A5B79F;
loc_00A58198:
    goto loc_00A59FAB;
loc_00A581A2:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (19));
    if (condition_is_equal) goto loc_00A5818B;
    a2 = (unsigned int)((a2) - (32));
    if (condition_is_equal) goto loc_00A59854;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00A582CA;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00A5821F;
    if (((unsigned int)(a2)) != 1) goto loc_00A5B6E3;
    if (((unsigned int)((unsigned int)(a5))) == 20) goto loc_00A581E9;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 20;
    goto loc_00A5B755;
loc_00A581E9:
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5689041)));
    *(unsigned int *)(a4 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5689072)));
    *(unsigned int *)(a4 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5689027)));
    *(unsigned int *)(a4 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5689238)));
loc_00A5820D:
    v_stack_m3B4 = 20;
    goto loc_00A5B79F;
loc_00A5821F:
    result = (unsigned int)((v_stack_m3B4 + v_stack_m3B4 * 2) << (3));
    v_stack_m3B4 = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(a5))) >= ((unsigned int)(result))) goto loc_00A58245;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = (unsigned int)(result);
    goto loc_00A5B755;
loc_00A58245:
    v_stack_m3A8 = 0;
loc_00A58253:
    v_stack_m2D8 = a4;
    if (0 >= ((unsigned int)(v_stack_m3B4))) goto loc_00A5869E;
    v_stack_m3AC = (unsigned __int16)(v_stack_m3A0);
    v_stack_m3AA = 0;
    v_stack_m3A9 = 0;
    result = KeGetProcessorIndexFromNumber(v_stack_m3AC, a2, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m3B4);
    *(unsigned int *)(a4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5704173 + (unsigned int)((unsigned int)(result)) * 8) + 11580)));
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5704173 + (unsigned int)((unsigned int)(result)) * 8) + 14428)));
    *(unsigned int *)(a4 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5704173 + (unsigned int)((unsigned int)(result)) * 8) + 14508)));
    *(unsigned int *)(a4 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5695704)));
    *(unsigned int *)(a4 + 16) = 0;
    *(unsigned int *)(a4 + 20) = 0;
    v_rdi = (a4) + (24);
    v_r14 = (unsigned int)((0) + ((unsigned int)(3 - 2)));
    v_stack_m3A8 = (unsigned int)(v_r14);
    goto loc_00A58253;
loc_00A582CA:
    if (((unsigned int)(v_r14)) >= 48) goto loc_00A582EB;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 48;
    goto loc_00A5B755;
loc_00A582EB:
    result = ExGetPoolTagInfo(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4, (unsigned int)(v_stack_m384));
    goto loc_00A5B773;
loc_00A58300:
    if (((unsigned int)(v_rip + 5704173)) > 50) goto loc_00A587E3;
    if (((unsigned int)(v_rip + 5704173)) == 50) goto loc_00A587AC;
    if (((unsigned int)(v_rip + 5704173)) > 36) goto loc_00A5854D;
    if (((unsigned int)(v_rip + 5704173)) == 36) goto loc_00A58495;
    v_rbx = (unsigned int)((v_rip + 5704173) - (28));
    if (condition_is_equal) goto loc_00A58407;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A59177;
    v_rbx = (unsigned int)((v_rbx) - (48));
    if (condition_is_equal) goto loc_00A583ED;
    v_rbx = (unsigned int)((v_rbx) - (48));
    if (condition_is_equal) goto loc_00A5837D;
    if (((unsigned int)(v_rbx)) != 48) goto loc_00A5B6E3;
    if (((unsigned int)(v_r14)) >= 48) goto loc_00A58362;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 48;
    goto loc_00A5B755;
loc_00A58362:
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 5173904));
    *(unsigned __int8 *)(v_rdi + 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 5173868));
    goto loc_00A59A32;
loc_00A5837D:
    if (((unsigned int)(v_r14)) >= 16) goto loc_00A5839D;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 16;
    goto loc_00A5B755;
loc_00A5839D:
    v_stack_m3B4 = 16;
    if ((unsigned int)((unsigned int)(v_stack_m384)) == 0) goto loc_00A583D7;
    v_stack_m3A8 = (unsigned int)((unsigned int)(v_stack_m384));
loc_00A583BE:
    a2 = (unsigned int)((0) + (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5703818) + 35768)));
    a3 = (unsigned int)((0) + (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5703818) + 34416)));
    v_r10 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m384)))) - (3 - 2);
    if (condition_is_not_equal) goto loc_00A583BE;
loc_00A583D7:
    *(unsigned int *)(v_rdi) = (unsigned int)(a2);
    *(unsigned int *)(v_rdi + 4) = a3;
    *(unsigned int *)(v_rdi + 8) = 0;
    *(unsigned int *)(v_rdi + 12) = 0;
    goto loc_00A5B79F;
loc_00A583ED:
    result = EtwQueryPerformanceTraceInformation(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B0, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A58407:
    if (((unsigned int)(v_r14)) == 12) goto loc_00A5842D;
    if (((unsigned int)(v_r14)) == 24) goto loc_00A5842D;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 12;
    goto loc_00A5B755;
loc_00A5842D:
    result = ExAcquireTimeRefreshLockShared(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B0, v_stack_m3B4);
    result = ExReleaseTimeRefreshLockShared(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B0, v_stack_m3B4);
    if (((unsigned int)(v_r14)) != 24) goto loc_00A58463;
    *(unsigned __int64 *)(v_rdi) = *(unsigned __int64 *)(v_rip + 5696567);
    *(unsigned __int64 *)(v_rdi + 8) = result;
    *(unsigned __int8 *)(v_rdi + 16) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 5688279));
    goto loc_00A5848B;
loc_00A58463:
    result = ((unsigned int)(*(unsigned int *)(v_rip + 5695031))) * (*(unsigned __int64 *)(v_rdi));
    a2 = 0;
    *(unsigned int *)(v_rdi) = (unsigned int)(result);
    *(unsigned int *)(v_rdi + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5695004)));
    *(unsigned __int8 *)(v_rdi + 8) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 5688279));
loc_00A5848B:
    goto loc_00A57EB7;
loc_00A58495:
    if (((unsigned int)(v_r14)) >= 48) goto loc_00A584B6;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 48;
    goto loc_00A5B755;
loc_00A584B6:
    if ((unsigned int)(v_stack_m3B4) == 0) goto loc_00A584DE;
    v_stack_m3A8 = (unsigned int)(v_stack_m3B4);
loc_00A584CC:
    a2 = (unsigned int)((0) + (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5703548) + 11580)));
    a3 = ((unsigned int)((unsigned int)(v_stack_m3B4))) - (3 - 2);
    if (condition_is_not_equal) goto loc_00A584CC;
loc_00A584DE:
    *(unsigned int *)(v_rdi) = (unsigned int)(a2);
    *(unsigned int *)(v_rdi + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5024986)));
    *(unsigned int *)(v_rdi + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5024985)));
    *(unsigned int *)(v_rdi + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5024972)));
    *(unsigned int *)(v_rdi + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5024971)));
    *(unsigned int *)(v_rdi + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5024966)));
    *(unsigned int *)(v_rdi + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5024965)));
    *(unsigned int *)(v_rdi + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5024952)));
    *(unsigned int *)(v_rdi + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5024951)));
    *(unsigned int *)(v_rdi + 36) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5024946)));
    *(unsigned int *)(v_rdi + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5024941)));
    *(unsigned int *)(v_rdi + 44) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5024936)));
    goto loc_00A59A32;
loc_00A5854D:
    v_rbx = (unsigned int)((*(unsigned __int64 *)(v_rip + 5696567)) - (37));
    if (condition_is_equal) goto loc_00A58773;
    v_rbx = (unsigned int)((v_rbx) - (5));
    if (condition_is_equal) goto loc_00A586E3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A586AC;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5858B;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A5B6E3;
    result = ExpGetLookasideInformation(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5858B:
    if (((unsigned int)(v_r14)) >= 172) goto loc_00A585AC;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 172;
    goto loc_00A5B755;
loc_00A585AC:
    result = PsGetCurrentServerSiloGlobals(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4, v_stack_m3B4);
    result = ExAcquireTimeRefreshLockShared(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4, v_stack_m3B4);
    *(unsigned __int64 *)(v_stack_m208) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m208 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m208 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m208 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m208 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m208 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m208 + 96) = v_xmm0;
    a1 = (v_stack_m208) + (128);
    *(unsigned __int64 *)(a1 - 16) = v_xmm0;
    v_rbx = (*(unsigned __int64 *)(result + 1224)) + (128);
    *(unsigned __int64 *)(a1) = v_xmm1;
    *(unsigned __int64 *)(a1 + 16) = v_xmm0;
    *(unsigned __int64 *)(a1 + 32) = *(unsigned __int64 *)(v_rbx + 32);
    *(unsigned int *)(a1 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 40)));
    result = ExReleaseTimeRefreshLockShared(a1, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4, v_stack_m3B4);
    *(unsigned __int64 *)(v_rdi) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 16) = v_xmm1;
    *(unsigned __int64 *)(v_rdi + 32) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 48) = v_xmm1;
    *(unsigned __int64 *)(v_rdi + 64) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 80) = v_xmm1;
    *(unsigned __int64 *)(v_rdi + 96) = v_xmm0;
    v_rdi = (v_rdi) + (128);
    *(unsigned __int64 *)(v_rdi - 16) = v_xmm1;
    a1 = (v_stack_m208) + (128);
    *(unsigned __int64 *)(v_rdi) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 16) = v_xmm1;
    *(unsigned __int64 *)(v_rdi + 32) = *(unsigned __int64 *)(a1 + 32);
    *(unsigned int *)(v_rdi + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)));
    v_stack_m3B4 = 172;
loc_00A5869E:
    v_stack_m3B8 = 0;
    goto loc_00A5B79F;
loc_00A586AC:
    if (128 >= 24) goto loc_00A586CC;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 24;
    goto loc_00A5B755;
loc_00A586CC:
    v_stack_m3B4 = 128;
    result = ExpQueryLegacyDriverInformation(v_rdi, v_stack_m3B4, v_stack_m3B4, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A586E3:
    result = (unsigned int)((v_stack_m3B4 + v_stack_m3B4 * 2) << (4));
    v_stack_m3B4 = (unsigned int)(result);
    if (128 < ((unsigned int)(result))) goto loc_00A589BB;
loc_00A586FF:
    v_stack_m3A8 = 0;
    v_stack_m2D8 = v_rdi;
    if (0 >= ((unsigned int)(v_stack_m3B4))) goto loc_00A5B79F;
    v_stack_m3AC = (unsigned __int16)(v_r10);
    v_stack_m3AA = 0;
    v_stack_m3A9 = 0;
    a3 = 0;
    result = PoGetIdleTimes(v_stack_m3AC, v_stack_m208, a3, v_stack_m3B4);
    *(unsigned __int64 *)(v_rdi) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 16) = v_xmm1;
    *(unsigned __int64 *)(v_rdi + 32) = v_xmm0;
    v_rdi = (v_rdi) + (48);
    v_rbx = (unsigned int)((0) + ((unsigned int)(3 - 2)));
    goto loc_00A586FF;
loc_00A58773:
    if (128 >= 16) goto loc_00A58793;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 16;
    goto loc_00A5B755;
loc_00A58793:
    result = CmQueryRegistryQuotaInformation(v_rdi, v_stack_m208, a3, (unsigned int)(v_stack_m384));
    v_stack_m3B8 = (unsigned int)(result);
    v_stack_m3B4 = 16;
    goto loc_00A5B79F;
loc_00A587AC:
    if (128 == 8) goto loc_00A587CC;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 8;
    goto loc_00A5B755;
loc_00A587CC:
    *(unsigned __int64 *)(v_rdi) = result;
    goto loc_00A5B0A7;
loc_00A587E3:
    if (((unsigned int)(v_rbx)) > 58) goto loc_00A58931;
    if (((unsigned int)(v_rbx)) == 58) goto loc_00A58900;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (51));
    if (condition_is_equal) goto loc_00A588BD;
    a1 = (unsigned int)((a1) - (48));
    if (condition_is_equal) goto loc_00A5884E;
    a1 = (unsigned int)((a1) - (48));
    if (condition_is_equal) goto loc_00A58839;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5881A;
loc_00A5880F:
    if (a1 == 1) goto loc_00A5B737;
    goto loc_00A5B6E3;
loc_00A5881A:
    v_stack_m3C8 = v_stack_m3B4;
    result = PfSnQueryPrefetcherInformation(a1, v_rdi, 128, v_stack_m3B0);
    goto loc_00A5B773;
loc_00A58839:
    result = ExpQueryNumaProcessorMap(v_rdi, 128, v_stack_m3B4, v_stack_m3B0);
    goto loc_00A5B773;
loc_00A5884E:
    if (128 >= 16) goto loc_00A5886E;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 16;
    goto loc_00A5B755;
loc_00A5886E:
    v_stack_m2AC = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)));
    v_stack_m220 = *(unsigned __int64 *)(v_rdi + 8);
    v_stack_m238 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 4)));
    result = ProbeForWrite(*(unsigned __int64 *)(v_rdi + 8), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 4)))), 4, v_stack_m3B0);
    v_stack_m3C8 = 5;
    goto loc_00A5B769;
loc_00A588BD:
    if (v_stack_m3B0 == 0) goto loc_00A5AE6D;
    if (128 >= 144) goto loc_00A588E8;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 144;
    goto loc_00A5B755;
loc_00A588E8:
    a4 = 0;
loc_00A588EB:
    result = VfGetVerifierInformation((unsigned int)(*(unsigned int *)(v_rdi + 4)), 128, v_stack_m3B4, a4);
    goto loc_00A5B773;
loc_00A58900:
    if (128 >= 4) goto loc_00A58920;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 4;
    goto loc_00A5B755;
loc_00A58920:
    result = KeGetRecommendedSharedDataAlignment((unsigned int)(*(unsigned int *)(v_rdi + 4)), 128, v_stack_m3B4, a4);
    *(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 4))) = (unsigned int)(result);
    goto loc_00A57FDB;
loc_00A58931:
    v_rbx = (unsigned int)((*(unsigned __int64 *)(v_rdi + 8)) - (59));
    if (condition_is_equal) goto loc_00A58AE8;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A58AD3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A589AB;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A58983;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A5B6E3;
    if (128 >= 12) goto loc_00A58976;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 12;
    goto loc_00A5B755;
loc_00A58976:
    result = ExpGetSystemEmulationProcessorInformation((unsigned int)(*(unsigned int *)(v_rdi + 4)), 128, v_stack_m3B4, a4);
    goto loc_00A57F3B;
loc_00A58983:
    if (128 == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 4))))) goto loc_00A5899E;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 4)));
    goto loc_00A5B755;
loc_00A5899E:
    result = ExpGetSystemEmulationBasicInformation((unsigned int)(*(unsigned int *)(v_rdi + 4)), 128, v_stack_m3B4, a4);
    goto loc_00A59755;
loc_00A589AB:
    result = (unsigned int)((a4 + a4 * 4) << (4));
    v_stack_m3B4 = (unsigned int)(result);
    if (128 >= ((unsigned int)(result))) goto loc_00A589CB;
loc_00A589BB:
    v_stack_m3B8 = (unsigned int)((unsigned int)(0xC0000004ULL));
    goto loc_00A5B79F;
loc_00A589CB:
    v_stack_m2D8 = (unsigned int)(*(unsigned int *)(v_rdi + 4));
    v_stack_m3A8 = 0;
loc_00A589E7:
    if (0 >= 0) goto loc_00A5B79F;
    v_stack_m3AC = (unsigned __int16)((unsigned int)(v_stack_m380));
    v_stack_m3AA = 0;
    v_stack_m3A9 = 0;
    result = KeGetProcessorIndexFromNumber(v_stack_m3AC, 128, v_stack_m3B4, a4);
    v_stack_m378 = *(unsigned __int64 *)(v_rip + 5702239 + (unsigned int)((unsigned int)(result)) * 8);
    a3 = 0;
    result = PoGetPerfStateAndParkingInfo(v_stack_m3AC, v_stack_m208, a3, v_stack_m270);
    a2 = 0;
    result = memset((unsigned int)(*(unsigned int *)(v_rdi + 4)), a2, 80, v_stack_m270);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m378 + 34376))) + (*(unsigned int *)(v_stack_m378 + 34372)));
    a1 = (a1) * ((unsigned int)(*(unsigned int *)(v_rip + 5693530)));
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rdi + 4)) + 40) = a1;
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m378 + 24) + 652))) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5693530)))));
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rdi + 4)) + 48) = a1;
    result = *(unsigned __int64 *)(v_stack_m378 + 24);
    if (v_stack_m1EC != 0) {
        result = v_stack_m200;
        *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_rdi + 4))) = (unsigned __int8)(result);
        result = v_stack_m1FC;
        *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_rdi + 4)) + 7) = (unsigned __int8)(result);
        result = v_stack_m1F8;
        *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_rdi + 4)) + 8) = (unsigned __int8)(result);
        *(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 4)) + 12) = (unsigned int)((unsigned int)(0xC0000004ULL));
    }
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rdi + 4)) + 72) = v_stack_m270;
    v_rdi = ((unsigned int)(*(unsigned int *)(v_rdi + 4))) + (80);
    v_stack_m2D8 = v_rdi;
    v_r12 = (unsigned int)((0) + ((unsigned int)((unsigned int)(0xC0000004ULL))));
    v_stack_m3A8 = (unsigned int)(v_r12);
    goto loc_00A589E7;
loc_00A58AD3:
    result = ExpQueryNumaAvailableMemory(v_rdi, 80, v_stack_m3B4, (unsigned int)(v_stack_m384));
    goto loc_00A5B773;
loc_00A58AE8:
    if (80 == 4) goto loc_00A58B08;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 4;
    goto loc_00A5B755;
loc_00A58B08:
    if ((*(unsigned int *)(result)) != -1) goto loc_00A58B28;
    result = ExpReadComPlusPackage(v_rdi, 80, v_stack_m3B4, (unsigned int)(v_stack_m384));
    v_stack_m3B8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A5B7BE;
loc_00A58B28:
    *(unsigned int *)(v_rdi) = (unsigned int)(result);
    goto loc_00A57FDB;
loc_00A58B3D:
    if (80 >= 56) goto loc_00A58B5D;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 56;
    goto loc_00A5B755;
loc_00A58B5D:
    if ((((unsigned __int8)(v_rdi)) & (7)) == 0) goto loc_00A58B6D;
loc_00A58B63:
    goto loc_00A5B7BE;
loc_00A58B6D:
    result = ExIsRestrictedCaller(v_stack_m3B0, v_stack_m38C, v_stack_m3B4, (unsigned int)(v_stack_m384));
    if ((unsigned int)(result) != 0) goto loc_00A597E9;
    result = ExpGetHandleInformationEx((unsigned int)(v_stack_m38C), v_rdi, 80, v_stack_m3B4);
    goto loc_00A57FA3;
loc_00A58BA1:
    if (((unsigned int)(v_rip + 5702239)) > 99) goto loc_00A591E6;
    if (((unsigned int)(v_rip + 5702239)) == 99) goto loc_00A591DC;
    if (((unsigned int)(v_rip + 5702239)) > 80) goto loc_00A58E33;
    if (((unsigned int)(v_rip + 5702239)) == 80) goto loc_00A58E15;
    if (((unsigned int)(v_rip + 5702239)) > 70) goto loc_00A58CE3;
    if (((unsigned int)(v_rip + 5702239)) == 70) goto loc_00A58CB1;
    v_rbx = (unsigned int)((v_rip + 5702239) - (65));
    if (condition_is_equal) goto loc_00A58C5D;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A58C08;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5B6E3;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5B6E3;
loc_00A58BF2:
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A5B6E3;
loc_00A58BFB:
    v_stack_m3B8 = 0xC00000BBULL;
    goto loc_00A5B79F;
loc_00A58C08:
    if (80 >= 32) goto loc_00A58C29;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 32;
    goto loc_00A5B755;
loc_00A58C29:
    result = ExIsRestrictedCaller(v_stack_m3B0, v_stack_m38C, 80, v_stack_m3B4);
    if ((unsigned int)(result) != 0) goto loc_00A597E9;
    result = ExGetBigPoolInfo((unsigned int)(v_stack_m38C), v_rdi, 80, v_stack_m3B4);
    goto loc_00A57FA3;
loc_00A58C5D:
    if (80 >= 4) goto loc_00A58C7D;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 4;
    goto loc_00A5B755;
loc_00A58C7D:
    if ((unsigned int)(v_stack_m3B4) == 0) goto loc_00A58CA5;
    v_stack_m3A8 = (unsigned int)(v_stack_m3B4);
loc_00A58C93:
    a2 = (unsigned int)((0) + (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5701557) + 34812)));
    a3 = ((unsigned int)((unsigned int)(v_stack_m3B4))) - ((unsigned int)(0xC0000004ULL));
    if (condition_is_not_equal) goto loc_00A58C93;
loc_00A58CA5:
    *(unsigned int *)(v_rdi) = (unsigned int)(a2);
    goto loc_00A57FDB;
loc_00A58CB1:
    if (80 == 4) goto loc_00A58CD1;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 4;
    goto loc_00A5B755;
loc_00A58CD1:
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3876525)));
    goto loc_00A57FDB;
loc_00A58CE3:
    v_rbx = (unsigned int)((v_rbx) - (72));
    if (condition_is_equal) goto loc_00A58DB7;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A58D95;
    v_rbx = (unsigned int)((v_rbx) - (3));
    if (condition_is_equal) goto loc_00A58D77;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A58D27;
    if (((unsigned int)(v_rbx)) != 32) goto loc_00A5B6E3;
    v_stack_m3C8 = v_stack_m3B4;
    result = PfQuerySuperfetchInformation(v_rip + 5701557 + 8, v_rdi, 80, v_stack_m3B0);
    goto loc_00A5B773;
loc_00A58D27:
    result = ExIsRestrictedCaller((unsigned __int8)(v_stack_m3B0), v_stack_m38C, 80, v_stack_m3B0);
    if ((unsigned int)(result) != 0) goto loc_00A597E9;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5770712), (unsigned __int8)(v_stack_m3B0), 80, v_stack_m3B0);
    a4 = ((unsigned __int8)(result) == 0) ? 1 : 0;
    v_stack_m3C8 = v_stack_m3B4;
    result = ExpQueryModuleInformationEx((unsigned int)(v_stack_m38C), v_rdi, 80, a4);
    goto loc_00A57FA3;
loc_00A58D77:
    result = ExpGetSystemFirmwareTableInformation(v_rdi, v_stack_m3B0, 80, v_stack_m3B4);
    goto loc_00A57FA3;
loc_00A58D95:
    result = KeBuildLogicalProcessorSystemInformation((unsigned __int16)((unsigned int)(v_stack_m380)), v_rdi, 80, v_stack_m3B4);
    v_stack_m3B8 = (unsigned int)(result);
    goto loc_00A5B79F;
loc_00A58DB7:
    if (80 != 8) goto loc_00A5B7B9;
    a2 = (unsigned int)((v_rdi) - (7));
    if (condition_is_equal) goto loc_00A58DEF;
    if (((unsigned int)(a2)) == 1) goto loc_00A58DD5;
    goto loc_00A5B7BE;
loc_00A58DD5:
    *(unsigned int *)(v_rdi) = 8;
    result = guard_dispatch_icall((unsigned __int16)((unsigned int)(v_stack_m380)), a2, 80, v_stack_m3B4);
    *(unsigned int *)(v_rdi + 4) = (unsigned int)((unsigned __int8)(result));
    goto loc_00A58E0B;
loc_00A58DEF:
    *(unsigned int *)(v_rdi) = 7;
    a1 = ((*(unsigned __int64 *)(v_rip + 3833139)) != (v_rip - 5621758)) ? 1 : 0;
    *(unsigned int *)(v_rdi + 4) = a1;
loc_00A58E0B:
    goto loc_00A5B0A7;
loc_00A58E15:
    v_stack_m3C8 = v_stack_m3B4;
    a1 = (a1) | (-1);
    result = MmQueryMemoryListInformation(a1, v_rdi, 80, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A58E33:
    if (((unsigned int)(v_stack_m3B0)) > 90) goto loc_00A5914C;
    if (((unsigned int)(v_stack_m3B0)) == 90) goto loc_00A590EC;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m3B0))) - (81));
    if (condition_is_equal) goto loc_00A59854;
    a2 = (unsigned int)((a2) - (32));
    if (condition_is_equal) goto loc_00A59029;
    a2 = (unsigned int)((a2) - (3));
    if (condition_is_equal) goto loc_00A59014;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00A58FE2;
    if (((unsigned int)(a2)) != 1) goto loc_00A5B6E3;
    result = 0;
    v_stack_m288 = v_xmm0;
    v_stack_m278 = 0;
    v_stack_m3B4 = 24;
    if (80 != 24) goto loc_00A589BB;
    v_stack_m288 = v_xmm0;
    v_stack_m278 = v_xmm1;
    if (v_stack_m280 != 0) goto loc_00A5B7B9;
    result = (v_stack_m280) >> (16);
    if ((((unsigned __int8)((unsigned int)(0xC0000004ULL))) & ((unsigned __int8)(result))) != 0) goto loc_00A5B7B9;
    if (v_stack_m3B0 == 0) goto loc_00A58F1E;
    if ((unsigned __int16)(result) == 0) goto loc_00A58F17;
    if (((v_stack_m278) & ((unsigned __int8)((unsigned int)(0xC0000004ULL)))) != 0) goto loc_00A5B7E2;
    a2 = (v_stack_m27E) + (v_stack_m278);
    if (a2 > result) goto loc_00A58F15;
    if (a2 < v_stack_m278) {
        result = *(unsigned __int8 *)(result);
    }
    goto loc_00A58F1E;
loc_00A58F1E:
    v_stack_m2C0 = (unsigned int)(v_stack_m27E);
    result = (v_stack_m27E) | (-1);
    result = PsLookupProcessByProcessId(v_stack_m288, v_stack_m2C8, 80, v_stack_m3B4);
    if (!sign_flag) goto loc_00A58F6E;
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m2C8, 80, v_stack_m3B4);
    goto loc_00A5B7BE;
loc_00A58F6E:
    result = PsQueryFullProcessImageName(v_stack_m2C8, v_rdi + 8, v_stack_m278, v_stack_m2C0);
    v_stack_m3B8 = (unsigned int)(result);
    result = ObfDereferenceObjectWithTag(v_stack_m2C8, (unsigned int)(0x746C6644ULL), v_stack_m278, v_stack_m2C0);
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x746C6644ULL), v_stack_m278, v_stack_m2C0);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)((unsigned int)(0xC0000004ULL)))) goto loc_00A5B79F;
    *(unsigned __int16 *)(v_rdi + 10) = (unsigned __int16)((unsigned int)(v_stack_m2C0));
    goto loc_00A5B79F;
loc_00A58FE2:
    v_stack_m3B4 = 8;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 8) goto loc_00A589BB;
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5692462)));
    a1 = ((*(unsigned int *)(v_rip + 5685536)) != 0) ? 1 : 0;
    *(unsigned int *)(v_rdi + 4) = a1;
    goto loc_00A5B79F;
loc_00A59014:
    result = ObQueryRefTraceInformation(v_rdi, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m3B4, v_stack_m2C0);
    goto loc_00A5B773;
loc_00A59029:
    a4 = (unsigned int)((v_stack_m2C0) << (3));
    v_stack_m3B4 = (unsigned int)(a4);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) < 8) goto loc_00A590DF;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) >= ((unsigned int)(a4))) goto loc_00A5904A;
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) >> (3));
    goto loc_00A5904F;
loc_00A5904A:
loc_00A5904F:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (0xC0000004ULL));
    v_stack_m2D8 = v_rdi;
    result = KeFlushProcessWriteBuffers(1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m3B4, a4);
loc_00A5907D:
    v_stack_m3A8 = 0;
    if (0 >= ((unsigned int)((unsigned int)(v_stack_m384)))) goto loc_00A590D5;
    v_stack_m3AC = (unsigned __int16)((unsigned int)(v_stack_m380));
    v_stack_m3AA = 0;
    v_stack_m3A9 = 0;
    result = KeGetProcessorIndexFromNumber(v_stack_m3AC, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m3B4, a4);
    *(unsigned __int64 *)(v_stack_m2D8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5700551 + (unsigned int)((unsigned int)(result)) * 8) + 24) + 72);
    result = (v_stack_m2D8) + (8);
    v_stack_m2D8 = result;
    result = (unsigned int)(((unsigned int)(v_stack_m3A8)) + (1));
    goto loc_00A5907D;
loc_00A590D5:
    v_stack_m3B8 = (unsigned int)(v_r14);
    goto loc_00A5B79F;
loc_00A590DF:
    v_stack_m3B8 = 0xC0000023ULL;
    goto loc_00A5B79F;
loc_00A590EC:
    v_stack_m3B4 = 32;
    if (((unsigned int)(v_r14)) >= 20) goto loc_00A59113;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 32;
    goto loc_00A5B755;
loc_00A59113:
    *(unsigned __int64 *)(v_rip + 5700551) = v_xmm0;
    *(unsigned int *)(v_rip + 5700551 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4874028)));
    if (((unsigned int)(v_r14)) < v_stack_m3B4) goto loc_00A5820D;
    *(unsigned __int64 *)(v_rip + 5700551 + 24) = *(unsigned __int64 *)(v_rip + 4874015);
    goto loc_00A5B79F;
loc_00A5914C:
    v_rbx = (unsigned int)((1) - (91));
    if (condition_is_equal) goto loc_00A591C7;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A59181;
    v_rbx = (unsigned int)((v_rbx) - (3));
    if (condition_is_equal) goto loc_00A5AE6D;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A59177;
    if (((unsigned int)(v_rbx)) != 32) goto loc_00A5B6E3;
    goto loc_00A5AE30;
loc_00A59177:
    goto loc_00A5B7BE;
loc_00A59181:
    if (v_stack_m3B0 == 0) goto loc_00A5AE6D;
    if (((unsigned int)(v_r14)) == 40) goto loc_00A591AD;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 40;
    goto loc_00A5B755;
loc_00A591AD:
    result = VfGetVerifierInformationEx(v_rip + 5700551, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m3B4, a4);
    v_stack_m3B8 = (unsigned int)(result);
    result = (unsigned int)((result) >> (31));
    result = (unsigned int)((result) & (0xFFFFFFD8ULL));
    result = (unsigned int)((result) + (40));
    goto loc_00A59EB4;
loc_00A591C7:
    result = HvlQueryEnlightenmentInfo(v_rip + 5700551, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A591DC:
    goto loc_00A5AE30;
loc_00A591E6:
    if (((unsigned int)(v_rbx)) > 114) goto loc_00A59766;
    if (((unsigned int)(v_rbx)) == 114) goto loc_00A59732;
    if (((unsigned int)(v_rbx)) > 106) goto loc_00A59573;
    if (((unsigned int)(v_rbx)) == 106) goto loc_00A59566;
    v_rbx = (unsigned int)((v_rbx) - (100));
    if (condition_is_equal) goto loc_00A5946E;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A59459;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5931F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5930A;
    if (((unsigned int)(v_rbx)) != 32) goto loc_00A5B6E3;
    a3 = 0;
    a2 = 0;
    result = guard_dispatch_icall(a2 + 23, a2, a3, v_stack_m398);
    v_stack_m3B8 = (unsigned int)(result);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000004ULL)))) goto loc_00A58BFB;
    if (((unsigned int)(v_r14)) < v_stack_m398) goto loc_00A59301;
    if (v_rip + 5700551 == 0) goto loc_00A59301;
    if ((unsigned __int8)(v_stack_m3B0) == 0) goto loc_00A5929F;
    result = ExAllocatePool2(257, (unsigned int)(v_stack_m398), (unsigned int)(0x6F666E49ULL), v_stack_m398);
    v_stack_m3A0 = result;
    if (result != 0) goto loc_00A592A7;
    goto loc_00A594F9;
loc_00A5929F:
    v_stack_m3A0 = v_rip + 5700551;
loc_00A592A7:
    result = guard_dispatch_icall(23, (unsigned int)(v_stack_m398), v_rip + 5700551, v_stack_m3B4);
    v_stack_m3B8 = (unsigned int)(result);
    if ((unsigned __int8)(v_stack_m3B0) == 0) goto loc_00A5B79F;
    if (sign_flag) goto loc_00A592F4;
    result = memcpy(v_rip + 5700551, v_rip + 5700551, (unsigned int)(v_stack_m3B4), v_stack_m3B4);
    goto loc_00A592F4;
loc_00A592F4:
    goto loc_00A5955C;
loc_00A59301:
    goto loc_00A59EB4;
loc_00A5930A:
    result = SeCodeIntegrityQueryInformation(v_rip + 5700551, (unsigned int)((unsigned int)(v_rip + 5700551)), v_stack_m3B4, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5931F:
    if (((unsigned int)(v_rip + 5700551)) >= 432) goto loc_00A59340;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 432;
    goto loc_00A5B755;
loc_00A59340:
    result = PsGetCurrentServerSiloGlobals(v_rip + 5700551, (unsigned int)((unsigned int)(v_rip + 5700551)), v_stack_m3B4, v_stack_m3B4);
    result = ExAcquireTimeRefreshLockShared(v_rip + 5700551, (unsigned int)((unsigned int)(v_rip + 5700551)), v_stack_m3B4, v_stack_m3B4);
loc_00A59366:
    *(unsigned __int64 *)(v_stack_m208) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m208 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m208 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m208 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m208 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m208 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m208 + 96) = v_xmm0;
    result = (v_stack_m208) + (3 + 125);
    *(unsigned __int64 *)(result - 16) = v_xmm1;
    v_r12 = (*(unsigned __int64 *)(result + 1224)) + (3 + 125);
    a1 = (3) - (1);
    if (condition_is_not_equal) goto loc_00A59366;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    result = ExReleaseTimeRefreshLockShared(a1, (unsigned int)((unsigned int)(v_rip + 5700551)), v_stack_m3B4, v_stack_m3B4);
loc_00A593EA:
    *(unsigned __int64 *)(v_rip + 5700551) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 5700551 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_rip + 5700551 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 5700551 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_rip + 5700551 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 5700551 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_rip + 5700551 + 96) = v_xmm0;
    v_rdi = (v_rip + 5700551) + (3 + 125);
    *(unsigned __int64 *)(v_rdi - 16) = v_xmm1;
    result = (v_stack_m208) + (3 + 125);
    v_r14 = (3) - (1);
    if (condition_is_not_equal) goto loc_00A593EA;
    *(unsigned __int64 *)(v_rdi) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 16) = v_xmm1;
    *(unsigned __int64 *)(v_rdi + 32) = v_xmm0;
    v_stack_m3B4 = 432;
    goto loc_00A5869E;
loc_00A59459:
    result = ExpQueryNumaProximityNode(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5946E:
    v_stack_m240 = (unsigned __int16)((unsigned int)(v_stack_m380));
    result = KeQueryGroupAffinity((unsigned __int16)((unsigned int)(v_stack_m380)), (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4, v_stack_m3B4);
    v_stack_m248 = result;
    v_stack_m368 = result;
    v_stack_m3C8 = v_stack_m398;
    a2 = 0;
    a1 = 0;
    result = PpmCapturePerformanceDistribution(a1, a2, (unsigned int)((unsigned int)(result)), v_stack_m248);
    v_stack_m3B8 = (unsigned int)(result);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000004ULL)))) goto loc_00A5B79F;
    if (((unsigned int)((unsigned int)(v_stack_m398))) <= ((unsigned int)(v_r14))) goto loc_00A594D9;
    v_stack_m3B8 = (unsigned int)((unsigned int)(0xC0000004ULL));
    goto loc_00A59EB4;
loc_00A594D9:
    result = ExAllocatePool2(64, (unsigned int)(v_stack_m398), (unsigned int)(0x744D5050ULL), v_stack_m248);
    v_stack_m3A0 = result;
    if (result != 0) goto loc_00A59506;
loc_00A594F9:
    v_stack_m3B8 = 0xC000009AULL;
    goto loc_00A5B79F;
loc_00A59506:
    v_stack_m3C8 = v_stack_m3B4;
    result = PpmCapturePerformanceDistribution(result, (unsigned int)(v_stack_m398), (unsigned int)(v_stack_m368), v_stack_m248);
    v_stack_m3B8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A59554;
    result = memcpy(v_rdi, result, (unsigned int)(v_stack_m3B4), v_stack_m248);
    goto loc_00A59554;
loc_00A59554:
loc_00A59559:
loc_00A5955C:
    result = ExFreePoolWithTag(result, (unsigned int)(0x744D5050ULL), (unsigned int)(v_stack_m3B4), v_stack_m248);
    goto loc_00A5B79F;
loc_00A59566:
    v_stack_m3B8 = 0xC0000003ULL;
    goto loc_00A5B79F;
loc_00A59573:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) - (107));
    if (condition_is_equal) goto loc_00A59690;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A595E4;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A595C5;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00A595B0;
    if (a1 != 1) goto loc_00A5B6E3;
    result = PsQueryCpuQuotaInformation(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B0, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A595B0:
    result = IoQueryVhdBootInformation(v_rdi, v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4);
    goto loc_00A5B773;
loc_00A595C5:
    v_stack_m3C8 = v_stack_m3B4;
    result = SmQueryStoreInformation(v_rdi, v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B0);
    goto loc_00A5B773;
loc_00A595E4:
    v_stack_m3B4 = (unsigned int)(v_stack_m3B0 * 8);
    if (((unsigned int)(v_r14)) < 8) goto loc_00A590DF;
    if (((unsigned int)(v_r14)) < ((unsigned int)(v_stack_m3B0 * 8))) {
        a4 = (unsigned int)(v_r14);
        a4 = (unsigned int)((a4) >> (3));
        v_stack_m384 = (unsigned int)(a4);
    }
    v_r14 = (unsigned int)((v_r14) & (0xC0000004ULL));
    v_stack_m2D8 = v_rdi;
loc_00A5962E:
    v_stack_m3A8 = 0;
    if (0 >= ((unsigned int)(a4))) goto loc_00A590D5;
    v_stack_m3AC = (unsigned __int16)((unsigned int)(v_stack_m380));
    v_stack_m3AA = 0;
    v_stack_m3A9 = 0;
    result = KeGetProcessorIndexFromNumber(v_stack_m3AC, v_rdi, (unsigned int)((unsigned int)(v_r14)), a4);
    *(unsigned __int64 *)(v_stack_m2D8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5699095 + (unsigned int)((unsigned int)(result)) * 8) + 34680);
    result = (v_stack_m2D8) + (8);
    v_stack_m2D8 = result;
    result = (unsigned int)(((unsigned int)(v_stack_m3A8)) + (1));
    goto loc_00A5962E;
loc_00A59690:
loc_00A59695:
    v_stack_m3A0 = v_stack_m208;
    v_stack_m398 = 80;
    result = 80;
    if (((unsigned int)(v_r14)) < 80) {
        result = (unsigned int)(v_r14);
        v_stack_m398 = (unsigned int)(result);
    }
    v_stack_m3B4 = (unsigned int)(result);
    result = v_stack_m3AC;
    if (1 != 231) { result = 0; }
    v_stack_m368 = result;
loc_00A596D9:
    result = KeQueryLogicalProcessorRelationship(result, (unsigned int)(v_stack_m2D0), v_stack_m3A0, v_stack_m3B4);
    v_stack_m3B8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A5B3BB;
    result = memcpy(v_rip + 5699095, v_stack_m3A0, (unsigned int)(v_stack_m3B4), v_stack_m3B4);
    v_stack_m3B8 = 0;
loc_00A59711:
    if (v_stack_m3A0 == 0) goto loc_00A5B79F;
    if (v_stack_m3A0 == v_stack_m208) goto loc_00A5B79F;
loc_00A5972B:
    a2 = 0;
    goto loc_00A59559;
loc_00A59732:
    if (((unsigned int)(v_r14)) == ((unsigned int)(v_rip + 5699095))) goto loc_00A5974D;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = (unsigned int)(v_rip + 5699095);
    goto loc_00A5B755;
loc_00A5974D:
    result = ExpGetSystemBasicInformation(v_rip + 5699095, a2, (unsigned int)(v_stack_m3B4), v_stack_m3B4);
loc_00A59755:
    v_stack_m3B8 = (unsigned int)(result);
loc_00A59759:
    v_stack_m3B4 = 64;
    goto loc_00A5B79F;
loc_00A59766:
    if (((unsigned int)(v_stack_m3A0)) > 120) goto loc_00A59910;
    if (((unsigned int)(v_stack_m3A0)) == 120) goto loc_00A59854;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m3A0))) - (115));
    if (condition_is_equal) goto loc_00A59815;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00A59800;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00A597D0;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00A5979D;
    if (((unsigned int)(a2)) == 1) goto loc_00A59854;
    goto loc_00A5B6E3;
loc_00A5979D:
    if (v_stack_m3B0 == 0) goto loc_00A5AE6D;
    if (((unsigned int)(v_r14)) >= 272) goto loc_00A597C8;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 272;
    goto loc_00A5B755;
loc_00A597C8:
    goto loc_00A588EB;
loc_00A597D0:
    v_stack_m3B4 = (unsigned int)((unsigned int)(0x448ULL));
    if (((unsigned int)(v_r14)) != ((unsigned int)((unsigned int)(0x448ULL)))) goto loc_00A589BB;
    if (v_stack_m3B0 == 0) goto loc_00A597F3;
loc_00A597E9:
    goto loc_00A5B7BE;
loc_00A597F3:
    result = ExQueryBootEntropyInformation(v_rip + 5699095, a2, (unsigned int)(v_stack_m3B4), (unsigned int)((unsigned int)((unsigned int)(0xC0000004ULL))));
    goto loc_00A5B773;
loc_00A59800:
    result = IoQueryLowPriorityIoInformation(v_rip + 5699095, v_rip + 5699095, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4);
    goto loc_00A5B773;
loc_00A59815:
    if ((unsigned int)((unsigned int)(v_stack_m390)) != 0) goto loc_00A589BB;
    v_stack_m3B4 = 8;
    if (((unsigned int)(v_r14)) < 8) goto loc_00A589BB;
    *(unsigned int *)(v_rip + 5699095) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5683622)));
    *(unsigned int *)(v_rip + 5699095 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5684042)));
    goto loc_00A5B79F;
loc_00A59854:
    if (((unsigned int)(v_r14)) >= ((unsigned int)(v_rip + 5699095))) goto loc_00A5986F;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = (unsigned int)(v_rip + 5699095);
    goto loc_00A5B755;
loc_00A5986F:
    result = (unsigned int)(*(unsigned int *)(v_rip + 5684042));
    v_r13 = (unsigned int)(0xC0000004ULL);
    if (((unsigned int)(v_stack_m3A0)) != 119) {
        result = 3;
        v_r13 = (unsigned int)(0xC0000004ULL);
        if (((unsigned int)(v_stack_m3A0)) == 120) { v_r13 = (unsigned int)(result); }
        v_r12 = (unsigned int)(v_r13);
    }
    result = MmQuerySystemWorkingSetInformation((unsigned int)((unsigned int)(v_r12)), v_stack_m208, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4);
    *(unsigned __int64 *)(v_rip + 5699095) = v_stack_m208;
    *(unsigned __int64 *)(v_rip + 5699095 + 8) = v_stack_m200;
    *(unsigned int *)(v_rip + 5699095 + 16) = (unsigned int)((unsigned int)(v_stack_m1F8));
    v_stack_m3A8 = 64;
    *(unsigned __int64 *)(v_rip + 5699095 + 24) = v_stack_m1F0;
    *(unsigned __int64 *)(v_rip + 5699095 + 32) = v_stack_m1E8;
    *(unsigned __int64 *)(v_rip + 5699095 + 40) = v_stack_m1E0;
    *(unsigned __int64 *)(v_rip + 5699095 + 48) = v_stack_m1D8;
    *(unsigned int *)(v_rip + 5699095 + 56) = (unsigned int)((unsigned int)(v_stack_m1D0));
    *(unsigned int *)(v_rip + 5699095 + 60) = (unsigned int)((unsigned int)(v_stack_m1CC));
    goto loc_00A59759;
loc_00A59910:
    v_rbx = (unsigned int)((v_stack_m3A0) - (121));
    if (condition_is_equal) goto loc_00A59AEB;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A59A41;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5998C;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A5B6E3;
    v_stack_m3B4 = 12;
    if (((unsigned int)(v_r14)) < 4) goto loc_00A589BB;
    v_stack_m230 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5699095)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5699095)))) != 1) goto loc_00A58BFB;
    if (((unsigned int)(v_r14)) < 12) goto loc_00A589BB;
    *(unsigned int *)(v_rip + 5699095 + 8) = 0;
    *(unsigned int *)(v_rip + 5699095 + 4) = 0;
    *(unsigned int *)(v_rip + 5699095 + 8) = (unsigned int)(v_r13);
    *(unsigned int *)(v_rip + 5699095 + 4) = (unsigned int)(v_r13);
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5699095))) != 0) {
    }
    goto loc_00A5B79F;
loc_00A5998C:
    if (((unsigned int)(v_r14)) == 32) goto loc_00A599AD;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 32;
    goto loc_00A5B755;
loc_00A599AD:
    result = MmGetProcessPartitionId(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_stack_m208, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4);
    result = MmGetAvailablePages((unsigned __int16)(result), v_stack_m208, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4);
    v_stack_m208 = result;
    result = MmGetTotalCommittedPages((unsigned __int16)(result), v_stack_m208, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4);
    v_stack_m200 = result;
    result = MmGetTotalCommitLimit((unsigned __int16)(result), v_stack_m208, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4);
    v_stack_m1F8 = result;
    result = MmGetPeakCommitment((unsigned __int16)(result), v_stack_m208, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4);
    v_stack_m1F0 = result;
    result = v_stack_m1F0;
    if (v_stack_m1F0 < v_stack_m200) { result = v_stack_m200; }
    v_stack_m1F0 = result;
    *(unsigned __int64 *)(v_rip + 5699095) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 5699095 + 16) = v_xmm1;
loc_00A59A32:
    v_stack_m3B4 = 32;
    goto loc_00A5B79F;
loc_00A59A41:
    v_stack_m3B4 = 8;
    if (((unsigned int)(v_r14)) != 8) goto loc_00A589BB;
    if (v_rip + 5699095 == 0) goto loc_00A589BB;
    result = ExAllocatePool2(257, (unsigned int)((unsigned int)(v_r14)), (unsigned int)(0x6F666E49ULL), v_stack_m3B4);
    v_stack_m3A0 = result;
    if (result == 0) goto loc_00A594F9;
    result = guard_dispatch_icall(v_r14 + 18, (unsigned int)((unsigned int)(v_r14)), result, v_stack_m3B4);
    v_stack_m3B8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A59AE1;
    *(unsigned int *)(v_rip + 5699095) = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5699095 + 4))))) ^ (*(unsigned int *)(result + 4)));
    a1 = (unsigned int)((a1) & ((unsigned int)(v_r13)));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5699095 + 4)))));
    *(unsigned int *)(v_rip + 5699095 + 4) = a1;
    a2 = (unsigned int)(((unsigned int)(a1)) ^ (*(unsigned int *)(result + 4)));
    a2 = (unsigned int)((a2) & (2));
    a2 = (unsigned int)((a2) ^ (a1));
    *(unsigned int *)(v_rip + 5699095 + 4) = (unsigned int)(a2);
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) ^ (*(unsigned int *)(result + 4)));
    result = (unsigned int)((result) & (4));
    result = (unsigned int)((result) ^ ((unsigned int)(a2)));
    *(unsigned int *)(v_rip + 5699095 + 4) = (unsigned int)(result);
    goto loc_00A59AE1;
loc_00A59AE1:
    goto loc_00A59559;
loc_00A59AEB:
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rip + 5682446)) << (2));
    v_stack_m3B4 = a1;
    if (((unsigned int)(v_r14)) < a1) goto loc_00A589BB;
    v_stack_m3A8 = 0;
loc_00A59B10:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 5682409)))) goto loc_00A59B4B;
    a1 = (unsigned int)((v_stack_m370) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 5682409))))));
    a1 = (unsigned int)((a1) + (0));
    *(unsigned int *)(v_rip + 5699095 + 0 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5682552) + a1 * 4)));
    v_stack_m3A8 = (unsigned int)(0 + 1);
    goto loc_00A59B10;
loc_00A59B4B:
    goto loc_00A5B79F;
loc_00A59B55:
    v_stack_m3B4 = 32;
    if (((unsigned int)(v_r14)) != 32) goto loc_00A589BB;
    a1 = 0;
    result = BgkQueryBootGraphicsInformation(a1, v_stack_m208, (unsigned int)((unsigned int)(0 + 1)), (unsigned int)((unsigned int)(0 + 1)));
    v_stack_m3B8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A5B79F;
    result = v_stack_m208;
    if (v_stack_m3B0 != 0) { result = 0; }
    v_stack_m208 = result;
    result = memcpy(v_rip + 5699095, v_stack_m208, (unsigned int)(v_stack_m3B4), (unsigned int)((unsigned int)(0 + 1)));
    goto loc_00A5B79F;
loc_00A59BC5:
    if (((unsigned int)(result)) > 189) goto loc_00A5AC36;
    if (((unsigned int)(result)) == 189) goto loc_00A5B6ED;
    if (((unsigned int)(result)) > 159) goto loc_00A5A32E;
    if (((unsigned int)(result)) == 159) goto loc_00A5A319;
    if (((unsigned int)(result)) > 144) goto loc_00A5A004;
    if (((unsigned int)(result)) == 144) goto loc_00A59FAB;
    if (((unsigned int)(result)) > 137) goto loc_00A59D27;
    if (((unsigned int)(result)) == 137) goto loc_00A59CF4;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) - (128));
    if (condition_is_equal) goto loc_00A5B505;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_00A59CC2;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A59CA1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A59C40;
    if (a1 == 1) goto loc_00A59CF4;
    goto loc_00A5B6E3;
loc_00A59C40:
    v_stack_m3B4 = 8;
    if (((unsigned int)(v_r14)) < 8) goto loc_00A589BB;
    a2 = 0;
    result = HvlQueryActiveProcessors(v_stack_m2BC, a2, (unsigned int)(v_stack_m3B4), (unsigned int)((unsigned int)(0 + 1)));
    if ((unsigned int)(result) != 0) goto loc_00A58BFB;
    a1 = 0;
    result = HvlQueryProcessorTopologyCount(a1, v_stack_m2B8, (unsigned int)(v_stack_m3B4), (unsigned int)((unsigned int)(0 + 1)));
    v_stack_m3B8 = (unsigned int)(result);
    if ((unsigned int)(result) != 0) goto loc_00A58BFB;
    *(unsigned int *)(v_rip + 5699095) = (unsigned int)((unsigned int)(v_stack_m2BC));
    *(unsigned int *)(v_rip + 5699095 + 4) = (unsigned int)((unsigned int)(v_stack_m2B8));
    goto loc_00A5B79F;
loc_00A59CA1:
    v_stack_m3B4 = 32;
    if (((unsigned int)(v_r14)) != 32) goto loc_00A589BB;
    result = sub_00A179B0(a1, v_rip + 5699095, (unsigned int)(v_stack_m3B4), (unsigned int)((unsigned int)(0 + 1)));
    goto loc_00A5B773;
loc_00A59CC2:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5766569), (unsigned __int8)(v_stack_m3B0), (unsigned int)(v_stack_m3B4), (unsigned int)((unsigned int)(0 + 1)));
    if ((unsigned __int8)(result) == 0) goto loc_00A5B210;
    result = ExpGetSystemPlatformBinary(v_rip + 5699095, (unsigned int)((unsigned int)(v_r14)), (unsigned __int8)(v_stack_m3B0), (unsigned int)((unsigned int)(0 + 1)));
    goto loc_00A57FA3;
loc_00A59CF4:
    if (((unsigned int)(v_r14)) == 48) goto loc_00A59D15;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 48;
    goto loc_00A5B755;
loc_00A59D15:
    result = ExpGetDeviceDataInformation((unsigned int)((unsigned int)(v_stack_m3B0)), v_rip + 5699095, 48, (unsigned int)((unsigned int)(0 + 1)));
    goto loc_00A5B7BE;
loc_00A59D27:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m3B0))) - (138));
    if (condition_is_equal) goto loc_00A59F91;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A59F77;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A59ED7;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A59D6C;
    if (a1 != 48) goto loc_00A5B6E3;
loc_00A59D55:
    result = SeSecureBootQueryInformation((unsigned int)((unsigned int)(v_stack_m3B0)), v_rip + 5699095, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4);
    goto loc_00A5B773;
loc_00A59D6C:
    v_r12 = 48;
    if (((unsigned int)(v_stack_m3B0)) != 8) { v_r12 = (unsigned int)(48 + 24); }
    if ((unsigned int)(v_r14) == 0) goto loc_00A59EBD;
    a2 = 0;
    if (0 != 0) goto loc_00A59EBD;
    v_stack_m368 = 0;
loc_00A59DA0:
    v_stack_m3A8 = 0;
    v_stack_m2D8 = v_rip + 5699095;
    if (0 >= ((unsigned int)(v_stack_m3B4))) goto loc_00A59EAD;
    v_stack_m3AC = (unsigned __int16)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 5682409))));
    v_stack_m3AA = 0;
    v_stack_m3A9 = 0;
    result = KeGetProcessorIndexFromNumber(v_stack_m3AC, a2, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4);
    v_stack_m378 = *(unsigned __int64 *)(v_rip + 5697129 + (unsigned int)((unsigned int)(result)) * 8);
    if (((unsigned int)(v_r14)) < ((unsigned int)(v_r12 + (unsigned int)(v_stack_m368) * 1))) goto loc_00A59EB4;
    v_stack_m368 = (unsigned int)(v_r12 + (unsigned int)(v_stack_m368) * 1);
    a2 = 0;
    result = PoGetIdleTimes(v_stack_m3AC, a2, v_stack_m208, v_stack_m3B4);
    result = ((unsigned int)(*(unsigned int *)(v_stack_m378 + 34376))) * ((unsigned int)(*(unsigned int *)(v_rip + 5688458)));
    *(unsigned __int64 *)(v_rip + 5699095 + 16) = result;
    result = ((unsigned int)(v_stack_m204)) * ((unsigned int)(*(unsigned int *)(v_rip + 5688458)));
    *(unsigned __int64 *)(v_rip + 5699095 + 8) = result;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m378 + 34380))) * ((unsigned int)(*(unsigned int *)(v_rip + 5688458)));
    *(unsigned __int64 *)(v_rip + 5699095 + 24) = result;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m378 + 34384))) * ((unsigned int)(*(unsigned int *)(v_rip + 5688458)));
    *(unsigned __int64 *)(v_rip + 5699095 + 32) = result;
    result = ((unsigned int)(v_stack_m208)) * ((unsigned int)(*(unsigned int *)(v_rip + 5688458)));
    *(unsigned __int64 *)(v_rip + 5699095) = result;
    *(unsigned int *)(v_rip + 5699095 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m378 + 34368)));
    result = (unsigned int)(*(unsigned int *)(v_stack_m378 + 34368));
    if (((unsigned int)(v_stack_m3B0)) == 141) {
        result = *(unsigned int *)(v_stack_m378 + 34412);
        result = (result) * ((unsigned int)(*(unsigned int *)(v_rip + 5688458)));
        *(unsigned __int64 *)(v_rip + 5699095 + 48) = result;
        *(unsigned int *)(v_rip + 5699095 + 44) = 0;
        *(unsigned __int64 *)(v_rip + 5699095 + 56) = 0;
        *(unsigned __int64 *)(v_rip + 5699095 + 64) = 0;
    }
    v_rdi = (v_rip + 5699095) + ((unsigned int)((unsigned int)(v_r12)));
    result = (unsigned int)(((unsigned int)(v_stack_m3A8)) + ((unsigned int)(v_r13)));
    goto loc_00A59DA0;
loc_00A59EAD:
loc_00A59EB4:
    v_stack_m3B4 = (unsigned int)((unsigned int)(v_stack_m368));
    goto loc_00A5B79F;
loc_00A59EBD:
    if (a6 == 0) goto loc_00A5B755;
    v_r12 = (unsigned int)((v_r12) * ((unsigned int)((unsigned int)(v_stack_m384))));
    *(unsigned int *)(a6) = (unsigned int)(v_r12);
    goto loc_00A5B755;
loc_00A59ED7:
    if (a6 != 0) goto loc_00A59EEF;
    if (((unsigned int)(v_r14)) >= 8) goto loc_00A59EEF;
    v_stack_m3B8 = 0xC000000DULL;
    goto loc_00A5B79F;
loc_00A59EEF:
    result = BgkQueryBootGraphicsInformation((unsigned int)((unsigned int)(v_r12)), v_stack_m3B4, v_stack_m208, (unsigned int)(v_stack_m384));
    v_stack_m3B8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A5B79F;
    if (v_stack_m3B4 == 0) goto loc_00A594F9;
    if (((unsigned int)(v_r14)) < v_stack_m3B4) goto loc_00A590DF;
    result = BgkQueryBootGraphicsInformation((unsigned int)((unsigned int)(v_r13)), v_stack_m2A8, v_stack_m208, (unsigned int)(v_stack_m384));
    v_stack_m3B8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A5B79F;
    if (v_stack_m2A8 == 0) goto loc_00A594F9;
    result = memcpy(v_rdi, v_stack_m2A8, (unsigned int)(v_stack_m3B4), (unsigned int)(v_stack_m384));
    goto loc_00A59F6D;
loc_00A59F6D:
    goto loc_00A59559;
loc_00A59F77:
    result = ExpQueryChannelInformation(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4, (unsigned int)(v_stack_m384));
    goto loc_00A57FA3;
loc_00A59F91:
    result = ExpQueryMemoryTopologyInformation(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4, (unsigned int)(v_stack_m384));
    goto loc_00A57FA3;
loc_00A59FAB:
    v_r12 = 32;
    if (((unsigned int)(v_stack_m2A8)) != 18) { v_r12 = (unsigned int)(32 + 8); }
    v_stack_m3B4 = (unsigned int)(v_r12);
    if (((unsigned int)(v_r14)) >= ((unsigned int)(v_r12))) goto loc_00A59FDD;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = (unsigned int)(v_r12);
    goto loc_00A5B755;
loc_00A59FDD:
    v_stack_m3B4 = 0;
    a4 = (((unsigned int)(v_stack_m2A8)) == ((unsigned int)(result))) ? 1 : 0;
    v_stack_m3C8 = v_stack_m3B4;
    result = MmGetPageFileInformation(v_rdi, v_rdi, (unsigned int)((unsigned int)(v_r14)), a4);
    goto loc_00A5B773;
loc_00A5A004:
    if (((unsigned int)(v_stack_m2A8)) > 151) goto loc_00A5A124;
    if (((unsigned int)(v_stack_m2A8)) == 151) goto loc_00A5A0E1;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m2A8))) - (145));
    if (condition_is_equal) goto loc_00A59D55;
    a1 = (unsigned int)((a1) - ((unsigned int)(v_r12)));
    if (condition_is_equal) goto loc_00A5A0CC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5B737;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5A07C;
    if (a1 != 1) goto loc_00A5B6E3;
    if (v_rdi == 0) goto loc_00A5A062;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5765667), v_stack_m3B0, (unsigned int)((unsigned int)(v_r14)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A5B210;
loc_00A5A062:
    result = ExpQueryBootLoaderMetadata(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4, a4);
    goto loc_00A57FA3;
loc_00A5A07C:
    if (((unsigned int)(v_r14)) >= 3) goto loc_00A5A09C;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 3;
    goto loc_00A5B755;
loc_00A5A09C:
    result = ((*(unsigned __int8 *)(v_rip + 3869050)) == 0) ? 1 : 0;
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(result);
    *(unsigned __int8 *)(v_rdi + 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 5166410));
    result = ((*(unsigned __int8 *)(v_rip + 5166372)) == 0) ? 1 : 0;
    *(unsigned __int8 *)(v_rdi + 2) = (unsigned __int8)(result);
    v_stack_m3B4 = 3;
    goto loc_00A5B79F;
loc_00A5A0CC:
    result = ExpQueryPortableWorkspaceEfiLauncherInformation(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4, a4);
    goto loc_00A5B773;
loc_00A5A0E1:
    v_stack_m3B4 = 4;
    if (((unsigned int)(v_r14)) >= 4) goto loc_00A5A109;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 4;
    goto loc_00A5B755;
loc_00A5A109:
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4252725)));
    goto loc_00A5B79F;
loc_00A5A124:
    v_rbx = (unsigned int)((v_stack_m2A8) - (153));
    if (condition_is_equal) goto loc_00A5A287;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5A255;
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(v_r12)));
    if (condition_is_equal) goto loc_00A5A1FB;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5A181;
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A5B6E3;
    v_stack_m3B4 = (unsigned int)(32 + 8);
    if (((unsigned int)(v_r14)) >= ((unsigned int)(32 + 8))) goto loc_00A5A170;
    if (a6 == 0) goto loc_00A589BB;
    *(unsigned int *)(a6) = (unsigned int)(32 + 8);
    goto loc_00A589BB;
loc_00A5A170:
    result = PoEnergyEstimationEnabled(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4, a4);
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(result);
    goto loc_00A5B79F;
loc_00A5A181:
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rip + 4869858)) + (24));
    v_stack_m3B4 = a1;
    if (((unsigned int)(v_r14)) < a1) goto loc_00A589BB;
    result = 0;
    *(unsigned __int64 *)(v_rdi) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 16) = 0;
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4869810)));
    *(unsigned __int16 *)(v_rdi + 8) = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 4869809));
    *(unsigned __int16 *)(v_rdi + 10) = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 4869800));
    result = *(unsigned __int16 *)(v_rip + 4869800);
    if ((*(unsigned __int16 *)(v_rip + 4869786)) != 0) {
        *(unsigned __int64 *)(v_rdi + 16) = v_rdi + 24;
        a3 = *(unsigned __int16 *)(v_rip + 4869774);
        a2 = *(unsigned __int64 *)(v_rip + 4869773);
        result = memcpy(v_rdi + 24, a2, a3, a4);
    }
    goto loc_00A5B79F;
loc_00A5A1FB:
    v_stack_m3B4 = 128;
    if (((unsigned int)(v_r14)) != 128) goto loc_00A589BB;
    result = BgkQueryBootGraphicsInformation(v_r14 - 125, v_stack_m208, a3, a4);
    v_stack_m3B8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A5B79F;
    result = memcpy(v_rdi, v_stack_m208, (unsigned int)(v_stack_m3B4), a4);
    goto loc_00A5B79F;
loc_00A5A255:
    if (((unsigned int)(v_r14)) >= 32) goto loc_00A5A276;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 32;
    goto loc_00A5B755;
loc_00A5A276:
    result = ExpGetSystemProcessorFeaturesInformation(v_rdi, v_stack_m208, (unsigned int)(v_stack_m3B4), a4);
loc_00A5A27E:
    v_stack_m3B8 = (unsigned int)(result);
    goto loc_00A59A32;
loc_00A5A287:
    if ((unsigned int)((unsigned int)(v_stack_m390)) != 0) goto loc_00A589BB;
    v_stack_m3B4 = (unsigned int)((unsigned int)(v_stack_m390) + 32);
    if (((unsigned int)(v_r14)) < ((unsigned int)((unsigned int)(v_stack_m390) + 32))) goto loc_00A5A2CE;
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4935516)));
    *(unsigned int *)(v_rdi + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4935512)));
    *(unsigned int *)(v_rdi + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4935507)));
    *(unsigned __int64 *)(v_rdi + 16) = *(unsigned __int64 *)(v_rip + 4935505);
    *(unsigned int *)(v_rdi + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4935503)));
    goto loc_00A5A2F6;
loc_00A5A2CE:
    if (((unsigned int)(v_r14)) < 12) goto loc_00A5A2FB;
    v_stack_m3B4 = 12;
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4935454)));
    *(unsigned int *)(v_rdi + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4935450)));
    *(unsigned int *)(v_rdi + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4935445)));
loc_00A5A2F6:
    goto loc_00A5B79F;
loc_00A5A2FB:
    v_stack_m3B8 = (unsigned int)((unsigned int)(0xC0000004ULL));
    goto loc_00A5B79F;
loc_00A5A319:
    result = HvlQueryDetailInfo(v_rdi, (unsigned int)((unsigned int)(v_r14)), (unsigned int)(v_stack_m3B4), v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5A32E:
    if (((unsigned int)(v_rbx)) > 174) goto loc_00A5A76E;
    if (((unsigned int)(v_rbx)) == 174) goto loc_00A5A759;
    if (((unsigned int)(v_rbx)) > 166) goto loc_00A5A60A;
    if (((unsigned int)(v_rbx)) == 166) goto loc_00A5A5F5;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (160));
    if (condition_is_equal) goto loc_00A5A546;
    a1 = (unsigned int)((a1) - ((unsigned int)((unsigned int)(v_stack_m390) + 32)));
    if (condition_is_equal) goto loc_00A5A531;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5A4FF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5B6ED;
    if (a1 != 1) goto loc_00A5B6E3;
    v_stack_m3B4 = 16;
    if (((unsigned int)(v_r14)) == 16) goto loc_00A5A3AE;
    if (a6 == 0) goto loc_00A589BB;
    *(unsigned int *)(a6) = 16;
    goto loc_00A589BB;
loc_00A5A3AE:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 4869316)) & ((unsigned __int8)((unsigned int)(0xC0000004ULL))));
    a1 = (unsigned __int8)((a1) << (4));
    result = (unsigned __int8)((v_stack_m208) & (239));
    a1 = (unsigned __int8)((a1) | ((unsigned __int8)(result)));
    v_stack_m208 = (unsigned __int8)(a1);
    result = VslIsSecureKernelRunning(a1, (unsigned int)((unsigned int)(v_r14)), (unsigned int)(v_stack_m3B4), v_stack_m3B4);
    if ((unsigned __int8)(result) == 0) goto loc_00A5A4E9;
    v_stack_m388 = 0;
    a1 = (unsigned __int8)((a1) | ((unsigned __int8)((unsigned int)(0xC0000004ULL))));
    v_stack_m208 = (unsigned __int8)(a1);
    a1 = 0;
    result = VslGetNestedPageProtectionFlags(a1, (unsigned int)((unsigned int)(v_r14)), (unsigned int)(v_stack_m3B4), v_stack_m3B4);
    if ((((unsigned __int8)((unsigned int)(v_stack_m390) + 32)) & ((unsigned __int8)(result))) != 0) {
    }
    if (((32) & ((unsigned __int8)((unsigned int)((unsigned int)(result))))) != 0) {
    }
    if ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (16)) != 0) {
    }
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned __int8)((v_stack_m207) | (2));
        v_stack_m207 = (unsigned __int8)(a1);
    }
    result = v_stack_m2A0;
    if (v_stack_m2A0 != 0) {
        a2 = v_stack_m388;
        a1 = v_stack_m2A0;
        result = VslIsTrustletRunning(a1, a2, (unsigned int)(v_stack_m3B4), v_stack_m3B4);
        v_stack_m3B8 = (unsigned int)(result);
        a1 = v_stack_m207;
        a1 = (unsigned __int8)((a1) & (254));
        result = v_stack_m388;
        result = (unsigned __int8)((result) & ((unsigned __int8)((unsigned int)(0xC0000004ULL))));
        a1 = (unsigned __int8)((a1) | ((unsigned __int8)(result)));
        v_stack_m207 = (unsigned __int8)(a1);
    }
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned __int8)((a1) | (4));
        v_stack_m207 = (unsigned __int8)(a1);
    }
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned __int8)((a1) | (8));
        v_stack_m207 = (unsigned __int8)(a1);
    }
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned __int8)((a1) | (16));
        v_stack_m207 = (unsigned __int8)(a1);
    }
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned __int8)((a1) | (32));
        v_stack_m207 = (unsigned __int8)(a1);
    }
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned __int8)((a1) | (64));
        v_stack_m207 = (unsigned __int8)(a1);
    }
    if (!(condition_is_above_or_equal)) {
    }
    result = VslIsEncryptionKeyAvailable(a1, a2, (unsigned int)(v_stack_m3B4), v_stack_m3B4);
    result = (unsigned __int8)((result) & ((unsigned __int8)((unsigned int)(0xC0000004ULL))));
    result = (unsigned __int8)((result) << (5));
    a1 = (unsigned __int8)((v_stack_m208) & (223));
    result = (unsigned __int8)((result) | ((unsigned __int8)(a1)));
    v_stack_m208 = (unsigned __int8)(result);
loc_00A5A4E9:
    *(unsigned __int64 *)(v_rdi) = v_xmm0;
    goto loc_00A5B79F;
loc_00A5A4FF:
    if (((unsigned int)(v_r14)) >= ((unsigned int)((unsigned int)(0xC0000004ULL)))) goto loc_00A5A51A;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(0xC0000004ULL));
    goto loc_00A5B755;
loc_00A5A51A:
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 5224320));
    v_stack_m3B4 = (unsigned int)((unsigned int)(0xC0000004ULL));
    goto loc_00A5B79F;
loc_00A5A531:
    result = SeQueryTrustedPlatformModuleInformation(v_rdi, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5A546:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m3B4))) << (6));
    v_stack_m3B4 = (unsigned int)(result);
    if (((unsigned int)(v_r14)) < 64) goto loc_00A590DF;
    if (((unsigned int)(v_r14)) < ((unsigned int)(result))) {
        a4 = (unsigned int)(v_r14);
        a4 = (unsigned int)((a4) >> (6));
        v_stack_m384 = (unsigned int)(a4);
    }
    result = (unsigned int)((result) & (0xC0000004ULL));
    v_stack_m368 = (unsigned int)(result);
    v_stack_m2D8 = v_rdi;
    v_stack_m3A8 = 0;
loc_00A5A597:
    if (0 >= ((unsigned int)(a4))) goto loc_00A5A5E9;
    v_stack_m3AC = (unsigned __int16)((unsigned int)(v_stack_m380));
    v_stack_m3AA = 0;
    v_stack_m3A9 = 0;
    result = KeGetProcessorIndexFromNumber(v_stack_m3AC, (unsigned int)((unsigned int)(v_r14)), v_stack_m3B4, a4);
    result = KeQueryCycleTimeStatsProcessor(*(unsigned __int64 *)(v_rip + 5695150 + (unsigned int)((unsigned int)(result)) * 8), v_rdi, v_stack_m3B4, a4);
    v_rdi = (v_rdi) + (64);
    v_stack_m2D8 = v_rdi;
    v_r12 = (unsigned int)((0) + (1));
    v_stack_m3A8 = (unsigned int)(v_r12);
    goto loc_00A5A597;
loc_00A5A5E9:
    goto loc_00A5B773;
loc_00A5A5F5:
    result = SeQueryHSTIResults(v_rdi, (unsigned int)((unsigned int)(v_rip + 5695150)), v_stack_m3B4, (unsigned int)(v_stack_m384));
    goto loc_00A5B773;
loc_00A5A60A:
    a1 = (unsigned int)((1) - (167));
    if (condition_is_equal) goto loc_00A5A73F;
    a1 = (unsigned int)((a1) - ((unsigned int)(v_r12)));
    if (condition_is_equal) goto loc_00A5A72A;
    a1 = (unsigned int)((a1) - ((unsigned int)(v_r12)));
    if (condition_is_equal) goto loc_00A59D55;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5B6ED;
    if (a1 != 1) goto loc_00A5B6E3;
    result = ExCpuSetResourceManagerAccessCheck(v_stack_m3B0, (unsigned int)((unsigned int)(v_rip + 5695150)), v_stack_m3B4, (unsigned int)(v_stack_m384));
    v_stack_m3B8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A5B7BE;
    v_stack_m3B4 = 264;
    if (((unsigned int)(v_rip + 5695150)) != 264) goto loc_00A589BB;
    result = ExAllocatePool2((unsigned int)((unsigned int)(264 - 8)), 264, (unsigned int)(0x6F666E49ULL), (unsigned int)(v_stack_m384));
    v_stack_m3A0 = result;
    if (result != 0) goto loc_00A5A68C;
    goto loc_00A5B7BE;
loc_00A5A68C:
    *(unsigned __int16 *)((unsigned int)(0xC000009AULL)) = (unsigned __int16)((unsigned int)(0xC0000004ULL));
    *(unsigned __int16 *)((unsigned int)(0xC000009AULL) + 2) = 32;
    *(unsigned int *)((unsigned int)(0xC000009AULL) + 4) = 0;
    a2 = 0;
    result = memset((unsigned int)(0xC000009AULL) + 8, a2, 264 - 8, (unsigned int)(v_stack_m384));
    result = KeGetAffinitizedInterruptsInfo(result, a2, 264 - 8, (unsigned int)(v_stack_m384));
loc_00A5A6B8:
    *(unsigned __int64 *)(v_rdi) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 16) = v_xmm1;
    *(unsigned __int64 *)(v_rdi + 32) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 48) = v_xmm1;
    *(unsigned __int64 *)(v_rdi + 64) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 80) = v_xmm1;
    *(unsigned __int64 *)(v_rdi + 96) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 128 - 16) = v_xmm1;
    result = (2) - (1);
    if (condition_is_not_equal) goto loc_00A5A6B8;
    *(unsigned __int64 *)(v_rdi + 128) = *(unsigned __int64 *)(result + 128);
    goto loc_00A5972B;
loc_00A5A72A:
    result = HvlQueryVsmProtectionInfo(v_rdi + 128, (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4, (unsigned int)(v_stack_m384));
    goto loc_00A5B773;
loc_00A5A73F:
    result = ExpQuerySingleModuleInformation(v_rdi + 128, (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B0, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5A759:
    result = PsRootSiloInformation(v_rdi + 128, (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5A76E:
    if (((unsigned int)(result)) > 182) goto loc_00A5AAAA;
    if (((unsigned int)(result)) == 182) goto loc_00A5A95B;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) - (175));
    if (condition_is_equal) goto loc_00A5A8C9;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00A5A832;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A59D55;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5A810;
loc_00A5A7A6:
    if (a1 != 1) goto loc_00A5B6E3;
    if (v_stack_m3B4 == 0) goto loc_00A5B306;
    v_stack_m250 = 0;
    v_stack_m3C0 = 0;
    v_stack_m3C8 = v_stack_m250;
    result = ObReferenceObjectByHandle(v_stack_m298, (unsigned int)(0x1000ULL), *(unsigned __int64 *)(v_rip + 5685977), v_stack_m3B0);
    v_stack_m2C8 = v_stack_m250;
    if (sign_flag) goto loc_00A5B7BE;
    goto loc_00A5B311;
loc_00A5A810:
    v_stack_m3C8 = v_stack_m3B4;
    result = ExpQueryInterruptSteeringInformation(v_stack_m3A0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128, (unsigned int)((unsigned int)(264 - 8)));
    goto loc_00A5B773;
loc_00A5A832:
    if ((unsigned int)(264 - 8) == 0) goto loc_00A590DF;
    if ((unsigned __int8)(v_stack_m3B0) == 0) goto loc_00A5A859;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5763836), (unsigned __int8)(v_stack_m3B0), v_rdi + 128, (unsigned int)((unsigned int)(264 - 8)));
    if ((unsigned __int8)(result) == 0) goto loc_00A5B210;
loc_00A5A859:
    result = ExAllocatePool2(65, 264 - 8, (unsigned int)(0x6F666E49ULL), (unsigned int)((unsigned int)(264 - 8)));
    v_stack_m3A0 = result;
    if (result == 0) goto loc_00A594F9;
    result = VslQuerySecureKernelProfileInformation(v_stack_m268, result, (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4);
    v_stack_m3B8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A59AE1;
    result = memcpy(v_rdi + 128, result, (unsigned int)(v_stack_m3B4), v_stack_m3B4);
    goto loc_00A59AE1;
loc_00A5A8C9:
    if ((unsigned int)(v_stack_m3B4) == 0) goto loc_00A5A923;
    v_stack_m260 = 0;
    v_stack_m3C0 = 0;
    v_stack_m3C8 = v_stack_m260;
    result = ObReferenceObjectByHandle(v_stack_m298, (unsigned int)(0x1000ULL), *(unsigned __int64 *)(v_rip + 5685699), v_stack_m3B0);
    v_stack_m2C8 = v_stack_m260;
    if (sign_flag) goto loc_00A5B7BE;
    goto loc_00A5A92E;
loc_00A5A923:
loc_00A5A92E:
    result = KeQueryCpuSetInformation(v_rdi + 128, (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
loc_00A5A941:
    v_stack_m3B8 = (unsigned int)(result);
    if (0 == 0) goto loc_00A5B79F;
    result = ObfDereferenceObject(v_stack_m2C8, (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    goto loc_00A5B79F;
loc_00A5A95B:
    if (((unsigned int)(264 - 8)) == 56) goto loc_00A5A97B;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 56;
    goto loc_00A5B755;
loc_00A5A97B:
    result = MmGetProcessPartitionId(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = MmGetNumberOfPhysicalPages((unsigned __int16)(result), (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = (result) << (12);
    v_stack_m208 = result;
    result = MmGetAvailablePages((unsigned __int16)((unsigned __int16)(result)), (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = (result) << (12);
    v_stack_m200 = result;
    result = MmGetResidentAvailablePages((unsigned __int16)((unsigned __int16)(result)), (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = (result) << (12);
    v_stack_m1F8 = result;
    result = MmGetTotalCommittedPages((unsigned __int16)((unsigned __int16)(result)), (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = (result) << (12);
    v_stack_m1F0 = result;
    result = MmGetTotalCommitLimit((unsigned __int16)((unsigned __int16)(result)), (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = (result) << (12);
    v_stack_m1E0 = result;
    result = MmGetPeakCommitment((unsigned __int16)((unsigned __int16)(result)), (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = (result) << (12);
    v_stack_m1D8 = result;
    result = MmGetSharedCommit((unsigned __int16)((unsigned __int16)(result)), (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = (result) << (12);
    v_stack_m1E8 = result;
    result = v_stack_m208;
    if (v_stack_m208 < v_stack_m200) { result = v_stack_m200; }
    v_stack_m208 = result;
    result = v_stack_m1E0;
    if (v_stack_m1E0 < v_stack_m1F0) { result = v_stack_m1F0; }
    v_stack_m1E0 = result;
    result = v_stack_m1D8;
    if (v_stack_m1D8 < v_stack_m1F0) { result = v_stack_m1F0; }
    v_stack_m1D8 = result;
    *(unsigned __int64 *)(v_rdi + 128) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 128 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_rdi + 128 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 128 + 48) = v_xmm0;
    v_stack_m3B4 = 56;
    goto loc_00A5B79F;
loc_00A5AAAA:
    v_rbx = (unsigned int)(((unsigned __int16)(result)) - (183));
    if (condition_is_equal) goto loc_00A5AC08;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5AB66;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5AB56;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5AB0E;
    if (((unsigned int)(v_rbx)) != 0) goto loc_00A5B6E3;
    if (((unsigned int)(264 - 8)) != 8) goto loc_00A5B755;
    result = PsQueryActivityModerationUserSettings(v_stack_m208, (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    v_stack_m3B8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A5B79F;
    *(unsigned __int64 *)(v_rdi + 128) = v_stack_m208;
    goto loc_00A5B79F;
loc_00A5AB0E:
    if ((unsigned int)(264 - 8) == 0) goto loc_00A5AB29;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 0;
    goto loc_00A5B755;
loc_00A5AB29:
    v_stack_m302 = (unsigned __int8)((unsigned int)(0xC0000004ULL));
    v_stack_m3C8 = (unsigned int)((unsigned int)(0xC0000004ULL));
    result = ZwFilterBootOption((unsigned int)((unsigned int)((unsigned int)(0xC0000004ULL))), (unsigned int)(0x10200003ULL), (unsigned int)(0x260000A0ULL), v_stack_m302);
    goto loc_00A5B7BE;
loc_00A5AB56:
    result = sub_008D3420(v_rdi + 128, (unsigned int)((unsigned int)(264 - 8)), (unsigned int)(0x260000A0ULL), v_stack_m302);
    goto loc_00A5B773;
loc_00A5AB66:
    if (((unsigned int)(264 - 8)) == 24) goto loc_00A5AB86;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 24;
    goto loc_00A5B755;
loc_00A5AB86:
    result = MmGetProcessPartitionId(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), (unsigned int)((unsigned int)(264 - 8)), (unsigned int)(0x260000A0ULL), v_stack_m302);
    result = MmGetNumberOfPhysicalPages((unsigned __int16)(result), (unsigned int)((unsigned int)(264 - 8)), (unsigned int)(0x260000A0ULL), v_stack_m302);
    result = (result) << (12);
    v_stack_m208 = result;
    result = MmGetLowestPhysicalPage((unsigned __int16)((unsigned __int16)(result)), (unsigned int)((unsigned int)(264 - 8)), (unsigned int)(0x260000A0ULL), v_stack_m302);
    result = (result) << (12);
    v_stack_m200 = result;
    result = MmGetHighestPhysicalPage((unsigned __int16)((unsigned __int16)(result)), (unsigned int)((unsigned int)(264 - 8)), (unsigned int)(0x260000A0ULL), v_stack_m302);
    result = (result) << (12);
    result = (result) + (0xFFFULL);
    v_stack_m1F8 = result;
    *(unsigned __int64 *)(v_rdi + 128) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 128 + 16) = v_xmm0;
loc_00A5ABF6:
    v_stack_m3B4 = 24;
    goto loc_00A5B79F;
loc_00A5AC08:
    if (((unsigned int)(264 - 8)) != 16) goto loc_00A5B755;
    v_stack_m218 = *(unsigned __int64 *)(v_rdi + 128);
    v_stack_m228 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 128 + 8)));
    result = ExpQueryCodeIntegrityCertificateInfo(*(unsigned __int64 *)(v_rdi + 128), (unsigned int)(*(unsigned int *)(v_rdi + 128 + 8)), (unsigned int)(0x260000A0ULL), v_stack_m302);
    goto loc_00A5B773;
loc_00A5AC36:
    if (((unsigned int)((unsigned __int16)(result))) > 222) goto loc_00A5B2A9;
    if (((unsigned int)((unsigned __int16)(result))) == 222) goto loc_00A5B274;
    if (((unsigned int)((unsigned __int16)(result))) > 202) goto loc_00A5AFCF;
    if (((unsigned int)((unsigned __int16)(result))) == 202) goto loc_00A5AF4E;
    if (((unsigned int)((unsigned __int16)(result))) > 196) goto loc_00A5ADEC;
    if (((unsigned int)((unsigned __int16)(result))) == 196) goto loc_00A5ADD7;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int16)(result)))) - (190));
    if (condition_is_equal) goto loc_00A5B6ED;
    a1 = (unsigned int)((a1) - (0));
    if (condition_is_equal) goto loc_00A5ADA9;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5ACF3;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5ACC9;
    if (a1 != 1) goto loc_00A5B6E3;
    if (((unsigned int)(264 - 8)) >= 8) goto loc_00A5ACB8;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 8;
    goto loc_00A5B755;
loc_00A5ACB8:
    result = ExpGetSystemWriteConstraintInformation(v_rdi + 128, (unsigned int)(*(unsigned int *)(v_rdi + 128 + 8)), (unsigned int)(0x260000A0ULL), v_stack_m302);
    v_stack_m3B8 = (unsigned int)(result);
    goto loc_00A5B0A7;
loc_00A5ACC9:
    v_stack_m3C0 = (unsigned __int8)(v_stack_m3B0);
    v_stack_m3C8 = v_stack_m3B4;
    result = VslTransformDumpKey(v_stack_m3A0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128, (unsigned int)((unsigned int)(264 - 8)));
    goto loc_00A5B773;
loc_00A5ACF3:
    result = KeQueryActiveGroupCount(v_stack_m3A0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128, (unsigned int)((unsigned int)(264 - 8)));
    result = (unsigned int)(((unsigned __int16)(result)) << (3));
    v_stack_m3B4 = (unsigned int)(result);
    if (((unsigned int)(264 - 8)) < ((unsigned int)(result))) goto loc_00A590DF;
    a2 = 0;
    result = memset(v_rdi + 128, a2, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(264 - 8)));
loc_00A5AD1F:
    v_stack_m3A8 = 0;
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 5677782)))) goto loc_00A5AD96;
    result = KeInitializeSchedulerSubNodeEnumerationContext(v_stack_m58, *(unsigned __int64 *)(v_rip + 5720456 + 0 * 8), 0, (unsigned int)((unsigned int)(264 - 8)));
loc_00A5AD49:
    result = KeEnumerateNextSchedulerSubNodeInNode(v_stack_m58, v_stack_m258, 0, (unsigned int)((unsigned int)(264 - 8)));
    if ((unsigned int)(result) != 0) goto loc_00A5AD8D;
    v_stack_m394 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m258 + 136));
    a2 = (*(unsigned __int64 *)(v_stack_m258 + 16)) | (*(unsigned __int64 *)(v_rdi + 128 + v_stack_m394 * 8));
    *(unsigned __int64 *)(v_rdi + 128 + v_stack_m394 * 8) = a2;
    goto loc_00A5AD49;
loc_00A5AD8D:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m3A8)) + 1);
    goto loc_00A5AD1F;
loc_00A5AD96:
    goto loc_00A5B79F;
loc_00A5ADA9:
    if (((unsigned int)(264 - 8)) >= 32) goto loc_00A5ADCA;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 32;
    goto loc_00A5B755;
loc_00A5ADCA:
    result = ExpGetSystemFlushInformation(v_rdi + 128, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(264 - 8)));
    goto loc_00A5A27E;
loc_00A5ADD7:
    result = KeQueryKvaShadowInformation(v_rdi + 128, (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4, (unsigned int)((unsigned int)(264 - 8)));
    goto loc_00A5B773;
loc_00A5ADEC:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (197));
    if (condition_is_equal) goto loc_00A5AF1A;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5AE45;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5B6ED;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5AE2B;
    if (a1 != 1) goto loc_00A5B6E3;
    result = KeQuerySpeculationControlInformation(v_rdi + 128, (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4, (unsigned int)((unsigned int)(264 - 8)));
    goto loc_00A5B773;
loc_00A5AE2B:
loc_00A5AE30:
    result = IoQuerySystemDeviceName(200, v_rdi + 128, (unsigned int)((unsigned int)(264 - 8)), v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5AE45:
    a3 = 0;
    a2 = 0;
    result = guard_dispatch_icall(a2 + 34, a2, a3, v_stack_m398);
    v_stack_m3B8 = (unsigned int)(result);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC0000004ULL)))) goto loc_00A5AE77;
loc_00A5AE6D:
    goto loc_00A5B7BE;
loc_00A5AE77:
    if (((unsigned int)(264 - 8)) < v_stack_m398) goto loc_00A59301;
    if (v_rdi + 128 == 0) goto loc_00A59301;
    if ((unsigned __int8)(v_stack_m3B0) == 0) goto loc_00A5AEB9;
    result = ExAllocatePool2(257, (unsigned int)(v_stack_m398), (unsigned int)(0x6F666E49ULL), v_stack_m398);
    v_stack_m3A0 = result;
    if (result != 0) goto loc_00A5AEC1;
    goto loc_00A594F9;
loc_00A5AEB9:
    v_stack_m3A0 = v_rdi + 128;
loc_00A5AEC1:
    result = guard_dispatch_icall(34, (unsigned int)(v_stack_m398), v_rdi + 128, v_stack_m3B4);
    v_stack_m3B8 = (unsigned int)(result);
    if ((unsigned __int8)(v_stack_m3B0) == 0) goto loc_00A5B79F;
    if (sign_flag) goto loc_00A592F4;
    result = memcpy(v_rdi + 128, v_rdi + 128, (unsigned int)(v_stack_m3B4), v_stack_m3B4);
    goto loc_00A592F4;
loc_00A5AF1A:
    v_stack_m3B4 = 8;
    if (((unsigned int)(v_rdi + 128)) < 8) goto loc_00A589BB;
    a1 = 0;
    *(unsigned __int64 *)(v_rdi + 128) = 0;
    *(unsigned __int64 *)(v_rdi + 128) = *(unsigned __int64 *)(v_rip + 4009029);
    goto loc_00A5B79F;
loc_00A5AF4E:
    v_stack_m3B4 = (unsigned int)((unsigned int)(0xC0000004ULL));
    if (((unsigned int)(v_rdi + 128)) == ((unsigned int)((unsigned int)(0xC0000004ULL)))) goto loc_00A5AF6E;
    if (a6 == 0) goto loc_00A589BB;
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(0xC0000004ULL));
    goto loc_00A589BB;
loc_00A5AF6E:
    v_stack_m2B4 = 0;
    result = guard_dispatch_icall(48, (unsigned int)((unsigned int)((unsigned int)(0xC0000004ULL))), v_stack_m208, v_stack_m2B4);
    v_stack_m3B8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A58BFB;
    if (v_stack_m2B4 != ((unsigned int)((unsigned int)(0xC0000004ULL)))) goto loc_00A58BFB;
    *(unsigned __int8 *)(v_rdi + 128) = (unsigned __int8)(v_stack_m208);
    goto loc_00A5B79F;
loc_00A5AFCF:
    if (((unsigned int)(v_stack_m3B0)) > 211) goto loc_00A5B0EE;
    if (((unsigned int)(v_stack_m3B0)) == 211) goto loc_00A5B0B9;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m3B0))) - (206));
    if (condition_is_equal) goto loc_00A5B075;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5B043;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5B02E;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5B6ED;
    if (a1 != 1) goto loc_00A5B6E3;
    v_stack_m3C8 = v_stack_m3B4;
    result = CmQuerySingleFeatureConfiguration(v_stack_m3A0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B02E:
    result = SeSecurityModelQueryInformation(v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)), v_stack_m3B4, (unsigned int)((unsigned int)(v_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B043:
    if (((unsigned int)(v_rdi + 128)) == 4) goto loc_00A5B063;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 4;
    goto loc_00A5B755;
loc_00A5B063:
    *(unsigned int *)(v_rdi + 128) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5673815)));
    goto loc_00A57FDB;
loc_00A5B075:
    if (((unsigned int)(v_rdi + 128)) == 8) goto loc_00A5B095;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 8;
    goto loc_00A5B755;
loc_00A5B095:
    result = ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4865436))) != 0) ? 1 : 0;
    *(unsigned __int8 *)(v_rdi + 128) = (unsigned __int8)(result);
    *(unsigned int *)(v_rdi + 128 + 4) = 0;
loc_00A5B0A7:
    v_stack_m3B4 = 8;
    goto loc_00A5B79F;
loc_00A5B0B9:
    v_stack_m3C0 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m3C8 = v_stack_m3B4;
    result = CmQueryFeatureConfigurationSections(v_stack_m3A0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B0EE:
    v_rbx = (unsigned int)((v_stack_m3B0) - (213));
    if (condition_is_equal) goto loc_00A5B25F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5B209;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5B1B5;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5B18C;
    if (((unsigned int)(v_rbx)) != 5) goto loc_00A5B6E3;
    if (((unsigned int)(v_rdi + 128)) == 4) goto loc_00A5B13A;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 4;
    goto loc_00A5B755;
loc_00A5B13A:
    result = 0;
    *(unsigned int *)(v_rdi + 128) = 0;
    result = KeIsCetCapable(v_stack_m3A0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)));
    a1 = (unsigned int)(((unsigned __int8)(result)) & ((unsigned int)((unsigned int)(0xC0000004ULL))));
    *(unsigned int *)(v_rdi + 128) = a1;
    result = KeIsUserCetAllowed(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)));
    v_rbx = (unsigned int)(((unsigned __int8)(result)) + ((unsigned int)((unsigned __int8)(result))));
    v_rbx = (unsigned int)((v_rbx) ^ (a1));
    v_rbx = (unsigned int)((v_rbx) & (32));
    v_rbx = (unsigned int)((v_rbx) ^ (a1));
    *(unsigned int *)(v_rdi + 128) = (unsigned int)(v_rbx);
    result = KeIsKernelCetEnabled(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)));
    a2 = (unsigned int)(((unsigned __int8)(result)) & ((unsigned int)((unsigned int)(0xC0000004ULL))));
    a2 = (unsigned int)((a2) << (8));
    a2 = (unsigned int)((a2) | ((unsigned int)(v_rbx)));
    *(unsigned int *)(v_rdi + 128) = (unsigned int)(a2);
    result = KeIsKernelCetAuditModeEnabled(a1, a2, v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)));
    a1 = (unsigned int)(((unsigned __int8)(result)) & ((unsigned int)((unsigned int)(0xC0000004ULL))));
    a1 = (unsigned int)((a1) << (9));
    a1 = (unsigned int)((a1) | ((unsigned int)(a2)));
    *(unsigned int *)(v_rdi + 128) = a1;
    goto loc_00A57FDB;
loc_00A5B18C:
    v_stack_m3B4 = 32;
    if (((unsigned int)(v_rdi + 128)) != 32) goto loc_00A589BB;
    result = WheaQuerySystemInformation(v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)), v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)));
    goto loc_00A57FA3;
loc_00A5B1B5:
    if (v_stack_m3B0 == 0) goto loc_00A5B1C9;
loc_00A5B1BC:
    v_stack_m3B8 = 0xC0000061ULL;
    goto loc_00A5B79F;
loc_00A5B1C9:
    if (*(unsigned __int64 *)(v_rip + 4865624) != 0) goto loc_00A5B1E2;
loc_00A5B1D5:
    v_stack_m3B8 = 0xC000000EULL;
    goto loc_00A5B79F;
loc_00A5B1E2:
    v_stack_m3B4 = 24;
    if (((unsigned int)(v_rdi + 128)) < 24) goto loc_00A589BB;
    *(unsigned __int64 *)(v_rdi + 128) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 128 + 16) = v_xmm1;
    goto loc_00A5B79F;
loc_00A5B209:
    if (v_stack_m3B0 == 0) goto loc_00A5B21A;
loc_00A5B210:
    goto loc_00A5B7BE;
loc_00A5B21A:
    if (*(unsigned __int64 *)(v_rip + 4865535) == 0) goto loc_00A5B79F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4865535))) == 0) goto loc_00A5B79F;
    v_stack_m3B4 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4865535))));
    if (v_rdi + 128 == 0) goto loc_00A5B79F;
    if (((unsigned int)(v_rdi + 128)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4865535)))))) goto loc_00A589BB;
    a2 = (*(unsigned __int64 *)(v_rip + 4865535)) + (8);
loc_00A5B24F:
    result = memcpy(v_rdi + 128, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4865535))), (unsigned int)((unsigned int)(v_rdi + 128)));
    goto loc_00A5B79F;
loc_00A5B25F:
    result = KeQuerySecureSpeculationInformation(v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)), v_stack_m3B4, (unsigned int)((unsigned int)(v_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B274:
    v_stack_m3C0 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m3C8 = v_stack_m3B4;
    result = CmQueryBuildVersionInformation(v_stack_m3A0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B2A9:
    if (((unsigned int)(v_rbx)) > 238) goto loc_00A5B4C0;
    if (((unsigned int)(v_rbx)) == 238) goto loc_00A5B4A3;
    if (((unsigned int)(v_rbx)) > ((unsigned int)(238 - 7))) goto loc_00A5B436;
    if (((unsigned int)(v_rbx)) == ((unsigned int)(238 - 7))) goto loc_00A59695;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (223));
    if (condition_is_equal) goto loc_00A5B361;
    a1 = (unsigned int)((a1) - (4));
    if (condition_is_equal) goto loc_00A5B32B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5B2EE;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00A5A7A6;
loc_00A5B2EE:
    v_stack_m3B4 = (unsigned int)(v_rdi + 128);
    result = KeQueryDpcWatchdogConfiguration(v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)), (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B306:
loc_00A5B311:
    v_stack_m3C8 = v_stack_m2C8;
    result = PsGetSupportedProcessorArchitectures(v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)), (unsigned int)((unsigned int)(v_rdi + 128)), v_stack_m3B4);
    goto loc_00A5A941;
loc_00A5B32B:
    v_stack_m3B4 = (unsigned int)((unsigned int)(0xC0000004ULL));
    if (((unsigned int)(v_rdi + 128)) == ((unsigned int)((unsigned int)(0xC0000004ULL)))) goto loc_00A5B34B;
    if (a6 == 0) goto loc_00A589BB;
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(0xC0000004ULL));
    goto loc_00A589BB;
loc_00A5B34B:
    *(unsigned __int8 *)(v_rdi + 128) = (unsigned __int8)((unsigned int)(0xC0000004ULL));
    goto loc_00A5B79F;
loc_00A5B361:
    if (v_stack_m3A0 == 0) goto loc_00A5B6E3;
    v_stack_m3C8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = ExPoolQueryLimits(v_stack_m3A0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128, v_rdi + 128);
    v_stack_m3B8 = (unsigned int)(result);
    if (sign_flag) goto loc_00A5B79F;
    goto loc_00A59EB4;
loc_00A5B3BB:
    if (v_stack_m3B8 != ((unsigned int)((unsigned int)(0xC0000004ULL)))) goto loc_00A59711;
    if (v_stack_m3B4 <= ((unsigned int)(v_rdi + 128))) goto loc_00A5B3D7;
    v_stack_m3B8 = (unsigned int)((unsigned int)(0xC0000004ULL));
    goto loc_00A59711;
loc_00A5B3D7:
    if (v_stack_m2C8 == 0) goto loc_00A5B3F3;
    result = v_stack_m208;
    if (v_stack_m2C8 != v_stack_m208) {
        a2 = 0;
        a1 = v_stack_m2C8;
        result = ExFreePoolWithTag(a1, a2, v_rdi + 128, v_rdi + 128);
    }
    result = ExAllocatePool2(257, (unsigned int)(v_stack_m3B4), (unsigned int)(0x6F666E49ULL), v_rdi + 128);
    v_stack_m3A0 = result;
    if (result != 0) goto loc_00A5B421;
    v_stack_m3B8 = 0xC000009AULL;
    goto loc_00A59711;
loc_00A5B421:
    v_stack_m398 = (unsigned int)((unsigned int)(v_stack_m3B4));
    goto loc_00A596D9;
loc_00A5B436:
    v_rbx = (unsigned int)((result) - (232));
    if (condition_is_equal) goto loc_00A58BFB;
    v_rbx = (unsigned int)((v_rbx) - (0));
    if (condition_is_equal) goto loc_00A5B47C;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A5B45A;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00A58BFB;
    goto loc_00A58BF2;
loc_00A5B45A:
    v_stack_m3C8 = v_stack_m3B4;
    result = HvlQuerySetBootPagesInfo(v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)), v_stack_m3B0, (unsigned __int8)((unsigned int)(0xC0000004ULL)));
    goto loc_00A5B773;
loc_00A5B47C:
    v_stack_m3B4 = (unsigned int)((unsigned int)(0x4298ULL));
    if (((unsigned int)(v_rdi + 128)) < ((unsigned int)((unsigned int)(0x4298ULL)))) goto loc_00A589BB;
    result = HvlQueryMinrootInfo(v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)), v_stack_m3B4, (unsigned __int8)((unsigned int)(0xC0000004ULL)));
    goto loc_00A5B773;
loc_00A5B4A3:
    v_stack_m3C8 = v_stack_m3B4;
    result = ExpQueryOriginalImageFeatureInformation(v_rdi + 128, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B4C0:
    if (((unsigned int)(v_rbx)) > 247) goto loc_00A5B6C1;
    if (((unsigned int)(v_rbx)) == 247) goto loc_00A5B685;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (239));
    if (condition_is_equal) goto loc_00A5B663;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5B641;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5B6ED;
    a1 = (unsigned int)((a1) - (0));
    if (condition_is_equal) goto loc_00A5B5F7;
    if (a1 != 1) goto loc_00A5B6E3;
loc_00A5B505:
    if ((unsigned int)((unsigned int)(v_stack_m390)) != 0) goto loc_00A589BB;
    result = MmEnumerateBadPages(v_stack_m290, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)));
    if (v_stack_m290 == 0) goto loc_00A5B561;
    a1 = (*(unsigned __int64 *)(v_stack_m290)) & (0);
    if (a1 <= 0x1FFFFFFFULL) goto loc_00A5B556;
    goto loc_00A5B561;
loc_00A5B556:
    v_stack_m3B4 = (unsigned int)(a1 * 8);
loc_00A5B561:
    v_r12 = (unsigned int)((unsigned int)((unsigned int)(0xC0000004ULL)));
    if (((unsigned int)(v_rdi + 128)) < ((unsigned int)(a1 * 8))) { v_r12 = (unsigned int)((unsigned int)(0xC0000004ULL)); }
    v_stack_m3B8 = (unsigned int)(v_r12);
    if (v_stack_m290 == 0) goto loc_00A5B79F;
    if (sign_flag) goto loc_00A5B5E8;
    if (((unsigned int)(v_rbx)) != 128) goto loc_00A5B5CC;
    if (a1 == 0) goto loc_00A5B5BE;
loc_00A5B594:
    result = v_stack_m290 + 8;
    if (!(condition_is_below)) {
        a4 = (*(unsigned __int64 *)(v_stack_m290 + 8)) & (v_stack_m3A0);
        *(unsigned __int64 *)(v_stack_m290 + 8) = a4;
        *(unsigned __int64 *)(v_stack_m290 + 8) = a4;
        result = (v_stack_m290 + 8) + (8);
    }
    a3 = (v_stack_m290 + 8) + (8);
    a1 = (a1) - (1);
    if (condition_is_not_equal) goto loc_00A5B594;
loc_00A5B5BE:
    result = (result) - (v_stack_m290);
    result = (result) - (8);
    result = (unsigned int)((result) & (0xFFFFFFF8ULL));
    v_stack_m3B4 = (unsigned int)(result);
loc_00A5B5CC:
    a2 = (v_stack_m290) + (8);
    result = memcpy(v_rdi + 128, a2, (unsigned int)(v_stack_m3B4), a4);
    goto loc_00A5B5E8;
loc_00A5B5E8:
    a2 = 0;
    goto loc_00A5955C;
loc_00A5B5F7:
    v_stack_m3B4 = 16;
    if (((unsigned int)(v_rdi + 128)) < 16) goto loc_00A589BB;
    result = VslQueryTrustedAppRuntimeInformation(v_stack_m208, a2, (unsigned int)(v_stack_m3B4), a4);
    v_stack_m3B8 = (unsigned int)(result);
    if (sign_flag) {
        v_stack_m3B8 = 0;
    }
    *(unsigned __int64 *)(v_rdi + 128) = v_xmm0;
    goto loc_00A5B79F;
loc_00A5B641:
    v_stack_m3C8 = v_stack_m3B4;
    result = ExpQuerySystemMemoryNumaPerformanceInformation(v_stack_m3A0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B663:
    v_stack_m3C8 = v_stack_m3B4;
    result = ExpQuerySystemMemoryNumaInformation(v_stack_m3A0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B685:
    if (v_stack_m3B0 != 0) goto loc_00A5B1BC;
    if (*(unsigned __int64 *)(v_rip + 4864409) == 0) goto loc_00A5B1D5;
    v_stack_m3B4 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4864409) + 4)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4864409) + 4)) * 2 * 8 + 8);
    if (((unsigned int)(v_rdi + 128)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4864409) + 4)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4864409) + 4)) * 2 * 8 + 8))) goto loc_00A589BB;
    goto loc_00A5B24F;
loc_00A5B6C1:
    a1 = (unsigned int)((1) - (250));
    if (condition_is_equal) goto loc_00A5B779;
    a1 = (unsigned int)((a1) - ((unsigned int)(v_r12)));
    if (condition_is_equal) goto loc_00A5B737;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5B737;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A5B710;
    if (a1 == ((unsigned int)(v_r12))) goto loc_00A5B6ED;
loc_00A5B6E3:
    goto loc_00A5B7BE;
loc_00A5B6ED:
    v_stack_m3C0 = v_stack_m3B4;
    v_stack_m3C8 = (unsigned int)(v_rdi + 128);
    result = SeCodeIntegrityQueryPolicyInformation(1, v_stack_m3A0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128);
    goto loc_00A5B773;
loc_00A5B710:
    v_stack_m3C0 = (unsigned __int8)(v_stack_m3B0);
    v_stack_m3C8 = v_stack_m3B4;
    result = ExpQueryRuntimeAttestationReport(v_stack_m3A0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m390))), v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B737:
    if (((unsigned int)(v_stack_m3B0)) != 253) goto loc_00A5B75C;
    if (((unsigned int)(v_rdi + 128)) >= 12) goto loc_00A5B75C;
    if (a6 == 0) goto loc_00A5B755;
    *(unsigned int *)(a6) = 12;
    goto loc_00A5B755;
loc_00A5B755:
    goto loc_00A5B7BE;
loc_00A5B75C:
    v_stack_m3C8 = (unsigned int)(v_stack_m3B0);
    a4 = 0;
loc_00A5B769:
    result = ExpGetProcessInformation(v_rdi + 128, (unsigned int)((unsigned int)(v_rdi + 128)), v_stack_m3B4, a4);
loc_00A5B773:
    v_stack_m3B8 = (unsigned int)(result);
    goto loc_00A5B79F;
loc_00A5B779:
    v_stack_m3B4 = 16;
    if (((unsigned int)(v_rdi + 128)) < 16) goto loc_00A589BB;
    if ((((unsigned __int8)(v_rdi + 128)) & (7)) != 0) goto loc_00A589BB;
    *(unsigned __int64 *)(v_rdi + 128) = v_xmm0;
loc_00A5B79F:
    if (a6 == 0) goto loc_00A5B7B1;
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(v_stack_m3B4));
    goto loc_00A5B7B1;
loc_00A5B7B1:
    goto loc_00A5B7BE;
loc_00A5B7B9:
loc_00A5B7BE:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)((unsigned int)(v_rdi + 128)), v_stack_m3B4, a4);
    v_rsp = (v_rsp) + (944);
    return result;
loc_00A5B7E2:
    result = ExRaiseDatatypeMisalignment(a1, (unsigned int)((unsigned int)(v_rdi + 128)), v_stack_m3B4, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpQuerySystemInformation(int32_t Arg1, int64_t Arg2, int32_t Arg3, void *Arg4, uint32_t Arg5, int64_t Arg6)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m1CC;
    uint32_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint8_t v_stack_m1EC;
    uint32_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint8_t v_stack_m1FC;
    uint64_t v_stack_m200;
    uint32_t v_stack_m204;
    uint8_t v_stack_m206;
    uint8_t v_stack_m207;
    uint64_t v_stack_m208;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint32_t v_stack_m228;
    uint32_t v_stack_m230;
    uint32_t v_stack_m238;
    uint16_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint16_t v_stack_m27E;
    uint16_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint32_t v_stack_m2AC;
    uint32_t v_stack_m2B0;
    uint32_t v_stack_m2B4;
    uint32_t v_stack_m2B8;
    uint32_t v_stack_m2BC;
    uint32_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint32_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint8_t v_stack_m302;
    uint32_t v_stack_m368;
    uint16_t v_stack_m370;
    uint64_t v_stack_m378;
    uint32_t v_stack_m380;
    uint32_t v_stack_m384;
    uint8_t v_stack_m388;
    uint32_t v_stack_m38C;
    uint32_t v_stack_m390;
    uint16_t v_stack_m394;
    uint32_t v_stack_m398;
    uint64_t v_stack_m3A0;
    uint32_t v_stack_m3A8;
    uint8_t v_stack_m3A9;
    uint8_t v_stack_m3AA;
    uint32_t v_stack_m3AC;
    uint8_t v_stack_m3B0;
    uint32_t v_stack_m3B4;
    uint32_t v_stack_m3B8;
    uint64_t v_stack_m3C0;
    uint64_t v_stack_m3C8;
    uint64_t v_stack_m40;
    uint64_t v_stack_m58;

    local_rsp = (local_rsp) - (944);
    result = (*(uint64_t *)(v_rip + 0x3B2ECC)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m390 = Arg3;
    v_stack_m3A0 = Arg2;
    v_stack_m378 = Arg6;
    local_rsi = 0;
    v_stack_m398 = 0;
    *(uint64_t *)(local_rsp - 0x270) = 0;
    v_stack_m2BC = 0;
    v_stack_m2B8 = 0;
    v_stack_m3A8 = 0;
    v_stack_m2AC = 0;
    v_stack_m370 = 0;
    v_stack_m394 = 0;
    v_stack_m248 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x2C8) = 0;
    v_stack_m3AC = 0;
    *(uint64_t *)(local_rsp - 0x290) = 0;
    *(uint64_t *)(local_rsp - 0x2A8) = 0;
    v_stack_m2B0 = 0;
    v_stack_m38C = 0;
    *(uint64_t *)(local_rsp - 0x258) = 0;
    result = 0;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x48) = 0;
    Arg2 = 0;
    result = memset(local_rsp - 520, Arg2, 432, Arg4);
    v_stack_m3B8 = 0;
    v_stack_m3B0 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00A57AC2;
    if (((uint32_t)((uint32_t)(Arg1))) > 157) goto loc_00A579F4;
    if (((uint32_t)((uint32_t)(Arg1))) == 157) goto loc_00A57A7C;
    if (((uint32_t)((uint32_t)(Arg1))) > 126) goto loc_00A579A8;
    if (((uint32_t)((uint32_t)(Arg1))) == 126) goto loc_00A57A7C;
    if (((uint32_t)((uint32_t)(Arg1))) == 5) goto loc_00A57A7C;
    if (((uint32_t)((uint32_t)(Arg1))) == 12) goto loc_00A57999;
    if (((uint32_t)((uint32_t)(Arg1))) == 17) goto loc_00A57A7C;
    if (((uint32_t)((uint32_t)(Arg1))) != 35) goto loc_00A57A7C;
loc_00A57985:
loc_00A5798B:
    goto loc_00A57A8E;
loc_00A57999:
    goto loc_00A57A88;
loc_00A579A8:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (133));
    if (condition_is_equal) goto loc_00A57A7C;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_00A57A7C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A57A7C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A57A82;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_00A5798B;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00A5798B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A57A82;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5798B;
    goto loc_00A57A82;
loc_00A579F4:
    if (((uint32_t)((uint32_t)(Arg1))) > 202) goto loc_00A57A45;
    if (((uint32_t)((uint32_t)(Arg1))) == 202) goto loc_00A5798B;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (158));
    if (condition_is_equal) goto loc_00A5798B;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00A57A82;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(2 + 1)));
    if (condition_is_equal) goto loc_00A5798B;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_00A5798B;
    Arg1 = (uint32_t)((Arg1) - (4));
    if (condition_is_equal) goto loc_00A57A82;
    Arg1 = (uint32_t)((Arg1) - (15));
    if (condition_is_equal) goto loc_00A57A82;
    Arg1 = (uint32_t)((Arg1) - (4));
    if (condition_is_equal) goto loc_00A57A82;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(2 + 1)));
    if (condition_is_equal) goto loc_00A57A82;
    goto loc_00A57A82;
loc_00A57A45:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (210));
    if (condition_is_equal) goto loc_00A57A7C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A57A7C;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_00A57A7C;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_00A57A7C;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_00A57985;
    Arg1 = (uint32_t)((Arg1) - (16));
    if (condition_is_equal) goto loc_00A57A82;
    Arg1 = (uint32_t)((Arg1) - (7));
    if (condition_is_equal) goto loc_00A57A82;
    Arg1 = (uint32_t)((Arg1) - (2));
    goto loc_00A57A82;
loc_00A57A7C:
loc_00A57A82:
loc_00A57A88:
loc_00A57A8E:
    result = ProbeForWrite(Arg4, (uint32_t)(Arg5), 4, Arg4);
    if (Arg6 != 0) {
        Arg1 = local_rsp;
        if (Arg6 < local_rsp) { Arg1 = Arg6; }
        result = *(uint32_t *)(Arg1);
        *(uint32_t *)(Arg1) = (uint32_t)(result);
    }
    goto loc_00A57ACF;
loc_00A57AC2:
loc_00A57ACF:
    v_stack_m3B4 = 0;
    v_stack_m2D0 = (uint32_t)((uint32_t)(0xFFFFULL));
    v_stack_m384 = 0;
    v_stack_m380 = 0;
    v_stack_m394 = 0;
    v_stack_m370 = 0;
    v_stack_m2A0 = 0;
    v_stack_m298 = 0;
    v_stack_m268 = 0;
    v_stack_m368 = 9;
    v_stack_m2B0 = 9;
    if (((uint32_t)((uint32_t)(Arg1))) > 100) goto loc_00A57BF6;
    if (((uint32_t)((uint32_t)(Arg1))) == 100) goto loc_00A57C64;
    if (((uint32_t)((uint32_t)(Arg1))) > 42) goto loc_00A57B73;
    if (((uint32_t)((uint32_t)(Arg1))) == 42) goto loc_00A57C64;
    if (((uint32_t)((uint32_t)(Arg1))) == ((uint32_t)(3 - 1))) goto loc_00A57BC0;
    if (((uint32_t)((uint32_t)(Arg1))) == 8) goto loc_00A57C64;
    if (((uint32_t)((uint32_t)(Arg1))) == 23) goto loc_00A57C64;
    if (((uint32_t)((uint32_t)(Arg1))) == 33) goto loc_00A57BC0;
    if (((uint32_t)((uint32_t)(Arg1))) == 36) goto loc_00A57BC0;
loc_00A57B64:
loc_00A57B69:
loc_00A57B6E:
    goto loc_00A57DA7;
loc_00A57B73:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (61));
    if (condition_is_equal) goto loc_00A57C64;
    Arg1 = (uint32_t)((Arg1) - (4));
    if (condition_is_equal) goto loc_00A57BC0;
    Arg1 = (uint32_t)((Arg1) - (7));
    if (condition_is_equal) goto loc_00A57B99;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A57C64;
    goto loc_00A57C26;
loc_00A57B99:
    if (((uint32_t)((uint32_t)(v_stack_m390))) != 4) goto loc_00A5B7B9;
    v_stack_m2B0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m3A0)));
    goto loc_00A57DA7;
loc_00A57BC0:
    v_stack_m380 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m390))));
    v_stack_m394 = (uint16_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m390))));
loc_00A57BCC:
    result = KeQueryActiveProcessorCountEx((uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), (uint32_t)(*(uint32_t *)(v_stack_m3A0)), 0, 0);
    v_stack_m384 = (uint32_t)(result);
    goto loc_00A57DA7;
loc_00A57BF6:
    if (((uint32_t)((uint32_t)(Arg1))) > 165) goto loc_00A57D01;
    if (((uint32_t)((uint32_t)(Arg1))) == 165) goto loc_00A57CC6;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (107));
    if (condition_is_equal) goto loc_00A57C9F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A57C64;
    Arg1 = (uint32_t)((Arg1) - (13));
    if (condition_is_equal) goto loc_00A57C2D;
    Arg1 = (uint32_t)((Arg1) - (20));
    if (condition_is_equal) goto loc_00A57C64;
loc_00A57C26:
    if (Arg1 == 19) goto loc_00A57C64;
    goto loc_00A57B64;
loc_00A57C2D:
    if (((uint32_t)((uint32_t)(v_stack_m390))) < ((uint32_t)(3 - 1))) goto loc_00A5B7B9;
    v_stack_m370 = (uint16_t)(*(uint16_t *)(v_stack_m3A0));
    if (v_stack_m370 >= ((uint16_t)(*(uint16_t *)(v_rip + 0x56D3B1)))) goto loc_00A5B7B9;
    goto loc_00A57DA7;
loc_00A57C64:
    if (((uint32_t)((uint32_t)(v_stack_m390))) < ((uint32_t)(3 - 1))) goto loc_00A5B7B9;
    v_stack_m380 = (uint32_t)(*(uint16_t *)(v_stack_m3A0));
    v_stack_m394 = (uint16_t)(*(uint16_t *)(v_stack_m3A0));
    result = KeQueryActiveGroupCount(v_stack_m3A0, (uint32_t)(v_stack_m368), 0, (uint32_t)((uint32_t)(result)));
    if (((uint16_t)((uint32_t)(v_stack_m380))) >= ((uint16_t)(result))) goto loc_00A5B7B9;
    goto loc_00A57BCC;
loc_00A57C9F:
    if (((uint32_t)((uint32_t)(v_stack_m390))) < 4) goto loc_00A5B7B9;
    v_stack_m2D0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m3A0)));
    goto loc_00A57DA7;
loc_00A57CC6:
    if ((uint32_t)((uint32_t)(v_stack_m390)) == 0) goto loc_00A57CF4;
    if (((uint32_t)((uint32_t)(v_stack_m390))) != 8) goto loc_00A5B7B9;
    v_stack_m2A0 = *(uint64_t *)(v_stack_m3A0);
    goto loc_00A57B6E;
loc_00A57CF4:
    v_stack_m2A0 = 0;
    goto loc_00A57B69;
loc_00A57D01:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (175));
    if (condition_is_equal) goto loc_00A57D81;
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(v_stack_m3A0)));
    if (condition_is_equal) goto loc_00A57D5B;
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(v_stack_m3A0)));
    if (condition_is_equal) goto loc_00A57D81;
    Arg2 = (uint32_t)((Arg2) - (49));
    if (condition_is_equal) goto loc_00A57D81;
    if (((uint32_t)(Arg2)) != 1) goto loc_00A57D4F;
    if (((uint32_t)((uint32_t)(v_stack_m390))) < 8) goto loc_00A5B7B9;
    v_stack_m3AC = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m3A0 + 0x4)));
    v_stack_m2D0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m3A0)));
loc_00A57D41:
    goto loc_00A57DA7;
loc_00A57D4F:
    goto loc_00A57B69;
loc_00A57D5B:
    if (((uint32_t)((uint32_t)(v_stack_m390))) != 8) goto loc_00A5B7B9;
    v_stack_m268 = *(uint64_t *)(v_stack_m3A0);
    goto loc_00A57D41;
loc_00A57D81:
    if (((uint32_t)((uint32_t)(v_stack_m390))) != 8) goto loc_00A5B7B9;
    v_stack_m298 = *(uint64_t *)(v_stack_m3A0);
loc_00A57DA7:
    if (((uint32_t)((uint32_t)(Arg1))) > 126) goto loc_00A59BC5;
    if (((uint32_t)((uint32_t)(Arg1))) == 126) goto loc_00A59B55;
    if (((uint32_t)((uint32_t)(Arg1))) > 64) goto loc_00A58BA1;
    if (((uint32_t)((uint32_t)(Arg1))) == 64) goto loc_00A58B3D;
    if (((uint32_t)((uint32_t)(Arg1))) > 25) goto loc_00A58300;
    if (((uint32_t)((uint32_t)(Arg1))) == 25) goto loc_00A59177;
    if (((uint32_t)((uint32_t)(Arg1))) > 12) goto loc_00A580A5;
    if (((uint32_t)((uint32_t)(Arg1))) == 12) goto loc_00A58051;
    if (((uint32_t)((uint32_t)(Arg1))) > 6) goto loc_00A57F4C;
    if (((uint32_t)((uint32_t)(Arg1))) == 6) goto loc_00A5AE6D;
    if ((uint32_t)((uint32_t)(Arg1)) == 0) goto loc_00A59732;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) - (1));
    if (condition_is_equal) goto loc_00A57F13;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00A57EC6;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00A57E28;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00A59177;
    goto loc_00A5880F;
loc_00A57E28:
    if (((uint32_t)((uint32_t)(Arg5))) <= 48) goto loc_00A57E49;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 48;
    goto loc_00A5B755;
loc_00A57E49:
    result = KeQueryBootTimeValues(v_stack_m200, v_stack_m208, v_stack_m1E8, (uint32_t)((uint32_t)(result)));
    result = PsGetCurrentServerSiloGlobals(v_stack_m200, v_stack_m208, v_stack_m1E8, (uint32_t)((uint32_t)(result)));
    v_stack_m1F8 = *(uint64_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B8);
    v_stack_m1F0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B0)));
    v_stack_m1E0 = *(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4C8) + 0x1B0)));
    result = memcpy(Arg4, v_stack_m208, (uint32_t)(Arg5), (uint32_t)((uint32_t)(result)));
loc_00A57EB7:
    v_stack_m3B4 = (uint32_t)((uint32_t)(Arg5));
    goto loc_00A5B79F;
loc_00A57EC6:
    if (((uint32_t)((uint32_t)(Arg5))) >= 312) goto loc_00A57EEA;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 376;
    goto loc_00A5B755;
loc_00A57EEA:
    local_rbx = 376;
    if (((uint32_t)((uint32_t)(Arg5))) <= 376) { local_rbx = (uint32_t)((uint32_t)(Arg5)); }
    result = ExpQuerySystemPerformanceInformation((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg4, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(result)));
    v_stack_m3B4 = (uint32_t)(local_rbx);
    goto loc_00A5B79F;
loc_00A57F13:
    if (((uint32_t)((uint32_t)(Arg5))) >= 12) goto loc_00A57F33;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 12;
    goto loc_00A5B755;
loc_00A57F33:
    result = ExpGetSystemProcessorInformation(Arg4, Arg4, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(result)));
loc_00A57F3B:
    v_stack_m3B8 = (uint32_t)(result);
    v_stack_m3B4 = 12;
    goto loc_00A5B79F;
loc_00A57F4C:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (7));
    if (condition_is_equal) goto loc_00A57FED;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A59D6C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A57FB3;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A59177;
    if (Arg1 != 1) goto loc_00A5B6E3;
    result = ExIsRestrictedCaller(v_stack_m3B0, v_stack_m38C, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(result)));
    if ((uint32_t)(result) != 0) goto loc_00A597E9;
    result = ExpQueryModuleInformation((uint32_t)(v_stack_m38C), Arg4, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m3B4);
    Arg2 = 0;
loc_00A57FA3:
    v_stack_m3B8 = (uint32_t)(result);
    result = EtwTiLogSyscallUsage((uint32_t)((uint32_t)(result)), Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m3B4);
    goto loc_00A5B79F;
loc_00A57FB3:
    if (((uint32_t)((uint32_t)(Arg5))) == 4) goto loc_00A57FD3;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 4;
    goto loc_00A5B755;
loc_00A57FD3:
    *(uint32_t *)(arg4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56C2E7)));
loc_00A57FDB:
    v_stack_m3B4 = 4;
    goto loc_00A5B79F;
loc_00A57FED:
    if (((uint32_t)((uint32_t)(Arg5))) == 24) goto loc_00A5800D;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 24;
    goto loc_00A5B755;
loc_00A5800D:
    *(uint32_t *)(arg4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x580825)));
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)(*(uint64_t *)(v_rip + 0x580820));
    *(uint32_t *)(arg4 + 0x8) = (uint32_t)(*(uint64_t *)(v_rip + 0x58081A));
    *(uint32_t *)(arg4 + 0xC) = (uint32_t)(*(uint64_t *)(v_rip + 0x580814));
    *(uint32_t *)(arg4 + 0x10) = (uint32_t)(*(uint64_t *)(v_rip + 0x580812));
    *(uint32_t *)(arg4 + 0x14) = (uint32_t)(*(uint64_t *)(v_rip + 0x58080C));
    goto loc_00A5ABF6;
loc_00A58051:
    if (((uint32_t)((uint32_t)(Arg5))) >= 56) goto loc_00A58071;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 56;
    goto loc_00A5B755;
loc_00A58071:
    result = ExIsRestrictedCaller(v_stack_m3B0, v_stack_m38C, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m3B4);
    if ((uint32_t)(result) != 0) goto loc_00A597E9;
    result = ExpGetLockInformation((uint32_t)(v_stack_m38C), Arg4, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m3B4);
    goto loc_00A57FA3;
loc_00A580A5:
    if (((uint32_t)(local_rbx)) > 18) goto loc_00A581A2;
    if (((uint32_t)(local_rbx)) == 18) goto loc_00A58198;
    local_rbx = (uint32_t)((local_rbx) - (13));
    if (condition_is_equal) goto loc_00A5818B;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5818B;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5818B;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5812C;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A5B6E3;
    if (((uint32_t)((uint32_t)(Arg5))) >= ((uint32_t)((uint32_t)(v_stack_m38C)))) goto loc_00A580F8;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = (uint32_t)((uint32_t)(v_stack_m38C));
    goto loc_00A5B755;
loc_00A580F8:
    result = ExIsRestrictedCaller(v_stack_m3B0, v_stack_m38C, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m3B4);
    if ((uint32_t)(result) != 0) goto loc_00A597E9;
    result = ExpGetObjectInformation((uint32_t)(v_stack_m38C), Arg4, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m3B4);
    goto loc_00A57FA3;
loc_00A5812C:
    if (((uint32_t)((uint32_t)(Arg5))) >= 32) goto loc_00A5814D;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 32;
    goto loc_00A5B755;
loc_00A5814D:
    if ((((uint8_t)(Arg4)) & (7)) != 0) goto loc_00A58B63;
    result = ExIsRestrictedCaller(v_stack_m3B0, v_stack_m38C, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m3B4);
    if ((uint32_t)(result) != 0) goto loc_00A597E9;
    result = ExpGetHandleInformation((uint32_t)(v_stack_m38C), Arg4, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m3B4);
    goto loc_00A57FA3;
loc_00A5818B:
    v_stack_m3B8 = 0xC0000002ULL;
    goto loc_00A5B79F;
loc_00A58198:
    goto loc_00A59FAB;
loc_00A581A2:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (19));
    if (condition_is_equal) goto loc_00A5818B;
    Arg2 = (uint32_t)((Arg2) - (32));
    if (condition_is_equal) goto loc_00A59854;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00A582CA;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00A5821F;
    if (((uint32_t)(Arg2)) != 1) goto loc_00A5B6E3;
    if (((uint32_t)((uint32_t)(Arg5))) == 20) goto loc_00A581E9;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 20;
    goto loc_00A5B755;
loc_00A581E9:
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56CED1)));
    *(uint32_t *)(arg4 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56CEF0)));
    *(uint32_t *)(arg4 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56CEC3)));
    *(uint32_t *)(arg4 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56CF96)));
loc_00A5820D:
    v_stack_m3B4 = 20;
    goto loc_00A5B79F;
loc_00A5821F:
    result = (uint32_t)((v_stack_m3B4 + v_stack_m3B4 * 2) << (3));
    v_stack_m3B4 = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(Arg5))) >= ((uint32_t)(result))) goto loc_00A58245;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = (uint32_t)(result);
    goto loc_00A5B755;
loc_00A58245:
    v_stack_m3A8 = 0;
loc_00A58253:
    v_stack_m2D8 = Arg4;
    if (0 >= ((uint32_t)(v_stack_m3B4))) goto loc_00A5869E;
    v_stack_m3AC = (uint16_t)(v_stack_m3A0);
    v_stack_m3AA = 0;
    v_stack_m3A9 = 0;
    result = KeGetProcessorIndexFromNumber(v_stack_m3AC, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m3B4);
    *(uint32_t *)(arg4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x5709ED + (uint32_t)((uint32_t)(result)) * 8) + 0x2D3C)));
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x5709ED + (uint32_t)((uint32_t)(result)) * 8) + 0x385C)));
    *(uint32_t *)(arg4 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x5709ED + (uint32_t)((uint32_t)(result)) * 8) + 0x38AC)));
    *(uint32_t *)(arg4 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56E8D8)));
    *(uint32_t *)(arg4 + 0x10) = 0;
    *(uint32_t *)(arg4 + 0x14) = 0;
    local_rdi = (Arg4) + (24);
    local_r14 = (uint32_t)((0) + ((uint32_t)(3 - 2)));
    v_stack_m3A8 = (uint32_t)(local_r14);
    goto loc_00A58253;
loc_00A582CA:
    if (((uint32_t)(local_r14)) >= 48) goto loc_00A582EB;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 48;
    goto loc_00A5B755;
loc_00A582EB:
    result = ExGetPoolTagInfo(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4, (uint32_t)(v_stack_m384));
    goto loc_00A5B773;
loc_00A58300:
    if (((uint32_t)(v_rip + 5704173)) > 50) goto loc_00A587E3;
    if (((uint32_t)(v_rip + 5704173)) == 50) goto loc_00A587AC;
    if (((uint32_t)(v_rip + 5704173)) > 36) goto loc_00A5854D;
    if (((uint32_t)(v_rip + 5704173)) == 36) goto loc_00A58495;
    local_rbx = (uint32_t)((v_rip + 5704173) - (28));
    if (condition_is_equal) goto loc_00A58407;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A59177;
    local_rbx = (uint32_t)((local_rbx) - (48));
    if (condition_is_equal) goto loc_00A583ED;
    local_rbx = (uint32_t)((local_rbx) - (48));
    if (condition_is_equal) goto loc_00A5837D;
    if (((uint32_t)(local_rbx)) != 48) goto loc_00A5B6E3;
    if (((uint32_t)(local_r14)) >= 48) goto loc_00A58362;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 48;
    goto loc_00A5B755;
loc_00A58362:
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(v_rip + 0x4EF290));
    *(uint8_t *)(local_rdi + 0x1) = (uint8_t)(*(uint8_t *)(v_rip + 0x4EF26C));
    goto loc_00A59A32;
loc_00A5837D:
    if (((uint32_t)(local_r14)) >= 16) goto loc_00A5839D;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 16;
    goto loc_00A5B755;
loc_00A5839D:
    v_stack_m3B4 = 16;
    if ((uint32_t)((uint32_t)(v_stack_m384)) == 0) goto loc_00A583D7;
    v_stack_m3A8 = (uint32_t)((uint32_t)(v_stack_m384));
loc_00A583BE:
    Arg2 = (uint32_t)((0) + (*(uint32_t *)(*(uint64_t *)(v_rip + 0x57088A) + 0x8BB8)));
    Arg3 = (uint32_t)((0) + (*(uint32_t *)(*(uint64_t *)(v_rip + 0x57088A) + 0x8670)));
    local_r10 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m384)))) - (3 - 2);
    if (condition_is_not_equal) goto loc_00A583BE;
loc_00A583D7:
    *(uint32_t *)(local_rdi) = (uint32_t)(Arg2);
    *(uint32_t *)(local_rdi + 0x4) = Arg3;
    *(uint32_t *)(local_rdi + 0x8) = 0;
    *(uint32_t *)(local_rdi + 0xC) = 0;
    goto loc_00A5B79F;
loc_00A583ED:
    result = EtwQueryPerformanceTraceInformation(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B0, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A58407:
    if (((uint32_t)(local_r14)) == 12) goto loc_00A5842D;
    if (((uint32_t)(local_r14)) == 24) goto loc_00A5842D;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 12;
    goto loc_00A5B755;
loc_00A5842D:
    result = ExAcquireTimeRefreshLockShared(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B0, v_stack_m3B4);
    result = ExReleaseTimeRefreshLockShared(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B0, v_stack_m3B4);
    if (((uint32_t)(local_r14)) != 24) goto loc_00A58463;
    *(uint64_t *)(local_rdi) = *(uint64_t *)(v_rip + 0x56EC37);
    *(uint64_t *)(local_rdi + 0x8) = result;
    *(uint8_t *)(local_rdi + 0x10) = (uint8_t)(*(uint8_t *)(v_rip + 0x56CBD7));
    goto loc_00A5848B;
loc_00A58463:
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0x56E637))) * (*(uint64_t *)(local_rdi));
    Arg2 = 0;
    *(uint32_t *)(local_rdi) = (uint32_t)(result);
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56E61C)));
    *(uint8_t *)(local_rdi + 0x8) = (uint8_t)(*(uint8_t *)(v_rip + 0x56CBD7));
loc_00A5848B:
    goto loc_00A57EB7;
loc_00A58495:
    if (((uint32_t)(local_r14)) >= 48) goto loc_00A584B6;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 48;
    goto loc_00A5B755;
loc_00A584B6:
    if ((uint32_t)(v_stack_m3B4) == 0) goto loc_00A584DE;
    v_stack_m3A8 = (uint32_t)(v_stack_m3B4);
loc_00A584CC:
    Arg2 = (uint32_t)((0) + (*(uint32_t *)(*(uint64_t *)(v_rip + 0x57077C) + 0x2D3C)));
    Arg3 = ((uint32_t)((uint32_t)(v_stack_m3B4))) - (3 - 2);
    if (condition_is_not_equal) goto loc_00A584CC;
loc_00A584DE:
    *(uint32_t *)(local_rdi) = (uint32_t)(Arg2);
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4CACDA)));
    *(uint32_t *)(local_rdi + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4CACD9)));
    *(uint32_t *)(local_rdi + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4CACCC)));
    *(uint32_t *)(local_rdi + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4CACCB)));
    *(uint32_t *)(local_rdi + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4CACC6)));
    *(uint32_t *)(local_rdi + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4CACC5)));
    *(uint32_t *)(local_rdi + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4CACB8)));
    *(uint32_t *)(local_rdi + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4CACB7)));
    *(uint32_t *)(local_rdi + 0x24) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4CACB2)));
    *(uint32_t *)(local_rdi + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4CACAD)));
    *(uint32_t *)(local_rdi + 0x2C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4CACA8)));
    goto loc_00A59A32;
loc_00A5854D:
    local_rbx = (uint32_t)((*(uint64_t *)(v_rip + 0x56EC37)) - (37));
    if (condition_is_equal) goto loc_00A58773;
    local_rbx = (uint32_t)((local_rbx) - (5));
    if (condition_is_equal) goto loc_00A586E3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A586AC;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5858B;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A5B6E3;
    result = ExpGetLookasideInformation(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5858B:
    if (((uint32_t)(local_r14)) >= 172) goto loc_00A585AC;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 172;
    goto loc_00A5B755;
loc_00A585AC:
    result = PsGetCurrentServerSiloGlobals(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4, v_stack_m3B4);
    result = ExAcquireTimeRefreshLockShared(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4, v_stack_m3B4);
    *(uint64_t *)(v_stack_m208) = v_xmm0;
    *(uint64_t *)(v_stack_m208 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_m208 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_m208 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_m208 + 0x40) = v_xmm0;
    *(uint64_t *)(v_stack_m208 + 0x50) = v_xmm1;
    *(uint64_t *)(v_stack_m208 + 0x60) = v_xmm0;
    Arg1 = (v_stack_m208) + (128);
    *(uint64_t *)(Arg1 - 0x10) = v_xmm0;
    local_rbx = (*(uint64_t *)(result + 0x4C8)) + (128);
    *(uint64_t *)(Arg1) = v_xmm1;
    *(uint64_t *)(Arg1 + 0x10) = v_xmm0;
    *(uint64_t *)(Arg1 + 0x20) = *(uint64_t *)(local_rbx + 0x20);
    *(uint32_t *)(Arg1 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x28)));
    result = ExReleaseTimeRefreshLockShared(Arg1, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4, v_stack_m3B4);
    *(uint64_t *)(local_rdi) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x10) = v_xmm1;
    *(uint64_t *)(local_rdi + 0x20) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x30) = v_xmm1;
    *(uint64_t *)(local_rdi + 0x40) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x50) = v_xmm1;
    *(uint64_t *)(local_rdi + 0x60) = v_xmm0;
    local_rdi = (local_rdi) + (128);
    *(uint64_t *)(local_rdi - 0x10) = v_xmm1;
    Arg1 = (v_stack_m208) + (128);
    *(uint64_t *)(local_rdi) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x10) = v_xmm1;
    *(uint64_t *)(local_rdi + 0x20) = *(uint64_t *)(Arg1 + 0x20);
    *(uint32_t *)(local_rdi + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x28)));
    v_stack_m3B4 = 172;
loc_00A5869E:
    v_stack_m3B8 = 0;
    goto loc_00A5B79F;
loc_00A586AC:
    if (128 >= 24) goto loc_00A586CC;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 24;
    goto loc_00A5B755;
loc_00A586CC:
    v_stack_m3B4 = 128;
    result = ExpQueryLegacyDriverInformation(local_rdi, v_stack_m3B4, v_stack_m3B4, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A586E3:
    result = (uint32_t)((v_stack_m3B4 + v_stack_m3B4 * 2) << (4));
    v_stack_m3B4 = (uint32_t)(result);
    if (128 < ((uint32_t)(result))) goto loc_00A589BB;
loc_00A586FF:
    v_stack_m3A8 = 0;
    v_stack_m2D8 = local_rdi;
    if (0 >= ((uint32_t)(v_stack_m3B4))) goto loc_00A5B79F;
    v_stack_m3AC = (uint16_t)(local_r10);
    v_stack_m3AA = 0;
    v_stack_m3A9 = 0;
    Arg3 = 0;
    result = PoGetIdleTimes(v_stack_m3AC, v_stack_m208, Arg3, v_stack_m3B4);
    *(uint64_t *)(local_rdi) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x10) = v_xmm1;
    *(uint64_t *)(local_rdi + 0x20) = v_xmm0;
    local_rdi = (local_rdi) + (48);
    local_rbx = (uint32_t)((0) + ((uint32_t)(3 - 2)));
    goto loc_00A586FF;
loc_00A58773:
    if (128 >= 16) goto loc_00A58793;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 16;
    goto loc_00A5B755;
loc_00A58793:
    result = CmQueryRegistryQuotaInformation(local_rdi, v_stack_m208, Arg3, (uint32_t)(v_stack_m384));
    v_stack_m3B8 = (uint32_t)(result);
    v_stack_m3B4 = 16;
    goto loc_00A5B79F;
loc_00A587AC:
    if (128 == 8) goto loc_00A587CC;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 8;
    goto loc_00A5B755;
loc_00A587CC:
    *(uint64_t *)(local_rdi) = result;
    goto loc_00A5B0A7;
loc_00A587E3:
    if (((uint32_t)(local_rbx)) > 58) goto loc_00A58931;
    if (((uint32_t)(local_rbx)) == 58) goto loc_00A58900;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (51));
    if (condition_is_equal) goto loc_00A588BD;
    Arg1 = (uint32_t)((Arg1) - (48));
    if (condition_is_equal) goto loc_00A5884E;
    Arg1 = (uint32_t)((Arg1) - (48));
    if (condition_is_equal) goto loc_00A58839;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5881A;
loc_00A5880F:
    if (Arg1 == 1) goto loc_00A5B737;
    goto loc_00A5B6E3;
loc_00A5881A:
    v_stack_m3C8 = v_stack_m3B4;
    result = PfSnQueryPrefetcherInformation(Arg1, local_rdi, 128, v_stack_m3B0);
    goto loc_00A5B773;
loc_00A58839:
    result = ExpQueryNumaProcessorMap(local_rdi, 128, v_stack_m3B4, v_stack_m3B0);
    goto loc_00A5B773;
loc_00A5884E:
    if (128 >= 16) goto loc_00A5886E;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 16;
    goto loc_00A5B755;
loc_00A5886E:
    v_stack_m2AC = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)));
    v_stack_m220 = *(uint64_t *)(local_rdi + 0x8);
    v_stack_m238 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    result = ProbeForWrite(*(uint64_t *)(local_rdi + 0x8), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)))), 4, v_stack_m3B0);
    v_stack_m3C8 = 5;
    goto loc_00A5B769;
loc_00A588BD:
    if (v_stack_m3B0 == 0) goto loc_00A5AE6D;
    if (128 >= 144) goto loc_00A588E8;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 144;
    goto loc_00A5B755;
loc_00A588E8:
    Arg4 = 0;
loc_00A588EB:
    result = VfGetVerifierInformation((uint32_t)(*(uint32_t *)(local_rdi + 0x4)), 128, v_stack_m3B4, Arg4);
    goto loc_00A5B773;
loc_00A58900:
    if (128 >= 4) goto loc_00A58920;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 4;
    goto loc_00A5B755;
loc_00A58920:
    result = KeGetRecommendedSharedDataAlignment((uint32_t)(*(uint32_t *)(local_rdi + 0x4)), 128, v_stack_m3B4, Arg4);
    *(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0x4))) = (uint32_t)(result);
    goto loc_00A57FDB;
loc_00A58931:
    local_rbx = (uint32_t)((*(uint64_t *)(local_rdi + 0x8)) - (59));
    if (condition_is_equal) goto loc_00A58AE8;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A58AD3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A589AB;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A58983;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A5B6E3;
    if (128 >= 12) goto loc_00A58976;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 12;
    goto loc_00A5B755;
loc_00A58976:
    result = ExpGetSystemEmulationProcessorInformation((uint32_t)(*(uint32_t *)(local_rdi + 0x4)), 128, v_stack_m3B4, Arg4);
    goto loc_00A57F3B;
loc_00A58983:
    if (128 == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4))))) goto loc_00A5899E;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    goto loc_00A5B755;
loc_00A5899E:
    result = ExpGetSystemEmulationBasicInformation((uint32_t)(*(uint32_t *)(local_rdi + 0x4)), 128, v_stack_m3B4, Arg4);
    goto loc_00A59755;
loc_00A589AB:
    result = (uint32_t)((Arg4 + Arg4 * 4) << (4));
    v_stack_m3B4 = (uint32_t)(result);
    if (128 >= ((uint32_t)(result))) goto loc_00A589CB;
loc_00A589BB:
    v_stack_m3B8 = (uint32_t)((uint32_t)(0xC0000004ULL));
    goto loc_00A5B79F;
loc_00A589CB:
    v_stack_m2D8 = (uint32_t)(*(uint32_t *)(local_rdi + 0x4));
    v_stack_m3A8 = 0;
loc_00A589E7:
    if (0 >= 0) goto loc_00A5B79F;
    v_stack_m3AC = (uint16_t)((uint32_t)(v_stack_m380));
    v_stack_m3AA = 0;
    v_stack_m3A9 = 0;
    result = KeGetProcessorIndexFromNumber(v_stack_m3AC, 128, v_stack_m3B4, Arg4);
    v_stack_m378 = *(uint64_t *)(v_rip + 0x57025F + (uint32_t)((uint32_t)(result)) * 8);
    Arg3 = 0;
    result = PoGetPerfStateAndParkingInfo(v_stack_m3AC, v_stack_m208, Arg3, v_stack_m270);
    Arg2 = 0;
    result = memset((uint32_t)(*(uint32_t *)(local_rdi + 0x4)), Arg2, 80, v_stack_m270);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m378 + 0x8648))) + (*(uint32_t *)(v_stack_m378 + 0x8644)));
    Arg1 = (Arg1) * ((uint32_t)(*(uint32_t *)(v_rip + 0x56E05A)));
    *(uint64_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)) + 0x28) = Arg1;
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m378 + 0x18) + 0x28C))) * ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56E05A)))));
    *(uint64_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)) + 0x30) = Arg1;
    result = *(uint64_t *)(v_stack_m378 + 0x18);
    if (v_stack_m1EC != 0) {
        result = v_stack_m200;
        *(uint8_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0x4))) = (uint8_t)(result);
        result = v_stack_m1FC;
        *(uint8_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)) + 0x7) = (uint8_t)(result);
        result = v_stack_m1F8;
        *(uint8_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)) + 0x8) = (uint8_t)(result);
        *(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)) + 0xC) = (uint32_t)((uint32_t)(0xC0000004ULL));
    }
    *(uint64_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)) + 0x48) = v_stack_m270;
    local_rdi = ((uint32_t)(*(uint32_t *)(local_rdi + 0x4))) + (80);
    v_stack_m2D8 = local_rdi;
    local_r12 = (uint32_t)((0) + ((uint32_t)((uint32_t)(0xC0000004ULL))));
    v_stack_m3A8 = (uint32_t)(local_r12);
    goto loc_00A589E7;
loc_00A58AD3:
    result = ExpQueryNumaAvailableMemory(local_rdi, 80, v_stack_m3B4, (uint32_t)(v_stack_m384));
    goto loc_00A5B773;
loc_00A58AE8:
    if (80 == 4) goto loc_00A58B08;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 4;
    goto loc_00A5B755;
loc_00A58B08:
    if ((*(uint32_t *)(result)) != -1) goto loc_00A58B28;
    result = ExpReadComPlusPackage(local_rdi, 80, v_stack_m3B4, (uint32_t)(v_stack_m384));
    v_stack_m3B8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A5B7BE;
loc_00A58B28:
    *(uint32_t *)(local_rdi) = (uint32_t)(result);
    goto loc_00A57FDB;
loc_00A58B3D:
    if (80 >= 56) goto loc_00A58B5D;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 56;
    goto loc_00A5B755;
loc_00A58B5D:
    if ((((uint8_t)(local_rdi)) & (7)) == 0) goto loc_00A58B6D;
loc_00A58B63:
    goto loc_00A5B7BE;
loc_00A58B6D:
    result = ExIsRestrictedCaller(v_stack_m3B0, v_stack_m38C, v_stack_m3B4, (uint32_t)(v_stack_m384));
    if ((uint32_t)(result) != 0) goto loc_00A597E9;
    result = ExpGetHandleInformationEx((uint32_t)(v_stack_m38C), local_rdi, 80, v_stack_m3B4);
    goto loc_00A57FA3;
loc_00A58BA1:
    if (((uint32_t)(v_rip + 5702239)) > 99) goto loc_00A591E6;
    if (((uint32_t)(v_rip + 5702239)) == 99) goto loc_00A591DC;
    if (((uint32_t)(v_rip + 5702239)) > 80) goto loc_00A58E33;
    if (((uint32_t)(v_rip + 5702239)) == 80) goto loc_00A58E15;
    if (((uint32_t)(v_rip + 5702239)) > 70) goto loc_00A58CE3;
    if (((uint32_t)(v_rip + 5702239)) == 70) goto loc_00A58CB1;
    local_rbx = (uint32_t)((v_rip + 5702239) - (65));
    if (condition_is_equal) goto loc_00A58C5D;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A58C08;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5B6E3;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5B6E3;
loc_00A58BF2:
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A5B6E3;
loc_00A58BFB:
    v_stack_m3B8 = 0xC00000BBULL;
    goto loc_00A5B79F;
loc_00A58C08:
    if (80 >= 32) goto loc_00A58C29;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 32;
    goto loc_00A5B755;
loc_00A58C29:
    result = ExIsRestrictedCaller(v_stack_m3B0, v_stack_m38C, 80, v_stack_m3B4);
    if ((uint32_t)(result) != 0) goto loc_00A597E9;
    result = ExGetBigPoolInfo((uint32_t)(v_stack_m38C), local_rdi, 80, v_stack_m3B4);
    goto loc_00A57FA3;
loc_00A58C5D:
    if (80 >= 4) goto loc_00A58C7D;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 4;
    goto loc_00A5B755;
loc_00A58C7D:
    if ((uint32_t)(v_stack_m3B4) == 0) goto loc_00A58CA5;
    v_stack_m3A8 = (uint32_t)(v_stack_m3B4);
loc_00A58C93:
    Arg2 = (uint32_t)((0) + (*(uint32_t *)(*(uint64_t *)(v_rip + 0x56FFB5) + 0x87FC)));
    Arg3 = ((uint32_t)((uint32_t)(v_stack_m3B4))) - ((uint32_t)(0xC0000004ULL));
    if (condition_is_not_equal) goto loc_00A58C93;
loc_00A58CA5:
    *(uint32_t *)(local_rdi) = (uint32_t)(Arg2);
    goto loc_00A57FDB;
loc_00A58CB1:
    if (80 == 4) goto loc_00A58CD1;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 4;
    goto loc_00A5B755;
loc_00A58CD1:
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3B26AD)));
    goto loc_00A57FDB;
loc_00A58CE3:
    local_rbx = (uint32_t)((local_rbx) - (72));
    if (condition_is_equal) goto loc_00A58DB7;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A58D95;
    local_rbx = (uint32_t)((local_rbx) - (3));
    if (condition_is_equal) goto loc_00A58D77;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A58D27;
    if (((uint32_t)(local_rbx)) != 32) goto loc_00A5B6E3;
    v_stack_m3C8 = v_stack_m3B4;
    result = PfQuerySuperfetchInformation(v_rip + 5701557 + 8, local_rdi, 80, v_stack_m3B0);
    goto loc_00A5B773;
loc_00A58D27:
    result = ExIsRestrictedCaller((uint8_t)(v_stack_m3B0), v_stack_m38C, 80, v_stack_m3B0);
    if ((uint32_t)(result) != 0) goto loc_00A597E9;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x580DD8), (uint8_t)(v_stack_m3B0), 80, v_stack_m3B0);
    Arg4 = ((uint8_t)(result) == 0) ? 1 : 0;
    v_stack_m3C8 = v_stack_m3B4;
    result = ExpQueryModuleInformationEx((uint32_t)(v_stack_m38C), local_rdi, 80, Arg4);
    goto loc_00A57FA3;
loc_00A58D77:
    result = ExpGetSystemFirmwareTableInformation(local_rdi, v_stack_m3B0, 80, v_stack_m3B4);
    goto loc_00A57FA3;
loc_00A58D95:
    result = KeBuildLogicalProcessorSystemInformation((uint16_t)((uint32_t)(v_stack_m380)), local_rdi, 80, v_stack_m3B4);
    v_stack_m3B8 = (uint32_t)(result);
    goto loc_00A5B79F;
loc_00A58DB7:
    if (80 != 8) goto loc_00A5B7B9;
    Arg2 = (uint32_t)((local_rdi) - (7));
    if (condition_is_equal) goto loc_00A58DEF;
    if (((uint32_t)(Arg2)) == 1) goto loc_00A58DD5;
    goto loc_00A5B7BE;
loc_00A58DD5:
    *(uint32_t *)(local_rdi) = 8;
    result = guard_dispatch_icall((uint16_t)((uint32_t)(v_stack_m380)), Arg2, 80, v_stack_m3B4);
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)((uint8_t)(result));
    goto loc_00A58E0B;
loc_00A58DEF:
    *(uint32_t *)(local_rdi) = 7;
    Arg1 = ((*(uint64_t *)(v_rip + 0x3A7D33)) != (v_rip - 5621758)) ? 1 : 0;
    *(uint32_t *)(local_rdi + 0x4) = Arg1;
loc_00A58E0B:
    goto loc_00A5B0A7;
loc_00A58E15:
    v_stack_m3C8 = v_stack_m3B4;
    Arg1 = (Arg1) | (-1);
    result = MmQueryMemoryListInformation(Arg1, local_rdi, 80, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A58E33:
    if (((uint32_t)(v_stack_m3B0)) > 90) goto loc_00A5914C;
    if (((uint32_t)(v_stack_m3B0)) == 90) goto loc_00A590EC;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m3B0))) - (81));
    if (condition_is_equal) goto loc_00A59854;
    Arg2 = (uint32_t)((Arg2) - (32));
    if (condition_is_equal) goto loc_00A59029;
    Arg2 = (uint32_t)((Arg2) - (3));
    if (condition_is_equal) goto loc_00A59014;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00A58FE2;
    if (((uint32_t)(Arg2)) != 1) goto loc_00A5B6E3;
    result = 0;
    v_stack_m288 = v_xmm0;
    v_stack_m278 = 0;
    v_stack_m3B4 = 24;
    if (80 != 24) goto loc_00A589BB;
    v_stack_m288 = v_xmm0;
    v_stack_m278 = v_xmm1;
    if (v_stack_m280 != 0) goto loc_00A5B7B9;
    result = (v_stack_m280) >> (16);
    if ((((uint8_t)((uint32_t)(0xC0000004ULL))) & ((uint8_t)(result))) != 0) goto loc_00A5B7B9;
    if (v_stack_m3B0 == 0) goto loc_00A58F1E;
    if ((uint16_t)(result) == 0) goto loc_00A58F17;
    if (((v_stack_m278) & ((uint8_t)((uint32_t)(0xC0000004ULL)))) != 0) goto loc_00A5B7E2;
    Arg2 = (v_stack_m27E) + (v_stack_m278);
    if (Arg2 > result) goto loc_00A58F15;
    if (Arg2 < v_stack_m278) {
        result = *(uint8_t *)(result);
    }
    goto loc_00A58F1E;
loc_00A58F1E:
    v_stack_m2C0 = (uint32_t)(v_stack_m27E);
    result = (v_stack_m27E) | (-1);
    result = PsLookupProcessByProcessId(v_stack_m288, v_stack_m2C8, 80, v_stack_m3B4);
    if (!sign_flag) goto loc_00A58F6E;
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m2C8, 80, v_stack_m3B4);
    goto loc_00A5B7BE;
loc_00A58F6E:
    result = PsQueryFullProcessImageName(v_stack_m2C8, local_rdi + 8, v_stack_m278, v_stack_m2C0);
    v_stack_m3B8 = (uint32_t)(result);
    result = ObfDereferenceObjectWithTag(v_stack_m2C8, (uint32_t)(0x746C6644ULL), v_stack_m278, v_stack_m2C0);
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x746C6644ULL), v_stack_m278, v_stack_m2C0);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)((uint32_t)(0xC0000004ULL)))) goto loc_00A5B79F;
    *(uint16_t *)(local_rdi + 0xA) = (uint16_t)((uint32_t)(v_stack_m2C0));
    goto loc_00A5B79F;
loc_00A58FE2:
    v_stack_m3B4 = 8;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 8) goto loc_00A589BB;
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56DC2E)));
    Arg1 = ((*(uint32_t *)(v_rip + 0x56C120)) != 0) ? 1 : 0;
    *(uint32_t *)(local_rdi + 0x4) = Arg1;
    goto loc_00A5B79F;
loc_00A59014:
    result = ObQueryRefTraceInformation(local_rdi, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m3B4, v_stack_m2C0);
    goto loc_00A5B773;
loc_00A59029:
    Arg4 = (uint32_t)((v_stack_m2C0) << (3));
    v_stack_m3B4 = (uint32_t)(Arg4);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) < 8) goto loc_00A590DF;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) >= ((uint32_t)(Arg4))) goto loc_00A5904A;
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) >> (3));
    goto loc_00A5904F;
loc_00A5904A:
loc_00A5904F:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (0xC0000004ULL));
    v_stack_m2D8 = local_rdi;
    result = KeFlushProcessWriteBuffers(1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m3B4, Arg4);
loc_00A5907D:
    v_stack_m3A8 = 0;
    if (0 >= ((uint32_t)((uint32_t)(v_stack_m384)))) goto loc_00A590D5;
    v_stack_m3AC = (uint16_t)((uint32_t)(v_stack_m380));
    v_stack_m3AA = 0;
    v_stack_m3A9 = 0;
    result = KeGetProcessorIndexFromNumber(v_stack_m3AC, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m3B4, Arg4);
    *(uint64_t *)(v_stack_m2D8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x56FBC7 + (uint32_t)((uint32_t)(result)) * 8) + 0x18) + 0x48);
    result = (v_stack_m2D8) + (8);
    v_stack_m2D8 = result;
    result = (uint32_t)(((uint32_t)(v_stack_m3A8)) + (1));
    goto loc_00A5907D;
loc_00A590D5:
    v_stack_m3B8 = (uint32_t)(local_r14);
    goto loc_00A5B79F;
loc_00A590DF:
    v_stack_m3B8 = 0xC0000023ULL;
    goto loc_00A5B79F;
loc_00A590EC:
    v_stack_m3B4 = 32;
    if (((uint32_t)(local_r14)) >= 20) goto loc_00A59113;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 32;
    goto loc_00A5B755;
loc_00A59113:
    *(uint64_t *)(v_rip + 0x56FBC7) = v_xmm0;
    *(uint32_t *)(v_rip + 0x56FBC7 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4A5F2C)));
    if (((uint32_t)(local_r14)) < v_stack_m3B4) goto loc_00A5820D;
    *(uint64_t *)(v_rip + 0x56FBC7 + 0x18) = *(uint64_t *)(v_rip + 0x4A5F1F);
    goto loc_00A5B79F;
loc_00A5914C:
    local_rbx = (uint32_t)((1) - (91));
    if (condition_is_equal) goto loc_00A591C7;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A59181;
    local_rbx = (uint32_t)((local_rbx) - (3));
    if (condition_is_equal) goto loc_00A5AE6D;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A59177;
    if (((uint32_t)(local_rbx)) != 32) goto loc_00A5B6E3;
    goto loc_00A5AE30;
loc_00A59177:
    goto loc_00A5B7BE;
loc_00A59181:
    if (v_stack_m3B0 == 0) goto loc_00A5AE6D;
    if (((uint32_t)(local_r14)) == 40) goto loc_00A591AD;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 40;
    goto loc_00A5B755;
loc_00A591AD:
    result = VfGetVerifierInformationEx(v_rip + 5700551, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m3B4, Arg4);
    v_stack_m3B8 = (uint32_t)(result);
    result = (uint32_t)((result) >> (31));
    result = (uint32_t)((result) & (0xFFFFFFD8ULL));
    result = (uint32_t)((result) + (40));
    goto loc_00A59EB4;
loc_00A591C7:
    result = HvlQueryEnlightenmentInfo(v_rip + 5700551, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A591DC:
    goto loc_00A5AE30;
loc_00A591E6:
    if (((uint32_t)(local_rbx)) > 114) goto loc_00A59766;
    if (((uint32_t)(local_rbx)) == 114) goto loc_00A59732;
    if (((uint32_t)(local_rbx)) > 106) goto loc_00A59573;
    if (((uint32_t)(local_rbx)) == 106) goto loc_00A59566;
    local_rbx = (uint32_t)((local_rbx) - (100));
    if (condition_is_equal) goto loc_00A5946E;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A59459;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5931F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5930A;
    if (((uint32_t)(local_rbx)) != 32) goto loc_00A5B6E3;
    Arg3 = 0;
    Arg2 = 0;
    result = guard_dispatch_icall(Arg2 + 23, Arg2, Arg3, v_stack_m398);
    v_stack_m3B8 = (uint32_t)(result);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000004ULL)))) goto loc_00A58BFB;
    if (((uint32_t)(local_r14)) < v_stack_m398) goto loc_00A59301;
    if (v_rip + 5700551 == 0) goto loc_00A59301;
    if ((uint8_t)(v_stack_m3B0) == 0) goto loc_00A5929F;
    result = ExAllocatePool2(257, (uint32_t)(v_stack_m398), (uint32_t)(0x6F666E49ULL), v_stack_m398);
    v_stack_m3A0 = result;
    if (result != 0) goto loc_00A592A7;
    goto loc_00A594F9;
loc_00A5929F:
    v_stack_m3A0 = v_rip + 5700551;
loc_00A592A7:
    result = guard_dispatch_icall(23, (uint32_t)(v_stack_m398), v_rip + 5700551, v_stack_m3B4);
    v_stack_m3B8 = (uint32_t)(result);
    if ((uint8_t)(v_stack_m3B0) == 0) goto loc_00A5B79F;
    if (sign_flag) goto loc_00A592F4;
    result = memcpy(v_rip + 5700551, v_rip + 5700551, (uint32_t)(v_stack_m3B4), v_stack_m3B4);
    goto loc_00A592F4;
loc_00A592F4:
    goto loc_00A5955C;
loc_00A59301:
    goto loc_00A59EB4;
loc_00A5930A:
    result = SeCodeIntegrityQueryInformation(v_rip + 5700551, (uint32_t)((uint32_t)(v_rip + 5700551)), v_stack_m3B4, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5931F:
    if (((uint32_t)(v_rip + 5700551)) >= 432) goto loc_00A59340;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 432;
    goto loc_00A5B755;
loc_00A59340:
    result = PsGetCurrentServerSiloGlobals(v_rip + 5700551, (uint32_t)((uint32_t)(v_rip + 5700551)), v_stack_m3B4, v_stack_m3B4);
    result = ExAcquireTimeRefreshLockShared(v_rip + 5700551, (uint32_t)((uint32_t)(v_rip + 5700551)), v_stack_m3B4, v_stack_m3B4);
loc_00A59366:
    *(uint64_t *)(v_stack_m208) = v_xmm0;
    *(uint64_t *)(v_stack_m208 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_m208 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_m208 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_m208 + 0x40) = v_xmm0;
    *(uint64_t *)(v_stack_m208 + 0x50) = v_xmm1;
    *(uint64_t *)(v_stack_m208 + 0x60) = v_xmm0;
    result = (v_stack_m208) + (3 + 125);
    *(uint64_t *)(result - 0x10) = v_xmm1;
    local_r12 = (*(uint64_t *)(result + 0x4C8)) + (3 + 125);
    Arg1 = (3) - (1);
    if (condition_is_not_equal) goto loc_00A59366;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    result = ExReleaseTimeRefreshLockShared(Arg1, (uint32_t)((uint32_t)(v_rip + 5700551)), v_stack_m3B4, v_stack_m3B4);
loc_00A593EA:
    *(uint64_t *)(v_rip + 0x56FBC7) = v_xmm0;
    *(uint64_t *)(v_rip + 0x56FBC7 + 0x10) = v_xmm1;
    *(uint64_t *)(v_rip + 0x56FBC7 + 0x20) = v_xmm0;
    *(uint64_t *)(v_rip + 0x56FBC7 + 0x30) = v_xmm1;
    *(uint64_t *)(v_rip + 0x56FBC7 + 0x40) = v_xmm0;
    *(uint64_t *)(v_rip + 0x56FBC7 + 0x50) = v_xmm1;
    *(uint64_t *)(v_rip + 0x56FBC7 + 0x60) = v_xmm0;
    local_rdi = (v_rip + 5700551) + (3 + 125);
    *(uint64_t *)(local_rdi - 0x10) = v_xmm1;
    result = (v_stack_m208) + (3 + 125);
    local_r14 = (3) - (1);
    if (condition_is_not_equal) goto loc_00A593EA;
    *(uint64_t *)(local_rdi) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x10) = v_xmm1;
    *(uint64_t *)(local_rdi + 0x20) = v_xmm0;
    v_stack_m3B4 = 432;
    goto loc_00A5869E;
loc_00A59459:
    result = ExpQueryNumaProximityNode(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5946E:
    v_stack_m240 = (uint16_t)((uint32_t)(v_stack_m380));
    result = KeQueryGroupAffinity((uint16_t)((uint32_t)(v_stack_m380)), (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4, v_stack_m3B4);
    v_stack_m248 = result;
    v_stack_m368 = result;
    v_stack_m3C8 = v_stack_m398;
    Arg2 = 0;
    Arg1 = 0;
    result = PpmCapturePerformanceDistribution(Arg1, Arg2, (uint32_t)((uint32_t)(result)), v_stack_m248);
    v_stack_m3B8 = (uint32_t)(result);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000004ULL)))) goto loc_00A5B79F;
    if (((uint32_t)((uint32_t)(v_stack_m398))) <= ((uint32_t)(local_r14))) goto loc_00A594D9;
    v_stack_m3B8 = (uint32_t)((uint32_t)(0xC0000004ULL));
    goto loc_00A59EB4;
loc_00A594D9:
    result = ExAllocatePool2(64, (uint32_t)(v_stack_m398), (uint32_t)(0x744D5050ULL), v_stack_m248);
    v_stack_m3A0 = result;
    if (result != 0) goto loc_00A59506;
loc_00A594F9:
    v_stack_m3B8 = 0xC000009AULL;
    goto loc_00A5B79F;
loc_00A59506:
    v_stack_m3C8 = v_stack_m3B4;
    result = PpmCapturePerformanceDistribution(result, (uint32_t)(v_stack_m398), (uint32_t)(v_stack_m368), v_stack_m248);
    v_stack_m3B8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A59554;
    result = memcpy(local_rdi, result, (uint32_t)(v_stack_m3B4), v_stack_m248);
    goto loc_00A59554;
loc_00A59554:
loc_00A59559:
loc_00A5955C:
    result = ExFreePoolWithTag(result, (uint32_t)(0x744D5050ULL), (uint32_t)(v_stack_m3B4), v_stack_m248);
    goto loc_00A5B79F;
loc_00A59566:
    v_stack_m3B8 = 0xC0000003ULL;
    goto loc_00A5B79F;
loc_00A59573:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) - (107));
    if (condition_is_equal) goto loc_00A59690;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A595E4;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A595C5;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00A595B0;
    if (Arg1 != 1) goto loc_00A5B6E3;
    result = PsQueryCpuQuotaInformation(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B0, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A595B0:
    result = IoQueryVhdBootInformation(local_rdi, local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4);
    goto loc_00A5B773;
loc_00A595C5:
    v_stack_m3C8 = v_stack_m3B4;
    result = SmQueryStoreInformation(local_rdi, local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B0);
    goto loc_00A5B773;
loc_00A595E4:
    v_stack_m3B4 = (uint32_t)(v_stack_m3B0 * 8);
    if (((uint32_t)(local_r14)) < 8) goto loc_00A590DF;
    if (((uint32_t)(local_r14)) < ((uint32_t)(v_stack_m3B0 * 8))) {
        Arg4 = (uint32_t)(local_r14);
        Arg4 = (uint32_t)((Arg4) >> (3));
        v_stack_m384 = (uint32_t)(Arg4);
    }
    local_r14 = (uint32_t)((local_r14) & (0xC0000004ULL));
    v_stack_m2D8 = local_rdi;
loc_00A5962E:
    v_stack_m3A8 = 0;
    if (0 >= ((uint32_t)(Arg4))) goto loc_00A590D5;
    v_stack_m3AC = (uint16_t)((uint32_t)(v_stack_m380));
    v_stack_m3AA = 0;
    v_stack_m3A9 = 0;
    result = KeGetProcessorIndexFromNumber(v_stack_m3AC, local_rdi, (uint32_t)((uint32_t)(local_r14)), Arg4);
    *(uint64_t *)(v_stack_m2D8) = *(uint64_t *)(*(uint64_t *)(v_rip + 0x56F617 + (uint32_t)((uint32_t)(result)) * 8) + 0x8778);
    result = (v_stack_m2D8) + (8);
    v_stack_m2D8 = result;
    result = (uint32_t)(((uint32_t)(v_stack_m3A8)) + (1));
    goto loc_00A5962E;
loc_00A59690:
loc_00A59695:
    v_stack_m3A0 = v_stack_m208;
    v_stack_m398 = 80;
    result = 80;
    if (((uint32_t)(local_r14)) < 80) {
        result = (uint32_t)(local_r14);
        v_stack_m398 = (uint32_t)(result);
    }
    v_stack_m3B4 = (uint32_t)(result);
    result = v_stack_m3AC;
    if (1 != 231) { result = 0; }
    v_stack_m368 = result;
loc_00A596D9:
    result = KeQueryLogicalProcessorRelationship(result, (uint32_t)(v_stack_m2D0), v_stack_m3A0, v_stack_m3B4);
    v_stack_m3B8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A5B3BB;
    result = memcpy(v_rip + 5699095, v_stack_m3A0, (uint32_t)(v_stack_m3B4), v_stack_m3B4);
    v_stack_m3B8 = 0;
loc_00A59711:
    if (v_stack_m3A0 == 0) goto loc_00A5B79F;
    if (v_stack_m3A0 == v_stack_m208) goto loc_00A5B79F;
loc_00A5972B:
    Arg2 = 0;
    goto loc_00A59559;
loc_00A59732:
    if (((uint32_t)(local_r14)) == ((uint32_t)(v_rip + 5699095))) goto loc_00A5974D;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = (uint32_t)(v_rip + 5699095);
    goto loc_00A5B755;
loc_00A5974D:
    result = ExpGetSystemBasicInformation(v_rip + 5699095, Arg2, (uint32_t)(v_stack_m3B4), v_stack_m3B4);
loc_00A59755:
    v_stack_m3B8 = (uint32_t)(result);
loc_00A59759:
    v_stack_m3B4 = 64;
    goto loc_00A5B79F;
loc_00A59766:
    if (((uint32_t)(v_stack_m3A0)) > 120) goto loc_00A59910;
    if (((uint32_t)(v_stack_m3A0)) == 120) goto loc_00A59854;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m3A0))) - (115));
    if (condition_is_equal) goto loc_00A59815;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00A59800;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00A597D0;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00A5979D;
    if (((uint32_t)(Arg2)) == 1) goto loc_00A59854;
    goto loc_00A5B6E3;
loc_00A5979D:
    if (v_stack_m3B0 == 0) goto loc_00A5AE6D;
    if (((uint32_t)(local_r14)) >= 272) goto loc_00A597C8;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 272;
    goto loc_00A5B755;
loc_00A597C8:
    goto loc_00A588EB;
loc_00A597D0:
    v_stack_m3B4 = (uint32_t)((uint32_t)(0x448ULL));
    if (((uint32_t)(local_r14)) != ((uint32_t)((uint32_t)(0x448ULL)))) goto loc_00A589BB;
    if (v_stack_m3B0 == 0) goto loc_00A597F3;
loc_00A597E9:
    goto loc_00A5B7BE;
loc_00A597F3:
    result = ExQueryBootEntropyInformation(v_rip + 5699095, Arg2, (uint32_t)(v_stack_m3B4), (uint32_t)((uint32_t)((uint32_t)(0xC0000004ULL))));
    goto loc_00A5B773;
loc_00A59800:
    result = IoQueryLowPriorityIoInformation(v_rip + 5699095, v_rip + 5699095, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4);
    goto loc_00A5B773;
loc_00A59815:
    if ((uint32_t)((uint32_t)(v_stack_m390)) != 0) goto loc_00A589BB;
    v_stack_m3B4 = 8;
    if (((uint32_t)(local_r14)) < 8) goto loc_00A589BB;
    *(uint32_t *)(v_rip + 0x56F617) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56B9A6)));
    *(uint32_t *)(v_rip + 0x56F617 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56BB4A)));
    goto loc_00A5B79F;
loc_00A59854:
    if (((uint32_t)(local_r14)) >= ((uint32_t)(v_rip + 5699095))) goto loc_00A5986F;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = (uint32_t)(v_rip + 5699095);
    goto loc_00A5B755;
loc_00A5986F:
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x56BB4A));
    local_r13 = (uint32_t)(0xC0000004ULL);
    if (((uint32_t)(v_stack_m3A0)) != 119) {
        result = 3;
        local_r13 = (uint32_t)(0xC0000004ULL);
        if (((uint32_t)(v_stack_m3A0)) == 120) { local_r13 = (uint32_t)(result); }
        local_r12 = (uint32_t)(local_r13);
    }
    result = MmQuerySystemWorkingSetInformation((uint32_t)((uint32_t)(local_r12)), v_stack_m208, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4);
    *(uint64_t *)(v_rip + 0x56F617) = v_stack_m208;
    *(uint64_t *)(v_rip + 0x56F617 + 0x8) = v_stack_m200;
    *(uint32_t *)(v_rip + 0x56F617 + 0x10) = (uint32_t)((uint32_t)(v_stack_m1F8));
    v_stack_m3A8 = 64;
    *(uint64_t *)(v_rip + 0x56F617 + 0x18) = v_stack_m1F0;
    *(uint64_t *)(v_rip + 0x56F617 + 0x20) = v_stack_m1E8;
    *(uint64_t *)(v_rip + 0x56F617 + 0x28) = v_stack_m1E0;
    *(uint64_t *)(v_rip + 0x56F617 + 0x30) = v_stack_m1D8;
    *(uint32_t *)(v_rip + 0x56F617 + 0x38) = (uint32_t)((uint32_t)(v_stack_m1D0));
    *(uint32_t *)(v_rip + 0x56F617 + 0x3C) = (uint32_t)((uint32_t)(v_stack_m1CC));
    goto loc_00A59759;
loc_00A59910:
    local_rbx = (uint32_t)((v_stack_m3A0) - (121));
    if (condition_is_equal) goto loc_00A59AEB;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A59A41;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5998C;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A5B6E3;
    v_stack_m3B4 = 12;
    if (((uint32_t)(local_r14)) < 4) goto loc_00A589BB;
    v_stack_m230 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56F617)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56F617)))) != 1) goto loc_00A58BFB;
    if (((uint32_t)(local_r14)) < 12) goto loc_00A589BB;
    *(uint32_t *)(v_rip + 0x56F617 + 0x8) = 0;
    *(uint32_t *)(v_rip + 0x56F617 + 0x4) = 0;
    *(uint32_t *)(v_rip + 0x56F617 + 0x8) = (uint32_t)(local_r13);
    *(uint32_t *)(v_rip + 0x56F617 + 0x4) = (uint32_t)(local_r13);
    if ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56F617))) != 0) {
    }
    goto loc_00A5B79F;
loc_00A5998C:
    if (((uint32_t)(local_r14)) == 32) goto loc_00A599AD;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 32;
    goto loc_00A5B755;
loc_00A599AD:
    result = MmGetProcessPartitionId(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), v_stack_m208, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4);
    result = MmGetAvailablePages((uint16_t)(result), v_stack_m208, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4);
    v_stack_m208 = result;
    result = MmGetTotalCommittedPages((uint16_t)(result), v_stack_m208, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4);
    v_stack_m200 = result;
    result = MmGetTotalCommitLimit((uint16_t)(result), v_stack_m208, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4);
    v_stack_m1F8 = result;
    result = MmGetPeakCommitment((uint16_t)(result), v_stack_m208, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4);
    v_stack_m1F0 = result;
    result = v_stack_m1F0;
    if (v_stack_m1F0 < v_stack_m200) { result = v_stack_m200; }
    v_stack_m1F0 = result;
    *(uint64_t *)(v_rip + 0x56F617) = v_xmm0;
    *(uint64_t *)(v_rip + 0x56F617 + 0x10) = v_xmm1;
loc_00A59A32:
    v_stack_m3B4 = 32;
    goto loc_00A5B79F;
loc_00A59A41:
    v_stack_m3B4 = 8;
    if (((uint32_t)(local_r14)) != 8) goto loc_00A589BB;
    if (v_rip + 5699095 == 0) goto loc_00A589BB;
    result = ExAllocatePool2(257, (uint32_t)((uint32_t)(local_r14)), (uint32_t)(0x6F666E49ULL), v_stack_m3B4);
    v_stack_m3A0 = result;
    if (result == 0) goto loc_00A594F9;
    result = guard_dispatch_icall(local_r14 + 18, (uint32_t)((uint32_t)(local_r14)), result, v_stack_m3B4);
    v_stack_m3B8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A59AE1;
    *(uint32_t *)(v_rip + 0x56F617) = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56F617 + 0x4))))) ^ (*(uint32_t *)(result + 0x4)));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(local_r13)));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56F617 + 0x4)))));
    *(uint32_t *)(v_rip + 0x56F617 + 0x4) = Arg1;
    Arg2 = (uint32_t)(((uint32_t)(Arg1)) ^ (*(uint32_t *)(result + 0x4)));
    Arg2 = (uint32_t)((Arg2) & (2));
    Arg2 = (uint32_t)((Arg2) ^ (Arg1));
    *(uint32_t *)(v_rip + 0x56F617 + 0x4) = (uint32_t)(Arg2);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) ^ (*(uint32_t *)(result + 0x4)));
    result = (uint32_t)((result) & (4));
    result = (uint32_t)((result) ^ ((uint32_t)(Arg2)));
    *(uint32_t *)(v_rip + 0x56F617 + 0x4) = (uint32_t)(result);
    goto loc_00A59AE1;
loc_00A59AE1:
    goto loc_00A59559;
loc_00A59AEB:
    Arg1 = (uint32_t)((*(uint16_t *)(v_rip + 0x56B50E)) << (2));
    v_stack_m3B4 = Arg1;
    if (((uint32_t)(local_r14)) < Arg1) goto loc_00A589BB;
    v_stack_m3A8 = 0;
loc_00A59B10:
    if (0 >= ((uint32_t)(*(uint16_t *)(v_rip + 0x56B4E9)))) goto loc_00A59B4B;
    Arg1 = (uint32_t)((v_stack_m370) * ((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0x56B4E9))))));
    Arg1 = (uint32_t)((Arg1) + (0));
    *(uint32_t *)(v_rip + 0x56F617 + 0x0 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x56B578) + Arg1 * 4)));
    v_stack_m3A8 = (uint32_t)(0 + 1);
    goto loc_00A59B10;
loc_00A59B4B:
    goto loc_00A5B79F;
loc_00A59B55:
    v_stack_m3B4 = 32;
    if (((uint32_t)(local_r14)) != 32) goto loc_00A589BB;
    Arg1 = 0;
    result = BgkQueryBootGraphicsInformation(Arg1, v_stack_m208, (uint32_t)((uint32_t)(0 + 1)), (uint32_t)((uint32_t)(0 + 1)));
    v_stack_m3B8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A5B79F;
    result = v_stack_m208;
    if (v_stack_m3B0 != 0) { result = 0; }
    v_stack_m208 = result;
    result = memcpy(v_rip + 5699095, v_stack_m208, (uint32_t)(v_stack_m3B4), (uint32_t)((uint32_t)(0 + 1)));
    goto loc_00A5B79F;
loc_00A59BC5:
    if (((uint32_t)(result)) > 189) goto loc_00A5AC36;
    if (((uint32_t)(result)) == 189) goto loc_00A5B6ED;
    if (((uint32_t)(result)) > 159) goto loc_00A5A32E;
    if (((uint32_t)(result)) == 159) goto loc_00A5A319;
    if (((uint32_t)(result)) > 144) goto loc_00A5A004;
    if (((uint32_t)(result)) == 144) goto loc_00A59FAB;
    if (((uint32_t)(result)) > 137) goto loc_00A59D27;
    if (((uint32_t)(result)) == 137) goto loc_00A59CF4;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) - (128));
    if (condition_is_equal) goto loc_00A5B505;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_00A59CC2;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A59CA1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A59C40;
    if (Arg1 == 1) goto loc_00A59CF4;
    goto loc_00A5B6E3;
loc_00A59C40:
    v_stack_m3B4 = 8;
    if (((uint32_t)(local_r14)) < 8) goto loc_00A589BB;
    Arg2 = 0;
    result = HvlQueryActiveProcessors(v_stack_m2BC, Arg2, (uint32_t)(v_stack_m3B4), (uint32_t)((uint32_t)(0 + 1)));
    if ((uint32_t)(result) != 0) goto loc_00A58BFB;
    Arg1 = 0;
    result = HvlQueryProcessorTopologyCount(Arg1, v_stack_m2B8, (uint32_t)(v_stack_m3B4), (uint32_t)((uint32_t)(0 + 1)));
    v_stack_m3B8 = (uint32_t)(result);
    if ((uint32_t)(result) != 0) goto loc_00A58BFB;
    *(uint32_t *)(v_rip + 0x56F617) = (uint32_t)((uint32_t)(v_stack_m2BC));
    *(uint32_t *)(v_rip + 0x56F617 + 0x4) = (uint32_t)((uint32_t)(v_stack_m2B8));
    goto loc_00A5B79F;
loc_00A59CA1:
    v_stack_m3B4 = 32;
    if (((uint32_t)(local_r14)) != 32) goto loc_00A589BB;
    result = sub_00A179B0(Arg1, v_rip + 5699095, (uint32_t)(v_stack_m3B4), (uint32_t)((uint32_t)(0 + 1)));
    goto loc_00A5B773;
loc_00A59CC2:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x57FDA9), (uint8_t)(v_stack_m3B0), (uint32_t)(v_stack_m3B4), (uint32_t)((uint32_t)(0 + 1)));
    if ((uint8_t)(result) == 0) goto loc_00A5B210;
    result = ExpGetSystemPlatformBinary(v_rip + 5699095, (uint32_t)((uint32_t)(local_r14)), (uint8_t)(v_stack_m3B0), (uint32_t)((uint32_t)(0 + 1)));
    goto loc_00A57FA3;
loc_00A59CF4:
    if (((uint32_t)(local_r14)) == 48) goto loc_00A59D15;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 48;
    goto loc_00A5B755;
loc_00A59D15:
    result = ExpGetDeviceDataInformation((uint32_t)((uint32_t)(v_stack_m3B0)), v_rip + 5699095, 48, (uint32_t)((uint32_t)(0 + 1)));
    goto loc_00A5B7BE;
loc_00A59D27:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m3B0))) - (138));
    if (condition_is_equal) goto loc_00A59F91;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A59F77;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A59ED7;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A59D6C;
    if (Arg1 != 48) goto loc_00A5B6E3;
loc_00A59D55:
    result = SeSecureBootQueryInformation((uint32_t)((uint32_t)(v_stack_m3B0)), v_rip + 5699095, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4);
    goto loc_00A5B773;
loc_00A59D6C:
    local_r12 = 48;
    if (((uint32_t)(v_stack_m3B0)) != 8) { local_r12 = (uint32_t)(48 + 24); }
    if ((uint32_t)(local_r14) == 0) goto loc_00A59EBD;
    Arg2 = 0;
    if (0 != 0) goto loc_00A59EBD;
    v_stack_m368 = 0;
loc_00A59DA0:
    v_stack_m3A8 = 0;
    v_stack_m2D8 = v_rip + 5699095;
    if (0 >= ((uint32_t)(v_stack_m3B4))) goto loc_00A59EAD;
    v_stack_m3AC = (uint16_t)((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0x56B4E9))));
    v_stack_m3AA = 0;
    v_stack_m3A9 = 0;
    result = KeGetProcessorIndexFromNumber(v_stack_m3AC, Arg2, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4);
    v_stack_m378 = *(uint64_t *)(v_rip + 0x56EE69 + (uint32_t)((uint32_t)(result)) * 8);
    if (((uint32_t)(local_r14)) < ((uint32_t)(local_r12 + (uint32_t)(v_stack_m368) * 1))) goto loc_00A59EB4;
    v_stack_m368 = (uint32_t)(local_r12 + (uint32_t)(v_stack_m368) * 1);
    Arg2 = 0;
    result = PoGetIdleTimes(v_stack_m3AC, Arg2, v_stack_m208, v_stack_m3B4);
    result = ((uint32_t)(*(uint32_t *)(v_stack_m378 + 0x8648))) * ((uint32_t)(*(uint32_t *)(v_rip + 0x56CC8A)));
    *(uint64_t *)(v_rip + 0x56F617 + 0x10) = result;
    result = ((uint32_t)(v_stack_m204)) * ((uint32_t)(*(uint32_t *)(v_rip + 0x56CC8A)));
    *(uint64_t *)(v_rip + 0x56F617 + 0x8) = result;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m378 + 0x864C))) * ((uint32_t)(*(uint32_t *)(v_rip + 0x56CC8A)));
    *(uint64_t *)(v_rip + 0x56F617 + 0x18) = result;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m378 + 0x8650))) * ((uint32_t)(*(uint32_t *)(v_rip + 0x56CC8A)));
    *(uint64_t *)(v_rip + 0x56F617 + 0x20) = result;
    result = ((uint32_t)(v_stack_m208)) * ((uint32_t)(*(uint32_t *)(v_rip + 0x56CC8A)));
    *(uint64_t *)(v_rip + 0x56F617) = result;
    *(uint32_t *)(v_rip + 0x56F617 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m378 + 0x8640)));
    result = (uint32_t)(*(uint32_t *)(v_stack_m378 + 0x8640));
    if (((uint32_t)(v_stack_m3B0)) == 141) {
        result = *(uint32_t *)(v_stack_m378 + 0x866C);
        result = (result) * ((uint32_t)(*(uint32_t *)(v_rip + 0x56CC8A)));
        *(uint64_t *)(v_rip + 0x56F617 + 0x30) = result;
        *(uint32_t *)(v_rip + 0x56F617 + 0x2C) = 0;
        *(uint64_t *)(v_rip + 0x56F617 + 0x38) = 0;
        *(uint64_t *)(v_rip + 0x56F617 + 0x40) = 0;
    }
    local_rdi = (v_rip + 5699095) + ((uint32_t)((uint32_t)(local_r12)));
    result = (uint32_t)(((uint32_t)(v_stack_m3A8)) + ((uint32_t)(local_r13)));
    goto loc_00A59DA0;
loc_00A59EAD:
loc_00A59EB4:
    v_stack_m3B4 = (uint32_t)((uint32_t)(v_stack_m368));
    goto loc_00A5B79F;
loc_00A59EBD:
    if (Arg6 == 0) goto loc_00A5B755;
    local_r12 = (uint32_t)((local_r12) * ((uint32_t)((uint32_t)(v_stack_m384))));
    *(uint32_t *)(Arg6) = (uint32_t)(local_r12);
    goto loc_00A5B755;
loc_00A59ED7:
    if (Arg6 != 0) goto loc_00A59EEF;
    if (((uint32_t)(local_r14)) >= 8) goto loc_00A59EEF;
    v_stack_m3B8 = 0xC000000DULL;
    goto loc_00A5B79F;
loc_00A59EEF:
    result = BgkQueryBootGraphicsInformation((uint32_t)((uint32_t)(local_r12)), v_stack_m3B4, v_stack_m208, (uint32_t)(v_stack_m384));
    v_stack_m3B8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A5B79F;
    if (v_stack_m3B4 == 0) goto loc_00A594F9;
    if (((uint32_t)(local_r14)) < v_stack_m3B4) goto loc_00A590DF;
    result = BgkQueryBootGraphicsInformation((uint32_t)((uint32_t)(local_r13)), v_stack_m2A8, v_stack_m208, (uint32_t)(v_stack_m384));
    v_stack_m3B8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A5B79F;
    if (v_stack_m2A8 == 0) goto loc_00A594F9;
    result = memcpy(local_rdi, v_stack_m2A8, (uint32_t)(v_stack_m3B4), (uint32_t)(v_stack_m384));
    goto loc_00A59F6D;
loc_00A59F6D:
    goto loc_00A59559;
loc_00A59F77:
    result = ExpQueryChannelInformation(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4, (uint32_t)(v_stack_m384));
    goto loc_00A57FA3;
loc_00A59F91:
    result = ExpQueryMemoryTopologyInformation(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4, (uint32_t)(v_stack_m384));
    goto loc_00A57FA3;
loc_00A59FAB:
    local_r12 = 32;
    if (((uint32_t)(v_stack_m2A8)) != 18) { local_r12 = (uint32_t)(32 + 8); }
    v_stack_m3B4 = (uint32_t)(local_r12);
    if (((uint32_t)(local_r14)) >= ((uint32_t)(local_r12))) goto loc_00A59FDD;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = (uint32_t)(local_r12);
    goto loc_00A5B755;
loc_00A59FDD:
    v_stack_m3B4 = 0;
    Arg4 = (((uint32_t)(v_stack_m2A8)) == ((uint32_t)(result))) ? 1 : 0;
    v_stack_m3C8 = v_stack_m3B4;
    result = MmGetPageFileInformation(local_rdi, local_rdi, (uint32_t)((uint32_t)(local_r14)), Arg4);
    goto loc_00A5B773;
loc_00A5A004:
    if (((uint32_t)(v_stack_m2A8)) > 151) goto loc_00A5A124;
    if (((uint32_t)(v_stack_m2A8)) == 151) goto loc_00A5A0E1;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m2A8))) - (145));
    if (condition_is_equal) goto loc_00A59D55;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_r12)));
    if (condition_is_equal) goto loc_00A5A0CC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5B737;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5A07C;
    if (Arg1 != 1) goto loc_00A5B6E3;
    if (local_rdi == 0) goto loc_00A5A062;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x57FA23), v_stack_m3B0, (uint32_t)((uint32_t)(local_r14)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A5B210;
loc_00A5A062:
    result = ExpQueryBootLoaderMetadata(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4, Arg4);
    goto loc_00A57FA3;
loc_00A5A07C:
    if (((uint32_t)(local_r14)) >= 3) goto loc_00A5A09C;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 3;
    goto loc_00A5B755;
loc_00A5A09C:
    result = ((*(uint8_t *)(v_rip + 0x3B097A)) == 0) ? 1 : 0;
    *(uint8_t *)(local_rdi) = (uint8_t)(result);
    *(uint8_t *)(local_rdi + 0x1) = (uint8_t)(*(uint8_t *)(v_rip + 0x4ED54A));
    result = ((*(uint8_t *)(v_rip + 0x4ED524)) == 0) ? 1 : 0;
    *(uint8_t *)(local_rdi + 0x2) = (uint8_t)(result);
    v_stack_m3B4 = 3;
    goto loc_00A5B79F;
loc_00A5A0CC:
    result = ExpQueryPortableWorkspaceEfiLauncherInformation(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4, Arg4);
    goto loc_00A5B773;
loc_00A5A0E1:
    v_stack_m3B4 = 4;
    if (((uint32_t)(local_r14)) >= 4) goto loc_00A5A109;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 4;
    goto loc_00A5B755;
loc_00A5A109:
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x40E435)));
    goto loc_00A5B79F;
loc_00A5A124:
    local_rbx = (uint32_t)((v_stack_m2A8) - (153));
    if (condition_is_equal) goto loc_00A5A287;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5A255;
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(local_r12)));
    if (condition_is_equal) goto loc_00A5A1FB;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5A181;
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A5B6E3;
    v_stack_m3B4 = (uint32_t)(32 + 8);
    if (((uint32_t)(local_r14)) >= ((uint32_t)(32 + 8))) goto loc_00A5A170;
    if (Arg6 == 0) goto loc_00A589BB;
    *(uint32_t *)(Arg6) = (uint32_t)(32 + 8);
    goto loc_00A589BB;
loc_00A5A170:
    result = PoEnergyEstimationEnabled(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4, Arg4);
    *(uint8_t *)(local_rdi) = (uint8_t)(result);
    goto loc_00A5B79F;
loc_00A5A181:
    Arg1 = (uint32_t)((*(uint16_t *)(v_rip + 0x4A4EE2)) + (24));
    v_stack_m3B4 = Arg1;
    if (((uint32_t)(local_r14)) < Arg1) goto loc_00A589BB;
    result = 0;
    *(uint64_t *)(local_rdi) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x10) = 0;
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4A4EB2)));
    *(uint16_t *)(local_rdi + 0x8) = (uint16_t)(*(uint16_t *)(v_rip + 0x4A4EB1));
    *(uint16_t *)(local_rdi + 0xA) = (uint16_t)(*(uint16_t *)(v_rip + 0x4A4EA8));
    result = *(uint16_t *)(v_rip + 0x4A4EA8);
    if ((*(uint16_t *)(v_rip + 0x4A4E9A)) != 0) {
        *(uint64_t *)(local_rdi + 0x10) = local_rdi + 24;
        Arg3 = *(uint16_t *)(v_rip + 0x4A4E8E);
        Arg2 = *(uint64_t *)(v_rip + 0x4A4E8D);
        result = memcpy(local_rdi + 24, Arg2, Arg3, Arg4);
    }
    goto loc_00A5B79F;
loc_00A5A1FB:
    v_stack_m3B4 = 128;
    if (((uint32_t)(local_r14)) != 128) goto loc_00A589BB;
    result = BgkQueryBootGraphicsInformation(local_r14 - 125, v_stack_m208, Arg3, Arg4);
    v_stack_m3B8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A5B79F;
    result = memcpy(local_rdi, v_stack_m208, (uint32_t)(v_stack_m3B4), Arg4);
    goto loc_00A5B79F;
loc_00A5A255:
    if (((uint32_t)(local_r14)) >= 32) goto loc_00A5A276;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 32;
    goto loc_00A5B755;
loc_00A5A276:
    result = ExpGetSystemProcessorFeaturesInformation(local_rdi, v_stack_m208, (uint32_t)(v_stack_m3B4), Arg4);
loc_00A5A27E:
    v_stack_m3B8 = (uint32_t)(result);
    goto loc_00A59A32;
loc_00A5A287:
    if ((uint32_t)((uint32_t)(v_stack_m390)) != 0) goto loc_00A589BB;
    v_stack_m3B4 = (uint32_t)((uint32_t)(v_stack_m390) + 32);
    if (((uint32_t)(local_r14)) < ((uint32_t)((uint32_t)(v_stack_m390) + 32))) goto loc_00A5A2CE;
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4B4F5C)));
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4B4F58)));
    *(uint32_t *)(local_rdi + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4B4F53)));
    *(uint64_t *)(local_rdi + 0x10) = *(uint64_t *)(v_rip + 0x4B4F51);
    *(uint32_t *)(local_rdi + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4B4F4F)));
    goto loc_00A5A2F6;
loc_00A5A2CE:
    if (((uint32_t)(local_r14)) < 12) goto loc_00A5A2FB;
    v_stack_m3B4 = 12;
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4B4F1E)));
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4B4F1A)));
    *(uint32_t *)(local_rdi + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4B4F15)));
loc_00A5A2F6:
    goto loc_00A5B79F;
loc_00A5A2FB:
    v_stack_m3B8 = (uint32_t)((uint32_t)(0xC0000004ULL));
    goto loc_00A5B79F;
loc_00A5A319:
    result = HvlQueryDetailInfo(local_rdi, (uint32_t)((uint32_t)(local_r14)), (uint32_t)(v_stack_m3B4), v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5A32E:
    if (((uint32_t)(local_rbx)) > 174) goto loc_00A5A76E;
    if (((uint32_t)(local_rbx)) == 174) goto loc_00A5A759;
    if (((uint32_t)(local_rbx)) > 166) goto loc_00A5A60A;
    if (((uint32_t)(local_rbx)) == 166) goto loc_00A5A5F5;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (160));
    if (condition_is_equal) goto loc_00A5A546;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)((uint32_t)(v_stack_m390) + 32)));
    if (condition_is_equal) goto loc_00A5A531;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5A4FF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5B6ED;
    if (Arg1 != 1) goto loc_00A5B6E3;
    v_stack_m3B4 = 16;
    if (((uint32_t)(local_r14)) == 16) goto loc_00A5A3AE;
    if (Arg6 == 0) goto loc_00A589BB;
    *(uint32_t *)(Arg6) = 16;
    goto loc_00A589BB;
loc_00A5A3AE:
    Arg1 = (uint8_t)((*(uint8_t *)(v_rip + 0x4A4CC4)) & ((uint8_t)((uint32_t)(0xC0000004ULL))));
    Arg1 = (uint8_t)((Arg1) << (4));
    result = (uint8_t)((v_stack_m208) & (239));
    Arg1 = (uint8_t)((Arg1) | ((uint8_t)(result)));
    v_stack_m208 = (uint8_t)(Arg1);
    result = VslIsSecureKernelRunning(Arg1, (uint32_t)((uint32_t)(local_r14)), (uint32_t)(v_stack_m3B4), v_stack_m3B4);
    if ((uint8_t)(result) == 0) goto loc_00A5A4E9;
    v_stack_m388 = 0;
    Arg1 = (uint8_t)((Arg1) | ((uint8_t)((uint32_t)(0xC0000004ULL))));
    v_stack_m208 = (uint8_t)(Arg1);
    Arg1 = 0;
    result = VslGetNestedPageProtectionFlags(Arg1, (uint32_t)((uint32_t)(local_r14)), (uint32_t)(v_stack_m3B4), v_stack_m3B4);
    if ((((uint8_t)((uint32_t)(v_stack_m390) + 32)) & ((uint8_t)(result))) != 0) {
    }
    if (((32) & ((uint8_t)((uint32_t)((uint32_t)(result))))) != 0) {
    }
    if ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (16)) != 0) {
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint8_t)((v_stack_m207) | (2));
        v_stack_m207 = (uint8_t)(Arg1);
    }
    result = v_stack_m2A0;
    if (v_stack_m2A0 != 0) {
        Arg2 = v_stack_m388;
        Arg1 = v_stack_m2A0;
        result = VslIsTrustletRunning(Arg1, Arg2, (uint32_t)(v_stack_m3B4), v_stack_m3B4);
        v_stack_m3B8 = (uint32_t)(result);
        Arg1 = v_stack_m207;
        Arg1 = (uint8_t)((Arg1) & (254));
        result = v_stack_m388;
        result = (uint8_t)((result) & ((uint8_t)((uint32_t)(0xC0000004ULL))));
        Arg1 = (uint8_t)((Arg1) | ((uint8_t)(result)));
        v_stack_m207 = (uint8_t)(Arg1);
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint8_t)((Arg1) | (4));
        v_stack_m207 = (uint8_t)(Arg1);
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint8_t)((Arg1) | (8));
        v_stack_m207 = (uint8_t)(Arg1);
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint8_t)((Arg1) | (16));
        v_stack_m207 = (uint8_t)(Arg1);
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint8_t)((Arg1) | (32));
        v_stack_m207 = (uint8_t)(Arg1);
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint8_t)((Arg1) | (64));
        v_stack_m207 = (uint8_t)(Arg1);
    }
    if (!(condition_is_above_or_equal)) {
    }
    result = VslIsEncryptionKeyAvailable(Arg1, Arg2, (uint32_t)(v_stack_m3B4), v_stack_m3B4);
    result = (uint8_t)((result) & ((uint8_t)((uint32_t)(0xC0000004ULL))));
    result = (uint8_t)((result) << (5));
    Arg1 = (uint8_t)((v_stack_m208) & (223));
    result = (uint8_t)((result) | ((uint8_t)(Arg1)));
    v_stack_m208 = (uint8_t)(result);
loc_00A5A4E9:
    *(uint64_t *)(local_rdi) = v_xmm0;
    goto loc_00A5B79F;
loc_00A5A4FF:
    if (((uint32_t)(local_r14)) >= ((uint32_t)((uint32_t)(0xC0000004ULL)))) goto loc_00A5A51A;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = (uint32_t)((uint32_t)(0xC0000004ULL));
    goto loc_00A5B755;
loc_00A5A51A:
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(v_rip + 0x4FB780));
    v_stack_m3B4 = (uint32_t)((uint32_t)(0xC0000004ULL));
    goto loc_00A5B79F;
loc_00A5A531:
    result = SeQueryTrustedPlatformModuleInformation(local_rdi, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5A546:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m3B4))) << (6));
    v_stack_m3B4 = (uint32_t)(result);
    if (((uint32_t)(local_r14)) < 64) goto loc_00A590DF;
    if (((uint32_t)(local_r14)) < ((uint32_t)(result))) {
        Arg4 = (uint32_t)(local_r14);
        Arg4 = (uint32_t)((Arg4) >> (6));
        v_stack_m384 = (uint32_t)(Arg4);
    }
    result = (uint32_t)((result) & (0xC0000004ULL));
    v_stack_m368 = (uint32_t)(result);
    v_stack_m2D8 = local_rdi;
    v_stack_m3A8 = 0;
loc_00A5A597:
    if (0 >= ((uint32_t)(Arg4))) goto loc_00A5A5E9;
    v_stack_m3AC = (uint16_t)((uint32_t)(v_stack_m380));
    v_stack_m3AA = 0;
    v_stack_m3A9 = 0;
    result = KeGetProcessorIndexFromNumber(v_stack_m3AC, (uint32_t)((uint32_t)(local_r14)), v_stack_m3B4, Arg4);
    result = KeQueryCycleTimeStatsProcessor(*(uint64_t *)(v_rip + 0x56E6AE + (uint32_t)((uint32_t)(result)) * 8), local_rdi, v_stack_m3B4, Arg4);
    local_rdi = (local_rdi) + (64);
    v_stack_m2D8 = local_rdi;
    local_r12 = (uint32_t)((0) + (1));
    v_stack_m3A8 = (uint32_t)(local_r12);
    goto loc_00A5A597;
loc_00A5A5E9:
    goto loc_00A5B773;
loc_00A5A5F5:
    result = SeQueryHSTIResults(local_rdi, (uint32_t)((uint32_t)(v_rip + 5695150)), v_stack_m3B4, (uint32_t)(v_stack_m384));
    goto loc_00A5B773;
loc_00A5A60A:
    Arg1 = (uint32_t)((1) - (167));
    if (condition_is_equal) goto loc_00A5A73F;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_r12)));
    if (condition_is_equal) goto loc_00A5A72A;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_r12)));
    if (condition_is_equal) goto loc_00A59D55;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5B6ED;
    if (Arg1 != 1) goto loc_00A5B6E3;
    result = ExCpuSetResourceManagerAccessCheck(v_stack_m3B0, (uint32_t)((uint32_t)(v_rip + 5695150)), v_stack_m3B4, (uint32_t)(v_stack_m384));
    v_stack_m3B8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A5B7BE;
    v_stack_m3B4 = 264;
    if (((uint32_t)(v_rip + 5695150)) != 264) goto loc_00A589BB;
    result = ExAllocatePool2((uint32_t)((uint32_t)(264 - 8)), 264, (uint32_t)(0x6F666E49ULL), (uint32_t)(v_stack_m384));
    v_stack_m3A0 = result;
    if (result != 0) goto loc_00A5A68C;
    goto loc_00A5B7BE;
loc_00A5A68C:
    *(uint16_t *)((uint32_t)(0xC000009AULL)) = (uint16_t)((uint32_t)(0xC0000004ULL));
    *(uint16_t *)((uint32_t)(0xC000009AULL) + 0x2) = 32;
    *(uint32_t *)((uint32_t)(0xC000009AULL) + 0x4) = 0;
    Arg2 = 0;
    result = memset((uint32_t)(0xC000009AULL) + 8, Arg2, 264 - 8, (uint32_t)(v_stack_m384));
    result = KeGetAffinitizedInterruptsInfo(result, Arg2, 264 - 8, (uint32_t)(v_stack_m384));
loc_00A5A6B8:
    *(uint64_t *)(local_rdi) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x10) = v_xmm1;
    *(uint64_t *)(local_rdi + 0x20) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x30) = v_xmm1;
    *(uint64_t *)(local_rdi + 0x40) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x50) = v_xmm1;
    *(uint64_t *)(local_rdi + 0x60) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x80 - 0x10) = v_xmm1;
    result = (2) - (1);
    if (condition_is_not_equal) goto loc_00A5A6B8;
    *(uint64_t *)(local_rdi + 0x80) = *(uint64_t *)(result + 0x80);
    goto loc_00A5972B;
loc_00A5A72A:
    result = HvlQueryVsmProtectionInfo(local_rdi + 128, (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4, (uint32_t)(v_stack_m384));
    goto loc_00A5B773;
loc_00A5A73F:
    result = ExpQuerySingleModuleInformation(local_rdi + 128, (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B0, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5A759:
    result = PsRootSiloInformation(local_rdi + 128, (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4, v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5A76E:
    if (((uint32_t)(result)) > 182) goto loc_00A5AAAA;
    if (((uint32_t)(result)) == 182) goto loc_00A5A95B;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) - (175));
    if (condition_is_equal) goto loc_00A5A8C9;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00A5A832;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A59D55;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5A810;
loc_00A5A7A6:
    if (Arg1 != 1) goto loc_00A5B6E3;
    if (v_stack_m3B4 == 0) goto loc_00A5B306;
    v_stack_m250 = 0;
    v_stack_m3C0 = 0;
    v_stack_m3C8 = v_stack_m250;
    result = ObReferenceObjectByHandle(v_stack_m298, (uint32_t)(0x1000ULL), *(uint64_t *)(v_rip + 0x56C2D9), v_stack_m3B0);
    v_stack_m2C8 = v_stack_m250;
    if (sign_flag) goto loc_00A5B7BE;
    goto loc_00A5B311;
loc_00A5A810:
    v_stack_m3C8 = v_stack_m3B4;
    result = ExpQueryInterruptSteeringInformation(v_stack_m3A0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128, (uint32_t)((uint32_t)(264 - 8)));
    goto loc_00A5B773;
loc_00A5A832:
    if ((uint32_t)(264 - 8) == 0) goto loc_00A590DF;
    if ((uint8_t)(v_stack_m3B0) == 0) goto loc_00A5A859;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x57F2FC), (uint8_t)(v_stack_m3B0), local_rdi + 128, (uint32_t)((uint32_t)(264 - 8)));
    if ((uint8_t)(result) == 0) goto loc_00A5B210;
loc_00A5A859:
    result = ExAllocatePool2(65, 264 - 8, (uint32_t)(0x6F666E49ULL), (uint32_t)((uint32_t)(264 - 8)));
    v_stack_m3A0 = result;
    if (result == 0) goto loc_00A594F9;
    result = VslQuerySecureKernelProfileInformation(v_stack_m268, result, (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4);
    v_stack_m3B8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A59AE1;
    result = memcpy(local_rdi + 128, result, (uint32_t)(v_stack_m3B4), v_stack_m3B4);
    goto loc_00A59AE1;
loc_00A5A8C9:
    if ((uint32_t)(v_stack_m3B4) == 0) goto loc_00A5A923;
    v_stack_m260 = 0;
    v_stack_m3C0 = 0;
    v_stack_m3C8 = v_stack_m260;
    result = ObReferenceObjectByHandle(v_stack_m298, (uint32_t)(0x1000ULL), *(uint64_t *)(v_rip + 0x56C1C3), v_stack_m3B0);
    v_stack_m2C8 = v_stack_m260;
    if (sign_flag) goto loc_00A5B7BE;
    goto loc_00A5A92E;
loc_00A5A923:
loc_00A5A92E:
    result = KeQueryCpuSetInformation(local_rdi + 128, (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
loc_00A5A941:
    v_stack_m3B8 = (uint32_t)(result);
    if (0 == 0) goto loc_00A5B79F;
    result = ObfDereferenceObject(v_stack_m2C8, (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    goto loc_00A5B79F;
loc_00A5A95B:
    if (((uint32_t)(264 - 8)) == 56) goto loc_00A5A97B;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 56;
    goto loc_00A5B755;
loc_00A5A97B:
    result = MmGetProcessPartitionId(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = MmGetNumberOfPhysicalPages((uint16_t)(result), (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = (result) << (12);
    v_stack_m208 = result;
    result = MmGetAvailablePages((uint16_t)((uint16_t)(result)), (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = (result) << (12);
    v_stack_m200 = result;
    result = MmGetResidentAvailablePages((uint16_t)((uint16_t)(result)), (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = (result) << (12);
    v_stack_m1F8 = result;
    result = MmGetTotalCommittedPages((uint16_t)((uint16_t)(result)), (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = (result) << (12);
    v_stack_m1F0 = result;
    result = MmGetTotalCommitLimit((uint16_t)((uint16_t)(result)), (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = (result) << (12);
    v_stack_m1E0 = result;
    result = MmGetPeakCommitment((uint16_t)((uint16_t)(result)), (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = (result) << (12);
    v_stack_m1D8 = result;
    result = MmGetSharedCommit((uint16_t)((uint16_t)(result)), (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    result = (result) << (12);
    v_stack_m1E8 = result;
    result = v_stack_m208;
    if (v_stack_m208 < v_stack_m200) { result = v_stack_m200; }
    v_stack_m208 = result;
    result = v_stack_m1E0;
    if (v_stack_m1E0 < v_stack_m1F0) { result = v_stack_m1F0; }
    v_stack_m1E0 = result;
    result = v_stack_m1D8;
    if (v_stack_m1D8 < v_stack_m1F0) { result = v_stack_m1F0; }
    v_stack_m1D8 = result;
    *(uint64_t *)(local_rdi + 0x80) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x80 + 0x10) = v_xmm1;
    *(uint64_t *)(local_rdi + 0x80 + 0x20) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x80 + 0x30) = v_xmm0;
    v_stack_m3B4 = 56;
    goto loc_00A5B79F;
loc_00A5AAAA:
    local_rbx = (uint32_t)(((uint16_t)(result)) - (183));
    if (condition_is_equal) goto loc_00A5AC08;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5AB66;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5AB56;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5AB0E;
    if (((uint32_t)(local_rbx)) != 0) goto loc_00A5B6E3;
    if (((uint32_t)(264 - 8)) != 8) goto loc_00A5B755;
    result = PsQueryActivityModerationUserSettings(v_stack_m208, (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4, v_stack_m2C8);
    v_stack_m3B8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A5B79F;
    *(uint64_t *)(local_rdi + 0x80) = v_stack_m208;
    goto loc_00A5B79F;
loc_00A5AB0E:
    if ((uint32_t)(264 - 8) == 0) goto loc_00A5AB29;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 0;
    goto loc_00A5B755;
loc_00A5AB29:
    v_stack_m302 = (uint8_t)((uint32_t)(0xC0000004ULL));
    v_stack_m3C8 = (uint32_t)((uint32_t)(0xC0000004ULL));
    result = ZwFilterBootOption((uint32_t)((uint32_t)((uint32_t)(0xC0000004ULL))), (uint32_t)(0x10200003ULL), (uint32_t)(0x260000A0ULL), v_stack_m302);
    goto loc_00A5B7BE;
loc_00A5AB56:
    result = sub_008D3420(local_rdi + 128, (uint32_t)((uint32_t)(264 - 8)), (uint32_t)(0x260000A0ULL), v_stack_m302);
    goto loc_00A5B773;
loc_00A5AB66:
    if (((uint32_t)(264 - 8)) == 24) goto loc_00A5AB86;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 24;
    goto loc_00A5B755;
loc_00A5AB86:
    result = MmGetProcessPartitionId(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), (uint32_t)((uint32_t)(264 - 8)), (uint32_t)(0x260000A0ULL), v_stack_m302);
    result = MmGetNumberOfPhysicalPages((uint16_t)(result), (uint32_t)((uint32_t)(264 - 8)), (uint32_t)(0x260000A0ULL), v_stack_m302);
    result = (result) << (12);
    v_stack_m208 = result;
    result = MmGetLowestPhysicalPage((uint16_t)((uint16_t)(result)), (uint32_t)((uint32_t)(264 - 8)), (uint32_t)(0x260000A0ULL), v_stack_m302);
    result = (result) << (12);
    v_stack_m200 = result;
    result = MmGetHighestPhysicalPage((uint16_t)((uint16_t)(result)), (uint32_t)((uint32_t)(264 - 8)), (uint32_t)(0x260000A0ULL), v_stack_m302);
    result = (result) << (12);
    result = (result) + (0xFFFULL);
    v_stack_m1F8 = result;
    *(uint64_t *)(local_rdi + 0x80) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x80 + 0x10) = v_xmm0;
loc_00A5ABF6:
    v_stack_m3B4 = 24;
    goto loc_00A5B79F;
loc_00A5AC08:
    if (((uint32_t)(264 - 8)) != 16) goto loc_00A5B755;
    v_stack_m218 = *(uint64_t *)(local_rdi + 0x80);
    v_stack_m228 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x80 + 0x8)));
    result = ExpQueryCodeIntegrityCertificateInfo(*(uint64_t *)(local_rdi + 0x80), (uint32_t)(*(uint32_t *)(local_rdi + 0x80 + 0x8)), (uint32_t)(0x260000A0ULL), v_stack_m302);
    goto loc_00A5B773;
loc_00A5AC36:
    if (((uint32_t)((uint16_t)(result))) > 222) goto loc_00A5B2A9;
    if (((uint32_t)((uint16_t)(result))) == 222) goto loc_00A5B274;
    if (((uint32_t)((uint16_t)(result))) > 202) goto loc_00A5AFCF;
    if (((uint32_t)((uint16_t)(result))) == 202) goto loc_00A5AF4E;
    if (((uint32_t)((uint16_t)(result))) > 196) goto loc_00A5ADEC;
    if (((uint32_t)((uint16_t)(result))) == 196) goto loc_00A5ADD7;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint16_t)(result)))) - (190));
    if (condition_is_equal) goto loc_00A5B6ED;
    Arg1 = (uint32_t)((Arg1) - (0));
    if (condition_is_equal) goto loc_00A5ADA9;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5ACF3;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5ACC9;
    if (Arg1 != 1) goto loc_00A5B6E3;
    if (((uint32_t)(264 - 8)) >= 8) goto loc_00A5ACB8;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 8;
    goto loc_00A5B755;
loc_00A5ACB8:
    result = ExpGetSystemWriteConstraintInformation(local_rdi + 128, (uint32_t)(*(uint32_t *)(local_rdi + 0x80 + 0x8)), (uint32_t)(0x260000A0ULL), v_stack_m302);
    v_stack_m3B8 = (uint32_t)(result);
    goto loc_00A5B0A7;
loc_00A5ACC9:
    v_stack_m3C0 = (uint8_t)(v_stack_m3B0);
    v_stack_m3C8 = v_stack_m3B4;
    result = VslTransformDumpKey(v_stack_m3A0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128, (uint32_t)((uint32_t)(264 - 8)));
    goto loc_00A5B773;
loc_00A5ACF3:
    result = KeQueryActiveGroupCount(v_stack_m3A0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128, (uint32_t)((uint32_t)(264 - 8)));
    result = (uint32_t)(((uint16_t)(result)) << (3));
    v_stack_m3B4 = (uint32_t)(result);
    if (((uint32_t)(264 - 8)) < ((uint32_t)(result))) goto loc_00A590DF;
    Arg2 = 0;
    result = memset(local_rdi + 128, Arg2, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(264 - 8)));
loc_00A5AD1F:
    v_stack_m3A8 = 0;
    if (0 >= ((uint32_t)(*(uint16_t *)(v_rip + 0x56A2D6)))) goto loc_00A5AD96;
    result = KeInitializeSchedulerSubNodeEnumerationContext(v_stack_m58, *(uint64_t *)(v_rip + 0x574988 + 0x0 * 8), 0, (uint32_t)((uint32_t)(264 - 8)));
loc_00A5AD49:
    result = KeEnumerateNextSchedulerSubNodeInNode(v_stack_m58, v_stack_m258, 0, (uint32_t)((uint32_t)(264 - 8)));
    if ((uint32_t)(result) != 0) goto loc_00A5AD8D;
    v_stack_m394 = (uint16_t)(*(uint16_t *)(v_stack_m258 + 0x88));
    Arg2 = (*(uint64_t *)(v_stack_m258 + 0x10)) | (*(uint64_t *)(local_rdi + 0x80 + v_stack_m394 * 8));
    *(uint64_t *)(local_rdi + 0x80 + v_stack_m394 * 8) = Arg2;
    goto loc_00A5AD49;
loc_00A5AD8D:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m3A8)) + 1);
    goto loc_00A5AD1F;
loc_00A5AD96:
    goto loc_00A5B79F;
loc_00A5ADA9:
    if (((uint32_t)(264 - 8)) >= 32) goto loc_00A5ADCA;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 32;
    goto loc_00A5B755;
loc_00A5ADCA:
    result = ExpGetSystemFlushInformation(local_rdi + 128, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(264 - 8)));
    goto loc_00A5A27E;
loc_00A5ADD7:
    result = KeQueryKvaShadowInformation(local_rdi + 128, (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4, (uint32_t)((uint32_t)(264 - 8)));
    goto loc_00A5B773;
loc_00A5ADEC:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (197));
    if (condition_is_equal) goto loc_00A5AF1A;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5AE45;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5B6ED;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5AE2B;
    if (Arg1 != 1) goto loc_00A5B6E3;
    result = KeQuerySpeculationControlInformation(local_rdi + 128, (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4, (uint32_t)((uint32_t)(264 - 8)));
    goto loc_00A5B773;
loc_00A5AE2B:
loc_00A5AE30:
    result = IoQuerySystemDeviceName(200, local_rdi + 128, (uint32_t)((uint32_t)(264 - 8)), v_stack_m3B4);
    goto loc_00A5B773;
loc_00A5AE45:
    Arg3 = 0;
    Arg2 = 0;
    result = guard_dispatch_icall(Arg2 + 34, Arg2, Arg3, v_stack_m398);
    v_stack_m3B8 = (uint32_t)(result);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC0000004ULL)))) goto loc_00A5AE77;
loc_00A5AE6D:
    goto loc_00A5B7BE;
loc_00A5AE77:
    if (((uint32_t)(264 - 8)) < v_stack_m398) goto loc_00A59301;
    if (local_rdi + 128 == 0) goto loc_00A59301;
    if ((uint8_t)(v_stack_m3B0) == 0) goto loc_00A5AEB9;
    result = ExAllocatePool2(257, (uint32_t)(v_stack_m398), (uint32_t)(0x6F666E49ULL), v_stack_m398);
    v_stack_m3A0 = result;
    if (result != 0) goto loc_00A5AEC1;
    goto loc_00A594F9;
loc_00A5AEB9:
    v_stack_m3A0 = local_rdi + 128;
loc_00A5AEC1:
    result = guard_dispatch_icall(34, (uint32_t)(v_stack_m398), local_rdi + 128, v_stack_m3B4);
    v_stack_m3B8 = (uint32_t)(result);
    if ((uint8_t)(v_stack_m3B0) == 0) goto loc_00A5B79F;
    if (sign_flag) goto loc_00A592F4;
    result = memcpy(local_rdi + 128, local_rdi + 128, (uint32_t)(v_stack_m3B4), v_stack_m3B4);
    goto loc_00A592F4;
loc_00A5AF1A:
    v_stack_m3B4 = 8;
    if (((uint32_t)(local_rdi + 128)) < 8) goto loc_00A589BB;
    Arg1 = 0;
    *(uint64_t *)(local_rdi + 0x80) = 0;
    *(uint64_t *)(local_rdi + 0x80) = *(uint64_t *)(v_rip + 0x3D2C45);
    goto loc_00A5B79F;
loc_00A5AF4E:
    v_stack_m3B4 = (uint32_t)((uint32_t)(0xC0000004ULL));
    if (((uint32_t)(local_rdi + 128)) == ((uint32_t)((uint32_t)(0xC0000004ULL)))) goto loc_00A5AF6E;
    if (Arg6 == 0) goto loc_00A589BB;
    *(uint32_t *)(Arg6) = (uint32_t)((uint32_t)(0xC0000004ULL));
    goto loc_00A589BB;
loc_00A5AF6E:
    v_stack_m2B4 = 0;
    result = guard_dispatch_icall(48, (uint32_t)((uint32_t)((uint32_t)(0xC0000004ULL))), v_stack_m208, v_stack_m2B4);
    v_stack_m3B8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A58BFB;
    if (v_stack_m2B4 != ((uint32_t)((uint32_t)(0xC0000004ULL)))) goto loc_00A58BFB;
    *(uint8_t *)(local_rdi + 0x80) = (uint8_t)(v_stack_m208);
    goto loc_00A5B79F;
loc_00A5AFCF:
    if (((uint32_t)(v_stack_m3B0)) > 211) goto loc_00A5B0EE;
    if (((uint32_t)(v_stack_m3B0)) == 211) goto loc_00A5B0B9;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m3B0))) - (206));
    if (condition_is_equal) goto loc_00A5B075;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5B043;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5B02E;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5B6ED;
    if (Arg1 != 1) goto loc_00A5B6E3;
    v_stack_m3C8 = v_stack_m3B4;
    result = CmQuerySingleFeatureConfiguration(v_stack_m3A0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B02E:
    result = SeSecurityModelQueryInformation(local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)), v_stack_m3B4, (uint32_t)((uint32_t)(local_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B043:
    if (((uint32_t)(local_rdi + 128)) == 4) goto loc_00A5B063;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 4;
    goto loc_00A5B755;
loc_00A5B063:
    *(uint32_t *)(local_rdi + 0x80) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x569357)));
    goto loc_00A57FDB;
loc_00A5B075:
    if (((uint32_t)(local_rdi + 128)) == 8) goto loc_00A5B095;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 8;
    goto loc_00A5B755;
loc_00A5B095:
    result = ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x4A3D9C))) != 0) ? 1 : 0;
    *(uint8_t *)(local_rdi + 0x80) = (uint8_t)(result);
    *(uint32_t *)(local_rdi + 0x80 + 0x4) = 0;
loc_00A5B0A7:
    v_stack_m3B4 = 8;
    goto loc_00A5B79F;
loc_00A5B0B9:
    v_stack_m3C0 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m3C8 = v_stack_m3B4;
    result = CmQueryFeatureConfigurationSections(v_stack_m3A0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B0EE:
    local_rbx = (uint32_t)((v_stack_m3B0) - (213));
    if (condition_is_equal) goto loc_00A5B25F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5B209;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5B1B5;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5B18C;
    if (((uint32_t)(local_rbx)) != 5) goto loc_00A5B6E3;
    if (((uint32_t)(local_rdi + 128)) == 4) goto loc_00A5B13A;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 4;
    goto loc_00A5B755;
loc_00A5B13A:
    result = 0;
    *(uint32_t *)(local_rdi + 0x80) = 0;
    result = KeIsCetCapable(v_stack_m3A0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)));
    Arg1 = (uint32_t)(((uint8_t)(result)) & ((uint32_t)((uint32_t)(0xC0000004ULL))));
    *(uint32_t *)(local_rdi + 0x80) = Arg1;
    result = KeIsUserCetAllowed(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)));
    local_rbx = (uint32_t)(((uint8_t)(result)) + ((uint32_t)((uint8_t)(result))));
    local_rbx = (uint32_t)((local_rbx) ^ (Arg1));
    local_rbx = (uint32_t)((local_rbx) & (32));
    local_rbx = (uint32_t)((local_rbx) ^ (Arg1));
    *(uint32_t *)(local_rdi + 0x80) = (uint32_t)(local_rbx);
    result = KeIsKernelCetEnabled(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)));
    Arg2 = (uint32_t)(((uint8_t)(result)) & ((uint32_t)((uint32_t)(0xC0000004ULL))));
    Arg2 = (uint32_t)((Arg2) << (8));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(local_rbx)));
    *(uint32_t *)(local_rdi + 0x80) = (uint32_t)(Arg2);
    result = KeIsKernelCetAuditModeEnabled(Arg1, Arg2, local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)));
    Arg1 = (uint32_t)(((uint8_t)(result)) & ((uint32_t)((uint32_t)(0xC0000004ULL))));
    Arg1 = (uint32_t)((Arg1) << (9));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(Arg2)));
    *(uint32_t *)(local_rdi + 0x80) = Arg1;
    goto loc_00A57FDB;
loc_00A5B18C:
    v_stack_m3B4 = 32;
    if (((uint32_t)(local_rdi + 128)) != 32) goto loc_00A589BB;
    result = WheaQuerySystemInformation(local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)), local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)));
    goto loc_00A57FA3;
loc_00A5B1B5:
    if (v_stack_m3B0 == 0) goto loc_00A5B1C9;
loc_00A5B1BC:
    v_stack_m3B8 = 0xC0000061ULL;
    goto loc_00A5B79F;
loc_00A5B1C9:
    if (*(uint64_t *)(v_rip + 0x4A3E58) != 0) goto loc_00A5B1E2;
loc_00A5B1D5:
    v_stack_m3B8 = 0xC000000EULL;
    goto loc_00A5B79F;
loc_00A5B1E2:
    v_stack_m3B4 = 24;
    if (((uint32_t)(local_rdi + 128)) < 24) goto loc_00A589BB;
    *(uint64_t *)(local_rdi + 0x80) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x80 + 0x10) = v_xmm1;
    goto loc_00A5B79F;
loc_00A5B209:
    if (v_stack_m3B0 == 0) goto loc_00A5B21A;
loc_00A5B210:
    goto loc_00A5B7BE;
loc_00A5B21A:
    if (*(uint64_t *)(v_rip + 0x4A3DFF) == 0) goto loc_00A5B79F;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x4A3DFF))) == 0) goto loc_00A5B79F;
    v_stack_m3B4 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x4A3DFF))));
    if (local_rdi + 128 == 0) goto loc_00A5B79F;
    if (((uint32_t)(local_rdi + 128)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x4A3DFF)))))) goto loc_00A589BB;
    Arg2 = (*(uint64_t *)(v_rip + 0x4A3DFF)) + (8);
loc_00A5B24F:
    result = memcpy(local_rdi + 128, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x4A3DFF))), (uint32_t)((uint32_t)(local_rdi + 128)));
    goto loc_00A5B79F;
loc_00A5B25F:
    result = KeQuerySecureSpeculationInformation(local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)), v_stack_m3B4, (uint32_t)((uint32_t)(local_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B274:
    v_stack_m3C0 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m3C8 = v_stack_m3B4;
    result = CmQueryBuildVersionInformation(v_stack_m3A0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B2A9:
    if (((uint32_t)(local_rbx)) > 238) goto loc_00A5B4C0;
    if (((uint32_t)(local_rbx)) == 238) goto loc_00A5B4A3;
    if (((uint32_t)(local_rbx)) > ((uint32_t)(238 - 7))) goto loc_00A5B436;
    if (((uint32_t)(local_rbx)) == ((uint32_t)(238 - 7))) goto loc_00A59695;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (223));
    if (condition_is_equal) goto loc_00A5B361;
    Arg1 = (uint32_t)((Arg1) - (4));
    if (condition_is_equal) goto loc_00A5B32B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5B2EE;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00A5A7A6;
loc_00A5B2EE:
    v_stack_m3B4 = (uint32_t)(local_rdi + 128);
    result = KeQueryDpcWatchdogConfiguration(local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)), (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B306:
loc_00A5B311:
    v_stack_m3C8 = v_stack_m2C8;
    result = PsGetSupportedProcessorArchitectures(local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)), (uint32_t)((uint32_t)(local_rdi + 128)), v_stack_m3B4);
    goto loc_00A5A941;
loc_00A5B32B:
    v_stack_m3B4 = (uint32_t)((uint32_t)(0xC0000004ULL));
    if (((uint32_t)(local_rdi + 128)) == ((uint32_t)((uint32_t)(0xC0000004ULL)))) goto loc_00A5B34B;
    if (Arg6 == 0) goto loc_00A589BB;
    *(uint32_t *)(Arg6) = (uint32_t)((uint32_t)(0xC0000004ULL));
    goto loc_00A589BB;
loc_00A5B34B:
    *(uint8_t *)(local_rdi + 0x80) = (uint8_t)((uint32_t)(0xC0000004ULL));
    goto loc_00A5B79F;
loc_00A5B361:
    if (v_stack_m3A0 == 0) goto loc_00A5B6E3;
    v_stack_m3C8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = ExPoolQueryLimits(v_stack_m3A0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128, local_rdi + 128);
    v_stack_m3B8 = (uint32_t)(result);
    if (sign_flag) goto loc_00A5B79F;
    goto loc_00A59EB4;
loc_00A5B3BB:
    if (v_stack_m3B8 != ((uint32_t)((uint32_t)(0xC0000004ULL)))) goto loc_00A59711;
    if (v_stack_m3B4 <= ((uint32_t)(local_rdi + 128))) goto loc_00A5B3D7;
    v_stack_m3B8 = (uint32_t)((uint32_t)(0xC0000004ULL));
    goto loc_00A59711;
loc_00A5B3D7:
    if (v_stack_m2C8 == 0) goto loc_00A5B3F3;
    result = v_stack_m208;
    if (v_stack_m2C8 != v_stack_m208) {
        Arg2 = 0;
        Arg1 = v_stack_m2C8;
        result = ExFreePoolWithTag(Arg1, Arg2, local_rdi + 128, local_rdi + 128);
    }
    result = ExAllocatePool2(257, (uint32_t)(v_stack_m3B4), (uint32_t)(0x6F666E49ULL), local_rdi + 128);
    v_stack_m3A0 = result;
    if (result != 0) goto loc_00A5B421;
    v_stack_m3B8 = 0xC000009AULL;
    goto loc_00A59711;
loc_00A5B421:
    v_stack_m398 = (uint32_t)((uint32_t)(v_stack_m3B4));
    goto loc_00A596D9;
loc_00A5B436:
    local_rbx = (uint32_t)((result) - (232));
    if (condition_is_equal) goto loc_00A58BFB;
    local_rbx = (uint32_t)((local_rbx) - (0));
    if (condition_is_equal) goto loc_00A5B47C;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A5B45A;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00A58BFB;
    goto loc_00A58BF2;
loc_00A5B45A:
    v_stack_m3C8 = v_stack_m3B4;
    result = HvlQuerySetBootPagesInfo(local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)), v_stack_m3B0, (uint8_t)((uint32_t)(0xC0000004ULL)));
    goto loc_00A5B773;
loc_00A5B47C:
    v_stack_m3B4 = (uint32_t)((uint32_t)(0x4298ULL));
    if (((uint32_t)(local_rdi + 128)) < ((uint32_t)((uint32_t)(0x4298ULL)))) goto loc_00A589BB;
    result = HvlQueryMinrootInfo(local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)), v_stack_m3B4, (uint8_t)((uint32_t)(0xC0000004ULL)));
    goto loc_00A5B773;
loc_00A5B4A3:
    v_stack_m3C8 = v_stack_m3B4;
    result = ExpQueryOriginalImageFeatureInformation(local_rdi + 128, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B4C0:
    if (((uint32_t)(local_rbx)) > 247) goto loc_00A5B6C1;
    if (((uint32_t)(local_rbx)) == 247) goto loc_00A5B685;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (239));
    if (condition_is_equal) goto loc_00A5B663;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5B641;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5B6ED;
    Arg1 = (uint32_t)((Arg1) - (0));
    if (condition_is_equal) goto loc_00A5B5F7;
    if (Arg1 != 1) goto loc_00A5B6E3;
loc_00A5B505:
    if ((uint32_t)((uint32_t)(v_stack_m390)) != 0) goto loc_00A589BB;
    result = MmEnumerateBadPages(v_stack_m290, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)));
    if (v_stack_m290 == 0) goto loc_00A5B561;
    Arg1 = (*(uint64_t *)(v_stack_m290)) & (0);
    if (Arg1 <= 0x1FFFFFFFULL) goto loc_00A5B556;
    goto loc_00A5B561;
loc_00A5B556:
    v_stack_m3B4 = (uint32_t)(Arg1 * 8);
loc_00A5B561:
    local_r12 = (uint32_t)((uint32_t)((uint32_t)(0xC0000004ULL)));
    if (((uint32_t)(local_rdi + 128)) < ((uint32_t)(Arg1 * 8))) { local_r12 = (uint32_t)((uint32_t)(0xC0000004ULL)); }
    v_stack_m3B8 = (uint32_t)(local_r12);
    if (v_stack_m290 == 0) goto loc_00A5B79F;
    if (sign_flag) goto loc_00A5B5E8;
    if (((uint32_t)(local_rbx)) != 128) goto loc_00A5B5CC;
    if (Arg1 == 0) goto loc_00A5B5BE;
loc_00A5B594:
    result = v_stack_m290 + 8;
    if (!(condition_is_below)) {
        Arg4 = (*(uint64_t *)(v_stack_m290 + 0x8)) & (v_stack_m3A0);
        *(void **)(v_stack_m290 + 0x8) = Arg4;
        *(void **)(v_stack_m290 + 0x8) = Arg4;
        result = (v_stack_m290 + 8) + (8);
    }
    Arg3 = (v_stack_m290 + 8) + (8);
    Arg1 = (Arg1) - (1);
    if (condition_is_not_equal) goto loc_00A5B594;
loc_00A5B5BE:
    result = (result) - (v_stack_m290);
    result = (result) - (8);
    result = (uint32_t)((result) & (0xFFFFFFF8ULL));
    v_stack_m3B4 = (uint32_t)(result);
loc_00A5B5CC:
    Arg2 = (v_stack_m290) + (8);
    result = memcpy(local_rdi + 128, Arg2, (uint32_t)(v_stack_m3B4), Arg4);
    goto loc_00A5B5E8;
loc_00A5B5E8:
    Arg2 = 0;
    goto loc_00A5955C;
loc_00A5B5F7:
    v_stack_m3B4 = 16;
    if (((uint32_t)(local_rdi + 128)) < 16) goto loc_00A589BB;
    result = VslQueryTrustedAppRuntimeInformation(v_stack_m208, Arg2, (uint32_t)(v_stack_m3B4), Arg4);
    v_stack_m3B8 = (uint32_t)(result);
    if (sign_flag) {
        v_stack_m3B8 = 0;
    }
    *(uint64_t *)(local_rdi + 0x80) = v_xmm0;
    goto loc_00A5B79F;
loc_00A5B641:
    v_stack_m3C8 = v_stack_m3B4;
    result = ExpQuerySystemMemoryNumaPerformanceInformation(v_stack_m3A0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B663:
    v_stack_m3C8 = v_stack_m3B4;
    result = ExpQuerySystemMemoryNumaInformation(v_stack_m3A0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B685:
    if (v_stack_m3B0 != 0) goto loc_00A5B1BC;
    if (*(uint64_t *)(v_rip + 0x4A3999) == 0) goto loc_00A5B1D5;
    v_stack_m3B4 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x4A3999) + 0x4)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x4A3999) + 0x4)) * 2 * 8 + 8);
    if (((uint32_t)(local_rdi + 128)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x4A3999) + 0x4)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x4A3999) + 0x4)) * 2 * 8 + 8))) goto loc_00A589BB;
    goto loc_00A5B24F;
loc_00A5B6C1:
    Arg1 = (uint32_t)((1) - (250));
    if (condition_is_equal) goto loc_00A5B779;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_r12)));
    if (condition_is_equal) goto loc_00A5B737;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5B737;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A5B710;
    if (Arg1 == ((uint32_t)(local_r12))) goto loc_00A5B6ED;
loc_00A5B6E3:
    goto loc_00A5B7BE;
loc_00A5B6ED:
    v_stack_m3C0 = v_stack_m3B4;
    v_stack_m3C8 = (uint32_t)(local_rdi + 128);
    result = SeCodeIntegrityQueryPolicyInformation(1, v_stack_m3A0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128);
    goto loc_00A5B773;
loc_00A5B710:
    v_stack_m3C0 = (uint8_t)(v_stack_m3B0);
    v_stack_m3C8 = v_stack_m3B4;
    result = ExpQueryRuntimeAttestationReport(v_stack_m3A0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m390))), local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)));
    goto loc_00A5B773;
loc_00A5B737:
    if (((uint32_t)(v_stack_m3B0)) != 253) goto loc_00A5B75C;
    if (((uint32_t)(local_rdi + 128)) >= 12) goto loc_00A5B75C;
    if (Arg6 == 0) goto loc_00A5B755;
    *(uint32_t *)(Arg6) = 12;
    goto loc_00A5B755;
loc_00A5B755:
    goto loc_00A5B7BE;
loc_00A5B75C:
    v_stack_m3C8 = (uint32_t)(v_stack_m3B0);
    Arg4 = 0;
loc_00A5B769:
    result = ExpGetProcessInformation(local_rdi + 128, (uint32_t)((uint32_t)(local_rdi + 128)), v_stack_m3B4, Arg4);
loc_00A5B773:
    v_stack_m3B8 = (uint32_t)(result);
    goto loc_00A5B79F;
loc_00A5B779:
    v_stack_m3B4 = 16;
    if (((uint32_t)(local_rdi + 128)) < 16) goto loc_00A589BB;
    if ((((uint8_t)(local_rdi + 128)) & (7)) != 0) goto loc_00A589BB;
    *(uint64_t *)(local_rdi + 0x80) = v_xmm0;
loc_00A5B79F:
    if (Arg6 == 0) goto loc_00A5B7B1;
    *(uint32_t *)(Arg6) = (uint32_t)((uint32_t)(v_stack_m3B4));
    goto loc_00A5B7B1;
loc_00A5B7B1:
    goto loc_00A5B7BE;
loc_00A5B7B9:
loc_00A5B7BE:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)((uint32_t)(local_rdi + 128)), v_stack_m3B4, Arg4);
    local_rsp = (local_rsp) + (944);
    return result;
loc_00A5B7E2:
    result = ExRaiseDatatypeMisalignment(Arg1, (uint32_t)((uint32_t)(local_rdi + 128)), v_stack_m3B4, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `- 0x10` | `128` | `R` |
| `Arg4` | `+ 0x0` | `8` | `W` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `W` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x0` | `128` | `R` |
| `Arg4` | `+ 0x0` | `128` | `W` |
| `Arg4` | `+ 0x0 + rax*4` | `32` | `W` |
| `Arg4` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg4` | `+ 0x0 + rax*8` | `64` | `W` |
| `Arg4` | `+ 0x1` | `8` | `W` |
| `Arg4` | `+ 0x2` | `8` | `W` |
| `Arg4` | `+ 0x4` | `32` | `R` |
| `Arg4` | `+ 0x4` | `32` | `R/W` |
| `Arg4` | `+ 0x4` | `32` | `W` |
| `Arg4` | `+ 0x7` | `8` | `W` |
| `Arg4` | `+ 0x8` | `8` | `W` |
| `Arg4` | `+ 0x8` | `16` | `W` |
| `Arg4` | `+ 0x8` | `32` | `R` |
| `Arg4` | `+ 0x8` | `32` | `W` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `W` |
| `Arg4` | `+ 0xA` | `16` | `W` |
| `Arg4` | `+ 0xC` | `32` | `W` |
| `Arg4` | `+ 0x10` | `8` | `W` |
| `Arg4` | `+ 0x10` | `32` | `W` |
| `Arg4` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x10` | `64` | `W` |
| `Arg4` | `+ 0x10` | `128` | `R` |
| `Arg4` | `+ 0x14` | `32` | `W` |
| `Arg4` | `+ 0x18` | `32` | `W` |

추가 오프셋 21개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A57858&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
